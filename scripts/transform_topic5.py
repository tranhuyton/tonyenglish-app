import sys
import re

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# ==============================================================================
# 1. TRANSFORM 5.1
# ==============================================================================
with open('scripts/raw_geo/5_1_p1.html', 'r', encoding='utf-8') as f:
    h51 = f.read()

diff_51_orig = len(h51.split('<div')) - len(h51.split('</div>'))
print(f"5.1 original diff: {diff_51_orig}")

# 1a. Major section headers in 5.1
def repl_h51_header(m):
    inner_num = m.group(1)
    inner_h2 = m.group(2)
    return f'''<div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 18px; border-bottom: 2px solid #bae6fd; padding-bottom: 8px;">
        <div style="display: flex; align-items: center; gap: 12px;">
            {inner_num}
            {inner_h2}
        </div>
        <span style="font-size: 11px; font-weight: 700; background: #f0f9ff; color: #0284c7; padding: 3px 8px; border-radius: 4px; border: 1px solid #bae6fd;">Nghe cả phần</span>
    </div>'''

pat_h51_header = r'<div style="display: flex; align-items: center; gap: 12px; margin-bottom: 18px;">\s*(<div style="width: 36px; height: 36px;[^>]*>.*?</div>)\s*(<h2 style="[^"]*">.*?</h2>)\s*</div>'
h51_mod, count_h51 = re.subn(pat_h51_header, repl_h51_header, h51, flags=re.DOTALL)
print(f"5.1: Replaced {count_h51} section headers")

# 1b. volcanic-cooling
pat_vc = r'<h3 id="volcanic-cooling" class="lecture-interactive-card" data-lecture-section="volcanic_cooling"[^>]*>(.*?)</h3>\s*(<p>.*?</p>)\s*(<!-- Figure 5\.6 -->\s*<div style="margin: 24px auto; background: #f8fafc;[^>]*>.*?</div>\s*</div>)'

def repl_vc(m):
    title = m.group(1).strip()
    para = m.group(2).strip()
    fig = m.group(3).strip()
    return f'''<div id="volcanic-cooling" class="lecture-interactive-card" data-lecture-section="volcanic_cooling" style="margin-top: 24px; margin-bottom: 20px; padding: 20px 22px; background: #ffffff; border: 1.5px solid #bae6fd; border-radius: 12px; box-shadow: 0 2px 6px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s ease;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px; border-bottom: 1.5px solid #bae6fd; padding-bottom: 6px;">
            <h3 style="color: #0369a1; font-size: 18px; font-weight: 700; margin: 0;">{title}</h3>
            <span style="font-size: 11px; font-weight: 700; background: #f0f9ff; color: #0284c7; padding: 2px 7px; border-radius: 4px; border: 1px solid #bae6fd;">Nghe phần này</span>
        </div>
        {para}
        {fig}
    </div>'''

h51_mod, count_vc = re.subn(pat_vc, repl_vc, h51_mod, flags=re.DOTALL)
print(f"5.1: Replaced {count_vc} volcanic-cooling card")

# 1c. gh-gases-breakdown
pat_gh = r'<h3 id="gh-gases-breakdown" class="lecture-interactive-card" data-lecture-section="gh_gases_breakdown"[^>]*>(.*?)</h3>\s*(<p>.*?</p>)\s*(<div style="overflow-x: auto; margin: 18px 0;">\s*<table style="[^"]*">.*?</table>\s*</div>)'

def repl_gh(m):
    title = m.group(1).strip()
    para = m.group(2).strip()
    tbl = m.group(3).strip()
    return f'''<div id="gh-gases-breakdown" class="lecture-interactive-card" data-lecture-section="gh_gases_breakdown" style="margin-top: 24px; margin-bottom: 20px; padding: 20px 22px; background: #ffffff; border: 1.5px solid #bae6fd; border-radius: 12px; box-shadow: 0 2px 6px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s ease;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px; border-bottom: 1.5px solid #bae6fd; padding-bottom: 6px;">
            <h3 style="color: #0369a1; font-size: 18px; font-weight: 700; margin: 0;">{title}</h3>
            <span style="font-size: 11px; font-weight: 700; background: #f0f9ff; color: #0284c7; padding: 2px 7px; border-radius: 4px; border: 1px solid #bae6fd;">Nghe phần này</span>
        </div>
        {para}
        {tbl}
    </div>'''

h51_mod, count_gh = re.subn(pat_gh, repl_gh, h51_mod, flags=re.DOTALL)
print(f"5.1: Replaced {count_gh} gh-gases-breakdown card")

diff_51_new = len(h51_mod.split('<div')) - len(h51_mod.split('</div>'))
print(f"5.1 new diff: {diff_51_new}")
if diff_51_new != 0:
    raise ValueError(f"5.1 diff mismatch: {diff_51_new}")

with open('scripts/raw_geo/5_1_p1_transformed.html', 'w', encoding='utf-8') as f:
    f.write(h51_mod)


# ==============================================================================
# 2. TRANSFORM 5.2
# ==============================================================================
with open('scripts/raw_geo/5_2_p1.html', 'r', encoding='utf-8') as f:
    h52 = f.read()

diff_52_orig = len(h52.split('<div')) - len(h52.split('</div>'))
print(f"\n5.2 original diff: {diff_52_orig}")

def repl_h52_header(m):
    mb = m.group(1)
    inner_num = m.group(2)
    inner_h2 = m.group(3)
    return f'''<div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: {mb}; border-bottom: 2px solid #99f6e4; padding-bottom: 8px;">
        <div style="display: flex; align-items: center; gap: 12px;">
            {inner_num}
            {inner_h2}
        </div>
        <span style="font-size: 11px; font-weight: 700; background: #f0fdfa; color: #0f766e; padding: 3px 8px; border-radius: 4px; border: 1px solid #99f6e4;">Nghe cả phần</span>
    </div>'''

pat_h52_header = r'<div style="display: flex; align-items: center; gap: 12px; margin-bottom: (18px|14px);">\s*(<div style="width: 36px; height: 36px;[^>]*>.*?</div>)\s*(<h2 style="[^"]*">.*?</h2>)\s*</div>'
h52_mod, count_h52 = re.subn(pat_h52_header, repl_h52_header, h52, flags=re.DOTALL)
print(f"5.2: Replaced {count_h52} section headers")

diff_52_new = len(h52_mod.split('<div')) - len(h52_mod.split('</div>'))
print(f"5.2 new diff: {diff_52_new}")
if diff_52_new != 0:
    raise ValueError(f"5.2 diff mismatch: {diff_52_new}")

with open('scripts/raw_geo/5_2_p1_transformed.html', 'w', encoding='utf-8') as f:
    f.write(h52_mod)


# ==============================================================================
# 3. TRANSFORM 5.3
# ==============================================================================
with open('scripts/raw_geo/5_3_p1.html', 'r', encoding='utf-8') as f:
    h53 = f.read()

diff_53_orig = len(h53.split('<div')) - len(h53.split('</div>'))
print(f"\n5.3 original diff: {diff_53_orig}")

# 3a. Major section headers in 5.3
def repl_h53_header(m):
    mb = m.group(1)
    inner_num = m.group(2)
    inner_h2 = m.group(3)
    return f'''<div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: {mb}; border-bottom: 2px solid #a7f3d0; padding-bottom: 8px;">
        <div style="display: flex; align-items: center; gap: 12px;">
            {inner_num}
            {inner_h2}
        </div>
        <span style="font-size: 11px; font-weight: 700; background: #ecfdf5; color: #059669; padding: 3px 8px; border-radius: 4px; border: 1px solid #a7f3d0;">Nghe cả phần</span>
    </div>'''

pat_h53_header = r'<div style="display: flex; align-items: center; gap: 12px; margin-bottom: (18px|14px);">\s*(<div style="width: 36px; height: 36px;[^>]*>.*?</div>)\s*(<h2 style="[^"]*">.*?</h2>)\s*</div>'
h53_mod, count_h53 = re.subn(pat_h53_header, repl_h53_header, h53, flags=re.DOTALL)
print(f"5.3: Replaced {count_h53} section headers")

# 3b. accords-history
pat_ah = r'<h3 id="accords-history" class="lecture-interactive-card" data-lecture-section="accords_history"[^>]*>(.*?)</h3>\s*(<div style="display: grid; grid-template-columns: repeat\(auto-fit, minmax\(250px, 1fr\)\); gap: 14px;">.*?</div>\s*</div>\s*</div>\s*</div>)'

def repl_ah(m):
    title = m.group(1).strip()
    grid = m.group(2).strip()
    return f'''<div id="accords-history" class="lecture-interactive-card" data-lecture-section="accords_history" style="margin-top: 24px; margin-bottom: 20px; padding: 20px 22px; background: #ffffff; border: 1.5px solid #a7f3d0; border-radius: 12px; box-shadow: 0 2px 6px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s ease;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px; border-bottom: 1.5px solid #a7f3d0; padding-bottom: 6px;">
            <h3 style="color: #0f172a; font-size: 18px; font-weight: 700; margin: 0;">{title}</h3>
            <span style="font-size: 11px; font-weight: 700; background: #ecfdf5; color: #059669; padding: 2px 7px; border-radius: 4px; border: 1px solid #a7f3d0;">Nghe phần này</span>
        </div>
        {grid}
    </div>'''

h53_mod, count_ah = re.subn(pat_ah, repl_ah, h53_mod, flags=re.DOTALL)
print(f"5.3: Replaced {count_ah} accords-history card")

# 3c. bd-policy-framework
pat_bd = r'<h3 id="bd-policy-framework" class="lecture-interactive-card" data-lecture-section="bd_policy_framework"[^>]*>(.*?)</h3>\s*(<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 10px; padding: 18px;">.*?</div>\s*</div>\s*</div>\s*</div>\s*</div>)'

def repl_bd(m):
    title = m.group(1).strip()
    content = m.group(2).strip()
    return f'''<div id="bd-policy-framework" class="lecture-interactive-card" data-lecture-section="bd_policy_framework" style="margin-top: 24px; margin-bottom: 20px; padding: 20px 22px; background: #ffffff; border: 1.5px solid #a7f3d0; border-radius: 12px; box-shadow: 0 2px 6px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s ease;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px; border-bottom: 1.5px solid #a7f3d0; padding-bottom: 6px;">
            <h3 style="color: #0f172a; font-size: 18px; font-weight: 700; margin: 0;">{title}</h3>
            <span style="font-size: 11px; font-weight: 700; background: #ecfdf5; color: #059669; padding: 2px 7px; border-radius: 4px; border: 1px solid #a7f3d0;">Nghe phần này</span>
        </div>
        {content}
    </div>'''

h53_mod, count_bd = re.subn(pat_bd, repl_bd, h53_mod, flags=re.DOTALL)
print(f"5.3: Replaced {count_bd} bd-policy-framework card")

diff_53_new = len(h53_mod.split('<div')) - len(h53_mod.split('</div>'))
print(f"5.3 new diff: {diff_53_new}")
if diff_53_new != 0:
    raise ValueError(f"5.3 diff mismatch: {diff_53_new}")

with open('scripts/raw_geo/5_3_p1_transformed.html', 'w', encoding='utf-8') as f:
    f.write(h53_mod)

print("\n🎉 Topic 5 transformation complete and verified!")
