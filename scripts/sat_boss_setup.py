# -*- coding: utf-8 -*-
"""
Sets up the Capstone 'Hard M2 Boss Masterclass (750–800 Sprint)' module (order 10)
and 'Hard M2 Boss Drills' folder (display_order 3) inside the unified 'Digital SAT 1500+' course.
Preserves all existing R&W and Math IDs in scripts/sat_course_ids.json.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from sat_audio_pipeline import sb, load_ids, save_ids

BOSS_MODULE_TITLE = '🔥 Hard M2 Boss Masterclass (750–800 Sprint) [color:#fef2f2,#991b1b]'
BOSS_FOLDER_TITLE = '🔥 Hard M2 Boss Drills (120 Câu Trùm Cuối 750–800)'

def main():
    ids = load_ids()
    course_id = ids['course_id']
    print(f"Setting up Hard M2 Boss Masterclass inside Course ID: {course_id}", flush=True)

    # 1. Lecture Module (order_index = 10)
    existing_mod = (
        sb.table('lecture_modules')
        .select('*')
        .eq('course_id', course_id)
        .eq('order_index', 10)
        .execute()
        .data
    )
    if existing_mod:
        mod_id = existing_mod[0]['id']
        if existing_mod[0]['title'] != BOSS_MODULE_TITLE:
            sb.table('lecture_modules').update({'title': BOSS_MODULE_TITLE}).eq('id', mod_id).execute()
        print(f"  [FOUND] Module 10: {mod_id}", flush=True)
    else:
        res = (
            sb.table('lecture_modules')
            .insert({'course_id': course_id, 'title': BOSS_MODULE_TITLE, 'order_index': 10})
            .execute()
            .data[0]
        )
        mod_id = res['id']
        print(f"  [CREATED] Module 10: {mod_id} ({BOSS_MODULE_TITLE})", flush=True)

    # 2. Root Folder (display_order = 3)
    existing_f = (
        sb.table('folders')
        .select('*')
        .eq('course_id', course_id)
        .eq('title', BOSS_FOLDER_TITLE)
        .is_('parent_id', 'null')
        .execute()
        .data
    )
    if existing_f:
        folder_id = existing_f[0]['id']
        print(f"  [FOUND] Folder: {folder_id}", flush=True)
    else:
        res = (
            sb.table('folders')
            .insert({'course_id': course_id, 'title': BOSS_FOLDER_TITLE, 'display_order': 3})
            .execute()
            .data[0]
        )
        folder_id = res['id']
        print(f"  [CREATED] Folder: {folder_id} ({BOSS_FOLDER_TITLE})", flush=True)

    ids.setdefault('modules', {})['boss_m10'] = mod_id
    ids.setdefault('folders', {})['boss_drills'] = folder_id
    ids.setdefault('boss_lectures', {})
    ids.setdefault('boss_drills', {})
    save_ids(ids)
    print("[OK] Hard M2 Boss module & folder saved to scripts/sat_course_ids.json!", flush=True)

if __name__ == '__main__':
    main()
