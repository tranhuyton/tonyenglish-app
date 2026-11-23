# -*- coding: utf-8 -*-
"""
Publishes all 12 Digital SAT Math 1500+ Lectures (m1_1 .. m4_3) to Supabase
and generates all 48 bilingual audio segments (en-US-AndrewNeural + vi-VN-HoaiMyNeural)
under public/audio/lectures/sat_math/{code}/.
Also supports --link-drills-only mode to re-link task_list exercise UUIDs once drills are published.
"""

import os
import sys
import asyncio

sys.path.insert(0, os.path.dirname(__file__))
from sat_audio_pipeline import upsert_sat_lecture, generate_lecture_audio, load_ids
from sat_math_lectures_m1 import get_m1_lectures
from sat_math_lectures_m2 import get_m2_lectures
from sat_math_lectures_m3 import get_m3_lectures
from sat_math_lectures_m4 import get_m4_lectures

def get_all_math_lectures():
    return get_m1_lectures() + get_m2_lectures() + get_m3_lectures() + get_m4_lectures()

async def main():
    link_only = '--link-drills-only' in sys.argv
    lectures = get_all_math_lectures()
    ids = load_ids()
    math_drills = ids.get('math_drills', {})

    print(f"=== PUBLISHING {len(lectures)} DIGITAL SAT MATH 1500+ LECTURES (link_only={link_only}) ===", flush=True)
    manifest_entries = []

    for lec in lectures:
        code = lec['code']
        drill_key = lec['drill_key']
        drill_id = math_drills.get(drill_key)
        drill_title = f"Math Drill {code[1:].replace('_', '.')} (15 câu chuẩn Bluebook)" if drill_id else None

        # Verify every audio segment selector exists in HTML
        for seg in lec['segments']:
            sel_id = seg['selector'].lstrip('#')
            assert f'id="{sel_id}"' in lec['html'], f"Selector {seg['selector']} missing in {code} HTML!"

        lec_id = upsert_sat_lecture(
            lecture_code=code,
            module_key=lec['module_key'],
            title=lec['title'],
            order_index=lec['order_index'],
            html_content=lec['html'],
            drill_id=drill_id,
            drill_title=drill_title,
            extra_manual_task='Nghe trọn bài giảng song ngữ & ghi chú Công thức + Mẹo Desmos 800',
            id_bucket='math_lectures',
        )

        if not link_only:
            manifest_url = await generate_lecture_audio(
                lecture_code=code,
                lecture_id=lec_id,
                course_title='Digital SAT 1500+ (Math)',
                lecture_title=lec['title'],
                segments=lec['segments'],
                major_sections=lec['major_sections'],
                subject='sat_math',
            )
            manifest_entries.append((lec_id, manifest_url, lec['title']))

    if not link_only:
        print("\n=== LECTURE_MANIFEST_MAP ENTRIES (SAT MATH) ===", flush=True)
        for lid, murl, title in manifest_entries:
            print(f"  '{lid}': '{murl}', // {title}", flush=True)
    print("\n[DONE] All 12 SAT Math 1500+ lectures processed successfully!", flush=True)

if __name__ == '__main__':
    asyncio.run(main())
