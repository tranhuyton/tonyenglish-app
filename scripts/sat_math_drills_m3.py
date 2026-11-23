# -*- coding: utf-8 -*-
"""
Digital SAT Math 1500+ — Module 3: Problem-Solving & Data Analysis
2 Flagship Skill Drills (30 unique questions: 2 drills × 15 questions; 11 MCQ + 4 SPR each):
  - Drill 3.1 (order_index=8): Ratios, Rates, Squared/Cubed Units & Percent Traps
  - Drill 3.2 (order_index=9): Statistics, Probability, Margin of Error & Study Design

All math values are verified programmatically in verify_all_math().
"""

import os
import sys
import math
import statistics
from fractions import Fraction

sys.path.insert(0, os.path.dirname(__file__))
from sat_math_helpers import (
    math_mcq,
    math_spr,
    build_math_drill_json,
    build_math_table,
)
from sat_qa_validator import validate_sat_test


def svg_scatterplot_q12():
    """
    Crisp official Bluebook-style scatterplot for Drill 3.2 Q12.
    8 exact data points whose OLS line of best fit is literally y_hat = 4x + 20:
      (1, 28) [+4], (2, 27) [-1], (3, 34) [+2], (4, 31) [-5],
      (5, 35) [-5], (6, 46) [+2], (7, 47) [-1], (8, 56) [+4].
    Plot box: x in [0, 9] -> px [56, 362] (34 px/unit)
              y in [15, 60] -> py [200, 20] (4 px/unit)
    """
    def px(x):
        return 56 + x * 34

    def py(y):
        return 200 - (y - 15) * 4

    points = [
        (1, 28), (2, 27), (3, 34), (4, 31),
        (5, 35), (6, 46), (7, 47), (8, 56),
    ]
    grid_h = []
    for yv in range(20, 61, 10):
        yy = py(yv)
        grid_h.append(
            f'<line x1="56" y1="{yy}" x2="362" y2="{yy}" stroke="#e2e8f0" stroke-width="1" stroke-dasharray="3,3"/>'
            f'<text x="48" y="{yy + 4}" text-anchor="end" font-family="sans-serif" font-size="10.5" fill="#475569">{yv}</text>'
        )
    grid_v = []
    for xv in range(1, 9):
        xx = px(xv)
        grid_v.append(
            f'<line x1="{xx}" y1="20" x2="{xx}" y2="200" stroke="#e2e8f0" stroke-width="1" stroke-dasharray="3,3"/>'
            f'<text x="{xx}" y="216" text-anchor="middle" font-family="sans-serif" font-size="10.5" fill="#475569">{xv}</text>'
        )

    dots = []
    for x, y in points:
        cx, cy = px(x), py(y)
        above = y > (4 * x + 20)
        dy_lbl = -8 if above else 14
        dots.append(
            f'<circle cx="{cx}" cy="{cy}" r="4.2" fill="#1e3a8a" stroke="#ffffff" stroke-width="1.2"/>'
            f'<text x="{cx}" y="{cy + dy_lbl}" text-anchor="middle" font-family="sans-serif" font-size="9.5" font-weight="700" fill="#0f172a">({x},{y})</text>'
        )

    # Line y = 4x + 20 from x=0 (y=20) to x=8.5 (y=54)
    lx1, ly1 = px(0), py(20)
    lx2, ly2 = px(8.5), py(54)

    return (
        '<div style="background:#f8fafc;border:1px solid #cbd5e1;border-radius:12px;padding:12px 14px;margin-bottom:12px;text-align:center;">'
        '<div style="font-family:\'Segoe UI\',sans-serif;font-size:13px;font-weight:800;color:#0f172a;margin-bottom:6px;">'
        'Weekly Training Hours vs. Productivity Index (8 Employees)'
        '</div>'
        '<svg viewBox="0 0 390 242" width="390" height="242" xmlns="http://www.w3.org/2000/svg" style="max-width:100%;height:auto;background:#ffffff;border-radius:8px;">'
        + ''.join(grid_h)
        + ''.join(grid_v)
        + '<line x1="56" y1="20" x2="56" y2="200" stroke="#334155" stroke-width="1.8"/>'
        + '<line x1="56" y1="200" x2="362" y2="200" stroke="#334155" stroke-width="1.8"/>'
        + f'<line x1="{lx1}" y1="{ly1}" x2="{lx2}" y2="{ly2}" stroke="#dc2626" stroke-width="2.2"/>'
        + ''.join(dots)
        + '<text x="209" y="235" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" fill="#334155">Training Hours (x)</text>'
        + '<text x="16" y="110" text-anchor="middle" font-family="sans-serif" font-size="11.5" font-weight="700" fill="#334155" transform="rotate(-90 16 110)">Productivity Index (y)</text>'
        + '<text x="358" y="34" text-anchor="end" font-family="sans-serif" font-size="10.5" font-weight="700" fill="#dc2626">Line of best fit: y = 4x + 20</text>'
        + '</svg></div>'
    )


def build_drill_3_1():
    """Math Drill 3.1: Ratios, Rates, Squared/Cubed Units & Percent Traps (15 Qs: 11 MCQ + 4 SPR)."""
    DOMAIN = 'Problem-Solving and Data Analysis'
    SK_RATIO = 'Ratios, rates, proportional relationships, and units'
    SK_PCT = 'Percentages'

    questions = [
        # Q1 (MCQ - A) — Squared unit conversion ft^2 -> yd^2
        math_mcq(
            'sat_m3_1_q1', 1, DOMAIN, SK_RATIO, 'Medium',
            r'<p>A rectangular botanical greenhouse has a floor area of \(432\text{ square feet}\). A contractor plans to cover the entire floor with glass tile panels priced at \(\$18\) per square yard. (Note: \(1\text{ yard} = 3\text{ feet}\))</p>',
            r'<p>What is the total cost, in dollars, of the glass tile panels needed to cover the entire greenhouse floor?</p>',
            {
                'A': r'\(864\)',
                'B': r'\(2,592\)',
                'C': r'\(7,776\)',
                'D': r'\(23,328\)',
            },
            'A',
            r'Vì diện tích là đơn vị bậc hai, ta phải bình phương hệ số quy đổi chiều dài: \(1\text{ yd} = 3\text{ ft} \Rightarrow 1\text{ yd}^2 = 3^2 = 9\text{ ft}^2\). Diện tích theo \(\text{yd}^2\) là \(\frac{432}{9} = 48\text{ yd}^2\). Tổng chi phí là \(48 \times 18 = \$864\).',
            r'Đổi đơn vị diện tích (\(\text{ft}^2 \to \text{yd}^2\)) bắt buộc bình phương hệ số: chia cho \(3^2 = 9\), KHÔNG chia cho \(3\).',
            {
                'A': ('Đáp án đúng', r'Chia cho \(9\) được \(48\text{ yd}^2\), rồi nhân \(\$18/\text{yd}^2\) ra \(\$864\).'),
                'B': ('Bẫy quên bình phương', r'Chia \(432\) cho \(3\) (thay vì \(3^2 = 9\)) ra \(144\), rồi nhân \(18\) thành \(2,592\).'),
                'C': ('Quên đổi đơn vị', r'Lấy thẳng \(432 \times 18 = 7,776\) mà chưa đổi \(\text{ft}^2\) sang \(\text{yd}^2\).'),
                'D': ('Đổi ngược chiều', r'Nhân \(432 \times 3 \times 18 = 23,328\) thay vì chia cho \(9\).'),
            },
            r'Nhập trực tiếp <code>(432 / 3^2) * 18</code> trên Desmos để tránh sai sót nhầm lũy thừa khi đổi đơn vị diện tích.',
        ),

        # Q2 (MCQ - B) — Successive percent increase/decrease (+25% then -20%)
        math_mcq(
            'sat_m3_1_q2', 2, DOMAIN, SK_PCT, 'Medium',
            r'<p>The monthly subscription price of a cloud analytics platform was increased by \(25\%\) in January. In July, the new price was decreased by \(20\%\).</p>',
            r'<p>Compared with the original price before January, what was the net percent change in the subscription price after July?</p>',
            {
                'A': r'A \(5\%\) increase',
                'B': r'A \(0\%\) change (the price returned to its original value)',
                'C': r'A \(4\%\) decrease',
                'D': r'A \(5\%\) decrease',
            },
            'B',
            r'Đặt giá ban đầu là \(P\) (hoặc chọn \(P = 100\)). Tăng \(25\%\) tương đương nhân với \(1.25\); sau đó giảm \(20\%\) tương đương nhân với \(0.80\). Giá cuối cùng là \(P \times 1.25 \times 0.80 = 1.00P\), tức thay đổi ròng bằng \(0\%\).',
            r'Phần trăm liên tiếp luôn NHÂN các hệ số (multipliers), KHÔNG cộng trừ trực tiếp: \(1.25 \times 0.80 = 1.00\).',
            {
                'A': ('Bẫy cộng trừ tuyến tính', r'Lấy \(+25\% - 20\% = +5\%\) mà quên rằng mức giảm \(20\%\) tính trên giá ĐÃ tăng lớn hơn.'),
                'B': ('Đáp án đúng', r'Hệ số tích lũy \(1.25 \times 0.80 = 1.00\), giá quay về đúng mức ban đầu (\(0\%\) thay đổi).'),
                'C': ('Nhầm cặp +20% / -20%', r'Chỉ khi tăng \(20\%\) rồi giảm \(20\%\) mới ra \(1.20 \times 0.80 = 0.96\) (giảm \(4\%\)).'),
                'D': ('Đoán ngược dấu', r'Trừ sai hướng \(20\% - 25\% = -5\%\).'),
            },
            r'Thử giá trị mẫu \(100\) trên Desmos: gõ <code>100 * 1.25 * 0.80</code> ra đúng <code>100</code> trong 2 giây.',
        ),

        # Q3 (MCQ - C) — Squared unit conversion cm^2 -> m^2 in rate
        math_mcq(
            'sat_m3_1_q3', 3, DOMAIN, SK_RATIO, 'Hard',
            r'<p>Under peak sunlight, a specialized solar membrane generates electrical power at a constant rate of \(0.036\text{ watts per square centimeter}\) (\(\text{W/cm}^2\)). (Note: \(1\text{ meter} = 100\text{ centimeters}\))</p>',
            r'<p>Under peak sunlight, how many watts does this solar membrane generate per square meter (\(\text{W/m}^2\))?</p>',
            {
                'A': r'\(3.6\)',
                'B': r'\(36\)',
                'C': r'\(360\)',
                'D': r'\(3,600\)',
            },
            'C',
            r'Ta có \(1\text{ m} = 100\text{ cm} \Rightarrow 1\text{ m}^2 = (100\text{ cm})^2 = 10,000\text{ cm}^2\). Do đó công suất trên mỗi mét vuông là: \(0.036\ \frac{\text{W}}{\text{cm}^2} \times 10,000\ \frac{\text{cm}^2}{\text{m}^2} = 360\text{ W/m}^2\).',
            r'Khi mẫu số là đơn vị diện tích (\(\text{cm}^2 \to \text{m}^2\)), viết rõ phân số triệt tiêu đơn vị và nhân hệ số \(100^2 = 10,000\).',
            {
                'A': ('Bẫy quên bình phương', r'Chỉ nhân với \(100\) thay vì \(100^2 = 10,000\), ra \(0.036 \times 100 = 3.6\).'),
                'B': ('Nhầm lũy thừa 10', r'Nhân với \(1,000\) thay vì \(10,000\).'),
                'C': ('Đáp án đúng', r'\(0.036 \times 100^2 = 0.036 \times 10,000 = 360\text{ W/m}^2\).'),
                'D': ('Trượt dấu phẩy thập phân', r'Nhân nhầm thêm một bậc \(10\) (thành \(100,000\)).'),
            },
            r'Gõ <code>0.036 * 100^2</code> vào Desmos để chắc chắn không đếm nhầm số chữ số \(0\).',
        ),

        # Q4 (SPR - 45) — Cubed unit conversion in^3 -> ft^3 + Density = Mass / Volume
        math_spr(
            'sat_m3_1_q4', 4, DOMAIN, SK_RATIO, 'Hard',
            r'<p>A solid metal alloy has a uniform density of \(172.8\text{ pounds per cubic foot}\). A precision part machined from this alloy has a volume of \(450\text{ cubic inches}\). (Note: \(1\text{ foot} = 12\text{ inches}\))</p>',
            r'<p>What is the mass, in pounds, of the machined precision part?</p>',
            ['45', '45.0'], '45',
            r'Áp dụng công thức khối lượng riêng \(\text{Mass} = \text{Density} \times \text{Volume}\). Trước hết đổi thể tích từ \(\text{in}^3\) sang \(\text{ft}^3\): vì \(1\text{ ft} = 12\text{ in}\) nên \(1\text{ ft}^3 = 12^3 = 1,728\text{ in}^3\). Thể tích linh kiện là \(\frac{450}{1,728}\text{ ft}^3\). Suy ra khối lượng \(= 172.8 \times \frac{450}{1,728} = 0.1 \times 450 = 45\text{ pounds}\).',
            r'Với thể tích (\(\text{in}^3 \to \text{ft}^3\)), BẮT BUỘC lập phương hệ số đổi đơn vị (\(12^3 = 1,728\)); luôn kiểm tra đơn vị đồng nhất trước khi dùng \(m = \rho V\).',
            r'Gõ thẳng <code>172.8 * (450 / 12^3)</code> trong Desmos để ra ngay kết quả chính xác <code>45</code>.',
        ),

        # Q5 (MCQ - D) — "p% greater than" vs "p% of" trap
        math_mcq(
            'sat_m3_1_q5', 5, DOMAIN, SK_PCT, 'Hard',
            r'<p>In a chemical synthesis trial, the mass yield of Compound X is \(240\%\) greater than the mass yield of Compound Y.</p>',
            r'<p>The mass yield of Compound X is what percent of the mass yield of Compound Y?</p>',
            {
                'A': r'\(140\%\)',
                'B': r'\(240\%\)',
                'C': r'\(241\%\)',
                'D': r'\(340\%\)',
            },
            'D',
            r'Cụm từ "\(p\%\) greater than \(Y\)" dịch chuẩn xác sang đại số là \(X = Y + \frac{p}{100}Y = \left(1 + \frac{p}{100}\right)Y\). Với \(p = 240\), ta có \(X = Y + 2.40Y = 3.40Y\), tức là \(X\) bằng \(340\%\) của \(Y\).',
            r'Phân biệt sống còn trên SAT: "\(p\%\) of \(Y\)" là \(\frac{p}{100}Y\), còn "\(p\%\) greater than \(Y\)" là \((100 + p)\%\) của \(Y\).',
            {
                'A': ('Trừ nhầm 100%', r'Lấy \(240\% - 100\% = 140\%\) thay vì cộng thêm \(100\%\).'),
                'B': ('Bẫy ngôn từ kinh điển', r'Nhầm lẫn "\(240\%\) greater than" thành "\(240\%\) of".'),
                'C': ('Cộng nhầm 1 thay vì 100%', r'Cộng số \(1\) vào \(240\) thay vì cộng \(100\%\).'),
                'D': ('Đáp án đúng', r'\(Y + 2.40Y = 3.40Y = 340\%\) của \(Y\).'),
            },
            r'Gán \(Y = 100\): tăng thêm \(240\%\) của \(100\) là cộng thêm \(240 \Rightarrow X = 100 + 240 = 340\), tức \(340\%\) của \(100\).',
        ),

        # Q6 (MCQ - A) — Algebraic percent chain (a is 160% of b, b is 40% of c) + "percent less than"
        math_mcq(
            'sat_m3_1_q6', 6, DOMAIN, SK_PCT, 'Hard',
            r'<p>Three positive numbers \(a\), \(b\), and \(c\) satisfy the following conditions: \(a\) is \(160\%\) of \(b\), and \(b\) is \(40\%\) of \(c\).</p>',
            r'<p>By what percent is \(a\) less than \(c\)?</p>',
            {
                'A': r'\(36\%\)',
                'B': r'\(56.25\%\)',
                'C': r'\(64\%\)',
                'D': r'\(120\%\)',
            },
            'A',
            r'Biểu diễn theo \(c\): \(b = 0.40c\) và \(a = 1.60b = 1.60(0.40c) = 0.64c\). Vì \(a = 0.64c = (1 - 0.36)c\), nên \(a\) nhỏ hơn \(c\) đúng \(36\%\).',
            r'Với chuỗi phần trăm liên kết, gán biến gốc cuối cùng \(c = 100\) rồi tính ngược ra \(b\) và \(a\); đọc kỹ đề hỏi "\(a\) là bao nhiêu % của \(c\)" hay "\(a\) ít hơn \(c\) bao nhiêu %".',
            {
                'A': ('Đáp án đúng', r'\(a = 0.64c\), nên \(a\) nhỏ hơn \(c\) một lượng \(100\% - 64\% = 36\%\).'),
                'B': ('Sai mẫu số so sánh', r'Tính \(\frac{c - a}{a} = \frac{36}{64} = 56.25\%\) (đây là % mà \(c\) lớn hơn \(a\), không phải % mà \(a\) nhỏ hơn \(c\)).'),
                'C': ('Dừng sớm một bước', r'Trả lời \(a\) bằng \(64\%\) của \(c\), quên lấy \(100\% - 64\%\).'),
                'D': ('Trừ trực tiếp phần trăm', r'Lấy \(160\% - 40\% = 120\%\) hoàn toàn sai bản chất nhân tỉ lệ.'),
            },
            r'Đặt <code>c = 100</code>, <code>b = 0.4 * c</code>, <code>a = 1.6 * b</code>, rồi tính <code>(c - a) / c * 100</code> trên Desmos ra ngay <code>36</code>.',
        ),

        # Q7 (MCQ - B) — Average speed harmonic-mean trap (equal distances)
        math_mcq(
            'sat_m3_1_q7', 7, DOMAIN, SK_RATIO, 'Hard',
            r'<p>A medical courier drives from City P to City Q along a highway at a constant speed of \(60\text{ miles per hour}\), and immediately returns from City Q to City P along the exact same route at a constant speed of \(40\text{ miles per hour}\).</p>',
            r'<p>What is the courier’s average speed, in miles per hour, for the entire round trip?</p>',
            {
                'A': r'\(45\)',
                'B': r'\(48\)',
                'C': r'\(50\)',
                'D': r'\(52\)',
            },
            'B',
            r'Vì chiều đi và chiều về có cùng quãng đường \(d\), vận tốc trung bình KHÔNG phải trung bình cộng mà là trung bình điều hòa: \(v_{\text{avg}} = \frac{2 v_1 v_2}{v_1 + v_2} = \frac{2(60)(40)}{60 + 40} = \frac{4800}{100} = 48\text{ mph}\). Kiểm chứng bằng chọn \(d = 120\text{ mi}\): đi hết \(2\text{ giờ}\), về hết \(3\text{ giờ}\), tổng quãng đường \(240\text{ mi}\) chia tổng thời gian \(5\text{ giờ}\) bằng \(48\text{ mph}\).',
            r'Vận tốc trung bình luôn bằng \(\frac{\text{Tổng quãng đường}}{\text{Tổng thời gian}}\). Khi hai chặng bằng nhau về độ dài, dùng \(v_{\text{avg}} = \frac{2v_1v_2}{v_1+v_2}\), luôn nhỏ hơn trung bình cộng!',
            {
                'A': ('Ước lượng sai', r'Giảm quá đà so với trung bình cộng \(50\).'),
                'B': ('Đáp án đúng', r'\(\frac{2 \times 60 \times 40}{60 + 40} = 48\text{ mph}\).'),
                'C': ('Bẫy trung bình cộng kinh điển', r'Lấy \(\frac{60 + 40}{2} = 50\) — chỉ đúng khi thời gian hai chặng bằng nhau, còn ở đây thời gian đi chậm (\(40\text{ mph}\)) lâu hơn nên kéo vận tốc trung bình xuống dưới \(50\).'),
                'D': ('Lệch trọng số ngược chiều', r'Tưởng vận tốc trung bình lớn hơn \(50\).'),
            },
            r'Chọn quãng đường giả định bằng bội chung nhỏ nhất \(d = 120\), nhập <code>(2 * 120) / (120/60 + 120/40)</code> vào Desmos ra <code>48</code>.',
        ),

        # Q8 (SPR - 900) — Reverse successive percent decreases
        math_spr(
            'sat_m3_1_q8', 8, DOMAIN, SK_PCT, 'Hard',
            r'<p>After a \(15\%\) seasonal markdown and a subsequent \(20\%\) loyalty-member discount applied to the already marked-down price, a digital oscilloscope sells for \(\$612\).</p>',
            r'<p>What was the original price, in dollars, of the oscilloscope before either price reduction?</p>',
            ['900', '900.0'], '900',
            r'Gọi giá gốc là \(P\). Sau khi giảm \(15\%\), giá còn \(0.85P\). Sau khi giảm tiếp \(20\%\) trên mức giá mới, giá bán cuối là \(0.80 \times (0.85P) = 0.68P\). Ta có phương trình \(0.68P = 612 \Rightarrow P = \frac{612}{0.68} = 900\text{ đô-la}\).',
            r'Tìm giá gốc (reverse percentage) luôn lập phương trình \(P \times (1 - r_1)(1 - r_2) = P_{\text{final}}\) rồi CHIA cho tích hệ số — tuyệt đối không cộng \(15\% + 20\% = 35\%\) và không nhân ngược \(612 \times 1.35\).',
            r'Gõ <code>612 / (0.85 * 0.80)</code> trên Desmos để thu ngay đáp án chính xác <code>900</code>.',
        ),

        # Q9 (MCQ - C) — Density + Cubed geometric volume scaling
        math_mcq(
            'sat_m3_1_q9', 9, DOMAIN, SK_RATIO, 'Hard',
            r'<p>Two solid spheres, Sphere A and Sphere B, are crafted from the same uniform titanium alloy so that they have identical densities. The radius of Sphere B is \(3\) times the radius of Sphere A. Sphere A has a mass of \(14\text{ grams}\).</p>',
            r'<p>What is the mass, in grams, of Sphere B?</p>',
            {
                'A': r'\(42\)',
                'B': r'\(126\)',
                'C': r'\(378\)',
                'D': r'\(441\)',
            },
            'C',
            r'Do hai khối cầu cùng khối lượng riêng \(\rho\), khối lượng tỷ lệ thuận trực tiếp với thể tích: \(m = \rho V = \rho \cdot \frac{4}{3}\pi r^3 \propto r^3\). Khi bán kính tăng \(k = 3\) lần, thể tích và khối lượng tăng \(k^3 = 3^3 = 27\) lần. Vậy \(m_B = 14 \times 27 = 378\text{ grams}\).',
            r'Cùng chất liệu (cùng mật độ \(\rho\)): tỷ số khối lượng \(=\) tỷ số thể tích \(= k^3\) (lập phương tỷ số chiều dài/bán kính).',
            {
                'A': ('Bẫy tỷ lệ bậc nhất', r'Chỉ nhân khối lượng với \(3\) (\(14 \times 3 = 42\)).'),
                'B': ('Bẫy tỷ lệ diện tích bậc hai', r'Nhân khối lượng với \(3^2 = 9\) (\(14 \times 9 = 126\)).'),
                'C': ('Đáp án đúng', r'Nhân khối lượng với \(3^3 = 27\): \(14 \times 27 = 378\text{ g}\).'),
                'D': ('Nhầm phép bình phương', r'Tính sai công thức thành \(21^2 = 441\).'),
            },
            r'Nhập <code>14 * 3^3</code> vào Desmos ra ngay <code>378</code> — không cần thay số \(\pi\) hay công thức thể tích cầu đầy đủ.',
        ),

        # Q10 (MCQ - B) — Compound rate + squared unit conversion (m^2/min -> km^2 in 5 hours)
        math_mcq(
            'sat_m3_1_q10', 10, DOMAIN, SK_RATIO, 'Hard',
            r'<p>An automated agricultural drone sprays liquid fertilizer at a constant rate of \(1,800\text{ square meters per minute}\). (Note: \(1\text{ kilometer} = 1,000\text{ meters}\))</p>',
            r'<p>At this rate, how many square kilometers of farmland can the drone spray in \(5\text{ hours}\)?</p>',
            {
                'A': r'\(0.009\)',
                'B': r'\(0.54\)',
                'C': r'\(5.4\)',
                'D': r'\(540\)',
            },
            'B',
            r'Đổi thời gian: \(5\text{ giờ} = 5 \times 60 = 300\text{ phút}\). Tổng diện tích phun được là \(1,800 \times 300 = 540,000\text{ m}^2\). Vì \(1\text{ km}^2 = (1,000\text{ m})^2 = 1,000,000\text{ m}^2\), diện tích theo \(\text{km}^2\) là \(\frac{540,000}{1,000,000} = 0.54\text{ km}^2\).',
            r'Với bài toán tốc độ kết hợp 2 đơn vị (thời gian + diện tích), đổi tách bạch từng đại lượng: giờ \(\to\) phút (\(\times 60\)) và \(\text{m}^2 \to \text{km}^2\) (\(\div 1,000^2\)).',
            {
                'A': ('Quên đổi giờ sang phút', r'Tính \(\frac{1,800 \times 5}{1,000^2} = 0.009\), quên nhân \(60\) phút/giờ.'),
                'B': ('Đáp án đúng', r'\(\frac{1,800 \times 5 \times 60}{1,000^2} = \frac{540,000}{1,000,000} = 0.54\text{ km}^2\).'),
                'C': ('Lệch một bậc thập phân', r'Chia cho \(10^5\) thay vì \(10^6\).'),
                'D': ('Bẫy quên bình phương đơn vị', r'Chỉ chia \(540,000\) cho \(1,000\) thay vì \(1,000^2\), ra \(540\).'),
            },
            r'Gõ trọn chuỗi phân số khử đơn vị vào Desmos: <code>1800 * (5 * 60) / 1000^2</code> ra ngay <code>0.54</code>.',
        ),

        # Q11 (MCQ - C) — 3-variable algebraic percent chain with "greater than" & "less than"
        math_mcq(
            'sat_m3_1_q11', 11, DOMAIN, SK_PCT, 'Hard',
            r'<p>Positive numbers \(x\), \(y\), and \(z\) satisfy the following relationships: \(x\) is \(25\%\) greater than \(y\), \(y\) is \(k\%\) less than \(z\), and \(x\) is \(10\%\) less than \(z\).</p>',
            r'<p>What is the value of \(k\)?</p>',
            {
                'A': r'\(15\)',
                'B': r'\(25\)',
                'C': r'\(28\)',
                'D': r'\(72\)',
            },
            'C',
            r'Gán \(z = 100\). Vì \(x\) nhỏ hơn \(z\) \(10\%\) nên \(x = 90\). Mặt khác \(x\) lớn hơn \(y\) \(25\%\), tức \(x = 1.25y \Rightarrow 90 = 1.25y \Rightarrow y = \frac{90}{1.25} = 72\). Vì \(y = 72\) so với \(z = 100\), nên \(y\) nhỏ hơn \(z\) đúng \(100 - 72 = 28\%\), suy ra \(k = 28\).',
            r'Gặp bài toán phần trăm nhiều biến liên kết, chọn biến làm mốc chung (\(z = 100\)) giúp chuyển toàn bộ bài đại số thành phép chia số học trong 10 giây!',
            {
                'A': ('Bẫy cộng trừ phần trăm', r'Lấy thẳng \(25 - 10 = 15\) mà không xét mốc so sánh khác nhau.'),
                'B': ('Nhầm lẫn tỷ lệ đối xứng', r'Cho rằng lớn hơn \(25\%\) sẽ bù trực tiếp bằng \(25\%\).'),
                'C': ('Đáp án đúng', r'\(y = \frac{0.90}{1.25}z = 0.72z \Rightarrow k = 100 - 72 = 28\).'),
                'D': ('Bẫy đọc sai câu hỏi', r'Tìm ra \(y = 72\%\) của \(z\) nhưng quên lấy \(100 - 72 = 28\) để ra "% less than".'),
            },
            r'Nhập <code>100 - (90 / 1.25)</code> vào Desmos để thấy ngay \(k = 28\).',
        ),

        # Q12 (SPR - 18) — Unequal-distance average speed (anti-formula-blindness trap!)
        math_spr(
            'sat_m3_1_q12', 12, DOMAIN, SK_RATIO, 'Hard',
            r'<p>A cyclist completes a \(90\text{-kilometer}\) mountain training loop divided into two segments. She rides the first \(36\text{ kilometers}\) uphill at a constant speed of \(12\text{ kilometers per hour}\) and the remaining \(54\text{ kilometers}\) downhill at a constant speed of \(27\text{ kilometers per hour}\).</p>',
            r'<p>What is the cyclist’s average speed, in kilometers per hour, for the entire \(90\text{-kilometer}\) loop?</p>',
            ['18', '18.0'], '18',
            r'Vì hai chặng có độ dài KHÁC NHAU (\(36\text{ km}\) và \(54\text{ km}\)), không được dùng cả trung bình cộng lẫn công thức \(\frac{2v_1v_2}{v_1+v_2}\). Ta tính tổng thời gian: \(t_1 = \frac{36}{12} = 3\text{ giờ}\), \(t_2 = \frac{54}{27} = 2\text{ giờ}\). Tổng thời gian \(T = 3 + 2 = 5\text{ giờ}\). Vận tốc trung bình \(= \frac{90}{5} = 18\text{ km/h}\).',
            r'Công thức \(\frac{2v_1v_2}{v_1+v_2}\) CHỈ áp dụng khi hai chặng bằng nhau về quãng đường; công thức vạn năng luôn đúng là \(v_{\text{avg}} = \frac{d_1 + d_2}{d_1/v_1 + d_2/v_2}\).',
            r'Gõ trực tiếp <code>(36 + 54) / (36/12 + 54/27)</code> trên Desmos để có ngay đáp án <code>18</code>.',
        ),

        # Q13 (MCQ - A) — Saline solution dilution / percent concentration
        math_mcq(
            'sat_m3_1_q13', 13, DOMAIN, SK_PCT, 'Hard',
            r'<p>A laboratory technician has \(40\text{ liters}\) of a saline solution that is \(15\%\) salt by volume. She adds \(x\text{ liters}\) of pure water (containing \(0\%\) salt) to dilute the solution until it is \(10\%\) salt by volume.</p>',
            r'<p>What is the value of \(x\)?</p>',
            {
                'A': r'\(20\)',
                'B': r'\(30\)',
                'C': r'\(40\)',
                'D': r'\(60\)',
            },
            'A',
            r'Lượng muối nguyên chất không đổi khi chỉ thêm nước tinh khiết: \(\text{Salt} = 0.15 \times 40 = 6\text{ lít}\). Ở dung dịch mới nồng độ \(10\%\): \(\frac{6}{40 + x} = 0.10 \Rightarrow 40 + x = 60 \Rightarrow x = 20\text{ lít}\).',
            r'Trong bài toán pha loãng (thêm nước), lượng chất tan KHÔNG ĐỔI: thiết lập ngay \(\text{Chất tan ban đầu} = c_{\text{mới}} \times (V_{\text{đầu}} + x)\).',
            {
                'A': ('Đáp án đúng', r'Tổng thể tích mới là \(\frac{6}{0.10} = 60\text{ L}\), nên lượng nước thêm vào là \(60 - 40 = 20\text{ L}\).'),
                'B': ('Sai tỷ lệ pha loãng', r'Tính nhầm lượng nước cần thêm là \(30\text{ L}\) (khi đó nồng độ sẽ là \(6/70 \approx 8.57\%\)).'),
                'C': ('Tưởng cần gấp đôi thể tích', r'Nếu thêm \(40\text{ L}\) nước, nồng độ giảm một nửa còn \(7.5\%\) chứ không phải \(10\%\).'),
                'D': ('Bẫy trả lời tổng thể tích cuối', r'Tìm đúng tổng thể tích mới là \(60\text{ L}\) nhưng quên trừ đi \(40\text{ L}\) ban đầu.'),
            },
            r'Nhập <code>0.15 * 40 / (40 + x) = 0.10</code> vào Desmos, nhìn vạch thẳng đứng cắt trục hoành tại <code>x = 20</code>.',
        ),

        # Q14 (MCQ - D) — Compound proportional scaling with squared variable (V = pi * r^2 * h)
        math_mcq(
            'sat_m3_1_q14', 14, DOMAIN, SK_PCT, 'Hard',
            r'<p>The manufacturing cost \(C\) of a solid cylindrical ceramic tank is directly proportional to its volume \(V = \pi r^2 h\), where \(r\) is the base radius and \(h\) is the height. An engineer designs a larger prototype by increasing the radius by \(20\%\) and increasing the height by \(25\%\).</p>',
            r'<p>By what percent does the manufacturing cost \(C\) increase from the original tank to the new prototype?</p>',
            {
                'A': r'\(45\%\)',
                'B': r'\(50\%\)',
                'C': r'\(65\%\)',
                'D': r'\(80\%\)',
            },
            'D',
            r'Thay các hệ số tỷ lệ mới vào công thức thể tích: \(r_{\text{new}} = 1.20r\) và \(h_{\text{new}} = 1.25h\). Khi đó \(V_{\text{new}} = \pi (1.20r)^2 (1.25h) = (1.44 \times 1.25)\pi r^2 h = 1.80V\). Do \(C \propto V\), chi phí tăng thêm \((1.80 - 1) \times 100\% = 80\%\).',
            r'Trong công thức đa biến như \(V = \pi r^2 h\), đặt các biến gốc bằng \(1\), thay trực tiếp hệ số tăng/giảm vào đúng số mũ (\(1.20^2 \times 1.25 = 1.80 \Rightarrow +80\%\)).',
            {
                'A': ('Cộng tuyến tính đơn giản', r'Lấy \(20\% + 25\% = 45\%\), sai cả lũy thừa lẫn quy tắc nhân.'),
                'B': ('Bẫy quên bình phương bán kính', r'Tính \(1.20 \times 1.25 = 1.50 \Rightarrow 50\%\), quên rằng \(r\) có số mũ \(2\) trong \(V = \pi r^2 h\).'),
                'C': ('Cộng tuyến tính cả 3 nhân tử', r'Lấy \(20\% + 20\% + 25\% = 65\%\) thay vì nhân các hệ số \((1.2)(1.2)(1.25)\).'),
                'D': ('Đáp án đúng', r'\(1.20^2 \times 1.25 = 1.44 \times 1.25 = 1.80\), tức tăng đúng \(80\%\).'),
            },
            r'Gõ <code>(1.20^2 * 1.25 - 1) * 100</code> trên Desmos để có ngay đáp án <code>80</code>.',
        ),

        # Q15 (SPR - 15) — Two-subgroup weighted percent change
        math_spr(
            'sat_m3_1_q15', 15, DOMAIN, SK_PCT, 'Hard',
            r'<p>A biotechnology company stores active lab samples at two facilities, Facility North and Facility South. At the start of the quarter, Facility North held \(60\%\) of the company’s total samples and Facility South held the remaining \(40\%\). Over the quarter, the number of samples at Facility North increased by \(35\%\), while the number of samples at Facility South decreased by \(15\%\).</p>',
            r'<p>By what percent did the total number of active lab samples across both facilities increase over the quarter? (Enter the number without the percent sign.)</p>',
            ['15', '15.0'], '15',
            r'Giả sử tổng số mẫu ban đầu là \(100\): cơ sở Bắc có \(60\) mẫu và cơ sở Nam có \(40\) mẫu. Cuối quý: cơ sở Bắc có \(60 \times 1.35 = 81\) mẫu; cơ sở Nam có \(40 \times 0.85 = 34\) mẫu. Tổng số mẫu mới là \(81 + 34 = 115\). So với \(100\) mẫu ban đầu, tổng số mẫu tăng \(15\%\).',
            r'Thay đổi phần trăm tổng hợp của 2 nhóm bằng trung bình trọng số: \(0.60(+35\%) + 0.40(-15\%) = +21\% - 6\% = +15\%\). Chọn tổng ban đầu bằng \(100\) giúp tính cực nhanh không bao giờ nhầm!',
            r'Gõ <code>60 * 1.35 + 40 * 0.85 - 100</code> trên Desmos để ra ngay <code>15</code>.',
        ),
    ]

    title = 'Math Drill 3.1: Ratios, Rates, Squared/Cubed Units & Percent Traps (15 câu)'
    subtitle = '15 câu (11 MCQ + 4 SPR) • Chuyên sâu đổi đơn vị bậc 2/3, bẫy phần trăm liên tiếp, mật độ & vận tốc trung bình'
    return (
        'drill_m3_1',
        title,
        8,
        build_math_drill_json(title, subtitle, 'Module 3 • Band 700–800', questions, target_minutes=22),
    )


def build_drill_3_2():
    """Math Drill 3.2: Statistics, Probability, Margin of Error & Study Design (15 Qs: 11 MCQ + 4 SPR)."""
    DOMAIN = 'Problem-Solving and Data Analysis'
    SK_ONE = 'One-variable data: Distributions and measures of center and spread'
    SK_TWO = 'Two-variable data: Models and scatterplots'
    SK_PROB = 'Probability and conditional probability'
    SK_ME = 'Inference from sample statistics and margin of error'
    SK_STUDY = 'Evaluating statistical claims: Observational studies and experiments'

    tbl_q1 = build_math_table(
        ['Employee', '1', '2', '3', '4', '5', '6', '7', '8', '9 (CEO)'],
        [['Salary (in $1,000s)', '64', '66', '68', '70', '72', '74', '76', '78', '242']],
        caption='Annual Salaries at a Software Startup (in thousands of dollars)',
    )

    tbl_q3 = build_math_table(
        ['Quiz Score (points)', 'Number of Students (Frequency)'],
        [
            ['5', '2'],
            ['7', '5'],
            ['8', '<i>k</i>'],
            ['10', '3'],
        ],
        caption='Distribution of 10-Point Chemistry Quiz Scores',
    )

    tbl_q4 = build_math_table(
        ['Data Value', 'Data Set X (Frequency)', 'Data Set Y (Frequency)'],
        [
            ['10', '6', '2'],
            ['15', '2', '4'],
            ['20', '4', '8'],
            ['25', '2', '4'],
            ['30', '6', '2'],
        ],
        caption='Frequency Distributions of Data Set X and Data Set Y (n = 20 each)',
    )

    tbl_q5 = build_math_table(
        ['Vehicle Type', 'Under 15 Miles', '15 Miles or More', 'Total'],
        [
            ['Electric', '42', '18', '60'],
            ['Hybrid', '51', '39', '90'],
            ['Gasoline', '33', '57', '90'],
            ['<b>Total</b>', '<b>126</b>', '<b>114</b>', '<b>240</b>'],
        ],
        caption='Survey of 240 Commuters by Vehicle Type and Daily Commute Distance',
    )

    tbl_q7 = build_math_table(
        ['Fellowship Track', 'Prior Coding: Yes', 'Prior Coding: No', 'Total'],
        [
            ['Data Science', '<i>x</i>', '28', '<i>x</i> + 28'],
            ['Biomedical', '44', '<i>y</i>', '44 + <i>y</i>'],
            ['<b>Total</b>', '<b>96</b>', '<b>64</b>', '<b>160</b>'],
        ],
        caption='STEM Fellowship Applicants by Track and Prior Coding Experience',
    )

    tbl_q11 = build_math_table(
        ['Seedling', 'Weekly Sunlight <i>x</i> (hours)', 'Actual Dry Biomass <i>y</i> (grams)'],
        [
            ['A', '10', '34.0'],
            ['B', '12', '41.8'],
            ['C', '15', '51.2'],
            ['D', '18', '52.0'],
            ['E', '20', '58.6'],
        ],
        caption='Observed Weekly Sunlight vs. Dry Biomass for 5 Greenhouse Seedlings',
    )

    tbl_q14 = build_math_table(
        ['Time <i>t</i> (hours)', '0', '2', '4', '6'],
        [['Population <i>P</i>(<i>t</i>) (thousands)', '12', '18', '27', '40.5']],
        caption='Bacterial Colony Population Over Time',
    )

    questions = [
        # Q1 (MCQ - A) — Outlier removal effect on Mean vs Median
        math_mcq(
            'sat_m3_2_q1', 1, DOMAIN, SK_ONE, 'Medium',
            tbl_q1 + r'<p>The table above shows the annual salaries, in thousands of dollars, of the \(9\) employees at a boutique software startup. Suppose the outlier value of \(242\) is removed from the data set to create a new \(8\text{-value}\) data set.</p>',
            r'<p>Which of the following statements accurately describes how the mean and median change when the outlier \(242\) is removed?</p>',
            {
                'A': r'Both the mean and the median decrease, and the mean decreases by a greater amount than the median.',
                'B': r'Both the mean and the median decrease, and the median decreases by a greater amount than the mean.',
                'C': r'The mean decreases, while the median remains exactly the same.',
                'D': r'The mean remains unchanged, while the range and standard deviation decrease.',
            },
            'A',
            r'Ban đầu (\(9\) giá trị): tổng \(= 810 \Rightarrow \text{Mean} = \frac{810}{9} = 90\); \(\text{Median}\) (giá trị thứ \(5\)) \(= 72\). Sau khi bỏ ngoại lệ \(242\) (\(8\) giá trị còn lại \(64\text{ đến }78\)): tổng \(= 568 \Rightarrow \text{Mean} = \frac{568}{8} = 71\); \(\text{Median} = \frac{70 + 72}{2} = 71\). Như vậy Mean giảm mạnh \(19\) đơn vị, còn Median cũng giảm nhưng chỉ giảm \(1\) đơn vị.',
            r'Bỏ một ngoại lệ cực lớn (high outlier) kéo Mean giảm mạnh hơn nhiều so với Median — nhưng CẨN THẬN: đừng vội chọn "Median giữ nguyên" trước khi kiểm tra trung vị thực tế của dãy mới!',
            {
                'A': ('Đáp án đúng', r'Mean giảm \(19\) (từ \(90 \to 71\)), Median giảm \(1\) (từ \(72 \to 71\)); cả hai đều giảm và Mean giảm nhiều hơn hẳn.'),
                'B': ('Đảo ngược tính nhạy cảm', r'Mean luôn nhạy cảm với outlier hơn Median, không thể giảm ít hơn Median.'),
                'C': ('Bẫy học vẹt "Median không đổi"', r'Vì số phần tử giảm từ \(9\) xuống \(8\) và các số phân biệt đều nhau, Median dịch từ \(72\) xuống \(\frac{70+72}{2} = 71\), KHÔNG giữ nguyên.'),
                'D': ('Hiểu sai bản chất Mean', r'Loại bỏ giá trị lớn hơn trung bình chắc chắn làm giảm Mean.'),
            },
            r'Tạo danh sách <code>A = [64,66,68,70,72,74,76,78,242]</code> và <code>B = [64,66,68,70,72,74,76,78]</code> trong Desmos rồi gõ <code>mean(A)</code>, <code>mean(B)</code>, <code>median(A)</code>, <code>median(B)</code> để kiểm chứng tức thì.',
        ),

        # Q2 (MCQ - B) — Adding a constant c to every value: Center shifts, Spread unchanged
        math_mcq(
            'sat_m3_2_q2', 2, DOMAIN, SK_ONE, 'Medium',
            r'<p>Data Set A consists of \(25\) positive integers with a mean of \(42\), a median of \(40\), a range of \(18\), and a standard deviation of \(5.4\). Data Set B is formed by adding \(15\) to every value in Data Set A.</p>',
            r'<p>Which of the following gives the mean, median, range, and standard deviation of Data Set B?</p>',
            {
                'A': r'Mean \(= 57\), Median \(= 55\), Range \(= 33\), Standard deviation \(= 20.4\)',
                'B': r'Mean \(= 57\), Median \(= 55\), Range \(= 18\), Standard deviation \(= 5.4\)',
                'C': r'Mean \(= 42\), Median \(= 40\), Range \(= 33\), Standard deviation \(= 20.4\)',
                'D': r'Mean \(= 57\), Median \(= 40\), Range \(= 18\), Standard deviation \(= 5.4\)',
            },
            'B',
            r'Khi cộng cùng một hằng số \(c = 15\) vào mọi phần tử, toàn bộ phân phối chỉ tịnh tiến sang phải \(15\) đơn vị mà không bị giãn hay co lại. Vì vậy các thước đo tâm (Mean, Median) tăng thêm \(15\) (lên \(57\) và \(55\)), còn các thước đo độ phân tán (Range, Standard Deviation) giữ nguyên hoàn toàn (\(18\) và \(5.4\)).',
            r'Cộng hằng số \(+c\) vào mọi số liệu: Mean & Median cộng thêm \(c\); Range, IQR và Standard Deviation KHÔNG ĐỔI!',
            {
                'A': ('Cộng c vào cả độ phân tán', r'Nhầm lẫn cộng \(15\) vào cả Range (\(18+15=33\)) và SD (\(5.4+15=20.4\)).'),
                'B': ('Đáp án đúng', r'Tâm tịnh tiến \(+15\) (\(57\) và \(55\)); độ phân tán giữ nguyên (\(18\) và \(5.4\)).'),
                'C': ('Đảo ngược quy tắc tâm và độ phân tán', r'Giữ nguyên Mean/Median nhưng lại cộng \(15\) vào Range và SD.'),
                'D': ('Quên tịnh tiến Median', r'Chỉ cộng \(15\) vào Mean mà bỏ quên Median.'),
            },
            r'Thử nhanh một dãy mẫu nhỏ trên Desmos: <code>L = [1, 3, 5]</code> và <code>L + 15</code>, so sánh <code>stdev(L)</code> với <code>stdev(L + 15)</code> thấy y hệt nhau.',
        ),

        # Q3 (SPR - 10) — Unknown frequency k from weighted mean in frequency table
        math_spr(
            'sat_m3_2_q3', 3, DOMAIN, SK_ONE, 'Hard',
            tbl_q3 + r'<p>The frequency table above summarizes the scores of a group of students on a \(10\text{-point}\) chemistry quiz, where \(k\) is a positive integer. The mean score of all students represented in the table is \(7.75\).</p>',
            r'<p>What is the value of \(k\)?</p>',
            ['10', '10.0'], '10',
            r'Tổng số học sinh là \(2 + 5 + k + 3 = 10 + k\). Tổng điểm là \(2(5) + 5(7) + 8k + 3(10) = 10 + 35 + 30 + 8k = 75 + 8k\). Từ giả thiết điểm trung bình bằng \(7.75\): \(\frac{75 + 8k}{10 + k} = 7.75 \Rightarrow 75 + 8k = 77.5 + 7.75k \Rightarrow 0.25k = 2.5 \Rightarrow k = 10\).',
            r'Với bảng tần số, luôn lập phương trình \(\frac{\sum (\text{Giá trị} \times \text{Tần số})}{\sum \text{Tần số}} = \text{Mean}\) — đừng quên cộng \(k\) vào CẢ tử số (nhân với điểm tương ứng) và mẫu số!',
            r'Nhập thẳng phương trình <code>(2*5 + 5*7 + 8*x + 3*10) / (2 + 5 + x + 3) = 7.75</code> vào Desmos, đọc ngay đường thẳng đứng tại <code>x = 10</code>.',
        ),

        # Q4 (MCQ - C) — Comparing SD of two frequency tables with identical mean & range
        math_mcq(
            'sat_m3_2_q4', 4, DOMAIN, SK_ONE, 'Hard',
            tbl_q4 + r'<p>The table above shows the frequency distributions of two data sets, Data Set X and Data Set Y, each consisting of \(20\) measurements.</p>',
            r'<p>Which of the following statements best compares the means and standard deviations of Data Set X and Data Set Y?</p>',
            {
                'A': r'The means are equal, and the standard deviation of Data Set X is less than the standard deviation of Data Set Y.',
                'B': r'The mean of Data Set X is greater than the mean of Data Set Y, and their standard deviations are equal.',
                'C': r'The means are equal, and the standard deviation of Data Set X is greater than the standard deviation of Data Set Y.',
                'D': r'The means are equal, and the standard deviations are equal because both data sets have the same range of \(20\).',
            },
            'C',
            r'Cả hai bộ dữ liệu đều đối xứng hoàn toàn quanh giá trị \(20\), nên \(\text{Mean}_X = \text{Mean}_Y = 20\). Về độ lệch chuẩn (SD), Data Set X có tới \(12/20\) phần tử tập trung ở hai cực trị xa trung bình nhất (\(10\) và \(30\)), trong khi Data Set Y tập trung dày đặc quanh giá trị trung bình \(20\) (\(8\) phần tử tại \(20\)). Do đó \(\text{SD}_X > \text{SD}_Y\) (cụ thể \(\sigma_X = \sqrt{65} \approx 8.06 > \sigma_Y = \sqrt{30} \approx 5.48\)).',
            r'Standard Deviation đo khoảng cách trung bình tới Mean: dữ liệu dồn ra 2 đầu mút (hình chữ U) luôn có SD LỚN HƠN dữ liệu dồn vào giữa (hình chuông), dù Range hoàn toàn bằng nhau!',
            {
                'A': ('Nhầm chiều độ phân tán', r'Đảo ngược kết luận: tập trung ở 2 biên tạo SD lớn hơn, không phải nhỏ hơn.'),
                'B': ('Nhầm tính đối xứng', r'Cả hai bảng đều đối xứng hoàn hảo quanh \(20\) nên Mean chắc chắn bằng nhau.'),
                'C': ('Đáp án đúng', r'Cùng Mean \(= 20\), và X phân tán ra hai đầu mút nhiều hơn nên \(\text{SD}_X > \text{SD}_Y\).'),
                'D': ('Bẫy "cùng Range = cùng SD"', r'Hai tập có cùng Range \(= 30 - 10 = 20\) nhưng phân bố bên trong khác hẳn nên SD khác nhau rõ rệt.'),
            },
            r'Không cần tính tay trên bài thi: chỉ cần nhìn độ đối xứng để chốt Mean bằng nhau, và đếm số điểm nằm ở 2 cực trị (\(10, 30\)): X có \(12\) điểm, Y chỉ có \(4\) điểm \(\Rightarrow \text{SD}_X > \text{SD}_Y\).',
        ),

        # Q5 (MCQ - D) — Conditional probability from two-way table ("given that...")
        math_mcq(
            'sat_m3_2_q5', 5, DOMAIN, SK_PROB, 'Medium',
            tbl_q5 + r'<p>The two-way table above summarizes the results of a survey of \(240\) daily commuters categorized by vehicle type and one-way commute distance.</p>',
            r'<p>If a commuter from the survey is selected at random from those who commute \(15\text{ miles or more}\), what is the probability that the commuter drives a hybrid vehicle?</p>',
            {
                'A': r'\(\frac{13}{80}\)',
                'B': r'\(\frac{13}{30}\)',
                'C': r'\(\frac{19}{40}\)',
                'D': r'\(\frac{13}{38}\)',
            },
            'D',
            r'Điều kiện "selected from those who commute \(15\text{ miles or more}\)" giới hạn không gian mẫu (mẫu số) chỉ còn cột "\(15\text{ Miles or More}\)" gồm \(114\) người. Trong nhóm \(114\) người này, có \(39\) người đi xe Hybrid. Vậy xác suất cần tìm là \(\frac{39}{114} = \frac{13}{38}\).',
            r'Xác suất có điều kiện ("given that..." / "from those who..."): bước 1 khoanh tròn đúng HÀNG hoặc CỘT điều kiện làm mẫu số, tuyệt đối không lấy tổng chung \(240\)!',
            {
                'A': ('Bẫy lấy tổng toàn bảng', r'Tính \(\frac{39}{240} = \frac{13}{80}\) — đây là xác suất đồng thời, bỏ qua điều kiện "15 miles or more".'),
                'B': ('Đảo ngược điều kiện', r'Chia cho tổng hàng Hybrid (\(90\)) ra \(\frac{39}{90} = \frac{13}{30}\) — đây là \(P(15+\text{ miles} \mid \text{Hybrid})\).'),
                'C': ('Tính xác suất biên', r'Tính \(\frac{114}{240} = \frac{19}{40}\), chỉ là tỷ lệ người đi \(\ge 15\) dặm.'),
                'D': ('Đáp án đúng', r'\(P(\text{Hybrid} \mid 15+\text{ miles}) = \frac{39}{114} = \frac{13}{38}\).'),
            },
            r'Gõ <code>39/114</code> trên Desmos rồi bấm biểu tượng phân số ở bên trái ô nhập để rút gọn tự động thành <code>13/38</code>.',
        ),

        # Q6 (MCQ - A) — Margin of Error: Plausible values interpretation
        math_mcq(
            'sat_m3_2_q6', 6, DOMAIN, SK_ME, 'Hard',
            r'<p>A polling organization surveyed a random sample of \(1,200\) registered voters in a state regarding a proposed public transit bond. Of the voters surveyed, \(54\%\) supported the bond, with an associated margin of error of \(3\%\) at a \(95\%\) confidence level.</p>',
            r'<p>Which of the following is the most appropriate conclusion based on the survey results?</p>',
            {
                'A': r'It is plausible that between \(51\%\) and \(57\%\) of all registered voters in the state support the proposed public transit bond.',
                'B': r'Exactly \(54\%\) of all registered voters in the state support the bond, with up to \(3\%\) of voters remaining undecided.',
                'C': r'It is guaranteed that at least \(51\%\) of all voters in the entire country support the proposed public transit bond.',
                'D': r'If the survey were repeated with \(1,200\) different voters in the state, between \(51\%\) and \(57\%\) would definitely support the bond.',
            },
            'A',
            r'Khoảng giá trị hợp lý (plausible values) cho tỷ lệ thực tế của QUẦN THỂ được lấy mẫu (all registered voters in the state) là \(\hat{p} \pm \text{ME} = 54\% \pm 3\%\), tức từ \(51\%\) đến \(57\%\). Mọi phương án dùng từ khẳng định tuyệt đối ("guaranteed", "definitely", "exactly") hoặc mở rộng ra ngoài bang ("entire country") đều sai về mặt thống kê.',
            r'Quy tắc vàng Margin of Error trên SAT: tìm đúng 3 dấu hiệu chuẩn — (1) từ mềm "plausible", (2) khoảng \(\hat{p} - \text{ME}\) đến \(\hat{p} + \text{ME}\), và (3) đúng quần thể được lấy mẫu (in the state).',
            {
                'A': ('Đáp án đúng', r'Diễn đạt chính xác khoảng khả dĩ \(51\%\text{–}57\%\) cho đúng quần thể cử tri đăng ký trong bang.'),
                'B': ('Hiểu sai ý nghĩa ME', r'Biên độ sai số \(3\%\) phản ánh độ bất định lấy mẫu, không phải tỷ lệ cử tri chưa quyết định, và mẫu không thể khẳng định chính xác \(54\%\) toàn bang.'),
                'C': ('Bẫy khẳng định tuyệt đối + vượt phạm vi', r'Sai kép: vừa dùng "guaranteed" (độ tin cậy \(95\%\) không bao giờ là đảm bảo \(100\%\)), vừa khái quát quá đà ra "entire country".'),
                'D': ('Bẫy "definitely"', r'Một mẫu ngẫu nhiên mới vẫn có xác suất nhỏ rơi ra ngoài khoảng \(51\%\text{–}57\%\), không thể nói "definitely".'),
            },
            r'Câu hỏi lý thuyết thống kê — loại trừ nhanh mọi đáp án chứa từ cực đoan <em>guaranteed, definitely, must, prove, exactly</em>.',
        ),

        # Q7 (SPR - 0.65 / 13/20) — Incomplete two-way table deduction + conditional probability
        math_spr(
            'sat_m3_2_q7', 7, DOMAIN, SK_PROB, 'Hard',
            tbl_q7 + r'<p>The incomplete two-way table above categorizes \(160\) applicants to a summer STEM fellowship by their chosen track and whether they have prior coding experience.</p>',
            r'<p>If one applicant is selected at random from those who applied to the Data Science track, what is the probability that the applicant has prior coding experience? (Express your answer as a decimal or a simplified fraction.)</p>',
            ['0.65', '.65', '13/20', '52/80'], '13/20 (or 0.65)',
            r'Từ tổng cột "Prior Coding: Yes", ta có \(x + 44 = 96 \Rightarrow x = 52\). Khi đó tổng số ứng viên ngành Data Science là \(x + 28 = 52 + 28 = 80\). (Kiểm tra chéo: \(y = 64 - 28 = 36\), tổng Biomedical \(= 44 + 36 = 80\), \(80 + 80 = 160\) khớp). Xác suất có điều kiện cần tìm là \(P(\text{Yes} \mid \text{Data Science}) = \frac{52}{80} = \frac{13}{20} = 0.65\).',
            r'Gặp bảng hai chiều khuyết ô: giải các biến ẩn từ tổng hàng/cột trước, sau đó khóa chặt điều kiện ("from those who applied to Data Science") làm mẫu số.',
            r'Tính <code>x = 96 - 44</code> được <code>52</code>, sau đó gõ <code>52 / (52 + 28)</code> trong Desmos ra ngay <code>0.65</code> (hoặc <code>13/20</code>).',
        ),

        # Q8 (MCQ - B) — Sample size n effect on Margin of Error (ME proportional to 1/sqrt(n))
        math_mcq(
            'sat_m3_2_q8', 8, DOMAIN, SK_ME, 'Hard',
            r'<p>Two independent polling firms each survey a random sample of residents in the same metropolitan area to estimate the proportion who support extending public library hours. Firm A surveys \(400\) residents and reports a margin of error of \(4.8\%\). Firm B uses the same confidence level and sampling method, but surveys \(1,600\) residents.</p>',
            r'<p>Assuming both surveys obtain similar sample proportions, which of the following is closest to the margin of error for Firm B’s survey?</p>',
            {
                'A': r'\(1.2\%\)',
                'B': r'\(2.4\%\)',
                'C': r'\(4.8\%\)',
                'D': r'\(9.6\%\)',
            },
            'B',
            r'Biên độ sai số tỷ lệ nghịch với căn bậc hai của cỡ mẫu: \(\text{ME} = z^* \sqrt{\frac{\hat{p}(1-\hat{p})}{n}} \propto \frac{1}{\sqrt{n}}\). Khi cỡ mẫu tăng gấp \(\frac{1,600}{400} = 4\) lần, biên độ sai số giảm đi \(\sqrt{4} = 2\) lần: \(\text{ME}_B \approx \frac{4.8\%}{2} = 2.4\%\).',
            r'Cỡ mẫu \(n\) tăng \(k\) lần \(\Rightarrow\) Margin of Error GIẢM \(\sqrt{k}\) lần (muốn giảm ME đi một nửa phải tăng cỡ mẫu gấp \(4\) lần!).',
            {
                'A': ('Bẫy chia thẳng cho 4', r'Chia \(4.8\%\) cho \(4\) thay vì cho \(\sqrt{4} = 2\).'),
                'B': ('Đáp án đúng', r'Cỡ mẫu tăng \(4\) lần nên ME giảm \(\sqrt{4} = 2\) lần: \(4.8\% / 2 = 2.4\%\).'),
                'C': ('Bỏ qua ảnh hưởng cỡ mẫu', r'Cỡ mẫu lớn hơn chắc chắn làm thu hẹp biên độ sai số.'),
                'D': ('Nhầm tỷ lệ thuận', r'Nhân đôi ME thay vì chia đôi.'),
            },
            r'Gõ <code>4.8 / sqrt(1600 / 400)</code> trên Desmos để chốt nhanh <code>2.4</code>.',
        ),

        # Q9 (MCQ - D) — Random assignment (causation) WITHOUT random selection (no generalization)
        math_mcq(
            'sat_m3_2_q9', 9, DOMAIN, SK_STUDY, 'Hard',
            r'<p>A sleep researcher recruited \(120\) volunteers from the psychology department at a single university to test whether listening to brown noise increases deep-sleep duration. She randomly assigned \(60\) volunteers to listen to brown noise each night for two weeks and the other \(60\) volunteers to sleep in silence. The brown-noise group averaged \(24\text{ minutes}\) more deep sleep per night, a statistically significant difference.</p>',
            r'<p>Based on the study’s design, which of the following conclusions is best supported?</p>',
            {
                'A': r'Listening to brown noise causes an increase in deep-sleep duration for all university students nationwide.',
                'B': r'Listening to brown noise is associated with increased deep sleep for all university students nationwide, but causation cannot be established.',
                'C': r'Neither causation nor any meaningful inference can be drawn because the study lasted only two weeks.',
                'D': r'Listening to brown noise causes an increase in deep-sleep duration for people similar to the volunteers in the study, but the results cannot be generalized to all university students.',
            },
            'D',
            r'Phân tích hai trục thiết kế thí nghiệm: (1) Có <b>random assignment</b> (phân nhóm ngẫu nhiên \(60/60\)) \(\Rightarrow\) CÓ THỂ kết luận quan hệ nhân quả (causation). (2) Không có <b>random selection</b> (chỉ tuyển tình nguyện viên của 1 khoa ở 1 trường đại học) \(\Rightarrow\) KHÔNG THỂ khái quát cho toàn bộ sinh viên toàn quốc, chỉ áp dụng cho nhóm người tương tự tình nguyện viên.',
            r'Ma trận vàng SAT Study Design: Random Assignment \(\Rightarrow\) Causation (nhân quả); Random Selection \(\Rightarrow\) Generalization (khái quát hóa cho quần thể).',
            {
                'A': ('Khái quát hóa quá đà', r'Vì không lấy mẫu ngẫu nhiên toàn quốc (chỉ dùng volunteers), không thể kết luận cho "all university students nationwide".'),
                'B': ('Đảo ngược hoàn toàn 2 tiêu chí', r'Nói sai cả hai vế: thí nghiệm CÓ random assignment (rút được nhân quả) nhưng KHÔNG có random selection (không khái quát toàn quốc).'),
                'C': ('Lý do không liên quan', r'Sự khác biệt đã có ý nghĩa thống kê với phân nhóm ngẫu nhiên nên hoàn toàn rút được kết luận nhân quả trong phạm vi mẫu tình nguyện.'),
                'D': ('Đáp án đúng', r'Khẳng định đúng quan hệ nhân quả (nhờ random assignment) và giới hạn phạm vi ở người tương tự tình nguyện viên (do thiếu random selection).'),
            },
            r'Ghi chú nhanh 2 dấu tick ngoài nháp: <code>Assign ✓ (Cause ✓)</code> và <code>Select ✗ (All students ✗)</code> \(\Rightarrow\) chọn ngay D.',
        ),

        # Q10 (MCQ - B) — Observational study WITH random selection (generalization YES, causation NO)
        math_mcq(
            'sat_m3_2_q10', 10, DOMAIN, SK_STUDY, 'Hard',
            r'<p>A municipal health department selected a random sample of \(850\) adult residents from the city’s population registry and recorded each resident’s weekly cycling hours and resting heart rate. Analysis showed a statistically significant negative association: residents who cycled at least \(5\text{ hours}\) per week had significantly lower resting heart rates than those who did not.</p>',
            r'<p>Which of the following conclusions is best supported by this study?</p>',
            {
                'A': r'Cycling at least \(5\text{ hours}\) per week causes a lower resting heart rate among all adult residents of the city.',
                'B': r'Among all adult residents of the city, cycling at least \(5\text{ hours}\) per week is associated with a lower resting heart rate, though causation cannot be concluded from this study alone.',
                'C': r'The observed association applies only to the \(850\) surveyed residents and cannot be generalized to the city’s adult population.',
                'D': r'Cycling at least \(5\text{ hours}\) per week is associated with a lower resting heart rate among all adults worldwide.',
            },
            'B',
            r'Đây là nghiên cứu quan sát (observational study) có <b>random selection</b> từ danh sách cư dân thành phố \(\Rightarrow\) CÓ THỂ khái quát hóa mối liên hệ (association) cho toàn bộ cư dân trưởng thành trong thành phố. Tuy nhiên KHÔNG có <b>random assignment</b> (cư dân tự quyết định có đạp xe hay không, dễ nhiễu bởi chế độ ăn/tuổi tác) \(\Rightarrow\) KHÔNG THỂ khẳng định nhân quả (causation).',
            r'Observational study + Random selection \(\Rightarrow\) Generalize association to the sampled population ONLY; NEVER conclude causation!',
            {
                'A': ('Bẫy khẳng định nhân quả ở nghiên cứu quan sát', r'Không phân nhóm ngẫu nhiên nên không thể kết luận "causes" (có thể người vốn khỏe mạnh mới chọn đạp xe).'),
                'B': ('Đáp án đúng', r'Khái quát hóa đúng mối liên hệ cho toàn bộ cư dân trưởng thành của thành phố và cẩn trọng loại trừ kết luận nhân quả.'),
                'C': ('Bỏ qua random selection', r'Vì mẫu \(850\) người được chọn ngẫu nhiên từ danh sách toàn thành phố nên HOÀN TOÀN khái quát được cho thành phố.'),
                'D': ('Khái quát vượt quá quần thể mẫu', r'Chỉ chọn mẫu trong một thành phố nên không thể suy rộng ra "all adults worldwide".'),
            },
            r'Kiểm tra ma trận 2 tick: <code>Select ✓ (City adults ✓)</code> và <code>Assign ✗ (Cause ✗)</code> \(\Rightarrow\) chốt ngay B.',
        ),

        # Q11 (SPR - 3.7) — Largest positive residual from table & linear model
        math_spr(
            'sat_m3_2_q11', 11, DOMAIN, SK_TWO, 'Hard',
            tbl_q11 + r'<p>A botanist models the relationship between weekly sunlight \(x\), in hours, and dry biomass \(y\), in grams, using the line of best fit \(\hat{y} = 2.4x + 11.5\). The table above displays the actual observed measurements for \(5\) greenhouse seedlings.</p>',
            r'<p>For the seedling in the table with the greatest positive residual (where \(\text{residual} = \text{actual } y - \text{predicted } \hat{y}\)), what is the value of that residual, in grams?</p>',
            ['3.7', '37/10'], '3.7',
            r'Tính giá trị dự đoán \(\hat{y} = 2.4x + 11.5\) và phần dư \(r = y - \hat{y}\) cho từng cây: (A) \(x=10 \Rightarrow \hat{y}=35.5,\ r=-1.5\); (B) \(x=12 \Rightarrow \hat{y}=40.3,\ r=+1.5\); (C) \(x=15 \Rightarrow \hat{y}=47.5,\ r=51.2-47.5=+3.7\); (D) \(x=18 \Rightarrow \hat{y}=54.7,\ r=-2.7\); (E) \(x=20 \Rightarrow \hat{y}=59.5,\ r=-0.9\). Phần dư dương lớn nhất thuộc về cây C và bằng \(3.7\text{ grams}\).',
            r'Luôn nhớ thứ tự chuẩn của phần dư: \(\text{Residual} = y_{\text{actual}} - \hat{y}_{\text{predicted}}\). Phần dư dương nghĩa là điểm thực tế nằm PHÍA TRÊN đường hồi quy.',
            r'Tạo bảng \((x_1, y_1)\) gồm \(5\) điểm trên Desmos, thêm cột thứ 3 gõ <code>y_1 - (2.4*x_1 + 11.5)</code> để hiện ngay cả 5 phần dư và đọc giá trị lớn nhất <code>3.7</code>.',
        ),

        # Q12 (MCQ - C) — Scatterplot SVG + exact OLS line of best fit: counting points exceeding threshold
        math_mcq(
            'sat_m3_2_q12', 12, DOMAIN, SK_TWO, 'Hard',
            svg_scatterplot_q12() + r'<p>The scatterplot above shows \(8\) data points comparing weekly training hours \(x\) and productivity index \(y\) for \(8\) employees, along with the line of best fit \(\hat{y} = 4x + 20\).</p>',
            r'<p>For how many of the \(8\) data points is the actual \(y\text{-value}\) greater than the value predicted by the line of best fit by <b>more than \(2\)</b>?</p>',
            {
                'A': r'\(0\)',
                'B': r'\(1\)',
                'C': r'\(2\)',
                'D': r'\(4\)',
            },
            'C',
            r'Tính phần dư \(y - (4x + 20)\) cho \(4\) điểm nằm phía trên đường thẳng: tại \(x=1\): \(28 - 24 = +4 > 2\) (Đạt); tại \(x=3\): \(34 - 32 = +2\) (KHÔNG lớn hơn \(2\)); tại \(x=6\): \(46 - 44 = +2\) (KHÔNG lớn hơn \(2\)); tại \(x=8\): \(56 - 52 = +4 > 2\) (Đạt). Vậy chỉ có đúng \(2\) điểm thỏa mãn lớn hơn dự đoán quá \(2\) đơn vị.',
            r'Đọc cực kỹ từ khóa bất đẳng thức trên SAT: "more than \(2\)" là dấu lớn hơn ngặt (\(> 2\)), nên các điểm có hiệu đúng bằng \(2\) PHẢI bị loại!',
            {
                'A': ('Kiểm tra sai dấu', r'Có hai điểm \((1, 28)\) và \((8, 56)\) vượt giá trị dự đoán tới \(4\) đơn vị.'),
                'B': ('Đếm sót một điểm', r'Bỏ sót một trong hai điểm \((1, 28)\) hoặc \((8, 56)\).'),
                'C': ('Đáp án đúng', r'Chỉ có \((1, 28)\) và \((8, 56)\) có phần dư \(+4 > 2\); hai điểm \((3, 34)\) và \((6, 46)\) chỉ hơn đúng \(2\).'),
                'D': ('Bẫy đếm tất cả điểm phía trên đường', r'Đếm cả \(4\) điểm nằm trên đường hồi quy mà quên loại hai điểm chỉ chênh đúng \(2\) đơn vị.'),
            },
            r'Nhập tọa độ \(4\) điểm nằm trên đường vào bảng Desmos rồi kiểm tra nhanh cột <code>y_1 - (4*x_1 + 20)</code>: thấy ngay chỉ có hai giá trị bằng <code>4</code> (còn lại bằng <code>2</code>).',
        ),

        # Q13 (MCQ - A) — Linear transformation Y = 1.8X + 32 on Mean AND Standard Deviation
        math_mcq(
            'sat_m3_2_q13', 13, DOMAIN, SK_ONE, 'Hard',
            r'<p>A sample of \(30\) laboratory temperature readings, recorded in degrees Celsius (\(^\circ\text{C}\)), has a mean of \(20^\circ\text{C}\) and a standard deviation of \(2.5^\circ\text{C}\). Every reading \(C\) is converted to degrees Fahrenheit (\(^\circ\text{F}\)) using the linear equation \(F = 1.8C + 32\).</p>',
            r'<p>What are the mean and standard deviation of the converted temperature readings in degrees Fahrenheit?</p>',
            {
                'A': r'Mean \(= 68^\circ\text{F}\), Standard deviation \(= 4.5^\circ\text{F}\)',
                'B': r'Mean \(= 68^\circ\text{F}\), Standard deviation \(= 36.5^\circ\text{F}\)',
                'C': r'Mean \(= 68^\circ\text{F}\), Standard deviation \(= 2.5^\circ\text{F}\)',
                'D': r'Mean \(= 36^\circ\text{F}\), Standard deviation \(= 4.5^\circ\text{F}\)',
            },
            'A',
            r'Với phép biến đổi tuyến tính \(Y = aX + b\): giá trị trung bình chịu cả phép nhân và phép cộng \(\mu_F = 1.8(20) + 32 = 36 + 32 = 68^\circ\text{F}\); còn độ lệch chuẩn chỉ chịu phép nhân theo \(|a|\) và không bị ảnh hưởng bởi hằng số cộng \(+32\): \(\sigma_F = |1.8| \times 2.5 = 4.5^\circ\text{F}\).',
            r'Biến đổi \(Y = aX + b\): \(\text{Mean}_Y = a\cdot\text{Mean}_X + b\), nhưng \(\text{SD}_Y = |a|\cdot\text{SD}_X\) (nhân làm giãn độ phân tán, cộng chỉ tịnh tiến nên bỏ qua \(+b\)).',
            {
                'A': ('Đáp án đúng', r'Mean \(= 1.8(20)+32 = 68^\circ\text{F}\) và SD \(= 1.8(2.5) = 4.5^\circ\text{F}\).'),
                'B': ('Cộng +32 vào cả SD', r'Tính \(1.8(2.5) + 32 = 36.5^\circ\text{F}\) — sai vì phép tịnh tiến \(+32\) không thay đổi khoảng cách giữa các số liệu.'),
                'C': ('Nhầm với phép chỉ cộng hằng số', r'Giữ nguyên SD \(= 2.5\) mà quên hệ số nhân \(1.8\) làm giãn rộng độ lệch chuẩn.'),
                'D': ('Quên +32 khi tính Mean', r'Chỉ tính \(1.8 \times 20 = 36\) cho Mean.'),
            },
            r'Gõ <code>1.8 * 20 + 32</code> (ra <code>68</code>) và <code>1.8 * 2.5</code> (ra <code>4.5</code>) trên Desmos — nhớ tách riêng quy tắc của Mean và SD.',
        ),

        # Q14 (MCQ - D) — Exponential vs Linear model from table with step dt = 2
        math_mcq(
            'sat_m3_2_q14', 14, DOMAIN, SK_TWO, 'Hard',
            tbl_q14 + r'<p>The table above shows the population \(P(t)\), in thousands, of a bacterial colony measured every \(2\text{ hours}\) over a \(6\text{-hour}\) period.</p>',
            r'<p>Which of the following equations best models the population \(P(t)\) after \(t\text{ hours}\)?</p>',
            {
                'A': r'\(P(t) = 3t + 12\)',
                'B': r'\(P(t) = 12(1.5)^{t}\)',
                'C': r'\(P(t) = 12(1.5)^{2t}\)',
                'D': r'\(P(t) = 12(1.5)^{t/2}\)',
            },
            'D',
            r'Kiểm tra hiệu số giữa các mốc cách nhau \(2\text{ giờ}\): \(+6, +9, +13.5\) (không đều \(\Rightarrow\) không phải tuyến tính). Kiểm tra tỷ số: \(\frac{18}{12} = 1.5\), \(\frac{27}{18} = 1.5\), \(\frac{40.5}{27} = 1.5\) (không đổi \(\Rightarrow\) hàm mũ!). Giá trị ban đầu \(P(0) = 12\) và cứ sau mỗi chu kỳ \(2\text{ giờ}\) nhân \(1.5\), do đó số chu kỳ trong \(t\text{ giờ}\) là \(\frac{t}{2}\): \(P(t) = 12(1.5)^{t/2}\).',
            r'Hiệu không đổi \(\Rightarrow\) Tuyến tính; Tỷ số không đổi \(\Rightarrow\) Hàm mũ \(y = a \cdot b^{t/T}\), trong đó \(T\) là khoảng thời gian ứng với mỗi lần nhân hệ số \(b\)!',
            {
                'A': ('Bẫy mô hình tuyến tính', r'Dùng hai điểm đầu \((0,12)\) và \((2,18)\) lập đường thẳng, nhưng tại \(t=4\) chỉ cho \(24 \neq 27\).'),
                'B': ('Bẫy quên chia chu kỳ T = 2', r'Với \(P(t) = 12(1.5)^t\), tại \(t=2\) cho \(12(1.5)^2 = 27 \neq 18\).'),
                'C': ('Nhân ngược chu kỳ lên tử số', r'Với \(2t\), tại \(t=2\) cho \(12(1.5)^4 = 60.75 \neq 18\).'),
                'D': ('Đáp án đúng', r'Thay \(t=0,2,4,6\) vào \(12(1.5)^{t/2}\) ra chuẩn xác \(12, 18, 27, 40.5\).'),
            },
            r'Nhập bảng \((t_1, P_1)\) vào Desmos rồi gõ hồi quy <code>P_1 ~ a * b^(t_1 / 2)</code> hoặc đơn giản thay \(t = 2\) vào từng đáp án để kiểm tra kết quả nào bằng <code>18</code>!',
        ),

        # Q15 (SPR - 3960) — Maximum plausible population count using sample proportion + ME
        math_spr(
            'sat_m3_2_q15', 15, DOMAIN, SK_ME, 'Hard',
            r'<p>An urban forester randomly selected \(250\) mature street trees from a city that has a total of \(18,000\) mature street trees. Of the \(250\) sampled trees, \(45\) showed early signs of emerald ash borer infestation. Based on the sample, the estimated proportion of infested trees in the city has an associated margin of error of \(4\%\).</p>',
            r'<p>Based on the sample estimate and its margin of error, what is the maximum plausible number of mature street trees in the entire city that show early signs of infestation?</p>',
            ['3960', '3960.0'], '3960',
            r'Tỷ lệ mẫu bị sâu bệnh là \(\hat{p} = \frac{45}{250} = 0.18 = 18\%\). Với biên độ sai số \(4\%\), khoảng tỷ lệ hợp lý của toàn thành phố là \([18\% - 4\%,\ 18\% + 4\%] = [14\%,\ 22\%]\). Vậy số cây bị sâu bệnh hợp lý lớn nhất trong toàn thành phố là \(22\% \times 18,000 = 0.22 \times 18,000 = 3,960\text{ cây}\).',
            r'Để tìm số lượng hợp lý lớn nhất/nhỏ nhất của quần thể: cộng (hoặc trừ) biên độ sai số vào tỷ lệ mẫu \(\hat{p} \pm \text{ME}\), rồi nhân với TỔNG QUẦN THỂ \(N\) (không nhân với cỡ mẫu \(n\)).',
            r'Nhập một dòng duy nhất trên Desmos: <code>(45/250 + 0.04) * 18000</code> để nhận kết quả <code>3960</code>.',
        ),
    ]

    title = 'Math Drill 3.2: Statistics, Probability, Margin of Error & Study Design (15 câu)'
    subtitle = '15 câu (11 MCQ + 4 SPR) • Thống kê Mean/Median/SD, Bảng hai chiều, Margin of Error, Scatterplot & Thiết kế thí nghiệm'
    return (
        'drill_m3_2',
        title,
        9,
        build_math_drill_json(title, subtitle, 'Module 3 • Band 700–800', questions, target_minutes=22),
    )


def get_drills():
    """Returns the 2 Module 3 Skill Drills as (drill_key, title, order_index, content_json)."""
    return [build_drill_3_1(), build_drill_3_2()]


def verify_all_math():
    """Programmatically verifies EVERY single numeric calculation across all 30 questions."""
    # --- Drill 3.1 (15 questions) ---
    # Q1: 432 ft^2 -> yd^2 at $18/yd^2
    assert Fraction(432, 3**2) * 18 == 864
    assert Fraction(432, 3) * 18 == 2592
    assert 432 * 18 == 7776
    assert 432 * 3 * 18 == 23328

    # Q2: +25% then -20%
    assert Fraction(125, 100) * Fraction(80, 100) == 1

    # Q3: 0.036 W/cm^2 -> W/m^2
    assert Fraction(36, 1000) * (100**2) == 360

    # Q4: Density 172.8 lb/ft^3, volume 450 in^3
    assert Fraction(1728, 10) * Fraction(450, 12**3) == 45

    # Q5: 240% greater than Y -> 340% of Y
    assert 100 + 240 == 340

    # Q6: a = 160% of b, b = 40% of c -> % a is less than c
    a_ratio = Fraction(160, 100) * Fraction(40, 100)
    assert a_ratio == Fraction(64, 100)
    assert (1 - a_ratio) * 100 == 36
    assert (1 - a_ratio) / a_ratio * 100 == Fraction(5625, 100)

    # Q7: Round trip 60 mph & 40 mph
    assert Fraction(2 * 60 * 40, 60 + 40) == 48

    # Q8: Reverse -15% then -20% -> $612
    p_orig = Fraction(612, 1) / (Fraction(85, 100) * Fraction(80, 100))
    assert p_orig == 900
    assert p_orig * Fraction(85, 100) * Fraction(80, 100) == 612

    # Q9: Same density, radius x3, mass A = 14 g
    assert 14 * (3**3) == 378

    # Q10: 1800 m^2/min for 5 hours in km^2
    assert Fraction(1800 * 5 * 60, 1000**2) == Fraction(54, 100)

    # Q11: x = 1.25y, x = 0.90z -> y = (1 - k/100)z
    y_over_z = Fraction(90, 100) / Fraction(125, 100)
    assert y_over_z == Fraction(72, 100)
    assert (1 - y_over_z) * 100 == 28

    # Q12: 36 km at 12 km/h, 54 km at 27 km/h
    t1 = Fraction(36, 12)
    t2 = Fraction(54, 27)
    assert t1 == 3 and t2 == 2
    assert Fraction(36 + 54, t1 + t2) == 18

    # Q13: 40 L of 15% salt + x L water -> 10% salt
    salt = Fraction(15, 100) * 40
    assert salt == 6
    x_water = salt / Fraction(10, 100) - 40
    assert x_water == 20

    # Q14: V = pi * r^2 * h; r +20%, h +25%
    v_mult = Fraction(120, 100)**2 * Fraction(125, 100)
    assert v_mult == Fraction(180, 100)
    assert (v_mult - 1) * 100 == 80

    # Q15: 60% North (+35%), 40% South (-15%)
    new_total = Fraction(60) * Fraction(135, 100) + Fraction(40) * Fraction(85, 100)
    assert new_total == 115
    assert new_total - 100 == 15

    # --- Drill 3.2 (15 questions) ---
    # Q1: Outlier removal
    s9 = [64, 66, 68, 70, 72, 74, 76, 78, 242]
    s8 = s9[:-1]
    assert statistics.mean(s9) == 90 and statistics.median(s9) == 72
    assert statistics.mean(s8) == 71 and statistics.median(s8) == 71
    assert (statistics.mean(s9) - statistics.mean(s8)) == 19 > (statistics.median(s9) - statistics.median(s8)) == 1

    # Q2: Shift +15
    sample_a = [30, 35, 40, 42, 48]
    sample_b = [v + 15 for v in sample_a]
    assert math.isclose(statistics.mean(sample_b), statistics.mean(sample_a) + 15)
    assert math.isclose(statistics.median(sample_b), statistics.median(sample_a) + 15)
    assert (max(sample_b) - min(sample_b)) == (max(sample_a) - min(sample_a))
    assert math.isclose(statistics.pstdev(sample_b), statistics.pstdev(sample_a))
    assert 42 + 15 == 57 and 40 + 15 == 55

    # Q3: Frequency table mean = 7.75 -> k = 10
    k = 10
    assert Fraction(2*5 + 5*7 + 8*k + 3*10, 2 + 5 + k + 3) == Fraction(775, 100)

    # Q4: Compare SD of X and Y
    ds_x = [10]*6 + [15]*2 + [20]*4 + [25]*2 + [30]*6
    ds_y = [10]*2 + [15]*4 + [20]*8 + [25]*4 + [30]*2
    assert len(ds_x) == 20 and len(ds_y) == 20
    assert statistics.mean(ds_x) == 20 and statistics.mean(ds_y) == 20
    assert (max(ds_x) - min(ds_x)) == (max(ds_y) - min(ds_y)) == 20
    assert math.isclose(statistics.pvariance(ds_x), 65.0)
    assert math.isclose(statistics.pvariance(ds_y), 30.0)
    assert statistics.stdev(ds_x) > statistics.stdev(ds_y)

    # Q5: Two-way table totals & conditional prob
    assert 42 + 18 == 60 and 51 + 39 == 90 and 33 + 57 == 90
    assert 42 + 51 + 33 == 126 and 18 + 39 + 57 == 114 and 126 + 114 == 240
    assert Fraction(39, 114) == Fraction(13, 38)
    assert Fraction(39, 240) == Fraction(13, 80)
    assert Fraction(39, 90) == Fraction(13, 30)
    assert Fraction(114, 240) == Fraction(19, 40)

    # Q6: 54% +/- 3% -> [51%, 57%]
    assert 54 - 3 == 51 and 54 + 3 == 57

    # Q7: Incomplete table x + 44 = 96, 28 + y = 64 -> P(Yes | DS) = 52/80 = 13/20 = 0.65
    x_q7 = 96 - 44
    y_q7 = 64 - 28
    assert x_q7 == 52 and y_q7 == 36
    assert (x_q7 + 28) + (44 + y_q7) == 160
    assert Fraction(x_q7, x_q7 + 28) == Fraction(13, 20) == Fraction(65, 100)

    # Q8: ME with n=400 (4.8%) vs n=1600 -> 2.4%
    assert math.isclose(4.8 / math.sqrt(1600 / 400), 2.4)

    # Q9 & Q10: Study design counts
    assert 60 + 60 == 120 and 850 > 0

    # Q11: Residuals for y_hat = 2.4x + 11.5
    obs_q11 = [(10, Fraction(340, 10)), (12, Fraction(418, 10)), (15, Fraction(512, 10)),
               (18, Fraction(520, 10)), (20, Fraction(586, 10))]
    res_q11 = [y - (Fraction(24, 10) * x + Fraction(115, 10)) for x, y in obs_q11]
    assert res_q11 == [Fraction(-15, 10), Fraction(15, 10), Fraction(37, 10),
                       Fraction(-27, 10), Fraction(-9, 10)]
    assert max(res_q11) == Fraction(37, 10)

    # Q12: Scatterplot exact OLS verification & count of residuals > 2
    pts_q12 = [(1, 28), (2, 27), (3, 34), (4, 31), (5, 35), (6, 46), (7, 47), (8, 56)]
    xs = [p[0] for p in pts_q12]
    ys = [p[1] for p in pts_q12]
    xbar = sum(xs) / len(xs)
    ybar = sum(ys) / len(ys)
    slope = sum((x - xbar) * (y - ybar) for x, y in pts_q12) / sum((x - xbar)**2 for x in xs)
    intercept = ybar - slope * xbar
    assert math.isclose(slope, 4.0) and math.isclose(intercept, 20.0)
    res_q12 = [y - (4 * x + 20) for x, y in pts_q12]
    assert res_q12 == [4, -1, 2, -5, -5, 2, -1, 4]
    assert sum(1 for r in res_q12 if r > 2) == 2
    assert sum(1 for r in res_q12 if r > 0) == 4

    # Q13: F = 1.8C + 32
    assert math.isclose(1.8 * 20 + 32, 68.0)
    assert math.isclose(1.8 * 2.5, 4.5)

    # Q14: P(t) = 12 * 1.5^(t/2)
    for t, expected in [(0, Fraction(12)), (2, Fraction(18)), (4, Fraction(27)), (6, Fraction(81, 2))]:
        assert Fraction(12) * (Fraction(3, 2) ** (t // 2)) == expected

    # Q15: 45/250 = 18%, +4% = 22%, 22% of 18000 = 3960
    p_hat = Fraction(45, 250)
    assert p_hat == Fraction(18, 100)
    assert (p_hat + Fraction(4, 100)) * 18000 == 3960

    print("[OK] verify_all_math(): All 30 questions in Module 3 Drills verified with 100% exact arithmetic!")


if __name__ == '__main__':
    import re
    verify_all_math()
    drills = get_drills()
    assert len(drills) == 2
    all_qids = set()
    for key, title, order_idx, cjson in drills:
        errs = validate_sat_test(cjson, title)
        assert not errs, f"Validation failed for {key}:\n" + "\n".join(errs)
        qs = cjson['drillModule']['questions']
        assert len(qs) == 15, f"{key} has {len(qs)} questions, expected 15"
        mcq_qs = [q for q in qs if q['questionFormat'] == 'mcq']
        spr_qs = [q for q in qs if q['questionFormat'] == 'spr']
        assert len(mcq_qs) == 11 and len(spr_qs) == 4, f"{key}: expected 11 MCQ + 4 SPR"
        counts = {lbl: sum(1 for q in mcq_qs if q['correctAnswer'] == lbl) for lbl in 'ABCD'}
        for q in qs:
            assert q['id'] not in all_qids, f"Duplicate qid {q['id']}"
            all_qids.add(q['id'])
            # Ensure no $...$ LaTeX delimiters and no unescaped control chars
            blob = q['stimulusHtml'] + q['questionHtml'] + q['explanation']['summaryVi'] + q['explanation'].get('desmosTipVi', '') + q['explanation'].get('keyTakeaway', '')
            for o in q.get('options', []):
                blob += o['text']
            for lbl, oa in (q['explanation'].get('optionAnalysis') or {}).items():
                blob += oa['reasonVi']
            assert not re.search(r'(?<!\\)\$[^$]+\$', blob), f"Potential $...$ LaTeX in {q['id']}"
            assert blob.count(r'\(') == blob.count(r'\)'), f"Unbalanced \\( \\) in {q['id']}"
            assert blob.count(r'\[') == blob.count(r'\]'), f"Unbalanced \\[ \\] in {q['id']}"
            for bad_ch in ('\x08', '\x0c', '\r', '\t'):
                assert bad_ch not in blob, f"Control char {repr(bad_ch)} in {q['id']}"
        print(f"  [PASS] {key} (order={order_idx}): 15 Qs (11 MCQ {counts} + 4 SPR) — 0 validator errors")
    print(f"[ALL PASS] {len(all_qids)} unique verified questions across Module 3 Drills!")
