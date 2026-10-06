import os
import sys
import re
from bs4 import BeautifulSoup

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

# Read original 3_1_p1.html
with open('scripts/raw_geo/3_1_p1.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Verify initial diff
diff_orig = len(html.split('<div')) - len(html.split('</div>'))
print(f"Original 3_1 diff: {diff_orig}")

# Let's inspect where the 5 sections are:
# 1. id="sec-geography"
# 2. id="sec-climate"
# 3. id="sec-food-web"
# 4. id="sec-adaptations"
# 5. id="sec-seasonal-cycles"

pattern_geography = r'<h2 id="sec-geography" class="lecture-interactive-card" data-lecture-section="sec_geography"[^>]*>(.*?)</h2>\s*<p>(.*?)</p>'
replacement_geography = '''<div id="sec-geography" class="lecture-interactive-card" data-lecture-section="sec_geography" style="margin-bottom: 24px; padding: 22px 24px; background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s ease;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px; border-bottom: 2px solid #bae6fd; padding-bottom: 8px;">
            <h2 style="color: #0369a1; font-size: 22px; font-weight: 700; margin: 0;">\\1</h2>
            <span style="font-size: 11px; font-weight: 700; background: #f0f9ff; color: #0284c7; padding: 3px 8px; border-radius: 4px; border: 1px solid #bae6fd;">Nghe phần này</span>
        </div>
        <p style="margin: 0; color: #334155; font-size: 15px; line-height: 1.6;">
            \\2
        </p>
    </div>'''

pattern_climate = r'<h2 id="sec-climate" class="lecture-interactive-card" data-lecture-section="sec_climate"[^>]*>(.*?)</h2>\s*<p>(.*?)</p>'
replacement_climate = '''<div id="sec-climate" class="lecture-interactive-card" data-lecture-section="sec_climate" style="margin-bottom: 24px; padding: 22px 24px; background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s ease;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px; border-bottom: 2px solid #bae6fd; padding-bottom: 8px;">
            <h2 style="color: #0369a1; font-size: 22px; font-weight: 700; margin: 0;">\\1</h2>
            <span style="font-size: 11px; font-weight: 700; background: #f0f9ff; color: #0284c7; padding: 3px 8px; border-radius: 4px; border: 1px solid #bae6fd;">Nghe phần này</span>
        </div>
        <p style="margin: 0; color: #334155; font-size: 15px; line-height: 1.6;">
            \\2
        </p>
    </div>'''

pattern_food_web = r'<h2 id="sec-food-web" class="lecture-interactive-card" data-lecture-section="sec_food_web"[^>]*>(.*?)</h2>\s*<p>(.*?)</p>'
replacement_food_web = '''<div id="sec-food-web" class="lecture-interactive-card" data-lecture-section="sec_food_web" style="margin-bottom: 24px; padding: 22px 24px; background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s ease;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px; border-bottom: 2px solid #bae6fd; padding-bottom: 8px;">
            <h2 style="color: #0369a1; font-size: 22px; font-weight: 700; margin: 0;">\\1</h2>
            <span style="font-size: 11px; font-weight: 700; background: #f0f9ff; color: #0284c7; padding: 3px 8px; border-radius: 4px; border: 1px solid #bae6fd;">Nghe phần này</span>
        </div>
        <p style="margin: 0; color: #334155; font-size: 15px; line-height: 1.6;">
            \\2
        </p>
    </div>'''

pattern_adaptations = r'<h2 id="sec-adaptations" class="lecture-interactive-card" data-lecture-section="sec_adaptations"[^>]*>(.*?)</h2>\s*<p>(.*?)</p>'
replacement_adaptations = '''<div id="sec-adaptations" class="lecture-interactive-card" data-lecture-section="sec_adaptations" style="margin-bottom: 24px; padding: 22px 24px; background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s ease;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px; border-bottom: 2px solid #bae6fd; padding-bottom: 8px;">
            <h2 style="color: #0369a1; font-size: 22px; font-weight: 700; margin: 0;">\\1</h2>
            <span style="font-size: 11px; font-weight: 700; background: #f0f9ff; color: #0284c7; padding: 3px 8px; border-radius: 4px; border: 1px solid #bae6fd;">Nghe phần này</span>
        </div>
        <p style="margin: 0; color: #334155; font-size: 15px; line-height: 1.6;">
            \\2
        </p>
    </div>'''

pattern_seasonal = r'<h2 id="sec-seasonal-cycles" class="lecture-interactive-card" data-lecture-section="sec_seasonal_cycles"[^>]*>(.*?)</h2>\s*<p>(.*?)</p>'
replacement_seasonal = '''<div id="sec-seasonal-cycles" class="lecture-interactive-card" data-lecture-section="sec_seasonal_cycles" style="margin-bottom: 24px; padding: 22px 24px; background: #ffffff; border: 1.5px solid #cbd5e1; border-radius: 14px; box-shadow: 0 2px 8px rgba(0,0,0,0.02); cursor: pointer; transition: all 0.2s ease;">
        <div style="display: flex; align-items: center; justify-content: space-between; margin-bottom: 12px; border-bottom: 2px solid #bae6fd; padding-bottom: 8px;">
            <h2 style="color: #0369a1; font-size: 22px; font-weight: 700; margin: 0;">\\1</h2>
            <span style="font-size: 11px; font-weight: 700; background: #f0f9ff; color: #0284c7; padding: 3px 8px; border-radius: 4px; border: 1px solid #bae6fd;">Nghe phần này</span>
        </div>
        <p style="margin: 0; color: #334155; font-size: 15px; line-height: 1.6;">
            \\2
        </p>
    </div>'''

new_html = html
for pat, rep in [
    (pattern_geography, replacement_geography),
    (pattern_climate, replacement_climate),
    (pattern_food_web, replacement_food_web),
    (pattern_adaptations, replacement_adaptations),
    (pattern_seasonal, replacement_seasonal)
]:
    new_html, count = re.subn(pat, rep, new_html, flags=re.DOTALL)
    print(f"Replaced {count} instances for pattern {pat[:35]}")

diff_new = len(new_html.split('<div')) - len(new_html.split('</div>'))
print(f"New 3_1 diff: {diff_new}")

with open('scripts/raw_geo/3_1_p1_transformed.html', 'w', encoding='utf-8') as f:
    f.write(new_html)
print("Saved transformed HTML.")
