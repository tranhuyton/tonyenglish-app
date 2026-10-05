import os
import sys
import re
from supabase import create_client
from build_econ_topic2_html import (
    build_c5_html, build_c6_html, build_c7_html, build_c8_html, build_c9_html,
    build_c10_html, build_c11_html, build_c12_html, build_c13_html, build_c14_html, build_c15_html
)
from build_econ_topic2_audio import (
    LEC5_ID, LEC6_ID, LEC7_ID, LEC8_ID, LEC9_ID, LEC10_ID, LEC11_ID, LEC12_ID, LEC13_ID, LEC14_ID, LEC15_ID
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
    (5, LEC5_ID, build_c5_html),
    (6, LEC6_ID, build_c6_html),
    (7, LEC7_ID, build_c7_html),
    (8, LEC8_ID, build_c8_html),
    (9, LEC9_ID, build_c9_html),
    (10, LEC10_ID, build_c10_html),
    (11, LEC11_ID, build_c11_html),
    (12, LEC12_ID, build_c12_html),
    (13, LEC13_ID, build_c13_html),
    (14, LEC14_ID, build_c14_html),
    (15, LEC15_ID, build_c15_html),
]

print("=== DEPLOYING TOPIC 2 (LECTURES 5 - 15) PAGE 1 TO SUPABASE ===")
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

print("\n🎉 ALL 11 LECTURES OF TOPIC 2 DEPLOYED TO SUPABASE SUCCESSFULLY!")
