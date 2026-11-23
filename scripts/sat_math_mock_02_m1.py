# -*- coding: utf-8 -*-
"""
Digital SAT Math Adaptive Mock Test #2 — Module 1 (Routing Module: 22 Questions)
Difficulty progression: Easy -> Medium -> Medium-Hard
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
    svg_right_triangle,
    svg_cylinder,
    svg_parabola_vertex,
)


def verify_math():
    """Programmatic exact verification of all 22 Module 1 answers."""
    # Q1: 3(2x - 5) + 8 = 29 => 4x + 3 = 27
    x1 = Fraction(29 - 8 + 15, 6)
    assert 3 * (2 * x1 - 5) + 8 == 29
    assert 4 * x1 + 3 == 27

    # Q2: E(t) = 480 - 32t -> slope = -32 (rate of decrease 32 Wh/min)
    assert 480 - 32 * 0 == 480 and (480 - 32 * 1) - 480 == -32

    # Q3: 17 + 6.5m <= 95 -> m <= 12
    assert Fraction(95 - 17, 1) / Fraction(13, 2) == 12

    # Q4: f(x) = -3x + 5 passes through (-2, 11), (1, 2), (4, -7)
    for xv, yv in [(-2, 11), (1, 2), (4, -7)]:
        assert -3 * xv + 5 == yv

    # Q5 (SPR): s + e = 85, 14s + 26e = 1586 -> e = 33
    e5 = Fraction(1586 - 14 * 85, 26 - 14)
    s5 = 85 - e5
    assert e5 == 33 and s5 == 52 and 14 * s5 + 26 * e5 == 1586

    # Q6: 3x + 4y = 20 -> perp slope 4/3 through (6, 5) -> y-intercept (0, -3)
    m_p = Fraction(-3, 4)
    m_q = Fraction(-1, 1) / m_p
    b_q = 5 - m_q * 6
    assert m_q == Fraction(4, 3) and b_q == -3

    # Q7: y > 2x - 3 and x + y <= 9 -> (2, 5) only valid option
    assert 5 > 2 * 2 - 3 and 2 + 5 <= 9
    assert not (5 > 2 * 4 - 3 and 4 + 5 <= 9)
    assert not (7 > 2 * 3 - 3 and 3 + 7 <= 9)
    assert not (4 > 2 * 5 - 3 and 5 + 4 <= 9)

    # Q8: kx - 6y = 14, 4x + 9y = 21 has no solution -> k = -8/3
    k8 = Fraction(4, 1) * Fraction(-6, 9)
    assert k8 == Fraction(-8, 3)
    assert Fraction(-6, 9) != Fraction(14, 21)

    # Q9 (SPR): g(x) = 2x^2 - 5x + 4 -> g(6) - g(2) = 44
    g9 = lambda x: 2 * x * x - 5 * x + 4
    assert g9(6) - g9(2) == 44

    # Q10: (2x - 3)(3x + 5) - (x^2 - 4x + 2) = 5x^2 + 5x - 17
    for xv in (-2, 0, 1, 5):
        lhs = (2 * xv - 3) * (3 * xv + 5) - (xv ** 2 - 4 * xv + 2)
        rhs = 5 * xv ** 2 + 5 * xv - 17
        assert lhs == rhs

    # Q11: P(t) = 1200 * 2^(t/4)
    assert 1200 * (2 ** (0 / 4)) == 1200
    assert 1200 * (2 ** (4 / 4)) == 2400
    assert 1200 * (2 ** (8 / 4)) == 4800

    # Q12: vertex (3, -8), passes through (5, 0) -> a = 2, f(0) = 10
    a12 = Fraction(0 - (-8), (5 - 3) ** 2)
    assert a12 == 2 and a12 * (0 - 3) ** 2 - 8 == 10

    # Q13 (SPR): sqrt(4x + 17) = x + 3 -> x = 2 (x = -4 extraneous)
    assert math.isqrt(4 * 2 + 17) == 2 + 3
    assert math.isqrt(4 * (-4) + 17) != -4 + 3

    # Q14: v = sqrt(mu / (r + h)) -> h = mu / v^2 - r
    mu, r, h = Fraction(100), Fraction(6), Fraction(19)
    v2 = mu / (r + h)
    assert mu / v2 - r == h

    # Q15: y = x^2 - 4x + 7 and y = 2x + k have 1 solution -> k = -2
    k15 = -2
    disc15 = (-6) ** 2 - 4 * 1 * (7 - k15)
    assert disc15 == 0

    # Q16 (SPR): 180 km in 40 min -> 270 km/h
    assert Fraction(180, 1) / Fraction(40, 60) == 270

    # Q17: P(Alpha | Positive) = 54 / 80 = 27/40
    assert Fraction(54, 80) == Fraction(27, 40)

    # Q18: +30% then -20% -> 1.30 * 0.80 = 1.04 (+4%)
    assert Fraction(130, 100) * Fraction(80, 100) == Fraction(104, 100)

    # Q19 (SPR): Ratings 3(7), 5(5), 9(4), 14(4) -> n=20, mean=6.9, median=5, diff=1.9
    vals19 = [3] * 7 + [5] * 5 + [9] * 4 + [14] * 4
    mean19 = Fraction(sum(vals19), len(vals19))
    med19 = Fraction(vals19[9] + vals19[10], 2)
    assert mean19 == Fraction(69, 10) and med19 == 5
    assert mean19 - med19 == Fraction(19, 10)

    # Q20: Right triangle AB=15, BC=36 -> AC=39, sin(C) = 15/39 = 5/13
    ac20 = math.isqrt(15 ** 2 + 36 ** 2)
    assert ac20 == 39 and Fraction(15, ac20) == Fraction(5, 13)

    # Q21: (x - 4)^2 + (y + 7)^2 = 144 -> center (4, -7), radius 12
    assert math.isqrt(144) == 12

    # Q22 (SPR): pi * r^2 * 12 = 300 * pi -> r = 5, diameter = 10
    r22 = math.isqrt(300 // 12)
    assert r22 == 5 and 2 * r22 == 10
    return True


def get_m1_questions():
    qs = []

    # Q1 - Algebra - Easy - B
    qs.append(math_mcq(
        qid='sat_mm2_m1_q1',
        number=1,
        domain='Algebra',
        skill='Linear equations in one variable',
        difficulty='Easy',
        stimulus_html=r'<p>\[3(2x - 5) + 8 = 29\]</p>',
        question_html=r'<p>If \(x\) satisfies the equation above, what is the value of \(4x + 3\)?</p>',
        options_dict={
            'A': r'\(6\)',
            'B': r'\(27\)',
            'C': r'\(15\)',
            'D': r'\(31\)',
        },
        correct_label='B',
        summary_vi=r'Trừ \(8\) ở cả hai vế: \(3(2x - 5) = 21\). Chia cả hai vế cho \(3\): \(2x - 5 = 7 \Rightarrow 2x = 12 \Rightarrow x = 6\). Đề bài hỏi giá trị của \(4x + 3\), nên thay \(x = 6\) vào ta được \(4(6) + 3 = 27\).',
        key_takeaway=r'Luôn gạch chân biểu thức đề bài hỏi ở cuối câu (\(4x + 3\), không phải \(x\)) trước khi khoanh đáp án.',
        desmos_tip_vi=r'Gõ thẳng <code>3(2x - 5) + 8 = 29</code> vào Desmos để thấy đường đứng tại \(x = 6\), sau đó gõ dòng hai <code>4(6) + 3</code> ra ngay \(27\).',
        option_analysis={
            'A': ('Asked Wrong Variable', r'Đây chỉ là giá trị của \(x = 6\), học sinh quên bước cuối tính \(4x + 3\).'),
            'B': ('Correct', r'Tìm được \(x = 6\) chính xác rồi thay vào \(4(6) + 3 = 27\).'),
            'C': ('Expression Misread', r'Tính nhầm \(2x + 3 = 15\) thay vì \(4x + 3\).'),
            'D': ('Arithmetic Sign Error', r'Giải sai thành \(2x = 14 \Rightarrow x = 7\), dẫn tới \(4(7) + 3 = 31\).'),
        },
    ))

    # Q2 - Algebra - Easy - D
    qs.append(math_mcq(
        qid='sat_mm2_m1_q2',
        number=2,
        domain='Algebra',
        skill='Linear functions in context',
        difficulty='Easy',
        stimulus_html=r'<p>During an orbital eclipse, the stored battery energy \(E(t)\), in watt-hours, of a research nanosatellite \(t\) minutes after entering Earth’s shadow is modeled by the function:</p><p>\[E(t) = 480 - 32t\]</p>',
        question_html=r'<p>Which of the following is the best interpretation of the number \(32\) in this context?</p>',
        options_dict={
            'A': r'The nanosatellite’s stored battery energy, in watt-hours, at the moment it enters Earth’s shadow.',
            'B': r'The total number of minutes the nanosatellite can operate before its battery is completely depleted.',
            'C': r'The remaining battery energy, in watt-hours, after \(32\) minutes in Earth’s shadow.',
            'D': r'The rate, in watt-hours per minute, at which the nanosatellite’s stored battery energy decreases during the eclipse.',
        },
        correct_label='D',
        summary_vi=r'Trong hàm bậc nhất \(E(t) = b + mt\) với \(b = 480\) và hệ số góc \(m = -32\), hằng số \(480\) là mức năng lượng ban đầu (khi \(t = 0\)), còn \(-32\) là tốc độ thay đổi theo mỗi phút \(t\). Vì mang dấu trừ, số \(32\) biểu diễn tốc độ giảm năng lượng pin là \(32\) watt-hours mỗi phút.',
        key_takeaway=r'Hệ số nhân với biến thời gian \(t\) trong mô hình tuyến tính luôn là tốc độ thay đổi (rate of change per unit time).',
        desmos_tip_vi=r'Không cần vẽ đồ thị; nếu muốn kiểm chứng, lập bảng giá trị \(E(0)=480\), \(E(1)=448\), \(E(2)=416\) sẽ thấy cứ tăng \(1\) phút thì năng lượng giảm đúng \(32\) watt-hours.',
        option_analysis={
            'A': ('Y-Intercept Confusion', r'Năng lượng ban đầu khi vào vùng tối là \(480\) watt-hours, không phải \(32\).'),
            'B': ('X-Intercept Confusion', r'Thời gian cạn pin là nghiệm \(480 - 32t = 0 \Rightarrow t = 15\) phút, không phải \(32\).'),
            'C': ('Variable Swap', r'Nhầm hệ số tốc độ \(32\) với giá trị thời gian \(t = 32\) phút.'),
            'D': ('Correct', r'Hệ số \(-32\) đi kèm biến \(t\) thể hiện tốc độ giảm \(32\) watt-hours trên mỗi phút.'),
        },
    ))

    # Q3 - Algebra - Easy - A
    qs.append(math_mcq(
        qid='sat_mm2_m1_q3',
        number=3,
        domain='Algebra',
        skill='Linear inequalities in one variable',
        difficulty='Easy',
        stimulus_html=r'<p>In an automated vertical greenhouse, a hydroponic growing tray can safely support a total mass of at most \(95\) kilograms. The empty aluminum tray frame has a mass of \(17\) kilograms, and each nutrient pod placed on the tray has a mass of \(6.5\) kilograms.</p>',
        question_html=r'<p>Which inequality represents all possible numbers of nutrient pods, \(m\), that can be safely placed on the tray?</p>',
        options_dict={
            'A': r'\(17 + 6.5m \le 95\)',
            'B': r'\(17 + 6.5m \ge 95\)',
            'C': r'\(17m + 6.5 \le 95\)',
            'D': r'\(6.5m - 17 \le 95\)',
        },
        correct_label='A',
        summary_vi=r'Tổng khối lượng trên khay gồm khối lượng cố định của khung nhôm (\(17\text{ kg}\)) cộng với khối lượng của \(m\) hộp dinh dưỡng (\(6.5m\text{ kg}\)). Cụm từ "at most \(95\) kilograms" (nhiều nhất là \(95\text{ kg}\)) tương ứng với dấu \(\le 95\). Do đó bất phương trình đúng là \(17 + 6.5m \le 95\).',
        key_takeaway=r'"At most" dịch chuẩn sang toán học là \(\le\) (nhỏ hơn hoặc bằng); "at least" là \(\ge\).',
        desmos_tip_vi=r'Bạn có thể kiểm tra nhanh bằng cách thử \(m = 0\) (khay rỗng nặng \(17\text{ kg}\) phải thỏa mãn bất phương trình) — chỉ có A, C, D thỏa, sau đó thử \(m = 1\) nặng \(23.5\text{ kg}\) để chốt A.',
        option_analysis={
            'A': ('Correct', r'Khối lượng cố định \(17\) cộng \(6.5m\) không vượt quá (\(\le\)) giới hạn \(95\).'),
            'B': ('Inequality Flip', r'Đảo ngược dấu thành \(\ge\) (biểu thị "ít nhất \(95\)" thay vì "nhiều nhất \(95\)").'),
            'C': ('Coefficient Swap', r'Gắn nhầm biến \(m\) vào khối lượng cố định \(17\) của khung nhôm.'),
            'D': ('Sign Error', r'Trừ khối lượng khung \(17\) thay vì cộng dồn vào tổng tải trọng.'),
        },
    ))

    # Q4 - Algebra - Medium - C
    t4 = build_math_table(
        [r'\(x\)', r'\(f(x)\)'],
        [[r'\(-2\)', r'\(11\)'], [r'\(1\)', r'\(2\)'], [r'\(4\)', r'\(-7\)']],
        caption='Biomedical Incubator Calibration Values'
    )
    qs.append(math_mcq(
        qid='sat_mm2_m1_q4',
        number=4,
        domain='Algebra',
        skill='Linear functions from tables',
        difficulty='Medium',
        stimulus_html=rf'<p>The table below gives three values of \(x\) and their corresponding values of \(f(x)\) for a linear function \(f\) used to calibrate a biomedical lab incubator.</p>{t4}',
        question_html=r'<p>Which equation defines the linear function \(f\)?</p>',
        options_dict={
            'A': r'\(f(x) = -3x - 5\)',
            'B': r'\(f(x) = 3x + 5\)',
            'C': r'\(f(x) = -3x + 5\)',
            'D': r'\(f(x) = -\frac{1}{3}x + 5\)',
        },
        correct_label='C',
        summary_vi=r'Tính hệ số góc từ hai điểm \((-2, 11)\) và \((1, 2)\): \(m = \frac{2 - 11}{1 - (-2)} = \frac{-9}{3} = -3\). Thay điểm \((1, 2)\) vào dạng \(f(x) = -3x + b\): \(2 = -3(1) + b \Rightarrow b = 5\). Kiểm tra điểm thứ ba: \(f(4) = -3(4) + 5 = -7\) (khớp hoàn toàn).',
        key_takeaway=r'Khi tính hệ số góc có tọa độ âm, luôn đóng mở ngoặc: \(1 - (-2) = 3\) để tránh sai dấu.',
        desmos_tip_vi=r'Bấm dấu <code>+</code> \(\rightarrow\) <b>Table</b>, nhập 3 điểm \((-2, 11), (1, 2), (4, -7)\), rồi gõ dòng dưới <code>y1 ~ m x1 + b</code> \(\rightarrow\) Desmos trả ngay \(m = -3, b = 5\).',
        option_analysis={
            'A': ('Intercept Sign Error', r'Tính đúng hệ số góc \(m = -3\) nhưng tìm nhầm tung độ gốc là \(-5\).'),
            'B': ('Slope Sign Error', r'Quên dấu trừ ở hệ số góc; khi \(x\) tăng thì \(f(x)\) giảm nên \(m < 0\).'),
            'C': ('Correct', r'Thỏa mãn cả 3 cặp giá trị trong bảng: \(f(-2)=11, f(1)=2, f(4)=-7\).'),
            'D': ('Reciprocal Slope Trap', r'Tính ngược công thức hệ số góc thành \(\frac{\Delta x}{\Delta y} = -\frac{1}{3}\).'),
        },
    ))

    # Q5 - Algebra - Medium - SPR
    qs.append(math_spr(
        qid='sat_mm2_m1_q5',
        number=5,
        domain='Algebra',
        skill='Systems of linear equations in context',
        difficulty='Medium',
        stimulus_html=r'<p>An urban high-speed rail line sells Standard commuter passes for $14 each and Executive passes for $26 each. On a morning departure, a total of \(85\) passes were sold, generating $1,586 in ticket revenue.</p>',
        question_html=r'<p>How many Executive passes were sold on that morning departure?</p>',
        accepted_answers=['33'],
        correct_display='33',
        summary_vi=r'Gọi \(s\) là số vé Standard và \(e\) là số vé Executive. Ta có hệ phương trình: \(s + e = 85\) và \(14s + 26e = 1586\). Thế \(s = 85 - e\) vào phương trình thứ hai: \(14(85 - e) + 26e = 1586 \Rightarrow 1190 + 12e = 1586 \Rightarrow 12e = 396 \Rightarrow e = 33\). Kiểm tra: \(52(14) + 33(26) = 728 + 858 = 1586\).',
        key_takeaway=r'Với bài toán hệ phương trình hỏi 1 ẩn cụ thể (\(e\)), rút ẩn còn lại (\(s = 85 - e\)) để giải trực tiếp ra ngay đáp số cần tìm.',
        desmos_tip_vi=r'Gõ hai dòng <code>x + y = 85</code> và <code>14x + 26y = 1586</code> (với \(y\) là số vé Executive), bấm vào giao điểm \((52, 33)\) và đọc tung độ \(y = 33\).',
    ))

    # Q6 - Algebra - Medium - B
    qs.append(math_mcq(
        qid='sat_mm2_m1_q6',
        number=6,
        domain='Algebra',
        skill='Perpendicular lines in the xy-plane',
        difficulty='Medium',
        stimulus_html=r'<p>In the \(xy\)-plane, line \(p\) is defined by the equation \(3x + 4y = 20\). Line \(q\) is perpendicular to line \(p\) and passes through the point \((6, 5)\).</p>',
        question_html=r'<p>What is the \(y\)-intercept of line \(q\)?</p>',
        options_dict={
            'A': r'\((0, -8)\)',
            'B': r'\((0, -3)\)',
            'C': r'\((0, 3)\)',
            'D': r'\((0, 5)\)',
        },
        correct_label='B',
        summary_vi=r'Đưa đường thẳng \(p\) về dạng \(y = mx + b\): \(4y = -3x + 20 \Rightarrow y = -\frac{3}{4}x + 5\), nên \(m_p = -\frac{3}{4}\). Vì \(q \perp p\), hệ số góc của \(q\) là nghịch đảo đối dấu: \(m_q = \frac{4}{3}\). Đường thẳng \(q\) đi qua \((6, 5)\): \(5 = \frac{4}{3}(6) + b \Rightarrow 5 = 8 + b \Rightarrow b = -3\). Vậy giao điểm trục tung là \((0, -3)\).',
        key_takeaway=r'Hai đường thẳng vuông góc có tích hệ số góc bằng \(-1\) (\(m_q = -\frac{1}{m_p}\)), tức vừa đảo phân số vừa đổi dấu.',
        desmos_tip_vi=r'Gõ <code>y = (4/3)(x - 6) + 5</code> vào Desmos và bấm vào giao điểm với trục tung để đọc trực tiếp \((0, -3)\).',
        option_analysis={
            'A': ('Incomplete Substitution', r'Tính đúng \(\frac{4}{3}(6) = 8\) rồi lấy \(-8\) mà quên cộng \(+5\) từ tung độ điểm \((6, 5)\).'),
            'B': ('Correct', r'Hệ số góc \(m_q = \frac{4}{3}\) đi qua \((6, 5)\) cho phương trình \(y = \frac{4}{3}x - 3\), cắt \(Oy\) tại \((0, -3)\).'),
            'C': ('Sign Error', r'Chuyển vế nhầm \(b = 8 - 5 = 3\) thay vì \(b = 5 - 8 = -3\).'),
            'D': ('Same Y-Intercept Trap', r'Nhầm lẫn tung độ của điểm đi qua \((6, 5)\) hoặc tung độ gốc của đường thẳng \(p\) (\(b_p = 5\)) với đáp án.'),
        },
    ))

    # Q7 - Algebra - Medium - A
    qs.append(math_mcq(
        qid='sat_mm2_m1_q7',
        number=7,
        domain='Algebra',
        skill='Systems of linear inequalities',
        difficulty='Medium',
        stimulus_html=r'<p>\[y > 2x - 3\]\[x + y \le 9\]</p>',
        question_html=r'<p>Which of the following ordered pairs \((x, y)\) is a solution to the system of inequalities above?</p>',
        options_dict={
            'A': r'\((2, 5)\)',
            'B': r'\((4, 5)\)',
            'C': r'\((3, 7)\)',
            'D': r'\((5, 4)\)',
        },
        correct_label='A',
        summary_vi=r'Thử từng điểm vào cả hai bất phương trình. Với \((2, 5)\): bất phương trình 1 cho \(5 > 2(2) - 3 = 1\) (Đúng); bất phương trình 2 cho \(2 + 5 = 7 \le 9\) (Đúng). Điểm \((4, 5)\) làm vế 1 thành \(5 > 5\) (Sai vì dấu lớn hơn ngặt \(>\)).',
        key_takeaway=r'Cảnh giác tuyệt đối với ranh giới dấu ngặt (\(>\) hoặc \(<\)): giá trị làm hai vế bằng nhau KHÔNG phải là nghiệm.',
        desmos_tip_vi=r'Gõ cả hai bất phương trình và 4 điểm <code>(2,5)</code>, <code>(4,5)</code>, <code>(3,7)</code>, <code>(5,4)</code> vào Desmos: điểm duy nhất nằm trọn trong vùng giao tô đậm (không nằm trên đường nét đứt) là \((2, 5)\).',
        option_analysis={
            'A': ('Correct', r'Thỏa mãn đồng thời \(5 > 1\) và \(7 \le 9\).'),
            'B': ('Strict Boundary Trap', r'Thay \((4, 5)\) vào \(y > 2x - 3\) được \(5 > 5\) (sai vì không có dấu bằng).'),
            'C': ('Second Constraint Violation', r'Thỏa \(7 > 3\) nhưng vi phạm điều kiện thứ hai vì \(3 + 7 = 10 > 9\).'),
            'D': ('First Constraint Violation', r'Thỏa \(5 + 4 = 9 \le 9\) nhưng vi phạm điều kiện đầu vì \(4 < 2(5) - 3 = 7\).'),
        },
    ))

    # Q8 - Algebra - Medium-Hard - D
    qs.append(math_mcq(
        qid='sat_mm2_m1_q8',
        number=8,
        domain='Algebra',
        skill='Systems of linear equations with no solution',
        difficulty='Hard',
        stimulus_html=r'<p>\[kx - 6y = 14\]\[4x + 9y = 21\]</p>',
        question_html=r'<p>In the system of equations above, \(k\) is a constant. If the system has no solution, what is the value of \(k\)?</p>',
        options_dict={
            'A': r'\(-\frac{27}{2}\)',
            'B': r'\(\frac{8}{3}\)',
            'C': r'\(-6\)',
            'D': r'\(-\frac{8}{3}\)',
        },
        correct_label='D',
        summary_vi=r'Hệ hai phương trình tuyến tính vô nghiệm khi hai đường thẳng song song nhưng không trùng nhau, tức tỉ lệ hệ số \(x\) bằng tỉ lệ hệ số \(y\) và khác tỉ lệ hằng số: \(\frac{k}{4} = \frac{-6}{9} \ne \frac{14}{21}\). Rút gọn \(\frac{-6}{9} = -\frac{2}{3}\), kiểm tra \(\frac{14}{21} = \frac{2}{3} \ne -\frac{2}{3}\) (đảm bảo vô nghiệm). Từ đó \(k = 4 \cdot \left(-\frac{2}{3}\right) = -\frac{8}{3}\).',
        key_takeaway=r'Hệ \(a_1x + b_1y = c_1\) và \(a_2x + b_2y = c_2\) vô nghiệm \(\Leftrightarrow \frac{a_1}{a_2} = \frac{b_1}{b_2} \ne \frac{c_1}{c_2}\).',
        desmos_tip_vi=r'Gõ hai phương trình vào Desmos, bấm <b>Add slider: k</b> rồi kéo hoặc nhập thử 4 đáp án — tại \(k = -8/3\), hai đường thẳng song song hoàn toàn và không cắt nhau.',
        option_analysis={
            'A': ('Inverted Ratio', r'Đảo ngược tỉ lệ thành \(\frac{k}{9} = \frac{-6}{4} \Rightarrow k = -\frac{27}{2}\).'),
            'B': ('Sign Error', r'Quên dấu âm của \(-6y\), tính thành \(k = 4 \cdot \frac{6}{9} = \frac{8}{3}\).'),
            'C': ('Cross-Term Confusion', r'Gán trực tiếp \(k = -6\) bằng hệ số của \(y\) mà không xét tỉ lệ.'),
            'D': ('Correct', r'\(\frac{-8/3}{4} = -\frac{2}{3} = \frac{-6}{9} \ne \frac{14}{21}\), hệ vô nghiệm chuẩn xác.'),
        },
    ))

    # Q9 - Advanced Math - Easy - SPR
    qs.append(math_spr(
        qid='sat_mm2_m1_q9',
        number=9,
        domain='Advanced Math',
        skill='Evaluating nonlinear functions',
        difficulty='Easy',
        stimulus_html=r'<p>The acoustic gain function \(g\) is defined by:</p><p>\[g(x) = 2x^2 - 5x + 4\]</p>',
        question_html=r'<p>What is the value of \(g(6) - g(2)\)?</p>',
        accepted_answers=['44'],
        correct_display='44',
        summary_vi=r'Tính từng giá trị hàm số: \(g(6) = 2(6)^2 - 5(6) + 4 = 72 - 30 + 4 = 46\); \(g(2) = 2(2)^2 - 5(2) + 4 = 8 - 10 + 4 = 2\). Hiệu cần tìm là \(g(6) - g(2) = 46 - 2 = 44\).',
        key_takeaway=r'Cẩn thận lỗi kinh điển: \(g(6) - g(2) \ne g(6 - 2) = g(4)\) vì \(g\) là hàm bậc hai (phi tuyến), không phải hàm tuyến tính qua gốc tọa độ.',
        desmos_tip_vi=r'Gõ <code>g(x) = 2x^2 - 5x + 4</code> ở dòng 1, gõ <code>g(6) - g(2)</code> ở dòng 2 để Desmos tính tức thì ra \(44\).',
    ))

    # Q10 - Advanced Math - Medium - C
    qs.append(math_mcq(
        qid='sat_mm2_m1_q10',
        number=10,
        domain='Advanced Math',
        skill='Equivalent polynomial expressions',
        difficulty='Medium',
        stimulus_html=r'<p>\[(2x - 3)(3x + 5) - (x^2 - 4x + 2)\]</p>',
        question_html=r'<p>Which of the following expressions is equivalent to the expression above?</p>',
        options_dict={
            'A': r'\(5x^2 - 3x - 17\)',
            'B': r'\(5x^2 + 5x - 13\)',
            'C': r'\(5x^2 + 5x - 17\)',
            'D': r'\(7x^2 + 5x - 17\)',
        },
        correct_label='C',
        summary_vi=r'Khai triển tích thứ nhất: \((2x - 3)(3x + 5) = 6x^2 + 10x - 9x - 15 = 6x^2 + x - 15\). Phá ngoặc dấu trừ ở cụm thứ hai (đổi dấu toàn bộ các hạng tử bên trong): \(-x^2 + 4x - 2\). Cộng gộp các hạng tử đồng dạng: \((6x^2 - x^2) + (x + 4x) + (-15 - 2) = 5x^2 + 5x - 17\).',
        key_takeaway=r'Dấu trừ đứng trước dấu ngoặc phải phân phối đổi dấu cho TẤT CẢ các hạng tử bên trong ngoặc.',
        desmos_tip_vi=r'Gõ biểu thức đề bài thành <code>f(x) = ...</code> và từng đáp án thành <code>g(x) = ...</code> (hoặc thử tại \(x = 1\): đề bài \(= -8 - (-1) = -7\), kiểm tra \(5 + 5 - 17 = -7\)).',
        option_analysis={
            'A': ('Distribution Sign Error', r'Quên đổi dấu \(-4x\) thành \(+4x\) khi phá ngoặc trừ, tính thành \(x - 4x = -3x\).'),
            'B': ('Constant Sign Error', r'Quên đổi dấu \(+2\) thành \(-2\) khi phá ngoặc trừ, tính thành \(-15 + 2 = -13\).'),
            'C': ('Correct', r'Khai triển và thu gọn chuẩn xác: \(5x^2 + 5x - 17\).'),
            'D': ('Leading Term Addition', r'Cộng \(6x^2 + x^2 = 7x^2\) thay vì trừ \(6x^2 - x^2 = 5x^2\).'),
        },
    ))

    # Q11 - Advanced Math - Medium - A
    qs.append(math_mcq(
        qid='sat_mm2_m1_q11',
        number=11,
        domain='Advanced Math',
        skill='Exponential growth modeling',
        difficulty='Medium',
        stimulus_html=r'<p>In a biomedical laboratory, a bacterial cell culture begins with \(1{,}200\) cells. Under optimal incubator conditions, the number of cells doubles every \(4\) hours.</p>',
        question_html=r'<p>Which equation models the number of cells \(P(t)\) in the culture \(t\) hours after the observation begins?</p>',
        options_dict={
            'A': r'\(P(t) = 1{,}200(2)^{\frac{t}{4}}\)',
            'B': r'\(P(t) = 1{,}200(2)^{4t}\)',
            'C': r'\(P(t) = 1{,}200(4)^{\frac{t}{2}}\)',
            'D': r'\(P(t) = 1{,}200(1.25)^{t}\)',
        },
        correct_label='A',
        summary_vi=r'Hàm mũ tăng trưởng có dạng \(P(t) = P_0 \cdot r^{t/d}\), trong đó giá trị ban đầu \(P_0 = 1{,}200\), hệ số nhân gấp đôi \(r = 2\), và chu kỳ gấp đôi là \(d = 4\) giờ. Do đó \(P(t) = 1{,}200(2)^{\frac{t}{4}}\). Thử tại \(t = 4\): \(P(4) = 1{,}200 \cdot 2^1 = 2{,}400\) (đúng gấp đôi).',
        key_takeaway=r'Với bài toán hàm mũ, luôn kiểm chứng nhanh bằng cách thế \(t = \text{chu kỳ}\) (ở đây \(t = 4\)): số mũ phải bằng \(1\).',
        desmos_tip_vi=r'Thế \(t = 4\) vào 4 phương án: chỉ có A cho ra \(1200 \cdot 2^{4/4} = 2400\) (gấp đôi lượng ban đầu).',
        option_analysis={
            'A': ('Correct', r'Khi \(t = 4\), \(P(4) = 1{,}200 \cdot 2^1 = 2{,}400\), khớp chuẩn chu kỳ gấp đôi mỗi \(4\) giờ.'),
            'B': ('Exponent Multiplication Trap', r'Đặt số mũ là \(4t\) khiến sau \(4\) giờ số tế bào nhân lên \(2^{16}\) lần.'),
            'C': ('Base-Period Swap', r'Tráo đổi cơ số \(2\) và chu kỳ \(4\); khi \(t = 4\) cho \(4^2 = 16\) lần thay vì \(2\) lần.'),
            'D': ('Linear-Rate Misconception', r'Chia đều mức tăng \(100\%\) cho \(4\) giờ thành \(25\%\)/giờ — sai vì tăng trưởng mũ có lãi kép (\(1.25^4 \approx 2.44 \ne 2\)).'),
        },
    ))

    # Q12 - Advanced Math - Medium - D
    svg12 = svg_parabola_vertex(
        h_lbl='3',
        k_lbl='-8',
        opens_up=True,
        pt_lbl='(5, 0)',
        note='Note: Figure not drawn to scale.'
    )
    qs.append(math_mcq(
        qid='sat_mm2_m1_q12',
        number=12,
        domain='Advanced Math',
        skill='Quadratic functions in vertex form',
        difficulty='Medium',
        stimulus_html=rf'<p>The graph of the quadratic function \(y = f(x)\) in the \(xy\)-plane is shown below, with vertex \((3, -8)\) and passing through the point \((5, 0)\).</p><div style="display:flex;justify-content:center;margin:12px 0;">{svg12}</div>',
        question_html=r'<p>What is the \(y\)-intercept of the graph of \(y = f(x)\)?</p>',
        options_dict={
            'A': r'\((0, -8)\)',
            'B': r'\((0, 1)\)',
            'C': r'\((0, 6)\)',
            'D': r'\((0, 10)\)',
        },
        correct_label='D',
        summary_vi=r'Viết phương trình parabol theo dạng đỉnh: \(f(x) = a(x - 3)^2 - 8\). Vì đồ thị đi qua \((5, 0)\), thay \(x = 5, y = 0\): \(0 = a(5 - 3)^2 - 8 \Rightarrow 4a = 8 \Rightarrow a = 2\). Vậy \(f(x) = 2(x - 3)^2 - 8\). Giao điểm trục tung ứng với \(x = 0\): \(f(0) = 2(0 - 3)^2 - 8 = 18 - 8 = 10\), tức \((0, 10)\).',
        key_takeaway=r'Đừng bao giờ mặc định hệ số đầu \(a = 1\) khi viết parabol dạng đỉnh — luôn dùng điểm thứ hai đề cho để giải tìm \(a\).',
        desmos_tip_vi=r'Gõ <code>f(x) = a(x - 3)^2 - 8</code> kèm <b>Add slider: a</b>, chỉnh \(a = 2\) để đường cong đi qua \((5, 0)\) rồi bấm vào chấm xám trên trục \(Oy\) để thấy \((0, 10)\).',
        option_analysis={
            'A': ('Vertex Y-Value Trap', r'Nhầm tung độ đỉnh \(-8\) với tung độ gốc \(f(0)\).'),
            'B': ('Assumed a = 1 Trap', r'Mặc định sai \(a = 1\), tính thành \((0 - 3)^2 - 8 = 1\).'),
            'C': ('Arithmetic Error', r'Tính sai \((0 - 3)^2\) hoặc trừ nhầm \(18 - 12 = 6\).'),
            'D': ('Correct', r'Tìm đúng \(a = 2\) và thay \(x = 0\) thu được \(f(0) = 2(9) - 8 = 10\).'),
        },
    ))

    # Q13 - Advanced Math - Medium-Hard - SPR
    qs.append(math_spr(
        qid='sat_mm2_m1_q13',
        number=13,
        domain='Advanced Math',
        skill='Radical equations and extraneous solutions',
        difficulty='Hard',
        stimulus_html=r'<p>\[\sqrt{4x + 17} = x + 3\]</p>',
        question_html=r'<p>What is the real solution to the equation above?</p>',
        accepted_answers=['2'],
        correct_display='2',
        summary_vi=r'Điều kiện để căn thức có nghĩa và vế phải không âm: \(x + 3 \ge 0 \Rightarrow x \ge -3\). Bình phương hai vế: \(4x + 17 = (x + 3)^2 = x^2 + 6x + 9 \Rightarrow x^2 + 2x - 8 = 0 \Rightarrow (x + 4)(x - 2) = 0\). Ta thu được \(x = 2\) hoặc \(x = -4\). Thử lại vào phương trình gốc: với \(x = 2\), \(\sqrt{25} = 5 = 2 + 3\) (thỏa mãn); với \(x = -4\), \(\sqrt{1} = 1 \ne -1\) (nghiệm ngoại lai, loại). Vậy nghiệm duy nhất là \(x = 2\).',
        key_takeaway=r'Bất kỳ khi nào bình phương hai vế phương trình chứa căn thức, BẮT BUỘC thử lại nghiệm vào phương trình gốc để loại nghiệm ngoại lai.',
        desmos_tip_vi=r'Gõ <code>y = sqrt(4x + 17)</code> và <code>y = x + 3</code> vào Desmos: hai đồ thị chỉ cắt nhau tại ĐÚNG 1 điểm \((2, 5)\), loại bỏ hoàn toàn nguy cơ dính bẫy nghiệm ngoại lai \(x = -4\).',
    ))

    # Q14 - Advanced Math - Medium-Hard - B
    qs.append(math_mcq(
        qid='sat_mm2_m1_q14',
        number=14,
        domain='Advanced Math',
        skill='Isolating a quantity in a nonlinear formula',
        difficulty='Hard',
        stimulus_html=r'<p>The circular orbital speed \(v\) of a communications satellite at altitude \(h\) above a planet of radius \(r\) is given by the equation below, where \(\mu\) is the planet’s gravitational parameter and \(v, \mu, r, h > 0\):</p><p>\[v = \sqrt{\frac{\mu}{r + h}}\]</p>',
        question_html=r'<p>Which of the following equations correctly expresses \(h\) in terms of \(v\), \(\mu\), and \(r\)?</p>',
        options_dict={
            'A': r'\(h = \frac{\mu - r}{v^2}\)',
            'B': r'\(h = \frac{\mu}{v^2} - r\)',
            'C': r'\(h = \frac{\mu}{v} - r\)',
            'D': r'\(h = \frac{v^2}{\mu} - r\)',
        },
        correct_label='B',
        summary_vi=r'Bình phương hai vế để khử căn bậc hai: \(v^2 = \frac{\mu}{r + h}\). Nhân chéo \(r + h\) và chia cho \(v^2\): \(r + h = \frac{\mu}{v^2}\). Trừ \(r\) ở cả hai vế: \(h = \frac{\mu}{v^2} - r\).',
        key_takeaway=r'Với bài toán rút ẩn (literal equations), luôn xử lý từ lớp ngoài vào trong: bình phương khử căn \(\rightarrow\) khử mẫu số \(\rightarrow\) tách phép cộng/trừ cuối cùng.',
        desmos_tip_vi=r'Chọn bộ số thử đẹp: \(r = 1, h = 3, \mu = 16 \Rightarrow v = \sqrt{16/4} = 2\). Thay \(v=2, \mu=16, r=1\) vào 4 đáp án: chỉ B cho \(16/4 - 1 = 3 = h\).',
        option_analysis={
            'A': ('Fraction Scope Error', r'Đưa nhầm \(-r\) lên trên tử số chung với \(\mu\) trước khi chia cho \(v^2\).'),
            'B': ('Correct', r'Biến đổi đúng theo thứ tự: \(v^2 = \frac{\mu}{r+h} \Rightarrow r+h = \frac{\mu}{v^2} \Rightarrow h = \frac{\mu}{v^2} - r\).'),
            'C': ('Forgot Squaring', r'Bỏ căn bậc hai ở vế phải nhưng quên bình phương \(v\) thành \(v^2\) ở vế trái.'),
            'D': ('Reciprocal Inversion Error', r'Đảo ngược phân số \(\frac{\mu}{v^2}\) thành \(\frac{v^2}{\mu}\).'),
        },
    ))

    # Q15 - Advanced Math - Hard - C
    qs.append(math_mcq(
        qid='sat_mm2_m1_q15',
        number=15,
        domain='Advanced Math',
        skill='Nonlinear systems and the discriminant',
        difficulty='Hard',
        stimulus_html=r'<p>\[y = x^2 - 4x + 7\]\[y = 2x + k\]</p>',
        question_html=r'<p>In the system of equations above, \(k\) is a constant. If the system has exactly one real solution, what is the value of \(k\)?</p>',
        options_dict={
            'A': r'\(-9\)',
            'B': r'\(-4\)',
            'C': r'\(-2\)',
            'D': r'\(2\)',
        },
        correct_label='C',
        summary_vi=r'Cho hai vế phải bằng nhau để tìm phương trình hoành độ giao điểm: \(x^2 - 4x + 7 = 2x + k \Rightarrow x^2 - 6x + (7 - k) = 0\). Hệ có đúng 1 nghiệm thực khi biệt thức \(\Delta = b^2 - 4ac = 0\): \((-6)^2 - 4(1)(7 - k) = 0 \Rightarrow 36 - 28 + 4k = 0 \Rightarrow 8 + 4k = 0 \Rightarrow k = -2\).',
        key_takeaway=r'Đường thẳng tiếp xúc parabol (đúng 1 nghiệm) luôn quy về điều kiện biệt thức \(\Delta = b^2 - 4ac = 0\).',
        desmos_tip_vi=r'Gõ <code>y = x^2 - 4x + 7</code> và <code>y = 2x + k</code> vào Desmos, thêm thanh trượt <b>k</b> và kéo tới khi đường thẳng vừa chạm (tiếp xúc) parabol tại đúng 1 điểm \((3, 4)\) khi \(k = -2\).',
        option_analysis={
            'A': ('Constant Omission', r'Quên hạng tử \(+7\) trong phương trình parabol, giải nhầm \(36 + 4k = 0 \Rightarrow k = -9\).'),
            'B': ('Term Shift Error', r'Nhầm \(b = -2\) thay vì \(-6\) khi chuyển \(2x\) sang vế trái.'),
            'C': ('Correct', r'Với \(k = -2\), phương trình trở thành \(x^2 - 6x + 9 = (x - 3)^2 = 0\) có nghiệm kép duy nhất \(x = 3\).'),
            'D': ('Sign Error', r'Sai dấu khi phá ngoặc \(-4(7 - k)\) thành \(-28 - 4k = 0 \Rightarrow k = 2\).'),
        },
    ))

    # Q16 - PSDA - Easy-Medium - SPR
    qs.append(math_spr(
        qid='sat_mm2_m1_q16',
        number=16,
        domain='Problem-Solving and Data Analysis',
        skill='Rates and unit conversions',
        difficulty='Easy',
        stimulus_html=r'<p>During an express intercity test run, a high-speed maglev train travels a distance of \(180\) kilometers in \(40\) minutes.</p>',
        question_html=r'<p>What is the train’s average speed, in kilometers per hour, during this test run?</p>',
        accepted_answers=['270'],
        correct_display='270',
        summary_vi=r'Đổi \(40\) phút sang giờ: \(40\text{ phút} = \frac{40}{60}\text{ giờ} = \frac{2}{3}\text{ giờ}\). Vận tốc trung bình bằng quãng đường chia thời gian: \(v = \frac{180}{2/3} = 180 \times \frac{3}{2} = 270\text{ km/h}\).',
        key_takeaway=r'Kiểm tra đơn vị câu hỏi (km/giờ vs km/phút) trước khi chia: muốn đổi phút sang giờ phải chia cho \(60\).',
        desmos_tip_vi=r'Gõ trực tiếp phân số <code>180 / (40/60)</code> vào Desmos để nhận ngay kết quả \(270\) mà không lo nhầm lẫn nghịch đảo.',
    ))

    # Q17 - PSDA - Medium - D
    t17 = build_math_table(
        ['Cell Strain', 'Positive Assay', 'Negative Assay', 'Total'],
        [
            ['Strain Alpha', '54', '36', '90'],
            ['Strain Beta', '26', '124', '150'],
            ['<b>Total</b>', '<b>80</b>', '<b>160</b>', '<b>240</b>'],
        ],
        caption='Biomedical Diagnostic Assay Results (240 Lab Samples)'
    )
    qs.append(math_mcq(
        qid='sat_mm2_m1_q17',
        number=17,
        domain='Problem-Solving and Data Analysis',
        skill='Two-way tables and conditional probability',
        difficulty='Medium',
        stimulus_html=rf'<p>The table below summarizes the results of a diagnostic fluorescence assay performed on \(240\) lab cell culture samples.</p>{t17}',
        question_html=r'<p>If one sample that tested positive is selected at random, what is the probability that the selected sample is from Strain Alpha?</p>',
        options_dict={
            'A': r'\(\frac{9}{40}\)',
            'B': r'\(\frac{3}{8}\)',
            'C': r'\(\frac{3}{5}\)',
            'D': r'\(\frac{27}{40}\)',
        },
        correct_label='D',
        summary_vi=r'Cụm điều kiện "If one sample that tested positive is selected at random" thu hẹp không gian mẫu (mẫu số) xuống CHỈ cột Positive Assay, gồm \(80\) mẫu. Trong \(80\) mẫu dương tính này, có \(54\) mẫu thuộc Strain Alpha. Vậy xác suất là \(\frac{54}{80} = \frac{27}{40}\).',
        key_takeaway=r'Trong xác suất có điều kiện từ bảng 2 chiều, mệnh đề "If a [Nhóm X] is selected..." luôn quy định mẫu số là tổng của riêng Nhóm X.',
        desmos_tip_vi=r'Gõ <code>54/80</code> vào Desmos rồi nhấn biểu tượng phân số ở đầu dòng để rút gọn ngay thành \(\frac{27}{40}\).',
        option_analysis={
            'A': ('Total Sample Space Trap', r'Chia nhầm cho tổng toàn bộ \(240\) mẫu: \(\frac{54}{240} = \frac{9}{40}\).'),
            'B': ('Marginal Probability Trap', r'Tính tỉ lệ chung của Strain Alpha là \(\frac{90}{240} = \frac{3}{8}\).'),
            'C': ('Reversed Conditional Trap', r'Đảo ngược điều kiện thành \(P(\text{Positive} \mid \text{Alpha}) = \frac{54}{90} = \frac{3}{5}\).'),
            'D': ('Correct', r'\(P(\text{Alpha} \mid \text{Positive}) = \frac{54}{80} = \frac{27}{40}\).'),
        },
    ))

    # Q18 - PSDA - Medium - A
    qs.append(math_mcq(
        qid='sat_mm2_m1_q18',
        number=18,
        domain='Problem-Solving and Data Analysis',
        skill='Successive percentage change',
        difficulty='Medium',
        stimulus_html=r'<p>After installing automated LED spectrum controls, an agricultural greenhouse increased its annual tomato harvest by \(30\%\) in Year 1 compared to the baseline year. In Year 2, due to a cooling failure, the harvest decreased by \(20\%\) compared to Year 1.</p>',
        question_html=r'<p>Compared to the baseline year, the Year 2 tomato harvest was:</p>',
        options_dict={
            'A': r'\(4\%\) greater',
            'B': r'\(10\%\) greater',
            'C': r'\(4\%\) less',
            'D': r'\(6\%\) less',
        },
        correct_label='A',
        summary_vi=r'Gọi sản lượng gốc (baseline) là \(100\). Sau Year 1 tăng \(30\%\): \(100 \times 1.30 = 130\). Sang Year 2 giảm \(20\%\) so với Year 1: \(130 \times 0.80 = 104\). So với mức gốc \(100\), sản lượng Year 2 cao hơn \(104 - 100 = 4\), tức tăng \(4\%\).',
        key_takeaway=r'Không bao giờ cộng trừ thẳng hai phần trăm liên tiếp — luôn nhân các hệ số biến đổi \((1 + p_1)(1 - p_2)\).',
        desmos_tip_vi=r'Gõ thẳng <code>1.30 * 0.80</code> ra \(1.04\), đọc ngay phần vượt quá \(1\) là \(+0.04 = +4\%\).',
        option_analysis={
            'A': ('Correct', r'\(1.30 \times 0.80 = 1.04\), tức lớn hơn \(4\%\) so với năm gốc.'),
            'B': ('Additive Percent Trap', r'Bẫy cộng trừ thô \(+30\% - 20\% = +10\%\), quên rằng mức giảm \(20\%\) tính trên nền \(130\%\) đã tăng.'),
            'C': ('Direction Confusion', r'Tính đúng độ lệch \(4\%\) nhưng đọc nhầm thành giảm \(4\%\).'),
            'D': ('Product of Percents Trap', r'Nhân thẳng \(30\% \times 20\% = 6\%\) rồi kết luận sai là giảm \(6\%\).'),
        },
    ))

    # Q19 - PSDA - Medium-Hard - SPR
    t19 = build_math_table(
        ['Acoustic Clarity Rating', 'Number of Panels'],
        [['3', '7'], ['5', '5'], ['9', '4'], ['14', '4']],
        caption='Acoustic Panel Clarity Ratings (20 Concert Hall Panels)'
    )
    qs.append(math_spr(
        qid='sat_mm2_m1_q19',
        number=19,
        domain='Problem-Solving and Data Analysis',
        skill='Mean and median from frequency tables',
        difficulty='Hard',
        stimulus_html=rf'<p>The frequency table below summarizes the acoustic clarity ratings of \(20\) wall panels tested in a concert hall.</p>{t19}',
        question_html=r'<p>How much greater is the mean rating than the median rating for these \(20\) panels? (Express your answer as a decimal or fraction.)</p>',
        accepted_answers=['1.9', '19/10'],
        correct_display='1.9 hoặc 19/10',
        summary_vi=r'Tổng số tấm là \(7 + 5 + 4 + 4 = 20\). Tổng điểm: \(3(7) + 5(5) + 9(4) + 14(4) = 21 + 25 + 36 + 56 = 138\), nên trung bình \(\text{Mean} = \frac{138}{20} = 6.9\). Vì có \(20\) giá trị (số chẵn), trung vị là trung bình cộng của giá trị thứ \(10\) và thứ \(11\) khi xếp tăng dần: vị trí \(1\text{–}7\) mang điểm \(3\), vị trí \(8\text{–}12\) mang điểm \(5\), nên cả hai vị trí \(10, 11\) đều bằng \(5 \Rightarrow \text{Median} = 5\). Hiệu cần tìm là \(6.9 - 5 = 1.9\) (hay \(\frac{19}{10}\)).',
        key_takeaway=r'Khi tìm trung vị từ bảng tần số, luôn cộng dồn tần số để xác định chính xác vị trí \(\frac{n}{2}\) và \(\frac{n}{2} + 1\) (khi \(n\) chẵn) chứ không lấy trung vị của 4 mức điểm thô.',
        desmos_tip_vi=r'Trong Desmos, gõ <code>L = [3,3,3,3,3,3,3,5,5,5,5,5,9,9,9,9,14,14,14,14]</code> rồi gõ <code>mean(L) - median(L)</code> để nhận ngay \(1.9\).',
    ))

    # Q20 - Geometry & Trig - Medium - B
    svg20 = svg_right_triangle(
        a_lbl='15',
        b_lbl='36',
        c_lbl='',
        v_top='A',
        v_right_angle='B',
        v_right='C',
        note='Note: Figure not drawn to scale.'
    )
    qs.append(math_mcq(
        qid='sat_mm2_m1_q20',
        number=20,
        domain='Geometry and Trigonometry',
        skill='Right triangle trigonometry',
        difficulty='Medium',
        stimulus_html=rf'<p>In the right triangle \(ABC\) shown below, representing a stage lighting truss in a concert hall, \(\angle B = 90^\circ\), \(AB = 15\) feet, and \(BC = 36\) feet.</p><div style="display:flex;justify-content:center;margin:12px 0;">{svg20}</div>',
        question_html=r'<p>What is the value of \(\sin C\)?</p>',
        options_dict={
            'A': r'\(\frac{5}{12}\)',
            'B': r'\(\frac{5}{13}\)',
            'C': r'\(\frac{12}{13}\)',
            'D': r'\(\frac{13}{5}\)',
        },
        correct_label='B',
        summary_vi=r'Áp dụng định lý Pythagore cho tam giác vuông \(ABC\): \(AC = \sqrt{15^2 + 36^2} = \sqrt{225 + 1296} = \sqrt{1521} = 39\) (nhận diện nhanh bộ ba Pythagore \(5\text{–}12\text{–}13\) nhân \(3\)). Theo SOH-CAH-TOA, cạnh đối góc \(C\) là \(AB = 15\) và cạnh huyền là \(AC = 39\), nên \(\sin C = \frac{15}{39} = \frac{5}{13}\).',
        key_takeaway=r'Thuộc lòng các bộ ba Pythagore kinh điển (\(3\text{–}4\text{–}5\), \(5\text{–}12\text{–}13\), \(8\text{–}15\text{–}17\), \(7\text{–}24\text{–}25\)) giúp tìm cạnh huyền trong 2 giây.',
        desmos_tip_vi=r'Gõ <code>15 / sqrt(15^2 + 36^2)</code> vào Desmos rồi nhấn nút chuyển đổi phân số ở đầu dòng để hiện ngay \(\frac{5}{13}\).',
        option_analysis={
            'A': ('Tangent Confusion', r'Tính \(\frac{15}{36} = \frac{5}{12}\), đây là \(\tan C\) (đối/kề) chứ không phải \(\sin C\).'),
            'B': ('Correct', r'\(\sin C = \frac{AB}{AC} = \frac{15}{39} = \frac{5}{13}\).'),
            'C': ('Cosine Confusion', r'Tính \(\frac{36}{39} = \frac{12}{13}\), đây là \(\cos C\) (kề/huyền) hay \(\sin A\).'),
            'D': ('Reciprocal Ratio Trap', r'Lấy ngược huyền/đối thành \(\frac{39}{15} = \frac{13}{5}\) (đây là \(\csc C\)).'),
        },
    ))

    # Q21 - Geometry & Trig - Medium - C
    qs.append(math_mcq(
        qid='sat_mm2_m1_q21',
        number=21,
        domain='Geometry and Trigonometry',
        skill='Circle equations in standard form',
        difficulty='Medium',
        stimulus_html=r'<p>In a regional coordinate map, the circular reception zone of a satellite ground station is modeled by the equation:</p><p>\[(x - 4)^2 + (y + 7)^2 = 144\]</p>',
        question_html=r'<p>What are the coordinates of the center and the radius of this circular reception zone?</p>',
        options_dict={
            'A': r'Center \((-4, 7)\), radius \(12\)',
            'B': r'Center \((4, -7)\), radius \(144\)',
            'C': r'Center \((4, -7)\), radius \(12\)',
            'D': r'Center \((-4, 7)\), radius \(72\)',
        },
        correct_label='C',
        summary_vi=r'So sánh với phương trình chuẩn đường tròn \((x - h)^2 + (y - k)^2 = r^2\): ta có \(h = 4\), \(k = -7\) (vì \(y + 7 = y - (-7)\)), và \(r^2 = 144 \Rightarrow r = \sqrt{144} = 12\). Do đó tâm là \((4, -7)\) và bán kính là \(12\).',
        key_takeaway=r'Tâm đường tròn \((h, k)\) luôn ĐỔI DẤU so với hai con số trong ngoặc, và bán kính \(r\) là CĂN BẬC HAI của vế phải.',
        desmos_tip_vi=r'Gõ thẳng <code>(x - 4)^2 + (y + 7)^2 = 144</code> vào Desmos để nhìn ngay tâm nằm ở góc phần tư IV tại \((4, -7)\) với đường kính \(24 \Rightarrow r = 12\).',
        option_analysis={
            'A': ('Center Sign Flip', r'Quên đổi dấu tọa độ tâm bên trong dấu ngoặc, đọc nhầm thành \((-4, 7)\).'),
            'B': ('Forgot Square Root', r'Lấy luôn vế phải \(r^2 = 144\) làm bán kính thay vì khai căn thành \(12\).'),
            'C': ('Correct', r'Tâm \((4, -7)\) và bán kính \(r = \sqrt{144} = 12\).'),
            'D': ('Halved Instead of Root', r'Vừa sai dấu tọa độ tâm, vừa chia đôi \(144\) thành \(72\) thay vì lấy căn bậc hai.'),
        },
    ))

    # Q22 - Geometry & Trig - Medium-Hard - SPR
    svg22 = svg_cylinder(
        r_lbl='r',
        h_lbl='12 m',
        note='Note: Figure not drawn to scale.'
    )
    qs.append(math_spr(
        qid='sat_mm2_m1_q22',
        number=22,
        domain='Geometry and Trigonometry',
        skill='Volume of a right circular cylinder',
        difficulty='Hard',
        stimulus_html=rf'<p>A right circular cylindrical hydroponic nutrient reservoir in an automated greenhouse has a height of \(12\) meters and a volume of \(300\pi\) cubic meters, as shown below.</p><div style="display:flex;justify-content:center;margin:12px 0;">{svg22}</div>',
        question_html=r'<p>What is the <b>diameter</b>, in meters, of the circular base of the reservoir?</p>',
        accepted_answers=['10'],
        correct_display='10',
        summary_vi=r'Công thức thể tích hình trụ: \(V = \pi r^2 h\). Thay \(V = 300\pi\) và \(h = 12\): \(300\pi = \pi r^2 (12) \Rightarrow r^2 = \frac{300}{12} = 25 \Rightarrow r = 5\text{ m}\). Vì đề bài hỏi <b>đường kính (diameter)</b> của đáy nên \(d = 2r = 2(5) = 10\text{ m}\).',
        key_takeaway=r'Bẫy kinh điển của hình học tròn/trụ trên SAT: giải ra bán kính \(r\) nhưng câu hỏi lại yêu cầu ĐƯỜNG KÍNH \(d = 2r\).',
        desmos_tip_vi=r'Gõ <code>pi * x^2 * 12 = 300 * pi</code> trên Desmos để thấy nghiệm dương \(x = 5\), rồi nhân đôi thành \(10\).',
    ))

    return qs


if __name__ == '__main__':
    verify_math()
    qs = get_m1_questions()
    print(f"M1 verified OK: {len(qs)} questions.")
