import os
import sys
import json
import re
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
    ('C1', '3fc0ef74-3661-4f23-a8a8-9c33d11051f5', 'c1', 'States of matter'),
    ('C2', 'ee4f94c2-382b-4dbb-aaf8-981e7b0d7223', 'c2', 'Atoms elements and compounds'),
    ('C3', 'f0988036-6fd0-4768-993d-a5ea5fe4eb0b', 'c3', 'Stoichiometry'),
    ('C4', '4732621b-f827-4b12-934b-3b53e694cc2a', 'c4', 'Electrochemistry'),
    ('C5', '71545c83-4d45-4201-978c-aa58d01b57e5', 'c5', 'Chemical energetics'),
    ('C6', '7f2b44b2-ba70-4cfc-85b3-3a0709058b46', 'c6', 'Chemical reactions'),
    ('C7', '2c83104c-9413-4ee1-bdf3-2c0da8fd96a6', 'c7', 'Acids bases and salts'),
    ('C8', '856f20da-80e8-4c6a-9cd1-dbe8a1f40828', 'c8', 'Periodic table'),
    ('C9', 'd34bbfa2-7449-4192-b471-3a6a8ba49257', 'c9', 'Metals'),
    ('C10', '9d61f516-a24c-4485-8490-8485604130ec', 'c10', 'Chemistry of the environment'),
    ('C11', '69b82c81-05a0-40a8-816f-c21a882cef54', 'c11', 'Organic chemistry'),
    ('C12', 'd51b5192-ff57-48a0-bcd9-d4f8a7d10757', 'c12', 'Experimental techniques and Chemical analysis'),
    # Physics (6)
    ('P1', '690ff013-5d01-4c1e-8546-25b3cd056e64', 'p1', 'Motion, forces & energy'),
    ('P2', 'dc33ed9d-e328-4f60-8c47-f0dbd103e8c1', 'p2', 'Thermal physics'),
    ('P3', 'eb3ed0a0-bd5e-4c0f-961f-1b9af74bf4a8', 'p3', 'Waves'),
    ('P4', '2a155fd4-9bd1-4136-b7b7-3ce55d6fbb69', 'p4', 'Electricity and magnetism'),
    ('P5', 'a6077865-db01-4785-9ec7-e8b0f531fcdc', 'p5', 'Nuclear physics'),
    ('P6', 'd11f8920-fe86-4cd4-ad9a-e8b669bc687b', 'p6', 'Space physics')
]

print(f"=== INITIAL AUDIT: ALL {len(chem_phys_lectures)} CHEMISTRY & PHYSICS LECTURES (0654) ===")

total_segs = 0
total_missing_audio = 0
ms_list_count = 0
ms_dict_count = 0

os.makedirs('scripts/raw_science_chem_phys', exist_ok=True)

for name, lid, code, title in chem_phys_lectures:
    # 1. Check manifest
    mpath = f"public/audio/lectures/science/{code}/manifest.json"
    if not os.path.exists(mpath):
        print(f"❌ {name:4} ({code:4}): Manifest MISSING at {mpath}")
        continue
    
    with open(mpath, 'r', encoding='utf-8') as f:
        m = json.load(f)
    
    segs = m.get('segments', [])
    total_segs += len(segs)
    
    # Audio files
    missing_audio = []
    for s in segs:
        rel = s.get('audioUrl', '').lstrip('/')
        if not os.path.exists(os.path.join('public', rel)):
            missing_audio.append(s['id'])
    total_missing_audio += len(missing_audio)
    
    # majorSections
    ms = m.get('majorSections')
    if isinstance(ms, dict):
        ms_dict_count += 1
        ms_str = f"dict({len(ms)})"
    elif isinstance(ms, list):
        ms_list_count += 1
        ms_str = f"list({len(ms)}) ⚠️"
    else:
        ms_str = f"{type(ms).__name__} ⚠️"
        
    # 2. Fetch pages from Supabase & save raw HTML
    pages = sb.table('lecture_pages').select('page_number, content_html').eq('lecture_id', lid).order('page_number').execute()
    p1_html = ""
    page_diffs = []
    for p in pages.data:
        pnum = p['page_number']
        ch = p.get('content_html') or ''
        if pnum == 1:
            p1_html = ch
        with open(f"scripts/raw_science_chem_phys/{code}_p{pnum}.html", 'w', encoding='utf-8') as f:
            f.write(ch)
        op = len(ch.split('<div')) - 1
        cl = len(ch.split('</div>')) - 1
        df = op - cl
        if df != 0:
            page_diffs.append(f"P{pnum}(d={df})")
            
    # 3. Check heading cards and selectors on Page 1
    soup = BeautifulSoup(p1_html, 'html.parser')
    h_cards = soup.find_all(['h1', 'h2', 'h3', 'h4'], class_='lecture-interactive-card')
    
    missing_sel = []
    for s in segs:
        sel = s.get('selector', '')
        if sel and not soup.select_one(sel):
            missing_sel.append(f"{s['id']} ({sel})")
            
    diff_info = f"Diffs: [{', '.join(page_diffs)}]" if page_diffs else "Diff=0 (all pages)"
    h_info = f"{len(h_cards)} heading cards" if h_cards else "0 heading cards"
    sel_info = f"Missing sel: {len(missing_sel)}" if missing_sel else f"{len(segs)} sel OK"
    audio_info = f"Missing audio: {len(missing_audio)}" if missing_audio else "Audio OK"
    
    print(f"{name:4} ({code:4}): Pages={len(pages.data)} | {diff_info} | MS: {ms_str:10} | {h_info} | {sel_info} | {audio_info}")

print(f"\nSummary:")
print(f"Total segments: {total_segs}")
print(f"Total missing audio files: {total_missing_audio}")
print(f"majorSections as dict: {ms_dict_count}, as list: {ms_list_count}")
