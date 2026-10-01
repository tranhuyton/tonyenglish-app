import os
import sys
import json
from bs4 import BeautifulSoup

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

lessons = [
    ('9.1', '9_1'), ('9.2', '9_2'), ('9.3', '9_3'),
    ('10.1', '10_1'), ('10.2', '10_2'), ('10.3', '10_3'),
    ('10.4', '10_4'), ('10.5', '10_5'), ('10.6', '10_6')
]

print("=== AUDITING LESSONS 9.1 TO 10.6 ===")
all_pass = True

for name, code in lessons:
    mpath = f"public/audio/lectures/geography/{code}/manifest.json"
    hpath = f"scripts/raw_geo/{code}_p1_transformed.html"

    if not os.path.exists(hpath):
        print(f"[⏳ PENDING] Lesson {name:4} ({code:4}) -> Transformed file not created yet.")
        all_pass = False
        continue

    with open(mpath, 'r', encoding='utf-8') as f:
        m = json.load(f)
    with open(hpath, 'r', encoding='utf-8') as f:
        html = f.read()

    soup = BeautifulSoup(html, 'html.parser')

    # 1. Div balance
    opens = len(html.split('<div')) - 1
    closes = len(html.split('</div>')) - 1
    diff = opens - closes

    # 2. Check bare heading interactive cards
    h_cards = soup.find_all(['h1', 'h2', 'h3', 'h4'], class_='lecture-interactive-card')

    # 3. Check missing selectors from manifest
    missing_sel = []
    missing_audio = []
    for s in m.get('segments', []):
        sel = s.get('selector', '')
        if sel:
            el = soup.select_one(sel)
            if not el:
                missing_sel.append(f"{s['id']} ({sel})")
        
        rel = s.get('audioUrl', '').lstrip('/')
        if not os.path.exists(os.path.join('public', rel)):
            missing_audio.append(s['id'])

    # 4. Check majorSections
    ms = m.get('majorSections', {})
    is_ms_dict = isinstance(ms, dict)

    status = "✅ PASS"
    issues = []
    if diff != 0:
        issues.append(f"div diff={diff}")
        status = "❌ FAIL"
        all_pass = False
    if len(h_cards) > 0:
        issues.append(f"{len(h_cards)} heading cards remain ({[h.get('id') for h in h_cards]})")
        status = "❌ FAIL"
        all_pass = False
    if missing_sel:
        issues.append(f"Missing selectors: {', '.join(missing_sel)}")
        status = "❌ FAIL"
        all_pass = False
    if not is_ms_dict:
        issues.append(f"majorSections is {type(ms)}")
        status = "❌ FAIL"
        all_pass = False
    if missing_audio:
        issues.append(f"{len(missing_audio)} missing audio files")
        status = "❌ FAIL"
        all_pass = False

    issue_str = f" -> Issues: {'; '.join(issues)}" if issues else f" -> All {len(m.get('segments', []))} selectors OK, 0 heading cards, diff=0, {len(ms)} majorSections, audio {len(m.get('segments', []))}/{len(m.get('segments', []))} OK."
    print(f"[{status}] Lesson {name:4} ({code:4}){issue_str}")

print("\n" + "="*70)
if all_pass:
    print("🎉 ALL LESSONS PASS WITH FLYING COLORS!")
else:
    print("ℹ️ Note: Pending lessons are normal if Topic 9 is not transformed yet.")
