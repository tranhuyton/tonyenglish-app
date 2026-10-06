import re
from bs4 import BeautifulSoup

def inspect_topic(code):
    with open(f'scripts/raw_geo/{code}_p1.html', 'r', encoding='utf-8') as f:
        html = f.read()
    soup = BeautifulSoup(html, 'html.parser')
    print(f"\n=== INSPECTING {code} ===")
    cards = soup.find_all(class_='lecture-interactive-card')
    print(f"Total interactive cards: {len(cards)}")
    for c in cards:
        cid = c.get('id', 'NO_ID')
        tag = c.name
        classes = " ".join(c.get('class', []))
        style = c.get('style', '')[:60]
        badge = c.find(string=re.compile(r'Nghe'))
        badge_text = badge.strip() if badge else "NO_BADGE"
        print(f"  <{tag} id='{cid}'> badge='{badge_text}' style='{style}...'")

inspect_topic('4_1')
inspect_topic('4_2')
inspect_topic('5_1')
inspect_topic('5_2')
inspect_topic('5_3')
