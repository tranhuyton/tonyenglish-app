import sys
import re

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

theme = {
    'border': '#ddd6fe',
    'title_color': '#4c1d95',
    'badge_bg': '#f5f3ff',
    'badge_color': '#6d28d9',
    'badge_border': '#ddd6fe',
    'badge_text': 'Nghe phần này'
}

for code in ['6_1', '6_2', '6_3']:
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

    # 2. Specific h3 cards for 6.1 and 6.2
    if code == '6_1':
        pat_61_h3 = r'<h3 id="card-mortality-transition" class="lecture-interactive-card" data-lecture-section="mortality_transition"[^>]*>(.*?)</h3>\s*(<p>.*?</p>)\s*(<ul>.*?</ul>)'
        def repl_61_h3(m):
            title = m.group(1).strip()
            para = m.group(2).strip()
            ul = m.group(3).strip()
            return f'''<div id="card-mortality-transition" class="lecture-interactive-card" data-lecture-section="mortality_transition" style="margin-top: 24px; margin-bottom: 20px; padding: 20px 22px; background: #ffffff; border: 1.5px solid #ddd6fe; border-radius: 12px; box-shadow: 0 2px 6px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s ease;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px; border-bottom: 1.5px solid #ddd6fe; padding-bottom: 6px;">
            <h3 style="color: #6d28d9; font-size: 18px; font-weight: 700; margin: 0;">{title}</h3>
            <span style="font-size: 11px; font-weight: 700; background: #f5f3ff; color: #6d28d9; padding: 2px 7px; border-radius: 4px; border: 1px solid #ddd6fe;">Nghe phần này</span>
        </div>
        {para}
        {ul}
    </div>'''
        new_html, count_h3 = re.subn(pat_61_h3, repl_61_h3, new_html, flags=re.DOTALL)
        print(f"  Replaced {count_h3} h3 card in 6.1")

    elif code == '6_2':
        pat_62_h3 = r'<h3 id="card-pyramid-anomalies" class="lecture-interactive-card" data-lecture-section="pyramid_anomalies"[^>]*>(.*?)</h3>\s*(<p>.*?</p>)\s*(<ul>.*?</ul>)'
        def repl_62_h3(m):
            title = m.group(1).strip()
            para = m.group(2).strip()
            ul = m.group(3).strip()
            return f'''<div id="card-pyramid-anomalies" class="lecture-interactive-card" data-lecture-section="pyramid_anomalies" style="margin-top: 24px; margin-bottom: 20px; padding: 20px 22px; background: #ffffff; border: 1.5px solid #ddd6fe; border-radius: 12px; box-shadow: 0 2px 6px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s ease;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px; border-bottom: 1.5px solid #ddd6fe; padding-bottom: 6px;">
            <h3 style="color: #6d28d9; font-size: 18px; font-weight: 700; margin: 0;">{title}</h3>
            <span style="font-size: 11px; font-weight: 700; background: #f5f3ff; color: #6d28d9; padding: 2px 7px; border-radius: 4px; border: 1px solid #ddd6fe;">Nghe phần này</span>
        </div>
        {para}
        {ul}
    </div>'''
        new_html, count_h3 = re.subn(pat_62_h3, repl_62_h3, new_html, flags=re.DOTALL)
        print(f"  Replaced {count_h3} h3 card in 6.2")

    new_opens = len(new_html.split('<div')) - 1
    new_closes = len(new_html.split('</div>')) - 1
    diff_new = new_opens - new_closes
    print(f"  New div diff = {diff_new}")

    if diff_new != 0:
        raise ValueError(f"Diff not balanced in {code}: {diff_new}")

    with open(f'scripts/raw_geo/{code}_p1_transformed.html', 'w', encoding='utf-8') as f:
        f.write(new_html)

print("\n🎉 Topic 6 complete transformation and verification passed!")
