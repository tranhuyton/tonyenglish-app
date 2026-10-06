# -*- coding: utf-8 -*-
"""
Master Verification Script for all Cambridge IGCSE Biology (0610) Topics 1 to 21
Verifies:
1. Supabase Page 1 & Page 2 HTML div balance (diff == 0)
2. Manifest.json existence and validity
3. 100% of manifest selectors match in Page 1 and Page 2
4. Audio mp3 files exist on disk and have non-zero size
5. Summary table of segments, durations, and compliance
"""

import os
import sys
import json
import re
from bs4 import BeautifulSoup
from audio_lecture_engine import sb

sys.stdout.reconfigure(encoding='utf-8')

COURSE_ID = 'a68bae8c-a21c-4cb2-8cd7-6097de211060'

def master_verify():
    # Fetch all lectures for Cambridge Biology course
    res = sb.table('lectures').select('id, title, order_index').eq('course_id', COURSE_ID).order('order_index').execute()
    lectures = res.data

    topic_map = {}
    for l in lectures:
        m = re.search(r'Topic\s+(\d+):?\s*(.*)', l['title'], re.IGNORECASE)
        if m:
            num = int(m.group(1))
            topic_map[num] = {
                'id': l['id'],
                'full_title': l['title'],
                'short_title': m.group(2).strip(),
                'code': str(num)
            }

    print("="*110)
    print(f"{'TOPIC':<7} | {'TITLE':<38} | {'SEGS':<5} | {'DURATION':<9} | {'DIV P1/P2':<10} | {'SELECTORS':<10} | {'STATUS'}")
    print("="*110)

    total_duration = 0.0
    total_segments = 0
    all_passed = True

    for num in range(1, 22):
        info = topic_map.get(num)
        if not info:
            print(f"Topic {num:02d} | {'NOT FOUND IN DATABASE':<38} | {'-':<5} | {'-':<9} | {'-':<10} | {'-':<10} | ❌ MISSING")
            all_passed = False
            continue

        lid = info['id']
        short_t = (info['short_title'][:35] + '...') if len(info['short_title']) > 38 else info['short_title']

        # 1. Check pages in Supabase
        pages_res = sb.table('lecture_pages').select('page_number, content_html').eq('lecture_id', lid).order('page_number').execute()
        pages = {p['page_number']: p['content_html'] for p in pages_res.data}
        p1 = pages.get(1, '')
        p2 = pages.get(2, '')

        d1 = p1.count('<div') - p1.count('</div>') if p1 else -999
        d2 = p2.count('<div') - p2.count('</div>') if p2 else -999
        div_str = f"{d1}/{d2}"

        # 2. Check manifest on disk
        manifest_path = os.path.join('public', 'audio', 'lectures', 'biology', str(num), 'manifest.json')
        if not os.path.exists(manifest_path):
            print(f"Topic {num:02d} | {short_t:<38} | {'0':<5} | {'0s':<9} | {div_str:<10} | {'0/0':<10} | ❌ NO MANIFEST")
            all_passed = False
            continue

        with open(manifest_path, 'r', encoding='utf-8') as f:
            manifest = json.load(f)

        segs = manifest.get('segments', [])
        dur = manifest.get('totalDuration', 0.0)
        total_duration += dur
        total_segments += len(segs)

        # 3. Check selectors in P1 and P2
        soup1 = BeautifulSoup(p1, 'html.parser') if p1 else None
        soup2 = BeautifulSoup(p2, 'html.parser') if p2 else None

        missing_p1 = []
        missing_p2 = []
        audio_missing = []

        audio_dir = os.path.join('public', 'audio', 'lectures', 'biology', str(num))
        for s in segs:
            sel = s['selector']
            if not soup1 or not soup1.select(sel):
                missing_p1.append(sel)
            if not soup2 or not soup2.select(sel):
                missing_p2.append(sel)
            
            # 4. Check audio file
            mp3_path = os.path.join(audio_dir, f"{s['id']}.mp3")
            if not os.path.exists(mp3_path) or os.path.getsize(mp3_path) < 1000:
                audio_missing.append(s['id'])

        sel_match = f"{len(segs) - len(missing_p1)}/{len(segs)}"
        dur_str = f"{dur:.1f}s"

        issues = []
        if d1 != 0 or d2 != 0:
            issues.append(f"Div Diff ({div_str})")
        if missing_p1:
            issues.append(f"P1 Missing ({len(missing_p1)})")
        if missing_p2:
            issues.append(f"P2 Missing ({len(missing_p2)})")
        if audio_missing:
            issues.append(f"Audio Missing ({len(audio_missing)})")

        if not issues:
            status = "✅ PERFECT"
        else:
            status = f"❌ {', '.join(issues)}"
            all_passed = False

        print(f"Topic {num:02d} | {short_t:<38} | {len(segs):<5} | {dur_str:<9} | {div_str:<10} | {sel_match:<10} | {status}")

    print("="*110)
    mins = total_duration / 60.0
    print(f"TOTAL: 21 Topics | {total_segments} Segments | {total_duration:.1f}s ({mins:.1f} mins) Audio Lecture Content")
    if all_passed:
        print("🎉 ALL 21 TOPICS FULLY VALIDATED: 100% SELECTORS MATCHED & 0 DIV DIFFS ON BOTH PAGES!")
    else:
        print("⚠️ Some topics still require processing or have warnings.")

if __name__ == '__main__':
    master_verify()
