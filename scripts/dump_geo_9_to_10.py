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

os.makedirs('scripts/raw_geo', exist_ok=True)

print("=== DUMPING PAGES FOR 9.1 TO 10.6 ===")
for name, lid, code in lecs:
    pages = sb.table('lecture_pages').select('page_number, content_html').eq('lecture_id', lid).order('page_number').execute()
    for p in pages.data:
        pnum = p['page_number']
        html = p.get('content_html') or ''
        fname = f"scripts/raw_geo/{code}_p{pnum}.html"
        with open(fname, 'w', encoding='utf-8') as f:
            f.write(html)
    print(f"Dumped {name:4} ({code:4}) - {len(pages.data)} pages")

print("\n=== AUDITING MANIFESTS & AUDIO FILES ===")
total_segs = 0
total_missing_audio = 0

for name, lid, code in lecs:
    mpath = f"public/audio/lectures/geography/{code}/manifest.json"
    if not os.path.exists(mpath):
        print(f"❌ {name} ({code}): MANIFEST MISSING at {mpath}")
        continue
    with open(mpath, 'r', encoding='utf-8') as f:
        m = json.load(f)
    segs = m.get('segments', [])
    total_segs += len(segs)
    ms = m.get('majorSections')
    is_dict = isinstance(ms, dict)
    
    missing_audio = []
    for s in segs:
        rel = s.get('audioUrl', '').lstrip('/')
        if not os.path.exists(os.path.join('public', rel)):
            missing_audio.append(s.get('id'))
    total_missing_audio += len(missing_audio)
    
    ms_info = f"dict({len(ms)})" if is_dict else f"{type(ms).__name__}"
    print(f"{name:4} ({code:4}): Segs={len(segs):2d}, MajorSecs={ms_info}, MissingAudio={len(missing_audio)}")

print(f"\nTotal segments across 9 lessons: {total_segs}, Total missing audio: {total_missing_audio}")
