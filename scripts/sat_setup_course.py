import os
import re
import sys
import json
from supabase import create_client

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

ROOT_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
with open(os.path.join(ROOT_DIR, '.env'), 'r', encoding='utf-8') as f:
    env = f.read()

URL = re.search(r'^VITE_SUPABASE_URL=(.*)$', env, re.M).group(1).strip()
KEY = re.search(r'^VITE_SUPABASE_ANON_KEY=(.*)$', env, re.M).group(1).strip()
sb = create_client(URL, KEY)

COURSE_TITLE = 'Digital SAT 1500+'
COURSE_TYPE = 'SAT'

RW_MODULES = [
    {
        'key': 'rw_m1',
        'title': 'R&W • Module 1: Strategy & 1500+ Architecture [color:#dbeafe,#1e3a8a]',
        'order_index': 1,
    },
    {
        'key': 'rw_m2',
        'title': 'R&W • Module 2: Standard English Conventions [color:#d1fae5,#065f46]',
        'order_index': 2,
    },
    {
        'key': 'rw_m3',
        'title': 'R&W • Module 3: Expression of Ideas [color:#fef3c7,#b45309]',
        'order_index': 3,
    },
    {
        'key': 'rw_m4',
        'title': 'R&W • Module 4: Craft and Structure [color:#e0e7ff,#3730a3]',
        'order_index': 4,
    },
    {
        'key': 'rw_m5',
        'title': 'R&W • Module 5: Information and Ideas (Hard M2) [color:#fee2e2,#991b1b]',
        'order_index': 5,
    },
]

def get_or_create_course():
    existing = sb.table('courses').select('*').eq('title', COURSE_TITLE).execute().data
    if existing:
        print(f"[FOUND] Course '{COURSE_TITLE}': {existing[0]['id']}")
        return existing[0]
    all_courses = sb.table('courses').select('order_index').execute().data
    max_order = max((c.get('order_index') or 0) for c in all_courses) if all_courses else 0
    res = sb.table('courses').insert({
        'title': COURSE_TITLE,
        'type': COURSE_TYPE,
        'order_index': max_order + 1,
    }).execute().data[0]
    print(f"[CREATED] Course '{COURSE_TITLE}': {res['id']}")
    return res

def get_or_create_module(course_id, title, order_index):
    existing = sb.table('lecture_modules').select('*').eq('course_id', course_id).eq('order_index', order_index).execute().data
    if existing:
        if existing[0]['title'] != title:
            sb.table('lecture_modules').update({'title': title}).eq('id', existing[0]['id']).execute()
        print(f"  [FOUND] Module {order_index}: {existing[0]['id']}")
        return existing[0]
    res = sb.table('lecture_modules').insert({
        'course_id': course_id,
        'title': title,
        'order_index': order_index,
    }).execute().data[0]
    print(f"  [CREATED] Module {order_index}: {res['id']}")
    return res

def get_or_create_folder(course_id, title, display_order, parent_id=None):
    q = sb.table('folders').select('*').eq('course_id', course_id).eq('title', title)
    if parent_id is None:
        q = q.is_('parent_id', 'null')
    else:
        q = q.eq('parent_id', parent_id)
    existing = q.execute().data
    if existing:
        print(f"  [FOUND] Folder '{title}': {existing[0]['id']}")
        return existing[0]
    payload = {
        'course_id': course_id,
        'title': title,
        'display_order': display_order,
    }
    if parent_id is not None:
        payload['parent_id'] = parent_id
    res = sb.table('folders').insert(payload).execute().data[0]
    print(f"  [CREATED] Folder '{title}': {res['id']}")
    return res

def main():
    course = get_or_create_course()
    course_id = course['id']

    modules_map = {}
    for m in RW_MODULES:
        mod = get_or_create_module(course_id, m['title'], m['order_index'])
        modules_map[m['key']] = mod['id']

    # Root branch folder: Reading & Writing (R&W)
    rw_root = get_or_create_folder(course_id, 'Reading & Writing (R&W)', 1, None)
    f_drills = get_or_create_folder(course_id, '1. Skill Drills (Luyện từng kỹ năng 1500+)', 1, rw_root['id'])
    f_mocks = get_or_create_folder(course_id, '2. Full-Length Adaptive Mock Tests (Bluebook)', 2, rw_root['id'])
    f_vocab = get_or_create_folder(course_id, '3. Elite Vocabulary Games (500 Từ SAT 1500+)', 3, rw_root['id'])

    ids_out = {
        'course_id': course_id,
        'course_title': COURSE_TITLE,
        'modules': modules_map,
        'folders': {
            'rw_root': rw_root['id'],
            'rw_drills': f_drills['id'],
            'rw_mocks': f_mocks['id'],
            'rw_vocab': f_vocab['id'],
        },
        'lectures': {},
        'drills': {},
        'mocks': {},
        'vocab_games': {},
    }

    ids_path = os.path.join(os.path.dirname(__file__), 'sat_course_ids.json')
    if os.path.exists(ids_path):
        with open(ids_path, 'r', encoding='utf-8') as f:
            old = json.load(f)
        for k in ['lectures', 'drills', 'mocks', 'vocab_games']:
            if k in old and isinstance(old[k], dict):
                ids_out[k] = old[k]

    with open(ids_path, 'w', encoding='utf-8') as f:
        json.dump(ids_out, f, indent=2, ensure_ascii=False)
    print(f"\nSaved SAT course IDs to {ids_path}")

if __name__ == '__main__':
    main()
