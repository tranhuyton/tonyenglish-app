# -*- coding: utf-8 -*-
"""
Digital SAT Math Adaptive Mock Test #7 — Module 2 Standard/Lower (300–600 Band, 22 Questions)
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
    svg_parabola_vertex, svg_right_triangle, svg_circle_sector, svg_cylinder,
)


def verify_math():
    # Q1: 5x - 9 = 26 => x = 7 => 3x + 2 = 23
    x1 = Fraction(26 + 9, 5)
    assert 5 * x1 - 9 == 26 and 3 * x1 + 2 == 23
    # Q2: F(r) = 14r + 35 => F(0) = 35
    assert 14 * 0 + 35 == 35
    # Q3: slope through (2, 5) and (6, 21) = 16/4 = 4
    assert Fraction(21 - 5, 6 - 2) == 4
    # Q4: x + y = 18, x - y = 4 => x = 11, y = 7
    assert 11 + 7 == 18 and 11 - 7 == 4
    # Q5: 4(x + 3) = 44 => x = 8
    assert 4 * (8 + 3) == 44
    # Q6: 3x + 7 >= 28 => x >= 7
    assert 3 * 7 + 7 == 28 and 3 * 6 + 7 < 28
    # Q7: parallel to y = -3x + 8 through (0, -5) => y = -3x - 5
    assert -3 * 0 - 5 == -5
    # Q8: x + y = 18, 30x + 55y = 740 => x = 10, y = 8
    assert 10 + 8 == 18 and 30 * 10 + 55 * 8 == 740
    # Q9: f(x) = 3x^2 - 4x + 7 => f(5) = 75 - 20 + 7 = 62
    assert 3 * (5 ** 2) - 4 * 5 + 7 == 62
    # Q10: (5x^2 - 3x + 8) + (2x^2 + 7x - 5) = 7x^2 + 4x + 3
    for xv in (0, 2, -3):
        assert (5 * xv ** 2 - 3 * xv + 8) + (2 * xv ** 2 + 7 * xv - 5) == 7 * xv ** 2 + 4 * xv + 3
    # Q11: (x^3)^4 * x^2 = x^14
    assert 3 * 4 + 2 == 14 and (2 ** 3) ** 4 * (2 ** 2) == 2 ** 14
    # Q12: (x - 6)(x + 2) = 0 => roots 6, -2 => sum = 4
    assert (6 - 6) * (6 + 2) == 0 and (-2 - 6) * (-2 + 2) == 0 and 6 + (-2) == 4
    # Q13: f(x) = (x - 4)^2 + 9 => vertex (4, 9) => h + k = 13
    assert (4 - 4) ** 2 + 9 == 9 and 4 + 9 == 13
    # Q14: A(t) = 250(0.85)^t => 1 - 0.85 = 0.15 = 15%
    assert 1 - Fraction(85, 100) == Fraction(15, 100)
    # Q15: sqrt(2x + 7) = 5 => 2x + 7 = 25 => x = 9
    assert math.isclose(math.sqrt(2 * 9 + 7), 5)
    # Q16: 12 laps / 4 min * 15 min = 45 laps
    assert Fraction(12, 4) * 15 == 45
    # Q17: 15% of 320 = 48
    assert Fraction(15, 100) * 320 == 48
    # Q18: median of [145, 162, 138, 174, 151, 169, 158] = 158
    s18 = sorted([145, 162, 138, 174, 151, 169, 158])
    assert s18[3] == 158
    # Q19: Rejected = 24 / 150 = 4/25 = 0.16
    assert 68 + 58 == 126 and 12 + 12 == 24 and 68 + 12 == 80 and 58 + 12 == 70
    assert 126 + 24 == 80 + 70 == 150 and Fraction(24, 150) == Fraction(4, 25)
    # Q20: right triangle with 38 deg => x = 90 - 38 = 52
    assert 90 + 38 + 52 == 180
    # Q21: sector r = 12, angle = 60 deg => (60/360) * 144 = 24
    assert Fraction(60, 360) * (12 ** 2) == 24
    # Q22: cylinder r = 5, h = 10 => V = 25 * 10 * pi = 250pi
    assert (5 ** 2) * 10 == 250


def get_m2l_questions():
    tbl_q18 = build_math_table(
        ['Tower ID', 'T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7'],
        [['Daily Basil Yield (g)', '145', '162', '138', '174', '151', '169', '158']],
        caption='Urban Vertical Hydroponic Tower Daily Harvests',
    )
    tbl_q19 = build_math_table(
        ['Inspection Result', 'Production Line A', 'Production Line B', 'Total'],
        [
            ['Approved', '68', '58', '126'],
            ['Rejected', '12', '12', '24'],
            ['Total', '80', '70', '150'],
        ],
        caption='Pharmaceutical Vial Quality Control Batch',
    )
    svg_q13 = svg_parabola_vertex(h_lbl='h', k_lbl='k', opens_up=True, note='Vertex at (h, k)')
    svg_q20 = svg_right_triangle(
        'AB', 'BC', 'AC', angle_bottom_right='38°', angle_top_left='x°',
        v_top='A', v_right_angle='B', v_right='C', note='Right triangle ABC',
    )
    svg_q21 = svg_circle_sector(
        radius_lbl='r = 12', angle_lbl='60°', center_lbl='O', pt_a='A', pt_b='B',
        note='Circle with center O',
    )
    svg_q22 = svg_cylinder('r = 5', 'h = 10', note='Hydroponic Nutrient Reservoir')

    return [
        math_mcq(
            'sat_mm7_m2l_q1', 1, 'Algebra', 'Linear equations in one variable', 'Easy',
            r'<p>Consider the linear equation \(5x - 9 = 26\).</p>',
            r'What is the value of \(3x + 2\)?',
            {'A': r'\(7\)', 'B': r'\(19\)', 'C': r'\(21\)', 'D': r'\(23\)'},
            'D',
            r'Cộng \(9\) vào cả hai vế: \(5x = 26 + 9 = 35 \Rightarrow x = 7\). Thay \(x = 7\) vào biểu thức đề hỏi: \(3(7) + 2 = 21 + 2 = 23\).',
            r'Giải xong \(x = 7\), nhớ đọc lại câu hỏi để thay vào đúng biểu thức \(3x + 2\)!',
            {
                'A': ('Dừng ở x', r'\(7\) chỉ là giá trị của \(x\), chưa tính \(3x + 2\).'),
                'B': ('Trừ thay vì cộng 2', r'Tính nhầm \(3(7) - 2 = 19\) thay vì cộng \(2\).'),
                'C': ('Quên cộng 2', r'Chỉ tính \(3x = 21\) mà bỏ sót \(+2\).'),
                'D': ('Đáp án đúng', r'\(x = 7 \Rightarrow 3(7) + 2 = 23\).'),
            },
            r'Gõ `5x - 9 = 26` trên Desmos ra `x = 7`, sau đó gõ `3(7) + 2` ra ngay `23`.'
        ),
        math_mcq(
            'sat_mm7_m2l_q2', 2, 'Algebra', 'Linear functions', 'Easy',
            r'<p>An electric harbor ferry operator charges commuter pass holders a total monthly cost \(F(r)\), in dollars, for \(r\) round-trip rides according to the equation:</p><p style="text-align:center;">\[F(r) = 14r + 35\]</p>',
            r'What does the number \(35\) represent in this equation?',
            {
                'A': r'The cost per round-trip ferry ride, in dollars',
                'B': r'The maximum number of rides allowed per month',
                'C': r'The fixed monthly membership fee, in dollars, before any rides are taken',
                'D': r'The discount applied after \(35\) round-trip rides',
            },
            'C',
            r'Trong hàm bậc nhất \(F(r) = 14r + 35\), khi số chuyến \(r = 0\) thì \(F(0) = 35\). Do đó hằng số tự do \(35\) là khoản phí hội viên cố định hàng tháng (flat monthly fee) bất kể số chuyến đi, còn \(14\) là giá tiền mỗi chuyến khứ hồi.',
            r'Hằng số đứng một mình \(b\) trong \(y = mx + b\) luôn là chi phí cố định ban đầu tại \(x = 0\).',
            {
                'A': ('Nhầm với hệ số góc', r'$14 mới là đơn giá mỗi chuyến khứ hồi, không phải $35.'),
                'B': ('Sai đơn vị', r'35 có đơn vị là dollars (tiền), không phải số chuyến đi.'),
                'C': ('Đáp án đúng', r'$35 là khoản phí cố định ban đầu trước khi tính tiền từng chuyến.'),
                'D': ('Suy diễn sai dấu', r'\(+35\) là phí cộng thêm, không phải tiền giảm giá.'),
            },
            r'Thay `r = 0` vào `14(0) + 35 = 35` để thấy ngay đó là chi phí cố định ban đầu.'
        ),
        math_mcq(
            'sat_mm7_m2l_q3', 3, 'Algebra', 'Linear equations in two variables', 'Easy',
            r'<p>A straight line in the \(xy\)-plane passes through the points \((2, 5)\) and \((6, 21)\).</p>',
            r'What is the <b>slope</b> of this line?',
            {'A': r'\(\frac{1}{4}\)', 'B': r'\(4\)', 'C': r'\(3\)', 'D': r'\(16\)'},
            'B',
            r'Áp dụng công thức hệ số góc: \(m = \frac{y_2 - y_1}{x_2 - x_1} = \frac{21 - 5}{6 - 2} = \frac{16}{4} = 4\).',
            r'Slope luôn là \(\frac{\Delta y}{\Delta x}\) — hiệu tung độ chia hiệu hoành độ theo đúng cùng thứ tự điểm!',
            {
                'A': ('Đảo ngược Δx/Δy', r'Tính ngược \(\frac{6 - 2}{21 - 5} = \frac{4}{16} = \frac{1}{4}\).'),
                'B': ('Đáp án đúng', r'\(\frac{21 - 5}{6 - 2} = \frac{16}{4} = 4\).'),
                'C': ('Trừ sai tọa độ', r'Nhầm hiệu tung độ hoặc hiệu hoành độ.'),
                'D': ('Quên chia cho Δx', r'\(16\) mới là \(\Delta y = 21 - 5\), quên chia cho \(6 - 2 = 4\).'),
            },
            r'Gõ `(21 - 5)/(6 - 2)` vào Desmos ra ngay `4`.'
        ),
        math_mcq(
            'sat_mm7_m2l_q4', 4, 'Algebra', 'Systems of two linear equations in two variables', 'Easy',
            r'<p>Consider the system of linear equations below:</p><p style="text-align:center;">\[\begin{cases} x + y = 18 \\ x - y = 4 \end{cases}\]</p>',
            r'What is the value of \(x\)?',
            {'A': r'\(11\)', 'B': r'\(7\)', 'C': r'\(14\)', 'D': r'\(22\)'},
            'A',
            r'Cộng vế theo vế hai phương trình để khử \(y\): \((x + y) + (x - y) = 18 + 4 \Rightarrow 2x = 22 \Rightarrow x = 11\) (và \(y = 7\)).',
            r'Gặp hệ đối xứng \(x + y\) và \(x - y\), cộng thẳng hai phương trình sẽ triệt tiêu ngay \(y\) và ra \(2x\)!',
            {
                'A': ('Đáp án đúng', r'\(2x = 22 \Rightarrow x = 11\).'),
                'B': ('Bẫy tìm y thay vì x', r'\(7\) là giá trị của \(y\), đề yêu cầu tìm \(x\).'),
                'C': ('Trừ hai hằng số', r'\(18 - 4 = 14\) là giá trị của \(2y\), không phải \(x\).'),
                'D': ('Quên chia 2', r'\(22\) là giá trị của \(2x\), cần chia 2 ra \(x = 11\).'),
            },
            r'Vẽ `x + y = 18` và `x - y = 4` trên Desmos → bấm giao điểm `(11, 7)` → đọc ngay `x = 11`.'
        ),
        math_spr(
            'sat_mm7_m2l_q5', 5, 'Algebra', 'Linear equations in one variable', 'Easy',
            r'<p>Solve for \(x\) in the equation below:</p><p style="text-align:center;">\[4(x + 3) = 44\]</p>',
            r'What is the value of \(x\)?',
            ['8'], '8',
            r'Chia cả hai vế cho \(4\): \(x + 3 = 11\). Trừ \(3\) ở hai vế: \(x = 11 - 3 = 8\).',
            r'Khi vế phải chia hết cho hệ số ngoài ngoặc (\(44 / 4 = 11\)), chia trước sẽ nhanh và ít lỗi hơn khai triển!',
            r'Gõ `4(x + 3) = 44` trên Desmos ra ngay đường thẳng đứng `x = 8`.'
        ),
        math_mcq(
            'sat_mm7_m2l_q6', 6, 'Algebra', 'Linear inequalities in one or two variables', 'Easy',
            r'<p>Consider the linear inequality \(3x + 7 \ge 28\).</p>',
            r'Which of the following represents all solutions to the inequality?',
            {'A': r'\(x \le 7\)', 'B': r'\(x \ge 11\)', 'C': r'\(x \ge 7\)', 'D': r'\(x \ge 21\)'},
            'C',
            r'Trừ \(7\) ở cả hai vế: \(3x \ge 21\). Chia hai vế cho \(3\) (số dương nên giữ nguyên chiều dấu): \(x \ge 7\).',
            r'Chỉ đổi chiều dấu bất đẳng thức khi nhân hoặc chia cho số ÂM; chia cho \(+3\) giữ nguyên dấu \(\ge\)!',
            {
                'A': ('Đổi chiều dấu sai', r'Chia cho số dương \(+3\) không được đảo dấu thành \(\le\).'),
                'B': ('Cộng 7 thay vì trừ 7', r'Tính nhầm \(28 + 7 = 35\) rồi làm tròn sai.'),
                'C': ('Đáp án đúng', r'\(3x \ge 21 \Rightarrow x \ge 7\).'),
                'D': ('Quên chia cho 3', r'Dừng lại ở \(3x \ge 21\) chưa chia cho \(3\).'),
            },
            r'Gõ `3x + 7 >= 28` vào Desmos thấy miền tô nằm hoàn toàn từ đường nét liền `x = 7` sang phải.'
        ),
        math_mcq(
            'sat_mm7_m2l_q7', 7, 'Algebra', 'Linear equations in two variables', 'Easy',
            r'<p>In the \(xy\)-plane, line \(q\) is parallel to the line \(y = -3x + 8\) and passes through the point \((0, -5)\).</p>',
            r'Which of the following is the equation of line \(q\)?',
            {
                'A': r'\(y = \frac{1}{3}x - 5\)',
                'B': r'\(y = -3x + 5\)',
                'C': r'\(y = 3x - 5\)',
                'D': r'\(y = -3x - 5\)',
            },
            'D',
            r'Hai đường thẳng song song có cùng hệ số góc \(m = -3\). Vì đường \(q\) đi qua \((0, -5)\) nên tung độ gốc \(b = -5\). Phương trình đường \(q\) là \(y = -3x - 5\).',
            r'Song song \(\Rightarrow\) giữ nguyên hoàn toàn slope \(m = -3\) (kể cả dấu âm!), chỉ thay tung độ gốc \(b = -5\).',
            {
                'A': ('Nhầm đường vuông góc', r'Slope \(\frac{1}{3}\) là của đường vuông góc, không phải đường song song.'),
                'B': ('Sai dấu y-intercept', r'Điểm \((0, -5)\) có tung độ gốc là \(-5\), không phải \(+5\).'),
                'C': ('Đổi mất dấu âm của slope', r'Slope của đường song song phải giữ nguyên là \(-3\), không phải \(+3\).'),
                'D': ('Đáp án đúng', r'Cùng slope \(-3\) và đi qua \((0, -5)\).'),
            },
            r'Vẽ `y = -3x + 8` và `y = -3x - 5` trên Desmos xác nhận hai đường song song và đi qua `(0, -5)`.'
        ),
        math_mcq(
            'sat_mm7_m2l_q8', 8, 'Algebra', 'Systems of two linear equations in two variables', 'Medium',
            r'<p>An urban vertical hydroponic supplier packs \(18\) LED lighting kits in one shipment: \(x\) seedling strips priced at $30 each and \(y\) full-spectrum bars priced at $55 each. The total value of the shipment is $740.</p>',
            r'How many full-spectrum bars (\(y\)) are in the shipment?',
            {'A': r'\(6\)', 'B': r'\(8\)', 'C': r'\(10\)', 'D': r'\(12\)'},
            'B',
            r'Lập hệ hai phương trình: \(x + y = 18\) và \(30x + 55y = 740\). Thế \(x = 18 - y\) vào phương trình thứ hai: \(30(18 - y) + 55y = 740 \Rightarrow 540 + 25y = 740 \Rightarrow 25y = 200 \Rightarrow y = 8\) (và \(x = 10\)).',
            r'Với bài toán số lượng & tổng tiền, lập 2 phương trình rồi thế \(x = 18 - y\) hoặc gõ thẳng vào Desmos tìm giao điểm!',
            {
                'A': ('Sai phép trừ tiền', r'Nếu \(y = 6, x = 12\) thì tổng tiền chỉ là \(360 + 330 = \$690 \neq \$740\).'),
                'B': ('Đáp án đúng', r'\(10(30) + 8(55) = 300 + 440 = \$740\).'),
                'C': ('Bẫy tìm x thay vì y', r'\(10\) là số lượng seedling strips (\(x\)), đề hỏi full-spectrum bars (\(y\)).'),
                'D': ('Thử sai số lượng', r'Nếu \(y = 12, x = 6\) thì tổng tiền là \(180 + 660 = \$840\).'),
            },
            r'Gõ `x + y = 18` và `30x + 55y = 740` trên Desmos → bấm giao điểm `(10, 8)` → `y = 8`!'
        ),
        math_spr(
            'sat_mm7_m2l_q9', 9, 'Advanced Math', 'Nonlinear functions', 'Easy',
            r'<p>The quadratic function \(f\) is defined by \(f(x) = 3x^2 - 4x + 7\).</p>',
            r'What is the value of \(f(5)\)?',
            ['62'], '62',
            r'Thay \(x = 5\) vào biểu thức hàm số (tính lũy thừa trước khi nhân): \(f(5) = 3(5^2) - 4(5) + 7 = 3(25) - 20 + 7 = 75 - 20 + 7 = 62\).',
            r'Thứ tự phép tính PEMDAS: luôn bình phương \(5^2 = 25\) TRƯỚC rồi mới nhân với \(3\)!',
            r'Gõ `f(x) = 3x^2 - 4x + 7` rồi gõ `f(5)` trên Desmos ra ngay `62`.'
        ),
        math_mcq(
            'sat_mm7_m2l_q10', 10, 'Advanced Math', 'Equivalent expressions', 'Easy',
            r'<p>Consider the sum of polynomials below:</p><p style="text-align:center;">\[(5x^2 - 3x + 8) + (2x^2 + 7x - 5)\]</p>',
            r'Which of the following is equivalent to the given expression?',
            {
                'A': r'\(7x^2 + 4x + 3\)',
                'B': r'\(7x^2 - 4x + 3\)',
                'C': r'\(7x^2 + 10x + 13\)',
                'D': r'\(3x^2 + 4x + 3\)',
            },
            'A',
            r'Gom các hạng tử đồng dạng theo từng bậc của \(x\): bậc hai \((5 + 2)x^2 = 7x^2\); bậc nhất \((-3 + 7)x = +4x\); hằng số \(8 - 5 = +3\). Kết quả: \(7x^2 + 4x + 3\).',
            r'Cộng đa thức: ghép từng cột \(x^2\), \(x\), hằng số và kiểm tra kỹ dấu \(-3 + 7 = +4\).',
            {
                'A': ('Đáp án đúng', r'\((5 + 2)x^2 + (-3 + 7)x + (8 - 5) = 7x^2 + 4x + 3\).'),
                'B': ('Sai dấu -3 + 7', r'Nhầm \(-3 + 7\) thành \(-4\) thay vì \(+4\).'),
                'C': ('Bỏ qua dấu trừ', r'Cộng trị tuyệt đối \(3 + 7 = 10\) và \(8 + 5 = 13\).'),
                'D': ('Trừ nhầm hệ số x²', r'Lấy \(5 - 2 = 3\) thay vì cộng \(5 + 2 = 7\).'),
            },
            r'Gõ `(5x^2 - 3x + 8) + (2x^2 + 7x - 5)` và so khớp đồ thị với phương án A trên Desmos.'
        ),
        math_mcq(
            'sat_mm7_m2l_q11', 11, 'Advanced Math', 'Equivalent expressions', 'Easy',
            r'<p>For a positive real number \(x\), consider the exponential expression:</p><p style="text-align:center;">\[(x^3)^4 \cdot x^2\]</p>',
            r'Which of the following is equivalent to the given expression?',
            {'A': r'\(x^9\)', 'B': r'\(x^{12}\)', 'C': r'\(x^{14}\)', 'D': r'\(x^{24}\)'},
            'C',
            r'Bước 1 (Lũy thừa của lũy thừa — NHÂN số mũ): \((x^3)^4 = x^{3 \times 4} = x^{12}\). Bước 2 (Nhân hai lũy thừa cùng cơ số — CỘNG số mũ): \(x^{12} \cdot x^2 = x^{12 + 2} = x^{14}\).',
            r'Phân biệt rõ: \((x^a)^b = x^{a \cdot b}\) (nhân mũ), còn \(x^m \cdot x^n = x^{m + n}\) (cộng mũ)!',
            {
                'A': ('Cộng hết các số mũ', r'Lấy \(3 + 4 + 2 = 9\) — sai quy tắc \((x^3)^4\).'),
                'B': ('Quên nhân với x²', r'Chỉ tính \((x^3)^4 = x^{12}\) mà bỏ sót nhân tử \(x^2\).'),
                'C': ('Đáp án đúng', r'\(x^{3 \times 4 + 2} = x^{14}\).'),
                'D': ('Nhân luôn số mũ 12 × 2', r'Khi nhân cùng cơ số \(x^{12} \cdot x^2\) phải CỘNG mũ, không nhân \(12 \times 2 = 24\).'),
            },
            r'Thử thay `x = 2`: gõ `(2^3)^4 * 2^2 = 16384` và `2^14 = 16384` trên Desmos để xác nhận ngay!'
        ),
        math_mcq(
            'sat_mm7_m2l_q12', 12, 'Advanced Math', 'Nonlinear equations in one variable and systems of equations in two variables', 'Easy',
            r'<p>Consider the quadratic equation in factored form:</p><p style="text-align:center;">\[(x - 6)(x + 2) = 0\]</p>',
            r'What is the <b>sum</b> of the solutions to the given equation?',
            {'A': r'\(-12\)', 'B': r'\(-4\)', 'C': r'\(8\)', 'D': r'\(4\)'},
            'D',
            r'Đặt từng nhân tử bằng \(0\): \(x - 6 = 0 \Rightarrow x = 6\), và \(x + 2 = 0 \Rightarrow x = -2\). Tổng hai nghiệm là \(6 + (-2) = 4\).',
            r'Nhớ ĐỔI DẤU khi đọc nghiệm từ dạng nhân tử \((x - r) = 0 \Rightarrow x = r\): nghiệm là \(+6\) và \(-2\), không phải \(-6\) và \(+2\)!',
            {
                'A': ('Tính tích thay vì tổng', r'\(6 \times (-2) = -12\) là tích hai nghiệm, đề hỏi tổng.'),
                'B': ('Đọc ngược dấu hai nghiệm', r'Cộng nhầm \((-6) + 2 = -4\) do quên đổi dấu trong ngoặc.'),
                'C': ('Quên dấu âm của nghiệm -2', r'Cộng \(6 + 2 = 8\) thay vì \(6 + (-2)\).'),
                'D': ('Đáp án đúng', r'\(6 + (-2) = 4\).'),
            },
            r'Vẽ `y = (x - 6)(x + 2)` trên Desmos → đọc 2 giao điểm trục Ox `-2` và `6` → `-2 + 6 = 4`.'
        ),
        math_spr(
            'sat_mm7_m2l_q13', 13, 'Advanced Math', 'Nonlinear functions', 'Medium',
            svg_q13 + r'<p>In the \(xy\)-plane, the graph of the quadratic function \(f(x) = (x - 4)^2 + 9\) is a parabola with its vertex at \((h, k)\), as shown above.</p>',
            r'What is the value of \(h + k\)?',
            ['13'], '13',
            r'Đối chiếu trực tiếp với dạng đỉnh chuẩn \(f(x) = a(x - h)^2 + k\): ta đọc được ngay hoành độ đỉnh \(h = 4\) (đổi dấu của \(-4\)) và tung độ đỉnh \(k = 9\) (giữ nguyên dấu của \(+9\)). Vậy \(h + k = 4 + 9 = 13\).',
            r'Trong Vertex Form \((x - h)^2 + k\): \(h\) ngược dấu trong ngoặc (\(4\)), còn \(k\) cùng dấu ngoài ngoặc (\(9\))!',
            r'Vẽ `y = (x - 4)^2 + 9` trên Desmos → bấm trực tiếp vào đỉnh parabol đọc ngay `(4, 9)` → `4 + 9 = 13`.'
        ),
        math_mcq(
            'sat_mm7_m2l_q14', 14, 'Advanced Math', 'Nonlinear functions', 'Medium',
            r'<p>In a pharmacokinetic dosage test, the amount \(A(t)\), in milligrams, of medication remaining in a patient’s body \(t\) hours after taking a tablet is modeled by:</p><p style="text-align:center;">\[A(t) = 250(0.85)^t\]</p>',
            r'According to the model, by what percent does the amount of medication <b>decrease</b> each hour?',
            {'A': r'\(0.85\%\)', 'B': r'\(15\%\)', 'C': r'\(85\%\)', 'D': r'\(25\%\)'},
            'B',
            r'So sánh với dạng suy giảm hàm mũ chuẩn \(A(t) = A_0(1 - r)^t\): hệ số cơ số là \(1 - r = 0.85 \Rightarrow r = 1 - 0.85 = 0.15 = 15\%\). Nghĩa là mỗi giờ lượng thuốc giữ lại \(85\%\) và giảm đi \(15\%\).',
            r'Khi cơ số nhỏ hơn 1 (\(0.85\)), tỉ lệ giảm mỗi chu kỳ luôn là \(1 - 0.85 = 0.15 = 15\%\) (KHÔNG chọn \(85\%\)!).',
            {
                'A': ('Đọc nhầm số thập phân sang %', r'\(0.85\) là \(85\%\), không phải \(0.85\%\), và đó cũng là phần còn lại.'),
                'B': ('Đáp án đúng', r'\(1 - 0.85 = 0.15 = 15\%\) giảm mỗi giờ.'),
                'C': ('Bẫy tỉ lệ CÒN LẠI 85%', r'\(85\%\) là phần trăm thuốc giữ lại, đề hỏi phần trăm GIẢM ĐI.'),
                'D': ('Nhầm từ hệ số 250', r'\(250\) là liều ban đầu (mg), không phải tỉ lệ \(25\%\).'),
            },
            r'Gõ `(1 - 0.85) * 100` trên Desmos ra ngay `15`.'
        ),
        math_mcq(
            'sat_mm7_m2l_q15', 15, 'Advanced Math', 'Nonlinear equations in one variable and systems of equations in two variables', 'Medium',
            r'<p>Consider the radical equation below:</p><p style="text-align:center;">\[\sqrt{2x + 7} = 5\]</p>',
            r'What is the value of \(x\)?',
            {'A': r'\(9\)', 'B': r'\(16\)', 'C': r'\(-1\)', 'D': r'\(18\)'},
            'A',
            r'Bình phương cả hai vế để khử dấu căn: \(2x + 7 = 5^2 = 25 \Rightarrow 2x = 18 \Rightarrow x = 9\). Thử lại: \(\sqrt{2(9) + 7} = \sqrt{25} = 5\) (đúng!).',
            r'Để phá dấu căn bậc hai, nhớ bình phương CẢ HAI VẾ (\(5 \to 25\)), không để nguyên \(5\)!',
            {
                'A': ('Đáp án đúng', r'\(2(9) + 7 = 25\) và \(\sqrt{25} = 5\).'),
                'B': ('Cộng 7 thay vì trừ 7', r'Tính nhầm \(2x = 25 + 7 = 32 \Rightarrow x = 16\).'),
                'C': ('Quên bình phương vế phải', r'Giải nhầm \(2x + 7 = 5 \Rightarrow x = -1\).'),
                'D': ('Quên chia 2', r'Dừng lại ở \(2x = 18\) chưa chia cho \(2\).'),
            },
            r'Gõ `y = sqrt(2x + 7)` và `y = 5` trên Desmos → bấm giao điểm `(9, 5)` → `x = 9`.'
        ),
        math_spr(
            'sat_mm7_m2l_q16', 16, 'Problem-Solving and Data Analysis', 'Ratios, rates, proportional relationships, and units', 'Easy',
            r'<p>During an Olympic velodrome training session, a track cyclist completes \(12\) laps in \(4\) minutes at a constant speed.</p>',
            r'At this same rate, how many laps will the cyclist complete in \(15\) minutes?',
            ['45'], '45',
            r'Tốc độ chạy mỗi phút là \(\frac{12\text{ vòng}}{4\text{ phút}} = 3\text{ vòng/phút}\). Trong \(15\) phút, tay đua hoàn thành \(3 \times 15 = 45\) vòng.',
            r'Tìm đơn giá cho 1 đơn vị thời gian (unit rate = 3 vòng/phút) rồi nhân với \(15\) phút!',
            r'Gõ `(12 / 4) * 15` trên Desmos ra ngay `45`.'
        ),
        math_mcq(
            'sat_mm7_m2l_q17', 17, 'Problem-Solving and Data Analysis', 'Percentages', 'Easy',
            r'<p>A bronze sculpture foundry prepares \(320\) kilograms of molten bronze alloy for a casting batch. If \(15\%\) of the batch by mass is tin, how many kilograms of tin are in the batch?</p>',
            r'How many kilograms of tin are in the batch?',
            {'A': r'\(32\)', 'B': r'\(42\)', 'C': r'\(48\)', 'D': r'\(54\)'},
            'C',
            r'Tính \(15\%\) của \(320\): \(0.15 \times 320 = 48\text{ kg}\). (Mẹo nhẩm nhanh: \(10\%\) là \(32\), thêm một nửa của \(32\) là \(16 \Rightarrow 32 + 16 = 48\text{ kg}\)).',
            r'Mẹo tính nhanh \(15\%\): lấy \(10\%\) cộng thêm nửa của nó (\(32 + 16 = 48\))!',
            {
                'A': ('Chỉ tính 10%', r'\(32\) là \(10\%\) của \(320\), thiếu thêm \(5\% = 16\).'),
                'B': ('Nhân sai chữ số', r'Cộng nhầm \(32 + 10 = 42\).'),
                'C': ('Đáp án đúng', r'\(0.15 \times 320 = 48\text{ kg}\).'),
                'D': ('Tính dư phần trăm', r'\(54\) lớn hơn \(15\%\) của \(320\).'),
            },
            r'Gõ `0.15 * 320` trên Desmos ra ngay `48`.'
        ),
        math_mcq(
            'sat_mm7_m2l_q18', 18, 'Problem-Solving and Data Analysis', 'One-variable data: Distributions and measures of center and spread', 'Medium',
            tbl_q18 + r'<p>The table above records the daily basil harvest, in grams, collected from \(7\) vertical hydroponic towers.</p>',
            r'What is the <b>median</b> daily basil yield, in grams, of the \(7\) towers?',
            {'A': r'\(151\)', 'B': r'\(174\)', 'C': r'\(162\)', 'D': r'\(158\)'},
            'D',
            r'Sắp xếp 7 giá trị theo thứ tự tăng dần: \(138,\; 145,\; 151,\; \mathbf{158},\; 162,\; 169,\; 174\). Với \(7\) phần tử, trung vị (median) là số đứng chính giữa ở vị trí thứ \(4\), tức là \(158\text{ g}\).',
            r'TUYỆT ĐỐI PHẢI sắp xếp dãy số từ bé đến lớn trước khi lấy số chính giữa — đừng chọn bừa ô ở giữa bảng chưa sắp xếp (\(174\))!',
            {
                'A': ('Lấy vị trí thứ 3', r'\(151\) đứng thứ 3 sau khi sắp xếp, chưa phải chính giữa (vị trí 4).'),
                'B': ('Bẫy quên sắp xếp bảng', r'\(174\) chỉ đứng giữa trong bảng gốc (cột T4), nhưng lại là giá trị lớn nhất!'),
                'C': ('Lấy vị trí thứ 5', r'\(162\) đứng thứ 5 trong dãy tăng dần.'),
                'D': ('Đáp án đúng', r'Số đứng thứ 4 trong dãy tăng dần là \(158\).'),
            },
            r'Gõ `median(145, 162, 138, 174, 151, 169, 158)` trực tiếp vào Desmos ra ngay `158`!'
        ),
        math_spr(
            'sat_mm7_m2l_q19', 19, 'Problem-Solving and Data Analysis', 'Probability and conditional probability', 'Medium',
            tbl_q19 + r'<p>The table above shows the quality control inspection results for \(150\) pharmaceutical dosage vials produced on two bottling lines.</p>',
            r'If one vial is selected at random from all \(150\) vials inspected, what is the probability that the selected vial was <b>rejected</b>? (Enter your answer as a fraction or a decimal.)',
            ['4/25', '0.16', '.16'], '4/25 (hoặc 0.16)',
            r'Tổng số lọ thuốc bị loại (Rejected) ở cả hai dây chuyền là \(24\) lọ trên tổng số \(150\) lọ kiểm tra. Xác suất chọn ngẫu nhiên trúng một lọ bị loại là \(\frac{24}{150} = \frac{4}{25} = 0.16\).',
            r'Xác suất cơ bản \(= \frac{\text{Số phần tử thỏa điều kiện}}{\text{Tổng toàn bảng}} = \frac{24}{150} = \frac{4}{25} = 0.16\).',
            r'Gõ `24 / 150` trên Desmos ra `0.16`, bấm biểu tượng phân số ra `4/25`.'
        ),
        math_mcq(
            'sat_mm7_m2l_q20', 20, 'Geometry and Trigonometry', 'Lines, angles, and triangles', 'Easy',
            svg_q20 + r'<p>The side profile of a velodrome entry ramp forms right triangle \(ABC\) shown above, where \(\angle B = 90^\circ\) and \(\angle C = 38^\circ\).</p>',
            r'What is the value of \(x\)?',
            {'A': r'\(52\)', 'B': r'\(38\)', 'C': r'\(62\)', 'D': r'\(142\)'},
            'A',
            r'Tổng ba góc trong một tam giác bằng \(180^\circ\). Vì \(\angle B = 90^\circ\), hai góc nhọn còn lại phụ nhau (tổng bằng \(90^\circ\)): \(x = 90 - 38 = 52\).',
            r'Trong tam giác vuông, hai góc nhọn luôn cộng lại đúng bằng \(90^\circ\)!',
            {
                'A': ('Đáp án đúng', r'\(90^\circ - 38^\circ = 52^\circ\).'),
                'B': ('Tưởng hai góc nhọn bằng nhau', r'Chỉ khi tam giác vuông cân hai góc nhọn mới bằng \(45^\circ\).'),
                'C': ('Trừ nhầm 90 - 38', r'Tính nhầm \(90 - 38 = 62\) do quên nhớ \(1\) ở hàng chục.'),
                'D': ('Trừ cho 180 thay vì 90', r'Tính \(180 - 38 = 142\), quên trừ góc vuông \(90^\circ\).'),
            },
            r'Gõ `90 - 38` trên Desmos ra ngay `52`.'
        ),
        math_mcq(
            'sat_mm7_m2l_q21', 21, 'Geometry and Trigonometry', 'Circles', 'Medium',
            svg_q21 + r'<p>The figure above shows a circular bronze medallion mold with center \(O\), radius \(r = 12\) centimeters, and shaded sector \(OAB\) with central angle \(60^\circ\).</p>',
            r'What is the <b>area</b>, in square centimeters, of the shaded sector \(OAB\)?',
            {
                'A': r'\(12\pi\)',
                'B': r'\(24\pi\)',
                'C': r'\(72\pi\)',
                'D': r'\(144\pi\)',
            },
            'B',
            r'Góc \(60^\circ\) chiếm \(\frac{60^\circ}{360^\circ} = \frac{1}{6}\) cả hình tròn. Diện tích cả hình tròn là \(\pi r^2 = \pi(12^2) = 144\pi\). Do đó diện tích hình quạt tô đậm là \(\frac{1}{6} \times 144\pi = 24\pi\text{ cm}^2\).',
            r'Góc \(60^\circ\) chính là \(\frac{1}{6}\) đường tròn \(\Rightarrow\) lấy diện tích cả hình tròn \(144\pi\) chia \(6\) ra ngay \(24\pi\)!',
            {
                'A': ('Dùng công thức chu vi 2πr', r'\(\frac{1}{6}(24\pi) = 4\pi\) hoặc nhầm \(r = 12\) thay vì \(r^2 = 144\).'),
                'B': ('Đáp án đúng', r'\(\frac{60}{360} \cdot \pi(12^2) = \frac{1}{6}(144\pi) = 24\pi\).'),
                'C': ('Chia 2 thay vì chia 6', r'\(72\pi\) là diện tích nửa hình tròn (\(180^\circ\)), không phải \(60^\circ\).'),
                'D': ('Diện tích cả hình tròn', r'\(144\pi\) là diện tích toàn hình tròn, quên nhân tỉ lệ \(\frac{60}{360}\).'),
            },
            r'Gõ `(60 / 360) * 12^2` trên Desmos ra ngay `24` → đáp án `24π`.'
        ),
        math_spr(
            'sat_mm7_m2l_q22', 22, 'Geometry and Trigonometry', 'Area and volume', 'Medium',
            svg_q22 + r'<p>A right circular cylindrical nutrient reservoir for a vertical hydroponic facility has radius \(r = 5\) feet and height \(h = 10\) feet, as shown above.</p>',
            r'If the volume of the reservoir is \(v\pi\) cubic feet, what is the value of \(v\)?',
            ['250'], '250',
            r'Áp dụng công thức thể tích hình trụ (có sẵn trên Reference Sheet): \(V = \pi r^2 h = \pi(5^2)(10) = 250\pi\text{ ft}^3\). Đối chiếu với \(v\pi\), ta được \(v = 250\).',
            r'Thể tích hình trụ \(V = \pi r^2 h\): nhớ bình phương bán kính (\(5^2 = 25\)) trước khi nhân chiều cao \(h = 10\), và chỉ điền hệ số \(250\) (không điền \(\pi\))!',
            r'Gõ `5^2 * 10` trên Desmos ra ngay `250`.'
        ),
    ]
