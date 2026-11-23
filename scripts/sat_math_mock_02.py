# -*- coding: utf-8 -*-
"""
Digital SAT Math Full-Length Adaptive Mock Test #2 (Bluebook Official Format)
66 unique, 100% original questions:
  - Module 1 (Routing): 22 questions (16 MCQ + 6 SPR)
  - Module 2 Hard (650–800 Band): 22 questions (16 MCQ + 6 SPR)
  - Module 2 Standard/Lower (300–600 Band): 22 questions (16 MCQ + 6 SPR)
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))

from sat_math_helpers import build_math_adaptive_mock_json
from sat_math_mock_02_m1 import get_m1_questions, verify_math as verify_m1
from sat_math_mock_02_m2h import get_m2h_questions, verify_math as verify_m2h
from sat_math_mock_02_m2l import get_m2l_questions, verify_math as verify_m2l


def get_mock_02():
    title = 'SAT Math Adaptive Mock Test #2 (Full 2-Module Bluebook)'
    subtitle = (
        'Đề thi thử SAT Math thích ứng chuẩn Bluebook #2 '
        '(Module 1 Routing → Module 2 Hard/Standard, 44 câu / 70 phút, '
        'tích hợp Desmos & quy đổi thang điểm 200–800).'
    )
    content_json = build_math_adaptive_mock_json(
        title=title,
        subtitle=subtitle,
        m1_qs=get_m1_questions(),
        m2_hard_qs=get_m2h_questions(),
        m2_lower_qs=get_m2l_questions(),
        routing_threshold=15,
    )
    return ('math_mock_02', title, 2, content_json)


def _check_latex_and_strings(text, label):
    """Strict KaTeX delimiter, no-$ math, and control-character audit."""
    assert text is not None, f"{label}: None text"
    # Check accidental Python escape sequences like \f, \b, \a, \t, \r
    for ch, name in [('\x07', '\\a'), ('\x08', '\\b'), ('\x0c', '\\f'), ('\x0d', '\\r'), ('\t', '\\t')]:
        assert ch not in text, f"{label}: stray control character {name} found in {text!r}"
    # Check balanced \( ... \) and \[ ... \]
    assert text.count(r'\(') == text.count(r'\)'), f"{label}: unbalanced \\( \\) in {text!r}"
    assert text.count(r'\[') == text.count(r'\]'), f"{label}: unbalanced \\[ \\] in {text!r}"
    # Check no $$ display math and no $...$ LaTeX math (allow currency like $14, $1,586, $2.50)
    assert '$$' not in text, f"{label}: forbidden $$ delimiter found in {text!r}"
    # Look for $ followed by non-digit (like $x$) or $...$ enclosing variables/operators
    dollar_math = re.findall(r'\$[^0-9\s][^$]*\$', text)
    assert not dollar_math, f"{label}: forbidden $...$ math found: {dollar_math}"
    # Check no accidental double opening braces in LaTeX from f-strings (closing }} is valid in e.g. ^{\frac{t}{4}})
    assert '{{' not in text, f"{label}: accidental double opening brace found in {text!r}"


def run_strict_blueprint_audit(content_json):
    expected_domains = (
        ['Algebra'] * 8
        + ['Advanced Math'] * 7
        + ['Problem-Solving and Data Analysis'] * 4
        + ['Geometry and Trigonometry'] * 3
    )
    expected_spr_numbers = {5, 9, 13, 16, 19, 22}
    prefix_map = {
        'module1': 'sat_mm2_m1_q',
        'module2_hard': 'sat_mm2_m2h_q',
        'module2_lower': 'sat_mm2_m2l_q',
    }

    assert content_json['basicInfo']['routingThreshold'] == 15
    total_qs = 0
    seen_ids = set()

    for mod_key, id_prefix in prefix_map.items():
        qs = content_json[mod_key]['questions']
        assert len(qs) == 22, f"{mod_key}: expected 22 questions, got {len(qs)}"
        total_qs += len(qs)

        mcq_counts = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
        spr_nums = set()

        for i, q in enumerate(qs):
            num = i + 1
            expected_id = f"{id_prefix}{num}"
            assert q['id'] == expected_id, f"{mod_key} Q{num}: expected id {expected_id}, got {q['id']}"
            assert q['id'] not in seen_ids, f"Duplicate ID: {q['id']}"
            seen_ids.add(q['id'])
            assert q['number'] == num, f"{mod_key} Q{num}: bad number {q['number']}"
            assert q['domain'] == expected_domains[i], (
                f"{mod_key} Q{num}: expected domain {expected_domains[i]}, got {q['domain']}"
            )

            exp = q['explanation']
            assert exp.get('desmosTipVi', '').strip(), f"{mod_key} Q{num}: missing desmosTipVi"
            assert exp.get('keyTakeaway', '').strip(), f"{mod_key} Q{num}: missing keyTakeaway"

            _check_latex_and_strings(q['stimulusHtml'], f"{mod_key} Q{num} stimulusHtml")
            _check_latex_and_strings(q['questionHtml'], f"{mod_key} Q{num} questionHtml")
            _check_latex_and_strings(exp['summaryVi'], f"{mod_key} Q{num} summaryVi")
            _check_latex_and_strings(exp['desmosTipVi'], f"{mod_key} Q{num} desmosTipVi")
            _check_latex_and_strings(exp['keyTakeaway'], f"{mod_key} Q{num} keyTakeaway")

            if q['questionFormat'] == 'spr':
                spr_nums.add(num)
                assert q.get('correctDisplay'), f"{mod_key} Q{num}: missing correctDisplay"
                assert r'\(' not in q['correctDisplay'], f"{mod_key} Q{num}: correctDisplay should be plain text"
            else:
                assert q['questionFormat'] == 'mcq'
                mcq_counts[q['correctAnswer']] += 1
                for opt in q['options']:
                    _check_latex_and_strings(opt['text'], f"{mod_key} Q{num} opt {opt['label']}")
                for lbl in ('A', 'B', 'C', 'D'):
                    _check_latex_and_strings(
                        exp['optionAnalysis'][lbl]['reasonVi'],
                        f"{mod_key} Q{num} optionAnalysis[{lbl}]"
                    )

        assert spr_nums == expected_spr_numbers, f"{mod_key}: SPR positions {spr_nums} != {expected_spr_numbers}"
        assert mcq_counts == {'A': 4, 'B': 4, 'C': 4, 'D': 4}, f"{mod_key}: unbalanced MCQ keys {mcq_counts}"

    assert total_qs == 66, f"Expected 66 total questions, got {total_qs}"


if __name__ == '__main__':
    from sat_qa_validator import validate_sat_test

    assert verify_m1() is True
    assert verify_m2h() is True
    assert verify_m2l() is True

    key, title, order_idx, content_json = get_mock_02()
    assert key == 'math_mock_02'
    assert title == 'SAT Math Adaptive Mock Test #2 (Full 2-Module Bluebook)'
    assert order_idx == 2

    errors = validate_sat_test(content_json, title)
    if errors:
        for err in errors:
            print("QA ERROR:", err)
        sys.exit(1)

    run_strict_blueprint_audit(content_json)
    print("MATH MOCK 02 (66 Qs) VERIFIED & QA PASSED!")
