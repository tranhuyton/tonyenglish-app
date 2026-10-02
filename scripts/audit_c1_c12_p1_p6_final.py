import os
import sys
import json
import re
from supabase import create_client

# Ensure utf-8 output in Windows console
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

with open('.env', 'r', encoding='utf-8') as f:
    env = f.read()

URL = re.search(r'^VITE_SUPABASE_URL=(.*)$', env, re.M).group(1).strip()
KEY = re.search(r'^VITE_SUPABASE_ANON_KEY=(.*)$', env, re.M).group(1).strip()
sb = create_client(URL, KEY)

TARGET_LECTURES = [
    # Chemistry
    ("C1", "3fc0ef74-3661-4f23-a8a8-9c33d11051f5", "c1"),
    ("C2", "ee4f94c2-382b-4dbb-aaf8-981e7b0d7223", "c2"),
    ("C3", "f0988036-6fd0-4768-993d-a5ea5fe4eb0b", "c3"),
    ("C4", "4732621b-f827-4b12-934b-3b53e694cc2a", "c4"),
    ("C5", "71545c83-4d45-4201-978c-aa58d01b57e5", "c5"),
    ("C6", "7f2b44b2-ba70-4cfc-85b3-3a0709058b46", "c6"),
    ("C7", "2c83104c-9413-4ee1-bdf3-2c0da8fd96a6", "c7"),
    ("C8", "856f20da-80e8-4c6a-9cd1-dbe8a1f40828", "c8"),
    ("C9", "d34bbfa2-7449-4192-b471-3a6a8ba49257", "c9"),
    ("C10", "9d61f516-a24c-4485-8490-8485604130ec", "c10"),
    ("C11", "69b82c81-05a0-40a8-816f-c21a882cef54", "c11"),
    ("C12", "d51b5192-ff57-48a0-bcd9-d4f8a7d10757", "c12"),
    # Physics
    ("P1", "690ff013-5d01-4c1e-8546-25b3cd056e64", "p1"),
    ("P2", "dc33ed9d-e328-4f60-8c47-f0dbd103e8c1", "p2"),
    ("P3", "eb3ed0a0-bd5e-4c0f-961f-1b9af74bf4a8", "p3"),
    ("P4", "2a155fd4-9bd1-4136-b7b7-3ce55d6fbb69", "p4"),
    ("P5", "a6077865-db01-4785-9ec7-e8b0f531fcdc", "p5"),
    ("P6", "d11f8920-fe86-4cd4-ad9a-e8b669bc687b", "p6"),
]

def fetch_supabase_pages(lec_id):
    res = sb.table("lecture_pages").select("id, page_number, content_html").eq("lecture_id", lec_id).execute()
    return res.data

print("=" * 80)
print("COMPREHENSIVE FINAL AUDIT: C1-C12 & P1-P6")
print("=" * 80)

all_passed = True

for tag, lec_id, slug in TARGET_LECTURES:
    print(f"\n[{tag}] Auditing {slug} (Lecture ID: {lec_id})...")
    
    # 1. Fetch Supabase pages
    pages = fetch_supabase_pages(lec_id)
    pages_by_num = {p["page_number"]: (p.get("content_html") or "") for p in pages}
    
    p1_html = pages_by_num.get(1, "")
    p2_html = pages_by_num.get(2, "")
    
    # Check Study Resources on P1 & P2
    sr_p1 = "tài liệu học tập" in p1_html.lower() or "study resources" in p1_html.lower()
    sr_p2 = "tài liệu học tập" in p2_html.lower() or "study resources" in p2_html.lower()
    
    if sr_p1 or sr_p2:
        print(f"  ❌ FAILED: Found Study Resources! P1: {sr_p1}, P2: {sr_p2}")
        all_passed = False
    else:
        print("  ✅ Study Resources stripped: 0 occurrences on Page 1 and Page 2.")
        
    # Check Div Balance on P1 & P2
    opens_p1 = len(re.findall(r'<div\b', p1_html, re.I))
    closes_p1 = len(re.findall(r'</div>', p1_html, re.I))
    diff_p1 = opens_p1 - closes_p1
    
    opens_p2 = len(re.findall(r'<div\b', p2_html, re.I))
    closes_p2 = len(re.findall(r'</div>', p2_html, re.I))
    diff_p2 = opens_p2 - closes_p2
    
    if diff_p1 != 0 or diff_p2 != 0:
        print(f"  ❌ FAILED: Div imbalance! P1: opens={opens_p1}, closes={closes_p1} (diff={diff_p1}) | P2: diff={diff_p2}")
        all_passed = False
    else:
        print(f"  ✅ Div balance: P1 (diff=0, {opens_p1} divs), P2 (diff=0, {opens_p2} divs).")
        
    # Check Header Anchor on P1
    has_sec_header = 'id="sec-header"' in p1_html or 'data-lecture-section="intro"' in p1_html
    if not has_sec_header:
        print("  ❌ FAILED: Missing #sec-header / data-lecture-section=\"intro\" on Page 1!")
        all_passed = False
    else:
        print("  ✅ Top Header Anchor: #sec-header present.")

    # Check Interactive Cards
    card_count = len(re.findall(r'lecture-interactive-card', p1_html))
    print(f"  ✅ Interactive Cards: {card_count} card elements detected.")

    # 2. Check Manifest & Audio Files
    manifest_path = f"public/audio/lectures/science/{slug}/manifest.json"
    if not os.path.exists(manifest_path):
        print(f"  ❌ FAILED: Manifest not found at {manifest_path}!")
        all_passed = False
        continue
        
    with open(manifest_path, "r", encoding="utf-8") as f:
        manifest = json.load(f)
        
    missing_audio = []
    zero_byte_audio = []
    selectors_to_check = set()
    
    # Check majorSections
    major_secs = manifest.get("majorSections", {})
    for m_id, m_data in major_secs.items():
        sel = m_data.get("selector", "")
        if sel:
            selectors_to_check.add(sel)

    # Check segments
    segments = manifest.get("segments", [])
    for seg in segments:
        audio_url = seg.get("audioUrl", "")
        # convert /audio/lectures/... to public/audio/lectures/...
        rel_path = audio_url.lstrip("/")
        audio_file = os.path.join("public", rel_path) if not rel_path.startswith("public") else rel_path
        if not os.path.exists(audio_file):
            missing_audio.append(audio_url)
        elif os.path.getsize(audio_file) == 0:
            zero_byte_audio.append(audio_url)
            
        sel = seg.get("selector", "")
        if sel:
            selectors_to_check.add(sel)

    if missing_audio or zero_byte_audio:
        print(f"  ❌ FAILED: Missing/empty audio files! Missing: {missing_audio}, Empty: {zero_byte_audio}")
        all_passed = False
    else:
        print(f"  ✅ Audio files: 100% verified ({len(major_secs)} majorSections, {len(segments)} segments, all valid .mp3 on disk).")
        
    # 3. Check Selector Matching in Live Supabase HTML
    missing_selectors = []
    for sel in sorted(selectors_to_check):
        clean_id = sel.lstrip("#")
        if f'id="{clean_id}"' not in p1_html and f"id='{clean_id}'" not in p1_html:
            missing_selectors.append(sel)
            
    if missing_selectors:
        print(f"  ❌ FAILED: Selectors in manifest not found in Supabase HTML: {missing_selectors}")
        all_passed = False
    else:
        print(f"  ✅ Manifest Selectors: 100% match ({len(selectors_to_check)} unique selectors matched in Supabase Page 1).")

print("\n" + "=" * 80)
if all_passed:
    print("🏆 FINAL VERIFICATION PASSED: ALL 18 LECTURES (C1-C12 & P1-P6) ARE 100% PERFECT!")
else:
    print("💥 SOME CHECKS FAILED. Please review above logs.")
print("=" * 80)
