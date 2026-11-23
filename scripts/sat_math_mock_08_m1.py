# -*- coding: utf-8 -*-
"""
Digital SAT Math Adaptive Mock Test #8 — Module 1 (Routing Module, 22 Questions)
Themes: Geothermal Power Wells, Autonomous Warehouse Conveyor Robotics,
        Violin Luthier Acoustics & Wood Curing, National Park Wildlife Census & Tagging,
        Stepped-Pyramid & Truncated-Cone Monument Geometry.
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
    # Q1: 4(3x - 5) + 7 = 5x + 15 => 7x = 28 => x = 4 => 2x + 3 = 11
    x1 = Fraction(15 + 20 - 7, 12 - 5)
    assert x1 == 4 and 4 * (3 * x1 - 5) + 7 == 5 * x1 + 15 and 2 * x1 + 3 == 11

    # Q2: T(k) = 28k + 15 => T(0) = 15 (surface temperature at depth 0 km)
    assert 28 * 0 + 15 == 15 and (28 * 1 + 15) - (28 * 0 + 15) == 28

    # Q3: linear f(3) = 19, f(8) = 44 => m = 5, b = 4 => f(12) = 64
    m3 = Fraction(44 - 19, 8 - 3)
    b3 = 19 - m3 * 3
    assert m3 == 5 and b3 == 4 and m3 * 12 + b3 == 64

    # Q4: x + y = 14, 65x + 95y = 1090 => x = 8, y = 6
    x4 = Fraction(95 * 14 - 1090, 95 - 65)
    y4 = 14 - x4
    assert x4 == 8 and y4 == 6 and 65 * x4 + 95 * y4 == 1090

    # Q5 (SPR): 4x + 6y = 21, 8x - ky = 35 no solution => -k/6 = 8/4 = 2 => k = -12
    k5 = -Fraction(8, 4) * 6
    assert k5 == -12 and Fraction(-k5, 6) == Fraction(8, 4) and Fraction(35, 21) != Fraction(8, 4)

    # Q6: 5x - 2y = 20 => m = 5/2 => perp = -2/5 through (10, 3) => b = 7
    m6_p = Fraction(5, 2)
    m6_q = -Fraction(1, m6_p)
    b6_q = 3 - m6_q * 10
    assert m6_q == Fraction(-2, 5) and b6_q == 7 and m6_q * 10 + b6_q == 3

    # Q7: 35(22) + 60y <= 1900 => y <= 1130/60 = 18.833... => max int 18
    assert 35 * 22 + 60 * 18 <= 1900 and 35 * 22 + 60 * 19 > 1900

    # Q8: 7x - 2y = 43, 2x + 5y = 20 => add => 9x + 3y = 63 => 3x + y = 21
    x8 = Fraction(43 * 5 + 20 * 2, 7 * 5 + 2 * 2)
    y8 = Fraction(20 - 2 * x8, 5)
    assert 7 * x8 - 2 * y8 == 43 and 2 * x8 + 5 * y8 == 20 and 3 * x8 + y8 == 21

    # Q9 (SPR): f(x) = a(x - 5)^2 - 3, f(8) = 15 => a = 2 => f(1) = 29
    a9 = Fraction(15 - (-3), (8 - 5) ** 2)
    assert a9 == 2 and a9 * (1 - 5) ** 2 - 3 == 29

    # Q10: 4x^2 + 24x + c = 0 exact one real solution => 24^2 - 16c = 0 => c = 36
    c10 = Fraction(24 ** 2, 4 * 4)
    assert c10 == 36 and 24 ** 2 - 4 * 4 * c10 == 0

    # Q11: (x^2 - 16)/(x^2 - x - 12) = (x + 4)/(x + 3) for x > 4
    for xv in (5, 7, 10):
        assert Fraction(xv ** 2 - 16, xv ** 2 - xv - 12) == Fraction(xv + 4, xv + 3)

    # Q12: M(t) = 24(0.92)^t => weekly percent decrease = (1 - 0.92) * 100 = 8%
    assert (1 - Fraction(92, 100)) * 100 == 8

    # Q13 (SPR): 4x^2 - 32x + 19 = 0 => Delta = 720 > 0, sum = 32/4 = 8
    assert (-32) ** 2 - 4 * 4 * 19 == 720 > 0 and Fraction(32, 4) == 8

    # Q14: sqrt(5x + 11) = x + 1 => x^2 - 3x - 10 = 0 => x = 5 valid, x = -2 extraneous
    assert math.isclose(math.sqrt(5 * 5 + 11), 5 + 1) and (-2 + 1) < 0

    # Q15: y = x^2 - 5x + 10 and y = 2x - 2 => x = 3 (y=4) or x = 4 (y=6); x > 3.5 => 4 + 6 = 10
    assert 3 ** 2 - 5 * 3 + 10 == 2 * 3 - 2 == 4
    assert 4 ** 2 - 5 * 4 + 10 == 2 * 4 - 2 == 6
    assert 4 + 6 == 10

    # Q16 (SPR): 2160 in^2 / 144 = 15 ft^2
    assert Fraction(2160, 12 ** 2) == 15

    # Q17: P(GPS-Tagged | Alpine Ridge) = 27 / 45 = 3/5
    assert 27 + 18 == 45 and 36 + 44 == 80 and 17 + 58 == 75
    assert 45 + 80 + 75 == 200 and 27 + 36 + 17 == 80 and 18 + 44 + 58 == 120
    assert Fraction(27, 45) == Fraction(3, 5)

    # Q18: Geothermal pressure frequency table (n = 15): mean = 22, median = 20 => diff = 2
    data18 = [15] * 2 + [18] * 4 + [20] * 5 + [26] * 3 + [50] * 1
    assert len(data18) == 15
    mean18 = Fraction(sum(data18), len(data18))
    median18 = data18[7]
    assert mean18 == 22 and median18 == 20 and mean18 - median18 == 2

    # Q19 (SPR): p = 150% of q, q = 30% of r => p = 45% of r
    assert Fraction(150, 100) * Fraction(30, 100) == Fraction(45, 100)

    # Q20: alternate exterior angles 5x + 14 = 3x + 62 => x = 24 => obtuse = 134 => acute = 46
    x20 = Fraction(62 - 14, 5 - 3)
    obtuse20 = 5 * x20 + 14
    acute20 = 180 - obtuse20
    assert x20 == 24 and obtuse20 == 3 * x20 + 62 == 134 and acute20 == 46

    # Q21: sector radius 12, angle 75 deg => area = (75/360) * 144 pi = 30 pi
    assert Fraction(75, 360) * (12 ** 2) == 30

    # Q22 (SPR): right triangle PQR, angle Q = 90, PR = 51, cos(P) = 8/17 => PQ = 24, QR = 45
    pq22 = 51 * Fraction(8, 17)
    qr22 = math.isqrt(51 ** 2 - int(pq22) ** 2)
    assert pq22 == 24 and qr22 == 45 and 24 ** 2 + 45 ** 2 == 51 ** 2

    return True


def get_m1_questions():
    svg_q9 = svg_parabola_vertex(
        '5', '-3', opens_up=True, pt_lbl='(8, 15)',
        note='Graph of y = f(x) (not to scale)'
    )
    tbl_q17 = build_math_table(
        ['Habitat Zone', 'GPS-Tagged', 'Untagged', 'Total'],
        [
            ['Alpine Ridge', '27', '18', '45'],
            ['Canyon Floor', '36', '44', '80'],
            ['Pine Basin', '17', '58', '75'],
            ['Total', '80', '120', '200'],
        ],
        caption='National Park Elk Wildlife Census and GPS Tagging'
    )
    tbl_q18 = build_math_table(
        ['Steam Pressure (bars)', 'Number of Wells'],
        [
            ['15', '2'],
            ['18', '4'],
            ['20', '5'],
            ['26', '3'],
            ['50', '1'],
        ],
        caption='Daily Wellhead Steam Pressure Across 15 Geothermal Wells'
    )
    svg_q20 = svg_parallel_transversal(
        'ℓ', 'm', ang1_lbl='(5x + 14)°', ang2_lbl='', ang3_lbl='(3x + 62)°'
    )
    svg_q21 = svg_circle_sector(
        'r = 12', '75°', center_lbl='O', pt_a='A', pt_b='B',
        note='Circular Monument Courtyard Sector'
    )
    svg_q22 = svg_right_triangle(
        'PQ', 'QR', '51', angle_top_left='P',
        v_top='P', v_right_angle='Q', v_right='R',
        note='cos(P) = 8/17'
    )

    return [
        # Q1 — Algebra (Easy, MCQ -> C)
        math_mcq(
            'sat_mm8_m1_q1', 1, 'Algebra', 'Linear equations in one variable', 'Easy',
            r'<p>Consider the linear equation shown below:</p><p style="text-align:center;font-size:18px;">\[4(3x - 5) + 7 = 5x + 15\]</p>',
            r'What is the value of \(2x + 3\)?',
            {'A': r'\(4\)', 'B': r'\(5\)', 'C': r'\(11\)', 'D': r'\(14\)'},
            'C',
            r'Khai triển vế trái: \(12x - 20 + 7 = 5x + 15 \Rightarrow 12x - 13 = 5x + 15 \Rightarrow 7x = 28 \Rightarrow x = 4\). Thay \(x = 4\) vào biểu thức đề hỏi: \(2(4) + 3 = 11\).',
            r'Luôn kiểm tra kỹ biểu thức đề hỏi cuối cùng (\(2x + 3\)) sau khi giải xong \(x\) để tránh bẫy dừng sớm ở \(x = 4\).',
            {
                'A': ('Stopped at x', r'\(4\) mới là nghiệm \(x\), chưa thay vào \(2x + 3\).'),
                'B': ('Subtracted Instead of Added', r'Tính nhầm \(2(4) - 3 = 5\) thay vì \(2(4) + 3\).'),
                'C': ('Correct', r'\(x = 4 \Rightarrow 2(4) + 3 = 11\).'),
                'D': ('Sign Error on Constant', r'Tính sai \(-20 + 7 = -27\) hoặc cộng nhầm hằng số.'),
            },
            r'Gõ `4(3x - 5) + 7 = 5x + 15` vào Desmos để đọc đường thẳng đứng `x = 4`, sau đó tính `2(4) + 3 = 11`.'
        ),
        # Q2 — Algebra (Easy, MCQ -> A) | Theme: Geothermal Power Wells
        math_mcq(
            'sat_mm8_m1_q2', 2, 'Algebra', 'Linear functions', 'Easy',
            r'<p>A geothermal engineering team models the subsurface rock temperature \(T(k)\), in degrees Celsius, at a drilling depth of \(k\) kilometers using the linear function:</p><p style="text-align:center;">\[T(k) = 28k + 15\]</p>',
            r'Which of the following is the best interpretation of the number \(15\) in this context?',
            {
                'A': r'The estimated rock temperature at the ground surface (\(0\) kilometers depth) is \(15^\circ\text{C}\).',
                'B': r'The rock temperature increases by \(15^\circ\text{C}\) for each additional kilometer drilled.',
                'C': r'The maximum drilling depth of the geothermal well is \(15\) kilometers.',
                'D': r'The rock temperature increases by \(28^\circ\text{C}\) every \(15\) kilometers.',
            },
            'A',
            r'Trong hàm bậc nhất \(T(k) = 28k + 15\), hằng số tự do \(b = 15\) là giá trị \(T(0) = 15\), biểu thị nhiệt độ đá ước tính ngay tại bề mặt đất (độ sâu \(0\) km). Hệ số góc \(28\) mới là mức tăng nhiệt độ trên mỗi km khoan sâu thêm.',
            r'Trong mô hình \(y = mx + b\), hằng số \(b\) luôn ứng với giá trị ban đầu khi biến độc lập bằng \(0\) (\(k = 0\)).',
            {
                'A': ('Correct', r'Tại \(k = 0\) km (mặt đất), \(T(0) = 15^\circ\text{C}\).'),
                'B': ('Confused Intercept with Slope', r'Mức tăng theo mỗi km là hệ số góc \(28^\circ\text{C}\), không phải \(15^\circ\text{C}\).'),
                'C': ('Misread Unit & Domain', r'\(15\) có đơn vị là độ C (đầu ra \(T\)), không phải độ sâu tối đa tính bằng km.'),
                'D': ('Misread Slope Ratio', r'Hệ số góc \(28\) là tăng \(28^\circ\text{C}\) cho mỗi \(1\) km, không phải mỗi \(15\) km.'),
            },
            r'Thay trực tiếp `k = 0` vào `28(0) + 15 = 15` để xác nhận đây là nhiệt độ ở bề mặt đất.'
        ),
        # Q3 — Algebra (Easy, MCQ -> D) | Theme: Warehouse Conveyor Robotics
        math_mcq(
            'sat_mm8_m1_q3', 3, 'Algebra', 'Linear functions', 'Easy',
            r'<p>An autonomous warehouse conveyor controller tracks cumulative energy consumption \(f(t)\), in kilowatt-hours, as a linear function of operating hours \(t\). It is given that \(f(3) = 19\) and \(f(8) = 44\).</p>',
            r'What is the value of \(f(12)\)?',
            {'A': r'\(56\)', 'B': r'\(60\)', 'C': r'\(62\)', 'D': r'\(64\)'},
            'D',
            r'Tính hệ số góc: \(m = \frac{44 - 19}{8 - 3} = \frac{25}{5} = 5\). Suy ra tung độ gốc: \(b = 19 - 5(3) = 4\), nên \(f(t) = 5t + 4\). Thay \(t = 12\): \(f(12) = 5(12) + 4 = 64\).',
            r'Có thể tính nhanh bằng bước nhảy: tăng \(4\) giờ từ \(t = 8\) lên \(t = 12\) làm \(f(t)\) tăng \(4 \times 5 = 20\), nên \(44 + 20 = 64\).',
            {
                'A': ('Wrong Step Increment', r'Chỉ cộng thêm \(12\) vào \(44\) thay vì \(4 \times 5 = 20\).'),
                'B': ('Forgot y-intercept b = 4', r'Tính \(5(12) = 60\) mà bỏ quên hằng số \(b = 4\).'),
                'C': ('Arithmetic Slip', r'Cộng nhầm \(44 + 18 = 62\).'),
                'D': ('Correct', r'\(f(12) = 5(12) + 4 = 64\).'),
            },
            r'Nhập bảng `x1 = [3, 8]`, `y1 = [19, 44]` rồi gõ hồi quy `y1 ~ m x1 + b` trên Desmos; tính `m(12) + b` ra ngay `64`.'
        ),
        # Q4 — Algebra (Medium, MCQ -> B) | Theme: Violin Luthier Wood Curing
        math_mcq(
            'sat_mm8_m1_q4', 4, 'Algebra', 'Systems of two linear equations in two variables', 'Medium',
            r'<p>A violin luthier orders \(14\) seasoned tonewood blanks for a workshop batch: aged spruce soundboard blanks cost $65 each, and flamed maple back blanks cost $95 each. The total cost of the order is $1,090.</p>',
            r'How many aged spruce soundboard blanks did the luthier order?',
            {'A': r'\(6\)', 'B': r'\(8\)', 'C': r'\(9\)', 'D': r'\(10\)'},
            'B',
            r'Gọi \(x\) là số phôi gỗ vân sam (spruce) và \(y\) là số phôi gỗ phong (maple). Ta có hệ phương trình: \(x + y = 14\) và \(65x + 95y = 1{,}090\). Thế \(y = 14 - x\) vào phương trình hai: \(65x + 95(14 - x) = 1{,}090 \Rightarrow 1{,}330 - 30x = 1{,}090 \Rightarrow 30x = 240 \Rightarrow x = 8\).',
            r'Xác định rõ ẩn nào là spruce (\(x\)) và ẩn nào là maple (\(y\)) ngay khi đặt hệ để tránh khoanh nhầm \(y = 6\).',
            {
                'A': ('Solved for Wrong Variable', r'\(6\) là số phôi gỗ phong (maple), trong khi đề hỏi số phôi gỗ vân sam (spruce).'),
                'B': ('Correct', r'\(8\) phôi spruce ($520) và \(6\) phôi maple ($570) có tổng đúng $1,090.'),
                'C': ('Arithmetic Error', r'Với \(9\) spruce và \(5\) maple, tổng tiền là $1,060 \(\neq\) $1,090.'),
                'D': ('Arithmetic Error', r'Với \(10\) spruce và \(4\) maple, tổng tiền là $1,030 \(\neq\) $1,090.'),
            },
            r'Gõ thẳng hệ `x + y = 14` và `65x + 95y = 1090` vào Desmos → bấm giao điểm `(8, 6)` → đọc ngay `x = 8`!'
        ),
        # Q5 — Algebra (Medium, SPR -> -12)
        math_spr(
            'sat_mm8_m1_q5', 5, 'Algebra', 'Systems of two linear equations in two variables', 'Medium',
            r'<p>Consider the system of linear equations below, where \(k\) is a constant:</p><p style="text-align:center;">\[\begin{cases} 4x + 6y = 21 \\ 8x - ky = 35 \end{cases}\]</p>',
            r'If the system has <b>no solution</b>, what is the value of \(k\)?',
            ['-12'], '-12',
            r'Hệ hai phương trình bậc nhất vô nghiệm khi hai đường thẳng song song nhưng không trùng nhau, tức tỉ số hệ số của \(x\) và \(y\) bằng nhau nhưng khác tỉ số hằng số tự do: \(\frac{8}{4} = \frac{-k}{6} \neq \frac{35}{21}\). Ta có \(2 = \frac{-k}{6} \Rightarrow -k = 12 \Rightarrow k = -12\). Kiểm tra hằng số: \(\frac{35}{21} = \frac{5}{3} \neq 2\) (thỏa mãn vô nghiệm!).',
            r'Chú ý dấu trừ đứng trước \(ky\): hệ số của \(y\) ở phương trình dưới là \(-k\), không phải \(+k\)!',
            r'Gõ `4x + 6y = 21` và `8x - ky = 35` vào Desmos, thêm thanh trượt `k` (từ `-20` đến `20`) → kéo đến `k = -12` thấy hai đường thẳng song song!'
        ),
        # Q6 — Algebra (Medium, MCQ -> A)
        math_mcq(
            'sat_mm8_m1_q6', 6, 'Algebra', 'Linear equations in two variables', 'Medium',
            r'<p>In the \(xy\)-plane, line \(p\) is defined by the equation \(5x - 2y = 20\). Line \(q\) is <b>perpendicular</b> to line \(p\) and passes through the point \((10, 3)\).</p>',
            r'Which of the following is an equation of line \(q\)?',
            {
                'A': r'\(y = -\frac{2}{5}x + 7\)',
                'B': r'\(y = \frac{2}{5}x - 1\)',
                'C': r'\(y = \frac{5}{2}x - 22\)',
                'D': r'\(y = -\frac{5}{2}x + 28\)',
            },
            'A',
            r'Đưa đường thẳng \(p\) về dạng \(y = mx + b\): \(-2y = -5x + 20 \Rightarrow y = \frac{5}{2}x - 10\), nên \(m_p = \frac{5}{2}\). Đường thẳng \(q\) vuông góc với \(p\) có hệ số góc nghịch đảo đổi dấu: \(m_q = -\frac{2}{5}\). Thay \((10, 3)\) vào \(y = -\frac{2}{5}x + b\): \(3 = -\frac{2}{5}(10) + b = -4 + b \Rightarrow b = 7\). Vậy \(y = -\frac{2}{5}x + 7\).',
            r'Hệ số góc đường vuông góc luôn là nghịch đảo ĐỔI DẤU: \(+\frac{5}{2} \to -\frac{2}{5}\).',
            {
                'A': ('Correct', r'Hệ số góc \(-\frac{2}{5}\) vuông góc với \(\frac{5}{2}\) và đi qua \((10, 3)\).'),
                'B': ('Forgot Negative Sign', r'Nghịch đảo thành \(\frac{2}{5}\) nhưng quên đổi sang dấu âm.'),
                'C': ('Parallel Instead of Perpendicular', r'Giữ nguyên hệ số góc \(\frac{5}{2}\) của đường song song.'),
                'D': ('Forgot Reciprocal', r'Chỉ đổi dấu thành \(-\frac{5}{2}\) mà không nghịch đảo phân số.'),
            },
            r'Vẽ `5x - 2y = 20`, chấm điểm `(10, 3)` và nhập phương án A trên Desmos để xác nhận góc vuông và giao điểm chính xác.'
        ),
        # Q7 — Algebra (Medium, MCQ -> C) | Theme: Warehouse Conveyor Robotics
        math_mcq(
            'sat_mm8_m1_q7', 7, 'Algebra', 'Linear inequalities in one or two variables', 'Medium',
            r'<p>An automated warehouse conveyor belt has a maximum load limit of \(1{,}900\) kilograms. It is currently carrying \(22\) electronics bins weighing \(35\) kilograms each, and a robotic arm is loading \(y\) heavy battery packs weighing \(60\) kilograms each.</p>',
            r'What is the <b>maximum</b> number of heavy battery packs that can be added without exceeding the conveyor belt\'s load limit?',
            {'A': r'\(17\)', 'B': r'\(19\)', 'C': r'\(18\)', 'D': r'\(31\)'},
            'C',
            r'Thiết lập bất phương trình tải trọng: \(35(22) + 60y \le 1{,}900 \Rightarrow 770 + 60y \le 1{,}900 \Rightarrow 60y \le 1{,}130 \Rightarrow y \le \frac{1{,}130}{60} \approx 18.83\). Vì số gói pin là số nguyên không được vượt quá giới hạn tải, giá trị nguyên lớn nhất là \(18\).',
            r'Khi ràng buộc là "không vượt quá" (\(y \le 18.83\)), LUÔN làm tròn XUỐNG (\(18\)), tuyệt đối không làm tròn lên \(19\)!',
            {
                'A': ('Undercounted by 1', r'Với \(17\) gói pin, tổng tải mới là \(1{,}790\) kg — vẫn tải thêm được \(1\) gói nữa.'),
                'B': ('Rounded Up Trap', r'Làm tròn \(18.83 \to 19\) làm tổng tải lên \(1{,}910 > 1{,}900\) kg (quá tải!).'),
                'C': ('Correct', r'\(770 + 60(18) = 1{,}850 \le 1{,}900\) kg, tối đa đúng \(18\) gói.'),
                'D': ('Ignored Existing Bins', r'Lấy \(1{,}900 / 60 \approx 31.67\) mà quên trừ \(770\) kg của \(22\) thùng linh kiện.'),
            },
            r'Gõ `(1900 - 35*22) / 60` vào Desmos ra `18.833...` → lấy phần nguyên dưới là `18`.'
        ),
        # Q8 — Algebra (Medium-Hard, MCQ -> D)
        math_mcq(
            'sat_mm8_m1_q8', 8, 'Algebra', 'Systems of two linear equations in two variables', 'Medium-Hard',
            r'<p>In the system of equations below, \((x, y)\) is the solution:</p><p style="text-align:center;">\[\begin{cases} 7x - 2y = 43 \\ 2x + 5y = 20 \end{cases}\]</p>',
            r'What is the value of \(3x + y\)?',
            {'A': r'\(7\)', 'B': r'\(14\)', 'C': r'\(63\)', 'D': r'\(21\)'},
            'D',
            r'Cộng vế theo vế hai phương trình: \((7x + 2x) + (-2y + 5y) = 43 + 20 \Rightarrow 9x + 3y = 63\). Chia cả hai vế cho \(3\) ta thu ngay \(3x + y = 21\) mà không cần giải nghiệm phân số lẻ \(x = \frac{85}{13}, y = \frac{18}{13}\).',
            r'Trước khi giải riêng \(x\) và \(y\), luôn thử cộng hoặc trừ 2 phương trình xem có ra bội số của biểu thức đề hỏi không!',
            {
                'A': ('Divided Twice by 3', r'Chia nhầm \(63 / 9 = 7\) thay vì chia cho \(3\).'),
                'B': ('Arithmetic Slip', r'Cộng nhầm hoặc trừ sai vế phải.'),
                'C': ('Forgot to Divide by 3', r'\(63\) là giá trị của \(9x + 3y\), cần chia \(3\) để ra \(3x + y\).'),
                'D': ('Correct', r'\(9x + 3y = 63 \Rightarrow 3x + y = 21\).'),
            },
            r'Cộng nhẩm ra `9x + 3y = 63` → chia 3 bằng `21`; hoặc gõ hệ vào Desmos đọc giao điểm `(6.538, 1.385)` rồi tính `3(6.538) + 1.385 = 21`.'
        ),
        # Q9 — Advanced Math (Medium-Hard, SPR -> 29) | SVG Parabola Vertex
        math_spr(
            'sat_mm8_m1_q9', 9, 'Advanced Math', 'Nonlinear functions', 'Medium-Hard',
            f'<div style="text-align:center;margin-bottom:10px;">{svg_q9}</div>' + r'<p>The parabola \(y = f(x)\) shown above has its vertex at \((5, -3)\) and passes through the point \((8, 15)\).</p>',
            r'What is the value of \(f(1)\)?',
            ['29'], '29',
            r'Viết phương trình parabol theo dạng đỉnh: \(f(x) = a(x - 5)^2 - 3\). Thay điểm \((8, 15)\): \(a(8 - 5)^2 - 3 = 15 \Rightarrow 9a = 18 \Rightarrow a = 2\). Vậy \(f(x) = 2(x - 5)^2 - 3\). Thay \(x = 1\): \(f(1) = 2(1 - 5)^2 - 3 = 2(16) - 3 = 29\).',
            r'Biết đỉnh \((h, k)\) và một điểm trên parabol, luôn dùng dạng đỉnh \(f(x) = a(x - h)^2 + k\) để giải nhanh hệ số \(a\).',
            r'Gõ `a(8 - 5)^2 - 3 = 15` trên Desmos tìm `a = 2`, rồi tính `2(1 - 5)^2 - 3` ra ngay `29`.'
        ),
        # Q10 — Advanced Math (Medium, MCQ -> B)
        math_mcq(
            'sat_mm8_m1_q10', 10, 'Advanced Math', 'Nonlinear equations in one variable and systems of equations in two variables', 'Medium',
            r'<p>Consider the quadratic equation below, where \(c\) is a constant:</p><p style="text-align:center;">\[4x^2 + 24x + c = 0\]</p>',
            r'If the equation has <b>exactly one real solution</b>, what is the value of \(c\)?',
            {'A': r'\(9\)', 'B': r'\(36\)', 'C': r'\(144\)', 'D': r'\(72\)'},
            'B',
            r'Phương trình bậc hai có đúng \(1\) nghiệm thực khi và chỉ khi biệt thức \(\Delta = b^2 - 4ac = 0\): \(24^2 - 4(4)c = 0 \Rightarrow 576 - 16c = 0 \Rightarrow c = 36\).',
            r'Có thể rút \(4\) ra ngoài: \(4(x^2 + 6x + \frac{c}{4}) = 0\); để thành bình phương đúng \((x + 3)^2\) thì \(\frac{c}{4} = 9 \Rightarrow c = 36\).',
            {
                'A': ('Forgot Leading Coefficient a = 4', r'Tính \((6/2)^2 = 9\) mà quên nhân lại với hệ số dẫn đầu \(a = 4\).'),
                'B': ('Correct', r'\(\Delta = 576 - 16c = 0 \Rightarrow c = 36\).'),
                'C': ('Divided by 4 Instead of 16', r'Quên nhân \(a = 4\) trong công thức \(4ac\), giải \(576 / 4 = 144\).'),
                'D': ('Divided by 8 Instead of 16', r'Nhầm \(4ac\) thành \(2ac = 8c \Rightarrow c = 72\).'),
            },
            r'Vẽ `y = 4x^2 + 24x + c` trên Desmos kèm thanh trượt `c` → kéo đến `c = 36` thấy đỉnh parabol chạm đúng trục Ox tại `(-3, 0)`!'
        ),
        # Q11 — Advanced Math (Medium, MCQ -> D)
        math_mcq(
            'sat_mm8_m1_q11', 11, 'Advanced Math', 'Equivalent expressions', 'Medium',
            r'<p>Consider the rational expression below for all \(x > 4\):</p><p style="text-align:center;">\[\frac{x^2 - 16}{x^2 - x - 12}\]</p>',
            r'Which of the following is equivalent to the given expression?',
            {
                'A': r'\(\frac{x - 4}{x + 3}\)',
                'B': r'\(\frac{x + 4}{x - 3}\)',
                'C': r'\(\frac{4}{3}\)',
                'D': r'\(\frac{x + 4}{x + 3}\)',
            },
            'D',
            r'Phân tích nhân tử tử số và mẫu số: \(\frac{x^2 - 16}{x^2 - x - 12} = \frac{(x - 4)(x + 4)}{(x - 4)(x + 3)}\). Vì \(x > 4\) nên \(x - 4 \neq 0\), rút gọn nhân tử chung \((x - 4)\) còn \(\frac{x + 4}{x + 3}\).',
            r'Luôn phân tích nhân tử trước khi rút gọn; kiểm tra nhanh bằng cách thay \(x = 5\) vào biểu thức gốc và đáp án!',
            {
                'A': ('Canceled Wrong Factor', r'Giữ lại \((x - 4)\) thay vì triệt tiêu nhân tử chung \((x - 4)\).'),
                'B': ('Wrong Sign Factoring Denominator', r'Phân tích nhầm \(x^2 - x - 12\) thành \((x - 4)(x - 3)\).'),
                'C': ('Illegal Term Cancellation', r'Gạch nhầm số hạng \(x^2\) và \(-x\) rồi rút gọn \(-16/-12 = 4/3\).'),
                'D': ('Correct', r'Rút gọn chuẩn nhân tử chung \((x - 4)\) ra \(\frac{x + 4}{x + 3}\).'),
            },
            r'Thay nhanh `x = 5` trên Desmos: `(25 - 16)/(25 - 5 - 12) = 9/8`. Chỉ phương án D cho `(5 + 4)/(5 + 3) = 9/8`!'
        ),
        # Q12 — Advanced Math (Easy, MCQ -> A) | Theme: Violin Luthier Wood Curing
        math_mcq(
            'sat_mm8_m1_q12', 12, 'Advanced Math', 'Nonlinear functions', 'Easy',
            r'<p>A master violin luthier cures alpine spruce tonewood in a humidity-controlled kiln. The moisture content \(M(t)\), as a percentage of wood weight, \(t\) weeks after entering the kiln is modeled by:</p><p style="text-align:center;">\[M(t) = 24(0.92)^t\]</p>',
            r'According to the model, by what percent does the moisture content decrease each week?',
            {'A': r'\(8\%\)', 'B': r'\(92\%\)', 'C': r'\(24\%\)', 'D': r'\(0.92\%\)'},
            'A',
            r'Trong hàm mũ giảm \(M(t) = a(1 - r)^t\), cơ số \(0.92 = 1 - 0.08\) nghĩa là sau mỗi tuần độ ẩm còn giữ lại \(92\%\) và <b>giảm đi \(8\%\)</b>.',
            r'Với cơ số suy giảm \(b < 1\), tỉ lệ phần trăm giảm luôn là \((1 - b) \times 100\%\), KHÔNG phải \(b \times 100\%\).',
            {
                'A': ('Correct', r'\(1 - 0.92 = 0.08 = 8\%\) giảm mỗi tuần.'),
                'B': ('Base Equals Decay Rate Trap', r'\(92\%\) là tỉ lệ độ ẩm CÒN LẠI, không phải phần trăm giảm đi.'),
                'C': ('Initial Value Trap', r'\(24\%\) là độ ẩm ban đầu tại \(t = 0\), không phải tốc độ giảm.'),
                'D': ('Decimal Conversion Error', r'Đọc trực tiếp cơ số \(0.92\) thành \(0.92\%\).'),
            },
            r'Kiểm tra nhanh tại `t = 0` (`24`) và `t = 1` (`22.08`): mức giảm `(24 - 22.08) / 24 = 0.08 = 8%`.'
        ),
        # Q13 — Advanced Math (Medium-Hard, SPR -> 8)
        math_spr(
            'sat_mm8_m1_q13', 13, 'Advanced Math', 'Nonlinear equations in one variable and systems of equations in two variables', 'Medium-Hard',
            r'<p>Consider the quadratic equation below:</p><p style="text-align:center;">\[4x^2 - 32x + 19 = 0\]</p>',
            r'What is the <b>sum</b> of the solutions to this equation?',
            ['8'], '8',
            r'Kiểm tra biệt thức: \(\Delta = (-32)^2 - 4(4)(19) = 1{,}024 - 304 = 720 > 0\), nên phương trình có \(2\) nghiệm thực phân biệt. Theo định lý Viète, tổng hai nghiệm bằng \(-\frac{b}{a} = -\frac{-32}{4} = 8\).',
            r'Tổng nghiệm phương trình bậc hai luôn là \(-\frac{b}{a}\) — đừng quên chia cho hệ số dẫn đầu \(a = 4\)!',
            r'Vẽ `y = 4x^2 - 32x + 19` trên Desmos, bấm 2 giao điểm trục Ox (`0.646` và `7.354`) → cộng lại đúng bằng `8`!'
        ),
        # Q14 — Advanced Math (Medium-Hard, MCQ -> C)
        math_mcq(
            'sat_mm8_m1_q14', 14, 'Advanced Math', 'Nonlinear equations in one variable and systems of equations in two variables', 'Medium-Hard',
            r'<p>Consider the radical equation shown below:</p><p style="text-align:center;">\[\sqrt{5x + 11} = x + 1\]</p>',
            r'What is the set of all real solutions to this equation?',
            {'A': r'\(\{-2, 5\}\)', 'B': r'\(\{-2\}\)', 'C': r'\(\{5\}\)', 'D': r'There are no real solutions.'},
            'C',
            r'Điều kiện vế phải không âm: \(x + 1 \ge 0 \Leftrightarrow x \ge -1\). Bình phương hai vế: \(5x + 11 = (x + 1)^2 = x^2 + 2x + 1 \Rightarrow x^2 - 3x - 10 = 0 \Rightarrow (x - 5)(x + 2) = 0 \Rightarrow x = 5\) hoặc \(x = -2\). Thử lại: \(x = 5 \Rightarrow \sqrt{36} = 6\) (đúng); \(x = -2 \Rightarrow \sqrt{1} = 1 \neq -1\) (nghiệm ngoại lai, LOẠI!).',
            r'Phương trình chứa căn bậc hai BẮT BUỘC thử lại nghiệm vào phương trình gốc để loại nghiệm ngoại lai làm vế phải âm.',
            {
                'A': ('Kept Extraneous Root', r'Giữ lại \(x = -2\) dù khi thay vào ta có \(\sqrt{1} = 1 \neq -1\).'),
                'B': ('Picked Only Extraneous Root', r'\(x = -2\) làm sai phương trình gốc.'),
                'C': ('Correct', r'Chỉ có duy nhất \(x = 5\) thỏa mãn phương trình gốc.'),
                'D': ('Missed Valid Solution', r'\(x = 5\) là nghiệm thực hoàn toàn hợp lệ.'),
            },
            r'Vẽ `y = sqrt(5x + 11)` và `y = x + 1` trên Desmos → chỉ có ĐÚNG 1 giao điểm tại `(5, 6)` → nghiệm duy nhất là `5`!'
        ),
        # Q15 — Advanced Math (Medium-Hard, MCQ -> B)
        math_mcq(
            'sat_mm8_m1_q15', 15, 'Advanced Math', 'Nonlinear equations in one variable and systems of equations in two variables', 'Medium-Hard',
            r'<p>Consider the system of equations in the \(xy\)-plane:</p><p style="text-align:center;">\[\begin{cases} y = x^2 - 5x + 10 \\ y = 2x - 2 \end{cases}\]</p>',
            r'If \((x, y)\) is a solution to the system with \(x > 3.5\), what is the value of \(x + y\)?',
            {'A': r'\(7\)', 'B': r'\(10\)', 'C': r'\(6\)', 'D': r'\(4\)'},
            'B',
            r'Lập phương trình hoành độ giao điểm: \(x^2 - 5x + 10 = 2x - 2 \Rightarrow x^2 - 7x + 12 = 0 \Rightarrow (x - 3)(x - 4) = 0 \Rightarrow x = 3\) hoặc \(x = 4\). Vì đề yêu cầu \(x > 3.5\), ta chọn \(x = 4\), khi đó \(y = 2(4) - 2 = 6\). Vậy \(x + y = 4 + 6 = 10\).',
            r'Với hệ parabol + đường thẳng có 2 giao điểm, đọc kỹ điều kiện lọc nghiệm (\(x > 3.5\)) và biểu thức cuối cùng (\(x + y\)).',
            {
                'A': ('Used Wrong Intersection Point', r'Chọn nhầm giao điểm \((3, 4)\) có \(x = 3 < 3.5\), ra \(3 + 4 = 7\).'),
                'B': ('Correct', r'Giao điểm thỏa \(x > 3.5\) là \((4, 6) \Rightarrow x + y = 10\).'),
                'C': ('Stopped at y', r'\(6\) chỉ là tung độ \(y\), quên cộng với \(x = 4\).'),
                'D': ('Stopped at x', r'\(4\) chỉ là hoành độ \(x\), quên cộng với \(y = 6\).'),
            },
            r'Vẽ `y = x^2 - 5x + 10` và `y = 2x - 2` trên Desmos → bấm 2 giao điểm `(3, 4)` và `(4, 6)` → chọn điểm có `x > 3.5` và tính `4 + 6 = 10`.'
        ),
        # Q16 — PSDA (Medium, SPR -> 15) | Theme: Stepped-Pyramid Monument
        math_spr(
            'sat_mm8_m1_q16', 16, 'Problem-Solving and Data Analysis', 'Ratios, rates, proportional relationships, and units', 'Medium',
            r'<p>A restoration crew resurfaces a stepped-pyramid monument walkway using limestone slabs covering an area of \(2{,}160\) square inches. <em>(\(1\text{ foot} = 12\text{ inches}\))</em></p>',
            r'What is the area of the resurfaced walkway, in <b>square feet</b>?',
            ['15'], '15',
            r'Vì \(1\text{ ft} = 12\text{ in}\), nên \(1\text{ ft}^2 = 12^2 = 144\text{ in}^2\). Đổi sang feet vuông: \(\frac{2{,}160}{144} = 15\text{ ft}^2\).',
            r'Khi quy đổi đơn vị DIỆN TÍCH (square units), BẮT BUỘC bình phương tỉ lệ chiều dài (\(12^2 = 144\)), không chia cho \(12\)!',
            r'Gõ `2160 / 12^2` vào Desmos ra ngay kết quả chính xác `15`.'
        ),
        # Q17 — PSDA (Medium, MCQ -> B) | Theme: National Park Wildlife Census (Table)
        math_mcq(
            'sat_mm8_m1_q17', 17, 'Problem-Solving and Data Analysis', 'Probability and conditional probability', 'Medium',
            tbl_q17 + r'<p>The table above summarizes the results of a national park elk census across three habitat zones.</p>',
            r'If an elk recorded in the <b>Alpine Ridge</b> is selected at random, what is the probability that it is <b>GPS-Tagged</b>?',
            {'A': r'\(\frac{27}{200}\)', 'B': r'\(\frac{3}{5}\)', 'C': r'\(\frac{27}{80}\)', 'D': r'\(\frac{2}{5}\)'},
            'B',
            r'Cụm điều kiện "If an elk recorded in the Alpine Ridge is selected at random" thu hẹp không gian mẫu chỉ còn tổng hàng Alpine Ridge \(= 45\). Số cá thể được gắn thẻ GPS ở Alpine Ridge là \(27\). Xác suất cần tìm: \(\frac{27}{45} = \frac{3}{5}\).',
            r'Trong xác suất có điều kiện từ bảng 2 chiều, mẫu số CHỈ là tổng của nhóm điều kiện ("Alpine Ridge" = 45), không phải tổng toàn bảng (200)!',
            {
                'A': ('Grand Total Denominator Trap', r'Chia cho tổng cả công viên \(200\) thay vì tổng riêng Alpine Ridge (\(45\)).'),
                'B': ('Correct', r'\(\frac{27}{45} = \frac{3}{5}\).'),
                'C': ('Column Total Denominator Trap', r'Chia cho tổng cột GPS-Tagged (\(80\)) thay vì tổng hàng Alpine Ridge (\(45\)).'),
                'D': ('Complement Event Trap', r'\(\frac{18}{45} = \frac{2}{5}\) là xác suất chọn cá thể KHÔNG gắn thẻ (Untagged).'),
            },
            r'Gõ `27/45` vào Desmos rồi bấm nút phân số ở bên trái ô nhập để rút gọn ngay thành `3/5`.'
        ),
        # Q18 — PSDA (Medium-Hard, MCQ -> D) | Theme: Geothermal Power Wells (Table)
        math_mcq(
            'sat_mm8_m1_q18', 18, 'Problem-Solving and Data Analysis', 'One-variable data: Distributions and measures of center and spread', 'Medium-Hard',
            tbl_q18 + r'<p>The frequency table above summarizes the daily wellhead steam pressure, in bars, recorded at \(15\) geothermal power wells.</p>',
            r'By how many bars does the <b>mean</b> steam pressure exceed the <b>median</b> steam pressure for these \(15\) wells?',
            {'A': r'\(0\)', 'B': r'\(1\)', 'C': r'\(5.8\)', 'D': r'\(2\)'},
            'D',
            r'Bước 1 (Tính trung bình có trọng số): Tổng áp suất \(= 15(2) + 18(4) + 20(5) + 26(3) + 50(1) = 30 + 72 + 100 + 78 + 50 = 330\). Trung bình cộng \(\bar{x} = \frac{330}{15} = 22\) bars.<br>Bước 2 (Tìm trung vị): Với \(15\) giếng, trung vị nằm ở vị trí thứ \(\frac{15 + 1}{2} = 8\). Cộng dồn tần số: mức \(15\) (vị trí 1–2), mức \(18\) (vị trí 3–6), mức \(20\) (vị trí 7–11) → giá trị thứ \(8\) là \(20\) bars.<br>Bước 3: Hiệu \(\text{Mean} - \text{Median} = 22 - 20 = 2\) bars.',
            r'Tuyệt đối không lấy trung bình cộng của 5 con số ở cột trái mà bỏ qua tần số (Number of Wells) ở cột phải!',
            {
                'A': ('Assumed Symmetric Distribution', r'Giá trị ngoại lai \(50\) kéo trung bình lên lớn hơn trung vị, không thể bằng nhau.'),
                'B': ('Miscomputed Mean or Median', r'Nhầm trung vị thành \(21\) hoặc sai phép tính tổng.'),
                'C': ('Unweighted Average Trap', r'Lấy trung bình của 5 giá trị \(\frac{15+18+20+26+50}{5} = 25.8\) mà quên nhân tần số, ra \(25.8 - 20 = 5.8\).'),
                'D': ('Correct', r'Trung bình \(22\) trừ trung vị \(20\) bằng chính xác \(2\) bars.'),
            },
            r'Gõ `(15*2 + 18*4 + 20*5 + 26*3 + 50*1)/15` trên Desmos ra `22`; vị trí thứ 8 là `20` → `22 - 20 = 2`.'
        ),
        # Q19 — PSDA (Medium-Hard, SPR -> 45) | Theme: Violin Luthier Acoustics
        math_spr(
            'sat_mm8_m1_q19', 19, 'Problem-Solving and Data Analysis', 'Percentages', 'Medium-Hard',
            r'<p>In a violin acoustics grading model, three positive indices \(p\), \(q\), and \(r\) satisfy the following relationships: \(p\) is \(150\%\) of \(q\), and \(q\) is \(30\%\) of \(r\).</p>',
            r'If \(p\) is \(k\%\) of \(r\), what is the value of \(k\)?',
            ['45'], '45',
            r'Đặt \(r = 100\). Khi đó \(q = 30\% \text{ của } 100 = 30\). Tiếp tục \(p = 150\% \text{ của } 30 = 1.50 \times 30 = 45\). Vì \(r = 100\), \(p = 45\) chính là \(45\%\) của \(r\), suy ra \(k = 45\).',
            r'Với chuỗi phần trăm dạng "\(p\) là \(a\%\) của \(q\), \(q\) là \(b\%\) của \(r\)", chỉ cần nhân hệ số thập phân \(1.50 \times 0.30 = 0.45 = 45\%\)!',
            r'Gõ `1.50 * 0.30 * 100` trên Desmos ra ngay `45`.'
        ),
        # Q20 — Geometry (Medium, MCQ -> A) | SVG Parallel Transversal
        math_mcq(
            'sat_mm8_m1_q20', 20, 'Geometry and Trigonometry', 'Lines, angles, and triangles', 'Medium',
            f'<div style="text-align:center;margin-bottom:10px;">{svg_q20}</div>' + r'<p>In the figure above, parallel lines \(\ell\) and \(m\) are intersected by a transversal.</p>',
            r'What is the measure, in degrees, of the <b>acute</b> angle formed by the intersection of the transversal and line \(m\)?',
            {'A': r'\(46\)', 'B': r'\(24\)', 'C': r'\(134\)', 'D': r'\(56\)'},
            'A',
            r'Hai góc \((5x + 14)^\circ\) và \((3x + 62)^\circ\) là cặp góc so le ngoài (alternate exterior angles) trên hai đường song song nên bằng nhau: \(5x + 14 = 3x + 62 \Rightarrow 2x = 48 \Rightarrow x = 24\). Số đo góc tù là \(5(24) + 14 = 134^\circ\). Góc nhọn kề bù với góc tù đó trên đường thẳng \(m\) có số đo \(180^\circ - 134^\circ = 46^\circ\).',
            r'Cát tuyến cắt hai đường thẳng song song chỉ tạo ra 2 cỡ góc bù nhau: tìm xong góc tù \(134^\circ\), nhớ lấy \(180^\circ - 134^\circ\) để ra góc nhọn!',
            {
                'A': ('Correct', r'\(x = 24 \Rightarrow\) góc tù \(134^\circ \Rightarrow\) góc nhọn \(180 - 134 = 46^\circ\).'),
                'B': ('Stopped at x', r'\(24\) chỉ là giá trị biến \(x\), chưa tính số đo góc.'),
                'C': ('Obtuse Instead of Acute', r'\(134^\circ\) là số đo góc tù, trong khi đề hỏi góc nhọn (acute angle).'),
                'D': ('Subtraction Error', r'Trừ nhầm \(180 - 134\) thành \(56\).'),
            },
            r'Gõ `5x + 14 = 3x + 62` trên Desmos tìm `x = 24`, rồi tính `180 - (5*24 + 14) = 46`.'
        ),
        # Q21 — Geometry (Medium-Hard, MCQ -> C) | SVG Circle Sector | Theme: Monument Courtyard
        math_mcq(
            'sat_mm8_m1_q21', 21, 'Geometry and Trigonometry', 'Circles', 'Medium-Hard',
            f'<div style="text-align:center;margin-bottom:10px;">{svg_q21}</div>' + r'<p>The figure above represents a circular stone monument courtyard centered at \(O\) with radius \(OA = 12\) meters. The shaded sector \(AOB\) has a central angle of \(75^\circ\).</p>',
            r'What is the area of the shaded sector \(AOB\), in square meters?',
            {'A': r'\(5\pi\)', 'B': r'\(15\pi\)', 'C': r'\(30\pi\)', 'D': r'\(60\pi\)'},
            'C',
            r'Diện tích hình quạt tròn bằng tỉ phần góc tâm nhân diện tích cả hình tròn: \(A_{\text{quạt}} = \frac{75^\circ}{360^\circ} \cdot \pi r^2 = \frac{5}{24} \cdot \pi (12^2) = \frac{5}{24} \cdot 144\pi = 5 \cdot 6\pi = 30\pi\text{ m}^2\).',
            r'Phân biệt rõ công thức diện tích quạt \(\frac{\theta}{360^\circ} \pi r^2\) với độ dài cung \(\frac{\theta}{360^\circ} (2\pi r)\) để tránh khoanh nhầm \(5\pi\)!',
            {
                'A': ('Arc Length Trap', r'\(\frac{75}{360}(2\pi \cdot 12) = 5\pi\) là độ dài cung \(AB\), không phải diện tích quạt.'),
                'B': ('Halved the Area', r'Chia đôi nhầm \(30\pi\) thành \(15\pi\).'),
                'C': ('Correct', r'\(\frac{75}{360} \cdot 144\pi = 30\pi\text{ m}^2\).'),
                'D': ('Doubled the Area', r'Nhân thêm hệ số 2 từ công thức chu vi \(2\pi r^2\).'),
            },
            r'Gõ `(75 / 360) * 12^2` trên Desmos ra ngay `30` → chọn `30π`!'
        ),
        # Q22 — Geometry (Medium-Hard, SPR -> 45) | SVG Right Triangle
        math_spr(
            'sat_mm8_m1_q22', 22, 'Geometry and Trigonometry', 'Right triangles and trigonometry', 'Medium-Hard',
            f'<div style="text-align:center;margin-bottom:10px;">{svg_q22}</div>' + r'<p>In right triangle \(PQR\) shown above, \(\angle Q = 90^\circ\), the hypotenuse \(PR = 51\), and \(\cos(P) = \frac{8}{17}\).</p>',
            r'What is the length of side \(QR\)?',
            ['45'], '45',
            r'Trong tam giác vuông \(PQR\), \(\cos(P) = \frac{\text{kề}}{\text{huyền}} = \frac{PQ}{PR} = \frac{8}{17}\). Vì \(PR = 51 = 17 \times 3\), suy ra cạnh kề \(PQ = 8 \times 3 = 24\). Áp dụng định lý Pythagoras (hoặc bộ ba \(8\text{–}15\text{–}17\) nhân \(3\)): \(QR = \sqrt{51^2 - 24^2} = \sqrt{2{,}025} = 45\).',
            r'Nhớ kỹ \(\cos(P) = \frac{PQ}{PR}\) cho cạnh KỀ \(PQ = 24\); đọc kỹ đề hỏi cạnh ĐỐI \(QR = 45\) (bộ ba \(8\text{–}15\text{–}17\) phóng đại \(3\) lần)!',
            r'Tính `PQ = 51 * (8/17) = 24`, sau đó gõ `sqrt(51^2 - 24^2)` trên Desmos ra ngay `45`!'
        ),
    ]


if __name__ == '__main__':
    assert verify_math()
    qs = get_m1_questions()
    print(f"M1 verified: {len(qs)} questions")
