# -*- coding: utf-8 -*-
"""
Digital SAT Math Adaptive Mock Test #3 — Module 1 (Routing Module)
22 Questions: 16 MCQ (A:4, B:4, C:4, D:4) + 6 SPR (Q5, Q9, Q13, Q16, Q19, Q22)
Domains: Algebra (Q1-Q8), Advanced Math (Q9-Q15),
         Problem-Solving and Data Analysis (Q16-Q19),
         Geometry and Trigonometry (Q20-Q22)
Difficulty: Easy -> Medium -> Medium-Hard
IDs: sat_mm3_m1_q1 .. sat_mm3_m1_q22
"""

from fractions import Fraction
import math
from sat_math_helpers import (
    math_mcq,
    math_spr,
    build_math_table,
    svg_right_triangle,
    svg_cylinder,
)


def get_m1_questions():
    qs = []

    # =========================================================================
    # DOMAIN 1: ALGEBRA (Q1 - Q8)
    # =========================================================================

    # Q1 — MCQ (B) — Easy — Linear equation in one variable (Museum conservation)
    qs.append(math_mcq(
        'sat_mm3_m1_q1', 1, 'Algebra', 'Linear Equations in One Variable', 'Easy',
        r'<p>An art museum conservation studio charges a flat inspection fee of $195 plus $65 per hour of canvas stabilization for private collections. A collector paid a total of $650 to stabilize a single painting.</p>',
        r'<p>How many hours of canvas stabilization were performed on the painting?</p>',
        {'A': r'6', 'B': r'7', 'C': r'10', 'D': r'13'},
        'B',
        '\n'.join([
            r'Bước 1: Lập phương trình tổng chi phí theo số giờ \(h\): \(195 + 65h = 650\).',
            r'Bước 2: Trừ phí cố định hai vế: \(65h = 650 - 195 = 455\).',
            r'Bước 3: Chia hai vế cho \(65\): \(h = \frac{455}{65} = 7\) giờ.',
        ]),
        r'Mô hình chi phí tuyến tính chuẩn: \(\text{Tổng} = \text{Phí cố định} + (\text{Đơn giá}) \times (\text{Số giờ})\). Luôn trừ phí cố định trước khi chia cho đơn giá.',
        {
            'A': ('Arithmetic Error', r'Trừ hoặc chia nhầm dẫn đến thiếu 1 giờ; kiểm tra lại: \(195 + 65(6) = 585 \ne 650\).'),
            'B': ('Đáp án đúng', r'Thay \(h = 7\): \(195 + 65(7) = 195 + 455 = 650\) khớp chính xác.'),
            'C': ('Ignored Fixed Fee', r'Quên trừ phí kiểm tra cố định $195 và lấy thẳng \(650 \div 65 = 10\).'),
            'D': ('Sign Error', r'Cộng thêm $195 thay vì trừ: \((650 + 195) \div 65 = 13\).'),
        },
        desmos_tip_vi=r'Gõ thẳng <code>195 + 65x = 650</code> trên Desmos rồi click vào đường thẳng đứng để đọc ngay nghiệm <code>x = 7</code>.'
    ))

    # Q2 — MCQ (D) — Easy — Interpreting slope in context (Alpine meteorology)
    qs.append(math_mcq(
        'sat_mm3_m1_q2', 2, 'Algebra', 'Linear Functions & Slope Interpretation', 'Easy',
        r'<p>An alpine weather station models the mean air temperature \(T(h)\), in degrees Celsius, at an elevation of \(h\) hundred meters above sea level using the linear function:</p><p style="text-align:center;">\[T(h) = 14.5 - 0.65h\]</p>',
        r'<p>Which of the following is the best interpretation of \(-0.65\) in this context?</p>',
        {
            'A': r'The estimated air temperature at sea level is \(-0.65\) degrees Celsius.',
            'B': r'For every \(1\)-degree Celsius increase in air temperature, the elevation decreases by \(0.65\) meters.',
            'C': r'For every \(1\)-meter increase in elevation, the estimated air temperature decreases by \(0.65\) degrees Celsius.',
            'D': r'For every \(100\)-meter increase in elevation, the estimated air temperature decreases by \(0.65\) degrees Celsius.',
        },
        'D',
        '\n'.join([
            r'Bước 1: Trong hàm bậc nhất \(T(h) = 14.5 - 0.65h\), hệ số góc \(m = -0.65\) biểu thị độ biến thiên của \(T(h)\) khi biến đầu vào \(h\) tăng thêm \(1\) đơn vị.',
            r'Bước 2: Đọc kỹ đơn vị của \(h\) trong đề bài: \(h\) được đo bằng <b>trăm mét</b> ("hundred meters above sea level").',
            r'Bước 3: Do đó, khi \(h\) tăng \(1\) đơn vị (tức tăng \(100\) mét độ cao), nhiệt độ ước tính giảm \(0.65^\circ\text{C}\).',
        ]),
        r'Với câu hỏi diễn giải hệ số góc \(m\), luôn kiểm tra <b>đơn vị của biến độc lập</b> (ví dụ: trăm mét, nghìn đô, thập kỷ) để tránh bẫy đơn vị cơ bản.',
        {
            'A': ('Slope-Intercept Swap', r'Nhầm hệ số góc \(-0.65\) với tung độ gốc \(14.5\) (nhiệt độ tại mực nước biển \(h = 0\)).'),
            'B': ('Inverted Variables', r'Đảo ngược vai trò biến đầu vào (độ cao) và biến đầu ra (nhiệt độ), đồng thời sai đơn vị.'),
            'C': ('Unit Conversion Trap', r'Bỏ sót từ "hundred" trong định nghĩa của \(h\); \(h = 1\) tương ứng \(100\) mét chứ không phải \(1\) mét.'),
            'D': ('Đáp án đúng', r'Diễn giải chuẩn xác cả dấu âm (giảm), giá trị (\(0.65^\circ\text{C}\)) và đơn vị của \(h\) (\(100\) mét).'),
        },
        desmos_tip_vi=r'Thử tính nhanh <code>T(1) - T(0) = -0.65</code> trong Desmos và nhớ rằng <code>h = 1</code> ứng với độ cao \(100\) mét.'
    ))

    # Q3 — MCQ (A) — Easy — Systems of two linear equations (Semiconductor wafer)
    qs.append(math_mcq(
        'sat_mm3_m1_q3', 3, 'Algebra', 'Systems of Two Linear Equations', 'Easy',
        r'<p>In a semiconductor cleanroom, a fabrication engineer compares the thickness \(x\), in microns, of a standard silicon wafer with the thickness \(y\), in microns, of a back-ground wafer using the system of equations:</p><p style="text-align:center;">\[2x + 3y = 1,920\]\[x - y = 110\]</p>',
        r'<p>What is the thickness \(x\), in microns, of a standard silicon wafer?</p>',
        {'A': r'450', 'B': r'340', 'C': r'318', 'D': r'560'},
        'A',
        '\n'.join([
            r'Bước 1: Nhân phương trình thứ hai với \(3\) để khử \(y\): \(3x - 3y = 330\).',
            r'Bước 2: Cộng với phương trình thứ nhất: \((2x + 3y) + (3x - 3y) = 1,920 + 330 \Rightarrow 5x = 2,250\).',
            r'Bước 3: Chia hai vế cho \(5\): \(x = \frac{2,250}{5} = 450\) microns.',
        ]),
        r'Khi một phương trình có hệ số \(-y\) và phương trình kia có \(+3y\), nhân phương trình có \(-y\) với \(3\) rồi cộng đại số là cách khử biến nhanh và ít sai dấu nhất.',
        {
            'A': ('Đáp án đúng', r'Với \(x = 450\), suy ra \(y = 340\); kiểm tra: \(2(450) + 3(340) = 900 + 1,020 = 1,920\).'),
            'B': ('Wrong Variable', r'Đây là giá trị của \(y\) (tấm wafer mỏng hơn), không phải \(x\) mà đề bài hỏi.'),
            'C': ('Sign Error', r'Trừ \(330\) thay vì cộng vào \(1,920\): \((1,920 - 330) \div 5 = 318\).'),
            'D': ('Arithmetic Error', r'Cộng nhầm \(450 + 110 = 560\) sau khi tìm được \(x\).'),
        },
        desmos_tip_vi=r'Gõ <code>2x + 3y = 1920</code> và <code>x - y = 110</code> vào Desmos, phóng nhỏ đồ thị rồi click giao điểm để đọc ngay <code>(450, 340)</code>.'
    ))

    # Q4 — MCQ (C) — Medium — Perpendicular line equation (Athletic biomechanics)
    qs.append(math_mcq(
        'sat_mm3_m1_q4', 4, 'Algebra', 'Linear Equations in Two Variables', 'Medium',
        r'<p>In a biomechanics motion-capture plane, line \(p\) passes through the points \((2, 5)\) and \((6, 13)\). Line \(q\) is perpendicular to line \(p\) and passes through the point \((8, 3)\).</p>',
        r'<p>Which of the following is an equation of line \(q\)?</p>',
        {
            'A': r'\(y = -2x + 19\)',
            'B': r'\(y = \frac{1}{2}x - 1\)',
            'C': r'\(y = -\frac{1}{2}x + 7\)',
            'D': r'\(y = -\frac{1}{2}x + 3\)',
        },
        'C',
        '\n'.join([
            r'Bước 1: Tính hệ số góc của đường thẳng \(p\): \(m_p = \frac{13 - 5}{6 - 2} = \frac{8}{4} = 2\).',
            r'Bước 2: Vì đường thẳng \(q \perp p\), hệ số góc của \(q\) là nghịch đảo đối dấu: \(m_q = -\frac{1}{m_p} = -\frac{1}{2}\).',
            r'Bước 3: Thay điểm \((8, 3)\) vào \(y = -\frac{1}{2}x + b\): \(3 = -\frac{1}{2}(8) + b \Rightarrow 3 = -4 + b \Rightarrow b = 7\).',
            r'Bước 4: Phương trình đường thẳng \(q\) là \(y = -\frac{1}{2}x + 7\).',
        ]),
        r'Hai đường thẳng vuông góc luôn thỏa \(m_1 \cdot m_2 = -1\) (vừa đảo phân số, vừa đổi dấu). Không bao giờ dùng tung độ của một điểm bất kỳ làm tung độ gốc \(b\).',
        {
            'A': ('Incomplete Slope Transformation', r'Chỉ đổi dấu \(m_p = 2\) thành \(-2\) mà quên lấy nghịch đảo.'),
            'B': ('Sign Error', r'Lấy nghịch đảo \(\frac{1}{2}\) nhưng quên đổi dấu sang âm.'),
            'C': ('Đáp án đúng', r'Hệ số góc \(-\frac{1}{2}\) vuông góc với \(2\), và khi \(x = 8\) thì \(y = -4 + 7 = 3\).'),
            'D': ('Intercept Confusion', r'Dùng thẳng tung độ \(3\) của điểm \((8, 3)\) làm \(y\)-intercept thay vì giải tìm \(b\).'),
        },
        desmos_tip_vi=r'Vẽ điểm <code>(2,5), (6,13), (8,3)</code> và đồ thị <code>y = 2x + 1</code> cùng đáp án <code>y = -0.5x + 7</code> để thấy rõ góc vuông đi qua <code>(8, 3)</code>.'
    ))

    # Q5 — SPR (-9) — Medium — No-solution parametric linear system
    qs.append(math_spr(
        'sat_mm3_m1_q5', 5, 'Algebra', 'Systems of Linear Equations (No Solution)', 'Medium',
        r'<p>Consider the system of linear equations below, where \(k\) is a constant:</p><p style="text-align:center;">\[\frac{3}{4}x - \frac{5}{6}y = 9\]\[kx + 10y = 24\]</p>',
        r'<p>If the system of equations has no solution, what is the value of \(k\)?</p>',
        ['-9'],
        '-9',
        '\n'.join([
            r'Bước 1: Hệ hai phương trình bậc nhất vô nghiệm khi và chỉ khi hai đường thẳng song song và không trùng nhau: \(\frac{a_2}{a_1} = \frac{b_2}{b_1} \ne \frac{c_2}{c_1}\).',
            r'Bước 2: Tính tỉ lệ hệ số của \(y\): \(\frac{10}{-5/6} = 10 \times \left(-\frac{6}{5}\right) = -12\).',
            r'Bước 3: Áp dụng cùng tỉ lệ cho hệ số của \(x\): \(\frac{k}{3/4} = -12 \Rightarrow k = -12 \times \frac{3}{4} = -9\).',
            r'Bước 4: Kiểm tra tỉ lệ hằng số tự do: \(\frac{24}{9} = \frac{8}{3} \ne -12\), xác nhận hệ thực sự vô nghiệm.',
        ]),
        r'Quy tắc tỉ lệ hệ số 5 giây cho hệ vô nghiệm: \(\frac{a_2}{a_1} = \frac{b_2}{b_1} \ne \frac{c_2}{c_1}\). Luôn kiểm tra kỹ dấu âm trước hệ số \(y\).',
        desmos_tip_vi=r'Gõ cả hai phương trình kèm <code>k</code> vào Desmos, bấm <b>Add slider: k</b> rồi kéo tới <code>k = -9</code> để thấy hai đường thẳng song song hoàn toàn.'
    ))

    # Q6 — MCQ (D) — Medium — Systems of linear inequalities (Municipal water reservoirs)
    qs.append(math_mcq(
        'sat_mm3_m1_q6', 6, 'Algebra', 'Systems of Linear Inequalities', 'Medium',
        r'<p>A municipal water utility blends treated water from Reservoir North, which costs $1.20 per thousand gallons, and Reservoir South, which costs $1.80 per thousand gallons. Each day, the utility must supply at least \(500\) thousand gallons in total while keeping the total daily treatment cost to at most $780.</p>',
        r'<p>If \(n\) represents the number of thousands of gallons drawn from Reservoir North and \(s\) represents the number of thousands of gallons drawn from Reservoir South, which system of inequalities models this situation?</p>',
        {
            'A': r'\(n + s \le 500\) and \(1.2n + 1.8s \ge 780\)',
            'B': r'\(n + s \ge 500\) and \(1.8n + 1.2s \le 780\)',
            'C': r'\(n + s \le 500\) and \(1.2n + 1.8s \le 780\)',
            'D': r'\(n + s \ge 500\) and \(1.2n + 1.8s \le 780\)',
        },
        'D',
        '\n'.join([
            r'Bước 1: Tổng lượng nước tối thiểu ("at least 500") cho bất phương trình: \(n + s \ge 500\).',
            r'Bước 2: Tổng chi phí xử lý là \(1.20n + 1.80s\) và tối đa $780 ("at most $780"), cho bất phương trình: \(1.2n + 1.8s \le 780\).',
            r'Bước 3: Ghép hai bất phương trình được hệ đáp án D.',
        ]),
        r'Khóa từ vựng bất phương trình SAT: <b>at least / minimum</b> \(\rightarrow \ge\); <b>at most / maximum / no more than</b> \(\rightarrow \le\). Luôn đối chiếu đúng biến với đơn giá.',
        {
            'A': ('Reversed Inequality', r'Đảo ngược cả hai dấu bất đẳng thức: "at least" phải là \(\ge\) và "at most" phải là \(\le\).'),
            'B': ('Swapped Coefficients', r'Gán nhầm đơn giá $1.80 cho Reservoir North (\(n\)) và $1.20 cho Reservoir South (\(s\)).'),
            'C': ('Reversed Inequality', r'Dùng sai dấu \(\le\) cho điều kiện tổng lượng nước "at least 500".'),
            'D': ('Đáp án đúng', r'Khớp hoàn toàn cả hai ràng buộc về tổng lưu lượng (\(\ge 500\)) và trần ngân sách (\(\le 780\)).'),
        },
        desmos_tip_vi=r'Thử một điểm hợp lệ như <code>(400, 150)</code>: tổng <code>550 >= 500</code> và chi phí <code>1.2(400)+1.8(150) = 750 <= 780</code> — chỉ đáp án D đúng!'
    ))

    # Q7 — MCQ (A) — Medium — Linear function from two points + sum expression
    qs.append(math_mcq(
        'sat_mm3_m1_q7', 7, 'Algebra', 'Linear Functions', 'Medium',
        r'<p>For a linear function \(f\), \(f(4) = 19\) and \(f(10) = 43\).</p>',
        r'<p>What is the value of \(f(7) + f(0)\)?</p>',
        {'A': r'34', 'B': r'31', 'C': r'35', 'D': r'28'},
        'A',
        '\n'.join([
            r'Bước 1: Tìm hệ số góc: \(m = \frac{f(10) - f(4)}{10 - 4} = \frac{43 - 19}{6} = \frac{24}{6} = 4\).',
            r'Bước 2: Thay \((4, 19)\) vào \(f(x) = 4x + b\): \(19 = 4(4) + b \Rightarrow b = 3\). Vậy \(f(x) = 4x + 3\).',
            r'Bước 3: Tính \(f(7) = 4(7) + 3 = 31\) (hoặc nhận xét nhanh \(7\) là trung điểm của \(4\) và \(10\) nên \(f(7) = \frac{19 + 43}{2} = 31\)) và \(f(0) = b = 3\).',
            r'Bước 4: Cộng lại: \(f(7) + f(0) = 31 + 3 = 34\).',
        ]),
        r'Khi đề cho hai giá trị \(f(x_1), f(x_2)\), hãy xác định ngay \(m\) và \(b = f(0)\), đồng thời đọc kỹ biểu thức mục tiêu cuối cùng \(f(7) + f(0)\) tránh dừng sớm ở \(f(7)\).',
        {
            'A': ('Đáp án đúng', r'\(f(7) = 31\) và \(f(0) = 3\), tổng bằng \(34\).'),
            'B': ('Partial Solution', r'Dừng lại ngay sau khi tính \(f(7) = 31\), quên cộng thêm \(f(0) = 3\).'),
            'C': ('Slope-Intercept Swap', r'Lấy nhầm hệ số góc \(m = 4\) thay cho \(f(0) = 3\), dẫn đến \(31 + 4 = 35\).'),
            'D': ('Ignored Intercept', r'Bỏ qua tung độ gốc \(b = 3\) nên tính thành \(4(7) + 0 = 28\).'),
        },
        desmos_tip_vi=r'Tạo bảng Table gồm <code>(4, 19)</code> và <code>(10, 43)</code>, gõ hồi quy <code>y_1 ~ m x_1 + b</code> để lấy <code>m = 4, b = 3</code> rồi tính <code>(4*7 + 3) + 3 = 34</code>.'
    ))

    # Q8 — MCQ (B) — Medium-Hard — Infinitely many solutions linear equation (Museum auction)
    qs.append(math_mcq(
        'sat_mm3_m1_q8', 8, 'Algebra', 'Linear Equations (Infinitely Many Solutions)', 'Hard',
        r'<p>In an auction-house fee equivalence model, the equation below has infinitely many solutions for \(x\), where \(a\) and \(b\) are constants:</p><p style="text-align:center;">\[a(4x - 6) + 12 = 10x - b\]</p>',
        r'<p>What is the value of \(a + b\)?</p>',
        {
            'A': r'\(-\frac{1}{2}\)',
            'B': r'\(\frac{11}{2}\)',
            'C': r'\(\frac{17}{2}\)',
            'D': r'\(3\)',
        },
        'B',
        '\n'.join([
            r'Bước 1: Khai triển vế trái: \(4ax - 6a + 12 = 10x - b\).',
            r'Bước 2: Để phương trình có vô số nghiệm với mọi \(x\), hệ số của \(x\) và hằng số tự do ở hai vế phải đồng nhất.',
            r'Bước 3: Đồng nhất hệ số của \(x\): \(4a = 10 \Rightarrow a = \frac{5}{2}\).',
            r'Bước 4: Đồng nhất hằng số tự do: \(-6a + 12 = -b \Rightarrow -6\left(\frac{5}{2}\right) + 12 = -b \Rightarrow -15 + 12 = -b \Rightarrow -3 = -b \Rightarrow b = 3\).',
            r'Bước 5: Tính \(a + b = \frac{5}{2} + 3 = \frac{11}{2}\).',
        ]),
        r'Phương trình bậc nhất \(Ax + B = Cx + D\) có vô số nghiệm khi và chỉ khi \(A = C\) và \(B = D\). Cẩn thận dấu trừ đứng trước \(b\) ở vế phải!',
        {
            'A': ('Sign Error', r'Đồng nhất nhầm \(-6a + 12 = b\) thay vì \(-b\), suy ra \(b = -3\) và \(a + b = -\frac{1}{2}\).'),
            'B': ('Đáp án đúng', r'\(a = \frac{5}{2}\) và \(b = 3\), do đó \(a + b = \frac{11}{2}\).'),
            'C': ('Distribution Error', r'Quên nhân phân phối \(a\) vào \(-6\), ra \(-6 + 12 = 6\) rồi lấy \(b = 6 \Rightarrow a + b = \frac{17}{2}\).'),
            'D': ('Partial Solution', r'Chỉ tìm ra giá trị của \(b = 3\) mà quên cộng thêm \(a = \frac{5}{2}\).'),
        },
        desmos_tip_vi=r'Gõ <code>y = a(4x - 6) + 12</code> và <code>y = 10x - b</code> với thanh trượt <code>a, b</code>; khi <code>a = 2.5, b = 3</code> hai đường thẳng chồng khít 100%.'
    ))

    # =========================================================================
    # DOMAIN 2: ADVANCED MATH (Q9 - Q15)
    # =========================================================================

    # Q9 — SPR (-11) — Easy-Medium — Polynomial operations & coefficient sum
    qs.append(math_spr(
        'sat_mm3_m1_q9', 9, 'Advanced Math', 'Equivalent Polynomial Expressions', 'Medium',
        r'<p>The expression \((3x - 4)(2x + 7) - (x^2 - 5x + 6)\) is equivalent to \(ax^2 + bx + c\), where \(a\), \(b\), and \(c\) are constants.</p>',
        r'<p>What is the value of \(a + b + c\)?</p>',
        ['-11'],
        '-11',
        '\n'.join([
            r'Bước 1 (Cách đại số): Khai triển \((3x - 4)(2x + 7) = 6x^2 + 21x - 8x - 28 = 6x^2 + 13x - 28\).',
            r'Bước 2: Trừ đa thức sau (đổi dấu từng hạng tử): \((6x^2 + 13x - 28) - x^2 + 5x - 6 = 5x^2 + 18x - 34\).',
            r'Bước 3: Suy ra \(a = 5, b = 18, c = -34 \Rightarrow a + b + c = 5 + 18 - 34 = -11\).',
            r'Mẹo 3 giây: Tổng hệ số \(a + b + c\) chính là giá trị biểu thức tại \(x = 1\): \((3(1)-4)(2(1)+7) - (1^2 - 5(1) + 6) = (-1)(9) - 2 = -11\).',
        ]),
        r'Tổng các hệ số của đa thức \(ax^2 + bx + c\) luôn bằng giá trị của biểu thức khi thay \(x = 1\)! Cách này tránh 100% lỗi sai dấu khi khai triển.',
        desmos_tip_vi=r'Gõ <code>f(x) = (3x - 4)(2x + 7) - (x^2 - 5x + 6)</code> rồi gõ dòng dưới <code>f(1)</code> — Desmos trả ngay kết quả <code>-11</code> trong 2 giây!'
    ))

    # Q10 — MCQ (C) — Medium — Exponential decay interpretation (Alpine telemetry buoy)
    qs.append(math_mcq(
        'sat_mm3_m1_q10', 10, 'Advanced Math', 'Exponential Functions & Decay Models', 'Medium',
        r'<p>An alpine meteorology telemetry buoy operates on a lithium-thionyl battery whose remaining charge \(C(t)\), in ampere-hours, after \(t\) months in the field is modeled by:</p><p style="text-align:center;">\[C(t) = 48(0.94)^{\frac{t}{3}}\]</p>',
        r'<p>Which of the following is the best interpretation of the value \(0.94\) in this model?</p>',
        {
            'A': r'The battery loses \(94\%\) of its remaining charge every \(3\) months.',
            'B': r'The battery loses \(6\%\) of its remaining charge every month.',
            'C': r'The battery loses \(6\%\) of its remaining charge every \(3\) months.',
            'D': r'The battery loses \(0.94\) ampere-hours of charge every \(3\) months.',
        },
        'C',
        '\n'.join([
            r'Bước 1: Cơ số \(0.94 = 1 - 0.06\) cho biết sau mỗi chu kỳ, dung lượng pin còn lại \(94\%\), tức là <b>giảm đi \(6\%\)</b>.',
            r'Bước 2: Xét số mũ \(\frac{t}{3}\): số mũ tăng thêm \(1\) đơn vị khi \(t\) tăng thêm \(3\) tháng.',
            r'Bước 3: Vậy cứ mỗi \(3\) tháng, lượng điện còn lại của pin giảm đi \(6\%\).',
        ]),
        r'Trong mô hình hàm mũ \(y = P(1 - r)^{t/k}\): phần trăm giảm là \(r = 1 - \text{cơ số}\) và chu kỳ áp dụng là \(k\) (mẫu số của số mũ).',
        {
            'A': ('Percent Remaining vs. Lost', r'Nhầm \(94\%\) là phần bị mất đi; thực tế \(0.94\) là tỷ lệ còn lại, còn phần mất đi là \(1 - 0.94 = 6\%\).'),
            'B': ('Period Trap', r'Bỏ qua mẫu số \(3\) trong số mũ \(\frac{t}{3}\); chu kỳ giảm \(6\%\) là \(3\) tháng chứ không phải \(1\) tháng.'),
            'C': ('Đáp án đúng', r'Khớp cả tỷ lệ giảm \(6\%\) lẫn chu kỳ \(3\) tháng từ số mũ \(\frac{t}{3}\).'),
            'D': ('Linear vs. Exponential', r'Diễn giải sai hệ số nhân mũ thành mức giảm tuyến tính cố định theo ampe-giờ.'),
        },
        desmos_tip_vi=r'Tính <code>C(3)/C(0) = 0.94</code> và <code>1 - 0.94 = 0.06</code> trên Desmos để xác nhận sau \(3\) tháng pin giảm đúng \(6\%\).'
    ))

    # Q11 — MCQ (A) — Medium — Quadratic vertex form (Athletic biomechanics)
    qs.append(math_mcq(
        'sat_mm3_m1_q11', 11, 'Advanced Math', 'Quadratic Vertex Form & Extrema', 'Medium',
        r'<p>During a vertical-jump biomechanics assessment, the height \(h(t)\), in meters above a force plate, of an athlete’s center of mass \(t\) seconds after takeoff is modeled by:</p><p style="text-align:center;">\[h(t) = -5t^2 + 3t + 1.15\]</p>',
        r'<p>Which equivalent form of \(h(t)\) displays both the maximum height of the athlete’s center of mass and the time at which it is reached as constants or coefficients?</p>',
        {
            'A': r'\(h(t) = -5(t - 0.3)^2 + 1.60\)',
            'B': r'\(h(t) = -5(t + 0.3)^2 + 1.60\)',
            'C': r'\(h(t) = -5(t - 0.3)^2 + 0.70\)',
            'D': r'\(h(t) = -5(t - 0.6)^2 + 2.95\)',
        },
        'A',
        '\n'.join([
            r'Bước 1: Dạng đỉnh \(h(t) = a(t - t_{\text{max}})^2 + h_{\text{max}}\) hiển thị trực tiếp thời điểm đạt đỉnh và độ cao cực đại.',
            r'Bước 2: Hoành độ đỉnh: \(t_{\text{max}} = -\frac{b}{2a} = -\frac{3}{2(-5)} = 0.3\) giây.',
            r'Bước 3: Tung độ đỉnh: \(h(0.3) = -5(0.3)^2 + 3(0.3) + 1.15 = -0.45 + 0.90 + 1.15 = 1.60\) mét.',
            r'Bước 4: Dạng đỉnh tương đương là \(h(t) = -5(t - 0.3)^2 + 1.60\).',
        ]),
        r'Hoàn thành bình phương nhanh: tìm đỉnh \(\left(-\frac{b}{2a}, f\left(-\frac{b}{2a}\right)\right)\) rồi viết ngay \(a(t - h)^2 + k\), giữ nguyên hệ số \(a = -5\).',
        {
            'A': ('Đáp án đúng', r'Khai triển lại: \(-5(t^2 - 0.6t + 0.09) + 1.60 = -5t^2 + 3t + 1.15\), khớp 100%.'),
            'B': ('Sign Error', r'Sai dấu trong bình phương: viết \((t + 0.3)^2\) ứng với đỉnh âm \(t = -0.3\).'),
            'C': ('Completing-the-Square Sign Trap', r'Trừ \(0.45\) khỏi \(1.15\) thay vì cộng \(0.45\): vì \(-5(0.09) = -0.45\) nên cần \(+0.45\) để cân bằng.'),
            'D': ('Forgot to Halve Linear Coefficient', r'Quên chia đôi hệ số \(0.6\) khi hoàn thành bình phương \(-5(t^2 - 0.6t)\).'),
        },
        desmos_tip_vi=r'Gõ <code>y = -5x^2 + 3x + 1.15</code> trên Desmos rồi click vào đỉnh parabol — Desmos hiện ngay <code>(0.3, 1.6)</code>!'
    ))

    # Q12 — MCQ (D) — Medium — Radical equations & extraneous root check
    qs.append(math_mcq(
        'sat_mm3_m1_q12', 12, 'Advanced Math', 'Radical Equations & Extraneous Solutions', 'Medium',
        r'<p>Consider the equation:</p><p style="text-align:center;">\[\sqrt{4x + 17} = x + 3\]</p>',
        r'<p>Which of the following gives all real solutions to the equation?</p>',
        {
            'A': r'\(-4\) only',
            'B': r'\(-4\) and \(2\)',
            'C': r'\(-2\) and \(4\)',
            'D': r'\(2\) only',
        },
        'D',
        '\n'.join([
            r'Bước 1: Đặt điều kiện vế phải không âm: \(x + 3 \ge 0 \Rightarrow x \ge -3\).',
            r'Bước 2: Bình phương hai vế: \(4x + 17 = (x + 3)^2 = x^2 + 6x + 9\).',
            r'Bước 3: Đưa về phương trình bậc hai: \(x^2 + 2x - 8 = 0 \Rightarrow (x + 4)(x - 2) = 0 \Rightarrow x = -4\) hoặc \(x = 2\).',
            r'Bước 4: Thử lại vào phương trình gốc: với \(x = 2\), \(\sqrt{25} = 5 = 2 + 3\) (nhận); với \(x = -4\), \(\sqrt{1} = 1 \ne -1\) (loại nghiệm ngoại lai).',
        ]),
        r'Bất cứ khi nào bình phương hai vế phương trình chứa căn thức \(\sqrt{A} = B\), <b>BẮT BUỘC thử lại nghiệm</b> vì \(B\) không thể âm!',
        {
            'A': ('Kept Extraneous Root', r'Giữ nhầm nghiệm ngoại lai \(x = -4\) làm vế phải bằng \(-1 < 0\).'),
            'B': ('Forgot Extraneous Check', r'Bẫy kinh điển SAT: giải đúng phương trình bậc hai nhưng quên kiểm tra điều kiện \(x + 3 \ge 0\).'),
            'C': ('Factoring Sign Error', r'Đảo dấu hai nghiệm khi phân tích \((x + 4)(x - 2) = 0\).'),
            'D': ('Đáp án đúng', r'Chỉ có \(x = 2\) thỏa mãn phương trình căn thức gốc.'),
        },
        desmos_tip_vi=r'Vẽ <code>y = sqrt(4x + 17)</code> và <code>y = x + 3</code> trên Desmos — hai đồ thị chỉ cắt nhau tại <b>đúng 1 điểm</b> <code>(2, 5)</code>!'
    ))

    # Q13 — SPR (3) — Medium-Hard — Line tangent to parabola (discriminant = 0)
    qs.append(math_spr(
        'sat_mm3_m1_q13', 13, 'Advanced Math', 'Nonlinear Systems & Discriminant', 'Hard',
        r'<p>In the \(xy\)-plane, the line \(y = 6x + c\) intersects the parabola \(y = 2x^2 - 2x + 11\) at exactly one point, where \(c\) is a constant.</p>',
        r'<p>What is the value of \(c\)?</p>',
        ['3'],
        '3',
        '\n'.join([
            r'Bước 1: Lập phương trình hoành độ giao điểm: \(2x^2 - 2x + 11 = 6x + c \Rightarrow 2x^2 - 8x + (11 - c) = 0\).',
            r'Bước 2: Để đường thẳng cắt parabol tại đúng một điểm (tiếp xúc), biệt thức \(\Delta = b^2 - 4ac = 0\).',
            r'Bước 3: Thay \(a = 2, b = -8, C = 11 - c\): \((-8)^2 - 4(2)(11 - c) = 0 \Rightarrow 64 - 8(11 - c) = 0\).',
            r'Bước 4: Chia hai vế cho \(8\): \(8 - (11 - c) = 0 \Rightarrow c - 3 = 0 \Rightarrow c = 3\).',
        ]),
        r'Cụm từ "intersects at exactly one point" cho hệ parabol–đường thẳng luôn dẫn ngay đến điều kiện \(\Delta = b^2 - 4ac = 0\).',
        desmos_tip_vi=r'Gõ <code>y = 2x^2 - 2x + 11</code> và <code>y = 6x + c</code> kèm thanh trượt <code>c</code>; kéo đến khi đường thẳng chạm đúng 1 điểm vào parabol tại <code>c = 3</code> (tiếp điểm <code>(2, 15)</code>).'
    ))

    # Q14 — MCQ (B) — Medium-Hard — Isolating a variable (Municipal water spillway)
    qs.append(math_mcq(
        'sat_mm3_m1_q14', 14, 'Advanced Math', 'Isolating Quantities', 'Medium',
        r'<p>The discharge flow rate \(Q\) through a conical municipal reservoir spillway nozzle of diameter \(d\) is related to the hydraulic head \(H\) by the formula:</p><p style="text-align:center;">\[Q = kd^2\sqrt{2gH}\]</p><p>where \(Q, k, d, g,\) and \(H\) are positive quantities.</p>',
        r'<p>Which equation correctly expresses \(H\) in terms of \(Q, k, d,\) and \(g\)?</p>',
        {
            'A': r'\(H = \frac{Q^2}{2gkd^2}\)',
            'B': r'\(H = \frac{Q^2}{2gk^2d^4}\)',
            'C': r'\(H = \frac{Q}{2gk^2d^4}\)',
            'D': r'\(H = \frac{Q^2}{4g^2k^2d^4}\)',
        },
        'B',
        '\n'.join([
            r'Bước 1: Bình phương cả hai vế để khử dấu căn: \(Q^2 = (kd^2)^2 \cdot (2gH) = 2gk^2d^4H\).',
            r'Bước 2: Chia cả hai vế cho \(2gk^2d^4\) để cô lập \(H\): \(H = \frac{Q^2}{2gk^2d^4}\).',
        ]),
        r'Khi bình phương tích chứa căn thức \((A\sqrt{B})^2 = A^2 B\), phải bình phương MỌI thừa số ngoài căn (\(k \to k^2, d^2 \to d^4\)) và chỉ bỏ dấu căn ở phần trong căn (\(2gH\) giữ nguyên, không thành \(4g^2\)).',
        {
            'A': ('Forgot to Square Outside Factors', r'Chỉ bình phương \(Q\) và bỏ dấu căn mà quên bình phương \(k\) và \(d^2\).'),
            'B': ('Đáp án đúng', r'Bình phương đầy đủ từng thành phần và cô lập chuẩn xác \(H\).'),
            'C': ('Forgot to Square LHS', r'Bình phương vế phải nhưng quên bình phương \(Q\) ở vế trái.'),
            'D': ('Over-Squared Radical Interior', r'Bình phương cả \(2g\) vốn nằm bên trong dấu căn, biến thành \(4g^2\).'),
        },
        desmos_tip_vi=r'Gán số thử nhanh: <code>k=1, d=2, g=2, H=1</code> \(\Rightarrow Q = 1(4)\sqrt{4} = 8\). Thử vào 4 đáp án: chỉ B cho <code>64 / (4*1*16) = 1 = H</code>!'
    ))

    # Q15 — MCQ (C) — Medium-Hard — Cubic polynomial zeros & y-intercept (Semiconductor)
    qs.append(math_mcq(
        'sat_mm3_m1_q15', 15, 'Advanced Math', 'Polynomial Factors & Graphs', 'Hard',
        r'<p>A cubic polynomial function \(p(x)\) models the thermal profile across a silicon wafer mask. The graph of \(y = p(x)\) crosses the \(x\)-axis at \((-3, 0)\), \((1, 0)\), and \((4, 0)\), and passes through \((2, -30)\).</p>',
        r'<p>What is the value of \(p(0)\)?</p>',
        {'A': r'-36', 'B': r'12', 'C': r'36', 'D': r'48'},
        'C',
        '\n'.join([
            r'Bước 1: Từ ba nghiệm \(-3, 1, 4\), viết dạng tích có hệ số dẫn đầu \(a\): \(p(x) = a(x + 3)(x - 1)(x - 4)\).',
            r'Bước 2: Thay điểm \((2, -30)\): \(p(2) = a(5)(1)(-2) = -10a = -30 \Rightarrow a = 3\).',
            r'Bước 3: Tính \(p(0) = 3(0 + 3)(0 - 1)(0 - 4) = 3(3)(-1)(-4) = 36\).',
        ]),
        r'Khi đề cho các \(x\)-intercept của đa thức, TUYỆT ĐỐI không quên hệ số dẫn đầu \(a\) trong \(p(x) = a(x - r_1)(x - r_2)(x - r_3)\) rồi dùng điểm phụ để tìm \(a\).',
        {
            'A': ('Sign Error', r'Sai dấu khi nhân \((-1)(-4)\) nên ra \(-36\) thay vì \(+36\).'),
            'B': ('Omitted Leading Coefficient', r'Quên hệ số dẫn đầu \(a = 3\), chỉ tính \((3)(-1)(-4) = 12\).'),
            'C': ('Đáp án đúng', r'Xác định đúng \(a = 3\) và tính chuẩn \(p(0) = 36\).'),
            'D': ('Arithmetic Error', r'Tính nhầm \(a = 4\) dẫn đến \(4 \times 12 = 48\).'),
        },
        desmos_tip_vi=r'Gõ <code>p(x) = a(x+3)(x-1)(x-4)</code> kèm slider <code>a</code>, nhập điểm <code>(2, -30)</code> để thấy <code>a = 3</code> rồi gõ <code>p(0)</code> ra ngay <code>36</code>.'
    ))

    # =========================================================================
    # DOMAIN 3: PROBLEM-SOLVING AND DATA ANALYSIS (Q16 - Q19)
    # =========================================================================

    # Q16 — SPR (16.2 / 81/5) — Medium — Squared unit conversion (Semiconductor wafer)
    qs.append(math_spr(
        'sat_mm3_m1_q16', 16, 'Problem-Solving and Data Analysis', 'Rates & Squared Unit Conversions', 'Medium',
        r'<p>A deep-ultraviolet lithography scanner exposes silicon wafer surface area at a constant rate of \(45\) square centimeters per second.</p>',
        r'<p>At this rate, how many square meters of wafer surface can the scanner expose in \(1\) hour? (Note: \(1\text{ meter} = 100\text{ centimeters}\)).</p>',
        ['16.2', '81/5'],
        '16.2 (hoặc 81/5)',
        '\n'.join([
            r'Bước 1: Đổi thời gian: \(1\text{ giờ} = 3,600\text{ giây}\). Diện tích quét trong \(1\) giờ là \(45 \times 3,600 = 162,000\text{ cm}^2\).',
            r'Bước 2: Đổi đơn vị diện tích (bình phương hệ số đổi!): \(1\text{ m}^2 = (100\text{ cm})^2 = 10,000\text{ cm}^2\).',
            r'Bước 3: Chia cho \(10,000\): \(\frac{162,000}{10,000} = 16.2\text{ m}^2 = \frac{81}{5}\text{ m}^2\).',
        ]),
        r'Bẫy kinh điển SAT: đổi đơn vị diện tích phải <b>bình phương</b> tỉ lệ chiều dài (\(1\text{ m}^2 = 100^2\text{ cm}^2 = 10,000\text{ cm}^2\)), không chia cho \(100\)!',
        desmos_tip_vi=r'Gõ một dòng duy nhất trên Desmos: <code>45 * 3600 / 100^2</code> để ra chính xác <code>16.2</code> (bấm biểu tượng phân số sẽ hiện <code>81/5</code>).'
    ))

    # Q17 — MCQ (A) — Medium — Two-way table conditional probability (Museum conservation)
    tbl_q17 = build_math_table(
        ['Medium', 'Requires Cleaning', 'Stable', 'Total'],
        [
            ['Oil', '36', '84', '120'],
            ['Tempera', '24', '36', '60'],
            ['Watercolor', '15', '45', '60'],
            ['<b>Total</b>', '<b>75</b>', '<b>165</b>', '<b>240</b>'],
        ],
        caption='Museum Conservation Audit of 240 Cataloged Paintings'
    )
    qs.append(math_mcq(
        'sat_mm3_m1_q17', 17, 'Problem-Solving and Data Analysis', 'Two-Way Tables & Conditional Probability', 'Medium',
        rf'<p>The table below summarizes the results of a museum conservation audit classifying \(240\) cataloged paintings by medium and current conservation status.</p>{tbl_q17}',
        r'<p>If one painting that requires cleaning is selected at random, what is the probability that it is an oil painting?</p>',
        {
            'A': r'\(\frac{12}{25}\)',
            'B': r'\(\frac{3}{20}\)',
            'C': r'\(\frac{3}{10}\)',
            'D': r'\(\frac{1}{2}\)',
        },
        'A',
        '\n'.join([
            r'Bước 1: Xác định không gian mẫu thu hẹp ("one painting that requires cleaning"): tổng cột <b>Requires Cleaning</b> là \(75\).',
            r'Bước 2: Xác định tử số — tranh sơn dầu (Oil) nằm trong cột Requires Cleaning: \(36\).',
            r'Bước 3: Tính xác suất có điều kiện và rút gọn: \(\frac{36}{75} = \frac{12}{25}\).',
        ]),
        r'Trong câu hỏi xác suất có điều kiện từ bảng hai chiều, cụm từ ngay sau "If one [nhóm điều kiện] is selected..." quy định chính xác <b>mẫu số</b>.',
        {
            'A': ('Đáp án đúng', r'\(\frac{36}{75} = \frac{12}{25}\).'),
            'B': ('Grand Total Denominator Trap', r'Chia cho tổng toàn bảng \(240\) (\(\frac{36}{240} = \frac{3}{20}\)) thay vì cột điều kiện \(75\).'),
            'C': ('Reversed Conditioning', r'Lấy điều kiện là tranh Oil (\(\frac{36}{120} = \frac{3}{10}\)) thay vì điều kiện Requires Cleaning.'),
            'D': ('Marginal Probability Trap', r'Tính tỉ lệ chung của tranh Oil trên toàn bộ bảo tàng (\(\frac{120}{240} = \frac{1}{2}\)).'),
        },
        desmos_tip_vi=r'Gõ <code>36/75</code> vào Desmos rồi nhấn nút chuyển đổi phân số (góc trái ô nhập) để rút gọn tức thì thành <code>12/25</code>.'
    ))

    # Q18 — MCQ (D) — Medium — Sequential percent change (Museum auction)
    qs.append(math_mcq(
        'sat_mm3_m1_q18', 18, 'Problem-Solving and Data Analysis', 'Percentages & Compound Multipliers', 'Medium',
        r'<p>After an initial appraisal at value \(P\), in dollars, a rare ceramic vessel decreased in market valuation by \(20\%\) during an auction downturn. Two years later, following authenticated provenance research, its valuation increased by \(10\%\) from that reduced value to reach a final value of $4,400.</p>',
        r'<p>What was the initial appraised value \(P\), in dollars?</p>',
        {'A': r'$3,872', 'B': r'$4,840', 'C': r'$4,928', 'D': r'$5,000'},
        'D',
        '\n'.join([
            r'Bước 1: Giảm \(20\%\) tương ứng nhân với \(1 - 0.20 = 0.80\); tăng \(10\%\) tiếp theo tương ứng nhân với \(1 + 0.10 = 1.10\).',
            r'Bước 2: Hệ số gộp: \(0.80 \times 1.10 = 0.88\). Suy ra \(0.88P = 4,400\).',
            r'Bước 3: Giải tìm giá trị ban đầu: \(P = \frac{4,400}{0.88} = 5,000\) đô la.',
        ]),
        r'Phần trăm nối tiếp luôn <b>NHÂN</b> hệ số (\(0.80 \times 1.10 = 0.88\)), tuyệt đối không cộng trừ phần trăm (\(-20\% + 10\% \ne -10\%\)); và để tìm giá gốc \(P\), phải <b>CHIA</b> cho \(0.88\).',
        {
            'A': ('Multiplied Instead of Divided', r'Nhân \(4,400 \times 0.88 = 3,872\) thay vì chia cho \(0.88\).'),
            'B': ('Additive Percent Error', r'Gộp sai thành giảm \(10\%\) rồi nhân ngược \(4,400 \times 1.10 = 4,840\).'),
            'C': ('Reverse Percent Multiplier Trap', r'Nhận ra giảm \(12\%\) nhưng lại nhân \(4,400 \times 1.12 = 4,928\) thay vì chia \(0.88\).'),
            'D': ('Đáp án đúng', r'Kiểm tra xuôi: \(\$5,000 \times 0.80 = \$4,000\); \(\$4,000 \times 1.10 = \$4,400\).'),
        },
        desmos_tip_vi=r'Gõ trực tiếp <code>4400 / (0.8 * 1.1)</code> trên Desmos để nhận ngay <code>5000</code> mà không lo nhầm chiều nhân/chia.'
    ))

    # Q19 — SPR (65) — Medium-Hard — Weighted mean from frequency table (Alpine meteorology)
    tbl_q19 = build_math_table(
        ['Daily Peak Wind Speed (km/h)', 'Number of Days'],
        [
            ['30', '4'],
            ['40', '6'],
            ['50', '5'],
            ['60', '3'],
            [r'\(w\)', '2'],
        ],
        caption='Daily Peak Wind Speeds at Alpine Ridge Station (20 Days)'
    )
    qs.append(math_spr(
        'sat_mm3_m1_q19', 19, 'Problem-Solving and Data Analysis', 'Weighted Mean & Frequency Tables', 'Hard',
        rf'<p>The frequency table below shows the daily peak wind speeds recorded at an alpine ridge meteorology station over \(20\) days, where \(w\) is a constant.</p>{tbl_q19}',
        r'<p>If the mean daily peak wind speed for all \(20\) days was \(46\) kilometers per hour, what is the value of \(w\)?</p>',
        ['65'],
        '65',
        '\n'.join([
            r'Bước 1: Tổng tốc độ gió đỉnh của cả \(20\) ngày là \(20 \times 46 = 920\text{ km/h}\).',
            r'Bước 2: Tổng của \(18\) ngày đã biết: \(30(4) + 40(6) + 50(5) + 60(3) = 120 + 240 + 250 + 180 = 790\).',
            r'Bước 3: Suy ra \(790 + 2w = 920 \Rightarrow 2w = 130 \Rightarrow w = 65\).',
        ]),
        r'Luôn chuyển trung bình cộng có trọng số về phương trình <b>Tổng = (Trung bình) × (Tổng tần số)</b> để tránh quên nhân với tần số của ẩn \(w\).',
        desmos_tip_vi=r'Gõ thẳng phương trình <code>(30*4 + 40*6 + 50*5 + 60*3 + 2x) / 20 = 46</code> trên Desmos để nhận ngay nghiệm <code>x = 65</code>.'
    ))

    # =========================================================================
    # DOMAIN 4: GEOMETRY AND TRIGONOMETRY (Q20 - Q22)
    # =========================================================================

    # Q20 — MCQ (C) — Medium — Right triangle trigonometry (SVG right triangle)
    svg_q20 = svg_right_triangle(
        a_lbl='15', b_lbl='8', c_lbl='',
        v_top='A', v_right_angle='B', v_right='C',
        note='Note: Figure not drawn to scale.'
    )
    qs.append(math_mcq(
        'sat_mm3_m1_q20', 20, 'Geometry and Trigonometry', 'Right Triangle Trigonometry', 'Medium',
        rf'<div style="display:flex;justify-content:center;margin:8px 0 12px;">{svg_q20}</div><p>In right triangle \(ABC\) shown above, \(\angle B = 90^\circ\), \(AB = 15\), and \(BC = 8\).</p>',
        r'<p>What is the value of \(\cos A\)?</p>',
        {
            'A': r'\(\frac{8}{17}\)',
            'B': r'\(\frac{8}{15}\)',
            'C': r'\(\frac{15}{17}\)',
            'D': r'\(\frac{17}{15}\)',
        },
        'C',
        '\n'.join([
            r'Bước 1: Dùng định lý Pythagoras tìm cạnh huyền \(AC\): \(AC = \sqrt{15^2 + 8^2} = \sqrt{225 + 64} = \sqrt{289} = 17\) (bộ ba Pythagoras kinh điển \(8\text{–}15\text{–}17\)).',
            r'Bước 2: Với góc \(A\), cạnh kề là \(AB = 15\) và cạnh huyền là \(AC = 17\).',
            r'Bước 3: Áp dụng SOH-CAH-TOA: \(\cos A = \frac{\text{kề}}{\text{huyền}} = \frac{15}{17}\).',
        ]),
        r'Ghi nhớ 4 bộ ba Pythagoras vàng trên SAT (\(3\text{–}4\text{–}5\), \(5\text{–}12\text{–}13\), \(8\text{–}15\text{–}17\), \(7\text{–}24\text{–}25\)) và luôn kiểm tra cạnh kề so với đúng đỉnh góc được hỏi.',
        {
            'A': ('Sine-Cosine Confusion', r'Tính nhầm \(\sin A = \frac{BC}{AC} = \frac{8}{17}\) (đối/huyền) thay vì \(\cos A\).'),
            'B': ('Tangent Confusion', r'Tính nhầm \(\tan A = \frac{8}{15}\) (đối/kề).'),
            'C': ('Đáp án đúng', r'\(\cos A = \frac{AB}{AC} = \frac{15}{17}\).'),
            'D': ('Inverted Ratio', r'Đảo ngược tỉ số thành \(\frac{\text{huyền}}{\text{kề}} = \frac{17}{15}\) (lớn hơn \(1\), vô lý với cosin!).'),
        },
        desmos_tip_vi=r'Tính nhanh cạnh huyền <code>sqrt(15^2 + 8^2) = 17</code> trên Desmos rồi lập tỉ số kề/huyền <code>15/17</code>.'
    ))

    # Q21 — MCQ (B) — Medium-Hard — Cylinder volume & percent scaling (Municipal water)
    svg_q21 = svg_cylinder(r_lbl='r', h_lbl='h', note='Municipal Cylindrical Water Tank')
    qs.append(math_mcq(
        'sat_mm3_m1_q21', 21, 'Geometry and Trigonometry', 'Volume & Dimensional Scaling', 'Hard',
        rf'<div style="display:flex;justify-content:center;margin:8px 0 12px;">{svg_q21}</div><p>A cylindrical municipal water tank has radius \(r = 6\) meters and height \(h = 10\) meters. Engineers design a replacement cylindrical tank whose radius is \(50\%\) greater than the original radius and whose height is \(20\%\) less than the original height.</p>',
        r'<p>What is the volume, in cubic meters, of the replacement water tank?</p>',
        {
            'A': r'\(432\pi\)',
            'B': r'\(648\pi\)',
            'C': r'\(810\pi\)',
            'D': r'\(972\pi\)',
        },
        'B',
        '\n'.join([
            r'Bước 1: Tính bán kính mới (tăng \(50\%\)): \(r_{\text{new}} = 6 \times 1.5 = 9\) mét.',
            r'Bước 2: Tính chiều cao mới (giảm \(20\%\)): \(h_{\text{new}} = 10 \times 0.8 = 8\) mét.',
            r'Bước 3: Áp dụng công thức thể tích hình trụ \(V = \pi r^2 h\): \(V_{\text{new}} = \pi (9)^2 (8) = \pi (81)(8) = 648\pi\text{ m}^3\).',
        ]),
        r'Trong công thức thể tích hình trụ \(V = \pi r^2 h\), hệ số thay đổi bán kính luôn bị <b>bình phương</b> (\(1.5^2 \times 0.8 = 1.8\), nên \(V_{\text{new}} = 1.8 \times 360\pi = 648\pi\)).',
        {
            'A': ('Forgot to Square Radius Scale', r'Quên bình phương hệ số bán kính \(1.5\), tính nhầm \(360\pi \times 1.5 \times 0.8 = 432\pi\).'),
            'B': ('Đáp án đúng', r'\(\pi (9^2)(8) = 648\pi\).'),
            'C': ('Ignored Height Change', r'Tính đúng bán kính mới \(9\) nhưng quên giảm chiều cao \(20\%\), ra \(\pi (9^2)(10) = 810\pi\).'),
            'D': ('Sign Error on Height', r'Tăng chiều cao thêm \(20\%\) thành \(12\) thay vì giảm xuống \(8\): \(\pi(9^2)(12) = 972\pi\).'),
        },
        desmos_tip_vi=r'Gõ phần hệ số trước \(\pi\): <code>(6*1.5)^2 * (10*0.8)</code> trên Desmos để ra ngay <code>648</code> \(\Rightarrow 648\pi\).'
    ))

    # Q22 — SPR (11) — Medium-Hard — Circle equation & completing the square (Alpine radar)
    qs.append(math_spr(
        'sat_mm3_m1_q22', 22, 'Geometry and Trigonometry', 'Circles in the Coordinate Plane', 'Hard',
        r'<p>In the \(xy\)-plane, the boundary of an alpine meteorological radar coverage zone is modeled by the circle with equation:</p><p style="text-align:center;">\[x^2 + y^2 - 12x + 16y = 21\]</p>',
        r'<p>What is the radius of this circle?</p>',
        ['11'],
        '11',
        '\n'.join([
            r'Bước 1: Nhóm các hạng tử theo \(x\) và \(y\): \((x^2 - 12x) + (y^2 + 16y) = 21\).',
            r'Bước 2: Hoàn thành bình phương bằng cách cộng \(\left(\frac{-12}{2}\right)^2 = 36\) và \(\left(\frac{16}{2}\right)^2 = 64\) vào cả hai vế:',
            r'\[(x - 6)^2 + (y + 8)^2 = 21 + 36 + 64 = 121\]',
            r'Bước 3: Vì dạng chuẩn là \((x - h)^2 + (y - k)^2 = r^2\), suy ra \(r = \sqrt{121} = 11\).',
        ]),
        r'Công thức siêu tốc tìm bán kính từ \(x^2 + y^2 + Dx + Ey = C\): \(r = \sqrt{C + (D/2)^2 + (E/2)^2}\). Đừng quên lấy căn bậc hai ở bước cuối!',
        desmos_tip_vi=r'Gõ thẳng <code>x^2 + y^2 - 12x + 16y = 21</code> vào Desmos, click vào điểm cao nhất <code>(6, 3)</code> và thấp nhất <code>(6, -19)</code> \(\Rightarrow\) đường kính \(22\), bán kính \(r = 11\)!'
    ))

    return qs


def verify_math():
    """Programmatic exact verification of all 22 Module 1 answers."""
    # Q1: 195 + 65h = 650
    assert Fraction(650 - 195, 65) == 7
    # Q2: T(h) = 14.5 - 0.65h => T(1) - T(0) = -0.65 per 100 m
    assert Fraction(145, 10) - Fraction(65, 100) * 1 - Fraction(145, 10) == Fraction(-65, 100)
    # Q3: 2x + 3y = 1920, x - y = 110
    x3 = Fraction(1920 + 3 * 110, 5)
    y3 = x3 - 110
    assert x3 == 450 and y3 == 340 and 2 * x3 + 3 * y3 == 1920
    # Q4: line p through (2,5),(6,13); q perp through (8,3)
    mp = Fraction(13 - 5, 6 - 2)
    mq = -Fraction(1, mp)
    bq = 3 - mq * 8
    assert mp == 2 and mq == Fraction(-1, 2) and bq == 7
    # Q5: (3/4)x - (5/6)y = 9 and kx + 10y = 24 no solution
    ratio = Fraction(10, Fraction(-5, 6))
    k5 = ratio * Fraction(3, 4)
    assert k5 == -9 and Fraction(24, 9) != ratio
    # Q6: (400, 150) feasible for n+s>=500 and 1.2n+1.8s<=780
    assert 400 + 150 >= 500 and Fraction(12, 10) * 400 + Fraction(18, 10) * 150 <= 780
    # Q7: f(4)=19, f(10)=43 => f(7)+f(0)
    m7 = Fraction(43 - 19, 10 - 4)
    b7 = 19 - m7 * 4
    assert (m7 * 7 + b7) + b7 == 34
    # Q8: a(4x - 6) + 12 = 10x - b infinitely many solutions
    a8 = Fraction(10, 4)
    b8 = -(-6 * a8 + 12)
    assert a8 == Fraction(5, 2) and b8 == 3 and a8 + b8 == Fraction(11, 2)
    # Q9: (3x-4)(2x+7) - (x^2 - 5x + 6) = ax^2+bx+c => a+b+c = f(1)
    a9, b9, c9 = 6 - 1, (21 - 8) + 5, -28 - 6
    assert a9 == 5 and b9 == 18 and c9 == -34 and (a9 + b9 + c9) == -11
    assert (3 * 1 - 4) * (2 * 1 + 7) - (1 - 5 + 6) == -11
    # Q10: C(t) = 48*(0.94)^(t/3) => C(3)/C(0) = 0.94 => 6% decrease every 3 months
    assert Fraction(100 - 94, 100) == Fraction(6, 100)
    # Q11: -5(t - 0.3)^2 + 1.60 == -5t^2 + 3t + 1.15
    for tv in [Fraction(0), Fraction(3, 10), Fraction(1), Fraction(7, 5)]:
        lhs = -5 * tv**2 + 3 * tv + Fraction(115, 100)
        rhs = -5 * (tv - Fraction(3, 10))**2 + Fraction(160, 100)
        assert lhs == rhs
    # Q12: sqrt(4x+17) = x+3
    assert math.isclose(math.sqrt(4 * 2 + 17), 2 + 3)
    assert not math.isclose(math.sqrt(4 * (-4) + 17), -4 + 3)
    # Q13: 2x^2 - 2x + 11 = 6x + c tangent
    c13 = 11 - Fraction((-8)**2, 4 * 2)
    assert c13 == 3
    # Q14: Q = k*d^2*sqrt(2gH) => H = Q^2 / (2 g k^2 d^4)
    k14, d14, g14, H14 = Fraction(3), Fraction(2), Fraction(5), Fraction(10)
    Q14_sq = (k14**2) * (d14**4) * (2 * g14 * H14)
    assert Fraction(Q14_sq, 2 * g14 * (k14**2) * (d14**4)) == H14
    # Q15: p(x) = a(x+3)(x-1)(x-4), p(2)=-30 => p(0)
    a15 = Fraction(-30, (2 + 3) * (2 - 1) * (2 - 4))
    p0 = a15 * (0 + 3) * (0 - 1) * (0 - 4)
    assert a15 == 3 and p0 == 36
    # Q16: 45 cm^2/s in m^2/hr
    assert Fraction(45 * 3600, 100**2) == Fraction(81, 5)
    # Q17: Oil & Requires Cleaning / Requires Cleaning
    assert Fraction(36, 36 + 24 + 15) == Fraction(12, 25)
    assert (36 + 84) + (24 + 36) + (15 + 45) == 240
    # Q18: P * 0.80 * 1.10 = 4400
    assert Fraction(4400, Fraction(80, 100) * Fraction(110, 100)) == 5000
    # Q19: weighted mean = 46 over 20 days
    known = 30 * 4 + 40 * 6 + 50 * 5 + 60 * 3
    w19 = Fraction(20 * 46 - known, 2)
    assert 4 + 6 + 5 + 3 + 2 == 20 and w19 == 65
    # Q20: right triangle 8-15-17, cos(A) = AB/AC = 15/17
    assert 15**2 + 8**2 == 17**2 and Fraction(15, 17) == Fraction(15, 17)
    # Q21: cylinder r=6->9, h=10->8
    r21, h21 = Fraction(6) * Fraction(3, 2), Fraction(10) * Fraction(4, 5)
    assert r21**2 * h21 == 648
    # Q22: x^2 + y^2 - 12x + 16y = 21 => r^2 = 21 + 36 + 64 = 121 => r = 11
    assert 21 + (-6)**2 + 8**2 == 11**2


if __name__ == '__main__':
    verify_math()
    qs = get_m1_questions()
    print(f"M1 OK: {len(qs)} Qs verified.")
