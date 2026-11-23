# -*- coding: utf-8 -*-
"""
Digital SAT Math Adaptive Mock Test #4 — Module 1 (Routing Module: 22 Questions)
Difficulty progression: Easy -> Medium -> Medium-Hard (Routing threshold: 15/22).
Blueprint:
  - Q1-Q8  : Algebra (8 Qs; Q5 SPR)
  - Q9-Q15 : Advanced Math (7 Qs; Q9, Q13 SPR)
  - Q16-Q19: Problem-Solving and Data Analysis (4 Qs; Q16, Q19 SPR; HTML tables)
  - Q20-Q22: Geometry and Trigonometry (3 Qs; Q22 SPR; SVG diagrams)
  - 16 MCQ strictly balanced A:4, B:4, C:4, D:4 + 6 SPR at Q5, Q9, Q13, Q16, Q19, Q22.
"""

from fractions import Fraction
import math
from sat_math_helpers import (
    math_mcq,
    math_spr,
    build_math_table,
    svg_parallel_transversal,
    svg_right_triangle,
    svg_circle_sector,
)


def get_m1_questions():
    qs = []

    # =========================================================================
    # Q1 — Algebra (Easy, MCQ -> B) | Theme: EV Charging Station
    # =========================================================================
    qs.append(math_mcq(
        'sat_mm4_m1_q1', 1, 'Algebra', 'Linear equations in one variable', 'Easy',
        r'''<p>A public fast-charging station for electric vehicles charges a flat session fee of $5.25 plus $0.35 per kilowatt-hour (kWh) of electricity delivered. During a single charging session, a driver is billed a total of $22.75.</p>''',
        r'''<p>How many kilowatt-hours of electricity did the driver purchase during this session?</p>''',
        {
            'A': r'35',
            'B': r'50',
            'C': r'65',
            'D': r'80',
        },
        'B',
        r'''Thiết lập phương trình tổng chi phí theo số kWh điện \(x\): \(5.25 + 0.35x = 22.75\). Trừ phí cố định \(5.25\) ở hai vế: \(0.35x = 17.50\). Chia hai vế cho \(0.35\): \(x = \dfrac{17.50}{0.35} = 50\text{ kWh}\).''',
        r'''Luôn tách biệt phần phí cố định (hằng số tự do) và đơn giá biến đổi (hệ số góc) trước khi chia.''',
        {
            'A': ('Unit Confusion', r'Nhầm đơn giá $0.35/kWh thành 35 kWh mà không giải phương trình.'),
            'B': ('Correct', r'Trừ đúng phí cố định ($22.75 − $5.25 = $17.50) rồi chia cho $0.35/kWh ra chính xác 50 kWh.'),
            'C': ('Omitted Fixed Fee', r'Quên trừ phí kết nối cố định $5.25 và chia thẳng 22.75 / 0.35 = 65.'),
            'D': ('Sign Reversal', r'Cộng nhầm phí cố định thay vì trừ: (22.75 + 5.25) / 0.35 = 80.'),
        },
        desmos_tip_vi=r'''Gõ thẳng <code>5.25 + 0.35x = 22.75</code> vào Desmos (hoặc tính trực tiếp <code>(22.75 - 5.25) / 0.35</code>) để đọc ngay kết quả 50.''',
    ))

    # =========================================================================
    # Q2 — Algebra (Easy, MCQ -> D) | Theme: Sustainable Forestry
    # =========================================================================
    qs.append(math_mcq(
        'sat_mm4_m1_q2', 2, 'Algebra', 'Linear functions in context', 'Easy',
        r'''<p>A sustainable forestry crew plants pine saplings at a constant rate. The number of saplings remaining in their trailer \(t\) hours after the start of a shift is modeled by the function:</p><p style="text-align:center;">\[R(t) = 420 - 35t\]</p>''',
        r'''<p>Which of the following is the best interpretation of the number \(35\) in this context?</p>''',
        {
            'A': r'The total number of hours required to plant all the saplings in the trailer',
            'B': r'The number of saplings loaded in the trailer at the start of the shift',
            'C': r'The number of saplings remaining in the trailer after 1 hour of planting',
            'D': r'The number of saplings the crew plants each hour',
        },
        'D',
        r'''Hàm bậc nhất có dạng \(R(t) = b + mt\) với \(b = 420\) là số cây ban đầu (\(t=0\)) và hệ số góc \(m = -35\) biểu thị tốc độ giảm của số cây còn lại trên xe mỗi giờ. Do đó, \(35\) chính là số cây thông đội trồng được trong mỗi giờ.''',
        r'''Trong mô hình tuyến tính \(y = b - rt\), hằng số \(r\) luôn là tốc độ thay đổi trên mỗi 1 đơn vị của biến đầu vào \(t\).''',
        {
            'A': ('X-Intercept Confusion', r'Tổng số giờ trồng hết cây là nghiệm \(t = 420/35 = 12\), không phải 35.'),
            'B': ('Y-Intercept Confusion', r'Số cây ban đầu trên xe khi \(t = 0\) là 420, không phải 35.'),
            'C': ('Evaluation Error', r'Sau 1 giờ số cây còn lại là \(R(1) = 420 - 35 = 385\), không phải 35.'),
            'D': ('Correct', r'Độ lớn hệ số góc \(|-35| = 35\) thể hiện đúng số cây đội trồng được mỗi giờ.'),
        },
        desmos_tip_vi=r'''Vẽ <code>y = 420 - 35x</code> trong Desmos rồi so sánh <code>y(0) = 420</code> và <code>y(1) = 385</code>: sau mỗi 1 giờ, số cây giảm đúng 35.''',
    ))

    # =========================================================================
    # Q3 — Algebra (Easy, MCQ -> A) | Theme: Pure Math (Expression Shortcut)
    # =========================================================================
    qs.append(math_mcq(
        'sat_mm4_m1_q3', 3, 'Algebra', 'Linear equations & expression evaluation', 'Easy',
        r'''<p>Consider the linear equation:</p><p style="text-align:center;">\[4(2x - 3) = 20\]</p>''',
        r'''<p>What is the value of \(6x - 9\)?</p>''',
        {
            'A': r'15',
            'B': r'4',
            'C': r'24',
            'D': r'33',
        },
        'A',
        r'''Cách siêu tốc (không cần tìm \(x\)): Chia cả hai vế của \(4(2x - 3) = 20\) cho \(4\), ta được \(2x - 3 = 5\). Nhận thấy \(6x - 9 = 3(2x - 3)\), nên \(6x - 9 = 3 \times 5 = 15\). Kiểm tra bằng cách giải trực tiếp: \(2x = 8 \Rightarrow x = 4 \Rightarrow 6(4) - 9 = 15\).''',
        r'''Luôn quan sát xem biểu thức cần tìm có là bội trực tiếp của cụm biểu thức trong phương trình hay không để rút gọn trong 5 giây.''',
        {
            'A': ('Correct', r'Vì \(2x - 3 = 5\) nên \(6x - 9 = 3(2x - 3) = 15\).'),
            'B': ('Solved for Wrong Quantity', r'4 là giá trị của \(x\), nhưng đề bài hỏi giá trị của \(6x - 9\).'),
            'C': ('Partial Evaluation', r'Tính \(6x = 24\) nhưng quên trừ đi \(9\).'),
            'D': ('Sign Flip Error', r'Cộng nhầm thành \(6(4) + 9 = 33\) thay vì trừ \(9\).'),
        },
        desmos_tip_vi=r'''Gõ <code>4(2x - 3) = 20</code> để xem đường thẳng đứng tại \(x = 4\), rồi gõ dòng dưới <code>6(4) - 9</code> để kiểm tra chắc chắn ra 15.''',
    ))

    # =========================================================================
    # Q4 — Algebra (Medium, MCQ -> C) | Theme: Archaeological Excavation Grids
    # =========================================================================
    qs.append(math_mcq(
        'sat_mm4_m1_q4', 4, 'Algebra', 'Systems of linear equations in context', 'Medium',
        r'''<p>During a field survey, an archaeological team excavated \(18\) grid squares in total. Each shallow trench square required \(2\) hours to clear, and each deep stratigraphic square required \(5\) hours to clear. The team spent a total of \(57\) hours clearing all \(18\) squares.</p>''',
        r'''<p>How many deep stratigraphic squares did the team clear?</p>''',
        {
            'A': r'5',
            'B': r'6',
            'C': r'7',
            'D': r'11',
        },
        'C',
        r'''Gọi \(s\) là số ô rãnh nông và \(d\) là số ô địa tầng sâu. Ta có hệ phương trình: \(s + d = 18\) và \(2s + 5d = 57\). Từ phương trình đầu rút \(s = 18 - d\), thay vào phương trình hai: \(2(18 - d) + 5d = 57 \Rightarrow 36 + 3d = 57 \Rightarrow 3d = 21 \Rightarrow d = 7\). Khi đó \(s = 11\).''',
        r'''Với bài toán tổng số lượng và tổng thời gian, đặt tên biến gợi nhớ (\(s, d\)) và đọc kỹ câu hỏi cuối để tránh chọn nhầm biến còn lại.''',
        {
            'A': ('Coefficient Reading Error', r'5 là số giờ cần cho mỗi ô sâu, không phải số lượng ô sâu.'),
            'B': ('Arithmetic Slip', r'Tính nhầm \(57 - 36 = 18\) rồi chia 3 ra 6 (đúng phải là \(21 / 3 = 7\)).'),
            'C': ('Correct', r'Giải hệ phương trình ra đúng \(d = 7\) ô sâu (và \(s = 11\) ô nông; tổng \(2(11) + 5(7) = 57\) giờ).'),
            'D': ('Solved for Other Variable', r'11 là số ô rãnh nông \(s\), trong khi đề hỏi số ô địa tầng sâu \(d\).'),
        },
        desmos_tip_vi=r'''Đổi biến sang \(x, y\): nhập <code>x + y = 18</code> và <code>2x + 5y = 57</code> vào Desmos, bấm chấm xám giao điểm \((11, 7)\) và đọc tung độ \(y = 7\).''',
    ))

    # =========================================================================
    # Q5 — Algebra (Medium, SPR -> -3) | Theme: Perpendicular Lines
    # =========================================================================
    qs.append(math_spr(
        'sat_mm4_m1_q5', 5, 'Algebra', 'Linear equations in two variables', 'Medium',
        r'''<p>In the \(xy\)-plane, line \(p\) passes through the points \((-2, 7)\) and \((4, -2)\). Line \(q\) is perpendicular to line \(p\) and passes through the point \((6, 1)\).</p>''',
        r'''<p>If the \(y\)-intercept of line \(q\) is \((0, b)\), what is the value of \(b\)?</p>''',
        ['-3'],
        '-3',
        r'''Bước 1: Tính hệ số góc của đường thẳng \(p\): \(m_p = \dfrac{-2 - 7}{4 - (-2)} = \dfrac{-9}{6} = -\dfrac{3}{2}\).<br>Bước 2: Vì đường thẳng \(q \perp p\), hệ số góc của \(q\) là số nghịch đảo đối dấu: \(m_q = -\dfrac{1}{m_p} = \dfrac{2}{3}\).<br>Bước 3: Đường thẳng \(q\) có dạng \(y = \dfrac{2}{3}x + b\) và đi qua \((6, 1)\), suy ra \(1 = \dfrac{2}{3}(6) + b \Rightarrow 1 = 4 + b \Rightarrow b = -3\).''',
        r'''Hai đường thẳng vuông góc có tích hệ số góc bằng \(-1\) (\(m_q = -1/m_p\)); nhớ đổi cả dấu lẫn đảo tử–mẫu.''',
        desmos_tip_vi=r'''Tính nhanh <code>m = (-2 - 7)/(4 - (-2))</code> trong Desmos rồi gõ <code>y - 1 = (-1/m)(x - 6)</code> và bấm vào giao điểm với trục \(Oy\) để thấy \((0, -3)\).''',
    ))

    # =========================================================================
    # Q6 — Algebra (Medium, MCQ -> A) | Theme: Sustainable Timber Economics
    # =========================================================================
    qs.append(math_mcq(
        'sat_mm4_m1_q6', 6, 'Algebra', 'Systems of linear inequalities', 'Medium',
        r'''<p>A community timber cooperative has a monthly hauling budget of at most $3,600 to transport cedar logs and birch logs to a regional sawmill. Transporting each cedar log costs $45, and transporting each birch log costs $30. To satisfy a standing contract, the cooperative must haul at least \(24\) cedar logs this month.</p>''',
        r'''<p>Which system of inequalities represents the possible numbers of cedar logs, \(c\), and birch logs, \(b\), that the cooperative can transport this month?</p>''',
        {
            'A': r'\(45c + 30b \le 3{,}600\) and \(c \ge 24\)',
            'B': r'\(45c + 30b \ge 3{,}600\) and \(c \le 24\)',
            'C': r'\(30c + 45b \le 3{,}600\) and \(c \ge 24\)',
            'D': r'\(45c + 30b \le 3{,}600\) and \(c + b \ge 24\)',
        },
        'A',
        r'''Cụm từ "at most $3,600" (tối đa $3,600) chuyển thành bất đẳng thức \(\le\): tổng chi phí vận chuyển là \(45c + 30b \le 3{,}600\). Cụm từ "at least 24 cedar logs" (ít nhất 24 khúc gỗ tuyết tùng) chuyển thành \(c \ge 24\).''',
        r'''Dịch chuẩn từ khóa bất đẳng thức SAT: "at most" \(\leftrightarrow \le\), "at least" \(\leftrightarrow \ge\), và kiểm tra kỹ ràng buộc áp dụng cho biến riêng hay tổng hai biến.''',
        {
            'A': ('Correct', r'Đúng cả chiều bất đẳng thức lẫn hệ số từng loại gỗ (\(45c + 30b \le 3{,}600\) và \(c \ge 24\)).'),
            'B': ('Reversed Inequalities', r'Đảo ngược cả hai dấu bất đẳng thức: dùng \(\ge\) cho ngân sách tối đa và \(\le\) cho hạn mức tối thiểu.'),
            'C': ('Swapped Coefficients', r'Gắn nhầm đơn giá $30 cho gỗ tuyết tùng \(c\) và $45 cho gỗ bạch dương \(b\).'),
            'D': ('Scope Mismatch', r'Áp dụng điều kiện "ít nhất 24" cho tổng cả hai loại gỗ (\(c + b \ge 24\)) thay vì riêng gỗ tuyết tùng \(c\).'),
        },
        desmos_tip_vi=r'''Kiểm tra nhanh bằng điểm thử hợp lệ: chọn \(c = 24, b = 0\) có chi phí \(45(24) = 1{,}080 \le 3{,}600\); chỉ các đáp án thỏa mãn điểm thử mới có thể đúng.''',
    ))

    # =========================================================================
    # Q7 — Algebra (Medium, MCQ -> C) | Theme: No-Solution Parametric System
    # =========================================================================
    qs.append(math_mcq(
        'sat_mm4_m1_q7', 7, 'Algebra', 'Systems of linear equations — no solution', 'Medium',
        r'''<p>Consider the system of linear equations below, where \(k\) is a constant:</p><p style="text-align:center;">\[\begin{aligned} 6x - 9y &= 15 \\ kx + 12y &= 10 \end{aligned}\]</p>''',
        r'''<p>If the system has no solution, what is the value of \(k\)?</p>''',
        {
            'A': r'\(-\dfrac{9}{2}\)',
            'B': r'\(-4\)',
            'C': r'\(-8\)',
            'D': r'\(8\)',
        },
        'C',
        r'''Hệ phương trình bậc nhất vô nghiệm khi hai đường thẳng song song (cùng tỉ lệ hệ số \(x, y\) nhưng khác tỉ lệ hằng số tự do): \(\dfrac{k}{6} = \dfrac{12}{-9} \ne \dfrac{10}{15}\). Ta có \(\dfrac{12}{-9} = -\dfrac{4}{3}\), suy ra \(k = 6 \cdot \left(-\dfrac{4}{3}\right) = -8\). Kiểm tra điều kiện hằng số: \(\dfrac{10}{15} = \dfrac{2}{3} \ne -\dfrac{4}{3}\) (thỏa mãn vô nghiệm).''',
        r'''Hệ \(a_1x + b_1y = c_1\) và \(a_2x + b_2y = c_2\) vô nghiệm khi và chỉ khi \(\dfrac{a_1}{a_2} = \dfrac{b_1}{b_2} \ne \dfrac{c_1}{c_2}\).''',
        {
            'A': ('Inverted Ratio', r'Lấy nghịch đảo tỉ số hệ số \(y\): \(6 \cdot (-9/12) = -9/2\).'),
            'B': ('Arithmetic Slip', r'Rút gọn sai tỉ lệ \(12/(-9)\) thành \(-2/3\) rồi nhân 6 ra \(-4\).'),
            'C': ('Correct', r'Đúng tỉ lệ \(k/6 = 12/(-9) = -4/3 \Rightarrow k = -8\), hai đường thẳng song song phân biệt.'),
            'D': ('Sign Error', r'Quên dấu âm của \(-9y\) nên giải ra \(k = +8\).'),
        },
        desmos_tip_vi=r'''Nhập <code>6x - 9y = 15</code> và <code>kx + 12y = 10</code>, bấm <b>Add slider: k</b> rồi thử \(k = -8\): hai đường thẳng song song hoàn toàn không cắt nhau.''',
    ))

    # =========================================================================
    # Q8 — Algebra (Medium-Hard, MCQ -> D) | Theme: Infinitely Many Solutions
    # =========================================================================
    qs.append(math_mcq(
        'sat_mm4_m1_q8', 8, 'Algebra', 'Linear equations — infinitely many solutions', 'Medium-Hard',
        r'''<p>In the equation below, \(a\) and \(b\) are constants:</p><p style="text-align:center;">\[a(3x - 4) + 2x = 14x + b\]</p>''',
        r'''<p>If the equation has infinitely many solutions, what is the value of \(a + b\)?</p>''',
        {
            'A': r'\(20\)',
            'B': r'\(4\)',
            'C': r'\(-16\)',
            'D': r'\(-12\)',
        },
        'D',
        r'''Khai triển và gom hệ số vế trái: \(3ax - 4a + 2x = (3a + 2)x - 4a\). Để phương trình có vô số nghiệm, hai vế phải đồng nhất với mọi \(x\), tức hệ số của \(x\) bằng nhau và hằng số tự do bằng nhau:<br>• \(3a + 2 = 14 \Rightarrow 3a = 12 \Rightarrow a = 4\).<br>• \(b = -4a = -4(4) = -16\).<br>Do đó \(a + b = 4 + (-16) = -12\).''',
        r'''Phương trình bậc nhất có vô số nghiệm khi đồng nhất cả hệ số góc (\(m_1 = m_2\)) lẫn hằng số tự do (\(c_1 = c_2\)).''',
        {
            'A': ('Sign Error on Constant', r'Quên dấu trừ ở \(-4a\) nên lấy \(b = +16\), dẫn tới \(4 + 16 = 20\).'),
            'B': ('Partial Solution', r'Chỉ tìm ra \(a = 4\) rồi chọn ngay mà quên cộng với \(b = -16\).'),
            'C': ('Partial Solution', r'Chỉ tìm ra \(b = -16\) mà quên cộng với \(a = 4\).'),
            'D': ('Correct', r'Đồng nhất hệ số cho \(a = 4\) và \(b = -16\), suy ra \(a + b = -12\).'),
        },
        desmos_tip_vi=r'''Vẽ <code>y = a(3x - 4) + 2x</code> và <code>y = 14x + b</code> với thanh trượt \(a, b\); điều chỉnh \(a = 4, b = -16\) sẽ thấy hai đường thẳng trùng khít hoàn toàn.''',
    ))

    # =========================================================================
    # Q9 — Advanced Math (Medium, SPR -> 11/2) | Theme: Sum of Quadratic Roots
    # =========================================================================
    qs.append(math_spr(
        'sat_mm4_m1_q9', 9, 'Advanced Math', 'Quadratic equations & Vieta formulas', 'Medium',
        r'''<p>Consider the quadratic equation:</p><p style="text-align:center;">\[2x^2 - 11x + 12 = 0\]</p>''',
        r'''<p>What is the sum of the solutions to the given equation?</p>''',
        ['11/2', '5.5'],
        '11/2 (or 5.5)',
        r'''Áp dụng định lý Viète cho phương trình bậc hai \(ax^2 + bx + c = 0\) (trước tiên kiểm tra \(\Delta = (-11)^2 - 4(2)(12) = 121 - 96 = 25 > 0\) có 2 nghiệm thực phân biệt): tổng hai nghiệm là \(x_1 + x_2 = -\dfrac{b}{a} = -\dfrac{-11}{2} = \dfrac{11}{2} = 5.5\).<br>Kiểm tra bằng phân tích nhân tử: \((2x - 3)(x - 4) = 0 \Rightarrow x_1 = 1.5, x_2 = 4 \Rightarrow 1.5 + 4 = 5.5\).''',
        r'''Với phương trình \(ax^2 + bx + c = 0\) có \(\Delta \ge 0\), tổng hai nghiệm luôn bằng \(-b/a\); đừng quên chia cho hệ số \(a\).''',
        desmos_tip_vi=r'''Vẽ <code>y = 2x^2 - 11x + 12</code> trong Desmos, bấm vào 2 giao điểm trục hoành \((1.5, 0)\) và \((4, 0)\) rồi cộng lại: \(1.5 + 4 = 5.5\).''',
    ))

    # =========================================================================
    # Q10 — Advanced Math (Easy, MCQ -> B) | Theme: Polynomial Operations
    # =========================================================================
    qs.append(math_mcq(
        'sat_mm4_m1_q10', 10, 'Advanced Math', 'Equivalent polynomial expressions', 'Easy',
        r'''<p>Consider the polynomial expression:</p><p style="text-align:center;">\[(3x^2 - 5x + 4) - (x^2 - 7x + 9)\]</p>''',
        r'''<p>Which of the following is equivalent to the given expression?</p>''',
        {
            'A': r'\(2x^2 - 12x + 13\)',
            'B': r'\(2x^2 + 2x - 5\)',
            'C': r'\(2x^2 - 12x - 5\)',
            'D': r'\(2x^2 + 2x + 13\)',
        },
        'B',
        r'''Phân phối dấu trừ vào toàn bộ ngoặc thứ hai: \(3x^2 - 5x + 4 - x^2 + 7x - 9\). Gom các hạng tử đồng dạng:<br>• \((3x^2 - x^2) = 2x^2\)<br>• \((-5x + 7x) = +2x\)<br>• \((4 - 9) = -5\)<br>Kết quả là \(2x^2 + 2x - 5\).''',
        r'''Khi trừ một đa thức trong ngoặc, bắt buộc đổi dấu TẤT CẢ các hạng tử bên trong ngoặc trước khi cộng gom.''',
        {
            'A': ('Missed Sign Distribution', r'Chỉ đổi dấu \(x^2\) mà quên đổi dấu cả \(-7x\) lẫn \(+9\).'),
            'B': ('Correct', r'Đổi dấu chuẩn xác thành \(-x^2 + 7x - 9\), gom gọn ra \(2x^2 + 2x - 5\).'),
            'C': ('Double Negative Trap', r'Tính sai \(-5x - (-7x)\) thành \(-12x\) thay vì \(+2x\).'),
            'D': ('Constant Sign Trap', r'Cộng nhầm \(4 + 9 = 13\) thay vì \(4 - 9 = -5\).'),
        },
        desmos_tip_vi=r'''Đặt <code>f(x) = (3x^2 - 5x + 4) - (x^2 - 7x + 9)</code> và thử các đáp án <code>g(x)</code>; chỉ có đáp án B vẽ ra parabol trùng khít 100%.''',
    ))

    # =========================================================================
    # Q11 — Advanced Math (Medium, MCQ -> A) | Theme: Sustainable Forestry Biomass
    # =========================================================================
    qs.append(math_mcq(
        'sat_mm4_m1_q11', 11, 'Advanced Math', 'Exponential growth modeling', 'Medium',
        r'''<p>A sustainably managed timber reserve initially holds \(12{,}000\) metric tons of standing biomass. Under a selective-harvesting plan, the reserve's biomass increases by \(8\%\) every \(5\) years.</p>''',
        r'''<p>Which function \(B(t)\) models the standing biomass, in metric tons, \(t\) years after the initial measurement?</p>''',
        {
            'A': r'\(B(t) = 12{,}000(1.08)^{t/5}\)',
            'B': r'\(B(t) = 12{,}000(1.08)^{5t}\)',
            'C': r'\(B(t) = 12{,}000(0.08)^{t/5}\)',
            'D': r'\(B(t) = 12{,}000(1.40)^{t}\)',
        },
        'A',
        r'''Hàm mũ tăng trưởng có dạng \(B(t) = B_0(1 + r)^{t/T}\), trong đó giá trị ban đầu \(B_0 = 12{,}000\), tỉ lệ tăng \(r = 0.08\) (hệ số nhân \(1.08\)) sau mỗi chu kỳ \(T = 5\) năm. Vì cứ \(t = 5\) năm mới nhân với \(1.08\) một lần, số mũ phải là \(t/5\), cho \(B(t) = 12{,}000(1.08)^{t/5}\).''',
        r'''Kiểm tra chu kỳ hàm mũ bằng cách thay \(t = T\) (ở đây \(t = 5\)): số mũ phải đúng bằng \(1\) để giá trị tăng đúng một lần \(8\%\).''',
        {
            'A': ('Correct', r'Khi \(t = 5\), \(B(5) = 12{,}000(1.08)^1\), khớp hoàn toàn với mức tăng 8% sau 5 năm.'),
            'B': ('Inverted Period Exponent', r'Dùng \(5t\) nghĩa là tăng 8% mỗi \(1/5\) năm (5 lần mỗi năm), sai chu kỳ.'),
            'C': ('Missing Base 1', r'Dùng cơ số \(0.08\) thay vì \(1 + 0.08 = 1.08\), biến tăng trưởng thành suy giảm mạnh.'),
            'D': ('Linearized Rate Error', r'Nhân gộp \(8\% \times 5 = 40\%\) cho mỗi 1 năm, sai bản chất chu kỳ 5 năm.'),
        },
        desmos_tip_vi=r'''Kiểm tra bằng mốc \(t = 5\): sinh khối đúng sau 5 năm là \(12{,}000 \times 1.08 = 12{,}960\); thay \(t = 5\) vào 4 đáp án chỉ có A ra \(12{,}960\).''',
    ))

    # =========================================================================
    # Q12 — Advanced Math (Medium, MCQ -> D) | Theme: Stone Monument Parabolic Arch
    # =========================================================================
    qs.append(math_mcq(
        'sat_mm4_m1_q12', 12, 'Advanced Math', 'Quadratic functions — vertex form', 'Medium',
        r'''<p>The interior height \(h(x)\), in meters, of a parabolic stone monument arch at a horizontal distance of \(x\) meters from its left base is modeled by:</p><p style="text-align:center;">\[h(x) = -0.25(x - 8)^2 + 16\]</p>''',
        r'''<p>According to the model, what is the maximum height of the arch and at what horizontal distance from the left base does it occur?</p>''',
        {
            'A': r'Maximum height of \(8\) meters at a horizontal distance of \(16\) meters',
            'B': r'Maximum height of \(16\) meters at a horizontal distance of \(16\) meters',
            'C': r'Maximum height of \(4\) meters at a horizontal distance of \(8\) meters',
            'D': r'Maximum height of \(16\) meters at a horizontal distance of \(8\) meters',
        },
        'D',
        r'''Hàm bậc hai dạng đỉnh \(h(x) = a(x - h)^2 + k\) có hệ số \(a = -0.25 < 0\) nên parabol quay bề lõm xuống dưới và đạt giá trị lớn nhất tại đỉnh \((h, k) = (8, 16)\). Do đó, chiều cao tối đa của vòm đá là \(16\) mét tại khoảng cách ngang \(x = 8\) mét tính từ chân trái.''',
        r'''Dạng đỉnh \(a(x - h)^2 + k\) cho biết ngay hoành độ đỉnh \(x = h\) (đổi dấu trong ngoặc) và cực trị \(y = k\) (giữ nguyên dấu ngoài ngoặc).''',
        {
            'A': ('Swapped Coordinates', r'Đổi nhầm hoành độ \(h = 8\) và tung độ cực đại \(k = 16\).'),
            'B': ('Span Confusion', r'16 mét là toàn bộ bề rộng chân vòm (từ \(x = 0\) đến \(x = 16\)), còn đỉnh nằm ở chính giữa \(x = 8\).'),
            'C': ('Coefficient Multiplication Trap', r'Nhân nhầm \(|-0.25| \times 16 = 4\) để tính chiều cao tối đa.'),
            'D': ('Correct', r'Đọc chuẩn đỉnh \((8, 16)\): chiều cao cực đại 16 m đạt tại \(x = 8\) m.'),
        },
        desmos_tip_vi=r'''Vẽ <code>y = -0.25(x - 8)^2 + 16</code> trên Desmos rồi bấm vào đỉnh parabol sẽ hiển thị ngay tọa độ \((8, 16)\).''',
    ))

    # =========================================================================
    # Q13 — Advanced Math (Medium, SPR -> 2) | Theme: Radical Equations
    # =========================================================================
    qs.append(math_spr(
        'sat_mm4_m1_q13', 13, 'Advanced Math', 'Radical equations & extraneous solutions', 'Medium',
        r'''<p>Consider the equation:</p><p style="text-align:center;">\[\sqrt{3x + 10} = x + 2\]</p>''',
        r'''<p>What is the solution to the given equation?</p>''',
        ['2'],
        '2',
        r'''Điều kiện để vế phải không âm: \(x + 2 \ge 0 \Rightarrow x \ge -2\). Bình phương hai vế:<br>\(3x + 10 = (x + 2)^2 = x^2 + 4x + 4 \Rightarrow x^2 + x - 6 = 0 \Rightarrow (x + 3)(x - 2) = 0\).<br>Ta được hai ứng viên \(x = 2\) và \(x = -3\). Thử lại vào phương trình gốc:<br>• Với \(x = 2\): \(\sqrt{16} = 4 = 2 + 2\) (thỏa mãn).<br>• Với \(x = -3\): \(\sqrt{1} = 1 \ne -3 + 2 = -1\) (nghiệm ngoại lai, loại).<br>Vậy nghiệm duy nhất là \(2\).''',
        r'''Với phương trình căn bậc hai \(\sqrt{A} = B\), BẮT BUỘC thử lại nghiệm vào phương trình gốc để loại nghiệm ngoại lai làm \(B < 0\).''',
        desmos_tip_vi=r'''Vẽ <code>y = sqrt(3x + 10)</code> và <code>y = x + 2</code> trong Desmos: hai đồ thị chỉ cắt nhau tại đúng 1 điểm \((2, 4)\) — Desmos tự động loại nghiệm ngoại lai!''',
    ))

    # =========================================================================
    # Q14 — Advanced Math (Medium-Hard, MCQ -> C) | Theme: Rational Expressions
    # =========================================================================
    qs.append(math_mcq(
        'sat_mm4_m1_q14', 14, 'Advanced Math', 'Equivalent rational expressions', 'Medium-Hard',
        r'''<p>For all values of \(x > 3\), consider the rational expression:</p><p style="text-align:center;">\[\dfrac{5}{x - 3} - \dfrac{2}{x + 1}\]</p>''',
        r'''<p>Which of the following is equivalent to the given expression?</p>''',
        {
            'A': r'\(\dfrac{3}{2x - 2}\)',
            'B': r'\(\dfrac{3x - 1}{(x - 3)(x + 1)}\)',
            'C': r'\(\dfrac{3x + 11}{(x - 3)(x + 1)}\)',
            'D': r'\(\dfrac{7x - 1}{(x - 3)(x + 1)}\)',
        },
        'C',
        r'''Quy đồng mẫu số chung \((x - 3)(x + 1)\):<br>\(\dfrac{5(x + 1) - 2(x - 3)}{(x - 3)(x + 1)} = \dfrac{5x + 5 - 2x + 6}{(x - 3)(x + 1)} = \dfrac{3x + 11}{(x - 3)(x + 1)}\).''',
        r'''Khi trừ hai phân thức, chú ý phân phối dấu trừ cho cả hạng tử âm trong ngoặc thứ hai: \(-2(-3) = +6\).''',
        {
            'A': ('Illegal Term Subtraction', r'Trừ thẳng tử với tử và cộng mẫu với mẫu — sai quy tắc phân thức.'),
            'B': ('Sign Distribution Error', r'Quên nhân dấu trừ với \(-3\), tính \(5 - 6 = -1\) thay vì \(5 + 6 = 11\).'),
            'C': ('Correct', r'Quy đồng và khai triển chính xác tử số \(5x + 5 - 2x + 6 = 3x + 11\).'),
            'D': ('Addition Instead of Subtraction', r'Cộng nhầm \(5x + 2x = 7x\) thay vì trừ \(5x - 2x\).'),
        },
        desmos_tip_vi=r'''Thay nhanh \(x = 4\) (thỏa mãn \(x > 3\)): biểu thức gốc là \(\dfrac{5}{1} - \dfrac{2}{5} = 4.6\). Kiểm tra C: \(\dfrac{3(4) + 11}{1 \cdot 5} = \dfrac{23}{5} = 4.6\) khớp chính xác!''',
    ))

    # =========================================================================
    # Q15 — Advanced Math (Medium-Hard, MCQ -> B) | Theme: EV Battery Energy Formula
    # =========================================================================
    qs.append(math_mcq(
        'sat_mm4_m1_q15', 15, 'Advanced Math', 'Isolating quantities in nonlinear formulas', 'Medium-Hard',
        r'''<p>In an electric vehicle battery storage array, the maximum transferable power \(P\), open-circuit voltage \(V\), and internal resistance \(R\) (all positive quantities) are related by the formula:</p><p style="text-align:center;">\[P = \dfrac{V^2}{4R}\]</p>''',
        r'''<p>Which equation correctly expresses \(V\) in terms of \(P\) and \(R\)?</p>''',
        {
            'A': r'\(V = 4\sqrt{PR}\)',
            'B': r'\(V = 2\sqrt{PR}\)',
            'C': r'\(V = \dfrac{\sqrt{PR}}{2}\)',
            'D': r'\(V = 2PR\)',
        },
        'B',
        r'''Nhân hai vế với \(4R\) để cô lập \(V^2\): \(V^2 = 4PR\). Vì \(V > 0\), lấy căn bậc hai hai vế: \(V = \sqrt{4PR} = 2\sqrt{PR}\).''',
        r'''Khi lấy căn bậc hai tích chứa hằng số như \(\sqrt{4PR}\), nhớ khai căn luôn cả hệ số số học (\(\sqrt{4} = 2\)).''',
        {
            'A': ('Unrooted Coefficient', r'Khai căn \(PR\) nhưng quên khai căn hệ số 4 ở ngoài căn.'),
            'B': ('Correct', r'Biến đổi chuẩn \(V^2 = 4PR \Rightarrow V = \sqrt{4PR} = 2\sqrt{PR}\).'),
            'C': ('Inverted Operation', r'Chia cho \(4\) thay vì nhân với \(4\) trước khi lấy căn bậc hai.'),
            'D': ('Forgot Square Root', r'Chia đôi số 4 thành 2 nhưng quên lấy căn bậc hai của \(PR\).'),
        },
        desmos_tip_vi=r'''Chọn số thử đẹp \(R = 1, V = 6 \Rightarrow P = 36/4 = 9\). Thay \(P = 9, R = 1\) vào các đáp án: chỉ có B cho \(2\sqrt{9} = 6 = V\).''',
    ))

    # =========================================================================
    # Q16 — Data Analysis (Medium, SPR -> 16/25) | Theme: Clinical Trials Table
    # =========================================================================
    tbl_q16 = build_math_table(
        ['Treatment Group', 'Improved', 'No Change', 'Total'],
        [
            ['Supplement', '96', '24', '120'],
            ['Placebo', '54', '66', '120'],
            ['Total', '150', '90', '240'],
        ],
        caption='University Sleep-Recovery Clinical Trial Outcomes (n = 240)'
    )
    qs.append(math_spr(
        'sat_mm4_m1_q16', 16, 'Problem-Solving and Data Analysis', 'Conditional probability & two-way tables', 'Medium',
        rf'''<p>A university medical center conducted a clinical trial of a sleep-recovery supplement with \(240\) adult volunteers. The table summarizes the results.</p>{tbl_q16}''',
        r'''<p>If one volunteer who showed improvement is selected at random, what is the probability that this volunteer was in the supplement group?</p>''',
        ['16/25', '0.64', '.64'],
        '16/25 (or 0.64)',
        r'''Đây là xác suất có điều kiện: không gian mẫu bị thu hẹp chỉ gồm những tình nguyện viên có kết quả "Improved" (cột Improved có tổng \(150\) người). Trong số \(150\) người đó, có \(96\) người thuộc nhóm Supplement. Vậy xác suất là \(\dfrac{96}{150} = \dfrac{16}{25} = 0.64\).''',
        r'''Trong bảng hai chiều, cụm "If one [X] is selected at random" xác định MẪU SỐ là tổng của riêng nhóm [X] (ở đây là 150, không phải tổng toàn bảng 240).''',
        desmos_tip_vi=r'''Gõ <code>96/150</code> vào Desmos để nhận ngay <code>0.64</code>, bấm nút phân số ở bên trái dòng để đổi sang phân số tối giản <code>16/25</code>.''',
    ))

    # =========================================================================
    # Q17 — Data Analysis (Medium, MCQ -> D) | Theme: EV Charging Network Growth
    # =========================================================================
    qs.append(math_mcq(
        'sat_mm4_m1_q17', 17, 'Problem-Solving and Data Analysis', 'Compound percent increase', 'Medium',
        r'''<p>A municipal electric vehicle charging network operated \(320\) active charging ports in 2023. In 2024, the number of active ports increased by \(25\%\) compared to 2023. In 2025, the number of active ports increased by \(15\%\) compared to 2024.</p>''',
        r'''<p>How many active charging ports did the network operate in 2025?</p>''',
        {
            'A': r'400',
            'B': r'448',
            'C': r'452',
            'D': r'460',
        },
        'D',
        r'''Tính tuần tự qua từng năm:<br>• Năm 2024: \(320 \times (1 + 0.25) = 320 \times 1.25 = 400\) cổng sạc.<br>• Năm 2025: \(400 \times (1 + 0.15) = 400 \times 1.15 = 460\) cổng sạc.<br>Lưu ý hệ số nhân tổng hợp là \(1.25 \times 1.15 = 1.4375\) (tăng \(43.75\%\)), chứ không phải \(25\% + 15\% = 40\%\).''',
        r'''Phần trăm nối tiếp luôn NHÂN các hệ số tăng trưởng \((1 + r_1)(1 + r_2)\), tuyệt đối không cộng gộp phần trăm.''',
        {
            'A': ('Stopped Early', r'400 chỉ là số cổng sạc của năm 2024, chưa tính mức tăng 15% của năm 2025.'),
            'B': ('Additive Percent Trap', r'Cộng gộp \(25\% + 15\% = 40\%\) rồi tính \(320 \times 1.40 = 448\) — bẫy phần trăm kinh điển!'),
            'C': ('Arithmetic Slip', r'Tính nhầm \(15\%\) của 400 hoặc cộng sai phần chênh lệch.'),
            'D': ('Correct', r'Nhân nối tiếp chính xác \(320 \times 1.25 \times 1.15 = 460\).'),
        },
        desmos_tip_vi=r'''Tính thẳng một dòng <code>320 * 1.25 * 1.15</code> trong Desmos để nhận ngay 460 mà không lo cộng nhầm phần trăm.''',
    ))

    # =========================================================================
    # Q18 — Data Analysis (Medium, MCQ -> A) | Theme: University Polling & MoE
    # =========================================================================
    qs.append(math_mcq(
        'sat_mm4_m1_q18', 18, 'Problem-Solving and Data Analysis', 'Inference from sample & margin of error', 'Medium',
        r'''<p>A university polling center randomly selected \(400\) undergraduate students from the official registrar list of all \(18{,}000\) undergraduates at the university. Of those surveyed, \(28\%\) reported commuting to campus by bicycle, with an associated margin of error of \(4.4\%\) at the \(95\%\) confidence level.</p>''',
        r'''<p>Which of the following conclusions is best supported by the survey results?</p>''',
        {
            'A': r'It is plausible that between \(23.6\%\) and \(32.4\%\) of all undergraduate students at the university commute by bicycle.',
            'B': r'Exactly \(28\%\) of all \(18{,}000\) undergraduate students at the university commute by bicycle.',
            'C': r'It is plausible that between \(23.6\%\) and \(32.4\%\) of all university students nationwide commute by bicycle.',
            'D': r'If the polling center had randomly surveyed \(1{,}600\) undergraduates instead of \(400\), the margin of error would have been larger.',
        },
        'A',
        r'''Mẫu được chọn ngẫu nhiên từ toàn bộ \(18{,}000\) sinh viên đại học của trường đó, nên có thể suy rộng hợp lý cho đúng tổng thể sinh viên đại học của trường này. Khoảng ước lượng hợp lý (plausible interval) là \(28\% \pm 4.4\%\), tức từ \(23.6\%\) đến \(32.4\%\).''',
        r'''Trong câu hỏi Margin of Error trên SAT: (1) dùng từ ngữ thận trọng "plausible" trên khoảng \(\hat{p} \pm \text{ME}\), (2) chỉ suy rộng đúng phạm vi tổng thể lấy mẫu, (3) mẫu càng lớn thì ME càng nhỏ.''',
        {
            'A': ('Correct', r'Đúng cả khoảng tin cậy \(28\% \pm 4.4\% = [23.6\%, 32.4\%]\) lẫn đúng tổng thể suy rộng (sinh viên đại học tại trường).'),
            'B': ('Absolute Claim Trap', r'Khẳng định "chính xác 28%" bỏ qua hoàn toàn sai số chọn mẫu (margin of error).'),
            'C': ('Overgeneralization Trap', r'Suy rộng quá đà ra sinh viên toàn quốc ("nationwide") dù mẫu chỉ lấy ở một trường đại học.'),
            'D': ('Sample Size Misconception', r'Ngược quy luật thống kê: tăng cỡ mẫu từ 400 lên 1,600 làm sai số giảm đi một nửa, không phải tăng lên.'),
        },
        desmos_tip_vi=r'''Tính nhanh hai đầu mút khoảng ước lượng trong Desmos: <code>28 - 4.4 = 23.6</code> và <code>28 + 4.4 = 32.4</code>.''',
    ))

    # =========================================================================
    # Q19 — Data Analysis (Medium-Hard, SPR -> 2.95) | Theme: Archaeological Pits Table
    # =========================================================================
    tbl_q19 = build_math_table(
        ['Intact Vessels per Pit', 'Number of Excavation Pits'],
        [
            ['1', '3'],
            ['2', '5'],
            ['3', '4'],
            ['4', '6'],
            ['5', '2'],
        ],
        caption='Ceramic Vessels Uncovered Across 20 Excavation Pits'
    )
    qs.append(math_spr(
        'sat_mm4_m1_q19', 19, 'Problem-Solving and Data Analysis', 'Weighted mean from frequency table', 'Medium-Hard',
        rf'''<p>An archaeological team cataloged the number of intact ceramic vessels found in each of \(20\) excavation pits, as summarized in the frequency table below.</p>{tbl_q19}''',
        r'''<p>What is the mean number of intact ceramic vessels uncovered per excavation pit?</p>''',
        ['59/20', '2.95'],
        '2.95 (or 59/20)',
        r'''Tính tổng số bình gốm thu được bằng cách nhân từng giá trị với tần số tương ứng:<br>\(\text{Tổng} = 1(3) + 2(5) + 3(4) + 4(6) + 5(2) = 3 + 10 + 12 + 24 + 10 = 59\).<br>Tổng số hố khai quật: \(3 + 5 + 4 + 6 + 2 = 20\).<br>Giá trị trung bình: \(\bar{x} = \dfrac{59}{20} = 2.95\).''',
        r'''Với bảng tần số, tuyệt đối không lấy trung bình cộng của riêng cột giá trị \((1+2+3+4+5)/5 = 3\); phải tính trung bình có trọng số \(\dfrac{\sum x_i f_i}{\sum f_i}\).''',
        desmos_tip_vi=r'''Gõ trực tiếp biểu thức <code>(1*3 + 2*5 + 3*4 + 4*6 + 5*2) / (3 + 5 + 4 + 6 + 2)</code> vào Desmos để nhận ngay <code>2.95</code>.''',
    ))

    # =========================================================================
    # Q20 — Geometry (Easy, MCQ -> C) | Theme: Parallel Grid Lines (SVG)
    # =========================================================================
    svg_q20 = svg_parallel_transversal(
        line1='ℓ', line2='m',
        ang1_lbl='(4x + 25)°', ang2_lbl='(6x − 25)°', ang3_lbl='',
        note='Note: Figure not drawn to scale.'
    )
    qs.append(math_mcq(
        'sat_mm4_m1_q20', 20, 'Geometry and Trigonometry', 'Parallel lines & transversals', 'Easy',
        rf'''<div style="text-align:center;margin-bottom:10px;">{svg_q20}</div><p>In the figure above, parallel survey lines \(\ell\) and \(m\) in an archaeological grid are intersected by a diagonal transect line.</p>''',
        r'''<p>What is the value of \(x\)?</p>''',
        {
            'A': r'15',
            'B': r'18',
            'C': r'25',
            'D': r'125',
        },
        'C',
        r'''Hai góc \((4x + 25)^\circ\) và \((6x - 25)^\circ\) nằm ở vị trí đồng vị (corresponding angles) tạo bởi cát tuyến cắt hai đường thẳng song song \(\ell \parallel m\), do đó chúng bằng nhau:<br>\(4x + 25 = 6x - 25 \Rightarrow 50 = 2x \Rightarrow x = 25\).<br>(Khi đó mỗi góc đo \(4(25) + 25 = 125^\circ\).)''',
        r'''Cát tuyến cắt hai đường thẳng song song chỉ tạo ra 2 cỡ góc: các góc đồng vị/so le trong BẰNG nhau, còn các góc trong cùng phía bù nhau (tổng \(180^\circ\)).''',
        {
            'A': ('Arithmetic Slip', r'Giải nhầm \(10x = 150\) hoặc cộng trừ sai hằng số 25.'),
            'B': ('Supplementary Angle Trap', r'Đặt nhầm tổng hai góc bằng \(180^\circ\): \((4x + 25) + (6x - 25) = 180 \Rightarrow 10x = 180 \Rightarrow x = 18\).'),
            'C': ('Correct', r'Đặt hai góc đồng vị bằng nhau \(4x + 25 = 6x - 25\) cho chính xác \(x = 25\).'),
            'D': ('Found Angle Instead of x', r'125° là số đo của góc, nhưng đề bài yêu cầu tìm giá trị của \(x\).'),
        },
        desmos_tip_vi=r'''Nhập <code>4x + 25 = 6x - 25</code> vào Desmos để xem ngay đường thẳng đứng tại \(x = 25\).''',
    ))

    # =========================================================================
    # Q21 — Geometry (Medium, MCQ -> B) | Theme: Stone Monument Right Triangle (SVG)
    # =========================================================================
    svg_q21 = svg_right_triangle(
        a_lbl='15', b_lbl='36', c_lbl='?',
        v_top='A', v_right_angle='B', v_right='C',
        note='Note: Figure not drawn to scale.'
    )
    qs.append(math_mcq(
        'sat_mm4_m1_q21', 21, 'Geometry and Trigonometry', 'Right triangle trigonometry', 'Medium',
        rf'''<div style="text-align:center;margin-bottom:10px;">{svg_q21}</div><p>Right triangle \(ABC\) models a cross-sectional stone support ramp for a pyramid monument, where \(\angle B = 90^\circ\), \(AB = 15\) meters, and \(BC = 36\) meters.</p>''',
        r'''<p>What is the value of \(\sin C\)?</p>''',
        {
            'A': r'\(\dfrac{5}{12}\)',
            'B': r'\(\dfrac{5}{13}\)',
            'C': r'\(\dfrac{12}{13}\)',
            'D': r'\(\dfrac{13}{5}\)',
        },
        'B',
        r'''Bước 1: Tìm cạnh huyền \(AC\) bằng định lý Pythagore (hoặc nhận ra bộ ba \(5\text{-}12\text{-}13\) nhân 3):<br>\(AC = \sqrt{15^2 + 36^2} = \sqrt{225 + 1296} = \sqrt{1521} = 39\).<br>Bước 2: Áp dụng SOH-CAH-TOA cho góc \(C\): cạnh đối là \(AB = 15\), cạnh huyền là \(AC = 39\), suy ra \(\sin C = \dfrac{15}{39} = \dfrac{5}{13}\).''',
        r'''Ghi nhớ các bộ ba Pythagore kinh điển (\(3\text{-}4\text{-}5\), \(5\text{-}12\text{-}13\), \(8\text{-}15\text{-}17\)) cùng bội của chúng giúp giải nhanh lượng giác không cần bấm nhiều.''',
        {
            'A': ('Trig Ratio Confusion (tan)', r'Tính \(\tan C = \dfrac{AB}{BC} = \dfrac{15}{36} = \dfrac{5}{12}\) thay vì \(\sin C\).'),
            'B': ('Correct', r'Đúng tỉ số \(\sin C = \dfrac{\text{đối}}{\text{huyền}} = \dfrac{15}{39} = \dfrac{5}{13}\).'),
            'C': ('Trig Ratio Confusion (cos)', r'Tính \(\cos C = \dfrac{BC}{AC} = \dfrac{36}{39} = \dfrac{12}{13}\) (dùng cạnh kề thay cho cạnh đối).'),
            'D': ('Inverted Ratio', r'Đảo ngược tỉ số thành huyền / đối \(= \dfrac{39}{15} = \dfrac{13}{5}\).'),
        },
        desmos_tip_vi=r'''Tính <code>15 / sqrt(15^2 + 36^2)</code> trong Desmos rồi bấm nút phân số ở bên trái dòng để đổi ra ngay <code>5/13</code>.''',
    ))

    # =========================================================================
    # Q22 — Geometry (Medium-Hard, SPR -> 30) | Theme: Geodesic Dome Sector (SVG)
    # =========================================================================
    svg_q22 = svg_circle_sector(
        radius_lbl='12 m', angle_lbl='75°',
        center_lbl='O', pt_a='A', pt_b='B',
        note='Note: Figure not drawn to scale.'
    )
    qs.append(math_spr(
        'sat_mm4_m1_q22', 22, 'Geometry and Trigonometry', 'Circles — area of a sector', 'Medium-Hard',
        rf'''<div style="text-align:center;margin-bottom:10px;">{svg_q22}</div><p>The diagram shows the circular base of a geodesic dome with center \(O\) and radius \(12\) meters. Shaded glass sector \(AOB\) has a central angle of \(75^\circ\).</p>''',
        r'''<p>If the area of shaded sector \(AOB\) is \(k\pi\) square meters, what is the value of \(k\)?</p>''',
        ['30'],
        '30',
        r'''Diện tích hình quạt tròn tỉ lệ thuận với góc ở tâm:<br>\(S_{\text{sector}} = \dfrac{75^\circ}{360^\circ} \cdot \pi r^2 = \dfrac{5}{24} \cdot \pi (12^2) = \dfrac{5}{24} \cdot 144\pi = 5 \cdot 6\pi = 30\pi\).<br>So sánh với \(k\pi\), ta được \(k = 30\).''',
        r'''Công thức diện tích hình quạt theo độ: \(S = \dfrac{\theta}{360} \pi r^2\). Luôn kiểm tra đề hỏi \(k\) (hệ số của \(\pi\)) hay hỏi giá trị xấp xỉ đã nhân \(\pi\).''',
        desmos_tip_vi=r'''Vì đề hỏi hệ số \(k\) trước \(\pi\), chỉ cần gõ <code>(75/360) * 12^2</code> vào Desmos để nhận ngay kết quả chính xác <code>30</code>.''',
    ))

    return qs


def verify_math():
    """Programmatic exact arithmetic verification for all 22 Module 1 questions."""
    # Q1: 5.25 + 0.35x = 22.75
    q1 = (Fraction(2275, 100) - Fraction(525, 100)) / Fraction(35, 100)
    assert q1 == 50, f"Q1 failed: {q1}"

    # Q2: R(t) = 420 - 35t -> rate = R(0) - R(1) = 35
    assert (420 - 35 * 0) - (420 - 35 * 1) == 35

    # Q3: 4(2x - 3) = 20 -> 6x - 9
    x3 = (Fraction(20, 4) + 3) / 2
    assert 6 * x3 - 9 == 15

    # Q4: s + d = 18, 2s + 5d = 57
    d4 = Fraction(57 - 2 * 18, 5 - 2)
    s4 = 18 - d4
    assert d4 == 7 and s4 == 11 and 2 * s4 + 5 * d4 == 57

    # Q5: p through (-2, 7), (4, -2); q perp p through (6, 1) -> b
    mp = Fraction(-2 - 7, 4 - (-2))
    mq = -1 / mp
    b5 = 1 - mq * 6
    assert mp == Fraction(-3, 2) and mq == Fraction(2, 3) and b5 == -3

    # Q6: 45c + 30b <= 3600 and c >= 24 (check boundary c=24, b=0)
    assert 45 * 24 + 30 * 0 <= 3600 and 24 >= 24

    # Q7: 6x - 9y = 15, kx + 12y = 10 no solution -> k/6 = 12/(-9) != 10/15
    k7 = 6 * Fraction(12, -9)
    assert k7 == -8 and Fraction(12, -9) != Fraction(10, 15)

    # Q8: a(3x - 4) + 2x = 14x + b -> infinitely many solutions -> a + b
    a8 = Fraction(14 - 2, 3)
    b8 = -4 * a8
    assert a8 == 4 and b8 == -16 and a8 + b8 == -12

    # Q9: 2x^2 - 11x + 12 = 0 -> sum of roots
    r9_1, r9_2 = Fraction(3, 2), Fraction(4, 1)
    assert 2 * r9_1**2 - 11 * r9_1 + 12 == 0
    assert 2 * r9_2**2 - 11 * r9_2 + 12 == 0
    assert r9_1 + r9_2 == Fraction(11, 2)

    # Q10: (3x^2 - 5x + 4) - (x^2 - 7x + 9) == 2x^2 + 2x - 5
    for xv in (-3, 0, 2, 7):
        lhs = (3 * xv**2 - 5 * xv + 4) - (xv**2 - 7 * xv + 9)
        rhs = 2 * xv**2 + 2 * xv - 5
        assert lhs == rhs

    # Q11: B(t) = 12000 * (1.08)^(t/5) -> at t=5, B(5) = 12960
    assert Fraction(12000) * Fraction(108, 100) == 12960

    # Q12: h(x) = -0.25(x - 8)^2 + 16 -> max at (8, 16)
    h12 = lambda x: Fraction(-1, 4) * (x - 8)**2 + 16
    assert h12(8) == 16 and h12(0) == 0 and h12(16) == 0 and h12(7) < 16

    # Q13: sqrt(3x + 10) = x + 2 -> unique valid root x = 2
    assert math.isclose(math.sqrt(3 * 2 + 10), 2 + 2)
    assert not math.isclose(math.sqrt(3 * (-3) + 10), -3 + 2)

    # Q14: 5/(x-3) - 2/(x+1) == (3x+11)/((x-3)(x+1))
    for xv in (4, 5, 10):
        lhs = Fraction(5, xv - 3) - Fraction(2, xv + 1)
        rhs = Fraction(3 * xv + 11, (xv - 3) * (xv + 1))
        assert lhs == rhs

    # Q15: P = V^2 / (4R) -> V = 2*sqrt(PR)
    for V, R in ((6, 1), (10, 5), (12, 3)):
        P = Fraction(V**2, 4 * R)
        assert math.isclose(2 * math.sqrt(float(P * R)), V)

    # Q16: P(Supplement | Improved) = 96 / 150 = 16/25 = 0.64
    assert 96 + 24 == 120 and 54 + 66 == 120 and 96 + 54 == 150 and 24 + 66 == 90
    p16 = Fraction(96, 150)
    assert p16 == Fraction(16, 25) and float(p16) == 0.64

    # Q17: 320 * 1.25 * 1.15 = 460
    p17 = Fraction(320) * Fraction(125, 100) * Fraction(115, 100)
    assert p17 == 460

    # Q18: 28% +/- 4.4% = [23.6%, 32.4%]
    assert Fraction(280 - 44, 10) == Fraction(236, 10)
    assert Fraction(280 + 44, 10) == Fraction(324, 10)

    # Q19: weighted mean = (1*3 + 2*5 + 3*4 + 4*6 + 5*2) / 20
    tot_pits = 3 + 5 + 4 + 6 + 2
    tot_vessels = 1 * 3 + 2 * 5 + 3 * 4 + 4 * 6 + 5 * 2
    mean19 = Fraction(tot_vessels, tot_pits)
    assert tot_pits == 20 and mean19 == Fraction(59, 20) and float(mean19) == 2.95

    # Q20: 4x + 25 = 6x - 25 -> x = 25, angle = 125
    x20 = Fraction(25 + 25, 6 - 4)
    assert x20 == 25 and 4 * x20 + 25 == 125 and 6 * x20 - 25 == 125

    # Q21: right triangle 15-36-39, sin(C) = 15/39 = 5/13
    ac21 = math.isqrt(15**2 + 36**2)
    assert ac21**2 == 15**2 + 36**2 and ac21 == 39
    assert Fraction(15, ac21) == Fraction(5, 13)

    # Q22: sector area (75/360) * 12^2 * pi = 30 pi
    k22 = Fraction(75, 360) * 12**2
    assert k22 == 30

    return True


if __name__ == '__main__':
    assert verify_math()
    qs = get_m1_questions()
    print(f"M1 verified: {len(qs)} questions")
