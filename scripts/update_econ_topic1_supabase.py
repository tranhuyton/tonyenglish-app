import os
import sys
import re
from supabase import create_client

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

sys.path.insert(0, os.path.dirname(__file__))
from build_econ_topic1_html import build_c1_html, build_c2_html, build_c3_html, build_c4_html

with open('.env', 'r', encoding='utf-8') as f:
    env = f.read()

URL = re.search(r'^VITE_SUPABASE_URL=(.*)$', env, re.M).group(1).strip()
KEY = re.search(r'^VITE_SUPABASE_ANON_KEY=(.*)$', env, re.M).group(1).strip()
sb = create_client(URL, KEY)

LECTURES = [
    ("1", "1fba7e8c-742f-4697-b93e-a0205fc7d825", "1. The Basic Economic Problem", build_c1_html),
    ("2", "34bbcc7c-6b51-40fd-9585-9eb3c37da582", "2. The Factors of Production", build_c2_html),
    ("3", "9b0e6a87-ed26-43bb-a20c-ffa636f9ef11", "3. Opportunity Cost", build_c3_html),
    ("4", "9d5f779b-5254-48ed-8284-3918eaacd579", "4. Production Possibility Curve", build_c4_html),
]

def main():
    print("=====================================================================")
    print("DEPLOYING ECONOMICS TOPIC 1 (LECTURES 1 - 4) TO SUPABASE")
    print("=====================================================================")

    for code, lec_id, title, builder in LECTURES:
        html = builder()
        
        # Verify div balance
        opens = len(re.findall(r'<div\b[^>]*>', html))
        closes = len(re.findall(r'</div>', html))
        assert opens == closes, f"Div mismatch for Lec {code}: opens={opens}, closes={closes}"
        assert "Tài liệu học tập" not in html, f"Tài liệu học tập found in Lec {code}"
        assert "Study Resources" not in html, f"Study Resources found in Lec {code}"
        assert 'id="sec-header"' in html, f"Missing #sec-header in Lec {code}"

        print(f"Deploying Lecture {code}: {title} (ID: {lec_id})...")
        res = sb.table('lecture_pages').update({
            'content_html': html
        }).eq('lecture_id', lec_id).eq('page_number', 1).execute()

        print(f"  ✅ Page 1 updated in Supabase ({len(res.data)} rows, diff={opens-closes}).")

    print("\n🎉 ALL 4 LECTURES IN TOPIC 1 DEPLOYED SUCCESSFULLY TO SUPABASE!")

if __name__ == '__main__':
    main()
