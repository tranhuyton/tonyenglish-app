import os
import sys
import re
import json
from supabase import create_client
from bs4 import BeautifulSoup

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

print("=== LIVE VERIFICATION FROM SUPABASE FOR LESSONS 9.1 TO 10.6 ===")
all_pass = True

for name, lid, code in lecs:
    mpath = f"public/audio/lectures/geography/{code}/manifest.json"
    with open(mpath, 'r', encoding='utf-8') as f:
        m = json.load(f)

    pages = sb.table('lecture_pages').select('page_number, content_html').eq('lecture_id', lid).order('page_number').execute()
    
    # 1. Check all pages for div diff
    page_diffs = []
    p1_html = ""
    for p in pages.data:
        pnum = p['page_number']
        ch = p.get('content_html') or ''
        if pnum == 1:
            p1_html = ch
        op = len(ch.split('<div')) - 1
        cl = len(ch.split('</div>')) - 1
        df = op - cl
        if df != 0:
            page_diffs.append(f"P{pnum}: diff={df}")

    # 2. Check heading cards on Page 1
    soup = BeautifulSoup(p1_html, 'html.parser')
    h_cards = soup.find_all(['h1', 'h2', 'h3', 'h4'], class_='lecture-interactive-card')

    # 3. Check selectors on Page 1
    missing_sel = []
    for s in m.get('segments', []):
        sel = s.get('selector', '')
        if sel and not soup.select_one(sel):
            missing_sel.append(f"{s['id']} ({sel})")

    # 4. Check majorSections
    ms = m.get('majorSections', {})
    is_ms_dict = isinstance(ms, dict)

    status = "✅ PASS"
    issues = []
    if page_diffs:
        issues.append(f"Div imbalance: {', '.join(page_diffs)}")
        status = "❌ FAIL"
        all_pass = False
    if len(h_cards) > 0:
        issues.append(f"{len(h_cards)} heading cards remain ({[h.get('id') for h in h_cards]})")
        status = "❌ FAIL"
        all_pass = False
    if missing_sel:
        issues.append(f"Missing selectors: {', '.join(missing_sel)}")
        status = "❌ FAIL"
        all_pass = False
    if not is_ms_dict:
        issues.append("majorSections is not dict")
        status = "❌ FAIL"
        all_pass = False

    issue_str = f" -> Issues: {'; '.join(issues)}" if issues else f" -> All {len(pages.data)} pages diff=0, {len(m.get('segments', []))} selectors OK, 0 heading cards, majorSections dict({len(ms)})"
    print(f"[{status}] Lesson {name:4} ({code:4}){issue_str}")

print("\n" + "="*70)
if all_pass:
    print("🎉 ALL 9 LESSONS LIVE IN SUPABASE ARE 100% VERIFIED AND PERFECT!")
else:
    print("❌ SOME LESSONS FAILED LIVE VERIFICATION.")
