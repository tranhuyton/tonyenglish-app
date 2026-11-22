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
from sat_m5_lectures import get_stage4_lectures
from sat_drills_5_1_to_5_3 import get_drill_5_1, get_drill_5_2, get_drill_5_3
from sat_drills_5_4_to_5_5 import get_drill_5_4, get_drill_5_5

async def main():
    drills = [
        ('drill_5_1', 12, get_drill_5_1()),
        ('drill_5_2', 13, get_drill_5_2()),
        ('drill_5_3', 14, get_drill_5_3()),
        ('drill_5_4', 15, get_drill_5_4()),
        ('drill_5_5', 16, get_drill_5_5()),
    ]

    print("=== STEP 1: QA VALIDATION OF ALL STAGE 4 DRILLS (65 QUESTIONS) ===", flush=True)
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
            print(f"  [PASS] {key}: {q_len} questions | Answer distribution: {dist}", flush=True)

    if all_errors:
        print("\n[QA FAILED] Fix errors before uploading:", flush=True)
        for e in all_errors:
            print("  -", e, flush=True)
        sys.exit(1)

    print("\n=== STEP 2: UPSERTING 5 HARD MODULE 2 DRILLS TO SUPABASE ===", flush=True)
    drill_id_map = {}
    for key, order_idx, data in drills:
        tid = upsert_sat_drill(key, data['basicInfo']['title'], order_idx, data, folder_key='rw_drills')
        drill_id_map[key] = (tid, data['basicInfo']['title'])

    print("\n=== STEP 3: UPSERTING 5 MODULE 5 LECTURES + GENERATING BILINGUAL AUDIO ===", flush=True)
    ids = load_ids()
    course_title = ids['course_title']
    lectures = get_stage4_lectures()
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

    print("\n=== STAGE 4 COMPLETE! MANIFEST ENTRIES ===", flush=True)
    for lid, murl, title in manifest_entries:
        print(f"  '{lid}': '{murl}', // {title}", flush=True)

if __name__ == '__main__':
    asyncio.run(main())
