# -*- coding: utf-8 -*-
"""
Digital SAT Math Adaptive Mock Test #1 — Module 2 Standard/Lower (300–600 Band, 22 Questions)
Themes: Renewable Energy/Solar, Robotics/Microchips, Oceanography, Botanical Architecture, Shipping Logistics.
Blueprint: 8 Algebra (Q1-Q8), 7 Advanced Math (Q9-Q15), 4 PSDA (Q16-Q19), 3 Geometry/Trig (Q20-Q22).
Format: 16 MCQ (A:4, B:4, C:4, D:4) + 6 SPR (Q5, Q9, Q13, Q16, Q19, Q22).
"""

from fractions import Fraction
from sat_math_helpers import math_mcq, math_spr, build_math_table, svg_circle_sector

def verify_math():
    assert 4 * 6 + 7 == 31 and 2 * 6 + 1 == 13
    assert Fraction(16 - 4, 5 - 1) == 3
    assert 10 + 4 == 14 and 10 - 4 == 6
    assert 3 * (9 - 4) == 15
    assert 2 * 8 - 5 == 11
    assert 12 + 8 == 20 and 50 * 12 + 80 * 8 == 1240
    assert 2 * 16 - 3 * 4 + 5 == 25
    assert (3 - 3) * (3 - 4) == 0 and 3 + 4 == 7
    assert Fraction(90, 15) * 25 == 150
    assert Fraction(35, 100) * 240 == 84
    s = sorted([12, 18, 15, 29, 21, 16, 24])
    assert s[3] == 18
    assert Fraction(18, 120) == Fraction(3, 20)
    assert 180 - (48 + 67) == 65
    assert 7 ** 2 == 49
    assert 8 * 5 * 4 == 160

def get_m2l_questions():
    tbl_q19 = build_math_table(
        ['Inspection Status', 'Sensor Batch A', 'Sensor Batch B', 'Total'],
        [
            ['Passed', '56', '46', '102'],
            ['Defective', '8', '10', '18'],
            ['Total', '64', '56', '120'],
        ],
        caption='Robotics Microchip Quality Control'
    )
    svg_q21 = svg_circle_sector('r = 7', '360°', note='Circle with radius 7')

    return [
        math_mcq(
            'sat_mm1_m2l_q1', 1, 'Algebra', 'Linear equations in one variable', 'Easy',
            r'<p>Consider the equation \(4x + 7 = 31\).</p>',
            r'What is the value of \(2x + 1\)?',
            {'A': r'\(13\)', 'B': r'\(6\)', 'C': r'\(12\)', 'D': r'\(19\)'},
            'A',
            r'Giải phương trình: \(4x = 31 - 7 = 24 \Rightarrow x = 6\). Thay vào biểu thức cần tìm: \(2(6) + 1 = 13\).',
            r'Tìm \(x\) xong phải thay vào đúng biểu thức \(2x + 1\) đề hỏi.',
            {
                'A': ('Đáp án đúng', r'\(x = 6 \Rightarrow 2(6) + 1 = 13\).'),
                'B': ('Dừng ở x', r'6 chỉ là giá trị của \(x\).'),
                'C': ('Quên cộng 1', r'Chỉ tính \(2x = 12\).'),
                'D': ('Cộng thay vì trừ 7', r'Tính nhầm \(4x = 38\).'),
            },
            r'Gõ `4x + 7 = 31` trên Desmos ra `x = 6`, rồi tính `2(6) + 1 = 13`.'
        ),
        math_mcq(
            'sat_mm1_m2l_q2', 2, 'Algebra', 'Linear functions', 'Easy',
            r'<p>A botanical nursery charges a customer \(P(n) = 18n + 45\) dollars to deliver \(n\) potted olive trees.</p>',
            r'What does the number \(45\) represent in this equation?',
            {
                'A': r'The cost per potted olive tree, in dollars',
                'B': r'The flat delivery fee, in dollars, regardless of the number of trees',
                'C': r'The maximum number of trees that can be delivered',
                'D': r'The total price of \(45\) olive trees',
            },
            'B',
            r'Trong hàm \(P(n) = 18n + 45\), hằng số \(45\) là giá trị tại \(n = 0\) (y-intercept), tức mức phí giao hàng cố định $45 chưa tính tiền cây.',
            r'Hằng số tự do \(b\) trong \(y = mx + b\) luôn là chi phí/giá trị ban đầu cố định.',
            {
                'A': ('Nhầm với slope', r'$18 mới là đơn giá mỗi cây.'),
                'B': ('Đáp án đúng', r'$45 là phí cố định ban đầu (flat delivery fee).'),
                'C': ('Sai ý nghĩa', r'Không phải số lượng cây tối đa.'),
                'D': ('Sai đơn vị', r'45 có đơn vị là dollars, không phải số cây.'),
            },
            r'Thay `n = 0` vào `18(0) + 45 = 45` để thấy ngay đó là phí cố định ban đầu.'
        ),
        math_mcq(
            'sat_mm1_m2l_q3', 3, 'Algebra', 'Linear equations in two variables', 'Easy',
            r'<p>A line in the \(xy\)-plane passes through the points \((1, 4)\) and \((5, 16)\).</p>',
            r'What is the slope of this line?',
            {'A': r'\(\frac{1}{3}\)', 'B': r'\(2\)', 'C': r'\(3\)', 'D': r'\(4\)'},
            'C',
            r'Hệ số góc \(m = \frac{y_2 - y_1}{x_2 - x_1} = \frac{16 - 4}{5 - 1} = \frac{12}{4} = 3\).',
            r'Công thức slope luôn là \(\frac{\Delta y}{\Delta x}\) (tung độ trên tử, hoành độ dưới mẫu).',
            {
                'A': ('Đảo ngược Δx/Δy', r'Tính \(\frac{4}{12} = \frac{1}{3}\) bị ngược tử mẫu.'),
                'B': ('Tính sai hiệu', r'Trừ nhầm tọa độ.'),
                'C': ('Đáp án đúng', r'\(\frac{16 - 4}{5 - 1} = 3\).'),
                'D': ('Chia nhầm', r'Chia cho 3 thay vì 4.'),
            },
            r'Gõ `(16 - 4)/(5 - 1)` trên Desmos ra ngay `3`.'
        ),
        math_mcq(
            'sat_mm1_m2l_q4', 4, 'Algebra', 'Systems of two linear equations in two variables', 'Easy',
            r'<p>Consider the system of equations:</p><p style="text-align:center;">\[\begin{cases} x + y = 14 \\ x - y = 6 \end{cases}\]</p>',
            r'What is the value of \(y\)?',
            {'A': r'\(10\)', 'B': r'\(8\)', 'C': r'\(6\)', 'D': r'\(4\)'},
            'D',
            r'Lấy phương trình 1 trừ phương trình 2: \((x + y) - (x - y) = 14 - 6 \Rightarrow 2y = 8 \Rightarrow y = 4\) (và \(x = 10\)).',
            r'Với hệ đối xứng \(x + y\) và \(x - y\), trừ trực tiếp 2 phương trình ra ngay \(2y\)!',
            {
                'A': ('Bẫy tìm x thay vì y', r'10 là giá trị của \(x\), đề hỏi \(y\).'),
                'B': ('Quên chia 2', r'8 là \(2y\), cần chia 2 ra \(y = 4\).'),
                'C': ('Nhầm hằng số', r'6 là hiệu \(x - y\).'),
                'D': ('Đáp án đúng', r'\(y = 4\).'),
            },
            r'Vẽ `x + y = 14` và `x - y = 6` trên Desmos → bấm giao điểm `(10, 4)` → `y = 4`.'
        ),
        math_spr(
            'sat_mm1_m2l_q5', 5, 'Algebra', 'Linear equations in one variable', 'Easy',
            r'<p>Solve for \(x\) in the equation below:</p><p style="text-align:center;">\[3(x - 4) = 15\]</p>',
            r'What is the value of \(x\)?',
            ['9'], '9',
            r'Chia cả hai vế cho 3: \(x - 4 = 5 \Rightarrow x = 9\).',
            r'Chia trực tiếp hệ số ngoài ngoặc trước khi khai triển sẽ nhanh và ít sai hơn.',
            r'Gõ `3(x - 4) = 15` trên Desmos ra ngay đường thẳng đứng `x = 9`.'
        ),
        math_mcq(
            'sat_mm1_m2l_q6', 6, 'Algebra', 'Linear inequalities in one or two variables', 'Easy',
            r'<p>Consider the linear inequality \(2x - 5 \le 11\).</p>',
            r'Which of the following represents all solutions to the inequality?',
            {'A': r'\(x \le 8\)', 'B': r'\(x \le 3\)', 'C': r'\(x \ge 8\)', 'D': r'\(x \le 16\)'},
            'A',
            r'Cộng 5 vào hai vế: \(2x \le 16\). Chia hai vế cho 2 (số dương, giữ nguyên chiều): \(x \le 8\).',
            r'Chỉ đổi chiều bất đẳng thức khi nhân hoặc chia cho số ÂM.',
            {
                'A': ('Đáp án đúng', r'\(2x \le 16 \Rightarrow x \le 8\).'),
                'B': ('Trừ 5 thay vì cộng 5', r'Tính \(11 - 5 = 6 \Rightarrow x \le 3\).'),
                'C': ('Đổi chiều dấu nhầm', r'Chia cho số dương \(+2\) không được đổi chiều dấu.'),
                'D': ('Quên chia 2', r'Dừng lại ở \(2x \le 16\).'),
            },
            r'Gõ `2x - 5 <= 11` trên Desmos thấy miền tô nằm bên trái đường nét liền `x = 8`.'
        ),
        math_mcq(
            'sat_mm1_m2l_q7', 7, 'Algebra', 'Linear equations in two variables', 'Easy',
            r'<p>In the \(xy\)-plane, line \(p\) is parallel to the line \(y = 4x - 7\) and passes through the point \((0, 3)\).</p>',
            r'Which of the following is the equation of line \(p\)?',
            {'A': r'\(y = -\frac{1}{4}x + 3\)', 'B': r'\(y = 4x + 3\)', 'C': r'\(y = 4x - 3\)', 'D': r'\(y = 3x + 4\)'},
            'B',
            r'Hai đường thẳng song song có cùng hệ số góc \(m = 4\). Đi qua \((0, 3)\) nên tung độ gốc \(b = 3\). Vậy \(y = 4x + 3\).',
            r'Song song \(\Rightarrow\) giữ nguyên slope \(m\), chỉ thay y-intercept \(b\).',
            {
                'A': ('Nhầm vuông góc', r'Slope \(-\frac{1}{4}\) là đường vuông góc, không phải song song.'),
                'B': ('Đáp án đúng', r'Cùng slope 4 và y-intercept bằng 3.'),
                'C': ('Nhầm dấu b', r'Tung độ gốc là \(+3\), không phải \(-3\).'),
                'D': ('Đảo chỗ m và b', r'Hoán đổi nhầm hệ số góc và tung độ gốc.'),
            },
            r'Vẽ `y = 4x - 7` và `y = 4x + 3` trên Desmos thấy hai đường song song và đi qua `(0, 3)`.'
        ),
        math_mcq(
            'sat_mm1_m2l_q8', 8, 'Algebra', 'Systems of two linear equations in two variables', 'Medium',
            r'<p>A solar supplier ships \(20\) inverter kits in one order: \(x\) standard kits priced at $50 each and \(y\) pro kits priced at $80 each. The total value of the order is $1,240.</p>',
            r'How many pro kits (\(y\)) are in the order?',
            {'A': r'\(6\)', 'B': r'\(12\)', 'C': r'\(8\)', 'D': r'\(10\)'},
            'C',
            r'Lập hệ: \(x + y = 20\) và \(50x + 80y = 1{,}240\). Thế \(x = 20 - y\): \(50(20 - y) + 80y = 1{,}240 \Rightarrow 1{,}000 + 30y = 1{,}240 \Rightarrow 30y = 240 \Rightarrow y = 8\).',
            r'Gõ trực tiếp hệ hai phương trình vào Desmos để tránh sai số cộng trừ khi giải tay.',
            {
                'A': ('Tính nhầm 30y', r'Chia sai \(240/30\).'),
                'B': ('Bẫy tìm x thay vì y', r'12 là số bộ standard (\(x\)), đề hỏi số bộ pro (\(y\)).'),
                'C': ('Đáp án đúng', r'\(y = 8\) bộ pro và \(x = 12\) bộ standard.'),
                'D': ('Chia đều 20/2', r'Giả định sai hai loại có số lượng bằng nhau.'),
            },
            r'Gõ `x + y = 20` và `50x + 80y = 1240` trên Desmos → bấm giao điểm `(12, 8)` → `y = 8`!'
        ),
        math_spr(
            'sat_mm1_m2l_q9', 9, 'Advanced Math', 'Nonlinear functions', 'Easy',
            r'<p>The function \(f\) is defined by \(f(x) = 2x^2 - 3x + 5\).</p>',
            r'What is the value of \(f(4)\)?',
            ['25'], '25',
            r'Thay \(x = 4\) vào hàm số: \(f(4) = 2(4)^2 - 3(4) + 5 = 2(16) - 12 + 5 = 32 - 12 + 5 = 25\).',
            r'Nhớ thực hiện phép lũy thừa \(4^2 = 16\) trước khi nhân hệ số 2 (không tính \((2 \times 4)^2 = 64\))!',
            r'Gõ `f(x) = 2x^2 - 3x + 5` rồi gõ `f(4)` trên Desmos ra ngay `25`.'
        ),
        math_mcq(
            'sat_mm1_m2l_q10', 10, 'Advanced Math', 'Nonlinear equations in one variable and systems of equations in two variables', 'Easy',
            r'<p>Consider the quadratic equation \(x^2 - 7x + 12 = 0\).</p>',
            r'What is the sum of the two solutions to this equation?',
            {'A': r'\(-7\)', 'B': r'\(12\)', 'C': r'\(1\)', 'D': r'\(7\)'},
            'D',
            r'Phân tích nhân tử: \((x - 3)(x - 4) = 0 \Rightarrow x = 3\) hoặc \(x = 4\). Tổng hai nghiệm là \(3 + 4 = 7\) (hoặc dùng Vieta \(-\frac{b}{a} = 7\)).',
            r'Tổng hai nghiệm của \(x^2 + bx + c = 0\) bằng \(-b\) (nhớ đổi dấu hệ số \(b\)!).',
            {
                'A': ('Quên đổi dấu -b', r'\(-7\) là hệ số \(b\), tổng nghiệm phải là \(-b = +7\).'),
                'B': ('Nhầm tích hai nghiệm', r'12 là tích hai nghiệm \(3 \times 4\), không phải tổng.'),
                'C': ('Lấy hiệu 4 - 3', r'Tính nhầm hiệu thay vì tổng.'),
                'D': ('Đáp án đúng', r'\(3 + 4 = 7\).'),
            },
            r'Vẽ `y = x^2 - 7x + 12` trên Desmos thấy 2 nghiệm `3` và `4` → tổng là `7`.'
        ),
        math_mcq(
            'sat_mm1_m2l_q11', 11, 'Advanced Math', 'Equivalent expressions', 'Easy',
            r'<p>Which of the following expressions is equivalent to \((3x^4)^2\)?</p>',
            r'Choose the equivalent simplified expression.',
            {'A': r'\(9x^8\)', 'B': r'\(6x^8\)', 'C': r'\(9x^6\)', 'D': r'\(3x^8\)'},
            'A',
            r'Áp dụng quy tắc lũy thừa của tích và lũy thừa của lũy thừa: \((3x^4)^2 = 3^2 \cdot (x^4)^2 = 9x^{4 \cdot 2} = 9x^8\).',
            r'Nhớ bình phương CẢ hệ số \(3^2 = 9\) và NHÂN các số mũ \(4 \times 2 = 8\)!',
            {
                'A': ('Đáp án đúng', r'\(3^2 x^{4 \cdot 2} = 9x^8\).'),
                'B': ('Nhân 3 × 2 thay vì 3²', r'Hệ số 3 phải nâng lên mũ 2 thành 9.'),
                'C': ('Cộng số mũ 4 + 2', r'Lũy thừa tầng phải nhân số mũ \(4 \times 2 = 8\).'),
                'D': ('Quên bình phương hệ số 3', r'Giữ nguyên 3 thay vì \(3^2 = 9\).'),
            },
            r'Thử `x = 2` trên Desmos: `(3 * 2^4)^2 = 2304`, khớp duy nhất với `9 * 2^8 = 2304`.'
        ),
        math_mcq(
            'sat_mm1_m2l_q12', 12, 'Advanced Math', 'Nonlinear functions', 'Easy',
            r'<p>An ocean algae culture has mass \(N(t) = 250(1.12)^t\) grams after \(t\) days of growth.</p>',
            r'What is the initial mass of the algae culture at \(t = 0\), in grams?',
            {'A': r'\(1.12\)', 'B': r'\(250\)', 'C': r'\(280\)', 'D': r'\(12\)'},
            'B',
            r'Tại \(t = 0\): \(N(0) = 250(1.12)^0 = 250 \times 1 = 250\) gam.',
            r'Trong \(y = a \cdot b^t\), giá trị ban đầu tại \(t = 0\) luôn là hệ số \(a\) (vì \(b^0 = 1\)).',
            {
                'A': ('Nhầm với hệ số tăng trưởng', r'1.12 là growth factor mỗi ngày.'),
                'B': ('Đáp án đúng', r'\(N(0) = 250\) gam.'),
                'C': ('Tính tại t = 1', r'\(280\) là khối lượng sau 1 ngày, không phải ban đầu.'),
                'D': ('Nhầm phần trăm tăng', r'12% là tỉ lệ tăng mỗi ngày.'),
            },
            r'Thay `t = 0` vào `250 * 1.12^0 = 250`.'
        ),
        math_spr(
            'sat_mm1_m2l_q13', 13, 'Advanced Math', 'Nonlinear functions', 'Easy',
            r'<p>Consider the quadratic function written in vertex form:</p><p style="text-align:center;">\[y = (x - 5)^2 + 11\]</p>',
            r'What is the <b>minimum</b> value of \(y\)?',
            ['11'], '11',
            r'Vì \((x - 5)^2 \ge 0\) với mọi \(x\), giá trị nhỏ nhất của \(y\) bằng \(11\) đạt tại đỉnh \(x = 5\).',
            r'Trong Vertex Form \(y = a(x - h)^2 + k\) (với \(a > 0\)), giá trị nhỏ nhất là \(k\) (cẩn thận không nhập nhầm \(h = 5\))!',
            r'Vẽ `y = (x - 5)^2 + 11` trên Desmos → bấm điểm thấp nhất `(5, 11)` → giá trị nhỏ nhất của `y` là `11`.'
        ),
        math_mcq(
            'sat_mm1_m2l_q14', 14, 'Advanced Math', 'Equivalent expressions', 'Easy',
            r'<p>Which of the following is equivalent to \((x + 5)(x - 2)\)?</p>',
            r'Select the expanded polynomial.',
            {'A': r'\(x^2 - 3x - 10\)', 'B': r'\(x^2 + 3x + 10\)', 'C': r'\(x^2 + 3x - 10\)', 'D': r'\(x^2 + 7x - 10\)'},
            'C',
            r'Nhân phá ngoặc (FOIL): \(x^2 - 2x + 5x - 10 = x^2 + 3x - 10\).',
            r'Hệ số giữa là \(+5 + (-2) = +3\), hằng số tự do là \(5 \times (-2) = -10\).',
            {
                'A': ('Nhầm dấu hệ số x', r'\(5 - 2 = +3\), không phải \(-3\).'),
                'B': ('Nhầm dấu hằng số', r'\(5 \times (-2) = -10\), không phải \(+10\).'),
                'C': ('Đáp án đúng', r'\(x^2 + 3x - 10\).'),
                'D': ('Cộng 5 + 2 thay vì 5 - 2', r'Quên dấu trừ trước số 2.'),
            },
            r'Vẽ `y = (x + 5)(x - 2)` và kiểm tra đáp án trùng khít hoàn toàn trên Desmos.'
        ),
        math_mcq(
            'sat_mm1_m2l_q15', 15, 'Advanced Math', 'Nonlinear equations in one variable and systems of equations in two variables', 'Medium',
            r'<p>The perimeter \(P\) of a rectangular botanical bed with length \(L\) and width \(W\) is given by \(P = 2L + 2W\).</p>',
            r'Which equation correctly expresses \(W\) in terms of \(P\) and \(L\)?',
            {
                'A': r'\(W = P - 2L\)',
                'B': r'\(W = \frac{P + 2L}{2}\)',
                'C': r'\(W = \frac{P}{2} - 2L\)',
                'D': r'\(W = \frac{P - 2L}{2}\)',
            },
            'D',
            r'Chuyển \(2L\) sang vế trái: \(2W = P - 2L\). Chia cả hai vế cho 2: \(W = \frac{P - 2L}{2}\).',
            r'Khi chia cả hai vế cho 2, phải chia TẤT CẢ các số hạng ở tử (không quên chia 2 cho \(2L\)).',
            {
                'A': ('Quên chia 2', r'\(P - 2L\) mới là \(2W\).'),
                'B': ('Đổi sai dấu khi chuyển vế', r'Chuyển \(+2L\) phải đổi thành \(-2L\).'),
                'C': ('Chỉ chia P cho 2 mà quên chia 2L', r'\(\frac{P - 2L}{2} = \frac{P}{2} - L\), không phải \(\frac{P}{2} - 2L\).'),
                'D': ('Đáp án đúng', r'\(W = \frac{P - 2L}{2}\).'),
            },
            r'Thử số cụ thể `L = 3, W = 4` → `P = 14`; thay vào phương án D: `(14 - 6)/2 = 4` khớp chính xác!'
        ),
        math_spr(
            'sat_mm1_m2l_q16', 16, 'Problem-Solving and Data Analysis', 'Ratios, rates, proportional relationships, and units', 'Easy',
            r'<p>At a solar test site, \(15\) identical solar tiles generate \(90\) kilowatt-hours (kWh) of electricity per day.</p>',
            r'At the same rate, how many kilowatt-hours of electricity will \(25\) identical solar tiles generate per day?',
            ['150'], '150',
            r'Mỗi tấm tạo ra \(\frac{90}{15} = 6\text{ kWh/ngày}\). Vậy \(25\) tấm tạo ra \(25 \times 6 = 150\text{ kWh/ngày}\).',
            r'Tính đơn vị cơ sở (unit rate = 6 kWh/tấm) trước rồi nhân với số lượng mới.',
            r'Gõ `(90/15) * 25` trên Desmos ra ngay `150`.'
        ),
        math_mcq(
            'sat_mm1_m2l_q17', 17, 'Problem-Solving and Data Analysis', 'Percentages', 'Easy',
            r'<p>A robotics warehouse holds \(240\) circuit boards, and \(35\%\) of them are reserved for export.</p>',
            r'How many circuit boards are reserved for export?',
            {'A': r'\(84\)', 'B': r'\(72\)', 'C': r'\(96\)', 'D': r'\(156\)'},
            'A',
            r'Tính \(35\% \text{ của } 240 = 0.35 \times 240 = 84\).',
            r'Đổi \(p\%\) thành số thập phân \(p/100\) rồi nhân trực tiếp với tổng.',
            {
                'A': ('Đáp án đúng', r'\(0.35 \times 240 = 84\).'),
                'B': ('Tính 30%', r'\(0.30 \times 240 = 72\).'),
                'C': ('Tính 40%', r'\(0.40 \times 240 = 96\).'),
                'D': ('Tính phần còn lại 65%', r'\(240 - 84 = 156\) là số bảng mạch KHÔNG xuất khẩu.'),
            },
            r'Gõ `0.35 * 240` trên Desmos ra ngay `84`.'
        ),
        math_mcq(
            'sat_mm1_m2l_q18', 18, 'Problem-Solving and Data Analysis', 'One-variable data: Distributions and measures of center and spread', 'Easy',
            r'<p>Seven cargo ships waited the following numbers of hours at a port:</p><p style="text-align:center;">\[12,\; 18,\; 15,\; 29,\; 21,\; 16,\; 24\]</p>',
            r'What is the <b>median</b> wait time, in hours?',
            {'A': r'\(16\)', 'B': r'\(18\)', 'C': r'\(21\)', 'D': r'\(29\)'},
            'B',
            r'BẮT BUỘC sắp xếp dãy tăng dần trước: \(12, 15, 16, \mathbf{18}, 21, 24, 29\). Với 7 số, số trung vị (median) là số đứng chính giữa (vị trí thứ 4) \(= 18\).',
            r'Luôn sắp xếp dãy số theo thứ tự tăng dần trước khi lấy số chính giữa (đừng lấy ngay số giữa của dãy chưa sắp xếp là 29)!',
            {
                'A': ('Chọn vị trí thứ 3', r'16 đứng thứ 3, chưa phải chính giữa của 7 số.'),
                'B': ('Đáp án đúng', r'Số ở vị trí thứ 4 sau khi sắp xếp tăng dần là \(18\).'),
                'C': ('Chọn vị trí thứ 5', r'21 đứng thứ 5.'),
                'D': ('Bẫy chưa sắp xếp dãy', r'29 là số đứng thứ 4 trong dãy lộn xộn ban đầu!'),
            },
            r'Gõ `median(12, 18, 15, 29, 21, 16, 24)` trên Desmos ra ngay `18`!'
        ),
        math_spr(
            'sat_mm1_m2l_q19', 19, 'Problem-Solving and Data Analysis', 'Probability and conditional probability', 'Medium',
            tbl_q19 + r'<p>The table above shows the quality control results for \(120\) robotics microchips.</p>',
            r'If one microchip is selected at random from all \(120\) microchips, what is the probability that it is <b>defective</b>? (Express your answer as a fraction or decimal.)</p>',
            ['3/20', '0.15', '.15'], '3/20 hoặc 0.15',
            r'Tổng số chip lỗi (Defective) là \(18\) trên tổng số \(120\) chip. Xác suất là \(\frac{18}{120} = \frac{3}{20} = 0.15\).',
            r'Cả dạng phân số rút gọn `3/20` và số thập phân `0.15` đều được Bluebook chấm đúng tuyệt đối!',
            r'Gõ `18 / 120` trên Desmos ra `0.15` (bấm nút phân số ra `3/20`).'
        ),
        math_mcq(
            'sat_mm1_m2l_q20', 20, 'Geometry and Trigonometry', 'Lines, angles, and triangles', 'Easy',
            r'<p>In a triangle, two interior angles measure \(48^\circ\) and \(67^\circ\).</p>',
            r'What is the measure of the third interior angle, in degrees?',
            {'A': r'\(55^\circ\)', 'B': r'\(115^\circ\)', 'C': r'\(65^\circ\)', 'D': r'\(75^\circ\)'},
            'C',
            r'Tổng 3 góc trong một tam giác luôn bằng \(180^\circ\): \(180^\circ - (48^\circ + 67^\circ) = 180^\circ - 115^\circ = 65^\circ\).',
            r'Tổng 3 góc tam giác luôn bằng \(180^\circ\) (cẩn thận không dừng lại ở tổng 2 góc \(115^\circ\)).',
            {
                'A': ('Trừ sai 180 - 115', r'Tính nhầm ra 55.'),
                'B': ('Quên trừ khỏi 180°', r'\(115^\circ\) là tổng hai góc đã cho.'),
                'C': ('Đáp án đúng', r'\(180^\circ - 115^\circ = 65^\circ\).'),
                'D': ('Cộng nhầm 48 + 67 = 105', r'Sai phép cộng hàng đơn vị.'),
            },
            r'Gõ `180 - 48 - 67` trên Desmos ra ngay `65`.'
        ),
        math_mcq(
            'sat_mm1_m2l_q21', 21, 'Geometry and Trigonometry', 'Circles', 'Easy',
            svg_q21 + r'<p>A circular botanical fountain has a radius of \(7\) meters.</p>',
            r'What is the area of the circular fountain, in square meters?',
            {'A': r'\(7\pi\)', 'B': r'\(14\pi\)', 'C': r'\(28\pi\)', 'D': r'\(49\pi\)'},
            'D',
            r'Diện tích hình tròn: \(A = \pi r^2 = \pi(7)^2 = 49\pi\text{ m}^2\).',
            r'Phân biệt chu vi \(C = 2\pi r = 14\pi\) với diện tích \(A = \pi r^2 = 49\pi\).',
            {
                'A': ('Quên bình phương r', r'\(7\pi\) mới chỉ là \(\pi r\).'),
                'B': ('Nhầm chu vi C = 2πr', r'\(14\pi\) là chu vi hình tròn, không phải diện tích.'),
                'C': ('Nhân 4 thay vì bình phương', r'Tính nhầm \(4 \times 7\pi = 28\pi\).'),
                'D': ('Đáp án đúng', r'\(A = \pi (7^2) = 49\pi\).'),
            },
            r'Kiểm tra trong bảng Reference Sheet: Circle Area `A = pi * r^2 = 49pi`.'
        ),
        math_spr(
            'sat_mm1_m2l_q22', 22, 'Geometry and Trigonometry', 'Area and volume', 'Easy',
            r'<p>A rectangular shipping crate has a length of \(8\) feet, a width of \(5\) feet, and a height of \(4\) feet.</p>',
            r'What is the volume of the shipping crate, in cubic feet?',
            ['160'], '160',
            r'Thể tích hình hộp chữ nhật: \(V = \ell w h = 8 \times 5 \times 4 = 160\text{ ft}^3\).',
            r'Thể tích lăng trụ chữ nhật = Dài × Rộng × Cao (có sẵn trong nút Reference).',
            r'Gõ `8 * 5 * 4` trên Desmos ra ngay `160`.'
        ),
    ]
