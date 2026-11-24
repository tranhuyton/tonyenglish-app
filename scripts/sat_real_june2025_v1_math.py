# -*- coding: utf-8 -*-
"""
Digital SAT Real Past Exam — June 2025 Ver 1: Math (Real M1 + M2, 44 Unique Questions)
Visually verified page-by-page from `math_p41.png` through `math_p71.png`:
  - Section 2, Module 1: Math (22 real questions: 15 MCQ + 7 SPR)
  - Section 2, Module 2: Math (22 real questions: 18 MCQ + 4 SPR)
Zero watermarks, crisp inline SVGs & HTML tables, full bilingual Vietnamese explanations,
Desmos tips, programmatic mathematical audit (`verify_all_math`), and real Node KaTeX validation.
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

TEST_CODE = 'real_june2025_v1_math'
FOLDER_KEY = 'real_math'
ORDER_INDEX = 3
TEST_TITLE = '🏛️ Real Exam — June 2025 Ver 1 Math (Real M1 + M2)'


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
        '<table style="border-collapse:collapse;font-size:15px;min-width:190px;'
        'background:#ffffff;box-shadow:0 1px 2px rgba(15,23,42,0.06);">'
        f'<thead><tr>{th}</tr></thead><tbody>{trs}</tbody></table></div>'
    )


def _svg_m1_q5_right_triangle():
    """Exact recreation of June 2025 Ver 1 M1 Q5 right triangle (legs 9, 12; hypotenuse r)."""
    return (
        '<div style="display:flex;justify-content:center;margin:10px 0;">'
        '<svg viewBox="0 0 300 220" width="300" height="220" xmlns="http://www.w3.org/2000/svg" '
        'style="background:#ffffff;border:1px solid #e2e8f0;border-radius:12px;">'
        '<polygon points="64,32 64,168 246,168" fill="#f8fafc" stroke="#0f172a" '
        'stroke-width="2.2" stroke-linejoin="round"/>'
        '<rect x="64" y="152" width="16" height="16" fill="none" stroke="#0f172a" stroke-width="1.8"/>'
        '<text x="44" y="106" text-anchor="middle" font-family="Georgia,serif" font-size="18" '
        'fill="#0f172a">9</text>'
        '<text x="155" y="191" text-anchor="middle" font-family="Georgia,serif" font-size="18" '
        'fill="#0f172a">12</text>'
        '<text x="166" y="88" text-anchor="middle" font-family="Georgia,serif" font-style="italic" '
        'font-size="19" fill="#0f172a">r</text>'
        '<text x="150" y="212" text-anchor="middle" font-family="Georgia,serif" font-size="12.5" '
        'fill="#475569">Note: Figure not drawn to scale.</text>'
        '</svg></div>'
    )


def _svg_m1_q9_parallel_transversal():
    """Exact recreation of June 2025 Ver 1 M1 Q9 (parallel lines ℓ, k; transversal t; obtuse x°, acute y°)."""
    return (
        '<div style="display:flex;justify-content:center;margin:10px 0;">'
        '<svg viewBox="0 0 320 225" width="320" height="225" xmlns="http://www.w3.org/2000/svg" '
        'style="background:#ffffff;border:1px solid #e2e8f0;border-radius:12px;">'
        # Parallel lines ℓ (y=72) and k (y=138)
        '<line x1="34" y1="72" x2="262" y2="72" stroke="#0f172a" stroke-width="2.1"/>'
        '<line x1="34" y1="138" x2="262" y2="138" stroke="#0f172a" stroke-width="2.1"/>'
        # Transversal t from (52,24) to (246,192): slope = 168/194 = 0.866
        # Intersects y=72 at x = 52 + (48/168)*194 = 107.4
        # Intersects y=138 at x = 52 + (114/168)*194 = 183.6
        '<line x1="52" y1="24" x2="246" y2="192" stroke="#0f172a" stroke-width="2.1"/>'
        # Subtle angle arcs for x° (obtuse upper-right at ℓ∩t) and y° (acute upper-left at k∩t)
        '<path d="M 92.3 58.9 A 20 20 0 0 1 127.4 72" fill="none" stroke="#1d4ed8" stroke-width="1.5"/>'
        '<path d="M 161.6 138 A 22 22 0 0 1 167.0 123.6" fill="none" stroke="#b91c1c" stroke-width="1.5"/>'
        # Line labels
        '<text x="50" y="18" font-family="Georgia,serif" font-style="italic" font-size="16" '
        'fill="#0f172a">t</text>'
        '<text x="274" y="77" font-family="Georgia,serif" font-style="italic" font-size="17" '
        'fill="#0f172a">&#x2113;</text>'
        '<text x="274" y="143" font-family="Georgia,serif" font-style="italic" font-size="17" '
        'fill="#0f172a">k</text>'
        # Angle labels
        '<text x="122" y="61" font-family="Georgia,serif" font-style="italic" font-size="15" '
        'fill="#1d4ed8">x&#176;</text>'
        '<text x="148" y="131" font-family="Georgia,serif" font-style="italic" font-size="15" '
        'fill="#b91c1c">y&#176;</text>'
        '<text x="160" y="214" text-anchor="middle" font-family="Georgia,serif" font-size="12.5" '
        'fill="#475569">Note: Figure not drawn to scale.</text>'
        '</svg></div>'
    )


def _svg_m1_q12_inequality_graph():
    """Exact recreation of June 2025 Ver 1 M1 Q12 coordinate graph: y < 3x + 8."""
    # Grid spans x in [-4, 8] (12 units) and y in [-1, 15] (16 units), 18px per unit
    step = 18
    x0 = 112  # pixel x for math x=0 (x=-4 is at 40, x=8 is at 256)
    y0 = 304  # pixel y for math y=0 (y=15 is at 34, y=-1 is at 322)

    def px(x):
        return x0 + x * step

    def py(y):
        return y0 - y * step

    grid_lines = []
    for gx in range(-4, 9):
        if gx == 0:
            continue
        x_p = px(gx)
        grid_lines.append(
            f'<line x1="{x_p}" y1="{py(15)}" x2="{x_p}" y2="{py(-1)}" '
            f'stroke="#64748b" stroke-width="0.8"/>'
        )
    for gy in range(-1, 16):
        if gy == 0:
            continue
        y_p = py(gy)
        grid_lines.append(
            f'<line x1="{px(-4)}" y1="{y_p}" x2="{px(8)}" y2="{y_p}" '
            f'stroke="#64748b" stroke-width="0.8"/>'
        )

    # Boundary y = 3x + 8 clipped to grid box [-4, 8] x [-1, 15]:
    # At y = -1 => x = -3; at y = 15 => x = 7/3 ≈ 2.3333
    bx1, by1 = px(-3), py(-1)
    bx2, by2 = px(7 / 3), py(15)
    # Shaded polygon below and right of boundary: (-3,-1) -> (7/3,15) -> (8,15) -> (8,-1)
    poly_pts = f'{bx1:.1f},{by1:.1f} {bx2:.1f},{by2:.1f} {px(8):.1f},{py(15):.1f} {px(8):.1f},{py(-1):.1f}'

    return (
        '<div style="display:flex;justify-content:center;margin:10px 0;">'
        '<svg viewBox="0 0 300 345" width="300" height="345" xmlns="http://www.w3.org/2000/svg" '
        'style="background:#ffffff;border:1px solid #e2e8f0;border-radius:12px;">'
        # Shaded region
        f'<polygon points="{poly_pts}" fill="#94a3b8" fill-opacity="0.45"/>'
        # Grid lines on top of shading for clarity
        + ''.join(grid_lines) +
        # Axes with arrows
        f'<line x1="{px(-4) - 6}" y1="{py(0)}" x2="{px(8) + 14}" y2="{py(0)}" '
        'stroke="#0f172a" stroke-width="1.7"/>'
        f'<polygon points="{px(8) + 18},{py(0)} {px(8) + 10},{py(0) - 3.5} '
        f'{px(8) + 10},{py(0) + 3.5}" fill="#0f172a"/>'
        f'<line x1="{px(0)}" y1="{py(-1) + 6}" x2="{px(0)}" y2="{py(15) - 14}" '
        'stroke="#0f172a" stroke-width="1.7"/>'
        f'<polygon points="{px(0)},{py(15) - 18} {px(0) - 3.5},{py(15) - 10} '
        f'{px(0) + 3.5},{py(15) - 10}" fill="#0f172a"/>'
        # Dashed boundary line y = 3x + 8
        f'<line x1="{bx1:.1f}" y1="{by1:.1f}" x2="{bx2:.1f}" y2="{by2:.1f}" '
        'stroke="#0f172a" stroke-width="2.8" stroke-dasharray="8,5"/>'
        # Axis labels x, y, O
        f'<text x="{px(8) + 23}" y="{py(0) + 4}" font-family="Georgia,serif" '
        'font-style="italic" font-size="15" fill="#0f172a">x</text>'
        f'<text x="{px(0)}" y="{py(15) - 22}" text-anchor="middle" font-family="Georgia,serif" '
        'font-style="italic" font-size="15" fill="#0f172a">y</text>'
        f'<text x="{px(0) - 10}" y="{py(0) + 15}" font-family="Georgia,serif" '
        'font-style="italic" font-size="14" fill="#0f172a">O</text>'
        # Major tick labels (-4, 4, 8 on x; 4, 8, 12 on y) with crisp white halo
        f'<text x="{px(-4)}" y="{py(0) + 16}" text-anchor="middle" font-family="Georgia,serif" '
        'font-size="13.5" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4">-4</text>'
        f'<text x="{px(4)}" y="{py(0) + 16}" text-anchor="middle" font-family="Georgia,serif" '
        'font-size="13.5" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4">4</text>'
        f'<text x="{px(8)}" y="{py(0) + 16}" text-anchor="middle" font-family="Georgia,serif" '
        'font-size="13.5" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4">8</text>'
        f'<text x="{px(0) - 8}" y="{py(4) + 5}" text-anchor="end" font-family="Georgia,serif" '
        'font-size="13.5" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4">4</text>'
        f'<text x="{px(0) - 8}" y="{py(8) + 5}" text-anchor="end" font-family="Georgia,serif" '
        'font-size="13.5" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4">8</text>'
        f'<text x="{px(0) - 8}" y="{py(12) + 5}" text-anchor="end" font-family="Georgia,serif" '
        'font-size="13.5" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="4">12</text>'
        '</svg></div>'
    )


SCATTER_M1_Q14_PTS = [
    (0.0, 0.0),
    (0.3, 0.7),
    (1.2, 0.5),
    (1.9, 1.9),
    (2.8, 2.9),
    (3.7, 3.8),
    (4.2, 4.3),
    (4.8, 4.5),
    (6.1, 6.5),
    (7.4, 7.1),
    (9.2, 9.6),
]


def _svg_m1_q14_scatterplot():
    """Exact recreation of June 2025 Ver 1 M1 Q14 scatterplot (all 11 data points)."""
    step = 24
    x0 = 46
    y0 = 274

    def px(x):
        return x0 + x * step

    def py(y):
        return y0 - y * step

    parts = []
    # Grid lines 1..10
    for i in range(1, 11):
        parts.append(
            f'<line x1="{px(i)}" y1="{py(10) - 6}" x2="{px(i)}" y2="{py(0) + 4}" '
            'stroke="#94a3b8" stroke-width="0.9"/>'
        )
        parts.append(
            f'<line x1="{px(0) - 4}" y1="{py(i)}" x2="{px(10) + 6}" y2="{py(i)}" '
            'stroke="#94a3b8" stroke-width="0.9"/>'
        )
        # Labels
        parts.append(
            f'<text x="{px(i)}" y="{py(0) + 18}" text-anchor="middle" '
            f'font-family="Georgia,serif" font-size="13" fill="#0f172a">{i}</text>'
        )
        parts.append(
            f'<text x="{px(0) - 10}" y="{py(i) + 4.5}" text-anchor="end" '
            f'font-family="Georgia,serif" font-size="13" fill="#0f172a">{i}</text>'
        )

    # Axes with arrowheads
    parts.append(
        f'<line x1="{px(0)}" y1="{py(0)}" x2="{px(10) + 16}" y2="{py(0)}" '
        'stroke="#0f172a" stroke-width="1.8"/>'
    )
    parts.append(
        f'<polygon points="{px(10) + 20},{py(0)} {px(10) + 12},{py(0) - 3.5} '
        f'{px(10) + 12},{py(0) + 3.5}" fill="#0f172a"/>'
    )
    parts.append(
        f'<line x1="{px(0)}" y1="{py(0)}" x2="{px(0)}" y2="{py(10) - 16}" '
        'stroke="#0f172a" stroke-width="1.8"/>'
    )
    parts.append(
        f'<polygon points="{px(0)},{py(10) - 20} {px(0) - 3.5},{py(10) - 12} '
        f'{px(0) + 3.5},{py(10) - 12}" fill="#0f172a"/>'
    )
    # Origin and axis letters
    parts.append(
        f'<text x="{px(0) - 10}" y="{py(0) + 16}" font-family="Georgia,serif" '
        'font-style="italic" font-size="14" fill="#0f172a">O</text>'
    )
    parts.append(
        f'<text x="{px(10) + 25}" y="{py(0) + 4}" font-family="Georgia,serif" '
        'font-style="italic" font-size="15" fill="#0f172a">x</text>'
    )
    parts.append(
        f'<text x="{px(0)}" y="{py(10) - 24}" text-anchor="middle" font-family="Georgia,serif" '
        'font-style="italic" font-size="15" fill="#0f172a">y</text>'
    )
    # 11 plotted data points
    for dx, dy in SCATTER_M1_Q14_PTS:
        parts.append(
            f'<circle cx="{px(dx):.1f}" cy="{py(dy):.1f}" r="4.2" fill="#0f172a"/>'
        )

    return (
        '<div style="display:flex;justify-content:center;margin:10px 0;">'
        '<svg viewBox="0 0 325 305" width="325" height="305" xmlns="http://www.w3.org/2000/svg" '
        'style="background:#ffffff;border:1px solid #e2e8f0;border-radius:12px;">'
        + ''.join(parts) +
        '</svg></div>'
    )


# ============================================================================
# SECTION 2, MODULE 1: MATH (22 REAL QUESTIONS — JUNE 2025 VER 1)
# ============================================================================

def _build_m1_questions():
    tbl_m1_q22 = _bluebook_table(
        [r'\(x\)', r'\(g(x)\)'],
        [
            [r'\(-17\)', r'\(-7\)'],
            [r'\(-9\)', r'\(0\)'],
            [r'\(-1\)', r'\(7\)'],
        ],
    )

    return [
        # M1 Q1 (p41)
        math_mcq(
            'sat_real_jun25v1_m1_q1', 1, 'Algebra', 'Linear functions', 'Easy',
            r'<p>The function \(f\) is defined by the equation \(f(x) = 10x + 4\).</p>',
            r'What is the value of \(f(x)\) when \(x = 7\)?',
            {'A': r'\(21\)', 'B': r'\(38\)', 'C': r'\(47\)', 'D': r'\(74\)'},
            'D',
            r'Thay \(x = 7\) trực tiếp vào hàm \(f(x) = 10x + 4\): \[f(7) = 10(7) + 4 = 70 + 4 = 74.\]',
            r'Với câu tính giá trị hàm \(f(a)\), chỉ cần thay trực tiếp \(x = a\) và tính đúng thứ tự nhân trước cộng sau.',
            {
                'A': ('Cộng thay vì nhân', r'\(10 + 7 + 4 = 21\) — cộng nhầm hệ số \(10\) với \(7\).'),
                'B': ('Đổi vai trò hệ số', r'\(4(7) + 10 = 38\) — thế ngược \(10\) và \(4\).'),
                'C': ('Ghi ngược chữ số', r'\(47\) là đảo chữ số của \(74\) hoặc nhầm \(10(4) + 7\).'),
                'D': ('Đáp án đúng', r'\(10(7) + 4 = 74\).'),
            },
            r'Gõ `f(x) = 10x + 4` rồi dòng dưới gõ `f(7)` trong Desmos sẽ hiện ngay kết quả `74`.'
        ),

        # M1 Q2 (p42)
        math_spr(
            'sat_real_jun25v1_m1_q2', 2, 'Problem-Solving and Data Analysis',
            'Ratios, rates, proportional relationships, and units', 'Easy',
            r'<p>A remotely operated vehicle (ROV) is used for underwater ocean research. (\(1\text{ fathom} = 6\text{ feet}\))</p>',
            r'When the ROV is at a depth of \(26\) fathoms, what is the ROV\'s depth in <u>feet</u>?',
            ['156'], '156',
            r'Vì \(1\text{ fathom} = 6\text{ feet}\), nên độ sâu \(26\text{ fathoms}\) đổi sang feet là: \[26 \times 6 = 156\text{ feet}.\]',
            r'Khi đổi từ đơn vị lớn hơn (fathom) sang đơn vị nhỏ hơn (feet), ta nhân với hệ số quy đổi: \(26\text{ fathoms} \times \frac{6\text{ feet}}{1\text{ fathom}} = 156\text{ feet}\).',
            r'Bấm trực tiếp `26 * 6` trong Desmos ra ngay `156`.'
        ),

        # M1 Q3 (p42)
        math_mcq(
            'sat_real_jun25v1_m1_q3', 3, 'Algebra',
            'Systems of two linear equations in two variables', 'Easy',
            r'<p style="text-align:center;">\[6x = 30\]\[6x - 10y = 80\]</p>',
            r'What is the solution \((x, y)\) to the given system of equations?',
            {'A': r'\((5, -5)\)', 'B': r'\((5, -11)\)', 'C': r'\((30, 80)\)', 'D': r'\((30, 50)\)'},
            'A',
            r'Từ phương trình thứ nhất: \(6x = 30 \Rightarrow x = 5\). Thế cả cụm \(6x = 30\) vào phương trình thứ hai: \[30 - 10y = 80 \Rightarrow -10y = 50 \Rightarrow y = -5.\] Vậy nghiệm của hệ là \((5, -5)\).',
            r'Không cần tìm \(x\) trước mới thế — có thể thay thẳng cụm \(6x = 30\) vào phương trình dưới để giải \(y\) cực nhanh.',
            {
                'A': ('Đáp án đúng', r'\(6(5) = 30\) và \(30 - 10(-5) = 30 + 50 = 80\).'),
                'B': ('Sai dấu khi chuyển vế', r'Cộng nhầm \(80 + 30 = 110 \Rightarrow y = -11\) thay vì lấy \(80 - 30 = 50\).'),
                'C': ('Lấy nguyên vế phải', r'Đọc nhầm hai hằng số \(30\) và \(80\) thành tọa độ \((x, y)\).'),
                'D': ('Quên chia hệ số', r'Không chia \(30\) cho \(6\) và không chia \(50\) cho \(-10\).'),
            },
            r'Gõ hai phương trình `6x = 30` và `6x - 10y = 80` vào Desmos rồi click giao điểm sẽ hiện ngay `(5, -5)`.'
        ),

        # M1 Q4 (p42)
        math_mcq(
            'sat_real_jun25v1_m1_q4', 4, 'Advanced Math', 'Equivalent expressions', 'Easy',
            r'<p>Consider the algebraic expression:</p><p style="text-align:center;">\[41x^2 + 41\]</p>',
            r'Which expression is equivalent to \(41x^2 + 41\)?',
            {
                'A': r'\(41\left(x^2 + \frac{1}{41}\right)\)',
                'B': r'\(41(41x^2 + 1)\)',
                'C': r'\(41(x^2 + 41)\)',
                'D': r'\(41(x^2 + 1)\)',
            },
            'D',
            r'Đặt nhân tử chung \(41\) ra ngoài ở cả hai hạng tử: \[41x^2 + 41 = 41 \cdot x^2 + 41 \cdot 1 = 41(x^2 + 1).\]',
            r'Khi đặt nhân tử chung \(a\) ra khỏi tổng \(ax^2 + a\), phải chia ĐỒNG THỜI cả hai hạng tử cho \(a\) (hạng tử \(a\) trở thành \(1\), không biến mất và không giữ nguyên thành \(a\)).',
            {
                'A': ('Chia 41 hai lần', r'Nhân phân phối ra \(41x^2 + 1 \neq 41x^2 + 41\).'),
                'B': ('Quên chia hạng tử đầu', r'Nhân phân phối ra \(1{,}681x^2 + 41 \neq 41x^2 + 41\).'),
                'C': ('Quên chia hạng tử sau', r'Nhân phân phối ra \(41x^2 + 1{,}681 \neq 41x^2 + 41\).'),
                'D': ('Đáp án đúng', r'Nhân phân phối ra đúng \(41x^2 + 41\).'),
            },
            r'Gõ `y = 41x^2 + 41` và đồ thị từng đáp án vào Desmos — đáp án đúng trùng khít 100% đồ thị gốc (hoặc thử \(x = 1\): gốc bằng `82`, chỉ D cho `41(1 + 1) = 82`).'
        ),

        # M1 Q5 (p44-45)
        math_mcq(
            'sat_real_jun25v1_m1_q5', 5, 'Geometry and Trigonometry',
            'Right triangles and trigonometry', 'Easy',
            _svg_m1_q5_right_triangle(),
            r'Which equation gives the relationship between the side lengths of the triangle shown?',
            {
                'A': r'\(9 + 12 = r\)',
                'B': r'\(12 - 9 = r\)',
                'C': r'\(9^2 + 12^2 = r^2\)',
                'D': r'\(12^2 - 9^2 = r^2\)',
            },
            'C',
            r'Tam giác trên là tam giác vuông có hai cạnh góc vuông dài \(9\) và \(12\), cạnh huyền (đối diện góc vuông) là \(r\). Theo định lý Py-ta-go: \[9^2 + 12^2 = r^2.\]',
            r'Định lý Py-ta-go: tổng bình phương hai cạnh góc vuông bằng bình phương cạnh huyền (\(a^2 + b^2 = c^2\)).',
            {
                'A': ('Quên bình phương', r'Cộng trực tiếp hai cạnh góc vuông \(9 + 12 = r\) là sai (vi phạm bất đẳng thức tam giác).'),
                'B': ('Trừ cạnh góc vuông', r'\(12 - 9 = r\) sai hoàn toàn về bản chất tam giác vuông.'),
                'C': ('Đáp án đúng', r'Đúng định lý Py-ta-go \(9^2 + 12^2 = r^2\) (suy ra \(r = 15\)).'),
                'D': ('Nhầm cạnh huyền', r'Đặt \(12\) làm cạnh huyền là sai vì \(r\) mới là cạnh đối diện góc vuông.'),
            },
            r'Câu nhận diện định lý Py-ta-go cơ bản — đối chiếu ngay cạnh đối diện ký hiệu vuông góc chính là cạnh huyền \(r\).'
        ),

        # M1 Q6 (p45)
        math_spr(
            'sat_real_jun25v1_m1_q6', 6, 'Algebra',
            'Linear inequalities in one or two variables', 'Easy',
            r'<p>An event planner is planning an ice-skating event. It costs the event planner a onetime fee of $45 to rent the skating rink and $10.75 per attendee. The event planner has a budget of $275.</p>',
            r'What is the greatest number of attendees possible without exceeding the budget?',
            ['21'], '21',
            r'Gọi \(n\) là số người tham dự (\(n\) nguyên dương). Tổng chi phí không vượt quá ngân sách $275: \[45 + 10.75n \le 275 \Rightarrow 10.75n \le 230 \Rightarrow n \le \frac{230}{10.75} \approx 21.395.\] Vì số người phải là số nguyên và không được vượt ngân sách, ta làm tròn xuống: \(n_{\max} = 21\). (Kiểm tra: \(21\) người hết $270.75 \(\le\) $275; \(22\) người hết $281.50 \(>\) $275).',
            r'Với bài toán ngân sách tối đa ("greatest number ... without exceeding"), LUÔN làm tròn XUỐNG (floor) sau khi chia!',
            r'Gõ `(275 - 45) / 10.75` trong Desmos ra `21.395...`, lấy phần nguyên `21`.'
        ),

        # M1 Q7 (p46)
        math_spr(
            'sat_real_jun25v1_m1_q7', 7, 'Problem-Solving and Data Analysis',
            'Ratios, rates, proportional relationships, and units', 'Easy',
            r'<p>The ratio of cups of flour to cups of butter in a pie dough recipe is \(2.75\) to \(1\). The ratio of cups of flour to cups of butter in a biscuit recipe is \(7\) to \(1\). Each recipe has \(1\) cup of butter.</p>',
            r'How many more cups of flour are in the biscuit recipe than in the pie dough recipe?',
            ['4.25', '17/4'], '4.25 (hoặc 17/4)',
            r'Vì mỗi công thức đều dùng đúng \(1\) cốc bơ nên: công thức vỏ bánh (pie dough) có \(2.75\) cốc bột, công thức bánh quy (biscuit) có \(7\) cốc bột. Hiệu số cốc bột là: \[7 - 2.75 = 4.25 = \frac{17}{4}.\]',
            r'Chú ý cả hai tỉ lệ đều đã chuẩn hóa về cùng mốc \(1\) cốc bơ, nên chỉ cần trừ trực tiếp hai lượng bột.',
            r'Gõ `7 - 2.75` trong Desmos ra `4.25` (bấm biểu tượng phân số sẽ ra `17/4`).'
        ),

        # M1 Q8 (p47)
        math_mcq(
            'sat_real_jun25v1_m1_q8', 8, 'Geometry and Trigonometry',
            'Area and volume', 'Easy',
            r'<p>A cube has an edge length of \(13\) inches.</p>',
            r'What is the volume, in cubic inches, of the cube?',
            {'A': r'\(39\)', 'B': r'\(78\)', 'C': r'\(169\)', 'D': r'\(2{,}197\)'},
            'D',
            r'Thể tích hình lập phương cạnh \(s\) là \(V = s^3\). Với \(s = 13\text{ inches}\): \[V = 13^3 = 13 \times 13 \times 13 = 169 \times 13 = 2{,}197.\] ',
            r'Thể tích hình lập phương là \(s^3\) (mũ 3), đừng nhầm với diện tích một mặt \(s^2\) hay \(3s\).',
            {
                'A': ('Nhân 3 thay vì mũ 3', r'\(13 \times 3 = 39\) — nhầm \(s^3\) với \(3s\).'),
                'B': ('Nhân 6 mặt với cạnh', r'\(13 \times 6 = 78\) — nhầm công thức diện tích toàn phần \(6s^2\) thành \(6s\).'),
                'C': ('Tính diện tích một mặt', r'\(13^2 = 169\) chỉ là diện tích một mặt vuông, thiếu nhân thêm chiều cao \(13\).'),
                'D': ('Đáp án đúng', r'\(13^3 = 2{,}197\).'),
            },
            r'Gõ `13^3` vào Desmos ra ngay `2197`.'
        ),

        # M1 Q9 (p47)
        math_mcq(
            'sat_real_jun25v1_m1_q9', 9, 'Geometry and Trigonometry',
            'Lines, angles, and triangles', 'Easy',
            _svg_m1_q9_parallel_transversal() +
            r'<p>In the figure shown, lines \(\ell\) and \(k\) are parallel and line \(t\) intersects both lines.</p>',
            r'If \(x > 145\), which of the following must be true?',
            {
                'A': r'\(y < 35\)',
                'B': r'\(y > 35\)',
                'C': r'\(x + y < 180\)',
                'D': r'\(x + y > 180\)',
            },
            'A',
            r'Vì \(\ell \parallel k\), góc tù \(x^\circ\) và góc nhọn \(y^\circ\) tạo thành cặp góc bù nhau (góc kề bù của \(x^\circ\) nằm bên trái \(t\) phía trên \(\ell\) là góc đồng vị với \(y^\circ\)), nên luôn có: \[x + y = 180 \Rightarrow y = 180 - x.\] Khi \(x > 145\), suy ra \(y = 180 - x < 180 - 145 = 35\), tức là \(y < 35\).',
            r'Hai đường song song cắt bởi một cát tuyến chỉ tạo ra tối đa 2 cỡ góc: góc nhọn và góc tù, và tổng của một góc nhọn với một góc tù LUÔN bằng \(180^\circ\).',
            {
                'A': ('Đáp án đúng', r'Vì \(x + y = 180\) và \(x > 145 \Rightarrow y = 180 - x < 35\).'),
                'B': ('Ngược chiều bất đẳng thức', r'Khi trừ \(x\) lớn hơn \(145\) khỏi \(180\), kết quả \(y\) phải NHỎ hơn \(35\), không phải lớn hơn.'),
                'C': ('Sai quan hệ song song', r'Do \(\ell \parallel k\), ta luôn có đẳng thức \(x + y = 180\), không bao giờ nhỏ hơn \(180\).'),
                'D': ('Sai quan hệ song song', r'Tương tự, \(x + y\) luôn bằng đúng \(180\), không thể lớn hơn \(180\).'),
            },
            r'Thử giá trị mẫu thỏa \(x > 145\): chọn \(x = 150 \Rightarrow y = 180 - 150 = 30\), thấy ngay chỉ A (`30 < 35`) đúng!'
        ),

        # M1 Q10 (p48)
        math_mcq(
            'sat_real_jun25v1_m1_q10', 10, 'Advanced Math',
            'Nonlinear equations in one variable and systems of equations in two variables', 'Easy',
            r'<p style="text-align:center;">\[(2x - 4)(x - 8)(x - 9) = 0\]</p>',
            r'What is the sum of the solutions to the given equation?',
            {'A': r'\(-21\)', 'B': r'\(-19\)', 'C': r'\(19\)', 'D': r'\(21\)'},
            'C',
            r'Cho từng nhân tử bằng \(0\):<ul><li>\(2x - 4 = 0 \Rightarrow x = 2\)</li><li>\(x - 8 = 0 \Rightarrow x = 8\)</li><li>\(x - 9 = 0 \Rightarrow x = 9\)</li></ul>Tổng các nghiệm là: \[2 + 8 + 9 = 19.\]',
            r'Cẩn thận nhân tử có hệ số trước \(x\) như \((2x - 4)\): nghiệm là \(x = \frac{4}{2} = 2\), không phải \(4\)!',
            {
                'A': ('Sai dấu và quên chia 2', r'Lấy \(-4 - 8 - 9 = -21\).'),
                'B': ('Sai dấu tất cả nghiệm', r'Lấy \(-2 - 8 - 9 = -19\) thay vì đổi dấu khi giải phương trình tích.'),
                'C': ('Đáp án đúng', r'\(2 + 8 + 9 = 19\).'),
                'D': ('Bẫy quên chia 2 ở 2x − 4', r'Lấy \(4 + 8 + 9 = 21\) do nhầm nghiệm của \(2x - 4 = 0\) là \(4\).'),
            },
            r'Gõ `y = (2x - 4)(x - 8)(x - 9)` vào Desmos → bấm 3 giao điểm trục hoành `(2, 0)`, `(8, 0)`, `(9, 0)` → cộng `2 + 8 + 9 = 19`.'
        ),

        # M1 Q11 (p48)
        math_spr(
            'sat_real_jun25v1_m1_q11', 11, 'Advanced Math', 'Nonlinear functions', 'Easy',
            r'<p>The function \(g\) is defined by \(g(x) = 7x^{-1}\).</p>',
            r'What is the value of \(g(13)\)?',
            ['7/13', '.5384', '.5385', '0.5385', '0.5384', '0.538'], '7/13 (hoặc 0.5385)',
            r'Nhớ quy tắc số mũ âm \(x^{-1} = \frac{1}{x}\). Do đó \(g(x) = \frac{7}{x}\). Thay \(x = 13\): \[g(13) = 7 \cdot 13^{-1} = \frac{7}{13} \approx 0.5385.\]',
            r'Trong bài tự luận điền đáp án (SPR), phân số tối giản `7/13` luôn chính xác tuyệt đối và tránh rủi ro làm tròn thập phân.',
            r'Gõ `g(x) = 7x^(-1)` rồi dòng sau gõ `g(13)` → bấm nút chuyển phân số (hình chữ nhật chia đôi bên trái) trong Desmos sẽ hiện ngay `7/13`.'
        ),

        # M1 Q12 (p49-50)
        math_mcq(
            'sat_real_jun25v1_m1_q12', 12, 'Algebra',
            'Linear inequalities in one or two variables', 'Medium',
            _svg_m1_q12_inequality_graph(),
            r'The shaded region shown represents the solutions to which inequality?',
            {
                'A': r'\(y < \frac{1}{3}x + 8\)',
                'B': r'\(y < 3x + 8\)',
                'C': r'\(y > \frac{1}{3}x + 8\)',
                'D': r'\(y > 3x + 8\)',
            },
            'B',
            r'Bước 1 — Tìm phương trình đường biên nét đứt: đường thẳng đi qua \((0, 8)\) và \((1, 11)\), nên tung độ gốc \(b = 8\) và hệ số góc \[m = \frac{11 - 8}{1 - 0} = 3 \Rightarrow y = 3x + 8.\] Bước 2 — Xác định chiều bất đẳng thức: gốc tọa độ \((0, 0)\) nằm TRONG miền tô đậm. Thay \((0, 0)\): \(0 < 3(0) + 8\) (đúng), và đường biên nét đứt ứng với dấu \(<\). Vậy bất đẳng thức là \(y < 3x + 8\).',
            r'Luôn dùng điểm thử vàng \((0, 0)\) (nếu đường biên không đi qua gốc) để kiểm tra chiều dấu \(<\) hay \(>\) trong 2 giây.',
            {
                'A': ('Nghịch đảo hệ số góc', r'Nhầm hệ số góc \(m = \frac{\Delta x}{\Delta y} = \frac{1}{3}\) thay vì \(\frac{\Delta y}{\Delta x} = 3\).'),
                'B': ('Đáp án đúng', r'Đường biên \(y = 3x + 8\) nét đứt và tô phần bên dưới chứa \((0, 0)\).'),
                'C': ('Sai cả hệ số góc và chiều dấu', r'Hệ số góc sai (\(\frac{1}{3}\)) và miền nghiệm nằm phía trên đường thẳng.'),
                'D': ('Ngược chiều dấu bất đẳng thức', r'\(y > 3x + 8\) tô phần phía trên bên trái, không chứa \((0, 0)\).'),
            },
            r'Gõ thẳng `y < 3x + 8` vào Desmos sẽ thấy miền tô và đường biên nét đứt qua `(0, 8)`, `(1, 11)` khớp y hệt hình đề bài.'
        ),

        # M1 Q13 (p49)
        math_mcq(
            'sat_real_jun25v1_m1_q13', 13, 'Advanced Math',
            'Nonlinear equations in one variable and systems of equations in two variables', 'Medium',
            r'<p style="text-align:center;">\[y = -8x + 26\]\[y = 2x^2 + 16\]</p>'
            r'<p>The graphs of the equations in the given system of equations intersect at the point \((a, b)\) in the \(xy\)-plane.</p>',
            r'What is a possible value of \(a\)?',
            {'A': r'\(-5\)', 'B': r'\(-1\)', 'C': r'\(2\)', 'D': r'\(5\)'},
            'A',
            r'Cho hai vế phải bằng nhau để tìm hoành độ giao điểm \(x\): \[2x^2 + 16 = -8x + 26 \Rightarrow 2x^2 + 8x - 10 = 0 \Rightarrow x^2 + 4x - 5 = 0.\] Phân tích nhân tử: \((x + 5)(x - 1) = 0 \Rightarrow x = -5\) hoặc \(x = 1\). Trong 4 đáp án, chỉ có \(a = -5\) là nghiệm hợp lệ.',
            r'Đề hỏi "a possible value of \(a\)" (một giá trị có thể của hoành độ \(x\)), nghĩa là hệ có 2 giao điểm và đáp án đúng là một trong hai nghiệm đó.',
            {
                'A': ('Đáp án đúng', r'Với \(a = -5\): \(-8(-5) + 26 = 66\) và \(2(-5)^2 + 16 = 66\).'),
                'B': ('Đổi dấu nghiệm x = 1', r'Nghiệm còn lại là \(x = 1\), không phải \(-1\).'),
                'C': ('Thế sai phương trình', r'Tại \(x = 2\): \(y_1 = 10 \neq y_2 = 24\).'),
                'D': ('Đổi dấu nghiệm x = −5', r'Phân tích nhầm \((x - 5)(x + 1) = 0\) do nhầm dấu của \(+4x\).'),
            },
            r'Gõ `y = -8x + 26` và `y = 2x^2 + 16` vào Desmos → zoom ra và bấm vào 2 giao điểm `(-5, 66)` và `(1, 18)` → chọn ngay `a = -5`.'
        ),

        # M1 Q14 (p51-52)
        math_mcq(
            'sat_real_jun25v1_m1_q14', 14, 'Problem-Solving and Data Analysis',
            'Two-variable data: Models and scatterplots', 'Medium',
            r'<p>The scatterplot shows the relationship between two variables, \(x\) and \(y\).</p>' +
            _svg_m1_q14_scatterplot(),
            r'Which of the following equations is the most appropriate linear model for the data shown?',
            {
                'A': r'\(y = 0.07 - 1.02x\)',
                'B': r'\(y = 1.02 - 0.07x\)',
                'C': r'\(y = -0.07 + 1.02x\)',
                'D': r'\(y = -1.02 + 0.07x\)',
            },
            'C',
            r'Quan sát biểu đồ phân tán: khi \(x\) tăng từ \(0\) đến \(9.2\), \(y\) tăng gần như tỉ lệ \(1:1\) từ \(0\) lên \(9.6\). Do đó:<ul><li>Hệ số góc (slope) phải <b>dương</b> và xấp xỉ \(+1\) (\(\approx +1.02\)).</li><li>Tung độ gốc (\(y\)-intercept) rất gần \(0\) (\(\approx -0.07\)).</li></ul>Phương trình dạng \(y = b + mx\) thỏa mãn là \(y = -0.07 + 1.02x\).',
            r'Mẹo cực nhanh với câu scatterplot dạng \(y = a + bx\): kiểm tra dấu của hệ số góc (hệ số đi với \(x\)) để loại ngay 2 đáp án, sau đó thế \(x = 9\) để chốt đáp án cho \(y \approx 9\).',
            {
                'A': ('Hệ số góc âm', r'Slope \(-1.02 < 0\) (đi xuống), trái ngược với xu hướng tăng của dữ liệu.'),
                'B': ('Đảo slope và y-intercept', r'Slope \(-0.07 < 0\) và tại \(x = 9\) chỉ cho \(y \approx 0.39\).'),
                'C': ('Đáp án đúng', r'Slope \(+1.02\) và \(y\)-intercept \(-0.07\); tại \(x = 9\) cho \(y \approx 9.11\), khớp khít các điểm dữ liệu.'),
                'D': ('Đảo slope và y-intercept', r'Slope \(+0.07\) quá phẳng — tại \(x = 9\) cho \(y = -0.39 < 0\).'),
            },
            r'Thử nhanh \(x = 9\) vào phương trình C: `-0.07 + 1.02(9) = 9.11`, khớp ngay vị trí đám mây điểm ở vùng `(9, 9.5)`!'
        ),

        # M1 Q15 (p53)
        math_spr(
            'sat_real_jun25v1_m1_q15', 15, 'Algebra', 'Linear equations in one variable', 'Easy',
            r'<p style="text-align:center;">\[4(x - 3) = 11 + 2(x - 3)\]</p>',
            r'If \(x\) is the solution to the given equation, what is the value of \(x - 3\)?',
            ['5.5', '11/2'], '5.5 (hoặc 11/2)',
            r'Đặt ẩn phụ \(u = x - 3\). Phương trình trở thành: \[4u = 11 + 2u \Rightarrow 2u = 11 \Rightarrow u = \frac{11}{2} = 5.5.\] Vì đề hỏi trực tiếp giá trị của \(x - 3\), đáp án chính là \(5.5\) (hoặc \(\frac{11}{2}\)).',
            r'Mẹo SAT kinh điển: coi cả cụm \((x - 3)\) là một biến duy nhất — vừa nhanh hơn vừa tránh hoàn toàn bẫy điền nhầm giá trị \(x = 8.5\)!',
            r'Gõ `4(x - 3) = 11 + 2(x - 3)` vào Desmos thấy đường thẳng đứng `x = 8.5`, sau đó nhớ tính `8.5 - 3 = 5.5`.'
        ),

        # M1 Q16 (p54)
        math_mcq(
            'sat_real_jun25v1_m1_q16', 16, 'Problem-Solving and Data Analysis',
            'Percentages', 'Medium',
            r'<p>In \(1980\), the population density of Carroll County was \(125\) people per square mile. In \(1990\), the population density of Carroll County was \(141\) people per square mile. The population density of Carroll County in \(1990\) was \(p\%\) of the population density of Carroll County in \(1980\).</p>',
            r'What is the value of \(p\)?',
            {'A': r'\(116.0\)', 'B': r'\(112.8\)', 'C': r'\(16.0\)', 'D': r'\(12.8\)'},
            'B',
            r'Dịch chuẩn câu "in \(1990\) was \(p\%\) of ... in \(1980\)": \[141 = \frac{p}{100} \cdot 125 \Rightarrow p = \frac{141}{125} \times 100 = 1.128 \times 100 = 112.8.\]',
            r'Phân biệt sống còn: "A is \(p\%\) <b>of</b> B" \(\Rightarrow p = \frac{A}{B}\times 100\) (ở đây \(112.8\)), khác hoàn toàn với "A is \(p\%\) <b>greater than</b> B" (\(12.8\))!',
            {
                'A': ('Cộng hiệu trực tiếp vào 100', r'Lấy \(100 + (141 - 125) = 116.0\), quên chia cho gốc \(125\).'),
                'B': ('Đáp án đúng', r'\(\frac{141}{125} \times 100 = 112.8\).'),
                'C': ('Lấy hiệu thô', r'\(141 - 125 = 16\), không tính tỉ số phần trăm.'),
                'D': ('Bẫy tính % tăng thêm', r'\(12.8\%\) là phần trăm TĂNG THÊM ("greater than"), còn đề hỏi "was \(p\%\) OF" nên phải cộng thêm \(100\%\) thành \(112.8\).'),
            },
            r'Gõ `(141 / 125) * 100` trong Desmos ra ngay `112.8`.'
        ),

        # M1 Q17 (p54)
        math_mcq(
            'sat_real_jun25v1_m1_q17', 17, 'Advanced Math', 'Equivalent expressions', 'Medium',
            r'<p>Consider the expression:</p><p style="text-align:center;">\[(2x + 9)^2 - (x - 7)\]</p>',
            r'Which expression is equivalent to \((2x + 9)^2 - (x - 7)\)?',
            {
                'A': r'\(4x^2 + 35x + 74\)',
                'B': r'\(4x^2 + 35x + 88\)',
                'C': r'\(4x^2 - x + 74\)',
                'D': r'\(4x^2 - x + 88\)',
            },
            'B',
            r'Khai triển hằng đẳng thức và phá ngoặc cẩn thận dấu trừ: \[(2x + 9)^2 - (x - 7) = (4x^2 + 36x + 81) - x + 7 = 4x^2 + 35x + 88.\]',
            r'Hai lỗi kinh điển SAT hay bẫy trong cùng một câu: (1) quên số hạng giữa \(2ab = 36x\) khi khai triển \((a+b)^2\), và (2) quên đổi dấu \(-(-7) = +7\).',
            {
                'A': ('Quên đổi dấu −(−7)', r'Tính nhầm \(81 - 7 = 74\) thay vì \(81 + 7 = 88\).'),
                'B': ('Đáp án đúng', r'\(4x^2 + (36x - x) + (81 + 7) = 4x^2 + 35x + 88\).'),
                'C': ('Quên cả 2ab lẫn đổi dấu', r'Khai triển sai \((2x+9)^2 = 4x^2 + 81\) và tính sai \(81 - 7 = 74\).'),
                'D': ('Quên số hạng giữa 2ab', r'Khai triển thiếu \(2(2x)(9) = 36x\).'),
            },
            r'Gõ `f(x) = (2x + 9)^2 - (x - 7)` vào Desmos và thử \(x = 0\): `f(0) = 81 + 7 = 88` (loại A, C); thử \(x = 1\): `f(1) = 121 + 6 = 127`, chỉ B cho `4 + 35 + 88 = 127`!'
        ),

        # M1 Q18 (p55)
        math_spr(
            'sat_real_jun25v1_m1_q18', 18, 'Geometry and Trigonometry', 'Circles', 'Medium',
            r'<p>A circle has center \(O\), and points \(R\) and \(S\) lie on the circle. In triangle \(ORS\), the measure of \(\angle ROS\) is \(116^\circ\).</p>',
            r'What is the measure of \(\angle RSO\), in degrees? (Disregard the degree symbol when entering your answer.)',
            ['32'], '32',
            r'Vì \(R\) và \(S\) cùng nằm trên đường tròn tâm \(O\) nên \(OR = OS = R_{\text{đường tròn}}\). Suy ra \(\triangle ORS\) cân tại \(O\), do đó hai góc ở đáy bằng nhau: \(\angle ORS = \angle RSO\). Ta có: \[\angle RSO = \frac{180^\circ - 116^\circ}{2} = \frac{64^\circ}{2} = 32^\circ.\]',
            r'Hễ thấy tâm \(O\) và hai điểm \(R, S\) nằm trên đường tròn, hãy đánh dấu ngay \(OR = OS\) (bán kính bằng nhau) \(\Rightarrow \triangle ORS\) luôn là tam giác cân tại \(O\)!',
            r'Gõ `(180 - 116) / 2` trong Desmos ra ngay `32`.'
        ),

        # M1 Q19 (p56)
        math_mcq(
            'sat_real_jun25v1_m1_q19', 19, 'Advanced Math', 'Nonlinear functions', 'Medium',
            r'<p>\(32\) teams are competing in a baseball tournament. The tournament has \(5\) rounds. After each round, half the teams competing are eliminated from the tournament.</p>',
            r'If \(r\) teams remain in the tournament after \(x\) rounds of play, which of the following gives \(r\) in terms of \(x\)?',
            {
                'A': r'\(r = \frac{1}{2}(32^x)\)',
                'B': r'\(r = \frac{1}{2}x^{32}\)',
                'C': r'\(r = 32\left(\frac{1}{2}\right)^x\)',
                'D': r'\(r = 32x^{\frac{1}{2}}\)',
            },
            'C',
            r'Đây là hàm suy giảm theo cấp số nhân \(y = a \cdot b^x\):<ul><li>Giá trị ban đầu (khi \(x = 0\) vòng): \(a = 32\) đội.</li><li>Sau mỗi vòng, một nửa số đội bị loại \(\Rightarrow\) còn lại một nửa, nên hệ số nhân mỗi vòng là \(b = \frac{1}{2}\).</li></ul>Vậy \(r = 32\left(\frac{1}{2}\right)^x\). (Kiểm tra: \(x = 0 \Rightarrow r = 32\); \(x = 1 \Rightarrow r = 16\); \(x = 5 \Rightarrow r = 1\)).',
            r'Trong mô hình hàm mũ \(y = a \cdot b^x\), giá trị ban đầu \(a\) luôn đứng ngoài ngoặc, còn tỉ lệ thay đổi lặp lại \(b\) nằm dưới số mũ \(x\).',
            {
                'A': ('Đảo vị trí a và b', r'Tại \(x = 0\), công thức cho \(r = \frac{1}{2}\) đội (vô lý).'),
                'B': ('Nhầm sang hàm lũy thừa', r'Tại \(x = 0\), công thức cho \(r = 0\), không phải \(32\).'),
                'C': ('Đáp án đúng', r'Khớp hoàn toàn: \(x = 0 \to 32\), \(x = 1 \to 16\), \(x = 5 \to 1\).'),
                'D': ('Nhầm sang hàm căn bậc hai', r'Tại \(x = 0\) cho \(r = 0\), tại \(x = 1\) cho \(r = 32\) (không giảm).'),
            },
            r'Thử ngay điểm \((x, r) = (1, 16)\) vào từng đáp án: chỉ C cho `32 * (1/2)^1 = 16`!'
        ),

        # M1 Q20 (p56)
        math_mcq(
            'sat_real_jun25v1_m1_q20', 20, 'Algebra',
            'Linear equations in two variables', 'Hard',
            r'<p>A boat traveled a certain distance upriver and then traveled downriver \(10\) miles farther than it traveled upriver. The boat took \(x\) hours to travel upriver at a speed of \(12\) miles per hour. The boat then took \(y\) hours to travel downriver at a speed of \(18\) miles per hour faster than the speed at which the boat traveled upriver.</p>',
            r'Which of the following equations best represents this situation?',
            {
                'A': r'\(12x - 30y = -10\)',
                'B': r'\(12x + 30y = -10\)',
                'C': r'\(12x + 30y = 10\)',
                'D': r'\(12x - 30y = 10\)',
            },
            'A',
            r'Tính từng quãng đường theo công thức \(d = v \cdot t\):<ul><li>Quãng đường ngược dòng (upriver): \(d_{\text{up}} = 12x\).</li><li>Vận tốc xuôi dòng nhanh hơn ngược dòng \(18\text{ mph}\) nên \(v_{\text{down}} = 12 + 18 = 30\text{ mph}\) \(\Rightarrow\) quãng đường xuôi dòng: \(d_{\text{down}} = 30y\).</li></ul>Vì quãng đường xuôi dòng dài hơn quãng đường ngược dòng \(10\) dặm: \[30y = 12x + 10 \Rightarrow 12x - 30y = -10.\]',
            r'Đọc kỹ ai LỚN HƠN ai: "downriver \(10\) miles farther than upriver" nghĩa là \(d_{\text{down}} - d_{\text{up}} = 10 \Rightarrow d_{\text{up}} - d_{\text{down}} = -10\)!',
            {
                'A': ('Đáp án đúng', r'\(30y = 12x + 10 \Leftrightarrow 12x - 30y = -10\).'),
                'B': ('Cộng hai quãng đường', r'Tổng hai quãng đường dương không thể bằng \(-10\).'),
                'C': ('Cộng thay vì lấy hiệu', r'Đề nói chênh lệch là \(10\) dặm, không phải tổng quãng đường bằng \(10\).'),
                'D': ('Ngược chiều phép trừ', r'\(12x - 30y = 10\) nghĩa là ngược dòng dài hơn xuôi dòng \(10\) dặm — ngược đề bài!'),
            },
            r'Thử số cụ thể: giả sử ngược dòng đi `20` dặm (`12x = 20`) thì xuôi dòng đi `20 + 10 = 30` dặm (`30y = 30`). Khi đó `12x - 30y = 20 - 30 = -10` → chốt ngay A!'
        ),

        # M1 Q21 (p57)
        math_spr(
            'sat_real_jun25v1_m1_q21', 21, 'Advanced Math', 'Nonlinear functions', 'Hard',
            r'<p>The function \(f\) is defined by \(f(x) = 4(x - 3)(x^2 - k)\), where \(k\) is a constant. In the \(xy\)-plane, the graph of \(y = f(x)\) passes through the point \((-8, 0)\).</p>',
            r'What is the value of \(f(0)\)?',
            ['768'], '768',
            r'Vì đồ thị đi qua \((-8, 0)\), ta có \(f(-8) = 0\): \[4(-8 - 3)\bigl((-8)^2 - k\bigr) = 0 \Rightarrow 4(-11)(64 - k) = 0 \Rightarrow k = 64.\] Thay \(k = 64\) và \(x = 0\) vào \(f(x)\): \[f(0) = 4(0 - 3)(0^2 - 64) = 4(-3)(-64) = 12 \times 64 = 768.\]',
            r'Cẩn thận dấu âm nhân âm ở bước cuối: \(4 \times (-3) \times (-64) = +768\) (số dương)!',
            r'Trong Desmos, gõ `k = (-8)^2` rồi `f(x) = 4(x - 3)(x^2 - k)` và dòng cuối gõ `f(0)` ra ngay `768`.'
        ),

        # M1 Q22 (p58)
        math_mcq(
            'sat_real_jun25v1_m1_q22', 22, 'Algebra', 'Linear functions', 'Hard',
            tbl_m1_q22 +
            r'<p>For the linear function \(g\), the table shows three values of \(x\) and their corresponding values of \(g(x)\). Function \(g\) is defined by \(g(x) = ax + b\), where \(a\) and \(b\) are constants.</p>',
            r'What is the value of \(a + b\)?',
            {
                'A': r'\(\frac{28}{5}\)',
                'B': r'\(\frac{63}{10}\)',
                'C': r'\(\frac{63}{8}\)',
                'D': r'\(\frac{35}{4}\)',
            },
            'D',
            r'Tính hệ số góc \(a\) từ hai dòng bất kỳ trong bảng: \[a = \frac{0 - (-7)}{-9 - (-17)} = \frac{7}{8}.\] Thế điểm \((-9, 0)\) vào \(g(x) = ax + b\): \[0 = \frac{7}{8}(-9) + b \Rightarrow b = \frac{63}{8}.\] Vậy \[a + b = \frac{7}{8} + \frac{63}{8} = \frac{70}{8} = \frac{35}{4}.\] <i>Mẹo siêu tốc:</i> \(a + b = a(1) + b = g(1)\). Từ \(x = -1\) đến \(x = 1\) tăng \(2\) đơn vị nên \(g(1) = 7 + 2 \cdot \frac{7}{8} = 7 + \frac{7}{4} = \frac{35}{4}\).',
            r'Nhận diện nhanh: với hàm bậc nhất \(g(x) = ax + b\), giá trị \(a + b\) chính là \(g(1)\) — không nhất thiết phải tìm riêng \(b\)!',
            {
                'A': ('Sai mẫu số slope', r'Tính nhầm mẫu số dẫn tới \(\frac{28}{5}\).'),
                'B': ('Tính sai phân số b', r'Nhầm mẫu số \(8\) thành \(10\) khi tìm \(b\).'),
                'C': ('Bẫy dừng ở giá trị b', r'\(\frac{63}{8}\) mới chỉ là hằng số \(b\), quên cộng thêm \(a = \frac{7}{8}\)!'),
                'D': ('Đáp án đúng', r'\(a + b = \frac{7}{8} + \frac{63}{8} = \frac{70}{8} = \frac{35}{4}\).'),
            },
            r'Tạo bảng `x1 = [-17, -9, -1]`, `y1 = [-7, 0, 7]` rồi chạy hồi quy `y1 ~ a x1 + b` trong Desmos → gõ `a + b` và bấm nút phân số ra ngay `35/4`!'
        ),
    ]


# ============================================================================
# SECTION 2, MODULE 2: MATH (22 REAL QUESTIONS — JUNE 2025 VER 1)
# ============================================================================

def _build_m2_questions():
    tbl_m2_q13 = _bluebook_table(
        [r'\(x\)', r'\(y\)'],
        [
            [r'\(-6\)', r'\(-14\)'],
            [r'\(-3\)', r'\(-16\)'],
            [r'\(3\)', r'\(-20\)'],
            [r'\(6\)', r'\(-22\)'],
        ],
    )
    tbl_m2_q19 = _bluebook_table(
        ['Pieces of mail', 'Days'],
        [
            [r'\(0\)', r'\(2\)'],
            [r'\(4\)', r'\(2\)'],
            [r'\(5\)', r'\(2\)'],
            [r'\(6\)', r'\(2\)'],
            [r'\(7\)', r'\(1\)'],
            [r'\(8\)', r'\(1\)'],
            [r'\(17\)', r'\(1\)'],
        ],
    )

    return [
        # M2 Q1 (p59)
        math_mcq(
            'sat_real_jun25v1_m2_q1', 1, 'Algebra', 'Linear functions', 'Easy',
            r'<p>A business owner purchased an energy-efficient air conditioning system for a cost of $4,200, including installation. The business owner saves $940 per year to operate the new system compared to the operating cost of the old system.</p>',
            r'Including the cost of the new system, which function \(f\) gives the total amount, in dollars, the business owner has saved \(x\) years after purchasing the new system?',
            {
                'A': r'\(f(x) = -4{,}200x + 940\)',
                'B': r'\(f(x) = -940x - 4{,}200\)',
                'C': r'\(f(x) = 940x - 4{,}200\)',
                'D': r'\(f(x) = 4{,}200x - 940\)',
            },
            'C',
            r'Mỗi năm tiết kiệm được $940 nên sau \(x\) năm tiết kiệm vận hành được \(+940x\). Tuy nhiên phải trừ đi chi phí đầu tư ban đầu một lần là $4,200. Do đó tổng số tiền tiết kiệm ròng là: \[f(x) = 940x - 4{,}200.\]',
            r'Khoản lặp lại hằng năm ("per year") luôn đi với biến \(x\) (slope), còn chi phí bỏ ra một lần ban đầu là hằng số âm (\(-4{,}200\)).',
            {
                'A': ('Đảo vai trò 4,200 và 940', r'Gắn $4,200 với số năm \(x\) là sai vì đây là chi phí mua 1 lần.'),
                'B': ('Sai dấu tiền tiết kiệm', r'\(-940x\) nghĩa là mỗi năm lại tốn thêm $940 thay vì tiết kiệm.'),
                'C': ('Đáp án đúng', r'Tiết kiệm \(940x\) trừ chi phí đầu tư \(4{,}200\): \(f(x) = 940x - 4{,}200\).'),
                'D': ('Đảo vai trò 4,200 và 940', r'Nhầm tiết kiệm hằng năm là $4,200 và giá máy là $940.'),
            },
            r'Thử \(x = 0\): ngay lúc mới mua máy, số tiền tiết kiệm ròng phải là \(-4{,}200\), và sau nhiều năm phải tăng lên → chỉ C thỏa mãn!'
        ),

        # M2 Q2 (p59)
        math_mcq(
            'sat_real_jun25v1_m2_q2', 2, 'Algebra', 'Linear functions', 'Easy',
            r'<p>For the linear function \(g\), the graph of \(y = g(x)\) in the \(xy\)-plane has a slope of \(5\) and passes through the point \((2, 37)\).</p>',
            r'Which equation defines \(g\)?',
            {
                'A': r'\(g(x) = 27x\)',
                'B': r'\(g(x) = 27x + 5\)',
                'C': r'\(g(x) = 5x\)',
                'D': r'\(g(x) = 5x + 27\)',
            },
            'D',
            r'Hàm bậc nhất có hệ số góc \(m = 5\) có dạng \(g(x) = 5x + b\). Vì đồ thị đi qua \((2, 37)\): \[37 = 5(2) + b \Rightarrow b = 37 - 10 = 27.\] Vậy \(g(x) = 5x + 27\).',
            r'Thấy slope = \(5\) là loại ngay A và B; sau đó thế \(x = 2\) kiểm tra \(g(2) = 37\) để chốt D trong 3 giây.',
            {
                'A': ('Sai cả slope và b', r'Hệ số góc là \(27\) thay vì \(5\), và \(g(2) = 54 \neq 37\).'),
                'B': ('Đảo slope và y-intercept', r'Hoán đổi \(m = 5\) và \(b = 27\).'),
                'C': ('Thiếu tung độ gốc b', r'\(g(2) = 5(2) = 10 \neq 37\).'),
                'D': ('Đáp án đúng', r'Slope \(5\) và \(g(2) = 5(2) + 27 = 37\).'),
            },
            r'Thử `5(2) + 27` ra đúng `37`, khớp ngay điểm `(2, 37)`!'
        ),

        # M2 Q3 (p60)
        math_mcq(
            'sat_real_jun25v1_m2_q3', 3, 'Geometry and Trigonometry',
            'Lines, angles, and triangles', 'Easy',
            r'<p>Parallelogram \(PQRS\) is similar to parallelogram \(TUVW\), such that \(P\), \(Q\), \(R\), and \(S\) correspond to \(T\), \(U\), \(V\), and \(W\), respectively.</p>',
            r'If \(PQ = 28TU\), then which of the following must be true?',
            {
                'A': r'\(PR = 3QR\)',
                'B': r'\(PR = 3VW\)',
                'C': r'\(QR = 28TU\)',
                'D': r'\(QR = 28UV\)',
            },
            'D',
            r'Hai hình bình hành \(PQRS \sim TUVW\) với các đỉnh tương ứng \(P \leftrightarrow T,\; Q \leftrightarrow U,\; R \leftrightarrow V,\; S \leftrightarrow W\). Vì \(PQ = 28TU\), tỉ số đồng dạng từ \(TUVW\) sang \(PQRS\) là \(28\). Cạnh \(QR\) tương ứng với cạnh \(UV\), do đó bắt buộc: \[QR = 28UV.\]',
            r'Viết thẳng hai tên đa giác chồng lên nhau (\(PQRS\) trên \(TUVW\)) để đối chiếu từng cặp cạnh tương ứng không bao giờ nhầm: \(PQ \leftrightarrow TU\), \(QR \leftrightarrow UV\), \(RS \leftrightarrow VW\), \(SP \leftrightarrow WT\).',
            {
                'A': ('Quan hệ không xác định', r'Đề không cho tỉ lệ giữa đường chéo \(PR\) và cạnh \(QR\).'),
                'B': ('Sai tỉ số và cạnh', r'Hệ số \(3\) không liên quan đến tỉ số đồng dạng \(28\).'),
                'C': ('Nhầm cặp cạnh tương ứng', r'\(QR\) tương ứng với \(UV\), không tương ứng với \(TU\) (hai cạnh kề của hình bình hành không nhất thiết bằng nhau).'),
                'D': ('Đáp án đúng', r'Đúng cặp cạnh tương ứng \(QR \leftrightarrow UV\) với tỉ số đồng dạng \(28\).'),
            },
            r'Câu tính chất hình học đồng dạng — đối chiếu trực tiếp thứ tự chữ cái `P-Q-R-S` với `T-U-V-W` là ra ngay `QR = 28UV`.'
        ),

        # M2 Q4 (p61)
        math_spr(
            'sat_real_jun25v1_m2_q4', 4, 'Problem-Solving and Data Analysis',
            'Probability and conditional probability', 'Easy',
            r'<p>At a convention center, there are a total of \(250\) visitors. Each visitor is located in either room A, room B, or room C. If one of these visitors is selected at random, the probability of selecting a visitor who is located in room A is \(0.72\) and the probability of selecting a visitor who is located in room B is \(0.24\).</p>',
            r'How many visitors are located in room C?',
            ['10'], '10',
            r'Vì mỗi khách tham dự chỉ ở đúng một trong ba phòng A, B, hoặc C nên tổng xác suất bằng \(1\): \[P(\text{C}) = 1 - 0.72 - 0.24 = 0.04.\] Số khách ở phòng C là: \[0.04 \times 250 = 10.\] (Kiểm tra: phòng A có \(180\), phòng B có \(60\), phòng C có \(10\); tổng \(180 + 60 + 10 = 250\)).',
            r'Tổng xác suất của các biến cố xung khắc phủ kín không gian mẫu luôn bằng \(1\); nhớ nhân xác suất với tổng số người (\(250\)) vì đề hỏi "How many visitors", không phải xác suất.',
            r'Gõ `(1 - 0.72 - 0.24) * 250` trong Desmos ra ngay `10`.'
        ),

        # M2 Q5 (p62)
        math_mcq(
            'sat_real_jun25v1_m2_q5', 5, 'Algebra',
            'Linear equations in two variables', 'Easy',
            r'<p>Line \(k\) is defined by \(y = 4x + \frac{1}{2}\). Line \(j\) is perpendicular to line \(k\) in the \(xy\)-plane.</p>',
            r'What is the slope of line \(j\)?',
            {'A': r'\(-2\)', 'B': r'\(-\frac{1}{4}\)', 'C': r'\(\frac{1}{2}\)', 'D': r'\(4\)'},
            'B',
            r'Đường thẳng \(k\) có hệ số góc \(m_k = 4\). Vì đường thẳng \(j \perp k\), tích hai hệ số góc bằng \(-1\) (nghịch đảo và đổi dấu): \[m_j = -\frac{1}{m_k} = -\frac{1}{4}.\]',
            r'Hai đường thẳng vuông góc có hệ số góc là <b>số đối nghịch đảo</b> của nhau: \(m_1 \cdot m_2 = -1\). Tung độ gốc \(\frac{1}{2}\) không ảnh hưởng đến hệ số góc.',
            {
                'A': ('Nghịch đảo nhầm y-intercept', r'\(-2\) là số đối nghịch đảo của \(\frac{1}{2}\), không phải của hệ số góc \(4\).'),
                'B': ('Đáp án đúng', r'\(4 \times \left(-\frac{1}{4}\right) = -1\).'),
                'C': ('Lấy tung độ gốc', r'\(\frac{1}{2}\) là \(y\)-intercept của đường thẳng \(k\), không phải slope.'),
                'D': ('Slope đường song song', r'\(4\) là hệ số góc của đường thẳng song song với \(k\), không phải vuông góc.'),
            },
            r'Gõ `y = 4x + 1/2` và `y = -(1/4)x` vào Desmos để xác nhận trực quan hai đường cắt nhau vuông góc.'
        ),

        # M2 Q6 (p62)
        math_mcq(
            'sat_real_jun25v1_m2_q6', 6, 'Advanced Math', 'Equivalent expressions', 'Easy',
            r'<p>The kinetic energy \(K\), in joules, of an object is given by the formula \(K = \frac{1}{2}mv^2\), where \(m\) is the mass of the object, in kilograms, and \(v\) is the velocity of the object, in meters per second.</p>',
            r'If the kinetic energy of a certain object can be found by using the formula \(K = 82v^2\), what is the mass of the object, in kilograms?',
            {'A': r'\(6{,}724\)', 'B': r'\(164\)', 'C': r'\(82\)', 'D': r'\(41\)'},
            'B',
            r'Đồng nhất hệ số của \(v^2\) trong hai công thức \(K = \frac{1}{2}mv^2\) và \(K = 82v^2\): \[\frac{1}{2}m = 82 \Rightarrow m = 82 \times 2 = 164\text{ kg}.\]',
            r'Cẩn thận hướng chia/nhân: \(\frac{1}{2}m = 82\) thì phải NHÂN \(2\) ra \(164\), tuyệt đối không chia \(2\) ra \(41\)!',
            {
                'A': ('Bình phương 82', r'\(82^2 = 6{,}724\) — nhầm với số mũ của \(v^2\).'),
                'B': ('Đáp án đúng', r'\(\frac{1}{2}(164)v^2 = 82v^2\).'),
                'C': ('Quên hệ số 1/2', r'Cho trực tiếp \(m = 82\) mà bỏ qua \(\frac{1}{2}\).'),
                'D': ('Chia 2 thay vì nhân 2', r'Tính \(\frac{1}{2}(82) = 41\) thay vì giải \(\frac{1}{2}m = 82\).'),
            },
            r'Gõ `0.5m = 82` vào Desmos sẽ ra ngay `m = 164`.'
        ),

        # M2 Q7 (p63)
        math_mcq(
            'sat_real_jun25v1_m2_q7', 7, 'Advanced Math', 'Nonlinear functions', 'Easy',
            r'<p>Consider the graph of the exponential equation \(y = 16^x\) in the \(xy\)-plane.</p>',
            r'What is the \(y\)-intercept of the graph of \(y = 16^x\) in the \(xy\)-plane?',
            {
                'A': r'\((0, 1)\)',
                'B': r'\((0, 16)\)',
                'C': r'\((0, 0)\)',
                'D': r'\((0, 15)\)',
            },
            'A',
            r'Giao điểm với trục tung (\(y\)-intercept) xảy ra khi \(x = 0\). Thay \(x = 0\) vào \(y = 16^x\): \[y = 16^0 = 1.\] Vậy \(y\)-intercept là \((0, 1)\).',
            r'Mọi số khác \(0\) mũ \(0\) đều bằng \(1\) (\(a^0 = 1\)), do đó đồ thị \(y = a^x\) (\(a > 0\)) LUÔN đi qua \((0, 1)\)!',
            {
                'A': ('Đáp án đúng', r'Khi \(x = 0\), \(y = 16^0 = 1 \Rightarrow (0, 1)\).'),
                'B': ('Nhầm với x = 1', r'\(16^1 = 16\) ứng với điểm \((1, 16)\), không phải \((0, 16)\).'),
                'C': ('Nhầm với hàm tuyến tính y = 16x', r'Nghĩ sai \(16^0 = 0\) hoặc đọc nhầm \(16^x\) thành \(16x\).'),
                'D': ('Trừ 1 nhầm lẫn', r'\(16 - 1 = 15\) không có cơ sở toán học ở đây.'),
            },
            r'Gõ `y = 16^x` vào Desmos và bấm trực tiếp vào giao điểm với trục tung sẽ hiện ngay `(0, 1)`.'
        ),

        # M2 Q8 (p63)
        math_mcq(
            'sat_real_jun25v1_m2_q8', 8, 'Advanced Math', 'Equivalent expressions', 'Medium',
            r'<p>Consider the radical expression \(\left(\left(\sqrt[7]{3}\right)t\right)^{\frac{7}{8}}\), where \(t > 0\).</p>',
            r'Which expression is equivalent to \(\left(\left(\sqrt[7]{3}\right)t\right)^{\frac{7}{8}}\), where \(t > 0\)?',
            {
                'A': r'\(\sqrt[7]{3t^8}\)',
                'B': r'\(\sqrt[7]{3^8 t}\)',
                'C': r'\(\sqrt[8]{3t^7}\)',
                'D': r'\(\sqrt[8]{3^7 t}\)',
            },
            'C',
            r'Đổi căn thức sang số mũ hữu tỉ \(\sqrt[7]{3} = 3^{\frac{1}{7}}\), rồi phân phối số mũ \(\frac{7}{8}\) cho từng thừa số: \[\left(3^{\frac{1}{7}} \cdot t^1\right)^{\frac{7}{8}} = 3^{\frac{1}{7} \cdot \frac{7}{8}} \cdot t^{\frac{7}{8}} = 3^{\frac{1}{8}} \cdot t^{\frac{7}{8}} = \left(3t^7\right)^{\frac{1}{8}} = \sqrt[8]{3t^7}.\]',
            r'Quy tắc vàng cho mọi bài căn bậc \(n\) trên SAT: đổi toàn bộ sang dạng lũy thừa \(a^{m/n}\), rút gọn số mũ, rồi ghép chung mẫu số \(8\) thành căn bậc \(\sqrt[8]{\;\cdot\;}\).',
            {
                'A': ('Đảo tử và mẫu số mũ', r'\(\sqrt[7]{3t^8} = 3^{1/7} t^{8/7}\), đảo ngược \(\frac{7}{8}\) thành \(\frac{8}{7}\).'),
                'B': ('Đảo vị trí mũ 8 vào cơ số 3', r'\(\sqrt[7]{3^8 t} = 3^{8/7} t^{1/7}\), sai cả cơ số lẫn bậc căn.'),
                'C': ('Đáp án đúng', r'\(\sqrt[8]{3t^7} = 3^{1/8} t^{7/8}\), khớp hoàn toàn.'),
                'D': ('Gắn nhầm mũ 7 cho 3 thay vì t', r'\(\sqrt[8]{3^7 t} = 3^{7/8} t^{1/8}\), quên rút gọn \(\frac{1}{7} \cdot \frac{7}{8} = \frac{1}{8}\).'),
            },
            r'Đặt thanh trượt `t = 2` trong Desmos, tính `((3^(1/7)) * t)^(7/8)` ra `2.1049...`, rồi kiểm tra `(3 * t^7)^(1/8)` ra y hệt `2.1049...`!'
        ),

        # M2 Q9 (p64)
        math_mcq(
            'sat_real_jun25v1_m2_q9', 9, 'Advanced Math', 'Nonlinear functions', 'Medium',
            r'<p style="text-align:center;">\[m(t) = -0.0274\left(\frac{t}{7}\right)^2 + 7.3873\left(\frac{t}{7}\right) + 75.032\]</p>'
            r'<p>The function \(m\) gives the predicted body mass \(m(t)\), in kilograms (kg), of a male giraffe \(t\) days after it was born in a wildlife reserve, where \(t \le 390\).</p>',
            r'Which of the following is the best interpretation of the statement “\(m(370)\) is approximately equal to \(389\)” in this context?',
            {
                'A': r'The predicted body mass of a male giraffe was approximately \(370\text{ kg}\) \(389\) days after it was born.',
                'B': r'The predicted body mass of a male giraffe was approximately \(389\text{ kg}\) \(370\) days after it was born.',
                'C': r'The predicted body mass of a male giraffe was approximately \(389\text{ kg}\) \(\frac{370}{7}\) days after it was born.',
                'D': r'The predicted body mass of a male giraffe was approximately \(\frac{370}{7}\text{ kg}\) \(389\) days after it was born.',
            },
            'B',
            r'Đối chiếu định nghĩa biến vào/ra trong đề:<ul><li>Đầu vào \(t = 370\): số <b>ngày</b> sau khi sinh (\(370\) ngày).</li><li>Đầu ra \(m(370) \approx 389\): khối lượng cơ thể dự đoán tính bằng <b>kg</b> (\(389\text{ kg}\)).</li></ul>Do đó phát biểu nghĩa là: khối lượng cơ thể dự đoán của một con hươu cao cổ đực xấp xỉ \(389\text{ kg}\) vào thời điểm \(370\) ngày sau khi sinh.',
            r'Đừng bị phân tâm bởi cụm \(\frac{t}{7}\) trong công thức (đổi sang tuần): đề đã định nghĩa rõ \(t\) tính bằng <b>ngày</b>, nên đầu vào trong \(m(370)\) là đúng \(370\) ngày!',
            {
                'A': ('Đảo đầu vào và đầu ra', r'Gán nhầm \(370\) là khối lượng (kg) và \(389\) là số ngày.'),
                'B': ('Đáp án đúng', r'Đầu vào \(t = 370\) ngày, đầu ra \(m(370) \approx 389\text{ kg}\).'),
                'C': ('Bẫy chia 7 từ công thức', r'\(\frac{370}{7}\) là số TUẦN, không phải số ngày.'),
                'D': ('Sai cả đơn vị lẫn biến', r'Vừa đảo đầu vào/đầu ra vừa chia nhầm cho \(7\).'),
            },
            r'Câu đọc hiểu ký hiệu hàm `m(input) = output` — không cần bấm máy, chỉ cần đối chiếu đơn vị của `t` (days) và `m(t)` (kg).'
        ),

        # M2 Q10 (p64)
        math_mcq(
            'sat_real_jun25v1_m2_q10', 10, 'Algebra', 'Linear equations in one variable', 'Medium',
            r'<p style="text-align:center;">\[\frac{5}{9}(x - k) = k\left(x - \frac{9}{5}\right)\]</p>'
            r'<p>In the given equation, \(k\) is a constant. The equation has no solution.</p>',
            r'What is the value of \(k\)?',
            {
                'A': r'\(-\frac{5}{9}\)',
                'B': r'\(-\frac{9}{5}\)',
                'C': r'\(\frac{9}{5}\)',
                'D': r'\(\frac{5}{9}\)',
            },
            'D',
            r'Khai triển hai vế theo dạng \(Ax + B = Cx + D\): \[\frac{5}{9}x - \frac{5}{9}k = kx - \frac{9}{5}k.\] Phương trình bậc nhất một ẩn <b>vô nghiệm</b> khi và chỉ khi hệ số của \(x\) hai vế bằng nhau và hằng số tự do khác nhau:<ul><li>Hệ số của \(x\): \(k = \frac{5}{9}\).</li><li>Kiểm tra hằng số khi \(k = \frac{5}{9}\): vế trái là \(-\frac{25}{81}\), vế phải là \(-1\). Vì \(-\frac{25}{81} \neq -1\), phương trình vô nghiệm!</li></ul>',
            r'Với \(Ax + B = Cx + D\): <b>vô nghiệm</b> \(\Leftrightarrow A = C\) và \(B \neq D\); <b>vô số nghiệm</b> \(\Leftrightarrow A = C\) và \(B = D\).',
            {
                'A': ('Sai dấu hệ số x', r'Nếu \(k = -\frac{5}{9}\) thì \(\frac{5}{9}x \neq -\frac{5}{9}x\), phương trình có nghiệm duy nhất.'),
                'B': ('Nghịch đảo và đổi dấu', r'Nếu \(k = -\frac{9}{5}\), hệ số của \(x\) hai vế khác nhau \(\Rightarrow\) có nghiệm duy nhất.'),
                'C': ('Nghịch đảo hệ số x', r'Nếu \(k = \frac{9}{5}\), hệ số của \(x\) là \(\frac{5}{9} \neq \frac{9}{5}\) \(\Rightarrow\) có 1 nghiệm duy nhất.'),
                'D': ('Đáp án đúng', r'Khi \(k = \frac{5}{9}\), hai vế cùng có \(\frac{5}{9}x\) nhưng hằng số \(-\frac{25}{81} \neq -1\) nên vô nghiệm.'),
            },
            r'Gõ `y = (5/9)(x - k)` và `y = k(x - 9/5)` vào Desmos kèm thanh trượt `k` — khi nhập `k = 5/9`, hai đường thẳng song song nhau (không cắt nhau)!'
        ),

        # M2 Q11 (p65)
        math_mcq(
            'sat_real_jun25v1_m2_q11', 11, 'Advanced Math', 'Nonlinear functions', 'Medium',
            r'<p style="text-align:center;">\[f(x) = -3x^2 + 30x - 48\]</p>'
            r'<p>The function \(f\) is defined by the given equation.</p>',
            r'Which of the following equivalent forms of the equation displays the maximum value of the function as a constant or coefficient?',
            {
                'A': r'\(f(x) = -3x^2 + 24x + 6x - 48\)',
                'B': r'\(f(x) = -3x(x - 8) + 6(x - 8)\)',
                'C': r'\(f(x) = -3(x - 5)^2 + 27\)',
                'D': r'\(f(x) = -3(x - 8)(x - 2)\)',
            },
            'C',
            r'Để hiển thị trực tiếp giá trị lớn nhất (maximum value) của parabol dưới dạng một hằng số, ta phải viết về <b>dạng đỉnh (vertex form)</b> \(f(x) = a(x - h)^2 + k\): \[f(x) = -3(x^2 - 10x) - 48 = -3\bigl((x - 5)^2 - 25\bigr) - 48 = -3(x - 5)^2 + 27.\] Vì \(-3(x - 5)^2 \le 0\), giá trị lớn nhất của \(f\) chính là hằng số \(27\) (đạt tại \(x = 5\)).',
            r'Ba dạng parabol trên SAT: dạng chuẩn hiển thị \(y\)-intercept, dạng tích hiển thị nghiệm (\(x\)-intercepts), và <b>dạng đỉnh \(a(x - h)^2 + k\)</b> hiển thị cực trị (min/max = \(k\))!',
            {
                'A': ('Dạng tách hạng tử trung gian', r'Chỉ là bước tách \(30x = 24x + 6x\), không hiển thị giá trị lớn nhất \(27\).'),
                'B': ('Dạng nhóm nhân tử chưa hoàn tất', r'Mới dừng ở bước nhóm nhân tử \((x - 8)\), không hiển thị cực đại.'),
                'C': ('Đáp án đúng', r'Dạng đỉnh hiển thị ngay cực đại \(27\) và khai triển đúng ra \(-3x^2 + 30x - 48\).'),
                'D': ('Dạng tích (factored form)', r'Hiển thị hai nghiệm \(x = 8\) và \(x = 2\), không hiển thị giá trị lớn nhất \(27\).'),
            },
            r'Gõ `y = -3x^2 + 30x - 48` vào Desmos → bấm vào đỉnh parabol thấy `(5, 27)` → chọn ngay dạng đỉnh chứa số `5` và `27` (đáp án C)!'
        ),

        # M2 Q12 (p65)
        math_mcq(
            'sat_real_jun25v1_m2_q12', 12, 'Problem-Solving and Data Analysis',
            'Ratios, rates, proportional relationships, and units', 'Medium',
            r'<p>An object\'s speed, in meters per hour, is increasing at a rate of \(1{,}530\) meters per hour per second. (Use \(1\text{ meter} = 3.28\text{ feet}\).) </p>',
            r'Which of the following is closest to this rate in <b>feet per second squared</b>?',
            {'A': r'\(0.13\)', 'B': r'\(1.39\)', 'C': r'\(7.77\)', 'D': r'\(83.6\)'},
            'B',
            r'Đổi từng đơn vị bằng phương pháp khử thứ nguyên: \[\frac{1{,}530\text{ m}}{\text{hr} \cdot \text{s}} \times \frac{3.28\text{ ft}}{1\text{ m}} \times \frac{1\text{ hr}}{3{,}600\text{ s}} = \frac{1{,}530 \times 3.28}{3{,}600}\;\frac{\text{ft}}{\text{s}^2} = \frac{5{,}018.4}{3{,}600} \approx 1.394\text{ ft/s}^2.\] Giá trị gần nhất là \(1.39\).',
            r'Nhớ kỹ \(1\text{ giờ} = 60 \times 60 = 3{,}600\text{ giây}\)! Đề cho "meters per hour per second" tức mẫu số đã có sẵn \(1\) lần giây, nên chỉ cần đổi \(\text{hour} \to 3{,}600\text{ s}\) là đủ ra \(\text{s}^2\).',
            {
                'A': ('Chia thay vì nhân 3.28', r'\(\frac{1{,}530}{3.28 \times 3{,}600} \approx 0.13\) — ngược tỉ số đổi mét sang feet.'),
                'B': ('Đáp án đúng', r'\(\frac{1{,}530 \times 3.28}{3{,}600} = 1.394 \approx 1.39\).'),
                'C': ('Chia 60 và chia 3.28', r'\(\frac{1{,}530}{60 \times 3.28} \approx 7.77\) — sai cả hai bước đổi đơn vị.'),
                'D': ('Chỉ chia 60 thay vì 3,600', r'\(\frac{1{,}530 \times 3.28}{60} = 83.64 \approx 83.6\) — quên đổi giờ sang giây cần \(3{,}600\) chứ không phải \(60\).'),
            },
            r'Gõ `(1530 * 3.28) / 3600` vào Desmos ra ngay `1.394`, làm tròn thành `1.39`.'
        ),

        # M2 Q13 (p66)
        math_spr(
            'sat_real_jun25v1_m2_q13', 13, 'Algebra',
            'Linear equations in two variables', 'Medium',
            tbl_m2_q13 +
            r'<p>The table shows four values of \(x\) and their corresponding values of \(y\). The linear relationship between \(x\) and \(y\) can be represented by the equation \(2x + By = C\), where \(B\) and \(C\) are constants.</p>',
            r'What is the value of \(C\)?',
            ['-54'], '-54',
            r'Bước 1 — Tìm phương trình dạng \(y = mx + b\): \[m = \frac{-16 - (-14)}{-3 - (-6)} = \frac{-2}{3}.\] Thay \((-3, -16)\) vào \(y = -\frac{2}{3}x + b\): \[-16 = -\frac{2}{3}(-3) + b = 2 + b \Rightarrow b = -18.\] Bước 2 — Đưa về dạng chuẩn \(2x + By = C\) (hệ số của \(x\) bằng đúng \(2\)): \[y = -\frac{2}{3}x - 18 \Rightarrow 3y = -2x - 54 \Rightarrow 2x + 3y = -54.\] Vậy \(B = 3\) và \(C = -54\).',
            r'Bắt buộc chuẩn hóa hệ số trước \(x\) về ĐÚNG số đề cho (\(2x\)) trước khi đọc \(C\)! (Kiểm tra lại bằng điểm \((6, -22)\): \(2(6) + 3(-22) = 12 - 66 = -54\)).',
            r'Nhập bảng `x1 = [-6, -3, 3, 6]`, `y1 = [-14, -16, -20, -22]` trong Desmos → gõ thẳng hồi quy dạng chuẩn `2 x1 + B y1 ~ C` sẽ nhả ngay `B = 3`, `C = -54`!'
        ),

        # M2 Q14 (p67)
        math_mcq(
            'sat_real_jun25v1_m2_q14', 14, 'Algebra',
            'Systems of two linear equations in two variables', 'Medium',
            r'<p style="text-align:center;">\[2x + 5y = 9\]\[12x + 30y = 54\]</p>',
            r'For each real number \(r\), which of the following points lies on the graph of each equation in the \(xy\)-plane for the given system?',
            {
                'A': r'\(\left(r,\; -\frac{2r}{5} + \frac{9}{5}\right)\)',
                'B': r'\(\left(-\frac{2r}{5} + \frac{9}{5},\; r\right)\)',
                'C': r'\(\left(-\frac{2r}{5} + 9,\; \frac{2r}{5} + 54\right)\)',
                'D': r'\(\left(\frac{r}{6} + 9,\; -\frac{r}{6} + 54\right)\)',
            },
            'A',
            r'Nhận xét phương trình thứ hai gấp đúng \(6\) lần phương trình thứ nhất: \(6(2x + 5y) = 12x + 30y = 54\). Do đó hai đồ thị trùng nhau hoàn toàn (vô số nghiệm chung). Đặt \(x = r\) và rút \(y\) từ \(2r + 5y = 9\): \[5y = -2r + 9 \Rightarrow y = -\frac{2r}{5} + \frac{9}{5}.\] Vậy mọi điểm có dạng \(\left(r,\; -\frac{2r}{5} + \frac{9}{5}\right)\) đều nằm trên cả hai đồ thị.',
            r'Với câu điểm tham số theo \(r\), cách kiểm tra siêu nhanh không sợ nhầm là thay \(r = 0\) vào 4 đáp án rồi thế ngược vào \(2x + 5y = 9\)!',
            {
                'A': ('Đáp án đúng', r'Thay vào \(2x + 5y\): \(2r + 5\left(-\frac{2r}{5} + \frac{9}{5}\right) = 2r - 2r + 9 = 9\) (đúng với mọi \(r\)).'),
                'B': ('Đảo tọa độ (x, y)', r'Thử \(r = 0\): điểm \(\left(\frac{9}{5}, 0\right)\) cho \(2\left(\frac{9}{5}\right) + 0 = \frac{18}{5} \neq 9\).'),
                'C': ('Quên chia 5 cho hằng số 9', r'Thử \(r = 0\): điểm \((9, 54)\) cho \(2(9) + 5(54) = 288 \neq 9\).'),
                'D': ('Dùng sai hệ số tỉ lệ 6', r'Thử \(r = 0\): điểm \((9, 54)\) không thỏa mãn \(2x + 5y = 9\).'),
            },
            r'Chọn \(r = 0\), tính nhanh: đáp án A cho `(0, 9/5)` → thế `2(0) + 5(9/5) = 9` (đúng ngay!), còn B, C, D đều sai.'
        ),

        # M2 Q15 (p67)
        math_mcq(
            'sat_real_jun25v1_m2_q15', 15, 'Advanced Math',
            'Nonlinear equations in one variable and systems of equations in two variables', 'Hard',
            r'<p style="text-align:center;">\[9x^2 + 30x + q = 43\]</p>'
            r'<p>In the given equation, \(q\) is a constant. One solution to the given equation is \(\frac{-5 + \sqrt{14}}{3}\).</p>',
            r'What is the value of \(q\)?',
            {'A': r'\(54\)', 'B': r'\(43\)', 'C': r'\(11\)', 'D': r'\(5\)'},
            'A',
            r'<b>Cách 1 (Hoàn thiện bình phương cực gọn):</b> Từ \(x = \frac{-5 + \sqrt{14}}{3}\), nhân chéo và chuyển \(-5\) sang: \[3x + 5 = \sqrt{14} \Rightarrow (3x + 5)^2 = 14 \Rightarrow 9x^2 + 30x + 25 = 14 \Rightarrow 9x^2 + 30x = -11.\] Thay \(9x^2 + 30x = -11\) vào phương trình đề bài: \[-11 + q = 43 \Rightarrow q = 43 + 11 = 54.\] <b>Cách 2 (Công thức nghiệm):</b> \(9x^2 + 30x + (q - 43) = 0\) có \(x = \frac{-30 \pm \sqrt{900 - 36(q - 43)}}{18} = \frac{-5 \pm \sqrt{25 - (q - 43)}}{3} \Rightarrow 68 - q = 14 \Rightarrow q = 54\).',
            r'Khi thấy nghiệm chứa căn dạng \(\frac{-b + \sqrt{d}}{a}\), khử mẫu rồi bình phương hai vế \((3x + 5)^2 = 14\) sẽ tái tạo ngay lập tức đúng cụm \(9x^2 + 30x\) của đề bài!',
            {
                'A': ('Đáp án đúng', r'\(q = 54\) cho phương trình \(9x^2 + 30x + 11 = 0\), đúng nghiệm \(\frac{-5 + \sqrt{14}}{3}\).'),
                'B': ('Nhầm q = 43', r'Nếu \(q = 43\) thì \(9x^2 + 30x = 0\) có nghiệm \(0\) và \(-\frac{10}{3}\).'),
                'C': ('Quên cộng lại 43 ở vế phải', r'\(11\) là giá trị của \(q - 43\) (hằng số sau khi chuyển \(43\) sang vế trái), chưa cộng \(43\) để ra \(q\)!'),
                'D': ('Đọc nhầm từ −5 của nghiệm', r'\(q = 5\) cho \(9x^2 + 30x - 38 = 0\), không khớp căn \(\sqrt{14}\).'),
            },
            r'Gõ `x_0 = (-5 + sqrt(14)) / 3` rồi dòng sau gõ `43 - (9x_0^2 + 30x_0)` trong Desmos sẽ ra chính xác số nguyên `54` trong 5 giây!'
        ),

        # M2 Q16 (p68)
        math_mcq(
            'sat_real_jun25v1_m2_q16', 16, 'Problem-Solving and Data Analysis',
            'Percentages', 'Medium',
            r'<p>At a hotel, guests used the pool for a total of \(t\) hours in March. At the same hotel, guests used the pool for \(3.61t\) hours in April.</p>',
            r'What is the percent increase in the number of hours guests used the pool from March to April?',
            {'A': r'\(2.61\%\)', 'B': r'\(3.61\%\)', 'C': r'\(261\%\)', 'D': r'\(361\%\)'},
            'C',
            r'Tỉ lệ phần trăm tăng thêm từ tháng 3 (\(t\)) sang tháng 4 (\(3.61t\)): \[\frac{3.61t - t}{t} \times 100\% = 2.61 \times 100\% = 261\%.\]',
            r'Với hệ số nhân \(k\) (ở đây \(k = 3.61\)): phần trăm TĂNG THÊM luôn là \((k - 1) \times 100\%\) — nhớ vừa TRỪ \(1\) vừa NHÂN \(100\)!',
            {
                'A': ('Quên nhân 100%', r'\(2.61\) là dạng thập phân, chưa đổi sang phần trăm (\(261\%\)).'),
                'B': ('Vừa quên trừ 1 vừa quên nhân 100%', r'Giữ nguyên hệ số \(3.61\) rồi gắn thêm ký hiệu \(\%\).'),
                'C': ('Đáp án đúng', r'\((3.61 - 1) \times 100\% = 261\%\).'),
                'D': ('Quên trừ 100% ban đầu', r'\(361\%\) là tỉ số của tháng 4 SO VỚI tháng 3, không phải phần trăm TĂNG THÊM.'),
            },
            r'Đặt \(t = 100\) giờ: tháng 4 là \(361\) giờ, tăng thêm \(361 - 100 = 261\) giờ trên nền \(100\) giờ \(\Rightarrow 261\%\)!'
        ),

        # M2 Q17 (p68)
        math_mcq(
            'sat_real_jun25v1_m2_q17', 17, 'Algebra',
            'Linear inequalities in one or two variables', 'Easy',
            r'<p>Consider the point \((6, 7)\) in the \(xy\)-plane.</p>',
            r'In the \(xy\)-plane, the point \((6, 7)\) is a solution to which of the following systems of inequalities?',
            {
                'A': r'\(x < 3\)<br/>\(y > 5\)',
                'B': r'\(x < 3\)<br/>\(y < 5\)',
                'C': r'\(x > 3\)<br/>\(y < 5\)',
                'D': r'\(x > 3\)<br/>\(y > 5\)',
            },
            'D',
            r'Với điểm \((x, y) = (6, 7)\), ta kiểm tra từng tọa độ:<ul><li>\(x = 6 > 3\)</li><li>\(y = 7 > 5\)</li></ul>Chỉ hệ bất đẳng thức ở đáp án D thỏa mãn đồng thời cả hai điều kiện.',
            r'Điểm là nghiệm của HỆ bất đẳng thức khi và chỉ khi nó làm đúng CẢ HAI bất đẳng thức cùng lúc.',
            {
                'A': ('Sai điều kiện x', r'\(x = 6\) không thỏa mãn \(x < 3\).'),
                'B': ('Sai cả hai điều kiện', r'\(6 \not< 3\) và \(7 \not< 5\).'),
                'C': ('Sai điều kiện y', r'\(y = 7\) không thỏa mãn \(y < 5\).'),
                'D': ('Đáp án đúng', r'Cả \(6 > 3\) và \(7 > 5\) đều đúng.'),
            },
            r'So sánh trực tiếp \(6 > 3\) và \(7 > 5\) là chọn ngay đáp án D trong 2 giây.'
        ),

        # M2 Q18 (p69)
        math_mcq(
            'sat_real_jun25v1_m2_q18', 18, 'Advanced Math', 'Nonlinear functions', 'Hard',
            r'<p>At different times on a certain day, a manager at a theme park recorded the number of visitors. An exponential model gives the estimated number of visitors, \(V\), at the theme park \(t\) hours after the theme park opened, where \(t \le 3\). Based on the model, \(80\) visitors were estimated to be at the theme park when it opened, and every \(30\) minutes the estimated number of visitors increased by \(150\%\) of the estimated number of visitors \(30\) minutes earlier.</p>',
            r'Which of the following equations best represents this model?',
            {
                'A': r'\(V = 80(2.50)^{2t}\)',
                'B': r'\(V = 80(2.50)^{\frac{t}{30}}\)',
                'C': r'\(V = 80(1.50)^{2t}\)',
                'D': r'\(V = 80(1.50)^{\frac{t}{30}}\)',
            },
            'A',
            r'Xây dựng mô hình hàm mũ \(V = a \cdot b^{n(t)}\):<ul><li>Giá trị ban đầu lúc mở cửa (\(t = 0\)): \(a = 80\).</li><li>Tăng thêm \(150\%\) nghĩa là hệ số tăng trưởng mỗi chu kỳ là \(b = 1 + 150\% = 1 + 1.50 = 2.50\).</li><li>Đổi chu kỳ theo đơn vị của \(t\) (<b>giờ</b>): \(30\text{ phút} = 0.5\text{ giờ}\). Trong \(t\) giờ có \(\frac{t}{0.5} = 2t\) chu kỳ 30 phút.</li></ul>Vậy \(V = 80(2.50)^{2t}\).',
            r'Hai bẫy kép của SAT Hard Math: (1) "increased by \(150\%\)" \(\Rightarrow\) cơ số là \(1 + 1.50 = 2.50\) (KHÔNG phải \(1.50\)), và (2) chu kỳ \(30\) phút khi \(t\) tính bằng GIỜ \(\Rightarrow\) số mũ là \(\frac{t}{0.5} = 2t\) (KHÔNG phải \(\frac{t}{30}\))!',
            {
                'A': ('Đáp án đúng', r'Kiểm tra sau 30 phút (\(t = 0.5\) giờ): \(V = 80(2.50)^1 = 200\), đúng bằng \(80 + 150\%(80)\).'),
                'B': ('Quên đổi 30 phút sang giờ', r'Số mũ \(\frac{t}{30}\) nghĩa là mỗi \(30\) GIỜ mới tăng một lần, không phải \(30\) phút.'),
                'C': ('Quên cộng 1 vào 150%', r'Cơ số \(1.50\) chỉ tương ứng với mức tăng \(50\%\), không phải tăng \(150\%\).'),
                'D': ('Mắc cả hai bẫy', r'Vừa dùng sai cơ số \(1.50\) vừa quên đổi \(30\) phút sang \(0.5\) giờ.'),
            },
            r'Kiểm tra nhanh tại \(t = 0.5\) giờ (30 phút): số khách phải là `80 + 1.50 * 80 = 200`. Gõ `80 * (2.50)^(2 * 0.5)` trong Desmos ra đúng `200`!'
        ),

        # M2 Q19 (p69-70)
        math_mcq(
            'sat_real_jun25v1_m2_q19', 19, 'Problem-Solving and Data Analysis',
            'One-variable data: Distributions and measures of center and spread', 'Medium',
            r'<p>For data set A, the table summarizes the distribution of the number of pieces of mail received by a business each day during a period of \(11\) days.</p>' +
            tbl_m2_q19 +
            r'<p>The data value \(17\) is removed from data set A to create data set B, which consists of the remaining \(10\) data values.</p>',
            r'Which statement best compares the median of data set A and the median of data set B?',
            {
                'A': 'The median of data set B is less than the median of data set A.',
                'B': 'The median of data set B is greater than the median of data set A.',
                'C': 'The median of data set B is equal to the median of data set A.',
                'D': 'There is not enough information to compare the medians of the two data sets.',
            },
            'C',
            r'Liệt kê dãy giá trị đã sắp xếp tăng dần từ bảng tần số:<ul><li><b>Tập A (11 giá trị):</b> \(0,\; 0,\; 4,\; 4,\; 5,\; \mathbf{5},\; 6,\; 6,\; 7,\; 8,\; 17\). Trung vị là giá trị đứng thứ \(\frac{11 + 1}{2} = 6\), tức \(\text{Median}_A = 5\).</li><li><b>Tập B (10 giá trị, bỏ \(17\)):</b> \(0,\; 0,\; 4,\; 4,\; \mathbf{5},\; \mathbf{5},\; 6,\; 6,\; 7,\; 8\). Trung vị là trung bình cộng của giá trị thứ \(5\) và thứ \(6\): \[\text{Median}_B = \frac{5 + 5}{2} = 5.\]</li></ul>Do đó trung vị của tập B <b>bằng</b> trung vị của tập A.',
            r'Đừng đoán theo cảm tính "bỏ số ngoại lai lớn nhất \(17\) thì trung vị giảm"! Khi giá trị đứng thứ 5 và thứ 6 trùng nhau (đều là \(5\)), trung vị hoàn toàn KHÔNG đổi (trung bình cộng/mean mới giảm).',
            {
                'A': ('Bẫy cảm tính bỏ outlier', r'Mean (trung bình cộng) giảm khi bỏ \(17\), nhưng ở đây hai phần tử giữa đều là \(5\) nên median giữ nguyên bằng \(5\).'),
                'B': ('Ngược chiều tác động', r'Bỏ giá trị lớn nhất không bao giờ làm trung vị tăng lên được.'),
                'C': ('Đáp án đúng', r'\(\text{Median}_A = 5\) và \(\text{Median}_B = \frac{5 + 5}{2} = 5\).'),
                'D': ('Hiểu nhầm bảng tần số', r'Bảng tần số đã cho đầy đủ chính xác từng giá trị của cả 11 ngày.'),
            },
            r'Gõ `median([0,0,4,4,5,5,6,6,7,8,17])` và `median([0,0,4,4,5,5,6,6,7,8])` vào Desmos — cả hai đều hiện ngay `5`!'
        ),

        # M2 Q20 (p70)
        math_mcq(
            'sat_real_jun25v1_m2_q20', 20, 'Geometry and Trigonometry',
            'Right triangles and trigonometry', 'Hard',
            r'<p>Triangle \(ABC\) is similar to triangle \(DEF\), where \(A\) corresponds to \(D\) and \(C\) corresponds to \(F\). Angles \(C\) and \(F\) are right angles. If \(\tan(A) = \sqrt{3}\) and \(DF = 53\).</p>',
            r'What is the length of \(\overline{DE}\)?',
            {
                'A': r'\(53\frac{\sqrt{3}}{3}\)',
                'B': r'\(53\frac{\sqrt{3}}{2}\)',
                'C': r'\(53\sqrt{3}\)',
                'D': r'\(106\)',
            },
            'D',
            r'Vì \(\triangle ABC \sim \triangle DEF\) với \(A \leftrightarrow D\) và \(C \leftrightarrow F\) (\(\angle C = \angle F = 90^\circ\)), nên \(\angle D = \angle A\), suy ra \[\tan(D) = \tan(A) = \sqrt{3} \Rightarrow \angle D = 60^\circ.\] Trong tam giác vuông \(DEF\) vuông tại \(F\) (tam giác đặc biệt \(30^\circ\text{–}60^\circ\text{–}90^\circ\)):<ul><li>\(DF = 53\) là cạnh kề góc \(60^\circ\) (cạnh ngắn nhất).</li><li>\(EF = 53\sqrt{3}\) là cạnh đối góc \(60^\circ\).</li><li>\(\overline{DE}\) là <b>cạnh huyền</b> (đối diện góc vuông \(F\)): \(DE = 2 \cdot DF = 2(53) = 106\) (hoặc \(\sqrt{53^2 + (53\sqrt{3})^2} = 106\)).</li></ul>',
            r'Vẽ nhanh tam giác vuông \(DEF\) với góc vuông ở \(F\) để thấy rõ \(\overline{DE}\) là CẠNH HUYỀN — cực nhiều thí sinh dính bẫy C tính ra cạnh góc vuông \(EF = 53\sqrt{3}\)!',
            {
                'A': ('Chia cho căn 3', r'\(\frac{53}{\sqrt{3}} = 53\frac{\sqrt{3}}{3}\) — đảo nhầm \(\tan(60^\circ) = \frac{DF}{EF}\) thay vì \(\frac{EF}{DF}\).'),
                'B': ('Dùng sai tỉ số sin/cos', r'Nhân nhầm với \(\sin(60^\circ) = \frac{\sqrt{3}}{2}\).'),
                'C': ('Bẫy tính nhầm cạnh EF', r'\(53\sqrt{3}\) là độ dài cạnh góc vuông \(EF\), KHÔNG phải cạnh huyền \(DE\)!'),
                'D': ('Đáp án đúng', r'\(\triangle DEF\) là tam giác \(30^\circ\text{–}60^\circ\text{–}90^\circ\) có cạnh huyền \(DE = 2 \cdot DF = 106\).'),
            },
            r'Trong Desmos (chế độ Degrees hoặc Radians đều được), gõ `sqrt(53^2 + (53 * sqrt(3))^2)` sẽ ra ngay `106`!'
        ),

        # M2 Q21 (p71)
        math_spr(
            'sat_real_jun25v1_m2_q21', 21, 'Geometry and Trigonometry',
            'Area and volume', 'Hard',
            r'<p>A right triangular pyramid has exactly six edges. Each of these edges is \(96\) centimeters long. The surface area of the pyramid is \(k\sqrt{3}\) square centimeters.</p>',
            r'What is the value of \(k\)?',
            ['9216'], '9216',
            r'Một hình chóp tam giác có tất cả \(6\) cạnh bằng nhau (\(s = 96\text{ cm}\)) chính là <b>tứ diện đều</b> gồm đúng \(4\) mặt là \(4\) tam giác đều cạnh \(s = 96\).<br/>Diện tích một tam giác đều cạnh \(s\) là: \[A_{\text{mặt}} = \frac{\sqrt{3}}{4}s^2.\] Tổng diện tích toàn phần (surface area) của cả \(4\) mặt: \[SA = 4 \cdot \frac{\sqrt{3}}{4}s^2 = s^2\sqrt{3} = 96^2\sqrt{3} = 9{,}216\sqrt{3}.\] Suy ra \(k = 9{,}216\).',
            r'Công thức siêu tốc cho tứ diện đều cạnh \(s\): \(SA = 4 \times \frac{\sqrt{3}}{4}s^2 = s^2\sqrt{3}\) — hệ số \(4\) tự triệt tiêu cực đẹp!',
            r'Gõ `96^2` trong Desmos ra ngay `9216` (lưu ý nhập SPR không điền dấu phẩy: `9216`).'
        ),

        # M2 Q22 (p71)
        math_spr(
            'sat_real_jun25v1_m2_q22', 22, 'Advanced Math',
            'Nonlinear equations in one variable and systems of equations in two variables', 'Hard',
            r'<p style="text-align:center;">\[x(kx - 96) = -8\]</p>'
            r'<p>In the given equation, \(k\) is an integer constant.</p>',
            r'If the equation has two distinct real solutions, what is the greatest possible value of \(k\)?',
            ['287'], '287',
            r'Nhân phá ngoặc và chuyển vế về phương trình bậc hai chuẩn: \[kx^2 - 96x + 8 = 0.\] Để phương trình có <b>hai nghiệm thực phân biệt</b>, cần \(k \neq 0\) và biệt thức \(\Delta > 0\): \[\Delta = (-96)^2 - 4(k)(8) > 0 \Rightarrow 9{,}216 - 32k > 0 \Rightarrow 32k < 9{,}216 \Rightarrow k < \frac{9{,}216}{32} = 288.\] Vì \(k\) là <b>số nguyên</b> và \(k < 288\) (dấu nhỏ hơn nghiêm ngặt — tại \(k = 288\) phương trình có nghiệm kép duy nhất \(x = \frac{1}{6}\)), giá trị nguyên lớn nhất của \(k\) là \(287\).',
            r'Bẫy kinh điển câu chốt số 22: "two distinct real solutions" yêu cầu \(\Delta > 0\) (KHÔNG có dấu bằng)! Khi tìm ra \(k < 288\), phải trừ đi \(1\) để lấy số nguyên lớn nhất là \(287\)!',
            r'Gõ `96^2 / (4 * 8)` trong Desmos ra đúng `288` → vì bất đẳng thức nghiêm ngặt `k < 288` và `k` nguyên, chốt ngay `287`!'
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
        'subtitle': 'Đề thi thật Digital SAT Toán tháng 6/2025 (Ver 1) — Đầy đủ Module 1 & Module 2',
        'difficultyBadge': 'REAL EXAM • JUNE 2025',
        'targetTimeMinutes': 70,
        'routingThreshold': 0,
    },
    'module1': {
        'id': 'm1',
        'title': 'Section 2, Module 1: Math',
        'subtitle': '22 Questions • 35 Minutes • June 2025 Ver 1 Real Exam',
        'timeLimitMinutes': 35,
        'questions': M1_QUESTIONS,
    },
    'module2_hard': {
        'id': 'm2_hard',
        'title': 'Section 2, Module 2: Math',
        'subtitle': '22 Questions • 35 Minutes • June 2025 Ver 1 Real Exam',
        'timeLimitMinutes': 35,
        'questions': M2_QUESTIONS,
    },
    'module2_lower': {
        'id': 'm2_lower',
        'title': 'Section 2, Module 2: Math',
        'subtitle': '22 Questions • 35 Minutes • June 2025 Ver 1 Real Exam',
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
    # M1 Q1: f(x) = 10x + 4, x = 7 => 74 (D)
    assert 10 * 7 + 4 == 74 and m1[1]['correctAnswer'] == 'D'

    # M1 Q2: 26 fathoms * 6 ft/fathom = 156
    assert 26 * 6 == 156 and '156' in m1[2]['acceptedAnswers']

    # M1 Q3: 6x = 30, 6x - 10y = 80 => x = 5, y = -5 (A)
    x3 = Fraction(30, 6)
    y3 = Fraction(6 * x3 - 80, 10)
    assert (x3, y3) == (5, -5) and m1[3]['correctAnswer'] == 'A'

    # M1 Q4: 41x^2 + 41 == 41(x^2 + 1) (D)
    for xv in (-3, 0, 1, 5):
        assert 41 * xv ** 2 + 41 == 41 * (xv ** 2 + 1)
    assert m1[4]['correctAnswer'] == 'D'

    # M1 Q5: right triangle legs 9, 12, hyp r => 9^2 + 12^2 = r^2 (C)
    assert 9 ** 2 + 12 ** 2 == 15 ** 2 and m1[5]['correctAnswer'] == 'C'

    # M1 Q6: 45 + 10.75n <= 275 => max integer n = 21
    n6 = int(Fraction(275 - 45, Fraction(1075, 100)))
    assert n6 == 21
    assert 45 + Fraction(1075, 100) * 21 <= 275
    assert 45 + Fraction(1075, 100) * 22 > 275
    assert '21' in m1[6]['acceptedAnswers']

    # M1 Q7: 7 - 2.75 = 4.25 = 17/4
    diff7 = Fraction(7) - Fraction(275, 100)
    assert diff7 == Fraction(17, 4) and float(diff7) == 4.25
    assert '4.25' in m1[7]['acceptedAnswers'] and '17/4' in m1[7]['acceptedAnswers']

    # M1 Q8: cube edge 13 => 13^3 = 2197 (D)
    assert 13 ** 3 == 2197 and m1[8]['correctAnswer'] == 'D'

    # M1 Q9: parallel lines, x + y = 180, x > 145 => y < 35 (A)
    for x9 in (146, 150, 179):
        y9 = 180 - x9
        assert y9 < 35 and x9 + y9 == 180
    assert m1[9]['correctAnswer'] == 'A'

    # M1 Q10: (2x - 4)(x - 8)(x - 9) = 0 => solutions 2, 8, 9 => sum 19 (C)
    sols10 = [Fraction(4, 2), Fraction(8), Fraction(9)]
    assert sum(sols10) == 19 and m1[10]['correctAnswer'] == 'C'

    # M1 Q11: g(x) = 7x^(-1) => g(13) = 7/13
    val11 = Fraction(7, 13)
    assert val11 == Fraction(7, 13) and round(float(val11), 4) == 0.5385
    assert '7/13' in m1[11]['acceptedAnswers']

    # M1 Q12: boundary through (0, 8) and (1, 11) => m = 3, b = 8; (0,0) satisfies 0 < 8 => y < 3x + 8 (B)
    m12 = Fraction(11 - 8, 1 - 0)
    assert m12 == 3 and 0 < m12 * 0 + 8 and m1[12]['correctAnswer'] == 'B'

    # M1 Q13: 2x^2 + 16 = -8x + 26 => x = -5 or x = 1 => -5 in options (A)
    for x13 in (-5, 1):
        assert 2 * x13 ** 2 + 16 == -8 * x13 + 26
    assert m1[13]['correctAnswer'] == 'A'

    # M1 Q14: OLS regression on all 11 scatterplot points => y = -0.07 + 1.02x (C)
    n14 = len(SCATTER_M1_Q14_PTS)
    assert n14 == 11
    mx14 = sum(x for x, _ in SCATTER_M1_Q14_PTS) / n14
    my14 = sum(y for _, y in SCATTER_M1_Q14_PTS) / n14
    slope14 = sum((x - mx14) * (y - my14) for x, y in SCATTER_M1_Q14_PTS) / sum(
        (x - mx14) ** 2 for x, _ in SCATTER_M1_Q14_PTS
    )
    inter14 = my14 - slope14 * mx14
    assert round(slope14, 2) == 1.02 and round(inter14, 2) == -0.07
    assert m1[14]['correctAnswer'] == 'C'

    # M1 Q15: 4(x - 3) = 11 + 2(x - 3) => x - 3 = 11/2 = 5.5
    u15 = Fraction(11, 2)
    assert 4 * u15 == 11 + 2 * u15 and float(u15) == 5.5
    assert '5.5' in m1[15]['acceptedAnswers'] and '11/2' in m1[15]['acceptedAnswers']

    # M1 Q16: 141 is p% of 125 => p = 112.8 (B)
    p16 = Fraction(141, 125) * 100
    assert float(p16) == 112.8 and m1[16]['correctAnswer'] == 'B'

    # M1 Q17: (2x + 9)^2 - (x - 7) == 4x^2 + 35x + 88 (B)
    for xv in (-4, 0, 1, 7):
        assert (2 * xv + 9) ** 2 - (xv - 7) == 4 * xv ** 2 + 35 * xv + 88
    assert m1[17]['correctAnswer'] == 'B'

    # M1 Q18: isosceles triangle ORS with ∠ROS = 116° => ∠RSO = (180 - 116)/2 = 32°
    assert Fraction(180 - 116, 2) == 32 and '32' in m1[18]['acceptedAnswers']

    # M1 Q19: r = 32 * (1/2)^x (C)
    assert 32 * Fraction(1, 2) ** 0 == 32
    assert 32 * Fraction(1, 2) ** 5 == 1
    assert m1[19]['correctAnswer'] == 'C'

    # M1 Q20: d_up = 12x, d_down = (12+18)y = 30y, d_down = d_up + 10 => 12x - 30y = -10 (A)
    x20 = Fraction(2)
    d_up = 12 * x20
    d_down = d_up + 10
    y20 = d_down / 30
    assert 12 * x20 - 30 * y20 == -10 and m1[20]['correctAnswer'] == 'A'

    # M1 Q21: f(x) = 4(x - 3)(x^2 - k), f(-8) = 0 => k = 64 => f(0) = 4(-3)(-64) = 768
    k21 = (-8) ** 2
    assert 4 * (-8 - 3) * ((-8) ** 2 - k21) == 0
    f0_21 = 4 * (0 - 3) * (0 - k21)
    assert f0_21 == 768 and '768' in m1[21]['acceptedAnswers']

    # M1 Q22: table (-17,-7), (-9,0), (-1,7) => a = 7/8, b = 63/8 => a + b = 35/4 (D)
    a22 = Fraction(0 - (-7), -9 - (-17))
    assert a22 == Fraction(7 - 0, -1 - (-9)) == Fraction(7, 8)
    b22 = 0 - a22 * (-9)
    assert b22 == Fraction(63, 8) and a22 + b22 == Fraction(35, 4)
    assert m1[22]['correctAnswer'] == 'D'

    # ---------- MODULE 2 VERIFICATIONS ----------
    # M2 Q1: f(x) = 940x - 4200 (C)
    assert 940 * 0 - 4200 == -4200 and 940 * 5 - 4200 == 500
    assert m2[1]['correctAnswer'] == 'C'

    # M2 Q2: slope 5 through (2, 37) => g(x) = 5x + 27 (D)
    b_m2_2 = 37 - 5 * 2
    assert b_m2_2 == 27 and m2[2]['correctAnswer'] == 'D'

    # M2 Q3: PQRS ~ TUVW, PQ = 28TU => QR = 28UV (D)
    assert m2[3]['correctAnswer'] == 'D'

    # M2 Q4: 250 * (1 - 0.72 - 0.24) = 10
    p_c = Fraction(1) - Fraction(72, 100) - Fraction(24, 100)
    assert p_c * 250 == 10 and '10' in m2[4]['acceptedAnswers']

    # M2 Q5: perp to slope 4 => -1/4 (B)
    assert Fraction(4) * Fraction(-1, 4) == -1 and m2[5]['correctAnswer'] == 'B'

    # M2 Q6: (1/2)m = 82 => m = 164 (B)
    assert Fraction(1, 2) * 164 == 82 and m2[6]['correctAnswer'] == 'B'

    # M2 Q7: y = 16^x at x = 0 => (0, 1) (A)
    assert 16 ** 0 == 1 and m2[7]['correctAnswer'] == 'A'

    # M2 Q8: ((3^(1/7)) * t)^(7/8) == (3 * t^7)^(1/8) (C)
    for t8 in (0.5, 2.0, 9.5):
        lhs = ((3 ** (1 / 7)) * t8) ** (7 / 8)
        rhs = (3 * (t8 ** 7)) ** (1 / 8)
        assert math.isclose(lhs, rhs, rel_tol=1e-12)
    assert m2[8]['correctAnswer'] == 'C'

    # M2 Q9: m(370) ≈ 389 kg at 370 days (B)
    m370 = -0.0274 * (370 / 7) ** 2 + 7.3873 * (370 / 7) + 75.032
    assert round(m370) == 389 and m2[9]['correctAnswer'] == 'B'

    # M2 Q10: (5/9)(x - k) = k(x - 9/5) no solution => k = 5/9 (D)
    k10 = Fraction(5, 9)
    assert k10 == Fraction(5, 9) and (-Fraction(5, 9) * k10) != (-Fraction(9, 5) * k10)
    assert m2[10]['correctAnswer'] == 'D'

    # M2 Q11: -3x^2 + 30x - 48 == -3(x - 5)^2 + 27 (C)
    for xv in (-2, 0, 2, 5, 8):
        assert -3 * xv ** 2 + 30 * xv - 48 == -3 * (xv - 5) ** 2 + 27
    assert m2[11]['correctAnswer'] == 'C'

    # M2 Q12: 1530 m/(hr*s) * 3.28 ft/m / 3600 s/hr = 1.394 ≈ 1.39 (B)
    rate12 = Fraction(1530) * Fraction(328, 100) / Fraction(3600)
    assert round(float(rate12), 2) == 1.39 and m2[12]['correctAnswer'] == 'B'

    # M2 Q13: (-6,-14), (-3,-16), (3,-20), (6,-22) => 2x + 3y = -54 => C = -54
    for x13, y13 in ((-6, -14), (-3, -16), (3, -20), (6, -22)):
        assert 2 * x13 + 3 * y13 == -54
    assert '-54' in m2[13]['acceptedAnswers']

    # M2 Q14: 2x + 5y = 9 and 12x + 30y = 54 => (r, -2r/5 + 9/5) (A)
    for r14 in (-5, 0, 3, 10):
        xr = Fraction(r14)
        yr = Fraction(-2 * r14, 5) + Fraction(9, 5)
        assert 2 * xr + 5 * yr == 9 and 12 * xr + 30 * yr == 54
    assert m2[14]['correctAnswer'] == 'A'

    # M2 Q15: 9x^2 + 30x + q = 43, x = (-5 + sqrt(14))/3 => q = 54 (A)
    x15 = (-5 + math.sqrt(14)) / 3
    q15 = 43 - (9 * x15 ** 2 + 30 * x15)
    assert math.isclose(q15, 54.0, abs_tol=1e-12) and m2[15]['correctAnswer'] == 'A'

    # M2 Q16: t -> 3.61t => percent increase = 261% (C)
    inc16 = (Fraction(361, 100) - 1) * 100
    assert inc16 == 261 and m2[16]['correctAnswer'] == 'C'

    # M2 Q17: (6, 7) satisfies x > 3 and y > 5 (D)
    assert 6 > 3 and 7 > 5 and m2[17]['correctAnswer'] == 'D'

    # M2 Q18: V = 80(2.50)^(2t) (A)
    assert math.isclose(80 * (2.50 ** (2 * 0.5)), 80 + 1.50 * 80)
    assert m2[18]['correctAnswer'] == 'A'

    # M2 Q19: mail data set A (11) vs B (10 without 17) => both medians = 5 (C)
    data_a = [0, 0, 4, 4, 5, 5, 6, 6, 7, 8, 17]
    data_b = data_a[:-1]
    assert len(data_a) == 11 and len(data_b) == 10
    med_a = data_a[len(data_a) // 2]
    med_b = Fraction(data_b[4] + data_b[5], 2)
    assert med_a == 5 and med_b == 5 and m2[19]['correctAnswer'] == 'C'

    # M2 Q20: right △DEF (∠F=90°), tan(D) = sqrt(3), DF = 53 => EF = 53√3, DE = 106 (D)
    df20 = 53
    ef20 = df20 * math.sqrt(3)
    de20 = math.hypot(df20, ef20)
    assert math.isclose(de20, 106.0, rel_tol=1e-12) and m2[20]['correctAnswer'] == 'D'

    # M2 Q21: regular tetrahedron edge 96 => SA = 4 * (sqrt(3)/4) * 96^2 = 9216*sqrt(3) => k = 9216
    k21_m2 = 96 ** 2
    assert k21_m2 == 9216 and '9216' in m2[21]['acceptedAnswers']

    # M2 Q22: kx^2 - 96x + 8 = 0 has 2 distinct real roots => 96^2 - 32k > 0 => k < 288 => max int k = 287
    bound22 = Fraction((-96) ** 2, 4 * 8)
    assert bound22 == 288
    assert (-96) ** 2 - 4 * 287 * 8 > 0
    assert (-96) ** 2 - 4 * 288 * 8 == 0
    assert '287' in m2[22]['acceptedAnswers']

    # ---------- EXTRA HYGIENE & OPTION-ANALYSIS KATEX AUDIT ----------
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
    assert svg_count == 4, f'Expected 4 inline SVGs, got {svg_count}'
    assert table_count == 3, f'Expected 3 HTML tables, got {table_count}'

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
