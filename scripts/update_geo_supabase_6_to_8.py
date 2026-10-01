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

lecs = [
    ('6.1', 'c6fccfc5-088b-4145-9a23-9cbb2df1cce9', '6_1'),
    ('6.2', '5390b0d7-995c-4c18-a092-b5cdd4eda49a', '6_2'),
    ('6.3', '33c91ae9-b13f-49d7-b29f-0c3b794d192d', '6_3'),
    ('7.1', '556bc6b6-1555-49a9-a043-35f059b44559', '7_1'),
    ('7.2', '30bae547-a9b0-4c09-8850-ce22b96cfea2', '7_2'),
    ('7.3', '0b658b3f-bf70-4991-95d5-d65616b7ec1a', '7_3'),
    ('8.1', '5ff5f837-df39-4488-bbd2-5138f4faed1e', '8_1'),
    ('8.2', '9cf90212-43f4-4b28-8014-fd6c130db8ef', '8_2'),
    ('8.3', '7da208d1-559d-4e60-a6a3-ebfb8c2d232f', '8_3')
]

print("=== UPDATING SUPABASE LECTURE_PAGES (PAGE 1) FOR LESSONS 6.1 TO 8.3 ===")

for name, lid, code in lecs:
    hpath = f"scripts/raw_geo/{code}_p1_transformed.html"
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

print("\n🎉 ALL 9 LESSONS SUCCESSFULLY UPDATED IN SUPABASE!")
