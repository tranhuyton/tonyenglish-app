# -*- coding: utf-8 -*-
"""
Digital SAT Math 1500+ — Capstone Hard M2 Boss Masterclass (750–800 Sprint)
2 Hard/Elite-Only Math Boss Drills (30 brand-new, 100% original, copyright-clean 750–800 Qs):
  - Boss Drill 5 (boss_drill_5): Desmos Advanced Hacks — Multi-Param Regression & Identity Systems (15 Qs)
  - Boss Drill 6 (boss_drill_6): Parametric Quadratics, Integer Bounds & Disguised Substitutions (15 Qs)

Every question includes deep Vietnamese 800-level explanations, concrete advanced Desmos shortcuts
(multi-parameter regression `~`, list evaluation `[...]`, slider tangency, system regression),
key takeaways, and (for MCQs) 4-option trap analysis. All 30 answers are verified programmatically
via exact Fraction/math arithmetic in verify_all_math().
"""

import math
import os
import re
import sys
from fractions import Fraction

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sat_math_helpers import (
    build_math_drill_json,
    build_math_table,
    math_mcq,
    math_spr,
    svg_parabola_vertex,
)
from sat_qa_validator import validate_sat_test

DOM_ALG = 'Algebra'
DOM_ADV = 'Advanced Math'

SK_LIN_EQ_2V = 'Linear equations in two variables'
SK_LIN_FUNC = 'Linear functions'
SK_LIN_SYS = 'Systems of two linear equations in two variables'
SK_LIN_INEQ = 'Linear inequalities in one or two variables'
SK_NONLIN_FUNC = 'Nonlinear functions'
SK_NONLIN_EQ = 'Nonlinear equations in one variable and systems of equations in two variables'
SK_EQUIV = 'Equivalent expressions'


# ============================================================================
# BOSS DRILL 5: Desmos Advanced Hacks — Multi-Param Regression & Identity Systems
# Domain Mix: Algebra (5 Qs: Q2, Q6, Q9, Q11, Q13) & Advanced Math (10 Qs)
# MCQ Key Distribution (10 MCQs): A=3, B=3, C=2, D=2 | SPR: Q3, Q6, Q9, Q12, Q15
# Difficulty: Q1–Q5 Hard, Q6–Q15 Elite 750+
# ============================================================================
def _build_boss_drill_5():
    tbl_q1 = build_math_table(
        [r'\(x\)', r'\(f(x) + 11\)'],
        [
            [r'\(-1\)', r'\(33\)'],
            [r'\(2\)', r'\(0\)'],
            [r'\(5\)', r'\(21\)'],
        ],
        caption='Selected Values of f(x) + 11',
    )

    tbl_q5 = build_math_table(
        [r'\(x\)', r'\(f(x)\)'],
        [
            [r'\(0\)', r'\(-9\)'],
            [r'\(1\)', r'\(1\)'],
            [r'\(2\)', r'\(31\)'],
        ],
        caption='Selected Values of the Shifted Exponential Function f',
    )

    tbl_q10 = build_math_table(
        [r'\(x\)', r'\(f(x - 2)\)'],
        [
            [r'\(-2\)', r'\(9\)'],
            [r'\(1\)', r'\(0\)'],
            [r'\(3\)', r'\(14\)'],
        ],
        caption='Selected Values of f(x - 2)',
    )

    tbl_q15 = build_math_table(
        [r'\(x\)', r'\(p(x)\)'],
        [
            [r'\(-2\)', r'\(-13\)'],
            [r'\(-1\)', r'\(6\)'],
            [r'\(1\)', r'\(2\)'],
            [r'\(2\)', r'\(3\)'],
        ],
        caption='Selected Values of the Cubic Polynomial p',
    )

    qs = [
        # Q1 — Hard, MCQ, Key=A, Advanced Math
        math_mcq(
            'sat_boss_d5_q1', 1, DOM_ADV, SK_NONLIN_FUNC, 'Hard',
            f'<div style="margin-bottom:12px;">{tbl_q1}</div>'
            r'<p>For the quadratic function \(f(x) = ax^2 + bx + c\), where \(a\), \(b\), and \(c\) are constants, the table above gives three values of \(x\) and the corresponding values of \(f(x) + 11\).</p>',
            r'<p>What is the value of \(a + b + c\)?</p>',
            {
                'A': r'\(-6\)',
                'B': r'\(5\)',
                'C': r'\(16\)',
                'D': r'\(22\)',
            },
            'A',
            r'<b>Bước 1 (Tách độ dịch đứng):</b> Đặt \(g(x) = f(x) + 11 = ax^2 + bx + (c + 11)\). Vì \(g(2) = 0\), ta có \(4a + 2b + (c + 11) = 0\).<br/>'
            r'<b>Bước 2 (Tìm \(a, b, c\)):</b> Thay ba điểm \((-1, 33),\; (2, 0),\; (5, 21)\) vào \(g(x) = ax^2 + bx + d\) (với \(d = c + 11\)):<br/>'
            r'\[\begin{cases} a - b + d = 33 \\ 4a + 2b + d = 0 \\ 25a + 5b + d = 21 \end{cases}\]'
            r'Lấy (2) trừ (1): \(3a + 3b = -33 \implies a + b = -11\). Lấy (3) trừ (2): \(21a + 3b = 21 \implies 7a + b = 7\).<br/>'
            r'Trừ hai phương trình mới: \(6a = 18 \implies a = 3 \implies b = -14\). Từ (1): \(3 - (-14) + d = 33 \implies d = 16 \implies c = d - 11 = 5\).<br/>'
            r'<b>Bước 3 (Tính đích):</b> \(a + b + c = 3 + (-14) + 5 = -6\) (chính là \(f(1)\)).',
            r'Với bảng cho cột dịch đứng \(f(x) + k\), luôn đặt trực tiếp \(y_1 \sim ax_1^2 + bx_1 + c + k\) để tránh quên trừ \(k\) ở bước cuối; nhớ \(a + b + c = f(1)\).',
            {
                'A': ('Đáp án đúng', r'Từ \(f(x) = 3x^2 - 14x + 5\) suy ra \(a + b + c = f(1) = 3 - 14 + 5 = -6\).'),
                'B': ('Forgot Vertical Shift', r'Quên trừ \(11\) khỏi cột \(f(x) + 11\), tính nhầm \(g(1) = f(1) + 11 = -6 + 11 = 5\).'),
                'C': ('Shifted y-Intercept Trap', r'Lấy nhầm hằng số tự do của bảng đã dịch \(c + 11 = 16\) thay vì \(a + b + c\).'),
                'D': ('Wrong Evaluation Point', r'Tính nhầm \(a - b + c = f(-1) = 33 - 11 = 22\) do đảo dấu hệ số \(b\).'),
            },
            desmos_tip_vi=r'Gõ bảng hoặc danh sách \(x_1 = [-1, 2, 5]\), \(y_1 = [33, 0, 21]\), rồi gõ thẳng hồi quy có sẵn độ dịch \(y_1 \sim ax_1^2 + bx_1 + c + 11\). Desmos trả ngay \(a = 3,\; b = -14,\; c = 5\) (\(R^2 = 1\)); gõ \(a + b + c\) ra ngay \(-6\) trong 10 giây!',
        ),

        # Q2 — Hard, MCQ, Key=C, Algebra
        math_mcq(
            'sat_boss_d5_q2', 2, DOM_ALG, SK_LIN_SYS, 'Hard',
            r'<p>\[\begin{aligned} 2ax - 5y &= 14 + 3y \\ 9x + (b - 2)y &= 21 \end{aligned}\]</p>'
            r'<p>In the given system of equations, \(a\) and \(b\) are constants. The system has infinitely many solutions.</p>',
            r'<p>What is the value of \(a - b\)?</p>',
            {
                'A': r'\(-13\)',
                'B': r'\(-7\)',
                'C': r'\(13\)',
                'D': r'\(17\)',
            },
            'C',
            r'<b>Bước 1 (Đưa về dạng chuẩn \(Ax + By = C\)):</b> Chuyển \(3y\) sang vế trái ở phương trình thứ nhất:<br/>'
            r'\[2ax - 8y = 14\]'
            r'Phương trình thứ hai đã ở dạng chuẩn: \(9x + (b - 2)y = 21\).<br/>'
            r'<b>Bước 2 (Tỉ số trùng nhau cho vô số nghiệm):</b> Hệ có vô số nghiệm khi và chỉ khi tỉ số các hệ số tương ứng bằng nhau:<br/>'
            r'\[\frac{2a}{9} = \frac{-8}{b - 2} = \frac{14}{21} = \frac{2}{3}\]'
            r'Giải từng ẩn: \(\frac{2a}{9} = \frac{2}{3} \implies 2a = 6 \implies a = 3\); và \(\frac{-8}{b - 2} = \frac{2}{3} \implies 2(b - 2) = -24 \implies b - 2 = -12 \implies b = -10\).<br/>'
            r'<b>Bước 3 (Tính \(a - b\)):</b> \(a - b = 3 - (-10) = 13\).',
            r'Trước khi lập tỉ số \(\frac{A_1}{A_2} = \frac{B_1}{B_2} = \frac{C_1}{C_2}\), BẮT BUỘC gom toàn bộ biến cùng loại về một vế và cực kỳ cẩn thận dấu trừ kép khi tính \(a - b\).',
            {
                'A': ('Reversed Subtraction', r'Tính nhầm \(b - a = -10 - 3 = -13\) thay vì \(a - b\).'),
                'B': ('Sign Error on Subtraction', r'Tính nhầm \(a + b = 3 + (-10) = -7\) do quên quy tắc trừ số âm thành cộng.'),
                'C': ('Đáp án đúng', r'Với \(a = 3\) và \(b = -10\), cả hai phương trình đều rút gọn thành \(3x - 4y = 7\), nên \(a - b = 3 - (-10) = 13\).'),
                'D': ('Constant Shift Sign Error', r'Giải nhầm \(b - 2 = -12 \implies b = -14\), dẫn tới \(3 - (-14) = 17\).'),
            },
            desmos_tip_vi=r'Gõ trực tiếp hồi quy tỉ số hai phương trình trên Desmos: \([2a/9,\; -8/(b - 2)] \sim [14/21,\; 14/21]\). Desmos trả ngay \(a = 3,\; b = -10\), gõ \(a - b\) ra \(13\). Hoặc vẽ thẳng hai đường \(2ax - 5y = 14 + 3y\) và \(9x + (b - 2)y = 21\) để kiểm chứng chúng trùng khít tại \(a = 3, b = -10\).',
        ),

        # Q3 — Hard, SPR, Advanced Math
        math_spr(
            'sat_boss_d5_q3', 3, DOM_ADV, SK_EQUIV, 'Hard',
            r'<p>\[(px^2 + qx + 6)(2x - r) = 8x^3 - 26x^2 + kx - 30\]</p>'
            r'<p>The equation above is true for all values of \(x\), where \(p\), \(q\), \(r\), and \(k\) are constants.</p>',
            r'<p>What is the value of \(k\)?</p>',
            ['27'], '27',
            r'<b>Bước 1 (Khai triển vế trái):</b><br/>'
            r'\[(px^2 + qx + 6)(2x - r) = 2px^3 + (2q - pr)x^2 + (12 - qr)x - 6r\]'
            r'<b>Bước 2 (Đồng nhất hệ số theo từng bậc của \(x\)):</b><br/>'
            r'- Bậc \(x^3\): \(2p = 8 \implies p = 4\).<br/>'
            r'- Hệ số tự do: \(-6r = -30 \implies r = 5\).<br/>'
            r'- Bậc \(x^2\): \(2q - pr = -26 \implies 2q - 4(5) = -26 \implies 2q = -6 \implies q = -3\).<br/>'
            r'- Bậc \(x\): \(k = 12 - qr = 12 - (-3)(5) = 12 + 15 = 27\).',
            r'Với đồng nhất thức đa thức 4 ẩn bậc 3, ghép hồi quy danh sách \(x_1 = [-2, -1, 0, 1, 2]\) (nhiều điểm hơn số ẩn) giúp Desmos giải đồng thời cả 4 tham số trong 1 dòng duy nhất.',
            desmos_tip_vi=r'Tạo danh sách 5 điểm bất kỳ \(x_1 = [-2, -1, 0, 1, 2]\), rồi gõ đúng một dòng hồi quy đồng nhất thức: \((px_1^2 + qx_1 + 6)(2x_1 - r) \sim 8x_1^3 - 26x_1^2 + kx_1 - 30\). Desmos lập tức trả \(p = 4,\; q = -3,\; r = 5,\; k = 27\) với \(R^2 = 1\)!',
        ),

        # Q4 — Hard, MCQ, Key=B, Advanced Math
        math_mcq(
            'sat_boss_d5_q4', 4, DOM_ADV, SK_EQUIV, 'Hard',
            r'<p>\[\frac{A}{2x - 3} + \frac{B}{x + 4} = \frac{3x + 34}{2x^2 + 5x - 12}\]</p>'
            r'<p>The equation above holds for all values of \(x\) except \(x = \frac{3}{2}\) and \(x = -4\), where \(A\) and \(B\) are constants.</p>',
            r'<p>What is the value of \(A - B\)?</p>',
            {
                'A': r'\(5\)',
                'B': r'\(9\)',
                'C': r'\(11\)',
                'D': r'\(14\)',
            },
            'B',
            r'<b>Bước 1 (Phân tích mẫu và quy đồng):</b> Nhận thấy \(2x^2 + 5x - 12 = (2x - 3)(x + 4)\). Nhân hai vế với mẫu chung:<br/>'
            r'\[A(x + 4) + B(2x - 3) = 3x + 34\]'
            r'<b>Bước 2 (Thay nghiệm mẫu — Heaviside Cover-Up):</b><br/>'
            r'- Thay \(x = -4\): \(A(0) + B(-8 - 3) = 3(-4) + 34 \implies -11B = 22 \implies B = -2\).<br/>'
            r'- Thay \(x = \frac{3}{2}\): \(A\left(\frac{3}{2} + 4\right) + B(0) = 3\left(\frac{3}{2}\right) + 34 \implies \frac{11}{2}A = \frac{77}{2} \implies A = 7\).<br/>'
            r'<b>Bước 3 (Tính \(A - B\)):</b> \(A - B = 7 - (-2) = 9\).',
            r'Phân tích phân thức hữu tỉ bằng mẹo thay nghiệm mẫu (Heaviside) hoặc hồi quy danh sách trên Desmos giúp loại bỏ hoàn toàn sai sót khi giải hệ.',
            {
                'A': ('Double-Negative Error', r'Tính nhầm \(7 - 2 = 5\) thay vì \(7 - (-2) = 9\) (tức tính nhầm \(A + B\)).'),
                'B': ('Đáp án đúng', r'Từ \(A = 7\) và \(B = -2\) suy ra \(A - B = 7 - (-2) = 9\).'),
                'C': ('Forgot Factor of 2 on B', r'Quên chia hệ số \(2\) của \(2B\) khi nhân chéo, tính nhầm \(A - 2B = 7 - (-4) = 11\).'),
                'D': ('Product Magnitude Trap', r'Nhân nhầm \(|A \cdot B| = |7(-2)| = 14\) (hoặc lấy \(2A = 14\)) thay vì hiệu \(A - B\).'),
            },
            desmos_tip_vi=r'Tạo danh sách tránh hai nghiệm mẫu \(x_1 = [-2, 0, 1, 3]\), rồi gõ hồi quy: \(a/(2x_1 - 3) + b/(x_1 + 4) \sim (3x_1 + 34)/(2x_1^2 + 5x_1 - 12)\). Desmos trả ngay \(a = 7,\; b = -2\) (\(R^2 = 1\)), gõ \(a - b\) ra \(9\) trong 10 giây!',
        ),

        # Q5 — Hard, MCQ, Key=D, Advanced Math
        math_mcq(
            'sat_boss_d5_q5', 5, DOM_ADV, SK_NONLIN_FUNC, 'Hard',
            f'<div style="margin-bottom:12px;">{tbl_q5}</div>'
            r'<p>The table above gives three points on the graph of \(y = f(x)\) in the \(xy\)-plane, where \(f(x) = a \cdot b^x + k\) and \(a\), \(b\), and \(k\) are constants with \(b > 0\).</p>',
            r'<p>What is the value of \(f(3)\)?</p>',
            {
                'A': r'\(81\)',
                'B': r'\(93\)',
                'C': r'\(111\)',
                'D': r'\(121\)',
            },
            'D',
            r'<b>Bước 1 (Khử hằng số dịch \(k\) bằng hiệu liên tiếp):</b><br/>'
            r'\[f(1) - f(0) = a(b - 1) = 1 - (-9) = 10\]'
            r'\[f(2) - f(1) = ab(b - 1) = 31 - 1 = 30\]'
            r'Chia hai đẳng thức: \(b = \frac{30}{10} = 3\).<br/>'
            r'<b>Bước 2 (Tìm \(a\) và \(k\)):</b> \(a(3 - 1) = 10 \implies a = 5\). Từ \(f(0) = a + k = -9 \implies k = -9 - 5 = -14\).<br/>'
            r'<b>Bước 3 (Tính \(f(3)\)):</b> \[f(3) = 5 \cdot 3^3 - 14 = 5(27) - 14 = 135 - 14 = 121.\]',
            r'Với hàm mũ có dịch đứng \(a \cdot b^x + k\), tỉ số của các HIỆU liên tiếp \(\frac{f(x+2)-f(x+1)}{f(x+1)-f(x)}\) luôn bằng đúng cơ số \(b\) (khác với hàm \(ab^x\) không có \(+k\)).',
            {
                'A': ('Quadratic Fit Trap', r'Nhầm sang hàm bậc hai có sai phân bậc hai không đổi (\(10, 30, 50\)), tính ra \(31 + 50 = 81\).'),
                'B': ('Ignored Vertical Shift k', r'Nhân thẳng \(f(2) \cdot 3 = 31 \cdot 3 = 93\) như thể hàm không có hằng số dịch \(k = -14\).'),
                'C': ('Confused y-Intercept with Asymptote', r'Nhầm \(f(0) = -9\) là tiệm cận ngang \(k\), tính \(3(31 - (-9)) + (-9) = 111\) thay vì dùng \(k = -14\).'),
                'D': ('Đáp án đúng', r'Hàm chính xác là \(f(x) = 5 \cdot 3^x - 14\), cho \(f(3) = 135 - 14 = 121\).'),
            },
            desmos_tip_vi=r'Nhập \(x_1 = [0, 1, 2]\) và \(y_1 = [-9, 1, 31]\), sau đó gõ hồi quy mũ có dịch đứng \(y_1 \sim a \cdot b^{x_1} + k\) (KHÔNG bật Log Mode). Desmos trả ngay \(a = 5,\; b = 3,\; k = -14\); gõ tiếp \(a \cdot b^3 + k\) ra ngay \(121\)!',
        ),

        # Q6 — Elite 750+, SPR, Algebra
        math_spr(
            'sat_boss_d5_q6', 6, DOM_ALG, SK_LIN_SYS, 'Elite 750+',
            r'<p>\[\begin{aligned} kx + 6y &= k + 6 \\ 2x + (k - 1)y &= 5 \end{aligned}\]</p>'
            r'<p>In the given system of equations, \(k\) is a constant. The system has <b>no solution</b>.</p>',
            r'<p>What is the value of \(k\)?</p>',
            ['-3'], '-3',
            r'<b>Bước 1 (Điều kiện song song — hệ số góc bằng nhau):</b> Hai đường thẳng song song hoặc trùng nhau khi định thức hệ số bằng \(0\):<br/>'
            r'\[k(k - 1) - 6(2) = 0 \implies k^2 - k - 12 = 0 \implies (k - 4)(k + 3) = 0 \implies k = 4 \text{ hoặc } k = -3.\]'
            r'<b>Bước 2 (Bẫy 800 — Loại nghiệm gây vô số nghiệm!):</b><br/>'
            r'- Với \(k = 4\): phương trình (1) là \(4x + 6y = 10 \iff 2x + 3y = 5\), trùng khít với phương trình (2) là \(2x + 3y = 5\) \(\implies\) <b>vô số nghiệm</b> (LOẠI!).<br/>'
            r'- Với \(k = -3\): phương trình (1) là \(-3x + 6y = 3 \iff 2x - 4y = -2\), còn phương trình (2) là \(2x - 4y = 5\). Vì \(-2 \neq 5\), hai đường thẳng song song tách biệt \(\implies\) <b>vô nghiệm</b> (NHẬN!).<br/>'
            r'Vậy giá trị duy nhất thỏa mãn là \(k = -3\).',
            r'Khi tham số \(k\) xuất hiện ở cả hai phương trình và giải ra 2 giá trị từ \(A_1 B_2 = A_2 B_1\), BẮT BUỘC thay ngược cả 2 giá trị để loại trường hợp trùng nhau (vô số nghiệm).',
            desmos_tip_vi=r'Gõ thẳng cả hai phương trình \(kx + 6y = k + 6\) và \(2x + (k - 1)y = 5\) lên Desmos, bấm thêm thanh trượt \(k\). Khi gõ \(k = 4\), hai đường trùng khít thành một (vô số nghiệm — loại!); khi gõ \(k = -3\), hai đường song song rõ rệt không bao giờ cắt nhau \(\implies\) chốt ngay \(k = -3\)!',
        ),

        # Q7 — Elite 750+, MCQ, Key=A, Advanced Math
        math_mcq(
            'sat_boss_d5_q7', 7, DOM_ADV, SK_NONLIN_EQ, 'Elite 750+',
            r'<p>\[\begin{aligned} (x - 5)^2 + (y + 2)^2 &= 25 \\ 3x - 4y &= k \end{aligned}\]</p>'
            r'<p>In the given system of equations, \(k\) is a constant. The system has <b>exactly one</b> real solution \((x, y)\).</p>',
            r'<p>What is the <b>least</b> possible value of \(k\)?</p>',
            {
                'A': r'\(-2\)',
                'B': r'\(18\)',
                'C': r'\(28\)',
                'D': r'\(48\)',
            },
            'A',
            r'<b>Cách 1 (Khoảng cách tâm–đường thẳng — Siêu tốc 15 giây):</b> Đường tròn có tâm \(I(5, -2)\) và bán kính \(R = \sqrt{25} = 5\). Hệ có đúng 1 nghiệm khi và chỉ khi đường thẳng \(3x - 4y - k = 0\) tiếp xúc với đường tròn, tức khoảng cách từ \(I\) đến đường thẳng bằng \(R\):<br/>'
            r'\[\frac{|3(5) - 4(-2) - k|}{\sqrt{3^2 + (-4)^2}} = 5 \implies \frac{|23 - k|}{5} = 5 \implies |23 - k| = 25\]'
            r'Suy ra \(23 - k = 25 \implies k = -2\), hoặc \(23 - k = -25 \implies k = 48\).<br/>'
            r'<b>Cách 2 (Thế đại số):</b> Thế \(y = \frac{3x - k}{4}\) vào đường tròn được \(25x^2 - (6k + 112)x + (8 - k)^2 = 0\), đặt \(\Delta = 0\) cho \((16k + 32)(-4k + 192) = 0 \implies k \in \{-2, 48\}\).<br/>'
            r'Giá trị nhỏ nhất (least possible value) của \(k\) là \(-2\) (tiếp điểm \((2, 2)\)).',
            r'Đường thẳng \(Ax + By = k\) tiếp xúc đường tròn tâm \((h, v)\) bán kính \(R\) \(\iff |Ah + Bv - k| = R\sqrt{A^2 + B^2}\) — nhanh gấp 5 lần khai triển biệt thức!',
            {
                'A': ('Đáp án đúng', r'Hai tiếp tuyến ứng với \(k = -2\) và \(k = 48\); giá trị nhỏ nhất là \(k = -2\).'),
                'B': ('Forgot Norm Factor 5', r'Quên nhân bán kính \(R = 5\) với \(\sqrt{3^2 + (-4)^2} = 5\), giải nhầm \(|23 - k| = 5 \implies k = 18\).'),
                'C': ('Forgot Norm Factor (Upper)', r'Cùng lỗi thiếu hệ số chuẩn hóa \(\sqrt{3^2 + 4^2} = 5\), lấy nhánh lớn \(23 + 5 = 28\).'),
                'D': ('Greatest Instead of Least', r'Chọn nhầm giá trị lớn nhất \(k = 48\) (tiếp điểm \((8, -6)\)) thay vì giá trị nhỏ nhất.'),
            },
            desmos_tip_vi=r'Vẽ đường tròn \((x - 5)^2 + (y + 2)^2 = 25\) và đường thẳng \(3x - 4y = k\), thêm thanh trượt \(k\) rồi đổi miền thanh trượt sang \([-10, 60]\) (hoặc nhập thẳng danh sách \(k = [-2, 18, 28, 48]\) để Desmos vẽ đồng loạt cả 4 đường!). Chỉ có \(k = -2\) và \(k = 48\) chạm đúng 1 điểm; chọn nhỏ nhất là \(-2\)!',
        ),

        # Q8 — Elite 750+, MCQ, Key=B, Advanced Math
        math_mcq(
            'sat_boss_d5_q8', 8, DOM_ADV, SK_NONLIN_EQ, 'Elite 750+',
            r'<p>\[\begin{aligned} y &= 2x^2 + 5x + 14 \\ y &= mx + 6 \end{aligned}\]</p>'
            r'<p>In the given system of equations, \(m\) is a <b>negative</b> constant. The system has <b>exactly one</b> real solution \((x, y)\).</p>',
            r'<p>What is the value of \(m\)?</p>',
            {
                'A': r'\(-13\)',
                'B': r'\(-3\)',
                'C': r'\(3\)',
                'D': r'\(13\)',
            },
            'B',
            r'<b>Bước 1 (Phương trình hoành độ giao điểm):</b><br/>'
            r'\[2x^2 + 5x + 14 = mx + 6 \implies 2x^2 + (5 - m)x + 8 = 0\]'
            r'<b>Bước 2 (Điều kiện tiếp xúc \(\Delta = 0\)):</b><br/>'
            r'\[\Delta = (5 - m)^2 - 4(2)(8) = 0 \implies (5 - m)^2 = 64 \implies 5 - m = \pm 8\]'
            r'Suy ra \(m = 5 - 8 = -3\) hoặc \(m = 5 + 8 = 13\).<br/>'
            r'<b>Bước 3 (Lọc điều kiện \(m < 0\)):</b> Vì đề bài yêu cầu \(m\) là hằng số âm, chọn \(m = -3\) (khi đó \(2(x + 2)^2 = 0\), tiếp điểm duy nhất là \((-2, 12)\)).',
            r'Khi đường thẳng \(y = mx + q\) tiếp xúc parabol \(y = ax^2 + bx + c\), phương trình \(\Delta = 0\) luôn tạo hai tiếp tuyến đối xứng về hệ số góc — đọc kỹ điều kiện dấu của \(m\).',
            {
                'A': ('Sign Error in Grouping x', r'Gộp nhầm \(5x - mx\) thành \((5 + m)x\), giải \((5 + m)^2 = 64\) lấy nhánh âm \(m = -13\).'),
                'B': ('Đáp án đúng', r'Từ \((5 - m)^2 = 64\) với \(m < 0\) thu được duy nhất \(m = -3\).'),
                'C': ('Final Sign Flip', r'Đổi nhầm dấu của nghiệm đúng \(-3\) thành \(3\).'),
                'D': ('Ignored Negative Constraint', r'Chọn nhầm nghiệm dương \(m = 13\) (tiếp điểm \((2, 32)\)) mà quên điều kiện \(m < 0\).'),
            },
            desmos_tip_vi=r'Vẽ parabol \(y = 2x^2 + 5x + 14\) và họ đường thẳng bằng danh sách \(m = [-13, -3, 3, 13]\), \(y = mx + 6\) (zoom rộng quanh \((0, 15)\)). Hoặc gõ thẳng phương trình biệt thức \((5 - x)^2 - 64 = 0\) lên Desmos để thấy hai đường đứng \(x = -3\) và \(x = 13\); lấy giá trị âm là \(-3\)!',
        ),

        # Q9 — Elite 750+, SPR, Algebra
        math_spr(
            'sat_boss_d5_q9', 9, DOM_ALG, SK_LIN_INEQ, 'Elite 750+',
            r'<p>\[\begin{aligned} 2x + 3y &\le 36 \\ 5x + 2y &\le 46 \end{aligned}\]</p>'
            r'<p>The ordered pair \((x, y)\) is a solution to the given system of inequalities.</p>',
            r'<p>What is the <b>maximum</b> possible value of \(7x + 6y\)?</p>',
            ['90'], '90',
            r'<b>Bước 1 (Tổ hợp tuyến tính dương — Duality):</b> Biểu diễn \(7x + 6y = u(2x + 3y) + v(5x + 2y)\):<br/>'
            r'\[\begin{cases} 2u + 5v = 7 \\ 3u + 2v = 6 \end{cases} \implies u = \frac{16}{11} > 0,\quad v = \frac{9}{11} > 0\]'
            r'Vì cả \(u > 0\) và \(v > 0\), nhân hai bất đẳng thức rồi cộng vế theo vế ta được chặn trên tuyệt đối:<br/>'
            r'\[7x + 6y \le \frac{16}{11}(36) + \frac{9}{11}(46) = \frac{576 + 414}{11} = \frac{990}{11} = 90.\]'
            r'<b>Bước 2 (Kiểm tra dấu bằng tại đỉnh giao điểm):</b> Giải hệ biên \(2x + 3y = 36\) và \(5x + 2y = 46\) được \(11x = 66 \implies x = 6,\; y = 8\). Tại \((6, 8)\), \(7(6) + 6(8) = 42 + 48 = 90\).',
            r'Với hệ hai bất phương trình tuyến tính, cực trị của hàm mục tiêu \(px + qy\) (khi hệ số góc \(-\frac{p}{q}\) nằm giữa hai hệ số góc biên) LUÔN đạt tại đúng giao điểm của hai đường biên!',
            desmos_tip_vi=r'Gõ thẳng hai bất phương trình \(2x + 3y \le 36\) và \(5x + 2y \le 46\) lên Desmos, bấm vào đỉnh giao điểm đậm nhất của hai đường biên thấy ngay tọa độ \((6, 8)\). Gõ tiếp \(7(6) + 6(8)\) ra \(90\) (có thể kiểm chứng bằng đường trượt \(7x + 6y = k\) đẩy lên cao nhất vẫn còn chạm miền chung).',
        ),

        # Q10 — Elite 750+, MCQ, Key=C, Advanced Math
        math_mcq(
            'sat_boss_d5_q10', 10, DOM_ADV, SK_NONLIN_FUNC, 'Elite 750+',
            f'<div style="margin-bottom:12px;">{tbl_q10}</div>'
            r'<p>For the quadratic function \(f(x) = ax^2 + bx + c\), where \(a\), \(b\), and \(c\) are constants, the table above shows three values of \(x\) and the corresponding values of \(f(x - 2)\).</p>',
            r'<p>What is the value of \(b\)?</p>',
            {
                'A': r'\(-9\)',
                'B': r'\(-1\)',
                'C': r'\(7\)',
                'D': r'\(14\)',
            },
            'C',
            r'<b>Bước 1 (Đổi biến về đầu vào thật của \(f\)):</b> Đặt \(t = x - 2\). Các cặp \((t, f(t))\) tương ứng với bảng là:<br/>'
            r'- Khi \(x = -2 \implies t = -4 \implies f(-4) = 9\).<br/>'
            r'- Khi \(x = 1 \implies t = -1 \implies f(-1) = 0\).<br/>'
            r'- Khi \(x = 3 \implies t = 1 \implies f(1) = 14\).<br/>'
            r'<b>Bước 2 (Tìm nhanh \(b\) bằng tính đối xứng \(-1\) và \(1\)):</b><br/>'
            r'Ta có \(f(1) = a + b + c = 14\) và \(f(-1) = a - b + c = 0\).<br/>'
            r'Trừ vế theo vế hai phương trình này lập tức triệt tiêu cả \(a\) và \(c\):<br/>'
            r'\[2b = f(1) - f(-1) = 14 - 0 = 14 \implies b = 7.\]'
            r'(Kiểm chứng thêm \(f(-4) = 16a - 4(7) + c = 9\) cùng \(a + c = 7 \implies a = 2,\; c = 5\), tức \(f(x) = 2x^2 + 7x + 5\).)',
            r'Khi bảng cho \(x\) và \(f(x - h)\), gõ trực tiếp hồi quy dạng dịch ngang \(y_1 \sim a(x_1 - h)^2 + b(x_1 - h) + c\) trên Desmos để không bao giờ bị dịch ngược dấu!',
            {
                'A': ('Wrong Shift Direction', r'Dịch ngược dấu thành \(y_1 \sim a(x_1 + 2)^2 + b(x_1 + 2) + c\), thu được \(b = -9\).'),
                'B': ('Ignored Horizontal Shift', r'Quên độ dịch \(x - 2\), hồi quy thẳng \(y_1 \sim ax_1^2 + bx_1 + c\) cho hàm \(g(x) = 2x^2 - x - 1\) và đọc nhầm \(-1\).'),
                'C': ('Đáp án đúng', r'Từ \(f(1) = 14\) và \(f(-1) = 0\) suy ra ngay \(2b = 14 \implies b = 7\).'),
                'D': ('Forgot to Divide by 2', r'Lấy nhầm \(f(1) - f(-1) = 14\) (chính là \(2b\) hoặc \(a + b + c\)) mà quên chia cho \(2\).'),
            },
            desmos_tip_vi=r'Gõ \(x_1 = [-2, 1, 3]\) và \(y_1 = [9, 0, 14]\), rồi nhập nguyên vẹn biểu thức dịch vào hồi quy: \(y_1 \sim a(x_1 - 2)^2 + b(x_1 - 2) + c\). Không cần đổi biến nháp tay — Desmos in thẳng \(a = 2,\; b = 7,\; c = 5\) với \(R^2 = 1\) trong 8 giây!',
        ),

        # Q11 — Elite 750+, MCQ, Key=D, Algebra
        math_mcq(
            'sat_boss_d5_q11', 11, DOM_ALG, SK_LIN_FUNC, 'Elite 750+',
            r'<p>\[p(x) = \begin{cases} ax + b & \text{if } x < 4 \\ 5x - 3a & \text{if } x \ge 4 \end{cases}\]</p>'
            r'<p>In the piecewise linear function \(p\) defined above, \(a\) and \(b\) are constants. The graph of \(y = p(x)\) has no jump or break at \(x = 4\) (meaning both expressions evaluate to the same value at \(x = 4\)), and \(p(-2) = -7\).</p>',
            r'<p>What is the value of \(p(8)\)?</p>',
            {
                'A': r'\(11\)',
                'B': r'\(13\)',
                'C': r'\(23\)',
                'D': r'\(31\)',
            },
            'D',
            r'<b>Bước 1 (Thiết lập hệ 2 phương trình cho \(a, b\)):</b><br/>'
            r'- Điều kiện liên tục (khớp nhau tại \(x = 4\)): \(a(4) + b = 5(4) - 3a \implies 4a + b = 20 - 3a \implies 7a + b = 20\).<br/>'
            r'- Vì \(-2 < 4\), dùng nhánh thứ nhất cho \(p(-2) = -7\): \(-2a + b = -7\).<br/>'
            r'<b>Bước 2 (Giải tìm \(a, b\)):</b> Lấy \((7a + b) - (-2a + b) = 20 - (-7) \implies 9a = 27 \implies a = 3\), suy ra \(b = 20 - 21 = -1\).<br/>'
            r'<b>Bước 3 (Chọn đúng nhánh tính \(p(8)\)):</b> Vì \(8 \ge 4\), dùng nhánh thứ hai:<br/>'
            r'\[p(8) = 5(8) - 3(3) = 40 - 9 = 31.\]',
            r'Với hàm ghép mảnh (piecewise), luôn giải hệ tại điểm nối + điểm đã biết để khóa tham số, rồi kiểm tra kỹ miền \(x \ge 4\) hay \(x < 4\) trước khi thay giá trị cuối.',
            {
                'A': ('Junction Value Trap', r'Tính nhầm giá trị tại điểm nối \(p(4) = 5(4) - 3(3) = 11\) thay vì \(p(8)\).'),
                'B': ('Continuity Sign Error', r'Chuyển vế sai dấu thành \(4a + b = 20 + 3a \implies a + b = 20\), giải ra \(a = 9\) rồi tính \(5(8) - 3(9) = 13\).'),
                'C': ('Wrong Branch Evaluation', r'Thay \(x = 8\) vào nhầm nhánh thứ nhất \(3(8) - 1 = 23\) thay vì nhánh \(x \ge 4\).'),
                'D': ('Đáp án đúng', r'Với \(a = 3,\; b = -1\) và \(8 \ge 4\), nhánh thứ hai cho \(p(8) = 5(8) - 3(3) = 31\).'),
            },
            desmos_tip_vi=r'Gõ thẳng hồi quy hệ 2 ẩn từ 2 điều kiện: \([4a + b - (20 - 3a),\; -2a + b] \sim [0,\; -7]\) để Desmos trả ngay \(a = 3,\; b = -1\). Sau đó định nghĩa hàm ghép mảnh \(p(x) = \{x < 4: ax + b,\; x \ge 4: 5x - 3a\}\) rồi gõ \(p(8)\) ra ngay \(31\)!',
        ),

        # Q12 — Elite 750+, SPR, Advanced Math
        math_spr(
            'sat_boss_d5_q12', 12, DOM_ADV, SK_EQUIV, 'Elite 750+',
            r'<p>\[(ax + b)(cx + d) = 15x^2 + kx + 14\]</p>'
            r'<p>The equation above is true for all values of \(x\), where \(a\), \(b\), \(c\), and \(d\) are <b>positive integers</b> and \(a + c = 8\).</p>',
            r'<p>What is the <b>greatest</b> possible value of \(k\)?</p>',
            ['73'], '73',
            r'<b>Bước 1 (Khóa cặp \(\{a, c\}\)):</b> Đồng nhất hệ số \(x^2\) và hằng số tự do:<br/>'
            r'\[ac = 15,\quad bd = 14,\quad k = ad + bc.\]'
            r'Vì \(a, c\) là các số nguyên dương thỏa mãn \(ac = 15\) và \(a + c = 8\), cặp duy nhất là \(\{a, c\} = \{3, 5\}\).<br/>'
            r'<b>Bước 2 (Tối đa hóa \(k = ad + bc\)):</b> Không mất tính tổng quát, gán \(a = 5,\; c = 3\). Các cặp số nguyên dương \((b, d)\) thỏa \(bd = 14\) là \((1, 14),\; (2, 7),\; (7, 2),\; (14, 1)\).<br/>'
            r'Thay lần lượt vào \(k = 5d + 3b\):<br/>'
            r'- \((b, d) = (1, 14) \implies k = 5(14) + 3(1) = 73\).<br/>'
            r'- \((b, d) = (2, 7) \implies k = 5(7) + 3(2) = 41\).<br/>'
            r'- \((b, d) = (7, 2) \implies k = 5(2) + 3(7) = 31\).<br/>'
            r'- \((b, d) = (14, 1) \implies k = 5(1) + 3(14) = 47\).<br/>'
            r'(Theo bất đẳng thức sắp xếp lại, ghép số lớn \(5\) với số lớn \(14\) luôn đạt cực đại). Vậy giá trị lớn nhất của \(k\) là \(73\).',
            r'Với \(k = ad + bc\) khi biết tích \(ac\) và \(bd\), cực đại LUÔN đạt khi ghép thừa số lớn nhất của \(ac\) với thừa số lớn nhất của \(bd\) (và danh sách Desmos kiểm tra toàn bộ tổ hợp trong 5 giây).',
            desmos_tip_vi=r'Từ \(ac = 15, a + c = 8 \implies \{a, c\} = \{5, 3\}\). Trên Desmos, gõ đúng 2 dòng bằng list: \(d = [1, 2, 7, 14]\) rồi \(5d + 3(14/d)\) — Desmos in tức thì cả 4 giá trị \([47, 31, 41, 73]\), đọc ngay cực đại \(73\) (hoặc bọc trong \(\max(5d + 3(14/d))\))!',
        ),

        # Q13 — Elite 750+, MCQ, Key=A, Algebra
        math_mcq(
            'sat_boss_d5_q13', 13, DOM_ALG, SK_LIN_EQ_2V, 'Elite 750+',
            r'<p>\[\begin{aligned} 3a + 2b - c &= -6 \\ a - 4b + 3c &= -4 \\ 2a + 5b + 2c &= 24 \end{aligned}\]</p>'
            r'<p>The ordered triple \((a, b, c)\) is the solution to the given system of three linear equations.</p>',
            r'<p>What is the value of \(a - b + c\)?</p>',
            {
                'A': r'\(-2\)',
                'B': r'\(2\)',
                'C': r'\(6\)',
                'D': r'\(12\)',
            },
            'A',
            r'<b>Bước 1 (Khử \(c\) từ phương trình (1)):</b> Từ (1) suy ra \(c = 3a + 2b + 6\).<br/>'
            r'<b>Bước 2 (Thế vào (2) và (3)):</b><br/>'
            r'- Vào (2): \(a - 4b + 3(3a + 2b + 6) = -4 \implies 10a + 2b = -22 \implies 5a + b = -11\).<br/>'
            r'- Vào (3): \(2a + 5b + 2(3a + 2b + 6) = 24 \implies 8a + 9b = 12\).<br/>'
            r'<b>Bước 3 (Giải hệ 2 ẩn \(a, b\)):</b> Từ \(b = -11 - 5a\), thế vào \(8a + 9(-11 - 5a) = 12 \implies -37a = 111 \implies a = -3\).<br/>'
            r'Suy ra \(b = -11 - 5(-3) = 4\) và \(c = 3(-3) + 2(4) + 6 = 5\).<br/>'
            r'<b>Bước 4 (Tính đích):</b> \(a - b + c = -3 - 4 + 5 = -2\).',
            r'Với hệ tuyến tính 3 ẩn \((a, b, c)\), hồi quy danh sách \([VT_1, VT_2, VT_3] \sim [VP_1, VP_2, VP_3]\) trên Desmos biến 3 phút khử Gauss thành đúng 12 giây không bao giờ sai dấu!',
            {
                'A': ('Đáp án đúng', r'Nghiệm duy nhất \((a, b, c) = (-3, 4, 5)\) cho \(a - b + c = -3 - 4 + 5 = -2\).'),
                'B': ('Sign Reversal', r'Đảo dấu biểu thức thành \(-a + b - c = 2\) hoặc lấy nhầm trị tuyệt đối \(|-2| = 2\).'),
                'C': ('Sum Instead of Alternating', r'Tính nhầm tổng \(a + b + c = -3 + 4 + 5 = 6\) thay vì trừ \(b\).'),
                'D': ('Dropped Negative on a', r'Quên dấu âm của \(a = -3\), cộng \(3 + 4 + 5 = 12\).'),
            },
            desmos_tip_vi=r'Bí kíp 800 Desmos giải hệ 3 ẩn (lưu ý KHÔNG dùng tên biến \(x, y\) trong hồi quy): gõ nguyên một dòng \([3a + 2b - c,\; a - 4b + 3c,\; 2a + 5b + 2c] \sim [-6,\; -4,\; 24]\). Desmos trả ngay \(a = -3,\; b = 4,\; c = 5\) với sai số \(0\); gõ tiếp \(a - b + c\) ra ngay \(-2\)!',
        ),

        # Q14 — Elite 750+, MCQ, Key=B, Advanced Math
        math_mcq(
            'sat_boss_d5_q14', 14, DOM_ADV, SK_NONLIN_EQ, 'Elite 750+',
            r'<p>\[\begin{aligned} y &= kx^2 - 4x + 13 \\ y &= 2x^2 + 8x + 4 \end{aligned}\]</p>'
            r'<p>In the given system of equations, \(k\) is a constant. The system has <b>exactly one</b> real solution \((x, y)\).</p>',
            r'<p>What is the <b>sum</b> of all possible values of \(k\)?</p>',
            {
                'A': r'\(6\)',
                'B': r'\(8\)',
                'C': r'\(12\)',
                'D': r'\(18\)',
            },
            'B',
            r'<b>Bước 1 (Phương trình hoành độ giao điểm):</b><br/>'
            r'\[kx^2 - 4x + 13 = 2x^2 + 8x + 4 \implies (k - 2)x^2 - 12x + 9 = 0\]'
            r'<b>Bước 2 (Xét ĐỦ cả hai trường hợp — Bẫy 800 kinh điển!):</b><br/>'
            r'- <b>Trường hợp 1 (Suy biến thành bậc nhất khi \(k - 2 = 0\)):</b> Khi \(k = 2\), phương trình trở thành \(-12x + 9 = 0 \implies x = \frac{3}{4}\) (và \(y = \frac{89}{8}\)). Hai parabol cùng độ mở \(2x^2\) cắt nhau tại <b>đúng 1 điểm</b> \(\implies k = 2\) THỎA MÃN!<br/>'
            r'- <b>Trường hợp 2 (Bậc hai tiếp xúc khi \(k \neq 2\) và \(\Delta = 0\)):</b><br/>'
            r'\[\Delta = (-12)^2 - 4(k - 2)(9) = 144 - 36(k - 2) = 0 \implies k - 2 = 4 \implies k = 6\]'
            r'(Khi \(k = 6\), \(4x^2 - 12x + 9 = (2x - 3)^2 = 0\), tiếp điểm duy nhất là \(\left(\frac{3}{2}, \frac{41}{2}\right)\)).<br/>'
            r'<b>Bước 3 (Tính tổng):</b> Tổng tất cả giá trị của \(k\) là \(2 + 6 = 8\).',
            r'BẤT CỨ KHI NÀO tham số nằm ở hệ số của \(x^2\) như \((k - a)x^2 + bx + c = 0\) và đề hỏi "exactly one real solution", BẮT BUỘC kiểm tra trường hợp hệ số \(x^2\) bằng \(0\) (\(k = a\)) trước khi xét \(\Delta = 0\)!',
            {
                'A': ('Missed Degenerate Linear Case', r'Chỉ giải \(\Delta = 0 \implies k = 6\) mà bỏ sót hoàn toàn trường hợp suy biến bậc nhất \(k = 2\) (bẫy chết người phổ biến nhất của câu 22!).'),
                'B': ('Đáp án đúng', r'Hai giá trị thỏa mãn là \(k = 2\) (phương trình bậc nhất 1 nghiệm) và \(k = 6\) (hai parabol tiếp xúc), tổng \(2 + 6 = 8\).'),
                'C': ('Product Instead of Sum', r'Tìm đúng cả hai giá trị \(2\) và \(6\) nhưng lấy tích \(2 \cdot 6 = 12\) thay vì tổng.'),
                'D': ('Forgot Factor 4 in Discriminant', r'Tính nhầm \(\Delta = b^2 - ac = 144 - 9(k - 2) = 0 \implies k = 18\).'),
            },
            desmos_tip_vi=r'Vẽ \(y = kx^2 - 4x + 13\) và \(y = 2x^2 + 8x + 4\) với thanh trượt \(k\). Khi kéo \(k = 6\), hai parabol tiếp xúc tại \((1.5, 20.5)\). Đừng vội chốt \(6\) — hãy gõ \(k = 2\) vào thanh trượt: hai parabol có cùng hệ số \(2x^2\) nên chỉ cắt nhau tại đúng 1 điểm \((0.75, 11.125)\)! Cộng cả hai: \(2 + 6 = 8\).',
        ),

        # Q15 — Elite 750+, SPR, Advanced Math
        math_spr(
            'sat_boss_d5_q15', 15, DOM_ADV, SK_NONLIN_FUNC, 'Elite 750+',
            f'<div style="margin-bottom:12px;">{tbl_q15}</div>'
            r'<p>The table above shows four values of \(x\) and their corresponding values of the cubic polynomial function \(p(x) = ax^3 + bx^2 + cx + d\), where \(a\), \(b\), \(c\), and \(d\) are constants.</p>',
            r'<p>What is the value of \(p(3)\)?</p>',
            ['22'], '22',
            r'<b>Bước 1 (Tận dụng tính đối xứng chẵn–lẻ của \(x = \pm 1,\; \pm 2\)):</b><br/>'
            r'Cộng các cặp đối xứng để tách riêng phần chẵn \((b, d)\):<br/>'
            r'- \(p(1) + p(-1) = 2(b + d) = 2 + 6 = 8 \implies b + d = 4\).<br/>'
            r'- \(p(2) + p(-2) = 2(4b + d) = 3 + (-13) = -10 \implies 4b + d = -5\).<br/>'
            r'Trừ vế theo vế: \(3b = -9 \implies b = -3\), suy ra \(d = 7\).<br/>'
            r'<b>Bước 2 (Tách phần lẻ \((a, c)\) bằng hiệu đối xứng):</b><br/>'
            r'- \(p(1) - p(-1) = 2(a + c) = 2 - 6 = -4 \implies a + c = -2\).<br/>'
            r'- \(p(2) - p(-2) = 2(8a + 2c) = 3 - (-13) = 16 \implies 4a + c = 4\).<br/>'
            r'Trừ vế theo vế: \(3a = 6 \implies a = 2\), suy ra \(c = -4\).<br/>'
            r'<b>Bước 3 (Tính \(p(3)\)):</b> Với \(p(x) = 2x^3 - 3x^2 - 4x + 7\):<br/>'
            r'\[p(3) = 2(27) - 3(9) - 4(3) + 7 = 54 - 27 - 12 + 7 = 22.\]',
            r'Một đa thức bậc 3 (4 tham số) được xác định duy nhất bởi 4 điểm bất kỳ: dùng hồi quy bậc 3 trên Desmos tốn 10 giây, còn giải tay cực nhanh nhờ tách tổng/hiệu cặp điểm đối xứng \(\pm x\).',
            desmos_tip_vi=r'Gõ hai danh sách \(x_1 = [-2, -1, 1, 2]\) và \(y_1 = [-13, 6, 2, 3]\), rồi chạy hồi quy bậc 3: \(y_1 \sim ax_1^3 + bx_1^2 + cx_1 + d\). Desmos trả ngay \(a = 2,\; b = -3,\; c = -4,\; d = 7\) (\(R^2 = 1\)); định nghĩa \(p(x) = ax^3 + bx^2 + cx + d\) rồi gõ \(p(3)\) ra ngay \(22\)!',
        ),
    ]

    return build_math_drill_json(
        '🔥 Math Boss Drill 5: Desmos Advanced Hacks — Multi-Param Regression & Identity Systems (15 câu 750–800)',
        '15 câu trùm cuối Hard M2 (Q16–Q22) • Hồi quy đa tham số ~, List Evaluation [...], Đồng nhất thức, Hệ tiếp xúc & Tối ưu hóa (750–800)',
        'Hard M2 Boss • 750–800 Sprint',
        qs,
        target_minutes=28,
    )


# ============================================================================
# BOSS DRILL 6: Parametric Quadratics, Integer Bounds & Disguised Substitutions
# Domain: Advanced Math ONLY (All 15 Qs)
# MCQ Key Distribution (10 MCQs): A=2, B=2, C=3, D=3 | SPR: Q3, Q6, Q9, Q12, Q15
# Difficulty: Q1–Q5 Hard, Q6–Q15 Elite 750+
# ============================================================================
def _build_boss_drill_6():
    svg_q8 = svg_parabola_vertex(
        h_lbl='3',
        k_lbl='f(3)',
        opens_up=True,
        pt_lbl='zeros: -2, 8',
        note='Graph of y = f(x) in the xy-plane (not to scale)',
    )

    qs = [
        # Q1 — Hard, MCQ, Key=C, Advanced Math
        math_mcq(
            'sat_boss_d6_q1', 1, DOM_ADV, SK_NONLIN_EQ, 'Hard',
            r'<p>\[4x^2 - 24x + k = 7\]</p>'
            r'<p>In the given equation, \(k\) is an integer constant. The equation has <b>two distinct real solutions</b>.</p>',
            r'<p>What is the <b>greatest</b> possible integer value of \(k\)?</p>',
            {
                'A': r'\(28\)',
                'B': r'\(35\)',
                'C': r'\(42\)',
                'D': r'\(43\)',
            },
            'C',
            r'<b>Bước 1 (Đưa về vế phải bằng \(0\)):</b><br/>'
            r'\[4x^2 - 24x + (k - 7) = 0\]'
            r'<b>Bước 2 (Điều kiện 2 nghiệm thực phân biệt \(\Delta > 0\) NGHIÊM NGẶT):</b><br/>'
            r'\[\Delta = (-24)^2 - 4(4)(k - 7) > 0 \implies 576 - 16(k - 7) > 0\]'
            r'Chia cả hai vế cho \(16\): \(36 - (k - 7) > 0 \implies 43 - k > 0 \implies k < 43\).<br/>'
            r'<b>Bước 3 (Bẫy bất đẳng thức nghiêm ngặt):</b> Tại \(k = 43\), \(\Delta = 0\) nên phương trình chỉ có <b>1 nghiệm kép</b> (\(4(x - 3)^2 = 0\)). Vì đề yêu cầu 2 nghiệm phân biệt và \(k\) nguyên, giá trị nguyên lớn nhất là \(k = 42\).',
            r'Khi nghiệm biên của \(\Delta = 0\) là một số nguyên chẵn đẹp, câu hỏi "two distinct real solutions" (\(\Delta > 0\)) hay "no real solutions" (\(\Delta < 0\)) LUÔN đặt bẫy chênh 1 đơn vị tại đúng giá trị biên đó!',
            {
                'A': ('Opposite Sign on RHS 7', r'Chuyển vế sai dấu thành \(k + 7\) nên giải \(k + 7 < 36 \implies k < 29\), chọn nhầm \(28\).'),
                'B': ('Ignored RHS 7', r'Quên số \(7\) ở vế phải, giải \(576 - 16k > 0 \implies k < 36\) nên chọn nhầm \(35\).'),
                'C': ('Đáp án đúng', r'Từ \(k < 43\) với bất đẳng thức nghiêm ngặt, số nguyên lớn nhất là \(42\).'),
                'D': ('Strict Inequality Boundary Trap', r'Lấy nhầm giá trị biên \(k = 43\) — khi đó \(\Delta = 0\) chỉ cho 1 nghiệm kép thay vì 2 nghiệm phân biệt.'),
            },
            desmos_tip_vi=r'Vẽ parabol \(y = 4x^2 - 24x + k\) và đường ngang \(y = 7\), thêm thanh trượt \(k\) (bước nhảy \(1\)). Kéo \(k\) tới \(43\), đỉnh parabol \((3, 7)\) chỉ chạm đường \(y = 7\) tại 1 điểm (LOẠI); lùi xuống 1 nấc còn \(k = 42\), đỉnh tụt xuống \((3, 6)\) nên cắt \(y = 7\) tại đúng 2 điểm phân biệt!',
        ),

        # Q2 — Hard, MCQ, Key=D, Advanced Math
        math_mcq(
            'sat_boss_d6_q2', 2, DOM_ADV, SK_NONLIN_EQ, 'Hard',
            r'<p>\[3x^4 - 23x^2 - 36 = 0\]</p>'
            r'<p>Consider all <b>real</b> solutions to the given quartic equation.</p>',
            r'<p>What is the <b>sum of the squares</b> of all real solutions to the given equation?</p>',
            {
                'A': r'\(0\)',
                'B': r'\(\frac{23}{3}\)',
                'C': r'\(9\)',
                'D': r'\(18\)',
            },
            'D',
            r'<b>Bước 1 (Đặt ẩn phụ trùng phương \(u = x^2 \ge 0\)):</b> Phương trình trở thành:<br/>'
            r'\[3u^2 - 23u - 36 = 0 \implies (3u + 4)(u - 9) = 0\]'
            r'Suy ra \(u = -\frac{4}{3}\) hoặc \(u = 9\).<br/>'
            r'<b>Bước 2 (Lọc điều kiện nghiệm thực \(x^2 \ge 0\)):</b><br/>'
            r'- Với \(x^2 = -\frac{4}{3} < 0\): <b>vô nghiệm thực</b> (LOẠI!).<br/>'
            r'- Với \(x^2 = 9\): có <b>hai nghiệm thực phân biệt</b> là \(x = -3\) và \(x = 3\).<br/>'
            r'<b>Bước 3 (Tính tổng bình phương các nghiệm thực):</b><br/>'
            r'\[(-3)^2 + 3^2 = 9 + 9 = 18.\]',
            r'Với phương trình trùng phương \(ax^4 + bx^2 + c = 0\), tuyệt đối không dùng mù Viète cho \(u = x^2\) vì: (1) nghiệm \(u < 0\) không sinh nghiệm thực, và (2) mỗi \(u > 0\) sinh tới HAI nghiệm thực \(\pm\sqrt{u}\)!',
            {
                'A': ('Sum of Roots Instead of Squares', r'Tính tổng hai nghiệm thực \(-3 + 3 = 0\) thay vì tổng bình phương \((-3)^2 + 3^2\).'),
                'B': ('Blind Vieta on u Trap', r'Áp dụng máy móc \(u_1 + u_2 = \frac{23}{3}\) mà không loại nghiệm âm \(u = -\frac{4}{3}\) và quên nhân đôi cho hai nghiệm \(\pm 3\).'),
                'C': ('Counted x² Only Once', r'Thấy \(x^2 = 9\) rồi chọn ngay \(9\), quên rằng có HAI nghiệm thực phân biệt là \(x = 3\) và \(x = -3\), mỗi nghiệm đóng góp \(9\).'),
                'D': ('Đáp án đúng', r'Hai nghiệm thực duy nhất là \(x = -3\) và \(x = 3\), tổng bình phương là \((-3)^2 + 3^2 = 18\).'),
            },
            desmos_tip_vi=r'Vẽ trực tiếp \(y = 3x^4 - 23x^2 - 36\) trên Desmos. Đồ thị chỉ cắt trục \(Ox\) tại đúng 2 điểm \(x = -3\) và \(x = 3\) (nhánh nghiệm ảo \(x^2 = -4/3\) tự động bị loại sạch trên đồ thị thực!). Bấm \((-3)^2 + 3^2 = 18\).',
        ),

        # Q3 — Hard, SPR, Advanced Math
        math_spr(
            'sat_boss_d6_q3', 3, DOM_ADV, SK_NONLIN_EQ, 'Hard',
            r'<p>\[3x^2 - 15x + 4 = 0\]</p>'
            r'<p>In the given equation, \(r\) and \(s\) are the two real solutions.</p>',
            r'<p>What is the value of \(\frac{r}{s} + \frac{s}{r}\)?</p>',
            ['67/4', '16.75'], '67/4 (or 16.75)',
            r'<b>Bước 1 (Kiểm tra nghiệm thực khác \(0\) và áp dụng Viète):</b><br/>'
            r'Biệt thức \(\Delta = (-15)^2 - 4(3)(4) = 225 - 48 = 177 > 0\), nên phương trình có hai nghiệm thực phân biệt khác \(0\) (vì \(c = 4 \neq 0\)):<br/>'
            r'\[r + s = -\frac{-15}{3} = 5,\qquad rs = \frac{4}{3}.\]'
            r'<b>Bước 2 (Quy đồng về biểu thức đối xứng của \(r + s\) và \(rs\)):</b><br/>'
            r'\[\frac{r}{s} + \frac{s}{r} = \frac{r^2 + s^2}{rs} = \frac{(r + s)^2 - 2rs}{rs} = \frac{(r + s)^2}{rs} - 2\]'
            r'<b>Bước 3 (Thay số chính xác):</b><br/>'
            r'\[\frac{5^2}{4/3} - 2 = \frac{25 \cdot 3}{4} - 2 = \frac{75}{4} - \frac{8}{4} = \frac{67}{4} = 16.75.\]',
            r'Bất kỳ biểu thức đối xứng nào như \(r^2 + s^2\), \(\frac{1}{r} + \frac{1}{s}\), hay \(\frac{r}{s} + \frac{s}{r} = \frac{(r+s)^2}{rs} - 2\) đều rút gọn siêu nhanh bằng Viète mà không bao giờ cần tính căn \(\sqrt{177}\)!',
            desmos_tip_vi=r'CẢNH BÁO PRO: Không dùng số làm tròn 3 chữ số từ điểm cắt trục \(Ox\) (vì \(s \approx 0.283\) nhỏ nên chia \(r/s\) sẽ bị sai số!). Thay vào đó gõ công thức nghiệm chính xác trên Desmos: \(r = (15 + \sqrt{177})/6\), \(s = (15 - \sqrt{177})/6\), rồi gõ \(r/s + s/r\) \(\implies\) hiện chính xác \(16.75\), bấm nút phân số ra \(67/4\)!',
        ),

        # Q4 — Hard, MCQ, Key=A, Advanced Math
        math_mcq(
            'sat_boss_d6_q4', 4, DOM_ADV, SK_NONLIN_EQ, 'Hard',
            r'<p>\[2(x - 3)^2 + 15(x - 3) + 7 = 0\]</p>'
            r'<p>The given equation has two distinct real solutions.</p>',
            r'<p>What is the <b>product</b> of all solutions to the given equation?</p>',
            {
                'A': r'\(-10\)',
                'B': r'\(-\frac{3}{2}\)',
                'C': r'\(\frac{7}{2}\)',
                'D': r'\(10\)',
            },
            'A',
            r'<b>Cách 1 (Đặt ẩn phụ \(u = x - 3\)):</b> Phương trình trở thành:<br/>'
            r'\[2u^2 + 15u + 7 = 0 \implies (2u + 1)(u + 7) = 0 \implies u = -\frac{1}{2} \text{ hoặc } u = -7.\]'
            r'Trả về biến \(x = u + 3\):<br/>'
            r'- \(x_1 = -\frac{1}{2} + 3 = \frac{5}{2}\).<br/>'
            r'- \(x_2 = -7 + 3 = -4\).<br/>'
            r'Tích các nghiệm là: \(x_1 x_2 = \left(\frac{5}{2}\right)(-4) = -10\).<br/>'
            r'<b>Cách 2 (Khai triển tìm hằng số tự do):</b> \(2(x^2 - 6x + 9) + 15x - 45 + 7 = 2x^2 + 3x - 20 = 0\). Theo Viète, tích hai nghiệm là \(\frac{-20}{2} = -10\).',
            r'Trong phương trình ẩn phụ dạng \(a(x - h)^2 + b(x - h) + c = 0\), công thức Viète \(\frac{c}{a}\) chỉ là tích của \(u = x - h\), TUYỆT ĐỐI KHÔNG phải tích của \(x\) — luôn trả về \(x = u + h\) trước khi nhân!',
            {
                'A': ('Đáp án đúng', r'Hai nghiệm thật của \(x\) là \(\frac{5}{2}\) và \(-4\), có tích \(\frac{5}{2}(-4) = -10\).'),
                'B': ('Sum Instead of Product', r'Tính nhầm tổng hai nghiệm \(\frac{5}{2} + (-4) = -\frac{3}{2}\) thay vì tích hai nghiệm.'),
                'C': ('Vieta on u Instead of x', r'Lấy nhầm \(\frac{c}{a} = \frac{7}{2}\) (chính là tích \(u_1 u_2\)) mà quên cộng lại \(3\) để ra \(x_1, x_2\).'),
                'D': ('Sign Error', r'Quên dấu âm của nghiệm \(x_2 = -4\), nhân nhầm \(\frac{5}{2} \cdot 4 = 10\).'),
            },
            desmos_tip_vi=r'Gõ thẳng \(y = 2(x - 3)^2 + 15(x - 3) + 7\) vào Desmos mà không cần khai triển. Bấm 2 giao điểm trục \(Ox\) đọc ngay \(x = -4\) và \(x = 2.5\), gõ \((-4)(2.5)\) ra \(-10\) trong 6 giây!',
        ),

        # Q5 — Hard, MCQ, Key=B, Advanced Math
        math_mcq(
            'sat_boss_d6_q5', 5, DOM_ADV, SK_NONLIN_FUNC, 'Hard',
            r'<p>\[p(x) = x^3 + ax^2 + bx - 10\]</p>'
            r'<p>In the polynomial function \(p\) defined above, \(a\) and \(b\) are constants. The binomial \((x - 2)\) is a factor of \(p(x)\), and the remainder when \(p(x)\) is divided by \((x + 1)\) is \(12\).</p>',
            r'<p>What is the value of \(a + b\)?</p>',
            {
                'A': r'\(-15\)',
                'B': r'\(-7\)',
                'C': r'\(8\)',
                'D': r'\(21\)',
            },
            'B',
            r'<b>Bước 1 (Áp dụng Định lý Nhân tử & Định lý Số dư):</b><br/>'
            r'- Vì \((x - 2)\) là nhân tử của \(p(x)\), ta có \(p(2) = 0\):<br/>'
            r'\[2^3 + a(2)^2 + b(2) - 10 = 0 \implies 4a + 2b - 2 = 0 \implies 2a + b = 1.\]'
            r'- Vì phép chia \(p(x)\) cho \((x + 1)\) dư \(12\), ta có \(p(-1) = 12\):<br/>'
            r'\[(-1)^3 + a(-1)^2 + b(-1) - 10 = 12 \implies a - b - 11 = 12 \implies a - b = 23.\]'
            r'<b>Bước 2 (Giải hệ tìm \(a, b\)):</b> Cộng hai phương trình \((2a + b) + (a - b) = 1 + 23 \implies 3a = 24 \implies a = 8\).<br/>'
            r'Thay vào \(a - b = 23 \implies b = 8 - 23 = -15\).<br/>'
            r'<b>Bước 3 (Tính \(a + b\)):</b> \(a + b = 8 + (-15) = -7\).',
            r'Ghi nhớ cặp công cụ vàng: chia hết cho \((x - r) \iff p(r) = 0\); chia cho \((x - r)\) dư \(R \iff p(r) = R\). Cực kỳ chú ý đổi dấu nghiệm khi nhân tử là \((x + 1) \implies r = -1\)!',
            {
                'A': ('Stopped at b Only', r'Tìm đúng \(b = -15\) rồi chọn luôn mà quên cộng thêm \(a = 8\).'),
                'B': ('Đáp án đúng', r'Giải hệ \(2a + b = 1\) và \(a - b = 23\) cho \(a = 8,\; b = -15\), suy ra \(a + b = -7\).'),
                'C': ('Stopped at a Only', r'Tìm đúng \(a = 8\) rồi dừng lại, quên cộng với \(b = -15\).'),
                'D': ('Sign Error on (x + 1)', r'Bẫy kinh điển: thay nhầm \(x = +1\) thay vì \(x = -1\) vào \(p(1) = 12\), dẫn tới \(1 + a + b - 10 = 12 \implies a + b = 21\).'),
            },
            desmos_tip_vi=r'Định nghĩa đa thức ngay trên Desmos không cần rút gọn tay: gõ hồi quy hai điều kiện \([2^3 + a(2)^2 + b(2) - 10,\; (-1)^3 + a(-1)^2 + b(-1) - 10] \sim [0,\; 12]\). Desmos trả tức thì \(a = 8,\; b = -15\); gõ \(a + b\) ra \(-7\)!',
        ),

        # Q6 — Elite 750+, SPR, Advanced Math
        math_spr(
            'sat_boss_d6_q6', 6, DOM_ADV, SK_NONLIN_EQ, 'Elite 750+',
            r'<p>\[3x - 7\sqrt{x + 2} = 14\]</p>'
            r'<p>The given radical equation has a unique real solution \(x\).</p>',
            r'<p>What is the value of \(x\)?</p>',
            ['14'], '14',
            r'<b>Bước 1 (Đặt ẩn phụ căn \(u = \sqrt{x + 2} \ge 0\)):</b> Khi đó \(u^2 = x + 2 \implies x = u^2 - 2\).<br/>'
            r'Thay vào phương trình ban đầu:<br/>'
            r'\[3(u^2 - 2) - 7u = 14 \implies 3u^2 - 7u - 20 = 0 \implies (3u + 5)(u - 4) = 0\]'
            r'<b>Bước 2 (Loại nghiệm ngoại lai bằng điều kiện \(u \ge 0\)):</b><br/>'
            r'- \(u = -\frac{5}{3} < 0\): <b>LOẠI</b> ngay lập tức vì căn bậc hai số học luôn không âm (nếu bình phương trực tiếp sẽ sinh nghiệm ngoại lai \(x = \frac{7}{9}\) khiến \(3x - 14 < 0\)).<br/>'
            r'- \(u = 4 \ge 0\): nhận! Suy ra \(\sqrt{x + 2} = 4 \implies x + 2 = 16 \implies x = 14\).<br/>'
            r'<b>Bước 3 (Kiểm chứng):</b> \(3(14) - 7\sqrt{14 + 2} = 42 - 7(4) = 42 - 28 = 14\) (đúng tuyệt đối!).',
            r'Với phương trình dạng \(ax + b\sqrt{x + c} = d\), đặt \(u = \sqrt{x + c} \ge 0\) và thay \(x = u^2 - c\) vừa giải nhanh hơn bình phương hai vế vừa chặn đứng 100% nghiệm ngoại lai.',
            desmos_tip_vi=r'Vẽ đồng thời \(y = 3x - 7\sqrt{x + 2}\) và \(y = 14\) trên Desmos. Hai đồ thị chỉ cắt nhau tại đúng một điểm duy nhất \((14, 14)\) \(\implies\) chốt ngay \(x = 14\) (Desmos tự động loại sạch nghiệm ngoại lai \(x = 7/9\))!',
        ),

        # Q7 — Elite 750+, MCQ, Key=C, Advanced Math
        math_mcq(
            'sat_boss_d6_q7', 7, DOM_ADV, SK_NONLIN_EQ, 'Elite 750+',
            r'<p>\[2^{2x + 1} - 33(2^x) + 16 = 0\]</p>'
            r'<p>The given exponential equation has two distinct real solutions.</p>',
            r'<p>What is the <b>sum</b> of all solutions to the given equation?</p>',
            {
                'A': r'\(-4\)',
                'B': r'\(2\)',
                'C': r'\(3\)',
                'D': r'\(4\)',
            },
            'C',
            r'<b>Bước 1 (Tách lũy thừa và đặt ẩn phụ \(u = 2^x > 0\)):</b><br/>'
            r'Chú ý \(2^{2x + 1} = 2^1 \cdot 2^{2x} = 2(2^x)^2 = 2u^2\). Phương trình trở thành:<br/>'
            r'\[2u^2 - 33u + 16 = 0 \implies (2u - 1)(u - 16) = 0\]'
            r'<b>Bước 2 (Giải tìm cả hai nghiệm \(x\)):</b><br/>'
            r'- \(u = \frac{1}{2} \implies 2^x = 2^{-1} \implies x = -1\).<br/>'
            r'- \(u = 16 \implies 2^x = 2^4 \implies x = 4\).<br/>'
            r'<b>Bước 3 (Mẹo Viète siêu tốc & Tổng nghiệm):</b> \(x_1 + x_2 = -1 + 4 = 3\).<br/>'
            r'(Mẹo 800: Vì cả hai nghiệm \(u_1, u_2 > 0\), ta có \(2^{x_1 + x_2} = u_1 u_2 = \frac{16}{2} = 8 = 2^3 \implies x_1 + x_2 = 3\) mà không cần phân tích nhân tử!)',
            r'Với phương trình bậc hai theo \(2^x\) dạng \(A(2^x)^2 + B(2^x) + C = 0\) có 2 nghiệm dương \(u_1, u_2\), tổng các nghiệm \(x\) luôn thỏa \(2^{x_1 + x_2} = \frac{C}{A}\); nhớ tách chuẩn \(2^{2x+1} = 2(2^x)^2\)!',
            {
                'A': ('Product Instead of Sum', r'Tìm đúng hai nghiệm \(-1\) và \(4\) nhưng lấy tích \((-1)(4) = -4\) thay vì tổng.'),
                'B': ('Exponent Split Error', r'Tách nhầm \(2^{2x + 1}\) thành \(4(2^x)^2\), khiến \(u_1 u_2 = \frac{16}{4} = 4 \implies x_1 + x_2 = 2\).'),
                'C': ('Đáp án đúng', r'Hai nghiệm là \(x = -1\) và \(x = 4\), tổng bằng \(-1 + 4 = 3\).'),
                'D': ('Dropped Negative Root or Coefficient 2', r'Loại nhầm nghiệm âm \(x = -1\) (nhầm \(2^x > 0\) với \(x > 0\)), hoặc quên hệ số \(2\) của \(2^{2x+1}\) ra \(\log_2(16) = 4\).'),
            },
            desmos_tip_vi=r'Vẽ trực tiếp \(y = 2^{2x + 1} - 33 \cdot 2^x + 16\) trên Desmos. Bấm vào hai giao điểm với trục \(Ox\) thấy ngay \((-1, 0)\) và \((4, 0)\) \(\implies\) tổng \(-1 + 4 = 3\) trong 5 giây!',
        ),

        # Q8 — Elite 750+, MCQ, Key=D, Advanced Math
        math_mcq(
            'sat_boss_d6_q8', 8, DOM_ADV, SK_NONLIN_FUNC, 'Elite 750+',
            f'<div style="display:flex;justify-content:center;margin-bottom:12px;">{svg_q8}</div>'
            r'<p>For the quadratic function \(f(x) = ax^2 + bx + c\), where \(a\), \(b\), and \(c\) are constants and \(a\) is a <b>positive integer</b>, \(f(-2) = f(8) = 0\) and \(f(x) \ge -125\) for all real values of \(x\).</p>',
            r'<p>What is the <b>greatest</b> possible value of \(f(9)\)?</p>',
            {
                'A': r'\(5\)',
                'B': r'\(11\)',
                'C': r'\(44\)',
                'D': r'\(55\)',
            },
            'D',
            r'<b>Bước 1 (Dạng tích và tọa độ đỉnh parabol):</b> Vì \(f(-2) = f(8) = 0\), viết dạng tích:<br/>'
            r'\[f(x) = a(x + 2)(x - 8)\]'
            r'Do tính đối xứng, hoành độ đỉnh nằm chính giữa hai nghiệm: \(h = \frac{-2 + 8}{2} = 3\). Vì \(a > 0\), giá trị nhỏ nhất của \(f(x)\) đạt tại đỉnh:<br/>'
            r'\[f(3) = a(3 + 2)(3 - 8) = -25a.\]'
            r'<b>Bước 2 (Chặn nguyên cho \(a\) từ điều kiện đỉnh):</b> Điều kiện \(f(x) \ge -125\) với mọi \(x \in \mathbb{R}\) tương đương với giá trị nhỏ nhất \(\ge -125\):<br/>'
            r'\[-25a \ge -125 \implies a \le 5.\]'
            r'Vì \(a\) là số nguyên dương, \(a \in \{1, 2, 3, 4, 5\}\), lớn nhất là \(a = 5\).<br/>'
            r'<b>Bước 3 (Tính cực đại của \(f(9)\)):</b><br/>'
            r'\[f(9) = a(9 + 2)(9 - 8) = 11a \le 11(5) = 55.\]',
            r'Gặp \(f(r_1) = f(r_2) = 0\) kèm chặn đỉnh \(f(x) \ge M\), lập tức dùng \(f(x) = a(x - r_1)(x - r_2)\) và đặt \(f\left(\frac{r_1 + r_2}{2}\right) \ge M\) để khóa giá trị cực đại của \(a\).',
            {
                'A': ('Stopped at Parameter a', r'Tìm đúng số nguyên lớn nhất \(a = 5\) rồi chọn luôn mà quên tính \(f(9) = 11a\).'),
                'B': ('Assumed Monic a = 1', r'Bỏ quên hệ số \(a\), tính nhầm \((9 + 2)(9 - 8) = 11\) như thể \(a = 1\).'),
                'C': ('Misread >= as Strict >', r'Đọc nhầm dấu \(\ge -125\) thành nghiêm ngặt \(> -125\), chọn nhầm \(a = 4 \implies f(9) = 44\).'),
                'D': ('Đáp án đúng', r'Vì \(-25a \ge -125 \iff a \le 5\), giá trị lớn nhất đạt tại \(a = 5\) cho \(f(9) = 5(11)(1) = 55\).'),
            },
            desmos_tip_vi=r'Gõ \(f(x) = a(x + 2)(x - 8)\) và đường biên \(y = -125\), cài đặt thanh trượt \(a\) với bước nhảy \(1\). Tăng \(a\) nguyên lớn nhất sao cho đáy parabol không tụt dưới \(y = -125\) \(\implies\) chạm khít tại \(a = 5\). Gõ \(f(9)\) ra ngay \(55\)!',
        ),

        # Q9 — Elite 750+, SPR, Advanced Math
        math_spr(
            'sat_boss_d6_q9', 9, DOM_ADV, SK_NONLIN_FUNC, 'Elite 750+',
            r'<p>\[f(x) = a \cdot b^x + c\]</p>'
            r'<p>In the function \(f\) defined above, \(a\), \(b\), and \(c\) are constants with \(b > 1\). In the \(xy\)-plane, as \(x\) decreases without bound, the value of \(f(x)\) approaches \(-11\). The graph of \(y = f(x)\) has a \(y\)-intercept at \((0, -6)\) and passes through the point \((2, 34)\).</p>'
            r'<p>The function \(g\) is defined by \(g(x) = f(x + 1) + 9\).</p>',
            r'<p>What is the \(y\)-coordinate of the \(y\)-intercept of the graph of \(y = g(x)\)?</p>',
            ['13'], '13',
            r'<b>Bước 1 (Đọc hằng số tiệm cận \(c\)):</b> Vì \(b > 1\), khi \(x \to -\infty\) ta có \(b^x \to 0\), do đó \(f(x) \to c\). Từ giả thiết tiệm cận ngang \(y = -11\), suy ra \(c = -11\).<br/>'
            r'<b>Bước 2 (Tìm \(a\) từ giao trục \(Oy\)):</b><br/>'
            r'\[f(0) = a \cdot b^0 + (-11) = -6 \implies a - 11 = -6 \implies a = 5.\]'
            r'<b>Bước 3 (Tìm cơ số \(b > 1\) từ điểm \((2, 34)\)):</b><br/>'
            r'\[f(2) = 5 \cdot b^2 - 11 = 34 \implies 5b^2 = 45 \implies b^2 = 9 \implies b = 3 \text{ (vì } b > 1\text{)}.\]'
            r'<b>Bước 4 (Tính \(g(0)\)):</b> Với \(f(x) = 5 \cdot 3^x - 11\):<br/>'
            r'\[g(0) = f(0 + 1) + 9 = f(1) + 9 = (5 \cdot 3^1 - 11) + 9 = 4 + 9 = 13.\]',
            r'Với hàm mũ dịch \(f(x) = a \cdot b^x + c\) (\(b > 1\)): tiệm cận ngang khi \(x \to -\infty\) luôn là \(y = c\), còn tung độ gốc là \(f(0) = a + c\) (KHÔNG phải \(a\))!',
            desmos_tip_vi=r'Chốt ngay \(c = -11\) từ tiệm cận ngang. Nhập 2 điểm \(x_1 = [0, 2]\), \(y_1 = [-6, 34]\) và gõ hồi quy \(y_1 \sim a \cdot b^{x_1} - 11\) (Desmos cho \(a = 5,\; b = 3\)). Định nghĩa \(f(x) = a \cdot b^x - 11\) và \(g(x) = f(x + 1) + 9\), rồi gõ \(g(0)\) ra ngay \(13\)!',
        ),

        # Q10 — Elite 750+, MCQ, Key=A, Advanced Math
        math_mcq(
            'sat_boss_d6_q10', 10, DOM_ADV, SK_NONLIN_EQ, 'Elite 750+',
            r'<p>\[x^2 + (k - 4)x + (k - 1) = 0\]</p>'
            r'<p>In the given equation, \(k\) is an integer constant. The equation has <b>no real solutions</b>.</p>',
            r'<p>How many integer values of \(k\) satisfy this condition?</p>',
            {
                'A': r'\(7\)',
                'B': r'\(8\)',
                'C': r'\(9\)',
                'D': r'\(10\)',
            },
            'A',
            r'<b>Bước 1 (Lập bất phương trình biệt thức \(\Delta < 0\)):</b><br/>'
            r'\[\Delta = (k - 4)^2 - 4(1)(k - 1) < 0\]'
            r'Khai triển và thu gọn:<br/>'
            r'\[(k^2 - 8k + 16) - (4k - 4) < 0 \implies k^2 - 12k + 20 < 0\]'
            r'<b>Bước 2 (Phân tích nhân tử để giải bất phương trình bậc hai theo \(k\)):</b><br/>'
            r'\[(k - 2)(k - 10) < 0 \iff 2 < k < 10.\]'
            r'<b>Bước 3 (Đếm chính xác các giá trị nguyên NGHIÊM NGẶT):</b><br/>'
            r'Vì tại \(k = 2\) (cho \((x - 1)^2 = 0\)) và \(k = 10\) (cho \((x + 3)^2 = 0\)), phương trình có 1 nghiệm thực nên CẢ HAI ĐẦU MÚT đều bị loại.<br/>'
            r'Tập các số nguyên thỏa mãn là \(\{3, 4, 5, 6, 7, 8, 9\}\), gồm đúng \(9 - 3 + 1 = 7\) giá trị.',
            r'Khi đếm số nguyên nằm NGHIÊM NGẶT giữa hai số nguyên \(m < k < n\), công thức chuẩn là \((n - m) - 1\) (không phải \(n - m\) hay \(n - m + 1\))!',
            {
                'A': ('Đáp án đúng', r'Khoảng nghiệm là \(2 < k < 10\), chứa đúng \(7\) số nguyên: \(3, 4, 5, 6, 7, 8, 9\).'),
                'B': ('Fencepost Error', r'Lấy hiệu hai đầu mút \(10 - 2 = 8\) mà quên trừ thêm \(1\) do dấu bất đẳng thức nghiêm ngặt ở cả hai đầu.'),
                'C': ('Inclusive Endpoints Trap', r'Đếm cả \(k = 2\) và \(k = 10\) (\(10 - 2 + 1 = 9\)), quên rằng tại hai biên này \(\Delta = 0\) có 1 nghiệm thực.'),
                'D': ('Read Upper Bound as Count', r'Nhìn nghiệm lớn \(k = 10\) rồi chọn nhầm \(10\) làm số lượng giá trị nguyên.'),
            },
            desmos_tip_vi=r'Gõ thẳng hàm biệt thức theo biến \(x\) (đại diện cho \(k\)): \(y = (x - 4)^2 - 4(x - 1)\). Bấm 2 giao điểm với trục \(Ox\) là \((2, 0)\) và \((10, 0)\); phần đồ thị chìm dưới trục \(Ox\) (\(y < 0\)) nằm gọn trong \((2, 10)\) \(\implies\) đếm các số nguyên \(3, 4, 5, 6, 7, 8, 9\) là \(7\) giá trị!',
        ),

        # Q11 — Elite 750+, MCQ, Key=C, Advanced Math
        math_mcq(
            'sat_boss_d6_q11', 11, DOM_ADV, SK_NONLIN_EQ, 'Elite 750+',
            r'<p>\[3|2x - 5| + 2x = k\]</p>'
            r'<p>In the given equation, \(k\) is a constant. The equation has <b>exactly one</b> real solution.</p>',
            r'<p>What is the value of \(k\)?</p>',
            {
                'A': r'\(0\)',
                'B': r'\(\frac{5}{2}\)',
                'C': r'\(5\)',
                'D': r'\(15\)',
            },
            'C',
            r'<b>Bước 1 (Phân nhánh hàm vế trái \(g(x) = 3|2x - 5| + 2x\) tại điểm gãy \(x = \frac{5}{2}\)):</b><br/>'
            r'- Khi \(x \ge \frac{5}{2}\): \(g(x) = 3(2x - 5) + 2x = 8x - 15\) (đồng biến với hệ số góc \(+8 > 0\)).<br/>'
            r'- Khi \(x < \frac{5}{2}\): \(g(x) = 3(5 - 2x) + 2x = 15 - 4x\) (nghịch biến với hệ số góc \(-4 < 0\)).<br/>'
            r'<b>Bước 2 (Tìm giá trị cực tiểu tại đỉnh chữ V):</b><br/>'
            r'Vì đồ thị giảm liên tục về phía \(x = \frac{5}{2}\) rồi tăng liên tục sau \(x = \frac{5}{2}\), \(g(x)\) đạt giá trị nhỏ nhất duy nhất tại đỉnh \(x = \frac{5}{2}\):<br/>'
            r'\[g\!\left(\frac{5}{2}\right) = 3\left|2\left(\frac{5}{2}\right) - 5\right| + 2\left(\frac{5}{2}\right) = 0 + 5 = 5.\]'
            r'<b>Bước 3 (Biện luận số nghiệm theo \(k\)):</b> Với \(k < 5\) có \(0\) nghiệm; với \(k > 5\) có \(2\) nghiệm; đường thẳng \(y = k\) chỉ cắt đồ thị tại <b>đúng 1 điểm</b> khi đi qua đúng đỉnh, tức \(k = 5\).',
            r'Với phương trình dạng \(a|bx + c| + dx = k\) (khi \(|ab| > |d|\)), đồ thị vế trái là hình chữ V bất đối xứng — phương trình có đúng 1 nghiệm khi và chỉ khi \(k\) bằng tung độ đỉnh tại \(bx + c = 0\)!',
            {
                'A': ('Zero RHS Reflex Trap', r'Nhớ máy móc "|...| = 0 có 1 nghiệm" nên chọn \(k = 0\), quên mất số hạng \(+2x\) ngoài dấu giá trị tuyệt đối.'),
                'B': ('x-Coordinate of Vertex', r'Giải đúng điểm gãy \(x = \frac{5}{2}\) nhưng chọn nhầm hoành độ \(x\) thay vì giá trị \(k = g(5/2)\).'),
                'C': ('Đáp án đúng', r'Đỉnh chữ V nằm tại \(\left(\frac{5}{2}, 5\right)\), nên \(k = 5\) là giá trị duy nhất cho đúng 1 nghiệm thực.'),
                'D': ('y-Intercept Confusion', r'Tính nhầm tung độ gốc \(g(0) = 3|-5| + 0 = 15\) thay vì tung độ cực tiểu tại đỉnh.'),
            },
            desmos_tip_vi=r'Gõ thẳng \(y = 3|2x - 5| + 2x\) lên Desmos, bấm ngay vào điểm gãy (đỉnh nhọn đáy chữ V) sẽ thấy tọa độ \((2.5, 5)\). Đường ngang \(y = k\) chỉ chạm đúng 1 điểm tại đỉnh này \(\implies\) chốt ngay \(k = 5\) trong 5 giây!',
        ),

        # Q12 — Elite 750+, SPR, Advanced Math
        math_spr(
            'sat_boss_d6_q12', 12, DOM_ADV, SK_NONLIN_EQ, 'Elite 750+',
            r'<p>\[kx^2 - (2k + 7)x + (k + 6) = 0\]</p>'
            r'<p>In the given equation, \(k\) is a nonzero constant. The equation has two real solutions \(r\) and \(s\) such that \(\frac{1}{r} + \frac{1}{s} = \frac{5}{3}\).</p>',
            r'<p>What is the value of \(k\)?</p>',
            ['9'], '9',
            r'<b>Bước 1 (Rút gọn \(\frac{1}{r} + \frac{1}{s}\) bằng Viète — Khử sạch \(k\) ở mẫu!):</b><br/>'
            r'Theo Viète, \(r + s = \frac{2k + 7}{k}\) và \(rs = \frac{k + 6}{k}\) (điều kiện \(k \neq 0,\; k \neq -6\) để \(r, s \neq 0\)). Do đó:<br/>'
            r'\[\frac{1}{r} + \frac{1}{s} = \frac{r + s}{rs} = \frac{(2k + 7)/k}{(k + 6)/k} = \frac{2k + 7}{k + 6}.\]'
            r'<b>Bước 2 (Giải tìm \(k\)):</b><br/>'
            r'\[\frac{2k + 7}{k + 6} = \frac{5}{3} \implies 3(2k + 7) = 5(k + 6) \implies 6k + 21 = 5k + 30 \implies k = 9.\]'
            r'<b>Bước 3 (Kiểm tra bắt buộc \(\Delta \ge 0\)):</b> Khi \(k = 9\), phương trình là \(9x^2 - 25x + 15 = 0\) có \(\Delta = (-25)^2 - 4(9)(15) = 625 - 540 = 85 > 0\), chắc chắn có 2 nghiệm thực phân biệt khác \(0\).',
            r'Công thức tắt 800 cực mạnh: với mọi phương trình bậc hai \(ax^2 + bx + c = 0\) (\(c \neq 0\)), tổng nghịch đảo hai nghiệm luôn là \(\frac{1}{r} + \frac{1}{s} = -\frac{b}{c}\) — hoàn toàn độc lập với hệ số đầu \(a\)!',
            desmos_tip_vi=r'Dùng mẹo Viète \(\frac{1}{r} + \frac{1}{s} = -\frac{b}{c} = \frac{2k + 7}{k + 6}\). Trên Desmos gõ hồi quy 1 dòng \((2k + 7)/(k + 6) \sim 5/3\) (hoặc vẽ giao điểm của \(y = (2x + 7)/(x + 6)\) và \(y = 5/3\)) ra ngay \(k = 9\), sau đó vẽ \(y = 9x^2 - 25x + 15\) xác nhận có 2 giao điểm trục \(Ox\)!',
        ),

        # Q13 — Elite 750+, MCQ, Key=B, Advanced Math
        math_mcq(
            'sat_boss_d6_q13', 13, DOM_ADV, SK_NONLIN_EQ, 'Elite 750+',
            r'<p>\[\sqrt{4x + 12} = x + k\]</p>'
            r'<p>In the given equation, \(k\) is a constant.</p>',
            r'<p>What is the <b>greatest</b> possible value of \(k\) for which the equation has <b>exactly one</b> real solution?</p>',
            {
                'A': r'\(3\)',
                'B': r'\(4\)',
                'C': r'\(5\)',
                'D': r'\(12\)',
            },
            'B',
            r'<b>Bước 1 (Phân tích hình học của \(y = \sqrt{4x + 12}\) và đường thẳng \(y = x + k\)):</b><br/>'
            r'Đồ thị \(y = \sqrt{4x + 12}\) là nửa parabol nằm ngang bắt đầu từ điểm mút \((-3, 0)\) đi lên về phía phải. Đường thẳng \(y = x + k\) có hệ số góc \(+1\) trượt lên xuống theo \(k\).<br/>'
            r'<b>Bước 2 (Tìm ngưỡng tiếp xúc cực đại bằng \(\Delta = 0\)):</b> Bình phương hai vế (với điều kiện \(x + k \ge 0\)):<br/>'
            r'\[4x + 12 = (x + k)^2 \implies x^2 + (2k - 4)x + (k^2 - 12) = 0\]'
            r'Tính biệt thức:<br/>'
            r'\[\Delta = (2k - 4)^2 - 4(k^2 - 12) = (4k^2 - 16k + 16) - 4k^2 + 48 = 64 - 16k\]'
            r'Đặt \(\Delta = 0 \implies 64 - 16k = 0 \implies k = 4\).<br/>'
            r'<b>Bước 3 (Kiểm tra điều kiện nghiệm thật & đầy đủ các miền của \(k\)):</b><br/>'
            r'- Khi \(k > 4\): \(\Delta < 0 \implies 0\) nghiệm.<br/>'
            r'- Khi \(k = 4\): \(x^2 + 4x + 4 = 0 \implies x = -2\), kiểm tra \(x + k = -2 + 4 = 2 \ge 0\) và \(\sqrt{4(-2) + 12} = 2\) (thỏa mãn!) \(\implies\) <b>đúng 1 nghiệm</b>.<br/>'
            r'- Khi \(3 \le k < 4\): đường thẳng cắt cả 2 lần \(\implies 2\) nghiệm (ví dụ tại điểm mút \(k = 3\), hai nghiệm là \(x = -3\) và \(x = 1\)).<br/>'
            r'- Khi \(k < 3\): có \(1\) nghiệm.<br/>'
            r'Vậy giá trị <b>lớn nhất</b> của \(k\) để phương trình có đúng 1 nghiệm thực là \(k = 4\).',
            r'Với phương trình căn \(\sqrt{ax + b} = x + k\), có hai vùng sinh đúng 1 nghiệm: vùng đi dưới điểm mút (\(k < -x_{\text{mút}}\)) và điểm tiếp xúc cực đại tại \(\Delta = 0\) — luôn kiểm tra \(x + k \ge 0\) tại tiếp điểm!',
            {
                'A': ('Endpoint Gives 2 Solutions Trap', r'Tại \(k = 3\), đường thẳng đi qua điểm mút \((-3, 0)\) nhưng còn cắt nhánh cong thêm một lần nữa tại \((1, 4)\), tức có tới 2 nghiệm thực.'),
                'B': ('Đáp án đúng', r'Tại \(k = 4\), đường thẳng tiếp xúc duy nhất với đồ thị căn tại \((-2, 2)\); mọi \(k > 4\) đều vô nghiệm.'),
                'C': ('Exceeded Tangency Bound', r'Cộng nhầm thêm \(1\) thành \(k = 5\); khi đó \(\Delta = -16 < 0\) khiến phương trình vô nghiệm.'),
                'D': ('Constant Inside Radical Trap', r'Đọc nhầm hằng số \(12\) bên trong dấu căn thành giá trị cực đại của \(k\).'),
            },
            desmos_tip_vi=r'Vẽ \(y = \sqrt{4x + 12}\) và \(y = x + k\) với thanh trượt \(k\). Khi trượt \(k\) tăng dần: \(k < 3\) có 1 giao điểm; \(3 \le k < 4\) có 2 giao điểm; tại đúng \(k = 4\), đường thẳng tiếp xúc đẹp tại \((-2, 2)\) cho đúng 1 giao điểm; \(k > 4\) tách hẳn lên trên (0 giao điểm). Chốt ngay \(k = 4\)!',
        ),

        # Q14 — Elite 750+, MCQ, Key=D, Advanced Math
        math_mcq(
            'sat_boss_d6_q14', 14, DOM_ADV, SK_NONLIN_FUNC, 'Elite 750+',
            r'<p>\[h(x) = a\left(\frac{1}{2}\right)^x + c\]</p>'
            r'<p>In the function \(h\) defined above, \(a\) and \(c\) are constants. In the \(xy\)-plane, as \(x\) increases without bound, the value of \(h(x)\) approaches \(-15\). The \(y\)-intercept of the graph of \(y = h(x)\) is \((0, -7)\), and the graph passes through \((-3, m)\).</p>',
            r'<p>What is the value of \(m\)?</p>',
            {
                'A': r'\(-71\)',
                'B': r'\(-14\)',
                'C': r'\(33\)',
                'D': r'\(49\)',
            },
            'D',
            r'<b>Bước 1 (Xác định \(c\) từ tiệm cận ngang khi \(x \to +\infty\)):</b><br/>'
            r'Vì cơ số \(0 < \frac{1}{2} < 1\), khi \(x \to +\infty\) thì \(\left(\frac{1}{2}\right)^x \to 0\), do đó \(h(x) \to c\). Từ giả thiết suy ra \(c = -15\).<br/>'
            r'<b>Bước 2 (Xác định \(a\) từ tung độ gốc \((0, -7)\)):</b><br/>'
            r'\[h(0) = a\left(\frac{1}{2}\right)^0 + (-15) = -7 \implies a - 15 = -7 \implies a = 8.\]'
            r'<b>Bước 3 (Tính \(m = h(-3)\) bằng quy tắc số mũ âm):</b><br/>'
            r'\[m = h(-3) = 8\left(\frac{1}{2}\right)^{-3} - 15 = 8 \cdot 2^3 - 15 = 8(8) - 15 = 64 - 15 = 49.\]',
            r'Với hàm mũ suy giảm \(a\left(\frac{1}{b}\right)^x + c\), tiệm cận ngang xảy ra khi \(x \to +\infty\) (khác chiều với \(b > 1\)), luôn giải \(a + c = y_{\text{intercept}}\) thay vì gán nhầm \(a = y_{\text{intercept}}\)!',
            {
                'A': ('Set a Equal to y-Intercept', r'Gán nhầm \(a = -7\) trực tiếp từ \((0, -7)\) thay vì giải \(a - 15 = -7\), tính ra \(-7(8) - 15 = -71\).'),
                'B': ('Positive Exponent Sign Error', r'Thay nhầm \(x = +3\) thay vì \(x = -3\), tính \(8\left(\frac{1}{8}\right) - 15 = -14\).'),
                'C': ('Linearized Exponent 2×3', r'Tính nhầm \(\left(\frac{1}{2}\right)^{-3} = 2 \cdot 3 = 6\) thay vì \(2^3 = 8\), dẫn tới \(8(6) - 15 = 33\).'),
                'D': ('Đáp án đúng', r'Với \(a = 8\) và \(c = -15\), ta có \(h(-3) = 8 \cdot 2^3 - 15 = 64 - 15 = 49\).'),
            },
            desmos_tip_vi=r'Từ tiệm cận ngang \(c = -15\), gõ \(h(x) = a(0.5)^x - 15\) rồi giải nhanh \(h(0) \sim -7\) (Desmos trả \(a = 8\)). Sau đó gõ \(h(-3)\) để Desmos tính tự động số mũ âm ra ngay \(49\)!',
        ),

        # Q15 — Elite 750+, SPR, Advanced Math
        math_spr(
            'sat_boss_d6_q15', 15, DOM_ADV, SK_NONLIN_FUNC, 'Elite 750+',
            r'<p>In the \(xy\)-plane, the graph of the quadratic function \(y = f(x)\) has its vertex at \((5, k)\), passes through the point \((1, 21)\), and intersects the \(x\)-axis at two points \((r, 0)\) and \((s, 0)\) such that \(|r - s| = 6\).</p>',
            r'<p>What is the value of \(k\)?</p>',
            ['-27'], '-27',
            r'<b>Cách 1 (Đối xứng trục — 20 giây):</b><br/>'
            r'Vì đỉnh là \((5, k)\), trục đối xứng của parabol là \(x = 5\). Hai nghiệm \(r, s\) đối xứng qua \(x = 5\) và cách nhau \(|r - s| = 6\), nên mỗi nghiệm cách trục đối xứng đúng \(\frac{6}{2} = 3\) đơn vị:<br/>'
            r'\[r = 5 - 3 = 2,\qquad s = 5 + 3 = 8.\]'
            r'Viết hàm dưới dạng tích \(f(x) = a(x - 2)(x - 8)\) và thay điểm \((1, 21)\):<br/>'
            r'\[21 = a(1 - 2)(1 - 8) = a(-1)(-7) = 7a \implies a = 3.\]'
            r'Do đó tung độ đỉnh là:<br/>'
            r'\[k = f(5) = 3(5 - 2)(5 - 8) = 3(3)(-3) = -27.\]'
            r'<b>Cách 2 (Dạng đỉnh thuần túy):</b> Từ \(f(x) = a(x - 5)^2 + k\), nghiệm cách đỉnh \(3\) đơn vị cho \(0 = a(3)^2 + k \implies k = -9a\). Thay \((1, 21)\): \(21 = a(1 - 5)^2 + k = 16a - 9a = 7a \implies a = 3 \implies k = -27\).',
            r'Biết hoành độ đỉnh \(h\) và khoảng cách giữa hai nghiệm \(d = |r - s|\), ta lập tức xác định chính xác hai nghiệm là \(h - \frac{d}{2}\) và \(h + \frac{d}{2}\) — biến bài toán ẩn tham số thành dạng tích siêu gọn!',
            desmos_tip_vi=r'Từ trục đối xứng \(x = 5\) và khoảng cách hai nghiệm \(6\), chốt ngay 2 nghiệm \(2\) và \(8\). Trên Desmos gõ \(f(x) = a(x - 2)(x - 8)\), giải hệ số \(a\) bằng hồi quy 1 điểm \(21 \sim a(1 - 2)(1 - 8)\) ra ngay \(a = 3\), rồi gõ \(f(5)\) nhận kết quả \(-27\)!',
        ),
    ]

    return build_math_drill_json(
        '🔥 Math Boss Drill 6: Parametric Quadratics, Integer Bounds & Disguised Substitutions (15 câu 750–800)',
        '15 câu trùm cuối Hard M2 Advanced Math • Chặn nguyên biệt thức, Ẩn phụ bậc cao/căn/mũ, Viète nâng cao, Định lý nhân tử & Tiệm cận mũ (750–800)',
        'Hard M2 Boss • 750–800 Sprint',
        qs,
        target_minutes=28,
    )


def get_drills():
    """Returns the 2 Hard/Elite Math Boss Drills (5 & 6) as (drill_key, title, order_index, content_json)."""
    d5 = _build_boss_drill_5()
    d6 = _build_boss_drill_6()
    return [
        ('boss_drill_5', d5['basicInfo']['title'], 5, d5),
        ('boss_drill_6', d6['basicInfo']['title'], 6, d6),
    ]


# ============================================================================
# 100% PROGRAMMATIC EXACT-ARITHMETIC VERIFICATION OF ALL 30 ELITE QUESTIONS
# ============================================================================
def _extract_all_strings(obj):
    if isinstance(obj, str):
        yield obj
    elif isinstance(obj, dict):
        for v in obj.values():
            yield from _extract_all_strings(v)
    elif isinstance(obj, (list, tuple)):
        for item in obj:
            yield from _extract_all_strings(item)


def _check_latex_and_hygiene(drills):
    bad_ctrl_re = re.compile(r'[\x08\x0c\r\t]')
    bad_dollar_re = re.compile(r'\$(?![0-9])')
    for key, title, order_idx, cj in drills:
        qs = cj['drillModule']['questions']
        for q in qs:
            qid = q['id']
            if q['questionFormat'] == 'spr':
                cd = q.get('correctDisplay', '')
                assert r'\(' not in cd and r'\[' not in cd, f"{qid}: correctDisplay must be plain text, got {cd}"
            for s in _extract_all_strings(q):
                assert not bad_ctrl_re.search(s), f"{qid}: Stray control char (unescaped LaTeX?) in {s!r}"
                assert '$$' not in s, f"{qid}: Found $$ delimiter in {s!r}"
                assert not bad_dollar_re.search(s), f"{qid}: Non-currency $ delimiter in {s!r}"
                assert s.count(r'\(') == s.count(r'\)'), f"{qid}: Unbalanced inline math delimiters in {s!r}"
                assert s.count(r'\[') == s.count(r'\]'), f"{qid}: Unbalanced display math delimiters in {s!r}"


def _q_by_id(drills):
    mp = {}
    for _, _, _, cj in drills:
        for q in cj['drillModule']['questions']:
            mp[q['id']] = q
    return mp


def _correct_opt_text(q):
    lbl = q['correctAnswer']
    for o in q['options']:
        if o['label'] == lbl:
            return o['text']
    raise AssertionError(f"Missing correct option for {q['id']}")


def verify_all_math():
    """Programmatically verifies structure, LaTeX hygiene, and exact math for all 30 Boss Drill 5 & 6 questions."""
    drills = get_drills()
    assert len(drills) == 2, f"Expected 2 drills, got {len(drills)}"

    expected_meta = [
        (
            'boss_drill_5',
            '🔥 Math Boss Drill 5: Desmos Advanced Hacks — Multi-Param Regression & Identity Systems (15 câu 750–800)',
            5,
            {'A': 3, 'B': 3, 'C': 2, 'D': 2},
            {DOM_ALG, DOM_ADV},
        ),
        (
            'boss_drill_6',
            '🔥 Math Boss Drill 6: Parametric Quadratics, Integer Bounds & Disguised Substitutions (15 câu 750–800)',
            6,
            {'A': 2, 'B': 2, 'C': 3, 'D': 3},
            {DOM_ADV},
        ),
    ]

    for (k, t, idx, cj), (ek, et, eidx, exp_keys, allowed_domains) in zip(drills, expected_meta):
        assert (k, t, idx) == (ek, et, eidx), f"Drill metadata mismatch: {(k, t, idx)} != {(ek, et, eidx)}"
        qs = cj['drillModule']['questions']
        assert len(qs) == 15, f"{k}: expected 15 questions, got {len(qs)}"
        mcq_counts = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
        spr_nums = []
        seen_domains = set()
        for pos, q in enumerate(qs, start=1):
            assert q['id'] == f'sat_boss_d{eidx}_q{pos}', f"Bad id {q['id']}"
            assert q['number'] == pos
            assert q['domain'] in allowed_domains, f"{q['id']}: bad domain {q['domain']}"
            seen_domains.add(q['domain'])
            assert q['difficulty'] in ('Hard', 'Elite 750+'), f"{q['id']}: non-boss difficulty {q['difficulty']}"
            exp = q['explanation']
            assert len(exp.get('summaryVi', '').strip()) >= 40, f"{q['id']}: short summaryVi"
            assert len(exp.get('desmosTipVi', '').strip()) >= 30, f"{q['id']}: missing/short desmosTipVi"
            assert len(exp.get('keyTakeaway', '').strip()) >= 25, f"{q['id']}: missing/short keyTakeaway"
            if q['questionFormat'] == 'spr':
                spr_nums.append(pos)
            else:
                ans = q['correctAnswer']
                mcq_counts[ans] += 1
                for lbl in ('A', 'B', 'C', 'D'):
                    oa = exp['optionAnalysis'][lbl]
                    assert oa.get('trapTag'), f"{q['id']}[{lbl}] missing trapTag"
        assert spr_nums == [3, 6, 9, 12, 15], f"{k}: SPR positions {spr_nums}"
        assert mcq_counts == exp_keys, f"{k}: MCQ key distribution {mcq_counts} != {exp_keys}"
        assert seen_domains == allowed_domains, f"{k}: domains {seen_domains} != expected {allowed_domains}"

    _check_latex_and_hygiene(drills)
    qm = _q_by_id(drills)

    # ==================================================================
    # BOSS DRILL 5 EXACT ARITHMETIC ASSERTIONS (Q1..Q15)
    # ==================================================================
    # D5 Q1: f(x) = ax^2 + bx + c; f(-1)+11=33, f(2)+11=0, f(5)+11=21 => a=3, b=-14, c=5 => a+b+c=-6
    a5_1 = (Fraction(21 - 0, 5 - 2) - Fraction(0 - 33, 2 - (-1))) / (5 - (-1))
    b5_1 = Fraction(0 - 33, 2 - (-1)) - a5_1 * (2 + (-1))
    c5_1 = 0 - 11 - a5_1 * 4 - b5_1 * 2
    assert (a5_1, b5_1, c5_1) == (3, -14, 5)
    for xv, yv in [(-1, 33), (2, 0), (5, 21)]:
        assert a5_1 * xv**2 + b5_1 * xv + c5_1 + 11 == yv
    assert a5_1 + b5_1 + c5_1 == -6
    assert qm['sat_boss_d5_q1']['correctAnswer'] == 'A' and '-6' in _correct_opt_text(qm['sat_boss_d5_q1'])

    # D5 Q2: 2ax - 5y = 14 + 3y => 2ax - 8y = 14; 9x + (b - 2)y = 21 => inf many solns => a=3, b=-10, a-b=13
    ratio5_2 = Fraction(14, 21)
    a5_2 = ratio5_2 * 9 / 2
    b5_2 = Fraction(-8, ratio5_2) + 2
    assert (a5_2, b5_2) == (3, -10) and a5_2 - b5_2 == 13
    assert Fraction(2 * a5_2, 9) == Fraction(-8, b5_2 - 2) == Fraction(14, 21)
    assert qm['sat_boss_d5_q2']['correctAnswer'] == 'C' and '13' in _correct_opt_text(qm['sat_boss_d5_q2'])

    # D5 Q3 (SPR): (px^2 + qx + 6)(2x - r) = 8x^3 - 26x^2 + kx - 30 => p=4, r=5, q=-3, k=27
    p5_3 = Fraction(8, 2)
    r5_3 = Fraction(-30, -6)
    q5_3 = Fraction(-26 + p5_3 * r5_3, 2)
    k5_3 = 12 - q5_3 * r5_3
    assert (p5_3, q5_3, r5_3, k5_3) == (4, -3, 5, 27)
    for x in range(-4, 6):
        assert (p5_3 * x**2 + q5_3 * x + 6) * (2 * x - r5_3) == 8 * x**3 - 26 * x**2 + k5_3 * x - 30
    assert qm['sat_boss_d5_q3']['acceptedAnswers'] == ['27']

    # D5 Q4: A/(2x-3) + B/(x+4) = (3x+34)/(2x^2+5x-12) => A=7, B=-2, A-B=9
    B5_4 = Fraction(3 * (-4) + 34, 2 * (-4) - 3)
    A5_4 = Fraction(3 * Fraction(3, 2) + 34, Fraction(3, 2) + 4)
    assert (A5_4, B5_4) == (7, -2) and A5_4 - B5_4 == 9
    for x in [-5, -2, 0, 1, 2, 5]:
        assert Fraction(A5_4, 2 * x - 3) + Fraction(B5_4, x + 4) == Fraction(3 * x + 34, 2 * x**2 + 5 * x - 12)
    assert qm['sat_boss_d5_q4']['correctAnswer'] == 'B' and '9' in _correct_opt_text(qm['sat_boss_d5_q4'])

    # D5 Q5: f(x) = a*b^x + k; f(0)=-9, f(1)=1, f(2)=31 => b=3, a=5, k=-14 => f(3)=121
    b5_5 = Fraction(31 - 1, 1 - (-9))
    a5_5 = Fraction(1 - (-9), b5_5 - 1)
    k5_5 = -9 - a5_5
    assert (a5_5, b5_5, k5_5) == (5, 3, -14)
    for xv, yv in [(0, -9), (1, 1), (2, 31)]:
        assert a5_5 * (b5_5 ** xv) + k5_5 == yv
    assert a5_5 * (b5_5 ** 3) + k5_5 == 121
    assert qm['sat_boss_d5_q5']['correctAnswer'] == 'D' and '121' in _correct_opt_text(qm['sat_boss_d5_q5'])

    # D5 Q6 (SPR): kx + 6y = k + 6 and 2x + (k - 1)y = 5 => det=0 at k in {-3, 4}; k=4 inf many, k=-3 no soln
    det_zeros = [k for k in range(-20, 21) if k * (k - 1) - 12 == 0]
    assert det_zeros == [-3, 4]
    no_sol_ks = [k for k in det_zeros if Fraction(k + 6, 6) != Fraction(5, k - 1)]
    inf_sol_ks = [k for k in det_zeros if Fraction(k + 6, 6) == Fraction(5, k - 1)]
    assert no_sol_ks == [-3] and inf_sol_ks == [4]
    assert qm['sat_boss_d5_q6']['acceptedAnswers'] == ['-3']

    # D5 Q7: (x-5)^2 + (y+2)^2 = 25, 3x - 4y = k tangent => |23 - k|/5 = 5 => k in {-2, 48}, least = -2
    ks5_7 = [k for k in range(-50, 60) if (-6 * k - 112) ** 2 - 4 * 25 * (8 - k) ** 2 == 0]
    assert ks5_7 == [-2, 48] and min(ks5_7) == -2
    # Verify tangent point (2, 2) for k=-2 and (8, -6) for k=48
    assert (2 - 5) ** 2 + (2 + 2) ** 2 == 25 and 3 * 2 - 4 * 2 == -2
    assert (8 - 5) ** 2 + (-6 + 2) ** 2 == 25 and 3 * 8 - 4 * (-6) == 48
    assert qm['sat_boss_d5_q7']['correctAnswer'] == 'A' and '-2' in _correct_opt_text(qm['sat_boss_d5_q7'])

    # D5 Q8: y = 2x^2 + 5x + 14 and y = mx + 6 tangent, m < 0 => (5 - m)^2 = 64 => m in {-3, 13} => m = -3
    ms5_8 = [m for m in range(-30, 30) if (5 - m) ** 2 - 4 * 2 * (14 - 6) == 0]
    assert ms5_8 == [-3, 13] and [m for m in ms5_8 if m < 0] == [-3]
    assert 2 * (-2) ** 2 + 5 * (-2) + 14 == (-3) * (-2) + 6 == 12
    assert qm['sat_boss_d5_q8']['correctAnswer'] == 'B' and '-3' in _correct_opt_text(qm['sat_boss_d5_q8'])

    # D5 Q9 (SPR): 2x + 3y <= 36, 5x + 2y <= 46 => max 7x + 6y = 90 at (6, 8)
    u5_9 = Fraction(16, 11)
    v5_9 = Fraction(9, 11)
    assert u5_9 > 0 and v5_9 > 0
    assert 2 * u5_9 + 5 * v5_9 == 7 and 3 * u5_9 + 2 * v5_9 == 6
    max5_9 = u5_9 * 36 + v5_9 * 46
    assert max5_9 == 90 and 2 * 6 + 3 * 8 == 36 and 5 * 6 + 2 * 8 == 46 and 7 * 6 + 6 * 8 == 90
    assert qm['sat_boss_d5_q9']['acceptedAnswers'] == ['90']

    # D5 Q10: f(x-2) at x in {-2, 1, 3} is {9, 0, 14} => f(-4)=9, f(-1)=0, f(1)=14 => f(x)=2x^2+7x+5 => b=7
    b5_10 = Fraction(14 - 0, 2)
    # a + c = 7 and 16a + c = 9 + 4*7 = 37 => 15a = 30 => a = 2, c = 5
    a5_10 = Fraction(37 - 7, 15)
    c5_10 = 7 - a5_10
    assert (a5_10, b5_10, c5_10) == (2, 7, 5)
    for xv, yv in [(-2, 9), (1, 0), (3, 14)]:
        t = xv - 2
        assert a5_10 * t**2 + b5_10 * t + c5_10 == yv
    assert qm['sat_boss_d5_q10']['correctAnswer'] == 'C' and '7' in _correct_opt_text(qm['sat_boss_d5_q10'])

    # D5 Q11: p(x) = ax+b (x<4), 5x-3a (x>=4); continuous at 4 (7a+b=20) & p(-2)=-7 (-2a+b=-7) => a=3, b=-1 => p(8)=31
    a5_11 = Fraction(20 - (-7), 7 - (-2))
    b5_11 = 20 - 7 * a5_11
    assert (a5_11, b5_11) == (3, -1)
    assert a5_11 * 4 + b5_11 == 5 * 4 - 3 * a5_11 == 11
    assert a5_11 * (-2) + b5_11 == -7
    p8_5_11 = 5 * 8 - 3 * a5_11
    assert p8_5_11 == 31 and qm['sat_boss_d5_q11']['correctAnswer'] == 'D' and '31' in _correct_opt_text(qm['sat_boss_d5_q11'])

    # D5 Q12 (SPR): (ax+b)(cx+d)=15x^2+kx+14, positive ints, a+c=8 => max k = 73
    ks5_12 = []
    for a in range(1, 16):
        if 15 % a != 0:
            continue
        c = 15 // a
        if a + c != 8:
            continue
        for b in range(1, 15):
            if 14 % b != 0:
                continue
            d = 14 // b
            ks5_12.append(a * d + b * c)
    assert sorted(set(ks5_12)) == [31, 41, 47, 73] and max(ks5_12) == 73
    assert qm['sat_boss_d5_q12']['acceptedAnswers'] == ['73']

    # D5 Q13: 3a+2b-c=-6, a-4b+3c=-4, 2a+5b+2c=24 => (-3, 4, 5), a-b+c=-2
    # Determinant of [[3, 2, -1], [1, -4, 3], [2, 5, 2]] = -74 != 0 (unique)
    det5_13 = 3 * (-8 - 15) - 2 * (2 - 6) + (-1) * (5 + 8)
    assert det5_13 == -74
    a5_13, b5_13, c5_13 = -3, 4, 5
    assert 3 * a5_13 + 2 * b5_13 - c5_13 == -6
    assert a5_13 - 4 * b5_13 + 3 * c5_13 == -4
    assert 2 * a5_13 + 5 * b5_13 + 2 * c5_13 == 24
    assert a5_13 - b5_13 + c5_13 == -2
    assert qm['sat_boss_d5_q13']['correctAnswer'] == 'A' and '-2' in _correct_opt_text(qm['sat_boss_d5_q13'])

    # D5 Q14: y=kx^2-4x+13, y=2x^2+8x+4 => (k-2)x^2 - 12x + 9 = 0 => 1 real soln iff k=2 or k=6 => sum=8
    ks5_14 = [2] + [k for k in range(-20, 30) if k != 2 and (-12) ** 2 - 4 * (k - 2) * 9 == 0]
    assert ks5_14 == [2, 6] and sum(ks5_14) == 8
    # Verify both exact unique intersections
    x_k2 = Fraction(9, 12)
    assert 2 * x_k2**2 - 4 * x_k2 + 13 == 2 * x_k2**2 + 8 * x_k2 + 4
    x_k6 = Fraction(12, 8)
    assert 6 * x_k6**2 - 4 * x_k6 + 13 == 2 * x_k6**2 + 8 * x_k6 + 4
    assert qm['sat_boss_d5_q14']['correctAnswer'] == 'B' and '8' in _correct_opt_text(qm['sat_boss_d5_q14'])

    # D5 Q15 (SPR): cubic p(x)=2x^3-3x^2-4x+7 through (-2,-13),(-1,6),(1,2),(2,3) => p(3)=22
    b5_15 = Fraction((-5) - 4, 3)
    d5_15 = 4 - b5_15
    a5_15 = Fraction(4 - (-2), 3)
    c5_15 = -2 - a5_15
    assert (a5_15, b5_15, c5_15, d5_15) == (2, -3, -4, 7)
    for xv, yv in [(-2, -13), (-1, 6), (1, 2), (2, 3)]:
        assert a5_15 * xv**3 + b5_15 * xv**2 + c5_15 * xv + d5_15 == yv
    p3_5_15 = a5_15 * 27 + b5_15 * 9 + c5_15 * 3 + d5_15
    assert p3_5_15 == 22 and qm['sat_boss_d5_q15']['acceptedAnswers'] == ['22']

    # ==================================================================
    # BOSS DRILL 6 EXACT ARITHMETIC ASSERTIONS (Q1..Q15)
    # ==================================================================
    # D6 Q1: 4x^2 - 24x + (k - 7) = 0, Delta > 0 => k < 43 => greatest int k = 42
    valid6_1 = [k for k in range(0, 60) if (-24) ** 2 - 4 * 4 * (k - 7) > 0]
    assert max(valid6_1) == 42 and (-24) ** 2 - 4 * 4 * (43 - 7) == 0
    assert qm['sat_boss_d6_q1']['correctAnswer'] == 'C' and '42' in _correct_opt_text(qm['sat_boss_d6_q1'])

    # D6 Q2: 3x^4 - 23x^2 - 36 = (3x^2 + 4)(x - 3)(x + 3) = 0 => real roots {-3, 3}, sum of squares = 18
    for x in range(-5, 6):
        assert 3 * x**4 - 23 * x**2 - 36 == (3 * x**2 + 4) * (x - 3) * (x + 3)
    real_roots6_2 = [-3, 3]
    assert sum(r**2 for r in real_roots6_2) == 18
    assert qm['sat_boss_d6_q2']['correctAnswer'] == 'D' and '18' in _correct_opt_text(qm['sat_boss_d6_q2'])

    # D6 Q3 (SPR): 3x^2 - 15x + 4 = 0 => r+s=5, rs=4/3 => r/s + s/r = (25 - 8/3)/(4/3) = 67/4 = 16.75
    disc6_3 = (-15) ** 2 - 4 * 3 * 4
    assert disc6_3 == 177 > 0
    s_sum6_3 = Fraction(15, 3)
    p_prod6_3 = Fraction(4, 3)
    val6_3 = (s_sum6_3**2 - 2 * p_prod6_3) / p_prod6_3
    assert val6_3 == Fraction(67, 4)
    r_num = (15 + math.sqrt(177)) / 6
    s_num = (15 - math.sqrt(177)) / 6
    assert abs((r_num / s_num + s_num / r_num) - 16.75) < 1e-12
    assert '67/4' in qm['sat_boss_d6_q3']['acceptedAnswers'] and '16.75' in qm['sat_boss_d6_q3']['acceptedAnswers']

    # D6 Q4: 2(x-3)^2 + 15(x-3) + 7 = 0 => x in {5/2, -4}, product = -10
    x1_6_4, x2_6_4 = Fraction(5, 2), Fraction(-4)
    for xv in (x1_6_4, x2_6_4):
        assert 2 * (xv - 3) ** 2 + 15 * (xv - 3) + 7 == 0
    assert x1_6_4 * x2_6_4 == -10
    assert qm['sat_boss_d6_q4']['correctAnswer'] == 'A' and '-10' in _correct_opt_text(qm['sat_boss_d6_q4'])

    # D6 Q5: p(x) = x^3 + ax^2 + bx - 10; p(2)=0, p(-1)=12 => a=8, b=-15, a+b=-7
    # 2a + b = 1 and a - b = 23 => 3a = 24 => a = 8, b = -15
    a6_5 = Fraction(1 + 23, 3)
    b6_5 = a6_5 - 23
    assert (a6_5, b6_5) == (8, -15) and a6_5 + b6_5 == -7
    assert 2**3 + a6_5 * 4 + b6_5 * 2 - 10 == 0
    assert (-1) ** 3 + a6_5 * 1 + b6_5 * (-1) - 10 == 12
    assert qm['sat_boss_d6_q5']['correctAnswer'] == 'B' and '-7' in _correct_opt_text(qm['sat_boss_d6_q5'])

    # D6 Q6 (SPR): 3x - 7*sqrt(x+2) = 14 => u=4 => x=14 (u=-5/3 extraneous => x=7/9 fails)
    assert 3 * 14 - 7 * math.isqrt(14 + 2) == 14
    x_ext = Fraction(7, 9)
    assert (3 * x_ext - 14) ** 2 == 49 * (x_ext + 2) and (3 * x_ext - 14) < 0  # extraneous!
    assert qm['sat_boss_d6_q6']['acceptedAnswers'] == ['14']

    # D6 Q7: 2^(2x+1) - 33*(2^x) + 16 = 0 => u in {1/2, 16} => x in {-1, 4}, sum = 3
    u1_6_7, u2_6_7 = Fraction(1, 2), Fraction(16)
    assert 2 * u1_6_7**2 - 33 * u1_6_7 + 16 == 0 and 2 * u2_6_7**2 - 33 * u2_6_7 + 16 == 0
    assert Fraction(1, 2) - 33 * Fraction(1, 2) + 16 == 0  # x = -1
    assert 2**9 - 33 * 2**4 + 16 == 0  # x = 4
    assert -1 + 4 == 3
    assert qm['sat_boss_d6_q7']['correctAnswer'] == 'C' and '3' in _correct_opt_text(qm['sat_boss_d6_q7'])

    # D6 Q8: f(x)=a(x+2)(x-8), a pos int, f(x)>=-125 => -25a>=-125 => a<=5 => max f(9)=11*5=55
    valid_a6_8 = [a for a in range(1, 20) if a * (3 + 2) * (3 - 8) >= -125]
    assert max(valid_a6_8) == 5
    max_f9 = max(a * (9 + 2) * (9 - 8) for a in valid_a6_8)
    assert max_f9 == 55 and qm['sat_boss_d6_q8']['correctAnswer'] == 'D' and '55' in _correct_opt_text(qm['sat_boss_d6_q8'])

    # D6 Q9 (SPR): f(x)=a*b^x+c (b>1), c=-11, f(0)=-6 => a=5, f(2)=34 => b=3; g(0)=f(1)+9=13
    c6_9 = -11
    a6_9 = -6 - c6_9
    b6_9 = math.isqrt((34 - c6_9) // a6_9)
    assert (a6_9, b6_9, c6_9) == (5, 3, -11) and b6_9 > 1
    assert a6_9 * b6_9**0 + c6_9 == -6 and a6_9 * b6_9**2 + c6_9 == 34
    g0_6_9 = (a6_9 * b6_9**1 + c6_9) + 9
    assert g0_6_9 == 13 and qm['sat_boss_d6_q9']['acceptedAnswers'] == ['13']

    # D6 Q10: x^2 + (k-4)x + (k-1) = 0, Delta = (k-2)(k-10) < 0 => k in {3..9}, count = 7
    no_real_ks = [k for k in range(-20, 30) if (k - 4) ** 2 - 4 * (k - 1) < 0]
    assert no_real_ks == [3, 4, 5, 6, 7, 8, 9] and len(no_real_ks) == 7
    assert (2 - 4) ** 2 - 4 * (2 - 1) == 0 and (10 - 4) ** 2 - 4 * (10 - 1) == 0
    assert qm['sat_boss_d6_q10']['correctAnswer'] == 'A' and '7' in _correct_opt_text(qm['sat_boss_d6_q10'])

    # D6 Q11: 3|2x-5| + 2x = k has exactly 1 soln iff k = g(5/2) = 5
    g6_11 = lambda x: 3 * abs(2 * x - 5) + 2 * x
    k6_11 = g6_11(Fraction(5, 2))
    assert k6_11 == 5
    # Verify k=5 is the strict global minimum over sample grid around 5/2
    for num in range(-20, 40):
        xv = Fraction(num, 4)
        if xv != Fraction(5, 2):
            assert g6_11(xv) > k6_11
    assert qm['sat_boss_d6_q11']['correctAnswer'] == 'C' and '5' in _correct_opt_text(qm['sat_boss_d6_q11'])

    # D6 Q12 (SPR): kx^2 - (2k+7)x + (k+6) = 0, 1/r + 1/s = (2k+7)/(k+6) = 5/3 => k = 9
    k6_12 = Fraction(5 * 6 - 3 * 7, 3 * 2 - 5)
    assert k6_12 == 9
    disc6_12 = (2 * k6_12 + 7) ** 2 - 4 * k6_12 * (k6_12 + 6)
    assert disc6_12 == 85 > 0
    r12 = (25 + math.sqrt(85)) / 18
    s12 = (25 - math.sqrt(85)) / 18
    assert abs((1 / r12 + 1 / s12) - 5 / 3) < 1e-12
    assert qm['sat_boss_d6_q12']['acceptedAnswers'] == ['9']

    # D6 Q13: sqrt(4x+12) = x + k => max k with exactly 1 real soln is k = 4
    def _count_rad_sols(k_val):
        # x^2 + (2k-4)x + (k^2-12) = 0 with x >= -3 and x + k >= 0
        disc = 64 - 16 * k_val
        if disc < 0:
            return 0
        if disc == 0:
            xr = -(2 * k_val - 4) / 2
            return 1 if (4 * xr + 12 >= -1e-12 and xr + k_val >= -1e-12) else 0
        sq = math.sqrt(disc)
        sols = []
        for xr in ((-(2 * k_val - 4) - sq) / 2, (-(2 * k_val - 4) + sq) / 2):
            if 4 * xr + 12 >= -1e-12 and xr + k_val >= -1e-12:
                sols.append(xr)
        return len(sols)

    assert _count_rad_sols(5) == 0
    assert _count_rad_sols(4) == 1
    assert _count_rad_sols(3.5) == 2
    assert _count_rad_sols(3) == 2
    assert _count_rad_sols(2) == 1
    assert qm['sat_boss_d6_q13']['correctAnswer'] == 'B' and '4' in _correct_opt_text(qm['sat_boss_d6_q13'])

    # D6 Q14: h(x) = a*(1/2)^x + c; c=-15, h(0)=-7 => a=8; h(-3) = 8*8 - 15 = 49
    c6_14 = -15
    a6_14 = -7 - c6_14
    m6_14 = a6_14 * (Fraction(1, 2) ** -3) + c6_14
    assert (a6_14, c6_14, m6_14) == (8, -15, 49)
    assert qm['sat_boss_d6_q14']['correctAnswer'] == 'D' and '49' in _correct_opt_text(qm['sat_boss_d6_q14'])

    # D6 Q15 (SPR): vertex (5, k), passes (1, 21), |r - s| = 6 => r=2, s=8, a=3, k=-27
    r6_15, s6_15 = 5 - 3, 5 + 3
    a6_15 = Fraction(21, (1 - r6_15) * (1 - s6_15))
    k6_15 = a6_15 * (5 - r6_15) * (5 - s6_15)
    assert (r6_15, s6_15, a6_15, k6_15) == (2, 8, 3, -27)
    assert a6_15 * (1 - 5) ** 2 + k6_15 == 21
    assert a6_15 * (2 - 5) ** 2 + k6_15 == 0 and a6_15 * (8 - 5) ** 2 + k6_15 == 0
    assert qm['sat_boss_d6_q15']['acceptedAnswers'] == ['-27']

    return True


if __name__ == '__main__':
    verify_all_math()
    for drill_key, title, order_idx, content_json in get_drills():
        errs = validate_sat_test(content_json, title)
        if errs:
            print(f"[QA FAIL] {drill_key}:")
            for e in errs:
                print("  -", e)
            sys.exit(1)
        qs = content_json['drillModule']['questions']
        mcq_c = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
        spr_c = 0
        for q in qs:
            if q['questionFormat'] == 'spr':
                spr_c += 1
            else:
                mcq_c[q['correctAnswer']] += 1
        print(f"[OK] {drill_key} (order={order_idx}): {len(qs)} Qs | MCQ={mcq_c} | SPR={spr_c} | {title}")
    print("BOSS MATH DRILLS 5 & 6 (30 ELITE Qs) VERIFIED & QA PASSED!")
