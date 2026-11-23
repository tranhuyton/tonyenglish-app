# -*- coding: utf-8 -*-
"""
Validates, cross-deduplicates, and publishes all 4 Full-Length Adaptive Math Mock Tests
(4 x 66 = 264 unique Bluebook Math questions) to Supabase.
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from sat_audio_pipeline import upsert_sat_drill
from sat_qa_validator import validate_sat_test

from sat_math_mock_01 import get_mock_01
from sat_math_mock_02 import get_mock_02
from sat_math_mock_03 import get_mock_03
from sat_math_mock_04 import get_mock_04

def main():
    mocks = [get_mock_01(), get_mock_02(), get_mock_03(), get_mock_04()]
    seen_ids = set()
    seen_stems = set()
    total_qs = 0

    print("=== VALIDATING ALL 4 ADAPTIVE MATH MOCK TESTS (264 Qs) ===", flush=True)
    for mkey, title, order_idx, cj in mocks:
        errs = validate_sat_test(cj, title)
        if errs:
            print(f"[QA FAILED] {title}:", flush=True)
            for e in errs:
                print("  -", e, flush=True)
            sys.exit(1)

        m_total = 0
        for mk in ('module1', 'module2_hard', 'module2_lower'):
            qs = cj[mk]['questions']
            assert len(qs) == 22, f"{mkey}:{mk} has {len(qs)} Qs, expected 22"
            m_total += len(qs)
            for q in qs:
                assert q['id'] not in seen_ids, f"Duplicate ID: {q['id']}"
                seen_ids.add(q['id'])
                sig = (q['stimulusHtml'].strip(), q['questionHtml'].strip())
                assert sig not in seen_stems, f"Duplicate question content in {mkey}:{mk} Q{q['number']}"
                seen_stems.add(sig)
        total_qs += m_total
        print(f"  [QA OK] {mkey}: {m_total} unique Qs", flush=True)

    print(f"\nAll 4 Adaptive Math Mocks verified ({total_qs} unique Qs, 0 duplicates). Publishing...", flush=True)
    for mkey, title, order_idx, cj in mocks:
        upsert_sat_drill(mkey, title, order_idx, cj, folder_key='math_mocks')

    print(f"\n[DONE] All 4 Adaptive Math Mock Tests ({total_qs} Qs) published to Supabase!", flush=True)

if __name__ == '__main__':
    main()
