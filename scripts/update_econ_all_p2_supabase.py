import os
import sys
import re
import json
from supabase import create_client
from bs4 import BeautifulSoup

sys.stdout.reconfigure(encoding='utf-8')

# Import Topic 1
from build_econ_topic1_p2_html import (
    build_c1_p2_html, build_c2_p2_html, build_c3_p2_html, build_c4_p2_html
)

# Import Topic 2
from build_econ_topic2_p2_html import (
    build_c5_p2_html, build_c6_p2_html, build_c7_p2_html, build_c8_p2_html,
    build_c9_p2_html, build_c10_p2_html, build_c11_p2_html, build_c12_p2_html,
    build_c13_p2_html, build_c14_p2_html, build_c15_p2_html
)

# Import Topic 3
from build_econ_topic3_p2_html import (
    build_c16_p2_html, build_c17_p2_html, build_c18_p2_html, build_c19_p2_html,
    build_c20_p2_html, build_c21_p2_html, build_c22_p2_html, build_c23_p2_html
)

# Environment & Supabase
env_path = os.path.join(os.path.dirname(__file__), '..', '.env')
with open(env_path, 'r', encoding='utf-8') as f:
    env = f.read()

URL = re.search(r'^VITE_SUPABASE_URL=(.*)$', env, re.M).group(1).strip()
KEY = re.search(r'^VITE_SUPABASE_ANON_KEY=(.*)$', env, re.M).group(1).strip()
sb = create_client(URL, KEY)

LECTURES = [
    # Topic 1
    (1, "1fba7e8c-742f-4697-b93e-a0205fc7d825", build_c1_p2_html),
    (2, "34bbcc7c-6b51-40fd-9585-9eb3c37da582", build_c2_p2_html),
    (3, "9b0e6a87-ed26-43bb-a20c-ffa636f9ef11", build_c3_p2_html),
    (4, "9d5f779b-5254-48ed-8284-3918eaacd579", build_c4_p2_html),
    # Topic 2
    (5, "d6e6ad94-1106-43ae-b37c-1b36832f03e6", build_c5_p2_html),
    (6, "71e51517-0174-49fc-9796-802abee0c5a5", build_c6_p2_html),
    (7, "06450a33-0477-4bd2-9d1b-4e424f8e973d", build_c7_p2_html),
    (8, "d15b56e7-9b09-4120-829c-1955efd21602", build_c8_p2_html),
    (9, "763cd322-6b7d-43b0-a18d-15da34137d9d", build_c9_p2_html),
    (10, "16314014-7787-41dc-9ff5-47fd1d2c7409", build_c10_p2_html),
    (11, "4a5f97fd-91d2-41f4-8cbb-b928f5aea5e9", build_c11_p2_html),
    (12, "38954a57-c9bc-4714-b53e-e404e78379cd", build_c12_p2_html),
    (13, "6f3173be-e12a-4a93-8f76-8cb09fb026fe", build_c13_p2_html),
    (14, "69df5ed2-ce91-4e2a-b818-0e2957483b12", build_c14_p2_html),
    (15, "1af33337-f02c-45ff-a8d0-040864272c98", build_c15_p2_html),
    # Topic 3
    (16, "3adca75c-b852-48be-9cbf-5074ae12e430", build_c16_p2_html),
    (17, "123d8a13-d619-45cd-b363-702e9039627a", build_c17_p2_html),
    (18, "95fb66bf-66f0-4bbd-a7e4-418f191f487a", build_c18_p2_html),
    (19, "1943e7bc-cdee-45b1-93d5-830b704a4017", build_c19_p2_html),
    (20, "07e42111-1e2c-4810-bce3-02d8df497c97", build_c20_p2_html),
    (21, "604d1490-caed-47aa-a562-a6a902790a30", build_c21_p2_html),
    (22, "d2019792-c956-44e2-98ed-c247617a9162", build_c22_p2_html),
    (23, "4a814791-86ae-4aab-b9e2-a94b2565c55c", build_c23_p2_html),
]

def main():
    print("=" * 70)
    print("DEPLOYING ECONOMICS LECTURES 1 - 23 (PAGE 2 - VIETNAMESE) TO SUPABASE")
    print("=" * 70)

    # Pre-verification
    print("\n[Step 1/2] Pre-verifying all 23 lectures locally...")
    all_ready = []
    for num, lec_id, builder in LECTURES:
        html = builder()
        diff = html.count('<div') - html.count('</div')
        assert diff == 0, f"Lec {num} div imbalance: {diff}"
        assert 'id="sec-header"' in html, f"Lec {num} missing #sec-header"
        assert not re.search(r'Thanh Tài liệu học tập|Study Resources Bar', html, re.I), f"Lec {num} has study resources bar"

        manifest_path = f'public/audio/lectures/economics/{num}/manifest.json'
        with open(manifest_path, 'r', encoding='utf-8') as f:
            manifest = json.load(f)

        soup = BeautifulSoup(html, 'html.parser')
        missing = []
        for s in manifest.get('segments', []):
            sel = s.get('selector', '')
            if sel.startswith('#'):
                if not soup.find(id=sel[1:]):
                    missing.append(sel)
            elif sel.startswith('.'):
                if not soup.find(class_=sel[1:]):
                    missing.append(sel)

        assert not missing, f"Lec {num} missing manifest selectors: {missing}"
        all_ready.append((num, lec_id, html, len(manifest.get('segments', []))))

    print("✅ All 23 lectures passed pre-verification!\n")

    # Supabase deploy
    print("[Step 2/2] Updating Supabase lecture_pages (page_number=2)...")
    for num, lec_id, html, seg_count in all_ready:
        res = sb.table('lecture_pages').update({
            'content_html': html
        }).eq('lecture_id', lec_id).eq('page_number', 2).execute()

        rows_updated = len(res.data) if res.data else 0
        if rows_updated == 1:
            print(f"  ✅ Lec {num:02d} ({lec_id}): Page 2 updated ({seg_count} audio segments, 0 div imbalance).")
        else:
            print(f"  ⚠️ Lec {num:02d} ({lec_id}): Warning - updated {rows_updated} rows!")

    print("\n🎉 ALL 23 LECTURES (PAGE 2) DEPLOYED TO SUPABASE SUCCESSFULLY!")

if __name__ == '__main__':
    main()
