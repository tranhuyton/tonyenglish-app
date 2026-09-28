import sys
import os
import json
import re
from bs4 import BeautifulSoup

sys.path.append('scripts')
from audio_lecture_engine import sb

sys.stdout.reconfigure(encoding='utf-8')

TOPICS_6_10 = [
    ("6_1", "c6fccfc5-088b-4145-9a23-9cbb2df1cce9", "6.1 Populations grow and decline"),
    ("6_2", "5390b0d7-995c-4c18-a092-b5cdd4eda49a", "6.2 Population structures change over time"),
    ("6_3", "33c91ae9-b13f-49d7-b29f-0c3b794d192d", "6.3 The causes and impacts of international migration"),
    ("7_1", "556bc6b6-1555-49a9-a043-35f059b44559", "7.1 Where people live"),
    ("7_2", "30bae547-a9b0-4c09-8850-ce22b96cfea2", "7.2 The opportunities and challenges of urbanisation"),
    ("7_3", "0b658b3f-bf70-4991-95d5-d65616b7ec1a", "7.3 The management of urban growth"),
    ("8_1", "5ff5f837-df39-4488-bbd2-5138f4faed1e", "8.1 Measuring development"),
    ("8_2", "9cf90212-43f4-4b28-8014-fd6c130db8ef", "8.2 The world is developing unevenly"),
    ("8_3", "7da208d1-559d-4e60-a6a3-ebfb8c2d232f", "8.3 Achieving sustainable development"),
    ("9_1", "6c14f92b-774a-45d1-a68d-2e9fe5e0b85d", "9.1 Changing employment structures"),
    ("9_2", "5b7da7e1-3da1-4bf4-9700-6e11d7a7ef6b", "9.2 The impact of globalisation and the role of transnational corporations"),
    ("9_3", "53517557-9eb4-450d-a8dd-18b73c71938a", "9.3 Tourism is a growing industry"),
    ("10_1", "362104be-aedc-4cbe-87b2-29034e93cc9c", "10.1 How our food is produced"),
    ("10_2", "76dcafbf-e6b8-47f1-8618-be1b14e975ed", "10.2 The global patterns of food supply and demand"),
    ("10_3", "96d7f427-3b6d-43e3-84dc-f8f052f20033", "10.3 The challenges of food supply"),
    ("10_4", "199a26cd-1226-4ff7-b063-f7df7fa7b5ba", "10.4 How our energy is produced"),
    ("10_5", "a3a8d904-d277-4eef-b8ff-52a913ebc5f6", "10.5 The global patterns of energy supply and demand"),
    ("10_6", "fb30c141-db3a-49e8-aa55-028c913640d4", "10.6 The impacts of energy production"),
]

print(f"{'Code':5s} | {'Manifest':8s} | {'Segs':4s} | {'AudioOK':7s} | {'Pages':5s} | {'CardsInDB':9s} | {'MissingSel':10s} | {'MapsFound':9s} | Status")
print("-" * 95)

detailed_audit = {}

for code, lid, title in TOPICS_6_10:
    m_path = f"public/audio/lectures/geography/{code}/manifest.json"
    manifest_exists = os.path.exists(m_path)
    manifest = None
    segs = 0
    audio_ok_count = 0
    if manifest_exists:
        with open(m_path, 'r', encoding='utf-8') as f:
            manifest = json.load(f)
        segs = len(manifest.get('segments', []))
        for s in manifest.get('segments', []):
            a_url = s.get('audioUrl', '').lstrip('/')
            fp = os.path.join('public', a_url.replace('public/', '')) if not a_url.startswith('public') else a_url
            if os.path.exists(fp) and os.path.getsize(fp) > 0:
                audio_ok_count += 1
                
    pages_res = sb.table('lecture_pages').select('page_number, content_html').eq('lecture_id', lid).order('page_number').execute()
    page_count = len(pages_res.data)
    
    html = ""
    cards = []
    missing_selectors = []
    missing_classes = []
    maps_found = []
    div_diff = 0
    
    if page_count > 0:
        html = pages_res.data[0]['content_html']
        soup = BeautifulSoup(html, 'html.parser')
        cards = soup.find_all(class_='lecture-interactive-card')
        
        # Check div balance
        open_divs = len(re.findall(r'<div\b', html, re.I))
        close_divs = len(re.findall(r'</div>', html, re.I))
        div_diff = open_divs - close_divs
        
        all_ids = set(e.get('id') for e in soup.find_all(id=True))
        
        if manifest:
            for s in manifest.get('segments', []):
                raw_id = s['selector'].lstrip('#')
                if raw_id not in all_ids:
                    missing_selectors.append(s['selector'])
                else:
                    el = soup.find(id=raw_id)
                    cls = el.get('class', [])
                    if isinstance(cls, str):
                        cls = cls.split()
                    if 'lecture-interactive-card' not in cls:
                        missing_classes.append(raw_id)
                        
        # Check interactive map candidates: SVGs, map containers, hotspots, pins
        for svg in soup.find_all('svg'):
            # look for groups with IDs or transforms or tooltips
            hotspot_groups = svg.find_all(['g', 'circle', 'path'], id=True)
            class_groups = svg.find_all(['g', 'circle', 'path'], class_=re.compile(r'node|hotspot|point|marker|pin|band|step|route|region|country', re.I))
            for g in hotspot_groups + class_groups:
                gid = g.get('id') or g.get('class')
                maps_found.append(f"{g.name}#{gid}")
                
        # Also check for interactive map divs/buttons
        for d in soup.find_all(['div', 'button'], class_=re.compile(r'map|hotspot|pin|marker', re.I)):
            did = d.get('id') or d.get('class')
            maps_found.append(f"{d.name}#{did}")
            
    m_status = "YES" if manifest_exists else "NO"
    audio_str = f"{audio_ok_count}/{segs}" if segs > 0 else "0/0"
    
    status = "OK"
    if not manifest_exists or segs == 0:
        status = "NO_MANIFEST"
    elif audio_ok_count < segs:
        status = "MISSING_AUDIO"
    elif len(missing_selectors) > 0:
        status = f"MISSING_{len(missing_selectors)}_SEL"
    elif len(missing_classes) > 0:
        status = f"MISSING_{len(missing_classes)}_CLS"
    elif len(cards) == 0:
        status = "NO_CARDS"
        
    print(f"{code:5s} | {m_status:8s} | {segs:4d} | {audio_str:7s} | {page_count:5d} | {len(cards):9d} | {len(missing_selectors):10d} | {len(maps_found):9d} | {status}")
    
    detailed_audit[code] = {
        "title": title,
        "lid": lid,
        "manifest_exists": manifest_exists,
        "segments": segs,
        "audio_ok": audio_ok_count,
        "page_count": page_count,
        "cards_in_db": len(cards),
        "missing_selectors": missing_selectors,
        "missing_classes": missing_classes,
        "maps_found": maps_found,
        "div_diff": div_diff,
        "status": status
    }

print("\n" + "=" * 80)
print("DEEP DIVE: LECTURES NEEDING FIXES / GENERATION")
print("=" * 80)

for code, d in detailed_audit.items():
    if d['status'] != 'OK':
        print(f"\n[{code}] {d['title']} -> STATUS: {d['status']}")
        if not d['manifest_exists']:
            print("   -> Manifest does NOT exist! No audio generated yet.")
        if d['audio_ok'] < d['segments']:
            print(f"   -> Audio incomplete: {d['audio_ok']}/{d['segments']} files.")
        if d['cards_in_db'] == 0:
            print("   -> Page 1 in DB has 0 interactive cards!")
        if d['missing_selectors']:
            print(f"   -> Missing {len(d['missing_selectors'])} selectors: {d['missing_selectors']}")
        if d['missing_classes']:
            print(f"   -> Elements missing 'lecture-interactive-card' class: {d['missing_classes']}")
        if d['maps_found']:
            print(f"   -> Map/graphic elements found: {len(d['maps_found'])} elements (e.g. {d['maps_found'][:5]})")
