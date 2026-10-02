import re
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

pat_c1 = (
    r'<div style="background:\s*#ffffff;\s*border:\s*1px solid #e2e8f0;\s*border-radius:\s*12px;\s*padding:\s*28px;\s*margin-bottom:\s*25px;\s*box-shadow:\s*0 4px 12px rgba\(0,0,0,0\.03\);">\s*'
    r'<div style="display:\s*flex;\s*align-items:\s*center;\s*gap:\s*10px;\s*margin-bottom:\s*18px;\s*border-bottom:\s*2px solid #e2e8f0;\s*padding-bottom:\s*12px;">\s*'
    r'(<span style="[^"]*">.*?</span>\s*)'
    r'<h2 (?=[^>]*\bid="([^"]+)")(?=[^>]*\bdata-lecture-section="([^"]+)")[^>]*>(.*?)</h2>\s*'
    r'</div>'
)

pat_c2_12 = (
    r'<div style="margin-bottom:\s*(?:50px|60px);">\s*'
    r'<h2 (?=[^>]*\bid="([^"]+)")(?=[^>]*\bdata-lecture-section="([^"]+)")[^>]*>(.*?)</h2>'
)

pat_phys = (
    r'<div style="background:\s*#ffffff;\s*border:\s*2px solid #e2e8f0;\s*border-radius:\s*12px;\s*padding:\s*25px;[^"]*">\s*'
    r'<h2 (?=[^>]*\bid="([^"]+)")(?=[^>]*\bdata-lecture-section="([^"]+)")[^>]*>(.*?)</h2>'
)

# Test C1
with open("scripts/raw_science_chem_phys/c1_p1.html", 'r', encoding='utf-8') as f:
    h_c1 = f.read()
m_c1 = list(re.finditer(pat_c1, h_c1, flags=re.DOTALL))
print(f"C1 matches: {len(m_c1)} / 4")
for m in m_c1:
    print(f"  ID: {m.group(2)} | Section: {m.group(3)}")

# Test C2 to C12
tot_c = 0
for i in range(2, 13):
    code = f"c{i}"
    with open(f"scripts/raw_science_chem_phys/{code}_p1.html", 'r', encoding='utf-8') as f:
        h = f.read()
    m_c = list(re.finditer(pat_c2_12, h, flags=re.DOTALL))
    print(f"{code.upper():4}: {len(m_c)} matches")
    tot_c += len(m_c)
print(f"Total C2-C12: {tot_c} / 35")

# Test P1 to P6
tot_p = 0
for i in range(1, 7):
    code = f"p{i}"
    with open(f"scripts/raw_science_chem_phys/{code}_p1.html", 'r', encoding='utf-8') as f:
        h = f.read()
    m_p = list(re.finditer(pat_phys, h, flags=re.DOTALL))
    print(f"{code.upper():4}: {len(m_p)} matches")
    tot_p += len(m_p)
print(f"Total Physics: {tot_p} / 26")

grand_total = len(m_c1) + tot_c + tot_p
print(f"\n==========================================")
print(f"GRAND TOTAL MATCHES: {grand_total} / 65")
print(f"==========================================")
