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

chem_phys_lectures = [
    # Chemistry (12)
    ('C1', '3fc0ef74-3661-4f23-a8a8-9c33d11051f5', 'c1'),
    ('C2', 'ee4f94c2-382b-4dbb-aaf8-981e7b0d7223', 'c2'),
    ('C3', 'f0988036-6fd0-4768-993d-a5ea5fe4eb0b', 'c3'),
    ('C4', '4732621b-f827-4b12-934b-3b53e694cc2a', 'c4'),
    ('C5', '71545c83-4d45-4201-978c-aa58d01b57e5', 'c5'),
    ('C6', '7f2b44b2-ba70-4cfc-85b3-3a0709058b46', 'c6'),
    ('C7', '2c83104c-9413-4ee1-bdf3-2c0da8fd96a6', 'c7'),
    ('C8', '856f20da-80e8-4c6a-9cd1-dbe8a1f40828', 'c8'),
    ('C9', 'd34bbfa2-7449-4192-b471-3a6a8ba49257', 'c9'),
    ('C10', '9d61f516-a24c-4485-8490-8485604130ec', 'c10'),
    ('C11', '69b82c81-05a0-40a8-816f-c21a882cef54', 'c11'),
    ('C12', 'd51b5192-ff57-48a0-bcd9-d4f8a7d10757', 'c12'),
    # Physics (6)
    ('P1', '690ff013-5d01-4c1e-8546-25b3cd056e64', 'p1'),
    ('P2', 'dc33ed9d-e328-4f60-8c47-f0dbd103e8c1', 'p2'),
    ('P3', 'eb3ed0a0-bd5e-4c0f-961f-1b9af74bf4a8', 'p3'),
    ('P4', '2a155fd4-9bd1-4136-b7b7-3ce55d6fbb69', 'p4'),
    ('P5', 'a6077865-db01-4785-9ec7-e8b0f531fcdc', 'p5'),
    ('P6', 'd11f8920-fe86-4cd4-ad9a-e8b669bc687b', 'p6')
]

print("=== LIVE VERIFICATION: SUPABASE LECTURE_PAGES FOR CHEMISTRY & PHYSICS (0654) ===")

all_live_ok = True

for name, lid, code in chem_phys_lectures:
    mf_path = f"public/audio/lectures/science/{code}/manifest.json"
    with open(mf_path, 'r', encoding='utf-8') as f:
        mf = json.load(f)
    major_secs = mf.get("majorSections", {})
    
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    if not res.data:
        print(f"❌ {name:4} ({code:4}): No page 1 found in Supabase!")
        all_live_ok = False
        continue
    
    live_html = res.data[0]['content_html']
    
    # 1. Div balance check
    opens = len(re.findall(r'<div\b[^>]*>', live_html, flags=re.IGNORECASE))
    closes = len(re.findall(r'</div>', live_html, flags=re.IGNORECASE))
    diff = opens - closes
    
    # 2. Card tags check
    soup = BeautifulSoup(live_html, 'html.parser')
    h2_cards = [h for h in soup.find_all('h2') if 'lecture-interactive-card' in h.get('class', [])]
    div_cards = [d for d in soup.find_all('div') if 'lecture-interactive-card' in d.get('class', [])]
    
    # 3. Match against manifest
    missing_manifest_secs = []
    for s_key in major_secs.keys():
        elem = soup.find(attrs={"data-lecture-section": s_key})
        if not elem:
            norm_id = "sec-" + s_key.replace("_", "-").replace("sec-", "")
            elem = soup.find(id=norm_id) or soup.find(id=s_key)
        if not elem or elem.name != 'div':
            missing_manifest_secs.append(s_key)
            
    is_ok = (diff == 0) and (len(h2_cards) == 0) and (len(div_cards) > 0) and (len(missing_manifest_secs) == 0)
    if not is_ok:
        all_live_ok = False
        print(f"❌ {name:4} ({code:4}): FAIL -> diff={diff}, h2_cards={len(h2_cards)}, div_cards={len(div_cards)}, missing={missing_manifest_secs}")
    else:
        print(f"✅ {name:4} ({code:4}): PASS -> diff=0, h2_cards=0, div_cards={len(div_cards)}, all {len(major_secs)} manifest sections mapped!")

print("\n" + "="*70)
print(f"OVERALL LIVE AUDIT RESULT: {'ALL 18 LESSONS 100% PERFECT! 🎉' if all_live_ok else 'SOME LESSONS FAILED! ❌'}")
print("="*70)
