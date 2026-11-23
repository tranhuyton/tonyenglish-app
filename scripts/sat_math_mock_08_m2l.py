# -*- coding: utf-8 -*-
"""
Digital SAT Math Adaptive Mock Test #8 — Module 2 Standard/Lower (300–600 Band, 22 Questions)
Themes: Geothermal Power Wells, Autonomous Warehouse Conveyor Robotics,
        Violin Luthier Acoustics & Wood Curing, National Park Wildlife Census & Tagging,
        Stepped-Pyramid & Truncated-Cone Monument Geometry.
Blueprint: 8 Algebra (Q1-Q8), 7 Advanced Math (Q9-Q15), 4 PSDA (Q16-Q19), 3 Geometry/Trig (Q20-Q22).
Format: 16 MCQ (A:4, B:4, C:4, D:4) + 6 SPR (Q5, Q9, Q13, Q16, Q19, Q22).
"""

from fractions import Fraction
from sat_math_helpers import (
    math_mcq, math_spr, build_math_table,
    svg_right_triangle, svg_similar_triangles, svg_cylinder
)


def verify_math():
    """Programmatic exact arithmetic verification for all 22 Module 2 Standard questions."""
    # Q1: 6x - 11 = 37 => x = 8 => 4x - 5 = 27
    x1 = Fraction(37 + 11, 6)
    assert x1 == 8 and 6 * x1 - 11 == 37 and 4 * x1 - 5 == 27

    # Q2: C(h) = 45h + 75 => C(0) = 75
    assert 45 * 0 + 75 == 75

    # Q3: slope through (2, 5) and (6, 21) => 16/4 = 4
    assert Fraction(21 - 5, 6 - 2) == 4

    # Q4: x + y = 18, x - y = 4 => x = 11, y = 7
    x4 = Fraction(18 + 4, 2)
    y4 = 18 - x4
    assert x4 == 11 and y4 == 7 and x4 + y4 == 18 and x4 - y4 == 4

    # Q5 (SPR): 4(x - 5) = 28 => x = 12
    assert 4 * (12 - 5) == 28

    # Q6: 3x + 8 >= 29 => x >= 7
    assert 3 * 7 + 8 == 29 and 3 * 6 + 8 < 29

    # Q7: parallel to y = -3x + 5 through (0, -4) => y = -3x - 4
    assert -3 * 0 - 4 == -4

    # Q8: x + y = 16, 30x + 50y = 620 => x = 9, y = 7
    x8 = Fraction(50 * 16 - 620, 50 - 30)
    y8 = 16 - x8
    assert x8 == 9 and y8 == 7 and 30 * x8 + 50 * y8 == 620

    # Q9 (SPR): f(x) = 3x^2 - 4x + 7 => f(3) = 27 - 12 + 7 = 22
    assert 3 * (3 ** 2) - 4 * 3 + 7 == 22

    # Q10: x^2 - 9x + 20 = 0 => (x - 4)(x - 5) = 0 => sum = 9
    assert (4 - 4) * (4 - 5) == 0 and 4 * 5 == 20 and 4 + 5 == 9

    # Q11: (2x^3)^4 = 16x^12
    for xv in (2, 3):
        assert (2 * (xv ** 3)) ** 4 == 16 * (xv ** 12)

    # Q12: B(t) = 140(1.08)^t => B(0) = 140
    assert 140 * (Fraction(108, 100) ** 0) == 140

    # Q13 (SPR): y = 2(x - 6)^2 + 14 => min value = 14 at x = 6
    assert 2 * (6 - 6) ** 2 + 14 == 14 and 2 * (5 - 6) ** 2 + 14 > 14

    # Q14: (x - 6)(x + 4) = x^2 - 2x - 24
    for xv in (-3, 0, 5):
        assert (xv - 6) * (xv + 4) == xv ** 2 - 2 * xv - 24

    # Q15: (5x^2 - 3x + 8) - (2x^2 - 7x + 3) = 3x^2 + 4x + 5
    for xv in (-2, 1, 4):
        assert (5 * xv ** 2 - 3 * xv + 8) - (2 * xv ** 2 - 7 * xv + 3) == 3 * xv ** 2 + 4 * xv + 5

    # Q16 (SPR): 84 MWh in 12 hrs => (84/12) * 30 = 210 MWh
    assert Fraction(84, 12) * 30 == 210

    # Q17: 65% of 320 = 208
    assert Fraction(65, 100) * 320 == 208

    # Q18: median of [14, 23, 19, 11, 27, 17, 21] => sorted [11, 14, 17, 19, 21, 23, 27] => 19
    sightings = sorted([14, 23, 19, 11, 27, 17, 21])
    assert len(sightings) == 7 and sightings[3] == 19

    # Q19 (SPR): P(Delayed) = 45 / 150 = 3/10 = 0.3
    assert 62 + 18 == 80 and 43 + 27 == 70 and 80 + 70 == 150
    assert 62 + 43 == 105 and 18 + 27 == 45
    assert Fraction(45, 150) == Fraction(3, 10)

    # Q20: right triangle angle sum: 180 - 90 - 34 = 56
    assert 180 - 90 - 34 == 56

    # Q21: similar triangles AB=6, BC=10, DE=15 => EF = 10 * (15/6) = 25
    assert 10 * Fraction(15, 6) == 25

    # Q22 (SPR): cylinder r = 6, h = 5 => V = pi * 6^2 * 5 = 180 pi
    assert (6 ** 2) * 5 == 180

    return True


def get_m2l_questions():
    tbl_q18 = build_math_table(
        ['Day', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
        [['Mountain Goats Sighted', '14', '23', '19', '11', '27', '17', '21']],
        caption='National Park Daily Mountain Goat Sightings (7-Day Survey)'
    )
    tbl_q19 = build_math_table(
        ['Routing Lane', 'On-Time', 'Delayed', 'Total'],
        [
            ['Lane A', '62', '18', '80'],
            ['Lane B', '43', '27', '70'],
            ['Total', '105', '45', '150'],
        ],
        caption='Autonomous Warehouse Conveyor Package Routing'
    )
    svg_q20 = svg_right_triangle(
        'AB', 'BC', 'AC', angle_top_left='34°', angle_bottom_right='x°',
        v_top='A', v_right_angle='B', v_right='C',
        note='Note: Figure not drawn to scale.'
    )
    svg_q21 = svg_similar_triangles(
        '6', '10', '15', 'x',
        'A', 'B', 'C', 'D', 'E', 'F'
    )
    svg_q22 = svg_cylinder(
        'r = 6', 'h = 5',
        note='Cylindrical Geothermal Brine Tank'
    )

    return [
        # Q1 — Algebra (Easy, MCQ -> D)
        math_mcq(
            'sat_mm8_m2l_q1', 1, 'Algebra', 'Linear equations in one variable', 'Easy',
            r'<p>Consider the linear equation \(6x - 11 = 37\).</p>',
            r'What is the value of \(4x - 5\)?',
            {'A': r'\(8\)', 'B': r'\(32\)', 'C': r'\(37\)', 'D': r'\(27\)'},
            'D',
            r'Cộng \(11\) vào hai vế: \(6x = 48 \Rightarrow x = 8\). Thay \(x = 8\) vào biểu thức đề hỏi: \(4(8) - 5 = 27\).',
            r'Giải xong \(x = 8\), luôn nhớ thay ngược vào biểu thức cuối cùng \(4x - 5\) trước khi chọn đáp án.',
            {
                'A': ('Stopped at x', r'\(8\) mới là giá trị của \(x\), chưa tính \(4x - 5\).'),
                'B': ('Forgot -5', r'Chỉ tính \(4x = 32\) mà quên trừ \(5\).'),
                'C': ('Added 5 Instead of Subtracted', r'Tính nhầm \(4(8) + 5 = 37\).'),
                'D': ('Correct', r'\(x = 8 \Rightarrow 4(8) - 5 = 27\).'),
            },
            r'Gõ `6x - 11 = 37` trên Desmos ra `x = 8`, sau đó tính `4(8) - 5 = 27`.'
        ),
        # Q2 — Algebra (Easy, MCQ -> B) | Theme: Violin Luthier Acoustics
        math_mcq(
            'sat_mm8_m2l_q2', 2, 'Algebra', 'Linear functions', 'Easy',
            r'<p>A violin workshop models the total cost \(C(h)\), in dollars, to rehair and service a bow taking \(h\) hours of labor using the equation \(C(h) = 45h + 75\).</p>',
            r'What does the number \(75\) represent in this equation?',
            {
                'A': r'The labor charge per hour, in dollars',
                'B': r'The flat base workshop inspection fee, in dollars, before any labor hours are added',
                'C': r'The maximum number of hours required to service a bow',
                'D': r'The total cost of \(75\) hours of bow service',
            },
            'B',
            r'Trong phương trình \(C(h) = 45h + 75\), hằng số \(75\) là tung độ gốc (giá trị tại \(h = 0\)), tức khoản phí kiểm tra cố định ban đầu ($75) chưa cộng tiền công theo giờ.',
            r'Trong \(y = mx + b\), hằng số tự do \(b\) luôn là khoản phí cố định ban đầu (flat fee) khi \(x = 0\).',
            {
                'A': ('Confused with Slope', r'$45 mới là đơn giá công làm việc mỗi giờ.'),
                'B': ('Correct', r'$75 là mức phí kiểm tra cố định ban đầu.'),
                'C': ('Wrong Quantity', r'75 không phải số giờ làm việc tối đa.'),
                'D': ('Wrong Unit', r'75 có đơn vị là dollars, không phải số giờ.'),
            },
            r'Thay `h = 0` vào `45(0) + 75 = 75` để thấy ngay đó là chi phí cố định ban đầu.'
        ),
        # Q3 — Algebra (Easy, MCQ -> A)
        math_mcq(
            'sat_mm8_m2l_q3', 3, 'Algebra', 'Linear equations in two variables', 'Easy',
            r'<p>In the \(xy\)-plane, a line passes through the points \((2, 5)\) and \((6, 21)\).</p>',
            r'What is the slope of this line?',
            {'A': r'\(4\)', 'B': r'\(\frac{1}{4}\)', 'C': r'\(3\)', 'D': r'\(16\)'},
            'A',
            r'Áp dụng công thức hệ số góc: \(m = \frac{y_2 - y_1}{x_2 - x_1} = \frac{21 - 5}{6 - 2} = \frac{16}{4} = 4\).',
            r'Luôn đặt hiệu tung độ (\(\Delta y\)) ở tử số và hiệu hoành độ (\(\Delta x\)) ở mẫu số.',
            {
                'A': ('Correct', r'\(\frac{21 - 5}{6 - 2} = \frac{16}{4} = 4\).'),
                'B': ('Inverted Slope Ratio', r'Tính ngược \(\frac{\Delta x}{\Delta y} = \frac{4}{16} = \frac{1}{4}\).'),
                'C': ('Subtraction Error', r'Trừ nhầm tọa độ hoặc chia sai.'),
                'D': ('Forgot to Divide by Δx', r'\(16\) mới chỉ là \(\Delta y = 21 - 5\), quên chia cho \(\Delta x = 4\).'),
            },
            r'Gõ `(21 - 5) / (6 - 2)` trên Desmos ra ngay `4`.'
        ),
        # Q4 — Algebra (Easy, MCQ -> C)
        math_mcq(
            'sat_mm8_m2l_q4', 4, 'Algebra', 'Systems of two linear equations in two variables', 'Easy',
            r'<p>Consider the system of equations below:</p><p style="text-align:center;">\[\begin{cases} x + y = 18 \\ x - y = 4 \end{cases}\]</p>',
            r'What is the value of \(x\)?',
            {'A': r'\(7\)', 'B': r'\(22\)', 'C': r'\(11\)', 'D': r'\(14\)'},
            'C',
            r'Cộng vế theo vế hai phương trình để khử \(y\): \((x + y) + (x - y) = 18 + 4 \Rightarrow 2x = 22 \Rightarrow x = 11\) (và \(y = 7\)).',
            r'Với hệ có \(+y\) và \(-y\), cộng trực tiếp hai phương trình sẽ triệt tiêu ngay \(y\) và ra \(2x\)!',
            {
                'A': ('Found y Instead of x', r'\(7\) là giá trị của \(y\), trong khi đề hỏi \(x\).'),
                'B': ('Forgot to Divide by 2', r'\(22\) là giá trị của \(2x\), cần chia \(2\) để ra \(x = 11\).'),
                'C': ('Correct', r'\(2x = 22 \Rightarrow x = 11\).'),
                'D': ('Subtracted Instead of Added', r'Trừ hai vế phải \(18 - 4 = 14\) nhưng lại quên chia \(2\) và tìm nhầm biến.'),
            },
            r'Vẽ `x + y = 18` và `x - y = 4` trên Desmos → bấm chấm giao điểm `(11, 7)` → đọc ngay `x = 11`.'
        ),
        # Q5 — Algebra (Easy, SPR -> 12)
        math_spr(
            'sat_mm8_m2l_q5', 5, 'Algebra', 'Linear equations in one variable', 'Easy',
            r'<p>Solve for \(x\) in the equation shown below:</p><p style="text-align:center;">\[4(x - 5) = 28\]</p>',
            r'What is the value of \(x\)?',
            ['12'], '12',
            r'Chia cả hai vế cho \(4\): \(x - 5 = 7 \Rightarrow x = 7 + 5 = 12\).',
            r'Chia trực tiếp cho hệ số \(4\) bên ngoài ngoặc giúp rút gọn ngay về phương trình một bước \(x - 5 = 7\).',
            r'Gõ `4(x - 5) = 28` trên Desmos sẽ ra ngay đường thẳng đứng `x = 12`.'
        ),
        # Q6 — Algebra (Easy, MCQ -> B)
        math_mcq(
            'sat_mm8_m2l_q6', 6, 'Algebra', 'Linear inequalities in one or two variables', 'Easy',
            r'<p>Consider the linear inequality \(3x + 8 \ge 29\).</p>',
            r'Which of the following represents all solutions to the inequality?',
            {'A': r'\(x \le 7\)', 'B': r'\(x \ge 7\)', 'C': r'\(x \ge 12\)', 'D': r'\(x \ge 21\)'},
            'B',
            r'Trừ \(8\) ở cả hai vế: \(3x \ge 21\). Chia hai vế cho \(3\) (số dương, giữ nguyên chiều bất đẳng thức): \(x \ge 7\).',
            r'Chia cho số dương \(+3\) giữ nguyên dấu \(\ge\); chỉ đổi chiều khi nhân hoặc chia cho số âm.',
            {
                'A': ('Flipped Inequality Sign', r'Đổi chiều thành \(\le\) sai vì ta chia cho số dương \(3\).'),
                'B': ('Correct', r'\(3x \ge 21 \Rightarrow x \ge 7\).'),
                'C': ('Added 8 Instead of Subtracted', r'Cộng \(29 + 8 = 37\) rồi làm tròn nhầm.'),
                'D': ('Forgot to Divide by 3', r'Dừng lại ở \(3x \ge 21\) mà quên chia cho \(3\).'),
            },
            r'Gõ `3x + 8 >= 29` trên Desmos thấy miền tô nằm bên phải đường nét liền `x = 7`.'
        ),
        # Q7 — Algebra (Easy, MCQ -> D)
        math_mcq(
            'sat_mm8_m2l_q7', 7, 'Algebra', 'Linear equations in two variables', 'Easy',
            r'<p>In the \(xy\)-plane, line \(k\) is <b>parallel</b> to the line \(y = -3x + 5\) and passes through the point \((0, -4)\).</p>',
            r'Which of the following is the equation of line \(k\)?',
            {'A': r'\(y = \frac{1}{3}x - 4\)', 'B': r'\(y = 3x - 4\)', 'C': r'\(y = -3x + 4\)', 'D': r'\(y = -3x - 4\)'},
            'D',
            r'Hai đường thẳng song song có cùng hệ số góc \(m = -3\). Đường thẳng \(k\) đi qua \((0, -4)\) nên tung độ gốc \(b = -4\). Vậy phương trình là \(y = -3x - 4\).',
            r'Song song \(\Rightarrow\) giữ nguyên hoàn toàn hệ số góc \(m = -3\) (cả dấu âm!), chỉ thay tung độ gốc \(b = -4\).',
            {
                'A': ('Perpendicular Instead of Parallel', r'Hệ số góc \(\frac{1}{3}\) là đường vuông góc, không phải song song.'),
                'B': ('Dropped Negative Sign on Slope', r'Đổi nhầm slope \(-3\) thành \(+3\).'),
                'C': ('Wrong Sign on y-Intercept', r'Tung độ gốc là \(-4\), không phải \(+4\).'),
                'D': ('Correct', r'Cùng hệ số góc \(-3\) và đi qua \((0, -4)\).'),
            },
            r'Vẽ `y = -3x + 5` và `y = -3x - 4` trên Desmos thấy hai đường song song và đi qua đúng `(0, -4)`.'
        ),
        # Q8 — Algebra (Medium, MCQ -> A) | Theme: Warehouse Conveyor Robotics
        math_mcq(
            'sat_mm8_m2l_q8', 8, 'Algebra', 'Systems of two linear equations in two variables', 'Medium',
            r'<p>An autonomous warehouse dispatches \(16\) robotic tote carts in one batch: \(x\) standard carts carrying \(30\) kilograms each and \(y\) heavy carts carrying \(50\) kilograms each. The total cargo weight of the batch is \(620\) kilograms.</p>',
            r'How many standard carts (\(x\)) are in the batch?',
            {'A': r'\(9\)', 'B': r'\(7\)', 'C': r'\(8\)', 'D': r'\(10\)'},
            'A',
            r'Lập hệ phương trình: \(x + y = 16\) và \(30x + 50y = 620\). Thế \(y = 16 - x\) vào phương trình hai: \(30x + 50(16 - x) = 620 \Rightarrow 800 - 20x = 620 \Rightarrow 20x = 180 \Rightarrow x = 9\) (và \(y = 7\)).',
            r'Kiểm tra nhanh lại đáp án \(x = 9, y = 7\): \(9 + 7 = 16\) xe và \(30(9) + 50(7) = 270 + 350 = 620\) kg chuẩn xác!',
            {
                'A': ('Correct', r'\(x = 9\) xe chuẩn và \(y = 7\) xe tải nặng.'),
                'B': ('Solved for Heavy Carts y', r'\(7\) là số xe tải nặng (\(y\)), trong khi đề hỏi số xe chuẩn (\(x\)).'),
                'C': ('Assumed Equal Split', r'Chia đều \(8\) mỗi loại cho tổng \(640 \neq 620\) kg.'),
                'D': ('Arithmetic Error', r'\(10\) xe chuẩn và \(6\) xe nặng cho tổng \(600 \neq 620\) kg.'),
            },
            r'Gõ `x + y = 16` và `30x + 50y = 620` vào Desmos → bấm giao điểm `(9, 7)` → đọc ngay `x = 9`!'
        ),
        # Q9 — Advanced Math (Easy, SPR -> 22)
        math_spr(
            'sat_mm8_m2l_q9', 9, 'Advanced Math', 'Nonlinear functions', 'Easy',
            r'<p>The quadratic function \(f\) is defined by \(f(x) = 3x^2 - 4x + 7\).</p>',
            r'What is the value of \(f(3)\)?',
            ['22'], '22',
            r'Thay \(x = 3\) vào hàm số: \(f(3) = 3(3)^2 - 4(3) + 7 = 3(9) - 12 + 7 = 27 - 12 + 7 = 22\).',
            r'Thực hiện lũy thừa \(3^2 = 9\) TRƯỚC khi nhân với hệ số \(3\) (tránh tính nhầm \((3 \times 3)^2 = 81\)).',
            r'Gõ `f(x) = 3x^2 - 4x + 7` rồi gõ `f(3)` trên Desmos ra ngay `22`.'
        ),
        # Q10 — Advanced Math (Easy, MCQ -> C)
        math_mcq(
            'sat_mm8_m2l_q10', 10, 'Advanced Math', 'Nonlinear equations in one variable and systems of equations in two variables', 'Easy',
            r'<p>Consider the quadratic equation \(x^2 - 9x + 20 = 0\).</p>',
            r'What is the <b>sum</b> of the two solutions to this equation?',
            {'A': r'\(-9\)', 'B': r'\(20\)', 'C': r'\(9\)', 'D': r'\(1\)'},
            'C',
            r'Phân tích nhân tử: \((x - 4)(x - 5) = 0 \Rightarrow x = 4\) hoặc \(x = 5\). Tổng hai nghiệm là \(4 + 5 = 9\) (hoặc áp dụng Viète \(-\frac{b}{a} = 9\)).',
            r'Tổng hai nghiệm của \(x^2 + bx + c = 0\) là \(-b\) (nhớ đảo dấu của hệ số \(-9\) thành \(+9\))!',
            {
                'A': ('Forgot Sign Flip on -b', r'\(-9\) là hệ số \(b\), tổng hai nghiệm phải là \(-b = +9\).'),
                'B': ('Product Instead of Sum', r'\(20\) là tích hai nghiệm \(4 \times 5\), không phải tổng.'),
                'C': ('Correct', r'\(4 + 5 = 9\).'),
                'D': ('Difference Instead of Sum', r'\(5 - 4 = 1\) là hiệu hai nghiệm, không phải tổng.'),
            },
            r'Vẽ `y = x^2 - 9x + 20` trên Desmos thấy 2 nghiệm trục Ox là `4` và `5` → tổng bằng `9`.'
        ),
        # Q11 — Advanced Math (Easy, MCQ -> B)
        math_mcq(
            'sat_mm8_m2l_q11', 11, 'Advanced Math', 'Equivalent expressions', 'Easy',
            r'<p>Which of the following expressions is equivalent to \((2x^3)^4\)?</p>',
            r'Select the simplified equivalent expression.',
            {'A': r'\(8x^{12}\)', 'B': r'\(16x^{12}\)', 'C': r'\(16x^7\)', 'D': r'\(2x^{12}\)'},
            'B',
            r'Áp dụng quy tắc lũy thừa: \((2x^3)^4 = 2^4 \cdot (x^3)^4 = 16x^{3 \cdot 4} = 16x^{12}\).',
            r'Phải nâng cả hệ số \(2^4 = 16\) lên lũy thừa \(4\) và NHÂN các số mũ \(3 \times 4 = 12\)!',
            {
                'A': ('Multiplied 2 × 4 Instead of 2⁴', r'Hệ số \(2\) phải lấy mũ \(4\) ra \(16\), không phải \(2 \times 4 = 8\).'),
                'B': ('Correct', r'\(2^4 x^{3 \cdot 4} = 16x^{12}\).'),
                'C': ('Added Exponents 3 + 4', r'Lũy thừa của lũy thừa phải nhân số mũ \(3 \times 4 = 12\), không cộng \(3 + 4 = 7\).'),
                'D': ('Forgot to Raise Coefficient 2', r'Quên tính \(2^4 = 16\), giữ nguyên hệ số \(2\).'),
            },
            r'Thử `x = 2` trên Desmos: `(2 * 2^3)^4 = 65536`, chỉ phương án B (`16 * 2^12 = 65536`) trùng khớp!'
        ),
        # Q12 — Advanced Math (Easy, MCQ -> D) | Theme: National Park Wildlife Census
        math_mcq(
            'sat_mm8_m2l_q12', 12, 'Advanced Math', 'Nonlinear functions', 'Easy',
            r'<p>A national park biologist models the population \(B(t)\) of a protected beaver colony \(t\) years after monitoring begins using the function \(B(t) = 140(1.08)^t\).</p>',
            r'According to the model, what was the initial beaver population when monitoring began (\(t = 0\))?',
            {'A': r'\(1.08\)', 'B': r'\(8\)', 'C': r'\(151.2\)', 'D': r'\(140\)'},
            'D',
            r'Tại thời điểm ban đầu \(t = 0\): \(B(0) = 140(1.08)^0 = 140 \times 1 = 140\) cá thể.',
            r'Trong mô hình hàm mũ \(y = a \cdot b^t\), hệ số \(a\) đứng phía trước luôn là giá trị ban đầu tại \(t = 0\).',
            {
                'A': ('Growth Factor Trap', r'\(1.08\) là hệ số tăng trưởng mỗi năm, không phải dân số ban đầu.'),
                'B': ('Percent Rate Trap', r'\(8\%\) là tỉ lệ tăng hàng năm.'),
                'C': ('Evaluated at t = 1', r'\(151.2\) là dân số sau \(1\) năm (\(t = 1\)), không phải lúc ban đầu.'),
                'D': ('Correct', r'\(B(0) = 140\).'),
            },
            r'Gõ `140 * 1.08^0` trên Desmos xác nhận ngay `140`.'
        ),
        # Q13 — Advanced Math (Easy-Medium, SPR -> 14)
        math_spr(
            'sat_mm8_m2l_q13', 13, 'Advanced Math', 'Nonlinear functions', 'Easy',
            r'<p>Consider the quadratic equation written in vertex form:</p><p style="text-align:center;">\[y = 2(x - 6)^2 + 14\]</p>',
            r'What is the <b>minimum</b> value of \(y\)?',
            ['14'], '14',
            r'Vì \(2(x - 6)^2 \ge 0\) với mọi số thực \(x\), nên \(y \ge 14\). Giá trị nhỏ nhất của \(y\) bằng \(14\), đạt tại đỉnh \(x = 6\).',
            r'Trong dạng đỉnh \(y = a(x - h)^2 + k\) với \(a > 0\), giá trị nhỏ nhất của \(y\) luôn là tung độ đỉnh \(k\) (đừng nhập nhầm hoành độ \(h = 6\))!',
            r'Vẽ `y = 2(x - 6)^2 + 14` trên Desmos → bấm điểm thấp nhất `(6, 14)` → giá trị nhỏ nhất của `y` là `14`.'
        ),
        # Q14 — Advanced Math (Easy, MCQ -> A)
        math_mcq(
            'sat_mm8_m2l_q14', 14, 'Advanced Math', 'Equivalent expressions', 'Easy',
            r'<p>Which of the following expressions is equivalent to \((x - 6)(x + 4)\)?</p>',
            r'Select the expanded quadratic expression.',
            {'A': r'\(x^2 - 2x - 24\)', 'B': r'\(x^2 + 2x - 24\)', 'C': r'\(x^2 - 2x + 24\)', 'D': r'\(x^2 - 10x - 24\)'},
            'A',
            r'Nhân phân phối (FOIL): \((x - 6)(x + 4) = x^2 + 4x - 6x - 24 = x^2 - 2x - 24\).',
            r'Hệ số của \(x\) là tổng \((-6) + 4 = -2\), còn hằng số tự do là tích \((-6) \times 4 = -24\).',
            {
                'A': ('Correct', r'\(x^2 + 4x - 6x - 24 = x^2 - 2x - 24\).'),
                'B': ('Wrong Sign on Middle Term', r'\(-6 + 4 = -2\), không phải \(+2\).'),
                'C': ('Wrong Sign on Constant', r'\((-6)(4) = -24\), không phải \(+24\).'),
                'D': ('Subtracted Both Terms', r'Nhầm \(-6 - 4 = -10\) thay vì \(-6 + 4 = -2\).'),
            },
            r'Vẽ `y = (x - 6)(x + 4)` và `y = x^2 - 2x - 24` trên Desmos để thấy hai đồ thị trùng khít hoàn toàn.'
        ),
        # Q15 — Advanced Math (Medium, MCQ -> C)
        math_mcq(
            'sat_mm8_m2l_q15', 15, 'Advanced Math', 'Equivalent expressions', 'Medium',
            r'<p>Consider the polynomial expression shown below:</p><p style="text-align:center;">\[(5x^2 - 3x + 8) - (2x^2 - 7x + 3)\]</p>',
            r'Which of the following is equivalent to the given expression?',
            {'A': r'\(3x^2 - 10x + 5\)', 'B': r'\(3x^2 + 4x + 11\)', 'C': r'\(3x^2 + 4x + 5\)', 'D': r'\(7x^2 - 10x + 11\)'},
            'C',
            r'Phá ngoặc và đổi dấu TẤT CẢ các số hạng trong ngoặc thứ hai: \(5x^2 - 3x + 8 - 2x^2 + 7x - 3 = (5 - 2)x^2 + (-3 + 7)x + (8 - 3) = 3x^2 + 4x + 5\).',
            r'Khi trừ một đa thức trong ngoặc, nhớ phân phối dấu trừ vào TỪNG hạng tử: \(-(-7x) = +7x\) và \(-(+3) = -3\)!',
            {
                'A': ('Forgot to Flip Sign on -7x', r'Tính nhầm \(-3x - 7x = -10x\) thay vì \(-3x + 7x = +4x\).'),
                'B': ('Forgot to Flip Sign on +3', r'Cộng nhầm \(8 + 3 = 11\) thay vì \(8 - 3 = 5\).'),
                'C': ('Correct', r'\(3x^2 + 4x + 5\).'),
                'D': ('Added Instead of Subtracted', r'Cộng hai đa thức thay vì trừ.'),
            },
            r'Thay nhanh `x = 1` trên Desmos: `(5 - 3 + 8) - (2 - 7 + 3) = 10 - (-2) = 12`. Chỉ phương án C cho `3 + 4 + 5 = 12`!'
        ),
        # Q16 — PSDA (Easy, SPR -> 210) | Theme: Geothermal Power Wells
        math_spr(
            'sat_mm8_m2l_q16', 16, 'Problem-Solving and Data Analysis', 'Ratios, rates, proportional relationships, and units', 'Easy',
            r'<p>A geothermal power turbine generates \(84\) megawatt-hours (MWh) of electricity in \(12\) hours while operating at a constant rate.</p>',
            r'At this same constant rate, how many megawatt-hours of electricity will the turbine generate in \(30\) hours?',
            ['210'], '210',
            r'Tính công suất mỗi giờ: \(\frac{84}{12} = 7\text{ MWh/giờ}\). Trong \(30\) giờ, tua-bin phát ra: \(7 \times 30 = 210\text{ MWh}\).',
            r'Tìm tốc độ đơn vị (unit rate) cho \(1\) giờ trước, rồi nhân với số giờ đề yêu cầu.',
            r'Gõ `(84 / 12) * 30` trên Desmos ra ngay `210`.'
        ),
        # Q17 — PSDA (Easy, MCQ -> D) | Theme: Violin Luthier Wood Curing
        math_mcq(
            'sat_mm8_m2l_q17', 17, 'Problem-Solving and Data Analysis', 'Percentages', 'Easy',
            r'<p>A tonewood supplier inspects \(320\) cured spruce soundboard planks and approves \(65\%\) of them for concert-grade violin production.</p>',
            r'How many of the inspected planks are approved for concert-grade violin production?',
            {'A': r'\(112\)', 'B': r'\(192\)', 'C': r'\(224\)', 'D': r'\(208\)'},
            'D',
            r'Số tấm gỗ đạt chuẩn là: \(65\% \times 320 = 0.65 \times 320 = 208\) tấm.',
            r'Chuyển phần trăm sang số thập phân (\(65\% = 0.65\)) rồi nhân trực tiếp với tổng \(320\).',
            {
                'A': ('Computed Rejected 35%', r'\(112 = 35\% \times 320\) là số tấm bị loại, không phải số tấm đạt chuẩn.'),
                'B': ('Used 60% Instead of 65%', r'\(0.60 \times 320 = 192\).'),
                'C': ('Used 70% Instead of 65%', r'\(0.70 \times 320 = 224\).'),
                'D': ('Correct', r'\(0.65 \times 320 = 208\).'),
            },
            r'Gõ `0.65 * 320` trên Desmos ra ngay `208`.'
        ),
        # Q18 — PSDA (Medium, MCQ -> A) | Theme: National Park Wildlife Census (Table)
        math_mcq(
            'sat_mm8_m2l_q18', 18, 'Problem-Solving and Data Analysis', 'One-variable data: Distributions and measures of center and spread', 'Medium',
            tbl_q18 + r'<p>The table above shows the number of mountain goats sighted each day over a \(7\)-day national park wildlife survey.</p>',
            r'What is the <b>median</b> number of mountain goats sighted per day during this \(7\)-day survey?',
            {'A': r'\(19\)', 'B': r'\(11\)', 'C': r'\(16\)', 'D': r'\(21\)'},
            'A',
            r'Sắp xếp \(7\) số liệu theo thứ tự tăng dần: \(11, 14, 17, \mathbf{19}, 21, 23, 27\). Giá trị chính giữa (vị trí thứ \(4\)) là \(19\).',
            r'LUÔN sắp xếp dữ liệu theo thứ tự tăng dần trước khi lấy giá trị ở giữa — tuyệt đối không chọn ngay cột thứ 4 trong bảng (Thursday = 11)!',
            {
                'A': ('Correct', r'Sau khi sắp tăng dần, số đứng thứ \(4\) là \(19\).'),
                'B': ('Forgot to Sort Table', r'\(11\) là cột thứ \(4\) (thứ Năm) khi CHƯA sắp xếp thứ tự!'),
                'C': ('Computed Range Instead of Median', r'\(27 - 11 = 16\) là khoảng biến thiên (range), không phải trung vị.'),
                'D': ('Picked 5th Ordered Value', r'\(21\) là số lớn thứ \(5\), không phải vị trí chính giữa thứ \(4\).'),
            },
            r'Gõ `median(14, 23, 19, 11, 27, 17, 21)` trên Desmos ra ngay chính xác `19`!'
        ),
        # Q19 — PSDA (Medium, SPR -> 3/10) | Theme: Warehouse Conveyor Robotics (Table)
        math_spr(
            'sat_mm8_m2l_q19', 19, 'Problem-Solving and Data Analysis', 'Probability and conditional probability', 'Medium',
            tbl_q19 + r'<p>The table above classifies \(150\) packages routed by an autonomous warehouse conveyor system across two sorting lanes.</p>',
            r'If one package is selected at random from all \(150\) packages, what is the probability that the selected package was <b>Delayed</b>? <em>(Express your answer as a fraction or decimal.)</em>',
            ['3/10', '0.3', '.3'], '3/10 (or 0.3)',
            r'Tổng số kiện hàng bị trễ (Delayed) ở cả hai làn là \(18 + 27 = 45\). Tổng toàn bộ kiện hàng là \(150\). Xác suất cần tìm: \(\frac{45}{150} = \frac{3}{10} = 0.3\).',
            r'Đọc kỹ mẫu số là "from all 150 packages" (tổng toàn bảng) và tử số là tổng cột Delayed (\(45\)).',
            r'Gõ `45/150` trên Desmos đọc ngay `0.3`, hoặc bấm nút phân số để ra `3/10`.'
        ),
        # Q20 — Geometry (Easy, MCQ -> C) | SVG Right Triangle
        math_mcq(
            'sat_mm8_m2l_q20', 20, 'Geometry and Trigonometry', 'Lines, angles, and triangles', 'Easy',
            f'<div style="text-align:center;margin-bottom:10px;">{svg_q20}</div>' + r'<p>In right triangle \(ABC\) shown above, \(\angle B = 90^\circ\) and \(\angle A = 34^\circ\).</p>',
            r'What is the value of \(x\)?',
            {'A': r'\(34\)', 'B': r'\(66\)', 'C': r'\(56\)', 'D': r'\(146\)'},
            'C',
            r'Tổng ba góc trong tam giác bằng \(180^\circ\). Trong tam giác vuông tại \(B\), hai góc nhọn phụ nhau: \(x = 90 - 34 = 56\).',
            r'Trong tam giác vuông, hai góc nhọn luôn cộng lại bằng \(90^\circ\)!',
            {
                'A': ('Copied Angle A', r'Hai góc nhọn chỉ bằng nhau khi tam giác vuông cân (\(45^\circ\)).'),
                'B': ('Subtracted from 100', r'Tính nhầm \(100 - 34 = 66\) thay vì \(90 - 34\).'),
                'C': ('Correct', r'\(90 - 34 = 56\).'),
                'D': ('Forgot Right Angle 90°', r'Lấy \(180 - 34 = 146\) mà quên trừ góc vuông \(90^\circ\).'),
            },
            r'Gõ `90 - 34` trên Desmos ra ngay `56`.'
        ),
        # Q21 — Geometry (Easy-Medium, MCQ -> B) | SVG Similar Triangles | Theme: Stepped-Pyramid Monument
        math_mcq(
            'sat_mm8_m2l_q21', 21, 'Geometry and Trigonometry', 'Lines, angles, and triangles', 'Medium',
            f'<div style="text-align:center;margin-bottom:10px;">{svg_q21}</div>' + r'<p>Two triangular stone support brackets used on a stepped-pyramid monument, \(\triangle ABC\) and \(\triangle DEF\), are similar, where vertices \(A, B, C\) correspond to \(D, E, F\), respectively. Given \(AB = 6\) feet, \(BC = 10\) feet, and \(DE = 15\) feet.</p>',
            r'What is the length of side \(EF\) (\(x\)), in feet?',
            {'A': r'\(19\)', 'B': r'\(25\)', 'C': r'\(20\)', 'D': r'\(4\)'},
            'B',
            r'Vì \(\triangle ABC \sim \triangle DEF\), các cặp cạnh tương ứng tỉ lệ với nhau: \(\frac{EF}{BC} = \frac{DE}{AB} \Rightarrow \frac{x}{10} = \frac{15}{6} = 2.5 \Rightarrow x = 10 \times 2.5 = 25\) feet.',
            r'Tam giác đồng dạng phóng đại theo PHÉP NHÂN tỉ số (\(\times 2.5\)), tuyệt đối không cộng hiệu \(15 - 6 = +9\) vào cạnh kia!',
            {
                'A': ('Additive Scaling Trap', r'Cộng nhầm \(10 + (15 - 6) = 19\) thay vì nhân tỉ lệ đồng dạng \(2.5\).'),
                'B': ('Correct', r'\(x = 10 \times \frac{15}{6} = 25\) feet.'),
                'C': ('Doubled Instead of ×2.5', r'Nhân nhầm tỉ số \(2\) thay vì \(2.5\).'),
                'D': ('Inverted Ratio Trap', r'Lấy ngược \(10 \times \frac{6}{15} = 4\), nhỏ hơn cả tam giác gốc.'),
            },
            r'Gõ `10 * (15 / 6)` trên Desmos ra ngay `25`.'
        ),
        # Q22 — Geometry (Medium, SPR -> 180) | SVG Cylinder | Theme: Geothermal Power Wells
        math_spr(
            'sat_mm8_m2l_q22', 22, 'Geometry and Trigonometry', 'Area and volume', 'Medium',
            f'<div style="text-align:center;margin-bottom:10px;">{svg_q22}</div>' + r'<p>A right circular cylindrical geothermal brine storage tank has a base radius of \(6\) meters and a height of \(5\) meters, as shown above.</p>',
            r'If the volume of the cylindrical tank is \(v\pi\) cubic meters, what is the value of \(v\)?',
            ['180'], '180',
            r'Áp dụng công thức thể tích hình trụ (có sẵn trên SAT Reference Sheet): \(V = \pi r^2 h = \pi (6^2)(5) = 36 \times 5\pi = 180\pi\text{ m}^3\). Suy ra \(v = 180\).',
            r'Nhớ bình phương bán kính \(r^2 = 6^2 = 36\) rồi mới nhân chiều cao \(h = 5\), và không gõ ký hiệu \(\pi\) vào ô kết quả!',
            r'Gõ `6^2 * 5` trên Desmos ra ngay `180`.'
        ),
    ]


if __name__ == '__main__':
    assert verify_math()
    qs = get_m2l_questions()
    print(f"M2L verified: {len(qs)} questions")
