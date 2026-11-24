# -*- coding: utf-8 -*-
"""
Master Verification & Publisher for IGCSE Maths 0580 & 0606 (2025-2027 Upgrade):
1. Runs verify_all_math() on all 6 authored content modules (354 drill Qs + 8 full mocks).
2. Validates every drill with validate_igcse_drill() and checks zero cross-test duplicate stems.
3. Exports every LaTeX string and verifies 100% of expressions with REAL Node KaTeX (throwOnError: true).
4. Generates all 8 Cambridge A4 Exam PDFs under public/papers/igcse-maths/ and verifies via PyMuPDF.
5. Publishes all 35 new Tests (12 for 0580 + 23 for 0606) idempotently to live Supabase.
6. Links every new Drill & Mock cleanly into the `task_list` of ALL 11 (0580) & 18 (0606) lectures!
"""

import json
import os
import subprocess
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

import fitz

from scripts.igcse_maths_pipeline import (
    COURSE_0580_ID,
    COURSE_0606_ID,
    ROOT_DIR,
    build_igcse_drill_json,
    build_igcse_paper_json,
    generate_cambridge_exam_pdf,
    load_ids,
    save_ids,
    sb_get,
    sb_patch,
    upsert_test,
    validate_igcse_drill,
)
from scripts.igcse_0580_drills_2025 import DRILLS_0580_2025, verify_all_math as verify_0580_drills
from scripts.igcse_0580_full_mocks import MOCKS_0580_2025, verify_all_math as verify_0580_mocks
from scripts.igcse_0606_drills_p1 import DRILLS_0606_P1, verify_all_math as verify_0606_p1
from scripts.igcse_0606_drills_p2a import DRILLS_0606_P2A, verify_all_math as verify_0606_p2a
from scripts.igcse_0606_drills_p2b import DRILLS_0606_P2B, verify_all_math as verify_0606_p2b
from scripts.igcse_0606_full_mocks import MOCKS_0606_2025, verify_all_math as verify_0606_mocks


def merge_task_list(existing_list, new_tasks):
    """Preserves existing tasks while idempotently upserting new 2025 tasks by id."""
    out = list(existing_list or [])
    idx_by_id = {t.get('id'): i for i, t in enumerate(out) if isinstance(t, dict) and t.get('id')}
    for nt in new_tasks:
        tid = nt['id']
        if tid in idx_by_id:
            out[idx_by_id[tid]] = nt
        else:
            idx_by_id[tid] = len(out)
            out.append(nt)
    return out


def main():
    print("=== 1. RUNNING PYTHON MATH VERIFICATION ACROSS ALL 6 MODULES ===", flush=True)
    verify_0580_drills()
    verify_0580_mocks()
    verify_0606_p1()
    verify_0606_p2a()
    verify_0606_p2b()
    verify_0606_mocks()
    print("  [OK] All 6 verify_all_math() suites passed!\n", flush=True)

    ids = load_ids()
    katex_items = []
    seen_stems = {}
    all_errors = []

    all_0580_drills_built = []
    all_0606_drills_built = []

    print("=== 2. BUILDING & VALIDATING ALL 27 DRILLS (354 QUESTIONS) ===", flush=True)
    for d in DRILLS_0580_2025:
        cj = build_igcse_drill_json(
            title=d['title'],
            course_id=COURSE_0580_ID,
            calculator_policy=d['calculator_policy'],
            syllabus_code='0580',
            intro_html=d['intro_html'],
            questions=d['questions'],
            time_limit=d.get('time_limit', '30'),
        )
        all_errors.extend(validate_igcse_drill(cj, d['code']))
        for idx, q in enumerate(d['questions'], 1):
            stem = q['q'].strip()
            if stem in seen_stems:
                all_errors.append(f"DUPLICATE STEM: {d['code']} Q{idx} duplicates {seen_stems[stem]}")
            seen_stems[stem] = f"{d['code']} Q{idx}"
            katex_items.append({'label': f"{d['code']} Q{idx}", 'text': q['q'] + ' ' + ' '.join(q['options']) + ' ' + q['explanation']})
        all_0580_drills_built.append((d, cj))

    for d in (DRILLS_0606_P1 + DRILLS_0606_P2A + DRILLS_0606_P2B):
        cj = build_igcse_drill_json(
            title=d['title'],
            course_id=COURSE_0606_ID,
            calculator_policy=d['calculator_policy'],
            syllabus_code='0606',
            intro_html=d['intro_html'],
            questions=d['questions'],
            time_limit=d.get('time_limit', '30'),
        )
        all_errors.extend(validate_igcse_drill(cj, d['code']))
        for idx, q in enumerate(d['questions'], 1):
            stem = q['q'].strip()
            if stem in seen_stems:
                all_errors.append(f"DUPLICATE STEM: {d['code']} Q{idx} duplicates {seen_stems[stem]}")
            seen_stems[stem] = f"{d['code']} Q{idx}"
            katex_items.append({'label': f"{d['code']} Q{idx}", 'text': q['q'] + ' ' + ' '.join(q['options']) + ' ' + q['explanation']})
        all_0606_drills_built.append((d, cj))

    for m in (MOCKS_0580_2025 + MOCKS_0606_2025):
        expected_marks = 100 if m['paper_meta']['syllabus'] == '0580' else 80
        total_marks = sum(int(sq['max_marks']) for q in m['questions'] for sq in q['sub_questions'])
        if total_marks != expected_marks:
            all_errors.append(f"{m['code']}: expected {expected_marks} marks, got {total_marks}")
        for q in m['questions']:
            if q.get('stem'):
                katex_items.append({'label': f"{m['code']} Q{q['question_number']} stem", 'text': q['stem']})
            for sq in q['sub_questions']:
                katex_items.append({'label': f"{m['code']} {sq['id']}", 'text': sq['label'] + ' ' + sq['marking_scheme']})

    if all_errors:
        print("VALIDATION ERRORS DETECTED:", flush=True)
        for e in all_errors:
            print("  -", e, flush=True)
        sys.exit(1)
    print(f"  [OK] Zero validation/duplicate errors across {len(all_0580_drills_built)} (0580) + {len(all_0606_drills_built)} (0606) drills & 8 mocks!\n", flush=True)

    print("=== 3. VERIFYING 100% OF LATEX EXPRESSIONS WITH REAL NODE KATEX ===", flush=True)
    scratch_dir = os.path.join(ROOT_DIR, 'scratch')
    os.makedirs(scratch_dir, exist_ok=True)
    payload_path = os.path.join(scratch_dir, 'igcse_katex_payload.json')
    with open(payload_path, 'w', encoding='utf-8') as f:
        json.dump(katex_items, f, ensure_ascii=False)
    res = subprocess.run(['node', os.path.join(ROOT_DIR, 'scripts', 'igcse_maths_verify_katex.mjs')], check=False)
    if res.returncode != 0:
        print("ABORTING: KaTeX errors found!", flush=True)
        sys.exit(1)
    os.remove(payload_path)
    print("", flush=True)

    print("=== 4. GENERATING ALL 8 CAMBRIDGE A4 EXAM PDFs ===", flush=True)
    mock_payloads_0580 = []
    for m in MOCKS_0580_2025:
        pdf_url = generate_cambridge_exam_pdf(m['pdf_rel_path'], m['paper_meta'], m['questions'])
        full_pdf = os.path.join(ROOT_DIR, 'public', m['pdf_rel_path'].replace('/', os.sep))
        doc = fitz.open(full_pdf)
        assert len(doc) >= 2 and os.path.getsize(full_pdf) > 5000, f"Invalid PDF {full_pdf}"
        doc.close()
        cj = build_igcse_paper_json(m['paper_meta'], pdf_url, m['questions'])
        mock_payloads_0580.append((m, cj))

    mock_payloads_0606 = []
    for m in MOCKS_0606_2025:
        pdf_url = generate_cambridge_exam_pdf(m['pdf_rel_path'], m['paper_meta'], m['questions'])
        full_pdf = os.path.join(ROOT_DIR, 'public', m['pdf_rel_path'].replace('/', os.sep))
        doc = fitz.open(full_pdf)
        assert len(doc) >= 2 and os.path.getsize(full_pdf) > 5000, f"Invalid PDF {full_pdf}"
        doc.close()
        cj = build_igcse_paper_json(m['paper_meta'], pdf_url, m['questions'])
        mock_payloads_0606.append((m, cj))
    print("", flush=True)

    print("=== 5. PUBLISHING ALL 35 TESTS TO LIVE SUPABASE ===", flush=True)
    ids = load_ids()
    f0580 = ids['m0580']['folders']
    f0606 = ids['m0606']['folders']

    pub_0580_drills = {}
    for d, cj in all_0580_drills_built:
        tid = upsert_test(
            course_id=COURSE_0580_ID,
            folder_id=f0580[d['folder_key']],
            title=d['title'],
            test_type='Standard-MCQ',
            order_index=d['order_index'],
            content_json=cj,
            id_bucket_key='tests_0580',
            code=d['code'],
        )
        pub_0580_drills[d['code']] = (tid, d)

    pub_0580_mocks = {}
    for m, cj in mock_payloads_0580:
        tid = upsert_test(
            course_id=COURSE_0580_ID,
            folder_id=f0580['past_papers'],
            title=m['paper_meta']['title'],
            test_type='IGCSE-Math',
            order_index=m['order_index'],
            content_json=cj,
            id_bucket_key='tests_0580',
            code=m['code'],
        )
        pub_0580_mocks[m['code']] = (tid, m)

    pub_0606_drills = {}
    for d, cj in all_0606_drills_built:
        tid = upsert_test(
            course_id=COURSE_0606_ID,
            folder_id=f0606[d['folder_key']],
            title=d['title'],
            test_type='Standard-MCQ',
            order_index=d['order_index'],
            content_json=cj,
            id_bucket_key='tests_0606',
            code=d['code'],
        )
        pub_0606_drills[d['code']] = (tid, d)

    pub_0606_mocks = {}
    for m, cj in mock_payloads_0606:
        tid = upsert_test(
            course_id=COURSE_0606_ID,
            folder_id=f0606['past_papers'],
            title=m['paper_meta']['title'],
            test_type='IGCSE-Math',
            order_index=m['order_index'],
            content_json=cj,
            id_bucket_key='tests_0606',
            code=m['code'],
        )
        pub_0606_mocks[m['code']] = (tid, m)

    print("\n=== 6. LINKING DRILLS & MOCKS TO LECTURE TASK LISTS ===", flush=True)
    ids = load_ids()
    # Link 0580 lectures
    lecs_0580 = ids['m0580']['lectures']
    tasks_by_lec_0580 = {k: [] for k in lecs_0580}
    for code, (tid, d) in pub_0580_drills.items():
        for lk in d.get('lecture_keys', []):
            if lk in tasks_by_lec_0580:
                tasks_by_lec_0580[lk].append({
                    'id': f'igcse25_{code}',
                    'text': f'Làm chuyên đề: {d["title"]}',
                    'type': 'exercise',
                    'test_id': tid,
                })
    # Attach 4 full mocks to rev & p2p4
    for code, (tid, m) in pub_0580_mocks.items():
        tasks_by_lec_0580['rev'].append({
            'id': f'igcse25_{code}',
            'text': f'Thi thử chuẩn Cambridge (120 phút): {m["paper_meta"]["title"]}',
            'type': 'exercise',
            'test_id': tid,
        })
    tasks_by_lec_0580['p2p4'].insert(0, {
        'id': 'igcse25_0580_p2p4_read',
        'text': 'Học thuộc bảng Lượng giác chính xác (0°–90°) & Ma trận Paper 2 Non-Calc vs Paper 4 Calc',
        'type': 'manual',
    })

    for lk, lid in lecs_0580.items():
        if not tasks_by_lec_0580[lk]:
            continue
        cur = sb_get(f'lectures?id=eq.{lid}&select=task_list')[0].get('task_list') or []
        merged = merge_task_list(cur, tasks_by_lec_0580[lk])
        sb_patch(f'lectures?id=eq.{lid}', {'task_list': merged})
    print("  [OK] Updated task_list on 0580 lectures!", flush=True)

    # Link 0606 lectures (every single chapter gets audio study task + its topical drill!)
    lecs_0606 = ids['m0606']['lectures']
    tasks_by_lec_0606 = {
        k: [{
            'id': f'igcse25_0606_{k}_study',
            'text': 'Nghe trọn bài giảng Audio Song ngữ & tóm tắt công thức trọng tâm (Paper 1 vs Paper 2)',
            'type': 'manual',
        }]
        for k in lecs_0606
    }
    for code, (tid, d) in pub_0606_drills.items():
        lk = d.get('lecture_key')
        if lk in tasks_by_lec_0606:
            tasks_by_lec_0606[lk].append({
                'id': f'igcse25_{code}',
                'text': f'Làm bài luyện chuyên đề: {d["title"]}',
                'type': 'exercise',
                'test_id': tid,
            })
    for code, (tid, m) in pub_0606_mocks.items():
        tasks_by_lec_0606['rev'].append({
            'id': f'igcse25_{code}',
            'text': f'Thi thử 80 điểm chuẩn Cambridge (120 phút): {m["paper_meta"]["title"]}',
            'type': 'exercise',
            'test_id': tid,
        })

    for lk, lid in lecs_0606.items():
        cur = sb_get(f'lectures?id=eq.{lid}&select=task_list')[0].get('task_list') or []
        merged = merge_task_list(cur, tasks_by_lec_0606[lk])
        sb_patch(f'lectures?id=eq.{lid}', {'task_list': merged})
    print("  [OK] Updated task_list on all 18 lectures of 0606!", flush=True)
    print("\n[SUCCESS] PUBLISHED ALL 35 NEW TESTS + 8 CAMBRIDGE A4 PDFs + LECTURE TASK LINKS!", flush=True)


if __name__ == '__main__':
    main()
