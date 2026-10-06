import sys
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
from bs4 import BeautifulSoup
import json

topics = ['3_1', '3_2', '3_3', '3_4', '4_1', '4_2', '4_3', '4_4', '5_1', '5_2', '5_3']

for t in topics:
    mpath = f"public/audio/lectures/geography/{t}/manifest.json"
    hpath = f"scripts/raw_geo/{t}_p1.html"
    with open(mpath, 'r', encoding='utf-8') as f:
        m = json.load(f)
    with open(hpath, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f.read(), 'html.parser')
        
    print(f"\n==========================================")
    print(f"LESSON {t}: {m.get('lectureTitle')}")
    ms = m.get('majorSections', {})
    print(f"Major sections ({len(ms)}):")
    for sec_id, rng in ms.items():
        # find segment
        seg = next((s for s in m['segments'] if s['id'] == sec_id), None)
        sel = seg.get('selector') if seg else f"#{sec_id.replace('_', '-')}"
        el = soup.select_one(sel) if sel else None
        tag_info = f"<{el.name} id='{el.get('id')}'>" if el else "NOT FOUND"
        has_card = 'lecture-interactive-card' in el.get('class', []) if el else False
        style = el.get('style', '') if el else ''
        has_border = 'border' in style
        print(f"  {sec_id:25} ({rng['start']:2}-{rng['end']:2}) -> {tag_info:35} | card={has_card} | border={has_border}")
