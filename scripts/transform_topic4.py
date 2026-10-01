import sys
import re

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

for code in ['4_1', '4_2', '4_3', '4_4']:
    with open(f'scripts/raw_geo/{code}_p1.html', 'r', encoding='utf-8') as f:
        html = f.read()

    orig_opens = len(html.split('<div')) - 1
    orig_closes = len(html.split('</div>')) - 1
    diff_orig = orig_opens - orig_closes
    print(f"\nProcessing {code}: Initial div diff = {diff_orig}")

    # 1. Update outer div style for the 4 major sections
    old_div_style = 'style="cursor:pointer; border-radius:12px; padding:12px; margin-top:28px; transition:all 0.2s ease;"'
    new_div_style = 'style="cursor:pointer; background:#ffffff; border:1.5px solid #fed7aa; border-radius:14px; padding:22px 24px; margin-top:28px; margin-bottom:24px; box-shadow:0 2px 8px rgba(0,0,0,0.02); transition:all 0.2s ease;"'
    
    html_mod, div_count = re.subn(re.escape(old_div_style), new_div_style, html)
    print(f"  Updated {div_count} section outer div styles in {code}")

    # 2. Update h2 inside major sections
    h2_pattern = r'<h2 style="color:#b91c1c; font-size:22px; font-weight:bold; border-bottom:2px solid #fecaca; padding-bottom:8px; margin-bottom:18px;">\s*(.*?)\s*</h2>'
    def replace_h2(m):
        title = m.group(1).strip()
        return f'''<div style="display: flex; align-items: center; justify-content: space-between; border-bottom: 2px solid #fecaca; padding-bottom: 8px; margin-bottom: 18px;">
        <h2 style="color:#b91c1c; font-size:22px; font-weight:bold; margin: 0;">{title}</h2>
        <span style="font-size: 11px; font-weight: 700; background: #fff7ed; color: #ea580c; padding: 3px 8px; border-radius: 4px; border: 1px solid #fed7aa;">Nghe cả phần</span>
    </div>'''

    html_mod, h2_count = re.subn(h2_pattern, replace_h2, html_mod, flags=re.DOTALL)
    print(f"  Updated {h2_count} h2 headings in {code}")

    new_opens = len(html_mod.split('<div')) - 1
    new_closes = len(html_mod.split('</div>')) - 1
    diff_new = new_opens - new_closes
    print(f"  New div diff = {diff_new}")

    if diff_new != 0:
        raise ValueError(f"Diff not balanced in {code}: {diff_new}")

    with open(f'scripts/raw_geo/{code}_p1_transformed.html', 'w', encoding='utf-8') as f:
        f.write(html_mod)

print("\n🎉 Topic 4 transformation complete and verified!")
