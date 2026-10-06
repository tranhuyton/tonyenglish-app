import os
import sys
import re
from bs4 import BeautifulSoup

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

topics = ['3_1', '3_2', '3_3', '3_4', '4_1', '4_2', '4_3', '4_4', '5_1', '5_2', '5_3']

for t in topics:
    fname = f"scripts/raw_geo/{t}_p1.html"
    if not os.path.exists(fname):
        print(f"{t}: NOT FOUND")
        continue
    with open(fname, 'r', encoding='utf-8') as f:
        html = f.read()
    
    soup = BeautifulSoup(html, 'html.parser')
    
    # Find all elements with data-lecture-section
    secs = soup.find_all(attrs={"data-lecture-section": True})
    
    h_tags = [f"<{s.name} id='{s.get('id')}' sec='{s.get('data-lecture-section')}'>" for s in secs if s.name in ['h1', 'h2', 'h3', 'h4']]
    div_tags = [f"<{s.name} id='{s.get('id')}' sec='{s.get('data-lecture-section')}'>" for s in secs if s.name == 'div']
    g_tags = [f"<{s.name} id='{s.get('id')}' sec='{s.get('data-lecture-section')}'>" for s in secs if s.name == 'g']
    
    print(f"\n=== Lecture {t} (len: {len(html)}) ===")
    print(f"Total interactive elements: {len(secs)}")
    print(f"  Heading cards ({len(h_tags)}):", ", ".join(h_tags))
    print(f"  Div cards ({len(div_tags)}):", ", ".join(div_tags[:6]), "..." if len(div_tags) > 6 else "")
    print(f"  SVG cards ({len(g_tags)}):", ", ".join(g_tags[:6]), "..." if len(g_tags) > 6 else "")
