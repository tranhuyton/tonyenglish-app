# -*- coding: utf-8 -*-
"""
Shared pipeline for IGCSE Mathematics (0580) & IGCSE Additional Mathematics (0606)
2025-2027 Upgrade:
- Supabase REST helpers (using VITE_SUPABASE_ANON_KEY)
- Idempotent ID registry (`scripts/igcse_maths_ids.json`)
- StandardMCQTest drill builder & validator (100% compliant with AGENTS.md & KaTeX)
- Cambridge IGCSE A4 Exam Paper PDF generator via PyMuPDF (`fitz.Story` + `DocumentWriter`)
- Bilingual audio generator (`en-US-AndrewNeural` + `vi-VN-HoaiMyNeural`) via `edge-tts`
"""

import asyncio
import json
import os
import re
import subprocess
import sys
import urllib.error
import urllib.request

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ENV_PATH = os.path.join(ROOT_DIR, '.env')
IDS_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'igcse_maths_ids.json')

COURSE_0580_ID = '7211abb0-ccba-479f-92ad-2d218121f717'
COURSE_0606_ID = '0a8d7434-262a-4462-89c1-2b01c6ea1e4e'

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
    url = SB_BASE + path
    req = urllib.request.Request(url, headers=_hdr(False))
    return json.loads(urllib.request.urlopen(req, timeout=30).read().decode('utf-8'))


def sb_post(table, payload):
    url = SB_BASE + table
    body = json.dumps(payload, ensure_ascii=False).encode('utf-8')
    req = urllib.request.Request(url, data=body, method='POST', headers=_hdr(True))
    try:
        return json.loads(urllib.request.urlopen(req, timeout=30).read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"POST {table} failed ({e.code}): {e.read().decode('utf-8', errors='replace')}")


def sb_patch(path, payload):
    url = SB_BASE + path
    body = json.dumps(payload, ensure_ascii=False).encode('utf-8')
    req = urllib.request.Request(url, data=body, method='PATCH', headers=_hdr(True))
    try:
        return json.loads(urllib.request.urlopen(req, timeout=30).read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        raise RuntimeError(f"PATCH {path} failed ({e.code}): {e.read().decode('utf-8', errors='replace')}")


def load_ids():
    if os.path.exists(IDS_PATH):
        with open(IDS_PATH, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}


def save_ids(data):
    with open(IDS_PATH, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)


def upsert_lecture_with_page(
    course_id,
    module_id,
    title,
    order_index,
    content_html,
    tutor_context='',
    task_list=None,
    existing_lecture_id=None,
    id_bucket_key=None,
    code=None,
):
    ids = load_ids()
    if id_bucket_key and code and not existing_lecture_id:
        existing_lecture_id = ids.get(id_bucket_key, {}).get(code)

    if not existing_lecture_id:
        # Check DB by course_id + title to avoid duplicates
        existing = sb_get(f'lectures?course_id=eq.{course_id}&select=id,title')
        for row in existing:
            if (row.get('title') or '').strip() == title.strip():
                existing_lecture_id = row['id']
                break

    lec_payload = {
        'course_id': course_id,
        'module_id': module_id,
        'title': title,
        'order_index': order_index,
        'is_published': True,
        'tutor_context': tutor_context,
    }
    if task_list is not None:
        lec_payload['task_list'] = task_list

    if existing_lecture_id:
        sb_patch(f'lectures?id=eq.{existing_lecture_id}', lec_payload)
        lec_id = existing_lecture_id
        print(f"  [UPDATED LECTURE] {title} ({lec_id})", flush=True)
    else:
        created = sb_post('lectures', lec_payload)
        lec_id = created[0]['id']
        print(f"  [CREATED LECTURE] {title} ({lec_id})", flush=True)

    # Upsert page 1 in lecture_pages
    pages = sb_get(f'lecture_pages?lecture_id=eq.{lec_id}&order=page_number.asc&select=id,page_number')
    if pages:
        sb_patch(f'lecture_pages?id=eq.{pages[0]["id"]}', {'content_html': content_html})
    else:
        sb_post('lecture_pages', {
            'lecture_id': lec_id,
            'page_number': 1,
            'content_html': content_html,
        })

    if id_bucket_key and code:
        ids.setdefault(id_bucket_key, {})[code] = lec_id
        save_ids(ids)
    return lec_id


def upsert_test(course_id, folder_id, title, test_type, order_index, content_json, id_bucket_key=None, code=None):
    ids = load_ids()
    existing_id = None
    if id_bucket_key and code:
        existing_id = ids.get(id_bucket_key, {}).get(code)
    if not existing_id:
        existing = sb_get(f'tests?course_id=eq.{course_id}&select=id,title')
        for row in existing:
            if (row.get('title') or '').strip() == title.strip():
                existing_id = row['id']
                break

    payload = {
        'course_id': course_id,
        'folder_id': folder_id,
        'title': title,
        'test_type': test_type,
        'order_index': order_index,
        'is_published': True,
        'content_json': content_json,
    }
    if isinstance(content_json, dict):
        pdf_u = (content_json.get('basicInfo') or {}).get('insert_pdf_url')
        if pdf_u:
            payload['insert_pdf_url'] = pdf_u
        if content_json.get('questions'):
            payload['json_config'] = {
                'timeLimit': int((content_json.get('basicInfo') or {}).get('timeLimit') or 120),
                'questions': content_json['questions'],
            }

    if existing_id:
        sb_patch(f'tests?id=eq.{existing_id}', payload)
        tid = existing_id
        print(f"  [UPDATED TEST] {title} ({tid})", flush=True)
    else:
        created = sb_post('tests', payload)
        tid = created[0]['id']
        print(f"  [CREATED TEST] {title} ({tid})", flush=True)

    if id_bucket_key and code:
        ids.setdefault(id_bucket_key, {})[code] = tid
        save_ids(ids)
    return tid


# =============================================================================
# STANDARD MCQ / HYBRID DRILL BUILDER & VALIDATOR (100% AGENTS.md compliant)
# =============================================================================
def build_igcse_drill_json(
    title,
    course_id,
    calculator_policy,
    syllabus_code,
    intro_html,
    questions,
    time_limit='35',
):
    """
    questions: list of dicts:
      {
        'q': '<p>...KaTeX \\(...\\)...</p>',
        'options': ['optA', 'optB', 'optC', 'optD'],
        'answer': 'A' | 'B' | 'C' | 'D',
        'explanation': '<p><b>Bước 1 ...</b></p>',
        'tag': 'Surds (Non-Calc)'  # optional
      }
    """
    is_non_calc = calculator_policy == 'non-calculator'
    policy_banner = (
        '<div style="background:#fff1f2;border:1.5px solid #fda4af;border-radius:10px;padding:10px 14px;margin-bottom:12px;color:#9f1239;font-weight:700;">'
        '🚫 NON-CALCULATOR DRILL (Cambridge 2025–2027): Không dùng máy tính cầm tay. Giữ kết quả ở dạng chính xác (căn thức, phân số tối giản, π).'
        '</div>'
        if is_non_calc
        else '<div style="background:#ecfdf5;border:1.5px solid #6ee7b7;border-radius:10px;padding:10px 14px;margin-bottom:12px;color:#065f46;font-weight:700;">'
        '🧮 CALCULATOR ALLOWED DRILL (Cambridge 2025–2027): Được sử dụng máy tính Casio fx-991EX/CW. Làm tròn đáp án đến 3 chữ số có nghĩa (3 s.f.), góc đến 1 d.p.'
        '</div>'
    )

    q_objs = []
    for idx, q in enumerate(questions, start=1):
        tag_html = (
            f'<span style="display:inline-block;font-size:11px;font-weight:800;padding:2px 8px;border-radius:6px;background:#eef2ff;color:#3730a3;margin-bottom:6px;">{q["tag"]}</span>'
            if q.get('tag')
            else ''
        )
        q_html = f'{tag_html}{q["q"]}'
        q_objs.append({
            'id': str(idx),
            'number': idx,
            'content': q_html,
            'options': q['options'],
            'correctAnswer': q['answer'],
            'explanation': q['explanation'],
        })

    return {
        'basicInfo': {
            'title': title,
            'courseId': course_id,
            'skill': f'IGCSE Maths {syllabus_code}',
            'category': 'exercise',
            'timeLimit': str(time_limit),
            'calculatorPolicy': calculator_policy,
            'tags': f'IGCSE {syllabus_code}, {calculator_policy}, 2025-2027',
        },
        'parts': [
            {
                'id': '1',
                'title': '',
                'content': f'<p><b>{title}</b></p>{policy_banner}{intro_html}',
                'audioUrl': '',
                'explanation': '',
                'sections': [
                    {
                        'id': '101',
                        'title': 'Section 1',
                        'questionType': 'Trắc nghiệm',
                        'content': '<p class="font-bold text-[15px] text-slate-700 mb-3">Chọn đáp án đúng nhất (A, B, C hoặc D). Xem lời giải chi tiết chuẩn Cambridge Marking Scheme (M1/A1) sau khi nộp bài.</p>',
                        'questions': q_objs,
                    }
                ],
            }
        ],
    }


def validate_igcse_drill(cj, title=''):
    errs = []
    parts = cj.get('parts') or []
    if len(parts) != 1:
        errs.append(f'{title}: must have exactly 1 part, got {len(parts)}')
        return errs
    secs = parts[0].get('sections') or []
    if not secs:
        errs.append(f'{title}: missing sections')
        return errs
    ans_counts = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
    seen_q = set()
    for s in secs:
        if '<' in (s.get('title') or ''):
            errs.append(f'{title}: HTML forbidden in section.title')
        if s.get('questionType') != 'Trắc nghiệm':
            errs.append(f'{title}: invalid questionType {s.get("questionType")}')
        for q in s.get('questions') or []:
            qid = str(q.get('id') or '')
            if not qid.isdigit():
                errs.append(f'{title}: non-numeric question id {qid}')
            opts = q.get('options') or []
            if len(opts) != 4:
                errs.append(f'{title} Q{qid}: expected 4 options, got {len(opts)}')
            if len(set(o.strip() for o in opts)) != 4:
                errs.append(f'{title} Q{qid}: duplicate options {opts}')
            ans = q.get('correctAnswer')
            if ans not in ans_counts:
                errs.append(f'{title} Q{qid}: invalid answer {ans}')
            else:
                ans_counts[ans] += 1
            if not (q.get('explanation') or '').strip():
                errs.append(f'{title} Q{qid}: missing explanation')
            txt_all = (q.get('content') or '') + ' '.join(opts) + (q.get('explanation') or '')
            if re.search(r'(?<!\\)\$[a-zA-Z0-9\\]', txt_all) and not re.search(r'\$\d', txt_all):
                errs.append(f'{title} Q{qid}: possible raw $ math delimiter')
            if txt_all.count('\\(') != txt_all.count('\\)'):
                errs.append(f'{title} Q{qid}: unbalanced \\( \\)')
            if txt_all.count('\\[') != txt_all.count('\\]'):
                errs.append(f'{title} Q{qid}: unbalanced \\[ \\]')
            stem = (q.get('content') or '').strip()
            if stem in seen_q:
                errs.append(f'{title} Q{qid}: duplicate stem within test')
            seen_q.add(stem)
    # Check reasonable answer balance (each letter >= 1)
    total = sum(ans_counts.values())
    if total >= 12 and min(ans_counts.values()) < 2:
        errs.append(f'{title}: unbalanced answers {ans_counts}')
    return errs


# =============================================================================
# CAMBRIDGE A4 EXAM PAPER PDF GENERATOR (PyMuPDF fitz.Story)
# =============================================================================
def latex_to_pdf_html(text):
    """Converts \\(...\\) and basic LaTeX into crisp HTML math for PyMuPDF Story PDF."""
    if not text:
        return ''
    s = str(text)
    # Strip \( \) and \[ \] wrappers after converting math inside
    def _conv_expr(expr):
        r = expr
        # Nested/simple fractions
        for _ in range(3):
            r = re.sub(r'\\frac\{([^{}]+)\}\{([^{}]+)\}', r'(\1)/(\2)', r)
        r = re.sub(r'\\sqrt\[(\d+)\]\{([^{}]+)\}', r'<sup>\1</sup>√(\2)', r)
        r = re.sub(r'\\sqrt\{([^{}]+)\}', r'√(\1)', r)
        r = re.sub(r'\\binom\{([^{}]+)\}\{([^{}]+)\}', r'C(\1, \2)', r)
        r = re.sub(r'\\int_\{([^{}]+)\}\^\{([^{}]+)\}', r'∫<sub>\1</sub><sup>\2</sup>', r)
        r = re.sub(r'\\vec\{([^{}]+)\}', r'<b>\1</b>', r)
        r = re.sub(r'\\mathbf\{([^{}]+)\}', r'<b>\1</b>', r)
        r = re.sub(r'\\text\{([^{}]+)\}', r'\1', r)
        repls = [
            ('\\pi', 'π'), ('\\theta', 'θ'), ('\\alpha', 'α'), ('\\beta', 'β'),
            ('\\gamma', 'γ'), ('\\delta', 'δ'), ('\\Delta', 'Δ'), ('\\lambda', 'λ'),
            ('\\pm', '±'), ('\\mp', '∓'), ('\\times', '×'), ('\\div', '÷'), ('\\cdot', '·'),
            ('\\leq', '≤'), ('\\geq', '≥'), ('\\neq', '≠'), ('\\approx', '≈'), ('\\equiv', '≡'),
            ('\\infty', '∞'), ('\\int', '∫'), ('\\sum', 'Σ'), ('\\angle', '∠'), ('\\triangle', '△'),
            ('\\perp', '⊥'), ('\\parallel', '∥'), ('\\circ', '°'), ('\\degree', '°'),
            ('\\Rightarrow', '⇒'), ('\\rightarrow', '→'), ('\\implies', '⇒'),
            ('\\in', '∈'), ('\\notin', '∉'), ('\\cap', '∩'), ('\\cup', '∪'),
            ('\\sin', 'sin'), ('\\cos', 'cos'), ('\\tan', 'tan'), ('\\sec', 'sec'),
            ('\\csc', 'cosec'), ('\\cosec', 'cosec'), ('\\cot', 'cot'),
            ('\\ln', 'ln'), ('\\log', 'log'), ('\\quad', '  '), ('\\;', ' '), ('\\,', ' '),
            ('\\left', ''), ('\\right', ''),
        ]
        for k, v in repls:
            r = r.replace(k, v)
        r = re.sub(r'\^\{([^{}]+)\}', r'<sup>\1</sup>', r)
        r = re.sub(r'_\{([^{}]+)\}', r'<sub>\1</sub>', r)
        r = re.sub(r'\^([0-9a-zA-Z\-])', r'<sup>\1</sup>', r)
        r = re.sub(r'_([0-9a-zA-Z])', r'<sub>\1</sub>', r)
        r = r.replace('{', '').replace('}', '')
        return f'<i>{r}</i>'

    s = re.sub(r'\\\[([\s\S]*?)\\\]', lambda m: f'<div class="eq">{_conv_expr(m.group(1))}</div>', s)
    s = re.sub(r'\\\(([\s\S]*?)\\\)', lambda m: _conv_expr(m.group(1)), s)
    return s


def generate_cambridge_exam_pdf(out_rel_path, paper_meta, questions):
    """
    Generates an authentic Cambridge IGCSE A4 Exam Paper PDF using PyMuPDF Story.
    out_rel_path: e.g. 'papers/igcse-maths/0580_p2_noncalc_mock1.pdf' (stored under public/)
    Returns public URL path: '/papers/igcse-maths/...'
    """
    import fitz

    full_path = os.path.join(ROOT_DIR, 'public', out_rel_path.replace('/', os.sep))
    os.makedirs(os.path.dirname(full_path), exist_ok=True)

    is_non_calc = paper_meta['calculator_policy'] == 'non-calculator'
    calc_box = (
        '<div class="banner-noncalc">ELECTRONIC CALCULATORS MUST NOT BE USED IN THIS PAPER.<br/>'
        'Leave all answers in exact form (surds, π, simplified fractions) unless otherwise instructed.</div>'
        if is_non_calc
        else '<div class="banner-calc">ELECTRONIC CALCULATOR ALLOWED (Casio fx-991EX/CW).<br/>'
        'Give non-exact numerical answers correct to 3 significant figures, or 1 decimal place for angles in degrees.</div>'
    )

    formula_html = (
        '<div class="formula-box"><b>OFFICIAL 2025–2027 FORMULA REFERENCE (0580 EXTENDED):</b><br/>'
        'Trapezium: A = ½(a + b)h &nbsp;|&nbsp; Cone CSA: πrl &nbsp;|&nbsp; Cone Vol: ⅓πr²h &nbsp;|&nbsp; '
        'Sphere SA: 4πr², Vol: ⁴⁄₃πr³ &nbsp;|&nbsp; Quadratic: x = (−b ± √(b² − 4ac)) / 2a<br/>'
        'Sine Rule: a/sin A = b/sin B = c/sin C &nbsp;|&nbsp; Cosine Rule: a² = b² + c² − 2bc cos A &nbsp;|&nbsp; '
        'Triangle Area: ½ab sin C</div>'
        if paper_meta['syllabus'] == '0580'
        else '<div class="formula-box"><b>OFFICIAL 2025–2027 FORMULA REFERENCE (0606 ADDITIONAL MATHS):</b><br/>'
        'Quadratic: x = (−b ± √(b² − 4ac)) / 2a &nbsp;|&nbsp; AP: uₙ = a + (n−1)d, Sₙ = (n/2)[2a + (n−1)d] &nbsp;|&nbsp; '
        'GP: uₙ = arⁿ⁻¹, Sₙ = a(1−rⁿ)/(1−r), S∞ = a/(1−r)<br/>'
        'Circle: (x−a)² + (y−b)² = r² &nbsp;|&nbsp; Radians: s = rθ, A = ½r²θ &nbsp;|&nbsp; '
        'Trig: sin²A + cos²A = 1, sec²A = 1 + tan²A, cosec²A = 1 + cot²A</div>'
    )

    q_blocks = []
    total_marks = 0
    for q in questions:
        qnum = q['question_number']
        stem_html = latex_to_pdf_html(q.get('stem') or '')
        sub_html_parts = []
        for sq in q['sub_questions']:
            m = int(sq['max_marks'])
            total_marks += m
            lbl = latex_to_pdf_html(sq['label'])
            lines_needed = 3 if m <= 2 else (5 if m <= 4 else 7)
            work_lines = '<div class="work-space">' + ('<div class="wline">&nbsp;</div>' * lines_needed) + '</div>'
            sub_html_parts.append(
                f'<div class="subq">'
                f'<table class="subq-tbl"><tr><td class="subq-text">{lbl}</td>'
                f'<td class="subq-marks">[{m}]</td></tr></table>'
                f'{work_lines}'
                f'</div>'
            )
        q_blocks.append(
            f'<div class="qblock">'
            f'<div class="qheader">Question {qnum}</div>'
            f'{f"<div class=qstem>{stem_html}</div>" if stem_html else ""}'
            f'{"".join(sub_html_parts)}'
            f'</div>'
        )

    html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  body {{ font-family: Helvetica, Arial, sans-serif; font-size: 10.5pt; color: #111827; line-height: 1.45; }}
  .cover-top {{ border-bottom: 2.5px solid #0f172a; padding-bottom: 8px; margin-bottom: 10px; }}
  .brand {{ font-size: 9pt; font-weight: bold; color: #1e3a8a; letter-spacing: 1px; text-transform: uppercase; }}
  .paper-title {{ font-size: 15pt; font-weight: bold; color: #0f172a; margin: 4px 0; }}
  .paper-meta {{ font-size: 10pt; color: #334155; }}
  .banner-noncalc {{ background-color: #fff1f2; border: 1.5px solid #e11d48; color: #9f1239; padding: 8px 10px; font-weight: bold; font-size: 9.5pt; margin: 10px 0; }}
  .banner-calc {{ background-color: #ecfdf5; border: 1.5px solid #059669; color: #065f46; padding: 8px 10px; font-weight: bold; font-size: 9.5pt; margin: 10px 0; }}
  .formula-box {{ background-color: #f8fafc; border: 1px solid #cbd5e1; padding: 8px 10px; font-size: 8.8pt; color: #1e293b; margin-bottom: 14px; line-height: 1.5; }}
  .qblock {{ margin-bottom: 14px; border-top: 1px solid #e2e8f0; padding-top: 8px; }}
  .qheader {{ font-size: 11.5pt; font-weight: bold; color: #1e3a8a; margin-bottom: 4px; }}
  .qstem {{ margin-bottom: 6px; color: #111827; }}
  .subq {{ margin-bottom: 8px; }}
  .subq-tbl {{ width: 100%; border-collapse: collapse; }}
  .subq-text {{ width: 90%; vertical-align: top; padding-right: 8px; }}
  .subq-marks {{ width: 10%; vertical-align: top; text-align: right; font-weight: bold; color: #0f172a; }}
  .work-space {{ margin-top: 4px; margin-bottom: 4px; }}
  .wline {{ border-bottom: 0.7px dotted #94a3b8; height: 15px; }}
  .eq {{ text-align: center; font-weight: bold; margin: 4px 0; }}
</style>
</head>
<body>
  <div class="cover-top">
    <div class="brand">TONYENGLISH.VN • CAMBRIDGE IGCSE 2025–2027 OFFICIAL-STYLE PRACTICE PAPER</div>
    <div class="paper-title">{paper_meta['title']}</div>
    <div class="paper-meta">Syllabus: <b>{paper_meta['syllabus_name']}</b> &nbsp;|&nbsp; Duration: <b>{paper_meta['time_limit']} minutes</b> &nbsp;|&nbsp; Total Marks: <b>{total_marks}</b></div>
  </div>
  {calc_box}
  {formula_html}
  {"".join(q_blocks)}
</body>
</html>"""

    raw_path = full_path + '.raw.pdf'
    story = fitz.Story(html=html)
    writer = fitz.DocumentWriter(raw_path)
    mediabox = fitz.paper_rect('a4')
    where = mediabox + (42, 42, -42, -48)

    page_num = 0
    more = True
    while more:
        page_num += 1
        dev = writer.begin_page(mediabox)
        more, _ = story.place(where)
        story.draw(dev)
        writer.end_page()
    writer.close()
    del writer
    del story

    # Stamp clean page numbers at bottom of every page and save directly to full_path
    doc = fitz.open(raw_path)
    total_pages = len(doc)
    for idx, page in enumerate(doc, start=1):
        footer = f"{paper_meta['code']} • TonyEnglish.vn (2025–2027 Syllabus)    Page {idx} of {total_pages}"
        page.insert_text((42, mediabox.height - 24), footer, fontsize=8.5, color=(0.4, 0.45, 0.52))
    doc.save(full_path, deflate=True, garbage=3)
    doc.close()
    try:
        os.remove(raw_path)
    except OSError:
        pass
    if os.path.exists(full_path + '.tmp.pdf'):
        try:
            os.remove(full_path + '.tmp.pdf')
        except OSError:
            pass

    fsize = os.path.getsize(full_path)
    print(f"  [PDF OK] {out_rel_path} ({total_pages} pages, {fsize // 1024} KB, {total_marks} marks)", flush=True)
    return '/' + out_rel_path.lstrip('/')


def build_igcse_paper_json(paper_meta, pdf_url, questions):
    """Builds `IGCSE-Math` content_json compatible with `IgcsePaperTest.tsx`."""
    clean_qs = []
    for q in questions:
        stem = (q.get('stem') or '').strip()
        subs = []
        for idx, sq in enumerate(q['sub_questions']):
            lbl = sq['label']
            if idx == 0 and stem:
                lbl = f"{stem}\n{lbl}"
            subs.append({
                'id': sq['id'],
                'type': sq.get('type', 'short_answer'),
                'label': lbl,
                'max_marks': int(sq['max_marks']),
                'marking_scheme': sq['marking_scheme'],
            })
        clean_qs.append({
            'question_number': str(q['question_number']),
            'sub_questions': subs,
        })

    return {
        'basicInfo': {
            'skill': 'IGCSE-Math',
            'title': paper_meta['title'],
            'category': 'test',
            'courseId': paper_meta['course_id'],
            'timeLimit': str(paper_meta['time_limit']),
            'insert_pdf_url': pdf_url,
            'calculatorPolicy': paper_meta['calculator_policy'],
            'tags': f"IGCSE {paper_meta['syllabus']}, {paper_meta['calculator_policy']}, 2025-2027",
        },
        'questions': clean_qs,
    }
