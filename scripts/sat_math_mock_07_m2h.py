# -*- coding: utf-8 -*-
"""
Digital SAT Math Adaptive Mock Test #7 — Module 2 Hard (650–800 Band, 22 Questions)
Themes: Electric Ferry Maritime Routes, Urban Vertical Hydroponic Towers,
        Pharmaceutical Dosage Pharmacokinetics, Olympic Velodrome Track Geometry,
        Bronze Sculpture Foundry & Alloy Density.
Blueprint: 8 Algebra (Q1-Q8), 7 Advanced Math (Q9-Q15), 4 PSDA (Q16-Q19), 3 Geometry/Trig (Q20-Q22).
Format: 16 MCQ (A:4, B:4, C:4, D:4) + 6 SPR (Q5, Q9, Q13, Q16, Q19, Q22).
"""

from fractions import Fraction
import math
from sat_math_helpers import (
    math_mcq, math_spr, build_math_table,
    svg_circle_sector, svg_similar_triangles, svg_cylinder,
)


def verify_math():
    # Q1: (a/4)x - 6y = 15, 7x - by = 60 inf many solutions => scale = 4 => b = 24, a = 7 => b - 2a = 10
    scale1 = Fraction(60, 15)
    b1 = 6 * scale1
    a1 = Fraction(7, scale1) * 4
    assert scale1 == 4 and b1 == 24 and a1 == 7 and b1 - 2 * a1 == 10
    # Q2: f(x) - 9 passes through (4, 8), (9, 33), (12, 48) => f(x) = 5x - 3 => x-int = 3/5
    for xv, yv in [(4, 17), (9, 42), (12, 57)]:
        assert 5 * xv - 3 == yv and yv - 9 in (8, 33, 48)
    assert 5 * Fraction(3, 5) - 3 == 0
    # Q3: 8x - 12y = 7 perp to kx + 6y = 19 => 8k + (-12)(6) = 0 => k = 9
    assert 8 * 9 + (-12) * 6 == 0 and Fraction(8, 12) * Fraction(-9, 6) == -1
    # Q4: |3x - 12| + |2x - 8| = 35 => 5|x - 4| = 35 => x in {11, -3} => product = -33
    assert abs(3 * 11 - 12) + abs(2 * 11 - 8) == 35
    assert abs(3 * (-3) - 12) + abs(2 * (-3) - 8) == 35
    assert 11 * (-3) == -33
    # Q5: y >= 5x - 17 and y >= -3x + 23 => intersection (5, 8) => b_min = 8
    assert 5 * 5 - 17 == -3 * 5 + 23 == 8
    # Q6: y < -2x - 6 and y < 4x - 12 => intersection (1, -8), y < -8 < 0 => Q-I & Q-II empty
    assert -2 * 1 - 6 == 4 * 1 - 12 == -8 < 0
    assert (-20 < -2 * (-1) - 6 and -20 < 4 * (-1) - 12)  # Q-III valid
    assert (-20 < -2 * 1 - 6 and -20 < 4 * 1 - 12)  # Q-IV valid
    # Q7: P(t+6) - P(t) = 27 => m = 9/2, P(10) = 195 => P(0) = 195 - 45 = 150
    m7 = Fraction(27, 6)
    p0 = 195 - m7 * 10
    assert m7 == Fraction(9, 2) and p0 == 150 and m7 * 10 + p0 == 195
    # Q8: (3/5)(kx - 10) + 4x = 7x - 11 no solution => 3k/5 + 4 = 7 => k = 5, -6 != -11
    k8 = Fraction((7 - 4) * 5, 3)
    assert k8 == 5 and Fraction(3, 5) * (-10) == -6 != -11
    # Q9: y = 6x + k tangent to y = 2x^2 - 10x + 27 => 2x^2 - 16x + (27 - k) = 0 => D = 0 => k = -5
    assert (-16) ** 2 - 4 * 2 * (27 - (-5)) == 0
    assert 2 * (4 ** 2) - 10 * 4 + 27 == 6 * 4 + (-5) == 19
    # Q10: f(x) = 108 * 3^(x - 3) + 17 => f(0) = 108/27 + 17 = 21 => f(0) - 5 = 16
    assert Fraction(108, 27) + 17 - 5 == 16
    # Q11: p(x) = 3x^3 - 7x^2 + kx + 18 div by (x - 2) => k = -7 => p(-1) = 15
    k11 = Fraction(-(3 * 8 - 7 * 4 + 18), 2)
    assert k11 == -7
    assert 3 * (-1) ** 3 - 7 * (-1) ** 2 + k11 * (-1) + 18 == 15
    # Q12: 3x^2 - (2k + 5)x + 4k = 0, product = 16 => 4k/3 = 16 => k = 12, D = 265 > 0, sum = 29/3
    k12 = Fraction(16 * 3, 4)
    assert k12 == 12
    b12 = -(2 * k12 + 5)
    assert b12 ** 2 - 4 * 3 * (4 * k12) > 0 and Fraction(-b12, 3) == Fraction(29, 3)
    # Q13: x - 10/(x - 4) = (8x - 42)/(x - 4) => (x - 4)(x - 8) = 0 => x = 8 valid, x = 4 extraneous
    assert Fraction(8) - Fraction(10, 8 - 4) == Fraction(8 * 8 - 42, 8 - 4)
    assert (4 - 4) == 0 and (8 - 4) * (8 - 8) == 0
    # Q14: Vertex (h, -18), roots h-3 & h+3 => a = 2; f(1) = a+b+c = 14, h > 0 => h = 5
    a14 = Fraction(18, 3 ** 2)
    assert a14 == 2
    h14 = 5
    assert a14 * (1 - h14) ** 2 - 18 == 14
    # Expanded check: 2(x - 5)^2 - 18 = 2x^2 - 20x + 32
    assert 2 + (-20) + 32 == 14 and 2 * (2 - 5) ** 2 - 18 == 0 and 2 * (8 - 5) ** 2 - 18 == 0
    # Q15: C(t) = 1250*(0.64)^(t/6); 9-hr factor = (0.64)^(3/2) = 0.8^3 = 0.512 => 48.8% decrease
    assert Fraction(8, 10) ** 2 == Fraction(64, 100)
    decay15 = 1 - Fraction(8, 10) ** 3
    assert decay15 == Fraction(488, 1000)
    # Q16: density 8.8 g/cm^3, V = 0.045 m^3 = 45000 cm^3 => mass = 396000 g = 396 kg
    mass_kg = Fraction(88, 10) * Fraction(45, 1000) * (100 ** 3) / 1000
    assert mass_kg == 396
    # Q17: 1.25 * (1 - p/100) = 0.90 => p = 28
    assert Fraction(125, 100) * (1 - Fraction(28, 100)) == Fraction(90, 100)
    # Q18: Route A & B frequency comparison
    vals18 = [12, 14, 16, 18, 20]
    freqA = [3, 5, 9, 5, 3]
    freqB = [1, 4, 9, 5, 6]
    dataA = [v for v, f in zip(vals18, freqA) for _ in range(f)]
    dataB = [v for v, f in zip(vals18, freqB) for _ in range(f)]
    assert len(dataA) == 25 and len(dataB) == 25
    assert dataA[12] == dataB[12] == 16
    assert Fraction(sum(dataA), 25) == 16 and Fraction(sum(dataB), 25) == Fraction(422, 25) > 16
    # Q19: Ingot weights (12*5 + 15*k + 20*7 + 26*5) / (17 + k) = 18 => k = 8
    k19 = 8
    assert Fraction(12 * 5 + 15 * k19 + 20 * 7 + 26 * 5, 5 + k19 + 7 + 5) == 18
    # Q20: Sector area = (1/2) r^2 (5pi/12) = 120pi => r = 24 => arc s = 24*(5pi/12) = 10pi
    r_sq20 = Fraction(120 * 24, 5)
    assert r_sq20 == 576 and int(math.isqrt(int(r_sq20))) == 24
    assert 24 * Fraction(5, 12) == 10
    # Q21: Right triangle ABC ~ DEF, AB=20, BC=21 => AC=29 => sin(D)+cos(F) = 21/29 + 21/29 = 42/29
    assert 20 ** 2 + 21 ** 2 == 29 ** 2
    assert Fraction(21, 29) + Fraction(21, 29) == Fraction(42, 29)
    # Q22: Similar cylinders SA 48pi & 300pi => k^2 = 25/4 => k = 5/2 => k^3 = 125/8 => V_Y = 128*(125/8) = 2000
    k_sq22 = Fraction(300, 48)
    k22 = Fraction(5, 2)
    assert k22 ** 2 == k_sq22 and 128 * (k22 ** 3) == 2000


def get_m2h_questions():
    tbl_q2 = build_math_table(
        [r'\(x\)', r'\(f(x) - 9\)'],
        [['4', '8'], ['9', '33'], ['12', '48']],
        caption='Hydroponic Nutrient Sensor Calibration Table',
    )
    tbl_q18 = build_math_table(
        ['Daily Crossings', 'Route A (Days)', 'Route B (Days)'],
        [
            ['12', '3', '1'],
            ['14', '5', '4'],
            ['16', '9', '9'],
            ['18', '5', '5'],
            ['20', '3', '6'],
        ],
        caption='Electric Ferry Daily Crossings (25-Day Log)',
    )
    tbl_q19 = build_math_table(
        ['Ingot Mass (kg)', 'Number of Ingots'],
        [['12', '5'], ['15', r'\(k\)'], ['20', '7'], ['26', '5']],
        caption='Bronze Foundry Cast Ingot Batch',
    )
    svg_q20 = svg_circle_sector(
        radius_lbl='r', angle_lbl='5π/12 rad', center_lbl='O', pt_a='A', pt_b='B',
        note='Note: Figure not drawn to scale.',
    )
    svg_q21 = svg_similar_triangles('20', '21', '60', 'EF', 'A', 'B', 'C', 'D', 'E', 'F')
    svg_q22 = svg_cylinder('r', 'h', note='Similar Bronze Pedestal Columns X and Y')

    return [
        math_mcq(
            'sat_mm7_m2h_q1', 1, 'Algebra', 'Systems of two linear equations in two variables', 'Hard',
            r'<p>In the system of equations below, \(a\) and \(b\) are constants:</p><p style="text-align:center;">\[\begin{cases} \frac{a}{4}x - 6y = 15 \\ 7x - by = 60 \end{cases}\]</p>',
            r'If the system has <b>infinitely many solutions</b>, what is the value of \(b - 2a\)?',
            {'A': r'\(7\)', 'B': r'\(10\)', 'C': r'\(17\)', 'D': r'\(31\)'},
            'B',
            r'Để hệ có vô số nghiệm, phương trình thứ hai phải là bội số chính xác của phương trình thứ nhất. So sánh hằng số tự do: \(\frac{60}{15} = 4\). Suy ra: \(-b = 4(-6) \Rightarrow b = 24\), và \(7 = 4 \cdot \left(\frac{a}{4}\right) \Rightarrow a = 7\). Cuối cùng tính đúng biểu thức đề hỏi: \(b - 2a = 24 - 2(7) = 10\).',
            r'Hệ vô số nghiệm: tìm tỉ số từ cặp hằng số đã biết (\(60/15 = 4\)) rồi nhân tỉ số đó cho từng hệ số của phương trình đầu!',
            {
                'A': ('Dừng ở giá trị a', r'\(7\) chỉ là giá trị của \(a\), chưa tính \(b - 2a\).'),
                'B': ('Đáp án đúng', r'\(a = 7, b = 24 \Rightarrow b - 2a = 24 - 14 = 10\).'),
                'C': ('Tính b - a thay vì b - 2a', r'\(24 - 7 = 17\), quên hệ số \(2\) trước \(a\).'),
                'D': ('Tính b + a', r'Cộng \(24 + 7 = 31\) thay vì trừ \(2a\).'),
            },
            r'Gõ `(a/4)x - 6y = 15` và `7x - by = 60` trên Desmos kèm sliders `a, b` → tại `a = 7, b = 24`, hai đường trùng khít → tính `24 - 2(7) = 10`.'
        ),
        math_mcq(
            'sat_mm7_m2h_q2', 2, 'Algebra', 'Linear functions', 'Hard',
            tbl_q2 + r'<p>The table above shows three ordered pairs for \(x\) and \(f(x) - 9\), where \(f\) is a linear function modeling an urban vertical hydroponic tower’s calibration curve.</p>',
            r'What is the \(x\)-intercept of the graph of \(y = f(x)\) in the \(xy\)-plane?',
            {
                'A': r'\(\left(\frac{12}{5}, 0\right)\)',
                'B': r'\((0, -3)\)',
                'C': r'\(\left(\frac{5}{3}, 0\right)\)',
                'D': r'\(\left(\frac{3}{5}, 0\right)\)',
            },
            'D',
            r'Cộng \(9\) vào cột phải để khôi phục bảng giá trị đúng của \(f(x)\): \((4, 17)\), \((9, 42)\), \((12, 57)\). Tính hệ số góc: \(m = \frac{42 - 17}{9 - 4} = \frac{25}{5} = 5\). Suy ra \(f(x) = 5(x - 4) + 17 = 5x - 3\). Tìm \(x\)-intercept (cho \(f(x) = 0\)): \(5x - 3 = 0 \Rightarrow x = \frac{3}{5}\). Vậy \(x\)-intercept là \(\left(\frac{3}{5}, 0\right)\).',
            r'Bảng cho \(f(x) - 9\) thì PHẢI cộng \(+9\) để khôi phục đúng \(f(x)\) trước khi giải \(f(x) = 0\)!',
            {
                'A': ('Quên cộng 9 vào cột phải', r'Lập hàm của \(f(x) - 9 = 5x - 12 = 0 \Rightarrow x = \frac{12}{5}\) (sai hàm!).'),
                'B': ('Nhầm y-intercept với x-intercept', r'\((0, -3)\) là giao điểm trục Oy, đề hỏi giao điểm trục Ox!'),
                'C': ('Nghịch đảo phân số', r'Giải nhầm \(5x - 3 = 0\) thành \(x = \frac{5}{3}\).'),
                'D': ('Đáp án đúng', r'\(f(x) = 5x - 3 = 0 \Rightarrow \left(\frac{3}{5}, 0\right)\).'),
            },
            r'Nhập Table `x1 = [4, 9, 12]`, `y1 = [17, 42, 57]` vào Desmos → hồi quy `y1 ~ m x1 + b` → bấm giao điểm trục Ox trên đồ thị `y = 5x - 3` đọc ngay `(0.6, 0)`!'
        ),
        math_mcq(
            'sat_mm7_m2h_q3', 3, 'Algebra', 'Linear equations in two variables', 'Medium-Hard',
            r'<p>In the \(xy\)-plane, the line \(8x - 12y = 7\) is perpendicular to the line \(kx + 6y = 19\), where \(k\) is a constant.</p>',
            r'What is the value of \(k\)?',
            {'A': r'\(9\)', 'B': r'\(-9\)', 'C': r'\(-4\)', 'D': r'\(4\)'},
            'A',
            r'Cách nhanh chuẩn Hard M2: hai đường thẳng dạng chuẩn \(A_1x + B_1y = C_1\) và \(A_2x + B_2y = C_2\) vuông góc nhau khi và chỉ khi \(A_1A_2 + B_1B_2 = 0\). Thay số: \(8k + (-12)(6) = 0 \Rightarrow 8k = 72 \Rightarrow k = 9\). (Kiểm tra lại slope: \(m_1 = \frac{8}{12} = \frac{2}{3}\), \(m_2 = -\frac{9}{6} = -\frac{3}{2}\), tích \(m_1m_2 = -1\)).',
            r'Công thức tích vô hướng \(A_1A_2 + B_1B_2 = 0\) xử gọn mọi câu đường vuông góc dạng Standard Form trong 3 giây!',
            {
                'A': ('Đáp án đúng', r'\(8(9) + (-12)(6) = 72 - 72 = 0\).'),
                'B': ('Sai dấu âm', r'Quên dấu trừ ở \(-12y\) nên giải ra \(k = -9\).'),
                'C': ('Điều kiện song song thay vì vuông góc', r'Giải \(\frac{k}{8} = \frac{6}{-12} \Rightarrow k = -4\) (đây là đường song song!).'),
                'D': ('Song song kèm sai dấu', r'Giải nhầm \(\frac{k}{8} = \frac{6}{12} \Rightarrow k = 4\).'),
            },
            r'Gõ `8x - 12y = 7` và `kx + 6y = 19` trên Desmos, thêm slider `k` → tại `k = 9`, hai đường cắt vuông góc hoàn hảo!'
        ),
        math_mcq(
            'sat_mm7_m2h_q4', 4, 'Algebra', 'Linear equations in one variable', 'Hard',
            r'<p>Consider the absolute value equation below:</p><p style="text-align:center;font-size:18px;">\[|3x - 12| + |2x - 8| = 35\]</p>',
            r'What is the <b>product</b> of all real solutions to the given equation?',
            {'A': r'\(8\)', 'B': r'\(-11\)', 'C': r'\(-33\)', 'D': r'\(33\)'},
            'C',
            r'Đặt nhân tử chung bên trong từng dấu giá trị tuyệt đối: \(|3(x - 4)| + |2(x - 4)| = 35 \Rightarrow 3|x - 4| + 2|x - 4| = 35 \Rightarrow 5|x - 4| = 35 \Rightarrow |x - 4| = 7\). Tách 2 trường hợp: \(x - 4 = 7 \Rightarrow x = 11\), hoặc \(x - 4 = -7 \Rightarrow x = -3\). Tích các nghiệm là \(11 \times (-3) = -33\).',
            r'Khi hai biểu thức trong dấu \(|\cdot|\) tỉ lệ với nhau (\(3x - 12\) và \(2x - 8\)), rút nhân tử chung \(|x - 4|\) để gộp thành MỘT giá trị tuyệt đối duy nhất!',
            {
                'A': ('Tính tổng thay vì tích', r'\(11 + (-3) = 8\) là tổng hai nghiệm, đề yêu cầu tìm TÍCH (product).'),
                'B': ('Nhầm nghiệm âm thành -1', r'Giải sai \(x - 4 = -7\) hoặc lấy \(-11\).'),
                'C': ('Đáp án đúng', r'Hai nghiệm là \(11\) và \(-3 \Rightarrow 11 \times (-3) = -33\).'),
                'D': ('Quên dấu âm của nghiệm -3', r'Tính \(11 \times 3 = 33\) do bỏ quên dấu âm.'),
            },
            r'Gõ `y = |3x - 12| + |2x - 8|` và `y = 35` lên Desmos → bấm 2 giao điểm `(-3, 35)` và `(11, 35)` → gõ `(-3) * 11` ra ngay `-33`!'
        ),
        math_spr(
            'sat_mm7_m2h_q5', 5, 'Algebra', 'Linear inequalities in one or two variables', 'Hard',
            r'<p>In the \(xy\)-plane, a point \((a, b)\) is a solution to the system of inequalities below:</p><p style="text-align:center;">\[\begin{cases} y \ge 5x - 17 \\ y \ge -3x + 23 \end{cases}\]</p>',
            r'What is the <b>minimum</b> possible value of \(b\)?',
            ['8'], '8',
            r'Vì cả hai bất phương trình đều chặn phía dưới của \(y\) với hai hệ số góc ngược dấu (\(+5\) và \(-3\)), giá trị nhỏ nhất của tung độ \(b\) đạt đúng tại đỉnh giao điểm hai đường biên: \(5x - 17 = -3x + 23 \Rightarrow 8x = 40 \Rightarrow x = 5\). Thay vào tìm tung độ: \(b_{\min} = 5(5) - 17 = 8\) (kiểm tra đường kia: \(-3(5) + 23 = 8\)).',
            r'Quy tắc Corner-Point: cực tiểu của \(y\) với hệ hai bất đẳng thức \(y \ge\) ngược chiều slope luôn nằm ngay tại giao điểm 2 đường biên!',
            r'Gõ `y >= 5x - 17` và `y >= -3x + 23` vào Desmos → bấm vào đỉnh nhọn thấp nhất của vùng tô chồng chéo đọc ngay `(5, 8)` → `b_min = 8`!'
        ),
        math_mcq(
            'sat_mm7_m2h_q6', 6, 'Algebra', 'Linear inequalities in one or two variables', 'Hard',
            r'<p>Consider the system of linear inequalities in the \(xy\)-plane:</p><p style="text-align:center;">\[\begin{cases} y < -2x - 6 \\ y < 4x - 12 \end{cases}\]</p>',
            r'Which quadrants of the \(xy\)-plane contain <b>no solutions</b> to this system?',
            {
                'A': r'Quadrant I only',
                'B': r'Quadrant II only',
                'C': r'Quadrants II and III',
                'D': r'Quadrants I and II',
            },
            'D',
            r'Tìm giao điểm 2 đường biên: \(-2x - 6 = 4x - 12 \Rightarrow 6x = 6 \Rightarrow x = 1 \Rightarrow y = -2(1) - 6 = -8\). Do cả hai bất phương trình đều lấy miền <b>phía dưới</b> (\(y <\)) hai đường có slope trái dấu (\(-2\) và \(+4\)), mọi điểm nghiệm \((x, y)\) bắt buộc phải thỏa mãn \(y < -8 < 0\)! Vì thế toàn bộ nửa mặt phẳng phía trên trục Ox (\(y > 0\), gồm cả <b>Quadrant I và Quadrant II</b>) hoàn toàn KHÔNG có nghiệm (còn Q-III chứa \((-1, -20)\) và Q-IV chứa \((1, -20)\)).',
            r'Nếu hệ \(y <\) có đỉnh giao điểm nằm dưới trục Ox (\(y = -8 < 0\)), toàn bộ phần \(y > 0\) (Quadrants I & II) chắc chắn vô nghiệm!',
            {
                'A': ('Bỏ sót Quadrant II', r'Tại Quadrant II (\(x < 0, y > 0\)), \(4x - 12 < -12 < 0 < y\), nên bất phương trình thứ hai cũng bị vi phạm.'),
                'B': ('Bỏ sót Quadrant I', r'Tại Quadrant I (\(x > 0, y > 0\)), \(-2x - 6 < -6 < 0 < y\), nên bất phương trình thứ nhất bị vi phạm.'),
                'C': ('Loại nhầm Quadrant III', r'Điểm \((-1, -20)\) ở Quadrant III thỏa mãn cả \(-20 < -4\) và \(-20 < -16\).'),
                'D': ('Đáp án đúng', r'Mọi nghiệm đều có \(y < -8 < 0\), nên cả Quadrant I và Quadrant II đều không có nghiệm.'),
            },
            r'Gõ thẳng `y < -2x - 6` và `y < 4x - 12` vào Desmos → vùng tô đậm nằm hoàn toàn dưới đường `y = -8` → nhìn 2 giây thấy ngay Q-I và Q-II trống hoàn toàn!'
        ),
        math_mcq(
            'sat_mm7_m2h_q7', 7, 'Algebra', 'Linear functions', 'Hard',
            r'<p>While docked at a maritime fast-charging station, an electric ferry’s battery energy \(P(t)\), in kilowatt-hours, \(t\) minutes after charging begins is modeled by a linear function \(P\) satisfying \(P(t + 6) - P(t) = 27\) for all values of \(t\). If \(P(10) = 195\), what is the value of \(P(0)\)?</p>',
            r'What was the ferry’s battery energy, in kilowatt-hours, at \(t = 0\)?',
            {'A': r'\(120\)', 'B': r'\(150\)', 'C': r'\(168\)', 'D': r'\(240\)'},
            'B',
            r'Hàm \(P(t)\) tuyến tính nên hệ số góc (tốc độ sạc mỗi phút) là \(m = \frac{P(t + 6) - P(t)}{6} = \frac{27}{6} = 4.5\text{ kWh/phút}\). Do đó trong \(10\) phút đầu, pin tăng thêm \(4.5 \times 10 = 45\text{ kWh}\). Năng lượng ban đầu tại \(t = 0\) là: \(P(0) = P(10) - 45 = 195 - 45 = 150\text{ kWh}\).',
            r'Với hàm bậc nhất, công thức \(P(t + \Delta t) - P(t) = m \cdot \Delta t\) cho ra ngay slope \(m = \frac{27}{6} = 4.5\), sau đó lùi ngược về \(t = 0\)!',
            {
                'A': ('Sai slope hoặc trừ dư', r'Trừ nhầm \(75\) thay vì \(45\).'),
                'B': ('Đáp án đúng', r'\(m = 4.5 \Rightarrow P(0) = 195 - 4.5(10) = 150\).'),
                'C': ('Quên chia 6 ở bước nhảy', r'Lấy thẳng \(195 - 27 = 168\) (chỉ lùi 6 phút chứ chưa lùi đủ 10 phút).'),
                'D': ('Cộng thay vì trừ 45', r'Tính \(195 + 45 = 240\), ngược chiều thời gian từ \(t = 10\) về \(t = 0\).'),
            },
            r'Gõ `P(x) = (27/6)*(x - 10) + 195` vào Desmos rồi đọc ngay giao điểm trục Oy `(0, 150)`!'
        ),
        math_mcq(
            'sat_mm7_m2h_q8', 8, 'Algebra', 'Linear equations in one variable', 'Hard',
            r'<p>Consider the linear equation below, where \(k\) is a constant:</p><p style="text-align:center;font-size:18px;">\[\frac{3}{5}(kx - 10) + 4x = 7x - 11\]</p>',
            r'If the equation has <b>no solution</b>, what is the value of \(k\)?',
            {'A': r'\(5\)', 'B': r'\(3\)', 'C': r'\(15\)', 'D': r'\(\frac{55}{3}\)'},
            'A',
            r'Khai triển và gom nhóm theo \(x\) ở vế trái: \(\left(\frac{3k}{5} + 4\right)x - 6 = 7x - 11\). Phương trình bậc nhất một ẩn vô nghiệm khi hệ số của \(x\) hai vế bằng nhau trong khi hằng số tự do khác nhau: \(\frac{3k}{5} + 4 = 7 \Rightarrow \frac{3k}{5} = 3 \Rightarrow k = 5\). Kiểm tra hằng số: \(-6 \neq -11\) (thỏa mãn vô nghiệm!).',
            r'Phương trình \(Ax + B = Cx + D\) vô nghiệm \(\Leftrightarrow A = C\) và \(B \neq D\) — gom hết các số hạng chứa \(x\) về cùng một hệ số trước khi cân bằng!',
            {
                'A': ('Đáp án đúng', r'\(\frac{3(5)}{5} + 4 = 7\) và \(-6 \neq -11\).'),
                'B': ('Bỏ quên phân số 3/5', r'Giải nhầm \(k + 4 = 7 \Rightarrow k = 3\).'),
                'C': ('Quên chia cho 3', r'Giải \(\frac{3k}{5} = 3 \Rightarrow 3k = 15\) rồi dừng ở \(15\).'),
                'D': ('Quên số hạng +4x ở vế trái', r'Cân bằng sai \(\frac{3k}{5} = 11 \Rightarrow k = \frac{55}{3}\).'),
            },
            r'Gõ `y = (3/5)(kx - 10) + 4x` và `y = 7x - 11` trên Desmos, thêm slider `k` → tại `k = 5`, hai đường song song hoàn toàn không cắt nhau!'
        ),
        math_spr(
            'sat_mm7_m2h_q9', 9, 'Advanced Math', 'Nonlinear equations in one variable and systems of equations in two variables', 'Hard',
            r'<p>In the \(xy\)-plane, the line \(y = 6x + k\) intersects the parabola \(y = 2x^2 - 10x + 27\) at <b>exactly one point</b>, where \(k\) is a constant.</p>',
            r'What is the value of \(k\)?',
            ['-5'], '-5',
            r'Lập phương trình hoành độ giao điểm: \(2x^2 - 10x + 27 = 6x + k \Rightarrow 2x^2 - 16x + (27 - k) = 0\). Để đường thẳng cắt parabol tại đúng 1 điểm (tiếp tuyến), biệt thức \(\Delta = 0\): \((-16)^2 - 4(2)(27 - k) = 0 \Rightarrow 256 - 8(27 - k) = 0 \Rightarrow 256 - 216 + 8k = 0 \Rightarrow 8k = -40 \Rightarrow k = -5\).',
            r'Đường thẳng tiếp xúc parabol (đúng 1 giao điểm) \(\Leftrightarrow\) chuyển hết sang một vế rồi đặt \(\Delta = b^2 - 4ac = 0\)!',
            r'Gõ `y = 2x^2 - 10x + 27` và `y = 6x + k` trên Desmos → kéo slider `k` đến `-5` sẽ thấy đường thẳng tiếp xúc parabol tại đúng 1 điểm `(4, 19)`!'
        ),
        math_mcq(
            'sat_mm7_m2h_q10', 10, 'Advanced Math', 'Nonlinear functions', 'Hard',
            r'<p>The exponential function \(f\) is defined by:</p><p style="text-align:center;">\[f(x) = 108 \cdot 3^{x - 3} + 17\]</p>',
            r'What is the \(y\)-intercept of the graph of \(y = f(x) - 5\) in the \(xy\)-plane?',
            {
                'A': r'\((0, 4)\)',
                'B': r'\((0, 12)\)',
                'C': r'\((0, 16)\)',
                'D': r'\((0, 21)\)',
            },
            'C',
            r'Tung độ gốc của \(y = f(x) - 5\) là giá trị tại \(x = 0\): trước hết tính \(f(0) = 108 \cdot 3^{0 - 3} + 17 = 108 \cdot \frac{1}{27} + 17 = 4 + 17 = 21\). Sau đó trừ đi \(5\) theo phép tịnh tiến đề bài: \(y(0) = f(0) - 5 = 21 - 5 = 16\). Vậy \(y\)-intercept là \((0, 16)\).',
            r'Cẩn thận bẫy kép: vừa có số mũ dịch chuyển \((x - 3)\) vừa hỏi đồ thị dịch xuống \(f(x) - 5\) — luôn thay thẳng \(x = 0\) vào cả biểu thức!',
            {
                'A': ('Bỏ quên +17 và -5', r'Chỉ tính \(108 \cdot 3^{-3} = 4\).'),
                'B': ('Nhầm với đường tiệm cận ngang', r'\(y = 17 - 5 = 12\) là tiệm cận ngang (asymptote), không phải y-intercept.'),
                'C': ('Đáp án đúng', r'\(f(0) - 5 = (4 + 17) - 5 = 16 \Rightarrow (0, 16)\).'),
                'D': ('Quên trừ 5', r'\((0, 21)\) là \(y\)-intercept của \(y = f(x)\), chưa trừ \(5\).'),
            },
            r'Gõ `y = 108 * 3^(x - 3) + 17 - 5` lên Desmos rồi bấm thẳng vào giao điểm trục Oy đọc ngay `(0, 16)`!'
        ),
        math_mcq(
            'sat_mm7_m2h_q11', 11, 'Advanced Math', 'Nonlinear functions', 'Hard',
            r'<p>The polynomial \(p(x) = 3x^3 - 7x^2 + kx + 18\), where \(k\) is a constant, is divisible by \((x - 2)\).</p>',
            r'What is the <b>remainder</b> when \(p(x)\) is divided by \((x + 1)\)?',
            {'A': r'\(15\)', 'B': r'\(1\)', 'C': r'\(-7\)', 'D': r'\(29\)'},
            'A',
            r'Bước 1 (Định lý Nhân tử): Vì \(p(x)\) chia hết cho \((x - 2)\), ta có \(p(2) = 0 \Rightarrow 3(8) - 7(4) + 2k + 18 = 0 \Rightarrow 24 - 28 + 18 + 2k = 0 \Rightarrow 14 + 2k = 0 \Rightarrow k = -7\). Bước 2 (Định lý Số dư): Số dư khi chia \(p(x)\) cho \((x + 1)\) chính là \(p(-1) = 3(-1)^3 - 7(-1)^2 + (-7)(-1) + 18 = -3 - 7 + 7 + 18 = 15\).',
            r'Kết hợp Factor Theorem (\(p(2) = 0 \Rightarrow k\)) và Remainder Theorem (số dư chia cho \(x + 1\) chính là \(p(-1)\), chú ý đổi dấu từ \(+1\) sang \(-1\)!).',
            {
                'A': ('Đáp án đúng', r'\(k = -7 \Rightarrow p(-1) = -3 - 7 + 7 + 18 = 15\).'),
                'B': ('Sai dấu hạng tử kx tại x = -1', r'Tính nhầm \((-7)(-1) = -7\) ra \(-3 - 7 - 7 + 18 = 1\).'),
                'C': ('Bẫy dừng ở k', r'\(-7\) mới chỉ là hằng số \(k\), chưa tính số dư \(p(-1)\).'),
                'D': ('Tính p(1) thay vì p(-1)', r'Nhầm chia cho \((x + 1)\) là thay \(x = +1\), hoặc sai dấu bình phương.'),
            },
            r'Gõ `p(x) = 3x^3 - 7x^2 + kx + 18`, tìm `k = -7` từ `p(2) = 0`, rồi gõ `p(-1)` trên Desmos ra ngay `15`!'
        ),
        math_mcq(
            'sat_mm7_m2h_q12', 12, 'Advanced Math', 'Nonlinear equations in one variable and systems of equations in two variables', 'Hard',
            r'<p>In the quadratic equation \(3x^2 - (2k + 5)x + 4k = 0\), where \(k\) is a constant, the <b>product</b> of the two real solutions is \(16\).</p>',
            r'What is the <b>sum</b> of the two solutions to this equation?',
            {
                'A': r'\(29\)',
                'B': r'\(\frac{29}{3}\)',
                'C': r'\(\frac{13}{3}\)',
                'D': r'\(12\)',
            },
            'B',
            r'Theo định lý Vieta, tích hai nghiệm bằng \(\frac{c}{a} = \frac{4k}{3} = 16 \Rightarrow 4k = 48 \Rightarrow k = 12\). Thay \(k = 12\) vào phương trình: \(3x^2 - 29x + 48 = 0\) (kiểm tra \(\Delta = (-29)^2 - 4(3)(48) = 841 - 576 = 265 > 0\), có 2 nghiệm thực phân biệt). Tổng hai nghiệm là \(-\frac{b}{a} = \frac{2k + 5}{3} = \frac{2(12) + 5}{3} = \frac{29}{3}\).',
            r'Khi \(a = 3 \neq 1\), cả hai công thức Vieta (Tích \(\frac{c}{a}\) và Tổng \(-\frac{b}{a}\)) đều PHẢI chia cho \(a = 3\)!',
            {
                'A': ('Quên chia a = 3 ở tổng', r'\(29\) chỉ là \(-b = 2k + 5\), quên chia cho hệ số \(a = 3\).'),
                'B': ('Đáp án đúng', r'\(k = 12 \Rightarrow \text{Tổng} = \frac{2(12) + 5}{3} = \frac{29}{3}\).'),
                'C': ('Quên chia a = 3 ở tích', r'Giải nhầm \(4k = 16 \Rightarrow k = 4 \Rightarrow \frac{2(4) + 5}{3} = \frac{13}{3}\).'),
                'D': ('Bẫy dừng ở k', r'\(12\) chỉ là giá trị của tham số \(k\), chưa tính tổng nghiệm.'),
            },
            r'Giải `4k/3 = 16` ra `k = 12`, sau đó tính `(2*12 + 5)/3` trên Desmos và chuyển sang phân số ra ngay `29/3`!'
        ),
        math_spr(
            'sat_mm7_m2h_q13', 13, 'Advanced Math', 'Nonlinear equations in one variable and systems of equations in two variables', 'Hard',
            r'<p>Consider the rational equation below:</p><p style="text-align:center;font-size:18px;">\[x - \frac{10}{x - 4} = \frac{8x - 42}{x - 4}\]</p>',
            r'What is the valid real solution \(x\) to the given equation?',
            ['8'], '8',
            r'Điều kiện xác định: \(x \neq 4\). Nhân cả hai vế với \((x - 4)\): \(x(x - 4) - 10 = 8x - 42 \Rightarrow x^2 - 4x - 10 = 8x - 42 \Rightarrow x^2 - 12x + 32 = 0 \Rightarrow (x - 4)(x - 8) = 0\). Vì \(x = 4\) làm mẫu số bằng \(0\) (nghiệm ngoại lai, LOẠI!), nghiệm hợp lệ duy nhất là \(x = 8\).',
            r'Phương trình phân thức có mẫu chung \((x - 4)\) trên Hard M2 gần như luôn giấu 1 nghiệm ngoại lai đúng bằng \(4\) — LUÔN đối chiếu điều kiện mẫu khác 0!',
            r'Vẽ `y = x - 10/(x - 4)` và `y = (8x - 42)/(x - 4)` trên Desmos → hai đồ thị chỉ cắt nhau tại ĐÚNG 1 điểm `(8, 5.5)` → `x = 8`!'
        ),
        math_mcq(
            'sat_mm7_m2h_q14', 14, 'Advanced Math', 'Nonlinear functions', 'Hard',
            r'<p>In the \(xy\)-plane, a parabola has its vertex at \((h, -18)\) and passes through the points \((h - 3, 0)\) and \((h + 3, 0)\), where \(h\) is a positive constant. When the equation of the parabola is written in standard form \(y = ax^2 + bx + c\), it is given that \(a + b + c = 14\).</p>',
            r'What is the value of \(h\)?',
            {'A': r'\(2\)', 'B': r'\(3\)', 'C': r'\(4\)', 'D': r'\(5\)'},
            'D',
            r'Bước 1: Viết dạng đỉnh \(f(x) = a(x - h)^2 - 18\). Thay điểm \((h + 3, 0)\) vào để tìm \(a\): \(a\big((h + 3) - h\big)^2 - 18 = 0 \Rightarrow 9a = 18 \Rightarrow a = 2\). Vậy \(f(x) = 2(x - h)^2 - 18\). Bước 2 (Bí kíp 780+): Với đa thức \(f(x) = ax^2 + bx + c\), biểu thức \(a + b + c\) chính là giá trị \(f(1)\)! Do đó: \(f(1) = 2(1 - h)^2 - 18 = 14 \Rightarrow 2(1 - h)^2 = 32 \Rightarrow (1 - h)^2 = 16 \Rightarrow 1 - h = \pm 4\). Giải ra \(h = 5\) hoặc \(h = -3\). Vì \(h > 0\), chọn \(h = 5\)! (Kiểm tra lại: \(2(x - 5)^2 - 18 = 2x^2 - 20x + 32 \Rightarrow 2 - 20 + 32 = 14\)).',
            r'Bí kíp SAT 800: Với mọi hàm bậc hai \(f(x) = ax^2 + bx + c\), ta luôn có \(f(1) = a + b + c\) và \(f(0) = c\) — KHÔNG cần khai triển tung tóe!',
            {
                'A': ('Dừng ở hệ số a = 2', r'\(2\) là hệ số mở \(a\), không phải hoành độ đỉnh \(h\).'),
                'B': ('Nhầm |h| của nghiệm âm -3', r'\(h = -3\) là nghiệm thứ hai nhưng đề yêu cầu \(h > 0\) (khi \(h = 3\) thì \(f(1) = -10\)).'),
                'C': ('Quên số 1 trong (1 - h) = -4', r'Giải \((1 - h)^2 = 16\) ra \(4\) rồi khoanh nhầm \(h = 4\).'),
                'D': ('Đáp án đúng', r'\(2(1 - 5)^2 - 18 = 32 - 18 = 14\) và \(h = 5 > 0\).'),
            },
            r'Gõ `f(x) = 2(x - h)^2 - 18` vào Desmos, thêm slider `h` và kiểm tra dòng `f(1)` → khi `h = 5`, `f(1)` đúng bằng `14`!'
        ),
        math_mcq(
            'sat_mm7_m2h_q15', 15, 'Advanced Math', 'Equivalent expressions', 'Hard',
            r'<p>After an initial intravenous infusion, the plasma concentration \(C(t)\), in micrograms per liter, of a pharmaceutical compound \(t\) hours after dosing is modeled by:</p><p style="text-align:center;">\[C(t) = 1{,}250(0.64)^{\frac{t}{6}}\]</p>',
            r'According to the model, by what percent does the plasma concentration of the compound <b>decrease</b> every \(9\) hours?',
            {
                'A': r'\(36\%\)',
                'B': r'\(51.2\%\)',
                'C': r'\(48.8\%\)',
                'D': r'\(54\%\)',
            },
            'C',
            r'Tìm hệ số còn lại sau mỗi chu kỳ \(t = 9\) giờ bằng cách thay \(t = 9\) vào phần lũy thừa: \((0.64)^{\frac{9}{6}} = (0.64)^{\frac{3}{2}} = \left(\sqrt{0.64}\right)^3 = (0.8)^3 = 0.512\). Điều này nghĩa là sau mỗi \(9\) giờ, nồng độ chỉ còn lại \(51.2\%\), tức đã <b>giảm đi</b> \(1 - 0.512 = 0.488 = 48.8\%\)!',
            r'Khi đổi chu kỳ hàm mũ sang \(9\) giờ, tính hệ số nhân \((0.64)^{9/6} = 0.512\) rồi lấy \(1 - 0.512 = 48.8\%\) — TUYỆT ĐỐI KHÔNG nhân tuyến tính \(36\% \times 1.5 = 54\%\)!',
            {
                'A': ('Chưa đổi chu kỳ từ 6 giờ sang 9 giờ', r'\(36\%\) là tỉ lệ giảm mỗi \(6\) giờ, không phải mỗi \(9\) giờ.'),
                'B': ('Bẫy phần trăm CÒN LẠI', r'\(51.2\%\) là tỉ lệ thuốc CÒN LẠI, đề hỏi tỉ lệ GIẢM ĐI (decrease).'),
                'C': ('Đáp án đúng', r'\(1 - (0.64)^{9/6} = 1 - 0.512 = 0.488 = 48.8\%\).'),
                'D': ('Bẫy nhân tuyến tính 36% × 1.5', r'Hàm mũ giảm theo lãi kép nên mức giảm sau 9 giờ là \(48.8\%\), nhỏ hơn \(36\% \times 1.5 = 54\%\).'),
            },
            r'Gõ `(1 - 0.64^(9/6)) * 100` trên Desmos ra ngay chính xác `48.8`!'
        ),
        math_spr(
            'sat_mm7_m2h_q16', 16, 'Problem-Solving and Data Analysis', 'Ratios, rates, proportional relationships, and units', 'Hard',
            r'<p>A foundry casts a solid bronze monument from a copper–tin alloy with a density of \(8.8\) grams per cubic centimeter. The finished monument has a volume of \(0.045\) cubic meters. (\(1\text{ meter} = 100\text{ centimeters}\); \(1\text{ kilogram} = 1{,}000\text{ grams}\))</p>',
            r'What is the mass of the bronze monument, in <b>kilograms</b>?',
            ['396'], '396',
            r'Bước 1 (Đổi thể tích 3D): \(1\text{ m}^3 = 100^3 = 1{,}000{,}000\text{ cm}^3\), nên \(V = 0.045 \times 10^6 = 45{,}000\text{ cm}^3\). Bước 2 (Tính khối lượng theo gam): \(m = \text{Density} \times V = 8.8 \times 45{,}000 = 396{,}000\text{ g}\). Bước 3 (Đổi sang kilôgam): \(\frac{396{,}000}{1{,}000} = 396\text{ kg}\).',
            r'Đổi thể tích \(\text{m}^3 \to \text{cm}^3\) phải nhân \(100^3 = 10^6\) (một triệu!), rồi nhân khối lượng riêng và chia \(1{,}000\) để ra \(\text{kg}\)!',
            r'Gõ `8.8 * (0.045 * 100^3) / 1000` trên Desmos ra ngay `396`.'
        ),
        math_mcq(
            'sat_mm7_m2h_q17', 17, 'Problem-Solving and Data Analysis', 'Percentages', 'Hard',
            r'<p>An urban vertical hydroponic tower’s weekly basil harvest increased by \(25\%\) from Week 1 to Week 2, and then decreased by \(p\%\) from Week 2 to Week 3. If the Week 3 harvest was \(10\%\) <b>less than</b> the Week 1 harvest, what is the value of \(p\)?</p>',
            r'What is the value of \(p\)?',
            {'A': r'\(15\)', 'B': r'\(28\)', 'C': r'\(35\)', 'D': r'\(72\)'},
            'B',
            r'Đặt sản lượng Tuần 1 là \(100\). Tuần 2 tăng \(25\%\) nên đạt \(100 \times 1.25 = 125\). Tuần 3 thấp hơn Tuần 1 đúng \(10\%\) nên đạt \(100 \times (1 - 0.10) = 90\). Từ Tuần 2 (\(125\)) giảm xuống Tuần 3 (\(90\)), mức giảm tương đối là: \(p\% = \frac{125 - 90}{125} = \frac{35}{125} = \frac{7}{25} = 28\% \Rightarrow p = 28\). (Hoặc giải phương trình \(1.25\left(1 - \frac{p}{100}\right) = 0.90 \Rightarrow 1 - \frac{p}{100} = 0.72 \Rightarrow p = 28\)).',
            r'Với phần trăm kép ngược chiều, luôn lấy mốc ban đầu \(= 100\) và chia cho đúng giá trị GỐC của bước giảm (Tuần 2 \(= 125\), KHÔNG chia cho \(100\))!',
            {
                'A': ('Trừ thẳng 25 - 10', r'Lấy \(25 - 10 = 15\) — sai hoàn toàn bản chất phần trăm nối tiếp.'),
                'B': ('Đáp án đúng', r'\(\frac{125 - 90}{125} = \frac{35}{125} = 28\% \Rightarrow p = 28\).'),
                'C': ('Bẫy cộng thẳng 25 + 10', r'\(35\) là độ giảm tuyệt đối trên nền 100, nhưng phải chia cho nền Tuần 2 là \(125\)!'),
                'D': ('Bẫy tỉ lệ còn lại 72%', r'\(72\%\) là tỉ lệ giữ lại (\(90 / 125\)), không phải tỉ lệ giảm \(p\%\).'),
            },
            r'Gõ `(1 - 0.90 / 1.25) * 100` trên Desmos ra ngay `28`!'
        ),
        math_mcq(
            'sat_mm7_m2h_q18', 18, 'Problem-Solving and Data Analysis', 'One-variable data: Distributions and measures of center and spread', 'Hard',
            tbl_q18 + r'<p>The frequency table above summarizes the number of daily electric ferry crossings recorded over \(25\) days on two maritime routes, Route A and Route B.</p>',
            r'Which of the following statements accurately compares the <b>medians</b> and the <b>means</b> of the two data sets?',
            {
                'A': r'The median of Route A is equal to the median of Route B, and the mean of Route B is greater than the mean of Route A.',
                'B': r'The median of Route B is greater than the median of Route A, and the mean of Route B is greater than the mean of Route A.',
                'C': r'The median of Route A is equal to the median of Route B, and the mean of Route A is equal to the mean of Route B.',
                'D': r'The median of Route A is greater than the median of Route B, and the mean of Route A is less than the mean of Route B.',
            },
            'A',
            r'Cả hai tuyến đều có \(n = 25\) ngày nên trung vị (median) là giá trị đứng ở vị trí thứ \(\frac{25 + 1}{2} = 13\). Cộng dồn tần suất: ở Route A là \(3 \to 8 \to 17\) (vị trí 13 nằm ở mức \(16\)); ở Route B là \(1 \to 5 \to 14\) (vị trí 13 cũng nằm ở mức \(16\)) \(\Rightarrow \text{Median}_A = \text{Median}_B = 16\). Về trung bình cộng (mean): Route A phân bố đối xứng hoàn toàn quanh \(16\) nên \(\text{Mean}_A = 16\). Route B dịch chuyển \(3\) ngày từ nhóm thấp (\(12, 14\)) lên mức cao nhất (\(20\)), nên \(\text{Mean}_B = \frac{1(12) + 4(14) + 9(16) + 5(18) + 6(20)}{25} = \frac{422}{25} = 16.88 > 16\).',
            r'Trong bảng tần suất \(n = 25\), cộng dồn tìm vị trí thứ \(13\) để chốt Median; so sánh Mean nhanh bằng tính đối xứng của Route A so với sự dịch chuyển trọng tâm về phía giá trị lớn của Route B!',
            {
                'A': ('Đáp án đúng', r'\(\text{Median}_A = \text{Median}_B = 16\), còn \(\text{Mean}_B = 16.88 > \text{Mean}_A = 16\).'),
                'B': ('Nhầm Median tăng theo Mean', r'Vị trí thứ 13 của Route B vẫn rơi vào nhóm \(16\) (vì \(1 + 4 = 5 < 13 \le 14\)).'),
                'C': ('Tưởng hai Mean bằng nhau', r'Route B có nhiều ngày đạt 20 chuyến hơn (6 vs 3) và ít ngày 12–14 chuyến hơn nên Mean cao hơn hẳn.'),
                'D': ('So sánh sai chiều Median', r'Hai trung vị bằng nhau (\(16 = 16\)), Route A không có trung vị lớn hơn.'),
            },
            r'Trên Desmos gõ `L = [12, 14, 16, 18, 20]`, `A = [3, 5, 9, 5, 3]`, `B = [1, 4, 9, 5, 6]` rồi tính `total(L*B)/25 = 16.88` so với `total(L*A)/25 = 16`!'
        ),
        math_spr(
            'sat_mm7_m2h_q19', 19, 'Problem-Solving and Data Analysis', 'One-variable data: Distributions and measures of center and spread', 'Hard',
            tbl_q19 + r'<p>The table above shows the mass distribution of all bronze ingots produced in one foundry shift, where \(k\) is a positive integer. The <b>mean</b> mass of all ingots in the batch is \(18\) kilograms.</p>',
            r'What is the value of \(k\)?',
            ['8'], '8',
            r'Áp dụng công thức trung bình có trọng số: \(\frac{12(5) + 15k + 20(7) + 26(5)}{5 + k + 7 + 5} = 18 \Rightarrow \frac{60 + 15k + 140 + 130}{17 + k} = 18 \Rightarrow \frac{330 + 15k}{17 + k} = 18\). Nhân chéo: \(330 + 15k = 18(17 + k) = 306 + 18k \Rightarrow 24 = 3k \Rightarrow k = 8\). (Mẹo cân bằng độ lệch so với Mean 18: \(5(-6) + k(-3) + 7(+2) + 5(+8) = 0 \Rightarrow -30 - 3k + 14 + 40 = 0 \Rightarrow 3k = 24 \Rightarrow k = 8\)!).',
            r'Mẹo SAT 800 (Zero-Sum Deviations): Tổng độ lệch so với Mean luôn bằng \(0\): \(5(-6) + k(-3) + 7(+2) + 5(+8) = 0 \Rightarrow k = 8\) cực nhanh và gọn số!',
            r'Gõ `(60 + 15x + 140 + 130) / (17 + x) = 18` trên Desmos → đọc đường thẳng đứng tại `x = 8`!'
        ),
        math_mcq(
            'sat_mm7_m2h_q20', 20, 'Geometry and Trigonometry', 'Circles', 'Hard',
            svg_q20 + r'<p>In an Olympic velodrome architectural blueprint, a curved turn apron is modeled by circular sector \(OAB\) with center \(O\) and central angle \(\angle AOB = \frac{5\pi}{12}\) radians. The <b>area</b> of sector \(OAB\) is \(120\pi\) square meters.</p>',
            r'What is the length of <b>arc \(AB\)</b>, in meters?',
            {
                'A': r'\(5\pi\)',
                'B': r'\(20\pi\)',
                'C': r'\(10\pi\)',
                'D': r'\(24\pi\)',
            },
            'C',
            r'Bước 1 (Tìm bán kính \(r\) từ diện tích quạt theo radian): \(A = \frac{1}{2}r^2\theta \Rightarrow 120\pi = \frac{1}{2}r^2\left(\frac{5\pi}{12}\right) = \frac{5\pi}{24}r^2\). Chia hai vế cho \(\pi\): \(r^2 = 120 \cdot \frac{24}{5} = 24 \times 24 = 576 \Rightarrow r = 24\text{ m}\). Bước 2 (Tính độ dài cung \(AB\)): \(s = r\theta = 24 \cdot \frac{5\pi}{12} = 10\pi\text{ m}\). (Mẹo nhanh: \(A = \frac{1}{2}rs \Rightarrow s = \frac{2A}{r} = \frac{240\pi}{24} = 10\pi\)!).',
            r'Cặp công thức radian cốt lõi của Hard M2: \(A = \frac{1}{2}r^2\theta\) và \(s = r\theta\) (liên hệ trực tiếp \(A = \frac{1}{2}rs\))!',
            {
                'A': ('Chia đôi nhầm độ dài cung', r'Tính \(s = \frac{1}{2}r\theta = 5\pi\) (nhầm thêm hệ số \(\frac{1}{2}\) vào công thức cung).'),
                'B': ('Quên hệ số 1/2 khi tính diện tích', r'Giải \(r^2 \cdot \frac{5\pi}{12} = 120\pi\) hoặc nhân đôi \(10\pi\) thành \(20\pi\).'),
                'C': ('Đáp án đúng', r'\(r = 24 \Rightarrow s = 24 \cdot \frac{5\pi}{12} = 10\pi\).'),
                'D': ('Bẫy dừng ở bán kính r', r'\(24\) là bán kính \(r\), gắn thêm \(\pi\) thành \(24\pi\) là sai.'),
            },
            r'Gõ `r = sqrt(120 * 24 / 5)` trên Desmos ra `24`, rồi tính `24 * 5/12 = 10` → độ dài cung là `10π`!'
        ),
        math_mcq(
            'sat_mm7_m2h_q21', 21, 'Geometry and Trigonometry', 'Right triangles and trigonometry', 'Hard',
            svg_q21 + r'<p>In the figure above (not drawn to scale), right triangle \(ABC\) is similar to right triangle \(DEF\), where \(\angle B = \angle E = 90^\circ\) and vertices \(A, B, C\) correspond to \(D, E, F\), respectively. It is given that \(AB = 20\), \(BC = 21\), and \(DE = 60\).</p>',
            r'What is the value of \(\sin(D) + \cos(F)\)?',
            {
                'A': r'\(\frac{21}{29}\)',
                'B': r'\(\frac{40}{29}\)',
                'C': r'\(\frac{41}{29}\)',
                'D': r'\(\frac{42}{29}\)',
            },
            'D',
            r'Bước 1 (Bất biến đồng dạng): Vì \(\triangle ABC \sim \triangle DEF\), các góc tương ứng bằng nhau (\(\angle D = \angle A\), \(\angle F = \angle C\)), nên ta tính thẳng trên \(\triangle ABC\) mà không cần nhân tỉ lệ \(DE = 60\). Cạnh huyền \(AC = \sqrt{20^2 + 21^2} = \sqrt{400 + 441} = \sqrt{841} = 29\). Bước 2 (Tính chất góc phụ nhau): Trong tam giác vuông, \(\angle D + \angle F = 90^\circ \Rightarrow \cos(F) = \sin(D)\)! Ta có \(\sin(D) = \sin(A) = \frac{BC}{AC} = \frac{21}{29}\), và \(\cos(F) = \cos(C) = \frac{BC}{AC} = \frac{21}{29}\). Do đó \(\sin(D) + \cos(F) = \frac{21}{29} + \frac{21}{29} = \frac{42}{29}\).',
            r'Đòn combo 780+: (1) Tỉ số lượng giác bất biến theo đồng dạng (bỏ qua \(DE = 60\)), và (2) Góc phụ nhau \(\angle D + \angle F = 90^\circ \Rightarrow \sin(D) = \cos(F)\)!',
            {
                'A': ('Dừng ở sin(D)', r'\(\frac{21}{29}\) chỉ là \(\sin(D)\), quên cộng thêm \(\cos(F) = \frac{21}{29}\).'),
                'B': ('Dùng cạnh kề AB thay vì BC', r'\(\frac{40}{29}\) là giá trị của \(\cos(D) + \sin(F)\), ngược vai trò đối/kề.'),
                'C': ('Quên đồng nhất thức sin(D) = cos(F)', r'Cộng nhầm \(\frac{21}{29} + \frac{20}{29} = \frac{41}{29}\) vì tưởng \(\sin(D)\) và \(\cos(F)\) dùng 2 cạnh khác nhau!'),
                'D': ('Đáp án đúng', r'\(\sin(D) + \cos(F) = \frac{21}{29} + \frac{21}{29} = \frac{42}{29}\).'),
            },
            r'Gõ `c = sqrt(20^2 + 21^2)` ra `29`, rồi tính `21/29 + 21/29` và bấm biểu tượng phân số trên Desmos ra ngay `42/29`!'
        ),
        math_spr(
            'sat_mm7_m2h_q22', 22, 'Geometry and Trigonometry', 'Area and volume', 'Hard',
            svg_q22 + r'<p>A bronze sculpture foundry casts two geometrically similar solid right circular cylindrical pedestals, Column X and Column Y. The total surface area of Column X is \(48\pi\text{ cm}^2\), and the total surface area of Column Y is \(300\pi\text{ cm}^2\). If the volume of Column X is \(128\pi\text{ cm}^3\) and the volume of Column Y is \(v\pi\text{ cm}^3\), what is the value of \(v\)?</p>',
            r'What is the value of \(v\)?',
            ['2000'], '2000',
            r'Hai hình trụ đồng dạng có tỉ số diện tích toàn phần là \(k^2 = \frac{300\pi}{48\pi} = \frac{25}{4}\). Lấy căn bậc hai tìm tỉ số đồng dạng tuyến tính: \(k = \sqrt{\frac{25}{4}} = \frac{5}{2} = 2.5\). Lập phương tìm tỉ số thể tích: \(k^3 = \left(\frac{5}{2}\right)^3 = \frac{125}{8}\). Vậy thể tích Column Y là: \(V_Y = 128\pi \cdot \frac{125}{8} = 16 \cdot 125\pi = 2{,}000\pi \Rightarrow v = 2{,}000\).',
            r'Bậc thang tỉ lệ 3D chuẩn 800 (kể cả khi \(k\) là phân số!): \(k^2 = \frac{300}{48} = \frac{25}{4} \xrightarrow{\sqrt{\cdot}} k = \frac{5}{2} \xrightarrow{(\cdot)^3} k^3 = \frac{125}{8}\)!',
            r'Gõ `128 * (sqrt(300 / 48))^3` trực tiếp vào Desmos ra ngay chính xác `2000`!'
        ),
    ]
