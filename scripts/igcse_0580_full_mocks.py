# -*- coding: utf-8 -*-
"""
Cambridge IGCSE Mathematics (0580) Extended — 2025–2027 Syllabus
4 Official-Style Full-Length 100-Mark Mock Papers for TonyEnglish.vn:
  1. m0580_p2_1 (0580/21) Paper 2 Extended — Non-Calculator Full Mock #1 (100 marks, 120 min)
  2. m0580_p2_2 (0580/22) Paper 2 Extended — Non-Calculator Full Mock #2 (100 marks, 120 min)
  3. m0580_p4_1 (0580/41) Paper 4 Extended — Calculator Full Mock #1     (100 marks, 120 min)
  4. m0580_p4_2 (0580/42) Paper 4 Extended — Calculator Full Mock #2     (100 marks, 120 min)

Matches schema expected by `scripts/igcse_maths_pipeline.py`:
  - `generate_cambridge_exam_pdf(out_rel_path, paper_meta, questions)`
  - `build_igcse_paper_json(paper_meta, pdf_url, questions)`
"""

from fractions import Fraction
import math
import re

COURSE_0580_ID = '7211abb0-ccba-479f-92ad-2d218121f717'

# =============================================================================
# PAPER 1: 0580/21 — Paper 2 (Extended — Non-Calculator) Full Mock #1 (100 marks)
# =============================================================================
PAPER_0580_P2_1_QUESTIONS = [
    {
        'question_number': '1',
        'stem': '',
        'sub_questions': [
            {
                'id': 'q1a',
                'type': 'short_answer',
                'label': r'(a) Express \(180\) as a product of its prime factors in index form.',
                'max_marks': 2,
                'marking_scheme': (
                    r'M1: Correct factor tree or repeated division by primes showing \(2, 2, 3, 3, 5\) (phân tích đúng thừa số nguyên tố) | '
                    r'A1: \(2^{2} \times 3^{2} \times 5\)'
                ),
            },
            {
                'id': 'q1b',
                'type': 'short_answer',
                'label': r'(b) Given that \(252 = 2^{2} \times 3^{2} \times 7\), find the highest common factor (HCF) and the lowest common multiple (LCM) of \(180\) and \(252\).',
                'max_marks': 2,
                'marking_scheme': (
                    r'B1: \(\text{HCF} = 2^{2} \times 3^{2} = 36\) (ƯCLN lấy số mũ nhỏ nhất) | '
                    r'B1: \(\text{LCM} = 2^{2} \times 3^{2} \times 5 \times 7 = 1260\) (BCNN lấy số mũ lớn nhất)'
                ),
            },
            {
                'id': 'q1c',
                'type': 'short_answer',
                'label': r'(c) Find the smallest positive integer \(k\) such that \(180k\) is a square number.',
                'max_marks': 1,
                'marking_scheme': (
                    r'B1: \(k = 5\) (vì \(180 = 2^{2} \times 3^{2} \times 5\), cần nhân thêm \(5\) để mọi số mũ đều chẵn: \(180 \times 5 = 900 = 30^{2}\))'
                ),
            },
        ],
    },
    {
        'question_number': '2',
        'stem': '',
        'sub_questions': [
            {
                'id': 'q2a',
                'type': 'structured',
                'label': r'(a) Show by algebra that the recurring decimal \(0.363636...\) (where the digits \(36\) recur) is equal to \(\frac{4}{11}\).',
                'max_marks': 2,
                'marking_scheme': (
                    r'M1: Let \(x = 0.363636...\), then \(100x = 36.363636...\), subtracting gives \(99x = 36\) (đặt \(x\) và nhân \(100\) để khử phần tuần hoàn) | '
                    r'A1: \(x = \frac{36}{99} = \frac{4}{11}\) convincingly shown'
                ),
            },
            {
                'id': 'q2b',
                'type': 'structured',
                'label': r'(b) Without a calculator, evaluate \((4.8 \times 10^{7}) \div (1.6 \times 10^{-3}) + 5 \times 10^{9}\), giving your answer in standard form.',
                'max_marks': 3,
                'marking_scheme': (
                    r'M1: \(\frac{4.8}{1.6} \times 10^{7 - (-3)} = 3 \times 10^{10}\) (chia phần số và trừ số mũ) | '
                    r'M1: Convert to same power of \(10\): \(30 \times 10^{9} + 5 \times 10^{9} = 35 \times 10^{9}\) (hoặc \(3 \times 10^{10} + 0.5 \times 10^{10}\)) | '
                    r'A1: \(3.5 \times 10^{10}\)'
                ),
            },
        ],
    },
    {
        'question_number': '3',
        'stem': '',
        'sub_questions': [
            {
                'id': 'q3a',
                'type': 'short_answer',
                'label': r'(a) Simplify \(\sqrt{72} - \sqrt{18} + \sqrt{50}\), giving your answer in the form \(k\sqrt{2}\).',
                'max_marks': 2,
                'marking_scheme': (
                    r'M1: Correctly simplifying at least two surds: \(\sqrt{72} = 6\sqrt{2}\), \(\sqrt{18} = 3\sqrt{2}\), \(\sqrt{50} = 5\sqrt{2}\) (rút gọn căn thức về \(\sqrt{2}\)) | '
                    r'A1: \(8\sqrt{2}\)'
                ),
            },
            {
                'id': 'q3b',
                'type': 'short_answer',
                'label': r'(b) Expand and simplify \((3 + 2\sqrt{5})(4 - \sqrt{5})\).',
                'max_marks': 2,
                'marking_scheme': (
                    r'M1: \(12 - 3\sqrt{5} + 8\sqrt{5} - 2(\sqrt{5})^{2} = 12 + 5\sqrt{5} - 10\) (nhân phân phối đầy đủ 4 hạng tử) | '
                    r'A1: \(2 + 5\sqrt{5}\)'
                ),
            },
            {
                'id': 'q3c',
                'type': 'structured',
                'label': r'(c) Rationalise the denominator and simplify \(14 / (3 - \sqrt{2})\), giving your answer in the form \(a + b\sqrt{2}\) where \(a\) and \(b\) are integers.',
                'max_marks': 2,
                'marking_scheme': (
                    r'M1: Multiply numerator and denominator by conjugate \(3 + \sqrt{2}\): \(\frac{14(3 + \sqrt{2})}{9 - 2} = \frac{14(3 + \sqrt{2})}{7}\) (nhân lượng liên hợp để khử căn ở mẫu) | '
                    r'A1: \(6 + 2\sqrt{2}\)'
                ),
            },
        ],
    },
    {
        'question_number': '4',
        'stem': '',
        'sub_questions': [
            {
                'id': 'q4a',
                'type': 'short_answer',
                'label': r'(a) Find the exact value of \(27^{-\frac{2}{3}}\).',
                'max_marks': 2,
                'marking_scheme': (
                    r'M1: \(27^{\frac{1}{3}} = 3\) or writing \(\frac{1}{(\sqrt[3]{27})^{2}}\) (áp dụng quy tắc số mũ âm và phân số) | '
                    r'A1: \(\frac{1}{9}\)'
                ),
            },
            {
                'id': 'q4b',
                'type': 'structured',
                'label': r'(b) Solve the equation \(4^{2x - 1} = \frac{1}{8}\).',
                'max_marks': 3,
                'marking_scheme': (
                    r'M1: Rewrite both sides in base \(2\): \((2^{2})^{2x - 1} = 2^{-3}\) (đưa cùng cơ số \(2\)) | '
                    r'M1: Equate powers: \(2(2x - 1) = -3 \Rightarrow 4x - 2 = -3\) | '
                    r'A1: \(x = -\frac{1}{4}\) (or \(-0.25\))'
                ),
            },
        ],
    },
    {
        'question_number': '5',
        'stem': '',
        'sub_questions': [
            {
                'id': 'q5a',
                'type': 'structured',
                'label': r'(a) Simplify completely \(\frac{2x^2 - 5x - 3}{x^2 - 9}\).',
                'max_marks': 3,
                'marking_scheme': (
                    r'M1: Factorise numerator as \((2x + 1)(x - 3)\) (phân tích đa thức tử thành nhân tử) | '
                    r'M1: Factorise denominator as \((x - 3)(x + 3)\) (hiệu hai bình phương) | '
                    r'A1: \(\frac{2x + 1}{x + 3}\)'
                ),
            },
            {
                'id': 'q5b',
                'type': 'structured',
                'label': r'(b) Express \(\frac{3}{x - 2} - \frac{2}{x + 1}\) as a single fraction in its simplest form.',
                'max_marks': 3,
                'marking_scheme': (
                    r'M1: Common denominator \((x - 2)(x + 1)\) with numerator \(3(x + 1) - 2(x - 2)\) (quy đồng mẫu số) | '
                    r'M1: Correct expansion of numerator: \(3x + 3 - 2x + 4\) (chú ý dấu trừ đổi dấu thành \(+4\)) | '
                    r'A1: \(\frac{x + 7}{(x - 2)(x + 1)}\) (or \(\frac{x + 7}{x^{2} - x - 2}\))'
                ),
            },
        ],
    },
    {
        'question_number': '6',
        'stem': '',
        'sub_questions': [
            {
                'id': 'q6a',
                'type': 'short_answer',
                'label': r'(a) Write \(x^{2} - 8x + 11\) in the form \((x - a)^{2} + b\), where \(a\) and \(b\) are integers.',
                'max_marks': 2,
                'marking_scheme': (
                    r'M1: \((x - 4)^{2} - 16 + 11\) (hoàn thành bình phương với \(a = 4\)) | '
                    r'A1: \((x - 4)^{2} - 5\)'
                ),
            },
            {
                'id': 'q6b',
                'type': 'short_answer',
                'label': r'(b) Hence write down the coordinates of the minimum turning point of the curve \(y = x^{2} - 8x + 11\).',
                'max_marks': 1,
                'marking_scheme': (
                    r'B1: \((4, -5)\) (tọa độ đỉnh parabol từ dạng \((x - a)^{2} + b\) là \((a, b)\))'
                ),
            },
            {
                'id': 'q6c',
                'type': 'structured',
                'label': r'(c) Use your answer to part (a) to solve \(x^{2} - 8x + 11 = 0\), giving your answers in exact surd form.',
                'max_marks': 3,
                'marking_scheme': (
                    r'M1: \((x - 4)^{2} = 5\) | '
                    r'M1: \(x - 4 = \pm \sqrt{5}\) (không quên dấu \(\pm\)) | '
                    r'A1: \(x = 4 + \sqrt{5}\) and \(x = 4 - \sqrt{5}\)'
                ),
            },
        ],
    },
    {
        'question_number': '7',
        'stem': r'The functions \(f\) and \(g\) are defined by \(f(x) = \sqrt{x - 3}\) for \(x \geq 3\), and \(g(x) = 12x^{-\frac{1}{2}}\) for \(x > 0\).',
        'sub_questions': [
            {
                'id': 'q7a',
                'type': 'short_answer',
                'label': r'(a) State the range of \(f(x)\).',
                'max_marks': 1,
                'marking_scheme': (
                    r'B1: \(f(x) \geq 0\) (or \(y \geq 0\); căn bậc hai số học luôn không âm)'
                ),
            },
            {
                'id': 'q7b',
                'type': 'structured',
                'label': r'(b) Find an expression for \(f^{-1}(x)\) and state the domain of \(f^{-1}\).',
                'max_marks': 3,
                'marking_scheme': (
                    r'M1: Let \(y = \sqrt{x - 3} \Rightarrow y^{2} = x - 3 \Rightarrow x = y^{2} + 3\) (đổi biến tìm hàm ngược) | '
                    r'A1: \(f^{-1}(x) = x^{2} + 3\) | '
                    r'B1: Domain of \(f^{-1}\) is \(x \geq 0\) (tập xác định của hàm ngược bằng tập giá trị của \(f\))'
                ),
            },
            {
                'id': 'q7c',
                'type': 'short_answer',
                'label': r'(c) Calculate the exact value of \(g(9) + g(16)\).',
                'max_marks': 2,
                'marking_scheme': (
                    r'M1: \(g(9) = \frac{12}{\sqrt{9}} = 4\) and \(g(16) = \frac{12}{\sqrt{16}} = 3\) (hiểu \(x^{-\frac{1}{2}} = \frac{1}{\sqrt{x}}\)) | '
                    r'A1: \(7\)'
                ),
            },
        ],
    },
    {
        'question_number': '8',
        'stem': '',
        'sub_questions': [
            {
                'id': 'q8',
                'type': 'structured',
                'label': r'Solve the simultaneous equations \(y = 2x - 1\) and \(x^{2} + y^{2} = 13\). Show all your working clearly.',
                'max_marks': 6,
                'marking_scheme': (
                    r'M1: Substitute \(y = 2x - 1\) into \(x^{2} + y^{2} = 13\): \(x^{2} + (2x - 1)^{2} = 13\) (thế phương trình bậc nhất vào bậc hai) | '
                    r'M1: Expand accurately: \(x^{2} + 4x^{2} - 4x + 1 = 13\) | '
                    r'A1: Simplify to \(5x^{2} - 4x - 12 = 0\) | '
                    r'M1: Factorise \((5x + 6)(x - 2) = 0\) (or exact quadratic formula) | '
                    r'A1: \(x = 2, y = 3\) | '
                    r'A1: \(x = -\frac{6}{5}\) (or \(-1.2\)), \(y = -\frac{17}{5}\) (or \(-3.4\))'
                ),
            },
        ],
    },
    {
        'question_number': '9',
        'stem': r'The points \(A(-2, 1)\) and \(B(6, 5)\) lie on the coordinate plane.',
        'sub_questions': [
            {
                'id': 'q9a',
                'type': 'short_answer',
                'label': r'(a) Calculate the exact length of \(AB\), giving your answer in the form \(k\sqrt{5}\).',
                'max_marks': 2,
                'marking_scheme': (
                    r'M1: \(AB = \sqrt{(6 - (-2))^{2} + (5 - 1)^{2}} = \sqrt{8^{2} + 4^{2}} = \sqrt{80}\) | '
                    r'A1: \(4\sqrt{5}\)'
                ),
            },
            {
                'id': 'q9b',
                'type': 'structured',
                'label': r'(b) Find the equation of the perpendicular bisector of \(AB\), giving your answer in the form \(y = mx + c\).',
                'max_marks': 4,
                'marking_scheme': (
                    r'B1: Midpoint \(M = \left(\frac{-2 + 6}{2}, \frac{1 + 5}{2}\right) = (2, 3)\) (trung điểm \(AB\)) | '
                    r'M1: Gradient of \(AB = \frac{5 - 1}{6 - (-2)} = \frac{4}{8} = \frac{1}{2}\) | '
                    r'M1: Perpendicular gradient \(m = -2\) and substitute \((2, 3)\): \(y - 3 = -2(x - 2)\) (hệ số góc vuông góc \(m_1 m_2 = -1\)) | '
                    r'A1: \(y = -2x + 7\)'
                ),
            },
        ],
    },
    {
        'question_number': '10',
        'stem': r'Points \(A, B, C\) and \(D\) lie in anticlockwise order on the circumference of a circle with centre \(O\). The line \(PAT\) is a tangent to the circle at \(A\), with \(B\) on the same side of \(OA\) as \(T\). Given that \(\angle BOC = 112^{\circ}\), \(\angle TAB = 58^{\circ}\), and \(\angle BAD = 74^{\circ}\):',
        'sub_questions': [
            {
                'id': 'q10a',
                'type': 'structured',
                'label': r'(a) Find \(\angle BAC\), giving a geometrical reason for your answer.',
                'max_marks': 2,
                'marking_scheme': (
                    r'B1: \(\angle BAC = 56^{\circ}\) | '
                    r'B1: Angle at the circumference is half the angle at the centre subtended by the same arc \(BC\) (góc nội tiếp bằng nửa góc ở tâm cùng chắn cung \(BC\))'
                ),
            },
            {
                'id': 'q10b',
                'type': 'structured',
                'label': r'(b) Find \(\angle ACB\), giving a geometrical reason for your answer.',
                'max_marks': 2,
                'marking_scheme': (
                    r'B1: \(\angle ACB = 58^{\circ}\) | '
                    r'B1: Alternate segment theorem — angle between tangent \(AT\) and chord \(AB\) equals angle in the alternate segment (góc tạo bởi tia tiếp tuyến và dây cung bằng góc nội tiếp cùng chắn cung \(AB\))'
                ),
            },
            {
                'id': 'q10c',
                'type': 'structured',
                'label': r'(c) Find \(\angle BCD\), giving a geometrical reason for your answer.',
                'max_marks': 2,
                'marking_scheme': (
                    r'B1: \(\angle BCD = 180^{\circ} - 74^{\circ} = 106^{\circ}\) | '
                    r'B1: Opposite angles of a cyclic quadrilateral \(ABCD\) sum to \(180^{\circ}\) (tổng hai góc đối của tứ giác nội tiếp bằng \(180^{\circ}\))'
                ),
            },
        ],
    },
    {
        'question_number': '11',
        'stem': '',
        'sub_questions': [
            {
                'id': 'q11a',
                'type': 'structured',
                'label': r'(a) Without a calculator, find the exact value of \(4\sin 60^{\circ}\cos 30^{\circ} + \tan^{2} 45^{\circ} - 2\sin 30^{\circ}\).',
                'max_marks': 3,
                'marking_scheme': (
                    r'B1: Exact trig values \(\sin 60^{\circ} = \frac{\sqrt{3}}{2}\), \(\cos 30^{\circ} = \frac{\sqrt{3}}{2}\), \(\tan 45^{\circ} = 1\), \(\sin 30^{\circ} = \frac{1}{2}\) (thuộc bảng giá trị lượng giác đặc biệt) | '
                    r'M1: Substitute correctly: \(4\left(\frac{\sqrt{3}}{2}\right)\left(\frac{\sqrt{3}}{2}\right) + 1^{2} - 2\left(\frac{1}{2}\right) = 3 + 1 - 1\) | '
                    r'A1: \(3\)'
                ),
            },
            {
                'id': 'q11b',
                'type': 'structured',
                'label': r'(b) Solve the equation \(2\sin x = \sqrt{3}\) for \(0^{\circ} \leq x \leq 360^{\circ}\).',
                'max_marks': 3,
                'marking_scheme': (
                    r'M1: \(\sin x = \frac{\sqrt{3}}{2}\) | '
                    r'A1: \(x = 60^{\circ}\) | '
                    r'A1: \(x = 180^{\circ} - 60^{\circ} = 120^{\circ}\) (góc phần tư thứ II có \(\sin > 0\))'
                ),
            },
        ],
    },
    {
        'question_number': '12',
        'stem': r'A sector \(OAB\) of a circle has centre \(O\), radius \(12\text{ cm}\), and angle \(\angle AOB = 150^{\circ}\).',
        'sub_questions': [
            {
                'id': 'q12a',
                'type': 'structured',
                'label': r'(a) Calculate the exact perimeter of the sector \(OAB\), giving your answer in the form \(a + b\pi\).',
                'max_marks': 3,
                'marking_scheme': (
                    r'M1: Arc length \(AB = \frac{150}{360} \times 2 \times \pi \times 12\) (công thức độ dài cung tròn) | '
                    r'A1: Arc length \(= 10\pi\text{ cm}\) | '
                    r'A1: Perimeter \(= 24 + 10\pi\text{ cm}\) (nhớ cộng hai bán kính \(12 + 12 = 24\))'
                ),
            },
            {
                'id': 'q12b',
                'type': 'structured',
                'label': r'(b) Calculate the exact area of the minor segment cut off by the chord \(AB\), giving your answer in the form \(p\pi - q\).',
                'max_marks': 3,
                'marking_scheme': (
                    r'M1: Sector area \(= \frac{150}{360} \times \pi \times 12^{2} = 60\pi\text{ cm}^{2}\) | '
                    r'M1: Triangle area \(= \frac{1}{2}(12)(12)\sin 150^{\circ} = 72 \times \frac{1}{2} = 36\text{ cm}^{2}\) (dùng \(\sin 150^{\circ} = \sin 30^{\circ} = \frac{1}{2}\)) | '
                    r'A1: \((60\pi - 36)\text{ cm}^{2}\)'
                ),
            },
        ],
    },
    {
        'question_number': '13',
        'stem': r'In triangle \(OAB\), \(\vec{OA} = \mathbf{a}\) and \(\vec{OB} = \mathbf{b}\). The point \(M\) is the midpoint of \(AB\), the point \(P\) lies on \(OA\) such that \(OP : PA = 2 : 1\), and the point \(Q\) lies on \(OB\) produced such that \(\vec{OQ} = 2\mathbf{b}\).',
        'sub_questions': [
            {
                'id': 'q13a',
                'type': 'short_answer',
                'label': r'(a) Express \(\vec{AB}\) and \(\vec{OM}\) in terms of \(\mathbf{a}\) and \(\mathbf{b}\) in their simplest forms.',
                'max_marks': 2,
                'marking_scheme': (
                    r'B1: \(\vec{AB} = \mathbf{b} - \mathbf{a}\) | '
                    r'B1: \(\vec{OM} = \mathbf{a} + \frac{1}{2}(\mathbf{b} - \mathbf{a}) = \frac{1}{2}\mathbf{a} + \frac{1}{2}\mathbf{b}\)'
                ),
            },
            {
                'id': 'q13b',
                'type': 'short_answer',
                'label': r'(b) Express \(\vec{PM}\) and \(\vec{PQ}\) in terms of \(\mathbf{a}\) and \(\mathbf{b}\).',
                'max_marks': 2,
                'marking_scheme': (
                    r'B1: \(\vec{OP} = \frac{2}{3}\mathbf{a} \Rightarrow \vec{PM} = \vec{OM} - \vec{OP} = -\frac{1}{6}\mathbf{a} + \frac{1}{2}\mathbf{b}\) | '
                    r'B1: \(\vec{PQ} = \vec{OQ} - \vec{OP} = -\frac{2}{3}\mathbf{a} + 2\mathbf{b}\)'
                ),
            },
            {
                'id': 'q13c',
                'type': 'structured',
                'label': r'(c) Use your answers to part (b) to prove that \(P, M\) and \(Q\) are collinear, and state the ratio \(PM : MQ\).',
                'max_marks': 2,
                'marking_scheme': (
                    r'B1: \(\vec{PQ} = 4\vec{PM}\), so \(\vec{PQ}\) is parallel to \(\vec{PM}\) and they share the common point \(P\); hence \(P, M, Q\) are collinear (cùng phương và chung điểm \(P\) nên thẳng hàng) | '
                    r'B1: \(PM : MQ = 1 : 3\) (vì \(PQ = 4PM \Rightarrow MQ = 3PM\))'
                ),
            },
        ],
    },
    {
        'question_number': '14',
        'stem': r'A curve has equation \(y = x^{3} - 3x^{2} - 9x + 5\).',
        'sub_questions': [
            {
                'id': 'q14a',
                'type': 'short_answer',
                'label': r'(a) Find \(\frac{dy}{dx}\).',
                'max_marks': 2,
                'marking_scheme': (
                    r'M1: At least two terms differentiated correctly | '
                    r'A1: \(\frac{dy}{dx} = 3x^{2} - 6x - 9\)'
                ),
            },
            {
                'id': 'q14b',
                'type': 'structured',
                'label': r'(b) Find the coordinates of the two stationary points on the curve.',
                'max_marks': 4,
                'marking_scheme': (
                    r'M1: Set \(\frac{dy}{dx} = 0\): \(3x^{2} - 6x - 9 = 0 \Rightarrow x^{2} - 2x - 3 = 0\) (điểm dừng khi đạo hàm bằng \(0\)) | '
                    r'M1: Factorise \((x - 3)(x + 1) = 0 \Rightarrow x = 3\) or \(x = -1\) | '
                    r'A1: When \(x = 3, y = 27 - 27 - 27 + 5 = -22 \Rightarrow (3, -22)\) | '
                    r'A1: When \(x = -1, y = -1 - 3 + 9 + 5 = 10 \Rightarrow (-1, 10)\)'
                ),
            },
        ],
    },
    {
        'question_number': '15',
        'stem': r'In a class of \(40\) students, \(24\) study French (\(F\)), \(18\) study Spanish (\(S\)), and \(5\) study neither language.',
        'sub_questions': [
            {
                'id': 'q15a',
                'type': 'short_answer',
                'label': r'(a) Find the number of students who study both French and Spanish.',
                'max_marks': 2,
                'marking_scheme': (
                    r'M1: \(n(F \cup S) = 40 - 5 = 35\) and \(n(F \cap S) = 24 + 18 - 35\) (áp dụng công thức biểu đồ Venn) | '
                    r'A1: \(7\)'
                ),
            },
            {
                'id': 'q15b',
                'type': 'short_answer',
                'label': r'(b) One student is chosen at random from the class. Find the probability that this student studies Spanish, given that they study French.',
                'max_marks': 2,
                'marking_scheme': (
                    r'M1: Conditional probability denominator \(n(F) = 24\) with numerator \(n(F \cap S) = 7\) (xác suất có điều kiện) | '
                    r'A1: \(\frac{7}{24}\)'
                ),
            },
            {
                'id': 'q15c',
                'type': 'structured',
                'label': r'(c) Two students are chosen at random from the \(40\) students without replacement. Find the exact probability that both study neither language.',
                'max_marks': 3,
                'marking_scheme': (
                    r'M1: First student probability \(\frac{5}{40}\), second student (without replacement) \(\frac{4}{39}\) (chọn không hoàn lại) | '
                    r'M1: Multiply: \(\frac{5}{40} \times \frac{4}{39} = \frac{20}{1560}\) | '
                    r'A1: \(\frac{1}{78}\)'
                ),
            },
        ],
    },
    {
        'question_number': '16',
        'stem': r'Triangle \(T\) has vertices \(A(2, 1)\), \(B(4, 1)\) and \(C(4, 2)\).',
        'sub_questions': [
            {
                'id': 'q16a',
                'type': 'short_answer',
                'label': r'(a) Triangle \(T\) is reflected in the line \(y = x\) to form triangle \(T_{1}\). State the coordinates of the vertices of \(T_{1}\).',
                'max_marks': 2,
                'marking_scheme': (
                    r'M1: Rule \((x, y) \rightarrow (y, x)\) applied to at least two vertices (đối xứng qua \(y = x\) đổi chỗ hoành độ và tung độ) | '
                    r'A1: \(A_{1}(1, 2)\), \(B_{1}(1, 4)\), \(C_{1}(2, 4)\)'
                ),
            },
            {
                'id': 'q16b',
                'type': 'short_answer',
                'label': r'(b) Triangle \(T\) is enlarged with centre \((0, 1)\) and scale factor \(-2\) to form triangle \(T_{2}\). Find the coordinates of the vertices of \(T_{2}\).',
                'max_marks': 2,
                'marking_scheme': (
                    r'M1: Multiply displacement vectors from \((0, 1)\) by \(-2\): e.g. \((2, 0) \rightarrow (-4, 0)\) (phép vị tự tỉ số âm \(-2\) tâm \((0, 1)\)) | '
                    r'A1: \(A_{2}(-4, 1)\), \(B_{2}(-8, 1)\), \(C_{2}(-8, -1)\)'
                ),
            },
            {
                'id': 'q16c',
                'type': 'structured',
                'label': r'(c) Triangle \(T_{3}\) has vertices \((-1, 2)\), \((-1, 4)\) and \((-2, 4)\). Describe fully the single transformation that maps triangle \(T\) onto triangle \(T_{3}\).',
                'max_marks': 2,
                'marking_scheme': (
                    r'B1: Rotation through \(90^{\circ}\) anticlockwise (or \(270^{\circ}\) clockwise) (phép quay \(90^{\circ}\) ngược chiều kim đồng hồ) | '
                    r'B1: Centre \((0, 0)\) (the origin) — check \((x, y) \rightarrow (-y, x)\)'
                ),
            },
        ],
    },
    {
        'question_number': '17',
        'stem': '',
        'sub_questions': [
            {
                'id': 'q17a',
                'type': 'structured',
                'label': r'(a) A list of \(5\) positive integers has a mean of \(14\), a median of \(15\), a unique mode of \(16\), and a range of \(6\). Find the \(5\) integers.',
                'max_marks': 3,
                'marking_scheme': (
                    r'M1: Sum \(= 5 \times 14 = 70\); median \(= 15\) and unique mode \(= 16\) forces largest two integers to be \(16, 16\) | '
                    r'M1: Range \(= 6 \Rightarrow\) smallest integer \(= 16 - 6 = 10\), so second integer \(= 70 - (10 + 15 + 16 + 16) = 13\) | '
                    r'A1: \(10, 13, 15, 16, 16\)'
                ),
            },
            {
                'id': 'q17b',
                'type': 'structured',
                'label': r'(b) \(y\) is inversely proportional to \(\sqrt{x}\). When \(x = 16\), \(y = 6\). Find the value of \(x\) when \(y = 8\).',
                'max_marks': 3,
                'marking_scheme': (
                    r'M1: \(y = \frac{k}{\sqrt{x}}\), substitute \(x = 16, y = 6 \Rightarrow k = 6 \times 4 = 24\) (tỉ lệ nghịch với \(\sqrt{x}\)) | '
                    r'M1: Set \(8 = \frac{24}{\sqrt{x}} \Rightarrow \sqrt{x} = 3\) | '
                    r'A1: \(x = 9\)'
                ),
            },
        ],
    },
]

# =============================================================================
# PAPER 2: 0580/22 — Paper 2 (Extended — Non-Calculator) Full Mock #2 (100 marks)
# =============================================================================
PAPER_0580_P2_2_QUESTIONS = [
    {
        'question_number': '1',
        'stem': r'A rectangular card has length \(L = 12\text{ cm}\) and width \(W = 8\text{ cm}\), both measured correct to the nearest centimetre.',
        'sub_questions': [
            {
                'id': 'q1a',
                'type': 'short_answer',
                'label': r'(a) Write down the lower bound and the upper bound of \(L\).',
                'max_marks': 1,
                'marking_scheme': (
                    r'B1: Lower bound \(= 11.5\text{ cm}\), upper bound \(= 12.5\text{ cm}\) (sai số \(\pm 0.5\text{ cm}\))'
                ),
            },
            {
                'id': 'q1b',
                'type': 'short_answer',
                'label': r'(b) Calculate the upper bound of the perimeter of the card.',
                'max_marks': 2,
                'marking_scheme': (
                    r'M1: \(2(L_{\max} + W_{\max}) = 2(12.5 + 8.5)\) (lấy cận trên của cả chiều dài và chiều rộng) | '
                    r'A1: \(42\text{ cm}\)'
                ),
            },
            {
                'id': 'q1c',
                'type': 'structured',
                'label': r'(c) A piece of string has length \(S = 40\text{ cm}\), measured correct to the nearest \(2\text{ cm}\). Calculate the upper bound of \(\frac{S}{W}\), giving your answer as an exact improper fraction in its simplest form.',
                'max_marks': 2,
                'marking_scheme': (
                    r'M1: \(\frac{S_{\max}}{W_{\min}} = \frac{41}{7.5}\) (tử lấy cận trên \(40 + 1 = 41\), mẫu lấy cận dưới \(8 - 0.5 = 7.5\)) | '
                    r'A1: \(\frac{82}{15}\)'
                ),
            },
        ],
    },
    {
        'question_number': '2',
        'stem': '',
        'sub_questions': [
            {
                'id': 'q2a',
                'type': 'short_answer',
                'label': r'(a) Simplify \((\sqrt{48} + \sqrt{27}) \div \sqrt{3}\).',
                'max_marks': 2,
                'marking_scheme': (
                    r'M1: \(\sqrt{48} = 4\sqrt{3}\) and \(\sqrt{27} = 3\sqrt{3}\) (or \(\sqrt{16} + \sqrt{9}\)) | '
                    r'A1: \(7\)'
                ),
            },
            {
                'id': 'q2b',
                'type': 'structured',
                'label': r'(b) Show that \(10 / (\sqrt{7} - \sqrt{2}) - 2\sqrt{7}\) simplifies to \(2\sqrt{2}\).',
                'max_marks': 4,
                'marking_scheme': (
                    r'M1: Multiply first term by \(\frac{\sqrt{7} + \sqrt{2}}{\sqrt{7} + \sqrt{2}}\) (nhân lượng liên hợp) | '
                    r'M1: Denominator \((\sqrt{7})^{2} - (\sqrt{2})^{2} = 7 - 2 = 5\) | '
                    r'A1: First term becomes \(\frac{10(\sqrt{7} + \sqrt{2})}{5} = 2\sqrt{7} + 2\sqrt{2}\) | '
                    r'A1: \(2\sqrt{7} + 2\sqrt{2} - 2\sqrt{7} = 2\sqrt{2}\) clearly shown'
                ),
            },
        ],
    },
    {
        'question_number': '3',
        'stem': '',
        'sub_questions': [
            {
                'id': 'q3a',
                'type': 'structured',
                'label': r'(a) Convert the recurring decimal \(0.2454545...\) (where the digits \(45\) recur) into a fraction in its simplest form.',
                'max_marks': 3,
                'marking_scheme': (
                    r'M1: Let \(x = 0.2454545...\), write \(10x = 2.454545...\) and \(1000x = 245.454545...\) (nhân \(10\) và \(1000\) để phần thập phân giống hệt nhau) | '
                    r'M1: Subtract: \(990x = 243 \Rightarrow x = \frac{243}{990}\) | '
                    r'A1: \(\frac{27}{110}\) (rút gọn cho \(9\))'
                ),
            },
            {
                'id': 'q3b',
                'type': 'short_answer',
                'label': r'(b) Find the exact value of \(\left(\frac{16}{81}\right)^{-\frac{3}{4}}\).',
                'max_marks': 2,
                'marking_scheme': (
                    r'M1: Invert for negative index and take \(4\)th root: \(\left(\frac{81}{16}\right)^{\frac{3}{4}} = \left(\frac{3}{2}\right)^{3}\) | '
                    r'A1: \(\frac{27}{8}\) (or \(3.375\))'
                ),
            },
        ],
    },
    {
        'question_number': '4',
        'stem': '',
        'sub_questions': [
            {
                'id': 'q4a',
                'type': 'short_answer',
                'label': r'(a) In a sale, all prices are reduced by \(15\)%. A jacket costs £\(68\) in the sale. Calculate the original price of the jacket.',
                'max_marks': 2,
                'marking_scheme': (
                    r'M1: \(85\)% \(= 68 \Rightarrow \text{Original price} = \frac{68}{0.85}\) (tính phần trăm ngược) | '
                    r'A1: £\(80\)'
                ),
            },
            {
                'id': 'q4b',
                'type': 'structured',
                'label': r'(b) £\(450\) is shared between Ali, Ben and Chloe in the ratio \(2 : 5 : 8\). Chloe then gives \(25\)% of her share to Ali. Find the new ratio of Ali : Ben : Chloe in its simplest form.',
                'max_marks': 3,
                'marking_scheme': (
                    r'M1: \(1\) part \(= \frac{450}{15} = 30\), so initial shares are Ali £\(60\), Ben £\(150\), Chloe £\(240\) | '
                    r'M1: Chloe gives \(25\)% \(\times 240 = 60\) to Ali \(\Rightarrow\) new shares \(120 : 150 : 180\) | '
                    r'A1: \(4 : 5 : 6\)'
                ),
            },
        ],
    },
    {
        'question_number': '5',
        'stem': r'The functions \(f, g\) and \(h\) are defined by \(f(x) = \frac{3x - 1}{2}\), \(g(x) = x^{2} + 4\) for \(x \geq 0\), and \(h(x) = 2x^{-\frac{1}{2}}\) for \(x > 0\).',
        'sub_questions': [
            {
                'id': 'q5a',
                'type': 'short_answer',
                'label': r'(a) Find \(fg(x)\) in its simplest form.',
                'max_marks': 2,
                'marking_scheme': (
                    r'M1: \(f(g(x)) = \frac{3(x^{2} + 4) - 1}{2}\) (thế \(g(x)\) vào \(f\)) | '
                    r'A1: \(\frac{3x^{2} + 11}{2}\)'
                ),
            },
            {
                'id': 'q5b',
                'type': 'short_answer',
                'label': r'(b) Find \(g^{-1}(x)\) and state the domain of \(g^{-1}\).',
                'max_marks': 2,
                'marking_scheme': (
                    r'B1: \(g^{-1}(x) = \sqrt{x - 4}\) (chọn căn dương vì tập xác định của \(g\) là \(x \geq 0\)) | '
                    r'B1: Domain of \(g^{-1}\) is \(x \geq 4\) (bằng tập giá trị của \(g\))'
                ),
            },
            {
                'id': 'q5c',
                'type': 'short_answer',
                'label': r'(c) Solve the equation \(h(x) = \frac{1}{3}\).',
                'max_marks': 2,
                'marking_scheme': (
                    r'M1: \(\frac{2}{\sqrt{x}} = \frac{1}{3} \Rightarrow \sqrt{x} = 6\) | '
                    r'A1: \(x = 36\)'
                ),
            },
        ],
    },
    {
        'question_number': '6',
        'stem': '',
        'sub_questions': [
            {
                'id': 'q6a',
                'type': 'structured',
                'label': r'(a) Rearrange the formula \(p = \frac{3t + 4}{t - 2}\) to make \(t\) the subject.',
                'max_marks': 3,
                'marking_scheme': (
                    r'M1: Multiply both sides by \((t - 2)\): \(pt - 2p = 3t + 4\) | '
                    r'M1: Collect \(t\) terms and factorise: \(t(p - 3) = 2p + 4\) (gom hạng tử chứa \(t\) về một vế) | '
                    r'A1: \(t = \frac{2p + 4}{p - 3}\)'
                ),
            },
            {
                'id': 'q6b',
                'type': 'structured',
                'label': r'(b) Solve the quadratic inequality \(2x^{2} - 5x - 12 \leq 0\).',
                'max_marks': 3,
                'marking_scheme': (
                    r'M1: Factorise \((2x + 3)(x - 4) = 0\) (phân tích nhân tử tìm nghiệm biên) | '
                    r'A1: Critical values \(x = -\frac{3}{2}\) and \(x = 4\) | '
                    r'A1: \(-\frac{3}{2} \leq x \leq 4\) (vì hệ số \(a = 2 > 0\), biểu thức \(\leq 0\) nằm giữa hai nghiệm)'
                ),
            },
        ],
    },
    {
        'question_number': '7',
        'stem': '',
        'sub_questions': [
            {
                'id': 'q7a',
                'type': 'structured',
                'label': r'(a) Find an expression for the \(n\)th term of the quadratic sequence \(5, 11, 21, 35, 53, ...\).',
                'max_marks': 3,
                'marking_scheme': (
                    r'M1: First differences \(6, 10, 14, 18\) and constant second difference \(4\), giving coefficient of \(n^{2}\) as \(\frac{4}{2} = 2\) (sai phân bậc hai bằng \(2a\)) | '
                    r'M1: Subtract \(2n^{2}\) (\(2, 8, 18, 32, 50\)) from sequence to obtain constant \(3\) | '
                    r'A1: \(2n^{2} + 3\)'
                ),
            },
            {
                'id': 'q7b',
                'type': 'structured',
                'label': r'(b) Another sequence has \(n\)th term \(T_{n} = \frac{n + 2}{3n - 1}\). Find the value of \(n\) for which \(T_{n} = \frac{9}{20}\).',
                'max_marks': 3,
                'marking_scheme': (
                    r'M1: Set \(\frac{n + 2}{3n - 1} = \frac{9}{20}\) and cross-multiply: \(20(n + 2) = 9(3n - 1)\) | '
                    r'M1: \(20n + 40 = 27n - 9 \Rightarrow 7n = 49\) | '
                    r'A1: \(n = 7\)'
                ),
            },
        ],
    },
    {
        'question_number': '8',
        'stem': r'A train starts from rest and accelerates uniformly for \(20\) seconds to reach a speed of \(v\text{ m/s}\). It then travels at this constant speed \(v\text{ m/s}\) for \(50\) seconds, before decelerating uniformly to rest in a further \(30\) seconds. The total distance travelled by the train is \(1875\text{ m}\).',
        'sub_questions': [
            {
                'id': 'q8a',
                'type': 'structured',
                'label': r'(a) Calculate the value of \(v\).',
                'max_marks': 3,
                'marking_scheme': (
                    r'M1: Total time \(= 20 + 50 + 30 = 100\text{ s}\); area of speed-time trapezium \(= \frac{1}{2}(50 + 100)v\) (quãng đường bằng diện tích hình thang dưới đồ thị \(v\)–\(t\)) | '
                    r'M1: \(75v = 1875\) | '
                    r'A1: \(v = 25\text{ m/s}\)'
                ),
            },
            {
                'id': 'q8b',
                'type': 'short_answer',
                'label': r'(b) Calculate the acceleration of the train during the first \(20\) seconds.',
                'max_marks': 1,
                'marking_scheme': (
                    r'B1: \(a = \frac{25}{20} = 1.25\text{ m/s}^{2}\) (or \(\frac{5}{4}\text{ m/s}^{2}\))'
                ),
            },
            {
                'id': 'q8c',
                'type': 'short_answer',
                'label': r'(c) Calculate the distance travelled by the train during the last \(30\) seconds.',
                'max_marks': 2,
                'marking_scheme': (
                    r'M1: Area of final triangle \(= \frac{1}{2} \times 30 \times 25\) | '
                    r'A1: \(375\text{ m}\)'
                ),
            },
        ],
    },
    {
        'question_number': '9',
        'stem': '',
        'sub_questions': [
            {
                'id': 'q9a',
                'type': 'structured',
                'label': r'(a) Solve the equation \(2\cos x = -1\) for \(0^{\circ} \leq x \leq 360^{\circ}\).',
                'max_marks': 3,
                'marking_scheme': (
                    r'M1: \(\cos x = -\frac{1}{2}\), basic acute angle \(= 60^{\circ}\) (vì \(\cos 60^{\circ} = \frac{1}{2}\)) | '
                    r'A1: \(x = 180^{\circ} - 60^{\circ} = 120^{\circ}\) (góc phần tư II) | '
                    r'A1: \(x = 180^{\circ} + 60^{\circ} = 240^{\circ}\) (góc phần tư III)'
                ),
            },
            {
                'id': 'q9b',
                'type': 'structured',
                'label': r'(b) In triangle \(PQR\), \(PQ = 8\text{ cm}\), \(PR = 6\sqrt{3}\text{ cm}\) and \(\angle QPR = 30^{\circ}\). Without a calculator, find the exact length of \(QR\) in its simplest surd form.',
                'max_marks': 3,
                'marking_scheme': (
                    r'M1: Apply Cosine Rule: \(QR^{2} = 8^{2} + (6\sqrt{3})^{2} - 2(8)(6\sqrt{3})\cos 30^{\circ}\) | '
                    r'M1: Substitute \(\cos 30^{\circ} = \frac{\sqrt{3}}{2}\): \(QR^{2} = 64 + 108 - 96\sqrt{3}\left(\frac{\sqrt{3}}{2}\right) = 172 - 144 = 28\) | '
                    r'A1: \(QR = \sqrt{28} = 2\sqrt{7}\text{ cm}\)'
                ),
            },
        ],
    },
    {
        'question_number': '10',
        'stem': '',
        'sub_questions': [
            {
                'id': 'q10a',
                'type': 'structured',
                'label': r'(a) The interior angle of a regular polygon is \(5\) times its exterior angle. Calculate the number of sides of the polygon.',
                'max_marks': 3,
                'marking_scheme': (
                    r'M1: Let exterior angle be \(e\); then \(5e + e = 180^{\circ}\) (góc trong + góc ngoài \(= 180^{\circ}\)) | '
                    r'A1: \(e = 30^{\circ}\) | '
                    r'A1: Number of sides \(n = \frac{360^{\circ}}{30^{\circ}} = 12\)'
                ),
            },
            {
                'id': 'q10b',
                'type': 'structured',
                'label': r'(b) In trapezium \(PQRS\), side \(PQ\) is parallel to side \(SR\), with \(PQ = 6\text{ cm}\) and \(SR = 15\text{ cm}\). The diagonals \(PR\) and \(QS\) intersect at \(X\). Prove that triangles \(PXQ\) and \(RXS\) are similar, and given \(PX = 4\text{ cm}\), find the exact length of \(PR\).',
                'max_marks': 3,
                'marking_scheme': (
                    r'B1: \(\angle QPX = \angle SRX\) and \(\angle PQX = \angle RSX\) (alternate angles, \(PQ \parallel SR\)), and \(\angle PXQ = \angle RXS\) (vertically opposite), so \(\triangle PXQ \sim \triangle RXS\) by AAA (đồng dạng góc–góc–góc) | '
                    r'M1: Scale factor \(= \frac{SR}{PQ} = \frac{15}{6} = \frac{5}{2}\), so \(RX = 4 \times \frac{5}{2} = 10\text{ cm}\) | '
                    r'A1: \(PR = PX + RX = 4 + 10 = 14\text{ cm}\)'
                ),
            },
        ],
    },
    {
        'question_number': '11',
        'stem': r'A solid metal cylinder has base radius \(4\text{ cm}\) and height \(6\text{ cm}\).',
        'sub_questions': [
            {
                'id': 'q11a',
                'type': 'short_answer',
                'label': r'(a) Calculate the exact volume of the cylinder in terms of \(\pi\).',
                'max_marks': 2,
                'marking_scheme': (
                    r'M1: \(V = \pi r^{2} h = \pi \times 4^{2} \times 6\) | '
                    r'A1: \(96\pi\text{ cm}^{3}\)'
                ),
            },
            {
                'id': 'q11b',
                'type': 'short_answer',
                'label': r'(b) The cylinder is melted down and recast, with no metal wasted, into a solid right circular cone of base radius \(6\text{ cm}\). Calculate the height of the cone.',
                'max_marks': 2,
                'marking_scheme': (
                    r'M1: \(\frac{1}{3}\pi (6^{2}) H = 96\pi \Rightarrow 12H = 96\) (bảo toàn thể tích) | '
                    r'A1: \(H = 8\text{ cm}\)'
                ),
            },
            {
                'id': 'q11c',
                'type': 'short_answer',
                'label': r'(c) Calculate the exact total surface area of the cone in terms of \(\pi\).',
                'max_marks': 2,
                'marking_scheme': (
                    r'M1: Slant height \(l = \sqrt{6^{2} + 8^{2}} = 10\text{ cm}\); \(\text{TSA} = \pi r l + \pi r^{2} = \pi(6)(10) + \pi(6^{2})\) (diện tích xung quanh + diện tích đáy) | '
                    r'A1: \(96\pi\text{ cm}^{2}\)'
                ),
            },
        ],
    },
    {
        'question_number': '12',
        'stem': r'The straight line \(L_{1}\) has equation \(3x + 2y = 12\).',
        'sub_questions': [
            {
                'id': 'q12a',
                'type': 'short_answer',
                'label': r'(a) State the gradient of \(L_{1}\) and the coordinates of the points \(A\) and \(B\) where \(L_{1}\) crosses the \(x\)-axis and \(y\)-axis respectively.',
                'max_marks': 2,
                'marking_scheme': (
                    r'B1: Gradient \(= -\frac{3}{2}\) (viết lại \(y = -\frac{3}{2}x + 6\)) | '
                    r'B1: \(A(4, 0)\) and \(B(0, 6)\)'
                ),
            },
            {
                'id': 'q12b',
                'type': 'short_answer',
                'label': r'(b) Line \(L_{2}\) is perpendicular to \(L_{1}\) and passes through \((5, 5)\). Find the equation of \(L_{2}\) in the form \(ax + by + c = 0\), where \(a, b, c\) are integers.',
                'max_marks': 2,
                'marking_scheme': (
                    r'M1: Perpendicular gradient \(= \frac{2}{3}\) and \(y - 5 = \frac{2}{3}(x - 5)\) | '
                    r'A1: \(2x - 3y + 5 = 0\) (or equivalent integer multiple)'
                ),
            },
            {
                'id': 'q12c',
                'type': 'short_answer',
                'label': r'(c) Find the coordinates of the point of intersection of \(L_{1}\) and \(L_{2}\).',
                'max_marks': 2,
                'marking_scheme': (
                    r'M1: Solve \(3x + 2y = 12\) and \(2x - 3y = -5\) simultaneously (e.g. \(9x + 6y = 36\) and \(4x - 6y = -10 \Rightarrow 13x = 26\)) | '
                    r'A1: \((2, 3)\)'
                ),
            },
        ],
    },
    {
        'question_number': '13',
        'stem': r'The universal set \(U\) consists of the integers from \(1\) to \(12\) inclusive: \(U =\) {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}. Sets \(A, B\) and \(C\) are defined by \(A =\) {even numbers}, \(B =\) {multiples of 3}, and \(C =\) {prime numbers}.',
        'sub_questions': [
            {
                'id': 'q13a',
                'type': 'short_answer',
                'label': r'(a) List the elements of \(A \cap B\) and \(A \cap C\).',
                'max_marks': 2,
                'marking_scheme': (
                    r'B1: \(A \cap B = \{6, 12\}\) | '
                    r'B1: \(A \cap C = \{2\}\) (số nguyên tố chẵn duy nhất là \(2\))'
                ),
            },
            {
                'id': 'q13b',
                'type': 'short_answer',
                'label': r"(b) List the elements of \((A \cup B)' \cap C\).",
                'max_marks': 2,
                'marking_scheme': (
                    r"M1: \((A \cup B)' = \{1, 5, 7, 11\}\) (phần bù của hợp \(A \cup B\) trong \(U\)) | "
                    r'A1: \(\{5, 7, 11\}\)'
                ),
            },
            {
                'id': 'q13c',
                'type': 'short_answer',
                'label': r"(c) Find \(n((A \cup B \cup C)')\) and list the element(s) in \((A \cup B \cup C)'\).",
                'max_marks': 2,
                'marking_scheme': (
                    r"B1: \((A \cup B \cup C)' = \{1\}\) (lưu ý \(1\) không phải là số nguyên tố) | "
                    r"B1: \(n((A \cup B \cup C)') = 1\)"
                ),
            },
        ],
    },
    {
        'question_number': '14',
        'stem': r'The curve \(C\) has equation \(y = 2x^{3} - 9x^{2} + 12x + 1\).',
        'sub_questions': [
            {
                'id': 'q14a',
                'type': 'short_answer',
                'label': r'(a) Find \(\frac{dy}{dx}\).',
                'max_marks': 2,
                'marking_scheme': (
                    r'M1: At least two terms differentiated correctly | '
                    r'A1: \(\frac{dy}{dx} = 6x^{2} - 18x + 12\)'
                ),
            },
            {
                'id': 'q14b',
                'type': 'short_answer',
                'label': r'(b) Find the equation of the tangent to \(C\) at the point where \(x = 3\), giving your answer in the form \(y = mx + c\).',
                'max_marks': 2,
                'marking_scheme': (
                    r'M1: At \(x = 3\): \(y = 54 - 81 + 36 + 1 = 10\) and \(m = 6(9) - 18(3) + 12 = 12\) | '
                    r'A1: \(y - 10 = 12(x - 3) \Rightarrow y = 12x - 26\)'
                ),
            },
            {
                'id': 'q14c',
                'type': 'structured',
                'label': r'(c) Find the coordinates of the two stationary points on \(C\) and determine which is a local maximum and which is a local minimum.',
                'max_marks': 3,
                'marking_scheme': (
                    r'M1: \(6(x^{2} - 3x + 2) = 0 \Rightarrow (x - 1)(x - 2) = 0 \Rightarrow x = 1, 2\) | '
                    r'A1: Stationary points \((1, 6)\) and \((2, 5)\) | '
                    r'A1: Using \(\frac{d^{2}y}{dx^{2}} = 12x - 18\): at \(x = 1, y^{\prime\prime} = -6 < 0 \Rightarrow (1, 6)\) local maximum; at \(x = 2, y^{\prime\prime} = +6 > 0 \Rightarrow (2, 5)\) local minimum'
                ),
            },
        ],
    },
    {
        'question_number': '15',
        'stem': r'Two vectors in component form are given by \(\mathbf{p} = (3, -4)\) and \(\mathbf{q} = (-2, 5)\).',
        'sub_questions': [
            {
                'id': 'q15a',
                'type': 'short_answer',
                'label': r'(a) Calculate the exact magnitude \(|\mathbf{p}|\).',
                'max_marks': 1,
                'marking_scheme': (
                    r'B1: \(|\mathbf{p}| = \sqrt{3^{2} + (-4)^{2}} = \sqrt{25} = 5\)'
                ),
            },
            {
                'id': 'q15b',
                'type': 'short_answer',
                'label': r'(b) Find \(2\mathbf{p} - 3\mathbf{q}\) in component form.',
                'max_marks': 2,
                'marking_scheme': (
                    r'M1: \((6, -8) - (-6, 15)\) | '
                    r'A1: \((12, -23)\)'
                ),
            },
            {
                'id': 'q15c',
                'type': 'structured',
                'label': r'(c) Find the value of the scalar \(k\) such that \(\mathbf{p} + k\mathbf{q}\) is parallel to the vector \((1, 1)\).',
                'max_marks': 3,
                'marking_scheme': (
                    r'M1: \(\mathbf{p} + k\mathbf{q} = (3 - 2k, -4 + 5k)\) | '
                    r'M1: Parallel to \((1, 1)\) means \(3 - 2k = -4 + 5k \Rightarrow 7k = 7\) (hai thành phần bằng nhau) | '
                    r'A1: \(k = 1\)'
                ),
            },
        ],
    },
    {
        'question_number': '16',
        'stem': r'A bag contains \(5\) red counters and \(3\) blue counters. Counters are drawn at random one after another without replacement.',
        'sub_questions': [
            {
                'id': 'q16a',
                'type': 'short_answer',
                'label': r'(a) Two counters are drawn. Find the exact probability that both counters are red.',
                'max_marks': 2,
                'marking_scheme': (
                    r'M1: \(\frac{5}{8} \times \frac{4}{7}\) (rút không hoàn lại) | '
                    r'A1: \(\frac{5}{14}\)'
                ),
            },
            {
                'id': 'q16b',
                'type': 'short_answer',
                'label': r'(b) Two counters are drawn. Find the exact probability that the two counters are of different colours.',
                'max_marks': 2,
                'marking_scheme': (
                    r'M1: \(P(RB) + P(BR) = \frac{5}{8}\times\frac{3}{7} + \frac{3}{8}\times\frac{5}{7} = \frac{30}{56}\) | '
                    r'A1: \(\frac{15}{28}\)'
                ),
            },
            {
                'id': 'q16c',
                'type': 'short_answer',
                'label': r'(c) A third counter is also drawn without replacement. Find the exact probability that all three counters are the same colour.',
                'max_marks': 2,
                'marking_scheme': (
                    r'M1: \(P(RRR) + P(BBB) = \frac{5}{8}\times\frac{4}{7}\times\frac{3}{6} + \frac{3}{8}\times\frac{2}{7}\times\frac{1}{6} = \frac{66}{336}\) | '
                    r'A1: \(\frac{11}{56}\)'
                ),
            },
        ],
    },
    {
        'question_number': '17',
        'stem': '',
        'sub_questions': [
            {
                'id': 'q17',
                'type': 'structured',
                'label': r'Solve the equation \(\frac{2}{x - 1} + \frac{5}{x + 2} = 2\). Show all your algebraic working clearly.',
                'max_marks': 6,
                'marking_scheme': (
                    r'M1: Multiply through by \((x - 1)(x + 2)\): \(2(x + 2) + 5(x - 1) = 2(x - 1)(x + 2)\) (khử mẫu số) | '
                    r'M1: Expand both sides accurately: \(7x - 1 = 2x^{2} + 2x - 4\) | '
                    r'A1: Rearrange to standard quadratic \(2x^{2} - 5x - 3 = 0\) | '
                    r'M1: Factorise \((2x + 1)(x - 3) = 0\) | '
                    r'A1: \(x = 3\) | '
                    r'A1: \(x = -\frac{1}{2}\) (or \(-0.5\))'
                ),
            },
        ],
    },
]

# =============================================================================
# PAPER 3: 0580/41 — Paper 4 (Extended — Calculator) Full Mock #1 (100 marks)
# =============================================================================
PAPER_0580_P4_1_QUESTIONS = [
    {
        'question_number': '1',
        'stem': r'Maya manages her personal savings and travel budget.',
        'sub_questions': [
            {
                'id': 'q1a',
                'type': 'structured',
                'label': r'(a) Maya invests £\(4500\) in an account paying \(3.6\)% per year compound interest. Calculate the total value of her investment after \(5\) years, correct to the nearest penny.',
                'max_marks': 3,
                'marking_scheme': (
                    r'M1: Compound multiplier \(1.036^{5}\) | '
                    r'M1: \(4500 \times 1.036^{5} = 5370.4576...\) (công thức lãi kép \(P(1 + r)^{n}\)) | '
                    r'A1: £\(5370.46\)'
                ),
            },
            {
                'id': 'q1b',
                'type': 'structured',
                'label': r'(b) In a different savings account paying \(r\)% per year compound interest, an investment of £\(2000\) grows to £\(2385.04\) after \(4\) years. Calculate the value of \(r\), correct to \(1\) decimal place.',
                'max_marks': 3,
                'marking_scheme': (
                    r'M1: \(2000\left(1 + \frac{r}{100}\right)^{4} = 2385.04 \Rightarrow \left(1 + \frac{r}{100}\right)^{4} = 1.19252\) | '
                    r'M1: Take \(4\)th root: \(1 + \frac{r}{100} = (1.19252)^{\frac{1}{4}} = 1.045000...\) | '
                    r'A1: \(r = 4.5\)'
                ),
            },
            {
                'id': 'q1c',
                'type': 'short_answer',
                'label': r'(c) A laptop is reduced by \(18\)% in a sale to £\(779\). Calculate the original price of the laptop before the reduction.',
                'max_marks': 2,
                'marking_scheme': (
                    r'M1: \(\frac{779}{0.82}\) (giá sau giảm ứng với \(82\)%) | '
                    r'A1: £\(950\)'
                ),
            },
            {
                'id': 'q1d',
                'type': 'short_answer',
                'label': r'(d) The exchange rate is £\(1 = 1.27\text{ USD}\). Maya changes £\(640\) into USD, spends \(350\text{ USD}\), and converts the remaining USD back into pounds at £\(1 = 1.30\text{ USD}\). Calculate how much she receives in pounds.',
                'max_marks': 2,
                'marking_scheme': (
                    r'M1: \(640 \times 1.27 = 812.80\text{ USD}\); remaining \(= 812.80 - 350 = 462.80\text{ USD}\); \(\frac{462.80}{1.30}\) | '
                    r'A1: £\(356\) (or £\(356.00\))'
                ),
            },
        ],
    },
    {
        'question_number': '2',
        'stem': r'The functions \(f\) and \(g\) are defined by \(f(x) = 3x - 4\) and \(g(x) = \frac{10}{x + 2}\) for \(x > -2\).',
        'sub_questions': [
            {
                'id': 'q2a',
                'type': 'short_answer',
                'label': r'(a) Calculate \(fg(3)\).',
                'max_marks': 1,
                'marking_scheme': (
                    r'B1: \(g(3) = \frac{10}{5} = 2 \Rightarrow f(2) = 3(2) - 4 = 2\)'
                ),
            },
            {
                'id': 'q2b',
                'type': 'structured',
                'label': r'(b) State the range of \(g(x)\), find \(g^{-1}(x)\), and state the domain of \(g^{-1}\).',
                'max_marks': 4,
                'marking_scheme': (
                    r'B1: Range of \(g\) is \(g(x) > 0\) (vì \(x + 2 > 0 \Rightarrow \frac{10}{x + 2} > 0\)) | '
                    r'M1: \(y = \frac{10}{x + 2} \Rightarrow x + 2 = \frac{10}{y} \Rightarrow x = \frac{10}{y} - 2\) | '
                    r'A1: \(g^{-1}(x) = \frac{10}{x} - 2\) (or \(\frac{10 - 2x}{x}\)) | '
                    r'B1: Domain of \(g^{-1}\) is \(x > 0\)'
                ),
            },
            {
                'id': 'q2ci',
                'type': 'structured',
                'label': r'(c)(i) Show that the equation \(fg(x) = 2x\) reduces to \(x^{2} + 4x - 11 = 0\).',
                'max_marks': 2,
                'marking_scheme': (
                    r'M1: \(\frac{30}{x + 2} - 4 = 2x \Rightarrow 30 - 4(x + 2) = 2x(x + 2)\) | '
                    r'A1: \(22 - 4x = 2x^{2} + 4x \Rightarrow 2x^{2} + 8x - 22 = 0 \Rightarrow x^{2} + 4x - 11 = 0\) shown cleanly'
                ),
            },
            {
                'id': 'q2cii',
                'type': 'structured',
                'label': r'(c)(ii) Solve \(x^{2} + 4x - 11 = 0\), giving both answers correct to \(2\) decimal places, and state which solution satisfies \(fg(x) = 2x\) for the given domain of \(g\).',
                'max_marks': 4,
                'marking_scheme': (
                    r'M1: Substitute into quadratic formula: \(x = \frac{-4 \pm \sqrt{4^{2} - 4(1)(-11)}}{2(1)} = \frac{-4 \pm \sqrt{60}}{2}\) | '
                    r'A1: \(x = 1.87\) (from \(1.87298...\)) | '
                    r'A1: \(x = -5.87\) (from \(-5.87298...\)) | '
                    r'B1: Only \(x = 1.87\) is valid since domain of \(g\) requires \(x > -2\) (loại \(-5.87\) vì vi phạm tập xác định)'
                ),
            },
        ],
    },
    {
        'question_number': '3',
        'stem': r'A solid toy is formed by joining a solid hemisphere of radius \(5\text{ cm}\) to the flat circular base of a solid right circular cone of base radius \(5\text{ cm}\) and vertical height \(12\text{ cm}\).',
        'sub_questions': [
            {
                'id': 'q3a',
                'type': 'structured',
                'label': r'(a) Calculate the total volume of the toy, giving your answer correct to \(3\) significant figures.',
                'max_marks': 4,
                'marking_scheme': (
                    r'M1: \(V_{\text{cone}} = \frac{1}{3}\pi (5^{2})(12) = 100\pi\) | '
                    r'M1: \(V_{\text{hemi}} = \frac{2}{3}\pi (5^{3}) = \frac{250}{3}\pi\) (thể tích bán cầu bằng nửa hình cầu) | '
                    r'M1: Total volume \(= \frac{550}{3}\pi = 575.9586...\) | '
                    r'A1: \(576\text{ cm}^{3}\)'
                ),
            },
            {
                'id': 'q3b',
                'type': 'structured',
                'label': r'(b) Calculate the total surface area of the toy, giving your answer correct to \(3\) significant figures.',
                'max_marks': 3,
                'marking_scheme': (
                    r'M1: Slant height of cone \(l = \sqrt{5^{2} + 12^{2}} = 13\text{ cm}\) | '
                    r'M1: \(\text{TSA} = \pi r l + 2\pi r^{2} = \pi(5)(13) + 2\pi(5^{2}) = 115\pi = 361.283...\) (không tính mặt tròn tiếp giáp bên trong) | '
                    r'A1: \(361\text{ cm}^{2}\)'
                ),
            },
            {
                'id': 'q3c',
                'type': 'structured',
                'label': r'(c) The toy has a mass of \(480\text{ g}\). A mathematically similar larger model is made of the same material and has cone vertical height \(18\text{ cm}\). Calculate the mass of the larger model in kilograms.',
                'max_marks': 3,
                'marking_scheme': (
                    r'M1: Linear scale factor \(k = \frac{18}{12} = 1.5\) | '
                    r'M1: Mass scales by \(k^{3}\): \(480 \times 1.5^{3} = 1620\text{ g}\) (khối lượng tỉ lệ với lập phương tỉ số đồng dạng) | '
                    r'A1: \(1.62\text{ kg}\)'
                ),
            },
        ],
    },
    {
        'question_number': '4',
        'stem': r'Three ports \(A, B\) and \(C\) lie on a calm sea. Port \(B\) is \(42\text{ km}\) from port \(A\) on a bearing of \(065^{\circ}\). Port \(C\) is \(58\text{ km}\) from port \(B\) on a bearing of \(140^{\circ}\).',
        'sub_questions': [
            {
                'id': 'q4a',
                'type': 'short_answer',
                'label': r'(a) Show that \(\angle ABC = 105^{\circ}\).',
                'max_marks': 1,
                'marking_scheme': (
                    r'B1: Bearing of \(A\) from \(B\) is \(065^{\circ} + 180^{\circ} = 245^{\circ}\), so \(\angle ABC = 245^{\circ} - 140^{\circ} = 105^{\circ}\) (hoặc dùng góc trong cùng phía \(115^{\circ} + 140^{\circ} = 255^{\circ}\), \(360^{\circ} - 255^{\circ} = 105^{\circ}\))'
                ),
            },
            {
                'id': 'q4b',
                'type': 'structured',
                'label': r'(b) Calculate the straight-line distance \(AC\), giving your answer correct to \(3\) significant figures.',
                'max_marks': 3,
                'marking_scheme': (
                    r'M1: Cosine Rule: \(AC^{2} = 42^{2} + 58^{2} - 2(42)(58)\cos 105^{\circ}\) | '
                    r'M1: \(AC^{2} = 5128 - (-1260.966...) = 6388.966...\) | '
                    r'A1: \(AC = 79.931... \approx 79.9\text{ km}\)'
                ),
            },
            {
                'id': 'q4c',
                'type': 'structured',
                'label': r'(c) Calculate the bearing of port \(C\) from port \(A\), giving your answer correct to \(1\) decimal place.',
                'max_marks': 4,
                'marking_scheme': (
                    r'M1: Sine Rule: \(\frac{\sin \angle BAC}{58} = \frac{\sin 105^{\circ}}{79.931...}\) | '
                    r'M1: \(\sin \angle BAC = 0.70090... \Rightarrow \angle BAC = 44.499...^{\circ}\) | '
                    r'M1: Bearing of \(C\) from \(A\) \(= 065^{\circ} + 44.499...^{\circ}\) (cộng thêm góc phương vị ban đầu \(065^{\circ}\)) | '
                    r'A1: \(109.5^{\circ}\)'
                ),
            },
            {
                'id': 'q4d',
                'type': 'structured',
                'label': r'(d) Calculate the shortest distance from port \(B\) to the straight shipping lane \(AC\), giving your answer correct to \(3\) significant figures.',
                'max_marks': 3,
                'marking_scheme': (
                    r'M1: Area of \(\triangle ABC = \frac{1}{2}(42)(58)\sin 105^{\circ} = 1176.497...\text{ km}^{2}\) | '
                    r'M1: \(\frac{1}{2}(79.931...) d = 1176.497... \Rightarrow d = \frac{2 \times 1176.497...}{79.931...}\) (hoặc \(d = 42\sin 44.50^{\circ}\)) | '
                    r'A1: \(29.4\text{ km}\) (from \(29.4378...\))'
                ),
            },
        ],
    },
    {
        'question_number': '5',
        'stem': r'The waiting times, \(t\) minutes, of \(80\) patients at a clinic are grouped as follows: \(0 < t \leq 10\) (frequency \(8\)); \(10 < t \leq 20\) (frequency \(24\)); \(20 < t \leq 35\) (frequency \(30\)); \(35 < t \leq 60\) (frequency \(18\)).',
        'sub_questions': [
            {
                'id': 'q5a',
                'type': 'structured',
                'label': r'(a) Calculate an estimate of the mean waiting time.',
                'max_marks': 4,
                'marking_scheme': (
                    r'B1: Midpoints \(5, 15, 27.5, 47.5\) (trung điểm các khoảng) | '
                    r'M1: \(\sum fx = 8(5) + 24(15) + 30(27.5) + 18(47.5) = 40 + 360 + 825 + 855 = 2080\) | '
                    r'M1: Divide by total frequency \(80\): \(\frac{2080}{80}\) | '
                    r'A1: \(26\text{ minutes}\)'
                ),
            },
            {
                'id': 'q5b',
                'type': 'structured',
                'label': r'(b) A histogram is drawn to represent these data. The bar for \(10 < t \leq 20\) has height \(4.8\text{ cm}\). Calculate the heights of the bars for \(20 < t \leq 35\) and \(35 < t \leq 60\).',
                'max_marks': 3,
                'marking_scheme': (
                    r'M1: Frequency densities: \(\frac{24}{10} = 2.4\), \(\frac{30}{15} = 2.0\), \(\frac{18}{25} = 0.72\); scale factor \(= \frac{4.8}{2.4} = 2\text{ cm}\) per unit FD (mật độ tần số \(=\) tần số / độ rộng lớp) | '
                    r'A1: Height for \(20 < t \leq 35\) is \(2.0 \times 2 = 4.0\text{ cm}\) | '
                    r'A1: Height for \(35 < t \leq 60\) is \(0.72 \times 2 = 1.44\text{ cm}\)'
                ),
            },
            {
                'id': 'q5c',
                'type': 'structured',
                'label': r'(c) Using cumulative frequencies and linear interpolation, estimate the median waiting time and the interquartile range (IQR).',
                'max_marks': 3,
                'marking_scheme': (
                    r'B1: Cumulative frequencies \(8, 32, 62, 80\); median (\(40\)th value) \(= 20 + \frac{40 - 32}{30}\times 15 = 24\text{ minutes}\) | '
                    r'M1: \(Q_{1}\) (\(20\)th value) \(= 10 + \frac{20 - 8}{24}\times 10 = 15\text{ min}\); \(Q_{3}\) (\(60\)th value) \(= 20 + \frac{60 - 32}{30}\times 15 = 34\text{ min}\) | '
                    r'A1: \(\text{IQR} = 34 - 15 = 19\text{ minutes}\)'
                ),
            },
        ],
    },
    {
        'question_number': '6',
        'stem': r'\(VABCD\) is a right pyramid with a horizontal rectangular base \(ABCD\), where \(AB = 16\text{ cm}\) and \(BC = 12\text{ cm}\). The vertex \(V\) is vertically above the centre \(M\) of the base, and \(VM = 15\text{ cm}\).',
        'sub_questions': [
            {
                'id': 'q6a',
                'type': 'short_answer',
                'label': r'(a) Calculate the length of the base diagonal \(AC\).',
                'max_marks': 2,
                'marking_scheme': (
                    r'M1: \(AC = \sqrt{16^{2} + 12^{2}} = \sqrt{400}\) | '
                    r'A1: \(20\text{ cm}\)'
                ),
            },
            {
                'id': 'q6b',
                'type': 'short_answer',
                'label': r'(b) Calculate the length of the sloping edge \(VA\), correct to \(3\) significant figures.',
                'max_marks': 2,
                'marking_scheme': (
                    r'M1: \(AM = \frac{1}{2}AC = 10\text{ cm}\); \(VA = \sqrt{10^{2} + 15^{2}} = \sqrt{325}\) | '
                    r'A1: \(18.0\text{ cm}\) (from \(18.0277...\))'
                ),
            },
            {
                'id': 'q6c',
                'type': 'short_answer',
                'label': r'(c) Calculate the angle between the sloping edge \(VA\) and the base \(ABCD\), correct to \(1\) decimal place.',
                'max_marks': 2,
                'marking_scheme': (
                    r'M1: \(\tan(\angle VAM) = \frac{VM}{AM} = \frac{15}{10} = 1.5\) (góc giữa đường thẳng và mặt phẳng đáy) | '
                    r'A1: \(56.3^{\circ}\) (from \(56.3099...\))'
                ),
            },
            {
                'id': 'q6d',
                'type': 'structured',
                'label': r'(d) Calculate the angle between the triangular face \(VBC\) and the base \(ABCD\), correct to \(1\) decimal place.',
                'max_marks': 3,
                'marking_scheme': (
                    r'M1: Let \(N\) be midpoint of \(BC\); identify angle \(\angle VNM\) with \(MN = \frac{1}{2}AB = 8\text{ cm}\) (xác định đúng góc nhị diện) | '
                    r'M1: \(\tan(\angle VNM) = \frac{15}{8} = 1.875\) | '
                    r'A1: \(61.9^{\circ}\) (from \(61.9275...\))'
                ),
            },
        ],
    },
    {
        'question_number': '7',
        'stem': r'A curve has equation \(y = x^{3} - 6x^{2} + 9x + 2\).',
        'sub_questions': [
            {
                'id': 'q7a',
                'type': 'short_answer',
                'label': r'(a) Find \(\frac{dy}{dx}\) and \(\frac{d^2 y}{dx^2}\).',
                'max_marks': 2,
                'marking_scheme': (
                    r'B1: \(\frac{dy}{dx} = 3x^{2} - 12x + 9\) | '
                    r'B1: \(\frac{d^{2}y}{dx^{2}} = 6x - 12\)'
                ),
            },
            {
                'id': 'q7b',
                'type': 'structured',
                'label': r'(b) Find the coordinates of the two stationary points on the curve and use \(\frac{d^2 y}{dx^2}\) to classify each point.',
                'max_marks': 5,
                'marking_scheme': (
                    r'M1: \(3x^{2} - 12x + 9 = 0 \Rightarrow 3(x - 1)(x - 3) = 0 \Rightarrow x = 1, 3\) | '
                    r'A1: Coordinates \((1, 6)\) | '
                    r'A1: Coordinates \((3, 2)\) | '
                    r'M1: Evaluate \(\frac{d^{2}y}{dx^{2}}\) at both points: at \(x = 1, -6 < 0\); at \(x = 3, +6 > 0\) | '
                    r'A1: \((1, 6)\) is a local maximum and \((3, 2)\) is a local minimum'
                ),
            },
            {
                'id': 'q7c',
                'type': 'structured',
                'label': r'(c) Find the equation of the tangent to the curve at the point where \(x = 4\), and find the coordinates of the point where this tangent crosses the \(x\)-axis.',
                'max_marks': 3,
                'marking_scheme': (
                    r'M1: At \(x = 4\): \(y = 64 - 96 + 36 + 2 = 6\) and \(m = 3(16) - 12(4) + 9 = 9\) | '
                    r'A1: Tangent equation \(y - 6 = 9(x - 4) \Rightarrow y = 9x - 30\) | '
                    r'A1: Crosses \(x\)-axis when \(y = 0 \Rightarrow \left(\frac{10}{3}, 0\right)\) (or \((3.33, 0)\))'
                ),
            },
        ],
    },
    {
        'question_number': '8',
        'stem': r'A box contains \(6\) green balls, \(5\) yellow balls and \(4\) white balls (\(15\) balls in total).',
        'sub_questions': [
            {
                'id': 'q8a',
                'type': 'short_answer',
                'label': r'(a) Two balls are picked at random without replacement. Calculate the exact probability that both balls are yellow.',
                'max_marks': 2,
                'marking_scheme': (
                    r'M1: \(\frac{5}{15} \times \frac{4}{14}\) | '
                    r'A1: \(\frac{2}{21}\)'
                ),
            },
            {
                'id': 'q8b',
                'type': 'structured',
                'label': r'(b) Two balls are picked at random without replacement. Calculate the exact probability that both balls are the same colour.',
                'max_marks': 3,
                'marking_scheme': (
                    r'M1: \(P(GG) = \frac{6}{15}\times\frac{5}{14} = \frac{30}{210}\) and \(P(WW) = \frac{4}{15}\times\frac{3}{14} = \frac{12}{210}\) | '
                    r'M1: Sum all three cases: \(\frac{30 + 20 + 12}{210} = \frac{62}{210}\) | '
                    r'A1: \(\frac{31}{105}\)'
                ),
            },
            {
                'id': 'q8c',
                'type': 'short_answer',
                'label': r'(c) Given that the two balls chosen are the same colour, find the exact probability that both balls are green.',
                'max_marks': 2,
                'marking_scheme': (
                    r'M1: \(P(GG \mid \text{same colour}) = \frac{30/210}{62/210} = \frac{30}{62}\) (xác suất có điều kiện) | '
                    r'A1: \(\frac{15}{31}\)'
                ),
            },
            {
                'id': 'q8d',
                'type': 'structured',
                'label': r'(d) Instead, balls are drawn one by one without replacement until a white ball is obtained. Find the exact probability that the first white ball is drawn on the \(3\)rd draw.',
                'max_marks': 3,
                'marking_scheme': (
                    r'M1: Need non-white, then non-white, then white: \(\frac{11}{15} \times \frac{10}{14} \times \frac{4}{13}\) (có \(11\) bi không phải màu trắng) | '
                    r'M1: Multiply to \(\frac{440}{2730}\) | '
                    r'A1: \(\frac{44}{273}\)'
                ),
            },
        ],
    },
    {
        'question_number': '9',
        'stem': r'In the coordinate plane, points \(A(1, 2)\), \(B(7, 5)\) and \(C(5, 9)\) are three vertices of a quadrilateral.',
        'sub_questions': [
            {
                'id': 'q9a',
                'type': 'structured',
                'label': r'(a) Write down the vectors \(\vec{AB}\) and \(\vec{BC}\) in component form and show that \(AB\) is perpendicular to \(BC\).',
                'max_marks': 3,
                'marking_scheme': (
                    r'B1: \(\vec{AB} = (6, 3)\) and \(\vec{BC} = (-2, 4)\) | '
                    r'M1: Gradients \(m_{AB} = \frac{3}{6} = \frac{1}{2}\) and \(m_{BC} = \frac{4}{-2} = -2\) (or Pythagoras \(AB^{2} + BC^{2} = 45 + 20 = 65 = AC^{2}\)) | '
                    r'A1: \(m_{AB} \times m_{BC} = \frac{1}{2} \times (-2) = -1\), hence \(AB \perp BC\)'
                ),
            },
            {
                'id': 'q9b',
                'type': 'structured',
                'label': r'(b) Point \(D\) is positioned such that \(ABCD\) is a rectangle. Find the coordinates of \(D\) and calculate the exact area of rectangle \(ABCD\).',
                'max_marks': 3,
                'marking_scheme': (
                    r'B1: \(\vec{OD} = \vec{OA} + \vec{BC} = (1, 2) + (-2, 4) = (-1, 6) \Rightarrow D(-1, 6)\) | '
                    r'M1: \(AB = \sqrt{6^{2} + 3^{2}} = \sqrt{45} = 3\sqrt{5}\) and \(BC = \sqrt{(-2)^{2} + 4^{2}} = \sqrt{20} = 2\sqrt{5}\) | '
                    r'A1: Area \(= 3\sqrt{5} \times 2\sqrt{5} = 30\) square units'
                ),
            },
            {
                'id': 'q9c',
                'type': 'structured',
                'label': r'(c) Find the coordinates of the centre \(E\) of rectangle \(ABCD\), and find the equation of the diagonal \(AC\) in the form \(ay = bx + c\) where \(a, b, c\) are integers.',
                'max_marks': 4,
                'marking_scheme': (
                    r'B1: Centre \(E = \text{midpoint of } AC = \left(\frac{1 + 5}{2}, \frac{2 + 9}{2}\right) = (3, 5.5)\) | '
                    r'M1: Gradient of \(AC = \frac{9 - 2}{5 - 1} = \frac{7}{4}\) | '
                    r'M1: \(y - 2 = \frac{7}{4}(x - 1)\) | '
                    r'A1: \(4y = 7x + 1\)'
                ),
            },
        ],
    },
    {
        'question_number': '10',
        'stem': '',
        'sub_questions': [
            {
                'id': 'q10ai',
                'type': 'structured',
                'label': r'(a)(i) Find an expression for the \(n\)th term of the sequence \(4, 11, 22, 37, ...\).',
                'max_marks': 3,
                'marking_scheme': (
                    r'M1: First differences \(7, 11, 15\); second difference \(4 \Rightarrow 2n^{2}\) | '
                    r'M1: Subtract \(2n^{2}\) (\(2, 8, 18, 32\)) to get linear remainder \(2, 3, 4, 5 = n + 1\) | '
                    r'A1: \(2n^{2} + n + 1\)'
                ),
            },
            {
                'id': 'q10aii',
                'type': 'short_answer',
                'label': r'(a)(ii) Calculate the \(20\)th term of this sequence.',
                'max_marks': 1,
                'marking_scheme': (
                    r'B1: \(2(20^{2}) + 20 + 1 = 821\)'
                ),
            },
            {
                'id': 'q10bi',
                'type': 'structured',
                'label': r"(b)(i) A car travels a distance \(d = 250\text{ km}\), measured correct to the nearest \(5\text{ km}\), in a time \(t = 4.0\text{ hours}\), measured correct to \(1\) decimal place. Calculate the upper bound and lower bound of the car's average speed, correct to \(3\) significant figures.",
                'max_marks': 4,
                'marking_scheme': (
                    r'B1: Bounds \(247.5 \leq d < 252.5\) and \(3.95 \leq t < 4.05\) | '
                    r'M1: \(v_{\max} = \frac{252.5}{3.95} = 63.924...\) and \(v_{\min} = \frac{247.5}{4.05} = 61.111...\) | '
                    r'A1: Upper bound \(= 63.9\text{ km/h}\) | '
                    r'A1: Lower bound \(= 61.1\text{ km/h}\)'
                ),
            },
            {
                'id': 'q10bii',
                'type': 'short_answer',
                'label': r'(b)(ii) State the average speed of the car to an appropriate degree of accuracy, giving a reason.',
                'max_marks': 1,
                'marking_scheme': (
                    r'B1: \(60\text{ km/h}\), because both the upper bound (\(63.9\)) and lower bound (\(61.1\)) round to \(60\) correct to \(1\) significant figure (cả hai cận đều làm tròn về \(60\) ở 1 chữ số có nghĩa)'
                ),
            },
        ],
    },
]

# =============================================================================
# PAPER 4: 0580/42 — Paper 4 (Extended — Calculator) Full Mock #2 (100 marks)
# =============================================================================
PAPER_0580_P4_2_QUESTIONS = [
    {
        'question_number': '1',
        'stem': '',
        'sub_questions': [
            {
                'id': 'q1a',
                'type': 'structured',
                'label': r'(a) A delivery van is bought for £\(28000\). Its value depreciates by \(14\)% each year. Calculate the value of the van after \(4\) years, correct to the nearest pound.',
                'max_marks': 3,
                'marking_scheme': (
                    r'M1: Depreciation multiplier \(1 - 0.14 = 0.86\) (khấu hao \(14\)%) | '
                    r'M1: \(28000 \times 0.86^{4} = 15316.228...\) | '
                    r'A1: £\(15316\)'
                ),
            },
            {
                'id': 'q1b',
                'type': 'structured',
                'label': r'(b) A retailer buys \(120\) watches for a total cost of £\(3000\). He sells \(95\) watches at £\(36\) each and the remaining \(25\) watches at £\(22\) each. Calculate his overall percentage profit, correct to \(1\) decimal place.',
                'max_marks': 3,
                'marking_scheme': (
                    r'M1: Total revenue \(= 95 \times 36 + 25 \times 22 = 3420 + 550 = 3970\) | '
                    r'M1: Profit \(= 970\); \(\text{percentage profit} = \frac{970}{3000} \times 100 = 32.333...\)% | '
                    r'A1: \(32.3\)%'
                ),
            },
            {
                'id': 'q1c',
                'type': 'short_answer',
                'label': r'(c) Find the smallest integer number of complete years \(n\) for which an investment of £\(5000\) at \(4.2\)% per year compound interest first exceeds £\(7000\).',
                'max_marks': 2,
                'marking_scheme': (
                    r'M1: Trial with \(5000 \times 1.042^{n}\): \(n = 8 \Rightarrow 6949.47 < 7000\), \(n = 9 \Rightarrow 7241.35 > 7000\) (hoặc dùng logarit \(n > \frac{\ln 1.4}{\ln 1.042} = 8.17...\)) | '
                    r'A1: \(n = 9\)'
                ),
            },
            {
                'id': 'q1d',
                'type': 'short_answer',
                'label': r'(d) The mass of Earth is \(5.97 \times 10^{24}\text{ kg}\) and the mass of Mars is \(6.42 \times 10^{23}\text{ kg}\). Calculate how many times heavier Earth is than Mars, correct to \(3\) significant figures.',
                'max_marks': 2,
                'marking_scheme': (
                    r'M1: \(\frac{5.97 \times 10^{24}}{6.42 \times 10^{23}} = 9.29906...\) | '
                    r'A1: \(9.30\) (phải giữ chữ số \(0\) cuối để đủ \(3\) s.f.)'
                ),
            },
        ],
    },
    {
        'question_number': '2',
        'stem': '',
        'sub_questions': [
            {
                'id': 'q2ai',
                'type': 'structured',
                'label': r'(a)(i) A rectangular garden has length \((2x + 5)\text{ m}\) and width \((x + 1)\text{ m}\). A square pond of side length \(x\text{ m}\) is built inside the garden. The remaining grass area is \(47\text{ m}^{2}\). Show that \(x^{2} + 7x - 42 = 0\).',
                'max_marks': 3,
                'marking_scheme': (
                    r'M1: Form area equation \((2x + 5)(x + 1) - x^{2} = 47\) | '
                    r'M1: Expand correctly: \(2x^{2} + 7x + 5 - x^{2} = 47\) | '
                    r'A1: Simplify cleanly to \(x^{2} + 7x - 42 = 0\)'
                ),
            },
            {
                'id': 'q2aii',
                'type': 'structured',
                'label': r'(a)(ii) Solve \(x^{2} + 7x - 42 = 0\), giving both roots correct to \(2\) decimal places, and hence calculate the perimeter of the garden correct to \(3\) significant figures.',
                'max_marks': 4,
                'marking_scheme': (
                    r'M1: Quadratic formula \(x = \frac{-7 \pm \sqrt{7^{2} - 4(1)(-42)}}{2} = \frac{-7 \pm \sqrt{217}}{2}\) | '
                    r'A1: \(x = 3.87\) (from \(3.86546...\)) and \(x = -10.87\) (from \(-10.86546...\)) | '
                    r'M1: Perimeter \(= 2((2x + 5) + (x + 1)) = 6x + 12\) with positive root \(x = 3.86546...\) | '
                    r'A1: \(35.2\text{ m}\) (from \(35.1927...\))'
                ),
            },
            {
                'id': 'q2bi',
                'type': 'short_answer',
                'label': r'(b)(i) The function \(h(x) = 3x^{\frac{1}{2}} - 2\) is defined for \(1 \leq x \leq 25\). Find the range of \(h(x)\).',
                'max_marks': 2,
                'marking_scheme': (
                    r'M1: Evaluate endpoints (increasing function): \(h(1) = 3(1) - 2 = 1\) and \(h(25) = 3(5) - 2 = 13\) | '
                    r'A1: \(1 \leq h(x) \leq 13\)'
                ),
            },
            {
                'id': 'q2bii',
                'type': 'short_answer',
                'label': r'(b)(ii) Find \(h^{-1}(x)\) and state its domain.',
                'max_marks': 2,
                'marking_scheme': (
                    r'B1: \(h^{-1}(x) = \left(\frac{x + 2}{3}\right)^{2}\) | '
                    r'B1: Domain of \(h^{-1}\) is \(1 \leq x \leq 13\)'
                ),
            },
        ],
    },
    {
        'question_number': '3',
        'stem': r'A bucket is in the shape of a frustum of a right circular cone. It is formed by removing a smaller cone of base radius \(10\text{ cm}\) and vertical height \(16\text{ cm}\) from a larger cone of base radius \(15\text{ cm}\).',
        'sub_questions': [
            {
                'id': 'q3a',
                'type': 'short_answer',
                'label': r'(a) Show that the vertical height of the larger cone is \(24\text{ cm}\), and state the vertical height of the bucket.',
                'max_marks': 2,
                'marking_scheme': (
                    r'M1: By similar cones, \(\frac{H}{16} = \frac{15}{10} \Rightarrow H = 16 \times 1.5 = 24\text{ cm}\) (hai hình nón đồng dạng) | '
                    r'A1: Height of bucket \(= 24 - 16 = 8\text{ cm}\)'
                ),
            },
            {
                'id': 'q3b',
                'type': 'structured',
                'label': r'(b) Calculate the volume of the bucket, giving your answer correct to \(3\) significant figures.',
                'max_marks': 3,
                'marking_scheme': (
                    r'M1: \(V_{\text{large}} = \frac{1}{3}\pi (15^{2})(24) = 1800\pi\) and \(V_{\text{small}} = \frac{1}{3}\pi (10^{2})(16) = \frac{1600}{3}\pi\) | '
                    r'M1: \(V_{\text{frustum}} = 1800\pi - \frac{1600}{3}\pi = \frac{3800}{3}\pi = 3979.35...\) | '
                    r'A1: \(3980\text{ cm}^{3}\)'
                ),
            },
            {
                'id': 'q3c',
                'type': 'structured',
                'label': r'(c) Calculate the curved surface area of the outside of the bucket, correct to \(3\) significant figures.',
                'max_marks': 3,
                'marking_scheme': (
                    r'M1: Slant heights \(L = \sqrt{15^{2} + 24^{2}} = \sqrt{801} \approx 28.302\text{ cm}\) and \(l = \sqrt{10^{2} + 16^{2}} = \sqrt{356} \approx 18.868\text{ cm}\) | '
                    r'M1: \(\text{CSA} = \pi(15)L - \pi(10)l = 740.943...\) | '
                    r'A1: \(741\text{ cm}^{2}\)'
                ),
            },
            {
                'id': 'q3d',
                'type': 'short_answer',
                'label': r'(d) The bucket is filled completely with water, which is then poured into an empty cylindrical tank of radius \(16\text{ cm}\). Calculate the depth of water in the tank, correct to \(3\) significant figures.',
                'max_marks': 2,
                'marking_scheme': (
                    r'M1: \(\pi (16^{2}) d = \frac{3800}{3}\pi \Rightarrow d = \frac{3800}{768} = 4.9479...\) | '
                    r'A1: \(4.95\text{ cm}\)'
                ),
            },
        ],
    },
    {
        'question_number': '4',
        'stem': r'In quadrilateral \(ABCD\), \(AB = 11.4\text{ cm}\), \(BC = 9.2\text{ cm}\), \(CD = 13.5\text{ cm}\), \(\angle ABC = 112^{\circ}\) and \(\angle ACD = 38^{\circ}\), with \(B\) and \(D\) on opposite sides of the diagonal \(AC\).',
        'sub_questions': [
            {
                'id': 'q4a',
                'type': 'structured',
                'label': r'(a) Calculate the length of diagonal \(AC\), correct to \(3\) significant figures.',
                'max_marks': 3,
                'marking_scheme': (
                    r'M1: Cosine Rule in \(\triangle ABC\): \(AC^{2} = 11.4^{2} + 9.2^{2} - 2(11.4)(9.2)\cos 112^{\circ}\) | '
                    r'M1: \(AC^{2} = 214.6 + 78.5775... = 293.1775...\) | '
                    r'A1: \(AC = 17.1224... \approx 17.1\text{ cm}\)'
                ),
            },
            {
                'id': 'q4b',
                'type': 'structured',
                'label': r'(b) Calculate \(\angle BAC\), correct to \(1\) decimal place.',
                'max_marks': 3,
                'marking_scheme': (
                    r'M1: Sine Rule: \(\frac{\sin \angle BAC}{9.2} = \frac{\sin 112^{\circ}}{17.1224...}\) | '
                    r'M1: \(\sin \angle BAC = 0.49818...\) | '
                    r'A1: \(29.9^{\circ}\) (from \(29.879...\))'
                ),
            },
            {
                'id': 'q4c',
                'type': 'structured',
                'label': r'(c) Calculate the total area of quadrilateral \(ABCD\), correct to \(3\) significant figures.',
                'max_marks': 4,
                'marking_scheme': (
                    r'M1: Area \(\triangle ABC = \frac{1}{2}(11.4)(9.2)\sin 112^{\circ} = 48.6215...\) | '
                    r'M1: Area \(\triangle ACD = \frac{1}{2}(17.1224...)(13.5)\sin 38^{\circ} = 71.1559...\) | '
                    r'M1: Total area \(= 48.6215... + 71.1559... = 119.777...\) | '
                    r'A1: \(120\text{ cm}^{2}\)'
                ),
            },
        ],
    },
    {
        'question_number': '5',
        'stem': r'\(ABCDEFGH\) is a rectangular cuboid with horizontal rectangular base \(ABCD\) and vertical edges \(AE, BF, CG, DH\). Given \(AB = 14\text{ cm}\), \(BC = 9\text{ cm}\) and \(CG = 6\text{ cm}\):',
        'sub_questions': [
            {
                'id': 'q5a',
                'type': 'structured',
                'label': r'(a) Calculate the length of the space diagonal \(AG\), correct to \(3\) significant figures.',
                'max_marks': 3,
                'marking_scheme': (
                    r'M1: Base diagonal \(AC^{2} = 14^{2} + 9^{2} = 277\) | '
                    r'M1: \(AG = \sqrt{14^{2} + 9^{2} + 6^{2}} = \sqrt{313} = 17.6918...\) (Pythagoras 3D) | '
                    r'A1: \(17.7\text{ cm}\)'
                ),
            },
            {
                'id': 'q5b',
                'type': 'short_answer',
                'label': r'(b) Calculate the angle that \(AG\) makes with the horizontal base \(ABCD\), correct to \(1\) decimal place.',
                'max_marks': 2,
                'marking_scheme': (
                    r'M1: \(\sin(\angle GAC) = \frac{6}{\sqrt{313}}\) (or \(\tan(\angle GAC) = \frac{6}{\sqrt{277}}\)) | '
                    r'A1: \(19.8^{\circ}\) (from \(19.824...\))'
                ),
            },
            {
                'id': 'q5c',
                'type': 'structured',
                'label': r'(c) Point \(P\) is the midpoint of the top edge \(EF\). Calculate \(\angle APB\), correct to \(1\) decimal place.',
                'max_marks': 3,
                'marking_scheme': (
                    r'M1: Let \(Q\) be midpoint of \(AB\); \(PQ = 6\text{ cm}\) and \(AQ = 7\text{ cm}\) (or \(AP = BP = \sqrt{6^{2} + 7^{2}} = \sqrt{85}\)) | '
                    r'M1: \(\tan(\angle APQ) = \frac{7}{6} \Rightarrow \angle APQ = 49.3987^{\circ}\) and \(\angle APB = 2 \times \angle APQ\) (or Cosine Rule \(\cos \angle APB = \frac{85 + 85 - 196}{170}\)) | '
                    r'A1: \(98.8^{\circ}\) (from \(98.797...\))'
                ),
            },
            {
                'id': 'q5d',
                'type': 'short_answer',
                'label': r'(d) Calculate the angle between the diagonal plane \(ABGH\) and the horizontal base \(ABCD\), correct to \(1\) decimal place.',
                'max_marks': 2,
                'marking_scheme': (
                    r'M1: Identify \(\angle GBC\) (since \(BC \perp AB\) and \(BG \perp AB\)) with \(\tan(\angle GBC) = \frac{6}{9} = \frac{2}{3}\) | '
                    r'A1: \(33.7^{\circ}\) (from \(33.690...\))'
                ),
            },
        ],
    },
    {
        'question_number': '6',
        'stem': r'The masses, \(m\) grams, of \(120\) apples picked from an orchard are grouped as follows: \(100 < m \leq 120\) (frequency \(18\)); \(120 < m \leq 140\) (frequency \(42\)); \(140 < m \leq 170\) (frequency \(45\)); \(170 < m \leq 200\) (frequency \(15\)).',
        'sub_questions': [
            {
                'id': 'q6a',
                'type': 'structured',
                'label': r'(a) Calculate an estimate of the mean mass of an apple, giving your exact decimal answer.',
                'max_marks': 4,
                'marking_scheme': (
                    r'B1: Class midpoints \(110, 130, 155, 185\) | '
                    r'M1: \(\sum fm = 18(110) + 42(130) + 45(155) + 15(185) = 1980 + 5460 + 6975 + 2775 = 17190\) | '
                    r'M1: Divide by \(120\): \(\frac{17190}{120}\) | '
                    r'A1: \(143.25\text{ g}\)'
                ),
            },
            {
                'id': 'q6b',
                'type': 'short_answer',
                'label': r'(b) Calculate the frequency density for each of the four class intervals.',
                'max_marks': 2,
                'marking_scheme': (
                    r'M1: Divide each frequency by its class width (\(20, 20, 30, 30\)) | '
                    r'A1: \(0.9, 2.1, 1.5, 0.5\)'
                ),
            },
            {
                'id': 'q6ci',
                'type': 'short_answer',
                'label': r'(c)(i) Using cumulative frequencies, state the median mass.',
                'max_marks': 1,
                'marking_scheme': (
                    r'B1: Cumulative frequencies \(18, 60, 105, 120\); the \(60\)th value is at the exact upper boundary \(140\text{ g}\)'
                ),
            },
            {
                'id': 'q6cii',
                'type': 'structured',
                'label': r'(c)(ii) Using cumulative frequencies and linear interpolation, estimate the \(80\)th percentile mass.',
                'max_marks': 3,
                'marking_scheme': (
                    r'M1: \(80\%\) of \(120 = 96\)th value, which lies in \(140 < m \leq 170\) (bách phân vị thứ \(80\) ứng với vị trí \(96\)) | '
                    r'M1: \(P_{80} = 140 + \frac{96 - 60}{45} \times 30 = 140 + 24\) | '
                    r'A1: \(164\text{ g}\)'
                ),
            },
        ],
    },
    {
        'question_number': '7',
        'stem': r'The curve \(y = x^{3} - 3x^{2} - 24x + 10\) is considered for \(-4 \leq x \leq 6\).',
        'sub_questions': [
            {
                'id': 'q7a',
                'type': 'short_answer',
                'label': r'(a) Find \(\frac{dy}{dx}\).',
                'max_marks': 2,
                'marking_scheme': (
                    r'M1: At least two terms differentiated correctly | '
                    r'A1: \(\frac{dy}{dx} = 3x^{2} - 6x - 24\)'
                ),
            },
            {
                'id': 'q7b',
                'type': 'structured',
                'label': r'(b) Find the coordinates of the two stationary points on the curve and determine whether each is a local maximum or a local minimum.',
                'max_marks': 5,
                'marking_scheme': (
                    r'M1: \(3(x^{2} - 2x - 8) = 0 \Rightarrow (x - 4)(x + 2) = 0 \Rightarrow x = -2, 4\) | '
                    r'A1: Coordinates \((-2, 38)\) | '
                    r'A1: Coordinates \((4, -70)\) | '
                    r'M1: \(\frac{d^{2}y}{dx^{2}} = 6x - 6\): at \(x = -2, -18 < 0\); at \(x = 4, +18 > 0\) | '
                    r'A1: \((-2, 38)\) is a local maximum and \((4, -70)\) is a local minimum'
                ),
            },
            {
                'id': 'q7c',
                'type': 'structured',
                'label': r'(c) Find the range of values of \(x\) for which the curve has a negative gradient (is strictly decreasing).',
                'max_marks': 3,
                'marking_scheme': (
                    r'M1: Set \(\frac{dy}{dx} < 0\): \(3(x + 2)(x - 4) < 0\) (hàm nghịch biến khi đạo hàm âm) | '
                    r'M1: Identify interval strictly between the two stationary \(x\)-values \(-2\) and \(4\) | '
                    r'A1: \(-2 < x < 4\)'
                ),
            },
        ],
    },
    {
        'question_number': '8',
        'stem': r'The probability that it rains on any given morning is \(0.3\). If it rains, the probability that Sam takes the bus to school is \(0.85\). If it does not rain, the probability that Sam takes the bus is \(0.4\).',
        'sub_questions': [
            {
                'id': 'q8a',
                'type': 'short_answer',
                'label': r'(a) Calculate the probability that on a randomly chosen morning, it rains and Sam takes the bus.',
                'max_marks': 2,
                'marking_scheme': (
                    r'M1: \(0.3 \times 0.85\) | '
                    r'A1: \(0.255\) (or \(\frac{51}{200}\))'
                ),
            },
            {
                'id': 'q8b',
                'type': 'structured',
                'label': r'(b) Calculate the probability that Sam takes the bus on a randomly chosen morning.',
                'max_marks': 3,
                'marking_scheme': (
                    r'M1: \(P(\text{not rain and bus}) = 0.7 \times 0.4 = 0.28\) | '
                    r'M1: Add both branches: \(0.255 + 0.28\) (quy tắc cộng xác suất toàn phần) | '
                    r'A1: \(0.535\) (or \(\frac{107}{200}\))'
                ),
            },
            {
                'id': 'q8c',
                'type': 'structured',
                'label': r'(c) Given that Sam took the bus this morning, calculate the probability that it rained. Give your answer as an exact fraction in its simplest form.',
                'max_marks': 3,
                'marking_scheme': (
                    r'M1: Conditional probability \(P(\text{rain} \mid \text{bus}) = \frac{P(\text{rain and bus})}{P(\text{bus})}\) | '
                    r'M1: \(\frac{0.255}{0.535} = \frac{255}{535}\) | '
                    r'A1: \(\frac{51}{107}\) (approx \(0.477\))'
                ),
            },
            {
                'id': 'q8d',
                'type': 'short_answer',
                'label': r'(d) Assuming the weather on consecutive mornings is independent, calculate the probability that it rains on at least one of the next \(3\) mornings.',
                'max_marks': 2,
                'marking_scheme': (
                    r'M1: \(1 - P(\text{no rain on all 3 mornings}) = 1 - 0.7^{3} = 1 - 0.343\) (dùng biến cố đối) | '
                    r'A1: \(0.657\)'
                ),
            },
        ],
    },
    {
        'question_number': '9',
        'stem': r'A circle has centre \(O\) and radius \(8\text{ cm}\). Two tangents \(PA\) and \(PB\) are drawn from an external point \(P\) to touch the circle at \(A\) and \(B\), where \(OP = 17\text{ cm}\).',
        'sub_questions': [
            {
                'id': 'q9a',
                'type': 'structured',
                'label': r'(a) State the size of \(\angle OAP\) with a geometrical reason, and calculate the exact length of \(PA\).',
                'max_marks': 3,
                'marking_scheme': (
                    r'B1: \(\angle OAP = 90^{\circ}\) because a radius is perpendicular to a tangent at the point of contact (bán kính vuông góc tiếp tuyến tại tiếp điểm) | '
                    r'M1: \(PA = \sqrt{17^{2} - 8^{2}} = \sqrt{225}\) | '
                    r'A1: \(PA = 15\text{ cm}\)'
                ),
            },
            {
                'id': 'q9b',
                'type': 'structured',
                'label': r'(b) Calculate \(\angle AOB\), giving your answer correct to \(1\) decimal place.',
                'max_marks': 3,
                'marking_scheme': (
                    r'M1: In right-angled \(\triangle OAP\), \(\cos(\angle AOP) = \frac{8}{17}\) | '
                    r'M1: \(\angle AOP = 61.9275...^{\circ}\), so \(\angle AOB = 2 \times 61.9275...^{\circ} = 123.855...^{\circ}\) | '
                    r'A1: \(123.9^{\circ}\)'
                ),
            },
            {
                'id': 'q9c',
                'type': 'structured',
                'label': r'(c) Calculate the area of the region bounded by the two tangents \(PA, PB\) and the minor arc \(AB\), correct to \(3\) significant figures.',
                'max_marks': 3,
                'marking_scheme': (
                    r'M1: Area of kite \(OAPB = 2 \times \frac{1}{2}(8)(15) = 120\text{ cm}^{2}\) | '
                    r'M1: Area of minor sector \(OAB = \frac{123.855...}{360} \times \pi \times 8^{2} = 69.175...\text{ cm}^{2}\); subtract \(120 - 69.175...\) | '
                    r'A1: \(50.8\text{ cm}^{2}\) (from \(50.8249...\))'
                ),
            },
        ],
    },
    {
        'question_number': '10',
        'stem': '',
        'sub_questions': [
            {
                'id': 'q10ai',
                'type': 'short_answer',
                'label': r'(a)(i) In parallelogram \(OABC\), \(\vec{OA} = \mathbf{a}\) and \(\vec{OC} = \mathbf{c}\). Point \(X\) lies on \(AB\) such that \(AX : XB = 1 : 2\), and \(Y\) is the midpoint of \(BC\). Express \(\vec{OX}\) and \(\vec{OY}\) in terms of \(\mathbf{a}\) and \(\mathbf{c}\).',
                'max_marks': 2,
                'marking_scheme': (
                    r'B1: \(\vec{OX} = \mathbf{a} + \frac{1}{3}\mathbf{c}\) (vì \(\vec{AB} = \mathbf{c}\)) | '
                    r'B1: \(\vec{OY} = \frac{1}{2}\mathbf{a} + \mathbf{c}\) (vì \(\vec{CB} = \mathbf{a}\))'
                ),
            },
            {
                'id': 'q10aii',
                'type': 'structured',
                'label': r'(a)(ii) The line \(OX\) extended meets \(CB\) extended at point \(Z\). Find \(\vec{OZ}\) in terms of \(\mathbf{a}\) and \(\mathbf{c}\), and hence state the ratio \(CB : BZ\).',
                'max_marks': 4,
                'marking_scheme': (
                    r'M1: Express \(\vec{OZ}\) in two ways: \(\vec{OZ} = k\vec{OX} = k\mathbf{a} + \frac{k}{3}\mathbf{c}\) and \(\vec{OZ} = \mathbf{c} + m\mathbf{a}\) (biểu diễn giao điểm theo 2 phương trình vectơ) | '
                    r'M1: Equate coefficients of \(\mathbf{c}\): \(\frac{k}{3} = 1 \Rightarrow k = 3\), and coefficients of \(\mathbf{a}\): \(m = k = 3\) | '
                    r'A1: \(\vec{OZ} = 3\mathbf{a} + \mathbf{c}\) | '
                    r'A1: \(\vec{BZ} = \vec{OZ} - \vec{OB} = 2\mathbf{a}\) and \(\vec{CB} = \mathbf{a} \Rightarrow CB : BZ = 1 : 2\)'
                ),
            },
            {
                'id': 'q10bi',
                'type': 'short_answer',
                'label': r'(b)(i) An exponential sequence has \(n\)th term \(u_{n} = 80 \times (0.75)^{n - 1}\). Calculate the exact value of \(u_{4}\).',
                'max_marks': 2,
                'marking_scheme': (
                    r'M1: \(u_{4} = 80 \times (0.75)^{3} = 80 \times \frac{27}{64}\) | '
                    r'A1: \(33.75\) (or \(\frac{135}{4}\))'
                ),
            },
            {
                'id': 'q10bii',
                'type': 'short_answer',
                'label': r'(b)(ii) Find the smallest positive integer \(n\) for which \(u_{n} < 10\).',
                'max_marks': 2,
                'marking_scheme': (
                    r'M1: Check \(u_{8} = 80(0.75)^{7} = 10.6787... > 10\) and \(u_{9} = 80(0.75)^{8} = 8.009... < 10\) (thử giá trị hoặc giải bất phương trình mũ) | '
                    r'A1: \(n = 9\)'
                ),
            },
        ],
    },
]

# =============================================================================
# EXPORTED LIST OF 4 FULL-LENGTH 100-MARK MOCK PAPERS
# =============================================================================
MOCKS_0580_2025 = [
    {
        'code': 'm0580_p2_1',
        'pdf_rel_path': 'papers/igcse-maths/0580_p2_noncalc_mock1.pdf',
        'order_index': 101,
        'paper_meta': {
            'code': '0580/21',
            'title': '🚫 0580/21 Paper 2 (Extended — Non-Calculator) Full Mock #1 [2025–2027]',
            'syllabus': '0580',
            'syllabus_name': 'Cambridge IGCSE Mathematics (0580) Extended — Paper 2 Non-Calculator',
            'course_id': COURSE_0580_ID,
            'time_limit': 120,
            'calculator_policy': 'non-calculator',
        },
        'questions': PAPER_0580_P2_1_QUESTIONS,
    },
    {
        'code': 'm0580_p2_2',
        'pdf_rel_path': 'papers/igcse-maths/0580_p2_noncalc_mock2.pdf',
        'order_index': 102,
        'paper_meta': {
            'code': '0580/22',
            'title': '🚫 0580/22 Paper 2 (Extended — Non-Calculator) Full Mock #2 [2025–2027]',
            'syllabus': '0580',
            'syllabus_name': 'Cambridge IGCSE Mathematics (0580) Extended — Paper 2 Non-Calculator',
            'course_id': COURSE_0580_ID,
            'time_limit': 120,
            'calculator_policy': 'non-calculator',
        },
        'questions': PAPER_0580_P2_2_QUESTIONS,
    },
    {
        'code': 'm0580_p4_1',
        'pdf_rel_path': 'papers/igcse-maths/0580_p4_calc_mock1.pdf',
        'order_index': 103,
        'paper_meta': {
            'code': '0580/41',
            'title': '🧮 0580/41 Paper 4 (Extended — Calculator) Full Mock #1 [2025–2027]',
            'syllabus': '0580',
            'syllabus_name': 'Cambridge IGCSE Mathematics (0580) Extended — Paper 4 Calculator',
            'course_id': COURSE_0580_ID,
            'time_limit': 120,
            'calculator_policy': 'calculator',
        },
        'questions': PAPER_0580_P4_1_QUESTIONS,
    },
    {
        'code': 'm0580_p4_2',
        'pdf_rel_path': 'papers/igcse-maths/0580_p4_calc_mock2.pdf',
        'order_index': 104,
        'paper_meta': {
            'code': '0580/42',
            'title': '🧮 0580/42 Paper 4 (Extended — Calculator) Full Mock #2 [2025–2027]',
            'syllabus': '0580',
            'syllabus_name': 'Cambridge IGCSE Mathematics (0580) Extended — Paper 4 Calculator',
            'course_id': COURSE_0580_ID,
            'time_limit': 120,
            'calculator_policy': 'calculator',
        },
        'questions': PAPER_0580_P4_2_QUESTIONS,
    },
]


# =============================================================================
# STRUCTURAL, LATEX & MATHEMATICAL VERIFICATION SUITE
# =============================================================================
def _check_balanced_delimiters(text, context):
    assert '$' not in text, f'{context}: raw $ character found (must use \\(...\\) and £/USD)'
    assert text.count(r'\(') == text.count(r'\)'), f'{context}: unbalanced \\( \\)'
    assert text.count(r'\[') == text.count(r'\]'), f'{context}: unbalanced \\[ \\]'
    # Ensure no raw unsupported macros or HTML tag hazards for PyMuPDF Story
    for bad in [r'\begin{', r'\overrightarrow', r'\overline', r'\dot{', r'\le ', r'\ge ', r'\ne ', r'^\circ']:
        assert bad not in text, f'{context}: unsupported LaTeX macro {bad!r}'
    assert not re.search(r'<[a-zA-Z]', text), f'{context}: unspaced <letter could break HTML/PDF parser'


def verify_all_math():
    """
    Validates:
      1) Schema integrity, exact 100-mark totals per paper, unique sub-question IDs,
         balanced KaTeX delimiters, and exact Cambridge mark-code totals.
      2) Programmatic verification of key numerical/algebraic answers across all 4 papers.
    """
    assert len(MOCKS_0580_2025) == 4, f'Expected 4 mocks, got {len(MOCKS_0580_2025)}'
    expected_codes = ['m0580_p2_1', 'm0580_p2_2', 'm0580_p4_1', 'm0580_p4_2']
    expected_pdfs = [
        'papers/igcse-maths/0580_p2_noncalc_mock1.pdf',
        'papers/igcse-maths/0580_p2_noncalc_mock2.pdf',
        'papers/igcse-maths/0580_p4_calc_mock1.pdf',
        'papers/igcse-maths/0580_p4_calc_mock2.pdf',
    ]
    assert [m['code'] for m in MOCKS_0580_2025] == expected_codes
    assert [m['pdf_rel_path'] for m in MOCKS_0580_2025] == expected_pdfs
    assert [m['order_index'] for m in MOCKS_0580_2025] == [101, 102, 103, 104]

    # 1) Structural, KaTeX & Marking-Scheme Audit
    for mock in MOCKS_0580_2025:
        code = mock['code']
        meta = mock['paper_meta']
        assert meta['course_id'] == COURSE_0580_ID
        assert meta['syllabus'] == '0580'
        assert meta['time_limit'] == 120
        assert meta['calculator_policy'] in ('non-calculator', 'calculator')

        total_marks = 0
        seen_ids = set()
        for q in mock['questions']:
            qnum = q['question_number']
            stem = q.get('stem', '')
            if stem:
                _check_balanced_delimiters(stem, f'{code} Q{qnum} stem')
            assert q['sub_questions'], f'{code} Q{qnum}: empty sub_questions'
            for sq in q['sub_questions']:
                sqid = sq['id']
                assert sqid not in seen_ids, f'{code}: duplicate sub_question id {sqid}'
                seen_ids.add(sqid)
                assert sq['type'] in ('short_answer', 'structured'), f'{code} {sqid}: invalid type'
                assert sq['label'].strip(), f'{code} {sqid}: empty label'
                assert sq['marking_scheme'].strip(), f'{code} {sqid}: empty marking_scheme'
                m = int(sq['max_marks'])
                assert m > 0, f'{code} {sqid}: non-positive max_marks'
                total_marks += m

                _check_balanced_delimiters(sq['label'], f'{code} {sqid} label')
                _check_balanced_delimiters(sq['marking_scheme'], f'{code} {sqid} marking_scheme')

                # Verify Cambridge mark codes (B#, M#, A#) sum cleanly to max_marks
                segments = [seg.strip() for seg in sq['marking_scheme'].split(' | ')]
                code_sum = 0
                for seg in segments:
                    match = re.match(r'^([BMA])(\d+):', seg)
                    assert match, f'{code} {sqid}: segment missing B/M/A mark code: {seg[:40]!r}'
                    code_sum += int(match.group(2))
                assert code_sum == m, f'{code} {sqid}: mark codes sum to {code_sum}, expected {m}'

        assert total_marks == 100, f'{code}: total_marks = {total_marks}, expected EXACTLY 100'

    # 2) Programmatic Math Verification — Paper 1 (m0580_p2_1)
    assert 2**2 * 3**2 * 5 == 180
    assert math.gcd(180, 252) == 36
    assert (180 * 252) // math.gcd(180, 252) == 1260
    assert math.isqrt(180 * 5) ** 2 == 180 * 5
    assert Fraction(36, 99) == Fraction(4, 11)
    assert math.isclose((4.8e7 / 1.6e-3) + 5e9, 3.5e10)
    assert math.isclose(math.sqrt(72) - math.sqrt(18) + math.sqrt(50), 8 * math.sqrt(2))
    assert math.isclose((3 + 2 * math.sqrt(5)) * (4 - math.sqrt(5)), 2 + 5 * math.sqrt(5))
    assert math.isclose(14 / (3 - math.sqrt(2)), 6 + 2 * math.sqrt(2))
    assert Fraction(1, 3**2) == Fraction(1, 9)
    assert math.isclose(4 ** (2 * (-0.25) - 1), 1 / 8)
    for xv in [1, 2, 5, -4]:
        assert math.isclose((2 * xv**2 - 5 * xv - 3) / (xv**2 - 9), (2 * xv + 1) / (xv + 3))
        assert math.isclose(3 / (xv - 2) - 2 / (xv + 1) if xv != 2 else 0, (xv + 7) / ((xv - 2) * (xv + 1)) if xv != 2 else 0)
    for xv in [4 + math.sqrt(5), 4 - math.sqrt(5)]:
        assert math.isclose(xv**2 - 8 * xv + 11, 0.0, abs_tol=1e-12)
    assert 12 / math.sqrt(9) + 12 / math.sqrt(16) == 7
    for x_sim, y_sim in [(Fraction(2), Fraction(3)), (Fraction(-6, 5), Fraction(-17, 5))]:
        assert y_sim == 2 * x_sim - 1 and x_sim**2 + y_sim**2 == 13
    assert math.isclose(math.hypot(6 - (-2), 5 - 1), 4 * math.sqrt(5))
    # Q9 perp bisector through (2,3) with m=-2 -> y=-2x+7
    assert -2 * 2 + 7 == 3 and Fraction(5 - 1, 6 - (-2)) * (-2) == -1
    # Q10 circle angles consistency (central arcs 116 + 112 + 36 + 96 = 360)
    assert 116 + 112 + 36 + 96 == 360
    assert 112 // 2 == 56 and 116 // 2 == 58 and (112 + 36) // 2 == 74 and 180 - 74 == 106
    # Q11 trig
    val_p1_q11a = 4 * math.sin(math.radians(60)) * math.cos(math.radians(30)) + math.tan(math.radians(45))**2 - 2 * math.sin(math.radians(30))
    assert math.isclose(val_p1_q11a, 3.0)
    assert math.isclose(2 * math.sin(math.radians(60)), math.sqrt(3)) and math.isclose(2 * math.sin(math.radians(120)), math.sqrt(3))
    # Q12 sector/segment
    assert Fraction(150, 360) * 2 * 12 == 10
    assert Fraction(150, 360) * 144 == 60
    assert math.isclose(0.5 * 12 * 12 * math.sin(math.radians(150)), 36.0)
    # Q13 vectors: PM = (-1/6, 1/2), PQ = (-2/3, 2) = 4*PM
    assert 4 * Fraction(-1, 6) == Fraction(-2, 3) and 4 * Fraction(1, 2) == 2
    # Q14 cubic y = x^3 - 3x^2 - 9x + 5
    for xs, ys in [(3, -22), (-1, 10)]:
        assert 3 * xs**2 - 6 * xs - 9 == 0
        assert xs**3 - 3 * xs**2 - 9 * xs + 5 == ys
    # Q15 Venn & prob
    assert 24 + 18 - (40 - 5) == 7
    assert Fraction(5, 40) * Fraction(4, 39) == Fraction(1, 78)
    # Q16 transformations
    assert [(-y, x) for x, y in [(2, 1), (4, 1), (4, 2)]] == [(-1, 2), (-1, 4), (-2, 4)]
    assert [(0 - 2 * (x - 0), 1 - 2 * (y - 1)) for x, y in [(2, 1), (4, 1), (4, 2)]] == [(-4, 1), (-8, 1), (-8, -1)]
    # Q17 stats & inverse proportion
    nums = [10, 13, 15, 16, 16]
    assert sum(nums) / 5 == 14 and nums[2] == 15 and nums[-1] - nums[0] == 6
    assert 24 / math.sqrt(9) == 8

    # 3) Programmatic Math Verification — Paper 2 (m0580_p2_2)
    assert 2 * (12.5 + 8.5) == 42
    assert Fraction(41, 1) / Fraction(15, 2) == Fraction(82, 15)
    assert math.isclose((math.sqrt(48) + math.sqrt(27)) / math.sqrt(3), 7.0)
    assert math.isclose(10 / (math.sqrt(7) - math.sqrt(2)) - 2 * math.sqrt(7), 2 * math.sqrt(2))
    assert Fraction(243, 990) == Fraction(27, 110)
    assert math.isclose(float(Fraction(27, 110)), 0.2454545454545)
    assert Fraction(81, 16) == Fraction(3**4, 2**4) and Fraction(3, 2)**3 == Fraction(27, 8)
    assert Fraction(68, 1) / Fraction(85, 100) == 80
    assert (60 + 60, 150, 240 - 60) == (120, 150, 180)
    assert Fraction(2, math.isqrt(36)) == Fraction(1, 3)
    assert [2 * n**2 + 3 for n in range(1, 6)] == [5, 11, 21, 35, 53]
    assert Fraction(7 + 2, 3 * 7 - 1) == Fraction(9, 20)
    assert Fraction(1, 2) * (50 + 100) * 25 == 1875 and Fraction(25, 20) == Fraction(5, 4) and Fraction(1, 2) * 30 * 25 == 375
    assert math.isclose(2 * math.cos(math.radians(120)), -1.0) and math.isclose(2 * math.cos(math.radians(240)), -1.0)
    assert math.isclose(8**2 + (6 * math.sqrt(3))**2 - 2 * 8 * 6 * math.sqrt(3) * math.cos(math.radians(30)), 28.0)
    assert 360 // 30 == 12 and 4 + 4 * Fraction(15, 6) == 14
    assert 4**2 * 6 == 96 and Fraction(1, 3) * 6**2 * 8 == 96 and math.hypot(6, 8) == 10 and 6 * 10 + 6**2 == 96
    assert 3 * 2 + 2 * 3 == 12 and 2 * 2 - 3 * 3 + 5 == 0
    U = set(range(1, 13))
    A = {x for x in U if x % 2 == 0}
    B = {x for x in U if x % 3 == 0}
    C = {2, 3, 5, 7, 11}
    assert (A & B) == {6, 12} and (A & C) == {2}
    assert ((U - (A | B)) & C) == {5, 7, 11}
    assert (U - (A | B | C)) == {1}
    # Q14 cubic y = 2x^3 - 9x^2 + 12x + 1
    assert 2 * 27 - 9 * 9 + 12 * 3 + 1 == 10 and 6 * 9 - 18 * 3 + 12 == 12 and 12 * 3 - 26 == 10
    assert (2 * 1 - 9 + 12 + 1) == 6 and (2 * 8 - 36 + 24 + 1) == 5
    # Q15 vectors
    assert math.hypot(3, -4) == 5 and (2 * 3 - 3 * (-2), 2 * (-4) - 3 * 5) == (12, -23)
    assert (3 - 2 * 1, -4 + 5 * 1) == (1, 1)
    # Q16 prob
    assert Fraction(5, 8) * Fraction(4, 7) == Fraction(5, 14)
    assert 2 * Fraction(5, 8) * Fraction(3, 7) == Fraction(15, 28)
    assert Fraction(5 * 4 * 3 + 3 * 2 * 1, 8 * 7 * 6) == Fraction(11, 56)
    # Q17 algebraic fraction eq
    for xr in [Fraction(3), Fraction(-1, 2)]:
        assert Fraction(2, xr - 1) + Fraction(5, xr + 2) == 2

    # 4) Programmatic Math Verification — Paper 3 (m0580_p4_1)
    assert round(4500 * 1.036**5, 2) == 5370.46
    assert round((2385.04 / 2000) ** 0.25 * 100 - 100, 1) == 4.5
    assert math.isclose(779 / 0.82, 950.0)
    assert math.isclose((640 * 1.27 - 350) / 1.30, 356.0)
    assert 3 * (10 / (3 + 2)) - 4 == 2
    r1_p3 = (-4 + math.sqrt(60)) / 2
    r2_p3 = (-4 - math.sqrt(60)) / 2
    assert round(r1_p3, 2) == 1.87 and round(r2_p3, 2) == -5.87
    assert math.isclose(30 / (r1_p3 + 2) - 4, 2 * r1_p3)
    v_toy = (550 / 3) * math.pi
    sa_toy = 115 * math.pi
    assert round(v_toy) == 576 and round(sa_toy) == 361
    assert math.isclose(480 * (18 / 12)**3 / 1000, 1.62)
    # Q4 bearings via Cartesian coords
    bx, by = 42 * math.sin(math.radians(65)), 42 * math.cos(math.radians(65))
    cx, cy = bx + 58 * math.sin(math.radians(140)), by + 58 * math.cos(math.radians(140))
    ac_len = math.hypot(cx, cy)
    bearing_ac = math.degrees(math.atan2(cx, cy)) % 360
    area_abc = 0.5 * 42 * 58 * math.sin(math.radians(105))
    short_d = 2 * area_abc / ac_len
    assert round(ac_len, 1) == 79.9 and round(bearing_ac, 1) == 109.5 and round(short_d, 1) == 29.4
    # Q5 stats
    assert (8 * 5 + 24 * 15 + 30 * 27.5 + 18 * 47.5) / 80 == 26.0
    assert math.isclose((30 / 15) * 2, 4.0) and math.isclose((18 / 25) * 2, 1.44)
    q1_p3 = 10 + ((20 - 8) / 24) * 10
    q2_p3 = 20 + ((40 - 32) / 30) * 15
    q3_p3 = 20 + ((60 - 32) / 30) * 15
    assert (q1_p3, q2_p3, q3_p3, q3_p3 - q1_p3) == (15.0, 24.0, 34.0, 19.0)
    # Q6 3D pyramid
    assert math.hypot(16, 12) == 20
    assert round(math.hypot(10, 15), 1) == 18.0
    assert round(math.degrees(math.atan(15 / 10)), 1) == 56.3
    assert round(math.degrees(math.atan(15 / 8)), 1) == 61.9
    # Q7 diff
    assert (1 - 6 + 9 + 2, 27 - 54 + 27 + 2) == (6, 2)
    assert 64 - 96 + 36 + 2 == 6 and 9 * 4 - 30 == 6
    # Q8 prob
    assert Fraction(5, 15) * Fraction(4, 14) == Fraction(2, 21)
    assert Fraction(30 + 20 + 12, 210) == Fraction(31, 105)
    assert Fraction(30, 62) == Fraction(15, 31)
    assert Fraction(11, 15) * Fraction(10, 14) * Fraction(4, 13) == Fraction(44, 273)
    # Q9 coord geom & vectors
    assert math.isclose(math.hypot(6, 3) * math.hypot(-2, 4), 30.0)
    assert 4 * 9 == 7 * 5 + 1 and 4 * 2 == 7 * 1 + 1
    # Q10 seq & bounds
    assert [2 * n**2 + n + 1 for n in range(1, 5)] == [4, 11, 22, 37]
    assert 2 * 20**2 + 20 + 1 == 821
    assert round(252.5 / 3.95, 1) == 63.9 and round(247.5 / 4.05, 1) == 61.1

    # 5) Programmatic Math Verification — Paper 4 (m0580_p4_2)
    assert round(28000 * 0.86**4) == 15316
    assert round(((95 * 36 + 25 * 22 - 3000) / 3000) * 100, 1) == 32.3
    assert 5000 * 1.042**8 < 7000 < 5000 * 1.042**9
    assert round(5.97e24 / 6.42e23, 2) == 9.30
    x_pos = (-7 + math.sqrt(217)) / 2
    x_neg = (-7 - math.sqrt(217)) / 2
    assert round(x_pos, 2) == 3.87 and round(x_neg, 2) == -10.87
    assert round(6 * x_pos + 12, 1) == 35.2
    assert 3 * math.sqrt(1) - 2 == 1 and 3 * math.sqrt(25) - 2 == 13
    # Q3 frustum
    v_frus = (3800 / 3) * math.pi
    csa_frus = math.pi * (15 * math.hypot(15, 24) - 10 * math.hypot(10, 16))
    d_tank = v_frus / (math.pi * 16**2)
    assert round(v_frus, -1) == 3980 and round(csa_frus) == 741 and round(d_tank, 2) == 4.95
    # Q4 quad trig
    ac_p4 = math.sqrt(11.4**2 + 9.2**2 - 2 * 11.4 * 9.2 * math.cos(math.radians(112)))
    ang_bac = math.degrees(math.asin(9.2 * math.sin(math.radians(112)) / ac_p4))
    area_abcd = 0.5 * 11.4 * 9.2 * math.sin(math.radians(112)) + 0.5 * ac_p4 * 13.5 * math.sin(math.radians(38))
    assert round(ac_p4, 1) == 17.1 and round(ang_bac, 1) == 29.9 and round(area_abcd) == 120
    # Q5 3D cuboid
    ag_len = math.sqrt(14**2 + 9**2 + 6**2)
    assert round(ag_len, 1) == 17.7
    assert round(math.degrees(math.asin(6 / ag_len)), 1) == 19.8
    assert round(2 * math.degrees(math.atan(7 / 6)), 1) == 98.8
    assert round(math.degrees(math.atan(6 / 9)), 1) == 33.7
    # Q6 stats
    assert (18 * 110 + 42 * 130 + 45 * 155 + 15 * 185) / 120 == 143.25
    assert 140 + ((96 - 60) / 45) * 30 == 164.0
    # Q7 diff
    assert ((-2)**3 - 3 * (-2)**2 - 24 * (-2) + 10) == 38
    assert (4**3 - 3 * 4**2 - 24 * 4 + 10) == -70
    # Q8 prob
    assert math.isclose(0.3 * 0.85, 0.255)
    assert math.isclose(0.3 * 0.85 + 0.7 * 0.4, 0.535)
    assert Fraction(255, 535) == Fraction(51, 107)
    assert math.isclose(1 - 0.7**3, 0.657)
    # Q9 circle tangents
    assert math.sqrt(17**2 - 8**2) == 15
    ang_aob = 2 * math.degrees(math.acos(8 / 17))
    shaded_p4 = 8 * 15 - (ang_aob / 360) * math.pi * 8**2
    assert round(ang_aob, 1) == 123.9 and round(shaded_p4, 1) == 50.8
    # Q10 vectors & exponential seq
    assert Fraction(80) * Fraction(3, 4)**3 == Fraction(135, 4) == 33.75
    assert 80 * 0.75**7 > 10 > 80 * 0.75**8

    print('ALL 4 CAMBRIDGE IGCSE 0580 (2025–2027) FULL MOCKS VERIFIED SUCCESSFULLY:')
    for mock in MOCKS_0580_2025:
        q_count = len(mock['questions'])
        sq_count = sum(len(q['sub_questions']) for q in mock['questions'])
        m_total = sum(sq['max_marks'] for q in mock['questions'] for sq in q['sub_questions'])
        print(f"  - {mock['code']} ({mock['paper_meta']['code']}): {q_count} Qs, {sq_count} sub-Qs, {m_total} marks [{mock['paper_meta']['calculator_policy']}]")


if __name__ == '__main__':
    verify_all_math()
