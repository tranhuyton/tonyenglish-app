# -*- coding: utf-8 -*-
"""
Sets up the Math 1500+ branch inside the unified 'Digital SAT 1500+' course on Supabase:
- 4 Math lecture_modules (order_index 6..9)
- 4 Math folders (root 'Math (1500+)' + Drills + Adaptive Mocks + Formula & Desmos Speed Games)
Preserves all existing Reading & Writing keys in scripts/sat_course_ids.json.
"""

import os
import sys
import json

sys.path.insert(0, os.path.dirname(__file__))
from sat_audio_pipeline import sb, load_ids, save_ids

MATH_MODULES = [
    {
        'key': 'math_m1',
        'title': 'Math • Module 1: Algebra & Desmos Mastery [color:#dcfce7,#166534]',
        'order_index': 6,
    },
    {
        'key': 'math_m2',
        'title': 'Math • Module 2: Advanced Math (Hard M2 Core) [color:#e0e7ff,#3730a3]',
        'order_index': 7,
    },
    {
        'key': 'math_m3',
        'title': 'Math • Module 3: Problem-Solving & Data Analysis [color:#fef3c7,#92400e]',
        'order_index': 8,
    },
    {
        'key': 'math_m4',
        'title': 'Math • Module 4: Geometry & Trigonometry (750–800) [color:#fce7f3,#9d174d]',
        'order_index': 9,
    },
]

def get_or_create_module(course_id, title, order_index):
    existing = (
        sb.table('lecture_modules')
        .select('*')
        .eq('course_id', course_id)
        .eq('order_index', order_index)
        .execute()
        .data
    )
    if existing:
        if existing[0]['title'] != title:
            sb.table('lecture_modules').update({'title': title}).eq('id', existing[0]['id']).execute()
        print(f"  [FOUND] Module {order_index}: {existing[0]['id']} ({title})", flush=True)
        return existing[0]
    res = (
        sb.table('lecture_modules')
        .insert({'course_id': course_id, 'title': title, 'order_index': order_index})
        .execute()
        .data[0]
    )
    print(f"  [CREATED] Module {order_index}: {res['id']} ({title})", flush=True)
    return res

def get_or_create_folder(course_id, title, display_order, parent_id=None):
    q = sb.table('folders').select('*').eq('course_id', course_id).eq('title', title)
    if parent_id is None:
        q = q.is_('parent_id', 'null')
    else:
        q = q.eq('parent_id', parent_id)
    existing = q.execute().data
    if existing:
        print(f"  [FOUND] Folder '{title}': {existing[0]['id']}", flush=True)
        return existing[0]
    payload = {
        'course_id': course_id,
        'title': title,
        'display_order': display_order,
    }
    if parent_id is not None:
        payload['parent_id'] = parent_id
    res = sb.table('folders').insert(payload).execute().data[0]
    print(f"  [CREATED] Folder '{title}': {res['id']}", flush=True)
    return res

def main():
    ids = load_ids()
    course_id = ids['course_id']
    print(f"Setting up Digital SAT Math 1500+ inside Course ID: {course_id}", flush=True)

    for m in MATH_MODULES:
        mod = get_or_create_module(course_id, m['title'], m['order_index'])
        ids.setdefault('modules', {})[m['key']] = mod['id']

    math_root = get_or_create_folder(course_id, 'Math (1500+)', 2, None)
    f_drills = get_or_create_folder(course_id, '1. Math Skill Drills (Luyện từng chuyên đề 1500+)', 1, math_root['id'])
    f_mocks = get_or_create_folder(course_id, '2. Full-Length Adaptive Math Mock Tests (Bluebook)', 2, math_root['id'])
    f_games = get_or_create_folder(course_id, '3. Formula & Desmos Speed Games (100 Công thức 800)', 3, math_root['id'])

    ids.setdefault('folders', {}).update({
        'math_root': math_root['id'],
        'math_drills': f_drills['id'],
        'math_mocks': f_mocks['id'],
        'math_games': f_games['id'],
    })
    ids.setdefault('math_lectures', {})
    ids.setdefault('math_drills', {})
    ids.setdefault('math_mocks', {})
    ids.setdefault('math_games', {})

    save_ids(ids)
    print("\n[OK] Math 1500+ modules & folders synced and saved to scripts/sat_course_ids.json!", flush=True)

if __name__ == '__main__':
    main()
