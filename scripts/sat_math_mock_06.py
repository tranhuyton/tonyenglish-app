# -*- coding: utf-8 -*-
"""
Wrapper & QA Verifier for Digital SAT Math Adaptive Mock Test #6 (66 unique questions).
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
from sat_math_helpers import build_math_adaptive_mock_json
from sat_qa_validator import validate_sat_test
import sat_math_mock_06_m1 as m1
import sat_math_mock_06_m2h as m2h
import sat_math_mock_06_m2l as m2l


def get_mock_06():
    assert m1.verify_math()
    assert m2h.verify_math()
    assert m2l.verify_math()
    content_json = build_math_adaptive_mock_json(
        title='SAT Math Adaptive Mock Test #6 (Full 2-Module Bluebook)',
        subtitle='44 câu Adaptive (22 M1 + 22 M2 Hard/Standard) • 70 phút • Desmos + Reference Sheet + Thang 200–800',
        m1_qs=m1.get_m1_questions(),
        m2_hard_qs=m2h.get_m2h_questions(),
        m2_lower_qs=m2l.get_m2l_questions(),
        routing_threshold=15,
    )
    return (
        'math_mock_06',
        'SAT Math Adaptive Mock Test #6 (Full 2-Module Bluebook)',
        6,
        content_json,
    )


def _check_strict_blueprint(cj):
    expected_domains = (
        ['Algebra'] * 8
        + ['Advanced Math'] * 7
        + ['Problem-Solving and Data Analysis'] * 4
        + ['Geometry and Trigonometry'] * 3
    )
    expected_spr_nums = [5, 9, 13, 16, 19, 22]
    id_prefixes = {
        'module1': 'sat_mm6_m1_q',
        'module2_hard': 'sat_mm6_m2h_q',
        'module2_lower': 'sat_mm6_m2l_q',
    }
    # Catch accidental LaTeX $...$ (non-currency: $ followed by letter, backslash, or opening paren/brace)
    bad_dollar_re = re.compile(r'\$[A-Za-z\\({]')

    for mk in ('module1', 'module2_hard', 'module2_lower'):
        qs = cj[mk]['questions']
        assert len(qs) == 22, f"{mk}: expected 22 Qs, got {len(qs)}"
        mcqs = [q for q in qs if q.get('questionFormat', 'mcq') != 'spr']
        sprs = [q for q in qs if q.get('questionFormat') == 'spr']
        assert len(mcqs) == 16, f"{mk}: expected 16 MCQ, got {len(mcqs)}"
        assert len(sprs) == 6, f"{mk}: expected 6 SPR, got {len(sprs)}"
        assert [q['number'] for q in sprs] == expected_spr_nums, f"{mk}: bad SPR positions {[q['number'] for q in sprs]}"

        dist = {k: sum(1 for q in mcqs if q['correctAnswer'] == k) for k in 'ABCD'}
        assert dist == {'A': 4, 'B': 4, 'C': 4, 'D': 4}, f"{mk}: imbalanced MCQ keys {dist}"

        psda_has_table = False
        geo_has_svg = False
        for i, q in enumerate(qs):
            assert q['id'] == f"{id_prefixes[mk]}{i+1}", f"{mk}: bad id {q['id']}"
            assert q['domain'] == expected_domains[i], f"{mk} Q{i+1}: domain {q['domain']} != {expected_domains[i]}"
            exp = q['explanation']
            assert exp.get('desmosTipVi') and len(exp['desmosTipVi'].strip()) >= 15, f"{mk} Q{i+1}: weak desmosTipVi"
            assert exp.get('keyTakeaway') and len(exp['keyTakeaway'].strip()) >= 15, f"{mk} Q{i+1}: weak keyTakeaway"
            if q['domain'] == 'Problem-Solving and Data Analysis' and '<table>' in q['stimulusHtml']:
                psda_has_table = True
            if q['domain'] == 'Geometry and Trigonometry' and '<svg ' in q['stimulusHtml']:
                geo_has_svg = True
            # Check no $...$ LaTeX in text fields
            texts = [q['stimulusHtml'], q['questionHtml'], exp['summaryVi'], exp['keyTakeaway'], exp['desmosTipVi']]
            for o in q.get('options', []):
                texts.append(o['text'])
            for oa in (exp.get('optionAnalysis') or {}).values():
                texts.append(oa['reasonVi'])
            for t in texts:
                assert not bad_dollar_re.search(t), f"{mk} Q{i+1}: suspicious $ math syntax in: {t[:120]}"

        assert psda_has_table, f"{mk}: PSDA missing HTML data table"
        assert geo_has_svg, f"{mk}: Geometry missing SVG diagram"
        print(f"  {mk}: {len(qs)} Qs ({len(mcqs)} MCQ {dist}, {len(sprs)} SPR)")


if __name__ == '__main__':
    key, title, order_idx, cj = get_mock_06()
    assert key == 'math_mock_06' and order_idx == 6
    assert cj['basicInfo']['routingThreshold'] == 15
    errs = validate_sat_test(cj, title)
    if errs:
        print("ERRORS FOUND:")
        for e in errs:
            print("  -", e)
        sys.exit(1)
    _check_strict_blueprint(cj)
    print("MATH MOCK 06 (66 Qs) VERIFIED & QA PASSED!")
