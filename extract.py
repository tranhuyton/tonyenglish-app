import json

def extract_vocab(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        d = json.load(f)
    print(f"File: {filename}")
    for i, part in enumerate(d.get('parts', [])):
        if part.get('title', '').startswith('Word List'):
            content = part.get('content', '')
            words = []
            parts = content.split('color: #65a30d;">')[1:]
            for p in parts:
                w = p.split('</span>')[0].split('>')[-1]
                words.append(w)
            print(f"Part {i} ({part['title']}): {words}")

extract_vocab('public/unit6_ielts.json')
extract_vocab('public/unit7_ielts.json')
