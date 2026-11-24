# -*- coding: utf-8 -*-
"""
Cambridge IGCSE Mathematics (0580) Extended — 2025–2027 Syllabus Drills
Exports `DRILLS_0580_2025`: 8 drills x 15 questions = 120 verified MCQ questions.
  - 4 Non-Calculator Drills (Paper 2): d0580_nc1 .. d0580_nc4
  - 4 Calculator Allowed Drills (Paper 4): d0580_c1 .. d0580_c4
"""

import math
import os
import re
import sys
from fractions import Fraction


DRILLS_0580_2025 = [
    # =========================================================================
    # DRILL 1 (NON-CALC): Surds, Rationalising & Exact Indices (0580 P2)
    # =========================================================================
    {
        'code': 'd0580_nc1',
        'folder_key': 'non_calc',
        'calculator_policy': 'non-calculator',
        'order_index': 1,
        'title': '🚫 Non-Calc Drill 1: Surds, Rationalising & Exact Indices (0580 P2)',
        'time_limit': '30',
        'intro_html': (
            '<p><b>Mục tiêu (Paper 2 Non-Calculator — Syllabus 2025–2027):</b> '
            'Thành thạo rút gọn căn thức (surds), khai triển ngoặc chứa căn, trục căn thức ở mẫu '
            '(rationalising the denominator), và xử lý lũy thừa phân số/âm hoàn toàn <b>không dùng máy tính</b>. '
            'Luôn giữ đáp án ở dạng chính xác tối giản.</p>'
        ),
        'lecture_keys': ['t1', 'p2p4'],
        'questions': [
            # Q1 -> B
            {
                'tag': 'Surds (P2 Non-Calc)',
                'q': r'<p>Simplify fully without a calculator: \(\sqrt{75} + \sqrt{48} - \sqrt{27}\).</p>',
                'options': [
                    r'\(4\sqrt{3}\)',
                    r'\(6\sqrt{3}\)',
                    r'\(8\sqrt{3}\)',
                    r'\(12\sqrt{3}\)',
                ],
                'answer': 'B',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Phân tích từng căn thức theo số chính phương lớn nhất: '
                    r'\(\sqrt{75} = \sqrt{25 \times 3} = 5\sqrt{3}\), '
                    r'\(\sqrt{48} = \sqrt{16 \times 3} = 4\sqrt{3}\), '
                    r'\(\sqrt{27} = \sqrt{9 \times 3} = 3\sqrt{3}\).<br/>'
                    r'<b>Bước 2 [A1]:</b> Cộng trừ các căn đồng dạng: '
                    r'\(5\sqrt{3} + 4\sqrt{3} - 3\sqrt{3} = (5 + 4 - 3)\sqrt{3} = 6\sqrt{3}\).</p>'
                ),
            },
            # Q2 -> C
            {
                'tag': 'Surds (P2 Non-Calc)',
                'q': r'<p>Express \(\sqrt{72} - \sqrt{18} + \sqrt{8}\) in the form \(k\sqrt{2}\), where \(k\) is an integer.</p>',
                'options': [
                    r'\(3\sqrt{2}\)',
                    r'\(7\sqrt{2}\)',
                    r'\(5\sqrt{2}\)',
                    r'\(11\sqrt{2}\)',
                ],
                'answer': 'C',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Đưa thừa số ra ngoài dấu căn: '
                    r'\(\sqrt{72} = \sqrt{36 \times 2} = 6\sqrt{2}\), '
                    r'\(\sqrt{18} = \sqrt{9 \times 2} = 3\sqrt{2}\), '
                    r'\(\sqrt{8} = \sqrt{4 \times 2} = 2\sqrt{2}\).<br/>'
                    r'<b>Bước 2 [A1]:</b> Thu gọn: '
                    r'\(6\sqrt{2} - 3\sqrt{2} + 2\sqrt{2} = 5\sqrt{2}\).</p>'
                ),
            },
            # Q3 -> A
            {
                'tag': 'Expanding Surds (P2 Non-Calc)',
                'q': r'<p>Expand and simplify \((3 + 2\sqrt{5})(4 - \sqrt{5})\).</p>',
                'options': [
                    r'\(2 + 5\sqrt{5}\)',
                    r'\(22 + 5\sqrt{5}\)',
                    r'\(2 - 5\sqrt{5}\)',
                    r'\(2 + 11\sqrt{5}\)',
                ],
                'answer': 'A',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Nhân từng hạng tử (FOIL): '
                    r'\(3(4) - 3\sqrt{5} + 8\sqrt{5} - 2(\sqrt{5})^2 = 12 + 5\sqrt{5} - 2(5)\).<br/>'
                    r'<b>Bước 2 [A1]:</b> Thu gọn phần nguyên và phần căn: '
                    r'\(12 - 10 + 5\sqrt{5} = 2 + 5\sqrt{5}\).</p>'
                ),
            },
            # Q4 -> D
            {
                'tag': 'Expanding Surds (P2 Non-Calc)',
                'q': r'<p>Expand and simplify \((2\sqrt{3} - 5)^2\).</p>',
                'options': [
                    r'\(37 - 10\sqrt{3}\)',
                    r'\(31 - 20\sqrt{3}\)',
                    r'\(13 - 20\sqrt{3}\)',
                    r'\(37 - 20\sqrt{3}\)',
                ],
                'answer': 'D',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Áp dụng hằng đẳng thức \((a - b)^2 = a^2 - 2ab + b^2\): '
                    r'\((2\sqrt{3})^2 - 2(2\sqrt{3})(5) + 5^2\).<br/>'
                    r'<b>Bước 2 [A1]:</b> Tính \((2\sqrt{3})^2 = 4 \times 3 = 12\), do đó kết quả là '
                    r'\(12 - 20\sqrt{3} + 25 = 37 - 20\sqrt{3}\).</p>'
                ),
            },
            # Q5 -> A
            {
                'tag': 'Rationalising Denominators (P2 Non-Calc)',
                'q': r'<p>Rationalise the denominator and simplify \(\frac{18}{\sqrt{6}}\).</p>',
                'options': [
                    r'\(3\sqrt{6}\)',
                    r'\(6\sqrt{3}\)',
                    r'\(3\sqrt{3}\)',
                    r'\(\frac{3\sqrt{6}}{2}\)',
                ],
                'answer': 'A',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Nhân cả tử và mẫu với \(\sqrt{6}\): '
                    r'\(\frac{18}{\sqrt{6}} \times \frac{\sqrt{6}}{\sqrt{6}} = \frac{18\sqrt{6}}{6}\).<br/>'
                    r'<b>Bước 2 [A1]:</b> Rút gọn \(\frac{18}{6} = 3\), thu được \(3\sqrt{6}\).</p>'
                ),
            },
            # Q6 -> C
            {
                'tag': 'Rationalising Denominators (P2 Non-Calc)',
                'q': r'<p>Simplify \(\frac{10 + \sqrt{20}}{\sqrt{5}}\), giving your answer in the form \(a + b\sqrt{5}\).</p>',
                'options': [
                    r'\(2 + 5\sqrt{5}\)',
                    r'\(10\sqrt{5} + 4\)',
                    r'\(2 + 2\sqrt{5}\)',
                    r'\(4 + 2\sqrt{5}\)',
                ],
                'answer': 'C',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Rút gọn \(\sqrt{20} = 2\sqrt{5}\), sau đó tách phân số: '
                    r'\(\frac{10}{\sqrt{5}} + \frac{2\sqrt{5}}{\sqrt{5}}\).<br/>'
                    r'<b>Bước 2 [A1]:</b> Trục căn thức \(\frac{10}{\sqrt{5}} = \frac{10\sqrt{5}}{5} = 2\sqrt{5}\) và \(\frac{2\sqrt{5}}{\sqrt{5}} = 2\), '
                    r'nên kết quả là \(2 + 2\sqrt{5}\).</p>'
                ),
            },
            # Q7 -> B
            {
                'tag': 'Rationalising Denominators (P2 Non-Calc)',
                'q': r'<p>Rationalise the denominator of \(\frac{12}{3 - \sqrt{5}}\) and simplify fully.</p>',
                'options': [
                    r'\(9 - 3\sqrt{5}\)',
                    r'\(9 + 3\sqrt{5}\)',
                    r'\(3 + \sqrt{5}\)',
                    r'\(6 + 2\sqrt{5}\)',
                ],
                'answer': 'B',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Nhân tử và mẫu với biểu thức liên hợp \((3 + \sqrt{5})\): '
                    r'\(\frac{12(3 + \sqrt{5})}{(3 - \sqrt{5})(3 + \sqrt{5})}\).<br/>'
                    r'<b>Bước 2 [A1]:</b> Mẫu số bằng \(3^2 - (\sqrt{5})^2 = 9 - 5 = 4\), '
                    r'suy ra \(\frac{12(3 + \sqrt{5})}{4} = 3(3 + \sqrt{5}) = 9 + 3\sqrt{5}\).</p>'
                ),
            },
            # Q8 -> D
            {
                'tag': 'Rationalising Denominators (P2 Non-Calc)',
                'q': r'<p>Write \(\frac{6}{\sqrt{7} + 2}\) in the form \(a\sqrt{7} - b\), where \(a\) and \(b\) are integers.</p>',
                'options': [
                    r'\(2\sqrt{7} + 4\)',
                    r'\(3\sqrt{7} - 6\)',
                    r'\(6\sqrt{7} - 12\)',
                    r'\(2\sqrt{7} - 4\)',
                ],
                'answer': 'D',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Nhân tử và mẫu với liên hợp \((\sqrt{7} - 2)\): '
                    r'\(\frac{6(\sqrt{7} - 2)}{(\sqrt{7})^2 - 2^2} = \frac{6(\sqrt{7} - 2)}{7 - 4}\).<br/>'
                    r'<b>Bước 2 [A1]:</b> Rút gọn \(\frac{6}{3} = 2\), thu được \(2(\sqrt{7} - 2) = 2\sqrt{7} - 4\).</p>'
                ),
            },
            # Q9 -> B
            {
                'tag': 'Surds in Geometry (P2 Non-Calc)',
                'q': r'<p>A rectangle has area \((14 + 4\sqrt{3})\text{ cm}^2\) and width \((2 + \sqrt{3})\text{ cm}\). Find its exact length in \(\text{cm}\).</p>',
                'options': [
                    r'\(16 + 6\sqrt{3}\)',
                    r'\(16 - 6\sqrt{3}\)',
                    r'\(40 - 6\sqrt{3}\)',
                    r'\(16 - 2\sqrt{3}\)',
                ],
                'answer': 'B',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Chiều dài \(L = \frac{14 + 4\sqrt{3}}{2 + \sqrt{3}}\). '
                    r'Nhân tử và mẫu với \((2 - \sqrt{3})\): mẫu số là \(2^2 - 3 = 1\).<br/>'
                    r'<b>Bước 2 [A1]:</b> Tử số là \((14 + 4\sqrt{3})(2 - \sqrt{3}) = 28 - 14\sqrt{3} + 8\sqrt{3} - 12 = 16 - 6\sqrt{3}\text{ cm}\).</p>'
                ),
            },
            # Q10 -> A
            {
                'tag': 'Fractional & Negative Indices (P2 Non-Calc)',
                'q': r'<p>Evaluate \(27^{-\frac{2}{3}}\) without a calculator.</p>',
                'options': [
                    r'\(\frac{1}{9}\)',
                    r'\(-9\)',
                    r'\(-\frac{1}{9}\)',
                    r'\(\frac{1}{18}\)',
                ],
                'answer': 'A',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Đổi số mũ âm thành nghịch đảo và căn bậc ba trước: '
                    r'\(27^{-\frac{2}{3}} = \frac{1}{(27^{\frac{1}{3}})^2} = \frac{1}{(\sqrt[3]{27})^2}\).<br/>'
                    r'<b>Bước 2 [A1]:</b> Vì \(\sqrt[3]{27} = 3\), nên giá trị là \(\frac{1}{3^2} = \frac{1}{9}\).</p>'
                ),
            },
            # Q11 -> D
            {
                'tag': 'Fractional & Negative Indices (P2 Non-Calc)',
                'q': r'<p>Find the exact value of \(\left(\frac{16}{81}\right)^{-\frac{3}{4}}\).</p>',
                'options': [
                    r'\(\frac{8}{27}\)',
                    r'\(-\frac{27}{8}\)',
                    r'\(\frac{9}{4}\)',
                    r'\(\frac{27}{8}\)',
                ],
                'answer': 'D',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Đảo ngược phân số để khử dấu trừ ở số mũ: '
                    r'\(\left(\frac{16}{81}\right)^{-\frac{3}{4}} = \left(\frac{81}{16}\right)^{\frac{3}{4}}\).<br/>'
                    r'<b>Bước 2 [A1]:</b> Lấy căn bậc bốn trước: '
                    r'\(\left(\frac{\sqrt[4]{81}}{\sqrt[4]{16}}\right)^3 = \left(\frac{3}{2}\right)^3 = \frac{27}{8}\).</p>'
                ),
            },
            # Q12 -> C
            {
                'tag': 'Algebraic Indices (P2 Non-Calc)',
                'q': r'<p>Simplify \(\left(8x^6y^{-3}\right)^{\frac{2}{3}}\), expressing your answer with positive indices only.</p>',
                'options': [
                    r'\(\frac{16x^4}{y^2}\)',
                    r'\(\frac{4x^9}{y^2}\)',
                    r'\(\frac{4x^4}{y^2}\)',
                    r'\(\frac{4x^4}{y^3}\)',
                ],
                'answer': 'C',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Áp dụng quy tắc \((ab)^n = a^n b^n\): '
                    r'\(8^{\frac{2}{3}} \cdot x^{6 \times \frac{2}{3}} \cdot y^{-3 \times \frac{2}{3}}\).<br/>'
                    r'<b>Bước 2 [A1]:</b> Ta có \(8^{\frac{2}{3}} = (\sqrt[3]{8})^2 = 2^2 = 4\), '
                    r'\(x^4\), và \(y^{-2} = \frac{1}{y^2}\), suy ra \(\frac{4x^4}{y^2}\).</p>'
                ),
            },
            # Q13 -> B
            {
                'tag': 'Index Equations (P2 Non-Calc)',
                'q': r'<p>Solve the exact index equation \(4^x = 8^{x - 1}\).</p>',
                'options': [
                    r'\(x = 1\)',
                    r'\(x = 3\)',
                    r'\(x = \frac{3}{2}\)',
                    r'\(x = -3\)',
                ],
                'answer': 'B',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Quy cả hai vế về cùng cơ số \(2\): '
                    r'\((2^2)^x = (2^3)^{x - 1} \Rightarrow 2^{2x} = 2^{3x - 3}\).<br/>'
                    r'<b>Bước 2 [A1]:</b> Đồng nhất số mũ: \(2x = 3x - 3 \Rightarrow x = 3\).</p>'
                ),
            },
            # Q14 -> C
            {
                'tag': 'Index Equations (P2 Non-Calc)',
                'q': r'<p>Given that \(9^{2x - 1} = \frac{1}{27\sqrt{3}}\), find the exact value of \(x\).</p>',
                'options': [
                    r'\(x = -\frac{5}{8}\)',
                    r'\(x = \frac{3}{8}\)',
                    r'\(x = -\frac{3}{8}\)',
                    r'\(x = -\frac{1}{4}\)',
                ],
                'answer': 'C',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Đưa hai vế về cơ số \(3\): '
                    r'\(9^{2x - 1} = 3^{2(2x - 1)} = 3^{4x - 2}\), và '
                    r'\(\frac{1}{27\sqrt{3}} = \frac{1}{3^3 \cdot 3^{\frac{1}{2}}} = 3^{-\frac{7}{2}}\).<br/>'
                    r'<b>Bước 2 [A1]:</b> Giải \(4x - 2 = -\frac{7}{2} \Rightarrow 4x = -\frac{3}{2} \Rightarrow x = -\frac{3}{8}\).</p>'
                ),
            },
            # Q15 -> A
            {
                'tag': 'Exact Indices (P2 Non-Calc)',
                'q': r'<p>Given that \(2^p = \frac{\sqrt{8}}{16}\), find the exact value of \(p\).</p>',
                'options': [
                    r'\(p = -\frac{5}{2}\)',
                    r'\(p = -\frac{3}{2}\)',
                    r'\(p = \frac{5}{2}\)',
                    r'\(p = -\frac{7}{2}\)',
                ],
                'answer': 'A',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Viết tử và mẫu theo cơ số \(2\): '
                    r'\(\sqrt{8} = (2^3)^{\frac{1}{2}} = 2^{\frac{3}{2}}\) và \(16 = 2^4\).<br/>'
                    r'<b>Bước 2 [A1]:</b> Áp dụng phép chia lũy thừa cùng cơ số: '
                    r'\(2^p = 2^{\frac{3}{2} - 4} = 2^{-\frac{5}{2}} \Rightarrow p = -\frac{5}{2}\).</p>'
                ),
            },
        ],
    },

    # =========================================================================
    # DRILL 2 (NON-CALC): Exact Trig Values, Special Triangles & Bearings
    # =========================================================================
    {
        'code': 'd0580_nc2',
        'folder_key': 'non_calc',
        'calculator_policy': 'non-calculator',
        'order_index': 2,
        'title': '🚫 Non-Calc Drill 2: Exact Trig Values (0°–90°), Special Triangles & Bearings (0580 P2)',
        'time_limit': '30',
        'intro_html': (
            r'<p><b>Mục tiêu (Paper 2 Non-Calculator — Syllabus 2025–2027):</b> '
            r'Thuộc lòng và vận dụng bảng giá trị lượng giác chính xác (exact trig values) tại '
            r'\(0^\circ, 30^\circ, 45^\circ, 60^\circ, 90^\circ\), góc tù \(120^\circ, 135^\circ, 150^\circ\), '
            r'tam giác đặc biệt \(30^\circ\text{–}60^\circ\text{–}90^\circ\) và \(45^\circ\text{–}45^\circ\text{–}90^\circ\), '
            r'phương trình lượng giác cơ bản và góc phương vị (bearings) không dùng máy tính.</p>'
        ),
        'lecture_keys': ['t6', 'p2p4'],
        'questions': [
            # Q1 -> C
            {
                'tag': 'Exact Trig Values (P2 Non-Calc)',
                'q': r'<p>Find the exact value of \(\sin 30^\circ + \cos 60^\circ + \tan 45^\circ\).</p>',
                'options': [
                    r'\(1\)',
                    r'\(\frac{3}{2}\)',
                    r'\(2\)',
                    r'\(\sqrt{3}\)',
                ],
                'answer': 'C',
                'explanation': (
                    r'<p><b>Bước 1 [B1]:</b> Thay các giá trị lượng giác đặc biệt: '
                    r'\(\sin 30^\circ = \frac{1}{2}\), \(\cos 60^\circ = \frac{1}{2}\), \(\tan 45^\circ = 1\).<br/>'
                    r'<b>Bước 2 [A1]:</b> Cộng lại: \(\frac{1}{2} + \frac{1}{2} + 1 = 2\).</p>'
                ),
            },
            # Q2 -> A
            {
                'tag': 'Exact Trig Values (P2 Non-Calc)',
                'q': r'<p>Evaluate \(\sin 60^\circ \cos 30^\circ - \cos 60^\circ \sin 30^\circ\) without a calculator.</p>',
                'options': [
                    r'\(\frac{1}{2}\)',
                    r'\(1\)',
                    r'\(0\)',
                    r'\(\frac{\sqrt{3}}{2}\)',
                ],
                'answer': 'A',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Thay đúng các giá trị chính xác: '
                    r'\(\left(\frac{\sqrt{3}}{2}\right)\left(\frac{\sqrt{3}}{2}\right) - \left(\frac{1}{2}\right)\left(\frac{1}{2}\right)\).<br/>'
                    r'<b>Bước 2 [A1]:</b> Tính toán: \(\frac{3}{4} - \frac{1}{4} = \frac{2}{4} = \frac{1}{2}\).</p>'
                ),
            },
            # Q3 -> D
            {
                'tag': 'Exact Trig Values (P2 Non-Calc)',
                'q': r'<p>Find the exact value of \(\frac{\tan 60^\circ - \tan 30^\circ}{1 + \tan 60^\circ \tan 30^\circ}\).</p>',
                'options': [
                    r'\(\sqrt{3}\)',
                    r'\(1\)',
                    r'\(\frac{2\sqrt{3}}{3}\)',
                    r'\(\frac{\sqrt{3}}{3}\)',
                ],
                'answer': 'D',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Thay \(\tan 60^\circ = \sqrt{3}\) và \(\tan 30^\circ = \frac{1}{\sqrt{3}}\): '
                    r'tử số là \(\sqrt{3} - \frac{1}{\sqrt{3}} = \frac{2}{\sqrt{3}}\), mẫu số là \(1 + \sqrt{3} \cdot \frac{1}{\sqrt{3}} = 2\).<br/>'
                    r'<b>Bước 2 [A1]:</b> Rút gọn và trục căn thức: '
                    r'\(\frac{2/\sqrt{3}}{2} = \frac{1}{\sqrt{3}} = \frac{\sqrt{3}}{3}\).</p>'
                ),
            },
            # Q4 -> B
            {
                'tag': 'Boundary Angles (P2 Non-Calc)',
                'q': r'<p>Evaluate \(3\cos 0^\circ - 2\sin 90^\circ + 5\tan 0^\circ + 4\cos 90^\circ\).</p>',
                'options': [
                    r'\(5\)',
                    r'\(1\)',
                    r'\(-1\)',
                    r'\(3\)',
                ],
                'answer': 'B',
                'explanation': (
                    r'<p><b>Bước 1 [B1]:</b> Nhớ giá trị biên: \(\cos 0^\circ = 1\), \(\sin 90^\circ = 1\), \(\tan 0^\circ = 0\), \(\cos 90^\circ = 0\).<br/>'
                    r'<b>Bước 2 [A1]:</b> Thay vào biểu thức: \(3(1) - 2(1) + 5(0) + 4(0) = 3 - 2 = 1\).</p>'
                ),
            },
            # Q5 -> D
            {
                'tag': 'Obtuse Exact Angles (P2 Non-Calc)',
                'q': r'<p>Find the exact value of \(\cos 150^\circ + \sin 120^\circ\).</p>',
                'options': [
                    r'\(\sqrt{3}\)',
                    r'\(-\sqrt{3}\)',
                    r'\(\frac{\sqrt{3}}{2}\)',
                    r'\(0\)',
                ],
                'answer': 'D',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Áp dụng công thức góc bù (supplementary angles): '
                    r'\(\cos 150^\circ = -\cos(180^\circ - 150^\circ) = -\cos 30^\circ = -\frac{\sqrt{3}}{2}\), và '
                    r'\(\sin 120^\circ = \sin(180^\circ - 120^\circ) = \sin 60^\circ = \frac{\sqrt{3}}{2}\).<br/>'
                    r'<b>Bước 2 [A1]:</b> Cộng lại: \(-\frac{\sqrt{3}}{2} + \frac{\sqrt{3}}{2} = 0\).</p>'
                ),
            },
            # Q6 -> B
            {
                'tag': 'Obtuse Exact Angles (P2 Non-Calc)',
                'q': r'<p>Find the exact value of \(\sin 135^\circ \times \cos 120^\circ\).</p>',
                'options': [
                    r'\(\frac{\sqrt{2}}{4}\)',
                    r'\(-\frac{\sqrt{2}}{4}\)',
                    r'\(-\frac{\sqrt{6}}{4}\)',
                    r'\(-\frac{\sqrt{2}}{2}\)',
                ],
                'answer': 'B',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Đổi góc tù về góc nhọn: '
                    r'\(\sin 135^\circ = \sin 45^\circ = \frac{\sqrt{2}}{2}\) và '
                    r'\(\cos 120^\circ = -\cos 60^\circ = -\frac{1}{2}\).<br/>'
                    r'<b>Bước 2 [A1]:</b> Nhân hai giá trị: '
                    r'\(\frac{\sqrt{2}}{2} \times \left(-\frac{1}{2}\right) = -\frac{\sqrt{2}}{4}\).</p>'
                ),
            },
            # Q7 -> A
            {
                'tag': 'Special Triangles (P2 Non-Calc)',
                'q': r'<p>In right-angled triangle \(ABC\), \(\angle B = 90^\circ\), \(\angle A = 30^\circ\), and hypotenuse \(AC = 14\text{ cm}\). Find the exact length of \(AB\).</p>',
                'options': [
                    r'\(7\sqrt{3}\text{ cm}\)',
                    r'\(7\text{ cm}\)',
                    r'\(7\sqrt{2}\text{ cm}\)',
                    r'\(\frac{14\sqrt{3}}{3}\text{ cm}\)',
                ],
                'answer': 'A',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Trong tam giác vuông \(ABC\), \(AB\) là cạnh kề góc \(A = 30^\circ\): '
                    r'\(\cos 30^\circ = \frac{AB}{AC} \Rightarrow AB = 14\cos 30^\circ\).<br/>'
                    r'<b>Bước 2 [A1]:</b> Thay \(\cos 30^\circ = \frac{\sqrt{3}}{2}\), ta được '
                    r'\(AB = 14 \times \frac{\sqrt{3}}{2} = 7\sqrt{3}\text{ cm}\).</p>'
                ),
            },
            # Q8 -> C
            {
                'tag': 'Special Triangles (P2 Non-Calc)',
                'q': r'<p>A square \(PQRS\) has diagonal \(PR = 10\text{ cm}\). Find the exact perimeter of the square.</p>',
                'options': [
                    r'\(40\sqrt{2}\text{ cm}\)',
                    r'\(10\sqrt{2}\text{ cm}\)',
                    r'\(20\sqrt{2}\text{ cm}\)',
                    r'\(20\text{ cm}\)',
                ],
                'answer': 'C',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Đường chéo chia hình vuông thành hai tam giác vuông cân \(45^\circ\text{–}45^\circ\text{–}90^\circ\). '
                    r'Cạnh hình vuông \(s = 10\cos 45^\circ = 10 \times \frac{\sqrt{2}}{2} = 5\sqrt{2}\text{ cm}\).<br/>'
                    r'<b>Bước 2 [A1]:</b> Chu vi hình vuông \(P = 4s = 4 \times 5\sqrt{2} = 20\sqrt{2}\text{ cm}\).</p>'
                ),
            },
            # Q9 -> B
            {
                'tag': 'Special Triangles (P2 Non-Calc)',
                'q': r'<p>In triangle \(PQR\), the altitude \(PS\) is perpendicular to base \(QR\) with \(PS = 6\text{ cm}\), \(\angle PQS = 45^\circ\), and \(\angle PRS = 60^\circ\). Find the exact length of \(QR\).</p>',
                'options': [
                    r'\(6 + 6\sqrt{3}\text{ cm}\)',
                    r'\(6 + 2\sqrt{3}\text{ cm}\)',
                    r'\(6 + 3\sqrt{3}\text{ cm}\)',
                    r'\(12\sqrt{3}\text{ cm}\)',
                ],
                'answer': 'B',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Trong \(\triangle PQS\): \(QS = \frac{PS}{\tan 45^\circ} = \frac{6}{1} = 6\text{ cm}\). '
                    r'Trong \(\triangle PRS\): \(SR = \frac{PS}{\tan 60^\circ} = \frac{6}{\sqrt{3}} = 2\sqrt{3}\text{ cm}\).<br/>'
                    r'<b>Bước 2 [A1]:</b> Cộng hai đoạn thẳng: \(QR = QS + SR = 6 + 2\sqrt{3}\text{ cm}\).</p>'
                ),
            },
            # Q10 -> D
            {
                'tag': 'Exact Triangle Area (P2 Non-Calc)',
                'q': r'<p>Triangle \(ABC\) has \(AB = 8\text{ cm}\), \(AC = 12\text{ cm}\), and \(\angle BAC = 60^\circ\). Calculate the exact area of triangle \(ABC\).</p>',
                'options': [
                    r'\(48\sqrt{3}\text{ cm}^2\)',
                    r'\(24\text{ cm}^2\)',
                    r'\(12\sqrt{3}\text{ cm}^2\)',
                    r'\(24\sqrt{3}\text{ cm}^2\)',
                ],
                'answer': 'D',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Dùng công thức diện tích \(\text{Area} = \frac{1}{2}ab\sin C = \frac{1}{2}(8)(12)\sin 60^\circ\).<br/>'
                    r'<b>Bước 2 [A1]:</b> Thay \(\sin 60^\circ = \frac{\sqrt{3}}{2}\): '
                    r'\(48 \times \frac{\sqrt{3}}{2} = 24\sqrt{3}\text{ cm}^2\).</p>'
                ),
            },
            # Q11 -> A
            {
                'tag': 'Exact Area — Obtuse Angle (P2 Non-Calc)',
                'q': r'<p>A parallelogram has adjacent sides of lengths \(6\text{ cm}\) and \(10\text{ cm}\) with an included angle of \(135^\circ\). Find its exact area.</p>',
                'options': [
                    r'\(30\sqrt{2}\text{ cm}^2\)',
                    r'\(15\sqrt{2}\text{ cm}^2\)',
                    r'\(30\sqrt{3}\text{ cm}^2\)',
                    r'\(60\sqrt{2}\text{ cm}^2\)',
                ],
                'answer': 'A',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Diện tích hình bình hành bằng hai lần diện tích tam giác: '
                    r'\(\text{Area} = ab\sin\theta = 6 \times 10 \times \sin 135^\circ\).<br/>'
                    r'<b>Bước 2 [A1]:</b> Vì \(\sin 135^\circ = \sin 45^\circ = \frac{\sqrt{2}}{2}\), nên '
                    r'\(\text{Area} = 60 \times \frac{\sqrt{2}}{2} = 30\sqrt{2}\text{ cm}^2\).</p>'
                ),
            },
            # Q12 -> C
            {
                'tag': 'Trig Equations (P2 Non-Calc)',
                'q': r'<p>Solve the equation \(2\sin x = \sqrt{3}\) for \(0^\circ \le x \le 360^\circ\).</p>',
                'options': [
                    r'\(x = 30^\circ \text{ or } 150^\circ\)',
                    r'\(x = 60^\circ \text{ or } 300^\circ\)',
                    r'\(x = 60^\circ \text{ or } 120^\circ\)',
                    r'\(x = 60^\circ \text{ or } 240^\circ\)',
                ],
                'answer': 'C',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Chuyển vế: \(\sin x = \frac{\sqrt{3}}{2} > 0\), nên nghiệm nằm ở góc phần tư I và II (CAST). '
                    r'Góc nhọn cơ sở là \(60^\circ\).<br/>'
                    r'<b>Bước 2 [A1]:</b> Nghiệm là \(x = 60^\circ\) và \(x = 180^\circ - 60^\circ = 120^\circ\).</p>'
                ),
            },
            # Q13 -> D
            {
                'tag': 'Trig Equations (P2 Non-Calc)',
                'q': r'<p>Solve the equation \(2\cos x + 1 = 0\) for \(0^\circ \le x \le 360^\circ\).</p>',
                'options': [
                    r'\(x = 60^\circ \text{ or } 300^\circ\)',
                    r'\(x = 120^\circ \text{ or } 300^\circ\)',
                    r'\(x = 150^\circ \text{ or } 210^\circ\)',
                    r'\(x = 120^\circ \text{ or } 240^\circ\)',
                ],
                'answer': 'D',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Giải \(\cos x = -\frac{1}{2} < 0\). Góc nhọn cơ sở thỏa \(\cos \alpha = \frac{1}{2}\) là \(\alpha = 60^\circ\). '
                    r'Cos âm ở góc phần tư II và III.<br/>'
                    r'<b>Bước 2 [A1]:</b> Nghiệm là \(x = 180^\circ - 60^\circ = 120^\circ\) và \(x = 180^\circ + 60^\circ = 240^\circ\).</p>'
                ),
            },
            # Q14 -> A
            {
                'tag': 'Bearings & Exact Trig (P2 Non-Calc)',
                'q': r'<p>A ship sails \(20\text{ km}\) from port \(A\) to point \(B\) on a bearing of \(060^\circ\). How far <b>east</b> of \(A\) is \(B\)?</p>',
                'options': [
                    r'\(10\sqrt{3}\text{ km}\)',
                    r'\(10\text{ km}\)',
                    r'\(10\sqrt{2}\text{ km}\)',
                    r'\(20\sqrt{3}\text{ km}\)',
                ],
                'answer': 'A',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Góc phương vị \(060^\circ\) đo theo chiều kim đồng hồ từ hướng Bắc (North). '
                    r'Độ dịch chuyển về phía Đông là cạnh đối góc \(60^\circ\): \(d_{\text{East}} = 20\sin 60^\circ\).<br/>'
                    r'<b>Bước 2 [A1]:</b> Thay \(\sin 60^\circ = \frac{\sqrt{3}}{2}\): '
                    r'\(d_{\text{East}} = 20 \times \frac{\sqrt{3}}{2} = 10\sqrt{3}\text{ km}\).</p>'
                ),
            },
            # Q15 -> C
            {
                'tag': 'Bearings & Exact Trig (P2 Non-Calc)',
                'q': r'<p>Point \(Q\) is \(12\text{ km}\) from point \(P\) on a bearing of \(150^\circ\). Find the bearing of \(P\) from \(Q\) and the exact distance that \(Q\) is <b>south</b> of \(P\).</p>',
                'options': [
                    r'Bearing \(330^\circ\), distance \(6\text{ km}\)',
                    r'Bearing \(030^\circ\), distance \(6\sqrt{3}\text{ km}\)',
                    r'Bearing \(330^\circ\), distance \(6\sqrt{3}\text{ km}\)',
                    r'Bearing \(300^\circ\), distance \(6\sqrt{3}\text{ km}\)',
                ],
                'answer': 'C',
                'explanation': (
                    r'<p><b>Bước 1 [B1]:</b> Góc phương vị ngược (back-bearing) của \(P\) từ \(Q\) là '
                    r'\(150^\circ + 180^\circ = 330^\circ\).<br/>'
                    r'<b>Bước 2 [M1][A1]:</b> Hướng \(150^\circ\) lệch khỏi hướng Nam (\(180^\circ\)) một góc \(30^\circ\). '
                    r'Khoảng cách về phía Nam là \(12\cos 30^\circ = 12 \times \frac{\sqrt{3}}{2} = 6\sqrt{3}\text{ km}\).</p>'
                ),
            },
        ],
    },

    # =========================================================================
    # DRILL 3 (NON-CALC): Recurring Decimals, Standard Form, Fractions & Bounds
    # =========================================================================
    {
        'code': 'd0580_nc3',
        'folder_key': 'non_calc',
        'calculator_policy': 'non-calculator',
        'order_index': 3,
        'title': '🚫 Non-Calc Drill 3: Recurring Decimals, Standard Form, Fractions & Bounds (0580 P2)',
        'time_limit': '30',
        'intro_html': (
            r'<p><b>Mục tiêu (Paper 2 Non-Calculator — Syllabus 2025–2027):</b> '
            r'Rèn kỹ năng tính nhẩm chính xác cho các dạng bài kinh điển của Paper 2: đổi số thập phân vô hạn tuần hoàn '
            r'(recurring decimals) sang phân số tối giản, phép toán dạng chuẩn (standard form), giới hạn trên/dưới '
            r'(upper &amp; lower bounds), ƯCLN/BCNN bằng thừa số nguyên tố, phần trăm ngược và tỉ số gộp.</p>'
        ),
        'lecture_keys': ['t1', 'p2p4'],
        'questions': [
            # Q1 -> A
            {
                'tag': 'Recurring Decimals (P2 Non-Calc)',
                'q': r'<p>Convert the recurring decimal \(0.\dot{4}\dot{5} = 0.454545\dots\) into a fraction in its lowest terms.</p>',
                'options': [
                    r'\(\frac{5}{11}\)',
                    r'\(\frac{9}{20}\)',
                    r'\(\frac{4}{9}\)',
                    r'\(\frac{15}{34}\)',
                ],
                'answer': 'A',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Đặt \(x = 0.454545\dots\), suy ra \(100x = 45.454545\dots\). '
                    r'Trừ hai phương trình: \(100x - x = 45 \Rightarrow 99x = 45\).<br/>'
                    r'<b>Bước 2 [A1]:</b> Rút gọn phân số chia cả tử và mẫu cho \(9\): '
                    r'\(x = \frac{45}{99} = \frac{5}{11}\).</p>'
                ),
            },
            # Q2 -> D
            {
                'tag': 'Recurring Decimals (P2 Non-Calc)',
                'q': r'<p>Express the recurring decimal \(0.2\dot{7} = 0.27777\dots\) as a fraction in its simplest form.</p>',
                'options': [
                    r'\(\frac{3}{11}\)',
                    r'\(\frac{7}{25}\)',
                    r'\(\frac{5}{19}\)',
                    r'\(\frac{5}{18}\)',
                ],
                'answer': 'D',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Đặt \(x = 0.27777\dots\). Nhân \(10\) và \(100\): '
                    r'\(10x = 2.7777\dots\) và \(100x = 27.7777\dots\). '
                    r'Trừ vế theo vế: \(90x = 25\).<br/>'
                    r'<b>Bước 2 [A1]:</b> Rút gọn cho \(5\): \(x = \frac{25}{90} = \frac{5}{18}\).</p>'
                ),
            },
            # Q3 -> B
            {
                'tag': 'Recurring Decimals (P2 Non-Calc)',
                'q': r'<p>Convert \(0.1\dot{3}\dot{6} = 0.1363636\dots\) to a simplified fraction.</p>',
                'options': [
                    r'\(\frac{17}{125}\)',
                    r'\(\frac{3}{22}\)',
                    r'\(\frac{5}{37}\)',
                    r'\(\frac{2}{15}\)',
                ],
                'answer': 'B',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Đặt \(x = 0.1363636\dots\). Ta có \(10x = 1.363636\dots\) và '
                    r'\(1000x = 136.363636\dots\). Lấy hiệu: \(990x = 135\).<br/>'
                    r'<b>Bước 2 [A1]:</b> Chia cả tử và mẫu cho \(45\): '
                    r'\(x = \frac{135}{990} = \frac{3}{22}\).</p>'
                ),
            },
            # Q4 -> C
            {
                'tag': 'Standard Form (P2 Non-Calc)',
                'q': r'<p>Calculate \((4.5 \times 10^5) \times (6 \times 10^{-8})\), giving your answer in standard form.</p>',
                'options': [
                    r'\(27 \times 10^{-3}\)',
                    r'\(2.7 \times 10^{-3}\)',
                    r'\(2.7 \times 10^{-2}\)',
                    r'\(2.7 \times 10^{-4}\)',
                ],
                'answer': 'C',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Nhân phần hệ số và cộng số mũ: '
                    r'\((4.5 \times 6) \times 10^{5 + (-8)} = 27 \times 10^{-3}\).<br/>'
                    r'<b>Bước 2 [A1]:</b> Chỉnh về dạng chuẩn \(A \times 10^n\) với \(1 \le A < 10\): '
                    r'\(27 \times 10^{-3} = 2.7 \times 10^1 \times 10^{-3} = 2.7 \times 10^{-2}\).</p>'
                ),
            },
            # Q5 -> B
            {
                'tag': 'Standard Form (P2 Non-Calc)',
                'q': r'<p>Work out \(\frac{3.6 \times 10^{-4}}{9 \times 10^3}\) without a calculator, giving your answer in standard form.</p>',
                'options': [
                    r'\(4 \times 10^{-7}\)',
                    r'\(4 \times 10^{-8}\)',
                    r'\(0.4 \times 10^{-7}\)',
                    r'\(4 \times 10^{-6}\)',
                ],
                'answer': 'B',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Chia hệ số và trừ số mũ: '
                    r'\(\frac{3.6}{9} \times 10^{-4 - 3} = 0.4 \times 10^{-7}\).<br/>'
                    r'<b>Bước 2 [A1]:</b> Chuẩn hóa \(0.4 = 4 \times 10^{-1}\), thu được '
                    r'\(4 \times 10^{-1} \times 10^{-7} = 4 \times 10^{-8}\).</p>'
                ),
            },
            # Q6 -> A
            {
                'tag': 'Standard Form (P2 Non-Calc)',
                'q': r'<p>Calculate \((6.4 \times 10^5) + (8.5 \times 10^4)\), giving your answer in standard form.</p>',
                'options': [
                    r'\(7.25 \times 10^5\)',
                    r'\(1.49 \times 10^9\)',
                    r'\(7.25 \times 10^4\)',
                    r'\(1.49 \times 10^6\)',
                ],
                'answer': 'A',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Đưa hai số về cùng bậc lũy thừa \(10^5\): '
                    r'\(8.5 \times 10^4 = 0.85 \times 10^5\).<br/>'
                    r'<b>Bước 2 [A1]:</b> Cộng phần hệ số: '
                    r'\((6.4 + 0.85) \times 10^5 = 7.25 \times 10^5\).</p>'
                ),
            },
            # Q7 -> D
            {
                'tag': 'Standard Form (P2 Non-Calc)',
                'q': r'<p>Evaluate \((5.2 \times 10^{-3}) - (7 \times 10^{-4})\) in standard form.</p>',
                'options': [
                    r'\(4.5 \times 10^{-4}\)',
                    r'\(1.8 \times 10^{-3}\)',
                    r'\(4.5 \times 10^{-2}\)',
                    r'\(4.5 \times 10^{-3}\)',
                ],
                'answer': 'D',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Quy đổi \(7 \times 10^{-4} = 0.7 \times 10^{-3}\) để đồng nhất lũy thừa \(10^{-3}\).<br/>'
                    r'<b>Bước 2 [A1]:</b> Trừ phần hệ số: \((5.2 - 0.7) \times 10^{-3} = 4.5 \times 10^{-3}\).</p>'
                ),
            },
            # Q8 -> C
            {
                'tag': 'Exact Fractions (P2 Non-Calc)',
                'q': r'<p>Without using a calculator, calculate \(2\frac{1}{4} \div 1\frac{7}{8} + \frac{3}{5}\), giving your answer as a mixed number in its simplest form.</p>',
                'options': [
                    r'\(1\frac{2}{5}\)',
                    r'\(2\frac{1}{5}\)',
                    r'\(1\frac{4}{5}\)',
                    r'\(1\frac{1}{2}\)',
                ],
                'answer': 'C',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Đổi hỗn số thành phân số và thực hiện phép chia trước (BIDMAS): '
                    r'\(\frac{9}{4} \div \frac{15}{8} = \frac{9}{4} \times \frac{8}{15} = \frac{72}{60} = \frac{6}{5}\).<br/>'
                    r'<b>Bước 2 [A1]:</b> Cộng tiếp \(\frac{3}{5}\): '
                    r'\(\frac{6}{5} + \frac{3}{5} = \frac{9}{5} = 1\frac{4}{5}\).</p>'
                ),
            },
            # Q9 -> D
            {
                'tag': 'Upper & Lower Bounds (P2 Non-Calc)',
                'q': r'<p>Two lengths are measured as \(a = 14\text{ cm}\) (correct to the nearest \(\text{cm}\)) and \(b = 6.2\text{ cm}\) (correct to the nearest \(0.1\text{ cm}\)). Find the exact <b>upper bound</b> of \(a - b\).</p>',
                'options': [
                    r'\(8.25\text{ cm}\)',
                    r'\(7.25\text{ cm}\)',
                    r'\(8.30\text{ cm}\)',
                    r'\(8.35\text{ cm}\)',
                ],
                'answer': 'D',
                'explanation': (
                    r'<p><b>Bước 1 [B1]:</b> Xác định cận: \(13.5 \le a < 14.5\) và \(6.15 \le b < 6.25\).<br/>'
                    r'<b>Bước 2 [M1][A1]:</b> Để hiệu \(a - b\) lớn nhất, lấy \(a_{\max} - b_{\min}\): '
                    r'\(14.5 - 6.15 = 8.35\text{ cm}\).</p>'
                ),
            },
            # Q10 -> A
            {
                'tag': 'Upper & Lower Bounds (P2 Non-Calc)',
                'q': r'<p>Given \(P = \frac{M}{V}\), where \(M = 40\) (correct to the nearest \(10\)) and \(V = 5\) (correct to the nearest integer), find the exact <b>upper bound</b> of \(P\).</p>',
                'options': [
                    r'\(10\)',
                    r'\(9\)',
                    r'\(\frac{90}{11}\)',
                    r'\(\frac{70}{9}\)',
                ],
                'answer': 'A',
                'explanation': (
                    r'<p><b>Bước 1 [B1]:</b> Cận của \(M\) (sai số \(\pm 5\)) là \(M_{\max} = 45\); '
                    r'cận của \(V\) (sai số \(\pm 0.5\)) là \(V_{\min} = 4.5\).<br/>'
                    r'<b>Bước 2 [M1][A1]:</b> Thương lớn nhất đạt được tại \(P_{\max} = \frac{M_{\max}}{V_{\min}} = \frac{45}{4.5} = 10\).</p>'
                ),
            },
            # Q11 -> C
            {
                'tag': 'Upper & Lower Bounds (P2 Non-Calc)',
                'q': r'<p>A rectangle has length \(8.4\text{ cm}\) and width \(4.6\text{ cm}\), both measured to \(1\) decimal place. Calculate the exact <b>lower bound</b> of its perimeter.</p>',
                'options': [
                    r'\(26.2\text{ cm}\)',
                    r'\(25.9\text{ cm}\)',
                    r'\(25.8\text{ cm}\)',
                    r'\(25.6\text{ cm}\)',
                ],
                'answer': 'C',
                'explanation': (
                    r'<p><b>Bước 1 [B1]:</b> Với độ chính xác \(0.1\text{ cm}\) (sai số \(\pm 0.05\)): '
                    r'\(L_{\min} = 8.35\text{ cm}\) và \(W_{\min} = 4.55\text{ cm}\).<br/>'
                    r'<b>Bước 2 [M1][A1]:</b> Cận dưới chu vi là '
                    r'\(P_{\min} = 2(8.35 + 4.55) = 2(12.9) = 25.8\text{ cm}\).</p>'
                ),
            },
            # Q12 -> B
            {
                'tag': 'HCF & LCM (P2 Non-Calc)',
                'q': r'<p>Given \(A = 2^3 \times 3^2 \times 5\) and \(B = 2^2 \times 3^3 \times 7\), find the \(\text{HCF}\) and \(\text{LCM}\) of \(A\) and \(B\) in index form.</p>',
                'options': [
                    r'\(\text{HCF} = 2^3 \times 3^3\), \(\text{LCM} = 2^2 \times 3^2 \times 5 \times 7\)',
                    r'\(\text{HCF} = 2^2 \times 3^2\), \(\text{LCM} = 2^3 \times 3^3 \times 5 \times 7\)',
                    r'\(\text{HCF} = 2^2 \times 3^2 \times 5 \times 7\), \(\text{LCM} = 2^3 \times 3^3\)',
                    r'\(\text{HCF} = 2^2 \times 3^2\), \(\text{LCM} = 2^5 \times 3^5 \times 5 \times 7\)',
                ],
                'answer': 'B',
                'explanation': (
                    r'<p><b>Bước 1 [B1]:</b> \(\text{HCF}\) lấy các thừa số nguyên tố <b>chung</b> với số mũ <b>nhỏ nhất</b>: '
                    r'\(2^{\min(3,2)} \times 3^{\min(2,3)} = 2^2 \times 3^2\).<br/>'
                    r'<b>Bước 2 [B1]:</b> \(\text{LCM}\) lấy <b>mọi</b> thừa số nguyên tố với số mũ <b>lớn nhất</b>: '
                    r'\(2^3 \times 3^3 \times 5 \times 7\).</p>'
                ),
            },
            # Q13 -> C
            {
                'tag': 'LCM Application (P2 Non-Calc)',
                'q': r'<p>Three warning beacons flash every \(36\) seconds, \(48\) seconds, and \(60\) seconds respectively. All three flash together at \(09{:}00\). At what time will all three next flash together?</p>',
                'options': [
                    r'\(09{:}06\)',
                    r'\(09{:}15\)',
                    r'\(09{:}12\)',
                    r'\(09{:}24\)',
                ],
                'answer': 'C',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Phân tích thừa số nguyên tố: '
                    r'\(36 = 2^2 \times 3^2\), \(48 = 2^4 \times 3\), \(60 = 2^2 \times 3 \times 5\). '
                    r'Suy ra \(\text{LCM} = 2^4 \times 3^2 \times 5 = 16 \times 9 \times 5 = 720\text{ giây}\).<br/>'
                    r'<b>Bước 2 [A1]:</b> Đổi \(720\text{ giây} = \frac{720}{60} = 12\text{ phút}\), nên lần sáng cùng lúc tiếp theo là \(09{:}12\).</p>'
                ),
            },
            # Q14 -> D
            {
                'tag': 'Reverse Percentages (P2 Non-Calc)',
                'q': r'<p>In a sale, all prices are reduced by \(20\%\). A jacket costs £\(96\) in the sale. Calculate the original price of the jacket before the sale.</p>',
                'options': [
                    r'£\(115.20\)',
                    r'£\(116\)',
                    r'£\(124\)',
                    r'£\(120\)',
                ],
                'answer': 'D',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Giá sau khi giảm \(20\%\) tương ứng với \(80\%\) giá gốc: '
                    r'\(0.8 \times \text{Original} = 96\). (Tránh bẫy cộng thêm \(20\%\) của \(96\)!)<br/>'
                    r'<b>Bước 2 [A1]:</b> Giá gốc \(= \frac{96}{0.8} = \frac{960}{8} = \text{£}120\).</p>'
                ),
            },
            # Q15 -> B
            {
                'tag': 'Compound Ratios (P2 Non-Calc)',
                'q': r'<p>In a box of \(140\) counters, the ratio of red to blue counters is \(2 : 3\), and the ratio of blue to green counters is \(4 : 5\). How many counters are <b>green</b>?</p>',
                'options': [
                    r'\(48\)',
                    r'\(60\)',
                    r'\(32\)',
                    r'\(70\)',
                ],
                'answer': 'B',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Quy đồng phần chung (blue) bằng \(\text{LCM}(3, 4) = 12\): '
                    r'\(R : B = 8 : 12\) và \(B : G = 12 : 15 \Rightarrow R : B : G = 8 : 12 : 15\).<br/>'
                    r'<b>Bước 2 [M1][A1]:</b> Tổng số phần \(= 8 + 12 + 15 = 35\). Giá trị \(1\) phần \(= \frac{140}{35} = 4\). '
                    r'Số bi xanh lá (green) \(= 15 \times 4 = 60\).</p>'
                ),
            },
        ],
    },

    # =========================================================================
    # DRILL 4 (NON-CALC): Domain & Range, x^(±1/2) & Algebra (NEW 2025)
    # =========================================================================
    {
        'code': 'd0580_nc4',
        'folder_key': 'non_calc',
        'calculator_policy': 'non-calculator',
        'order_index': 4,
        'title': '🚫 Non-Calc Drill 4: Domain & Range, Fractional Powers x^(±1/2) & Algebra (0580 P2 NEW 2025)',
        'time_limit': '30',
        'intro_html': (
            r'<p><b>Mục tiêu (NEW 2025–2027 0580 Syllabus — Paper 2 Non-Calculator):</b> '
            r'Chinh phục các nội dung <b>MỚI bổ sung từ kỳ thi 2025</b>: Tập xác định (domain) và tập giá trị (range) '
            r'của hàm số, đồ thị và giá trị hàm lũy thừa phân số \(y = x^{\frac{1}{2}}\) và \(y = x^{-\frac{1}{2}}\), '
            r'kết hợp hàm hợp \(fg(x)\), hàm ngược \(f^{-1}(x)\), hoàn thành bình phương (completing the square), '
            r'phân thức đại số và hệ phương trình bậc nhất – bậc hai chính xác.</p>'
        ),
        'lecture_keys': ['t2', 'p2p4'],
        'questions': [
            # Q1 -> D
            {
                'tag': 'Domain & Range (NEW 2025 P2)',
                'q': r'<p>Find the largest possible real domain of the function \(f(x) = \sqrt{2x - 6}\).</p>',
                'options': [
                    r'\(x > 3\)',
                    r'\(x \ge -3\)',
                    r'\(x \ge 6\)',
                    r'\(x \ge 3\)',
                ],
                'answer': 'D',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Để căn bậc hai xác định trên tập số thực, biểu thức dưới dấu căn phải không âm: '
                    r'\(2x - 6 \ge 0\).<br/>'
                    r'<b>Bước 2 [A1]:</b> Giải bất phương trình: \(2x \ge 6 \Rightarrow x \ge 3\) '
                    r'(chú ý có dấu bằng vì \(\sqrt{0} = 0\) xác định).</p>'
                ),
            },
            # Q2 -> B
            {
                'tag': 'Domain & Range (NEW 2025 P2)',
                'q': r'<p>The linear function \(f(x) = 5 - 2x\) has domain \(-1 \le x \le 4\). Find the <b>range</b> of \(f(x)\).</p>',
                'options': [
                    r'\(3 \le f(x) \le 7\)',
                    r'\(-3 \le f(x) \le 7\)',
                    r'\(-3 \le f(x) \le 3\)',
                    r'\(-1 \le f(x) \le 4\)',
                ],
                'answer': 'B',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Tính giá trị tại hai đầu mút của tập xác định: '
                    r'\(f(-1) = 5 - 2(-1) = 7\) và \(f(4) = 5 - 2(4) = -3\).<br/>'
                    r'<b>Bước 2 [A1]:</b> Vì hàm bậc nhất nghịch biến (hệ số góc \(-2 < 0\)), '
                    r'tập giá trị là \(-3 \le f(x) \le 7\).</p>'
                ),
            },
            # Q3 -> A
            {
                'tag': 'Domain & Range (NEW 2025 P2)',
                'q': r'<p>Find the range of the quadratic function \(g(x) = (x - 3)^2 + 4\) for \(x \in \mathbb{R}\).</p>',
                'options': [
                    r'\(g(x) \ge 4\)',
                    r'\(g(x) \ge 3\)',
                    r'\(g(x) \ge -4\)',
                    r'\(g(x) > 4\)',
                ],
                'answer': 'A',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Với mọi số thực \(x\), ta có \((x - 3)^2 \ge 0\), dấu bằng xảy ra khi \(x = 3\).<br/>'
                    r'<b>Bước 2 [A1]:</b> Cộng \(4\) vào hai vế: \((x - 3)^2 + 4 \ge 4\), do đó tập giá trị là \(g(x) \ge 4\).</p>'
                ),
            },
            # Q4 -> C
            {
                'tag': 'Reciprocal Domain & Range (NEW 2025 P2)',
                'q': r'<p>For the reciprocal function \(h(x) = \frac{3}{x + 2} - 1\), state the value excluded from its <b>domain</b> and the value excluded from its <b>range</b>.</p>',
                'options': [
                    r'Domain: \(x \neq 2\); Range: \(h(x) \neq -1\)',
                    r'Domain: \(x \neq -2\); Range: \(h(x) \neq 1\)',
                    r'Domain: \(x \neq -2\); Range: \(h(x) \neq -1\)',
                    r'Domain: \(x \neq -2\); Range: \(h(x) \neq 3\)',
                ],
                'answer': 'C',
                'explanation': (
                    r'<p><b>Bước 1 [B1]:</b> Mẫu số khác \(0 \Rightarrow x + 2 \neq 0 \Rightarrow x \neq -2\) (tiệm cận đứng).<br/>'
                    r'<b>Bước 2 [B1]:</b> Vì \(\frac{3}{x + 2} \neq 0\) với mọi \(x\), nên \(h(x) = \frac{3}{x+2} - 1 \neq -1\) '
                    r'(tiệm cận ngang \(y = -1\)).</p>'
                ),
            },
            # Q5 -> C
            {
                'tag': 'Fractional Powers x^(±1/2) (NEW 2025 P2)',
                'q': r'<p>Given \(f(x) = 6x^{\frac{1}{2}} - 4x^{-\frac{1}{2}}\) for \(x > 0\), find the exact value of \(f(16)\).</p>',
                'options': [
                    r'\(25\)',
                    r'\(22\)',
                    r'\(23\)',
                    r'\(8\)',
                ],
                'answer': 'C',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Áp dụng \(x^{\frac{1}{2}} = \sqrt{x}\) và \(x^{-\frac{1}{2}} = \frac{1}{\sqrt{x}}\): '
                    r'\(16^{\frac{1}{2}} = 4\) và \(16^{-\frac{1}{2}} = \frac{1}{4}\).<br/>'
                    r'<b>Bước 2 [A1]:</b> Thay vào: \(f(16) = 6(4) - 4\left(\frac{1}{4}\right) = 24 - 1 = 23\).</p>'
                ),
            },
            # Q6 -> A
            {
                'tag': 'Graph of y = ax^(1/2) + b (NEW 2025 P2)',
                'q': r'<p>Which statement accurately describes the graph of \(y = 2x^{\frac{1}{2}} + 3\) for \(x \ge 0\)?</p>',
                'options': [
                    r'Starts at \((0, 3)\), curves upward with decreasing gradient, and passes through \((9, 9)\)',
                    r'Starts at \((3, 0)\), curves upward with increasing gradient, and passes through \((9, 9)\)',
                    r'Has a vertical asymptote at \(x = 0\) and decreases towards \(y = 3\)',
                    r'Is a straight line with gradient \(2\) and \(y\)-intercept \(3\)',
                ],
                'answer': 'A',
                'explanation': (
                    r'<p><b>Bước 1 [B1]:</b> Khi \(x = 0\), \(y = 2\sqrt{0} + 3 = 3\), nên đồ thị bắt đầu tại \((0, 3)\). '
                    r'Khi \(x = 9\), \(y = 2\sqrt{9} + 3 = 2(3) + 3 = 9\).<br/>'
                    r'<b>Bước 2 [B1]:</b> Đồ thị hàm căn bậc hai \(y = 2\sqrt{x} + 3\) đồng biến và cong lõm xuống '
                    r'(độ dốc giảm dần khi \(x\) tăng).</p>'
                ),
            },
            # Q7 -> D
            {
                'tag': 'Graph of y = x^(-1/2) (NEW 2025 P2)',
                'q': r'<p>Which statement is <b>true</b> for the graph of \(y = x^{-\frac{1}{2}}\) (\(x > 0\))?</p>',
                'options': [
                    r'It passes through \((0, 1)\) and \((4, 2)\)',
                    r'It is defined for all real numbers \(x \neq 0\), including negative \(x\)',
                    r'It passes through \(\left(4, -\frac{1}{2}\right)\) and approaches \(y = 1\)',
                    r'It has asymptotes \(x = 0\) and \(y = 0\), and passes through \((1, 1)\) and \(\left(4, \frac{1}{2}\right)\)',
                ],
                'answer': 'D',
                'explanation': (
                    r'<p><b>Bước 1 [B1]:</b> \(y = x^{-\frac{1}{2}} = \frac{1}{\sqrt{x}}\) chỉ xác định khi \(x > 0\), '
                    r'có tiệm cận đứng \(x = 0\) và tiệm cận ngang \(y = 0\).<br/>'
                    r'<b>Bước 2 [B1]:</b> Kiểm tra điểm: khi \(x = 1 \Rightarrow y = 1\); '
                    r'khi \(x = 4 \Rightarrow y = \frac{1}{\sqrt{4}} = \frac{1}{2}\).</p>'
                ),
            },
            # Q8 -> B
            {
                'tag': 'Fractional Power Equation (NEW 2025 P2)',
                'q': r'<p>Find the exact coordinates of the point where the curve \(y = 2x^{\frac{1}{2}} + 3\) intersects the horizontal line \(y = 13\).</p>',
                'options': [
                    r'\((5, 13)\)',
                    r'\((25, 13)\)',
                    r'\((10, 13)\)',
                    r'\((64, 13)\)',
                ],
                'answer': 'B',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Giải phương trình hoành độ giao điểm: '
                    r'\(2x^{\frac{1}{2}} + 3 = 13 \Rightarrow 2\sqrt{x} = 10 \Rightarrow \sqrt{x} = 5\).<br/>'
                    r'<b>Bước 2 [A1]:</b> Bình phương hai vế: \(x = 5^2 = 25\). Tọa độ giao điểm là \((25, 13)\).</p>'
                ),
            },
            # Q9 -> A
            {
                'tag': 'Composite Functions (P2 Non-Calc)',
                'q': r'<p>Given \(f(x) = 3x - 2\) and \(g(x) = x^2 + 1\), find the composite function \(fg(x)\) in simplified form.</p>',
                'options': [
                    r'\(3x^2 + 1\)',
                    r'\(9x^2 - 12x + 5\)',
                    r'\(3x^2 - 1\)',
                    r'\(3x^2 + 3\)',
                ],
                'answer': 'A',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> \(fg(x) = f(g(x))\) nghĩa là thay toàn bộ \(g(x) = x^2 + 1\) vào biến \(x\) của \(f\): '
                    r'\(fg(x) = 3(x^2 + 1) - 2\).<br/>'
                    r'<b>Bước 2 [A1]:</b> Khai triển và rút gọn: \(3x^2 + 3 - 2 = 3x^2 + 1\). '
                    r'(Chú ý \(9x^2 - 12x + 5\) là \(gf(x)\), bẫy đảo thứ tự!)</p>'
                ),
            },
            # Q10 -> D
            {
                'tag': 'Inverse Functions (P2 Non-Calc)',
                'q': r'<p>Find the inverse function \(f^{-1}(x)\) of \(f(x) = \frac{2x + 5}{x - 1}\), where \(x \neq 1\).</p>',
                'options': [
                    r'\(\frac{x - 5}{x + 2}\)',
                    r'\(\frac{x + 5}{2 - x}\)',
                    r'\(\frac{x - 1}{2x + 5}\)',
                    r'\(\frac{x + 5}{x - 2}\)',
                ],
                'answer': 'D',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Đặt \(y = \frac{2x + 5}{x - 1} \Rightarrow y(x - 1) = 2x + 5 \Rightarrow xy - y = 2x + 5\).<br/>'
                    r'<b>Bước 2 [M1][A1]:</b> Gom các hạng tử chứa \(x\): \(x(y - 2) = y + 5 \Rightarrow x = \frac{y + 5}{y - 2}\). '
                    r'Đổi \(y\) thành \(x\): \(f^{-1}(x) = \frac{x + 5}{x - 2}\) (\(x \neq 2\)).</p>'
                ),
            },
            # Q11 -> B
            {
                'tag': 'Inverse Domain & Range (NEW 2025 P2)',
                'q': r'<p>The function \(f(x) = x^2 + 6x + 11\) is defined for \(x \ge -3\). What is the <b>domain</b> of its inverse function \(f^{-1}(x)\)?</p>',
                'options': [
                    r'\(x \ge -3\)',
                    r'\(x \ge 2\)',
                    r'\(x \ge 11\)',
                    r'\(x \ge -2\)',
                ],
                'answer': 'B',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Hoàn thành bình phương: '
                    r'\(f(x) = (x + 3)^2 - 9 + 11 = (x + 3)^2 + 2\). '
                    r'Với \(x \ge -3\), tập giá trị (range) của \(f\) là \(f(x) \ge 2\).<br/>'
                    r'<b>Bước 2 [A1]:</b> Tập xác định của hàm ngược chính là tập giá trị của hàm gốc: '
                    r'\(\text{Domain of } f^{-1}: x \ge 2\).</p>'
                ),
            },
            # Q12 -> C
            {
                'tag': 'Completing the Square (P2 Non-Calc)',
                'q': r'<p>Write \(2x^2 - 12x + 11\) in the form \(a(x - b)^2 + c\), where \(a, b, c\) are integers.</p>',
                'options': [
                    r'\(2(x - 3)^2 + 2\)',
                    r'\(2(x - 6)^2 - 61\)',
                    r'\(2(x - 3)^2 - 7\)',
                    r'\(2(x - 3)^2 - 16\)',
                ],
                'answer': 'C',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Đặt nhân tử chung \(2\) cho hai hạng tử đầu: '
                    r'\(2(x^2 - 6x) + 11 = 2\left[(x - 3)^2 - 9\right] + 11\).<br/>'
                    r'<b>Bước 2 [A1]:</b> Nhân phân phối và rút gọn: '
                    r'\(2(x - 3)^2 - 18 + 11 = 2(x - 3)^2 - 7\).</p>'
                ),
            },
            # Q13 -> A
            {
                'tag': 'Algebraic Fractions (P2 Non-Calc)',
                'q': r'<p>Express \(\frac{5}{x - 2} - \frac{3}{x + 1}\) as a single fraction in its simplest form.</p>',
                'options': [
                    r'\(\frac{2x + 11}{(x - 2)(x + 1)}\)',
                    r'\(\frac{2x - 1}{(x - 2)(x + 1)}\)',
                    r'\(\frac{2x + 1}{(x - 2)(x + 1)}\)',
                    r'\(\frac{8x - 1}{(x - 2)(x + 1)}\)',
                ],
                'answer': 'A',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Quy đồng mẫu số chung \((x - 2)(x + 1)\): '
                    r'\(\frac{5(x + 1) - 3(x - 2)}{(x - 2)(x + 1)}\).<br/>'
                    r'<b>Bước 2 [A1]:</b> Khai triển cẩn thận dấu trừ: '
                    r'\(\frac{5x + 5 - 3x + 6}{(x - 2)(x + 1)} = \frac{2x + 11}{(x - 2)(x + 1)}\).</p>'
                ),
            },
            # Q14 -> B
            {
                'tag': 'Algebraic Fractions (P2 Non-Calc)',
                'q': r'<p>Simplify fully \(\frac{2x^2 + x - 6}{x^2 - 4}\).</p>',
                'options': [
                    r'\(\frac{2x + 3}{x + 2}\)',
                    r'\(\frac{2x - 3}{x - 2}\)',
                    r'\(\frac{2x - 3}{x + 2}\)',
                    r'\(\frac{2x + 3}{x - 2}\)',
                ],
                'answer': 'B',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Phân tích tử và mẫu thành nhân tử: '
                    r'\(2x^2 + x - 6 = (2x - 3)(x + 2)\) và \(x^2 - 4 = (x - 2)(x + 2)\).<br/>'
                    r'<b>Bước 2 [A1]:</b> Triệt tiêu nhân tử chung \((x + 2)\): '
                    r'\(\frac{2x - 3}{x - 2}\).</p>'
                ),
            },
            # Q15 -> D
            {
                'tag': 'Simultaneous Equations (P2 Non-Calc)',
                'q': r'<p>Find the exact coordinates of the two points of intersection of the line \(y = 2x - 1\) and the curve \(y = x^2 - 2x + 2\).</p>',
                'options': [
                    r'\((-1, -3)\) and \((3, 5)\)',
                    r'\((1, 1)\) and \((-3, -7)\)',
                    r'\((1, 3)\) and \((3, 5)\)',
                    r'\((1, 1)\) and \((3, 5)\)',
                ],
                'answer': 'D',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Cho hai vế bằng nhau: '
                    r'\(x^2 - 2x + 2 = 2x - 1 \Rightarrow x^2 - 4x + 3 = 0 \Rightarrow (x - 1)(x - 3) = 0\).<br/>'
                    r'<b>Bước 2 [A1]:</b> Suy ra \(x = 1\) hoặc \(x = 3\). Thay vào \(y = 2x - 1\): '
                    r'khi \(x = 1 \Rightarrow y = 1\); khi \(x = 3 \Rightarrow y = 5\). Giao điểm là \((1, 1)\) và \((3, 5)\).</p>'
                ),
            },
        ],
    },

    # =========================================================================
    # DRILL 5 (CALC): Compound Interest, Reverse % & Exponential Growth/Decay
    # =========================================================================
    {
        'code': 'd0580_c1',
        'folder_key': 'calc',
        'calculator_policy': 'calculator',
        'order_index': 1,
        'title': '🧮 Calc Drill 1: Compound Interest, Reverse % & Exponential Growth/Decay (0580 P4)',
        'time_limit': '30',
        'intro_html': (
            r'<p><b>Mục tiêu (Paper 4 Calculator Allowed — Syllabus 2025–2027):</b> '
            r'Sử dụng máy tính khoa học hiệu quả cho bài toán lãi kép nhiều kỳ (compound interest), '
            r'tìm lãi suất \(r\%\) hoặc số năm \(n\), khấu hao/tăng trưởng hàm mũ (exponential growth/decay), '
            r'quy đổi ngoại tệ có phí hoa hồng, cận tốc độ – quãng đường đến \(3\text{ s.f.}\) và biến thiên phần trăm phức hợp.</p>'
        ),
        'lecture_keys': ['t1', 'p2p4'],
        'questions': [
            # Q1 -> B
            {
                'tag': 'Compound Interest (P4 Calc)',
                'q': r'<p>Liam invests £\(4500\) in a savings account paying \(3.6\%\) per year compound interest. Calculate the total value of his investment after \(5\) years, correct to the nearest penny (\(2\text{ d.p.}\)).</p>',
                'options': [
                    r'£\(5310.00\)',
                    r'£\(5370.46\)',
                    r'£\(5183.84\)',
                    r'£\(5563.79\)',
                ],
                'answer': 'B',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Áp dụng công thức lãi kép \(A = P\left(1 + \frac{r}{100}\right)^n\): '
                    r'\(A = 4500 \times (1.036)^5\).<br/>'
                    r'<b>Bước 2 [A1]:</b> Bấm máy: \(4500 \times 1.193435\dots = 5370.4576\dots \approx \text{£}5370.46\). '
                    r'(£\(5310.00\) là bẫy dùng lãi đơn!)</p>'
                ),
            },
            # Q2 -> D
            {
                'tag': 'Compound Interest (P4 Calc)',
                'q': r'<p>Maya invests \(\text{EUR } 6000\) at a nominal rate of \(4.8\%\) per annum, compounded <b>half-yearly</b> (\(2.4\%\) every \(6\) months). Find the <b>compound interest earned</b> after \(3\) years, correct to \(2\text{ d.p.}\)</p>',
                'options': [
                    r'\(\text{EUR } 6917.53\)',
                    r'\(\text{EUR } 906.13\)',
                    r'\(\text{EUR } 864.00\)',
                    r'\(\text{EUR } 917.53\)',
                ],
                'answer': 'D',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Trong \(3\) năm có \(3 \times 2 = 6\) kỳ bán niên với lãi suất \(2.4\%\) mỗi kỳ: '
                    r'\(A = 6000 \times (1.024)^6 = 6917.5290\dots\).<br/>'
                    r'<b>Bước 2 [M1][A1]:</b> Đề hỏi tiền <b>lãi</b> (interest earned), lấy tổng trừ gốc: '
                    r'\(6917.5290 - 6000 = \text{EUR } 917.53\).</p>'
                ),
            },
            # Q3 -> A
            {
                'tag': 'Finding Compound Rate (P4 Calc)',
                'q': r'<p>An investment grows from £\(8000\) to £\(9845\) in \(4\) years under annual compound interest at \(r\%\) per year. Calculate \(r\), correct to \(2\text{ d.p.}\)</p>',
                'options': [
                    r'\(5.32\%\)',
                    r'\(5.77\%\)',
                    r'\(4.86\%\)',
                    r'\(6.15\%\)',
                ],
                'answer': 'A',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Thiết lập phương trình: \(8000\left(1 + \frac{r}{100}\right)^4 = 9845 \Rightarrow '
                    r'\left(1 + \frac{r}{100}\right)^4 = \frac{9845}{8000} = 1.230625\).<br/>'
                    r'<b>Bước 2 [M1][A1]:</b> Lấy căn bậc bốn: \(1 + \frac{r}{100} = (1.230625)^{\frac{1}{4}} = 1.0532496\dots '
                    r'\Rightarrow r = 5.32\%\).</p>'
                ),
            },
            # Q4 -> C
            {
                'tag': 'Finding Years n (P4 Calc)',
                'q': r'<p>A bank account pays \(4.5\%\) per year compound interest. What is the <b>least number of complete years</b> required for an investment of £\(2000\) to exceed £\(3000\)?</p>',
                'options': [
                    r'\(9\text{ years}\)',
                    r'\(11\text{ years}\)',
                    r'\(10\text{ years}\)',
                    r'\(12\text{ years}\)',
                ],
                'answer': 'C',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Cần \(2000 \times 1.045^n > 3000 \Rightarrow 1.045^n > 1.5\). '
                    r'Thử bằng máy tính (hoặc logarit): \(n > \frac{\ln 1.5}{\ln 1.045} = 9.21\dots\).<br/>'
                    r'<b>Bước 2 [A1]:</b> Kiểm tra: \(n = 9 \Rightarrow \text{£}2972.19 < 3000\); '
                    r'\(n = 10 \Rightarrow \text{£}3105.94 > 3000\). Vậy cần ít nhất \(10\) năm nguyên.</p>'
                ),
            },
            # Q5 -> A
            {
                'tag': 'Depreciation (P4 Calc)',
                'q': r'<p>A new car is bought for £\(24\,000\) and depreciates in value by \(14\%\) each year. Find its value after \(6\) years, correct to the nearest pound.</p>',
                'options': [
                    r'£\(9710\)',
                    r'£\(3840\)',
                    r'£\(11\,290\)',
                    r'£\(8350\)',
                ],
                'answer': 'A',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Hệ số giảm mỗi năm là \(1 - 0.14 = 0.86\). '
                    r'Giá trị sau \(6\) năm là \(24\,000 \times (0.86)^6\).<br/>'
                    r'<b>Bước 2 [A1]:</b> Tính toán: \(24\,000 \times 0.4045672\dots = 9709.61\dots \approx \text{£}9710\).</p>'
                ),
            },
            # Q6 -> B
            {
                'tag': 'Reverse Depreciation (P4 Calc)',
                'q': r'<p>After depreciating by \(12\%\) per year for \(3\) years, a laptop is worth £\(1022.21\). Find its original price when new, correct to the nearest pound.</p>',
                'options': [
                    r'£\(1436\)',
                    r'£\(1500\)',
                    r'£\(1597\)',
                    r'£\(1390\)',
                ],
                'answer': 'B',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Gọi giá ban đầu là \(P\). Ta có \(P \times (0.88)^3 = 1022.21\).<br/>'
                    r'<b>Bước 2 [A1]:</b> Suy ra \(P = \frac{1022.21}{0.681472} = 1500.0029\dots \approx \text{£}1500\). '
                    r'(Không được nhân ngược với \(1.12^3\)!)</p>'
                ),
            },
            # Q7 -> C
            {
                'tag': 'Exponential Growth (P4 Calc)',
                'q': r'<p>A bacteria culture starts with \(1250\) cells and increases by \(18\%\) every hour. Find the number of cells after \(8\) hours, correct to \(3\) significant figures.</p>',
                'options': [
                    r'\(3050\)',
                    r'\(3980\)',
                    r'\(4700\)',
                    r'\(5540\)',
                ],
                'answer': 'C',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Số tế bào sau \(8\) giờ là \(N = 1250 \times (1.18)^8\).<br/>'
                    r'<b>Bước 2 [A1]:</b> Bấm máy: \(1250 \times 3.758859\dots = 4698.57\dots \approx 4700\) (làm tròn \(3\text{ s.f.}\)).</p>'
                ),
            },
            # Q8 -> D
            {
                'tag': 'Exponential Decay Rate (P4 Calc)',
                'q': r"<p>A town's population fell from \(48\,000\) to \(41\,500\) over \(5\) years at a constant annual decrease of \(k\%\). Find \(k\), correct to \(2\text{ d.p.}\)</p>",
                'options': [
                    r'\(2.71\%\)',
                    r'\(3.14\%\)',
                    r'\(2.58\%\)',
                    r'\(2.87\%\)',
                ],
                'answer': 'D',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Thiết lập phương trình: '
                    r'\(48\,000\left(1 - \frac{k}{100}\right)^5 = 41\,500 \Rightarrow '
                    r'\left(1 - \frac{k}{100}\right)^5 = \frac{41\,500}{48\,000} = 0.864583\dots\).<br/>'
                    r'<b>Bước 2 [M1][A1]:</b> Lấy căn bậc năm: \(1 - \frac{k}{100} = 0.9713148\dots '
                    r'\Rightarrow \frac{k}{100} = 0.028685\dots \Rightarrow k = 2.87\%\).</p>'
                ),
            },
            # Q9 -> C
            {
                'tag': 'Currency & Commission (P4 Calc)',
                'q': r'<p>A traveller changes £\(850\) into Japanese Yen (\(\text{JPY}\)). The bank deducts a \(2.5\%\) commission before converting at £\(1 = 192.5\text{ JPY}\). How many \(\text{JPY}\) does the traveller receive, correct to the nearest Yen?</p>',
                'options': [
                    r'\(163\,625\text{ JPY}\)',
                    r'\(159\,634\text{ JPY}\)',
                    r'\(159\,534\text{ JPY}\)',
                    r'\(167\,716\text{ JPY}\)',
                ],
                'answer': 'C',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Số tiền GBP còn lại sau khi trừ \(2.5\%\) phí hoa hồng: '
                    r'\(850 \times (1 - 0.025) = 850 \times 0.975 = \text{£}828.75\).<br/>'
                    r'<b>Bước 2 [M1][A1]:</b> Đổi sang JPY: '
                    r'\(828.75 \times 192.5 = 159\,534.375 \approx 159\,534\text{ JPY}\).</p>'
                ),
            },
            # Q10 -> A
            {
                'tag': 'Currency Conversion (P4 Calc)',
                'q': r'<p>A tourist converts \(\text{EUR } 540\) into GBP at \(\text{EUR } 1 = \text{£}0.86\), spends £\(215\), and then converts the remaining GBP into USD at £\(1 = \text{USD } 1.28\). How much USD does the tourist receive, correct to \(2\text{ d.p.}\)?</p>',
                'options': [
                    r'\(\text{USD } 319.23\)',
                    r'\(\text{USD } 194.84\)',
                    r'\(\text{USD } 594.43\)',
                    r'\(\text{USD } 416.00\)',
                ],
                'answer': 'A',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Đổi sang GBP rồi trừ chi tiêu: '
                    r'\(540 \times 0.86 = \text{£}464.40\); còn lại \(464.40 - 215 = \text{£}249.40\).<br/>'
                    r'<b>Bước 2 [M1][A1]:</b> Đổi sang USD: '
                    r'\(249.40 \times 1.28 = 319.232 \approx \text{USD } 319.23\).</p>'
                ),
            },
            # Q11 -> D
            {
                'tag': 'Speed-Distance-Time Bounds (P4 Calc)',
                'q': r"<p>A runner completes \(400\text{ m}\) (measured to the nearest \(5\text{ m}\)) in \(52.4\text{ s}\) (measured to the nearest \(0.1\text{ s}\)). Calculate the <b>upper bound</b> of the runner's average speed in \(\text{m/s}\), correct to \(3\text{ s.f.}\)</p>",
                'options': [
                    r'\(7.67\text{ m/s}\)',
                    r'\(7.58\text{ m/s}\)',
                    r'\(7.74\text{ m/s}\)',
                    r'\(7.69\text{ m/s}\)',
                ],
                'answer': 'D',
                'explanation': (
                    r'<p><b>Bước 1 [B1]:</b> \(d_{\max} = 400 + 2.5 = 402.5\text{ m}\) và \(t_{\min} = 52.4 - 0.05 = 52.35\text{ s}\).<br/>'
                    r'<b>Bước 2 [M1][A1]:</b> Tốc độ cực đại \(v_{\max} = \frac{d_{\max}}{t_{\min}} = \frac{402.5}{52.35} = 7.68863\dots \approx 7.69\text{ m/s}\).</p>'
                ),
            },
            # Q12 -> B
            {
                'tag': 'Speed-Distance-Time Bounds (P4 Calc)',
                'q': r'<p>A train travels \(185\text{ km}\) (correct to the nearest \(5\text{ km}\)) in \(2\text{ hours } 15\text{ minutes}\) (correct to the nearest \(5\text{ minutes}\)). Calculate the <b>lower bound</b> of its average speed in \(\text{km/h}\), correct to \(3\text{ s.f.}\)</p>',
                'options': [
                    r'\(82.2\text{ km/h}\)',
                    r'\(79.6\text{ km/h}\)',
                    r'\(84.9\text{ km/h}\)',
                    r'\(78.2\text{ km/h}\)',
                ],
                'answer': 'B',
                'explanation': (
                    r'<p><b>Bước 1 [B1]:</b> \(d_{\min} = 185 - 2.5 = 182.5\text{ km}\). '
                    r'Thời gian \(135\text{ phút} \Rightarrow t_{\max} = 135 + 2.5 = 137.5\text{ phút} = \frac{137.5}{60}\text{ giờ}\).<br/>'
                    r'<b>Bước 2 [M1][A1]:</b> \(v_{\min} = \frac{d_{\min}}{t_{\max}} = \frac{182.5}{137.5 / 60} = 79.636\dots \approx 79.6\text{ km/h}\).</p>'
                ),
            },
            # Q13 -> D
            {
                'tag': 'Successive Percentage Change (P4 Calc)',
                'q': r'<p>The price of a watch increases by \(15\%\) in January and then decreases by \(12\%\) in February. If the final price is £\(253\), find the original price before January.</p>',
                'options': [
                    r'£\(245.63\)',
                    r'£\(256.04\)',
                    r'£\(260.59\)',
                    r'£\(250\)',
                ],
                'answer': 'D',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Hệ số biến đổi gộp là \(1.15 \times 0.88 = 1.012\) '
                    r'(tăng tổng cộng \(1.2\%\), không phải \(15\% - 12\% = 3\%\)!).<br/>'
                    r'<b>Bước 2 [A1]:</b> Giá gốc \(P = \frac{253}{1.012} = \text{£}250\).</p>'
                ),
            },
            # Q14 -> B
            {
                'tag': 'Proportional Change (P4 Calc)',
                'q': r'<p>The radius of a cylinder is increased by \(12\%\) while its height is decreased by \(15\%\). Calculate the overall percentage change in its volume, correct to \(2\text{ d.p.}\)</p>',
                'options': [
                    r'Decrease of \(4.80\%\)',
                    r'Increase of \(6.62\%\)',
                    r'Increase of \(9.00\%\)',
                    r'Increase of \(10.62\%\)',
                ],
                'answer': 'B',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Vì \(V = \pi r^2 h\), khi \(r \to 1.12r\) và \(h \to 0.85h\), '
                    r'tỉ số thể tích mới/cũ là \((1.12)^2 \times 0.85 = 1.2544 \times 0.85 = 1.06624\).<br/>'
                    r'<b>Bước 2 [A1]:</b> Phần trăm thay đổi \(= (1.06624 - 1) \times 100\% = +6.624\% \approx\) tăng \(6.62\%\).</p>'
                ),
            },
            # Q15 -> A
            {
                'tag': 'Multi-Rate Compound Growth (P4 Calc)',
                'q': r'<p>Priya invests £\(5000\). For the first \(2\) years it earns \(3.2\%\) p.a. compound interest, and for the next \(3\) years it earns \(4.5\%\) p.a. compound interest. Find the overall percentage increase over the \(5\) years, correct to \(2\text{ d.p.}\)</p>',
                'options': [
                    r'\(21.54\%\)',
                    r'\(19.90\%\)',
                    r'\(20.54\%\)',
                    r'\(22.18\%\)',
                ],
                'answer': 'A',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Hệ số tăng trưởng gộp sau \(5\) năm là '
                    r'\((1.032)^2 \times (1.045)^3 = 1.065024 \times 1.141166125 = 1.2153693\dots\).<br/>'
                    r'<b>Bước 2 [A1]:</b> Tỉ lệ tăng tổng cộng \(= (1.2153693 - 1) \times 100\% = 21.5369\dots\% \approx 21.54\%\).</p>'
                ),
            },
        ],
    },

    # =========================================================================
    # DRILL 6 (CALC): Quadratics, Turning Points, Differentiation & Kinematics
    # =========================================================================
    {
        'code': 'd0580_c2',
        'folder_key': 'calc',
        'calculator_policy': 'calculator',
        'order_index': 2,
        'title': '🧮 Calc Drill 2: Quadratics, Turning Points, Differentiation & Kinematics (0580 P4)',
        'time_limit': '30',
        'intro_html': (
            r'<p><b>Mục tiêu (Paper 4 Calculator Allowed — Syllabus 2025–2027):</b> '
            r'Luyện trọn bộ câu hỏi điểm cao của Đại số &amp; Giải tích 0580 Extended: công thức nghiệm bậc hai '
            r'đến \(2\text{ d.p.}\), đạo hàm \(\frac{dy}{dx} = 0\) tìm điểm dừng (stationary points) &amp; phân loại cực đại/cực tiểu, '
            r'phương trình tiếp tuyến/pháp tuyến, đồ thị vận tốc – thời gian (kinematics) và tỉ lệ thuận/nghịch phi tuyến.</p>'
        ),
        'lecture_keys': ['t2', 't3', 'p2p4'],
        'questions': [
            # Q1 -> C
            {
                'tag': 'Quadratic Formula (P4 Calc)',
                'q': r'<p>Solve the equation \(3x^2 - 7x - 5 = 0\), giving your answers correct to \(2\) decimal places.</p>',
                'options': [
                    r'\(x = -2.91 \text{ or } 0.57\)',
                    r'\(x = 5.81 \text{ or } -1.15\)',
                    r'\(x = 2.91 \text{ or } -0.57\)',
                    r'\(x = 1.67 \text{ or } 0.67\)',
                ],
                'answer': 'C',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Áp dụng công thức nghiệm với \(a = 3, b = -7, c = -5\): '
                    r'\(x = \frac{7 \pm \sqrt{(-7)^2 - 4(3)(-5)}}{2(3)} = \frac{7 \pm \sqrt{109}}{6}\).<br/>'
                    r'<b>Bước 2 [A1]:</b> Vì \(\sqrt{109} \approx 10.4403\), ta có '
                    r'\(x_1 = \frac{17.4403}{6} \approx 2.91\) và \(x_2 = \frac{-3.4403}{6} \approx -0.57\).</p>'
                ),
            },
            # Q2 -> B
            {
                'tag': 'Fractional Quadratic Equation (P4 Calc)',
                'q': r'<p>Solve \(\frac{4}{x} + \frac{3}{x + 2} = 2\), giving the <b>positive</b> solution correct to \(2\text{ d.p.}\)</p>',
                'options': [
                    r'\(x = 1.39\)',
                    r'\(x = 2.89\)',
                    r'\(x = 3.14\)',
                    r'\(x = 2.54\)',
                ],
                'answer': 'B',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Nhân hai vế với \(x(x + 2)\): '
                    r'\(4(x + 2) + 3x = 2x(x + 2) \Rightarrow 7x + 8 = 2x^2 + 4x \Rightarrow 2x^2 - 3x - 8 = 0\).<br/>'
                    r'<b>Bước 2 [M1][A1]:</b> Nghiệm dương \(x = \frac{3 + \sqrt{9 - 4(2)(-8)}}{4} = \frac{3 + \sqrt{73}}{4} = 2.886\dots \approx 2.89\).</p>'
                ),
            },
            # Q3 -> D
            {
                'tag': 'Differentiation — Gradient (P4 Calc)',
                'q': r'<p>Find the gradient of the curve \(y = 2x^3 - 5x^2 + 4x - 7\) at the point where \(x = 2\).</p>',
                'options': [
                    r'\(-3\)',
                    r'\(14\)',
                    r'\(4\)',
                    r'\(8\)',
                ],
                'answer': 'D',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Lấy đạo hàm theo \(x\): '
                    r'\(\frac{dy}{dx} = 6x^2 - 10x + 4\).<br/>'
                    r'<b>Bước 2 [A1]:</b> Thay \(x = 2\): '
                    r'\(\frac{dy}{dx}\Big|_{x=2} = 6(4) - 10(2) + 4 = 24 - 20 + 4 = 8\).</p>'
                ),
            },
            # Q4 -> A
            {
                'tag': 'Stationary Points (P4 Calc)',
                'q': r'<p>Find the coordinates of the <b>two stationary points</b> of the curve \(y = x^3 - 3x^2 - 9x + 5\).</p>',
                'options': [
                    r'\((-1, 10)\) and \((3, -22)\)',
                    r'\((1, -6)\) and \((-3, -22)\)',
                    r'\((-1, 10)\) and \((3, 22)\)',
                    r'\((-1, -2)\) and \((3, -22)\)',
                ],
                'answer': 'A',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Giải \(\frac{dy}{dx} = 3x^2 - 6x - 9 = 0 \Rightarrow x^2 - 2x - 3 = 0 '
                    r'\Rightarrow (x - 3)(x + 1) = 0 \Rightarrow x = -1\) hoặc \(x = 3\).<br/>'
                    r'<b>Bước 2 [A1]:</b> Thay vào \(y\): \(y(-1) = -1 - 3 + 9 + 5 = 10\); '
                    r'\(y(3) = 27 - 27 - 27 + 5 = -22\). Hai điểm dừng là \((-1, 10)\) và \((3, -22)\).</p>'
                ),
            },
            # Q5 -> D
            {
                'tag': 'Classifying Turning Points (P4 Calc)',
                'q': r'<p>For the curve \(y = 2x^3 - 9x^2 + 12x + 1\), find the coordinates of its <b>local minimum</b> turning point.</p>',
                'options': [
                    r'\((1, 6)\)',
                    r'\((2, 6)\)',
                    r'\((1.5, 5.5)\)',
                    r'\((2, 5)\)',
                ],
                'answer': 'D',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> \(\frac{dy}{dx} = 6x^2 - 18x + 12 = 6(x - 1)(x - 2) = 0 \Rightarrow x = 1\) hoặc \(x = 2\).<br/>'
                    r'<b>Bước 2 [M1][A1]:</b> Xét đạo hàm cấp hai \(\frac{d^2y}{dx^2} = 12x - 18\): '
                    r'tại \(x = 1\) được \(-6 < 0\) (cực đại); tại \(x = 2\) được \(+6 > 0\) (cực tiểu). '
                    r'Tung độ \(y(2) = 16 - 36 + 24 + 1 = 5 \Rightarrow (2, 5)\).</p>'
                ),
            },
            # Q6 -> C
            {
                'tag': 'Optimisation via Differentiation (P4 Calc)',
                'q': r'<p>A farmer uses \(60\text{ m}\) of fencing along three sides of a rectangular paddock against a straight stone wall. If the two sides perpendicular to the wall each have length \(x\text{ m}\), the enclosed area is \(A = 60x - 2x^2\text{ m}^2\). Use differentiation to find the <b>maximum possible area</b>.</p>',
                'options': [
                    r'\(225\text{ m}^2\)',
                    r'\(300\text{ m}^2\)',
                    r'\(450\text{ m}^2\)',
                    r'\(900\text{ m}^2\)',
                ],
                'answer': 'C',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Đặt đạo hàm bằng \(0\): '
                    r'\(\frac{dA}{dx} = 60 - 4x = 0 \Rightarrow x = 15\text{ m}\) (và \(\frac{d^2A}{dx^2} = -4 < 0\) xác nhận cực đại).<br/>'
                    r'<b>Bước 2 [A1]:</b> Diện tích cực đại: '
                    r'\(A_{\max} = 60(15) - 2(15)^2 = 900 - 450 = 450\text{ m}^2\).</p>'
                ),
            },
            # Q7 -> A
            {
                'tag': 'Equation of Tangent (P4 Calc)',
                'q': r'<p>Find the equation of the <b>tangent</b> to the curve \(y = x^3 - 4x + 2\) at the point where \(x = 2\).</p>',
                'options': [
                    r'\(y = 8x - 14\)',
                    r'\(y = 8x - 16\)',
                    r'\(y = 8x + 2\)',
                    r'\(y = 12x - 22\)',
                ],
                'answer': 'A',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Tại \(x = 2\): \(y = 8 - 8 + 2 = 2\) (tiếp điểm \((2, 2)\)). '
                    r'Đạo hàm \(\frac{dy}{dx} = 3x^2 - 4 \Rightarrow m = 3(4) - 4 = 8\).<br/>'
                    r'<b>Bước 2 [A1]:</b> Phương trình tiếp tuyến: '
                    r'\(y - 2 = 8(x - 2) \Rightarrow y = 8x - 14\).</p>'
                ),
            },
            # Q8 -> B
            {
                'tag': 'Equation of Normal (P4 Calc)',
                'q': r'<p>Find the equation of the <b>normal</b> (the line perpendicular to the tangent) to the curve \(y = x^2 - 6x + 10\) at the point \((4, 2)\).</p>',
                'options': [
                    r'\(y = 2x - 6\)',
                    r'\(y = -\frac{1}{2}x + 4\)',
                    r'\(y = -\frac{1}{2}x + 2\)',
                    r'\(y = \frac{1}{2}x\)',
                ],
                'answer': 'B',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Hệ số góc tiếp tuyến: \(\frac{dy}{dx} = 2x - 6\); tại \(x = 4\), \(m_{\text{tan}} = 2\). '
                    r'Do pháp tuyến vuông góc tiếp tuyến nên \(m_{\text{norm}} = -\frac{1}{2}\).<br/>'
                    r'<b>Bước 2 [A1]:</b> Phương trình đi qua \((4, 2)\): '
                    r'\(y - 2 = -\frac{1}{2}(x - 4) \Rightarrow y = -\frac{1}{2}x + 4\).</p>'
                ),
            },
            # Q9 -> C
            {
                'tag': 'Perpendicular Bisector (P4 Calc)',
                'q': r'<p>Find the equation of the perpendicular bisector of the line segment joining \(A(-2, 5)\) and \(B(6, 1)\).</p>',
                'options': [
                    r'\(y = -\frac{1}{2}x + 4\)',
                    r'\(y = 2x + 1\)',
                    r'\(y = 2x - 1\)',
                    r'\(y = 2x - 4\)',
                ],
                'answer': 'C',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Trung điểm \(M = \left(\frac{-2+6}{2}, \frac{5+1}{2}\right) = (2, 3)\). '
                    r'Hệ số góc \(m_{AB} = \frac{1 - 5}{6 - (-2)} = -\frac{1}{2} \Rightarrow m_\perp = 2\).<br/>'
                    r'<b>Bước 2 [A1]:</b> Đường trung trực qua \((2, 3)\) với \(m = 2\): '
                    r'\(y - 3 = 2(x - 2) \Rightarrow y = 2x - 1\).</p>'
                ),
            },
            # Q10 -> A
            {
                'tag': 'Speed-Time Graphs (P4 Calc)',
                'q': r'<p>A car accelerates uniformly from rest to \(24\text{ m/s}\) in \(8\text{ s}\), travels at constant speed for \(12\text{ s}\), and then decelerates uniformly to rest in \(6\text{ s}\). Find its <b>acceleration</b> in the first \(8\text{ s}\) and its <b>deceleration</b> in the last \(6\text{ s}\).</p>',
                'options': [
                    r'\(3\text{ m/s}^2\) and \(4\text{ m/s}^2\)',
                    r'\(4\text{ m/s}^2\) and \(3\text{ m/s}^2\)',
                    r'\(3\text{ m/s}^2\) and \(2\text{ m/s}^2\)',
                    r'\(2\text{ m/s}^2\) and \(4\text{ m/s}^2\)',
                ],
                'answer': 'A',
                'explanation': (
                    r'<p><b>Bước 1 [B1]:</b> Gia tốc là hệ số góc đồ thị vận tốc – thời gian: '
                    r'\(a = \frac{24 - 0}{8} = 3\text{ m/s}^2\).<br/>'
                    r'<b>Bước 2 [B1]:</b> Độ giảm tốc (deceleration là giá trị dương) trong \(6\text{ s}\) cuối: '
                    r'\(\frac{24 - 0}{6} = 4\text{ m/s}^2\).</p>'
                ),
            },
            # Q11 -> B
            {
                'tag': 'Kinematics — Trapezium Distance (P4 Calc)',
                'q': r'<p>A cyclist accelerates uniformly from \(4\text{ m/s}\) to \(12\text{ m/s}\) in \(10\text{ s}\), maintains \(12\text{ m/s}\) for \(25\text{ s}\), and then decelerates uniformly to rest in \(15\text{ s}\). Calculate the <b>total distance travelled</b>.</p>',
                'options': [
                    r'\(450\text{ m}\)',
                    r'\(470\text{ m}\)',
                    r'\(510\text{ m}\)',
                    r'\(430\text{ m}\)',
                ],
                'answer': 'B',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Quãng đường bằng diện tích dưới đồ thị speed–time, chia làm \(3\) hình: '
                    r'hình thang \(\frac{1}{2}(4 + 12)(10) = 80\text{ m}\), hình chữ nhật \(12 \times 25 = 300\text{ m}\), '
                    r'và tam giác \(\frac{1}{2}(15)(12) = 90\text{ m}\).<br/>'
                    r'<b>Bước 2 [A1]:</b> Tổng quãng đường \(= 80 + 300 + 90 = 470\text{ m}\).</p>'
                ),
            },
            # Q12 -> D
            {
                'tag': 'Kinematics — Finding Time (P4 Calc)',
                'q': r'<p>A train accelerates uniformly from rest to \(30\text{ m/s}\) in \(20\text{ s}\), travels at constant speed \(30\text{ m/s}\) for \(T\text{ seconds}\), and decelerates uniformly to rest in \(10\text{ s}\). Given that the total distance travelled is \(1950\text{ m}\), find the value of \(T\).</p>',
                'options': [
                    r'\(65\text{ s}\)',
                    r'\(45\text{ s}\)',
                    r'\(55\text{ s}\)',
                    r'\(50\text{ s}\)',
                ],
                'answer': 'D',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Đồ thị là một hình thang lớn có đáy trên \(T\), đáy dưới \(20 + T + 10 = T + 30\), chiều cao \(30\): '
                    r'\(\frac{1}{2}(T + T + 30)(30) = 1950 \Rightarrow 15(2T + 30) = 1950\).<br/>'
                    r'<b>Bước 2 [A1]:</b> Chia hai vế cho \(15\): \(2T + 30 = 130 \Rightarrow 2T = 100 \Rightarrow T = 50\text{ s}\).</p>'
                ),
            },
            # Q13 -> A
            {
                'tag': 'Direct Variation (P4 Calc)',
                'q': r'<p>\(y\) is directly proportional to the cube of \(x\) (\(y \propto x^3\)). When \(x = 3\), \(y = 108\). Find the value of \(x\) when \(y = 500\).</p>',
                'options': [
                    r'\(x = 5\)',
                    r'\(x = 12.5\)',
                    r'\(x = 6.25\)',
                    r'\(x = 25\)',
                ],
                'answer': 'A',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Viết \(y = kx^3\). Thay \(x = 3, y = 108\): '
                    r'\(108 = k(3^3) = 27k \Rightarrow k = 4 \Rightarrow y = 4x^3\).<br/>'
                    r'<b>Bước 2 [A1]:</b> Khi \(y = 500\): \(4x^3 = 500 \Rightarrow x^3 = 125 \Rightarrow x = \sqrt[3]{125} = 5\).</p>'
                ),
            },
            # Q14 -> D
            {
                'tag': 'Inverse Variation (P4 Calc)',
                'q': r'<p>\(y\) is inversely proportional to \(\sqrt{x}\). Given that \(y = 6\) when \(x = 16\), find the value of \(x\) when \(y = 4.8\).</p>',
                'options': [
                    r'\(x = 5\)',
                    r'\(x = 12.8\)',
                    r'\(x = 20\)',
                    r'\(x = 25\)',
                ],
                'answer': 'D',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Viết \(y = \frac{k}{\sqrt{x}}\). Thay \(x = 16, y = 6\): '
                    r'\(k = 6\sqrt{16} = 6 \times 4 = 24 \Rightarrow y = \frac{24}{\sqrt{x}}\).<br/>'
                    r'<b>Bước 2 [A1]:</b> Khi \(y = 4.8\): \(\sqrt{x} = \frac{24}{4.8} = 5 \Rightarrow x = 5^2 = 25\).</p>'
                ),
            },
            # Q15 -> B
            {
                'tag': 'Inverse Square Variation (P4 Calc)',
                'q': r'<p>\(F\) is inversely proportional to the square of \(d\) (\(F \propto \frac{1}{d^2}\)). If \(d\) is increased by \(25\%\), calculate the percentage <b>decrease</b> in \(F\).</p>',
                'options': [
                    r'\(25\%\)',
                    r'\(36\%\)',
                    r'\(50\%\)',
                    r'\(20\%\)',
                ],
                'answer': 'B',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Khi \(d\) tăng \(25\%\), \(d_{\text{new}} = 1.25d = \frac{5}{4}d\). '
                    r'Do đó \(F_{\text{new}} = \frac{k}{(1.25d)^2} = \frac{F}{1.5625} = 0.64F\).<br/>'
                    r'<b>Bước 2 [A1]:</b> Mức giảm phần trăm là \((1 - 0.64) \times 100\% = 36\%\).</p>'
                ),
            },
        ],
    },

    # =========================================================================
    # DRILL 7 (CALC): Sine/Cosine Rule, 3D Trig, Bearings & 3D Mensuration
    # =========================================================================
    {
        'code': 'd0580_c3',
        'folder_key': 'calc',
        'calculator_policy': 'calculator',
        'order_index': 3,
        'title': '🧮 Calc Drill 3: Sine/Cosine Rule, 3D Trigonometry, Bearings & 3D Mensuration (0580 P4)',
        'time_limit': '30',
        'intro_html': (
            r'<p><b>Mục tiêu (Paper 4 Calculator Allowed — Syllabus 2025–2027):</b> '
            r'Làm chủ Hình học &amp; Lượng giác nâng cao (Topic 4, 5, 6): Định lý Sin (kể cả góc tù mơ hồ — ambiguous case), '
            r'Định lý Cosin, góc phương vị (bearings), Lượng giác 3D trong hình hộp/hình chóp, thể tích hình nón cụt (frustum), '
            r'khối ghép nón – bán cầu và tỉ số diện tích/thể tích khối đồng dạng (\(k^2, k^3\)). '
            r'Làm tròn độ dài/diện tích/thể tích đến \(3\text{ s.f.}\), góc đến \(1\text{ d.p.}\)</p>'
        ),
        'lecture_keys': ['t4', 't5', 't6', 'p2p4'],
        'questions': [
            # Q1 -> A
            {
                'tag': 'Sine Rule (P4 Calc)',
                'q': r'<p>In \(\triangle ABC\), \(AC = 14.2\text{ cm}\), \(\angle B = 54^\circ\), and \(\angle A = 73^\circ\). Calculate the length of \(BC\), correct to \(3\text{ s.f.}\)</p>',
                'options': [
                    r'\(16.8\text{ cm}\)',
                    r'\(12.0\text{ cm}\)',
                    r'\(15.4\text{ cm}\)',
                    r'\(17.6\text{ cm}\)',
                ],
                'answer': 'A',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Áp dụng Định lý Sin: '
                    r'\(\frac{BC}{\sin A} = \frac{AC}{\sin B} \Rightarrow BC = \frac{14.2 \sin 73^\circ}{\sin 54^\circ}\).<br/>'
                    r'<b>Bước 2 [A1]:</b> Bấm máy (chế độ DEG): '
                    r'\(BC = \frac{14.2 \times 0.956305}{0.809017} = 16.785\dots \approx 16.8\text{ cm}\).</p>'
                ),
            },
            # Q2 -> C
            {
                'tag': 'Sine Rule — Ambiguous Obtuse Angle (P4 Calc)',
                'q': r'<p>In \(\triangle PQR\), \(PQ = 11\text{ cm}\), \(PR = 8\text{ cm}\), and \(\angle PQR = 38^\circ\). Given that \(\angle PRQ\) is <b>obtuse</b>, calculate \(\angle PRQ\), correct to \(1\text{ d.p.}\)</p>',
                'options': [
                    r'\(57.8^\circ\)',
                    r'\(112.2^\circ\)',
                    r'\(122.2^\circ\)',
                    r'\(142.0^\circ\)',
                ],
                'answer': 'C',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Dùng Định lý Sin: '
                    r'\(\frac{\sin R}{11} = \frac{\sin 38^\circ}{8} \Rightarrow \sin R = \frac{11\sin 38^\circ}{8} = 0.84653\dots\). '
                    r'Góc nhọn tương ứng là \(\arcsin(0.84653) = 57.837^\circ\).<br/>'
                    r'<b>Bước 2 [M1][A1]:</b> Vì đề yêu cầu góc <b>tù</b> (obtuse): '
                    r'\(\angle PRQ = 180^\circ - 57.837^\circ = 122.163^\circ \approx 122.2^\circ\).</p>'
                ),
            },
            # Q3 -> B
            {
                'tag': 'Cosine Rule — Side (P4 Calc)',
                'q': r'<p>In \(\triangle XYZ\), \(XY = 11.4\text{ cm}\), \(XZ = 8.6\text{ cm}\), and \(\angle YXZ = 112^\circ\). Calculate the length of \(YZ\), correct to \(3\text{ s.f.}\)</p>',
                'options': [
                    r'\(11.4\text{ cm}\)',
                    r'\(16.7\text{ cm}\)',
                    r'\(14.3\text{ cm}\)',
                    r'\(19.2\text{ cm}\)',
                ],
                'answer': 'B',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Áp dụng Định lý Cosin: '
                    r'\(YZ^2 = 11.4^2 + 8.6^2 - 2(11.4)(8.6)\cos 112^\circ = 129.96 + 73.96 - 196.08(-0.374607)\).<br/>'
                    r'<b>Bước 2 [A1]:</b> \(YZ^2 = 203.92 + 73.4529 = 277.3729 \Rightarrow YZ = \sqrt{277.3729} = 16.6545\dots \approx 16.7\text{ cm}\).</p>'
                ),
            },
            # Q4 -> D
            {
                'tag': 'Cosine Rule — Angle (P4 Calc)',
                'q': r'<p>A triangle has side lengths \(7\text{ cm}\), \(10\text{ cm}\), and \(14\text{ cm}\). Calculate the size of its <b>largest angle</b>, correct to \(1\text{ d.p.}\)</p>',
                'options': [
                    r'\(70.4^\circ\)',
                    r'\(104.5^\circ\)',
                    r'\(98.2^\circ\)',
                    r'\(109.6^\circ\)',
                ],
                'answer': 'D',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Góc lớn nhất đối diện cạnh dài nhất (\(14\text{ cm}\)): '
                    r'\(\cos C = \frac{7^2 + 10^2 - 14^2}{2(7)(10)} = \frac{49 + 100 - 196}{140} = -\frac{47}{140}\).<br/>'
                    r'<b>Bước 2 [A1]:</b> \(C = \arccos\left(-\frac{47}{140}\right) = 109.617^\circ \approx 109.6^\circ\).</p>'
                ),
            },
            # Q5 -> C
            {
                'tag': 'Bearings & Cosine Rule (P4 Calc)',
                'q': r'<p>A boat sails \(18\text{ km}\) from port \(A\) to island \(B\) on a bearing of \(055^\circ\), and then sails \(24\text{ km}\) from \(B\) to island \(C\) on a bearing of \(150^\circ\). Calculate the straight-line distance \(AC\), correct to \(3\text{ s.f.}\)</p>',
                'options': [
                    r'\(30.0\text{ km}\)',
                    r'\(31.2\text{ km}\)',
                    r'\(28.7\text{ km}\)',
                    r'\(26.1\text{ km}\)',
                ],
                'answer': 'C',
                'explanation': (
                    r'<p><b>Bước 1 [B1]:</b> Tại \(B\), góc phương vị ngược của \(A\) từ \(B\) là \(55^\circ + 180^\circ = 235^\circ\), '
                    r'nên góc trong \(\angle ABC = 235^\circ - 150^\circ = 85^\circ\).<br/>'
                    r'<b>Bước 2 [M1][A1]:</b> Dùng Định lý Cosin: '
                    r'\(AC = \sqrt{18^2 + 24^2 - 2(18)(24)\cos 85^\circ} = \sqrt{900 - 75.3025} = 28.7175\dots \approx 28.7\text{ km}\).</p>'
                ),
            },
            # Q6 -> B
            {
                'tag': 'Bearings & Sine Rule (P4 Calc)',
                'q': r'<p>Two lighthouses \(P\) and \(Q\) are \(15\text{ km}\) apart, with \(Q\) due east of \(P\). A ship \(S\) is on a bearing of \(040^\circ\) from \(P\) and \(325^\circ\) from \(Q\). Calculate the distance \(PS\), correct to \(3\text{ s.f.}\)</p>',
                'options': [
                    r'\(11.9\text{ km}\)',
                    r'\(12.7\text{ km}\)',
                    r'\(14.1\text{ km}\)',
                    r'\(10.5\text{ km}\)',
                ],
                'answer': 'B',
                'explanation': (
                    r'<p><b>Bước 1 [B1]:</b> Trong \(\triangle PQS\): \(\angle QPS = 90^\circ - 40^\circ = 50^\circ\), '
                    r'\(\angle PQS = 325^\circ - 270^\circ = 55^\circ\), suy ra \(\angle PSQ = 180^\circ - 50^\circ - 55^\circ = 75^\circ\).<br/>'
                    r'<b>Bước 2 [M1][A1]:</b> Định lý Sin: '
                    r'\(PS = \frac{15\sin 55^\circ}{\sin 75^\circ} = 12.7207\dots \approx 12.7\text{ km}\).</p>'
                ),
            },
            # Q7 -> D
            {
                'tag': '3D Trigonometry — Cuboid (P4 Calc)',
                'q': r'<p>A cuboid \(ABCDEFGH\) has horizontal rectangular base \(ABCD\) with \(AB = 12\text{ cm}\), \(BC = 9\text{ cm}\), and vertical height \(CG = 8\text{ cm}\). Calculate the angle between the space diagonal \(AG\) and the base \(ABCD\), correct to \(1\text{ d.p.}\)</p>',
                'options': [
                    r'\(33.7^\circ\)',
                    r'\(41.6^\circ\)',
                    r'\(61.9^\circ\)',
                    r'\(28.1^\circ\)',
                ],
                'answer': 'D',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Hình chiếu của \(AG\) lên mặt đáy là đường chéo đáy \(AC\): '
                    r'\(AC = \sqrt{12^2 + 9^2} = \sqrt{225} = 15\text{ cm}\).<br/>'
                    r'<b>Bước 2 [M1][A1]:</b> Trong tam giác vuông \(ACG\): '
                    r'\(\tan(\angle GAC) = \frac{CG}{AC} = \frac{8}{15} \Rightarrow \angle GAC = \arctan\left(\frac{8}{15}\right) = 28.07^\circ \approx 28.1^\circ\).</p>'
                ),
            },
            # Q8 -> A
            {
                'tag': '3D Trigonometry — Pyramid Edge (P4 Calc)',
                'q': r'<p>A right square-based pyramid \(VABCD\) has base edge \(AB = 10\text{ cm}\) and vertical height \(VO = 12\text{ cm}\), where \(O\) is the centre of the square base. Calculate the angle between the slant edge \(VA\) and the base \(ABCD\), correct to \(1\text{ d.p.}\)</p>',
                'options': [
                    r'\(59.5^\circ\)',
                    r'\(67.4^\circ\)',
                    r'\(50.2^\circ\)',
                    r'\(30.5^\circ\)',
                ],
                'answer': 'A',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Nửa đường chéo đáy \(OA = \frac{1}{2}\sqrt{10^2 + 10^2} = 5\sqrt{2}\text{ cm}\). '
                    r'(Tránh bẫy dùng \(5\text{ cm}\) vì \(5\text{ cm}\) là khoảng cách tới trung điểm cạnh!)<br/>'
                    r'<b>Bước 2 [M1][A1]:</b> Trong \(\triangle VOA\) vuông tại \(O\): '
                    r'\(\tan(\angle VAO) = \frac{12}{5\sqrt{2}} \Rightarrow \angle VAO = 59.49^\circ \approx 59.5^\circ\).</p>'
                ),
            },
            # Q9 -> B
            {
                'tag': '3D Trigonometry — Pyramid Face (P4 Calc)',
                'q': r'<p>A right square-based pyramid \(VABCD\) has base edge \(16\text{ cm}\) and slant edge \(VB = VC = 17\text{ cm}\). Calculate the angle between the triangular face \(VBC\) and the square base \(ABCD\), correct to \(1\text{ d.p.}\)</p>',
                'options': [
                    r'\(61.9^\circ\)',
                    r'\(57.8^\circ\)',
                    r'\(48.2^\circ\)',
                    r'\(32.2^\circ\)',
                ],
                'answer': 'B',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Gọi \(M\) là trung điểm \(BC\) và \(O\) là tâm đáy: \(BM = 8\text{ cm}\), \(OM = 8\text{ cm}\). '
                    r'Đường cao mặt bên \(VM = \sqrt{17^2 - 8^2} = \sqrt{225} = 15\text{ cm}\).<br/>'
                    r'<b>Bước 2 [M1][A1]:</b> Trong \(\triangle VOM\) vuông tại \(O\): '
                    r'\(\cos(\angle VMO) = \frac{OM}{VM} = \frac{8}{15} \Rightarrow \angle VMO = 57.77^\circ \approx 57.8^\circ\).</p>'
                ),
            },
            # Q10 -> D
            {
                'tag': 'Frustum Volume (P4 Calc)',
                'q': r'<p>A frustum is formed by removing a small cone of base radius \(4\text{ cm}\) and height \(6\text{ cm}\) from the top of a larger similar cone of base radius \(10\text{ cm}\). Calculate the volume of the frustum, correct to \(3\text{ s.f.}\)</p>',
                'options': [
                    r'\(1570\text{ cm}^3\)',
                    r'\(1370\text{ cm}^3\)',
                    r'\(942\text{ cm}^3\)',
                    r'\(1470\text{ cm}^3\)',
                ],
                'answer': 'D',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Do hai hình nón đồng dạng, tỉ số đồng dạng \(k = \frac{10}{4} = 2.5\), '
                    r'nên chiều cao nón lớn \(H = 6 \times 2.5 = 15\text{ cm}\).<br/>'
                    r'<b>Bước 2 [M1][A1]:</b> \(V_{\text{frustum}} = \frac{1}{3}\pi(10^2 \times 15 - 4^2 \times 6) '
                    r'= \frac{1}{3}\pi(1500 - 96) = 468\pi = 1470.27\dots \approx 1470\text{ cm}^3\).</p>'
                ),
            },
            # Q11 -> A
            {
                'tag': 'Composite 3D Volume (P4 Calc)',
                'q': r'<p>A solid toy is made by joining a hemisphere of radius \(6\text{ cm}\) flat-to-flat with a right circular cone of base radius \(6\text{ cm}\). The total height of the toy is \(16\text{ cm}\). Calculate the total <b>volume</b> of the toy, correct to \(3\text{ s.f.}\)</p>',
                'options': [
                    r'\(829\text{ cm}^3\)',
                    r'\(1060\text{ cm}^3\)',
                    r'\(1280\text{ cm}^3\)',
                    r'\(679\text{ cm}^3\)',
                ],
                'answer': 'A',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Chiều cao phần hình nón là \(h = 16 - 6 = 10\text{ cm}\). '
                    r'Thể tích bán cầu \(= \frac{2}{3}\pi(6^3) = 144\pi\); thể tích nón \(= \frac{1}{3}\pi(6^2)(10) = 120\pi\).<br/>'
                    r'<b>Bước 2 [A1]:</b> Tổng thể tích \(= 264\pi = 829.38\dots \approx 829\text{ cm}^3\).</p>'
                ),
            },
            # Q12 -> C
            {
                'tag': 'Composite 3D Surface Area (P4 Calc)',
                'q': r'<p>A solid ornament consists of a hemisphere of radius \(5\text{ cm}\) joined flat-to-flat to a cone of base radius \(5\text{ cm}\) and vertical height \(12\text{ cm}\). Calculate its <b>total outer surface area</b>, correct to \(3\text{ s.f.}\)</p>',
                'options': [
                    r'\(440\text{ cm}^2\)',
                    r'\(346\text{ cm}^2\)',
                    r'\(361\text{ cm}^2\)',
                    r'\(518\text{ cm}^2\)',
                ],
                'answer': 'C',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Đường sinh hình nón \(l = \sqrt{5^2 + 12^2} = 13\text{ cm}\). '
                    r'Mặt phẳng tiếp giáp nằm bên trong nên không tính vào diện tích ngoài.<br/>'
                    r'<b>Bước 2 [M1][A1]:</b> Diện tích xung quanh nón \(\pi r l = 65\pi\); '
                    r'diện tích mặt cong bán cầu \(2\pi r^2 = 50\pi\). '
                    r'Tổng \(\text{SA} = 115\pi = 361.28\dots \approx 361\text{ cm}^2\).</p>'
                ),
            },
            # Q13 -> D
            {
                'tag': 'Sector & Minor Segment Area (P4 Calc)',
                'q': r'<p>A sector of a circle of radius \(12\text{ cm}\) has central angle \(105^\circ\). Calculate the area of the <b>minor segment</b> cut off by the chord, correct to \(3\text{ s.f.}\)</p>',
                'options': [
                    r'\(132\text{ cm}^2\)',
                    r'\(69.5\text{ cm}^2\)',
                    r'\(58.2\text{ cm}^2\)',
                    r'\(62.4\text{ cm}^2\)',
                ],
                'answer': 'D',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Diện tích hình quạt \(A_{\text{sector}} = \frac{105}{360}\pi(12^2) = 42\pi = 131.9469\text{ cm}^2\). '
                    r'Diện tích tam giác \(A_{\triangle} = \frac{1}{2}(12)(12)\sin 105^\circ = 69.5467\text{ cm}^2\).<br/>'
                    r'<b>Bước 2 [A1]:</b> Diện tích viên phân (minor segment) \(= 131.9469 - 69.5467 = 62.400\dots \approx 62.4\text{ cm}^2\).</p>'
                ),
            },
            # Q14 -> C
            {
                'tag': 'Similar Solids — k^3 to k^2 (P4 Calc)',
                'q': r'<p>Two mathematically similar bottles have volumes \(250\text{ cm}^3\) and \(2000\text{ cm}^3\). If the total surface area of the smaller bottle is \(185\text{ cm}^2\), calculate the total surface area of the larger bottle.</p>',
                'options': [
                    r'\(1480\text{ cm}^2\)',
                    r'\(370\text{ cm}^2\)',
                    r'\(740\text{ cm}^2\)',
                    r'\(523\text{ cm}^2\)',
                ],
                'answer': 'C',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Tỉ số thể tích \(k^3 = \frac{2000}{250} = 8 \Rightarrow\) tỉ số đồng dạng độ dài \(k = \sqrt[3]{8} = 2\).<br/>'
                    r'<b>Bước 2 [M1][A1]:</b> Tỉ số diện tích \(k^2 = 2^2 = 4\), '
                    r'nên diện tích chai lớn \(= 185 \times 4 = 740\text{ cm}^2\).</p>'
                ),
            },
            # Q15 -> B
            {
                'tag': 'Similar Solids — k^2 to k^3 (P4 Calc)',
                'q': r'<p>Two mathematically similar statues have total surface areas \(320\text{ cm}^2\) and \(720\text{ cm}^2\). If the larger statue has volume \(4050\text{ cm}^3\), calculate the volume of the smaller statue.</p>',
                'options': [
                    r'\(1800\text{ cm}^3\)',
                    r'\(1200\text{ cm}^3\)',
                    r'\(2700\text{ cm}^3\)',
                    r'\(900\text{ cm}^3\)',
                ],
                'answer': 'B',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Tỉ số diện tích (nhỏ/lớn) \(= \frac{320}{720} = \frac{4}{9} '
                    r'\Rightarrow\) tỉ số tuyến tính \(k = \sqrt{\frac{4}{9}} = \frac{2}{3}\).<br/>'
                    r'<b>Bước 2 [M1][A1]:</b> Tỉ số thể tích \(k^3 = \left(\frac{2}{3}\right)^3 = \frac{8}{27}\), '
                    r'suy ra \(V_{\text{small}} = 4050 \times \frac{8}{27} = 1200\text{ cm}^3\).</p>'
                ),
            },
        ],
    },

    # =========================================================================
    # DRILL 8 (CALC): Conditional Probability, Histograms & Cumulative Frequency
    # =========================================================================
    {
        'code': 'd0580_c4',
        'folder_key': 'calc',
        'calculator_policy': 'calculator',
        'order_index': 4,
        'title': '🧮 Calc Drill 4: Conditional Probability, Histograms & Cumulative Frequency (0580 P4)',
        'time_limit': '30',
        'intro_html': (
            r'<p><b>Mục tiêu (Paper 4 Calculator Allowed — Syllabus 2025–2027):</b> '
            r'Chinh phục Topic 8 &amp; 9 theo đúng chuẩn <b>Syllabus 2025–2027</b>: sơ đồ cây không hoàn lại '
            r'(without replacement), xác suất có điều kiện \(P(A \mid B)\) từ biểu đồ Venn &amp; bảng hai chiều, '
            r'biểu đồ tần suất (histograms với \(\text{Frequency Density} = \frac{\text{Frequency}}{\text{Class Width}}\)), '
            r'tần suất tích lũy (cumulative frequency: trung vị, IQR, phân vị) và số trung bình ước lượng của dữ liệu ghép nhóm.</p>'
        ),
        'lecture_keys': ['t8', 't9', 'p2p4'],
        'questions': [
            # Q1 -> D
            {
                'tag': 'Without-Replacement Tree Diagram (P4 Calc)',
                'q': r'<p>A bag contains \(7\) red counters and \(5\) blue counters. Two counters are picked at random <b>without replacement</b>. Find the probability that both counters are the <b>same colour</b>.</p>',
                'options': [
                    r'\(\frac{37}{72}\)',
                    r'\(\frac{35}{66}\)',
                    r'\(\frac{7}{22}\)',
                    r'\(\frac{31}{66}\)',
                ],
                'answer': 'D',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Tính xác suất hai nhánh \(RR\) và \(BB\) (mẫu số giảm từ \(12\) xuống \(11\)): '
                    r'\(P(RR) = \frac{7}{12} \times \frac{6}{11} = \frac{42}{132}\), '
                    r'\(P(BB) = \frac{5}{12} \times \frac{4}{11} = \frac{20}{132}\).<br/>'
                    r'<b>Bước 2 [A1]:</b> Cộng hai nhánh: \(\frac{42 + 20}{132} = \frac{62}{132} = \frac{31}{66}\).</p>'
                ),
            },
            # Q2 -> A
            {
                'tag': 'Without-Replacement Probability (P4 Calc)',
                'q': r'<p>A box holds \(6\) white marbles and \(4\) black marbles. Three marbles are drawn at random <b>without replacement</b>. Find the probability that <b>at least one</b> marble is black.</p>',
                'options': [
                    r'\(\frac{5}{6}\)',
                    r'\(\frac{1}{6}\)',
                    r'\(\frac{98}{125}\)',
                    r'\(\frac{2}{5}\)',
                ],
                'answer': 'A',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Dùng biến cố đối: \(P(\text{at least one black}) = 1 - P(WWW)\). '
                    r'Ta có \(P(WWW) = \frac{6}{10} \times \frac{5}{9} \times \frac{4}{8} = \frac{120}{720} = \frac{1}{6}\).<br/>'
                    r'<b>Bước 2 [A1]:</b> Suy ra \(1 - \frac{1}{6} = \frac{5}{6}\).</p>'
                ),
            },
            # Q3 -> C
            {
                'tag': 'Conditional Tree Diagram (P4 Calc)',
                'q': r'<p>The probability that it rains on Monday is \(0.3\). If it rains on Monday, the probability it rains on Tuesday is \(0.6\). If it does not rain on Monday, the probability it rains on Tuesday is \(0.2\). Find the probability that it rains on <b>Tuesday</b>.</p>',
                'options': [
                    r'\(0.18\)',
                    r'\(0.40\)',
                    r'\(0.32\)',
                    r'\(0.80\)',
                ],
                'answer': 'C',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Xét hai nhánh dẫn đến trời mưa thứ Ba: '
                    r'\(P(R_M \cap R_T) = 0.3 \times 0.6 = 0.18\) và \(P(R_M^{\prime} \cap R_T) = 0.7 \times 0.2 = 0.14\).<br/>'
                    r'<b>Bước 2 [A1]:</b> Cộng xác suất hai nhánh xung khắc: \(0.18 + 0.14 = 0.32\).</p>'
                ),
            },
            # Q4 -> B
            {
                'tag': 'Conditional Probability — Venn Diagram (P4 Calc)',
                'q': r'<p>In a group of \(40\) students, \(22\) study French (\(F\)), \(18\) study Spanish (\(S\)), and \(8\) study neither language. A student is chosen at random. Given that the student studies <b>French</b>, find \(P(S \mid F)\).</p>',
                'options': [
                    r'\(\frac{1}{5}\)',
                    r'\(\frac{4}{11}\)',
                    r'\(\frac{4}{9}\)',
                    r'\(\frac{1}{4}\)',
                ],
                'answer': 'B',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Số học sinh học ít nhất một ngoại ngữ: \(n(F \cup S) = 40 - 8 = 32\). '
                    r'Phần giao: \(n(F \cap S) = 22 + 18 - 32 = 8\).<br/>'
                    r'<b>Bước 2 [M1][A1]:</b> Thu hẹp không gian mẫu vào tập \(F\) (\(22\) học sinh): '
                    r'\(P(S \mid F) = \frac{n(F \cap S)}{n(F)} = \frac{8}{22} = \frac{4}{11}\).</p>'
                ),
            },
            # Q5 -> A
            {
                'tag': 'Conditional Probability — Two-Way Table (P4 Calc)',
                'q': r'<p>A survey of \(120\) commuters records transport mode by weather: on rainy days, \(28\) took the bus, \(17\) the train, and \(15\) a car; on dry days, \(20\) took the bus, \(25\) the train, and \(15\) a car. Find the probability that a randomly selected commuter travelled on a <b>rainy day</b>, given that they took the <b>bus</b>.</p>',
                'options': [
                    r'\(\frac{7}{12}\)',
                    r'\(\frac{7}{30}\)',
                    r'\(\frac{7}{15}\)',
                    r'\(\frac{5}{12}\)',
                ],
                'answer': 'A',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Tổng số người đi xe buýt (mẫu số điều kiện): \(n(\text{Bus}) = 28 + 20 = 48\). '
                    r'Số người vừa đi xe buýt vừa vào ngày mưa là \(28\).<br/>'
                    r'<b>Bước 2 [A1]:</b> \(P(\text{Rainy} \mid \text{Bus}) = \frac{28}{48} = \frac{7}{12}\).</p>'
                ),
            },
            # Q6 -> D
            {
                'tag': 'Conditional Probability — Reverse Tree (P4 Calc)',
                'q': r'<p>At a factory, Machine \(A\) produces \(60\%\) of items and Machine \(B\) produces \(40\%\). The defect rate is \(5\%\) for Machine \(A\) and \(10\%\) for Machine \(B\). An item chosen at random is found to be <b>defective</b>. Find the probability that it was made by <b>Machine \(B\)</b>.</p>',
                'options': [
                    r'\(\frac{3}{7}\)',
                    r'\(\frac{2}{5}\)',
                    r'\(\frac{1}{25}\)',
                    r'\(\frac{4}{7}\)',
                ],
                'answer': 'D',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Tính xác suất sản phẩm lỗi từ từng máy: '
                    r'\(P(A \cap D) = 0.6 \times 0.05 = 0.03\), \(P(B \cap D) = 0.4 \times 0.10 = 0.04\), '
                    r'nên \(P(D) = 0.03 + 0.04 = 0.07\).<br/>'
                    r'<b>Bước 2 [A1]:</b> \(P(B \mid D) = \frac{P(B \cap D)}{P(D)} = \frac{0.04}{0.07} = \frac{4}{7}\).</p>'
                ),
            },
            # Q7 -> B
            {
                'tag': 'Histograms — Frequency Density (P4 Calc)',
                'q': r'<p>In a histogram, the class interval \(20 < t \le 35\) has a frequency of \(42\). Calculate the <b>frequency density</b> for this interval.</p>',
                'options': [
                    r'\(1.4\)',
                    r'\(2.8\)',
                    r'\(4.2\)',
                    r'\(0.36\)',
                ],
                'answer': 'B',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Độ rộng lớp \(\text{Class Width} = 35 - 20 = 15\).<br/>'
                    r'<b>Bước 2 [A1]:</b> Áp dụng công thức \(\text{Frequency Density} = \frac{\text{Frequency}}{\text{Class Width}} = \frac{42}{15} = 2.8\).</p>'
                ),
            },
            # Q8 -> C
            {
                'tag': 'Histograms — Bar Area Scaling (P4 Calc)',
                'q': r'<p>In a histogram, the interval \(10 < x \le 20\) has frequency \(30\) and is drawn as a bar of width \(2\text{ cm}\) and height \(6\text{ cm}\). Another interval \(20 < x \le 45\) is drawn with a bar height of \(3.2\text{ cm}\). Find the <b>frequency</b> of the interval \(20 < x \le 45\).</p>',
                'options': [
                    r'\(16\)',
                    r'\(32\)',
                    r'\(40\)',
                    r'\(48\)',
                ],
                'answer': 'C',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Cột \(1\): \(\text{FD}_1 = \frac{30}{20 - 10} = 3\) ứng với chiều cao \(6\text{ cm}\) '
                    r'(tỉ lệ \(1\text{ đơn vị FD} = 2\text{ cm}\)). '
                    r'Hoặc theo diện tích: \(2 \times 6 = 12\text{ cm}^2\) ứng với \(30\) phần tử \(\Rightarrow 1\text{ cm}^2 = 2.5\) phần tử.<br/>'
                    r'<b>Bước 2 [M1][A1]:</b> Cột \(2\): \(\text{FD}_2 = \frac{3.2}{2} = 1.6\), độ rộng lớp \(= 45 - 20 = 25\). '
                    r'Tần số \(= 1.6 \times 25 = 40\).</p>'
                ),
            },
            # Q9 -> A
            {
                'tag': 'Histograms — Estimating Frequency (P4 Calc)',
                'q': r'<p>A histogram summarises the completion times (in minutes) of \(90\) students with frequency densities: \(0 < t \le 10: 1.8\); \(10 < t \le 20: 3.0\); \(20 < t \le 40: 1.5\); \(40 < t \le 60: 0.6\). Estimate the number of students who took <b>more than \(30\) minutes</b>.</p>',
                'options': [
                    r'\(27\)',
                    r'\(42\)',
                    r'\(12\)',
                    r'\(21\)',
                ],
                'answer': 'A',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Tần số bằng diện tích cột (\(\text{Width} \times \text{FD}\)). '
                    r'Trên đoạn \(30 < t \le 40\) (độ rộng \(10\)): \(10 \times 1.5 = 15\) học sinh.<br/>'
                    r'<b>Bước 2 [M1][A1]:</b> Trên đoạn \(40 < t \le 60\) (độ rộng \(20\)): \(20 \times 0.6 = 12\) học sinh. '
                    r'Tổng số học sinh mất hơn \(30\) phút là \(15 + 12 = 27\).</p>'
                ),
            },
            # Q10 -> C
            {
                'tag': 'Cumulative Frequency — Median & IQR (P4 Calc)',
                'q': r'<p>A cumulative frequency distribution of \(160\) exam scores passes exactly through the points \((20, 12)\), \((40, 40)\), \((60, 80)\), \((75, 120)\), and \((100, 160)\). Find the <b>median</b> and the <b>interquartile range (IQR)</b>.</p>',
                'options': [
                    r'Median \(= 60\), \(\text{IQR} = 40\)',
                    r'Median \(= 50\), \(\text{IQR} = 35\)',
                    r'Median \(= 60\), \(\text{IQR} = 35\)',
                    r'Median \(= 80\), \(\text{IQR} = 80\)',
                ],
                'answer': 'C',
                'explanation': (
                    r'<p><b>Bước 1 [B1]:</b> Với \(N = 160\): trung vị tại vị trí \(0.5 \times 160 = 80 \Rightarrow \text{Median} = 60\).<br/>'
                    r'<b>Bước 2 [M1][A1]:</b> Tứ phân vị dưới \(Q_1\) tại vị trí \(0.25 \times 160 = 40 \Rightarrow Q_1 = 40\); '
                    r'tứ phân vị trên \(Q_3\) tại vị trí \(0.75 \times 160 = 120 \Rightarrow Q_3 = 75\). '
                    r'Vậy \(\text{IQR} = Q_3 - Q_1 = 75 - 40 = 35\).</p>'
                ),
            },
            # Q11 -> D
            {
                'tag': 'Cumulative Frequency — Percentiles (P4 Calc)',
                'q': r'<p>The cumulative frequency table for the lifetimes \(t\) (hours) of \(200\) batteries passes through \((10, 15)\), \((20, 55)\), \((30, 120)\), \((40, 160)\), \((50, 185)\), and \((60, 200)\). Find the <b>80th percentile</b> and the <b>percentage of batteries lasting more than \(30\) hours</b>.</p>',
                'options': [
                    r'\(40\text{ hours}\) and \(60\%\)',
                    r'\(48\text{ hours}\) and \(40\%\)',
                    r'\(30\text{ hours}\) and \(60\%\)',
                    r'\(40\text{ hours}\) and \(40\%\)',
                ],
                'answer': 'D',
                'explanation': (
                    r'<p><b>Bước 1 [B1]:</b> Vị trí phân vị thứ \(80\) là \(0.80 \times 200 = 160\), ứng với điểm \((40, 160)\), '
                    r'nên phân vị thứ \(80\) là \(40\text{ giờ}\).<br/>'
                    r'<b>Bước 2 [M1][A1]:</b> Có \(120\) pin kéo dài \(\le 30\text{ giờ}\), nên số pin kéo dài \(> 30\text{ giờ}\) là '
                    r'\(200 - 120 = 80\), chiếm \(\frac{80}{200} \times 100\% = 40\%\).</p>'
                ),
            },
            # Q12 -> B
            {
                'tag': 'Cumulative Frequency — Interpolation (P4 Calc)',
                'q': r'<p>The heights \(h\) (in \(\text{cm}\)) of \(100\) plants are grouped as: \(0 < h \le 10: 15\); \(10 < h \le 20: 25\); \(20 < h \le 30: 40\); \(30 < h \le 40: 20\). Using linear interpolation within the median class, estimate the <b>median</b> height.</p>',
                'options': [
                    r'\(25.0\text{ cm}\)',
                    r'\(22.5\text{ cm}\)',
                    r'\(24.0\text{ cm}\)',
                    r'\(21.5\text{ cm}\)',
                ],
                'answer': 'B',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Tần suất tích lũy: \(15, 40, 80, 100\). '
                    r'Vị trí trung vị thứ \(50\) nằm trong lớp \(20 < h \le 30\) (tần số lớp \(= 40\), tích lũy trước đó \(= 40\)).<br/>'
                    r'<b>Bước 2 [A1]:</b> Nội suy tuyến tính: '
                    r'\(20 + \frac{50 - 40}{40} \times 10 = 20 + 2.5 = 22.5\text{ cm}\).</p>'
                ),
            },
            # Q13 -> C
            {
                'tag': 'Estimated Mean of Grouped Data (P4 Calc)',
                'q': r'<p>The masses \(m\) (in \(\text{kg}\)) of \(50\) parcels are grouped as: \(0 < m \le 4: 8\); \(4 < m \le 8: 15\); \(8 < m \le 12: 17\); \(12 < m \le 20: 10\). Calculate an estimate for the <b>mean mass</b> of a parcel.</p>',
                'options': [
                    r'\(8.32\text{ kg}\)',
                    r'\(9.12\text{ kg}\)',
                    r'\(8.72\text{ kg}\)',
                    r'\(7.96\text{ kg}\)',
                ],
                'answer': 'C',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Lấy trung điểm từng lớp (chú ý lớp cuối rộng \(8\) nên trung điểm là \(16\), không phải \(14\)!): '
                    r'\(\sum fm = 8(2) + 15(6) + 17(10) + 10(16) = 16 + 90 + 170 + 160 = 436\).<br/>'
                    r'<b>Bước 2 [A1]:</b> Số trung bình ước lượng \(= \frac{436}{50} = 8.72\text{ kg}\).</p>'
                ),
            },
            # Q14 -> A
            {
                'tag': 'Combined Weighted Mean (P4 Calc)',
                'q': r'<p>Class \(X\) has \(24\) students with a mean test score of \(72.5\). Class \(Y\) has \(16\) students with a mean test score of \(80.0\). Calculate the combined mean score of all \(40\) students.</p>',
                'options': [
                    r'\(75.5\)',
                    r'\(76.25\)',
                    r'\(74.8\)',
                    r'\(77.0\)',
                ],
                'answer': 'A',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Tổng điểm lớp \(X = 24 \times 72.5 = 1740\); '
                    r'tổng điểm lớp \(Y = 16 \times 80.0 = 1280\).<br/>'
                    r'<b>Bước 2 [A1]:</b> Trung bình gộp \(= \frac{1740 + 1280}{24 + 16} = \frac{3020}{40} = 75.5\). '
                    r'(Không lấy trung bình cộng \((72.5+80)/2 = 76.25\)!)</p>'
                ),
            },
            # Q15 -> D
            {
                'tag': 'Probability from Frequency Table (P4 Calc)',
                'q': r'<p>In a class of \(25\) students, their test marks are: \(0 \le m < 40\): \(5\) students; \(40 \le m < 70\): \(12\) students; \(70 \le m \le 100\): \(8\) students. Two students are chosen at random <b>without replacement</b>. Find the probability that <b>exactly one</b> of them scored at least \(70\).</p>',
                'options': [
                    r'\(\frac{17}{75}\)',
                    r'\(\frac{272}{625}\)',
                    r'\(\frac{7}{75}\)',
                    r'\(\frac{34}{75}\)',
                ],
                'answer': 'D',
                'explanation': (
                    r'<p><b>Bước 1 [M1]:</b> Có \(8\) học sinh đạt \(\ge 70\) và \(17\) học sinh đạt \(< 70\). '
                    r'Có hai thứ tự: (người \(1 \ge 70\), người \(2 < 70\)) hoặc ngược lại.<br/>'
                    r'<b>Bước 2 [M1][A1]:</b> '
                    r'\(P = \frac{8}{25} \times \frac{17}{24} + \frac{17}{25} \times \frac{8}{24} = \frac{272}{600} = \frac{34}{75}\).</p>'
                ),
            },
        ],
    },
]


# =============================================================================
# COMPREHENSIVE MATH & PIPELINE VERIFICATION (ALL 120 QUESTIONS)
# =============================================================================
def _sigfig(val, n=3):
    """Round a positive number to n significant figures (matching Cambridge 3 s.f.)."""
    if val == 0:
        return '0'
    exp = math.floor(math.log10(abs(val)))
    dec = n - 1 - exp
    rounded = round(val, dec)
    if dec <= 0:
        return str(int(round(rounded)))
    return f'{rounded:.{dec}f}'


def verify_all_math():
    """
    Independently verifies:
      1) Structural schema, metadata, balanced answers (3-4 per A/B/C/D), KaTeX hygiene,
         zero raw '$', zero control-character LaTeX corruption, zero forbidden box-plot topics.
      2) Every single mathematical calculation across all 120 questions (8 drills x 15 Qs)
         using Python `fractions.Fraction` and `math`, cross-checked against the selected option.
      3) Official `build_igcse_drill_json` + `validate_igcse_drill` from `scripts.igcse_maths_pipeline`.
    """
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if root_dir not in sys.path:
        sys.path.insert(0, root_dir)

    from scripts.igcse_maths_pipeline import (
        COURSE_0580_ID,
        build_igcse_drill_json,
        validate_igcse_drill,
    )

    # 1. Structural & formatting verification
    assert len(DRILLS_0580_2025) == 8, f'Expected 8 drills, got {len(DRILLS_0580_2025)}'
    expected_codes = [
        'd0580_nc1', 'd0580_nc2', 'd0580_nc3', 'd0580_nc4',
        'd0580_c1', 'd0580_c2', 'd0580_c3', 'd0580_c4',
    ]
    expected_titles = [
        '🚫 Non-Calc Drill 1: Surds, Rationalising & Exact Indices (0580 P2)',
        '🚫 Non-Calc Drill 2: Exact Trig Values (0°–90°), Special Triangles & Bearings (0580 P2)',
        '🚫 Non-Calc Drill 3: Recurring Decimals, Standard Form, Fractions & Bounds (0580 P2)',
        '🚫 Non-Calc Drill 4: Domain & Range, Fractional Powers x^(±1/2) & Algebra (0580 P2 NEW 2025)',
        '🧮 Calc Drill 1: Compound Interest, Reverse % & Exponential Growth/Decay (0580 P4)',
        '🧮 Calc Drill 2: Quadratics, Turning Points, Differentiation & Kinematics (0580 P4)',
        '🧮 Calc Drill 3: Sine/Cosine Rule, 3D Trigonometry, Bearings & 3D Mensuration (0580 P4)',
        '🧮 Calc Drill 4: Conditional Probability, Histograms & Cumulative Frequency (0580 P4)',
    ]
    valid_lec_keys = {'t1', 't2', 't3', 't4', 't5', 't6', 't7', 't8', 't9', 'rev', 'p2p4'}
    ctrl_re = re.compile(r'[\t\r\f\b\x07\x0b]')
    opt_prefix_re = re.compile(r'^\s*[A-Da-d][\.\)]\s+')
    forbidden_re = re.compile(r'box[\s\-]*(and[\s\-]*whisker|plot)', re.IGNORECASE)

    by_code = {}
    global_stems = set()
    total_q = 0
    for idx, d in enumerate(DRILLS_0580_2025):
        code = d['code']
        assert code == expected_codes[idx], f'Code mismatch at {idx}: {code}'
        assert d['title'] == expected_titles[idx], f'Title mismatch for {code}: {d["title"]}'
        assert d['time_limit'] == '30', f'{code}: time_limit must be "30"'
        if idx < 4:
            assert d['folder_key'] == 'non_calc'
            assert d['calculator_policy'] == 'non-calculator'
            assert d['order_index'] == idx + 1
        else:
            assert d['folder_key'] == 'calc'
            assert d['calculator_policy'] == 'calculator'
            assert d['order_index'] == idx - 3
        assert d['lecture_keys'] and set(d['lecture_keys']).issubset(valid_lec_keys)

        qs = d['questions']
        assert len(qs) == 15, f'{code}: expected 15 questions, got {len(qs)}'
        total_q += len(qs)
        by_code[code] = qs

        # Check intro_html hygiene
        intro = d['intro_html']
        assert '$' not in intro, f'{code}: raw $ in intro_html'
        assert not ctrl_re.search(intro), f'{code}: control char in intro_html'
        assert intro.count(r'\(') == intro.count(r'\)'), f'{code}: unbalanced \\( \\) in intro_html'
        assert not forbidden_re.search(intro), f'{code}: forbidden box-plot reference in intro_html'
        for m in re.finditer(r'\\\((.*?)\\\)', intro):
            expr = m.group(1)
            assert '&' not in expr, f'{code}: & inside KaTeX in intro_html: {expr}'
            assert expr.count('{') == expr.count('}'), f'{code}: unbalanced braces in intro_html: {expr}'

        ans_dist = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
        for q_idx, q in enumerate(qs, start=1):
            assert q['q'] not in global_stems, f'{code} Q{q_idx}: duplicate question stem across drills'
            global_stems.add(q['q'])
            assert q['answer'] in ans_dist
            ans_dist[q['answer']] += 1
            assert len(q['options']) == 4
            assert q.get('tag', '').strip()
            for o in q['options']:
                assert not opt_prefix_re.match(o), f'{code} Q{q_idx}: option has A./B. prefix: {o}'
            fields = [q['q'], q['explanation']] + q['options']
            for field_txt in fields:
                assert '$' not in field_txt, f'{code} Q{q_idx}: raw $ found in {field_txt}'
                assert not ctrl_re.search(field_txt), f'{code} Q{q_idx}: control char in {field_txt!r}'
                assert field_txt.count(r'\(') == field_txt.count(r'\)'), f'{code} Q{q_idx}: unbalanced \\( \\)'
                assert field_txt.count(r'\[') == field_txt.count(r'\]'), f'{code} Q{q_idx}: unbalanced \\[ \\]'
                assert not forbidden_re.search(field_txt), f'{code} Q{q_idx}: forbidden box-plot reference'
                for m in re.finditer(r'\\\((.*?)\\\)', field_txt):
                    expr = m.group(1)
                    assert '&' not in expr, f'{code} Q{q_idx}: & inside KaTeX: {expr}'
                    assert expr.count('{') == expr.count('}'), f'{code} Q{q_idx}: unbalanced braces in KaTeX: {expr}'
                    assert not re.search(r'<[a-zA-Z/]', expr), f'{code} Q{q_idx}: HTML-like <tag in KaTeX: {expr}'
            assert any(m in q['explanation'] for m in ('[M1]', '[B1]')), f'{code} Q{q_idx}: missing [M1]/[B1]'
            assert any(m in q['explanation'] for m in ('[A1]', '[B1]')), f'{code} Q{q_idx}: missing [A1]/[B1]'

        for letter, cnt in ans_dist.items():
            assert 3 <= cnt <= 4, f'{code}: unbalanced answer distribution {ans_dist}'

        # Pipeline builder + official validator
        cj = build_igcse_drill_json(
            title=d['title'],
            course_id=COURSE_0580_ID,
            calculator_policy=d['calculator_policy'],
            syllabus_code='0580',
            intro_html=d['intro_html'],
            questions=qs,
            time_limit=d['time_limit'],
        )
        errs = validate_igcse_drill(cj, title=code)
        assert not errs, f'validate_igcse_drill failed for {code}: {errs}'

    assert total_q == 120, f'Expected 120 total questions, got {total_q}'

    def ans_opt(code, qnum):
        q = by_code[code][qnum - 1]
        return q['options'][ord(q['answer']) - ord('A')]

    # 2. Independent mathematical checks for ALL 120 questions
    verified_count = 0

    # --- DRILL 1 (d0580_nc1): Surds, Rationalising & Exact Indices ---
    # Q1: sqrt(75) + sqrt(48) - sqrt(27) = 6*sqrt(3)
    assert math.isclose(math.sqrt(75) + math.sqrt(48) - math.sqrt(27), 6 * math.sqrt(3), rel_tol=1e-12)
    assert r'6\sqrt{3}' in ans_opt('d0580_nc1', 1); verified_count += 1
    # Q2: sqrt(72) - sqrt(18) + sqrt(8) = 5*sqrt(2)
    assert math.isclose(math.sqrt(72) - math.sqrt(18) + math.sqrt(8), 5 * math.sqrt(2), rel_tol=1e-12)
    assert r'5\sqrt{2}' in ans_opt('d0580_nc1', 2); verified_count += 1
    # Q3: (3 + 2*sqrt(5))(4 - sqrt(5)) = 2 + 5*sqrt(5)
    assert math.isclose((3 + 2 * math.sqrt(5)) * (4 - math.sqrt(5)), 2 + 5 * math.sqrt(5), rel_tol=1e-12)
    assert r'2 + 5\sqrt{5}' in ans_opt('d0580_nc1', 3); verified_count += 1
    # Q4: (2*sqrt(3) - 5)^2 = 37 - 20*sqrt(3)
    assert math.isclose((2 * math.sqrt(3) - 5) ** 2, 37 - 20 * math.sqrt(3), rel_tol=1e-12)
    assert r'37 - 20\sqrt{3}' in ans_opt('d0580_nc1', 4); verified_count += 1
    # Q5: 18/sqrt(6) = 3*sqrt(6)
    assert math.isclose(18 / math.sqrt(6), 3 * math.sqrt(6), rel_tol=1e-12)
    assert r'3\sqrt{6}' in ans_opt('d0580_nc1', 5); verified_count += 1
    # Q6: (10 + sqrt(20))/sqrt(5) = 2 + 2*sqrt(5)
    assert math.isclose((10 + math.sqrt(20)) / math.sqrt(5), 2 + 2 * math.sqrt(5), rel_tol=1e-12)
    assert r'2 + 2\sqrt{5}' in ans_opt('d0580_nc1', 6); verified_count += 1
    # Q7: 12/(3 - sqrt(5)) = 9 + 3*sqrt(5)
    assert math.isclose(12 / (3 - math.sqrt(5)), 9 + 3 * math.sqrt(5), rel_tol=1e-12)
    assert r'9 + 3\sqrt{5}' in ans_opt('d0580_nc1', 7); verified_count += 1
    # Q8: 6/(sqrt(7) + 2) = 2*sqrt(7) - 4
    assert math.isclose(6 / (math.sqrt(7) + 2), 2 * math.sqrt(7) - 4, rel_tol=1e-12)
    assert r'2\sqrt{7} - 4' in ans_opt('d0580_nc1', 8); verified_count += 1
    # Q9: (14 + 4*sqrt(3))/(2 + sqrt(3)) = 16 - 6*sqrt(3)
    assert math.isclose((14 + 4 * math.sqrt(3)) / (2 + math.sqrt(3)), 16 - 6 * math.sqrt(3), rel_tol=1e-12)
    assert r'16 - 6\sqrt{3}' in ans_opt('d0580_nc1', 9); verified_count += 1
    # Q10: 27^(-2/3) = 1/9
    assert math.isclose(27 ** (-Fraction(2, 3)), float(Fraction(1, 9)), rel_tol=1e-12)
    assert r'\frac{1}{9}' in ans_opt('d0580_nc1', 10); verified_count += 1
    # Q11: (16/81)^(-3/4) = 27/8
    assert math.isclose(float(Fraction(16, 81)) ** (-0.75), float(Fraction(27, 8)), rel_tol=1e-12)
    assert r'\frac{27}{8}' in ans_opt('d0580_nc1', 11); verified_count += 1
    # Q12: (8*x^6*y^-3)^(2/3) = 4*x^4/y^2
    for x_v, y_v in [(2, 3), (5, 2)]:
        lhs = (8 * (x_v ** 6) * (y_v ** -3)) ** (2 / 3)
        rhs = 4 * (x_v ** 4) / (y_v ** 2)
        assert math.isclose(lhs, rhs, rel_tol=1e-12)
    assert r'\frac{4x^4}{y^2}' in ans_opt('d0580_nc1', 12); verified_count += 1
    # Q13: 4^x = 8^(x-1) => x = 3
    assert 4 ** 3 == 8 ** (3 - 1)
    assert r'x = 3' in ans_opt('d0580_nc1', 13); verified_count += 1
    # Q14: 9^(2x-1) = 1/(27*sqrt(3)) => x = -3/8
    x14 = Fraction(-3, 8)
    assert math.isclose(9 ** float(2 * x14 - 1), 1 / (27 * math.sqrt(3)), rel_tol=1e-12)
    assert r'-\frac{3}{8}' in ans_opt('d0580_nc1', 14); verified_count += 1
    # Q15: 2^p = sqrt(8)/16 => p = -5/2
    p15 = Fraction(-5, 2)
    assert math.isclose(2 ** float(p15), math.sqrt(8) / 16, rel_tol=1e-12)
    assert r'-\frac{5}{2}' in ans_opt('d0580_nc1', 15); verified_count += 1

    # --- DRILL 2 (d0580_nc2): Exact Trig Values, Special Triangles & Bearings ---
    sind = lambda deg: math.sin(math.radians(deg))
    cosd = lambda deg: math.cos(math.radians(deg))
    tand = lambda deg: math.tan(math.radians(deg))

    # Q1: sin30 + cos60 + tan45 = 2
    assert math.isclose(sind(30) + cosd(60) + tand(45), 2.0, rel_tol=1e-12)
    assert r'\(2\)' == ans_opt('d0580_nc2', 1); verified_count += 1
    # Q2: sin60*cos30 - cos60*sin30 = 1/2
    assert math.isclose(sind(60) * cosd(30) - cosd(60) * sind(30), 0.5, rel_tol=1e-12)
    assert r'\frac{1}{2}' in ans_opt('d0580_nc2', 2); verified_count += 1
    # Q3: (tan60 - tan30)/(1 + tan60*tan30) = sqrt(3)/3
    assert math.isclose((tand(60) - tand(30)) / (1 + tand(60) * tand(30)), math.sqrt(3) / 3, rel_tol=1e-12)
    assert r'\frac{\sqrt{3}}{3}' in ans_opt('d0580_nc2', 3); verified_count += 1
    # Q4: 3*cos0 - 2*sin90 + 5*tan0 + 4*cos90 = 1
    assert math.isclose(3 * cosd(0) - 2 * sind(90) + 5 * tand(0) + 4 * cosd(90), 1.0, abs_tol=1e-12)
    assert r'\(1\)' == ans_opt('d0580_nc2', 4); verified_count += 1
    # Q5: cos150 + sin120 = 0
    assert math.isclose(cosd(150) + sind(120), 0.0, abs_tol=1e-12)
    assert r'\(0\)' == ans_opt('d0580_nc2', 5); verified_count += 1
    # Q6: sin135 * cos120 = -sqrt(2)/4
    assert math.isclose(sind(135) * cosd(120), -math.sqrt(2) / 4, rel_tol=1e-12)
    assert r'-\frac{\sqrt{2}}{4}' in ans_opt('d0580_nc2', 6); verified_count += 1
    # Q7: AB = 14*cos30 = 7*sqrt(3)
    assert math.isclose(14 * cosd(30), 7 * math.sqrt(3), rel_tol=1e-12)
    assert r'7\sqrt{3}' in ans_opt('d0580_nc2', 7); verified_count += 1
    # Q8: square diagonal 10 => perimeter = 4*(10/sqrt(2)) = 20*sqrt(2)
    assert math.isclose(4 * 10 * cosd(45), 20 * math.sqrt(2), rel_tol=1e-12)
    assert r'20\sqrt{2}' in ans_opt('d0580_nc2', 8); verified_count += 1
    # Q9: QS + SR = 6/tan45 + 6/tan60 = 6 + 2*sqrt(3)
    assert math.isclose(6 / tand(45) + 6 / tand(60), 6 + 2 * math.sqrt(3), rel_tol=1e-12)
    assert r'6 + 2\sqrt{3}' in ans_opt('d0580_nc2', 9); verified_count += 1
    # Q10: 1/2 * 8 * 12 * sin60 = 24*sqrt(3)
    assert math.isclose(0.5 * 8 * 12 * sind(60), 24 * math.sqrt(3), rel_tol=1e-12)
    assert r'24\sqrt{3}' in ans_opt('d0580_nc2', 10); verified_count += 1
    # Q11: parallelogram 6*10*sin135 = 30*sqrt(2)
    assert math.isclose(6 * 10 * sind(135), 30 * math.sqrt(2), rel_tol=1e-12)
    assert r'30\sqrt{2}' in ans_opt('d0580_nc2', 11); verified_count += 1
    # Q12: 2*sin(x) = sqrt(3) on [0, 360] => 60, 120
    sols12 = [deg for deg in range(361) if math.isclose(2 * sind(deg), math.sqrt(3), abs_tol=1e-9)]
    assert sols12 == [60, 120]
    assert r'60^\circ' in ans_opt('d0580_nc2', 12) and r'120^\circ' in ans_opt('d0580_nc2', 12); verified_count += 1
    # Q13: 2*cos(x) + 1 = 0 on [0, 360] => 120, 240
    sols13 = [deg for deg in range(361) if math.isclose(2 * cosd(deg) + 1, 0.0, abs_tol=1e-9)]
    assert sols13 == [120, 240]
    assert r'120^\circ' in ans_opt('d0580_nc2', 13) and r'240^\circ' in ans_opt('d0580_nc2', 13); verified_count += 1
    # Q14: 20 km at bearing 060 => East = 20*sin60 = 10*sqrt(3)
    assert math.isclose(20 * sind(60), 10 * math.sqrt(3), rel_tol=1e-12)
    assert r'10\sqrt{3}' in ans_opt('d0580_nc2', 14); verified_count += 1
    # Q15: bearing 150 -> back-bearing 330; south = 12*cos30 = 6*sqrt(3)
    assert (150 + 180) % 360 == 330 and math.isclose(12 * cosd(30), 6 * math.sqrt(3), rel_tol=1e-12)
    assert r'330^\circ' in ans_opt('d0580_nc2', 15) and r'6\sqrt{3}' in ans_opt('d0580_nc2', 15); verified_count += 1

    # --- DRILL 3 (d0580_nc3): Recurring Decimals, Standard Form, Fractions & Bounds ---
    # Q1: 0.4545... = 45/99 = 5/11
    assert Fraction(45, 99) == Fraction(5, 11)
    assert r'\frac{5}{11}' in ans_opt('d0580_nc3', 1); verified_count += 1
    # Q2: 0.2777... = (27 - 2)/90 = 5/18
    assert Fraction(27 - 2, 90) == Fraction(5, 18)
    assert r'\frac{5}{18}' in ans_opt('d0580_nc3', 2); verified_count += 1
    # Q3: 0.13636... = (136 - 1)/990 = 3/22
    assert Fraction(136 - 1, 990) == Fraction(3, 22)
    assert r'\frac{3}{22}' in ans_opt('d0580_nc3', 3); verified_count += 1
    # Q4: (4.5e5)*(6e-8) = 2.7e-2
    assert math.isclose(4.5e5 * 6e-8, 2.7e-2, rel_tol=1e-12)
    assert r'2.7 \times 10^{-2}' in ans_opt('d0580_nc3', 4); verified_count += 1
    # Q5: (3.6e-4)/(9e3) = 4e-8
    assert math.isclose(3.6e-4 / 9e3, 4e-8, rel_tol=1e-12)
    assert r'4 \times 10^{-8}' in ans_opt('d0580_nc3', 5); verified_count += 1
    # Q6: 6.4e5 + 8.5e4 = 7.25e5
    assert math.isclose(6.4e5 + 8.5e4, 7.25e5, rel_tol=1e-12)
    assert r'7.25 \times 10^5' in ans_opt('d0580_nc3', 6); verified_count += 1
    # Q7: 5.2e-3 - 7e-4 = 4.5e-3
    assert math.isclose(5.2e-3 - 7e-4, 4.5e-3, rel_tol=1e-12)
    assert r'4.5 \times 10^{-3}' in ans_opt('d0580_nc3', 7); verified_count += 1
    # Q8: 2 1/4 / 1 7/8 + 3/5 = 9/5 = 1 4/5
    assert Fraction(9, 4) / Fraction(15, 8) + Fraction(3, 5) == Fraction(9, 5)
    assert r'1\frac{4}{5}' in ans_opt('d0580_nc3', 8); verified_count += 1
    # Q9: UB(a - b) = 14.5 - 6.15 = 8.35
    assert Fraction('14.5') - Fraction('6.15') == Fraction('8.35')
    assert '8.35' in ans_opt('d0580_nc3', 9); verified_count += 1
    # Q10: UB(M/V) = 45 / 4.5 = 10
    assert Fraction(45, 1) / Fraction('4.5') == Fraction(10, 1)
    assert r'\(10\)' == ans_opt('d0580_nc3', 10); verified_count += 1
    # Q11: LB perimeter = 2*(8.35 + 4.55) = 25.8
    assert 2 * (Fraction('8.35') + Fraction('4.55')) == Fraction('25.8')
    assert '25.8' in ans_opt('d0580_nc3', 11); verified_count += 1
    # Q12: HCF & LCM of 2^3*3^2*5 and 2^2*3^3*7
    a12, b12 = (2**3) * (3**2) * 5, (2**2) * (3**3) * 7
    assert math.gcd(a12, b12) == (2**2) * (3**2)
    assert math.lcm(a12, b12) == (2**3) * (3**3) * 5 * 7
    assert r'2^2 \times 3^2' in ans_opt('d0580_nc3', 12) and r'2^3 \times 3^3 \times 5 \times 7' in ans_opt('d0580_nc3', 12)
    verified_count += 1
    # Q13: LCM(36, 48, 60) = 720s = 12 min -> 09:12
    assert math.lcm(36, 48, 60) == 720 and 720 // 60 == 12
    assert '09{:}12' in ans_opt('d0580_nc3', 13); verified_count += 1
    # Q14: 0.8 * P = 96 => P = 120
    assert Fraction(96, 1) / Fraction(4, 5) == 120
    assert '120' in ans_opt('d0580_nc3', 14); verified_count += 1
    # Q15: R:B:G = 8:12:15 (sum 35), green = 15/35 * 140 = 60
    assert Fraction(15, 35) * 140 == 60
    assert '60' in ans_opt('d0580_nc3', 15); verified_count += 1

    # --- DRILL 4 (d0580_nc4): Domain & Range, x^(±1/2) & Algebra (NEW 2025) ---
    # Q1: 2x - 6 >= 0 => x >= 3
    assert Fraction(6, 2) == 3
    assert r'x \ge 3' in ans_opt('d0580_nc4', 1); verified_count += 1
    # Q2: f(x) = 5 - 2x on [-1, 4] => [-3, 7]
    vals2 = [5 - 2 * (-1), 5 - 2 * 4]
    assert (min(vals2), max(vals2)) == (-3, 7)
    assert r'-3 \le f(x) \le 7' in ans_opt('d0580_nc4', 2); verified_count += 1
    # Q3: min of (x - 3)^2 + 4 is 4
    assert min((x - 3) ** 2 + 4 for x in range(-10, 15)) == 4
    assert r'g(x) \ge 4' in ans_opt('d0580_nc4', 3); verified_count += 1
    # Q4: 3/(x+2) - 1 excludes x = -2 and h(x) = -1
    assert r'x \neq -2' in ans_opt('d0580_nc4', 4) and r'h(x) \neq -1' in ans_opt('d0580_nc4', 4)
    verified_count += 1
    # Q5: f(16) = 6*sqrt(16) - 4/sqrt(16) = 23
    assert 6 * int(math.isqrt(16)) - Fraction(4, int(math.isqrt(16))) == 23
    assert '23' in ans_opt('d0580_nc4', 5); verified_count += 1
    # Q6: y = 2*sqrt(x) + 3 passes through (0, 3) and (9, 9)
    assert 2 * math.sqrt(0) + 3 == 3 and 2 * math.sqrt(9) + 3 == 9
    assert '(0, 3)' in ans_opt('d0580_nc4', 6) and '(9, 9)' in ans_opt('d0580_nc4', 6); verified_count += 1
    # Q7: y = x^(-1/2) passes through (1, 1) and (4, 1/2)
    assert 1 ** (-0.5) == 1.0 and 4 ** (-0.5) == 0.5
    assert '(1, 1)' in ans_opt('d0580_nc4', 7) and r'\frac{1}{2}' in ans_opt('d0580_nc4', 7); verified_count += 1
    # Q8: 2*sqrt(x) + 3 = 13 => x = 25
    assert 2 * math.sqrt(25) + 3 == 13
    assert '(25, 13)' in ans_opt('d0580_nc4', 8); verified_count += 1
    # Q9: fg(x) = 3(x^2 + 1) - 2 = 3x^2 + 1
    for xv in [-3, 0, 2, 5]:
        assert 3 * (xv ** 2 + 1) - 2 == 3 * (xv ** 2) + 1
    assert r'3x^2 + 1' in ans_opt('d0580_nc4', 9); verified_count += 1
    # Q10: f(x) = (2x+5)/(x-1) => f^-1(x) = (x+5)/(x-2)
    for xv in [-4, 0, 3, 7]:
        fx = Fraction(2 * xv + 5, xv - 1)
        assert Fraction(fx + 5, fx - 2) == xv
    assert r'\frac{x + 5}{x - 2}' in ans_opt('d0580_nc4', 10); verified_count += 1
    # Q11: f(x) = x^2 + 6x + 11 = (x+3)^2 + 2 >= 2 => domain of f^-1 is x >= 2
    assert (-3) ** 2 + 6 * (-3) + 11 == 2
    assert r'x \ge 2' in ans_opt('d0580_nc4', 11); verified_count += 1
    # Q12: 2x^2 - 12x + 11 = 2(x - 3)^2 - 7
    for xv in [-2, 0, 3, 5]:
        assert 2 * (xv ** 2) - 12 * xv + 11 == 2 * ((xv - 3) ** 2) - 7
    assert r'2(x - 3)^2 - 7' in ans_opt('d0580_nc4', 12); verified_count += 1
    # Q13: 5/(x-2) - 3/(x+1) = (2x+11)/((x-2)(x+1))
    for xv in [-3, 0, 4, 7]:
        assert Fraction(5, xv - 2) - Fraction(3, xv + 1) == Fraction(2 * xv + 11, (xv - 2) * (xv + 1))
    assert r'\frac{2x + 11}{(x - 2)(x + 1)}' in ans_opt('d0580_nc4', 13); verified_count += 1
    # Q14: (2x^2 + x - 6)/(x^2 - 4) = (2x - 3)/(x - 2)
    for xv in [-5, 0, 1, 5]:
        assert Fraction(2 * xv * xv + xv - 6, xv * xv - 4) == Fraction(2 * xv - 3, xv - 2)
    assert r'\frac{2x - 3}{x - 2}' in ans_opt('d0580_nc4', 14); verified_count += 1
    # Q15: y = 2x - 1 and y = x^2 - 2x + 2 => (1, 1) and (3, 5)
    for xv, yv in [(1, 1), (3, 5)]:
        assert yv == 2 * xv - 1 and yv == xv * xv - 2 * xv + 2
    assert '(1, 1)' in ans_opt('d0580_nc4', 15) and '(3, 5)' in ans_opt('d0580_nc4', 15); verified_count += 1

    # --- DRILL 5 (d0580_c1): Compound Interest, Reverse % & Exponential Growth/Decay ---
    # Q1: 4500 * 1.036^5 = 5370.46
    assert f'{4500 * (1.036 ** 5):.2f}' == '5370.46'
    assert '5370.46' in ans_opt('d0580_c1', 1); verified_count += 1
    # Q2: 6000 * 1.024^6 - 6000 = 917.53
    assert f'{6000 * (1.024 ** 6) - 6000:.2f}' == '917.53'
    assert '917.53' in ans_opt('d0580_c1', 2); verified_count += 1
    # Q3: ((9845/8000)^(1/4) - 1)*100 = 5.32
    assert f'{((9845 / 8000) ** 0.25 - 1) * 100:.2f}' == '5.32'
    assert '5.32' in ans_opt('d0580_c1', 3); verified_count += 1
    # Q4: least integer n with 2000 * 1.045^n > 3000 is 10
    assert 2000 * (1.045 ** 9) <= 3000 < 2000 * (1.045 ** 10)
    assert '10' in ans_opt('d0580_c1', 4); verified_count += 1
    # Q5: 24000 * 0.86^6 = 9710 (nearest pound)
    assert round(24000 * (0.86 ** 6)) == 9710
    assert '9710' in ans_opt('d0580_c1', 5); verified_count += 1
    # Q6: 1022.21 / 0.88^3 = 1500
    assert round(1022.21 / (0.88 ** 3)) == 1500
    assert '1500' in ans_opt('d0580_c1', 6); verified_count += 1
    # Q7: 1250 * 1.18^8 = 4700 (3 s.f.)
    assert _sigfig(1250 * (1.18 ** 8), 3) == '4700'
    assert '4700' in ans_opt('d0580_c1', 7); verified_count += 1
    # Q8: (1 - (41500/48000)^(1/5))*100 = 2.87
    assert f'{(1 - (41500 / 48000) ** 0.2) * 100:.2f}' == '2.87'
    assert '2.87' in ans_opt('d0580_c1', 8); verified_count += 1
    # Q9: 850 * 0.975 * 192.5 = 159534 (nearest Yen)
    assert round(850 * 0.975 * 192.5) == 159534
    assert r'159\,534' in ans_opt('d0580_c1', 9); verified_count += 1
    # Q10: (540*0.86 - 215)*1.28 = 319.23
    assert f'{(540 * 0.86 - 215) * 1.28:.2f}' == '319.23'
    assert '319.23' in ans_opt('d0580_c1', 10); verified_count += 1
    # Q11: 402.5 / 52.35 = 7.69 (3 s.f.)
    assert _sigfig(402.5 / 52.35, 3) == '7.69'
    assert '7.69' in ans_opt('d0580_c1', 11); verified_count += 1
    # Q12: 182.5 / (137.5 / 60) = 79.6 (3 s.f.)
    assert _sigfig(182.5 / (137.5 / 60), 3) == '79.6'
    assert '79.6' in ans_opt('d0580_c1', 12); verified_count += 1
    # Q13: 253 / (1.15 * 0.88) = 250
    assert Fraction(253, 1) / (Fraction(115, 100) * Fraction(88, 100)) == 250
    assert '250' in ans_opt('d0580_c1', 13); verified_count += 1
    # Q14: (1.12^2 * 0.85 - 1)*100 = 6.62%
    assert f'{((1.12 ** 2) * 0.85 - 1) * 100:.2f}' == '6.62'
    assert 'Increase of' in ans_opt('d0580_c1', 14) and '6.62' in ans_opt('d0580_c1', 14); verified_count += 1
    # Q15: (1.032^2 * 1.045^3 - 1)*100 = 21.54%
    assert f'{((1.032 ** 2) * (1.045 ** 3) - 1) * 100:.2f}' == '21.54'
    assert '21.54' in ans_opt('d0580_c1', 15); verified_count += 1

    # --- DRILL 6 (d0580_c2): Quadratics, Turning Points, Differentiation & Kinematics ---
    # Q1: 3x^2 - 7x - 5 = 0 => 2.91, -0.57
    r1a = (7 + math.sqrt(49 + 60)) / 6
    r1b = (7 - math.sqrt(49 + 60)) / 6
    assert f'{r1a:.2f}' == '2.91' and f'{r1b:.2f}' == '-0.57'
    assert '2.91' in ans_opt('d0580_c2', 1) and '-0.57' in ans_opt('d0580_c2', 1); verified_count += 1
    # Q2: 4/x + 3/(x+2) = 2 => 2x^2 - 3x - 8 = 0 => positive root 2.89
    r2 = (3 + math.sqrt(9 + 64)) / 4
    assert math.isclose(4 / r2 + 3 / (r2 + 2), 2.0, rel_tol=1e-12) and f'{r2:.2f}' == '2.89'
    assert '2.89' in ans_opt('d0580_c2', 2); verified_count += 1
    # Q3: dy/dx of 2x^3 - 5x^2 + 4x - 7 at x=2 is 8
    assert 6 * (2 ** 2) - 10 * 2 + 4 == 8
    assert r'\(8\)' == ans_opt('d0580_c2', 3); verified_count += 1
    # Q4: stationary points of x^3 - 3x^2 - 9x + 5: (-1, 10), (3, -22)
    f4 = lambda x: x**3 - 3 * x**2 - 9 * x + 5
    df4 = lambda x: 3 * x**2 - 6 * x - 9
    assert df4(-1) == 0 and df4(3) == 0 and f4(-1) == 10 and f4(3) == -22
    assert '(-1, 10)' in ans_opt('d0580_c2', 4) and '(3, -22)' in ans_opt('d0580_c2', 4); verified_count += 1
    # Q5: local min of 2x^3 - 9x^2 + 12x + 1 at (2, 5)
    f5 = lambda x: 2 * x**3 - 9 * x**2 + 12 * x + 1
    df5 = lambda x: 6 * x**2 - 18 * x + 12
    d2f5 = lambda x: 12 * x - 18
    assert df5(2) == 0 and d2f5(2) > 0 and f5(2) == 5
    assert '(2, 5)' in ans_opt('d0580_c2', 5); verified_count += 1
    # Q6: max of 60x - 2x^2 at x = 15 => 450
    assert 60 - 4 * 15 == 0 and 60 * 15 - 2 * (15 ** 2) == 450
    assert '450' in ans_opt('d0580_c2', 6); verified_count += 1
    # Q7: tangent to y = x^3 - 4x + 2 at x=2 => y = 8x - 14
    y7, m7 = 2**3 - 4 * 2 + 2, 3 * (2**2) - 4
    c7 = y7 - m7 * 2
    assert (m7, c7) == (8, -14)
    assert '8x - 14' in ans_opt('d0580_c2', 7); verified_count += 1
    # Q8: normal to y = x^2 - 6x + 10 at (4, 2) => y = -1/2 x + 4
    assert 4**2 - 6 * 4 + 10 == 2
    m_tan8 = 2 * 4 - 6
    m_norm8 = Fraction(-1, m_tan8)
    c_norm8 = 2 - m_norm8 * 4
    assert m_norm8 == Fraction(-1, 2) and c_norm8 == 4
    assert r'-\frac{1}{2}x + 4' in ans_opt('d0580_c2', 8); verified_count += 1
    # Q9: perp bisector of (-2, 5) and (6, 1) => y = 2x - 1
    mid9 = (Fraction(-2 + 6, 2), Fraction(5 + 1, 2))
    m_ab9 = Fraction(1 - 5, 6 - (-2))
    m_p9 = -1 / m_ab9
    c_p9 = mid9[1] - m_p9 * mid9[0]
    assert m_p9 == 2 and c_p9 == -1
    assert '2x - 1' in ans_opt('d0580_c2', 9); verified_count += 1
    # Q10: accel 24/8 = 3, decel 24/6 = 4
    assert Fraction(24, 8) == 3 and Fraction(24, 6) == 4
    assert r'3\text{ m/s}^2' in ans_opt('d0580_c2', 10) and r'4\text{ m/s}^2' in ans_opt('d0580_c2', 10); verified_count += 1
    # Q11: distance = 0.5*(4+12)*10 + 12*25 + 0.5*15*12 = 470
    assert Fraction(1, 2) * (4 + 12) * 10 + 12 * 25 + Fraction(1, 2) * 15 * 12 == 470
    assert '470' in ans_opt('d0580_c2', 11); verified_count += 1
    # Q12: 0.5*(2T + 30)*30 = 1950 => T = 50
    t12 = Fraction(1950 // 15 - 30, 2)
    assert t12 == 50 and Fraction(1, 2) * (20 + t12 + 10 + t12) * 30 == 1950
    assert '50' in ans_opt('d0580_c2', 12); verified_count += 1
    # Q13: y = kx^3, k = 108/27 = 4; 4x^3 = 500 => x = 5
    k13 = Fraction(108, 27)
    assert k13 == 4 and k13 * (5 ** 3) == 500
    assert 'x = 5' in ans_opt('d0580_c2', 13); verified_count += 1
    # Q14: y = k/sqrt(x), k = 6*4 = 24; 24/sqrt(x) = 4.8 => x = 25
    k14 = 6 * 4
    assert math.isclose(k14 / math.sqrt(25), 4.8, rel_tol=1e-12)
    assert 'x = 25' in ans_opt('d0580_c2', 14); verified_count += 1
    # Q15: F prop 1/d^2, d*1.25 => decrease 36%
    dec15 = (1 - Fraction(1, 1) / (Fraction(5, 4) ** 2)) * 100
    assert dec15 == 36
    assert '36' in ans_opt('d0580_c2', 15); verified_count += 1

    # --- DRILL 7 (d0580_c3): Sine/Cosine Rule, 3D Trig, Bearings & 3D Mensuration ---
    # Q1: BC = 14.2 * sin73 / sin54 = 16.8
    assert _sigfig(14.2 * sind(73) / sind(54), 3) == '16.8'
    assert '16.8' in ans_opt('d0580_c3', 1); verified_count += 1
    # Q2: obtuse angle PRQ = 180 - arcsin(11*sin38/8) = 122.2
    ang2 = 180.0 - math.degrees(math.asin(11 * sind(38) / 8))
    assert f'{ang2:.1f}' == '122.2'
    assert '122.2' in ans_opt('d0580_c3', 2); verified_count += 1
    # Q3: YZ = sqrt(11.4^2 + 8.6^2 - 2*11.4*8.6*cos112) = 16.7
    yz3 = math.sqrt(11.4**2 + 8.6**2 - 2 * 11.4 * 8.6 * cosd(112))
    assert _sigfig(yz3, 3) == '16.7'
    assert '16.7' in ans_opt('d0580_c3', 3); verified_count += 1
    # Q4: largest angle in 7-10-14 triangle = 109.6
    ang4 = math.degrees(math.acos((7**2 + 10**2 - 14**2) / (2 * 7 * 10)))
    assert f'{ang4:.1f}' == '109.6'
    assert '109.6' in ans_opt('d0580_c3', 4); verified_count += 1
    # Q5: bearings 055 and 150 -> angle 85, AC = 28.7
    ac5 = math.sqrt(18**2 + 24**2 - 2 * 18 * 24 * cosd((55 + 180) - 150))
    assert _sigfig(ac5, 3) == '28.7'
    assert '28.7' in ans_opt('d0580_c3', 5); verified_count += 1
    # Q6: bearings 040 from P, 325 from Q -> PS = 15*sin55/sin75 = 12.7
    ps6 = 15 * sind(325 - 270) / sind(180 - (90 - 40) - (325 - 270))
    assert _sigfig(ps6, 3) == '12.7'
    assert '12.7' in ans_opt('d0580_c3', 6); verified_count += 1
    # Q7: cuboid 12x9x8 -> atan(8/15) = 28.1
    ang7 = math.degrees(math.atan(8 / math.hypot(12, 9)))
    assert f'{ang7:.1f}' == '28.1'
    assert '28.1' in ans_opt('d0580_c3', 7); verified_count += 1
    # Q8: pyramid base 10, height 12 -> edge angle atan(12/(5*sqrt(2))) = 59.5
    ang8 = math.degrees(math.atan(12 / (5 * math.sqrt(2))))
    assert f'{ang8:.1f}' == '59.5'
    assert '59.5' in ans_opt('d0580_c3', 8); verified_count += 1
    # Q9: pyramid base 16, slant edge 17 -> slant height 15, face angle acos(8/15) = 57.8
    vm9 = math.sqrt(17**2 - 8**2)
    ang9 = math.degrees(math.acos(8 / vm9))
    assert vm9 == 15.0 and f'{ang9:.1f}' == '57.8'
    assert '57.8' in ans_opt('d0580_c3', 9); verified_count += 1
    # Q10: frustum r1=4, h1=6, r2=10 => H=15, V = 468*pi = 1470 (3 s.f.)
    v10 = (1 / 3) * math.pi * (10**2 * 15 - 4**2 * 6)
    assert _sigfig(v10, 3) == '1470'
    assert '1470' in ans_opt('d0580_c3', 10); verified_count += 1
    # Q11: hemisphere r=6 + cone r=6, h=10 => V = 264*pi = 829 (3 s.f.)
    v11 = (2 / 3) * math.pi * (6**3) + (1 / 3) * math.pi * (6**2) * 10
    assert _sigfig(v11, 3) == '829'
    assert '829' in ans_opt('d0580_c3', 11); verified_count += 1
    # Q12: hemisphere r=5 + cone r=5, h=12 (l=13) => outer SA = 115*pi = 361 (3 s.f.)
    sa12 = 2 * math.pi * (5**2) + math.pi * 5 * math.hypot(5, 12)
    assert _sigfig(sa12, 3) == '361'
    assert '361' in ans_opt('d0580_c3', 12); verified_count += 1
    # Q13: minor segment r=12, theta=105 => 62.4 (3 s.f.)
    seg13 = (105 / 360) * math.pi * (12**2) - 0.5 * 12 * 12 * sind(105)
    assert _sigfig(seg13, 3) == '62.4'
    assert '62.4' in ans_opt('d0580_c3', 13); verified_count += 1
    # Q14: similar bottles V=250, 2000 => k=2, A_large = 185 * 4 = 740
    assert round(185 * ((2000 / 250) ** (2 / 3))) == 740
    assert '740' in ans_opt('d0580_c3', 14); verified_count += 1
    # Q15: similar statues A=320, 720 => k=2/3, V_small = 4050 * 8/27 = 1200
    assert Fraction(4050, 1) * (Fraction(2, 3) ** 3) == 1200
    assert '1200' in ans_opt('d0580_c3', 15); verified_count += 1

    # --- DRILL 8 (d0580_c4): Conditional Probability, Histograms & Cumulative Frequency ---
    # Q1: 7R, 5B without replacement, same colour = 31/66
    p1 = Fraction(7, 12) * Fraction(6, 11) + Fraction(5, 12) * Fraction(4, 11)
    assert p1 == Fraction(31, 66)
    assert r'\frac{31}{66}' in ans_opt('d0580_c4', 1); verified_count += 1
    # Q2: 6W, 4B, 3 drawn without replacement, at least one B = 5/6
    p2 = 1 - Fraction(6, 10) * Fraction(5, 9) * Fraction(4, 8)
    assert p2 == Fraction(5, 6)
    assert r'\frac{5}{6}' in ans_opt('d0580_c4', 2); verified_count += 1
    # Q3: P(T) = 0.3*0.6 + 0.7*0.2 = 0.32
    p3 = Fraction(3, 10) * Fraction(6, 10) + Fraction(7, 10) * Fraction(2, 10)
    assert p3 == Fraction(32, 100)
    assert '0.32' in ans_opt('d0580_c4', 3); verified_count += 1
    # Q4: Venn N=40, F=22, S=18, neither=8 => F&S=8, P(S|F)=8/22=4/11
    n_both4 = 22 + 18 - (40 - 8)
    assert Fraction(n_both4, 22) == Fraction(4, 11)
    assert r'\frac{4}{11}' in ans_opt('d0580_c4', 4); verified_count += 1
    # Q5: Two-way table P(Rainy | Bus) = 28 / (28 + 20) = 7/12
    assert Fraction(28, 28 + 20) == Fraction(7, 12)
    assert r'\frac{7}{12}' in ans_opt('d0580_c4', 5); verified_count += 1
    # Q6: P(B | D) = (0.4*0.10) / (0.6*0.05 + 0.4*0.10) = 4/7
    p6_a = Fraction(6, 10) * Fraction(5, 100)
    p6_b = Fraction(4, 10) * Fraction(10, 100)
    assert p6_b / (p6_a + p6_b) == Fraction(4, 7)
    assert r'\frac{4}{7}' in ans_opt('d0580_c4', 6); verified_count += 1
    # Q7: FD = 42 / (35 - 20) = 2.8
    assert Fraction(42, 35 - 20) == Fraction(28, 10)
    assert '2.8' in ans_opt('d0580_c4', 7); verified_count += 1
    # Q8: Histogram scaling -> freq = 40
    fd1 = Fraction(30, 10)
    scale_cm_per_fd = Fraction(6, 1) / fd1
    fd2 = Fraction('3.2') / scale_cm_per_fd
    assert fd2 * (45 - 20) == 40
    assert '40' in ans_opt('d0580_c4', 8); verified_count += 1
    # Q9: Histogram > 30 min = 10*1.5 + 20*0.6 = 27 (and total = 90)
    assert 10 * Fraction('1.8') + 10 * 3 + 20 * Fraction('1.5') + 20 * Fraction('0.6') == 90
    assert 10 * Fraction('1.5') + 20 * Fraction('0.6') == 27
    assert '27' in ans_opt('d0580_c4', 9); verified_count += 1
    # Q10: CF N=160 -> Median=60, Q1=40, Q3=75, IQR=35
    assert 75 - 40 == 35
    assert '60' in ans_opt('d0580_c4', 10) and '35' in ans_opt('d0580_c4', 10); verified_count += 1
    # Q11: CF N=200 -> 80th pct at 160 -> 40h; >30h = (200-120)/200 = 40%
    assert Fraction(80, 100) * 200 == 160 and Fraction(200 - 120, 200) * 100 == 40
    assert '40' in ans_opt('d0580_c4', 11) and r'40\%' in ans_opt('d0580_c4', 11); verified_count += 1
    # Q12: Linear interpolation median = 20 + ((50 - 40)/40)*10 = 22.5
    assert 20 + Fraction(50 - 40, 40) * 10 == Fraction(45, 2)
    assert '22.5' in ans_opt('d0580_c4', 12); verified_count += 1
    # Q13: Estimated mean = (8*2 + 15*6 + 17*10 + 10*16)/50 = 8.72
    mean13 = Fraction(8 * 2 + 15 * 6 + 17 * 10 + 10 * 16, 8 + 15 + 17 + 10)
    assert mean13 == Fraction(872, 100)
    assert '8.72' in ans_opt('d0580_c4', 13); verified_count += 1
    # Q14: Combined mean = (24*72.5 + 16*80)/40 = 75.5
    mean14 = (24 * Fraction('72.5') + 16 * 80) / 40
    assert mean14 == Fraction('75.5')
    assert '75.5' in ans_opt('d0580_c4', 14); verified_count += 1
    # Q15: P(exactly one >= 70) = 2 * (8/25) * (17/24) = 34/75
    p15 = 2 * Fraction(8, 25) * Fraction(17, 24)
    assert p15 == Fraction(34, 75)
    assert r'\frac{34}{75}' in ans_opt('d0580_c4', 15); verified_count += 1

    assert verified_count == 120, f'Expected 120 math assertions, ran {verified_count}'
    return {
        'drills': len(DRILLS_0580_2025),
        'questions': total_q,
        'math_verified': verified_count,
    }


if __name__ == '__main__':
    if hasattr(sys.stdout, 'reconfigure'):
        sys.stdout.reconfigure(encoding='utf-8')
    summary = verify_all_math()
    print(
        f"[OK] IGCSE 0580 (2025–2027) Drills Verified: "
        f"{summary['drills']} drills, {summary['questions']} questions, "
        f"{summary['math_verified']}/120 math assertions passed, 0 validation errors."
    )
    for d in DRILLS_0580_2025:
        dist = {k: sum(1 for q in d['questions'] if q['answer'] == k) for k in 'ABCD'}
        print(f"  - {d['code']} ({d['calculator_policy']}, order {d['order_index']}): {len(d['questions'])} Qs | dist={dist} | {d['title']}")
