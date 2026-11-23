# -*- coding: utf-8 -*-
"""
Wrapper & QA Verifier for Digital SAT Math Adaptive Mock Test #8 (66 unique questions).
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
from sat_math_helpers import build_math_adaptive_mock_json
from sat_qa_validator import validate_sat_test
import sat_math_mock_08_m1 as m1
import sat_math_mock_08_m2h as m2h
import sat_math_mock_08_m2l as m2l


def get_mock_08():
    assert m1.verify_math()
    assert m2h.verify_math()
    assert m2l.verify_math()
    content_json = build_math_adaptive_mock_json(
        title='SAT Math Adaptive Mock Test #8 (Full 2-Module Bluebook)',
        subtitle='44 câu Adaptive (22 M1 + 22 M2 Hard/Standard) • 70 phút • Desmos + Reference Sheet + Thang 200–800',
        m1_qs=m1.get_m1_questions(),
        m2_hard_qs=m2h.get_m2h_questions(),
        m2_lower_qs=m2l.get_m2l_questions(),
        routing_threshold=15,
    )
    return (
        'math_mock_08',
        'SAT Math Adaptive Mock Test #8 (Full 2-Module Bluebook)',
        8,
        content_json,
    )


if __name__ == '__main__':
    key, title, order_idx, cj = get_mock_08()
    assert key == 'math_mock_08' and order_idx == 8
    errs = validate_sat_test(cj, title)
    if errs:
        print("ERRORS FOUND:")
        for e in errs:
            print("  -", e)
        sys.exit(1)

    expected_spr_nums = [5, 9, 13, 16, 19, 22]
    dollar_math_re = re.compile(r'\$(?![0-9])')
    for mk, id_prefix in (
        ('module1', 'sat_mm8_m1_q'),
        ('module2_hard', 'sat_mm8_m2h_q'),
        ('module2_lower', 'sat_mm8_m2l_q'),
    ):
        qs = cj[mk]['questions']
        assert len(qs) == 22, f"{mk}: expected 22 Qs, got {len(qs)}"
        mcqs = [q for q in qs if q.get('questionFormat', 'mcq') != 'spr']
        sprs = [q for q in qs if q.get('questionFormat') == 'spr']
        dist = {k: sum(1 for q in mcqs if q['correctAnswer'] == k) for k in 'ABCD'}
        assert dist == {'A': 4, 'B': 4, 'C': 4, 'D': 4}, f"{mk}: unbalanced MCQ keys {dist}"
        spr_nums = [q['number'] for q in sprs]
        assert spr_nums == expected_spr_nums, f"{mk}: SPR slots {spr_nums} != {expected_spr_nums}"
        for idx, q in enumerate(qs, start=1):
            assert q['id'] == f"{id_prefix}{idx}", f"{mk}: bad id {q['id']}"
            if idx <= 8:
                exp_dom = 'Algebra'
            elif idx <= 15:
                exp_dom = 'Advanced Math'
            elif idx <= 19:
                exp_dom = 'Problem-Solving and Data Analysis'
            else:
                exp_dom = 'Geometry and Trigonometry'
            assert q['domain'] == exp_dom, f"{mk} Q{idx}: {q['domain']} != {exp_dom}"
            exp = q['explanation']
            assert exp.get('desmosTipVi'), f"{mk} Q{idx}: missing desmosTipVi"
            assert exp.get('keyTakeaway'), f"{mk} Q{idx}: missing keyTakeaway"
            # Verify no $...$ LaTeX delimiters leaked
            fields = [q['stimulusHtml'], q['questionHtml'], exp['summaryVi'], exp['keyTakeaway'], exp['desmosTipVi']]
            fields += [o['text'] for o in q.get('options', [])]
            for fval in fields:
                assert not dollar_math_re.search(fval), f"{mk} Q{idx}: suspicious $ math in {fval[:80]}"
        print(f"  {mk}: {len(qs)} Qs ({len(mcqs)} MCQ {dist}, {len(sprs)} SPR @ {spr_nums})")
    print("MATH MOCK 08 (66 Qs) VERIFIED & QA PASSED!")
