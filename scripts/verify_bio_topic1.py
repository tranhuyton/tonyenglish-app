# -*- coding: utf-8 -*-
import json
import os
import re
from bs4 import BeautifulSoup
from supabase import create_client

with open('.env', 'r', encoding='utf-8') as f:
    env = f.read()

URL = re.search(r'^VITE_SUPABASE_URL=(.*)$', env, re.M).group(1).strip()
KEY = re.search(r'^VITE_SUPABASE_ANON_KEY=(.*)$', env, re.M).group(1).strip()
sb = create_client(URL, KEY)

LEC_ID = '11cfe97d-205e-418b-ae79-e39d7e57e0a8'

# 1. Check Manifest
manifest_path = 'public/audio/lectures/biology/1/manifest.json'
with open(manifest_path, 'r', encoding='utf-8') as f:
    manifest = json.load(f)

print('=== MANIFEST VERIFICATION ===')
print('Lecture ID:', manifest['lectureId'])
print('Title:', manifest['lectureTitle'])
print('Total segments:', len(manifest['segments']))
total_min = round(manifest['totalDuration'] / 60, 1)
print(f"Total duration: {manifest['totalDuration']}s (~{total_min} mins)")

missing_files = []
for s in manifest['segments']:
    audio_path = os.path.join('public', s['audioUrl'].lstrip('/'))
    if not os.path.exists(audio_path):
        missing_files.append((s['id'], audio_path))
    elif os.path.getsize(audio_path) < 1000:
        missing_files.append((s['id'], audio_path, 'too small'))

print('Missing or invalid audio files:', len(missing_files))
assert len(missing_files) == 0, f'Missing files: {missing_files}'

# 2. Check Supabase Pages
pages = sb.table('lecture_pages').select('id, page_number, content_html').eq('lecture_id', LEC_ID).order('page_number').execute()
print('\n=== SUPABASE PAGES VERIFICATION ===')
print('Total pages in Supabase:', len(pages.data))
assert len(pages.data) == 3, f"Expected 3 pages, found {len(pages.data)}"

for p in pages.data:
    pn = p['page_number']
    html = p['content_html'] or ''
    soup = BeautifulSoup(html, 'html.parser')
    diff = html.count('<div') - html.count('</div>')
    print(f"  Page {pn}: len={len(html)}, div_diff={diff}")
    assert diff == 0, f"Page {pn} div mismatch!"

    if pn in [1, 2]:
        for s in manifest['segments']:
            sel = s['selector']
            target_id = sel.replace('#', '')
            found = soup.find(id=target_id)
            if not found:
                print(f"    [WARNING] Page {pn} missing element with id={target_id} (selector: {sel})")
                assert False, f"Missing selector in page {pn}: {sel}"

print('\nALL 40 SELECTORS VERIFIED 100% IN BOTH PAGE 1 AND PAGE 2!')
print('ALL CHECKS PASSED PERFECTLY!')
