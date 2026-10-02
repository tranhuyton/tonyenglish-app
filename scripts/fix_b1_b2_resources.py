import sys
import os
import re
from supabase import create_client

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

with open('.env', 'r', encoding='utf-8') as f:
    env = f.read()

URL = re.search(r'^VITE_SUPABASE_URL=(.*)$', env, re.M).group(1).strip()
KEY = re.search(r'^VITE_SUPABASE_ANON_KEY=(.*)$', env, re.M).group(1).strip()
sb = create_client(URL, KEY)

for num, lid in [(1, '1231b474-8a99-4330-b45d-fdda19a802fe'), (2, '7b3c2e0a-b0d5-4716-a574-6f1c5c379c7c')]:
    res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).single().execute()
    html = res.data['content_html']
    
    # 1. Remove study resources div
    html = re.sub(r'<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro"[^>]*>.*?</div>\s*', '', html, flags=re.DOTALL)
    
    # 2. Change sec-banner-en to sec-header interactive card
    html = re.sub(r'<div id="sec-banner-en"', '<div id="sec-header" class="lecture-interactive-card" data-lecture-section="intro"', html)
    
    opens = len(re.findall(r'<div\b[^>]*>', html, flags=re.IGNORECASE))
    closes = len(re.findall(r'</div>', html, flags=re.IGNORECASE))
    diff = opens - closes
    print(f'B{num} P1: opens={opens}, closes={closes}, diff={diff}')
    if diff != 0:
        raise ValueError(f'B{num} diff != 0')
        
    sb.table('lecture_pages').update({'content_html': html}).eq('lecture_id', lid).eq('page_number', 1).execute()
    print(f'Updated B{num} P1 in Supabase!')
