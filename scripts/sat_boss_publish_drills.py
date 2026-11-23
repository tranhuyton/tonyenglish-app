# -*- coding: utf-8 -*-
"""
Validates, cross-deduplicates, and publishes all 8 Capstone Hard M2 Boss Drills
(4 R&W = 60 Elite Qs + 4 Math = 60 Elite Qs = 120 Qs total) to Supabase.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from sat_audio_pipeline import upsert_sat_drill
from sat_qa_validator import validate_sat_test

import sat_boss_rw_drills_1_2 as rw12
import sat_boss_rw_drills_3_4 as rw34
import sat_boss_math_drills_5_6 as math56
import sat_boss_math_drills_7_8 as math78

def main():
    print("=== 1. VERIFYING MATH & QA FOR ALL 8 HARD M2 BOSS DRILLS (120 ELITE Qs) ===", flush=True)
    math56.verify_all_math()
    math78.verify_all_math()

    all_drills = rw12.get_drills() + rw34.get_drills() + math56.get_drills() + math78.get_drills()
    assert len(all_drills) == 8, f"Expected 8 boss drills, got {len(all_drills)}"

    seen_ids = set()
    seen_stems = set()
    total_qs = 0
    for drill_key, title, order_idx, cj in all_drills:
        errs = validate_sat_test(cj, title)
        if errs:
            print(f"[QA FAILED] {title}:", flush=True)
            for e in errs:
                print("  -", e, flush=True)
            sys.exit(1)
        qs = cj['drillModule']['questions']
        assert len(qs) == 15, f"{drill_key} has {len(qs)} Qs, expected 15"
        for q in qs:
            assert q['id'] not in seen_ids, f"Duplicate Boss ID: {q['id']}"
            seen_ids.add(q['id'])
            sig = (q['stimulusHtml'].strip(), q['questionHtml'].strip())
            assert sig not in seen_stems, f"Duplicate Boss stem in {drill_key} Q{q['number']}"
            seen_stems.add(sig)
            total_qs += 1
        print(f"  [QA OK] {drill_key}: {len(qs)} Elite Qs", flush=True)

    print(f"\nAll 8 Hard M2 Boss Drills verified ({total_qs} unique Elite Qs). Publishing...", flush=True)
    for drill_key, title, order_idx, cj in all_drills:
        upsert_sat_drill(drill_key, title, order_idx, cj, folder_key='boss_drills')

    print(f"\n[DONE] Published all 8 Hard M2 Boss Drills ({total_qs} Elite 750–800 Qs)!", flush=True)

if __name__ == '__main__':
    main()
