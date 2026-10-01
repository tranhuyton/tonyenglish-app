import sys
import re

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

themes = {
    '9_1': {
        'border': '#bfdbfe',
        'title_color': '#1e40af',
        'badge_bg': '#eff6ff',
        'badge_color': '#1d4ed8',
        'badge_border': '#bfdbfe',
        'badge_text': 'Nghe phần này'
    },
    '9_2': {
        'border': '#ddd6fe',
        'title_color': '#5b21b6',
        'badge_bg': '#f5f3ff',
        'badge_color': '#6d28d9',
        'badge_border': '#ddd6fe',
        'badge_text': 'Nghe phần này'
    },
    '9_3': {
        'border': '#a7f3d0',
        'title_color': '#065f46',
        'badge_bg': '#ecfdf5',
        'badge_color': '#059669',
        'badge_border': '#a7f3d0',
        'badge_text': 'Nghe phần này'
    }
}

for code in ['9_1', '9_2', '9_3']:
    with open(f'scripts/raw_geo/{code}_p1.html', 'r', encoding='utf-8') as f:
        html = f.read()

    theme = themes[code]
    orig_opens = len(html.split('<div')) - 1
    orig_closes = len(html.split('</div>')) - 1
    diff_orig = orig_opens - orig_closes
    print(f"\nProcessing {code}: Initial div diff = {diff_orig}")

    # Safe h2 + p pattern: (?:(?!<h2).)*? inside h2, so it cannot cross any h2 boundary!
    safe_pattern_h2 = r'<h2 id="([^"]+)" class="lecture-interactive-card" data-lecture-section="([^"]+)"[^>]*>((?:(?!<h2).)*?)</h2>\s*<p>(.*?)</p>'

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

    new_html, count_h2 = re.subn(safe_pattern_h2, make_repl_h2, html, flags=re.DOTALL)
    print(f"  Replaced {count_h2} standard h2 sections in {code}")

    if code == '9_2':
        # sec-tnc-impacts
        pat_92_impacts = r'<h2 id="sec-tnc-impacts" class="lecture-interactive-card" data-lecture-section="sec_tnc_impacts"[^>]*>(.*?)</h2>'
        repl_92_impacts = f'''<div id="sec-tnc-impacts" class="lecture-interactive-card" data-lecture-section="sec_tnc_impacts" style="margin-bottom: 24px; padding: 22px 24px; background: #ffffff; border: 1.5px solid {theme['border']}; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s ease;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px; border-bottom: 2px solid {theme['border']}; padding-bottom: 8px;">
            <h2 style="color: {theme['title_color']}; font-size: 22px; font-weight: 700; margin: 0;">4. Impacts of TNCs</h2>
            <span style="font-size: 11px; font-weight: 700; background: {theme['badge_bg']}; color: {theme['badge_color']}; padding: 3px 8px; border-radius: 4px; border: 1px solid {theme['badge_border']};">{theme['badge_text']}</span>
        </div>
        <p style="margin: 0; color: #334155; font-size: 15px; line-height: 1.6;">
            Transnational corporations bring substantial foreign direct investment and employment to host nations, but also create significant socio-economic challenges, leakages, and environmental impacts.
        </p>
    </div>'''
        new_html, count_92 = re.subn(pat_92_impacts, repl_92_impacts, new_html, flags=re.DOTALL)
        print(f"  Replaced {count_92} sec-tnc-impacts in 9.2")

    elif code == '9_3':
        # sec-types-tourism
        pat_93_types = r'<h2 id="sec-types-tourism" class="lecture-interactive-card" data-lecture-section="sec_types_tourism"[^>]*>(.*?)</h2>\s*(<ul>.*?</ul>)'
        def repl_93_types(m):
            title = m.group(1).strip()
            ul = m.group(2).strip()
            return f'''<div id="sec-types-tourism" class="lecture-interactive-card" data-lecture-section="sec_types_tourism" style="margin-bottom: 24px; padding: 22px 24px; background: #ffffff; border: 1.5px solid {theme['border']}; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s ease;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px; border-bottom: 2px solid {theme['border']}; padding-bottom: 8px;">
            <h2 style="color: {theme['title_color']}; font-size: 22px; font-weight: 700; margin: 0;">{title}</h2>
            <span style="font-size: 11px; font-weight: 700; background: {theme['badge_bg']}; color: {theme['badge_color']}; padding: 3px 8px; border-radius: 4px; border: 1px solid {theme['badge_border']};">{theme['badge_text']}</span>
        </div>
        {ul}
    </div>'''
        new_html, count_types = re.subn(pat_93_types, repl_93_types, new_html, flags=re.DOTALL)
        print(f"  Replaced {count_types} sec-types-tourism in 9.3")

        # sec-impacts-tourism
        pat_93_impacts = r'<h2 id="sec-impacts-tourism" class="lecture-interactive-card" data-lecture-section="sec_impacts_tourism"[^>]*>(.*?)</h2>'
        repl_93_impacts = f'''<div id="sec-impacts-tourism" class="lecture-interactive-card" data-lecture-section="sec_impacts_tourism" style="margin-bottom: 24px; padding: 22px 24px; background: #ffffff; border: 1.5px solid {theme['border']}; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s ease;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px; border-bottom: 2px solid {theme['border']}; padding-bottom: 8px;">
            <h2 style="color: {theme['title_color']}; font-size: 22px; font-weight: 700; margin: 0;">4. Impacts of Tourism (EVE framework)</h2>
            <span style="font-size: 11px; font-weight: 700; background: {theme['badge_bg']}; color: {theme['badge_color']}; padding: 3px 8px; border-radius: 4px; border: 1px solid {theme['badge_border']};">{theme['badge_text']}</span>
        </div>
        <p style="margin: 0; color: #334155; font-size: 15px; line-height: 1.6;">
            The impacts of tourism can be categorized using the EVE framework: Economic, Value (Socio-cultural), and Environmental dimensions, each having both positive multiplier benefits and negative externalities.
        </p>
    </div>'''
        new_html, count_imp = re.subn(pat_93_impacts, repl_93_impacts, new_html, flags=re.DOTALL)
        print(f"  Replaced {count_imp} sec-impacts-tourism in 9.3")

    new_opens = len(new_html.split('<div')) - 1
    new_closes = len(new_html.split('</div>')) - 1
    diff_new = new_opens - new_closes
    print(f"  New div diff = {diff_new}")

    if diff_new != 0:
        raise ValueError(f"Diff not balanced in {code}: {diff_new}")

    with open(f'scripts/raw_geo/{code}_p1_transformed.html', 'w', encoding='utf-8') as f:
        f.write(new_html)

print("\n🎉 Topic 9 (9.1 to 9.3) complete transformation passed!")
