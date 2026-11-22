# -*- coding: utf-8 -*-
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

from sat_mock_01_m1 import get_m1_questions
from sat_mock_01_m2h import get_m2h_questions
from sat_mock_01_m2l import get_m2l_questions

def get_mock_01():
    return {
        'schemaVersion': 1,
        'mode': 'adaptive_mock',
        'section': 'Reading and Writing',
        'basicInfo': {
            'title': 'Digital SAT R&W Adaptive Mock Test #1 (Bluebook Official Format)',
            'subtitle': 'Đề thi thử thích ứng chuẩn Bluebook #1 (Module 1 → Adaptive Module 2 Hard/Lower, 54 câu / 64 phút, quy đổi thang điểm 200–800).',
            'difficultyBadge': 'Adaptive Mock #1 • Target 1500+',
            'routingThreshold': 18,
        },
        'module1': {
            'id': 'mock1_m1',
            'title': 'Section 1, Module 1: Reading and Writing',
            'timeLimitMinutes': 32,
            'questions': get_m1_questions(),
        },
        'module2_hard': {
            'id': 'mock1_m2h',
            'title': 'Section 1, Module 2: Reading and Writing (Hard Route)',
            'timeLimitMinutes': 32,
            'questions': get_m2h_questions(),
        },
        'module2_lower': {
            'id': 'mock1_m2l',
            'title': 'Section 1, Module 2: Reading and Writing (Standard Route)',
            'timeLimitMinutes': 32,
            'questions': get_m2l_questions(),
        },
    }

if __name__ == '__main__':
    from sat_qa_validator import validate_sat_test
    d = get_mock_01()
    errs = validate_sat_test(d, 'Mock 1')
    print('ERRORS:', errs or 'NONE')
    for k in ('module1', 'module2_hard', 'module2_lower'):
        qs = d[k]['questions']
        dist = {c: sum(1 for q in qs if q['correctAnswer'] == c) for c in 'ABCD'}
        print(f"  {k}: {len(qs)} Qs | Keys: {dist}")
