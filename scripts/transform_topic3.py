import sys
import re

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# Definitions of themes for Topic 3
configs = {
    '3_1': {
        'default': {
            'border': '#bae6fd',
            'title_color': '#0369a1',
            'badge_bg': '#f0f9ff',
            'badge_color': '#0284c7',
            'badge_text': 'Nghe phần này'
        }
    },
    '3_2': {
        'default': {
            'border': '#bae6fd',
            'title_color': '#0369a1',
            'badge_bg': '#f0f9ff',
            'badge_color': '#0284c7',
            'badge_text': 'Nghe phần này'
        }
    },
    '3_3': {
        'default': {
            'border': '#bbf7d0',
            'title_color': '#15803d',
            'badge_bg': '#f0fdf4',
            'badge_color': '#16a34a',
            'badge_text': 'Nghe phần này'
        }
    },
    '3_4': {
        'default': {
            'border': '#fca5a5',
            'title_color': '#b91c1c',
            'badge_bg': '#fef2f2',
            'badge_color': '#dc2626',
            'badge_text': 'Nghe phần này'
        },
        'sec-management': {
            'border': '#bbf7d0',
            'title_color': '#15803d',
            'badge_bg': '#f0fdf4',
            'badge_color': '#16a34a',
            'badge_text': 'Nghe phần này'
        }
    }
}

for code, cfg in configs.items():
    with open(f'scripts/raw_geo/{code}_p1.html', 'r', encoding='utf-8') as f:
        html = f.read()

    orig_opens = len(html.split('<div')) - 1
    orig_closes = len(html.split('</div>')) - 1
    diff_orig = orig_opens - orig_closes
    print(f"\nProcessing {code}: Initial div diff = {diff_orig}")

    pattern = r'<h2 id="([^"]+)" class="lecture-interactive-card" data-lecture-section="([^"]+)"[^>]*>(.*?)</h2>\s*<p>(.*?)</p>'

    def make_repl(match):
        sec_id = match.group(1)
        dls = match.group(2)
        title = match.group(3)
        para = match.group(4)

        theme = cfg.get(sec_id, cfg['default'])

        repl = f'''<div id="{sec_id}" class="lecture-interactive-card" data-lecture-section="{dls}" style="margin-bottom: 24px; padding: 22px 24px; background: #ffffff; border: 1.5px solid {theme['border']}; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s ease;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px; border-bottom: 2px solid {theme['border']}; padding-bottom: 8px;">
            <h2 style="color: {theme['title_color']}; font-size: 22px; font-weight: 700; margin: 0;">{title}</h2>
            <span style="font-size: 11px; font-weight: 700; background: {theme['badge_bg']}; color: {theme['badge_color']}; padding: 3px 8px; border-radius: 4px; border: 1px solid {theme['border']};">{theme['badge_text']}</span>
        </div>
        <p style="margin: 0; color: #334155; font-size: 15px; line-height: 1.6;">
            {para}
        </p>
    </div>'''
        return repl

    new_html, count = re.subn(pattern, make_repl, html, flags=re.DOTALL)
    print(f"  Replaced {count} h2 sections in {code}")

    new_opens = len(new_html.split('<div')) - 1
    new_closes = len(new_html.split('</div>')) - 1
    diff_new = new_opens - new_closes
    print(f"  New div diff = {diff_new}")

    if diff_new != 0:
        raise ValueError(f"Diff not balanced in {code}: {diff_new}")

    with open(f'scripts/raw_geo/{code}_p1_transformed.html', 'w', encoding='utf-8') as f:
        f.write(new_html)

print("\n🎉 Topic 3 transformation complete and verified!")
