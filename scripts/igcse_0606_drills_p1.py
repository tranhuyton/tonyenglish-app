# -*- coding: utf-8 -*-
"""
Cambridge IGCSE Additional Mathematics (0606) — 2025–2027 Syllabus Upgrade
Part 1 Topical Drills: Chapters 1 to 7B (Algebra, Logs, Linear Law & Circle)
8 Topical Drills × 12 Questions = 96 Programmatically Verified Questions:
  1. d0606_c1  (Ch. 1)  — Functions, Domain/Range, Composite & Inverse (Non-Calc)
  2. d0606_c2  (Ch. 2)  — Quadratic Functions, Discriminant & Inequalities (Non-Calc)
  3. d0606_c3  (Ch. 3)  — Indices & Surds — Paper 1 Foundation Bridge (Non-Calc)
  4. d0606_c4  (Ch. 4)  — Factors of Polynomials — Remainder & Factor Theorem (Non-Calc)
  5. d0606_c5  (Ch. 5)  — Simultaneous Equations, Modulus & Cubic Inequalities (Non-Calc)
  6. d0606_c6  (Ch. 6)  — Logarithmic & Exponential Functions (Calculator)
  7. d0606_c7  (Ch. 7)  — Straight Line Graphs & Linear Law Transformation (Calculator)
  8. d0606_c7b (Ch. 7B) — Coordinate Geometry of the Circle (NEW 2025–2027, Non-Calc)
"""

import math
import os
import re
import sys
from fractions import Fraction

_ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _ROOT_DIR not in sys.path:
    sys.path.insert(0, _ROOT_DIR)

from scripts.igcse_maths_pipeline import (
    COURSE_0606_ID,
    build_igcse_drill_json,
    validate_igcse_drill,
)


def _q(tag, q, options, answer, explanation):
    return {
        'tag': tag,
        'q': q,
        'options': options,
        'answer': answer,
        'explanation': explanation,
    }


# =============================================================================
# DRILL 1 (Ch. 1): Functions, Domain/Range, Composite & Inverse (Non-Calc)
# Answer balance: B, D, A, C, D, A, B, C, A, D, C, B (A:3, B:3, C:3, D:3)
# =============================================================================
_DRILL_C1 = {
    'code': 'd0606_c1',
    'folder_key': 'drills_p1',
    'lecture_key': 'c1',
    'calculator_policy': 'non-calculator',
    'order_index': 1,
    'title': 'Ch. 1 Drill: Functions, Domain/Range, Composite & Inverse (0606)',
    'time_limit': '30',
    'intro_html': (
        r'<p><b>Mục tiêu Chapter 1 (Cambridge 0606 Paper 1 Non-Calculator):</b> '
        r'Làm chủ điều kiện đơn ánh (1-to-1) bằng hoàn thành bình phương, xác định miền giá trị (range) của hàm bậc hai/hàm mũ, '
        r'tính hàm hợp \(fg(x)\), hàm ngược \(f^{-1}(x)\), giải \(f(x)=f^{-1}(x)\) qua đường thẳng \(y=x\), và phân tích hàm trị tuyệt đối \(|ax+b|\).</p>'
    ),
    'questions': [
        _q(
            'Domain for 1-to-1 (Non-Calc)',
            r'<p>The function \(f\) is defined by \(f(x) = 2x^2 - 12x + 23\) for \(x \ge k\). Find the smallest value of \(k\) such that \(f\) has an inverse function.</p>',
            [
                r'\(k = 5\)',
                r'\(k = 3\)',
                r'\(k = 6\)',
                r'\(k = -3\)',
            ],
            'B',
            r'<p><b>Bước 1 (Hoàn thành bình phương / Complete the square):</b> '
            r'\(f(x) = 2(x^2 - 6x) + 23 = 2\left[(x - 3)^2 - 9\right] + 23 = 2(x - 3)^2 + 5\). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Điều kiện 1-to-1):</b> Hàm số bậc hai có đỉnh tại \((3, 5)\). Để \(f\) là hàm đơn ánh (one-to-one) và tồn tại hàm ngược \(f^{-1}\) trên \(x \ge k\), ta cần \(k \ge 3\). '
            r'Vậy giá trị nhỏ nhất là \(k = 3\). <b>[A1]</b></p>'
            r'<p><i>Bẫy thường gặp:</i> Nhầm hoành độ đỉnh \(x = 3\) với tung độ đỉnh \(y = 5\), hoặc quên đặt nhân tử chung \(2\) dẫn đến chọn \(k = 6\).</p>',
        ),
        _q(
            'Range on Restricted Domain (Non-Calc)',
            r'<p>The function \(f\) is defined by \(f(x) = 7 + 4x - x^2\) for \(x \ge 3\). State the range of \(f\).</p>',
            [
                r'\(f(x) \le 11\)',
                r'\(f(x) \ge 10\)',
                r'\(f(x) \ge 11\)',
                r'\(f(x) \le 10\)',
            ],
            'D',
            r'<p><b>Bước 1 (Tìm đỉnh parabol / Find vertex):</b> '
            r'\(f(x) = -(x^2 - 4x) + 7 = -(x - 2)^2 + 11\). Parabol úp xuống (hệ số \(x^2\) âm) với đỉnh cực đại tại \((2, 11)\). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Kiểm tra miền xác định \(x \ge 3\)):</b> Do \(x = 3\) nằm hoàn toàn bên phải trục đối xứng \(x = 2\), hàm \(f\) nghịch biến nghiêm ngặt trên \(x \ge 3\). '
            r'Giá trị lớn nhất đạt tại biên \(x = 3\): \(f(3) = 7 + 4(3) - 3^2 = 10\). '
            r'Khi \(x \to +\infty\) thì \(f(x) \to -\infty\), nên miền giá trị là \(f(x) \le 10\). <b>[A1]</b></p>'
            r'<p><i>Lưu ý Cambridge 0606:</i> Rất nhiều thí sinh mất điểm vì chọn \(f(x) \le 11\) mà quên kiểm tra xem hoành độ đỉnh \(x = 2\) có thuộc miền xác định hay không!</p>',
        ),
        _q(
            'Range of Exponential Function (Non-Calc)',
            r'<p>The function \(g\) is defined by \(g(x) = 5 - 3e^{2x}\) for \(x \in \mathbb{R}\). State the range of \(g\).</p>',
            [
                r'\(g(x) < 5\)',
                r'\(g(x) \le 5\)',
                r'\(g(x) > 5\)',
                r'\(g(x) < 2\)',
            ],
            'A',
            r'<p><b>Bước 1 (Tính chất hàm mũ / Property of \(e^{2x}\)):</b> Với mọi \(x \in \mathbb{R}\), ta luôn có \(e^{2x} > 0\) (không bao giờ bằng \(0\)). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Suy ra miền giá trị):</b> Nhân hai vế với \(-3\) (đổi chiều bất đẳng thức): \(-3e^{2x} < 0\). '
            r'Cộng \(5\) vào hai vế: \(5 - 3e^{2x} < 5\), tức là \(g(x) < 5\) (bất đẳng thức nghiêm ngặt vì \(y = 5\) là tiệm cận ngang). <b>[A1]</b></p>',
        ),
        _q(
            'Composite Function Equation (Non-Calc)',
            r'<p>Functions \(f\) and \(g\) are defined by \(f(x) = \frac{3x + 1}{x - 2}\) (\(x \ne 2\)) and \(g(x) = 2x + 1\) (\(x \in \mathbb{R}\)). Solve the equation \(fg(x) = 4\).</p>',
            [
                r'\(x = 2\)',
                r'\(x = \frac{5}{2}\)',
                r'\(x = 4\)',
                r'\(x = 9\)',
            ],
            'C',
            r'<p><b>Bước 1 (Lập hàm hợp \(fg(x)\)):</b> Thay \(g(x) = 2x + 1\) vào \(f\): '
            r'\[fg(x) = f(2x + 1) = \frac{3(2x + 1) + 1}{(2x + 1) - 2} = \frac{6x + 4}{2x - 1}\] <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Giải phương trình):</b> \(\frac{6x + 4}{2x - 1} = 4 \implies 6x + 4 = 4(2x - 1) = 8x - 4 \implies 2x = 8 \implies x = 4\). '
            r'Thử lại: \(g(4) = 9\), \(f(9) = \frac{28}{7} = 4\) (thỏa mãn). <b>[A1]</b></p>',
        ),
        _q(
            'Domain of Composite Function (Non-Calc)',
            r'<p>Given \(f(x) = 3x - 5\) for \(x \ge 2\) and \(g(x) = \sqrt{x - 4}\) for \(x \ge 4\), find the largest possible domain of \(x\) for which the composite function \(gf(x)\) is defined.</p>',
            [
                r'\(x \ge 2\)',
                r'\(x \ge 4\)',
                r'\(x \ge \frac{5}{3}\)',
                r'\(x \ge 3\)',
            ],
            'D',
            r'<p><b>Bước 1 (Điều kiện tồn tại của \(gf(x)\)):</b> Để \(gf(x) = g(f(x))\) xác định, ta cần đồng thời: '
            r'\(x\) thuộc miền xác định của \(f\) (\(x \ge 2\)) VÀ giá trị \(f(x)\) thuộc miền xác định của \(g\) (\(f(x) \ge 4\)). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Giải bất phương trình):</b> \(3x - 5 \ge 4 \implies 3x \ge 9 \implies x \ge 3\). '
            r'Kết hợp với \(x \ge 2\), ta được miền xác định lớn nhất là \(x \ge 3\). <b>[A1]</b></p>',
        ),
        _q(
            'Inverse of Quadratic Function (Non-Calc)',
            r'<p>The function \(f\) is defined by \(f(x) = (x - 4)^2 + 3\) for \(x \le 4\). Find an expression for \(f^{-1}(x)\) and state its domain.</p>',
            [
                r'\(f^{-1}(x) = 4 - \sqrt{x - 3}, \quad x \ge 3\)',
                r'\(f^{-1}(x) = 4 + \sqrt{x - 3}, \quad x \ge 3\)',
                r'\(f^{-1}(x) = 4 - \sqrt{x + 3}, \quad x \ge -3\)',
                r'\(f^{-1}(x) = 4 - \sqrt{x - 3}, \quad x \le 4\)',
            ],
            'A',
            r'<p><b>Bước 1 (Đảo vai trò \(x, y\)):</b> Đặt \(y = (x - 4)^2 + 3 \implies (x - 4)^2 = y - 3 \implies x - 4 = \pm\sqrt{y - 3}\). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Chọn dấu đúng theo miền xác định của \(f\)):</b> Vì miền xác định của \(f\) là \(x \le 4\), nên \(x - 4 \le 0\). '
            r'Do đó bắt buộc chọn dấu trừ: \(x = 4 - \sqrt{y - 3}\). '
            r'Miền xác định của \(f^{-1}\) chính là miền giá trị của \(f\): \(y \ge 3\). '
            r'Vậy \(f^{-1}(x) = 4 - \sqrt{x - 3}\) với \(x \ge 3\). <b>[A1]</b></p>',
        ),
        _q(
            'Inverse of Rational Function (Non-Calc)',
            r'<p>The function \(h\) is defined by \(h(x) = \frac{2x - 5}{x + 3}\) for \(x \ne -3\). Find \(h^{-1}(x)\).</p>',
            [
                r'\(h^{-1}(x) = \frac{3x - 5}{2 - x}, \quad x \ne 2\)',
                r'\(h^{-1}(x) = \frac{3x + 5}{2 - x}, \quad x \ne 2\)',
                r'\(h^{-1}(x) = \frac{5 - 3x}{x - 2}, \quad x \ne 2\)',
                r'\(h^{-1}(x) = \frac{2x + 5}{x - 3}, \quad x \ne 3\)',
            ],
            'B',
            r'<p><b>Bước 1 (Biến đổi theo \(x\)):</b> Đặt \(y = \frac{2x - 5}{x + 3} \implies y(x + 3) = 2x - 5 \implies xy + 3y = 2x - 5\). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Cô lập \(x\)):</b> \(3y + 5 = 2x - xy = x(2 - y) \implies x = \frac{3y + 5}{2 - y}\). '
            r'Đổi \(y\) thành \(x\): \(h^{-1}(x) = \frac{3x + 5}{2 - x}\) với \(x \ne 2\). <b>[A1]</b></p>',
        ),
        _q(
            'Solving f(x) = f⁻¹(x) via y = x (Non-Calc)',
            r'<p>The function \(f\) is defined by \(f(x) = x^2 - 6x + 10\) for \(x \ge 3\). Solve the equation \(f(x) = f^{-1}(x)\).</p>',
            [
                r'\(x = 2 \text{ and } x = 5\)',
                r'\(x = 2\)',
                r'\(x = 5\)',
                r'\(x = 3\)',
            ],
            'C',
            r'<p><b>Bước 1 (Dùng tính đối xứng qua đường \(y = x\)):</b> Với \(x \ge 3\), \(f(x) = (x - 3)^2 + 1\) đồng biến nghiêm ngặt nên giao điểm của \(y = f(x)\) và \(y = f^{-1}(x)\) nằm trên đường thẳng \(y = x\): '
            r'\(f(x) = x \implies x^2 - 6x + 10 = x \implies x^2 - 7x + 10 = 0\). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Giải và đối chiếu miền xác định):</b> \((x - 2)(x - 5) = 0 \implies x = 2 \text{ hoặc } x = 5\). '
            r'Vì miền xác định là \(x \ge 3\), ta LOẠI \(x = 2\) và chỉ nhận \(x = 5\). <b>[A1]</b></p>',
        ),
        _q(
            'Inverse of Logarithmic Function (Non-Calc)',
            r'<p>Given \(f(x) = 2\ln(x - 3) + 1\) for \(x > 3\), find \(f^{-1}(x)\).</p>',
            [
                r'\(f^{-1}(x) = 3 + e^{\frac{x - 1}{2}}\)',
                r'\(f^{-1}(x) = 3 + e^{2(x - 1)}\)',
                r'\(f^{-1}(x) = e^{\frac{x - 1}{2}} - 3\)',
                r'\(f^{-1}(x) = 3 + \frac{1}{2}e^{x - 1}\)',
            ],
            'A',
            r'<p><b>Bước 1 (Cô lập logarit tự nhiên):</b> Đặt \(y = 2\ln(x - 3) + 1 \implies \ln(x - 3) = \frac{y - 1}{2}\). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Mũ hóa cơ số \(e\)):</b> \(x - 3 = e^{\frac{y - 1}{2}} \implies x = 3 + e^{\frac{y - 1}{2}}\). '
            r'Vậy \(f^{-1}(x) = 3 + e^{\frac{x - 1}{2}}\) (với \(x \in \mathbb{R}\)). <b>[A1]</b></p>',
        ),
        _q(
            'Modulus Function Range (Non-Calc)',
            r'<p>The function \(f\) is defined by \(f(x) = 8 - |2x - 6|\) for \(0 \le x \le 8\). Find the range of \(f\).</p>',
            [
                r'\(2 \le f(x) \le 8\)',
                r'\(f(x) \le 8\)',
                r'\(0 \le f(x) \le 8\)',
                r'\(-2 \le f(x) \le 8\)',
            ],
            'D',
            r'<p><b>Bước 1 (Tìm đỉnh đồ thị chữ V ngược):</b> \(|2x - 6| = 0 \implies x = 3 \in [0, 8]\). '
            r'Tại \(x = 3\), \(f\) đạt giá trị lớn nhất \(f(3) = 8 - 0 = 8\). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Kiểm tra cả hai đầu mút của đoạn \([0, 8]\)):</b> '
            r'\(f(0) = 8 - |-6| = 2\) và \(f(8) = 8 - |10| = -2\). '
            r'Vì \(-2 < 2\), giá trị nhỏ nhất là \(-2\). Vậy miền giá trị là \(-2 \le f(x) \le 8\). <b>[A1]</b></p>',
        ),
        _q(
            'Modulus Quadratic Graph (Non-Calc)',
            r'<p>The graph of \(y = |x^2 - 4x - 5|\) is sketched for \(x \in \mathbb{R}\). State the coordinates of the local maximum point and the \(x\)-intercepts.</p>',
            [
                r'Local max \((2, -9)\); \(x\)-intercepts \((-1, 0)\) and \((5, 0)\)',
                r'Local max \((-2, 9)\); \(x\)-intercepts \((-5, 0)\) and \((1, 0)\)',
                r'Local max \((2, 9)\); \(x\)-intercepts \((-1, 0)\) and \((5, 0)\)',
                r'Local max \((2, 5)\); \(x\)-intercepts \((-1, 0)\) and \((5, 0)\)',
            ],
            'C',
            r'<p><b>Bước 1 (Tìm giao điểm trục \(Ox\) và đỉnh parabol gốc):</b> '
            r'\(x^2 - 4x - 5 = (x + 1)(x - 5) = (x - 2)^2 - 9\). '
            r'Giao trục \(Ox\) tại \((-1, 0)\) và \((5, 0)\); đỉnh cực tiểu của parabol gốc là \((2, -9)\). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Lấy đối xứng phần âm qua trục \(Ox\)):</b> Khi lấy trị tuyệt đối, phần đồ thị nằm dưới trục \(Ox\) được lật lên trên: '
            r'đỉnh \((2, -9)\) biến thành điểm cực đại địa phương (local maximum) \((2, 9)\), còn các giao điểm trục \(Ox\) giữ nguyên tại \((-1, 0)\) và \((5, 0)\). <b>[A1]</b></p>',
        ),
        _q(
            'Composite & Modulus Evaluation (Non-Calc)',
            r'<p>Given \(f(x) = |3x - 7|\) and \(g(x) = x^2 - 2\), evaluate \(fg(-2) - gf(1)\).</p>',
            [
                r'\(-15\)',
                r'\(-13\)',
                r'\(13\)',
                r'\(11\)',
            ],
            'B',
            r'<p><b>Bước 1 (Tính \(fg(-2)\)):</b> \(g(-2) = (-2)^2 - 2 = 2 \implies fg(-2) = f(2) = |3(2) - 7| = |-1| = 1\). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Tính \(gf(1)\) và hiệu):</b> \(f(1) = |3(1) - 7| = |-4| = 4 \implies gf(1) = g(4) = 4^2 - 2 = 14\). '
            r'Vậy \(fg(-2) - gf(1) = 1 - 14 = -13\). <b>[A1]</b></p>',
        ),
    ],
}


# =============================================================================
# DRILL 2 (Ch. 2): Quadratic Functions, Discriminant & Inequalities (Non-Calc)
# Answer balance: C, A, D, B, A, C, D, B, D, A, B, C (A:3, B:3, C:3, D:3)
# =============================================================================
_DRILL_C2 = {
    'code': 'd0606_c2',
    'folder_key': 'drills_p1',
    'lecture_key': 'c2',
    'calculator_policy': 'non-calculator',
    'order_index': 2,
    'title': 'Ch. 2 Drill: Quadratic Functions, Discriminant & Inequalities (0606)',
    'time_limit': '30',
    'intro_html': (
        r'<p><b>Mục tiêu Chapter 2 (Cambridge 0606 Paper 1 Non-Calculator):</b> '
        r'Hoàn thành bình phương dạng \(a(x+p)^2+q\), tìm GTLN/GTNN, vận dụng biệt thức \(\Delta = b^2 - 4ac\) cho bài toán tương giao đường thẳng–parabol '
        r'(tiếp xúc / 2 giao điểm / vô nghiệm), giải bất phương trình bậc hai và phương trình quy về bậc hai (hidden quadratics \(x^{2/3}, e^{2x}, \sqrt{x}\)).</p>'
    ),
    'questions': [
        _q(
            'Completing the Square (Non-Calc)',
            r'<p>Express \(3x^2 - 12x + 7\) in the form \(a(x + p)^2 + q\), where \(a, p, q\) are integers.</p>',
            [
                r'\(3(x - 2)^2 + 3\)',
                r'\(3(x - 4)^2 - 5\)',
                r'\(3(x - 2)^2 - 5\)',
                r'\(3(x - 2)^2 - 19\)',
            ],
            'C',
            r'<p><b>Bước 1 (Đặt nhân tử chung hệ số \(x^2\)):</b> '
            r'\(3x^2 - 12x + 7 = 3(x^2 - 4x) + 7 = 3\left[(x - 2)^2 - 4\right] + 7\). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Phá ngoặc chính xác):</b> '
            r'\(3(x - 2)^2 - 12 + 7 = 3(x - 2)^2 - 5\). <b>[A1]</b></p>'
            r'<p><i>Bẫy thường gặp:</i> Quên nhân \(3\) với \(-4\) trong ngoặc dẫn đến đáp án sai \(3(x - 2)^2 + 3\).</p>',
        ),
        _q(
            'Maximum Value of Quadratic (Non-Calc)',
            r'<p>Find the maximum value of \(f(x) = 5 - 8x - 2x^2\) and the value of \(x\) at which it occurs.</p>',
            [
                r'Maximum \(13\) at \(x = -2\)',
                r'Maximum \(13\) at \(x = 2\)',
                r'Maximum \(-3\) at \(x = -2\)',
                r'Maximum \(9\) at \(x = -2\)',
            ],
            'A',
            r'<p><b>Bước 1 (Hoàn thành bình phương với hệ số âm):</b> '
            r'\(f(x) = -2(x^2 + 4x) + 5 = -2\left[(x + 2)^2 - 4\right] + 5\). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Rút gọn và đọc cực đại):</b> '
            r'\(f(x) = -2(x + 2)^2 + 8 + 5 = 13 - 2(x + 2)^2\). '
            r'Vì \(-2(x + 2)^2 \le 0\), giá trị lớn nhất của \(f(x)\) là \(13\), đạt được khi \(x + 2 = 0 \implies x = -2\). <b>[A1]</b></p>',
        ),
        _q(
            'Reciprocal Quadratic Extremum (Non-Calc)',
            r'<p>Find the exact maximum value of \(y = \frac{12}{2x^2 - 12x + 21}\) for \(x \in \mathbb{R}\).</p>',
            [
                r'\(\frac{4}{7}\)',
                r'\(3\)',
                r'\(6\)',
                r'\(4\)',
            ],
            'D',
            r'<p><b>Bước 1 (Tìm GTNN của mẫu số):</b> '
            r'\(2x^2 - 12x + 21 = 2(x^2 - 6x) + 21 = 2\left[(x - 3)^2 - 9\right] + 21 = 2(x - 3)^2 + 3\). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Suy ra GTLN của phân thức):</b> Mẫu số luôn dương và đạt giá trị nhỏ nhất bằng \(3\) tại \(x = 3\). '
            r'Do tử số \(12 > 0\), phân thức đạt giá trị lớn nhất là \(y_{\max} = \frac{12}{3} = 4\). <b>[A1]</b></p>',
        ),
        _q(
            'Discriminant: No Real Roots (Non-Calc)',
            r'<p>Find the set of values of \(k\) for which the quadratic equation \(x^2 + (k - 2)x + k + 1 = 0\) has no real roots.</p>',
            [
                r'\(k < 0 \text{ or } k > 8\)',
                r'\(0 < k < 8\)',
                r'\(0 \le k \le 8\)',
                r'\(-8 < k < 0\)',
            ],
            'B',
            r'<p><b>Bước 1 (Lập điều kiện \(\Delta < 0\)):</b> Với \(a = 1, \; b = k - 2, \; c = k + 1\): '
            r'\[\Delta = (k - 2)^2 - 4(1)(k + 1) < 0 \implies k^2 - 4k + 4 - 4k - 4 < 0\] <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Giải bất phương trình bậc hai):</b> \(k^2 - 8k < 0 \implies k(k - 8) < 0 \implies 0 < k < 8\). <b>[A1]</b></p>',
        ),
        _q(
            'Line Tangent to Curve (Non-Calc)',
            r'<p>The line \(y = 2x + c\) is a tangent to the curve \(y = x^2 - 4x + 7\). Find the value of the constant \(c\).</p>',
            [
                r'\(c = -2\)',
                r'\(c = 2\)',
                r'\(c = -16\)',
                r'\(c = 16\)',
            ],
            'A',
            r'<p><b>Bước 1 (Phương trình hoành độ giao điểm):</b> '
            r'\(x^2 - 4x + 7 = 2x + c \implies x^2 - 6x + (7 - c) = 0\). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Điều kiện tiếp xúc \(\Delta = 0\)):</b> '
            r'\((-6)^2 - 4(1)(7 - c) = 0 \implies 36 - 28 + 4c = 0 \implies 4c = -8 \implies c = -2\). <b>[A1]</b></p>',
        ),
        _q(
            'Two Distinct Intersections (Non-Calc)',
            r'<p>Find the range of values of \(m\) for which the line \(y = mx - 3\) intersects the curve \(y = x^2 + x + 1\) at two distinct points.</p>',
            [
                r'\(-3 < m < 5\)',
                r'\(m < -5 \text{ or } m > 3\)',
                r'\(m < -3 \text{ or } m > 5\)',
                r'\(m \le -3 \text{ or } m \ge 5\)',
            ],
            'C',
            r'<p><b>Bước 1 (Lập phương trình giao điểm):</b> '
            r'\(x^2 + x + 1 = mx - 3 \implies x^2 + (1 - m)x + 4 = 0\). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Điều kiện 2 giao điểm phân biệt \(\Delta > 0\)):</b> '
            r'\((1 - m)^2 - 4(1)(4) > 0 \implies (m - 1)^2 > 16 \implies m - 1 < -4 \text{ hoặc } m - 1 > 4 \implies m < -3 \text{ or } m > 5\). <b>[A1]</b></p>',
        ),
        _q(
            'Always Positive Quadratic (Non-Calc)',
            r'<p>Find the set of values of \(k\) for which the curve \(y = kx^2 + 4x + k\) lies completely above the \(x\)-axis for all real values of \(x\).</p>',
            [
                r'\(k < -2 \text{ or } k > 2\)',
                r'\(-2 < k < 2\)',
                r'\(k \ge 2\)',
                r'\(k > 2\)',
            ],
            'D',
            r'<p><b>Bước 1 (Điều kiện kép cho đồ thị nằm hoàn toàn trên \(Ox\)):</b> Cần ĐỒNG THỜI hệ số \(a = k > 0\) (bề lõm hướng lên) VÀ \(\Delta < 0\) (không cắt trục \(Ox\)). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Giải và giao nghiệm):</b> '
            r'\(\Delta = 4^2 - 4(k)(k) < 0 \implies 16 - 4k^2 < 0 \implies k^2 > 4 \implies k < -2 \text{ hoặc } k > 2\). '
            r'Kết hợp với \(k > 0\), ta loại nhánh \(k < -2\) (nằm dưới \(Ox\)) và chỉ nhận \(k > 2\). <b>[A1]</b></p>',
        ),
        _q(
            'Quadratic Inequality (Non-Calc)',
            r'<p>Solve the inequality \(15 + 2x - x^2 \ge 0\).</p>',
            [
                r'\(x \le -3 \text{ or } x \ge 5\)',
                r'\(-3 \le x \le 5\)',
                r'\(-5 \le x \le 3\)',
                r'\(-3 < x < 5\)',
            ],
            'B',
            r'<p><b>Bước 1 (Đổi dấu về hệ số \(x^2\) dương):</b> Nhân hai vế với \(-1\) và đảo chiều bất đẳng thức: '
            r'\(x^2 - 2x - 15 \le 0 \implies (x - 5)(x + 3) \le 0\). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Đọc khoảng nghiệm):</b> Các nghiệm biên là \(x = -3\) và \(x = 5\); vì parabol hướng lên và lấy phần \(\le 0\), ta lấy miền giữa (bao gồm biên): \(-3 \le x \le 5\). <b>[A1]</b></p>',
        ),
        _q(
            'Rearranged Quadratic Inequality (Non-Calc)',
            r'<p>Solve the inequality \((2x - 1)(x + 3) > x^2 + 11\).</p>',
            [
                r'\(-7 < x < 2\)',
                r'\(-2 < x < 7\)',
                r'\(x < -2 \text{ or } x > 7\)',
                r'\(x < -7 \text{ or } x > 2\)',
            ],
            'D',
            r'<p><b>Bước 1 (Khai triển và chuyển vế):</b> '
            r'\(2x^2 + 5x - 3 > x^2 + 11 \implies x^2 + 5x - 14 > 0\). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Phân tích nhân tử):</b> \((x + 7)(x - 2) > 0\). '
            r'Nghiệm biên là \(-7\) và \(2\); lấy hai miền ngoài nên \(x < -7 \text{ or } x > 2\). <b>[A1]</b></p>',
        ),
        _q(
            'Hidden Quadratic: Fractional Power (Non-Calc)',
            r'<p>Solve the equation \(x^{\frac{2}{3}} - 5x^{\frac{1}{3}} + 6 = 0\).</p>',
            [
                r'\(x = 8 \text{ or } x = 27\)',
                r'\(x = 2 \text{ or } x = 3\)',
                r'\(x = 4 \text{ or } x = 9\)',
                r'\(x = \sqrt[3]{2} \text{ or } x = \sqrt[3]{3}\)',
            ],
            'A',
            r'<p><b>Bước 1 (Đặt ẩn phụ / Substitution):</b> Đặt \(u = x^{\frac{1}{3}}\), suy ra \(u^2 = x^{\frac{2}{3}}\). '
            r'Phương trình trở thành \(u^2 - 5u + 6 = 0 \implies (u - 2)(u - 3) = 0 \implies u = 2 \text{ hoặc } u = 3\). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Lập phương hai vế tìm \(x\)):</b> '
            r'\(x^{\frac{1}{3}} = 2 \implies x = 2^3 = 8\), và \(x^{\frac{1}{3}} = 3 \implies x = 3^3 = 27\). <b>[A1]</b></p>',
        ),
        _q(
            'Hidden Quadratic: Exponential (Non-Calc)',
            r'<p>Solve the equation \(e^{2x} - 2e^x - 15 = 0\), giving the exact value(s) of \(x\).</p>',
            [
                r'\(x = \ln 5 \text{ or } x = \ln(-3)\)',
                r'\(x = \ln 5\)',
                r'\(x = \ln 3\)',
                r'\(x = 5\)',
            ],
            'B',
            r'<p><b>Bước 1 (Đặt ẩn phụ \(u = e^x > 0\)):</b> '
            r'\(u^2 - 2u - 15 = 0 \implies (u - 5)(u + 3) = 0 \implies u = 5 \text{ hoặc } u = -3\). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Loại nghiệm âm và lấy \(\ln\)):</b> Vì \(e^x > 0\) với mọi \(x \in \mathbb{R}\), ta loại \(e^x = -3\). '
            r'Chỉ nhận \(e^x = 5 \implies x = \ln 5\). <b>[A1]</b></p>',
        ),
        _q(
            'Hidden Quadratic: Surd Root (Non-Calc)',
            r'<p>Solve the equation \(2x - 7\sqrt{x} - 15 = 0\) for \(x \ge 0\).</p>',
            [
                r'\(x = 25 \text{ or } x = \frac{9}{4}\)',
                r'\(x = 5\)',
                r'\(x = 25\)',
                r'\(x = 25 \text{ or } x = -\frac{3}{2}\)',
            ],
            'C',
            r'<p><b>Bước 1 (Đặt \(u = \sqrt{x} \ge 0\)):</b> '
            r'\(2u^2 - 7u - 15 = 0 \implies (2u + 3)(u - 5) = 0 \implies u = -\frac{3}{2} \text{ hoặc } u = 5\). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Kiểm tra điều kiện \(\sqrt{x} \ge 0\)):</b> Loại \(u = -\frac{3}{2}\) vì căn bậc hai số học không thể âm (nếu bình phương bừa sẽ sinh nghiệm ngoại lai \(x = \frac{9}{4}\)). '
            r'Với \(\sqrt{x} = 5 \implies x = 25\). <b>[A1]</b></p>',
        ),
    ],
}


# =============================================================================
# DRILL 3 (Ch. 3): Indices & Surds — Paper 1 Foundation Bridge (Non-Calc)
# Answer balance: A, C, B, D, C, B, A, D, B, D, C, A (A:3, B:3, C:3, D:3)
# =============================================================================
_DRILL_C3 = {
    'code': 'd0606_c3',
    'folder_key': 'drills_p1',
    'lecture_key': 'c3',
    'calculator_policy': 'non-calculator',
    'order_index': 3,
    'title': 'Ch. 3 Drill: Indices & Surds — Paper 1 Foundation Bridge (0606)',
    'time_limit': '30',
    'intro_html': (
        r'<p><b>Mục tiêu Chapter 3 (Cambridge 0606 Paper 1 Non-Calculator):</b> '
        r'Trục căn thức ở mẫu dạng \(\frac{a+b\sqrt{c}}{d+e\sqrt{c}}\), tính diện tích/chiều cao/chu vi chính xác của hình thang & tam giác chứa căn thức, '
        r'giải phương trình chứa căn, giải phương trình mũ chính xác \(9^x - 4(3^x) + 3 = 0\) và xử lý lũy thừa số mũ phân số/âm.</p>'
    ),
    'questions': [
        _q(
            'Rationalising Surds (Non-Calc)',
            r'<p>Express \(\frac{11 + 3\sqrt{5}}{3 - \sqrt{5}}\) in the form \(a + b\sqrt{5}\), where \(a\) and \(b\) are integers.</p>',
            [
                r'\(12 + 5\sqrt{5}\)',
                r'\(12 - 5\sqrt{5}\)',
                r'\(12 + 2\sqrt{5}\)',
                r'\(9 + 5\sqrt{5}\)',
            ],
            'A',
            r'<p><b>Bước 1 (Nhân tử và mẫu với lượng liên hợp \(3 + \sqrt{5}\)):</b> '
            r'\[\frac{(11 + 3\sqrt{5})(3 + \sqrt{5})}{(3 - \sqrt{5})(3 + \sqrt{5})} = \frac{33 + 11\sqrt{5} + 9\sqrt{5} + 15}{9 - 5}\] <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Rút gọn):</b> \(\frac{48 + 20\sqrt{5}}{4} = 12 + 5\sqrt{5}\). <b>[A1]</b></p>',
        ),
        _q(
            'Rationalising Complex Denominator (Non-Calc)',
            r'<p>Express \(\frac{6 - \sqrt{3}}{2\sqrt{3} - 3}\) in the form \(p + q\sqrt{3}\), where \(p\) and \(q\) are integers.</p>',
            [
                r'\(4 - 3\sqrt{3}\)',
                r'\(6 + 3\sqrt{3}\)',
                r'\(4 + 3\sqrt{3}\)',
                r'\(2 + 3\sqrt{3}\)',
            ],
            'C',
            r'<p><b>Bước 1 (Nhân liên hợp \(2\sqrt{3} + 3\)):</b> '
            r'\[\frac{(6 - \sqrt{3})(2\sqrt{3} + 3)}{(2\sqrt{3})^2 - 3^2} = \frac{12\sqrt{3} + 18 - 6 - 3\sqrt{3}}{12 - 9}\] <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Rút gọn tử và mẫu):</b> \(\frac{12 + 9\sqrt{3}}{3} = 4 + 3\sqrt{3}\). <b>[A1]</b></p>',
        ),
        _q(
            'Surd Trapezium Height (Non-Calc)',
            r'<p>A trapezium has parallel sides of lengths \((3 + \sqrt{2})\text{ cm}\) and \((5 + 3\sqrt{2})\text{ cm}\), and its exact area is \((16 + 6\sqrt{2})\text{ cm}^2\). Find the exact perpendicular height \(h\) of the trapezium in the form \(a + b\sqrt{2}\).</p>',
            [
                r'\((5 + \sqrt{2})\text{ cm}\)',
                r'\((5 - \sqrt{2})\text{ cm}\)',
                r'\((10 - 2\sqrt{2})\text{ cm}\)',
                r'\((3 - \sqrt{2})\text{ cm}\)',
            ],
            'B',
            r'<p><b>Bước 1 (Áp dụng công thức diện tích hình thang):</b> '
            r'\(\text{Area} = \frac{1}{2}(a + b)h = \frac{1}{2}\left[(3 + \sqrt{2}) + (5 + 3\sqrt{2})\right]h = (4 + 2\sqrt{2})h\). '
            r'Suy ra \(h = \frac{16 + 6\sqrt{2}}{4 + 2\sqrt{2}} = \frac{8 + 3\sqrt{2}}{2 + \sqrt{2}}\). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Trục căn thức ở mẫu):</b> '
            r'\(h = \frac{(8 + 3\sqrt{2})(2 - \sqrt{2})}{4 - 2} = \frac{16 - 8\sqrt{2} + 6\sqrt{2} - 6}{2} = \frac{10 - 2\sqrt{2}}{2} = (5 - \sqrt{2})\text{ cm}\). <b>[A1]</b></p>',
        ),
        _q(
            'Surd Right Triangle Perimeter (Non-Calc)',
            r'<p>A right-angled triangle has perpendicular sides of lengths \((\sqrt{11} + \sqrt{7})\text{ cm}\) and \((\sqrt{11} - \sqrt{7})\text{ cm}\). Find the exact perimeter of the triangle.</p>',
            [
                r'\((6 + 2\sqrt{7})\text{ cm}\)',
                r'\((18 + 2\sqrt{11})\text{ cm}\)',
                r'\((3\sqrt{2} + 2\sqrt{11})\text{ cm}\)',
                r'\((6 + 2\sqrt{11})\text{ cm}\)',
            ],
            'D',
            r'<p><b>Bước 1 (Tính cạnh huyền bằng định lý Pythagoras):</b> '
            r'\(c^2 = (\sqrt{11} + \sqrt{7})^2 + (\sqrt{11} - \sqrt{7})^2 = (11 + 2\sqrt{77} + 7) + (11 - 2\sqrt{77} + 7) = 36 \implies c = 6\text{ cm}\). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Tính chu vi tam giác):</b> '
            r'\(\text{Perimeter} = (\sqrt{11} + \sqrt{7}) + (\sqrt{11} - \sqrt{7}) + 6 = (6 + 2\sqrt{11})\text{ cm}\). <b>[A1]</b></p>',
        ),
        _q(
            'Solving Surd Linear Equation (Non-Calc)',
            r'<p>Solve the equation \(x\sqrt{5} - 4 = 2x + \sqrt{5}\), giving your answer in the form \(a + b\sqrt{5}\) where \(a\) and \(b\) are integers.</p>',
            [
                r'\(x = 3 + 6\sqrt{5}\)',
                r'\(x = 13 - 6\sqrt{5}\)',
                r'\(x = 13 + 6\sqrt{5}\)',
                r'\(x = 13 + 2\sqrt{5}\)',
            ],
            'C',
            r'<p><b>Bước 1 (Gom các hạng tử chứa \(x\)):</b> '
            r'\(x\sqrt{5} - 2x = 4 + \sqrt{5} \implies x(\sqrt{5} - 2) = 4 + \sqrt{5} \implies x = \frac{4 + \sqrt{5}}{\sqrt{5} - 2}\). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Trục căn thức):</b> '
            r'\(x = \frac{(4 + \sqrt{5})(\sqrt{5} + 2)}{5 - 4} = 4\sqrt{5} + 8 + 5 + 2\sqrt{5} = 13 + 6\sqrt{5}\). <b>[A1]</b></p>',
        ),
        _q(
            'Radical Equation with Extraneous Root (Non-Calc)',
            r'<p>Solve the equation \(\sqrt{2x + 7} = x - 4\).</p>',
            [
                r'\(x = 1 \text{ or } x = 9\)',
                r'\(x = 9\)',
                r'\(x = 1\)',
                r'\(x = 5\)',
            ],
            'B',
            r'<p><b>Bước 1 (Đặt điều kiện và bình phương hai vế):</b> Cần \(x - 4 \ge 0 \implies x \ge 4\). '
            r'Bình phương hai vế: \(2x + 7 = (x - 4)^2 = x^2 - 8x + 16 \implies x^2 - 10x + 9 = 0\). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Giải và loại nghiệm ngoại lai):</b> \((x - 1)(x - 9) = 0 \implies x = 1 \text{ hoặc } x = 9\). '
            r'Thử lại: với \(x = 1\), vế trái \(\sqrt{9} = 3 \ne -3\) (loại!). Chỉ nhận \(x = 9\). <b>[A1]</b></p>',
        ),
        _q(
            'Simplifying Surds (Non-Calc)',
            r'<p>Express \(\sqrt{75} + \frac{18}{\sqrt{3}} - \sqrt{48}\) in the form \(k\sqrt{3}\), where \(k\) is an integer.</p>',
            [
                r'\(7\sqrt{3}\)',
                r'\(5\sqrt{3}\)',
                r'\(15\sqrt{3}\)',
                r'\(3\sqrt{3}\)',
            ],
            'A',
            r'<p><b>Bước 1 (Đưa từng hạng tử về dạng \(n\sqrt{3}\)):</b> '
            r'\(\sqrt{75} = 5\sqrt{3}\), \(\frac{18}{\sqrt{3}} = \frac{18\sqrt{3}}{3} = 6\sqrt{3}\), và \(\sqrt{48} = 4\sqrt{3}\). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Cộng trừ hệ số):</b> \((5 + 6 - 4)\sqrt{3} = 7\sqrt{3}\). <b>[A1]</b></p>',
        ),
        _q(
            'Exact Index Equation (Non-Calc)',
            r'<p>Solve the equation \(9^x - 4(3^x) + 3 = 0\).</p>',
            [
                r'\(x = 1 \text{ or } x = 3\)',
                r'\(x = 1\)',
                r'\(x = 0 \text{ or } x = 3\)',
                r'\(x = 0 \text{ or } x = 1\)',
            ],
            'D',
            r'<p><b>Bước 1 (Đưa về cùng cơ số \(3\)):</b> Nhận xét \(9^x = (3^2)^x = (3^x)^2\). Đặt \(u = 3^x > 0\): '
            r'\(u^2 - 4u + 3 = 0 \implies (u - 1)(u - 3) = 0 \implies u = 1 \text{ hoặc } u = 3\). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Tìm \(x\)):</b> \(3^x = 1 = 3^0 \implies x = 0\); và \(3^x = 3 = 3^1 \implies x = 1\). <b>[A1]</b></p>',
        ),
        _q(
            'Shifted Index Quadratic (Non-Calc)',
            r'<p>Solve the equation \(2^{2x + 1} - 9(2^x) + 4 = 0\).</p>',
            [
                r'\(x = \frac{1}{2} \text{ or } x = 4\)',
                r'\(x = -1 \text{ or } x = 2\)',
                r'\(x = 1 \text{ or } x = 2\)',
                r'\(x = -2 \text{ or } x = 1\)',
            ],
            'B',
            r'<p><b>Bước 1 (Tách số mũ và đặt ẩn phụ):</b> \(2^{2x+1} = 2 \cdot (2^x)^2\). Đặt \(u = 2^x > 0\): '
            r'\(2u^2 - 9u + 4 = 0 \implies (2u - 1)(u - 4) = 0 \implies u = \frac{1}{2} \text{ hoặc } u = 4\). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Giải tìm \(x\)):</b> \(2^x = \frac{1}{2} = 2^{-1} \implies x = -1\); và \(2^x = 4 = 2^2 \implies x = 2\). <b>[A1]</b></p>',
        ),
        _q(
            'Fractional & Negative Indices (Non-Calc)',
            r'<p>Evaluate \(\left(\frac{27}{8}\right)^{-\frac{2}{3}} + 16^{\frac{3}{4}} - 81^{0.25}\), giving your answer as an exact improper fraction.</p>',
            [
                r'\(\frac{41}{9}\)',
                r'\(\frac{29}{4}\)',
                r'\(\frac{67}{9}\)',
                r'\(\frac{49}{9}\)',
            ],
            'D',
            r'<p><b>Bước 1 (Tính từng lũy thừa phân số không dùng máy tính):</b> '
            r'\(\left(\frac{27}{8}\right)^{-\frac{2}{3}} = \left(\frac{8}{27}\right)^{\frac{2}{3}} = \left(\frac{2}{3}\right)^2 = \frac{4}{9}\); '
            r'\(16^{\frac{3}{4}} = (\sqrt[4]{16})^3 = 2^3 = 8\); \(81^{0.25} = \sqrt[4]{81} = 3\). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Cộng trừ phân số):</b> \(\frac{4}{9} + 8 - 3 = \frac{4}{9} + 5 = \frac{49}{9}\). <b>[A1]</b></p>',
        ),
        _q(
            'Simultaneous Index Equations (Non-Calc)',
            r'<p>Solve the simultaneous equations \(4^x \times 2^y = 32\) and \(9^x \div 3^y = 27\).</p>',
            [
                r'\(x = 1, \quad y = 3\)',
                r'\(x = 3, \quad y = -1\)',
                r'\(x = 2, \quad y = 1\)',
                r'\(x = 2, \quad y = -1\)',
            ],
            'C',
            r'<p><b>Bước 1 (Đưa về cùng cơ số \(2\) và \(3\)):</b> '
            r'\(2^{2x} \times 2^y = 2^5 \implies 2x + y = 5\); '
            r'\(3^{2x} \div 3^y = 3^3 \implies 2x - y = 3\). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Giải hệ tuyến tính):</b> Cộng hai phương trình: \(4x = 8 \implies x = 2\). '
            r'Thay vào \(2x + y = 5 \implies y = 1\). <b>[A1]</b></p>',
        ),
        _q(
            'Index Laws Single Base (Non-Calc)',
            r'<p>Given that \(\frac{2^{3x - 1} \times 8^{x + 2}}{4^{2x}} = \sqrt{2}\), find the exact value of \(x\).</p>',
            [
                r'\(x = -\frac{9}{4}\)',
                r'\(x = -\frac{7}{4}\)',
                r'\(x = \frac{9}{4}\)',
                r'\(x = -\frac{11}{4}\)',
            ],
            'A',
            r'<p><b>Bước 1 (Đổi tất cả về cơ số \(2\)):</b> \(8^{x+2} = 2^{3x+6}\), \(4^{2x} = 2^{4x}\), \(\sqrt{2} = 2^{\frac{1}{2}}\). '
            r'Số mũ vế trái: \((3x - 1) + (3x + 6) - 4x = 2x + 5\). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Cho hai số mũ bằng nhau):</b> '
            r'\(2x + 5 = \frac{1}{2} \implies 2x = -\frac{9}{2} \implies x = -\frac{9}{4}\). <b>[A1]</b></p>',
        ),
    ],
}


# =============================================================================
# DRILL 4 (Ch. 4): Factors of Polynomials — Remainder & Factor Theorem (Non-Calc)
# Answer balance: D, B, C, A, B, D, C, A, C, A, D, B (A:3, B:3, C:3, D:3)
# =============================================================================
_DRILL_C4 = {
    'code': 'd0606_c4',
    'folder_key': 'drills_p1',
    'lecture_key': 'c4',
    'calculator_policy': 'non-calculator',
    'order_index': 4,
    'title': 'Ch. 4 Drill: Factors of Polynomials — Remainder & Factor Theorem (0606)',
    'time_limit': '30',
    'intro_html': (
        r'<p><b>Mục tiêu Chapter 4 (Cambridge 0606 Paper 1 Non-Calculator):</b> '
        r'Thành thạo Định lý số dư (Remainder Theorem), Định lý nhân tử (Factor Theorem) với bài toán tìm 2 ẩn \(a, b\), '
        r'phân tích triệt để đa thức bậc ba \(ax^3+bx^2+cx+d\), giải phương trình bậc ba (kể cả trường hợp vô nghiệm/nghiệm vô tỉ) và bất phương trình bậc ba.</p>'
    ),
    'questions': [
        _q(
            'Remainder Theorem (Non-Calc)',
            r'<p>Find the remainder when \(P(x) = 2x^3 - 5x^2 + 3x - 7\) is divided by \((x - 2)\).</p>',
            [
                r'\(5\)',
                r'\(-11\)',
                r'\(-23\)',
                r'\(-5\)',
            ],
            'D',
            r'<p><b>Bước 1 (Áp dụng Định lý số dư / Remainder Theorem):</b> Số dư khi chia \(P(x)\) cho \((x - 2)\) bằng \(P(2)\). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Tính giá trị):</b> \(P(2) = 2(2)^3 - 5(2)^2 + 3(2) - 7 = 16 - 20 + 6 - 7 = -5\). <b>[A1]</b></p>',
        ),
        _q(
            'Factor Theorem with (ax - b) (Non-Calc)',
            r'<p>Given that \((2x - 1)\) is a factor of \(f(x) = 4x^3 + kx^2 - 5x + 1\), find the value of \(k\).</p>',
            [
                r'\(k = -4\)',
                r'\(k = 4\)',
                r'\(k = 2\)',
                r'\(k = 8\)',
            ],
            'B',
            r'<p><b>Bước 1 (Áp dụng Định lý nhân tử):</b> Vì \((2x - 1)\) là nhân tử của \(f(x)\), ta có \(f\left(\frac{1}{2}\right) = 0\). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Giải tìm \(k\)):</b> \(4\left(\frac{1}{8}\right) + k\left(\frac{1}{4}\right) - 5\left(\frac{1}{2}\right) + 1 = 0 \implies \frac{1}{2} + \frac{k}{4} - \frac{5}{2} + 1 = 0 \implies \frac{k}{4} - 1 = 0 \implies k = 4\). <b>[A1]</b></p>',
        ),
        _q(
            'Two Unknowns a, b (Non-Calc)',
            r'<p>The polynomial \(P(x) = x^3 + ax^2 + bx - 6\) is divisible by \((x - 1)\) and leaves a remainder of \(12\) when divided by \((x + 2)\). Find the values of \(a\) and \(b\).</p>',
            [
                r'\(a = 4, \quad b = 1\)',
                r'\(a = 6, \quad b = 1\)',
                r'\(a = 6, \quad b = -1\)',
                r'\(a = -1, \quad b = 6\)',
            ],
            'C',
            r'<p><b>Bước 1 (Lập hệ 2 phương trình từ \(P(1)=0\) và \(P(-2)=12\)):</b> '
            r'\(P(1) = 1 + a + b - 6 = 0 \implies a + b = 5\); '
            r'\(P(-2) = -8 + 4a - 2b - 6 = 12 \implies 4a - 2b = 26 \implies 2a - b = 13\). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Giải hệ):</b> Cộng hai phương trình: \(3a = 18 \implies a = 6\). Suy ra \(b = 5 - 6 = -1\). <b>[A1]</b></p>',
        ),
        _q(
            'Remainder Theorem 2 Unknowns (Non-Calc)',
            r'<p>When \(f(x) = 2x^3 + px^2 + qx + 5\) is divided by \((x - 2)\) the remainder is \(15\), and when divided by \((x + 1)\) the remainder is \(-6\). Find \(p\) and \(q\).</p>',
            [
                r'\(p = -4, \quad q = 5\)',
                r'\(p = 4, \quad q = -5\)',
                r'\(p = -4, \quad q = -5\)',
                r'\(p = -2, \quad q = 1\)',
            ],
            'A',
            r'<p><b>Bước 1 (Thiết lập hệ phương trình):</b> '
            r'\(f(2) = 16 + 4p + 2q + 5 = 15 \implies 4p + 2q = -6 \implies 2p + q = -3\); '
            r'\(f(-1) = -2 + p - q + 5 = -6 \implies p - q = -9\). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Giải hệ):</b> Cộng vế theo vế: \(3p = -12 \implies p = -4\), suy ra \(q = p + 9 = 5\). <b>[A1]</b></p>',
        ),
        _q(
            'Complete Cubic Factorisation (Non-Calc)',
            r'<p>Factorise \(x^3 - 4x^2 + x + 6\) completely.</p>',
            [
                r'\((x - 1)(x - 2)(x + 3)\)',
                r'\((x + 1)(x - 2)(x - 3)\)',
                r'\((x + 1)(x + 2)(x - 3)\)',
                r'\((x - 1)(x + 2)(x - 3)\)',
            ],
            'B',
            r'<p><b>Bước 1 (Thử nghiệm nguyên bằng Factor Theorem):</b> Với \(x = -1\): \((-1)^3 - 4(-1)^2 + (-1) + 6 = 0 \implies (x + 1)\) là nhân tử. <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Chia đa thức và phân tích tiếp):</b> '
            r'\(x^3 - 4x^2 + x + 6 = (x + 1)(x^2 - 5x + 6) = (x + 1)(x - 2)(x - 3)\). <b>[A1]</b></p>',
        ),
        _q(
            'Non-Monic Cubic Factorisation (Non-Calc)',
            r'<p>Factorise \(2x^3 - 3x^2 - 11x + 6\) completely.</p>',
            [
                r'\((x - 2)(2x + 1)(x + 3)\)',
                r'\((x + 2)(2x + 1)(x - 3)\)',
                r'\((x - 3)(2x - 3)(x + 1)\)',
                r'\((x + 2)(2x - 1)(x - 3)\)',
            ],
            'D',
            r'<p><b>Bước 1 (Tìm một nhân tử bậc nhất):</b> Thử \(x = -2\): \(2(-8) - 3(4) - 11(-2) + 6 = -16 - 12 + 22 + 6 = 0 \implies (x + 2)\) là nhân tử. <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Chia đa thức và phân tích nhân tử bậc hai):</b> '
            r'\(2x^3 - 3x^2 - 11x + 6 = (x + 2)(2x^2 - 7x + 3) = (x + 2)(2x - 1)(x - 3)\). <b>[A1]</b></p>',
        ),
        _q(
            'Cubic with One Real Root (Non-Calc)',
            r'<p>Given that \((x - 2)\) is a factor of \(f(x) = x^3 - x^2 + x - 6\), determine the number of real roots of \(f(x) = 0\) and state the real root(s).</p>',
            [
                r'Three real roots: \(x = 2, -1, 3\)',
                r'Two real roots: \(x = 2, -3\)',
                r'Exactly one real root: \(x = 2\)',
                r'No real roots',
            ],
            'C',
            r'<p><b>Bước 1 (Phân tích theo nhân tử \((x - 2)\)):</b> '
            r'\(x^3 - x^2 + x - 6 = (x - 2)(x^2 + x + 3)\). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Kiểm tra biệt thức phần bậc hai):</b> Với \(x^2 + x + 3 = 0\), ta có \(\Delta = 1^2 - 4(1)(3) = -11 < 0\) nên vô nghiệm thực. '
            r'Vậy phương trình \(f(x) = 0\) có đúng một nghiệm thực duy nhất là \(x = 2\). <b>[A1]</b></p>',
        ),
        _q(
            'Cubic with Irrational Roots (Non-Calc)',
            r'<p>Find all exact real solutions to the cubic equation \(2x^3 - 5x^2 - 2x + 2 = 0\).</p>',
            [
                r'\(x = \frac{1}{2}, \quad 1 + \sqrt{3}, \quad 1 - \sqrt{3}\)',
                r'\(x = \frac{1}{2}, \quad -1 + \sqrt{3}, \quad -1 - \sqrt{3}\)',
                r'\(x = -\frac{1}{2}, \quad 1 + \sqrt{3}, \quad 1 - \sqrt{3}\)',
                r'\(x = \frac{1}{2}, \quad 1 + \sqrt{2}, \quad 1 - \sqrt{2}\)',
            ],
            'A',
            r'<p><b>Bước 1 (Tìm nghiệm hữu tỉ bằng Factor Theorem):</b> Thử \(x = \frac{1}{2}\): '
            r'\(2\left(\frac{1}{8}\right) - 5\left(\frac{1}{4}\right) - 2\left(\frac{1}{2}\right) + 2 = \frac{1}{4} - \frac{5}{4} - 1 + 2 = 0 \implies (2x - 1)\) là nhân tử. '
            r'Chia đa thức: \(2x^3 - 5x^2 - 2x + 2 = (2x - 1)(x^2 - 2x - 2)\). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Giải phương trình bậc hai bằng hoàn thành bình phương):</b> '
            r'\(x^2 - 2x - 2 = 0 \implies (x - 1)^2 = 3 \implies x = 1 \pm \sqrt{3}\). '
            r'Tập nghiệm chính xác là \(x = \frac{1}{2}, \; 1 + \sqrt{3}, \; 1 - \sqrt{3}\). <b>[A1]</b></p>',
        ),
        _q(
            'Polynomial Long Division (Non-Calc)',
            r'<p>When \(3x^3 - 2x^2 + 4x - 2\) is divided by \((x - 1)\), it can be written as \((x - 1)Q(x) + R\). Find \(Q(x)\) and \(R\).</p>',
            [
                r'\(Q(x) = 3x^2 - 5x + 9, \quad R = 7\)',
                r'\(Q(x) = 3x^2 + x + 5, \quad R = -3\)',
                r'\(Q(x) = 3x^2 + x + 5, \quad R = 3\)',
                r'\(Q(x) = 3x^2 + x + 3, \quad R = 1\)',
            ],
            'C',
            r'<p><b>Bước 1 (Chia đa thức / So sánh hệ số):</b> Đặt \(3x^3 - 2x^2 + 4x - 2 = (x - 1)(3x^2 + bx + c) + R\). '
            r'Hệ số \(x^2\): \(b - 3 = -2 \implies b = 1\). Hệ số \(x\): \(c - b = 4 \implies c = 5\). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Tìm số dư \(R\)):</b> Hằng số: \(-c + R = -2 \implies R = 5 - 2 = 3\) (khớp \(P(1) = 3 - 2 + 4 - 2 = 3\)). '
            r'Vậy \(Q(x) = 3x^2 + x + 5\) và \(R = 3\). <b>[A1]</b></p>',
        ),
        _q(
            'Quadratic Divisor Remainder (Non-Calc)',
            r'<p>A polynomial \(P(x)\) leaves a remainder of \(7\) when divided by \((x - 1)\), and a remainder of \(-2\) when divided by \((x + 2)\). Find the remainder when \(P(x)\) is divided by \((x - 1)(x + 2)\).</p>',
            [
                r'\(3x + 4\)',
                r'\(3x - 4\)',
                r'\(-3x + 10\)',
                r'\(4x + 3\)',
            ],
            'A',
            r'<p><b>Bước 1 (Biểu diễn số dư bậc nhất):</b> Vì đa thức chia \((x - 1)(x + 2)\) có bậc \(2\), số dư có dạng \(Ax + B\): '
            r'\(P(x) = (x - 1)(x + 2)Q(x) + Ax + B\). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Thay \(x = 1\) và \(x = -2\)):</b> '
            r'\(P(1) = A + B = 7\) và \(P(-2) = -2A + B = -2\). '
            r'Trừ vế theo vế: \(3A = 9 \implies A = 3\), suy ra \(B = 4\). Vậy số dư là \(3x + 4\). <b>[A1]</b></p>',
        ),
        _q(
            'Cubic Inequality (Non-Calc)',
            r'<p>Solve the cubic inequality \((x + 3)(x - 1)(x - 4) \ge 0\).</p>',
            [
                r'\(x \le -3 \text{ or } 1 \le x \le 4\)',
                r'\(-3 < x < 1 \text{ or } x > 4\)',
                r'\(-3 \le x \le 4\)',
                r'\(-3 \le x \le 1 \text{ or } x \ge 4\)',
            ],
            'D',
            r'<p><b>Bước 1 (Xác định các nghiệm biên và dáng đồ thị bậc ba):</b> '
            r'Các nghiệm là \(x = -3, \; 1, \; 4\) và hệ số bậc cao nhất \(+1 > 0\) (nhánh phải đi lên \(+\infty\)). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Lập bảng xét dấu):</b> '
            r'\((-\infty, -3): -\); \([-3, 1]: +\); \((1, 4): -\); \([4, +\infty): +\). '
            r'Do lấy dấu \(\ge 0\), tập nghiệm là \(-3 \le x \le 1 \text{ or } x \ge 4\). <b>[A1]</b></p>',
        ),
        _q(
            'Cubic Inequality with Repeated Root (Non-Calc)',
            r'<p>Solve the inequality \((x - 2)^2(5 - x) > 0\).</p>',
            [
                r'\(x < 5\)',
                r'\(x < 2 \text{ or } 2 < x < 5\)',
                r'\(2 < x < 5\)',
                r'\(x > 5\)',
            ],
            'B',
            r'<p><b>Bước 1 (Phân tích nhân tử nghiệm kép):</b> Vì \((x - 2)^2 \ge 0\) với mọi \(x\), để tích lớn hơn hẳn \(0\) ta cần ĐỒNG THỜI \((x - 2)^2 > 0\) (tức \(x \ne 2\)) VÀ \(5 - x > 0\) (tức \(x < 5\)). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Kết luận chính xác):</b> Tập nghiệm là \(x < 5\) với \(x \ne 2\), viết chuẩn là \(x < 2 \text{ or } 2 < x < 5\). <b>[A1]</b></p>'
            r'<p><i>Bẫy Cambridge 0606:</i> Rất dễ chọn nhầm \(x < 5\) vì quên loại điểm tiếp xúc \(x = 2\) (nơi vế trái bằng \(0\)).</p>',
        ),
    ],
}


# =============================================================================
# DRILL 5 (Ch. 5): Simultaneous Equations, Modulus & Cubic Inequalities (Non-Calc)
# Answer balance: B, A, C, D, C, D, B, A, D, B, A, C (A:3, B:3, C:3, D:3)
# =============================================================================
_DRILL_C5 = {
    'code': 'd0606_c5',
    'folder_key': 'drills_p1',
    'lecture_key': 'c5',
    'calculator_policy': 'non-calculator',
    'order_index': 5,
    'title': 'Ch. 5 Drill: Simultaneous Equations, Modulus & Cubic Inequalities (0606)',
    'time_limit': '30',
    'intro_html': (
        r'<p><b>Mục tiêu Chapter 5 (Cambridge 0606 Paper 1 Non-Calculator):</b> '
        r'Giải hệ phương trình tuyến tính–phi tuyến (đường thẳng cắt đường tròn/parabol/hyperbol), giải phương trình và bất phương trình chứa dấu giá trị tuyệt đối '
        r'\(|2x-3|=|x+5|\), \(|2x-1|<5\), \(|x-2|<|2x+1|\), bất phương trình bậc ba và điều kiện tương giao bằng đồ thị.</p>'
    ),
    'questions': [
        _q(
            'Simultaneous Linear & Quadratic (Non-Calc)',
            r'<p>Solve the simultaneous equations \(y = 2x - 1\) and \(x^2 + y^2 = 13\).</p>',
            [
                r'\((2, 3) \text{ and } \left(\frac{6}{5}, \frac{7}{5}\right)\)',
                r'\((2, 3) \text{ and } \left(-\frac{6}{5}, -\frac{17}{5}\right)\)',
                r'\((-2, -5) \text{ and } \left(\frac{6}{5}, \frac{7}{5}\right)\)',
                r'\((2, 3) \text{ and } \left(-\frac{6}{5}, \frac{17}{5}\right)\)',
            ],
            'B',
            r'<p><b>Bước 1 (Thế \(y = 2x - 1\) vào phương trình bậc hai):</b> '
            r'\(x^2 + (2x - 1)^2 = 13 \implies x^2 + 4x^2 - 4x + 1 = 13 \implies 5x^2 - 4x - 12 = 0\). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Phân tích nhân tử và tìm \(y\) tương ứng):</b> '
            r'\((5x + 6)(x - 2) = 0 \implies x = 2 \text{ hoặc } x = -\frac{6}{5}\). '
            r'Với \(x = 2 \implies y = 2(2) - 1 = 3\); với \(x = -\frac{6}{5} \implies y = -\frac{12}{5} - 1 = -\frac{17}{5}\). '
            r'Vậy hai nghiệm là \((2, 3)\) và \(\left(-\frac{6}{5}, -\frac{17}{5}\right)\). <b>[A1]</b></p>',
        ),
        _q(
            'Simultaneous Line & Hyperbola (Non-Calc)',
            r'<p>Find the coordinates of the points of intersection of the line \(2x + y = 7\) and the curve \(xy = 6\).</p>',
            [
                r'\((2, 3) \text{ and } \left(\frac{3}{2}, 4\right)\)',
                r'\((3, 2) \text{ and } \left(4, \frac{3}{2}\right)\)',
                r'\((2, 3) \text{ and } \left(-\frac{3}{2}, 10\right)\)',
                r'\((2, 4) \text{ and } \left(\frac{3}{2}, 3\right)\)',
            ],
            'A',
            r'<p><b>Bước 1 (Thế \(y = 7 - 2x\) vào \(xy = 6\)):</b> '
            r'\(x(7 - 2x) = 6 \implies 2x^2 - 7x + 6 = 0 \implies (2x - 3)(x - 2) = 0\). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Tìm tọa độ từng giao điểm):</b> '
            r'Khi \(x = 2 \implies y = 7 - 4 = 3\); khi \(x = \frac{3}{2} \implies y = 7 - 3 = 4\). '
            r'Giao điểm là \((2, 3)\) và \(\left(\frac{3}{2}, 4\right)\). <b>[A1]</b></p>',
        ),
        _q(
            'Length Between Intersections (Non-Calc)',
            r'<p>The line \(y = x + 2\) intersects the curve \(y = x^2 - 2x - 2\) at points \(A\) and \(B\). Find the exact length of the line segment \(AB\).</p>',
            [
                r'\(5\)',
                r'\(10\)',
                r'\(5\sqrt{2}\)',
                r'\(3\sqrt{2}\)',
            ],
            'C',
            r'<p><b>Bước 1 (Tìm tọa độ \(A\) và \(B\)):</b> '
            r'\(x^2 - 2x - 2 = x + 2 \implies x^2 - 3x - 4 = 0 \implies (x - 4)(x + 1) = 0 \implies x = -1 \text{ hoặc } x = 4\). '
            r'Thay vào \(y = x + 2\): \(A(-1, 1)\) và \(B(4, 6)\). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Tính khoảng cách \(AB\)):</b> '
            r'\(AB = \sqrt{(4 - (-1))^2 + (6 - 1)^2} = \sqrt{25 + 25} = \sqrt{50} = 5\sqrt{2}\). <b>[A1]</b></p>',
        ),
        _q(
            'Modulus Equation |ax+b| = |cx+d| (Non-Calc)',
            r'<p>Solve the equation \(|2x - 3| = |x + 5|\).</p>',
            [
                r'\(x = 8 \text{ or } x = \frac{2}{3}\)',
                r'\(x = -8 \text{ or } x = \frac{2}{3}\)',
                r'\(x = 8 \text{ only}\)',
                r'\(x = 8 \text{ or } x = -\frac{2}{3}\)',
            ],
            'D',
            r'<p><b>Bước 1 (Tách hai trường hợp tương đương \(A = B\) hoặc \(A = -B\)):</b> '
            r'Trường hợp 1: \(2x - 3 = x + 5 \implies x = 8\). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Giải trường hợp còn lại):</b> '
            r'Trường hợp 2: \(2x - 3 = -(x + 5) = -x - 5 \implies 3x = -2 \implies x = -\frac{2}{3}\). '
            r'Cả hai giá trị đều thỏa mãn phương trình gốc. Vậy \(x = 8 \text{ or } x = -\frac{2}{3}\). <b>[A1]</b></p>',
        ),
        _q(
            'Modulus Equation Extraneous Check (Non-Calc)',
            r'<p>Solve the equation \(|x - 4| = 2x - 5\).</p>',
            [
                r'\(x = 1 \text{ or } x = 3\)',
                r'\(x = 1\)',
                r'\(x = 3\)',
                r'\(x = 3 \text{ or } x = 9\)',
            ],
            'C',
            r'<p><b>Bước 1 (Đặt điều kiện vế phải không âm và xét 2 trường hợp):</b> Vì \(|x - 4| \ge 0\), cần \(2x - 5 \ge 0 \implies x \ge \frac{5}{2}\). '
            r'TH1: \(x - 4 = 2x - 5 \implies x = 1\); TH2: \(-(x - 4) = 2x - 5 \implies 3x = 9 \implies x = 3\). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Thử lại để loại nghiệm ngoại lai):</b> '
            r'Với \(x = 1\): \(|1 - 4| = 3 \ne 2(1) - 5 = -3\) (loại!). '
            r'Với \(x = 3\): \(|3 - 4| = 1 = 2(3) - 5\) (thỏa mãn). Vậy nghiệm duy nhất là \(x = 3\). <b>[A1]</b></p>',
        ),
        _q(
            'Modulus Inequality |ax+b| < c (Non-Calc)',
            r'<p>Solve the inequality \(|2x - 1| < 5\).</p>',
            [
                r'\(x < -2 \text{ or } x > 3\)',
                r'\(-3 < x < 2\)',
                r'\(-2 \le x \le 3\)',
                r'\(-2 < x < 3\)',
            ],
            'D',
            r'<p><b>Bước 1 (Viết dạng bất đẳng thức kép):</b> '
            r'\(|2x - 1| < 5 \iff -5 < 2x - 1 < 5\). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Cô lập \(x\)):</b> Cộng \(1\) vào cả ba vế: \(-4 < 2x < 6\). '
            r'Chia cho \(2\): \(-2 < x < 3\). <b>[A1]</b></p>',
        ),
        _q(
            'Modulus Inequality |ax+b| >= c (Non-Calc)',
            r'<p>Solve the inequality \(|3x + 2| \ge 7\).</p>',
            [
                r'\(-3 \le x \le \frac{5}{3}\)',
                r'\(x \le -3 \text{ or } x \ge \frac{5}{3}\)',
                r'\(x \le -\frac{5}{3} \text{ or } x \ge 3\)',
                r'\(x < -3 \text{ or } x > \frac{5}{3}\)',
            ],
            'B',
            r'<p><b>Bước 1 (Tách hai nhánh ngoài):</b> '
            r'\(|3x + 2| \ge 7 \iff 3x + 2 \le -7 \text{ hoặc } 3x + 2 \ge 7\). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Giải từng bất phương trình):</b> '
            r'\(3x \le -9 \implies x \le -3\), hoặc \(3x \ge 5 \implies x \ge \frac{5}{3}\). '
            r'Vậy \(x \le -3 \text{ or } x \ge \frac{5}{3}\). <b>[A1]</b></p>',
        ),
        _q(
            'Modulus Inequality Both Sides (Non-Calc)',
            r'<p>Solve the inequality \(|x - 2| < |2x + 1|\).</p>',
            [
                r'\(x < -3 \text{ or } x > \frac{1}{3}\)',
                r'\(-3 < x < \frac{1}{3}\)',
                r'\(x < -\frac{1}{3} \text{ or } x > 3\)',
                r'\(-\frac{1}{3} < x < 3\)',
            ],
            'A',
            r'<p><b>Bước 1 (Bình phương hai vế không âm):</b> '
            r'\((x - 2)^2 < (2x + 1)^2 \implies x^2 - 4x + 4 < 4x^2 + 4x + 1 \implies 3x^2 + 8x - 3 > 0\). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Phân tích nhân tử và chọn miền):</b> '
            r'\((3x - 1)(x + 3) > 0 \implies x < -3 \text{ or } x > \frac{1}{3}\). <b>[A1]</b></p>',
        ),
        _q(
            'Modulus of Quadratic Equation (Non-Calc)',
            r'<p>Find the sum of all real solutions to the equation \(|x^2 - 5x + 4| = 2\).</p>',
            [
                r'\(5\)',
                r'\(6\)',
                r'\(8\)',
                r'\(10\)',
            ],
            'D',
            r'<p><b>Bước 1 (Xét hai trường hợp và kiểm tra \(\Delta > 0\)):</b> '
            r'TH1: \(x^2 - 5x + 4 = 2 \implies x^2 - 5x + 2 = 0\), có \(\Delta_1 = 25 - 8 = 17 > 0\) (2 nghiệm thực phân biệt, tổng \(S_1 = 5\)). '
            r'TH2: \(x^2 - 5x + 4 = -2 \implies x^2 - 5x + 6 = 0 \implies (x - 2)(x - 3) = 0\) (2 nghiệm thực \(2, 3\), tổng \(S_2 = 5\)). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Cộng tổng cả 4 nghiệm thực phân biệt):</b> '
            r'Tổng tất cả các nghiệm thực là \(S_1 + S_2 = 5 + 5 = 10\). <b>[A1]</b></p>',
        ),
        _q(
            'Cubic Inequality by Factoring (Non-Calc)',
            r'<p>Solve the cubic inequality \(x^3 - 2x^2 - 8x < 0\).</p>',
            [
                r'\(-2 < x < 0 \text{ or } x > 4\)',
                r'\(x < -2 \text{ or } 0 < x < 4\)',
                r'\(-2 < x < 4\)',
                r'\(x < -4 \text{ or } 0 < x < 2\)',
            ],
            'B',
            r'<p><b>Bước 1 (Đặt nhân tử chung và phân tích hết):</b> '
            r'\(x(x^2 - 2x - 8) < 0 \implies x(x - 4)(x + 2) < 0\). Các nghiệm biên là \(-2, \; 0, \; 4\). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Lập bảng xét dấu với hệ số \(x^3\) dương):</b> '
            r'Tích âm trên \((-\infty, -2)\) và \((0, 4)\). Vậy \(x < -2 \text{ or } 0 < x < 4\). <b>[A1]</b></p>',
        ),
        _q(
            'Graphical Intersection Condition (Non-Calc)',
            r'<p>The graph of \(y = |x^2 - 6x + 5|\) and the horizontal line \(y = k\) intersect at <b>exactly 4 distinct points</b>. Find the range of values of \(k\).</p>',
            [
                r'\(0 < k < 4\)',
                r'\(0 \le k \le 4\)',
                r'\(k > 4\)',
                r'\(0 < k < 5\)',
            ],
            'A',
            r'<p><b>Bước 1 (Xác định đỉnh lật của đồ thị \(y = |x^2 - 6x + 5|\)):</b> '
            r'\(x^2 - 6x + 5 = (x - 1)(x - 5) = (x - 3)^2 - 4\). Đỉnh parabol gốc là \((3, -4)\). '
            r'Sau khi lấy trị tuyệt đối, đỉnh lật lên thành cực đại địa phương \((3, 4)\), còn giao trục \(Ox\) tại \((1, 0)\) và \((5, 0)\). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Biện luận số giao điểm với đường ngang \(y = k\)):</b> '
            r'Tại \(k = 0\) có 2 giao điểm; tại \(k = 4\) có 3 giao điểm; với \(k > 4\) có 2 giao điểm. '
            r'Để có đúng 4 giao điểm phân biệt, đường ngang phải cắt giữa trục \(Ox\) và đỉnh cực đại: \(0 < k < 4\). <b>[A1]</b></p>',
        ),
        _q(
            'Non-Intersection Condition (Non-Calc)',
            r'<p>Find the range of values of \(k\) for which the line \(y = 3x + k\) does not intersect the curve \(y = 2 - \frac{3}{x}\) (\(x \ne 0\)).</p>',
            [
                r'\(k < -4 \text{ or } k > 8\)',
                r'\(-8 < k < 4\)',
                r'\(-4 < k < 8\)',
                r'\(-4 \le k \le 8\)',
            ],
            'C',
            r'<p><b>Bước 1 (Khử mẫu tạo phương trình bậc hai):</b> '
            r'\(3x + k = 2 - \frac{3}{x} \implies 3x^2 + (k - 2)x + 3 = 0\) (với \(x \ne 0\), luôn thỏa mãn vì hệ số tự do \(3 \ne 0\)). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Điều kiện không giao nhau \(\Delta < 0\)):</b> '
            r'\((k - 2)^2 - 4(3)(3) < 0 \implies (k - 2)^2 < 36 \implies -6 < k - 2 < 6 \implies -4 < k < 8\). <b>[A1]</b></p>',
        ),
    ],
}


# =============================================================================
# DRILL 6 (Ch. 6): Logarithmic & Exponential Functions (Calculator Allowed)
# Answer balance: A, D, B, C, B, A, D, C, C, B, D, A (A:3, B:3, C:3, D:3)
# =============================================================================
_DRILL_C6 = {
    'code': 'd0606_c6',
    'folder_key': 'drills_p1',
    'lecture_key': 'c6',
    'calculator_policy': 'calculator',
    'order_index': 6,
    'title': 'Ch. 6 Drill: Logarithmic & Exponential Functions (0606)',
    'time_limit': '30',
    'intro_html': (
        r'<p><b>Mục tiêu Chapter 6 (Cambridge 0606 Paper 2 Calculator):</b> '
        r'Vận dụng thành thạo quy tắc logarit, công thức đổi cơ số \(\log_4 x + \log_2 x = 6\), giải phương trình mũ ẩn phụ '
        r'\(2^{2x+1}-5(2^x)+2=0\) và \(e^{2x}-7e^x+10=0\), khảo sát tiệm cận & hàm ngược của \(y = ae^{bx}+c\) và \(y = \ln(ax+b)\), cùng mô hình tăng trưởng/phân rã mũ.</p>'
    ),
    'questions': [
        _q(
            'Laws of Logarithms (Calc)',
            r'<p>Solve the equation \(\lg(2x + 1) - \lg(x - 2) = 1\), where \(\lg\) denotes \(\log_{10}\).</p>',
            [
                r'\(x = \frac{21}{8}\)',
                r'\(x = \frac{19}{8}\)',
                r'\(x = 3\)',
                r'\(x = \frac{7}{4}\)',
            ],
            'A',
            r'<p><b>Bước 1 (Áp dụng quy tắc hiệu logarit):</b> '
            r'\(\lg\left(\frac{2x + 1}{x - 2}\right) = 1 \implies \frac{2x + 1}{x - 2} = 10^1 = 10\). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Giải và kiểm tra điều kiện \(x > 2\)):</b> '
            r'\(2x + 1 = 10x - 20 \implies 8x = 21 \implies x = \frac{21}{8} = 2.625 > 2\) (thỏa mãn). <b>[A1]</b></p>',
        ),
        _q(
            'Log Equation Extraneous Root (Calc)',
            r'<p>Solve the equation \(\log_2(x + 2) + \log_2(x - 1) = 2\).</p>',
            [
                r'\(x = -3 \text{ or } x = 2\)',
                r'\(x = 3\)',
                r'\(x = -2 \text{ or } x = 3\)',
                r'\(x = 2\)',
            ],
            'D',
            r'<p><b>Bước 1 (Gộp logarit cùng cơ số \(2\)):</b> '
            r'\(\log_2\left[(x + 2)(x - 1)\right] = 2 \implies (x + 2)(x - 1) = 2^2 = 4 \implies x^2 + x - 6 = 0\). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Giải và loại nghiệm ngoài miền xác định):</b> '
            r'\((x + 3)(x - 2) = 0 \implies x = -3 \text{ hoặc } x = 2\). '
            r'Điều kiện logarit: \(x - 1 > 0 \implies x > 1\), nên loại \(x = -3\) và nhận \(x = 2\). <b>[A1]</b></p>',
        ),
        _q(
            'Change of Base (Calc)',
            r'<p>Solve the equation \(\log_4 x + \log_2 x = 6\) for \(x > 0\).</p>',
            [
                r'\(x = 8\)',
                r'\(x = 16\)',
                r'\(x = 32\)',
                r'\(x = 64\)',
            ],
            'B',
            r'<p><b>Bước 1 (Đổi về cùng cơ số \(2\)):</b> '
            r'\(\log_4 x = \frac{\log_2 x}{\log_2 4} = \frac{1}{2}\log_2 x\). '
            r'Phương trình trở thành \(\frac{1}{2}\log_2 x + \log_2 x = 6 \implies \frac{3}{2}\log_2 x = 6\). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Giải tìm \(x\)):</b> \(\log_2 x = 4 \implies x = 2^4 = 16\). <b>[A1]</b></p>',
        ),
        _q(
            'Reciprocal Change of Base (Calc)',
            r'<p>Solve the equation \(\log_3 x - 2\log_x 3 = 1\) for \(x > 0, \; x \ne 1\).</p>',
            [
                r'\(x = 9 \text{ only}\)',
                r'\(x = 3 \text{ or } x = \frac{1}{9}\)',
                r'\(x = 9 \text{ or } x = \frac{1}{3}\)',
                r'\(x = 2 \text{ or } x = -1\)',
            ],
            'C',
            r'<p><b>Bước 1 (Dùng tính chất \(\log_x 3 = \frac{1}{\log_3 x}\)):</b> Đặt \(u = \log_3 x\): '
            r'\(u - \frac{2}{u} = 1 \implies u^2 - u - 2 = 0 \implies (u - 2)(u + 1) = 0 \implies u = 2 \text{ hoặc } u = -1\). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Tìm \(x\) cho cả hai trường hợp):</b> '
            r'\(\log_3 x = 2 \implies x = 3^2 = 9\); \(\log_3 x = -1 \implies x = 3^{-1} = \frac{1}{3}\) (đều \(> 0, \ne 1\)). <b>[A1]</b></p>',
        ),
        _q(
            'Exponential Quadratic Base 2 (Calc)',
            r'<p>Solve the equation \(2^{2x + 1} - 5(2^x) + 2 = 0\).</p>',
            [
                r'\(x = \frac{1}{2} \text{ or } x = 2\)',
                r'\(x = -1 \text{ or } x = 1\)',
                r'\(x = 0 \text{ or } x = 1\)',
                r'\(x = -2 \text{ or } x = 1\)',
            ],
            'B',
            r'<p><b>Bước 1 (Đặt \(u = 2^x > 0\)):</b> Do \(2^{2x+1} = 2(2^x)^2\), ta có '
            r'\(2u^2 - 5u + 2 = 0 \implies (2u - 1)(u - 2) = 0 \implies u = \frac{1}{2} \text{ hoặc } u = 2\). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Tìm \(x\)):</b> \(2^x = \frac{1}{2} = 2^{-1} \implies x = -1\), và \(2^x = 2^1 \implies x = 1\). <b>[A1]</b></p>',
        ),
        _q(
            'Exponential Quadratic Base e (Calc)',
            r'<p>Solve the equation \(e^{2x} - 7e^x + 10 = 0\), giving your answers correct to 3 significant figures.</p>',
            [
                r'\(x = 0.693 \text{ or } x = 1.61\)',
                r'\(x = 0.301 \text{ or } x = 0.699\)',
                r'\(x = 2.00 \text{ or } x = 5.00\)',
                r'\(x = 0.693 \text{ or } x = 1.60\)',
            ],
            'A',
            r'<p><b>Bước 1 (Phân tích nhân tử theo \(e^x\)):</b> '
            r'\((e^x - 2)(e^x - 5) = 0 \implies e^x = 2 \text{ hoặc } e^x = 5\). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Lấy logarit tự nhiên \(\ln\) và làm tròn 3 s.f.):</b> '
            r'\(x = \ln 2 = 0.6931\ldots \approx 0.693\), và \(x = \ln 5 = 1.6094\ldots \approx 1.61\). <b>[A1]</b></p>',
        ),
        _q(
            'Different Bases Exponential Equation (Calc)',
            r'<p>Solve the equation \(3^{x + 1} = 5^{2x - 1}\), giving \(x\) correct to 3 significant figures.</p>',
            [
                r'\(x = 0.783\)',
                r'\(x = 1.27\)',
                r'\(x = 2.12\)',
                r'\(x = 1.28\)',
            ],
            'D',
            r'<p><b>Bước 1 (Lấy \(\ln\) hai vế):</b> '
            r'\((x + 1)\ln 3 = (2x - 1)\ln 5 \implies x\ln 3 + \ln 3 = 2x\ln 5 - \ln 5\). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Cô lập \(x\) và bấm máy làm tròn 3 s.f.):</b> '
            r'\(x(2\ln 5 - \ln 3) = \ln 3 + \ln 5 \implies x = \frac{\ln 15}{\ln(25/3)} = \frac{2.70805\ldots}{2.12026\ldots} = 1.2772\ldots \approx 1.28\). <b>[A1]</b></p>',
        ),
        _q(
            'Exponential Graph & Asymptote (Calc)',
            r'<p>For the curve \(y = 4e^{-2x} - 3\), state the equation of its horizontal asymptote and the exact coordinates of its \(x\)-intercept.</p>',
            [
                r'Asymptote \(y = 4\); \(x\)-intercept \(\left(\frac{1}{2}\ln\frac{4}{3}, 0\right)\)',
                r'Asymptote \(y = -3\); \(x\)-intercept \(\left(-\frac{1}{2}\ln\frac{4}{3}, 0\right)\)',
                r'Asymptote \(y = -3\); \(x\)-intercept \(\left(\frac{1}{2}\ln\frac{4}{3}, 0\right)\)',
                r'Asymptote \(x = -3\); \(x\)-intercept \(\left(\ln\frac{4}{3}, 0\right)\)',
            ],
            'C',
            r'<p><b>Bước 1 (Tìm tiệm cận ngang):</b> Khi \(x \to +\infty\), \(e^{-2x} \to 0 \implies y \to -3\). Vậy tiệm cận ngang là \(y = -3\). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Tìm giao điểm trục \(Ox\) khi \(y = 0\)):</b> '
            r'\(4e^{-2x} - 3 = 0 \implies e^{-2x} = \frac{3}{4} \implies -2x = \ln\left(\frac{3}{4}\right) \implies x = -\frac{1}{2}\ln\left(\frac{3}{4}\right) = \frac{1}{2}\ln\left(\frac{4}{3}\right)\). '
            r'Giao điểm trục \(Ox\) là \(\left(\frac{1}{2}\ln\frac{4}{3}, 0\right)\). <b>[A1]</b></p>',
        ),
        _q(
            'Logarithmic Asymptote & Inverse (Calc)',
            r'<p>Given \(f(x) = \ln(3x - 6)\) for \(x > 2\), state the equation of its vertical asymptote and find \(f^{-1}(x)\).</p>',
            [
                r'Asymptote \(y = 2\); \(f^{-1}(x) = \frac{e^x + 6}{3}\)',
                r'Asymptote \(x = 2\); \(f^{-1}(x) = 3e^x + 6\)',
                r'Asymptote \(x = 2\); \(f^{-1}(x) = \frac{e^x + 6}{3}\)',
                r'Asymptote \(x = 6\); \(f^{-1}(x) = \frac{e^x - 6}{3}\)',
            ],
            'C',
            r'<p><b>Bước 1 (Tìm tiệm cận đứng):</b> Biểu thức trong \(\ln\) tiến về \(0^+\) khi \(3x - 6 = 0 \implies x = 2\). Tiệm cận đứng là đường thẳng \(x = 2\). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Tìm hàm ngược \(f^{-1}(x)\)):</b> Đặt \(y = \ln(3x - 6) \implies e^y = 3x - 6 \implies x = \frac{e^y + 6}{3}\). '
            r'Vậy \(f^{-1}(x) = \frac{e^x + 6}{3}\) với \(x \in \mathbb{R}\). <b>[A1]</b></p>',
        ),
        _q(
            'Exponential Decay Modelling (Calc)',
            r'<p>The mass \(M\) grams of a radioactive substance after \(t\) days is modelled by \(M = 200e^{-0.04t}\). Find the number of days, correct to 3 significant figures, for the mass to decrease to \(80\text{ g}\).</p>',
            [
                r'\(9.95\text{ days}\)',
                r'\(22.9\text{ days}\)',
                r'\(17.3\text{ days}\)',
                r'\(25.0\text{ days}\)',
            ],
            'B',
            r'<p><b>Bước 1 (Thay \(M = 80\) và rút gọn):</b> '
            r'\(80 = 200e^{-0.04t} \implies e^{-0.04t} = \frac{80}{200} = 0.4\). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Lấy \(\ln\) hai vế và tính 3 s.f.):</b> '
            r'\(-0.04t = \ln(0.4) \implies t = \frac{\ln(0.4)}{-0.04} = 25\ln(2.5) = 22.907\ldots \approx 22.9\text{ days}\). <b>[A1]</b></p>',
        ),
        _q(
            'Logarithmic Manipulation in p, q (Calc)',
            r'<p>Given that \(\log_a 2 = p\) and \(\log_a 3 = q\), express \(\log_a\left(\frac{24}{\sqrt{a}}\right)\) in terms of \(p\) and \(q\).</p>',
            [
                r'\(3p + q + \frac{1}{2}\)',
                r'\(2p + 3q - \frac{1}{2}\)',
                r'\(\frac{3p + q}{2}\)',
                r'\(3p + q - \frac{1}{2}\)',
            ],
            'D',
            r'<p><b>Bước 1 (Phân tích thừa số nguyên tố và tách logarit):</b> '
            r'\(\log_a\left(\frac{24}{\sqrt{a}}\right) = \log_a(2^3 \times 3) - \log_a\left(a^{\frac{1}{2}}\right)\). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Thay \(\log_a 2 = p, \; \log_a 3 = q, \; \log_a a = 1\)):</b> '
            r'\(3\log_a 2 + \log_a 3 - \frac{1}{2}\log_a a = 3p + q - \frac{1}{2}\). <b>[A1]</b></p>',
        ),
        _q(
            'Simultaneous Log Equations (Calc)',
            r'<p>Solve the simultaneous equations \(\log_2(x - y) = 2\) and \(\log_2 x + \log_2 y = 5\), where \(x > y > 0\).</p>',
            [
                r'\(x = 8, \quad y = 4\)',
                r'\(x = 4, \quad y = 8\)',
                r'\(x = 16, \quad y = 2\)',
                r'\(x = 8, \; y = 4 \text{ or } x = -4, \; y = -8\)',
            ],
            'A',
            r'<p><b>Bước 1 (Chuyển hai phương trình logarit sang đại số):</b> '
            r'\(x - y = 2^2 = 4 \implies x = y + 4\), và \(\log_2(xy) = 5 \implies xy = 2^5 = 32\). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Giải và lọc điều kiện \(x > y > 0\)):</b> '
            r'\((y + 4)y = 32 \implies y^2 + 4y - 32 = 0 \implies (y + 8)(y - 4) = 0\). '
            r'Vì \(y > 0\) nên loại \(y = -8\), nhận \(y = 4 \implies x = 8\). <b>[A1]</b></p>',
        ),
    ],
}


# =============================================================================
# DRILL 7 (Ch. 7): Straight Line Graphs & Linear Law Transformation (Calculator)
# Answer balance: C, B, A, D, A, D, C, B, B, C, A, D (A:3, B:3, C:3, D:3)
# =============================================================================
_DRILL_C7 = {
    'code': 'd0606_c7',
    'folder_key': 'drills_p1',
    'lecture_key': 'c7',
    'calculator_policy': 'calculator',
    'order_index': 7,
    'title': 'Ch. 7 Drill: Straight Line Graphs & Linear Law Transformation (0606)',
    'time_limit': '30',
    'intro_html': (
        r'<p><b>Mục tiêu Chapter 7 (Cambridge 0606 Paper 2 Calculator):</b> '
        r'Lập phương trình đường trung trực (perpendicular bisector), tính diện tích đa giác bằng công thức tọa độ (shoelace formula), '
        r'và tuyến tính hóa (Linear Law) các quan hệ phi tuyến \(y = Ax^n\), \(y = Ab^x\), \(y = ax^2 + bx\), \(y = \frac{a}{x+b}\) về dạng \(Y = mX + c\) để xác định hằng số từ hệ số góc và tung độ gốc.</p>'
    ),
    'questions': [
        _q(
            'Perpendicular Bisector (Calc)',
            r'<p>Find the equation of the perpendicular bisector of the line segment joining \(A(-2, 5)\) and \(B(6, 1)\), giving your answer in the form \(y = mx + c\).</p>',
            [
                r'\(y = -\frac{1}{2}x + 4\)',
                r'\(y = 2x + 1\)',
                r'\(y = 2x - 1\)',
                r'\(y = -2x + 7\)',
            ],
            'C',
            r'<p><b>Bước 1 (Tìm trung điểm và hệ số góc vuông góc):</b> '
            r'Trung điểm \(M = \left(\frac{-2 + 6}{2}, \frac{5 + 1}{2}\right) = (2, 3)\). '
            r'Hệ số góc \(m_{AB} = \frac{1 - 5}{6 - (-2)} = -\frac{1}{2} \implies m_{\perp} = 2\). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Viết phương trình đường thẳng qua \(M(2, 3)\)):</b> '
            r'\(y - 3 = 2(x - 2) \implies y = 2x - 1\). <b>[A1]</b></p>',
        ),
        _q(
            'Parallelogram Vertex (Calc)',
            r'<p>Points \(A(1, 2)\), \(B(5, 4)\), and \(D(3, 6)\) are three vertices of a parallelogram \(ABCD\). Find the coordinates of vertex \(C\).</p>',
            [
                r'\((9, 12)\)',
                r'\((7, 8)\)',
                r'\((3, 0)\)',
                r'\((-1, 4)\)',
            ],
            'B',
            r'<p><b>Bước 1 (Dùng tính chất trung điểm hai đường chéo trùng nhau):</b> '
            r'Trong hình bình hành \(ABCD\), trung điểm \(AC\) trùng với trung điểm \(BD\): '
            r'\(\left(\frac{1 + x_C}{2}, \frac{2 + y_C}{2}\right) = \left(\frac{5 + 3}{2}, \frac{4 + 6}{2}\right) = (4, 5)\). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Tìm tọa độ \(C\)):</b> \(x_C = 8 - 1 = 7\), \(y_C = 10 - 2 = 8\). Vậy \(C(7, 8)\). <b>[A1]</b></p>',
        ),
        _q(
            'Shoelace Area of Quadrilateral (Calc)',
            r'<p>Find the exact area of the quadrilateral \(ABCD\) with vertices \(A(1, 1)\), \(B(5, 2)\), \(C(6, 7)\), and \(D(2, 5)\) taken in anticlockwise order.</p>',
            [
                r'\(16.5\text{ units}^2\)',
                r'\(33\text{ units}^2\)',
                r'\(18.5\text{ units}^2\)',
                r'\(14.5\text{ units}^2\)',
            ],
            'A',
            r'<p><b>Bước 1 (Áp dụng công thức Shoelace theo thứ tự ngược chiều kim đồng hồ):</b> '
            r'\(\text{Area} = \frac{1}{2}\left|(x_1 y_2 + x_2 y_3 + x_3 y_4 + x_4 y_1) - (y_1 x_2 + y_2 x_3 + y_3 x_4 + y_4 x_1)\right|\). '
            r'Tổng chéo xuống: \(1(2) + 5(7) + 6(5) + 2(1) = 2 + 35 + 30 + 2 = 69\). '
            r'Tổng chéo lên: \(1(5) + 2(6) + 7(2) + 5(1) = 5 + 12 + 14 + 5 = 36\). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Tính diện tích):</b> \(\text{Area} = \frac{1}{2}|69 - 36| = \frac{33}{2} = 16.5\text{ units}^2\). <b>[A1]</b></p>',
        ),
        _q(
            'Perpendicular Bisector Intersection (Calc)',
            r'<p>The perpendicular bisector of the line segment joining \(P(0, 2)\) and \(Q(6, 4)\) meets the line \(y = x + 4\) at point \(R\). Find the coordinates of \(R\).</p>',
            [
                r'\((3, 7)\)',
                r'\((4, 8)\)',
                r'\((1, 5)\)',
                r'\((2, 6)\)',
            ],
            'D',
            r'<p><b>Bước 1 (Tìm phương trình trung trực \(PQ\)):</b> '
            r'Trung điểm \(M = (3, 3)\), \(m_{PQ} = \frac{4 - 2}{6 - 0} = \frac{1}{3} \implies m_{\perp} = -3\). '
            r'Đường trung trực: \(y - 3 = -3(x - 3) \implies y = -3x + 12\). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Tìm giao điểm \(R\) với \(y = x + 4\)):</b> '
            r'\(x + 4 = -3x + 12 \implies 4x = 8 \implies x = 2 \implies y = 6\). Vậy \(R(2, 6)\). <b>[A1]</b></p>',
        ),
        _q(
            'Unknown Vertex from Triangle Area (Calc)',
            r'<p>A triangle has vertices \(A(1, 2)\), \(B(5, 4)\), and \(C(k, 10)\) taken in anticlockwise order. Given that the area of \(\triangle ABC\) is \(14\text{ units}^2\), find the value of \(k\).</p>',
            [
                r'\(k = 3\)',
                r'\(k = 6\)',
                r'\(k = 10\)',
                r'\(k = 31\)',
            ],
            'A',
            r'<p><b>Bước 1 (Lập biểu thức diện tích Shoelace):</b> '
            r'\(\text{Area} = \frac{1}{2}\left[(1 \cdot 4 + 5 \cdot 10 + k \cdot 2) - (2 \cdot 5 + 4 \cdot k + 10 \cdot 1)\right] = \frac{1}{2}\left[(54 + 2k) - (20 + 4k)\right] = 17 - k\). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Giải tìm \(k\)):</b> \(17 - k = 14 \implies k = 3\). <b>[A1]</b></p>',
        ),
        _q(
            'Linear Law: y = Axⁿ (Calc)',
            r'<p>Variables \(x\) and \(y\) are related by \(y = Ax^n\), where \(A\) and \(n\) are constants. When \(\ln y\) is plotted against \(\ln x\), a straight line passes through the points \((1, 4)\) and \((3, 10)\). Find the exact values of \(n\) and \(A\).</p>',
            [
                r'\(n = 3, \quad A = 1\)',
                r'\(n = 2, \quad A = e^2\)',
                r'\(n = 3, \quad A = e^4\)',
                r'\(n = 3, \quad A = e\)',
            ],
            'D',
            r'<p><b>Bước 1 (Lấy \(\ln\) hai vế để tuyến tính hóa):</b> '
            r'\(\ln y = n\ln x + \ln A\), dạng \(Y = mX + c\) với hệ số góc \(m = n\) và tung độ gốc \(c = \ln A\). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Tính \(n\) và \(A\) từ 2 điểm):</b> '
            r'\(n = \frac{10 - 4}{3 - 1} = 3\). Thay \((1, 4)\): \(4 = 3(1) + \ln A \implies \ln A = 1 \implies A = e\). <b>[A1]</b></p>',
        ),
        _q(
            'Linear Law: y = Abˣ (Calc)',
            r'<p>Variables \(x\) and \(y\) are related by \(y = Ab^x\). When \(\lg y\) (base 10) is plotted against \(x\), a straight line passes through \((2, 1.4)\) and \((6, 2.6)\). Find the values of \(A\) and \(b\) correct to 3 significant figures.</p>',
            [
                r'\(A = 0.800, \quad b = 0.300\)',
                r'\(A = 2.23, \quad b = 1.35\)',
                r'\(A = 6.31, \quad b = 2.00\)',
                r'\(A = 25.1, \quad b = 2.00\)',
            ],
            'C',
            r'<p><b>Bước 1 (Tuyến tính hóa với logarit thập phân \(\lg\)):</b> '
            r'\(\lg y = (\lg b)x + \lg A\). '
            r'Hệ số góc \(\lg b = \frac{2.6 - 1.4}{6 - 2} = 0.3\). '
            r'Tung độ gốc \(\lg A = 1.4 - 0.3(2) = 0.8\). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Giải mũ cơ số \(10\) và làm tròn 3 s.f.):</b> '
            r'\(b = 10^{0.3} = 1.9952\ldots \approx 2.00\), và \(A = 10^{0.8} = 6.3095\ldots \approx 6.31\). <b>[A1]</b></p>',
        ),
        _q(
            'Linear Law: y = ax² + bx (Calc)',
            r'<p>Variables \(x\) and \(y\) satisfy \(y = ax^2 + bx\) (\(x \ne 0\)). When \(\frac{y}{x}\) is plotted against \(x\), a straight line passes through \((2, 11)\) and \((5, 20)\). Find the values of \(a\) and \(b\).</p>',
            [
                r'\(a = 5, \quad b = 3\)',
                r'\(a = 3, \quad b = 5\)',
                r'\(a = 3, \quad b = 11\)',
                r'\(a = \frac{1}{3}, \quad b = 5\)',
            ],
            'B',
            r'<p><b>Bước 1 (Chia hai vế cho \(x\)):</b> '
            r'\(\frac{y}{x} = ax + b\). Khi vẽ \(\frac{y}{x}\) theo \(x\), hệ số góc là \(a\) và tung độ gốc là \(b\). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Tính \(a\) và \(b\)):</b> '
            r'\(a = \frac{20 - 11}{5 - 2} = \frac{9}{3} = 3\). Thay \((2, 11)\): \(11 = 3(2) + b \implies b = 5\). <b>[A1]</b></p>',
        ),
        _q(
            'Linear Law: Reciprocal Form (Calc)',
            r'<p>Variables \(x\) and \(y\) are connected by \(y = \frac{a}{x + b}\). When \(\frac{1}{y}\) is plotted against \(x\), the resulting straight line has gradient \(\frac{1}{4}\) and passes through \((2, 2)\). Find the values of \(a\) and \(b\).</p>',
            [
                r'\(a = \frac{1}{4}, \quad b = \frac{3}{2}\)',
                r'\(a = 4, \quad b = 6\)',
                r'\(a = 4, \quad b = \frac{3}{2}\)',
                r'\(a = 4, \quad b = 2\)',
            ],
            'B',
            r'<p><b>Bước 1 (Nghịch đảo hai vế):</b> '
            r'\(\frac{1}{y} = \frac{x + b}{a} = \frac{1}{a}x + \frac{b}{a}\). So sánh với \(Y = mX + c\): '
            r'\(\frac{1}{a} = \frac{1}{4} \implies a = 4\). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Thay điểm \((2, 2)\) tìm \(b\)):</b> '
            r'\(2 = \frac{1}{4}(2) + \frac{b}{4} \implies 2 - \frac{1}{2} = \frac{b}{4} \implies \frac{b}{4} = \frac{3}{2} \implies b = 6\). <b>[A1]</b></p>',
        ),
        _q(
            'Linear Law: Reading Transformed Axes (Calc)',
            r'<p>A straight-line graph is obtained by plotting \(y^2\) on the vertical axis against \(\frac{1}{x}\) on the horizontal axis. The line passes through \((2, 17)\) and \((5, 29)\). Find the positive value of \(y\) when \(x = \frac{1}{4}\).</p>',
            [
                r'\(y = 3.16\)',
                r'\(y = 25\)',
                r'\(y = 5\)',
                r'\(y = 4.47\)',
            ],
            'C',
            r'<p><b>Bước 1 (Tìm phương trình đường thẳng \(Y = mX + c\) với \(Y = y^2, \; X = \frac{1}{x}\)):</b> '
            r'\(m = \frac{29 - 17}{5 - 2} = 4\); \(c = 17 - 4(2) = 9\). '
            r'Vậy \(y^2 = \frac{4}{x} + 9\). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Thay \(x = \frac{1}{4} \implies \frac{1}{x} = 4\)):</b> '
            r'\(y^2 = 4(4) + 9 = 25 \implies y = 5\) (nhận giá trị dương). <b>[A1]</b></p>',
        ),
        _q(
            'Linear Law: Exponential Decay (Calc)',
            r'<p>Variables \(x\) and \(y\) satisfy \(y = Ae^{kx}\). When \(\ln y\) is plotted against \(x\), a straight line passes through \((0, 2.5)\) and \((5, 0.5)\). Find \(A\) (to 3 s.f.) and the exact value of \(k\).</p>',
            [
                r'\(A = 12.2, \quad k = -0.4\)',
                r'\(A = 2.50, \quad k = -0.4\)',
                r'\(A = 12.2, \quad k = 0.4\)',
                r'\(A = 316, \quad k = -0.4\)',
            ],
            'A',
            r'<p><b>Bước 1 (Tuyến tính hóa bằng \(\ln\)):</b> '
            r'\(\ln y = kx + \ln A\). Hệ số góc \(k = \frac{0.5 - 2.5}{5 - 0} = -\frac{2}{5} = -0.4\). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Tìm \(A\) từ tung độ gốc \(\ln A = 2.5\)):</b> '
            r'\(A = e^{2.5} = 12.182\ldots \approx 12.2\). <b>[A1]</b></p>',
        ),
        _q(
            'Linear Law: Choosing Axes (Calc)',
            r'<p>Variables \(x\) and \(y\) satisfy \(y = px^2 + \frac{q}{x}\) (\(x \ne 0\)). To obtain a straight-line graph whose gradient is \(p\) and vertical-axis intercept is \(q\), which variables should be plotted on the vertical (\(Y\)) and horizontal (\(X\)) axes?</p>',
            [
                r'\(Y = y\) against \(X = x^2\)',
                r'\(Y = \frac{y}{x^2}\) against \(X = \frac{1}{x^3}\)',
                r'\(Y = xy\) against \(X = x^2\)',
                r'\(Y = xy\) against \(X = x^3\)',
            ],
            'D',
            r'<p><b>Bước 1 (Biến đổi phương trình về dạng \(Y = pX + q\)):</b> '
            r'Nhân cả hai vế của \(y = px^2 + \frac{q}{x}\) với \(x\): \(xy = px^3 + q\). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Đối chiếu với \(Y = mX + c\)):</b> '
            r'Chọn trục tung \(Y = xy\) và trục hoành \(X = x^3\), khi đó hệ số góc \(m = p\) và tung độ gốc \(c = q\). '
            r'(Nếu chia cho \(x^2\) sẽ được \(\frac{y}{x^2} = q\cdot\frac{1}{x^3} + p\), khi đó hệ số góc bị đảo thành \(q\)). <b>[A1]</b></p>',
        ),
    ],
}


# =============================================================================
# DRILL 8 (Ch. 7B): Coordinate Geometry of the Circle (NEW 2025–2027, Non-Calc)
# Answer balance: D, A, B, C, A, C, B, D, B, D, A, C (A:3, B:3, C:3, D:3)
# =============================================================================
_DRILL_C7B = {
    'code': 'd0606_c7b',
    'folder_key': 'drills_p1',
    'lecture_key': 'c7b',
    'calculator_policy': 'non-calculator',
    'order_index': 8,
    'title': 'Ch. 7B Drill: Coordinate Geometry of the Circle (NEW 2025–2027) (0606)',
    'time_limit': '30',
    'intro_html': (
        r'<p><b>Chuyên đề MỚI BẮT BUỘC Cambridge 0606 (2025–2027 Syllabus — Paper 1 Non-Calculator):</b> '
        r'Phương trình chuẩn \((x-a)^2+(y-b)^2=r^2\), hoàn thành bình phương \(x^2+y^2+2gx+2fy+c=0\), lập phương trình đường tròn từ đường kính, '
        r'phương trình tiếp tuyến (tangent) & pháp tuyến (normal) tại \(P\), xét tương giao đường thẳng–đường tròn bằng biệt thức \(\Delta\), '
        r'tính độ dài dây cung & tiếp tuyến bằng Pythagoras, và điều kiện hai đường tròn tiếp xúc ngoài / tiếp xúc trong.</p>'
    ),
    'questions': [
        _q(
            'Circle Standard Form (NEW 2025+)',
            r'<p>A circle has centre \(C(3, -2)\) and passes through the point \(P(7, 1)\). Find the equation of the circle in standard form.</p>',
            [
                r'\((x - 3)^2 + (y + 2)^2 = 5\)',
                r'\((x + 3)^2 + (y - 2)^2 = 25\)',
                r'\((x - 7)^2 + (y - 1)^2 = 25\)',
                r'\((x - 3)^2 + (y + 2)^2 = 25\)',
            ],
            'D',
            r'<p><b>Bước 1 (Tính bình phương bán kính \(r^2 = CP^2\)):</b> '
            r'\(r^2 = (7 - 3)^2 + (1 - (-2))^2 = 4^2 + 3^2 = 16 + 9 = 25\). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Thay tâm \((a, b) = (3, -2)\) và \(r^2 = 25\) vào \((x - a)^2 + (y - b)^2 = r^2\)):</b> '
            r'\((x - 3)^2 + (y + 2)^2 = 25\). <b>[A1]</b></p>',
        ),
        _q(
            'General Form to Centre & Radius (NEW 2025+)',
            r'<p>Find the centre and exact radius of the circle with equation \(x^2 + y^2 - 8x + 6y - 11 = 0\).</p>',
            [
                r'Centre \((4, -3)\), radius \(6\)',
                r'Centre \((-4, 3)\), radius \(6\)',
                r'Centre \((4, -3)\), radius \(\sqrt{14}\)',
                r'Centre \((8, -6)\), radius \(6\)',
            ],
            'A',
            r'<p><b>Bước 1 (Hoàn thành bình phương cho cả \(x\) và \(y\)):</b> '
            r'\((x - 4)^2 - 16 + (y + 3)^2 - 9 - 11 = 0 \implies (x - 4)^2 + (y + 3)^2 = 36\). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Đọc tâm và bán kính):</b> Tâm \(C(4, -3)\) và bán kính \(r = \sqrt{36} = 6\). <b>[A1]</b></p>',
        ),
        _q(
            'Scaled General Circle Equation (NEW 2025+)',
            r'<p>Find the centre and exact radius of the circle \(2x^2 + 2y^2 + 12x - 8y + 6 = 0\).</p>',
            [
                r'Centre \((-6, 4)\), radius \(\sqrt{46}\)',
                r'Centre \((-3, 2)\), radius \(\sqrt{10}\)',
                r'Centre \((3, -2)\), radius \(\sqrt{10}\)',
                r'Centre \((-3, 2)\), radius \(4\)',
            ],
            'B',
            r'<p><b>Bước 1 (Chia hai vế cho \(2\) TRƯỚC khi hoàn thành bình phương):</b> '
            r'\(x^2 + y^2 + 6x - 4y + 3 = 0 \implies (x + 3)^2 - 9 + (y - 2)^2 - 4 + 3 = 0\). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Rút gọn):</b> \((x + 3)^2 + (y - 2)^2 = 10\). '
            r'Vậy tâm \((-3, 2)\) và bán kính chính xác \(r = \sqrt{10}\). <b>[A1]</b></p>',
        ),
        _q(
            'Circle from Diameter Endpoints (NEW 2025+)',
            r'<p>The points \(A(-1, 6)\) and \(B(5, -2)\) are the endpoints of a diameter of a circle. Find the equation of the circle.</p>',
            [
                r'\((x - 2)^2 + (y - 2)^2 = 100\)',
                r'\((x + 2)^2 + (y + 2)^2 = 25\)',
                r'\((x - 2)^2 + (y - 2)^2 = 25\)',
                r'\((x - 3)^2 + (y - 4)^2 = 25\)',
            ],
            'C',
            r'<p><b>Bước 1 (Tìm tâm là trung điểm đường kính \(AB\)):</b> '
            r'\(C = \left(\frac{-1 + 5}{2}, \frac{6 + (-2)}{2}\right) = (2, 2)\). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Tính \(r^2 = CA^2\) và lập phương trình):</b> '
            r'\(r^2 = (2 - (-1))^2 + (2 - 6)^2 = 9 + 16 = 25\). '
            r'Phương trình đường tròn: \((x - 2)^2 + (y - 2)^2 = 25\). <b>[A1]</b></p>',
        ),
        _q(
            'Tangent to Circle at Point P (NEW 2025+)',
            r'<p>A circle has equation \((x - 2)^2 + (y + 1)^2 = 25\). Find the equation of the tangent to the circle at the point \(P(5, 3)\).</p>',
            [
                r'\(3x + 4y = 27\)',
                r'\(4x - 3y = 11\)',
                r'\(3x - 4y = 3\)',
                r'\(3x + 4y = 25\)',
            ],
            'A',
            r'<p><b>Bước 1 (Tính hệ số góc bán kính \(CP\) và tiếp tuyến vuông góc):</b> '
            r'Tâm \(C(2, -1)\), \(m_{CP} = \frac{3 - (-1)}{5 - 2} = \frac{4}{3}\). '
            r'Do tiếp tuyến vuông góc bán kính tại tiếp điểm \(P\), ta có \(m_{\text{tangent}} = -\frac{3}{4}\). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Viết phương trình tiếp tuyến qua \(P(5, 3)\)):</b> '
            r'\(y - 3 = -\frac{3}{4}(x - 5) \implies 4y - 12 = -3x + 15 \implies 3x + 4y = 27\). <b>[A1]</b></p>',
        ),
        _q(
            'Normal to Circle at Point P (NEW 2025+)',
            r'<p>Find the equation of the normal to the circle \(x^2 + y^2 - 4x - 6y - 12 = 0\) at the point \(P(6, 0)\).</p>',
            [
                r'\(4x - 3y = 24\)',
                r'\(3x - 4y = 18\)',
                r'\(3x + 4y = 18\)',
                r'\(4x + 3y = 24\)',
            ],
            'C',
            r'<p><b>Bước 1 (Tìm tâm đường tròn — pháp tuyến luôn đi qua tâm!):</b> '
            r'\((x - 2)^2 + (y - 3)^2 = 25 \implies\) tâm \(C(2, 3)\). '
            r'Hệ số góc pháp tuyến \(CP\): \(m_{CP} = \frac{0 - 3}{6 - 2} = -\frac{3}{4}\). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Lập phương trình đường thẳng qua \(P(6, 0)\)):</b> '
            r'\(y - 0 = -\frac{3}{4}(x - 6) \implies 4y = -3x + 18 \implies 3x + 4y = 18\). <b>[A1]</b></p>',
        ),
        _q(
            'Line Tangent via Discriminant (NEW 2025+)',
            r'<p>The line \(y = x + k\) is a tangent to the circle \(x^2 + y^2 = 18\). Find the two possible values of \(k\).</p>',
            [
                r'\(k = \pm 3\sqrt{2}\)',
                r'\(k = \pm 6\)',
                r'\(k = \pm 9\)',
                r'\(k = \pm 18\)',
            ],
            'B',
            r'<p><b>Bước 1 (Thế \(y = x + k\) vào phương trình đường tròn):</b> '
            r'\(x^2 + (x + k)^2 = 18 \implies 2x^2 + 2kx + (k^2 - 18) = 0\). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Áp dụng điều kiện tiếp xúc \(\Delta = 0\)):</b> '
            r'\((2k)^2 - 4(2)(k^2 - 18) = 0 \implies 4k^2 - 8k^2 + 144 = 0 \implies 4k^2 = 144 \implies k^2 = 36 \implies k = \pm 6\). <b>[A1]</b></p>',
        ),
        _q(
            'Line Intersects Circle at 2 Points (NEW 2025+)',
            r'<p>Find the range of values of \(c\) for which the line \(y = 2x + c\) intersects the circle \((x - 1)^2 + y^2 = 5\) at two distinct points.</p>',
            [
                r'\(c < -7 \text{ or } c > 3\)',
                r'\(-3 < c < 7\)',
                r'\(-7 \le c \le 3\)',
                r'\(-7 < c < 3\)',
            ],
            'D',
            r'<p><b>Bước 1 (Lập phương trình hoành độ giao điểm):</b> '
            r'\((x - 1)^2 + (2x + c)^2 = 5 \implies 5x^2 + (4c - 2)x + (c^2 - 4) = 0\). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Giải điều kiện \(\Delta > 0\)):</b> '
            r'\((4c - 2)^2 - 4(5)(c^2 - 4) > 0 \implies -4c^2 - 16c + 84 > 0 \implies c^2 + 4c - 21 < 0 \implies (c + 7)(c - 3) < 0 \implies -7 < c < 3\). <b>[A1]</b></p>',
        ),
        _q(
            'Chord Length via Pythagoras (NEW 2025+)',
            r'<p>The line \(x + y = 7\) intersects the circle \((x - 1)^2 + (y - 2)^2 = 16\) at points \(A\) and \(B\). Find the exact length of the chord \(AB\).</p>',
            [
                r'\(2\sqrt{2}\)',
                r'\(4\sqrt{2}\)',
                r'\(8\)',
                r'\(2\sqrt{6}\)',
            ],
            'B',
            r'<p><b>Bước 1 (Tìm tọa độ giao điểm \(A, B\) hoặc khoảng cách từ tâm đến dây cung):</b> '
            r'Thế \(y = 7 - x\): \((x - 1)^2 + (5 - x)^2 = 16 \implies 2x^2 - 12x + 10 = 0 \implies (x - 1)(x - 5) = 0\), cho \(A(1, 6)\) và \(B(5, 2)\). '
            r'(Hoặc bằng Pythagoras: tâm \(C(1, 2)\), trung điểm \(M(3, 4)\), \(CM = \sqrt{8}\), nửa dây cung \(= \sqrt{4^2 - 8} = 2\sqrt{2}\)). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Tính độ dài dây cung \(AB\)):</b> '
            r'\(AB = \sqrt{(5 - 1)^2 + (2 - 6)^2} = \sqrt{32} = 4\sqrt{2}\) (gấp đôi nửa dây cung \(2\sqrt{2}\)). <b>[A1]</b></p>',
        ),
        _q(
            'External Tangent Length (NEW 2025+)',
            r'<p>A tangent is drawn from the external point \(T(10, 5)\) to the circle \((x - 2)^2 + (y + 1)^2 = 36\), touching the circle at point \(Q\). Find the exact length of \(TQ\).</p>',
            [
                r'\(10\)',
                r'\(4\)',
                r'\(\sqrt{136}\)',
                r'\(8\)',
            ],
            'D',
            r'<p><b>Bước 1 (Tìm khoảng cách từ tâm \(C(2, -1)\) tới \(T(10, 5)\)):</b> '
            r'\(CT = \sqrt{(10 - 2)^2 + (5 - (-1))^2} = \sqrt{64 + 36} = \sqrt{100} = 10\), và bán kính \(r = \sqrt{36} = 6\). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Áp dụng Pythagoras trong tam giác vuông \(CQT\) vuông tại \(Q\)):</b> '
            r'\(TQ = \sqrt{CT^2 - r^2} = \sqrt{10^2 - 6^2} = \sqrt{64} = 8\). <b>[A1]</b></p>',
        ),
        _q(
            'Circles Touching Externally (NEW 2025+)',
            r'<p>Circle \(C_1\) has equation \((x - 1)^2 + (y - 2)^2 = 9\) and Circle \(C_2\) has equation \((x - 7)^2 + (y - 10)^2 = k^2\) (\(k > 0\)). Given that the two circles touch <b>externally</b>, find the value of \(k\).</p>',
            [
                r'\(k = 7\)',
                r'\(k = 13\)',
                r'\(k = 1\)',
                r'\(k = 49\)',
            ],
            'A',
            r'<p><b>Bước 1 (Tính khoảng cách giữa hai tâm \(O_1(1, 2)\) và \(O_2(7, 10)\)):</b> '
            r'\(d = O_1O_2 = \sqrt{(7 - 1)^2 + (10 - 2)^2} = \sqrt{36 + 64} = 10\). Bán kính lần lượt là \(r_1 = 3\) và \(r_2 = k\). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Điều kiện tiếp xúc ngoài \(d = r_1 + r_2\)):</b> '
            r'\(10 = 3 + k \implies k = 7\). <b>[A1]</b></p>',
        ),
        _q(
            'Circles Touching Internally (NEW 2025+)',
            r'<p>Circle \(C_1\) has centre \((-2, 1)\) and radius \(4\). Circle \(C_2\) has centre \((1, 5)\) and radius \(R\) (where \(R > 4\)). Given that \(C_1\) lies inside \(C_2\) and the two circles touch <b>internally</b>, find the value of \(R\).</p>',
            [
                r'\(R = 1\)',
                r'\(R = 5\)',
                r'\(R = 9\)',
                r'\(R = 20\)',
            ],
            'C',
            r'<p><b>Bước 1 (Tính khoảng cách giữa hai tâm):</b> '
            r'\(d = \sqrt{(1 - (-2))^2 + (5 - 1)^2} = \sqrt{9 + 16} = 5\). <b>[M1]</b></p>'
            r'<p><b>Bước 2 (Điều kiện tiếp xúc trong \(d = |R - r_1|\) với \(R > 4\)):</b> '
            r'\(5 = R - 4 \implies R = 9\). '
            r'(<i>Lưu ý:</i> nếu nhầm sang tiếp xúc ngoài \(R + 4 = 5\) sẽ ra đáp án sai \(R = 1\)). <b>[A1]</b></p>',
        ),
    ],
}


DRILLS_0606_P1 = [
    _DRILL_C1,
    _DRILL_C2,
    _DRILL_C3,
    _DRILL_C4,
    _DRILL_C5,
    _DRILL_C6,
    _DRILL_C7,
    _DRILL_C7B,
]


# =============================================================================
# PROGRAMMATIC MATHEMATICAL & SCHEMA VERIFICATION (ALL 96 QUESTIONS)
# =============================================================================
def _opt(drill_idx, q_num):
    """Returns (answer_letter, chosen_option_text) for 1-indexed q_num."""
    q = DRILLS_0606_P1[drill_idx]['questions'][q_num - 1]
    ans = q['answer']
    idx = {'A': 0, 'B': 1, 'C': 2, 'D': 3}[ans]
    return ans, q['options'][idx]


def verify_all_math():
    """
    Independently verifies EVERY SINGLE mathematical calculation across all 96 questions
    using exact Python arithmetic (Fraction, math) AND validates all 8 drills through
    `build_igcse_drill_json` + `validate_igcse_drill`.
    """
    # -------------------------------------------------------------------------
    # 1. STRUCTURAL, METADATA, BALANCE & KATEX HYGIENE CHECKS
    # -------------------------------------------------------------------------
    assert len(DRILLS_0606_P1) == 8, f'Expected 8 drills, got {len(DRILLS_0606_P1)}'
    expected_meta = [
        ('d0606_c1', 'c1', 'non-calculator', 1),
        ('d0606_c2', 'c2', 'non-calculator', 2),
        ('d0606_c3', 'c3', 'non-calculator', 3),
        ('d0606_c4', 'c4', 'non-calculator', 4),
        ('d0606_c5', 'c5', 'non-calculator', 5),
        ('d0606_c6', 'c6', 'calculator', 6),
        ('d0606_c7', 'c7', 'calculator', 7),
        ('d0606_c7b', 'c7b', 'non-calculator', 8),
    ]
    bad_ctrl_re = re.compile(r'[\x07\x08\x09\x0b\x0c\x0d]')
    prefix_re = re.compile(r'^\s*[A-D]\s*[\.\)]\s*')
    total_q = 0

    for d, (exp_code, exp_lec, exp_pol, exp_ord) in zip(DRILLS_0606_P1, expected_meta):
        assert d['code'] == exp_code
        assert d['folder_key'] == 'drills_p1'
        assert d['lecture_key'] == exp_lec
        assert d['calculator_policy'] == exp_pol
        assert d['order_index'] == exp_ord
        assert d['time_limit'] == '30'
        assert '$' not in d['intro_html'], f"{exp_code}: raw $ in intro_html"
        assert not bad_ctrl_re.search(d['intro_html']), f"{exp_code}: control char in intro_html"

        qs = d['questions']
        assert len(qs) == 12, f"{exp_code}: expected 12 questions, got {len(qs)}"
        total_q += len(qs)

        counts = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
        for i, q in enumerate(qs, start=1):
            counts[q['answer']] += 1
            assert '[M1]' in q['explanation'] and '[A1]' in q['explanation'], (
                f"{exp_code} Q{i}: missing [M1]/[A1] tags"
            )
            for field_name, txt in [('q', q['q']), ('explanation', q['explanation'])] + [
                (f'opt{j}', o) for j, o in enumerate(q['options'])
            ]:
                assert '$' not in txt, f"{exp_code} Q{i} {field_name}: raw $ found"
                assert not bad_ctrl_re.search(txt), (
                    f"{exp_code} Q{i} {field_name}: accidental escape/control char"
                )
            for j, o in enumerate(q['options']):
                assert not prefix_re.match(o), (
                    f"{exp_code} Q{i} opt{j}: forbidden option letter prefix in {o!r}"
                )

        assert counts == {'A': 3, 'B': 3, 'C': 3, 'D': 3}, (
            f"{exp_code}: answer distribution must be exactly 3 each, got {counts}"
        )

        # Validate through production pipeline builder & validator (no Supabase calls)
        cj = build_igcse_drill_json(
            title=d['title'],
            course_id=COURSE_0606_ID,
            calculator_policy=d['calculator_policy'],
            syllabus_code='0606',
            intro_html=d['intro_html'],
            questions=qs,
            time_limit=d['time_limit'],
        )
        errs = validate_igcse_drill(cj, title=d['code'])
        assert not errs, f"Pipeline validation failed for {d['code']}: {errs}"

    assert total_q == 96, f'Expected 96 questions total, got {total_q}'

    # -------------------------------------------------------------------------
    # 2. DRILL 1 (Ch. 1) — ALL 12 QUESTIONS MATH VERIFICATION
    # -------------------------------------------------------------------------
    # Q1: f(x) = 2x^2 - 12x + 23 = 2(x - 3)^2 + 5 -> vertex x = 3
    for x in (-2, 0, 3, 5):
        assert 2 * x * x - 12 * x + 23 == 2 * (x - 3) ** 2 + 5
    assert Fraction(12, 2 * 2) == 3
    assert _opt(0, 1) == ('B', r'\(k = 3\)')

    # Q2: f(x) = 7 + 4x - x^2 = -(x - 2)^2 + 11 on x >= 3 -> max at x = 3 is 10
    f2 = lambda x: 7 + 4 * x - x * x
    assert f2(3) == 10
    assert all(f2(x) < f2(3) for x in (4, 5, 10, 100))
    assert _opt(0, 2) == ('D', r'\(f(x) \le 10\)')

    # Q3: g(x) = 5 - 3e^(2x) -> g(x) < 5 strictly for all real x
    g3 = lambda x: 5 - 3 * math.exp(2 * x)
    assert all(g3(x) < 5 for x in (-10, -1, 0, 1, 5))
    assert math.isclose(g3(-50), 5.0, rel_tol=1e-12)
    assert _opt(0, 3) == ('A', r'\(g(x) < 5\)')

    # Q4: f(x) = (3x+1)/(x-2), g(x) = 2x+1, fg(x) = 4 -> x = 4
    f4 = lambda x: Fraction(3 * x + 1, x - 2)
    g4 = lambda x: 2 * x + 1
    assert f4(g4(4)) == 4
    assert _opt(0, 4) == ('C', r'\(x = 4\)')

    # Q5: f(x) = 3x - 5 (x >= 2), g(x) = sqrt(x - 4) (x >= 4) -> 3x - 5 >= 4 => x >= 3
    assert 3 * 3 - 5 == 4 and 3 >= 2
    assert _opt(0, 5) == ('D', r'\(x \ge 3\)')

    # Q6: f(x) = (x - 4)^2 + 3 for x <= 4 -> f^-1(x) = 4 - sqrt(x - 3), x >= 3
    f6 = lambda x: (x - 4) ** 2 + 3
    finv6 = lambda y: 4 - math.sqrt(y - 3)
    for x in (-5.0, 0.0, 2.5, 4.0):
        assert math.isclose(finv6(f6(x)), x, abs_tol=1e-12)
    assert _opt(0, 6) == ('A', r'\(f^{-1}(x) = 4 - \sqrt{x - 3}, \quad x \ge 3\)')

    # Q7: h(x) = (2x - 5)/(x + 3) -> h^-1(x) = (3x + 5)/(2 - x)
    h7 = lambda x: Fraction(2 * x - 5, x + 3)
    hinv7 = lambda y: Fraction(3 * y + 5, 2 - y)
    for x in (Fraction(-2), Fraction(0), Fraction(1), Fraction(7, 2)):
        assert hinv7(h7(x)) == x
    assert _opt(0, 7) == ('B', r'\(h^{-1}(x) = \frac{3x + 5}{2 - x}, \quad x \ne 2\)')

    # Q8: f(x) = x^2 - 6x + 10 for x >= 3 -> f(x) = x => (x-2)(x-5)=0; reject 2, accept 5
    f8 = lambda x: x * x - 6 * x + 10
    finv8 = lambda y: 3 + math.sqrt(y - 1)
    assert f8(5) == 5 and math.isclose(finv8(5), 5.0)
    assert f8(2) == 2 and not math.isclose(finv8(2), 2.0)  # 2 not in domain x >= 3
    assert _opt(0, 8) == ('C', r'\(x = 5\)')

    # Q9: f(x) = 2 ln(x - 3) + 1 -> f^-1(x) = 3 + e^((x-1)/2)
    f9 = lambda x: 2 * math.log(x - 3) + 1
    finv9 = lambda y: 3 + math.exp((y - 1) / 2)
    for x in (3.5, 4.0, 10.0):
        assert math.isclose(finv9(f9(x)), x, abs_tol=1e-12)
    assert _opt(0, 9) == ('A', r'\(f^{-1}(x) = 3 + e^{\frac{x - 1}{2}}\)')

    # Q10: f(x) = 8 - |2x - 6| on [0, 8] -> max = 8 at x=3, min = -2 at x=8
    f10 = lambda x: 8 - abs(2 * x - 6)
    vals10 = [f10(i / 2) for i in range(0, 17)]
    assert max(vals10) == 8 and min(vals10) == -2
    assert _opt(0, 10) == ('D', r'\(-2 \le f(x) \le 8\)')

    # Q11: y = |x^2 - 4x - 5| -> roots -1, 5; original vertex (2, -9) -> reflected (2, 9)
    q11 = lambda x: x * x - 4 * x - 5
    assert q11(-1) == 0 and q11(5) == 0 and q11(2) == -9 and abs(q11(2)) == 9
    assert _opt(0, 11) == ('C', r'Local max \((2, 9)\); \(x\)-intercepts \((-1, 0)\) and \((5, 0)\)')

    # Q12: f(x) = |3x - 7|, g(x) = x^2 - 2 -> fg(-2) - gf(1) = 1 - 14 = -13
    f12 = lambda x: abs(3 * x - 7)
    g12 = lambda x: x * x - 2
    assert f12(g12(-2)) - g12(f12(1)) == -13
    assert _opt(0, 12) == ('B', r'\(-13\)')

    # -------------------------------------------------------------------------
    # 3. DRILL 2 (Ch. 2) — ALL 12 QUESTIONS MATH VERIFICATION
    # -------------------------------------------------------------------------
    # Q1: 3x^2 - 12x + 7 = 3(x - 2)^2 - 5
    for x in (-3, 0, 2, 5):
        assert 3 * x * x - 12 * x + 7 == 3 * (x - 2) ** 2 - 5
    assert _opt(1, 1) == ('C', r'\(3(x - 2)^2 - 5\)')

    # Q2: 5 - 8x - 2x^2 = 13 - 2(x + 2)^2 -> max 13 at x = -2
    for x in (-4, -2, 0, 3):
        assert 5 - 8 * x - 2 * x * x == 13 - 2 * (x + 2) ** 2
    assert _opt(1, 2) == ('A', r'Maximum \(13\) at \(x = -2\)')

    # Q3: max of 12 / (2x^2 - 12x + 21) = 12 / (2(x-3)^2 + 3) = 4
    denom3 = lambda x: 2 * x * x - 12 * x + 21
    assert denom3(3) == 3 and Fraction(12, denom3(3)) == 4
    assert all(denom3(x) >= 3 for x in range(-10, 15))
    assert _opt(1, 3) == ('D', r'\(4\)')

    # Q4: x^2 + (k-2)x + k+1 = 0 no real roots -> Delta = k^2 - 8k < 0 -> 0 < k < 8
    delta4 = lambda k: (k - 2) ** 2 - 4 * (k + 1)
    assert delta4(0) == 0 and delta4(8) == 0 and delta4(4) < 0 and delta4(-1) > 0 and delta4(9) > 0
    assert _opt(1, 4) == ('B', r'\(0 < k < 8\)')

    # Q5: y = 2x + c tangent to y = x^2 - 4x + 7 -> x^2 - 6x + (7-c) = 0 -> Delta = 36 - 4(7-c)=0 -> c = -2
    c5 = Fraction(4 * 7 - 36, 4)
    assert c5 == -2
    assert (-6) ** 2 - 4 * (7 - c5) == 0
    assert _opt(1, 5) == ('A', r'\(c = -2\)')

    # Q6: y = mx - 3 meets y = x^2 + x + 1 at 2 points -> (1-m)^2 - 16 > 0 -> m < -3 or m > 5
    delta6 = lambda m: (1 - m) ** 2 - 16
    assert delta6(-3) == 0 and delta6(5) == 0 and delta6(-4) > 0 and delta6(6) > 0 and delta6(1) < 0
    assert _opt(1, 6) == ('C', r'\(m < -3 \text{ or } m > 5\)')

    # Q7: y = kx^2 + 4x + k > 0 for all x -> k > 0 and 16 - 4k^2 < 0 -> k > 2
    assert all(3 * x * x + 4 * x + 3 > 0 for x in (-10, -1, 0, 1, 10))
    assert (-3) * 0 + 4 * 0 + (-3) < 0  # k = -3 lies below x-axis!
    assert _opt(1, 7) == ('D', r'\(k > 2\)')

    # Q8: 15 + 2x - x^2 >= 0 -> -3 <= x <= 5
    p8 = lambda x: 15 + 2 * x - x * x
    assert p8(-3) == 0 and p8(5) == 0 and p8(0) > 0 and p8(-4) < 0 and p8(6) < 0
    assert _opt(1, 8) == ('B', r'\(-3 \le x \le 5\)')

    # Q9: (2x-1)(x+3) > x^2 + 11 -> x^2 + 5x - 14 > 0 -> x < -7 or x > 2
    p9 = lambda x: (2 * x - 1) * (x + 3) - (x * x + 11)
    assert p9(-7) == 0 and p9(2) == 0 and p9(-8) > 0 and p9(3) > 0 and p9(0) < 0
    assert _opt(1, 9) == ('D', r'\(x < -7 \text{ or } x > 2\)')

    # Q10: x^(2/3) - 5x^(1/3) + 6 = 0 -> x = 8 or 27
    for x in (8, 27):
        u = round(x ** (1 / 3))
        assert u ** 3 == x and u ** 2 - 5 * u + 6 == 0
    assert _opt(1, 10) == ('A', r'\(x = 8 \text{ or } x = 27\)')

    # Q11: e^(2x) - 2e^x - 15 = 0 -> e^x = 5 -> x = ln 5
    x11 = math.log(5)
    assert math.isclose(math.exp(2 * x11) - 2 * math.exp(x11) - 15, 0.0, abs_tol=1e-12)
    assert _opt(1, 11) == ('B', r'\(x = \ln 5\)')

    # Q12: 2x - 7sqrt(x) - 15 = 0 -> x = 25 only (x = 9/4 is extraneous)
    assert 2 * 25 - 7 * 5 - 15 == 0
    assert 2 * Fraction(9, 4) - 7 * Fraction(3, 2) - 15 != 0
    assert _opt(1, 12) == ('C', r'\(x = 25\)')

    # -------------------------------------------------------------------------
    # 4. DRILL 3 (Ch. 3) — ALL 12 QUESTIONS MATH VERIFICATION
    # -------------------------------------------------------------------------
    # Q1: (11 + 3sqrt(5)) / (3 - sqrt(5)) = 12 + 5sqrt(5)
    assert math.isclose((11 + 3 * math.sqrt(5)) / (3 - math.sqrt(5)), 12 + 5 * math.sqrt(5), rel_tol=1e-12)
    assert _opt(2, 1) == ('A', r'\(12 + 5\sqrt{5}\)')

    # Q2: (6 - sqrt(3)) / (2sqrt(3) - 3) = 4 + 3sqrt(3)
    assert math.isclose((6 - math.sqrt(3)) / (2 * math.sqrt(3) - 3), 4 + 3 * math.sqrt(3), rel_tol=1e-12)
    assert _opt(2, 2) == ('C', r'\(4 + 3\sqrt{3}\)')

    # Q3: Trapezium parallel sides (3+sqrt(2)), (5+3sqrt(2)), area (16+6sqrt(2)) -> h = 5 - sqrt(2)
    a3, b3 = 3 + math.sqrt(2), 5 + 3 * math.sqrt(2)
    area3 = 16 + 6 * math.sqrt(2)
    h3 = 2 * area3 / (a3 + b3)
    assert math.isclose(h3, 5 - math.sqrt(2), rel_tol=1e-12)
    assert _opt(2, 3) == ('B', r'\((5 - \sqrt{2})\text{ cm}\)')

    # Q4: Right triangle legs sqrt(11)+sqrt(7), sqrt(11)-sqrt(7) -> hyp = 6, perimeter = 6 + 2sqrt(11)
    l1, l2 = math.sqrt(11) + math.sqrt(7), math.sqrt(11) - math.sqrt(7)
    hyp4 = math.hypot(l1, l2)
    assert math.isclose(hyp4, 6.0, rel_tol=1e-12)
    assert math.isclose(l1 + l2 + hyp4, 6 + 2 * math.sqrt(11), rel_tol=1e-12)
    assert _opt(2, 4) == ('D', r'\((6 + 2\sqrt{11})\text{ cm}\)')

    # Q5: x sqrt(5) - 4 = 2x + sqrt(5) -> x = 13 + 6sqrt(5)
    x5 = 13 + 6 * math.sqrt(5)
    assert math.isclose(x5 * math.sqrt(5) - 4, 2 * x5 + math.sqrt(5), rel_tol=1e-12)
    assert _opt(2, 5) == ('C', r'\(x = 13 + 6\sqrt{5}\)')

    # Q6: sqrt(2x + 7) = x - 4 -> x = 9 only (x = 1 fails)
    assert math.isclose(math.sqrt(2 * 9 + 7), 9 - 4)
    assert not math.isclose(math.sqrt(2 * 1 + 7), 1 - 4)
    assert _opt(2, 6) == ('B', r'\(x = 9\)')

    # Q7: sqrt(75) + 18/sqrt(3) - sqrt(48) = 7sqrt(3)
    assert math.isclose(math.sqrt(75) + 18 / math.sqrt(3) - math.sqrt(48), 7 * math.sqrt(3), rel_tol=1e-12)
    assert _opt(2, 7) == ('A', r'\(7\sqrt{3}\)')

    # Q8: 9^x - 4(3^x) + 3 = 0 -> x = 0 or 1
    for x in (0, 1):
        assert 9 ** x - 4 * (3 ** x) + 3 == 0
    assert _opt(2, 8) == ('D', r'\(x = 0 \text{ or } x = 1\)')

    # Q9: 2^(2x+1) - 9(2^x) + 4 = 0 -> x = -1 or 2
    for x in (-1, 2):
        assert math.isclose(2 ** (2 * x + 1) - 9 * (2 ** x) + 4, 0.0, abs_tol=1e-12)
    assert _opt(2, 9) == ('B', r'\(x = -1 \text{ or } x = 2\)')

    # Q10: (27/8)^(-2/3) + 16^(3/4) - 81^(1/4) = 4/9 + 8 - 3 = 49/9
    val10 = Fraction(2, 3) ** 2 + 8 - 3
    assert val10 == Fraction(49, 9)
    assert math.isclose((27 / 8) ** (-2 / 3) + 16 ** 0.75 - 81 ** 0.25, 49 / 9, rel_tol=1e-12)
    assert _opt(2, 10) == ('D', r'\(\frac{49}{9}\)')

    # Q11: 4^x * 2^y = 32 and 9^x / 3^y = 27 -> x = 2, y = 1
    assert 4 ** 2 * 2 ** 1 == 32 and Fraction(9 ** 2, 3 ** 1) == 27
    assert _opt(2, 11) == ('C', r'\(x = 2, \quad y = 1\)')

    # Q12: 2^(3x-1) * 8^(x+2) / 4^(2x) = sqrt(2) -> 2x + 5 = 1/2 -> x = -9/4
    x12 = Fraction(-9, 4)
    assert (3 * x12 - 1) + 3 * (x12 + 2) - 4 * x12 == Fraction(1, 2)
    assert _opt(2, 12) == ('A', r'\(x = -\frac{9}{4}\)')

    # -------------------------------------------------------------------------
    # 5. DRILL 4 (Ch. 4) — ALL 12 QUESTIONS MATH VERIFICATION
    # -------------------------------------------------------------------------
    # Q1: P(2) for 2x^3 - 5x^2 + 3x - 7 = -5
    assert 2 * 8 - 5 * 4 + 3 * 2 - 7 == -5
    assert _opt(3, 1) == ('D', r'\(-5\)')

    # Q2: f(1/2) = 0 for 4x^3 + kx^2 - 5x + 1 -> k = 4
    k2 = 4
    assert 4 * Fraction(1, 8) + k2 * Fraction(1, 4) - 5 * Fraction(1, 2) + 1 == 0
    assert _opt(3, 2) == ('B', r'\(k = 4\)')

    # Q3: P(x) = x^3 + ax^2 + bx - 6, P(1)=0, P(-2)=12 -> a=6, b=-1
    a3c4, b3c4 = 6, -1
    assert 1 + a3c4 + b3c4 - 6 == 0 and (-8) + 4 * a3c4 - 2 * b3c4 - 6 == 12
    assert _opt(3, 3) == ('C', r'\(a = 6, \quad b = -1\)')

    # Q4: f(x) = 2x^3 + px^2 + qx + 5, f(2)=15, f(-1)=-6 -> p=-4, q=5
    p4, q4 = -4, 5
    assert 2 * 8 + 4 * p4 + 2 * q4 + 5 == 15 and 2 * (-1) + p4 - q4 + 5 == -6
    assert _opt(3, 4) == ('A', r'\(p = -4, \quad q = 5\)')

    # Q5: x^3 - 4x^2 + x + 6 = (x+1)(x-2)(x-3)
    for x in (-3, -1, 0, 2, 3, 5):
        assert x ** 3 - 4 * x ** 2 + x + 6 == (x + 1) * (x - 2) * (x - 3)
    assert _opt(3, 5) == ('B', r'\((x + 1)(x - 2)(x - 3)\)')

    # Q6: 2x^3 - 3x^2 - 11x + 6 = (x+2)(2x-1)(x-3)
    for x in (-2, 0, 1, 3, 4):
        assert 2 * x ** 3 - 3 * x ** 2 - 11 * x + 6 == (x + 2) * (2 * x - 1) * (x - 3)
    assert _opt(3, 6) == ('D', r'\((x + 2)(2x - 1)(x - 3)\)')

    # Q7: x^3 - x^2 + x - 6 = (x-2)(x^2 + x + 3), quadratic Delta = -11 < 0 -> 1 real root x = 2
    for x in (-2, 0, 2, 4):
        assert x ** 3 - x ** 2 + x - 6 == (x - 2) * (x ** 2 + x + 3)
    assert 1 ** 2 - 4 * 1 * 3 == -11 < 0
    assert _opt(3, 7) == ('C', r'Exactly one real root: \(x = 2\)')

    # Q8: 2x^3 - 5x^2 - 2x + 2 = (2x - 1)(x^2 - 2x - 2) -> x = 1/2, 1 +- sqrt(3)
    for r in (0.5, 1 + math.sqrt(3), 1 - math.sqrt(3)):
        assert math.isclose(2 * r ** 3 - 5 * r ** 2 - 2 * r + 2, 0.0, abs_tol=1e-12)
    assert _opt(3, 8) == ('A', r'\(x = \frac{1}{2}, \quad 1 + \sqrt{3}, \quad 1 - \sqrt{3}\)')

    # Q9: 3x^3 - 2x^2 + 4x - 2 = (x-1)(3x^2 + x + 5) + 3
    for x in (-2, 0, 1, 4):
        assert 3 * x ** 3 - 2 * x ** 2 + 4 * x - 2 == (x - 1) * (3 * x ** 2 + x + 5) + 3
    assert _opt(3, 9) == ('C', r'\(Q(x) = 3x^2 + x + 5, \quad R = 3\)')

    # Q10: P(1) = 7, P(-2) = -2 -> R(x) = 3x + 4
    R10 = lambda x: 3 * x + 4
    assert R10(1) == 7 and R10(-2) == -2
    assert _opt(3, 10) == ('A', r'\(3x + 4\)')

    # Q11: (x+3)(x-1)(x-4) >= 0 -> -3 <= x <= 1 or x >= 4
    c11 = lambda x: (x + 3) * (x - 1) * (x - 4)
    assert c11(-4) < 0 and c11(-3) == 0 and c11(0) > 0 and c11(1) == 0 and c11(2) < 0 and c11(4) == 0 and c11(5) > 0
    assert _opt(3, 11) == ('D', r'\(-3 \le x \le 1 \text{ or } x \ge 4\)')

    # Q12: (x-2)^2(5-x) > 0 -> x < 2 or 2 < x < 5
    c12 = lambda x: ((x - 2) ** 2) * (5 - x)
    assert c12(0) > 0 and c12(2) == 0 and c12(3) > 0 and c12(5) == 0 and c12(6) < 0
    assert _opt(3, 12) == ('B', r'\(x < 2 \text{ or } 2 < x < 5\)')

    # -------------------------------------------------------------------------
    # 6. DRILL 5 (Ch. 5) — ALL 12 QUESTIONS MATH VERIFICATION
    # -------------------------------------------------------------------------
    # Q1: y = 2x - 1, x^2 + y^2 = 13 -> (2, 3) and (-6/5, -17/5)
    for x, y in [(Fraction(2), Fraction(3)), (Fraction(-6, 5), Fraction(-17, 5))]:
        assert y == 2 * x - 1 and x * x + y * y == 13
    assert _opt(4, 1) == ('B', r'\((2, 3) \text{ and } \left(-\frac{6}{5}, -\frac{17}{5}\right)\)')

    # Q2: 2x + y = 7, xy = 6 -> (2, 3) and (3/2, 4)
    for x, y in [(Fraction(2), Fraction(3)), (Fraction(3, 2), Fraction(4))]:
        assert 2 * x + y == 7 and x * y == 6
    assert _opt(4, 2) == ('A', r'\((2, 3) \text{ and } \left(\frac{3}{2}, 4\right)\)')

    # Q3: y = x + 2 meets y = x^2 - 2x - 2 at (-1,1) and (4,6) -> AB = 5sqrt(2)
    assert (-1) ** 2 - 2 * (-1) - 2 == (-1) + 2 and 4 ** 2 - 2 * 4 - 2 == 4 + 2
    assert math.isclose(math.hypot(4 - (-1), 6 - 1), 5 * math.sqrt(2), rel_tol=1e-12)
    assert _opt(4, 3) == ('C', r'\(5\sqrt{2}\)')

    # Q4: |2x - 3| = |x + 5| -> x = 8 or -2/3
    for x in (Fraction(8), Fraction(-2, 3)):
        assert abs(2 * x - 3) == abs(x + 5)
    assert _opt(4, 4) == ('D', r'\(x = 8 \text{ or } x = -\frac{2}{3}\)')

    # Q5: |x - 4| = 2x - 5 -> x = 3 only (x = 1 is extraneous)
    assert abs(3 - 4) == 2 * 3 - 5
    assert abs(1 - 4) != 2 * 1 - 5
    assert _opt(4, 5) == ('C', r'\(x = 3\)')

    # Q6: |2x - 1| < 5 -> -2 < x < 3
    assert abs(2 * (-2) - 1) == 5 and abs(2 * 3 - 1) == 5 and abs(2 * 0 - 1) < 5
    assert _opt(4, 6) == ('D', r'\(-2 < x < 3\)')

    # Q7: |3x + 2| >= 7 -> x <= -3 or x >= 5/3
    assert abs(3 * (-3) + 2) == 7 and abs(3 * Fraction(5, 3) + 2) == 7 and abs(3 * 0 + 2) < 7
    assert _opt(4, 7) == ('B', r'\(x \le -3 \text{ or } x \ge \frac{5}{3}\)')

    # Q8: |x - 2| < |2x + 1| -> x < -3 or x > 1/3
    assert abs(-3 - 2) == abs(2 * (-3) + 1)
    assert abs(Fraction(1, 3) - 2) == abs(2 * Fraction(1, 3) + 1)
    assert abs(1 - 2) < abs(2 * 1 + 1) and abs(-4 - 2) < abs(2 * (-4) + 1) and not (abs(0 - 2) < abs(1))
    assert _opt(4, 8) == ('A', r'\(x < -3 \text{ or } x > \frac{1}{3}\)')

    # Q9: |x^2 - 5x + 4| = 2 -> 4 distinct real roots with sum = 10
    roots9 = [(5 + math.sqrt(17)) / 2, (5 - math.sqrt(17)) / 2, 2.0, 3.0]
    assert len(set(round(r, 8) for r in roots9)) == 4
    for r in roots9:
        assert math.isclose(abs(r * r - 5 * r + 4), 2.0, abs_tol=1e-12)
    assert math.isclose(sum(roots9), 10.0, abs_tol=1e-12)
    assert _opt(4, 9) == ('D', r'\(10\)')

    # Q10: x^3 - 2x^2 - 8x < 0 -> x < -2 or 0 < x < 4
    c10 = lambda x: x ** 3 - 2 * x ** 2 - 8 * x
    assert c10(-3) < 0 and c10(-2) == 0 and c10(-1) > 0 and c10(0) == 0 and c10(2) < 0 and c10(4) == 0 and c10(5) > 0
    assert _opt(4, 10) == ('B', r'\(x < -2 \text{ or } 0 < x < 4\)')

    # Q11: y = |x^2 - 6x + 5| meets y = k at 4 points -> 0 < k < 4
    assert abs(3 ** 2 - 6 * 3 + 5) == 4
    assert _opt(4, 11) == ('A', r'\(0 < k < 4\)')

    # Q12: y = 3x + k does not meet y = 2 - 3/x -> (k-2)^2 - 36 < 0 -> -4 < k < 8
    d12 = lambda k: (k - 2) ** 2 - 36
    assert d12(-4) == 0 and d12(8) == 0 and d12(2) < 0 and d12(-5) > 0 and d12(9) > 0
    assert _opt(4, 12) == ('C', r'\(-4 < k < 8\)')

    # -------------------------------------------------------------------------
    # 7. DRILL 6 (Ch. 6) — ALL 12 QUESTIONS MATH VERIFICATION
    # -------------------------------------------------------------------------
    # Q1: lg(2x+1) - lg(x-2) = 1 -> x = 21/8
    x6_1 = Fraction(21, 8)
    assert math.isclose(math.log10(float(2 * x6_1 + 1)) - math.log10(float(x6_1 - 2)), 1.0, abs_tol=1e-12)
    assert _opt(5, 1) == ('A', r'\(x = \frac{21}{8}\)')

    # Q2: log_2(x+2) + log_2(x-1) = 2 -> x = 2 only
    assert math.isclose(math.log2(2 + 2) + math.log2(2 - 1), 2.0, abs_tol=1e-12)
    assert _opt(5, 2) == ('D', r'\(x = 2\)')

    # Q3: log_4(x) + log_2(x) = 6 -> x = 16
    assert math.isclose(math.log(16, 4) + math.log2(16), 6.0, abs_tol=1e-12)
    assert _opt(5, 3) == ('B', r'\(x = 16\)')

    # Q4: log_3(x) - 2 log_x(3) = 1 -> x = 9 or 1/3
    for x in (9.0, 1 / 3):
        assert math.isclose(math.log(x, 3) - 2 * math.log(3, x), 1.0, abs_tol=1e-12)
    assert _opt(5, 4) == ('C', r'\(x = 9 \text{ or } x = \frac{1}{3}\)')

    # Q5: 2^(2x+1) - 5(2^x) + 2 = 0 -> x = -1 or 1
    for x in (-1, 1):
        assert math.isclose(2 ** (2 * x + 1) - 5 * (2 ** x) + 2, 0.0, abs_tol=1e-12)
    assert _opt(5, 5) == ('B', r'\(x = -1 \text{ or } x = 1\)')

    # Q6: e^(2x) - 7e^x + 10 = 0 -> ln 2 = 0.693, ln 5 = 1.61 (3 s.f.)
    assert f'{math.log(2):.3g}' == '0.693' and f'{math.log(5):.3g}' == '1.61'
    assert _opt(5, 6) == ('A', r'\(x = 0.693 \text{ or } x = 1.61\)')

    # Q7: 3^(x+1) = 5^(2x-1) -> x = ln(15) / ln(25/3) = 1.28 (3 s.f.)
    x6_7 = math.log(15) / (2 * math.log(5) - math.log(3))
    assert math.isclose(3 ** (x6_7 + 1), 5 ** (2 * x6_7 - 1), rel_tol=1e-12)
    assert f'{x6_7:.3g}' == '1.28'
    assert _opt(5, 7) == ('D', r'\(x = 1.28\)')

    # Q8: y = 4e^(-2x) - 3 -> asymptote y = -3, x-intercept x = 0.5 ln(4/3)
    x6_8 = 0.5 * math.log(4 / 3)
    assert math.isclose(4 * math.exp(-2 * x6_8) - 3, 0.0, abs_tol=1e-12)
    assert _opt(5, 8) == ('C', r'Asymptote \(y = -3\); \(x\)-intercept \(\left(\frac{1}{2}\ln\frac{4}{3}, 0\right)\)')

    # Q9: f(x) = ln(3x - 6) -> vertical asymptote x = 2, f^-1(x) = (e^x + 6)/3
    f6_9 = lambda x: math.log(3 * x - 6)
    finv6_9 = lambda y: (math.exp(y) + 6) / 3
    for x in (2.5, 4.0, 9.0):
        assert math.isclose(finv6_9(f6_9(x)), x, abs_tol=1e-12)
    assert _opt(5, 9) == ('C', r'Asymptote \(x = 2\); \(f^{-1}(x) = \frac{e^x + 6}{3}\)')

    # Q10: 80 = 200e^(-0.04t) -> t = 25 ln(2.5) = 22.9 (3 s.f.)
    t6_10 = math.log(0.4) / (-0.04)
    assert math.isclose(200 * math.exp(-0.04 * t6_10), 80.0, rel_tol=1e-12)
    assert f'{t6_10:.3g}' == '22.9'
    assert _opt(5, 10) == ('B', r'\(22.9\text{ days}\)')

    # Q11: log_a(24 / sqrt(a)) = 3p + q - 1/2
    for a in (5.0, 7.0, 10.0):
        p, q = math.log(2, a), math.log(3, a)
        assert math.isclose(math.log(24 / math.sqrt(a), a), 3 * p + q - 0.5, abs_tol=1e-12)
    assert _opt(5, 11) == ('D', r'\(3p + q - \frac{1}{2}\)')

    # Q12: log_2(x-y)=2 and log_2(x)+log_2(y)=5 -> x=8, y=4
    assert math.log2(8 - 4) == 2 and math.log2(8) + math.log2(4) == 5
    assert _opt(5, 12) == ('A', r'\(x = 8, \quad y = 4\)')

    # -------------------------------------------------------------------------
    # 8. DRILL 7 (Ch. 7) — ALL 12 QUESTIONS MATH VERIFICATION
    # -------------------------------------------------------------------------
    # Q1: Perpendicular bisector of A(-2, 5) and B(6, 1) -> y = 2x - 1
    mx1, my1 = Fraction(-2 + 6, 2), Fraction(5 + 1, 2)
    m_ab1 = Fraction(1 - 5, 6 - (-2))
    m_p1 = -1 / m_ab1
    assert (mx1, my1) == (2, 3) and m_p1 == 2 and my1 - m_p1 * mx1 == -1
    assert _opt(6, 1) == ('C', r'\(y = 2x - 1\)')

    # Q2: Parallelogram ABCD with A(1,2), B(5,4), D(3,6) -> C(7,8)
    assert (5 + 3 - 1, 4 + 6 - 2) == (7, 8)
    assert _opt(6, 2) == ('B', r'\((7, 8)\)')

    # Q3: Shoelace area of A(1,1), B(5,2), C(6,7), D(2,5) = 16.5
    pts3 = [(1, 1), (5, 2), (6, 7), (2, 5)]
    shoe3 = sum(pts3[i][0] * pts3[(i + 1) % 4][1] - pts3[i][1] * pts3[(i + 1) % 4][0] for i in range(4))
    assert Fraction(abs(shoe3), 2) == Fraction(33, 2)
    assert _opt(6, 3) == ('A', r'\(16.5\text{ units}^2\)')

    # Q4: Perp bisector of P(0,2), Q(6,4) meets y = x + 4 at R(2, 6)
    rx, ry = 2, 6
    assert ry == rx + 4
    assert (rx - 0) ** 2 + (ry - 2) ** 2 == (rx - 6) ** 2 + (ry - 4) ** 2
    assert _opt(6, 4) == ('D', r'\((2, 6)\)')

    # Q5: Triangle A(1,2), B(5,4), C(k,10) anticlockwise, area 14 -> k = 3
    k7_5 = 3
    area7_5 = Fraction((1 * 4 + 5 * 10 + k7_5 * 2) - (2 * 5 + 4 * k7_5 + 10 * 1), 2)
    assert area7_5 == 14
    assert _opt(6, 5) == ('A', r'\(k = 3\)')

    # Q6: y = A x^n, ln y vs ln x through (1, 4) and (3, 10) -> n = 3, A = e
    n6 = Fraction(10 - 4, 3 - 1)
    lnA6 = 4 - n6 * 1
    assert n6 == 3 and lnA6 == 1
    assert _opt(6, 6) == ('D', r'\(n = 3, \quad A = e\)')

    # Q7: y = A b^x, lg y vs x through (2, 1.4) and (6, 2.6) -> A = 6.31, b = 2.00 (3 s.f.)
    lg_b7 = (2.6 - 1.4) / (6 - 2)
    lg_A7 = 1.4 - lg_b7 * 2
    assert f'{10 ** lg_A7:.3g}' == '6.31' and f'{10 ** lg_b7:.2f}' == '2.00'
    assert _opt(6, 7) == ('C', r'\(A = 6.31, \quad b = 2.00\)')

    # Q8: y = ax^2 + bx, y/x vs x through (2, 11) and (5, 20) -> a = 3, b = 5
    a8 = Fraction(20 - 11, 5 - 2)
    b8 = 11 - a8 * 2
    assert a8 == 3 and b8 == 5
    assert _opt(6, 8) == ('B', r'\(a = 3, \quad b = 5\)')

    # Q9: y = a / (x + b), 1/y vs x gradient 1/4 through (2, 2) -> a = 4, b = 6
    a9 = 4
    b9 = 6
    assert Fraction(1, a9) == Fraction(1, 4) and Fraction(2 + b9, a9) == 2
    assert _opt(6, 9) == ('B', r'\(a = 4, \quad b = 6\)')

    # Q10: y^2 vs 1/x through (2, 17) and (5, 29) -> y^2 = 4/x + 9; at x = 1/4, y = 5
    m10 = Fraction(29 - 17, 5 - 2)
    c10_ll = 17 - m10 * 2
    assert m10 == 4 and c10_ll == 9 and m10 * 4 + c10_ll == 25
    assert _opt(6, 10) == ('C', r'\(y = 5\)')

    # Q11: y = A e^(kx), ln y vs x through (0, 2.5) and (5, 0.5) -> A = 12.2 (3 s.f.), k = -0.4
    k11 = Fraction(5 - 25, 50)
    assert k11 == Fraction(-2, 5) and f'{math.exp(2.5):.3g}' == '12.2'
    assert _opt(6, 11) == ('A', r'\(A = 12.2, \quad k = -0.4\)')

    # Q12: y = p x^2 + q/x -> xy = p x^3 + q -> Y = xy vs X = x^3
    for x in (2.0, 3.0):
        p_t, q_t = 4.0, 7.0
        y_t = p_t * x * x + q_t / x
        assert math.isclose(x * y_t, p_t * (x ** 3) + q_t, rel_tol=1e-12)
    assert _opt(6, 12) == ('D', r'\(Y = xy\) against \(X = x^3\)')

    # -------------------------------------------------------------------------
    # 9. DRILL 8 (Ch. 7B NEW 2025–2027 CIRCLE) — ALL 12 QUESTIONS VERIFICATION
    # -------------------------------------------------------------------------
    # Q1: Centre (3, -2), through (7, 1) -> r^2 = 25
    assert (7 - 3) ** 2 + (1 - (-2)) ** 2 == 25
    assert _opt(7, 1) == ('D', r'\((x - 3)^2 + (y + 2)^2 = 25\)')

    # Q2: x^2 + y^2 - 8x + 6y - 11 = 0 -> (x-4)^2 + (y+3)^2 = 36 -> C(4,-3), r=6
    for x, y in [(4, 3), (10, -3), (-2, -3)]:
        assert x * x + y * y - 8 * x + 6 * y - 11 == 0
        assert (x - 4) ** 2 + (y + 3) ** 2 == 36
    assert _opt(7, 2) == ('A', r'Centre \((4, -3)\), radius \(6\)')

    # Q3: 2x^2 + 2y^2 + 12x - 8y + 6 = 0 -> (x+3)^2 + (y-2)^2 = 10 -> C(-3,2), r=sqrt(10)
    assert 9 + 4 - 3 == 10
    assert _opt(7, 3) == ('B', r'Centre \((-3, 2)\), radius \(\sqrt{10}\)')

    # Q4: Diameter A(-1, 6) to B(5, -2) -> C(2, 2), r^2 = 25
    cx4, cy4 = Fraction(-1 + 5, 2), Fraction(6 - 2, 2)
    assert (cx4, cy4) == (2, 2) and (2 - (-1)) ** 2 + (2 - 6) ** 2 == 25
    assert _opt(7, 4) == ('C', r'\((x - 2)^2 + (y - 2)^2 = 25\)')

    # Q5: Tangent to (x-2)^2 + (y+1)^2 = 25 at P(5, 3) -> 3x + 4y = 27
    assert (5 - 2) ** 2 + (3 + 1) ** 2 == 25
    assert 3 * 5 + 4 * 3 == 27
    # Tangent normal vector (3,4) parallel to CP = (3,4) -> dot(CP, tangent dir (-4,3)) = 0
    assert (5 - 2) * (-4) + (3 - (-1)) * 3 == 0
    assert _opt(7, 5) == ('A', r'\(3x + 4y = 27\)')

    # Q6: Normal to x^2 + y^2 - 4x - 6y - 12 = 0 at P(6, 0) -> 3x + 4y = 18
    assert 6 ** 2 + 0 ** 2 - 4 * 6 - 6 * 0 - 12 == 0
    assert 3 * 2 + 4 * 3 == 18 and 3 * 6 + 4 * 0 == 18
    assert _opt(7, 6) == ('C', r'\(3x + 4y = 18\)')

    # Q7: y = x + k tangent to x^2 + y^2 = 18 -> k = +-6
    for k in (-6, 6):
        assert (2 * k) ** 2 - 4 * 2 * (k * k - 18) == 0
    assert _opt(7, 7) == ('B', r'\(k = \pm 6\)')

    # Q8: y = 2x + c meets (x-1)^2 + y^2 = 5 at 2 points -> -7 < c < 3
    d8_8 = lambda c: (4 * c - 2) ** 2 - 20 * (c * c - 4)
    assert d8_8(-7) == 0 and d8_8(3) == 0 and d8_8(0) > 0 and d8_8(-8) < 0 and d8_8(4) < 0
    assert _opt(7, 8) == ('D', r'\(-7 < c < 3\)')

    # Q9: Chord of x + y = 7 on (x-1)^2 + (y-2)^2 = 16 -> A(1,6), B(5,2), AB = 4sqrt(2)
    for x, y in [(1, 6), (5, 2)]:
        assert x + y == 7 and (x - 1) ** 2 + (y - 2) ** 2 == 16
    assert math.isclose(math.hypot(5 - 1, 2 - 6), 4 * math.sqrt(2), rel_tol=1e-12)
    assert _opt(7, 9) == ('B', r'\(4\sqrt{2}\)')

    # Q10: Tangent from T(10, 5) to (x-2)^2 + (y+1)^2 = 36 -> TQ = sqrt(10^2 - 6^2) = 8
    ct_sq = (10 - 2) ** 2 + (5 - (-1)) ** 2
    assert ct_sq == 100 and ct_sq - 36 == 64 and math.isqrt(64) == 8
    assert _opt(7, 10) == ('D', r'\(8\)')

    # Q11: External touch: C1 centre(1,2) r=3, C2 centre(7,10) r=k -> d=10=3+k -> k=7
    d11_c = math.isqrt((7 - 1) ** 2 + (10 - 2) ** 2)
    assert d11_c == 10 and 10 - 3 == 7
    assert _opt(7, 11) == ('A', r'\(k = 7\)')

    # Q12: Internal touch: C1 centre(-2,1) r=4 inside C2 centre(1,5) r=R -> d=5=R-4 -> R=9
    d12_c = math.isqrt((1 - (-2)) ** 2 + (5 - 1) ** 2)
    assert d12_c == 5 and d12_c + 4 == 9
    assert _opt(7, 12) == ('C', r'\(R = 9\)')

    print(
        f"[OK] Verified all {len(DRILLS_0606_P1)} drills x 12 questions = {total_q} questions "
        f"(math assertions + answer balance 3/3/3/3 + KaTeX + validate_igcse_drill)!",
        flush=True,
    )
    return True


if __name__ == '__main__':
    verify_all_math()
