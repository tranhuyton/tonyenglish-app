# -*- coding: utf-8 -*-
"""
Digital SAT Math Adaptive Mock Test #6 — Module 2 Standard/Lower (300–600 Band, 22 Questions)
Themes: Coral nursery aquaculture, commercial drone delivery networks, digital printmaking studios,
seismology & tectonic monitoring stations, spherical & conical observatory domes.
Blueprint: 8 Algebra (Q1-Q8), 7 Advanced Math (Q9-Q15), 4 PSDA (Q16-Q19), 3 Geometry/Trig (Q20-Q22).
Format: 16 MCQ (A:4, B:4, C:4, D:4) + 6 SPR (Q5, Q9, Q13, Q16, Q19, Q22).
"""

from fractions import Fraction
import math
from sat_math_helpers import (
    math_mcq, math_spr, build_math_table,
    svg_parabola_vertex, svg_right_triangle, svg_circle_sector, svg_cylinder
)


def verify_math():
    """Programmatic exact arithmetic verification for all 22 Module 2 Standard/Lower questions."""
    # Q1: 5x - 8 = 27 => x = 7 => 3x + 2 = 23
    x1 = Fraction(27 + 8, 5)
    assert x1 == 7 and 5 * x1 - 8 == 27 and 3 * x1 + 2 == 23

    # Q2: C(n) = 24n + 65 => C(0) = 65
    assert 24 * 0 + 65 == 65

    # Q3: slope through (2, 30) and (6, 78) => 48 / 4 = 12
    assert Fraction(78 - 30, 6 - 2) == 12

    # Q4: x + y = 22, x - y = 8 => x = 15, y = 7
    assert 15 + 7 == 22 and 15 - 7 == 8

    # Q5: 4(x - 6) = 28 => x = 13
    x5 = Fraction(28, 4) + 6
    assert x5 == 13 and 4 * (x5 - 6) == 28

    # Q6: 3x + 5 > 26 => x > 7; among {4, 6, 7, 9} only 9 satisfies
    assert not (3 * 4 + 5 > 26) and not (3 * 6 + 5 > 26) and not (3 * 7 + 5 > 26) and (3 * 9 + 5 > 26)

    # Q7: s + L = 30, 12s + 20L = 472 => s = 16, L = 14
    assert 16 + 14 == 30 and 12 * 16 + 20 * 14 == 472

    # Q8: 3x - 5y = 24, y = 0 => x = 8 => (8, 0)
    assert Fraction(24, 3) == 8 and 3 * 8 - 5 * 0 == 24

    # Q9: f(x) = 3x^2 - 4x + 2 => f(4) = 34
    assert 3 * (4 ** 2) - 4 * 4 + 2 == 34

    # Q10: (x^9 * x^4) / x^5 = x^8
    assert 9 + 4 - 5 == 8 and Fraction(2 ** 9 * 2 ** 4, 2 ** 5) == 2 ** 8

    # Q11: (4x^2 - 3x + 7) - (x^2 - 5x + 2) = 3x^2 + 2x + 5
    for xv in (0, 1, 3):
        assert (4 * xv**2 - 3 * xv + 7) - (xv**2 - 5 * xv + 2) == 3 * xv**2 + 2 * xv + 5

    # Q12: x^2 - 5x - 14 = (x - 7)(x + 2) = 0 => positive root 7
    assert 7**2 - 5 * 7 - 14 == 0 and (-2)**2 - 5 * (-2) - 14 == 0 and 7 > 0

    # Q13: h(x) = -2(x - 4)^2 + 9 => max = 9 at x = 4
    h13 = lambda x: -2 * (x - 4) ** 2 + 9
    assert h13(4) == 9 and h13(3) < 9 and h13(5) < 9

    # Q14: P(t) = 80 * 2^(t/3) => P(9) = 80 * 8 = 640
    assert 80 * (2 ** (9 // 3)) == 640

    # Q15: sqrt(x + 9) = 7 => x = 40
    assert math.isclose(math.sqrt(40 + 9), 7)

    # Q16: 105 km / 3 hr * 5 hr = 175 km
    assert Fraction(105, 3) * 5 == 175

    # Q17: 35% of 320 = 112
    assert Fraction(35, 100) * 320 == 112

    # Q18: Median of [19, 14, 27, 16, 22, 18, 25] => sorted [14, 16, 18, 19, 22, 25, 27] => 19
    d18 = sorted([19, 14, 27, 16, 22, 18, 25])
    assert d18[3] == 19

    # Q19: 24 / 160 = 3/20 = 0.15
    assert 52 + 28 == 80 and 56 + 24 == 80 and 80 + 80 == 160 and Fraction(24, 160) == Fraction(3, 20)

    # Q20: Right triangle, angle C = 34 deg => x = 90 - 34 = 56
    assert 180 - 90 - 34 == 56

    # Q21: Sector r = 12, angle = 60 deg => area = (60/360) * 144 * pi = 24 * pi
    assert Fraction(60, 360) * (12 ** 2) == 24

    # Q22: Cylinder r = 6, h = 10 => V = 360 * pi
    assert (6 ** 2) * 10 == 360

    return True


def get_m2l_questions():
    svg_q13 = svg_parabola_vertex(
        h_lbl='4', k_lbl='9', opens_up=False,
        note='Observatory Dome Arch Height Model'
    )
    tbl_q18 = build_math_table(
        ['Day', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
        [
            ['Tremor Count', '19', '14', '27', '16', '22', '18', '25'],
        ],
        caption='Daily Micro-Tremor Readings at Seismic Station West'
    )
    tbl_q19 = build_math_table(
        ['Paper Size', 'Matte Finish', 'Glossy Finish', 'Total'],
        [
            ['Small', '52', '28', '80'],
            ['Large', '56', '24', '80'],
            ['Total', '108', '52', '160'],
        ],
        caption='Digital Printmaking Studio Inventory Batch'
    )
    svg_q20 = svg_right_triangle(
        a_lbl='', b_lbl='', c_lbl='',
        angle_bottom_right='34°', angle_top_left='x°',
        v_top='A', v_right_angle='B', v_right='C',
        note='Seismic Triangulation Triangle (not drawn to scale).'
    )
    svg_q21 = svg_circle_sector(
        radius_lbl='r = 12', angle_lbl='60°', center_lbl='O', pt_a='A', pt_b='B',
        note='Observatory Dome Floor Sector (not drawn to scale).'
    )
    svg_q22 = svg_cylinder(
        r_lbl='r = 6', h_lbl='h = 10',
        note='Cylindrical Coral Nursery Filtration Tank'
    )

    return [
        # Q1 — Algebra (Easy, MCQ -> A)
        math_mcq(
            'sat_mm6_m2l_q1', 1, 'Algebra', 'Linear equations in one variable', 'Easy',
            r'<p>Consider the linear equation shown below:</p><p style="text-align:center;font-size:18px;">\[5x - 8 = 27\]</p>',
            r'What is the value of \(3x + 2\)?',
            {'A': r'\(23\)', 'B': r'\(7\)', 'C': r'\(21\)', 'D': r'\(19\)'},
            'A',
            r'Cộng \(8\) vào cả hai vế: \(5x = 27 + 8 = 35 \Rightarrow x = 7\). Thay \(x = 7\) vào biểu thức đề hỏi: \(3(7) + 2 = 21 + 2 = 23\).',
            r'Sau khi tìm ra \(x = 7\), luôn nhớ thay vào biểu thức \(3x + 2\) trước khi chọn đáp án!',
            {
                'A': ('Đáp án đúng', r'\(x = 7 \Rightarrow 3(7) + 2 = 23\).'),
                'B': ('Dừng ở giá trị x', r'\(7\) chỉ mới là giá trị của \(x\), chưa tính \(3x + 2\).'),
                'C': ('Quên cộng +2', r'Chỉ tính \(3(7) = 21\) mà quên cộng \(2\).'),
                'D': ('Trừ thay vì cộng 2', r'Tính nhầm \(3(7) - 2 = 19\).'),
            },
            r'Gõ `5x - 8 = 27` vào Desmos ra đường đứng `x = 7`, sau đó tính `3(7) + 2 = 23`.'
        ),
        # Q2 — Algebra (Easy, MCQ -> B)
        math_mcq(
            'sat_mm6_m2l_q2', 2, 'Algebra', 'Linear functions', 'Easy',
            r'<p>A digital printmaking studio charges a client \(C(n) = 24n + 65\) dollars to produce \(n\) framed archival giclée prints.</p>',
            r'What does the number \(65\) represent in this equation?',
            {
                'A': r'The cost, in dollars, for each framed print produced',
                'B': r'The flat setup and proofing fee, in dollars, regardless of the number of prints',
                'C': r'The maximum number of framed prints that can be ordered',
                'D': r'The total price of \(65\) framed prints',
            },
            'B',
            r'Trong hàm bậc nhất \(C(n) = 24n + 65\), hằng số tự do \(65\) là giá trị khi \(n = 0\) (y-intercept), biểu thị khoản phí cố định ban đầu (setup & proofing fee) $65 chưa tính số lượng bản in.',
            r'Trong \(y = mx + b\), hằng số tự do \(b\) luôn là chi phí cố định ban đầu (flat fee / initial value) tại \(x = 0\).',
            {
                'A': ('Nhầm với hệ số góc m', r'$24 mới là đơn giá cho mỗi bản in.'),
                'B': ('Đáp án đúng', r'$65 là khoản phí cố định ban đầu không phụ thuộc số bản in \(n\).'),
                'C': ('Sai ý nghĩa đại lượng', r'65 có đơn vị là dollars, không phải số lượng bản in tối đa.'),
                'D': ('Hiểu sai công thức', r'Giá của 65 bản in là \(24(65) + 65\), không phải $65.'),
            },
            r'Thay `n = 0` vào `24(0) + 65 = 65` để thấy ngay đó là chi phí cố định ban đầu.'
        ),
        # Q3 — Algebra (Easy, MCQ -> C)
        math_mcq(
            'sat_mm6_m2l_q3', 3, 'Algebra', 'Linear equations in two variables', 'Easy',
            r'<p>A commercial delivery drone ascends at a constant rate. On a graph of altitude versus time, the line passes through the points \((2, 30)\) and \((6, 78)\).</p>',
            r'What is the slope of this line?',
            {'A': r'\(4\)', 'B': r'\(8\)', 'C': r'\(12\)', 'D': r'\(16\)'},
            'C',
            r'Áp dụng công thức hệ số góc: \(m = \dfrac{y_2 - y_1}{x_2 - x_1} = \dfrac{78 - 30}{6 - 2} = \dfrac{48}{4} = 12\).',
            r'Hệ số góc luôn là \(\dfrac{\text{Rise}}{\text{Run}} = \dfrac{y_2 - y_1}{x_2 - x_1}\) (hiệu tung độ trên tử, hiệu hoành độ dưới mẫu).',
            {
                'A': ('Lấy hiệu hoành độ Δx', r'\(6 - 2 = 4\) mới là mẫu số \(\Delta x\), chưa tính tỉ số.'),
                'B': ('Chia sai cho 6', r'Tính nhầm \(48 / 6 = 8\) thay vì chia cho \(6 - 2 = 4\).'),
                'C': ('Đáp án đúng', r'\(\frac{78 - 30}{6 - 2} = \frac{48}{4} = 12\).'),
                'D': ('Chia sai cho 3', r'Trừ nhầm \(6 - 2\) thành \(3\): \(48 / 3 = 16\).'),
            },
            r'Gõ `(78 - 30) / (6 - 2)` vào Desmos ra ngay `12`.'
        ),
        # Q4 — Algebra (Easy, MCQ -> D)
        math_mcq(
            'sat_mm6_m2l_q4', 4, 'Algebra', 'Systems of two linear equations in two variables', 'Easy',
            r'<p>Two coral nursery tank temperatures \(x\) and \(y\) satisfy the system of equations below:</p><p style="text-align:center;">\[\begin{cases} x + y = 22 \\ x - y = 8 \end{cases}\]</p>',
            r'What is the value of \(y\)?',
            {'A': r'\(15\)', 'B': r'\(14\)', 'C': r'\(8\)', 'D': r'\(7\)'},
            'D',
            r'Lấy phương trình thứ nhất trừ phương trình thứ hai: \((x + y) - (x - y) = 22 - 8 \Rightarrow 2y = 14 \Rightarrow y = 7\) (và \(x = 15\)).',
            r'Với hệ tổng–hiệu \(x + y\) và \(x - y\), trừ hai phương trình triệt tiêu ngay \(x\) để tìm trực tiếp \(2y\)!',
            {
                'A': ('Tìm nhầm x thay vì y', r'\(15\) là giá trị của \(x\), đề bài hỏi \(y\).'),
                'B': ('Quên chia cho 2', r'\(14\) là giá trị của \(2y\), cần chia \(2\) ra \(y = 7\).'),
                'C': ('Chọn nhầm vế phải', r'\(8\) là hiệu \(x - y\), không phải \(y\).'),
                'D': ('Đáp án đúng', r'\(2y = 14 \Rightarrow y = 7\).'),
            },
            r'Vẽ `x + y = 22` và `x - y = 8` trên Desmos → bấm giao điểm `(15, 7)` → đọc tung độ `y = 7`.'
        ),
        # Q5 — Algebra (Easy, SPR -> 13)
        math_spr(
            'sat_mm6_m2l_q5', 5, 'Algebra', 'Linear equations in one variable', 'Easy',
            r'<p>Consider the linear equation shown below:</p><p style="text-align:center;font-size:18px;">\[4(x - 6) = 28\]</p>',
            r'What is the value of \(x\)?',
            ['13'], '13',
            r'Chia cả hai vế cho \(4\): \(x - 6 = 7\). Cộng \(6\) vào cả hai vế: \(x = 7 + 6 = 13\).',
            r'Khi vế phải chia hết cho hệ số ngoài ngoặc (\(28 / 4 = 7\)), hãy chia ngay trước khi phá ngoặc để giải nhanh và tránh sai sót!',
            r'Gõ `4(x - 6) = 28` vào Desmos sẽ hiện ngay đường thẳng đứng tại `x = 13`.'
        ),
        # Q6 — Algebra (Easy, MCQ -> D)
        math_mcq(
            'sat_mm6_m2l_q6', 6, 'Algebra', 'Linear inequalities in one or two variables', 'Easy',
            r'<p>A seismic station power controller requires voltage index \(x\) to satisfy the inequality below:</p><p style="text-align:center;">\[3x + 5 > 26\]</p>',
            r'Which of the following values of \(x\) is a solution to the inequality?',
            {'A': r'\(4\)', 'B': r'\(6\)', 'C': r'\(7\)', 'D': r'\(9\)'},
            'D',
            r'Giải bất phương trình: \(3x > 26 - 5 \Rightarrow 3x > 21 \Rightarrow x > 7\). Vì dấu bất đẳng thức là lớn hơn NGHIÊM NGẶT (\(>\)), số \(7\) không thỏa mãn; chỉ duy nhất \(9 > 7\) là nghiệm.',
            r'Phân biệt thật rõ dấu \(>\) (nghiêm ngặt, KHÔNG lấy giá trị biên \(7\)) với dấu \(\ge\) (có lấy giá trị biên)!',
            {
                'A': ('Không thỏa mãn', r'\(3(4) + 5 = 17 \ngtr 26\).'),
                'B': ('Không thỏa mãn', r'\(3(6) + 5 = 23 \ngtr 26\).'),
                'C': ('Bẫy giá trị biên x = 7', r'\(3(7) + 5 = 26\), bằng \(26\) chứ không lớn hơn hẳn \(26\).'),
                'D': ('Đáp án đúng', r'\(3(9) + 5 = 32 > 26\).'),
            },
            r'Gõ `3x + 5 > 26` vào Desmos để thấy miền tô nằm bên phải đường nét đứt `x = 7` → chỉ `9` nằm trong miền nghiệm!'
        ),
        # Q7 — Algebra (Medium, MCQ -> A)
        math_mcq(
            'sat_mm6_m2l_q7', 7, 'Algebra', 'Systems of two linear equations in two variables', 'Medium',
            r'<p>A commercial drone delivery depot dispatched \(30\) parcels in one morning, consisting of \(s\) small parcels and \(L\) large parcels. Each small parcel earned a delivery fee of $12, and each large parcel earned a delivery fee of $20. The depot earned a total of $472 in delivery fees from these \(30\) parcels.</p>',
            r'Which system of equations represents this situation?',
            {
                'A': r'\(s + L = 30\) and \(12s + 20L = 472\)',
                'B': r'\(s + L = 472\) and \(12s + 20L = 30\)',
                'C': r'\(s + L = 30\) and \(20s + 12L = 472\)',
                'D': r'\(12s + 20L = 30\) and \(s - L = 472\)',
            },
            'A',
            r'• Phương trình tổng số kiện hàng: số kiện nhỏ \(s\) cộng số kiện lớn \(L\) bằng \(30 \Rightarrow s + L = 30\).<br>• Phương trình tổng doanh thu (tính bằng đô-la): \(12s + 20L = 472\) (vì kiện nhỏ $12 và kiện lớn $20).',
            r'Khi lập hệ phương trình từ bài toán thực tế, luôn khớp ĐÚNG ĐƠN VỊ của từng phương trình (kiện + kiện = tổng kiện; đô-la + đô-la = tổng đô-la) và khớp đúng giá với từng biến!',
            {
                'A': ('Đáp án đúng', r'Khớp chuẩn cả tổng số kiện (\(30\)) lẫn đơn giá từng loại ($12 cho \(s\), $20 cho \(L\)).'),
                'B': ('Đảo lộn hai vế phải', r'Gán nhầm tổng số tiền $472 cho số lượng kiện hàng và ngược lại.'),
                'C': ('Tráo đổi đơn giá s và L', r'Gắn nhầm giá $20 cho kiện nhỏ \(s\) và $12 cho kiện lớn \(L\).'),
                'D': ('Lẫn lộn cả hai phương trình', r'Sai cả đơn vị lẫn phép toán trừ giữa \(s\) và \(L\).'),
            },
            r'Kiểm tra nhanh bằng cách vẽ hệ A trên Desmos: giao điểm là `(16, 14)` — cả hai đều là số nguyên dương hợp lý!'
        ),
        # Q8 — Algebra (Medium, MCQ -> B)
        math_mcq(
            'sat_mm6_m2l_q8', 8, 'Algebra', 'Linear equations in two variables', 'Medium',
            r'<p>In the \(xy\)-plane, a line is defined by the equation:</p><p style="text-align:center;">\[3x - 5y = 24\]</p>',
            r'What is the \(x\)-intercept of this line?',
            {'A': r'\((0, 8)\)', 'B': r'\((8, 0)\)', 'C': r'\((0, -4.8)\)', 'D': r'\((-8, 0)\)'},
            'B',
            r'Giao điểm với trục hoành (\(x\)-intercept) luôn có tung độ \(y = 0\). Thay \(y = 0\) vào phương trình: \(3x - 5(0) = 24 \Rightarrow 3x = 24 \Rightarrow x = 8\). Vậy \(x\)-intercept là \((8, 0)\).',
            r'Luôn nhớ: tìm \(x\)-intercept thì đặt \(y = 0\) (viết dạng \((x, 0)\)); tìm \(y\)-intercept thì đặt \(x = 0\) (viết dạng \((0, y)\))!',
            {
                'A': ('Đảo ngược tọa độ (x, y)', r'\((0, 8)\) nằm trên trục tung Oy, không phải trục hoành Ox.'),
                'B': ('Đáp án đúng', r'Thay \(y = 0 \Rightarrow x = 8\), tọa độ là \((8, 0)\).'),
                'C': ('Tìm nhầm y-intercept', r'\((0, -4.8)\) là giao điểm trục tung (khi \(x = 0\)).'),
                'D': ('Sai dấu', r'Tính nhầm \(x = -8\) thay vì \(+8\).'),
            },
            r'Gõ thẳng `3x - 5y = 24` vào Desmos rồi bấm chấm xám nằm trên trục ngang Ox để đọc ngay `(8, 0)`!'
        ),
        # Q9 — Advanced Math (Easy, SPR -> 34)
        math_spr(
            'sat_mm6_m2l_q9', 9, 'Advanced Math', 'Nonlinear functions', 'Easy',
            r'<p>The height function \(f\) is defined by:</p><p style="text-align:center;">\[f(x) = 3x^2 - 4x + 2\]</p>',
            r'What is the value of \(f(4)\)?',
            ['34'], '34',
            r'Thay \(x = 4\) vào hàm số (tính lũy thừa trước khi nhân):<br>\(f(4) = 3(4^2) - 4(4) + 2 = 3(16) - 16 + 2 = 48 - 16 + 2 = 34\).',
            r'Theo thứ tự phép toán PEMDAS, luôn bình phương \(4^2 = 16\) TRƯỚC khi nhân với \(3\) (tuyệt đối không tính \((3 \times 4)^2 = 144\))!',
            r'Gõ `f(x) = 3x^2 - 4x + 2` rồi gõ `f(4)` ở dòng dưới trên Desmos ra ngay `34`.'
        ),
        # Q10 — Advanced Math (Easy, MCQ -> C)
        math_mcq(
            'sat_mm6_m2l_q10', 10, 'Advanced Math', 'Equivalent expressions', 'Easy',
            r'<p>For all positive values of \(x\), consider the exponential expression below:</p><p style="text-align:center;">\[\frac{x^9 \cdot x^4}{x^5}\]</p>',
            r'Which of the following is equivalent to the given expression?',
            {'A': r'\(x^{18}\)', 'B': r'\(x^{10}\)', 'C': r'\(x^8\)', 'D': r'\(x^{31}\)'},
            'C',
            r'Áp dụng quy tắc lũy thừa cùng cơ số: nhân thì CỘNG số mũ, chia thì TRỪ số mũ:<br>\(\dfrac{x^9 \cdot x^4}{x^5} = \dfrac{x^{9 + 4}}{x^5} = \dfrac{x^{13}}{x^5} = x^{13 - 5} = x^8\).',
            r'Cùng cơ số \(x\): \(x^a \cdot x^b = x^{a + b}\) và \(\dfrac{x^a}{x^b} = x^{a - b}\).',
            {
                'A': ('Cộng cả số mũ ở mẫu', r'Tính nhầm \(9 + 4 + 5 = 18\) thay vì trừ \(5\).'),
                'B': ('Đảo dấu +4 và -5', r'Tính nhầm \(9 - 4 + 5 = 10\).'),
                'C': ('Đáp án đúng', r'\(x^{9 + 4 - 5} = x^8\).'),
                'D': ('Nhân số mũ thay vì cộng', r'Tính nhầm \(9 \times 4 - 5 = 31\).'),
            },
            r'Gõ `(2^9 * 2^4) / 2^5` trên Desmos ra `256`, so với `2^8 = 256` để kiểm chứng ngay đáp án C!'
        ),
        # Q11 — Advanced Math (Easy, MCQ -> D)
        math_mcq(
            'sat_mm6_m2l_q11', 11, 'Advanced Math', 'Equivalent expressions', 'Easy',
            r'<p>Consider the polynomial expression below:</p><p style="text-align:center;">\[(4x^2 - 3x + 7) - (x^2 - 5x + 2)\]</p>',
            r'Which of the following is equivalent to the given expression?',
            {
                'A': r'\(3x^2 - 8x + 5\)',
                'B': r'\(3x^2 - 8x + 9\)',
                'C': r'\(3x^2 + 2x + 9\)',
                'D': r'\(3x^2 + 2x + 5\)',
            },
            'D',
            r'Phân phối dấu trừ vào TẤT CẢ các hạng tử trong ngoặc thứ hai:<br>\(4x^2 - 3x + 7 - x^2 + 5x - 2 = (4 - 1)x^2 + (-3 + 5)x + (7 - 2) = 3x^2 + 2x + 5\).',
            r'Khi bỏ ngoặc có dấu trừ đằng trước, PHẢI đổi dấu toàn bộ các hạng tử bên trong (\(-(-5x) = +5x\) và \(-(+2) = -2\))!',
            {
                'A': ('Quên đổi dấu -5x', r'Cộng nhầm \(-3x - 5x = -8x\) thay vì \(-3x + 5x = +2x\).'),
                'B': ('Quên đổi dấu cả -5x lẫn +2', r'Ra \(-8x + 9\) do chỉ trừ mỗi \(x^2\).'),
                'C': ('Quên đổi dấu +2', r'Cộng nhầm \(7 + 2 = 9\) thay vì \(7 - 2 = 5\).'),
                'D': ('Đáp án đúng', r'Đổi dấu đầy đủ và gom nhóm chính xác thành \(3x^2 + 2x + 5\).'),
            },
            r'Thay nhanh `x = 1` vào đề: `(4 - 3 + 7) - (1 - 5 + 2) = 8 - (-2) = 10`. Thay `x = 1` vào 4 phương án, chỉ D cho `3 + 2 + 5 = 10`!'
        ),
        # Q12 — Advanced Math (Medium, MCQ -> C)
        math_mcq(
            'sat_mm6_m2l_q12', 12, 'Advanced Math', 'Nonlinear equations in one variable and systems of equations in two variables', 'Medium',
            r'<p>Consider the quadratic equation below:</p><p style="text-align:center;">\[x^2 - 5x - 14 = 0\]</p>',
            r'What is the <b>positive</b> solution to this equation?',
            {'A': r'\(2\)', 'B': r'\(5\)', 'C': r'\(7\)', 'D': r'\(14\)'},
            'C',
            r'Tìm hai số có tích bằng \(-14\) và tổng bằng \(-5\): đó là \(-7\) và \(+2\). Phân tích nhân tử:<br>\((x - 7)(x + 2) = 0 \Rightarrow x = 7\) hoặc \(x = -2\).<br>Vậy nghiệm dương (positive solution) là \(7\).',
            r'Khi đã tách thành \((x - 7)(x + 2) = 0\), nhớ ĐỔI DẤU trong ngoặc để đọc nghiệm: \(x = +7\) và \(x = -2\)!',
            {
                'A': ('Sai dấu nghiệm -2', r'\((x + 2) = 0\) cho \(x = -2\) (nghiệm âm), không phải \(+2\).'),
                'B': ('Nhầm tổng hai nghiệm', r'\(5\) là tổng hai nghiệm \(7 + (-2)\), không phải một nghiệm của phương trình.'),
                'C': ('Đáp án đúng', r'\(7^2 - 5(7) - 14 = 49 - 35 - 14 = 0\) và \(7 > 0\).'),
                'D': ('Lấy nhầm hằng số c', r'\(14\) là giá trị tuyệt đối của tích hai nghiệm, không phải nghiệm.'),
            },
            r'Vẽ `y = x^2 - 5x - 14` trên Desmos → bấm vào giao điểm bên phải trục Oy đọc ngay `(7, 0)`!'
        ),
        # Q13 — Advanced Math (Medium, SPR -> 9)
        math_spr(
            'sat_mm6_m2l_q13', 13, 'Advanced Math', 'Nonlinear functions', 'Medium',
            f'<div style="text-align:center;margin-bottom:10px;">{svg_q13}</div>' + r'<p>The cross-sectional height \(h(x)\), in meters, of a parabolic observatory arch is modeled by the function:</p><p style="text-align:center;">\[h(x) = -2(x - 4)^2 + 9\]</p>',
            r'What is the <b>maximum</b> value of \(h(x)\)?',
            ['9'], '9',
            r'Hàm bậc hai dạng đỉnh \(h(x) = a(x - h)^2 + k\) có \(a = -2 < 0\) nên parabol úp xuống và đạt giá trị lớn nhất (maximum) ngay tại đỉnh \((4, 9)\). Do đó giá trị lớn nhất của \(h(x)\) là tung độ đỉnh \(k = 9\) (đạt được khi \(x = 4\)).',
            r'Giá trị cực đại/cực tiểu của parabol \(a(x - h)^2 + k\) luôn là TUNG ĐỘ đỉnh \(k\) (còn \(h\) là vị trí \(x\) nơi cực trị xảy ra)!',
            r'Vẽ `y = -2(x - 4)^2 + 9` trên Desmos → bấm đỉnh cao nhất `(4, 9)` → giá trị lớn nhất của hàm là `9`.'
        ),
        # Q14 — Advanced Math (Medium, MCQ -> A)
        math_mcq(
            'sat_mm6_m2l_q14', 14, 'Advanced Math', 'Nonlinear functions', 'Medium',
            r'<p>In a coral nursery aquaculture tank, a colony starts with \(80\) polyps and doubles in size every \(3\) months according to the model:</p><p style="text-align:center;">\[P(t) = 80(2)^{t/3}\]</p><p>where \(P(t)\) is the predicted number of polyps after \(t\) months.</p>',
            r'How many polyps are predicted to be in the colony after \(9\) months?',
            {'A': r'\(640\)', 'B': r'\(240\)', 'C': r'\(480\)', 'D': r'\(720\)'},
            'A',
            r'Thay \(t = 9\) vào hàm số: số chu kỳ nhân đôi là \(\dfrac{9}{3} = 3\) chu kỳ.<br>\(P(9) = 80 \cdot 2^{9/3} = 80 \cdot 2^3 = 80 \cdot 8 = 640\) polyps.',
            r'Với hàm nhân đôi theo chu kỳ \(2^{t/3}\), luôn chia thời gian cho độ dài chu kỳ (\(9/3 = 3\)) rồi tính lũy thừa \(2^3 = 8\) (không nhân \(2 \times 3 = 6\))!',
            {
                'A': ('Đáp án đúng', r'\(80 \times 2^3 = 80 \times 8 = 640\).'),
                'B': ('Nhầm nhân tuyến tính với 3', r'Tính \(80 \times 3 = 240\) thay vì nhân với \(2^3 = 8\).'),
                'C': ('Nhầm 2³ thành 2 × 3 = 6', r'Tính nhầm \(80 \times 6 = 480\) thay vì \(80 \times 8 = 640\).'),
                'D': ('Nhân trực tiếp với t = 9', r'Tính nhầm \(80 \times 9 = 720\).'),
            },
            r'Gõ thẳng `80 * 2^(9/3)` vào Desmos ra ngay `640`.'
        ),
        # Q15 — Advanced Math (Medium, MCQ -> B)
        math_mcq(
            'sat_mm6_m2l_q15', 15, 'Advanced Math', 'Nonlinear equations in one variable and systems of equations in two variables', 'Medium',
            r'<p>Consider the radical equation shown below:</p><p style="text-align:center;">\[\sqrt{x + 9} = 7\]</p>',
            r'What is the value of \(x\)?',
            {'A': r'\(5\)', 'B': r'\(40\)', 'C': r'\(58\)', 'D': r'\(16\)'},
            'B',
            r'Bình phương cả hai vế để khử căn bậc hai: \(x + 9 = 7^2 = 49 \Rightarrow x = 49 - 9 = 40\). Thử lại: \(\sqrt{40 + 9} = \sqrt{49} = 7\) (đúng!).',
            r'Để giải \(\sqrt{A} = B\) (với \(B \ge 0\)), bình phương hai vế thành \(A = B^2\) rồi chuyển vế tìm \(x\).',
            {
                'A': ('Nhầm 7² thành 14', r'Tính \(7 \times 2 = 14 \Rightarrow 14 - 9 = 5\) thay vì \(7^2 = 49\).'),
                'B': ('Đáp án đúng', r'\(x + 9 = 49 \Rightarrow x = 40\).'),
                'C': ('Cộng thay vì trừ 9', r'Tính \(49 + 9 = 58\) thay vì \(49 - 9 = 40\).'),
                'D': ('Quên bình phương vế phải', r'Cộng nhầm \(7 + 9 = 16\).'),
            },
            r'Vẽ `y = sqrt(x + 9)` và `y = 7` trên Desmos (kéo trục Ox tới 50) → bấm giao điểm đọc ngay `(40, 7)`!'
        ),
        # Q16 — PSDA (Easy, SPR -> 175)
        math_spr(
            'sat_mm6_m2l_q16', 16, 'Problem-Solving and Data Analysis', 'Ratios, rates, proportional relationships, and units', 'Easy',
            r'<p>A long-range commercial delivery drone flies \(105\) kilometers in \(3\) hours at a constant cruising speed.</p>',
            r'At this same constant speed, how many kilometers will the drone fly in \(5\) hours?',
            ['175'], '175',
            r'Tìm tốc độ bay mỗi giờ (unit rate): \(\dfrac{105\text{ km}}{3\text{ giờ}} = 35\text{ km/giờ}\). Quãng đường bay trong \(5\) giờ: \(35 \times 5 = 175\text{ km}\).',
            r'Với bài toán tỉ lệ thuận (constant speed), tìm ngay tốc độ trong 1 giờ (\(105/3 = 35\)) rồi nhân với số giờ mới (\(5\))!',
            r'Gõ `(105 / 3) * 5` trên Desmos ra ngay `175`.'
        ),
        # Q17 — PSDA (Easy, MCQ -> C)
        math_mcq(
            'sat_mm6_m2l_q17', 17, 'Problem-Solving and Data Analysis', 'Percentages', 'Easy',
            r'<p>A coral nursery cultivated \(320\) staghorn coral fragments this quarter. Of these fragments, \(35\%\) reached the target size for reef outplanting.</p>',
            r'How many coral fragments reached the target size for reef outplanting?',
            {'A': r'\(96\)', 'B': r'\(105\)', 'C': r'\(112\)', 'D': r'\(208\)'},
            'C',
            r'Đổi \(35\% = 0.35\) rồi nhân với tổng số mảnh san hô: \(0.35 \times 320 = 112\) mảnh. (Nhẩm nhanh: \(10\%\) là \(32 \Rightarrow 30\%\) là \(96\), cộng thêm \(5\%\) là \(16 \Rightarrow 96 + 16 = 112\).)',
            r'Công thức phần trăm cơ bản: \(\text{Part} = \frac{p}{100} \times \text{Whole}\).',
            {
                'A': ('Chỉ tính 30%', r'\(0.30 \times 320 = 96\), quên cộng thêm \(5\%\) (\(16\)).'),
                'B': ('Nhân nhầm số nguyên', r'Tính sai \(35\% \times 300 = 105\) thay vì \(320\).'),
                'C': ('Đáp án đúng', r'\(0.35 \times 320 = 112\).'),
                'D': ('Tính nhầm phần bù 65%', r'\(208 = 320 - 112\) là số mảnh CHƯA đạt kích thước.'),
            },
            r'Gõ `0.35 * 320` vào Desmos ra ngay `112`.'
        ),
        # Q18 — PSDA (Medium, MCQ -> D)
        math_mcq(
            'sat_mm6_m2l_q18', 18, 'Problem-Solving and Data Analysis', 'One-variable data: Distributions and measures of center and spread', 'Medium',
            tbl_q18 + r'<p>The table above shows the daily micro-tremor counts recorded over \(7\) days at Seismic Station West.</p>',
            r'What is the <b>median</b> daily tremor count for these \(7\) days?',
            {'A': r'\(16\)', 'B': r'\(18\)', 'C': r'\(20\)', 'D': r'\(19\)'},
            'D',
            r'Bước 1 (BẮT BUỘC): Sắp xếp \(7\) số theo thứ tự tăng dần:<br>\(14,\; 16,\; 18,\; \mathbf{19},\; 22,\; 25,\; 27\).<br>Bước 2: Với \(n = 7\) số, trung vị (median) là phần tử đứng chính giữa (vị trí thứ \(\frac{7 + 1}{2} = 4\)), tức là \(19\).',
            r'TUYỆT ĐỐI không lấy số đứng giữa của bảng chưa sắp xếp (ở đây Thu = 16 là bẫy!) — luôn xếp tăng dần trước khi tìm Median!',
            {
                'A': ('Bẫy không sắp xếp dữ liệu', r'\(16\) chỉ là giá trị ngày thứ Tư (ô giữa bảng) khi chưa sắp xếp theo thứ tự tăng dần!'),
                'B': ('Đếm lệch 1 vị trí', r'\(18\) là giá trị nhỏ thứ 3, chưa phải giá trị thứ 4.'),
                'C': ('Tính xấp xỉ trung bình cộng', r'Mean \(\approx 20.1\), đề bài hỏi Median (trung vị).'),
                'D': ('Đáp án đúng', r'Dãy xếp tăng dần có phần tử thứ 4 đúng bằng \(19\).'),
            },
            r'Gõ `median(19, 14, 27, 16, 22, 18, 25)` vào Desmos — máy tự sắp xếp và trả ngay `19`!'
        ),
        # Q19 — PSDA (Medium, SPR -> 3/20 or 0.15)
        math_spr(
            'sat_mm6_m2l_q19', 19, 'Problem-Solving and Data Analysis', 'Probability and conditional probability', 'Medium',
            tbl_q19 + r'<p>The table above summarizes an inventory batch of \(160\) prints at a digital printmaking studio, categorized by paper size and surface finish.</p>',
            r'If one print is selected at random from <b>all \(160\) prints</b>, what is the probability that it is a <b>Large</b> print with a <b>Glossy</b> finish?',
            ['3/20', '0.15', '.15'], '3/20 (or 0.15)',
            r'Số bản in vừa cỡ <b>Large</b> vừa phủ <b>Glossy</b> đọc tại ô giao giữa hàng Large và cột Glossy là \(24\). Chọn ngẫu nhiên trong toàn bộ \(160\) bản in nên xác suất là \(\dfrac{24}{160} = \dfrac{3}{20} = 0.15\).',
            r'Khi đề nói "selected at random from all 160 prints", mẫu số chính là tổng toàn bảng (\(160\)) và tử số là đúng ô giao nhau (\(24\)).',
            r'Gõ `24 / 160` trên Desmos ra `0.15` (bấm nút phân số bên trái sẽ đổi thành `3/20`).'
        ),
        # Q20 — Geometry & Trig (Easy, MCQ -> A)
        math_mcq(
            'sat_mm6_m2l_q20', 20, 'Geometry and Trigonometry', 'Lines, angles, and triangles', 'Easy',
            f'<div style="text-align:center;margin-bottom:10px;">{svg_q20}</div>' + r'<p>In right triangle \(ABC\) shown above, \(\angle B = 90^\circ\) and \(\angle C = 34^\circ\).</p>',
            r'What is the value of \(x\)?',
            {'A': r'\(56\)', 'B': r'\(34\)', 'C': r'\(66\)', 'D': r'\(146\)'},
            'A',
            r'Tổng ba góc trong tam giác bằng \(180^\circ\). Vì \(\angle B = 90^\circ\), hai góc nhọn phụ nhau nên tổng bằng \(90^\circ\): \(x = 90 - 34 = 56\).',
            r'Trong tam giác vuông, hai góc nhọn luôn cộng lại đúng bằng \(90^\circ\)!',
            {
                'A': ('Đáp án đúng', r'\(90 - 34 = 56\).'),
                'B': ('Nhầm hai góc bằng nhau', r'\(34^\circ\) là số đo góc \(C\), không phải góc \(A\).'),
                'C': ('Trừ nhầm từ 100', r'Tính \(100 - 34 = 66\) thay vì \(90 - 34 = 56\).'),
                'D': ('Quên trừ góc vuông 90°', r'Tính \(180 - 34 = 146\) mà quên trừ \(\angle B = 90^\circ\).'),
            },
            r'Gõ `90 - 34` trên Desmos ra ngay `56`.'
        ),
        # Q21 — Geometry & Trig (Medium, MCQ -> B)
        math_mcq(
            'sat_mm6_m2l_q21', 21, 'Geometry and Trigonometry', 'Circles', 'Medium',
            f'<div style="text-align:center;margin-bottom:10px;">{svg_q21}</div>' + r'<p>The circular floor of an observatory dome has center \(O\) and radius \(12\) meters. Shaded sector \(AOB\) has a central angle of \(60^\circ\), as shown above.</p>',
            r'What is the <b>area</b> of shaded sector \(AOB\), in square meters?',
            {'A': r'\(12\pi\)', 'B': r'\(24\pi\)', 'C': r'\(4\pi\)', 'D': r'\(144\pi\)'},
            'B',
            r'Diện tích hình quạt tròn bằng tỉ lệ góc ở tâm nhân diện tích cả hình tròn \(\pi r^2\):<br>\(\text{Area} = \dfrac{60^\circ}{360^\circ} \cdot \pi(12^2) = \dfrac{1}{6} \cdot 144\pi = 24\pi\text{ m}^2\).',
            r'Góc \(60^\circ\) chiếm đúng \(\dfrac{1}{6}\) hình tròn — tính diện tích cả hình tròn \(\pi(12^2) = 144\pi\) rồi chia \(6\) ra ngay \(24\pi\)!',
            {
                'A': ('Quên bình phương hoặc chia đôi nhầm', r'Tính nhầm \(\frac{1}{6} \cdot 72\pi = 12\pi\).'),
                'B': ('Đáp án đúng', r'\(\frac{60}{360} \cdot \pi(12)^2 = \frac{144\pi}{6} = 24\pi\).'),
                'C': ('Tính nhầm Độ dài cung tròn', r'\(\frac{60}{360} \cdot 2\pi(12) = 4\pi\) là độ dài cung \(\widehat{AB}\), không phải diện tích hình quạt.'),
                'D': ('Quên nhân tỉ lệ 60°/360°', r'\(144\pi\) là diện tích CẢ hình tròn, chưa lấy phần quạt \(60^\circ\).'),
            },
            r'Gõ `(60/360) * 12^2` trên Desmos ra `24` → gắn `π` được `24π`.'
        ),
        # Q22 — Geometry & Trig (Medium, SPR -> 360)
        math_spr(
            'sat_mm6_m2l_q22', 22, 'Geometry and Trigonometry', 'Area and volume', 'Medium',
            f'<div style="text-align:center;margin-bottom:10px;">{svg_q22}</div>' + r'<p>A cylindrical coral nursery filtration tank has a base radius of \(6\) feet and a height of \(10\) feet, as shown in the figure above.</p>',
            r'If the volume of the tank is \(k\pi\) cubic feet, what is the value of \(k\)?',
            ['360'], '360',
            r'Áp dụng công thức thể tích hình trụ tròn xoay (có sẵn trong SAT Reference Sheet):<br>\(V = \pi r^2 h = \pi(6^2)(10) = 36 \times 10\pi = 360\pi\text{ ft}^3\).<br>Vậy \(k = 360\).',
            r'Thể tích hình trụ là \(V = \pi r^2 h\): nhớ BÌNH PHƯƠNG bán kính (\(6^2 = 36\)) trước khi nhân với chiều cao \(h = 10\)!',
            r'Gõ `6^2 * 10` trên Desmos ra ngay `360`.'
        ),
    ]


if __name__ == '__main__':
    assert verify_math()
    qs = get_m2l_questions()
    print(f"M2L verified: {len(qs)} questions")
