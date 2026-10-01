import os
import sys
import json
from bs4 import BeautifulSoup

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

lessons = [
    ('6.1', '6_1'), ('6.2', '6_2'), ('6.3', '6_3'),
    ('7.1', '7_1'), ('7.2', '7_2'), ('7.3', '7_3'),
    ('8.1', '8_1'), ('8.2', '8_2'), ('8.3', '8_3')
]

print("=== AUDITING ALL 9 TRANSFORMED LESSONS (6.1 TO 8.3) ===")
all_pass = True

for name, code in lessons:
    mpath = f"public/audio/lectures/geography/{code}/manifest.json"
    hpath = f"scripts/raw_geo/{code}_p1_transformed.html"

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
    print("🎉 ALL 9 LESSONS (6.1 TO 8.3) PASS WITH FLYING COLORS!")
else:
    print("❌ SOME LESSONS FAILED AUDIT.")
