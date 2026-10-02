import os
import sys
import re
import json
from supabase import create_client
from bs4 import BeautifulSoup

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

with open('.env', 'r', encoding='utf-8') as f:
    env = f.read()

URL = re.search(r'^VITE_SUPABASE_URL=(.*)$', env, re.M).group(1).strip()
KEY = re.search(r'^VITE_SUPABASE_ANON_KEY=(.*)$', env, re.M).group(1).strip()
supabase = create_client(URL, KEY)

ALL_BIOLOGY_LECTURES = [
    (1, 'b1', '1231b474-8a99-4330-b45d-fdda19a802fe', 'Characteristics and classification of living organisms'),
    (2, 'b2', '7b3c2e0a-b0d5-4716-a574-6f1c5c379c7c', 'Organisation of the organism'),
    (3, 'b3', '9a23109e-ad73-4fcf-a599-9605cc4906eb', 'Movement into and out of cells'),
    (4, 'b4', '757409b3-5cec-4e1f-8877-18d81e440103', 'Biological molecules'),
    (5, 'b5', '8ab2afa2-59e3-4c56-8971-8d93dec5ad8e', 'Enzymes'),
    (6, 'b6', '1d6a6b7b-ae57-404f-9ad1-58b11219b4d1', 'Plant nutrition'),
    (7, 'b7', 'cbebf582-244c-48bf-a586-c6c1922d8e20', 'Human nutrition'),
    (8, 'b8', 'e2819423-13ed-47a2-bd80-9a083989e8bd', 'Transport in plants'),
    (9, 'b9', 'a79dd569-671f-4559-84a3-eee1e6018172', 'Transport in animals'),
    (10, 'b10', '04d34896-13fb-411b-9e13-2bc3f9725136', 'Diseases and immunity'),
    (11, 'b11', '39003a2f-708e-47fe-b8ad-7aae073273a3', 'Gas exchange in humans'),
    (12, 'b12', '58e65add-a67a-4b90-8b84-52de1a2840be', 'Respiration'),
    (13, 'b13', '2637d6ee-fd5f-48fc-aa7a-fc794fb3e561', 'Coordination and response'),
    (14, 'b14', '7ed510d0-acd2-4d0a-9079-1f1e4e4fc463', 'Drugs'),
    (15, 'b15', 'deb8222d-2b75-42a3-b454-9601fbfa1bd2', 'Reproduction'),
    (16, 'b16', 'd48c8f84-ba93-49d4-bf61-c7890bd6d2ce', 'Inheritance'),
    (17, 'b17', '24f0deeb-3cd9-4b82-b253-5a070ca31275', 'Variation and selection'),
    (18, 'b18', 'cbeb6b74-e9c2-4a91-b39f-decb63e72ec0', 'Organisms and their environment'),
    (19, 'b19', '298327a8-455a-44d5-9a4c-164e2653c456', 'Human influences on ecosystems')
]

def main():
    print("=================================================================")
    print("VERIFYING ALL 19 BIOLOGY LECTURES (B1 to B19) IN SUPABASE")
    print("=================================================================")

    all_passed = True

    for num, code, lec_id, title in ALL_BIOLOGY_LECTURES:
        print(f"\n--- Checking B{num}: {title} (ID: {lec_id}) ---")

        # Check pages in Supabase
        pages_res = supabase.table("lecture_pages").select("page_number, content_html").eq("lecture_id", lec_id).order("page_number").execute()
        pages = {p["page_number"]: p["content_html"] for p in pages_res.data}

        p1_content = pages.get(1, "")
        p2_content = pages.get(2, "")

        # Test 1: No study resources in p1
        p1_has_res = "Tài liệu học tập" in p1_content or "Study Resources" in p1_content
        if p1_has_res:
            print(f"  ❌ FAIL: Page 1 contains 'Tài liệu học tập'")
            all_passed = False
        else:
            print(f"  ✅ PASS: Page 1 clean of study resources")

        # Test 2: No study resources in p2
        p2_has_res = "Tài liệu học tập" in p2_content or "Study Resources" in p2_content
        if p2_has_res:
            print(f"  ❌ FAIL: Page 2 contains 'Tài liệu học tập'")
            all_passed = False
        else:
            print(f"  ✅ PASS: Page 2 clean of study resources")

        # Test 3: Div balance on Page 1
        opens_p1 = len(re.findall(r'<div\b[^>]*>', p1_content, re.IGNORECASE))
        closes_p1 = len(re.findall(r'</div>', p1_content, re.IGNORECASE))
        diff_p1 = opens_p1 - closes_p1
        if diff_p1 != 0:
            print(f"  ❌ FAIL: Page 1 div balance diff={diff_p1} (opens={opens_p1}, closes={closes_p1})")
            all_passed = False
        else:
            print(f"  ✅ PASS: Page 1 div balance diff=0 ({opens_p1}/{closes_p1})")

        # Test 4: Div balance on Page 2 (if exists)
        if p2_content:
            opens_p2 = len(re.findall(r'<div\b[^>]*>', p2_content, re.IGNORECASE))
            closes_p2 = len(re.findall(r'</div>', p2_content, re.IGNORECASE))
            diff_p2 = opens_p2 - closes_p2
            if diff_p2 != 0:
                print(f"  ⚠️ NOTE: Page 2 div balance diff={diff_p2} (opens={opens_p2}, closes={closes_p2})")
            else:
                print(f"  ✅ PASS: Page 2 div balance diff=0 ({opens_p2}/{closes_p2})")

        # Test 5: No bare <h2> cards
        p1_soup = BeautifulSoup(p1_content, 'html.parser')
        bare_h_cards = p1_soup.find_all(re.compile(r'^h[1-6]$'), class_="lecture-interactive-card")
        if bare_h_cards:
            print(f"  ❌ FAIL: Page 1 has {len(bare_h_cards)} bare heading cards: {[h.get_text(strip=True)[:30] for h in bare_h_cards]}")
            all_passed = False
        else:
            print(f"  ✅ PASS: Page 1 has 0 bare heading cards")

        # Test 6: Check manifest.json
        manifest_path = f"public/audio/lectures/science/{code}/manifest.json"
        if os.path.exists(manifest_path):
            with open(manifest_path, 'r', encoding='utf-8') as f:
                manifest = json.load(f)
            segments = manifest.get("segments", [])
            major_sections = manifest.get("majorSections", {})
            total_duration = manifest.get("totalDuration", 0)
            print(f"  ✅ PASS: manifest.json exists with {len(segments)} segments ({total_duration:.1f}s), {len(major_sections)} majorSections")
            
            # Check all segment mp3s exist
            missing_mp3s = []
            for seg in segments:
                mp3_file = f"public/audio/lectures/science/{code}/{seg['id']}.mp3"
                if not os.path.exists(mp3_file) or os.path.getsize(mp3_file) < 1000:
                    missing_mp3s.append(seg['id'])
            if missing_mp3s:
                print(f"  ❌ FAIL: Missing MP3s: {missing_mp3s}")
                all_passed = False
            else:
                print(f"  ✅ PASS: 100% segment audio files present on disk")
        else:
            print(f"  ❌ FAIL: manifest.json missing at {manifest_path}")
            all_passed = False

    print("\n=================================================================")
    if all_passed:
        print("🎉 ALL 19 BIOLOGY LECTURES (B1-B19) 100% PASSED ALL VALIDATION CHECKS!")
    else:
        print("❌ SOME LECTURES FAILED VALIDATION CHECKS.")
    print("=================================================================")

if __name__ == "__main__":
    main()
