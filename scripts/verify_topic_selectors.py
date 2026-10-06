# -*- coding: utf-8 -*-
import sys
import json
from bs4 import BeautifulSoup
from audio_lecture_engine import sb

sys.stdout.reconfigure(encoding='utf-8')

def verify_topic(topic_num, lecture_id):
    p1 = sb.table('lecture_pages').select('content_html').eq('lecture_id', lecture_id).eq('page_number', 1).single().execute().data['content_html']
    p2 = sb.table('lecture_pages').select('content_html').eq('lecture_id', lecture_id).eq('page_number', 2).single().execute().data['content_html']

    d1 = p1.count('<div') - p1.count('</div>')
    d2 = p2.count('<div') - p2.count('</div>')
    print(f"Topic {topic_num} Div diff: P1 = {d1}, P2 = {d2}")

    manifest_path = f"public/audio/lectures/biology/{topic_num}/manifest.json"
    with open(manifest_path, 'r', encoding='utf-8') as f:
        mf = json.load(f)

    soup1 = BeautifulSoup(p1, 'html.parser')
    soup2 = BeautifulSoup(p2, 'html.parser')

    all_ok = True
    for seg in mf['segments']:
        sel = seg.get('selector')
        if sel:
            m1 = soup1.select(sel)
            m2 = soup2.select(sel)
            if not m1 or not m2:
                print(f"  [MISMATCH] {seg['id']}: sel='{sel}' (P1 count: {len(m1)}, P2 count: {len(m2)})")
                all_ok = False

    if all_ok and d1 == 0 and d2 == 0:
        print(f"🎉 Topic {topic_num}: PERFECT! 100% of {len(mf['segments'])} selectors match & div diff == 0!")
    else:
        print(f"⚠️ Topic {topic_num}: Needs attention!")

if __name__ == '__main__':
    t_num = int(sys.argv[1]) if len(sys.argv) > 1 else 2
    # Load topics map
    cid = 'a68bae8c-a21c-4cb2-8cd7-6097de211060'
    import re
    lecs = sb.table('lectures').select('id, title').eq('course_id', cid).execute()
    t_id = None
    for l in lecs.data:
        m = re.search(r'Topic\s+(\d+):?', l['title'], re.IGNORECASE)
        if m and int(m.group(1)) == t_num:
            t_id = l['id']
            break
    if t_id:
        verify_topic(t_num, t_id)
    else:
        print(f"Topic {t_num} not found in database!")
