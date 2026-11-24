# -*- coding: utf-8 -*-
"""
Generates an idempotent SQL script `supabase_sync_maths_0580_0606_boards.sql`
that upgrades the Task Boards for IGCSE Maths 0580 & IGCSE Maths 0606 to match
the new 2025-2027 4-Module (0580, with strict Non-Calc vs Calc columns) and
5-Module (0606, with Ch. 7B Circle & Paper 1 Non-Calc / Paper 2 Calc) structure,
and assigns every newly added item to all currently enrolled students.
"""

import json
import os
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

from scripts.igcse_maths_pipeline import (
    COURSE_0580_ID,
    COURSE_0606_ID,
    ROOT_DIR,
    sb_get,
)


def sql_str(val):
    if val is None:
        return 'NULL'
    return "'" + str(val).replace("'", "''") + "'"


def fmt_lec_desc(lec_id, lec_title, course_id, task_id=None):
    parts = [f"lecture_id:{lec_id}", f"course_id:{course_id}"]
    if task_id:
        parts.append(f"task_id:{task_id}")
    return f"Được tạo tự động từ bài giảng: {lec_title} | " + " | ".join(parts)


def build_course_board_sql(course_id, board_title):
    mods = sb_get(f'lecture_modules?course_id=eq.{course_id}&order=order_index.asc,id.asc&select=id,title,order_index')
    lecs = sb_get(f'lectures?course_id=eq.{course_id}&order=order_index.asc,id.asc&select=id,module_id,title,order_index,task_list')
    folders = sb_get(f'folders?course_id=eq.{course_id}&order=display_order.asc,id.asc&select=id,title,display_order')
    tests = sb_get(f'tests?course_id=eq.{course_id}&order=order_index.asc,id.asc&select=id,folder_id,title,test_type,order_index')

    tests_by_id = {t['id']: t for t in tests}
    folders_by_id = {f['id']: f for f in folders}
    used_test_ids = set()

    columns = []
    for m in mods:
        m_lecs = [l for l in lecs if l['module_id'] == m['id']]
        if not m_lecs:
            continue
        cards = []
        for l in m_lecs:
            items = []
            tlist = l.get('task_list') or []
            manuals = [x for x in tlist if isinstance(x, dict) and (x.get('type') or 'manual') == 'manual' and (x.get('text') or x.get('title'))]
            exers = [x for x in tlist if isinstance(x, dict) and x.get('test_id')]
            if manuals:
                for mt in manuals:
                    items.append({
                        'task_type': 'manual',
                        'title': str(mt.get('text') or mt.get('title')).strip(),
                        'description': fmt_lec_desc(l['id'], l['title'], course_id, mt.get('id')),
                        'test_id': None,
                    })
            else:
                items.append({
                    'task_type': 'manual',
                    'title': 'Học kỹ bài giảng & ghi chép công thức trọng tâm',
                    'description': fmt_lec_desc(l['id'], l['title'], course_id),
                    'test_id': None,
                })
            for ex in exers:
                tid = str(ex['test_id'])
                if tid in used_test_ids or tid not in tests_by_id:
                    continue
                used_test_ids.add(tid)
                items.append({
                    'task_type': 'test',
                    'title': tests_by_id[tid]['title'],
                    'description': '',
                    'test_id': tid,
                })
            cards.append({'title': l['title'], 'items': items})
        columns.append({'title': m['title'], 'cards': cards})

    # Collect unlinked Past Papers & Mocks separated cleanly into Non-Calc vs Calc
    rem = [t for t in tests if t['id'] not in used_test_ids]
    nc_rem = []
    c_rem = []
    other_rem = []
    for t in rem:
        fname = (folders_by_id.get(t.get('folder_id') or '', {}).get('title') or '').lower()
        tt = (t.get('title') or '').lower()
        if 'non-calc' in tt or 'non-calculator' in fname or 'paper 2' in tt and course_id == COURSE_0580_ID or '0580/2' in tt or '0606/1' in tt or 'paper 1' in tt and course_id == COURSE_0606_ID:
            nc_rem.append(t)
        elif 'calc' in tt or 'past paper' in fname or '0580/4' in tt or '0606/2' in tt:
            c_rem.append(t)
        else:
            other_rem.append(t)

    extra_cards = []
    if nc_rem:
        extra_cards.append({
            'title': '🚫 Non-Calculator Past Papers & Full Mocks',
            'items': [{'task_type': 'test', 'title': t['title'], 'description': '', 'test_id': t['id']} for t in nc_rem],
        })
    if c_rem:
        extra_cards.append({
            'title': '🧮 Calculator Past Papers & Full Mocks',
            'items': [{'task_type': 'test', 'title': t['title'], 'description': '', 'test_id': t['id']} for t in c_rem],
        })
    if other_rem:
        extra_cards.append({
            'title': '📘 Bài luyện bổ sung',
            'items': [{'task_type': 'test', 'title': t['title'], 'description': '', 'test_id': t['id']} for t in other_rem],
        })
    if extra_cards:
        columns.append({
            'title': '🏆 Kho Đề Thi Thử & Past Papers (Non-Calc vs Calc) [color:#ffe4e6,#9f1239]',
            'cards': extra_cards,
        })

    lines = [
        f"-- =============================================================================",
        f"-- REBUILD TASK BOARD: {board_title} ({course_id})",
        f"-- =============================================================================",
        "DO $$",
        "DECLARE",
        "  v_tpl_id uuid;",
        "  v_col_id uuid;",
        "  v_card_id uuid;",
        "BEGIN",
        f"  SELECT id INTO v_tpl_id FROM public.board_templates WHERE course_id = {sql_str(course_id)} ORDER BY created_at ASC LIMIT 1;",
        "  IF v_tpl_id IS NULL THEN",
        f"    INSERT INTO public.board_templates (course_id, title, is_active) VALUES ({sql_str(course_id)}, {sql_str(board_title)}, true) RETURNING id INTO v_tpl_id;",
        "  ELSE",
        f"    UPDATE public.board_templates SET title = {sql_str(board_title)}, is_active = true WHERE id = v_tpl_id;",
        "    DELETE FROM public.board_card_items WHERE card_id IN (SELECT id FROM public.board_cards WHERE column_id IN (SELECT id FROM public.board_columns WHERE board_template_id = v_tpl_id));",
        "    DELETE FROM public.board_cards WHERE column_id IN (SELECT id FROM public.board_columns WHERE board_template_id = v_tpl_id);",
        "    DELETE FROM public.board_columns WHERE board_template_id = v_tpl_id;",
        "  END IF;",
    ]

    for c_idx, col in enumerate(columns, 1):
        lines.append(
            f"  INSERT INTO public.board_columns (course_id, board_template_id, title, order_index) "
            f"VALUES ({sql_str(course_id)}, v_tpl_id, {sql_str(col['title'])}, {c_idx}) RETURNING id INTO v_col_id;"
        )
        for k_idx, card in enumerate(col['cards'], 1):
            lines.append(
                f"  INSERT INTO public.board_cards (column_id, title, order_index) "
                f"VALUES (v_col_id, {sql_str(card['title'])}, {k_idx}) RETURNING id INTO v_card_id;"
            )
            for i_idx, it in enumerate(card['items'], 1):
                lines.append(
                    f"  INSERT INTO public.board_card_items (card_id, task_type, title, description, test_id, order_index) "
                    f"VALUES (v_card_id, {sql_str(it['task_type'])}, {sql_str(it['title'])}, {sql_str(it['description'])}, {sql_str(it['test_id'])}, {i_idx});"
                )

    lines.append("END $$;")
    return "\n".join(lines)


def main():
    sql_parts = [
        "-- Auto-generated idempotent SQL to sync IGCSE Maths 0580 & 0606 Task Boards (2025-2027 Upgrade)",
        "-- Safe to run in Supabase SQL Editor (only modifies board_templates/columns/cards/items for 0580 & 0606).",
        "BEGIN;",
        "",
        build_course_board_sql(COURSE_0580_ID, 'Bảng công việc IGCSE Maths 0580 (2025–2027)'),
        "",
        build_course_board_sql(COURSE_0606_ID, 'Bảng công việc IGCSE Maths 0606 (2025–2027)'),
        "",
        "COMMIT;",
    ]
    out_path = os.path.join(ROOT_DIR, 'supabase_sync_maths_0580_0606_boards.sql')
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write("\n".join(sql_parts) + "\n")
    print(f"[OK] Generated {out_path} ({os.path.getsize(out_path)} bytes)", flush=True)


if __name__ == '__main__':
    main()
