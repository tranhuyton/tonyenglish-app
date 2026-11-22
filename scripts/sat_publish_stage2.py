import os
import sys
import asyncio

sys.path.insert(0, os.path.dirname(__file__))

from sat_audio_pipeline import (
    load_ids,
    upsert_sat_drill,
    upsert_sat_lecture,
    generate_lecture_audio,
)
from sat_qa_validator import validate_sat_test
from sat_m1_m2_lectures import get_stage2_lectures
from sat_drills_1_1_and_2_1 import get_drill_1_1, get_drill_2_1
from sat_drills_2_2_to_2_4 import get_drill_2_2, get_drill_2_3, get_drill_2_4

async def main():
    drills = [
        ('drill_1_1', 1, get_drill_1_1()),
        ('drill_2_1', 2, get_drill_2_1()),
        ('drill_2_2', 3, get_drill_2_2()),
        ('drill_2_3', 4, get_drill_2_3()),
        ('drill_2_4', 5, get_drill_2_4()),
    ]

    print("=== STEP 1: QA VALIDATION OF ALL STAGE 2 DRILLS (72 QUESTIONS) ===")
    all_errors = []
    for key, order_idx, data in drills:
        errs = validate_sat_test(data, data['basicInfo']['title'])
        if errs:
            all_errors.extend(errs)
        else:
            q_len = len(data['drillModule']['questions'])
            dist = {}
            for q in data['drillModule']['questions']:
                dist[q['correctAnswer']] = dist.get(q['correctAnswer'], 0) + 1
            print(f"  [PASS] {key}: {q_len} questions | Answer distribution: {dist}")

    if all_errors:
        print("\n[QA FAILED] Fix errors before uploading:")
        for e in all_errors:
            print("  -", e)
        sys.exit(1)

    print("\n=== STEP 2: UPSERTING 5 DRILLS TO SUPABASE ===")
    drill_id_map = {}
    for key, order_idx, data in drills:
        tid = upsert_sat_drill(key, data['basicInfo']['title'], order_idx, data, folder_key='rw_drills')
        drill_id_map[key] = (tid, data['basicInfo']['title'])

    print("\n=== STEP 3: UPSERTING 5 LECTURES + LINKING TASK_LIST + GENERATING BILINGUAL AUDIO ===")
    ids = load_ids()
    course_title = ids['course_title']
    lectures = get_stage2_lectures()
    manifest_entries = []

    for lec in lectures:
        d_id, d_title = drill_id_map[lec['drill_key']]
        lec_id = upsert_sat_lecture(
            lecture_code=lec['code'],
            module_key=lec['module_key'],
            title=lec['title'],
            order_index=lec['order_index'],
            html_content=lec['html'],
            drill_id=d_id,
            drill_title=d_title,
        )
        manifest_url = await generate_lecture_audio(
            lecture_code=lec['code'],
            lecture_id=lec_id,
            course_title=course_title,
            lecture_title=lec['title'],
            segments=lec['segments'],
            major_sections=lec['major_sections'],
        )
        manifest_entries.append((lec_id, manifest_url, lec['title']))

    print("\n=== STAGE 2 COMPLETE! ADD THESE TO LECTURE_MANIFEST_MAP ===")
    for lid, murl, title in manifest_entries:
        print(f"  '{lid}': '{murl}', // {title}")

if __name__ == '__main__':
    asyncio.run(main())
