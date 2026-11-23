# -*- coding: utf-8 -*-
"""
Publishes all 8 Capstone Hard M2 Boss Masterclass Lectures (b1..b8: 4 R&W + 4 Math)
to Supabase and generates all 32 bilingual audio segments (en-US-AndrewNeural + vi-VN-HoaiMyNeural)
under public/audio/lectures/sat_boss/{code}/.
Supports --link-drills-only mode once the 8 Boss Drills are published.
"""

import os
import sys
import asyncio

sys.path.insert(0, os.path.dirname(__file__))
from sat_audio_pipeline import upsert_sat_lecture, generate_lecture_audio, load_ids
from sat_boss_lectures_rw import get_boss_rw_lectures
from sat_boss_lectures_math import get_boss_math_lectures

def get_all_boss_lectures():
    return get_boss_rw_lectures() + get_boss_math_lectures()

async def main():
    link_only = '--link-drills-only' in sys.argv
    lectures = get_all_boss_lectures()
    ids = load_ids()
    boss_drills = ids.get('boss_drills', {})

    print(f"=== PUBLISHING {len(lectures)} HARD M2 BOSS MASTERCLASS LECTURES (link_only={link_only}) ===", flush=True)
    manifest_entries = []

    for lec in lectures:
        code = lec['code']
        drill_key = lec['drill_key']
        drill_id = boss_drills.get(drill_key)
        idx_num = lec['order_index']
        branch_lbl = 'R&W' if idx_num <= 4 else 'Math'
        drill_title = f"🔥 {branch_lbl} Boss Drill {idx_num} (15 câu Hard/Elite 750–800)" if drill_id else None

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
            extra_manual_task='Nghe trọn Masterclass song ngữ & ghi chú chiến thuật phá bẫy Hard M2 (750–800)',
            id_bucket='boss_lectures',
        )

        if not link_only:
            manifest_url = await generate_lecture_audio(
                lecture_code=code,
                lecture_id=lec_id,
                course_title='Digital SAT 1500+ (Hard M2 Boss Masterclass)',
                lecture_title=lec['title'],
                segments=lec['segments'],
                major_sections=lec['major_sections'],
                subject='sat_boss',
            )
            manifest_entries.append((lec_id, manifest_url, lec['title']))

    if not link_only:
        print("\n=== LECTURE_MANIFEST_MAP ENTRIES (SAT BOSS MASTERCLASS) ===", flush=True)
        for lid, murl, title in manifest_entries:
            print(f"  '{lid}': '{murl}', // {title}", flush=True)
    print("\n[DONE] All 8 Hard M2 Boss Masterclass lectures processed successfully!", flush=True)

if __name__ == '__main__':
    asyncio.run(main())
