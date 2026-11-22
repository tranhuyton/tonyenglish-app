# -*- coding: utf-8 -*-
"""
Digital SAT Reading & Writing Adaptive Mock Test #3 (Bluebook Official Format)
Combines Module 1 (27 Qs), Module 2 Hard Route (27 Qs), and Module 2 Lower Route (27 Qs).
"""

from sat_mock_03_m1 import get_m1_questions
from sat_mock_03_m2h import get_m2h_questions
from sat_mock_03_m2l import get_m2l_questions


def get_mock_03():
    return {
        'schemaVersion': 1,
        'mode': 'adaptive_mock',
        'section': 'Reading and Writing',
        'basicInfo': {
            'title': 'Digital SAT R&W Adaptive Mock Test #3 (Bluebook Official Format)',
            'subtitle': 'Đề thi thử thích ứng chuẩn Bluebook #3 (Module 1 → Adaptive Module 2 Hard/Lower, 54 câu / 64 phút, quy đổi thang điểm 200–800).',
            'difficultyBadge': 'Adaptive Mock #3 • Target 1500+',
            'routingThreshold': 18,
        },
        'module1': {
            'id': 'mock3_m1',
            'title': 'Section 1, Module 1: Reading and Writing',
            'timeLimitMinutes': 32,
            'questions': get_m1_questions(),
        },
        'module2_hard': {
            'id': 'mock3_m2h',
            'title': 'Section 1, Module 2: Reading and Writing (Hard Route)',
            'timeLimitMinutes': 32,
            'questions': get_m2h_questions(),
        },
        'module2_lower': {
            'id': 'mock3_m2l',
            'title': 'Section 1, Module 2: Reading and Writing (Standard Route)',
            'timeLimitMinutes': 32,
            'questions': get_m2l_questions(),
        },
    }


if __name__ == '__main__':
    from sat_qa_validator import validate_sat_test
    mock = get_mock_03()
    errs = validate_sat_test(mock, 'Mock 3')
    print('ERRORS:', errs or 'NONE')
    for k in ('module1', 'module2_hard', 'module2_lower'):
        qs = mock[k]['questions']
        dist = {c: sum(1 for q in qs if q['correctAnswer'] == c) for c in 'ABCD'}
        print(k, len(qs), dist)
