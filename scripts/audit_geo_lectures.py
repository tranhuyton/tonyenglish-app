import os
import sys
import re
from supabase import create_client

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

with open('.env', 'r', encoding='utf-8') as f:
    env = f.read()

URL = re.search(r'^VITE_SUPABASE_URL=(.*)$', env, re.M).group(1).strip()
KEY = re.search(r'^VITE_SUPABASE_ANON_KEY=(.*)$', env, re.M).group(1).strip()
sb = create_client(URL, KEY)

lecs = [
    ('3.1', '1b4caf37-15e4-475a-939c-e6490b366fd0', '3_1'),
    ('3.2', '93a28707-1b95-4ed2-a3ff-4789143118cd', '3_2'),
    ('3.3', '7d543b73-837d-4129-afc6-7196df47b6f6', '3_3'),
    ('3.4', 'c5ce49f0-7b81-4843-a477-3ee46e41928e', '3_4'),
    ('4.1', 'e5fde4e7-a1e6-4b3c-aeb2-756155f06ff5', '4_1'),
    ('4.2', 'f45dd9b1-ef60-4521-a067-04bd896fc7e2', '4_2'),
    ('4.3', '1f909afc-865f-46d0-bb20-2e6d474fa87b', '4_3'),
    ('4.4', 'c81dc416-7aa4-4e26-a2af-341d6c03fa52', '4_4'),
    ('5.1', '7c30919a-5d22-425a-a167-21e5de07d203', '5_1'),
    ('5.2', '23eee2fb-427c-4843-8d2d-ec296188730d', '5_2'),
    ('5.3', '36e35bdb-986b-4cd5-b8df-6bb0f93282e5', '5_3')
]

print("=== AUDIT GEOGRAPHY 3.1 TO 5.3 IN SUPABASE ===")
for name, lid, code in lecs:
    pages = sb.table('lecture_pages').select('page_number, content_html').eq('lecture_id', lid).order('page_number').execute()
    p_info = []
    for p in pages.data:
        pnum = p['page_number']
        html = p.get('content_html') or ''
        has_sr = 'Study Resources' in html or ('Textbook' in html and 'Paper 1' in html) or 'Tài liệu học tập' in html
        h2_cards = len(re.findall(r'<h[1-6][^>]*class=[\'"][^\'"]*lecture-interactive-card', html))
        div_cards = len(re.findall(r'<div[^>]*class=[\'"][^\'"]*lecture-interactive-card', html))
        opens = len(html.split('<div')) - 1
        closes = len(html.split('</div>')) - 1
        diff = opens - closes
        p_info.append(f"P{pnum}(diff={diff}, sr={has_sr}, h2={h2_cards}, divCards={div_cards})")
    print(f"Lesson {name:4} ({code:4}): {len(pages.data)} pages | {', '.join(p_info)}")
