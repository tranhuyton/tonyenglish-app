# -*- coding: utf-8 -*-
"""
Digital SAT Math Adaptive Mock Test #8 — Module 2 Hard (650–800 Band, 22 Questions)
Themes: Geothermal Power Wells, Autonomous Warehouse Conveyor Robotics,
        Violin Luthier Acoustics & Wood Curing, National Park Wildlife Census & Tagging,
        Stepped-Pyramid & Truncated-Cone Monument Geometry.
Blueprint: 8 Algebra (Q1-Q8), 7 Advanced Math (Q9-Q15), 4 PSDA (Q16-Q19), 3 Geometry/Trig (Q20-Q22).
Format: 16 MCQ (A:4, B:4, C:4, D:4) + 6 SPR (Q5, Q9, Q13, Q16, Q19, Q22).
Bosses: Q14–Q22 target true 750–800 parametric, multi-step, and 3D-scaling mastery.
"""

from fractions import Fraction
import math
from sat_math_helpers import (
    math_mcq, math_spr, build_math_table,
    svg_circle_sector, svg_right_triangle
)


def _svg_truncated_cone_monument():
    return '''<svg viewBox="0 0 270 205" width="270" height="205" xmlns="http://www.w3.org/2000/svg" style="background:#f8fafc;border:1px solid #e2e8f0;border-radius:12px;">
  <line x1="125" y1="22" x2="85" y2="114" stroke="#94a3b8" stroke-width="1.6" stroke-dasharray="4 3"/>
  <line x1="125" y1="22" x2="165" y2="114" stroke="#94a3b8" stroke-width="1.6" stroke-dasharray="4 3"/>
  <circle cx="125" cy="22" r="2.5" fill="#64748b"/>
  <path d="M 85 114 L 65 160 A 60 16 0 0 0 185 160 L 165 114 Z" fill="#eff6ff" stroke="#1e3a8a" stroke-width="2.2" stroke-linejoin="round"/>
  <ellipse cx="125" cy="114" rx="40" ry="12" fill="#dbeafe" stroke="#1e3a8a" stroke-width="2.2"/>
  <path d="M 65 160 A 60 16 0 0 1 185 160" fill="none" stroke="#1e3a8a" stroke-width="1.4" stroke-dasharray="4 3"/>
  <line x1="125" y1="114" x2="165" y2="114" stroke="#b91c1c" stroke-width="2"/>
  <circle cx="125" cy="114" r="2.4" fill="#0f172a"/>
  <text x="136" y="109" font-family="sans-serif" font-size="11.5" font-weight="700" fill="#b91c1c">r = 8 m</text>
  <line x1="125" y1="160" x2="185" y2="160" stroke="#b91c1c" stroke-width="2"/>
  <circle cx="125" cy="160" r="2.4" fill="#0f172a"/>
  <text x="142" y="155" font-family="sans-serif" font-size="11.5" font-weight="700" fill="#b91c1c">R = 12 m</text>
  <line x1="202" y1="114" x2="202" y2="160" stroke="#047857" stroke-width="2"/>
  <line x1="196" y1="114" x2="208" y2="114" stroke="#047857" stroke-width="1.8"/>
  <line x1="196" y1="160" x2="208" y2="160" stroke="#047857" stroke-width="1.8"/>
  <text x="213" y="141" font-family="sans-serif" font-size="12" font-weight="700" fill="#047857">h = 9 m</text>
  <text x="135" y="196" text-anchor="middle" font-family="sans-serif" font-size="10.5" fill="#64748b">Truncated-Cone Monument (dashed cone removed)</text>
</svg>'''


def verify_math():
    """Programmatic exact arithmetic verification for all 22 Module 2 Hard questions."""
    # Q1: (2/5)x - (3/4)y = 6, ax + 15y = b infinitely many => k = -20 => a = -8, b = -120 => a - b = 112
    k1 = Fraction(15, 1) / Fraction(-3, 4)
    a1 = Fraction(2, 5) * k1
    b1 = 6 * k1
    assert k1 == -20 and a1 == -8 and b1 == -120 and a1 - b1 == 112

    # Q2: f(x) - 9 has (3, 3), (7, 23), (13, 53) => f(x) has (3, 12), (7, 32), (13, 62) => f(x) = 5x - 3 => x-int = 3/5
    for xv, yv in [(3, 12), (7, 32), (13, 62)]:
        assert 5 * xv - 3 == yv
    assert 5 * Fraction(3, 5) - 3 == 0

    # Q3: l1 through (2, -5) and (6, 7) => m1 = 3; l2: kx + 9y = 21 => m2 = -k/9; perp => k = 3
    m3_1 = Fraction(7 - (-5), 6 - 2)
    k3 = Fraction(9, m3_1)
    assert m3_1 == 3 and k3 == 3 and m3_1 * Fraction(-k3, 9) == -1

    # Q4: 2|4x - 9| - c = 14, diff of roots = 5 => |4x - 9| = 10 => (14 + c)/2 = 10 => c = 6
    d4 = Fraction(5 * 4, 2)
    c4 = 2 * d4 - 14
    r4_1 = Fraction(9 + d4, 4)
    r4_2 = Fraction(9 - d4, 4)
    assert c4 == 6 and r4_1 - r4_2 == 5
    assert 2 * abs(4 * r4_1 - 9) - c4 == 14 and 2 * abs(4 * r4_2 - 9) - c4 == 14

    # Q5 (SPR): e + b <= 90, 3.5e + 2.0b >= 264 => 1.5e + 180 >= 264 => e >= 56
    min_e5 = (Fraction(264) - 2 * 90) / (Fraction(7, 2) - 2)
    assert min_e5 == 56
    assert Fraction(7, 2) * 56 + 2 * 34 == 264
    assert Fraction(7, 2) * 55 + 2 * 35 < 264

    # Q6: y < -2x - 6 and y < 3x - 11 => vertex (1, -8), y < -8 < 0 => Q-I & Q-II empty
    x6 = Fraction(11 - 6, 3 + 2)
    y6 = -2 * x6 - 6
    assert x6 == 1 and y6 == 3 * x6 - 11 == -8 < 0
    assert (-20 < -2 * (-1) - 6 and -20 < 3 * (-1) - 11)  # Q-III has solution
    assert (-20 < -2 * 1 - 6 and -20 < 3 * 1 - 11)        # Q-IV has solution

    # Q7: f(x) = mx + b (m < 0), f(f(x)) = 16x + 15 => m = -4, b = -5 => f(-2) = 3
    m7 = -4
    b7 = Fraction(15, m7 + 1)
    assert m7 < 0 and m7 ** 2 == 16 and b7 == -5
    for xv in (-3, 0, 4):
        assert m7 * (m7 * xv + b7) + b7 == 16 * xv + 15
    assert m7 * (-2) + b7 == 3

    # Q8: 4(2 - n) < 3n + 43 => -7n < 35 => n > -5 => min integer n = -4 => 5(-4) + 9 = -11
    assert 4 * (2 - (-4)) < 3 * (-4) + 43
    assert not (4 * (2 - (-5)) < 3 * (-5) + 43)
    assert 5 * (-4) + 9 == -11

    # Q9 (SPR): 243 * (1/3)^(t/4) = 9 => (1/3)^(t/4) = 1/27 = (1/3)^3 => t = 12
    assert Fraction(243, 3 ** (12 // 4)) == 9

    # Q10: P(x) = 2x^3 + kx^2 - 11x - 10, P(2) = 0 => k = 4 => P(-2) = 12
    k10 = Fraction(-(2 * 8 - 11 * 2 - 10), 4)
    p10 = lambda x: 2 * x ** 3 + k10 * x ** 2 - 11 * x - 10
    assert k10 == 4 and p10(2) == 0 and p10(-2) == 12

    # Q11: 2x^2 + 5x + 11 = -3x + c => 2x^2 + 8x + (11 - c) = 0, Delta = 0 => c = 3
    c11 = 11 - Fraction(8 ** 2, 4 * 2)
    assert c11 == 3 and 8 ** 2 - 4 * 2 * (11 - c11) == 0

    # Q12: 2x^2 - 14x + k = 0, |r - s| = 5 => (r + s)^2 - 4rs = 25 => 49 - 2k = 25 => k = 12
    s12 = Fraction(14, 2)
    k12 = Fraction(s12 ** 2 - 25, 2)
    assert k12 == 12 and 2 * 1 ** 2 - 14 * 1 + k12 == 0 and 2 * 6 ** 2 - 14 * 6 + k12 == 0 and abs(6 - 1) == 5

    # Q13 (SPR): (1.5625)^(1/2) = 1.25 => r = 25
    assert Fraction(5, 4) ** 2 == Fraction(15625, 10000)
    assert (Fraction(5, 4) - 1) * 100 == 25

    # Q14 (Boss): (px + q)(rx + s) = 18x^2 + kx + 20, pos ints, p + r = 9 => max k = 123
    k_vals = []
    for p in range(1, 19):
        if 18 % p == 0:
            r = 18 // p
            if p + r == 9:
                for q in range(1, 21):
                    if 20 % q == 0:
                        s = 20 // q
                        k_vals.append(p * s + q * r)
    assert max(k_vals) == 123

    # Q15 (Boss): A(t) = c * b^t + 8, A(0) = 72, A(3) = 16 => c = 64, b = 1/2 => A(2) = 24
    c15 = 72 - 8
    b15_cubed = Fraction(16 - 8, c15)
    b15 = Fraction(1, 2)
    assert c15 == 64 and b15 ** 3 == b15_cubed
    assert c15 * (b15 ** 2) + 8 == 24

    # Q16 (SPR Boss): 540 ft^3/min -> 20 yd^3/min -> 1200 yd^3/hr => 43200 / 1200 = 36 hrs
    rate_yd3_hr = Fraction(540, 3 ** 3) * 60
    assert rate_yd3_hr == 1200 and Fraction(43200, rate_yd3_hr) == 36

    # Q17 (Boss): P(Juvenile | South Valley) = k/(k + 135) = 1/4 => k = 45 => P(South Valley | Juvenile) = 45/105 = 3/7
    k17 = Fraction(135, 3)
    assert k17 == 45 and Fraction(k17, k17 + 135) == Fraction(1, 4)
    assert Fraction(k17, 60 + k17) == Fraction(3, 7)

    # Q18 (Boss): frequencies 40:6, 50:8, 60:m, 70:5 => greatest int m with median == 50 is 8
    def _median_for_m(m):
        arr = [40] * 6 + [50] * 8 + [60] * m + [70] * 5
        n = len(arr)
        if n % 2 == 1:
            return Fraction(arr[n // 2])
        return Fraction(arr[n // 2 - 1] + arr[n // 2], 2)

    valid_m = [m for m in range(1, 25) if _median_for_m(m) == 50]
    assert max(valid_m) == 8 and _median_for_m(8) == 50 and _median_for_m(9) == 55

    # Q19 (SPR Boss): Alpha Q1 = 1.5*B, Q2 Alpha +40%, Beta -15% => combined increase = 18%
    q1_tot = Fraction(3, 2) + 1
    q2_tot = Fraction(3, 2) * Fraction(140, 100) + Fraction(85, 100)
    pct_inc19 = (q2_tot - q1_tot) / q1_tot * 100
    assert pct_inc19 == 18

    # Q20 (Boss): sector arc = 10pi, area = 90pi => r = 18, angle = 100 deg
    r20 = Fraction(2 * 90, 10)
    deg20 = Fraction(10, 2 * r20) * 360
    assert r20 == 18 and deg20 == 100
    assert Fraction(deg20, 360) * (r20 ** 2) == 90 and Fraction(deg20, 360) * (2 * r20) == 10

    # Q21 (Boss): right triangle sin(A) = 7/25, perimeter = 168 => sides 21, 72, 75 => area = 756
    assert 7 ** 2 + 24 ** 2 == 25 ** 2
    scale21 = Fraction(168, 7 + 24 + 25)
    area21 = Fraction(1, 2) * (7 * scale21) * (24 * scale21)
    assert scale21 == 3 and area21 == 756

    # Q22 (SPR Boss): truncated cone R = 12, r = 8, h = 9 => top cone h_top = 18, H = 27 => V = 912pi
    h_top22 = Fraction(8 * 9, 12 - 8)
    H22 = h_top22 + 9
    v_full = Fraction(1, 3) * (12 ** 2) * H22
    v_top = Fraction(1, 3) * (8 ** 2) * h_top22
    v_frustum = v_full - v_top
    v_formula = Fraction(1, 3) * 9 * (12 ** 2 + 12 * 8 + 8 ** 2)
    assert h_top22 == 18 and H22 == 27 and v_frustum == v_formula == 912

    return True


def get_m2h_questions():
    tbl_q2 = build_math_table(
        ['\\(x\\)', '\\(f(x) - 9\\)'],
        [['3', '3'], ['7', '23'], ['13', '53']],
        caption='Geothermal Borehole Calibration Offset Table'
    )
    tbl_q17 = build_math_table(
        ['Park Sector', 'Juvenile', 'Adult', 'Total'],
        [
            ['North Ridge', '60', '90', '150'],
            ['South Valley', 'k', '135', 'k + 135'],
            ['Total', '60 + k', '225', '285 + k'],
        ],
        caption='National Park Bighorn Sheep Census by Age Class'
    )
    tbl_q18 = build_math_table(
        ['Daily Conveyor Cycles', 'Number of Robots'],
        [
            ['40', '6'],
            ['50', '8'],
            ['60', 'm'],
            ['70', '5'],
        ],
        caption='Autonomous Warehouse Conveyor Robot Throughput Distribution'
    )
    svg_q20 = svg_circle_sector(
        'r', 'θ', center_lbl='O', pt_a='A', pt_b='B',
        note='Monument Plaza Sector (not to scale)'
    )
    svg_q21 = svg_right_triangle(
        'AB', 'BC', 'AC', angle_top_left='A', angle_bottom_right='C',
        v_top='A', v_right_angle='B', v_right='C',
        note='Stepped-Pyramid Brace Cross-Section (not to scale)'
    )
    svg_q22 = _svg_truncated_cone_monument()

    return [
        # Q1 — Algebra (Hard, MCQ -> B)
        math_mcq(
            'sat_mm8_m2h_q1', 1, 'Algebra', 'Systems of two linear equations in two variables', 'Hard',
            r'<p>In the system of linear equations below, \(a\) and \(b\) are constants:</p><p style="text-align:center;">\[\begin{cases} \dfrac{2}{5}x - \dfrac{3}{4}y = 6 \\ ax + 15y = b \end{cases}\]</p>',
            r'If the system has <b>infinitely many solutions</b>, what is the value of \(a - b\)?',
            {'A': r'\(-128\)', 'B': r'\(112\)', 'C': r'\(-112\)', 'D': r'\(128\)'},
            'B',
            r'Hệ có vô số nghiệm khi phương trình thứ hai là bội số hằng \(k\) của phương trình thứ nhất. So hệ số của \(y\): \(k \cdot \left(-\frac{3}{4}\right) = 15 \Rightarrow k = 15 \cdot \left(-\frac{4}{3}\right) = -20\). Nhân \(-20\) vào hai hệ số còn lại: \(a = (-20)\left(\frac{2}{5}\right) = -8\) và \(b = (-20)(6) = -120\). Vậy \(a - b = -8 - (-120) = 112\).',
            r'Tìm hệ số tỉ lệ \(k\) từ cặp biến đã biết cả hai hệ số (\(y\)), rồi chú ý dấu trừ kép khi tính \(a - b = -8 - (-120) = 112\)!',
            {
                'A': ('Computed a + b Instead of a - b', r'\(-8 + (-120) = -128\), đọc nhầm phép trừ thành phép cộng.'),
                'B': ('Correct', r'\(k = -20 \Rightarrow a = -8, b = -120 \Rightarrow a - b = 112\).'),
                'C': ('Reversed Subtraction Order', r'Tính ngược \(b - a = -120 - (-8) = -112\).'),
                'D': ('Sign Error on a', r'Quên dấu âm của \(k\) khi tính \(a = +8\), ra \(8 - (-120) = 128\).'),
            },
            r'Tính hệ số tỉ lệ `k = 15 / (-3/4)` (`-20`) trên Desmos, sau đó tính `(2/5)*(-20) - 6*(-20)` ra ngay `112`!'
        ),
        # Q2 — Algebra (Hard, MCQ -> D) | Theme: Geothermal Power Wells (Table)
        math_mcq(
            'sat_mm8_m2h_q2', 2, 'Algebra', 'Linear functions', 'Hard',
            tbl_q2 + r'<p>A geothermal drilling monitor records the shifted output \(f(x) - 9\) for three borehole depths \(x\), where \(f\) is a linear function.</p>',
            r'What is the \(x\)-intercept of the graph of \(y = f(x)\) in the \(xy\)-plane?',
            {'A': r'\(\left(\frac{12}{5}, 0\right)\)', 'B': r'\((0, -3)\)', 'C': r'\(\left(-\frac{3}{5}, 0\right)\)', 'D': r'\(\left(\frac{3}{5}, 0\right)\)'},
            'D',
            r'Khôi phục giá trị thật của \(f(x)\) bằng cách <b>cộng thêm \(9\)</b> vào cột phải: \((3, 12)\), \((7, 32)\), \((13, 62)\). Hệ số góc: \(m = \frac{32 - 12}{7 - 3} = \frac{20}{4} = 5\). Suy ra \(f(x) = 5(x - 3) + 12 = 5x - 3\). Đặt \(f(x) = 0 \Rightarrow 5x - 3 = 0 \Rightarrow x = \frac{3}{5}\). Vậy \(x\)-intercept là \(\left(\frac{3}{5}, 0\right)\).',
            r'Gặp bảng cho \(f(x) - 9\), PHẢI cộng ngược \(+9\) để khôi phục \(f(x)\) trước khi giải \(f(x) = 0\)!',
            {
                'A': ('Forgot to Restore +9 Shift', r'Tìm nghiệm của \(f(x) - 9 = 5x - 12 = 0 \Rightarrow x = \frac{12}{5}\).'),
                'B': ('y-Intercept Instead of x-Intercept', r'\((0, -3)\) là giao điểm trục \(Oy\), trong khi đề hỏi giao điểm trục \(Ox\).'),
                'C': ('Sign Error Solving 5x - 3 = 0', r'Chuyển vế sai dấu thành \(x = -\frac{3}{5}\).'),
                'D': ('Correct', r'\(f(x) = 5x - 3 = 0 \Rightarrow \left(\frac{3}{5}, 0\right)\).'),
            },
            r'Nhập bảng `x1 = [3, 7, 13]`, `y1 = [12, 32, 62]` trên Desmos → gõ `y1 ~ m x1 + b` → bấm giao điểm trục Ox đọc ngay `(0.6, 0) = (3/5, 0)`.'
        ),
        # Q3 — Algebra (Hard, MCQ -> A)
        math_mcq(
            'sat_mm8_m2h_q3', 3, 'Algebra', 'Linear equations in two variables', 'Hard',
            r'<p>In the \(xy\)-plane, line \(\ell_1\) passes through the points \((2, -5)\) and \((6, 7)\). Line \(\ell_2\) is defined by \(kx + 9y = 21\), where \(k\) is a constant. Line \(\ell_1\) is <b>perpendicular</b> to line \(\ell_2\).</p>',
            r'What is the value of \(k\)?',
            {'A': r'\(3\)', 'B': r'\(-3\)', 'C': r'\(-27\)', 'D': r'\(27\)'},
            'A',
            r'Bước 1: Tính hệ số góc của \(\ell_1\): \(m_1 = \frac{7 - (-5)}{6 - 2} = \frac{12}{4} = 3\).<br>Bước 2: Đường vuông góc \(\ell_2\) phải có hệ số góc \(m_2 = -\frac{1}{3}\).<br>Bước 3: Từ \(kx + 9y = 21\), hệ số góc của \(\ell_2\) là \(m_2 = -\frac{k}{9}\). Đặt \(-\frac{k}{9} = -\frac{1}{3} \Rightarrow k = 3\).',
            r'Đường thẳng \(Ax + By = C\) luôn có hệ số góc \(-A/B\); hai đường vuông góc khi tích hai hệ số góc bằng \(-1\).',
            {
                'A': ('Correct', r'\(m_1 = 3\) và \(m_2 = -\frac{3}{9} = -\frac{1}{3} \Rightarrow m_1 m_2 = -1\).'),
                'B': ('Sign Error on Slope -A/B', r'Quên dấu trừ ở \(m_2 = -k/9\) nên giải ra \(k = -3\).'),
                'C': ('Parallel Instead of Perpendicular', r'Đặt \(-\frac{k}{9} = 3 \Rightarrow k = -27\) (điều kiện song song).'),
                'D': ('Parallel + Sign Error', r'Đặt \(\frac{k}{9} = 3 \Rightarrow k = 27\).'),
            },
            r'Tính `m1 = (7 - (-5))/(6 - 2) = 3` trên Desmos, sau đó vẽ `y = 3(x - 2) - 5` và `kx + 9y = 21` với thanh trượt `k = 3` để kiểm chứng góc vuông.'
        ),
        # Q4 — Algebra (Hard, MCQ -> C)
        math_mcq(
            'sat_mm8_m2h_q4', 4, 'Algebra', 'Linear equations in one variable', 'Hard',
            r'<p>Consider the absolute value equation below, where \(c\) is a constant:</p><p style="text-align:center;">\[2|4x - 9| - c = 14\]</p><p>The positive difference between the two real solutions to this equation is \(5\).</p>',
            r'What is the value of \(c\)?',
            {'A': r'\(-4\)', 'B': r'\(16\)', 'C': r'\(6\)', 'D': r'\(26\)'},
            'C',
            r'Cô lập giá trị tuyệt đối: \(|4x - 9| = \frac{14 + c}{2}\). Đặt \(d = \frac{14 + c}{2} > 0\). Hai nghiệm là \(x_1 = \frac{9 + d}{4}\) và \(x_2 = \frac{9 - d}{4}\). Hiệu dương giữa hai nghiệm bằng \(x_1 - x_2 = \frac{2d}{4} = \frac{d}{2}\). Theo đề bài: \(\frac{d}{2} = 5 \Rightarrow d = 10\). Suy ra \(\frac{14 + c}{2} = 10 \Rightarrow 14 + c = 20 \Rightarrow c = 6\).',
            r'Mẹo nhanh: Khoảng cách giữa hai nghiệm của \(|ax - b| = d\) luôn bằng \(\frac{2d}{|a|}\) (độc lập hoàn toàn với hằng số \(b\))!',
            {
                'A': ('Missed Factor of 2 in Root Span', r'Đặt nhầm \(d = 5\) thay vì \(\frac{d}{2} = 5\), giải \(\frac{14 + c}{2} = 5 \Rightarrow c = -4\).'),
                'B': ('Sign Reversal on -c', r'Viết nhầm \(|4x - 9| = \frac{14 - c}{2}\) hoặc giải sai dấu ra \(16\).'),
                'C': ('Correct', r'\(d = 10 \Rightarrow 14 + c = 20 \Rightarrow c = 6\) (hai nghiệm là \(4.75\) và \(-0.25\), hiệu bằng \(5\)).'),
                'D': ('Doubled d by Mistake', r'Giải nhầm \(\frac{d}{4} = 5 \Rightarrow d = 20 \Rightarrow c = 26\).'),
            },
            r'Vẽ `y = 2|4x - 9| - c` và `y = 14` với thanh trượt `c`; tại `c = 6`, hai giao điểm là `(-0.25, 14)` và `(4.75, 14)` có khoảng cách đúng `5`!'
        ),
        # Q5 — Algebra (Hard, SPR -> 56) | Theme: Warehouse Conveyor Robotics
        math_spr(
            'sat_mm8_m2h_q5', 5, 'Algebra', 'Linear inequalities in one or two variables', 'Hard',
            r'<p>During a night shift, an autonomous warehouse conveyor system processes \(e\) Express sorting units and \(b\) Bulk sorting units. The system can handle at most \(90\) total units per shift (\(e + b \le 90\)). Each Express unit contributes \(3.5\) throughput points and each Bulk unit contributes \(2.0\) throughput points. To meet its service quota, the system must achieve at least \(264\) total throughput points.</p>',
            r'What is the <b>minimum</b> number of Express sorting units (\(e\)) the system must process to satisfy both constraints?',
            ['56'], '56',
            r'Hệ bất phương trình: \(e + b \le 90 \Rightarrow b \le 90 - e\), và \(3.5e + 2.0b \ge 264\). Để tối thiểu hóa \(e\) mà vẫn đạt ít nhất \(264\) điểm, ta đẩy \(b\) lên tối đa \(b = 90 - e\): \(3.5e + 2.0(90 - e) \ge 264 \Rightarrow 1.5e + 180 \ge 264 \Rightarrow 1.5e \ge 84 \Rightarrow e \ge \frac{84}{1.5} = 56\). Kiểm tra tại \((56, 34)\): \(3.5(56) + 2(34) = 196 + 68 = 264\) (thỏa mãn!).',
            r'Muốn tìm giá trị NHỎ NHẤT của biến hiệu suất cao (\(e\)), hãy cho tổng số lượng đạt kịch trần (\(b = 90 - e\)) rồi thế vào bất phương trình điểm số!',
            r'Vẽ `x + y <= 90` và `3.5x + 2y >= 264` trên Desmos → bấm vào đỉnh cực trái của vùng giao nhau đọc ngay `(56, 34)` → `e_min = 56`!'
        ),
        # Q6 — Algebra (Hard, MCQ -> D)
        math_mcq(
            'sat_mm8_m2h_q6', 6, 'Algebra', 'Linear inequalities in one or two variables', 'Hard',
            r'<p>Consider the system of linear inequalities in the \(xy\)-plane:</p><p style="text-align:center;">\[\begin{cases} y < -2x - 6 \\ y < 3x - 11 \end{cases}\]</p>',
            r'Which quadrants of the \(xy\)-plane contain <b>no solutions</b> to this system?',
            {'A': r'Quadrant I only', 'B': r'Quadrant II only', 'C': r'Quadrants II and III', 'D': r'Quadrants I and II'},
            'D',
            r'Tìm giao điểm hai đường biên: \(-2x - 6 = 3x - 11 \Rightarrow 5x = 5 \Rightarrow x = 1\), suy ra \(y = -2(1) - 6 = -8\). Vì cả hai bất phương trình đều có dạng \(y <\) (lấy phần phía dưới hai đường có hệ số góc trái dấu \(-2\) và \(+3\)), mọi nghiệm \((x, y)\) đều phải thỏa \(y < -8 < 0\). Do đó không có điểm nghiệm nào nằm ở nửa mặt phẳng trên (\(y > 0\)), tức cả <b>Quadrant I và Quadrant II</b> đều vô nghiệm (trong khi \((-1, -20)\) thuộc Q-III và \((1, -20)\) thuộc Q-IV đều là nghiệm).',
            r'Khi hai bất phương trình \(y <\) có slope trái dấu và giao nhau ở tung độ âm (\(y = -8 < 0\)), toàn bộ nửa trên trục Ox (Q-I và Q-II) lập tức bị loại!',
            {
                'A': ('Missed Quadrant II', r'Tại Q-II (\(x < 0, y > 0\)), vế phải \(3x - 11 < -11 < 0 < y\), vi phạm bất phương trình thứ hai.'),
                'B': ('Missed Quadrant I', r'Tại Q-I (\(x > 0, y > 0\)), vế phải \(-2x - 6 < -6 < 0 < y\), vi phạm bất phương trình thứ nhất.'),
                'C': ('Wrongly Excluded Quadrant III', r'Điểm \((-1, -20)\) thuộc Q-III thỏa mãn cả \(-20 < -4\) và \(-20 < -14\).'),
                'D': ('Correct', r'Mọi nghiệm đều có \(y < -8 < 0\), nên cả Quadrant I và Quadrant II đều hoàn toàn trống nghiệm.'),
            },
            r'Gõ thẳng `y < -2x - 6` và `y < 3x - 11` trên Desmos → vùng tô đậm nằm hoàn toàn dưới đường `y = -8` → nhìn 2 giây thấy Q-I và Q-II không có nghiệm!'
        ),
        # Q7 — Algebra (Hard, MCQ -> B)
        math_mcq(
            'sat_mm8_m2h_q7', 7, 'Algebra', 'Linear functions', 'Hard',
            r'<p>A linear function is defined by \(f(x) = mx + b\), where \(m\) and \(b\) are constants with \(m < 0\). For all real numbers \(x\), the function satisfies:</p><p style="text-align:center;">\[f(f(x)) = 16x + 15\]</p>',
            r'What is the value of \(f(-2)\)?',
            {'A': r'\(-5\)', 'B': r'\(3\)', 'C': r'\(-13\)', 'D': r'\(13\)'},
            'B',
            r'Tính hàm hợp: \(f(f(x)) = m(mx + b) + b = m^2x + b(m + 1)\). Đồng nhất hệ số với \(16x + 15\):<br>• \(m^2 = 16 \Rightarrow m = -4\) (vì đề cho điều kiện \(m < 0\)!).<br>• \(b(m + 1) = 15 \Rightarrow b(-4 + 1) = 15 \Rightarrow -3b = 15 \Rightarrow b = -5\).<br>Vậy \(f(x) = -4x - 5 \Rightarrow f(-2) = -4(-2) - 5 = 8 - 5 = 3\).',
            r'Đọc cực kỹ điều kiện dấu \(m < 0\)! Khi giải \(m^2 = 16\), bỏ qua điều kiện âm sẽ ra hàm \(f(x) = 4x + 3\) và dính bẫy \(-5\)!',
            {
                'A': ('Ignored m < 0 Constraint', r'Chọn nhầm \(m = +4 \Rightarrow 5b = 15 \Rightarrow b = 3 \Rightarrow f(-2) = 4(-2) + 3 = -5\).'),
                'B': ('Correct', r'\(m = -4, b = -5 \Rightarrow f(-2) = -4(-2) - 5 = 3\).'),
                'C': ('Evaluated f(2) Instead of f(-2)', r'Thay nhầm \(x = +2\): \(f(2) = -4(2) - 5 = -13\).'),
                'D': ('Sign Error on b', r'Giải nhầm \(b = +5 \Rightarrow -4(-2) + 5 = 13\).'),
            },
            r'Thử trực tiếp trong Desmos: nhập `f(x) = -4x - 5` và vẽ `y = f(f(x))` trùng khít với `y = 16x + 15`, rồi gõ `f(-2)` ra ngay `3`!'
        ),
        # Q8 — Algebra (Hard, MCQ -> A)
        math_mcq(
            'sat_mm8_m2h_q8', 8, 'Algebra', 'Linear inequalities in one or two variables', 'Hard',
            r'<p>An integer \(n\) satisfies the strict linear inequality:</p><p style="text-align:center;">\[4(2 - n) < 3n + 43\]</p>',
            r'What is the <b>least</b> possible value of \(5n + 9\)?',
            {'A': r'\(-11\)', 'B': r'\(-16\)', 'C': r'\(-21\)', 'D': r'\(34\)'},
            'A',
            r'Khai triển và chuyển vế: \(8 - 4n < 3n + 43 \Rightarrow -7n < 35\). Chia hai vế cho \(-7\) và <b>đảo chiều dấu bất đẳng thức</b>: \(n > -5\). Vì \(n\) là số nguyên nghiêm ngặt lớn hơn \(-5\), giá trị nguyên nhỏ nhất của \(n\) là \(-4\). Thay vào biểu thức: \(5(-4) + 9 = -20 + 9 = -11\).',
            r'Hai bẫy liên hoàn: (1) chia cho \(-7\) phải đảo chiều thành \(n > -5\), và (2) số nguyên nhỏ nhất lớn hơn hẳn \(-5\) là \(-4\) (KHÔNG phải \(-5\) hay \(-6\))!',
            {
                'A': ('Correct', r'\(n > -5 \Rightarrow n_{\min} = -4 \Rightarrow 5(-4) + 9 = -11\).'),
                'B': ('Included Boundary n = -5', r'Thay nhầm \(n = -5\) ra \(-16\), nhưng dấu \(<\) nghiêm ngặt không nhận \(n = -5\).'),
                'C': ('Negative Number Direction Error', r'Tưởng \(-6 > -5\) nên chọn \(n = -6\) và tính \(5(-6) + 9 = -21\).'),
                'D': ('Sign Error Solving for n', r'Giải nhầm \(n > +5\) hoặc đổi dấu sai dẫn tới \(5(5) + 9 = 34\).'),
            },
            r'Gõ `4(2 - x) < 3x + 43` trên Desmos thấy miền tô nằm bên phải đường nét đứt `x = -5` → số nguyên nhỏ nhất trong miền là `-4` → `5(-4) + 9 = -11`.'
        ),
        # Q9 — Advanced Math (Hard, SPR -> 12) | Theme: Violin Luthier Acoustics
        math_spr(
            'sat_mm8_m2h_q9', 9, 'Advanced Math', 'Nonlinear equations in one variable and systems of equations in two variables', 'Hard',
            r'<p>During ultrasonic seasoning of spruce violin soundboards, the internal resin viscosity index \(V(t)\) after \(t\) hours of treatment is modeled by:</p><p style="text-align:center;">\[V(t) = 243\left(\dfrac{1}{3}\right)^{t/4}\]</p>',
            r'After how many hours of treatment will the viscosity index equal \(9\)?',
            ['12'], '12',
            r'Đặt \(V(t) = 9\): \(243\left(\frac{1}{3}\right)^{t/4} = 9 \Rightarrow \left(\frac{1}{3}\right)^{t/4} = \frac{9}{243} = \frac{1}{27} = \left(\frac{1}{3}\right)^3\). Đồng nhất số mũ cùng cơ số \(\frac{1}{3}\): \(\frac{t}{4} = 3 \Rightarrow t = 12\) giờ.',
            r'Nhận diện nhanh lũy thừa của \(3\) (\(243 = 3^5, 9 = 3^2 \Rightarrow \frac{9}{243} = \frac{1}{3^3}\)) giúp giải phương trình mũ trong 5 giây mà không cần logarit!',
            r'Vẽ `y = 243*(1/3)^(x/4)` và `y = 9` trên Desmos → bấm giao điểm đọc ngay `x = 12`!'
        ),
        # Q10 — Advanced Math (Hard, MCQ -> C)
        math_mcq(
            'sat_mm8_m2h_q10', 10, 'Advanced Math', 'Nonlinear functions', 'Hard',
            r'<p>The polynomial \(P(x) = 2x^3 + kx^2 - 11x - 10\), where \(k\) is a constant, is divisible by \((x - 2)\).</p>',
            r'What is the remainder when \(P(x)\) is divided by \((x + 2)\)?',
            {'A': r'\(4\)', 'B': r'\(-20\)', 'C': r'\(12\)', 'D': r'\(-32\)'},
            'C',
            r'Bước 1 (Định lý Nhân tử): \(P(x)\) chia hết cho \((x - 2) \Leftrightarrow P(2) = 0\). Thay \(x = 2\): \(2(8) + 4k - 22 - 10 = 0 \Rightarrow 4k - 16 = 0 \Rightarrow k = 4\).<br>Bước 2 (Định lý Số dư): Số dư khi chia \(P(x) = 2x^3 + 4x^2 - 11x - 10\) cho \((x + 2)\) chính là \(P(-2)\): \(2(-8) + 4(4) - 11(-2) - 10 = -16 + 16 + 22 - 10 = 12\).',
            r'Số dư khi chia cho \((x + 2)\) là \(P(-2)\) (nhớ đảo dấu nghiệm chia); cẩn thận \((-2)^2 = +4\) và \(-11(-2) = +22\)!',
            {
                'A': ('Stopped at Constant k', r'\(4\) mới chỉ là hằng số \(k\), chưa tính số dư \(P(-2)\).'),
                'B': ('Square Sign Error on (-2)^2', r'Tính nhầm \(4(-2)^2 = -16\), ra \(-16 - 16 + 22 - 10 = -20\).'),
                'C': ('Correct', r'\(k = 4 \Rightarrow P(-2) = -16 + 16 + 22 - 10 = 12\).'),
                'D': ('Sign Error on -11(-2)', r'Tính nhầm \(-11(-2) = -22\), ra \(-16 + 16 - 22 - 10 = -32\).'),
            },
            r'Gõ `P(x) = 2x^3 + kx^2 - 11x - 10` kèm thanh trượt `k`, kéo đến khi `P(2) = 0` (`k = 4`), rồi gõ `P(-2)` đọc ngay `12`!'
        ),
        # Q11 — Advanced Math (Hard, MCQ -> A)
        math_mcq(
            'sat_mm8_m2h_q11', 11, 'Advanced Math', 'Nonlinear equations in one variable and systems of equations in two variables', 'Hard',
            r'<p>In the \(xy\)-plane, the line \(y = -3x + c\) intersects the parabola \(y = 2x^2 + 5x + 11\) at <b>exactly one point</b>, where \(c\) is a constant.</p>',
            r'What is the value of \(c\)?',
            {'A': r'\(3\)', 'B': r'\(-3\)', 'C': r'\(19\)', 'D': r'\(\frac{21}{2}\)'},
            'A',
            r'Lập phương trình hoành độ giao điểm: \(2x^2 + 5x + 11 = -3x + c \Rightarrow 2x^2 + 8x + (11 - c) = 0\). Để cắt tại đúng \(1\) điểm (tiếp xúc), biệt thức \(\Delta = 8^2 - 4(2)(11 - c) = 0 \Rightarrow 64 - 8(11 - c) = 0 \Rightarrow 11 - c = 8 \Rightarrow c = 3\). (Tiếp điểm duy nhất tại \((-2, 9)\)).',
            r'Đừng quên đổi dấu khi chuyển \(-3x\) sang vế trái thành \(+3x\) (\(5x + 3x = 8x\)), rồi giải \(\Delta = b^2 - 4ac = 0\)!',
            {
                'A': ('Correct', r'\(2x^2 + 8x + (11 - c) = 0\) có \(\Delta = 0 \Leftrightarrow 11 - c = 8 \Rightarrow c = 3\).'),
                'B': ('Sign Reversal Solving for c', r'Giải nhầm \(11 - c = 8\) thành \(c = -3\).'),
                'C': ('Added Instead of Subtracted', r'Giải nhầm \(c - 11 = 8 \Rightarrow c = 19\).'),
                'D': ('Sign Error Moving -3x', r'Gộp nhầm \(5x - 3x = 2x\), giải \(4 - 8(11 - c) = 0 \Rightarrow c = \frac{21}{2}\).'),
            },
            r'Vẽ `y = 2x^2 + 5x + 11` và `y = -3x + c` kèm thanh trượt `c`; tại `c = 3`, đường thẳng chạm tiếp xúc parabol tại đúng 1 điểm `(-2, 9)`!'
        ),
        # Q12 — Advanced Math (Hard, MCQ -> D)
        math_mcq(
            'sat_mm8_m2h_q12', 12, 'Advanced Math', 'Nonlinear equations in one variable and systems of equations in two variables', 'Hard',
            r'<p>The quadratic equation \(2x^2 - 14x + k = 0\), where \(k\) is a constant, has two distinct real solutions \(r\) and \(s\) such that \(|r - s| = 5\).</p>',
            r'What is the value of \(k\)?',
            {'A': r'\(6\)', 'B': r'\(24\)', 'C': r'\(37\)', 'D': r'\(12\)'},
            'D',
            r'Theo định lý Viète cho \(2x^2 - 14x + k = 0\): tổng \(r + s = \frac{14}{2} = 7\) và tích \(rs = \frac{k}{2}\). Áp dụng hằng đẳng thức \((r - s)^2 = (r + s)^2 - 4rs\): \(5^2 = 7^2 - 4\left(\frac{k}{2}\right) \Rightarrow 25 = 49 - 2k \Rightarrow 2k = 24 \Rightarrow k = 12\). (Kiểm tra: \(2(x - 1)(x - 6) = 0\) có hai nghiệm \(1\) và \(6\), thỏa \(|6 - 1| = 5\)).',
            r'Hằng đẳng thức 750+ cực lợi hại: \((r - s)^2 = (r + s)^2 - 4rs\) (nhớ hệ số là \(4\), KHÔNG phải \(2\), và \(rs = c/a = k/2\))!',
            {
                'A': ('Forgot Leading Coefficient a = 2', r'Tính đúng \(rs = 6\) nhưng quên nhân với \(a = 2\) để ra \(k = 12\).'),
                'B': ('Used -2rs Instead of -4rs', r'Dùng nhầm hằng đẳng thức \((r + s)^2 - 2rs = 25 \Rightarrow k = 24\).'),
                'C': ('Added Instead of Subtracted', r'Tính sai \(49 + 25 = 74 \Rightarrow k = 37\).'),
                'D': ('Correct', r'\(49 - 2k = 25 \Rightarrow k = 12\).'),
            },
            r'Vẽ `y = 2x^2 - 14x + k` với thanh trượt `k`; thử `k = 12` thấy ngay hai nghiệm trục hoành là `1` và `6`, khoảng cách đúng `6 - 1 = 5`!'
        ),
        # Q13 — Advanced Math (Hard, SPR -> 25) | Theme: National Park Wildlife Census
        math_spr(
            'sat_mm8_m2h_q13', 13, 'Advanced Math', 'Equivalent expressions', 'Hard',
            r'<p>Biologists tracking a reintroduced river otter population in a national park model the population \(P(t)\) after \(t\) years by:</p><p style="text-align:center;">\[P(t) = 180(1.5625)^{t/2}\]</p><p>The model can be rewritten in the equivalent annual form \(P(t) = 180\left(1 + \dfrac{r}{100}\right)^t\), where \(r\) is a positive constant.</p>',
            r'What is the value of \(r\)?',
            ['25'], '25',
            r'Đưa số mũ về bậc \(t\): \((1.5625)^{t/2} = \left[(1.5625)^{1/2}\right]^t = \left(\sqrt{1.5625}\right)^t\). Vì \(1.5625 = \frac{25}{16} = (1.25)^2\), suy ra \(\sqrt{1.5625} = 1.25\). Đồng nhất với \(1 + \frac{r}{100} = 1.25 \Rightarrow r = 25\).',
            r'Đổi hàm mũ chu kỳ \(2\) năm (\(t/2\)) sang chu kỳ \(1\) năm (\(t\)): luôn lấy căn bậc hai cơ số \(\sqrt{b}\) rồi trừ \(1\) và nhân \(100\%\)!',
            r'Gõ `(sqrt(1.5625) - 1) * 100` trên Desmos trả về ngay chính xác `25`!'
        ),
        # Q14 — Advanced Math (750–800 BOSS, MCQ -> B) | Parametric Quadratic Factorization
        math_mcq(
            'sat_mm8_m2h_q14', 14, 'Advanced Math', 'Equivalent expressions', 'Hard',
            r'<p>In the polynomial identity below, \(p, q, r, s,\) and \(k\) are <b>positive integers</b>:</p><p style="text-align:center;">\[(px + q)(rx + s) = 18x^2 + kx + 20\]</p><p>It is also known that \(p + r = 9\).</p>',
            r'What is the <b>greatest</b> possible value of \(k\)?',
            {'A': r'\(66\)', 'B': r'\(123\)', 'C': r'\(361\)', 'D': r'\(42\)'},
            'B',
            r'Bước 1: Khai triển vế trái: \(prx^2 + (ps + qr)x + qs = 18x^2 + kx + 20\), suy ra \(pr = 18\), \(qs = 20\), và \(k = ps + qr\).<br>Bước 2: Kết hợp \(pr = 18\) và \(p + r = 9\) (nguyên dương): \(p\) và \(r\) là nghiệm của \(t^2 - 9t + 18 = 0 \Rightarrow \{p, r\} = \{3, 6\}\) (cặp duy nhất!).<br>Bước 3: Theo bất đẳng thức sắp xếp lại, để tối đa hóa \(k = 6u + 3v\) với \(uv = 20\), ta ghép số lớn nhất của \(\{3, 6\}\) là \(6\) với thừa số lớn nhất của \(20\) là \(20\), và \(3\) với \(1\): \(k_{\max} = 6(20) + 3(1) = 123\) (ứng với \((6x + 1)(3x + 20)\)).',
            r'Quy tắc tối ưu hóa \(k = ps + qr\): luôn ghép hệ số LỚN nhất của \(x\) với hằng số LỚN nhất (cặp \(1 \times 20\)) để tổng tích đạt cực đại!',
            {
                'A': ('Paired Opposite Extremes or Used 2×10', r'Ghép \(3(20) + 6(1) = 66\) (hoặc \(6(10) + 3(2) = 66\)) chưa đạt giá trị lớn nhất.'),
                'B': ('Correct', r'Với \(\{p, r\} = \{3, 6\}\) và \(\{q, s\} = \{1, 20\}\), cực đại \(k = 6(20) + 3(1) = 123\).'),
                'C': ('Ignored p + r = 9 Constraint', r'Chọn nhầm \(p = 18, r = 1\) (có \(p + r = 19 \neq 9\)) ra \(18(20) + 1(1) = 361\).'),
                'D': ('Used Middle Factors 4×5', r'Ghép \(6(5) + 3(4) = 42\) — gần giá trị nhỏ nhất thay vì lớn nhất.'),
            },
            r'Tạo danh sách các ước của 20 trên Desmos: `u = [1, 2, 4, 5, 10, 20]` rồi tính `max(6*u + 3*(20/u))` đọc ngay `123`!'
        ),
        # Q15 — Advanced Math (750–800 BOSS, MCQ -> C) | Theme: Violin Luthier Acoustics
        math_mcq(
            'sat_mm8_m2h_q15', 15, 'Advanced Math', 'Nonlinear functions', 'Hard',
            r'<p>An acoustic physicist measures the decaying overtone vibration amplitude \(A(t)\), in microns, of a plucked violin G-string \(t\) milliseconds after release. The amplitude is modeled by an exponential function of the form \(A(t) = c \cdot b^t + d\), where \(c, b,\) and \(d\) are positive constants. As \(t\) increases without bound, \(A(t)\) approaches \(8\). Furthermore, \(A(0) = 72\) and \(A(3) = 16\).</p>',
            r'What is the value of \(A(2)\)?',
            {'A': r'\(16\)', 'B': r'\(26\)', 'C': r'\(24\)', 'D': r'\(40\)'},
            'C',
            r'Bước 1 (Tiệm cận ngang): Vì \(A(t)\) tiến dần về \(8\) khi \(t \to \infty\) (nên \(0 < b < 1\) và \(b^t \to 0\)), ta suy ra ngay hằng số tiệm cận \(d = 8\).<br>Bước 2 (Tìm \(c\)): Thay \(t = 0\): \(A(0) = c \cdot b^0 + 8 = 72 \Rightarrow c + 8 = 72 \Rightarrow c = 64\).<br>Bước 3 (Tìm cơ số \(b\)): Thay \(t = 3\): \(64 b^3 + 8 = 16 \Rightarrow 64 b^3 = 8 \Rightarrow b^3 = \frac{1}{8} \Rightarrow b = \frac{1}{2}\).<br>Bước 4 (Tính \(A(2)\)): \(A(2) = 64\left(\frac{1}{2}\right)^2 + 8 = 64\left(\frac{1}{4}\right) + 8 = 16 + 8 = 24\).',
            r'Với hàm mũ có dịch chuyển đứng \(A(t) = c \cdot b^t + d\): giá trị tiệm cận là \(d\), giá trị đầu là \(c + d\) (nên \(c = A(0) - d\)), và nhớ CỘNG LẠI \(d\) ở bước tính cuối!',
            {
                'A': ('Forgot to Add Asymptote d = 8 at End', r'Tính \(64(1/2)^2 = 16\) mà quên cộng lại tiệm cận \(+8\).'),
                'B': ('Used c = A(0) = 72 Without Subtracting d', r'Lấy nhầm \(c = 72\) thay vì \(72 - 8 = 64\), tính \(72(1/4) + 8 = 26\).'),
                'C': ('Correct', r'\(c = 64, b = \frac{1}{2}, d = 8 \Rightarrow A(2) = 64(1/4) + 8 = 24\).'),
                'D': ('Evaluated A(1) Instead of A(2)', r'Tính nhầm \(A(1) = 64(1/2) + 8 = 40\).'),
            },
            r'Gõ `c = 72 - 8`, `b = ((16 - 8)/c)^(1/3)`, sau đó tính `c * b^2 + 8` trên Desmos trả về ngay `24`!'
        ),
        # Q16 — PSDA (750–800 BOSS, SPR -> 36) | Theme: Geothermal Power Wells
        math_spr(
            'sat_mm8_m2h_q16', 16, 'Problem-Solving and Data Analysis', 'Ratios, rates, proportional relationships, and units', 'Hard',
            r'<p>A geothermal power plant pumps cooled brine back into a deep injection well at a constant rate of \(540\) cubic feet per minute. <em>(\(1\text{ yard} = 3\text{ feet}\))</em></p>',
            r'At this rate, how many <b>hours</b> will it take to inject \(43{,}200\) cubic yards of brine into the well?',
            ['36'], '36',
            r'Bước 1 (Đổi thể tích lập phương): Vì \(1\text{ yd} = 3\text{ ft}\), nên \(1\text{ yd}^3 = 3^3 = 27\text{ ft}^3\). Tốc độ bơm tính theo yard khối mỗi phút là: \(\frac{540}{27} = 20\text{ yd}^3/\text{min}\).<br>Bước 2 (Đổi sang mỗi giờ): Nhân với \(60\) phút/giờ: \(20 \times 60 = 1{,}200\text{ yd}^3/\text{hr}\).<br>Bước 3 (Tính thời gian): \(t = \frac{43{,}200}{1{,}200} = 36\text{ giờ}\).',
            r'Chuyển đổi kép 3D + thời gian: chia \(3^3 = 27\) để đổi \(\text{ft}^3 \to \text{yd}^3\), nhân \(60\) để đổi phút \(\to\) giờ, rồi mới chia tổng thể tích!',
            r'Tính một dòng trên Desmos: `43200 / ((540 / 3^3) * 60)` ra ngay kết quả chuẩn xác `36`!'
        ),
        # Q17 — PSDA (750–800 BOSS, MCQ -> A) | Theme: National Park Wildlife Census (Table)
        math_mcq(
            'sat_mm8_m2h_q17', 17, 'Problem-Solving and Data Analysis', 'Probability and conditional probability', 'Hard',
            tbl_q17 + r'<p>The table above summarizes a national park census of bighorn sheep across two sectors, where \(k\) is a positive integer. If a bighorn sheep recorded in <b>South Valley</b> is selected at random, the probability that it is a <b>Juvenile</b> is \(\dfrac{1}{4}\).</p>',
            r'If a <b>Juvenile</b> bighorn sheep is selected at random from the census, what is the probability that it was recorded in <b>South Valley</b>?',
            {'A': r'\(\dfrac{3}{7}\)', 'B': r'\(\dfrac{4}{7}\)', 'C': r'\(\dfrac{3}{22}\)', 'D': r'\(\dfrac{1}{3}\)'},
            'A',
            r'Bước 1 (Tìm \(k\) từ dữ kiện điều kiện): \(P(\text{Juvenile} \mid \text{South Valley}) = \frac{k}{k + 135} = \frac{1}{4} \Rightarrow 4k = k + 135 \Rightarrow 3k = 135 \Rightarrow k = 45\).<br>Bước 2 (Tính tổng cột Juvenile): \(60 + 45 = 105\).<br>Bước 3 (Tính xác suất đảo chiều điều kiện): \(P(\text{South Valley} \mid \text{Juvenile}) = \frac{45}{105} = \frac{3}{7}\).',
            r'Để ý cú đảo chiều điều kiện: giả thiết cho \(P(\text{Juvenile} \mid \text{South Valley})\), còn câu hỏi đảo ngược thành \(P(\text{South Valley} \mid \text{Juvenile})\)!',
            {
                'A': ('Correct', r'\(k = 45\), tổng Juvenile \(= 105 \Rightarrow \frac{45}{105} = \frac{3}{7}\).'),
                'B': ('Picked Wrong Sector (North Ridge)', r'Tính \(P(\text{North Ridge} \mid \text{Juvenile}) = \frac{60}{105} = \frac{4}{7}\).'),
                'C': ('Grand Total Denominator Trap', r'Chia cho tổng toàn công viên \(285 + 45 = 330\): \(\frac{45}{330} = \frac{3}{22}\).'),
                'D': ('Used Adult Count as Denominator', r'Chia nhầm \(\frac{45}{135} = \frac{1}{3}\) thay vì tổng cột Juvenile.'),
            },
            r'Gõ `x / (x + 135) = 1/4` trên Desmos đọc ngay `x = 45`, sau đó gõ `45 / (60 + 45)` và bấm nút phân số ra ngay `3/7`!'
        ),
        # Q18 — PSDA (750–800 BOSS, MCQ -> C) | Theme: Warehouse Conveyor Robotics (Parametric Median Table)
        math_mcq(
            'sat_mm8_m2h_q18', 18, 'Problem-Solving and Data Analysis', 'One-variable data: Distributions and measures of center and spread', 'Hard',
            tbl_q18 + r'<p>The frequency table above shows the number of daily sorting cycles completed by a fleet of autonomous warehouse conveyor robots, where \(m\) is a positive integer.</p>',
            r'What is the <b>greatest</b> possible value of \(m\) such that the <b>median</b> number of daily sorting cycles for all robots in the table is \(50\)?',
            {'A': r'\(7\)', 'B': r'\(9\)', 'C': r'\(8\)', 'D': r'\(13\)'},
            'C',
            r'Có \(6 + 8 = 14\) robot ở nhóm \(\le 50\) (vị trí \(1\text{–}6\) là \(40\); vị trí \(7\text{–}14\) là \(50\)) và \(m + 5\) robot ở nhóm \(\ge 60\). Tổng số robot là \(n = 19 + m\).<br>• Thử \(m = 8\): \(n = 27\) (số lẻ), trung vị là phần tử chính giữa ở vị trí \(\frac{27 + 1}{2} = 14\), rơi ĐÚNG vào mức \(50\) (thỏa mãn!).<br>• Thử \(m = 9\): \(n = 28\) (số chẵn!), trung vị là trung bình cộng của phần tử thứ \(14\) (mức \(50\)) và phần tử thứ \(15\) (mức \(60\)), cho trung vị \(\frac{50 + 60}{2} = 55 \neq 50\) (LOẠI!).<br>Với mọi \(m \ge 9\), trung vị đều lớn hơn hẳn \(50\). Vậy giá trị nguyên lớn nhất của \(m\) là \(8\).',
            r'Bẫy 790–800 kinh điển về trung vị: khi số phần tử hai bên bằng nhau (\(14\) và \(14\) tại \(m = 9\)), tổng \(n = 28\) là số CHẴN nên trung vị bị kéo lên trung bình cộng \(\frac{50 + 60}{2} = 55\)! Muốn giữ trung vị đúng \(50\), tổng \(n\) cực đại phải là số LẺ (\(14\) bên trái, \(13\) bên phải \(\Rightarrow m + 5 = 13 \Rightarrow m = 8\))!',
            {
                'A': ('Over-Restricted to Even n', r'Tại \(m = 7\) (\(n = 26\)), vị trí 13 và 14 đều là \(50\), nhưng vẫn tăng được lên \(m = 8\).'),
                'B': ('Even-Total Averaging Trap', r'Bẫy chí mạng: đặt \(m + 5 = 14 \Rightarrow m = 9\) khiến \(n = 28\) chẵn và trung vị biến thành \(\frac{50 + 60}{2} = 55\)!'),
                'C': ('Correct', r'Tại \(m = 8\), \(n = 27\) lẻ và phần tử thứ 14 đúng bằng \(50\); đây là giá trị \(m\) lớn nhất.'),
                'D': ('Forgot the 5 Robots at 70 Cycles', r'Đặt \(m = 14 - 1 = 13\) mà bỏ quên \(5\) robot ở mức \(70\) chu kỳ.'),
            },
            r'Kiểm tra thẳng quy tắc: muốn vị trí giữa dừng ở 14 (số lẻ \(n = 27\)), số robot bên phải tối đa là \(13 \Rightarrow m + 5 = 13 \Rightarrow m = 8\). Thử bằng `median()` trên Desmos để xác nhận tại `m=8` ra `50` và `m=9` ra `55`!'
        ),
        # Q19 — PSDA (750–800 BOSS, SPR -> 18) | Theme: Geothermal Power Wells
        math_spr(
            'sat_mm8_m2h_q19', 19, 'Problem-Solving and Data Analysis', 'Percentages', 'Hard',
            r'<p>A geothermal power station operates two turbine blocks, Block Alpha and Block Beta. In Quarter 1, Block Alpha generated \(50\%\) more electricity than Block Beta. In Quarter 2, Block Alpha\'s output increased by \(40\%\) compared to Quarter 1, while Block Beta\'s output decreased by \(15\%\) compared to Quarter 1.</p>',
            r'The combined electricity generated by both blocks in Quarter 2 was \(p\%\) greater than their combined electricity generated in Quarter 1. What is the value of \(p\)?',
            ['18'], '18',
            r'Chọn mốc tính nhanh: đặt sản lượng Block Beta ở Quý 1 là \(100\) MWh.<br>• Block Alpha ở Quý 1 lớn hơn \(50\%\): \(100 \times 1.50 = 150\) MWh \(\Rightarrow\) Tổng Quý 1 \(= 100 + 150 = 250\) MWh.<br>• Sang Quý 2: Block Alpha tăng \(40\% \Rightarrow 150 \times 1.40 = 210\) MWh; Block Beta giảm \(15\% \Rightarrow 100 \times 0.85 = 85\) MWh \(\Rightarrow\) Tổng Quý 2 \(= 210 + 85 = 295\) MWh.<br>• Phần trăm tăng trưởng tổng hợp: \(\frac{295 - 250}{250} \times 100\% = \frac{45}{250} \times 100\% = 18\% \Rightarrow p = 18\).',
            r'Gặp bài toán phần trăm tổng hợp của 2 thành phần có quy mô chênh lệch, LUÔN gán mốc \(100\) cho thành phần gốc (Block Beta Q1) — tuyệt đối không trừ thẳng \(40\% - 15\%\) hay lấy trung bình cộng!',
            r'Gõ `((150*1.40 + 100*0.85) - 250) / 250 * 100` vào Desmos ra ngay chính xác `18`!'
        ),
        # Q20 — Geometry (750–800 BOSS, MCQ -> D) | SVG Circle Sector | Theme: Monument Courtyard
        math_mcq(
            'sat_mm8_m2h_q20', 20, 'Geometry and Trigonometry', 'Circles', 'Hard',
            f'<div style="text-align:center;margin-bottom:10px;">{svg_q20}</div>' + r'<p>In the circular monument plaza centered at \(O\) shown above, shaded sector \(AOB\) has radius \(r\) meters, arc length \(\widehat{AB} = 10\pi\) meters, and area \(90\pi\) square meters.</p>',
            r'What is the measure of central angle \(\angle AOB\), in <b>degrees</b>?',
            {'A': r'\(40\)', 'B': r'\(50\)', 'C': r'\(200\)', 'D': r'\(100\)'},
            'D',
            r'Bước 1 (Tìm bán kính \(r\)): Dùng liên hệ diện tích quạt tròn và độ dài cung \(A_{\text{quạt}} = \frac{1}{2} r \cdot s\):<br>\(90\pi = \frac{1}{2} r (10\pi) = 5\pi r \Rightarrow r = 18\text{ m}\).<br>(Hoặc lập tỉ số \(\frac{\text{Area}}{\text{Arc}} = \frac{\pi r^2}{2\pi r} = \frac{r}{2} \Rightarrow \frac{90\pi}{10\pi} = 9 = \frac{r}{2} \Rightarrow r = 18\)).<br>Bước 2 (Tìm góc ở tâm \(\theta\)): Chu vi cả đường tròn là \(2\pi(18) = 36\pi\). Do đó \(\frac{\theta}{360^\circ} = \frac{10\pi}{36\pi} = \frac{5}{18} \Rightarrow \theta = \frac{5}{18} \times 360^\circ = 100^\circ\).',
            r'Phím tắt 800 Geometry cho hình quạt tròn: luôn nhớ \(\frac{\text{Diện tích quạt}}{\text{Độ dài cung}} = \frac{r}{2}\) để chốt ngay bán kính \(r\) trong 3 giây!',
            {
                'A': ('Divided Arc by Area Directly', r'Tính sai \(\frac{10\pi}{90\pi} \times 360^\circ = 40^\circ\) mà không tìm bán kính \(r\).'),
                'B': ('Doubled Radius to r = 36', r'Nhầm \(r = 36\) khiến góc bị giảm một nửa còn \(50^\circ\).'),
                'C': ('Forgot Factor of 2 in r/2', r'Đặt nhầm \(r = \frac{90\pi}{10\pi} = 9\) (quên hệ số \(\frac{1}{2}\)), dẫn đến \(\frac{10\pi}{18\pi} \times 360^\circ = 200^\circ\).'),
                'D': ('Correct', r'\(r = 18 \Rightarrow \theta = \frac{10\pi}{36\pi} \cdot 360^\circ = 100^\circ\).'),
            },
            r'Tính `r = 2 * 90 / 10` (`18`) rồi gõ `(10 / (2 * 18)) * 360` trên Desmos ra ngay `100`!'
        ),
        # Q21 — Geometry (750–800 BOSS, MCQ -> B) | SVG Right Triangle | Theme: Stepped-Pyramid Monument
        math_mcq(
            'sat_mm8_m2h_q21', 21, 'Geometry and Trigonometry', 'Right triangles and trigonometry', 'Hard',
            f'<div style="text-align:center;margin-bottom:10px;">{svg_q21}</div>' + r'<p>The cross-section of a stepped-pyramid monument\'s structural support brace is modeled by right triangle \(ABC\) above, where \(\angle B = 90^\circ\), \(\sin(A) = \dfrac{7}{25}\), and the <b>perimeter</b> of \(\triangle ABC\) is \(168\) meters.</p>',
            r'What is the <b>area</b> of \(\triangle ABC\), in square meters?',
            {'A': r'\(252\)', 'B': r'\(756\)', 'C': r'\(1{,}512\)', 'D': r'\(84\)'},
            'B',
            r'Bước 1 (Dùng tỉ số lượng giác + Pythagoras): Vì \(\sin(A) = \frac{BC}{AC} = \frac{7}{25}\), đặt \(BC = 7k\) và \(AC = 25k\) (\(k > 0\)). Khi đó cạnh góc vuông còn lại là \(AB = \sqrt{(25k)^2 - (7k)^2} = \sqrt{576k^2} = 24k\) (bộ ba Pythagoras \(7\text{–}24\text{–}25\)).<br>Bước 2 (Tìm hệ số tỉ lệ \(k\) từ chu vi): \(7k + 24k + 25k = 56k = 168 \Rightarrow k = 3\).<br>Bước 3 (Tính diện tích): Hai cạnh góc vuông là \(BC = 21\text{ m}\) và \(AB = 72\text{ m}\), suy ra \(\text{Area} = \frac{1}{2}(21)(72) = 756\text{ m}^2\). (Hoặc lấy diện tích tam giác gốc \(\frac{1}{2}(7)(24) = 84\) nhân với \(k^2 = 9\): \(84 \times 9 = 756\)).',
            r'Tam giác phóng đại theo hệ số cạnh \(k = 3\) thì DIỆN TÍCH phóng đại theo \(k^2 = 9\) (\(84 \times 9 = 756\)) — không bao giờ nhân tuyến tính với \(3\)!',
            {
                'A': ('Linear Area Scaling Trap', r'Lấy diện tích tam giác gốc \(84\) nhân tuyến tính với \(k = 3\) thành \(252\) thay vì nhân \(k^2 = 9\).'),
                'B': ('Correct', r'Các cạnh là \(21, 72, 75 \Rightarrow \text{Area} = \frac{1}{2}(21)(72) = 756\text{ m}^2\).'),
                'C': ('Forgot Factor of 1/2', r'Tính \(21 \times 72 = 1{,}512\) mà quên chia đôi trong công thức diện tích tam giác.'),
                'D': ('Ignored Scale Factor k = 3', r'\(84\) chỉ là diện tích của tam giác gốc \(7\text{–}24\text{–}25\) có chu vi \(56\), chưa phóng lên chu vi \(168\).'),
            },
            r'Gõ `k = 168 / (7 + 24 + 25)` (`3`), sau đó tính `0.5 * (7*k) * (24*k)` trên Desmos ra ngay `756`!'
        ),
        # Q22 — Geometry (750–800 BOSS, SPR -> 912) | Truncated-Cone Monument 3D Scaling
        math_spr(
            'sat_mm8_m2h_q22', 22, 'Geometry and Trigonometry', 'Area and volume', 'Hard',
            f'<div style="text-align:center;margin-bottom:10px;">{svg_q22}</div>' + r'<p>A solid stone monument has the shape of a <b>truncated right circular cone</b> formed by slicing a smaller right circular cone off the top of a larger right circular cone parallel to its circular base. As shown above, the monument has a bottom base radius of \(R = 12\) meters, a top circular face radius of \(r = 8\) meters, and a vertical height of \(h = 9\) meters.</p>',
            r'If the volume of the truncated-cone monument is \(m\pi\) cubic meters, what is the value of \(m\)?',
            ['912'], '912',
            r'Bước 1 (Khôi phục chiều cao phần chóp nón đã cắt bằng tam giác đồng dạng): Gọi \(h_{\text{top}}\) là chiều cao hình nón nhỏ phía trên bị cắt đi. Mặt cắt dọc qua trục tạo hai tam giác vuông đồng dạng: \(\frac{h_{\text{top}}}{h_{\text{top}} + 9} = \frac{8}{12} = \frac{2}{3} \Rightarrow 3h_{\text{top}} = 2h_{\text{top}} + 18 \Rightarrow h_{\text{top}} = 18\text{ m}\). Do đó hình nón lớn ban đầu có chiều cao \(H = 18 + 9 = 27\text{ m}\).<br>Bước 2 (Trừ thể tích hai hình nón):<br>• Thể tích nón lớn: \(V_{\text{lớn}} = \frac{1}{3}\pi (12^2)(27) = 144 \times 9\pi = 1{,}296\pi\text{ m}^3\).<br>• Thể tích nón nhỏ cắt bỏ: \(V_{\text{nhỏ}} = \frac{1}{3}\pi (8^2)(18) = 64 \times 6\pi = 384\pi\text{ m}^3\).<br>• Thể tích tượng đài nón cụt: \(V = 1{,}296\pi - 384\pi = 912\pi \Rightarrow m = 912\).<br><em>(Kiểm tra nhanh bằng công thức nón cụt: \(\frac{1}{3}\pi h (R^2 + Rr + r^2) = \frac{1}{3}\pi (9)(144 + 96 + 64) = 3\pi(304) = 912\pi\).)</em>',
            r'Mọi bài toán nón cụt (frustum) trên SAT 800 đều giải đẹp bằng hai bước: (1) dùng tam giác đồng dạng khôi phục chiều cao nón đầy đủ, rồi (2) lấy \(V_{\text{lớn}} - V_{\text{nhỏ}}\) (hoặc dùng công thức \(\frac{1}{3}\pi h (R^2 + Rr + r^2)\))!',
            r'Kiểm chứng ngay bằng công thức nón cụt trên Desmos: `(1/3) * 9 * (12^2 + 12*8 + 8^2)` trả về chính xác `912`!'
        ),
    ]


if __name__ == '__main__':
    assert verify_math()
    qs = get_m2h_questions()
    print(f"M2H verified: {len(qs)} questions")
