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
from sat_m3_m4_lectures import get_stage3_lectures
from sat_drills_3_1_to_3_2 import get_drill_3_1, get_drill_3_2
from sat_drills_4_1_to_4_2 import get_drill_4_1, get_drill_4_2
from sat_drills_4_3_to_4_4 import get_drill_4_3, get_drill_4_4
from sat_vocab_500 import publish_all_vocab_games

async def main():
    drills = [
        ('drill_3_1', 6, get_drill_3_1()),
        ('drill_3_2', 7, get_drill_3_2()),
        ('drill_4_1', 8, get_drill_4_1()),
        ('drill_4_2', 9, get_drill_4_2()),
        ('drill_4_3', 10, get_drill_4_3()),
        ('drill_4_4', 11, get_drill_4_4()),
    ]

    print("=== STEP 1: QA VALIDATION OF ALL STAGE 3 DRILLS (84 QUESTIONS) ===", flush=True)
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

    print("\n=== STEP 2: UPSERTING 6 DRILLS TO SUPABASE ===", flush=True)
    drill_id_map = {}
    for key, order_idx, data in drills:
        tid = upsert_sat_drill(key, data['basicInfo']['title'], order_idx, data, folder_key='rw_drills')
        drill_id_map[key] = (tid, data['basicInfo']['title'])

    print("\n=== STEP 3: PUBLISHING 500 ELITE SAT VOCAB WORDS (10 GAME SETS) ===", flush=True)
    publish_all_vocab_games()

    print("\n=== STEP 4: UPSERTING 6 LECTURES + GENERATING BILINGUAL AUDIO ===", flush=True)
    ids = load_ids()
    course_title = ids['course_title']
    lectures = get_stage3_lectures()
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

    print("\n=== STAGE 3 COMPLETE! MANIFEST ENTRIES ===", flush=True)
    for lid, murl, title in manifest_entries:
        print(f"  '{lid}': '{murl}', // {title}", flush=True)

if __name__ == '__main__':
    asyncio.run(main())
