import sys
import re

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

theme = {
    'border': '#99f6e4',
    'title_color': '#0f766e',
    'badge_bg': '#f0fdfa',
    'badge_color': '#0f766e',
    'badge_border': '#99f6e4',
    'badge_text': 'Nghe phần này'
}

for code in ['7_1', '7_2', '7_3']:
    with open(f'scripts/raw_geo/{code}_p1.html', 'r', encoding='utf-8') as f:
        html = f.read()

    orig_opens = len(html.split('<div')) - 1
    orig_closes = len(html.split('</div>')) - 1
    diff_orig = orig_opens - orig_closes
    print(f"\nProcessing {code}: Initial div diff = {diff_orig}")

    # 1. Replace major section h2 tags
    pattern_h2 = r'<h2 id="([^"]+)" class="lecture-interactive-card" data-lecture-section="([^"]+)"[^>]*>(.*?)</h2>\s*<p>(.*?)</p>'

    def make_repl_h2(m):
        sec_id = m.group(1)
        dls = m.group(2)
        title = m.group(3).strip()
        para = m.group(4).strip()

        return f'''<div id="{sec_id}" class="lecture-interactive-card" data-lecture-section="{dls}" style="margin-bottom: 24px; padding: 22px 24px; background: #ffffff; border: 1.5px solid {theme['border']}; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s ease;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px; border-bottom: 2px solid {theme['border']}; padding-bottom: 8px;">
            <h2 style="color: {theme['title_color']}; font-size: 22px; font-weight: 700; margin: 0;">{title}</h2>
            <span style="font-size: 11px; font-weight: 700; background: {theme['badge_bg']}; color: {theme['badge_color']}; padding: 3px 8px; border-radius: 4px; border: 1px solid {theme['badge_border']};">{theme['badge_text']}</span>
        </div>
        <p style="margin: 0; color: #334155; font-size: 15px; line-height: 1.6;">
            {para}
        </p>
    </div>'''

    new_html, count_h2 = re.subn(pattern_h2, make_repl_h2, html, flags=re.DOTALL)
    print(f"  Replaced {count_h2} h2 sections in {code}")

    # 2. Specific h3 cards for 7.2
    if code == '7_2':
        # rural-urban-fringe
        pat_ruf = r'<h3 id="sec-rural-urban-fringe" class="lecture-interactive-card" data-lecture-section="rural_urban_fringe"[^>]*>(.*?)</h3>\s*(<p>.*?</p>)\s*(<div style="display:grid; grid-template-columns:repeat\(auto-fit, minmax\(320px, 1fr\)\); gap:18px; margin:20px 0;">.*?</div>\s*</div>\s*</div>)'
        def repl_ruf(m):
            title = m.group(1).strip()
            para = m.group(2).strip()
            grid = m.group(3).strip()
            return f'''<div id="sec-rural-urban-fringe" class="lecture-interactive-card" data-lecture-section="rural_urban_fringe" style="margin-top: 24px; margin-bottom: 20px; padding: 20px 22px; background: #ffffff; border: 1.5px solid {theme['border']}; border-radius: 12px; box-shadow: 0 2px 6px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s ease;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px; border-bottom: 1.5px solid {theme['border']}; padding-bottom: 6px;">
            <h3 style="color: {theme['title_color']}; font-size: 18px; font-weight: 700; margin: 0;">{title}</h3>
            <span style="font-size: 11px; font-weight: 700; background: {theme['badge_bg']}; color: {theme['badge_color']}; padding: 2px 7px; border-radius: 4px; border: 1px solid {theme['badge_border']};">{theme['badge_text']}</span>
        </div>
        {para}
        {grid}
    </div>'''
        new_html, count_ruf = re.subn(pat_ruf, repl_ruf, new_html, flags=re.DOTALL)
        print(f"  Replaced {count_ruf} rural-urban-fringe card in 7.2")

        # gentrification
        pat_gent = r'<h3 id="sec-gentrification" class="lecture-interactive-card" data-lecture-section="gentrification"[^>]*>(.*?)</h3>\s*(<p>.*?</p>)\s*(<!-- FIGURES 7\.8, 7\.9, 7\.10 -->\s*<div style="display:grid; grid-template-columns:repeat\(auto-fit, minmax\(280px, 1fr\)\); gap:16px; margin:20px 0;">.*?</div>)'
        def repl_gent(m):
            title = m.group(1).strip()
            para = m.group(2).strip()
            grid = m.group(3).strip()
            return f'''<div id="sec-gentrification" class="lecture-interactive-card" data-lecture-section="gentrification" style="margin-top: 24px; margin-bottom: 20px; padding: 20px 22px; background: #ffffff; border: 1.5px solid {theme['border']}; border-radius: 12px; box-shadow: 0 2px 6px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s ease;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px; border-bottom: 1.5px solid {theme['border']}; padding-bottom: 6px;">
            <h3 style="color: {theme['title_color']}; font-size: 18px; font-weight: 700; margin: 0;">{title}</h3>
            <span style="font-size: 11px; font-weight: 700; background: {theme['badge_bg']}; color: {theme['badge_color']}; padding: 2px 7px; border-radius: 4px; border: 1px solid {theme['badge_border']};">{theme['badge_text']}</span>
        </div>
        {para}
        {grid}
    </div>'''
        new_html, count_gent = re.subn(pat_gent, repl_gent, new_html, flags=re.DOTALL)
        print(f"  Replaced {count_gent} gentrification card in 7.2")

    new_opens = len(new_html.split('<div')) - 1
    new_closes = len(new_html.split('</div>')) - 1
    diff_new = new_opens - new_closes
    print(f"  New div diff = {diff_new}")

    if diff_new != 0:
        raise ValueError(f"Diff not balanced in {code}: {diff_new}")

    with open(f'scripts/raw_geo/{code}_p1_transformed.html', 'w', encoding='utf-8') as f:
        f.write(new_html)

print("\n🎉 Topic 7 complete transformation and verification passed!")
