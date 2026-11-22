# -*- coding: utf-8 -*-
"""
Master QA, Deduplication Audit & Publisher for all 4 Full-Length Adaptive Mock Tests
(4 tests x 81 questions = 324 questions) to Supabase under `2. Full-Length Adaptive Mock Tests (Bluebook)`.
"""

import os
import sys
import re

sys.path.insert(0, os.path.dirname(__file__))

from sat_audio_pipeline import upsert_sat_drill, load_ids
from sat_qa_validator import validate_sat_test
from sat_mock_01 import get_mock_01
from sat_mock_02 import get_mock_02
from sat_mock_03 import get_mock_03
from sat_mock_04 import get_mock_04

def strip_tags(html):
    return re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', html or '')).strip().lower()

def audit_and_publish_mocks():
    mocks = [
        ('mock_01', 1, get_mock_01()),
        ('mock_02', 2, get_mock_02()),
        ('mock_03', 3, get_mock_03()),
        ('mock_04', 4, get_mock_04()),
    ]

    print("=== MASTER QA VALIDATION FOR ALL 4 ADAPTIVE MOCK TESTS (324 QUESTIONS) ===", flush=True)
    all_errors = []
    seen_ids = set()
    seen_stimuli = {}
    total_qs = 0

    for key, order_idx, data in mocks:
        title = data['basicInfo']['title']
        errs = validate_sat_test(data, title)
        if errs:
            all_errors.extend(errs)

        for mk in ('module1', 'module2_hard', 'module2_lower'):
            qs = data[mk]['questions']
            if len(qs) != 27:
                all_errors.append(f"[{key}:{mk}] Expected 27 questions, got {len(qs)}")
            dist = {c: sum(1 for q in qs if q['correctAnswer'] == c) for c in 'ABCD'}
            print(f"  [{key}:{mk}] {len(qs)} Qs | Keys: {dist}", flush=True)
            for q in qs:
                total_qs += 1
                if q['id'] in seen_ids:
                    all_errors.append(f"Duplicate global ID: {q['id']}")
                seen_ids.add(q['id'])
                sig = strip_tags(q['stimulusHtml'])[:120]
                if sig in seen_stimuli:
                    all_errors.append(f"Potential duplicate stimulus: {q['id']} vs {seen_stimuli[sig]}")
                seen_stimuli[sig] = q['id']

    if all_errors:
        print("\n[MASTER QA FAILED]:", flush=True)
        for e in all_errors:
            print("  -", e, flush=True)
        sys.exit(1)

    print(f"\n[MASTER QA PASSED] {total_qs} unique Adaptive Mock Test questions verified with 0 errors!", flush=True)

    print("\n=== UPLOADING ALL 4 ADAPTIVE MOCK TESTS TO SUPABASE ===", flush=True)
    for key, order_idx, data in mocks:
        upsert_sat_drill(key, data['basicInfo']['title'], order_idx, data, folder_key='rw_mocks')

    print("\nALL 4 ADAPTIVE MOCK TESTS PUBLISHED SUCCESSFULLY!", flush=True)

if __name__ == '__main__':
    audit_and_publish_mocks()
