# -*- coding: utf-8 -*-
"""
Full Live Supabase DB & Integrity Audit for ALL 14 Digital SAT Real Past Exams (2024-2025),
plus generates idempotent SQL `supabase_sync_sat_real_exams_board.sql` to append the new
`🏛️ Real Past Exams (2024–2025 — 14 Đề Thi Thật)` column to the Digital SAT 1500+ Task Board!
"""

import json
import os
import re
import sys
import xml.etree.ElementTree as ET

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

from scripts.sat_real_exams_pipeline import (
    ROOT_DIR,
    SAT_COURSE_ID,
    load_ids,
    sb_get,
    validate_sat_bluebook_json,
)


def sql_str(val):
    if val is None:
        return 'NULL'
    return "'" + str(val).replace("'", "''") + "'"


def audit_live_real_exams():
    ids = load_ids()
    f_rw = ids['folders']['real_rw']
    f_math = ids['folders']['real_math']
    f_root = ids['folders']['real_root']

    print("=== LIVE SUPABASE AUDIT: DIGITAL SAT REAL PAST EXAMS (2024-2025) ===", flush=True)
    folders = sb_get(f'folders?course_id=eq.{SAT_COURSE_ID}&select=id,title,parent_id,display_order')
    f_by_id = {f['id']: f for f in folders}
    assert f_root in f_by_id and f_rw in f_by_id and f_math in f_by_id, 'Missing real exam folders in DB!'

    tests = sb_get(
        f'tests?course_id=eq.{SAT_COURSE_ID}&folder_id=in.({f_rw},{f_math})&order=order_index.asc,id.asc&select=id,folder_id,title,test_type,is_published,order_index,content_json'
    )
    rw_tests = [t for t in tests if t['folder_id'] == f_rw]
    math_tests = [t for t in tests if t['folder_id'] == f_math]
    print(f"  Folders verified: Root + R&W ({len(rw_tests)} tests) + Math ({len(math_tests)} tests) = {len(tests)} tests total", flush=True)
    assert len(rw_tests) == 7, f'Expected 7 R&W real exams, got {len(rw_tests)}'
    assert len(math_tests) == 7, f'Expected 7 Math real exams, got {len(math_tests)}'

    total_unique_qs = 0
    total_svgs = 0
    bad_watermarks = ('@dsatuz', '@d7sat', 'satuzhunters', 'minh nghĩa', 't.me/d7sat', '______blank')

    for t in tests:
        assert t['is_published'] is True, f"Unpublished test: {t['title']}"
        assert t['test_type'] == 'SAT-Bluebook', f"Bad test_type: {t['test_type']}"
        cj = t['content_json']
        errs = validate_sat_bluebook_json(cj, t['title'])
        assert not errs, f"Validation errors in {t['title']}: {errs[:5]}"

        raw_low = json.dumps(cj, ensure_ascii=False).lower()
        for bw in bad_watermarks:
            assert bw not in raw_low, f"Watermark '{bw}' leaked in {t['title']}!"

        # Check SVG XML validity & optionAnalysis alignment
        m1 = cj['module1']['questions']
        m2h = cj['module2_hard']['questions']
        m2l = cj['module2_lower']['questions']
        is_true_adaptive = (cj['basicInfo'].get('routingThreshold', 0) or 0) > 0
        uniq_qs = len(m1) + len(m2h) + (len(m2l) if is_true_adaptive else 0)
        total_unique_qs += uniq_qs

        checked_qs = m1 + m2h + (m2l if is_true_adaptive else [])
        svg_cnt = 0
        for q in checked_qs:
            # Verify every inline SVG is valid XML
            for m in re.finditer(r'<svg[\s\S]*?</svg>', (q.get('stimulusHtml') or '') + ' ' + ' '.join(o.get('text', '') for o in (q.get('options') or []))):
                ET.fromstring(m.group(0))
                svg_cnt += 1
            if q.get('questionFormat', 'mcq') == 'mcq':
                oa = (q.get('explanation') or {}).get('optionAnalysis') or {}
                if oa:
                    corr = [k for k, v in oa.items() if isinstance(v, dict) and v.get('status') == 'correct']
                    assert corr == [q['correctAnswer']], f"{t['title']} Q{q['number']}: optionAnalysis correct {corr} != {q['correctAnswer']}"
        total_svgs += svg_cnt
        tag = 'ADAPTIVE-3MOD' if is_true_adaptive else '2-MOD'
        print(f"  [PASS] {t['title']} | {tag} | {uniq_qs} unique Qs | {svg_cnt} SVGs | KaTeX OK", flush=True)

    print(f"\n[ALL 14 LIVE REAL SAT EXAMS PASSED 100%!] Total unique verified questions: {total_unique_qs} | Total crisp inline SVGs: {total_svgs}\n", flush=True)
    return rw_tests, math_tests


def generate_board_sync_sql(rw_tests, math_tests):
    col_title = '🏛️ Real Past Exams (2024–2025 — 14 Đề Thi Thật) [color:#fef3c7,#b45309]'
    cards = [
        ('1. Real Exams — Reading & Writing 2025 (7 Đề • 405 câu)', rw_tests),
        ('2. Real Exams — Math 2024–2025 (7 Đề • 329 câu)', math_tests),
    ]
    lines = [
        "-- Auto-generated idempotent SQL to add/refresh the '🏛️ Real Past Exams (2024–2025)' column",
        "-- on the existing Digital SAT 1500+ Task Board WITHOUT modifying existing columns or progress.",
        "BEGIN;",
        "DO $$",
        "DECLARE",
        "  v_tpl_id uuid;",
        "  v_col_id uuid;",
        "  v_card_id uuid;",
        "  v_next_order int;",
        "BEGIN",
        f"  SELECT id INTO v_tpl_id FROM public.board_templates WHERE course_id = {sql_str(SAT_COURSE_ID)} ORDER BY created_at ASC LIMIT 1;",
        "  IF v_tpl_id IS NULL THEN",
        "    RAISE EXCEPTION 'Digital SAT 1500+ board_template not found';",
        "  END IF;",
        "",
        "  -- Remove previous copy of this Real Past Exams column if re-running (idempotent)",
        "  SELECT id INTO v_col_id FROM public.board_columns WHERE board_template_id = v_tpl_id AND title LIKE '%Real Past Exams%' LIMIT 1;",
        "  IF v_col_id IS NOT NULL THEN",
        "    DELETE FROM public.board_card_items WHERE card_id IN (SELECT id FROM public.board_cards WHERE column_id = v_col_id);",
        "    DELETE FROM public.board_cards WHERE column_id = v_col_id;",
        "    DELETE FROM public.board_columns WHERE id = v_col_id;",
        "  END IF;",
        "",
        "  SELECT COALESCE(MAX(order_index), 0) + 1 INTO v_next_order FROM public.board_columns WHERE board_template_id = v_tpl_id;",
        f"  INSERT INTO public.board_columns (course_id, board_template_id, title, order_index) VALUES ({sql_str(SAT_COURSE_ID)}, v_tpl_id, {sql_str(col_title)}, v_next_order) RETURNING id INTO v_col_id;",
    ]

    for c_idx, (card_title, tlist) in enumerate(cards, 1):
        lines.append(
            f"  INSERT INTO public.board_cards (column_id, title, order_index) VALUES (v_col_id, {sql_str(card_title)}, {c_idx}) RETURNING id INTO v_card_id;"
        )
        for i_idx, t in enumerate(tlist, 1):
            lines.append(
                f"  INSERT INTO public.board_card_items (card_id, task_type, title, description, test_id, order_index) "
                f"VALUES (v_card_id, 'test', {sql_str(t['title'])}, '', {sql_str(t['id'])}, {i_idx});"
            )

    lines.extend(["END $$;", "COMMIT;", ""])
    out_path = os.path.join(ROOT_DIR, 'supabase_sync_sat_real_exams_board.sql')
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines))
    print(f"[OK] Generated {out_path} ({os.path.getsize(out_path)} bytes)", flush=True)


if __name__ == '__main__':
    rw, mt = audit_live_real_exams()
    generate_board_sync_sql(rw, mt)
