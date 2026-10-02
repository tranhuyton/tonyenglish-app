import os
import sys
import re
from supabase import create_client

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

sys.path.insert(0, os.path.dirname(__file__))
from build_chem_batch2_html import build_c5_html, build_c6_html, build_c7_html, build_c8_html

with open('.env', 'r', encoding='utf-8') as f:
    env = f.read()

URL = re.search(r'^VITE_SUPABASE_URL=(.*)$', env, re.M).group(1).strip()
KEY = re.search(r'^VITE_SUPABASE_ANON_KEY=(.*)$', env, re.M).group(1).strip()
sb = create_client(URL, KEY)

LECTURES = [
    ("c5", "71545c83-4d45-4201-978c-aa58d01b57e5", "C5: Chemical energetics", build_c5_html),
    ("c6", "7f2b44b2-ba70-4cfc-85b3-3a0709058b46", "C6: Chemical reactions", build_c6_html),
    ("c7", "2c83104c-9413-4ee1-bdf3-2c0da8fd96a6", "C7: Acids bases and salts", build_c7_html),
    ("c8", "856f20da-80e8-4c6a-9cd1-dbe8a1f40828", "C8: Periodic table", build_c8_html),
]

def main():
    print("=====================================================================")
    print("DEPLOYING CHEMISTRY BATCH 2 (C5-C8) TO SUPABASE")
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

    print("\n🎉 ALL BATCH 2 (C5-C8) LECTURES SUCCESSFULLY DEPLOYED TO SUPABASE!")

if __name__ == '__main__':
    main()
