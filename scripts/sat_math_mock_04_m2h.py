# -*- coding: utf-8 -*-
"""
Digital SAT Math Adaptive Mock Test #4 — Module 2 Hard (22 Questions, 650–800 Band)
Difficulty progression: Medium -> Medium-Hard -> Hard (True 750–800 parametric/multi-step challenges on Q14–Q22).
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
    svg_similar_triangles,
    svg_cylinder,
)


def get_m2h_questions():
    qs = []

    # =========================================================================
    # Q1 — Algebra (Medium, MCQ -> C) | Linear Function Symmetry / Slope
    # =========================================================================
    qs.append(math_mcq(
        'sat_mm4_m2h_q1', 1, 'Algebra', 'Linear functions & midpoint property', 'Medium',
        r'''<p>For a linear function \(f\), \(f(4) = 17\) and \(f(10) = 35\).</p>''',
        r'''<p>What is the value of \(f(1) + f(7)\)?</p>''',
        {
            'A': r'26',
            'B': r'29',
            'C': r'34',
            'D': r'52',
        },
        'C',
        r'''Cách 1 (Giải trực tiếp): Hệ số góc \(m = \dfrac{35 - 17}{10 - 4} = \dfrac{18}{6} = 3\). Suy ra \(f(x) = 3x + b\); thay \(f(4) = 17 \Rightarrow 12 + b = 17 \Rightarrow b = 5\), nên \(f(x) = 3x + 5\). Tính \(f(1) = 8\) và \(f(7) = 26\), suy ra \(f(1) + f(7) = 8 + 26 = 34\).<br>Cách 2 (Phím tắt 5 giây): Với mọi hàm bậc nhất, nếu \(x_1 + x_2 = 2x_0\) thì \(f(x_1) + f(x_2) = 2f(x_0)\). Vì \(1 + 7 = 8 = 2(4)\) nên \(f(1) + f(7) = 2f(4) = 2(17) = 34\)!''',
        r'''Với hàm bậc nhất \(f(x) = mx + b\), \(f(a) + f(b) \ne f(a + b)\) khi \(b \ne 0\), nhưng luôn có tính chất trung điểm \(f(a) + f(b) = 2f\!\left(\dfrac{a+b}{2}\right)\).''',
        {
            'A': ('Partial Calculation', r'26 chỉ là giá trị của \(f(7)\), quên cộng thêm \(f(1) = 8\).'),
            'B': ('Additivity Fallacy', r'Tính nhầm \(f(1) + f(7) = f(8) = 3(8) + 5 = 29\), quên cộng hằng số \(b = 5\) hai lần.'),
            'C': ('Correct', r'\(f(1) = 8\) và \(f(7) = 26\), tổng bằng \(34\) (cũng bằng \(2 \cdot f(4)\)).'),
            'D': ('Added Given Outputs', r'Cộng nhầm hai giá trị đề cho \(f(4) + f(10) = 17 + 35 = 52\).'),
        },
        desmos_tip_vi=r'''Nhập bảng \((4, 17)\) và \((10, 35)\) rồi gõ hồi quy <code>y_1 ~ m x_1 + b</code> để lấy \(m = 3, b = 5\), sau đó tính <code>(3*1+5) + (3*7+5) = 34</code>.''',
    ))

    # =========================================================================
    # Q2 — Algebra (Medium, MCQ -> A) | Theme: EV Battery Storage Facility
    # =========================================================================
    qs.append(math_mcq(
        'sat_mm4_m2h_q2', 2, 'Algebra', 'Systems of linear equations — linear combinations', 'Medium',
        r'''<p>At a grid-scale electric vehicle battery storage facility, the number of lithium-iron-phosphate racks, \(x\), and the number of sodium-ion racks, \(y\), satisfy the system of equations below:</p><p style="text-align:center;">\[\begin{aligned} 7x + 4y &= 156 \\ 3x - 2y &= 26 \end{aligned}\]</p>''',
        r'''<p>What is the value of \(5x + y\)?</p>''',
        {
            'A': r'91',
            'B': r'65',
            'C': r'130',
            'D': r'182',
        },
        'A',
        r'''Mẹo cộng thẳng biểu thức: Cộng hai phương trình vế theo vế:<br>\((7x + 4y) + (3x - 2y) = 156 + 26 \Rightarrow 10x + 2y = 182\).<br>Chia hai vế cho \(2\), ta có ngay \(5x + y = 91\) mà không cần giải riêng \(x\) và \(y\)!<br>(Kiểm tra nghiệm cụ thể: \(x = 16, y = 11 \Rightarrow 5(16) + 11 = 91\).)''',
        r'''Khi đề hệ phương trình hỏi giá trị một tổ hợp tuyến tính như \(5x + y\), thử cộng hoặc trừ trực tiếp hai phương trình trước khi giải riêng lẻ từng ẩn.''',
        {
            'A': ('Correct', r'Cộng hai phương trình được \(10x + 2y = 182\), chia 2 ra đúng \(5x + y = 91\).'),
            'B': ('Subtracted Instead of Added', r'Trừ hai phương trình rồi chia 2: \((156 - 26)/2 = 65\).'),
            'C': ('Subtracted Equations', r'Tính \(156 - 26 = 130\) thay vì cộng và chia đôi.'),
            'D': ('Forgot to Divide by 2', r'Cộng ra \(10x + 2y = 182\) nhưng quên chia 2 để lấy \(5x + y\).'),
        },
        desmos_tip_vi=r'''Vẽ hai đường thẳng <code>7x + 4y = 156</code> và <code>3x - 2y = 26</code> trong Desmos, bấm giao điểm \((16, 11)\) rồi tính <code>5(16) + 11 = 91</code>.''',
    ))

    # =========================================================================
    # Q3 — Algebra (Medium-Hard, MCQ -> D) | Theme: Sustainable Forestry Permit
    # =========================================================================
    qs.append(math_mcq(
        'sat_mm4_m2h_q3', 3, 'Algebra', 'Systems of linear inequalities in context', 'Medium-Hard',
        r'''<p>A sustainable forestry permit limits a logging crew to harvesting at most \(140\) trees in a sector, consisting of oak trees and maple trees. Each oak tree yields \(1.8\) cubic meters of timber, and each maple tree yields \(1.2\) cubic meters of timber. To meet mill demand, the crew must harvest at least \(216\) cubic meters of timber in total.</p>''',
        r'''<p>What is the minimum number of oak trees the crew must harvest to meet both conditions?</p>''',
        {
            'A': r'60',
            'B': r'72',
            'C': r'76',
            'D': r'80',
        },
        'D',
        r'''Gọi \(x\) là số cây sồi (oak) và \(y\) là số cây phong (maple). Ta có hệ bất phương trình:<br>\(x + y \le 140 \Rightarrow y \le 140 - x\) và \(1.8x + 1.2y \ge 216\).<br>Để cực tiểu hóa số cây sồi \(x\) (loại cho sản lượng lớn hơn), ta cho tổng số cây đạt kịch trần \(y = 140 - x\):<br>\(1.8x + 1.2(140 - x) \ge 216 \Rightarrow 1.8x + 168 - 1.2x \ge 216 \Rightarrow 0.6x \ge 48 \Rightarrow x \ge 80\).<br>Vậy cần khai thác ít nhất \(80\) cây sồi (kèm \(60\) cây phong).''',
        r'''Để tìm giá trị nhỏ nhất của biến có đơn vị lớn hơn trong bài toán ràng buộc tổng, đặt biến còn lại ở mức tối đa \(y = N - x\) rồi giải bất phương trình.''',
        {
            'A': ('Solved for Other Variable', r'60 là số cây phong tối đa đi kèm khi số cây sồi bằng 80, không phải số cây sồi.'),
            'B': ('Added Unit Yields', r'Cộng nhầm \(1.8 + 1.2 = 3.0\) rồi chia \(216 / 3 = 72\).'),
            'C': ('Arithmetic Slip', r'Sai phép trừ \(216 - 168\) hoặc sai phép chia cho \(0.6\).'),
            'D': ('Correct', r'Giải \(0.6x \ge 48\) cho chính xác \(x \ge 80\) cây sồi tối thiểu.'),
        },
        desmos_tip_vi=r'''Vẽ hệ <code>x + y <= 140</code> và <code>1.8x + 1.2y >= 216</code> trong Desmos; bấm vào đỉnh trái nhất của vùng giao nhau sẽ thấy ngay điểm \((80, 60)\).''',
    ))

    # =========================================================================
    # Q4 — Algebra (Medium-Hard, MCQ -> B) | Absolute Value with Parameter
    # =========================================================================
    qs.append(math_mcq(
        'sat_mm4_m2h_q4', 4, 'Algebra', 'Absolute value equations with parameters', 'Medium-Hard',
        r'''<p>In the equation below, \(c\) is a positive constant:</p><p style="text-align:center;">\[|3x - 7| + c = 12\]</p>''',
        r'''<p>If the equation has two solutions whose positive difference is \(6\), what is the value of \(c\)?</p>''',
        {
            'A': r'2',
            'B': r'3',
            'C': r'6',
            'D': r'9',
        },
        'B',
        r'''Cô lập trị tuyệt đối: \(|3x - 7| = 12 - c\) (với \(12 - c > 0\)). Phương trình tách thành hai nhánh:<br>• \(3x_1 - 7 = 12 - c \Rightarrow x_1 = \dfrac{19 - c}{3}\)<br>• \(3x_2 - 7 = -(12 - c) \Rightarrow x_2 = \dfrac{c - 5}{3}\)<br>Hiệu dương giữa hai nghiệm là:<br>\(x_1 - x_2 = \dfrac{(19 - c) - (c - 5)}{3} = \dfrac{24 - 2c}{3} = 6 \Rightarrow 24 - 2c = 18 \Rightarrow 2c = 6 \Rightarrow c = 3\).''',
        r'''Khoảng cách giữa hai nghiệm của \(|ax + b| = R\) (\(R > 0\)) luôn bằng \(\dfrac{2R}{|a|}\) — không hề phụ thuộc vào hằng số \(b\)!''',
        {
            'A': ('Arithmetic Slip', r'Nhầm hệ số chia khi giải \(24 - 2c = 18\).'),
            'B': ('Correct', r'Đặt \(\dfrac{2(12 - c)}{3} = 6 \Rightarrow 12 - c = 9 \Rightarrow c = 3\).'),
            'C': ('Ignored Coefficient and Factor of 2', r'Đặt nhầm \(12 - c = 6 \Rightarrow c = 6\).'),
            'D': ('Stopped at Intermediate Expression', r'Giải ra \(12 - c = 9\) rồi chọn ngay 9 thay vì tìm \(c = 12 - 9 = 3\).'),
        },
        desmos_tip_vi=r'''Gõ <code>y = |3x - 7| + c</code> và <code>y = 12</code> với thanh trượt \(c\); kéo tới \(c = 3\), hai giao điểm là \((-0.667, 12)\) và \((5.333, 12)\) có khoảng cách đúng bằng \(6\).''',
    ))

    # =========================================================================
    # Q5 — Algebra (Hard, SPR -> -69) | Parametric System — Infinite Solutions
    # =========================================================================
    qs.append(math_spr(
        'sat_mm4_m2h_q5', 5, 'Algebra', 'Systems of linear equations — infinitely many solutions', 'Hard',
        r'''<p>In the system of equations below, \(a\) and \(b\) are constants:</p><p style="text-align:center;">\[\begin{aligned} \dfrac{3}{4}x - \dfrac{5}{6}y &= 5 \\ ax + 10y &= b \end{aligned}\]</p>''',
        r'''<p>If the system has infinitely many solutions, what is the value of \(a + b\)?</p>''',
        ['-69'],
        '-69',
        r'''Để hệ có vô số nghiệm, phương trình thứ hai phải là bội số chính xác của phương trình thứ nhất. So sánh hệ số của \(y\) để tìm hệ số nhân \(k\):<br>\(k = \dfrac{10}{-5/6} = 10 \cdot \left(-\dfrac{6}{5}\right) = -12\).<br>Nhân toàn bộ phương trình thứ nhất với \(-12\):<br>\((-12)\cdot\dfrac{3}{4}x - (-12)\cdot\dfrac{5}{6}y = (-12)\cdot 5 \Rightarrow -9x + 10y = -60\).<br>Đồng nhất với \(ax + 10y = b\), ta được \(a = -9\) và \(b = -60\). Vậy \(a + b = -9 + (-60) = -69\).''',
        r'''Cách nhanh nhất cho hệ phân số vô số nghiệm là tìm hệ số nhân \(k\) từ cặp hệ số đã biết đầy đủ rồi nhân cả 3 hạng tử cho \(k\) — luôn chú ý dấu âm!''',
        desmos_tip_vi=r'''Tính ngay trong Desmos: <code>k = 10 / (-5/6)</code> ra \(-12\), rồi <code>a = (3/4)*k</code> (\(-9\)), <code>b = 5*k</code> (\(-60\)), và <code>a + b = -69</code>.''',
    ))

    # =========================================================================
    # Q6 — Algebra (Hard, MCQ -> A) | Area of Triangular Feasible Region
    # =========================================================================
    qs.append(math_mcq(
        'sat_mm4_m2h_q6', 6, 'Algebra', 'Systems of linear inequalities — feasible region geometry', 'Hard',
        r'''<p>In the \(xy\)-plane, the solution set of the system of inequalities below forms a triangular region:</p><p style="text-align:center;">\[\begin{aligned} y &\le 3x + 6 \\ y &\le -2x + 26 \\ y &\ge 0 \end{aligned}\]</p>''',
        r'''<p>What is the area of this triangular region?</p>''',
        {
            'A': r'135',
            'B': r'117',
            'C': r'270',
            'D': r'99',
        },
        'A',
        r'''Tìm tọa độ 3 đỉnh của tam giác tạo bởi ba đường biên:<br>1. Hai giao điểm với trục hoành \(y = 0\):<br>&nbsp;&nbsp;• \(3x + 6 = 0 \Rightarrow x_1 = -2\) (đỉnh \((-2, 0)\))<br>&nbsp;&nbsp;• \(-2x + 26 = 0 \Rightarrow x_2 = 13\) (đỉnh \((13, 0)\))<br>&nbsp;&nbsp;Chiều dài cạnh đáy trên trục \(Ox\): \(B = 13 - (-2) = 15\).<br>2. Đỉnh trên cùng (giao điểm hai đường thẳng):<br>&nbsp;&nbsp;\(3x + 6 = -2x + 26 \Rightarrow 5x = 20 \Rightarrow x = 4 \Rightarrow y = 3(4) + 6 = 18\) (đỉnh \((4, 18)\)).<br>3. Chiều cao \(H = 18\), do đó diện tích tam giác là \(\dfrac{1}{2} \cdot 15 \cdot 18 = 135\).''',
        r'''Khi tính đáy tam giác trên trục \(Ox\), luôn lấy \(x_{\text{phải}} - x_{\text{trái}}\); nếu \(x_{\text{trái}}\) âm thì khoảng cách sẽ cộng thêm \(|x_{\text{trái}}|\).''',
        {
            'A': ('Correct', r'Đáy \(13 - (-2) = 15\), chiều cao \(18\), diện tích \(\frac{1}{2}(15)(18) = 135\).'),
            'B': ('First-Quadrant Restriction Trap', r'Bỏ sót phần tam giác nằm bên trái trục \(Oy\), tính đáy từ \(0\) đến \(13\): \(\frac{1}{2}(13)(18) = 117\).'),
            'C': ('Forgot Factor of 1/2', r'Lấy \(15 \times 18 = 270\) mà quên chia đôi trong công thức diện tích tam giác.'),
            'D': ('Sign Error on Base Length', r'Tính sai độ dài đáy thành \(13 - 2 = 11\), ra \(\frac{1}{2}(11)(18) = 99\).'),
        },
        desmos_tip_vi=r'''Nhập cả 3 bất phương trình vào Desmos để hiện rõ vùng tam giác đậm nhất; bấm vào 3 đỉnh \((-2, 0), (13, 0), (4, 18)\) rồi tính <code>0.5 * (13 - (-2)) * 18 = 135</code>.''',
    ))

    # =========================================================================
    # Q7 — Algebra (Hard, MCQ -> C) | Linear Function Composition f(f(x))
    # =========================================================================
    qs.append(math_mcq(
        'sat_mm4_m2h_q7', 7, 'Algebra', 'Composition of linear functions', 'Hard',
        r'''<p>Let \(f(x) = ax + b\) be a linear function, where \(a\) and \(b\) are constants with \(a > 0\). For all real numbers \(x\):</p><p style="text-align:center;">\[f(f(x)) = 9x - 16\]</p>''',
        r'''<p>What is the value of \(f(5)\)?</p>''',
        {
            'A': r'\(-1\)',
            'B': r'\(7\)',
            'C': r'\(11\)',
            'D': r'\(29\)',
        },
        'C',
        r'''Thay \(f(x) = ax + b\) vào chính nó:<br>\(f(f(x)) = a(ax + b) + b = a^2 x + (ab + b) = a^2 x + b(a + 1)\).<br>Đồng nhất hệ số với \(9x - 16\):<br>• \(a^2 = 9\) và \(a > 0 \Rightarrow a = 3\).<br>• \(b(a + 1) = -16 \Rightarrow 4b = -16 \Rightarrow b = -4\).<br>Vậy \(f(x) = 3x - 4\), suy ra \(f(5) = 3(5) - 4 = 11\).''',
        r'''Với hàm hợp \(f(f(x))\) của hàm tuyến tính \(ax + b\), hằng số tự do mới là \(b(a + 1)\), KHÔNG phải \(2b\) hay \(b^2\).''',
        {
            'A': ('Unscaled Constant Trap', r'Giữ nguyên \(b = -16\) nên tính \(3(5) - 16 = -1\).'),
            'B': ('Doubled Constant Trap', r'Nhầm hằng số tự do là \(2b = -16 \Rightarrow b = -8\), tính \(3(5) - 8 = 7\).'),
            'C': ('Correct', r'Đồng nhất chuẩn ra \(a = 3, b = -4 \Rightarrow f(5) = 3(5) - 4 = 11\).'),
            'D': ('Evaluated Composite Function', r'Thay \(x = 5\) thẳng vào \(f(f(x)) = 9(5) - 16 = 29\) thay vì tính \(f(5)\).'),
        },
        desmos_tip_vi=r'''Định nghĩa <code>f(x) = ax + b</code> với thanh trượt \(a, b\), rồi vẽ <code>y = f(f(x))</code> và <code>y = 9x - 16</code>; khi \(a = 3, b = -4\) hai đường trùng khít và gõ <code>f(5)</code> ra ngay 11.''',
    ))

    # =========================================================================
    # Q8 — Algebra (Hard, MCQ -> B) | Line Translation in xy-Plane
    # =========================================================================
    qs.append(math_mcq(
        'sat_mm4_m2h_q8', 8, 'Algebra', 'Translations of linear graphs', 'Hard',
        r'''<p>In the \(xy\)-plane, the line defined by \(3x - 4y = 24\) is translated \(4\) units to the right and \(k\) units upward. The resulting line passes through the origin \((0, 0)\).</p>''',
        r'''<p>What is the value of \(k\)?</p>''',
        {
            'A': r'3',
            'B': r'9',
            'C': r'6',
            'D': r'12',
        },
        'B',
        r'''Bước 1: Đưa đường thẳng gốc về dạng \(y = mx + b\): \(4y = 3x - 24 \Rightarrow y = \dfrac{3}{4}x - 6\).<br>Bước 2: Tịnh tiến sang phải \(4\) đơn vị (thay \(x\) bằng \(x - 4\)) và lên trên \(k\) đơn vị (cộng thêm \(k\) vào vế phải):<br>\(y = \dfrac{3}{4}(x - 4) - 6 + k = \dfrac{3}{4}x - 3 - 6 + k = \dfrac{3}{4}x - 9 + k\).<br>Bước 3: Đường mới đi qua \((0, 0)\) nên tung độ gốc mới bằng \(0\): \(-9 + k = 0 \Rightarrow k = 9\).''',
        r'''Quy tắc tịnh tiến bất di bất dịch: dịch sang PHẢI \(h\) đơn vị thì thay \(x \to (x - h)\), dịch LÊN \(k\) đơn vị thì cộng \(+k\) (hoặc thay \(y \to y - k\)).''',
        {
            'A': ('Horizontal Shift Sign Reversal', r'Thay nhầm \(x \to x + 4\) (dịch trái thay vì phải), dẫn đến \(+3 - 6 + k = 0 \Rightarrow k = 3\).'),
            'B': ('Correct', r'Thay \(x \to x - 4\) làm tung độ gốc hạ từ \(-6\) xuống \(-9\), nên cần dịch lên \(k = 9\) đơn vị.'),
            'C': ('Ignored Horizontal Shift', r'Chỉ triệt tiêu tung độ gốc ban đầu \(-6\) mà bỏ qua tác động của phép dịch phải 4 đơn vị.'),
            'D': ('Intercept Confusion', r'Dịch hoành độ gốc từ 8 sang 12 rồi lấy nhầm 12 làm khoảng dịch chuyển đứng \(k\).'),
        },
        desmos_tip_vi=r'''Vẽ đường tịnh tiến trực tiếp <code>3(x - 4) - 4(y - k) = 24</code> với thanh trượt \(k\) và kéo tới khi đường thẳng đi qua gốc tọa độ \((0, 0)\) tại \(k = 9\).''',
    ))

    # =========================================================================
    # Q9 — Advanced Math (Medium-Hard, SPR -> 15) | Theme: EV Battery Discharge
    # =========================================================================
    qs.append(math_spr(
        'sat_mm4_m2h_q9', 9, 'Advanced Math', 'Exponential equations & half-life decay', 'Medium-Hard',
        r'''<p>During a continuous stress test, the remaining stored energy \(Q(t)\), in kilowatt-hours, of an electric vehicle battery pack \(t\) hours after the test begins is modeled by:</p><p style="text-align:center;">\[Q(t) = 128\left(\dfrac{1}{2}\right)^{t/3}\]</p>''',
        r'''<p>After how many hours will the battery pack's remaining stored energy equal \(4\) kilowatt-hours?</p>''',
        ['15'],
        '15',
        r'''Đặt \(Q(t) = 4\): \(128\left(\dfrac{1}{2}\right)^{t/3} = 4\). Chia hai vế cho \(128\):<br>\(\left(\dfrac{1}{2}\right)^{t/3} = \dfrac{4}{128} = \dfrac{1}{32} = \left(\dfrac{1}{2}\right)^5\).<br>Đồng nhất số mũ hai vế cùng cơ số \(\dfrac{1}{2}\): \(\dfrac{t}{3} = 5 \Rightarrow t = 15\) giờ.''',
        r'''Với phương trình mũ có cùng cơ số lũy thừa của \(2\), chia hệ số đứng trước rồi đưa về dạng \((1/2)^n\) để đọc ngay số mũ mà không cần logarit.''',
        desmos_tip_vi=r'''Vẽ <code>y = 128*(0.5)^(x/3)</code> và đường ngang <code>y = 4</code> trong Desmos, bấm giao điểm sẽ đọc ngay \(x = 15\).''',
    ))

    # =========================================================================
    # Q10 — Advanced Math (Medium-Hard, MCQ -> D) | Polynomial Remainder Theorem
    # =========================================================================
    qs.append(math_mcq(
        'sat_mm4_m2h_q10', 10, 'Advanced Math', 'Polynomial factor & remainder theorems', 'Medium-Hard',
        r'''<p>The polynomial \(P(x) = x^3 - 4x^2 + kx - 12\), where \(k\) is a constant, is divisible by \((x - 3)\).</p>''',
        r'''<p>What is the remainder when \(P(x)\) is divided by \((x + 1)\)?</p>''',
        {
            'A': r'\(7\)',
            'B': r'\(-8\)',
            'C': r'\(-16\)',
            'D': r'\(-24\)',
        },
        'D',
        r'''Bước 1: Áp dụng Định lý Nhân tử: \(P(x)\) chia hết cho \((x - 3)\) khi và chỉ khi \(P(3) = 0\):<br>\(3^3 - 4(3^2) + 3k - 12 = 0 \Rightarrow 27 - 36 + 3k - 12 = 0 \Rightarrow 3k - 21 = 0 \Rightarrow k = 7\).<br>Bước 2: Áp dụng Định lý Số dư: số dư khi chia \(P(x) = x^3 - 4x^2 + 7x - 12\) cho \((x + 1)\) là \(P(-1)\):<br>\(P(-1) = (-1)^3 - 4(-1)^2 + 7(-1) - 12 = -1 - 4 - 7 - 12 = -24\).''',
        r'''Chia cho \((x - r)\) có số dư là \(P(r)\); đặc biệt chia cho \((x + 1) = (x - (-1))\) phải thay \(x = -1\) và tính cẩn thận dấu của \((-1)^2 = +1\).''',
        {
            'A': ('Stopped at Parameter k', r'7 chỉ là giá trị của hằng số \(k\), chưa tính số dư \(P(-1)\).'),
            'B': ('Sign Error on Divisor Root', r'Thay nhầm \(x = +1\) thay vì \(x = -1\): \(P(1) = 1 - 4 + 7 - 12 = -8\).'),
            'C': ('Square Sign Trap', r'Tính sai \(-4(-1)^2\) thành \(+4\) thay vì \(-4\), ra \(-1 + 4 - 7 - 12 = -16\).'),
            'D': ('Correct', r'Tìm đúng \(k = 7\) rồi tính chính xác \(P(-1) = -1 - 4 - 7 - 12 = -24\).'),
        },
        desmos_tip_vi=r'''Nhập <code>P(x) = x^3 - 4x^2 + kx - 12</code> kèm thanh trượt \(k\), điều chỉnh đến khi <code>P(3) = 0</code> (tại \(k = 7\)), rồi gõ <code>P(-1)</code> đọc ngay \(-24\).''',
    ))

    # =========================================================================
    # Q11 — Advanced Math (Hard, MCQ -> A) | Line Tangent to Parabola (Delta = 0)
    # =========================================================================
    qs.append(math_mcq(
        'sat_mm4_m2h_q11', 11, 'Advanced Math', 'Nonlinear systems & discriminant tangency', 'Hard',
        r'''<p>In the \(xy\)-plane, the line \(y = 4x + c\) intersects the parabola \(y = 2x^2 - 8x + 15\) at exactly one point, where \(c\) is a constant.</p>''',
        r'''<p>What is the value of \(c\)?</p>''',
        {
            'A': r'\(-3\)',
            'B': r'\(3\)',
            'C': r'\(7\)',
            'D': r'\(13\)',
        },
        'A',
        r'''Lập phương trình hoành độ giao điểm:<br>\(2x^2 - 8x + 15 = 4x + c \Rightarrow 2x^2 - 12x + (15 - c) = 0\).<br>Đường thẳng cắt parabol tại đúng một điểm (tiếp xúc) khi và chỉ khi biệt thức \(\Delta = b^2 - 4ac = 0\):<br>\((-12)^2 - 4(2)(15 - c) = 0 \Rightarrow 144 - 8(15 - c) = 0 \Rightarrow 15 - c = 18 \Rightarrow c = -3\).<br>(Kiểm tra: \(2x^2 - 12x + 18 = 2(x - 3)^2 = 0\), tiếp điểm duy nhất tại \((3, 9)\).)''',
        r'''Hệ gồm 1 đường thẳng và 1 parabol có đúng 1 nghiệm khi đưa về phương trình bậc hai \(Ax^2 + Bx + C = 0\) và đặt \(\Delta = B^2 - 4AC = 0\).''',
        {
            'A': ('Correct', r'Chuyển vế đúng ra \(2x^2 - 12x + (15 - c) = 0\) và giải \(\Delta = 0\) được \(c = -3\).'),
            'B': ('Sign Error or Found Tangency x', r'Giải nhầm dấu từ \(15 - c = 18\) thành \(c = 3\) (hoặc chọn nhầm hoành độ tiếp điểm \(x = 3\)).'),
            'C': ('Dropped Linear Term 4x', r'Quên chuyển \(4x\) sang vế trái, giải \(\Delta\) của \(2x^2 - 8x + (15 - c) = 0\) ra \(c = 7\).'),
            'D': ('Sign Error Combining x Terms', r'Cộng nhầm \(-8x + 4x = -4x\) thay vì \(-8x - 4x = -12x\), giải ra \(c = 13\).'),
        },
        desmos_tip_vi=r'''Vẽ <code>y = 2x^2 - 8x + 15</code> và <code>y = 4x + c</code> với thanh trượt \(c\); kéo thanh trượt đến khi đường thẳng chạm đúng một điểm vào parabol tại \(c = -3\).''',
    ))

    # =========================================================================
    # Q12 — Advanced Math (Hard, MCQ -> C) | Vieta Transformation (r^2 + s^2)
    # =========================================================================
    qs.append(math_mcq(
        'sat_mm4_m2h_q12', 12, 'Advanced Math', 'Quadratic equations — Vieta identities', 'Hard',
        r'''<p>The quadratic equation \(3x^2 - 18x + k = 0\), where \(k\) is a constant, has two distinct real solutions \(r\) and \(s\) such that \(r^2 + s^2 = 26\).</p>''',
        r'''<p>What is the value of \(k\)?</p>''',
        {
            'A': r'5',
            'B': r'10',
            'C': r'15',
            'D': r'30',
        },
        'C',
        r'''Theo định lý Viète cho phương trình \(3x^2 - 18x + k = 0\):<br>• Tổng hai nghiệm: \(r + s = -\dfrac{-18}{3} = 6\).<br>• Tích hai nghiệm: \(rs = \dfrac{k}{3}\).<br>Dùng hằng đẳng thức \(r^2 + s^2 = (r + s)^2 - 2rs\):<br>\(26 = 6^2 - 2\left(\dfrac{k}{3}\right) \Rightarrow 26 = 36 - \dfrac{2k}{3} \Rightarrow \dfrac{2k}{3} = 10 \Rightarrow k = 15\).<br>(Kiểm tra: \(3x^2 - 18x + 15 = 3(x - 1)(x - 5) = 0\), hai nghiệm \(1\) và \(5\) thỏa \(1^2 + 5^2 = 26\).)''',
        r'''Ghi nhớ bộ đôi Viète + hằng đẳng thức \(r^2 + s^2 = (r + s)^2 - 2rs\); luôn nhớ chia cho hệ số dẫn đầu \(a\) khi viết \(r + s = -b/a\) và \(rs = c/a\).''',
        {
            'A': ('Forgot Leading Coefficient a', r'Tính đúng tích \(rs = 5\) nhưng quên nhân với \(a = 3\) để tìm \(k = 3rs = 15\).'),
            'B': ('Stopped at 2rs', r'Tìm ra \(2rs = 10\) rồi chọn ngay 10 thay vì giải cho \(k\).'),
            'C': ('Correct', r'Giải \(\frac{2k}{3} = 36 - 26 = 10\) cho chính xác \(k = 15\).'),
            'D': ('Dropped Factor of 2', r'Dùng sai hằng đẳng thức \(r^2 + s^2 = (r + s)^2 - rs\), dẫn đến \(k/3 = 10 \Rightarrow k = 30\).'),
        },
        desmos_tip_vi=r'''Vẽ <code>y = 3x^2 - 18x + k</code> với thanh trượt \(k\); thử đáp án \(k = 15\) thấy ngay hai nghiệm trục hoành là \(1\) và \(5\), kiểm tra \(1^2 + 5^2 = 26\) chuẩn xác!''',
    ))

    # =========================================================================
    # Q13 — Advanced Math (Hard, SPR -> 21) | Theme: Forestry Carbon Valuation
    # =========================================================================
    qs.append(math_spr(
        'sat_mm4_m2h_q13', 13, 'Advanced Math', 'Rewriting exponential functions & equivalent bases', 'Hard',
        r'''<p>The estimated market value \(V(t)\), in thousands of dollars, of a certified sustainable timber plantation \(t\) years after establishment is modeled by:</p><p style="text-align:center;">\[V(t) = 250(1.331)^{2t/3}\]</p><p>The model can be rewritten in the equivalent form \(V(t) = 250\left(1 + \dfrac{p}{100}\right)^t\), where \(p\) is a positive constant representing the effective annual percentage growth rate.</p>''',
        r'''<p>What is the value of \(p\)?</p>''',
        ['21'],
        '21',
        r'''Tách số mũ để đưa về dạng cơ số lũy thừa bậc \(t\):<br>\((1.331)^{2t/3} = \left[(1.331)^{2/3}\right]^t\).<br>Nhận thấy \(1.331 = 1.1^3\) (vì \(11^3 = 1331\)), do đó:<br>\((1.331)^{2/3} = \left(1.1^3\right)^{2/3} = 1.1^2 = 1.21\).<br>So sánh với \(1 + \dfrac{p}{100} = 1.21 \Rightarrow \dfrac{p}{100} = 0.21 \Rightarrow p = 21\).''',
        r'''Để đổi hàm mũ \(a^{kt}\) về dạng lãi suất hàng năm \((1 + r)^t\), chỉ cần tính giá trị chính xác của \(a^k\) rồi trừ đi \(1\) và nhân \(100\%\).''',
        desmos_tip_vi=r'''Gõ trực tiếp <code>(1.331^(2/3) - 1) * 100</code> vào Desmos — máy tính trả ngay kết quả chính xác tuyệt đối <code>21</code> trong 2 giây!''',
    ))

    # =========================================================================
    # Q14 — Advanced Math (Hard 750–800 Boss, MCQ -> B) | Parametric Parabola
    # =========================================================================
    qs.append(math_mcq(
        'sat_mm4_m2h_q14', 14, 'Advanced Math', 'Quadratic symmetry & vertex-form parameters', 'Hard',
        r'''<p>Consider the quadratic function \(g(x) = a(x - 4)^2 + k\), where \(a\) and \(k\) are nonzero constants. The graph of \(y = g(x)\) in the \(xy\)-plane passes through the points \((1, 20)\) and \((9, 68)\). Suppose \(p\) is a constant such that \(p \ne 11\) and \(g(p) = g(11)\).</p>''',
        r'''<p>What is the value of \(g(p) - g(4)\)?</p>''',
        {
            'A': r'140',
            'B': r'147',
            'C': r'133',
            'D': r'154',
        },
        'B',
        r'''Bước 1: Thay hai điểm \((1, 20)\) và \((9, 68)\) vào \(g(x) = a(x - 4)^2 + k\):<br>• \(g(1) = a(1 - 4)^2 + k = 9a + k = 20\)<br>• \(g(9) = a(9 - 4)^2 + k = 25a + k = 68\)<br>Trừ phương trình trên từ phương trình dưới: \(16a = 48 \Rightarrow a = 3\), và \(k = 20 - 9(3) = -7\).<br>Bước 2: Vì \(g(p) = g(11)\) (điểm đối xứng \(p = -3\) qua trục \(x = 4\)) và \(g(4) = k\), ta có phím tắt trực tiếp:<br>\(g(p) - g(4) = g(11) - k = \left[a(11 - 4)^2 + k\right] - k = a(7)^2 = 3(49) = 147\).<br>(Kiểm tra đầy đủ: \(g(11) = 3(49) - 7 = 140\) và \(g(4) = -7 \Rightarrow 140 - (-7) = 147\).)''',
        r'''Mẹo 800 Math: Khi trừ hai giá trị hàm parabol dạng đỉnh \(g(x_1) - g(h)\), hằng số \(k\) tự triệt tiêu hoàn toàn, còn lại đúng \(a(x_1 - h)^2\)!''',
        {
            'A': ('Omitted -g(4)', r'140 chỉ là giá trị của \(g(p) = g(11)\), quên trừ đi \(g(4) = -7\).'),
            'B': ('Correct', r'\(g(11) = 140\) và \(g(4) = -7\), hiệu \(140 - (-7) = 147\) (cũng bằng \(3 \cdot 7^2\)).'),
            'C': ('Double Negative Error', r'Tính sai \(140 - (-7)\) thành \(140 - 7 = 133\).'),
            'D': ('Added Constant Twice', r'Tính \(3(49) + 7 = 154\) thay vì \(3(49) = 147\).'),
        },
        desmos_tip_vi=r'''Dùng Desmos giải hệ <code>9a + k = 20</code> và <code>25a + k = 68</code> (đổi biến thành \(x, y\)) ra \((3, -7)\), rồi nhập <code>g(x) = 3(x - 4)^2 - 7</code> và tính <code>g(11) - g(4) = 147</code>.''',
    ))

    # =========================================================================
    # Q15 — Advanced Math (Hard 750–800 Boss, MCQ -> D) | Rational No-Solution Sum
    # =========================================================================
    qs.append(math_mcq(
        'sat_mm4_m2h_q15', 15, 'Advanced Math', 'Rational equations with parameters & extraneous roots', 'Hard',
        r'''<p>In the rational equation below, \(m\) is a real constant:</p><p style="text-align:center;">\[\dfrac{2x + m}{x - 3} + \dfrac{x - 1}{x + 2} = 3\]</p>''',
        r'''<p>What is the sum of all values of \(m\) for which the equation has no real solution?</p>''',
        {
            'A': r'\(-3\)',
            'B': r'\(-6\)',
            'C': r'\(3\)',
            'D': r'\(-9\)',
        },
        'D',
        r'''Điều kiện xác định: \(x \ne 3\) và \(x \ne -2\). Nhân cả hai vế với mẫu chung \((x - 3)(x + 2)\):<br>\((2x + m)(x + 2) + (x - 1)(x - 3) = 3(x - 3)(x + 2)\)<br>\(\left[2x^2 + (m + 4)x + 2m\right] + \left[x^2 - 4x + 3\right] = 3x^2 - 3x - 18\)<br>Rút gọn \(3x^2\) ở hai vế: \(mx + 2m + 3 = -3x - 18 \Rightarrow (m + 3)x = -2m - 21\).<br>Phương trình vô nghiệm trong ĐÚNG hai trường hợp:<br>• <b>Trường hợp 1 (Phương trình bậc nhất suy biến vô nghiệm):</b> \(m + 3 = 0 \Rightarrow m = -3\). Khi đó \(0x = -15\) (vô nghiệm).<br>• <b>Trường hợp 2 (Nghiệm duy nhất trùng nghiệm ngoại lai bị loại):</b> \(x = \dfrac{-2m - 21}{m + 3}\).<br>&nbsp;&nbsp;– Thử \(x = 3\): \(-2m - 21 = 3(m + 3) \Rightarrow 5m = -30 \Rightarrow m = -6\) (thỏa mãn vô nghiệm!).<br>&nbsp;&nbsp;– Thử \(x = -2\): \(-2m - 21 = -2(m + 3) \Rightarrow -21 = -6\) (không có giá trị \(m\)).<br>Tổng tất cả giá trị \(m\) là \((-3) + (-6) = -9\).''',
        r'''Bẫy 780–800 của phương trình phân thức chứa tham số: phương trình vô nghiệm không chỉ khi hệ số \(x\) bằng \(0\), mà còn khi nghiệm tìm được rơi đúng vào điểm làm mẫu số bằng \(0\)!''',
        {
            'A': ('Missed Extraneous Root Case', r'Chỉ xét trường hợp hệ số \(m + 3 = 0 \Rightarrow m = -3\), bỏ sót trường hợp nghiệm trùng mẫu \(x = 3\) (\(m = -6\)).'),
            'B': ('Missed Degenerate Linear Case', r'Chỉ xét điều kiện nghiệm trùng mẫu \(x = 3 \Rightarrow m = -6\), bỏ sót \(m = -3\).'),
            'C': ('Sign Error', r'Giải nhầm dấu từ \(m + 3 = 0\) thành \(m = +3\).'),
            'D': ('Correct', r'Đủ cả hai trường hợp vô nghiệm \(m = -3\) và \(m = -6\), tổng bằng \(-9\).'),
        },
        desmos_tip_vi=r'''Vẽ <code>y = (2x + m)/(x - 3) + (x - 1)/(x + 2)</code> và <code>y = 3</code> với thanh trượt \(m\); kiểm tra tại \(m = -3\) (đường tiệm cận ngang \(y = 3\) không cắt) và \(m = -6\) (lỗ hổng ngay tại \(x = 3\)) đều không có giao điểm thực!''',
    ))

    # =========================================================================
    # Q16 — Data Analysis (Hard 750–800, SPR -> 72) | Theme: Archaeological Grid Scan
    # =========================================================================
    qs.append(math_spr(
        'sat_mm4_m2h_q16', 16, 'Problem-Solving and Data Analysis', 'Squared-unit area conversions & rates', 'Hard',
        r'''<p>An archaeological excavation site is a square region with side length \(0.3\) kilometers. An autonomous ground-penetrating radar cart scans the site at a constant rate of \(750\) square meters per minute. After scanning \(60\%\) of the site's total area, the cart pauses to recharge its electric battery.</p><p><em>(Note: \(1\text{ kilometer} = 1{,}000\text{ meters}\).)</em></p>''',
        r'''<p>How many minutes did the cart spend scanning before pausing to recharge?</p>''',
        ['72'],
        '72',
        r'''Bước 1: Đổi cạnh hình vuông sang mét TRƯỚC khi bình phương để tránh lỗi đơn vị diện tích:<br>\(0.3\text{ km} = 0.3 \times 1{,}000 = 300\text{ m}\).<br>Bước 2: Tính tổng diện tích khu khai quật: \(A_{\text{tổng}} = 300^2 = 90{,}000\text{ m}^2\).<br>Bước 3: Tính \(60\%\) diện tích đã quét: \(A_{\text{quét}} = 0.60 \times 90{,}000 = 54{,}000\text{ m}^2\).<br>Bước 4: Thời gian quét: \(t = \dfrac{54{,}000}{750} = 72\) phút.''',
        r'''Với đơn vị diện tích (\(\text{km}^2 \to \text{m}^2\)), luôn đổi đơn vị chiều dài trước khi bình phương hoặc nhân hệ số bình phương \(1{,}000^2 = 10^6\).''',
        desmos_tip_vi=r'''Tính gọn một dòng trong Desmos: <code>0.60 * (0.3 * 1000)^2 / 750</code> sẽ trả ngay kết quả chính xác <code>72</code>.''',
    ))

    # =========================================================================
    # Q17 — Data Analysis (Hard 750–800, MCQ -> C) | Theme: Clinical Trials SD Table
    # =========================================================================
    tbl_q17 = build_math_table(
        ['Recovery Time (days)', 'Cohort A (Number of Patients)', 'Cohort B (Number of Patients)'],
        [
            ['4', '1', '5'],
            ['5', '3', '2'],
            ['6', '7', '1'],
            ['7', '3', '2'],
            ['8', '1', '5'],
        ],
        caption='Post-Treatment Recovery Times for Two Clinical Trial Cohorts (n = 15 each)'
    )
    qs.append(math_mcq(
        'sat_mm4_m2h_q17', 17, 'Problem-Solving and Data Analysis', 'Comparing standard deviation & center from distributions', 'Hard',
        rf'''<p>A clinical research team recorded the recovery times, in days, of two cohorts of \(15\) patients each, as summarized in the frequency table below.</p>{tbl_q17}''',
        r'''<p>Which of the following statements accurately compares the means and standard deviations of the recovery times for Cohort A and Cohort B?</p>''',
        {
            'A': r'Cohort A has a greater mean and a greater standard deviation than Cohort B.',
            'B': r'Cohort A and Cohort B have the same mean, and Cohort A has a greater standard deviation than Cohort B.',
            'C': r'Cohort A and Cohort B have the same mean, and Cohort B has a greater standard deviation than Cohort A.',
            'D': r'Cohort A and Cohort B have the same mean and the same standard deviation because both cohorts have the same range of \(4\) days.',
        },
        'C',
        r'''Bước 1 (So sánh giá trị trung bình): Cả hai nhóm Cohort A và Cohort B đều có bảng tần số đối xứng hoàn toàn qua giá trị chính giữa là \(6\) ngày (\(1\text{-}3\text{-}7\text{-}3\text{-}1\) và \(5\text{-}2\text{-}1\text{-}2\text{-}5\)), nên cả hai nhóm có cùng giá trị trung bình \(\bar{x}_A = \bar{x}_B = 6\) ngày.<br>Bước 2 (So sánh độ lệch chuẩn SD): Độ lệch chuẩn đo mức độ phân tán trung bình quanh giá trị trung bình \(6\). Ở Cohort A, phần lớn dữ liệu tập trung sát trung tâm (\(7\) bệnh nhân tại \(6\) ngày). Ở Cohort B, dữ liệu dồn mạnh ra hai đầu mút xa trung tâm (\(5\) bệnh nhân tại \(4\) ngày và \(5\) bệnh nhân tại \(8\) ngày). Cụ thể, phương sai \(\sigma_A^2 = \dfrac{14}{15} < \sigma_B^2 = \dfrac{44}{15}\), nên Cohort B có độ lệch chuẩn lớn hơn.''',
        r'''Khi hai phân phối có cùng trung bình và cùng khoảng biến thiên (range), phân phối nào tập trung nhiều giá trị ở hai đầu mút (tails) hơn sẽ có độ lệch chuẩn (SD) LỚN hơn.''',
        {
            'A': ('Misread Center & Spread', r'Cả hai bảng đều đối xứng quanh 6 nên trung bình bằng nhau; Cohort A tập trung quanh tâm hơn nên SD nhỏ hơn.'),
            'B': ('Inverted SD Intuition', r'Nhầm lẫn rằng cột cao nhất ở giữa (7 người ở mức 6) tạo ra độ lệch chuẩn lớn hơn — thực tế tập trung ở tâm làm SD nhỏ đi.'),
            'C': ('Correct', r'Cùng trung bình 6 ngày nhờ tính đối xứng, và Cohort B phân tán mạnh ra hai biên (4 và 8 ngày) nên có SD lớn hơn.'),
            'D': ('Range-Equals-SD Fallacy', r'Bẫy kinh điển SAT: cùng range (8 − 4 = 4) KHÔNG hề suy ra cùng độ lệch chuẩn.'),
        },
        desmos_tip_vi=r'''Kiểm chứng trong Desmos: tạo danh sách <code>A = [4,5,5,5,6,6,6,6,6,6,6,7,7,7,8]</code> và <code>B = [4,4,4,4,4,5,5,6,7,7,8,8,8,8,8]</code> rồi gõ <code>stdevp(A)</code> (\(\approx 0.97\)) vs <code>stdevp(B)</code> (\(\approx 1.71\)).''',
    ))

    # =========================================================================
    # Q18 — Data Analysis (Hard 750–800, MCQ -> A) | Theme: University EV Poll Table
    # =========================================================================
    tbl_q18 = build_math_table(
        ['Student Status', 'Support', 'Oppose', 'Total'],
        [
            ['Undergraduate', '180', '60', '240'],
            ['Graduate', 'k', '40', 'k + 40'],
            ['Total', '180 + k', '100', '280 + k'],
        ],
        caption='University Poll on Expanding Solar EV Charging Lots'
    )
    qs.append(math_mcq(
        'sat_mm4_m2h_q18', 18, 'Problem-Solving and Data Analysis', 'Parametric two-way tables & conditional probability', 'Hard',
        r'''<p>A university polling center surveyed undergraduate and graduate students on whether they support expanding solar-powered EV charging lots on campus. The results are partially summarized in the table below, where \(k\) is a positive integer.</p>''' + tbl_q18 + r'''<p>If a student who <b>supports</b> the expansion is selected at random, the probability that the student is a <b>graduate</b> student is \(\dfrac{2}{5}\).</p>''',
        r'''<p>If a <b>graduate</b> student is selected at random from those surveyed, what is the probability that this student <b>opposes</b> the expansion?</p>''',
        {
            'A': r'\(\dfrac{1}{4}\)',
            'B': r'\(\dfrac{1}{10}\)',
            'C': r'\(\dfrac{2}{5}\)',
            'D': r'\(\dfrac{1}{3}\)',
        },
        'A',
        r'''Bước 1: Dùng dữ kiện xác suất có điều kiện \(P(\text{Graduate} \mid \text{Support}) = \dfrac{2}{5}\) để tìm \(k\):<br>\(\dfrac{k}{180 + k} = \dfrac{2}{5} \Rightarrow 5k = 360 + 2k \Rightarrow 3k = 360 \Rightarrow k = 120\).<br>Bước 2: Tính tổng số sinh viên cao học (Graduate): \(k + 40 = 120 + 40 = 160\).<br>Bước 3: Tính xác suất có điều kiện đề hỏi \(P(\text{Oppose} \mid \text{Graduate})\):<br>\(\dfrac{40}{160} = \dfrac{1}{4}\).''',
        r'''Bài toán bảng 2 chiều 750+ thường đảo chiều điều kiện giữa dữ kiện cho trước và câu hỏi cuối — luôn gạch chân chính xác mẫu số của TỪNG xác suất!''',
        {
            'A': ('Correct', r'Tìm đúng \(k = 120\), tổng sinh viên cao học là \(160\), suy ra \(P(\text{Oppose} \mid \text{Graduate}) = \frac{40}{160} = \frac{1}{4}\).'),
            'B': ('Grand Total Denominator Trap', r'Chia cho tổng toàn bộ sinh viên \(280 + 120 = 400\) ra \(\frac{40}{400} = \frac{1}{10}\) thay vì riêng nhóm Graduate.'),
            'C': ('Reversed Conditional Probability', r'Tính ngược \(P(\text{Graduate} \mid \text{Oppose}) = \frac{40}{100} = \frac{2}{5}\).'),
            'D': ('Partial Row Denominator Trap', r'Chia 40 cho \(k = 120\) thay vì tổng hàng \(k + 40 = 160\), ra \(\frac{1}{3}\).'),
        },
        desmos_tip_vi=r'''Gõ <code>x / (180 + x) = 2/5</code> vào Desmos để đọc ngay \(k = 120\), rồi tính <code>40 / (120 + 40)</code> và đổi sang phân số ra <code>1/4</code>.''',
    ))

    # =========================================================================
    # Q19 — Data Analysis (Hard 750–800, SPR -> 450) | Theme: Timber Parcels Mean
    # =========================================================================
    qs.append(math_spr(
        'sat_mm4_m2h_q19', 19, 'Problem-Solving and Data Analysis', 'Weighted averages of combined groups', 'Hard',
        r'''<p>A sustainable timber company harvests two forest parcels, Parcel North and Parcel South. Parcel North covers \(300\) hectares and yields an average of \(140\) cubic meters of timber per hectare. Parcel South yields an average of \(215\) cubic meters of timber per hectare. Across both parcels combined, the overall average yield is \(185\) cubic meters of timber per hectare.</p>''',
        r'''<p>How many hectares does Parcel South cover?</p>''',
        ['450'],
        '450',
        r'''Cách 1 (Phương trình trung bình có trọng số): Gọi \(S\) là diện tích (ha) của Parcel South. Tổng sản lượng hai khu bằng tổng diện tích nhân trung bình chung:<br>\(300(140) + 215S = 185(300 + S)\)<br>\(42{,}000 + 215S = 55{,}500 + 185S \Rightarrow 30S = 13{,}500 \Rightarrow S = 450\text{ ha}\).<br>Cách 2 (Quy tắc đòn bẩy 5 giây): Khoảng cách trung bình chung tới North là \(185 - 140 = 45\), tới South là \(215 - 185 = 30\). Tỉ lệ diện tích nghịch đảo tỉ lệ khoảng cách: \(\dfrac{S}{300} = \dfrac{45}{30} = \dfrac{3}{2} \Rightarrow S = 450\).''',
        r'''Trong bài toán trộn hai nhóm có trung bình khác nhau, tỉ số quy mô hai nhóm luôn NGHỊCH ĐẢO tỉ số khoảng cách của mỗi nhóm tới trung bình chung.''',
        desmos_tip_vi=r'''Gõ phương trình <code>(300*140 + 215x) / (300 + x) = 185</code> vào Desmos (thu nhỏ trục hoành tới 500) sẽ thấy ngay đường thẳng đứng tại \(x = 450\).''',
    ))

    # =========================================================================
    # Q20 — Geometry (Hard 750–800, MCQ -> D) | Theme: Geodesic Dome Circle Eq
    # =========================================================================
    qs.append(math_mcq(
        'sat_mm4_m2h_q20', 20, 'Geometry and Trigonometry', 'Circles in the xy-plane — completing the square', 'Hard',
        r'''<p>In the \(xy\)-plane, the circular footprint of a geodesic dome is given by the equation below, where \(k\) is a constant:</p><p style="text-align:center;">\[2x^2 + 2y^2 - 16x + 24y + k = 0\]</p><p>The radius of the circular footprint is \(7\) units.</p>''',
        r'''<p>What is the value of \(k\)?</p>''',
        {
            'A': r'3',
            'B': r'90',
            'C': r'159',
            'D': r'6',
        },
        'D',
        r'''Bước 1 (Bắt buộc): Chia TẤT CẢ các hạng tử cho \(2\) để hệ số của \(x^2\) và \(y^2\) bằng \(1\):<br>\(x^2 - 8x + y^2 + 12y + \dfrac{k}{2} = 0\).<br>Bước 2: Hoàn thành bình phương cho \(x\) và \(y\):<br>\((x - 4)^2 - 16 + (y + 6)^2 - 36 + \dfrac{k}{2} = 0 \Rightarrow (x - 4)^2 + (y + 6)^2 = 52 - \dfrac{k}{2}\).<br>Bước 3: Vì bán kính \(r = 7\) nên \(r^2 = 49\):<br>\(52 - \dfrac{k}{2} = 49 \Rightarrow \dfrac{k}{2} = 3 \Rightarrow k = 6\).''',
        r'''Bẫy kinh điển 750+ phương trình đường tròn \(Ax^2 + Ay^2 + Dx + Ey + k = 0\): PHẢI chia cả hằng số \(k\) cho \(A\) trước khi hoàn thành bình phương, và đặt vế phải bằng \(r^2\) (không phải \(r\))!''',
        {
            'A': ('Forgot to Divide k by 2', r'Chia các hệ số \(x, y\) cho 2 nhưng quên chia \(k\) cho 2, giải \(52 - k = 49 \Rightarrow k = 3\).'),
            'B': ('Used r Instead of r^2', r'Đặt vế phải bằng \(7\) thay vì \(7^2 = 49\), giải \(52 - k/2 = 7 \Rightarrow k = 90\).'),
            'C': ('Skipped Normalizing by 2', r'Hoàn thành bình phương trực tiếp với \(-16\) và \(+24\) mà không chia 2: \(8^2 + 12^2 - k = 49 \Rightarrow k = 159\).'),
            'D': ('Correct', r'Chia đều cho 2 rồi hoàn thành bình phương chuẩn xác cho \(52 - k/2 = 49 \Rightarrow k = 6\).'),
        },
        desmos_tip_vi=r'''Vẽ thẳng <code>2x^2 + 2y^2 - 16x + 24y + k = 0</code> trong Desmos kèm thanh trượt \(k\); đặt \(k = 6\) rồi bấm 2 điểm cao nhất/thấp nhất \((4, 1)\) và \((4, -13)\) thấy ngay đường kính \(14 \Rightarrow r = 7\)!''',
    ))

    # =========================================================================
    # Q21 — Geometry (Hard 750–800, MCQ -> B) | Theme: Geodesic Dome Similar Trusses
    # =========================================================================
    svg_q21 = svg_similar_triangles(
        side_ab='12', side_bc='18', side_de='20', side_ef='',
        v1='A', v2='B', v3='C', v4='D', v5='E', v6='F'
    )
    qs.append(math_mcq(
        'sat_mm4_m2h_q21', 21, 'Geometry and Trigonometry', 'Similar triangles — area scaling ratio', 'Hard',
        f'<div style="text-align:center;margin-bottom:10px;">{svg_q21}</div>' + r'''<p>In the figure above, triangular geodesic dome trusses \(\triangle ABC\) and \(\triangle DEF\) are similar, where vertex \(A\) corresponds to \(D\), \(B\) corresponds to \(E\), and \(C\) corresponds to \(F\). Side lengths are \(AB = 12\text{ m}\), \(BC = 18\text{ m}\), and \(DE = 20\text{ m}\). The sum of the areas of \(\triangle ABC\) and \(\triangle DEF\) is \(272\) square meters.</p>''',
        r'''<p>What is the area of \(\triangle DEF\), in square meters?</p>''',
        {
            'A': r'72',
            'B': r'200',
            'C': r'170',
            'D': r'102',
        },
        'B',
        r'''Bước 1: Tìm tỉ số đồng dạng tuyến tính (tỉ số cạnh tương ứng):<br>\(\dfrac{AB}{DE} = \dfrac{12}{20} = \dfrac{3}{5}\).<br>Bước 2: Tỉ số diện tích bằng BÌNH PHƯƠNG tỉ số đồng dạng:<br>\(\dfrac{\text{Area}(\triangle ABC)}{\text{Area}(\triangle DEF)} = \left(\dfrac{3}{5}\right)^2 = \dfrac{9}{25}\).<br>Bước 3: Đặt \(\text{Area}(\triangle ABC) = 9u\) và \(\text{Area}(\triangle DEF) = 25u\). Theo đề bài:<br>\(9u + 25u = 272 \Rightarrow 34u = 272 \Rightarrow u = 8\).<br>Vậy \(\text{Area}(\triangle DEF) = 25 \times 8 = 200\text{ m}^2\).''',
        r'''Trong hai hình đồng dạng với tỉ số cạnh \(k\), tỉ số diện tích là \(k^2\) (và tỉ số thể tích là \(k^3\)) — đừng bao giờ chia tổng diện tích theo tỉ số cạnh tuyến tính!''',
        {
            'A': ('Found Smaller Triangle Area', r'72 là diện tích của \(\triangle ABC\) (\(9 \times 8 = 72\)), trong khi đề hỏi diện tích \(\triangle DEF\).'),
            'B': ('Correct', r'Chia tổng 272 theo tỉ lệ diện tích \(9 : 25\) cho \(\text{Area}(\triangle DEF) = \frac{25}{34}(272) = 200\).'),
            'C': ('Linear Ratio Trap', r'Chia nhầm theo tỉ số cạnh \(3 : 5\) thay vì \(9 : 25\): \(\frac{5}{8}(272) = 170\).'),
            'D': ('Linear Ratio on Smaller Triangle', r'Tính \(\frac{3}{8}(272) = 102\) — sai cả tỉ số bình phương lẫn chọn nhầm tam giác nhỏ.'),
        },
        desmos_tip_vi=r'''Tính thẳng tỉ phần diện tích trong Desmos: <code>272 * 20^2 / (12^2 + 20^2)</code> ra ngay <code>200</code>.''',
    ))

    # =========================================================================
    # Q22 — Geometry (Hard 750–800 Boss, SPR -> 297) | Theme: Stone Monument Cylinder
    # =========================================================================
    svg_q22 = svg_cylinder(
        r_lbl='r', h_lbl='h',
        note='Note: Figure not drawn to scale.'
    )
    qs.append(math_spr(
        'sat_mm4_m2h_q22', 22, 'Geometry and Trigonometry', '3D solids — cylinder surface area, volume & similarity', 'Hard',
        rf'''<div style="text-align:center;margin-bottom:10px;">{svg_q22}</div><p>A right circular cylindrical stone pedestal at a pyramid monument has base radius \(r\) meters and height \(h\) meters. Its volume is \(180\pi\) cubic meters, and its lateral surface area (the curved side only, given by \(2\pi rh\)) is \(60\pi\) square meters. A second, larger cylindrical pedestal is geometrically similar to the first pedestal and has a base radius of \(9\) meters.</p>''',
        r'''<p>If the total surface area (including both circular bases and the curved side) of the <b>larger</b> pedestal is \(m\pi\) square meters, what is the value of \(m\)?</p>''',
        ['297'],
        '297',
        r'''Bước 1 (Tìm \(r\) và \(h\) của trụ nhỏ):<br>• Thể tích: \(\pi r^2 h = 180\pi \Rightarrow r^2 h = 180\).<br>• Diện tích xung quanh: \(2\pi r h = 60\pi \Rightarrow r h = 30\).<br>Chia hai phương trình cho nhau: \(r = \dfrac{r^2 h}{rh} = \dfrac{180}{30} = 6\text{ m}\), suy ra \(h = \dfrac{30}{6} = 5\text{ m}\).<br>Bước 2 (Tính diện tích toàn phần trụ nhỏ):<br>\(\text{TSA}_1 = 2\pi r^2 + 2\pi rh = 2\pi(6^2) + 60\pi = 72\pi + 60\pi = 132\pi\text{ m}^2\).<br>Bước 3 (Phóng đại đồng dạng sang trụ lớn có bán kính \(R = 9\text{ m}\)):<br>Tỉ số đồng dạng cạnh \(s = \dfrac{9}{6} = \dfrac{3}{2}\), suy ra tỉ số diện tích là \(s^2 = \dfrac{9}{4}\).<br>\(\text{TSA}_2 = \dfrac{9}{4} \cdot 132\pi = 9 \cdot 33\pi = 297\pi \Rightarrow m = 297\).''',
        r'''Với bài toán hình trụ kết hợp thể tích và diện tích xung quanh, chia \(V / (\text{LSA}) = r / 2\) để rút ngay bán kính \(r\) trong 3 giây, rồi dùng tỉ lệ diện tích \(s^2\) để phóng sang hình đồng dạng!''',
        desmos_tip_vi=r'''Kiểm chứng trong Desmos: <code>r = 180/30</code> (6), <code>tsa1 = 2*r^2 + 60</code> (132), rồi <code>tsa1 * (9/6)^2</code> ra ngay <code>297</code>.''',
    ))

    return qs


def verify_math():
    """Programmatic exact arithmetic verification for all 22 Module 2 Hard questions."""
    # Q1: f(4)=17, f(10)=35 -> f(1) + f(7)
    m1 = Fraction(35 - 17, 10 - 4)
    b1 = 17 - m1 * 4
    f1 = lambda x: m1 * x + b1
    assert f1(1) + f1(7) == 34 and f1(1) + f1(7) == 2 * f1(4)

    # Q2: 7x + 4y = 156, 3x - 2y = 26 -> 5x + y
    x2, y2 = Fraction(16), Fraction(11)
    assert 7 * x2 + 4 * y2 == 156 and 3 * x2 - 2 * y2 == 26
    assert 5 * x2 + y2 == 91 and Fraction(156 + 26, 2) == 91

    # Q3: o + m <= 140, 1.8o + 1.2m >= 216 -> min o
    min_o3 = (Fraction(216) - Fraction(12, 10) * 140) / (Fraction(18, 10) - Fraction(12, 10))
    assert min_o3 == 80
    assert Fraction(18, 10) * 80 + Fraction(12, 10) * 60 == 216
    assert Fraction(18, 10) * 79 + Fraction(12, 10) * 61 < 216

    # Q4: |3x - 7| + c = 12, diff of roots = 6 -> c
    c4 = 12 - Fraction(6 * 3, 2)
    assert c4 == 3
    r4_1 = Fraction(7 + (12 - c4), 3)
    r4_2 = Fraction(7 - (12 - c4), 3)
    assert r4_1 - r4_2 == 6

    # Q5: (3/4)x - (5/6)y = 5, ax + 10y = b infinite solutions -> a + b
    k5 = Fraction(10, 1) / Fraction(-5, 6)
    a5 = Fraction(3, 4) * k5
    b5 = 5 * k5
    assert k5 == -12 and a5 == -9 and b5 == -60 and a5 + b5 == -69

    # Q6: y <= 3x + 6, y <= -2x + 26, y >= 0 -> triangle area
    x6_left = Fraction(-6, 3)
    x6_right = Fraction(26, 2)
    x6_top = Fraction(26 - 6, 3 + 2)
    y6_top = 3 * x6_top + 6
    assert y6_top == -2 * x6_top + 26
    area6 = Fraction(1, 2) * (x6_right - x6_left) * y6_top
    assert area6 == 135

    # Q7: f(x) = ax + b (a > 0), f(f(x)) = 9x - 16 -> f(5)
    a7 = 3
    b7 = Fraction(-16, a7 + 1)
    assert a7**2 == 9 and b7 == -4
    for xv in (-2, 0, 5):
        assert a7 * (a7 * xv + b7) + b7 == 9 * xv - 16
    assert a7 * 5 + b7 == 11

    # Q8: 3x - 4y = 24 shifted right 4, up k passes through (0, 0) -> k
    # 3(0 - 4) - 4(0 - k) = 24 -> -12 + 4k = 24
    k8 = Fraction(24 + 12, 4)
    assert k8 == 9

    # Q9: 128 * (1/2)^(t/3) = 4 -> t = 15
    t9 = 15
    assert Fraction(128, 2 ** (t9 // 3)) == 4

    # Q10: P(x) = x^3 - 4x^2 + kx - 12, P(3) = 0 -> P(-1)
    k10 = Fraction(-(3**3 - 4 * 3**2 - 12), 3)
    assert k10 == 7
    p10 = lambda x: x**3 - 4 * x**2 + k10 * x - 12
    assert p10(3) == 0 and p10(-1) == -24

    # Q11: 2x^2 - 8x + 15 = 4x + c tangent -> 2x^2 - 12x + (15 - c) = 0, Delta = 0
    c11 = 15 - Fraction((-12)**2, 4 * 2)
    assert c11 == -3
    assert (-12)**2 - 4 * 2 * (15 - c11) == 0

    # Q12: 3x^2 - 18x + k = 0, r^2 + s^2 = 26 -> k
    sum12 = Fraction(18, 3)
    prod12 = Fraction(sum12**2 - 26, 2)
    k12 = 3 * prod12
    assert k12 == 15 and 1**2 + 5**2 == 26 and 3 * 1**2 - 18 * 1 + k12 == 0 and 3 * 5**2 - 18 * 5 + k12 == 0

    # Q13: (1.331)^(2/3) = 1.21 -> p = 21
    assert Fraction(11, 10)**3 == Fraction(1331, 1000)
    assert Fraction(11, 10)**2 == Fraction(121, 100)
    assert (Fraction(121, 100) - 1) * 100 == 21

    # Q14: g(x) = a(x - 4)^2 + k through (1, 20) and (9, 68) -> g(11) - g(4)
    a14 = Fraction(68 - 20, (9 - 4)**2 - (1 - 4)**2)
    k14 = 20 - a14 * (1 - 4)**2
    g14 = lambda x: a14 * (x - 4)**2 + k14
    assert a14 == 3 and k14 == -7
    assert g14(-3) == g14(11) == 140
    assert g14(-3) - g14(4) == 147

    # Q15: (2x + m)/(x - 3) + (x - 1)/(x + 2) = 3 -> (m + 3)x = -2m - 21
    m15_1 = Fraction(-3)  # degenerate linear
    assert -2 * m15_1 - 21 != 0
    m15_2 = Fraction(-21 - 9, 3 + 2)  # extraneous x = 3
    assert m15_2 == -6
    # Verify for m = -6, candidate x = 3
    assert Fraction(-2 * m15_2 - 21, m15_2 + 3) == 3
    assert m15_1 + m15_2 == -9

    # Q16: side 0.3 km = 300 m, 60% of 90000 m^2 at 750 m^2/min -> 72 min
    t16 = Fraction(60, 100) * (Fraction(3, 10) * 1000)**2 / 750
    assert t16 == 72

    # Q17: Cohort A vs Cohort B means & variances
    A17 = [4]*1 + [5]*3 + [6]*7 + [7]*3 + [8]*1
    B17 = [4]*5 + [5]*2 + [6]*1 + [7]*2 + [8]*5
    assert len(A17) == 15 and len(B17) == 15
    meanA = Fraction(sum(A17), len(A17))
    meanB = Fraction(sum(B17), len(B17))
    varA = sum((x - meanA)**2 for x in A17) / len(A17)
    varB = sum((x - meanB)**2 for x in B17) / len(B17)
    assert meanA == meanB == 6 and varA == Fraction(14, 15) and varB == Fraction(44, 15) and varB > varA

    # Q18: k/(180+k) = 2/5 -> k = 120 -> P(Oppose | Grad) = 40 / (120 + 40) = 1/4
    k18 = Fraction(2 * 180, 5 - 2)
    assert k18 == 120
    p18 = Fraction(40, k18 + 40)
    assert p18 == Fraction(1, 4)

    # Q19: (300*140 + 215S)/(300 + S) = 185 -> S = 450
    s19 = Fraction(300 * (185 - 140), 215 - 185)
    assert s19 == 450 and Fraction(300 * 140 + 215 * s19, 300 + s19) == 185

    # Q20: 2x^2 + 2y^2 - 16x + 24y + k = 0, r = 7 -> k = 6
    # x^2 - 8x + y^2 + 12y + k/2 = 0 -> (x-4)^2 + (y+6)^2 = 16 + 36 - k/2 = 49
    k20 = 2 * (16 + 36 - 7**2)
    assert k20 == 6

    # Q21: similar triangles AB=12, DE=20, Area(ABC)+Area(DEF)=272 -> Area(DEF) = 200
    ratio_sq = Fraction(12, 20)**2
    area_def = Fraction(272) / (1 + ratio_sq)
    assert ratio_sq == Fraction(9, 25) and area_def == 200 and 272 - area_def == 72

    # Q22: V = 180pi, LSA = 60pi -> r = 6, h = 5; similar R = 9 -> TSA_2 = 297pi
    r22 = Fraction(180, 30)
    h22 = Fraction(30, r22)
    tsa1 = 2 * r22**2 + 2 * r22 * h22
    scale22 = Fraction(9, r22)
    tsa2 = tsa1 * scale22**2
    assert r22 == 6 and h22 == 5 and tsa1 == 132 and tsa2 == 297
    # Direct verification on larger cylinder (R=9, H=7.5)
    R22, H22 = Fraction(9), h22 * scale22
    assert 2 * R22**2 + 2 * R22 * H22 == 297

    return True


if __name__ == '__main__':
    assert verify_math()
    qs = get_m2h_questions()
    print(f"M2H verified: {len(qs)} questions")
