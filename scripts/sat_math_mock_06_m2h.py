# -*- coding: utf-8 -*-
"""
Digital SAT Math Adaptive Mock Test #6 — Module 2 Hard (650–800 Band, 22 Questions)
Themes: Coral nursery aquaculture, commercial drone delivery networks, digital printmaking studios,
seismology & tectonic monitoring stations, spherical & conical observatory domes.
Blueprint: 8 Algebra (Q1-Q8), 7 Advanced Math (Q9-Q15), 4 PSDA (Q16-Q19), 3 Geometry/Trig (Q20-Q22).
Format: 16 MCQ (A:4, B:4, C:4, D:4) + 6 SPR (Q5, Q9, Q13, Q16, Q19, Q22).
"""

from fractions import Fraction
import math
from sat_math_helpers import (
    math_mcq, math_spr, build_math_table,
    svg_right_triangle, svg_cylinder
)


def verify_math():
    """Programmatic exact arithmetic verification for all 22 Module 2 Hard questions."""
    # Q1: (2/5)x - (3/4)y = 6 and ax + 15y = b infinitely many solutions => k = -20 => a = -8, b = -120 => a+b = -128
    k1 = Fraction(15, 1) / Fraction(-3, 4)
    a1 = Fraction(2, 5) * k1
    b1 = 6 * k1
    assert k1 == -20 and a1 == -8 and b1 == -120 and a1 + b1 == -128

    # Q2: Table (1,9), (4,27), (7,45) for 2f(x) - 5 => f(x) = 3x + 4 => x-int = -4/3
    for xv, yv in [(1, 9), (4, 27), (7, 45)]:
        fx = Fraction(yv + 5, 2)
        assert fx == 3 * xv + 4
    assert 3 * Fraction(-4, 3) + 4 == 0

    # Q3: |4x - 9| - c = 11, diff of roots = 8 => 2(c + 11)/4 = 8 => c = 5
    c3 = Fraction(8 * 4, 2) - 11
    r3_hi = Fraction(9 + (c3 + 11), 4)
    r3_lo = Fraction(9 - (c3 + 11), 4)
    assert c3 == 5 and r3_hi - r3_lo == 8

    # Q4: f(x) = mx + b (m < 0), f(f(x)) = 16x - 15 => m = -4, b = 5 => f(2) = -3
    m4 = -4
    b4 = Fraction(-15, m4 + 1)
    assert m4 < 0 and m4 ** 2 == 16 and b4 == 5
    for xv in (-3, 0, 2, 5):
        assert m4 * (m4 * xv + b4) + b4 == 16 * xv - 15
    assert m4 * 2 + b4 == -3

    # Q5: y <= 2x + 8, y <= -4x + 44, y >= 4 => vertices (-2,4), (10,4), (6,20) => Area = 96
    x5_l = Fraction(4 - 8, 2)
    x5_r = Fraction(44 - 4, 4)
    x5_t = Fraction(44 - 8, 2 + 4)
    y5_t = 2 * x5_t + 8
    assert x5_l == -2 and x5_r == 10 and x5_t == 6 and y5_t == -4 * x5_t + 44 == 20
    area5 = Fraction(1, 2) * (x5_r - x5_l) * (y5_t - 4)
    assert area5 == 96

    # Q6: y < -(3/2)x - 4 and y < 2x - 11 => intersection (2, -7) => y < -7 < 0 => Q-I & Q-II empty
    x6 = Fraction(11 - 4, Fraction(2) + Fraction(3, 2))
    y6 = 2 * x6 - 11
    assert x6 == 2 and y6 == Fraction(-3, 2) * x6 - 4 == -7 < 0
    assert -10 < Fraction(-3, 2) * 2 - 4 and -10 < 2 * 2 - 11          # Q-IV solution (2, -10)
    assert -20 < Fraction(-3, 2) * (-2) - 4 and -20 < 2 * (-2) - 11    # Q-III solution (-2, -20)

    # Q7: s + d <= 120, 14s + 22d >= 2120 => min d = 55
    d7_min = Fraction(2120 - 14 * 120, 22 - 14)
    assert d7_min == 55 and 14 * 65 + 22 * 55 == 2120 and 14 * 66 + 22 * 54 < 2120

    # Q8: 5x + 3y = 36 shifted left 3, down k passes through (0, 0) => 5(3) + 3k = 36 => k = 7
    k8 = Fraction(36 - 5 * 3, 3)
    assert k8 == 7 and 5 * (0 + 3) + 3 * (0 + k8) == 36

    # Q9: 324 * (1/3)^(t/6) = 12 => t = 18
    t9 = 18
    assert Fraction(324, 3 ** (t9 // 6)) == 12

    # Q10: P(x) = 2x^3 + kx^2 - 11x - 6, P(2) = 0 => k = 3 => P(-2) = 12
    k10 = Fraction(-(2 * (2 ** 3) - 11 * 2 - 6), 2 ** 2)
    p10 = lambda x: 2 * (x ** 3) + k10 * (x ** 2) - 11 * x - 6
    assert k10 == 3 and p10(2) == 0 and p10(-2) == 12

    # Q11: 2x^2 - 14x + c = 0, (r - s)^2 = 17 => (7)^2 - 4(c/2) = 17 => c = 16
    sum11 = Fraction(14, 2)
    c11 = Fraction(sum11 ** 2 - 17, 2)
    assert c11 == 16 and (-14) ** 2 - 4 * 2 * c11 == 68 > 0 and Fraction(68, 2 ** 2) == 17

    # Q12: -2x^2 + 12x + 5 = 4x + k tangent => 2x^2 - 8x + (k - 5) = 0 => Delta = 0 => k = 13
    k12 = 5 + Fraction((-8) ** 2, 4 * 2)
    assert k12 == 13 and (-8) ** 2 - 4 * 2 * (k12 - 5) == 0

    # Q13: (1.728)^(2/3) = (1.2^3)^(2/3) = 1.44 => r = 44
    assert Fraction(12, 10) ** 3 == Fraction(1728, 1000)
    assert (Fraction(12, 10) ** 2 - 1) * 100 == 44

    # Q14: f(x)=a(x-h)^2+5 through (-1,37) and (7,37) => h=3, a=2; g(x)=f(x+2)-10=2(x-1)^2-5 => g(x)=67 (x>0) => x=7
    h14 = Fraction(-1 + 7, 2)
    a14 = Fraction(37 - 5, (7 - h14) ** 2)
    f14 = lambda x: a14 * (x - h14) ** 2 + 5
    g14 = lambda x: f14(x + 2) - 10
    assert h14 == 3 and a14 == 2 and f14(-1) == f14(7) == 37
    assert g14(7) == 67 and g14(-5) == 67

    # Q15: 2x^2 - kx + 36 = 0, distinct positive integer roots => rs = 18 => k in {38, 22, 18} => max - min = 20
    ks15 = [2 * (r + 18 // r) for r in range(1, 19) if 18 % r == 0 and r < 18 // r]
    assert ks15 == [38, 22, 18] and max(ks15) - min(ks15) == 20

    # Q16: 225 yd^3 at 45 ft^3/min => (225 * 27) / 45 = 135 min
    assert Fraction(225 * (3 ** 3), 45) == 135

    # Q17: m / (135 + m) = 2/5 => m = 90 => P(Gallery Grade | Baryta) = 90 / (90 + 30) = 3/4
    m17 = Fraction(2 * 135, 5 - 2)
    assert m17 == 90 and Fraction(m17, m17 + 30) == Fraction(3, 4)

    # Q18: Station Alpha vs Station Gamma (= Beta + 5)
    alpha18 = [10]*4 + [12]*2 + [14]*4 + [16]*2 + [18]*4
    beta18 = [10]*1 + [12]*3 + [14]*8 + [16]*3 + [18]*1
    gamma18 = [x + 5 for x in beta18]
    mean_a = Fraction(sum(alpha18), len(alpha18))
    mean_g = Fraction(sum(gamma18), len(gamma18))
    var_a = sum((x - mean_a) ** 2 for x in alpha18) / len(alpha18)
    var_g = sum((x - mean_g) ** 2 for x in gamma18) / len(gamma18)
    assert mean_a == 14 and mean_g == 19 and mean_g > mean_a
    assert var_a == 9 and var_g == Fraction(7, 2) and var_g < var_a

    # Q19: (240 * 17.5 + 22.5 * w) / (240 + w) = 20.5 => w = 360
    w19 = Fraction(240 * (Fraction(41, 2) - Fraction(35, 2)), Fraction(45, 2) - Fraction(41, 2))
    assert w19 == 360 and Fraction(240 * Fraction(35, 2) + w19 * Fraction(45, 2), 240 + w19) == Fraction(41, 2)

    # Q20: 3x^2 + 3y^2 - 18x + 24y + c = 0, C = 12pi => r = 6 => 25 - c/3 = 36 => c = -33
    r20 = Fraction(12, 2)
    c20 = 3 * (3 ** 2 + 4 ** 2 - r20 ** 2)
    assert r20 == 6 and c20 == -33 and (9 + 16 - Fraction(c20, 3)) == 36

    # Q21: Conical roof, sin(alpha) = r/s = 8/17, base area 256pi => r = 16, s = 34 => LSA = 544pi
    r21 = int(math.isqrt(256))
    s21 = r21 * Fraction(17, 8)
    assert r21 == 16 and s21 == 34 and r21 * s21 == 544 and 16 ** 2 + 30 ** 2 == 34 ** 2

    # Q22: Cylinder + hemisphere, 2pi r^2 = (1/2)(2pi rh) => h = 2r; V_cyl = 432pi => r = 6, h = 12
    # Curved SA_1 = 216pi, Curved SA_2 = 486pi => k = 3/2 => V_total_2 = 576pi * (3/2)^3 = 1944pi
    r22 = 6
    h22 = 2 * r22
    assert r22 ** 2 * h22 == 432
    csa1 = 2 * r22 ** 2 + 2 * r22 * h22
    v1_tot = r22 ** 2 * h22 + Fraction(2, 3) * (r22 ** 3)
    scale_sq = Fraction(486, csa1)
    scale = Fraction(3, 2)
    assert csa1 == 216 and v1_tot == 576 and scale_sq == scale ** 2
    v2_tot = v1_tot * (scale ** 3)
    assert v2_tot == 1944
    # Direct verification on scaled tower (R=9, H=18)
    R22, H22 = r22 * scale, h22 * scale
    assert 2 * R22 ** 2 + 2 * R22 * H22 == 486
    assert R22 ** 2 * H22 + Fraction(2, 3) * (R22 ** 3) == 1944

    return True


def get_m2h_questions():
    tbl_q2 = build_math_table(
        ['\\(x\\)', '\\(2f(x) - 5\\)'],
        [
            ['1', '9'],
            ['4', '27'],
            ['7', '45'],
        ],
        caption='Transformed Linear Function Values'
    )
    tbl_q17 = build_math_table(
        ['Paper Stock', 'Gallery Grade', 'Second Tier', 'Total'],
        [
            ['Cotton Rag', '135', '45', '180'],
            ['Baryta', '\\(m\\)', '30', '\\(m + 30\\)'],
            ['Total', '\\(135 + m\\)', '75', '\\(210 + m\\)'],
        ],
        caption='Digital Printmaking Studio Quality Inspection'
    )
    tbl_q18 = build_math_table(
        ['Vibration Duration (seconds)', 'Station Alpha (Number of Events)', 'Station Beta (Number of Events)'],
        [
            ['10', '4', '1'],
            ['12', '2', '3'],
            ['14', '4', '8'],
            ['16', '2', '3'],
            ['18', '4', '1'],
        ],
        caption='Seismic Vibration Durations Recorded at Two Monitoring Stations (n = 16 each)'
    )
    svg_q21 = svg_right_triangle(
        a_lbl='h', b_lbl='r', c_lbl='s',
        angle_bottom_right='θ', angle_top_left='α',
        v_top='V', v_right_angle='O', v_right='P',
        note='Axial cross-section of conical observatory roof (not to scale).'
    )
    svg_q22 = svg_cylinder(
        r_lbl='r', h_lbl='h',
        note='Cylindrical wall section beneath hemispherical dome (not to scale).'
    )

    return [
        # Q1 — Algebra (Hard, MCQ -> B)
        math_mcq(
            'sat_mm6_m2h_q1', 1, 'Algebra', 'Systems of two linear equations in two variables', 'Hard',
            r'<p>In the system of linear equations below, \(a\) and \(b\) are constants:</p><p style="text-align:center;">\[\begin{cases} \dfrac{2}{5}x - \dfrac{3}{4}y = 6 \\ ax + 15y = b \end{cases}\]</p>',
            r'If the system has <b>infinitely many solutions</b>, what is the value of \(a + b\)?',
            {'A': r'\(-112\)', 'B': r'\(-128\)', 'C': r'\(128\)', 'D': r'\(-122\)'},
            'B',
            r'Hệ có vô số nghiệm khi phương trình thứ hai là bội số hằng \(k\) của phương trình thứ nhất. So sánh cặp hệ số của \(y\): \(k = \dfrac{15}{-3/4} = -20\). Nhân toàn bộ phương trình đầu với \(-20\):<br>\((-20)\left(\dfrac{2}{5}\right)x - (-20)\left(\dfrac{3}{4}\right)y = (-20)(6) \Rightarrow -8x + 15y = -120\).<br>Vậy \(a = -8\) và \(b = -120\), suy ra \(a + b = -8 + (-120) = -128\).',
            r'Khi hệ có phân số, tìm ngay tỉ số nhân \(k\) từ cột đã biết đầy đủ hệ số (\(-3/4 \to +15\) tức nhân \(-20\)), đặc biệt chú ý DẤU ÂM!',
            {
                'A': ('Sai dấu của a', r'Tính đúng \(b = -120\) nhưng lấy nhầm \(a = +8 \Rightarrow 8 - 120 = -112\).'),
                'B': ('Đáp án đúng', r'\(k = -20 \Rightarrow a = -8, b = -120 \Rightarrow a + b = -128\).'),
                'C': ('Quên dấu trừ ở k = -20', r'Nhân với \(+20\) thay vì \(-20\) nên ra \(+8 + 120 = +128\).'),
                'D': ('Nhân sai phân số 2/5', r'Tính nhầm \(a = -2\) thay vì \(-8\), dẫn đến \(-2 - 120 = -122\).'),
            },
            r'Gõ `(2/5)x - (3/4)y = 6` và `ax + 15y = b` vào Desmos (đặt `a = -8, b = -120`) sẽ thấy hai đường thẳng trùng khít hoàn toàn!'
        ),
        # Q2 — Algebra (Hard, MCQ -> D)
        math_mcq(
            'sat_mm6_m2h_q2', 2, 'Algebra', 'Linear functions', 'Hard',
            tbl_q2 + r'<p>The table above shows three pairs of values for \(x\) and \(2f(x) - 5\), where \(f\) is a linear function.</p>',
            r'What is the \(x\)-intercept of the graph of \(y = f(x)\) in the \(xy\)-plane?',
            {
                'A': r'\(\left(-\dfrac{1}{2}, 0\right)\)',
                'B': r'\((0, 4)\)',
                'C': r'\(\left(\dfrac{4}{3}, 0\right)\)',
                'D': r'\(\left(-\dfrac{4}{3}, 0\right)\)',
            },
            'D',
            r'Bước 1: Khôi phục giá trị thực của \(f(x)\) bằng cách cộng \(5\) rồi chia \(2\) ở cột phải:<br>• \(x = 1 \Rightarrow f(1) = \dfrac{9 + 5}{2} = 7\)<br>• \(x = 4 \Rightarrow f(4) = \dfrac{27 + 5}{2} = 16\)<br>• \(x = 7 \Rightarrow f(7) = \dfrac{45 + 5}{2} = 25\).<br>Bước 2: Tìm phương trình \(f(x)\): hệ số góc \(m = \dfrac{16 - 7}{4 - 1} = 3\), và \(f(x) = 3(x - 1) + 7 = 3x + 4\).<br>Bước 3: Tìm \(x\)-intercept (\(f(x) = 0\)): \(3x + 4 = 0 \Rightarrow x = -\dfrac{4}{3}\), tức điểm \(\left(-\dfrac{4}{3}, 0\right)\).',
            r'Gặp bảng cho biểu thức biến đổi như \(2f(x) - 5\), PHẢI giải ngược lại để tìm đúng bảng giá trị của \(f(x)\) trước khi tìm giao điểm trục hoành!',
            {
                'A': ('Dùng thẳng cột 2f(x) - 5', r'Lập phương trình \(y = 6x + 3 = 0 \Rightarrow x = -\frac{1}{2}\) (sai vì chưa khôi phục \(f(x)\)).'),
                'B': ('Nhầm y-intercept với x-intercept', r'\((0, 4)\) là giao điểm trục tung, đề hỏi giao điểm trục hoành.'),
                'C': ('Sai dấu khi chuyển vế', r'Giải \(3x + 4 = 0\) nhầm thành \(x = +\frac{4}{3}\).'),
                'D': ('Đáp án đúng', r'\(f(x) = 3x + 4 = 0 \Rightarrow \left(-\frac{4}{3}, 0\right)\).'),
            },
            r'Nhập Table `x1 = [1, 4, 7]`, `y1 = [7, 16, 25]` vào Desmos → gõ `y1 ~ m x1 + b` ra `y = 3x + 4` → bấm giao điểm trục Ox đọc ngay `(-1.333, 0)`!'
        ),
        # Q3 — Algebra (Hard, MCQ -> A)
        math_mcq(
            'sat_mm6_m2h_q3', 3, 'Algebra', 'Absolute value linear equations', 'Hard',
            r'<p>During a seismic sensor calibration test, the threshold equation below has two real solutions, where \(c\) is a constant:</p><p style="text-align:center;">\[|4x - 9| - c = 11\]</p><p>The positive difference between the two solutions to this equation is \(8\).</p>',
            r'What is the value of \(c\)?',
            {'A': r'\(5\)', 'B': r'\(16\)', 'C': r'\(21\)', 'D': r'\(-3\)'},
            'A',
            r'Cô lập giá trị tuyệt đối: \(|4x - 9| = c + 11\) (với \(c + 11 > 0\)).<br>Hai nghiệm của phương trình là:<br>\(x_1 = \dfrac{9 + (c + 11)}{4}\) và \(x_2 = \dfrac{9 - (c + 11)}{4}\).<br>Hiệu dương giữa hai nghiệm:<br>\(x_1 - x_2 = \dfrac{2(c + 11)}{4} = \dfrac{c + 11}{2} = 8 \Rightarrow c + 11 = 16 \Rightarrow c = 5\).<br>(Kiểm tra: \(|4x - 9| = 16 \Rightarrow x = 6.25\) và \(x = -1.75\), hiệu đúng bằng \(8\)!)',
            r'Khoảng cách giữa hai nghiệm của \(|ax - b| = M\) luôn là \(\dfrac{2M}{|a|}\) (độc lập hoàn toàn với hằng số \(b\)!).',
            {
                'A': ('Đáp án đúng', r'\(\frac{c + 11}{2} = 8 \Rightarrow c + 11 = 16 \Rightarrow c = 5\).'),
                'B': ('Dừng ở giá trị M = c + 11', r'\(16\) là giá trị của \(c + 11\), quên trừ đi \(11\) để ra \(c\).'),
                'C': ('Quên nhân hệ số 2 ở khoảng cách hai phía', r'Giải nhầm \(\frac{c + 11}{4} = 8 \Rightarrow c = 21\).'),
                'D': ('Quên nhân 4 trong mẫu số', r'Giải nhầm \(2(c + 11) = 16 \Rightarrow c = -3\).'),
            },
            r'Gõ `y = abs(4x - 9) - c` và `y = 11` trên Desmos với thanh trượt `c`; tại `c = 5`, bấm hai giao điểm `(-1.75, 11)` và `(6.25, 11)` thấy ngay hiệu `6.25 - (-1.75) = 8`!'
        ),
        # Q4 — Algebra (Hard, MCQ -> C)
        math_mcq(
            'sat_mm6_m2h_q4', 4, 'Algebra', 'Linear functions', 'Hard',
            r'<p>A digital printmaking color-profile routine applies a linear function \(f(x) = mx + b\), where \(m\) and \(b\) are constants and \(m < 0\). Applying the function twice yields:</p><p style="text-align:center;">\[f(f(x)) = 16x - 15\]</p><p>for all real numbers \(x\).</p>',
            r'What is the value of \(f(2)\)?',
            {'A': r'\(5\)', 'B': r'\(-13\)', 'C': r'\(-3\)', 'D': r'\(13\)'},
            'C',
            r'Tính hàm hợp \(f(f(x))\):<br>\(f(f(x)) = m(mx + b) + b = m^2 x + b(m + 1)\).<br>Đồng nhất hệ số với \(16x - 15\):<br>• \(m^2 = 16\). Vì đề cho điều kiện <b>\(m < 0\)</b>, ta PHẢI chọn \(m = -4\).<br>• \(b(m + 1) = -15 \Rightarrow b(-4 + 1) = -15 \Rightarrow -3b = -15 \Rightarrow b = 5\).<br>Vậy \(f(x) = -4x + 5\), suy ra \(f(2) = -4(2) + 5 = -3\).',
            r'Với bài toán hàm hợp \(f(f(x)) = m^2 x + b(m + 1)\), luôn kiểm tra cực kỹ điều kiện dấu của \(m\) (\(m < 0\) hay \(m > 0\)) trước khi giải tìm \(b\)!',
            {
                'A': ('Bỏ qua điều kiện m < 0', r'Chọn nhầm \(m = +4 \Rightarrow 5b = -15 \Rightarrow b = -3 \Rightarrow f(2) = 4(2) - 3 = 5\).'),
                'B': ('Sai dấu b = -5', r'Giải nhầm \(-3b = -15 \Rightarrow b = -5 \Rightarrow f(2) = -8 - 5 = -13\).'),
                'C': ('Đáp án đúng', r'\(m = -4, b = 5 \Rightarrow f(2) = -4(2) + 5 = -3\).'),
                'D': ('Bỏ dấu trừ khi tính f(2)', r'Tính nhầm \(4(2) + 5 = 13\) thay vì \(-4(2) + 5 = -3\).'),
            },
            r'Kiểm chứng nhanh trên Desmos: định nghĩa `f(x) = -4x + 5`, vẽ `y = f(f(x))` và `y = 16x - 15` thấy trùng khít 100%, rồi gõ `f(2)` ra ngay `-3`!'
        ),
        # Q5 — Algebra (Hard, SPR -> 96)
        math_spr(
            'sat_mm6_m2h_q5', 5, 'Algebra', 'Linear inequalities in one or two variables', 'Hard',
            r'<p>In the \(xy\)-plane, a triangular commercial drone staging zone is bounded by the system of linear inequalities below:</p><p style="text-align:center;">\[\begin{cases} y \le 2x + 8 \\ y \le -4x + 44 \\ y \ge 4 \end{cases}\]</p>',
            r'What is the <b>area</b>, in square units, of this triangular staging zone?',
            ['96'], '96',
            r'Tìm tọa độ 3 đỉnh của tam giác:<br>• Đỉnh trái (giao của \(y = 2x + 8\) và \(y = 4\)): \(2x + 8 = 4 \Rightarrow x = -2\), đỉnh \((-2, 4)\).<br>• Đỉnh phải (giao của \(y = -4x + 44\) và \(y = 4\)): \(-4x + 44 = 4 \Rightarrow x = 10\), đỉnh \((10, 4)\).<br>• Đỉnh trên (giao của \(y = 2x + 8\) và \(y = -4x + 44\)): \(2x + 8 = -4x + 44 \Rightarrow 6x = 36 \Rightarrow x = 6, y = 20\), đỉnh \((6, 20)\).<br>Độ dài đáy ngang nằm trên đường \(y = 4\) là \(b = 10 - (-2) = 12\). Chiều cao từ đỉnh \((6, 20)\) xuống đáy \(y = 4\) là \(h = 20 - 4 = 16\).<br>Diện tích tam giác: \(A = \dfrac{1}{2} \times 12 \times 16 = 96\).',
            r'Cẩn thận bẫy chiều cao khi đường biên đáy là \(y = 4\) (KHÔNG phải trục Ox \(y = 0\)) — phải lấy \(h = y_{\text{đỉnh}} - 4 = 16\), không lấy \(20\)!',
            r'Vẽ `y = 2x + 8`, `y = -4x + 44`, `y = 4` trên Desmos → bấm 3 giao điểm `(-2, 4)`, `(10, 4)`, `(6, 20)` → gõ `0.5 * (10 - (-2)) * (20 - 4)` ra ngay `96`!'
        ),
        # Q6 — Algebra (Hard, MCQ -> D)
        math_mcq(
            'sat_mm6_m2h_q6', 6, 'Algebra', 'Linear inequalities in one or two variables', 'Hard',
            r'<p>Consider the system of linear inequalities in the \(xy\)-plane:</p><p style="text-align:center;">\[\begin{cases} y < -\dfrac{3}{2}x - 4 \\ y < 2x - 11 \end{cases}\]</p>',
            r'Which quadrants of the \(xy\)-plane contain <b>no solutions</b> to this system?',
            {
                'A': r'Quadrant I only',
                'B': r'Quadrant II only',
                'C': r'Quadrants II and III',
                'D': r'Quadrants I and II',
            },
            'D',
            r'Tìm đỉnh giao điểm hai đường biên: \(-\dfrac{3}{2}x - 4 = 2x - 11 \Rightarrow \dfrac{7}{2}x = 7 \Rightarrow x = 2\), và \(y = 2(2) - 11 = -7\).<br>Vì cả hai bất phương trình đều lấy phần <b>phía dưới</b> hai đường thẳng có hệ số góc trái dấu (\(-\frac{3}{2}\) và \(+2\)), mọi điểm nghiệm \((x, y)\) đều phải thỏa \(y < -7 < 0\). Do đó toàn bộ nửa mặt phẳng trên (\(y > 0\), tức cả <b>Quadrant I và Quadrant II</b>) hoàn toàn không có nghiệm! Ngược lại, điểm \((2, -10)\) nằm trong Q-IV và \((-2, -20)\) nằm trong Q-III đều thỏa mãn hệ.',
            r'Khi cả hai bất phương trình dạng \(y <\) (ngược chiều slope) cắt nhau tại điểm có tung độ âm (\(y = -7 < 0\)), toàn bộ phần \(y > 0\) (Quadrants I & II) chắc chắn vô nghiệm!',
            {
                'A': ('Bỏ sót Quadrant II', r'Tại Quadrant II (\(x < 0, y > 0\)), bất phương trình \(y < 2x - 11 < -11 < 0\) cũng bị vi phạm hoàn toàn.'),
                'B': ('Bỏ sót Quadrant I', r'Tại Quadrant I (\(x > 0, y > 0\)), bất phương trình \(y < -\frac{3}{2}x - 4 < -4 < 0\) cũng vô nghiệm.'),
                'C': ('Loại nhầm Quadrant III', r'Điểm \((-2, -20)\) thuộc Q-III thỏa cả \(-20 < -1\) và \(-20 < -15\).'),
                'D': ('Đáp án đúng', r'Mọi nghiệm đều có \(y < -7 < 0\), nên cả Quadrant I và Quadrant II không có nghiệm nào.'),
            },
            r'Gõ thẳng `y < -(3/2)x - 4` và `y < 2x - 11` vào Desmos → vùng giao nhau nằm hoàn toàn phía dưới đường `y = -7` → nhìn 2 giây thấy ngay Q-I và Q-II trống hoàn toàn!'
        ),
        # Q7 — Algebra (Hard, MCQ -> B)
        math_mcq(
            'sat_mm6_m2h_q7', 7, 'Algebra', 'Linear inequalities in one or two variables', 'Hard',
            r'<p>A coral nursery aquaculture facility plans to install at most \(120\) total propagation racks, divided between shallow racks (\(s\)) and deep racks (\(d\)). Each shallow rack holds \(14\) coral fragments, and each deep rack holds \(22\) coral fragments. The facility must accommodate at least \(2{,}120\) coral fragments in total.</p>',
            r'What is the <b>minimum</b> number of deep racks \(d\) the facility must install?',
            {'A': r'\(54\)', 'B': r'\(55\)', 'C': r'\(65\)', 'D': r'\(97\)'},
            'B',
            r'Hệ bất phương trình ràng buộc:<br>\(s + d \le 120\) và \(14s + 22d \ge 2{,}120\).<br>Để tối thiểu hóa số giá sâu \(d\), ta tối đa hóa số giá nông \(s = 120 - d\) và thay vào bất phương trình số mảnh san hô:<br>\(14(120 - d) + 22d \ge 2{,}120 \Rightarrow 1{,}680 + 8d \ge 2{,}120 \Rightarrow 8d \ge 440 \Rightarrow d \ge 55\).<br>Kiểm tra: với \(d = 55, s = 65\), tổng là \(14(65) + 22(55) = 910 + 1{,}210 = 2{,}120\) mảnh (đạt chính xác!).',
            r'Với bài toán tìm giá trị nhỏ nhất của biến năng suất cao hơn (\(d\)), thay biên trên \(s = \text{Max} - d\) để chuyển về bất phương trình 1 ẩn!',
            {
                'A': ('Thiếu 8 mảnh san hô', r'Với \(d = 54, s = 66\), tối đa chỉ chứa \(14(66) + 22(54) = 2{,}112 < 2{,}120\) mảnh.'),
                'B': ('Đáp án đúng', r'\(8d \ge 440 \Rightarrow d_{\min} = 55\).'),
                'C': ('Nhầm số giá nông s', r'\(65\) là số giá nông tối đa tương ứng (\(120 - 55 = 65\)), không phải giá sâu \(d\).'),
                'D': ('Bỏ qua giá nông hoàn toàn', r'Lấy \(\lceil 2{,}120 / 22 \rceil = 97\) (giả sử không dùng giá nông nào).'),
            },
            r'Gõ `(2120 - 14*120) / (22 - 14)` trên Desmos ra ngay `55` (phương pháp giả thiết tạm: dùng toàn bộ 120 giá nông chỉ đạt 1680, thiếu 440, mỗi lần đổi 1 giá nông thành 1 giá sâu tăng thêm 8 mảnh)!'
        ),
        # Q8 — Algebra (Hard, MCQ -> A)
        math_mcq(
            'sat_mm6_m2h_q8', 8, 'Algebra', 'Linear equations in two variables', 'Hard',
            r'<p>In the \(xy\)-plane, line \(\ell\) has the equation \(5x + 3y = 36\). When line \(\ell\) is translated \(3\) units to the <b>left</b> and \(k\) units <b>downward</b>, the resulting line passes through the origin \((0, 0)\).</p>',
            r'What is the value of \(k\)?',
            {'A': r'\(7\)', 'B': r'\(-7\)', 'C': r'\(12\)', 'D': r'\(17\)'},
            'A',
            r'Khi tịnh tiến đồ thị sang <b>trái \(3\) đơn vị</b> và <b>xuống dưới \(k\) đơn vị</b>, ta thay \(x \mapsto (x + 3)\) và \(y \mapsto (y + k)\) vào phương trình gốc:<br>\(5(x + 3) + 3(y + k) = 36\).<br>Vì đường thẳng mới đi qua gốc tọa độ \((0, 0)\), thay \(x = 0, y = 0\):<br>\(5(3) + 3(k) = 36 \Rightarrow 15 + 3k = 36 \Rightarrow 3k = 21 \Rightarrow k = 7\).<br>(Cách kiểm tra trực quan: điểm gốc trên đường \(\ell\) dịch trái 3, xuống \(k\) về \((0, 0)\) chính là điểm \((3, k)\); thay \((3, k)\) vào \(5x + 3y = 36 \Rightarrow 15 + 3k = 36 \Rightarrow k = 7\)!)',
            r'Mẹo tịnh tiến ngược 3 giây: nếu hình dịch trái \(3\) và xuống \(k\) đi qua \((0, 0)\), thì hình GỐC chắc chắn đi qua điểm \((0 + 3, 0 + k) = (3, k)\)!',
            {
                'A': ('Đáp án đúng', r'Điểm \((3, k)\) thuộc đường thẳng gốc \(\Rightarrow 5(3) + 3k = 36 \Rightarrow k = 7\).'),
                'B': ('Nhầm dấu dịch chuyển dọc', r'Thay nhầm \((y - k)\) thay vì \((y + k)\) khi dịch xuống dưới, ra \(-7\).'),
                'C': ('Bỏ qua dịch chuyển ngang', r'Chỉ nhìn tung độ gốc \(y = 12\) của đường ban đầu mà quên dịch sang trái 3 đơn vị.'),
                'D': ('Nhầm dấu dịch chuyển ngang', r'Thay nhầm \((x - 3)\) thay vì \((x + 3)\) khi dịch trái: \(-15 + 3k = 36 \Rightarrow k = 17\).'),
            },
            r'Vẽ `5(x + 3) + 3(y + k) = 36` trên Desmos với thanh trượt `k` → kéo đến `k = 7` sẽ thấy đường thẳng đi xuyên chính xác qua gốc tọa độ `(0, 0)`!'
        ),
        # Q9 — Advanced Math (Hard, SPR -> 18)
        math_spr(
            'sat_mm6_m2h_q9', 9, 'Advanced Math', 'Nonlinear functions', 'Hard',
            r'<p>Following a major tectonic rupture, seismologists model the hourly aftershock energy index \(E(t)\) of a fault zone \(t\) hours after the mainshock by the exponential function:</p><p style="text-align:center;">\[E(t) = 324\left(\frac{1}{3}\right)^{t/6}\]</p>',
            r'After how many hours \(t\) does the aftershock energy index drop to \(12\)?',
            ['18'], '18',
            r'Đặt \(E(t) = 12\):<br>\(324\left(\dfrac{1}{3}\right)^{t/6} = 12 \Rightarrow \left(\dfrac{1}{3}\right)^{t/6} = \dfrac{12}{324} = \dfrac{1}{27}\).<br>Nhận thấy \(\dfrac{1}{27} = \left(\dfrac{1}{3}\right)^3\), so sánh số mũ: \(\dfrac{t}{6} = 3 \Rightarrow t = 18\) giờ.',
            r'Khi giải phương trình mũ trên SAT, luôn chia hệ số đầu \(a\) trước rồi biểu diễn tỉ số về cùng cơ số (\(\frac{1}{27} = (\frac{1}{3})^3\))!',
            r'Vẽ `y = 324 * (1/3)^(x/6)` và `y = 12` trên Desmos → bấm giao điểm đọc ngay `(18, 12)` → `t = 18`!'
        ),
        # Q10 — Advanced Math (Hard, MCQ -> C)
        math_mcq(
            'sat_mm6_m2h_q10', 10, 'Advanced Math', 'Polynomial factor & remainder theorems', 'Hard',
            r'<p>The cubic polynomial \(P(x) = 2x^3 + kx^2 - 11x - 6\), where \(k\) is a constant, is divisible by \((x - 2)\).</p>',
            r'What is the remainder when \(P(x)\) is divided by \((x + 2)\)?',
            {'A': r'\(3\)', 'B': r'\(-12\)', 'C': r'\(12\)', 'D': r'\(-32\)'},
            'C',
            r'Bước 1 (Định lý Nhân tử): Vì \(P(x)\) chia hết cho \((x - 2)\) nên \(P(2) = 0\):<br>\(2(2^3) + k(2^2) - 11(2) - 6 = 0 \Rightarrow 16 + 4k - 22 - 6 = 0 \Rightarrow 4k - 12 = 0 \Rightarrow k = 3\).<br>Bước 2 (Định lý Số dư): Số dư khi chia \(P(x) = 2x^3 + 3x^2 - 11x - 6\) cho \((x + 2)\) chính là \(P(-2)\):<br>\(P(-2) = 2(-8) + 3(4) - 11(-2) - 6 = -16 + 12 + 22 - 6 = 12\).',
            r'Khi chia cho \((x + 2) = (x - (-2))\), số dư là \(P(-2)\); đặc biệt cẩn thận dấu từng lũy thừa âm: \((-2)^3 = -8\), \((-2)^2 = +4\), \(-11(-2) = +22\)!',
            {
                'A': ('Dừng ở hằng số k', r'\(3\) mới là giá trị của \(k\), chưa tính số dư \(P(-2)\).'),
                'B': ('Sai dấu bình phương số âm', r'Tính nhầm \(3(-2)^2 = -12\) thay vì \(+12\), ra \(-16 - 12 + 22 - 6 = -12\).'),
                'C': ('Đáp án đúng', r'\(k = 3 \Rightarrow P(-2) = -16 + 12 + 22 - 6 = 12\).'),
                'D': ('Sai dấu hạng tử -11(-2)', r'Tính nhầm \(-11(-2) = -22\), ra \(-16 + 12 - 22 - 6 = -32\).'),
            },
            r'Nhập `P(x) = 2x^3 + kx^2 - 11x - 6` kèm slider `k` trên Desmos → kéo đến khi `P(2) = 0` (`k = 3`) → gõ `P(-2)` ra ngay `12`!'
        ),
        # Q11 — Advanced Math (Hard, MCQ -> D)
        math_mcq(
            'sat_mm6_m2h_q11', 11, 'Advanced Math', 'Quadratic equations — Vieta identities', 'Hard',
            r'<p>The quadratic equation \(2x^2 - 14x + c = 0\), where \(c\) is a constant, has two distinct real solutions \(r\) and \(s\) such that \((r - s)^2 = 17\).</p>',
            r'What is the value of \(c\)?',
            {'A': r'\(8\)', 'B': r'\(32\)', 'C': r'\(33\)', 'D': r'\(16\)'},
            'D',
            r'Theo định lý Viète cho \(2x^2 - 14x + c = 0\):<br>• Tổng hai nghiệm: \(r + s = -\dfrac{-14}{2} = 7\).<br>• Tích hai nghiệm: \(rs = \dfrac{c}{2}\).<br>Áp dụng hằng đẳng thức \((r - s)^2 = (r + s)^2 - 4rs\):<br>\(17 = 7^2 - 4\left(\dfrac{c}{2}\right) \Rightarrow 17 = 49 - 2c \Rightarrow 2c = 32 \Rightarrow c = 16\).<br>(Kiểm tra bằng công thức nhanh: \((r - s)^2 = \dfrac{\Delta}{a^2} = \dfrac{196 - 8c}{4} = 49 - 2c = 17 \Rightarrow c = 16\)!)',
            r'Ghi nhớ hằng đẳng thức vàng Viète: \((r - s)^2 = (r + s)^2 - 4rs = \dfrac{\Delta}{a^2}\) — giải gọn trong 10 giây mà không cần giải nghiệm căn phức tạp!',
            {
                'A': ('Dừng ở tích rs = 8', r'Tìm ra \(rs = 8\) nhưng quên nhân hệ số \(a = 2\) để ra \(c = 2rs = 16\).'),
                'B': ('Quên chia 2 ở 2c = 32', r'Giải sai \((r - s)^2 = (r + s)^2 - 2rs \Rightarrow 49 - c = 17 \Rightarrow c = 32\).'),
                'C': ('Cộng thay vì trừ 17', r'Giải nhầm \(2c = 49 + 17 = 66 \Rightarrow c = 33\).'),
                'D': ('Đáp án đúng', r'\(49 - 2c = 17 \Rightarrow c = 16\).'),
            },
            r'Gõ `y = 2x^2 - 14x + 16` trên Desmos, bấm hai nghiệm trục hoành (`1.4384` và `5.5616`) → kiểm tra `(5.5616 - 1.4384)^2 = 17.00` chuẩn xác!'
        ),
        # Q12 — Advanced Math (Hard, MCQ -> B)
        math_mcq(
            'sat_mm6_m2h_q12', 12, 'Advanced Math', 'Nonlinear systems & discriminant tangency', 'Hard',
            r'<p>In a vertical flight cross-section, a commercial delivery drone follows the parabolic climb path \(y = -2x^2 + 12x + 5\). An upper laser clearance corridor is modeled by the line \(y = 4x + k\), where \(k\) is a constant.</p>',
            r'For what value of \(k\) does the line intersect the parabolic path at <b>exactly one point</b>?',
            {'A': r'\(8\)', 'B': r'\(13\)', 'C': r'\(21\)', 'D': r'\(23\)'},
            'B',
            r'Lập phương trình hoành độ giao điểm:<br>\(-2x^2 + 12x + 5 = 4x + k \Rightarrow 2x^2 - 8x + (k - 5) = 0\).<br>Đường thẳng cắt parabol tại đúng một điểm (tiếp xúc) khi và chỉ khi \(\Delta = b^2 - 4ac = 0\):<br>\((-8)^2 - 4(2)(k - 5) = 0 \Rightarrow 64 - 8(k - 5) = 0 \Rightarrow k - 5 = 8 \Rightarrow k = 13\).<br>(Kiểm tra: \(2x^2 - 8x + 8 = 2(x - 2)^2 = 0\), tiếp điểm duy nhất là \((2, 21)\)!)',
            r'Hệ đường thẳng + parabol tiếp xúc \(\Leftrightarrow\) phương trình hoành độ giao điểm có biệt thức \(\Delta = 0\)!',
            {
                'A': ('Quên cộng lại +5', r'Giải ra \(k - 5 = 8\) nhưng chọn ngay \(8\) thay vì \(k = 13\).'),
                'B': ('Đáp án đúng', r'\(\Delta = 64 - 8(k - 5) = 0 \Rightarrow k = 13\).'),
                'C': ('Nhầm tung độ tiếp điểm', r'\(21\) là tung độ \(y\) tại điểm tiếp xúc \((2, 21)\), không phải \(k\).'),
                'D': ('Bỏ quên hạng tử 4x', r'Giải tiếp xúc với đường nằm ngang \(y = k\) (tại đỉnh parabol \(y = 23\)) thay vì \(y = 4x + k\).'),
            },
            r'Vẽ `y = -2x^2 + 12x + 5` và `y = 4x + k` trên Desmos với thanh trượt `k` → tại `k = 13`, đường thẳng chạm đúng 1 điểm `(2, 21)` vào parabol!'
        ),
        # Q13 — Advanced Math (Hard, SPR -> 44)
        math_spr(
            'sat_mm6_m2h_q13', 13, 'Advanced Math', 'Rewriting exponential functions & equivalent bases', 'Hard',
            r'<p>The total dry biomass \(M(t)\), in grams, of an experimental coral nursery reef table \(t\) years after seeding is modeled by:</p><p style="text-align:center;">\[M(t) = 125(1.728)^{2t/3}\]</p><p>This equation can be rewritten in the equivalent annual growth form \(M(t) = 125\left(1 + \dfrac{r}{100}\right)^t\), where \(r\) is a positive constant.</p>',
            r'What is the value of \(r\)?',
            ['44'], '44',
            r'Đưa lũy thừa về dạng \((\text{cơ số})^t\):<br>\((1.728)^{2t/3} = \left[(1.728)^{2/3}\right]^t\).<br>Nhận thấy \(1.728 = 1.2^3\) (vì \(12^3 = 1{,}728\)), do đó:<br>\((1.728)^{2/3} = \left(1.2^3\right)^{2/3} = 1.2^2 = 1.44\).<br>So sánh với \(1 + \dfrac{r}{100} = 1.44 \Rightarrow \dfrac{r}{100} = 0.44 \Rightarrow r = 44\).',
            r'Để quy đổi hàm mũ \(b^{kt}\) về tỉ lệ tăng hàng năm \(\left(1 + \frac{r}{100}\right)^t\), tính ngay \(b^k\), trừ đi \(1\) rồi nhân \(100\)!',
            r'Gõ thẳng `(1.728^(2/3) - 1) * 100` vào Desmos — máy tính trả ngay kết quả chính xác tuyệt đối `44` trong 2 giây!'
        ),
        # Q14 — Advanced Math (Hard 750–800 Boss, MCQ -> A)
        math_mcq(
            'sat_mm6_m2h_q14', 14, 'Advanced Math', 'Quadratic symmetry, transformations & solving', 'Hard',
            r'<p>Let \(f(x) = a(x - h)^2 + k\) be a quadratic function where \(a, h,\) and \(k\) are constants and \(a > 0\). The graph of \(y = f(x)\) in the \(xy\)-plane passes through the points \((-1, 37)\) and \((7, 37)\), and the minimum value of \(f(x)\) is \(5\). The function \(g\) is defined by \(g(x) = f(x + 2) - 10\).</p>',
            r'For what <b>positive</b> value of \(x\) is \(g(x) = 67\)?',
            {'A': r'\(7\)', 'B': r'\(6\)', 'C': r'\(9\)', 'D': r'\(11\)'},
            'A',
            r'Bước 1 (Tìm \(h, k, a\) của \(f\)):<br>• Vì \(f(-1) = f(7) = 37\), theo tính đối xứng của parabol, hoành độ đỉnh là trung điểm \(h = \dfrac{-1 + 7}{2} = 3\).<br>• Cực tiểu của \(f\) bằng \(5 \Rightarrow k = 5\). Suy ra \(f(x) = a(x - 3)^2 + 5\).<br>• Thay \((7, 37)\): \(a(7 - 3)^2 + 5 = 37 \Rightarrow 16a = 32 \Rightarrow a = 2\), vậy \(f(x) = 2(x - 3)^2 + 5\).<br>Bước 2 (Tìm \(g(x)\) bằng tịnh tiến):<br>\(g(x) = f(x + 2) - 10 = 2\left[(x + 2) - 3\right]^2 + 5 - 10 = 2(x - 1)^2 - 5\).<br>Bước 3 (Giải \(g(x) = 67\)):<br>\(2(x - 1)^2 - 5 = 67 \Rightarrow 2(x - 1)^2 = 72 \Rightarrow (x - 1)^2 = 36 \Rightarrow x - 1 = \pm 6 \Rightarrow x = 7\) hoặc \(x = -5\).<br>Nghiệm dương duy nhất là \(x = 7\).',
            r'Bài toán 750–800 kết hợp 3 kỹ năng liên tiếp: (1) dùng đối xứng \(h = \frac{x_1 + x_2}{2}\) tìm hàm \(f\), (2) áp quy tắc tịnh tiến \(f(x + 2)\) dịch TRÁI 2 đơn vị (\(h: 3 \to 1\)), và (3) giải nghiệm dương!',
            {
                'A': ('Đáp án đúng', r'\(g(x) = 2(x - 1)^2 - 5 = 67 \Rightarrow (x - 1)^2 = 36 \Rightarrow x = 7\) (do \(x > 0\)).'),
                'B': ('Quên cộng +1 từ (x - 1) = 6', r'Lấy căn \(\sqrt{36} = 6\) rồi dừng mà quên giải \(x - 1 = 6 \Rightarrow x = 7\).'),
                'C': ('Quên phép dịch chuyển ngang x + 2', r'Giải \(2(x - 3)^2 - 5 = 67 \Rightarrow x - 3 = 6 \Rightarrow x = 9\).'),
                'D': ('Dịch chuyển ngược hướng sang phải', r'Nhầm \(f(x + 2)\) làm đỉnh tăng thành \(3 + 2 = 5\), giải \(x - 5 = 6 \Rightarrow x = 11\).'),
            },
            r'Tìm `h = (-1+7)/2 = 3`, `a = (37-5)/16 = 2` → nhập `f(x) = 2(x - 3)^2 + 5`, `g(x) = f(x + 2) - 10` và `y = 67` trên Desmos → bấm giao điểm bên phải trục Oy đọc ngay `(7, 67)`!'
        ),
        # Q15 — Advanced Math (Hard 750–800 Boss, MCQ -> C)
        math_mcq(
            'sat_mm6_m2h_q15', 15, 'Advanced Math', 'Quadratic equations — integer roots & Vieta bounds', 'Hard',
            r'<p>Consider the quadratic equation below, where \(k\) is a constant:</p><p style="text-align:center;">\[2x^2 - kx + 36 = 0\]</p><p>The equation has <b>two distinct positive integer solutions</b>.</p>',
            r'What is the difference between the <b>greatest</b> possible value of \(k\) and the <b>least</b> possible value of \(k\)?',
            {'A': r'\(10\)', 'B': r'\(24\)', 'C': r'\(20\)', 'D': r'\(26\)'},
            'C',
            r'Gọi \(r\) và \(s\) là hai nghiệm nguyên dương phân biệt (\(r < s\)). Chia cả hai vế cho \(2\):<br>\(x^2 - \dfrac{k}{2}x + 18 = 0\).<br>Theo định lý Viète:<br>• Tích hai nghiệm: \(rs = \dfrac{36}{2} = 18\).<br>• Tổng hai nghiệm: \(r + s = \dfrac{k}{2} \Rightarrow k = 2(r + s)\).<br>Liệt kê tất cả các cặp ước nguyên dương phân biệt của \(18\):<br>• \((1, 18) \Rightarrow r + s = 19 \Rightarrow k = 2(19) = 38\) (lớn nhất!).<br>• \((2, 9) \Rightarrow r + s = 11 \Rightarrow k = 2(11) = 22\).<br>• \((3, 6) \Rightarrow r + s = 9 \Rightarrow k = 2(9) = 18\) (nhỏ nhất!).<br>Hiệu giữa giá trị lớn nhất và nhỏ nhất của \(k\) là \(38 - 18 = 20\).',
            r'Bẫy 780–800 kinh điển: khi \(a \ne 1\), PHẢI chia phương trình cho \(a = 2\) để tìm đúng tích \(rs = c/a = 18\) (KHÔNG phân tích ước của \(36\)), rồi nhớ nhân ngược \(k = 2(r + s)\)!',
            {
                'A': ('Quên nhân hệ số a = 2 cho k', r'Tính đúng \((1 + 18) - (3 + 6) = 19 - 9 = 10\) nhưng đó là hiệu của \(\frac{k}{2}\), chưa nhân \(2\) để ra hiệu của \(k\).'),
                'B': ('Phân tích ước của 36 thay vì 18', r'Quên chia \(a = 2\), lấy các cặp ước của \(36\) là \((1, 36)\) và \((4, 9)\) ra hiệu \(37 - 13 = 24\).'),
                'C': ('Đáp án đúng', r'\(k_{\max} = 2(1 + 18) = 38\) và \(k_{\min} = 2(3 + 6) = 18 \Rightarrow 38 - 18 = 20\).'),
                'D': ('Nhầm cận dưới từ Δ = 0', r'Lấy \(k_{\min} = 2\sqrt{36} = 12\) (không tạo nghiệm nguyên phân biệt) rồi tính \(38 - 12 = 26\).'),
            },
            r'Kiểm chứng 2 biên trên Desmos: vẽ `y = 2x^2 - 38x + 36` (nghiệm nguyên `1` và `18`) và `y = 2x^2 - 18x + 36` (nghiệm nguyên `3` và `6`) → hiệu `38 - 18 = 20`!'
        ),
        # Q16 — PSDA (Hard 750–800, SPR -> 135)
        math_spr(
            'sat_mm6_m2h_q16', 16, 'Problem-Solving and Data Analysis', 'Cubic-unit volume conversions & rates', 'Hard',
            r'<p>A commercial coral nursery filtration system circulates seawater through a deep reef raceway at a constant rate of \(45\) cubic feet per minute. <em>(\(1\text{ yard} = 3\text{ feet}\))</em></p>',
            r'How many <b>minutes</b> does it take the filtration system to circulate \(225\) <b>cubic yards</b> of seawater?',
            ['135'], '135',
            r'Bước 1 (Đổi đơn vị thể tích): Vì \(1\text{ yard} = 3\text{ feet}\), nên \(1\text{ cubic yard} = 3^3 = 27\text{ cubic feet}\).<br>Thể tích nước cần tuần hoàn tính theo \(\text{ft}^3\): \(225 \times 27 = 6{,}075\text{ ft}^3\).<br>Bước 2 (Tính thời gian): \(t = \dfrac{6{,}075\text{ ft}^3}{45\text{ ft}^3/\text{min}} = 135\text{ phút}\).<br>(Hoặc rút gọn ngay trước khi nhân: \(\dfrac{225 \times 27}{45} = 5 \times 27 = 135\).)',
            r'Với đơn vị THỂ TÍCH (\(\text{yd}^3 \to \text{ft}^3\)), luôn LẬP PHƯƠNG hệ số đổi chiều dài (\(3^3 = 27\)) — lỗi phổ biến nhất là chỉ nhân \(3\) hoặc \(3^2 = 9\)!',
            r'Gõ thẳng `(225 * 3^3) / 45` vào Desmos ra ngay `135`!'
        ),
        # Q17 — PSDA (Hard 750–800, MCQ -> D)
        math_mcq(
            'sat_mm6_m2h_q17', 17, 'Problem-Solving and Data Analysis', 'Parametric two-way tables & conditional probability', 'Hard',
            r'<p>A digital printmaking studio inspected archival prints produced on two paper stocks and classified each print as either Gallery Grade or Second Tier. The results are partially summarized in the table below, where \(m\) is a positive integer.</p>' + tbl_q17 + r'<p>If a <b>Gallery Grade</b> print is selected at random from all prints inspected, the probability that it was printed on <b>Baryta</b> paper is \(\dfrac{2}{5}\).</p>',
            r'If a print made on <b>Baryta</b> paper is selected at random, what is the probability that it is <b>Gallery Grade</b>?',
            {'A': r'\(\dfrac{3}{10}\)', 'B': r'\(\dfrac{1}{4}\)', 'C': r'\(\dfrac{2}{5}\)', 'D': r'\(\dfrac{3}{4}\)'},
            'D',
            r'Bước 1: Dùng dữ kiện \(P(\text{Baryta} \mid \text{Gallery Grade}) = \dfrac{2}{5}\) để tìm \(m\):<br>\(\dfrac{m}{135 + m} = \dfrac{2}{5} \Rightarrow 5m = 270 + 2m \Rightarrow 3m = 270 \Rightarrow m = 90\).<br>Bước 2: Tính tổng số bản in trên giấy <b>Baryta</b>: \(m + 30 = 90 + 30 = 120\).<br>Bước 3: Tính xác suất có điều kiện đề hỏi \(P(\text{Gallery Grade} \mid \text{Baryta})\):<br>\(\dfrac{90}{120} = \dfrac{3}{4}\).',
            r'Bài bảng 2 chiều ẩn tham số 750+: luôn viết rõ hai điều kiện tách biệt — điều kiện 1 cố định cột Gallery Grade để giải \(m\), điều kiện 2 cố định hàng Baryta làm mẫu số cuối cùng!',
            {
                'A': ('Bẫy tổng toàn bảng', r'Chia \(90\) cho tổng toàn bảng \(210 + 90 = 300\) ra \(\frac{90}{300} = \frac{3}{10}\).'),
                'B': ('Nhầm Second Tier thay vì Gallery Grade', r'Tính \(P(\text{Second Tier} \mid \text{Baryta}) = \frac{30}{120} = \frac{1}{4}\).'),
                'C': ('Nhầm xác suất đảo ngược đã cho', r'\(\frac{2}{5}\) là \(P(\text{Baryta} \mid \text{Gallery Grade})\), không phải \(P(\text{Gallery Grade} \mid \text{Baryta})\).'),
                'D': ('Đáp án đúng', r'\(m = 90 \Rightarrow \frac{90}{90 + 30} = \frac{90}{120} = \frac{3}{4}\).'),
            },
            r'Gõ `x / (135 + x) = 2/5` trên Desmos tìm ngay `m = 90`, rồi gõ `90 / (90 + 30)` và bấm nút phân số ra ngay `3/4`!'
        ),
        # Q18 — PSDA (Hard 750–800, MCQ -> B)
        math_mcq(
            'sat_mm6_m2h_q18', 18, 'Problem-Solving and Data Analysis', 'Comparing mean & standard deviation across shifted distributions', 'Hard',
            r'<p>A seismology institute recorded the ground vibration durations, in seconds, of \(16\) tremor events at Station Alpha and \(16\) tremor events at Station Beta, as shown in the frequency table below.</p>' + tbl_q18 + r'<p>A third data set, for Station Gamma, is created by <b>adding \(5\) seconds</b> to every duration recorded at Station Beta.</p>',
            r'Which of the following correctly compares the <b>mean</b> and <b>standard deviation</b> of Station Gamma to those of Station Alpha?',
            {
                'A': r'Station Gamma has a greater mean and a greater standard deviation than Station Alpha.',
                'B': r'Station Gamma has a greater mean and a smaller standard deviation than Station Alpha.',
                'C': r'Station Gamma has the same mean and a smaller standard deviation than Station Alpha.',
                'D': r'Station Gamma has a smaller mean and a greater standard deviation than Station Alpha.',
            },
            'B',
            r'Bước 1 (So sánh Mean): Cả Station Alpha (\(4\text{-}2\text{-}4\text{-}2\text{-}4\)) và Station Beta (\(1\text{-}3\text{-}8\text{-}3\text{-}1\)) đều đối xứng hoàn hảo quanh \(14\) giây, nên \(\bar{x}_{\text{Alpha}} = \bar{x}_{\text{Beta}} = 14\text{ s}\). Vì Station Gamma cộng thêm \(5\) giây vào mọi giá trị của Beta, nên \(\bar{x}_{\text{Gamma}} = 14 + 5 = 19\text{ s} > 14\text{ s}\) (Mean của Gamma <b>lớn hơn</b>!).<br>Bước 2 (So sánh Standard Deviation): Cộng hằng số \(+5\) vào mọi phần tử KHÔNG làm thay đổi độ lệch chuẩn, nên \(\text{SD}_{\text{Gamma}} = \text{SD}_{\text{Beta}}\). So sánh độ phân tán của Beta và Alpha: dữ liệu Beta tập trung dày đặc tại trung tâm \(14\) (\(8\) lần), trong khi dữ liệu Alpha dồn mạnh ra hai biên \(10\) và \(18\) (\(4\) lần mỗi biên). Cụ thể \(\sigma_{\text{Alpha}} = \sqrt{9} = 3\) còn \(\sigma_{\text{Gamma}} = \sigma_{\text{Beta}} = \sqrt{3.5} \approx 1.87\), nên SD của Gamma <b>nhỏ hơn</b> Alpha!',
            r'Hai nguyên lý thống kê 750+ lồng nhau: (1) cộng \(+c\) tăng Mean thêm \(c\) nhưng giữ NGUYÊN SD; (2) phân phối càng tụ sát trung tâm thì SD càng NHỎ!',
            {
                'A': ('Hiểu sai ảnh hưởng của +5 lên SD', r'Tưởng cộng thêm \(5\) giây làm tăng cả độ lệch chuẩn, hoặc nhầm cột cao ở giữa có SD lớn hơn.'),
                'B': ('Đáp án đúng', r'Mean tăng lên \(19 > 14\), còn \(\text{SD}_{\text{Gamma}} = \text{SD}_{\text{Beta}} \approx 1.87 < 3 = \text{SD}_{\text{Alpha}}\).'),
                'C': ('Quên phép cộng +5 cho Station Gamma', r'So sánh Alpha với Beta thay vì Gamma nên tưởng Mean bằng nhau.'),
                'D': ('Đảo ngược cả Mean và SD', r'Ngược cả hai chiều so sánh trung tâm và độ phân tán.'),
            },
            r'Kiểm chứng trên Desmos: gõ list `A = [10,10,10,10,12,12,14,14,14,14,16,16,18,18,18,18]`, `B = [10,12,12,12,14,14,14,14,14,14,14,14,16,16,16,18]`, `G = B + 5` → so `mean(G)=19 > mean(A)=14` và `stdevp(G)=1.87 < stdevp(A)=3`!'
        ),
        # Q19 — PSDA (Hard 750–800, SPR -> 360)
        math_spr(
            'sat_mm6_m2h_q19', 19, 'Problem-Solving and Data Analysis', 'Weighted averages of combined groups', 'Hard',
            r'<p>A commercial drone delivery network operates two dispatch hubs, East Hub and West Hub. East Hub completes \(240\) deliveries per day with a mean delivery time of \(17.5\) minutes. West Hub has a mean delivery time of \(22.5\) minutes. Across all deliveries from both hubs combined, the overall mean delivery time is \(20.5\) minutes.</p>',
            r'How many deliveries per day does West Hub complete?',
            ['360'], '360',
            r'Cách 1 (Phương trình trung bình có trọng số): Gọi \(w\) là số chuyến mỗi ngày của West Hub:<br>\(240(17.5) + 22.5w = 20.5(240 + w)\)<br>\(4{,}200 + 22.5w = 4{,}920 + 20.5w \Rightarrow 2w = 720 \Rightarrow w = 360\).<br>Cách 2 (Quy tắc đòn bẩy 5 giây): Khoảng cách trung bình chung tới East Hub là \(20.5 - 17.5 = 3.0\), tới West Hub là \(22.5 - 20.5 = 2.0\). Tỉ số số chuyến nghịch đảo tỉ số khoảng cách: \(\dfrac{w}{240} = \dfrac{3.0}{2.0} = \dfrac{3}{2} \Rightarrow w = 360\).',
            r'Quy tắc đòn bẩy (Weighted Average Lever): nhóm nào càng gần trung bình chung thì có quy mô LỚN hơn theo đúng tỉ lệ nghịch khoảng cách!',
            r'Gõ `(240*17.5 + 22.5x) / (240 + x) = 20.5` trên Desmos (thu nhỏ trục hoành tới 400) sẽ thấy ngay đường thẳng đứng tại `x = 360`!'
        ),
        # Q20 — Geometry & Trig (Hard 750–800, MCQ -> A)
        math_mcq(
            'sat_mm6_m2h_q20', 20, 'Geometry and Trigonometry', 'Circles in the xy-plane — completing the square', 'Hard',
            r'<p>In the \(xy\)-plane, the circular foundation ring of an astronomical observatory dome is represented by the equation below, where \(c\) is a constant:</p><p style="text-align:center;">\[3x^2 + 3y^2 - 18x + 24y + c = 0\]</p><p>The <b>circumference</b> of this circular ring is \(12\pi\) units.</p>',
            r'What is the value of \(c\)?',
            {'A': r'\(-33\)', 'B': r'\(-11\)', 'C': r'\(33\)', 'D': r'\(-357\)'},
            'A',
            r'Bước 1 (Tìm bán kính từ chu vi): \(2\pi r = 12\pi \Rightarrow r = 6 \Rightarrow r^2 = 36\).<br>Bước 2 (Chia cả phương trình cho \(3\)):<br>\(x^2 - 6x + y^2 + 8y + \dfrac{c}{3} = 0\).<br>Bước 3 (Hoàn thành bình phương):<br>\((x - 3)^2 - 9 + (y + 4)^2 - 16 + \dfrac{c}{3} = 0 \Rightarrow (x - 3)^2 + (y + 4)^2 = 25 - \dfrac{c}{3}\).<br>Đặt vế phải bằng \(r^2 = 36\):<br>\(25 - \dfrac{c}{3} = 36 \Rightarrow -\dfrac{c}{3} = 11 \Rightarrow c = -33\).',
            r'Bộ ba bẫy 750+ phương trình đường tròn: (1) rút đúng \(r = \frac{C}{2\pi} = 6\) (không lấy \(12\)), (2) chia cả hằng số \(c\) cho hệ số \(3\), và (3) giữ cẩn thận dấu âm của \(c = -33\)!',
            {
                'A': ('Đáp án đúng', r'\(r = 6 \Rightarrow 25 - \frac{c}{3} = 36 \Rightarrow c = -33\).'),
                'B': ('Quên chia c cho 3', r'Chia hệ số \(x, y\) cho \(3\) nhưng quên chia \(c\) cho \(3\), giải \(25 - c = 36 \Rightarrow c = -11\).'),
                'C': ('Sai dấu khi chuyển vế', r'Viết nhầm \(25 + \frac{c}{3} = 36\) nên ra \(c = +33\).'),
                'D': ('Nhầm chu vi 12π thành r = 12', r'Đặt \(25 - \frac{c}{3} = 12^2 = 144 \Rightarrow c = -357\).'),
            },
            r'Vẽ `3x^2 + 3y^2 - 18x + 24y + c = 0` trên Desmos kèm slider `c` (từ `-50` đến `50`); đặt `c = -33` rồi bấm đỉnh trên `(3, 2)` và đáy `(3, -10)` thấy đường kính `12` → chu vi `12π`!'
        ),
        # Q21 — Geometry & Trig (Hard 750–800, MCQ -> C)
        math_mcq(
            'sat_mm6_m2h_q21', 21, 'Geometry and Trigonometry', 'Right triangles, trigonometry & conical surface area', 'Hard',
            f'<div style="text-align:center;margin-bottom:10px;">{svg_q21}</div>' + r'<p>The roof of a mountain observatory is shaped like a right circular cone whose axial right-triangle cross-section \(\triangle VOP\) (\(\angle O = 90^\circ\)) is shown above, where \(VO = h\) is the height, \(OP = r\) is the base radius, and \(VP = s\) is the slant height. It is given that \(\sin(\alpha) = \dfrac{8}{17}\) and the area of the circular base of the cone is \(256\pi\) square meters.</p>',
            r'What is the <b>lateral surface area</b> (the curved side only, given by \(\pi r s\)) of the conical roof, in square meters?',
            {'A': r'\(480\pi\)', 'B': r'\(272\pi\)', 'C': r'\(544\pi\)', 'D': r'\(800\pi\)'},
            'C',
            r'Bước 1 (Tìm bán kính đáy \(r\)): Diện tích đáy tròn \(\pi r^2 = 256\pi \Rightarrow r = \sqrt{256} = 16\text{ m}\).<br>Bước 2 (Dùng lượng giác tìm đường sinh \(s\)): Trong \(\triangle VOP\) vuông tại \(O\), cạnh đối của góc \(\alpha = \angle V\) là bán kính \(OP = r\) và cạnh huyền là đường sinh \(VP = s\):<br>\(\sin(\alpha) = \dfrac{r}{s} = \dfrac{8}{17} \Rightarrow \dfrac{16}{s} = \dfrac{8}{17} \Rightarrow s = 34\text{ m}\).<br>(Chiều cao nón là \(h = 30\text{ m}\) theo bộ ba \(8\text{–}15\text{–}17\) nhân \(2\).)<br>Bước 3 (Tính diện tích xung quanh): \(\text{LSA} = \pi r s = \pi(16)(34) = 544\pi\text{ m}^2\).',
            r'Luôn xác định đúng cạnh đối/kề/huyền của góc \(\alpha\) trên đỉnh nón: \(\sin(\alpha) = \dfrac{r}{s}\), và công thức diện tích xung quanh hình nón dùng ĐƯỜNG SINH \(s\) (\(\pi r s\)), KHÔNG dùng chiều cao \(h\)!',
            {
                'A': ('Dùng nhầm chiều cao h thay vì đường sinh s', r'Tính \(\pi r h = \pi(16)(30) = 480\pi\) thay vì \(\pi r s\).'),
                'B': ('Chia đôi nhầm công thức', r'Tính nhầm \(\frac{1}{2}\pi r s = 272\pi\) (hoặc dùng \(r = 8\) thay vì \(16\)).'),
                'C': ('Đáp án đúng', r'\(r = 16, s = 34 \Rightarrow \pi r s = 544\pi\).'),
                'D': ('Tính nhầm Diện tích toàn phần', r'Cộng thêm diện tích đáy \(544\pi + 256\pi = 800\pi\), trong khi đề chỉ hỏi lateral surface area.'),
            },
            r'Gõ lần lượt `r = sqrt(256)` (`16`), `s = r / (8/17)` (`34`), và `r * s` trên Desmos ra ngay `544` → `544π`!'
        ),
        # Q22 — Geometry & Trig (Hard 750–800 Boss, SPR -> 1944)
        math_spr(
            'sat_mm6_m2h_q22', 22, 'Geometry and Trigonometry', '3D composite solids — surface area, volume & similarity scaling', 'Hard',
            f'<div style="text-align:center;margin-bottom:10px;">{svg_q22}</div>' + r'<p>Observatory Tower 1 consists of a right circular cylindrical wall of base radius \(r\) meters and height \(h\) meters topped by a hemispherical dome of the same radius \(r\) meters. The exterior curved surface area of the hemispherical dome (\(2\pi r^2\)) is equal to \(\dfrac{1}{2}\) of the lateral curved surface area of the cylindrical wall (\(2\pi rh\)), and the volume of the cylindrical section alone is \(432\pi\) cubic meters.</p><p>Observatory Tower 2 is <b>geometrically similar</b> to Tower 1 and has a combined exterior curved surface area (cylindrical wall plus hemispherical dome) of \(486\pi\) square meters.</p>',
            r'If the combined interior volume (cylindrical section plus hemispherical dome) of <b>Observatory Tower 2</b> is \(v\pi\) cubic meters, what is the value of \(v\)?',
            ['1944'], '1944',
            r'Bước 1 (Tìm \(r\) và \(h\) của Tower 1):<br>• Từ tỉ lệ diện tích: \(2\pi r^2 = \dfrac{1}{2}(2\pi rh) \Rightarrow h = 2r\).<br>• Thể tích phần trụ: \(\pi r^2 h = \pi r^2(2r) = 2\pi r^3 = 432\pi \Rightarrow r^3 = 216 \Rightarrow r = 6\text{ m}\), và \(h = 12\text{ m}\).<br>Bước 2 (Tính diện tích mặt cong và tổng thể tích Tower 1):<br>• Tổng diện tích mặt cong ngoài Tower 1: \(2\pi r^2 + 2\pi rh = 2\pi(36) + 2\pi(6)(12) = 72\pi + 144\pi = 216\pi\text{ m}^2\).<br>• Tổng thể tích Tower 1 (trụ + bán cầu \(\frac{2}{3}\pi r^3\)): \(432\pi + \dfrac{2}{3}\pi(216) = 432\pi + 144\pi = 576\pi\text{ m}^3\).<br>Bước 3 (Phóng đại đồng dạng sang Tower 2):<br>• Tỉ số diện tích: \(k^2 = \dfrac{486\pi}{216\pi} = \dfrac{9}{4} \Rightarrow\) tỉ số cạnh tuyến tính \(k = \dfrac{3}{2}\).<br>• Tỉ số thể tích: \(k^3 = \left(\dfrac{3}{2}\right)^3 = \dfrac{27}{8}\).<br>• Tổng thể tích Tower 2: \(V_2 = 576\pi \times \dfrac{27}{8} = 72 \times 27\pi = 1{,}944\pi \Rightarrow v = 1{,}944\).',
            r'Câu Boss 800 chuẩn Bluebook: kết nối chuỗi \(h = 2r \to r = 6 \to (\text{SA}_1 = 216\pi, V_1 = 576\pi) \to k^2 = \frac{486}{216} = \frac{9}{4} \to k^3 = \frac{27}{8} \to V_2 = 1{,}944\pi\)! Nhớ thể tích BÁN cầu là \(\frac{2}{3}\pi r^3\) (một nửa hình cầu \(\frac{4}{3}\pi r^3\)).',
            r'Kiểm chứng siêu gọn trên Desmos: `r = (432/2)^(1/3)` (`6`), `sa1 = 2*r^2 + 2*r*(2r)` (`216`), `v1 = 432 + (2/3)*r^3` (`576`), rồi `v1 * (sqrt(486/sa1))^3` trả ngay `1944`!'
        ),
    ]


if __name__ == '__main__':
    assert verify_math()
    qs = get_m2h_questions()
    print(f"M2H verified: {len(qs)} questions")
