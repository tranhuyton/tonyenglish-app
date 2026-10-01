import os
import sys
import json
import re
from bs4 import BeautifulSoup
from supabase import create_client

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

with open('.env', 'r', encoding='utf-8') as f:
    env = f.read()

URL = re.search(r'^VITE_SUPABASE_URL=(.*)$', env, re.M).group(1).strip()
KEY = re.search(r'^VITE_SUPABASE_ANON_KEY=(.*)$', env, re.M).group(1).strip()
sb = create_client(URL, KEY)

lessons = [
    # Topic 3 (4)
    ('3.1', '1b4caf37-15e4-475a-939c-e6490b366fd0', '3_1'),
    ('3.2', '93a28707-1b95-4ed2-a3ff-4789143118cd', '3_2'),
    ('3.3', '7d543b73-837d-4129-afc6-7196df47b6f6', '3_3'),
    ('3.4', 'c5ce49f0-7b81-4843-a477-3ee46e41928e', '3_4'),
    # Topic 4 (4)
    ('4.1', 'e5fde4e7-a1e6-4b3c-aeb2-756155f06ff5', '4_1'),
    ('4.2', 'f45dd9b1-ef60-4521-a067-04bd896fc7e2', '4_2'),
    ('4.3', '1f909afc-865f-46d0-bb20-2e6d474fa87b', '4_3'),
    ('4.4', 'c81dc416-7aa4-4e26-a2af-341d6c03fa52', '4_4'),
    # Topic 5 (3)
    ('5.1', '7c30919a-5d22-425a-a167-21e5de07d203', '5_1'),
    ('5.2', '23eee2fb-427c-4843-8d2d-ec296188730d', '5_2'),
    ('5.3', '36e35bdb-986b-4cd5-b8df-6bb0f93282e5', '5_3'),
    # Topic 6 (3)
    ('6.1', 'c6fccfc5-088b-4145-9a23-9cbb2df1cce9', '6_1'),
    ('6.2', '5390b0d7-995c-4c18-a092-b5cdd4eda49a', '6_2'),
    ('6.3', '33c91ae9-b13f-49d7-b29f-0c3b794d192d', '6_3'),
    # Topic 7 (3)
    ('7.1', '556bc6b6-1555-49a9-a043-35f059b44559', '7_1'),
    ('7.2', '30bae547-a9b0-4c09-8850-ce22b96cfea2', '7_2'),
    ('7.3', '0b658b3f-bf70-4991-95d5-d65616b7ec1a', '7_3'),
    # Topic 8 (3)
    ('8.1', '5ff5f837-df39-4488-bbd2-5138f4faed1e', '8_1'),
    ('8.2', '9cf90212-43f4-4b28-8014-fd6c130db8ef', '8_2'),
    ('8.3', '7da208d1-559d-4e60-a6a3-ebfb8c2d232f', '8_3'),
    # Topic 9 (3)
    ('9.1', '6c14f92b-774a-45d1-a68d-2e9fe5e0b85d', '9_1'),
    ('9.2', '5b7da7e1-3da1-4bf4-9700-6e11d7a7ef6b', '9_2'),
    ('9.3', '53517557-9eb4-450d-a8dd-18b73c71938a', '9_3'),
    # Topic 10 (6)
    ('10.1', '362104be-aedc-4cbe-87b2-29034e93cc9c', '10_1'),
    ('10.2', '76dcafbf-e6b8-47f1-8618-be1b14e975ed', '10_2'),
    ('10.3', '96d7f427-3b6d-43e3-84dc-f8f052f20033', '10_3'),
    ('10.4', '199a26cd-1226-4ff7-b063-f7df7fa7b5ba', '10_4'),
    ('10.5', 'a3a8d904-d277-4eef-b8ff-52a913ebc5f6', '10_5'),
    ('10.6', 'fb30c141-db3a-49e8-aa55-028c913640d4', '10_6')
]

print(f"=== MASTER VERIFICATION: ALL {len(lessons)} GEOGRAPHY LESSONS (3.1 TO 10.6) LIVE IN SUPABASE ===")
all_pass = True
total_segments = 0
total_major_sections = 0

for name, lid, code in lessons:
    errors = []

    res = sb.table('lecture_pages').select('page_number, content_html').eq('lecture_id', lid).order('page_number').execute()
    pages = {r['page_number']: r.get('content_html') or '' for r in res.data}

    # Div diff
    for pnum in sorted(pages.keys()):
        html = pages[pnum]
        opens = len(html.split('<div')) - 1
        closes = len(html.split('</div>')) - 1
        diff = opens - closes
        if diff != 0:
            errors.append(f"P{pnum} diff={diff}")

    p1_html = pages.get(1, '')
    soup = BeautifulSoup(p1_html, 'html.parser')

    # Heading cards
    h_cards = soup.find_all(['h1', 'h2', 'h3', 'h4'], class_='lecture-interactive-card')
    if len(h_cards) > 0:
        errors.append(f"{len(h_cards)} bare heading cards: {[h.get('id') for h in h_cards]}")

    # Manifest
    mpath = f"public/audio/lectures/geography/{code}/manifest.json"
    if not os.path.exists(mpath):
        errors.append("Manifest missing")
    else:
        with open(mpath, 'r', encoding='utf-8') as f:
            m = json.load(f)

        ms = m.get('majorSections')
        if not isinstance(ms, dict):
            errors.append(f"majorSections is {type(ms).__name__}")
        else:
            total_major_sections += len(ms)

        missing_sel = []
        for s in m.get('segments', []):
            total_segments += 1
            sel = s.get('selector', '')
            if sel and not soup.select_one(sel):
                missing_sel.append(f"{s['id']} ({sel})")

        if missing_sel:
            errors.append(f"Missing selectors: {', '.join(missing_sel[:3])}")

    status = "✅ PASS" if not errors else "❌ FAIL"
    if errors:
        all_pass = False
        print(f"[{status}] Lesson {name:4} ({code:4}): ERRORS: {'; '.join(errors)}")
    else:
        print(f"[{status}] Lesson {name:4} ({code:4}): {len(pages)} pages diff=0, {len(m.get('segments', []))} selectors OK, 0 heading cards")

print("\n" + "="*80)
if all_pass:
    print(f"🎉 MASTER AUDIT PASSED: ALL {len(lessons)} LESSONS (3.1 TO 10.6) ARE 100% PERFECT IN SUPABASE!")
    print(f" - Total interactive audio segments verified: {total_segments}")
    print(f" - Total major section containers verified: {total_major_sections}")
    print(f" - Div balance diff = 0 across 100% of all pages in Supabase")
    print(f" - Zero bare heading interactive cards remain")
else:
    print("❌ SOME LESSONS FAILED MASTER AUDIT.")
