# -*- coding: utf-8 -*-
"""
Digital SAT Math Adaptive Mock Test #5 — Module 2 Standard/Lower (300–600 Band, 22 Questions)
Themes: Wind Turbines & Tidal Power Grids, Optical Lens Labs, Specialty Coffee Roasting, Alpine Suspension Bridges, Glass Atrium Architecture.
Blueprint: 8 Algebra (Q1-Q8), 7 Advanced Math (Q9-Q15), 4 PSDA (Q16-Q19), 3 Geometry/Trig (Q20-Q22).
Format: 16 MCQ (A:4, B:4, C:4, D:4) + 6 SPR (Q5, Q9, Q13, Q16, Q19, Q22).
"""

from fractions import Fraction
from sat_math_helpers import math_mcq, math_spr, build_math_table, svg_cylinder

def verify_math():
    assert 5 * 7 - 9 == 26 and 3 * 7 - 2 == 19
    assert Fraction(21 - 5, 6 - 2) == 4
    assert 11 + 7 == 18 and 11 - 7 == 4
    assert 4 * (8 + 3) == 44
    assert 3 * 7 + 4 == 25
    assert 18 + 12 == 30 and 12 * 18 + 18 * 12 == 432
    assert 3 * 9 - 4 * 3 + 2 == 17
    assert (5 - 4) * (5 - 5) == 0 and (4 - 4) * (4 - 5) == 0
    assert 2 ** 4 == 16 and 3 * 4 == 12
    assert Fraction(180, 12) * 20 == 300
    assert Fraction(45, 100) * 320 == 144
    assert sorted([9, 14, 11, 22, 17, 13, 25])[3] == 14
    assert Fraction(27, 108) == Fraction(1, 4)
    assert 180 - (52 + 71) == 57
    assert 2 * 9 == 18
    assert (4 ** 2) * 10 == 160

def get_m2l_questions():
    tbl_q19 = build_math_table(
        ['Optical Coating', 'Lab Line 1', 'Lab Line 2', 'Total'],
        [
            ['Anti-Glare', '15', '12', '27'],
            ['Standard Clear', '45', '36', '81'],
            ['Total', '60', '48', '108'],
        ],
        caption='Optical Lens Coating Batch Summary'
    )
    svg_q22 = svg_cylinder('r = 4', 'h = 10', note='Right Circular Cylinder')

    return [
        math_mcq(
            'sat_mm5_m2l_q1', 1, 'Algebra', 'Linear equations in one variable', 'Easy',
            r'<p>Consider the equation \(5x - 9 = 26\).</p>',
            r'What is the value of \(3x - 2\)?',
            {'A': r'\(7\)', 'B': r'\(19\)', 'C': r'\(21\)', 'D': r'\(23\)'},
            'B',
            r'Giải \(5x = 35 \Rightarrow x = 7\). Thay vào \(3x - 2 = 3(7) - 2 = 19\).',
            r'Luôn thay nghiệm \(x = 7\) vào đúng biểu thức \(3x - 2\) đề hỏi.',
            {
                'A': ('Dừng ở x', r'7 chỉ là giá trị của \(x\).'),
                'B': ('Đáp án đúng', r'\(3(7) - 2 = 19\).'),
                'C': ('Quên trừ 2', r'21 là \(3x\).'),
                'D': ('Cộng 2 thay vì trừ 2', r'\(21 + 2 = 23\).'),
            },
            r'Gõ `5x - 9 = 26` trên Desmos ra `x = 7`, rồi tính `3(7) - 2 = 19`.'
        ),
        math_mcq(
            'sat_mm5_m2l_q2', 2, 'Algebra', 'Linear functions', 'Easy',
            r'<p>An optical technician models the total polishing time \(T(n)\), in minutes, for \(n\) glass lenses using \(T(n) = 14n + 30\).</p>',
            r'What does the number \(14\) represent in this equation?',
            {
                'A': r'The polishing time required for each additional glass lens, in minutes',
                'B': r'The fixed machine warm-up time, in minutes',
                'C': r'The total number of lenses polished per day',
                'D': r'The total time to polish \(30\) lenses',
            },
            'A',
            r'Hệ số góc \(14\) là thời gian đánh bóng thêm cho mỗi thấu kính (14 phút/thấu kính), còn 30 là thời gian khởi động cố định.',
            r'Hệ số đứng trước biến \(n\) luôn biểu thị tốc độ tăng thêm trên MỖI 1 đơn vị \(n\).',
            {
                'A': ('Đáp án đúng', r'14 phút cho mỗi thấu kính tăng thêm.'),
                'B': ('Nhầm với y-intercept', r'Thời gian cố định ban đầu là 30 phút.'),
                'C': ('Sai đơn vị', r'14 có đơn vị phút/thấu kính, không phải số thấu kính.'),
                'D': ('Sai ý nghĩa', r'Tổng thời gian cho 30 thấu kính là \(14(30) + 30 = 450\) phút.'),
            },
            r'So sánh trực tiếp với dạng chuẩn `y = mx + b`: `m = 14` là tốc độ trên mỗi đơn vị.'
        ),
        math_mcq(
            'sat_mm5_m2l_q3', 3, 'Algebra', 'Linear equations in two variables', 'Easy',
            r'<p>A line in the \(xy\)-plane passes through the points \((2, 5)\) and \((6, 21)\).</p>',
            r'What is the slope of this line?',
            {'A': r'\(\frac{1}{4}\)', 'B': r'\(3\)', 'C': r'\(5\)', 'D': r'\(4\)'},
            'D',
            r'Hệ số góc \(m = \frac{21 - 5}{6 - 2} = \frac{16}{4} = 4\).',
            r'Slope luôn bằng \(\frac{y_2 - y_1}{x_2 - x_1}\).',
            {
                'A': ('Đảo tử mẫu Δx/Δy', r'Tính \(\frac{4}{16} = \frac{1}{4}\).'),
                'B': ('Trừ sai tọa độ', r'Tính nhầm tử hoặc mẫu.'),
                'C': ('Chia sai 16/4', r'Nhầm phép chia.'),
                'D': ('Đáp án đúng', r'\(\frac{16}{4} = 4\).'),
            },
            r'Gõ `(21 - 5)/(6 - 2)` trên Desmos ra ngay `4`.'
        ),
        math_mcq(
            'sat_mm5_m2l_q4', 4, 'Algebra', 'Systems of two linear equations in two variables', 'Easy',
            r'<p>Consider the system of equations:</p><p style="text-align:center;">\[\begin{cases} x + y = 18 \\ x - y = 4 \end{cases}\]</p>',
            r'What is the value of \(x\)?',
            {'A': r'\(7\)', 'B': r'\(14\)', 'C': r'\(11\)', 'D': r'\(22\)'},
            'C',
            r'Cộng hai phương trình: \(2x = 22 \Rightarrow x = 11\) (và \(y = 7\)).',
            r'Cộng trực tiếp hai phương trình để khử \(y\) trong 2 giây.',
            {
                'A': ('Bẫy tìm y thay vì x', r'7 là giá trị của \(y\).'),
                'B': ('Trừ thay vì cộng', r'\(18 - 4 = 14\) là \(2y\).'),
                'C': ('Đáp án đúng', r'\(2x = 22 \Rightarrow x = 11\).'),
                'D': ('Quên chia 2', r'22 là \(2x\).'),
            },
            r'Vẽ `x + y = 18` và `x - y = 4` trên Desmos → bấm giao điểm `(11, 7)` → `x = 11`.'
        ),
        math_spr(
            'sat_mm5_m2l_q5', 5, 'Algebra', 'Linear equations in one variable', 'Easy',
            r'<p>Solve the linear equation below for \(x\):</p><p style="text-align:center;">\[4(x + 3) = 44\]</p>',
            r'What is the value of \(x\)?',
            ['8'], '8',
            r'Chia hai vế cho 4: \(x + 3 = 11 \Rightarrow x = 8\).',
            r'Chia trực tiếp cho hệ số 4 trước rồi trừ 3.',
            r'Gõ `4(x + 3) = 44` trên Desmos ra ngay `x = 8`.'
        ),
        math_mcq(
            'sat_mm5_m2l_q6', 6, 'Algebra', 'Linear inequalities in one or two variables', 'Easy',
            r'<p>Consider the inequality \(3x + 4 \ge 25\).</p>',
            r'Which inequality represents all solutions for \(x\)?',
            {'A': r'\(x \le 7\)', 'B': r'\(x \ge 7\)', 'C': r'\(x \ge 9\)', 'D': r'\(x \ge 21\)'},
            'B',
            r'Trừ 4 hai vế: \(3x \ge 21 \Rightarrow x \ge 7\).',
            r'Chia cho số dương \(+3\) thì giữ nguyên chiều \(\ge\).',
            {
                'A': ('Đổi chiều dấu nhầm', r'Chia số dương không đảo chiều dấu.'),
                'B': ('Đáp án đúng', r'\(3x \ge 21 \Rightarrow x \ge 7\).'),
                'C': ('Cộng 4 thay vì trừ 4', r'Nhầm \(25 + 4 = 29\).'),
                'D': ('Quên chia 3', r'21 là \(3x\).'),
            },
            r'Gõ `3x + 4 >= 25` trên Desmos thấy miền tô nằm từ `x = 7` trở sang phải.'
        ),
        math_mcq(
            'sat_mm5_m2l_q7', 7, 'Algebra', 'Linear equations in two variables', 'Easy',
            r'<p>Line \(k\) in the \(xy\)-plane is parallel to the line \(y = -2x + 9\) and passes through \((0, -5)\).</p>',
            r'Which equation represents line \(k\)?',
            {'A': r'\(y = -2x - 5\)', 'B': r'\(y = 2x - 5\)', 'C': r'\(y = \frac{1}{2}x - 5\)', 'D': r'\(y = -2x + 5\)'},
            'A',
            r'Hai đường thẳng song song có cùng hệ số góc \(m = -2\). Qua \((0, -5) \Rightarrow b = -5\). Vậy \(y = -2x - 5\).',
            r'Song song giữ nguyên slope \(-2\) và lấy tung độ gốc \(-5\).',
            {
                'A': ('Đáp án đúng', r'Slope \(-2\) và y-intercept \(-5\).'),
                'B': ('Đổi sai dấu slope', r'Slope phải là \(-2\), không phải \(+2\).'),
                'C': ('Nhầm vuông góc', r'Slope \(+\frac{1}{2}\) là đường vuông góc.'),
                'D': ('Sai dấu y-intercept', r'Tung độ gốc là \(-5\), không phải \(+5\).'),
            },
            r'Vẽ `y = -2x + 9` và `y = -2x - 5` trên Desmos kiểm chứng song song và đi qua `(0, -5)`.'
        ),
        math_mcq(
            'sat_mm5_m2l_q8', 8, 'Algebra', 'Systems of two linear equations in two variables', 'Medium',
            r'<p>A coffee shop sells \(30\) bags of beans in one morning: \(x\) house-blend bags at $12 each and \(y\) single-origin bags at $18 each, totaling $432.</p>',
            r'How many house-blend bags (\(x\)) were sold?',
            {'A': r'\(12\)', 'B': r'\(15\)', 'C': r'\(16\)', 'D': r'\(18\)'},
            'D',
            r'Hệ: \(x + y = 30\) và \(12x + 18y = 432\). Thế \(y = 30 - x\): \(12x + 18(30 - x) = 432 \Rightarrow 540 - 6x = 432 \Rightarrow 6x = 108 \Rightarrow x = 18\).',
            r'Đọc kỹ đề hỏi \(x\) (house-blend = 18) chứ không phải \(y\) (single-origin = 12)!',
            {
                'A': ('Bẫy tìm y thay vì x', r'12 là số túi single-origin (\(y\)).'),
                'B': ('Chia đôi 30/2', r'Giả định sai hai loại bán bằng nhau.'),
                'C': ('Tính sai phép trừ 540 - 432', r'Chia nhầm \(108/6\).'),
                'D': ('Đáp án đúng', r'\(x = 18\) túi house-blend.'),
            },
            r'Gõ `x + y = 30` và `12x + 18y = 432` trên Desmos → bấm giao điểm `(18, 12)` → `x = 18`!'
        ),
        math_spr(
            'sat_mm5_m2l_q9', 9, 'Advanced Math', 'Nonlinear functions', 'Easy',
            r'<p>The function \(f\) is defined by \(f(x) = 3x^2 - 4x + 2\).</p>',
            r'What is the value of \(f(3)\)?',
            ['17'], '17',
            r'Thay \(x = 3\): \(f(3) = 3(3^2) - 4(3) + 2 = 27 - 12 + 2 = 17\).',
            r'Tính \(3^2 = 9\) trước khi nhân 3 để tránh nhầm thành \((3 \times 3)^2 = 81\).',
            r'Gõ `f(x) = 3x^2 - 4x + 2` rồi gõ `f(3)` trên Desmos ra ngay `17`.'
        ),
        math_mcq(
            'sat_mm5_m2l_q10', 10, 'Advanced Math', 'Nonlinear equations in one variable and systems of equations in two variables', 'Easy',
            r'<p>Consider the quadratic equation \(x^2 - 9x + 20 = 0\).</p>',
            r'What is the <b>greater</b> of the two solutions to this equation?',
            {'A': r'\(4\)', 'B': r'\(9\)', 'C': r'\(5\)', 'D': r'\(20\)'},
            'C',
            r'Phân tích nhân tử: \((x - 4)(x - 5) = 0 \Rightarrow x = 4\) hoặc \(x = 5\). Nghiệm lớn hơn là \(5\).',
            r'Tìm hai số có tích \(+20\) và tổng \(+9\): đó là \(4\) và \(5\).',
            {
                'A': ('Chọn nghiệm nhỏ hơn', r'4 là nghiệm nhỏ hơn trong hai nghiệm 4 và 5.'),
                'B': ('Nhầm tổng hai nghiệm', r'9 là tổng hai nghiệm \(4 + 5\).'),
                'C': ('Đáp án đúng', r'Nghiệm lớn hơn là \(5\).'),
                'D': ('Nhầm tích hai nghiệm', r'20 là tích hai nghiệm.'),
            },
            r'Vẽ `y = x^2 - 9x + 20` trên Desmos thấy 2 giao điểm trục Ox tại `4` và `5` → lớn hơn là `5`.'
        ),
        math_mcq(
            'sat_mm5_m2l_q11', 11, 'Advanced Math', 'Equivalent expressions', 'Easy',
            r'<p>Which expression is equivalent to \((2x^3)^4\)?</p>',
            r'Choose the simplified equivalent expression.',
            {'A': r'\(8x^{12}\)', 'B': r'\(16x^{12}\)', 'C': r'\(16x^7\)', 'D': r'\(2x^{12}\)'},
            'B',
            r'\((2x^3)^4 = 2^4 \cdot (x^3)^4 = 16x^{3 \cdot 4} = 16x^{12}\).',
            r'Nâng lũy thừa 4 cho cả hệ số \(2^4 = 16\) và nhân số mũ \(3 \times 4 = 12\)!',
            {
                'A': ('Nhân 2 × 4 thay vì 2⁴', r'\(2^4 = 16\), không phải \(8\).'),
                'B': ('Đáp án đúng', r'\(16x^{12}\).'),
                'C': ('Cộng số mũ 3 + 4', r'Phải nhân số mũ \(3 \times 4 = 12\).'),
                'D': ('Quên lũy thừa hệ số 2', r'Phải tính \(2^4 = 16\).'),
            },
            r'Thử `x = 2` trên Desmos kiểm chứng `(2 * 2^3)^4 = 65536 = 16 * 2^12`.'
        ),
        math_mcq(
            'sat_mm5_m2l_q12', 12, 'Advanced Math', 'Nonlinear functions', 'Easy',
            r'<p>The pressure \(P(t)\), in kilopascals, inside an alpine pipeline \(t\) minutes after a valve opens is modeled by \(P(t) = 420(0.92)^t\).</p>',
            r'What was the initial pressure at \(t = 0\), in kilopascals?',
            {'A': r'\(420\)', 'B': r'\(386.4\)', 'C': r'\(92\)', 'D': r'\(8\)'},
            'A',
            r'Tại \(t = 0\): \(P(0) = 420(0.92)^0 = 420\).',
            r'Hệ số đứng trước cơ số mũ là giá trị ban đầu tại \(t = 0\).',
            {
                'A': ('Đáp án đúng', r'\(P(0) = 420\).'),
                'B': ('Tính tại t = 1', r'\(386.4\) là áp suất sau 1 phút.'),
                'C': ('Nhầm cơ số %', r'92% là phần áp suất còn lại mỗi phút.'),
                'D': ('Nhầm tỉ lệ giảm %', r'8% là phần trăm giảm mỗi phút.'),
            },
            r'Thay `t = 0` vào `420 * 0.92^0 = 420`.'
        ),
        math_spr(
            'sat_mm5_m2l_q13', 13, 'Advanced Math', 'Nonlinear functions', 'Easy',
            r'<p>Consider the quadratic function \(y = (x + 4)^2 + 15\).</p>',
            r'What is the <b>minimum</b> possible value of \(y\)?',
            ['15'], '15',
            r'Vì \((x + 4)^2 \ge 0\) với mọi \(x\), giá trị nhỏ nhất của \(y\) là \(15\) đạt tại \(x = -4\).',
            r'Trong \(y = (x - h)^2 + k\), cực tiểu của \(y\) là \(k = 15\)!',
            r'Vẽ `y = (x + 4)^2 + 15` trên Desmos → bấm đỉnh `(-4, 15)` → giá trị nhỏ nhất là `15`.'
        ),
        math_mcq(
            'sat_mm5_m2l_q14', 14, 'Advanced Math', 'Equivalent expressions', 'Easy',
            r'<p>Which of the following is equivalent to \((x - 6)(x + 3)\)?</p>',
            r'Select the expanded form.',
            {'A': r'\(x^2 + 3x - 18\)', 'B': r'\(x^2 - 3x + 18\)', 'C': r'\(x^2 - 9x - 18\)', 'D': r'\(x^2 - 3x - 18\)'},
            'D',
            r'Nhân khai triển: \(x^2 + 3x - 6x - 18 = x^2 - 3x - 18\).',
            r'Hệ số giữa là \(-6 + 3 = -3\), hằng số tự do là \((-6)(3) = -18\).',
            {
                'A': ('Sai dấu hệ số x', r'\(-6 + 3 = -3\), không phải \(+3\).'),
                'B': ('Sai dấu hằng số', r'\((-6)(3) = -18\), không phải \(+18\).'),
                'C': ('Cộng thành -9x', r'Tính nhầm \(-6 - 3 = -9\).'),
                'D': ('Đáp án đúng', r'\(x^2 - 3x - 18\).'),
            },
            r'Vẽ `y = (x - 6)(x + 3)` và kiểm tra trùng khít với D trên Desmos.'
        ),
        math_mcq(
            'sat_mm5_m2l_q15', 15, 'Advanced Math', 'Nonlinear equations in one variable and systems of equations in two variables', 'Medium',
            r'<p>The area \(A\) of a triangular glass roof panel with base \(b\) and height \(h\) is given by \(A = \frac{1}{2}bh\).</p>',
            r'Which equation correctly expresses \(h\) in terms of \(A\) and \(b\)?',
            {'A': r'\(h = \frac{A}{2b}\)', 'B': r'\(h = 2Ab\)', 'C': r'\(h = \frac{2A}{b}\)', 'D': r'\(h = \frac{b}{2A}\)'},
            'C',
            r'Nhân hai vế với 2: \(2A = bh\). Chia hai vế cho \(b\): \(h = \frac{2A}{b}\).',
            r'Khử phân số \(\frac{1}{2}\) bằng cách nhân 2 cả hai vế trước khi chia cho \(b\).',
            {
                'A': ('Chia 2 thay vì nhân 2', r'Đưa số 2 nhầm xuống mẫu.'),
                'B': ('Nhân b thay vì chia b', r'Quên chia cho \(b\).'),
                'C': ('Đáp án đúng', r'\(h = \frac{2A}{b}\).'),
                'D': ('Nghịch đảo nhầm', r'Đảo ngược tử và mẫu.'),
            },
            r'Thử `b = 4, h = 5` → `A = 10`; chỉ phương án C cho `2(10)/4 = 5`!'
        ),
        math_spr(
            'sat_mm5_m2l_q16', 16, 'Problem-Solving and Data Analysis', 'Ratios, rates, proportional relationships, and units', 'Easy',
            r'<p>Twelve identical composite wind turbine blades have a combined mass of \(180\) kilograms.</p>',
            r'What is the combined mass, in kilograms, of \(20\) of these identical turbine blades?',
            ['300'], '300',
            r'Khối lượng 1 cánh quạt \(= \frac{180}{12} = 15\text{ kg}\). Vậy \(20\) cánh nặng \(20 \times 15 = 300\text{ kg}\).',
            r'Tính đơn vị 1 cánh trước (`15 kg`) rồi nhân với `20`.',
            r'Gõ `(180 / 12) * 20` trên Desmos ra ngay `300`.'
        ),
        math_mcq(
            'sat_mm5_m2l_q17', 17, 'Problem-Solving and Data Analysis', 'Percentages', 'Easy',
            r'<p>An alpine bridge engineering team inspected \(320\) steel cables, and \(45\%\) of them were upgraded with new sensors.</p>',
            r'How many steel cables were upgraded?',
            {'A': r'\(128\)', 'B': r'\(144\)', 'C': r'\(160\)', 'D': r'\(176\)'},
            'B',
            r'Tính \(45\% \text{ của } 320 = 0.45 \times 320 = 144\).',
            r'Đổi \(45\% = 0.45\) rồi nhân với \(320\).',
            {
                'A': ('Tính 40%', r'\(0.40 \times 320 = 128\).'),
                'B': ('Đáp án đúng', r'\(0.45 \times 320 = 144\).'),
                'C': ('Tính 50%', r'\(0.50 \times 320 = 160\).'),
                'D': ('Tính phần còn lại 55%', r'\(320 - 144 = 176\) là số cáp chưa nâng cấp.'),
            },
            r'Gõ `0.45 * 320` trên Desmos ra ngay `144`.'
        ),
        math_mcq(
            'sat_mm5_m2l_q18', 18, 'Problem-Solving and Data Analysis', 'One-variable data: Distributions and measures of center and spread', 'Easy',
            r'<p>Seven daily wind-speed averages, in knots, are listed below:</p><p style="text-align:center;">\[9,\; 14,\; 11,\; 22,\; 17,\; 13,\; 25\]</p>',
            r'What is the <b>median</b> of these seven wind-speed averages?',
            {'A': r'\(14\)', 'B': r'\(13\)', 'C': r'\(17\)', 'D': r'\(22\)'},
            'A',
            r'Sắp xếp tăng dần: \(9, 11, 13, \mathbf{14}, 17, 22, 25\). Giá trị đứng thứ 4 chính giữa là \(14\).',
            r'Luôn sắp xếp tăng dần trước khi chọn số đứng giữa (đừng lấy số thứ 4 chưa sắp là 22!).',
            {
                'A': ('Đáp án đúng', r'Trung vị của 7 số sau khi sắp xếp là \(14\).'),
                'B': ('Vị trí thứ 3', r'13 đứng thứ 3.'),
                'C': ('Vị trí thứ 5', r'17 đứng thứ 5.'),
                'D': ('Chưa sắp xếp dãy', r'22 chỉ là số thứ 4 của dãy lộn xộn ban đầu.'),
            },
            r'Gõ `median(9, 14, 11, 22, 17, 13, 25)` trên Desmos ra ngay `14`.'
        ),
        math_spr(
            'sat_mm5_m2l_q19', 19, 'Problem-Solving and Data Analysis', 'Probability and conditional probability', 'Medium',
            tbl_q19 + r'<p>The table above summarizes \(108\) optical lenses coated across two lab lines.</p>',
            r'If one lens is chosen at random from all \(108\) lenses, what is the probability that it has an <b>Anti-Glare</b> coating? (Enter as a fraction or decimal.)',
            ['1/4', '0.25', '.25'], '1/4 hoặc 0.25',
            r'Có \(27\) thấu kính Anti-Glare trên tổng \(108\) thấu kính. Xác suất: \(\frac{27}{108} = \frac{1}{4} = 0.25\).',
            r'Phân số rút gọn `1/4` hay thập phân `0.25` đều được chấm đúng 100%.',
            r'Gõ `27 / 108` trên Desmos ra `0.25` (hoặc `1/4`).'
        ),
        math_mcq(
            'sat_mm5_m2l_q20', 20, 'Geometry and Trigonometry', 'Lines, angles, and triangles', 'Easy',
            r'<p>Two interior angles of a triangle measure \(52^\circ\) and \(71^\circ\).</p>',
            r'What is the measure of the third interior angle, in degrees?',
            {'A': r'\(47^\circ\)', 'B': r'\(67^\circ\)', 'C': r'\(123^\circ\)', 'D': r'\(57^\circ\)'},
            'D',
            r'Tổng 3 góc tam giác bằng \(180^\circ\): \(180^\circ - (52^\circ + 71^\circ) = 180^\circ - 123^\circ = 57^\circ\).',
            r'Cộng hai góc rồi trừ khỏi \(180^\circ\).',
            {
                'A': ('Trừ sai 180 - 123', r'Nhầm hàng chục thành 47.'),
                'B': ('Trừ sai 180 - 123', r'Nhầm hàng chục thành 67.'),
                'C': ('Quên trừ khỏi 180°', r'123° là tổng 2 góc đã biết.'),
                'D': ('Đáp án đúng', r'\(180 - 123 = 57^\circ\).'),
            },
            r'Gõ `180 - 52 - 71` trên Desmos ra ngay `57`.'
        ),
        math_mcq(
            'sat_mm5_m2l_q21', 21, 'Geometry and Trigonometry', 'Circles', 'Easy',
            r'<p>A circular glass atrium dome has a radius of \(9\) meters.</p>',
            r'What is the <b>circumference</b> of the base of the dome, in meters?',
            {'A': r'\(9\pi\)', 'B': r'\(81\pi\)', 'C': r'\(18\pi\)', 'D': r'\(36\pi\)'},
            'C',
            r'Chu vi hình tròn: \(C = 2\pi r = 2\pi(9) = 18\pi\text{ m}\).',
            r'Đọc kỹ đề hỏi Chu vi (\(C = 2\pi r\)) chứ không phải Diện tích (\(\pi r^2 = 81\pi\))!',
            {
                'A': ('Quên nhân 2', r'\(9\pi\) thiếu hệ số 2.'),
                'B': ('Nhầm với diện tích πr²', r'\(81\pi\) là diện tích hình tròn.'),
                'C': ('Đáp án đúng', r'\(C = 2\pi(9) = 18\pi\).'),
                'D': ('Nhân 4 thay vì 2', r'Nhầm \(9\) là đường kính rồi nhân thêm.'),
            },
            r'Tra công thức Circle Circumference trong nút Reference: `C = 2 * pi * r = 18pi`.'
        ),
        math_spr(
            'sat_mm5_m2l_q22', 22, 'Geometry and Trigonometry', 'Area and volume', 'Easy',
            svg_q22 + r'<p>A right circular cylindrical glass column has a radius of \(4\) feet and a height of \(10\) feet.</p>',
            r'If the volume of the cylinder is \(k\pi\) cubic feet, what is the value of \(k\)?',
            ['160'], '160',
            r'Thể tích hình trụ: \(V = \pi r^2 h = \pi (4^2)(10) = 160\pi \Rightarrow k = 160\).',
            r'Nhớ bình phương bán kính \(r^2 = 16\) trước khi nhân chiều cao \(h = 10\)!',
            r'Gõ `4^2 * 10` trên Desmos ra ngay `160`.'
        ),
    ]
