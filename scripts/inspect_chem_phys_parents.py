from bs4 import BeautifulSoup
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

all_codes = [f"c{i}" for i in range(1, 13)] + [f"p{i}" for i in range(1, 7)]

for code in all_codes:
    hpath = f"scripts/raw_science_chem_phys/{code}_p1.html"
    with open(hpath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    soup = BeautifulSoup(html, 'html.parser')
    h2s = soup.find_all('h2')
    h2_cards = [h for h in h2s if 'lecture-interactive-card' in h.get('class', []) or h.get('id', '').startswith('sec-')]
    
    print(f"\n=== {code.upper()} ({len(h2_cards)} sections) ===")
    for hc in h2_cards:
        p = hc.parent
        gp = p.parent if p else None
        print(f"  {hc.get('id'):26} | P: <{p.name} style='{p.get('style', '')[:40]}'> | GP: <{gp.name if gp else 'None'} style='{gp.get('style', '')[:40] if gp else ''}'>")
