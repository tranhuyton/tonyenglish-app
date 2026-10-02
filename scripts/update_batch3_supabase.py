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
    ('B11', '39003a2f-708e-47fe-b8ad-7aae073273a3', 'scripts/raw_science_bio_b3_b19/b11_p1_transformed.html'),
    ('B12', '58e65add-a67a-4b90-8b84-52de1a2840be', 'scripts/raw_science_bio_b3_b19/b12_p1_transformed.html'),
    ('B13', '2637d6ee-fd5f-48fc-aa7a-fc794fb3e561', 'scripts/raw_science_bio_b3_b19/b13_p1_transformed.html'),
    ('B14', '7ed510d0-acd2-4d0a-9079-1f1e4e4fc463', 'scripts/raw_science_bio_b3_b19/b14_p1_transformed.html')
]

print("=== UPDATING SUPABASE LECTURE_PAGES FOR BATCH 3 (B11, B12, B13, B14) ===")

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

print("\n🎉 BATCH 3 (B11, B12, B13, B14) LIVE IN SUPABASE!")
