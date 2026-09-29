import os
import sys
import re
import json
from bs4 import BeautifulSoup
from supabase import create_client

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

with open('.env', 'r', encoding='utf-8') as f:
    env = f.read()

URL = re.search(r'^VITE_SUPABASE_URL=(.*)$', env, re.M).group(1).strip()
KEY = re.search(r'^VITE_SUPABASE_ANON_KEY=(.*)$', env, re.M).group(1).strip()
sb = create_client(URL, KEY)

with open('src/LectureViewer.tsx', 'r', encoding='utf-8') as f:
    lv_code = f.read()

LECTURES = [
    # Topic 1
    ('1_1', '6049f916-3af9-428a-bcd0-ce0574f1d7f7', '1.1 Business activity'),
    ('1_2', '7027f2e2-0ac5-4ee6-8913-7d93c7857733', '1.2. Classification of businesses'),
    ('1_3', 'a8ebc541-78ef-4202-96ad-161ed647a1b1', '1.3. Enterprise, business growth and size'),
    ('1_4', '71458f5f-ba54-4ac7-a4c2-8bc68f8f15a0', '1.4. Types of business organisation'),
    ('1_5', 'a6bf8fbd-9c3d-45a3-8cd7-d63a3e79e7b3', '1.5. Business objectives and stakeholder objectives'),
    # Topic 2
    ('2_1', 'cd1763a9-f030-4be1-b65b-c6dc6dde91c9', '2.1. Motivating employees'),
    ('2_2', 'fe4967aa-7d4c-480c-af71-e0d867459044', '2.2. Organisation and people management'),
    ('2_3', 'c2d359f6-1921-459e-a295-def7e891c352', '2.3. Recruitment, selection and training of employees'),
    ('2_4', '47166a31-2a55-40ea-a86c-81569cfafa32', '2.4. Internal and external communication'),
    # Topic 3
    ('3_1', '6cbe4a84-26ed-4a1d-933b-5843e9b9a501', '3.1. Marketing, competition and the customer'),
    ('3_2', '356dede8-277a-441a-ad73-ef9384973eb7', '3.2. Market research'),
    ('3_3', '25fe41d9-780d-41a6-876d-fff3e0d854c5', '3.3. The marketing mix'),
    ('3_4', 'c0d60bf9-ad33-456c-807e-9e29318113b8', '3.4. The marketing strategy'),
    # Topic 4
    ('4_1', '1e280547-ce64-44c2-8fcf-997f7d61cacf', '4.1. Production of goods and services'),
    ('4_2', '66589390-767c-4aab-957b-a970fa1a976e', '4.2. Costs, scale of production and break-even analysis'),
    ('4_3', '8f0fd09a-d6e6-438f-a2ab-ddc1447e0b00', '4.3. Quality management'),
    ('4_4', '95eb54ae-44d4-42f6-9d1d-c5c729a69954', '4.4. Location decisions'),
    # Topic 5
    ('5_1', '7b510a8f-757c-4856-9c68-65f98bf96836', '5.1. Business Finance: Needs and Sources'),
    ('5_2', 'dc0411df-d831-468a-9a7d-16fb4009290d', '5.2. Cash flow forecasting and working capital'),
    ('5_3', '71f25939-98d4-4fa3-8227-be8434f64581', '5.3. Income statements'),
    ('5_4', '5421db93-9d7b-4241-b362-171974092a30', '5.4. Statement of financial position'),
    ('5_5', 'd7564fe9-d338-4abc-acf3-affd8cca23fa', '5.5. Analysis of accounts'),
    # Topic 6
    ('6_1', '0e8fbc94-5976-4c7f-8588-471ea93926f5', '6.1. Economic issues'),
    ('6_2', 'a1d571ff-fa12-46c2-a49d-1df88df13214', '6.2. Environmental and ethical issues'),
    ('6_3', '1bc6f5c1-e71b-4d0d-8153-d2f74180a845', '6.3. Business and globalisation')
]

def audit():
    print(f"\n=========================================================================================")
    print(f"AUDITING IGCSE BUSINESS STUDIES (0450) LECTURES: ALL 25 LECTURES")
    print(f"=========================================================================================\n")
    
    passed_count = 0
    total = len(LECTURES)
    
    for code, lid, title in LECTURES:
        manifest_path = os.path.join('public', 'audio', 'lectures', 'business', code, 'manifest.json')
        issues = []
        
        # 1. Manifest
        if not os.path.exists(manifest_path):
            issues.append("Manifest missing")
            print(f"❌ [{code}] {title}: Manifest missing")
            continue
            
        with open(manifest_path, 'r', encoding='utf-8') as f:
            manifest = json.load(f)
            
        segs = manifest.get('segments', [])
        if not segs:
            issues.append("0 segments in manifest")
            
        # 2. Audio files
        for s in segs:
            audio_path = os.path.join('public', 'audio', 'lectures', 'business', code, f"{s['id']}.mp3")
            if not os.path.exists(audio_path) or os.path.getsize(audio_path) < 1000:
                issues.append(f"Audio missing/corrupt: {s['id']}")
                
        # 3. Supabase Page 1 HTML
        res = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).eq('page_number', 1).execute()
        if not res.data:
            issues.append("DB Page 1 missing")
        else:
            html = res.data[0]['content_html']
            diff = len(html.split('<div')) - len(html.split('</div>'))
            if diff != 0:
                issues.append(f"Div balance diff={diff}")
                
            soup = BeautifulSoup(html, 'html.parser')
            for s in segs:
                sel = s['selector']
                el = soup.select_one(sel)
                if not el:
                    issues.append(f"Selector '{sel}' not found in HTML")
                else:
                    if 'lecture-interactive-card' not in el.get('class', []):
                        issues.append(f"Selector '{sel}' missing 'lecture-interactive-card' class")
                    if el.get('data-lecture-section') != s['id']:
                        issues.append(f"Selector '{sel}' data-lecture-section mismatch")
                        
        # 4. LectureViewer map
        if f"'{lid}'" not in lv_code or f"business/{code}/manifest.json" not in lv_code:
            issues.append("LectureViewer.tsx manifest mapping missing")
            
        if issues:
            print(f"❌ [{code}] {title}: {', '.join(issues[:3])}")
        else:
            total_dur = manifest.get('totalDuration', 0)
            print(f"✅ [{code}] {title} | {len(segs)} segments | {total_dur}s | div diff=0 | Wired!")
            passed_count += 1
            
    print(f"\n=========================================================================================")
    print(f"AUDIT SUMMARY: {passed_count}/{total} LECTURES PASSED ALL CHECKS")
    print(f"=========================================================================================\n")
    return passed_count == total

if __name__ == "__main__":
    audit()
