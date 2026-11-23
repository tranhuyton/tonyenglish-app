# -*- coding: utf-8 -*-
"""
Wrapper & QA Verifier for Digital SAT Math Adaptive Mock Test #7 (66 unique questions).
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from sat_math_helpers import build_math_adaptive_mock_json
from sat_qa_validator import validate_sat_test
import sat_math_mock_07_m1 as m1
import sat_math_mock_07_m2h as m2h
import sat_math_mock_07_m2l as m2l


def get_mock_07():
    m1.verify_math()
    m2h.verify_math()
    m2l.verify_math()
    content_json = build_math_adaptive_mock_json(
        title='SAT Math Adaptive Mock Test #7 (Full 2-Module Bluebook)',
        subtitle='44 câu Adaptive (22 M1 + 22 M2 Hard/Standard) • 70 phút • Desmos + Reference Sheet + Thang 200–800',
        m1_qs=m1.get_m1_questions(),
        m2_hard_qs=m2h.get_m2h_questions(),
        m2_lower_qs=m2l.get_m2l_questions(),
        routing_threshold=15,
    )
    return (
        'math_mock_07',
        'SAT Math Adaptive Mock Test #7 (Full 2-Module Bluebook)',
        7,
        content_json,
    )


if __name__ == '__main__':
    key, title, order_idx, cj = get_mock_07()
    errs = validate_sat_test(cj, title)
    if errs:
        print("ERRORS FOUND:")
        for e in errs:
            print("  -", e)
        sys.exit(1)

    expected_domains = (
        ['Algebra'] * 8
        + ['Advanced Math'] * 7
        + ['Problem-Solving and Data Analysis'] * 4
        + ['Geometry and Trigonometry'] * 3
    )
    expected_spr_nums = [5, 9, 13, 16, 19, 22]

    for mk, prefix in (
        ('module1', 'sat_mm7_m1_q'),
        ('module2_hard', 'sat_mm7_m2h_q'),
        ('module2_lower', 'sat_mm7_m2l_q'),
    ):
        qs = cj[mk]['questions']
        assert len(qs) == 22, f"{mk} expected 22 Qs, got {len(qs)}"
        assert [q['id'] for q in qs] == [f"{prefix}{i}" for i in range(1, 23)], f"{mk} ID mismatch"
        assert [q['domain'] for q in qs] == expected_domains, f"{mk} domain mismatch"
        mcqs = [q for q in qs if q.get('questionFormat', 'mcq') != 'spr']
        sprs = [q for q in qs if q.get('questionFormat') == 'spr']
        assert [q['number'] for q in sprs] == expected_spr_nums, f"{mk} SPR positions mismatch"
        dist = {k: sum(1 for q in mcqs if q['correctAnswer'] == k) for k in 'ABCD'}
        assert dist == {'A': 4, 'B': 4, 'C': 4, 'D': 4}, f"{mk} imbalanced MCQ keys: {dist}"
        for q in qs:
            exp = q['explanation']
            assert exp.get('desmosTipVi') and len(exp['desmosTipVi']) >= 15, f"{q['id']} missing desmosTipVi"
            assert exp.get('keyTakeaway') and len(exp['keyTakeaway']) >= 15, f"{q['id']} missing keyTakeaway"
            if q['questionFormat'] == 'spr':
                assert q.get('correctDisplay'), f"{q['id']} missing correctDisplay"
        print(f"  {mk}: {len(qs)} Qs ({len(mcqs)} MCQ {dist}, {len(sprs)} SPR)")

    print("MATH MOCK 07 (66 Qs) VERIFIED & QA PASSED!")
