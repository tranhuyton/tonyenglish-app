import os
import sys
import json
from bs4 import BeautifulSoup

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

lessons = [
    ('3.1', '3_1'), ('3.2', '3_2'), ('3.3', '3_3'), ('3.4', '3_4'),
    ('4.1', '4_1'), ('4.2', '4_2'), ('4.3', '4_3'), ('4.4', '4_4'),
    ('5.1', '5_1'), ('5.2', '5_2'), ('5.3', '5_3')
]

print("=== AUDITING ALL 11 TRANSFORMED LESSONS ===")
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
    for s in m.get('segments', []):
        sel = s.get('selector', '')
        if sel:
            el = soup.select_one(sel)
            if not el:
                missing_sel.append(f"{s['id']} ({sel})")

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

    issue_str = f" -> Issues: {'; '.join(issues)}" if issues else f" -> All {len(m.get('segments', []))} selectors OK, 0 heading cards, diff=0, {len(ms)} majorSections."
    print(f"[{status}] Lesson {name:4} ({code:4}){issue_str}")

print("\n" + "="*70)
if all_pass:
    print("🎉 ALL 11 LESSONS PASS WITH FLYING COLORS!")
else:
    print("❌ SOME LESSONS FAILED AUDIT.")
