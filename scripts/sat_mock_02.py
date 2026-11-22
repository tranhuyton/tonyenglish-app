# -*- coding: utf-8 -*-
"""
Digital SAT 1500+ Reading & Writing — Full-Length Adaptive Mock Test #2
Combines Module 1 (Routing), Module 2 Hard Route, and Module 2 Standard Route
into the official Bluebook adaptive_mock schema (81 total questions).
"""

from sat_mock_02_m1 import get_m1_questions
from sat_mock_02_m2h import get_m2h_questions
from sat_mock_02_m2l import get_m2l_questions


def get_mock_02():
    return {
        'schemaVersion': 1,
        'mode': 'adaptive_mock',
        'section': 'Reading and Writing',
        'basicInfo': {
            'title': 'Digital SAT R&W Adaptive Mock Test #2 (Bluebook Official Format)',
            'subtitle': 'Đề thi thử thích ứng chuẩn Bluebook #2 (Module 1 → Adaptive Module 2 Hard/Lower, 54 câu / 64 phút, quy đổi thang điểm 200–800).',
            'difficultyBadge': 'Adaptive Mock #2 • Target 1500+',
            'routingThreshold': 18,
        },
        'module1': {
            'id': 'mock2_m1',
            'title': 'Section 1, Module 1: Reading and Writing',
            'timeLimitMinutes': 32,
            'questions': get_m1_questions(),
        },
        'module2_hard': {
            'id': 'mock2_m2h',
            'title': 'Section 1, Module 2: Reading and Writing (Hard Route)',
            'timeLimitMinutes': 32,
            'questions': get_m2h_questions(),
        },
        'module2_lower': {
            'id': 'mock2_m2l',
            'title': 'Section 1, Module 2: Reading and Writing (Standard Route)',
            'timeLimitMinutes': 32,
            'questions': get_m2l_questions(),
        },
    }


if __name__ == '__main__':
    from sat_qa_validator import validate_sat_test
    data = get_mock_02()
    errs = validate_sat_test(data, 'Mock 2')
    print('ERRORS:', errs or 'NONE')
    for k in ('module1', 'module2_hard', 'module2_lower'):
        qs = data[k]['questions']
        dist = {c: sum(1 for q in qs if q['correctAnswer'] == c) for c in 'ABCD'}
        print(k, len(qs), dist)
