# -*- coding: utf-8 -*-
"""
Digital SAT Math Adaptive Mock Test #5 — Module 2 Hard (650–800 Band, 22 Questions)
Themes: Wind Turbines & Tidal Power Grids, Optical Lens Labs, Specialty Coffee Roasting, Alpine Suspension Bridges, Glass Atrium Architecture.
Blueprint: 8 Algebra (Q1-Q8), 7 Advanced Math (Q9-Q15), 4 PSDA (Q16-Q19), 3 Geometry/Trig (Q20-Q22).
Format: 16 MCQ (A:4, B:4, C:4, D:4) + 6 SPR (Q5, Q9, Q13, Q16, Q19, Q22).
"""

from fractions import Fraction
import math
from sat_math_helpers import (
    math_mcq, math_spr, build_math_table,
    svg_circle_sector, svg_cylinder
)

def verify_math():
    assert Fraction(Fraction(27, 4), 9) == Fraction(6, 8) and Fraction(15, 25) != Fraction(6, 8)
    for x, y in [(1, 7), (4, 25), (7, 43)]:
        fx = Fraction(y + 3, 2)
        assert fx == 3 * x + 2
    assert 3 * (-5) + 2 == -13
    assert 5 * 12 + 4 * (-15) == 0
    assert 3 * 5 + 8 == 23 and -2 * 3 == -6 and 3 * 8 == 24
    assert -3 * 4 + 26 == 2 * 4 + 6 == 14
    assert -2 * 1 - 4 == 3 * 1 - 9 == -6
    assert (-30 < -2 * (-5) - 4 and -30 < 3 * (-5) - 9)  # Q-III valid
    assert (-30 < -2 * 5 - 4 and -30 < 3 * 5 - 9)        # Q-IV valid
    assert 41 - Fraction(18, 5) * 10 == 5
    assert 4 * 9 + 11 < 7 * 9 - 13 and not (4 * 8 + 11 < 7 * 8 - 13) and 5 * 9 - 3 == 42
    assert (-12) ** 2 - 4 * 2 * (11 - (-7)) == 0
    assert Fraction(81, 9) - 5 == 4
    assert 2 ** 3 + (-1) * 4 - 5 * 2 + 6 == 0
    assert (-3) ** 3 + (-1) * 9 - 5 * (-3) + 6 == -15
    assert Fraction(2 * 15 + 3, 3) == 11 and 33 ** 2 - 4 * 3 * 90 > 0 and Fraction(6 * 15, 3) == 30
    assert 9 + Fraction(15, 4) == Fraction(9 * 9 - 30, 4)
    assert (-20) ** 2 - 4 * 5 * 19 > 0 and (-20) ** 2 - 4 * 5 * 20 == 0
    assert Fraction(1, 2) == Fraction(12, 24)
    assert Fraction(81, 27) * 60 == 180
    assert Fraction(225, 100) * Fraction(80, 100) == Fraction(180, 100)
    assert Fraction(8 * 52 + 12 * 67, 20) == 61
    assert 11 + 16 + 9 == 36 and int(math.sqrt(36)) == 6 and Fraction(6 * 2, 3) == 4
    assert 3 * 12 + 12 + 2 * 12 + 18 == 90 and 5 * 12 == 60
    assert Fraction(1458, 54) == 27 and 45 * (3 ** 2) == 405

def get_m2h_questions():
    tbl_q2 = build_math_table(
        ['\\(x\\)', '\\(2f(x) - 3\\)'],
        [['1', '7'], ['4', '25'], ['7', '43']],
        caption='Transformed Linear Function Values'
    )
    svg_q20 = svg_circle_sector('r = 6', '2π/3 rad', note='Arc length s = rθ')
    svg_q22 = svg_cylinder('r', 'h', note='Similar Cones / 3D Solids Scaling (k : k² : k³)')

    return [
        math_mcq(
            'sat_mm5_m2h_q1', 1, 'Algebra', 'Systems of two linear equations in two variables', 'Hard',
            r'<p>In the system of linear equations below, \(k\) is a constant:</p><p style="text-align:center;">\[\begin{cases} \frac{k}{4}x + 6y = 15 \\ 9x + 8y = 25 \end{cases}\]</p>',
            r'If the system has <b>no solution</b>, what is the value of \(k\)?',
            {'A': r'\(\frac{27}{4}\)', 'B': r'\(27\)', 'C': r'\(48\)', 'D': r'\(12\)'},
            'B',
            r'Hệ vô nghiệm khi hai đường song song: \(\frac{k/4}{9} = \frac{6}{8} = \frac{3}{4} \Rightarrow \frac{k}{36} = \frac{3}{4} \Rightarrow k = 27\). Kiểm tra tỉ lệ hằng số: \(\frac{15}{25} = \frac{3}{5} \neq \frac{3}{4}\) (đúng vô nghiệm!).',
            r'Đặt tỉ số \(\frac{a_1}{a_2} = \frac{b_1}{b_2}\), cẩn thận phân số tầng \(\frac{k/4}{9} = \frac{k}{36}\)!',
            {
                'A': ('Quên nhân 4 ở mẫu', r'Chỉ giải \(\frac{k}{9} = \frac{3}{4}\) mà quên số 4 ở \(\frac{k}{4}\).'),
                'B': ('Đáp án đúng', r'\(\frac{k}{36} = \frac{3}{4} \Rightarrow k = 27\).'),
                'C': ('Đảo tỉ lệ 8/6', r'Giải \(\frac{k}{36} = \frac{4}{3} \Rightarrow k = 48\).'),
                'D': ('Chia nhầm 4 thay vì nhân 4', r'Tính sai phân số tầng.'),
            },
            r'Gõ `(k/4)x + 6y = 15` và `9x + 8y = 25` lên Desmos (slider `k` từ 0 đến 50) → hai đường song song chính xác tại `k = 27`.'
        ),
        math_mcq(
            'sat_mm5_m2h_q2', 2, 'Algebra', 'Linear functions', 'Hard',
            tbl_q2 + r'<p>The table above shows values of \(2f(x) - 3\) for selected values of \(x\), where \(f\) is a linear function.</p>',
            r'What is the value of \(f(-5)\)?',
            {'A': r'\(-29\)', 'B': r'\(-17\)', 'C': r'\(-13\)', 'D': r'\(-10\)'},
            'C',
            r'Khôi phục \(f(x) = \frac{(2f(x) - 3) + 3}{2}\): tại \(x = 1 \Rightarrow f(1) = 5\); tại \(x = 4 \Rightarrow f(4) = 14\); tại \(x = 7 \Rightarrow f(7) = 23\). Slope \(m = \frac{14 - 5}{4 - 1} = 3\), \(f(x) = 3x + 2\). Vậy \(f(-5) = 3(-5) + 2 = -13\).',
            r'Gặp bảng cho \(af(x) + c\), luôn khôi phục cột \(f(x)\) thực trước rồi mới tính slope và thay điểm!',
            {
                'A': ('Dùng thẳng cột 2f(x) - 3', r'Tính \(6(-5) + 1 = -29\) trên hàm bị nhân đôi.'),
                'B': ('Trừ 3 thay vì cộng 3 khi khôi phục', r'Nhầm \(f(x) = (y - 3)/2\).'),
                'C': ('Đáp án đúng', r'\(f(x) = 3x + 2 \Rightarrow f(-5) = -13\).'),
                'D': ('Quên cộng tung độ gốc +2', r'Lấy gần sai hoặc sai dấu \(+2\).'),
            },
            r'Nhập Table `x1=[1,4,7]`, `y1=[5,14,23]` trên Desmos → `y1 ~ m x1 + b` → `m=3, b=2` → `3(-5)+2 = -13`.'
        ),
        math_mcq(
            'sat_mm5_m2h_q3', 3, 'Algebra', 'Linear equations in two variables', 'Medium-Hard',
            r'<p>In the \(xy\)-plane, the line \(5x + ky = 18\) is perpendicular to the line \(12x - 15y = 7\), where \(k\) is a constant.</p>',
            r'What is the value of \(k\)?',
            {'A': r'\(4\)', 'B': r'\(-4\)', 'C': r'\(-\frac{25}{4}\)', 'D': r'\(\frac{25}{4}\)'},
            'A',
            r'Dùng quy tắc vuông góc Standard Form \(A_1A_2 + B_1B_2 = 0\): \(5(12) + k(-15) = 0 \Rightarrow 60 - 15k = 0 \Rightarrow k = 4\).',
            r'Hai đường \(A_1x + B_1y = C_1\) và \(A_2x + B_2y = C_2\) vuông góc \(\Leftrightarrow A_1A_2 + B_1B_2 = 0\)!',
            {
                'A': ('Đáp án đúng', r'\(60 - 15k = 0 \Rightarrow k = 4\).'),
                'B': ('Sai dấu âm', r'Quên dấu trừ ở \(-15y\).'),
                'C': ('Song song thay vì vuông góc', r'Giải \(-\frac{5}{k} = \frac{12}{15} \Rightarrow k = -\frac{25}{4}\).'),
                'D': ('Song song + sai dấu', r'Giải \(\frac{5}{k} = \frac{4}{5}\).'),
            },
            r'Gõ `5x + 4y = 18` và `12x - 15y = 7` trên Desmos thấy ngay góc cắt \(90^\circ\) hoàn hảo.'
        ),
        math_mcq(
            'sat_mm5_m2h_q4', 4, 'Algebra', 'Linear equations in one variable', 'Hard',
            r'<p>In the equation below, \(a\) and \(b\) are constants:</p><p style="text-align:center;">\[a(5x - 2) + bx = 23x - 6\]</p>',
            r'If the equation holds for all real numbers \(x\), what is the value of \(ab\)?',
            {'A': r'\(11\)', 'B': r'\(15\)', 'C': r'\(18\)', 'D': r'\(24\)'},
            'D',
            r'Thu gọn vế trái: \((5a + b)x - 2a = 23x - 6\). Đồng nhất hệ số: \(-2a = -6 \Rightarrow a = 3\), và \(5(3) + b = 23 \Rightarrow b = 8\). Tích \(ab = 3 \times 8 = 24\).',
            r'Đồng nhất hằng số tự do trước (\(-2a = -6 \Rightarrow a = 3\)) sẽ mở khóa ngay ẩn còn lại \(b\)!',
            {
                'A': ('Tính tổng a + b', r'\(3 + 8 = 11\), đề yêu cầu tích \(ab\).'),
                'B': ('Nhầm tính 5a', r'15 là \(5a\), chưa nhân \(a\) với \(b\).'),
                'C': ('Nhầm a = 3, b = 6', r'Trừ nhầm \(23 - 15\).'),
                'D': ('Đáp án đúng', r'\(a = 3, b = 8 \Rightarrow ab = 24\).'),
            },
            r'Thay `x = 0` tìm ngay `a = 3`; thay `x = 1` tìm `b = 8`; tính `3 * 8 = 24`.'
        ),
        math_spr(
            'sat_mm5_m2h_q5', 5, 'Algebra', 'Linear inequalities in one or two variables', 'Hard',
            r'<p>In the \(xy\)-plane, every point \((x, y)\) in a feasible region satisfies both inequalities below:</p><p style="text-align:center;">\[\begin{cases} y \ge -3x + 26 \\ y \ge 2x + 6 \end{cases}\]</p>',
            r'What is the <b>minimum</b> possible value of \(y\)?',
            ['14'], '14',
            r'Vì cả hai đường chặn phía DƯỚI của \(y\) với hai slope ngược dấu (\(-3\) và \(+2\)), giá trị nhỏ nhất của \(y\) đạt đúng tại đỉnh giao điểm hai đường biên: \(-3x + 26 = 2x + 6 \Rightarrow 5x = 20 \Rightarrow x = 4 \Rightarrow y_{\min} = 2(4) + 6 = 14\).',
            r'Corner-Point Rule: cực tiểu của \(y\) trong hệ hai bất phương trình \(y \ge\) ngược chiều slope nằm đúng tại giao điểm hai đường biên!',
            r'Gõ `y >= -3x + 26` và `y >= 2x + 6` trên Desmos → bấm đỉnh đáy của vùng tô đậm đọc ngay `(4, 14)` → `y_min = 14`!'
        ),
        math_mcq(
            'sat_mm5_m2h_q6', 6, 'Algebra', 'Linear inequalities in one or two variables', 'Hard',
            r'<p>Consider the system of linear inequalities in the \(xy\)-plane:</p><p style="text-align:center;">\[\begin{cases} y < -2x - 4 \\ y < 3x - 9 \end{cases}\]</p>',
            r'Which quadrants of the \(xy\)-plane contain <b>no solutions</b> to this system?',
            {'A': r'Quadrants I and II', 'B': r'Quadrant I only', 'C': r'Quadrant II only', 'D': r'Quadrants I and IV'},
            'A',
            r'Giao điểm hai đường biên: \(-2x - 4 = 3x - 9 \Rightarrow 5x = 5 \Rightarrow x = 1, y = -6\). Do cả hai bất phương trình lấy phần <b>phía dưới</b> hai đường ngược chiều slope, mọi điểm nghiệm đều có \(y < -6 < 0\). Do đó toàn bộ nửa trên trục Ox (<b>Quadrants I và II</b>) hoàn toàn không có nghiệm! (Q-III có \((-5, -30)\) và Q-IV có \((5, -30)\)).',
            r'Đỉnh cao nhất của miền nghiệm ở \((1, -6)\) nằm dưới trục Ox → cả Q-I và Q-II đều không có nghiệm!',
            {
                'A': ('Đáp án đúng', r'Mọi nghiệm đều có \(y < -6 < 0\), nên Q-I và Q-II đều trống.'),
                'B': ('Bỏ sót Quadrant II', r'Tại Q-II (\(x < 0, y > 0\)), bất phương trình hai đòi \(y < 3x - 9 < -9 < 0\), mâu thuẫn.'),
                'C': ('Bỏ sót Quadrant I', r'Tại Q-I (\(x > 0, y > 0\)), bất phương trình đầu đòi \(y < -2x - 4 < -4 < 0\), mâu thuẫn.'),
                'D': ('Loại nhầm Quadrant IV', r'Điểm \((5, -30)\) ở Q-IV thỏa mãn cả hai bất phương trình.'),
            },
            r'Gõ `y < -2x - 4` và `y < 3x - 9` vào Desmos → vùng tô đậm nằm hoàn toàn bên dưới `y = -6`, Q-I & Q-II hoàn toàn trống!'
        ),
        math_mcq(
            'sat_mm5_m2h_q7', 7, 'Algebra', 'Linear functions', 'Hard',
            r'<p>A linear function \(g\) satisfies \(g(t + 5) - g(t) = 18\) for all real numbers \(t\). If \(g(10) = 41\), what is the value of \(g(0)\)?</p>',
            r'Choose the exact value of \(g(0)\).',
            {'A': r'\(-139\)', 'B': r'\(5\)', 'C': r'\(23\)', 'D': r'\(77\)'},
            'B',
            r'Hệ số góc \(m = \frac{18}{5} = 3.6\). Suy ra \(g(10) = g(0) + 10(3.6) \Rightarrow 41 = g(0) + 36 \Rightarrow g(0) = 5\). (Hoặc dùng bước nhảy đôi: 2 bước 5 đơn vị tăng \(2 \times 18 = 36 \Rightarrow 41 - 36 = 5\)).',
            r'Mẹo bước nhảy: từ \(t = 0\) lên \(t = 10\) gồm đúng 2 bước \(\Delta t = 5\), nên \(g(10) - g(0) = 2 \times 18 = 36 \Rightarrow g(0) = 5\)!',
            {
                'A': ('Quên chia 5 cho slope', r'Tính \(41 - 18(10) = -139\).'),
                'B': ('Đáp án đúng', r'\(41 - 36 = 5\).'),
                'C': ('Chỉ trừ 1 bước 18', r'Tính \(41 - 18 = 23\) (đó là \(g(5)\), không phải \(g(0)\)!).'),
                'D': ('Cộng thay vì trừ 36', r'Tính \(41 + 36 = 77\) (đó là \(g(20)\)).'),
            },
            r'Gõ `g(x) = (18/5)(x - 10) + 41` trên Desmos rồi gõ `g(0)` ra ngay `5`!'
        ),
        math_mcq(
            'sat_mm5_m2h_q8', 8, 'Algebra', 'Linear inequalities in one or two variables', 'Hard',
            r'<p>An integer \(x\) satisfies the strict inequality \(4x + 11 < 7x - 13\).</p>',
            r'What is the <b>least</b> possible value of \(5x - 3\)?',
            {'A': r'\(37\)', 'B': r'\(39\)', 'C': r'\(45\)', 'D': r'\(42\)'},
            'D',
            r'Giải bất phương trình: \(11 + 13 < 7x - 4x \Rightarrow 24 < 3x \Rightarrow x > 8\). Vì \(x\) là số nguyên nghiêm ngặt lớn hơn 8, giá trị nhỏ nhất của \(x\) là \(9\). Do đó \((5x - 3)_{\min} = 5(9) - 3 = 42\).',
            r'Bất đẳng thức nghiêm ngặt \(x > 8\) với \(x\) nguyên có giá trị nhỏ nhất là \(9\), không lấy \(8\)!',
            {
                'A': ('Bẫy lấy dấu bằng x = 8', r'\(5(8) - 3 = 37\), vi phạm dấu `<` nghiêm ngặt.'),
                'B': ('Tính sai phép trừ', r'Sai số học đơn giản.'),
                'C': ('Cộng 3 thay vì trừ 3', r'Tính \(5(9) + 3 = 48\) hoặc nhầm số.'),
                'D': ('Đáp án đúng', r'\(x_{\min} = 9 \Rightarrow 5(9) - 3 = 42\).'),
            },
            r'Gõ `4x + 11 < 7x - 13` trên Desmos → biên nét đứt `x = 8` → chọn nguyên nhỏ nhất `x = 9` → `5(9) - 3 = 42`.'
        ),
        math_spr(
            'sat_mm5_m2h_q9', 9, 'Advanced Math', 'Nonlinear equations in one variable and systems of equations in two variables', 'Hard',
            r'<p>In the \(xy\)-plane, the line \(y = 4x + k\) is tangent to (intersects at exactly one point) the parabola \(y = 2x^2 - 8x + 11\), where \(k\) is a constant.</p>',
            r'What is the value of \(k\)?',
            ['-7'], '-7',
            r'Phương trình hoành độ giao điểm: \(2x^2 - 8x + 11 = 4x + k \Rightarrow 2x^2 - 12x + (11 - k) = 0\). Điều kiện tiếp xúc \(\Delta = 0\): \((-12)^2 - 4(2)(11 - k) = 0 \Rightarrow 144 - 88 + 8k = 0 \Rightarrow 8k = -56 \Rightarrow k = -7\).',
            r'Tiếp xúc giữa đường thẳng và parabol \(\Leftrightarrow \Delta = 0\) của phương trình hiệu hai hàm!',
            r'Vẽ `y = 2x^2 - 8x + 11` và `y = 4x + k` trên Desmos → kéo slider `k` tới `-7` sẽ thấy tiếp xúc tại `(3, 5)`!'
        ),
        math_mcq(
            'sat_mm5_m2h_q10', 10, 'Advanced Math', 'Nonlinear functions', 'Hard',
            r'<p>The exponential function \(f\) is defined by:</p><p style="text-align:center;">\[f(x) = 81 \cdot 3^{x - 2} - 5\]</p>',
            r'What is the \(y\)-intercept of the graph of \(y = f(x)\) in the \(xy\)-plane?',
            {'A': r'\((0, -5)\)', 'B': r'\((0, 9)\)', 'C': r'\((0, 4)\)', 'D': r'\((0, 76)\)'},
            'C',
            r'Thay \(x = 0\): \(f(0) = 81 \cdot 3^{-2} - 5 = \frac{81}{9} - 5 = 9 - 5 = 4\). Vậy tung độ gốc là \((0, 4)\).',
            r'Hàm mũ dịch chuyển cả số mũ lẫn đuôi: luôn thay trực tiếp \(x = 0\) để không nhầm với tiệm cận ngang \(y = -5\)!',
            {
                'A': ('Nhầm tiệm cận ngang', r'\(y = -5\) là tiệm cận ngang, không phải y-intercept.'),
                'B': ('Quên trừ 5', r'9 chỉ là \(81 \cdot 3^{-2}\), quên trừ 5 phía sau.'),
                'C': ('Đáp án đúng', r'\(f(0) = 9 - 5 = 4 \Rightarrow (0, 4)\).'),
                'D': ('Bỏ qua số mũ -2', r'Tính nhầm \(81 - 5 = 76\).'),
            },
            r'Gõ `y = 81 * 3^(x - 2) - 5` trên Desmos → bấm giao điểm trục Oy đọc ngay `(0, 4)`!'
        ),
        math_mcq(
            'sat_mm5_m2h_q11', 11, 'Advanced Math', 'Nonlinear functions', 'Hard',
            r'<p>The polynomial \(p(x) = x^3 + kx^2 - 5x + 6\), where \(k\) is a constant, is divisible by \((x - 2)\).</p>',
            r'What is the <b>remainder</b> when \(p(x)\) is divided by \((x + 3)\)?',
            {'A': r'\(-15\)', 'B': r'\(-1\)', 'C': r'\(3\)', 'D': r'\(-33\)'},
            'A',
            r'Bước 1 (Factor Theorem): \(p(2) = 0 \Rightarrow 8 + 4k - 10 + 6 = 0 \Rightarrow 4k = -4 \Rightarrow k = -1\). Bước 2 (Remainder Theorem): số dư khi chia cho \((x + 3)\) chính là \(p(-3) = (-3)^3 - (-3)^2 - 5(-3) + 6 = -27 - 9 + 15 + 6 = -15\).',
            r'Số dư khi chia đa thức \(p(x)\) cho \((x + 3)\) luôn bằng \(p(-3)\) (đổi dấu \(+3 \to -3\))!',
            {
                'A': ('Đáp án đúng', r'\(k = -1 \Rightarrow p(-3) = -15\).'),
                'B': ('Bẫy dừng ở k', r'\(-1\) chỉ là giá trị hằng số \(k\).'),
                'C': ('Thay +3 thay vì -3', r'\(p(3) = 27 - 9 - 15 + 6 = 9\) hoặc nhầm dấu.'),
                'D': ('Nhầm dấu -(-3)² thành +9 hoặc sai -5(-3)', r'Tính nhầm \(-27 - 9 - 15 + 6 = -45\) hay \(-33\).'),
            },
            r'Tìm `k = -1` từ `p(2) = 0`, gõ `p(x) = x^3 - x^2 - 5x + 6` rồi gõ `p(-3)` trên Desmos ra ngay `-15`!'
        ),
        math_mcq(
            'sat_mm5_m2h_q12', 12, 'Advanced Math', 'Nonlinear equations in one variable and systems of equations in two variables', 'Hard',
            r'<p>In the quadratic equation \(3x^2 - (2k + 3)x + 6k = 0\), where \(k\) is a constant, the <b>sum</b> of the two real solutions is \(11\).</p>',
            r'What is the <b>product</b> of the two solutions?',
            {'A': r'\(15\)', 'B': r'\(22\)', 'C': r'\(90\)', 'D': r'\(30\)'},
            'D',
            r'Theo Vieta: tổng hai nghiệm là \(\frac{2k + 3}{3} = 11 \Rightarrow 2k + 3 = 33 \Rightarrow k = 15\). Kiểm tra: \(3x^2 - 33x + 90 = 3(x - 5)(x - 6) = 0\) (có 2 nghiệm thực \(5\) và \(6\)). Tích hai nghiệm là \(\frac{6k}{3} = 2k = 30\).',
            r'Vieta 2 bước: dùng Tổng \(-b/a = 11\) tìm \(k = 15\), sau đó dùng Tích \(c/a = 2k = 30\)!',
            {
                'A': ('Dừng ở k', r'15 mới là giá trị của \(k\).'),
                'B': ('Nhầm nhân đôi tổng 11', r'22 không phải tích hai nghiệm.'),
                'C': ('Quên chia a = 3 ở tích', r'90 là hằng số \(c = 6k\), quên chia cho \(a = 3\).'),
                'D': ('Đáp án đúng', r'\(\frac{6(15)}{3} = 30\) (bằng \(5 \times 6\)).'),
            },
            r'Giải `(2k + 3)/3 = 11` được `k = 15`, rồi tính `6*15/3 = 30`.'
        ),
        math_spr(
            'sat_mm5_m2h_q13', 13, 'Advanced Math', 'Nonlinear equations in one variable and systems of equations in two variables', 'Hard',
            r'<p>Consider the rational equation below:</p><p style="text-align:center;">\[x + \frac{15}{x - 5} = \frac{9x - 30}{x - 5}\]</p>',
            r'What is the valid real solution \(x\) to the given equation?',
            ['9'], '9',
            r'Điều kiện \(x \neq 5\). Nhân cả hai vế với \((x - 5)\): \(x(x - 5) + 15 = 9x - 30 \Rightarrow x^2 - 14x + 45 = 0 \Rightarrow (x - 5)(x - 9) = 0\). Vì \(x = 5\) làm mẫu số bằng 0 (nghiệm ngoại lai, LOẠI!), nghiệm hợp lệ duy nhất là \(x = 9\).',
            r'Bắt buộc loại nghiệm làm mẫu số bằng 0 (\(x = 5\)) trước khi điền vào ô SPR!',
            r'Vẽ `y = x + 15/(x - 5)` và `y = (9x - 30)/(x - 5)` trên Desmos → chỉ có ĐÚNG 1 giao điểm tại `(9, 12.75)` → `x = 9`!'
        ),
        math_mcq(
            'sat_mm5_m2h_q14', 14, 'Advanced Math', 'Nonlinear equations in one variable and systems of equations in two variables', 'Hard',
            r'<p>The quadratic equation \(5x^2 - 20x + c = 0\), where \(c\) is an integer constant, has <b>two distinct real solutions</b>.</p>',
            r'What is the <b>greatest</b> possible value of \(c\)?',
            {'A': r'\(18\)', 'B': r'\(19\)', 'C': r'\(20\)', 'D': r'\(99\)'},
            'B',
            r'Có 2 nghiệm thực phân biệt \(\Leftrightarrow \Delta = b^2 - 4ac > 0 \Rightarrow (-20)^2 - 4(5)(c) > 0 \Rightarrow 400 - 20c > 0 \Rightarrow c < 20\). Vì \(c\) là số nguyên nhỏ hơn hẳn 20, giá trị nguyên lớn nhất là \(19\).',
            r'Tại \(c = 20\), \(\Delta = 0\) nên chỉ có 1 nghiệm kép — muốn có 2 nghiệm phân biệt phải lấy nguyên nhỏ hơn 1 đơn vị là \(19\)!',
            {
                'A': ('Chưa phải giá trị lớn nhất', r'\(c = 19\) vẫn thỏa \(c < 20\).'),
                'B': ('Đáp án đúng', r'\(c < 20 \Rightarrow c_{\max} = 19\).'),
                'C': ('Bẫy dấu bằng Δ = 0', r'Tại \(c = 20\) chỉ có đúng 1 nghiệm thực \(x = 2\).'),
                'D': ('Quên nhân hệ số a = 5', r'Giải nhầm \(400 - 4c > 0 \Rightarrow c < 100 \Rightarrow 99\).'),
            },
            r'Vẽ `y = 5x^2 - 20x + c` trên Desmos với slider nguyên `c` → `c = 19` cắt Ox tại 2 điểm, `c = 20` chỉ chạm 1 điểm!'
        ),
        math_mcq(
            'sat_mm5_m2h_q15', 15, 'Advanced Math', 'Equivalent expressions', 'Hard',
            r'<p>An offshore wind farm’s turbine output capacity \(N(t)\) after \(t\) <b>years</b> is modeled by \(N(t) = 600(1.25)^{t/2}\).</p>',
            r'Which of the following equations models the same capacity \(N\) in terms of \(m\), the number of <b>months</b> elapsed (where \(m = 12t\))?',
            {
                'A': r'\(N(m) = 600(1.25)^{6m}\)',
                'B': r'\(N(m) = 600(1.25)^{m/6}\)',
                'C': r'\(N(m) = 600(1.25)^{m/24}\)',
                'D': r'\(N(m) = 600(1.25)^{24m}\)',
            },
            'C',
            r'Vì \(m = 12t \Rightarrow t = \frac{m}{12}\). Thay vào số mũ: \(\frac{t}{2} = \frac{m/12}{2} = \frac{m}{24}\). Vậy \(N(m) = 600(1.25)^{m/24}\). Kiểm tra bằng phép thử 1 chu kỳ: sau 2 năm (\(m = 24\) tháng), số mũ bằng \(\frac{24}{24} = 1\) (khớp!).',
            r'Phép thử 1 chu kỳ (Plug-in 1 Cycle Test): 2 năm = 24 tháng phải làm số mũ bằng 1 \(\Rightarrow \frac{m}{24}\)!',
            {
                'A': ('Nhân ngược 12/2', r'Thay nhầm \(t = 12m\) thay vì \(t = m/12\).'),
                'B': ('Chia 12 cho 2 thay vì nhân mẫu', r'Nhầm \(\frac{m/12}{2} = \frac{m}{6}\).'),
                'C': ('Đáp án đúng', r'Khi \(m = 24\) tháng (= 2 năm), số mũ đúng bằng \(1\).'),
                'D': ('Đảo ngược phân số', r'Đặt \(24m\) thay vì \(m/24\).'),
            },
            r'Kiểm tra nhanh tại `t = 2` năm (`m = 24` tháng): gốc ra `600(1.25)^1 = 750`, chỉ phương án C cho `600(1.25)^(24/24) = 750`!'
        ),
        math_spr(
            'sat_mm5_m2h_q16', 16, 'Problem-Solving and Data Analysis', 'Ratios, rates, proportional relationships, and units', 'Hard',
            r'<p>A tidal turbine intake channel moves ocean water at a rate of \(81\) cubic feet per second. (\(1\text{ yard} = 3\text{ feet}\))</p>',
            r'What is this flow rate, in <b>cubic yards per minute</b>?',
            ['180'], '180',
            r'Đổi thể tích (\(1\text{ yd}^3 = 3^3 = 27\text{ ft}^3\)) và đổi thời gian (\(1\text{ phút} = 60\text{ giây}\)): \(\frac{81}{27} \times 60 = 3 \times 60 = 180\text{ yd}^3/\text{min}\).',
            r'Lập phương hệ số đổi đơn vị thể tích (\(3^3 = 27\)) rồi nhân 60 để chuyển từ giây sang phút!',
            r'Gõ `(81 / 3^3) * 60` trên Desmos ra ngay `180`.'
        ),
        math_mcq(
            'sat_mm5_m2h_q17', 17, 'Problem-Solving and Data Analysis', 'Percentages', 'Hard',
            r'<p>For three positive numbers \(p\), \(q\), and \(r\), it is given that \(p\) is \(125\%\) <b>greater than</b> \(q\), and \(q\) is \(20\%\) <b>less than</b> \(r\).</p>',
            r'Which statement accurately compares \(p\) to \(r\)?',
            {
                'A': r'\(p\) is \(80\%\) greater than \(r\).',
                'B': r'\(p\) is \(105\%\) greater than \(r\).',
                'C': r'\(p\) is equal to \(r\).',
                'D': r'\(p\) is \(180\%\) greater than \(r\).',
            },
            'A',
            r'Đặt \(r = 100 \Rightarrow q = (1 - 0.20)(100) = 80\). Chú ý "\(125\%\) GREATER than \(q\)" \(\Rightarrow p = (1 + 1.25)(80) = 2.25 \times 80 = 180\). So với \(r = 100\), \(p = 180\) nghĩa là \(p\) <b>lớn hơn \(r\) đúng \(80\%\)</b> (hay bằng \(180\%\) CỦA \(r\))!',
            r'Cảnh giác kép: "125% greater than" là nhân \(2.25\), và kết quả \(180\) so với \(100\) là "80% greater than" (KHÔNG phải "180% greater than"!).',
            {
                'A': ('Đáp án đúng', r'\(p = 1.80r \Rightarrow p\) lớn hơn \(r\) đúng \(80\%\).'),
                'B': ('Trừ thẳng phần trăm', r'Lấy \(125\% - 20\% = 105\%\).'),
                'C': ('Nhầm 125% OF q', r'Tính \(1.25 \times 0.80 = 1.00\) — bỏ quên chữ "greater than"!'),
                'D': ('Nhầm "180% of" với "180% greater than"', r'\(p = 180\%\) OF \(r\) tương đương \(80\%\) GREATER than \(r\)!'),
            },
            r'Gõ `2.25 * 0.80` trên Desmos ra `1.80` → lớn hơn `1.00` đúng `80%`!'
        ),
        math_mcq(
            'sat_mm5_m2h_q18', 18, 'Problem-Solving and Data Analysis', 'Evaluating statistical claims: Observational studies and experiments', 'Medium-Hard',
            r'<p>A specialty roaster randomly selected \(120\) green Arabica coffee batches from Highland Roasters’ annual harvest and randomly assigned \(60\) batches to a slow-roast profile and \(60\) batches to a fast-roast profile. Blind tastings showed that the slow-roast group scored significantly higher in aroma complexity than the fast-roast group.</p>',
            r'Which of the following is the strongest valid conclusion from this study?',
            {
                'A': r'Slow-roasting causes higher aroma complexity for all coffee varieties grown worldwide.',
                'B': r'Slow-roasting causes higher aroma complexity for Arabica batches from Highland Roasters’ annual harvest.',
                'C': r'Slow-roasting is associated with higher aroma complexity, but cause and effect cannot be established.',
                'D': r'Every slow-roasted batch will always score higher than every fast-roasted batch.',
            },
            'B',
            r'Nghiên cứu này có CẢ <b>Random Selection</b> (từ vụ mùa Arabica của Highland Roasters → suy rộng đúng cho quần thể đó, KHÔNG suy rộng ra toàn thế giới) VÀ <b>Random Assignment</b> (phân nhóm ngẫu nhiên → ĐƯỢC PHÉP kết luận nhân-quả Cause-and-Effect!).',
            r'Random Assignment chứng minh được Causation ("causes"), còn Random Selection quy định chính xác phạm vi quần thể được suy rộng!',
            {
                'A': ('Suy rộng quá phạm vi mẫu', r'Chỉ chọn ngẫu nhiên từ Highland Roasters nên không suy rộng ra "all coffee varieties worldwide".'),
                'B': ('Đáp án đúng', r'Vừa kết luận đúng nhân-quả (nhờ Random Assignment) vừa giới hạn đúng quần thể mẫu.'),
                'C': ('Phủ nhận nhầm nhân-quả', r'Vì có Random Assignment (thí nghiệm đối chứng), hoàn toàn đủ điều kiện kết luận nhân-quả.'),
                'D': ('Khẳng định tuyệt đối "every"', r'Kết quả thống kê áp dụng cho mức trung bình nhóm, không đảm bảo cho từng cá thể đơn lẻ.'),
            },
            r'Soi 2 từ khóa vàng: "randomly selected from [Population X]" + "randomly assigned" → Causes + đúng Population X!'
        ),
        math_spr(
            'sat_mm5_m2h_q19', 19, 'Problem-Solving and Data Analysis', 'One-variable data: Distributions and measures of center and spread', 'Medium-Hard',
            r'<p>A wind energy park consists of two sectors: \(8\) turbines in Sector North produce a mean of \(52\) MWh per day, and \(12\) turbines in Sector South produce a mean of \(67\) MWh per day.</p>',
            r'What is the mean daily output, in MWh, of all \(20\) turbines combined?',
            ['61'], '61',
            r'Tính trung bình có trọng số (Weighted Mean): Tổng sản lượng \(= 8(52) + 12(67) = 416 + 804 = 1{,}220\text{ MWh}\). Trung bình chung của 20 tuabin \(= \frac{1{,}220}{20} = 61\text{ MWh}\).',
            r'Khi gộp 2 nhóm khác cỡ mẫu (\(8 \neq 12\)), tuyệt đối không lấy \(\frac{52+67}{2} = 59.5\) mà phải lấy Tổng tất cả chia Tổng số lượng!',
            r'Gõ `(8*52 + 12*67) / 20` trên Desmos ra ngay `61`!'
        ),
        math_mcq(
            'sat_mm5_m2h_q20', 20, 'Geometry and Trigonometry', 'Circles', 'Hard',
            svg_q20 + r'<p>In the \(xy\)-plane, a circle is defined by \(3x^2 + 3y^2 - 24x + 18y - 33 = 0\). An arc on this circle is subtended by a central angle measuring \(\frac{2\pi}{3}\) radians.</p>',
            r'What is the length of this arc?',
            {'A': r'\(2\pi\)', 'B': r'\(12\pi\)', 'C': r'\(4\pi\)', 'D': r'\(24\pi\)'},
            'C',
            r'Bước 1: Chia hai vế cho 3: \(x^2 + y^2 - 8x + 6y = 11\). Bước 2: Hoàn thành bình phương: \((x - 4)^2 + (y + 3)^2 = 11 + 16 + 9 = 36 \Rightarrow r = 6\). Bước 3: Độ dài cung theo radian: \(s = r\theta = 6 \cdot \frac{2\pi}{3} = 4\pi\).',
            r'Bài toán ghép 2 kỹ năng Hard M2: chia hệ số 3 + hoàn thành bình phương tìm \(r = 6\), rồi nhân \(s = r\theta\)!',
            {
                'A': ('Nhầm θ = π/3', r'Thiếu hệ số 2 ở tử góc radian.'),
                'B': ('Nhầm với diện tích quạt', r'\(A = \frac{1}{2}r^2\theta = 12\pi\) là diện tích hình quạt, không phải độ dài cung!'),
                'C': ('Đáp án đúng', r'\(r = 6 \Rightarrow s = 6 \cdot \frac{2\pi}{3} = 4\pi\).'),
                'D': ('Dùng r² = 36 thay vì r = 6', r'Tính \(36 \cdot \frac{2\pi}{3} = 24\pi\).'),
            },
            r'Gõ `3x^2 + 3y^2 - 24x + 18y - 33 = 0` lên Desmos đo được `r = 6`, rồi tính `6 * (2/3) = 4` → `4π`!'
        ),
        math_mcq(
            'sat_mm5_m2h_q21', 21, 'Geometry and Trigonometry', 'Right triangles and trigonometry', 'Hard',
            r'<p>In a right triangle, the two acute angles measure \((3x + 12)^\circ\) and \((2x + 18)^\circ\), and \(\sin(3x + 12)^\circ = \cos(2x + 18)^\circ\).</p>',
            r'What is the exact value of \(\cos(5x)^\circ\)?',
            {'A': r'\(\frac{\sqrt{3}}{2}\)', 'B': r'\(\frac{\sqrt{2}}{2}\)', 'C': r'\(0\)', 'D': r'\(\frac{1}{2}\)'},
            'D',
            r'Vì hai góc nhọn thỏa \(\sin(A) = \cos(B)\), tổng hai góc bằng \(90^\circ\): \((3x + 12) + (2x + 18) = 90 \Rightarrow 5x + 30 = 90 \Rightarrow 5x = 60\)! Thay thẳng \(5x = 60^\circ\): \(\cos(60^\circ) = \frac{1}{2}\).',
            r'Định lý góc phụ nhau \(\sin(A) = \cos(B) \Rightarrow A + B = 90^\circ\) cho ra thẳng \(5x = 60^\circ\) không cần giải lẻ \(x\)!',
            {
                'A': ('Nhầm sin(60°) với cos(60°)', r'\(\frac{\sqrt{3}}{2}\) là \(\sin(60^\circ)\) hoặc \(\cos(30^\circ)\).'),
                'B': ('Nhầm góc 45°', r'\(\frac{\sqrt{2}}{2}\) là \(\cos(45^\circ)\).'),
                'C': ('Nhầm góc 90°', r'0 là \(\cos(90^\circ)\).'),
                'D': ('Đáp án đúng', r'\(5x = 60^\circ \Rightarrow \cos(60^\circ) = \frac{1}{2}\).'),
            },
            r'Đặt Desmos sang Degree mode (biểu tượng cờ-lê), giải `5x = 60` rồi bấm `cos(60)` ra ngay `0.5` (`1/2`)!'
        ),
        math_spr(
            'sat_mm5_m2h_q22', 22, 'Geometry and Trigonometry', 'Area and volume', 'Hard',
            svg_q22 + r'<p>Two similar glass atrium cones, Cone A and Cone B, have volumes of \(54\pi\text{ cm}^3\) and \(1{,}458\pi\text{ cm}^3\), respectively. The total surface area of Cone A is \(45\pi\text{ cm}^2\).</p>',
            r'If the total surface area of Cone B is \(s\pi\text{ cm}^2\), what is the value of \(s\)?',
            ['405'], '405',
            r'Tỉ số thể tích của hai khối đồng dạng là \(k^3 = \frac{1{,}458\pi}{54\pi} = 27 \Rightarrow\) tỉ số cạnh tuyến tính là \(k = \sqrt[3]{27} = 3\). Suy ra tỉ số diện tích toàn phần là \(k^2 = 3^2 = 9\). Vậy \(\text{SA}_B = 45\pi \times 9 = 405\pi \Rightarrow s = 405\).',
            r'Chiều ngược của bậc thang 3D: Tỉ số Thể tích \(k^3 \xrightarrow{\sqrt[3]{\cdot}} k \xrightarrow{(\cdot)^2} \text{Tỉ số Diện tích } k^2\)!',
            r'Gõ `45 * ((1458 / 54)^(1/3))^2` trên Desmos ra ngay `405`!'
        ),
    ]
