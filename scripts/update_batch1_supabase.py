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
    ('B3', '9a23109e-ad73-4fcf-a599-9605cc4906eb', 'scripts/raw_science_bio_b3_b19/b3_p1_transformed.html'),
    ('B4', '757409b3-5cec-4e1f-8877-18d81e440103', 'scripts/raw_science_bio_b3_b19/b4_p1_transformed.html'),
    ('B5', '8ab2afa2-59e3-4c56-8971-8d93dec5ad8e', 'scripts/raw_science_bio_b3_b19/b5_p1_transformed.html'),
    ('B6', '1d6a6b7b-ae57-404f-9ad1-58b11219b4d1', 'scripts/raw_science_bio_b3_b19/b6_p1_transformed.html')
]

print("=== UPDATING SUPABASE LECTURE_PAGES FOR BATCH 1 (B3, B4, B5, B6) ===")

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

print("\n🎉 BATCH 1 (B3, B4, B5, B6) LIVE IN SUPABASE!")
