import os
import sys
import re
import json
from supabase import create_client

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

with open('.env', 'r', encoding='utf-8') as f:
    env = f.read()

URL = re.search(r'^VITE_SUPABASE_URL=(.*)$', env, re.M).group(1).strip()
KEY = re.search(r'^VITE_SUPABASE_ANON_KEY=(.*)$', env, re.M).group(1).strip()
sb = create_client(URL, KEY)

for lec_num in range(1, 24):
    manifest_path = f'public/audio/lectures/economics/{lec_num}/manifest.json'
    if not os.path.exists(manifest_path):
        print(f"Lec {lec_num}: Manifest not found!")
        continue
    with open(manifest_path, 'r', encoding='utf-8') as f:
        m = json.load(f)
    lec_id = m['lectureId']
    segments = m['segments']
    
    p1 = sb.table('lecture_pages').select('content_html').eq('lecture_id', lec_id).eq('page_number', 1).execute()
    p2 = sb.table('lecture_pages').select('content_html').eq('lecture_id', lec_id).eq('page_number', 2).execute()
    
    p1_html = p1.data[0]['content_html'] if p1.data else ''
    p2_html = p2.data[0]['content_html'] if p2.data else ''
    
    p1_matches = len(re.findall(r'data-lecture-section', p1_html))
    p2_matches = len(re.findall(r'data-lecture-section', p2_html))
    
    missing_in_p1 = []
    for s in segments:
        sid = s['id']
        if f'data-lecture-section="{sid}"' not in p1_html:
            missing_in_p1.append(sid)
            
    print(f"Lec {lec_num:02d} ({lec_id[:8]}...): {len(segments)} segments | P1: {p1_matches} matches (missing: {missing_in_p1}) | P2: {p2_matches} matches")
