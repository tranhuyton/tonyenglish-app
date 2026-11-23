# -*- coding: utf-8 -*-
"""
Digital SAT Math Adaptive Mock Test #2 — Module 2 Standard/Lower (300–600 Band: 22 Questions)
Foundation-to-Medium routing track with clear scaffolds and core Bluebook skills.
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
    svg_parabola_vertex,
    svg_parallel_transversal,
    svg_similar_triangles,
    svg_right_triangle,
)


def verify_math():
    """Programmatic exact verification of all 22 Module 2 Lower answers."""
    # Q1: 5x - 9 = 26 -> x = 7
    assert 5 * 7 - 9 == 26

    # Q2: T(h) = 1.5h + 16 -> T(6) = 25
    assert Fraction(3, 2) * 6 + 16 == 25

    # Q3: slope through (2, 5) and (6, 17) = 3
    assert Fraction(17 - 5, 6 - 2) == 3

    # Q4: 45 + 2.50t = 80 -> t = 14
    assert 45 + Fraction(5, 2) * 14 == 80

    # Q5 (SPR): y = 3x, x + y = 32 -> x = 8, y = 24
    x5 = Fraction(32, 4)
    y5 = 3 * x5
    assert x5 == 8 and y5 == 24 and x5 + y5 == 32

    # Q6: 20 + 15n >= 110 -> n >= 6
    assert 20 + 15 * 6 == 110 and 20 + 15 * 5 < 110

    # Q7: parallel to y = -2x + 7 through (0, -4) -> y = -2x - 4
    assert -2 * 0 - 4 == -4

    # Q8: 2x + y = 29 and 3x - y = 16 -> 5x = 45 -> x = 9, y = 11
    x8 = Fraction(29 + 16, 5)
    y8 = 29 - 2 * x8
    assert x8 == 9 and y8 == 11 and 3 * x8 - y8 == 16

    # Q9 (SPR): 2^x * 2^5 = 2^14 -> x = 9
    assert (2 ** 9) * (2 ** 5) == 2 ** 14

    # Q10: (4x^2 + 3x - 5) + (2x^2 - 7x + 9) = 6x^2 - 4x + 4
    for xv in (-3, 0, 2, 5):
        assert (4 * xv ** 2 + 3 * xv - 5) + (2 * xv ** 2 - 7 * xv + 9) == 6 * xv ** 2 - 4 * xv + 4

    # Q11: x^2 - 7x + 12 = 0 -> x = 3 and x = 4
    for r in (3, 4):
        assert r ** 2 - 7 * r + 12 == 0

    # Q12: N(t) = 350(1.4)^t -> N(0) = 350
    assert 350 * (Fraction(14, 10) ** 0) == 350

    # Q13 (SPR): h(t) = -2(t - 4)^2 + 35 -> max = 35 at t = 4
    assert -2 * (4 - 4) ** 2 + 35 == 35

    # Q14: A = 2w^2 + 6h -> h = (A - 2w^2)/6
    w14, h14 = Fraction(3), Fraction(5)
    a14 = 2 * w14 ** 2 + 6 * h14
    assert (a14 - 2 * w14 ** 2) / 6 == h14

    # Q15: S(d) = 800 * (0.5)^d -> S(4) = 50
    assert 800 * (Fraction(1, 2) ** 4) == 50

    # Q16 (SPR): 28% of 450 = 126
    assert Fraction(28, 100) * 450 == 126

    # Q17: 48 / 150 = 8/25 (72 + 48 + 30 = 150)
    assert 72 + 48 + 30 == 150 and Fraction(48, 150) == Fraction(8, 25)

    # Q18: mean of [18, 22, 24, 26, 35] = 25
    vals18 = [18, 22, 24, 26, 35]
    assert Fraction(sum(vals18), len(vals18)) == 25

    # Q19 (SPR): 18 liters in 12 min -> in 50 min = 75 liters
    assert Fraction(18, 12) * 50 == 75

    # Q20: parallel lines corresponding angles: 2x + 10 = 124 -> x = 57
    assert 2 * 57 + 10 == 124

    # Q21: similar triangles AB=6, BC=10, DE=15, EF=x -> x = 25
    assert Fraction(15, 6) * 10 == 25

    # Q22 (SPR): right triangle AB=9, BC=12 -> AC=15, perimeter = 36
    ac22 = math.isqrt(9 ** 2 + 12 ** 2)
    assert ac22 == 15 and 9 + 12 + ac22 == 36
    return True


def get_m2l_questions():
    qs = []

    # Q1 - Algebra - Easy - A
    qs.append(math_mcq(
        qid='sat_mm2_m2l_q1',
        number=1,
        domain='Algebra',
        skill='Linear equations in one variable',
        difficulty='Easy',
        stimulus_html=r'<p>\[5x - 9 = 26\]</p>',
        question_html=r'<p>What value of \(x\) is the solution to the equation above?</p>',
        options_dict={
            'A': r'\(7\)',
            'B': r'\(3.4\)',
            'C': r'\(17\)',
            'D': r'\(35\)',
        },
        correct_label='A',
        summary_vi=r'Cộng \(9\) vào cả hai vế: \(5x = 26 + 9 = 35\). Chia cả hai vế cho \(5\): \(x = \frac{35}{5} = 7\). Kiểm tra lại: \(5(7) - 9 = 35 - 9 = 26\) (đúng).',
        key_takeaway=r'Chuyển hằng số âm sang vế kia thì đổi dấu thành cộng (\(-9 \rightarrow +9\)), rồi mới chia hệ số đứng trước \(x\).',
        desmos_tip_vi=r'Gõ trực tiếp <code>5x - 9 = 26</code> vào Desmos để thấy đường thẳng đứng đi qua \(x = 7\).',
        option_analysis={
            'A': ('Correct', r'\(5(7) - 9 = 35 - 9 = 26\).'),
            'B': ('Sign Error', r'Trừ nhầm \(26 - 9 = 17\) rồi chia \(5\) ra \(3.4\).'),
            'C': ('Sign & Incomplete Step', r'Trừ \(26 - 9 = 17\) và quên chia cho \(5\).'),
            'D': ('Forgot Division', r'Cộng đúng \(26 + 9 = 35\) nhưng dừng ở \(5x = 35\) mà chưa chia cho \(5\).'),
        },
    ))

    # Q2 - Algebra - Easy - C
    qs.append(math_mcq(
        qid='sat_mm2_m2l_q2',
        number=2,
        domain='Algebra',
        skill='Evaluating linear functions in context',
        difficulty='Easy',
        stimulus_html=r'<p>The temperature \(T(h)\), in degrees Celsius, inside an automated agricultural greenhouse \(h\) hours after sunrise is modeled by:</p><p>\[T(h) = 1.5h + 16\]</p>',
        question_html=r'<p>According to the model, what is the temperature inside the greenhouse \(6\) hours after sunrise?</p>',
        options_dict={
            'A': r'\(17.5^\circ\text{C}\)',
            'B': r'\(22^\circ\text{C}\)',
            'C': r'\(25^\circ\text{C}\)',
            'D': r'\(28^\circ\text{C}\)',
        },
        correct_label='C',
        summary_vi=r'Thay \(h = 6\) vào công thức hàm số: \(T(6) = 1.5(6) + 16 = 9 + 16 = 25^\circ\text{C}\).',
        key_takeaway=r'Với bài toán cho sẵn hàm \(T(h)\) và giá trị \(h = 6\), chỉ cần thế trực tiếp vào công thức và thực hiện nhân trước, cộng sau.',
        desmos_tip_vi=r'Gõ <code>1.5 * 6 + 16</code> vào máy tính Desmos để đọc kết quả \(25\).',
        option_analysis={
            'A': ('Evaluated at h = 1', r'Tính nhầm \(T(1) = 1.5 + 16 = 17.5\) thay vì thay \(h = 6\).'),
            'B': ('Ignored Coefficient 1.5', r'Cộng thẳng \(6 + 16 = 22\) mà quên nhân \(6\) với \(1.5\).'),
            'C': ('Correct', r'\(1.5(6) + 16 = 9 + 16 = 25^\circ\text{C}\).'),
            'D': ('Multiplication Error', r'Nhân nhầm \(1.5 \times 6 = 12\) rồi cộng \(16\) thành \(28\).'),
        },
    ))

    # Q3 - Algebra - Easy - B
    qs.append(math_mcq(
        qid='sat_mm2_m2l_q3',
        number=3,
        domain='Algebra',
        skill='Slope of a line from two points',
        difficulty='Easy',
        stimulus_html=r'<p>In the \(xy\)-plane, a line passes through the points \((2, 5)\) and \((6, 17)\).</p>',
        question_html=r'<p>What is the slope of this line?</p>',
        options_dict={
            'A': r'\(\frac{1}{3}\)',
            'B': r'\(3\)',
            'C': r'\(4\)',
            'D': r'\(12\)',
        },
        correct_label='B',
        summary_vi=r'Áp dụng công thức tính hệ số góc qua hai điểm \((x_1, y_1)\) và \((x_2, y_2)\): \(m = \frac{y_2 - y_1}{x_2 - x_1} = \frac{17 - 5}{6 - 2} = \frac{12}{4} = 3\).',
        key_takeaway=r'Hệ số góc luôn là "Rise over Run" = \(\frac{\Delta y}{\Delta x}\) (hiệu tung độ ở trên, hiệu hoành độ ở dưới).',
        desmos_tip_vi=r'Gõ trực tiếp <code>(17 - 5) / (6 - 2)</code> vào Desmos để nhận ngay \(3\).',
        option_analysis={
            'A': ('Inverted Slope Formula', r'Tính ngược thành \(\frac{x_2 - x_1}{y_2 - y_1} = \frac{4}{12} = \frac{1}{3}\).'),
            'B': ('Correct', r'\(m = \frac{17 - 5}{6 - 2} = \frac{12}{4} = 3\).'),
            'C': ('Delta X Only', r'Đây chỉ là hiệu hoành độ \(6 - 2 = 4\).'),
            'D': ('Delta Y Only', r'Đây chỉ là hiệu tung độ \(17 - 5 = 12\), quên chia cho \(4\).'),
        },
    ))

    # Q4 - Algebra - Easy - D
    qs.append(math_mcq(
        qid='sat_mm2_m2l_q4',
        number=4,
        domain='Algebra',
        skill='Linear equation modeling from context',
        difficulty='Easy',
        stimulus_html=r'<p>An urban high-speed rail commuter pays a fixed monthly pass fee of $45 plus $2.50 for each express trip taken during the month. In one month, the commuter spent a total of $80 on the pass and \(t\) express trips.</p>',
        question_html=r'<p>Which equation represents this situation?</p>',
        options_dict={
            'A': r'\(45t + 2.50 = 80\)',
            'B': r'\(47.50t = 80\)',
            'C': r'\(2.50t - 45 = 80\)',
            'D': r'\(45 + 2.50t = 80\)',
        },
        correct_label='D',
        summary_vi=r'Tổng chi phí gồm phí cố định trả một lần ($45) cộng với chi phí thay đổi theo số chuyến đi ($2.50 nhân \(t\) chuyến). Tổng cộng bằng $80, nên phương trình đúng là \(45 + 2.50t = 80\).',
        key_takeaway=r'Phân biệt rõ "fixed fee" (hằng số đứng độc lập, không nhân biến) và "per trip" (tốc độ biến thiên, LUÔN nhân với biến \(t\)).',
        desmos_tip_vi=r'Thử kiểm chứng với \(t = 1\) chuyến: tổng tiền phải là \(45 + 2.50 = 47.50\) đô-la — chỉ có vế trái của D cho đúng \(47.50\).',
        option_analysis={
            'A': ('Swapped Fixed & Variable', r'Nhân nhầm biến \(t\) vào phí cố định $45 thay vì phí mỗi chuyến $2.50.'),
            'B': ('Combined Unlike Terms', r'Cộng gộp phí cố định $45 vào đơn giá mỗi chuyến thành $47.50t.'),
            'C': ('Sign Error', r'Trừ phí cố định $45 thay vì cộng vào tổng chi phí.'),
            'D': ('Correct', r'Phí cố định $45 cộng \(2.50t\) cho \(t\) chuyến bằng tổng $80.'),
        },
    ))

    # Q5 - Algebra - Easy - SPR
    qs.append(math_spr(
        qid='sat_mm2_m2l_q5',
        number=5,
        domain='Algebra',
        skill='Systems of linear equations — substitution',
        difficulty='Easy',
        stimulus_html=r'<p>\[y = 3x\]\[x + y = 32\]</p>',
        question_html=r'<p>If \((x, y)\) is the solution to the system of equations above, what is the value of \(y\)?</p>',
        accepted_answers=['24'],
        correct_display='24',
        summary_vi=r'Thay \(y = 3x\) từ phương trình (1) vào phương trình (2): \(x + 3x = 32 \Rightarrow 4x = 32 \Rightarrow x = 8\). Lưu ý câu hỏi yêu cầu tìm \(y\) (không phải \(x\)): \(y = 3(8) = 24\). Kiểm tra: \(8 + 24 = 32\) (đúng).',
        key_takeaway=r'Kiểm tra kỹ lần cuối xem câu hỏi hỏi \(x\) hay \(y\) trước khi nhập số vào ô SPR.',
        desmos_tip_vi=r'Gõ <code>y = 3x</code> và <code>x + y = 32</code> vào Desmos, bấm giao điểm \((8, 24)\) và lấy tung độ \(y = 24\).',
    ))

    # Q6 - Algebra - Easy-Medium - C
    qs.append(math_mcq(
        qid='sat_mm2_m2l_q6',
        number=6,
        domain='Algebra',
        skill='Solving linear inequalities in context',
        difficulty='Easy',
        stimulus_html=r'<p>A weather satellite begins a mission with \(20\) gigabytes of telemetry data already transmitted and downloads an additional \(15\) gigabytes during each completed orbit. The satellite needs to transmit at least \(110\) gigabytes in total.</p>',
        question_html=r'<p>What is the minimum number of completed orbits \(n\) needed to reach this goal?</p>',
        options_dict={
            'A': r'\(4\)',
            'B': r'\(5\)',
            'C': r'\(6\)',
            'D': r'\(8\)',
        },
        correct_label='C',
        summary_vi=r'Lập bất phương trình cho tổng dung lượng dữ liệu: \(20 + 15n \ge 110\). Trừ \(20\) ở hai vế: \(15n \ge 90\). Chia hai vế cho \(15\): \(n \ge 6\). Do đó cần tối thiểu \(6\) vòng quỹ đạo hoàn chỉnh.',
        key_takeaway=r'Trừ lượng đã có sẵn (\(20\text{ GB}\)) trước khi chia cho tốc độ mỗi vòng (\(15\text{ GB/vòng}\)).',
        desmos_tip_vi=r'Gõ <code>20 + 15x >= 110</code> trên Desmos để thấy miền nghiệm bắt đầu từ đường biên nét liền \(x = 6\).',
        option_analysis={
            'A': ('Insufficient Orbits', r'Sau \(4\) vòng chỉ truyền được \(20 + 15(4) = 80\text{ GB} < 110\text{ GB}\).'),
            'B': ('Off-by-One Underestimation', r'Sau \(5\) vòng truyền được \(20 + 15(5) = 95\text{ GB}\), vẫn thiếu \(15\text{ GB}\).'),
            'C': ('Correct', r'\(20 + 15(6) = 110\text{ GB}\), đạt chuẩn mục tiêu tối thiểu.'),
            'D': ('Ignored Initial Data', r'Quên trừ \(20\text{ GB}\) ban đầu nên lấy \(110 / 15 \approx 7.33\) rồi làm tròn lên \(8\).'),
        },
    ))

    # Q7 - Algebra - Medium - D
    qs.append(math_mcq(
        qid='sat_mm2_m2l_q7',
        number=7,
        domain='Algebra',
        skill='Parallel lines in the xy-plane',
        difficulty='Medium',
        stimulus_html=r'<p>In the \(xy\)-plane, line \(k\) is defined by the equation \(y = -2x + 7\). Line \(m\) is parallel to line \(k\) and passes through the point \((0, -4)\).</p>',
        question_html=r'<p>Which equation defines line \(m\)?</p>',
        options_dict={
            'A': r'\(y = 2x - 4\)',
            'B': r'\(y = \frac{1}{2}x - 4\)',
            'C': r'\(y = -2x + 4\)',
            'D': r'\(y = -2x - 4\)',
        },
        correct_label='D',
        summary_vi=r'Hai đường thẳng song song có CÙNG hệ số góc, nên đường thẳng \(m\) có hệ số góc \(m = -2\). Vì đường thẳng \(m\) đi qua \((0, -4)\), tung độ gốc của nó chính là \(b = -4\). Ghép vào dạng \(y = mx + b\) ta được \(y = -2x - 4\).',
        key_takeaway=r'Song song = cùng hệ số góc \(m\); điểm \((0, b)\) chính là tung độ gốc \(b\) đặt thẳng vào công thức \(y = mx + b\).',
        desmos_tip_vi=r'Gõ <code>y = -2x + 7</code> và thử <code>y = -2x - 4</code> vào Desmos để thấy hai đường song song hoàn hảo và đường thứ hai cắt \(Oy\) đúng tại \((0, -4)\).',
        option_analysis={
            'A': ('Slope Sign Flip', r'Đổi dấu sai hệ số góc từ \(-2\) thành \(+2\).'),
            'B': ('Perpendicular Slope Trap', r'Nhầm điều kiện song song thành vuông góc (\(m_\perp = \frac{1}{2}\)).'),
            'C': ('Intercept Sign Flip', r'Đổi sai dấu tung độ gốc \(-4\) thành \(+4\).'),
            'D': ('Correct', r'Cùng hệ số góc \(-2\) và đi qua tung độ gốc \((0, -4)\).'),
        },
    ))

    # Q8 - Algebra - Medium - A
    qs.append(math_mcq(
        qid='sat_mm2_m2l_q8',
        number=8,
        domain='Algebra',
        skill='Systems of linear equations — elimination',
        difficulty='Medium',
        stimulus_html=r'<p>\[2x + y = 29\]\[3x - y = 16\]</p>',
        question_html=r'<p>What is the value of \(x\) in the solution \((x, y)\) to the system of equations above?</p>',
        options_dict={
            'A': r'\(9\)',
            'B': r'\(11\)',
            'C': r'\(13\)',
            'D': r'\(15\)',
        },
        correct_label='A',
        summary_vi=r'Cộng vế theo vế hai phương trình để triệt tiêu trực tiếp \(+y\) và \(-y\): \((2x + 3x) + (y - y) = 29 + 16 \Rightarrow 5x = 45 \Rightarrow x = 9\). (Thay lại ta cũng tìm được \(y = 29 - 18 = 11\), kiểm tra \(3(9) - 11 = 16\) khớp tuyệt đối).',
        key_takeaway=r'Khi thấy \(+y\) và \(-y\) đối dấu nhau ở hai phương trình, cộng thẳng hai phương trình để khử \(y\) trong 3 giây.',
        desmos_tip_vi=r'Gõ cả hai phương trình vào Desmos và bấm vào giao điểm \((9, 11)\) để đọc ngay hoành độ \(x = 9\).',
        option_analysis={
            'A': ('Correct', r'\(5x = 45 \Rightarrow x = 9\).'),
            'B': ('Solved for y Instead', r'Đây là giá trị của \(y = 11\), không phải \(x\).'),
            'C': ('Subtracted Constants Error', r'Trừ nhầm vế phải \(29 - 16 = 13\) thay vì cộng \(29 + 16 = 45\).'),
            'D': ('Divided by Wrong Coefficient', r'Cộng đúng \(45\) nhưng chia nhầm cho \(3\) thay vì \(2 + 3 = 5\).'),
        },
    ))

    # Q9 - Advanced Math - Easy - SPR
    qs.append(math_spr(
        qid='sat_mm2_m2l_q9',
        number=9,
        domain='Advanced Math',
        skill='Properties of exponents',
        difficulty='Easy',
        stimulus_html=r'<p>\[2^x \cdot 2^5 = 2^{14}\]</p>',
        question_html=r'<p>What value of \(x\) makes the equation above true?</p>',
        accepted_answers=['9'],
        correct_display='9',
        summary_vi=r'Khi nhân hai lũy thừa có cùng cơ số \(2\), ta giữ nguyên cơ số và CỘNG hai số mũ: \(2^{x + 5} = 2^{14}\). Suy ra \(x + 5 = 14 \Rightarrow x = 14 - 5 = 9\).',
        key_takeaway=r'Quy tắc nhân cùng cơ số: \(a^m \cdot a^n = a^{m + n}\) (cộng số mũ, không phải nhân số mũ).',
        desmos_tip_vi=r'Gõ <code>2^x * 2^5 = 2^14</code> trên Desmos để xác nhận vạch đứng chính xác tại \(x = 9\).',
    ))

    # Q10 - Advanced Math - Easy - B
    qs.append(math_mcq(
        qid='sat_mm2_m2l_q10',
        number=10,
        domain='Advanced Math',
        skill='Adding polynomial expressions',
        difficulty='Easy',
        stimulus_html=r'<p>\[(4x^2 + 3x - 5) + (2x^2 - 7x + 9)\]</p>',
        question_html=r'<p>Which of the following expressions is equivalent to the sum above?</p>',
        options_dict={
            'A': r'\(6x^2 + 10x + 4\)',
            'B': r'\(6x^2 - 4x + 4\)',
            'C': r'\(6x^2 - 4x - 14\)',
            'D': r'\(8x^2 - 4x + 4\)',
        },
        correct_label='B',
        summary_vi=r'Cộng từng cặp hạng tử đồng dạng cùng bậc: hệ số \(x^2\) là \(4 + 2 = 6\); hệ số \(x\) là \(3 + (-7) = -4\); hằng số tự do là \(-5 + 9 = +4\). Kết quả là \(6x^2 - 4x + 4\).',
        key_takeaway=r'Khi cộng hai đa thức, giữ nguyên số mũ của \(x^2\) và cộng đại số cẩn thận các số nguyên trái dấu (\(3 - 7 = -4\) và \(-5 + 9 = +4\)).',
        desmos_tip_vi=r'Thế \(x = 1\) vào đề bài: \((4 + 3 - 5) + (2 - 7 + 9) = 2 + 4 = 6\). Kiểm tra B tại \(x = 1\): \(6 - 4 + 4 = 6\) (khớp duy nhất!).',
        option_analysis={
            'A': ('Sign Error on x Term', r'Cộng nhầm \(3 + 7 = 10\) mà bỏ qua dấu trừ trước \(7x\).'),
            'B': ('Correct', r'Thu gọn đúng từng bậc: \(6x^2 - 4x + 4\).'),
            'C': ('Constant Sign Error', r'Tính nhầm \(-5 - 9 = -14\) thay vì \(-5 + 9 = +4\).'),
            'D': ('Multiplied Leading Coefficients', r'Nhân \(4 \times 2 = 8\) thay vì cộng \(4 + 2 = 6\) cho hạng tử \(x^2\).'),
        },
    ))

    # Q11 - Advanced Math - Easy-Medium - D
    qs.append(math_mcq(
        qid='sat_mm2_m2l_q11',
        number=11,
        domain='Advanced Math',
        skill='Solving quadratic equations by factoring',
        difficulty='Easy',
        stimulus_html=r'<p>\[x^2 - 7x + 12 = 0\]</p>',
        question_html=r'<p>What are the solutions to the quadratic equation above?</p>',
        options_dict={
            'A': r'\(x = -4\) and \(x = -3\)',
            'B': r'\(x = -6\) and \(x = 2\)',
            'C': r'\(x = 2\) and \(x = 6\)',
            'D': r'\(x = 3\) and \(x = 4\)',
        },
        correct_label='D',
        summary_vi=r'Tìm hai số có tích bằng \(+12\) và tổng bằng \(-7\): đó là \(-3\) và \(-4\). Phân tích thành nhân tử: \((x - 3)(x - 4) = 0\). Cho từng nhân tử bằng \(0\) ta thu được \(x = 3\) và \(x = 4\).',
        key_takeaway=r'Đừng quên đổi dấu khi chuyển từ nhân tử \((x - 3)(x - 4) = 0\) sang nghiệm \(x = +3\) và \(x = +4\).',
        desmos_tip_vi=r'Gõ <code>y = x^2 - 7x + 12</code> trên Desmos và bấm vào hai giao điểm trục hoành để thấy ngay \((3, 0)\) và \((4, 0)\).',
        option_analysis={
            'A': ('Factor Sign Trap', r'Lấy nhầm hai số trong nhân tử \(-3, -4\) làm nghiệm mà quên đổi dấu.'),
            'B': ('Wrong Factor Pair', r'Tích \((-6)(2) = -12 \ne +12\).'),
            'C': ('Wrong Sum Pair', r'Tích \((2)(6) = 12\) nhưng tổng \(2 + 6 = 8 \ne 7\).'),
            'D': ('Correct', r'\((x - 3)(x - 4) = 0 \Rightarrow x = 3\) và \(x = 4\).'),
        },
    ))

    # Q12 - Advanced Math - Medium - A
    qs.append(math_mcq(
        qid='sat_mm2_m2l_q12',
        number=12,
        domain='Advanced Math',
        skill='Interpreting parameters of exponential functions',
        difficulty='Medium',
        stimulus_html=r'<p>The estimated number of yeast cells \(N(t)\) in a biomedical lab culture \(t\) hours after observation begins is modeled by the function:</p><p>\[N(t) = 350(1.4)^t\]</p>',
        question_html=r'<p>Which of the following is the best interpretation of \(350\) in this context?</p>',
        options_dict={
            'A': r'The estimated initial number of yeast cells in the culture when \(t = 0\).',
            'B': r'The estimated number of yeast cells added to the culture each hour.',
            'C': r'The percent increase in the number of yeast cells each hour.',
            'D': r'The maximum number of yeast cells the culture can contain.',
        },
        correct_label='A',
        summary_vi=r'Trong mô hình hàm mũ chuẩn \(N(t) = a \cdot b^t\), hệ số đứng đầu \(a = 350\) luôn là giá trị ban đầu khi \(t = 0\) vì \(N(0) = 350(1.4)^0 = 350 \times 1 = 350\). Do đó \(350\) biểu thị số tế bào nấm men ước tính ban đầu tại thời điểm \(t = 0\).',
        key_takeaway=r'Trong \(y = a(b)^t\): \(a\) luôn là giá trị ban đầu (khi \(t = 0\)), còn \(b\) là hệ số tăng trưởng mỗi đơn vị thời gian (\(1.4 = \) tăng \(40\%\)/giờ).',
        desmos_tip_vi=r'Thế nhanh \(t = 0\): vì mọi số khác \(0\) mũ \(0\) đều bằng \(1\), nên \(N(0) = 350\) chính là số tế bào tại phút đầu tiên.',
        option_analysis={
            'A': ('Correct', r'Khi \(t = 0\), \(N(0) = 350\), biểu thị số tế bào ban đầu.'),
            'B': ('Linear Slope Confusion', r'Nhầm hàm mũ với hàm tuyến tính; số tế bào tăng thêm mỗi giờ thay đổi liên tục chứ không cố định \(350\).'),
            'C': ('Growth Rate Confusion', r'Tỉ lệ phần trăm tăng mỗi giờ là \(40\%\) (suy từ \(1.4 = 1 + 0.40\)), không phải \(350\).'),
            'D': ('Asymptote Misconception', r'Vì cơ số \(1.4 > 1\), hàm tăng không giới hạn khi \(t\) tăng nên \(350\) là giá trị nhỏ nhất (ban đầu), không phải tối đa.'),
        },
    ))

    # Q13 - Advanced Math - Medium - SPR
    svg13 = svg_parabola_vertex(
        h_lbl='4',
        k_lbl='35',
        opens_up=False,
        note='Note: Figure not drawn to scale.'
    )
    qs.append(math_spr(
        qid='sat_mm2_m2l_q13',
        number=13,
        domain='Advanced Math',
        skill='Maximum value of a quadratic in vertex form',
        difficulty='Medium',
        stimulus_html=rf'<p>The height \(h(t)\), in meters, of an aerospace test drone \(t\) seconds after launch is modeled by the quadratic function below, whose graph is shown:</p><p>\[h(t) = -2(t - 4)^2 + 35\]</p><div style="display:flex;justify-content:center;margin:12px 0;">{svg13}</div>',
        question_html=r'<p>What is the maximum height, in meters, reached by the test drone?</p>',
        accepted_answers=['35'],
        correct_display='35',
        summary_vi=r'Hàm bậc hai đã ở sẵn dạng đỉnh \(h(t) = a(t - h)^2 + k\) với \(a = -2 < 0\) (parabol quay bề lõm xuống dưới) và đỉnh \((4, 35)\). Vì \(-2(t - 4)^2 \le 0\) với mọi \(t\), giá trị lớn nhất của \(h(t)\) đạt được tại \(t = 4\) giây và bằng đúng tung độ đỉnh \(k = 35\) mét.',
        key_takeaway=r'Với parabol dạng đỉnh \(a(x - h)^2 + k\) có \(a < 0\): hoành độ \(h\) là THỜI ĐIỂM đạt cực đại, còn tung độ \(k\) là GIÁ TRỊ cực đại.',
        desmos_tip_vi=r'Gõ <code>y = -2(x - 4)^2 + 35</code> trên Desmos rồi bấm vào đỉnh cao nhất của đường cong để đọc tọa độ \((4, 35)\) \(\rightarrow\) độ cao cực đại \(35\).',
    ))

    # Q14 - Advanced Math - Medium - C
    qs.append(math_mcq(
        qid='sat_mm2_m2l_q14',
        number=14,
        domain='Advanced Math',
        skill='Rearranging formulas (isolating a variable)',
        difficulty='Medium',
        stimulus_html=r'<p>The surface-area calibration equation for a rectangular greenhouse planter box is given by:</p><p>\[A = 2w^2 + 6h\]</p>',
        question_html=r'<p>Which equation correctly expresses \(h\) in terms of \(A\) and \(w\)?</p>',
        options_dict={
            'A': r'\(h = \frac{A + 2w^2}{6}\)',
            'B': r'\(h = \frac{A}{6} - 2w^2\)',
            'C': r'\(h = \frac{A - 2w^2}{6}\)',
            'D': r'\(h = 6A - 2w^2\)',
        },
        correct_label='C',
        summary_vi=r'Muốn cô lập \(h\), trước tiên trừ \(2w^2\) ở cả hai vế: \(A - 2w^2 = 6h\). Sau đó chia toàn bộ vế trái cho \(6\): \(h = \frac{A - 2w^2}{6}\).',
        key_takeaway=r'Khi chia cả hai vế cho \(6\), phải chia TOÀN BỘ biểu thức \(A - 2w^2\) chứ không chỉ chia riêng \(A\).',
        desmos_tip_vi=r'Thử số đơn giản: chọn \(w = 1, h = 2 \Rightarrow A = 2(1) + 6(2) = 14\). Thay \(A = 14, w = 1\) vào 4 đáp án: chỉ C cho \(\frac{14 - 2}{6} = 2 = h\).',
        option_analysis={
            'A': ('Transposition Sign Error', r'Chuyển \(2w^2\) sang vế trái nhưng quên đổi dấu thành trừ.'),
            'B': ('Partial Division Error', r'Chỉ chia \(A\) cho \(6\) mà quên chia cả hạng tử \(-2w^2\) cho \(6\).'),
            'C': ('Correct', r'Trừ \(2w^2\) rồi chia toàn bộ cho \(6\): \(h = \frac{A - 2w^2}{6}\).'),
            'D': ('Multiplied Instead of Divided', r'Nhân \(6\) vào \(A\) thay vì chia cho \(6\).'),
        },
    ))

    # Q15 - Advanced Math - Medium - B
    qs.append(math_mcq(
        qid='sat_mm2_m2l_q15',
        number=15,
        domain='Advanced Math',
        skill='Evaluating exponential decay functions',
        difficulty='Medium',
        stimulus_html=r'<p>A satellite radio signal loses half of its power at each relay stage. Its power \(S(d)\), in microwatts, after \(d\) relay stages is modeled by:</p><p>\[S(d) = 800(0.5)^d\]</p>',
        question_html=r'<p>What is the signal power, in microwatts, after \(4\) relay stages?</p>',
        options_dict={
            'A': r'\(25\)',
            'B': r'\(50\)',
            'C': r'\(100\)',
            'D': r'\(200\)',
        },
        correct_label='B',
        summary_vi=r'Thay \(d = 4\) vào hàm số: \(S(4) = 800(0.5)^4 = 800 \times \frac{1}{16} = 50\) microwatts. (Hoặc chia đôi 4 lần liên tiếp: \(800 \rightarrow 400 \rightarrow 200 \rightarrow 100 \rightarrow 50\)).',
        key_takeaway=r'Với hàm mũ cơ số \(0.5\), có thể kiểm chứng nhanh bằng cách chia đôi đúng \(d\) lần liên tiếp.',
        desmos_tip_vi=r'Gõ <code>800 * (0.5)^4</code> vào Desmos để nhận ngay đáp số \(50\).',
        option_analysis={
            'A': ('One Extra Halving', r'Chia đôi tới \(5\) lần (\(S(5) = 25\)) thay vì \(4\) lần.'),
            'B': ('Correct', r'\(800 \times (0.5)^4 = 800 / 16 = 50\).'),
            'C': ('One Fewer Halving', r'Chỉ chia đôi \(3\) lần (\(S(3) = 100\)).'),
            'D': ('Linear Division Trap', r'Chia thẳng \(800 / 4 = 200\) thay vì nâng lũy thừa \((0.5)^4\).'),
        },
    ))

    # Q16 - PSDA - Easy - SPR
    qs.append(math_spr(
        qid='sat_mm2_m2l_q16',
        number=16,
        domain='Problem-Solving and Data Analysis',
        skill='Percentages of a quantity',
        difficulty='Easy',
        stimulus_html=r'<p>An automated hydroponic greenhouse harvested \(450\) kilograms of strawberries in one week. Of the total harvest, \(28\%\) met the Grade-A export standard.</p>',
        question_html=r'<p>How many kilograms of strawberries met the Grade-A export standard?</p>',
        accepted_answers=['126'],
        correct_display='126',
        summary_vi=r'Đổi \(28\% = 0.28\) rồi nhân với tổng sản lượng \(450\): \(0.28 \times 450 = 126\text{ kg}\).',
        key_takeaway=r'Muốn tìm \(p\%\) của một số \(N\), chỉ cần tính \(\frac{p}{100} \times N\).',
        desmos_tip_vi=r'Gõ trực tiếp <code>0.28 * 450</code> (hoặc <code>28% of 450</code>) trong Desmos để nhận ngay \(126\).',
    ))

    # Q17 - PSDA - Easy - A
    t17 = build_math_table(
        ['Ticket Category', 'Number of Passengers'],
        [
            ['Adult', '72'],
            ['Student', '48'],
            ['Senior', '30'],
            ['<b>Total</b>', '<b>150</b>'],
        ],
        caption='Passenger Ticket Categories on High-Speed Train #204'
    )
    qs.append(math_mcq(
        qid='sat_mm2_m2l_q17',
        number=17,
        domain='Problem-Solving and Data Analysis',
        skill='Simple probability from a frequency table',
        difficulty='Easy',
        stimulus_html=rf'<p>The table below shows the distribution of ticket categories for all \(150\) passengers aboard High-Speed Train #204.</p>{t17}',
        question_html=r'<p>If one passenger is selected at random from Train #204, what is the probability that the passenger holds a Student ticket?</p>',
        options_dict={
            'A': r'\(\frac{8}{25}\)',
            'B': r'\(\frac{1}{5}\)',
            'C': r'\(\frac{12}{25}\)',
            'D': r'\(\frac{8}{17}\)',
        },
        correct_label='A',
        summary_vi=r'Có \(48\) hành khách dùng vé Student trong tổng số \(150\) hành khách. Xác suất chọn ngẫu nhiên được hành khách vé Student là \(\frac{48}{150}\). Chia cả tử và mẫu cho \(6\): \(\frac{48}{150} = \frac{8}{25}\).',
        key_takeaway=r'Xác suất cơ bản = \(\frac{\text{Số phần tử thỏa mãn}}{\text{Tổng số phần tử}}\), sau đó rút gọn phân số tối giản.',
        desmos_tip_vi=r'Gõ <code>48/150</code> vào Desmos rồi nhấn nút chuyển đổi phân số bên trái dòng để nhận ngay \(\frac{8}{25}\).',
        option_analysis={
            'A': ('Correct', r'\(\frac{48}{150} = \frac{8}{25}\).'),
            'B': ('Wrong Category (Senior)', r'Đây là xác suất của nhóm Senior: \(\frac{30}{150} = \frac{1}{5}\).'),
            'C': ('Wrong Category (Adult)', r'Đây là xác suất của nhóm Adult: \(\frac{72}{150} = \frac{12}{25}\).'),
            'D': ('Part-to-Part Ratio Trap', r'Lấy tỉ lệ Student chia cho nhóm còn lại (\(\frac{48}{102} = \frac{8}{17}\)) thay vì chia cho tổng \(150\).'),
        },
    ))

    # Q18 - PSDA - Easy-Medium - C
    t18 = build_math_table(
        ['Sample ID', 'S1', 'S2', 'S3', 'S4', 'S5'],
        [['Temperature (°C)', '18', '22', '24', '26', '35']],
        caption='Biomedical Culture Chamber Temperature Readings'
    )
    qs.append(math_mcq(
        qid='sat_mm2_m2l_q18',
        number=18,
        domain='Problem-Solving and Data Analysis',
        skill='Calculating the arithmetic mean',
        difficulty='Easy',
        stimulus_html=rf'<p>The table below lists five temperature readings recorded in a biomedical cell culture chamber.</p>{t18}',
        question_html=r'<p>What is the mean (arithmetic average) of these five temperature readings, in degrees Celsius?</p>',
        options_dict={
            'A': r'\(22\)',
            'B': r'\(24\)',
            'C': r'\(25\)',
            'D': r'\(26\)',
        },
        correct_label='C',
        summary_vi=r'Cộng tất cả \(5\) giá trị rồi chia cho \(5\): \(\text{Mean} = \frac{18 + 22 + 24 + 26 + 35}{5} = \frac{125}{5} = 25^\circ\text{C}\).',
        key_takeaway=r'Không nhầm lẫn giữa Mean (trung bình cộng = tổng chia số lượng) và Median (số đứng chính giữa \(24\)).',
        desmos_tip_vi=r'Gõ <code>mean(18, 22, 24, 26, 35)</code> vào Desmos để hiện ngay kết quả \(25\).',
        option_analysis={
            'A': ('Wrong Position Value', r'Chọn nhầm giá trị thứ hai \(22\).'),
            'B': ('Median Instead of Mean', r'Bẫy kinh điển: \(24\) là trung vị (median — số đứng giữa), không phải trung bình cộng (mean).'),
            'C': ('Correct', r'\(\frac{125}{5} = 25\).'),
            'D': ('Arithmetic Mistake', r'Cộng nhầm tổng thành \(130\) hoặc chọn nhầm giá trị thứ tư \(26\).'),
        },
    ))

    # Q19 - PSDA - Medium - SPR
    qs.append(math_spr(
        qid='sat_mm2_m2l_q19',
        number=19,
        domain='Problem-Solving and Data Analysis',
        skill='Proportional relationships and unit rates',
        difficulty='Medium',
        stimulus_html=r'<p>An automated drip-irrigation line in a greenhouse delivers \(18\) liters of nutrient water every \(12\) minutes at a constant flow rate.</p>',
        question_html=r'<p>At this same constant rate, how many liters of nutrient water will the line deliver in \(50\) minutes?</p>',
        accepted_answers=['75'],
        correct_display='75',
        summary_vi=r'Tính tốc độ dòng chảy mỗi phút: \(\frac{18\text{ lít}}{12\text{ phút}} = 1.5\text{ lít/phút}\). Trong \(50\) phút, lượng nước bơm được là \(1.5 \times 50 = 75\text{ lít}\).',
        key_takeaway=r'Quy về đơn vị \(1\) phút (unit rate \(= 1.5\) lít/phút) rồi nhân với thời gian mới là cách ít sai sót nhất.',
        desmos_tip_vi=r'Gõ <code>(18 / 12) * 50</code> trên Desmos để nhận ngay đáp án \(75\).',
    ))

    # Q20 - Geometry & Trig - Easy - B
    svg20 = svg_parallel_transversal(
        line1='ℓ',
        line2='m',
        ang1_lbl='124°',
        ang2_lbl='(2x + 10)°',
        note='Note: Figure not drawn to scale.'
    )
    qs.append(math_mcq(
        qid='sat_mm2_m2l_q20',
        number=20,
        domain='Geometry and Trigonometry',
        skill='Parallel lines cut by a transversal',
        difficulty='Easy',
        stimulus_html=rf'<p>In the figure below, lines \(\ell\) and \(m\) are parallel and are intersected by a transversal line, representing parallel ceiling acoustic beams in a concert hall.</p><div style="display:flex;justify-content:center;margin:12px 0;">{svg20}</div>',
        question_html=r'<p>What is the value of \(x\)?</p>',
        options_dict={
            'A': r'\(28\)',
            'B': r'\(57\)',
            'C': r'\(62\)',
            'D': r'\(124\)',
        },
        correct_label='B',
        summary_vi=r'Hai góc \(124^\circ\) và \((2x + 10)^\circ\) nằm ở vị trí đồng vị (corresponding angles) tạo bởi hai đường thẳng song song \(\ell \parallel m\) và một cát tuyến, nên chúng bằng nhau: \(2x + 10 = 124 \Rightarrow 2x = 114 \Rightarrow x = 57\).',
        key_takeaway=r'Với hai đường thẳng song song cắt bởi một đường chéo, mọi góc tù đều bằng nhau và mọi góc nhọn đều bằng nhau (còn góc nhọn + góc tù = \(180^\circ\)).',
        desmos_tip_vi=r'Gõ <code>2x + 10 = 124</code> trên Desmos để xác nhận vạch đứng tại \(x = 57\).',
        option_analysis={
            'A': ('Supplementary Angle Trap', r'Đặt nhầm tổng bằng \(180^\circ\) (\(2x + 10 = 56 \Rightarrow x = 23\)) hoặc lấy \((180 - 124)/2 = 28\).'),
            'B': ('Correct', r'Góc đồng vị bằng nhau: \(2x + 10 = 124 \Rightarrow x = 57\).'),
            'C': ('Forgot to Subtract 10', r'Chia thẳng \(124 / 2 = 62\) mà quên trừ đi \(10\) trước khi chia.'),
            'D': ('Set x Equal to Angle', r'Gán luôn \(x = 124\) thay vì giải phương trình \(2x + 10 = 124\).'),
        },
    ))

    # Q21 - Geometry & Trig - Easy-Medium - D
    svg21 = svg_similar_triangles(
        side_ab='6',
        side_bc='10',
        side_de='15',
        side_ef='x',
        v1='A',
        v2='B',
        v3='C',
        v4='D',
        v5='E',
        v6='F',
    )
    qs.append(math_mcq(
        qid='sat_mm2_m2l_q21',
        number=21,
        domain='Geometry and Trigonometry',
        skill='Similar triangles and side ratios',
        difficulty='Medium',
        stimulus_html=rf'<p>In the figure below, triangle \(ABC\) is similar to triangle \(DEF\), where vertices \(A\), \(B\), and \(C\) correspond to vertices \(D\), \(E\), and \(F\), respectively.</p><div style="display:flex;justify-content:center;margin:12px 0;">{svg21}</div>',
        question_html=r'<p>What is the length of side \(\overline{EF}\), labeled \(x\) in the figure?</p>',
        options_dict={
            'A': r'\(9\)',
            'B': r'\(19\)',
            'C': r'\(21\)',
            'D': r'\(25\)',
        },
        correct_label='D',
        summary_vi=r'Vì \(\triangle ABC \sim \triangle DEF\), các cặp cạnh tương ứng tỉ lệ với nhau: \(\frac{EF}{BC} = \frac{DE}{AB}\). Thay số: \(\frac{x}{10} = \frac{15}{6} = 2.5 \Rightarrow x = 10 \times 2.5 = 25\).',
        key_takeaway=r'Tam giác đồng dạng có chung hệ số phóng đại \(k = \frac{\text{cạnh mới}}{\text{cạnh cũ}} = \frac{15}{6} = 2.5\), KHÔNG cộng thêm hiệu độ dài (\(15 - 6 = 9\)).',
        desmos_tip_vi=r'Gõ <code>(15 / 6) * 10</code> trên Desmos để nhận ngay đáp số \(25\).',
        option_analysis={
            'A': ('Additive Difference Only', r'Lấy hiệu \(15 - 6 = 9\) làm đáp số thay vì lập tỉ lệ.'),
            'B': ('Additive Scaling Trap', r'Bẫy kinh điển: thấy cạnh \(6\) tăng thêm \(9\) thành \(15\), rồi cộng nhầm \(10 + 9 = 19\) thay vì nhân hệ số \(2.5\).'),
            'C': ('Cross-Multiplication Error', r'Lập sai tỉ lệ cạnh tương ứng.'),
            'D': ('Correct', r'Hệ số đồng dạng \(k = \frac{15}{6} = 2.5 \Rightarrow x = 10 \times 2.5 = 25\).'),
        },
    ))

    # Q22 - Geometry & Trig - Medium - SPR
    svg22 = svg_right_triangle(
        a_lbl='9',
        b_lbl='12',
        c_lbl='',
        v_top='A',
        v_right_angle='B',
        v_right='C',
        note='Note: Figure not drawn to scale.'
    )
    qs.append(math_spr(
        qid='sat_mm2_m2l_q22',
        number=22,
        domain='Geometry and Trigonometry',
        skill='Pythagorean theorem and perimeter',
        difficulty='Medium',
        stimulus_html=rf'<p>An acoustic baffle panel in a concert hall is shaped like right triangle \(ABC\), with \(\angle B = 90^\circ\), \(AB = 9\) feet, and \(BC = 12\) feet, as shown below.</p><div style="display:flex;justify-content:center;margin:12px 0;">{svg22}</div>',
        question_html=r'<p>What is the <b>perimeter</b>, in feet, of triangle \(ABC\)?</p>',
        accepted_answers=['36'],
        correct_display='36',
        summary_vi=r'Áp dụng định lý Pythagore để tìm cạnh huyền \(AC\): \(AC = \sqrt{9^2 + 12^2} = \sqrt{81 + 144} = \sqrt{225} = 15\) feet (hoặc nhận nhanh bộ ba \(3\text{–}4\text{–}5\) nhân \(3\)). Chu vi (perimeter) của tam giác là tổng độ dài cả \(3\) cạnh: \(P = 9 + 12 + 15 = 36\) feet.',
        key_takeaway=r'Đọc kỹ câu hỏi yêu cầu tìm cạnh huyền (\(15\)), diện tích (\(54\)), hay CHU VI (\(9 + 12 + 15 = 36\)) trước khi điền đáp số.',
        desmos_tip_vi=r'Gõ <code>9 + 12 + sqrt(9^2 + 12^2)</code> vào Desmos để nhận ngay chu vi \(36\).',
    ))

    return qs


if __name__ == '__main__':
    verify_math()
    qs = get_m2l_questions()
    print(f"M2 Lower verified OK: {len(qs)} questions.")
