# -*- coding: utf-8 -*-
"""
Digital SAT Math Adaptive Mock Test #6 — Module 1 (Routing Module, 22 Questions)
Themes: Coral nursery aquaculture, commercial drone delivery networks, digital printmaking studios,
seismology & tectonic monitoring stations, spherical & conical observatory domes.
Blueprint: 8 Algebra (Q1-Q8), 7 Advanced Math (Q9-Q15), 4 PSDA (Q16-Q19), 3 Geometry/Trig (Q20-Q22).
Format: 16 MCQ (A:4, B:4, C:4, D:4) + 6 SPR (Q5, Q9, Q13, Q16, Q19, Q22).
"""

from fractions import Fraction
import math
from sat_math_helpers import (
    math_mcq, math_spr, build_math_table,
    svg_parabola_vertex, svg_parallel_transversal,
    svg_circle_sector, svg_right_triangle
)


def verify_math():
    """Programmatic exact arithmetic verification for all 22 Module 1 questions."""
    # Q1: 4(3x - 5) + 11 = 5x + 12 => 7x = 21 => x = 3 => 2x + 7 = 13
    x1 = Fraction(12 + 20 - 11, 12 - 5)
    assert x1 == 3 and 4 * (3 * x1 - 5) + 11 == 5 * x1 + 12 and 2 * x1 + 7 == 13

    # Q2: B(d) = 420 - 18d => slope -18 (decreases by 18 Wh per km)
    b2 = lambda d: 420 - 18 * d
    assert b2(0) == 420 and b2(1) - b2(0) == -18

    # Q3: Linear V(3)=29, V(7)=53, V(11)=77 => m=6, b=11 => V(15)=101
    m3 = Fraction(53 - 29, 7 - 3)
    b3 = 29 - m3 * 3
    assert m3 == 6 and b3 == 11 and m3 * 11 + b3 == 77 and m3 * 15 + b3 == 101

    # Q4: 4x + 3y = 58, x - 2y = -2 => x = 10, y = 6 => 3x - y = 24
    y4 = Fraction(58 + 8, 11)
    x4 = 2 * y4 - 2
    assert x4 == 10 and y4 == 6 and 4 * x4 + 3 * y4 == 58 and x4 - 2 * y4 == -2 and 3 * x4 - y4 == 24

    # Q5: 9x + 6y = 24, kx - 12y = 30 no solution => k/9 = -12/6 = -2 => k = -18
    k5 = Fraction(9 * (-12), 6)
    assert k5 == -18 and Fraction(30, 24) != Fraction(-12, 6)

    # Q6: 4x - 3y = 18 => m = 4/3 => perp m = -3/4 through (8, -1) => y = (-3/4)x + 5
    m6_orig = Fraction(4, 3)
    m6_perp = Fraction(-3, 4)
    b6 = -1 - m6_perp * 8
    assert m6_orig * m6_perp == -1 and b6 == 5 and m6_perp * 8 + b6 == -1

    # Q7: 110(9) + 45v <= 1650 => 45v <= 660 => v <= 44/3 => max int 14
    v7_max = Fraction(1650 - 110 * 9, 45)
    assert v7_max == Fraction(44, 3) and 110 * 9 + 45 * 14 <= 1650 and 110 * 9 + 45 * 15 > 1650

    # Q8: 5a + 2b = 43, a + 4b = 29 => 6a + 6b = 72 => a + b = 12
    a8, b8 = Fraction(19, 3), Fraction(17, 3)
    assert 5 * a8 + 2 * b8 == 43 and a8 + 4 * b8 == 29 and a8 + b8 == 12

    # Q9: f(x) = a(x - 5)^2 + 4, f(3) = 16, f(7) = 16 => a = 3 => f(8) = 31
    a9 = Fraction(16 - 4, (7 - 5) ** 2)
    f9 = lambda x: a9 * (x - 5) ** 2 + 4
    assert a9 == 3 and f9(3) == 16 and f9(7) == 16 and f9(8) == 31

    # Q10: 3x^2 - 18x + k = 0 one real solution => (-18)^2 - 12k = 0 => k = 27
    k10 = Fraction((-18) ** 2, 4 * 3)
    assert k10 == 27 and (-18) ** 2 - 4 * 3 * k10 == 0

    # Q11: 2/(x-4) + 5/(x+1) == (7x - 18)/(x^2 - 3x - 4)
    for xv in (5, 7, 10):
        lhs = Fraction(2, xv - 4) + Fraction(5, xv + 1)
        rhs = Fraction(7 * xv - 18, xv ** 2 - 3 * xv - 4)
        assert lhs == rhs

    # Q12: A(t) = 65 * (1.18)^t => 18% monthly increase
    assert Fraction(118, 100) - 1 == Fraction(18, 100)

    # Q13: 4x^2 - 18x + 11 = 0 => Delta = 148 > 0, sum = 18/4 = 9/2 = 4.5
    assert (-18) ** 2 - 4 * 4 * 11 == 148 > 0 and Fraction(18, 4) == Fraction(9, 2)

    # Q14: sqrt(5x + 11) = x + 1 => x = 5 valid, x = -2 extraneous
    assert math.isclose(math.sqrt(5 * 5 + 11), 5 + 1) and (-2 + 1) < 0 and (5 ** 2 - 3 * 5 - 10 == 0)

    # Q15: V = (1/3)*pi*r^2*h => r = sqrt(3V/(pi*h))
    r15_test, h15_test = Fraction(6), Fraction(5)
    v15_over_pi = Fraction(1, 3) * (r15_test ** 2) * h15_test
    assert Fraction(3) * v15_over_pi / h15_test == r15_test ** 2

    # Q16: 2160 in^2 / 144 = 15 ft^2
    assert Fraction(2160, 12 ** 2) == 15

    # Q17: P(Delayed | Windy) = 24 / 80 = 3/10
    assert 108 + 12 == 120 and 56 + 24 == 80 and 120 + 80 == 200 and Fraction(24, 80) == Fraction(3, 10)

    # Q18: [14,17,19,21,22,24,25] -> [14,17,19,21,22,24,67] => mean +6, median unchanged (21)
    d18_old = [14, 17, 19, 21, 22, 24, 25]
    d18_new = [14, 17, 19, 21, 22, 24, 67]
    assert Fraction(sum(d18_new), 7) - Fraction(sum(d18_old), 7) == 6
    assert d18_old[3] == d18_new[3] == 21

    # Q19: p = 120% of q, q = 45% of r => p = 54% of r
    assert Fraction(120, 100) * Fraction(45, 100) == Fraction(54, 100)

    # Q20: 4x + 12 = 6x - 32 => x = 22 => obtuse = 100 => acute = 80
    x20 = Fraction(32 + 12, 6 - 4)
    obtuse20 = 4 * x20 + 12
    assert x20 == 22 and obtuse20 == 6 * x20 - 32 == 100 and 180 - obtuse20 == 80

    # Q21: r = 18, angle = 70 deg => arc length = (70/360) * 2 * 18 * pi = 7*pi
    assert Fraction(70, 360) * 2 * 18 == 7

    # Q22: Right triangle PQR, PR = 52, cos(R) = 12/13 => QR = 48, PQ = 20
    qr22 = 52 * Fraction(12, 13)
    pq22_sq = 52 ** 2 - int(qr22) ** 2
    assert qr22 == 48 and pq22_sq == 20 ** 2

    return True


def get_m1_questions():
    tbl_q3 = build_math_table(
        ['Day \\(t\\)', 'Cumulative Calcium Additive \\(V(t)\\) (mL)'],
        [
            ['3', '29'],
            ['7', '53'],
            ['11', '77'],
        ],
        caption='Coral Nursery Automated Dosing Log'
    )
    svg_q9 = svg_parabola_vertex(
        h_lbl='5', k_lbl='4', opens_up=True, pt_lbl='(7, 16)',
        note='Note: Figure not drawn to scale.'
    )
    tbl_q17 = build_math_table(
        ['Weather Condition', 'On-Time', 'Delayed', 'Total'],
        [
            ['Clear', '108', '12', '120'],
            ['Windy', '56', '24', '80'],
            ['Total', '164', '36', '200'],
        ],
        caption='Commercial Drone Delivery Dispatch Summary'
    )
    tbl_q18 = build_math_table(
        ['Day', '1', '2', '3', '4', '5', '6', '7'],
        [
            ['Recorded Micro-Tremors', '14', '17', '19', '21', '22', '24', '25'],
        ],
        caption='Weekly Micro-Tremor Counts at Tectonic Station #4'
    )
    svg_q20 = svg_parallel_transversal(
        line1='f₁', line2='f₂',
        ang1_lbl='(4x + 12)°', ang2_lbl='(6x − 32)°', ang3_lbl='',
        note='Parallel fault lines f₁ ∥ f₂ (not drawn to scale).'
    )
    svg_q21 = svg_circle_sector(
        radius_lbl='18 m', angle_lbl='70°', center_lbl='O', pt_a='A', pt_b='B',
        note='Observatory Dome Aperture Sector (not drawn to scale).'
    )
    svg_q22 = svg_right_triangle(
        a_lbl='PQ', b_lbl='QR', c_lbl='52',
        angle_bottom_right='R', v_top='P', v_right_angle='Q', v_right='R',
        note='cos(R) = 12/13'
    )

    return [
        # Q1 — Algebra (Easy, MCQ -> B)
        math_mcq(
            'sat_mm6_m1_q1', 1, 'Algebra', 'Linear equations in one variable', 'Easy',
            r'<p>A digital printmaking studio calibrates its ink-flow pressure \(x\) using the linear equation below:</p><p style="text-align:center;font-size:18px;">\[4(3x - 5) + 11 = 5x + 12\]</p>',
            r'What is the value of \(2x + 7\)?',
            {'A': r'\(3\)', 'B': r'\(13\)', 'C': r'\(10\)', 'D': r'\(19\)'},
            'B',
            r'Khai triển vế trái: \(12x - 20 + 11 = 5x + 12 \Rightarrow 12x - 9 = 5x + 12 \Rightarrow 7x = 21 \Rightarrow x = 3\). Đề bài yêu cầu tính giá trị của \(2x + 7\), thay \(x = 3\) ta được \(2(3) + 7 = 13\).',
            r'Luôn đọc kỹ biểu thức đề hỏi (\(2x + 7\)) thay vì dừng ngay sau khi tìm ra \(x = 3\)!',
            {
                'A': ('Dừng ở giá trị x', r'\(3\) mới là nghiệm \(x\), chưa thay vào biểu thức \(2x + 7\).'),
                'B': ('Đáp án đúng', r'\(x = 3 \Rightarrow 2(3) + 7 = 13\).'),
                'C': ('Quên nhân 2 với x', r'Tính nhầm \(x + 7 = 3 + 7 = 10\) thay vì \(2x + 7\).'),
                'D': ('Sai dấu hằng số -20 + 11', r'Tính nhầm \(-20 + 11 = -31\) dẫn đến sai nghiệm \(x\).'),
            },
            r'Gõ trực tiếp `4(3x - 5) + 11 = 5x + 12` vào Desmos để đọc đường đứng `x = 3`, sau đó gõ `2(3) + 7` ra ngay `13`.'
        ),
        # Q2 — Algebra (Easy, MCQ -> A)
        math_mcq(
            'sat_mm6_m1_q2', 2, 'Algebra', 'Linear functions', 'Easy',
            r'<p>A commercial drone delivery network models the remaining battery charge \(B(d)\), in watt-hours, of a courier quadcopter after flying \(d\) kilometers with a standard parcel by the function:</p><p style="text-align:center;">\[B(d) = 420 - 18d\]</p>',
            r'Which of the following is the best interpretation of the number \(18\) in this context?',
            {
                'A': r"The drone's remaining battery charge decreases by \(18\) watt-hours for each kilometer flown.",
                'B': r"The drone's initial battery charge before takeoff is \(18\) watt-hours.",
                'C': r'The maximum distance the drone can fly on a full battery is \(18\) kilometers.',
                'D': r'The drone carries a standard parcel weighing \(18\) kilograms.',
            },
            'A',
            r'Trong hàm bậc nhất \(B(d) = 420 - 18d\), hệ số góc (slope) là \(-18\), cho biết mỗi khi quãng đường \(d\) tăng thêm \(1\) km thì mức pin còn lại \(B(d)\) giảm đi \(18\) watt-hours. Còn \(420\) là dung lượng pin ban đầu tại \(d = 0\).',
            r'Trong \(y = b - mx\), hệ số gắn với biến \(x\) luôn là tốc độ thay đổi trên mỗi đơn vị (per kilometer / each additional unit), còn dấu trừ biểu thị sự suy giảm.',
            {
                'A': ('Đáp án đúng', r'Mô tả chính xác ý nghĩa hệ số góc \(-18\): giảm \(18\) watt-hours cho mỗi km bay.'),
                'B': ('Nhầm với tung độ gốc', r'Dung lượng pin ban đầu trước khi cất cánh là \(420\) watt-hours, không phải \(18\).'),
                'C': ('Nhầm với hoành độ gốc', r'Quãng đường tối đa là \(420/18 \approx 23.3\) km, không phải \(18\) km.'),
                'D': ('Sai đại lượng vật lý', r'Hàm mô tả năng lượng pin (watt-hours) theo quãng đường (km), không liên quan khối lượng gói hàng.'),
            },
            r'Câu đọc hiểu ý nghĩa hệ số góc — kiểm tra nhanh `B(0) = 420` và `B(1) = 402` thấy giảm đúng `18` watt-hours mỗi km.'
        ),
        # Q3 — Algebra (Easy, MCQ -> D)
        math_mcq(
            'sat_mm6_m1_q3', 3, 'Algebra', 'Linear functions', 'Easy',
            tbl_q3 + r'<p>The table above shows the cumulative volume of liquid calcium additive \(V(t)\), in milliliters, dispensed into a coral nursery frag tank after \(t\) days. The relationship between \(t\) and \(V(t)\) is linear.</p>',
            r'According to the linear model, what is the value of \(V(15)\)?',
            {'A': r'\(83\)', 'B': r'\(90\)', 'C': r'\(95\)', 'D': r'\(101\)'},
            'D',
            r'Tính tốc độ châm dung dịch mỗi ngày (hệ số góc): \(m = \frac{53 - 29}{7 - 3} = \frac{24}{4} = 6\text{ mL/ngày}\). Từ ngày \(t = 11\) đến \(t = 15\) tăng thêm \(4\) ngày, nên thể tích tăng thêm đúng \(6 \times 4 = 24\text{ mL}\): \(V(15) = 77 + 24 = 101\). (Hoặc viết \(V(t) = 6t + 11 \Rightarrow V(15) = 101\).)',
            r'Mẹo bước nhảy đều của hàm bậc nhất: cứ tăng \(4\) ngày thì \(V(t)\) tăng \(24\text{ mL}\) (\(29 \to 53 \to 77 \to 101\)) — tính nhẩm 3 giây!',
            {
                'A': ('Chỉ cộng thêm 1 ngày', r'Cộng \(77 + 6 = 83\) thay vì cộng cho \(4\) ngày (\(24\)).'),
                'B': ('Quên tung độ gốc b = 11', r'Tính \(6 \times 15 = 90\) mà quên cộng giá trị ban đầu \(b = 11\).'),
                'C': ('Nhầm số ngày tăng thêm', r'Cộng \(77 + 18 = 95\) (nhầm tăng 3 ngày thay vì 4 ngày).'),
                'D': ('Đáp án đúng', r'\(V(15) = 77 + 24 = 101\).'),
            },
            r'Nhập Table `x1 = [3, 7, 11]`, `y1 = [29, 53, 77]` vào Desmos, gõ `y1 ~ m x1 + b` ra `m = 6, b = 11`, rồi tính `6(15) + 11 = 101`.'
        ),
        # Q4 — Algebra (Medium, MCQ -> C)
        math_mcq(
            'sat_mm6_m1_q4', 4, 'Algebra', 'Systems of two linear equations in two variables', 'Medium',
            r'<p>In a digital printmaking studio, the costs \(x\) and \(y\), in dollars, of two specialty pigment cartridges satisfy the system of equations below:</p><p style="text-align:center;">\[\begin{cases} 4x + 3y = 58 \\ x - 2y = -2 \end{cases}\]</p>',
            r'What is the value of \(3x - y\)?',
            {'A': r'\(16\)', 'B': r'\(20\)', 'C': r'\(24\)', 'D': r'\(36\)'},
            'C',
            r'Từ phương trình thứ hai: \(x = 2y - 2\). Thế vào phương trình thứ nhất: \(4(2y - 2) + 3y = 58 \Rightarrow 8y - 8 + 3y = 58 \Rightarrow 11y = 66 \Rightarrow y = 6\). Suy ra \(x = 2(6) - 2 = 10\). Khi đó \(3x - y = 3(10) - 6 = 24\).',
            r'Thế nhanh \(x = 2y - 2\) hoặc vẽ hai đường thẳng trên Desmos để chốt tọa độ \((10, 6)\) rồi tính biểu thức \(3x - y\).',
            {
                'A': ('Tính x + y', r'\(10 + 6 = 16\), đọc nhầm yêu cầu đề bài.'),
                'B': ('Nhầm tính 2x', r'\(2(10) = 20\), quên trừ \(y\) hoặc nhân sai hệ số.'),
                'C': ('Đáp án đúng', r'\(x = 10, y = 6 \Rightarrow 3(10) - 6 = 24\).'),
                'D': ('Cộng thay vì trừ y', r'Tính \(3(10) + 6 = 36\) thay vì \(3(10) - 6 = 24\).'),
            },
            r'Gõ `4x + 3y = 58` và `x - 2y = -2` vào Desmos → bấm giao điểm `(10, 6)` → gõ `3(10) - 6` ra `24`.'
        ),
        # Q5 — Algebra (Medium, SPR -> -18)
        math_spr(
            'sat_mm6_m1_q5', 5, 'Algebra', 'Systems of two linear equations in two variables', 'Medium',
            r'<p>Consider the system of linear equations below, where \(k\) is a constant:</p><p style="text-align:center;">\[\begin{cases} 9x + 6y = 24 \\ kx - 12y = 30 \end{cases}\]</p>',
            r'If the system has <b>no solution</b>, what is the value of \(k\)?',
            ['-18'], '-18',
            r'Hệ hai phương trình bậc nhất vô nghiệm khi và chỉ khi hai đường thẳng song song nhưng không trùng nhau, tức \(\dfrac{k}{9} = \dfrac{-12}{6} \ne \dfrac{30}{24}\). Giải tỉ lệ hệ số: \(\dfrac{k}{9} = -2 \Rightarrow k = -18\). Kiểm tra vế phải: \(\dfrac{30}{24} = \dfrac{5}{4} \ne -2\) (thỏa mãn vô nghiệm!).',
            r'Hệ vô nghiệm \(\Leftrightarrow \dfrac{a_1}{a_2} = \dfrac{b_1}{b_2} \ne \dfrac{c_1}{c_2}\) — chú ý dấu âm của \(-12y\) để không sai dấu \(k\)!',
            r'Gõ `9x + 6y = 24` và `kx - 12y = 30` vào Desmos, thêm thanh trượt `k` (từ `-25` đến `25`) → tại `k = -18`, hai đường thẳng song song hoàn toàn!'
        ),
        # Q6 — Algebra (Medium, MCQ -> D)
        math_mcq(
            'sat_mm6_m1_q6', 6, 'Algebra', 'Linear equations in two variables', 'Medium',
            r'<p>In the \(xy\)-plane, line \(p\) is defined by the equation \(4x - 3y = 18\). Line \(q\) is <b>perpendicular</b> to line \(p\) and passes through the point \((8, -1)\).</p>',
            r'Which of the following is an equation of line \(q\)?',
            {
                'A': r'\(y = \frac{3}{4}x - 7\)',
                'B': r'\(y = \frac{4}{3}x - \frac{35}{3}\)',
                'C': r'\(y = -\frac{4}{3}x + \frac{29}{3}\)',
                'D': r'\(y = -\frac{3}{4}x + 5\)',
            },
            'D',
            r'Đưa đường thẳng \(p\) về dạng slope-intercept: \(3y = 4x - 18 \Rightarrow y = \frac{4}{3}x - 6\), có hệ số góc \(m_p = \frac{4}{3}\). Đường thẳng \(q\) vuông góc với \(p\) nên có hệ số góc nghịch đảo đổi dấu: \(m_q = -\frac{3}{4}\). Thay điểm \((8, -1)\) vào \(y = -\frac{3}{4}x + b\): \(-1 = -\frac{3}{4}(8) + b = -6 + b \Rightarrow b = 5\). Vậy \(y = -\frac{3}{4}x + 5\).',
            r'Hệ số góc đường vuông góc luôn là nghịch đảo ĐỔI DẤU: \(\frac{4}{3} \to -\frac{3}{4}\), sau đó thay điểm đi qua để tìm \(b\).',
            {
                'A': ('Quên đổi dấu slope', r'Nghịch đảo thành \(+\frac{3}{4}\) nhưng quên dấu trừ.'),
                'B': ('Song song thay vì vuông góc', r'Giữ nguyên hệ số góc \(\frac{4}{3}\) của đường song song.'),
                'C': ('Chỉ đổi dấu, quên nghịch đảo', r'Dùng slope \(-\frac{4}{3}\) thay vì \(-\frac{3}{4}\).'),
                'D': ('Đáp án đúng', r'Slope \(-\frac{3}{4}\) và đi qua \((8, -1)\) vì \(-\frac{3}{4}(8) + 5 = -1\).'),
            },
            r'Vẽ `4x - 3y = 18` và điểm `(8, -1)` trên Desmos, sau đó nhập thử phương án D `y = -(3/4)x + 5` thấy ngay cắt vuông góc và đi qua đúng `(8, -1)`.'
        ),
        # Q7 — Algebra (Medium, MCQ -> B)
        math_mcq(
            'sat_mm6_m1_q7', 7, 'Algebra', 'Linear inequalities in one or two variables', 'Medium',
            r'<p>A commercial delivery drone has a maximum payload capacity of \(1{,}650\) grams. It is loaded with medical kits weighing \(110\) grams each and sample vials weighing \(45\) grams each.</p>',
            r'If the drone must carry \(9\) medical kits, what is the <b>maximum</b> number of sample vials it can carry without exceeding its payload capacity?',
            {'A': r'\(13\)', 'B': r'\(14\)', 'C': r'\(15\)', 'D': r'\(36\)'},
            'B',
            r'Lập bất phương trình tải trọng với \(v\) là số ống mẫu: \(110(9) + 45v \le 1{,}650 \Rightarrow 990 + 45v \le 1{,}650 \Rightarrow 45v \le 660 \Rightarrow v \le \frac{660}{45} = 14.666\dots\). Vì số ống mẫu phải là số nguyên không vượt quá sức chở, giá trị lớn nhất là \(14\).',
            r'Với điều kiện "without exceeding" (\(v \le 14.67\)), LUÔN làm tròn XUỐNG lấy phần nguyên (\(14\)), dù phần thập phân lớn hơn \(0.5\)!',
            {
                'A': ('Trừ dư 1 ống', r'\(990 + 45(13) = 1{,}575\text{ g}\), vẫn còn đủ \(75\text{ g}\) cho thêm 1 ống \(45\text{ g}\) nữa.'),
                'B': ('Đáp án đúng', r'\(v \le 14.67 \Rightarrow v_{\max} = 14\) (tổng \(1{,}620 \le 1{,}650\text{ g}\)).'),
                'C': ('Bẫy làm tròn lên', r'Làm tròn \(14.67 \to 15\) cho tổng \(1{,}665\text{ g} > 1{,}650\text{ g}\) (quá tải!).'),
                'D': ('Quên trừ 9 bộ y tế', r'Lấy \(\lfloor 1{,}650 / 45 \rfloor = 36\) mà bỏ qua \(990\text{ g}\) của 9 bộ y tế.'),
            },
            r'Gõ `(1650 - 110*9)/45` vào Desmos ra `14.6667` → làm tròn xuống thành `14`.'
        ),
        # Q8 — Algebra (Medium-Hard, MCQ -> A)
        math_mcq(
            'sat_mm6_m1_q8', 8, 'Algebra', 'Systems of two linear equations in two variables', 'Medium-Hard',
            r'<p>A seismology monitoring station calibrates two filter coefficients \(a\) and \(b\) that satisfy the system below:</p><p style="text-align:center;">\[\begin{cases} 5a + 2b = 43 \\ a + 4b = 29 \end{cases}\]</p>',
            r'What is the value of \(a + b\)?',
            {'A': r'\(12\)', 'B': r'\(14\)', 'C': r'\(24\)', 'D': r'\(72\)'},
            'A',
            r'Cộng vế theo vế hai phương trình: \((5a + a) + (2b + 4b) = 43 + 29 \Rightarrow 6a + 6b = 72\). Chia cả hai vế cho \(6\): \(a + b = 12\)! Không cần mất thời gian giải nghiệm phân số lẻ \(a = \frac{19}{3}, b = \frac{17}{3}\).',
            r'Khi đề hỏi tổ hợp \(a + b\) hay \(a - b\), hãy thử cộng/trừ thẳng hai phương trình trước khi giải từng ẩn!',
            {
                'A': ('Đáp án đúng', r'Cộng 2 phương trình ra \(6a + 6b = 72 \Rightarrow a + b = 12\).'),
                'B': ('Trừ thay vì cộng', r'Lấy \(43 - 29 = 14\) nhưng hiệu vế trái là \(4a - 2b\), không phải \(a + b\).'),
                'C': ('Chia sai cho 3 thay vì 6', r'Tính \(72 / 3 = 24\) do đếm nhầm tổng hệ số.'),
                'D': ('Quên chia cho 6', r'\(72\) là giá trị của \(6a + 6b\), chưa chia cho \(6\).'),
            },
            r'Cộng nhẩm ra `72 / 6 = 12`; hoặc vẽ `5x + 2y = 43` và `x + 4y = 29` trên Desmos, bấm giao điểm `(6.333, 5.667)` rồi cộng lại bằng `12`.'
        ),
        # Q9 — Advanced Math (Medium, SPR -> 31)
        math_spr(
            'sat_mm6_m1_q9', 9, 'Advanced Math', 'Nonlinear functions', 'Medium',
            f'<div style="text-align:center;margin-bottom:10px;">{svg_q9}</div>' + r'<p>The cross-section of a parabolic observatory mirror is modeled by the quadratic function \(f(x) = a(x - 5)^2 + 4\), where \(a\) is a constant. As shown in the figure above, the vertex is at \((5, 4)\) and the graph passes through \((7, 16)\).</p>',
            r'What is the value of \(f(8)\)?',
            ['31'], '31',
            r'Thay điểm \((7, 16)\) vào phương trình dạng đỉnh \(f(x) = a(x - 5)^2 + 4\): \(16 = a(7 - 5)^2 + 4 \Rightarrow 16 = 4a + 4 \Rightarrow 4a = 12 \Rightarrow a = 3\). Khi đó \(f(x) = 3(x - 5)^2 + 4\), suy ra \(f(8) = 3(8 - 5)^2 + 4 = 3(9) + 4 = 31\).',
            r'Với hàm bậc hai đã biết đỉnh \((h, k)\), chỉ cần 1 điểm phụ khác đỉnh là tìm ra ngay hệ số \(a = \dfrac{y - k}{(x - h)^2}\)!',
            r'Gõ `a = (16 - 4)/(7 - 5)^2` trên Desmos ra `3`, rồi gõ `f(x) = 3(x - 5)^2 + 4` và tính `f(8)` ra ngay `31`.'
        ),
        # Q10 — Advanced Math (Medium, MCQ -> C)
        math_mcq(
            'sat_mm6_m1_q10', 10, 'Advanced Math', 'Nonlinear equations in one variable and systems of equations in two variables', 'Medium',
            r'<p>Consider the quadratic equation below, where \(k\) is a constant:</p><p style="text-align:center;">\[3x^2 - 18x + k = 0\]</p>',
            r'If the equation has <b>exactly one real solution</b>, what is the value of \(k\)?',
            {'A': r'\(9\)', 'B': r'\(18\)', 'C': r'\(27\)', 'D': r'\(81\)'},
            'C',
            r'Phương trình bậc hai có đúng một nghiệm thực khi và chỉ khi biệt thức \(\Delta = b^2 - 4ac = 0\): \((-18)^2 - 4(3)(k) = 0 \Rightarrow 324 - 12k = 0 \Rightarrow k = 27\). (Hoặc đặt nhân tử chung: \(3(x^2 - 6x + 9) = 0 \Rightarrow k = 3 \times 9 = 27\).)',
            r'Điều kiện đúng 1 nghiệm thực là \(b^2 - 4ac = 0\); nếu dùng cách hoàn thành bình phương, đừng quên nhân ngược hệ số \(a = 3\)!',
            {
                'A': ('Quên nhân hệ số a = 3', r'\((6/2)^2 = 9\) chỉ là hằng số sau khi đã rút \(3\) ra ngoài.'),
                'B': ('Nhầm với |b|', r'Lấy trực tiếp giá trị \(18\) từ hệ số giữa.'),
                'C': ('Đáp án đúng', r'\(\Delta = 324 - 12k = 0 \Rightarrow k = 27\).'),
                'D': ('Quên nhân a = 3 trong 4ac', r'Chia \(324\) cho \(4\) thay vì \(4(3) = 12\), ra nhầm \(81\).'),
            },
            r'Vẽ `y = 3x^2 - 18x + k` với thanh trượt `k` (từ 0 đến 40) trên Desmos → đỉnh parabol tiếp xúc đúng trục Ox tại `k = 27`.'
        ),
        # Q11 — Advanced Math (Medium, MCQ -> D)
        math_mcq(
            'sat_mm6_m1_q11', 11, 'Advanced Math', 'Equivalent expressions', 'Medium',
            r'<p>Consider the rational expression below for all \(x > 4\):</p><p style="text-align:center;">\[\frac{2}{x - 4} + \frac{5}{x + 1}\]</p>',
            r'Which of the following is equivalent to the given expression?',
            {
                'A': r'\(\dfrac{7}{2x - 3}\)',
                'B': r'\(\dfrac{7x - 3}{x^2 - 3x - 4}\)',
                'C': r'\(\dfrac{7x + 22}{x^2 - 3x - 4}\)',
                'D': r'\(\dfrac{7x - 18}{x^2 - 3x - 4}\)',
            },
            'D',
            r'Quy đồng mẫu số chung \((x - 4)(x + 1) = x^2 - 3x - 4\):<br>\(\dfrac{2(x + 1) + 5(x - 4)}{(x - 4)(x + 1)} = \dfrac{2x + 2 + 5x - 20}{x^2 - 3x - 4} = \dfrac{7x - 18}{x^2 - 3x - 4}\).',
            r'Cộng hai phân thức khác mẫu PHẢI quy đồng nhân chéo lên tử rồi phân phối đầy đủ — không bao giờ cộng thẳng tử với tử, mẫu với mẫu!',
            {
                'A': ('Cộng thẳng tử và mẫu', r'Lỗi sai kinh điển: cộng \(2 + 5 = 7\) và \((x - 4) + (x + 1) = 2x - 3\).'),
                'B': ('Quên phân phối vào hằng số', r'Chỉ cộng \(2x + 5x = 7x\) và giữ nguyên \(1 - 4 = -3\) mà quên nhân \(2(1)\) và \(5(-4)\).'),
                'C': ('Sai dấu -20 thành +20', r'Cộng nhầm \(2 + 20 = 22\) thay vì \(2 - 20 = -18\).'),
                'D': ('Đáp án đúng', r'Quy đồng và rút gọn chuẩn xác ra \(\frac{7x - 18}{x^2 - 3x - 4}\).'),
            },
            r'Thay nhanh `x = 5` vào biểu thức đề: `2/1 + 5/6 = 17/6`. Thay `x = 5` vào 4 đáp án, chỉ D cho `(35 - 18)/(25 - 15 - 4) = 17/6`!'
        ),
        # Q12 — Advanced Math (Easy, MCQ -> B)
        math_mcq(
            'sat_mm6_m1_q12', 12, 'Advanced Math', 'Nonlinear functions', 'Easy',
            r'<p>In a marine aquaculture facility, the surface area \(A(t)\), in square centimeters, of a staghorn coral colony \(t\) months after fragmentation is modeled by:</p><p style="text-align:center;">\[A(t) = 65(1.18)^t\]</p>',
            r'According to the model, how does the surface area of the coral colony change each month?',
            {
                'A': r'It increases by \(118\%\) each month.',
                'B': r'It increases by \(18\%\) each month.',
                'C': r'It increases by \(1.18\) square centimeters each month.',
                'D': r'It increases by \(65\%\) each month.',
            },
            'B',
            r'Trong mô hình hàm mũ tăng trưởng \(A(t) = a(1 + r)^t\), cơ số \(1.18 = 1 + 0.18\), nghĩa là sau mỗi tháng diện tích bề mặt san hô <b>tăng thêm \(18\%\)</b> (so với tháng ngay trước đó).',
            r'Với cơ số tăng trưởng \(b > 1\), tỉ lệ tăng phần trăm mỗi chu kỳ là \((b - 1) \times 100\%\) — luôn trừ đi \(1\) (100% ban đầu)!',
            {
                'A': ('Quên trừ 100% ban đầu', r'\(118\%\) là tổng giá trị mới so với tháng trước, phần TĂNG THÊM chỉ là \(18\%\).'),
                'B': ('Đáp án đúng', r'\(1.18 - 1 = 0.18 = 18\%\) tăng mỗi tháng.'),
                'C': ('Nhầm mô hình tuyến tính', r'Hàm mũ tăng theo tỉ lệ phần trăm, không tăng lượng cố định theo cm².'),
                'D': ('Nhầm giá trị ban đầu thành %', r'\(65\) là diện tích ban đầu tại \(t = 0\), không phải tỉ lệ phần trăm.'),
            },
            r'Kiểm tra nhanh tại `t = 0` (`65`) và `t = 1` (`76.7`): mức tăng `(76.7 - 65)/65 = 0.18 = 18%`.'
        ),
        # Q13 — Advanced Math (Medium-Hard, SPR -> 9/2 or 4.5)
        math_spr(
            'sat_mm6_m1_q13', 13, 'Advanced Math', 'Nonlinear equations in one variable and systems of equations in two variables', 'Medium-Hard',
            r'<p>Consider the quadratic equation shown below:</p><p style="text-align:center;">\[4x^2 - 18x + 11 = 0\]</p>',
            r'What is the <b>sum</b> of the solutions to the given equation?',
            ['9/2', '4.5'], '9/2 (or 4.5)',
            r'Kiểm tra biệt thức \(\Delta = (-18)^2 - 4(4)(11) = 324 - 176 = 148 > 0\), nên phương trình có 2 nghiệm thực phân biệt. Theo định lý Viète, tổng hai nghiệm bằng \(-\dfrac{b}{a} = -\dfrac{-18}{4} = \dfrac{9}{2} = 4.5\).',
            r'Tổng hai nghiệm của \(ax^2 + bx + c = 0\) là \(-\dfrac{b}{a}\): nhớ chia cho \(a = 4\) và rút gọn phân số!',
            r'Vẽ `y = 4x^2 - 18x + 11` trên Desmos, bấm hai giao điểm trục hoành (`0.729` và `3.771`) → cộng lại chính xác bằng `4.5` (`9/2`)!'
        ),
        # Q14 — Advanced Math (Medium-Hard, MCQ -> A)
        math_mcq(
            'sat_mm6_m1_q14', 14, 'Advanced Math', 'Nonlinear equations in one variable and systems of equations in two variables', 'Medium-Hard',
            r'<p>Consider the radical equation below:</p><p style="text-align:center;">\[\sqrt{5x + 11} = x + 1\]</p>',
            r'What is the set of all real solutions to this equation?',
            {'A': r'\(\{5\}\)', 'B': r'\(\{-2, 5\}\)', 'C': r'\(\{-2\}\)', 'D': r'There are no real solutions.'},
            'A',
            r'Điều kiện để vế phải không âm: \(x + 1 \ge 0 \Leftrightarrow x \ge -1\). Bình phương hai vế: \(5x + 11 = (x + 1)^2 = x^2 + 2x + 1 \Rightarrow x^2 - 3x - 10 = 0 \Rightarrow (x - 5)(x + 2) = 0 \Rightarrow x = 5\) hoặc \(x = -2\). Thử lại vào phương trình gốc:<br>• Với \(x = 5\): \(\sqrt{36} = 6 = 5 + 1\) (nhận!).<br>• Với \(x = -2\): \(\sqrt{1} = 1 \ne -2 + 1 = -1\) (nghiệm ngoại lai, LOẠI!).',
            r'Phương trình chứa căn bậc hai BẮT BUỘC phải thử lại nghiệm — căn bậc hai số học không bao giờ nhận giá trị âm!',
            {
                'A': ('Đáp án đúng', r'Chỉ có duy nhất \(x = 5\) thỏa mãn phương trình gốc.'),
                'B': ('Quên loại nghiệm ngoại lai', r'Giữ nhầm \(x = -2\) dù vế phải bằng \(-1 < 0\).'),
                'C': ('Chọn nhầm nghiệm ngoại lai', r'\(x = -2\) làm sai đẳng thức gốc \(\sqrt{1} = -1\).'),
                'D': ('Bỏ sót nghiệm hợp lệ', r'\(x = 5\) là nghiệm thực hoàn toàn hợp lệ.'),
            },
            r'Vẽ `y = sqrt(5x + 11)` và `y = x + 1` trên Desmos → hai đồ thị chỉ cắt nhau tại ĐÚNG 1 điểm `(5, 6)` → nghiệm duy nhất `x = 5`!'
        ),
        # Q15 — Advanced Math (Medium-Hard, MCQ -> C)
        math_mcq(
            'sat_mm6_m1_q15', 15, 'Advanced Math', 'Equivalent expressions', 'Medium-Hard',
            r'<p>The interior volume \(V\) of a right circular conical observatory dome with positive base radius \(r\) and height \(h\) is given by the formula:</p><p style="text-align:center;">\[V = \frac{1}{3}\pi r^2 h\]</p>',
            r'Which of the following equations correctly expresses \(r\) in terms of \(V\) and \(h\)?',
            {
                'A': r'\(r = \sqrt{\dfrac{V}{3\pi h}}\)',
                'B': r'\(r = \dfrac{3V}{\pi h}\)',
                'C': r'\(r = \sqrt{\dfrac{3V}{\pi h}}\)',
                'D': r'\(r = \dfrac{\sqrt{3V}}{\pi h}\)',
            },
            'C',
            r'Nhân cả hai vế với \(3\): \(3V = \pi r^2 h\). Chia cả hai vế cho \(\pi h\): \(r^2 = \dfrac{3V}{\pi h}\). Vì bán kính \(r > 0\), lấy căn bậc hai hai vế ta được \(r = \sqrt{\dfrac{3V}{\pi h}}\).',
            r'Khi rút biến bậc hai từ công thức, cô lập hoàn toàn \(r^2\) trước rồi mới đặt dấu căn bậc hai trùm lên TOÀN BỘ phân số vế phải!',
            {
                'A': ('Chia 3 thay vì nhân 3', r'Chuyển \(\frac{1}{3}\) sang vế trái phải nhân \(3\), không phải chia \(3\).'),
                'B': ('Quên lấy căn bậc hai', r'\(\frac{3V}{\pi h}\) là giá trị của \(r^2\), không phải \(r\).'),
                'C': ('Đáp án đúng', r'Cô lập \(r^2 = \frac{3V}{\pi h}\) rồi lấy căn cho toàn bộ phân số.'),
                'D': ('Đặt căn thiếu mẫu số', r'Chỉ lấy căn ở tử số \(3V\) mà quên lấy căn của mẫu \(\pi h\).'),
            },
            r'Thử số đẹp `r = 6, h = 5` → `V = 60π`. Thay vào 4 đáp án trên Desmos, chỉ C cho `sqrt(180π / (5π)) = sqrt(36) = 6`!'
        ),
        # Q16 — PSDA (Medium, SPR -> 15)
        math_spr(
            'sat_mm6_m1_q16', 16, 'Problem-Solving and Data Analysis', 'Ratios, rates, proportional relationships, and units', 'Medium',
            r'<p>A digital printmaking studio trims an oversized sheet of archival cotton rag paper with an area of \(2{,}160\) square inches. <em>(\(1\text{ foot} = 12\text{ inches}\))</em></p>',
            r'What is the area of the paper sheet, in <b>square feet</b>?',
            ['15'], '15',
            r'Vì \(1\text{ foot} = 12\text{ inches}\), nên \(1\text{ square foot} = 12^2 = 144\text{ square inches}\). Đổi đơn vị diện tích: \(\dfrac{2{,}160}{144} = 15\text{ square feet}\).',
            r'Khi đổi đơn vị diện tích (square inches \(\to\) square feet), PHẢI chia cho \(12^2 = 144\), tuyệt đối không chia cho \(12\)!',
            r'Gõ `2160 / 12^2` trên Desmos ra ngay `15`.'
        ),
        # Q17 — PSDA (Medium, MCQ -> D)
        math_mcq(
            'sat_mm6_m1_q17', 17, 'Problem-Solving and Data Analysis', 'Probability and conditional probability', 'Medium',
            tbl_q17 + r'<p>The table above summarizes \(200\) commercial drone deliveries categorized by weather condition and arrival status.</p>',
            r'If a delivery made during <b>Windy</b> conditions is selected at random, what is the probability that it was <b>Delayed</b>?',
            {'A': r'\(\dfrac{3}{25}\)', 'B': r'\(\dfrac{2}{3}\)', 'C': r'\(\dfrac{7}{10}\)', 'D': r'\(\dfrac{3}{10}\)'},
            'D',
            r'Điều kiện "a delivery made during Windy conditions" thu hẹp không gian mẫu chỉ còn hàng <b>Windy</b> có tổng là \(80\) chuyến. Trong \(80\) chuyến đó, có \(24\) chuyến bị <b>Delayed</b>. Xác suất cần tìm là \(\dfrac{24}{80} = \dfrac{3}{10}\).',
            r'Với xác suất có điều kiện, luôn xác định nhóm nằm sau từ khóa "If a [Group] is selected..." để đặt đúng mẫu số (\(80\), không phải \(200\))!',
            {
                'A': ('Bẫy tổng toàn bảng', r'Chia cho tổng \(200\): \(\frac{24}{200} = \frac{3}{25}\) — quên điều kiện Windy.'),
                'B': ('Đảo ngược điều kiện', r'Tính \(P(\text{Windy} \mid \text{Delayed}) = \frac{24}{36} = \frac{2}{3}\).'),
                'C': ('Nhầm On-Time thay vì Delayed', r'Tính \(\frac{56}{80} = \frac{7}{10}\) là xác suất đúng giờ.'),
                'D': ('Đáp án đúng', r'\(\frac{24}{80} = \frac{3}{10}\).'),
            },
            r'Gõ `24/80` trên Desmos rồi bấm nút phân số bên trái để rút gọn ngay thành `3/10`.'
        ),
        # Q18 — PSDA (Medium, MCQ -> B)
        math_mcq(
            'sat_mm6_m1_q18', 18, 'Problem-Solving and Data Analysis', 'One-variable data: Distributions and measures of center and spread', 'Medium',
            tbl_q18 + r'<p>The table above shows the number of micro-tremors recorded at a tectonic monitoring station over \(7\) consecutive days. After a sensor audit, it was discovered that the reading of \(25\) on Day 7 was misrecorded and should actually be \(67\).</p>',
            r'How do the <b>mean</b> and <b>median</b> of the \(7\) readings change when \(25\) is corrected to \(67\)?',
            {
                'A': r'Both the mean and the median increase.',
                'B': r'The mean increases by \(6\), and the median remains unchanged.',
                'C': r'The mean increases by \(42\), and the median remains unchanged.',
                'D': r'The mean remains unchanged, and the median increases by \(6\).',
            },
            'B',
            r'• <b>Mean:</b> Khi sửa \(25 \to 67\), tổng 7 giá trị tăng thêm \(67 - 25 = 42\), do đó trung bình cộng tăng thêm đúng \(\dfrac{42}{7} = 6\).<br>• <b>Median:</b> Dãy số đã được sắp xếp tăng dần \([14, 17, 19, 21, 22, 24, 25]\). Giá trị chính giữa (thứ 4) là \(21\). Khi thay giá trị lớn nhất \(25\) thành \(67\), thứ tự các phần tử không đổi nên trung vị vẫn là \(21\) (không đổi!).',
            r'Tăng giá trị lớn nhất trong tập dữ liệu luôn kéo Mean tăng lên đúng \(\dfrac{\Delta\text{Sum}}{n}\), nhưng Median (giá trị ở giữa) hoàn toàn kháng ngoại lai (resistant to outliers)!',
            {
                'A': ('Nhầm tính chất Median', r'Thay giá trị lớn nhất \(25 \to 67\) không làm dịch chuyển phần tử đứng thứ 4 (\(21\)).'),
                'B': ('Đáp án đúng', r'Tổng tăng \(42\) nên Mean tăng \(42/7 = 6\), còn Median vẫn giữ nguyên là \(21\).'),
                'C': ('Quên chia cho n = 7', r'\(42\) là mức tăng của TỔNG (sum), chưa chia cho \(7\) ngày.'),
                'D': ('Đảo ngược Mean và Median', r'Mean mới tăng thêm \(6\), còn Median không đổi.'),
            },
            r'Kiểm chứng bằng `(67 - 25)/7 = 6` trên Desmos; hoặc so `mean` và `median` của 2 list trước/sau khi sửa.'
        ),
        # Q19 — PSDA (Medium-Hard, SPR -> 54)
        math_spr(
            'sat_mm6_m1_q19', 19, 'Problem-Solving and Data Analysis', 'Percentages', 'Medium-Hard',
            r'<p>In a coral reef restoration budget, three positive amounts \(p\), \(q\), and \(r\) satisfy the following relationships: \(p\) is \(120\%\) of \(q\), and \(q\) is \(45\%\) of \(r\).</p>',
            r'If \(p\) is \(k\%\) of \(r\), what is the value of \(k\)?',
            ['54'], '54',
            r'Đặt \(r = 100\). Khi đó \(q = 45\% \text{ của } 100 = 45\). Tiếp theo, \(p = 120\% \text{ của } 45 = 1.20 \times 45 = 54\). Vì \(r = 100\) nên \(p\) bằng đúng \(54\%\) của \(r \Rightarrow k = 54\).',
            r'Với chuỗi phần trăm liên tiếp, chọn biến gốc cuối cùng bằng \(100\) để đọc thẳng giá trị phần trăm \(k\) trong 5 giây!',
            r'Gõ `1.20 * 0.45 * 100` trên Desmos ra ngay `54`.'
        ),
        # Q20 — Geometry & Trig (Medium, MCQ -> A)
        math_mcq(
            'sat_mm6_m1_q20', 20, 'Geometry and Trigonometry', 'Lines, angles, and triangles', 'Medium',
            f'<div style="text-align:center;margin-bottom:10px;">{svg_q20}</div>' + r'<p>In the diagram above, two parallel tectonic fault lines \(f_1\) and \(f_2\) are intersected by a straight seismic survey line.</p>',
            r'What is the measure, in degrees, of each <b>acute</b> angle formed where the survey line intersects fault line \(f_2\)?',
            {'A': r'\(80\)', 'B': r'\(22\)', 'C': r'\(100\)', 'D': r'\(112\)'},
            'A',
            r'Hai góc đánh dấu \((4x + 12)^\circ\) và \((6x - 32)^\circ\) là hai góc đồng vị (cùng nằm ở phía trên bên phải của hai đường song song \(f_1 \parallel f_2\)) nên bằng nhau:<br>\(4x + 12 = 6x - 32 \Rightarrow 2x = 44 \Rightarrow x = 22\).<br>Thay ngược lại tìm số đo góc tù: \(4(22) + 12 = 100^\circ\). Vì góc nhọn và góc tù kề bù nhau nên mỗi góc nhọn bằng \(180^\circ - 100^\circ = 80^\circ\).',
            r'Đường cắt hai đường song song chỉ tạo ra 2 cỡ góc bù nhau (\(100^\circ\) và \(80^\circ\)); luôn đọc kỹ xem đề hỏi \(x\), góc tù hay góc nhọn (acute)!',
            {
                'A': ('Đáp án đúng', r'Giải ra \(x = 22 \Rightarrow\) góc tù \(100^\circ \Rightarrow\) góc nhọn \(180 - 100 = 80^\circ\).'),
                'B': ('Dừng ở giá trị x', r'\(22\) mới là giá trị của ẩn \(x\), không phải số đo góc.'),
                'C': ('Nhầm góc tù với góc nhọn', r'\(100^\circ > 90^\circ\) là góc tù (obtuse), đề yêu cầu tìm góc nhọn (acute).'),
                'D': ('Cộng sai khi giải x', r'Trừ/cộng nhầm hằng số khi lập phương trình góc.'),
            },
            r'Gõ `4x + 12 = 6x - 32` trên Desmos đọc `x = 22`, sau đó tính `180 - (4*22 + 12) = 80`.'
        ),
        # Q21 — Geometry & Trig (Medium-Hard, MCQ -> C)
        math_mcq(
            'sat_mm6_m1_q21', 21, 'Geometry and Trigonometry', 'Circles', 'Medium-Hard',
            f'<div style="text-align:center;margin-bottom:10px;">{svg_q21}</div>' + r'<p>The circular base of a spherical observatory dome has center \(O\) and radius \(18\) meters. A retractable viewing aperture spans minor arc \(\widehat{AB}\) with central angle \(\angle AOB = 70^\circ\), as shown above.</p>',
            r'What is the length of minor arc \(\widehat{AB}\), in meters?',
            {'A': r'\(\dfrac{7\pi}{2}\)', 'B': r'\(14\pi\)', 'C': r'\(7\pi\)', 'D': r'\(63\pi\)'},
            'C',
            r'Độ dài cung tròn bằng tỉ lệ góc ở tâm nhân với chu vi đường tròn \(2\pi r\):<br>\(L = \dfrac{70^\circ}{360^\circ} \cdot 2\pi(18) = \dfrac{7}{36} \cdot 36\pi = 7\pi\text{ m}\).',
            r'Phân biệt thật rõ hai công thức: Độ dài cung tròn dùng chu vi \(\dfrac{\theta}{360^\circ} \cdot 2\pi r\), còn Diện tích hình quạt mới dùng \(\dfrac{\theta}{360^\circ} \cdot \pi r^2\)!',
            {
                'A': ('Quên nhân 2 trong chu vi', r'Tính nhầm \(\frac{70}{360} \cdot \pi(18) = \frac{7\pi}{2}\).'),
                'B': ('Nhân đôi bán kính nhầm', r'Dùng nhầm \(r = 36\) thay vì \(r = 18\), ra \(14\pi\).'),
                'C': ('Đáp án đúng', r'\(\frac{70}{360} \cdot 2\pi(18) = 7\pi\).'),
                'D': ('Tính nhầm Diện tích hình quạt', r'\(\frac{70}{360} \cdot \pi(18)^2 = 63\pi\) là diện tích hình quạt, không phải độ dài cung.'),
            },
            r'Gõ `(70/360) * 2 * 18` trên Desmos ra đúng `7` → gắn thêm `π` được `7π`.'
        ),
        # Q22 — Geometry & Trig (Medium-Hard, SPR -> 20)
        math_spr(
            'sat_mm6_m1_q22', 22, 'Geometry and Trigonometry', 'Right triangles and trigonometry', 'Medium-Hard',
            f'<div style="text-align:center;margin-bottom:10px;">{svg_q22}</div>' + r'<p>In right triangle \(PQR\) shown above, \(\angle Q = 90^\circ\), the hypotenuse \(PR = 52\), and \(\cos(R) = \dfrac{12}{13}\).</p>',
            r'What is the length of side \(PQ\)?',
            ['20'], '20',
            r'Trong tam giác vuông \(PQR\) vuông tại \(Q\), \(\cos(R) = \dfrac{\text{kề}}{\text{huyền}} = \dfrac{QR}{PR} = \dfrac{12}{13}\). Vì \(PR = 52 = 13 \times 4\), suy ra cạnh kề \(QR = 12 \times 4 = 48\). Áp dụng định lý Pythagoras (hoặc bộ ba \(5\text{–}12\text{–}13\) nhân \(4\)): \(PQ = \sqrt{52^2 - 48^2} = \sqrt{2{,}704 - 2{,}304} = \sqrt{400} = 20\).',
            r'Nhận diện bộ ba Pythagoras \(5\text{–}12\text{–}13\) nhân hệ số \(4\) ra ngay tam giác \(20\text{–}48\text{–}52\); chú ý \(PQ\) là cạnh ĐỐI của góc \(R\) chứ không phải cạnh kề \(QR\)!',
            r'Tính `QR = 52*(12/13) = 48`, sau đó gõ `sqrt(52^2 - 48^2)` trên Desmos ra ngay `20`.'
        ),
    ]


if __name__ == '__main__':
    assert verify_math()
    qs = get_m1_questions()
    print(f"M1 verified: {len(qs)} questions")
