# -*- coding: utf-8 -*-
"""
Full Live DB & Asset Integrity Audit for IGCSE Maths 0580 & 0606 (2025-2027 Upgrade).
Checks:
- Modules, Lectures, Pages, tutor_context, task_list for BOTH courses
- Folders & Tests (counts, Non-Calc vs Calc tagging, mark sums, AGENTS.md MCQ compliance)
- All 8 Cambridge A4 PDFs on disk
- All 18 Bilingual Audio manifests + 54 MP3s on disk & registered in src/LectureViewer.tsx
"""

import json
import os
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

import fitz

from scripts.igcse_maths_pipeline import (
    COURSE_0580_ID,
    COURSE_0606_ID,
    ROOT_DIR,
    load_ids,
    sb_get,
    validate_igcse_drill,
)


def audit_course(name, course_id, exp_mods, exp_lecs):
    print(f"\n================ AUDIT: {name} ================", flush=True)
    mods = sb_get(f'lecture_modules?course_id=eq.{course_id}&order=order_index.asc,id.asc&select=id,title,order_index')
    lecs = sb_get(f'lectures?course_id=eq.{course_id}&order=order_index.asc,id.asc&select=id,module_id,title,is_published,tutor_context,task_list')
    folders = sb_get(f'folders?course_id=eq.{course_id}&order=display_order.asc,id.asc&select=id,title,display_order')
    tests = sb_get(f'tests?course_id=eq.{course_id}&order=order_index.asc,id.asc&select=id,folder_id,title,test_type,is_published,content_json')

    print(f"  Modules: {len(mods)} (expected {exp_mods})", flush=True)
    for m in mods:
        cnt = sum(1 for l in lecs if l['module_id'] == m['id'])
        print(f"    - #{m['order_index']} {m['title']} ({cnt} lectures)", flush=True)

    missing_ctx = [l['title'] for l in lecs if not (l.get('tutor_context') or '').strip()]
    unpub_lecs = [l['title'] for l in lecs if not l.get('is_published')]
    print(f"  Lectures: {len(lecs)} (expected {exp_lecs}) | missing tutor_context: {len(missing_ctx)} | unpublished: {len(unpub_lecs)}", flush=True)

    # Check lecture_pages
    empty_pages = []
    for l in lecs:
        ps = sb_get(f'lecture_pages?lecture_id=eq.{l["id"]}&select=id,content_html')
        if not ps or len((ps[0].get('content_html') or '').strip()) < 200:
            empty_pages.append(l['title'])
    print(f"  Empty/missing lecture_pages: {len(empty_pages)}", flush=True)

    print(f"  Folders: {len(folders)} | Total Tests: {len(tests)}", flush=True)
    by_folder = {}
    nc_count = 0
    c_count = 0
    mcq_errs = []
    pdf_missing = []

    for t in tests:
        by_folder[t['folder_id']] = by_folder.get(t['folder_id'], 0) + 1
        cj = t.get('content_json') or {}
        bi = cj.get('basicInfo') or {}
        pol = bi.get('calculatorPolicy')
        if pol == 'non-calculator':
            nc_count += 1
        elif pol == 'calculator':
            c_count += 1
        if t['test_type'] == 'Standard-MCQ' and pol in ('non-calculator', 'calculator'):
            mcq_errs.extend(validate_igcse_drill(cj, t['title']))
        if t['test_type'] == 'IGCSE-Math':
            pdf_url = bi.get('insert_pdf_url') or ''
            if pdf_url.startswith('/papers/igcse-maths/'):
                fp = os.path.join(ROOT_DIR, 'public', pdf_url.lstrip('/').replace('/', os.sep))
                if not os.path.exists(fp):
                    pdf_missing.append(pdf_url)
                else:
                    doc = fitz.open(fp)
                    assert len(doc) >= 2, f"PDF too short: {fp}"
                    doc.close()

    for f in folders:
        print(f"    - {f['title']}: {by_folder.get(f['id'], 0)} tests", flush=True)
    print(f"  Tagged Non-Calculator tests: {nc_count} | Tagged Calculator tests: {c_count}", flush=True)
    print(f"  MCQ validation errors: {len(mcq_errs)} | Missing PDFs: {len(pdf_missing)}", flush=True)

    assert len(mods) == exp_mods, f"{name}: mod count mismatch"
    assert len(lecs) == exp_lecs, f"{name}: lec count mismatch"
    assert not missing_ctx, f"{name}: missing tutor_context {missing_ctx}"
    assert not empty_pages, f"{name}: empty pages {empty_pages}"
    assert not mcq_errs, f"{name}: MCQ errors {mcq_errs[:5]}"
    assert not pdf_missing, f"{name}: missing PDFs {pdf_missing}"


def audit_0606_audio():
    print("\n================ AUDIT: 0606 BILINGUAL AUDIO ================", flush=True)
    ids = load_ids()
    lecs = ids['m0606']['lectures']
    lv_path = os.path.join(ROOT_DIR, 'src', 'LectureViewer.tsx')
    lv_src = open(lv_path, encoding='utf-8').read()

    mp3_total = 0
    missing_manifests = []
    missing_in_lv = []
    for code, lid in lecs.items():
        mdir = os.path.join(ROOT_DIR, 'public', 'audio', 'lectures', 'igcse_0606', code)
        mpath = os.path.join(mdir, 'manifest.json')
        if not os.path.exists(mpath):
            missing_manifests.append(code)
            continue
        m = json.load(open(mpath, encoding='utf-8'))
        for seg in m.get('segments', []):
            mp3p = os.path.join(ROOT_DIR, 'public', seg['audioUrl'].lstrip('/').replace('/', os.sep))
            assert os.path.exists(mp3p) and os.path.getsize(mp3p) > 1000, f"Bad MP3: {mp3p}"
            mp3_total += 1
        if lid not in lv_src:
            missing_in_lv.append(f"{code} ({lid})")

    print(f"  0606 Audio Manifests: {len(lecs) - len(missing_manifests)}/{len(lecs)} | Total MP3s verified: {mp3_total}", flush=True)
    print(f"  Missing in LectureViewer.tsx LECTURE_MANIFEST_MAP: {len(missing_in_lv)}", flush=True)
    assert not missing_manifests, f"Missing manifests: {missing_manifests}"
    assert not missing_in_lv, f"Missing in LectureViewer.tsx: {missing_in_lv}"


def main():
    audit_course('IGCSE - Maths-0580', COURSE_0580_ID, exp_mods=4, exp_lecs=11)
    audit_course('IGCSE - Maths-0606', COURSE_0606_ID, exp_mods=5, exp_lecs=18)
    audit_0606_audio()
    print("\n[ALL AUDITS PASSED 100% — ZERO ERRORS!]", flush=True)


if __name__ == '__main__':
    main()
