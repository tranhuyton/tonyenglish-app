# -*- coding: utf-8 -*-
"""
End-to-end Live Supabase & Disk Integrity Audit for Digital SAT 1500+ (R&W Branch).
Verifies:
- Course, 5 Modules, 4 Folders
- 16 Published Lectures, 16 Lecture HTML pages, 16 task_list Drill links
- 16 Bilingual Audio Manifests + all referenced MP3 files on disk + LECTURE_MANIFEST_MAP registration
- 16 Skill Drills + 4 Adaptive Mock Tests (all validated by sat_qa_validator)
- 10 Elite Vocab Game Sets (500 words total)
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

    print(f"=== FULL AUDIT: Digital SAT 1500+ (Course ID: {course_id}) ===")

    # 1. Course & Modules
    mods = sb.table('lecture_modules').select('*').eq('course_id', course_id).order('order_index').execute().data
    print(f"Modules: {len(mods)}/5")
    if len(mods) != 5:
        errors.append(f"Expected 5 modules, got {len(mods)}")

    # 2. Folders
    folders = sb.table('folders').select('*').eq('course_id', course_id).execute().data
    print(f"Folders: {len(folders)}/4")
    if len(folders) != 4:
        errors.append(f"Expected 4 folders, got {len(folders)}")

    # 3. Lectures + HTML Pages + Audio Manifests + LectureViewer map
    lecs = sb.table('lectures').select('*').eq('course_id', course_id).execute().data
    print(f"Lectures: {len(lecs)}/16")
    if len(lecs) != 16:
        errors.append(f"Expected 16 lectures, got {len(lecs)}")

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

    for code, lid in (ids.get('lectures') or {}).items():
        mpath = os.path.join(ROOT_DIR, 'public', 'audio', 'lectures', 'sat_rw', code, 'manifest.json')
        if not os.path.exists(mpath):
            errors.append(f"Missing manifest.json for {code}")
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

    # 4. Tests (Drills, Adaptive Mocks, Vocab Games)
    tests = sb.table('tests').select('*').eq('course_id', course_id).execute().data
    drill_count = 0
    drill_q_count = 0
    mock_count = 0
    mock_q_count = 0
    game_count = 0
    vocab_word_count = 0

    for t in tests:
        cj = t['content_json']
        if isinstance(cj, str):
            cj = json.loads(cj)
        if t['test_type'] == 'SAT-Bluebook':
            errs = validate_sat_test(cj, t['title'])
            errors.extend(errs)
            if cj.get('mode') == 'drill':
                drill_count += 1
                drill_q_count += len(cj['drillModule']['questions'])
            elif cj.get('mode') == 'adaptive_mock':
                mock_count += 1
                mock_q_count += sum(len(cj[mk]['questions']) for mk in ('module1', 'module2_hard', 'module2_lower'))
        elif cj.get('basicInfo', {}).get('category') == 'game':
            game_count += 1
            for p in cj.get('parts') or []:
                for s in p.get('sections') or []:
                    vocab_word_count += len(s.get('questions') or [])

    print(f"Skill Drills: {drill_count}/16 ({drill_q_count} questions)")
    print(f"Adaptive Mock Tests: {mock_count}/4 ({mock_q_count} questions)")
    print(f"Vocab Games: {game_count}/10 ({vocab_word_count} words)")
    print(f"TOTAL SAT BLUEBOOK QUESTIONS: {drill_q_count + mock_q_count}")

    if drill_count != 16:
        errors.append(f"Expected 16 drills, got {drill_count}")
    if mock_count != 4:
        errors.append(f"Expected 4 adaptive mocks, got {mock_count}")
    if game_count != 10 or vocab_word_count != 500:
        errors.append(f"Expected 10 vocab games (500 words), got {game_count} ({vocab_word_count})")

    if errors:
        print("\n[AUDIT FAILED]:")
        for e in errors:
            print("  -", e)
        sys.exit(1)
    else:
        print("\n[AUDIT 100% PASSED] Digital SAT 1500+ (R&W) is production-ready!")

if __name__ == '__main__':
    main()
