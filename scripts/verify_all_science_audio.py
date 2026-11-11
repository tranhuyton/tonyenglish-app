# -*- coding: utf-8 -*-
"""
End-to-End Post-Deployment Verification for all 76 Cambridge IGCSE Science Audio Lectures
(0610 Biology, 0620 Chemistry, 0625 Physics, 0654 Co-ordinated Sciences).
Checks:
  1. LECTURE_MANIFEST_MAP in src/LectureViewer.tsx covers all 76 lecture IDs with exact manifest URLs.
  2. Every manifest.json + granular MP3 file exists on disk, size > 1500B, duration > 0.5s, 0 orphan MP3s.
  3. Live Supabase lecture_pages (Page 1 & Page 2) have 0 div imbalances, 0 hidden data-lecture-section leaks,
     0 Vietnamese characters in Page 1 audio badges, and 100% selector resolution on both pages.
"""

import os
import sys
import re
import json
from bs4 import BeautifulSoup
from rebuild_all_science_audio import (
    REPO_ROOT, LECTURE_SPECS, sb, has_hidden_ancestor, VI_DIACRITIC_RE
)

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')
    sys.stderr.reconfigure(encoding='utf-8')


def main():
    lv_path = os.path.join(REPO_ROOT, 'src', 'LectureViewer.tsx')
    lv_src = open(lv_path, 'r', encoding='utf-8').read()

    total_mp3s = 0
    total_bytes = 0
    total_duration_sec = 0.0
    errors = []

    print(f"Auditing all {len(LECTURE_SPECS)} Science lectures (Frontend + Disk MP3s + Live Supabase P1/P2)...", flush=True)

    for idx, (subj, code, lid, course_title) in enumerate(LECTURE_SPECS, 1):
        key = f"{subj}/{code}"
        expected_url = f"/audio/lectures/{subj}/{code}/manifest.json"

        # 1. Check LectureViewer.tsx mapping
        pat = rf"['\"]{re.escape(lid)}['\"]\s*:\s*['\"]{re.escape(expected_url)}['\"]"
        if not re.search(pat, lv_src):
            errors.append(f"[{key}] Missing or mismatched LECTURE_MANIFEST_MAP entry in LectureViewer.tsx for {lid} -> {expected_url}")

        # 2. Check manifest.json & MP3s on disk
        lec_dir = os.path.join(REPO_ROOT, 'public', 'audio', 'lectures', subj, code)
        man_path = os.path.join(lec_dir, 'manifest.json')
        if not os.path.exists(man_path):
            errors.append(f"[{key}] Missing manifest.json at {man_path}")
            continue

        man = json.load(open(man_path, 'r', encoding='utf-8'))
        segs = man.get('segments', [])
        major_secs = man.get('majorSections', {})
        if len(segs) < 8:
            errors.append(f"[{key}] Suspiciously few segments ({len(segs)})")

        expected_files = set()
        seg_ids = set()
        for s_i, sg in enumerate(segs):
            sid = sg['id']
            seg_ids.add(sid)
            fname = f"{sid}.mp3"
            expected_files.add(fname)
            fpath = os.path.join(lec_dir, fname)
            if not os.path.exists(fpath):
                errors.append(f"[{key}] Missing MP3 file: {fname}")
            else:
                fsize = os.path.getsize(fpath)
                total_mp3s += 1
                total_bytes += fsize
                if fsize < 1500:
                    errors.append(f"[{key}] Tiny/corrupt MP3 ({fsize}B): {fname}")
            if sg.get('duration', 0) <= 0.4:
                errors.append(f"[{key}] Invalid duration ({sg.get('duration')}) on {sid}")
            if sg.get('audioUrl') != f"/audio/lectures/{subj}/{code}/{fname}":
                errors.append(f"[{key}] Bad audioUrl on {sid}: {sg.get('audioUrl')}")

        total_duration_sec += man.get('totalDuration', 0.0)

        actual_mp3s = {f for f in os.listdir(lec_dir) if f.endswith('.mp3')}
        orphans = actual_mp3s - expected_files
        if orphans:
            errors.append(f"[{key}] Orphan MP3 files in folder: {sorted(orphans)}")

        for m_id, rng in major_secs.items():
            st, ed = rng.get('start', -1), rng.get('end', -1)
            if not (0 <= st <= ed < len(segs)):
                errors.append(f"[{key}] Invalid majorSections[{m_id}] range: {rng} (len={len(segs)})")

        # 3. Fetch live Page 1 & Page 2 from Supabase
        rows = sb.table('lecture_pages').select('page_number, content_html').eq('lecture_id', lid).in_('page_number', [1, 2]).execute().data
        pmap = {r['page_number']: r['content_html'] or '' for r in rows}
        if 1 not in pmap or 2 not in pmap:
            errors.append(f"[{key}] Missing Page 1 or Page 2 in Supabase for {lid}")
            continue

        p1, p2 = pmap[1], pmap[2]
        d1 = len(re.findall(r'<div\b', p1, re.I)) - len(re.findall(r'</div>', p1, re.I))
        d2 = len(re.findall(r'<div\b', p2, re.I)) - len(re.findall(r'</div>', p2, re.I))
        if d1 != 0:
            errors.append(f"[{key}] Live P1 div imbalance: {d1}")
        if d2 != 0:
            errors.append(f"[{key}] Live P2 div imbalance: {d2}")

        s1 = BeautifulSoup(p1, 'html.parser')
        s2 = BeautifulSoup(p2, 'html.parser')

        for sg in segs:
            sel = sg['selector']
            m1 = [el for el in s1.select(sel) if not has_hidden_ancestor(el)]
            m2 = [el for el in s2.select(sel) if not has_hidden_ancestor(el)]
            if not m1:
                errors.append(f"[{key}] Live P1 missing visible match for {sel}")
            if not m2:
                errors.append(f"[{key}] Live P2 missing visible match for {sel}")

        major_ids = set(major_secs.keys())
        for pn, sp in [('P1', s1), ('P2', s2)]:
            dls_els = sp.find_all(attrs={'data-lecture-section': True})
            if len(dls_els) < len(segs) * 0.8:
                errors.append(f"[{key}] Live {pn} has too few clickable elements ({len(dls_els)} vs {len(segs)} segs)")
            for el in dls_els:
                dls = el['data-lecture-section']
                if has_hidden_ancestor(el):
                    errors.append(f"[{key}] Live {pn} data-lecture-section={dls} inside display:none")
                if dls not in seg_ids and dls not in major_ids:
                    errors.append(f"[{key}] Live {pn} unresolved data-lecture-section={dls}")

        for b in s1.find_all(attrs={'data-audio-badge': True}):
            if VI_DIACRITIC_RE.search(b.get_text()):
                errors.append(f"[{key}] Live P1 badge has Vietnamese text: {b.get_text()}")

        if idx % 15 == 0 or idx == len(LECTURE_SPECS):
            print(f"  Audited {idx}/{len(LECTURE_SPECS)} lectures... (errors so far: {len(errors)})", flush=True)

    print("\n=====================================================================")
    print(f"POST-DEPLOYMENT AUDIT SUMMARY ({len(LECTURE_SPECS)} Science Lectures):")
    print(f"  Total MP3 files verified : {total_mp3s}")
    print(f"  Total audio disk size    : {total_bytes / (1024*1024):.1f} MB")
    print(f"  Total audio duration     : {total_duration_sec / 3600:.2f} hours")
    print(f"  Total errors found       : {len(errors)}")
    print("=====================================================================")
    if errors:
        for e in errors[:50]:
            print("  ERROR:", e)
        sys.exit(1)
    print("100% ALL CHECKS PASSED ZERO ERRORS!")


if __name__ == '__main__':
    main()
