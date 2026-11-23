# -*- coding: utf-8 -*-
"""
Digital SAT Math Adaptive Mock Test #1 — Module 2 Hard (650–800 Band, 22 Questions)
Themes: Renewable Energy/Solar, Robotics/Microchips, Oceanography, Botanical Architecture, Shipping Logistics.
Blueprint: 8 Algebra (Q1-Q8), 7 Advanced Math (Q9-Q15), 4 PSDA (Q16-Q19), 3 Geometry/Trig (Q20-Q22).
Format: 16 MCQ (A:4, B:4, C:4, D:4) + 6 SPR (Q5, Q9, Q13, Q16, Q19, Q22).
"""

from fractions import Fraction
import math
from sat_math_helpers import (
    math_mcq, math_spr, build_math_table,
    svg_similar_triangles, svg_cylinder
)

def verify_math():
    # Q1: (a/3)x - 4y = 12, 5x - by = 36 inf many solutions => scale=3 => b=12, a/3=5/3 => a=5 => a+b=17
    assert Fraction(36, 12) == 3 and 4 * 3 == 12 and Fraction(5, Fraction(5, 3)) == 3 and 5 + 12 == 17
    # Q2: f(x)+6 has (2,13), (5,25), (9,41) => f has (2,7), (5,19), (9,35) => m=4, b=-1 => x-int = 1/4
    for x, y in [(2, 7), (5, 19), (9, 35)]:
        assert 4 * x - 1 == y
    assert 4 * Fraction(1, 4) - 1 == 0
    # Q3: kx+4y=12 perp to 6x-9y=5 (m=2/3, perp=-3/2) => -k/4 = -3/2 => k=6
    assert Fraction(-6, 4) * Fraction(6, 9) == -1
    # Q4: p(4x-3)+q = 12x+7 for all x => p=3, q=16 => p+q=19
    assert 4 * 3 == 12 and -3 * 3 + 16 == 7 and 3 + 16 == 19
    # Q5: y <= -4x+29 and y <= 3x+8 => x=3, y_max=17
    assert -4 * 3 + 29 == 3 * 3 + 8 == 17
    # Q6: y > 2x+5 and y > -3x+2 => intersection (-3/5, 19/5), y_min > 3.8 > 0 => Q-III & Q-IV empty
    x6 = Fraction(-3, 5)
    y6 = 2 * x6 + 5
    assert y6 == -3 * x6 + 2 == Fraction(19, 5) > 0
    assert (10 > 2 * 1 + 5 and 10 > -3 * 1 + 2)  # Q-I has solution (1, 10)
    assert (10 > 2 * (-1) + 5 and 10 > -3 * (-1) + 2)  # Q-II has solution (-1, 10)
    # Q7: h(t+4)-h(t)=-14 => m=-7/2, h(6)=5 => h(0)=5 - (-7/2)*6 = 26
    assert 5 - Fraction(-14, 4) * 6 == 26
    # Q8: 3x-7 > 5x+9 => x < -8 => max int x = -9 => 3(-9)+2 = -25
    assert 3 * (-9) - 7 > 5 * (-9) + 9 and not (3 * (-8) - 7 > 5 * (-8) + 9) and 3 * (-9) + 2 == -25
    # Q9: y = x^2-6x+14 and y = 2x+k tangent => x^2-8x+(14-k)=0 => 64-4(14-k)=0 => k=-2
    assert (-8) ** 2 - 4 * 1 * (14 - (-2)) == 0
    # Q10: f(x) = 32 * 2^(x-3) + 7 => f(0) = 32/8 + 7 = 11
    assert Fraction(32, 8) + 7 == 11
    # Q11: p(x) = 2x^3 - 5x^2 + kx - 12 div by (x-3) => 54-45+3k-12=0 => k=1 => p(-1)=-20
    assert 2 * 27 - 5 * 9 + 1 * 3 - 12 == 0 and 2 * (-1) - 5 * 1 + 1 * (-1) - 12 == -20
    # Q12: 2x^2 - (k+8)x + 3k = 0, product=12 => 3k/2=12 => k=8, D=256-192=64>0, sum=16/2=8
    assert Fraction(3 * 8, 2) == 12 and 16 ** 2 - 4 * 2 * 24 > 0 and Fraction(16, 2) == 8
    # Q13: x - 6/(x-3) = (7x-27)/(x-3) => x=7 valid, x=3 extraneous
    assert Fraction(7) - Fraction(6, 4) == Fraction(7 * 7 - 27, 4)
    # Q14: 4x^2-12x+c=0 no real sol => 144-16c<0 => c>9 => min int 10
    assert 144 - 16 * 10 < 0 and 144 - 16 * 9 == 0
    # Q15: (1.06)^2 = 1.1236 => 12.36%
    assert Fraction(106, 100) ** 2 == Fraction(11236, 10000)
    # Q16: 54 ft^3/min -> yd^3/hr = (54/27)*60 = 120
    assert Fraction(54, 27) * 60 == 120
    # Q17: 1.60 * 0.75 = 1.20 => 20% greater
    assert Fraction(160, 100) * Fraction(75, 100) == Fraction(120, 100)
    # Q19: 7*445 - 6*420 = 595
    assert 7 * 445 - 6 * 420 == 595
    # Q20: 2x^2+2y^2-20x+12y+18=0 => (x-5)^2+(y+3)^2=25 => r=5 => d=10
    assert -9 + 25 + 9 == 25 and 2 * int(math.sqrt(25)) == 10
    # Q21: AB=16, BC=30 => AC=34 => cos(F)=cos(C)=30/34=15/17
    assert 16 ** 2 + 30 ** 2 == 34 ** 2 and Fraction(30, 34) == Fraction(15, 17)
    # Q22: SA ratio 720/80=9 => k=3 => V_B = 64 * 27 = 1728
    assert Fraction(720, 80) == 9 and 64 * (3 ** 3) == 1728

def get_m2h_questions():
    tbl_q2 = build_math_table(
        ['\\(x\\)', '\\(f(x) + 6\\)'],
        [['2', '13'], ['5', '25'], ['9', '41']],
        caption='Shifted Linear Function Table'
    )
    svg_q21 = svg_similar_triangles('16', '30', '40', 'EF', 'A', 'B', 'C', 'D', 'E', 'F')
    svg_q22 = svg_cylinder('r', 'h', note='Similar Cylindrical Tanks A and B')

    return [
        math_mcq(
            'sat_mm1_m2h_q1', 1, 'Algebra', 'Systems of two linear equations in two variables', 'Hard',
            r'<p>In the system of equations below, \(a\) and \(b\) are constants:</p><p style="text-align:center;">\[\begin{cases} \frac{a}{3}x - 4y = 12 \\ 5x - by = 36 \end{cases}\]</p>',
            r'If the system has <b>infinitely many solutions</b>, what is the value of \(a + b\)?',
            {'A': r'\(11\)', 'B': r'\(15\)', 'C': r'\(17\)', 'D': r'\(27\)'},
            'C',
            r'Để hệ có vô số nghiệm, phương trình thứ hai phải là bội số của phương trình thứ nhất. So hằng số tự do: \(\frac{36}{12} = 3\). Suy ra: \(-b = 3(-4) \Rightarrow b = 12\), và \(5 = 3 \cdot \left(\frac{a}{3}\right) \Rightarrow a = 5\). Vậy \(a + b = 5 + 12 = 17\).',
            r'Với hệ vô số nghiệm, luôn bắt đầu từ tỉ số cặp hệ số đã biết (ở đây \(36/12 = 3\)) rồi nhân tỉ số đó cho 2 cặp còn lại!',
            {
                'A': ('Nhầm chia 3 ở a', r'Tính nhầm \(a = 5/3\) hoặc trừ sai dấu.'),
                'B': ('Tính sai a = 3', r'Nhầm \(\frac{a}{3} \cdot 3 = 3a\) thay vì \(a\).'),
                'C': ('Đáp án đúng', r'\(a = 5, b = 12 \Rightarrow a + b = 17\).'),
                'D': ('Nhân 3 thêm lần nữa cho a', r'Lấy \(a = 15\) thay vì \(5\), ra \(15 + 12 = 27\).'),
            },
            r'Gõ `(a/3)x - 4y = 12` và `5x - by = 36` trên Desmos, thêm sliders `a, b` → khi `a = 5, b = 12` hai đường trùng khít làm một!'
        ),
        math_mcq(
            'sat_mm1_m2h_q2', 2, 'Algebra', 'Linear functions', 'Hard',
            tbl_q2 + r'<p>The table above shows three pairs of values for \(x\) and \(f(x) + 6\), where \(f\) is a linear function.</p>',
            r'What is the \(x\)-intercept of the graph of \(y = f(x)\) in the \(xy\)-plane?',
            {'A': r'\(\left(\frac{1}{4}, 0\right)\)', 'B': r'\(\left(-\frac{5}{4}, 0\right)\)', 'C': r'\((0, -1)\)', 'D': r'\((4, 0)\)'},
            'A',
            r'Khôi phục giá trị thực của \(f(x)\) bằng cách trừ \(6\) ở cột phải: \((2, 7)\), \((5, 19)\), \((9, 35)\). Hệ số góc \(m = \frac{19 - 7}{5 - 2} = 4\). Suy ra \(f(x) = 4(x - 2) + 7 = 4x - 1\). Cho \(f(x) = 0 \Rightarrow 4x - 1 = 0 \Rightarrow x = \frac{1}{4}\).',
            r'Gặp bảng cho \(f(x) + c\), luôn trừ \(c\) để khôi phục đúng \(f(x)\) trước khi tính giao điểm trục Ox (\(f(x) = 0\))!',
            {
                'A': ('Đáp án đúng', r'\(f(x) = 4x - 1 = 0 \Rightarrow x = \frac{1}{4}\).'),
                'B': ('Quên trừ 6 ở cột phải', r'Lập phương trình \(y = 4x + 5 = 0 \Rightarrow x = -\frac{5}{4}\) (sai vì đây là \(f(x)+6\)).'),
                'C': ('Bẫy y-intercept thay vì x-intercept', r'\((0, -1)\) là tung độ gốc (y-intercept), đề hỏi x-intercept!'),
                'D': ('Nghịch đảo nhầm', r'Nhầm \(4x - 1 = 0\) thành \(x = 4\).'),
            },
            r'Nhập Table `x1 = [2, 5, 9]`, `y1 = [7, 19, 35]` → gõ `y1 ~ m x1 + b` → bấm giao điểm trục Ox trên đồ thị `y = 4x - 1` đọc ngay `(0.25, 0)`!'
        ),
        math_mcq(
            'sat_mm1_m2h_q3', 3, 'Algebra', 'Linear equations in two variables', 'Medium-Hard',
            r'<p>In the \(xy\)-plane, the line \(kx + 4y = 12\) is perpendicular to the line \(6x - 9y = 5\), where \(k\) is a constant.</p>',
            r'What is the value of \(k\)?',
            {'A': r'\(-\frac{8}{3}\)', 'B': r'\(-6\)', 'C': r'\(\frac{8}{3}\)', 'D': r'\(6\)'},
            'D',
            r'Hệ số góc đường thứ hai: \(m_2 = -\frac{6}{-9} = \frac{2}{3}\). Đường vuông góc phải có hệ số góc \(m_1 = -\frac{3}{2}\). Đường thứ nhất có \(m_1 = -\frac{k}{4} \Rightarrow -\frac{k}{4} = -\frac{3}{2} \Rightarrow k = 6\).',
            r'Mẹo Standard Form: hai đường \(A_1x + B_1y = C_1\) và \(A_2x + B_2y = C_2\) vuông góc \(\Leftrightarrow A_1A_2 + B_1B_2 = 0\) (\(6k + 4(-9) = 0 \Rightarrow k = 6\) trong 2 giây!).',
            {
                'A': ('Song song thay vì vuông góc', r'Giải \(-\frac{k}{4} = \frac{2}{3} \Rightarrow k = -\frac{8}{3}\).'),
                'B': ('Sai dấu âm', r'Quên dấu trừ ở công thức \(m = -A/B\).'),
                'C': ('Sai cả song song và dấu', r'Giải nhầm \(\frac{k}{4} = \frac{2}{3}\).'),
                'D': ('Đáp án đúng', r'\(6k - 36 = 0 \Rightarrow k = 6\).'),
            },
            r'Dùng công thức tích vô hướng `A1*A2 + B1*B2 = 0`: `6k - 36 = 0` → `k = 6`; kiểm chứng bằng cách vẽ cả hai đường trên Desmos.'
        ),
        math_mcq(
            'sat_mm1_m2h_q4', 4, 'Algebra', 'Linear equations in one variable', 'Medium-Hard',
            r'<p>In the equation below, \(p\) and \(q\) are constants:</p><p style="text-align:center;">\[p(4x - 3) + q = 12x + 7\]</p>',
            r'If the equation is true for <b>all real values of \(x\)</b>, what is the value of \(p + q\)?',
            {'A': r'\(13\)', 'B': r'\(19\)', 'C': r'\(10\)', 'D': r'\(22\)'},
            'B',
            r'Khai triển vế trái: \(4px + (q - 3p) = 12x + 7\). Để phương trình đúng với mọi \(x\), hệ số của \(x\) và hằng số tự do hai vế phải bằng nhau: \(4p = 12 \Rightarrow p = 3\), và \(q - 3(3) = 7 \Rightarrow q = 16\). Vậy \(p + q = 3 + 16 = 19\).',
            r'Phương trình bậc nhất đúng với mọi \(x\) \(\Leftrightarrow\) hệ số \(x\) bằng nhau VÀ hằng số tự do bằng nhau.',
            {
                'A': ('Cộng thay vì trừ 3p', r'Giải nhầm \(q + 9 = 7 \Rightarrow q = -2\), hoặc sai phép cộng.'),
                'B': ('Đáp án đúng', r'\(p = 3, q = 16 \Rightarrow p + q = 19\).'),
                'C': ('Quên nhân p vào -3', r'Viết nhầm \(q - 3 = 7 \Rightarrow q = 10\) rồi cộng sai.'),
                'D': ('Nhân sai hệ số', r'Nhầm \(4p = 12 \Rightarrow p = 4\) hoặc cộng nhầm.'),
            },
            r'Kiểm tra nhanh bằng cách thay \(x = 0\) và \(x = 1\) vào phương trình gốc để giải hệ 2 ẩn \(p, q\).'
        ),
        math_spr(
            'sat_mm1_m2h_q5', 5, 'Algebra', 'Linear inequalities in one or two variables', 'Hard',
            r'<p>In the \(xy\)-plane, a point \((a, b)\) satisfies both inequalities in the system below:</p><p style="text-align:center;">\[\begin{cases} y \le -4x + 29 \\ y \le 3x + 8 \end{cases}\]</p>',
            r'What is the <b>maximum</b> possible value of \(b\)?',
            ['17'], '17',
            r'Vì cả hai đường thẳng đều chặn phía trên của \(y\) (một đường slope âm \(-4\), một đường slope dương \(+3\)), giá trị lớn nhất của tung độ \(b\) nằm đúng tại đỉnh giao điểm hai đường biên: \(-4x + 29 = 3x + 8 \Rightarrow 7x = 21 \Rightarrow x = 3 \Rightarrow b_{\max} = 3(3) + 8 = 17\).',
            r'Áp dụng Corner-Point Rule: cực đại của \(y\) khi bị chặn bởi hai bất phương trình \(y \le\) ngược chiều slope luôn đạt tại giao điểm hai đường biên!',
            r'Gõ thẳng `y <= -4x + 29` và `y <= 3x + 8` vào Desmos → bấm vào đỉnh nhọn cao nhất của vùng tô đậm đọc ngay `(3, 17)` → `b_max = 17`!'
        ),
        math_mcq(
            'sat_mm1_m2h_q6', 6, 'Algebra', 'Linear inequalities in one or two variables', 'Hard',
            r'<p>Consider the system of linear inequalities in the \(xy\)-plane:</p><p style="text-align:center;">\[\begin{cases} y > 2x + 5 \\ y > -3x + 2 \end{cases}\]</p>',
            r'Which quadrants of the \(xy\)-plane contain <b>no solutions</b> to this system?',
            {'A': r'Quadrants III and IV', 'B': r'Quadrant IV only', 'C': r'Quadrant III only', 'D': r'Quadrants II and III'},
            'A',
            r'Tìm giao điểm 2 đường biên: \(2x + 5 = -3x + 2 \Rightarrow 5x = -3 \Rightarrow x = -0.6\), và \(y = 2(-0.6) + 5 = 3.8\). Vì cả hai bất phương trình đều lấy phần <b>phía trên</b> hai đường (một đường dốc lên, một đường dốc xuống), mọi điểm nghiệm \((x, y)\) đều phải thỏa \(y > 3.8 > 0\)! Do đó toàn bộ nửa mặt phẳng dưới (\(y < 0\), tức cả <b>Góc phần tư III và IV</b>) KHÔNG chứa bất kỳ nghiệm nào (trong khi Q-I chứa \((1, 10)\) và Q-II chứa \((-1, 10)\)).',
            r'Khi cả hai bất phương trình đều có dạng \(y >\) (ngược chiều slope) và đỉnh giao nhau có tung độ dương (\(y = 3.8 > 0\)), toàn bộ phần \(y < 0\) (Quadrants III & IV) chắc chắn vô nghiệm!',
            {
                'A': ('Đáp án đúng', r'Mọi nghiệm đều có \(y > 3.8 > 0\), nên cả Quadrant III và Quadrant IV đều không có nghiệm.'),
                'B': ('Bỏ sót Quadrant III', r'Tại Quadrant III (\(x < 0, y < 0\)), ta có \(-3x + 2 > 2 > 0 > y\) nên bất phương trình thứ 2 cũng bị vi phạm.'),
                'C': ('Bỏ sót Quadrant IV', r'Tại Quadrant IV (\(x > 0, y < 0\)), bất phương trình đầu cho \(2x + 5 > 5 > 0 > y\) cũng vô nghiệm.'),
                'D': ('Loại nhầm Quadrant II', r'Điểm \((-1, 10)\) thuộc Quadrant II thỏa mãn cả \(10 > 3\) và \(10 > 5\).'),
            },
            r'Gõ thẳng `y > 2x + 5` và `y > -3x + 2` lên Desmos → vùng tô đậm nằm hoàn toàn phía trên trục Ox (`y > 3.8`) → nhìn bằng mắt 2 giây thấy ngay Q-III và Q-IV trống hoàn toàn!'
        ),
        math_mcq(
            'sat_mm1_m2h_q7', 7, 'Algebra', 'Linear functions', 'Hard',
            r'<p>A linear function \(h\) satisfies \(h(t + 4) - h(t) = -14\) for all real numbers \(t\). It is also given that \(h(6) = 5\).</p>',
            r'What is the value of \(h(0)\)?',
            {'A': r'\(-16\)', 'B': r'\(19\)', 'C': r'\(21\)', 'D': r'\(26\)'},
            'D',
            r'Vì \(h\) là hàm bậc nhất nên tốc độ thay đổi là hằng số: \(m = \frac{h(t + 4) - h(t)}{4} = \frac{-14}{4} = -3.5\). Ta có \(h(t) = -3.5t + b\). Thay \(h(6) = 5\): \(-3.5(6) + b = 5 \Rightarrow -21 + b = 5 \Rightarrow b = 26\). Vậy \(h(0) = 26\).',
            r'Với hàm tuyến tính, \(h(t + \Delta t) - h(t) = m \cdot \Delta t\), nhớ chia cho \(\Delta t = 4\) để tìm đúng slope \(m\)!',
            {
                'A': ('Đảo dấu slope', r'Tính nhầm \(5 - 21 = -16\) thay vì \(5 + 21 = 26\).'),
                'B': ('Quên chia 4 ở bước nhảy', r'Cộng trực tiếp \(5 + 14 = 19\).'),
                'C': ('Quên cộng h(6) = 5', r'Chỉ tính \(3.5 \times 6 = 21\) mà quên cộng thêm \(5\).'),
                'D': ('Đáp án đúng', r'\(m = -3.5 \Rightarrow h(0) = 5 - (-3.5)(6) = 26\).'),
            },
            r'Gõ `h(x) = -3.5(x - 6) + 5` vào Desmos rồi đọc ngay giao điểm trục Oy `(0, 26)`!'
        ),
        math_mcq(
            'sat_mm1_m2h_q8', 8, 'Algebra', 'Linear inequalities in one or two variables', 'Hard',
            r'<p>An integer \(x\) satisfies the inequality \(3x - 7 > 5x + 9\).</p>',
            r'What is the <b>greatest</b> possible value of \(3x + 2\)?',
            {'A': r'\(-22\)', 'B': r'\(-25\)', 'C': r'\(-28\)', 'D': r'\(-19\)'},
            'B',
            r'Giải bất phương trình: \(3x - 5x > 9 + 7 \Rightarrow -2x > 16 \Rightarrow x < -8\) (nhớ đảo chiều dấu khi chia cho \(-2\)!). Vì \(x\) là số nguyên nghiêm ngặt nhỏ hơn \(-8\), giá trị lớn nhất của \(x\) là \(-9\). Khi đó giá trị lớn nhất của \(3x + 2\) là \(3(-9) + 2 = -25\).',
            r'Bất đẳng thức nghiêm ngặt \(x < -8\) với \(x\) nguyên có giá trị lớn nhất là \(-9\) (KHÔNG lấy \(-8\), và cẩn thận \(-9 < -8\), không phải \(-7\)!).',
            {
                'A': ('Bẫy lấy dấu bằng x = -8', r'Thay \(x = -8\) ra \(-22\), nhưng dấu là \(>\) nghiêm ngặt nên không nhận \(-8\).'),
                'B': ('Đáp án đúng', r'\(x \le -9 \Rightarrow (3x + 2)_{\max} = 3(-9) + 2 = -25\).'),
                'C': ('Chọn x = -10', r'Không phải giá trị nguyên lớn nhất.'),
                'D': ('Nhầm hướng số âm (-7)', r'Tưởng \(-7 < -8\) nên thay \(x = -7\) ra \(-19\).'),
            },
            r'Gõ `3x - 7 > 5x + 9` vào Desmos để thấy miền tô nằm hoàn toàn bên trái đường nét đứt `x = -8` → số nguyên lớn nhất là `-9` → `3(-9) + 2 = -25`.'
        ),
        math_spr(
            'sat_mm1_m2h_q9', 9, 'Advanced Math', 'Nonlinear equations in one variable and systems of equations in two variables', 'Hard',
            r'<p>In the \(xy\)-plane, the line \(y = 2x + k\) intersects the parabola \(y = x^2 - 6x + 14\) at <b>exactly one point</b>, where \(k\) is a constant.</p>',
            r'What is the value of \(k\)?',
            ['-2'], '-2',
            r'Phương trình hoành độ giao điểm: \(x^2 - 6x + 14 = 2x + k \Rightarrow x^2 - 8x + (14 - k) = 0\). Để cắt tại đúng 1 điểm (tiếp xúc), biệt thức \(\Delta = (-8)^2 - 4(1)(14 - k) = 0 \Rightarrow 64 - 56 + 4k = 0 \Rightarrow 4k = -8 \Rightarrow k = -2\).',
            r'Hệ đường thẳng + parabol có đúng 1 nghiệm \(\Leftrightarrow\) phương trình hoành độ giao điểm có \(\Delta = 0\)!',
            r'Gõ `y = x^2 - 6x + 14` và `y = 2x + k` trên Desmos, kéo slider `k` đến `-2` sẽ thấy đường thẳng tiếp xúc parabol tại đúng 1 điểm `(4, 6)`!'
        ),
        math_mcq(
            'sat_mm1_m2h_q10', 10, 'Advanced Math', 'Nonlinear functions', 'Hard',
            r'<p>The exponential function \(f\) is defined by:</p><p style="text-align:center;">\[f(x) = 32 \cdot 2^{x - 3} + 7\]</p>',
            r'What is the \(y\)-intercept of the graph of \(y = f(x)\) in the \(xy\)-plane?',
            {'A': r'\((0, 4)\)', 'B': r'\((0, 7)\)', 'C': r'\((0, 11)\)', 'D': r'\((0, 39)\)'},
            'C',
            r'Tung độ gốc là giá trị tại \(x = 0\): \(f(0) = 32 \cdot 2^{0 - 3} + 7 = 32 \cdot \frac{1}{8} + 7 = 4 + 7 = 11\). Vậy \(y\)-intercept là \((0, 11)\).',
            r'Khi hàm mũ vừa có số mũ dịch chuyển \((x - 3)\) vừa có hằng số cộng \(+7\), LUÔN thay trực tiếp \(x = 0\) để không bị lừa đọc số 32 hay 7!',
            {
                'A': ('Quên cộng +7', r'Tính \(32 \cdot 2^{-3} = 4\) mà bỏ quên hằng số dịch chuyển \(+7\).'),
                'B': ('Nhầm với tiệm cận ngang', r'\(y = 7\) là đường tiệm cận ngang (horizontal asymptote), không phải y-intercept.'),
                'C': ('Đáp án đúng', r'\(f(0) = 4 + 7 = 11 \Rightarrow (0, 11)\).'),
                'D': ('Bỏ qua số mũ -3', r'Nhầm \(2^{0-3} = 1\) nên tính \(32 + 7 = 39\).'),
            },
            r'Gõ `y = 32 * 2^(x - 3) + 7` trên Desmos rồi bấm thẳng vào giao điểm trục Oy đọc ngay `(0, 11)`!'
        ),
        math_mcq(
            'sat_mm1_m2h_q11', 11, 'Advanced Math', 'Nonlinear functions', 'Hard',
            r'<p>The polynomial \(p(x) = 2x^3 - 5x^2 + kx - 12\), where \(k\) is a constant, is divisible by \((x - 3)\).</p>',
            r'What is the value of \(p(-1)\)?',
            {'A': r'\(-20\)', 'B': r'\(-18\)', 'C': r'\(1\)', 'D': r'\(-6\)'},
            'A',
            r'Theo Định lý Nhân tử, \(p(x)\) chia hết cho \((x - 3) \Leftrightarrow p(3) = 0\). Thay \(x = 3\): \(2(27) - 5(9) + 3k - 12 = 54 - 45 - 12 + 3k = 3k - 3 = 0 \Rightarrow k = 1\). Khi đó \(p(x) = 2x^3 - 5x^2 + x - 12 \Rightarrow p(-1) = 2(-1) - 5(1) + (-1) - 12 = -20\).',
            r'Cẩn thận câu hỏi 2 bước: sau khi dùng \(p(3) = 0\) tìm ra \(k = 1\), phải thay ngược lại để tính \(p(-1)\)!',
            {
                'A': ('Đáp án đúng', r'\(k = 1 \Rightarrow p(-1) = -2 - 5 - 1 - 12 = -20\).'),
                'B': ('Sai dấu k(-1)', r'Tính nhầm \(+1\) thay vì \(-1\) ở số hạng \(kx\).'),
                'C': ('Bẫy dừng ở k', r'\(1\) mới là giá trị của \(k\), chưa tính \(p(-1)\).'),
                'D': ('Sai dấu (-1)^3 và (-1)^2', r'Nhầm \((-1)^2 = -1\) khiến tổng sai thành \(-6\).'),
            },
            r'Gõ `p(x) = 2x^3 - 5x^2 + kx - 12`, tìm `k` sao cho `p(3) = 0` (`k = 1`), rồi gõ `p(-1)` ra ngay `-20`.'
        ),
        math_mcq(
            'sat_mm1_m2h_q12', 12, 'Advanced Math', 'Nonlinear equations in one variable and systems of equations in two variables', 'Hard',
            r'<p>In the quadratic equation \(2x^2 - (k + 8)x + 3k = 0\), where \(k\) is a constant, the <b>product</b> of the two real solutions is \(12\).</p>',
            r'What is the <b>sum</b> of the two solutions to this equation?',
            {'A': r'\(4\)', 'B': r'\(6\)', 'C': r'\(16\)', 'D': r'\(8\)'},
            'D',
            r'Theo định lý Vieta, tích hai nghiệm là \(\frac{c}{a} = \frac{3k}{2} = 12 \Rightarrow k = 8\). Kiểm tra lại: phương trình thành \(2x^2 - 16x + 24 = 0 \Leftrightarrow 2(x - 2)(x - 6) = 0\) (có 2 nghiệm thực \(2\) và \(6\)). Tổng hai nghiệm là \(-\frac{b}{a} = \frac{k + 8}{2} = \frac{16}{2} = 8\).',
            r'Khi \(a \neq 1\), cả hai công thức Vieta (Tổng \(-b/a\) và Tích \(c/a\)) đều PHẢI chia cho hệ số \(a\)!',
            {
                'A': ('Quên chia 2 ở tích', r'Giải \(3k = 12 \Rightarrow k = 4\), tính nhầm tổng.'),
                'B': ('Nhầm tính nghiệm lớn nhất', r'6 chỉ là một nghiệm, không phải tổng 2 nghiệm.'),
                'C': ('Quên chia a = 2 ở tổng', r'Lấy \(k + 8 = 16\) mà quên chia cho \(a = 2\).'),
                'D': ('Đáp án đúng', r'\(k = 8 \Rightarrow \text{Tổng} = \frac{8 + 8}{2} = 8\).'),
            },
            r'Tìm `k = 8` từ `3k/2 = 12`, sau đó vẽ `y = 2x^2 - 16x + 24` trên Desmos thấy 2 nghiệm `2` và `6` → tổng bằng `8`!'
        ),
        math_spr(
            'sat_mm1_m2h_q13', 13, 'Advanced Math', 'Nonlinear equations in one variable and systems of equations in two variables', 'Hard',
            r'<p>Consider the rational equation below:</p><p style="text-align:center;">\[x - \frac{6}{x - 3} = \frac{7x - 27}{x - 3}\]</p>',
            r'What is the valid real solution \(x\) to the given equation?',
            ['7'], '7',
            r'Điều kiện mẫu khác 0: \(x \neq 3\). Nhân hai vế với \((x - 3)\): \(x(x - 3) - 6 = 7x - 27 \Rightarrow x^2 - 3x - 6 = 7x - 27 \Rightarrow x^2 - 10x + 21 = 0 \Rightarrow (x - 3)(x - 7) = 0\). Vì \(x = 3\) làm mẫu số bằng 0 (nghiệm ngoại lai, LOẠI!), nghiệm hợp lệ duy nhất là \(x = 7\).',
            r'Luôn kiểm tra nghiệm tìm được với mẫu số gốc — trên Hard M2, 1 trong 2 nghiệm bậc hai gần như chắc chắn là nghiệm ngoại lai!',
            r'Vẽ `y = x - 6/(x - 3)` và `y = (7x - 27)/(x - 3)` trên Desmos → chỉ có ĐÚNG 1 giao điểm tại `(7, 5.5)` → `x = 7`!'
        ),
        math_mcq(
            'sat_mm1_m2h_q14', 14, 'Advanced Math', 'Nonlinear equations in one variable and systems of equations in two variables', 'Hard',
            r'<p>The quadratic equation \(4x^2 - 12x + c = 0\), where \(c\) is an integer constant, has <b>no real solutions</b>.</p>',
            r'What is the <b>least</b> possible value of \(c\)?',
            {'A': r'\(9\)', 'B': r'\(10\)', 'C': r'\(11\)', 'D': r'\(37\)'},
            'B',
            r'Phương trình vô nghiệm thực \(\Leftrightarrow \Delta = b^2 - 4ac < 0 \Rightarrow (-12)^2 - 4(4)(c) < 0 \Rightarrow 144 - 16c < 0 \Rightarrow c > 9\). Vì \(c\) là số nguyên lớn hơn hẳn 9, giá trị nguyên nhỏ nhất là \(10\).',
            r'Với bất đẳng thức nghiêm ngặt \(c > 9\), tại \(c = 9\) phương trình có ĐÚNG 1 nghiệm kép — giá trị nguyên nhỏ nhất để VÔ NGHIỆM là \(10\)!',
            {
                'A': ('Bẫy dấu bằng Δ = 0', r'Tại \(c = 9\), phương trình có 1 nghiệm thực \(x = 1.5\), không phải vô nghiệm.'),
                'B': ('Đáp án đúng', r'\(c > 9 \Rightarrow c_{\min} = 10\).'),
                'C': ('Lớn hơn mức tối thiểu', r'\(c = 11\) cũng vô nghiệm nhưng chưa phải giá trị nhỏ nhất.'),
                'D': ('Quên nhân hệ số a = 4', r'Giải nhầm \(144 - 4c < 0 \Rightarrow c > 36 \Rightarrow 37\).'),
            },
            r'Gõ `y = 4x^2 - 12x + c` vào Desmos, đặt slider nguyên cho `c` → tại `c = 9` parabol chạm Ox, vừa tăng lên `c = 10` parabol tách hẳn lên trên!'
        ),
        math_mcq(
            'sat_mm1_m2h_q15', 15, 'Advanced Math', 'Equivalent expressions', 'Hard',
            r'<p>A solar energy storage fund models its value \(V(t)\), in dollars, after \(t\) years by the equation:</p><p style="text-align:center;">\[V(t) = 12{,}000(1.06)^{2t}\]</p>',
            r'According to the model, by what percent does the value of the fund increase each <b>year</b>?',
            {'A': r'\(6\%\)', 'B': r'\(12\%\)', 'C': r'\(12.36\%\)', 'D': r'\(36\%\)'},
            'C',
            r'Viết lại theo số mũ \(t\) (chu kỳ 1 năm): \(V(t) = 12{,}000\left((1.06)^2\right)^t = 12{,}000(1.1236)^t\). Hệ số tăng trưởng mỗi năm là \(1.1236 = 1 + 0.1236\), tương đương tăng \(12.36\%\) mỗi năm!',
            r'Đổi cơ số từ bán niên (\(2t\)) sang năm (\(t\)): luôn tính \((1 + r)^2\), KHÔNG nhân tuyến tính \(2 \times r\)!',
            {
                'A': ('Bẫy bỏ quên số 2 trên mũ', r'6% là mức tăng mỗi NỬA năm, không phải mỗi năm.'),
                'B': ('Bẫy nhân tuyến tính 2 × 6%', r'Lãi kép \((1.06)^2 = 1.1236\), lớn hơn 12% đơn giản.'),
                'C': ('Đáp án đúng', r'\((1.06)^2 - 1 = 0.1236 = 12.36\%\).'),
                'D': ('Bình phương sai 0.06', r'Nhầm \((1.06)^2\) thành \(1.36\).'),
            },
            r'Gõ `(1.06^2 - 1) * 100` trên Desmos ra ngay `12.36`!'
        ),
        math_spr(
            'sat_mm1_m2h_q16', 16, 'Problem-Solving and Data Analysis', 'Ratios, rates, proportional relationships, and units', 'Hard',
            r'<p>A coastal desalination pump transfers seawater at a constant rate of \(54\) cubic feet per minute. (\(1\text{ yard} = 3\text{ feet}\))</p>',
            r'What is this transfer rate, in <b>cubic yards per hour</b>?',
            ['120'], '120',
            r'Đổi 2 đơn vị cùng lúc: \(1\text{ yd}^3 = 3^3 = 27\text{ ft}^3\), và \(1\text{ giờ} = 60\text{ phút}\). Vậy tốc độ là: \(\frac{54\text{ ft}^3}{\text{min}} \times \frac{1\text{ yd}^3}{27\text{ ft}^3} \times \frac{60\text{ min}}{1\text{ hr}} = 2 \times 60 = 120\text{ yd}^3/\text{hr}\).',
            r'Luôn lập phương hệ số đổi đơn vị thể tích (\(3^3 = 27\)) rồi nhân 60 để chuyển từ mỗi phút sang mỗi giờ!',
            r'Gõ `(54 / 3^3) * 60` trên Desmos ra ngay `120`.'
        ),
        math_mcq(
            'sat_mm1_m2h_q17', 17, 'Problem-Solving and Data Analysis', 'Percentages', 'Hard',
            r'<p>For three positive quantities \(a\), \(b\), and \(c\), it is given that \(a\) is \(60\%\) <b>greater than</b> \(b\), and \(b\) is \(25\%\) <b>less than</b> \(c\).</p>',
            r'Which of the following accurately describes the relationship between \(a\) and \(c\)?',
            {
                'A': r'\(a\) is \(20\%\) greater than \(c\).',
                'B': r'\(a\) is \(35\%\) greater than \(c\).',
                'C': r'\(a\) is \(15\%\) less than \(c\).',
                'D': r'\(a\) is \(80\%\) of \(c\).',
            },
            'A',
            r'Đặt \(c = 100\). Vì \(b\) nhỏ hơn \(c\) 25%: \(b = (1 - 0.25)(100) = 75\). Vì \(a\) lớn hơn \(b\) 60%: \(a = (1 + 0.60)(75) = 1.60 \times 75 = 120\). So với \(c = 100\), \(a = 120\) tức \(a\) <b>lớn hơn \(c\) 20%</b>!',
            r'Nhân liên tiếp các hệ số \((1 + 0.60)(1 - 0.25) = 1.20\) — tuyệt đối không trừ thẳng \(60\% - 25\% = 35\%\)!',
            {
                'A': ('Đáp án đúng', r'\(1.60 \times 0.75 = 1.20 \Rightarrow\) lớn hơn 20%.'),
                'B': ('Bẫy trừ thẳng %', r'Lấy \(60\% - 25\% = 35\%\) — sai bản chất phần trăm kép.'),
                'C': ('Nhầm 60% of b', r'Lấy \(0.60 \times 0.75 = 0.45\) thay vì \(1.60 \times 0.75\).'),
                'D': ('Nhầm đảo ngược', r'Nhầm \(1.20\) với \(0.80\).'),
            },
            r'Gõ `1.60 * 0.75` trên Desmos ra `1.2` → tăng 20%.'
        ),
        math_mcq(
            'sat_mm1_m2h_q18', 18, 'Problem-Solving and Data Analysis', 'Inference from sample statistics and margin of error', 'Medium-Hard',
            r'<p>A logistics researcher randomly selected \(400\) marine engineers employed at Pacific Ports Corporation and asked whether they supported adopting autonomous tugboats. Of those surveyed, \(68\%\) answered yes, with an associated margin of error of \(4.5\%\).</p>',
            r'Which of the following is the most appropriate conclusion based on this survey?',
            {
                'A': r'Exactly \(68\%\) of all marine engineers at Pacific Ports Corporation support adopting autonomous tugboats.',
                'B': r'It is plausible that between \(63.5\%\) and \(72.5\%\) of all marine engineers worldwide support adopting autonomous tugboats.',
                'C': r'It is plausible that between \(63.5\%\) and \(72.5\%\) of all marine engineers at Pacific Ports Corporation support adopting autonomous tugboats.',
                'D': r'At least \(68\%\) of all marine engineers at Pacific Ports Corporation support adopting autonomous tugboats.',
            },
            'C',
            r'Khoảng hợp lý (plausible interval) là \(68\% \pm 4.5\% = [63.5\%, 72.5\%]\). Do mẫu được chọn ngẫu nhiên từ các kỹ sư của <b>Pacific Ports Corporation</b>, kết luận CHỈ được suy rộng cho đúng quần thể công ty đó (không suy rộng ra toàn thế giới) và phải dùng ngôn ngữ "plausible" (không khẳng định tuyệt đối "exactly" hay "at least 68%").',
            r'Ba tiêu chuẩn chọn đáp án Margin of Error: (1) dùng từ "plausible", (2) khoảng \(\hat{p} \pm \text{ME}\), và (3) đúng phạm vi quần thể lấy mẫu!',
            {
                'A': ('Khẳng định quá tuyệt đối', r'Mẫu không thể khẳng định "exactly 68%" cho tổng thể.'),
                'B': ('Suy rộng quá phạm vi mẫu', r'Chỉ lấy mẫu trong Pacific Ports Corp nên không suy rộng ra "worldwide".'),
                'C': ('Đáp án đúng', r'Đúng khoảng \([63.5\%, 72.5\%]\), dùng từ "plausible", đúng quần thể công ty.'),
                'D': ('Sai biên dưới của khoảng', r'Tỉ lệ thực có thể nằm dưới 68% (xuống tới 63.5%).'),
            },
            r'Tính biên khoảng `68 - 4.5 = 63.5` và `68 + 4.5 = 72.5` rồi soi kỹ phạm vi quần thể!'
        ),
        math_spr(
            'sat_mm1_m2h_q19', 19, 'Problem-Solving and Data Analysis', 'One-variable data: Distributions and measures of center and spread', 'Medium-Hard',
            r'<p>Six solar farms in a regional grid have a mean daily energy output of \(420\) megawatt-hours (MWh). After a seventh solar farm is connected to the grid, the mean daily output of all seven farms increases to \(445\) MWh.</p>',
            r'What is the daily energy output, in MWh, of the seventh solar farm?',
            ['595'], '595',
            r'Tổng sản lượng của 6 trạm đầu: \(6 \times 420 = 2{,}520\text{ MWh}\). Tổng sản lượng của cả 7 trạm: \(7 \times 445 = 3{,}115\text{ MWh}\). Sản lượng trạm thứ 7 là: \(3{,}115 - 2{,}520 = 595\text{ MWh}\).',
            r'Mọi bài Mean thêm/bớt phần tử đều quy về \(\text{Sum} = \text{Mean} \times n\)! (Mẹo nhanh: \(445 + 6 \times 25 = 595\)).',
            r'Gõ `7 * 445 - 6 * 420` trên Desmos ra ngay `595`.'
        ),
        math_mcq(
            'sat_mm1_m2h_q20', 20, 'Geometry and Trigonometry', 'Circles', 'Hard',
            r'<p>In the \(xy\)-plane, a circle is defined by the equation:</p><p style="text-align:center;">\[2x^2 + 2y^2 - 20x + 12y + 18 = 0\]</p>',
            r'What is the <b>diameter</b> of this circle?',
            {'A': r'\(5\)', 'B': r'\(10\)', 'C': r'\(25\)', 'D': r'\(50\)'},
            'B',
            r'Bước 1: Chia cả hai vế cho hệ số 2: \(x^2 + y^2 - 10x + 6y = -9\). Bước 2: Hoàn thành bình phương: \((x - 5)^2 + (y + 3)^2 = -9 + 25 + 9 = 25\). Suy ra bán kính \(r = \sqrt{25} = 5\). Bước 3: Đề hỏi <b>đường kính (diameter)</b> \(= 2r = 10\)!',
            r'Hai bẫy kép Hard M2 trong 1 câu: (1) phải chia hệ số \(2\) trước khi hoàn thành bình phương, và (2) đề hỏi DIAMETER (\(2r\)) chứ không phải radius (\(r\))!',
            {
                'A': ('Bẫy bán kính thay vì đường kính', r'5 là bán kính \(r\), đề yêu cầu tìm đường kính \(d = 2r = 10\).'),
                'B': ('Đáp án đúng', r'\(r = 5 \Rightarrow d = 2(5) = 10\).'),
                'C': ('Quên lấy căn r²', r'25 là \(r^2\), không phải đường kính.'),
                'D': ('Nhân đôi r²', r'Lấy \(2 \times 25 = 50\) thay vì \(2 \times \sqrt{25}\).'),
            },
            r'Gõ nguyên phương trình `2x^2 + 2y^2 - 20x + 12y + 18 = 0` vào Desmos → bấm đỉnh trên `(5, 2)` và đáy `(5, -8)` → đường kính là `2 - (-8) = 10`!'
        ),
        math_mcq(
            'sat_mm1_m2h_q21', 21, 'Geometry and Trigonometry', 'Right triangles and trigonometry', 'Hard',
            svg_q21 + r'<p>In the figure above, right triangle \(ABC\) is similar to right triangle \(DEF\), where \(\angle B = \angle E = 90^\circ\) and vertices \(A, B, C\) correspond to \(D, E, F\), respectively. It is given that \(AB = 16\), \(BC = 30\), and \(DE = 40\).</p>',
            r'What is the value of \(\cos(F)\)?',
            {'A': r'\(\frac{8}{17}\)', 'B': r'\(\frac{8}{15}\)', 'C': r'\(\frac{15}{8}\)', 'D': r'\(\frac{15}{17}\)'},
            'D',
            r'Vì \(\triangle ABC \sim \triangle DEF\), góc \(\angle F = \angle C\) nên \(\cos(F) = \cos(C)\) (tỉ số lượng giác bất biến theo đồng dạng — hoàn toàn không cần tính cạnh của \(\triangle DEF\)!). Trong \(\triangle ABC\), cạnh huyền \(AC = \sqrt{16^2 + 30^2} = \sqrt{1156} = 34\) (bộ \(8\text{–}15\text{–}17\) nhân 2). Vậy \(\cos(F) = \cos(C) = \frac{BC}{AC} = \frac{30}{34} = \frac{15}{17}\).',
            r'Tam giác đồng dạng có \(\sin, \cos, \tan\) các góc tương ứng BẰNG NHAU TUYỆT ĐỐI — đừng phí thời gian nhân tỉ lệ cạnh \(DE = 40\)!',
            {
                'A': ('Nhầm sin(F) với cos(F)', r'\(\frac{16}{34} = \frac{8}{17}\) là \(\sin(F)\), không phải \(\cos(F)\).'),
                'B': ('Nhầm tan(F)', r'\(\frac{16}{30} = \frac{8}{15}\) là \(\tan(F)\).'),
                'C': ('Nhầm cot(F)', r'\(\frac{30}{16} = \frac{15}{8} > 1\), không thể là giá trị của \(\cos\).'),
                'D': ('Đáp án đúng', r'\(\cos(F) = \cos(C) = \frac{30}{34} = \frac{15}{17}\).'),
            },
            r'Tính cạnh huyền `sqrt(16^2 + 30^2) = 34` trên Desmos, sau đó bấm `30/34` đổi phân số ra `15/17`.'
        ),
        math_spr(
            'sat_mm1_m2h_q22', 22, 'Geometry and Trigonometry', 'Area and volume', 'Hard',
            svg_q22 + r'<p>Two similar right circular cylindrical water tanks, Tank A and Tank B, have total surface areas of \(80\pi\text{ m}^2\) and \(720\pi\text{ m}^2\), respectively. The volume of Tank A is \(64\pi\text{ m}^3\).</p>',
            r'If the volume of Tank B is \(v\pi\text{ m}^3\), what is the value of \(v\)?',
            ['1728'], '1728',
            r'Hai hình trụ đồng dạng có tỉ số diện tích toàn phần là \(k^2 = \frac{720\pi}{80\pi} = 9 \Rightarrow\) tỉ số tuyến tính (bán kính & chiều cao) là \(k = \sqrt{9} = 3\). Do đó tỉ số thể tích là \(k^3 = 3^3 = 27\). Thể tích Tank B: \(V_B = 64\pi \times 27 = 1{,}728\pi \Rightarrow v = 1{,}728\).',
            r'Bậc thang 3D: Tỉ số Diện tích \(k^2 \xrightarrow{\sqrt{\cdot}} k \xrightarrow{(\cdot)^3} \text{Tỉ số Thể tích } k^3\)!',
            r'Gõ `64 * (sqrt(720 / 80))^3` trên Desmos ra ngay `1728`!'
        ),
    ]
