import os
import sys
import re
from supabase import create_client

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

sys.path.insert(0, os.path.dirname(__file__))
from build_chem_batch1_html import build_c1_html, build_c2_html, build_c3_html, build_c4_html

with open('.env', 'r', encoding='utf-8') as f:
    env = f.read()

URL = re.search(r'^VITE_SUPABASE_URL=(.*)$', env, re.M).group(1).strip()
KEY = re.search(r'^VITE_SUPABASE_ANON_KEY=(.*)$', env, re.M).group(1).strip()
sb = create_client(URL, KEY)

LECTURES = [
    ("c1", "3fc0ef74-3661-4f23-a8a8-9c33d11051f5", "C1: States of matter", build_c1_html),
    ("c2", "ee4f94c2-382b-4dbb-aaf8-981e7b0d7223", "C2: Atoms elements and compounds", build_c2_html),
    ("c3", "f0988036-6fd0-4768-993d-a5ea5fe4eb0b", "C3: Stoichiometry", build_c3_html),
    ("c4", "4732621b-f827-4b12-934b-3b53e694cc2a", "C4: Electrochemistry", build_c4_html),
]

def main():
    print("=====================================================================")
    print("DEPLOYING CHEMISTRY BATCH 1 (C1-C4) TO SUPABASE")
    print("=====================================================================")

    for code, lec_id, title, builder in LECTURES:
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

    print("\n🎉 ALL BATCH 1 (C1-C4) LECTURES SUCCESSFULLY DEPLOYED TO SUPABASE!")

if __name__ == '__main__':
    main()
