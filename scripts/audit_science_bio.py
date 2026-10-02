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

bio_lectures = [
    ('B1', '1231b474-8a99-4330-b45d-fdda19a802fe', 'b1', 'Characteristics of living organisms'),
    ('B2', '7b3c2e0a-b0d5-4716-a574-6f1c5c379c7c', 'b2', 'Cells and organisms'),
    ('B3', '9a23109e-ad73-4fcf-a599-9605cc4906eb', 'b3', 'Movement into and out of cells'),
    ('B4', '757409b3-5cec-4e1f-8877-18d81e440103', 'b4', 'Biological molecules'),
    ('B5', '8ab2afa2-59e3-4c56-8971-8d93dec5ad8e', 'b5', 'Enzymes'),
    ('B6', '1d6a6b7b-ae57-404f-9ad1-58b11219b4d1', 'b6', 'Plant Nutrition'),
    ('B7', 'cbebf582-244c-48bf-a586-c6c1922d8e20', 'b7', 'Human nutrition'),
    ('B8', 'e2819423-13ed-47a2-bd80-9a083989e8bd', 'b8', 'Transport in plants'),
    ('B9', 'a79dd569-671f-4559-84a3-eee1e6018172', 'b9', 'Transport in animals'),
    ('B10', '04d34896-13fb-411b-9e13-2bc3f9725136', 'b10', 'Diseases and immunity'),
    ('B11', '39003a2f-708e-47fe-b8ad-7aae073273a3', 'b11', 'Gas exchange and respiration'),
    ('B12', '58e65add-a67a-4b90-8b84-52de1a2840be', 'b12', 'Respiration'),
    ('B13', '2637d6ee-fd5f-48fc-aa7a-fc794fb3e561', 'b13', 'Coordination and response'),
    ('B14', '7ed510d0-acd2-4d0a-9079-1f1e4e4fc463', 'b14', 'Drugs'),
    ('B15', 'deb8222d-2b75-42a3-b454-9601fbfa1bd2', 'b15', 'Reproduction'),
    ('B16', 'd48c8f84-ba93-49d4-bf61-c7890bd6d2ce', 'b16', 'Inheritance'),
    ('B17', '24f0deeb-3cd9-4b82-b253-5a070ca31275', 'b17', 'Variation and selection'),
    ('B18', 'cbeb6b74-e9c2-4a91-b39f-decb63e72ec0', 'b18', 'Organisms and their environment'),
    ('B19', '298327a8-455a-44d5-9a4c-164e2653c456', 'b19', 'Human influences on ecosystems')
]

print(f"=== INITIAL AUDIT: ALL {len(bio_lectures)} BIOLOGY LECTURES (0654) ===")

total_segs = 0
total_missing_audio = 0
ms_list_count = 0
ms_dict_count = 0

os.makedirs('scripts/raw_science_bio', exist_ok=True)

for name, lid, code, title in bio_lectures:
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
        with open(f"scripts/raw_science_bio/{code}_p{pnum}.html", 'w', encoding='utf-8') as f:
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
