import os
import sys
import re
from supabase import create_client

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

sys.path.insert(0, os.path.dirname(__file__))
from build_phys_html import (
    build_p1_html,
    build_p2_html,
    build_p3_html,
    build_p4_html,
    build_p5_html,
    build_p6_html
)

with open('.env', 'r', encoding='utf-8') as f:
    env = f.read()

URL = re.search(r'^VITE_SUPABASE_URL=(.*)$', env, re.M).group(1).strip()
KEY = re.search(r'^VITE_SUPABASE_ANON_KEY=(.*)$', env, re.M).group(1).strip()
sb = create_client(URL, KEY)

PHYSICS_LECTURES = [
    ("p1", "690ff013-5d01-4c1e-8546-25b3cd056e64", "P1: Motion, forces & energy", build_p1_html),
    ("p2", "dc33ed9d-e328-4f60-8c47-f0dbd103e8c1", "P2: Thermal physics", build_p2_html),
    ("p3", "eb3ed0a0-bd5e-4c0f-961f-1b9af74bf4a8", "P3: Properties of waves", build_p3_html),
    ("p4", "2a155fd4-9bd1-4136-b7b7-3ce55d6fbb69", "P4: Electricity and magnetism", build_p4_html),
    ("p5", "a6077865-db01-4785-9ec7-e8b0f531fcdc", "P5: Nuclear physics", build_p5_html),
    ("p6", "d11f8920-fe86-4cd4-ad9a-e8b669bc687b", "P6: Space physics", build_p6_html),
]

def main():
    print("=====================================================================")
    print("DEPLOYING PHYSICS (P1-P6) TO SUPABASE")
    print("=====================================================================")

    for code, lec_id, title, builder in PHYSICS_LECTURES:
        html = builder()
        
        # Verify div balance
        opens = len(re.findall(r'<div\b[^>]*>', html))
        closes = len(re.findall(r'</div>', html))
        assert opens == closes, f"Div mismatch for {code}: opens={opens}, closes={closes}"
        assert "Tài liệu học tập" not in html, f"Tài liệu học tập found in {code}"
        assert "Study Resources" not in html, f"Study Resources found in {code}"

        print(f"\nUploading {code.upper()} ({title}) to Supabase (lec_id: {lec_id})...")
        res = sb.table('lecture_pages').update({
            'content_html': html
        }).eq('lecture_id', lec_id).eq('page_number', 1).execute()
        
        print(f"  ✅ Uploaded {code.upper()}: {len(res.data)} page updated.")

    print("\n🎉 ALL PHYSICS (P1-P6) LECTURES SUCCESSFULLY DEPLOYED TO SUPABASE!")

if __name__ == '__main__':
    main()
