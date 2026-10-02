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

lessons = [
    ('B1', '1231b474-8a99-4330-b45d-fdda19a802fe', 'public/audio/lectures/science/b1/manifest.json'),
    ('B2', '7b3c2e0a-b0d5-4716-a574-6f1c5c379c7c', 'public/audio/lectures/science/b2/manifest.json')
]

print("=== LIVE VERIFICATION: B1 & B2 IN SUPABASE ===")

all_ok = True

for name, lid, mf_path in lessons:
    with open(mf_path, 'r', encoding='utf-8') as f:
        mf = json.load(f)
        
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
    assert res.data, f"No page 1 data for {name}!"
    html = res.data[0]['content_html']
    
    # 1. Div balance
    opens = len(re.findall(r'<div\b[^>]*>', html, flags=re.IGNORECASE))
    closes = len(re.findall(r'</div>', html, flags=re.IGNORECASE))
    diff = opens - closes
    
    # 2. Check no study resources
    has_sr = 'Tài liệu học tập' in html or 'Study Resource' in html or ('Paper 2' in html and 'Textbook' in html)
    
    # 3. Check no h2 cards
    soup = BeautifulSoup(html, 'html.parser')
    h2_cards = [h for h in soup.find_all('h2') if 'lecture-interactive-card' in h.get('class', [])]
    
    # 4. Check segments matching
    missing_segs = []
    for seg in mf['segments']:
        sel = seg['selector']
        elems = soup.select(sel)
        if not elems:
            missing_segs.append((seg['id'], sel))
            
    is_ok = (diff == 0) and (not has_sr) and (len(h2_cards) == 0) and (len(missing_segs) == 0)
    if not is_ok:
        all_ok = False
        print(f"❌ {name}: FAIL -> diff={diff}, has_sr={has_sr}, h2_cards={len(h2_cards)}, missing_segs={missing_segs}")
    else:
        print(f"✅ {name}: PASS -> diff=0, study resources removed, h2_cards=0, all {len(mf['segments'])} segments mapped with interactive cards/elements!")

print(f"\nOVERALL RESULT: {'ALL PASS! 🎉' if all_ok else 'FAILED! ❌'}")
