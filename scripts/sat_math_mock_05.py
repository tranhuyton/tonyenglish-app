# -*- coding: utf-8 -*-
"""
Wrapper & QA Verifier for Digital SAT Math Adaptive Mock Test #5 (66 unique questions).
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from sat_math_helpers import build_math_adaptive_mock_json
from sat_qa_validator import validate_sat_test
import sat_math_mock_05_m1 as m1
import sat_math_mock_05_m2h as m2h
import sat_math_mock_05_m2l as m2l

def get_mock_05():
    m1.verify_math()
    m2h.verify_math()
    m2l.verify_math()
    content_json = build_math_adaptive_mock_json(
        title='SAT Math Adaptive Mock Test #5 (Full 2-Module Bluebook)',
        subtitle='44 câu Adaptive (22 M1 + 22 M2 Hard/Standard) • 70 phút • Desmos + Reference Sheet + Thang 200–800',
        m1_qs=m1.get_m1_questions(),
        m2_hard_qs=m2h.get_m2h_questions(),
        m2_lower_qs=m2l.get_m2l_questions(),
        routing_threshold=15,
    )
    return (
        'math_mock_05',
        'SAT Math Adaptive Mock Test #5 (Full 2-Module Bluebook)',
        5,
        content_json,
    )

if __name__ == '__main__':
    key, title, order_idx, cj = get_mock_05()
    errs = validate_sat_test(cj, title)
    if errs:
        print("ERRORS FOUND:")
        for e in errs:
            print("  -", e)
        sys.exit(1)
    for mk in ('module1', 'module2_hard', 'module2_lower'):
        qs = cj[mk]['questions']
        mcqs = [q for q in qs if q.get('questionFormat', 'mcq') != 'spr']
        sprs = [q for q in qs if q.get('questionFormat') == 'spr']
        dist = {k: sum(1 for q in mcqs if q['correctAnswer'] == k) for k in 'ABCD'}
        print(f"  {mk}: {len(qs)} Qs ({len(mcqs)} MCQ {dist}, {len(sprs)} SPR)")
    print("MATH MOCK 05 (66 Qs) VERIFIED & QA PASSED!")
