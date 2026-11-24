# -*- coding: utf-8 -*-
r"""
Shared pipeline for Digital SAT Real Past Exams (2024-2025) on TonyEnglish.
- Creates & maintains folder structure under Digital SAT 1500+ (`871fdd8e-96a4-4e4b-92a2-2cd41021ee82`):
    🏛️ Real Past Exams (2024–2025)
      ├── 📖 Real Exams — Reading & Writing (2025)
      └── 📐 Real Exams — Math (2024–2025)
- Validates every SAT-Bluebook Adaptive Mock / Real Exam JSON:
    - Exact schema compliance with `src/SatBluebookTest.tsx`
    - KaTeX hygiene (`\(...\)` / `\[...\]` only — never raw `$x$` colliding with `$145` currency)
    - Balanced/verified MCQ & SPR answers (`acceptedAnswers` + `correctDisplay`)
    - Bilingual Vietnamese/English `explanation` (`summaryVi`, `keyTakeaway`, `desmosTipVi`, `optionAnalysis`)
- Idempotently publishes to Supabase `tests` table and records IDs in `scripts/sat_real_exams_ids.json`.
"""

import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.request

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENV_PATH = os.path.join(ROOT_DIR, '.env')
IDS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'sat_real_exams_ids.json')

SAT_COURSE_ID = '871fdd8e-96a4-4e4b-92a2-2cd41021ee82'

_env = dict(
    l.strip().split('=', 1)
    for l in open(ENV_PATH, encoding='utf-8')
    if '=' in l and not l.startswith('#')
)
SB_BASE = _env['VITE_SUPABASE_URL'].rstrip('/') + '/rest/v1/'
SB_KEY = _env['VITE_SUPABASE_ANON_KEY']


def _hdr(json_body=False):
    h = {'apikey': SB_KEY, 'Authorization': f'Bearer {SB_KEY}'}
    if json_body:
        h['Content-Type'] = 'application/json'
        h['Prefer'] = 'return=representation'
    return h


def sb_get(path):
    req = urllib.request.Request(SB_BASE + path, headers=_hdr(False))
    return json.loads(urllib.request.urlopen(req, timeout=30).read().decode('utf-8'))


def sb_post(table, payload):
    body = json.dumps(payload, ensure_ascii=False).encode('utf-8')
    req = urllib.request.Request(SB_BASE + table, data=body, method='POST', headers=_hdr(True))
    try:
        return json.loads(urllib.request.urlopen(req, timeout=30).read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"POST {table} failed ({e.code}): {e.read().decode('utf-8', errors='replace')}")


def sb_patch(path, payload):
    body = json.dumps(payload, ensure_ascii=False).encode('utf-8')
    req = urllib.request.Request(SB_BASE + path, data=body, method='PATCH', headers=_hdr(True))
    try:
        return json.loads(urllib.request.urlopen(req, timeout=30).read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"PATCH {path} failed ({e.code}): {e.read().decode('utf-8', errors='replace')}")


def load_ids():
    if os.path.exists(IDS_PATH):
        return json.load(open(IDS_PATH, encoding='utf-8'))
    return {'course_id': SAT_COURSE_ID, 'folders': {}, 'tests': {}}


def save_ids(data):
    with open(IDS_PATH, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def ensure_real_exam_folders():
    """Idempotently creates the Real Past Exams folder tree in Digital SAT 1500+."""
    ids = load_ids()
    existing = sb_get(f'folders?course_id=eq.{SAT_COURSE_ID}&select=id,title,parent_id,display_order')

    def _upsert_folder(key, title, parent_id, order):
        for r in existing:
            if (r.get('title') or '').strip() == title.strip() and r.get('parent_id') == parent_id:
                ids['folders'][key] = r['id']
                return r['id']
        created = sb_post('folders', {
            'course_id': SAT_COURSE_ID,
            'title': title,
            'parent_id': parent_id,
            'display_order': order,
        })
        fid = created[0]['id']
        existing.append(created[0])
        ids['folders'][key] = fid
        print(f"  [CREATED FOLDER] {title} ({fid})", flush=True)
        return fid

    root_id = _upsert_folder('real_root', '🏛️ Real Past Exams (2024–2025)', None, 4)
    _upsert_folder('real_rw', '📖 Real Exams — Reading & Writing (2025)', root_id, 1)
    _upsert_folder('real_math', '📐 Real Exams — Math (2024–2025)', root_id, 2)
    save_ids(ids)
    return ids['folders']


def validate_sat_bluebook_json(cj, label=''):
    """Validates SAT-Bluebook JSON schema, KaTeX balance, options/SPR completeness, and explanations."""
    errs = []
    if cj.get('mode') not in ('adaptive_mock', 'drill'):
        errs.append(f'{label}: invalid mode {cj.get("mode")}')
    section = cj.get('section', 'rw')
    mod_keys = ['drillModule'] if cj.get('mode') == 'drill' else ['module1', 'module2_hard', 'module2_lower']
    all_katex_texts = []
    for mk in mod_keys:
        mod = cj.get(mk)
        if not mod:
            errs.append(f'{label}: missing {mk}')
            continue
        qs = mod.get('questions') or []
        if not qs:
            errs.append(f'{label}.{mk}: empty questions list')
        seen_ids = set()
        for q in qs:
            qid = str(q.get('id') or '')
            if not qid or qid in seen_ids:
                errs.append(f'{label}.{mk}: missing/duplicate id {qid}')
            seen_ids.add(qid)
            fmt = q.get('questionFormat', 'mcq')
            if fmt == 'mcq':
                opts = q.get('options') or []
                if len(opts) != 4:
                    errs.append(f'{label}.{mk} Q{q.get("number")}: expected 4 options, got {len(opts)}')
                labels = [o.get('label') for o in opts]
                if labels != ['A', 'B', 'C', 'D']:
                    errs.append(f'{label}.{mk} Q{q.get("number")}: bad option labels {labels}')
                texts = [str(o.get('text') or '').strip() for o in opts]
                if any(not t for t in texts):
                    errs.append(f'{label}.{mk} Q{q.get("number")}: blank option text')
                if q.get('correctAnswer') not in ('A', 'B', 'C', 'D'):
                    errs.append(f'{label}.{mk} Q{q.get("number")}: invalid MCQ answer {q.get("correctAnswer")}')
            elif fmt == 'spr':
                acc = q.get('acceptedAnswers') or []
                if not acc:
                    errs.append(f'{label}.{mk} Q{q.get("number")}: SPR missing acceptedAnswers')
                if not str(q.get('correctAnswer') or '').strip():
                    errs.append(f'{label}.{mk} Q{q.get("number")}: SPR missing correctAnswer')
            else:
                errs.append(f'{label}.{mk} Q{q.get("number")}: unknown format {fmt}')

            exp = q.get('explanation') or {}
            if not (exp.get('summaryVi') or '').strip():
                errs.append(f'{label}.{mk} Q{q.get("number")}: missing explanation.summaryVi')

            # Gather text for KaTeX balance check
            blob = ' '.join([
                str(q.get('stimulusHtml') or ''),
                str(q.get('questionHtml') or ''),
                ' '.join(str(o.get('text') or '') for o in (q.get('options') or [])),
                str(exp.get('summaryVi') or ''),
                str(exp.get('keyTakeaway') or ''),
                str(exp.get('desmosTipVi') or ''),
            ])
            if blob.count('\\(') != blob.count('\\)'):
                errs.append(f'{label}.{mk} Q{q.get("number")}: unbalanced \\( \\)')
            if blob.count('\\[') != blob.count('\\]'):
                errs.append(f'{label}.{mk} Q{q.get("number")}: unbalanced \\[ \\]')
            # Flag raw LaTeX dollar delimiters like $x$ (allowing currency like $145 or $5.50)
            if re.search(r'(?<!\\)\$[a-zA-Z\\]', blob):
                errs.append(f'{label}.{mk} Q{q.get("number")}: raw $ math delimiter detected')
            all_katex_texts.append({'label': f'{label}.{mk} Q{q.get("number")}', 'text': blob})

    # Verify with REAL Node KaTeX
    if not errs and all_katex_texts:
        os.makedirs(os.path.join(ROOT_DIR, 'scratch'), exist_ok=True)
        payload_path = os.path.join(ROOT_DIR, 'scratch', 'igcse_katex_payload.json')
        with open(payload_path, 'w', encoding='utf-8') as f:
            json.dump(all_katex_texts, f, ensure_ascii=False)
        res = subprocess.run(
            ['node', os.path.join(ROOT_DIR, 'scripts', 'igcse_maths_verify_katex.mjs')],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding='utf-8',
        )
        if os.path.exists(payload_path):
            os.remove(payload_path)
        if res.returncode != 0:
            errs.append(f'{label}: KaTeX verification failed:\n{res.stdout}\n{res.stderr}')
    return errs


def upsert_real_sat_test(code, folder_key, title, order_index, content_json):
    """Validates and publishes a Real Past Exam SAT-Bluebook test idempotently to Supabase."""
    errs = validate_sat_bluebook_json(content_json, code)
    if errs:
        raise ValueError(f"Validation failed for {code}:\n" + "\n".join(errs[:20]))

    folders = ensure_real_exam_folders()
    folder_id = folders[folder_key]
    ids = load_ids()
    existing_id = ids.get('tests', {}).get(code)
    if not existing_id:
        rows = sb_get(f'tests?course_id=eq.{SAT_COURSE_ID}&select=id,title')
        for r in rows:
            if (r.get('title') or '').strip() == title.strip():
                existing_id = r['id']
                break

    content_json.setdefault('basicInfo', {})['courseId'] = SAT_COURSE_ID
    payload = {
        'course_id': SAT_COURSE_ID,
        'folder_id': folder_id,
        'title': title,
        'test_type': 'SAT-Bluebook',
        'order_index': order_index,
        'is_published': True,
        'content_json': content_json,
    }
    if existing_id:
        sb_patch(f'tests?id=eq.{existing_id}', payload)
        tid = existing_id
        print(f"  [UPDATED REAL SAT] {title} ({tid})", flush=True)
    else:
        created = sb_post('tests', payload)
        tid = created[0]['id']
        print(f"  [CREATED REAL SAT] {title} ({tid})", flush=True)

    ids.setdefault('tests', {})[code] = tid
    save_ids(ids)
    return tid


if __name__ == '__main__':
    f = ensure_real_exam_folders()
    print("[OK] SAT Real Past Exams folders ready:", f)
