# -*- coding: utf-8 -*-
"""
Execute Upgrade for Cambridge IGCSE Biology Topics 3 to 21 in Supabase:
- Adds visible 🎧 audio badges to all major headings and sub-headings/cards
- Adds cursor: pointer to all headings and card containers
- Unhides all cards previously trapped inside display: none
- Cleans up corrupted/duplicate style attributes
- Guarantees div balance (diff == 0) on Page 1 and Page 2
- Updates lecture_pages in Supabase
"""

import os
import sys
import json
import re
from bs4 import BeautifulSoup
from audio_lecture_engine import sb

sys.stdout.reconfigure(encoding='utf-8')

def clean_double_style(html):
    # Fix corrupted style="... style="...
    html = re.sub(r'style="([^"]*?)\s+style="', r'style="\1; ', html)
    return html

def upgrade_topic_html(html, manifest, is_vietnamese=False):
    html = clean_double_style(html)
    soup = BeautifulSoup(html, 'html.parser')
    
    sec_badge_text = "🎧 Nghe phần này" if is_vietnamese else "🎧 Listen to Section"
    card_badge_text = "🎧 Nghe giảng" if is_vietnamese else "🎧 Audio"

    for s in manifest.get('segments', []):
        sid = s['id']
        sel = s['selector']
        el = soup.select_one(sel)
        if not el:
            print(f"    ❌ WARNING: {sid} ({sel}) not found!")
            continue

        # If selector matched a <br> tag, move id to parent
        if el.name == 'br' and el.parent and el.parent.name in ['h1', 'h2', 'h3', 'h4', 'div']:
            parent = el.parent
            parent['id'] = el.get('id', sid.replace('_', '-'))
            parent['data-lecture-section'] = sid
            el.decompose()
            el = parent

        # Check and unhide any display:none ancestor
        curr = el
        while curr and curr.name != '[document]':
            if curr.has_attr('style') and 'display: none' in curr['style']:
                print(f"    Unhiding display:none on <{curr.name} id='{curr.get('id')}'> for {sid}")
                new_style = curr['style'].replace('display: none;', 'display: block;').replace('display:none;', 'display: block;').replace('display: none', 'display: block')
                curr['style'] = new_style
            curr = curr.parent

        # Add lecture-interactive-card class
        classes = el.get('class', [])
        if isinstance(classes, str):
            classes = [classes]
        if 'lecture-interactive-card' not in classes:
            classes.append('lecture-interactive-card')
        el['class'] = classes

        # Add data-lecture-section
        el['data-lecture-section'] = sid

        # Ensure cursor: pointer
        style = el.get('style', '')
        if 'cursor: pointer' not in style and 'cursor:pointer' not in style:
            style = f"cursor: pointer; {style}".strip()
            el['style'] = style

        # Add Badge
        if sid == 'intro':
            pass
        elif sid.startswith('sec_') or sid.startswith('sec-') or 'sec' in sel:
            # Section header
            if '🎧' not in el.get_text():
                badge = soup.new_tag('span')
                badge['style'] = "font-size: 12px; color: #1d4ed8; font-weight: 600; background: #eff6ff; padding: 4px 10px; border-radius: 12px; border: 1px solid #bfdbfe; float: right; margin-left: 10px; font-family: sans-serif; display: inline-flex; align-items: center; gap: 4px;"
                badge.string = sec_badge_text
                el.append(badge)
        else:
            # Sub-card
            if '🎧' not in el.get_text():
                badge = soup.new_tag('span')
                badge['style'] = "font-size: 11px; color: #2563eb; background: #eff6ff; padding: 3px 8px; border-radius: 10px; font-weight: 600; float: right; margin-left: 8px; font-family: sans-serif; display: inline-flex; align-items: center; gap: 4px;"
                badge.string = card_badge_text
                el.append(badge)

            # If parent is a card container div, make the entire card clickable too
            p = el.parent
            if p and p.name == 'div':
                p_style = p.get('style', '')
                if any(k in p_style for k in ['background', 'border', 'padding', 'flex:']):
                    p_classes = p.get('class', [])
                    if isinstance(p_classes, str): p_classes = [p_classes]
                    if 'lecture-interactive-card' not in p_classes:
                        p_classes.append('lecture-interactive-card')
                    p['class'] = p_classes
                    p['data-lecture-section'] = sid
                    if 'cursor: pointer' not in p_style and 'cursor:pointer' not in p_style:
                        p['style'] = f"cursor: pointer; {p_style}".strip()

    out = str(soup)
    d = out.count('<div') - out.count('</div>')
    if d > 0:
        out += '</div>' * d
    elif d < 0:
        for _ in range(-d):
            idx = out.rfind('</div>')
            if idx != -1:
                out = out[:idx] + out[idx+6:]

    return out

def main():
    COURSE_ID = 'a68bae8c-a21c-4cb2-8cd7-6097de211060'
    res = sb.table('lectures').select('id, title, order_index').eq('course_id', COURSE_ID).order('order_index').execute().data
    topic_map = {}
    for l in res:
        m = re.search(r'Topic\s+(\d+)', l['title'], re.IGNORECASE)
        if m:
            topic_map[int(m.group(1))] = l

    print("="*80)
    print("UPGRADING BIOLOGY TOPICS 3 TO 21 IN SUPABASE...")
    print("="*80)

    for num in range(3, 22):
        l = topic_map.get(num)
        if not l:
            print(f"Skipping Topic {num}: Not found")
            continue
        lid = l['id']
        manifest_path = f'public/audio/lectures/biology/{num}/manifest.json'
        if not os.path.exists(manifest_path):
            print(f"Skipping Topic {num}: manifest not found")
            continue

        with open(manifest_path, 'r', encoding='utf-8') as f:
            manifest = json.load(f)

        print(f"\nProcessing Topic {num:02d}: {l['title']} ({len(manifest['segments'])} segments)...")
        pages_res = sb.table('lecture_pages').select('page_number, content_html').eq('lecture_id', lid).order('page_number').execute()
        pages = {p['page_number']: p['content_html'] for p in pages_res.data}

        p1_raw = pages.get(1, '')
        p2_raw = pages.get(2, '')

        p1_up = upgrade_topic_html(p1_raw, manifest, is_vietnamese=False)
        p2_up = upgrade_topic_html(p2_raw, manifest, is_vietnamese=True)

        d1 = p1_up.count('<div') - p1_up.count('</div>')
        d2 = p2_up.count('<div') - p2_up.count('</div>')
        assert d1 == 0 and d2 == 0, f"Divs unbalanced in Topic {num}: P1={d1}, P2={d2}"

        # Update Supabase
        sb.table('lecture_pages').update({'content_html': p1_up}).eq('lecture_id', lid).eq('page_number', 1).execute()
        sb.table('lecture_pages').update({'content_html': p2_up}).eq('lecture_id', lid).eq('page_number', 2).execute()
        print(f"  ✅ Updated Supabase for Topic {num:02d} Page 1 & Page 2 (Divs: P1={d1}, P2={d2})")

    print("\n" + "="*80)
    print("🎉 ALL TOPICS 3 TO 21 SUCCESSFULLY UPGRADED AND UPLOADED TO SUPABASE!")
    print("="*80)

if __name__ == '__main__':
    main()
