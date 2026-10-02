import re
import sys
from bs4 import BeautifulSoup

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

pat_c1 = (
    r'<div style="background:\s*#ffffff;\s*border:\s*1px solid #e2e8f0;\s*border-radius:\s*12px;\s*padding:\s*28px;\s*margin-bottom:\s*25px;\s*box-shadow:\s*0 4px 12px rgba\(0,0,0,0\.03\);">\s*'
    r'<div style="display:\s*flex;\s*align-items:\s*center;\s*gap:\s*10px;\s*margin-bottom:\s*18px;\s*border-bottom:\s*2px solid #e2e8f0;\s*padding-bottom:\s*12px;">\s*'
    r'(<span style="[^"]*">.*?</span>\s*)'
    r'<h2 (?=[^>]*\bid="([^"]+)")(?=[^>]*\bdata-lecture-section="([^"]+)")[^>]*>(.*?)</h2>\s*'
    r'</div>'
)

def repl_c1(m):
    span_tag = m.group(1).strip()
    sec_id = m.group(2).strip()
    sec_name = m.group(3).strip()
    h2_text = m.group(4).strip()
    return (
        f'<div id="{sec_id}" class="lecture-interactive-card" data-lecture-section="{sec_name}" style="background: #ffffff; border: 1.5px solid #fed7aa; border-radius: 14px; padding: 28px; margin-bottom: 25px; box-shadow: 0 4px 12px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s ease; position: relative;">\n'
        f'  <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #fff7ed; border: 1px solid #fed7aa; border-radius: 20px; font-size: 12px; font-weight: 600; color: #c2410c; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>\n'
        f'  <div style="display: flex; align-items: center; gap: 10px; margin-bottom: 18px; border-bottom: 2px solid #fed7aa; padding-bottom: 12px; padding-right: 140px;">\n'
        f'    {span_tag}\n'
        f'    <h2 style="margin: 0; color: #0f172a; font-size: 22px; font-weight: 700;">{h2_text}</h2>\n'
        f'  </div>'
    )

pat_c2_12 = (
    r'<div style="margin-bottom:\s*(?:50px|60px);">\s*'
    r'<h2 (?=[^>]*\bid="([^"]+)")(?=[^>]*\bdata-lecture-section="([^"]+)")[^>]*>(.*?)</h2>'
)

def repl_c2_12(m):
    sec_id = m.group(1).strip()
    sec_name = m.group(2).strip()
    h2_text = m.group(3).strip()
    return (
        f'<div id="{sec_id}" class="lecture-interactive-card" data-lecture-section="{sec_name}" style="background: #ffffff; border: 1.5px solid #fed7aa; border-radius: 14px; padding: 26px 28px; margin-bottom: 35px; box-shadow: 0 4px 12px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s ease; position: relative;">\n'
        f'  <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #fff7ed; border: 1px solid #fed7aa; border-radius: 20px; font-size: 12px; font-weight: 600; color: #c2410c; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>\n'
        f'  <h2 style="margin-top: 0; color: #0f172a; border-bottom: 3px solid #fed7aa; padding-bottom: 10px; margin-bottom: 25px; font-size: 24px; font-weight: 700; padding-right: 140px;">{h2_text}</h2>'
    )

pat_phys = (
    r'<div style="background:\s*#ffffff;\s*border:\s*2px solid #e2e8f0;\s*border-radius:\s*12px;\s*padding:\s*25px;[^"]*">\s*'
    r'<h2 (?=[^>]*\bid="([^"]+)")(?=[^>]*\bdata-lecture-section="([^"]+)")[^>]*>(.*?)</h2>'
)

def repl_phys(m):
    sec_id = m.group(1).strip()
    sec_name = m.group(2).strip()
    h2_text = m.group(3).strip()
    return (
        f'<div id="{sec_id}" class="lecture-interactive-card" data-lecture-section="{sec_name}" style="background: #ffffff; border: 1.5px solid #bfdbfe; border-radius: 14px; padding: 25px; margin-bottom: 30px; box-shadow: 0 4px 12px rgba(0,0,0,0.03); cursor: pointer; transition: all 0.2s ease; position: relative;">\n'
        f'  <div style="position: absolute; top: 16px; right: 16px; display: inline-flex; align-items: center; gap: 6px; padding: 4px 10px; background: #eff6ff; border: 1px solid #bfdbfe; border-radius: 20px; font-size: 12px; font-weight: 600; color: #0284c7; pointer-events: none;"><span style="font-size: 13px;">🎧</span> Nghe phần này</div>\n'
        f'  <h2 style="margin-top: 0; color: #0f172a; border-bottom: 2px solid #bfdbfe; padding-bottom: 10px; margin-bottom: 20px; font-size: 21px; font-weight: 700; display: flex; align-items: center; gap: 8px; padding-right: 140px;">{h2_text}</h2>'
    )

def count_div_diff(html):
    opens = len(re.findall(r'<div\b[^>]*>', html, flags=re.IGNORECASE))
    closes = len(re.findall(r'</div>', html, flags=re.IGNORECASE))
    return opens - closes

print("=== RUNNING TEST TRANSFORMATIONS ===")
all_chem = [f"c{i}" for i in range(1, 13)]
all_phys = [f"p{i}" for i in range(1, 7)]

success_all = True

for code in all_chem + all_phys:
    orig_path = f"scripts/raw_science_chem_phys/{code}_p1.html"
    with open(orig_path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    orig_diff = count_div_diff(html)
    
    if code == 'c1':
        new_html = re.sub(pat_c1, repl_c1, html, flags=re.DOTALL)
    elif code.startswith('c'):
        new_html = re.sub(pat_c2_12, repl_c2_12, html, flags=re.DOTALL)
    else:
        new_html = re.sub(pat_phys, repl_phys, html, flags=re.DOTALL)
    
    new_diff = count_div_diff(new_html)
    
    # Check for any remaining h2 cards
    soup = BeautifulSoup(new_html, 'html.parser')
    h2_cards = [h for h in soup.find_all('h2') if 'lecture-interactive-card' in h.get('class', [])]
    div_cards = [d for d in soup.find_all('div') if 'lecture-interactive-card' in d.get('class', [])]
    
    # Write transformed file
    out_path = f"scripts/raw_science_chem_phys/{code}_p1_transformed.html"
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(new_html)
        
    diff_ok = (new_diff == 0)
    h2_ok = (len(h2_cards) == 0)
    div_ok = (len(div_cards) > 0)
    
    status = "OK" if (diff_ok and h2_ok and div_ok) else "FAIL"
    if status == "FAIL":
        success_all = False
    
    print(f"[{code.upper():4}] status: {status:4} | orig_diff: {orig_diff} -> new_diff: {new_diff} | div_cards: {len(div_cards)} | h2_cards: {len(h2_cards)}")

print(f"\nALL LESSONS TRANSFORMED SUCCESSFULLY? {success_all}")
