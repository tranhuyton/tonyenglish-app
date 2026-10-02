import os
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

updates = [
    ('B1', '1231b474-8a99-4330-b45d-fdda19a802fe', 'scripts/raw_science_bio/b1_p1_transformed.html'),
    ('B2', '7b3c2e0a-b0d5-4716-a574-6f1c5c379c7c', 'scripts/raw_science_bio/b2_p1_transformed.html')
]

print("=== UPDATING SUPABASE LECTURE_PAGES (PAGE 1) FOR ENHANCED B1 & B2 ===")

for name, lid, hpath in updates:
    with open(hpath, 'r', encoding='utf-8') as f:
        html = f.read()
        
    opens = len(re.findall(r'<div\b[^>]*>', html, flags=re.IGNORECASE))
    closes = len(re.findall(r'</div>', html, flags=re.IGNORECASE))
    diff = opens - closes
    if diff != 0:
        raise ValueError(f"Aborting: {name} has div diff = {diff}!")
        
    res = sb.table('lecture_pages').update({'content_html': html}).eq('lecture_id', lid).eq('page_number', 1).execute()
    print(f"Updated Lesson {name} ({lid}) - rows affected: {len(res.data)}")

print("\n🎉 B1 AND B2 SUCCESSFULLY UPDATED IN SUPABASE!")
