import os
import sys
import re
from supabase import create_client
from build_econ_topic3_html import (
    build_c16_html, build_c17_html, build_c18_html, build_c19_html,
    build_c20_html, build_c21_html, build_c22_html, build_c23_html
)
from build_econ_topic3_audio import (
    LEC16_ID, LEC17_ID, LEC18_ID, LEC19_ID, LEC20_ID, LEC21_ID, LEC22_ID, LEC23_ID
)

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# Environment & Supabase
env_path = os.path.join(os.path.dirname(__file__), '..', '.env')
with open(env_path, 'r', encoding='utf-8') as f:
    env = f.read()

URL = re.search(r'^VITE_SUPABASE_URL=(.*)$', env, re.M).group(1).strip()
KEY = re.search(r'^VITE_SUPABASE_ANON_KEY=(.*)$', env, re.M).group(1).strip()
sb = create_client(URL, KEY)

lectures = [
    (16, LEC16_ID, build_c16_html),
    (17, LEC17_ID, build_c17_html),
    (18, LEC18_ID, build_c18_html),
    (19, LEC19_ID, build_c19_html),
    (20, LEC20_ID, build_c20_html),
    (21, LEC21_ID, build_c21_html),
    (22, LEC22_ID, build_c22_html),
    (23, LEC23_ID, build_c23_html),
]

print("=== DEPLOYING TOPIC 3 (LECTURES 16 - 23) PAGE 1 TO SUPABASE ===")
for lec_num, lec_id, builder in lectures:
    html = builder()
    diff = html.count('<div') - html.count('</div')
    has_sr = bool(re.search(r'Thanh Tài liệu học tập|Study Resources Bar', html, re.I))
    assert diff == 0, f"Div imbalance in Lecture {lec_num}: {diff}"
    assert not has_sr, f"Study resources found in Lecture {lec_num}"
    
    res = sb.table('lecture_pages').update({
        'content_html': html
    }).eq('lecture_id', lec_id).eq('page_number', 1).execute()
    
    print(f"Lec {lec_num:02d} ({lec_id}): Updated {len(res.data)} page(s) in Supabase. diff={diff}, has_sr={has_sr}")

print("\n🎉 ALL 8 LECTURES OF TOPIC 3 DEPLOYED TO SUPABASE SUCCESSFULLY!")
