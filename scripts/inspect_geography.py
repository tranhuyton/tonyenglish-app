import os
import sys
import json
import re
from supabase import create_client

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

with open('.env', 'r', encoding='utf-8') as f:
    env = f.read()

URL = re.search(r'^VITE_SUPABASE_URL=(.*)$', env, re.M).group(1).strip()
KEY = re.search(r'^VITE_SUPABASE_ANON_KEY=(.*)$', env, re.M).group(1).strip()
sb = create_client(URL, KEY)

courses = sb.table('courses').select('id, title').ilike('title', '%Geography%').execute()
print('Courses found:', len(courses.data))
for c in courses.data:
    cid = c['id']
    print(f"\nCourse: {c['title']} (id: {cid})")
    lecs = sb.table('lectures').select('*').eq('course_id', cid).limit(1).execute()
    if lecs.data:
        print("Lecture columns:", list(lecs.data[0].keys()))
    all_lecs = sb.table('lectures').select('*').eq('course_id', cid).execute()
    print(f"Total lectures: {len(all_lecs.data)}")
    for l in all_lecs.data:
        print(f"  {l['id']} : {l.get('title')}")
