import sys
import re
import json
from supabase import create_client
from bs4 import BeautifulSoup

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

with open('.env', 'r', encoding='utf-8') as f:
    env = f.read()

URL = re.search(r'^VITE_SUPABASE_URL=(.*)$', env, re.M).group(1).strip()
KEY = re.search(r'^VITE_SUPABASE_ANON_KEY=(.*)$', env, re.M).group(1).strip()
sb = create_client(URL, KEY)

course_id = 'a2a949c7-c23e-45a7-82fa-cdeda5cc32a7'
mods = sb.table('lecture_modules').select('*').eq('course_id', course_id).order('order_index').execute().data

def analyze_lecture(lec, mod_name):
    lid = lec['id']
    title = lec['title']
    pages = sb.table('lecture_pages').select('page_number, content_html').eq('lecture_id', lid).order('page_number').execute().data
    
    p_map = {p['page_number']: p.get('content_html') or '' for p in pages}
    p1 = p_map.get(1, '')
    p2 = p_map.get(2, '')
    p3 = p_map.get(3, '')
    
    # 1. Toolbars
    tb1 = 'Tài liệu học tập' in p1 or 'Study Resource' in p1
    tb2 = 'Tài liệu học tập' in p2 or 'Study Resource' in p2
    tb3 = 'Tài liệu học tập' in p3 or 'Study Resource' in p3
    
    # 2. Vietnamese in P1
    # Check for Vietnamese headers or paragraphs in P1
    soup1 = BeautifulSoup(p1, 'html.parser')
    p1_headings = [h.get_text().strip() for h in soup1.find_all(['h1', 'h2', 'h3', 'h4'])]
    vn_headings = [h for h in p1_headings if re.search(r'[àáạảãâầấậẩẫăằắặẳẵèéẹẻẽêềếệểễìíịỉĩòóọỏõôồốộổỗơờớợởỡùúụủũưừứựửữỳýỵỷỹđĐ]', h)]
    
    # 3. Bilingual format in P2
    has_bilingual_p2 = ('🇬🇧' in p2 or 'En:' in p2) and ('🇻🇳' in p2 or 'Vi:' in p2)
    
    # 4. Element ID collisions
    soup2 = BeautifulSoup(p2, 'html.parser')
    ids1 = set(el['id'] for el in soup1.find_all(id=True))
    ids2 = set(el['id'] for el in soup2.find_all(id=True))
    collisions = ids1.intersection(ids2)
    
    # 5. Extract Syllabus requirements from P3
    soup3 = BeautifulSoup(p3, 'html.parser')
    syl_items = []
    for li in soup3.find_all(['li', 'tr', 'p']):
        txt = li.get_text().strip()
        # Look for syllabus points like "1 Describe...", "2 State...", etc.
        m = re.match(r'^(\d+[\.\s]+[A-Z].{15,})', txt)
        if m:
            syl_items.append(m.group(1)[:120])
    
    return {
        'id': lid,
        'title': title,
        'module': mod_name,
        'lengths': {1: len(p1), 2: len(p2), 3: len(p3)},
        'toolbars': {'p1': tb1, 'p2': tb2, 'p3': tb3},
        'vn_headings_p1': vn_headings,
        'has_bilingual_p2': has_bilingual_p2,
        'id_collisions': list(collisions),
        'syl_count': len(syl_items),
        'syl_sample': syl_items[:5]
    }

results = []
for m in mods:
    if 'Past Paper' in m['title']:
        continue
    lecs = sb.table('lectures').select('id, title, order_index').eq('module_id', m['id']).order('order_index').execute().data
    print(f"Scanning {m['title']} ({len(lecs)} lectures)...")
    for l in lecs:
        res = analyze_lecture(l, m['title'])
        results.append(res)

with open('scripts/audit_0654_all_results.json', 'w', encoding='utf-8') as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print(f"\nDone auditing {len(results)} lectures! Output saved to scripts/audit_0654_all_results.json")
