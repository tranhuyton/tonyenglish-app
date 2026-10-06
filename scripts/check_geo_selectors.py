import os
import sys
import json
from bs4 import BeautifulSoup

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

topics = ['3_1', '3_2', '3_3', '3_4', '4_1', '4_2', '4_3', '4_4', '5_1', '5_2', '5_3']

for t in topics:
    mpath = f"public/audio/lectures/geography/{t}/manifest.json"
    hpath = f"scripts/raw_geo/{t}_p1.html"
    
    with open(mpath, 'r', encoding='utf-8') as f:
        m = json.load(f)
    with open(hpath, 'r', encoding='utf-8') as f:
        html = f.read()
        
    soup = BeautifulSoup(html, 'html.parser')
    
    print(f"\n==========================================")
    print(f"LESSON {t}: {m.get('lectureTitle')}")
    print(f"==========================================")
    
    # Check majorSections
    ms = m.get('majorSections', {})
    print(f"MajorSections ({len(ms)}):")
    for sec_id, rng in ms.items():
        print(f"  {sec_id:25} -> {rng}")
        
    # Check each segment's selector in HTML
    missing_selectors = []
    h_selectors = []
    div_selectors = []
    g_selectors = []
    
    for seg in m.get('segments', []):
        sel = seg.get('selector', '')
        el = soup.select_one(sel) if sel else None
        if not el:
            missing_selectors.append(f"{seg['id']}: '{sel}' NOT FOUND")
        else:
            tag = el.name
            classes = el.get('class', [])
            has_card_class = 'lecture-interactive-card' in classes
            if tag in ['h1', 'h2', 'h3', 'h4']:
                h_selectors.append(f"{seg['id']} (<{tag} id='{el.get('id')}'>, card={has_card_class})")
            elif tag == 'div':
                div_selectors.append(f"{seg['id']} (<div id='{el.get('id')}'>, card={has_card_class})")
            elif tag == 'g':
                g_selectors.append(f"{seg['id']} (<g id='{el.get('id')}'>, card={has_card_class})")
            else:
                print(f"  Other tag: {seg['id']} -> <{tag}>")
                
    if missing_selectors:
        print(f"❌ MISSING SELECTORS ({len(missing_selectors)}):")
        for ms in missing_selectors:
            print(f"   {ms}")
    else:
        print("✅ ALL selectors exist in HTML!")
        
    if h_selectors:
        print(f"⚠️ HEADINGS WITH SELECTORS ({len(h_selectors)}):")
        for hs in h_selectors:
            print(f"   {hs}")
    else:
        print("✅ No heading selectors (all are div or g cards)!")
        
    print(f"Summary: {len(div_selectors)} divs, {len(g_selectors)} svg <g>, {len(h_selectors)} headings.")
