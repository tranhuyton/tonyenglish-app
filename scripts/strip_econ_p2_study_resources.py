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

with open('scripts/econ_topics_1_to_3.json', 'r', encoding='utf-8') as f:
    lectures = json.load(f)

print(f"Loaded {len(lectures)} lectures to strip Study Resources from Page 2...")

success_count = 0
for lec in lectures:
    lid = lec['lecture_id']
    order = lec['lecture_order']
    title = lec['lecture_title']
    
    # Read raw p2
    raw_path = f"scripts/raw_econ/lec_{order}_p2.html"
    with open(raw_path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    cleaned = re.sub(r'<!--\s*(?:Thanh Tài liệu học tập|Study Resources Bar)[^>]*-->\s*<div[^>]*>.*?</div>\s*', '', html, flags=re.DOTALL)
    
    assert "Study Resources" not in cleaned and "Tài liệu học tập" not in cleaned, f"SR still found in Lec {order}"
    op = len(re.findall(r'<div\b', cleaned))
    cl = len(re.findall(r'</div>', cleaned))
    assert op == cl, f"Div mismatch in Lec {order}: {op} != {cl}"
    
    res = sb.table('lecture_pages').update({'content_html': cleaned}).eq('lecture_id', lid).eq('page_number', 2).execute()
    print(f"Lec {order:02d} ({lid[:8]}...): Updated Page 2 in Supabase ({len(res.data)} rows, diff={op-cl})")
    success_count += 1

print(f"\n✅ Successfully stripped Study Resources from Page 2 of all {success_count} lectures!")
