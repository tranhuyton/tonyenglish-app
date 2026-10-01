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
    ('9.1', '6c14f92b-774a-45d1-a68d-2e9fe5e0b85d', '9_1'),
    ('9.2', '5b7da7e1-3da1-4bf4-9700-6e11d7a7ef6b', '9_2'),
    ('9.3', '53517557-9eb4-450d-a8dd-18b73c71938a', '9_3'),
    ('10.1', '362104be-aedc-4cbe-87b2-29034e93cc9c', '10_1'),
    ('10.2', '76dcafbf-e6b8-47f1-8618-be1b14e975ed', '10_2'),
    ('10.3', '96d7f427-3b6d-43e3-84dc-f8f052f20033', '10_3'),
    ('10.4', '199a26cd-1226-4ff7-b063-f7df7fa7b5ba', '10_4'),
    ('10.5', 'a3a8d904-d277-4eef-b8ff-52a913ebc5f6', '10_5'),
    ('10.6', 'fb30c141-db3a-49e8-aa55-028c913640d4', '10_6')
]

print("=== UPDATING SUPABASE LECTURE_PAGES (PAGE 1) FOR LESSONS 9.1 TO 10.6 ===")

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

print("\n🎉 ALL 9 LESSONS (9.1 TO 10.6) SUCCESSFULLY UPDATED IN SUPABASE!")
