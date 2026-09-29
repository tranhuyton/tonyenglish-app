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

# 21 Biology Topics
LECTURES = [
    ('1', '11cfe97d-205e-418b-ae79-e39d7e57e0a8', 'Topic 1: Characteristics and classification of living organisms'),
    ('2', '2d2545c0-ccb9-4d04-a6fa-f2eec55cdecc', 'Topic 2: Cells and organisms'),
    ('3', '0f5013fb-eaf1-4f79-8f41-c6102d2185a2', 'Topic 3: Movement into and out of cells'),
    ('4', '821ff271-c9ae-493a-b14c-e3f4b074a9d9', 'Topic 4: Biological molecules'),
    ('5', 'a5d1775c-6ecb-4d6c-bc50-8aafbf641c1e', 'Topic 5: Enzymes'),
    ('6', 'e7d6e813-b7b9-4038-9911-8b886978cd07', 'Topic 6: Plant Nutrition'),
    ('7', '85f36013-879b-49a8-a531-69c245a9630e', 'Topic 7: Human nutrition'),
    ('8', '37f08657-58e8-4fad-8035-2d935e1259e8', 'Topic 8: Transport in plants'),
    ('9', 'b50dd00a-e2b4-4dba-8b1d-3f679dadae74', 'Topic 9: Transport in animals'),
    ('10', '62278d87-97ea-4fa5-aa46-748bca28db68', 'Topic 10: Diseases and immunity'),
    ('11', 'da59c2b3-124f-4e25-8537-74059e74f9b0', 'Topic 11: Gas exchange in humans'),
    ('12', 'fb098b77-64fa-463a-9829-64f5c9055de5', 'Topic 12: Respiration'),
    ('13', 'b8f0539e-9361-4ba4-a96e-74c106494ebe', 'Topic 13: Excretion in humans'),
    ('14', 'c9abc870-7cbd-4c7e-b6c9-2d6237ff7670', 'Topic 14: Coordination and response'),
    ('15', 'f87b29a1-56a3-4668-a249-ed9f118d31d8', 'Topic 15: Drugs'),
    ('16', '936affb8-f062-4e39-b415-cc3794fb341e', 'Topic 16: Reproduction'),
    ('17', '77f1f7b8-f30e-4b0b-89e2-2e2482242791', 'Topic 17: Inheritance'),
    ('18', '89750884-8439-4cda-916a-56bf5524741b', 'Topic 18: Variation and selection'),
    ('19', '7b2384dd-b79d-47fe-b36b-7abf36784f06', 'Topic 19: Organisms and their environment'),
    ('20', '7777b4df-68dd-4600-b4ba-a4ce56ecc6ac', 'Topic 20: Human influences on ecosystems'),
    ('21', '55023dc0-7fdc-46ea-a3e9-9a049306d086', 'Topic 21: Biotechnology and Genetic Engineering'),
]

def audit():
    print(f"\n=========================================================================================")
    print(f"AUDITING IGCSE BIOLOGY (0610) LECTURES: ALL 21 TOPICS")
    print(f"=========================================================================================\n")
    
    passed_count = 0
    total = len(LECTURES)
    
    for code, lid, title in LECTURES:
        manifest_path = os.path.join('public', 'audio', 'lectures', 'biology', code, 'manifest.json')
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
            audio_path = os.path.join('public', 'audio', 'lectures', 'biology', code, f"{s['id']}.mp3")
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
        if f"'{lid}'" not in lv_code or f"biology/{code}/manifest.json" not in lv_code:
            issues.append("LectureViewer.tsx manifest mapping missing")
            
        if issues:
            print(f"❌ [{code}] {title}: {', '.join(issues[:3])}")
        else:
            total_dur = manifest.get('totalDuration', 0)
            print(f"✅ [{code}] {title} | {len(segs)} segments | {total_dur}s | div diff=0 | Wired!")
            passed_count += 1
            
    print(f"\n=========================================================================================")
    print(f"AUDIT SUMMARY: {passed_count}/{total} BIOLOGY TOPICS PASSED ALL CHECKS")
    print(f"=========================================================================================\n")
    return passed_count == total

if __name__ == "__main__":
    audit()
