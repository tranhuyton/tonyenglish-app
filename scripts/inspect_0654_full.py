import sys
import re
from supabase import create_client

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

with open('.env', 'r', encoding='utf-8') as f:
    env = f.read()

URL = re.search(r'^VITE_SUPABASE_URL=(.*)$', env, re.M).group(1).strip()
KEY = re.search(r'^VITE_SUPABASE_ANON_KEY=(.*)$', env, re.M).group(1).strip()
sb = create_client(URL, KEY)

course_id = 'a2a949c7-c23e-45a7-82fa-cdeda5cc32a7'
mods = sb.table('lecture_modules').select('*').eq('course_id', course_id).order('order_index').execute().data
print(f"Total modules: {len(mods)}")
for m in mods:
    print(f"\n==========================================")
    print(f"Module: {m['id']} | {m['title']} | order={m.get('order_index')}")
    print(f"==========================================")
    lecs = sb.table('lectures').select('id, title, order_index').eq('module_id', m['id']).order('order_index').execute().data
    print(f"Lectures count: {len(lecs)}")
    for l in lecs:
        pages = sb.table('lecture_pages').select('page_number, content_html').eq('lecture_id', l['id']).order('page_number').execute().data
        p_info = [(p['page_number'], len(p.get('content_html') or '')) for p in pages]
        print(f"  [{l['id']}] {l['title']} -> Pages: {p_info}")
