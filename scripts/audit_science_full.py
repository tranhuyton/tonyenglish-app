import os
import sys
import re
import json
from bs4 import BeautifulSoup
from supabase import create_client

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

with open(os.path.join(os.path.dirname(__file__), '..', '.env'), 'r', encoding='utf-8') as f:
    env = f.read()

URL = re.search(r'^VITE_SUPABASE_URL=(.*)$', env, re.M).group(1).strip()
KEY = re.search(r'^VITE_SUPABASE_ANON_KEY=(.*)$', env, re.M).group(1).strip()
sb = create_client(URL, KEY)

with open(os.path.join(os.path.dirname(__file__), '..', 'src', 'LectureViewer.tsx'), 'r', encoding='utf-8') as f:
    lv_code = f.read()

with open(os.path.join(os.path.dirname(__file__), 'science_0654_catalog.json'), 'r', encoding='utf-8') as f:
    catalog = json.load(f)

def audit():
    print(f"\n=========================================================================================")
    print(f"AUDITING CAMBRIDGE IGCSE CO-ORDINATED SCIENCES (0654): ALL 37 LECTURES")
    print(f"=========================================================================================\n")
    
    passed_count = 0
    total = len(catalog)
    
    for item in catalog:
        code = item['code']
        lid = item['lid']
        title = item['title']
        manifest_path = os.path.join(os.path.dirname(__file__), '..', 'public', 'audio', 'lectures', 'science', code, 'manifest.json')
        issues = []
        
        # 1. Manifest
        if not os.path.exists(manifest_path):
            issues.append("Manifest missing")
            print(f"⏳ [{code:4}] {title}: Manifest missing (Not generated yet)")
            continue
            
        try:
            with open(manifest_path, 'r', encoding='utf-8') as f:
                manifest = json.load(f)
        except Exception as e:
            issues.append(f"Invalid JSON: {e}")
            print(f"❌ [{code:4}] {title}: Invalid JSON in manifest")
            continue
            
        segs = manifest.get('segments', [])
        if not segs:
            issues.append("0 segments in manifest")
            
        # 2. Audio files
        for s in segs:
            audio_path = os.path.join(os.path.dirname(__file__), '..', 'public', 'audio', 'lectures', 'science', code, f"{s['id']}.mp3")
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
        if f"'{lid}'" not in lv_code or f"science/{code}/manifest.json" not in lv_code:
            issues.append("Not wired in LectureViewer.tsx LECTURE_MANIFEST_MAP")
            
        if not issues:
            passed_count += 1
            dur = manifest.get('totalDuration', 0)
            print(f"✅ [{code:4}] {title} | {len(segs)} segments | {dur}s | div diff=0 | Wired!")
        else:
            print(f"❌ [{code:4}] {title}: {', '.join(issues)}")
            
    print(f"\n=========================================================================================")
    print(f"AUDIT SUMMARY: {passed_count}/{total} CO-ORDINATED SCIENCE LECTURES PASSED ALL CHECKS")
    print(f"=========================================================================================\n")
    return passed_count == total

if __name__ == "__main__":
    audit()
