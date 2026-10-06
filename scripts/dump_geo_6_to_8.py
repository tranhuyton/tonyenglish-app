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
    ('6.1', 'c6fccfc5-088b-4145-9a23-9cbb2df1cce9', '6_1'),
    ('6.2', '5390b0d7-995c-4c18-a092-b5cdd4eda49a', '6_2'),
    ('6.3', '33c91ae9-b13f-49d7-b29f-0c3b794d192d', '6_3'),
    ('7.1', '556bc6b6-1555-49a9-a043-35f059b44559', '7_1'),
    ('7.2', '30bae547-a9b0-4c09-8850-ce22b96cfea2', '7_2'),
    ('7.3', '0b658b3f-bf70-4991-95d5-d65616b7ec1a', '7_3'),
    ('8.1', '5ff5f837-df39-4488-bbd2-5138f4faed1e', '8_1'),
    ('8.2', '9cf90212-43f4-4b28-8014-fd6c130db8ef', '8_2'),
    ('8.3', '7da208d1-559d-4e60-a6a3-ebfb8c2d232f', '8_3')
]

os.makedirs('scripts/raw_geo', exist_ok=True)

print("=== DUMPING PAGES FOR 6.1 TO 8.3 ===")
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
