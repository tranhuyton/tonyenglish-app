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

bio_lectures = [
    ('B1', '1231b474-8a99-4330-b45d-fdda19a802fe', 'b1'),
    ('B2', '7b3c2e0a-b0d5-4716-a574-6f1c5c379c7c', 'b2'),
    ('B3', '9a23109e-ad73-4fcf-a599-9605cc4906eb', 'b3'),
    ('B4', '757409b3-5cec-4e1f-8877-18d81e440103', 'b4'),
    ('B5', '8ab2afa2-59e3-4c56-8971-8d93dec5ad8e', 'b5'),
    ('B6', '1d6a6b7b-ae57-404f-9ad1-58b11219b4d1', 'b6'),
    ('B7', 'cbebf582-244c-48bf-a586-c6c1922d8e20', 'b7'),
    ('B8', 'e2819423-13ed-47a2-bd80-9a083989e8bd', 'b8'),
    ('B9', 'a79dd569-671f-4559-84a3-eee1e6018172', 'b9'),
    ('B10', '04d34896-13fb-411b-9e13-2bc3f9725136', 'b10'),
    ('B11', '39003a2f-708e-47fe-b8ad-7aae073273a3', 'b11'),
    ('B12', '58e65add-a67a-4b90-8b84-52de1a2840be', 'b12'),
    ('B13', '2637d6ee-fd5f-48fc-aa7a-fc794fb3e561', 'b13'),
    ('B14', '7ed510d0-acd2-4d0a-9079-1f1e4e4fc463', 'b14'),
    ('B15', 'deb8222d-2b75-42a3-b454-9601fbfa1bd2', 'b15'),
    ('B16', 'd48c8f84-ba93-49d4-bf61-c7890bd6d2ce', 'b16'),
    ('B17', '24f0deeb-3cd9-4b82-b253-5a070ca31275', 'b17'),
    ('B18', 'cbeb6b74-e9c2-4a91-b39f-decb63e72ec0', 'b18'),
    ('B19', '298327a8-455a-44d5-9a4c-164e2653c456', 'b19')
]

print("=== UPDATING SUPABASE LECTURE_PAGES (PAGE 1) FOR SCIENCE BIOLOGY B1 TO B19 ===")

for name, lid, code in bio_lectures:
    hpath = f"scripts/raw_science_bio/{code}_p1_transformed.html"
    with open(hpath, 'r', encoding='utf-8') as f:
        new_html = f.read()

    # Pre-flight check
    opens = len(new_html.split('<div')) - 1
    closes = len(new_html.split('</div>')) - 1
    diff = opens - closes
    if diff != 0:
        raise ValueError(f"Aborting: {code} has div diff = {diff}!")

    res = sb.table('lecture_pages').update({'content_html': new_html}).eq('lecture_id', lid).eq('page_number', 1).execute()
    print(f"Updated Lesson {name:4} ({code:4}) - rows affected: {len(res.data)}")

print("\n🎉 ALL 19 SCIENCE BIOLOGY LESSONS SUCCESSFULLY UPDATED IN SUPABASE!")
