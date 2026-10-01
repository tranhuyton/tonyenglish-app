import sys
import re

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

themes = {
    '8_1': {
        'border': '#bae6fd',
        'title_color': '#0284c7',
        'badge_bg': '#f0f9ff',
        'badge_color': '#0284c7',
        'badge_border': '#bae6fd',
        'badge_text': 'Nghe phần này'
    },
    '8_2': {
        'border': '#fed7aa',
        'title_color': '#c2410c',
        'badge_bg': '#fff7ed',
        'badge_color': '#ea580c',
        'badge_border': '#fed7aa',
        'badge_text': 'Nghe phần này'
    },
    '8_3': {
        'border': '#a7f3d0',
        'title_color': '#059669',
        'badge_bg': '#ecfdf5',
        'badge_color': '#059669',
        'badge_border': '#a7f3d0',
        'badge_text': 'Nghe phần này'
    }
}

for code in ['8_1', '8_2', '8_3']:
    with open(f'scripts/raw_geo/{code}_p1.html', 'r', encoding='utf-8') as f:
        html = f.read()

    theme = themes[code]
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

    # 2. Specific h3 cards
    if code == '8_1':
        # card-economic-indicators
        pat_81_econ = r'<h3 id="card-economic-indicators" class="lecture-interactive-card" data-lecture-section="economic_indicators"[^>]*>(.*?)</h3>\s*(<ul style="[^"]*">.*?</ul>)\s*(<div style="background:\s*#fff1f2;[^>]*>.*?</div>)'
        def repl_81_econ(m):
            title = m.group(1).strip()
            ul = m.group(2).strip()
            box = m.group(3).strip()
            return f'''<div id="card-economic-indicators" class="lecture-interactive-card" data-lecture-section="economic_indicators" style="margin-top: 24px; margin-bottom: 20px; padding: 20px 22px; background: #ffffff; border: 1.5px solid {theme['border']}; border-radius: 12px; box-shadow: 0 2px 6px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s ease;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px; border-bottom: 1.5px solid {theme['border']}; padding-bottom: 6px;">
            <h3 style="color: {theme['title_color']}; font-size: 18px; font-weight: 700; margin: 0;">{title}</h3>
            <span style="font-size: 11px; font-weight: 700; background: {theme['badge_bg']}; color: {theme['badge_color']}; padding: 2px 7px; border-radius: 4px; border: 1px solid {theme['badge_border']};">{theme['badge_text']}</span>
        </div>
        {ul}
        {box}
    </div>'''
        new_html, count_econ = re.subn(pat_81_econ, repl_81_econ, new_html, flags=re.DOTALL)
        print(f"  Replaced {count_econ} economic-indicators card in 8.1")

        # card-social-indicators
        pat_81_soc = r'<h3 id="card-social-indicators" class="lecture-interactive-card" data-lecture-section="social_indicators"[^>]*>(.*?)</h3>\s*(<p>.*?</p>)\s*(<ul style="[^"]*">.*?</ul>)\s*(<!-- Figure 8\.4[^>]*-->\s*<figure style="[^"]*">.*?</figure>)'
        def repl_81_soc(m):
            title = m.group(1).strip()
            para = m.group(2).strip()
            ul = m.group(3).strip()
            fig = m.group(4).strip()
            return f'''<div id="card-social-indicators" class="lecture-interactive-card" data-lecture-section="social_indicators" style="margin-top: 24px; margin-bottom: 20px; padding: 20px 22px; background: #ffffff; border: 1.5px solid {theme['border']}; border-radius: 12px; box-shadow: 0 2px 6px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s ease;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px; border-bottom: 1.5px solid {theme['border']}; padding-bottom: 6px;">
            <h3 style="color: {theme['title_color']}; font-size: 18px; font-weight: 700; margin: 0;">{title}</h3>
            <span style="font-size: 11px; font-weight: 700; background: {theme['badge_bg']}; color: {theme['badge_color']}; padding: 2px 7px; border-radius: 4px; border: 1px solid {theme['badge_border']};">{theme['badge_text']}</span>
        </div>
        {para}
        {ul}
        {fig}
    </div>'''
        new_html, count_soc = re.subn(pat_81_soc, repl_81_soc, new_html, flags=re.DOTALL)
        print(f"  Replaced {count_soc} social-indicators card in 8.1")

        # card-brandt-failure
        pat_81_bf = r'<h3 id="card-brandt-failure" class="lecture-interactive-card" data-lecture-section="brandt_failure"[^>]*>(.*?)</h3>\s*(<ol style="[^"]*">.*?</ol>)'
        def repl_81_bf(m):
            title = m.group(1).strip()
            ol = m.group(2).strip()
            return f'''<div id="card-brandt-failure" class="lecture-interactive-card" data-lecture-section="brandt_failure" style="margin-top: 24px; margin-bottom: 20px; padding: 20px 22px; background: #ffffff; border: 1.5px solid {theme['border']}; border-radius: 12px; box-shadow: 0 2px 6px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s ease;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px; border-bottom: 1.5px solid {theme['border']}; padding-bottom: 6px;">
            <h3 style="color: {theme['title_color']}; font-size: 18px; font-weight: 700; margin: 0;">{title}</h3>
            <span style="font-size: 11px; font-weight: 700; background: {theme['badge_bg']}; color: {theme['badge_color']}; padding: 2px 7px; border-radius: 4px; border: 1px solid {theme['badge_border']};">{theme['badge_text']}</span>
        </div>
        {ol}
    </div>'''
        new_html, count_bf = re.subn(pat_81_bf, repl_81_bf, new_html, flags=re.DOTALL)
        print(f"  Replaced {count_bf} brandt-failure card in 8.1")

    elif code == '8_2':
        # card-physical-factors
        pat_82_phys = r'<h3 id="card-physical-factors" class="lecture-interactive-card" data-lecture-section="physical_factors"[^>]*>(.*?)</h3>\s*(<ul style="[^"]*">.*?</ul>)\s*(<!-- Figure 8\.11[^>]*-->\s*<div style="display:\s*grid;[^>]*>.*?</div>\s*</div>)'
        def repl_82_phys(m):
            title = m.group(1).strip()
            ul = m.group(2).strip()
            fig = m.group(3).strip()
            return f'''<div id="card-physical-factors" class="lecture-interactive-card" data-lecture-section="physical_factors" style="margin-top: 24px; margin-bottom: 20px; padding: 20px 22px; background: #ffffff; border: 1.5px solid {theme['border']}; border-radius: 12px; box-shadow: 0 2px 6px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s ease;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px; border-bottom: 1.5px solid {theme['border']}; padding-bottom: 6px;">
            <h3 style="color: {theme['title_color']}; font-size: 18px; font-weight: 700; margin: 0;">{title}</h3>
            <span style="font-size: 11px; font-weight: 700; background: {theme['badge_bg']}; color: {theme['badge_color']}; padding: 2px 7px; border-radius: 4px; border: 1px solid {theme['badge_border']};">{theme['badge_text']}</span>
        </div>
        {ul}
        {fig}
    </div>'''
        new_html, count_phys = re.subn(pat_82_phys, repl_82_phys, new_html, flags=re.DOTALL)
        print(f"  Replaced {count_phys} physical-factors card in 8.2")

        # card-historical-factors
        pat_82_hist = r'<h3 id="card-historical-factors" class="lecture-interactive-card" data-lecture-section="historical_factors"[^>]*>(.*?)</h3>\s*(<ul style="[^"]*">.*?</ul>)\s*(<!-- Two column: Figure 8\.12 and Figure 8\.13 -->\s*<div style="display:\s*grid;[^>]*>.*?</div>\s*</div>)'
        def repl_82_hist(m):
            title = m.group(1).strip()
            ul = m.group(2).strip()
            fig = m.group(3).strip()
            return f'''<div id="card-historical-factors" class="lecture-interactive-card" data-lecture-section="historical_factors" style="margin-top: 24px; margin-bottom: 20px; padding: 20px 22px; background: #ffffff; border: 1.5px solid {theme['border']}; border-radius: 12px; box-shadow: 0 2px 6px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s ease;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px; border-bottom: 1.5px solid {theme['border']}; padding-bottom: 6px;">
            <h3 style="color: {theme['title_color']}; font-size: 18px; font-weight: 700; margin: 0;">{title}</h3>
            <span style="font-size: 11px; font-weight: 700; background: {theme['badge_bg']}; color: {theme['badge_color']}; padding: 2px 7px; border-radius: 4px; border: 1px solid {theme['badge_border']};">{theme['badge_text']}</span>
        </div>
        {ul}
        {fig}
    </div>'''
        new_html, count_hist = re.subn(pat_82_hist, repl_82_hist, new_html, flags=re.DOTALL)
        print(f"  Replaced {count_hist} historical-factors card in 8.2")

    elif code == '8_3':
        # card-indonesia-drivers
        pat_83_indo = r'<h3 id="card-indonesia-drivers" class="lecture-interactive-card" data-lecture-section="indonesia_drivers"[^>]*>(.*?)</h3>\s*(<ul style="[^"]*">.*?</ul>)'
        def repl_83_indo(m):
            title = m.group(1).strip()
            ul = m.group(2).strip()
            return f'''<div id="card-indonesia-drivers" class="lecture-interactive-card" data-lecture-section="indonesia_drivers" style="margin-top: 24px; margin-bottom: 20px; padding: 20px 22px; background: #ffffff; border: 1.5px solid {theme['border']}; border-radius: 12px; box-shadow: 0 2px 6px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s ease;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px; border-bottom: 1.5px solid {theme['border']}; padding-bottom: 6px;">
            <h3 style="color: {theme['title_color']}; font-size: 18px; font-weight: 700; margin: 0;">{title}</h3>
            <span style="font-size: 11px; font-weight: 700; background: {theme['badge_bg']}; color: {theme['badge_color']}; padding: 2px 7px; border-radius: 4px; border: 1px solid {theme['badge_border']};">{theme['badge_text']}</span>
        </div>
        {ul}
    </div>'''
        new_html, count_indo = re.subn(pat_83_indo, repl_83_indo, new_html, flags=re.DOTALL)
        print(f"  Replaced {count_indo} indonesia-drivers card in 8.3")

    new_opens = len(new_html.split('<div')) - 1
    new_closes = len(new_html.split('</div>')) - 1
    diff_new = new_opens - new_closes
    print(f"  New div diff = {diff_new}")

    if diff_new != 0:
        raise ValueError(f"Diff not balanced in {code}: {diff_new}")

    with open(f'scripts/raw_geo/{code}_p1_transformed.html', 'w', encoding='utf-8') as f:
        f.write(new_html)

print("\n🎉 Topic 8 complete transformation and verification passed!")
