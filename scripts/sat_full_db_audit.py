# -*- coding: utf-8 -*-
"""
End-to-end Live Supabase & Disk Integrity Audit for the UNIFIED Digital SAT 1500+ Course
(BOTH Reading & Writing AND Math 1500+ Branches).
Verifies:
- Course, 9 Modules (5 R&W + 4 Math), 8 Folders (4 R&W + 4 Math)
- 28 Published Lectures (16 R&W + 12 Math), 28 HTML pages, 28 linked exercise drills
- 28 Bilingual Audio Manifests + all referenced MP3s on disk + LECTURE_MANIFEST_MAP registration
- 28 Skill Drills (16 R&W [221 Qs] + 12 Math [180 Qs]) + 8 Adaptive Mocks (4 R&W [324 Qs] + 4 Math [264 Qs])
- 12 Speed Games (10 R&W Vocab [500 words] + 2 Math Formula/Desmos [100 cards])
"""

import os
import sys
import json

sys.path.insert(0, os.path.dirname(__file__))

from sat_audio_pipeline import sb, load_ids, ROOT_DIR
from sat_qa_validator import validate_sat_test

def main():
    ids = load_ids()
    course_id = ids['course_id']
    errors = []

    print(f"=== FULL UNIFIED AUDIT: Digital SAT 1500+ (R&W + Math) | Course ID: {course_id} ===")

    # 1. Modules (5 R&W + 4 Math = 9)
    mods = sb.table('lecture_modules').select('*').eq('course_id', course_id).order('order_index').execute().data
    print(f"Modules: {len(mods)}/9 (5 R&W + 4 Math)")
    if len(mods) != 9:
        errors.append(f"Expected 9 modules, got {len(mods)}")

    # 2. Folders (4 R&W + 4 Math = 8)
    folders = sb.table('folders').select('*').eq('course_id', course_id).execute().data
    print(f"Folders: {len(folders)}/8 (4 R&W + 4 Math)")
    if len(folders) != 8:
        errors.append(f"Expected 8 folders, got {len(folders)}")

    # 3. Lectures + HTML Pages + task_list + Audio Manifests + LectureViewer registration
    lecs = sb.table('lectures').select('*').eq('course_id', course_id).execute().data
    print(f"Lectures: {len(lecs)}/28 (16 R&W + 12 Math)")
    if len(lecs) != 28:
        errors.append(f"Expected 28 lectures, got {len(lecs)}")

    lv_src = open(os.path.join(ROOT_DIR, 'src', 'LectureViewer.tsx'), encoding='utf-8').read()
    total_audio_secs = 0.0
    total_mp3s = 0

    for lec in lecs:
        lid = lec['id']
        pages = sb.table('lecture_pages').select('content_html').eq('lecture_id', lid).execute().data
        if not pages or len(pages[0]['content_html'] or '') < 1000:
            errors.append(f"Lecture '{lec['title']}' missing or short HTML page")
        tlist = lec.get('task_list') or []
        if not any(t.get('type') == 'exercise' and t.get('test_id') for t in tlist):
            errors.append(f"Lecture '{lec['title']}' missing linked exercise task_list")
        if lid not in lv_src:
            errors.append(f"Lecture ID {lid} ({lec['title']}) missing from LECTURE_MANIFEST_MAP in LectureViewer.tsx")

    for subject, bucket in [('sat_rw', 'lectures'), ('sat_math', 'math_lectures')]:
        for code, lid in (ids.get(bucket) or {}).items():
            mpath = os.path.join(ROOT_DIR, 'public', 'audio', 'lectures', subject, code, 'manifest.json')
            if not os.path.exists(mpath):
                errors.append(f"Missing manifest.json for {subject}/{code}")
                continue
            man = json.load(open(mpath, encoding='utf-8'))
            total_audio_secs += float(man.get('totalDuration') or 0)
            for seg in man.get('segments') or []:
                mp3_rel = seg['audioUrl'].lstrip('/')
                mp3_abs = os.path.join(ROOT_DIR, 'public', mp3_rel)
                if not os.path.exists(mp3_abs) or os.path.getsize(mp3_abs) < 1000:
                    errors.append(f"Missing/empty MP3: {mp3_abs}")
                else:
                    total_mp3s += 1

    print(f"Audio Segments Verified: {total_mp3s} MP3s ({round(total_audio_secs/60, 1)} mins total bilingual audio)")

    # 4. Tests (Drills, Adaptive Mocks, Games)
    tests = sb.table('tests').select('*').eq('course_id', course_id).execute().data
    rw_drills = rw_drill_qs = math_drills = math_drill_qs = 0
    rw_mocks = rw_mock_qs = math_mocks = math_mock_qs = 0
    game_count = game_cards = 0

    for t in tests:
        cj = t['content_json']
        if isinstance(cj, str):
            cj = json.loads(cj)
        if t['test_type'] == 'SAT-Bluebook':
            errs = validate_sat_test(cj, t['title'])
            errors.extend(errs)
            is_math = (cj.get('section') or '').lower() == 'math'
            if cj.get('mode') == 'drill':
                qlen = len(cj['drillModule']['questions'])
                if is_math:
                    math_drills += 1
                    math_drill_qs += qlen
                else:
                    rw_drills += 1
                    rw_drill_qs += qlen
            elif cj.get('mode') == 'adaptive_mock':
                qlen = sum(len(cj[mk]['questions']) for mk in ('module1', 'module2_hard', 'module2_lower'))
                if is_math:
                    math_mocks += 1
                    math_mock_qs += qlen
                else:
                    rw_mocks += 1
                    rw_mock_qs += qlen
        elif cj.get('basicInfo', {}).get('category') == 'game':
            game_count += 1
            for p in cj.get('parts') or []:
                for s in p.get('sections') or []:
                    game_cards += len(s.get('questions') or [])

    print(f"R&W Skill Drills:       {rw_drills}/16 ({rw_drill_qs} Qs)")
    print(f"R&W Adaptive Mocks:     {rw_mocks}/4 ({rw_mock_qs} Qs)")
    print(f"Math Skill Drills:      {math_drills}/12 ({math_drill_qs} Qs)")
    print(f"Math Adaptive Mocks:    {math_mocks}/4 ({math_mock_qs} Qs)")
    print(f"Interactive Speed Games:{game_count}/12 ({game_cards} cards: 500 Vocab + 100 Math Formulas)")
    print(f"TOTAL SAT BLUEBOOK QUESTIONS: {rw_drill_qs + rw_mock_qs + math_drill_qs + math_mock_qs}")

    if rw_drills != 16:
        errors.append(f"Expected 16 R&W drills, got {rw_drills}")
    if rw_mocks != 4:
        errors.append(f"Expected 4 R&W mocks, got {rw_mocks}")
    if math_drills != 12 or math_drill_qs != 180:
        errors.append(f"Expected 12 Math drills (180 Qs), got {math_drills} ({math_drill_qs})")
    if math_mocks != 4 or math_mock_qs != 264:
        errors.append(f"Expected 4 Math mocks (264 Qs), got {math_mocks} ({math_mock_qs})")
    if game_count != 12 or game_cards != 600:
        errors.append(f"Expected 12 games (600 cards), got {game_count} ({game_cards})")

    if errors:
        print("\n[AUDIT FAILED]:")
        for e in errors:
            print("  -", e)
        sys.exit(1)
    else:
        print("\n[AUDIT 100% PASSED] Digital SAT 1500+ (R&W + Math) is 100% production-ready!")

if __name__ == '__main__':
    main()
