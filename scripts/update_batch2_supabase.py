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

lessons = [
    ('B7', 'cbebf582-244c-48bf-a586-c6c1922d8e20', 'scripts/raw_science_bio_b3_b19/b7_p1_transformed.html'),
    ('B8', 'e2819423-13ed-47a2-bd80-9a083989e8bd', 'scripts/raw_science_bio_b3_b19/b8_p1_transformed.html'),
    ('B9', 'a79dd569-671f-4559-84a3-eee1e6018172', 'scripts/raw_science_bio_b3_b19/b9_p1_transformed.html'),
    ('B10', '04d34896-13fb-411b-9e13-2bc3f9725136', 'scripts/raw_science_bio_b3_b19/b10_p1_transformed.html')
]

print("=== UPDATING SUPABASE LECTURE_PAGES FOR BATCH 2 (B7, B8, B9, B10) ===")

for name, lid, hpath in lessons:
    with open(hpath, 'r', encoding='utf-8') as f:
        html = f.read()
        
    opens = len(re.findall(r'<div\b[^>]*>', html, flags=re.IGNORECASE))
    closes = len(re.findall(r'</div>', html, flags=re.IGNORECASE))
    diff = opens - closes
    if diff != 0:
        raise ValueError(f"Aborting: {name} has div diff = {diff}!")
        
    res = sb.table('lecture_pages').update({'content_html': html}).eq('lecture_id', lid).eq('page_number', 1).execute()
    print(f"Updated Lesson {name} ({lid}) - rows affected: {len(res.data)}")

print("\n🎉 BATCH 2 (B7, B8, B9, B10) LIVE IN SUPABASE!")
