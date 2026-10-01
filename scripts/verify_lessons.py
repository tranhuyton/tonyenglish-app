import os
import sys
import json
import re
from supabase import create_client

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

with open('.env', 'r', encoding='utf-8') as f:
    env = f.read()

URL = re.search(r'^VITE_SUPABASE_URL=(.*)$', env, re.M).group(1).strip()
KEY = re.search(r'^VITE_SUPABASE_ANON_KEY=(.*)$', env, re.M).group(1).strip()
sb = create_client(URL, KEY)

lessons = [
    ('1.1', '6049f916-3af9-428a-bcd0-ce0574f1d7f7', '1_1'),
    ('1.2', '7027f2e2-0ac5-4ee6-8913-7d93c7857733', '1_2'),
    ('1.3', 'a8ebc541-78ef-4202-96ad-161ed647a1b1', '1_3'),
    ('1.4', '71458f5f-ba54-4ac7-a4c2-8bc68f8f15a0', '1_4'),
    ('1.5', 'a6bf8fbd-9c3d-45a3-8cd7-d63a3e79e7b3', '1_5')
]

print("=== VERIFYING LESSONS 1.1 TO 1.5 ===")
all_ok = True
for name, lid, code in lessons:
    print(f"\n--- Lesson {name} ({code}) ---")
    # 1. Check pages in Supabase
    res = sb.table('lecture_pages').select('page_number, content_html').eq('lecture_id', lid).order('page_number').execute()
    pages = {r['page_number']: r['content_html'] for r in res.data}
    
    for pnum in [1, 2]:
        html = pages.get(pnum, '')
        opens = len(html.split('<div')) - 1
        closes = len(html.split('</div>')) - 1
        diff = opens - closes
        has_sr = 'Study Resources' in html or ('Textbook' in html and 'Paper 1' in html)
        print(f"  Page {pnum}: opens={opens}, closes={closes}, diff={diff}, has_study_resources={has_sr}")
        if diff != 0:
            print(f"  [FAIL] Page {pnum} div mismatch!")
            all_ok = False
        if has_sr:
            print(f"  [FAIL] Page {pnum} contains Study Resources!")
            all_ok = False

    # 2. Check manifest.json
    manifest_path = f"public/audio/lectures/business/{code}/manifest.json"
    if not os.path.exists(manifest_path):
        print(f"  [FAIL] Missing manifest: {manifest_path}")
        all_ok = False
        continue
    
    with open(manifest_path, 'r', encoding='utf-8') as f:
        mf = json.load(f)
    
    segs = mf.get('segments', [])
    major = mf.get('majorSections')
    print(f"  Manifest segments: {len(segs)}, majorSections type: {type(major).__name__}")
    if not isinstance(major, dict):
        print(f"  [FAIL] majorSections is not a dict!")
        all_ok = False

    # Check that audio files exist
    missing_audio = []
    p1_html = pages.get(1, '')
    missing_selectors = []
    for s in segs:
        audio_file = f"public/audio/lectures/business/{code}/{s['id']}.mp3"
        if not os.path.exists(audio_file):
            missing_audio.append(s['id'])
        
        # Check selector in HTML
        sel_list = [sub.strip() for sub in s.get('selector', '').split(',') if sub.strip()]
        for sub_sel in sel_list:
            if sub_sel.startswith('#'):
                el_id = sub_sel[1:]
                if f'id="{el_id}"' not in p1_html and f"id='{el_id}'" not in p1_html:
                    missing_selectors.append(sub_sel)
    
    if missing_audio:
        print(f"  [FAIL] Missing audio files: {missing_audio}")
        all_ok = False
    else:
        print(f"  All {len(segs)} audio files verified.")

    if missing_selectors:
        print(f"  [FAIL] Selectors not found in Page 1 HTML: {missing_selectors}")
        all_ok = False
    else:
        print(f"  All selectors found in Page 1 HTML.")

if all_ok:
    print("\n[SUCCESS] ALL CHECKS PASSED PERFECTLY!")
else:
    print("\n[ERROR] SOME CHECKS FAILED!")
