# -*- coding: utf-8 -*-
"""
Digital SAT Math Full-Length Adaptive Mock Test #3 (Bluebook Official Format)
Combines Module 1 (22 Qs), Module 2 Hard Route (22 Qs), and Module 2 Standard Route (22 Qs).
Total: 66 unique, programmatically verified questions.
"""

import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))

from sat_math_helpers import build_math_adaptive_mock_json
from sat_math_mock_03_m1 import get_m1_questions, verify_math as verify_m1
from sat_math_mock_03_m2h import get_m2h_questions, verify_math as verify_m2h
from sat_math_mock_03_m2l import get_m2l_questions, verify_math as verify_m2l


def get_mock_03():
    title = 'SAT Math Adaptive Mock Test #3 (Full 2-Module Bluebook)'
    subtitle = (
        'Đề thi thử thích ứng Digital SAT Math #3 chuẩn Bluebook '
        '(Module 1 Routing → Adaptive Module 2 Hard/Standard, 44 câu / 70 phút, '
        'tích hợp Desmos & SPR Grid-In, thang điểm 200–800).'
    )
    content_json = build_math_adaptive_mock_json(
        title=title,
        subtitle=subtitle,
        m1_qs=get_m1_questions(),
        m2_hard_qs=get_m2h_questions(),
        m2_lower_qs=get_m2l_questions(),
        routing_threshold=15,
    )
    return ('math_mock_03', title, 3, content_json)


def _iter_strings(obj, path=''):
    if isinstance(obj, str):
        yield path, obj
    elif isinstance(obj, dict):
        for k, v in obj.items():
            yield from _iter_strings(v, f'{path}.{k}' if path else k)
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            yield from _iter_strings(v, f'{path}[{i}]')


def _audit_blueprint(content_json):
    errors = []
    expected_spr = {5, 9, 13, 16, 19, 22}
    module_specs = [
        ('module1', 'sat_mm3_m1_q'),
        ('module2_hard', 'sat_mm3_m2h_q'),
        ('module2_lower', 'sat_mm3_m2l_q'),
    ]

    for mkey, id_prefix in module_specs:
        qs = content_json[mkey]['questions']
        if len(qs) != 22:
            errors.append(f'[{mkey}] Expected 22 questions, got {len(qs)}')
            continue

        spr_nums = set()
        mcq_counts = {'A': 0, 'B': 0, 'C': 0, 'D': 0}

        for idx, q in enumerate(qs, start=1):
            expected_id = f'{id_prefix}{idx}'
            if q['id'] != expected_id:
                errors.append(f'[{mkey} Q{idx}] Expected id {expected_id}, got {q["id"]}')

            if 1 <= idx <= 8:
                exp_domain = 'Algebra'
            elif 9 <= idx <= 15:
                exp_domain = 'Advanced Math'
            elif 16 <= idx <= 19:
                exp_domain = 'Problem-Solving and Data Analysis'
            else:
                exp_domain = 'Geometry and Trigonometry'

            if q['domain'] != exp_domain:
                errors.append(f'[{mkey} Q{idx}] Expected domain {exp_domain}, got {q["domain"]}')

            if q['questionFormat'] == 'spr':
                spr_nums.add(idx)
                if not q.get('correctDisplay'):
                    errors.append(f'[{mkey} Q{idx}] SPR missing correctDisplay')
                if r'\(' in (q.get('correctDisplay') or '') or r'\frac' in (q.get('correctDisplay') or ''):
                    errors.append(f'[{mkey} Q{idx}] SPR correctDisplay should be plain text, not raw LaTeX')
            else:
                mcq_counts[q['correctAnswer']] += 1

            exp = q.get('explanation') or {}
            if not exp.get('desmosTipVi') or len(exp['desmosTipVi'].strip()) < 15:
                errors.append(f'[{mkey} Q{idx}] Missing or short desmosTipVi')
            if not exp.get('keyTakeaway') or len(exp['keyTakeaway'].strip()) < 15:
                errors.append(f'[{mkey} Q{idx}] Missing or short keyTakeaway')

            # Check all string fields for escaped LaTeX corruption, unbalanced delimiters, or $...$ math
            for spath, s in _iter_strings(q):
                for ch in s:
                    if ord(ch) < 32 and ch != '\n':
                        errors.append(f'[{mkey} Q{idx} {spath}] Control char {repr(ch)} found (likely unescaped LaTeX)')
                if s.count(r'\(') != s.count(r'\)'):
                    errors.append(f'[{mkey} Q{idx} {spath}] Unbalanced \\( \\) delimiters')
                if s.count(r'\[') != s.count(r'\]'):
                    errors.append(f'[{mkey} Q{idx} {spath}] Unbalanced \\[ \\] delimiters')
                # Detect accidental $...$ math (e.g. $x+1$); allow currency like $195 or $34,000 or \$
                cleaned = s.replace(r'\$', '')
                if re.search(r'\$[a-zA-Z\\]', cleaned):
                    errors.append(f'[{mkey} Q{idx} {spath}] Possible $...$ math delimiter found')

        if spr_nums != expected_spr:
            errors.append(f'[{mkey}] SPR positions {sorted(spr_nums)} != {sorted(expected_spr)}')
        if mcq_counts != {'A': 4, 'B': 4, 'C': 4, 'D': 4}:
            errors.append(f'[{mkey}] MCQ answer distribution {mcq_counts} != A:4,B:4,C:4,D:4')

    return errors


if __name__ == '__main__':
    from sat_qa_validator import validate_sat_test

    verify_m1()
    verify_m2h()
    verify_m2l()

    key, title, order_num, content_json = get_mock_03()
    assert key == 'math_mock_03' and order_num == 3
    assert content_json['basicInfo']['routingThreshold'] == 15

    qa_errors = validate_sat_test(content_json, title)
    bp_errors = _audit_blueprint(content_json)
    all_errors = qa_errors + bp_errors

    if all_errors:
        print('QA ERRORS FOUND:')
        for e in all_errors:
            print('  -', e)
        sys.exit(1)

    for mk in ('module1', 'module2_hard', 'module2_lower'):
        qs = content_json[mk]['questions']
        mcq_dist = {c: sum(1 for q in qs if q['questionFormat'] == 'mcq' and q['correctAnswer'] == c) for c in 'ABCD'}
        spr_pos = [q['number'] for q in qs if q['questionFormat'] == 'spr']
        print(f'  {mk}: {len(qs)} Qs | MCQ={mcq_dist} | SPR={spr_pos}')

    print('MATH MOCK 03 (66 Qs) VERIFIED & QA PASSED!')
