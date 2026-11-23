# -*- coding: utf-8 -*-
"""
Wave 2 Mock Test Publisher & Global Deduplication Auditor:
- Cross-checks ALL 8 R&W Adaptive Mocks (#1..#8 = 648 Qs) for 0 duplicate IDs / stems
- Cross-checks ALL 8 Math Adaptive Mocks (#1..#8 = 528 Qs) for 0 duplicate IDs / stems + Python math assertions
- Publishes R&W Mocks #5..#8 (folder_key='rw_mocks', order 5..8)
- Publishes Math Mocks #5..#8 (folder_key='math_mocks', order 5..8)
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from sat_audio_pipeline import upsert_sat_drill
from sat_qa_validator import validate_sat_test

# R&W Mocks 1..8
from sat_mock_01 import get_mock_01 as get_rw_01
from sat_mock_02 import get_mock_02 as get_rw_02
from sat_mock_03 import get_mock_03 as get_rw_03
from sat_mock_04 import get_mock_04 as get_rw_04
from sat_mock_05 import get_mock_05 as get_rw_05
from sat_mock_06 import get_mock_06 as get_rw_06
from sat_mock_07 import get_mock_07 as get_rw_07
from sat_mock_08 import get_mock_08 as get_rw_08

# Math Mocks 1..8
from sat_math_mock_01 import get_mock_01 as get_math_01
from sat_math_mock_02 import get_mock_02 as get_math_02
from sat_math_mock_03 import get_mock_03 as get_math_03
from sat_math_mock_04 import get_mock_04 as get_math_04
from sat_math_mock_05 import get_mock_05 as get_math_05
from sat_math_mock_06 import get_mock_06 as get_math_06
from sat_math_mock_07 import get_mock_07 as get_math_07
from sat_math_mock_08 import get_mock_08 as get_math_08

def main():
    print("=== 1. CROSS-AUDITING ALL 8 R&W ADAPTIVE MOCKS (#1..#8) ===", flush=True)
    rw_all = [
        ('mock_01', 1, get_rw_01()),
        ('mock_02', 2, get_rw_02()),
        ('mock_03', 3, get_rw_03()),
        ('mock_04', 4, get_rw_04()),
        ('mock_05', 5, get_rw_05()),
        ('mock_06', 6, get_rw_06()),
        ('mock_07', 7, get_rw_07()),
        ('mock_08', 8, get_rw_08()),
    ]
    rw_ids = set()
    rw_stems = set()
    rw_total = 0
    for key, order_idx, cj in rw_all:
        title = cj['basicInfo']['title']
        errs = validate_sat_test(cj, title)
        if errs:
            print(f"[QA FAILED] {key}: {errs[:10]}", flush=True)
            sys.exit(1)
        for mk in ('module1', 'module2_hard', 'module2_lower'):
            qs = cj[mk]['questions']
            assert len(qs) == 27, f"{key}:{mk} has {len(qs)} Qs, expected 27"
            for q in qs:
                assert q['id'] not in rw_ids, f"Duplicate R&W ID: {q['id']}"
                rw_ids.add(q['id'])
                sig = (q['stimulusHtml'].strip(), q['questionHtml'].strip())
                assert sig not in rw_stems, f"Duplicate R&W stimulus/stem in {key}:{mk} Q{q['number']}"
                rw_stems.add(sig)
                rw_total += 1
        print(f"  [OK] {key}: 81 unique Qs verified", flush=True)
    print(f"Total R&W Mock Qs verified: {rw_total}/648 (0 duplicates)", flush=True)

    print("\n=== 2. CROSS-AUDITING ALL 8 MATH ADAPTIVE MOCKS (#1..#8) ===", flush=True)
    math_all = [
        get_math_01(),
        get_math_02(),
        get_math_03(),
        get_math_04(),
        get_math_05(),
        get_math_06(),
        get_math_07(),
        get_math_08(),
    ]
    math_ids = set()
    math_stems = set()
    math_total = 0
    for key, title, order_idx, cj in math_all:
        errs = validate_sat_test(cj, title)
        if errs:
            print(f"[QA FAILED] {key}: {errs[:10]}", flush=True)
            sys.exit(1)
        for mk in ('module1', 'module2_hard', 'module2_lower'):
            qs = cj[mk]['questions']
            assert len(qs) == 22, f"{key}:{mk} has {len(qs)} Qs, expected 22"
            for q in qs:
                assert q['id'] not in math_ids, f"Duplicate Math ID: {q['id']}"
                math_ids.add(q['id'])
                sig = (q['stimulusHtml'].strip(), q['questionHtml'].strip())
                assert sig not in math_stems, f"Duplicate Math stimulus/stem in {key}:{mk} Q{q['number']}"
                math_stems.add(sig)
                math_total += 1
        print(f"  [OK] {key}: 66 unique Qs verified", flush=True)
    print(f"Total Math Mock Qs verified: {math_total}/528 (0 duplicates)", flush=True)

    print("\n=== 3. PUBLISHING WAVE 2 R&W MOCKS (#5..#8) TO SUPABASE ===", flush=True)
    for key, order_idx, cj in rw_all[4:]:
        upsert_sat_drill(key, cj['basicInfo']['title'], order_idx, cj, folder_key='rw_mocks')

    print("\n=== 4. PUBLISHING WAVE 2 MATH MOCKS (#5..#8) TO SUPABASE ===", flush=True)
    for key, title, order_idx, cj in math_all[4:]:
        upsert_sat_drill(key, title, order_idx, cj, folder_key='math_mocks')

    print("\n[DONE] Wave 2 Adaptive Mock Tests (#5..#8 for R&W + Math = 588 new Qs) published cleanly!", flush=True)

if __name__ == '__main__':
    main()
