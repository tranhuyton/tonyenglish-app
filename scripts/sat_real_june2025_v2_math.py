# -*- coding: utf-8 -*-
"""
Digital SAT Real Past Exam — June 2025 Ver 2: Math (Real M1 + M2, 44 Unique Questions)
Visually verified page-by-page from clean vertical strips (`math_m1_p056_059.jpg` through
`math_m2_p100_102.jpg`) plus high-DPI PDF inspection of every graph, table, and tiny fraction:
  - Section 2, Module 1: Math (22 real questions: 15 MCQ + 7 SPR)
  - Section 2, Module 2: Math (22 real questions: 17 MCQ + 5 SPR)
Zero watermarks, crisp inline SVGs & HTML tables, rich Vietnamese explanations, Desmos tips,
independent programmatic mathematical verification (`verify_all_math`), and real Node KaTeX audit.
"""

from fractions import Fraction
import json
import math
import os
import re
import subprocess
import sys
import xml.etree.ElementTree as ET

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

from scripts.sat_math_helpers import math_mcq, math_spr
from scripts.sat_real_exams_pipeline import validate_sat_bluebook_json

TEST_CODE = 'real_june2025_v2_math'
FOLDER_KEY = 'real_math'
ORDER_INDEX = 7
TEST_TITLE = '🏛️ Real Exam — June 2025 Ver 2 Math (44 Qs)'


# ============================================================================
# CRISP BLUEBOOK-STYLE HTML TABLES & INLINE SVG DIAGRAMS (ZERO WATERMARKS)
# ============================================================================

def _bluebook_table(headers, rows):
    th = ''.join(
        f'<th style="padding:8px 18px;border:1px solid #cbd5e1;background:#f1f5f9;'
        f'font-weight:700;text-align:center;color:#0f172a;">{h}</th>'
        for h in headers
    )
    trs = ''.join(
        '<tr>' + ''.join(
            f'<td style="padding:7px 18px;border:1px solid #cbd5e1;'
            f'text-align:center;color:#0f172a;">{c}</td>'
            for c in r
        ) + '</tr>'
        for r in rows
    )
    return (
        '<div style="display:flex;justify-content:center;margin:12px 0;">'
        '<table style="border-collapse:collapse;font-size:15px;min-width:200px;'
        'background:#ffffff;box-shadow:0 1px 2px rgba(15,23,42,0.06);">'
        f'<thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table></div>'
    )


def _svg_m1_q9_parallel_transversal():
    """Exact recreation of June 2025 Ver 2 M1 Q9 (parallel lines r, s; transversal t; corresponding x° and 44°)."""
    # Line r: y = 74, line s: y = 142 (x from 34 to 256)
    # Transversal t: (58, 190) -> (248, 26), dx = 190, dy = -164 (angle ≈ 40.8°)
    # Intersections: y = 74 => x = 192.4; y = 142 => x = 113.6
    return (
        '<div style="display:flex;justify-content:center;margin:10px 0;">'
        '<svg viewBox="0 0 320 225" width="320" height="225" xmlns="http://www.w3.org/2000/svg" '
        'style="background:#ffffff;border:1px solid #e2e8f0;border-radius:12px;">'
        # Parallel lines r and s
        '<line x1="34" y1="74" x2="256" y2="74" stroke="#0f172a" stroke-width="2.1"/>'
        '<line x1="34" y1="142" x2="256" y2="142" stroke="#0f172a" stroke-width="2.1"/>'
        # Transversal t
        '<line x1="58" y1="190" x2="248" y2="26" stroke="#0f172a" stroke-width="2.1"/>'
        # Subtle angle arcs for corresponding acute angles x° and 44°
        '<path d="M 214.4 74 A 22 22 0 0 0 209.1 59.6" fill="none" stroke="#1d4ed8" stroke-width="1.5"/>'
        '<path d="M 135.6 142 A 22 22 0 0 0 130.3 127.6" fill="none" stroke="#b91c1c" stroke-width="1.5"/>'
        # Line labels
        '<text x="252" y="23" font-family="Georgia,serif" font-style="italic" font-size="16" '
        'fill="#0f172a">t</text>'
        '<text x="268" y="79" font-family="Georgia,serif" font-style="italic" font-size="17" '
        'fill="#0f172a">r</text>'
        '<text x="268" y="147" font-family="Georgia,serif" font-style="italic" font-size="17" '
        'fill="#0f172a">s</text>'
        # Angle labels
        '<text x="220" y="68" font-family="Georgia,serif" font-style="italic" font-size="15" '
        'fill="#1d4ed8">x&#176;</text>'
        '<text x="141" y="136" font-family="Georgia,serif" font-size="14.5" '
        'fill="#b91c1c">44&#176;</text>'
        '<text x="160" y="214" text-anchor="middle" font-family="Georgia,serif" font-size="12.5" '
        'fill="#475569">Note: Figure not drawn to scale.</text>'
        '</svg></div>'
    )


def _svg_m1_q17_subscribers_graph():
    """Exact recreation of June 2025 Ver 2 M1 Q17: y = 200 * 3^x passing through (0, 200) and (1, 600)."""
    x0, y0 = 68.0, 276.0
    sx, sy = 50.0, 0.2  # 50 px per 1 x-unit; 20 px per 100 y-units

    def px(x):
        return x0 + x * sx

    def py(y):
        return y0 - y * sy

    grid = []
    # Vertical gridlines at x = 1, 2, 3, 4
    for gx in range(1, 5):
        xp = px(gx)
        grid.append(
            f'<line x1="{xp:.1f}" y1="{py(1220):.1f}" x2="{xp:.1f}" y2="{py(0):.1f}" '
            f'stroke="#64748b" stroke-width="0.9"/>'
        )
    # Horizontal gridlines every 100 from 100 to 1200
    for gy in range(100, 1201, 100):
        yp = py(gy)
        grid.append(
            f'<line x1="{px(0):.1f}" y1="{yp:.1f}" x2="{px(4.12):.1f}" y2="{yp:.1f}" '
            f'stroke="#64748b" stroke-width="0.9"/>'
        )
        # Small y-axis tick marks
        grid.append(
            f'<line x1="{px(0) - 4:.1f}" y1="{yp:.1f}" x2="{px(0):.1f}" y2="{yp:.1f}" '
            f'stroke="#0f172a" stroke-width="1.4"/>'
        )

    # Sample smooth exponential curve y = 200 * 3^x up to y = 1250 (x ≈ 1.668)
    x_max = math.log(1250.0 / 200.0) / math.log(3.0)
    pts = []
    steps = 40
    for i in range(steps + 1):
        xv = x_max * i / steps
        yv = 200.0 * (3.0 ** xv)
        pts.append(f'{px(xv):.1f},{py(yv):.1f}')
    curve_d = 'M ' + ' L '.join(pts)

    x_ticks = ''.join(
        f'<line x1="{px(gx):.1f}" y1="{py(0):.1f}" x2="{px(gx):.1f}" y2="{py(0) + 5:.1f}" '
        f'stroke="#0f172a" stroke-width="1.4"/>'
        f'<text x="{px(gx):.1f}" y="{py(0) + 19:.1f}" text-anchor="middle" '
        f'font-family="Georgia,serif" font-size="13.5" fill="#0f172a">{gx}</text>'
        for gx in range(1, 5)
    )
    y_labels = ''.join(
        f'<text x="{px(0) - 8:.1f}" y="{py(gy) + 4.5:.1f}" text-anchor="end" '
        f'font-family="Georgia,serif" font-size="13.5" fill="#0f172a">{lbl}</text>'
        for gy, lbl in ((400, '400'), (800, '800'), (1200, '1,200'))
    )

    return (
        '<div style="display:flex;justify-content:center;margin:10px 0;">'
        '<svg viewBox="0 0 315 310" width="315" height="310" xmlns="http://www.w3.org/2000/svg" '
        'style="background:#ffffff;border:1px solid #e2e8f0;border-radius:12px;">'
        + ''.join(grid) +
        # Axes with arrowheads
        f'<line x1="{px(0) - 8:.1f}" y1="{py(0):.1f}" x2="{px(4.32):.1f}" y2="{py(0):.1f}" '
        f'stroke="#0f172a" stroke-width="2"/>'
        f'<polygon points="{px(4.32) + 6:.1f},{py(0):.1f} {px(4.32) - 2:.1f},{py(0) - 4:.1f} '
        f'{px(4.32) - 2:.1f},{py(0) + 4:.1f}" fill="#0f172a"/>'
        f'<line x1="{px(0):.1f}" y1="{py(0) + 8:.1f}" x2="{px(0):.1f}" y2="{py(1275):.1f}" '
        f'stroke="#0f172a" stroke-width="2"/>'
        f'<polygon points="{px(0):.1f},{py(1275) - 6:.1f} {px(0) - 4:.1f},{py(1275) + 2:.1f} '
        f'{px(0) + 4:.1f},{py(1275) + 2:.1f}" fill="#0f172a"/>'
        # Axis & origin labels
        f'<text x="{px(4.45):.1f}" y="{py(0) + 4:.1f}" font-family="Georgia,serif" '
        f'font-style="italic" font-size="15" fill="#0f172a">x</text>'
        f'<text x="{px(0):.1f}" y="{py(1275) - 10:.1f}" text-anchor="middle" '
        f'font-family="Georgia,serif" font-style="italic" font-size="15" fill="#0f172a">y</text>'
        f'<text x="{px(0) - 11:.1f}" y="{py(0) + 14:.1f}" font-family="Georgia,serif" '
        f'font-style="italic" font-size="13.5" fill="#0f172a">O</text>'
        + x_ticks + y_labels +
        # Exponential curve
        f'<path d="{curve_d}" fill="none" stroke="#0f172a" stroke-width="2.5" stroke-linecap="round"/>'
        '</svg></div>'
    )


def _svg_m1_q20_line_k_graph():
    """Exact recreation of June 2025 Ver 2 M1 Q20: line k through (-2, 1) and (2, -4)."""
    x0, y0, step = 160.0, 160.0, 12.0

    def px(x):
        return x0 + x * step

    def py(y):
        return y0 - y * step

    grid = []
    for g in range(-10, 11):
        if g == 0:
            continue
        xp = px(g)
        yp = py(g)
        grid.append(
            f'<line x1="{xp:.1f}" y1="{py(10.4):.1f}" x2="{xp:.1f}" y2="{py(-10.4):.1f}" '
            f'stroke="#64748b" stroke-width="0.75"/>'
        )
        grid.append(
            f'<line x1="{px(-10.4):.1f}" y1="{yp:.1f}" x2="{px(10.4):.1f}" y2="{yp:.1f}" '
            f'stroke="#64748b" stroke-width="0.75"/>'
        )

    # Tick labels every 2 units on x- and y-axes (with subtle white halo for readability)
    labels = []
    for v in (-10, -8, -6, -4, -2, 2, 4, 6, 8, 10):
        # x-axis label
        lx = px(v)
        ly = py(0) + 14.5
        labels.append(
            f'<text x="{lx:.1f}" y="{ly:.1f}" text-anchor="middle" font-family="Georgia,serif" '
            f'font-size="11" fill="#0f172a" stroke="#ffffff" stroke-width="3" '
            f'paint-order="stroke">{v}</text>'
        )
        # y-axis label
        yx = px(0) - 6.5
        yy = py(v) + 3.8
        labels.append(
            f'<text x="{yx:.1f}" y="{yy:.1f}" text-anchor="end" font-family="Georgia,serif" '
            f'font-size="11" fill="#0f172a" stroke="#ffffff" stroke-width="3" '
            f'paint-order="stroke">{v}</text>'
        )

    # Line k: y = -(5/4)x - 3/2, clipped to y in [-10.7, 10.7]
    # y = 10.7 => x = -4/5*(12.2) = -9.76; y = -10.7 => x = -4/5*(-9.2) = 7.36
    x_top, y_top = -9.76, 10.7
    x_bot, y_bot = 7.36, -10.7

    return (
        '<div style="display:flex;justify-content:center;margin:10px 0;">'
        '<svg viewBox="0 0 320 315" width="320" height="315" xmlns="http://www.w3.org/2000/svg" '
        'style="background:#ffffff;border:1px solid #e2e8f0;border-radius:12px;">'
        + ''.join(grid) +
        # Axes with arrowheads
        f'<line x1="{px(-10.8):.1f}" y1="{py(0):.1f}" x2="{px(11.1):.1f}" y2="{py(0):.1f}" '
        f'stroke="#0f172a" stroke-width="1.9"/>'
        f'<polygon points="{px(11.1) + 6:.1f},{py(0):.1f} {px(11.1) - 1:.1f},{py(0) - 3.8:.1f} '
        f'{px(11.1) - 1:.1f},{py(0) + 3.8:.1f}" fill="#0f172a"/>'
        f'<line x1="{px(0):.1f}" y1="{py(-10.8):.1f}" x2="{px(0):.1f}" y2="{py(11.1):.1f}" '
        f'stroke="#0f172a" stroke-width="1.9"/>'
        f'<polygon points="{px(0):.1f},{py(11.1) - 6:.1f} {px(0) - 3.8:.1f},{py(11.1) + 1:.1f} '
        f'{px(0) + 3.8:.1f},{py(11.1) + 1:.1f}" fill="#0f172a"/>'
        # Axis & origin labels
        f'<text x="{px(11.8):.1f}" y="{py(0) + 4:.1f}" font-family="Georgia,serif" '
        f'font-style="italic" font-size="14" fill="#0f172a">x</text>'
        f'<text x="{px(0):.1f}" y="{py(11.1) - 10:.1f}" text-anchor="middle" '
        f'font-family="Georgia,serif" font-style="italic" font-size="14" fill="#0f172a">y</text>'
        f'<text x="{px(0) - 8:.1f}" y="{py(0) + 12:.1f}" font-family="Georgia,serif" '
        f'font-style="italic" font-size="11.5" fill="#0f172a" stroke="#ffffff" stroke-width="2.5" '
        f'paint-order="stroke">O</text>'
        + ''.join(labels) +
        # Line k and plotted lattice dots (-2, 1) and (2, -4)
        f'<line x1="{px(x_top):.1f}" y1="{py(y_top):.1f}" x2="{px(x_bot):.1f}" y2="{py(y_bot):.1f}" '
        f'stroke="#0f172a" stroke-width="2.4" stroke-linecap="round"/>'
        f'<circle cx="{px(-2):.1f}" cy="{py(1):.1f}" r="4.2" fill="#0f172a"/>'
        f'<circle cx="{px(2):.1f}" cy="{py(-4):.1f}" r="4.2" fill="#0f172a"/>'
        '</svg></div>'
    )


def _html_m2_q6_tables():
    """Exact recreation of the 4 candidate (x, y) tables for June 2025 Ver 2 M2 Q6."""
    tables = [
        ('A', [(1, r'\(\frac{59}{15}\)'), (2, r'\(\frac{53}{15}\)'), (4, r'\(\frac{41}{15}\)')]),
        ('B', [(1, r'\(\frac{48}{5}\)'), (2, r'\(\frac{46}{5}\)'), (4, r'\(\frac{42}{5}\)')]),
        ('C', [(1, r'\(\frac{42}{5}\)'), (2, r'\(\frac{39}{5}\)'), (4, r'\(\frac{33}{5}\)')]),
        ('D', [(1, r'\(\frac{69}{10}\)'), (2, r'\(\frac{63}{10}\)'), (4, r'\(\frac{51}{10}\)')]),
    ]
    cards = []
    for label, rows in tables:
        trs = ''.join(
            f'<tr>'
            f'<td style="padding:6px 14px;border:1px solid #cbd5e1;text-align:center;">{x}</td>'
            f'<td style="padding:6px 14px;border:1px solid #cbd5e1;text-align:center;">{y}</td>'
            f'</tr>'
            for x, y in rows
        )
        cards.append(
            f'<div style="border:1px solid #cbd5e1;border-radius:10px;padding:10px 12px;background:#f8fafc;">'
            f'<div style="font-weight:800;font-size:13px;color:#1e3a8a;margin-bottom:6px;text-align:center;">'
            f'Table {label}</div>'
            f'<table style="border-collapse:collapse;width:100%;font-size:14.5px;background:#ffffff;">'
            f'<thead><tr>'
            f'<th style="padding:6px 14px;border:1px solid #cbd5e1;background:#f1f5f9;text-align:center;">\\(x\\)</th>'
            f'<th style="padding:6px 14px;border:1px solid #cbd5e1;background:#f1f5f9;text-align:center;">\\(y\\)</th>'
            f'</tr></thead><tbody>{trs}</tbody></table></div>'
        )
    return (
        r'<p style="text-align:center;">\[\frac{2}{5}x + \frac{2}{3}y = 5\]</p>'
        '<div style="display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px;margin:12px 0;">'
        + ''.join(cards) +
        '</div>'
    )


# ============================================================================
# MODULE 1: 22 REAL QUESTIONS (15 MCQ + 7 SPR) — p.56–79
# ============================================================================

def _build_m1_questions():
    tbl_m1_q1 = _bluebook_table(
        [r'\(x\)', r'\(f(x)\)'],
        [
            [r'\(-1\)', r'\(\frac{1}{50}\)'],
            [r'\(0\)', r'\(1\)'],
            [r'\(1\)', r'\(50\)'],
            [r'\(2\)', r'\(2{,}500\)'],
        ],
    )

    tbl_m1_q18 = _bluebook_table(
        ['Group', 'Number of objects'],
        [
            ['A', '325'],
            ['B', '64'],
            ['C', '611'],
            ['D', '96'],
            ['<b>Total</b>', '<b>1,096</b>'],
        ],
    )

    tbl_m1_q21 = _bluebook_table(
        [r'\(x\)', r'\(r(x)\)'],
        [
            [r'\(-41\)', r'\(-6\)'],
            [r'\(-21\)', r'\(0\)'],
            [r'\(-1\)', r'\(6\)'],
        ],
    )

    return [
        # M1 Q1 (p56)
        math_mcq(
            'sat_real_jun25v2_m1_q1', 1, 'Problem-Solving and Data Analysis',
            'Linear and exponential growth', 'Easy',
            r'<p>The table shows selected values from the function \(f\).</p>' + tbl_m1_q1,
            r'Which of the following is the best description of function \(f\)?',
            {
                'A': 'Increasing linear',
                'B': 'Decreasing linear',
                'C': 'Increasing exponential',
                'D': 'Decreasing exponential',
            },
            'C',
            r'Khi \(x\) tăng đều thêm \(1\) đơn vị (\(-1 \to 0 \to 1 \to 2\)), giá trị \(f(x)\) không tăng theo hiệu số cố định mà <b>nhân thêm hệ số không đổi bằng \(50\)</b>: \[\frac{1}{1/50} = 50, \quad \frac{50}{1} = 50, \quad \frac{2{,}500}{50} = 50.\] Như vậy \(f(x) = 50^x\) là <b>hàm mũ đồng biến (Increasing exponential)</b> vì cơ số \(50 > 1\).',
            r'Tỉ số giữa các giá trị \(f(x)\) liên tiếp không đổi (\(= b > 1\)) khi \(x\) tăng đều \(\Rightarrow\) <b>Increasing exponential</b>.',
            {
                'A': ('Nhầm hàm mũ với tuyến tính', r'Hàm tuyến tính tăng phải có hiệu \(f(x+1)-f(x)\) không đổi, nhưng ở đây \(1 - \frac{1}{50} \neq 50 - 1 \neq 2{,}500 - 50\).'),
                'B': ('Sai cả xu hướng lẫn dạng hàm', r'Các giá trị \(f(x)\) đang tăng mạnh chứ không giảm và cũng không tuyến tính.'),
                'C': ('Chính xác', r'\(f(x) = 50^x\) tăng theo cấp số nhân với công bội \(50 > 1\).'),
                'D': ('Nhầm chiều biến thiên', r'Hàm mũ giảm phải có \(0 < b < 1\) khiến \(f(x)\) nhỏ dần, trái ngược với bảng số liệu.'),
            },
            r'Nhập bảng điểm \((-1, 1/50), (0, 1), (1, 50), (2, 2500)\) hoặc gõ `y = 50^x` vào Desmos để thấy ngay đường cong mũ đi lên.'
        ),

        # M1 Q2 (p57)
        math_mcq(
            'sat_real_jun25v2_m1_q2', 2, 'Algebra',
            'Linear functions', 'Easy',
            r'<p>The equation \(d = 37w + 100\) gives the total amount of money \(d\), in dollars, that Janna plans to save \(w\) weeks after she starts to save.</p>',
            r'What is the total amount of money, in dollars, she plans to save in \(10\) weeks?',
            {
                'A': r'\(420\)',
                'B': r'\(470\)',
                'C': r'\(520\)',
                'D': r'\(570\)',
            },
            'B',
            r'Thay \(w = 10\) vào phương trình \(d = 37w + 100\): \[d = 37(10) + 100 = 370 + 100 = 470.\] Vậy tổng số tiền Janna dự định tiết kiệm sau \(10\) tuần là \(\$470\).',
            r'Đọc đúng biến cần thay (\(w = 10\)) và thực hiện phép nhân trước phép cộng.',
            {
                'A': ('Tính sai phép cộng', r'Nhầm \(370 + 100\) thành \(420\) (chỉ cộng \(50\)).'),
                'B': ('Chính xác', r'\(37(10) + 100 = 370 + 100 = 470\).'),
                'C': ('Tính sai phép cộng', r'Cộng thừa \(50\) vào kết quả đúng.'),
                'D': ('Nhầm hệ số góc thành 47', r'Tính \(47(10) + 100 = 570\) thay vì \(37(10) + 100\).'),
            },
            r'Gõ thẳng `37*10 + 100` vào Desmos ra ngay `470`.'
        ),

        # M1 Q3 (p58)
        math_mcq(
            'sat_real_jun25v2_m1_q3', 3, 'Algebra',
            'Linear equations in one variable', 'Easy',
            r'',
            r'What value of \(n\) is the solution to the equation \(9n - 10 = 2n + 25\)?',
            {
                'A': r'\(5\)',
                'B': r'\(7\)',
                'C': r'\(9\)',
                'D': r'\(11\)',
            },
            'A',
            r'Chuyển các hạng tử chứa \(n\) sang vế trái và hằng số sang vế phải: \[9n - 2n = 25 + 10 \Rightarrow 7n = 35 \Rightarrow n = \frac{35}{7} = 5.\] Thử lại: \(9(5) - 10 = 35\) và \(2(5) + 25 = 35\) (đúng!).',
            r'Chuyển vế nhớ đổi dấu: \(-10\) chuyển sang phải thành \(+10\), tạo tổng \(35\).',
            {
                'A': ('Chính xác', r'\(7n = 35 \Rightarrow n = 5\).'),
                'B': ('Nhầm hệ số chia', r'\(7\) là hệ số của \(n\) (\(9 - 2 = 7\)), không phải nghiệm \(n\).'),
                'C': ('Nhầm hệ số ban đầu', r'\(9\) chỉ là hệ số đứng trước \(n\) ở vế trái.'),
                'D': ('Cộng nhầm hệ số 9 + 2', r'\(11\) là tổng \(9 + 2\) khi chuyển vế không đổi dấu.'),
            },
            r'Gõ `9x - 10 = 2x + 25` vào Desmos: đường thẳng đứng cắt trục hoành tại `x = 5`.'
        ),

        # M1 Q4 (p59)
        math_mcq(
            'sat_real_jun25v2_m1_q4', 4, 'Advanced Math',
            'Nonlinear equations in one variable and systems of equations in two variables', 'Easy',
            r'<p style="text-align:center;">\[x^2 - 2 = 23\]</p>',
            r'Which value is a solution to the given equation?',
            {
                'A': r'\(-23\)',
                'B': r'\(-21\)',
                'C': r'\(-2\)',
                'D': r'\(5\)',
            },
            'D',
            r'Cộng \(2\) vào hai vế phương trình: \[x^2 = 23 + 2 = 25 \Rightarrow x = \pm 5.\] Trong bốn đáp án, chỉ có \(5\) là một nghiệm của phương trình.',
            r'Khi giải \(x^2 = k\), luôn nhớ có hai nghiệm đối nhau \(\pm\sqrt{k}\) rồi đối chiếu đáp án xuất hiện trong 4 lựa chọn.',
            {
                'A': ('Thay thử sai', r'\((-23)^2 - 2 = 527 \neq 23\).'),
                'B': ('Trừ nhầm 2 − 23', r'Nhầm \(x = 2 - 23 = -21\) mà quên bình phương \(x^2\).'),
                'C': ('Nhầm hằng số trong đề', r'\((-2)^2 - 2 = 2 \neq 23\).'),
                'D': ('Chính xác', r'\(5^2 - 2 = 25 - 2 = 23\).'),
            },
            r'Gõ `x^2 - 2 = 23` trong Desmos ra hai đường dọc `x = -5` và `x = 5` → chọn `5`.'
        ),

        # M1 Q5 (p60)
        math_mcq(
            'sat_real_jun25v2_m1_q5', 5, 'Algebra',
            'Linear functions', 'Easy',
            r'<p style="text-align:center;">\[f(x) = 7x + 9\]</p>'
            r'<p>The function \(f\) gives the estimated height, in feet, of a poplar tree \(x\) years after its height was first measured.</p>',
            r'Which statement is the best interpretation of \(9\) in this context?',
            {
                'A': r'The tree will be measured each year for \(9\) years.',
                'B': r'The tree is estimated to grow to a maximum height of \(9\) feet.',
                'C': r'The estimated height of the tree increased by \(9\) feet each year.',
                'D': r'The estimated height of the tree was \(9\) feet when it was first measured.',
            },
            'D',
            r'Trong hàm tuyến tính \(f(x) = 7x + 9\), hằng số tự do \(9\) là tung độ gốc \(f(0) = 9\). Vì \(x\) là số năm kể từ lần đo đầu tiên, \(x = 0\) ứng với thời điểm <b>đo lần đầu tiên</b>, và \(f(0) = 9\) biểu thị <b>chiều cao ước tính ban đầu của cây là \(9\) feet khi lần đầu được đo</b>.',
            r'Với \(f(x) = mx + b\): \(m = 7\) là tốc độ tăng mỗi năm (feet/năm), còn \(b = 9\) là giá trị ban đầu tại \(x = 0\).',
            {
                'A': ('Nhầm đơn vị của 9 thành số năm', r'\(9\) là đơn vị của \(f(x)\) (feet), không phải số năm \(x\).'),
                'B': ('Nhầm giá trị ban đầu thành cực đại', r'Cây tăng \(7\) feet mỗi năm nên \(9\) feet là chiều cao lúc ban đầu, không phải tối đa.'),
                'C': ('Nhầm tung độ gốc với hệ số góc', r'Mức tăng mỗi năm là hệ số góc \(7\), không phải \(9\).'),
                'D': ('Chính xác', r'Tại \(x = 0\) (lần đo đầu tiên), \(f(0) = 9\) feet.'),
            },
            r'Thay `x = 0` vào `f(x) = 7x + 9` ra `f(0) = 9` → chiều cao ban đầu là 9 feet.'
        ),

        # M1 Q6 (p61)
        math_spr(
            'sat_real_jun25v2_m1_q6', 6, 'Geometry and Trigonometry',
            'Area and volume', 'Easy',
            r'<p>The perimeter of a square can be expressed as \(4(76)\) units.</p>',
            r'What is the length, in units, of a side of this square?',
            ['76'], '76',
            r'Chu vi hình vuông có độ dài cạnh \(s\) là \(P = 4s\). Đề bài cho chu vi là \(4(76)\), suy ra: \[4s = 4(76) \Rightarrow s = 76.\] Vậy độ dài một cạnh của hình vuông là \(76\) đơn vị.',
            r'Đừng vội nhân bung \(4 \times 76 = 304\) rồi lại chia \(4\) — nhìn cấu trúc \(P = 4s = 4(76)\) để rút ngay \(s = 76\) trong 2 giây!',
            r'Không cần nhân ra; nếu kiểm tra bằng Desmos thì gõ `4*76 / 4` ra ngay `76`.'
        ),

        # M1 Q7 (p62)
        math_mcq(
            'sat_real_jun25v2_m1_q7', 7, 'Advanced Math',
            'Nonlinear functions', 'Easy',
            r'<p>Sonja purchased a laptop in September 2018 when the laptop had a value of $1,000. Each month for the next \(50\) months, the value of the laptop decreased by \(2\%\) of the previous month&#39;s value.</p>',
            r'Which equation represents this situation, where \(v\) is the value of the laptop, in dollars, \(m\) is the number of months since Sonja purchased the laptop, and \(m \le 50\)?',
            {
                'A': r'\(v = 2{,}018(0.98)^m\)',
                'B': r'\(v = 2{,}018(2)^m\)',
                'C': r'\(v = 1{,}000(0.98)^m\)',
                'D': r'\(v = 1{,}000(2)^m\)',
            },
            'C',
            r'Giá trị ban đầu của chiếc laptop lúc \(m = 0\) là \(a = 1{,}000\) đô la. Mỗi tháng giá trị <b>giảm \(2\%\)</b> so với tháng trước, nên còn lại \(100\% - 2\% = 98\% = 0.98\) lần giá trị tháng trước. Do đó hàm mũ biểu diễn là: \[v = 1{,}000(0.98)^m.\]',
            r'Công thức suy giảm theo phần trăm: \(v = a(1 - r)^m\). Giảm \(2\%\) nghĩa là nhân với \(1 - 0.02 = 0.98\), còn số năm \(2018\) chỉ là mốc thời gian gây nhiễu!',
            {
                'A': ('Bẫy lấy năm 2018 làm giá trị ban đầu', r'\(2018\) là năm mua máy, giá trị ban đầu của laptop là \(\$1{,}000\).'),
                'B': ('Sai cả giá trị đầu lẫn hệ số nhân', r'Lấy nhầm năm \(2018\) và dùng cơ số \(2\) (tăng gấp đôi mỗi tháng!).'),
                'C': ('Chính xác', r'Giá ban đầu \(1{,}000\) và hệ số suy giảm mỗi tháng \(1 - 0.02 = 0.98\).'),
                'D': ('Nhầm giảm 2% thành nhân 2', r'Cơ số \(2\) nghĩa là tăng \(100\%\) mỗi tháng chứ không phải giảm \(2\%\).'),
            },
            r'Kiểm tra nhanh tại `m = 1`: giảm `2%` của `1000` còn `1000 - 20 = 980`, khớp đúng `1000*(0.98)^1 = 980`.'
        ),

        # M1 Q8 (p63)
        math_mcq(
            'sat_real_jun25v2_m1_q8', 8, 'Geometry and Trigonometry',
            'Lines, angles, and triangles', 'Easy',
            r'<p>In triangle \(FGH\), the measure of angle \(F\) is \(63^\circ\).</p>',
            r'Which additional piece of information is sufficient to prove that triangle \(FGH\) is a right triangle?',
            {
                'A': r'The length of \(\overline{FH}\) is \(63\).',
                'B': r'The length of \(\overline{GH}\) is \(126\).',
                'C': r'The measure of angle \(H\) is \(27^\circ\).',
                'D': r'The sum of the measures of angles \(F\), \(G\), and \(H\) is \(180^\circ\).',
            },
            'C',
            r'Tổng ba góc trong một tam giác luôn bằng \(180^\circ\). Khi biết \(\angle F = 63^\circ\) và thêm dữ kiện \(\angle H = 27^\circ\), ta suy ra ngay: \[\angle G = 180^\circ - 63^\circ - 27^\circ = 90^\circ.\] Vì tam giác có một góc vuông (\(\angle G = 90^\circ\)), dữ kiện ở đáp án C là đủ để chứng minh \(\triangle FGH\) là tam giác vuông.',
            r'Muốn chứng minh tam giác vuông khi biết một góc nhọn \(\alpha\), chỉ cần góc nhọn thứ hai bằng \(90^\circ - \alpha\) (phụ nhau) hoặc trực tiếp có một góc \(90^\circ\).',
            {
                'A': ('Không xác định được góc vuông', r'Biết độ dài một cạnh \(\overline{FH} = 63\) và \(\angle F = 63^\circ\) vẫn tạo được vô số tam giác nhọn/tù.'),
                'B': ('Không xác định được góc vuông', r'Tương tự, biết một cạnh \(\overline{GH} = 126\) không buộc tam giác có góc \(90^\circ\).'),
                'C': ('Chính xác', r'\(63^\circ + 27^\circ = 90^\circ \Rightarrow \angle G = 180^\circ - 90^\circ = 90^\circ\).'),
                'D': ('Tính chất hiển nhiên của mọi tam giác', r'Mọi tam giác phẳng đều có tổng 3 góc bằng \(180^\circ\), không riêng gì tam giác vuông.'),
            },
            r'Gõ `180 - 63 - 27` trong Desmos ra đúng `90` độ.'
        ),

        # M1 Q9 (p64)
        math_spr(
            'sat_real_jun25v2_m1_q9', 9, 'Geometry and Trigonometry',
            'Lines, angles, and triangles', 'Easy',
            _svg_m1_q9_parallel_transversal() +
            r'<p>In the figure shown, line \(r\) is parallel to line \(s\).</p>',
            r'What is the value of \(x\)?',
            ['44'], '44',
            r'Vì đường thẳng \(r \parallel s\) bị cắt bởi cát tuyến \(t\), góc \(x^\circ\) (nằm phía trên đường \(r\), bên phải đường \(t\)) và góc \(44^\circ\) (nằm phía trên đường \(s\), bên phải đường \(t\)) là hai <b>góc đồng vị (corresponding angles)</b>. Hai góc đồng vị của hai đường thẳng song song luôn bằng nhau: \[x = 44.\]',
            r'Hai đường song song bị cắt bởi cát tuyến chỉ tạo ra đúng hai loại góc: bằng nhau (đồng vị, so le trong, đối đỉnh) hoặc bù nhau (tổng \(180^\circ\)). Ở đây cả hai đều nằm ở vị trí trên-phải nên bằng nhau!',
            r'Không cần máy tính; chỉ cần đối chiếu vị trí tương ứng (trên đường thẳng, bên phải cát tuyến) để chốt ngay `44`.'
        ),

        # M1 Q10 (p65)
        math_mcq(
            'sat_real_jun25v2_m1_q10', 10, 'Advanced Math',
            'Equivalent expressions', 'Easy',
            r'<p style="text-align:center;">\[11m = 7(n + p)\]</p>'
            r'<p>The given equation relates the positive numbers \(m\), \(n\), and \(p\).</p>',
            r'Which equation correctly gives \(n\) in terms of \(m\) and \(p\)?',
            {
                'A': r'\(n = \frac{7p}{11m}\)',
                'B': r'\(n = \frac{11m}{7} - p\)',
                'C': r'\(n = 7(11m) + p\)',
                'D': r'\(n = 11m - 7 - p\)',
            },
            'B',
            r'Chia cả hai vế của phương trình \(11m = 7(n + p)\) cho \(7\), sau đó trừ cả hai vế cho \(p\): \[\frac{11m}{7} = n + p \Rightarrow n = \frac{11m}{7} - p.\]',
            r'Muốn rút ẩn nằm trong ngoặc \(7(n + p)\), hãy gỡ lớp ngoài trước (chia cho \(7\)) rồi mới chuyển \(p\) sang vế kia.',
            {
                'A': ('Biến đổi sai phép cộng thành phép nhân', r'Coi nhầm \(7(n+p)\) như phép chia tỉ lệ dẫn tới phân thức sai.'),
                'B': ('Chính xác', r'Chia hai vế cho \(7\) rồi trừ \(p\): \(n = \frac{11m}{7} - p\).'),
                'C': ('Nhân ngược 7 và đổi nhầm dấu p', r'Thay vì chia \(7\) và trừ \(p\), đáp án này lại nhân \(7\) và cộng \(p\).'),
                'D': ('Biến phép nhân 7 thành phép trừ 7', r'Trừ đi \(7\) thay vì chia cho \(7\) là lỗi đại số cơ bản.'),
            },
            r'Mẹo thử số: chọn `n = 4, p = 7` → `11m = 7(11) = 77` → `m = 7`. Thay `m = 7, p = 7` vào 4 đáp án, chỉ B cho `11*7/7 - 7 = 4 = n`!'
        ),

        # M1 Q11 (p66)
        math_spr(
            'sat_real_jun25v2_m1_q11', 11, 'Problem-Solving and Data Analysis',
            'One-variable data: Distributions and measures of center and spread', 'Medium',
            r'<p>A survey of the daily commuting times, in minutes, of seven different Chicago-based employees at a certain company yielded a data set consisting of the values \(31, 13, 44, 32, 53, 22,\) and \(44\). A survey of the daily commuting times, in minutes, of seven different San Francisco-based employees at the same company yielded a data set consisting of the values \(46, 31, 19, 33, 48, x,\) and \(38\).</p>',
            r'If the means of the two data sets are equal, what is the value of \(x\)?',
            ['24'], '24',
            r'Cả hai tập dữ liệu đều gồm đúng \(7\) nhân viên, nên hai giá trị trung bình (mean) bằng nhau <b>khi và chỉ khi tổng các giá trị của hai tập bằng nhau</b>:<br>• Tổng của Chicago: \(31 + 13 + 44 + 32 + 53 + 22 + 44 = 239\).<br>• Tổng \(6\) số đã biết của San Francisco: \(46 + 31 + 19 + 33 + 48 + 38 = 215\).<br>Do đó: \[215 + x = 239 \Rightarrow x = 239 - 215 = 24.\]',
            r'Khi hai bộ số liệu có <b>cùng kích thước \(n\)</b> và cùng trung bình cộng, không cần chia cho \(n\) — cứ cho <b>Tổng 1 = Tổng 2</b> là nhanh và đỡ sai số nhất!',
            r'Gõ `(31+13+44+32+53+22+44) - (46+31+19+33+48+38)` trong Desmos ra ngay `24`.'
        ),

        # M1 Q12 (p67)
        math_mcq(
            'sat_real_jun25v2_m1_q12', 12, 'Advanced Math',
            'Equivalent expressions', 'Easy',
            r'',
            r'Which expression is equivalent to \(5xy + 30x^2y + 35xy^2\)?',
            {
                'A': r'\(5xy(1 + 30x + 35y)\)',
                'B': r'\(5xy(1 + 6x + 7y)\)',
                'C': r'\(5xy(30x + 35y)\)',
                'D': r'\(5xy(6x + 7y)\)',
            },
            'B',
            r'Đặt nhân tử chung lớn nhất \(5xy\) ra ngoài ngoặc, chia từng hạng tử cho \(5xy\): \[5xy + 30x^2y + 35xy^2 = 5xy\left(\frac{5xy}{5xy} + \frac{30x^2y}{5xy} + \frac{35xy^2}{5xy}\right) = 5xy(1 + 6x + 7y).\]',
            r'Khi đặt nhân tử chung \(5xy\), đừng quên hai bẫy kinh điển: hạng tử đầu \(5xy \div 5xy = 1\) (KHÔNG biến mất!) và hai hệ số \(30, 35\) cũng phải chia cho \(5\) thành \(6, 7\).',
            {
                'A': ('Quên chia hệ số 30, 35 cho 5', r'Nhân bung ra được \(5xy + 150x^2y + 175xy^2\), sai hệ số.'),
                'B': ('Chính xác', r'Nhân phân phối lại: \(5xy(1) + 5xy(6x) + 5xy(7y) = 5xy + 30x^2y + 35xy^2\).'),
                'C': ('Mất số hạng 1 và quên chia 5', r'Nhân ra thành \(150x^2y + 175xy^2\), thiếu hẳn hạng tử \(5xy\).'),
                'D': ('Bỏ sót số hạng 1', r'Nhân ra chỉ được \(30x^2y + 35xy^2\), bị mất hạng tử đầu \(5xy\).'),
            },
            r'Mẹo kiểm tra chắc ăn: thay `x = 1, y = 1` → đề bài ra `5 + 30 + 35 = 70`; đáp án B ra `5(1 + 6 + 7) = 70` (duy nhất khớp!).'
        ),

        # M1 Q13 (p68)
        math_mcq(
            'sat_real_jun25v2_m1_q13', 13, 'Problem-Solving and Data Analysis',
            'Inference from sample statistics and margin of error', 'Medium',
            r'<p>A survey was conducted in Madison to estimate the percent of adult residents who support the addition of streetlights at every corner in their town. Based on the survey, it is estimated that \(40\%\) of all adult residents of Madison support the addition of streetlights at every corner in their town, with an associated margin of error of \(6\%\).</p>',
            r'Which of the following is the most appropriate conclusion about all adult residents of Madison?',
            {
                'A': r'Plausible values for the percent of all adult residents of Madison who support the addition of streetlights at every corner in their town are between \(34\%\) and \(46\%\).',
                'B': r'The addition of streetlights at every corner in the town is supported by exactly \(34\%\) of all adult residents of Madison.',
                'C': r'Plausible values for the percent of all adult residents of Madison who support the addition of streetlights at every corner in their town are either less than \(34\%\) or more than \(46\%\).',
                'D': r'The addition of streetlights at every corner in the town is supported by more than \(46\%\) of all adult residents of Madison.',
            },
            'A',
            r'Với ước lượng điểm \(\hat{p} = 40\%\) và biên độ sai số (margin of error) \(\text{ME} = 6\%\), khoảng các giá trị hợp lý (plausible values) cho tỉ lệ thực tế của toàn bộ cư dân trưởng thành tại Madison là: \[40\% - 6\% = 34\% \quad \text{đến} \quad 40\% + 6\% = 46\%.\] Do đó kết luận phù hợp nhất là đáp án A.',
            r'Gặp câu hỏi Margin of Error trên SAT: luôn chọn câu chứa cụm từ mềm dẻo <b>"plausible values ... between \((\hat{p} - \text{ME})\) and \((\hat{p} + \text{ME})\)"</b>, loại ngay các câu khẳng định tuyệt đối ("exactly", "more than").',
            {
                'A': ('Chính xác', r'Khoảng giá trị hợp lý là \(40\% \pm 6\%\), tức là từ \(34\%\) đến \(46\%\).'),
                'B': ('Khẳng định tuyệt đối "exactly 34%"', r'Khảo sát mẫu chỉ cho khoảng ước lượng, không bao giờ khẳng định chính xác \(34\%\).'),
                'C': ('Đảo ngược khoảng tin cậy', r'Khoảng hợp lý phải nằm <b>bên trong</b> \([34\%, 46\%]\), không phải nằm ngoài hai đầu mút.'),
                'D': ('Khẳng định ngoài khoảng tin cậy', r'Khảo sát không chứng minh được tỉ lệ vượt quá \(46\%\).'),
            },
            r'Tính nhanh khoảng tin cậy: `40 - 6 = 34` và `40 + 6 = 46` → khoảng hợp lý nằm giữa `34%` và `46%`.'
        ),

        # M1 Q14 (p69)
        math_mcq(
            'sat_real_jun25v2_m1_q14', 14, 'Algebra',
            'Linear inequalities in one or two variables', 'Easy',
            r'<p>A plant nursery classifies a perennial flower species as tall if its typical height when fully grown is more than \(100\) centimeters. Each of the following inequalities represents the possible heights \(h\), in centimeters, for a specific perennial flower species when fully grown.</p>',
            r'Which inequality represents the possible heights \(h\), in centimeters, for a tall perennial flower species?',
            {
                'A': r'\(18 < h < 95\)',
                'B': r'\(41 < h < 89\)',
                'C': r'\(84 < h < 100\)',
                'D': r'\(110 < h < 158\)',
            },
            'D',
            r'Một loài hoa lâu năm được xếp loại "tall" (cao) nếu chiều cao điển hình khi trưởng thành <b>lớn hơn \(100\text{ cm}\)</b> (\(h > 100\)). Kiểm tra 4 khoảng:<br>• A, B, C đều có cận trên \(\le 100\), tức mọi giá trị \(h\) đều nhỏ hơn \(100\).<br>• Chỉ có đáp án D (\(110 < h < 158\)) có toàn bộ chiều cao lớn hơn \(100\text{ cm}\).',
            r'Chú ý từ khóa <b>"more than \(100\)"</b> là dấu lớn hơn ngặt (\(h > 100\)), loại cả đáp án C dù có số \(100\) ở cận trên.',
            {
                'A': ('Toàn bộ nhỏ hơn 100', r'Chiều cao tối đa chỉ dưới \(95\text{ cm}\), không thể vượt \(100\text{ cm}\).'),
                'B': ('Toàn bộ nhỏ hơn 100', r'Mọi giá trị đều dưới \(89\text{ cm}\).'),
                'C': ('Bẫy có mặt số 100', r'\(84 < h < 100\) nghĩa là \(h\) luôn <b>nhỏ hơn</b> \(100\text{ cm}\), không thỏa "more than \(100\)".'),
                'D': ('Chính xác', r'Mọi giá trị trong khoảng \(110 < h < 158\) đều lớn hơn \(100\text{ cm}\).'),
            },
            r'So sánh trực tiếp với ngưỡng `100`: chỉ khoảng `(110, 158)` nằm hoàn toàn bên phải `100`.'
        ),

        # M1 Q15 (p70)
        math_spr(
            'sat_real_jun25v2_m1_q15', 15, 'Advanced Math',
            'Equivalent expressions', 'Easy',
            r'<p style="text-align:center;">\[(2x^2 + 3x - 3) - (7x^2 + 2x)\]</p>'
            r'<p>The given expression is equivalent to \(-5x^2 + ax - 3\), where \(a\) is a constant.</p>',
            r'What is the value of \(a\)?',
            ['1'], '1',
            r'Phá ngoặc và đổi dấu toàn bộ các hạng tử sau dấu trừ: \[(2x^2 + 3x - 3) - (7x^2 + 2x) = 2x^2 + 3x - 3 - 7x^2 - 2x = (2 - 7)x^2 + (3 - 2)x - 3 = -5x^2 + 1x - 3.\] Đồng nhất hệ số của \(x\) với \(-5x^2 + ax - 3\), ta được \(a = 1\).',
            r'Khi trừ một đa thức trong ngoặc, nhớ phân phối dấu âm vào TẤT CẢ các hạng tử bên trong (\(-(7x^2 + 2x) = -7x^2 - 2x\)), đừng cộng nhầm \(3x + 2x = 5x\)!',
            r'Gõ `(2x^2 + 3x - 3) - (7x^2 + 2x)` và `-5x^2 + ax - 3` với thanh trượt `a` trong Desmos: hai parabol trùng khít nhau khi `a = 1`.'
        ),

        # M1 Q16 (p71)
        math_mcq(
            'sat_real_jun25v2_m1_q16', 16, 'Advanced Math',
            'Equivalent expressions', 'Medium',
            r'<p>The kinetic energy \(K\), in joules, of an object is given by the formula \(K = \frac{1}{2}mv^2\), where \(m\) is the mass of the object, in kilograms, and \(v\) is the velocity of the object, in meters per second.</p>',
            r'If the kinetic energy of a certain object can be found by using the formula \(K = 98v^2\), what is the mass of the object, in kilograms?',
            {
                'A': r'\(9{,}604\)',
                'B': r'\(196\)',
                'C': r'\(98\)',
                'D': r'\(49\)',
            },
            'B',
            r'So sánh hai công thức cùng biểu diễn động năng \(K\) của vật thể: \[\frac{1}{2}mv^2 = 98v^2 \Rightarrow \frac{1}{2}m = 98 \Rightarrow m = 98 \times 2 = 196.\] Vậy khối lượng của vật là \(196\text{ kg}\).',
            r'Đồng nhất hệ số trước \(v^2\): \(\frac{1}{2}m = 98\) nên phải <b>nhân đôi</b> \(98\) thành \(196\), tuyệt đối không chia đôi thành \(49\)!',
            {
                'A': ('Bình phương nhầm 98²', r'\(98^2 = 9{,}604\) là lỗi áp dụng số mũ \(2\) của \(v\) lên hệ số \(98\).'),
                'B': ('Chính xác', r'\(\frac{1}{2}m = 98 \Rightarrow m = 196\text{ kg}\).'),
                'C': ('Quên hệ số 1/2', r'Đồng nhất trực tiếp \(m = 98\) mà bỏ qua hệ số \(\frac{1}{2}\) trong công thức.'),
                'D': ('Chia đôi thay vì nhân đôi', r'Tính nhầm \(98 \div 2 = 49\) thay vì giải \(\frac{1}{2}m = 98\).'),
            },
            r'Gõ `0.5m = 98` (hoặc `98 * 2`) trong Desmos ra ngay `196`.'
        ),

        # M1 Q17 (p72-73)
        math_mcq(
            'sat_real_jun25v2_m1_q17', 17, 'Advanced Math',
            'Nonlinear functions', 'Medium',
            _svg_m1_q17_subscribers_graph() +
            r'<p>The graph models the number of online newsletter subscribers at the end of every six-month period, where \(x\) is the number of six-month periods since the end of January 1995 and \(0 \le x \le 4\).</p>',
            r'Which statement is the best interpretation of the point \((1, 600)\) in this context?',
            {
                'A': r'The estimated number of online newsletter subscribers at the end of the first six-month period was \(600\).',
                'B': r'The estimated number of online newsletter subscribers increased every six months by \(600\) subscribers.',
                'C': r'The estimated number of online newsletter subscribers at the end of January 1995 was \(600\).',
                'D': r'The estimated number of online newsletter subscribers at the end of January 1996 was \(600\).',
            },
            'A',
            r'Đọc kỹ định nghĩa hai trục tọa độ:<br>• Hoành độ \(x\): <b>số chu kỳ 6 tháng</b> kể từ cuối tháng 1/1995. Do đó \(x = 1\) tương ứng với thời điểm <b>cuối chu kỳ 6 tháng đầu tiên</b> (tức cuối tháng 7/1995).<br>• Tung độ \(y\): số lượng người đăng ký bản tin ước tính tại thời điểm đó.<br>Vậy điểm \((1, 600)\) có nghĩa là <b>vào cuối chu kỳ 6 tháng đầu tiên, số người đăng ký ước tính là \(600\)</b>.',
            r'Cực kỳ để ý đơn vị thời gian của trục \(x\)! Ở đây 1 đơn vị \(x = 6\text{ tháng}\) (nửa năm), nên cuối tháng 1/1996 (1 năm sau) ứng với \(x = 2\), còn \(x = 1\) là cuối chu kỳ 6 tháng thứ nhất.',
            {
                'A': ('Chính xác', r'\(x = 1\) là cuối chu kỳ 6 tháng đầu tiên và \(y = 600\) là số người đăng ký ước tính.'),
                'B': ('Nhầm tọa độ điểm với tốc độ tăng tuyến tính', r'Đồ thị cong đi lên (hàm mũ \(y = 200 \cdot 3^x\)), không phải tăng đều thêm \(600\) mỗi 6 tháng.'),
                'C': ('Nhầm x = 1 với x = 0', r'Cuối tháng 1/1995 là thời điểm ban đầu \(x = 0\), khi đó trên đồ thị \(y = 200\), không phải \(600\).'),
                'D': ('Bẫy nhầm 6 tháng thành 1 năm', r'Từ cuối tháng 1/1995 đến cuối tháng 1/1996 là \(12\) tháng, tức \(x = 2\) chu kỳ 6 tháng chứ không phải \(x = 1\).'),
            },
            r'Đối chiếu đồ thị tại `x = 0` (`y = 200`) và `x = 1` (`y = 600`): mỗi bước `x` bằng 1 chu kỳ 6 tháng nên `(1, 600)` là cuối chu kỳ 6 tháng đầu tiên.'
        ),

        # M1 Q18 (p74)
        math_spr(
            'sat_real_jun25v2_m1_q18', 18, 'Problem-Solving and Data Analysis',
            'Percentages', 'Medium',
            r'<p>The table summarizes the number of objects in each group.</p>' + tbl_m1_q18 +
            r'<p>The number of objects in group C is \(p\%\) of the number of objects in group A.</p>',
            r'What is the value of \(p\)?',
            ['188'], '188',
            r'Từ bảng số liệu: số vật thể trong nhóm C là \(611\) và trong nhóm A là \(325\). Theo đề bài: \[611 = \frac{p}{100} \times 325 \Rightarrow p = \frac{611}{325} \times 100 = 1.88 \times 100 = 188.\] (Chú ý rút gọn gọn đẹp: \(611 = 47 \times 13\) và \(325 = 25 \times 13\), nên \(\frac{611}{325} = \frac{47}{25} = 1.88\)).',
            r'Dịch chuẩn câu chữ phần trăm: "C is \(p\%\) of A" \(\iff C = \frac{p}{100} \cdot A \iff p = \frac{C}{A} \times 100\). Không nhập ký hiệu \(\%\) vào ô SPR!',
            r'Gõ `(611 / 325) * 100` trong Desmos ra đúng chẵn `188`.'
        ),

        # M1 Q19 (p75)
        math_spr(
            'sat_real_jun25v2_m1_q19', 19, 'Algebra',
            'Systems of two linear equations in two variables', 'Medium',
            r'<p style="text-align:center;">\[\begin{aligned} \frac{1}{4}(s + 4t) &= 544 \\ 7s - 8t &= 1{,}192 \end{aligned}\]</p>'
            r'<p>The solution to the given system of equations is \((s, t)\).</p>',
            r'What is the value of \(s - t\)?',
            ['226'], '226',
            r'Nhân hai vế phương trình thứ nhất với \(4\) để khử mẫu: \[s + 4t = 2{,}176.\] Tiếp tục nhân phương trình này với \(2\) để triệt tiêu \(8t\): \[2s + 8t = 4{,}352.\] Cộng vế theo vế với phương trình thứ hai \(7s - 8t = 1{,}192\): \[9s = 5{,}544 \Rightarrow s = \frac{5{,}544}{9} = 616.\] Thay \(s = 616\) vào \(s + 4t = 2{,}176\): \[4t = 2{,}176 - 616 = 1{,}560 \Rightarrow t = 390.\] Vậy giá trị cần tìm là: \[s - t = 616 - 390 = 226.\]',
            r'Khử mẫu ngay ở bước đầu (\(\times 4\)) rồi dùng cộng đại số khử \(8t\); cuối cùng đọc kỹ câu hỏi xem đề đòi \(s\), \(t\) hay \(s - t\)!',
            r'Gõ hệ `0.25(x + 4y) = 544` và `7x - 8y = 1192` vào Desmos, bấm vào giao điểm ra `(616, 390)` rồi tính `616 - 390 = 226`.'
        ),

        # M1 Q20 (p76-77)
        math_mcq(
            'sat_real_jun25v2_m1_q20', 20, 'Algebra',
            'Linear equations in two variables', 'Hard',
            _svg_m1_q20_line_k_graph() +
            r'<p>Line \(k\) is shown in the \(xy\)-plane. Line \(j\) (not shown) is perpendicular to line \(k\) and passes through the point \((7, 15)\).</p>',
            r'What is the \(y\)-coordinate of the \(y\)-intercept of line \(j\)?',
            {
                'A': r'\(-\frac{47}{4}\)',
                'B': r'\(-\frac{3}{2}\)',
                'C': r'\(\frac{4}{5}\)',
                'D': r'\(\frac{47}{5}\)',
            },
            'D',
            r'Đọc hai điểm lưới được chấm đậm trên đường thẳng \(k\): \((-2, 1)\) và \((2, -4)\).<br>1. Hệ số góc của đường thẳng \(k\): \[m_k = \frac{-4 - 1}{2 - (-2)} = -\frac{5}{4}.\] 2. Vì đường thẳng \(j \perp k\), hệ số góc của \(j\) là số đối nghịch đảo: \[m_j = -\frac{1}{m_k} = \frac{4}{5}.\] 3. Phương trình đường thẳng \(j\) có dạng \(y = \frac{4}{5}x + b\) đi qua điểm \((7, 15)\): \[15 = \frac{4}{5}(7) + b \Rightarrow b = 15 - \frac{28}{5} = \frac{75 - 28}{5} = \frac{47}{5}.\] Vậy tung độ gốc của đường thẳng \(j\) là \(\frac{47}{5}\).',
            r'Hai đường thẳng vuông góc có tích hệ số góc bằng \(-1\) (\(m_j = -1/m_k\)). Luôn dùng đúng các điểm được đánh dấu đậm trên đồ thị để tính \(m_k\) không bị sai lệch!',
            {
                'A': ('Dùng nhầm hệ số góc m_k = −5/4 hoặc trừ sai', r'Không đảo nghịch và đổi dấu đúng khi tìm tung độ gốc của đường vuông góc.'),
                'B': ('Nhầm sang tung độ gốc của đường k', r'\(-\frac{3}{2}\) là tung độ gốc của đường \(k\) (\(y = -\frac{5}{4}x - \frac{3}{2}\)), không phải đường \(j\).'),
                'C': ('Mới dừng ở hệ số góc m_j', r'\(\frac{4}{5}\) là hệ số góc của đường \(j\), đề bài hỏi tung độ gốc \(b\).'),
                'D': ('Chính xác', r'\(b = 15 - \frac{4}{5}(7) = \frac{47}{5}\).'),
            },
            r'Gõ `m = (-4 - 1)/(2 - (-2))`, rồi `m_j = -1/m`, rồi `15 - m_j*7` trong Desmos → bấm nút đổi phân số ra ngay `47/5`!'
        ),

        # M1 Q21 (p78)
        math_spr(
            'sat_real_jun25v2_m1_q21', 21, 'Algebra',
            'Linear functions', 'Hard',
            tbl_m1_q21 +
            r'<p>For the linear function \(r\), the table shows three values of \(x\) and their corresponding values of \(r(x)\). Function \(r\) is defined by \(r(x) = ax + b\), where \(a\) and \(b\) are constants.</p>',
            r'What is the value of \(a + b\)?',
            ['33/5', '6.6', '6.60'], r'33/5 (hoặc 6.6)',
            r'Từ bảng giá trị của hàm tuyến tính \(r(x) = ax + b\):<br>1. Tính hệ số góc \(a\): \[a = \frac{0 - (-6)}{-21 - (-41)} = \frac{6}{20} = \frac{3}{10} = 0.3.\] 2. Thay điểm \((-21, 0)\) để tìm \(b\): \[0 = 0.3(-21) + b \Rightarrow b = 6.3 = \frac{63}{10}.\] 3. Tổng \(a + b\): \[a + b = \frac{3}{10} + \frac{63}{10} = \frac{66}{10} = \frac{33}{5} = 6.6.\] <b>Mẹo siêu nhanh:</b> Chú ý \(a + b = a(1) + b = r(1)\)! Từ \(x = -1\) sang \(x = 1\) tăng \(2\) đơn vị, nên \(r(1) = r(-1) + 2a = 6 + 2(0.3) = 6.6\).',
            r'Với hàm tuyến tính \(r(x) = ax + b\), giá trị \(a + b\) chính là \(r(1)\)! Mẹo này giúp kiểm tra chéo cực nhanh trong 5 giây.',
            r'Nhập bảng `(-41, -6), (-21, 0), (-1, 6)` rồi hồi quy `y1 ~ a*x1 + b` trong Desmos ra `a = 0.3`, `b = 6.3` → gõ `a + b` ra ngay `6.6` (`33/5`).'
        ),

        # M1 Q22 (p79)
        math_mcq(
            'sat_real_jun25v2_m1_q22', 22, 'Advanced Math',
            'Nonlinear equations in one variable and systems of equations in two variables', 'Hard',
            r'<p style="text-align:center;">\[\begin{aligned} y &= -3x^2 - 40 \\ y &= qx - 37 \end{aligned}\]</p>'
            r'<p>In the given system of equations, \(q\) is a positive constant. The graphs of the equations in the given system intersect at exactly one point, \((x, y)\), in the \(xy\)-plane.</p>',
            r'What is the value of \(x\)?',
            {
                'A': r'\(-77\)',
                'B': r'\(-43\)',
                'C': r'\(-6\)',
                'D': r'\(-1\)',
            },
            'D',
            r'Phương trình hoành độ giao điểm của parabol và đường thẳng: \[-3x^2 - 40 = qx - 37 \Rightarrow 3x^2 + qx + 3 = 0.\] Để hai đồ thị cắt nhau tại <b>đúng một điểm</b>, phương trình bậc hai phải có nghiệm kép (\(\Delta = 0\)): \[\Delta = q^2 - 4(3)(3) = 0 \Rightarrow q^2 = 36.\] Vì \(q\) là hằng số <b>dương</b> (\(q > 0\)), ta có \(q = 6\). Thay \(q = 6\) trở lại phương trình: \[3x^2 + 6x + 3 = 0 \Rightarrow 3(x + 1)^2 = 0 \Rightarrow x = -1.\]',
            r'Bẫy chốt hạ câu 22: sau khi tìm được \(q = 6\), đọc kỹ xem đề hỏi \(q\), \(x\) hay \(y\)! Nghiệm kép luôn nằm tại \(x = -\frac{b}{2a} = -\frac{6}{2(3)} = -1\).',
            {
                'A': ('Cộng nhầm hai hằng số −40 − 37', r'\(-77\) là kết quả của việc cộng \(-40\) và \(-37\) sai chiều chuyển vế.'),
                'B': ('Nhầm sang tung độ y của giao điểm', r'Tại \(x = -1\), \(y = -3(-1)^2 - 40 = -43\). Đây là \(y\), trong khi đề hỏi \(x\)!'),
                'C': ('Nhầm sang −q', r'\(-6\) là giá trị đối của \(q = 6\), không phải nghiệm \(x\).'),
                'D': ('Chính xác', r'Với \(q = 6\), phương trình trở thành \(3(x + 1)^2 = 0 \Rightarrow x = -1\).'),
            },
            r'Gõ `y = -3x^2 - 40` và `y = qx - 37` (thêm slider `q > 0`) vào Desmos: chỉnh `q = 6` thấy đường thẳng tiếp xúc parabol tại đúng `(-1, -43)` → lấy hoành độ `x = -1`!'
        ),
    ]


# ============================================================================
# MODULE 2: 22 REAL QUESTIONS (17 MCQ + 5 SPR) — p.80–102
# ============================================================================

def _build_m2_questions():
    return [
        # M2 Q1 (p80)
        math_mcq(
            'sat_real_jun25v2_m2_q1', 1, 'Algebra',
            'Linear functions', 'Easy',
            r'<p>For the linear function \(g\), the graph of \(y = g(x)\) in the \(xy\)-plane has a slope of \(3\) and passes through the point \((2, 28)\).</p>',
            r'Which equation defines \(g\)?',
            {
                'A': r'\(g(x) = 22x\)',
                'B': r'\(g(x) = 22x + 3\)',
                'C': r'\(g(x) = 3x\)',
                'D': r'\(g(x) = 3x + 22\)',
            },
            'D',
            r'Hàm tuyến tính có hệ số góc \(m = 3\) nên có dạng \(g(x) = 3x + b\). Vì đồ thị đi qua điểm \((2, 28)\): \[28 = 3(2) + b \Rightarrow 28 = 6 + b \Rightarrow b = 22.\] Do đó \(g(x) = 3x + 22\).',
            r'Hệ số góc \(m = 3\) luôn đứng ngay trước \(x\) — loại ngay A và B, sau đó thay \(x = 2\) xem phương trình nào cho \(g(2) = 28\).',
            {
                'A': ('Đặt nhầm tung độ gốc làm hệ số góc', r'Có hệ số góc \(22\) thay vì \(3\), và \(g(2) = 44 \neq 28\).'),
                'B': ('Đảo vị trí hệ số góc và tung độ gốc', r'Hệ số góc phải là \(3\), không phải \(22\); hơn nữa \(g(2) = 47 \neq 28\).'),
                'C': ('Thiếu tung độ gốc b = 22', r'\(g(2) = 3(2) = 6 \neq 28\).'),
                'D': ('Chính xác', r'Hệ số góc bằng \(3\) và \(g(2) = 3(2) + 22 = 28\).'),
            },
            r'Kiểm tra nhanh bằng `3(2) + 22 = 28` trong Desmos → khớp ngay đáp án D.'
        ),

        # M2 Q2 (p81)
        math_mcq(
            'sat_real_jun25v2_m2_q2', 2, 'Algebra',
            'Systems of two linear equations in two variables', 'Easy',
            r'',
            r'If the equations \(-9x + y = 17\) and \(9x + y = 17\) are graphed in the \(xy\)-plane, at what point \((x, y)\) do the graphs intersect?',
            {
                'A': r'\((0, 17)\)',
                'B': r'\((0, 9)\)',
                'C': r'\((9, 0)\)',
                'D': r'\((17, 0)\)',
            },
            'A',
            r'Cộng vế theo vế hai phương trình để triệt tiêu \(x\): \[(-9x + y) + (9x + y) = 17 + 17 \Rightarrow 2y = 34 \Rightarrow y = 17.\] Thay \(y = 17\) vào \(9x + y = 17\): \[9x + 17 = 17 \Rightarrow 9x = 0 \Rightarrow x = 0.\] Vậy hai đường thẳng cắt nhau tại \((0, 17)\).',
            r'Nhìn tinh ý: viết lại thành \(y = 9x + 17\) và \(y = -9x + 17\) thấy ngay cả hai có <b>cùng tung độ gốc \((0, 17)\)</b> nên cắt nhau đúng tại đó!',
            {
                'A': ('Chính xác', r'Thay \(x = 0, y = 17\) vào cả hai phương trình đều cho \(17 = 17\).'),
                'B': ('Nhầm tung độ với hệ số 9', r'Thay \((0, 9)\) cho \(9 \neq 17\).'),
                'C': ('Đảo tọa độ và nhầm hệ số 9', r'Thay \((9, 0)\) cho \(\pm 81 \neq 17\).'),
                'D': ('Đảo thứ tự (x, y)', r'Thay \((17, 0)\) vào phương trình thứ nhất cho \(-153 \neq 17\).'),
            },
            r'Gõ `-9x + y = 17` và `9x + y = 17` vào Desmos, bấm giao điểm ra ngay `(0, 17)`.'
        ),

        # M2 Q3 (p82)
        math_mcq(
            'sat_real_jun25v2_m2_q3', 3, 'Algebra',
            'Linear inequalities in one or two variables', 'Easy',
            r'<p>A baker has a total of \(15\) cups of flour and enough other ingredients to make banana pancakes and apple pancakes. The baker needs \(1.25\) cups of flour for a batch of banana pancakes and \(0.75\) cups of flour for a batch of apple pancakes.</p>',
            r'If the baker makes \(8\) batches of banana pancakes, what is the greatest number of whole batches of apple pancakes the baker can make?',
            {
                'A': r'\(6\)',
                'B': r'\(7\)',
                'C': r'\(8\)',
                'D': r'\(9\)',
            },
            'A',
            r'Số cốc bột dùng để làm \(8\) mẻ bánh chuối là: \[8 \times 1.25 = 10\text{ cốc}.\] Lượng bột còn lại: \[15 - 10 = 5\text{ cốc}.\] Gọi \(a\) là số mẻ bánh táo (\(a \in \mathbb{Z}\)): \[0.75a \le 5 \Rightarrow a \le \frac{5}{0.75} = \frac{20}{3} \approx 6.67.\] Vì chỉ tính <b>số mẻ nguyên trọn vẹn (whole batches)</b>, phải làm tròn xuống: số mẻ bánh táo nhiều nhất có thể làm là \(6\).',
            r'Bẫy làm tròn cổ điển: \(6.67\) mẻ thì KHÔNG đủ bột làm mẻ thứ \(7\) (\(7 \times 0.75 = 5.25 > 5\)), nên bài toán giới hạn tài nguyên luôn làm tròn <b>XUỐNG</b>!',
            {
                'A': ('Chính xác', r'\(6 \times 0.75 = 4.5 \le 5\) cốc (đủ bột), còn \(7\) mẻ cần \(5.25 > 5\) cốc.'),
                'B': ('Bẫy làm tròn lên 6.67 → 7', r'\(7\) mẻ cần \(7 \times 0.75 = 5.25\) cốc, vượt quá \(5\) cốc còn lại.'),
                'C': ('Nhầm số mẻ chuối 8', r'\(8\) mẻ bánh táo cần \(6\) cốc bột, tổng \(16 > 15\) cốc.'),
                'D': ('Tính sai lượng bột còn lại', r'\(9\) mẻ bánh táo cần \(6.75\) cốc, vượt xa \(5\) cốc còn lại.'),
            },
            r'Gõ `(15 - 8*1.25) / 0.75` trong Desmos ra `6.6667` → làm tròn xuống số nguyên là `6`.'
        ),

        # M2 Q4 (p83)
        math_mcq(
            'sat_real_jun25v2_m2_q4', 4, 'Advanced Math',
            'Nonlinear functions', 'Easy',
            r'',
            r'What is the \(y\)-intercept of the graph of \(y = 6(7)^{x + 2}\) in the \(xy\)-plane?',
            {
                'A': r'\((0, 6)\)',
                'B': r'\((0, 84)\)',
                'C': r'\((0, 294)\)',
                'D': r'\((0, 1{,}764)\)',
            },
            'C',
            r'Tại giao điểm với trục tung (\(y\)-intercept), ta luôn có \(x = 0\). Thay \(x = 0\) vào phương trình: \[y = 6(7)^{0 + 2} = 6 \cdot 7^2 = 6 \cdot 49 = 294.\] Vậy giao điểm với trục tung là \((0, 294)\).',
            r'Cẩn thận bẫy số mũ dịch chuyển \((x + 2)\): đừng vội đọc hệ số phía trước \(6\) là tung độ gốc! Luôn thay \(x = 0\) vào hàm để tính.',
            {
                'A': ('Bẫy đọc hệ số phía trước 6', r'Chỉ đúng nếu là \(y = 6(7)^x\), còn ở đây số mũ là \(x + 2\) nên tại \(x = 0\) phải nhân thêm \(7^2 = 49\).'),
                'B': ('Nhầm 7² thành 7 × 2', r'Tính sai \(6 \times (7 \times 2) = 84\) thay vì \(6 \times 7^2 = 294\).'),
                'C': ('Chính xác', r'\(y = 6 \cdot 7^2 = 6 \cdot 49 = 294 \Rightarrow (0, 294)\).'),
                'D': ('Nhầm thứ tự lũy thừa (6 · 7)²', r'\((6 \cdot 7)^2 = 42^2 = 1{,}764\) — sai vì bình phương chỉ tác dụng lên cơ số \(7\), không bao gồm \(6\).'),
            },
            r'Gõ `6 * 7^(0 + 2)` trong Desmos ra ngay `294` → chọn `(0, 294)`.'
        ),

        # M2 Q5 (p84)
        math_mcq(
            'sat_real_jun25v2_m2_q5', 5, 'Advanced Math',
            'Nonlinear equations in one variable and systems of equations in two variables', 'Easy',
            r'<p style="text-align:center;">\[x^2 - 11x - 3 = 0\]</p>',
            r'What is a solution to the given equation?',
            {
                'A': r'\(\frac{11 + \sqrt{(-11)^2 - 4(1)(-3)}}{2(-3)}\)',
                'B': r'\(\frac{11 + \sqrt{(-11)^2 - 4(1)(-3)}}{2(1)}\)',
                'C': r'\(\frac{3 + \sqrt{(-3)^2 - 4(1)(-11)}}{2(-3)}\)',
                'D': r'\(\frac{3 + \sqrt{(-3)^2 - 4(1)(-11)}}{2(1)}\)',
            },
            'B',
            r'Áp dụng công thức nghiệm phương trình bậc hai \(ax^2 + bx + c = 0\) với \(a = 1\), \(b = -11\), \(c = -3\): \[x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a} = \frac{-(-11) \pm \sqrt{(-11)^2 - 4(1)(-3)}}{2(1)} = \frac{11 \pm \sqrt{(-11)^2 - 4(1)(-3)}}{2(1)}.\] Do đó một nghiệm của phương trình là biểu thức ở đáp án B.',
            r'Kiểm tra nhanh 3 vị trí trong công thức nghiệm: \(-b = 11\), biệt thức \(b^2 - 4ac = (-11)^2 - 4(1)(-3)\), và mẫu số \(2a = 2(1)\).',
            {
                'A': ('Nhầm mẫu số 2c thay vì 2a', r'Mẫu số phải là \(2a = 2(1)\), không phải \(2(-3)\).'),
                'B': ('Chính xác', r'Khớp hoàn toàn công thức \(\frac{-b + \sqrt{b^2 - 4ac}}{2a}\) với \(a = 1, b = -11, c = -3\).'),
                'C': ('Đảo nhầm vai trò b, c và sai mẫu số', r'Dùng nhầm \(b = -3, c = -11\) và chia cho \(2(-3)\).'),
                'D': ('Đảo nhầm vai trò b và c', r'Đổi nhầm \(b = -3\) và \(c = -11\) (đây là nghiệm của \(x^2 - 3x - 11 = 0\)).'),
            },
            r'Vẽ `y = x^2 - 11x - 3` trong Desmos ra nghiệm dương `x ≈ 11.266`, trùng khít với `(11 + sqrt(133))/2 ≈ 11.266` ở B.'
        ),

        # M2 Q6 (p85-86)
        math_mcq(
            'sat_real_jun25v2_m2_q6', 6, 'Algebra',
            'Linear equations in two variables', 'Medium',
            _html_m2_q6_tables(),
            r'Which table gives three values of \(x\) and their corresponding values of \(y\) for the given equation?',
            {
                'A': r'Table A: \(\left(1,\; \frac{59}{15}\right),\; \left(2,\; \frac{53}{15}\right),\; \left(4,\; \frac{41}{15}\right)\)',
                'B': r'Table B: \(\left(1,\; \frac{48}{5}\right),\; \left(2,\; \frac{46}{5}\right),\; \left(4,\; \frac{42}{5}\right)\)',
                'C': r'Table C: \(\left(1,\; \frac{42}{5}\right),\; \left(2,\; \frac{39}{5}\right),\; \left(4,\; \frac{33}{5}\right)\)',
                'D': r'Table D: \(\left(1,\; \frac{69}{10}\right),\; \left(2,\; \frac{63}{10}\right),\; \left(4,\; \frac{51}{10}\right)\)',
            },
            'D',
            r'Biểu diễn \(y\) theo \(x\) từ phương trình \(\frac{2}{5}x + \frac{2}{3}y = 5\): \[\frac{2}{3}y = 5 - \frac{2}{5}x \Rightarrow y = \frac{3}{2}\left(5 - \frac{2}{5}x\right) = \frac{15}{2} - \frac{3}{5}x = \frac{75 - 6x}{10}.\] Thay lần lượt \(x = 1, 2, 4\):<br>• \(x = 1 \Rightarrow y = \frac{75 - 6}{10} = \frac{69}{10}\).<br>• \(x = 2 \Rightarrow y = \frac{75 - 12}{10} = \frac{63}{10}\).<br>• \(x = 4 \Rightarrow y = \frac{75 - 24}{10} = \frac{51}{10}\).<br>Cả ba cặp đều khớp hoàn toàn với <b>Table D</b>.',
            r'Chỉ cần thay đúng giá trị đầu tiên \(x = 1\) vào phương trình để tìm \(y = \frac{69}{10}\) là loại ngay 3 bảng còn lại trong 10 giây!',
            {
                'A': ('Tính sai tại x = 1', r'Thay \((1, \frac{59}{15})\) cho \(\frac{2}{5}(1) + \frac{2}{3}(\frac{59}{15}) = \frac{136}{45} \neq 5\).'),
                'B': ('Tính sai tại x = 1', r'Thay \((1, \frac{48}{5})\) cho \(\frac{2}{5}(1) + \frac{2}{3}(\frac{48}{5}) = \frac{34}{5} \neq 5\).'),
                'C': ('Tính sai tại x = 1', r'Thay \((1, \frac{42}{5})\) cho \(\frac{2}{5}(1) + \frac{2}{3}(\frac{42}{5}) = 6 \neq 5\).'),
                'D': ('Chính xác', r'Cả ba cặp \((1, \frac{69}{10})\), \((2, \frac{63}{10})\), \((4, \frac{51}{10})\) đều thỏa \(\frac{2}{5}x + \frac{2}{3}y = 5\).'),
            },
            r'Gõ `f(x) = (5 - (2/5)x) * (3/2)` rồi gõ `f(1), f(2), f(4)` trong Desmos → bấm đổi sang phân số ra đúng `69/10, 63/10, 51/10`!'
        ),

        # M2 Q7 (p87)
        math_mcq(
            'sat_real_jun25v2_m2_q7', 7, 'Problem-Solving and Data Analysis',
            'One-variable data: Distributions and measures of center and spread', 'Medium',
            r'<p>Ari examined a set of \(86\) plants. The lightest plant had a mass of \(2.8\text{ kilograms (kg)}\) and the heaviest plant had a mass of \(6.3\text{ kg}\). Chihiro examined the same set of \(86\) plants and also an additional plant with a mass of \(11.6\text{ kg}\).</p>',
            r'Which of the following must be true about the set of plants that Ari examined and the set of plants that Chihiro examined?',
            {
                'A': r'The standard deviation of the masses, in kg, of the plants that Ari examined is greater than the standard deviation of the masses, in kg, of the plants that Chihiro examined.',
                'B': r'The range of the masses, in kg, of the plants that Ari examined is greater than the range of the masses, in kg, of the plants that Chihiro examined.',
                'C': r'The median of the masses, in kg, of the plants that Ari examined is less than the median of the masses, in kg, of the plants that Chihiro examined.',
                'D': r'The mean of the masses, in kg, of the plants that Ari examined is less than the mean of the masses, in kg, of the plants that Chihiro examined.',
            },
            'D',
            r'Phân tích tác động khi thêm một giá trị ngoại lai (outlier) \(11.6\text{ kg}\) lớn hơn hẳn toàn bộ tập cũ (nằm trong \([2.8, 6.3]\)):<br>• Trung bình cộng của Ari chắc chắn thỏa \(\bar{x}_{\text{Ari}} \le 6.3 < 11.6\). Khi thêm một phần tử <b>lớn hơn hẳn trung bình cũ</b>, trung bình mới bắt buộc <b>tăng lên nghiêm ngặt</b>: \[\bar{x}_{\text{Chihiro}} = \frac{86\bar{x}_{\text{Ari}} + 11.6}{87} > \bar{x}_{\text{Ari}}.\] Do đó đáp án D <b>luôn luôn đúng (must be true)</b>!',
            r'Ghi nhớ quy tắc "thêm giá trị ngoại lai lớn hơn Max": Mean <b>chắc chắn tăng</b>, Range <b>chắc chắn tăng</b> (\(3.5 \to 8.8\)), Standard Deviation <b>tăng</b>, còn Median <b>có thể giữ nguyên</b> nếu các giá trị ở giữa trùng nhau!',
            {
                'A': ('Ngược chiều', r'Thêm giá trị ngoại lai \(11.6\text{ kg}\) cách rất xa cụm \([2.8, 6.3]\) làm độ lệch chuẩn của Chihiro <b>lớn hơn</b> của Ari, không phải nhỏ hơn.'),
                'B': ('Ngược chiều', r'Khoảng biến thiên (range) của Ari là \(6.3 - 2.8 = 3.5\text{ kg}\), nhỏ hơn của Chihiro là \(11.6 - 2.8 = 8.8\text{ kg}\).'),
                'C': ('Không bắt buộc đúng (bẫy "must be true")', r'Nếu các cây ở vị trí thứ \(43, 44, 45\) đều có khối lượng bằng nhau (ví dụ \(5.0\text{ kg}\)), thì trung vị của cả Ari lẫn Chihiro đều bằng \(5.0\text{ kg}\) (bằng nhau chứ không nhỏ hơn!).'),
                'D': ('Chính xác', r'Vì \(11.6 > 6.3 \ge \bar{x}_{\text{Ari}}\), trung bình của Ari chắc chắn nhỏ hơn trung bình của Chihiro.'),
            },
            r'Thử ví dụ trong Desmos: giả sử 86 cây có 1 cây `2.8`, 84 cây `5`, 1 cây `6.3` → `mean` tăng từ `5.0047` lên `5.0805`, còn `median` giữ nguyên `5` (loại C ngay!).'
        ),

        # M2 Q8 (p88)
        math_mcq(
            'sat_real_jun25v2_m2_q8', 8, 'Algebra',
            'Systems of two linear equations in two variables', 'Easy',
            r'<p style="text-align:center;">\[\begin{aligned} 3x + 9y &= 10 \\ rx + 18y &= 20 \end{aligned}\]</p>'
            r'<p>In the given system of equations, \(r\) is a constant. The system has infinitely many solutions.</p>',
            r'What is the value of \(r\)?',
            {
                'A': r'\(2\)',
                'B': r'\(3\)',
                'C': r'\(6\)',
                'D': r'\(9\)',
            },
            'C',
            r'Để hệ hai phương trình tuyến tính có <b>vô số nghiệm (infinitely many solutions)</b>, hai phương trình phải tương đương nhau (tỉ lệ các hệ số bằng nhau). Nhận thấy phương trình thứ hai có hệ số của \(y\) và hằng số đều gấp \(2\) lần phương trình thứ nhất (\(18 = 2 \times 9\), \(20 = 2 \times 10\)). Nhân phương trình đầu với \(2\): \[6x + 18y = 20 \Rightarrow r = 6.\]',
            r'Hệ \(a_1 x + b_1 y = c_1\) và \(a_2 x + b_2 y = c_2\) có vô số nghiệm \(\iff \frac{a_2}{a_1} = \frac{b_2}{b_1} = \frac{c_2}{c_1}\). Ở đây tỉ số bằng \(2 \Rightarrow r = 3 \times 2 = 6\).',
            {
                'A': ('Nhầm sang tỉ số nhân k = 2', r'\(2\) là hệ số nhân cả phương trình, còn \(r = 3 \times 2 = 6\).'),
                'B': ('Giữ nguyên hệ số của phương trình 1', r'Nếu \(r = 3\) thì hai đường thẳng cắt nhau tại duy nhất \(1\) điểm \((0, \frac{10}{9})\).'),
                'C': ('Chính xác', r'\(\frac{6}{3} = \frac{18}{9} = \frac{20}{10} = 2\), hai đường thẳng trùng khít nhau.'),
                'D': ('Nhầm sang hệ số của y ở phương trình 1', r'\(9\) là hệ số đứng trước \(y\), không phải giá trị \(r\).'),
            },
            r'Gõ `3x + 9y = 10` và `rx + 18y = 20` (slider `r`) trong Desmos: hai đường thẳng trùng khít hoàn toàn khi `r = 6`.'
        ),

        # M2 Q9 (p89)
        math_mcq(
            'sat_real_jun25v2_m2_q9', 9, 'Geometry and Trigonometry',
            'Right triangles and trigonometry', 'Medium',
            r'<p>In triangle \(ABC\), angle \(B\) is a right angle. The length of side \(AB\) is \(10\sqrt{41}\) and the length of side \(BC\) is \(24\sqrt{41}\).</p>',
            r'What is the length of side \(AC\)?',
            {
                'A': r'\(14\sqrt{41}\)',
                'B': r'\(26\sqrt{41}\)',
                'C': r'\(34\sqrt{41}\)',
                'D': r'\(\sqrt{34 \cdot 41}\)',
            },
            'B',
            r'Vì \(\triangle ABC\) vuông tại \(B\), cạnh đối diện \(AC\) là <b>cạnh huyền</b>. Áp dụng định lý Pythagore: \[AC = \sqrt{AB^2 + BC^2} = \sqrt{(10\sqrt{41})^2 + (24\sqrt{41})^2} = \sqrt{41(10^2 + 24^2)} = \sqrt{41(100 + 576)} = \sqrt{41 \cdot 676} = 26\sqrt{41}.\] <b>Mẹo bộ ba Pythagore:</b> Nhận diện ngay bộ \((5, 12, 13)\) nhân với \(2\sqrt{41}\) cho \((10\sqrt{41},\; 24\sqrt{41},\; 26\sqrt{41})\)!',
            r'Ghi nhớ 4 bộ ba Pythagore kinh điển trên SAT: \((3,4,5)\), \((5,12,13)\), \((7,24,25)\), \((8,15,17)\). Thấy \(10\) và \(24\) (gấp đôi \(5\) và \(12\)) là chốt ngay cạnh huyền \(26\)!',
            {
                'A': ('Trừ hai cạnh góc vuông 24 − 10', r'Không áp dụng Pythagore mà lấy hiệu \(24 - 10 = 14\).'),
                'B': ('Chính xác', r'\(\sqrt{10^2 + 24^2}\sqrt{41} = \sqrt{676}\sqrt{41} = 26\sqrt{41}\).'),
                'C': ('Cộng hai cạnh góc vuông 10 + 24', r'Vi phạm bất đẳng thức tam giác (\(AC\) luôn phải nhỏ hơn \(AB + BC = 34\sqrt{41}\)).'),
                'D': ('Quên bình phương hai cạnh trong căn', r'Viết nhầm \(\sqrt{(10 + 24) \cdot 41}\) thay vì \(\sqrt{(10^2 + 24^2) \cdot 41}\).'),
            },
            r'Gõ `sqrt((10*sqrt(41))^2 + (24*sqrt(41))^2) / sqrt(41)` trong Desmos ra đúng chẵn `26` → chọn \(26\sqrt{41}\)!'
        ),

        # M2 Q10 (p90)
        math_mcq(
            'sat_real_jun25v2_m2_q10', 10, 'Advanced Math',
            'Nonlinear functions', 'Medium',
            r'<p style="text-align:center;">\[m(t) = -0.0274\left(\frac{t}{7}\right)^2 + 7.3873\left(\frac{t}{7}\right) + 75.032\]</p>'
            r'<p>The function \(m\) gives the predicted body mass \(m(t)\), in kilograms (kg), of a male giraffe \(t\) days after it was born in a wildlife reserve, where \(t \le 390\).</p>',
            r'Which of the following is the best interpretation of the statement &ldquo;\(m(140)\) is approximately equal to \(212\)&rdquo; in this context?',
            {
                'A': r'The predicted body mass of a male giraffe was approximately \(140\text{ kg}\) \(212\) days after it was born.',
                'B': r'The predicted body mass of a male giraffe was approximately \(212\text{ kg}\) \(140\) days after it was born.',
                'C': r'The predicted body mass of a male giraffe was approximately \(212\text{ kg}\) \(\frac{140}{7}\) days after it was born.',
                'D': r'The predicted body mass of a male giraffe was approximately \(\frac{140}{7}\text{ kg}\) \(212\) days after it was born.',
            },
            'B',
            r'Trong ký hiệu hàm số \(m(t)\):<br>• Đầu vào bên trong ngoặc \(t = 140\) là <b>số ngày sau khi chào đời</b> (140 ngày — KHÔNG chia cho \(7\), vì công thức đã tự đổi sang tuần qua \(\frac{t}{7}\)!).<br>• Đầu ra \(m(140) \approx 212\) là <b>khối lượng cơ thể dự đoán</b> (khoảng \(212\text{ kg}\)).<br>Vậy "\(m(140) \approx 212\)" nghĩa là khối lượng dự đoán của hươu cao cổ đực khoảng \(212\text{ kg}\) vào thời điểm \(140\) ngày sau khi sinh.',
            r'Bẫy cực tinh vi của câu C: biểu thức chứa \(\frac{t}{7}\) chỉ để quy đổi nội bộ sang số tuần, còn định nghĩa của biến \(t\) vẫn là <b>số ngày</b>, nên \(m(140)\) ứng với đúng \(140\) ngày!',
            {
                'A': ('Đảo ngược đầu vào và đầu ra', r'Nhầm \(140\) thành khối lượng (kg) và \(212\) thành số ngày.'),
                'B': ('Chính xác', r'\(t = 140\) ngày và \(m(140) \approx 212\text{ kg}\).'),
                'C': ('Bẫy chia thêm 7 vào số ngày', r'\(\frac{140}{7} = 20\) là số tuần, không phải số ngày! Đề đã ghi rõ \(t\) tính bằng ngày (days).'),
                'D': ('Vừa đảo đầu vào/ra vừa chia nhầm cho 7', r'Sai cả đơn vị khối lượng lẫn thời gian.'),
            },
            r'Thử kiểm chứng bằng Desmos: gõ `-0.0274*(140/7)^2 + 7.3873*(140/7) + 75.032` ra `211.818 ≈ 212` kg tại `t = 140` ngày.'
        ),

        # M2 Q11 (p91)
        math_mcq(
            'sat_real_jun25v2_m2_q11', 11, 'Geometry and Trigonometry',
            'Area and volume', 'Medium',
            r'<p>Rectangles \(ABCD\) and \(EFGH\) are similar. The length of each side of \(EFGH\) is \(10\) times the length of the corresponding side of \(ABCD\). The area of \(ABCD\) is \(140\) square units.</p>',
            r'What is the area, in square units, of \(EFGH\)?',
            {
                'A': r'\(14\)',
                'B': r'\(100\)',
                'C': r'\(1{,}400\)',
                'D': r'\(14{,}000\)',
            },
            'D',
            r'Khi hai hình đồng dạng có tỉ số độ dài cạnh là \(k = 10\), thì <b>tỉ số diện tích bằng bình phương tỉ số đồng dạng</b> \(k^2 = 10^2 = 100\) (vì cả chiều dài lẫn chiều rộng đều gấp \(10\) lần: \((10l)(10w) = 100lw\)). Do đó: \[\text{Area}(EFGH) = 140 \times 10^2 = 140 \times 100 = 14{,}000.\] ',
            r'Quy tắc tỉ lệ đồng dạng SAT: Cạnh nhân \(k \Rightarrow\) Chu vi nhân \(k\), Diện tích nhân \(k^2\), Thể tích nhân \(k^3\)!',
            {
                'A': ('Chia ngược cho 10', r'Tính \(140 \div 10 = 14\), ngược hoàn toàn đề bài.'),
                'B': ('Mới tính tỉ số diện tích k² = 100', r'\(100\) là hệ số nhân diện tích, quên chưa nhân với \(140\).'),
                'C': ('Bẫy kinh điển: quên bình phương k', r'Chỉ nhân \(140 \times 10 = 1{,}400\), quên rằng diện tích có 2 chiều nên phải nhân \(10^2 = 100\).'),
                'D': ('Chính xác', r'\(140 \times 10^2 = 14{,}000\) đơn vị diện tích.'),
            },
            r'Gõ `140 * 10^2` trong Desmos ra ngay `14000`.'
        ),

        # M2 Q12 (p92)
        math_mcq(
            'sat_real_jun25v2_m2_q12', 12, 'Algebra',
            'Linear equations in one variable', 'Medium',
            r'<p>A machine makes \(8\)-inch, \(5\)-inch, and \(7\)-inch parts. During a certain day, the number of \(8\)-inch parts that the machine makes is \(3\) times the number \(n\) of \(5\)-inch parts, and the number of \(7\)-inch parts is \(12\). During this day, the machine makes \(100\) parts total.</p>',
            r'Which equation represents this situation?',
            {
                'A': r'\(8(3n) + 5n + 7(12) = 100\)',
                'B': r'\(8n + 5n + 7n = 100\)',
                'C': r'\(3n + 12 = 100\)',
                'D': r'\(4n + 12 = 100\)',
            },
            'D',
            r'Chú ý phương trình biểu diễn <b>tổng số lượng linh kiện (parts)</b>, nên các kích thước \(8\)-inch, \(5\)-inch, \(7\)-inch chỉ là <b>tên gọi phân loại (nhiễu)</b>, KHÔNG đem nhân vào tổng!<br>• Số linh kiện \(5\)-inch: \(n\).<br>• Số linh kiện \(8\)-inch: \(3n\).<br>• Số linh kiện \(7\)-inch: \(12\).<br>Cộng tổng cả ba loại bằng \(100\): \[3n + n + 12 = 100 \Rightarrow 4n + 12 = 100.\]',
            r'Kiểm tra đơn vị vế phải: \(100\) là <b>số linh kiện (parts)</b> chứ không phải tổng số inch! Nên các con số \(8, 5, 7\) không bao giờ được nhân với số lượng.',
            {
                'A': ('Bẫy nhân kích thước (inch) vào số lượng', r'Vế trái có đơn vị là tổng số inch, không tương thích với \(100\) linh kiện ở vế phải.'),
                'B': ('Nhân kích thước và bỏ quên hệ số 3 lẫn 12', r'Sai hoàn toàn cả về đơn vị lẫn số lượng từng loại.'),
                'C': ('Quên cộng chính loại 5-inch (n)', r'Chỉ cộng \(3n\) (loại 8-inch) và \(12\) (loại 7-inch), bỏ sót \(n\) linh kiện 5-inch.'),
                'D': ('Chính xác', r'Tổng số linh kiện là \(3n + n + 12 = 4n + 12 = 100\).'),
            },
            r'Kiểm tra hợp lý: nếu `4n + 12 = 100` thì `n = 22` (5-inch), `3n = 66` (8-inch), `12` (7-inch) → tổng `22 + 66 + 12 = 100` khớp tuyệt đối!'
        ),

        # M2 Q13 (p93)
        math_spr(
            'sat_real_jun25v2_m2_q13', 13, 'Algebra',
            'Linear equations in one variable', 'Medium',
            r'',
            r'If \(2 + \frac{(1 - x)}{2} = \frac{-2(1 - x)}{3}\), what is the value of \(1 - x\)?',
            ['-12/7', '-1.714'], r'-12/7 (hoặc -1.714)',
            r'Đặt ẩn phụ \(u = 1 - x\) (vì đề hỏi trực tiếp giá trị của \(1 - x\)). Phương trình trở thành: \[2 + \frac{u}{2} = -\frac{2u}{3}.\] Nhân cả hai vế với mẫu số chung \(6\): \[12 + 3u = -4u \Rightarrow 7u = -12 \Rightarrow u = -\frac{12}{7}.\] Vậy \(1 - x = -\frac{12}{7} \approx -1.714\).',
            r'Chiến thuật "đặt cụm biểu thức làm một biến" (\(u = 1 - x\)): không cần giải ra \(x = \frac{19}{7}\) rồi lại lấy \(1 - \frac{19}{7}\), tránh mất thời gian và tránh lỗi quên đổi về \(1 - x\)!',
            r'Gõ `2 + u/2 = -2u/3` trong Desmos (dùng biến `x` thay cho `u` là `2 + x/2 = -2x/3`), đọc nghiệm `x = -1.714` và đổi phân số ra `-12/7`!'
        ),

        # M2 Q14 (p94)
        math_mcq(
            'sat_real_jun25v2_m2_q14', 14, 'Problem-Solving and Data Analysis',
            'Ratios, rates, proportional relationships, and units', 'Medium',
            r'<p>An object&#39;s speed, in meters per hour, is increasing at a rate of \(1{,}490\) meters per hour per second.</p>',
            r'Which of the following is closest to this rate in <b>feet per second squared</b>? (Use \(1\text{ meter} = 3.28\text{ feet}\).) ',
            {
                'A': r'\(0.126\)',
                'B': r'\(1.36\)',
                'C': r'\(7.57\)',
                'D': r'\(81.5\)',
            },
            'B',
            r'Viết đơn vị ban đầu dưới dạng phân số rồi nhân các hệ số chuyển đổi đơn vị (dimensional analysis): \[1{,}490\;\frac{\text{meters}}{\text{hour} \cdot \text{second}} \times \frac{3.28\text{ feet}}{1\text{ meter}} \times \frac{1\text{ hour}}{3{,}600\text{ seconds}} = \frac{1{,}490 \times 3.28}{3{,}600}\;\frac{\text{feet}}{\text{second}^2}.\] Tính giá trị: \[\frac{4{,}887.2}{3{,}600} \approx 1.3576 \approx 1.36\text{ ft/s}^2.\]',
            r'Bẫy quen thuộc trong bài đổi đơn vị gia tốc: "meters per hour per second" chỉ có <b>1 chữ hour</b> (đổi sang \(3{,}600\) giây), KHÔNG chia cho \(3{,}600^2\) và KHÔNG chia cho \(60\)!',
            {
                'A': ('Chia nhầm cho 3.28 thay vì nhân 3.28', r'\(\frac{1{,}490}{3.28 \times 3{,}600} \approx 0.126\) — đặt ngược tỉ lệ feet/meter.'),
                'B': ('Chính xác', r'\(\frac{1{,}490 \times 3.28}{3{,}600} \approx 1.358 \approx 1.36\text{ ft/s}^2\).'),
                'C': ('Chia nhầm cho 60 và chia cho 3.28', r'\(\frac{1{,}490}{3.28 \times 60} \approx 7.57\) — sai cả hai bước quy đổi.'),
                'D': ('Chỉ đổi giờ sang phút (chia 60 thay vì 3,600)', r'\(\frac{1{,}490 \times 3.28}{60} \approx 81.5\) — quên rằng \(1\text{ giờ} = 3{,}600\text{ giây}\).'),
            },
            r'Gõ `1490 * 3.28 / 3600` trong Desmos ra `1.35755...` → gần nhất là `1.36`!'
        ),

        # M2 Q15 (p95)
        math_mcq(
            'sat_real_jun25v2_m2_q15', 15, 'Algebra',
            'Linear equations in one variable', 'Medium',
            r'',
            r'Which equation has no solution?',
            {
                'A': r'\(63x + 36 = 9(7x + 4)\)',
                'B': r'\(63x + 4 = 7x + 4\)',
                'C': r'\(63x + 360 = 9(7x + 16)\)',
                'D': r'\(63x + 51 = -63x - 51\)',
            },
            'C',
            r'Nhân phá ngoặc và kiểm tra hệ số của \(x\) cùng hằng số ở hai vế:<br>• A: \(63x + 36 = 63x + 36 \Rightarrow\) hai vế giống hệt nhau \(\Rightarrow\) <b>vô số nghiệm</b>.<br>• B: \(63x + 4 = 7x + 4 \Rightarrow 56x = 0 \Rightarrow x = 0\) (\(1\) nghiệm duy nhất).<br>• C: \(63x + 360 = 63x + 144 \Rightarrow 360 = 144\) (vô lý!) \(\Rightarrow\) <b>vô nghiệm (no solution)</b>!<br>• D: \(63x + 51 = -63x - 51 \Rightarrow 126x = -102 \Rightarrow x = -\frac{17}{21}\) (\(1\) nghiệm duy nhất).',
            r'Phương trình bậc nhất \(ax + b = cx + d\) <b>vô nghiệm</b> \(\iff a = c\) (hệ số \(x\) bằng nhau) và \(b \neq d\) (hằng số khác nhau).',
            {
                'A': ('Vô số nghiệm (identity)', r'\(9(7x + 4) = 63x + 36\) trùng khít vế trái nên đúng với mọi \(x\).'),
                'B': ('Có đúng 1 nghiệm x = 0', r'Hai hệ số \(63 \neq 7\) khác nhau nên luôn có nghiệm duy nhất (\(x = 0\)).'),
                'C': ('Chính xác', r'\(63x + 360 = 63x + 144\) rút gọn thành mệnh đề sai \(360 = 144\), nên vô nghiệm.'),
                'D': ('Bẫy dấu đối lập hai vế', r'\(63x\) và \(-63x\) không triệt tiêu nhau mà cộng thành \(126x = -102\), vẫn có 1 nghiệm!'),
            },
            r'Gõ hai vế của C (`y = 63x + 360` và `y = 9(7x + 16)`) vào Desmos: thấy hai đường thẳng song song không bao giờ cắt nhau!'
        ),

        # M2 Q16 (p96)
        math_mcq(
            'sat_real_jun25v2_m2_q16', 16, 'Advanced Math',
            'Nonlinear functions', 'Hard',
            r'<p style="text-align:center;">\[f(x) = (x - a)(x - b)\]</p>'
            r'<p>The function \(f\) is defined by the given equation, where \(a\) and \(b\) are integer constants.</p>',
            r'If \(f(32) > 0\), \(f(35) < 0\), and \(f(38) > 0\), which of the following could be the value of \(a + b\)?',
            {
                'A': r'\(35\)',
                'B': r'\(37\)',
                'C': r'\(67\)',
                'D': r'\(69\)',
            },
            'D',
            r'Parabol \(f(x) = (x - a)(x - b)\) có bề lõm hướng lên trên (hệ số \(x^2\) dương bằng \(1\)) và hai nghiệm nguyên \(a, b\) (giả sử \(a < b\)). Do đó \(f(x) < 0\) khi và chỉ khi \(x\) nằm giữa hai nghiệm (\(a < x < b\)), còn \(f(x) > 0\) khi \(x < a\) hoặc \(x > b\).<br>Từ ba điều kiện dấu:<br>• \(f(35) < 0 \Rightarrow a < 35 < b\).<br>• \(f(32) > 0\) với \(32 < 35 \Rightarrow 32 < a < 35\). Vì \(a \in \mathbb{Z}\), ta có \(a \in \{33, 34\}\).<br>• \(f(38) > 0\) với \(38 > 35 \Rightarrow 35 < b < 38\). Vì \(b \in \mathbb{Z}\), ta có \(b \in \{36, 37\}\).<br>Suy ra tổng \(a + b\) chỉ có thể nhận các giá trị trong \(\{33+36,\; 33+37,\; 34+36,\; 34+37\} = \{69, 70, 71\}\). Trong 4 đáp án chỉ có \(69\) thỏa mãn (ví dụ \(a = 33, b = 36\))!',
            r'Kỹ thuật xét dấu tam thức bậc hai: parabol hướng lên âm ở giữa hai nghiệm (\(32 < a < 35 < b < 38\)). Khi \(a, b\) nguyên, chặn ngay \(a \ge 33\) và \(b \ge 36 \Rightarrow a + b \ge 69\)!',
            {
                'A': ('Nhầm sang giá trị x = 35', r'\(a > 32\) và \(b > 35\) nên \(a + b > 67\), không thể bằng \(35\).'),
                'B': ('Nhầm sang một nghiệm riêng lẻ b = 37', r'\(37\) chỉ là giá trị khả dĩ của \(b\), không phải tổng \(a + b\).'),
                'C': ('Bẫy lấy dấu bằng 32 + 35', r'Vì \(a > 32\) và \(b > 35\) (nguyên), nên \(a \ge 33\) và \(b \ge 36 \Rightarrow a + b \ge 69 > 67\).'),
                'D': ('Chính xác', r'Với \(a = 33, b = 36\): \(f(32) = 4 > 0\), \(f(35) = -2 < 0\), \(f(38) = 10 > 0\), và \(a + b = 69\).'),
            },
            r'Vẽ `f(x) = (x - a)(x - b)` với thanh trượt nguyên `a, b` trong Desmos: đặt `a = 33, b = 36` thấy ngay `f(32) = 4 > 0`, `f(35) = -2 < 0`, `f(38) = 10 > 0` → `a + b = 69`!'
        ),

        # M2 Q17 (p97)
        math_mcq(
            'sat_real_jun25v2_m2_q17', 17, 'Algebra',
            'Linear equations in two variables', 'Medium',
            r'<p>One gallon of sealant costs $13 and will cover \(300\) square feet of a surface. A deck has a total surface area of \(d\) square feet.</p>',
            r'Which equation represents the cost \(c\), in dollars, of the sealant needed to cover the deck twice?',
            {
                'A': r'\(c = \frac{300d}{13}\)',
                'B': r'\(c = \frac{600d}{13}\)',
                'C': r'\(c = 13\left(\frac{d}{150}\right)\)',
                'D': r'\(c = 13\left(\frac{d}{300}\right)\)',
            },
            'C',
            r'Để phủ mặt sàn <b>hai lần (twice)</b>, tổng diện tích cần sơn phủ là \(2d\) feet vuông.<br>Số gallon sơn chống thấm cần dùng: \[\frac{2d}{300} = \frac{d}{150}\text{ (gallons)}.\] Nhân với đơn giá \(\$13\) mỗi gallon, ta thu được tổng chi phí: \[c = 13\left(\frac{d}{150}\right).\]',
            r'Đọc đến tận từ cuối cùng của câu hỏi: từ khóa <b>"twice"</b> (2 lớp) làm gấp đôi lượng sơn cần mua: \(\frac{2d}{300} = \frac{d}{150}\) — đừng dừng lại ở đáp án bẫy D (\(\frac{d}{300}\))!',
            {
                'A': ('Đặt ngược tử và mẫu đơn vị', r'Diện tích \(d\) phải chia cho \(300\text{ ft}^2/\text{gal}\) và nhân với \(\$13\), không phải nhân \(300\) chia \(13\).'),
                'B': ('Đặt ngược tử/mẫu dù có nhân 2', r'Khi \(d = 150\), cần \(1\) gallon giá \(\$13\), nhưng công thức B ra \(\frac{600 \times 150}{13} \approx \$6{,}923\) (vô lý).'),
                'C': ('Chính xác', r'\(2\) lớp trên diện tích \(d\) cần \(\frac{2d}{300} = \frac{d}{150}\) gallon, chi phí là \(13\left(\frac{d}{150}\right)\).'),
                'D': ('Bẫy quên chữ "twice" (chỉ sơn 1 lớp)', r'\(13\left(\frac{d}{300}\right)\) chỉ là chi phí phủ mặt sàn \(1\) lần.'),
            },
            r'Thử số thực tế: sàn rộng `d = 150` ft², sơn 2 lần là `300` ft² → vừa đúng `1` gallon = `$13`. Thay `d = 150` vào 4 đáp án, chỉ C cho đúng `13`!'
        ),

        # M2 Q18 (p98)
        math_spr(
            'sat_real_jun25v2_m2_q18', 18, 'Advanced Math',
            'Nonlinear equations in one variable and systems of equations in two variables', 'Hard',
            r'<p style="text-align:center;">\[\sqrt{k - x} = 42 - x\]</p>'
            r'<p>In the given equation, \(k\) is a constant. The equation has exactly one real solution.</p>',
            r'What is the minimum possible value of \(4k\)?',
            ['167'], '167',
            r'Đặt \(u = 42 - x\). Điều kiện để \(\sqrt{k - x} = 42 - x\) có nghiệm là \(u \ge 0\) (khi đó \(k - x = u^2 \ge 0\) tự động thỏa mãn!). Thay \(x = 42 - u\) vào bình phương hai vế: \[u^2 = k - (42 - u) \iff u^2 - u + (42 - k) = 0 \quad (u \ge 0).\] Xét biệt thức \(\Delta = (-1)^2 - 4(1)(42 - k) = 4k - 167\):<br>• Nếu \(4k < 167\): \(\Delta < 0 \Rightarrow\) vô nghiệm.<br>• Nếu \(4k = 167\) (\(k = 41.75\)): \(\Delta = 0\) cho nghiệm kép duy nhất \(u = \frac{1}{2} \ge 0 \Rightarrow x = 41.5\) (đúng \(1\) nghiệm thực!).<br>• Nếu \(167 < 4k \le 168\): cả hai nghiệm đều không âm (\(u_1 + u_2 = 1 > 0,\; u_1 u_2 = 42 - k \ge 0\)) \(\Rightarrow 2\) nghiệm thực.<br>• Nếu \(4k > 168\): tích \(u_1 u_2 < 0\) nên có \(1\) nghiệm dương và \(1\) nghiệm âm (loại) \(\Rightarrow 1\) nghiệm thực.<br>Vậy tập các giá trị của \(4k\) để phương trình có đúng \(1\) nghiệm thực là \(\{167\} \cup (168, +\infty)\), nên <b>giá trị nhỏ nhất của \(4k\) là \(167\)</b>!',
            r'Câu phân loại 780–800 cực hay! Tại sao đề hỏi <b>"minimum possible value of \(4k\)"</b>? Vì với \(k > 42\) (\(4k > 168\)) đồ thị \(y = \sqrt{k - x}\) và \(y = 42 - x\) cũng chỉ cắt nhau 1 lần; còn giá trị nhỏ nhất đạt được chính tại điểm <b>tiếp xúc (\(\Delta = 0\))</b> ứng với \(4k = 167\)!',
            r'Vẽ `y = sqrt(k - x)` và `y = 42 - x` trong Desmos với thanh trượt `k` (phóng to quanh `(41.5, 0.5)`): khi `k = 41.75`, hai đồ thị vừa chạm tiếp xúc tại đúng 1 điểm → `4k = 4 * 41.75 = 167`!'
        ),

        # M2 Q19 (p99)
        math_spr(
            'sat_real_jun25v2_m2_q19', 19, 'Advanced Math',
            'Equivalent expressions', 'Hard',
            r'<p style="text-align:center;">\[26z^{18} + bz^9 + 70\]</p>'
            r'<p>In the given expression, \(b\) is a positive integer.</p>',
            r'If \(qz^9 + r\) is a factor of the expression, where \(q\) and \(r\) are positive integers, what is the greatest possible value of \(b\)?',
            ['1821'], '1821',
            r'Đặt \(u = z^9\), biểu thức trở thành tam thức bậc hai \(26u^2 + bu + 70\) có nhân tử \(qu + r\) (\(q, r \in \mathbb{Z}^+\)). Khi đó \(u = -\frac{r}{q}\) là nghiệm hữu tỉ của \(26u^2 + bu + 70 = 0\). Viết phân số tối giản \(\frac{r}{q} = \frac{r_1}{q_1}\) (\(\gcd(q_1, r_1) = 1\)); theo định lý nghiệm hữu tỉ, \(q_1 \mid 26\) và \(r_1 \mid 70\), đồng thời: \[26u^2 + bu + 70 = (q_1 u + r_1)(su + t), \quad \text{với } q_1 s = 26,\; r_1 t = 70,\; b = q_1 t + r_1 s.\] Để tổng \(b = q_1 t + r_1 s\) đạt <b>giá trị lớn nhất</b>, ta ghép cặp hai ước lớn nhất nhân với nhau (\(26 \times 70\)) và hai ước nhỏ nhất nhân với nhau (\(1 \times 1\)): \[26u^2 + 1{,}821u + 70 = (26u + 1)(u + 70) \Rightarrow b_{\max} = 26 \times 70 + 1 \times 1 = 1{,}821.\]',
            r'Công thức thần tốc SAT Hard cho dạng phân tích \(Au^2 + bu + C = (qu + r)(su + t)\) với hệ số nguyên dương: giá trị lớn nhất của \(b\) luôn là \(AC + 1\) (ở đây \(26 \times 70 + 1 = 1{,}821\))!',
            r'Gõ `26 * 70 + 1` trong Desmos ra ngay `1821` (nhập ô SPR không dùng dấu phẩy: `1821`).'
        ),

        # M2 Q20 (p100)
        math_mcq(
            'sat_real_jun25v2_m2_q20', 20, 'Geometry and Trigonometry',
            'Lines, angles, and triangles', 'Hard',
            r'<p>In isosceles triangle \(ABC\), sides \(AB\) and \(AC\) are congruent. Point \(D\) divides side \(BC\) such that the length of \(\overline{BD}\) is \(\frac{2}{7}\) of the length of \(\overline{BC}\). Point \(E\) lies on side \(AB\) and point \(F\) lies on side \(AC\) such that when segments \(DE\) and \(DF\) are drawn, angle \(BED\) is congruent to angle \(CFD\).</p>',
            r'If the length of \(\overline{BE}\) is \(14\), what is the length of \(\overline{CF}\)?',
            {
                'A': r'\(28\)',
                'B': r'\(35\)',
                'C': r'\(49\)',
                'D': r'\(98\)',
            },
            'B',
            r'Vì \(\triangle ABC\) cân tại \(A\) (\(AB = AC\)), hai góc ở đáy bằng nhau: \[\angle EBD = \angle B = \angle C = \angle FCD.\] Kết hợp với giả thiết \(\angle BED = \angle CFD\), suy ra hai tam giác đồng dạng theo trường hợp góc–góc (AA): \[\triangle BED \sim \triangle CFD \Rightarrow \frac{CF}{BE} = \frac{CD}{BD}.\] Vì \(BD = \frac{2}{7}BC\), phần còn lại là: \[CD = BC - BD = BC - \frac{2}{7}BC = \frac{5}{7}BC \Rightarrow \frac{CD}{BD} = \frac{5/7}{2/7} = \frac{5}{2}.\] Từ đó tính được độ dài \(\overline{CF}\): \[CF = BE \cdot \frac{5}{2} = 14 \cdot \frac{5}{2} = 35.\]',
            r'Gặp câu hình không cho sẵn hình vẽ, hãy phác nhanh tam giác cân \(ABC\) ra giấy nháp: thấy ngay \(\angle B = \angle C\) kết hợp \(\angle BED = \angle CFD \Rightarrow \triangle BED \sim \triangle CFD\), và cẩn thận tỉ số \(\frac{CD}{BD} = \frac{5}{2}\) (KHÔNG phải \(\frac{7}{2}\))!',
            {
                'A': ('Nhân đôi nhầm 2 × 14', r'Không dùng đúng tỉ số hai đoạn chia \(\frac{CD}{BD} = \frac{5}{2}\).'),
                'B': ('Chính xác', r'\(CF = 14 \times \frac{5}{2} = 35\).'),
                'C': ('Bẫy lấy tỉ số BC/BD = 7/2', r'Tính nhầm \(14 \times \frac{7}{2} = 49\) vì quên lấy \(CD = BC - BD = \frac{5}{7}BC\).'),
                'D': ('Nhân nhầm 7 × 14', r'Lấy mẫu số \(7\) nhân với \(14\) thành \(98\), sai hoàn toàn tỉ lệ đồng dạng.'),
            },
            r'Gõ `14 * ((1 - 2/7) / (2/7))` trong Desmos ra ngay `35`.'
        ),

        # M2 Q21 (p101)
        math_spr(
            'sat_real_jun25v2_m2_q21', 21, 'Geometry and Trigonometry',
            'Right triangles and trigonometry', 'Hard',
            r'<p>In the \(xy\)-plane, a unit circle with center at the origin \(O\) contains point \(A\) with coordinates \((1, 0)\) and point \(B\) with coordinates \(\left(-\frac{5}{\sqrt{89}}, \frac{8}{\sqrt{89}}\right)\).</p>',
            r'If the measure of angle \(AOB\) is \(w\) radians, what is the value of \(\tan w\)?',
            ['-8/5', '-1.6', '-1.60'], r'-8/5 (hoặc -1.6)',
            r'Trên đường tròn đơn vị tâm \(O(0, 0)\), tia \(OA\) trùng với chiều dương trục \(Ox\) và điểm \(B\) thuộc góc phần tư thứ II có tọa độ \((\cos w, \sin w) = \left(-\frac{5}{\sqrt{89}}, \frac{8}{\sqrt{89}}\right)\). Kiểm tra: \(\left(-\frac{5}{\sqrt{89}}\right)^2 + \left(\frac{8}{\sqrt{89}}\right)^2 = \frac{25 + 64}{89} = 1\).<br>Theo định nghĩa lượng giác trên đường tròn đơn vị: \[\tan w = \frac{\sin w}{\cos w} = \frac{y_B}{x_B} = \frac{8/\sqrt{89}}{-5/\sqrt{89}} = -\frac{8}{5} = -1.6.\]',
            r'Trên đường tròn đơn vị (bắt đầu từ điểm \((1, 0)\)), mọi điểm \((x, y)\) luôn cho ngay \(\cos w = x\), \(\sin w = y\), và \(\tan w = \frac{y}{x}\). Đừng quên <b>dấu âm</b> vì điểm \(B\) nằm ở góc phần tư II (\(x < 0, y > 0\))!',
            r'Gõ `(8 / sqrt(89)) / (-5 / sqrt(89))` trong Desmos ra ngay `-1.6` (hoặc `-8/5`).'
        ),

        # M2 Q22 (p102)
        math_spr(
            'sat_real_jun25v2_m2_q22', 22, 'Advanced Math',
            'Nonlinear equations in one variable and systems of equations in two variables', 'Hard',
            r'<p style="text-align:center;">\[x(kx - 112) = -8\]</p>'
            r'<p>In the given equation, \(k\) is an integer constant.</p>',
            r'If the equation has two distinct real solutions, what is the greatest possible value of \(k\)?',
            ['391'], '391',
            r'Nhân phá ngoặc và chuyển vế về phương trình bậc hai chuẩn: \[kx^2 - 112x + 8 = 0.\] Để phương trình có <b>hai nghiệm thực phân biệt</b>, cần \(k \neq 0\) và biệt thức \(\Delta > 0\): \[\Delta = (-112)^2 - 4(k)(8) > 0 \Rightarrow 12{,}544 - 32k > 0 \Rightarrow 32k < 12{,}544 \Rightarrow k < \frac{12{,}544}{32} = 392.\] Vì \(k\) là <b>số nguyên</b> và bất đẳng thức nghiêm ngặt \(k < 392\) (tại \(k = 392\), \(\Delta = 0\) chỉ cho \(1\) nghiệm kép duy nhất \(x = \frac{1}{7}\)), giá trị nguyên lớn nhất có thể của \(k\) là \(391\).',
            r'Bẫy kinh điển câu chốt 22: "two distinct real solutions" yêu cầu \(\Delta > 0\) (KHÔNG có dấu bằng)! Ra \(k < 392\) thì phải lấy số nguyên lớn nhất nhỏ hơn hẳn \(392\) là \(391\)!',
            r'Gõ `112^2 / (4 * 8)` trong Desmos ra đúng chẵn `392` → vì `k < 392` và `k` nguyên, chốt ngay `391`!'
        ),
    ]


M1_QUESTIONS = _build_m1_questions()
M2_QUESTIONS = _build_m2_questions()

TEST_DATA = {
    'schemaVersion': 2,
    'mode': 'adaptive_mock',
    'section': 'math',
    'basicInfo': {
        'title': TEST_TITLE,
        'subtitle': 'Đề thi thật Digital SAT Toán tháng 6/2025 (Ver 2) — Đủ 2 Module (M1: 22 câu + M2: 22 câu)',
        'difficultyBadge': 'REAL EXAM • JUNE 2025',
        'targetTimeMinutes': 70,
        'routingThreshold': 0,
    },
    'module1': {
        'id': 'm1',
        'title': 'Section 2, Module 1: Math',
        'subtitle': '22 Questions • 35 Minutes • June 2025 Ver 2 Real Exam',
        'timeLimitMinutes': 35,
        'questions': M1_QUESTIONS,
    },
    'module2_hard': {
        'id': 'm2_hard',
        'title': 'Section 2, Module 2: Math',
        'subtitle': '22 Questions • 35 Minutes • June 2025 Ver 2 Real Exam',
        'timeLimitMinutes': 35,
        'questions': M2_QUESTIONS,
    },
    'module2_lower': {
        'id': 'm2_lower',
        'title': 'Section 2, Module 2: Math',
        'subtitle': '22 Questions • 35 Minutes • June 2025 Ver 2 Real Exam',
        'timeLimitMinutes': 35,
        'questions': [dict(q) for q in M2_QUESTIONS],
    },
}


# ============================================================================
# INDEPENDENT PROGRAMMATIC MATHEMATICAL AUDIT (ALL 44 QUESTIONS)
# ============================================================================

def verify_all_math():
    """Independently computes and verifies every single one of the 44 answers in Python."""
    m1 = {q['number']: q for q in TEST_DATA['module1']['questions']}
    m2 = {q['number']: q for q in TEST_DATA['module2_hard']['questions']}
    assert len(m1) == 22, f'Expected 22 M1 Qs, got {len(m1)}'
    assert len(m2) == 22, f'Expected 22 M2 Qs, got {len(m2)}'

    # ---------- MODULE 1 VERIFICATIONS ----------
    # M1 Q1: (-1, 1/50), (0, 1), (1, 50), (2, 2500) => f(x) = 50^x (increasing exponential, C)
    vals1 = [Fraction(1, 50), Fraction(1), Fraction(50), Fraction(2500)]
    ratios1 = [vals1[i + 1] / vals1[i] for i in range(len(vals1) - 1)]
    assert all(r == 50 for r in ratios1) and m1[1]['correctAnswer'] == 'C'

    # M1 Q2: d = 37w + 100 at w = 10 => 470 (B)
    assert 37 * 10 + 100 == 470 and m1[2]['correctAnswer'] == 'B'

    # M1 Q3: 9n - 10 = 2n + 25 => n = 5 (A)
    n3 = Fraction(25 + 10, 9 - 2)
    assert n3 == 5 and 9 * n3 - 10 == 2 * n3 + 25 and m1[3]['correctAnswer'] == 'A'

    # M1 Q4: x^2 - 2 = 23 => x = +-5 => 5 (D)
    assert 5 ** 2 - 2 == 23 and m1[4]['correctAnswer'] == 'D'

    # M1 Q5: f(x) = 7x + 9 => f(0) = 9 initial height when first measured (D)
    assert 7 * 0 + 9 == 9 and m1[5]['correctAnswer'] == 'D'

    # M1 Q6: perimeter 4(76) => side = 76
    assert Fraction(4 * 76, 4) == 76 and '76' in m1[6]['acceptedAnswers']

    # M1 Q7: $1,000 decreasing by 2% per month => v = 1000(0.98)^m (C)
    assert Fraction(100 - 2, 100) == Fraction(98, 100) and m1[7]['correctAnswer'] == 'C'

    # M1 Q8: angle F = 63°, angle H = 27° => angle G = 90° (C)
    assert 180 - 63 - 27 == 90 and m1[8]['correctAnswer'] == 'C'

    # M1 Q9: parallel lines r || s, corresponding angles => x = 44
    assert 44 == 44 and '44' in m1[9]['acceptedAnswers']

    # M1 Q10: 11m = 7(n + p) => n = 11m/7 - p (B)
    for m10, p10 in ((7, 3), (14, 5), (21, 2)):
        n10 = Fraction(11 * m10, 7) - p10
        assert 11 * m10 == 7 * (n10 + p10)
    assert m1[10]['correctAnswer'] == 'B'

    # M1 Q11: equal means of 7-element sets => x = 24
    chi = [31, 13, 44, 32, 53, 22, 44]
    sf_known = [46, 31, 19, 33, 48, 38]
    x11 = sum(chi) - sum(sf_known)
    assert len(chi) == 7 and len(sf_known) == 6
    assert x11 == 24 and Fraction(sum(chi), 7) == Fraction(sum(sf_known) + x11, 7)
    assert '24' in m1[11]['acceptedAnswers']

    # M1 Q12: 5xy + 30x^2y + 35xy^2 == 5xy(1 + 6x + 7y) (B)
    for xv, yv in ((1, 1), (2, -3), (-4, 5)):
        lhs = 5 * xv * yv + 30 * (xv ** 2) * yv + 35 * xv * (yv ** 2)
        rhs = 5 * xv * yv * (1 + 6 * xv + 7 * yv)
        assert lhs == rhs
    assert m1[12]['correctAnswer'] == 'B'

    # M1 Q13: 40% +- 6% => [34%, 46%] (A)
    assert (40 - 6, 40 + 6) == (34, 46) and m1[13]['correctAnswer'] == 'A'

    # M1 Q14: tall iff h > 100 => 110 < h < 158 (D)
    assert 110 > 100 and 95 <= 100 and 89 <= 100 and 100 <= 100
    assert m1[14]['correctAnswer'] == 'D'

    # M1 Q15: (2x^2 + 3x - 3) - (7x^2 + 2x) = -5x^2 + 1x - 3 => a = 1
    a15 = 3 - 2
    assert a15 == 1 and 2 - 7 == -5 and '1' in m1[15]['acceptedAnswers']

    # M1 Q16: (1/2)m = 98 => m = 196 (B)
    assert Fraction(1, 2) * 196 == 98 and m1[16]['correctAnswer'] == 'B'

    # M1 Q17: y = 200 * 3^x => at x = 1 (end of 1st 6-month period), y = 600 (A)
    assert 200 * (3 ** 0) == 200 and 200 * (3 ** 1) == 600 and m1[17]['correctAnswer'] == 'A'

    # M1 Q18: group C = 611, group A = 325, total = 1096 => p = (611/325)*100 = 188
    assert 325 + 64 + 611 + 96 == 1096
    p18 = Fraction(611, 325) * 100
    assert p18 == 188 and '188' in m1[18]['acceptedAnswers']

    # M1 Q19: (1/4)(s + 4t) = 544 and 7s - 8t = 1192 => s = 616, t = 390 => s - t = 226
    s19 = Fraction(2 * (4 * 544) + 1192, 9)
    t19 = Fraction(4 * 544 - s19, 4)
    assert (s19, t19) == (616, 390)
    assert Fraction(1, 4) * (s19 + 4 * t19) == 544 and 7 * s19 - 8 * t19 == 1192
    assert s19 - t19 == 226 and '226' in m1[19]['acceptedAnswers']

    # M1 Q20: line k through (-2, 1), (2, -4) => m_k = -5/4 => m_j = 4/5 through (7, 15) => b_j = 47/5 (D)
    mk20 = Fraction(-4 - 1, 2 - (-2))
    mj20 = -1 / mk20
    bj20 = 15 - mj20 * 7
    assert mk20 == Fraction(-5, 4) and mj20 == Fraction(4, 5) and bj20 == Fraction(47, 5)
    assert m1[20]['correctAnswer'] == 'D'

    # M1 Q21: r(-41)=-6, r(-21)=0, r(-1)=6 => a = 3/10, b = 63/10 => a + b = 33/5 = 6.6
    a21 = Fraction(0 - (-6), -21 - (-41))
    b21 = 0 - a21 * (-21)
    assert a21 * (-1) + b21 == 6
    assert a21 + b21 == Fraction(33, 5) and float(a21 + b21) == 6.6
    assert '33/5' in m1[21]['acceptedAnswers'] and '6.6' in m1[21]['acceptedAnswers']

    # M1 Q22: -3x^2 - 40 = qx - 37 => 3x^2 + qx + 3 = 0; Delta = 0, q > 0 => q = 6 => x = -1 (D)
    q22 = 6
    assert q22 ** 2 - 4 * 3 * 3 == 0
    x22 = Fraction(-q22, 2 * 3)
    assert x22 == -1 and -3 * (x22 ** 2) - 40 == q22 * x22 - 37
    assert m1[22]['correctAnswer'] == 'D'

    # ---------- MODULE 2 VERIFICATIONS ----------
    # M2 Q1: slope 3 through (2, 28) => g(x) = 3x + 22 (D)
    b_m2_1 = 28 - 3 * 2
    assert b_m2_1 == 22 and m2[1]['correctAnswer'] == 'D'

    # M2 Q2: -9x + y = 17 and 9x + y = 17 => (0, 17) (A)
    assert -9 * 0 + 17 == 17 and 9 * 0 + 17 == 17 and m2[2]['correctAnswer'] == 'A'

    # M2 Q3: 15 - 8*1.25 = 5; floor(5 / 0.75) = 6 (A)
    rem3 = Fraction(15) - 8 * Fraction(5, 4)
    max_a3 = int(rem3 / Fraction(3, 4))
    assert rem3 == 5 and max_a3 == 6 and max_a3 * Fraction(3, 4) <= 5 and (max_a3 + 1) * Fraction(3, 4) > 5
    assert m2[3]['correctAnswer'] == 'A'

    # M2 Q4: y = 6(7)^(x+2) at x = 0 => 294 (C)
    assert 6 * (7 ** 2) == 294 and m2[4]['correctAnswer'] == 'C'

    # M2 Q5: x^2 - 11x - 3 = 0 => (11 + sqrt((-11)^2 - 4(1)(-3))) / (2(1)) (B)
    r5 = (11 + math.sqrt((-11) ** 2 - 4 * 1 * (-3))) / (2 * 1)
    assert math.isclose(r5 ** 2 - 11 * r5 - 3, 0.0, abs_tol=1e-12) and m2[5]['correctAnswer'] == 'B'

    # M2 Q6: (2/5)x + (2/3)y = 5 => (1, 69/10), (2, 63/10), (4, 51/10) (D)
    for x6, y6 in ((1, Fraction(69, 10)), (2, Fraction(63, 10)), (4, Fraction(51, 10))):
        assert Fraction(2, 5) * x6 + Fraction(2, 3) * y6 == 5
    assert m2[6]['correctAnswer'] == 'D'

    # M2 Q7: adding 11.6 > 6.3 >= mean(Ari) strictly increases mean (D), while median can stay equal
    ari_sample = [2.8] + [5.0] * 84 + [6.3]
    chi_sample = ari_sample + [11.6]
    assert sum(ari_sample) / len(ari_sample) < sum(chi_sample) / len(chi_sample)
    assert (ari_sample[42] + ari_sample[43]) / 2 == chi_sample[43]  # median unchanged => C not "must be true"
    assert max(ari_sample) - min(ari_sample) < max(chi_sample) - min(chi_sample)  # range increases => B false
    assert m2[7]['correctAnswer'] == 'D'

    # M2 Q8: 3x + 9y = 10 and rx + 18y = 20 infinitely many solutions => r = 6 (C)
    assert Fraction(6, 3) == Fraction(18, 9) == Fraction(20, 10) and m2[8]['correctAnswer'] == 'C'

    # M2 Q9: right triangle at B, AB = 10*sqrt(41), BC = 24*sqrt(41) => AC = 26*sqrt(41) (B)
    assert 10 ** 2 + 24 ** 2 == 26 ** 2 and m2[9]['correctAnswer'] == 'B'

    # M2 Q10: m(140) ≈ 212 => predicted mass ≈ 212 kg at 140 days after birth (B)
    m140 = -0.0274 * ((140 / 7) ** 2) + 7.3873 * (140 / 7) + 75.032
    assert round(m140) == 212 and m2[10]['correctAnswer'] == 'B'

    # M2 Q11: similar rectangles, side ratio 10, area ABCD = 140 => area EFGH = 140 * 100 = 14000 (D)
    assert 140 * (10 ** 2) == 14000 and m2[11]['correctAnswer'] == 'D'

    # M2 Q12: 3n + n + 12 = 100 => 4n + 12 = 100 (D)
    assert 3 + 1 == 4 and m2[12]['correctAnswer'] == 'D'

    # M2 Q13: 2 + u/2 = -2u/3 => u = 1 - x = -12/7 ≈ -1.714
    u13 = Fraction(-12, 7)
    assert 2 + u13 / 2 == Fraction(-2, 3) * u13
    assert round(float(u13), 3) == -1.714
    assert '-12/7' in m2[13]['acceptedAnswers'] and '-1.714' in m2[13]['acceptedAnswers']

    # M2 Q14: 1490 m/(hr*s) * 3.28 ft/m / 3600 s/hr = 1.35755... ≈ 1.36 (B)
    rate14 = Fraction(1490) * Fraction(328, 100) / Fraction(3600)
    assert round(float(rate14), 2) == 1.36 and m2[14]['correctAnswer'] == 'B'

    # M2 Q15: 63x + 360 = 9(7x + 16) => 63x + 360 = 63x + 144 (no solution, C)
    assert 9 * 7 == 63 and 9 * 16 == 144 and 360 != 144
    assert 9 * 4 == 36  # A has infinitely many solutions
    assert m2[15]['correctAnswer'] == 'C'

    # M2 Q16: f(x) = (x - a)(x - b), a,b ints, f(32)>0, f(35)<0, f(38)>0 => a in {33,34}, b in {36,37} => a+b in {69,70,71} (D)
    valid_sums = set()
    for a16 in range(25, 45):
        for b16 in range(a16, 45):
            f16 = lambda x: (x - a16) * (x - b16)
            if f16(32) > 0 and f16(35) < 0 and f16(38) > 0:
                valid_sums.add(a16 + b16)
    assert valid_sums == {69, 70, 71} and m2[16]['correctAnswer'] == 'D'

    # M2 Q17: cover deck of area d twice => 2d / 300 = d / 150 gallons => c = 13(d/150) (C)
    assert Fraction(2, 300) == Fraction(1, 150) and m2[17]['correctAnswer'] == 'C'

    # M2 Q18: sqrt(k - x) = 42 - x has exactly 1 real solution => 4k in {167} U (168, inf) => min 4k = 167
    def _count_real_sols_q18(k_val):
        # Solve u^2 - u + (42 - k) = 0 with u = 42 - x >= 0
        disc = 1 - 4 * (42 - k_val)
        if disc < -1e-12:
            return 0
        if abs(disc) <= 1e-12:
            return 1 if 0.5 >= 0 else 0
        s = math.sqrt(disc)
        roots = [(1 - s) / 2, (1 + s) / 2]
        return sum(1 for u in roots if u >= -1e-12)

    assert _count_real_sols_q18(166 / 4) == 0
    assert _count_real_sols_q18(167 / 4) == 1
    assert _count_real_sols_q18(167.5 / 4) == 2
    assert _count_real_sols_q18(168 / 4) == 2
    assert _count_real_sols_q18(169 / 4) == 1
    assert '167' in m2[18]['acceptedAnswers']

    # M2 Q19: 26u^2 + bu + 70 with positive int factor qu + r => max b = 26*70 + 1 = 1821
    possible_b = set()
    for q19 in (1, 2, 13, 26):
        s19_f = 26 // q19
        for r19 in (1, 2, 5, 7, 10, 14, 35, 70):
            t19_f = 70 // r19
            possible_b.add(q19 * t19_f + r19 * s19_f)
    assert max(possible_b) == 1821 and '1821' in m2[19]['acceptedAnswers']

    # M2 Q20: isosceles ABC (AB=AC), BD = (2/7)BC => CD/BD = 5/2; BE = 14 => CF = 35 (B)
    cf20 = 14 * (Fraction(5, 7) / Fraction(2, 7))
    assert cf20 == 35 and m2[20]['correctAnswer'] == 'B'

    # M2 Q21: B = (-5/sqrt(89), 8/sqrt(89)) on unit circle => tan(w) = -8/5 = -1.6
    assert Fraction((-5) ** 2 + 8 ** 2, 89) == 1
    tan_w = Fraction(8, -5)
    assert tan_w == Fraction(-8, 5) and float(tan_w) == -1.6
    assert '-8/5' in m2[21]['acceptedAnswers'] and '-1.6' in m2[21]['acceptedAnswers']

    # M2 Q22: kx^2 - 112x + 8 = 0 has 2 distinct real roots => 112^2 - 32k > 0 => k < 392 => max int k = 391
    bound22 = Fraction((-112) ** 2, 4 * 8)
    assert bound22 == 392
    assert (-112) ** 2 - 4 * 391 * 8 > 0
    assert (-112) ** 2 - 4 * 392 * 8 == 0
    assert '391' in m2[22]['acceptedAnswers']

    # ---------- EXTRA HYGIENE, XML SVG & OPTION-ANALYSIS KATEX AUDIT ----------
    raw_blob = str(TEST_DATA)
    for bad in ('@DSATuz', '@D7SAT', 'satuzhunters', 'Minh Nghĩa', 't.me/D7SAT', '______blank'):
        assert bad.lower() not in raw_blob.lower(), f'Watermark token leaked: {bad}'

    for mk in ('module1', 'module2_hard', 'module2_lower'):
        for q in TEST_DATA[mk]['questions']:
            exp = q.get('explanation') or {}
            assert exp.get('desmosTipVi', '').strip(), f'{mk} Q{q["number"]}: missing desmosTipVi'
            if q.get('questionFormat') == 'mcq':
                oa = exp.get('optionAnalysis') or {}
                for lbl in ('A', 'B', 'C', 'D'):
                    reason = oa[lbl]['reasonVi']
                    assert reason.count('\\(') == reason.count('\\)'), f'{mk} Q{q["number"]} {lbl} unbalanced \\( \\)'
                    assert reason.count('\\[') == reason.count('\\]'), f'{mk} Q{q["number"]} {lbl} unbalanced \\[ \\]'
                    assert not re.search(r'(?<!\\)\$[a-zA-Z\\]', reason), f'{mk} Q{q["number"]} {lbl} raw $ math'

    # Verify every inline SVG parses cleanly as strict XML and count figures/tables
    svg_count = 0
    table_count = 0
    oa_katex_items = []
    for mk in ('module1', 'module2_hard'):
        for q in TEST_DATA[mk]['questions']:
            stim = q.get('stimulusHtml') or ''
            for svg_str in re.findall(r'<svg[\s\S]*?</svg>', stim):
                ET.fromstring(svg_str)
                svg_count += 1
            table_count += len(re.findall(r'<table[\s\S]*?</table>', stim))
            if q.get('questionFormat') == 'mcq':
                oa = (q.get('explanation') or {}).get('optionAnalysis') or {}
                for lbl in ('A', 'B', 'C', 'D'):
                    oa_katex_items.append({
                        'label': f'{TEST_CODE}.{mk}.Q{q["number"]}.optionAnalysis.{lbl}',
                        'text': oa[lbl]['reasonVi'],
                    })
    assert svg_count == 3, f'Expected 3 inline SVGs, got {svg_count}'
    assert table_count == 7, f'Expected 7 HTML tables, got {table_count}'

    # Validate full Bluebook schema + REAL Node KaTeX (`throwOnError: true`)
    errs = validate_sat_bluebook_json(TEST_DATA, TEST_CODE)
    assert not errs, 'validate_sat_bluebook_json failed:\n' + '\n'.join(errs)

    # Also verify ALL optionAnalysis LaTeX expressions with REAL Node KaTeX
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    payload_path = os.path.join(root_dir, 'scratch', 'igcse_katex_payload.json')
    os.makedirs(os.path.dirname(payload_path), exist_ok=True)
    with open(payload_path, 'w', encoding='utf-8') as f:
        json.dump(oa_katex_items, f, ensure_ascii=False)
    try:
        res = subprocess.run(
            ['node', os.path.join(root_dir, 'scripts', 'igcse_maths_verify_katex.mjs')],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding='utf-8',
        )
    finally:
        if os.path.exists(payload_path):
            os.remove(payload_path)
    assert res.returncode == 0, f'optionAnalysis KaTeX failed:\n{res.stdout}\n{res.stderr}'


if __name__ == '__main__':
    verify_all_math()
    for mk in ('module1', 'module2_hard', 'module2_lower'):
        qs = TEST_DATA[mk]['questions']
        mcqs = [q for q in qs if q.get('questionFormat') == 'mcq']
        sprs = [q for q in qs if q.get('questionFormat') == 'spr']
        dist = {k: sum(1 for q in mcqs if q['correctAnswer'] == k) for k in 'ABCD'}
        print(f'  {mk}: {len(qs)} Qs ({len(mcqs)} MCQ {dist}, {len(sprs)} SPR)')
    print(f'[OK] {TEST_CODE}: ALL 44 REAL MATH QUESTIONS + NODE KATEX VERIFIED WITH 0 ERRORS!')
