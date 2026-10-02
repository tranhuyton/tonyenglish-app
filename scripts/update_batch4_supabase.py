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
    ('B15', 'deb8222d-2b75-42a3-b454-9601fbfa1bd2', 'scripts/raw_science_bio_b3_b19/b15_p1_transformed.html'),
    ('B16', 'd48c8f84-ba93-49d4-bf61-c7890bd6d2ce', 'scripts/raw_science_bio_b3_b19/b16_p1_transformed.html'),
    ('B17', '24f0deeb-3cd9-4b82-b253-5a070ca31275', 'scripts/raw_science_bio_b3_b19/b17_p1_transformed.html'),
    ('B18', 'cbeb6b74-e9c2-4a91-b39f-decb63e72ec0', 'scripts/raw_science_bio_b3_b19/b18_p1_transformed.html'),
    ('B19', '298327a8-455a-44d5-9a4c-164e2653c456', 'scripts/raw_science_bio_b3_b19/b19_p1_transformed.html')
]

print("=== UPDATING SUPABASE LECTURE_PAGES FOR BATCH 4 (B15, B16, B17, B18, B19) ===")
for code, lec_id, transformed_path in lessons:
    with open(transformed_path, 'r', encoding='utf-8') as f:
        content = f.read()
    res = sb.table('lecture_pages').update({'content_html': content}).eq('lecture_id', lec_id).eq('page_number', 1).execute()
    print(f"Updated Lesson {code} ({lec_id}) - rows affected: {len(res.data)}")

print("\n🎉 BATCH 4 (B15, B16, B17, B18, B19) LIVE IN SUPABASE!")
