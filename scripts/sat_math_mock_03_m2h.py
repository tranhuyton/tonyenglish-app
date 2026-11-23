# -*- coding: utf-8 -*-
"""
Digital SAT Math Adaptive Mock Test #3 — Module 2 (Hard Route, 650-800 Band)
22 Questions: 16 MCQ (A:4, B:4, C:4, D:4) + 6 SPR (Q5, Q9, Q13, Q16, Q19, Q22)
Domains: Algebra (Q1-Q8), Advanced Math (Q9-Q15),
         Problem-Solving and Data Analysis (Q16-Q19),
         Geometry and Trigonometry (Q20-Q22)
Q14-Q22 feature true 750-800 parametric, multi-step, and 3D similarity challenges.
IDs: sat_mm3_m2h_q1 .. sat_mm3_m2h_q22
"""

from fractions import Fraction
import math
from sat_math_helpers import (
    math_mcq,
    math_spr,
    build_math_table,
    svg_circle_sector,
    svg_right_triangle,
    svg_cylinder,
)


def get_m2h_questions():
    qs = []

    # =========================================================================
    # DOMAIN 1: ALGEBRA (Q1 - Q8)
    # =========================================================================

    # Q1 — MCQ (D) — Medium — Fractional linear equation + target expression (Semiconductor)
    qs.append(math_mcq(
        'sat_mm3_m2h_q1', 1, 'Algebra', 'Linear Equations in One Variable', 'Medium',
        r'<p>In a semiconductor lithography calibration check, the alignment offset \(x\) satisfies the equation:</p><p style="text-align:center;">\[\frac{5x - 7}{3} - \frac{2x + 1}{6} = \frac{11}{2}\]</p>',
        r'<p>What is the value of \(8x - 10\)?</p>',
        {'A': r'6', 'B': r'23', 'C': r'33', 'D': r'38'},
        'D',
        '\n'.join([
            r'Bước 1: Nhân cả hai vế với mẫu chung nhỏ nhất là \(6\): \(2(5x - 7) - (2x + 1) = 33\).',
            r'Bước 2: Phá ngoặc cẩn thận dấu trừ: \(10x - 14 - 2x - 1 = 33 \Rightarrow 8x - 15 = 33\).',
            r'Bước 3 (Phím tắt tốc độ): Đề hỏi \(8x - 10\), chỉ cần cộng \(5\) vào cả hai vế của \(8x - 15 = 33\): \(8x - 10 = 33 + 5 = 38\).',
            r'(Kiểm tra trực tiếp: \(8x = 48 \Rightarrow x = 6 \Rightarrow 8(6) - 10 = 38\).)',
        ]),
        r'Khi đề hỏi giá trị của một biểu thức tuyến tính như \(8x - 10\), hãy để ý xem có thể suy thẳng từ phương trình rút gọn \(8x - 15 = 33\) hay không — vừa nhanh hơn vừa tránh dừng sớm ở \(x = 6\)!',
        {
            'A': ('Stopped Early at x', r'Chỉ giải ra \(x = 6\) mà quên tính biểu thức mục tiêu \(8x - 10\).'),
            'B': ('Wrong Adjustment Sign', r'Từ \(8x - 15 = 33\) lại trừ thêm \(10\) thành \(33 - 10 = 23\) thay vì cộng \(5\).'),
            'C': ('Partial Constant Confusion', r'Nhầm vế phải \(33\) là đáp án cuối cùng sau khi quy đồng mẫu số.'),
            'D': ('Đáp án đúng', r'\(x = 6 \Rightarrow 8(6) - 10 = 38\).'),
        },
        desmos_tip_vi=r'Gõ <code>(5x-7)/3 - (2x+1)/6 = 11/2</code> để đọc nhanh <code>x = 6</code>, rồi dòng dưới tính <code>8(6) - 10 = 38</code>.'
    ))

    # Q2 — MCQ (A) — Medium — Shifted linear function & x-intercept (Alpine sensor)
    qs.append(math_mcq(
        'sat_mm3_m2h_q2', 2, 'Algebra', 'Linear Functions & Transformations', 'Medium',
        r'<p>For a linear function \(g\) modeling an alpine sensor’s baseline drift, the graph of \(y = g(x) + 4\) in the \(xy\)-plane passes through the points \((-2, 11)\) and \((4, -7)\).</p>',
        r'<p>What is the \(x\)-intercept of the graph of \(y = g(x)\)?</p>',
        {
            'A': r'\(\left(\frac{1}{3}, 0\right)\)',
            'B': r'\(\left(\frac{5}{3}, 0\right)\)',
            'C': r'\(\left(-\frac{1}{3}, 0\right)\)',
            'D': r'\((0, 1)\)',
        },
        'A',
        '\n'.join([
            r'Bước 1: Vì đồ thị \(y = g(x) + 4\) đi qua \((-2, 11)\) và \((4, -7)\), nên đồ thị \(y = g(x)\) (dịch xuống \(4\) đơn vị) đi qua \((-2, 7)\) và \((4, -11)\).',
            r'Bước 2: Tính hệ số góc: \(m = \frac{-11 - 7}{4 - (-2)} = \frac{-18}{6} = -3\).',
            r'Bước 3: Tìm tung độ gốc của \(g(x) = -3x + b\): \(7 = -3(-2) + b \Rightarrow 7 = 6 + b \Rightarrow b = 1\), vậy \(g(x) = -3x + 1\).',
            r'Bước 4: Đặt \(g(x) = 0\): \(-3x + 1 = 0 \Rightarrow x = \frac{1}{3}\). Giao điểm trục hoành là \(\left(\frac{1}{3}, 0\right)\).',
        ]),
        r'Khi đề cho điểm thuộc đồ thị dịch chuyển \(y = g(x) + k\), hãy trừ \(k\) khỏi tung độ của mọi điểm NGAY LẬP TỨC để làm việc trực tiếp trên \(y = g(x)\).',
        {
            'A': ('Đáp án đúng', r'\(g(x) = -3x + 1\) cắt trục hoành tại \(\left(\frac{1}{3}, 0\right)\).'),
            'B': ('Forgot Vertical Shift', r'Tìm \(x\)-intercept của \(y = g(x) + 4 = -3x + 5\), dẫn đến \(x = \frac{5}{3}\).'),
            'C': ('Sign Error', r'Giải sai phương trình \(-3x + 1 = 0\) thành \(x = -\frac{1}{3}\).'),
            'D': ('Intercept Swap', r'Tìm \(y\)-intercept \((0, 1)\) thay vì \(x\)-intercept.'),
        },
        desmos_tip_vi=r'Tạo bảng Table cho <code>(-2, 11-4)</code> và <code>(4, -7-4)</code>, chạy hồi quy <code>y_1 ~ m x_1 + b</code> rồi click giao điểm đường thẳng với trục \(x\) tại <code>(0.333, 0)</code>.'
    ))

    # Q3 — MCQ (C) — Medium-Hard — Integer linear programming / inequalities (Museum auction)
    qs.append(math_mcq(
        'sat_mm3_m2h_q3', 3, 'Algebra', 'Systems of Linear Inequalities & Optimization', 'Hard',
        r'<p>A fine-art auction house ships framed prints and bronze sculptures in a climate-controlled crate. Each framed print weighs \(6\) kilograms and is insured for $1,400; each bronze sculpture weighs \(15\) kilograms and is insured for $4,500. The crate can hold at most \(120\) kilograms, and the gallery must ship at least \(11\) artworks in total.</p>',
        r'<p>What is the maximum total insured value, in dollars, of the artworks that can be shipped in the crate?</p>',
        {'A': r'$28,000', 'B': r'$32,300', 'C': r'$34,000', 'D': r'$36,000'},
        'C',
        '\n'.join([
            r'Bước 1: Gọi \(p\) là số tranh in và \(s\) là số tượng đồng (\(p, s\) là số nguyên không âm). Ta có hệ ràng buộc:',
            r'\[6p + 15s \le 120 \iff 2p + 5s \le 40 \quad \text{và} \quad p + s \ge 11\]',
            r'Bước 2: So sánh giá trị bảo hiểm trên mỗi kg: tượng đồng đạt \(\frac{4,500}{15} = \$300/\text{kg}\), cao hơn tranh in \(\frac{1,400}{6} \approx \$233.33/\text{kg}\). Do đó cần tối đa hóa số tượng đồng \(s\).',
            r'Bước 3: Từ \(p \ge 11 - s\), thay vào điều kiện khối lượng: \(2(11 - s) + 5s \le 40 \Rightarrow 22 + 3s \le 40 \Rightarrow 3s \le 18 \Rightarrow s \le 6\).',
            r'Bước 4: Tại \(s = 6\), ta có \(p = 5\) (kiểm tra: \(6(5) + 15(6) = 120\text{ kg}\), tổng \(11\) tác phẩm). Giá trị tối đa: \(5(1,400) + 6(4,500) = 7,000 + 27,000 = \$34,000\).',
        ]),
        r'Trong bài toán tối ưu hệ bất phương trình tuyến tính, cực trị luôn nằm tại <b>giao điểm (đỉnh) của các đường biên</b>. So sánh đơn giá trên mỗi đơn vị tài nguyên (giá/kg) để biết cần ưu tiên biến nào.',
        {
            'A': ('Suboptimal Corner', r'Chỉ xếp toàn tranh in (\(p = 20, s = 0\)) cho tổng $28,000, thấp hơn tối ưu.'),
            'B': ('Non-Optimal Integer Point', r'Chọn \(s = 5, p = 7\) (nặng \(117\) kg) cho $32,300 — chưa đạt biên tối đa \(s = 6\).'),
            'C': ('Đáp án đúng', r'Đỉnh tối ưu \((p, s) = (5, 6)\) thỏa mãn đồng thời \(120\) kg và \(11\) tác phẩm, đạt $34,000.'),
            'D': ('Ignored Second Constraint', r'Xếp \(8\) tượng đồng (\(120\) kg, $36,000) nhưng vi phạm điều kiện tối thiểu \(11\) tác phẩm!'),
        },
        desmos_tip_vi=r'Vẽ vùng nghiệm <code>6x + 15y <= 120</code> và <code>x + y >= 11</code> trên Desmos, click giao điểm <code>(5, 6)</code> rồi tính <code>1400*5 + 4500*6 = 34000</code>.'
    ))

    # Q4 — MCQ (B) — Medium-Hard — Infinitely many solutions fractional system
    qs.append(math_mcq(
        'sat_mm3_m2h_q4', 4, 'Algebra', 'Systems of Linear Equations (Infinitely Many Solutions)', 'Hard',
        r'<p>Consider the system of linear equations below, where \(a\) and \(b\) are constants:</p><p style="text-align:center;">\[\frac{2}{5}x - \frac{3}{4}y = \frac{1}{2}\]\[ax + by = -10\]</p>',
        r'<p>If the system has infinitely many solutions, what is the value of \(a + b\)?</p>',
        {'A': r'-23', 'B': r'7', 'C': r'15', 'D': r'23'},
        'B',
        '\n'.join([
            r'Bước 1: Để hệ có vô số nghiệm, phương trình thứ hai phải là bội số của phương trình thứ nhất.',
            r'Bước 2: Tìm hệ số tỉ lệ từ vế phải: \(k = \frac{-10}{1/2} = -20\).',
            r'Bước 3: Nhân toàn bộ phương trình thứ nhất với \(-20\):',
            r'\[a = -20 \cdot \frac{2}{5} = -8, \qquad b = -20 \cdot \left(-\frac{3}{4}\right) = 15\]',
            r'Bước 4: Cộng lại: \(a + b = -8 + 15 = 7\).',
        ]),
        r'Khi hệ có vô số nghiệm và đã biết cả hai vế phải \(c_1, c_2\), hãy nhân phương trình 1 với đúng tỉ số \(k = \frac{c_2}{c_1}\) để đọc ngay mọi tham số ở vế trái.',
        {
            'A': ('Sign Error on b', r'Quên dấu trừ ở \(-\frac{3}{4}y\) nên tính nhầm \(b = -15 \Rightarrow a + b = -23\).'),
            'B': ('Đáp án đúng', r'\(a = -8, b = 15 \Rightarrow a + b = 7\).'),
            'C': ('Partial Solution', r'Chỉ tìm ra \(b = 15\) mà quên cộng \(a = -8\).'),
            'D': ('Sign Error on Multiplier', r'Dùng hệ số nhân \(+20\) thay vì \(-20\), ra \(a = 8, b = 15 \Rightarrow a + b = 23\).'),
        },
        desmos_tip_vi=r'Tính nhanh trong Desmos: <code>k = -10 / (1/2)</code>, rồi gõ <code>k*(2/5) + k*(-3/4)</code> ra trực tiếp <code>7</code>.'
    ))

    # Q5 — SPR (9/2 or 4.5) — Medium-Hard — Absolute value equation sum of solutions (Athletic biomechanics)
    qs.append(math_spr(
        'sat_mm3_m2h_q5', 5, 'Algebra', 'Absolute Value Equations', 'Hard',
        r'<p>In an athletic biomechanics timing calibration, the threshold parameter \(x\) satisfies the equation:</p><p style="text-align:center;">\[2|4x - 9| - 5 = 19\]</p>',
        r'<p>What is the sum of all solutions to the equation?</p>',
        ['9/2', '4.5'],
        '9/2 (hoặc 4.5)',
        '\n'.join([
            r'Bước 1: Cô lập biểu thức giá trị tuyệt đối: \(2|4x - 9| = 24 \Rightarrow |4x - 9| = 12\).',
            r'Bước 2: Tách hai trường hợp:',
            r'• Trường hợp 1: \(4x - 9 = 12 \Rightarrow 4x = 21 \Rightarrow x_1 = \frac{21}{4} = 5.25\).',
            r'• Trường hợp 2: \(4x - 9 = -12 \Rightarrow 4x = -3 \Rightarrow x_2 = -\frac{3}{4} = -0.75\).',
            r'Bước 3: Tổng các nghiệm: \(x_1 + x_2 = \frac{21}{4} + \left(-\frac{3}{4}\right) = \frac{18}{4} = \frac{9}{2} = 4.5\).',
            r'(Mẹo đối xứng: với \(|ax - b| = c > 0\), tổng hai nghiệm luôn bằng \(\frac{2b}{a} = \frac{18}{4} = 4.5\)!)',
        ]),
        r'Phương trình \(|ax - b| = c\) (với \(c > 0\)) luôn có hai nghiệm đối xứng qua trục \(x = \frac{b}{a}\), nên tổng hai nghiệm chính bằng \(\frac{2b}{a}\). Luôn nhớ kiểm tra \(c > 0\) trước khi áp dụng!',
        desmos_tip_vi=r'Vẽ <code>y = 2|4x - 9| - 5</code> và <code>y = 19</code> trên Desmos, click 2 giao điểm <code>(-0.75, 19)</code> và <code>(5.25, 19)</code> rồi cộng <code>-0.75 + 5.25 = 4.5</code>.'
    ))

    # Q6 — MCQ (A) — Hard — Quadrant analysis of system of linear inequalities
    qs.append(math_mcq(
        'sat_mm3_m2h_q6', 6, 'Algebra', 'Systems of Linear Inequalities in the xy-Plane', 'Hard',
        r'<p>Consider the system of linear inequalities in the \(xy\)-plane:</p><p style="text-align:center;">\[y > \frac{3}{2}x + 4\]\[y < -\frac{1}{2}x + 4\]</p>',
        r'<p>Which of the following correctly identifies all quadrants in the \(xy\)-plane that contain solutions to the system?</p>',
        {
            'A': r'Quadrants II and III only',
            'B': r'Quadrants I and II only',
            'C': r'Quadrants I, II, and III only',
            'D': r'Quadrant II only',
        },
        'A',
        '\n'.join([
            r'Bước 1: Để tồn tại \(y\) nằm giữa hai biên, biên dưới phải nhỏ hơn biên trên: \(\frac{3}{2}x + 4 < -\frac{1}{2}x + 4 \Rightarrow 2x < 0 \Rightarrow x < 0\).',
            r'Bước 2: Vì mọi nghiệm đều có \(x < 0\), vùng nghiệm hoàn toàn không chứa điểm nào thuộc Góc phần tư I (\(x > 0, y > 0\)) hay IV (\(x > 0, y < 0\)).',
            r'Bước 3: Kiểm tra dấu của \(y\) khi \(x < 0\):',
            r'• Với \(x = -2\): \(1 < y < 5 \Rightarrow (-2, 3)\) thuộc <b>Góc phần tư II</b>.',
            r'• Với \(x = -10\): \(-11 < y < 9 \Rightarrow (-10, -5)\) thuộc <b>Góc phần tư III</b>.',
            r'Bước 4: Vậy miền nghiệm chỉ nằm trong Góc phần tư II và III.',
        ]),
        r'Khi hai đường biên cắt nhau ngay trên trục tung \((0, b)\), bất đẳng thức kẹp giữa \(\text{biên dưới} < y < \text{biên trên}\) lập tức khóa dấu của \(x\) về hẳn một phía của trục tung.',
        {
            'A': ('Đáp án đúng', r'Mọi nghiệm đều có \(x < 0\) và \(y\) có thể dương hoặc âm nên phủ Góc phần tư II và III.'),
            'B': ('Intercept Visual Trap', r'Thấy cả hai đường cắt trục tung tại \((0, 4)\) nên ngộ nhận vùng nghiệm nằm phía trên trục hoành (I & II).'),
            'C': ('Forgot x < 0 Constraint', r'Không nhận ra hai đường đảo vị trí trên/dưới khi \(x > 0\), dẫn đến đưa nhầm Góc phần tư I vào.'),
            'D': ('Missed Negative y-Values', r'Chỉ thử các giá trị \(x\) âm nhỏ (như \(x = -1\)) mà bỏ quên rằng khi \(x < -\frac{8}{3}\), biên dưới âm nên vùng nghiệm đi sâu vào Góc phần tư III.'),
        },
        desmos_tip_vi=r'Gõ thẳng cả hai bất phương trình <code>y > (3/2)x + 4</code> và <code>y < -(1/2)x + 4</code> vào Desmos: miền tô chồng màu đậm chỉ nằm ở bên trái trục \(y\) (Góc phần tư II và III)!'
    ))

    # Q7 — MCQ (C) — Hard — Nonlinear parameter in linear system (infinitely many vs. no solution)
    qs.append(math_mcq(
        'sat_mm3_m2h_q7', 7, 'Algebra', 'Parametric Systems of Linear Equations', 'Hard',
        r'<p>In the system of equations below, \(p\) is a constant:</p><p style="text-align:center;">\[(p + 1)x + 6y = 18\]\[4x + (p - 1)y = 12\]</p>',
        r'<p>For what value of \(p\) does the system have infinitely many solutions?</p>',
        {'A': r'-5', 'B': r'3', 'C': r'5', 'D': r'6'},
        'C',
        '\n'.join([
            r'Bước 1: Để hệ có vô số nghiệm, tỉ lệ của cả ba cặp hệ số phải bằng nhau:',
            r'\[\frac{p + 1}{4} = \frac{6}{p - 1} = \frac{18}{12} = \frac{3}{2}\]',
            r'Bước 2: Giải tỉ lệ đầu tiên với \(\frac{3}{2}\): \(\frac{p + 1}{4} = \frac{3}{2} \Rightarrow p + 1 = 6 \Rightarrow p = 5\).',
            r'Bước 3: Kiểm tra lại tỉ lệ hệ số của \(y\) tại \(p = 5\): \(\frac{6}{5 - 1} = \frac{6}{4} = \frac{3}{2}\) (khớp hoàn toàn!).',
            r'(Lưu ý: giải chéo \((p + 1)(p - 1) = 24 \Rightarrow p^2 = 25 \Rightarrow p = \pm 5\), nhưng tại \(p = -5\) tỉ lệ vế trái là \(-1 \ne \frac{3}{2}\), đó là trường hợp <b>vô nghiệm</b> chứ không phải vô số nghiệm!)',
        ]),
        r'Khi giải điều kiện hệ số tỉ lệ ra 2 giá trị tham số (\(p = \pm 5\)), BẮT BUỘC đối chiếu với tỉ lệ hằng số tự do \(\frac{c_1}{c_2}\) để phân biệt <b>vô số nghiệm</b> (\(= c_1/c_2\)) và <b>vô nghiệm</b> (\(\ne c_1/c_2\)).',
        {
            'A': ('No-Solution Trap', r'Tại \(p = -5\), hai đường thẳng song song nhưng KHÔNG trùng nhau (\(-1 \ne \frac{3}{2}\)), nên hệ vô nghiệm.'),
            'B': ('Equated Raw Coefficients', r'Cho \(p + 1 = 4 \Rightarrow p = 3\) mà quên rằng vế phải có tỉ lệ \(18 : 12 = 3 : 2\).'),
            'C': ('Đáp án đúng', r'Tại \(p = 5\), phương trình (1) là \(6x + 6y = 18\) và (2) là \(4x + 4y = 12\), cùng rút gọn về \(x + y = 3\).'),
            'D': ('Solved for p+1', r'Tính đúng \(p + 1 = 6\) nhưng quên trừ \(1\) để ra \(p\).'),
        },
        desmos_tip_vi=r'Gõ hai phương trình kèm slider <code>p</code>; kéo tới <code>p = 5</code> hai đường trùng khít 1 đường duy nhất, còn tại <code>p = -5</code> hai đường song song tách rời.'
    ))

    # Q8 — MCQ (D) — Hard — Linear drainage models & ratio condition (Municipal water reservoirs)
    qs.append(math_mcq(
        'sat_mm3_m2h_q8', 8, 'Algebra', 'Linear Models & Systems Applications', 'Hard',
        r'<p>Two municipal water reservoirs begin draining simultaneously at \(t = 0\) hours. The volume of water remaining, in thousands of cubic meters, after \(t\) hours is modeled by \(V_A(t) = 89 - 4t\) for Reservoir A and \(V_B(t) = 64 - 2t\) for Reservoir B.</p>',
        r'<p>At the instant when the volume remaining in Reservoir A is exactly \(1.25\) times the volume remaining in Reservoir B, what is the combined volume, in thousands of cubic meters, remaining in both reservoirs?</p>',
        {'A': r'52', 'B': r'65', 'C': r'78', 'D': r'117'},
        'D',
        '\n'.join([
            r'Bước 1: Thiết lập phương trình theo điều kiện tỉ lệ: \(V_A(t) = 1.25\,V_B(t)\).',
            r'\[89 - 4t = 1.25(64 - 2t) = 80 - 2.5t\]',
            r'Bước 2: Giải tìm \(t\): \(89 - 80 = 4t - 2.5t \Rightarrow 9 = 1.5t \Rightarrow t = 6\) giờ.',
            r'Bước 3: Tính thể tích còn lại ở từng hồ tại \(t = 6\):',
            r'• \(V_A(6) = 89 - 4(6) = 65\) (nghìn \(\text{m}^3\)); kiểm tra tỉ số: \(\frac{65}{52} = 1.25\).',
            r'• \(V_B(6) = 64 - 2(6) = 52\) (nghìn \(\text{m}^3\)).',
            r'Bước 4: Tổng thể tích hai hồ: \(65 + 52 = 117\) nghìn \(\text{m}^3\).',
        ]),
        r'Trong các bài toán đố nhiều bước Hard M2, luôn gạch chân yêu cầu cuối cùng ("combined volume") và kiểm tra lại tỉ lệ \(V_A / V_B = 1.25\) trước khi chọn đáp án.',
        {
            'A': ('Partial Solution', r'Chỉ tính thể tích còn lại của Reservoir B (\(V_B(6) = 52\)).'),
            'B': ('Partial Solution', r'Chỉ tính thể tích còn lại của Reservoir A (\(V_A(6) = 65\)).'),
            'C': ('Wrong Condition (Equal Volumes)', r'Giải nhầm điều kiện \(V_A(t) = V_B(t) \Rightarrow t = 12.5 \Rightarrow 39 + 39 = 78\) thay vì \(V_A = 1.25V_B\).'),
            'D': ('Đáp án đúng', r'Tổng thể tích tại \(t = 6\) giờ là \(65 + 52 = 117\) nghìn \(\text{m}^3\).'),
        },
        desmos_tip_vi=r'Đặt <code>A(x) = 89 - 4x</code> và <code>B(x) = 64 - 2x</code>; tìm giao điểm của <code>y = A(x)</code> và <code>y = 1.25 B(x)</code> ra <code>x = 6</code>, rồi gõ <code>A(6) + B(6)</code> = <code>117</code>.'
    ))

    # =========================================================================
    # DOMAIN 2: ADVANCED MATH (Q9 - Q15)
    # =========================================================================

    # Q9 — SPR (16) — Medium-Hard — Vieta's formulas & sum of squares of roots
    qs.append(math_spr(
        'sat_mm3_m2h_q9', 9, 'Advanced Math', 'Quadratic Equations & Vieta’s Formulas', 'Hard',
        r'<p>The quadratic equation \(3x^2 - 14x + k = 0\), where \(k\) is a constant, has two distinct real solutions \(r\) and \(s\).</p>',
        r'<p>If \(r^2 + s^2 = \frac{100}{9}\), what is the value of \(k\)?</p>',
        ['16'],
        '16',
        '\n'.join([
            r'Bước 1: Áp dụng định lý Vieta cho \(3x^2 - 14x + k = 0\):',
            r'\[r + s = -\frac{-14}{3} = \frac{14}{3}, \qquad rs = \frac{k}{3}\]',
            r'Bước 2: Dùng hằng đẳng thức \(r^2 + s^2 = (r + s)^2 - 2rs\):',
            r'\[\frac{100}{9} = \left(\frac{14}{3}\right)^2 - 2\left(\frac{k}{3}\right) = \frac{196}{9} - \frac{2k}{3}\]',
            r'Bước 3: Chuyển vế giải \(k\): \(\frac{2k}{3} = \frac{196 - 100}{9} = \frac{96}{9} = \frac{32}{3} \Rightarrow 2k = 32 \Rightarrow k = 16\).',
            r'Bước 4: Kiểm tra điều kiện 2 nghiệm thực phân biệt: \(\Delta = 196 - 12(16) = 4 > 0\) (hai nghiệm là \(2\) và \(\frac{8}{3}\), thỏa mãn!).',
        ]),
        r'Cặp công thức 750+ không thể thiếu: \(r + s = -\frac{b}{a}\), \(rs = \frac{c}{a}\), và \(r^2 + s^2 = (r + s)^2 - 2rs\). Không bao giờ cần giải công thức nghiệm căn thức phức tạp!',
        desmos_tip_vi=r'Gõ <code>(14/3)^2 - 2*(k/3) = 100/9</code> trên Desmos (đổi <code>k</code> thành <code>x</code>) để nhận ngay nghiệm thẳng đứng <code>x = 16</code>.'
    ))

    # Q10 — MCQ (B) — Medium-Hard — Polynomial division / equivalent rational form
    qs.append(math_mcq(
        'sat_mm3_m2h_q10', 10, 'Advanced Math', 'Equivalent Rational Expressions', 'Hard',
        r'<p>For all \(x \ne \frac{3}{2}\), the rational expression \(\frac{6x^2 - 5x - 10}{2x - 3}\) is equivalent to \(3x + a + \frac{b}{2x - 3}\), where \(a\) and \(b\) are constants.</p>',
        r'<p>What is the value of \(a - b\)?</p>',
        {'A': r'-2', 'B': r'6', 'C': r'12', 'D': r'18'},
        'B',
        '\n'.join([
            r'Bước 1: Nhân hai vế với \((2x - 3)\) để khử mẫu: \(6x^2 - 5x - 10 = (3x + a)(2x - 3) + b\).',
            r'Bước 2: Khai triển vế phải: \(6x^2 + (2a - 9)x + (-3a + b)\).',
            r'Bước 3: Đồng nhất hệ số của \(x\): \(2a - 9 = -5 \Rightarrow 2a = 4 \Rightarrow a = 2\).',
            r'Bước 4: Đồng nhất hằng số tự do: \(-3(2) + b = -10 \Rightarrow -6 + b = -10 \Rightarrow b = -4\).',
            r'Bước 5: Tính \(a - b = 2 - (-4) = 6\).',
        ]),
        r'Khử mẫu bằng cách nhân chéo rồi đồng nhất hệ số nhanh hơn chia đa thức truyền thống rất nhiều. Có thể kiểm tra nhanh số dư \(b\) bằng Định lý số dư: thay \(x = \frac{3}{2}\) vào tử số \(6(9/4) - 5(3/2) - 10 = -4\).',
        {
            'A': ('Operation Confusion', r'Tính tổng \(a + b = 2 + (-4) = -2\) thay vì hiệu \(a - b\).'),
            'B': ('Đáp án đúng', r'\(a = 2\) và \(b = -4\), do đó \(a - b = 2 - (-4) = 6\).'),
            'C': ('Ignored Quotient Product', r'Lấy thẳng hằng số \(-10\) ở tử làm \(b\), bỏ quên hạng tử \(-3a\), ra \(2 - (-10) = 12\).'),
            'D': ('Sign Error', r'Nhân nhầm \((-3)(2)\) thành \(+6\), suy ra \(b = -16\) và \(a - b = 18\).'),
        },
        desmos_tip_vi=r'Gõ <code>f(x) = (6x^2 - 5x - 10)/(2x - 3)</code> và <code>g(x) = 3x + a + b/(2x - 3)</code> kèm slider <code>a, b</code>; khi <code>a = 2, b = -4</code> hai đồ thị trùng khít hoàn toàn!'
    ))

    # Q11 — MCQ (D) — Hard — Exponential re-indexing / changing time period (Semiconductor wafer)
    qs.append(math_mcq(
        'sat_mm3_m2h_q11', 11, 'Advanced Math', 'Exponential Functions & Period Conversion', 'Hard',
        r'<p>During a thermal annealing cycle for semiconductor wafers, the surface defect density \(D(t)\), in defects per square centimeter, decreases exponentially over \(t\) minutes. Initially, \(D(0) = 320\), and every \(30\) minutes the defect density decreases by \(36\%\).</p>',
        r'<p>Which function defines \(D(t)\) with the base representing the multiplicative factor applied every \(15\) minutes?</p>',
        {
            'A': r'\(D(t) = 320(0.32)^{\frac{t}{15}}\)',
            'B': r'\(D(t) = 320(0.4096)^{\frac{t}{15}}\)',
            'C': r'\(D(t) = 320(0.64)^{\frac{t}{15}}\)',
            'D': r'\(D(t) = 320(0.80)^{\frac{t}{15}}\)',
        },
        'D',
        '\n'.join([
            r'Bước 1: Giảm \(36\%\) mỗi \(30\) phút tương ứng hệ số nhân \(1 - 0.36 = 0.64\): \(D(t) = 320(0.64)^{\frac{t}{30}}\).',
            r'Bước 2: Viết lại số mũ theo chu kỳ \(15\) phút: \(\frac{t}{30} = \frac{1}{2} \cdot \frac{t}{15}\).',
            r'Bước 3: Đưa lũy thừa \(\frac{1}{2}\) vào cơ số: \((0.64)^{\frac{1}{2}} = \sqrt{0.64} = 0.80\).',
            r'Bước 4: Suy ra \(D(t) = 320(0.80)^{\frac{t}{15}}\) (tức mỗi \(15\) phút giảm \(20\%\); hai lần nhân \(0.80\) liên tiếp trong \(30\) phút là \(0.80^2 = 0.64\)).',
        ]),
        r'Khi chia đôi chu kỳ thời gian của hàm mũ (từ \(30\) phút xuống \(15\) phút), cơ số phải lấy <b>căn bậc hai</b> (\(\sqrt{b}\)), TUYỆT ĐỐI không chia đôi cơ số hay chia đôi phần trăm giảm!',
        {
            'A': ('Halved Base Trap', r'Chia đôi cơ số \(0.64 \div 2 = 0.32\) thay vì lấy căn bậc hai.'),
            'B': ('Squared Instead of Root', r'Bình phương cơ số \(0.64^2 = 0.4096\) (đây là hệ số cho chu kỳ \(60\) phút, không phải \(15\) phút).'),
            'C': ('Unchanged Base Trap', r'Đổi mẫu số mũ từ \(30\) sang \(15\) nhưng giữ nguyên cơ số \(0.64\).'),
            'D': ('Đáp án đúng', r'\(\left(0.80\right)^{30/15} = 0.80^2 = 0.64\), khớp chuẩn xác giảm \(36\%\) sau \(30\) phút.'),
        },
        desmos_tip_vi=r'Gõ <code>f(x) = 320*(0.64)^(x/30)</code> rồi thử gõ các đáp án; chỉ <code>320*(0.80)^(x/15)</code> cho đồ thị chồng khít 100% lên <code>f(x)</code>.'
    ))

    # Q12 — MCQ (A) — Hard — Nonlinear system no real solutions (discriminant inequality)
    qs.append(math_mcq(
        'sat_mm3_m2h_q12', 12, 'Advanced Math', 'Nonlinear Systems & Discriminant Inequalities', 'Hard',
        r'<p>Consider the system of equations in the \(xy\)-plane, where \(m\) is a real constant:</p><p style="text-align:center;">\[y = x^2 + 6x + 14\]\[y = mx + 5\]</p>',
        r'<p>If the system has no real solutions, which inequality represents all possible values of \(m\)?</p>',
        {
            'A': r'\(0 < m < 12\)',
            'B': r'\(-12 < m < 0\)',
            'C': r'\(m < 0 \text{ or } m > 12\)',
            'D': r'\(m < 12\)',
        },
        'A',
        '\n'.join([
            r'Bước 1: Lập phương trình hoành độ giao điểm: \(x^2 + 6x + 14 = mx + 5 \Rightarrow x^2 + (6 - m)x + 9 = 0\).',
            r'Bước 2: Hệ vô nghiệm thực khi và chỉ khi biệt thức \(\Delta < 0\):',
            r'\[(6 - m)^2 - 4(1)(9) < 0 \Rightarrow (6 - m)^2 < 36\]',
            r'Bước 3: Khai căn bất đẳng thức bình phương: \(-6 < 6 - m < 6\).',
            r'Bước 4: Trừ \(6\) ở cả ba vế rồi nhân \(-1\) (đổi chiều): \(-12 < -m < 0 \iff 0 < m < 12\).',
        ]),
        r'Khi giải bất đẳng thức dạng \((6 - m)^2 < 36\), luôn đưa về bất đẳng thức kép \(-6 < 6 - m < 6\) (giữa hai nghiệm \(m = 0\) và \(m = 12\)). Chú ý đổi chiều khi nhân với \(-1\).',
        {
            'A': ('Đáp án đúng', r'Với \(0 < m < 12\), \(\Delta = m(m - 12) < 0\) nên đường thẳng không cắt parabol.'),
            'B': ('Sign Error in Quadratic', r'Chuyển vế sai thành \(x^2 + (6 + m)x + 9 = 0\), dẫn đến \(-12 < m < 0\).'),
            'C': ('Reversed Inequality', r'Giải nhầm điều kiện \(\Delta > 0\) (hai giao điểm) thay vì \(\Delta < 0\) (vô nghiệm).'),
            'D': ('Forgot Lower Bound', r'Chỉ xét nhánh dương \(6 - m > -6 \Rightarrow m < 12\), quên nhánh còn lại \(6 - m < 6 \Rightarrow m > 0\).'),
        },
        desmos_tip_vi=r'Gõ <code>y = x^2 + 6x + 14</code> và <code>y = mx + 5</code> kèm slider <code>m</code>; đường thẳng tách rời hoàn toàn khỏi parabol đúng trong khoảng <code>0 < m < 12</code>!'
    ))

    # Q13 — SPR (65/4 or 16.25) — Hard — Hidden quadratic in sqrt(x)
    qs.append(math_spr(
        'sat_mm3_m2h_q13', 13, 'Advanced Math', 'Quadratic-Form Radical Equations', 'Hard',
        r'<p>Consider the equation below for \(x \ge 0\):</p><p style="text-align:center;">\[2x - 9\sqrt{x} + 4 = 0\]</p>',
        r'<p>What is the sum of all real solutions to this equation?</p>',
        ['65/4', '16.25'],
        '65/4 (hoặc 16.25)',
        '\n'.join([
            r'Bước 1: Đặt ẩn phụ \(u = \sqrt{x}\) (với điều kiện \(u \ge 0\)), khi đó \(x = u^2\). Phương trình trở thành:',
            r'\[2u^2 - 9u + 4 = 0\]',
            r'Bước 2: Phân tích thành nhân tử: \((2u - 1)(u - 4) = 0 \Rightarrow u = \frac{1}{2}\) hoặc \(u = 4\) (cả hai đều dương, hợp lệ).',
            r'Bước 3: Trả về biến \(x = u^2\): \(x_1 = \left(\frac{1}{2}\right)^2 = \frac{1}{4}\) và \(x_2 = 4^2 = 16\).',
            r'Bước 4: Tổng các nghiệm: \(x_1 + x_2 = \frac{1}{4} + 16 = \frac{65}{4} = 16.25\).',
        ]),
        r'Bẫy 760+ kinh điển: khi đặt \(u = \sqrt{x}\), ĐỪNG quên bình phương ngược lại (\(x = u^2\)) trước khi cộng nghiệm — rất nhiều thí sinh dùng nhầm Vieta \(u_1 + u_2 = 9/2 = 4.5\)!',
        desmos_tip_vi=r'Vẽ <code>y = 2x - 9*sqrt(x) + 4</code> trên Desmos, click vào hai giao điểm trục \(x\) tại <code>(0.25, 0)</code> và <code>(16, 0)</code> rồi cộng <code>0.25 + 16 = 16.25</code>!'
    ))

    # Q14 — MCQ (C) — Very Hard (760-800) — Symmetric quadratic points & vertex extremum
    qs.append(math_mcq(
        'sat_mm3_m2h_q14', 14, 'Advanced Math', 'Quadratic Symmetry & Parametric Models', 'Hard',
        r'<p>In an athletic biomechanics force model, a quadratic function \(f(x) = ax^2 + bx + c\), where \(a\), \(b\), and \(c\) are constants, satisfies \(f(2) = f(8) = 5\) and \(f(0) = -27\).</p>',
        r'<p>What is the maximum value of \(f(x)\)?</p>',
        {'A': r'13', 'B': r'18', 'C': r'23', 'D': r'27'},
        'C',
        '\n'.join([
            r'Bước 1 (Kỹ thuật viết dạng nhân tử dịch chuyển 780+): Vì \(f(2) = f(8) = 5\), hàm \(f(x) - 5\) có hai nghiệm \(x = 2\) và \(x = 8\), nên:',
            r'\[f(x) = a(x - 2)(x - 8) + 5\]',
            r'Bước 2: Dùng điều kiện \(f(0) = -27\) để tìm \(a\): \(a(-2)(-8) + 5 = -27 \Rightarrow 16a = -32 \Rightarrow a = -2\).',
            r'Bước 3: Vì \(a = -2 < 0\) (parabol úp xuống) và trục đối xứng nằm chính giữa \(2\) và \(8\) tại \(h = \frac{2 + 8}{2} = 5\), giá trị cực đại là:',
            r'\[f(5) = -2(5 - 2)(5 - 8) + 5 = -2(3)(-3) + 5 = 18 + 5 = 23\]',
        ]),
        r'Bí kíp 800 Math: hễ thấy hai điểm cùng tung độ \(f(x_1) = f(x_2) = k\), viết ngay \(f(x) = a(x - x_1)(x - x_2) + k\) và trục đối xứng luôn là \(h = \frac{x_1 + x_2}{2}\)!',
        {
            'A': ('Sign Error on Shift', r'Tính đúng \(18\) nhưng trừ \(5\) thay vì cộng \(5\): \(18 - 5 = 13\).'),
            'B': ('Forgot Vertical Offset +5', r'Chỉ tính \(-2(3)(-3) = 18\) mà quên cộng thêm tung độ tham chiếu \(+5\).'),
            'C': ('Đáp án đúng', r'\(f(x) = -2x^2 + 20x - 27\) đạt cực đại tại \(x = 5\) với \(f(5) = 23\).'),
            'D': ('Intercept Confusion', r'Lấy nhầm giá trị tuyệt đối của \(f(0) = -27\).'),
        },
        desmos_tip_vi=r'Tạo bảng Table gồm 3 điểm <code>(0, -27), (2, 5), (8, 5)</code>, gõ hồi quy parabol <code>y_1 ~ a x_1^2 + b x_1 + c</code> rồi click đỉnh parabol để đọc ngay <code>(5, 23)</code>!'
    ))

    # Q15 — MCQ (B) — Very Hard (780-800) — Factor theorem & parametric cubic divisibility
    qs.append(math_mcq(
        'sat_mm3_m2h_q15', 15, 'Advanced Math', 'Polynomial Divisibility & Factor Theorem', 'Hard',
        r'<p>The polynomial \(P(x) = 2x^3 + kx^2 - 14x + m\), where \(k\) and \(m\) are constants, is divisible by both \((x - 2)\) and \((2x + 1)\).</p>',
        r'<p>What is the value of \(k + m\)?</p>',
        {'A': r'-8', 'B': r'-3', 'C': r'5', 'D': r'13'},
        'B',
        '\n'.join([
            r'Bước 1 (Cách 1 — Định lý nhân tử): Vì \(P(x)\) chia hết cho \((x - 2)\) và \((2x + 1)\), ta có \(P(2) = 0\) và \(P\left(-\frac{1}{2}\right) = 0\).',
            r'• \(P(2) = 2(8) + 4k - 28 + m = 0 \Rightarrow 4k + m = 12\) (1)',
            r'• \(P\left(-\frac{1}{2}\right) = 2\left(-\frac{1}{8}\right) + \frac{k}{4} + 7 + m = 0 \Rightarrow \frac{k}{4} + m = -\frac{27}{4} \Rightarrow k + 4m = -27\) (2)',
            r'Bước 2: Từ (1) suy ra \(m = 12 - 4k\), thế vào (2): \(k + 4(12 - 4k) = -27 \Rightarrow 48 - 15k = -27 \Rightarrow 15k = 75 \Rightarrow k = 5\).',
            r'Bước 3: Suy ra \(m = 12 - 4(5) = -8\). Vậy \(k + m = 5 + (-8) = -3\).',
            r'(Cách 2 — Nhân tử thứ ba 10 giây: \(P(x) = (2x^2 - 3x - 2)(x - r)\) có hệ số \(x\) là \(3r - 2 = -14 \Rightarrow r = -4 \Rightarrow P(x) = (2x^2 - 3x - 2)(x + 4) = 2x^3 + 5x^2 - 14x - 8\).)',
        ]),
        r'Khi bậc của đa thức là \(3\) và đã biết 2 nhân tử bậc nhất, hãy viết \(P(x) = (\text{tích 2 nhân tử})(x - r)\) rồi đồng nhất hệ số đã biết (\(-14x\)) — nhanh gấp đôi việc giải hệ hai ẩn!',
        {
            'A': ('Partial Solution', r'Chỉ tìm giá trị của \(m = -8\) mà quên cộng \(k = 5\).'),
            'B': ('Đáp án đúng', r'\(k = 5\) và \(m = -8 \Rightarrow k + m = -3\).'),
            'C': ('Partial Solution', r'Chỉ tìm giá trị của \(k = 5\) mà quên cộng \(m = -8\).'),
            'D': ('Sign Error', r'Tính \(k - m = 5 - (-8) = 13\) thay vì \(k + m\).'),
        },
        desmos_tip_vi=r'Lập hệ <code>4x + y = 12</code> và <code>x + 4y = -27</code> trên Desmos (với <code>x=k, y=m</code>) → click giao điểm <code>(5, -8)</code> rồi tính <code>5 + (-8) = -3</code>.'
    ))

    # =========================================================================
    # DOMAIN 3: PROBLEM-SOLVING AND DATA ANALYSIS (Q16 - Q19)
    # =========================================================================

    # Q16 — SPR (50) — Very Hard (760-800) — Multi-factor area rate & percent comparison (Semiconductor)
    tbl_q16 = build_math_table(
        ['Fabrication Line', 'Circular Wafer Diameter (mm)', 'Usable Die Yield', 'Throughput (wafers/hour)'],
        [
            ['Line Alpha', '200', '80%', '45'],
            ['Line Beta', '300', '75%', '32'],
        ],
        caption='Semiconductor Cleanroom Hourly Wafer Production Specifications'
    )
    qs.append(math_spr(
        'sat_mm3_m2h_q16', 16, 'Problem-Solving and Data Analysis', 'Compound Rates, Geometric Ratios & Percent Change', 'Hard',
        rf'<p>The table below compares two semiconductor fabrication lines that process circular silicon wafers. For each wafer, the usable silicon area equals the circular wafer area multiplied by the line’s usable die yield.</p>{tbl_q16}',
        r'<p>The total usable circular silicon area produced per hour by Line Beta is \(p\%\) greater than that produced per hour by Line Alpha. What is the value of \(p\)?</p>',
        ['50'],
        '50',
        '\n'.join([
            r'Bước 1: Tính bán kính mỗi tấm wafer: Line Alpha có \(r_A = \frac{200}{2} = 100\text{ mm}\); Line Beta có \(r_B = \frac{300}{2} = 150\text{ mm}\).',
            r'Bước 2: Tổng diện tích sử dụng mỗi giờ của Line Alpha:',
            r'\[A_{\text{Alpha}} = \pi (100)^2 \times 0.80 \times 45 = 10,000\pi \times 36 = 360,000\pi\text{ mm}^2/\text{giờ}\]',
            r'Bước 3: Tổng diện tích sử dụng mỗi giờ của Line Beta:',
            r'\[A_{\text{Beta}} = \pi (150)^2 \times 0.75 \times 32 = 22,500\pi \times 24 = 540,000\pi\text{ mm}^2/\text{giờ}\]',
            r'Bước 4: Tính phần trăm lớn hơn so với Line Alpha:',
            r'\[p = \frac{540,000\pi - 360,000\pi}{360,000\pi} \times 100 = \frac{180}{360} \times 100 = 50\]',
        ]),
        r'Khi so sánh tỉ số diện tích hình tròn giữa hai quy trình, diện tích tỉ lệ với <b>bình phương đường kính</b> (\((300/200)^2 = 2.25\))! Tỉ số tổng hợp là \(2.25 \times \frac{75}{80} \times \frac{32}{45} = 1.50\), tức lớn hơn \(50\%\).',
        desmos_tip_vi=r'Bỏ \(\pi\) chung, gõ thẳng <code>((150^2 * 0.75 * 32) / (100^2 * 0.80 * 45) - 1) * 100</code> trên Desmos để ra đúng <code>50</code>.'
    ))

    # Q17 — MCQ (D) — Hard (750-800) — Mean vs. Standard Deviation from symmetric frequency table (Alpine)
    tbl_q17 = build_math_table(
        ['Pressure Anomaly (hPa)', 'Station P (days)', 'Station Q (days)'],
        [
            [r'\(-4\)', '2', '6'],
            [r'\(-2\)', '5', '4'],
            [r'\(0\)', '11', '5'],
            [r'\(+2\)', '5', '4'],
            [r'\(+4\)', '2', '6'],
        ],
        caption='25-Day Barometric Pressure Anomaly Distributions at Two Alpine Stations'
    )
    qs.append(math_mcq(
        'sat_mm3_m2h_q17', 17, 'Problem-Solving and Data Analysis', 'Center, Spread & Standard Deviation', 'Hard',
        rf'<p>The table below shows the frequency distributions of daily barometric pressure anomalies, in hectopascals (hPa), recorded over \(25\) days at two alpine weather stations, Station P and Station Q.</p>{tbl_q17}',
        r'<p>Which of the following statements accurately compares the mean and standard deviation of the \(25\) readings at Station P to those at Station Q?</p>',
        {
            'A': r'Both the mean and the standard deviation of Station P’s readings are greater than those of Station Q’s readings.',
            'B': r'The mean of Station P’s readings is greater than that of Station Q’s readings, and their standard deviations are equal.',
            'C': r'The means of the two stations’ readings are equal, and the standard deviation of Station P’s readings is greater than that of Station Q’s readings.',
            'D': r'The means of the two stations’ readings are equal, and the standard deviation of Station P’s readings is less than that of Station Q’s readings.',
        },
        'D',
        '\n'.join([
            r'Bước 1 (So sánh Mean): Cả hai bảng tần số đều <b>đối xứng hoàn hảo quanh \(0\)</b> (tần số của \(-4\) bằng \(+4\), và \(-2\) bằng \(+2\)), nên trung bình cộng của cả Station P và Station Q đều bằng \(0\text{ hPa}\).',
            r'Bước 2 (So sánh Standard Deviation): Độ lệch chuẩn đo mức độ phân tán của dữ liệu <b>xa khỏi trung bình</b>.',
            r'• Station P tập trung dày đặc ở giữa (\(11\) ngày tại \(0\), chỉ \(4\) ngày ở hai đầu cực \(\pm 4\)) \(\Rightarrow\) độ lệch chuẩn NHỎ hơn (\(\text{SD}_P = \sqrt{\frac{104}{25}} \approx 2.04\)).',
            r'• Station Q có nhiều ngày dồn ra hai đầu cực (\(12\) ngày tại \(\pm 4\), chỉ \(5\) ngày tại \(0\)) \(\Rightarrow\) độ lệch chuẩn LỚN hơn (\(\text{SD}_Q = \sqrt{\frac{224}{25}} \approx 2.99\)).',
        ]),
        r'Quy tắc nhận diện Độ lệch chuẩn (SD) không cần bấm máy: hai tập có cùng Range và cùng Mean nhưng tập nào dồn tần số nhiều hơn về <b>hai đầu cực (tails)</b> thì có SD <b>LỚN hơn</b>; tập dồn vào tâm có SD nhỏ hơn.',
        {
            'A': ('Missed Symmetry', r'Cả hai phân phối đều đối xứng quanh \(0\) nên trung bình bằng nhau, không có chuyện P lớn hơn Q.'),
            'B': ('Range vs. SD Confusion', r'Sai cả hai vế: trung bình bằng nhau, và cùng khoảng biến thiên (Range = 8) KHÔNG có nghĩa cùng độ lệch chuẩn.'),
            'C': ('Reversed SD Concept', r'Hiểu ngược khái niệm độ lệch chuẩn: đỉnh giữa cao (\(11\) ngày tại \(0\)) chứng tỏ dữ liệu ÍT phân tán hơn (SD nhỏ hơn), không phải lớn hơn!'),
            'D': ('Đáp án đúng', r'Trung bình bằng nhau (cùng bằng \(0\)) và \(\text{SD}_P < \text{SD}_Q\).'),
        },
        desmos_tip_vi=r'Nếu muốn kiểm chứng bằng số trên Desmos, tính phương sai của P: <code>(2*16 + 5*4 + 5*4 + 2*16)/25 = 4.16</code> so với Q: <code>(6*16 + 4*4 + 4*4 + 6*16)/25 = 8.96</code> \(\Rightarrow \text{SD}_P < \text{SD}_Q\).'
    ))

    # Q18 — MCQ (B) — Hard (750-800) — Margin of error & statistical inference (Museum conservation)
    qs.append(math_mcq(
        'sat_mm3_m2h_q18', 18, 'Problem-Solving and Data Analysis', 'Statistical Inference & Margin of Error', 'Hard',
        r'<p>A museum consortium randomly selected \(400\) art conservators from a national registry of \(12,000\) certified conservators and asked whether they use laser-ablation cleaning on marble sculptures. In the sample, \(38\%\) answered yes, with an associated margin of error of \(4.7\%\) at the \(95\%\) confidence level.</p>',
        r'<p>Which of the following conclusions is most appropriately supported by this study?</p>',
        {
            'A': r'Exactly \(38\%\) of all \(12,000\) certified conservators in the national registry use laser-ablation cleaning.',
            'B': r'It is plausible that between \(33.3\%\) and \(42.7\%\) of all \(12,000\) certified conservators in the national registry use laser-ablation cleaning.',
            'C': r'It is plausible that between \(33.3\%\) and \(42.7\%\) of all art conservators worldwide use laser-ablation cleaning.',
            'D': r'If the consortium had randomly sampled \(1,600\) conservators instead of \(400\), the margin of error would have been approximately \(9.4\%\).',
        },
        'B',
        '\n'.join([
            r'Bước 1: Khoảng giá trị hợp lý (plausible interval) cho tỉ lệ tổng thể là \(\hat{p} \pm \text{ME} = 38\% \pm 4.7\% = [33.3\%,\; 42.7\%]\).',
            r'Bước 2: Vì mẫu được chọn <b>ngẫu nhiên</b> từ danh sách \(12,000\) chuyên gia trong national registry, kết luận chỉ được suy rộng cho đúng tổng thể \(12,000\) người trong danh sách này (không suy rộng ra toàn thế giới).',
            r'Bước 3: Đáp án B dùng ngôn ngữ xác suất chuẩn ("It is plausible that..."), đúng khoảng số và đúng phạm vi tổng thể.',
        ]),
        r'3 nguyên tắc vàng Suy luận Thống kê SAT: (1) Dùng ngôn ngữ "plausible", cấm "exact/certain"; (2) Chỉ suy rộng cho ĐÚNG tổng thể nơi lấy mẫu ngẫu nhiên; (3) Tăng cỡ mẫu lên \(4\) lần thì Margin of Error <b>GIẢM một nửa</b> (\(\propto 1/\sqrt{n}\)).',
        {
            'A': ('Point-Estimate Certainty Trap', r'Tỉ lệ mẫu \(38\%\) chỉ là ước lượng điểm; không thể khẳng định "chính xác \(38\%\)" cho toàn tổng thể.'),
            'B': ('Đáp án đúng', r'Đúng khoảng tin cậy \(38\% \pm 4.7\% = [33.3\%, 42.7\%]\) và giới hạn đúng phạm vi \(12,000\) người trong registry.'),
            'C': ('Overgeneralization Beyond Sample Frame', r'Suy rộng quá phạm vi mẫu sang "all art conservators worldwide" dù chỉ lấy mẫu trong national registry.'),
            'D': ('Inverse Sample-Size Relationship Trap', r'Tăng cỡ mẫu gấp \(4\) lần (từ \(400\) lên \(1,600\)) làm biên sai số GIẢM đi \(\sqrt{4} = 2\) lần (xuống \(\approx 2.35\%\)), chứ không tăng gấp đôi!'),
        },
        desmos_tip_vi=r'Kiểm tra nhanh hai đầu khoảng tin cậy trên Desmos: <code>38 - 4.7 = 33.3</code> và <code>38 + 4.7 = 42.7</code>.'
    ))

    # Q19 — SPR (4) — Very Hard (780-800) — Median frequency optimization with even/odd trap (Biomechanics)
    tbl_q19 = build_math_table(
        ['40-Meter Split Time (seconds)', 'Number of Athletes'],
        [
            ['4.6', '5'],
            ['4.8', '8'],
            ['5.0', r'\(k\)'],
            ['5.2', '6'],
            ['5.4', '4'],
        ],
        caption='Sprint Split Times Recorded in Athletic Biomechanics Lab'
    )
    qs.append(math_spr(
        'sat_mm3_m2h_q19', 19, 'Problem-Solving and Data Analysis', 'Median & Order Statistics with Unknown Frequency', 'Hard',
        rf'<p>The frequency table below summarizes the 40-meter sprint split times of a track squad, where \(k\) is a positive integer.</p>{tbl_q19}',
        r'<p>What is the least possible integer value of \(k\) such that the median split time of the squad is \(5.0\) seconds?</p>',
        ['4'],
        '4',
        '\n'.join([
            r'Bước 1: Đếm số vận động viên nằm dưới và trên mức \(5.0\):',
            r'• Dưới \(5.0\) giây: \(5 + 8 = 13\) người (chiếm các vị trí xếp hạng từ \(1\) đến \(13\)).',
            r'• Đúng \(5.0\) giây: \(k\) người (chiếm các vị trí từ \(14\) đến \(13 + k\)).',
            r'• Trên \(5.0\) giây: \(6 + 4 = 10\) người (chiếm các vị trí từ \(14 + k\) đến \(23 + k\)).',
            r'Bước 2: Thử cẩn thận các giá trị nguyên nhỏ của \(k\) (tổng số người \(N = 23 + k\)):',
            r'• Với \(k = 3\): \(N = 26\) (chẵn) \(\Rightarrow\) trung vị là trung bình của vị trí \(13\) (giá trị \(4.8\)) và vị trí \(14\) (giá trị \(5.0\)), cho trung vị \(\frac{4.8 + 5.0}{2} = 4.9 \ne 5.0\)! (Loại!)',
            r'• Với \(k = 4\): \(N = 27\) (lẻ) \(\Rightarrow\) trung vị nằm đúng tại vị trí \(\frac{27 + 1}{2} = 14\), có giá trị đúng bằng \(5.0\)! (Nhận!)',
            r'Bước 3: Vậy giá trị nguyên dương nhỏ nhất của \(k\) là \(4\).',
        ]),
        r'Bẫy 790+ siêu kinh điển: muốn trung vị bằng \(5.0\), số phần tử \(\ge 5.0\) phải <b>LỚN HƠN HẲN</b> số phần tử \(< 5.0\) (\(k + 10 > 13 \Rightarrow k \ge 4\))! Nếu chỉ cho bằng nhau (\(k = 3\)), tổng \(N\) chẵn sẽ kéo trung vị thành trung bình cộng \(4.9\)!',
        desmos_tip_vi=r'Kiểm tra nhanh điều kiện lệch phía: bên trái có <code>5+8 = 13</code> người, bên phải có <code>6+4 = 10</code> người; cần <code>k + 10 > 13</code> nên <code>k > 3</code> \(\Rightarrow k_{\min} = 4\).'
    ))

    # =========================================================================
    # DOMAIN 4: GEOMETRY AND TRIGONOMETRY (Q20 - Q22)
    # =========================================================================

    # Q20 — MCQ (A) — Hard (760-800) — Circle sector area & arc length in radians (SVG)
    svg_q20 = svg_circle_sector(
        radius_lbl='r', angle_lbl='θ', center_lbl='O', pt_a='A', pt_b='B',
        note='Note: Figure not drawn to scale.'
    )
    qs.append(math_mcq(
        'sat_mm3_m2h_q20', 20, 'Geometry and Trigonometry', 'Circles, Arc Length & Sector Area (Radians)', 'Hard',
        rf'<div style="display:flex;justify-content:center;margin:8px 0 12px;">{svg_q20}</div><p>In the circle with center \(O\) shown above, the length of minor arc \(AB\) is \(5\pi\) centimeters, and the area of shaded sector \(AOB\) is \(30\pi\) square centimeters.</p>',
        r'<p>What is the radian measure of central angle \(\angle AOB\)?</p>',
        {
            'A': r'\(\frac{5\pi}{12}\)',
            'B': r'\(\frac{5\pi}{6}\)',
            'C': r'\(\frac{12\pi}{5}\)',
            'D': r'\(12\)',
        },
        'A',
        '\n'.join([
            r'Bước 1: Dùng hai công thức radian cho cung tròn và hình quạt: độ dài cung \(s = r\theta\) và diện tích hình quạt \(A = \frac{1}{2}r^2\theta = \frac{1}{2}r \cdot s\).',
            r'Bước 2: Thay \(s = 5\pi\) và \(A = 30\pi\) vào công thức rút gọn \(A = \frac{1}{2}rs\):',
            r'\[30\pi = \frac{1}{2}r(5\pi) \Rightarrow 60\pi = 5\pi r \Rightarrow r = 12\text{ cm}\]',
            r'Bước 3: Tìm góc ở tâm \(\theta\) theo radian: \(\theta = \frac{s}{r} = \frac{5\pi}{12}\).',
        ]),
        r'Công thức liên kết vàng \(A_{\text{sector}} = \frac{1}{2} r \cdot s\) giúp giải ngay bán kính \(r = \frac{2A}{s}\) chỉ trong một bước, sau đó suy ra \(\theta = \frac{s}{r}\).',
        {
            'A': ('Đáp án đúng', r'\(r = 12\) và \(\theta = \frac{5\pi}{12}\) radian (kiểm tra: \(A = \frac{1}{2}(144)\frac{5\pi}{12} = 30\pi\)).'),
            'B': ('Missing 1/2 Factor Trap', r'Quên hệ số \(\frac{1}{2}\) trong diện tích hình quạt, ra nhầm \(r = 6\) và \(\theta = \frac{5\pi}{6}\).'),
            'C': ('Inverted Formula', r'Chia ngược \(\frac{r}{s}\) thay vì \(\frac{s}{r}\) (hơn nữa \(\frac{12\pi}{5} > 2\pi\) vượt quá cả vòng tròn!).'),
            'D': ('Solved for Radius Instead of Angle', r'Dừng lại ở bán kính \(r = 12\) cm mà quên tính góc \(\theta\).'),
        },
        desmos_tip_vi=r'Lập hệ <code>r * t = 5*pi</code> và <code>0.5 * r^2 * t = 30*pi</code> (đổi thành <code>x, y</code>) trên Desmos → click giao điểm <code>(12, 1.309)</code> và kiểm tra <code>5*pi/12 = 1.309</code>!'
    ))

    # Q21 — MCQ (C) — Very Hard (780-800) — Altitude to hypotenuse, similar right triangles & trig (SVG)
    svg_q21 = svg_right_triangle(
        a_lbl='AB', b_lbl='BC', c_lbl='AC',
        v_top='A', v_right_angle='B', v_right='C',
        note='Note: Figure not drawn to scale.'
    )
    qs.append(math_mcq(
        'sat_mm3_m2h_q21', 21, 'Geometry and Trigonometry', 'Similar Right Triangles & Cofunction Trig', 'Hard',
        rf'<div style="display:flex;justify-content:center;margin:8px 0 12px;">{svg_q21}</div><p>In right triangle \(ABC\) with right angle at \(B\), an altitude is drawn from vertex \(B\) to point \(D\) on hypotenuse \(AC\) such that \(AD = 9\) and \(DC = 16\).</p>',
        r'<p>What is the value of \(\sin(\angle CBD) + \cos(\angle ABD)\)?</p>',
        {
            'A': r'\(\frac{6}{5}\)',
            'B': r'\(\frac{7}{5}\)',
            'C': r'\(\frac{8}{5}\)',
            'D': r'\(\frac{8}{3}\)',
        },
        'C',
        '\n'.join([
            r'Bước 1: Trong tam giác vuông \(ABC\) có đường cao \(BD \perp AC\), hai tam giác con \(\triangle ABD \sim \triangle BCD\) nên áp dụng hệ thức trung bình nhân:',
            r'\[BD^2 = AD \cdot DC = 9 \times 16 = 144 \Rightarrow BD = 12\]',
            r'Bước 2: Tính cạnh huyền hai tam giác vuông con:',
            r'• Trong \(\triangle BCD\) vuông tại \(D\): \(BC = \sqrt{BD^2 + DC^2} = \sqrt{12^2 + 16^2} = 20\). Suy ra \(\sin(\angle CBD) = \frac{DC}{BC} = \frac{16}{20} = \frac{4}{5}\).',
            r'• Trong \(\triangle ABD\) vuông tại \(D\): \(AB = \sqrt{AD^2 + BD^2} = \sqrt{9^2 + 12^2} = 15\). Suy ra \(\cos(\angle ABD) = \frac{BD}{AB} = \frac{12}{15} = \frac{4}{5}\).',
            r'(Phím tắt phụ nhau: vì \(\angle ABD + \angle CBD = 90^\circ\) nên \(\cos(\angle ABD) = \sin(\angle CBD) = \frac{4}{5}\) ngay lập tức!)',
            r'Bước 3: Cộng lại: \(\frac{4}{5} + \frac{4}{5} = \frac{8}{5}\).',
        ]),
        r'Kết hợp hai vũ khí 800 Geometry: đường cao ứng cạnh huyền \(h^2 = p \cdot q\) và đồng nhất thức góc phụ \(\cos(90^\circ - \theta) = \sin\theta\) để xử lý cực gọn mọi bài tam giác vuông lồng nhau!',
        {
            'A': ('Swapped Sine & Cosine', r'Tính nhầm \(\cos(\angle CBD) = \frac{3}{5}\) cho cả hai số hạng, ra \(\frac{3}{5} + \frac{3}{5} = \frac{6}{5}\).'),
            'B': ('Missed Cofunction Equality', r'Tính đúng một tỉ số \(\frac{4}{5}\) nhưng tính nhầm tỉ số kia là \(\frac{3}{5}\), cộng ra \(\frac{7}{5}\).'),
            'C': ('Đáp án đúng', r'\(\sin(\angle CBD) = \cos(\angle ABD) = \frac{4}{5}\), tổng bằng \(\frac{8}{5}\).'),
            'D': ('Used Tangent Instead of Sine/Cosine', r'Dùng tỉ số hai cạnh góc vuông \(\frac{16}{12} = \frac{4}{3}\) (tức \(\tan\)) cộng hai lần ra \(\frac{8}{3}\).'),
        },
        desmos_tip_vi=r'Tính <code>BD = sqrt(9*16) = 12</code>, <code>BC = sqrt(12^2 + 16^2) = 20</code>, <code>AB = sqrt(9^2 + 12^2) = 15</code> rồi bấm <code>16/20 + 12/15 = 1.6</code> (chuyển phân số ra <code>8/5</code>).'
    ))

    # Q22 — SPR (18) — Very Hard (790-800 Boss) — Cylindrical to Conical Reservoir Transfer & 3D Similarity
    svg_q22 = svg_cylinder(r_lbl='12 m', h_lbl='8 m', note='Cylindrical Reservoir (75% Full)')
    qs.append(math_spr(
        'sat_mm3_m2h_q22', 22, 'Geometry and Trigonometry', '3D Volumes & Similar Cones', 'Hard',
        rf'<div style="display:flex;justify-content:center;margin:8px 0 12px;">{svg_q22}</div><p>A municipal water facility stores treated water in a right circular cylindrical reservoir of radius \(12\) meters and height \(8\) meters that is initially filled to \(75\%\) of its total capacity. All of this water is then pumped into an empty inverted right circular conical holding basin (vertex pointing downward) with a top radius of \(18\) meters and a total depth of \(27\) meters.</p>',
        r'<p>After all the water has been transferred, what is the depth of the water, in meters, measured from the bottom vertex of the conical holding basin?</p>',
        ['18'],
        '18',
        '\n'.join([
            r'Bước 1: Tính thể tích nước chuyển từ bể trụ (đầy \(75\%\)):',
            r'\[V_{\text{nước}} = 0.75 \cdot \pi r^2 h = \frac{3}{4} \cdot \pi (12^2)(8) = 864\pi\text{ m}^3\]',
            r'Bước 2: Tính thể tích toàn phần của bể hình nón ngược (\(R = 18, H = 27\)):',
            r'\[V_{\text{nón}} = \frac{1}{3}\pi R^2 H = \frac{1}{3}\pi (18^2)(27) = 2,916\pi\text{ m}^3\]',
            r'Bước 3 (Kỹ thuật đồng dạng 3D 800 Math): Khối nước trong bể nón tạo thành một hình nón nhỏ đồng dạng với cả bể nón theo tỉ lệ chiều cao \(k = \frac{d}{27}\), do đó tỉ lệ thể tích là \(k^3\):',
            r'\[\left(\frac{d}{27}\right)^3 = \frac{V_{\text{nước}}}{V_{\text{nón}}} = \frac{864\pi}{2,916\pi} = \frac{8}{27}\]',
            r'Bước 4: Lấy căn bậc ba hai vế: \(\frac{d}{27} = \frac{2}{3} \Rightarrow d = 27 \times \frac{2}{3} = 18\) mét.',
        ]),
        r'Khi đổ nước vào hình nón ngược, thể tích khối nước tỉ lệ với <b>LẬP PHƯƠNG</b> độ sâu (\(V \propto d^3\))! Tỉ lệ thể tích \(\frac{8}{27}\) tương ứng tỉ lệ chiều cao \(\sqrt[3]{\frac{8}{27}} = \frac{2}{3}\).',
        desmos_tip_vi=r'Gõ thẳng phương trình tỉ lệ lập phương trên Desmos: <code>(x/27)^3 = (0.75 * 12^2 * 8) / ((1/3) * 18^2 * 27)</code> → đọc ngay đường thẳng đứng <code>x = 18</code>!'
    ))

    return qs


def verify_math():
    """Programmatic exact verification of all 22 Module 2 Hard answers."""
    # Q1: (5x-7)/3 - (2x+1)/6 = 11/2 => 8x - 10
    x1 = Fraction(48, 8)
    assert Fraction(5 * x1 - 7, 3) - Fraction(2 * x1 + 1, 6) == Fraction(11, 2)
    assert 8 * x1 - 10 == 38
    # Q2: g(x)+4 through (-2,11),(4,-7) => g(x) through (-2,7),(4,-11)
    m2 = Fraction(-11 - 7, 4 - (-2))
    b2 = 7 - m2 * (-2)
    x_int2 = Fraction(-b2, m2)
    assert m2 == -3 and b2 == 1 and x_int2 == Fraction(1, 3)
    # Q3: max 1400p + 4500s s.t. 6p+15s<=120, p+s>=11, p,s>=0 integers
    best = max(
        1400 * p + 4500 * s
        for p in range(25)
        for s in range(15)
        if 6 * p + 15 * s <= 120 and p + s >= 11
    )
    assert best == 34000
    # Q4: (2/5)x - (3/4)y = 1/2 and ax + by = -10 infinitely many solutions
    mult4 = Fraction(-10, Fraction(1, 2))
    a4 = mult4 * Fraction(2, 5)
    b4 = mult4 * Fraction(-3, 4)
    assert a4 == -8 and b4 == 15 and a4 + b4 == 7
    # Q5: 2|4x-9| - 5 = 19 => sum of solutions
    r5_1 = Fraction(9 + 12, 4)
    r5_2 = Fraction(9 - 12, 4)
    assert 2 * abs(4 * r5_1 - 9) - 5 == 19
    assert 2 * abs(4 * r5_2 - 9) - 5 == 19
    assert r5_1 + r5_2 == Fraction(9, 2)
    # Q6: y > (3/2)x + 4 and y < -(1/2)x + 4
    # Must satisfy x < 0; check QII (-2, 3) and QIII (-10, -5); no x > 0 possible
    assert 3 > Fraction(3, 2) * (-2) + 4 and 3 < Fraction(-1, 2) * (-2) + 4
    assert -5 > Fraction(3, 2) * (-10) + 4 and -5 < Fraction(-1, 2) * (-10) + 4
    for x_pos in [Fraction(1, 10), Fraction(1), Fraction(5)]:
        assert Fraction(3, 2) * x_pos + 4 > Fraction(-1, 2) * x_pos + 4
    # Q7: (p+1)x + 6y = 18 and 4x + (p-1)y = 12 infinitely many solutions
    p7 = 5
    assert Fraction(p7 + 1, 4) == Fraction(6, p7 - 1) == Fraction(18, 12)
    assert Fraction(-5 + 1, 4) == Fraction(6, -5 - 1) != Fraction(18, 12)
    # Q8: VA(t)=89-4t, VB(t)=64-2t, VA = 1.25 VB
    t8 = Fraction(89 - Fraction(5, 4) * 64, 4 - Fraction(5, 4) * 2)
    va8, vb8 = 89 - 4 * t8, 64 - 2 * t8
    assert t8 == 6 and va8 == 65 and vb8 == 52 and va8 == Fraction(5, 4) * vb8 and va8 + vb8 == 117
    # Q9: 3x^2 - 14x + k = 0, r^2 + s^2 = 100/9
    s9 = Fraction(14, 3)
    k9 = Fraction(3, 2) * (s9**2 - Fraction(100, 9))
    assert k9 == 16 and 14**2 - 4 * 3 * k9 > 0
    # Q10: (6x^2 - 5x - 10)/(2x - 3) = 3x + a + b/(2x - 3)
    a10 = Fraction(-5 + 9, 2)
    b10 = -10 + 3 * a10
    assert a10 == 2 and b10 == -4 and a10 - b10 == 6
    for xv in [Fraction(0), Fraction(1), Fraction(4)]:
        assert Fraction(6 * xv**2 - 5 * xv - 10, 2 * xv - 3) == 3 * xv + a10 + Fraction(b10, 2 * xv - 3)
    # Q11: 0.64^(t/30) == 0.80^(t/15)
    assert Fraction(80, 100)**2 == Fraction(64, 100)
    # Q12: x^2 + (6-m)x + 9 = 0 has Delta < 0 iff 0 < m < 12
    for mv in [1, 6, 11]:
        assert (6 - mv)**2 - 36 < 0
    for mv in [-1, 0, 12, 15]:
        assert (6 - mv)**2 - 36 >= 0
    # Q13: 2x - 9*sqrt(x) + 4 = 0
    u1, u2 = Fraction(1, 2), Fraction(4)
    x13_1, x13_2 = u1**2, u2**2
    assert 2 * x13_1 - 9 * u1 + 4 == 0 and 2 * x13_2 - 9 * u2 + 4 == 0
    assert x13_1 + x13_2 == Fraction(65, 4)
    # Q14: f(x) = a(x-2)(x-8)+5, f(0) = -27 => max f(5)
    a14 = Fraction(-27 - 5, (-2) * (-8))
    f5 = a14 * (5 - 2) * (5 - 8) + 5
    assert a14 == -2 and f5 == 23
    # Q15: P(x) = 2x^3 + kx^2 - 14x + m divisible by (x-2) and (2x+1)
    k15, m15 = 5, -8
    P = lambda x: 2 * x**3 + k15 * x**2 - 14 * x + m15
    assert P(2) == 0 and P(Fraction(-1, 2)) == 0 and k15 + m15 == -3
    # Q16: Line Beta vs Line Alpha usable silicon area per hour
    area_a = Fraction(100**2) * Fraction(80, 100) * 45
    area_b = Fraction(150**2) * Fraction(75, 100) * 32
    pct16 = Fraction(area_b - area_a, area_a) * 100
    assert pct16 == 50
    # Q17: Station P vs Station Q mean and variance
    vals = [-4, -2, 0, 2, 4]
    fp = [2, 5, 11, 5, 2]
    fq = [6, 4, 5, 4, 6]
    assert sum(fp) == 25 and sum(fq) == 25
    mean_p = Fraction(sum(v * f for v, f in zip(vals, fp)), 25)
    mean_q = Fraction(sum(v * f for v, f in zip(vals, fq)), 25)
    var_p = Fraction(sum(f * (v - mean_p)**2 for v, f in zip(vals, fp)), 25)
    var_q = Fraction(sum(f * (v - mean_q)**2 for v, f in zip(vals, fq)), 25)
    assert mean_p == mean_q == 0 and var_p < var_q
    # Q18: 38 +/- 4.7 => [33.3, 42.7]
    assert Fraction(38) - Fraction(47, 10) == Fraction(333, 10)
    assert Fraction(38) + Fraction(47, 10) == Fraction(427, 10)
    # Q19: least integer k so median is 5.0
    def median_for_k(k):
        arr = [Fraction(46, 10)] * 5 + [Fraction(48, 10)] * 8 + [Fraction(50, 10)] * k + [Fraction(52, 10)] * 6 + [Fraction(54, 10)] * 4
        n = len(arr)
        return arr[n // 2] if n % 2 == 1 else (arr[n // 2 - 1] + arr[n // 2]) / 2
    assert median_for_k(1) == Fraction(48, 10)
    assert median_for_k(2) == Fraction(48, 10)
    assert median_for_k(3) == Fraction(49, 10)
    assert median_for_k(4) == Fraction(50, 10)
    # Q20: s = 5*pi, A = 30*pi => r = 12, theta = 5*pi/12
    r20 = Fraction(2 * 30, 5)
    theta20_over_pi = Fraction(5, r20)
    assert r20 == 12 and theta20_over_pi == Fraction(5, 12)
    # Q21: AD=9, DC=16 => BD=12, AB=15, BC=20 => sin(CBD)+cos(ABD)
    bd = int(math.isqrt(9 * 16))
    ab = int(math.isqrt(9**2 + bd**2))
    bc = int(math.isqrt(16**2 + bd**2))
    assert bd == 12 and ab == 15 and bc == 20
    assert Fraction(16, bc) + Fraction(bd, ab) == Fraction(8, 5)
    # Q22: cylinder r=12, h=8 at 75% into inverted cone R=18, H=27 => d = 18
    v_water_over_pi = Fraction(3, 4) * (12**2) * 8
    v_cone_over_pi = Fraction(1, 3) * (18**2) * 27
    ratio22 = Fraction(v_water_over_pi, v_cone_over_pi)
    assert ratio22 == Fraction(8, 27)
    d22 = 27 * Fraction(2, 3)
    assert d22 == 18 and (d22 / 27)**3 == ratio22


if __name__ == '__main__':
    verify_math()
    qs = get_m2h_questions()
    print(f"M2H OK: {len(qs)} Qs verified.")
