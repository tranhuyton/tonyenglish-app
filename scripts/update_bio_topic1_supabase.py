# -*- coding: utf-8 -*-
"""
Update Supabase lecture_pages for Topic 1:
- page 1: merged_page_1.html
- page 2: merged_page_2.html
- page 3: original page 5 (syllabus checklist)
- delete old pages 4 and 5
"""

import os
import sys
import re
from supabase import create_client

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

env_path = os.path.join(os.path.dirname(__file__), '..', '.env')
with open(env_path, 'r', encoding='utf-8') as f:
    env = f.read()

URL = re.search(r'^VITE_SUPABASE_URL=(.*)$', env, re.M).group(1).strip()
KEY = re.search(r'^VITE_SUPABASE_ANON_KEY=(.*)$', env, re.M).group(1).strip()
sb = create_client(URL, KEY)

LEC_ID = '11cfe97d-205e-418b-ae79-e39d7e57e0a8'

def run_update():
    with open('scripts/output_bio/merged_page_1.html', 'r', encoding='utf-8') as f:
        html_p1 = f.read()
    with open('scripts/output_bio/merged_page_2.html', 'r', encoding='utf-8') as f:
        html_p2 = f.read()
    with open('scripts/raw_bio/page_5.html', 'r', encoding='utf-8') as f:
        html_p5 = f.read()

    print("Updating Page 1...")
    res1 = sb.table('lecture_pages').update({
        'content_html': html_p1
    }).eq('lecture_id', LEC_ID).eq('page_number', 1).execute()
    print("Page 1 updated:", len(res1.data))

    print("Updating Page 2...")
    res2 = sb.table('lecture_pages').update({
        'content_html': html_p2
    }).eq('lecture_id', LEC_ID).eq('page_number', 2).execute()
    print("Page 2 updated:", len(res2.data))

    print("Updating Page 3 with content of Page 5...")
    res3 = sb.table('lecture_pages').update({
        'content_html': html_p5
    }).eq('lecture_id', LEC_ID).eq('page_number', 3).execute()
    print("Page 3 updated:", len(res3.data))

    print("Deleting old Page 4 and Page 5...")
    del_res = sb.table('lecture_pages').delete().eq('lecture_id', LEC_ID).in_('page_number', [4, 5]).execute()
    print("Deleted rows:", len(del_res.data))

    # Verify final state
    final_pages = sb.table('lecture_pages').select('id, page_number').eq('lecture_id', LEC_ID).order('page_number').execute()
    print("\nFinal lecture_pages state for Topic 1:")
    for p in final_pages.data:
        print(f"  Page {p['page_number']} (id: {p['id']})")

if __name__ == '__main__':
    run_update()
