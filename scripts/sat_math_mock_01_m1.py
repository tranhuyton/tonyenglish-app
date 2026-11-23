# -*- coding: utf-8 -*-
"""
Digital SAT Math Adaptive Mock Test #1 — Module 1 (Routing Module, 22 Questions)
Themes: Renewable Energy/Solar, Robotics/Microchips, Oceanography, Botanical Architecture, Shipping Logistics.
Blueprint: 8 Algebra (Q1-Q8), 7 Advanced Math (Q9-Q15), 4 PSDA (Q16-Q19), 3 Geometry/Trig (Q20-Q22).
Format: 16 MCQ (A:4, B:4, C:4, D:4) + 6 SPR (Q5, Q9, Q13, Q16, Q19, Q22).
"""

from fractions import Fraction
import math
from sat_math_helpers import (
    math_mcq, math_spr, build_math_table,
    svg_parallel_transversal, svg_right_triangle, svg_parabola_vertex
)

def verify_math():
    # Q1: 5(2x-3)+4 = 3x+10 => 7x=21 => x=3 => 4x-5=7
    x1 = Fraction(21, 7)
    assert 5 * (2 * x1 - 3) + 4 == 3 * x1 + 10 and 4 * x1 - 5 == 7
    # Q3: f(2)=11, f(6)=23 => m=3, b=5 => f(10)=35
    m3 = Fraction(23 - 11, 6 - 2)
    b3 = 11 - m3 * 2
    assert m3 * 10 + b3 == 35
    # Q4: 3x+2y=26, x-y=2 => x=6, y=4 => x+2y=14
    assert 3 * 6 + 2 * 4 == 26 and 6 - 4 == 2 and 6 + 2 * 4 == 14
    # Q5: 6x-4y=15, kx+10y=25 no solution => k/6 = 10/(-4) => k=-15, 25/15 != -5/2
    k5 = Fraction(6 * 10, -4)
    assert k5 == -15 and Fraction(25, 15) != Fraction(10, -4)
    # Q6: 3x+5y=15 => m=-3/5 => perp=5/3 through (3,2) => y=(5/3)x - 3
    assert Fraction(5, 3) * 3 - 3 == 2
    # Q7: 45(18) + 60y <= 2400 => 60y <= 1590 => y <= 26.5 => max int 26
    assert 45 * 18 + 60 * 26 <= 2400 and 45 * 18 + 60 * 27 > 2400
    # Q8: 4x+7y=31, 2x-y=5 => add => 6x+6y=36
    x8, y8 = Fraction(11, 3), Fraction(7, 3)
    assert 4 * x8 + 7 * y8 == 31 and 2 * x8 - y8 == 5 and 6 * x8 + 6 * y8 == 36
    # Q9: f(x)=a(x-6)^2+3, f(2)=19 => a=1 => f(9)=12
    assert 1 * (2 - 6) ** 2 + 3 == 19 and 1 * (10 - 6) ** 2 + 3 == 19 and 1 * (9 - 6) ** 2 + 3 == 12
    # Q10: 2x^2-12x+c=0 => 144-8c=0 => c=18
    assert (-12) ** 2 - 4 * 2 * 18 == 0
    # Q11: (x^2-9)/(x^2+5x+6) at x=5 => 16/56 = 2/7 == (5-3)/(5+2)
    assert Fraction(25 - 9, 25 + 25 + 6) == Fraction(5 - 3, 5 + 2)
    # Q13: 3x^2-21x+10=0 => D=321>0, sum=7
    assert (-21) ** 2 - 4 * 3 * 10 > 0 and Fraction(21, 3) == 7
    # Q14: sqrt(3x+10)=x+2 => x=2 valid, x=-3 extraneous
    assert math.isclose(math.sqrt(3 * 2 + 10), 2 + 2) and (-3 + 2) < 0
    # Q15: f(x)=x^2-2x+5 vertex (1,4), g(x)=f(x-4)+7 => vertex (5,11)
    assert (1 + 4, 4 + 7) == (5, 11)
    # Q16: 720 in^2 / 144 = 5 ft^2
    assert Fraction(720, 12 ** 2) == 5
    # Q17: 24/60 = 2/5
    assert Fraction(24, 60) == Fraction(2, 5)
    # Q19: 1.40 * 0.25 = 0.35 => 35%
    assert Fraction(140, 100) * Fraction(25, 100) == Fraction(35, 100)
    # Q20: 3x+18 = 5x-14 => x=16 => acute=66 => obtuse=114
    assert 3 * 16 + 18 == 5 * 16 - 14 == 66 and 180 - 66 == 114
    # Q21: x^2+y^2-8x+4y=16 => (x-4)^2+(y+2)^2=36 => r=6
    assert 16 + 16 + 4 == 36 and int(math.sqrt(36)) == 6
    # Q22: sin(A)=5/13, AC=39 => BC=15, AB=36
    assert 15 ** 2 + 36 ** 2 == 39 ** 2 and Fraction(15, 39) == Fraction(5, 13)

def get_m1_questions():
    tbl_q17 = build_math_table(
        ['Marine Zone', 'Coral Samples', 'Kelp Samples', 'Total'],
        [
            ['Zone A', '32', '18', '50'],
            ['Zone B', '24', '36', '60'],
            ['Zone C', '19', '21', '40'],
            ['Total', '75', '75', '150'],
        ],
        caption='Oceanographic Reef Survey Samples'
    )
    svg_q20 = svg_parallel_transversal('ℓ', 'm', ang1_lbl='(3x + 18)°', ang2_lbl='(5x − 14)°', ang3_lbl='y°')
    svg_q22 = svg_right_triangle('AB', 'BC', '39', angle_top_left='A', v_top='A', v_right_angle='B', v_right='C', note='sin(A) = 5/13')

    return [
        math_mcq(
            'sat_mm1_m1_q1', 1, 'Algebra', 'Linear equations in one variable', 'Easy',
            r'<p>Consider the linear equation shown below:</p><p style="text-align:center;font-size:18px;">\[5(2x - 3) + 4 = 3x + 10\]</p>',
            r'What is the value of \(4x - 5\)?',
            {'A': r'\(3\)', 'B': r'\(7\)', 'C': r'\(11\)', 'D': r'\(17\)'},
            'B',
            r'Khai triển vế trái: \(10x - 15 + 4 = 3x + 10 \Rightarrow 10x - 11 = 3x + 10 \Rightarrow 7x = 21 \Rightarrow x = 3\). Đề hỏi giá trị của \(4x - 5\), thay \(x = 3\) ta được \(4(3) - 5 = 7\).',
            r'Luôn gạch chân biểu thức đề thực sự hỏi (\(4x - 5\)) trước khi khoanh đáp án — tránh bẫy khoanh nhầm giá trị \(x\).',
            {
                'A': ('Bẫy giải x dừng sớm', r'\(3\) chỉ là giá trị của \(x\), chưa tính \(4x - 5\).'),
                'B': ('Đáp án đúng', r'\(x = 3 \Rightarrow 4(3) - 5 = 7\).'),
                'C': ('Sai dấu hằng số', r'Nhầm \(-15 + 4 = -19\) hoặc cộng sai khi tính \(4x - 5\).'),
                'D': ('Cộng thay vì trừ', r'Tính nhầm \(4(3) + 5 = 17\) thay vì \(4(3) - 5\).'),
            },
            r'Gõ thẳng `5(2x - 3) + 4 = 3x + 10` vào Desmos sẽ ra đường thẳng đứng tại `x = 3`, sau đó gõ `4(3) - 5` ra ngay `7`.'
        ),
        math_mcq(
            'sat_mm1_m1_q2', 2, 'Algebra', 'Linear functions', 'Easy',
            r'<p>A renewable energy contractor models the total installation cost \(C(p)\), in dollars, of a residential rooftop solar array with \(p\) panels using the linear function:</p><p style="text-align:center;">\[C(p) = 320p + 1{,}850\]</p>',
            r'Which of the following is the best interpretation of the number \(320\) in this context?',
            {
                'A': r'The cost increases by $320 for each additional solar panel installed.',
                'B': r'The fixed permit and wiring fee before any solar panels are installed is $320.',
                'C': r'A maximum of 320 solar panels can be installed on the rooftop.',
                'D': r'The total installation cost of the solar array is $320.',
            },
            'A',
            r'Trong hàm bậc nhất \(C(p) = 320p + 1{,}850\), hệ số góc (slope) \(m = 320\) biểu thị mức tăng chi phí ($320) cho mỗi tấm pin mặt trời (\(p\)) lắp thêm, còn \(1{,}850\) là chi phí cố định ban đầu (y-intercept).',
            r'Trong \(y = mx + b\), slope \(m\) luôn gắn với từ khóa "for each additional / per unit", còn \(b\) là giá trị cố định ban đầu.',
            {
                'A': ('Đáp án đúng', r'Mô tả chuẩn xác ý nghĩa hệ số góc \(m = 320\): tăng $320 cho mỗi tấm pin tăng thêm.'),
                'B': ('Nhầm với y-intercept', r'Chi phí cố định ban đầu là $1,850, không phải $320.'),
                'C': ('Hiểu sai miền xác định', r'320 là đơn giá theo tấm, không phải số lượng tấm tối đa.'),
                'D': ('Nhầm với tổng chi phí', r'$320 chỉ là chi phí biên mỗi tấm, chưa tính tổng hay phí cố định.'),
            },
            r'Câu đọc hiểu hệ số góc — không cần dùng Desmos, chỉ cần đối chiếu trực tiếp cấu trúc `y = mx + b`.'
        ),
        math_mcq(
            'sat_mm1_m1_q3', 3, 'Algebra', 'Linear functions', 'Easy',
            r'<p>For a linear function \(f\), it is given that \(f(2) = 11\) and \(f(6) = 23\).</p>',
            r'What is the value of \(f(10)\)?',
            {'A': r'\(29\)', 'B': r'\(33\)', 'C': r'\(35\)', 'D': r'\(39\)'},
            'C',
            r'Tính hệ số góc: \(m = \frac{23 - 11}{6 - 2} = \frac{12}{4} = 3\). Từ \(x = 6\) lên \(x = 10\) tăng thêm 4 đơn vị, nên \(f(10) = 23 + 3(4) = 35\). (Hoặc tìm \(f(x) = 3x + 5 \Rightarrow f(10) = 35\)).',
            r'Hàm bậc nhất có bước nhảy đều nhau: \(x\) tăng từ \(2 \to 6\) (+4) làm \(y\) tăng 12, vậy tăng tiếp \(6 \to 10\) (+4) cũng làm \(y\) tăng đúng 12: \(23 + 12 = 35\)!',
            {
                'A': ('Nhầm bước nhảy', r'Chỉ cộng thêm 6 thay vì 12.'),
                'B': ('Quên tung độ gốc', r'Tính \(3(10) + 3 = 33\) do nhầm \(b = 3\).'),
                'C': ('Đáp án đúng', r'\(f(10) = 23 + 12 = 35\).'),
                'D': ('Tính sai slope', r'Nhầm \(m = 4 \Rightarrow 23 + 16 = 39\).'),
            },
            r'Nhập bảng `x1 = [2, 6]`, `y1 = [11, 23]` rồi gõ `y1 ~ m x1 + b` trong Desmos; tính `m(10) + b` ra ngay `35`.'
        ),
        math_mcq(
            'sat_mm1_m1_q4', 4, 'Algebra', 'Systems of two linear equations in two variables', 'Medium',
            r'<p>An autonomous robotics lab calibrates two micro-actuator voltages \(x\) and \(y\) satisfying the system:</p><p style="text-align:center;">\[\begin{cases} 3x + 2y = 26 \\ x - y = 2 \end{cases}\]</p>',
            r'What is the value of \(x + 2y\)?',
            {'A': r'\(10\)', 'B': r'\(12\)', 'C': r'\(13\)', 'D': r'\(14\)'},
            'D',
            r'Từ phương trình thứ hai: \(x = y + 2\). Thế vào phương trình đầu: \(3(y + 2) + 2y = 26 \Rightarrow 5y = 20 \Rightarrow y = 4 \Rightarrow x = 6\). Khi đó \(x + 2y = 6 + 2(4) = 14\).',
            r'Thế nhanh \(x = y + 2\) hoặc vẽ giao điểm 2 đường trên Desmos để chốt \((6, 4)\) trong 5 giây.',
            {
                'A': ('Tính x + y', r'\(6 + 4 = 10\), quên nhân 2 ở \(2y\).'),
                'B': ('Tính 2x', r'\(2(6) = 12\), đọc nhầm biểu thức.'),
                'C': ('Cộng nhầm', r'Nhầm \(x = 5, y = 4 \Rightarrow 13\).'),
                'D': ('Đáp án đúng', r'\(6 + 2(4) = 14\).'),
            },
            r'Gõ hai phương trình `3x + 2y = 26` và `x - y = 2` vào Desmos → bấm chấm giao điểm `(6, 4)` → tính `6 + 2(4) = 14`.'
        ),
        math_spr(
            'sat_mm1_m1_q5', 5, 'Algebra', 'Systems of two linear equations in two variables', 'Medium',
            r'<p>Consider the system of linear equations below, where \(k\) is a constant:</p><p style="text-align:center;">\[\begin{cases} 6x - 4y = 15 \\ kx + 10y = 25 \end{cases}\]</p>',
            r'If the system has <b>no solution</b>, what is the value of \(k\)?',
            ['-15'], '-15',
            r'Hệ hai phương trình bậc nhất vô nghiệm khi hai đường thẳng song song (tỉ lệ hệ số \(x, y\) bằng nhau nhưng khác tỉ lệ hằng số): \(\frac{k}{6} = \frac{10}{-4} = -\frac{5}{2} \Rightarrow k = 6 \cdot \left(-\frac{5}{2}\right) = -15\). Kiểm tra hằng số: \(\frac{25}{15} = \frac{5}{3} \neq -\frac{5}{2}\) (thỏa mãn vô nghiệm!).',
            r'Hệ vô nghiệm \(\Leftrightarrow \frac{a_1}{a_2} = \frac{b_1}{b_2} \neq \frac{c_1}{c_2}\) — cẩn thận dấu âm ở \(-4y\)!',
            r'Gõ `6x - 4y = 15` và `kx + 10y = 25` vào Desmos, thêm slider `k` (đặt khoảng `-20` đến `20`) → kéo đến `k = -15` sẽ thấy hai đường song song hoàn hảo!'
        ),
        math_mcq(
            'sat_mm1_m1_q6', 6, 'Algebra', 'Linear equations in two variables', 'Medium',
            r'<p>In the \(xy\)-plane, line \(m\) is defined by the equation \(3x + 5y = 15\). Line \(n\) is <b>perpendicular</b> to line \(m\) and passes through the point \((3, 2)\).</p>',
            r'Which of the following is an equation of line \(n\)?',
            {
                'A': r'\(y = \frac{5}{3}x - 3\)',
                'B': r'\(y = -\frac{5}{3}x + 7\)',
                'C': r'\(y = \frac{3}{5}x + \frac{1}{5}\)',
                'D': r'\(y = -\frac{3}{5}x + \frac{19}{5}\)',
            },
            'A',
            r'Đường thẳng \(m\) có hệ số góc \(m_1 = -\frac{3}{5}\). Đường thẳng \(n\) vuông góc với \(m\) có hệ số góc nghịch đảo đổi dấu: \(m_2 = \frac{5}{3}\). Thay điểm \((3, 2)\) vào \(y = \frac{5}{3}x + b\): \(2 = \frac{5}{3}(3) + b = 5 + b \Rightarrow b = -3\). Vậy \(y = \frac{5}{3}x - 3\).',
            r'Đường vuông góc luôn lấy nghịch đảo ĐỔI DẤU của slope: \(-\frac{3}{5} \to +\frac{5}{3}\).',
            {
                'A': ('Đáp án đúng', r'Slope \(\frac{5}{3}\) và đi qua \((3, 2)\) vì \(\frac{5}{3}(3) - 3 = 2\).'),
                'B': ('Quên đổi dấu slope', r'Lấy nghịch đảo \(-\frac{5}{3}\) nhưng quên đổi từ âm sang dương.'),
                'C': ('Quên nghịch đảo', r'Chỉ đổi dấu thành \(+\frac{3}{5}\) mà không nghịch đảo phân số.'),
                'D': ('Song song thay vì vuông góc', r'Giữ nguyên slope \(-\frac{3}{5}\) của đường song song.'),
            },
            r'Vẽ `3x + 5y = 15`, điểm `(3, 2)` và thử từng phương án trên Desmos để thấy ngay phương án A cắt vuông góc và đi đúng qua `(3, 2)`.'
        ),
        math_mcq(
            'sat_mm1_m1_q7', 7, 'Algebra', 'Linear inequalities in one or two variables', 'Medium',
            r'<p>A marine cargo container has a maximum weight capacity of \(2{,}400\) kilograms. It is being loaded with \(x\) standard crates weighing \(45\) kilograms each and \(y\) heavy crates weighing \(60\) kilograms each.</p>',
            r'If the container is loaded with \(18\) standard crates, what is the <b>maximum</b> number of heavy crates that can be added without exceeding the weight capacity?',
            {'A': r'\(25\)', 'B': r'\(26\)', 'C': r'\(27\)', 'D': r'\(40\)'},
            'B',
            r'Bất phương trình tải trọng: \(45x + 60y \le 2{,}400\). Thay \(x = 18\): \(45(18) + 60y \le 2{,}400 \Rightarrow 810 + 60y \le 2{,}400 \Rightarrow 60y \le 1{,}590 \Rightarrow y \le 26.5\). Vì số thùng là số nguyên không được vượt quá tải trọng, giá trị nguyên lớn nhất là \(26\).',
            r'Với điều kiện không vượt quá (\(y \le 26.5\)), LUÔN làm tròn xuống (26), tuyệt đối không làm tròn lên 27!',
            {
                'A': ('Trừ dư 1 thùng', r'Thừa tải trọng chưa dùng hết: \(810 + 60(25) = 2310\), vẫn thêm được 1 thùng nữa.'),
                'B': ('Đáp án đúng', r'\(y \le 26.5 \Rightarrow y_{\max} = 26\) (tổng \(2{,}370 \le 2{,}400\)).'),
                'C': ('Bẫy làm tròn lên', r'Làm tròn \(26.5 \to 27\) khiến tổng khối lượng thành \(2{,}430 > 2{,}400\) (quá tải!).'),
                'D': ('Bỏ quên 18 thùng nhỏ', r'Tính \(2400 / 60 = 40\) mà quên trừ 810 kg của 18 thùng chuẩn.'),
            },
            r'Gõ `(2400 - 45*18)/60` trên Desmos ra `26.5` → lấy phần nguyên dưới là `26`.'
        ),
        math_mcq(
            'sat_mm1_m1_q8', 8, 'Algebra', 'Systems of two linear equations in two variables', 'Medium-Hard',
            r'<p>In the system of equations below, \((x, y)\) is the solution:</p><p style="text-align:center;">\[\begin{cases} 4x + 7y = 31 \\ 2x - y = 5 \end{cases}\]</p>',
            r'What is the value of \(6x + 6y\)?',
            {'A': r'\(18\)', 'B': r'\(26\)', 'C': r'\(30\)', 'D': r'\(36\)'},
            'D',
            r'Cộng vế theo vế hai phương trình trực tiếp: \((4x + 2x) + (7y - y) = 31 + 5 \Rightarrow 6x + 6y = 36\)! Không cần mất thời gian giải nghiệm phân số lẻ \(x = \frac{11}{3}, y = \frac{7}{3}\).',
            r'Trước khi giải riêng \(x, y\), luôn thử cộng hoặc trừ 2 phương trình xem có ra thẳng biểu thức đề hỏi không!',
            {
                'A': ('Chia đôi nhầm', r'Nhầm tính \(3x + 3y = 18\).'),
                'B': ('Trừ thay vì cộng', r'Lấy \(31 - 5 = 26\) thay vì cộng vế theo vế.'),
                'C': ('Tính nhầm phân số', r'Làm tròn thô nghiệm \(x \approx 3.67, y \approx 2.33\) sai số.'),
                'D': ('Đáp án đúng', r'Cộng trực tiếp hai phương trình cho ra ngay \(6x + 6y = 36\).'),
            },
            r'Cộng nhẩm 2 giây ra 36; hoặc vẽ hệ trên Desmos sẽ thấy giao điểm `(3.667, 2.333)` → `6(3.667 + 2.333) = 36`.'
        ),
        math_spr(
            'sat_mm1_m1_q9', 9, 'Advanced Math', 'Nonlinear functions', 'Medium-Hard',
            r'<p>A quadratic function \(f(x) = a(x - h)^2 + k\) achieves its minimum value of \(3\) at \(x = h\). Furthermore, \(f(2) = 19\) and \(f(10) = 19\).</p>',
            r'What is the value of \(f(9)\)?',
            ['12'], '12',
            r'Vì \(f(2) = f(10) = 19\), theo tính đối xứng của parabol, hoành độ đỉnh là trung điểm: \(h = \frac{2 + 10}{2} = 6\), và cực tiểu \(k = 3\). Suy ra \(f(x) = a(x - 6)^2 + 3\). Thay \(f(2) = 19\): \(a(2 - 6)^2 + 3 = 19 \Rightarrow 16a = 16 \Rightarrow a = 1\). Vậy \(f(9) = (9 - 6)^2 + 3 = 9 + 3 = 12\).',
            r'Hễ thấy hai điểm có cùng tung độ \(f(x_1) = f(x_2)\), hoành độ đỉnh lập tức là \(h = \frac{x_1 + x_2}{2}\)!',
            r'Nhập 3 điểm `(2, 19)`, `(6, 3)`, `(10, 19)` vào Table trên Desmos rồi gõ `y1 ~ a(x1 - 6)^2 + 3` → ra ngay `a = 1`, tính `(9 - 6)^2 + 3 = 12`.'
        ),
        math_mcq(
            'sat_mm1_m1_q10', 10, 'Advanced Math', 'Nonlinear equations in one variable and systems of equations in two variables', 'Medium',
            r'<p>Consider the quadratic equation below, where \(c\) is a constant:</p><p style="text-align:center;">\[2x^2 - 12x + c = 0\]</p>',
            r'If the equation has <b>exactly one real solution</b>, what is the value of \(c\)?',
            {'A': r'\(9\)', 'B': r'\(12\)', 'C': r'\(18\)', 'D': r'\(36\)'},
            'C',
            r'Phương trình bậc hai có đúng 1 nghiệm thực khi biệt thức \(\Delta = b^2 - 4ac = 0\): \((-12)^2 - 4(2)(c) = 0 \Rightarrow 144 - 8c = 0 \Rightarrow c = 18\).',
            r'Đúng 1 nghiệm thực \(\Leftrightarrow b^2 - 4ac = 0\). Rút 2 ra ngoài cũng thấy ngay \(2(x^2 - 6x + 9) = 0 \Rightarrow c = 18\).',
            {
                'A': ('Quên nhân hệ số a = 2', r'Nhầm \(c = (6/2)^2 = 9\) mà quên hệ số \(a = 2\) phía trước \(x^2\).'),
                'B': ('Nhầm hệ số b', r'Lấy trực tiếp \(|b| = 12\).'),
                'C': ('Đáp án đúng', r'\(\Delta = 144 - 8c = 0 \Rightarrow c = 18\).'),
                'D': ('Nhầm công thức 4ac', r'Chỉ chia cho 4 thay vì \(4a = 8\): \(144/4 = 36\).'),
            },
            r'Gõ `y = 2x^2 - 12x + c` vào Desmos, thêm slider `c` (khoảng 0..40) → kéo đến khi đỉnh parabol vừa chạm đúng trục Ox tại `c = 18`.'
        ),
        math_mcq(
            'sat_mm1_m1_q11', 11, 'Advanced Math', 'Equivalent expressions', 'Medium',
            r'<p>Consider the rational expression below for all \(x > 3\):</p><p style="text-align:center;">\[\frac{x^2 - 9}{x^2 + 5x + 6}\]</p>',
            r'Which of the following is equivalent to the given expression?',
            {
                'A': r'\(\frac{x - 3}{x + 2}\)',
                'B': r'\(\frac{x + 3}{x + 2}\)',
                'C': r'\(\frac{x - 3}{x - 2}\)',
                'D': r'\(\frac{-9}{5x + 6}\)',
            },
            'A',
            r'Phân tích nhân tử cả tử và mẫu: \(\frac{(x - 3)(x + 3)}{(x + 2)(x + 3)}\). Vì \(x > 3\) nên \(x + 3 \neq 0\), triệt tiêu nhân tử chung \((x + 3)\) còn \(\frac{x - 3}{x + 2}\).',
            r'Nhận diện ngay hiệu hai bình phương \(x^2 - 9 = (x - 3)(x + 3)\) và không bao giờ gạch tắt \(x^2\) ở tổng!',
            {
                'A': ('Đáp án đúng', r'Triệt tiêu chính xác nhân tử chung \((x + 3)\).'),
                'B': ('Triệt tiêu nhầm dấu', r'Giữ lại \((x + 3)\) thay vì \((x - 3)\).'),
                'C': ('Phân tích sai mẫu', r'Nhầm \(x^2 + 5x + 6\) có nhân tử \((x - 2)\).'),
                'D': ('Bẫy gạch tắt số hạng', r'Gạch \(x^2\) trên tử và dưới mẫu — vi phạm cơ bản đại số!'),
            },
            r'Thử nhanh `x = 5` vào biểu thức gốc: `(25 - 9)/(25 + 25 + 6) = 16/56 = 2/7`. Chỉ phương án A cho `(5 - 3)/(5 + 2) = 2/7`!'
        ),
        math_mcq(
            'sat_mm1_m1_q12', 12, 'Advanced Math', 'Nonlinear functions', 'Easy',
            r'<p>An oceanographic buoy transmits a sonar pulse whose signal strength \(P(t)\), in milliwatts, \(t\) hours after deployment is modeled by:</p><p style="text-align:center;">\[P(t) = 480(0.85)^t\]</p>',
            r'According to the model, how does the signal strength change each hour?',
            {
                'A': r'It decreases by \(85\%\) each hour.',
                'B': r'It decreases by \(15\%\) each hour.',
                'C': r'It increases by \(85\%\) each hour.',
                'D': r'It decreases by \(0.85\) milliwatts each hour.',
            },
            'B',
            r'Trong mô hình hàm mũ giảm \(P(t) = a(1 - r)^t\), cơ số \(0.85 = 1 - 0.15\), nghĩa là sau mỗi giờ tín hiệu giữ lại 85% và <b>giảm đi 15%</b>.',
            r'Với cơ số \(b < 1\), tốc độ giảm phần trăm là \((1 - b) \times 100\%\), KHÔNG phải \(b \times 100\%\)!',
            {
                'A': ('Bẫy cơ số = phần trăm giảm', r'85% là phần CÒN LẠI, không phải phần bị giảm đi.'),
                'B': ('Đáp án đúng', r'\(1 - 0.85 = 0.15 = 15\%\) giảm mỗi giờ.'),
                'C': ('Nhầm tăng/giảm', r'Cơ số \(0.85 < 1\) là suy giảm (decay), không phải tăng trưởng.'),
                'D': ('Nhầm tuyến tính', r'Mô hình là hàm mũ (theo tỉ lệ %), không phải giảm lượng cố định milliwatts.'),
            },
            r'Kiểm tra nhanh tại `t = 0` (`480`) và `t = 1` (`408`): giảm `(480 - 408)/480 = 0.15 = 15%`.'
        ),
        math_spr(
            'sat_mm1_m1_q13', 13, 'Advanced Math', 'Nonlinear equations in one variable and systems of equations in two variables', 'Medium-Hard',
            r'<p>Consider the quadratic equation below:</p><p style="text-align:center;">\[3x^2 - 21x + 10 = 0\]</p>',
            r'What is the <b>sum</b> of the solutions to the given equation?',
            ['7'], '7',
            r'Kiểm tra biệt thức \(\Delta = (-21)^2 - 4(3)(10) = 441 - 120 = 321 > 0\), phương trình có 2 nghiệm thực phân biệt. Theo định lý Vieta, tổng hai nghiệm bằng \(-\frac{b}{a} = -\frac{-21}{3} = 7\).',
            r'Tổng nghiệm của \(ax^2 + bx + c = 0\) luôn bằng \(-\frac{b}{a}\) (nhớ chia cho \(a\) và kiểm tra \(\Delta \ge 0\))!',
            r'Vẽ `y = 3x^2 - 21x + 10` trong Desmos, bấm 2 giao điểm trục Ox (`0.514` và `6.486`) → cộng lại đúng bằng `7`!'
        ),
        math_mcq(
            'sat_mm1_m1_q14', 14, 'Advanced Math', 'Nonlinear equations in one variable and systems of equations in two variables', 'Medium-Hard',
            r'<p>Consider the radical equation shown below:</p><p style="text-align:center;">\[\sqrt{3x + 10} = x + 2\]</p>',
            r'What is the set of all real solutions to this equation?',
            {'A': r'\(\{-3, 2\}\)', 'B': r'\(\{-3\}\)', 'C': r'\(\{2\}\)', 'D': r'There are no real solutions.'},
            'C',
            r'Bình phương hai vế (điều kiện \(x + 2 \ge 0 \Leftrightarrow x \ge -2\)): \(3x + 10 = x^2 + 4x + 4 \Rightarrow x^2 + x - 6 = 0 \Rightarrow (x + 3)(x - 2) = 0 \Rightarrow x = -3\) hoặc \(x = 2\). Thử lại: \(x = 2 \Rightarrow \sqrt{16} = 4\) (đúng); \(x = -3 \Rightarrow \sqrt{1} = 1 \neq -1\) (nghiệm ngoại lai, LOẠI!).',
            r'Phương trình căn thức BẮT BUỘC thử lại nghiệm vào phương trình gốc để loại nghiệm ngoại lai làm vế phải âm!',
            {
                'A': ('Quên loại nghiệm ngoại lai', r'Giữ lại \(x = -3\) dù vế phải \(-3 + 2 = -1 < 0\) không thể bằng căn bậc hai.'),
                'B': ('Chọn đúng nghiệm ngoại lai', r'\(x = -3\) làm sai đẳng thức gốc.'),
                'C': ('Đáp án đúng', r'Chỉ có duy nhất \(x = 2\) thỏa mãn phương trình gốc.'),
                'D': ('Bỏ sót nghiệm hợp lệ', r'\(x = 2\) là nghiệm thực hoàn toàn hợp lệ.'),
            },
            r'Vẽ `y = sqrt(3x + 10)` và `y = x + 2` trên Desmos → chỉ có ĐÚNG 1 giao điểm tại `(2, 4)` → `x = 2`!'
        ),
        math_mcq(
            'sat_mm1_m1_q15', 15, 'Advanced Math', 'Nonlinear functions', 'Medium-Hard',
            r'<p>The function \(f\) is defined by \(f(x) = x^2 - 2x + 5\). The function \(g\) is defined by \(g(x) = f(x - 4) + 7\).</p>',
            r'What are the coordinates of the vertex of the graph of \(y = g(x)\) in the \(xy\)-plane?',
            {'A': r'\((-3, 11)\)', 'B': r'\((-3, -3)\)', 'C': r'\((5, -3)\)', 'D': r'\((5, 11)\)'},
            'D',
            r'Tìm đỉnh của \(f(x) = x^2 - 2x + 5 = (x - 1)^2 + 4\): đỉnh là \((1, 4)\). Hàm \(g(x) = f(x - 4) + 7\) dịch đồ thị sang <b>phải 4 đơn vị</b> (\(1 + 4 = 5\)) và <b>lên 7 đơn vị</b> (\(4 + 7 = 11\)). Vậy đỉnh của \(g\) là \((5, 11)\).',
            r'Quy tắc tịnh tiến: \(f(x - h) + k\) luôn cộng \(+h\) vào hoành độ và \(+k\) vào tung độ ("trong ngoặc ngược, ngoài ngoặc xuôi").',
            {
                'A': ('Dịch sai hướng ngang', r'Lấy \(1 - 4 = -3\) thay vì dịch phải \(1 + 4 = 5\).'),
                'B': ('Dịch sai cả 2 hướng', r'Trừ cả 4 lẫn 7.'),
                'C': ('Dịch sai hướng dọc', r'Lấy \(4 - 7 = -3\) thay vì \(4 + 7 = 11\).'),
                'D': ('Đáp án đúng', r'Đỉnh \((1, 4)\) dịch phải 4, lên 7 thành \((5, 11)\).'),
            },
            r'Gõ `f(x) = x^2 - 2x + 5` và `g(x) = f(x - 4) + 7` vào Desmos → bấm vào đáy parabol `g` đọc ngay `(5, 11)`!'
        ),
        math_spr(
            'sat_mm1_m1_q16', 16, 'Problem-Solving and Data Analysis', 'Ratios, rates, proportional relationships, and units', 'Medium',
            r'<p>A botanical conservatory installs a tempered glass skylight panel with an area of \(720\) square inches. (\(1\text{ foot} = 12\text{ inches}\))</p>',
            r'What is the area of the skylight panel, in <b>square feet</b>?',
            ['5'], '5',
            r'Vì \(1\text{ ft} = 12\text{ in}\), nên \(1\text{ ft}^2 = 12^2 = 144\text{ in}^2\). Đổi đơn vị diện tích: \(\frac{720}{144} = 5\text{ ft}^2\).',
            r'Khi đổi đơn vị DIỆN TÍCH (square units), phải BÌNH PHƯƠNG hệ số đổi chiều dài (\(12^2 = 144\))!',
            r'Gõ `720 / 12^2` vào Desmos ra ngay `5`.'
        ),
        math_mcq(
            'sat_mm1_m1_q17', 17, 'Problem-Solving and Data Analysis', 'Probability and conditional probability', 'Medium',
            tbl_q17 + r'<p>The table above summarizes the types of marine samples collected across three ocean zones during a reef survey.</p>',
            r'If a sample from <b>Zone B</b> is selected at random, what is the probability that it is a <b>Coral</b> sample?',
            {'A': r'\(\frac{2}{5}\)', 'B': r'\(\frac{4}{25}\)', 'C': r'\(\frac{8}{25}\)', 'D': r'\(\frac{3}{5}\)'},
            'A',
            r'Điều kiện bài toán: mẫu được chọn ngẫu nhiên từ <b>Zone B</b> → mẫu số chỉ là tổng hàng Zone B = \(60\). Số mẫu Coral ở Zone B là \(24\). Xác suất cần tìm: \(\frac{24}{60} = \frac{2}{5}\).',
            r'Xác suất có điều kiện: cụm "If a sample from Zone B..." cố định mẫu số bằng tổng đúng nhóm Zone B (60), không phải tổng toàn bảng (150)!',
            {
                'A': ('Đáp án đúng', r'\(\frac{24}{60} = \frac{2}{5}\).'),
                'B': ('Bẫy tổng toàn bảng', r'Tính \(\frac{24}{150} = \frac{4}{25}\) — quên giới hạn mẫu số vào Zone B.'),
                'C': ('Nhầm cột điều kiện', r'Tính \(\frac{24}{75} = \frac{8}{25}\) (chia cho tổng Coral thay vì tổng Zone B).'),
                'D': ('Nhầm Kelp thay vì Coral', r'Tính \(\frac{36}{60} = \frac{3}{5}\) là xác suất chọn mẫu Kelp.'),
            },
            r'Gõ `24/60` trên Desmos rồi bấm biểu tượng phân số bên trái để rút gọn ngay thành `2/5`.'
        ),
        math_mcq(
            'sat_mm1_m1_q18', 18, 'Problem-Solving and Data Analysis', 'One-variable data: Distributions and measures of center and spread', 'Medium',
            r'<p>Data set \(R\) consists of \(20\) temperature readings recorded by a deep-sea sensor. Data set \(S\) is created by adding \(15^\circ\text{C}\) to every reading in data set \(R\).</p>',
            r'Which of the following statements correctly compares the mean and standard deviation of data set \(S\) to those of data set \(R\)?',
            {
                'A': r'Both the mean and the standard deviation of \(S\) are \(15\) greater than those of \(R\).',
                'B': r'The mean of \(S\) is equal to the mean of \(R\), and the standard deviation of \(S\) is \(15\) greater.',
                'C': r'Both the mean and the standard deviation of \(S\) are equal to those of \(R\).',
                'D': r'The mean of \(S\) is \(15\) greater than the mean of \(R\), and the standard deviations are equal.',
            },
            'D',
            r'Cộng cùng hằng số \(+15\) vào mọi giá trị trong tập dữ liệu làm dịch chuyển vị trí trung tâm (Mean và Median đều tăng thêm 15), nhưng khoảng cách phân tán giữa các điểm hoàn toàn không đổi nên Standard Deviation giữ nguyên bằng nhau.',
            r'Cộng hằng số \(+c\) vào cả tập dữ liệu: Mean/Median \(+c\), còn Range và Standard Deviation KHÔNG ĐỔI!',
            {
                'A': ('Nhầm tính chất SD', r'Độ lệch chuẩn không tăng khi cộng cùng một hằng số.'),
                'B': ('Đảo ngược Mean và SD', r'Mean mới là đại lượng tăng thêm 15, còn SD giữ nguyên.'),
                'C': ('Bỏ qua dịch chuyển Mean', r'Trung bình cộng chắc chắn tăng thêm 15.'),
                'D': ('Đáp án đúng', r'Mean tăng 15 và Standard Deviation hoàn toàn không đổi.'),
            },
            r'Nếu muốn kiểm chứng, thử `A = [1, 3, 5]`, `B = A + 15` trên Desmos rồi so `mean(A), mean(B)` và `stdev(A), stdev(B)`.'
        ),
        math_spr(
            'sat_mm1_m1_q19', 19, 'Problem-Solving and Data Analysis', 'Percentages', 'Medium-Hard',
            r'<p>For three positive numbers \(a\), \(b\), and \(c\), it is known that \(a\) is \(140\%\) of \(b\), and \(b\) is \(25\%\) of \(c\).</p>',
            r'If \(a\) is \(p\%\) of \(c\), what is the value of \(p\)?',
            ['35'], '35',
            r'Đặt \(c = 100\). Khi đó \(b = 25\% \text{ của } 100 = 25\). Tiếp tục \(a = 140\% \text{ của } 25 = 1.40 \times 25 = 35\). Do \(c = 100\) nên \(a\) bằng đúng \(35\%\) của \(c \Rightarrow p = 35\).',
            r'Với chuỗi phần trăm đại số, đặt biến cuối \(c = 100\) để tính thẳng ra phần trăm trong 5 giây!',
            r'Gõ `1.40 * 0.25 * 100` trên Desmos ra ngay `35`.'
        ),
        math_mcq(
            'sat_mm1_m1_q20', 20, 'Geometry and Trigonometry', 'Lines, angles, and triangles', 'Medium',
            svg_q20 + r'<p>In the figure above, parallel lines \(\ell\) and \(m\) are intersected by a transversal.</p>',
            r'What is the value of \(y\)?',
            {'A': r'\(16\)', 'B': r'\(114\)', 'C': r'\(66\)', 'D': r'\(124\)'},
            'B',
            r'Hai góc \((3x + 18)^\circ\) và \((5x - 14)^\circ\) là hai góc đồng vị (cùng là góc nhọn trên 2 đường song song) nên bằng nhau: \(3x + 18 = 5x - 14 \Rightarrow 2x = 32 \Rightarrow x = 16\). Suy ra số đo góc nhọn là \(3(16) + 18 = 66^\circ\). Góc \(y^\circ\) kề bù (góc tù) với góc nhọn nên \(y = 180 - 66 = 114\).',
            r'Đường cắt hai đường song song chỉ có 2 cỡ góc: nhọn = nhọn, và nhọn + tù = \(180^\circ\)!',
            {
                'A': ('Bẫy dừng ở x', r'\(16\) mới chỉ là giá trị của \(x\), chưa tính góc \(y\).'),
                'B': ('Đáp án đúng', r'Góc nhọn \(= 66^\circ \Rightarrow y = 180 - 66 = 114\).'),
                'C': ('Nhầm góc nhọn vs góc tù', r'\(66^\circ\) là số đo góc nhọn, trong khi \(y^\circ\) là góc tù bù với nó.'),
                'D': ('Trừ nhầm 180', r'Tính sai \(180 - 66\) thành \(124\).'),
            },
            r'Gõ `3x + 18 = 5x - 14` trên Desmos tìm `x = 16`, sau đó tính `180 - (3*16 + 18) = 114`.'
        ),
        math_mcq(
            'sat_mm1_m1_q21', 21, 'Geometry and Trigonometry', 'Circles', 'Medium-Hard',
            r'<p>In the \(xy\)-plane, a circle is defined by the equation:</p><p style="text-align:center;">\[x^2 + y^2 - 8x + 4y = 16\]</p>',
            r'What are the coordinates of the center and the length of the radius of this circle?',
            {
                'A': r'Center \((-4, 2)\), radius \(6\)',
                'B': r'Center \((4, -2)\), radius \(36\)',
                'C': r'Center \((4, -2)\), radius \(6\)',
                'D': r'Center \((4, -2)\), radius \(4\)',
            },
            'C',
            r'Hoàn thành bình phương hai biến: \((x^2 - 8x + 16) + (y^2 + 4y + 4) = 16 + 16 + 4 \Rightarrow (x - 4)^2 + (y + 2)^2 = 36\). Suy ra tâm \((4, -2)\) và bán kính \(r = \sqrt{36} = 6\).',
            r'Khi hoàn thành bình phương, đừng quên cộng thêm \((D/2)^2 + (E/2)^2\) vào vế phải và lấy căn bậc hai để ra bán kính \(r\)!',
            {
                'A': ('Nhầm dấu tọa độ tâm', r'\((x - 4)^2 + (y + 2)^2\) có tâm \((4, -2)\), không phải \((-4, 2)\).'),
                'B': ('Quên lấy căn bán kính', r'36 là \(r^2\), không phải bán kính \(r\).'),
                'C': ('Đáp án đúng', r'Tâm \((4, -2)\) và \(r = \sqrt{36} = 6\).'),
                'D': ('Quên cộng 16 và 4 vào vế phải', r'Chỉ lấy \(\sqrt{16} = 4\) mà quên cộng \(4^2 + 2^2 = 20\) vào vế phải.'),
            },
            r'Gõ nguyên văn `x^2 + y^2 - 8x + 4y = 16` lên Desmos → bấm 2 điểm trên/dưới cùng `(4, 4)` và `(4, -8)` → tâm `(4, -2)` và bán kính `r = (4 - (-8))/2 = 6`!'
        ),
        math_spr(
            'sat_mm1_m1_q22', 22, 'Geometry and Trigonometry', 'Right triangles and trigonometry', 'Medium-Hard',
            svg_q22 + r'<p>In right triangle \(ABC\) shown above, \(\angle B = 90^\circ\), the hypotenuse \(AC = 39\), and \(\sin(A) = \frac{5}{13}\).</p>',
            r'What is the length of side \(AB\)?',
            ['36'], '36',
            r'Ta có \(\sin(A) = \frac{BC}{AC} = \frac{5}{13}\). Vì \(AC = 39 = 13 \times 3\), suy ra \(BC = 5 \times 3 = 15\). Theo bộ ba Pythagoras \(5\text{–}12\text{–}13\) nhân 3 (hoặc \(\sqrt{39^2 - 15^2} = \sqrt{1296}\)), cạnh \(AB = 12 \times 3 = 36\).',
            r'Nhận diện bộ ba Pythagoras \(5\text{–}12\text{–}13\) nhân với hệ số \(3\) cho ra ngay tam giác \(15\text{–}36\text{–}39\) trong 5 giây!',
            r'Tính `BC = 39*(5/13) = 15`, rồi gõ `sqrt(39^2 - 15^2)` trên Desmos ra ngay `36`.'
        ),
    ]
