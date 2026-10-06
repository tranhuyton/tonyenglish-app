import os
import sys
import re
import json
from supabase import create_client

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

with open('.env', 'r', encoding='utf-8') as f:
    env = f.read()

URL = re.search(r'^VITE_SUPABASE_URL=(.*)$', env, re.M).group(1).strip()
KEY = re.search(r'^VITE_SUPABASE_ANON_KEY=(.*)$', env, re.M).group(1).strip()
sb = create_client(URL, KEY)

CID = '9331cc50-d76b-4247-860e-25b2096e93cb'
lecs = sb.table('lectures').select('id, title, order_index').eq('course_id', CID).order('order_index').execute()

print(f"Total lectures in course: {len(lecs.data)}")
for l in lecs.data:
    title = l['title']
    print(f"[{l['order_index']:2d}] {l['id']} : {title}")
