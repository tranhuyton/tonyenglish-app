import sys
import re

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

themes = {
    '10_1': {
        'border': '#bbf7d0',
        'badge_bg': '#f0fdf4',
        'badge_color': '#15803d'
    },
    '10_2': {
        'border': '#bae6fd',
        'badge_bg': '#f0f9ff',
        'badge_color': '#0284c7'
    },
    '10_3': {
        'border': '#fecaca',
        'badge_bg': '#fef2f2',
        'badge_color': '#dc2626'
    },
    '10_4': {
        'border': '#fed7aa',
        'badge_bg': '#fff7ed',
        'badge_color': '#b45309'
    },
    '10_5': {
        'border': '#bae6fd',
        'badge_bg': '#f0f9ff',
        'badge_color': '#0369a1'
    },
    '10_6': {
        'border': '#99f6e4',
        'badge_bg': '#f0fdfa',
        'badge_color': '#0f766e'
    }
}

pat_gp = r'<div style="background:\s*#ffffff;\s*border:\s*1px solid #e2e8f0;\s*border-radius:\s*14px;\s*padding:\s*26px 30px;\s*margin-bottom:\s*32px;\s*box-shadow:\s*0 4px 6px -1px rgba\(0,0,0,0\.04\);">' \
         r'\s*<div style="display:\s*flex;\s*align-items:\s*center;\s*gap:\s*12px;\s*margin-bottom:\s*(18px|14px);">' \
         r'\s*(<div style="[^"]*">.*?</div>)' \
         r'\s*<h2 (?=[^>]*\bid="([^"]+)")(?=[^>]*\bdata-lecture-section="([^"]+)")[^>]*>(.*?)</h2>' \
         r'\s*</div>'

for code in ['10_1', '10_2', '10_3', '10_4', '10_5', '10_6']:
    with open(f'scripts/raw_geo/{code}_p1.html', 'r', encoding='utf-8') as f:
        html = f.read()

    theme = themes[code]
    orig_opens = len(html.split('<div')) - 1
    orig_closes = len(html.split('</div>')) - 1
    diff_orig = orig_opens - orig_closes
    print(f"\nProcessing {code}: Initial div diff = {diff_orig}")

    def make_repl_gp(m):
        mb = m.group(1)
        num_div = m.group(2)
        hid = m.group(3)
        dls = m.group(4)
        title = m.group(5).strip()

        return f'''<div id="{hid}" class="lecture-interactive-card" data-lecture-section="{dls}" style="background: #ffffff; border: 1.5px solid {theme['border']}; border-radius: 14px; padding: 26px 30px; margin-bottom: 32px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.04); cursor: pointer; transition: all 0.2s ease;">
    <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 18px; border-bottom: 2px solid {theme['border']}; padding-bottom: 8px;">
        <div style="display: flex; align-items: center; gap: 12px;">
            {num_div}
            <h2 style="color: #0f172a; margin: 0; font-size: 22px; font-weight: 700;">{title}</h2>
        </div>
        <span style="font-size: 11px; font-weight: 700; background: {theme['badge_bg']}; color: {theme['badge_color']}; padding: 3px 8px; border-radius: 4px; border: 1px solid {theme['border']};">Nghe cả phần</span>
    </div>'''

    new_html, count_gp = re.subn(pat_gp, make_repl_gp, html, flags=re.DOTALL)
    print(f"  Replaced {count_gp} grandparent sections in {code}")

    if code == '10_3':
        # card-malthus-boserup
        pat_103_mb = r'<h3 id="card-malthus-boserup" class="lecture-interactive-card" data-lecture-section="malthus_boserup"[^>]*>(.*?)</h3>\s*(<div style="display:\s*grid;\s*grid-template-columns:\s*1fr 1fr;\s*gap:\s*16px;">.*?</div>\s*</div>)'
        def repl_103_mb(m):
            title = m.group(1).strip()
            grid = m.group(2).strip()
            return f'''<div id="card-malthus-boserup" class="lecture-interactive-card" data-lecture-section="malthus_boserup" style="margin-top: 24px; margin-bottom: 20px; padding: 20px 22px; background: #ffffff; border: 1.5px solid #fecdd3; border-radius: 12px; box-shadow: 0 2px 6px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s ease;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 14px; border-bottom: 1.5px solid #fecdd3; padding-bottom: 6px;">
            <h3 style="color: #be123c; font-size: 18px; font-weight: 700; margin: 0;">{title}</h3>
            <span style="font-size: 11px; font-weight: 700; background: #fef2f2; color: #dc2626; padding: 2px 7px; border-radius: 4px; border: 1px solid #fecdd3;">Nghe phần này</span>
        </div>
        {grid}
    </div>'''
        new_html, count_mb = re.subn(pat_103_mb, repl_103_mb, new_html, flags=re.DOTALL)
        print(f"  Replaced {count_mb} malthus-boserup card in 10.3")

    new_opens = len(new_html.split('<div')) - 1
    new_closes = len(new_html.split('</div>')) - 1
    diff_new = new_opens - new_closes
    print(f"  New div diff = {diff_new}")

    if diff_new != 0:
        raise ValueError(f"Diff not balanced in {code}: {diff_new}")

    with open(f'scripts/raw_geo/{code}_p1_transformed.html', 'w', encoding='utf-8') as f:
        f.write(new_html)

print("\n🎉 Topic 10 (10.1 to 10.6) complete transformation passed!")
