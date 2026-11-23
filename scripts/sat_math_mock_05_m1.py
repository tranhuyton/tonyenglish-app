# -*- coding: utf-8 -*-
"""
Digital SAT Math Adaptive Mock Test #5 — Module 1 (Routing Module, 22 Questions)
Themes: Wind Turbines & Tidal Power Grids, Optical Lens Labs, Specialty Coffee Roasting, Alpine Suspension Bridges, Glass Atrium Architecture.
Blueprint: 8 Algebra (Q1-Q8), 7 Advanced Math (Q9-Q15), 4 PSDA (Q16-Q19), 3 Geometry/Trig (Q20-Q22).
Format: 16 MCQ (A:4, B:4, C:4, D:4) + 6 SPR (Q5, Q9, Q13, Q16, Q19, Q22).
"""

from fractions import Fraction
import math
from sat_math_helpers import (
    math_mcq, math_spr, build_math_table,
    svg_parallel_transversal, svg_right_triangle
)

def verify_math():
    assert 4 * (3 * 5 - 5) - 2 * 5 == 30 and 3 * 5 + 4 == 19
    m3 = Fraction(34 - 14, 8 - 3)
    b3 = 14 - m3 * 3
    assert m3 == 4 and b3 == 2 and m3 * 12 + b3 == 50
    assert 2 * 8 + 5 * 5 == 41 and 8 - 2 * 5 == -2 and 8 + 5 == 13
    assert Fraction(20, 8) == Fraction(-15, -6) == Fraction(50, 20) == Fraction(5, 2)
    assert Fraction(2, 7) * Fraction(-7, 2) == -1 and Fraction(-7, 2) * 4 + 11 == -3
    assert 12 * 95 + 11 * 65 <= 1900 and 12 * 95 + 12 * 65 > 1900
    x8, y8 = Fraction(43, 9), Fraction(4, 9)
    assert 5 * x8 - 2 * y8 == 23 and 3 * x8 + 6 * y8 == 17 and 4 * x8 + 2 * y8 == 20
    assert 3 * (4 - 7) ** 2 + 12 == 39 and 3 * (10 - 7) ** 2 + 12 == 39 and 3 * (9 - 7) ** 2 + 12 == 24
    assert 18 ** 2 - 4 * 3 * 27 == 0
    assert Fraction(25 - 16, 25 - 35 + 12) == Fraction(5 + 4, 5 - 3)
    assert (-20) ** 2 - 4 * 4 * 15 > 0 and Fraction(15, 4) == Fraction(375, 100)
    assert 2 * abs(12 - 5) - 6 == 8 and 2 * abs(-2 - 5) - 6 == 8 and 12 + (-2) == 10
    assert (-2 + 6, -9 + 4) == (4, -5)
    assert Fraction(432, 144) == 3
    assert Fraction(35, 50) == Fraction(7, 10)
    assert Fraction(120, 100) * Fraction(85, 100) == Fraction(102, 100)
    assert 4 * 23 - 10 == 2 * 23 + 36 == 82 and 180 - 82 == 98
    assert 15 + 9 + 25 == 49 and int(math.sqrt(49)) == 7
    assert 24 ** 2 + 45 ** 2 == 51 ** 2 and Fraction(24, 51) == Fraction(8, 17)

def get_m1_questions():
    tbl_q17 = build_math_table(
        ['Origin', 'Grade A Lots', 'Grade B Lots', 'Total'],
        [
            ['Ethiopia', '28', '12', '40'],
            ['Colombia', '35', '15', '50'],
            ['Sumatra', '17', '13', '30'],
            ['Total', '80', '40', '120'],
        ],
        caption='Specialty Coffee Roasting Quality Audit'
    )
    svg_q20 = svg_parallel_transversal('p', 'q', ang1_lbl='(4x − 10)°', ang2_lbl='(2x + 36)°', ang3_lbl='w°')
    svg_q22 = svg_right_triangle('AB', 'BC', '51', angle_top_left='A', v_top='A', v_right_angle='B', v_right='C', note='cos(A) = 8/17')

    return [
        math_mcq(
            'sat_mm5_m1_q1', 1, 'Algebra', 'Linear equations in one variable', 'Easy',
            r'<p>Consider the linear equation shown below:</p><p style="text-align:center;">\[4(3x - 5) - 2x = 30\]</p>',
            r'What is the value of \(3x + 4\)?',
            {'A': r'\(19\)', 'B': r'\(5\)', 'C': r'\(15\)', 'D': r'\(23\)'},
            'A',
            r'Khai triển: \(12x - 20 - 2x = 30 \Rightarrow 10x = 50 \Rightarrow x = 5\). Thay vào biểu thức cần tìm: \(3(5) + 4 = 19\).',
            r'Giải ra \(x = 5\) xong phải thay tiếp vào \(3x + 4\) — đừng dừng sớm ở \(x\).',
            {
                'A': ('Đáp án đúng', r'\(x = 5 \Rightarrow 3(5) + 4 = 19\).'),
                'B': ('Dừng ở x', r'5 chỉ là nghiệm \(x\), chưa tính \(3x + 4\).'),
                'C': ('Quên cộng 4', r'Chỉ tính \(3x = 15\).'),
                'D': ('Sai hệ số 10x', r'Nhầm \(12x + 2x\) hoặc cộng sai.'),
            },
            r'Gõ `4(3x - 5) - 2x = 30` trên Desmos ra đường thẳng đứng `x = 5`, rồi tính `3(5) + 4 = 19`.'
        ),
        math_mcq(
            'sat_mm5_m1_q2', 2, 'Algebra', 'Linear functions', 'Easy',
            r'<p>A coastal wind utility calculates a community turbine’s monthly revenue \(R(w)\), in dollars, from delivering \(w\) megawatt-hours of electricity using \(R(w) = 45w + 620\).</p>',
            r'Which of the following is the best interpretation of \(620\) in this context?',
            {
                'A': r'The revenue earned for each additional megawatt-hour delivered',
                'B': r'The fixed monthly grid-readiness payment, in dollars, received even if \(0\) megawatt-hours are delivered',
                'C': r'The maximum monthly output of the turbine, in megawatt-hours',
                'D': r'The total revenue earned when \(45\) megawatt-hours are delivered',
            },
            'B',
            r'Tại \(w = 0\), \(R(0) = 620\) dollars — đây là khoản cố định hàng tháng (y-intercept) bất kể sản lượng điện giao lưới.',
            r'Hằng số \(b\) trong \(R(w) = mw + b\) luôn biểu thị giá trị cố định ban đầu tại biến đầu vào bằng 0.',
            {
                'A': ('Nhầm với slope', r'Doanh thu mỗi MWh tăng thêm là $45, không phải $620.'),
                'B': ('Đáp án đúng', r'$620 là khoản cố định khi \(w = 0\).'),
                'C': ('Sai đơn vị', r'620 tính bằng dollars, không phải MWh.'),
                'D': ('Sai ý nghĩa', r'Khi \(w = 45\), tổng doanh thu là \(45(45) + 620 = 2{,}645\).'),
            },
            r'Thay `w = 0` vào `45(0) + 620 = 620` để thấy ngay ý nghĩa tung độ gốc.'
        ),
        math_mcq(
            'sat_mm5_m1_q3', 3, 'Algebra', 'Linear functions', 'Easy',
            r'<p>For a linear function \(f\), \(f(3) = 14\) and \(f(8) = 34\).</p>',
            r'What is the value of \(f(12)\)?',
            {'A': r'\(46\)', 'B': r'\(48\)', 'C': r'\(50\)', 'D': r'\(54\)'},
            'C',
            r'Hệ số góc \(m = \frac{34 - 14}{8 - 3} = \frac{20}{5} = 4\). Khi \(x\) tăng từ 8 lên 12 (+4 đơn vị), giá trị tăng thêm \(4 \times 4 = 16 \Rightarrow f(12) = 34 + 16 = 50\).',
            r'Tính slope \(m = 4\) rồi cộng trực tiếp \(m \cdot \Delta x = 4(12 - 8) = 16\) vào \(f(8) = 34\).',
            {
                'A': ('Nhầm bước nhảy', r'Cộng nhầm 12 thay vì 16.'),
                'B': ('Quên tung độ gốc b = 2', r'Tính \(4(12) = 48\) mà quên \(b = 2\).'),
                'C': ('Đáp án đúng', r'\(f(x) = 4x + 2 \Rightarrow f(12) = 50\).'),
                'D': ('Cộng bước nhảy cũ +20', r'Lấy \(34 + 20 = 54\) (dùng sai bước \(\Delta x = 5\) thay vì 4).'),
            },
            r'Nhập Table `x1=[3,8], y1=[14,34]` → `y1 ~ m x1 + b` → `4(12) + 2 = 50`.'
        ),
        math_mcq(
            'sat_mm5_m1_q4', 4, 'Algebra', 'Systems of two linear equations in two variables', 'Medium',
            r'<p>A coffee roastery tracks bean batch weights \(x\) and \(y\), in kilograms, using the system:</p><p style="text-align:center;">\[\begin{cases} 2x + 5y = 41 \\ x - 2y = -2 \end{cases}\]</p>',
            r'What is the value of \(x + y\)?',
            {'A': r'\(8\)', 'B': r'\(10\)', 'C': r'\(11\)', 'D': r'\(13\)'},
            'D',
            r'Từ phương trình hai: \(x = 2y - 2\). Thế vào phương trình đầu: \(2(2y - 2) + 5y = 41 \Rightarrow 9y = 45 \Rightarrow y = 5 \Rightarrow x = 8\). Tổng \(x + y = 8 + 5 = 13\).',
            r'Thế nhanh \(x = 2y - 2\) hoặc vẽ giao điểm trên Desmos đọc thẳng \((8, 5)\).',
            {
                'A': ('Chỉ lấy x', r'8 chỉ là giá trị của \(x\).'),
                'B': ('Tính 2y', r'10 chỉ là \(2y\).'),
                'C': ('Sai dấu -2', r'Nhầm \(x = 2y + 2\) dẫn tới nghiệm sai.'),
                'D': ('Đáp án đúng', r'\(x = 8, y = 5 \Rightarrow x + y = 13\).'),
            },
            r'Gõ `2x + 5y = 41` và `x - 2y = -2` trên Desmos → bấm giao điểm `(8, 5)` → `8 + 5 = 13`.'
        ),
        math_spr(
            'sat_mm5_m1_q5', 5, 'Algebra', 'Systems of two linear equations in two variables', 'Medium',
            r'<p>In the system of linear equations below, \(k\) is a constant:</p><p style="text-align:center;">\[\begin{cases} 8x - 6y = 20 \\ kx - 15y = 50 \end{cases}\]</p>',
            r'If the system has <b>infinitely many solutions</b>, what is the value of \(k\)?',
            ['20'], '20',
            r'Để hệ có vô số nghiệm, tỉ số hệ số phải bằng nhau: \(\frac{k}{8} = \frac{-15}{-6} = \frac{50}{20} = \frac{5}{2} \Rightarrow k = 8 \cdot \frac{5}{2} = 20\).',
            r'Vô số nghiệm \(\Leftrightarrow \frac{a_1}{a_2} = \frac{b_1}{b_2} = \frac{c_1}{c_2}\) — so cặp hằng số \(50/20 = 2.5\) rồi nhân \(8 \times 2.5 = 20\)!',
            r'Gõ hai phương trình vào Desmos với slider `k` → tại `k = 20` hai đường trùng khít hoàn toàn.'
        ),
        math_mcq(
            'sat_mm5_m1_q6', 6, 'Algebra', 'Linear equations in two variables', 'Medium',
            r'<p>In the \(xy\)-plane, line \(r\) is defined by \(2x - 7y = 14\). Line \(s\) is perpendicular to line \(r\) and passes through \((4, -3)\).</p>',
            r'Which of the following is an equation of line \(s\)?',
            {
                'A': r'\(y = -\frac{7}{2}x + 11\)',
                'B': r'\(y = \frac{7}{2}x - 17\)',
                'C': r'\(y = -\frac{2}{7}x - \frac{13}{7}\)',
                'D': r'\(y = \frac{2}{7}x - \frac{29}{7}\)',
            },
            'A',
            r'Đường \(r\) có slope \(m_1 = \frac{2}{7}\). Đường vuông góc \(s\) có slope \(m_2 = -\frac{7}{2}\). Thay \((4, -3)\) vào \(y = -\frac{7}{2}x + b\): \(-3 = -14 + b \Rightarrow b = 11\). Vậy \(y = -\frac{7}{2}x + 11\).',
            r'Slope đường vuông góc = nghịch đảo ĐỔI DẤU: \(\frac{2}{7} \to -\frac{7}{2}\).',
            {
                'A': ('Đáp án đúng', r'Slope \(-\frac{7}{2}\) và đi qua \((4, -3)\) vì \(-\frac{7}{2}(4) + 11 = -3\).'),
                'B': ('Quên đổi dấu slope', r'Dùng \(+\frac{7}{2}\) thay vì \(-\frac{7}{2}\).'),
                'C': ('Quên nghịch đảo', r'Dùng \(-\frac{2}{7}\) mà không đảo phân số.'),
                'D': ('Song song thay vì vuông góc', r'Giữ nguyên slope \(\frac{2}{7}\).'),
            },
            r'Vẽ `2x - 7y = 14`, điểm `(4, -3)` và kiểm tra đường A trên Desmos.'
        ),
        math_mcq(
            'sat_mm5_m1_q7', 7, 'Algebra', 'Linear inequalities in one or two variables', 'Medium',
            r'<p>An optical laboratory has a budget of $1,900 to order standard lenses at $65 each and precision coated lenses at $95 each. The lab orders \(12\) precision coated lenses.</p>',
            r'What is the <b>maximum</b> number of standard lenses the lab can order without exceeding its budget?',
            {'A': r'\(10\)', 'B': r'\(11\)', 'C': r'\(12\)', 'D': r'\(29\)'},
            'B',
            r'Chi phí 12 thấu kính phủ đặc biệt: \(12 \times 95 = \$1{,}140\). Ngân sách còn lại: \(1{,}900 - 1{,}140 = \$760\). Số thấu kính chuẩn tối đa: \(65x \le 760 \Rightarrow x \le 11.69\). Vì \(x\) là số nguyên không vượt ngân sách, \(x_{\max} = 11\).',
            r'Khi ràng buộc là \(\le 11.69\), luôn lấy phần nguyên dưới (\(11\)), KHÔNG làm tròn lên \(12\)!',
            {
                'A': ('Còn dư tiền mua thêm', r'Mua 10 chiếc tốn $1,790, vẫn còn $110 đủ mua thêm 1 chiếc nữa.'),
                'B': ('Đáp án đúng', r'\(11 \times 65 + 12 \times 95 = \$1{,}855 \le \$1{,}900\).'),
                'C': ('Bẫy làm tròn lên', r'Mua 12 chiếc tốn $1,920 > $1,900 (vượt ngân sách!).'),
                'D': ('Quên trừ 12 thấu kính đắt', r'Chia thẳng \(1900 / 65 = 29.2\).'),
            },
            r'Gõ `(1900 - 12*95)/65` trên Desmos ra `11.692` → chọn số nguyên lớn nhất là `11`.'
        ),
        math_mcq(
            'sat_mm5_m1_q8', 8, 'Algebra', 'Systems of two linear equations in two variables', 'Medium-Hard',
            r'<p>In the system below, \((x, y)\) is the solution:</p><p style="text-align:center;">\[\begin{cases} 5x - 2y = 23 \\ 3x + 6y = 17 \end{cases}\]</p>',
            r'What is the value of \(4x + 2y\)?',
            {'A': r'\(10\)', 'B': r'\(16\)', 'C': r'\(20\)', 'D': r'\(40\)'},
            'C',
            r'Cộng thẳng hai phương trình: \((5x + 3x) + (-2y + 6y) = 23 + 17 \Rightarrow 8x + 4y = 40\). Chia cả hai vế cho 2: \(4x + 2y = 20\)!',
            r'Cộng vế theo vế ra \(8x + 4y = 40\), chia đôi ra ngay \(4x + 2y = 20\) trong 3 giây mà không cần giải phân số!',
            {
                'A': ('Chia 4 nhầm', r'10 là giá trị của \(2x + y\).'),
                'B': ('Tính sai tổng vế phải', r'Cộng nhầm 23 + 17.'),
                'C': ('Đáp án đúng', r'\(8x + 4y = 40 \Rightarrow 4x + 2y = 20\).'),
                'D': ('Quên chia 2', r'40 là giá trị của \(8x + 4y\), không phải \(4x + 2y\).'),
            },
            r'Vẽ hai đường thẳng trên Desmos thấy giao điểm `(4.778, 0.444)` → `4(4.778) + 2(0.444) = 20`.'
        ),
        math_spr(
            'sat_mm5_m1_q9', 9, 'Advanced Math', 'Nonlinear functions', 'Medium-Hard',
            r'<p>The height \(h(x)\), in meters, of a parabolic suspension bridge cable above the roadway is modeled by \(h(x) = a(x - d)^2 + 12\), where \(12\) is the minimum height of the cable. Given that \(h(4) = 39\) and \(h(10) = 39\).</p>',
            r'What is the value of \(h(9)\)?',
            ['24'], '24',
            r'Vì \(h(4) = h(10) = 39\), trục đối xứng đi qua trung điểm \(d = \frac{4 + 10}{2} = 7\). Thay \(h(4) = 39\): \(a(4 - 7)^2 + 12 = 39 \Rightarrow 9a = 27 \Rightarrow a = 3\). Vậy \(h(9) = 3(9 - 7)^2 + 12 = 3(4) + 12 = 24\).',
            r'Hai điểm cùng tung độ cho ngay hoành độ đỉnh \(d = \frac{4 + 10}{2} = 7\)!',
            r'Nhập 3 điểm `(4, 39)`, `(7, 12)`, `(10, 39)` vào Table Desmos → `y1 ~ a(x1 - 7)^2 + 12` → `a = 3`, tính `3(9-7)^2 + 12 = 24`.'
        ),
        math_mcq(
            'sat_mm5_m1_q10', 10, 'Advanced Math', 'Nonlinear equations in one variable and systems of equations in two variables', 'Medium',
            r'<p>Consider the quadratic equation below, where \(c\) is a constant:</p><p style="text-align:center;">\[3x^2 + 18x + c = 0\]</p>',
            r'If the equation has <b>exactly one real solution</b>, what is the value of \(c\)?',
            {'A': r'\(9\)', 'B': r'\(18\)', 'C': r'\(81\)', 'D': r'\(27\)'},
            'D',
            r'Đúng 1 nghiệm thực \(\Leftrightarrow \Delta = b^2 - 4ac = 0 \Rightarrow 18^2 - 4(3)(c) = 0 \Rightarrow 324 - 12c = 0 \Rightarrow c = 27\).',
            r'Rút 3 ra ngoài: \(3(x^2 + 6x + c/3) = 0 \Rightarrow c/3 = (6/2)^2 = 9 \Rightarrow c = 27\)!',
            {
                'A': ('Quên nhân hệ số a = 3', r'9 chỉ là \(c/3\).'),
                'B': ('Lấy thẳng hệ số b', r'18 là hệ số \(b\), không phải \(c\).'),
                'C': ('Quên chia cho a = 3', r'Tính \(18^2 / 4 = 81\) mà quên nhân 3 dưới mẫu.'),
                'D': ('Đáp án đúng', r'\(324 / 12 = 27\).'),
            },
            r'Vẽ `y = 3x^2 + 18x + c` với slider `c` trên Desmos → đỉnh vừa chạm trục Ox tại `c = 27`.'
        ),
        math_mcq(
            'sat_mm5_m1_q11', 11, 'Advanced Math', 'Equivalent expressions', 'Medium',
            r'<p>Consider the rational expression below for all \(x > 4\):</p><p style="text-align:center;">\[\frac{x^2 - 16}{x^2 - 7x + 12}\]</p>',
            r'Which expression is equivalent to the given fraction?',
            {
                'A': r'\(\frac{x + 4}{x - 3}\)',
                'B': r'\(\frac{x - 4}{x - 3}\)',
                'C': r'\(\frac{x + 4}{x + 3}\)',
                'D': r'\(\frac{-16}{-7x + 12}\)',
            },
            'A',
            r'Phân tích nhân tử: \(\frac{(x - 4)(x + 4)}{(x - 4)(x - 3)}\). Với \(x > 4\), rút gọn \((x - 4)\) còn \(\frac{x + 4}{x - 3}\).',
            r'Nhận diện hiệu hai bình phương ở tử và phân tích tam thức bậc hai ở mẫu.',
            {
                'A': ('Đáp án đúng', r'Triệt tiêu chuẩn nhân tử chung \((x - 4)\).'),
                'B': ('Rút gọn sai dấu tử', r'Giữ lại \((x - 4)\) thay vì \((x + 4)\).'),
                'C': ('Phân tích sai dấu mẫu', r'\(x^2 - 7x + 12 = (x-4)(x-3)\), không phải \((x+3)\).'),
                'D': ('Gạch tắt x² sai đại số', r'Không được rút gọn số hạng trong tổng/hiệu.'),
            },
            r'Thử `x = 5`: `(25 - 16)/(25 - 35 + 12) = 9/2 = 4.5`. Chỉ phương án A cho `(5+4)/(5-3) = 4.5`!'
        ),
        math_mcq(
            'sat_mm5_m1_q12', 12, 'Advanced Math', 'Nonlinear functions', 'Easy',
            r'<p>A tidal power bank increases its stored capacity \(E(t)\), in megawatt-hours, after \(t\) months according to \(E(t) = 350(1.09)^t\).</p>',
            r'According to the model, how does the stored capacity change each month?',
            {
                'A': r'It increases by \(1.09\) megawatt-hours each month.',
                'B': r'It increases by \(9\%\) each month.',
                'C': r'It increases by \(109\%\) each month.',
                'D': r'It decreases by \(9\%\) each month.',
            },
            'B',
            r'Cơ số \(1.09 = 1 + 0.09\), biểu thị mức tăng trưởng mũ \(9\%\) mỗi tháng.',
            r'Trong \(a(1 + r)^t\), tốc độ tăng phần trăm mỗi chu kỳ là \((b - 1) \times 100\% = 9\%\).',
            {
                'A': ('Nhầm tăng tuyến tính', r'Mô hình là hàm mũ, không phải cộng 1.09 MWh mỗi tháng.'),
                'B': ('Đáp án đúng', r'\(1.09 - 1 = 0.09 = 9\%\) tăng mỗi tháng.'),
                'C': ('Quên trừ 100% gốc', r'109% là tổng giá trị mới so với tháng trước, mức TĂNG chỉ là 9%.'),
                'D': ('Nhầm tăng thành giảm', r'Cơ số \(1.09 > 1\) là tăng trưởng.'),
            },
            r'So `E(1)/E(0) = 1.09` → tăng `9%` mỗi tháng.'
        ),
        math_spr(
            'sat_mm5_m1_q13', 13, 'Advanced Math', 'Nonlinear equations in one variable and systems of equations in two variables', 'Medium-Hard',
            r'<p>Consider the quadratic equation below:</p><p style="text-align:center;">\[4x^2 - 20x + 15 = 0\]</p>',
            r'What is the <b>product</b> of the solutions to the given equation?',
            ['15/4', '3.75'], '15/4 hoặc 3.75',
            r'Kiểm tra \(\Delta = (-20)^2 - 4(4)(15) = 400 - 240 = 160 > 0\) (có 2 nghiệm thực phân biệt). Theo Vieta, tích hai nghiệm bằng \(\frac{c}{a} = \frac{15}{4} = 3.75\).',
            r'Tích nghiệm của \(ax^2 + bx + c = 0\) bằng \(\frac{c}{a}\) — đừng quên chia cho \(a = 4\)!',
            r'Vẽ `y = 4x^2 - 20x + 15` trên Desmos, nhân 2 nghiệm `0.919 * 4.081 = 3.75` (`15/4`).'
        ),
        math_mcq(
            'sat_mm5_m1_q14', 14, 'Advanced Math', 'Nonlinear equations in one variable and systems of equations in two variables', 'Medium-Hard',
            r'<p>Consider the absolute value equation below:</p><p style="text-align:center;">\[2|x - 5| - 6 = 8\]</p>',
            r'What is the <b>sum</b> of all solutions to this equation?',
            {'A': r'\(5\)', 'B': r'\(7\)', 'C': r'\(10\)', 'D': r'\(14\)'},
            'C',
            r'Cô lập trị tuyệt đối: \(2|x - 5| = 14 \Rightarrow |x - 5| = 7 \Rightarrow x - 5 = 7\) hoặc \(x - 5 = -7 \Rightarrow x = 12\) hoặc \(x = -2\). Tổng hai nghiệm là \(12 + (-2) = 10\).',
            r'Hai nghiệm của \(|x - c| = d\) (với \(d > 0\)) luôn đối xứng quanh \(c\), nên tổng 2 nghiệm luôn bằng \(2c = 10\)!',
            {
                'A': ('Chỉ lấy tâm đối xứng', r'5 là trung bình cộng 2 nghiệm, tổng là \(2 \times 5 = 10\).'),
                'B': ('Nhầm với vế phải 7', r'7 là khoảng cách từ tâm tới mỗi nghiệm.'),
                'C': ('Đáp án đúng', r'\(12 + (-2) = 10\).'),
                'D': ('Cộng hai giá trị tuyệt đối', r'Lấy \(|12| + |-2| = 14\) thay vì cộng đại số.'),
            },
            r'Vẽ `y = 2|x - 5| - 6` và `y = 8` trên Desmos → 2 giao điểm tại `x = -2` và `x = 12` → tổng là `10`.'
        ),
        math_mcq(
            'sat_mm5_m1_q15', 15, 'Advanced Math', 'Nonlinear functions', 'Medium-Hard',
            r'<p>The function \(f\) is defined by \(f(x) = (x + 2)^2 - 9\), and \(g(x) = f(x - 6) + 4\).</p>',
            r'What are the coordinates of the vertex of the graph of \(y = g(x)\)?',
            {'A': r'\((-8, -5)\)', 'B': r'\((4, -13)\)', 'C': r'\((-8, -13)\)', 'D': r'\((4, -5)\)'},
            'D',
            r'Đỉnh của \(f\) là \((-2, -9)\). Hàm \(g(x) = f(x - 6) + 4\) dịch sang <b>phải 6</b> (\(-2 + 6 = 4\)) và <b>lên 4</b> (\(-9 + 4 = -5\)). Đỉnh mới: \((4, -5)\).',
            r'Nhớ dấu trong ngoặc ngược chiều: \((x - 6)\) dịch sang PHẢI +6!',
            {
                'A': ('Dịch trái thay vì phải', r'Lấy \(-2 - 6 = -8\).'),
                'B': ('Dịch xuống thay vì lên', r'Lấy \(-9 - 4 = -13\).'),
                'C': ('Dịch ngược cả 2 trục', r'Trừ cả 6 lẫn 4.'),
                'D': ('Đáp án đúng', r'\((-2 + 6, -9 + 4) = (4, -5)\).'),
            },
            r'Gõ `f(x) = (x+2)^2 - 9` và `g(x) = f(x-6) + 4` trên Desmos → bấm đáy `g` đọc `(4, -5)`.'
        ),
        math_spr(
            'sat_mm5_m1_q16', 16, 'Problem-Solving and Data Analysis', 'Ratios, rates, proportional relationships, and units', 'Medium',
            r'<p>An architectural glass skylight prism has a base area of \(432\) square inches. (\(1\text{ foot} = 12\text{ inches}\))</p>',
            r'What is the base area of the skylight prism, in <b>square feet</b>?',
            ['3'], '3',
            r'Vì \(1\text{ ft}^2 = 12^2 = 144\text{ in}^2\), diện tích bằng \(\frac{432}{144} = 3\text{ ft}^2\).',
            r'Đổi diện tích luôn chia cho bình phương hệ số (\(12^2 = 144\)), không chia 12!',
            r'Gõ `432 / 12^2` trên Desmos ra ngay `3`.'
        ),
        math_mcq(
            'sat_mm5_m1_q17', 17, 'Problem-Solving and Data Analysis', 'Probability and conditional probability', 'Medium',
            tbl_q17 + r'<p>The table above categorizes \(120\) specialty coffee bean lots roasted during one quarter by origin and quality grade.</p>',
            r'If a lot from <b>Colombia</b> is chosen at random, what is the probability that it received <b>Grade A</b>?',
            {'A': r'\(\frac{7}{10}\)', 'B': r'\(\frac{7}{24}\)', 'C': r'\(\frac{7}{16}\)', 'D': r'\(\frac{3}{10}\)'},
            'A',
            r'Điều kiện chọn từ nhóm <b>Colombia</b> thu gọn mẫu số xuống tổng hàng Colombia = \(50\). Số lô Grade A của Colombia là \(35\). Xác suất: \(\frac{35}{50} = \frac{7}{10}\).',
            r'Xác suất có điều kiện "If a lot from Colombia..." lấy mẫu số bằng đúng tổng nhóm Colombia (50).',
            {
                'A': ('Đáp án đúng', r'\(\frac{35}{50} = \frac{7}{10}\).'),
                'B': ('Chia tổng toàn bảng 120', r'\(\frac{35}{120} = \frac{7}{24}\) quên giới hạn điều kiện.'),
                'C': ('Chia tổng cột Grade A (80)', r'\(\frac{35}{80} = \frac{7}{16}\) bị đảo ngược điều kiện.'),
                'D': ('Tính xác suất Grade B', r'\(\frac{15}{50} = \frac{3}{10}\) là Grade B.'),
            },
            r'Gõ `35 / 50` trên Desmos rồi bấm nút phân số ra `7/10`.'
        ),
        math_mcq(
            'sat_mm5_m1_q18', 18, 'Problem-Solving and Data Analysis', 'One-variable data: Distributions and measures of center and spread', 'Medium',
            r'<p>Seven optical calibration measurements, in microns, are recorded below:</p><p style="text-align:center;">\[18,\; 20,\; 21,\; 22,\; 23,\; 24,\; 98\]</p><p>The outlier value \(98\) was caused by a sensor glitch and is removed from the data set.</p>',
            r'How are the mean and standard deviation affected when \(98\) is removed?',
            {
                'A': r'The mean decreases, and the standard deviation increases.',
                'B': r'Both the mean and the standard deviation decrease.',
                'C': r'The mean remains unchanged, and the standard deviation decreases.',
                'D': r'Both the mean and the standard deviation remain unchanged.',
            },
            'B',
            r'Xóa bỏ giá trị ngoại lai cực lớn \(98\) kéo giá trị trung bình (Mean) giảm mạnh (từ \(32.3\) xuống \(21.3\)) và làm các điểm còn lại co cụm sát nhau nên độ lệch chuẩn (Standard Deviation) cũng giảm rất mạnh!',
            r'Xóa một outlier cực trị LUÔN làm Standard Deviation giảm mạnh và kéo Mean ngược về phía phần dữ liệu còn lại.',
            {
                'A': ('Ngược chiều SD', r'Bỏ outlier làm dữ liệu ít phân tán hơn → SD phải GIẢM.'),
                'B': ('Đáp án đúng', r'Cả Mean lẫn Standard Deviation đều giảm rõ rệt.'),
                'C': ('Nhầm Mean với Median', r'Mean rất nhạy với outlier nên chắc chắn giảm mạnh.'),
                'D': ('Sai hoàn toàn', r'Xóa 98 thay đổi mạnh cả tâm lẫn độ phân tán.'),
            },
            r'So `mean`/`stdev` của `[18,20,21,22,23,24,98]` với `[18,20,21,22,23,24]` trên Desmos để xác nhận tức thì.'
        ),
        math_spr(
            'sat_mm5_m1_q19', 19, 'Problem-Solving and Data Analysis', 'Percentages', 'Medium-Hard',
            r'<p>A wholesale coffee roaster raises the price of its signature blend by \(20\%\) in January, and then reduces the new price by \(15\%\) in March.</p>',
            r'The final price in March is \(p\%\) greater than the original price before January. What is the value of \(p\)?',
            ['2'], '2',
            r'Nhân liên tiếp hai hệ số phần trăm: \(1.20 \times 0.85 = 1.02\). So với giá gốc \(1.00\), giá cuối cùng tăng ròng \(0.02 = 2\% \Rightarrow p = 2\).',
            r'Phần trăm tăng giảm liên tiếp luôn NHÂN hệ số \((1.20)(0.85) = 1.02\), không lấy \(20 - 15 = 5\)!',
            r'Gõ `(1.20 * 0.85 - 1) * 100` trên Desmos ra ngay `2`.'
        ),
        math_mcq(
            'sat_mm5_m1_q20', 20, 'Geometry and Trigonometry', 'Lines, angles, and triangles', 'Medium',
            svg_q20 + r'<p>In the figure above, parallel lines \(p\) and \(q\) are intersected by a transversal.</p>',
            r'What is the value of \(w\)?',
            {'A': r'\(23\)', 'B': r'\(82\)', 'C': r'\(98\)', 'D': r'\(108\)'},
            'C',
            r'Hai góc đồng vị (nhọn) bằng nhau: \(4x - 10 = 2x + 36 \Rightarrow 2x = 46 \Rightarrow x = 23\). Góc nhọn bằng \(4(23) - 10 = 82^\circ\). Góc \(w^\circ\) là góc tù bù với góc nhọn nên \(w = 180 - 82 = 98\).',
            r'Tìm góc nhọn \(82^\circ\) xong phải kiểm tra vị trí góc \(w^\circ\) là góc tù (\(180 - 82 = 98\))!',
            {
                'A': ('Dừng ở x', r'23 mới chỉ là giá trị của \(x\).'),
                'B': ('Nhầm góc nhọn vs tù', r'\(82^\circ\) là góc nhọn, còn \(w^\circ\) là góc tù bù với nó.'),
                'C': ('Đáp án đúng', r'\(180 - 82 = 98\).'),
                'D': ('Trừ nhầm 180 - 82', r'Sai phép trừ hàng chục.'),
            },
            r'Gõ `4x - 10 = 2x + 36` trên Desmos ra `x = 23`, rồi tính `180 - (4*23 - 10) = 98`.'
        ),
        math_mcq(
            'sat_mm5_m1_q21', 21, 'Geometry and Trigonometry', 'Circles', 'Medium-Hard',
            r'<p>In the \(xy\)-plane, a circle has the equation \(x^2 + y^2 + 6x - 10y = 15\).</p>',
            r'What are the center and radius of the circle?',
            {
                'A': r'Center \((3, -5)\), radius \(7\)',
                'B': r'Center \((-3, 5)\), radius \(49\)',
                'C': r'Center \((-3, 5)\), radius \(\sqrt{15}\)',
                'D': r'Center \((-3, 5)\), radius \(7\)',
            },
            'D',
            r'Hoàn thành bình phương: \((x + 3)^2 + (y - 5)^2 = 15 + 3^2 + (-5)^2 = 15 + 9 + 25 = 49\). Tâm là \((-3, 5)\) và bán kính \(r = \sqrt{49} = 7\).',
            r'Nhớ đổi dấu khi đọc tâm từ \((x + 3)^2 + (y - 5)^2\) và lấy căn bậc hai vế phải \(\sqrt{49} = 7\).',
            {
                'A': ('Nhầm dấu tọa độ tâm', r'Tâm phải là \((-3, 5)\), không phải \((3, -5)\).'),
                'B': ('Quên lấy căn bán kính', r'49 là \(r^2\), không phải bán kính \(r\).'),
                'C': ('Quên cộng 9 + 25 vào vế phải', r'Chỉ lấy căn của 15.'),
                'D': ('Đáp án đúng', r'Tâm \((-3, 5)\), bán kính \(7\).'),
            },
            r'Gõ `x^2 + y^2 + 6x - 10y = 15` lên Desmos đọc ngay đỉnh/đáy tại `(-3, 12)` và `(-3, -2)` → tâm `(-3, 5)`, `r = 7`!'
        ),
        math_spr(
            'sat_mm5_m1_q22', 22, 'Geometry and Trigonometry', 'Right triangles and trigonometry', 'Medium-Hard',
            svg_q22 + r'<p>In right triangle \(ABC\) shown above, \(\angle B = 90^\circ\), hypotenuse \(AC = 51\), and \(\cos(A) = \frac{8}{17}\).</p>',
            r'What is the length of side \(BC\)?',
            ['45'], '45',
            r'\(\cos(A) = \frac{AB}{AC} = \frac{8}{17}\). Với \(AC = 51 = 17 \times 3\), suy ra \(AB = 8 \times 3 = 24\). Theo bộ ba Pythagoras \(8\text{–}15\text{–}17\) nhân 3, \(BC = 15 \times 3 = 45\) (kiểm tra \(\sqrt{51^2 - 24^2} = \sqrt{2025} = 45\)).',
            r'Bộ ba \(8\text{–}15\text{–}17\) nhân 3 ra ngay tam giác \(24\text{–}45\text{–}51\)!',
            r'Tính `AB = 51*(8/17) = 24`, sau đó gõ `sqrt(51^2 - 24^2)` trên Desmos ra ngay `45`.'
        ),
    ]
