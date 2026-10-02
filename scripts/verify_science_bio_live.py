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

print("=== LIVE VERIFICATION: ALL 19 SCIENCE BIOLOGY LESSONS DIRECTLY FROM SUPABASE ===")
all_pass = True
total_segments = 0
total_major_sections = 0

for name, lid, code in bio_lectures:
    mpath = f"public/audio/lectures/science/{code}/manifest.json"
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
        total_segments += 1
        sel = s.get('selector', '')
        if sel and not soup.select_one(sel):
            missing_sel.append(f"{s['id']} ({sel})")

    # 4. Check majorSections
    ms = m.get('majorSections', {})
    is_ms_dict = isinstance(ms, dict)
    if is_ms_dict:
        total_major_sections += len(ms)

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

print("\n" + "="*80)
if all_pass:
    print(f"🎉 ALL 19 SCIENCE BIOLOGY LESSONS LIVE IN SUPABASE ARE 100% VERIFIED AND PERFECT!")
    print(f" - Total interactive audio segments verified: {total_segments}")
    print(f" - Total major section keys in manifests: {total_major_sections}")
    print(f" - All pages in Supabase have div diff = 0")
    print(f" - Zero bare heading interactive cards remain")
else:
    print("❌ SOME LESSONS FAILED LIVE VERIFICATION.")
