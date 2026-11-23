# -*- coding: utf-8 -*-
"""
Digital SAT Math Adaptive Mock Test #3 — Module 2 (Standard/Lower Route, 300-600 Band)
22 Questions: 16 MCQ (A:4, B:4, C:4, D:4) + 6 SPR (Q5, Q9, Q13, Q16, Q19, Q22)
Domains: Algebra (Q1-Q8), Advanced Math (Q9-Q15),
         Problem-Solving and Data Analysis (Q16-Q19),
         Geometry and Trigonometry (Q20-Q22)
Difficulty: Easy -> Medium (Foundation-to-Standard Band)
IDs: sat_mm3_m2l_q1 .. sat_mm3_m2l_q22
"""

from fractions import Fraction
import math
from sat_math_helpers import (
    math_mcq,
    math_spr,
    build_math_table,
    svg_parabola_vertex,
    svg_parallel_transversal,
    svg_similar_triangles,
    svg_cylinder,
)


def get_m2l_questions():
    qs = []

    # =========================================================================
    # DOMAIN 1: ALGEBRA (Q1 - Q8)
    # =========================================================================

    # Q1 — MCQ (A) — Easy — Two-step linear equation (Museum art conservation)
    qs.append(math_mcq(
        'sat_mm3_m2l_q1', 1, 'Algebra', 'Linear Equations in One Variable', 'Easy',
        r'<p>A museum technician solves the linear equation below to determine the number of solvent vials \(x\) required for a restoration batch:</p><p style="text-align:center;">\[4x + 16 = 44\]</p>',
        r'<p>What is the value of \(x\)?</p>',
        {'A': r'7', 'B': r'15', 'C': r'28', 'D': r'60'},
        'A',
        '\n'.join([
            r'Bước 1: Trừ \(16\) ở cả hai vế: \(4x = 44 - 16 = 28\).',
            r'Bước 2: Chia cả hai vế cho \(4\): \(x = \frac{28}{4} = 7\).',
        ]),
        r'Để cô lập \(x\) trong phương trình dạng \(ax + b = c\), luôn khử hạng tử cộng/trừ \(b\) trước rồi mới chia cho hệ số \(a\).',
        {
            'A': ('Đáp án đúng', r'Thay \(x = 7\): \(4(7) + 16 = 28 + 16 = 44\), chính xác.'),
            'B': ('Sign Error', r'Cộng \(16\) thay vì trừ: \((44 + 16) \div 4 = 15\).'),
            'C': ('Forgot Final Division', r'Chỉ tính đến \(4x = 28\) mà quên chia cho \(4\).'),
            'D': ('Sign Error & Forgot Division', r'Cộng \(44 + 16 = 60\) và quên chia cho \(4\).'),
        },
        desmos_tip_vi=r'Gõ trực tiếp <code>4x + 16 = 44</code> trên Desmos rồi click vào đường thẳng đứng để đọc ngay <code>x = 7</code>.'
    ))

    # Q2 — MCQ (C) — Easy — Evaluating a linear function (Alpine sensor)
    qs.append(math_mcq(
        'sat_mm3_m2l_q2', 2, 'Algebra', 'Linear Functions', 'Easy',
        r'<p>The linear function \(f(x) = 3x + 14\) models the signal gain index of an alpine elevation sensor at calibration level \(x\).</p>',
        r'<p>What is the value of \(f(6)\)?</p>',
        {'A': r'20', 'B': r'23', 'C': r'32', 'D': r'60'},
        'C',
        '\n'.join([
            r'Bước 1: Thay \(x = 6\) vào công thức hàm số: \(f(6) = 3(6) + 14\).',
            r'Bước 2: Thực hiện phép nhân trước, cộng sau: \(18 + 14 = 32\).',
        ]),
        r'Ký hiệu \(f(6)\) có nghĩa là thay số \(6\) vào đúng vị trí của biến \(x\) và tuân thủ thứ tự phép toán (nhân trước, cộng sau).',
        {
            'A': ('Ignored Coefficient', r'Quên nhân với hệ số \(3\), chỉ tính \(6 + 14 = 20\).'),
            'B': ('Added Instead of Multiplied', r'Cộng \(3 + 6 + 14 = 23\) thay vì nhân \(3 \times 6\).'),
            'C': ('Đáp án đúng', r'\(3(6) + 14 = 18 + 14 = 32\).'),
            'D': ('Order of Operations Error', r'Cộng \(6 + 14 = 20\) trước rồi mới nhân \(3\), ra \(60\).'),
        },
        desmos_tip_vi=r'Gõ <code>f(x) = 3x + 14</code> ở dòng 1, rồi gõ <code>f(6)</code> ở dòng 2 để Desmos trả về <code>32</code>.'
    ))

    # Q3 — MCQ (B) — Easy — Slope from two points (Semiconductor wafer calibration)
    qs.append(math_mcq(
        'sat_mm3_m2l_q3', 3, 'Algebra', 'Slope of a Line', 'Easy',
        r'<p>In the \(xy\)-plane, a calibration line for a semiconductor wafer etcher passes through the points \((2, 5)\) and \((6, 17)\).</p>',
        r'<p>What is the slope of this line?</p>',
        {'A': r'\(\frac{1}{3}\)', 'B': r'3', 'C': r'4', 'D': r'12'},
        'B',
        '\n'.join([
            r'Bước 1: Áp dụng công thức hệ số góc: \(m = \frac{y_2 - y_1}{x_2 - x_1}\).',
            r'Bước 2: Thay tọa độ hai điểm: \(m = \frac{17 - 5}{6 - 2} = \frac{12}{4} = 3\).',
        ]),
        r'Hệ số góc luôn là "Rise over Run" (\(\frac{\Delta y}{\Delta x}\), tung độ trên tử, hoành độ dưới mẫu) — không bao giờ đảo ngược \(\frac{\Delta x}{\Delta y}\).',
        {
            'A': ('Inverted Slope Formula', r'Chia ngược \(\frac{\Delta x}{\Delta y} = \frac{4}{12} = \frac{1}{3}\).'),
            'B': ('Đáp án đúng', r'\(\frac{17 - 5}{6 - 2} = \frac{12}{4} = 3\).'),
            'C': ('Computed Run Only', r'Chỉ tính độ lệch hoành độ \(\Delta x = 6 - 2 = 4\).'),
            'D': ('Computed Rise Only', r'Chỉ tính độ lệch tung độ \(\Delta y = 17 - 5 = 12\) mà quên chia cho \(4\).'),
        },
        desmos_tip_vi=r'Gõ trực tiếp phân số <code>(17 - 5) / (6 - 2)</code> trên Desmos để có ngay <code>3</code>.'
    ))

    # Q4 — MCQ (D) — Easy — Building a linear model (Museum archive)
    qs.append(math_mcq(
        'sat_mm3_m2l_q4', 4, 'Algebra', 'Linear Models in Context', 'Easy',
        r'<p>A museum art archive starts with \(140\) cataloged oil sketches and restores \(12\) additional oil sketches each month.</p>',
        r'<p>Which equation gives the total number of restored oil sketches \(S\) in the archive after \(m\) months?</p>',
        {
            'A': r'\(S = 140m + 12\)',
            'B': r'\(S = 140 - 12m\)',
            'C': r'\(S = 152m\)',
            'D': r'\(S = 12m + 140\)',
        },
        'D',
        '\n'.join([
            r'Bước 1: Giá trị ban đầu (tại \(m = 0\)) là \(140\) bức tranh \(\Rightarrow\) hằng số tự do \(b = 140\).',
            r'Bước 2: Tốc độ tăng đều mỗi tháng ("each month") là \(+12\) bức \(\Rightarrow\) hệ số góc nhân với \(m\) là \(12m\).',
            r'Bước 3: Ghép lại: \(S = 12m + 140\).',
        ]),
        r'Trong bài toán mô hình tuyến tính: đại lượng có từ "each / per" luôn gắn liền với biến số (slope), còn số lượng "starts with / initial" là hằng số cộng thêm (y-intercept).',
        {
            'A': ('Slope-Intercept Swap', r'Đổi chỗ sai giữa số lượng ban đầu (\(140\)) và tốc độ mỗi tháng (\(12\)).'),
            'B': ('Sign Error', r'Dùng dấu trừ mặc dù số tranh phục chế đang tăng thêm mỗi tháng.'),
            'C': ('Combined Constant and Rate', r'Cộng gộp \(140 + 12 = 152\) rồi nhân cả hai với \(m\).'),
            'D': ('Đáp án đúng', r'Khớp đúng: tại \(m = 0\) có \(140\) bức, mỗi tháng tăng thêm \(12\) bức.'),
        },
        desmos_tip_vi=r'Kiểm tra nhanh tại <code>m = 1</code> tháng: phải có <code>140 + 12 = 152</code> bức; tại <code>m = 2</code> phải có <code>164</code> bức — chỉ đáp án D khớp cả hai!'
    ))

    # Q5 — SPR (17) — Easy — Simple linear system by elimination (Athletic biomechanics)
    qs.append(math_spr(
        'sat_mm3_m2l_q5', 5, 'Algebra', 'Systems of Two Linear Equations', 'Easy',
        r'<p>In an athletic biomechanics load test, two vertical force indices \(x\) and \(y\) satisfy the system of equations:</p><p style="text-align:center;">\[x + y = 26\]\[x - y = 8\]</p>',
        r'<p>What is the value of \(x\)?</p>',
        ['17'],
        '17',
        '\n'.join([
            r'Bước 1: Cộng vế theo vế hai phương trình để khử ngay \(y\): \((x + y) + (x - y) = 26 + 8 \Rightarrow 2x = 34\).',
            r'Bước 2: Chia hai vế cho \(2\): \(x = 17\) (và \(y = 26 - 17 = 9\)).',
            r'Bước 3: Kiểm tra lại: \(17 + 9 = 26\) và \(17 - 9 = 8\).',
        ]),
        r'Khi một hệ có dạng \(x + y = S\) và \(x - y = D\), cộng hai phương trình lập tức cho \(x = \frac{S + D}{2}\) trong 3 giây!',
        desmos_tip_vi=r'Gõ <code>x + y = 26</code> và <code>x - y = 8</code> trên Desmos rồi click giao điểm để đọc tọa độ <code>(17, 9)</code>.'
    ))

    # Q6 — MCQ (B) — Easy-Medium — Linear inequality in one variable (Municipal water reservoir)
    qs.append(math_mcq(
        'sat_mm3_m2l_q6', 6, 'Algebra', 'Linear Inequalities in One Variable', 'Easy',
        r'<p>A municipal water reservoir pump operator must keep the valve pressure setting \(p\) within the safety condition:</p><p style="text-align:center;">\[3p - 7 \le 20\]</p>',
        r'<p>What is the greatest possible value of \(p\)?</p>',
        {'A': r'\(\frac{13}{3}\)', 'B': r'9', 'C': r'13', 'D': r'27'},
        'B',
        '\n'.join([
            r'Bước 1: Cộng \(7\) vào cả hai vế của bất phương trình: \(3p \le 20 + 7 \Rightarrow 3p \le 27\).',
            r'Bước 2: Chia cả hai vế cho \(3\) (số dương nên giữ nguyên chiều): \(p \le 9\).',
            r'Bước 3: Giá trị lớn nhất có thể của \(p\) là \(9\).',
        ]),
        r'Giải bất phương trình bậc nhất giống hệt giải phương trình (chỉ cần nhớ đảo chiều nếu nhân hoặc chia cho số âm).',
        {
            'A': ('Sign Error', r'Trừ \(7\) khỏi \(20\) thay vì cộng \(7\), ra \(3p \le 13 \Rightarrow p \le \frac{13}{3}\).'),
            'B': ('Đáp án đúng', r'Tại \(p = 9\): \(3(9) - 7 = 20 \le 20\), là giá trị lớn nhất hợp lệ.'),
            'C': ('Sign Error & Forgot Division', r'Tính nhầm \(20 - 7 = 13\) và dừng lại.'),
            'D': ('Forgot Final Division', r'Chỉ giải đến \(3p \le 27\) mà quên chia cho \(3\).'),
        },
        desmos_tip_vi=r'Gõ <code>3x - 7 <= 20</code> trên Desmos — ranh giới bên phải của miền tô màu nằm đúng tại đường thẳng <code>x = 9</code>.'
    ))

    # Q7 — MCQ (D) — Medium — Parallel line equation (Alpine ridge survey)
    qs.append(math_mcq(
        'sat_mm3_m2l_q7', 7, 'Algebra', 'Parallel Lines in the xy-Plane', 'Medium',
        r'<p>In the \(xy\)-plane, line \(k\) models an alpine cable-car reference path with equation \(y = -4x + 5\). Line \(m\) is parallel to line \(k\) and passes through the point \((0, -3)\).</p>',
        r'<p>Which of the following is an equation of line \(m\)?</p>',
        {
            'A': r'\(y = 4x - 3\)',
            'B': r'\(y = \frac{1}{4}x - 3\)',
            'C': r'\(y = -4x + 3\)',
            'D': r'\(y = -4x - 3\)',
        },
        'D',
        '\n'.join([
            r'Bước 1: Hai đường thẳng song song có <b>cùng hệ số góc</b>. Vì đường thẳng \(k\) có \(m = -4\), đường thẳng \(m\) cũng có hệ số góc \(-4\).',
            r'Bước 2: Đường thẳng \(m\) đi qua \((0, -3)\), đây chính là tung độ gốc \(b = -3\).',
            r'Bước 3: Ghép dạng slope-intercept \(y = mx + b\): \(y = -4x - 3\).',
        ]),
        r'Song song (parallel) = giữ nguyên hệ số góc \(m\); vuông góc (perpendicular) = nghịch đảo đối dấu \(-\frac{1}{m}\). Luôn đọc kỹ từ khóa "parallel" hay "perpendicular"!',
        {
            'A': ('Sign Error on Slope', r'Đổi dấu hệ số góc từ \(-4\) thành \(+4\).'),
            'B': ('Parallel vs. Perpendicular Confusion', r'Dùng hệ số góc vuông góc \(\frac{1}{4}\) thay vì hệ số góc song song \(-4\).'),
            'C': ('Sign Error on Intercept', r'Viết nhầm tung độ gốc \(+3\) thay vì \(-3\).'),
            'D': ('Đáp án đúng', r'Cùng hệ số góc \(-4\) và cắt trục tung tại \((0, -3)\).'),
        },
        desmos_tip_vi=r'Vẽ <code>y = -4x + 5</code>, điểm <code>(0, -3)</code> và đồ thị <code>y = -4x - 3</code> để thấy hai đường song song hoàn toàn.'
    ))

    # Q8 — MCQ (A) — Medium — Word-problem linear system (Museum auction tickets)
    qs.append(math_mcq(
        'sat_mm3_m2l_q8', 8, 'Algebra', 'Systems of Linear Equations in Context', 'Medium',
        r'<p>At a museum benefit auction, general admission tickets cost $25 each and VIP preview tickets cost $60 each. A patron purchased a total of \(8\) tickets for $305.</p>',
        r'<p>How many VIP preview tickets did the patron purchase?</p>',
        {'A': r'3', 'B': r'4', 'C': r'5', 'D': r'6'},
        'A',
        '\n'.join([
            r'Bước 1: Gọi \(g\) là số vé thường và \(v\) là số vé VIP. Ta có hệ phương trình:',
            r'\[g + v = 8 \quad \text{và} \quad 25g + 60v = 305\]',
            r'Bước 2: Thế \(g = 8 - v\) vào phương trình tổng tiền: \(25(8 - v) + 60v = 305\).',
            r'Bước 3: Rút gọn: \(200 - 25v + 60v = 305 \Rightarrow 35v = 105 \Rightarrow v = 3\) vé VIP.',
        ]),
        r'Khi giải hệ bài toán đố, hãy đặt tên biến gợi nhớ (\(g\) cho general, \(v\) cho VIP) để không bao giờ trả nhầm số vé thường \(g = 5\) thay cho số vé VIP \(v = 3\)!',
        {
            'A': ('Đáp án đúng', r'\(3\) vé VIP ($180) + \(5\) vé thường ($125) = \(8\) vé, tổng $305.'),
            'B': ('Half-Split Guess', r'Chia đôi số vé \(4 + 4\) cho tổng \(4(25) + 4(60) = \$340 \ne \$305\).'),
            'C': ('Wrong Variable', r'Đây là số vé thường (\(g = 5\)), không phải số vé VIP mà đề bài yêu cầu!'),
            'D': ('Overestimation Error', r'Chỉ riêng \(6\) vé VIP đã tốn $360, vượt quá tổng chi $305.'),
        },
        desmos_tip_vi=r'Gõ <code>x + y = 8</code> và <code>25x + 60y = 305</code> (với <code>y</code> là vé VIP) rồi click giao điểm <code>(5, 3)</code> \(\Rightarrow y = 3\).'
    ))

    # =========================================================================
    # DOMAIN 2: ADVANCED MATH (Q9 - Q15)
    # =========================================================================

    # Q9 — SPR (21) — Easy — Evaluating a quadratic function (Athletic biomechanics)
    qs.append(math_spr(
        'sat_mm3_m2l_q9', 9, 'Advanced Math', 'Quadratic Function Evaluation', 'Easy',
        r'<p>In an athletic biomechanics sprint-power model, the function \(h\) is defined by:</p><p style="text-align:center;">\[h(t) = 2t^2 - 5t + 9\]</p>',
        r'<p>What is the value of \(h(4)\)?</p>',
        ['21'],
        '21',
        '\n'.join([
            r'Bước 1: Thay \(t = 4\) vào hàm số: \(h(4) = 2(4)^2 - 5(4) + 9\).',
            r'Bước 2: Tính lũy thừa trước: \(4^2 = 16 \Rightarrow 2(16) - 20 + 9 = 32 - 20 + 9 = 21\).',
        ]),
        r'Thứ tự ưu tiên phép tính (PEMDAS): luôn tính bình phương \(4^2 = 16\) trước khi nhân với \(2\) (tránh sai thành \((2 \times 4)^2 = 64\)).',
        desmos_tip_vi=r'Gõ <code>h(x) = 2x^2 - 5x + 9</code> rồi dòng dưới gõ <code>h(4)</code> để Desmos tính tức thì ra <code>21</code>.'
    ))

    # Q10 — MCQ (D) — Easy — Laws of exponents (Semiconductor wafer)
    qs.append(math_mcq(
        'sat_mm3_m2l_q10', 10, 'Advanced Math', 'Laws of Exponents', 'Easy',
        r'<p>For \(x > 0\), consider the algebraic expression used to scale a semiconductor wafer area factor:</p><p style="text-align:center;">\[(3x^4)^2 \cdot x^3\]</p>',
        r'<p>Which of the following is equivalent to this expression?</p>',
        {
            'A': r'\(6x^9\)',
            'B': r'\(9x^9\)',
            'C': r'\(6x^{11}\)',
            'D': r'\(9x^{11}\)',
        },
        'D',
        '\n'.join([
            r'Bước 1: Áp dụng quy tắc lũy thừa của một tích \((ab)^n = a^n b^n\) và \((x^m)^n = x^{mn}\):',
            r'\[(3x^4)^2 = 3^2 \cdot (x^4)^2 = 9x^8\]',
            r'Bước 2: Nhân với \(x^3\) bằng quy tắc cộng số mũ cùng cơ số \(x^a \cdot x^b = x^{a+b}\):',
            r'\[9x^8 \cdot x^3 = 9x^{8+3} = 9x^{11}\]',
        ]),
        r'Phân biệt rõ hai quy tắc lũy thừa: lũy thừa tầng \((x^4)^2\) thì <b>NHÂN số mũ</b> (\(x^8\)) và bình phương cả hệ số (\(3^2 = 9\)); nhân hai lũy thừa cùng cơ số \(x^8 \cdot x^3\) thì <b>CỘNG số mũ</b> (\(x^{11}\)).',
        {
            'A': ('Multiple Exponent Errors', r'Nhân nhầm \(3 \times 2 = 6\) và cộng nhầm số mũ \(4 + 2 + 3 = 9\).'),
            'B': ('Added Power-of-Power Exponents', r'Tính đúng \(3^2 = 9\) nhưng cộng \(4 + 2 = 6\) thay vì nhân \(4 \times 2 = 8\), dẫn đến \(x^9\).'),
            'C': ('Forgot to Square Coefficient', r'Tính đúng \(x^{11}\) nhưng nhân \(3 \times 2 = 6\) thay vì \(3^2 = 9\).'),
            'D': ('Đáp án đúng', r'\(3^2 \cdot x^{4 \cdot 2} \cdot x^3 = 9x^{11}\).'),
        },
        desmos_tip_vi=r'Thử thay <code>x = 2</code>: <code>(3*2^4)^2 * 2^3 = 18432</code>; kiểm tra 4 đáp án tại <code>x = 2</code>, chỉ <code>9*2^11 = 18432</code> khớp!'
    ))

    # Q11 — MCQ (C) — Easy-Medium — Expanding binomial product
    qs.append(math_mcq(
        'sat_mm3_m2l_q11', 11, 'Advanced Math', 'Expanding Polynomial Products', 'Easy',
        r'<p>Consider the product of two linear expressions:</p><p style="text-align:center;">\[(x + 7)(x - 3)\]</p>',
        r'<p>Which of the following is equivalent to the expression above?</p>',
        {
            'A': r'\(x^2 - 4x - 21\)',
            'B': r'\(x^2 + 4x + 21\)',
            'C': r'\(x^2 + 4x - 21\)',
            'D': r'\(x^2 + 10x - 21\)',
        },
        'C',
        '\n'.join([
            r'Bước 1: Áp dụng quy tắc phân phối FOIL:',
            r'\[(x + 7)(x - 3) = x^2 - 3x + 7x - 21\]',
            r'Bước 2: Gộp các hạng tử đồng dạng: \(-3x + 7x = +4x\), thu được \(x^2 + 4x - 21\).',
        ]),
        r'Khi khai triển \((x + a)(x + b)\), hệ số của \(x\) là tổng đại số \(a + b\) (\(7 + (-3) = +4\)) và hằng số tự do là tích \(a \cdot b\) (\(7 \times (-3) = -21\)).',
        {
            'A': ('Sign Error on Middle Term', r'Tính nhầm \(7x - 3x\) thành \(-4x\).'),
            'B': ('Sign Error on Constant', r'Nhân nhầm \((+7)(-3)\) thành \(+21\) thay vì \(-21\).'),
            'C': ('Đáp án đúng', r'\(x^2 + (7 - 3)x + (7)(-3) = x^2 + 4x - 21\).'),
            'D': ('Added Magnitudes Instead of Signed Terms', r'Cộng \(7 + 3 = 10\) cho hệ số \(x\) mà bỏ quên dấu trừ trước số \(3\).'),
        },
        desmos_tip_vi=r'Gõ <code>f(x) = (x + 7)(x - 3)</code> và từng đáp án trên Desmos — chỉ <code>y = x^2 + 4x - 21</code> trùng khít đồ thị 100%.'
    ))

    # Q12 — MCQ (B) — Medium — Solving a quadratic equation by factoring
    qs.append(math_mcq(
        'sat_mm3_m2l_q12', 12, 'Advanced Math', 'Solving Quadratic Equations', 'Medium',
        r'<p>Consider the quadratic equation:</p><p style="text-align:center;">\[x^2 - 3x - 28 = 0\]</p>',
        r'<p>What is the positive solution to this equation?</p>',
        {'A': r'4', 'B': r'7', 'C': r'14', 'D': r'28'},
        'B',
        '\n'.join([
            r'Bước 1: Tìm hai số có tích bằng \(-28\) và tổng bằng \(-3\): đó là \(-7\) và \(+4\).',
            r'Bước 2: Phân tích thành nhân tử: \((x - 7)(x + 4) = 0\).',
            r'Bước 3: Hai nghiệm là \(x = 7\) và \(x = -4\). Nghiệm dương là \(x = 7\).',
        ]),
        r'Khi giải \((x - r)(x + s) = 0\), luôn đảo dấu số trong ngoặc để đọc nghiệm (\(x - 7 = 0 \Rightarrow x = +7\)), và đọc kỹ đề hỏi nghiệm dương ("positive solution").',
        {
            'A': ('Sign Reversal Error', r'Đổi dấu sai khi phân tích \((x + 7)(x - 4) = 0\), dẫn đến chọn nhầm nghiệm dương là \(4\).'),
            'B': ('Đáp án đúng', r'Thay \(x = 7\): \(7^2 - 3(7) - 28 = 49 - 21 - 28 = 0\).'),
            'C': ('Halved Constant Error', r'Lấy nhầm \(28 \div 2 = 14\); kiểm tra: \(14^2 - 42 - 28 \ne 0\).'),
            'D': ('Constant Term Trap', r'Nhầm hằng số tự do \(28\) là nghiệm của phương trình.'),
        },
        desmos_tip_vi=r'Vẽ <code>y = x^2 - 3x - 28</code> trên Desmos rồi click vào giao điểm trục \(x\) nằm bên phải trục tung: <code>(7, 0)</code>.'
    ))

    # Q13 — SPR (9) — Medium — Vertex form of a parabola (SVG parabola)
    svg_q13 = svg_parabola_vertex(
        h_lbl='h', k_lbl='k', opens_up=True,
        note='Graph of y = 3(x - 5)² + 4 (not to scale)'
    )
    qs.append(math_spr(
        'sat_mm3_m2l_q13', 13, 'Advanced Math', 'Quadratic Vertex Form', 'Medium',
        rf'<div style="display:flex;justify-content:center;margin:8px 0 12px;">{svg_q13}</div><p>In the \(xy\)-plane, the parabola with equation \(y = 3(x - 5)^2 + 4\) has its vertex at the point \((h, k)\).</p>',
        r'<p>What is the value of \(h + k\)?</p>',
        ['9'],
        '9',
        '\n'.join([
            r'Bước 1: Đối chiếu với dạng chuẩn đỉnh parabol \(y = a(x - h)^2 + k\):',
            r'• \(h = 5\) (chú ý dấu trừ trong \((x - 5)^2\) nên \(h = +5\), không phải \(-5\)).',
            r'• \(k = 4\).',
            r'Bước 2: Tính tổng: \(h + k = 5 + 4 = 9\).',
        ]),
        r'Trong dạng đỉnh \(y = a(x - h)^2 + k\): hoành độ đỉnh \(h\) luôn <b>ngược dấu</b> với số trong ngoặc, còn tung độ đỉnh \(k\) giữ <b>nguyên dấu</b> số ngoài ngoặc!',
        desmos_tip_vi=r'Gõ <code>y = 3(x - 5)^2 + 4</code> trên Desmos, click vào đáy parabol để đọc tọa độ đỉnh <code>(5, 4)</code> rồi cộng <code>5 + 4 = 9</code>.'
    ))

    # Q14 — MCQ (A) — Medium — Exponential growth evaluation (Alpine sensor network)
    qs.append(math_mcq(
        'sat_mm3_m2l_q14', 14, 'Advanced Math', 'Exponential Growth Models', 'Medium',
        r'<p>An alpine meteorology network initially deploys \(80\) elevation sensor nodes. The number of active nodes \(N(t)\) after \(t\) years is modeled by the exponential function:</p><p style="text-align:center;">\[N(t) = 80(2)^{\frac{t}{2}}\]</p>',
        r'<p>According to this model, how many active sensor nodes will be in the network after \(6\) years?</p>',
        {'A': r'640', 'B': r'960', 'C': r'2,560', 'D': r'5,120'},
        'A',
        '\n'.join([
            r'Bước 1: Thay \(t = 6\) vào hàm số: \(N(6) = 80 \cdot 2^{\frac{6}{2}} = 80 \cdot 2^3\).',
            r'Bước 2: Tính lũy thừa \(2^3 = 8\), sau đó nhân: \(80 \times 8 = 640\) cảm biến.',
        ]),
        r'Đừng quên chia thời gian \(t\) cho chu kỳ nhân đôi (mẫu số \(2\)) trước khi tính lũy thừa: \(6\) năm tương ứng \(3\) chu kỳ nhân đôi (\(2^3 = 8\)), không phải \(2^6 = 64\).',
        {
            'A': ('Đáp án đúng', r'\(80 \times 2^{6/2} = 80 \times 8 = 640\).'),
            'B': ('Linear Multiplication Trap', r'Nhân tuyến tính \(80 \times 2 \times 6 = 960\) thay vì tính lũy thừa.'),
            'C': ('Off-by-One Exponent', r'Tính nhầm số mũ thành \(2^5 = 32 \Rightarrow 80 \times 32 = 2,560\).'),
            'D': ('Ignored Period Denominator', r'Quên chia \(6\) cho \(2\), tính thành \(80 \times 2^6 = 80 \times 64 = 5,120\).'),
        },
        desmos_tip_vi=r'Gõ thẳng <code>80 * 2^(6/2)</code> vào Desmos để nhận ngay kết quả chính xác <code>640</code>.'
    ))

    # Q15 — MCQ (C) — Medium — Solving a simple radical equation
    qs.append(math_mcq(
        'sat_mm3_m2l_q15', 15, 'Advanced Math', 'Radical Equations', 'Medium',
        r'<p>Consider the equation:</p><p style="text-align:center;">\[\sqrt{2x + 7} = 5\]</p>',
        r'<p>What is the value of \(x\)?</p>',
        {'A': r'-1', 'B': r'6', 'C': r'9', 'D': r'16'},
        'C',
        '\n'.join([
            r'Bước 1: Bình phương cả hai vế để khử dấu căn bậc hai: \(2x + 7 = 5^2 = 25\).',
            r'Bước 2: Trừ \(7\) hai vế: \(2x = 18\).',
            r'Bước 3: Chia \(2\) hai vế: \(x = 9\). Kiểm tra: \(\sqrt{2(9) + 7} = \sqrt{25} = 5\) (đúng!).',
        ]),
        r'Khi khử căn bậc hai \(\sqrt{A} = c\), phải bình phương vế phải thành \(c^2\) rồi mới giải phương trình bậc nhất.',
        {
            'A': ('Forgot to Square RHS', r'Bỏ dấu căn mà quên bình phương số \(5\): \(2x + 7 = 5 \Rightarrow x = -1\).'),
            'B': ('Forgot to Square & Sign Error', r'Giải nhầm \(2x = 5 + 7 = 12 \Rightarrow x = 6\).'),
            'C': ('Đáp án đúng', r'\(\sqrt{2(9) + 7} = \sqrt{25} = 5\).'),
            'D': ('Sign Error', r'Cộng \(7\) thay vì trừ \(7\) sau khi bình phương: \((25 + 7) \div 2 = 16\).'),
        },
        desmos_tip_vi=r'Vẽ <code>y = sqrt(2x + 7)</code> và <code>y = 5</code> trên Desmos rồi click giao điểm để đọc ngay <code>(9, 5)</code>.'
    ))

    # =========================================================================
    # DOMAIN 3: PROBLEM-SOLVING AND DATA ANALYSIS (Q16 - Q19)
    # =========================================================================

    # Q16 — SPR (1020) — Easy-Medium — Basic percentages (Museum art auction)
    qs.append(math_spr(
        'sat_mm3_m2l_q16', 16, 'Problem-Solving and Data Analysis', 'Percentages', 'Easy',
        r'<p>A framed architectural etching at a museum auction has an estimated value of $850. At the sale, the winning bid is \(120\%\) of its estimated value.</p>',
        r'<p>What is the winning bid, in dollars?</p>',
        ['1020'],
        '1020',
        '\n'.join([
            r'Bước 1: Đổi \(120\%\) sang số thập phân: \(120\% = \frac{120}{100} = 1.20\).',
            r'Bước 2: Nhân với giá ước tính: \(850 \times 1.20 = 1,020\) đô la.',
            r'(Hoặc nhẩm nhanh: \(20\%\) của \(850\) là \(170\), cộng thêm \(850 + 170 = 1,020\).)',
        ]),
        r'Cụm từ "\(p\%\) of \(X\)" luôn dịch thẳng sang phép nhân \(\frac{p}{100} \times X\). Với \(p > 100\), kết quả chắc chắn lớn hơn giá gốc \(X\).',
        desmos_tip_vi=r'Gõ <code>850 * 1.20</code> (hoặc <code>120% of 850</code>) trên Desmos để có ngay <code>1020</code>.'
    ))

    # Q17 — MCQ (B) — Easy-Medium — Unit rate & proportional table (Semiconductor wafer)
    tbl_q17 = build_math_table(
        ['Shift', 'Duration (hours)', 'Wafers Inspected'],
        [
            ['Shift 1', '4', '180'],
            ['Shift 2', '6', '270'],
            ['Shift 3', '8', '360'],
        ],
        caption='Semiconductor Wafer Optical Inspection Output'
    )
    qs.append(math_mcq(
        'sat_mm3_m2l_q17', 17, 'Problem-Solving and Data Analysis', 'Ratios, Rates & Proportional Relationships', 'Easy',
        rf'<p>The table below shows the number of silicon wafers inspected during three shifts at a semiconductor facility operating at a constant inspection rate.</p>{tbl_q17}',
        r'<p>At this same constant rate, how many silicon wafers will be inspected during a \(10\)-hour shift?</p>',
        {'A': r'405', 'B': r'450', 'C': r'540', 'D': r'630'},
        'B',
        '\n'.join([
            r'Bước 1: Tính tốc độ kiểm tra mỗi giờ (unit rate): \(\frac{180}{4} = 45\) wafer/giờ (kiểm tra ca 2 và ca 3: \(\frac{270}{6} = 45\), \(\frac{360}{8} = 45\)).',
            r'Bước 2: Nhân với \(10\) giờ: \(45 \times 10 = 450\) tấm wafer.',
        ]),
        r'Với bảng dữ liệu tỉ lệ thuận, luôn tìm đơn giá/tốc độ cho \(1\) đơn vị thời gian trước (\(\text{Rate} = \frac{\text{Sản lượng}}{\text{Giờ}}\)) rồi nhân với thời gian mới.',
        {
            'A': ('Arithmetic Error', r'Nhân nhầm \(45 \times 9 = 405\) thay vì \(10\) giờ.'),
            'B': ('Đáp án đúng', r'\(45\text{ wafer/giờ} \times 10\text{ giờ} = 450\) tấm wafer.'),
            'C': ('Wrong Multiplier', r'Tính nhầm \(45 \times 12 = 540\) (hoặc nhân đôi ca \(6\) giờ).'),
            'D': ('Summed Two Rows Trap', r'Cộng nhầm sản lượng của ca \(6\) giờ và ca \(8\) giờ (\(270 + 360 = 630\), ứng với \(14\) giờ).'),
        },
        desmos_tip_vi=r'Gõ <code>(180 / 4) * 10</code> trên Desmos để có ngay <code>450</code>.'
    ))

    # Q18 — MCQ (A) — Medium — Median of an unsorted data table (Alpine meteorology)
    tbl_q18 = build_math_table(
        ['Day', 'Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5', 'Day 6', 'Day 7'],
        [
            ['Midday Temp (°C)', '4', '7', '3', '11', '7', '6', '18'],
        ],
        caption='Midday Air Temperatures at Alpine Base Camp Over 7 Days'
    )
    qs.append(math_mcq(
        'sat_mm3_m2l_q18', 18, 'Problem-Solving and Data Analysis', 'Center & Spread (Median vs. Mean)', 'Medium',
        rf'<p>The table below records the midday air temperatures, in degrees Celsius, at an alpine base camp for \(7\) consecutive days.</p>{tbl_q18}',
        r'<p>What is the median midday air temperature, in degrees Celsius, for these \(7\) days?</p>',
        {'A': r'7', 'B': r'8', 'C': r'11', 'D': r'15'},
        'A',
        '\n'.join([
            r'Bước 1: <b>BẮT BUỘC sắp xếp</b> \(7\) số liệu theo thứ tự tăng dần: \(3,\; 4,\; 6,\; \mathbf{7},\; 7,\; 11,\; 18\).',
            r'Bước 2: Với \(7\) giá trị, trung vị (median) nằm ở vị trí chính giữa là vị trí thứ \(\frac{7 + 1}{2} = 4\).',
            r'Bước 3: Giá trị thứ \(4\) trong dãy đã sắp xếp là \(7^\circ\text{C}\).',
        ]),
        r'Bẫy số 1 của câu Median trên SAT: học sinh vội lấy luôn số ở cột giữa bảng (Day 4 = \(11\)) mà quên <b>sắp xếp dãy số từ bé đến lớn</b> trước!',
        {
            'A': ('Đáp án đúng', r'Dãy tăng dần \(3, 4, 6, 7, 7, 11, 18\) có số đứng giữa là \(7\).'),
            'B': ('Mean Instead of Median', r'Tính trung bình cộng \(\frac{56}{7} = 8\) thay vì trung vị.'),
            'C': ('Unsorted Middle Value Trap', r'Chọn thẳng giá trị ở ngày thứ \(4\) (\(11^\circ\text{C}\)) mà quên sắp xếp thứ tự tăng dần!'),
            'D': ('Range Instead of Median', r'Tính khoảng biến thiên \(\max - \min = 18 - 3 = 15\).'),
        },
        desmos_tip_vi=r'Gõ thẳng hàm <code>median(4, 7, 3, 11, 7, 6, 18)</code> trên Desmos — Desmos tự động sắp xếp và trả về ngay <code>7</code>!'
    ))

    # Q19 — SPR (3/10 or 0.3) — Medium — Joint probability from two-way table (Athletic biomechanics)
    tbl_q19 = build_math_table(
        ['Event Group', 'Forefoot Strike', 'Heel Strike', 'Total'],
        [
            ['Sprint', '28', '12', '40'],
            ['Distance', '16', '24', '40'],
            ['<b>Total</b>', '<b>44</b>', '<b>36</b>', '<b>80</b>'],
        ],
        caption='Foot-Strike Patterns of 80 Track Athletes'
    )
    qs.append(math_spr(
        'sat_mm3_m2l_q19', 19, 'Problem-Solving and Data Analysis', 'Two-Way Tables & Probability', 'Medium',
        rf'<p>In an athletic biomechanics study, \(80\) track athletes were classified by event group and foot-strike pattern, as shown in the table below.</p>{tbl_q19}',
        r'<p>If one athlete is selected at random from all \(80\) athletes, what is the probability that the athlete is in the distance group and has a heel strike? (Express your answer as a decimal or simplified fraction.)</p>',
        ['3/10', '0.3', '.3'],
        '3/10 (hoặc 0.3)',
        '\n'.join([
            r'Bước 1: Không gian mẫu là <b>tất cả \(80\) vận động viên</b> ("from all 80 athletes") \(\Rightarrow\) mẫu số là \(80\).',
            r'Bước 2: Tìm ô giao giữa hàng <b>Distance</b> và cột <b>Heel Strike</b>: có \(24\) vận động viên.',
            r'Bước 3: Xác suất cần tìm là \(\frac{24}{80} = \frac{3}{10} = 0.3\).',
        ]),
        r'Khi đề nói "selected at random from all 80...", mẫu số là tổng toàn bảng (\(80\)); còn khi giới hạn vào một hàng/cột cụ thể thì mẫu số mới thu hẹp theo hàng/cột đó.',
        desmos_tip_vi=r'Gõ <code>24 / 80</code> trên Desmos để có ngay <code>0.3</code> (nhấn biểu tượng phân số sẽ đổi sang <code>3/10</code>).'
    ))

    # =========================================================================
    # DOMAIN 4: GEOMETRY AND TRIGONOMETRY (Q20 - Q22)
    # =========================================================================

    # Q20 — MCQ (D) — Easy-Medium — Parallel lines & corresponding angles (SVG)
    svg_q20 = svg_parallel_transversal(
        line1='ℓ', line2='m', ang1_lbl='(x - 16)°', ang2_lbl='124°', ang3_lbl='',
        note='Note: Figure not drawn to scale.'
    )
    qs.append(math_mcq(
        'sat_mm3_m2l_q20', 20, 'Geometry and Trigonometry', 'Lines, Angles & Parallel Transversals', 'Easy',
        rf'<div style="display:flex;justify-content:center;margin:8px 0 12px;">{svg_q20}</div><p>In the figure shown above, line \(\ell\) is parallel to line \(m\) and both are intersected by a transversal.</p>',
        r'<p>What is the value of \(x\)?</p>',
        {'A': r'56', 'B': r'72', 'C': r'108', 'D': r'140'},
        'D',
        '\n'.join([
            r'Bước 1: Vì \(\ell \parallel m\), hai góc \((x - 16)^\circ\) và \(124^\circ\) nằm ở cùng vị trí góc trên-phải (hai góc đồng vị — corresponding angles), nên chúng <b>bằng nhau</b>.',
            r'Bước 2: Lập phương trình: \(x - 16 = 124\).',
            r'Bước 3: Cộng \(16\) hai vế: \(x = 124 + 16 = 140\).',
        ]),
        r'Với hai đường thẳng song song bị cắt bởi một cát tuyến, chỉ có đúng 2 loại góc: góc tù (bằng nhau) và góc nhọn (bằng nhau), và một góc tù + một góc nhọn = \(180^\circ\). Hai góc ở đây đều là góc tù nên bằng nhau!',
        {
            'A': ('Computed Supplementary Angle', r'Tính góc kề bù \(180 - 124 = 56\) mà quên đây là hai góc đồng vị bằng nhau.'),
            'B': ('Supplementary Assumption Trap', r'Cho tổng hai góc bằng \(180^\circ\): \((x - 16) + 124 = 180 \Rightarrow x = 72\).'),
            'C': ('Sign Error', r'Trừ \(16\) khỏi \(124\) thay vì cộng: \(124 - 16 = 108\).'),
            'D': ('Đáp án đúng', r'\(x - 16 = 124 \Rightarrow x = 140\).'),
        },
        desmos_tip_vi=r'Gõ <code>x - 16 = 124</code> trên Desmos để xác nhận nhanh <code>x = 140</code>.'
    ))

    # Q21 — MCQ (C) — Medium — Similar triangles side proportion (SVG)
    svg_q21 = svg_similar_triangles(
        side_ab='6', side_bc='9', side_de='10', side_ef='x',
        v1='A', v2='B', v3='C', v4='D', v5='E', v6='F'
    )
    qs.append(math_mcq(
        'sat_mm3_m2l_q21', 21, 'Geometry and Trigonometry', 'Similar Triangles', 'Medium',
        rf'<div style="display:flex;justify-content:center;margin:8px 0 12px;">{svg_q21}</div><p>In the figure shown above, \(\triangle ABC \sim \triangle DEF\), where vertices \(A, B,\) and \(C\) correspond to vertices \(D, E,\) and \(F\), respectively. If \(AB = 6\), \(BC = 9\), and \(DE = 10\), what is the length \(x\) of side \(\overline{{EF}}\)?</p>',
        r'<p>What is the value of \(x\)?</p>',
        {'A': r'5.4', 'B': r'13', 'C': r'15', 'D': r'18'},
        'C',
        '\n'.join([
            r'Bước 1: Vì \(\triangle ABC \sim \triangle DEF\), các cặp cạnh tương ứng tỉ lệ với nhau:',
            r'\[\frac{EF}{BC} = \frac{DE}{AB}\]',
            r'Bước 2: Thay số: \(\frac{x}{9} = \frac{10}{6} = \frac{5}{3}\).',
            r'Bước 3: Nhân chéo giải tìm \(x\): \(x = 9 \times \frac{5}{3} = 15\).',
        ]),
        r'Tam giác đồng dạng luôn giữ nguyên <b>tỉ số nhân</b> (scale factor \(k = \frac{10}{6} = \frac{5}{3}\)), tuyệt đối KHÔNG cộng thêm cùng một độ dài (\(10 - 6 = 4 \not\Rightarrow 9 + 4 = 13\))!',
        {
            'A': ('Inverted Scale Factor', r'Nhân nghịch đảo \(9 \times \frac{6}{10} = 5.4\), làm cạnh của tam giác lớn lại ngắn hơn tam giác nhỏ!'),
            'B': ('Additive Scaling Trap', r'Bẫy kinh điển: thấy \(DE\) dài hơn \(AB\) là \(4\) đơn vị nên cộng nhầm \(9 + 4 = 13\) thay vì nhân tỉ lệ.'),
            'C': ('Đáp án đúng', r'\(\frac{15}{9} = \frac{10}{6} = \frac{5}{3}\).'),
            'D': ('Doubled Side Guess', r'Nhân đôi \(9 \times 2 = 18\) mà không tính đúng tỉ lệ \(\frac{10}{6}\).'),
        },
        desmos_tip_vi=r'Gõ thẳng tỉ lệ thức <code>x / 9 = 10 / 6</code> trên Desmos để đọc ngay đường thẳng đứng <code>x = 15</code>.'
    ))

    # Q22 — SPR (300) — Medium — Cylinder volume (Municipal water reservoir, SVG)
    svg_q22 = svg_cylinder(r_lbl='5 m', h_lbl='12 m', note='Cylindrical Municipal Water Tank')
    qs.append(math_spr(
        'sat_mm3_m2l_q22', 22, 'Geometry and Trigonometry', 'Volume of Cylinders', 'Medium',
        rf'<div style="display:flex;justify-content:center;margin:8px 0 12px;">{svg_q22}</div><p>A cylindrical municipal water storage tank has a base radius of \(5\) meters and a height of \(12\) meters. The total volume of the tank is \(k\pi\) cubic meters, where \(k\) is a constant.</p>',
        r'<p>What is the value of \(k\)?</p>',
        ['300'],
        '300',
        '\n'.join([
            r'Bước 1: Áp dụng công thức thể tích hình trụ (có sẵn trong Reference Sheet trên Bluebook): \(V = \pi r^2 h\).',
            r'Bước 2: Thay \(r = 5\) và \(h = 12\): \(V = \pi (5)^2 (12) = \pi (25)(12) = 300\pi\text{ m}^3\).',
            r'Bước 3: So sánh với \(k\pi\), suy ra \(k = 300\).',
        ]),
        r'Khi đề cho sẵn đáp án dạng \(k\pi\), chỉ cần tính phần hệ số \(r^2 h\) và điền đúng giá trị \(k\) (KHÔNG nhân với \(3.14\)!).',
        desmos_tip_vi=r'Gõ <code>5^2 * 12</code> trên Desmos để có ngay hệ số <code>300</code>.'
    ))

    return qs


def verify_math():
    """Programmatic exact verification of all 22 Module 2 Lower answers."""
    # Q1: 4x + 16 = 44
    assert Fraction(44 - 16, 4) == 7
    # Q2: f(x) = 3x + 14 => f(6)
    assert 3 * 6 + 14 == 32
    # Q3: slope through (2,5),(6,17)
    assert Fraction(17 - 5, 6 - 2) == 3
    # Q4: S = 12m + 140
    assert 12 * 0 + 140 == 140 and 12 * 1 + 140 == 152
    # Q5: x + y = 26, x - y = 8
    x5 = Fraction(26 + 8, 2)
    y5 = 26 - x5
    assert x5 == 17 and y5 == 9 and x5 - y5 == 8
    # Q6: 3p - 7 <= 20
    assert Fraction(20 + 7, 3) == 9
    # Q7: parallel to y = -4x + 5 through (0, -3)
    assert -4 * 0 + (-3) == -3
    # Q8: g + v = 8, 25g + 60v = 305
    v8 = Fraction(305 - 25 * 8, 60 - 25)
    g8 = 8 - v8
    assert v8 == 3 and g8 == 5 and 25 * g8 + 60 * v8 == 305
    # Q9: h(t) = 2t^2 - 5t + 9 => h(4)
    assert 2 * 4**2 - 5 * 4 + 9 == 21
    # Q10: (3x^4)^2 * x^3 == 9x^11
    for xv in [1, 2, 3]:
        assert (3 * xv**4)**2 * (xv**3) == 9 * (xv**11)
    # Q11: (x + 7)(x - 3) == x^2 + 4x - 21
    for xv in [-2, 0, 5]:
        assert (xv + 7) * (xv - 3) == xv**2 + 4 * xv - 21
    # Q12: x^2 - 3x - 28 = 0 => positive root 7
    assert 7**2 - 3 * 7 - 28 == 0 and (-4)**2 - 3 * (-4) - 28 == 0
    # Q13: y = 3(x - 5)^2 + 4 => vertex (5, 4), h + k = 9
    assert 5 + 4 == 9
    # Q14: N(t) = 80 * 2^(t/2) => N(6)
    assert 80 * (2 ** Fraction(6, 2)) == 640
    # Q15: sqrt(2x + 7) = 5
    x15 = Fraction(5**2 - 7, 2)
    assert x15 == 9 and math.isclose(math.sqrt(2 * x15 + 7), 5)
    # Q16: 120% of 850
    assert Fraction(120, 100) * 850 == 1020
    # Q17: 180/4 = 270/6 = 360/8 = 45 => 10h = 450
    assert Fraction(180, 4) == Fraction(270, 6) == Fraction(360, 8) == 45
    assert 45 * 10 == 450
    # Q18: median of [4, 7, 3, 11, 7, 6, 18]
    temps = sorted([4, 7, 3, 11, 7, 6, 18])
    assert temps[3] == 7 and Fraction(sum(temps), len(temps)) == 8
    # Q19: P(Distance and Heel) = 24/80 = 3/10
    assert 28 + 12 + 16 + 24 == 80 and Fraction(24, 80) == Fraction(3, 10)
    # Q20: corresponding angles x - 16 = 124
    assert 124 + 16 == 140
    # Q21: similar triangles x/9 = 10/6
    assert Fraction(9 * 10, 6) == 15
    # Q22: cylinder V = pi * 5^2 * 12 = 300*pi
    assert 5**2 * 12 == 300


if __name__ == '__main__':
    verify_math()
    qs = get_m2l_questions()
    print(f"M2L OK: {len(qs)} Qs verified.")
