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

all_audit = {}

for m in mods:
    m_title = m['title']
    if 'Past Paper' in m_title:
        continue
    
    lecs = sb.table('lectures').select('id, title, order_index').eq('module_id', m['id']).order('order_index').execute().data
    all_audit[m_title] = []
    
    for l in lecs:
        lid = l['id']
        ltitle = l['title']
        
        pages = sb.table('lecture_pages').select('page_number, content_html').eq('lecture_id', lid).order('page_number').execute().data
        p_map = {p['page_number']: p.get('content_html') or '' for p in pages}
        
        p1 = p_map.get(1, '')
        p2 = p_map.get(2, '')
        p3 = p_map.get(3, '')
        
        # Parse P3 syllabus requirements
        soup3 = BeautifulSoup(p3, 'html.parser')
        
        # Syllabus items usually live in table rows, li, or p tags
        # Let's extract all bullet points / numbered items
        items = []
        for tag in soup3.find_all(['li', 'tr', 'p']):
            txt = tag.get_text().strip()
            # Look for Cambridge syllabus lines: e.g. "1 Describe...", "State that...", Core/Supplement bullets
            if len(txt) > 20 and any(keyword in txt.lower() for keyword in ['describe', 'state', 'explain', 'identify', 'outline', 'define', 'discuss', 'calculate', 'recall', 'understand']):
                # clean up multiple whitespaces
                clean_txt = re.sub(r'\s+', ' ', txt)
                if clean_txt not in items and not clean_txt.startswith('🎯') and not clean_txt.startswith('Syllabus'):
                    items.append(clean_txt)
        
        # Check text in P1 and P2
        soup1 = BeautifulSoup(p1, 'html.parser')
        p1_text = soup1.get_text().lower()
        
        soup2 = BeautifulSoup(p2, 'html.parser')
        p2_text = soup2.get_text().lower()
        
        # Check toolbar in P1, P2, P3
        tb1 = 'Tài liệu học tập' in p1 or 'Study Resource' in p1
        tb2 = 'Tài liệu học tập' in p2 or 'Study Resource' in p2
        tb3 = 'Tài liệu học tập' in p3 or 'Study Resource' in p3
        
        # Check ID collision between P1 and P2
        ids1 = set(el['id'] for el in soup1.find_all(id=True))
        ids2 = set(el['id'] for el in soup2.find_all(id=True))
        coll = list(ids1.intersection(ids2))
        
        # Check Vietnamese in P1
        p1_headings = [h.get_text().strip() for h in soup1.find_all(['h1', 'h2', 'h3', 'h4'])]
        vn_headings = [h for h in p1_headings if re.search(r'[àáạảãâầấậẩẫăằắặẳẵèéẹẻẽêềếệểễìíịỉĩòóọỏõôồốộổỗơờớợởỡùúụủũưừứựửữỳýỵỷỹđĐ]', h)]
        
        all_audit[m_title].append({
            'id': lid,
            'title': ltitle,
            'p1_len': len(p1),
            'p2_len': len(p2),
            'p3_len': len(p3),
            'toolbar_p1': tb1,
            'toolbar_p2': tb2,
            'toolbar_p3': tb3,
            'id_collisions': coll,
            'vn_headings_p1': vn_headings,
            'syllabus_items_count': len(items),
            'syllabus_sample': items[:8],
            'all_syllabus_items': items
        })

with open('scripts/deep_audit_0654_all.json', 'w', encoding='utf-8') as f:
    json.dump(all_audit, f, ensure_ascii=False, indent=2)

print("Saved detailed syllabus audit to scripts/deep_audit_0654_all.json")
