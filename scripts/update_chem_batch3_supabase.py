import os
import sys
import re
from supabase import create_client

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

sys.path.insert(0, os.path.dirname(__file__))
from build_chem_batch3_html import build_c9_html, build_c10_html, build_c11_html, build_c12_html

with open('.env', 'r', encoding='utf-8') as f:
    env = f.read()

URL = re.search(r'^VITE_SUPABASE_URL=(.*)$', env, re.M).group(1).strip()
KEY = re.search(r'^VITE_SUPABASE_ANON_KEY=(.*)$', env, re.M).group(1).strip()
sb = create_client(URL, KEY)

LECTURES = [
    ("c9", "d34bbfa2-7449-4192-b471-3a6a8ba49257", "C9: Metals", build_c9_html),
    ("c10", "9d61f516-a24c-4485-8490-8485604130ec", "C10: Chemistry of the environment", build_c10_html),
    ("c11", "69b82c81-05a0-40a8-816f-c21a882cef54", "C11: Organic chemistry", build_c11_html),
    ("c12", "d51b5192-ff57-48a0-bcd9-d4f8a7d10757", "C12: Experimental techniques and Chemical analysis", build_c12_html),
]

def main():
    print("=====================================================================")
    print("DEPLOYING CHEMISTRY BATCH 3 (C9-C12) TO SUPABASE")
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

    print("\n🎉 ALL BATCH 3 (C9-C12) LECTURES SUCCESSFULLY DEPLOYED TO SUPABASE!")

if __name__ == '__main__':
    main()
