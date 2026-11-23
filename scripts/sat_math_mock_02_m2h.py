# -*- coding: utf-8 -*-
"""
Digital SAT Math Adaptive Mock Test #2 — Module 2 Hard (650–800 Band: 22 Questions)
True 750–800 parametric & multi-step boss questions on Q14–Q22.
Domains: Algebra (Q1-Q8), Advanced Math (Q9-Q15),
         Problem-Solving and Data Analysis (Q16-Q19), Geometry and Trigonometry (Q20-Q22)
Format: 16 MCQ (A:4, B:4, C:4, D:4) + 6 SPR (Q5, Q9, Q13, Q16, Q19, Q22)
"""

import os
import sys
from fractions import Fraction
import math

sys.path.insert(0, os.path.dirname(__file__))
from sat_math_helpers import (
    math_mcq,
    math_spr,
    build_math_table,
    svg_circle_sector,
    svg_cylinder,
)


def verify_math():
    """Programmatic exact verification of all 22 Module 2 Hard answers."""
    # Q1: (5x - 3)/4 - (2x + 1)/3 = 11/12 => 7x - 13 = 11 => 7x = 24 => 7x - 2 = 22
    x1 = Fraction(24, 7)
    assert (5 * x1 - 3) / 4 - (2 * x1 + 1) / 3 == Fraction(11, 12)
    assert 7 * x1 - 2 == 22

    # Q2: f(2) = -1, f(6) = 11 -> f(x) = 3x - 7; g(x) = f(x - 3) + 5 = 3x - 11 -> x-int 11/3
    m2 = Fraction(11 - (-1), 6 - 2)
    assert m2 == 3
    f2 = lambda x: 3 * x - 7
    assert f2(2) == -1 and f2(6) == 11
    g2 = lambda x: f2(x - 3) + 5
    assert g2(Fraction(11, 3)) == 0

    # Q3: x + y = 250, 0.15x + 0.40y = 0.24*250 = 60 -> y = 90, x = 160, x - y = 70
    y3 = Fraction(60 - Fraction(15, 100) * 250, Fraction(25, 100))
    x3 = 250 - y3
    assert x3 == 160 and y3 == 90 and x3 - y3 == 70
    assert Fraction(15, 100) * x3 + Fraction(40, 100) * y3 == 60

    # Q4: 2|3x - 7| - 5 = 13 -> |3x - 7| = 9 -> x = 16/3 or -2/3, sum = 14/3
    r4a = Fraction(7 + 9, 3)
    r4b = Fraction(7 - 9, 3)
    assert 2 * abs(3 * r4a - 7) - 5 == 13
    assert 2 * abs(3 * r4b - 7) - 5 == 13
    assert r4a + r4b == Fraction(14, 3)

    # Q5 (SPR): (3/4)x - (5/6)y = 7 and ax + 10y = b infinitely many -> mult = -12 -> a = -9, b = -84, a + b = -93
    mult5 = Fraction(10, 1) / Fraction(-5, 6)
    a5 = Fraction(3, 4) * mult5
    b5 = 7 * mult5
    assert mult5 == -12 and a5 == -9 and b5 == -84 and a5 + b5 == -93

    # Q6: linear h: (c, 19), (c+4, 7), (c+10, -11), h(0) = 31 -> m = -3, -3c + 31 = 19 -> c = 4
    m6a = Fraction(7 - 19, 4)
    m6b = Fraction(-11 - 7, 6)
    assert m6a == m6b == -3
    c6 = Fraction(31 - 19, 3)
    assert c6 == 4 and -3 * c6 + 31 == 19 and -3 * (c6 + 10) + 31 == -11

    # Q7: 45s + 75t <= 1200, s >= 2t -> 165t <= 1200 -> max integer t = 7
    assert 45 * (2 * 7) + 75 * 7 <= 1200
    assert 45 * (2 * 8) + 75 * 8 > 1200

    # Q8: a(3x - 2) + 5 = b(x + 4) - 7 -> (3a - b)x = 2a + 4b - 12 -> no sol iff b = 3a and 14a != 12 (a != 6/7)
    a_bad = Fraction(6, 7)
    b_bad = 3 * a_bad
    assert 2 * a_bad + 4 * b_bad - 12 == 0
    assert 2 * 1 + 4 * 3 - 12 != 0

    # Q9 (SPR): 3x^2 - 14x + c = 0, r^2 + s^2 = 100/9 -> c = 16
    s_sum = Fraction(14, 3)
    two_rs = s_sum ** 2 - Fraction(100, 9)
    rs = two_rs / 2
    c9 = 3 * rs
    assert c9 == 16
    assert 14 ** 2 - 4 * 3 * c9 > 0  # real roots verified (2 and 8/3)
    assert Fraction(2) ** 2 + Fraction(8, 3) ** 2 == Fraction(100, 9)

    # Q10: C(t) = 500 * (0.512)^(t/12) = 500 * (0.8^3)^(t/12) = 500 * (0.8)^(t/4)
    assert Fraction(4, 5) ** 3 == Fraction(512, 1000)
    assert Fraction(3, 12) == Fraction(1, 4)

    # Q11: P(x) = 2x^3 + kx^2 - 11x + 6 divisible by (2x - 1) -> k = -3 -> P(2) = -12
    # P(1/2) = 2/8 + k/4 - 11/2 + 6 = (k + 3)/4 = 0 -> k = -3
    k11 = -3
    p11 = lambda x: 2 * x ** 3 + k11 * x ** 2 - 11 * x + 6
    assert p11(Fraction(1, 2)) == 0
    assert p11(2) == -12

    # Q12: 2x/(x - 4) - 9/(x + 2) = 48/(x^2 - 2x - 8) -> x = -3/2 (x = 4 extraneous)
    x12 = Fraction(-3, 2)
    lhs12 = (2 * x12) / (x12 - 4) - Fraction(9, 1) / (x12 + 2)
    rhs12 = Fraction(48, 1) / (x12 ** 2 - 2 * x12 - 8)
    assert lhs12 == rhs12

    # Q13 (SPR): f(1) = f(9) = 29, min = -3 -> vertex (5, -3), a = 2, f(3) = 5
    h13 = Fraction(1 + 9, 2)
    k13 = -3
    a13 = Fraction(29 - k13, (1 - h13) ** 2)
    f13 = lambda x: a13 * (x - h13) ** 2 + k13
    assert f13(1) == 29 and f13(9) == 29 and f13(5) == -3 and f13(3) == 5

    # Q14: 3x^2 - kx + 27 = 2x + 15 -> 3x^2 - (k + 2)x + 12 = 0 -> no real roots iff (k+2)^2 < 144 -> k < 10 -> max int k = 9
    assert (9 + 2) ** 2 - 4 * 3 * 12 < 0
    assert (10 + 2) ** 2 - 4 * 3 * 12 == 0

    # Q15: g(x) = a*b^x + c through (0, 11), (1, 17), (2, 35) -> b = 3, a = 3, c = 8 -> g(3) = 89
    a15, b15, c15 = 3, 3, 8
    g15 = lambda x: a15 * (b15 ** x) + c15
    assert g15(0) == 11 and g15(1) == 17 and g15(2) == 35 and g15(3) == 89

    # Q16 (SPR): 5.4 m^3 * 2.4 g/cm^3 -> 12.96 metric tons = 324/25
    grams16 = Fraction(54, 10) * (100 ** 3) * Fraction(24, 10)
    tons16 = grams16 / (1000 * 1000)
    assert tons16 == Fraction(324, 25) and float(tons16) == 12.96

    # Q17: Hall X: 10(5),20(3),30(4),40(3),50(5); Hall Y: 10(2),20(4),30(8),40(4),50(2)
    hx = [10] * 5 + [20] * 3 + [30] * 4 + [40] * 3 + [50] * 5
    hy = [10] * 2 + [20] * 4 + [30] * 8 + [40] * 4 + [50] * 2
    mx, my = Fraction(sum(hx), len(hx)), Fraction(sum(hy), len(hy))
    vx = Fraction(sum((v - mx) ** 2 for v in hx), len(hx))
    vy = Fraction(sum((v - my) ** 2 for v in hy), len(hy))
    assert mx == my == 30 and vx == 230 and vy == 120 and vx > vy

    # Q18: B = 1.35A, C = 0.80B = 1.08A = 216 -> A = 200
    a18 = Fraction(216, 1) / (Fraction(135, 100) * Fraction(80, 100))
    assert a18 == 200

    # Q19 (SPR): (35*26 + 65*34 + 46n) / (100 + n) = 36 -> n = 48
    n19 = Fraction(3600 - (35 * 26 + 65 * 34), 46 - 36)
    assert n19 == 48
    assert Fraction(35 * 26 + 65 * 34 + 46 * n19, 100 + n19) == 36

    # Q20: x^2 + y^2 - 12x + 16y + k = 0, r = 9 -> (x-6)^2 + (y+8)^2 = 100 - k = 81 -> k = 19
    assert 6 ** 2 + (-8) ** 2 - 19 == 9 ** 2

    # Q21: circle r = 18, shaded arc = 15pi -> shaded area = 135pi, unshaded area = 324pi - 135pi = 189pi
    total_area21 = 18 ** 2
    frac_shaded21 = Fraction(15, 2 * 18)
    shaded21 = frac_shaded21 * total_area21
    unshaded21 = total_area21 - shaded21
    assert shaded21 == 135 and unshaded21 == 189

    # Q22 (SPR): Similar cylinders: TSA_P = 72pi, TSA_Q = 162pi, V_P = 64pi -> k = 3/2, V_Q = 216pi -> V = 216
    k2_22 = Fraction(162, 72)
    k_22 = Fraction(math.isqrt(k2_22.numerator), math.isqrt(k2_22.denominator))
    assert k_22 ** 2 == k2_22 and k_22 == Fraction(3, 2)
    v_q = 64 * (k_22 ** 3)
    assert v_q == 216
    # Verify physical realizability with r_P = 2, h_P = 16 and r_Q = 3, h_Q = 24
    assert 2 * (2 ** 2) + 2 * 2 * 16 == 72 and (2 ** 2) * 16 == 64
    assert 2 * (3 ** 2) + 2 * 3 * 24 == 162 and (3 ** 2) * 24 == 216
    return True


def get_m2h_questions():
    qs = []

    # Q1 - Algebra - Medium - C
    qs.append(math_mcq(
        qid='sat_mm2_m2h_q1',
        number=1,
        domain='Algebra',
        skill='Linear equations with fractional coefficients',
        difficulty='Medium',
        stimulus_html=r'<p>\[\frac{5x - 3}{4} - \frac{2x + 1}{3} = \frac{11}{12}\]</p>',
        question_html=r'<p>If \(x\) is the solution to the equation above, what is the value of \(7x - 2\)?</p>',
        options_dict={
            'A': r'\(\frac{24}{7}\)',
            'B': r'\(14\)',
            'C': r'\(22\)',
            'D': r'\(24\)',
        },
        correct_label='C',
        summary_vi=r'Nhân cả hai vế với mẫu số chung \(12\) để khử toàn bộ phân số: \(3(5x - 3) - 4(2x + 1) = 11\). Khai triển cẩn thận dấu trừ: \(15x - 9 - 8x - 4 = 11 \Rightarrow 7x - 13 = 11 \Rightarrow 7x = 24\). Không cần chia lẻ ra \(x\), trừ ngay \(2\) ở hai vế: \(7x - 2 = 24 - 2 = 22\).',
        key_takeaway=r'Khi đề hỏi biểu thức \(7x - 2\) và bạn đã giải ra \(7x = 24\), hãy dùng thẳng \(7x = 24\) thay vì tính phân số lẻ \(x = \frac{24}{7}\).',
        desmos_tip_vi=r'Gõ nguyên phương trình vào Desmos để thấy đường đứng tại \(x \approx 3.4286\), rồi gõ <code>7*(24/7) - 2</code> hoặc dùng giá trị giao điểm nhân \(7\) trừ \(2\) ra \(22\).',
        option_analysis={
            'A': ('Solved for x Only', r'Đây là giá trị của \(x = \frac{24}{7}\), chưa tính biểu thức \(7x - 2\).'),
            'B': ('Distribution Sign Error', r'Quên đổi dấu \(-4(+1)\) thành \(-4\), giải sai thành \(7x - 5 = 11 \Rightarrow 7x = 16 \Rightarrow 7x - 2 = 14\).'),
            'C': ('Correct', r'Từ \(7x = 24\) suy thẳng ra \(7x - 2 = 22\).'),
            'D': ('Forgot Subtraction Step', r'Dừng lại ở \(7x = 24\) và quên trừ đi \(2\).'),
        },
    ))

    # Q2 - Algebra - Medium - A
    qs.append(math_mcq(
        qid='sat_mm2_m2h_q2',
        number=2,
        domain='Algebra',
        skill='Linear function transformations and intercepts',
        difficulty='Medium',
        stimulus_html=r'<p>For a linear function \(f\), \(f(2) = -1\) and \(f(6) = 11\). The function \(g\) is defined by \(g(x) = f(x - 3) + 5\).</p>',
        question_html=r'<p>What is the \(x\)-intercept of the graph of \(y = g(x)\) in the \(xy\)-plane?</p>',
        options_dict={
            'A': r'\(\left(\frac{11}{3}, 0\right)\)',
            'B': r'\(\left(\frac{7}{3}, 0\right)\)',
            'C': r'\(\left(-\frac{11}{3}, 0\right)\)',
            'D': r'\((0, -11)\)',
        },
        correct_label='A',
        summary_vi=r'Tìm công thức của \(f\): hệ số góc \(m = \frac{11 - (-1)}{6 - 2} = \frac{12}{4} = 3\). Suy ra \(f(x) = 3(x - 2) - 1 = 3x - 7\). Thay \(x\) bằng \(x - 3\) rồi cộng \(5\) để tìm \(g(x)\): \(g(x) = 3(x - 3) - 7 + 5 = 3x - 9 - 2 = 3x - 11\). Giao điểm trục hoành (\(x\)-intercept) ứng với \(g(x) = 0 \Rightarrow 3x - 11 = 0 \Rightarrow x = \frac{11}{3}\), tức \(\left(\frac{11}{3}, 0\right)\).',
        key_takeaway=r'Với hàm tịnh tiến \(g(x) = f(x - 3) + 5\), hãy tìm công thức rõ ràng của \(f(x)\) rồi thế nguyên cụm \((x - 3)\) vào vị trí của \(x\).',
        desmos_tip_vi=r'Gõ <code>f(x) = 3x - 7</code> và <code>g(x) = f(x - 3) + 5</code> trên Desmos, sau đó bấm thẳng vào chấm xám giao trục hoành của \(g(x)\) để thấy \((3.667, 0) = \left(\frac{11}{3}, 0\right)\).',
        option_analysis={
            'A': ('Correct', r'\(g(x) = 3x - 11 = 0 \Rightarrow x = \frac{11}{3}\).'),
            'B': ('Forgot Transformation', r'Đây là \(x\)-intercept của hàm gốc \(f(x) = 3x - 7 = 0 \Rightarrow x = \frac{7}{3}\), chưa áp dụng phép tịnh tiến.'),
            'C': ('Shift Direction Error', r'Dịch nhầm sang trái thành \(f(x + 3) + 5 = 3x + 7\) hoặc sai dấu nghiệm thành \(-\frac{11}{3}\).'),
            'D': ('Y-Intercept Confusion', r'Đây là \(y\)-intercept \((0, -11)\) của \(g(x)\), không phải \(x\)-intercept.'),
        },
    ))

    # Q3 - Algebra - Medium-Hard - D
    qs.append(math_mcq(
        qid='sat_mm2_m2h_q3',
        number=3,
        domain='Algebra',
        skill='Systems of linear equations — mixture problems',
        difficulty='Hard',
        stimulus_html=r'<p>In a biomedical cell-culture lab, a technician combines \(x\) milliliters of a \(15\%\) saline buffer solution with \(y\) milliliters of a \(40\%\) saline buffer solution to create \(250\) milliliters of a \(24\%\) saline buffer solution.</p>',
        question_html=r'<p>How many milliliters more of the \(15\%\) solution than of the \(40\%\) solution did the technician use?</p>',
        options_dict={
            'A': r'\(40\)',
            'B': r'\(50\)',
            'C': r'\(60\)',
            'D': r'\(70\)',
        },
        correct_label='D',
        summary_vi=r'Lập hệ hai phương trình: tổng thể tích \(x + y = 250\), và tổng lượng muối tinh khiết \(0.15x + 0.40y = 0.24(250) = 60\). Thay \(x = 250 - y\) vào phương trình muối: \(0.15(250 - y) + 0.40y = 60 \Rightarrow 37.5 + 0.25y = 60 \Rightarrow 0.25y = 22.5 \Rightarrow y = 90\text{ mL}\). Suy ra \(x = 250 - 90 = 160\text{ mL}\). Hiệu thể tích đề hỏi là \(x - y = 160 - 90 = 70\text{ mL}\).',
        key_takeaway=r'Mẹo cân bằng nồng độ (Alligation): khoảng cách tới \(24\%\) lần lượt là \(|24 - 15| = 9\) và \(|40 - 24| = 16\), nên tỉ lệ thể tích đảo ngược là \(x : y = 16 : 9\). Trong \(250\text{ mL}\), \(x = 160, y = 90\), hiệu \(x - y = 70\) chỉ trong 5 giây!',
        desmos_tip_vi=r'Gõ hai dòng <code>x + y = 250</code> và <code>0.15x + 0.40y = 0.24*250</code>, bấm vào giao điểm \((160, 90)\) rồi tính \(160 - 90 = 70\).',
        option_analysis={
            'A': ('Arithmetic Estimation Trap', r'Nhầm lẫn chênh lệch phần trăm \(40 - 15 = 25\) hoặc trừ sai \(160 - 120 = 40\).'),
            'B': ('Wrong Concentration Split', r'Chia sai tỉ lệ thành \(150\) và \(100\), dẫn tới hiệu \(50\).'),
            'C': ('Pure Solute Quantity Trap', r'Đây là tổng lượng muối tinh khiết \(0.24 \times 250 = 60\text{ mL}\), không phải hiệu \(x - y\).'),
            'D': ('Correct', r'Giải chính xác \(x = 160, y = 90\), suy ra \(x - y = 70\).'),
        },
    ))

    # Q4 - Algebra - Medium-Hard - B
    qs.append(math_mcq(
        qid='sat_mm2_m2h_q4',
        number=4,
        domain='Algebra',
        skill='Absolute value equations',
        difficulty='Hard',
        stimulus_html=r'<p>\[2|3x - 7| - 5 = 13\]</p>',
        question_html=r'<p>What is the sum of all solutions to the equation above?</p>',
        options_dict={
            'A': r'\(\frac{7}{3}\)',
            'B': r'\(\frac{14}{3}\)',
            'C': r'\(\frac{16}{3}\)',
            'D': r'\(6\)',
        },
        correct_label='B',
        summary_vi=r'Cô lập dấu giá trị tuyệt đối: \(2|3x - 7| = 18 \Rightarrow |3x - 7| = 9\). Tách thành hai trường hợp: (1) \(3x - 7 = 9 \Rightarrow 3x = 16 \Rightarrow x = \frac{16}{3}\); (2) \(3x - 7 = -9 \Rightarrow 3x = -2 \Rightarrow x = -\frac{2}{3}\). Tổng hai nghiệm là \(\frac{16}{3} + \left(-\frac{2}{3}\right) = \frac{14}{3}\).',
        key_takeaway=r'Công thức siêu tốc 800 Math: Khi \(|ax + b| = c\) với \(c > 0\), hai nghiệm luôn đối xứng quanh tâm \(x_0 = -\frac{b}{a}\), nên TỔNG HAI NGHIỆM luôn bằng \(2x_0 = -\frac{2b}{a} = \frac{14}{3}\)!',
        desmos_tip_vi=r'Gõ <code>y = 2|3x - 7| - 5</code> và <code>y = 13</code> trong Desmos, đọc hai hoành độ giao điểm \(-0.667\) và \(5.333\), cộng lại ra \(4.667 = \frac{14}{3}\).',
        option_analysis={
            'A': ('Midpoint Only Trap', r'Đây chỉ là trục đối xứng \(x_0 = \frac{7}{3}\) (trung bình cộng hai nghiệm), quên nhân đôi để ra tổng.'),
            'B': ('Correct', r'Tổng hai nghiệm \(\frac{16}{3} + \left(-\frac{2}{3}\right) = \frac{14}{3}\).'),
            'C': ('Positive Root Only Trap', r'Chỉ giải nhánh dương \(3x - 7 = 9 \Rightarrow x = \frac{16}{3}\) mà bỏ sót nhánh âm.'),
            'D': ('Absolute Value Sum Error', r'Cộng nhầm giá trị tuyệt đối của hai nghiệm: \(\frac{16}{3} + \frac{2}{3} = 6\).'),
        },
    ))

    # Q5 - Algebra - Hard - SPR
    qs.append(math_spr(
        qid='sat_mm2_m2h_q5',
        number=5,
        domain='Algebra',
        skill='Parametric linear systems — infinitely many solutions',
        difficulty='Hard',
        stimulus_html=r'<p>\[\frac{3}{4}x - \frac{5}{6}y = 7\]\[ax + 10y = b\]</p>',
        question_html=r'<p>In the system of equations above, \(a\) and \(b\) are constants. If the system has infinitely many solutions, what is the value of \(a + b\)?</p>',
        accepted_answers=['-93'],
        correct_display='-93',
        summary_vi=r'Hệ có vô số nghiệm khi hai phương trình hoàn toàn trùng nhau (tỉ lệ thuận ở cả 3 hệ số \(x, y\) và vế phải). Tìm hệ số nhân từ phương trình (1) sang phương trình (2) dựa vào hệ số của \(y\): \(k = \frac{10}{-5/6} = 10 \cdot \left(-\frac{6}{5}\right) = -12\). Nhân toàn bộ phương trình (1) với \(-12\): \(-12\left(\frac{3}{4}x\right) - 12\left(-\frac{5}{6}y\right) = -12(7) \Rightarrow -9x + 10y = -84\). So sánh trực tiếp với \(ax + 10y = b\), ta có \(a = -9\) và \(b = -84\). Vậy \(a + b = -9 + (-84) = -93\).',
        key_takeaway=r'Với hệ vô số nghiệm, tìm đúng hệ số tỷ lệ \(k\) từ cặp hệ số ĐÃ BIẾT (ở đây là hệ số của \(y\)), chú ý dấu âm của \(-\frac{5}{6}y\), rồi nhân \(k\) cho cả hai cột còn lại.',
        desmos_tip_vi=r'Gõ <code>k = 10 / (-5/6)</code> (ra \(-12\)), rồi gõ dòng hai <code>k*(3/4) + k*7</code> trên Desmos để chốt chuẩn \(-93\) trong 5 giây.',
    ))

    # Q6 - Algebra - Hard - A
    t6 = build_math_table(
        [r'\(x\)', r'\(h(x)\)'],
        [[r'\(c\)', r'\(19\)'], [r'\(c + 4\)', r'\(7\)'], [r'\(c + 10\)', r'\(-11\)']],
        caption='High-Speed Rail Braking Telemetry (Linear Function h)'
    )
    qs.append(math_mcq(
        qid='sat_mm2_m2h_q6',
        number=6,
        domain='Algebra',
        skill='Parametric linear functions from tables',
        difficulty='Hard',
        stimulus_html=rf'<p>The table below shows three values of \(x\) and their corresponding values of \(h(x)\) for a linear function \(h\) modeling a high-speed train’s braking velocity, where \(c\) is a constant.</p>{t6}',
        question_html=r'<p>If \(h(0) = 31\), what is the value of \(c\)?</p>',
        options_dict={
            'A': r'\(4\)',
            'B': r'\(6\)',
            'C': r'\(-4\)',
            'D': r'\(12\)',
        },
        correct_label='A',
        summary_vi=r'Dù cột \(x\) chứa ẩn \(c\), hiệu \(\Delta x\) hoàn toàn triệt tiêu \(c\): hệ số góc \(m = \frac{7 - 19}{(c + 4) - c} = \frac{-12}{4} = -3\). Kiểm tra lại với cặp sau: \(\frac{-11 - 7}{(c + 10) - (c + 4)} = \frac{-18}{6} = -3\) (khớp!). Vì \(h(0) = 31\) là tung độ gốc, công thức hàm là \(h(x) = -3x + 31\). Thay điểm \((c, 19)\): \(-3c + 31 = 19 \Rightarrow 3c = 12 \Rightarrow c = 4\).',
        key_takeaway=r'Gặp bảng hàm bậc nhất chứa tham số dạng \(c, c + 4, c + 10\): lấy hiệu hai giá trị \(x\) lập tức triệt tiêu \(c\) để tìm ra ngay hệ số góc \(m\).',
        desmos_tip_vi=r'Khi đã biết \(m = -3\) và \(b = 31\), gõ <code>y = -3x + 31</code> và <code>y = 19</code> vào Desmos để đọc hoành độ giao điểm \(x = 4\).',
        option_analysis={
            'A': ('Correct', r'\(h(x) = -3x + 31\) với \(h(4) = 19\), \(h(8) = 7\), \(h(14) = -11\).'),
            'B': ('Wrong Row Substituted', r'Giải nhầm \(h(c) = 13\) hoặc lấy \(\frac{18}{3} = 6\).'),
            'C': ('Slope Sign Flip', r'Tính nhầm hệ số góc thành \(+3\), dẫn tới \(3c + 31 = 19 \Rightarrow c = -4\).'),
            'D': ('Forgot to Divide by Slope', r'Tính được \(31 - 19 = 12\) nhưng quên chia cho độ lớn hệ số góc \(3\).'),
        },
    ))

    # Q7 - Algebra - Hard - C
    qs.append(math_mcq(
        qid='sat_mm2_m2h_q7',
        number=7,
        domain='Algebra',
        skill='Systems of linear inequalities — optimization',
        difficulty='Hard',
        stimulus_html=r'<p>A satellite launch fairing can accommodate \(s\) optical sensor pods (each weighing \(45\text{ kg}\)) and \(t\) ion thruster packs (each weighing \(75\text{ kg}\)). Mission requirements dictate that the total payload mass cannot exceed \(1{,}200\text{ kg}\), and there must be at least twice as many optical sensor pods as ion thruster packs.</p>',
        question_html=r'<p>What is the maximum number of ion thruster packs \(t\) that can be included in the payload?</p>',
        options_dict={
            'A': r'\(5\)',
            'B': r'\(6\)',
            'C': r'\(7\)',
            'D': r'\(8\)',
        },
        correct_label='C',
        summary_vi=r'Hai ràng buộc của bài toán là: \(45s + 75t \le 1{,}200\) và \(s \ge 2t\) (với \(s, t\) nguyên không âm). Để tối đa hóa \(t\), ta chọn \(s\) nhỏ nhất có thể là \(s = 2t\) rồi thế vào ràng buộc khối lượng: \(45(2t) + 75t \le 1{,}200 \Rightarrow 90t + 75t \le 1{,}200 \Rightarrow 165t \le 1{,}200 \Rightarrow t \le \frac{1200}{165} = \frac{80}{11} \approx 7.27\). Vì \(t\) phải là số nguyên, giá trị lớn nhất có thể của \(t\) là \(7\) (khi đó \(s = 14\), tổng khối lượng \(45(14) + 75(7) = 1{,}155 \le 1{,}200\text{ kg}\)).',
        key_takeaway=r'Với bài toán bất phương trình có biến nguyên đếm (số vật phẩm), sau khi tìm cận trên dạng thập phân \(t \le 7.27\), LUÔN làm tròn XUỐNG (floor) về số nguyên \(7\).',
        desmos_tip_vi=r'Gõ <code>45x + 75y <= 1200</code> và <code>x >= 2y</code> trên Desmos, bấm vào đỉnh giao điểm phía trên cùng của miền tô đậm để thấy \((14.545, 7.273)\) \(\rightarrow\) chốt số nguyên lớn nhất \(y = 7\).',
        option_analysis={
            'A': ('Underestimation', r'Chưa đạt mức tối đa; với \(t = 5, s = 10\) mới dùng \(825\text{ kg}\), vẫn còn dư tới \(375\text{ kg}\).'),
            'B': ('Suboptimal Integer', r'Với \(t = 6, s = 12\) tổng khối lượng \(990\text{ kg}\), vẫn thêm được \(1\) gói thruster và \(2\) cảm biến.'),
            'C': ('Correct', r'\(t = 7, s = 14\) cho tổng khối lượng \(1{,}155\text{ kg} \le 1{,}200\text{ kg}\); nếu \(t = 8\) thì cần tối thiểu \(1{,}320\text{ kg}\) (vượt giới hạn).'),
            'D': ('Rounding Up Trap', r'Làm tròn lên hoặc đảo ngược điều kiện thành \(t \ge 2s\); thực tế \(t = 8 \Rightarrow s \ge 16 \Rightarrow 45(16) + 75(8) = 1{,}320 > 1{,}200\).'),
        },
    ))

    # Q8 - Algebra - Very Hard - B
    qs.append(math_mcq(
        qid='sat_mm2_m2h_q8',
        number=8,
        domain='Algebra',
        skill='Parametric linear equations — conditions for no solution',
        difficulty='Hard',
        stimulus_html=r'<p>\[a(3x - 2) + 5 = b(x + 4) - 7\]</p>',
        question_html=r'<p>In the equation above, \(a\) and \(b\) are constants. If the equation has <b>no solution</b> for \(x\), which of the following statements must be true?</p>',
        options_dict={
            'A': r'\(b = 3a\) and \(a = \frac{6}{7}\)',
            'B': r'\(b = 3a\) and \(a \ne \frac{6}{7}\)',
            'C': r'\(b \ne 3a\) and \(a = \frac{6}{7}\)',
            'D': r'\(a = 3b\) and \(b \ne \frac{6}{7}\)',
        },
        correct_label='B',
        summary_vi=r'Khai triển hai vế rồi gom toàn bộ hạng tử chứa \(x\) sang vế trái và hằng số sang vế phải: \(3ax - 2a + 5 = bx + 4b - 7 \Rightarrow (3a - b)x = 2a + 4b - 12\). Phương trình dạng \(Ax = B\) VÔ NGHIỆM khi và chỉ khi \(A = 0\) và \(B \ne 0\). Điều kiện 1: \(3a - b = 0 \Rightarrow b = 3a\). Thay \(b = 3a\) vào điều kiện 2: \(2a + 4(3a) - 12 \ne 0 \Rightarrow 14a \ne 12 \Rightarrow a \ne \frac{6}{7}\).',
        key_takeaway=r'Phương trình bậc nhất \(Ax = B\) có 3 kịch bản: \(A \ne 0\) (1 nghiệm duy nhất); \(A = 0, B = 0\) (vô số nghiệm); \(A = 0, B \ne 0\) (vô nghiệm).',
        desmos_tip_vi=r'Thử kiểm chứng bằng số: chọn \(a = \frac{6}{7}, b = \frac{18}{7}\), hai vế trở thành hai đường thẳng TRÙNG NHAU (vô số nghiệm \(\rightarrow\) loại A). Chọn \(a = 1, b = 3\), hai vế trở thành \(3x + 3 = 3x + 5\) (song song, vô nghiệm \(\rightarrow\) chốt B).',
        option_analysis={
            'A': ('Infinitely Many Solutions Trap', r'Khi \(b = 3a\) và \(a = \frac{6}{7}\), cả hai vế đều trở thành \(0x = 0\), tức phương trình có VÔ SỐ nghiệm chứ không phải vô nghiệm.'),
            'B': ('Correct', r'Đảm bảo hệ số của \(x\) bằng \(0\) (\(b = 3a\)) đồng thời vế hằng số khác \(0\) (\(14a - 12 \ne 0 \Rightarrow a \ne \frac{6}{7}\)).'),
            'C': ('Unique Solution Condition', r'Nếu \(b \ne 3a\) thì hệ số của \(x\) khác \(0\), phương trình luôn có ĐÚNG 1 nghiệm duy nhất.'),
            'D': ('Swapped Parameters', r'Đảo ngược mối quan hệ giữa \(a\) và \(b\) thành \(a = 3b\) thay vì \(b = 3a\).'),
        },
    ))

    # Q9 - Advanced Math - Medium-Hard - SPR
    qs.append(math_spr(
        qid='sat_mm2_m2h_q9',
        number=9,
        domain='Advanced Math',
        skill='Quadratic equations — Vieta formulas and sum of squares',
        difficulty='Hard',
        stimulus_html=r'<p>The quadratic equation \(3x^2 - 14x + c = 0\), where \(c\) is a constant, has two real solutions \(r\) and \(s\) such that:</p><p>\[r^2 + s^2 = \frac{100}{9}\]</p>',
        question_html=r'<p>What is the value of \(c\)?</p>',
        accepted_answers=['16'],
        correct_display='16',
        summary_vi=r'Theo định lý Vieta cho phương trình \(3x^2 - 14x + c = 0\), tổng và tích hai nghiệm là \(r + s = \frac{14}{3}\) và \(rs = \frac{c}{3}\). Sử dụng hằng đẳng thức \(r^2 + s^2 = (r + s)^2 - 2rs\): \(\frac{100}{9} = \left(\frac{14}{3}\right)^2 - 2\left(\frac{c}{3}\right) = \frac{196}{9} - \frac{2c}{3}\). Suy ra \(\frac{2c}{3} = \frac{196 - 100}{9} = \frac{96}{9} = \frac{32}{3} \Rightarrow 2c = 32 \Rightarrow c = 16\). Kiểm tra nghiệm thực: \(3x^2 - 14x + 16 = (x - 2)(3x - 8) = 0 \Rightarrow r = 2, s = \frac{8}{3}\), đúng \(2^2 + \left(\frac{8}{3}\right)^2 = \frac{100}{9}\).',
        key_takeaway=r'Hằng đẳng thức Vieta tủ cho nhóm 750+: \(r^2 + s^2 = (r + s)^2 - 2rs\) giúp tìm hằng số \(c\) cực nhanh mà không cần dùng công thức nghiệm căn thức.',
        desmos_tip_vi=r'Gõ <code>(14/3)^2 - 2*(c/3) = 100/9</code> (thay \(c\) bằng \(x\)) vào Desmos để hiện ngay đường đứng tại \(x = 16\), sau đó gõ <code>y = 3x^2 - 14x + 16</code> để kiểm tra hai nghiệm thực \(2\) và \(2.667\).',
    ))

    # Q10 - Advanced Math - Medium-Hard - D
    qs.append(math_mcq(
        qid='sat_mm2_m2h_q10',
        number=10,
        domain='Advanced Math',
        skill='Equivalent exponential forms and decay intervals',
        difficulty='Hard',
        stimulus_html=r'<p>In a biomedical bioreactor trial, the concentration \(C(t)\), in micrograms per liter, of a fluorescent tracer \(t\) hours after injection is modeled by:</p><p>\[C(t) = 500(0.512)^{\frac{t}{12}}\]</p>',
        question_html=r'<p>Which of the following equivalent forms of \(C(t)\) reveals that the tracer concentration decreases by \(20\%\) every \(4\) hours?</p>',
        options_dict={
            'A': r'\(C(t) = 500(0.128)^{\frac{t}{3}}\)',
            'B': r'\(C(t) = 500(0.64)^{\frac{t}{6}}\)',
            'C': r'\(C(t) = 500(0.8)^{\frac{t}{3}}\)',
            'D': r'\(C(t) = 500(0.8)^{\frac{t}{4}}\)',
        },
        correct_label='D',
        summary_vi=r'Giảm \(20\%\) tương ứng với hệ số nhân \(1 - 0.20 = 0.8\). Nhận thấy \(0.512 = (0.8)^3\) (vì \(8^3 = 512\)). Biến đổi theo quy tắc lũy thừa của lũy thừa: \(C(t) = 500\left((0.8)^3\right)^{\frac{t}{12}} = 500(0.8)^{\frac{3t}{12}} = 500(0.8)^{\frac{t}{4}}\). Dạng này cho thấy chính xác cứ mỗi \(4\) giờ (\(t = 4\)), nồng độ nhân với \(0.8\), tức giảm \(20\%\).',
        key_takeaway=r'Khi đề hỏi dạng hàm mũ tương đương thể hiện mức giảm \(20\%\), cơ số bắt buộc là \(0.8\); hãy viết cơ số cũ thành lũy thừa của \(0.8\) rồi rút gọn số mũ.',
        desmos_tip_vi=r'Gõ <code>f(x) = 500(0.512)^(x/12)</code> và thử <code>g(x) = 500(0.8)^(x/4)</code> vào Desmos: hai đồ thị trùng khít hoàn toàn 100%, khẳng định đáp án D.',
        option_analysis={
            'A': ('Linear Base Division Trap', r'Chia nhầm cơ số \(0.512\) cho \(4\) thành \(0.128\) thay vì lấy căn bậc ba.'),
            'B': ('Wrong Root / Wrong Factor', r'\((0.64)^{1/6} = (0.8)^{1/3} \ne (0.8)^{1/4}\), không tương đương hàm gốc và cũng không hiển thị cơ số \(0.8\).'),
            'C': ('Exponent Division Error', r'Lấy đúng cơ số \(0.8\) từ \(0.8^3 = 0.512\) nhưng lại giữ số \(3\) ở mẫu số mũ thay vì lấy \(\frac{12}{3} = 4\).'),
            'D': ('Correct', r'\((0.512)^{t/12} = (0.8^3)^{t/12} = (0.8)^{t/4}\), vừa tương đương đại số vừa thể hiện giảm \(20\%\) mỗi \(4\) giờ.'),
        },
    ))

    # Q11 - Advanced Math - Hard - B
    qs.append(math_mcq(
        qid='sat_mm2_m2h_q11',
        number=11,
        domain='Advanced Math',
        skill='Polynomial factor theorem and remainder theorem',
        difficulty='Hard',
        stimulus_html=r'<p>\[P(x) = 2x^3 + kx^2 - 11x + 6\]</p><p>In the polynomial above, \(k\) is a constant. The polynomial \(P(x)\) is divisible by \((2x - 1)\).</p>',
        question_html=r'<p>What is the remainder when \(P(x)\) is divided by \((x - 2)\)?</p>',
        options_dict={
            'A': r'\(-18\)',
            'B': r'\(-12\)',
            'C': r'\(-3\)',
            'D': r'\(12\)',
        },
        correct_label='B',
        summary_vi=r'Theo Định lý Nhân tử (Factor Theorem), \(P(x)\) chia hết cho \((2x - 1)\) nghĩa là \(P\left(\frac{1}{2}\right) = 0\). Thay \(x = \frac{1}{2}\): \(2\left(\frac{1}{8}\right) + k\left(\frac{1}{4}\right) - 11\left(\frac{1}{2}\right) + 6 = 0 \Rightarrow \frac{1}{4} + \frac{k}{4} + \frac{1}{2} = 0 \Rightarrow \frac{k + 3}{4} = 0 \Rightarrow k = -3\). Theo Định lý Số dư (Remainder Theorem), số dư khi chia \(P(x)\) cho \((x - 2)\) chính là \(P(2) = 2(2)^3 - 3(2)^2 - 11(2) + 6 = 16 - 12 - 22 + 6 = -12\).',
        key_takeaway=r'Bộ đôi định lý đa thức SAT Hard M2: chia hết cho \((ax - b) \Leftrightarrow P(b/a) = 0\); số dư khi chia cho \((x - c)\) chính bằng \(P(c)\).',
        desmos_tip_vi=r'Gõ <code>P(x) = 2x^3 + k x^2 - 11x + 6</code> kèm slider \(k\), kéo \(k\) (hoặc giải \(P(0.5) = 0\)) tìm ra \(k = -3\), rồi gõ dòng mới <code>P(2)</code> ra thẳng \(-12\).',
        option_analysis={
            'A': ('Arithmetic Error', r'Tính sai giá trị \(P(2)\) hoặc nhầm dấu \(+6\) thành \(-6\), ra \(16 - 12 - 22 - 6 = -24\) hay nhầm \(k = -6\).'),
            'B': ('Correct', r'Tìm đúng \(k = -3\) rồi tính \(P(2) = 16 - 12 - 22 + 6 = -12\).'),
            'C': ('Stopped at Parameter k', r'Đây là giá trị của hằng số \(k = -3\), học sinh quên bước cuối tính số dư \(P(2)\).'),
            'D': ('Sign Flip in Remainder', r'Tính \(P(2)\) bị ngược dấu thành \(+12\) hoặc đánh nhầm \(k = +3\) cho ra \(P(2) = 12\).'),
        },
    ))

    # Q12 - Advanced Math - Hard - A
    qs.append(math_mcq(
        qid='sat_mm2_m2h_q12',
        number=12,
        domain='Advanced Math',
        skill='Rational equations with extraneous solutions',
        difficulty='Hard',
        stimulus_html=r'<p>\[\frac{2x}{x - 4} - \frac{9}{x + 2} = \frac{48}{x^2 - 2x - 8}\]</p>',
        question_html=r'<p>What is the value of \(x\) that satisfies the equation above?</p>',
        options_dict={
            'A': r'\(-\frac{3}{2}\)',
            'B': r'\(-\frac{2}{3}\)',
            'C': r'\(\frac{3}{2}\)',
            'D': r'\(4\)',
        },
        correct_label='A',
        summary_vi=r'Phân tích mẫu số vế phải: \(x^2 - 2x - 8 = (x - 4)(x + 2)\), điều kiện xác định \(x \ne 4\) và \(x \ne -2\). Nhân cả hai vế với mẫu thức chung \((x - 4)(x + 2)\): \(2x(x + 2) - 9(x - 4) = 48 \Rightarrow 2x^2 + 4x - 9x + 36 = 48 \Rightarrow 2x^2 - 5x - 12 = 0\). Phân tích thành nhân tử: \((x - 4)(2x + 3) = 0 \Rightarrow x = 4\) hoặc \(x = -\frac{3}{2}\). Vì \(x = 4\) làm mẫu số \(x - 4 = 0\) (nghiệm ngoại lai, bị loại), nghiệm duy nhất thỏa mãn là \(x = -\frac{3}{2}\).',
        key_takeaway=r'Với phương trình chứa ẩn ở mẫu, LUÔN ghi ngay điều kiện mẫu khác \(0\) ngay bước đầu để loại tức thì nghiệm ngoại lai như \(x = 4\).',
        desmos_tip_vi=r'Gõ <code>y = 2x/(x - 4) - 9/(x + 2)</code> và <code>y = 48/(x^2 - 2x - 8)</code> vào Desmos: tại \(x = 4\) là tiệm cận đứng nên KHÔNG có giao điểm; hai đồ thị chỉ cắt nhau tại \(x = -1.5 = -\frac{3}{2}\).',
        option_analysis={
            'A': ('Correct', r'Thỏa mãn điều kiện xác định và cho hai vế cùng bằng \(-\frac{192}{11}\).'),
            'B': ('Inverted Fraction Root', r'Giải sai nhân tử \(2x + 3 = 0\) thành \(x = -\frac{2}{3}\).'),
            'C': ('Sign Error in Factoring', r'Phân tích sai dấu thành \((2x - 3)(x + 4) = 0 \Rightarrow x = \frac{3}{2}\).'),
            'D': ('Extraneous Root Trap', r'Bẫy kinh điển 750+: \(x = 4\) là nghiệm của phương trình quy đồng nhưng làm mẫu số \(x - 4 = 0\) (vô nghĩa).'),
        },
    ))

    # Q13 - Advanced Math - Hard - SPR
    qs.append(math_spr(
        qid='sat_mm2_m2h_q13',
        number=13,
        domain='Advanced Math',
        skill='Quadratic symmetry and vertex form',
        difficulty='Hard',
        stimulus_html=r'<p>The cross-section of a parabolic acoustic reflector in a concert hall is modeled by a quadratic function \(f(x) = a(x - h)^2 + k\). The function has a minimum value of \(-3\) and satisfies \(f(1) = f(9) = 29\).</p>',
        question_html=r'<p>What is the value of \(f(3)\)?</p>',
        accepted_answers=['5'],
        correct_display='5',
        summary_vi=r'Vì parabol đối xứng qua trục \(x = h\) và \(f(1) = f(9)\), hoành độ đỉnh nằm chính giữa \(1\) và \(9\): \(h = \frac{1 + 9}{2} = 5\). Giá trị nhỏ nhất của hàm là tung độ đỉnh \(k = -3\). Vậy \(f(x) = a(x - 5)^2 - 3\). Thay \(f(1) = 29\): \(a(1 - 5)^2 - 3 = 29 \Rightarrow 16a = 32 \Rightarrow a = 2\). Cuối cùng tính \(f(3) = 2(3 - 5)^2 - 3 = 2(4) - 3 = 5\).',
        key_takeaway=r'Bất cứ khi nào thấy \(f(x_1) = f(x_2)\) với hàm bậc hai, lập tức suy ra trục đối xứng (hoành độ đỉnh) là \(h = \frac{x_1 + x_2}{2}\).',
        desmos_tip_vi=r'Gõ bảng 3 điểm \((1, 29), (5, -3), (9, 29)\) rồi hồi quy <code>y1 ~ a(x1 - 5)^2 - 3</code> tìm ra \(a = 2\), sau đó tính <code>2(3 - 5)^2 - 3</code> ra ngay \(5\).',
    ))

    # Q14 - Advanced Math - Very Hard (780) - C
    qs.append(math_mcq(
        qid='sat_mm2_m2h_q14',
        number=14,
        domain='Advanced Math',
        skill='Parametric nonlinear systems — discriminant inequality',
        difficulty='Hard',
        stimulus_html=r'<p>\[p(x) = 3x^2 - kx + 27\]\[q(x) = 2x + 15\]</p><p>In the functions above, \(k\) is an integer constant. In the \(xy\)-plane, the graphs of \(y = p(x)\) and \(y = q(x)\) do <b>not</b> intersect.</p>',
        question_html=r'<p>What is the greatest possible value of the integer \(k\)?</p>',
        options_dict={
            'A': r'\(7\)',
            'B': r'\(8\)',
            'C': r'\(9\)',
            'D': r'\(10\)',
        },
        correct_label='C',
        summary_vi=r'Xét phương trình hoành độ giao điểm \(p(x) = q(x)\): \(3x^2 - kx + 27 = 2x + 15 \Rightarrow 3x^2 - (k + 2)x + 12 = 0\). Hai đồ thị KHÔNG cắt nhau khi phương trình bậc hai này vô nghiệm thực, tức biệt thức \(\Delta < 0\): \([-(k + 2)]^2 - 4(3)(12) < 0 \Rightarrow (k + 2)^2 < 144\). Khai căn hai vế: \(-12 < k + 2 < 12 \Rightarrow -14 < k < 10\). Vì \(k\) là số nguyên nhỏ hơn ngặt \(10\), giá trị nguyên lớn nhất của \(k\) là \(9\).',
        key_takeaway=r'Với điều kiện "do NOT intersect" (\(\Delta < 0\) nghiêm ngặt), biên \(\Delta = 0\) ứng với tiếp xúc (CÓ 1 giao điểm), nên phải lùi xuống \(1\) đơn vị nguyên!',
        desmos_tip_vi=r'Gõ <code>y = 3x^2 - k x + 27</code> và <code>y = 2x + 15</code> kèm slider <b>k</b> (đặt bước nhảy step = 1). Tại \(k = 10\) hai đồ thị chạm nhau tại \((2, 19)\), còn tại \(k = 9\) hai đồ thị tách rời hoàn toàn \(\rightarrow\) chốt \(9\).',
        option_analysis={
            'A': ('Not Maximum Integer', r'Với \(k = 7\) hai đồ thị không cắt nhau, nhưng chưa phải số nguyên lớn nhất.'),
            'B': ('Over-Subtracted Shift', r'Trừ nhầm \(2\) hai lần hoặc lấy \(10 - 2 = 8\).'),
            'C': ('Correct', r'\(-14 < k < 10\) với \(k \in \mathbb{Z}\) cho giá trị lớn nhất là \(k = 9\) (\(\Delta = 11^2 - 144 = -23 < 0\)).'),
            'D': ('Boundary Tangency Trap', r'Bẫy 780 kinh điển: tại \(k = 10\), \(\Delta = 0\), đường thẳng TIẾP XÚC parabol tại \((2, 19)\) nên vẫn CÓ giao điểm!'),
        },
    ))

    # Q15 - Advanced Math - Very Hard (800) - D
    qs.append(math_mcq(
        qid='sat_mm2_m2h_q15',
        number=15,
        domain='Advanced Math',
        skill='Shifted exponential functions from data points',
        difficulty='Hard',
        stimulus_html=r'<p>The exponential function \(g(x) = a \cdot b^x + c\), where \(a\), \(b\), and \(c\) are positive constants with \(b > 1\), models a satellite amplifier response. The graph of \(y = g(x)\) passes through the points \((0, 11)\), \((1, 17)\), and \((2, 35)\).</p>',
        question_html=r'<p>What is the value of \(g(3)\)?</p>',
        options_dict={
            'A': r'\(53\)',
            'B': r'\(71\)',
            'C': r'\(81\)',
            'D': r'\(89\)',
        },
        correct_label='D',
        summary_vi=r'Thay 3 điểm vào \(g(x) = ab^x + c\): (1) \(a + c = 11\); (2) \(ab + c = 17\); (3) \(ab^2 + c = 35\). Lấy hiệu liên tiếp để triệt tiêu ngay hằng số tịnh tiến \(c\): \(\Delta_1 = g(1) - g(0) = a(b - 1) = 17 - 11 = 6\); \(\Delta_2 = g(2) - g(1) = ab(b - 1) = 35 - 17 = 18\). Chia \(\frac{\Delta_2}{\Delta_1} = \frac{ab(b - 1)}{a(b - 1)} = b = \frac{18}{6} = 3\). Từ đó \(a(3 - 1) = 6 \Rightarrow a = 3\), và \(c = 11 - 3 = 8\). Vậy \(g(x) = 3 \cdot 3^x + 8 \Rightarrow g(3) = 3(27) + 8 = 89\). (Cách siêu tốc 3 giây: hiệu kế tiếp tăng gấp \(b = 3\) lần nên \(\Delta_3 = 18 \times 3 = 54 \Rightarrow g(3) = 35 + 54 = 89\)!).',
        key_takeaway=r'Tuyệt chiêu 800 Math cho hàm \(a b^x + c\): các HIỆU LIÊN TIẾP \(g(x+1) - g(x)\) tạo thành một cấp số nhân có công bội đúng bằng cơ số \(b\)!',
        desmos_tip_vi=r'Nhập 3 điểm \((0, 11), (1, 17), (2, 35)\) vào <b>Table</b> của Desmos, gõ hồi quy <code>y1 ~ a * b^(x1) + c</code> để Desmos trả ngay \(a = 3, b = 3, c = 8\), rồi tính <code>3 * 3^3 + 8</code> ra \(89\).',
        option_analysis={
            'A': ('Linear Extrapolation Trap', r'Cộng đều hiệu gần nhất \(35 + 18 = 53\) như hàm bậc nhất thay vì nhân công bội \(3\).'),
            'B': ('Wrong Base Assumption', r'Giả định nhầm cơ số \(b = 2\) rồi cộng hiệu \(18 \times 2 = 36\) thành \(35 + 36 = 71\).'),
            'C': ('Omitted Vertical Shift c', r'Tính đúng \(3 \cdot 3^3 = 81\) nhưng quên cộng hằng số dịch chuyển \(c = 8\).'),
            'D': ('Correct', r'\(g(x) = 3 \cdot 3^x + 8 \Rightarrow g(3) = 81 + 8 = 89\).'),
        },
    ))

    # Q16 - PSDA - Hard - SPR
    qs.append(math_spr(
        qid='sat_mm2_m2h_q16',
        number=16,
        domain='Problem-Solving and Data Analysis',
        skill='Cubic unit conversions and density',
        difficulty='Hard',
        stimulus_html=r'<p>A prefabricated concrete girder for an urban high-speed rail viaduct has a volume of \(5.4\) cubic meters and a uniform density of \(2.4\) grams per cubic centimeter. (\(1\text{ meter} = 100\text{ centimeters}\); \(1\text{ kilogram} = 1{,}000\text{ grams}\); \(1\text{ metric ton} = 1{,}000\text{ kilograms}\)).</p>',
        question_html=r'<p>What is the mass of the concrete girder, in metric tons?</p>',
        accepted_answers=['12.96', '324/25'],
        correct_display='12.96 hoặc 324/25',
        summary_vi=r'Đổi thể tích từ \(\text{m}^3\) sang \(\text{cm}^3\): vì \(1\text{ m} = 100\text{ cm}\), nên \(1\text{ m}^3 = (100\text{ cm})^3 = 10^6\text{ cm}^3\). Vậy thể tích thanh dầm là \(5.4 \times 10^6\text{ cm}^3\). Khối lượng theo gam là: \(m = 2.4 \times 5.4 \times 10^6 = 12.96 \times 10^6\text{ g}\). Vì \(1\text{ tấn} = 1{,}000\text{ kg} = 10^6\text{ g}\), chia cho \(10^6\) ta thu được ngay \(m = 12.96\text{ metric tons}\) (tương đương phân số \(\frac{324}{25}\)).',
        key_takeaway=r'Mẹo vật lý tốc độ 800: \(1\text{ g/cm}^3\) bằng ĐÚNG \(1\text{ metric ton/m}^3\) (vì \(10^6\text{ cm}^3/\text{m}^3\) triệt tiêu trọn vẹn \(10^6\text{ g/tấn}\))!',
        desmos_tip_vi=r'Gõ nguyên chuỗi chuyển đổi đơn vị <code>5.4 * 100^3 * 2.4 / (1000 * 1000)</code> vào Desmos để tránh tuyệt đối lỗi thừa/thiếu chữ số \(0\), ra thẳng \(12.96\).',
    ))

    # Q17 - PSDA - Hard - A
    t17 = build_math_table(
        ['Acoustic Clarity Score', 'Hall X (Seats)', 'Hall Y (Seats)'],
        [
            ['10', '5', '2'],
            ['20', '3', '4'],
            ['30', '4', '8'],
            ['40', '3', '4'],
            ['50', '5', '2'],
        ],
        caption='Sound Clarity Scores Across 20 Measurement Seats in Two Concert Halls'
    )
    qs.append(math_mcq(
        qid='sat_mm2_m2h_q17',
        number=17,
        domain='Problem-Solving and Data Analysis',
        skill='Comparing means and standard deviations of distributions',
        difficulty='Hard',
        stimulus_html=rf'<p>Acoustic engineers measured sound clarity scores at \(20\) seat locations in Concert Hall X and \(20\) seat locations in Concert Hall Y, as summarized in the frequency table below.</p>{t17}',
        question_html=r'<p>Which of the following statements accurately compares the means and standard deviations of the two data sets?</p>',
        options_dict={
            'A': r'The means of the two data sets are equal, and the standard deviation of Hall X is greater than the standard deviation of Hall Y.',
            'B': r'The means of the two data sets are equal, and the standard deviation of Hall Y is greater than the standard deviation of Hall X.',
            'C': r'The mean of Hall X is greater than the mean of Hall Y, and the standard deviations of the two data sets are equal.',
            'D': r'The mean of Hall X is less than the mean of Hall Y, and the standard deviation of Hall X is greater than the standard deviation of Hall Y.',
        },
        correct_label='A',
        summary_vi=r'Quan sát tính đối xứng hoàn hảo quanh điểm giữa \(30\): ở Hall X tần số là \((5, 3, 4, 3, 5)\) và ở Hall Y là \((2, 4, 8, 4, 2)\), cả hai đều đối xứng gương qua \(30\) nên \(\text{Mean}_X = \text{Mean}_Y = 30\). Về độ lệch chuẩn (mức độ phân tán quanh giá trị trung bình \(30\)): Hall X có tới \(10\) giá trị dồn ra hai biên cực đại \(10\) và \(50\) (cách tâm \(20\) đơn vị), còn Hall Y tập trung chủ yếu ở tâm \(30\) (tới \(8\) giá trị). Do đó \(\text{SD}_X > \text{SD}_Y\) (chính xác: \(\text{SD}_X = \sqrt{230} \approx 15.17 > \text{SD}_Y = \sqrt{120} \approx 10.95\)).',
        key_takeaway=r'Không cần bấm máy tính: dữ liệu càng DỒN VỀ HAI BIÊN thì độ lệch chuẩn (SD) càng LỚN; dữ liệu càng TỤ Ở GIỮA thì SD càng NHỎ.',
        desmos_tip_vi=r'Nếu muốn kiểm chứng số tuyệt đối, nhập danh sách <code>X</code> và <code>Y</code> vào Desmos rồi gọi <code>stdevp(X)</code> (\(15.17\)) và <code>stdevp(Y)</code> (\(10.95\)).',
        option_analysis={
            'A': ('Correct', r'Hai phân phối cùng đối xứng tại \(30\) (bằng trung bình), nhưng Hall X phân tán mạnh về hai đầu \(10\) và \(50\) nên SD lớn hơn.'),
            'B': ('Peak Frequency Misconception', r'Bẫy kinh điển: nhầm tưởng cột tần số cao hơn ở giữa (\(8\) tại điểm \(30\)) đồng nghĩa độ lệch chuẩn lớn hơn — thực tế là NGƯỢC LẠI.'),
            'C': ('Mean & Spread Misread', r'Không nhận ra tính đối xứng quanh \(30\) khiến hai giá trị trung bình bằng nhau.'),
            'D': ('Mean Calculation Error', r'Kết luận sai rằng trung bình hai tập dữ liệu khác nhau.'),
        },
    ))

    # Q18 - PSDA - Very Hard (780) - B
    qs.append(math_mcq(
        qid='sat_mm2_m2h_q18',
        number=18,
        domain='Problem-Solving and Data Analysis',
        skill='Multi-step chained percentage relationships',
        difficulty='Hard',
        stimulus_html=r'<p>During an aerospace solar-panel endurance test, Array B generated \(35\%\) more electrical energy than Array A, and Array C generated \(20\%\) less electrical energy than Array B. Array C generated a total of \(216\) kilowatt-hours.</p>',
        question_html=r'<p>How many kilowatt-hours of electrical energy did Array A generate?</p>',
        options_dict={
            'A': r'\(180\)',
            'B': r'\(200\)',
            'C': r'\(240\)',
            'D': r'\(270\)',
        },
        correct_label='B',
        summary_vi=r'Dịch từng câu sang phương trình nhân: "Array B generated \(35\%\) more than Array A" \(\Rightarrow B = 1.35A\). "Array C generated \(20\%\) less than Array B" \(\Rightarrow C = 0.80B\). Thay \(B\) vào \(C\): \(C = 0.80(1.35A) = 1.08A\). Theo đề bài \(C = 216\), suy ra \(1.08A = 216 \Rightarrow A = \frac{216}{1.08} = 200\text{ kWh}\). Kiểm tra xuôi: \(A = 200 \rightarrow B = 270 \rightarrow C = 0.80(270) = 216\) (khớp 100%).',
        key_takeaway=r'Với bài toán phần trăm nối tiếp ngược (cho kết quả cuối tìm giá trị đầu), đặt biến \(A\), lập chuỗi nhân \(C = (1 + p_1)(1 - p_2)A\), rồi chia ngược chứ KHÔNG cộng/trừ phần trăm.',
        desmos_tip_vi=r'Gõ <code>216 / (1.35 * 0.80)</code> vào Desmos để nhận ngay đáp án chính xác \(200\).',
        option_analysis={
            'A': ('Wrong Reverse Multiplier', r'Nhân nhầm \(216\) với \(0.85\) hoặc chia sai bước ngược.'),
            'B': ('Correct', r'\(1.08A = 216 \Rightarrow A = 200\text{ kWh}\).'),
            'C': ('Additive Error', r'Ước lượng sai mức chênh lệch tích lũy giữa A và C.'),
            'D': ('Solved for Intermediate B', r'Bẫy dừng giữa chừng: \(270 = \frac{216}{0.80}\) là năng lượng của Array B, chưa chia tiếp cho \(1.35\) để ra Array A.'),
        },
    ))

    # Q19 - PSDA - Very Hard (800) - SPR
    t19 = build_math_table(
        ['Rail Corridor', 'Number of Surveyed Riders', 'Mean Commute Time (minutes)'],
        [
            ['North Corridor', '35', '26'],
            ['Central Corridor', '65', '34'],
            ['South Corridor', r'\(n\)', '46'],
        ],
        caption='Daily High-Speed Rail Commute Survey Across Three Corridors'
    )
    qs.append(math_spr(
        qid='sat_mm2_m2h_q19',
        number=19,
        domain='Problem-Solving and Data Analysis',
        skill='Weighted means with an unknown subgroup size',
        difficulty='Hard',
        stimulus_html=rf'<p>A regional transit authority surveyed high-speed rail commuters across three corridors, as shown in the table below. The overall mean commute time for all \(100 + n\) surveyed riders combined was \(36\) minutes.</p>{t19}',
        question_html=r'<p>What is the value of \(n\)?</p>',
        accepted_answers=['48'],
        correct_display='48',
        summary_vi=r'Tổng thời gian di chuyển của toàn bộ hành khách bằng tổng từng nhóm: \(\text{Total} = 35(26) + 65(34) + 46n = 910 + 2{,}210 + 46n = 3{,}120 + 46n\). Mặt khác, vì trung bình chung của \((100 + n)\) người là \(36\) phút nên \(\text{Total} = 36(100 + n) = 3{,}600 + 36n\). Cho hai biểu thức bằng nhau: \(3{,}120 + 46n = 3{,}600 + 36n \Rightarrow 10n = 480 \Rightarrow n = 48\). (Mẹo cân bằng độ lệch 800: North thiếu \(35 \times 10 = 350\), Central thiếu \(65 \times 2 = 130\), tổng thiếu \(480\); mỗi người ở South dư \(46 - 36 = 10\), nên cần \(n = \frac{480}{10} = 48\) người!).',
        key_takeaway=r'Mẹo cân bằng độ lệch (Balance Method) cho Weighted Mean: tổng phần thiếu dưới trung bình chung phải bằng đúng tổng phần dư trên trung bình chung!',
        desmos_tip_vi=r'Gõ <code>(35*26 + 65*34 + 46x) / (100 + x) = 36</code> vào Desmos để hiện ngay vạch đứng tại \(x = 48\).',
    ))

    # Q20 - Geometry & Trig - Hard (760) - D
    qs.append(math_mcq(
        qid='sat_mm2_m2h_q20',
        number=20,
        domain='Geometry and Trigonometry',
        skill='Circle equations — completing the square with a parameter',
        difficulty='Hard',
        stimulus_html=r'<p>In the \(xy\)-plane, a circle is defined by the equation below, where \(k\) is a constant:</p><p>\[x^2 + y^2 - 12x + 16y + k = 0\]</p>',
        question_html=r'<p>If the radius of this circle is \(9\), what is the value of \(k\)?</p>',
        options_dict={
            'A': r'\(-81\)',
            'B': r'\(-19\)',
            'C': r'\(11\)',
            'D': r'\(19\)',
        },
        correct_label='D',
        summary_vi=r'Nhóm các hạng tử theo \(x\) và \(y\) rồi hoàn thành bình phương: \((x^2 - 12x + 36) + (y^2 + 16y + 64) = -k + 36 + 64\). Thu gọn thành \((x - 6)^2 + (y + 8)^2 = 100 - k\). Vì bán kính \(r = 9\), vế phải phải bằng \(r^2 = 9^2 = 81\). Do đó \(100 - k = 81 \Rightarrow k = 19\).',
        key_takeaway=r'Công thức siêu tốc cho \(x^2 + y^2 + Dx + Ey + k = 0\): bán kính bình phương luôn bằng \(r^2 = \left(\frac{D}{2}\right)^2 + \left(\frac{E}{2}\right)^2 - k\).',
        desmos_tip_vi=r'Gõ <code>x^2 + y^2 - 12x + 16y + k = 0</code> kèm slider <b>k</b>, đặt \(k = 19\) rồi bấm đỉnh trên \((6, 1)\) và đáy dưới \((6, -17)\) để kiểm tra đường kính \(= 18 \Rightarrow r = 9\).',
        option_analysis={
            'A': ('Ignored Completing the Square', r'Nhầm \(k = -r^2 = -81\), quên cộng \(36 + 64 = 100\) khi hoàn thành bình phương.'),
            'B': ('Sign Error on k', r'Chuyển \(+k\) sang vế phải nhưng quên đổi dấu thành \(-k\), giải ra \(100 + k = 81 \Rightarrow k = -19\).'),
            'C': ('Forgot to Square Radius', r'Đặt nhầm \(100 - k = 9\) (dùng \(r\) thay vì \(r^2\)), hoặc sai phép tính \(100 - 81\) thành \(11\).'),
            'D': ('Correct', r'\(36 + 64 - k = 81 \Rightarrow k = 19\).'),
        },
    ))

    # Q21 - Geometry & Trig - Very Hard (790) - C
    svg21 = svg_circle_sector(
        radius_lbl='18 m',
        angle_lbl='θ',
        center_lbl='O',
        pt_a='A',
        pt_b='B',
        note='Note: Figure not drawn to scale.'
    )
    qs.append(math_mcq(
        qid='sat_mm2_m2h_q21',
        number=21,
        domain='Geometry and Trigonometry',
        skill='Arc length and sector area',
        difficulty='Hard',
        stimulus_html=rf'<p>The circular stage platform of an acoustic concert hall has center \(O\) and radius \(18\) meters, as shown below. The length of minor arc \(\widehat{{AB}}\) bounding the shaded acoustic sector \(AOB\) is \(15\pi\) meters.</p><div style="display:flex;justify-content:center;margin:12px 0;">{svg21}</div>',
        question_html=r'<p>What is the area, in square meters, of the <b>unshaded</b> region of the circular stage platform?</p>',
        options_dict={
            'A': r'\(135\pi\)',
            'B': r'\(162\pi\)',
            'C': r'\(189\pi\)',
            'D': r'\(270\pi\)',
        },
        correct_label='C',
        summary_vi=r'Tính chu vi và diện tích toàn hình tròn: \(C = 2\pi r = 2\pi(18) = 36\pi\text{ m}\), và \(A_{\text{total}} = \pi r^2 = \pi(18)^2 = 324\pi\text{ m}^2\). Tỉ lệ hình quạt tô đậm \(AOB\) so với cả hình tròn bằng tỉ lệ độ dài cung: \(\frac{15\pi}{36\pi} = \frac{5}{12}\). Do đó diện tích phần tô đậm là \(\frac{5}{12} \times 324\pi = 135\pi\text{ m}^2\) (hoặc dùng công thức nhanh \(A_{\text{sector}} = \frac{1}{2} r s = \frac{1}{2}(18)(15\pi) = 135\pi\)). Vì đề bài hỏi diện tích phần <b>KHÔNG tô đậm (unshaded)</b>, ta lấy phần bù: \(A_{\text{unshaded}} = 324\pi - 135\pi = 189\pi\text{ m}^2\).',
        key_takeaway=r'Công thức thần tốc cho hình quạt tròn khi biết bán kính \(r\) và cung \(s\): \(A_{\text{sector}} = \frac{1}{2}rs\). Và luôn đọc kỹ chữ "shaded" hay "unshaded"!',
        desmos_tip_vi=r'Gõ <code>18^2 - 0.5 * 18 * 15</code> vào Desmos để nhận ngay hệ số của \(\pi\) là \(189 \Rightarrow 189\pi\).',
        option_analysis={
            'A': ('Shaded Region Trap', r'Bẫy đọc lướt 790: \(135\pi\) là diện tích phần TÔ ĐẬM (shaded sector \(AOB\)), trong khi đề hỏi phần KHÔNG tô đậm!'),
            'B': ('Semicircle Guess', r'\(162\pi = \frac{1}{2}(324\pi)\) là diện tích nửa hình tròn, không khớp tỉ lệ cung \(\frac{15}{36}\).'),
            'C': ('Correct', r'\(324\pi - 135\pi = 189\pi\text{ m}^2\).'),
            'D': ('Forgot Factor of 1/2', r'Quên nhân \(\frac{1}{2}\) trong công thức \(\frac{1}{2}rs\), tính nhầm thành \(18 \times 15\pi = 270\pi\).'),
        },
    ))

    # Q22 - Geometry & Trig - Very Hard (800) - SPR
    svg22 = svg_cylinder(
        r_lbl='r',
        h_lbl='h',
        note='Reservoir P and Reservoir Q are geometrically similar.'
    )
    qs.append(math_spr(
        qid='sat_mm2_m2h_q22',
        number=22,
        domain='Geometry and Trigonometry',
        skill='Similar 3D solids — surface area and volume scaling',
        difficulty='Hard',
        stimulus_html=rf'<p>In an automated agricultural greenhouse complex, two right circular cylindrical water reservoirs, Reservoir P and Reservoir Q, are geometrically similar. The total surface area of Reservoir P is \(72\pi\) square meters, and the total surface area of Reservoir Q is \(162\pi\) square meters. The volume of Reservoir P is \(64\pi\) cubic meters.</p><div style="display:flex;justify-content:center;margin:12px 0;">{svg22}</div>',
        question_html=r'<p>If the volume of Reservoir Q is \(V\pi\) cubic meters, what is the value of \(V\)?</p>',
        accepted_answers=['216'],
        correct_display='216',
        summary_vi=r'Với hai khối hình học đồng dạng có tỉ số kích thước tuyến tính là \(k\): tỉ số diện tích toàn phần bằng \(k^2\) và tỉ số thể tích bằng \(k^3\). Ta có: \(k^2 = \frac{\text{TSA}_Q}{\text{TSA}_P} = \frac{162\pi}{72\pi} = \frac{9}{4}\). Khai căn tìm tỉ số độ dài: \(k = \sqrt{\frac{9}{4}} = \frac{3}{2}\). Suy ra tỉ số thể tích: \(k^3 = \left(\frac{3}{2}\right)^3 = \frac{27}{8}\). Do đó thể tích bể Q là \(V_Q = 64\pi \times \frac{27}{8} = 8 \times 27\pi = 216\pi\text{ m}^3\), suy ra \(V = 216\). (Kiểm chứng thực tế: bể P có \(r=2, h=16\) và bể Q có \(r=3, h=24\) thỏa mãn chính xác mọi thông số!).',
        key_takeaway=r'Bộ ba tỉ lệ đồng dạng 3D cho mốc 800 Math: Độ dài \(\propto k\), Diện tích \(\propto k^2\), Thể tích \(\propto k^3\). Từ diện tích sang thể tích luôn lấy mũ \(\frac{3}{2}\): \((k^2)^{3/2} = k^3\).',
        desmos_tip_vi=r'Gõ thẳng công thức lũy thừa <code>64 * (162 / 72)^(3/2)</code> vào Desmos để nhận ngay kết quả chính xác tuyệt đối \(216\).',
    ))

    return qs


if __name__ == '__main__':
    verify_math()
    qs = get_m2h_questions()
    print(f"M2 Hard verified OK: {len(qs)} questions.")
