# -*- coding: utf-8 -*-
"""
Cambridge IGCSE Additional Mathematics (0606) — 2025–2027 Syllabus Full Mock Exams
==================================================================================
Exports `MOCKS_0606_2025`: 4 authentic, strictly 80-mark (120-minute) Cambridge
0606 full-length mock exam papers compatible with `generate_cambridge_exam_pdf`
and `build_igcse_paper_json` in `scripts/igcse_maths_pipeline.py`:

  1. `m0606_p1_1` — 0606/11 Paper 1 (Non-Calculator) Full Mock #1 [80 marks]
  2. `m0606_p1_2` — 0606/12 Paper 1 (Non-Calculator) Full Mock #2 [80 marks]
  3. `m0606_p2_1` — 0606/21 Paper 2 (Calculator)     Full Mock #1 [80 marks]
  4. `m0606_p2_2` — 0606/22 Paper 2 (Calculator)     Full Mock #2 [80 marks]

Syllabus compliance (Cambridge 0606 2025–2027):
  - Paper 1 is 100% Non-Calculator (exact surds, fractions, pi, ln/e).
  - Paper 2 is Calculator Allowed (3 s.f. / 1 d.p. for angles in degrees).
  - Includes the NEW 2025–2027 topic: Coordinate Geometry of the Circle across all 4 papers.
  - Strictly ZERO Relative Velocity questions (removed in 2025–2027).
  - All math uses KaTeX `\\(...\\)` / `\\[...\\]` delimiters (never `$...$`).
"""

from fractions import Fraction
import itertools
import math
import re

COURSE_0606_ID = '0a8d7434-262a-4462-89c1-2b01c6ea1e4e'

# =============================================================================
# PAPER 1: 0606/11 — Paper 1 (Non-Calculator) Full Mock #1 — EXACTLY 80 MARKS
# Marks: Q1(7) Q2(7) Q3(9) Q4(8) Q5(8) Q6(7) Q7(8) Q8(8) Q9(8) Q10(10) = 80
# =============================================================================
PAPER_0606_11 = {
    'code': 'm0606_p1_1',
    'pdf_rel_path': 'papers/igcse-maths/0606_p1_noncalc_mock1.pdf',
    'order_index': 101,
    'paper_meta': {
        'code': '0606/11',
        'title': '🚫 0606/11 Paper 1 (Non-Calculator) Full Mock #1 [2025–2027]',
        'syllabus': '0606',
        'syllabus_name': 'Cambridge IGCSE Additional Mathematics (0606) — Paper 1 Non-Calculator',
        'course_id': COURSE_0606_ID,
        'time_limit': 120,
        'calculator_policy': 'non-calculator',
    },
    'questions': [
        {
            'question_number': 1,
            'stem': r'Do not use a calculator in this question.',
            'sub_questions': [
                {
                    'id': 'p11_q1a',
                    'type': 'long_answer',
                    'label': r'(a) Solve the equation \(|3x - 5| = x + 3\).',
                    'max_marks': 3,
                    'marking_scheme': (
                        r'[M1] Split into \(3x - 5 = x + 3\) and \(3x - 5 = -(x + 3)\), or square both sides to obtain \(2x^2 - 9x + 4 = 0\). '
                        r'[A1] \(x = 4\). '
                        r'[A1] \(x = \frac{1}{2}\) (both satisfy \(x + 3 \geq 0\)). '
                        r'| Ghi chú: Luôn kiểm tra điều kiện vế phải \(x + 3 \geq 0\) để loại nghiệm ngoại lai.'
                    ),
                },
                {
                    'id': 'p11_q1b',
                    'type': 'long_answer',
                    'label': r'(b) Find the range of values of \(k\) for which the line \(y = kx - 2\) does not intersect the curve \(y = x^2 + 5x + 2k\).',
                    'max_marks': 4,
                    'marking_scheme': (
                        r'[M1] Equate line and curve to form \(x^2 + (5 - k)x + (2k + 2) = 0\). '
                        r'[DM1] Apply no-intersection condition \(b^2 - 4ac < 0\): \((5 - k)^2 - 4(2k + 2) < 0 \Rightarrow k^2 - 18k + 17 < 0\). '
                        r'[A1] Factorise \((k - 1)(k - 17) < 0\), critical values \(k = 1\) and \(k = 17\). '
                        r'[A1] \(1 < k < 17\). '
                        r'| Ghi chú: Đường thẳng không cắt parabol khi biệt thức \(\Delta < 0\).'
                    ),
                },
            ],
        },
        {
            'question_number': 2,
            'stem': r'Do not use a calculator in this question.',
            'sub_questions': [
                {
                    'id': 'p11_q2a',
                    'type': 'long_answer',
                    'label': r'(a) Express \((2 + 7\sqrt{3}) \div (5 - 2\sqrt{3})\) in the form \(a + b\sqrt{3}\), where \(a\) and \(b\) are integers.',
                    'max_marks': 3,
                    'marking_scheme': (
                        r'[M1] Multiply numerator and denominator by the conjugate \(5 + 2\sqrt{3}\). '
                        r'[DM1] Expand to obtain \(\frac{10 + 4\sqrt{3} + 35\sqrt{3} + 42}{25 - 12} = \frac{52 + 39\sqrt{3}}{13}\). '
                        r'[A1] \(4 + 3\sqrt{3}\) (\(a = 4, \; b = 3\)). '
                        r'| Ghi chú: Nhân liên hợp mẫu số \((5 - 2\sqrt{3})(5 + 2\sqrt{3}) = 25 - 12 = 13\).'
                    ),
                },
                {
                    'id': 'p11_q2b',
                    'type': 'long_answer',
                    'label': r'(b) A trapezium has parallel sides of lengths \((3 + \sqrt{5})\text{ cm}\) and \((5 + \sqrt{5})\text{ cm}\), and its area is \((15 + \sqrt{5})\text{ cm}^2\). Find the exact perpendicular height of the trapezium in the form \(p + q\sqrt{5}\text{ cm}\), where \(p\) and \(q\) are integers.',
                    'max_marks': 4,
                    'marking_scheme': (
                        r'[M1] Substitute into trapezium area formula: \(\frac{1}{2}\left[(3 + \sqrt{5}) + (5 + \sqrt{5})\right]h = 15 + \sqrt{5}\). '
                        r'[A1] Simplify to \((4 + \sqrt{5})h = 15 + \sqrt{5}\), so \(h = \frac{15 + \sqrt{5}}{4 + \sqrt{5}}\). '
                        r'[DM1] Rationalise denominator: \(\frac{(15 + \sqrt{5})(4 - \sqrt{5})}{16 - 5} = \frac{60 - 15\sqrt{5} + 4\sqrt{5} - 5}{11} = \frac{55 - 11\sqrt{5}}{11}\). '
                        r'[A1] \(h = 5 - \sqrt{5}\text{ cm}\). '
                        r'| Ghi chú: Diện tích hình thang \(A = \frac{1}{2}(a + b)h\); kiểm tra \(5 - \sqrt{5} > 0\).'
                    ),
                },
            ],
        },
        {
            'question_number': 3,
            'stem': r'The polynomial \(\text{p}(x) = 2x^3 + ax^2 + bx + 6\) has a factor \((x - 2)\) and leaves a remainder of \(9\) when divided by \((x + 1)\).',
            'sub_questions': [
                {
                    'id': 'p11_q3a',
                    'type': 'long_answer',
                    'label': r'(a) Find the value of \(a\) and the value of \(b\).',
                    'max_marks': 4,
                    'marking_scheme': (
                        r'[M1] By Factor Theorem, \(\text{p}(2) = 0 \Rightarrow 16 + 4a + 2b + 6 = 0 \Rightarrow 2a + b = -11\). '
                        r'[M1] By Remainder Theorem, \(\text{p}(-1) = 9 \Rightarrow -2 + a - b + 6 = 9 \Rightarrow a - b = 5\). '
                        r'[DM1] Solve simultaneous linear equations: adding gives \(3a = -6\). '
                        r'[A1] \(a = -2\) and \(b = -7\). '
                        r'| Ghi chú: Dùng Định lý Nhân tử \(\text{p}(2) = 0\) và Định lý Số dư \(\text{p}(-1) = 9\).'
                    ),
                },
                {
                    'id': 'p11_q3b',
                    'type': 'long_answer',
                    'label': r'(b) Using your values of \(a\) and \(b\), solve the equation \(\text{p}(x) = 0\), giving your non-integer roots in exact surd form.',
                    'max_marks': 5,
                    'marking_scheme': (
                        r'[M1] Divide \(2x^3 - 2x^2 - 7x + 6\) by \((x - 2)\) by long division or coefficient comparison. '
                        r'[A1] Obtain quadratic factor: \(\text{p}(x) = (x - 2)(2x^2 + 2x - 3)\). '
                        r'[DM1] Solve \(2x^2 + 2x - 3 = 0\) using the quadratic formula: \(x = \frac{-2 \pm \sqrt{4 - 4(2)(-3)}}{4} = \frac{-2 \pm \sqrt{28}}{4}\). '
                        r'[A1] Simplify surd roots: \(x = \frac{-1 + \sqrt{7}}{2}\) and \(x = \frac{-1 - \sqrt{7}}{2}\). '
                        r'[B1] State all three roots including \(x = 2\). '
                        r'| Ghi chú: Rút gọn \(\sqrt{28} = 2\sqrt{7}\) trước khi chia cả tử và mẫu cho \(2\); không bỏ sót nghiệm \(x = 2\).'
                    ),
                },
            ],
        },
        {
            'question_number': 4,
            'stem': r'A circle \(C\) has equation \(x^2 + y^2 - 6x + 8y - 15 = 0\).',
            'sub_questions': [
                {
                    'id': 'p11_q4a',
                    'type': 'long_answer',
                    'label': r'(a) Find the coordinates of the centre \(M\) and the exact radius of \(C\), leaving the radius in simplified surd form.',
                    'max_marks': 3,
                    'marking_scheme': (
                        r'[M1] Complete the square: \((x - 3)^2 - 9 + (y + 4)^2 - 16 - 15 = 0 \Rightarrow (x - 3)^2 + (y + 4)^2 = 40\). '
                        r'[A1] Centre \(M(3, -4)\). '
                        r'[A1] Radius \(r = \sqrt{40} = 2\sqrt{10}\). '
                        r'| Ghi chú: Chuyên đề mới 2025–2027 (Circle); luôn rút gọn căn thức \(\sqrt{40} = 2\sqrt{10}\).'
                    ),
                },
                {
                    'id': 'p11_q4b',
                    'type': 'short_answer',
                    'label': r'(b) Verify that the point \(P(5, 2)\) lies on \(C\) and find the gradient of the radius \(MP\).',
                    'max_marks': 2,
                    'marking_scheme': (
                        r'[B1] Substitute \(x = 5, \; y = 2\): \(5^2 + 2^2 - 6(5) + 8(2) - 15 = 25 + 4 - 30 + 16 - 15 = 0\) (hence \(P\) lies on \(C\)). '
                        r'[B1] Gradient \(m_{MP} = \frac{2 - (-4)}{5 - 3} = \frac{6}{2} = 3\). '
                        r'| Ghi chú: Thay trực tiếp tọa độ \(P\) vào phương trình đường tròn để kiểm chứng.'
                    ),
                },
                {
                    'id': 'p11_q4c',
                    'type': 'long_answer',
                    'label': r'(c) Find the equation of the tangent to \(C\) at \(P\), giving your answer in the form \(ax + by + c = 0\), where \(a, b\) and \(c\) are integers.',
                    'max_marks': 3,
                    'marking_scheme': (
                        r'[M1] Tangent is perpendicular to radius \(MP\), so \(m_T = -\frac{1}{3}\). '
                        r'[DM1] Use point-slope form at \(P(5, 2)\): \(y - 2 = -\frac{1}{3}(x - 5)\). '
                        r'[A1] \(x + 3y - 11 = 0\) (accept any non-zero integer multiple such as \(-x - 3y + 11 = 0\)). '
                        r'| Ghi chú: Tiếp tuyến vuông góc bán kính tại tiếp điểm nên \(m_T \cdot m_{MP} = -1\).'
                    ),
                },
            ],
        },
        {
            'question_number': 5,
            'stem': r'Do not use a calculator in this question.',
            'sub_questions': [
                {
                    'id': 'p11_q5a',
                    'type': 'long_answer',
                    'label': r'(a) Solve the equation \(\log_{3}(2x - 1) + \log_{3}(x + 1) = 2\).',
                    'max_marks': 4,
                    'marking_scheme': (
                        r'[M1] Combine logarithms: \(\log_{3}\left[(2x - 1)(x + 1)\right] = 2\). '
                        r'[DM1] Convert to exponential form: \((2x - 1)(x + 1) = 3^2 = 9 \Rightarrow 2x^2 + x - 10 = 0\). '
                        r'[A1] Factorise \((2x + 5)(x - 2) = 0 \Rightarrow x = 2\) or \(x = -\frac{5}{2}\). '
                        r'[A1] Reject \(x = -\frac{5}{2}\) since \(2x - 1 > 0\), leaving \(x = 2\) only. '
                        r'| Ghi chú: Bắt buộc kiểm tra tập xác định \(2x - 1 > 0\) và \(x + 1 > 0\) để loại nghiệm âm.'
                    ),
                },
                {
                    'id': 'p11_q5b',
                    'type': 'long_answer',
                    'label': r'(b) Solve the equation \(2^{2y + 1} - 9(2^y) + 4 = 0\).',
                    'max_marks': 4,
                    'marking_scheme': (
                        r'[M1] Rewrite \(2^{2y + 1} = 2(2^y)^2\) and substitute \(u = 2^y\) (\(u > 0\)) to get \(2u^2 - 9u + 4 = 0\). '
                        r'[DM1] Factorise \((2u - 1)(u - 4) = 0\). '
                        r'[A1] \(u = \frac{1}{2}\) and \(u = 4\). '
                        r'[A1] \(2^y = 2^{-1} \Rightarrow y = -1\) and \(2^y = 2^2 \Rightarrow y = 2\). '
                        r'| Ghi chú: Tách \(2^{2y+1} = 2 \cdot (2^y)^2\) để đưa về phương trình bậc hai theo ẩn phụ \(u = 2^y\).'
                    ),
                },
            ],
        },
        {
            'question_number': 6,
            'stem': r'Do not use a calculator in this question.',
            'sub_questions': [
                {
                    'id': 'p11_q6a',
                    'type': 'long_answer',
                    'label': r'(a) Find the first three terms, in ascending powers of \(x\), in the expansion of \(\left(2 - \frac{x}{4}\right)^6\), simplifying each coefficient.',
                    'max_marks': 3,
                    'marking_scheme': (
                        r'[B1] Constant term: \(\binom{6}{0} 2^6 = 64\). '
                        r'[B1] \(x\)-term: \(\binom{6}{1} 2^5 \left(-\frac{x}{4}\right) = 6(32)\left(-\frac{1}{4}\right)x = -48x\). '
                        r'[B1] \(x^2\)-term: \(\binom{6}{2} 2^4 \left(-\frac{x}{4}\right)^2 = 15(16)\left(\frac{1}{16}\right)x^2 = 15x^2\). Final: \(64 - 48x + 15x^2\). '
                        r'| Ghi chú: Chú ý dấu trừ trong \(\left(-\frac{x}{4}\right)^r\) ở các lũy thừa lẻ và chẵn.'
                    ),
                },
                {
                    'id': 'p11_q6b',
                    'type': 'long_answer',
                    'label': r'(b) Given that the coefficient of \(x^2\) in the expansion of \((1 + kx)\left(2 - \frac{x}{4}\right)^6\) is \(-57\), find the exact value of the constant \(k\), and hence find the coefficient of \(x\) in this expansion.',
                    'max_marks': 4,
                    'marking_scheme': (
                        r'[M1] Identify terms contributing to \(x^2\) in \((1 + kx)(64 - 48x + 15x^2 + \dots)\): \(1(15) + k(-48) = 15 - 48k\). '
                        r'[DM1] Set \(15 - 48k = -57 \Rightarrow 48k = 72\). '
                        r'[A1] \(k = \frac{3}{2}\). '
                        r'[A1] Coefficient of \(x = 1(-48) + \frac{3}{2}(64) = -48 + 96 = 48\). '
                        r'| Ghi chú: Ghép đúng cặp nhân tạo ra \(x^2\) và \(x\), không cần khai triển toàn bộ đa thức.'
                    ),
                },
            ],
        },
        {
            'question_number': 7,
            'stem': r'Do not use a calculator in this question.',
            'sub_questions': [
                {
                    'id': 'p11_q7a',
                    'type': 'long_answer',
                    'label': r'(a) Prove the identity \(\frac{\sin x}{1 + \cos x} + \frac{1 + \cos x}{\sin x} \equiv 2\text{cosec}\,x\).',
                    'max_marks': 3,
                    'marking_scheme': (
                        r'[M1] Combine over common denominator: \(\text{LHS} = \frac{\sin^2 x + (1 + \cos x)^2}{\sin x(1 + \cos x)}\). '
                        r'[DM1] Expand and apply \(\sin^2 x + \cos^2 x = 1\): \(\frac{\sin^2 x + 1 + 2\cos x + \cos^2 x}{\sin x(1 + \cos x)} = \frac{2 + 2\cos x}{\sin x(1 + \cos x)} = \frac{2(1 + \cos x)}{\sin x(1 + \cos x)}\). '
                        r'[A1] Cancel \((1 + \cos x)\) to obtain \(\frac{2}{\sin x} = 2\text{cosec}\,x = \text{RHS}\) (AG). '
                        r'| Ghi chú: Chứng minh đẳng thức từ VT sang VP, trình bày rõ bước dùng \(\sin^2 x + \cos^2 x = 1\).'
                    ),
                },
                {
                    'id': 'p11_q7b',
                    'type': 'long_answer',
                    'label': r'(b) Hence solve the equation \(\frac{\sin x}{1 + \cos x} + \frac{1 + \cos x}{\sin x} = 4\sin x + 2\) for \(0 \leq x \leq 2\pi\), giving your answers as exact multiples of \(\pi\).',
                    'max_marks': 5,
                    'marking_scheme': (
                        r'[M1] Replace LHS using part (a): \(\frac{2}{\sin x} = 4\sin x + 2 \Rightarrow 4\sin^2 x + 2\sin x - 2 = 0 \Rightarrow 2\sin^2 x + \sin x - 1 = 0\). '
                        r'[DM1] Factorise \((2\sin x - 1)(\sin x + 1) = 0\). '
                        r'[A1] Obtain \(\sin x = \frac{1}{2}\) and \(\sin x = -1\). '
                        r'[A1] From \(\sin x = \frac{1}{2}\): \(x = \frac{\pi}{6}, \; \frac{5\pi}{6}\). '
                        r'[A1] From \(\sin x = -1\): \(x = \frac{3\pi}{2}\) (all satisfy \(\sin x \neq 0\) and \(\cos x \neq -1\)). '
                        r'| Ghi chú: Làm việc ở đơn vị Radian và kiểm tra không vi phạm mẫu số bằng \(0\).'
                    ),
                },
            ],
        },
        {
            'question_number': 8,
            'stem': (
                r'The functions \(\text{f}\) and \(\text{g}\) are defined by' + '\n'
                + r'\[\text{f}(x) = (x - 3)^2 + 2 \quad \text{for } x \geq 3,\]' + '\n'
                + r'\[\text{g}(x) = \frac{2x + 1}{x - 1} \quad \text{for } x > 1.\]'
            ),
            'sub_questions': [
                {
                    'id': 'p11_q8a',
                    'type': 'short_answer',
                    'label': r'(a) State the range of \(\text{f}\) and explain why \(\text{f}\) has an inverse.',
                    'max_marks': 2,
                    'marking_scheme': (
                        r'[B1] Range of \(\text{f}\): \(\text{f}(x) \geq 2\) (accept \(y \geq 2\)). '
                        r'[B1] \(\text{f}\) is a one-to-one function on the restricted domain \(x \geq 3\) (strictly increasing), so \(\text{f}^{-1}\) exists. '
                        r'| Ghi chú: Hàm ngược tồn tại khi và chỉ khi hàm là đơn ánh (one-to-one) trên miền xác định.'
                    ),
                },
                {
                    'id': 'p11_q8b',
                    'type': 'long_answer',
                    'label': r'(b) Find an expression for \(\text{f}^{-1}(x)\) and state its domain.',
                    'max_marks': 3,
                    'marking_scheme': (
                        r'[M1] Let \(y = (x - 3)^2 + 2 \Rightarrow (x - 3)^2 = y - 2 \Rightarrow x = 3 \pm \sqrt{y - 2}\). '
                        r'[A1] Since \(x \geq 3\), select positive root: \(\text{f}^{-1}(x) = 3 + \sqrt{x - 2}\). '
                        r'[B1] Domain of \(\text{f}^{-1}\): \(x \geq 2\) (equals the range of \(\text{f}\)). '
                        r'| Ghi chú: Miền xác định của \(\text{f}^{-1}\) chính là tập giá trị (range) của \(\text{f}\).'
                    ),
                },
                {
                    'id': 'p11_q8c',
                    'type': 'long_answer',
                    'label': r'(c) Solve the equation \(\text{fg}(x) = 11\).',
                    'max_marks': 3,
                    'marking_scheme': (
                        r'[M1] Apply \(\text{f}^{-1}\) to both sides: \(\text{g}(x) = \text{f}^{-1}(11) = 3 + \sqrt{11 - 2} = 6\) (or solve \((\text{g}(x) - 3)^2 = 9\) noting \(\text{g}(x) \geq 3\)). '
                        r'[DM1] Solve \(\frac{2x + 1}{x - 1} = 6 \Rightarrow 2x + 1 = 6x - 6 \Rightarrow 4x = 7\). '
                        r'[A1] \(x = \frac{7}{4}\) (valid since \(x > 1\)). '
                        r'| Ghi chú: Dùng \(\text{g}(x) = \text{f}^{-1}(11) = 6\) nhanh và tránh chọn nhầm nhánh âm không thuộc miền \(\text{f}\).'
                    ),
                },
            ],
        },
        {
            'question_number': 9,
            'stem': (
                r'Relative to an origin \(O\), the points \(A\) and \(B\) have position vectors \(\mathbf{a}\) and \(\mathbf{b}\) respectively, '
                r'where \(\mathbf{a}\) and \(\mathbf{b}\) are non-parallel vectors. '
                r'The point \(C\) lies on \(OA\) produced such that \(OC = 3OA\). '
                r'The point \(M\) is the midpoint of \(AB\), and the point \(D\) lies on \(OB\) such that \(OD : DB = 3 : 2\).'
            ),
            'sub_questions': [
                {
                    'id': 'p11_q9a',
                    'type': 'short_answer',
                    'label': r'(a) Express \(\vec{OM}\) and \(\vec{OD}\) in terms of \(\mathbf{a}\) and \(\mathbf{b}\).',
                    'max_marks': 2,
                    'marking_scheme': (
                        r'[B1] \(\vec{OM} = \frac{1}{2}\mathbf{a} + \frac{1}{2}\mathbf{b}\). '
                        r'[B1] \(\vec{OD} = \frac{3}{5}\mathbf{b}\). '
                        r'| Ghi chú: Tỉ số \(OD : DB = 3 : 2\) suy ra \(OD = \frac{3}{3 + 2}OB = \frac{3}{5}OB\).'
                    ),
                },
                {
                    'id': 'p11_q9b',
                    'type': 'long_answer',
                    'label': r'(b) Find \(\vec{CM}\) and \(\vec{MD}\) in terms of \(\mathbf{a}\) and \(\mathbf{b}\).',
                    'max_marks': 3,
                    'marking_scheme': (
                        r'[M1] Use \(\vec{OC} = 3\mathbf{a}\) and \(\vec{CM} = \vec{OM} - \vec{OC}\). '
                        r'[A1] \(\vec{CM} = \left(\frac{1}{2}\mathbf{a} + \frac{1}{2}\mathbf{b}\right) - 3\mathbf{a} = -\frac{5}{2}\mathbf{a} + \frac{1}{2}\mathbf{b}\). '
                        r'[A1] \(\vec{MD} = \vec{OD} - \vec{OM} = \frac{3}{5}\mathbf{b} - \left(\frac{1}{2}\mathbf{a} + \frac{1}{2}\mathbf{b}\right) = -\frac{1}{2}\mathbf{a} + \frac{1}{10}\mathbf{b}\). '
                        r'| Ghi chú: Quy tắc trừ vector: \(\vec{XY} = \vec{OY} - \vec{OX}\).'
                    ),
                },
                {
                    'id': 'p11_q9c',
                    'type': 'long_answer',
                    'label': r'(c) Show that the points \(C\), \(M\) and \(D\) are collinear, and state the ratio \(CM : MD\).',
                    'max_marks': 3,
                    'marking_scheme': (
                        r'[M1] Factor both vectors to compare: \(\vec{CM} = \frac{1}{2}(\mathbf{b} - 5\mathbf{a})\) and \(\vec{MD} = \frac{1}{10}(\mathbf{b} - 5\mathbf{a})\), so \(\vec{CM} = 5\vec{MD}\). '
                        r'[A1] Since \(\vec{CM} = 5\vec{MD}\), the vectors are parallel and share the common point \(M\); therefore \(C, M\) and \(D\) are collinear. '
                        r'[B1] \(CM : MD = 5 : 1\). '
                        r'| Ghi chú: Phải nêu đủ 2 ý: song song (\(\vec{CM} = k\vec{MD}\)) VÀ có điểm chung \(M\) mới kết luận thẳng hàng.'
                    ),
                },
            ],
        },
        {
            'question_number': 10,
            'stem': r'Do not use a calculator in this question.',
            'sub_questions': [
                {
                    'id': 'p11_q10a',
                    'type': 'long_answer',
                    'label': r'(a) Differentiate \(x\sqrt{2x + 1}\) with respect to \(x\), giving your answer in the form \((ax + b)(2x + 1)^{-1/2}\), where \(a\) and \(b\) are integers.',
                    'max_marks': 3,
                    'marking_scheme': (
                        r'[M1] Apply product rule and chain rule to \(x(2x + 1)^{1/2}\). '
                        r'[A1] \(\frac{\text{d}}{\text{d}x}\left(x\sqrt{2x + 1}\right) = (2x + 1)^{1/2} + x \cdot \frac{1}{2}(2x + 1)^{-1/2}(2) = (2x + 1)^{1/2} + x(2x + 1)^{-1/2}\). '
                        r'[A1] Factor out \((2x + 1)^{-1/2}\): \([(2x + 1) + x](2x + 1)^{-1/2} = (3x + 1)(2x + 1)^{-1/2}\) (\(a = 3, \; b = 1\)). '
                        r"| Ghi chú: Dùng quy tắc tích \((uv)' = u'v + uv'\) kết hợp quy tắc hàm hợp cho \((2x+1)^{1/2}\)."
                    ),
                },
                {
                    'id': 'p11_q10b',
                    'type': 'long_answer',
                    'label': r'(b) Hence find the exact value of \(\int_{0}^{4} (6x + 2)(2x + 1)^{-1/2}\,\text{d}x\).',
                    'max_marks': 3,
                    'marking_scheme': (
                        r'[M1] Recognise \((6x + 2)(2x + 1)^{-1/2} = 2(3x + 1)(2x + 1)^{-1/2}\). '
                        r'[A1] Antiderivative is \(\left[2x\sqrt{2x + 1}\right]_{0}^{4}\). '
                        r'[A1] Evaluate limits: \(2(4)\sqrt{9} - 0 = 24\). '
                        r'| Ghi chú: Dạng bài kinh điển "Hence integrate" của 0606: rút hệ số \(2\) để dùng trực tiếp kết quả câu (a).'
                    ),
                },
                {
                    'id': 'p11_q10c',
                    'type': 'long_answer',
                    'label': r'(c) Find the exact area of the region bounded by the curve \(y = (3x + 5)(2x + 1)^{-1/2}\), the \(x\)-axis, and the lines \(x = 0\) and \(x = 4\).',
                    'max_marks': 4,
                    'marking_scheme': (
                        r'[M1] Split the integrand: \((3x + 5)(2x + 1)^{-1/2} = (3x + 1)(2x + 1)^{-1/2} + 4(2x + 1)^{-1/2}\) (noting \(y > 0\) on \([0, 4]\)). '
                        r'[M1] Integrate the second term: \(\int 4(2x + 1)^{-1/2}\,\text{d}x = 4 \cdot \frac{(2x + 1)^{1/2}}{\frac{1}{2} \cdot 2} = 4\sqrt{2x + 1}\). '
                        r'[DM1] Evaluate \(\left[x\sqrt{2x + 1} + 4\sqrt{2x + 1}\right]_{0}^{4} = (4 \cdot 3 + 4 \cdot 3) - (0 + 4 \cdot 1) = 24 - 4\). '
                        r'[A1] Exact area \(= 20\). '
                        r'| Ghi chú: Tách \(3x + 5 = (3x + 1) + 4\) để tận dụng câu (a) và tính nguyên hàm cơ bản cho phần dư.'
                    ),
                },
            ],
        },
    ],
}

# =============================================================================
# PAPER 2: 0606/12 — Paper 1 (Non-Calculator) Full Mock #2 — EXACTLY 80 MARKS
# Marks: Q1(6) Q2(7) Q3(7) Q4(9) Q5(9) Q6(7) Q7(7) Q8(8) Q9(10) Q10(10) = 80
# =============================================================================
PAPER_0606_12 = {
    'code': 'm0606_p1_2',
    'pdf_rel_path': 'papers/igcse-maths/0606_p1_noncalc_mock2.pdf',
    'order_index': 102,
    'paper_meta': {
        'code': '0606/12',
        'title': '🚫 0606/12 Paper 1 (Non-Calculator) Full Mock #2 [2025–2027]',
        'syllabus': '0606',
        'syllabus_name': 'Cambridge IGCSE Additional Mathematics (0606) — Paper 1 Non-Calculator',
        'course_id': COURSE_0606_ID,
        'time_limit': 120,
        'calculator_policy': 'non-calculator',
    },
    'questions': [
        {
            'question_number': 1,
            'stem': r'Do not use a calculator in this question.',
            'sub_questions': [
                {
                    'id': 'p12_q1a',
                    'type': 'long_answer',
                    'label': r'(a) Solve the simultaneous equations \(2x + y = 5\) and \(x^2 + xy + y^2 = 13\).',
                    'max_marks': 4,
                    'marking_scheme': (
                        r'[M1] Substitute \(y = 5 - 2x\) into the quadratic equation: \(x^2 + x(5 - 2x) + (5 - 2x)^2 = 13\). '
                        r'[A1] Simplify to \(3x^2 - 15x + 12 = 0 \Rightarrow x^2 - 5x + 4 = 0\). '
                        r'[DM1] Factorise \((x - 1)(x - 4) = 0 \Rightarrow x = 1, \; x = 4\). '
                        r'[A1] Solutions: \((1, 3)\) and \((4, -3)\). '
                        r'| Ghi chú: Trình bày rõ từng cặp nghiệm \((x, y)\) tương ứng.'
                    ),
                },
                {
                    'id': 'p12_q1b',
                    'type': 'short_answer',
                    'label': r'(b) Hence find the exact distance between the two points of intersection of the line \(2x + y = 5\) and the curve \(x^2 + xy + y^2 = 13\).',
                    'max_marks': 2,
                    'marking_scheme': (
                        r'[M1] Apply distance formula: \(\sqrt{(4 - 1)^2 + (-3 - 3)^2} = \sqrt{9 + 36} = \sqrt{45}\). '
                        r'[A1] \(3\sqrt{5}\). '
                        r'| Ghi chú: Rút gọn \(\sqrt{45} = \sqrt{9 \times 5} = 3\sqrt{5}\).'
                    ),
                },
            ],
        },
        {
            'question_number': 2,
            'stem': r'Do not use a calculator in this question.',
            'sub_questions': [
                {
                    'id': 'p12_q2a',
                    'type': 'long_answer',
                    'label': r'(a) Solve the equation \(27^{2x - 1} = 9^{x + 2} \div 3^5\).',
                    'max_marks': 3,
                    'marking_scheme': (
                        r'[M1] Express all powers in base \(3\): \(3^{3(2x - 1)} = \frac{3^{2(x + 2)}}{3^5} = 3^{2x - 1}\). '
                        r'[DM1] Equate exponents: \(6x - 3 = 2x - 1 \Rightarrow 4x = 2\). '
                        r'[A1] \(x = \frac{1}{2}\). '
                        r'| Ghi chú: Đưa tất cả về cùng cơ số \(3\) rồi áp dụng quy tắc số mũ.'
                    ),
                },
                {
                    'id': 'p12_q2b',
                    'type': 'long_answer',
                    'label': r'(b) Solve the equation \(2x - \sqrt{75} = x\sqrt{3} - 4\), giving your answer in the form \(a + b\sqrt{3}\), where \(a\) and \(b\) are integers.',
                    'max_marks': 4,
                    'marking_scheme': (
                        r'[B1] Simplify \(\sqrt{75} = 5\sqrt{3}\). '
                        r'[M1] Collect \(x\)-terms: \(x(2 - \sqrt{3}) = 5\sqrt{3} - 4 \Rightarrow x = \frac{5\sqrt{3} - 4}{2 - \sqrt{3}}\). '
                        r'[DM1] Rationalise denominator: \(\frac{(5\sqrt{3} - 4)(2 + \sqrt{3})}{4 - 3} = 10\sqrt{3} + 15 - 8 - 4\sqrt{3}\). '
                        r'[A1] \(x = 7 + 6\sqrt{3}\). '
                        r'| Ghi chú: Mẫu số \((2 - \sqrt{3})(2 + \sqrt{3}) = 4 - 3 = 1\) giúp rút gọn trực tiếp.'
                    ),
                },
            ],
        },
        {
            'question_number': 3,
            'stem': r'Do not use a calculator in this question.',
            'sub_questions': [
                {
                    'id': 'p12_q3a',
                    'type': 'long_answer',
                    'label': r'(a) Solve the cubic inequality \((x + 3)(2x - 1)(x - 4) \leq 0\).',
                    'max_marks': 3,
                    'marking_scheme': (
                        r'[B1] Identify critical values \(x = -3, \; \frac{1}{2}, \; 4\) and positive cubic end-behaviour. '
                        r'[A1] \(x \leq -3\). '
                        r'[A1] \(\frac{1}{2} \leq x \leq 4\). '
                        r'| Ghi chú: Xét dấu đa thức bậc ba có hệ số đầu dương trên 4 khoảng tạo bởi 3 nghiệm.'
                    ),
                },
                {
                    'id': 'p12_q3b',
                    'type': 'long_answer',
                    'label': r'(b) Solve the modulus inequality \(|2x - 1| < |x + 4|\).',
                    'max_marks': 4,
                    'marking_scheme': (
                        r'[M1] Both sides are non-negative, so square both sides: \((2x - 1)^2 < (x + 4)^2\). '
                        r'[DM1] Expand and rearrange: \(4x^2 - 4x + 1 < x^2 + 8x + 16 \Rightarrow 3x^2 - 12x - 15 < 0 \Rightarrow x^2 - 4x - 5 < 0\). '
                        r'[A1] Factorise \((x - 5)(x + 1) < 0\), critical values \(x = -1\) and \(x = 5\). '
                        r'[A1] \(-1 < x < 5\). '
                        r'| Ghi chú: Hai vế đều không âm nên bình phương tương đương, sau đó giải bất phương trình bậc hai.'
                    ),
                },
            ],
        },
        {
            'question_number': 4,
            'stem': r'Do not use a calculator in this question.',
            'sub_questions': [
                {
                    'id': 'p12_q4a',
                    'type': 'long_answer',
                    'label': r'(a) An arithmetic progression has first term \(a\) and common difference \(d\). The 5th term is \(19\) and the sum of the first 10 terms is \(210\). Find the value of \(a\), the value of \(d\), and the 20th term.',
                    'max_marks': 4,
                    'marking_scheme': (
                        r'[M1] Form equations: \(a + 4d = 19\) and \(S_{10} = \frac{10}{2}(2a + 9d) = 210 \Rightarrow 2a + 9d = 42\). '
                        r'[DM1] Solve simultaneously: \((2a + 9d) - 2(a + 4d) = 42 - 38 \Rightarrow d = 4\). '
                        r'[A1] \(a = 3\) and \(d = 4\). '
                        r'[A1] \(u_{20} = 3 + 19(4) = 79\). '
                        r'| Ghi chú: Dùng \(u_n = a + (n - 1)d\) và \(S_n = \frac{n}{2}[2a + (n - 1)d]\).'
                    ),
                },
                {
                    'id': 'p12_q4b',
                    'type': 'long_answer',
                    'label': r'(b) The first three terms of a geometric progression are \(k + 10\), \(k + 4\) and \(k\), where \(k \neq 0\). Find the value of \(k\), the common ratio \(r\), and the sum to infinity \(S_{\infty}\) of this progression.',
                    'max_marks': 5,
                    'marking_scheme': (
                        r'[M1] Equate common ratios: \(\frac{k + 4}{k + 10} = \frac{k}{k + 4}\), so \((k + 4)^2 = k(k + 10)\). '
                        r'[DM1] Expand: \(k^2 + 8k + 16 = k^2 + 10k \Rightarrow 2k = 16\). '
                        r'[A1] \(k = 8\). '
                        r'[A1] First term \(a = 18\) and common ratio \(r = \frac{12}{18} = \frac{2}{3}\). '
                        r'[A1] Since \(|r| < 1\), \(S_{\infty} = \frac{18}{1 - \frac{2}{3}} = 54\). '
                        r'| Ghi chú: Tính chất 3 số hạng liên tiếp của cấp số nhân: \(u_2^2 = u_1 u_3\); điều kiện hội tụ \(|r| < 1\).'
                    ),
                },
            ],
        },
        {
            'question_number': 5,
            'stem': r'A circle \(C\) has centre \(A(-2, 5)\) and passes through the point \(B(4, -3)\).',
            'sub_questions': [
                {
                    'id': 'p12_q5a',
                    'type': 'short_answer',
                    'label': r'(a) Find the equation of the circle \(C\) in the form \((x - a)^2 + (y - b)^2 = r^2\).',
                    'max_marks': 2,
                    'marking_scheme': (
                        r'[M1] Radius squared \(r^2 = (4 - (-2))^2 + (-3 - 5)^2 = 36 + 64 = 100\) (\(r = 10\)). '
                        r'[A1] \((x + 2)^2 + (y - 5)^2 = 100\). '
                        r'| Ghi chú: Chuyên đề mới 2025–2027 (Circle); kiểm tra dấu của tọa độ tâm \((-2, 5)\).'
                    ),
                },
                {
                    'id': 'p12_q5b',
                    'type': 'long_answer',
                    'label': r'(b) The line \(y = 2x - 1\) intersects the circle \(C\) at the points \(P\) and \(Q\), where \(P\) has the greater \(x\)-coordinate. Find the coordinates of \(P\) and \(Q\).',
                    'max_marks': 4,
                    'marking_scheme': (
                        r'[M1] Substitute \(y = 2x - 1\) into \(C\): \((x + 2)^2 + (2x - 6)^2 = 100\). '
                        r'[A1] Expand and simplify: \(5x^2 - 20x - 60 = 0 \Rightarrow x^2 - 4x - 12 = 0\). '
                        r'[DM1] Factorise \((x - 6)(x + 2) = 0 \Rightarrow x = 6, \; x = -2\). '
                        r'[A1] \(P(6, 11)\) and \(Q(-2, -5)\). '
                        r'| Ghi chú: Thay \(x\) vào \(y = 2x - 1\) để tìm \(y\); chọn \(P\) có hoành độ lớn hơn.'
                    ),
                },
                {
                    'id': 'p12_q5c',
                    'type': 'long_answer',
                    'label': r'(c) Find the equation of the normal to the circle \(C\) at the point \(P\), giving your answer in the form \(ax + by + c = 0\), where \(a, b\) and \(c\) are integers.',
                    'max_marks': 3,
                    'marking_scheme': (
                        r'[M1] Normal to a circle passes through its centre \(A(-2, 5)\); gradient \(m_{AP} = \frac{11 - 5}{6 - (-2)} = \frac{6}{8} = \frac{3}{4}\). '
                        r'[DM1] Equation through \(P(6, 11)\): \(y - 11 = \frac{3}{4}(x - 6)\). '
                        r'[A1] \(3x - 4y + 26 = 0\). '
                        r'| Ghi chú: Pháp tuyến (normal) của đường tròn tại điểm \(P\) luôn đi qua tâm \(A\) của đường tròn.'
                    ),
                },
            ],
        },
        {
            'question_number': 6,
            'stem': r'A sector \(OAB\) of a circle with centre \(O\) and radius \(6\text{ cm}\) has angle \(\angle AOB = \frac{\pi}{3}\text{ radians}\). The chord \(AB\) divides the sector into triangle \(OAB\) and a minor segment.',
            'sub_questions': [
                {
                    'id': 'p12_q6a',
                    'type': 'long_answer',
                    'label': r'(a) Find the exact perimeter of the minor segment bounded by the chord \(AB\) and the arc \(AB\), giving your answer in the form \(p + q\pi\).',
                    'max_marks': 3,
                    'marking_scheme': (
                        r'[M1] Arc length \(AB = r\theta = 6 \times \frac{\pi}{3} = 2\pi\text{ cm}\). '
                        r'[B1] Since \(OA = OB = 6\) and \(\angle AOB = \frac{\pi}{3}\), \(\triangle OAB\) is equilateral, so chord \(AB = 6\text{ cm}\). '
                        r'[A1] Perimeter \(= 6 + 2\pi\text{ cm}\). '
                        r'| Ghi chú: Hình viên phân (minor segment) gồm cung \(AB\) và dây cung \(AB\).'
                    ),
                },
                {
                    'id': 'p12_q6b',
                    'type': 'long_answer',
                    'label': r'(b) Find the exact area of the minor segment, giving your answer in the form \(a\pi - b\sqrt{3}\text{ cm}^2\), where \(a\) and \(b\) are integers.',
                    'max_marks': 4,
                    'marking_scheme': (
                        r'[M1] Sector area \(= \frac{1}{2}r^2\theta = \frac{1}{2}(6)^2\left(\frac{\pi}{3}\right) = 6\pi\text{ cm}^2\). '
                        r'[M1] Triangle area \(= \frac{1}{2}r^2\sin\theta = \frac{1}{2}(36)\sin\left(\frac{\pi}{3}\right)\). '
                        r'[A1] Triangle area \(= 18 \times \frac{\sqrt{3}}{2} = 9\sqrt{3}\text{ cm}^2\). '
                        r'[A1] Minor segment area \(= 6\pi - 9\sqrt{3}\text{ cm}^2\). '
                        r'| Ghi chú: Ghi nhớ giá trị lượng giác chính xác \(\sin\left(\frac{\pi}{3}\right) = \frac{\sqrt{3}}{2}\).'
                    ),
                },
            ],
        },
        {
            'question_number': 7,
            'stem': r'Do not use a calculator in this question.',
            'sub_questions': [
                {
                    'id': 'p12_q7a',
                    'type': 'long_answer',
                    'label': r'(a) Solve the equation \(\log_{2} x + 2\log_{4}(x - 3) = 2\).',
                    'max_marks': 4,
                    'marking_scheme': (
                        r'[M1] Change base: \(\log_{4}(x - 3) = \frac{\log_{2}(x - 3)}{\log_{2} 4} = \frac{1}{2}\log_{2}(x - 3)\), so \(2\log_{4}(x - 3) = \log_{2}(x - 3)\). '
                        r'[DM1] Combine logs: \(\log_{2}[x(x - 3)] = 2 \Rightarrow x(x - 3) = 4 \Rightarrow x^2 - 3x - 4 = 0\). '
                        r'[A1] Factorise \((x - 4)(x + 1) = 0 \Rightarrow x = 4\) or \(x = -1\). '
                        r'[A1] Reject \(x = -1\) since \(x > 3\), giving \(x = 4\) only. '
                        r'| Ghi chú: Dùng công thức đổi cơ số \(\log_{a^k} b = \frac{1}{k}\log_a b\) và loại nghiệm ngoài miền \(x > 3\).'
                    ),
                },
                {
                    'id': 'p12_q7b',
                    'type': 'long_answer',
                    'label': r'(b) Solve the equation \(\text{e}^{2x} - 5\text{e}^{x} + 6 = 0\), giving your answers in exact logarithmic form.',
                    'max_marks': 3,
                    'marking_scheme': (
                        r'[M1] Factorise as quadratic in \(\text{e}^x\): \((\text{e}^x - 2)(\text{e}^x - 3) = 0\). '
                        r'[A1] \(\text{e}^x = 2\) and \(\text{e}^x = 3\). '
                        r'[A1] \(x = \ln 2\) and \(x = \ln 3\). '
                        r'| Ghi chú: Đề Non-Calculator yêu cầu giữ nguyên dạng chính xác \(\ln 2, \; \ln 3\).'
                    ),
                },
            ],
        },
        {
            'question_number': 8,
            'stem': r'Do not use a calculator in this question.',
            'sub_questions': [
                {
                    'id': 'p12_q8a',
                    'type': 'long_answer',
                    'label': r'(a) Given that \(\tan\theta = -\frac{3}{4}\) and \(\frac{\pi}{2} < \theta < \pi\), find the exact values of \(\sin\theta\) and \(\cos\theta\).',
                    'max_marks': 3,
                    'marking_scheme': (
                        r'[M1] Use \(\sec^2\theta = 1 + \tan^2\theta = 1 + \frac{9}{16} = \frac{25}{16}\) (or 3-4-5 triangle in Quadrant II). '
                        r'[A1] In Quadrant II, \(\cos\theta < 0\), so \(\cos\theta = -\frac{4}{5}\). '
                        r'[A1] \(\sin\theta = \tan\theta\cos\theta = \frac{3}{5}\) (positive in Quadrant II). '
                        r'| Ghi chú: Ở góc phần tư II (\(\frac{\pi}{2} < \theta < \pi\)): \(\sin\theta > 0\) và \(\cos\theta < 0\).'
                    ),
                },
                {
                    'id': 'p12_q8b',
                    'type': 'long_answer',
                    'label': r'(b) Solve the equation \(2\sin^2 x - \cos x - 1 = 0\) for \(0 \leq x \leq 2\pi\), giving your answers as exact multiples of \(\pi\).',
                    'max_marks': 5,
                    'marking_scheme': (
                        r'[M1] Substitute \(\sin^2 x = 1 - \cos^2 x\): \(2(1 - \cos^2 x) - \cos x - 1 = 0 \Rightarrow 2\cos^2 x + \cos x - 1 = 0\). '
                        r'[DM1] Factorise \((2\cos x - 1)(\cos x + 1) = 0\). '
                        r'[A1] \(\cos x = \frac{1}{2}\) and \(\cos x = -1\). '
                        r'[A1] From \(\cos x = \frac{1}{2}\): \(x = \frac{\pi}{3}, \; \frac{5\pi}{3}\). '
                        r'[A1] From \(\cos x = -1\): \(x = \pi\). '
                        r'| Ghi chú: Đổi \(\sin^2 x = 1 - \cos^2 x\) để thu phương trình bậc hai theo \(\cos x\).'
                    ),
                },
            ],
        },
        {
            'question_number': 9,
            'stem': r'A curve has equation \(y = \frac{x^2 + 3}{x - 1}\) for \(x \neq 1\).',
            'sub_questions': [
                {
                    'id': 'p12_q9a',
                    'type': 'long_answer',
                    'label': r'(a) Find \(\frac{dy}{dx}\), giving your answer as a single simplified fraction.',
                    'max_marks': 3,
                    'marking_scheme': (
                        r'[M1] Apply the quotient rule with \(u = x^2 + 3\) and \(v = x - 1\). '
                        r'[A1] \(\frac{\text{d}y}{\text{d}x} = \frac{2x(x - 1) - (x^2 + 3)(1)}{(x - 1)^2}\). '
                        r'[A1] Simplify numerator: \(\frac{\text{d}y}{\text{d}x} = \frac{x^2 - 2x - 3}{(x - 1)^2}\). '
                        r"| Ghi chú: Quy tắc thương \(\frac{u'v - uv'}{v^2}\); giữ nguyên mẫu \((x - 1)^2\)."
                    ),
                },
                {
                    'id': 'p12_q9b',
                    'type': 'long_answer',
                    'label': r'(b) Find the coordinates of the two stationary points on the curve and determine the nature of each stationary point.',
                    'max_marks': 4,
                    'marking_scheme': (
                        r'[M1] Set \(\frac{\text{d}y}{\text{d}x} = 0 \Rightarrow x^2 - 2x - 3 = 0 \Rightarrow (x - 3)(x + 1) = 0\). '
                        r'[A1] Stationary points: \((3, 6)\) and \((-1, -2)\). '
                        r'[DM1] Differentiate again to obtain \(\frac{\text{d}^2y}{\text{d}x^2} = \frac{8}{(x - 1)^3}\) (or perform a sign test on \(\frac{\text{d}y}{\text{d}x}\)). '
                        r'[A1] At \(x = 3\), \(\frac{\text{d}^2y}{\text{d}x^2} = 1 > 0\) (local minimum); at \(x = -1\), \(\frac{\text{d}^2y}{\text{d}x^2} = -1 < 0\) (local maximum). '
                        r'| Ghi chú: Điểm dừng khi \(\frac{\text{d}y}{\text{d}x} = 0\); kiểm tra cực đại/cực tiểu bằng đạo hàm cấp 2.'
                    ),
                },
                {
                    'id': 'p12_q9c',
                    'type': 'long_answer',
                    'label': r'(c) Find the equation of the tangent to the curve at the point where \(x = 2\).',
                    'max_marks': 3,
                    'marking_scheme': (
                        r'[B1] At \(x = 2\): \(y = \frac{2^2 + 3}{2 - 1} = 7\), so point is \((2, 7)\). '
                        r'[M1] Gradient \(m = \frac{2^2 - 2(2) - 3}{(2 - 1)^2} = -3\); form \(y - 7 = -3(x - 2)\). '
                        r'[A1] \(y = -3x + 13\) (accept \(3x + y = 13\)). '
                        r'| Ghi chú: Hệ số góc tiếp tuyến tại \(x = 2\) là giá trị \(\frac{\text{d}y}{\text{d}x}\) tại \(x = 2\).'
                    ),
                },
            ],
        },
        {
            'question_number': 10,
            'stem': r'A particle moves in a straight line so that, \(t\) seconds after passing through a fixed point \(O\), its velocity \(v\text{ m s}^{-1}\) is given by \[v = 3t^2 - 18t + 24.\]',
            'sub_questions': [
                {
                    'id': 'p12_q10a',
                    'type': 'short_answer',
                    'label': r'(a) Find the values of \(t\) when the particle is instantaneously at rest.',
                    'max_marks': 2,
                    'marking_scheme': (
                        r'[M1] Set \(v = 0\): \(3(t^2 - 6t + 8) = 0 \Rightarrow (t - 2)(t - 4) = 0\). '
                        r'[A1] \(t = 2\) and \(t = 4\). '
                        r'| Ghi chú: Vật đứng yên tức thời khi vận tốc \(v = 0\).'
                    ),
                },
                {
                    'id': 'p12_q10b',
                    'type': 'long_answer',
                    'label': r'(b) Find the acceleration of the particle when \(t = 1\), and find the velocity of the particle when its acceleration is zero.',
                    'max_marks': 3,
                    'marking_scheme': (
                        r'[M1] Differentiate: \(a = \frac{\text{d}v}{\text{d}t} = 6t - 18\). '
                        r'[A1] When \(t = 1\), \(a = 6(1) - 18 = -12\text{ m s}^{-2}\). '
                        r'[A1] When \(a = 0\), \(t = 3\), so \(v = 3(9) - 18(3) + 24 = -3\text{ m s}^{-1}\). '
                        r'| Ghi chú: Gia tốc \(a = \frac{\text{d}v}{\text{d}t}\); giữ nguyên dấu âm biểu thị chiều chuyển động.'
                    ),
                },
                {
                    'id': 'p12_q10c',
                    'type': 'long_answer',
                    'label': r'(c) Find an expression for the displacement \(s\text{ m}\) of the particle from \(O\) in terms of \(t\), and hence find the total distance travelled by the particle during the first \(5\) seconds.',
                    'max_marks': 5,
                    'marking_scheme': (
                        r'[M1] Integrate velocity: \(s = \int (3t^2 - 18t + 24)\,\text{d}t = t^3 - 9t^2 + 24t + c\), and apply \(s(0) = 0 \Rightarrow c = 0\). '
                        r'[A1] \(s = t^3 - 9t^2 + 24t\). '
                        r'[M1] Evaluate displacements at turning points and endpoint: \(s(2) = 20\), \(s(4) = 16\), \(s(5) = 20\). '
                        r'[DM1] Split into intervals where velocity keeps constant sign: \(|20 - 0| + |16 - 20| + |20 - 16| = 20 + 4 + 4\). '
                        r'[A1] Total distance \(= 28\text{ m}\). '
                        r'| Ghi chú: Tổng quãng đường PHẢI tách tại các thời điểm đổi chiều \(t = 2\) và \(t = 4\), không lấy trực tiếp \(s(5)\).'
                    ),
                },
            ],
        },
    ],
}

# =============================================================================
# PAPER 3: 0606/21 — Paper 2 (Calculator) Full Mock #1 — EXACTLY 80 MARKS
# Marks: Q1(7) Q2(8) Q3(7) Q4(7) Q5(8) Q6(8) Q7(8) Q8(8) Q9(9) Q10(10) = 80
# =============================================================================
PAPER_0606_21 = {
    'code': 'm0606_p2_1',
    'pdf_rel_path': 'papers/igcse-maths/0606_p2_calc_mock1.pdf',
    'order_index': 103,
    'paper_meta': {
        'code': '0606/21',
        'title': '🧮 0606/21 Paper 2 (Calculator) Full Mock #1 [2025–2027]',
        'syllabus': '0606',
        'syllabus_name': 'Cambridge IGCSE Additional Mathematics (0606) — Paper 2 Calculator',
        'course_id': COURSE_0606_ID,
        'time_limit': 120,
        'calculator_policy': 'calculator',
    },
    'questions': [
        {
            'question_number': 1,
            'stem': r'The variables \(x\) and \(y\) are related by the equation \(y = A b^x\), where \(A\) and \(b\) are positive constants. When \(\ln y\) is plotted against \(x\), a straight line is obtained passing through the points \((2, 1.8)\) and \((7, 4.3)\).',
            'sub_questions': [
                {
                    'id': 'p21_q1a',
                    'type': 'long_answer',
                    'label': r'(a) Find the value of \(A\) and the value of \(b\), giving each answer correct to 3 significant figures.',
                    'max_marks': 5,
                    'marking_scheme': (
                        r'[M1] Linearise the relation: \(\ln y = \ln A + (\ln b)x\). '
                        r'[M1] Gradient \(\ln b = \frac{4.3 - 1.8}{7 - 2} = \frac{2.5}{5} = 0.5\). '
                        r'[A1] \(b = \text{e}^{0.5} = 1.65\) (3 s.f.). '
                        r'[M1] Vertical intercept \(\ln A = 1.8 - 0.5(2) = 0.8\). '
                        r'[A1] \(A = \text{e}^{0.8} = 2.23\) (3 s.f.). '
                        r'| Ghi chú: Với đồ thị \(\ln y\) theo \(x\), hệ số góc là \(\ln b\) và tung độ gốc là \(\ln A\).'
                    ),
                },
                {
                    'id': 'p21_q1b',
                    'type': 'short_answer',
                    'label': r'(b) Find the value of \(x\) when \(y = 50\), giving your answer correct to 3 significant figures.',
                    'max_marks': 2,
                    'marking_scheme': (
                        r'[M1] Use exact linear equation: \(\ln 50 = 0.8 + 0.5x \Rightarrow x = 2(\ln 50 - 0.8)\). '
                        r'[A1] \(x = 6.22\) (3 s.f.). '
                        r'| Ghi chú: Dùng giá trị chính xác \(\ln A = 0.8, \; \ln b = 0.5\) để tránh sai số làm tròn trung gian.'
                    ),
                },
            ],
        },
        {
            'question_number': 2,
            'stem': r'Use permutations and combinations to answer each part of this question.',
            'sub_questions': [
                {
                    'id': 'p21_q2a',
                    'type': 'long_answer',
                    'label': r'(a) How many different 5-digit even numbers greater than \(40\,000\) can be formed using the digits \(1, 2, 3, 4, 5, 6, 7\) if no digit may be repeated?',
                    'max_marks': 4,
                    'marking_scheme': (
                        r'[M1] Split into two disjoint cases based on the parity of the first digit (chosen from \(\{4, 5, 6, 7\}\)). '
                        r'[A1] Case 1 (first digit even, \(4\) or \(6\)): \(2 \times 2 \times {}^5\text{P}_3 = 2 \times 2 \times 60 = 240\). '
                        r'[A1] Case 2 (first digit odd, \(5\) or \(7\)): \(2 \times 3 \times {}^5\text{P}_3 = 2 \times 3 \times 60 = 360\). '
                        r'[A1] Total \(= 240 + 360 = 600\). '
                        r'| Ghi chú: Bắt buộc chia 2 trường hợp vì chữ số đầu và cuối đều liên quan đến tập chữ số chẵn \(\{2, 4, 6\}\).'
                    ),
                },
                {
                    'id': 'p21_q2bi',
                    'type': 'short_answer',
                    'label': r'(b) A school committee of \(6\) students is to be chosen from \(5\) boys and \(7\) girls.' + '\n' + r'(i) Find the number of different committees that contain at least \(4\) girls.',
                    'max_marks': 2,
                    'marking_scheme': (
                        r'[M1] Sum valid cases (4G 2B, 5G 1B, 6G 0B): \(\binom{7}{4}\binom{5}{2} + \binom{7}{5}\binom{5}{1} + \binom{7}{6}\binom{5}{0}\). '
                        r'[A1] \(35(10) + 21(5) + 7(1) = 350 + 105 + 7 = 462\). '
                        r'| Ghi chú: "At least 4 girls" gồm 3 trường hợp rời nhau: 4, 5 hoặc 6 nữ.'
                    ),
                },
                {
                    'id': 'p21_q2bii',
                    'type': 'short_answer',
                    'label': r'(ii) Find the number of different committees of \(6\) students that can be chosen from the \(12\) students if two particular girls refuse to serve on the committee together.',
                    'max_marks': 2,
                    'marking_scheme': (
                        r'[M1] Complement method: total committees \(\binom{12}{6}\) minus committees containing both particular girls \(\binom{10}{4}\). '
                        r'[A1] \(924 - 210 = 714\). '
                        r'| Ghi chú: Dùng phần bù: Tổng số cách chọn trừ đi số cách mà cả 2 bạn nữ cùng được chọn.'
                    ),
                },
            ],
        },
        {
            'question_number': 3,
            'stem': r'A circle with centre \(O\) has radius \(9\text{ cm}\). Points \(A\) and \(B\) lie on the circumference such that the chord \(AB\) has length \(14\text{ cm}\).',
            'sub_questions': [
                {
                    'id': 'p21_q3a',
                    'type': 'short_answer',
                    'label': r'(a) Show that \(\angle AOB = 1.782\text{ radians}\), correct to 3 decimal places.',
                    'max_marks': 2,
                    'marking_scheme': (
                        r'[M1] Cosine rule \(\cos\theta = \frac{9^2 + 9^2 - 14^2}{2(9)(9)} = -\frac{17}{81}\), or right triangle \(\sin\left(\frac{\theta}{2}\right) = \frac{7}{9}\). '
                        r'[A1] \(\theta = 1.782245\dots = 1.782\text{ rad}\) (3 d.p., AG). '
                        r'| Ghi chú: Đảm bảo máy tính ở chế độ RAD khi bấm \(\arccos\) hoặc \(\arcsin\).'
                    ),
                },
                {
                    'id': 'p21_q3b',
                    'type': 'short_answer',
                    'label': r'(b) Find the perimeter of the minor segment bounded by the chord \(AB\) and the minor arc \(AB\), giving your answer correct to 3 significant figures.',
                    'max_marks': 2,
                    'marking_scheme': (
                        r'[M1] Perimeter \(= AB + r\theta = 14 + 9(1.782245)\). '
                        r'[A1] \(30.040\dots = 30.0\text{ cm}\) (3 s.f.). '
                        r'| Ghi chú: Chu vi viên phân \(= \text{dây cung} + \text{độ dài cung}\); viết đủ \(30.0\) cho 3 s.f.'
                    ),
                },
                {
                    'id': 'p21_q3c',
                    'type': 'long_answer',
                    'label': r'(c) Find the area of the minor segment, giving your answer correct to 3 significant figures.',
                    'max_marks': 3,
                    'marking_scheme': (
                        r'[M1] Sector area \(= \frac{1}{2}(9)^2(1.782245) = 72.1809\text{ cm}^2\). '
                        r'[M1] Triangle area \(= \frac{1}{2}(9)^2\sin(1.782245) = 39.5980\text{ cm}^2\). '
                        r'[A1] Segment area \(= 72.1809 - 39.5980 = 32.5829\dots = 32.6\text{ cm}^2\) (3 s.f.). '
                        r'| Ghi chú: Diện tích viên phân \(= \frac{1}{2}r^2(\theta - \sin\theta)\).'
                    ),
                },
            ],
        },
        {
            'question_number': 4,
            'stem': r'Give all non-exact numerical answers in this question correct to 3 significant figures.',
            'sub_questions': [
                {
                    'id': 'p21_q4a',
                    'type': 'long_answer',
                    'label': r'(a) Solve the equation \(3^{2x - 1} = 5^{x + 2}\).',
                    'max_marks': 3,
                    'marking_scheme': (
                        r'[M1] Take logarithms of both sides: \((2x - 1)\ln 3 = (x + 2)\ln 5\). '
                        r'[DM1] Collect \(x\)-terms: \(x(2\ln 3 - \ln 5) = 2\ln 5 + \ln 3 \Rightarrow x = \frac{2\ln 5 + \ln 3}{2\ln 3 - \ln 5}\). '
                        r'[A1] \(x = 7.3453\dots = 7.35\) (3 s.f.). '
                        r'| Ghi chú: Lấy \(\ln\) (hoặc \(\log_{10}\)) hai vế rồi chuyển tất cả hạng tử chứa \(x\) về một vế.'
                    ),
                },
                {
                    'id': 'p21_q4b',
                    'type': 'long_answer',
                    'label': r'(b) Solve the equation \(2\text{e}^{2x} - 7\text{e}^{x} + 4 = 0\).',
                    'max_marks': 4,
                    'marking_scheme': (
                        r'[M1] Let \(u = \text{e}^x > 0\) and apply the quadratic formula to \(2u^2 - 7u + 4 = 0\). '
                        r'[A1] \(u = \frac{7 \pm \sqrt{17}}{4} \approx 2.7808\) and \(0.71922\) (both positive). '
                        r'[DM1] Take natural logarithms: \(x = \ln(2.7808)\) and \(x = \ln(0.71922)\). '
                        r'[A1] \(x = 1.02\) and \(x = -0.330\) (3 s.f.). '
                        r'| Ghi chú: Lưu giữ đầy đủ chữ số trong máy tính khi bấm \(\ln\) để đạt chính xác 3 s.f. (`-0.330`).'
                    ),
                },
            ],
        },
        {
            'question_number': 5,
            'stem': r'Show full working for each trigonometric equation.',
            'sub_questions': [
                {
                    'id': 'p21_q5a',
                    'type': 'long_answer',
                    'label': r'(a) Solve the equation \(2\sec^2 x - 5\tan x - 5 = 0\) for \(0^\circ \leq x \leq 360^\circ\), giving your answers correct to 1 decimal place.',
                    'max_marks': 4,
                    'marking_scheme': (
                        r'[M1] Substitute \(\sec^2 x = 1 + \tan^2 x\) to obtain \(2\tan^2 x - 5\tan x - 3 = 0\). '
                        r'[DM1] Factorise \((2\tan x + 1)(\tan x - 3) = 0 \Rightarrow \tan x = 3\) or \(\tan x = -\frac{1}{2}\). '
                        r'[A1] From \(\tan x = 3\): \(x = 71.6^\circ, \; 251.6^\circ\) (1 d.p.). '
                        r'[A1] From \(\tan x = -\frac{1}{2}\): \(x = 153.4^\circ, \; 333.4^\circ\) (1 d.p.). '
                        r'| Ghi chú: Góc theo độ làm tròn 1 chữ số thập phân (1 d.p.); \(\tan x\) có chu kỳ \(180^\circ\).'
                    ),
                },
                {
                    'id': 'p21_q5b',
                    'type': 'long_answer',
                    'label': r'(b) Solve the equation \(3\text{cosec}^2 y - 5\cot y - 5 = 0\) for \(0 \leq y \leq \pi\), giving your answers correct to 3 significant figures.',
                    'max_marks': 4,
                    'marking_scheme': (
                        r'[M1] Substitute \(\text{cosec}^2 y = 1 + \cot^2 y\) to obtain \(3\cot^2 y - 5\cot y - 2 = 0\). '
                        r'[DM1] Factorise \((3\cot y + 1)(\cot y - 2) = 0 \Rightarrow \tan y = \frac{1}{2}\) or \(\tan y = -3\). '
                        r'[A1] From \(\tan y = \frac{1}{2}\): \(y = 0.464\text{ rad}\) (3 s.f.). '
                        r'[A1] From \(\tan y = -3\): \(y = \pi - \arctan(3) = 1.89\text{ rad}\) (3 s.f.). '
                        r'| Ghi chú: Chuyển sang chế độ RAD và đổi \(\cot y = k \Leftrightarrow \tan y = \frac{1}{k}\).'
                    ),
                },
            ],
        },
        {
            'question_number': 6,
            'stem': r'The circle \(C\) has equation \(x^2 + y^2 - 8x + 4y - 5 = 0\). The straight line \(L\) with equation \(y = 2x - 3\) intersects \(C\) at the points \(A\) and \(B\), where \(A\) has the positive \(x\)-coordinate.',
            'sub_questions': [
                {
                    'id': 'p21_q6a',
                    'type': 'short_answer',
                    'label': r'(a) Find the coordinates of the centre \(M\) and the radius of the circle \(C\).',
                    'max_marks': 2,
                    'marking_scheme': (
                        r'[M1] Complete the square: \((x - 4)^2 - 16 + (y + 2)^2 - 4 - 5 = 0 \Rightarrow (x - 4)^2 + (y + 2)^2 = 25\). '
                        r'[A1] Centre \(M(4, -2)\), radius \(r = 5\). '
                        r'| Ghi chú: Chuyên đề mới 2025–2027 (Circle).'
                    ),
                },
                {
                    'id': 'p21_q6b',
                    'type': 'long_answer',
                    'label': r'(b) Find the coordinates of \(A\) and \(B\), giving your answers correct to 3 significant figures.',
                    'max_marks': 4,
                    'marking_scheme': (
                        r'[M1] Substitute \(y = 2x - 3\) into \(C\): \((x - 4)^2 + (2x - 1)^2 = 25\). '
                        r'[A1] Expand and simplify to \(5x^2 - 12x - 8 = 0\). '
                        r'[DM1] Solve by quadratic formula: \(x = \frac{12 \pm \sqrt{304}}{10} = \frac{6 \pm 2\sqrt{19}}{5}\) (\(2.9436\) and \(-0.54356\)). '
                        r'[A1] \(A(2.94, 2.89)\) and \(B(-0.544, -4.09)\) (3 s.f.). '
                        r'| Ghi chú: Dùng giá trị \(x\) chưa làm tròn khi tính \(y = 2x - 3\).'
                    ),
                },
                {
                    'id': 'p21_q6c',
                    'type': 'short_answer',
                    'label': r'(c) Find the length of the chord \(AB\), giving your answer correct to 3 significant figures.',
                    'max_marks': 2,
                    'marking_scheme': (
                        r'[M1] Distance formula \(AB = \sqrt{(x_A - x_B)^2 + (y_A - y_B)^2} = \frac{4\sqrt{95}}{5}\) (or \(2\sqrt{r^2 - d^2} = 2\sqrt{25 - \frac{49}{5}}\)). '
                        r'[A1] \(AB = 7.7974\dots = 7.80\) (3 s.f.). '
                        r'| Ghi chú: Có thể kiểm chứng chéo bằng định lý Pythagoras với khoảng cách từ tâm \(M\) đến đường thẳng \(L\).'
                    ),
                },
            ],
        },
        {
            'question_number': 7,
            'stem': r'Use differentiation to answer both parts of this question.',
            'sub_questions': [
                {
                    'id': 'p21_q7a',
                    'type': 'long_answer',
                    'label': r'(a) Water is poured into an inverted right circular cone of base radius \(6\text{ cm}\) and vertical height \(18\text{ cm}\) at a constant rate of \(12\text{ cm}^3\text{ s}^{-1}\). Find the rate at which the depth of water \(h\text{ cm}\) is increasing when \(h = 9\text{ cm}\), giving your answer correct to 3 significant figures.',
                    'max_marks': 5,
                    'marking_scheme': (
                        r'[B1] By similar triangles, \(\frac{r}{h} = \frac{6}{18} \Rightarrow r = \frac{h}{3}\). '
                        r'[A1] Volume \(V = \frac{1}{3}\pi r^2 h = \frac{1}{3}\pi\left(\frac{h}{3}\right)^2 h = \frac{\pi h^3}{27}\). '
                        r'[M1] Differentiate with respect to \(h\): \(\frac{\text{d}V}{\text{d}h} = \frac{\pi h^2}{9}\). '
                        r'[DM1] Connected rates: \(\frac{\text{d}h}{\text{d}t} = \frac{\text{d}V/\text{d}t}{\text{d}V/\text{d}h} = \frac{12}{\frac{\pi(9)^2}{9}} = \frac{12}{9\pi} = \frac{4}{3\pi}\). '
                        r'[A1] \(\frac{\text{d}h}{\text{d}t} = 0.424\text{ cm s}^{-1}\) (3 s.f.). '
                        r'| Ghi chú: Biểu diễn \(V\) chỉ theo một biến \(h\) trước khi lấy đạo hàm \(\frac{\text{d}V}{\text{d}h}\).'
                    ),
                },
                {
                    'id': 'p21_q7b',
                    'type': 'long_answer',
                    'label': r'(b) Given that \(y = \ln(3x - 2)\), use differentiation to find the approximate change in \(y\) as \(x\) increases from \(4\) to \(4 + p\), where \(p\) is small.',
                    'max_marks': 3,
                    'marking_scheme': (
                        r'[M1] Differentiate: \(\frac{\text{d}y}{\text{d}x} = \frac{3}{3x - 2}\). '
                        r'[A1] At \(x = 4\): \(\frac{\text{d}y}{\text{d}x} = \frac{3}{10} = 0.3\). '
                        r'[A1] \(\delta y \approx \frac{\text{d}y}{\text{d}x}\delta x = 0.3p\). '
                        r'| Ghi chú: Công thức số gia nhỏ (Small Changes): \(\delta y \approx \frac{\text{d}y}{\text{d}x}\big|_{x=4} \cdot \delta x\).'
                    ),
                },
            ],
        },
        {
            'question_number': 8,
            'stem': r'Show clearly how logarithms or inequalities are used in each part.',
            'sub_questions': [
                {
                    'id': 'p21_q8a',
                    'type': 'long_answer',
                    'label': r'(a) A geometric progression has first term \(120\) and common ratio \(0.85\). Find the least integer value of \(n\) such that the sum of the first \(n\) terms exceeds \(720\).',
                    'max_marks': 4,
                    'marking_scheme': (
                        r'[M1] Set up GP sum inequality: \(\frac{120(1 - 0.85^n)}{1 - 0.85} > 720 \Rightarrow 800(1 - 0.85^n) > 720\). '
                        r'[A1] Rearrange to \(1 - 0.85^n > 0.9 \Rightarrow 0.85^n < 0.1\). '
                        r'[DM1] Take logs (reversing inequality since \(\ln 0.85 < 0\)): \(n > \frac{\ln 0.1}{\ln 0.85} = 14.168\dots\). '
                        r'[A1] Least integer \(n = 15\). '
                        r'| Ghi chú: Lưu ý đổi chiều bất đẳng thức khi chia cho \(\ln(0.85) < 0\).'
                    ),
                },
                {
                    'id': 'p21_q8b',
                    'type': 'long_answer',
                    'label': r'(b) An arithmetic progression has first term \(7\) and common difference \(3.5\). Find the least integer value of \(n\) such that the sum of the first \(n\) terms exceeds \(1000\).',
                    'max_marks': 4,
                    'marking_scheme': (
                        r'[M1] Set up AP sum inequality: \(\frac{n}{2}[14 + 3.5(n - 1)] > 1000\). '
                        r'[A1] Simplify to \(1.75n^2 + 5.25n - 1000 > 0\) (or \(7n^2 + 21n - 4000 > 0\)). '
                        r'[DM1] Solve positive root: \(n > \frac{-21 + \sqrt{21^2 + 4(7)(4000)}}{14} = 22.45\dots\). '
                        r'[A1] Least integer \(n = 23\). '
                        r'| Ghi chú: Kiểm tra lại \(S_{22} = 962.5 < 1000\) và \(S_{23} = 1046.5 > 1000\).'
                    ),
                },
            ],
        },
        {
            'question_number': 9,
            'stem': r'The curve \(y = \frac{12}{x}\) (\(x > 0\)) and the straight line \(y = 8 - x\) intersect at the points \(P\) and \(Q\), where \(P\) has the smaller \(x\)-coordinate.',
            'sub_questions': [
                {
                    'id': 'p21_q9a',
                    'type': 'long_answer',
                    'label': r'(a) Find the coordinates of \(P\) and \(Q\).',
                    'max_marks': 3,
                    'marking_scheme': (
                        r'[M1] Equate \(\frac{12}{x} = 8 - x \Rightarrow x^2 - 8x + 12 = 0\). '
                        r'[DM1] Factorise \((x - 2)(x - 6) = 0 \Rightarrow x = 2, \; x = 6\). '
                        r'[A1] \(P(2, 6)\) and \(Q(6, 2)\). '
                        r'| Ghi chú: Xác định giao điểm trước khi đặt cận tích phân.'
                    ),
                },
                {
                    'id': 'p21_q9b',
                    'type': 'long_answer',
                    'label': r'(b) Find the area of the region enclosed between the curve \(y = \frac{12}{x}\) and the line \(y = 8 - x\), giving your answer first in the exact form \(a - b\ln 3\) and then correct to 3 significant figures.',
                    'max_marks': 6,
                    'marking_scheme': (
                        r'[M1] Note line lies above curve on \([2, 6]\) and form \(\text{Area} = \int_{2}^{6} \left(8 - x - \frac{12}{x}\right)\,\text{d}x\) (or trapezium minus integral of curve). '
                        r'[A1] Integrate polynomial part: \(\left[8x - \frac{1}{2}x^2\right]_{2}^{6} = (48 - 18) - (16 - 2) = 16\) (or trapezium \(\frac{1}{2}(6 + 2)(4) = 16\)). '
                        r'[A1] Integrate reciprocal part: \(\int \frac{12}{x}\,\text{d}x = 12\ln x\). '
                        r'[DM1] Apply limits \(6\) and \(2\): \(16 - (12\ln 6 - 12\ln 2) = 16 - 12\ln\left(\frac{6}{2}\right)\). '
                        r'[A1] Exact area \(= 16 - 12\ln 3\). '
                        r'[A1] Numerical area \(= 2.81665\dots = 2.82\) (3 s.f.). '
                        r'| Ghi chú: Dùng quy tắc \(\ln 6 - \ln 2 = \ln 3\) để đưa về đúng dạng đề yêu cầu.'
                    ),
                },
            ],
        },
        {
            'question_number': 10,
            'stem': r'A particle moves in a straight line such that, \(t\) seconds after leaving a fixed point \(O\), its velocity \(v\text{ m s}^{-1}\) is given by \[v = 10\text{e}^{-0.2t} - 4.\]',
            'sub_questions': [
                {
                    'id': 'p21_q10a',
                    'type': 'long_answer',
                    'label': r'(a) Find the value of \(t\) when the particle is instantaneously at rest, giving your answer correct to 3 significant figures, and find the exact acceleration of the particle at this instant.',
                    'max_marks': 3,
                    'marking_scheme': (
                        r'[M1] Set \(10\text{e}^{-0.2t} - 4 = 0 \Rightarrow \text{e}^{-0.2t} = 0.4 \Rightarrow t = 5\ln(2.5)\). '
                        r'[A1] \(t = 4.5815\dots = 4.58\text{ s}\) (3 s.f.). '
                        r'[A1] Differentiate \(a = \frac{\text{d}v}{\text{d}t} = -2\text{e}^{-0.2t}\); substituting \(\text{e}^{-0.2t} = 0.4\) gives \(a = -0.8\text{ m s}^{-2}\). '
                        r'| Ghi chú: Thay thẳng \(\text{e}^{-0.2t} = 0.4\) vào \(a = -2\text{e}^{-0.2t}\) cho kết quả chính xác \(-0.8\text{ m s}^{-2}\).'
                    ),
                },
                {
                    'id': 'p21_q10b',
                    'type': 'long_answer',
                    'label': r'(b) Find an expression for the displacement \(s\text{ m}\) of the particle from \(O\) at time \(t\).',
                    'max_marks': 3,
                    'marking_scheme': (
                        r'[M1] Integrate: \(s = \int (10\text{e}^{-0.2t} - 4)\,\text{d}t = -50\text{e}^{-0.2t} - 4t + c\). '
                        r'[DM1] Use initial condition \(t = 0, \; s = 0\): \(-50(1) - 0 + c = 0 \Rightarrow c = 50\). '
                        r'[A1] \(s = 50 - 50\text{e}^{-0.2t} - 4t\). '
                        r'| Ghi chú: Nhớ chia cho hệ số \(-0.2\) khi nguyên hàm \(\text{e}^{-0.2t}\) và tìm hằng số \(c\) từ \(s(0) = 0\).'
                    ),
                },
                {
                    'id': 'p21_q10c',
                    'type': 'long_answer',
                    'label': r'(c) Find the total distance travelled by the particle during the first \(10\) seconds, giving your answer correct to 3 significant figures.',
                    'max_marks': 4,
                    'marking_scheme': (
                        r'[M1] Displacement at turning point \(T = 5\ln(2.5)\): \(s(T) = 50 - 50(0.4) - 20\ln(2.5) = 30 - 20\ln(2.5) \approx 11.6742\text{ m}\). '
                        r'[M1] Displacement at \(t = 10\): \(s(10) = 50 - 50\text{e}^{-2} - 40 = 10 - 50\text{e}^{-2} \approx 3.2332\text{ m}\). '
                        r'[DM1] Since velocity changes sign at \(t = T\): total distance \(= s(T) + [s(T) - s(10)] = 2(11.6742) - 3.2332\). '
                        r'[A1] Total distance \(= 20.115\dots = 20.1\text{ m}\) (3 s.f.). '
                        r'| Ghi chú: Vật tiến từ \(0\) đến \(11.674\text{ m}\) rồi lùi về \(3.233\text{ m}\), nên cộng hai đoạn đường lại.'
                    ),
                },
            ],
        },
    ],
}

# =============================================================================
# PAPER 4: 0606/22 — Paper 2 (Calculator) Full Mock #2 — EXACTLY 80 MARKS
# Marks: Q1(6) Q2(7) Q3(8) Q4(7) Q5(8) Q6(8) Q7(8) Q8(8) Q9(10) Q10(10) = 80
# =============================================================================
PAPER_0606_22 = {
    'code': 'm0606_p2_2',
    'pdf_rel_path': 'papers/igcse-maths/0606_p2_calc_mock2.pdf',
    'order_index': 104,
    'paper_meta': {
        'code': '0606/22',
        'title': '🧮 0606/22 Paper 2 (Calculator) Full Mock #2 [2025–2027]',
        'syllabus': '0606',
        'syllabus_name': 'Cambridge IGCSE Additional Mathematics (0606) — Paper 2 Calculator',
        'course_id': COURSE_0606_ID,
        'time_limit': 120,
        'calculator_policy': 'calculator',
    },
    'questions': [
        {
            'question_number': 1,
            'stem': r'Show full algebraic working in both parts of this question.',
            'sub_questions': [
                {
                    'id': 'p22_q1a',
                    'type': 'long_answer',
                    'label': r'(a) Express \(3x^2 - 12x + 17\) in the form \(a(x + b)^2 + c\), where \(a, b\) and \(c\) are integers, and state the coordinates of the minimum point of the curve \(y = 3x^2 - 12x + 17\).',
                    'max_marks': 3,
                    'marking_scheme': (
                        r'[M1] Factor out \(3\) and complete the square: \(3(x^2 - 4x) + 17 = 3[(x - 2)^2 - 4] + 17\). '
                        r'[A1] \(3(x - 2)^2 + 5\) (\(a = 3, \; b = -2, \; c = 5\)). '
                        r'[B1] Minimum point is \((2, 5)\). '
                        r'| Ghi chú: Chú ý nhân hệ số \(3\) với \(-4\) khi đưa ra ngoài ngoặc.'
                    ),
                },
                {
                    'id': 'p22_q1b',
                    'type': 'long_answer',
                    'label': r'(b) Solve the equation \(2x^{2/3} - 7x^{1/3} + 3 = 0\).',
                    'max_marks': 3,
                    'marking_scheme': (
                        r'[M1] Substitute \(u = x^{1/3}\) to form \(2u^2 - 7u + 3 = 0\) and factorise \((2u - 1)(u - 3) = 0\). '
                        r'[A1] \(u = \frac{1}{2}\) and \(u = 3\). '
                        r'[A1] Cube both values: \(x = \frac{1}{8}\) (or \(0.125\)) and \(x = 27\). '
                        r'| Ghi chú: Đặt ẩn phụ \(u = x^{1/3}\), sau khi tìm \(u\) phải lập phương \(x = u^3\).'
                    ),
                },
            ],
        },
        {
            'question_number': 2,
            'stem': r'The variables \(x\) and \(y\) are connected by the relation \(y = k x^n\), where \(k\) and \(n\) are constants. When \(\log_{10} y\) is plotted against \(\log_{10} x\), a straight line is obtained passing through the points \((0.5, 1.35)\) and \((2.5, 4.15)\).',
            'sub_questions': [
                {
                    'id': 'p22_q2a',
                    'type': 'long_answer',
                    'label': r'(a) Find the exact value of \(n\) and the value of \(k\) correct to 3 significant figures.',
                    'max_marks': 5,
                    'marking_scheme': (
                        r'[M1] Linearise: \(\log_{10} y = \log_{10} k + n\log_{10} x\). '
                        r'[M1] Gradient \(n = \frac{4.15 - 1.35}{2.5 - 0.5} = \frac{2.80}{2.0}\). '
                        r'[A1] \(n = 1.4\) (exact). '
                        r'[M1] Vertical intercept \(\log_{10} k = 1.35 - 1.4(0.5) = 0.65\). '
                        r'[A1] \(k = 10^{0.65} = 4.4668\dots = 4.47\) (3 s.f.). '
                        r'| Ghi chú: Với cơ số \(10\), nhớ nghịch đảo \(\log_{10} k = 0.65 \Rightarrow k = 10^{0.65}\), không dùng \(\text{e}^{0.65}\).'
                    ),
                },
                {
                    'id': 'p22_q2b',
                    'type': 'short_answer',
                    'label': r'(b) Find the value of \(y\) when \(x = 12\), giving your answer correct to 3 significant figures.',
                    'max_marks': 2,
                    'marking_scheme': (
                        r'[M1] Substitute \(x = 12\) into \(y = 10^{0.65} \cdot 12^{1.4}\). '
                        r'[A1] \(y = 144.83\dots = 145\) (3 s.f.). '
                        r'| Ghi chú: Cả giá trị \(k\) chính xác lẫn \(4.47\) đều cho kết quả làm tròn \(145\) (3 s.f.).'
                    ),
                },
            ],
        },
        {
            'question_number': 3,
            'stem': (
                r'The functions \(\text{f}\) and \(\text{g}\) are defined by' + '\n'
                + r'\[\text{f}(x) = 3\text{e}^{2x} - 1 \quad \text{for all real values of } x,\]' + '\n'
                + r'\[\text{g}(x) = \ln(x + 4) \quad \text{for } x > -4.\]'
            ),
            'sub_questions': [
                {
                    'id': 'p22_q3a',
                    'type': 'short_answer',
                    'label': r'(a) State the range of \(\text{f}\) and the range of \(\text{g}\).',
                    'max_marks': 2,
                    'marking_scheme': (
                        r'[B1] Range of \(\text{f}\): \(\text{f}(x) > -1\). '
                        r'[B1] Range of \(\text{g}\): all real numbers (accept \(-\infty < \text{g}(x) < \infty\)). '
                        r'| Ghi chú: Vì \(\text{e}^{2x} > 0\) với mọi \(x\) nên \(3\text{e}^{2x} - 1 > -1\) (không có dấu bằng).'
                    ),
                },
                {
                    'id': 'p22_q3b',
                    'type': 'long_answer',
                    'label': r'(b) Find an expression for \(\text{f}^{-1}(x)\) and state its domain.',
                    'max_marks': 3,
                    'marking_scheme': (
                        r'[M1] Rearrange \(y = 3\text{e}^{2x} - 1 \Rightarrow \text{e}^{2x} = \frac{y + 1}{3} \Rightarrow 2x = \ln\left(\frac{y + 1}{3}\right)\). '
                        r'[A1] \(\text{f}^{-1}(x) = \frac{1}{2}\ln\left(\frac{x + 1}{3}\right)\). '
                        r'[B1] Domain of \(\text{f}^{-1}\): \(x > -1\). '
                        r'| Ghi chú: Miền xác định của \(\text{f}^{-1}\) bằng tập giá trị của \(\text{f}\).'
                    ),
                },
                {
                    'id': 'p22_q3c',
                    'type': 'long_answer',
                    'label': r'(c) Solve the equation \(\text{fg}(x) = 20\), giving your answer correct to 3 significant figures.',
                    'max_marks': 3,
                    'marking_scheme': (
                        r'[M1] Form composite function: \(\text{fg}(x) = 3\text{e}^{2\ln(x + 4)} - 1 = 3(x + 4)^2 - 1\). '
                        r'[DM1] Solve \(3(x + 4)^2 - 1 = 20 \Rightarrow (x + 4)^2 = 7 \Rightarrow x = -4 \pm \sqrt{7}\). '
                        r'[A1] Since \(x > -4\), reject \(-4 - \sqrt{7}\), leaving \(x = -4 + \sqrt{7} = -1.35\) (3 s.f.). '
                        r'| Ghi chú: Áp dụng \(\text{e}^{2\ln A} = A^2\) và loại nghiệm nhỏ hơn \(-4\).'
                    ),
                },
            ],
        },
        {
            'question_number': 4,
            'stem': r'Use the Binomial Theorem to answer both parts of this question.',
            'sub_questions': [
                {
                    'id': 'p22_q4a',
                    'type': 'long_answer',
                    'label': r'(a) Find the term independent of \(x\) in the expansion of \(\left(2x^2 - \frac{1}{x}\right)^9\).',
                    'max_marks': 3,
                    'marking_scheme': (
                        r'[M1] General term: \(T_{r + 1} = \binom{9}{r}(2x^2)^{9 - r}(-x^{-1})^r = \binom{9}{r} 2^{9 - r}(-1)^r x^{18 - 3r}\). '
                        r'[A1] Set power of \(x\) to zero: \(18 - 3r = 0 \Rightarrow r = 6\). '
                        r'[A1] Term \(= \binom{9}{6}(2^3)(-1)^6 = 84 \times 8 \times 1 = 672\). '
                        r'| Ghi chú: Số hạng không chứa \(x\) ứng với số mũ của \(x\) bằng \(0\).'
                    ),
                },
                {
                    'id': 'p22_q4b',
                    'type': 'long_answer',
                    'label': r'(b) In the expansion of \((1 + ax)^n\), where \(n\) is a positive integer and \(a \neq 0\), the coefficient of \(x\) is \(24\) and the coefficient of \(x^2\) is \(252\). Find the value of \(n\) and the value of \(a\).',
                    'max_marks': 4,
                    'marking_scheme': (
                        r'[B1] Coefficient of \(x\): \(na = 24\). '
                        r'[B1] Coefficient of \(x^2\): \(\frac{n(n - 1)}{2}a^2 = 252 \Rightarrow n(n - 1)a^2 = 504\). '
                        r'[M1] Substitute \(a = \frac{24}{n}\) (or divide by \((na)^2 = 576\)): \(\frac{n - 1}{n} = \frac{504}{576} = \frac{7}{8}\). '
                        r'[A1] \(n = 8\) and \(a = 3\). '
                        r'| Ghi chú: Chia hai phương trình để khử \(a^2\) rất nhanh và gọn.'
                    ),
                },
            ],
        },
        {
            'question_number': 5,
            'stem': r'Eight distinct books — \(3\) Mathematics books, \(3\) Physics books and \(2\) Chemistry books — are to be arranged in a row on a shelf.',
            'sub_questions': [
                {
                    'id': 'p22_q5ai',
                    'type': 'short_answer',
                    'label': r'(a) (i) Find the number of arrangements in which all \(3\) Mathematics books are next to each other.',
                    'max_marks': 2,
                    'marking_scheme': (
                        r'[M1] Treat the \(3\) Mathematics books as one block: \(6! \times 3!\). '
                        r'[A1] \(720 \times 6 = 4320\). '
                        r'| Ghi chú: Nhớ nhân thêm \(3!\) cho các cách hoán vị nội bộ giữa 3 quyển Toán.'
                    ),
                },
                {
                    'id': 'p22_q5aii',
                    'type': 'long_answer',
                    'label': r'(ii) Find the number of arrangements in which no two Physics books are next to each other.',
                    'max_marks': 3,
                    'marking_scheme': (
                        r'[M1] Arrange the \(5\) non-Physics books first in \(5! = 120\) ways, creating \(6\) gaps. '
                        r'[M1] Place the \(3\) distinct Physics books into \(3\) of the \(6\) gaps in \({}^6\text{P}_3 = 120\) ways. '
                        r'[A1] Total \(= 5! \times {}^6\text{P}_3 = 120 \times 120 = 14\,400\). '
                        r'| Ghi chú: Quy tắc vách ngăn (gap method): không được dùng \(8! - 6! \times 3!\) vì điều đó chỉ loại trường hợp cả 3 quyển dính nhau.'
                    ),
                },
                {
                    'id': 'p22_q5b',
                    'type': 'long_answer',
                    'label': r'(b) A password of \(4\) characters is formed by choosing \(2\) different letters from the \(5\) vowels \(A, E, I, O, U\) and \(2\) different digits from \(1, 2, 3, 4, 5, 6\), and then arranging the \(4\) chosen characters in any order. Find the total number of possible passwords.',
                    'max_marks': 3,
                    'marking_scheme': (
                        r'[M1] Choose \(2\) vowels and \(2\) digits: \(\binom{5}{2} \times \binom{6}{2} = 10 \times 15 = 150\). '
                        r'[DM1] Arrange the \(4\) distinct chosen characters in \(4! = 24\) ways. '
                        r'[A1] Total \(= 150 \times 24 = 3600\). '
                        r'| Ghi chú: Tách rõ hai bước: Chọn tổ hợp (Choose) rồi Sắp xếp hoán vị (Arrange).'
                    ),
                },
            ],
        },
        {
            'question_number': 6,
            'stem': r'The points \(A(-3, 2)\) and \(B(5, 8)\) are the endpoints of a diameter of a circle \(C\).',
            'sub_questions': [
                {
                    'id': 'p22_q6a',
                    'type': 'long_answer',
                    'label': r'(a) Find the equation of the circle \(C\) in the form \((x - a)^2 + (y - b)^2 = r^2\).',
                    'max_marks': 3,
                    'marking_scheme': (
                        r'[B1] Centre \(M\) is the midpoint of \(AB\): \(M\left(\frac{-3 + 5}{2}, \frac{2 + 8}{2}\right) = (1, 5)\). '
                        r'[M1] Radius \(r = MB = \sqrt{(5 - 1)^2 + (8 - 5)^2} = \sqrt{16 + 9} = 5\). '
                        r'[A1] \((x - 1)^2 + (y - 5)^2 = 25\). '
                        r'| Ghi chú: Chuyên đề mới 2025–2027 (Circle): tâm là trung điểm đường kính \(AB\).'
                    ),
                },
                {
                    'id': 'p22_q6b',
                    'type': 'long_answer',
                    'label': r'(b) Find the equation of the tangent to \(C\) at \(B\), giving your answer in the form \(ax + by = c\), where \(a, b\) and \(c\) are integers.',
                    'max_marks': 3,
                    'marking_scheme': (
                        r'[M1] Gradient of radius \(MB = \frac{8 - 5}{5 - 1} = \frac{3}{4}\), so tangent gradient \(m_T = -\frac{4}{3}\). '
                        r'[DM1] Equation through \(B(5, 8)\): \(y - 8 = -\frac{4}{3}(x - 5)\). '
                        r'[A1] \(4x + 3y = 44\). '
                        r'| Ghi chú: Tiếp tuyến tại \(B\) vuông góc với đường kính \(AB\).'
                    ),
                },
                {
                    'id': 'p22_q6c',
                    'type': 'short_answer',
                    'label': r'(c) The tangent at \(B\) meets the \(x\)-axis at \(P\) and the \(y\)-axis at \(Q\). Find the area of triangle \(OPQ\), where \(O\) is the origin.',
                    'max_marks': 2,
                    'marking_scheme': (
                        r'[M1] Intercepts: \(P(11, 0)\) and \(Q\left(0, \frac{44}{3}\right)\). '
                        r'[A1] Area \(= \frac{1}{2}(11)\left(\frac{44}{3}\right) = \frac{242}{3} \approx 80.7\) (accept exact \(\frac{242}{3}\) or \(80.7\) to 3 s.f.). '
                        r'| Ghi chú: Tam giác \(OPQ\) vuông tại gốc tọa độ \(O\).'
                    ),
                },
            ],
        },
        {
            'question_number': 7,
            'stem': r'A circle has centre \(O\) and radius \(8\text{ cm}\). A point \(P\) lies outside the circle such that \(OP = 17\text{ cm}\). The tangents from \(P\) to the circle touch the circle at the points \(A\) and \(B\).',
            'sub_questions': [
                {
                    'id': 'p22_q7a',
                    'type': 'long_answer',
                    'label': r'(a) Find the length of \(PA\) and show that \(\angle AOB = 2.162\text{ radians}\), correct to 3 decimal places.',
                    'max_marks': 3,
                    'marking_scheme': (
                        r'[B1] Since \(OA \perp PA\), \(PA = \sqrt{17^2 - 8^2} = \sqrt{225} = 15\text{ cm}\). '
                        r'[M1] In right-angled \(\triangle OAP\), \(\angle AOP = \arccos\left(\frac{8}{17}\right) = 1.080839\text{ rad}\). '
                        r'[A1] \(\angle AOB = 2\angle AOP = 2.161678\dots = 2.162\text{ rad}\) (3 d.p., AG). '
                        r'| Ghi chú: Bộ ba Pythagoras \(8-15-17\); dùng chế độ RAD trên máy tính.'
                    ),
                },
                {
                    'id': 'p22_q7b',
                    'type': 'short_answer',
                    'label': r'(b) Find the perimeter of the region bounded by the tangents \(PA\), \(PB\) and the minor arc \(AB\), correct to 3 significant figures.',
                    'max_marks': 2,
                    'marking_scheme': (
                        r'[M1] Perimeter \(= PA + PB + r\theta = 15 + 15 + 8(2.161678)\). '
                        r'[A1] \(47.293\dots = 47.3\text{ cm}\) (3 s.f.). '
                        r'| Ghi chú: Hai tiếp tuyến từ một điểm ngoài đường tròn bằng nhau: \(PA = PB = 15\text{ cm}\).'
                    ),
                },
                {
                    'id': 'p22_q7c',
                    'type': 'long_answer',
                    'label': r'(c) Find the area of the region bounded by the tangents \(PA\), \(PB\) and the minor arc \(AB\), correct to 3 significant figures.',
                    'max_marks': 3,
                    'marking_scheme': (
                        r'[M1] Area of kite \(OAPB = 2 \times \frac{1}{2}(8)(15) = 120\text{ cm}^2\). '
                        r'[M1] Area of minor sector \(OAB = \frac{1}{2}(8)^2(2.161678) = 69.1737\text{ cm}^2\). '
                        r'[A1] Shaded area \(= 120 - 69.1737 = 50.826\dots = 50.8\text{ cm}^2\) (3 s.f.). '
                        r'| Ghi chú: Diện tích cần tìm \(= \text{Diện tích tứ giác } OAPB - \text{Diện tích hình quạt } OAB\).'
                    ),
                },
            ],
        },
        {
            'question_number': 8,
            'stem': r'Angles in this question are measured in radians.',
            'sub_questions': [
                {
                    'id': 'p22_q8a',
                    'type': 'short_answer',
                    'label': r'(a) A curve has equation \(y = 4\cos(3x) - 1\) for \(0 \leq x \leq 2\pi\). State the amplitude, the period (in terms of \(\pi\)), and the minimum value of \(y\).',
                    'max_marks': 3,
                    'marking_scheme': (
                        r'[B1] Amplitude \(= 4\). '
                        r'[B1] Period \(= \frac{2\pi}{3}\). '
                        r'[B1] Minimum value \(= -4 - 1 = -5\). '
                        r'| Ghi chú: Với \(y = a\cos(bx) + c\): biên độ \(|a|\), chu kỳ \(\frac{2\pi}{b}\), giá trị nhỏ nhất \(c - |a|\).'
                    ),
                },
                {
                    'id': 'p22_q8b',
                    'type': 'long_answer',
                    'label': r'(b) Solve the equation \(3\sin(2x - 0.4) = -2\) for \(0 \leq x \leq \pi\), giving your answers correct to 3 significant figures.',
                    'max_marks': 5,
                    'marking_scheme': (
                        r'[M1] \(\sin(2x - 0.4) = -\frac{2}{3}\); basic acute angle \(\alpha = \arcsin\left(\frac{2}{3}\right) = 0.72973\text{ rad}\). '
                        r'[DM1] Range for \(u = 2x - 0.4\) is \(-0.4 \leq u \leq 2\pi - 0.4 \approx 5.8832\); Q3 and Q4 solutions are \(u = \pi + \alpha = 3.8713\) and \(u = 2\pi - \alpha = 5.5535\). '
                        r'[M1] Solve \(x = \frac{u + 0.4}{2}\) for both values. '
                        r'[A1] \(x = 2.14\text{ rad}\) (3 s.f.). '
                        r'[A1] \(x = 2.98\text{ rad}\) (3 s.f.). '
                        r'| Ghi chú: Luôn đổi khoảng nghiệm sang biến \(u = 2x - 0.4\) trước khi tìm nghiệm trong các góc phần tư.'
                    ),
                },
            ],
        },
        {
            'question_number': 9,
            'stem': r'A closed cylindrical tin of base radius \(r\text{ cm}\) and height \(h\text{ cm}\) has a fixed volume of \(500\text{ cm}^3\).',
            'sub_questions': [
                {
                    'id': 'p22_q9a',
                    'type': 'long_answer',
                    'label': r'(a) Show that the total surface area \(S\text{ cm}^2\) of the tin is given by \(S = 2\pi r^2 + \frac{1000}{r}\).',
                    'max_marks': 3,
                    'marking_scheme': (
                        r'[B1] From volume \(V = \pi r^2 h = 500\), express \(h = \frac{500}{\pi r^2}\). '
                        r'[M1] Substitute into total surface area \(S = 2\pi r^2 + 2\pi r h = 2\pi r^2 + 2\pi r\left(\frac{500}{\pi r^2}\right)\). '
                        r'[A1] Simplify to \(S = 2\pi r^2 + \frac{1000}{r}\) (AG). '
                        r'| Ghi chú: Hình trụ kín (closed) có 2 mặt đáy (\(2\pi r^2\)) cộng diện tích xung quanh (\(2\pi rh\)).'
                    ),
                },
                {
                    'id': 'p22_q9b',
                    'type': 'long_answer',
                    'label': r'(b) Given that \(r\) can vary, find the value of \(r\) that makes \(S\) stationary, giving your answer to 3 significant figures, and determine whether this value gives a maximum or a minimum value of \(S\).',
                    'max_marks': 4,
                    'marking_scheme': (
                        r'[M1] Differentiate: \(\frac{\text{d}S}{\text{d}r} = 4\pi r - \frac{1000}{r^2}\). '
                        r'[DM1] Set \(\frac{\text{d}S}{\text{d}r} = 0 \Rightarrow 4\pi r^3 = 1000 \Rightarrow r^3 = \frac{250}{\pi}\). '
                        r'[A1] \(r = 4.3013\dots = 4.30\text{ cm}\) (3 s.f.). '
                        r'[A1] \(\frac{\text{d}^2S}{\text{d}r^2} = 4\pi + \frac{2000}{r^3} = 12\pi > 0\) (for \(r > 0\)), therefore \(S\) is a minimum. '
                        r'| Ghi chú: Bắt buộc kiểm chứng bằng \(\frac{\text{d}^2S}{\text{d}r^2} > 0\) để kết luận giá trị nhỏ nhất.'
                    ),
                },
                {
                    'id': 'p22_q9c',
                    'type': 'long_answer',
                    'label': r'(c) Find the minimum total surface area of the tin and the corresponding height \(h\), giving each answer correct to 3 significant figures.',
                    'max_marks': 3,
                    'marking_scheme': (
                        r'[M1] Substitute unrounded \(r = 4.30127\) into \(S\) and \(h = \frac{500}{\pi r^2}\). '
                        r'[A1] \(S_{\min} = 348.73\dots = 349\text{ cm}^2\) (3 s.f.). '
                        r'[A1] \(h = 8.6025\dots = 8.60\text{ cm}\) (3 s.f.; note \(h = 2r\)). '
                        r'| Ghi chú: Hình trụ tối ưu diện tích toàn phần luôn có chiều cao bằng đường kính (\(h = 2r\)).'
                    ),
                },
            ],
        },
        {
            'question_number': 10,
            'stem': r'A particle moves in a straight line such that, \(t\) seconds after passing through a fixed point \(O\), its velocity \(v\text{ m s}^{-1}\) is given by \[v = 6\sin(2t) - 3, \quad 0 \leq t \leq \frac{\pi}{2}.\]',
            'sub_questions': [
                {
                    'id': 'p22_q10a',
                    'type': 'long_answer',
                    'label': r'(a) Find the two values of \(t\) in the interval \(0 \leq t \leq \frac{\pi}{2}\) when the particle is instantaneously at rest, giving your answers as exact multiples of \(\pi\).',
                    'max_marks': 3,
                    'marking_scheme': (
                        r'[M1] Set \(6\sin(2t) - 3 = 0 \Rightarrow \sin(2t) = \frac{1}{2}\), with \(0 \leq 2t \leq \pi\). '
                        r'[A1] \(2t = \frac{\pi}{6} \Rightarrow t = \frac{\pi}{12}\). '
                        r'[A1] \(2t = \frac{5\pi}{6} \Rightarrow t = \frac{5\pi}{12}\). '
                        r'| Ghi chú: Cả hai góc \(\frac{\pi}{6}\) và \(\frac{5\pi}{6}\) đều nằm trong \([0, \pi]\).'
                    ),
                },
                {
                    'id': 'p22_q10b',
                    'type': 'short_answer',
                    'label': r'(b) Find the acceleration of the particle when \(t = \frac{\pi}{12}\), giving your answer correct to 3 significant figures.',
                    'max_marks': 2,
                    'marking_scheme': (
                        r'[M1] Differentiate: \(a = \frac{\text{d}v}{\text{d}t} = 12\cos(2t)\). '
                        r'[A1] At \(t = \frac{\pi}{12}\): \(a = 12\cos\left(\frac{\pi}{6}\right) = 6\sqrt{3} \approx 10.4\text{ m s}^{-2}\) (3 s.f.). '
                        r'| Ghi chú: Đạo hàm \(\frac{\text{d}}{\text{d}t}[\sin(2t)] = 2\cos(2t)\) (nhớ hệ số \(2\) của quy tắc hàm hợp).'
                    ),
                },
                {
                    'id': 'p22_q10c',
                    'type': 'long_answer',
                    'label': r'(c) Given that the particle passes through \(O\) when \(t = 0\), find an expression for its displacement \(s\text{ m}\) from \(O\) in terms of \(t\), and hence find the distance travelled by the particle between the two times of instantaneous rest, giving your answer correct to 3 significant figures.',
                    'max_marks': 5,
                    'marking_scheme': (
                        r'[M1] Integrate velocity: \(s = \int (6\sin(2t) - 3)\,\text{d}t = -3\cos(2t) - 3t + c\). '
                        r'[A1] Apply \(s(0) = 0\): \(-3(1) - 0 + c = 0 \Rightarrow c = 3\), so \(s = 3 - 3\cos(2t) - 3t\). '
                        r'[M1] Since \(v > 0\) throughout \(\left(\frac{\pi}{12}, \frac{5\pi}{12}\right)\), distance \(= s\left(\frac{5\pi}{12}\right) - s\left(\frac{\pi}{12}\right)\). '
                        r'[A1] Exact distance \(= \left(3 + \frac{3\sqrt{3}}{2} - \frac{5\pi}{4}\right) - \left(3 - \frac{3\sqrt{3}}{2} - \frac{\pi}{4}\right) = 3\sqrt{3} - \pi\). '
                        r'[A1] Numerical distance \(= 2.05456\dots = 2.05\text{ m}\) (3 s.f.). '
                        r'| Ghi chú: Vì \(\int \sin(2t)\,\text{d}t = -\frac{1}{2}\cos(2t)\), phải cẩn thận dấu trừ và hằng số \(c = 3\).'
                    ),
                },
            ],
        },
    ],
}

MOCKS_0606_2025 = [
    PAPER_0606_11,
    PAPER_0606_12,
    PAPER_0606_21,
    PAPER_0606_22,
]


# =============================================================================
# SELF-VERIFICATION SUITE (Schema, Marks, KaTeX, Step Marks & Mathematical Proof)
# =============================================================================
def _sig3(x):
    """Format a float to 3 significant figures (Cambridge standard)."""
    return f'{x:.3g}'


def verify_all_math():
    # -------------------------------------------------------------------------
    # 1. Structural, Metadata, 80-Mark, KaTeX & Step-Mark Integrity Checks
    # -------------------------------------------------------------------------
    assert len(MOCKS_0606_2025) == 4, f'Expected 4 papers, got {len(MOCKS_0606_2025)}'

    expected_meta = [
        ('m0606_p1_1', 'papers/igcse-maths/0606_p1_noncalc_mock1.pdf', 101, '0606/11', 'non-calculator'),
        ('m0606_p1_2', 'papers/igcse-maths/0606_p1_noncalc_mock2.pdf', 102, '0606/12', 'non-calculator'),
        ('m0606_p2_1', 'papers/igcse-maths/0606_p2_calc_mock1.pdf', 103, '0606/21', 'calculator'),
        ('m0606_p2_2', 'papers/igcse-maths/0606_p2_calc_mock2.pdf', 104, '0606/22', 'calculator'),
    ]

    global_ids = set()
    mark_tag_re = re.compile(r'\[(?:B|M|DM|A)(\d+)\]')

    for paper, (exp_code, exp_pdf, exp_order, exp_pcode, exp_policy) in zip(MOCKS_0606_2025, expected_meta):
        assert paper['code'] == exp_code
        assert paper['pdf_rel_path'] == exp_pdf
        assert paper['order_index'] == exp_order
        meta = paper['paper_meta']
        assert meta['code'] == exp_pcode
        assert meta['syllabus'] == '0606'
        assert meta['course_id'] == COURSE_0606_ID
        assert meta['time_limit'] == 120
        assert meta['calculator_policy'] == exp_policy
        assert 10 <= len(paper['questions']) <= 11, f"{exp_code}: expected 10-11 questions"

        paper_ids = set()
        total_marks = 0
        for q_idx, q in enumerate(paper['questions'], start=1):
            assert q['question_number'] == q_idx
            stem = q.get('stem') or ''
            assert '$' not in stem, f'{exp_code} Q{q_idx} stem contains $'
            assert stem.count(r'\(') == stem.count(r'\)'), f'{exp_code} Q{q_idx} unbalanced \\( \\) in stem'
            assert stem.count(r'\[') == stem.count(r'\]'), f'{exp_code} Q{q_idx} unbalanced \\[ \\] in stem'
            assert 'relative velocity' not in stem.lower(), f'{exp_code} Q{q_idx} mentions relative velocity'

            assert q['sub_questions'], f'{exp_code} Q{q_idx} has no sub_questions'
            for sq in q['sub_questions']:
                sid = sq['id']
                assert sid and sid not in paper_ids and sid not in global_ids, f'Duplicate sub-question id: {sid}'
                paper_ids.add(sid)
                global_ids.add(sid)

                assert sq['type'] in ('short_answer', 'long_answer'), f'Invalid type for {sid}'
                lbl = (sq.get('label') or '').strip()
                ms = (sq.get('marking_scheme') or '').strip()
                assert lbl, f'{sid}: empty label'
                assert ms, f'{sid}: empty marking_scheme'

                m = int(sq['max_marks'])
                assert m > 0, f'{sid}: non-positive max_marks'
                total_marks += m

                # Verify step marks in marking_scheme sum exactly to max_marks
                step_sum = sum(int(x) for x in mark_tag_re.findall(ms))
                assert step_sum == m, f'{sid}: step marks sum to {step_sum} != max_marks {m}'

                for field_name, txt in [('label', lbl), ('marking_scheme', ms)]:
                    assert '$' not in txt, f'{sid} {field_name} contains raw $'
                    assert txt.count(r'\(') == txt.count(r'\)'), f'{sid} {field_name} unbalanced \\( \\)'
                    assert txt.count(r'\[') == txt.count(r'\]'), f'{sid} {field_name} unbalanced \\[ \\]'
                    assert 'relative velocity' not in txt.lower(), f'{sid} {field_name} mentions relative velocity'
                    # Ensure no stray control characters from bad raw-string escapes
                    for bad_ch in ('\x07', '\x08', '\x0c', '\r', '\t'):
                        assert bad_ch not in txt, f'{sid} {field_name} has stray escape char {repr(bad_ch)}'
                    # Ensure no HTML-tag-like `<letter` sequence that could break PyMuPDF Story
                    assert not re.search(r'<[a-zA-Z/]', txt), f'{sid} {field_name} contains HTML-like tag sequence'
                    # Ensure no raw backslash-apostrophe inside raw strings
                    assert r"\'" not in txt, f"{sid} {field_name} contains raw backslash-apostrophe"

        assert total_marks == 80, f'{exp_code}: total_marks = {total_marks}, expected EXACTLY 80'

    # -------------------------------------------------------------------------
    # 2. Mathematical Verification — Paper 1 (0606/11 Non-Calculator)
    # -------------------------------------------------------------------------
    # P1 Q1a: |3x - 5| = x + 3 -> x = 4, 1/2
    for x in (Fraction(4), Fraction(1, 2)):
        assert abs(3 * x - 5) == x + 3
    # P1 Q1b: discriminant of x^2 + (5-k)x + (2k+2) = 0 -> (k-1)(k-17) < 0
    for k in (1, 17):
        assert (5 - k) ** 2 - 4 * (2 * k + 2) == 0
    assert (5 - 5) ** 2 - 4 * (2 * 5 + 2) < 0

    # P1 Q2a: (2 + 7*sqrt(3)) / (5 - 2*sqrt(3)) = 4 + 3*sqrt(3)
    assert math.isclose((2 + 7 * math.sqrt(3)) / (5 - 2 * math.sqrt(3)), 4 + 3 * math.sqrt(3), rel_tol=1e-12)
    # P1 Q2b: trapezium area 1/2 * ((3+sqrt5)+(5+sqrt5)) * (5-sqrt5) = 15 + sqrt5
    assert math.isclose(0.5 * ((3 + math.sqrt(5)) + (5 + math.sqrt(5))) * (5 - math.sqrt(5)), 15 + math.sqrt(5), rel_tol=1e-12)

    # P1 Q3: p(x) = 2x^3 - 2x^2 - 7x + 6
    p_p1q3 = lambda x: 2 * x ** 3 - 2 * x ** 2 - 7 * x + 6
    assert p_p1q3(2) == 0
    assert p_p1q3(-1) == 9
    assert math.isclose(p_p1q3((-1 + math.sqrt(7)) / 2), 0.0, abs_tol=1e-12)
    assert math.isclose(p_p1q3((-1 - math.sqrt(7)) / 2), 0.0, abs_tol=1e-12)

    # P1 Q4: x^2 + y^2 - 6x + 8y - 15 = 0 -> M(3,-4), r=2*sqrt(10), P(5,2), tangent x+3y-11=0
    assert (5 - 3) ** 2 + (2 - (-4)) ** 2 == 40
    assert Fraction(2 - (-4), 5 - 3) == Fraction(3, 1)
    assert 5 + 3 * 2 - 11 == 0
    assert Fraction(-1, 3) * Fraction(3, 1) == -1

    # P1 Q5a: log_3(2x-1) + log_3(x+1) = 2 -> x = 2
    assert math.isclose(math.log(2 * 2 - 1, 3) + math.log(2 + 1, 3), 2.0, rel_tol=1e-12)
    # P1 Q5b: 2^(2y+1) - 9*(2^y) + 4 = 0 -> y = -1, 2
    for y in (-1, 2):
        assert math.isclose(2 ** (2 * y + 1) - 9 * (2 ** y) + 4, 0.0, abs_tol=1e-12)

    # P1 Q6: (2 - x/4)^6 -> 64 - 48x + 15x^2; k = 3/2, x-coeff = 48
    c0 = Fraction(math.comb(6, 0) * (2 ** 6))
    c1 = Fraction(math.comb(6, 1) * (2 ** 5)) * Fraction(-1, 4)
    c2 = Fraction(math.comb(6, 2) * (2 ** 4)) * Fraction(-1, 4) ** 2
    assert (c0, c1, c2) == (64, -48, 15)
    k_val = Fraction(c2 - (-57), -c1)
    assert k_val == Fraction(3, 2)
    assert c1 + k_val * c0 == 48

    # P1 Q7: sin(x)/(1+cos x) + (1+cos x)/sin(x) = 4sin(x) + 2 -> pi/6, 5pi/6, 3pi/2
    for x in (math.pi / 6, 5 * math.pi / 6, 3 * math.pi / 2):
        lhs = math.sin(x) / (1 + math.cos(x)) + (1 + math.cos(x)) / math.sin(x)
        assert math.isclose(lhs, 2 / math.sin(x), rel_tol=1e-12)
        assert math.isclose(lhs, 4 * math.sin(x) + 2, rel_tol=1e-12)

    # P1 Q8: f(x) = (x-3)^2 + 2 (x>=3), g(x) = (2x+1)/(x-1) (x>1), fg(7/4) = 11
    x8 = Fraction(7, 4)
    gx8 = (2 * x8 + 1) / (x8 - 1)
    assert gx8 == 6 and (gx8 - 3) ** 2 + 2 == 11

    # P1 Q9: CM = (-5/2)a + (1/2)b, MD = (-1/2)a + (1/10)b -> CM = 5*MD
    assert Fraction(-5, 2) == 5 * Fraction(-1, 2)
    assert Fraction(1, 2) == 5 * Fraction(1, 10)

    # P1 Q10: integral_0^4 (6x+2)/sqrt(2x+1) dx = 24; area_0^4 (3x+5)/sqrt(2x+1) dx = 20
    # Verify numerically with Simpson's rule (1000 subintervals)
    def simpson(fn, a, b, n=1000):
        h = (b - a) / n
        s = fn(a) + fn(b) + sum((4 if i % 2 else 2) * fn(a + i * h) for i in range(1, n))
        return s * h / 3.0

    assert math.isclose(simpson(lambda x: (6 * x + 2) / math.sqrt(2 * x + 1), 0.0, 4.0), 24.0, rel_tol=1e-10)
    assert math.isclose(simpson(lambda x: (3 * x + 5) / math.sqrt(2 * x + 1), 0.0, 4.0), 20.0, rel_tol=1e-10)

    # -------------------------------------------------------------------------
    # 3. Mathematical Verification — Paper 2 (0606/12 Non-Calculator)
    # -------------------------------------------------------------------------
    # P2 Q1: (1, 3) and (4, -3), distance = 3*sqrt(5)
    for x, y in ((1, 3), (4, -3)):
        assert 2 * x + y == 5 and x ** 2 + x * y + y ** 2 == 13
    assert math.isclose(math.hypot(4 - 1, -3 - 3), 3 * math.sqrt(5), rel_tol=1e-12)

    # P2 Q2a: 27^(2x-1) = 9^(x+2)/3^5 -> x = 1/2
    assert math.isclose(27 ** (2 * 0.5 - 1), (9 ** (0.5 + 2)) / (3 ** 5), rel_tol=1e-12)
    # P2 Q2b: 2x - sqrt(75) = x*sqrt(3) - 4 -> x = 7 + 6*sqrt(3)
    x2b = 7 + 6 * math.sqrt(3)
    assert math.isclose(2 * x2b - math.sqrt(75), x2b * math.sqrt(3) - 4, rel_tol=1e-12)

    # P2 Q3a & Q3b boundary checks
    f3a = lambda x: (x + 3) * (2 * x - 1) * (x - 4)
    assert f3a(-4) < 0 and f3a(-3) == 0 and f3a(0) > 0 and f3a(0.5) == 0 and f3a(2) < 0 and f3a(4) == 0 and f3a(5) > 0
    assert abs(2 * 0 - 1) < abs(0 + 4) and abs(2 * (-1) - 1) == abs(-1 + 4) and abs(2 * 5 - 1) == abs(5 + 4)

    # P2 Q4a: AP a=3, d=4 -> u5=19, S10=210, u20=79
    a4, d4 = 3, 4
    assert a4 + 4 * d4 == 19 and 5 * (2 * a4 + 9 * d4) == 210 and a4 + 19 * d4 == 79
    # P2 Q4b: GP k=8 -> 18, 12, 8; r = 2/3, S_inf = 54
    k4 = 8
    assert Fraction(k4 + 4, k4 + 10) == Fraction(k4, k4 + 4) == Fraction(2, 3)
    assert Fraction(k4 + 10, 1 - Fraction(2, 3)) == 54

    # P2 Q5: Circle centre A(-2,5), B(4,-3) -> r^2=100; line y=2x-1 meets at P(6,11), Q(-2,-5); normal 3x-4y+26=0
    assert (4 - (-2)) ** 2 + (-3 - 5) ** 2 == 100
    for px, py in ((6, 11), (-2, -5)):
        assert py == 2 * px - 1 and (px + 2) ** 2 + (py - 5) ** 2 == 100
    assert 3 * 6 - 4 * 11 + 26 == 0 and 3 * (-2) - 4 * 5 + 26 == 0

    # P2 Q6: r=6, theta=pi/3 -> perim = 6 + 2pi, segment area = 6pi - 9sqrt(3)
    assert math.isclose(6 + 6 * (math.pi / 3), 6 + 2 * math.pi, rel_tol=1e-12)
    assert math.isclose(0.5 * 36 * (math.pi / 3 - math.sin(math.pi / 3)), 6 * math.pi - 9 * math.sqrt(3), rel_tol=1e-12)

    # P2 Q7a & Q7b
    assert math.isclose(math.log(4, 2) + 2 * math.log(4 - 3, 4), 2.0, rel_tol=1e-12)
    for x in (math.log(2), math.log(3)):
        assert math.isclose(math.exp(2 * x) - 5 * math.exp(x) + 6, 0.0, abs_tol=1e-12)

    # P2 Q8a & Q8b
    assert Fraction(3, 5) / Fraction(-4, 5) == Fraction(-3, 4) and Fraction(3, 5) ** 2 + Fraction(-4, 5) ** 2 == 1
    for x in (math.pi / 3, math.pi, 5 * math.pi / 3):
        assert math.isclose(2 * (math.sin(x) ** 2) - math.cos(x) - 1, 0.0, abs_tol=1e-12)

    # P2 Q9: y = (x^2+3)/(x-1) -> stat pts (3,6) min, (-1,-2) max; tangent at x=2: y = -3x + 13
    y9 = lambda x: Fraction(x ** 2 + 3, x - 1)
    dy9 = lambda x: Fraction(x ** 2 - 2 * x - 3, (x - 1) ** 2)
    d2y9 = lambda x: Fraction(8, (x - 1) ** 3)
    assert y9(3) == 6 and dy9(3) == 0 and d2y9(3) == 1 > 0
    assert y9(-1) == -2 and dy9(-1) == 0 and d2y9(-1) == -1 < 0
    assert y9(2) == 7 and dy9(2) == -3 and (-3 * 2 + 13) == 7

    # P2 Q10: v = 3t^2 - 18t + 24 -> rest t=2,4; a(1)=-12; v(3)=-3; total dist on [0,5] = 28
    v10 = lambda t: 3 * t ** 2 - 18 * t + 24
    s10 = lambda t: t ** 3 - 9 * t ** 2 + 24 * t
    assert v10(2) == 0 and v10(4) == 0 and (6 * 1 - 18) == -12 and v10(3) == -3
    assert abs(s10(2) - s10(0)) + abs(s10(4) - s10(2)) + abs(s10(5) - s10(4)) == 28

    # -------------------------------------------------------------------------
    # 4. Mathematical Verification — Paper 3 (0606/21 Calculator)
    # -------------------------------------------------------------------------
    # P3 Q1: Linear Law ln y = 0.8 + 0.5x
    assert _sig3(math.exp(0.5)) == '1.65'
    assert _sig3(math.exp(0.8)) == '2.23'
    assert _sig3(2 * (math.log(50) - 0.8)) == '6.22'

    # P3 Q2a: Brute-force verification of 5-digit even numbers > 40000 from {1..7}
    brute_q2a = sum(
        1 for p in itertools.permutations([1, 2, 3, 4, 5, 6, 7], 5)
        if p[0] >= 4 and p[-1] % 2 == 0
    )
    assert brute_q2a == 600
    # P3 Q2b(i) & (ii)
    assert math.comb(7, 4) * math.comb(5, 2) + math.comb(7, 5) * math.comb(5, 1) + math.comb(7, 6) * math.comb(5, 0) == 462
    assert math.comb(12, 6) - math.comb(10, 4) == 714

    # P3 Q3: Circular measure r=9, chord=14
    theta3 = math.acos(-17 / 81)
    assert f'{theta3:.3f}' == '1.782'
    assert f'{14 + 9 * theta3:.1f}' == '30.0'
    assert _sig3(0.5 * 81 * (theta3 - math.sin(theta3))) == '32.6'

    # P3 Q4a & Q4b
    x4a = (2 * math.log(5) + math.log(3)) / (2 * math.log(3) - math.log(5))
    assert _sig3(x4a) == '7.35'
    assert math.isclose(3 ** (2 * x4a - 1), 5 ** (x4a + 2), rel_tol=1e-12)
    u4b_1, u4b_2 = (7 + math.sqrt(17)) / 4, (7 - math.sqrt(17)) / 4
    assert _sig3(math.log(u4b_1)) == '1.02'
    assert f'{math.log(u4b_2):.3f}' == '-0.330'

    # P3 Q5a & Q5b
    roots_5a = sorted([
        math.degrees(math.atan(3)),
        180 + math.degrees(math.atan(3)),
        180 - math.degrees(math.atan(0.5)),
        360 - math.degrees(math.atan(0.5)),
    ])
    assert [f'{r:.1f}' for r in roots_5a] == ['71.6', '153.4', '251.6', '333.4']
    for r in roots_5a:
        rad = math.radians(r)
        assert math.isclose(2 / (math.cos(rad) ** 2) - 5 * math.tan(rad) - 5, 0.0, abs_tol=1e-10)
    r5b_1, r5b_2 = math.atan(0.5), math.pi - math.atan(3)
    assert _sig3(r5b_1) == '0.464' and _sig3(r5b_2) == '1.89'
    for y in (r5b_1, r5b_2):
        assert math.isclose(3 / (math.sin(y) ** 2) - 5 / math.tan(y) - 5, 0.0, abs_tol=1e-10)

    # P3 Q6: Circle (x-4)^2 + (y+2)^2 = 25, line y = 2x - 3
    xA, xB = (6 + 2 * math.sqrt(19)) / 5, (6 - 2 * math.sqrt(19)) / 5
    yA, yB = 2 * xA - 3, 2 * xB - 3
    assert _sig3(xA) == '2.94' and _sig3(yA) == '2.89'
    assert _sig3(xB) == '-0.544' and _sig3(yB) == '-4.09'
    chord_ab = math.hypot(xA - xB, yA - yB)
    assert math.isclose(chord_ab, 4 * math.sqrt(95) / 5, rel_tol=1e-12)
    assert f'{chord_ab:.2f}' == '7.80'

    # P3 Q7: Cone dh/dt = 4/(3pi), small change 0.3p
    assert _sig3(4 / (3 * math.pi)) == '0.424'
    assert Fraction(3, 3 * 4 - 2) == Fraction(3, 10)

    # P3 Q8: GP n = 15, AP n = 23
    S_gp = lambda n: 800 * (1 - 0.85 ** n)
    assert S_gp(14) <= 720 < S_gp(15)
    S_ap = lambda n: (n / 2) * (14 + 3.5 * (n - 1))
    assert S_ap(22) <= 1000 < S_ap(23)

    # P3 Q9: Area between y = 8 - x and y = 12/x from x = 2 to 6
    exact_area_p3q9 = 16 - 12 * math.log(3)
    assert math.isclose(simpson(lambda x: (8 - x) - 12 / x, 2.0, 6.0), exact_area_p3q9, rel_tol=1e-10)
    assert _sig3(exact_area_p3q9) == '2.82'

    # P3 Q10: v = 10e^(-0.2t) - 4
    T_p3q10 = 5 * math.log(2.5)
    assert _sig3(T_p3q10) == '4.58'
    assert math.isclose(-2 * math.exp(-0.2 * T_p3q10), -0.8, rel_tol=1e-12)
    s_p3q10 = lambda t: 50 - 50 * math.exp(-0.2 * t) - 4 * t
    dist_p3q10 = 2 * s_p3q10(T_p3q10) - s_p3q10(10)
    assert math.isclose(
        simpson(lambda t: abs(10 * math.exp(-0.2 * t) - 4), 0.0, T_p3q10)
        + simpson(lambda t: abs(10 * math.exp(-0.2 * t) - 4), T_p3q10, 10.0),
        dist_p3q10,
        rel_tol=1e-9,
    )
    assert _sig3(dist_p3q10) == '20.1'

    # -------------------------------------------------------------------------
    # 5. Mathematical Verification — Paper 4 (0606/22 Calculator)
    # -------------------------------------------------------------------------
    # P4 Q1a & Q1b
    for x in (-3, 0, 2, 5):
        assert 3 * x ** 2 - 12 * x + 17 == 3 * (x - 2) ** 2 + 5
    for x in (Fraction(1, 8), Fraction(27)):
        u = Fraction(1, 2) if x == Fraction(1, 8) else Fraction(3)
        assert u ** 3 == x and 2 * u ** 2 - 7 * u + 3 == 0

    # P4 Q2: Linear Law log10(y) = 0.65 + 1.4 log10(x)
    assert Fraction(415 - 135, 250 - 50) == Fraction(7, 5)
    assert _sig3(10 ** 0.65) == '4.47'
    assert _sig3((10 ** 0.65) * (12 ** 1.4)) == '145'

    # P4 Q3c: fg(x) = 3(x+4)^2 - 1 = 20 -> x = -4 + sqrt(7)
    x_p4q3 = -4 + math.sqrt(7)
    assert math.isclose(3 * math.exp(2 * math.log(x_p4q3 + 4)) - 1, 20.0, rel_tol=1e-12)
    assert _sig3(x_p4q3) == '-1.35'

    # P4 Q4a & Q4b
    assert math.comb(9, 6) * (2 ** 3) * ((-1) ** 6) == 672
    assert 8 * 3 == 24 and math.comb(8, 2) * (3 ** 2) == 252

    # P4 Q5a(i), (ii) & Q5b
    assert math.factorial(6) * math.factorial(3) == 4320
    assert math.factorial(5) * math.perm(6, 3) == 14400
    # Brute-force check of Q5a(ii) on 8 labelled items (3 Physics = {0,1,2})
    brute_q5aii = sum(
        1 for p in itertools.permutations(range(8))
        if all(not (p[i] < 3 and p[i + 1] < 3) for i in range(7))
    )
    assert brute_q5aii == 14400
    assert math.comb(5, 2) * math.comb(6, 2) * math.factorial(4) == 3600

    # P4 Q6: Diameter A(-3,2), B(5,8) -> M(1,5), r=5, tangent 4x+3y=44, area OPQ = 242/3
    assert (-3 + 5) == 2 and (2 + 8) == 10
    assert (5 - 1) ** 2 + (8 - 5) ** 2 == 25
    assert 4 * 5 + 3 * 8 == 44
    assert Fraction(1, 2) * 11 * Fraction(44, 3) == Fraction(242, 3)
    assert _sig3(242 / 3) == '80.7'

    # P4 Q7: r=8, OP=17 -> PA=15, AOB=2.162, perim=47.3, area=50.8
    assert math.isqrt(17 ** 2 - 8 ** 2) == 15
    aob7 = 2 * math.acos(8 / 17)
    assert f'{aob7:.3f}' == '2.162'
    assert _sig3(30 + 8 * aob7) == '47.3'
    assert _sig3(120 - 32 * aob7) == '50.8'

    # P4 Q8b: 3sin(2x - 0.4) = -2 on [0, pi]
    al8 = math.asin(2 / 3)
    x8_1, x8_2 = (math.pi + al8 + 0.4) / 2, (2 * math.pi - al8 + 0.4) / 2
    assert 0 <= x8_1 <= math.pi and 0 <= x8_2 <= math.pi
    assert _sig3(x8_1) == '2.14' and _sig3(x8_2) == '2.98'
    for x in (x8_1, x8_2):
        assert math.isclose(3 * math.sin(2 * x - 0.4), -2.0, rel_tol=1e-12)

    # P4 Q9: Closed cylinder V=500 -> r=(250/pi)^(1/3), S_min=349, h=8.60
    r9 = (250 / math.pi) ** (1 / 3)
    S9 = 2 * math.pi * r9 ** 2 + 1000 / r9
    h9 = 500 / (math.pi * r9 ** 2)
    assert f'{r9:.2f}' == '4.30' and _sig3(S9) == '349' and f'{h9:.2f}' == '8.60'
    assert math.isclose(h9, 2 * r9, rel_tol=1e-12)

    # P4 Q10: v = 6sin(2t) - 3 on [0, pi/2]
    t1, t2 = math.pi / 12, 5 * math.pi / 12
    assert math.isclose(6 * math.sin(2 * t1) - 3, 0.0, abs_tol=1e-12)
    assert math.isclose(6 * math.sin(2 * t2) - 3, 0.0, abs_tol=1e-12)
    assert _sig3(12 * math.cos(2 * t1)) == '10.4'
    exact_d10 = 3 * math.sqrt(3) - math.pi
    assert math.isclose(simpson(lambda t: 6 * math.sin(2 * t) - 3, t1, t2), exact_d10, rel_tol=1e-10)
    assert _sig3(exact_d10) == '2.05'

    print('=== ALL 4 CAMBRIDGE 0606 (2025-2027) FULL MOCK EXAMS VERIFIED ===')
    for p in MOCKS_0606_2025:
        tot = sum(sq['max_marks'] for q in p['questions'] for sq in q['sub_questions'])
        n_sub = sum(len(q['sub_questions']) for q in p['questions'])
        print(
            f"  [OK] {p['code']} ({p['paper_meta']['code']} | {p['paper_meta']['calculator_policy']}): "
            f"{len(p['questions'])} Qs, {n_sub} sub-Qs, {tot} marks"
        )


if __name__ == '__main__':
    verify_all_math()
