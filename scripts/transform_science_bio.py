import re
import sys
import os
from bs4 import BeautifulSoup

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

theme = {
    'border': '#a7f3d0',       # emerald-200
    'badge_bg': '#ecfdf5',     # emerald-50
    'badge_color': '#059669',  # emerald-600
}

# Group 2 pattern
pat_g2 = r'<div(?:\s+style="(?:margin-bottom:\s*35px;|)")?>\s*' \
         r'<div style="display:\s*flex;\s*align-items:\s*center;\s*gap:\s*10px;\s*margin-bottom:\s*15px;">\s*' \
         r'(<span style="[^"]*">.*?</span>\s*)?' \
         r'<h2 (?=[^>]*\bid="([^"]+)")(?=[^>]*\bdata-lecture-section="([^"]+)")[^>]*>(.*?)</h2>\s*' \
         r'</div>'

def repl_g2(m):
    span = m.group(1) or ''
    hid = m.group(2)
    dls = m.group(3)
    title = BeautifulSoup(m.group(4), 'html.parser').get_text().strip()

    span_part = f'{span.strip()}' if span.strip() else ''
    gap_part = f'<div style="display: flex; align-items: center; gap: 10px;">{span_part}<h2 style="color: #0f172a; margin: 0; font-size: 22px; font-weight: 700;">{title}</h2></div>'

    return f'''<div id="{hid}" class="lecture-interactive-card" data-lecture-section="{dls}" style="background: #ffffff; border: 1.5px solid {theme['border']}; border-radius: 14px; padding: 24px 28px; margin-bottom: 32px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); cursor: pointer; transition: all 0.2s ease;">
    <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 18px; border-bottom: 2px solid {theme['border']}; padding-bottom: 8px;">
        {gap_part}
        <span style="font-size: 11px; font-weight: 700; background: {theme['badge_bg']}; color: {theme['badge_color']}; padding: 3px 8px; border-radius: 4px; border: 1px solid {theme['border']};">Nghe phần này</span>
    </div>'''

# Group 1 pattern
pat_g1 = r'<div style="margin-bottom:\s*(?:45px|50px);">\s*' \
         r'<h2 (?=[^>]*\bid="([^"]+)")(?=[^>]*\bdata-lecture-section="([^"]+)")[^>]*>(.*?)</h2>'

def repl_g1(m):
    hid = m.group(1)
    dls = m.group(2)
    title = BeautifulSoup(m.group(3), 'html.parser').get_text().strip()

    return f'''<div id="{hid}" class="lecture-interactive-card" data-lecture-section="{dls}" style="background: #ffffff; border: 1.5px solid {theme['border']}; border-radius: 14px; padding: 24px 28px; margin-bottom: 32px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); cursor: pointer; transition: all 0.2s ease;">
    <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 18px; border-bottom: 2px solid {theme['border']}; padding-bottom: 8px;">
        <h2 style="color: #0f172a; margin: 0; font-size: 22px; font-weight: 700;">{title}</h2>
        <span style="font-size: 11px; font-weight: 700; background: {theme['badge_bg']}; color: {theme['badge_color']}; padding: 3px 8px; border-radius: 4px; border: 1px solid {theme['border']};">Nghe phần này</span>
    </div>'''

group2_lessons = ['b1', 'b2', 'b3', 'b5', 'b6', 'b7', 'b9', 'b10']
group1_lessons = ['b4', 'b8', 'b11', 'b12', 'b13', 'b14', 'b15', 'b16', 'b17', 'b18', 'b19']

print("=== TRANSFORMING ALL 19 SCIENCE BIOLOGY LESSONS ===")
all_pass = True

for i in range(1, 20):
    code = f"b{i}"
    hpath = f"scripts/raw_science_bio/{code}_p1.html"
    with open(hpath, 'r', encoding='utf-8') as f:
        html = f.read()

    orig_opens = len(html.split('<div')) - 1
    orig_closes = len(html.split('</div>')) - 1
    diff_orig = orig_opens - orig_closes

    if code in group2_lessons:
        new_html, count = re.subn(pat_g2, repl_g2, html, flags=re.DOTALL)
        grp = "G2"
    else:
        new_html, count = re.subn(pat_g1, repl_g1, html, flags=re.DOTALL)
        grp = "G1"

    new_opens = len(new_html.split('<div')) - 1
    new_closes = len(new_html.split('</div>')) - 1
    diff_new = new_opens - new_closes

    soup = BeautifulSoup(new_html, 'html.parser')
    h_cards = soup.find_all(['h1', 'h2', 'h3', 'h4'], class_='lecture-interactive-card')

    status = "✅ PASS"
    issues = []
    if diff_new != 0:
        issues.append(f"diff={diff_new}")
        status = "❌ FAIL"
        all_pass = False
    if len(h_cards) > 0:
        issues.append(f"{len(h_cards)} heading cards remain ({[h.get('id') for h in h_cards]})")
        status = "❌ FAIL"
        all_pass = False

    out_file = f"scripts/raw_science_bio/{code}_p1_transformed.html"
    with open(out_file, 'w', encoding='utf-8') as f:
        f.write(new_html)

    issue_str = f" -> Issues: {'; '.join(issues)}" if issues else f" -> {count} sections transformed, diff=0, 0 heading cards"
    print(f"[{status}] Lesson {code.upper():4} ({grp}):{issue_str}")

print("\n" + "="*70)
if all_pass:
    print("🎉 ALL 19 LESSONS SUCCESSFULLY TRANSFORMED AND BALANCED!")
else:
    print("❌ SOME LESSONS FAILED TRANSFORMATION.")
