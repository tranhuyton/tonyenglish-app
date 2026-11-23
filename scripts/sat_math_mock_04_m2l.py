# -*- coding: utf-8 -*-
"""
Digital SAT Math Adaptive Mock Test #4 — Module 2 Standard/Lower (22 Questions, 300–600 Band)
Difficulty progression: Easy -> Medium (Foundation & Core SAT Math skills).
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
    svg_parabola_vertex,
    svg_right_triangle,
    svg_cylinder,
    svg_similar_triangles,
)


def get_m2l_questions():
    qs = []

    # =========================================================================
    # Q1 — Algebra (Easy, MCQ -> A) | Two-Step Linear Equation & Target Expr
    # =========================================================================
    qs.append(math_mcq(
        'sat_mm4_m2l_q1', 1, 'Algebra', 'Linear equations in one variable', 'Easy',
        r'''<p>Consider the linear equation:</p><p style="text-align:center;">\[5x - 8 = 27\]</p>''',
        r'''<p>What is the value of \(2x + 1\)?</p>''',
        {
            'A': r'15',
            'B': r'7',
            'C': r'14',
            'D': r'19',
        },
        'A',
        r'''Bước 1: Cộng \(8\) vào cả hai vế: \(5x = 27 + 8 = 35\). Chia hai vế cho \(5\): \(x = 7\).<br>Bước 2: Thay \(x = 7\) vào biểu thức đề hỏi: \(2x + 1 = 2(7) + 1 = 15\).''',
        r'''Sau khi giải ra \(x\), luôn kiểm tra lại dòng câu hỏi cuối xem đề hỏi \(x\) hay hỏi một biểu thức như \(2x + 1\).''',
        {
            'A': ('Correct', r'Giải đúng \(x = 7\), thay vào \(2(7) + 1 = 15\).'),
            'B': ('Solved for x Only', r'7 là giá trị của \(x\), nhưng đề bài hỏi giá trị của \(2x + 1\).'),
            'C': ('Partial Evaluation', r'Tính \(2x = 14\) nhưng quên cộng thêm \(1\).'),
            'D': ('Arithmetic Slip', r'Trừ nhầm \(27 - 8 = 19\) thay vì cộng \(8\).'),
        },
        desmos_tip_vi=r'''Gõ <code>5x - 8 = 27</code> vào Desmos thấy đường thẳng đứng tại \(x = 7\), rồi gõ dòng dưới <code>2(7) + 1</code> ra ngay 15.''',
    ))

    # =========================================================================
    # Q2 — Algebra (Easy, MCQ -> C) | Theme: EV Charging Monthly Plan
    # =========================================================================
    qs.append(math_mcq(
        'sat_mm4_m2l_q2', 2, 'Algebra', 'Writing linear models from context', 'Easy',
        r'''<p>An electric vehicle charging network offers a monthly subscription plan that charges a flat fee of $15 per month plus $0.25 per kilowatt-hour (kWh) of electricity used.</p>''',
        r'''<p>Which equation represents the total monthly cost \(C\), in dollars, for using \(k\) kilowatt-hours of electricity?</p>''',
        {
            'A': r'\(C = 15k + 0.25\)',
            'B': r'\(C = 15.25k\)',
            'C': r'\(C = 0.25k + 15\)',
            'D': r'\(C = 0.25(k + 15)\)',
        },
        'C',
        r'''Phí cố định hàng tháng là $15 (hằng số tự do \(b = 15\)). Chi phí theo lượng điện tiêu thụ là $0.25 cho mỗi kWh nên với \(k\) kWh sẽ tốn \(0.25k\). Tổng chi phí hàng tháng là \(C = 0.25k + 15\).''',
        r'''Trong mô hình tuyến tính \(y = mx + b\), đơn giá đi kèm chữ "per" (mỗi) luôn nhân với biến \(x\), còn phí cố định ("flat fee") đứng độc lập.''',
        {
            'A': ('Swapped Slope and Intercept', r'Nhân nhầm phí cố định $15 với số kWh \(k\) và để $0.25 làm hằng số.'),
            'B': ('Combined Fixed and Variable Fees', r'Cộng gộp $15 và $0.25 thành $15.25/kWh — sai bản chất phí cố định.'),
            'C': ('Correct', r'Đúng cấu trúc tổng chi phí = đơn giá \(\times\) số lượng + phí cố định: \(C = 0.25k + 15\).'),
            'D': ('Distribution Error', r'Nhân hệ số $0.25 vào cả phí cố định $15, khiến phí cố định chỉ còn $3.75.'),
        },
        desmos_tip_vi=r'''Kiểm tra bằng giá trị thử \(k = 0\) kWh: tổng chi phí phải đúng bằng phí cố định $15. Thay \(k = 0\) vào 4 đáp án chỉ có C ra đúng 15.''',
    ))

    # =========================================================================
    # Q3 — Algebra (Easy, MCQ -> D) | Slope Between Two Points
    # =========================================================================
    qs.append(math_mcq(
        'sat_mm4_m2l_q3', 3, 'Algebra', 'Slope of a line from two points', 'Easy',
        r'''<p>A straight line in the \(xy\)-plane passes through the points \((2, 5)\) and \((6, 17)\).</p>''',
        r'''<p>What is the slope of this line?</p>''',
        {
            'A': r'\(\dfrac{1}{3}\)',
            'B': r'\(-3\)',
            'C': r'\(4\)',
            'D': r'\(3\)',
        },
        'D',
        r'''Áp dụng công thức hệ số góc đi qua hai điểm \((x_1, y_1)\) và \((x_2, y_2)\):<br>\(m = \dfrac{y_2 - y_1}{x_2 - x_1} = \dfrac{17 - 5}{6 - 2} = \dfrac{12}{4} = 3\).''',
        r'''Hệ số góc là "Rise over Run" = \(\dfrac{\Delta y}{\Delta x}\) — luôn đặt hiệu tung độ \(y\) ở tử số và hiệu hoành độ \(x\) theo CÙNG thứ tự ở mẫu số.''',
        {
            'A': ('Inverted Rise and Run', r'Đặt nhầm \(\Delta x / \Delta y = (6 - 2)/(17 - 5) = 4/12 = 1/3\).'),
            'B': ('Sign Order Error', r'Lấy \(y_2 - y_1\) ở tử nhưng đảo ngược thành \(x_1 - x_2\) ở mẫu, sinh ra dấu âm \(-3\).'),
            'C': ('Run Only', r'4 chỉ là độ biến thiên hoành độ \(\Delta x = 6 - 2\), chưa chia \(\Delta y / \Delta x\).'),
            'D': ('Correct', r'Tính chuẩn \(m = (17 - 5)/(6 - 2) = 12/4 = 3\).'),
        },
        desmos_tip_vi=r'''Gõ trực tiếp <code>(17 - 5) / (6 - 2)</code> vào Desmos (hoặc nhập bảng 2 điểm và gõ <code>y_1 ~ m x_1 + b</code>) để đọc ngay \(m = 3\).''',
    ))

    # =========================================================================
    # Q4 — Algebra (Easy, MCQ -> B) | Theme: Sustainable Forestry Sapling Height
    # =========================================================================
    qs.append(math_mcq(
        'sat_mm4_m2l_q4', 4, 'Algebra', 'Evaluating linear functions', 'Easy',
        r'''<p>A sustainable forestry nursery models the height \(h(w)\), in centimeters, of a spruce sapling \(w\) weeks after sprouting using the function:</p><p style="text-align:center;">\[h(w) = 2.5w + 14\]</p>''',
        r'''<p>What is the predicted height, in centimeters, of the sapling \(8\) weeks after sprouting?</p>''',
        {
            'A': r'20',
            'B': r'34',
            'C': r'24.5',
            'D': r'132',
        },
        'B',
        r'''Thay \(w = 8\) vào công thức hàm số:<br>\(h(8) = 2.5(8) + 14 = 20 + 14 = 34\text{ cm}\).''',
        r'''Khi tính giá trị hàm \(h(8)\), thực hiện phép nhân trước rồi mới cộng hằng số tự do theo đúng thứ tự phép tính.''',
        {
            'A': ('Omitted Intercept', r'Tính \(2.5 \times 8 = 20\) nhưng quên cộng chiều cao ban đầu \(14\).'),
            'B': ('Correct', r'Thay chuẩn xác \(h(8) = 2.5(8) + 14 = 20 + 14 = 34\).'),
            'C': ('Added Instead of Multiplied', r'Cộng nhầm \(2.5 + 8 + 14 = 24.5\) thay vì nhân \(2.5 \times 8\).'),
            'D': ('Order of Operations Error', r'Cộng \(2.5 + 14 = 16.5\) trước rồi mới nhân \(8\), ra \(132\).'),
        },
        desmos_tip_vi=r'''Nhập <code>h(x) = 2.5x + 14</code> rồi gõ dòng dưới <code>h(8)</code> để Desmos trả ngay kết quả 34.''',
    ))

    # =========================================================================
    # Q5 — Algebra (Easy, SPR -> 21) | Simple Substitution System
    # =========================================================================
    qs.append(math_spr(
        'sat_mm4_m2l_q5', 5, 'Algebra', 'Systems of linear equations — substitution', 'Easy',
        r'''<p>Consider the system of linear equations:</p><p style="text-align:center;">\[\begin{aligned} y &= 3x \\ x + y &= 28 \end{aligned}\]</p>''',
        r'''<p>What is the value of \(y\)?</p>''',
        ['21'],
        '21',
        r'''Thay \(y = 3x\) từ phương trình đầu vào phương trình thứ hai:<br>\(x + 3x = 28 \Rightarrow 4x = 28 \Rightarrow x = 7\).<br>Đề bài hỏi giá trị của \(y\), nên thay ngược lại: \(y = 3(7) = 21\).''',
        r'''Đừng dừng vội sau khi tìm ra \(x = 7\)! Đọc kỹ xem đề hỏi \(x\) hay \(y\) trước khi điền vào ô SPR.''',
        desmos_tip_vi=r'''Vẽ hai đường thẳng <code>y = 3x</code> và <code>x + y = 28</code> trong Desmos, bấm vào giao điểm \((7, 21)\) và đọc tung độ \(y = 21\).''',
    ))

    # =========================================================================
    # Q6 — Algebra (Easy, MCQ -> D) | Theme: Archaeological Supply Budget
    # =========================================================================
    qs.append(math_mcq(
        'sat_mm4_m2l_q6', 6, 'Algebra', 'Linear inequalities in one variable', 'Easy',
        r'''<p>An archaeological field station has a weekly supply budget of $500. After spending $140 on wooden survey stakes, the team plans to purchase boxes of archival specimen bags at $18 per box.</p>''',
        r'''<p>What is the maximum number of boxes of specimen bags the team can purchase without exceeding its weekly budget?</p>''',
        {
            'A': r'18',
            'B': r'27',
            'C': r'35',
            'D': r'20',
        },
        'D',
        r'''Gọi \(b\) là số hộp túi mẫu vật. Thiết lập bất phương trình ngân sách:<br>\(140 + 18b \le 500 \Rightarrow 18b \le 360 \Rightarrow b \le \dfrac{360}{18} = 20\).<br>Vậy đội có thể mua tối đa \(20\) hộp.''',
        r'''Trừ các khoản đã chi tiêu cố định khỏi tổng ngân sách trước, sau đó mới chia cho đơn giá mỗi sản phẩm.''',
        {
            'A': ('Unit Price Confusion', r'Nhầm đơn giá $18 mỗi hộp thành số lượng 18 hộp.'),
            'B': ('Ignored Initial Spending', r'Quên trừ $140 đã chi, lấy \(500 / 18 \approx 27.7 \to 27\).'),
            'C': ('Added Instead of Subtracted', r'Cộng nhầm $140 vào $500: \((500 + 140) / 18 \approx 35.5 \to 35\).'),
            'D': ('Correct', r'Ngân sách còn lại là $360; chia cho $18/hộp ra đúng tối đa 20 hộp.'),
        },
        desmos_tip_vi=r'''Tính thẳng <code>(500 - 140) / 18</code> trong Desmos để nhận ngay số nguyên chính xác 20.''',
    ))

    # =========================================================================
    # Q7 — Algebra (Medium, MCQ -> B) | Finding the x-Intercept
    # =========================================================================
    qs.append(math_mcq(
        'sat_mm4_m2l_q7', 7, 'Algebra', 'Graphing linear equations & intercepts', 'Medium',
        r'''<p>Consider the linear equation in the \(xy\)-plane:</p><p style="text-align:center;">\[4x - 3y = 36\]</p>''',
        r'''<p>What is the \(x\)-intercept of the graph of the equation?</p>''',
        {
            'A': r'\((0, -12)\)',
            'B': r'\((9, 0)\)',
            'C': r'\((0, 9)\)',
            'D': r'\((-12, 0)\)',
        },
        'B',
        r'''Giao điểm với trục hoành (\(x\)-intercept) luôn có tung độ \(y = 0\). Thay \(y = 0\) vào phương trình:<br>\(4x - 3(0) = 36 \Rightarrow 4x = 36 \Rightarrow x = 9\).<br>Do đó tọa độ \(x\)-intercept là \((9, 0)\).''',
        r'''Nhớ nhanh: tìm \(x\)-intercept thì đặt \(y = 0\) (dạng \((x, 0)\)); tìm \(y\)-intercept thì đặt \(x = 0\) (dạng \((0, y)\)).''',
        {
            'A': ('Found y-Intercept Instead', r'\((0, -12)\) là giao điểm với trục tung (\(y\)-intercept), không phải trục hoành.'),
            'B': ('Correct', r'Đặt \(y = 0\) giải ra \(x = 9\), tọa độ giao điểm trục hoành là \((9, 0)\).'),
            'C': ('Swapped Coordinates', r'Tìm đúng \(x = 9\) nhưng viết ngược thứ tự tọa độ thành \((0, 9)\).'),
            'D': ('Intercept Value Mix-up', r'Đặt giá trị \(y\)-intercept (\(-12\)) vào vị trí hoành độ \(x\).'),
        },
        desmos_tip_vi=r'''Gõ thẳng <code>4x - 3y = 36</code> vào Desmos rồi bấm chấm xám nơi đường thẳng cắt trục ngang \(Ox\): hiện ngay \((9, 0)\).''',
    ))

    # =========================================================================
    # Q8 — Algebra (Medium, MCQ -> A) | Theme: Geodesic Dome Conservatory Tickets
    # =========================================================================
    qs.append(math_mcq(
        'sat_mm4_m2l_q8', 8, 'Algebra', 'Systems of linear equations in context', 'Medium',
        r'''<p>A geodesic dome botanical conservatory sells adult tickets for $12 each and student tickets for $8 each. On Saturday, the conservatory sold \(50\) tickets in total and collected $520 in ticket revenue.</p>''',
        r'''<p>How many adult tickets were sold on Saturday?</p>''',
        {
            'A': r'30',
            'B': r'20',
            'C': r'26',
            'D': r'40',
        },
        'A',
        r'''Gọi \(a\) là số vé người lớn và \(s\) là số vé học sinh. Ta có hệ phương trình:<br>• \(a + s = 50 \Rightarrow 8a + 8s = 400\)<br>• \(12a + 8s = 520\)<br>Trừ phương trình trên từ phương trình dưới: \(4a = 120 \Rightarrow a = 30\) vé người lớn (và \(s = 20\) vé học sinh).<br>Kiểm tra: \(12(30) + 8(20) = 360 + 160 = 520\).''',
        r'''Để khử nhanh biến không cần tìm (\(s\)), nhân phương trình tổng số lượng với giá của \(s\) (là 8) rồi trừ vế theo vế.''',
        {
            'A': ('Correct', r'Giải hệ ra chính xác \(a = 30\) vé người lớn (và \(s = 20\) vé học sinh).'),
            'B': ('Solved for Other Variable', r'20 là số vé học sinh \(s\), trong khi đề bài hỏi số vé người lớn \(a\).'),
            'C': ('Summed Ticket Prices', r'Chia nhầm tổng doanh thu cho tổng giá 2 loại vé: \(520 / (12 + 8) = 26\).'),
            'D': ('Arithmetic Slip', r'Sai phép trừ doanh thu hoặc chia nhầm cho 3 thay vì 4.'),
        },
        desmos_tip_vi=r'''Nhập <code>x + y = 50</code> và <code>12x + 8y = 520</code> vào Desmos, bấm giao điểm \((30, 20)\) để đọc ngay số vé người lớn \(x = 30\).''',
    ))

    # =========================================================================
    # Q9 — Advanced Math (Easy, SPR -> 12) | Evaluating a Quadratic Function
    # =========================================================================
    qs.append(math_spr(
        'sat_mm4_m2l_q9', 9, 'Advanced Math', 'Evaluating quadratic functions', 'Easy',
        r'''<p>The quadratic function \(f\) is defined by:</p><p style="text-align:center;">\[f(x) = x^2 - 4x + 7\]</p>''',
        r'''<p>What is the value of \(f(5)\)?</p>''',
        ['12'],
        '12',
        r'''Thay \(x = 5\) vào từng hạng tử của hàm số:<br>\(f(5) = 5^2 - 4(5) + 7 = 25 - 20 + 7 = 12\).''',
        r'''Khi thay số vào hàm bậc hai, tính lũy thừa trước rồi thực hiện nhân và cộng trừ từ trái sang phải.''',
        desmos_tip_vi=r'''Nhập <code>f(x) = x^2 - 4x + 7</code> vào Desmos rồi gõ dòng dưới <code>f(5)</code> để nhận ngay kết quả 12.''',
    ))

    # =========================================================================
    # Q10 — Advanced Math (Easy, MCQ -> C) | Laws of Exponents
    # =========================================================================
    qs.append(math_mcq(
        'sat_mm4_m2l_q10', 10, 'Advanced Math', 'Properties of exponents', 'Easy',
        r'''<p>For all \(x > 0\), consider the expression:</p><p style="text-align:center;">\[\dfrac{(x^4)^3}{x^5}\]</p>''',
        r'''<p>Which of the following is equivalent to the given expression?</p>''',
        {
            'A': r'\(x^2\)',
            'B': r'\(x^{17}\)',
            'C': r'\(x^7\)',
            'D': r'\(x^{60}\)',
        },
        'C',
        r'''Bước 1 (Lũy thừa của lũy thừa — NHÂN số mũ): \((x^4)^3 = x^{4 \times 3} = x^{12}\).<br>Bước 2 (Chia hai lũy thừa cùng cơ số — TRỪ số mũ): \(\dfrac{x^{12}}{x^5} = x^{12 - 5} = x^7\).''',
        r'''Quy tắc số mũ nền tảng: \((x^a)^b = x^{ab}\) (nhân mũ) và \(\dfrac{x^m}{x^n} = x^{m - n}\) (trừ mũ).''',
        {
            'A': ('Added Exponents in Power Rule', r'Cộng nhầm \(4 + 3 = 7\) thay vì nhân \(4 \times 3 = 12\), rồi trừ \(5\) ra \(x^2\).'),
            'B': ('Added Instead of Subtracted', r'Tính đúng \(x^{12}\) nhưng cộng thêm \(5\) thay vì trừ \(5\), ra \(x^{17}\).'),
            'C': ('Correct', r'Áp dụng chuẩn \((x^4)^3 = x^{12}\) và \(x^{12} / x^5 = x^7\).'),
            'D': ('Multiplied All Exponents', r'Nhân gộp cả ba số mũ \(4 \times 3 \times 5 = 60\).'),
        },
        desmos_tip_vi=r'''Thử giá trị \(x = 2\): gõ <code>(2^4)^3 / 2^5</code> ra \(128\), kiểm tra <code>2^7 = 128</code> khớp chính xác đáp án C!''',
    ))

    # =========================================================================
    # Q11 — Advanced Math (Easy, MCQ -> B) | Solving Factorable Quadratic
    # =========================================================================
    qs.append(math_mcq(
        'sat_mm4_m2l_q11', 11, 'Advanced Math', 'Solving quadratic equations by factoring', 'Easy',
        r'''<p>Consider the quadratic equation:</p><p style="text-align:center;">\[x^2 - 7x + 10 = 0\]</p>''',
        r'''<p>What are the solutions to the given equation?</p>''',
        {
            'A': r'\(x = -2\) and \(x = -5\)',
            'B': r'\(x = 2\) and \(x = 5\)',
            'C': r'\(x = -2\) and \(x = 5\)',
            'D': r'\(x = 1\) and \(x = 10\)',
        },
        'B',
        r'''Tìm hai số có tích bằng \(+10\) và tổng bằng \(-7\): đó là \(-2\) và \(-5\). Phân tích thành nhân tử:<br>\((x - 2)(x - 5) = 0\).<br>Đặt từng nhân tử bằng \(0\): \(x - 2 = 0 \Rightarrow x = 2\) hoặc \(x - 5 = 0 \Rightarrow x = 5\).''',
        r'''Luôn đổi dấu khi chuyển từ dạng nhân tử \((x - r) = 0\) sang nghiệm \(x = r\).''',
        {
            'A': ('Forgot to Flip Factor Signs', r'Lấy thẳng hằng số \(-2\) và \(-5\) trong ngoặc \((x - 2)(x - 5)\) làm nghiệm mà quên đổi dấu.'),
            'B': ('Correct', r'Thay \(x = 2\) (\(4 - 14 + 10 = 0\)) và \(x = 5\) (\(25 - 35 + 10 = 0\)) đều thỏa mãn.'),
            'C': ('Mixed Signs', r'Tích \((-2)(5) = -10 \ne +10\), sai dấu hằng số tự do.'),
            'D': ('Wrong Factor Pair', r'Chọn cặp \(1 \times 10 = 10\) nhưng tổng là \(11 \ne 7\).'),
        },
        desmos_tip_vi=r'''Vẽ <code>y = x^2 - 7x + 10</code> trong Desmos rồi bấm vào 2 chấm xám cắt trục hoành: hiện ngay \((2, 0)\) và \((5, 0)\).''',
    ))

    # =========================================================================
    # Q12 — Advanced Math (Medium, MCQ -> D) | Theme: EV Van Exponential Decay
    # =========================================================================
    qs.append(math_mcq(
        'sat_mm4_m2l_q12', 12, 'Advanced Math', 'Interpreting exponential decay models', 'Medium',
        r'''<p>The maximum driving range \(D(t)\), in miles, of an electric delivery van \(t\) years after purchase is modeled by the function:</p><p style="text-align:center;">\[D(t) = 280(0.96)^t\]</p>''',
        r'''<p>According to this model, by what percent does the van's maximum driving range decrease each year?</p>''',
        {
            'A': r'\(96\%\)',
            'B': r'\(0.96\%\)',
            'C': r'\(28\%\)',
            'D': r'\(4\%\)',
        },
        'D',
        r'''Trong mô hình suy giảm hàm mũ \(D(t) = D_0(1 - r)^t\), cơ số \(0.96 = 1 - r\) biểu thị lượng còn giữ lại (\(96\%\)) sau mỗi năm. Do đó, tỉ lệ suy giảm mỗi năm là \(r = 1 - 0.96 = 0.04 = 4\%\).''',
        r'''Với cơ số \(b < 1\), phần trăm GIẢM mỗi chu kỳ luôn là \((1 - b) \times 100\%\) — đừng chọn nhầm bản thân cơ số \(b\) (đó là phần trăm CÒN LẠI).''',
        {
            'A': ('Retention vs Decay Confusion', r'96% là tỷ lệ quãng đường CÒN GIỮ LẠI sau mỗi năm, không phải tỷ lệ giảm đi.'),
            'B': ('Decimal Percent Error', r'Đọc nhầm số thập phân 0.96 trực tiếp thành 0.96%.'),
            'C': ('Initial Value Confusion', r'Nhầm lẫn giá trị ban đầu 280 dặm với tỷ lệ phần trăm 28%.'),
            'D': ('Correct', r'Đúng tỷ lệ giảm \(1 - 0.96 = 0.04 = 4\%\) mỗi năm.'),
        },
        desmos_tip_vi=r'''Tính trong Desmos: sau 1 năm giảm từ \(280\) xuống \(280(0.96) = 268.8\); tính <code>(280 - 268.8)/280 * 100</code> ra đúng 4%.''',
    ))

    # =========================================================================
    # Q13 — Advanced Math (Medium, SPR -> 20) | Radical Equation
    # =========================================================================
    qs.append(math_spr(
        'sat_mm4_m2l_q13', 13, 'Advanced Math', 'Solving radical equations', 'Medium',
        r'''<p>Consider the equation:</p><p style="text-align:center;">\[\sqrt{2x + 9} = 7\]</p>''',
        r'''<p>What is the solution to the given equation?</p>''',
        ['20'],
        '20',
        r'''Bình phương cả hai vế để khử dấu căn:<br>\(2x + 9 = 7^2 = 49 \Rightarrow 2x = 40 \Rightarrow x = 20\).<br>Thử lại: \(\sqrt{2(20) + 9} = \sqrt{49} = 7\) (đúng!).''',
        r'''Khi bình phương hai vế để phá căn \(\sqrt{A} = c\), nhớ bình phương luôn hằng số \(c\) ở vế phải (\(7^2 = 49\), không phải \(7\) hay \(14\)).''',
        desmos_tip_vi=r'''Vẽ <code>y = sqrt(2x + 9)</code> và <code>y = 7</code> trên Desmos (kéo sang phải tới \(x = 20\)) sẽ thấy ngay giao điểm \((20, 7)\).''',
    ))

    # =========================================================================
    # Q14 — Advanced Math (Medium, MCQ -> A) | Expanding Binomial Product
    # =========================================================================
    qs.append(math_mcq(
        'sat_mm4_m2l_q14', 14, 'Advanced Math', 'Multiplying binomials & equivalent quadratics', 'Medium',
        r'''<p>Consider the algebraic product:</p><p style="text-align:center;">\[(2x - 3)(x + 5)\]</p>''',
        r'''<p>Which of the following is equivalent to the given expression?</p>''',
        {
            'A': r'\(2x^2 + 7x - 15\)',
            'B': r'\(2x^2 - 7x - 15\)',
            'C': r'\(2x^2 + 13x - 15\)',
            'D': r'\(2x^2 - 15\)',
        },
        'A',
        r'''Áp dụng quy tắc nhân phân phối FOIL (First – Outer – Inner – Last):<br>• First: \(2x \cdot x = 2x^2\)<br>• Outer: \(2x \cdot 5 = +10x\)<br>• Inner: \((-3) \cdot x = -3x\)<br>• Last: \((-3) \cdot 5 = -15\)<br>Gom hai hạng tử giữa: \(2x^2 + (10x - 3x) - 15 = 2x^2 + 7x - 15\).''',
        r'''Khi nhân hai nhị thức \((ax + b)(cx + d)\), đừng bỏ quên hai tích chéo Outer và Inner tạo thành hạng tử bậc nhất.''',
        {
            'A': ('Correct', r'Khai triển đủ 4 tích và cộng gọn \(10x - 3x = +7x\) cho \(2x^2 + 7x - 15\).'),
            'B': ('Middle Term Sign Flip', r'Tính ngược dấu hệ số bậc nhất thành \(-7x\) thay vì \(+7x\).'),
            'C': ('Added Cross Terms', r'Cộng nhầm \(10x + 3x = 13x\) mà quên dấu trừ của \(-3\).'),
            'D': ('Missing Cross Terms', r'Chỉ nhân hạng tử đầu với đầu và cuối với cuối, bỏ sót hoàn toàn \(+10x - 3x\).'),
        },
        desmos_tip_vi=r'''Đặt <code>f(x) = (2x - 3)(x + 5)</code> trong Desmos rồi thử vẽ các đáp án; chỉ đồ thị A trùng khít 100% lên \(f(x)\).''',
    ))

    # =========================================================================
    # Q15 — Advanced Math (Medium, MCQ -> C) | Parabola Vertex Form (SVG)
    # =========================================================================
    svg_q15 = svg_parabola_vertex(
        h_lbl='3', k_lbl='-4', opens_up=True, pt_lbl='(5, 4)',
        note='Note: Figure not drawn to scale.'
    )
    qs.append(math_mcq(
        'sat_mm4_m2l_q15', 15, 'Advanced Math', 'Quadratic functions — vertex form from graph', 'Medium',
        rf'''<div style="text-align:center;margin-bottom:10px;">{svg_q15}</div><p>The graph of the quadratic function \(y = f(x)\) in the \(xy\)-plane above has its vertex at \((3, -4)\) and passes through the point \((5, 4)\).</p>''',
        r'''<p>Which of the following equations defines \(f(x)\)?</p>''',
        {
            'A': r'\(f(x) = 2(x + 3)^2 - 4\)',
            'B': r'\(f(x) = (x - 3)^2 - 4\)',
            'C': r'\(f(x) = 2(x - 3)^2 - 4\)',
            'D': r'\(f(x) = 2(x - 3)^2 + 4\)',
        },
        'C',
        r'''Bước 1: Viết dạng đỉnh với đỉnh \((h, k) = (3, -4)\):<br>\(f(x) = a(x - 3)^2 - 4\).<br>Bước 2: Thay tọa độ điểm \((5, 4)\) đi qua parabol để tìm hệ số \(a\):<br>\(4 = a(5 - 3)^2 - 4 \Rightarrow 8 = 4a \Rightarrow a = 2\).<br>Vậy \(f(x) = 2(x - 3)^2 - 4\).''',
        r'''Với đỉnh \((h, k)\), luôn dùng \((x - h)^2 + k\) (đổi dấu \(h\), giữ nguyên dấu \(k\)) và thay thêm 1 điểm trên đồ thị để xác định chính xác hệ số \(a\) — đừng mặc định \(a = 1\)!''',
        {
            'A': ('Horizontal Shift Sign Error', r'Dùng \((x + 3)^2\) ứng với đỉnh ở \(x = -3\) thay vì \(x = +3\).'),
            'B': ('Assumed a = 1', r'Bỏ qua bước thay điểm \((5, 4)\) nên giữ mặc định \(a = 1\) (khi đó \(f(5) = 0 \ne 4\)).'),
            'C': ('Correct', r'Đúng cả đỉnh \((3, -4)\) lẫn hệ số \(a = 2\) thỏa \(f(5) = 2(2)^2 - 4 = 4\).'),
            'D': ('Vertical Shift Sign Error', r'Dùng \(+4\) ứng với tung độ đỉnh \(+4\) thay vì \(-4\).'),
        },
        desmos_tip_vi=r'''Gõ đáp án <code>y = 2(x - 3)^2 - 4</code> vào Desmos để kiểm tra tức thì: đỉnh hiện đúng \((3, -4)\) và đi qua \((5, 4)\).''',
    ))

    # =========================================================================
    # Q16 — Data Analysis (Easy, SPR -> 405) | Theme: Timber Sawmill Rate
    # =========================================================================
    qs.append(math_spr(
        'sat_mm4_m2l_q16', 16, 'Problem-Solving and Data Analysis', 'Ratios, rates, and proportional relationships', 'Easy',
        r'''<p>A sustainable timber sawmill cuts \(180\) pine boards every \(4\) hours at a constant rate.</p>''',
        r'''<p>At this same rate, how many pine boards will the sawmill cut in \(9\) hours?</p>''',
        ['405'],
        '405',
        r'''Bước 1: Tìm năng suất trong \(1\) giờ: \(\dfrac{180\text{ tấm}}{4\text{ giờ}} = 45\text{ tấm/giờ}\).<br>Bước 2: Nhân với \(9\) giờ: \(45 \times 9 = 405\) tấm ván thông.''',
        r'''Luôn quy về đơn vị chuẩn (sản lượng trong 1 giờ) trước khi nhân với thời gian mới để tránh lập nhầm tỉ lệ thức.''',
        desmos_tip_vi=r'''Tính thẳng <code>(180 / 4) * 9</code> trong Desmos để nhận ngay 405.''',
    ))

    # =========================================================================
    # Q17 — Data Analysis (Easy, MCQ -> B) | Theme: University Polling Table
    # =========================================================================
    tbl_q17 = build_math_table(
        ['Class Standing', 'Main Library', 'Science Commons', 'Total'],
        [
            ['First-Year', '62', '38', '100'],
            ['Upperclass', '46', '54', '100'],
            ['Total', '108', '92', '200'],
        ],
        caption='Preferred Campus Study Space Survey (n = 200)'
    )
    qs.append(math_mcq(
        'sat_mm4_m2l_q17', 17, 'Problem-Solving and Data Analysis', 'Percentages from two-way tables', 'Easy',
        rf'''<p>A university polling club surveyed \(200\) students about which campus study space they prefer, as shown in the table below.</p>{tbl_q17}''',
        r'''<p>What percent of all \(200\) surveyed students prefer the Main Library?</p>''',
        {
            'A': r'\(46\%\)',
            'B': r'\(54\%\)',
            'C': r'\(62\%\)',
            'D': r'\(108\%\)',
        },
        'B',
        r'''Từ dòng Total của cột Main Library, có tổng cộng \(108\) sinh viên chọn Main Library trên tổng số \(200\) sinh viên tham gia khảo sát. Tỉ lệ phần trăm là:<br>\(\dfrac{108}{200} \times 100\% = 0.54 \times 100\% = 54\%\).''',
        r'''Đọc kỹ mẫu số trong câu hỏi bảng hai chiều: "percent of all 200 surveyed students" nghĩa là chia cho tổng toàn bảng \(200\), không phải \(100\).''',
        {
            'A': ('Wrong Column Percentage', r'46% là tỷ lệ sinh viên chọn Science Commons (\(92/200 = 46\%\)).'),
            'B': ('Correct', r'\(108 / 200 = 0.54 = 54\%\) tổng số sinh viên chọn Main Library.'),
            'C': ('Single-Row Trap', r'62% chỉ là tỷ lệ của riêng sinh viên năm nhất (\(62/100\)), chưa gộp sinh viên năm trên.'),
            'D': ('Forgot to Divide by Total', r'Lấy thẳng số đếm 108 người thành 108% mà quên chia cho 200.'),
        },
        desmos_tip_vi=r'''Tính nhanh <code>(108 / 200) * 100</code> trong Desmos ra ngay 54.''',
    ))

    # =========================================================================
    # Q18 — Data Analysis (Medium, MCQ -> D) | Theme: EV Charger Rebate Price
    # =========================================================================
    qs.append(math_mcq(
        'sat_mm4_m2l_q18', 18, 'Problem-Solving and Data Analysis', 'Percent decrease & finding original value', 'Medium',
        r'''<p>During a municipal clean-energy rebate week, a home electric vehicle wall charger is sold at a \(20\%\) discount off its regular price. The discounted sale price of the charger (before tax) is $520.</p>''',
        r'''<p>What is the regular price of the wall charger?</p>''',
        {
            'A': r'$416',
            'B': r'$540',
            'C': r'$624',
            'D': r'$650',
        },
        'D',
        r'''Gọi \(P\) là giá gốc của bộ sạc. Sau khi giảm \(20\%\), giá bán còn lại bằng \(100\% - 20\% = 80\%\) giá gốc:<br>\(0.80P = 520 \Rightarrow P = \dfrac{520}{0.80} = 650\) đô la.<br>Kiểm tra ngược: \(20\%\) của $650 là $130; \(\$650 - \$130 = \$520\) (khớp hoàn toàn!).''',
        r'''Bẫy phần trăm kinh điển: để tìm giá gốc trước khi giảm \(20\%\), PHẢI CHIA giá sau giảm cho \(0.80\), tuyệt đối KHÔNG nhân với \(1.20\)!''',
        {
            'A': ('Applied Discount Twice', r'Lấy \(520 \times 0.80 = 416\) — giảm thêm 20% lên giá đã giảm.'),
            'B': ('Treated Percent as Flat Dollars', r'Cộng nhầm $20 thay vì khôi phục 20%: \(520 + 20 = 540\).'),
            'C': ('Forward Percent Trap', r'Nhân nhầm \(520 \times 1.20 = 624\) — nhưng 20% của $624 là $124.80, trừ đi chỉ còn $499.20 \(\ne \$520\).'),
            'D': ('Correct', r'Giải chuẩn \(0.80P = 520 \Rightarrow P = \$650\).'),
        },
        desmos_tip_vi=r'''Gõ <code>0.80x = 520</code> (hoặc <code>520 / 0.80</code>) trong Desmos để nhận ngay giá gốc $650.''',
    ))

    # =========================================================================
    # Q19 — Data Analysis (Medium, SPR -> 7) | Theme: Clinical Trial Median Table
    # =========================================================================
    tbl_q19 = build_math_table(
        ['Resting Heart-Rate Reduction (bpm)', 'Number of Patients'],
        [
            ['3', '2'],
            ['5', '3'],
            ['7', '4'],
            ['9', '2'],
        ],
        caption='Clinical Trial Heart-Rate Reductions After 8 Weeks (n = 11)'
    )
    qs.append(math_spr(
        'sat_mm4_m2l_q19', 19, 'Problem-Solving and Data Analysis', 'Median from a frequency table', 'Medium',
        rf'''<p>In a university clinical study, \(11\) patients completed an 8-week walking program. The table below shows each patient's reduction in resting heart rate, in beats per minute (bpm).</p>{tbl_q19}''',
        r'''<p>What is the median resting heart-rate reduction, in bpm, for these \(11\) patients?</p>''',
        ['7'],
        '7',
        r'''Tổng số bệnh nhân là \(n = 2 + 3 + 4 + 2 = 11\). Với \(11\) số liệu sắp xếp tăng dần, trung vị (median) nằm đúng tại vị trí thứ \(\dfrac{11 + 1}{2} = 6\).<br>Đếm cộng dồn tần số từ trên xuống:<br>• Mức \(3\) bpm: vị trí 1–2 (\(2\) người)<br>• Mức \(5\) bpm: vị trí 3–5 (\(2 + 3 = 5\) người)<br>• Mức \(7\) bpm: vị trí 6–9 (\(5 + 4 = 9\) người)<br>Vì vị trí thứ 6 rơi vào mức \(7\), nên trung vị là \(7\).''',
        r'''Để tìm trung vị trên bảng tần số gồm \(n\) số liệu lẻ, luôn tính vị trí giữa \(\dfrac{n+1}{2}\) rồi cộng dồn cột tần số thay vì lấy trung bình hai số giữa của cột giá trị.''',
        desmos_tip_vi=r'''Nhập danh sách đầy đủ <code>L = [3,3,5,5,5,7,7,7,7,9,9]</code> rồi gõ <code>median(L)</code> trong Desmos để nhận ngay <code>7</code>.''',
    ))

    # =========================================================================
    # Q20 — Geometry (Easy, MCQ -> A) | Theme: Stone Monument Right Triangle (SVG)
    # =========================================================================
    svg_q20 = svg_right_triangle(
        a_lbl='9', b_lbl='12', c_lbl='x',
        v_top='A', v_right_angle='B', v_right='C',
        note='Note: Figure not drawn to scale.'
    )
    qs.append(math_mcq(
        'sat_mm4_m2l_q20', 20, 'Geometry and Trigonometry', 'Pythagorean theorem', 'Easy',
        rf'''<div style="text-align:center;margin-bottom:10px;">{svg_q20}</div><p>Right triangle \(ABC\) represents the cross-section of a stone stairway along a pyramid monument, where \(\angle B = 90^\circ\), \(AB = 9\) meters, and \(BC = 12\) meters.</p>''',
        r'''<p>What is the length \(x\), in meters, of hypotenuse \(AC\)?</p>''',
        {
            'A': r'15',
            'B': r'21',
            'C': r'10.5',
            'D': r'225',
        },
        'A',
        r'''Áp dụng định lý Pythagore cho tam giác vuông \(ABC\):<br>\(x^2 = 9^2 + 12^2 = 81 + 144 = 225 \Rightarrow x = \sqrt{225} = 15\text{ m}\).<br>(Mẹo nhanh: nhận ra bộ ba Pythagore \(3\text{-}4\text{-}5\) nhân với \(3\) cho ngay \(9\text{-}12\text{-}15\).)''',
        r'''Bộ ba \(3\text{-}4\text{-}5\) và các bội của nó (\(6\text{-}8\text{-}10\), \(9\text{-}12\text{-}15\), \(12\text{-}16\text{-}20\)) xuất hiện cực kỳ dày đặc trên Digital SAT!''',
        {
            'A': ('Correct', r'\(\sqrt{9^2 + 12^2} = \sqrt{225} = 15\) mét.'),
            'B': ('Added Legs Directly', r'Cộng thẳng hai cạnh góc vuông \(9 + 12 = 21\) thay vì dùng Pythagore.'),
            'C': ('Averaged Legs', r'Lấy trung bình cộng \((9 + 12)/2 = 10.5\) — cạnh huyền phải lớn hơn cả hai cạnh góc vuông.'),
            'D': ('Forgot Square Root', r'Tính \(9^2 + 12^2 = 225\) nhưng quên lấy căn bậc hai để tìm \(x\).'),
        },
        desmos_tip_vi=r'''Gõ trực tiếp <code>sqrt(9^2 + 12^2)</code> vào Desmos để đọc ngay kết quả 15.''',
    ))

    # =========================================================================
    # Q21 — Geometry (Medium, MCQ -> C) | Theme: Forestry Cylinder Tank (SVG)
    # =========================================================================
    svg_q21 = svg_cylinder(
        r_lbl='5 m', h_lbl='8 m',
        note='Note: Figure not drawn to scale.'
    )
    qs.append(math_mcq(
        'sat_mm4_m2l_q21', 21, 'Geometry and Trigonometry', 'Volume of a right circular cylinder', 'Medium',
        rf'''<div style="text-align:center;margin-bottom:10px;">{svg_q21}</div><p>A cylindrical rainwater storage tank at a sustainable forestry nursery has a base radius of \(5\) meters and a height of \(8\) meters.</p>''',
        r'''<p>What is the volume of the tank, in cubic meters?</p>''',
        {
            'A': r'\(40\pi\)',
            'B': r'\(80\pi\)',
            'C': r'\(200\pi\)',
            'D': r'\(320\pi\)',
        },
        'C',
        r'''Áp dụng công thức thể tích hình trụ tròn xoay (có sẵn trong Reference Sheet của Bluebook):<br>\(V = \pi r^2 h = \pi (5^2)(8) = \pi (25)(8) = 200\pi\text{ m}^3\).''',
        r'''Luôn mở Reference Sheet kiểm tra công thức 3D nếu phân vân: thể tích trụ là \(V = \pi r^2 h\) (bình phương bán kính \(r\), KHÔNG phải chiều cao \(h\)).''',
        {
            'A': ('Forgot to Square Radius', r'Tính \(\pi \cdot 5 \cdot 8 = 40\pi\) mà quên bình phương bán kính \(r\).'),
            'B': ('Used Lateral Surface Area Formula', r'Dùng nhầm công thức diện tích xung quanh \(2\pi r h = 2\pi(5)(8) = 80\pi\).'),
            'C': ('Correct', r'Áp dụng đúng \(V = \pi r^2 h = \pi(5^2)(8) = 200\pi\).'),
            'D': ('Squared Height Instead of Radius', r'Bình phương nhầm chiều cao \(8^2\) thay vì bán kính \(5^2\): \(\pi(5)(64) = 320\pi\).'),
        },
        desmos_tip_vi=r'''Gõ <code>5^2 * 8</code> trong Desmos ra \(200\), ghép thêm \(\pi\) được ngay \(200\pi\).''',
    ))

    # =========================================================================
    # Q22 — Geometry (Medium, SPR -> 25) | Theme: Geodesic Dome Similar Panels (SVG)
    # =========================================================================
    svg_q22 = svg_similar_triangles(
        side_ab='6', side_bc='10', side_de='15', side_ef='x',
        v1='A', v2='B', v3='C', v4='D', v5='E', v6='F'
    )
    qs.append(math_spr(
        'sat_mm4_m2l_q22', 22, 'Geometry and Trigonometry', 'Similar triangles — proportional side lengths', 'Medium',
        rf'''<div style="text-align:center;margin-bottom:10px;">{svg_q22}</div><p>In the figure above, triangular geodesic dome panels \(\triangle ABC\) and \(\triangle DEF\) are similar, where vertex \(A\) corresponds to \(D\), \(B\) corresponds to \(E\), and \(C\) corresponds to \(F\). If \(AB = 6\), \(BC = 10\), and \(DE = 15\), what is the length of side \(EF\), labeled \(x\)?</p>''',
        r'''<p>Enter the value of \(x\).</p>''',
        ['25'],
        '25',
        r'''Vì \(\triangle ABC \sim \triangle DEF\), tỉ số các cặp cạnh tương ứng bằng nhau:<br>\(\dfrac{EF}{BC} = \dfrac{DE}{AB} \Rightarrow \dfrac{x}{10} = \dfrac{15}{6} = \dfrac{5}{2} = 2.5\).<br>Nhân hai vế với \(10\): \(x = 10 \times 2.5 = 25\).''',
        r'''Khi lập tỉ lệ thức cho hai tam giác đồng dạng, giữ đúng hướng (tam giác lớn / tam giác nhỏ) ở cả hai phân số để không bị đảo ngược tỉ số.''',
        desmos_tip_vi=r'''Tính ngay trong Desmos: <code>10 * (15 / 6)</code> cho kết quả chính xác <code>25</code>.''',
    ))

    return qs


def verify_math():
    """Programmatic exact arithmetic verification for all 22 Module 2 Standard/Lower questions."""
    # Q1: 5x - 8 = 27 -> 2x + 1 = 15
    x1 = Fraction(27 + 8, 5)
    assert x1 == 7 and 2 * x1 + 1 == 15

    # Q2: C(k) = 0.25k + 15 -> C(0) = 15, C(40) = 25
    assert Fraction(25, 100) * 0 + 15 == 15 and Fraction(25, 100) * 40 + 15 == 25

    # Q3: slope through (2, 5) and (6, 17)
    assert Fraction(17 - 5, 6 - 2) == 3

    # Q4: h(8) = 2.5(8) + 14 = 34
    assert Fraction(25, 10) * 8 + 14 == 34

    # Q5: y = 3x, x + y = 28 -> y = 21
    x5 = Fraction(28, 4)
    y5 = 3 * x5
    assert x5 == 7 and y5 == 21 and x5 + y5 == 28

    # Q6: 140 + 18b <= 500 -> max b = 20
    assert Fraction(500 - 140, 18) == 20

    # Q7: 4x - 3y = 36 -> x-intercept when y = 0 is (9, 0)
    assert Fraction(36, 4) == 9

    # Q8: a + s = 50, 12a + 8s = 520 -> a = 30
    a8 = Fraction(520 - 8 * 50, 12 - 8)
    s8 = 50 - a8
    assert a8 == 30 and s8 == 20 and 12 * a8 + 8 * s8 == 520

    # Q9: f(5) = 5^2 - 4(5) + 7 = 12
    assert 5**2 - 4 * 5 + 7 == 12

    # Q10: (x^4)^3 / x^5 = x^7
    assert (2**4)**3 // (2**5) == 2**7

    # Q11: x^2 - 7x + 10 = 0 -> x = 2, 5
    for r in (2, 5):
        assert r**2 - 7 * r + 10 == 0

    # Q12: 1 - 0.96 = 0.04 = 4%
    assert (1 - Fraction(96, 100)) * 100 == 4

    # Q13: sqrt(2x + 9) = 7 -> x = 20
    x13 = Fraction(7**2 - 9, 2)
    assert x13 == 20 and math.isqrt(int(2 * x13 + 9)) == 7

    # Q14: (2x - 3)(x + 5) == 2x^2 + 7x - 15
    for xv in (-4, 0, 3, 7):
        assert (2 * xv - 3) * (xv + 5) == 2 * xv**2 + 7 * xv - 15

    # Q15: f(x) = a(x - 3)^2 - 4 passing through (5, 4) -> a = 2
    a15 = Fraction(4 - (-4), (5 - 3)**2)
    assert a15 == 2 and a15 * (5 - 3)**2 - 4 == 4

    # Q16: (180 / 4) * 9 = 405
    assert Fraction(180, 4) * 9 == 405

    # Q17: 108 / 200 = 54%
    assert 62 + 46 == 108 and 38 + 54 == 92 and 108 + 92 == 200
    assert Fraction(108, 200) * 100 == 54

    # Q18: 0.80 * P = 520 -> P = 650
    p18 = Fraction(520, 1) / Fraction(80, 100)
    assert p18 == 650 and p18 * Fraction(80, 100) == 520

    # Q19: median of [3,3, 5,5,5, 7,7,7,7, 9,9] is 7
    data19 = [3]*2 + [5]*3 + [7]*4 + [9]*2
    assert len(data19) == 11 and data19[5] == 7

    # Q20: right triangle 9-12-15
    x20 = math.isqrt(9**2 + 12**2)
    assert x20**2 == 9**2 + 12**2 and x20 == 15

    # Q21: cylinder r=5, h=8 -> V = 200pi
    assert 5**2 * 8 == 200

    # Q22: x / 10 = 15 / 6 -> x = 25
    x22 = Fraction(15, 6) * 10
    assert x22 == 25

    return True


if __name__ == '__main__':
    assert verify_math()
    qs = get_m2l_questions()
    print(f"M2L verified: {len(qs)} questions")
