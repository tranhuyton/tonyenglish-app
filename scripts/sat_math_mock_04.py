# -*- coding: utf-8 -*-
"""
Digital SAT Math Full-Length Adaptive Mock Test #4 (Bluebook Official Format)
Combines:
  - Module 1 (22 Qs, Routing Threshold: 15/22)
  - Module 2 Hard (22 Qs, 650–800 Band)
  - Module 2 Standard/Lower (22 Qs, 300–600 Band)
Total: 66 unique, 100% original, programmatically verified questions.
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))

from sat_math_helpers import build_math_adaptive_mock_json
from sat_math_mock_04_m1 import get_m1_questions, verify_math as verify_m1
from sat_math_mock_04_m2h import get_m2h_questions, verify_math as verify_m2h
from sat_math_mock_04_m2l import get_m2l_questions, verify_math as verify_m2l


def get_mock_04():
    title = 'SAT Math Adaptive Mock Test #4 (Full 2-Module Bluebook)'
    subtitle = (
        'Đề thi thử thích ứng chuẩn Bluebook #4 — Toán học '
        '(Module 1 Routing → Adaptive Module 2 Hard/Standard, 44 câu / 70 phút, '
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
    return ('math_mock_04', title, 4, content_json)


def _check_text_hygiene(text, label):
    # Ensure no accidental Python escape control chars (\a, \b, \f, \r, \t, \v)
    for ch in text:
        code = ord(ch)
        if code < 32 and ch not in ('\n',):
            raise AssertionError(f"{label}: Unexpected control char U+{code:04X} in {text[:80]!r}")
    # Ensure balanced \( ... \) and \[ ... \]
    assert text.count(r'\(') == text.count(r'\)'), f"{label}: Unbalanced \\( \\) in {text[:120]!r}"
    assert text.count(r'\[') == text.count(r'\]'), f"{label}: Unbalanced \\[ \\] in {text[:120]!r}"
    # Ensure no $...$ LaTeX delimiters: every unescaped $ must be currency followed by a digit
    for m in re.finditer(r'(?<!\\)\$', text):
        after = text[m.end():m.end() + 1]
        assert after.isdigit(), f"{label}: Non-currency '$' delimiter found near {text[max(0, m.start()-15):m.end()+20]!r}"


def _verify_blueprint(content_json):
    expected_domains = (
        ['Algebra'] * 8
        + ['Advanced Math'] * 7
        + ['Problem-Solving and Data Analysis'] * 4
        + ['Geometry and Trigonometry'] * 3
    )
    expected_spr = {5, 9, 13, 16, 19, 22}
    prefix_map = {
        'module1': 'sat_mm4_m1_q',
        'module2_hard': 'sat_mm4_m2h_q',
        'module2_lower': 'sat_mm4_m2l_q',
    }

    for mod_key, id_prefix in prefix_map.items():
        qs = content_json[mod_key]['questions']
        assert len(qs) == 22, f"{mod_key}: expected 22 questions, got {len(qs)}"
        spr_nums = set()
        mcq_counts = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
        has_table = False
        has_svg = False

        for i, q in enumerate(qs):
            num = i + 1
            assert q['id'] == f"{id_prefix}{num}", f"{mod_key} Q{num}: bad id {q['id']}"
            assert q['number'] == num, f"{mod_key} Q{num}: bad number {q['number']}"
            assert q['domain'] == expected_domains[i], (
                f"{mod_key} Q{num}: domain {q['domain']} != {expected_domains[i]}"
            )

            exp = q['explanation']
            assert exp.get('summaryVi') and len(exp['summaryVi']) >= 30, f"{mod_key} Q{num}: short summaryVi"
            assert exp.get('desmosTipVi') and len(exp['desmosTipVi']) >= 15, f"{mod_key} Q{num}: missing desmosTipVi"
            assert exp.get('keyTakeaway') and len(exp['keyTakeaway']) >= 15, f"{mod_key} Q{num}: missing keyTakeaway"

            _check_text_hygiene(q['stimulusHtml'], f"{mod_key} Q{num} stimulus")
            _check_text_hygiene(q['questionHtml'], f"{mod_key} Q{num} question")
            _check_text_hygiene(exp['summaryVi'], f"{mod_key} Q{num} summaryVi")
            _check_text_hygiene(exp['desmosTipVi'], f"{mod_key} Q{num} desmosTipVi")
            _check_text_hygiene(exp['keyTakeaway'], f"{mod_key} Q{num} keyTakeaway")

            if q['domain'] == 'Problem-Solving and Data Analysis' and '<table>' in q['stimulusHtml']:
                has_table = True
            if q['domain'] == 'Geometry and Trigonometry' and '<svg' in q['stimulusHtml']:
                has_svg = True

            if q['questionFormat'] == 'spr':
                spr_nums.add(num)
                assert q.get('acceptedAnswers'), f"{mod_key} Q{num}: missing acceptedAnswers"
                assert q.get('correctDisplay'), f"{mod_key} Q{num}: missing correctDisplay"
            else:
                mcq_counts[q['correctAnswer']] += 1
                for opt in q['options']:
                    _check_text_hygiene(opt['text'], f"{mod_key} Q{num} opt {opt['label']}")
                for lbl, oa in exp['optionAnalysis'].items():
                    _check_text_hygiene(oa['reasonVi'], f"{mod_key} Q{num} oa[{lbl}]")

        assert spr_nums == expected_spr, f"{mod_key}: SPR positions {spr_nums} != {expected_spr}"
        assert mcq_counts == {'A': 4, 'B': 4, 'C': 4, 'D': 4}, (
            f"{mod_key}: MCQ balance {mcq_counts} != A:4,B:4,C:4,D:4"
        )
        assert has_table, f"{mod_key}: missing HTML data table in Data Analysis"
        assert has_svg, f"{mod_key}: missing SVG diagram in Geometry and Trigonometry"


if __name__ == '__main__':
    from sat_qa_validator import validate_sat_test

    assert verify_m1(), 'Module 1 math verification failed!'
    assert verify_m2h(), 'Module 2 Hard math verification failed!'
    assert verify_m2l(), 'Module 2 Standard math verification failed!'

    slug, title, order_idx, content_json = get_mock_04()
    assert slug == 'math_mock_04'
    assert order_idx == 4
    assert content_json['basicInfo']['routingThreshold'] == 15

    errs = validate_sat_test(content_json, title)
    if errs:
        for e in errs:
            print('QA ERROR:', e)
        sys.exit(1)

    _verify_blueprint(content_json)
    print('MATH MOCK 04 (66 Qs) VERIFIED & QA PASSED!')
