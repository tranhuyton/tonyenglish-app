import sys
if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
from bs4 import BeautifulSoup
import json

with open('scripts/geo_3_1_p1.html', 'r', encoding='utf-8') as f:
    soup = BeautifulSoup(f.read(), 'html.parser')

cards = soup.find_all(class_='lecture-interactive-card')
print('Found interactive cards:', len(cards))
for c in cards:
    cid = c.get('id')
    sec = c.get('data-lecture-section')
    text = c.get_text(strip=True)[:40]
    print(f"  <{c.name}> id='{cid}' data-lecture-section='{sec}' : {text}")

print("\nAll elements with id starting with sec-:")
for el in soup.find_all(id=True):
    if el['id'].startswith('sec-'):
        print(f"  <{el.name}> id='{el['id']}' class='{el.get('class')}'")
