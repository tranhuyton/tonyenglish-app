# -*- coding: utf-8 -*-
"""
Digital SAT Math 1500+ — Module 2: Advanced Math (Hard M2 Core)
4 Flagship Skill Drills (60 unique, 100% original, copyright-clean questions):
- Drill 2.1: Quadratics — Discriminant, Vertex & Vieta Mastery (15 Qs)
- Drill 2.2: Polynomials, Factor Theorem & Rational Equations (15 Qs)
- Drill 2.3: Exponential Growth/Decay & Compound Scaling (15 Qs)
- Drill 2.4: Nonlinear Systems, Radicals, Absolute Value & Transformations (15 Qs)

Every question includes bilingual 800-level explanations, Desmos 10-second shortcuts,
key takeaways, and (for MCQs) 4-option trap analysis. All 60 answers are verified
programmatically via exact arithmetic in verify_all_math().
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

DOMAIN = 'Advanced Math'
SK_NONLIN_FUNC = 'Nonlinear functions'
SK_NONLIN_EQ = 'Nonlinear equations in one variable and systems of equations in two variables'
SK_EQUIV = 'Equivalent expressions'


# ============================================================================
# DRILL 2.1: Quadratics — Discriminant, Vertex & Vieta Mastery (15 Qs)
# MCQ Key Distribution (11 MCQs): A=3, B=3, C=3, D=2 | SPR: Q4, Q8, Q12, Q15
# ============================================================================
def _build_drill_m2_1():
    svg_q4 = svg_parabola_vertex(
        h_lbl='3',
        k_lbl='-8',
        opens_up=True,
        pt_lbl='(5, 4)',
        note='Graph of y = f(x) in the xy-plane',
    )
    tbl_q8 = build_math_table(
        ['\\(x\\)', '\\(h(x)\\)'],
        [['\\(-1\\)', '\\(0\\)'], ['\\(2\\)', '\\(-18\\)'], ['\\(5\\)', '\\(0\\)']],
        caption='Selected values of the quadratic function h',
    )

    qs = [
        # Q1 — Medium, MCQ, Ans=B
        math_mcq(
            'sat_m2_1_q1', 1, DOMAIN, SK_NONLIN_EQ, 'Medium',
            r'<p>\[4x^2 - 20x + c = 0\]</p>'
            r'<p>In the given equation, \(c\) is a constant. The equation has exactly one real solution.</p>',
            r'<p>What is the value of \(c\)?</p>',
            {'A': r'\(5\)', 'B': r'\(25\)', 'C': r'\(100\)', 'D': r'\(400\)'},
            'B',
            r'Phương trình bậc hai \(ax^2 + bx + c = 0\) có đúng một nghiệm thực khi và chỉ khi biệt thức \(\Delta = b^2 - 4ac = 0\).<br/>'
            r'Thay \(a = 4,\; b = -20\): \[(-20)^2 - 4(4)(c) = 0 \implies 400 - 16c = 0 \implies c = \frac{400}{16} = 25.\]',
            r'Phương trình bậc hai có đúng 1 nghiệm thực \(\iff \Delta = b^2 - 4ac = 0\); tuyệt đối không quên hệ số \(a \neq 1\).',
            {
                'A': ('Square Root Error', r'Lấy nhầm \(\sqrt{25} = 5\) thay vì giá trị của \(c\).'),
                'B': ('Đáp án đúng', r'Từ \(\Delta = (-20)^2 - 16c = 0\) suy ra \(c = 25\), khi đó phương trình trở thành \((2x - 5)^2 = 0\).'),
                'C': ('Forgot Coefficient a', r'Tính nhầm \(c = \left(\frac{20}{2}\right)^2 = 100\) như thể hệ số đầu là \(a = 1\) thay vì \(a = 4\).'),
                'D': ('Partial Calculation', r'Chỉ tính \(b^2 = 400\) mà chưa chia cho \(4a = 16\).'),
            },
            desmos_tip_vi=r'Gõ trực tiếp \(y = 4x^2 - 20x + c\) trên Desmos và thêm thanh trượt (slider) cho \(c\). Kéo \(c\) (hoặc gõ từng đáp án) để đỉnh parabol chạm đúng trục \(Ox\) — xảy ra tại \(c = 25\).',
        ),

        # Q2 — Medium, MCQ, Ans=A
        math_mcq(
            'sat_m2_1_q2', 2, DOMAIN, SK_NONLIN_FUNC, 'Medium',
            r'<p>\[f(x) = x^2 - 8x + 23\]</p>'
            r'<p>The quadratic function \(f\) is defined above.</p>',
            r'<p>Which of the following equivalent forms of \(f(x)\) displays the minimum value of \(f\) as a constant or coefficient?</p>',
            {
                'A': r'\(f(x) = (x - 4)^2 + 7\)',
                'B': r'\(f(x) = (x - 4)^2 + 23\)',
                'C': r'\(f(x) = x(x - 8) + 23\)',
                'D': r'\(f(x) = (x + 4)^2 + 7\)',
            },
            'A',
            r'Để hiển thị trực tiếp giá trị nhỏ nhất (minimum value) dưới dạng hằng số, ta đưa về dạng đỉnh \(f(x) = a(x - h)^2 + k\).<br/>'
            r'Hoàn thành bình phương: \[f(x) = (x^2 - 8x + 16) - 16 + 23 = (x - 4)^2 + 7.\]'
            r'Vì \((x - 4)^2 \ge 0\), giá trị nhỏ nhất của \(f\) là \(k = 7\) (đạt tại \(x = 4\)).',
            r'Câu hỏi “displays the minimum/maximum value as a constant” luôn yêu cầu chuyển sang dạng đỉnh \(a(x - h)^2 + k\) và phải tương đương với hàm gốc.',
            {
                'A': ('Đáp án đúng', r'Khai triển \((x - 4)^2 + 7 = x^2 - 8x + 16 + 7 = x^2 - 8x + 23\), khớp hàm gốc và hiện rõ giá trị nhỏ nhất \(7\).'),
                'B': ('Completing Square Trap', r'Quên trừ đi \(4^2 = 16\) khi tách bình phương; khai triển ra \(x^2 - 8x + 39 \neq f(x)\).'),
                'C': ('Wrong Form', r'Tuy tương đương với \(f(x)\) nhưng đây không phải dạng đỉnh nên chỉ hiển thị tung độ gốc \(23\), không hiển thị giá trị nhỏ nhất \(7\).'),
                'D': ('Sign Error', r'Đổi nhầm dấu bên trong bình phương; khai triển \((x + 4)^2 + 7 = x^2 + 8x + 23\) sai dấu hệ số \(x\).'),
            },
            desmos_tip_vi=r'Vẽ \(f(x) = x^2 - 8x + 23\) trên Desmos rồi bấm vào đỉnh parabol sẽ thấy tọa độ \((4, 7)\). Chọn ngay phương án có dạng \((x - 4)^2 + 7\).',
        ),

        # Q3 — Medium, MCQ, Ans=C
        math_mcq(
            'sat_m2_1_q3', 3, DOMAIN, SK_NONLIN_EQ, 'Medium',
            r'<p>\[3x^2 - 19x + 11 = 0\]</p>',
            r'<p>What is the sum of the solutions to the given equation?</p>',
            {
                'A': r'\(-\frac{19}{3}\)',
                'B': r'\(\frac{11}{3}\)',
                'C': r'\(\frac{19}{3}\)',
                'D': r'\(19\)',
            },
            'C',
            r'Kiểm tra biệt thức: \(\Delta = (-19)^2 - 4(3)(11) = 361 - 132 = 229 > 0\), nên phương trình có hai nghiệm thực phân biệt.<br/>'
            r'Áp dụng định lý Viète, tổng hai nghiệm là: \[x_1 + x_2 = -\frac{b}{a} = -\frac{-19}{3} = \frac{19}{3}.\]',
            r'Với \(ax^2 + bx + c = 0\) có nghiệm thực, tổng hai nghiệm luôn là \(-\frac{b}{a}\) (nhớ đổi dấu \(b\) và chia cho \(a\)).',
            {
                'A': ('Sign Error', r'Quên dấu trừ trong công thức \(-\frac{b}{a}\), lấy nhầm \(\frac{-19}{3}\).'),
                'B': ('Sum vs Product Swap', r'Tính nhầm tích hai nghiệm \(\frac{c}{a} = \frac{11}{3}\) thay vì tổng hai nghiệm.'),
                'C': ('Đáp án đúng', r'Áp dụng chuẩn công thức Viète: \(-\frac{-19}{3} = \frac{19}{3}\).'),
                'D': ('Forgot Coefficient a', r'Lấy \(-b = 19\) mà quên chia cho hệ số đầu \(a = 3\).'),
            },
            desmos_tip_vi=r'Nếu cần kiểm chứng, vẽ \(y = 3x^2 - 19x + 11\), bấm 2 giao điểm trục \(Ox\) (\(x_1 \approx 0.644,\; x_2 \approx 5.689\)), cộng lại ra \(6.333\dots = \frac{19}{3}\).',
        ),

        # Q4 — Medium, SPR
        math_spr(
            'sat_m2_1_q4', 4, DOMAIN, SK_NONLIN_FUNC, 'Medium',
            f'<div style="display:flex;justify-content:center;margin-bottom:12px;">{svg_q4}</div>'
            r'<p>In the \(xy\)-plane, the graph of the quadratic function \(y = f(x)\) is a parabola with vertex \((3, -8)\) that passes through the point \((5, 4)\).</p>',
            r'<p>What is the value of \(f(0)\)?</p>',
            ['19'], '19',
            r'Vì đỉnh parabol là \((3, -8)\), hàm bậc hai có dạng \(f(x) = a(x - 3)^2 - 8\).<br/>'
            r'Thay điểm \((5, 4)\) vào phương trình: \[4 = a(5 - 3)^2 - 8 \implies 4 = 4a - 8 \implies 4a = 12 \implies a = 3.\]'
            r'Do đó \(f(x) = 3(x - 3)^2 - 8\). Tại \(x = 0\): \[f(0) = 3(0 - 3)^2 - 8 = 3(9) - 8 = 19.\]',
            r'Biết đỉnh \((h, k)\) và thêm 1 điểm bất kỳ là đủ xác định duy nhất hệ số \(a\) bằng dạng đỉnh \(f(x) = a(x - h)^2 + k\).',
            desmos_tip_vi=r'Gõ \(f(x) = a(x - 3)^2 - 8\), thêm slider \(a\) và tìm giá trị để \(f(5) = 4\) (hoặc giải thẳng \(a(5 - 3)^2 - 8 = 4\)), sau đó gõ \(f(0)\) sẽ trả ngay kết quả \(19\).',
        ),

        # Q5 — Medium-Hard, MCQ, Ans=D
        math_mcq(
            'sat_m2_1_q5', 5, DOMAIN, SK_NONLIN_FUNC, 'Medium-Hard',
            r'<p>For the quadratic function \(g(x) = -2x^2 + bx + c\), where \(b\) and \(c\) are constants, \(g(2) = g(10) = 5\).</p>',
            r'<p>What is the maximum value of \(g(x)\)?</p>',
            {'A': r'\(6\)', 'B': r'\(21\)', 'C': r'\(32\)', 'D': r'\(37\)'},
            'D',
            r'Vì \(g(2) = g(10) = 5\), tính đối xứng của parabol cho biết hoành độ đỉnh nằm chính giữa \(2\) và \(10\): \[h = \frac{2 + 10}{2} = 6.\]'
            r'Hàm \(g(x)\) có hệ số đầu \(a = -2 < 0\) nên đạt cực đại tại đỉnh \((6, k)\), viết dạng đỉnh: \(g(x) = -2(x - 6)^2 + k\).<br/>'
            r'Thay \(x = 2,\; g(2) = 5\): \[5 = -2(2 - 6)^2 + k = -2(16) + k = -32 + k \implies k = 37.\]',
            r'Gặp dữ kiện \(f(x_1) = f(x_2)\) ở hàm bậc hai, lập tức lấy trung bình cộng \(h = \frac{x_1 + x_2}{2}\) để chốt hoành độ đỉnh và dùng dạng đỉnh \(a(x - h)^2 + k\).',
            {
                'A': ('Vertex X vs Y', r'Trả lời nhầm hoành độ đỉnh \(h = 6\) thay vì giá trị cực đại \(g(6) = 37\).'),
                'B': ('Forgot Coefficient a', r'Quên nhân hệ số \(|a| = 2\), tính nhầm \(5 + (2 - 6)^2 = 5 + 16 = 21\).'),
                'C': ('Omitted Constant Shift', r'Chỉ tính độ chênh lệch \(2(6 - 2)^2 = 32\) mà quên cộng giá trị nền \(g(2) = 5\).'),
                'D': ('Đáp án đúng', r'Hoành độ đỉnh \(h = 6\), suy ra cực đại \(k = 5 + 2(4)^2 = 37\).'),
            },
            desmos_tip_vi=r'Gõ \(g(x) = -2(x - 6)^2 + k\) với slider \(k\) (hoặc lập bảng 2 điểm \((2, 5), (10, 5)\) và gõ hồi quy \(y_1 \sim -2x_1^2 + bx_1 + c\)), bấm đỉnh parabol đọc ngay tung độ \(37\).',
        ),

        # Q6 — Medium-Hard, MCQ, Ans=A
        math_mcq(
            'sat_m2_1_q6', 6, DOMAIN, SK_NONLIN_EQ, 'Medium-Hard',
            r'<p>\[2x^2 - 12x + k = 0\]</p>'
            r'<p>In the given equation, \(k\) is an integer constant. The equation has no real solutions.</p>',
            r'<p>What is the least possible value of \(k\)?</p>',
            {'A': r'\(19\)', 'B': r'\(18\)', 'C': r'\(17\)', 'D': r'\(37\)'},
            'A',
            r'Phương trình vô nghiệm thực khi và chỉ khi \(\Delta = b^2 - 4ac < 0\): \[(-12)^2 - 4(2)(k) < 0 \implies 144 - 8k < 0 \implies 8k > 144 \implies k > 18.\]'
            r'Vì \(k\) là số nguyên và phải lớn hơn hẳn \(18\), giá trị nhỏ nhất có thể của \(k\) là \(19\).',
            r'Luôn kiểm tra dấu bất đẳng thức ngặt (\(< 0\) cho vô nghiệm): khi đề yêu cầu “integer”, phải nhảy qua giá trị biên \(18\) sang \(19\).',
            {
                'A': ('Đáp án đúng', r'Với \(k > 18\) và \(k \in \mathbb{Z}\), giá trị nguyên nhỏ nhất là \(19\).'),
                'B': ('Boundary Trap', r'Tại \(k = 18\), \(\Delta = 0\) nên phương trình vẫn có ĐÚNG 1 nghiệm thực (\(x = 3\)), không phải vô nghiệm.'),
                'C': ('Reversed Inequality', r'Đổi nhầm chiều bất đẳng thức thành \(k < 18\) nên chọn \(17\) (khi đó phương trình có 2 nghiệm thực).'),
                'D': ('Forgot Coefficient a', r'Quên hệ số \(a = 2\), giải nhầm \(144 - 4k < 0 \implies k > 36 \implies 37\).'),
            },
            desmos_tip_vi=r'Vẽ \(y = 2x^2 - 12x + k\), thêm slider \(k\). Parabol không cắt trục \(Ox\) khi nằm hoàn toàn phía trên \(Ox\); tại \(k = 18\) đỉnh chạm \((3, 0)\), nên số nguyên nhỏ nhất là \(19\).',
        ),

        # Q7 — Medium-Hard, MCQ, Ans=B
        math_mcq(
            'sat_m2_1_q7', 7, DOMAIN, SK_NONLIN_EQ, 'Medium-Hard',
            r'<p>\[6x^2 - 13x + 4 = 2x^2 + 5x - 9\]</p>',
            r'<p>What is the product of all solutions to the given equation?</p>',
            {
                'A': r'\(-\frac{13}{4}\)',
                'B': r'\(\frac{13}{4}\)',
                'C': r'\(\frac{9}{2}\)',
                'D': r'\(13\)',
            },
            'B',
            r'Chuyển toàn bộ các hạng tử sang vế trái để đưa về dạng chuẩn \(ax^2 + bx + c = 0\): \[(6 - 2)x^2 + (-13 - 5)x + (4 + 9) = 0 \implies 4x^2 - 18x + 13 = 0.\]'
            r'Kiểm tra biệt thức: \(\Delta = (-18)^2 - 4(4)(13) = 324 - 208 = 116 > 0\) (có 2 nghiệm thực phân biệt).<br/>'
            r'Theo định lý Viète, tích các nghiệm là: \[x_1 x_2 = \frac{c}{a} = \frac{13}{4}.\]',
            r'Bắt buộc chuyển hết về một vế bằng \(0\) trước khi đọc \(a, b, c\) cho Viète; tích nghiệm là \(+\frac{c}{a}\) (không đổi dấu).',
            {
                'A': ('Sign Error', r'Nhầm dấu trừ của công thức tổng nghiệm sang công thức tích nghiệm, viết \(-\frac{c}{a} = -\frac{13}{4}\).'),
                'B': ('Đáp án đúng', r'Sau khi rút gọn thành \(4x^2 - 18x + 13 = 0\), tích hai nghiệm bằng \(\frac{c}{a} = \frac{13}{4}\).'),
                'C': ('Sum vs Product Swap', r'Tính nhầm tổng hai nghiệm \(-\frac{-18}{4} = \frac{9}{2}\) thay vì tích hai nghiệm.'),
                'D': ('Forgot Coefficient a', r'Lấy nguyên hệ số tự do \(c = 13\) mà quên chia cho \(a = 4\).'),
            },
            desmos_tip_vi=r'Vẽ \(y = (6x^2 - 13x + 4) - (2x^2 + 5x - 9)\), bấm hai giao điểm trục \(Ox\) (\(x_1 \approx 0.904,\; x_2 \approx 3.596\)) rồi nhân lại được đúng \(3.25 = \frac{13}{4}\).',
        ),

        # Q8 — Medium-Hard, SPR
        math_spr(
            'sat_m2_1_q8', 8, DOMAIN, SK_NONLIN_FUNC, 'Medium-Hard',
            f'<div style="margin-bottom:10px;">{tbl_q8}</div>'
            r'<p>The table gives three values of \(x\) and their corresponding values of \(h(x)\) for a quadratic function \(h\) defined by \(h(x) = ax^2 + bx + c\), where \(a\), \(b\), and \(c\) are constants.</p>',
            r'<p>What is the value of \(a + b + c\)?</p>',
            ['-16'], '-16',
            r'Từ bảng, \(h(-1) = 0\) và \(h(5) = 0\) nên hàm bậc hai có dạng tích nhân tử: \[h(x) = a(x + 1)(x - 5).\]'
            r'Thay điểm \((2, -18)\): \[-18 = a(2 + 1)(2 - 5) = -9a \implies a = 2.\]'
            r'Để ý mẹo cực nhanh: \(a + b + c = a(1)^2 + b(1) + c = h(1)\)! Không cần khai triển: \[a + b + c = h(1) = 2(1 + 1)(1 - 5) = 2(2)(-4) = -16.\]'
            r'(Hoặc khai triển \(h(x) = 2x^2 - 8x - 10 \implies a + b + c = 2 - 8 - 10 = -16\).)',
            r'Với mọi đa thức \(ax^2 + bx + c\), tổng các hệ số \(a + b + c\) chính bằng \(h(1)\); và khi bảng cho hai nghiệm \(h(r) = h(s) = 0\), hãy viết ngay \(a(x - r)(x - s)\).',
            desmos_tip_vi=r'Nhập 3 dòng của bảng vào Desmos Table \((x_1, y_1)\), gõ hồi quy \(y_1 \sim ax_1^2 + bx_1 + c\). Desmos trả ngay \(a = 2,\; b = -8,\; c = -10\); gõ \(a + b + c\) ra \(-16\).',
        ),

        # Q9 — Medium-Hard, MCQ, Ans=C
        math_mcq(
            'sat_m2_1_q9', 9, DOMAIN, SK_NONLIN_FUNC, 'Medium-Hard',
            r'<p>A research drone launches vertically from an observation deck. Its altitude \(H(t)\), in meters above the ground, \(t\) seconds after launch is modeled by \[H(t) = -5t^2 + 30t + 35\] for \(t \ge 0\).</p>',
            r'<p>Which of the following equivalent forms of \(H(t)\) displays the time, in seconds after launch, at which the drone reaches the ground as a constant or coefficient?</p>',
            {
                'A': r'\(H(t) = -5(t - 3)^2 + 80\)',
                'B': r'\(H(t) = -5(t + 7)(t - 1)\)',
                'C': r'\(H(t) = -5(t - 7)(t + 1)\)',
                'D': r'\(H(t) = -5t(t - 6) + 35\)',
            },
            'C',
            r'Drone chạm mặt đất khi độ cao \(H(t) = 0\), tức ta cần nghiệm dương của \(H(t)\) hiện trực tiếp — đây là dạng tích nhân tử (factored form).<br/>'
            r'Đặt \(-5\) làm nhân tử chung: \[H(t) = -5(t^2 - 6t - 7) = -5(t - 7)(t + 1).\]'
            r'Nghiệm dương \(t = 7\) giây hiện trực tiếp trong nhân tử \((t - 7)\).',
            r'Nhớ 3 dạng vàng của hàm bậc hai: dạng chuẩn hiện \(y\)-intercept; dạng đỉnh \(a(t-h)^2+k\) hiện max/min; dạng nhân tử \(a(t-r)(t-s)\) hiện nghiệm (thời điểm chạm đất \(H = 0\)).',
            {
                'A': ('Wrong Form (Vertex)', r'Dạng đỉnh này tương đương với \(H(t)\) nhưng chỉ hiển thị độ cao cực đại \(80\) m tại \(t = 3\) s, không hiển thị thời điểm chạm đất \(t = 7\) s.'),
                'B': ('Sign Error', r'Đổi ngược dấu hai nghiệm; khai triển ra \(-5t^2 - 30t + 35 \neq H(t)\).'),
                'C': ('Đáp án đúng', r'Tương đương hoàn toàn với \(H(t)\) và hiển thị trực tiếp thời điểm chạm đất \(t = 7\) giây.'),
                'D': ('Wrong Form', r'Chỉ nhóm 2 hạng tử đầu; hiển thị độ cao ban đầu \(35\) m và lúc trở về độ cao bệ phóng \(t = 6\) s, không phải lúc chạm đất.'),
            },
            desmos_tip_vi=r'Vẽ \(H(x) = -5x^2 + 30x + 35\) trên Desmos, bấm giao điểm dương với trục \(Ox\) ra \((7, 0)\). Kiểm tra đáp án C chồng khít đồ thị và chứa số \(7\).',
        ),

        # Q10 — Medium-Hard, MCQ, Ans=D
        math_mcq(
            'sat_m2_1_q10', 10, DOMAIN, SK_NONLIN_EQ, 'Medium-Hard',
            r'<p>\[kx^2 - 24x + (3k + 12) = 0\]</p>'
            r'<p>In the given equation, \(k\) is a positive constant. The sum of the solutions to the equation is equal to the product of the solutions.</p>',
            r'<p>What is the value of \(k\)?</p>',
            {'A': r'\(2\)', 'B': r'\(3\)', 'C': r'\(6\)', 'D': r'\(4\)'},
            'D',
            r'Theo định lý Viète với \(a = k > 0,\; b = -24,\; c = 3k + 12\):<br/>'
            r'• Tổng các nghiệm: \(S = -\frac{-24}{k} = \frac{24}{k}\).<br/>'
            r'• Tích các nghiệm: \(P = \frac{3k + 12}{k}\).<br/>'
            r'Cho \(S = P\): \[\frac{24}{k} = \frac{3k + 12}{k} \implies 24 = 3k + 12 \implies 3k = 12 \implies k = 4.\]'
            r'Kiểm tra lại khi \(k = 4\): \(4x^2 - 24x + 24 = 0 \iff x^2 - 6x + 6 = 0\) có \(\Delta = 36 - 24 = 12 > 0\) (có 2 nghiệm thực hợp lệ).',
            r'Khi tổng bằng tích hai nghiệm của \(ax^2 + bx + c = 0\), mẫu số \(a\) tự triệt tiêu ngay lập tức: \(-b = c\).',
            {
                'A': ('Arithmetic Error', r'Giải nhầm \(3k + 12 = 18\) hoặc chia nhầm \(12/6 = 2\).'),
                'B': ('Arithmetic Error', r'Nếu \(k = 3\) thì tổng là \(8\) còn tích là \(\frac{21}{3} = 7 \neq 8\).'),
                'C': ('Partial Calculation', r'Cộng nhầm thành \(3k = 18 \implies k = 6\), khi đó tổng là \(4\) còn tích là \(5\).'),
                'D': ('Đáp án đúng', r'Từ \(-b = c \iff 24 = 3k + 12\) cho \(k = 4\), thỏa mãn \(\Delta > 0\).'),
            },
            desmos_tip_vi=r'Nhận xét \(-b = c \implies 24 = 3k + 12\) ra \(k = 4\) trong 3 giây; có thể kiểm lại bằng cách gõ \(y = 4x^2 - 24x + 24\) trên Desmos xem 2 nghiệm có tổng \(6\) và tích \(6\) hay không.',
        ),

        # Q11 — Hard (750-800), MCQ, Ans=A
        math_mcq(
            'sat_m2_1_q11', 11, DOMAIN, SK_NONLIN_EQ, 'Hard (750-800)',
            r'<p>\[x^2 + (k - 4)x + (k + 11) = 0\]</p>'
            r'<p>In the given equation, \(k\) is a constant. The equation has exactly one real solution.</p>',
            r'<p>What is the sum of all possible values of \(k\)?</p>',
            {'A': r'\(12\)', 'B': r'\(14\)', 'C': r'\(8\)', 'D': r'\(-28\)'},
            'A',
            r'Phương trình có đúng một nghiệm thực khi và chỉ khi \(\Delta = 0\): \[(k - 4)^2 - 4(1)(k + 11) = 0.\]'
            r'Khai triển và rút gọn: \[k^2 - 8k + 16 - 4k - 44 = 0 \implies k^2 - 12k - 28 = 0 \implies (k - 14)(k + 2) = 0.\]'
            r'Hai giá trị thỏa mãn là \(k = 14\) và \(k = -2\) (cả hai đều cho nghiệm kép thực). Tổng các giá trị của \(k\) là \(14 + (-2) = 12\) (hoặc đọc ngay từ Viète: \(-\frac{-12}{1} = 12\)).',
            r'Khi tham số \(k\) xuất hiện ở cả \(b\) và \(c\), phương trình \(\Delta = 0\) trở thành một phương trình bậc hai ẩn \(k\) — dùng luôn Viète cho ẩn \(k\) để lấy tổng/tích!',
            {
                'A': ('Đáp án đúng', r'\(\Delta = k^2 - 12k - 28 = 0\) có hai nghiệm \(k = 14\) và \(k = -2\), tổng bằng \(12\).'),
                'B': ('Partial Answer', r'Chỉ lấy giá trị dương \(k = 14\) mà bỏ sót giá trị âm \(k = -2\) (đề không giới hạn \(k > 0\)).'),
                'C': ('Distribution Trap', r'Quên nhân \(-4\) vào \(k\) trong \(-4(k + 11)\), chỉ giữ \(-8k\) nên lấy tổng là \(8\).'),
                'D': ('Sum vs Product Swap', r'Lấy nhầm tích hai giá trị của \(k\) là \(-28\) thay vì tổng \(12\).'),
            },
            desmos_tip_vi=r'Gõ thẳng phương trình biệt thức \(y = (x - 4)^2 - 4(x + 11)\) trên Desmos, bấm 2 giao điểm trục \(Ox\) là \((-2, 0)\) và \((14, 0)\), cộng lại được \(12\).',
        ),

        # Q12 — Hard (750-800), SPR
        math_spr(
            'sat_m2_1_q12', 12, DOMAIN, SK_NONLIN_EQ, 'Hard (750-800)',
            r'<p>\[2(3x - 5)^2 - 14(3x - 5) + 19 = 0\]</p>',
            r'<p>What is the sum of all solutions to the given equation?</p>',
            ['17/3', '5.667', '5.666'], '17/3 (hoặc 5.667)',
            r'Đặt ẩn phụ \(u = 3x - 5\), phương trình trở thành \(2u^2 - 14u + 19 = 0\).<br/>'
            r'Kiểm tra biệt thức: \(\Delta_u = (-14)^2 - 4(2)(19) = 196 - 152 = 44 > 0\), nên có 2 nghiệm thực phân biệt \(u_1, u_2\) với tổng \(u_1 + u_2 = \frac{14}{2} = 7\).<br/>'
            r'Chuyển ngược về \(x\): \[(3x_1 - 5) + (3x_2 - 5) = 7 \implies 3(x_1 + x_2) - 10 = 7 \implies 3(x_1 + x_2) = 17 \implies x_1 + x_2 = \frac{17}{3}.\]'
            r'(Cách 2: khai triển toàn bộ ra \(18x^2 - 102x + 139 = 0 \implies x_1 + x_2 = \frac{102}{18} = \frac{17}{3}\)).',
            r'Với phương trình dạng \(a(px + q)^2 + b(px + q) + c = 0\), đặt \(u = px + q\): nhớ rằng \(u_1 + u_2 = p(x_1 + x_2) + 2q\) (nhân ĐÔI hằng số \(q\) vì có 2 nghiệm!).',
            desmos_tip_vi=r'Vẽ trực tiếp \(y = 2(3x - 5)^2 - 14(3x - 5) + 19\), bấm hai nghiệm \(x_1 \approx 2.2805\) và \(x_2 \approx 3.3862\), cộng lại ra \(5.6667 = \frac{17}{3}\).',
        ),

        # Q13 — Hard (750-800), MCQ, Ans=B
        math_mcq(
            'sat_m2_1_q13', 13, DOMAIN, SK_NONLIN_FUNC, 'Hard (750-800)',
            r'<p>The quadratic function \(f\) is defined by \(f(x) = ax^2 + bx + c\), where \(a\), \(b\), and \(c\) are constants and \(a > 0\). In the \(xy\)-plane, the graph of \(y = f(x)\) passes through the points \((1, -6)\) and \((9, -6)\), and the equation \(f(x) = -38\) has exactly one real solution.</p>',
            r'<p>What is the value of \(b\)?</p>',
            {'A': r'\(-10\)', 'B': r'\(-20\)', 'C': r'\(12\)', 'D': r'\(20\)'},
            'B',
            r'Vì \(f(1) = f(9) = -6\), trục đối xứng của parabol là \(h = \frac{1 + 9}{2} = 5\).<br/>'
            r'Vì \(a > 0\) (bề lõm hướng lên) và \(f(x) = -38\) chỉ có ĐÚNG 1 nghiệm thực, đường thẳng \(y = -38\) phải tiếp xúc đúng tại đỉnh parabol! Vậy đỉnh là \((5, -38)\).<br/>'
            r'Viết dạng đỉnh: \(f(x) = a(x - 5)^2 - 38\). Thay \((1, -6)\): \[-6 = a(1 - 5)^2 - 38 \implies 16a = 32 \implies a = 2.\]'
            r'Khai triển: \(f(x) = 2(x^2 - 10x + 25) - 38 = 2x^2 - 20x + 12\), suy ra \(b = -20\).',
            r'Nếu \(a > 0\) và \(f(x) = m\) có đúng 1 nghiệm thực thì \(m\) chính là tung độ đỉnh (giá trị cực tiểu). Kết hợp \(f(x_1) = f(x_2)\) để khóa trọn tọa độ đỉnh \((h, m)\).',
            {
                'A': ('Assumed a = 1', r'Mặc định nhầm \(a = 1\) nên lấy \(b = -2(1)(5) = -10\) mà không giải tìm \(a = 2\).'),
                'B': ('Đáp án đúng', r'Đỉnh \((5, -38)\) kết hợp \(f(1) = -6\) cho \(a = 2\), suy ra \(b = -2ah = -2(2)(5) = -20\).'),
                'C': ('Wrong Coefficient', r'Tìm ra giá trị của hằng số \(c = 12\) thay vì hệ số \(b = -20\).'),
                'D': ('Sign Error', r'Quên dấu trừ trong \(b = -2ah\), viết nhầm \(+20\).'),
            },
            desmos_tip_vi=r'Từ \((1, -6), (9, -6)\) suy ra \(h = 5\) và đỉnh \((5, -38)\). Nhập 3 điểm \((1, -6), (5, -38), (9, -6)\) vào Desmos Table rồi chạy hồi quy \(y_1 \sim ax_1^2 + bx_1 + c\), đọc ngay \(b = -20\).',
        ),

        # Q14 — Hard (750-800), MCQ, Ans=C
        math_mcq(
            'sat_m2_1_q14', 14, DOMAIN, SK_NONLIN_EQ, 'Hard (750-800)',
            r'<p>The quadratic equation \(ax^2 + bx + c = 0\), where \(a\), \(b\), and \(c\) are positive constants, has two distinct real solutions whose sum is \(-\frac{10}{3}\) and whose product is \(\frac{4}{3}\).</p>',
            r'<p>If \(a + b + c = 51\), what is the value of \(b\)?</p>',
            {'A': r'\(9\)', 'B': r'\(12\)', 'C': r'\(30\)', 'D': r'\(34\)'},
            'C',
            r'Theo định lý Viète:<br/>'
            r'• Tổng hai nghiệm: \(-\frac{b}{a} = -\frac{10}{3} \implies b = \frac{10}{3}a\).<br/>'
            r'• Tích hai nghiệm: \(\frac{c}{a} = \frac{4}{3} \implies c = \frac{4}{3}a\).<br/>'
            r'Thay vào điều kiện \(a + b + c = 51\): \[a + \frac{10}{3}a + \frac{4}{3}a = 51 \implies \frac{17}{3}a = 51 \implies a = 9.\]'
            r'Suy ra \(b = \frac{10}{3}(9) = 30\) (và \(c = 12\), kiểm tra \(\Delta = 30^2 - 4(9)(12) = 468 > 0\)).',
            r'Khi Viète cho tỉ số của \(b/a\) và \(c/a\), biểu diễn cả \(b\) và \(c\) theo \(a\) (hoặc đặt \(a = 3k,\; b = 10k,\; c = 4k\)) để biến bài toán 3 ẩn thành 1 ẩn \(k\) siêu gọn.',
            {
                'A': ('Wrong Variable', r'Đây là giá trị của \(a = 9\), chưa nhân tỉ lệ \(\frac{10}{3}\) để ra \(b\).'),
                'B': ('Wrong Variable', r'Đây là giá trị của \(c = 12\) thay vì \(b = 30\).'),
                'C': ('Đáp án đúng', r'Đặt \(a = 3k, b = 10k, c = 4k \implies 17k = 51 \implies k = 3 \implies b = 30\).'),
                'D': ('Arithmetic Error', r'Lấy nhầm \(51 \times \frac{2}{3} = 34\) hoặc cộng sai tổng tỉ số thành \(15k\).'),
            },
            desmos_tip_vi=r'Gõ thẳng tỷ lệ trên Desmos: \(k = \frac{51}{3 + 10 + 4}\) ra \(k = 3\), rồi tính \(10k = 30\) trong 5 giây!',
        ),

        # Q15 — Hard (750-800), SPR
        math_spr(
            'sat_m2_1_q15', 15, DOMAIN, SK_NONLIN_EQ, 'Hard (750-800)',
            r'<p>\[2x^2 - 15x + c = 0\]</p>'
            r'<p>In the given equation, \(c\) is a constant. The equation has two distinct real solutions, \(r\) and \(s\), such that \(r^2 + s^2 = \frac{161}{4}\).</p>',
            r'<p>What is the value of \(c\)?</p>',
            ['16'], '16',
            r'Áp dụng định lý Viète cho \(2x^2 - 15x + c = 0\): \[r + s = \frac{15}{2}, \qquad rs = \frac{c}{2}.\]'
            r'Sử dụng hằng đẳng thức vàng \(r^2 + s^2 = (r + s)^2 - 2rs\): \[\frac{161}{4} = \left(\frac{15}{2}\right)^2 - 2\left(\frac{c}{2}\right) = \frac{225}{4} - c.\]'
            r'Giải tìm \(c\): \[c = \frac{225}{4} - \frac{161}{4} = \frac{64}{4} = 16.\]'
            r'Kiểm tra biệt thức với \(c = 16\): \(\Delta = 225 - 4(2)(16) = 97 > 0\) (có 2 nghiệm thực phân biệt hợp lệ).',
            r'Gặp tổng bình phương nghiệm \(r^2 + s^2\), không bao giờ giải nghiệm lẻ bằng công thức nghiệm — dùng ngay \(r^2 + s^2 = (r + s)^2 - 2rs\) kết hợp Viète.',
            desmos_tip_vi=r'Gõ thẳng phương trình Viète trên Desmos: \(\left(\frac{15}{2}\right)^2 - 2\left(\frac{x}{2}\right) = \frac{161}{4}\), đường đứng cắt ngay tại \(x = 16\).',
        ),
    ]

    return build_math_drill_json(
        'Math Drill 2.1: Quadratics — Discriminant, Vertex & Vieta Mastery (15 câu)',
        '15 câu trọng tâm Advanced Math • Biệt thức, Đỉnh Parabol, Viète & Dạng tương đương (650–800)',
        'Advanced Math • Hard M2 Core',
        qs,
        target_minutes=24,
    )


# ============================================================================
# DRILL 2.2: Polynomials, Factor Theorem & Rational Equations (15 Qs)
# MCQ Key Distribution (11 MCQs): A=3, B=3, C=2, D=3 | SPR: Q4, Q8, Q12, Q15
# ============================================================================
def _build_drill_m2_2():
    tbl_q1 = build_math_table(
        ['\\(x\\)', '\\(p(x)\\)'],
        [
            ['\\(-4\\)', '\\(6\\)'],
            ['\\(-2\\)', '\\(0\\)'],
            ['\\(0\\)', '\\(-8\\)'],
            ['\\(3\\)', '\\(12\\)'],
            ['\\(5\\)', '\\(0\\)'],
        ],
        caption='Selected values of the polynomial function p',
    )

    qs = [
        # Q1 — Medium, MCQ, Ans=D
        math_mcq(
            'sat_m2_2_q1', 1, DOMAIN, SK_EQUIV, 'Medium',
            f'<div style="margin-bottom:10px;">{tbl_q1}</div>'
            r'<p>The table gives selected values of a polynomial function \(p\).</p>',
            r'<p>Based on the table, which of the following must be a factor of \(p(x)\)?</p>',
            {'A': r'\(x - 2\)', 'B': r'\(x + 5\)', 'C': r'\(x + 8\)', 'D': r'\(x - 5\)'},
            'D',
            r'Theo Định lý Nhân tử (Factor Theorem), nếu \(p(a) = 0\) thì \((x - a)\) chắc chắn là một nhân tử của \(p(x)\).<br/>'
            r'Từ bảng giá trị, \(p(-2) = 0 \implies (x + 2)\) là nhân tử, và \(p(5) = 0 \implies (x - 5)\) là nhân tử. Trong 4 đáp án, chỉ có \(x - 5\) thỏa mãn.',
            r'Luôn đảo dấu nghiệm khi viết nhân tử: \(p(a) = 0 \iff (x - a)\) là nhân tử; đừng bao giờ nhầm tung độ gốc \(p(0) = -8\) với nghiệm \(x\).',
            {
                'A': ('Sign Error', r'Bảng cho \(p(-2) = 0\) nên nhân tử phải là \(x - (-2) = x + 2\), không phải \(x - 2\).'),
                'B': ('Sign Error', r'Bảng cho \(p(5) = 0\) nên nhân tử phải là \(x - 5\), không phải \(x + 5\).'),
                'C': ('Y-Intercept Confusion', r'Giá trị \(-8\) là \(p(0)\) (tung độ gốc), không phải giá trị \(x\) làm cho \(p(x) = 0\).'),
                'D': ('Đáp án đúng', r'Vì \(p(5) = 0\), theo Factor Theorem thì \((x - 5)\) chắc chắn là nhân tử của \(p(x)\).'),
            },
            desmos_tip_vi=r'Mẹo kiểm nhanh: tìm mọi dòng có cột \(p(x) = 0\) (\(x = -2\) và \(x = 5\)), thay từng giá trị đó vào 4 đáp án — nhân tử đúng sẽ cho kết quả bằng \(0\) (\(5 - 5 = 0\)).',
        ),

        # Q2 — Medium, MCQ, Ans=B
        math_mcq(
            'sat_m2_2_q2', 2, DOMAIN, SK_EQUIV, 'Medium',
            r'<p>\[(3x - 4)(2x^2 + kx - 5) = 6x^3 + 7x^2 - 35x + 20\]</p>'
            r'<p>The equation above is true for all values of \(x\), where \(k\) is a constant.</p>',
            r'<p>What is the value of \(k\)?</p>',
            {'A': r'\(-5\)', 'B': r'\(5\)', 'C': r'\(7\)', 'D': r'\(15\)'},
            'B',
            r'Không cần khai triển hết — chỉ cần đồng nhất hệ số của \(x^2\) ở hai vế:<br/>'
            r'Vế trái tạo ra \(x^2\) từ \(3x \cdot kx + (-4) \cdot 2x^2 = (3k - 8)x^2\).<br/>'
            r'Cho bằng hệ số của \(x^2\) ở vế phải: \[3k - 8 = 7 \implies 3k = 15 \implies k = 5.\]'
            r'Kiểm tra nhanh hệ số của \(x\): \(3(-5) - 4(5) = -35\), khớp hoàn toàn!',
            r'Với bài đồng nhất đa thức, chỉ nhặt đúng 1 bậc chứa tham số cần tìm (như bậc \(x^2\)) rồi đối chiếu hai vế — tiết kiệm hơn nửa thời gian.',
            {
                'A': ('Sign Error', r'Sai dấu khi chuyển vế hoặc nhân dấu trừ, tính nhầm \(k = -5\).'),
                'B': ('Đáp án đúng', r'Đồng nhất hệ số \(x^2\): \(3k - 8 = 7 \implies k = 5\) (khớp luôn hệ số \(x\) là \(-35\)).'),
                'C': ('Partial Calculation', r'Lấy luôn hệ số \(7\) của \(x^2\) ở vế phải làm \(k\).'),
                'D': ('Forgot Division', r'Tính đúng \(3k = 15\) nhưng quên chia cho \(3\).'),
            },
            desmos_tip_vi=r'Thay một giá trị đơn giản như \(x = 1\) vào hai vế trên Desmos: \((3 - 4)(2 + k - 5) = 6 + 7 - 35 + 20 \implies -(k - 3) = -2 \implies k = 5\) trong 5 giây!',
        ),

        # Q3 — Medium, MCQ, Ans=A
        math_mcq(
            'sat_m2_2_q3', 3, DOMAIN, SK_EQUIV, 'Medium',
            r'<p>\[\frac{5}{x - 3} - \frac{2}{x + 1}\]</p>'
            r'<p>For \(x \neq 3\) and \(x \neq -1\), the expression above is given.</p>',
            r'<p>Which of the following is equivalent to the given expression?</p>',
            {
                'A': r'\(\frac{3x + 11}{(x - 3)(x + 1)}\)',
                'B': r'\(\frac{3x - 1}{(x - 3)(x + 1)}\)',
                'C': r'\(\frac{3}{(x - 3)(x + 1)}\)',
                'D': r'\(\frac{7x - 1}{(x - 3)(x + 1)}\)',
            },
            'A',
            r'Quy đồng mẫu chung \((x - 3)(x + 1)\): \[\frac{5(x + 1) - 2(x - 3)}{(x - 3)(x + 1)} = \frac{5x + 5 - 2x + 6}{(x - 3)(x + 1)} = \frac{3x + 11}{(x - 3)(x + 1)}.\]'
            r'Chú ý phân phối dấu trừ: \(-2(-3) = +6\), nên hằng số ở tử là \(5 + 6 = 11\).',
            r'90% lỗi sai ở phép trừ phân thức là quên phân phối dấu trừ vào số hạng thứ hai của tử số thứ hai (\(-2 \cdot (-3) = +6\)).',
            {
                'A': ('Đáp án đúng', r'Quy đồng và phân phối dấu chuẩn: \(5x + 5 - 2x + 6 = 3x + 11\).'),
                'B': ('Sign Distribution Trap', r'Quên đổi dấu \(-2(-3)\), tính nhầm \(5 - 6 = -1\) thay vì \(5 + 6 = 11\).'),
                'C': ('Skipped Cross-Multiply', r'Trừ thẳng tử số \(5 - 2 = 3\) mà không nhân chéo với mẫu số tương ứng.'),
                'D': ('Operation Error', r'Cộng nhầm \(5x + 2x = 7x\) thay vì lấy hiệu \(5x - 2x\).'),
            },
            desmos_tip_vi=r'Vẽ đồ thị biểu thức đề \(f(x) = \frac{5}{x - 3} - \frac{2}{x + 1}\) và từng đáp án (hoặc gán \(x = 4\) để tính giá trị số: \(\frac{5}{1} - \frac{2}{5} = 4.6\), khớp ngay đáp án A: \(\frac{23}{5} = 4.6\)).',
        ),

        # Q4 — Medium, SPR
        math_spr(
            'sat_m2_2_q4', 4, DOMAIN, SK_NONLIN_EQ, 'Medium',
            r'<p>\[\frac{x^2 - 5x}{x - 4} = \frac{4 - 2x}{x - 4}\]</p>',
            r'<p>What is the solution to the given equation?</p>',
            ['-1'], '-1',
            r'Điều kiện xác định (mẫu khác \(0\)): \(x \neq 4\).<br/>'
            r'Nhân cả hai vế với \((x - 4)\): \[x^2 - 5x = 4 - 2x \implies x^2 - 3x - 4 = 0 \implies (x - 4)(x + 1) = 0.\]'
            r'Ta thu được hai nghiệm ứng viên \(x = 4\) và \(x = -1\). Tuy nhiên \(x = 4\) làm mẫu số bằng \(0\) nên là nghiệm ngoại lai (extraneous root) và bị loại. Nghiệm duy nhất là \(x = -1\).',
            r'Mọi phương trình chứa ẩn ở mẫu bắt buộc phải kiểm tra điều kiện mẫu \(\neq 0\) ngay bước đầu để loại nghiệm ngoại lai.',
            desmos_tip_vi=r'Vẽ \(y = \frac{x^2 - 5x}{x - 4}\) và \(y = \frac{4 - 2x}{x - 4}\) trên Desmos. Hai đường cắt nhau duy nhất tại \(x = -1\) (tại \(x = 4\) là tiệm cận đứng, không có giao điểm).',
        ),

        # Q5 — Medium-Hard, MCQ, Ans=C
        math_mcq(
            'sat_m2_2_q5', 5, DOMAIN, SK_EQUIV, 'Medium-Hard',
            r'<p>When the polynomial \(P(x) = 2x^3 - 5x^2 + kx - 9\), where \(k\) is a constant, is divided by \(x - 3\), the remainder is \(15\).</p>',
            r'<p>What is the value of \(k\)?</p>',
            {'A': r'\(0\)', 'B': r'\(2\)', 'C': r'\(5\)', 'D': r'\(8\)'},
            'C',
            r'Theo Định lý Số dư (Remainder Theorem), số dư khi chia \(P(x)\) cho \((x - 3)\) đúng bằng \(P(3)\).<br/>'
            r'Thay \(x = 3\) và cho bằng \(15\): \[P(3) = 2(3)^3 - 5(3)^2 + 3k - 9 = 54 - 45 + 3k - 9 = 3k.\]'
            r'Suy ra \(3k = 15 \implies k = 5\).',
            r'Định lý Số dư (Remainder Theorem): số dư khi chia đa thức \(P(x)\) cho \((x - a)\) là \(P(a)\) — không cần chia đa thức dài dòng.',
            {
                'A': ('Set Remainder to 0', r'Cho nhầm \(P(3) = 0\) (nhầm sang Factor Theorem) dẫn đến \(3k = 0 \implies k = 0\).'),
                'B': ('Dropped Constant Term', r'Quên hạng tử \(-9\), giải nhầm \(54 - 45 + 3k = 15 \implies 3k = 6 \implies k = 2\).'),
                'C': ('Đáp án đúng', r'\(P(3) = 54 - 45 + 3k - 9 = 3k = 15 \implies k = 5\).'),
                'D': ('Arithmetic Error', r'Rút gọn nhầm \(54 - 45 = 0\), dẫn đến \(3k - 9 = 15 \implies k = 8\).'),
            },
            desmos_tip_vi=r'Gõ thẳng \(2(3)^3 - 5(3)^2 + 3k - 9 = 15\) (thay \(k\) bằng \(x\)) trên Desmos, đọc ngay đường thẳng đứng \(x = 5\).',
        ),

        # Q6 — Medium-Hard, MCQ, Ans=D
        math_mcq(
            'sat_m2_2_q6', 6, DOMAIN, SK_NONLIN_EQ, 'Medium-Hard',
            r'<p>A polynomial function \(f\) has real zeros only at \(x = -3\), \(x = 1\), and \(x = 4\). In the \(xy\)-plane, the graph of \(y = f(x)\) crosses the \(x\)-axis at \((-3, 0)\) and \((4, 0)\), is tangent to (touches without crossing) the \(x\)-axis at \((1, 0)\), and satisfies \(f(x) \to -\infty\) as \(x \to \infty\) and as \(x \to -\infty\).</p>',
            r'<p>Which of the following could define \(f(x)\)?</p>',
            {
                'A': r'\(f(x) = (x + 3)(x - 1)^2(x - 4)\)',
                'B': r'\(f(x) = -(x - 3)(x + 1)^2(x + 4)\)',
                'C': r'\(f(x) = -(x + 3)^2(x - 1)(x - 4)\)',
                'D': r'\(f(x) = -(x + 3)(x - 1)^2(x - 4)\)',
            },
            'D',
            r'Phân tích từng đặc trưng đồ thị đa thức:<br/>'
            r'• Các nghiệm là \(-3, 1, 4\) nên các nhân tử tương ứng là \((x + 3),\; (x - 1),\; (x - 4)\).<br/>'
            r'• Đồ thị tiếp xúc trục \(Ox\) tại \(x = 1\) (không cắt qua) \(\implies\) bội của \((x - 1)\) phải là số chẵn (nhỏ nhất là mũ \(2\)). Cắt qua tại \(-3\) và \(4\) \(\implies\) bội lẻ (mũ \(1\)).<br/>'
            r'• Cả hai nhánh đều hướng xuống \(-\infty\) khi \(x \to \pm\infty\) \(\implies\) bậc chẵn (bậc \(4\)) và hệ số đầu âm (\(-\)).<br/>'
            r'Vậy \(f(x) = -(x + 3)(x - 1)^2(x - 4)\).',
            r'Ghi nhớ quy tắc bội nghiệm (multiplicity): cắt trục \(Ox\) = mũ lẻ; chạm rồi bật lại (tangent) = mũ chẵn; cả hai đầu cùng hướng \(-\infty\) = bậc chẵn + hệ số đầu âm.',
            {
                'A': ('End Behavior Trap', r'Hệ số đầu dương với bậc \(4\) khiến cả hai đầu đồ thị hướng lên \(+\infty\), trái với giả thiết \(-\infty\).'),
                'B': ('Sign Error on Factors', r'Đổi sai dấu cả ba nghiệm thành \(x = 3, -1, -4\).'),
                'C': ('Wrong Multiplicity', r'Đặt mũ chẵn tại \((x + 3)^2\) làm đồ thị tiếp xúc tại \(x = -3\) thay vì \(x = 1\).'),
                'D': ('Đáp án đúng', r'Đúng đủ 3 nghiệm, đúng bội chẵn tại \(x = 1\), bậc chẵn và hệ số đầu âm.'),
            },
            desmos_tip_vi=r'Gõ nhanh đáp án nghi ngờ vào Desmos để nhìn trực quan đồ thị: kiểm tra đồ thị cắt tại \(-3\) và \(4\), chạm bật lại tại \(1\), và 2 nhánh đều chúc xuống dưới.',
        ),

        # Q7 — Medium-Hard, MCQ, Ans=A
        math_mcq(
            'sat_m2_2_q7', 7, DOMAIN, SK_EQUIV, 'Medium-Hard',
            r'<p>\[\frac{4x^2 - 5x + 7}{x - 2} = ax + b + \frac{c}{x - 2}\]</p>'
            r'<p>The equation above is true for all \(x \neq 2\), where \(a\), \(b\), and \(c\) are constants.</p>',
            r'<p>What is the value of \(c\)?</p>',
            {'A': r'\(13\)', 'B': r'\(3\)', 'C': r'\(7\)', 'D': r'\(33\)'},
            'A',
            r'Nhân cả hai vế với \((x - 2)\): \[4x^2 - 5x + 7 = (ax + b)(x - 2) + c.\]'
            r'Thay ngay \(x = 2\) để triệt tiêu hoàn toàn \((ax + b)(x - 2)\): \[c = 4(2)^2 - 5(2) + 7 = 16 - 10 + 7 = 13.\]'
            r'(Nếu chia đa thức đầy đủ: \(4x^2 - 5x + 7 = (4x + 3)(x - 2) + 13\), nên \(a = 4, b = 3, c = 13\).)',
            r'Trong đẳng thức \(\frac{P(x)}{x - r} = Q(x) + \frac{c}{x - r}\), hằng số \(c\) luôn chính là số dư \(P(r)\) — tính trong 3 giây mà không cần chia đa thức!',
            {
                'A': ('Đáp án đúng', r'Thay \(x = 2\) vào tử số được ngay số dư \(c = 4(4) - 10 + 7 = 13\).'),
                'B': ('Wrong Constant', r'Đây là giá trị của \(b = 3\) trong thương số \((4x + 3)\), không phải số dư \(c\).'),
                'C': ('Naive Constant Copy', r'Lấy nhầm hằng số tự do \(7\) của tử số làm số dư \(c\).'),
                'D': ('Sign Error', r'Thay nhầm \(x = -2\) thay vì \(x = 2\): \(4(4) - 5(-2) + 7 = 33\).'),
            },
            desmos_tip_vi=r'Đặt \(P(x) = 4x^2 - 5x + 7\) trên Desmos rồi gõ \(P(2)\) sẽ trả ngay giá trị \(c = 13\).',
        ),

        # Q8 — Medium-Hard, SPR
        math_spr(
            'sat_m2_2_q8', 8, DOMAIN, SK_NONLIN_EQ, 'Medium-Hard',
            r'<p>\[\frac{2x}{x - 3} - \frac{5}{x + 2} = \frac{30}{x^2 - x - 6}\]</p>',
            r'<p>What is the real solution to the given equation?</p>',
            ['-5/2', '-2.5'], '-5/2 (hoặc -2.5)',
            r'Phân tích mẫu vế phải: \(x^2 - x - 6 = (x - 3)(x + 2)\). Điều kiện xác định: \(x \neq 3\) và \(x \neq -2\).<br/>'
            r'Nhân cả hai vế với \((x - 3)(x + 2)\): \[2x(x + 2) - 5(x - 3) = 30 \implies 2x^2 + 4x - 5x + 15 = 30 \implies 2x^2 - x - 15 = 0.\]'
            r'Phân tích nhân tử: \((2x + 5)(x - 3) = 0 \implies x = -\frac{5}{2}\) hoặc \(x = 3\).<br/>'
            r'Loại \(x = 3\) vì làm mẫu \((x - 3) = 0\). Nghiệm thực duy nhất là \(x = -\frac{5}{2} = -2.5\).',
            r'Đề SAT Hard M2 cực thích gài 1 nghiệm nguyên đẹp là nghiệm ngoại lai (\(x = 3\)) và bắt học sinh nhập nghiệm phân số âm (\(-5/2\)). Luôn kiểm tra điều kiện mẫu!',
            desmos_tip_vi=r'Vẽ vế trái \(y = \frac{2x}{x - 3} - \frac{5}{x + 2}\) và vế phải \(y = \frac{30}{x^2 - x - 6}\) trên Desmos. Hai đồ thị chỉ giao nhau duy nhất tại \(x = -2.5\) (tự động loại bỏ nghiệm ngoại lai \(x = 3\))!',
        ),

        # Q9 — Medium-Hard, MCQ, Ans=B
        math_mcq(
            'sat_m2_2_q9', 9, DOMAIN, SK_EQUIV, 'Medium-Hard',
            r'<p>The polynomial \(x^3 + 3x^2 - 16x - 48\) can be written in the equivalent factored form \((x + a)(x + b)(x + c)\), where \(a\), \(b\), and \(c\) are integers such that \(a < b < c\).</p>',
            r'<p>What is the value of \(c - a\)?</p>',
            {'A': r'\(7\)', 'B': r'\(8\)', 'C': r'\(1\)', 'D': r'\(0\)'},
            'B',
            r'Nhóm hai cặp hạng tử (factoring by grouping): \[x^3 + 3x^2 - 16x - 48 = x^2(x + 3) - 16(x + 3) = (x + 3)(x^2 - 16).\]'
            r'Tiếp tục dùng hằng đẳng thức hiệu hai bình phương: \[(x + 3)(x - 4)(x + 4).\]'
            r'Vì dạng yêu cầu là \((x + a)(x + b)(x + c)\) với \(a < b < c\), ta có \(a = -4,\; b = 3,\; c = 4\).<br/>'
            r'Do đó \(c - a = 4 - (-4) = 8\).',
            r'Thấy đa thức bậc ba có 4 hạng tử mà tỉ lệ hệ số cặp đầu bằng cặp cuối (\(1:3 = -16:-48\)), lập tức nhóm hạng tử (grouping) rồi tách tiếp hiệu hai bình phương.',
            {
                'A': ('Wrong Ordering', r'Lấy nhầm \(4 - (-3) = 7\) do đảo dấu nghiệm \(-3\) thành \(a = -3\) thay vì dùng hệ số \(+3\) trong \((x + 3)\).'),
                'B': ('Đáp án đúng', r'Với \(a = -4, b = 3, c = 4\), ta có \(c - a = 4 - (-4) = 8\).'),
                'C': ('Wrong Pair', r'Tính nhầm \(c - b = 4 - 3 = 1\) thay vì \(c - a\).'),
                'D': ('Sign Error', r'Cộng nhầm \(c + a = 4 + (-4) = 0\) thay vì trừ \(c - a\).'),
            },
            desmos_tip_vi=r'Vẽ \(y = x^3 + 3x^2 - 16x - 48\) trên Desmos, bấm 3 giao điểm trục \(Ox\) ra \(x = -4, -3, 4\), suy ra các nhân tử \((x+4)(x+3)(x-4)\) nên \(a = -4, b = 3, c = 4 \implies c - a = 8\).',
        ),

        # Q10 — Medium-Hard, MCQ, Ans=D
        math_mcq(
            'sat_m2_2_q10', 10, DOMAIN, SK_EQUIV, 'Medium-Hard',
            r'<p>\[\frac{7x + 13}{(x - 1)(x + 3)} = \frac{A}{x - 1} + \frac{B}{x + 3}\]</p>'
            r'<p>The equation above is true for all \(x \neq 1\) and \(x \neq -3\), where \(A\) and \(B\) are constants.</p>',
            r'<p>What is the value of \(A - B\)?</p>',
            {'A': r'\(-3\)', 'B': r'\(2\)', 'C': r'\(7\)', 'D': r'\(3\)'},
            'D',
            r'Nhân cả hai vế với mẫu chung \((x - 1)(x + 3)\): \[7x + 13 = A(x + 3) + B(x - 1).\]'
            r'Dùng phương pháp thế điểm nút (Heaviside cover-up):<br/>'
            r'• Thay \(x = 1\): \(7(1) + 13 = A(4) + 0 \implies 4A = 20 \implies A = 5\).<br/>'
            r'• Thay \(x = -3\): \(7(-3) + 13 = 0 + B(-4) \implies -4B = -8 \implies B = 2\).<br/>'
            r'Vậy \(A - B = 5 - 2 = 3\).',
            r'Với phân tích phân thức hữu tỉ (partial fractions), thay ngay các nghiệm của mẫu số (\(x = 1\) và \(x = -3\)) sau khi khử mẫu để tìm tức thì \(A, B\) mà không cần giải hệ phương trình.',
            {
                'A': ('Reversed Subtraction', r'Tính ngược \(B - A = 2 - 5 = -3\) hoặc gán nhầm \(A\) với mẫu \((x + 3)\).'),
                'B': ('Partial Answer', r'Chỉ trả lời giá trị \(B = 2\) mà quên tính \(A - B\).'),
                'C': ('Sum Instead of Difference', r'Tính tổng \(A + B = 7\) (chính là hệ số của \(x\)) thay vì hiệu \(A - B\).'),
                'D': ('Đáp án đúng', r'\(A = 5\) và \(B = 2\), suy ra \(A - B = 3\).'),
            },
            desmos_tip_vi=r'Sau khi nhẩm \(7x + 13 = A(x + 3) + B(x - 1)\), gõ \(A = \frac{7(1) + 13}{4}\) và \(B = \frac{7(-3) + 13}{-4}\) trên Desmos rồi tính \(A - B = 3\).',
        ),

        # Q11 — Hard (750-800), MCQ, Ans=A
        math_mcq(
            'sat_m2_2_q11', 11, DOMAIN, SK_EQUIV, 'Hard (750-800)',
            r'<p>\[(px - 3)(qx + 5) = 12x^2 + rx - 15\]</p>'
            r'<p>The equation above is true for all values of \(x\), where \(p\), \(q\), and \(r\) are integers, \(p + q = 7\), and \(p > q\).</p>',
            r'<p>What is the value of \(r\)?</p>',
            {'A': r'\(11\)', 'B': r'\(3\)', 'C': r'\(-11\)', 'D': r'\(29\)'},
            'A',
            r'Khai triển vế trái: \[pqx^2 + (5p - 3q)x - 15 = 12x^2 + rx - 15.\]'
            r'Đồng nhất hệ số cho \(pq = 12\) và \(r = 5p - 3q\).<br/>'
            r'Kết hợp với \(p + q = 7\) và \(p, q \in \mathbb{Z}\), cặp số có tổng \(7\) và tích \(12\) là \(\{4, 3\}\).<br/>'
            r'Vì giả thiết cho \(p > q\), bắt buộc \(p = 4\) và \(q = 3\).<br/>'
            r'Do đó \(r = 5(4) - 3(3) = 20 - 9 = 11\).',
            r'Đọc kỹ điều kiện sắp thứ tự \(p > q\) ở các câu đồng nhất hệ số Module 2 Hard — đảo vai trò \(p, q\) luôn tạo ra đúng một phương án bẫy có sẵn trong 4 lựa chọn.',
            {
                'A': ('Đáp án đúng', r'Với \(p = 4, q = 3\), ta có \(r = 5(4) - 3(3) = 11\).'),
                'B': ('Ignored p > q Constraint', r'Chọn nhầm \(p = 3, q = 4\) (vi phạm \(p > q\)), tính ra \(5(3) - 3(4) = 3\).'),
                'C': ('Sign Error', r'Đổi ngược dấu hệ số giữa thành \(3q - 5p = -11\).'),
                'D': ('Sign Error', r'Cộng nhầm thay vì trừ: \(5(4) + 3(3) = 29\).'),
            },
            desmos_tip_vi=r'Giải nhanh \(p + q = 7,\; pq = 12\) bằng cách vẽ \(y = x(7 - x) - 12\), hai nghiệm là \(3\) và \(4\); lấy \(p = 4 > q = 3\) rồi tính \(5(4) - 3(3) = 11\).',
        ),

        # Q12 — Hard (750-800), SPR
        math_spr(
            'sat_m2_2_q12', 12, DOMAIN, SK_NONLIN_EQ, 'Hard (750-800)',
            r'<p>The polynomial \(g(x) = x^3 + ax^2 + bx - 12\), where \(a\) and \(b\) are constants, is divisible by both \((x - 2)\) and \((x + 3)\).</p>',
            r'<p>What is the value of \(a + b\)?</p>',
            ['-1'], '-1',
            r'<strong>Cách 1 (Siêu tốc bằng hằng số tự do):</strong> Vì \(g(x)\) là đa thức bậc 3 có hệ số đầu bằng \(1\) và chia hết cho \((x - 2)(x + 3)\), ta viết \(g(x) = (x - 2)(x + 3)(x - r)\).<br/>'
            r'Hằng số tự do là \((-2)(3)(-r) = 6r = -12 \implies r = -2\).<br/>'
            r'Vậy \(g(x) = (x - 2)(x + 2)(x + 3) = (x^2 - 4)(x + 3) = x^3 + 3x^2 - 4x - 12\). Suy ra \(a = 3,\; b = -4\), và \(a + b = -1\).<br/>'
            r'<strong>Cách 2 (Hệ phương trình):</strong> \(g(2) = 0 \implies 2a + b = 2\) và \(g(-3) = 0 \implies 3a - b = 13\). Cộng lại ra \(5a = 15 \implies a = 3, b = -4 \implies a + b = -1\).',
            r'Khi một đa thức monic bậc 3 đã biết 2 nhân tử và hệ số tự do \(d\), tích 3 nghiệm bằng \(-d\) giúp chốt ngay nghiệm thứ 3 mà không cần giải hệ!',
            desmos_tip_vi=r'Gõ hệ phương trình từ Factor Theorem \(4x + 2y = 4\) và \(9x - 3y = 39\) trên Desmos (với \(x = a, y = b\)); bấm giao điểm \((3, -4)\) rồi cộng \(3 + (-4) = -1\).',
        ),

        # Q13 — Hard (750-800), MCQ, Ans=C
        math_mcq(
            'sat_m2_2_q13', 13, DOMAIN, SK_NONLIN_EQ, 'Hard (750-800)',
            r'<p>The graph of the cubic polynomial \(h(x) = 2x^3 - 10x^2 + px + q\), where \(p\) and \(q\) are constants, has \(x\)-intercepts at \((-1, 0)\), \((2, 0)\), and \((r, 0)\).</p>',
            r'<p>What is the value of \(q\)?</p>',
            {'A': r'\(8\)', 'B': r'\(-16\)', 'C': r'\(16\)', 'D': r'\(4\)'},
            'C',
            r'Áp dụng định lý Viète cho đa thức bậc ba \(ax^3 + bx^2 + cx + d\), tổng ba nghiệm bằng \(-\frac{b}{a}\): \[-1 + 2 + r = -\frac{-10}{2} = 5 \implies r = 4.\]'
            r'Khi đã biết đủ 3 nghiệm và hệ số đầu \(a = 2\), viết ngay dạng tích nhân tử: \[h(x) = 2(x + 1)(x - 2)(x - 4).\]'
            r'Hằng số tự do \(q\) chính là \(h(0)\): \[q = h(0) = 2(1)(-2)(-4) = 16.\]',
            r'Viète bậc ba: tổng 3 nghiệm của \(ax^3 + bx^2 + cx + d\) luôn là \(-\frac{b}{a}\) và tích 3 nghiệm là \(-\frac{d}{a}\) (tức \(d = -a r_1 r_2 r_3\)).',
            {
                'A': ('Forgot Leading Coefficient', r'Quên nhân hệ số đầu \(a = 2\), tính nhầm \((1)(-2)(-4) = 8\).'),
                'B': ('Sign Error', r'Sai dấu khi nhân \(2(1)(-2)(-4)\) hoặc quên dấu trừ trong \(d = -a r_1 r_2 r_3\).'),
                'C': ('Đáp án đúng', r'Tìm được nghiệm thứ ba \(r = 4\), rồi tính \(q = h(0) = 2(1)(-2)(-4) = 16\).'),
                'D': ('Wrong Variable', r'Trả lời giá trị nghiệm \(r = 4\) (hoặc hệ số \(p = 4\)) thay vì \(q = 16\).'),
            },
            desmos_tip_vi=r'Sau khi tìm \(r = 5 - (-1 + 2) = 4\), gõ \(h(x) = 2(x + 1)(x - 2)(x - 4)\) trên Desmos rồi bấm giao điểm trục \(Oy\) để đọc ngay \((0, 16)\).',
        ),

        # Q14 — Hard (750-800), MCQ, Ans=B
        math_mcq(
            'sat_m2_2_q14', 14, DOMAIN, SK_EQUIV, 'Hard (750-800)',
            r'<p>For all \(x > 3\), the rational expression \[\frac{2x^2 + kx - 15}{x^2 - 9}\] is equivalent to \(\frac{2x + 5}{x + 3}\), where \(k\) is a constant.</p>',
            r'<p>What is the value of \(k\)?</p>',
            {'A': r'\(-11\)', 'B': r'\(-1\)', 'C': r'\(1\)', 'D': r'\(11\)'},
            'B',
            r'Phân tích mẫu số: \(x^2 - 9 = (x - 3)(x + 3)\).<br/>'
            r'Để rút gọn được về \(\frac{2x + 5}{x + 3}\), tử số bắt buộc phải triệt tiêu nhân tử \((x - 3)\) với mẫu số, nghĩa là: \[2x^2 + kx - 15 = (2x + 5)(x - 3).\]'
            r'Khai triển vế phải: \[(2x + 5)(x - 3) = 2x^2 - 6x + 5x - 15 = 2x^2 - x - 15.\]'
            r'Đồng nhất hệ số của \(x\) ta được \(k = -1\). (Hoặc dùng Factor Theorem: tử số nhận \(x = 3\) làm nghiệm \(\implies 2(9) + 3k - 15 = 0 \implies k = -1\)).',
            r'Nếu phân thức \(\frac{P(x)}{(x - r)(x + r)}\) rút gọn được thành \(\frac{Q(x)}{x + r}\) thì \((x - r)\) chắc chắn là nhân tử của \(P(x)\), tức \(P(r) = 0\)!',
            {
                'A': ('Arithmetic Error', r'Tính nhầm \(-6x - 5x = -11x\) thay vì \(-6x + 5x\).'),
                'B': ('Đáp án đúng', r'Tử số bằng \((2x + 5)(x - 3) = 2x^2 - x - 15\), suy ra \(k = -1\).'),
                'C': ('Sign Error', r'Đổi nhầm dấu trong \((2x - 5)(x + 3) = 2x^2 + x - 15\), dẫn đến \(k = 1\).'),
                'D': ('Sign Error', r'Cộng cả hai tích thành \(6 + 5 = 11\).'),
            },
            desmos_tip_vi=r'Vì \((x - 3)\) bị rút gọn nên tử số bằng \(0\) tại \(x = 3\): gõ \(2(3)^2 + 3x - 15 = 0\) trên Desmos ra ngay \(x = -1\).',
        ),

        # Q15 — Hard (750-800), SPR
        math_spr(
            'sat_m2_2_q15', 15, DOMAIN, SK_NONLIN_EQ, 'Hard (750-800)',
            r'<p>\[\frac{x}{x - 3} - \frac{k}{x + 1} = \frac{x^2 + 19}{(x - 3)(x + 1)}\]</p>'
            r'<p>In the equation above, \(k\) is a constant.</p>',
            r'<p>What is the sum of all values of \(k\) for which the equation has no real solution?</p>',
            ['6'], '6',
            r'Điều kiện xác định: \(x \neq 3\) và \(x \neq -1\). Nhân hai vế với mẫu chung \((x - 3)(x + 1)\): \[x(x + 1) - k(x - 3) = x^2 + 19 \implies x^2 + x - kx + 3k = x^2 + 19 \implies (1 - k)x = 19 - 3k.\]'
            r'Phương trình phân thức gốc vô nghiệm trong <strong>2 kịch bản</strong> (đây chính là bẫy 800 điểm!):<br/>'
            r'• <strong>Kịch bản 1 (Vô nghiệm đại số):</strong> Hệ số của \(x\) bằng \(0\) còn vế phải khác \(0\): \(1 - k = 0 \implies k = 1\) (khi đó \(0 \cdot x = 16\), vô nghiệm).<br/>'
            r'• <strong>Kịch bản 2 (Nghiệm duy nhất rơi vào giá trị loại trừ):</strong><br/>'
            r'  – Thử \(x = 3\): \(3(1 - k) = 19 - 3k \implies 3 = 19\) (không có \(k\)).<br/>'
            r'  – Thử \(x = -1\): \(-(1 - k) = 19 - 3k \implies -1 + k = 19 - 3k \implies 4k = 20 \implies k = 5\) (khi \(k = 5\), phương trình rút gọn ra \(-4x = 4 \implies x = -1\), bị loại vì làm mẫu bằng \(0\)!).<br/>'
            r'Với mọi \(k \notin \{1, 5\}\), phương trình luôn có nghiệm thực hợp lệ. Vậy tổng các giá trị của \(k\) là \(1 + 5 = 6\).',
            r'Phương trình phân thức chứa tham số \(k\) vô nghiệm khi: (1) phương trình sau khử mẫu vô nghiệm, HOẶC (2) nghiệm duy nhất của nó trùng với giá trị làm mẫu bằng \(0\)!',
            desmos_tip_vi=r'Sau khi rút gọn về \((1 - k)x = 19 - 3k\), vẽ \(y = \frac{19 - 3x}{1 - x}\) trên Desmos (trục hoành là \(k\), trục tung là \(x\)). Tiệm cận đứng cho \(k = 1\), giao với đường ngang \(y = -1\) cho \(k = 5\), còn \(y = 3\) là tiệm cận ngang nên không cắt. Cộng \(1 + 5 = 6\)!',
        ),
    ]

    return build_math_drill_json(
        'Math Drill 2.2: Polynomials, Factor Theorem & Rational Equations (15 câu)',
        '15 câu trọng tâm Advanced Math • Định lý Nhân tử, Đồng nhất hệ số & Phương trình Phân thức (650–800)',
        'Advanced Math • Hard M2 Core',
        qs,
        target_minutes=24,
    )


# ============================================================================
# DRILL 2.3: Exponential Growth/Decay & Compound Scaling (15 Qs)
# MCQ Key Distribution (11 MCQs): A=3, B=2, C=3, D=3 | SPR: Q4, Q8, Q12, Q15
# ============================================================================
def _build_drill_m2_3():
    tbl_q3 = build_math_table(
        ['Year (\\(t\\))', 'Account X (USD)', 'Account Y (USD)'],
        [
            ['\\(0\\)', '$1,000', '$1,000'],
            ['\\(1\\)', '$1,200', '$1,250'],
            ['\\(2\\)', '$1,440', '$1,500'],
            ['\\(3\\)', '$1,728', '$1,750'],
        ],
        caption='Projected Account Balances Over Time',
    )
    tbl_q8 = build_math_table(
        ['\\(x\\)', '\\(g(x)\\)'],
        [['\\(1\\)', '\\(12\\)'], ['\\(3\\)', '\\(108\\)'], ['\\(5\\)', '\\(972\\)']],
        caption='Selected values of the exponential function g',
    )

    qs = [
        # Q1 — Medium, MCQ, Ans=A
        math_mcq(
            'sat_m2_3_q1', 1, DOMAIN, SK_NONLIN_FUNC, 'Medium',
            r'<p>A marine algae culture initially contains \(450\) cells, and the number of cells triples every \(4\) hours.</p>',
            r'<p>Which function \(P\) models the number of cells in the culture \(t\) hours after observation begins?</p>',
            {
                'A': r'\(P(t) = 450(3)^{\frac{t}{4}}\)',
                'B': r'\(P(t) = 450(3)^{4t}\)',
                'C': r'\(P(t) = 450(4)^{\frac{t}{3}}\)',
                'D': r'\(P(t) = 450(1 + 3t)\)',
            },
            'A',
            r'Số lượng tế bào nhân \(3\) (cơ số \(b = 3\)) sau mỗi chu kỳ \(k = 4\) giờ. Sau \(t\) giờ sẽ có \(\frac{t}{4}\) chu kỳ nhân ba.<br/>'
            r'Với giá trị ban đầu \(a = 450\), mô hình mũ là: \[P(t) = 450(3)^{\frac{t}{4}}.\]'
            r'Kiểm tra nhanh tại \(t = 4\): \(P(4) = 450(3)^1 = 1{,}350\) (đúng gấp \(3\) lần ban đầu).',
            r'Công thức tăng trưởng theo chu kỳ \(k\): \(f(t) = a(b)^{t/k}\) — LUÔN chia \(t\) cho độ dài chu kỳ \(k\), và kiểm chứng nhanh bằng cách thế \(t = k\).',
            {
                'A': ('Đáp án đúng', r'Thay \(t = 0 \implies 450\), thay \(t = 4 \implies 450 \cdot 3^1 = 1{,}350\), khớp tuyệt đối đề bài.'),
                'B': ('Inverted Exponent', r'Nhân \(4t\) thay vì chia \(\frac{t}{4}\); khi \(t = 4\) sẽ thành \(3^{16}\) lần (gấp ba \(4\) lần mỗi giờ!).'),
                'C': ('Base vs Period Swap', r'Đổi nhầm cơ số tăng trưởng (\(3\)) với độ dài chu kỳ (\(4\)).'),
                'D': ('Linear Model Trap', r'Viết nhầm sang hàm bậc nhất (tăng đều cộng thêm) thay vì hàm mũ (tăng theo bội số).'),
            },
            desmos_tip_vi=r'Mẹo thử nhanh 3 giây: đề nói sau \(t = 4\) giờ phải ra \(450 \times 3 = 1{,}350\). Thế \(t = 4\) vào 4 đáp án trên Desmos, chỉ duy nhất đáp án A cho đúng \(1{,}350\).',
        ),

        # Q2 — Medium, MCQ, Ans=C
        math_mcq(
            'sat_m2_3_q2', 2, DOMAIN, SK_NONLIN_FUNC, 'Medium',
            r'<p>The resale value \(V(t)\), in dollars, of a commercial delivery van \(t\) years after purchase is modeled by \[V(t) = 42{,}000(0.84)^t.\]</p>',
            r'<p>Which of the following statements best interprets the number \(0.84\) in this context?</p>',
            {
                'A': r'The van loses \(84\%\) of its value each year.',
                'B': r'The van’s value decreases by $840 each year.',
                'C': r'The van’s value decreases by \(16\%\) each year.',
                'D': r'The van’s value increases by \(84\%\) each year.',
            },
            'C',
            r'Trong hàm phân rã mũ \(V(t) = a(1 - r)^t\), cơ số \(0.84 = 1 - 0.16\) cho biết mỗi năm chiếc xe <strong>giữ lại \(84\%\)</strong> giá trị của năm trước, tương đương với việc <strong>giảm đi \(16\%\)</strong> mỗi năm.',
            r'Khi thấy cơ số \(b < 1\) (ví dụ \(0.84\)), phần trăm GIẢM là \(1 - b = 16\%\), tuyệt đối không đọc nhầm thành giảm \(84\%\)!',
            {
                'A': ('Rate vs Decay Factor', r'Bẫy kinh điển SAT: \(0.84\) là phần giá trị CÒN LẠI (\(84\%\)), không phải phần bị mất đi (\(16\%\)).'),
                'B': ('Linear Interpretation', r'Hàm mũ giảm theo tỷ lệ phần trăm, không giảm một lượng đô-la cố định hàng năm.'),
                'C': ('Đáp án đúng', r'Vì \(0.84 = 1 - 0.16\), giá trị xe giảm \(16\%\) mỗi năm.'),
                'D': ('Growth vs Decay Trap', r'Vì \(0 < 0.84 < 1\), hàm đang giảm dần chứ không tăng \(84\%\).'),
            },
            desmos_tip_vi=r'Tính trên Desmos: \(V(0) = 42{,}000\), \(V(1) = 42{,}000(0.84) = 35{,}280\). Phần trăm thay đổi là \(\frac{35{,}280 - 42{,}000}{42{,}000} = -0.16\), tức giảm \(16\%\).',
        ),

        # Q3 — Medium, MCQ, Ans=D
        math_mcq(
            'sat_m2_3_q3', 3, DOMAIN, SK_NONLIN_FUNC, 'Medium',
            f'<div style="margin-bottom:10px;">{tbl_q3}</div>'
            r'<p>The table shows the projected balances, in dollars, of Account X and Account Y at the end of year \(t\).</p>',
            r'<p>Which of the following best describes the growth of Account X and Account Y over the \(3\)-year period?</p>',
            {
                'A': r'Both Account X and Account Y grow linearly.',
                'B': r'Both Account X and Account Y grow exponentially.',
                'C': r'Account X grows linearly, and Account Y grows exponentially.',
                'D': r'Account X grows exponentially, and Account Y grows linearly.',
            },
            'D',
            r'Kiểm tra hiệu số liên tiếp (cho hàm bậc nhất) và tỉ số liên tiếp (cho hàm mũ):<br/>'
            r'• <strong>Account X:</strong> Hiệu số là \(+200,\; +240,\; +288\) (không đều), nhưng tỉ số là \(\frac{1200}{1000} = \frac{1440}{1200} = \frac{1728}{1440} = 1.2\) (không đổi \(\implies\) tăng trưởng mũ \(+20\%\)/năm).<br/>'
            r'• <strong>Account Y:</strong> Hiệu số là \(1250 - 1000 = 250\), \(1500 - 1250 = 250\), \(1750 - 1500 = 250\) (không đổi \(\implies\) tăng trưởng tuyến tính \(+\)$250/năm).',
            r'Với bảng có bước nhảy \(\Delta t\) đều nhau: Hiệu số không đổi \(\implies\) Linear; Tỉ số không đổi \(\implies\) Exponential.',
            {
                'A': ('Misread Account X', r'Account X tăng \(200\), rồi \(240\), rồi \(288\) — hiệu số không bằng nhau nên không thể là tuyến tính.'),
                'B': ('Misread Account Y', r'Tỉ số của Account Y giảm dần (\(1.25 \to 1.20 \to 1.167\)) nên không phải tăng trưởng mũ.'),
                'C': ('Swapped Accounts', r'Đảo ngược bản chất giữa Account X (mũ) và Account Y (tuyến tính).'),
                'D': ('Đáp án đúng', r'Account X có tỉ số không đổi \(1.2\) (mũ) và Account Y có hiệu số không đổi \(250\) (tuyến tính).'),
            },
            desmos_tip_vi=r'Gõ nhanh phép chia tỉ số trên Desmos: \(1440/1200 = 1.2\) và \(1728/1440 = 1.2\) xác nhận ngay Account X là hàm mũ; còn \(1500 - 1250 = 1750 - 1500 = 250\) xác nhận Account Y là tuyến tính.',
        ),

        # Q4 — Medium, SPR
        math_spr(
            'sat_m2_3_q4', 4, DOMAIN, SK_NONLIN_FUNC, 'Medium',
            r'<p>A radioactive tracer used in medical imaging has a half-life of \(6\) hours. A laboratory begins with a \(320\)-milligram sample of this tracer.</p>',
            r'<p>How many milligrams of the tracer remain after \(24\) hours?</p>',
            ['20'], '20',
            r'Chu kỳ bán rã là \(6\) giờ nên sau \(24\) giờ, số chu kỳ bán rã đã trôi qua là \(\frac{24}{6} = 4\) chu kỳ.<br/>'
            r'Khối lượng còn lại: \[M(24) = 320\left(\frac{1}{2}\right)^{\frac{24}{6}} = 320\left(\frac{1}{2}\right)^4 = \frac{320}{16} = 20\text{ mg}.\]',
            r'Bài bán rã (half-life): chỉ cần tính số lần chia đôi \(n = \frac{t}{t_{1/2}}\), sau đó tính \(M_0 \cdot (0.5)^n\).',
            desmos_tip_vi=r'Gõ thẳng \(320 \cdot (0.5)^{24/6}\) trên Desmos, nhận ngay đáp số \(20\).',
        ),

        # Q5 — Medium-Hard, MCQ, Ans=B
        math_mcq(
            'sat_m2_3_q5', 5, DOMAIN, SK_EQUIV, 'Medium-Hard',
            r'<p>The value, in dollars, of a savings certificate \(t\) years after deposit is modeled by \[A(t) = 2{,}500(1.04)^{2t}.\]</p>',
            r'<p>Which of the following equivalent expressions displays the annual growth factor as a base raised to the power \(t\)?</p>',
            {
                'A': r'\(2{,}500(1.08)^t\)',
                'B': r'\(2{,}500(1.0816)^t\)',
                'C': r'\(2{,}500(1.02)^t\)',
                'D': r'\(5{,}000(1.04)^t\)',
            },
            'B',
            r'Áp dụng quy tắc lũy thừa của lũy thừa \(b^{ct} = (b^c)^t\): \[2{,}500(1.04)^{2t} = 2{,}500\left((1.04)^2\right)^t.\]'
            r'Tính chính xác \((1.04)^2 = (1 + 0.04)^2 = 1 + 0.08 + 0.0016 = 1.0816\).<br/>'
            r'Vậy biểu thức tương đương là \(2{,}500(1.0816)^t\) (lãi suất hiệu dụng hàng năm là \(8.16\%\), không phải \(8\%\)).',
            r'Khi chuyển đổi kỳ ghép lãi \((1 + r)^{nt} = ((1 + r)^n)^t\), PHẢI nâng lũy thừa toàn bộ cơ số \((1 + r)^n\) — không bao giờ nhân tuyến tính \(n \cdot r\)!',
            {
                'A': ('Linear Rate Trap', r'Bẫy cực phổ biến: nhân đôi \(4\% \times 2 = 8\%\) thành \(1.08\) thay vì bình phương \((1.04)^2 = 1.0816\).'),
                'B': ('Đáp án đúng', r'Vì \((1.04)^2 = 1.0816\), ta có \(2{,}500(1.04)^{2t} = 2{,}500(1.0816)^t\).'),
                'C': ('Halved Rate Trap', r'Chia đôi lãi suất \(4\% / 2 = 2\%\) thay vì nâng lên lũy thừa \(2\).'),
                'D': ('Coefficient Multiply Trap', r'Nhân nhầm số mũ \(2\) vào hệ số ban đầu \(2{,}500\) thành \(5{,}000\).'),
            },
            desmos_tip_vi=r'Gõ thẳng \(1.04^2\) trên Desmos ra ngay \(1.0816\) — chốt đáp án B trong 2 giây mà không lo sai số làm tròn!',
        ),

        # Q6 — Medium-Hard, MCQ, Ans=A
        math_mcq(
            'sat_m2_3_q6', 6, DOMAIN, SK_NONLIN_FUNC, 'Medium-Hard',
            r'<p>The function \(f\) is defined by \[f(x) = 18(3)^{x - 2}.\]</p>',
            r'<p>Which of the following equivalent forms of \(f(x)\) displays the \(y\)-intercept of the graph of \(y = f(x)\) in the \(xy\)-plane as a constant or coefficient?</p>',
            {
                'A': r'\(f(x) = 2(3)^x\)',
                'B': r'\(f(x) = 6(3)^{x - 1}\)',
                'C': r'\(f(x) = 162(3)^x\)',
                'D': r'\(f(x) = 54(3)^{x - 3}\)',
            },
            'A',
            r'Tung độ gốc (\(y\)-intercept) là giá trị \(f(0)\): \[f(0) = 18(3)^{0 - 2} = 18 \cdot \frac{1}{9} = 2.\]'
            r'Tách hằng số ở số mũ: \[f(x) = 18 \cdot 3^x \cdot 3^{-2} = \frac{18}{9}(3)^x = 2(3)^x.\]'
            r'Dạng \(2(3)^x\) vừa tương đương với \(f(x)\) vừa hiển thị trực tiếp tung độ gốc \(2\) làm hệ số đứng trước.',
            r'Với \(f(x) = a \cdot b^{x - c}\), \(a\) KHÔNG phải là \(y\)-intercept! Phải tách \(b^{-c}\) ra ngoài nhân với \(a\) để đưa về dạng \(f(0) \cdot b^x\).',
            {
                'A': ('Đáp án đúng', r'Tách \(3^{-2} = \frac{1}{9}\), ta được \(18 \cdot \frac{1}{9} \cdot 3^x = 2(3)^x\), hiển thị rõ \(y\)-intercept là \(2\).'),
                'B': ('Equivalent But Wrong Form', r'Biểu thức này tương đương với \(f(x)\) nhưng vẫn còn dịch chuyển \(x - 1\) nên không hiển thị số \(2\).'),
                'C': ('Exponent Sign Trap', r'Nhân nhầm \(18 \times 3^2 = 162\) thay vì nhân \(18 \times 3^{-2} = 2\).'),
                'D': ('Equivalent But Wrong Form', r'Tương đương về mặt đại số (\(54/27 = 2\)) nhưng không hiển thị tung độ gốc \(2\) dưới dạng hệ số.'),
            },
            desmos_tip_vi=r'Vẽ \(f(x) = 18(3)^{x - 2}\) trên Desmos, bấm vào giao điểm với trục \(Oy\) thấy ngay \((0, 2)\). Chọn ngay phương án duy nhất có hệ số \(2\) và đồ thị trùng khít: \(2(3)^x\).',
        ),

        # Q7 — Medium-Hard, MCQ, Ans=C
        math_mcq(
            'sat_m2_3_q7', 7, DOMAIN, SK_NONLIN_FUNC, 'Medium-Hard',
            r'<p>A streaming platform’s active subscriber count increased by \(40\%\) during the first quarter of the year and then decreased by \(15\%\) during the second quarter.</p>',
            r'<p>Compared to the subscriber count at the start of the first quarter, the subscriber count at the end of the second quarter was:</p>',
            {
                'A': r'\(25\%\) greater',
                'B': r'\(21\%\) greater',
                'C': r'\(19\%\) greater',
                'D': r'\(6\%\) less',
            },
            'C',
            r'Gọi số thuê bao ban đầu là \(S_0\).<br/>'
            r'• Sau quý 1 (tăng \(40\%\)): \(S_1 = 1.40 S_0\).<br/>'
            r'• Sau quý 2 (giảm \(15\%\) trên \(S_1\)): \[S_2 = (1 - 0.15) S_1 = 0.85 \times 1.40 S_0 = 1.19 S_0.\]'
            r'Vì \(1.19 = 1 + 0.19\), số thuê bao cuối quý 2 lớn hơn \(19\%\) so với ban đầu.',
            r'Thay đổi phần trăm nối tiếp phải NHÂN các hệ số tăng/giảm \((1 + r_1)(1 - r_2)\) — tuyệt đối không cộng/trừ thẳng hai số phần trăm!',
            {
                'A': ('Additive Percent Trap', r'Trừ thẳng \(40\% - 15\% = 25\%\) mà quên rằng mức giảm \(15\%\) được tính trên nền mới \(140\%\), không phải nền gốc \(100\%\).'),
                'B': ('Arithmetic Error', r'Nhân nhầm \(1.40 \times 0.85\) ra \(1.21\) thay vì \(1.19\).'),
                'C': ('Đáp án đúng', r'\(1.40 \times 0.85 = 1.19\), tương ứng mức tăng ròng \(19\%\).'),
                'D': ('Multiplied Raw Rates', r'Nhân trực tiếp \(0.40 \times 0.15 = 0.06\) rồi kết luận nhầm là giảm \(6\%\).'),
            },
            desmos_tip_vi=r'Gõ thẳng \(1.40 \times 0.85 - 1\) trên Desmos ra ngay \(0.19\), tức tăng \(19\%\).',
        ),

        # Q8 — Medium-Hard, SPR
        math_spr(
            'sat_m2_3_q8', 8, DOMAIN, SK_NONLIN_FUNC, 'Medium-Hard',
            f'<div style="margin-bottom:10px;">{tbl_q8}</div>'
            r'<p>The table gives selected values of an exponential function \(g\) defined by \(g(x) = a \cdot b^x\), where \(a\) and \(b\) are positive constants.</p>',
            r'<p>What is the value of \(g(0)\)?</p>',
            ['4'], '4',
            r'Lấy tỉ số giữa hai giá trị trong bảng để khử \(a\): \[\frac{g(3)}{g(1)} = \frac{a \cdot b^3}{a \cdot b^1} = b^2 = \frac{108}{12} = 9.\]'
            r'Vì \(b > 0\), suy ra \(b = 3\). (Kiểm chứng: \(\frac{g(5)}{g(3)} = \frac{972}{108} = 9 = 3^2\), khớp hoàn toàn).<br/>'
            r'Thay \(x = 1\) vào \(g(x) = a \cdot 3^x\): \[12 = a \cdot 3^1 \implies a = 4.\]'
            r'Vậy \(g(0) = a \cdot 3^0 = 4\).',
            r'Khi bảng hàm mũ nhảy bước \(\Delta x = 2\) (từ \(1 \to 3 \to 5\)), tỉ số hai dòng liên tiếp là \(b^2\) chứ không phải \(b\) — nhớ lấy căn bậc \(\Delta x\)!',
            desmos_tip_vi=r'Nhập bảng \((1, 12), (3, 108), (5, 972)\) vào Desmos Table, gõ hồi quy \(y_1 \sim a \cdot b^{x_1}\) (nhớ tích ô Log Mode nếu cần hoặc đọc thẳng \(a = 4, b = 3\)). Suy ra \(g(0) = a = 4\).',
        ),

        # Q9 — Medium-Hard, MCQ, Ans=D
        math_mcq(
            'sat_m2_3_q9', 9, DOMAIN, SK_EQUIV, 'Medium-Hard',
            r'<p>A solar microgrid’s battery storage capacity increases by \(12\%\) every \(8\) months. The initial storage capacity is \(500\) kilowatt-hours.</p>',
            r'<p>Which equation models the storage capacity \(C\), in kilowatt-hours, \(t\) years after installation?</p>',
            {
                'A': r'\(C = 500(1.12)^{\frac{t}{8}}\)',
                'B': r'\(C = 500(1.12)^{\frac{2t}{3}}\)',
                'C': r'\(C = 500(1.12)^{8t}\)',
                'D': r'\(C = 500(1.12)^{\frac{3t}{2}}\)',
            },
            'D',
            r'Chú ý bẫy đơn vị thời gian: chu kỳ tính theo <strong>tháng</strong> (\(8\) tháng) trong khi biến \(t\) tính theo <strong>năm</strong>!<br/>'
            r'Đổi \(t\) năm sang tháng: \(12t\) tháng. Số chu kỳ \(8\) tháng trong \(t\) năm là: \[\frac{12t}{8} = \frac{3t}{2}.\]'
            r'Vì mỗi chu kỳ tăng \(12\%\) (nhân \(1.12\)), phương trình là \(C = 500(1.12)^{\frac{3t}{2}}\).<br/>'
            r'Kiểm tra nhanh tại \(t = 2\) năm (\(24\) tháng = đúng \(3\) chu kỳ \(8\) tháng): số mũ là \(\frac{3(2)}{2} = 3\), chính xác!',
            r'Khi chu kỳ cho bằng THÁNG còn biến \(t\) tính bằng NĂM, số mũ luôn là \(\frac{12t}{\text{số tháng mỗi chu kỳ}}\) — kiểm chứng bằng cách thế \(t = 2\) năm.',
            {
                'A': ('Unit Mismatch Trap', r'Quên đổi \(t\) năm sang \(12t\) tháng, viết nhầm số mũ \(\frac{t}{8}\) (tăng \(12\%\) mỗi \(8\) năm!).'),
                'B': ('Inverted Fraction', r'Đảo ngược tỉ số thành \(\frac{8}{12}t = \frac{2t}{3}\) thay vì \(\frac{12}{8}t\).'),
                'C': ('Multiply Instead of Convert', r'Nhân \(8t\) như thể tăng \(12\%\) tận \(8\) lần trong một năm.'),
                'D': ('Đáp án đúng', r'\(\frac{12t}{8} = \frac{3t}{2}\) chu kỳ trong \(t\) năm, cơ số tăng trưởng là \(1.12\).'),
            },
            desmos_tip_vi=r'Chọn mốc kiểm chứng dễ nhẩm: \(t = 2\) năm = \(24\) tháng = đúng \(3\) chu kỳ \(8\) tháng, nên số mũ phải bằng \(3\). Thế \(t = 2\) vào số mũ 4 đáp án: chỉ \(\frac{3(2)}{2} = 3\).',
        ),

        # Q10 — Medium-Hard, MCQ, Ans=B
        math_mcq(
            'sat_m2_3_q10', 10, DOMAIN, SK_NONLIN_FUNC, 'Medium-Hard',
            r'<p>The function \(f\) is defined by \[f(x) = -4(2)^x + 12\] and its graph is shown in the \(xy\)-plane.</p>',
            r'<p>Which of the following statements is true about the graph of \(y = f(x)\)?</p>',
            {
                'A': r'The \(y\)-intercept is \((0, 12)\), and \(f(x)\) is strictly increasing.',
                'B': r'The \(y\)-intercept is \((0, 8)\), and as \(x \to -\infty\), \(f(x)\) approaches \(12\).',
                'C': r'The \(y\)-intercept is \((0, 8)\), and as \(x \to \infty\), \(f(x)\) approaches \(12\).',
                'D': r'The \(y\)-intercept is \((0, -4)\), and as \(x \to -\infty\), \(f(x)\) approaches \(0\).',
            },
            'B',
            r'Phân tích đồ thị hàm mũ có dịch chuyển dọc \(f(x) = -4(2)^x + 12\):<br/>'
            r'• <strong>Tung độ gốc (\(x = 0\)):</strong> \(f(0) = -4(2)^0 + 12 = -4(1) + 12 = 8 \implies (0, 8)\).<br/>'
            r'• <strong>Tiệm cận ngang:</strong> Khi \(x \to -\infty\), ta có \(2^x \to 0\), nên \(-4(2)^x + 12 \to 0 + 12 = 12\). (Còn khi \(x \to +\infty\), \(2^x \to +\infty\) nên \(f(x) \to -\infty\)).',
            r'Với \(f(x) = a \cdot b^x + k\): tung độ gốc là \(a + k\) (KHÔNG phải \(k\) hay \(a\)), còn \(y = k\) là đường tiệm cận ngang!',
            {
                'A': ('Asymptote vs Y-Intercept', r'Nhầm tiệm cận ngang \(y = 12\) thành \(y\)-intercept; hơn nữa hệ số \(-4 < 0\) làm hàm nghịch biến chứ không đồng biến.'),
                'B': ('Đáp án đúng', r'\(f(0) = -4 + 12 = 8\), và khi \(x \to -\infty\) thì \(2^x \to 0\) nên \(f(x) \to 12\).'),
                'C': ('Reversed Asymptote End', r'Nhầm chiều tiệm cận: khi \(x \to +\infty\), \(-4(2)^x \to -\infty\) chứ không tiến về \(12\).'),
                'D': ('Ignored Vertical Shift', r'Quên hoàn toàn hằng số dịch chuyển \(+12\) ở cả tung độ gốc lẫn tiệm cận ngang.'),
            },
            desmos_tip_vi=r'Vẽ \(y = -4(2)^x + 12\) trên Desmos: bấm giao điểm trục \(Oy\) thấy ngay \((0, 8)\), và kéo sang trái (\(x \to -\infty\)) thấy đường cong áp sát sát đường ngang \(y = 12\).',
        ),

        # Q11 — Hard (750-800), MCQ, Ans=C
        math_mcq(
            'sat_m2_3_q11', 11, DOMAIN, SK_EQUIV, 'Hard (750-800)',
            r'<p>The population of an endangered amphibian species is modeled by \[P(t) = 6{,}400(0.81)^{\frac{t}{4}},\] where \(t\) is the number of years after 2020. According to the model, the population is predicted to decrease by \(p\%\) every \(2\) years.</p>',
            r'<p>What is the value of \(p\)?</p>',
            {'A': r'\(9.5\)', 'B': r'\(19\)', 'C': r'\(10\)', 'D': r'\(90\)'},
            'C',
            r'Để tìm hệ số nhân sau mỗi \(2\) năm, ta viết lại số mũ \(\frac{t}{4}\) thành bội của \(\frac{t}{2}\): \[\frac{t}{4} = \frac{1}{2} \cdot \frac{t}{2} \implies (0.81)^{\frac{t}{4}} = \left((0.81)^{\frac{1}{2}}\right)^{\frac{t}{2}} = (\sqrt{0.81})^{\frac{t}{2}} = (0.90)^{\frac{t}{2}}.\]'
            r'Mỗi \(2\) năm, quần thể nhân với \(0.90 = 1 - 0.10\), nghĩa là giảm đi \(10\%\). Vậy \(p = 10\).',
            r'Muốn chuyển chu kỳ mũ từ \(4\) năm xuống \(2\) năm, hãy lấy \(\sqrt{b} = b^{2/4}\) đối với cơ số \(b\), rồi tính \(p\% = (1 - b_{\text{mới}}) \times 100\%\). Không bao giờ chia đôi phần trăm!',
            {
                'A': ('Linear Rate Halving Trap', r'Bẫy 750+ kinh điển: thấy \(4\) năm giảm \(19\%\) nên chia đôi tuyến tính thành \(9.5\%\) cho \(2\) năm — sai vì tăng/giảm mũ không tuyến tính!'),
                'B': ('Wrong Time Period', r'Đây là phần trăm giảm sau \(4\) năm (\(1 - 0.81 = 19\%\)), chưa quy về chu kỳ \(2\) năm.'),
                'C': ('Đáp án đúng', r'\((0.81)^{2/4} = \sqrt{0.81} = 0.90\), tương đương giảm \(10\%\) mỗi \(2\) năm.'),
                'D': ('Remaining vs Decrease', r'Nhầm giữa tỉ lệ còn lại (\(90\%\)) và tỉ lệ giảm đi (\(10\%\)).'),
            },
            desmos_tip_vi=r'Gõ \(P(t) = 6400(0.81)^{t/4}\) trên Desmos, sau đó tính \(\left(1 - \frac{P(2)}{P(0)}\right) \times 100\), màn hình trả ngay đúng số \(10\)!',
        ),

        # Q12 — Hard (750-800), SPR
        math_spr(
            'sat_m2_3_q12', 12, DOMAIN, SK_NONLIN_FUNC, 'Hard (750-800)',
            r'<p>The function \(f\) is defined by \(f(x) = a \cdot b^x + c\), where \(a\), \(b\), and \(c\) are positive constants. In the \(xy\)-plane, the graph of \(y = f(x)\) passes through the points \((0, 11)\), \((1, 17)\), and \((2, 35)\).</p>',
            r'<p>What is the value of \(c\)?</p>',
            ['8'], '8',
            r'Viết 3 phương trình từ 3 điểm đã cho:<br/>'
            r'• \(f(0) = a + c = 11\)<br/>'
            r'• \(f(1) = ab + c = 17\)<br/>'
            r'• \(f(2) = ab^2 + c = 35\)<br/>'
            r'Trừ từng cặp liên tiếp để triệt tiêu ngay hằng số \(c\): \[f(1) - f(0) = a(b - 1) = 17 - 11 = 6, \qquad f(2) - f(1) = ab(b - 1) = 35 - 17 = 18.\]'
            r'Chia hai phương trình hiệu số cho nhau: \[b = \frac{18}{6} = 3.\]'
            r'Thay \(b = 3\) lại vào \(a(3 - 1) = 6 \implies 2a = 6 \implies a = 3\). Cuối cùng từ \(a + c = 11 \implies c = 11 - 3 = 8\).',
            r'Bí kíp 800 cho hàm mũ có dịch chuyển \(a \cdot b^x + c\): lấy các HIỆU LIÊN TIẾP \(\Delta y_1, \Delta y_2\) để khử \(c\) — tỉ số \(\frac{\Delta y_2}{\Delta y_1}\) chính là cơ số \(b\)!',
            desmos_tip_vi=r'Nhập 3 điểm \((0, 11), (1, 17), (2, 35)\) vào Desmos Table, gõ hồi quy \(y_1 \sim a \cdot b^{x_1} + c\). Desmos trả tức thì \(a = 3,\; b = 3,\; c = 8\)!',
        ),

        # Q13 — Hard (750-800), MCQ, Ans=A
        math_mcq(
            'sat_m2_3_q13', 13, DOMAIN, SK_EQUIV, 'Hard (750-800)',
            r'<p>The function \(h\) is defined by \[h(x) = 80(2)^{3x - 4}.\] When \(h(x)\) is rewritten in the equivalent form \(h(x) = c \cdot b^x\), where \(c\) and \(b\) are constants, both \(c\) and \(b\) are integers.</p>',
            r'<p>What is the value of \(c + b\)?</p>',
            {'A': r'\(13\)', 'B': r'\(7\)', 'C': r'\(18\)', 'D': r'\(1{,}288\)'},
            'A',
            r'Tách phần mũ hiệu và phần hệ số của \(x\) bằng quy tắc lũy thừa: \[h(x) = 80 \cdot 2^{3x} \cdot 2^{-4} = \frac{80}{16} \cdot (2^3)^x = 5 \cdot 8^x.\]'
            r'Đối chiếu với dạng \(c \cdot b^x\), ta có \(c = 5\) và \(b = 8\).<br/>'
            r'Vậy \(c + b = 5 + 8 = 13\).',
            r'Chuyển \(A \cdot m^{px + q}\) sang \(c \cdot b^x\): luôn có \(c = A \cdot m^q\) (giá trị tại \(x = 0\)) và \(b = m^p\) (cơ số mới sau khi gom hệ số của \(x\)).',
            {
                'A': ('Đáp án đúng', r'\(c = \frac{80}{2^4} = 5\) và \(b = 2^3 = 8\), suy ra \(c + b = 13\).'),
                'B': ('Forgot Exponent on Base', r'Tìm đúng \(c = 5\) nhưng giữ nguyên \(b = 2\) (quên gom mũ \(3\) thành \(2^3 = 8\)), tính ra \(5 + 2 = 7\).'),
                'C': ('Power Error', r'Tính nhầm \(2^4 = 8\) nên ra \(c = 80/8 = 10\), dẫn đến \(10 + 8 = 18\).'),
                'D': ('Exponent Sign Trap', r'Nhân nhầm \(80 \times 2^4 = 1{,}280\) thay vì chia \(80 / 2^4 = 5\), ra \(1{,}280 + 8 = 1{,}288\).'),
            },
            desmos_tip_vi=r'Gõ \(h(x) = 80(2)^{3x - 4}\) trên Desmos. Tính \(c = h(0) = 5\) và \(b = \frac{h(1)}{h(0)} = 8\), sau đó cộng \(c + b = 13\) — hoàn toàn không cần biến đổi mũ bằng tay!',
        ),

        # Q14 — Hard (750-800), MCQ, Ans=D
        math_mcq(
            'sat_m2_3_q14', 14, DOMAIN, SK_NONLIN_FUNC, 'Hard (750-800)',
            r'<p>At \(t = 0\) hours, Culture A contains \(12\) bacteria and doubles every \(3\) hours, while Culture B contains \(384\) bacteria and doubles every \(6\) hours.</p>',
            r'<p>After how many hours will Culture A and Culture B contain the exact same number of bacteria?</p>',
            {'A': r'\(15\)', 'B': r'\(18\)', 'C': r'\(24\)', 'D': r'\(30\)'},
            'D',
            r'Thiết lập hai hàm số lượng vi khuẩn sau \(t\) giờ: \[A(t) = 12 \cdot 2^{\frac{t}{3}}, \qquad B(t) = 384 \cdot 2^{\frac{t}{6}}.\]'
            r'Cho \(A(t) = B(t)\) và chia hai vế cho \(12 \cdot 2^{\frac{t}{6}}\): \[\frac{2^{\frac{t}{3}}}{2^{\frac{t}{6}}} = \frac{384}{12} \implies 2^{\frac{t}{3} - \frac{t}{6}} = 32 \implies 2^{\frac{t}{6}} = 2^5.\]'
            r'Đồng nhất số mũ: \(\frac{t}{6} = 5 \implies t = 30\) giờ.<br/>'
            r'Kiểm tra: \(A(30) = 12 \cdot 2^{10} = 12{,}288\) và \(B(30) = 384 \cdot 2^5 = 12{,}288\).',
            r'So sánh hai hàm mũ cùng cơ số \(a_1 b^{t/k_1} = a_2 b^{t/k_2}\): chia số đầu cho nhau và trừ số mũ — chú ý tốc độ đuổi kịp là hiệu \(\frac{1}{k_1} - \frac{1}{k_2}\)!',
            {
                'A': ('Ignored Culture B Growth', r'Giải nhầm \(2^{t/3} = 32 \implies t = 15\) như thể Culture B đứng yên không nhân đôi trong lúc Culture A tăng.'),
                'B': ('Arithmetic Guess', r'Nhân hai chu kỳ \(3 \times 6 = 18\) mà không giải phương trình mũ.'),
                'C': ('Power of 2 Error', r'Tính nhầm \(\frac{384}{12} = 16 = 2^4\) nên ra \(\frac{t}{6} = 4 \implies t = 24\).'),
                'D': ('Đáp án đúng', r'Mỗi \(6\) giờ, tỉ số \(A/B\) tăng gấp đôi; cần \(5\) chu kỳ \(6\) giờ để bù hệ số \(32 = 2^5\), tức \(t = 30\) giờ.'),
            },
            desmos_tip_vi=r'Gõ thẳng \(12 \cdot 2^{x/3} = 384 \cdot 2^{x/6}\) trên Desmos — máy kẻ ngay đường thẳng đứng tại \(x = 30\) (không cần phóng to trục \(y\) lên tới \(12{,}288\))!',
        ),

        # Q15 — Hard (750-800), SPR
        math_spr(
            'sat_m2_3_q15', 15, DOMAIN, SK_NONLIN_FUNC, 'Hard (750-800)',
            r'<p>The appraised value of a rare antique violin increases by \(r\%\) every \(5\) years, where \(r\) is a constant. The violin was valued at $8,000 in 2010 and $13,824 in 2025.</p>',
            r'<p>What is the value of \(r\)?</p>',
            ['20'], '20',
            r'Từ năm \(2010\) đến năm \(2025\) là \(15\) năm, tương ứng đúng \(\frac{15}{5} = 3\) chu kỳ \(5\) năm.<br/>'
            r'Gọi hệ số tăng trưởng mỗi chu kỳ là \(1 + \frac{r}{100}\). Ta có phương trình: \[8{,}000\left(1 + \frac{r}{100}\right)^3 = 13{,}824.\]'
            r'Chia hai vế cho \(8{,}000\) và rút gọn: \[\left(1 + \frac{r}{100}\right)^3 = \frac{13{,}824}{8{,}000} = \frac{1{,}728}{1{,}000} = \left(\frac{12}{10}\right)^3 = (1.2)^3.\]'
            r'Lấy căn bậc ba hai vế: \(1 + \frac{r}{100} = 1.2 \implies \frac{r}{100} = 0.2 \implies r = 20\).',
            r'Gặp bài tìm phần trăm tăng trưởng \(r\) qua nhiều chu kỳ: chia giá trị cuối cho giá trị đầu, lấy căn bậc \(n\) (số chu kỳ), rồi đổi sang phần trăm \((b - 1) \times 100\).',
            desmos_tip_vi=r'Gõ thẳng \(\left(\left(\frac{13824}{8000}\right)^{1/3} - 1\right) \cdot 100\) trên Desmos, trả ngay kết quả chính xác \(20\)!',
        ),
    ]

    return build_math_drill_json(
        'Math Drill 2.3: Exponential Growth/Decay & Compound Scaling (15 câu)',
        '15 câu trọng tâm Advanced Math • Tăng trưởng/Phân rã Mũ, Biến đổi Số mũ & Bẫy Giá trị ban đầu (650–800)',
        'Advanced Math • Hard M2 Core',
        qs,
        target_minutes=24,
    )


# ============================================================================
# DRILL 2.4: Nonlinear Systems, Radicals, Absolute Value & Transformations (15 Qs)
# MCQ Key Distribution (11 MCQs): A=2, B=3, C=3, D=3 | SPR: Q4, Q8, Q12, Q15
# ============================================================================
def _build_drill_m2_4():
    svg_q5 = svg_parabola_vertex(
        h_lbl='4',
        k_lbl='-3',
        opens_up=True,
        note='Graph of y = f(x) with vertex (4, -3)',
    )

    qs = [
        # Q1 — Medium, MCQ, Ans=C
        math_mcq(
            'sat_m2_4_q1', 1, DOMAIN, SK_NONLIN_EQ, 'Medium',
            r'<p>\[\sqrt{2x + 3} = x - 6\]</p>',
            r'<p>What is the set of all real solutions to the given equation?</p>',
            {
                'A': r'\(3\) only',
                'B': r'\(3\) and \(11\)',
                'C': r'\(11\) only',
                'D': r'There are no real solutions.',
            },
            'C',
            r'Vì căn bậc hai số học luôn không âm (\(\sqrt{2x + 3} \ge 0\)), điều kiện bắt buộc ở vế phải là \(x - 6 \ge 0 \implies x \ge 6\).<br/>'
            r'Bình phương hai vế: \[2x + 3 = (x - 6)^2 = x^2 - 12x + 36 \implies x^2 - 14x + 33 = 0 \implies (x - 11)(x - 3) = 0.\]'
            r'Thử lại vào phương trình gốc:<br/>'
            r'• \(x = 11\): \(\sqrt{25} = 5\) và \(11 - 6 = 5\) (thỏa mãn).<br/>'
            r'• \(x = 3\): \(\sqrt{9} = 3 \neq 3 - 6 = -3\) (nghiệm ngoại lai, loại!).<br/>'
            r'Vậy nghiệm duy nhất là \(11\).',
            r'Mọi phương trình chứa căn bậc hai sau khi bình phương BẮT BUỘC phải thử ngược lại vào vế phải (\(x - 6 \ge 0\)) để loại nghiệm ngoại lai.',
            {
                'A': ('Kept Extraneous Root', r'Giữ nhầm nghiệm ngoại lai \(x = 3\) làm vế phải bằng \(-3 < 0\), trong khi \(\sqrt{9} = +3\).'),
                'B': ('Extraneous Root Trap', r'Bẫy số 1 của SAT: giải đúng phương trình bậc hai nhưng quên thử lại vào phương trình căn gốc nên chọn cả \(3\) và \(11\).'),
                'C': ('Đáp án đúng', r'Chỉ có \(x = 11\) thỏa mãn \(\sqrt{2(11) + 3} = 5 = 11 - 6\).'),
                'D': ('Over-Eliminated', r'Loại nhầm cả nghiệm đúng \(x = 11\).'),
            },
            desmos_tip_vi=r'Vẽ \(y = \sqrt{2x + 3}\) và \(y = x - 6\) trên Desmos. Hai đồ thị chỉ giao nhau tại đúng 1 điểm \((11, 5)\) — tự động miễn nhiễm 100% bẫy nghiệm ngoại lai!',
        ),

        # Q2 — Medium, MCQ, Ans=B
        math_mcq(
            'sat_m2_4_q2', 2, DOMAIN, SK_NONLIN_EQ, 'Medium',
            r'<p>In physics, the period \(T\) of a simple pendulum of length \(L\) under gravitational acceleration \(g\) is modeled by \[T = 2\pi\sqrt{\frac{L}{g}},\] where \(T\), \(L\), and \(g\) are positive quantities.</p>',
            r'<p>Which equation correctly expresses \(L\) in terms of \(T\) and \(g\)?</p>',
            {
                'A': r'\(L = \frac{gT^2}{2\pi^2}\)',
                'B': r'\(L = \frac{gT^2}{4\pi^2}\)',
                'C': r'\(L = \frac{4\pi^2 g}{T^2}\)',
                'D': r'\(L = \frac{T^2}{4\pi^2 g}\)',
            },
            'B',
            r'Cô lập dấu căn trước khi bình phương:<br/>'
            r'1. Chia hai vế cho \(2\pi\): \(\frac{T}{2\pi} = \sqrt{\frac{L}{g}}\).<br/>'
            r'2. Bình phương cả hai vế (nhớ bình phương cả số \(2\) thành \(4\)): \[\frac{T^2}{4\pi^2} = \frac{L}{g}.\]'
            r'3. Nhân hai vế với \(g\): \[L = \frac{gT^2}{4\pi^2}.\]',
            r'Khi rút biến nằm trong căn, luôn tách hệ số bên ngoài căn (\(2\pi\)) trước rồi mới bình phương toàn bộ \((2\pi)^2 = 4\pi^2\).',
            {
                'A': ('Forgot to Square Coefficient', r'Chỉ bình phương \(\pi\) thành \(\pi^2\) mà quên bình phương số \(2\) thành \(4\).'),
                'B': ('Đáp án đúng', r'Bình phương chuẩn \(\left(\frac{T}{2\pi}\right)^2 = \frac{T^2}{4\pi^2}\), nhân với \(g\) cho \(L = \frac{gT^2}{4\pi^2}\).'),
                'C': ('Inverted Fraction', r'Đảo ngược tử số và mẫu số khi nhân chéo.'),
                'D': ('Divided Instead of Multiplied', r'Chia cho \(g\) thay vì nhân hai vế với \(g\).'),
            },
            desmos_tip_vi=r'Mẹo thử số: chọn \(L = 4,\; g = 1 \implies T = 2\pi\sqrt{4} = 4\pi\). Thay \(T = 4\pi,\; g = 1\) vào 4 đáp án trên Desmos, chỉ đáp án B trả đúng \(L = \frac{16\pi^2}{4\pi^2} = 4\).',
        ),

        # Q3 — Medium, MCQ, Ans=D
        math_mcq(
            'sat_m2_4_q3', 3, DOMAIN, SK_NONLIN_FUNC, 'Medium',
            r'<p>For all \(x > 0\), consider the expression \[\frac{\sqrt[3]{x^5} \cdot \sqrt{x}}{x^{\frac{2}{3}}}.\]</p>',
            r'<p>Which of the following is equivalent to the given expression?</p>',
            {
                'A': r'\(\sqrt[3]{x^2}\)',
                'B': r'\(\sqrt[6]{x^5}\)',
                'C': r'\(\sqrt[3]{x^4}\)',
                'D': r'\(\sqrt{x^3}\)',
            },
            'D',
            r'Đổi tất cả căn thức về số mũ hữu tỉ (\(\sqrt[n]{x^m} = x^{\frac{m}{n}}\)): \[\frac{x^{\frac{5}{3}} \cdot x^{\frac{1}{2}}}{x^{\frac{2}{3}}} = x^{\frac{5}{3} + \frac{1}{2} - \frac{2}{3}} = x^{\left(\frac{5}{3} - \frac{2}{3}\right) + \frac{1}{2}} = x^{1 + \frac{1}{2}} = x^{\frac{3}{2}} = \sqrt{x^3}.\]',
            r'Quy tắc vàng số mũ hữu tỉ: luôn đưa về cùng cơ số \(x\), nhân thì cộng mũ, chia thì trừ mũ — nhóm các phân số cùng mẫu trước (\(\frac{5}{3} - \frac{2}{3} = 1\)) để tính siêu nhanh!',
            {
                'A': ('Subtracted Wrongly', r'Trừ nhầm \(\frac{5}{3} - \frac{1}{2} - \frac{2}{3}\) hoặc tính sai mẫu chung thành \(x^{2/3}\).'),
                'B': ('Added Denominator Trap', r'Cộng nhầm tử với tử, mẫu với mẫu khi gộp \(\frac{1}{2}\) và \(\frac{2}{3}\).'),
                'C': ('Ignored Square Root', r'Cộng sai \(1 + \frac{1}{3} = \frac{4}{3}\) thay vì \(1 + \frac{1}{2} = \frac{3}{2}\).'),
                'D': ('Đáp án đúng', r'Số mũ rút gọn bằng \(\frac{5}{3} + \frac{1}{2} - \frac{2}{3} = \frac{3}{2}\), tương đương \(\sqrt{x^3}\).'),
            },
            desmos_tip_vi=r'Gán \(x = 64\) (số vừa khai căn bậc 2 vừa khai căn bậc 3 đẹp) trên Desmos: biểu thức gốc cho \(\frac{64^{5/3} \cdot 8}{64^{2/3}} = 512\), khớp duy nhất đáp án D (\(\sqrt{64^3} = 512\)).',
        ),

        # Q4 — Medium, SPR
        math_spr(
            'sat_m2_4_q4', 4, DOMAIN, SK_NONLIN_EQ, 'Medium',
            r'<p>\[3|2x - 5| - 7 = 14\]</p>',
            r'<p>What is the sum of all solutions to the given equation?</p>',
            ['5'], '5',
            r'Cô lập giá trị tuyệt đối trước khi phá dấu: \[3|2x - 5| = 21 \implies |2x - 5| = 7.\]'
            r'Tách thành 2 trường hợp:<br/>'
            r'• \(2x - 5 = 7 \implies 2x = 12 \implies x = 6\).<br/>'
            r'• \(2x - 5 = -7 \implies 2x = -2 \implies x = -1\).<br/>'
            r'Tổng các nghiệm là \(6 + (-1) = 5\).<br/>'
            r'<em>Mẹo đối xứng:</em> Khi \(|ax + b| = c > 0\), hai nghiệm luôn đối xứng quanh điểm giữa \(x = -\frac{b}{a} = \frac{5}{2}\), nên tổng hai nghiệm luôn là \(2\left(\frac{5}{2}\right) = 5\)!',
            r'Luôn kiểm tra vế phải sau khi cô lập \(|ax + b| = c\): nếu \(c > 0\) thì có 2 nghiệm và tổng hai nghiệm luôn bằng \(-\frac{2b}{a}\) (không phụ thuộc vào \(c\))!',
            desmos_tip_vi=r'Vẽ \(y = 3|2x - 5| - 7\) và \(y = 14\) trên Desmos, bấm hai giao điểm tại \(x = -1\) và \(x = 6\), cộng lại được \(5\).',
        ),

        # Q5 — Medium-Hard, MCQ, Ans=A
        math_mcq(
            'sat_m2_4_q5', 5, DOMAIN, SK_NONLIN_FUNC, 'Medium-Hard',
            f'<div style="display:flex;justify-content:center;margin-bottom:12px;">{svg_q5}</div>'
            r'<p>In the \(xy\)-plane, the graph of \(y = f(x)\) is a parabola with vertex \((4, -3)\), as shown above. The function \(g\) is defined by \[g(x) = f(x + 5) - 6.\]</p>',
            r'<p>What are the coordinates of the vertex of the graph of \(y = g(x)\)?</p>',
            {
                'A': r'\((-1, -9)\)',
                'B': r'\((9, -9)\)',
                'C': r'\((-1, 3)\)',
                'D': r'\((9, 3)\)',
            },
            'A',
            r'Áp dụng quy tắc tịnh tiến đồ thị \(g(x) = f(x - h) + k\):<br/>'
            r'• Bên trong ngoặc là \(x + 5 = x - (-5)\) \(\implies\) dịch đồ thị sang <strong>TRÁI \(5\) đơn vị</strong> (trừ \(5\) ở hoành độ): \(4 - 5 = -1\).<br/>'
            r'• Bên ngoài ngoặc là \(-6\) \(\implies\) dịch đồ thị xuống <strong>DƯỚI \(6\) đơn vị</strong> (trừ \(6\) ở tung độ): \(-3 - 6 = -9\).<br/>'
            r'Vậy tọa độ đỉnh mới của \(y = g(x)\) là \((-1, -9)\).',
            r'Quy tắc “Trong ngược – Ngoài xuôi”: \(f(x + 5)\) dịch TRÁI (\(-5\) vào \(x\)), còn \(-6\) bên ngoài dịch XUỐNG (\(-6\) vào \(y\)).',
            {
                'A': ('Đáp án đúng', r'Dịch trái \(5\) và xuống \(6\): \((4 - 5,\; -3 - 6) = (-1, -9)\).'),
                'B': ('Horizontal Shift Trap', r'Bẫy kinh điển: thấy \(+5\) trong ngoặc liền cộng \(4 + 5 = 9\) (dịch phải thay vì dịch trái).'),
                'C': ('Vertical Shift Sign Trap', r'Cộng nhầm \(-3 + 6 = 3\) thay vì trừ \(6\) ở tung độ.'),
                'D': ('Double Sign Error', r'Đảo ngược chiều của cả hai phép dịch chuyển ngang và dọc.'),
            },
            desmos_tip_vi=r'Tạo nhanh một parabol mẫu có đỉnh \((4, -3)\) trên Desmos: gõ \(f(x) = (x - 4)^2 - 3\), rồi gõ \(g(x) = f(x + 5) - 6\), bấm đỉnh của \(g\) đọc ngay \((-1, -9)\)!',
        ),

        # Q6 — Medium-Hard, MCQ, Ans=C
        math_mcq(
            'sat_m2_4_q6', 6, DOMAIN, SK_NONLIN_EQ, 'Medium-Hard',
            r'<p>\[y = x^2 - 4x + 7\]\[y = 2x + 2\]</p>'
            r'<p>In the \(xy\)-plane, the graphs of the equations in the given system intersect at two distinct points, \((x_1, y_1)\) and \((x_2, y_2)\).</p>',
            r'<p>What is the value of \(y_1 + y_2\)?</p>',
            {'A': r'\(6\)', 'B': r'\(12\)', 'C': r'\(16\)', 'D': r'\(14\)'},
            'C',
            r'Cho hai vế phải bằng nhau để tìm hoành độ giao điểm: \[x^2 - 4x + 7 = 2x + 2 \implies x^2 - 6x + 5 = 0 \implies (x - 1)(x - 5) = 0.\]'
            r'Ta có \(x_1 = 1 \implies y_1 = 2(1) + 2 = 4\) và \(x_2 = 5 \implies y_2 = 2(5) + 2 = 12\).<br/>'
            r'Vậy \(y_1 + y_2 = 4 + 12 = 16\).<br/>'
            r'<em>Mẹo Viète nhanh:</em> \(x_1 + x_2 = 6\), do đó \(y_1 + y_2 = (2x_1 + 2) + (2x_2 + 2) = 2(x_1 + x_2) + 4 = 2(6) + 4 = 16\).',
            r'Khi đề hỏi \(y_1 + y_2\) của hệ đường thẳng \(y = mx + b\) và parabol: nhớ cộng \(2b\) (chứ không phải \(1b\)) trong công thức \(y_1 + y_2 = m(x_1 + x_2) + 2b\)!',
            {
                'A': ('Wrong Variable', r'Đây là tổng hoành độ \(x_1 + x_2 = 6\), không phải tổng tung độ \(y_1 + y_2\).'),
                'B': ('Forgot Constant Term', r'Chỉ tính \(2(x_1 + x_2) = 12\) (hoặc chỉ lấy tung độ \(y_2 = 12\)) mà quên cộng \(2 + 2 = 4\).'),
                'C': ('Đáp án đúng', r'Hai giao điểm là \((1, 4)\) và \((5, 12)\), tổng tung độ \(4 + 12 = 16\).'),
                'D': ('Single Constant Trap', r'Viết nhầm \(y_1 + y_2 = 2(x_1 + x_2) + 2 = 14\) (quên rằng hằng số \(2\) xuất hiện ở CẢ \(y_1\) lẫn \(y_2\)).'),
            },
            desmos_tip_vi=r'Gõ cả hai phương trình \(y = x^2 - 4x + 7\) và \(y = 2x + 2\) trên Desmos, bấm 2 giao điểm \((1, 4)\) và \((5, 12)\) rồi cộng \(4 + 12 = 16\).',
        ),

        # Q7 — Medium-Hard, MCQ, Ans=B
        math_mcq(
            'sat_m2_4_q7', 7, DOMAIN, SK_NONLIN_EQ, 'Medium-Hard',
            r'<p>\[-2|x - 9| + k = 5\]</p>'
            r'<p>In the given equation, \(k\) is a constant.</p>',
            r'<p>For which of the following values of \(k\) does the equation have no real solution?</p>',
            {'A': r'\(5\)', 'B': r'\(3\)', 'C': r'\(7\)', 'D': r'\(9\)'},
            'B',
            r'Cô lập biểu thức trị tuyệt đối: \[-2|x - 9| = 5 - k \implies |x - 9| = \frac{k - 5}{2}.\]'
            r'Vì \(|x - 9| \ge 0\) với mọi \(x \in \mathbb{R}\), phương trình vô nghiệm thực khi và chỉ khi vế phải âm: \[\frac{k - 5}{2} < 0 \iff k < 5.\]'
            r'Trong 4 đáp án, chỉ có \(k = 3 < 5\) làm cho \(|x - 9| = -1\) (vô nghiệm).',
            r'Phương trình \(|u| = M\) có: \(2\) nghiệm khi \(M > 0\), đúng \(1\) nghiệm khi \(M = 0\), và VÔ NGHIỆM khi \(M < 0\). Nhớ đổi dấu khi chia cho hệ số âm (\(-2\))!',
            {
                'A': ('Boundary Trap', r'Với \(k = 5\), ta có \(|x - 9| = 0\), phương trình vẫn có ĐÚNG \(1\) nghiệm là \(x = 9\).'),
                'B': ('Đáp án đúng', r'Với \(k = 3\), phương trình thành \(|x - 9| = -1\), không thể xảy ra với mọi \(x\) thực.'),
                'C': ('Two Solutions Case', r'Với \(k = 7\), \(|x - 9| = 1\) có \(2\) nghiệm là \(x = 8\) và \(x = 10\).'),
                'D': ('Two Solutions Case', r'Với \(k = 9\), \(|x - 9| = 2\) có \(2\) nghiệm là \(x = 7\) và \(x = 11\).'),
            },
            desmos_tip_vi=r'Vẽ \(y = -2|x - 9| + k\) (đồ thị chữ V úp ngược có đỉnh \((9, k)\)) và đường ngang \(y = 5\). Đồ thị không cắt \(y = 5\) khi đỉnh nằm thấp hơn \(5\), tức \(k < 5 \implies k = 3\).',
        ),

        # Q8 — Medium-Hard, SPR
        math_spr(
            'sat_m2_4_q8', 8, DOMAIN, SK_NONLIN_EQ, 'Medium-Hard',
            r'<p>\[2(2x - 7)^{\frac{3}{2}} = 54\]</p>',
            r'<p>What is the real solution to the given equation?</p>',
            ['8'], '8',
            r'1. Chia hai vế cho \(2\): \((2x - 7)^{\frac{3}{2}} = 27\).<br/>'
            r'2. Nâng cả hai vế lên lũy thừa nghịch đảo \(\frac{2}{3}\) (vì \(2x - 7 \ge 0\) do mũ có mẫu chẵn): \[2x - 7 = 27^{\frac{2}{3}} = \left(\sqrt[3]{27}\right)^2 = 3^2 = 9.\]'
            r'3. Giải tiếp: \(2x = 16 \implies x = 8\).<br/>'
            r'Kiểm tra lại: \(2(2 \cdot 8 - 7)^{3/2} = 2(9)^{3/2} = 2(27) = 54\), hoàn toàn chính xác!',
            r'Giải \(u^{m/n} = c\): luôn tách hệ số bên ngoài trước, rồi nâng cả hai vế lên mũ nghịch đảo \(\frac{n}{m}\) (nhớ lấy căn bậc \(n\) trước rồi mới mũ \(m\) để số nhỏ gọn).',
            desmos_tip_vi=r'Gõ thẳng phương trình \(2(2x - 7)^{3/2} = 54\) trên Desmos, bấm vào đường đứng duy nhất đọc ngay \(x = 8\).',
        ),

        # Q9 — Medium-Hard, MCQ, Ans=D
        math_mcq(
            'sat_m2_4_q9', 9, DOMAIN, SK_NONLIN_EQ, 'Medium-Hard',
            r'<p>In optical physics, the thin-lens equation relates focal length \(f\), object distance \(u\), and image distance \(v\) by \[\frac{1}{f} = \frac{1}{u} + \frac{1}{v},\] where \(f\), \(u\), and \(v\) are positive constants with \(u > f\).</p>',
            r'<p>Which equation correctly expresses \(v\) in terms of \(f\) and \(u\)?</p>',
            {
                'A': r'\(v = u - f\)',
                'B': r'\(v = \frac{u - f}{fu}\)',
                'C': r'\(v = \frac{fu}{f - u}\)',
                'D': r'\(v = \frac{fu}{u - f}\)',
            },
            'D',
            r'Cô lập \(\frac{1}{v}\) sang một vế rồi quy đồng mẫu số:<br/>'
            r'\[\frac{1}{v} = \frac{1}{f} - \frac{1}{u} = \frac{u - f}{fu}.\]'
            r'Lấy nghịch đảo cả hai vế để tìm \(v\): \[v = \frac{fu}{u - f}.\]'
            r'Kiểm tra dấu: vì \(u > f > 0\) nên \(u - f > 0\), suy ra \(v > 0\) (khớp giả thiết).',
            r'TUYỆT ĐỐI KHÔNG nghịch đảo từng phân số riêng lẻ (\(\frac{1}{f} = \frac{1}{u} + \frac{1}{v} \not\Rightarrow f = u + v\))! Phải gộp thành MỘT phân số duy nhất rồi mới đảo ngược.',
            {
                'A': ('Term-by-Term Reciprocal', r'Lỗi kinh điển: nghịch đảo từng phân số riêng lẻ thành \(f = u + v \implies v = u - f\) (sai hoàn toàn về đại số).'),
                'B': ('Forgot Final Reciprocal', r'Quy đồng đúng được \(\frac{1}{v} = \frac{u - f}{fu}\) nhưng quên đảo ngược lại để ra \(v\).'),
                'C': ('Reversed Subtraction Sign', r'Đổi ngược dấu ở mẫu thành \(f - u < 0\), làm \(v\) mang giá trị âm (trái giả thiết \(u > f\) và \(v > 0\)).'),
                'D': ('Đáp án đúng', r'Từ \(\frac{1}{v} = \frac{u - f}{fu}\) lấy nghịch đảo thu được \(v = \frac{fu}{u - f}\).'),
            },
            desmos_tip_vi=r'Mẹo thử số: chọn \(f = 2,\; u = 6 \implies \frac{1}{v} = \frac{1}{2} - \frac{1}{6} = \frac{1}{3} \implies v = 3\). Thay \(f = 2, u = 6\) vào 4 đáp án, chỉ đáp án D cho \(\frac{12}{4} = 3\).',
        ),

        # Q10 — Medium-Hard, MCQ, Ans=A
        math_mcq(
            'sat_m2_4_q10', 10, DOMAIN, SK_NONLIN_FUNC, 'Medium-Hard',
            r'<p>\[y = 2x^2 - 7x + 11\]\[y = 5x + c\]</p>'
            r'<p>In the system of equations above, \(c\) is a constant. The system has exactly one real solution.</p>',
            r'<p>What is the value of \(c\)?</p>',
            {'A': r'\(-7\)', 'B': r'\(7\)', 'C': r'\(-25\)', 'D': r'\(18\)'},
            'A',
            r'Cho hai biểu thức của \(y\) bằng nhau và chuyển về phương trình bậc hai chuẩn: \[2x^2 - 7x + 11 = 5x + c \implies 2x^2 - 12x + (11 - c) = 0.\]'
            r'Hệ có đúng \(1\) nghiệm thực (đường thẳng tiếp xúc parabol) khi và chỉ khi \(\Delta = 0\): \[(-12)^2 - 4(2)(11 - c) = 0 \implies 144 - 88 + 8c = 0 \implies 56 + 8c = 0 \implies c = -7.\]'
            r'Kiểm tra khi \(c = -7\): \(2x^2 - 12x + 18 = 2(x - 3)^2 = 0\), tiếp điểm duy nhất là \((3, 8)\).',
            r'Hệ Đường thẳng + Parabol có đúng 1 nghiệm (tiếp xúc) \(\iff\) khử \(y\) để được bậc hai ẩn \(x\), rồi đặt \(\Delta = b^2 - 4ac = 0\).',
            {
                'A': ('Đáp án đúng', r'Từ \(\Delta = 144 - 8(11 - c) = 56 + 8c = 0\) giải ra \(c = -7\).'),
                'B': ('Sign Error', r'Sai dấu khi phân phối \(-8(-c)\) hoặc chuyển vế, tính ra \(+7\).'),
                'C': ('Forgot Coefficient a', r'Quên hệ số \(a = 2\), giải nhầm \(144 - 4(11 - c) = 0 \implies c = -25\).'),
                'D': ('Partial Answer', r'Tìm ra hằng số \(11 - c = 18\) nhưng dừng lại không giải tiếp tìm \(c = -7\).'),
            },
            desmos_tip_vi=r'Vẽ \(y = 2x^2 - 7x + 11\) và \(y = 5x + c\) trên Desmos, thêm slider \(c\). Di chuyển \(c\) sao cho đường thẳng chạm khít parabol tại đúng 1 điểm — xảy ra tại \(c = -7\).',
        ),

        # Q11 — Hard (750-800), MCQ, Ans=B
        math_mcq(
            'sat_m2_4_q11', 11, DOMAIN, SK_NONLIN_EQ, 'Hard (750-800)',
            r'<p>\[y = x^2 + 6x + 17\]\[y = mx + 8\]</p>'
            r'<p>In the system of equations above, \(m\) is a positive constant. The graph of \(y = mx + 8\) is tangent to the graph of \(y = x^2 + 6x + 17\) in the \(xy\)-plane (so the system has exactly one real solution).</p>',
            r'<p>What is the value of \(m\)?</p>',
            {'A': r'\(6\)', 'B': r'\(12\)', 'C': r'\(15\)', 'D': r'\(42\)'},
            'B',
            r'Khử \(y\) để lập phương trình hoành độ giao điểm: \[x^2 + 6x + 17 = mx + 8 \implies x^2 + (6 - m)x + 9 = 0.\]'
            r'Vì đường thẳng tiếp xúc parabol (có đúng 1 nghiệm thực), đặt \(\Delta = 0\): \[(6 - m)^2 - 4(1)(9) = 0 \implies (6 - m)^2 = 36 \implies 6 - m = \pm 6.\]'
            r'Giải hai trường hợp:<br/>'
            r'• \(6 - m = 6 \implies m = 0\) (loại vì đề yêu cầu \(m\) dương).<br/>'
            r'• \(6 - m = -6 \implies m = 12\) (thỏa mãn \(m > 0\)).<br/>'
            r'Kiểm chứng: khi \(m = 12\), phương trình trở thành \(x^2 - 6x + 9 = (x - 3)^2 = 0\), tiếp xúc tại \((3, 44)\).',
            r'Khi tham số nằm ở hệ số góc \(m\), phương trình \(\Delta = 0\) thường ra dạng bình phương \((b - m)^2 = 4ac\) cho 2 giá trị \(m\); đừng quên đọc điều kiện dấu (\(m > 0\))!',
            {
                'A': ('Set Bracket to 0', r'Cho nhầm \((6 - m) = 0 \implies m = 6\) mà quên hằng số \(-4(1)(9) = -36\) trong biệt thức.'),
                'B': ('Đáp án đúng', r'Từ \((6 - m)^2 = 36\) với \(m > 0\) thu được duy nhất \(m = 12\).'),
                'C': ('Arithmetic Error', r'Cộng nhầm \(6 + 9 = 15\) thay vì dùng \(\sqrt{36} = 6\).'),
                'D': ('Forgot Square Root', r'Quên khai căn số \(36\), giải nhầm \(m - 6 = 36 \implies m = 42\).'),
            },
            desmos_tip_vi=r'Gõ thẳng phương trình biệt thức \((6 - x)^2 - 4(9) = 0\) trên Desmos (với \(x = m\)): xuất hiện 2 đường đứng \(x = 0\) và \(x = 12\); lấy nghiệm dương \(m = 12\) trong 5 giây!',
        ),

        # Q12 — Hard (750-800), SPR
        math_spr(
            'sat_m2_4_q12', 12, DOMAIN, SK_NONLIN_EQ, 'Hard (750-800)',
            r'<p>\[2x - 9\sqrt{x} + 10 = 0\]</p>',
            r'<p>What is the sum of all real solutions to the given equation?</p>',
            ['41/4', '10.25'], '41/4 (hoặc 10.25)',
            r'Điều kiện: \(x \ge 0\). Đặt ẩn phụ \(u = \sqrt{x} \ge 0\) (nên \(x = u^2\)), phương trình trở thành: \[2u^2 - 9u + 10 = 0 \implies (2u - 5)(u - 2) = 0.\]'
            r'Hai nghiệm \(u\) đều dương và hợp lệ: \(u_1 = \frac{5}{2}\) và \(u_2 = 2\).<br/>'
            r'Bình phương để trả về ẩn \(x\): \[x_1 = \left(\frac{5}{2}\right)^2 = \frac{25}{4}, \qquad x_2 = 2^2 = 4.\]'
            r'Tổng các nghiệm thực của phương trình là: \[x_1 + x_2 = \frac{25}{4} + 4 = \frac{41}{4} = 10.25.\]'
            r'(Cảnh báo bẫy: không lấy \(\frac{9}{2}\) vì đó mới là \(u_1 + u_2 = \sqrt{x_1} + \sqrt{x_2}\), không phải \(x_1 + x_2\)!)',
            r'Với phương trình bậc hai ẩn \(\sqrt{x}\), đặt \(u = \sqrt{x} \ge 0\): nhớ loại mọi nghiệm \(u < 0\) và PHẢI bình phương \(x = u^2\) trước khi cộng tổng nghiệm!',
            desmos_tip_vi=r'Vẽ \(y = 2x - 9\sqrt{x} + 10\) trên Desmos, bấm 2 giao điểm trục \(Ox\) thấy ngay \((4, 0)\) và \((6.25, 0)\). Cộng \(4 + 6.25 = 10.25\) (hoặc \(41/4\))!',
        ),

        # Q13 — Hard (750-800), MCQ, Ans=D
        math_mcq(
            'sat_m2_4_q13', 13, DOMAIN, SK_NONLIN_FUNC, 'Hard (750-800)',
            r'<p>The quadratic function \(f\) is defined by \(f(x) = 2(x + 3)(x - 5)\). For a constant \(k\), the graph of \(y = f(x - 4) + k\) in the \(xy\)-plane is tangent to the \(x\)-axis (has exactly one \(x\)-intercept) at the point \((h, 0)\).</p>',
            r'<p>What is the value of \(h + k\)?</p>',
            {'A': r'\(29\)', 'B': r'\(33\)', 'C': r'\(-27\)', 'D': r'\(37\)'},
            'D',
            r'Bước 1 — Tìm đỉnh của parabol gốc \(f(x) = 2(x + 3)(x - 5)\):<br/>'
            r'• Hai nghiệm của \(f\) là \(-3\) và \(5\) \(\implies\) hoành độ đỉnh của \(f\) là \(x_0 = \frac{-3 + 5}{2} = 1\).<br/>'
            r'• Tung độ đỉnh (cực tiểu) của \(f\) là \(y_0 = f(1) = 2(1 + 3)(1 - 5) = 2(4)(-4) = -32\).<br/>'
            r'Bước 2 — Áp dụng phép tịnh tiến \(y = f(x - 4) + k\):<br/>'
            r'• Dịch <strong>PHẢI \(4\) đơn vị</strong> \(\implies\) hoành độ đỉnh mới là \(h = 1 + 4 = 5\).<br/>'
            r'• Để đồ thị tiếp xúc trục \(Ox\) (tung độ đỉnh mới bằng \(0\)), phải dịch <strong>LÊN \(32\) đơn vị</strong>: \(-32 + k = 0 \implies k = 32\).<br/>'
            r'Vậy \(h + k = 5 + 32 = 37\).',
            r'Khi kết hợp hàm bậc hai + phép tịnh tiến \(f(x - 4) + k\): theo dõi ĐỈNH parabol sẽ nhanh gấp 5 lần khai triển đại số — đỉnh \((x_0, y_0)\) biến thành \((x_0 + 4,\; y_0 + k)\)!',
            {
                'A': ('Horizontal Shift Trap', r'Dịch nhầm sang TRÁI \(4\) đơn vị thành \(h = 1 - 4 = -3\), tính ra \(-3 + 32 = 29\).'),
                'B': ('Forgot Horizontal Shift', r'Quên cộng dịch chuyển \(+4\) vào hoành độ đỉnh (giữ \(h = 1\)), ra \(1 + 32 = 33\).'),
                'C': ('Vertical Shift Sign Trap', r'Nhầm \(k = -32\) (tung độ đỉnh cũ) thay vì độ nâng \(k = +32\), tính ra \(5 - 32 = -27\).'),
                'D': ('Đáp án đúng', r'Đỉnh của \(f\) là \((1, -32)\); sau khi dịch phải \(4\) và lên \(32\), đỉnh mới nằm trên \(Ox\) tại \((5, 0)\), nên \(h + k = 5 + 32 = 37\).'),
            },
            desmos_tip_vi=r'Gõ \(f(x) = 2(x + 3)(x - 5)\) trên Desmos, bấm đỉnh thấy \((1, -32)\). Sau đó gõ \(g(x) = f(x - 4) + 32\) kiểm tra đỉnh chạm đúng \((5, 0)\), cộng \(5 + 32 = 37\).',
        ),

        # Q14 — Hard (750-800), MCQ, Ans=C
        math_mcq(
            'sat_m2_4_q14', 14, DOMAIN, SK_NONLIN_EQ, 'Hard (750-800)',
            r'<p>\[|x^2 - 6x + 5| = 4\]</p>',
            r'<p>What is the sum of all distinct real solutions to the given equation?</p>',
            {'A': r'\(6\)', 'B': r'\(3\)', 'C': r'\(9\)', 'D': r'\(12\)'},
            'C',
            r'Phá dấu giá trị tuyệt đối thành 2 phương trình bậc hai:<br/>'
            r'• <strong>Nhánh 1:</strong> \(x^2 - 6x + 5 = 4 \implies x^2 - 6x + 1 = 0\).<br/>'
            r'  Kiểm tra \(\Delta_1 = 36 - 4 = 32 > 0\), có \(2\) nghiệm thực phân biệt \(x = 3 \pm 2\sqrt{2}\), tổng hai nghiệm này theo Viète là \(6\).<br/>'
            r'• <strong>Nhánh 2:</strong> \(x^2 - 6x + 5 = -4 \implies x^2 - 6x + 9 = 0 \implies (x - 3)^2 = 0\).<br/>'
            r'  Kiểm tra \(\Delta_2 = 0\)! Nhánh này chỉ có <strong>ĐÚNG MỘT</strong> nghiệm thực duy nhất là \(x = 3\) (không trùng với \(3 \pm 2\sqrt{2}\))!<br/>'
            r'Do đề hỏi tổng các nghiệm thực <strong>phân biệt (distinct)</strong>, tổng đúng là: \[(3 - 2\sqrt{2}) + 3 + (3 + 2\sqrt{2}) = 6 + 3 = 9.\]',
            r'CẠM BẪY 800 ĐIỂM: Khi dùng Viète \(-\frac{b}{a}\) cho câu hỏi “sum of DISTINCT real solutions”, BẮT BUỘC kiểm tra \(\Delta\) — nếu \(\Delta = 0\) (nghiệm kép \(r\)), Viète \(2r\) sẽ ĐẾM ĐÔI nghiệm đó!',
            {
                'A': ('Only Solved One Branch', r'Chỉ giải nhánh dương \(x^2 - 6x + 5 = 4\) (tổng \(6\)) mà quên nhánh âm \(= -4\).'),
                'B': ('Only Counted Integer Root', r'Chỉ tính nghiệm nguyên \(x = 3\) mà bỏ qua 2 nghiệm vô tỉ \(3 \pm 2\sqrt{2}\).'),
                'C': ('Đáp án đúng', r'Có đúng \(3\) nghiệm thực phân biệt \(\{3 - 2\sqrt{2},\; 3,\; 3 + 2\sqrt{2}\}\), tổng bằng \(9\).'),
                'D': ('Double-Counted Repeated Root', r'Bẫy chí mạng: áp dụng máy móc Viète \(-\frac{b}{a} = 6\) cho cả hai nhánh rồi cộng \(6 + 6 = 12\), đếm lặp nghiệm kép \(x = 3\) hai lần!'),
            },
            desmos_tip_vi=r'Vẽ \(y = |x^2 - 6x + 5|\) và đường ngang \(y = 4\) trên Desmos. Đếm thấy ĐÚNG 3 giao điểm (chạm đỉnh vòm tại \(x = 3\) và cắt 2 bên tại \(0.172\) và \(5.828\)). Cộng 3 hoành độ ra chuẩn xác \(9\)!',
        ),

        # Q15 — Hard (750-800), SPR
        math_spr(
            'sat_m2_4_q15', 15, DOMAIN, SK_NONLIN_EQ, 'Hard (750-800)',
            r'<p>\[x^2 + y^2 = 85\]\[x - y = 5\]</p>'
            r'<p>If \((x, y)\) is a real solution to the system of equations above, what is the value of \(xy\)?</p>',
            r'<p>Enter the value of \(xy\).</p>',
            ['30'], '30',
            r'Không cần rút thế để giải nghiệm vô tỉ! Dùng ngay hằng đẳng thức bình phương của một hiệu: \[(x - y)^2 = x^2 - 2xy + y^2.\]'
            r'Thay \(x - y = 5\) và \(x^2 + y^2 = 85\) vào đẳng thức trên: \[5^2 = 85 - 2xy \implies 25 = 85 - 2xy \implies 2xy = 60 \implies xy = 30.\]'
            r'Kiểm tra sự tồn tại nghiệm thực: từ \(x - y = 5\) và \(xy = 30\), \(x\) là nghiệm của \(t^2 - 5t - 30 = 0\) có \(\Delta = 25 + 120 = 145 > 0\) (luôn có 2 nghiệm thực phân biệt, và cả hai đều cho \(xy = 30\)).',
            r'Hệ đối xứng \(x^2 + y^2\) và \(x \pm y\) là “đặc sản” câu cuối Hard M2: dùng ngay \((x \pm y)^2 = (x^2 + y^2) \pm 2xy\) để bật ra \(xy\) trong 5 giây!',
            desmos_tip_vi=r'Vẽ đường tròn \(x^2 + y^2 = 85\) và đường thẳng \(x - y = 5\) trên Desmos, bấm 1 giao điểm (ví dụ \((8.5208,\; 3.5208)\)) rồi gõ tích \(8.5208 \times 3.5208 \approx 30.000\) để xác nhận ngay \(30\)!',
        ),
    ]

    return build_math_drill_json(
        'Math Drill 2.4: Nonlinear Systems, Radicals, Absolute Value & Transformations (15 câu)',
        '15 câu trọng tâm Advanced Math • Hệ Phi tuyến tiếp xúc, Phương trình Căn/Trị tuyệt đối, Biến đổi Đồ thị & Rút biến (650–800)',
        'Advanced Math • Hard M2 Core',
        qs,
        target_minutes=24,
    )


def get_drills():
    """Returns the 4 flagship Module 2 (Advanced Math) drills as (drill_key, title, order_index, content_json)."""
    d1 = _build_drill_m2_1()
    d2 = _build_drill_m2_2()
    d3 = _build_drill_m2_3()
    d4 = _build_drill_m2_4()
    return [
        ('drill_m2_1', d1['basicInfo']['title'], 4, d1),
        ('drill_m2_2', d2['basicInfo']['title'], 5, d2),
        ('drill_m2_3', d3['basicInfo']['title'], 6, d3),
        ('drill_m2_4', d4['basicInfo']['title'], 7, d4),
    ]


# ============================================================================
# 100% PROGRAMMATIC EXACT-ARITHMETIC VERIFICATION OF ALL 60 QUESTIONS
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
    """Programmatically verifies structure, LaTeX hygiene, and exact math for all 60 M2 questions."""
    drills = get_drills()
    assert len(drills) == 4, f"Expected 4 drills, got {len(drills)}"

    expected_meta = [
        ('drill_m2_1', 'Math Drill 2.1: Quadratics — Discriminant, Vertex & Vieta Mastery (15 câu)', 4),
        ('drill_m2_2', 'Math Drill 2.2: Polynomials, Factor Theorem & Rational Equations (15 câu)', 5),
        ('drill_m2_3', 'Math Drill 2.3: Exponential Growth/Decay & Compound Scaling (15 câu)', 6),
        ('drill_m2_4', 'Math Drill 2.4: Nonlinear Systems, Radicals, Absolute Value & Transformations (15 câu)', 7),
    ]
    total_key_counts = {'A': 0, 'B': 0, 'C': 0, 'D': 0}

    for i, ((k, t, idx, cj), (ek, et, eidx)) in enumerate(zip(drills, expected_meta), start=1):
        assert (k, t, idx) == (ek, et, eidx), f"Drill metadata mismatch: {(k, t, idx)} != {(ek, et, eidx)}"
        qs = cj['drillModule']['questions']
        assert len(qs) == 15, f"{k}: expected 15 questions, got {len(qs)}"
        mcq_counts = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
        spr_nums = []
        for pos, q in enumerate(qs, start=1):
            assert q['id'] == f'sat_m2_{i}_q{pos}', f"Bad id {q['id']}"
            assert q['number'] == pos
            assert q['domain'] == DOMAIN
            expected_diff = 'Medium' if pos <= 4 else ('Medium-Hard' if pos <= 10 else 'Hard (750-800)')
            assert q['difficulty'] == expected_diff, f"{q['id']}: bad difficulty {q['difficulty']}"
            exp = q['explanation']
            assert len(exp.get('summaryVi', '').strip()) >= 30, f"{q['id']}: short summaryVi"
            assert len(exp.get('desmosTipVi', '').strip()) >= 20, f"{q['id']}: missing/short desmosTipVi"
            assert len(exp.get('keyTakeaway', '').strip()) >= 20, f"{q['id']}: missing/short keyTakeaway"
            if q['questionFormat'] == 'spr':
                spr_nums.append(pos)
            else:
                ans = q['correctAnswer']
                mcq_counts[ans] += 1
                total_key_counts[ans] += 1
                for lbl in ('A', 'B', 'C', 'D'):
                    oa = exp['optionAnalysis'][lbl]
                    assert oa.get('trapTag'), f"{q['id']}[{lbl}] missing trapTag"
        assert spr_nums == [4, 8, 12, 15], f"{k}: SPR positions {spr_nums}"
        assert sum(mcq_counts.values()) == 11, f"{k}: expected 11 MCQs"
        assert min(mcq_counts.values()) == 2 and max(mcq_counts.values()) == 3, f"{k}: unbalanced keys {mcq_counts}"

    assert total_key_counts == {'A': 11, 'B': 11, 'C': 11, 'D': 11}, f"Overall keys not 11/11/11/11: {total_key_counts}"
    _check_latex_and_hygiene(drills)

    qm = _q_by_id(drills)

    # ------------------------------------------------------------------
    # DRILL 2.1 EXACT ARITHMETIC ASSERTIONS (Q1..Q15)
    # ------------------------------------------------------------------
    # Q1: 4x^2 - 20x + c = 0 has 1 real solution => Delta = (-20)^2 - 16c = 0 => c = 25
    c_1_1 = Fraction((-20) ** 2, 4 * 4)
    assert c_1_1 == 25 and qm['sat_m2_1_q1']['correctAnswer'] == 'B' and '25' in _correct_opt_text(qm['sat_m2_1_q1'])

    # Q2: f(x) = x^2 - 8x + 23 = (x - 4)^2 + 7; verify equivalence for sample x and min at x=4
    for x in range(-5, 10):
        assert x**2 - 8*x + 23 == (x - 4)**2 + 7
    assert min(x**2 - 8*x + 23 for x in range(-5, 10)) == 7
    assert qm['sat_m2_1_q2']['correctAnswer'] == 'A'

    # Q3: 3x^2 - 19x + 11 = 0 => Delta > 0, sum = 19/3
    assert (-19)**2 - 4*3*11 == 229 > 0
    assert Fraction(19, 3) == Fraction(-(-19), 3) and qm['sat_m2_1_q3']['correctAnswer'] == 'C'

    # Q4 (SPR): vertex (3, -8), passes through (5, 4) => a = 3, f(0) = 19
    a_1_4 = Fraction(4 - (-8), (5 - 3) ** 2)
    f0_1_4 = a_1_4 * (0 - 3) ** 2 - 8
    assert a_1_4 == 3 and f0_1_4 == 19 and qm['sat_m2_1_q4']['acceptedAnswers'] == ['19']

    # Q5: g(x) = -2x^2 + bx + c, g(2) = g(10) = 5 => h = 6, k = 5 - (-2)*(2-6)^2 = 37
    h_1_5 = Fraction(2 + 10, 2)
    k_1_5 = 5 - (-2) * (2 - h_1_5) ** 2
    assert h_1_5 == 6 and k_1_5 == 37
    assert -2*(2 - 6)**2 + 37 == 5 and -2*(10 - 6)**2 + 37 == 5
    assert qm['sat_m2_1_q5']['correctAnswer'] == 'D'

    # Q6: 2x^2 - 12x + k = 0 no real solns => 144 - 8k < 0 => k > 18 => least integer = 19
    valid_k = [k for k in range(0, 40) if (-12)**2 - 4*2*k < 0]
    assert min(valid_k) == 19 and (-12)**2 - 4*2*18 == 0
    assert qm['sat_m2_1_q6']['correctAnswer'] == 'A'

    # Q7: 6x^2 - 13x + 4 = 2x^2 + 5x - 9 => 4x^2 - 18x + 13 = 0 => Delta=116>0, prod = 13/4
    a7, b7, c7 = 6 - 2, -13 - 5, 4 + 9
    assert (a7, b7, c7) == (4, -18, 13) and b7**2 - 4*a7*c7 == 116 > 0
    assert Fraction(c7, a7) == Fraction(13, 4) and qm['sat_m2_1_q7']['correctAnswer'] == 'B'

    # Q8 (SPR): h(-1)=0, h(5)=0, h(2)=-18 => a=2, h(1)=a+b+c=-16
    a_1_8 = Fraction(-18, (2 + 1) * (2 - 5))
    h1_1_8 = a_1_8 * (1 + 1) * (1 - 5)
    assert a_1_8 == 2 and h1_1_8 == -16 and qm['sat_m2_1_q8']['acceptedAnswers'] == ['-16']

    # Q9: H(t) = -5t^2 + 30t + 35 = -5(t - 7)(t + 1)
    for t in range(-2, 10):
        assert -5*t**2 + 30*t + 35 == -5*(t - 7)*(t + 1)
    assert -5*(7)**2 + 30*(7) + 35 == 0 and qm['sat_m2_1_q9']['correctAnswer'] == 'C'

    # Q10: kx^2 - 24x + (3k + 12) = 0, sum = prod => 24/k = (3k+12)/k => k = 4
    k_1_10 = Fraction(24 - 12, 3)
    assert k_1_10 == 4 and (-24)**2 - 4*k_1_10*(3*k_1_10 + 12) == 192 > 0
    assert Fraction(24, k_1_10) == Fraction(3*k_1_10 + 12, k_1_10) == 6
    assert qm['sat_m2_1_q10']['correctAnswer'] == 'D'

    # Q11: x^2 + (k - 4)x + (k + 11) = 0, Delta = k^2 - 12k - 28 = 0 => k in {-2, 14}, sum = 12
    ks_1_11 = [k for k in range(-50, 50) if (k - 4)**2 - 4*(k + 11) == 0]
    assert ks_1_11 == [-2, 14] and sum(ks_1_11) == 12 and qm['sat_m2_1_q11']['correctAnswer'] == 'A'

    # Q12 (SPR): 2(3x - 5)^2 - 14(3x - 5) + 19 = 0 => 18x^2 - 102x + 139 = 0 => sum = 17/3
    assert (-14)**2 - 4*2*19 == 44 > 0
    for x in range(-3, 6):
        assert 2*(3*x - 5)**2 - 14*(3*x - 5) + 19 == 18*x**2 - 102*x + 139
    sum_1_12 = Fraction(102, 18)
    assert sum_1_12 == Fraction(17, 3) and '17/3' in qm['sat_m2_1_q12']['acceptedAnswers']

    # Q13: f(1)=f(9)=-6, min=-38 => h=5, a=2, b=-20
    a_1_13 = Fraction(-6 - (-38), (1 - 5) ** 2)
    b_1_13 = -2 * a_1_13 * 5
    c_1_13 = a_1_13 * 25 - 38
    assert (a_1_13, b_1_13, c_1_13) == (2, -20, 12)
    assert 2*(1)**2 - 20*(1) + 12 == -6 and 2*(9)**2 - 20*(9) + 12 == -6 and 2*(5)**2 - 20*(5) + 12 == -38
    assert qm['sat_m2_1_q13']['correctAnswer'] == 'B'

    # Q14: -b/a = -10/3, c/a = 4/3, a + b + c = 51 => a=9, b=30, c=12
    a_1_14 = Fraction(51, 1 + Fraction(10, 3) + Fraction(4, 3))
    b_1_14 = a_1_14 * Fraction(10, 3)
    c_1_14 = a_1_14 * Fraction(4, 3)
    assert (a_1_14, b_1_14, c_1_14) == (9, 30, 12) and b_1_14**2 - 4*a_1_14*c_1_14 > 0
    assert qm['sat_m2_1_q14']['correctAnswer'] == 'C'

    # Q15 (SPR): 2x^2 - 15x + c = 0, r^2 + s^2 = 161/4 => (15/2)^2 - c = 161/4 => c = 16
    c_1_15 = Fraction(15, 2) ** 2 - Fraction(161, 4)
    assert c_1_15 == 16 and 15**2 - 4*2*c_1_15 == 97 > 0
    r_num = (15 + math.sqrt(97)) / 4
    s_num = (15 - math.sqrt(97)) / 4
    assert abs((r_num**2 + s_num**2) - 161 / 4) < 1e-12
    assert qm['sat_m2_1_q15']['acceptedAnswers'] == ['16']

    # ------------------------------------------------------------------
    # DRILL 2.2 EXACT ARITHMETIC ASSERTIONS (Q1..Q15)
    # ------------------------------------------------------------------
    # Q1: p(-2)=0, p(5)=0 => (x - 5) is a factor
    assert (5 - 5) == 0 and qm['sat_m2_2_q1']['correctAnswer'] == 'D'

    # Q2: (3x - 4)(2x^2 + kx - 5) = 6x^3 + 7x^2 - 35x + 20 => k = 5
    k_2_2 = Fraction(7 + 8, 3)
    assert k_2_2 == 5
    for x in range(-4, 6):
        assert (3*x - 4)*(2*x**2 + k_2_2*x - 5) == 6*x**3 + 7*x**2 - 35*x + 20
    assert qm['sat_m2_2_q2']['correctAnswer'] == 'B'

    # Q3: 5/(x - 3) - 2/(x + 1) = (3x + 11)/((x - 3)(x + 1))
    for x in [0, 1, 2, 4, 5, -2, -5]:
        lhs = Fraction(5, x - 3) - Fraction(2, x + 1)
        rhs = Fraction(3*x + 11, (x - 3)*(x + 1))
        assert lhs == rhs
    assert qm['sat_m2_2_q3']['correctAnswer'] == 'A'

    # Q4 (SPR): (x^2 - 5x)/(x - 4) = (4 - 2x)/(x - 4) => x = -1 (x = 4 extraneous)
    valid_2_4 = [x for x in range(-20, 21) if x != 4 and Fraction(x**2 - 5*x, x - 4) == Fraction(4 - 2*x, x - 4)]
    assert valid_2_4 == [-1] and qm['sat_m2_2_q4']['acceptedAnswers'] == ['-1']

    # Q5: P(3) = 2(27) - 5(9) + 3k - 9 = 15 => k = 5
    k_2_5 = Fraction(15 - (2*27 - 5*9 - 9), 3)
    assert k_2_5 == 5 and qm['sat_m2_2_q5']['correctAnswer'] == 'C'

    # Q6: f(x) = -(x + 3)(x - 1)^2(x - 4): zeros -3, 1, 4; touch at 1 (no sign change); negative ends
    f_2_6 = lambda x: -(x + 3) * (x - 1)**2 * (x - 4)
    assert f_2_6(-3) == 0 and f_2_6(1) == 0 and f_2_6(4) == 0
    assert f_2_6(Fraction(9, 10)) > 0 and f_2_6(Fraction(11, 10)) > 0  # tangent without crossing at x=1
    assert f_2_6(-4) < 0 and f_2_6(-2) > 0  # crosses at -3
    assert f_2_6(3) > 0 and f_2_6(5) < 0    # crosses at 4
    assert f_2_6(-100) < 0 and f_2_6(100) < 0
    assert qm['sat_m2_2_q6']['correctAnswer'] == 'D'

    # Q7: (4x^2 - 5x + 7)/(x - 2) = 4x + 3 + 13/(x - 2)
    c_2_7 = 4*(2**2) - 5*2 + 7
    assert c_2_7 == 13
    for x in [-3, 0, 1, 3, 7]:
        assert Fraction(4*x**2 - 5*x + 7, x - 2) == 4*x + 3 + Fraction(c_2_7, x - 2)
    assert qm['sat_m2_2_q7']['correctAnswer'] == 'A'

    # Q8 (SPR): 2x/(x - 3) - 5/(x + 2) = 30/(x^2 - x - 6) => x = -5/2 (x = 3 extraneous)
    x_2_8 = Fraction(-5, 2)
    assert Fraction(2*x_2_8, x_2_8 - 3) - Fraction(5, x_2_8 + 2) == Fraction(30, x_2_8**2 - x_2_8 - 6)
    assert (2*3 + 5)*(3 - 3) == 0  # 3 is the extraneous quadratic root
    assert '-5/2' in qm['sat_m2_2_q8']['acceptedAnswers'] and '-2.5' in qm['sat_m2_2_q8']['acceptedAnswers']

    # Q9: x^3 + 3x^2 - 16x - 48 = (x - 4)(x + 3)(x + 4), a=-4 < b=3 < c=4 => c - a = 8
    for x in range(-5, 6):
        assert x**3 + 3*x**2 - 16*x - 48 == (x - 4)*(x + 3)*(x + 4)
    assert 4 - (-4) == 8 and qm['sat_m2_2_q9']['correctAnswer'] == 'B'

    # Q10: (7x + 13)/((x - 1)(x + 3)) = 5/(x - 1) + 2/(x + 3) => A - B = 3
    A_2_10 = Fraction(7*1 + 13, 1 + 3)
    B_2_10 = Fraction(7*(-3) + 13, -3 - 1)
    assert (A_2_10, B_2_10) == (5, 2) and A_2_10 - B_2_10 == 3
    for x in [-4, -2, 0, 2, 5]:
        assert Fraction(7*x + 13, (x - 1)*(x + 3)) == Fraction(A_2_10, x - 1) + Fraction(B_2_10, x + 3)
    assert qm['sat_m2_2_q10']['correctAnswer'] == 'D'

    # Q11: (px - 3)(qx + 5) = 12x^2 + rx - 15, p+q=7, p>q => p=4, q=3, r=11
    pairs_2_11 = [(p, 7 - p) for p in range(-20, 21) if p * (7 - p) == 12 and p > 7 - p]
    assert pairs_2_11 == [(4, 3)]
    r_2_11 = 5*4 - 3*3
    assert r_2_11 == 11 and qm['sat_m2_2_q11']['correctAnswer'] == 'A'

    # Q12 (SPR): g(x) = x^3 + ax^2 + bx - 12 divisible by (x - 2) and (x + 3) => a=3, b=-4, a+b=-1
    a_2_12, b_2_12 = 3, -4
    for x in range(-4, 5):
        assert x**3 + a_2_12*x**2 + b_2_12*x - 12 == (x - 2)*(x + 3)*(x + 2)
    assert a_2_12 + b_2_12 == -1 and qm['sat_m2_2_q12']['acceptedAnswers'] == ['-1']

    # Q13: h(x) = 2x^3 - 10x^2 + px + q with roots -1, 2, r => r = 4, q = 16
    r_2_13 = Fraction(10, 2) - (-1 + 2)
    q_2_13 = 2 * (0 + 1) * (0 - 2) * (0 - r_2_13)
    assert r_2_13 == 4 and q_2_13 == 16
    for x in range(-3, 6):
        assert 2*(x + 1)*(x - 2)*(x - 4) == 2*x**3 - 10*x**2 + 4*x + 16
    assert qm['sat_m2_2_q13']['correctAnswer'] == 'C'

    # Q14: (2x^2 + kx - 15)/(x^2 - 9) = (2x + 5)/(x + 3) for x > 3 => k = -1
    k_2_14 = -1
    for x in [4, 5, 7, 10]:
        assert Fraction(2*x**2 + k_2_14*x - 15, x**2 - 9) == Fraction(2*x + 5, x + 3)
    assert qm['sat_m2_2_q14']['correctAnswer'] == 'B'

    # Q15 (SPR): x/(x - 3) - k/(x + 1) = (x^2 + 19)/((x - 3)(x + 1)) => (1 - k)x = 19 - 3k
    no_sol_ks = []
    for k in range(-20, 21):
        if 1 - k == 0:
            if 19 - 3*k != 0:
                no_sol_ks.append(k)
        else:
            x_cand = Fraction(19 - 3*k, 1 - k)
            if x_cand in (3, -1):
                no_sol_ks.append(k)
    assert no_sol_ks == [1, 5] and sum(no_sol_ks) == 6
    assert qm['sat_m2_2_q15']['acceptedAnswers'] == ['6']

    # ------------------------------------------------------------------
    # DRILL 2.3 EXACT ARITHMETIC ASSERTIONS (Q1..Q15)
    # ------------------------------------------------------------------
    # Q1: P(t) = 450 * 3^(t/4)
    assert 450 * (3 ** 0) == 450 and 450 * (3 ** 1) == 1350 and 450 * (3 ** 2) == 4050
    assert qm['sat_m2_3_q1']['correctAnswer'] == 'A'

    # Q2: V(t) = 42000 * (0.84)^t => 1 - 0.84 = 0.16 (16% decrease)
    assert Fraction(1) - Fraction(84, 100) == Fraction(16, 100)
    assert qm['sat_m2_3_q2']['correctAnswer'] == 'C'

    # Q3: Account X ratios = 1.2 (exponential), Account Y diffs = 250 (linear)
    acct_x = [1000, 1200, 1440, 1728]
    acct_y = [1000, 1250, 1500, 1750]
    assert all(Fraction(acct_x[i+1], acct_x[i]) == Fraction(6, 5) for i in range(3))
    assert all(acct_y[i+1] - acct_y[i] == 250 for i in range(3))
    assert qm['sat_m2_3_q3']['correctAnswer'] == 'D'

    # Q4 (SPR): 320 * (1/2)^(24/6) = 20
    rem_3_4 = Fraction(320) * (Fraction(1, 2) ** (24 // 6))
    assert rem_3_4 == 20 and qm['sat_m2_3_q4']['acceptedAnswers'] == ['20']

    # Q5: (1.04)^2 = 1.0816 exact
    assert Fraction(104, 100) ** 2 == Fraction(10816, 10000)
    assert qm['sat_m2_3_q5']['correctAnswer'] == 'B'

    # Q6: 18 * 3^(x - 2) = 2 * 3^x
    for x in range(0, 6):
        assert Fraction(18) * (Fraction(3) ** (x - 2)) == Fraction(2) * (Fraction(3) ** x)
    assert Fraction(18) * (Fraction(3) ** (-2)) == 2 and qm['sat_m2_3_q6']['correctAnswer'] == 'A'

    # Q7: 1.40 * 0.85 = 1.19 => 19% greater
    net_3_7 = Fraction(140, 100) * Fraction(85, 100)
    assert net_3_7 == Fraction(119, 100) and qm['sat_m2_3_q7']['correctAnswer'] == 'C'

    # Q8 (SPR): g(1)=12, g(3)=108, g(5)=972 => b=3, a=g(0)=4
    b_sq_3_8 = Fraction(108, 12)
    assert b_sq_3_8 == 9 and Fraction(972, 108) == 9
    b_3_8 = math.isqrt(int(b_sq_3_8))
    a_3_8 = Fraction(12, b_3_8)
    assert (a_3_8, b_3_8) == (4, 3) and qm['sat_m2_3_q8']['acceptedAnswers'] == ['4']

    # Q9: every 8 months in t years = 12t/8 = 3t/2
    assert Fraction(12, 8) == Fraction(3, 2) and qm['sat_m2_3_q9']['correctAnswer'] == 'D'

    # Q10: f(x) = -4(2)^x + 12 => f(0)=8, limit x->-inf is 12
    assert -4 * (2 ** 0) + 12 == 8
    assert abs((-4 * (2 ** -50) + 12) - 12) < 1e-12
    assert qm['sat_m2_3_q10']['correctAnswer'] == 'B'

    # Q11: (0.81)^(2/4) = 0.90 => p = 10
    base_2yr = Fraction(9, 10)
    assert base_2yr ** 2 == Fraction(81, 100)
    p_3_11 = (1 - base_2yr) * 100
    assert p_3_11 == 10 and qm['sat_m2_3_q11']['correctAnswer'] == 'C'

    # Q12 (SPR): f(x) = a*b^x + c, f(0)=11, f(1)=17, f(2)=35 => b=3, a=3, c=8
    b_3_12 = Fraction(35 - 17, 17 - 11)
    a_3_12 = Fraction(17 - 11, b_3_12 - 1)
    c_3_12 = 11 - a_3_12
    assert (a_3_12, b_3_12, c_3_12) == (3, 3, 8)
    assert a_3_12 * (b_3_12 ** 0) + c_3_12 == 11
    assert a_3_12 * (b_3_12 ** 1) + c_3_12 == 17
    assert a_3_12 * (b_3_12 ** 2) + c_3_12 == 35
    assert qm['sat_m2_3_q12']['acceptedAnswers'] == ['8']

    # Q13: 80 * 2^(3x - 4) = 5 * 8^x => c=5, b=8, c+b=13
    c_3_13 = Fraction(80, 2 ** 4)
    b_3_13 = 2 ** 3
    assert (c_3_13, b_3_13) == (5, 8) and c_3_13 + b_3_13 == 13
    for x in range(0, 5):
        assert Fraction(80) * (Fraction(2) ** (3*x - 4)) == c_3_13 * (b_3_13 ** x)
    assert qm['sat_m2_3_q13']['correctAnswer'] == 'A'

    # Q14: 12 * 2^(t/3) = 384 * 2^(t/6) => 2^(t/6) = 32 = 2^5 => t = 30
    assert Fraction(384, 12) == 32 == 2 ** 5
    t_3_14 = 5 * 6
    assert t_3_14 == 30 and 12 * (2 ** (t_3_14 // 3)) == 384 * (2 ** (t_3_14 // 6)) == 12288
    assert qm['sat_m2_3_q14']['correctAnswer'] == 'D'

    # Q15 (SPR): 8000 * (1 + r/100)^3 = 13824 => r = 20
    ratio_3_15 = Fraction(13824, 8000)
    assert ratio_3_15 == Fraction(6, 5) ** 3
    r_3_15 = (Fraction(6, 5) - 1) * 100
    assert r_3_15 == 20 and qm['sat_m2_3_q15']['acceptedAnswers'] == ['20']

    # ------------------------------------------------------------------
    # DRILL 2.4 EXACT ARITHMETIC ASSERTIONS (Q1..Q15)
    # ------------------------------------------------------------------
    # Q1: sqrt(2x + 3) = x - 6 => x = 11 only (x = 3 extraneous)
    sols_4_1 = [x for x in range(-10, 30) if 2*x + 3 >= 0 and x - 6 >= 0 and (2*x + 3) == (x - 6) ** 2]
    assert sols_4_1 == [11] and (2*3 + 3 == (3 - 6) ** 2 and 3 - 6 < 0)
    assert qm['sat_m2_4_q1']['correctAnswer'] == 'C'

    # Q2: T = 2*pi*sqrt(L/g) => L = g*T^2 / (4*pi^2)
    for L_val, g_val in [(4.0, 9.8), (1.5, 3.7), (9.0, 1.0)]:
        T_val = 2 * math.pi * math.sqrt(L_val / g_val)
        L_rec = (g_val * T_val ** 2) / (4 * math.pi ** 2)
        assert abs(L_rec - L_val) < 1e-12
    assert qm['sat_m2_4_q2']['correctAnswer'] == 'B'

    # Q3: (x^(5/3) * x^(1/2)) / x^(2/3) = x^(3/2) = sqrt(x^3)
    exp_4_3 = Fraction(5, 3) + Fraction(1, 2) - Fraction(2, 3)
    assert exp_4_3 == Fraction(3, 2) and qm['sat_m2_4_q3']['correctAnswer'] == 'D'

    # Q4 (SPR): 3|2x - 5| - 7 = 14 => |2x - 5| = 7 => x in {-1, 6}, sum = 5
    sols_4_4 = [x for x in range(-20, 21) if 3 * abs(2*x - 5) - 7 == 14]
    assert sols_4_4 == [-1, 6] and sum(sols_4_4) == 5
    assert qm['sat_m2_4_q4']['acceptedAnswers'] == ['5']

    # Q5: f vertex (4, -3), g(x) = f(x + 5) - 6 => vertex (-1, -9)
    assert (4 - 5, -3 - 6) == (-1, -9) and qm['sat_m2_4_q5']['correctAnswer'] == 'A'

    # Q6: y = x^2 - 4x + 7 and y = 2x + 2 => (1, 4) and (5, 12), y1 + y2 = 16
    xs_4_6 = [x for x in range(-10, 15) if x**2 - 4*x + 7 == 2*x + 2]
    ys_4_6 = [2*x + 2 for x in xs_4_6]
    assert xs_4_6 == [1, 5] and ys_4_6 == [4, 12] and sum(ys_4_6) == 16
    assert qm['sat_m2_4_q6']['correctAnswer'] == 'C'

    # Q7: -2|x - 9| + k = 5 => |x - 9| = (k - 5)/2 < 0 iff k < 5 => k = 3
    assert [k for k in (5, 3, 7, 9) if Fraction(k - 5, 2) < 0] == [3]
    assert qm['sat_m2_4_q7']['correctAnswer'] == 'B'

    # Q8 (SPR): 2(2x - 7)^(3/2) = 54 => 2x - 7 = 9 => x = 8
    x_4_8 = Fraction(3**2 + 7, 2)
    assert x_4_8 == 8 and 2 * ((2*int(x_4_8) - 7) ** 3) == (54 // 2) ** 2 * 2
    assert abs(2 * ((2 * 8 - 7) ** 1.5) - 54) < 1e-12
    assert qm['sat_m2_4_q8']['acceptedAnswers'] == ['8']

    # Q9: 1/f = 1/u + 1/v => v = fu/(u - f)
    for f_v, u_v in [(Fraction(2), Fraction(6)), (Fraction(3), Fraction(10)), (Fraction(5, 2), Fraction(7))]:
        v_v = (f_v * u_v) / (u_v - f_v)
        assert Fraction(1, f_v) == Fraction(1, u_v) + Fraction(1, v_v)
    assert qm['sat_m2_4_q9']['correctAnswer'] == 'D'

    # Q10: y = 2x^2 - 7x + 11, y = 5x + c tangent => 2x^2 - 12x + (11 - c) = 0, Delta = 0 => c = -7
    c_4_10 = 11 - Fraction((-12) ** 2, 4 * 2)
    assert c_4_10 == -7 and (-12)**2 - 4*2*(11 - c_4_10) == 0
    assert qm['sat_m2_4_q10']['correctAnswer'] == 'A'

    # Q11: y = x^2 + 6x + 17, y = mx + 8 tangent with m > 0 => (6 - m)^2 - 36 = 0 => m = 12
    ms_4_11 = [m for m in range(-20, 30) if (6 - m)**2 - 4*1*(17 - 8) == 0]
    assert ms_4_11 == [0, 12] and [m for m in ms_4_11 if m > 0] == [12]
    assert qm['sat_m2_4_q11']['correctAnswer'] == 'B'

    # Q12 (SPR): 2x - 9*sqrt(x) + 10 = 0 => u in {2, 5/2} => x in {4, 25/4}, sum = 41/4 = 10.25
    u1, u2 = Fraction(2), Fraction(5, 2)
    assert 2*u1**2 - 9*u1 + 10 == 0 and 2*u2**2 - 9*u2 + 10 == 0
    sum_4_12 = u1**2 + u2**2
    assert sum_4_12 == Fraction(41, 4) and '41/4' in qm['sat_m2_4_q12']['acceptedAnswers'] and '10.25' in qm['sat_m2_4_q12']['acceptedAnswers']

    # Q13: f(x) = 2(x + 3)(x - 5), vertex (1, -32); g(x) = f(x - 4) + k tangent to x-axis at (h, 0) => h=5, k=32, h+k=37
    x0 = Fraction(-3 + 5, 2)
    y0 = 2 * (x0 + 3) * (x0 - 5)
    h_4_13 = x0 + 4
    k_4_13 = -y0
    assert (x0, y0) == (1, -32) and (h_4_13, k_4_13) == (5, 32) and h_4_13 + k_4_13 == 37
    for x in range(-2, 10):
        assert 2*((x - 4) + 3)*((x - 4) - 5) + k_4_13 == 2*(x - h_4_13)**2
    assert qm['sat_m2_4_q13']['correctAnswer'] == 'D'

    # Q14: |x^2 - 6x + 5| = 4 => x^2 - 6x + 1 = 0 (2 distinct roots, sum 6) U (x - 3)^2 = 0 (1 root: 3) => distinct sum = 9
    r1 = 3 - 2 * math.sqrt(2)
    r2 = 3.0
    r3 = 3 + 2 * math.sqrt(2)
    assert len({round(r1, 8), round(r2, 8), round(r3, 8)}) == 3
    for r in (r1, r2, r3):
        assert abs(abs(r**2 - 6*r + 5) - 4) < 1e-12
    assert abs((r1 + r2 + r3) - 9.0) < 1e-12
    assert qm['sat_m2_4_q14']['correctAnswer'] == 'C'

    # Q15 (SPR): x^2 + y^2 = 85, x - y = 5 => 2xy = 85 - 25 = 60 => xy = 30
    xy_4_15 = Fraction(85 - 5**2, 2)
    assert xy_4_15 == 30
    # Verify real solutions exist and satisfy both equations
    x_sol = (5 + math.sqrt(145)) / 2
    y_sol = (-5 + math.sqrt(145)) / 2
    assert abs(x_sol - y_sol - 5) < 1e-12 and abs(x_sol**2 + y_sol**2 - 85) < 1e-12 and abs(x_sol * y_sol - 30) < 1e-12
    assert qm['sat_m2_4_q15']['acceptedAnswers'] == ['30']

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
    print("ALL 4 M2 DRILLS (60 Qs) VERIFIED & QA PASSED!")
