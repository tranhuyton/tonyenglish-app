# -*- coding: utf-8 -*-
"""
Digital SAT Math Adaptive Mock Test #7 — Module 1 (Routing Module, 22 Questions)
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
    svg_parallel_transversal, svg_right_triangle,
    svg_circle_sector, svg_parabola_vertex,
)


def verify_math():
    # Q1: 4(3x - 5) + 7 = 5x + 15 => 7x = 28 => x = 4 => 6x - 5 = 19
    x1 = Fraction(28, 7)
    assert 4 * (3 * x1 - 5) + 7 == 5 * x1 + 15 and 6 * x1 - 5 == 19
    # Q2: E(d) = 480 - 18d => E(d+1) - E(d) = -18
    assert (480 - 18 * 1) - (480 - 18 * 0) == -18
    # Q3: g(3)=22, g(7)=46, g(11)=70 => m=6, b=4 => g(15)=94
    m3 = Fraction(46 - 22, 7 - 3)
    b3 = 22 - m3 * 3
    assert m3 == 6 and m3 * 11 + b3 == 70 and m3 * 15 + b3 == 94
    # Q4: 5x + 3y = 47, 2x - y = 10 => x = 7, y = 4 => 3x - 2y = 13
    assert 5 * 7 + 3 * 4 == 47 and 2 * 7 - 4 == 10 and 3 * 7 - 2 * 4 == 13
    # Q5: 8x - 6y = 21, kx + 15y = 35 no solution => k/8 = 15/(-6) = -5/2 => k = -20
    k5 = Fraction(8 * 15, -6)
    assert k5 == -20 and Fraction(35, 21) != Fraction(15, -6)
    # Q6: 4x - 7y = 28 => m = 4/7 => perp m = -7/4 through (4, -2) => y = -(7/4)x + 5
    assert Fraction(4, 7) * Fraction(-7, 4) == -1 and Fraction(-7, 4) * 4 + 5 == -2
    # Q7: 75(22) + 50y <= 3120 => 50y <= 1470 => y <= 29.4 => max integer 29
    assert 75 * 22 + 50 * 29 <= 3120 and 75 * 22 + 50 * 30 > 3120
    # Q8: 7a + 4b = 58, 2a + 5b = 41 => 9a + 9b = 99 => 3a + 3b = 33
    a8, b8 = Fraction(14, 3), Fraction(19, 3)
    assert 7 * a8 + 4 * b8 == 58 and 2 * a8 + 5 * b8 == 41 and 3 * a8 + 3 * b8 == 33
    # Q9: f(x) = a(x - 5)^2 - 4, f(8) = 14 => 9a = 18 => a = 2 => f(9) = 28
    a9 = Fraction(14 - (-4), (8 - 5) ** 2)
    assert a9 == 2 and a9 * (9 - 5) ** 2 - 4 == 28
    # Q10: 3x^2 - 18x + c = 0 => (-18)^2 - 4(3)c = 0 => c = 27
    assert (-18) ** 2 - 4 * 3 * 27 == 0
    # Q11: (x^2 - 16)/(x^2 + 7x + 12) = (x - 4)/(x + 3) for x > 4
    for xv in (5, 7, 10):
        assert Fraction(xv ** 2 - 16, xv ** 2 + 7 * xv + 12) == Fraction(xv - 4, xv + 3)
    # Q12: M(t) = 640 * (1/2)^(t/4) at t = 12 => 640 * (1/2)^3 = 80
    assert 640 * Fraction(1, 2) ** 3 == 80
    # Q13: 4x^2 - 26x + 15 = 0 => D = 436 > 0, sum = 26/4 = 13/2 = 6.5
    assert (-26) ** 2 - 4 * 4 * 15 > 0 and Fraction(26, 4) == Fraction(13, 2)
    # Q14: sqrt(5x + 24) = x + 2 => x = 5 valid, x = -4 extraneous
    assert math.isclose(math.sqrt(5 * 5 + 24), 5 + 2) and (-4 + 2) < 0
    assert 5 * (-4) + 24 == (-4 + 2) ** 2  # confirms -4 is algebraic root of squared eq
    # Q15: f(x) = x^2 - 6x + 14 = (x - 3)^2 + 5 => g(x) = f(x + 2) - 9 has vertex (1, -4)
    assert (3 - 2, 5 - 9) == (1, -4)
    assert (1 + 2) ** 2 - 6 * (1 + 2) + 14 - 9 == -4
    # Q16: 1296 in^2 / 144 = 9 ft^2
    assert Fraction(1296, 12 ** 2) == 9
    # Q17: Island Express delayed = 27 / 90 = 3/10
    assert 48 + 12 == 60 and 63 + 27 == 90 and 39 + 11 == 50
    assert 48 + 63 + 39 == 150 and 12 + 27 + 11 == 50 and 150 + 50 == 200
    assert Fraction(27, 90) == Fraction(3, 10)
    # Q18: y_hat = 24.5(48) - 620 = 556, actual = 550 => 556 - 550 = 6
    pred18 = Fraction(49, 2) * 48 - 620
    assert pred18 == 556 and pred18 - 550 == 6
    # Q19: A = 1.25 B, C = 0.36 A => C = 0.45 B => p = 45
    assert Fraction(125, 100) * Fraction(36, 100) == Fraction(45, 100)
    # Q20: 5x + 18 = 7x - 16 => x = 17 => obtuse = 103 => acute = 77
    assert 5 * 17 + 18 == 7 * 17 - 16 == 103 and 180 - 103 == 77
    # Q21: Sector area r = 24, theta = 75 deg => (75/360) * 576 = 120
    assert Fraction(75, 360) * (24 ** 2) == 120
    # Q22: Right triangle ABC, AC = 51, sin(A) = 8/17 => BC = 24, AB = 45
    assert Fraction(24, 51) == Fraction(8, 17) and 24 ** 2 + 45 ** 2 == 51 ** 2


def get_m1_questions():
    tbl_q3 = build_math_table(
        [r'Vertical Tiers \(x\)', r'Recirculation Flow \(g(x)\) (L/hr)'],
        [['3', '22'], ['7', '46'], ['11', '70']],
        caption='Urban Vertical Hydroponic Tower Flow Rate',
    )
    tbl_q17 = build_math_table(
        ['Ferry Route', 'On-Time', 'Delayed', 'Total'],
        [
            ['Harbor Loop', '48', '12', '60'],
            ['Island Express', '63', '27', '90'],
            ['Bay Commuter', '39', '11', '50'],
            ['Total', '150', '50', '200'],
        ],
        caption='Electric Ferry Maritime Departures (Monthly Log)',
    )
    tbl_q18 = build_math_table(
        [r'Track Speed \(x\) (km/h)', r'Measured Power \(y\) (watts)'],
        [['44', '462'], ['48', '550'], ['52', '660'], ['56', '745']],
        caption='Olympic Velodrome Wind-Tunnel Test Data',
    )
    svg_q9 = svg_parabola_vertex(
        h_lbl='5', k_lbl='-4', opens_up=True, pt_lbl='(8, 14)', note='Graph of y = f(x)'
    )
    svg_q20 = svg_parallel_transversal(
        'ℓ', 'm', ang1_lbl='(5x + 18)°', ang2_lbl='', ang3_lbl='(7x − 16)°',
        note='Note: Figure not drawn to scale.',
    )
    svg_q21 = svg_circle_sector(
        radius_lbl='24 m', angle_lbl='75°', center_lbl='O', pt_a='A', pt_b='B',
        note='Note: Figure not drawn to scale.',
    )
    svg_q22 = svg_right_triangle(
        'AB', 'BC', '51', angle_top_left='A', v_top='A', v_right_angle='B', v_right='C',
        note='sin(A) = 8/17',
    )

    return [
        math_mcq(
            'sat_mm7_m1_q1', 1, 'Algebra', 'Linear equations in one variable', 'Easy',
            r'<p>Consider the linear equation shown below:</p><p style="text-align:center;font-size:18px;">\[4(3x - 5) + 7 = 5x + 15\]</p>',
            r'What is the value of \(6x - 5\)?',
            {'A': r'\(4\)', 'B': r'\(14\)', 'C': r'\(19\)', 'D': r'\(29\)'},
            'C',
            r'Khai triển vế trái: \(12x - 20 + 7 = 5x + 15 \Rightarrow 12x - 13 = 5x + 15 \Rightarrow 7x = 28 \Rightarrow x = 4\). Thay \(x = 4\) vào biểu thức đề hỏi: \(6(4) - 5 = 24 - 5 = 19\).',
            r'Luôn kiểm tra kỹ biểu thức cuối đề yêu cầu (\(6x - 5\)) — đừng dừng sớm ngay sau khi tìm được \(x = 4\)!',
            {
                'A': ('Bẫy dừng ở x', r'\(4\) mới chỉ là giá trị của \(x\), chưa tính \(6x - 5\).'),
                'B': ('Sai dấu hằng số khi giải', r'Nhầm \(-20 + 7\) hoặc trừ nhầm \(6(4) - 10 = 14\).'),
                'C': ('Đáp án đúng', r'\(x = 4 \Rightarrow 6(4) - 5 = 19\).'),
                'D': ('Cộng thay vì trừ 5', r'Tính nhầm \(6(4) + 5 = 29\) thay vì \(6(4) - 5\).'),
            },
            r'Gõ thẳng `4(3x - 5) + 7 = 5x + 15` vào Desmos để đọc đường thẳng đứng `x = 4`, sau đó gõ `6(4) - 5` ra ngay `19`.'
        ),
        math_mcq(
            'sat_mm7_m1_q2', 2, 'Algebra', 'Linear functions', 'Easy',
            r'<p>An electric harbor ferry begins its morning shift with a fully charged battery. The remaining battery energy \(E(d)\), in kilowatt-hours (kWh), after the ferry travels \(d\) nautical miles is modeled by the linear function:</p><p style="text-align:center;">\[E(d) = 480 - 18d\]</p>',
            r'Which of the following is the best interpretation of the number \(18\) in this context?',
            {
                'A': r'The ferry consumes \(18\) kWh of battery energy for each nautical mile traveled.',
                'B': r'The ferry starts its morning shift with \(18\) kWh of battery energy.',
                'C': r'The ferry can travel a maximum of \(18\) nautical miles on a single charge.',
                'D': r'The battery requires \(18\) minutes to recharge after each nautical mile.',
            },
            'A',
            r'Trong hàm bậc nhất \(E(d) = 480 - 18d\), tung độ gốc \(480\) là năng lượng pin ban đầu (khi \(d = 0\)), còn hệ số góc \(-18\) cho biết mỗi khi quãng đường \(d\) tăng thêm 1 hải lý (nautical mile), lượng điện còn lại giảm đi đúng \(18\text{ kWh}\) (tức phà tiêu thụ \(18\text{ kWh}\) mỗi hải lý).',
            r'Trong mô hình giảm tuyến tính \(y = b - mx\), giá trị \(m\) luôn biểu thị lượng tiêu thụ/giảm đi cho MỖI đơn vị tăng thêm của biến độc lập.',
            {
                'A': ('Đáp án đúng', r'Mô tả chính xác tốc độ tiêu thụ \(18\text{ kWh}\) cho mỗi hải lý.'),
                'B': ('Nhầm với y-intercept', r'Dung lượng pin ban đầu là \(480\text{ kWh}\), không phải \(18\text{ kWh}\).'),
                'C': ('Nhầm với x-intercept', r'Quãng đường tối đa là \(480 / 18 \approx 26.7\) hải lý, không phải \(18\).'),
                'D': ('Sai đơn vị thời gian', r'Phương trình không chứa biến phút (minutes) hay tốc độ sạc.'),
            },
            r'Câu đọc hiểu ý nghĩa hệ số góc: đối chiếu trực tiếp với `y = b + m*x` mà không cần bấm máy.'
        ),
        math_mcq(
            'sat_mm7_m1_q3', 3, 'Algebra', 'Linear functions', 'Easy',
            tbl_q3 + r'<p>The table above shows selected values of the linear function \(g\), which models the hourly nutrient solution recirculation flow \(g(x)\), in liters per hour, for a vertical hydroponic tower with \(x\) tiers.</p>',
            r'What is the value of \(g(15)\)?',
            {'A': r'\(76\)', 'B': r'\(86\)', 'C': r'\(90\)', 'D': r'\(94\)'},
            'D',
            r'Hệ số góc của hàm tuyến tính là \(m = \frac{46 - 22}{7 - 3} = \frac{24}{4} = 6\). Từ \(x = 11\) lên \(x = 15\) tăng thêm đúng \(4\) tầng (cùng bước nhảy \(+4\) như bảng), nên lưu lượng tăng thêm \(24\text{ L/hr}\): \(g(15) = 70 + 24 = 94\). (Hoặc viết \(g(x) = 6x + 4 \Rightarrow g(15) = 6(15) + 4 = 94\)).',
            r'Khi \(x\) tăng các bước đều nhau (\(+4\)), giá trị \(g(x)\) cũng tăng đúng một khoảng cố định (\(+24\)): \(70 + 24 = 94\) trong 3 giây!',
            {
                'A': ('Cộng sai bước nhảy', r'Chỉ cộng thêm hệ số góc \(6\) thay vì \(6 \times 4 = 24\).'),
                'B': ('Nhầm tung độ gốc âm', r'Tính \(6(15) - 4 = 86\) do sai dấu \(b\).'),
                'C': ('Quên tung độ gốc b = 4', r'Chỉ tính \(6 \times 15 = 90\) mà bỏ sót hằng số cố định \(+4\).'),
                'D': ('Đáp án đúng', r'\(g(15) = 6(15) + 4 = 94\).'),
            },
            r'Nhập Table `x1 = [3, 7, 11]`, `y1 = [22, 46, 70]` vào Desmos → gõ `y1 ~ m x1 + b` → gõ `m(15) + b` ra ngay `94`.'
        ),
        math_mcq(
            'sat_mm7_m1_q4', 4, 'Algebra', 'Systems of two linear equations in two variables', 'Medium',
            r'<p>A bronze sculpture foundry balances two alloy crucible charges \(x\) and \(y\) (in kilograms) using the system of linear equations below:</p><p style="text-align:center;">\[\begin{cases} 5x + 3y = 47 \\ 2x - y = 10 \end{cases}\]</p>',
            r'What is the value of \(3x - 2y\)?',
            {'A': r'\(11\)', 'B': r'\(13\)', 'C': r'\(15\)', 'D': r'\(29\)'},
            'B',
            r'Từ phương trình thứ hai: \(y = 2x - 10\). Thế vào phương trình thứ nhất: \(5x + 3(2x - 10) = 47 \Rightarrow 11x - 30 = 47 \Rightarrow 11x = 77 \Rightarrow x = 7\). Suy ra \(y = 2(7) - 10 = 4\). Khi đó \(3x - 2y = 3(7) - 2(4) = 21 - 8 = 13\).',
            r'Rút \(y = 2x - 10\) rồi thế hoặc vẽ giao điểm hai đường thẳng trên Desmos để chốt \((7, 4)\) không sai dấu!',
            {
                'A': ('Tính x + y', r'\(7 + 4 = 11\), không phải biểu thức \(3x - 2y\).'),
                'B': ('Đáp án đúng', r'\(3(7) - 2(4) = 21 - 8 = 13\).'),
                'C': ('Sai phép nhân 2y', r'Tính nhầm \(3(7) - 6 = 15\).'),
                'D': ('Cộng thay vì trừ', r'Tính \(3(7) + 2(4) = 29\) thay vì \(3(7) - 2(4)\).'),
            },
            r'Gõ `5x + 3y = 47` và `2x - y = 10` vào Desmos → bấm chấm giao điểm `(7, 4)` → tính `3(7) - 2(4) = 13`.'
        ),
        math_spr(
            'sat_mm7_m1_q5', 5, 'Algebra', 'Systems of two linear equations in two variables', 'Medium',
            r'<p>Consider the system of linear equations below, where \(k\) is a constant:</p><p style="text-align:center;">\[\begin{cases} 8x - 6y = 21 \\ kx + 15y = 35 \end{cases}\]</p>',
            r'If the system has <b>no solution</b>, what is the value of \(k\)?',
            ['-20'], '-20',
            r'Hệ phương trình bậc nhất vô nghiệm khi hai đường thẳng song song (tỉ lệ hệ số của \(x\) và \(y\) bằng nhau nhưng khác tỉ lệ hằng số): \(\frac{k}{8} = \frac{15}{-6} = -\frac{5}{2} \Rightarrow k = 8 \cdot \left(-\frac{5}{2}\right) = -20\). Kiểm tra tỉ lệ hằng số: \(\frac{35}{21} = \frac{5}{3} \neq -\frac{5}{2}\), xác nhận hai đường song song hoàn toàn (vô nghiệm).',
            r'Điều kiện vô nghiệm: \(\frac{a_1}{a_2} = \frac{b_1}{b_2} \neq \frac{c_1}{c_2}\) — luôn giữ chặt dấu âm của \(-6y\)!',
            r'Gõ `8x - 6y = 21` và `kx + 15y = 35` trên Desmos, thêm slider `k` từ `-30` đến `30` → tại `k = -20`, hai đường song song tuyệt đối!'
        ),
        math_mcq(
            'sat_mm7_m1_q6', 6, 'Algebra', 'Linear equations in two variables', 'Medium',
            r'<p>In a coordinate model of an Olympic velodrome training zone, line \(r\) is defined by the equation \(4x - 7y = 28\). Line \(s\) is <b>perpendicular</b> to line \(r\) and passes through the point \((4, -2)\).</p>',
            r'Which of the following is an equation of line \(s\)?',
            {
                'A': r'\(y = -\frac{7}{4}x + 5\)',
                'B': r'\(y = \frac{7}{4}x - 9\)',
                'C': r'\(y = \frac{4}{7}x - \frac{30}{7}\)',
                'D': r'\(y = -\frac{4}{7}x + \frac{2}{7}\)',
            },
            'A',
            r'Đổi đường \(r\) sang dạng \(y = mx + b\): \(7y = 4x - 28 \Rightarrow y = \frac{4}{7}x - 4\), nên hệ số góc \(m_r = \frac{4}{7}\). Đường vuông góc \(s\) có hệ số góc nghịch đảo đổi dấu: \(m_s = -\frac{7}{4}\). Thay điểm \((4, -2)\) vào \(y = -\frac{7}{4}x + b\): \(-2 = -\frac{7}{4}(4) + b = -7 + b \Rightarrow b = 5\). Vậy \(y = -\frac{7}{4}x + 5\).',
            r'Vuông góc \(\Rightarrow\) nghịch đảo VÀ đổi dấu hệ số góc: \(+\frac{4}{7} \to -\frac{7}{4}\).',
            {
                'A': ('Đáp án đúng', r'Slope \(-\frac{7}{4}\) và thay \(x = 4\) cho \(y = -7 + 5 = -2\).'),
                'B': ('Quên đổi dấu slope', r'Nghịch đảo thành \(\frac{7}{4}\) nhưng giữ nguyên dấu dương.'),
                'C': ('Song song thay vì vuông góc', r'Giữ nguyên hệ số góc \(\frac{4}{7}\) của đường song song.'),
                'D': ('Quên nghịch đảo phân số', r'Chỉ đổi dấu thành \(-\frac{4}{7}\) mà chưa lật ngược tử mẫu.'),
            },
            r'Vẽ `4x - 7y = 28`, chấm điểm `(4, -2)` và nhập phương án A trên Desmos để xác nhận cắt vuông góc và đi qua đúng `(4, -2)`.'
        ),
        math_mcq(
            'sat_mm7_m1_q7', 7, 'Algebra', 'Linear inequalities in one or two variables', 'Medium',
            r'<p>An electric ferry cargo deck has a maximum payload capacity of \(3{,}120\) kilograms. It is loaded with \(x\) battery supply pallets weighing \(75\) kilograms each and \(y\) mail crates weighing \(50\) kilograms each.</p>',
            r'If \(22\) battery supply pallets are already loaded, what is the <b>maximum</b> number of mail crates that can be added without exceeding the payload capacity?',
            {'A': r'\(28\)', 'B': r'\(30\)', 'C': r'\(29\)', 'D': r'\(62\)'},
            'C',
            r'Thiết lập bất phương trình tải trọng: \(75x + 50y \le 3{,}120\). Thay \(x = 22\): \(75(22) + 50y \le 3{,}120 \Rightarrow 1{,}650 + 50y \le 3{,}120 \Rightarrow 50y \le 1{,}470 \Rightarrow y \le 29.4\). Vì số thùng hàng \(y\) phải là số nguyên không vượt quá \(29.4\), giá trị lớn nhất là \(29\).',
            r'Khi giới hạn "không vượt quá" ra số thập phân \(y \le 29.4\), PHẢI làm tròn XUỐNG thành \(29\) (nếu lên 30 sẽ quá tải \(3{,}150\text{ kg}\))!',
            {
                'A': ('Thấp hơn mức tối đa', r'28 thùng vẫn còn dư \(70\text{ kg}\), đủ thêm 1 thùng 50 kg nữa.'),
                'B': ('Làm tròn lên gây quá tải', r'30 thùng làm tổng tải lên \(3{,}150\text{ kg} > 3{,}120\text{ kg}\).'),
                'C': ('Đáp án đúng', r'\(y \le 29.4 \Rightarrow y_{\max} = 29\) (tổng tải \(3{,}100\text{ kg}\)).'),
                'D': ('Quên trừ khối lượng pallets', r'Lấy thẳng \(3{,}120 / 50 = 62.4 \to 62\) mà quên \(22\) pallet đã chất sẵn.'),
            },
            r'Gõ `(3120 - 75*22) / 50` trên Desmos ra `29.4` → lấy phần nguyên lớn nhất là `29`.'
        ),
        math_mcq(
            'sat_mm7_m1_q8', 8, 'Algebra', 'Systems of two linear equations in two variables', 'Medium-Hard',
            r'<p>In a pharmaceutical formulation lab, two dosage coefficients \(a\) and \(b\) satisfy the system of equations below:</p><p style="text-align:center;">\[\begin{cases} 7a + 4b = 58 \\ 2a + 5b = 41 \end{cases}\]</p>',
            r'What is the value of \(3a + 3b\)?',
            {'A': r'\(11\)', 'B': r'\(19\)', 'C': r'\(27\)', 'D': r'\(33\)'},
            'D',
            r'Mẹo cộng vế theo vế hai phương trình: \((7a + 2a) + (4b + 5b) = 58 + 41 \Rightarrow 9a + 9b = 99\). Chia cả hai vế cho \(3\) ta thu được ngay \(3a + 3b = 33\) (không cần giải lẻ phân số \(a = \frac{14}{3}, b = \frac{19}{3}\)!).',
            r'Trước khi giải từng ẩn \(a, b\), hãy thử cộng hoặc trừ 2 phương trình xem có ra đúng bội số của biểu thức cần tìm (\(9a + 9b \to 3a + 3b\)) không!',
            {
                'A': ('Bẫy dừng ở a + b', r'\(11\) là giá trị của \(a + b\), quên nhân 3 để tính \(3a + 3b\).'),
                'B': ('Trừ 2 phương trình rồi đoán sai', r'Tính \(58 - 41 = 17\) hoặc làm tròn nhầm \(a, b\).'),
                'C': ('Chia sai 99 cho 3', r'Nhầm \(99 / 3 = 27\) thay vì \(33\).'),
                'D': ('Đáp án đúng', r'\(9a + 9b = 99 \Rightarrow 3a + 3b = 33\).'),
            },
            r'Gõ `7x + 4y = 58` và `2x + 5y = 41` trên Desmos → đọc giao điểm `(4.667, 6.333)` → tính `3*(4.6667 + 6.3333) = 33`.'
        ),
        math_spr(
            'sat_mm7_m1_q9', 9, 'Advanced Math', 'Nonlinear functions', 'Medium',
            svg_q9 + r'<p>The graph of the quadratic function \(y = f(x)\) in the \(xy\)-plane has its vertex at \((5, -4)\) and passes through the point \((8, 14)\), as shown above.</p>',
            r'What is the value of \(f(9)\)?',
            ['28'], '28',
            r'Viết phương trình dạng đỉnh (Vertex Form): \(f(x) = a(x - 5)^2 - 4\). Thay điểm \((8, 14)\): \(a(8 - 5)^2 - 4 = 14 \Rightarrow 9a = 18 \Rightarrow a = 2\). Vậy \(f(x) = 2(x - 5)^2 - 4\). Thay \(x = 9\): \(f(9) = 2(9 - 5)^2 - 4 = 2(16) - 4 = 28\).',
            r'Biết đỉnh \((h, k)\) là chốt ngay Vertex Form \(f(x) = a(x - h)^2 + k\), dùng điểm thứ hai tìm \(a\) rồi thay \(x = 9\)!',
            r'Gõ `f(x) = a(x - 5)^2 - 4`, tìm `a` sao cho `f(8) = 14` (`a = 2`), rồi gõ `f(9)` trên Desmos ra ngay `28`.'
        ),
        math_mcq(
            'sat_mm7_m1_q10', 10, 'Advanced Math', 'Nonlinear equations in one variable and systems of equations in two variables', 'Medium',
            r'<p>Consider the quadratic equation below, where \(c\) is a constant:</p><p style="text-align:center;">\[3x^2 - 18x + c = 0\]</p>',
            r'If the equation has <b>exactly one real solution</b>, what is the value of \(c\)?',
            {'A': r'\(9\)', 'B': r'\(27\)', 'C': r'\(36\)', 'D': r'\(81\)'},
            'B',
            r'Phương trình bậc hai có đúng 1 nghiệm thực khi biệt thức \(\Delta = b^2 - 4ac = 0\). Thay \(a = 3, b = -18\): \((-18)^2 - 4(3)c = 0 \Rightarrow 324 - 12c = 0 \Rightarrow c = \frac{324}{12} = 27\).',
            r'Đúng 1 nghiệm thực \(\Leftrightarrow \Delta = b^2 - 4ac = 0\) (nhớ nhân đủ hệ số \(a = 3\) trong \(4ac\)!).',
            {
                'A': ('Nhầm (b/2a)² chưa nhân a', r'Lấy \((-18 / 6)^2 = 9\) mà quên nhân lại với \(a = 3\).'),
                'B': ('Đáp án đúng', r'\(324 - 12c = 0 \Rightarrow c = 27\).'),
                'C': ('Chia sai 324 cho 12', r'Chia nhầm \(324 / 9 = 36\) thay vì chia \(12\).'),
                'D': ('Quên hệ số a = 3 trong 4ac', r'Giải nhầm \(324 - 4c = 0 \Rightarrow c = 81\).'),
            },
            r'Gõ `y = 3x^2 - 18x + c` vào Desmos, thêm slider `c` (khoảng `0` đến `50`) → tại `c = 27`, đỉnh parabol chạm đúng trục Ox tại `(3, 0)`!'
        ),
        math_mcq(
            'sat_mm7_m1_q11', 11, 'Advanced Math', 'Equivalent expressions', 'Medium',
            r'<p>Consider the rational expression below for all values \(x > 4\):</p><p style="text-align:center;">\[\frac{x^2 - 16}{x^2 + 7x + 12}\]</p>',
            r'Which of the following is equivalent to the given expression?',
            {
                'A': r'\(\frac{x + 4}{x + 3}\)',
                'B': r'\(\frac{x - 4}{x - 3}\)',
                'C': r'\(-\frac{4}{3}\)',
                'D': r'\(\frac{x - 4}{x + 3}\)',
            },
            'D',
            r'Phân tích nhân tử cả tử và mẫu: \(x^2 - 16 = (x - 4)(x + 4)\), và \(x^2 + 7x + 12 = (x + 3)(x + 4)\). Với \(x > 4\), rút gọn nhân tử chung \((x + 4) \neq 0\) ta được \(\frac{x - 4}{x + 3}\).',
            r'Gặp phân thức bậc hai, phân tích nhân tử rồi rút gọn; hoặc thay nhanh 1 số cụ thể (như \(x = 5\)) để đối chiếu 4 phương án!',
            {
                'A': ('Rút gọn nhầm (x - 4)', r'Giữ lại \((x + 4)\) thay vì \((x - 4)\) trên tử.'),
                'B': ('Sai dấu ở mẫu số', r'Phân tích sai \(x^2 + 7x + 12\) thành có dấu trừ \((x - 3)\).'),
                'C': ('Triệt tiêu x² sai quy tắc', r'Cắt ngang \(x^2\) trên tử và mẫu (lỗi đại số kinh điển!).'),
                'D': ('Đáp án đúng', r'\(\frac{(x - 4)(x + 4)}{(x + 3)(x + 4)} = \frac{x - 4}{x + 3}\).'),
            },
            r'Vẽ `y = (x^2 - 16)/(x^2 + 7x + 12)` và nhập từng phương án trên Desmos — chỉ đồ thị D trùng khít hoàn toàn với đồ thị gốc!'
        ),
        math_mcq(
            'sat_mm7_m1_q12', 12, 'Advanced Math', 'Nonlinear functions', 'Medium',
            r'<p>In a pharmacokinetic study, a patient receives a \(640\)-milligram intravenous dose of an antibiotic. The mass \(M(t)\), in milligrams, of the antibiotic remaining in the patient’s bloodstream \(t\) hours after administration is modeled by:</p><p style="text-align:center;">\[M(t) = 640\left(\frac{1}{2}\right)^{\frac{t}{4}}\]</p>',
            r'According to the model, how many milligrams of the antibiotic remain in the bloodstream \(12\) hours after administration?',
            {'A': r'\(80\)', 'B': r'\(160\)', 'C': r'\(40\)', 'D': r'\(213\)'},
            'A',
            r'Thay \(t = 12\) vào mô hình bán rã: số chu kỳ bán rã là \(\frac{12}{4} = 3\). Lượng thuốc còn lại: \(M(12) = 640 \cdot \left(\frac{1}{2}\right)^3 = 640 \cdot \frac{1}{8} = 80\text{ mg}\).',
            r'Với hàm bán rã \(\left(\frac{1}{2}\right)^{t/h}\), luôn tính số lần chia đôi \(n = t / h\) rồi chia \(2^n\)!',
            {
                'A': ('Đáp án đúng', r'\(12 / 4 = 3\) chu kỳ \(\Rightarrow 640 / 2^3 = 80\text{ mg}\).'),
                'B': ('Chỉ chia đôi 2 lần', r'Tính \(640 / 4 = 160\) (nhầm số chu kỳ thành 2 hoặc chia thẳng cho 4).'),
                'C': ('Chia đôi dư 1 chu kỳ', r'Tính \(640 / 16 = 40\) (nhầm 4 chu kỳ bán rã).'),
                'D': ('Chia thẳng cho 3', r'Tính tuyến tính \(640 / 3 \approx 213\) thay vì chia \(2^3 = 8\).'),
            },
            r'Gõ thẳng `640 * (1/2)^(12/4)` vào Desmos ra ngay `80`.'
        ),
        math_spr(
            'sat_mm7_m1_q13', 13, 'Advanced Math', 'Nonlinear equations in one variable and systems of equations in two variables', 'Medium-Hard',
            r'<p>Consider the quadratic equation below:</p><p style="text-align:center;">\[4x^2 - 26x + 15 = 0\]</p>',
            r'What is the <b>sum</b> of the solutions to the given equation?',
            ['13/2', '6.5'], '13/2 (hoặc 6.5)',
            r'Kiểm tra biệt thức \(\Delta = (-26)^2 - 4(4)(15) = 676 - 240 = 436 > 0\), nên phương trình có 2 nghiệm thực phân biệt. Theo định lý Vieta, tổng hai nghiệm bằng \(-\frac{b}{a} = -\frac{-26}{4} = \frac{26}{4} = \frac{13}{2} = 6.5\).',
            r'Đề hỏi TỔNG các nghiệm bậc hai \(\Rightarrow\) dùng ngay Vieta \(x_1 + x_2 = -\frac{b}{a}\) (nhớ chia cho \(a = 4\) và rút gọn phân số!).',
            r'Gõ `y = 4x^2 - 26x + 15` trên Desmos → bấm 2 giao điểm trục Ox (`0.640` và `5.860`) → cộng lại đúng `6.5`, hoặc bấm thẳng `26/4` ra `6.5` (`13/2`)!'
        ),
        math_mcq(
            'sat_mm7_m1_q14', 14, 'Advanced Math', 'Nonlinear equations in one variable and systems of equations in two variables', 'Medium-Hard',
            r'<p>Consider the radical equation below:</p><p style="text-align:center;">\[\sqrt{5x + 24} = x + 2\]</p>',
            r'Which of the following gives all real solutions to the given equation?',
            {
                'A': r'\(-4\) only',
                'B': r'\(-4\) and \(5\)',
                'C': r'\(5\) only',
                'D': r'There is no real solution.',
            },
            'C',
            r'Điều kiện vế phải không âm: \(x + 2 \ge 0 \Rightarrow x \ge -2\). Bình phương hai vế: \(5x + 24 = (x + 2)^2 = x^2 + 4x + 4 \Rightarrow x^2 - x - 20 = 0 \Rightarrow (x - 5)(x + 4) = 0 \Rightarrow x = 5\) hoặc \(x = -4\). Thử lại vào phương trình gốc: với \(x = 5\), \(\sqrt{49} = 7 = 5 + 2\) (thỏa mãn); với \(x = -4\), \(\sqrt{4} = 2 \neq -2\) (nghiệm ngoại lai, LOẠI!). Vậy chỉ có \(x = 5\).',
            r'MỌI phương trình căn bậc hai sau khi bình phương BẮT BUỘC phải thử nghiệm lại vào phương trình gốc để loại nghiệm ngoại lai!',
            {
                'A': ('Chọn nhầm nghiệm ngoại lai', r'Tại \(x = -4\), vế trái bằng \(+2\) còn vế phải bằng \(-2\).'),
                'B': ('Quên loại nghiệm ngoại lai', r'\(-4\) không thỏa mãn vì căn số học không bao giờ ra giá trị âm.'),
                'C': ('Đáp án đúng', r'Chỉ có \(x = 5\) thỏa mãn phương trình gốc.'),
                'D': ('Loại nhầm cả x = 5', r'Thay \(x = 5\) cho \(\sqrt{49} = 7\), hoàn toàn hợp lệ.'),
            },
            r'Vẽ `y = sqrt(5x + 24)` và `y = x + 2` trên Desmos → hai đồ thị chỉ cắt nhau tại ĐÚNG 1 điểm `(5, 7)` → chọn `5 only`!'
        ),
        math_mcq(
            'sat_mm7_m1_q15', 15, 'Advanced Math', 'Nonlinear functions', 'Medium-Hard',
            r'<p>In the \(xy\)-plane, the function \(f\) is defined by \(f(x) = x^2 - 6x + 14\). The function \(g\) is defined by \(g(x) = f(x + 2) - 9\).</p>',
            r'What are the coordinates of the <b>vertex</b> of the graph of \(y = g(x)\) in the \(xy\)-plane?',
            {
                'A': r'\((5, -4)\)',
                'B': r'\((1, -4)\)',
                'C': r'\((1, 14)\)',
                'D': r'\((-1, -4)\)',
            },
            'B',
            r'Hoàn thành bình phương \(f(x)\): \(f(x) = (x^2 - 6x + 9) + 5 = (x - 3)^2 + 5\), nên đỉnh của \(f\) là \((3, 5)\). Phép biến đổi \(g(x) = f(x + 2) - 9\) dịch đồ thị sang <b>TRÁI 2 đơn vị</b> (trừ 2 vào hoành độ) và <b>XUỐNG DƯỚI 9 đơn vị</b> (trừ 9 vào tung độ). Đỉnh mới của \(g\) là \((3 - 2,\; 5 - 9) = (1, -4)\).',
            r'Quy tắc dịch chuyển hàm: \(f(x + h)\) dịch sang TRÁI \(h\) đơn vị (ngược dấu trong ngoặc!), còn \(-k\) bên ngoài dịch XUỐNG \(k\) đơn vị (cùng dấu!).',
            {
                'A': ('Dịch nhầm sang phải (+2)', r'Cộng nhầm \(3 + 2 = 5\) thay vì dịch trái \(3 - 2 = 1\).'),
                'B': ('Đáp án đúng', r'Đỉnh \((3, 5) \xrightarrow{(-2,\; -9)} (1, -4)\).'),
                'C': ('Dịch nhầm lên trên (+9)', r'Cộng \(5 + 9 = 14\) thay vì trừ \(9\).'),
                'D': ('Nhầm dấu đỉnh ban đầu', r'Nhầm hoành độ đỉnh của \(f\) thành \(-3\) hoặc trừ sai.'),
            },
            r'Gõ `f(x) = x^2 - 6x + 14` và `g(x) = f(x + 2) - 9` vào Desmos → bấm trực tiếp vào đỉnh của đường `g(x)` đọc ngay `(1, -4)`!'
        ),
        math_spr(
            'sat_mm7_m1_q16', 16, 'Problem-Solving and Data Analysis', 'Ratios, rates, proportional relationships, and units', 'Medium',
            r'<p>A vertical hydroponic farm installs a rectangular high-pressure misting panel with an area of \(1{,}296\) square inches. (\(1\text{ foot} = 12\text{ inches}\))</p>',
            r'What is the area of the misting panel, in <b>square feet</b>?',
            ['9'], '9',
            r'Vì \(1\text{ foot} = 12\text{ inches}\), đơn vị diện tích phải bình phương tỉ số đổi: \(1\text{ ft}^2 = 12^2 = 144\text{ in}^2\). Diện tích tấm phun sương theo feet vuông là: \(\frac{1{,}296}{144} = 9\text{ ft}^2\).',
            r'Đổi đơn vị DIỆN TÍCH (square units) luôn chia/nhân với BÌNH PHƯƠNG hệ số (\(12^2 = 144\), tuyệt đối không chia cho 12!).',
            r'Gõ `1296 / 12^2` trên Desmos ra ngay `9`.'
        ),
        math_mcq(
            'sat_mm7_m1_q17', 17, 'Problem-Solving and Data Analysis', 'Probability and conditional probability', 'Medium',
            tbl_q17 + r'<p>The table above summarizes \(200\) scheduled electric ferry departures recorded across three maritime routes during one month.</p>',
            r'If one departure from the <b>Island Express</b> route is selected at random, what is the probability that it was <b>delayed</b>?',
            {
                'A': r'\(\frac{27}{200}\)',
                'B': r'\(\frac{27}{50}\)',
                'C': r'\(\frac{7}{10}\)',
                'D': r'\(\frac{3}{10}\)',
            },
            'D',
            r'Đây là xác suất có điều kiện: không gian mẫu bị thu hẹp chỉ trong hàng <b>Island Express</b> với tổng số \(90\) chuyến. Trong \(90\) chuyến này có \(27\) chuyến bị trễ (Delayed). Vậy xác suất cần tìm là \(\frac{27}{90} = \frac{3}{10}\).',
            r'Gặp cụm "If one [group] is selected at random", mẫu số PHẢI là tổng của đúng nhóm đó (\(90\)), không lấy tổng toàn bảng (\(200\))!',
            {
                'A': ('Dùng tổng toàn bảng 200', r'\(\frac{27}{200}\) là xác suất chọn từ cả 3 tuyến, không có điều kiện Island Express.'),
                'B': ('Đảo điều kiện sang cột Delayed', r'\(\frac{27}{50}\) là xác suất thuộc Island Express biết rằng chuyến bị trễ.'),
                'C': ('Tính nhầm On-Time thay vì Delayed', r'\(\frac{63}{90} = \frac{7}{10}\) là xác suất ĐÚNG GIỜ của Island Express.'),
                'D': ('Đáp án đúng', r'\(\frac{27}{90} = \frac{3}{10}\).'),
            },
            r'Gõ `27/90` trên Desmos rồi bấm biểu tượng phân số ở bên trái ra ngay `3/10`.'
        ),
        math_mcq(
            'sat_mm7_m1_q18', 18, 'Problem-Solving and Data Analysis', 'Two-variable data: Models and scatterplots', 'Medium',
            tbl_q18 + r'<p>The table above shows four wind-tunnel measurements of a velodrome cyclist’s aerodynamic power output \(y\), in watts, at track speed \(x\), in kilometers per hour. A line of best fit for the data is given by the equation \(y = 24.5x - 620\).</p>',
            r'At a track speed of \(48\) km/h, by how many watts does the value <b>predicted</b> by the line of best fit exceed the <b>actual</b> measured power output?',
            {'A': r'\(6\)', 'B': r'\(12\)', 'C': r'\(24.5\)', 'D': r'\(556\)'},
            'A',
            r'Tính giá trị dự đoán (predicted value) tại \(x = 48\) từ đường hồi quy: \(\hat{y} = 24.5(48) - 620 = 1{,}176 - 620 = 556\text{ watts}\). Trong bảng, giá trị đo thực tế (actual value) tại \(x = 48\) là \(550\text{ watts}\). Độ chênh lệch (predicted minus actual) là: \(556 - 550 = 6\text{ watts}\).',
            r'Residual = chênh lệch giữa giá trị thực tế trong bảng và giá trị thay vào phương trình đường thẳng (line of best fit).',
            {
                'A': ('Đáp án đúng', r'Dự đoán \(556\) lớn hơn thực tế \(550\) đúng \(6\text{ watts}\).'),
                'B': ('Sai phép nhân 24.5 × 48', r'Tính nhầm giá trị dự đoán hoặc nhân đôi độ lệch.'),
                'C': ('Nhầm với hệ số góc', r'\(24.5\) là hệ số góc của đường hồi quy, không phải sai số tại \(x = 48\).'),
                'D': ('Dừng ở giá trị dự đoán', r'\(556\) là giá trị dự đoán \(\hat{y}\), quên trừ đi giá trị thực tế \(550\).'),
            },
            r'Gõ `(24.5 * 48 - 620) - 550` vào Desmos ra ngay `6`.'
        ),
        math_spr(
            'sat_mm7_m1_q19', 19, 'Problem-Solving and Data Analysis', 'Percentages', 'Medium-Hard',
            r'<p>During a bronze foundry alloy density test, three metal ingots—Sample A, Sample B, and Sample C—are weighed. The mass of Sample A is \(125\%\) of the mass of Sample B, and the mass of Sample C is \(36\%\) of the mass of Sample A.</p>',
            r'If the mass of Sample C is \(p\%\) of the mass of Sample B, what is the value of \(p\)?',
            ['45'], '45',
            r'Đặt khối lượng Sample B bằng \(100\). Khi đó: Sample A \(= 125\% \times 100 = 125\), và Sample C \(= 36\% \times 125 = 0.36 \times 125 = 45\). Vì Sample B \(= 100\), Sample C bằng đúng \(45\%\) của Sample B \(\Rightarrow p = 45\).',
            r'Với chuỗi phần trăm liên tiếp, đặt đại lượng mốc cuối cùng bằng \(100\) để tính thẳng ra kết quả phần trăm \(p\)!',
            r'Gõ `1.25 * 0.36 * 100` trên Desmos ra ngay `45`.'
        ),
        math_mcq(
            'sat_mm7_m1_q20', 20, 'Geometry and Trigonometry', 'Lines, angles, and triangles', 'Medium',
            svg_q20 + r'<p>In the diagram of an electric ferry navigation channel above, parallel lane boundary lines \(\ell\) and \(m\) are intersected by a straight crossing path (transversal).</p>',
            r'What is the measure, in degrees, of an <b>acute</b> angle formed by the intersection of the transversal and line \(m\)?',
            {'A': r'\(17\)', 'B': r'\(77\)', 'C': r'\(103\)', 'D': r'\(127\)'},
            'B',
            r'Hai góc \((5x + 18)^\circ\) và \((7x - 16)^\circ\) là hai góc so le ngoài (alternate exterior angles) tạo bởi đường cắt hai đường thẳng song song nên bằng nhau: \(5x + 18 = 7x - 16 \Rightarrow 2x = 34 \Rightarrow x = 17\). Số đo mỗi góc tù được ghi nhãn là \(5(17) + 18 = 103^\circ\). Do góc nhọn và góc tù kề bù nhau trên đường thẳng \(m\), góc nhọn cần tìm bằng \(180^\circ - 103^\circ = 77^\circ\).',
            r'Hai đường song song bị cắt chỉ tạo ra 2 số đo góc bù nhau: giải ra góc tù \(103^\circ\) rồi nhớ đọc kỹ đề hỏi góc NHỌN (\(180^\circ - 103^\circ = 77^\circ\))!',
            {
                'A': ('Bẫy dừng ở x', r'\(17\) chỉ là giá trị của \(x\), chưa phải số đo góc.'),
                'B': ('Đáp án đúng', r'Góc tù \(= 103^\circ \Rightarrow\) góc nhọn \(= 180^\circ - 103^\circ = 77^\circ\).'),
                'C': ('Nhầm góc tù thay vì góc nhọn', r'\(103^\circ > 90^\circ\) là góc tù, còn đề yêu cầu tìm góc nhọn (acute angle).'),
                'D': ('Cộng/trừ sai 180°', r'Sai số học khi tính bù góc hoặc giải sai \(x\).'),
            },
            r'Gõ `5x + 18 = 7x - 16` trên Desmos ra `x = 17`, sau đó tính `180 - (5*17 + 18) = 77`.'
        ),
        math_mcq(
            'sat_mm7_m1_q21', 21, 'Geometry and Trigonometry', 'Circles', 'Medium-Hard',
            svg_q21 + r'<p>The figure above represents a circular curved apron of an Olympic velodrome with center \(O\), radius \(OA = 24\) meters, and central angle \(\angle AOB = 75^\circ\).</p>',
            r'What is the <b>area</b>, in square meters, of the shaded sector \(OAB\)?',
            {
                'A': r'\(10\pi\)',
                'B': r'\(60\pi\)',
                'C': r'\(120\pi\)',
                'D': r'\(576\pi\)',
            },
            'C',
            r'Diện tích hình quạt tròn tỉ lệ thuận với góc ở tâm: \(A_{\text{sector}} = \frac{75^\circ}{360^\circ} \cdot \pi r^2 = \frac{5}{24} \cdot \pi (24)^2 = \frac{5}{24} \cdot 576\pi = 5 \cdot 24\pi = 120\pi\text{ m}^2\).',
            r'Ghi nhớ cặp công thức quạt tròn: Diện tích \(= \frac{\theta}{360^\circ}\pi r^2\) (khác với Độ dài cung \(= \frac{\theta}{360^\circ}2\pi r\))!',
            {
                'A': ('Bẫy tính độ dài cung', r'\(10\pi\) là độ dài cung \(AB\), không phải diện tích hình quạt.'),
                'B': ('Chia đôi nhầm công thức', r'Lấy \(\frac{1}{2}\) diện tích quạt ra \(60\pi\).'),
                'C': ('Đáp án đúng', r'\(\frac{75}{360} \times 576\pi = 120\pi\).'),
                'D': ('Diện tích cả hình tròn', r'\(576\pi\) là diện tích toàn phần hình tròn \(360^\circ\), quên nhân tỉ lệ \(\frac{75}{360}\).'),
            },
            r'Gõ `(75 / 360) * 24^2` trên Desmos ra ngay `120` → đáp án `120π`.'
        ),
        math_spr(
            'sat_mm7_m1_q22', 22, 'Geometry and Trigonometry', 'Right triangles and trigonometry', 'Medium-Hard',
            svg_q22 + r'<p>A structural support truss for an Olympic velodrome banking ramp forms right triangle \(ABC\) shown above, where \(\angle B = 90^\circ\), hypotenuse \(AC = 51\) feet, and \(\sin(A) = \frac{8}{17}\).</p>',
            r'What is the length, in feet, of side \(AB\)?',
            ['45'], '45',
            r'Trong tam giác vuông \(ABC\), \(\sin(A) = \frac{\text{đối}}{\text{huyền}} = \frac{BC}{AC} = \frac{8}{17}\). Vì \(AC = 51 = 17 \times 3\), suy ra cạnh đối \(BC = 8 \times 3 = 24\). Áp dụng định lý Pythagoras (hoặc bộ ba \(8\text{–}15\text{–}17\) nhân 3): \(AB = \sqrt{51^2 - 24^2} = \sqrt{2{,}601 - 576} = \sqrt{2{,}025} = 45\).',
            r'Nhận diện bộ ba Pythagoras \(8\text{–}15\text{–}17\) nhân hệ số \(3\) cho ra ngay tam giác \(24\text{–}45\text{–}51\) cực nhanh!',
            r'Tính `BC = 51 * (8/17) = 24`, sau đó gõ `sqrt(51^2 - 24^2)` trên Desmos ra ngay `45`.'
        ),
    ]
