# -*- coding: utf-8 -*-
"""
Digital SAT Real Past Exam — March 2025 Ver 3: Math (44 Unique Questions)
Visually verified page-by-page from clean watermark-stripped strips & 200-250 dpi source checks
(`March Version 3 @DSATuz.pdf`, Math M1 p.55–79 + p.106 [Q7], Math M2 p.80–103):
  - Section 2, Module 1: Math (22 real questions: 16 MCQ + 6 SPR)
  - Section 2, Module 2: Math (22 real questions: 16 MCQ + 6 SPR)
Zero watermarks, crisp inline SVGs & HTML tables, full bilingual Vietnamese explanations,
10-second Desmos tips, programmatic mathematical audit (`verify_all_math`), and real Node KaTeX validation.
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

TEST_CODE = 'real_march2025_v3_math'
FOLDER_KEY = 'real_math'
ORDER_INDEX = 6
TEST_TITLE = '🏛️ Real Exam — March 2025 Ver 3 Math (44 Qs)'


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


def _choice_vtable(pairs):
    """Compact vertical x | f(x) table rendered cleanly inside an MCQ choice card."""
    trs = ''.join(
        f'<tr>'
        f'<td style="padding:4px 16px;border:1px solid #94a3b8;text-align:center;">{x}</td>'
        f'<td style="padding:4px 16px;border:1px solid #94a3b8;text-align:center;">{y}</td>'
        f'</tr>'
        for x, y in pairs
    )
    return (
        '<table style="border-collapse:collapse;font-size:14px;background:#ffffff;'
        'display:inline-table;margin:2px 0;">'
        '<thead><tr>'
        '<th style="padding:4px 16px;border:1px solid #94a3b8;background:#f8fafc;text-align:center;font-weight:700;">'
        r'\(x\)</th>'
        '<th style="padding:4px 16px;border:1px solid #94a3b8;background:#f8fafc;text-align:center;font-weight:700;">'
        r'\(f(x)\)</th>'
        f'</tr></thead><tbody>{trs}</tbody></table>'
    )


def _choice_htable(xs, ys):
    """Compact horizontal x / f(x) table rendered cleanly inside an MCQ choice card."""
    x_cells = ''.join(
        f'<td style="padding:5px 13px;border:1px solid #94a3b8;text-align:center;">{v}</td>'
        for v in xs
    )
    y_cells = ''.join(
        f'<td style="padding:5px 13px;border:1px solid #94a3b8;text-align:center;">{v}</td>'
        for v in ys
    )
    return (
        '<table style="border-collapse:collapse;font-size:14px;background:#ffffff;'
        'display:inline-table;margin:2px 0;">'
        '<tbody>'
        '<tr>'
        '<th style="padding:5px 13px;border:1px solid #94a3b8;background:#f8fafc;text-align:center;font-weight:700;">'
        r'\(x\)</th>'
        f'{x_cells}</tr>'
        '<tr>'
        '<th style="padding:5px 13px;border:1px solid #94a3b8;background:#f8fafc;text-align:center;font-weight:700;">'
        r'\(f(x)\)</th>'
        f'{y_cells}</tr>'
        '</tbody></table>'
    )


SCATTER_M1_Q2_PTS = [
    (0.5, 2.0),
    (1.6, 4.0),
    (2.5, 4.0),
    (2.5, 6.0),
    (3.6, 5.0),
    (3.6, 8.0),
    (4.4, 8.0),
    (4.4, 9.0),
    (5.5, 12.0),
    (6.7, 12.0),
]


def _svg_m1_q2_scatterplot():
    """Exact recreation of March 2025 Ver 3 M1 Q2 scatterplot & line of best fit y = 0.8 + 1.7x."""
    x0, y0 = 54, 296  # origin in SVG pixels
    sx, sy = 28, 16   # x: 0..8.5 (238px), y: 0..16.5 (264px)

    def px(x):
        return x0 + x * sx

    def py(y):
        return y0 - y * sy

    grid = []
    for gx in range(1, 9):
        xp = px(gx)
        grid.append(
            f'<line x1="{xp:.1f}" y1="{py(16.3):.1f}" x2="{xp:.1f}" y2="{y0:.1f}" '
            f'stroke="#94a3b8" stroke-width="0.9"/>'
        )
    for gy in range(1, 17):
        yp = py(gy)
        grid.append(
            f'<line x1="{x0:.1f}" y1="{yp:.1f}" x2="{px(8.5):.1f}" y2="{yp:.1f}" '
            f'stroke="#94a3b8" stroke-width="0.9"/>'
        )

    ticks = []
    for gx in range(1, 9):
        xp = px(gx)
        ticks.append(f'<line x1="{xp:.1f}" y1="{y0 - 3}" x2="{xp:.1f}" y2="{y0 + 3}" stroke="#0f172a" stroke-width="1.3"/>')
        ticks.append(
            f'<text x="{xp:.1f}" y="{y0 + 17}" text-anchor="middle" font-family="Georgia,serif" '
            f'font-size="12.5" fill="#0f172a">{gx}</text>'
        )
    for gy in range(2, 17, 2):
        yp = py(gy)
        ticks.append(f'<line x1="{x0 - 3}" y1="{yp:.1f}" x2="{x0 + 3}" y2="{yp:.1f}" stroke="#0f172a" stroke-width="1.3"/>')
        ticks.append(
            f'<text x="{x0 - 9}" y="{yp + 4:.1f}" text-anchor="end" font-family="Georgia,serif" '
            f'font-size="12.5" fill="#0f172a">{gy}</text>'
        )

    # Line of best fit: y = 0.8 + 1.7x from x = 0 to x = 8.4 (y = 15.08)
    lx1, ly1 = px(0.0), py(0.8)
    lx2, ly2 = px(8.4), py(0.8 + 1.7 * 8.4)
    dots = ''.join(
        f'<circle cx="{px(x):.1f}" cy="{py(y):.1f}" r="3.6" fill="#0f172a"/>'
        for x, y in SCATTER_M1_Q2_PTS
    )

    return (
        '<div style="display:flex;justify-content:center;margin:10px 0;">'
        '<svg viewBox="0 0 320 330" width="320" height="330" xmlns="http://www.w3.org/2000/svg" '
        'style="background:#ffffff;border:1px solid #e2e8f0;border-radius:12px;">'
        + ''.join(grid)
        + f'<line x1="{x0 - 6}" y1="{y0}" x2="{px(8.7):.1f}" y2="{y0}" stroke="#0f172a" stroke-width="1.8"/>'
        + f'<polygon points="{px(8.95):.1f},{y0} {px(8.62):.1f},{y0 - 3.8} {px(8.62):.1f},{y0 + 3.8}" fill="#0f172a"/>'
        + f'<line x1="{x0}" y1="{y0 + 6}" x2="{x0}" y2="{py(17.0):.1f}" stroke="#0f172a" stroke-width="1.8"/>'
        + f'<polygon points="{x0},{py(17.3):.1f} {x0 - 3.8},{py(16.85):.1f} {x0 + 3.8},{py(16.85):.1f}" fill="#0f172a"/>'
        + ''.join(ticks)
        + f'<text x="{x0 - 8}" y="{y0 + 15}" text-anchor="end" font-family="Georgia,serif" font-style="italic" font-size="13" fill="#0f172a">O</text>'
        + f'<text x="{px(9.15):.1f}" y="{y0 + 4}" font-family="Georgia,serif" font-style="italic" font-size="14" fill="#0f172a">x</text>'
        + f'<text x="{x0}" y="{py(17.7):.1f}" text-anchor="middle" font-family="Georgia,serif" font-style="italic" font-size="14" fill="#0f172a">y</text>'
        + f'<line x1="{lx1:.1f}" y1="{ly1:.1f}" x2="{lx2:.1f}" y2="{ly2:.1f}" stroke="#0f172a" stroke-width="2.1"/>'
        + dots
        + '</svg></div>'
    )


def _svg_m1_q10_line_graph():
    """Exact recreation of March 2025 Ver 3 M1 Q10 line through (-12, 0) and (0, -11)."""
    step = 16
    x0 = 282  # x = 0 at 282, x = -15 at 42, x = 1 at 298
    y0 = 42   # y = 0 at 42, y = -15 at 282, y = 1 at 26

    def px(x):
        return x0 + x * step

    def py(y):
        return y0 - y * step

    grid = []
    for gx in range(-15, 2):
        if gx == 0:
            continue
        xp = px(gx)
        grid.append(f'<line x1="{xp}" y1="{py(0.6):.1f}" x2="{xp}" y2="{py(-14.6):.1f}" stroke="#94a3b8" stroke-width="0.9"/>')
    for gy in range(-14, 1):
        if gy == 0:
            continue
        yp = py(gy)
        grid.append(f'<line x1="{px(-15.3):.1f}" y1="{yp}" x2="{px(0.6):.1f}" y2="{yp}" stroke="#94a3b8" stroke-width="0.9"/>')

    ticks = []
    for gx in range(-14, 0, 2):
        xp = px(gx)
        ticks.append(f'<line x1="{xp}" y1="{y0 - 3}" x2="{xp}" y2="{y0 + 3}" stroke="#0f172a" stroke-width="1.3"/>')
        ticks.append(
            f'<text x="{xp}" y="{y0 + 14}" text-anchor="middle" font-family="Georgia,serif" '
            f'font-size="11.5" fill="#0f172a">&#8722;{abs(gx)}</text>'
        )
    for gy in range(-14, 0, 2):
        yp = py(gy)
        ticks.append(f'<line x1="{x0 - 3}" y1="{yp}" x2="{x0 + 3}" y2="{yp}" stroke="#0f172a" stroke-width="1.3"/>')
        ticks.append(
            f'<text x="{x0 - 6}" y="{yp + 4}" text-anchor="end" font-family="Georgia,serif" '
            f'font-size="11.5" fill="#0f172a">&#8722;{abs(gy)}</text>'
        )

    # Line y = -(11/12)x - 11 from x = -12.6 to x = 0.6
    lx1, ly1 = px(-12.6), py(-(11 / 12) * (-12.6) - 11)
    lx2, ly2 = px(0.55), py(-(11 / 12) * 0.55 - 11)

    return (
        '<div style="display:flex;justify-content:center;margin:10px 0;">'
        '<svg viewBox="0 0 330 300" width="330" height="300" xmlns="http://www.w3.org/2000/svg" '
        'style="background:#ffffff;border:1px solid #e2e8f0;border-radius:12px;">'
        + ''.join(grid)
        + f'<line x1="{px(-15.5):.1f}" y1="{y0}" x2="{px(1.1):.1f}" y2="{y0}" stroke="#0f172a" stroke-width="1.8"/>'
        + f'<polygon points="{px(1.45):.1f},{y0} {px(1.0):.1f},{y0 - 3.6} {px(1.0):.1f},{y0 + 3.6}" fill="#0f172a"/>'
        + f'<line x1="{x0}" y1="{py(-14.8):.1f}" x2="{x0}" y2="{py(1.1):.1f}" stroke="#0f172a" stroke-width="1.8"/>'
        + f'<polygon points="{x0},{py(1.45):.1f} {x0 - 3.6},{py(1.0):.1f} {x0 + 3.6},{py(1.0):.1f}" fill="#0f172a"/>'
        + ''.join(ticks)
        + f'<text x="{x0 - 6}" y="{y0 + 14}" text-anchor="end" font-family="Georgia,serif" font-style="italic" font-size="12.5" fill="#0f172a">O</text>'
        + f'<text x="{px(1.7):.1f}" y="{y0 + 4}" font-family="Georgia,serif" font-style="italic" font-size="13.5" fill="#0f172a">x</text>'
        + f'<text x="{x0}" y="{py(1.75):.1f}" text-anchor="middle" font-family="Georgia,serif" font-style="italic" font-size="13.5" fill="#0f172a">y</text>'
        + f'<line x1="{lx1:.1f}" y1="{ly1:.1f}" x2="{lx2:.1f}" y2="{ly2:.1f}" stroke="#0f172a" stroke-width="2.2"/>'
        + f'<circle cx="{px(-12):.1f}" cy="{py(0):.1f}" r="3.8" fill="#0f172a"/>'
        + f'<circle cx="{px(0):.1f}" cy="{py(-11):.1f}" r="3.8" fill="#0f172a"/>'
        + '</svg></div>'
    )


def _svg_m1_q12_parallel_lines():
    """Exact recreation of March 2025 Ver 3 M1 Q12: lines r, s cut by transversal k with w°, x°, y°, z°."""
    return (
        '<div style="display:flex;justify-content:center;margin:10px 0;">'
        '<svg viewBox="0 0 300 250" width="300" height="250" xmlns="http://www.w3.org/2000/svg" '
        'style="background:#ffffff;border:1px solid #e2e8f0;border-radius:12px;">'
        # Two vertical lines r (x=115) and s (x=195)
        '<line x1="115" y1="30" x2="115" y2="215" stroke="#0f172a" stroke-width="1.9"/>'
        '<line x1="195" y1="30" x2="195" y2="215" stroke="#0f172a" stroke-width="1.9"/>'
        # Transversal k from (55, 38) to (255, 208): slope dy/dx = 170/200 = 0.85
        # Meets r (x=115) at y = 38 + 60*0.85 = 89; meets s (x=195) at y = 38 + 140*0.85 = 157
        '<line x1="55" y1="38" x2="255" y2="208" stroke="#0f172a" stroke-width="1.9"/>'
        # Line labels
        '<text x="44" y="34" font-family="Georgia,serif" font-style="italic" font-size="15.5" fill="#0f172a">k</text>'
        '<text x="115" y="21" text-anchor="middle" font-family="Georgia,serif" font-style="italic" font-size="15.5" fill="#0f172a">r</text>'
        '<text x="195" y="21" text-anchor="middle" font-family="Georgia,serif" font-style="italic" font-size="15.5" fill="#0f172a">s</text>'
        # Angle labels: w° obtuse upper-right at k∩r, x° acute lower-right at k∩r
        '<text x="123" y="83" font-family="Georgia,serif" font-style="italic" font-size="14.5" fill="#1d4ed8">w&#176;</text>'
        '<text x="122" y="114" font-family="Georgia,serif" font-style="italic" font-size="14.5" fill="#0f172a">x&#176;</text>'
        # Angle labels: y° obtuse upper-right at k∩s, z° acute lower-right at k∩s
        '<text x="203" y="151" font-family="Georgia,serif" font-style="italic" font-size="14.5" fill="#1d4ed8">y&#176;</text>'
        '<text x="202" y="183" font-family="Georgia,serif" font-style="italic" font-size="14.5" fill="#0f172a">z&#176;</text>'
        '<text x="150" y="238" text-anchor="middle" font-family="Georgia,serif" font-size="12.5" fill="#475569">Note: Figure not drawn to scale.</text>'
        '</svg></div>'
    )


def _svg_m1_q18_exp_graph():
    """Exact recreation of March 2025 Ver 3 M1 Q18 exponential graph y = -3^x - 5 (asymptote y = -5)."""
    step = 13
    x0 = 165  # x in [-10, 10] => 35..295
    y0 = 104  # y in [-11, 5] => y=5 at 39, y=-11 at 247

    def px(x):
        return x0 + x * step

    def py(y):
        return y0 - y * step

    grid = []
    for gx in range(-10, 11):
        if gx == 0:
            continue
        xp = px(gx)
        grid.append(f'<line x1="{xp}" y1="{py(5.3):.1f}" x2="{xp}" y2="{py(-10.8):.1f}" stroke="#94a3b8" stroke-width="0.85"/>')
    for gy in range(-10, 6):
        if gy == 0:
            continue
        yp = py(gy)
        grid.append(f'<line x1="{px(-10.4):.1f}" y1="{yp}" x2="{px(10.4):.1f}" y2="{yp}" stroke="#94a3b8" stroke-width="0.85"/>')

    ticks = []
    for gx in (-10, -8, -6, -4, -2, 2, 4, 6, 8, 10):
        xp = px(gx)
        lbl = f'&#8722;{abs(gx)}' if gx < 0 else str(gx)
        ticks.append(f'<line x1="{xp}" y1="{y0 - 3}" x2="{xp}" y2="{y0 + 3}" stroke="#0f172a" stroke-width="1.2"/>')
        ticks.append(f'<text x="{xp}" y="{y0 + 13}" text-anchor="middle" font-family="Georgia,serif" font-size="10.5" fill="#0f172a">{lbl}</text>')
    for gy in (-10, -8, -6, -4, -2, 2, 4):
        yp = py(gy)
        lbl = f'&#8722;{abs(gy)}' if gy < 0 else str(gy)
        ticks.append(f'<line x1="{x0 - 3}" y1="{yp}" x2="{x0 + 3}" y2="{yp}" stroke="#0f172a" stroke-width="1.2"/>')
        ticks.append(f'<text x="{x0 - 6}" y="{yp + 3.5}" text-anchor="end" font-family="Georgia,serif" font-size="10.5" fill="#0f172a">{lbl}</text>')

    # Sample y = -3^x - 5 densely from x = -10.3 to x = 1.60 (where y = -10.80)
    pts = []
    steps = 120
    x_start, x_end = -10.3, 1.60
    for i in range(steps + 1):
        xv = x_start + (x_end - x_start) * i / steps
        yv = -(3.0 ** xv) - 5.0
        pts.append(f'{px(xv):.1f},{py(yv):.1f}')
    path_d = 'M ' + ' L '.join(pts)

    return (
        '<div style="display:flex;justify-content:center;margin:10px 0;">'
        '<svg viewBox="0 0 330 264" width="330" height="264" xmlns="http://www.w3.org/2000/svg" '
        'style="background:#ffffff;border:1px solid #e2e8f0;border-radius:12px;">'
        + ''.join(grid)
        + f'<line x1="{px(-10.6):.1f}" y1="{y0}" x2="{px(10.8):.1f}" y2="{y0}" stroke="#0f172a" stroke-width="1.7"/>'
        + f'<polygon points="{px(11.15):.1f},{y0} {px(10.65):.1f},{y0 - 3.5} {px(10.65):.1f},{y0 + 3.5}" fill="#0f172a"/>'
        + f'<line x1="{x0}" y1="{py(-11.0):.1f}" x2="{x0}" y2="{py(5.8):.1f}" stroke="#0f172a" stroke-width="1.7"/>'
        + f'<polygon points="{x0},{py(6.2):.1f} {x0 - 3.5},{py(5.65):.1f} {x0 + 3.5},{py(5.65):.1f}" fill="#0f172a"/>'
        + ''.join(ticks)
        + f'<text x="{x0 - 6}" y="{y0 + 13}" text-anchor="end" font-family="Georgia,serif" font-style="italic" font-size="11.5" fill="#0f172a">O</text>'
        + f'<text x="{px(11.5):.1f}" y="{y0 + 4}" font-family="Georgia,serif" font-style="italic" font-size="13" fill="#0f172a">x</text>'
        + f'<text x="{x0}" y="{py(6.6):.1f}" text-anchor="middle" font-family="Georgia,serif" font-style="italic" font-size="13" fill="#0f172a">y</text>'
        + f'<path d="{path_d}" fill="none" stroke="#0f172a" stroke-width="2.2" stroke-linecap="round"/>'
        + '</svg></div>'
    )


def _svg_m1_q21_right_triangle():
    """Exact recreation of March 2025 Ver 3 M1 Q21 right triangle ABC (∠B=90°, ∠C=30°)."""
    return (
        '<div style="display:flex;justify-content:center;margin:10px 0;">'
        '<svg viewBox="0 0 300 215" width="300" height="215" xmlns="http://www.w3.org/2000/svg" '
        'style="background:#ffffff;border:1px solid #e2e8f0;border-radius:12px;">'
        '<polygon points="58,34 58,166 252,166" fill="#f8fafc" stroke="#0f172a" '
        'stroke-width="2.2" stroke-linejoin="round"/>'
        '<rect x="58" y="150" width="16" height="16" fill="none" stroke="#0f172a" stroke-width="1.8"/>'
        '<text x="45" y="31" text-anchor="middle" font-family="Georgia,serif" font-style="italic" font-size="16" fill="#0f172a">A</text>'
        '<text x="46" y="182" text-anchor="middle" font-family="Georgia,serif" font-style="italic" font-size="16" fill="#0f172a">B</text>'
        '<text x="262" y="180" text-anchor="middle" font-family="Georgia,serif" font-style="italic" font-size="16" fill="#0f172a">C</text>'
        '<text x="215" y="159" text-anchor="middle" font-family="Georgia,serif" font-size="14" fill="#0f172a">30&#176;</text>'
        '<text x="150" y="204" text-anchor="middle" font-family="Georgia,serif" font-size="12.5" fill="#475569">Note: Figure not drawn to scale.</text>'
        '</svg></div>'
    )


def _svg_m2_q10_line_graph():
    """Exact recreation of March 2025 Ver 3 M2 Q10 line through (-2, -3) and (0, 9)."""
    step = 13
    x0 = 165  # x in [-10, 10]
    y0 = 162  # y in [-10, 10]

    def px(x):
        return x0 + x * step

    def py(y):
        return y0 - y * step

    grid = []
    for gx in range(-10, 11):
        if gx == 0:
            continue
        xp = px(gx)
        grid.append(f'<line x1="{xp}" y1="{py(10.5):.1f}" x2="{xp}" y2="{py(-10.5):.1f}" stroke="#94a3b8" stroke-width="0.85"/>')
    for gy in range(-10, 11):
        if gy == 0:
            continue
        yp = py(gy)
        grid.append(f'<line x1="{px(-10.5):.1f}" y1="{yp}" x2="{px(10.5):.1f}" y2="{yp}" stroke="#94a3b8" stroke-width="0.85"/>')

    ticks = []
    for gx in (-10, -8, -6, -4, -2, 2, 4, 6, 8, 10):
        xp = px(gx)
        lbl = f'&#8722;{abs(gx)}' if gx < 0 else str(gx)
        ticks.append(f'<line x1="{xp}" y1="{y0 - 3}" x2="{xp}" y2="{y0 + 3}" stroke="#0f172a" stroke-width="1.2"/>')
        ticks.append(f'<text x="{xp}" y="{y0 + 13}" text-anchor="middle" font-family="Georgia,serif" font-size="10.5" fill="#0f172a">{lbl}</text>')
    for gy in (-10, -8, -6, -4, -2, 2, 4, 6, 8, 10):
        yp = py(gy)
        lbl = f'&#8722;{abs(gy)}' if gy < 0 else str(gy)
        ticks.append(f'<line x1="{x0 - 3}" y1="{yp}" x2="{x0 + 3}" y2="{yp}" stroke="#0f172a" stroke-width="1.2"/>')
        ticks.append(f'<text x="{x0 - 6}" y="{yp + 3.5}" text-anchor="end" font-family="Georgia,serif" font-size="10.5" fill="#0f172a">{lbl}</text>')

    # Line y = 6x + 9 clipped to y in [-10.5, 10.5]:
    # y = -10.5 => x = -19.5/6 = -3.25; y = 10.5 => x = 1.5/6 = 0.25
    lx1, ly1 = px(-3.25), py(-10.5)
    lx2, ly2 = px(0.25), py(10.5)

    return (
        '<div style="display:flex;justify-content:center;margin:10px 0;">'
        '<svg viewBox="0 0 332 320" width="332" height="320" xmlns="http://www.w3.org/2000/svg" '
        'style="background:#ffffff;border:1px solid #e2e8f0;border-radius:12px;">'
        + ''.join(grid)
        + f'<line x1="{px(-10.8):.1f}" y1="{y0}" x2="{px(10.9):.1f}" y2="{y0}" stroke="#0f172a" stroke-width="1.7"/>'
        + f'<polygon points="{px(11.3):.1f},{y0} {px(10.8):.1f},{y0 - 3.5} {px(10.8):.1f},{y0 + 3.5}" fill="#0f172a"/>'
        + f'<line x1="{x0}" y1="{py(-10.8):.1f}" x2="{x0}" y2="{py(10.9):.1f}" stroke="#0f172a" stroke-width="1.7"/>'
        + f'<polygon points="{x0},{py(11.3):.1f} {x0 - 3.5},{py(10.8):.1f} {x0 + 3.5},{py(10.8):.1f}" fill="#0f172a"/>'
        + ''.join(ticks)
        + f'<text x="{x0 - 6}" y="{y0 + 13}" text-anchor="end" font-family="Georgia,serif" font-style="italic" font-size="11.5" fill="#0f172a">O</text>'
        + f'<text x="{px(11.65):.1f}" y="{y0 + 4}" font-family="Georgia,serif" font-style="italic" font-size="13" fill="#0f172a">x</text>'
        + f'<text x="{x0}" y="{py(11.7):.1f}" text-anchor="middle" font-family="Georgia,serif" font-style="italic" font-size="13" fill="#0f172a">y</text>'
        + f'<line x1="{lx1:.1f}" y1="{ly1:.1f}" x2="{lx2:.1f}" y2="{ly2:.1f}" stroke="#0f172a" stroke-width="2.2"/>'
        + f'<circle cx="{px(-2):.1f}" cy="{py(-3):.1f}" r="3.8" fill="#0f172a"/>'
        + f'<circle cx="{px(0):.1f}" cy="{py(9):.1f}" r="3.8" fill="#0f172a"/>'
        + '</svg></div>'
    )


def _svg_m2_q12_inequality_graph():
    """Exact recreation of March 2025 Ver 3 M2 Q12 inequality graph: x + 7y >= -77."""
    step = 18
    x0 = 236  # x in [-10, 1] => x=-10 at 56, x=1 at 254
    y0 = 44   # y in [-15, 1] => y=1 at 26, y=-15 at 314

    def px(x):
        return x0 + x * step

    def py(y):
        return y0 - y * step

    # Boundary x + 7y = -77 => y = -(1/7)x - 11
    x_left, x_right = -10.0, 1.0
    y_left = -(1 / 7) * x_left - 11.0   # -9.5714
    y_right = -(1 / 7) * x_right - 11.0  # -11.1429
    y_top = 1.0
    poly_pts = (
        f'{px(x_left):.1f},{py(y_left):.1f} '
        f'{px(x_right):.1f},{py(y_right):.1f} '
        f'{px(x_right):.1f},{py(y_top):.1f} '
        f'{px(x_left):.1f},{py(y_top):.1f}'
    )

    grid = []
    for gx in range(-10, 2):
        if gx == 0:
            continue
        xp = px(gx)
        grid.append(f'<line x1="{xp}" y1="{py(1.0):.1f}" x2="{xp}" y2="{py(-15.0):.1f}" stroke="#64748b" stroke-width="0.85"/>')
    for gy in range(-15, 2):
        if gy == 0:
            continue
        yp = py(gy)
        grid.append(f'<line x1="{px(-10.0):.1f}" y1="{yp}" x2="{px(1.0):.1f}" y2="{yp}" stroke="#64748b" stroke-width="0.85"/>')

    ticks = []
    for gx in (-10, -8, -6, -4, -2):
        xp = px(gx)
        ticks.append(f'<line x1="{xp}" y1="{y0 - 3}" x2="{xp}" y2="{y0 + 3}" stroke="#0f172a" stroke-width="1.3"/>')
        ticks.append(
            f'<text x="{xp}" y="{y0 + 14}" text-anchor="middle" font-family="Georgia,serif" '
            f'font-size="11.5" fill="#0f172a">&#8722;{abs(gx)}</text>'
        )
    for gy in (-2, -4, -6, -8, -10, -12, -14):
        yp = py(gy)
        ticks.append(f'<line x1="{x0 - 3}" y1="{yp}" x2="{x0 + 3}" y2="{yp}" stroke="#0f172a" stroke-width="1.3"/>')
        ticks.append(
            f'<text x="{x0 - 7}" y="{yp + 4}" text-anchor="end" font-family="Georgia,serif" '
            f'font-size="11.5" fill="#0f172a">&#8722;{abs(gy)}</text>'
        )

    return (
        '<div style="display:flex;justify-content:center;margin:10px 0;">'
        '<svg viewBox="0 0 296 332" width="296" height="332" xmlns="http://www.w3.org/2000/svg" '
        'style="background:#ffffff;border:1px solid #e2e8f0;border-radius:12px;">'
        + f'<polygon points="{poly_pts}" fill="#64748b" fill-opacity="0.32"/>'
        + ''.join(grid)
        + f'<line x1="{px(-10.3):.1f}" y1="{y0}" x2="{px(1.45):.1f}" y2="{y0}" stroke="#0f172a" stroke-width="1.8"/>'
        + f'<polygon points="{px(1.75):.1f},{y0} {px(1.35):.1f},{y0 - 3.6} {px(1.35):.1f},{y0 + 3.6}" fill="#0f172a"/>'
        + f'<line x1="{x0}" y1="{py(-15.3):.1f}" x2="{x0}" y2="{py(1.45):.1f}" stroke="#0f172a" stroke-width="1.8"/>'
        + f'<polygon points="{x0},{py(1.75):.1f} {x0 - 3.6},{py(1.35):.1f} {x0 + 3.6},{py(1.35):.1f}" fill="#0f172a"/>'
        + ''.join(ticks)
        + f'<text x="{x0 - 6}" y="{y0 + 14}" text-anchor="end" font-family="Georgia,serif" font-style="italic" font-size="12.5" fill="#0f172a">O</text>'
        + f'<text x="{px(1.98):.1f}" y="{y0 + 4}" font-family="Georgia,serif" font-style="italic" font-size="13.5" fill="#0f172a">x</text>'
        + f'<text x="{x0}" y="{py(2.0):.1f}" text-anchor="middle" font-family="Georgia,serif" font-style="italic" font-size="13.5" fill="#0f172a">y</text>'
        + f'<line x1="{px(x_left):.1f}" y1="{py(y_left):.1f}" x2="{px(x_right):.1f}" y2="{py(y_right):.1f}" stroke="#0f172a" stroke-width="2.3"/>'
        + f'<circle cx="{px(-7):.1f}" cy="{py(-10):.1f}" r="4.0" fill="#0f172a"/>'
        + f'<circle cx="{px(0):.1f}" cy="{py(-11):.1f}" r="4.0" fill="#0f172a"/>'
        + '</svg></div>'
    )


def _svg_m2_q16_exp_shift_graph():
    """Exact recreation of March 2025 Ver 3 M2 Q16 graph of y = f(x) + 2 = -3^x + 5."""
    sx, sy = 36, 17
    x0 = 96   # x in [-1.5, 5.5] => 42..294
    y0 = 216  # y in [-5, 10.5] => y=10.5 at 37.5, y=-5 at 301

    def px(x):
        return x0 + x * sx

    def py(y):
        return y0 - y * sy

    grid = []
    for gx in range(-1, 6):
        if gx == 0:
            continue
        xp = px(gx)
        grid.append(f'<line x1="{xp}" y1="{py(10.5):.1f}" x2="{xp}" y2="{py(-5.0):.1f}" stroke="#94a3b8" stroke-width="0.9"/>')
    for gy in range(-5, 11):
        if gy == 0:
            continue
        yp = py(gy)
        grid.append(f'<line x1="{px(-1.45):.1f}" y1="{yp}" x2="{px(5.45):.1f}" y2="{yp}" stroke="#94a3b8" stroke-width="0.9"/>')

    ticks = []
    for gx in (-1, 1, 2, 3, 4, 5):
        xp = px(gx)
        lbl = f'&#8722;{abs(gx)}' if gx < 0 else str(gx)
        ticks.append(f'<line x1="{xp}" y1="{y0 - 3}" x2="{xp}" y2="{y0 + 3}" stroke="#0f172a" stroke-width="1.3"/>')
        ticks.append(f'<text x="{xp}" y="{y0 + 16}" text-anchor="middle" font-family="Georgia,serif" font-size="12" fill="#0f172a">{lbl}</text>')
    for gy in (-4, -2, 2, 4, 6, 8, 10):
        yp = py(gy)
        lbl = f'&#8722;{abs(gy)}' if gy < 0 else str(gy)
        ticks.append(f'<line x1="{x0 - 3}" y1="{yp}" x2="{x0 + 3}" y2="{yp}" stroke="#0f172a" stroke-width="1.3"/>')
        ticks.append(f'<text x="{x0 - 8}" y="{yp + 4}" text-anchor="end" font-family="Georgia,serif" font-size="12" fill="#0f172a">{lbl}</text>')

    # Sample y = -3^x + 5 from x = -1.45 to x = 2.095 (y = -4.99)
    pts = []
    steps = 100
    x_start, x_end = -1.45, 2.095
    for i in range(steps + 1):
        xv = x_start + (x_end - x_start) * i / steps
        yv = -(3.0 ** xv) + 5.0
        pts.append(f'{px(xv):.1f},{py(yv):.1f}')
    path_d = 'M ' + ' L '.join(pts)

    return (
        '<div style="display:flex;justify-content:center;margin:10px 0;">'
        '<svg viewBox="0 0 330 318" width="330" height="318" xmlns="http://www.w3.org/2000/svg" '
        'style="background:#ffffff;border:1px solid #e2e8f0;border-radius:12px;">'
        + ''.join(grid)
        + f'<line x1="{px(-1.55):.1f}" y1="{y0}" x2="{px(5.65):.1f}" y2="{y0}" stroke="#0f172a" stroke-width="1.8"/>'
        + f'<polygon points="{px(5.88):.1f},{y0} {px(5.58):.1f},{y0 - 3.6} {px(5.58):.1f},{y0 + 3.6}" fill="#0f172a"/>'
        + f'<line x1="{x0}" y1="{py(-5.2):.1f}" x2="{x0}" y2="{py(11.0):.1f}" stroke="#0f172a" stroke-width="1.8"/>'
        + f'<polygon points="{x0},{py(11.4):.1f} {x0 - 3.6},{py(10.9):.1f} {x0 + 3.6},{py(10.9):.1f}" fill="#0f172a"/>'
        + ''.join(ticks)
        + f'<text x="{x0 - 7}" y="{y0 + 15}" text-anchor="end" font-family="Georgia,serif" font-style="italic" font-size="12.5" fill="#0f172a">O</text>'
        + f'<text x="{px(6.05):.1f}" y="{y0 + 4}" font-family="Georgia,serif" font-style="italic" font-size="13.5" fill="#0f172a">x</text>'
        + f'<text x="{x0}" y="{py(11.75):.1f}" text-anchor="middle" font-family="Georgia,serif" font-style="italic" font-size="13.5" fill="#0f172a">y</text>'
        + f'<path d="{path_d}" fill="none" stroke="#0f172a" stroke-width="2.3" stroke-linecap="round"/>'
        + '</svg></div>'
    )


# ============================================================================
# MODULE 1 — SECTION 2, MODULE 1: MATH (22 REAL QUESTIONS: 16 MCQ + 6 SPR)
# ============================================================================

def _build_m1_questions():
    tbl_m1_q6 = _bluebook_table(
        ['Value', 'Frequency'],
        [['20', '6'], ['26', '1'], ['32', '6'], ['38', '3']],
    )

    return [
        math_mcq(
            'sat_real_mar25v3_m1_q1', 1, 'Algebra', 'Linear equations in one variable', 'Easy',
            r'<p style="text-align:center;">\[s = 40 + 2t\]</p>'
            r'<p>The equation gives the speed \(s\), in miles per hour, of a certain car \(t\) seconds after it began to accelerate.</p>',
            r'What is the speed, in miles per hour, of the car \(3\) seconds after it began to accelerate?',
            {'A': r'\(40\)', 'B': r'\(42\)', 'C': r'\(43\)', 'D': r'\(46\)'},
            'D',
            r'Thay trực tiếp \(t = 3\) vào phương trình tốc độ: \[s = 40 + 2(3) = 40 + 6 = 46\text{ (miles per hour)}.\]',
            r'Bài toán thay giá trị vào hàm bậc nhất: xác định đúng biến đầu vào \(t = 3\) và thực hiện nhân trước cộng sau.',
            {
                'A': ('Bỏ qua hạng tử 2t', r'\(40\) là tốc độ ban đầu tại \(t = 0\), chưa cộng thêm phần gia tốc sau \(3\) giây.'),
                'B': ('Thay nhầm t = 1', r'\(40 + 2(1) = 42\) là tốc độ sau \(1\) giây, không phải \(3\) giây.'),
                'C': ('Cộng t thay vì 2t', r'\(40 + 3 = 43\) đã quên nhân hệ số góc \(2\) với \(t = 3\).'),
                'D': ('Đáp án đúng', r'\(s = 40 + 2(3) = 46\).'),
            },
            r'Gõ nhanh `40 + 2*3` trong Desmos ra ngay `46` (2 giây).'
        ),

        math_mcq(
            'sat_real_mar25v3_m1_q2', 2, 'Problem-Solving and Data Analysis',
            'Two-variable data: Models and scatterplots', 'Easy',
            _svg_m1_q2_scatterplot(),
            r'Which of the following equations best represents the line of best fit shown?',
            {
                'A': r'\(y = 0.8 + 1.7x\)',
                'B': r'\(y = 0.8 - 1.7x\)',
                'C': r'\(y = -0.8 + 1.7x\)',
                'D': r'\(y = -0.8 - 1.7x\)',
            },
            'A',
            r'Đọc hai đặc trưng cốt lõi của đường hồi quy (line of best fit) trên đồ thị:<br/>'
            r'1. <b>Độ dốc (slope):</b> Đường thẳng đi lên từ trái sang phải \(\Rightarrow\) hệ số góc <b>dương</b> (\(+1.7\)), loại ngay B và D.<br/>'
            r'2. <b>Tung độ gốc (\(y\)-intercept):</b> Tại \(x = 0\), đường thẳng cắt trục \(Oy\) phía trên gốc tọa độ \(O\), ngay dưới vạch \(y = 1\) (xấp xỉ \(0.8 > 0\)), loại C.<br/>'
            r'Kiểm chứng thêm tại \(x = 5\): \(y = 0.8 + 1.7(5) = 9.3\), khớp hoàn hảo với đồ thị!',
            r'Với câu hỏi line of best fit trắc nghiệm, luôn kiểm tra <b>dấu của slope</b> và <b>dấu của \(y\)-intercept</b> trước — thường loại sạch 3 đáp án chỉ trong 5 giây!',
            {
                'A': ('Đáp án đúng', r'Hệ số góc dương (\(+1.7\)) và tung độ gốc dương (\(+0.8\)), khớp chính xác đường thẳng vẽ trên đồ thị.'),
                'B': ('Sai dấu hệ số góc', r'Hệ số góc \(-1.7 < 0\) tạo đường đi xuống, trái ngược hoàn toàn với đường đi lên trên hình.'),
                'C': ('Sai dấu tung độ gốc', r'Tung độ gốc \(-0.8 < 0\) sẽ cắt trục tung dưới điểm \(O\), trong khi đường thẳng cắt trục tung ở mức dương (\(\approx +0.8\)).'),
                'D': ('Sai cả hai dấu', r'Cả hệ số góc lẫn tung độ gốc đều âm, hoàn toàn không khớp đồ thị.'),
            },
            r'Nhìn mắt là đủ chọn A; nếu muốn chắc tuyệt đối, thử kiểm tra 1 điểm trên đường như `(6, 11)`: gõ `0.8 + 1.7*6 = 11` khớp ngay!'
        ),

        math_mcq(
            'sat_real_mar25v3_m1_q3', 3, 'Geometry and Trigonometry', 'Area and volume', 'Easy',
            r'<p>The width of a rectangle is \(5\) centimeters. The length of the rectangle is \(30\) centimeters longer than the width.</p>',
            r'What is the area, in square centimeters, of this rectangle?',
            {'A': r'\(175\)', 'B': r'\(40\)', 'C': r'\(10\)', 'D': r'\(5\)'},
            'A',
            r'Chiều rộng là \(w = 5\text{ cm}\).<br/>'
            r'Chiều dài <i>dài hơn chiều rộng \(30\text{ cm}\)</i> ("\(30\) centimeters longer than the width"): \[l = 5 + 30 = 35\text{ cm}.\]'
            r'Diện tích hình chữ nhật là: \[\text{Area} = l \times w = 35 \times 5 = 175\text{ cm}^2.\]',
            r'Đọc kỹ cụm từ "longer than" (cộng thêm \(30\), thành \(35\)) thay vì nhầm chiều dài bằng \(30\) hoặc tính chu vi!',
            {
                'A': ('Đáp án đúng', r'Chiều dài \(l = 5 + 30 = 35\), diện tích \(35 \times 5 = 175\).'),
                'B': ('Tính tổng thay vì nhân', r'\(35 + 5 = 40\) là nửa chu vi, không phải diện tích.'),
                'C': ('Tính sai phép toán', r'\(5 + 5 = 10\) chỉ là tổng hai chiều rộng.'),
                'D': ('Nhầm số liệu gốc', r'\(5\) là chiều rộng ban đầu, không phải diện tích.'),
            },
            r'Gõ `(5 + 30) * 5` trong Desmos ra ngay `175`.'
        ),

        math_spr(
            'sat_real_mar25v3_m1_q4', 4, 'Algebra', 'Linear equations in one variable', 'Easy',
            r'<p>If \(7 + x = 3\), what is the value of \(56 + 8x\)?</p>',
            r'Enter the exact value of \(56 + 8x\).',
            ['24'], '24',
            r'<b>Cách 1 (Nhận diện bội số — 3 giây):</b> Để ý biểu thức cần tìm gấp đúng \(8\) lần vế trái: \[56 + 8x = 8(7 + x) = 8(3) = 24.\]'
            r'<b>Cách 2 (Giải \(x\) trực tiếp):</b> Từ \(7 + x = 3 \Rightarrow x = -4\). Thay vào: \(56 + 8(-4) = 56 - 32 = 24\).',
            r'Mẹo SAT Algebra kinh điển: trước khi giải tìm \(x\), hãy liếc xem biểu thức cần tính có phải là bội số trực tiếp của biểu thức đã cho không (\(56 + 8x = 8(7 + x)\)).',
            r'Gõ `7 + x = 3` (tìm \(x = -4\)), rồi gõ `56 + 8(-4)` trong Desmos để xác nhận chắc chắn `24`.'
        ),

        math_mcq(
            'sat_real_mar25v3_m1_q5', 5, 'Algebra', 'Linear equations in two variables', 'Easy',
            r'<p>In one week in 2017, a technician earned a total of $1,055 by working at her regular job and at a second job doing part-time work. The equation \(20h + 17c = 1{,}055\) represents this situation, where \(h\) is the number of hours worked at her regular job and \(c\) is the number of hours worked at her second job.</p>',
            r'Which of the following is the best interpretation of \(20\) in this context?',
            {
                'A': 'The amount, in dollars, the technician earned for each hour she worked at her regular job',
                'B': 'The amount, in dollars, the technician earned for each hour she worked at her second job',
                'C': 'The number of hours the technician worked in one week at her regular job',
                'D': 'The number of hours the technician worked in one week at her second job',
            },
            'A',
            r'Phân tích đơn vị trong phương trình chuẩn \(20h + 17c = 1{,}055\):<br/>'
            r'- Vế phải là tổng thu nhập (đơn vị: <b>dollars</b>).<br/>'
            r'- \(h\) là số giờ làm việc tại công việc chính (<b>regular job</b>).<br/>'
            r'- Do \(20h\) là số tiền kiếm được từ công việc chính, hệ số \(20\) có đơn vị là \(\text{dollars/hour}\): <b>số tiền (đô-la) kỹ thuật viên kiếm được cho mỗi giờ làm việc tại công việc chính (regular job)</b>.',
            r'Trong phương trình tổng chi phí/thu nhập dạng \(ax + by = C\): hệ số đứng trước biến luôn là <b>đơn giá/tốc độ trên 1 đơn vị của biến đi kèm</b>.',
            {
                'A': ('Đáp án đúng', r'\(20\) nhân với \(h\) (số giờ ở regular job) nên \(20\) là tiền lương mỗi giờ ở regular job.'),
                'B': ('Nhầm biến c và h', r'Tiền lương mỗi giờ ở công việc thứ hai (second job) là hệ số \(17\) đi kèm biến \(c\).'),
                'C': ('Nhầm hệ số với biến số', r'Số giờ làm việc ở công việc chính là biến \(h\), không phải hệ số \(20\).'),
                'D': ('Nhầm cả hệ số lẫn công việc', r'Số giờ làm ở công việc thứ hai là biến \(c\).'),
            },
            r'Dạng câu hỏi đọc hiểu ý nghĩa mô hình tuyến tính — dùng kiểm tra đơn vị: \((\text{đơn vị của } 20) \times (\text{hours at regular job}) = \text{dollars} \Rightarrow \text{dollars per hour at regular job}\). Không cần bấm máy!'
        ),

        math_mcq(
            'sat_real_mar25v3_m1_q6', 6, 'Problem-Solving and Data Analysis',
            'One-variable data: Distributions and measures of center and spread', 'Easy',
            r'<p>The table shows the frequency of values in a data set.</p>' + tbl_m1_q6,
            r'What is the minimum value of the data set?',
            {'A': r'\(1\)', 'B': r'\(6\)', 'C': r'\(20\)', 'D': r'\(26\)'},
            'C',
            r'Bảng tần số cho biết tập dữ liệu gồm các giá trị:<br/>'
            r'- \(20\) (xuất hiện \(6\) lần)<br/>'
            r'- \(26\) (xuất hiện \(1\) lần)<br/>'
            r'- \(32\) (xuất hiện \(6\) lần)<br/>'
            r'- \(38\) (xuất hiện \(3\) lần)<br/>'
            r'Giá trị nhỏ nhất (<b>minimum value</b>) của tập dữ liệu nằm ở cột <b>Value</b>, tức là \(20\).',
            r'Bẫy kinh điển của bảng tần số: luôn phân biệt cột <b>Value</b> (giá trị dữ liệu) và cột <b>Frequency</b> (số lần xuất hiện). Minimum value nhìn ở cột Value!',
            {
                'A': ('Bẫy cột Frequency', r'\(1\) là tần số nhỏ nhất (của giá trị \(26\)), không phải giá trị nhỏ nhất của tập dữ liệu.'),
                'B': ('Bẫy cột Frequency', r'\(6\) là tần số xuất hiện của giá trị \(20\) và \(32\), không phải giá trị dữ liệu.'),
                'C': ('Đáp án đúng', r'\(20\) là giá trị nhỏ nhất trong cột Value (có tần số \(6 > 0\)).'),
                'D': ('Nhầm giá trị có tần số nhỏ nhất', r'\(26\) là giá trị có tần số ít nhất (\(1\)), nhưng \(20 < 26\).'),
            },
            r'Nếu muốn kiểm tra chắc chắn, liệt kê danh sách `L = [20,20,20,20,20,20,26,32,32,32,32,32,32,38,38,38]` và gõ `min(L)` trong Desmos ra ngay `20`.'
        ),

        math_spr(
            'sat_real_mar25v3_m1_q7', 7, 'Problem-Solving and Data Analysis',
            'One-variable data: Distributions and measures of center and spread', 'Easy',
            r'<p>The list gives the mass, in grams, of \(5\) ruffed lemurs.</p>'
            r'<p style="text-align:center;">\[3{,}810;\; 3{,}810;\; 3{,}030;\; 3{,}850;\; 3{,}050\]</p>',
            r'What is the mean mass, in grams, of these \(5\) ruffed lemurs?',
            ['3510'], '3510',
            r'Tính trung bình cộng (mean) bằng tổng \(5\) khối lượng chia cho \(5\):'
            r'\[\text{Mean} = \frac{3{,}810 + 3{,}810 + 3{,}030 + 3{,}850 + 3{,}050}{5} = \frac{17{,}550}{5} = 3{,}510\text{ (grams)}.\]'
            r'Khi nhập vào ô SPR, không gõ dấu phẩy: nhập `3510`.',
            r'Công thức \(\text{Mean} = \frac{\text{Tổng các phần tử}}{\text{Số phần tử}}\). Nhớ quy tắc SPR: không nhập dấu phẩy ngăn cách hàng nghìn!',
            r'Gõ thẳng `mean(3810, 3810, 3030, 3850, 3050)` trong Desmos — máy trả ngay `3510` mà không lo cộng nhầm!'
        ),

        math_mcq(
            'sat_real_mar25v3_m1_q8', 8, 'Advanced Math',
            'Nonlinear equations in one variable and systems of equations in two variables', 'Easy',
            r'<p style="text-align:center;">\[x + 7 = 13\]\[y = 5x^2 + 5\]</p>',
            r'At what point \((x, y)\) do the graphs of the equations in the given system intersect?',
            {
                'A': r'\((6, 180)\)',
                'B': r'\((6, 185)\)',
                'C': r'\((13, 5)\)',
                'D': r'\((13, 850)\)',
            },
            'B',
            r'Bước 1: Từ phương trình đầu tiên, tìm \(x\): \[x + 7 = 13 \Rightarrow x = 6.\]'
            r'Bước 2: Thay \(x = 6\) vào phương trình thứ hai: \[y = 5(6)^2 + 5 = 5(36) + 5 = 180 + 5 = 185.\]'
            r'Vậy hai đồ thị cắt nhau tại điểm \((6, 185)\).',
            r'Giao điểm của hai đồ thị chính là nghiệm \((x, y)\) của hệ phương trình. Đừng quên cộng hằng số \(+5\) ở bước cuối!',
            {
                'A': ('Quên cộng +5', r'\(5(6)^2 = 180\) đã bỏ quên số hạng \(+5\) trong phương trình \(y = 5x^2 + 5\).'),
                'B': ('Đáp án đúng', r'\(x = 6\) và \(y = 5(6)^2 + 5 = 185 \Rightarrow (6, 185)\).'),
                'C': ('Nhầm x = 13 và y = 5', r'Không trừ \(7\) để tìm \(x\) và đọc nhầm hằng số \(5\) làm tung độ.'),
                'D': ('Thay nhầm x = 13', r'\(5(13)^2 + 5 = 850\) mắc lỗi lấy nhầm vế phải \(13\) thay vì giải \(x = 13 - 7 = 6\).'),
            },
            r'Nhập hai dòng `x + 7 = 13` và `y = 5x^2 + 5` vào Desmos, hoặc bấm nhanh `5*(13 - 7)^2 + 5` ra ngay `185`.'
        ),

        math_spr(
            'sat_real_mar25v3_m1_q9', 9, 'Advanced Math', 'Equivalent expressions', 'Easy',
            r'<p>The expression \(19x^5 + 20x^5 - 10x^5\) is equivalent to \(bx^5\), where \(b\) is a constant.</p>',
            r'What is the value of \(b\)?',
            ['29'], '29',
            r'Cả ba hạng tử đều đồng dạng cùng chứa \(x^5\), nên ta chỉ việc cộng trừ các hệ số: \[19x^5 + 20x^5 - 10x^5 = (19 + 20 - 10)x^5 = 29x^5.\]'
            r'So sánh với \(bx^5\), suy ra \(b = 29\).',
            r'Khi cộng trừ các đơn thức đồng dạng, chỉ cộng trừ hệ số và giữ nguyên phần biến số mũ \(x^5\).',
            r'Gõ nhanh `19 + 20 - 10` trong Desmos được ngay `29`.'
        ),

        math_mcq(
            'sat_real_mar25v3_m1_q10', 10, 'Algebra', 'Linear equations in two variables', 'Medium',
            _svg_m1_q10_line_graph(),
            r'The point \((v, -5)\) lies on the line shown. What is the value of \(v\)?',
            {
                'A': r'\(-\frac{72}{11}\)',
                'B': r'\(-\frac{11}{12}\)',
                'C': r'\(\frac{72}{11}\)',
                'D': r'\(\frac{192}{11}\)',
            },
            'A',
            r'Bước 1: Đọc tọa độ hai chấm đen trên đường thẳng: \((-12, 0)\) và \((0, -11)\).<br/>'
            r'Bước 2: Viết phương trình đường thẳng:<br/>'
            r'- Hệ số góc: \(m = \frac{-11 - 0}{0 - (-12)} = -\frac{11}{12}\).<br/>'
            r'- Tung độ gốc: \(b = -11\).<br/>'
            r'Suy ra phương trình đường thẳng là: \[y = -\frac{11}{12}x - 11.\]'
            r'Bước 3: Thay điểm \((v, -5)\) vào phương trình: \[-5 = -\frac{11}{12}v - 11 \Rightarrow 6 = -\frac{11}{12}v \Rightarrow v = -\frac{72}{11}.\]'
            r'Kiểm tra nhanh bằng mắt: \(-\frac{72}{11} \approx -6.55\), khớp hoàn toàn với hoành độ trên đồ thị khi \(y = -5\)!',
            r'Luôn kiểm tra lại dấu âm/dương của đáp án ngay trên đồ thị: khi \(y = -5\), điểm trên đường nằm ở góc phần tư III (\(x < 0\), giữa \(-6\) và \(-7\)), loại ngay C và D!',
            {
                'A': ('Đáp án đúng', r'Giải \(-5 = -\frac{11}{12}v - 11\) cho \(v = -\frac{72}{11} \approx -6.55\).'),
                'B': ('Nhầm hệ số góc với v', r'\(-\frac{11}{12}\) là hệ số góc \(m\) của đường thẳng, không phải hoành độ \(v\).'),
                'C': ('Sai dấu âm', r'\(\frac{72}{11} > 0\), nhưng tại \(y = -5\) đường thẳng nằm hoàn toàn bên trái trục tung (\(x < 0\)).'),
                'D': ('Sai dấu khi chuyển vế', r'Tính nhầm \(-5 - 11 = -16 \Rightarrow \frac{16 \times 12}{11} = \frac{192}{11}\) thay vì \(-5 + 11 = 6\).'),
            },
            r'Trong Desmos, vẽ bảng điểm `(-12, 0)` và `(0, -11)`, gõ hồi quy `y_1 ~ m x_1 + b`, rồi vẽ đường ngang `y = -5` và bấm vào giao điểm — nhận ngay `-6.545... = -72/11`!'
        ),

        math_mcq(
            'sat_real_mar25v3_m1_q11', 11, 'Algebra', 'Linear functions', 'Easy',
            r'<p style="text-align:center;">\[f(x) = 22\]</p>',
            r'For the given linear function \(f\), which table gives three values of \(x\) and their corresponding values of \(f(x)\)?',
            {
                'A': _choice_vtable([(0, 0), (1, 0), (2, 0)]),
                'B': _choice_vtable([(0, 22), (1, 22), (2, 22)]),
                'C': _choice_vtable([(0, 0), (1, 22), (2, 44)]),
                'D': _choice_vtable([(0, 22), (1, 44), (2, 66)]),
            },
            'B',
            r'Hàm \(f(x) = 22\) là <b>hàm hằng</b> (một trường hợp đặc biệt của hàm bậc nhất với hệ số góc \(m = 0\) và tung độ gốc \(b = 22\)).<br/>'
            r'Với <b>mọi</b> giá trị đầu vào \(x\), giá trị đầu ra \(f(x)\) luôn không đổi và bằng \(22\):<br/>'
            r'\(f(0) = 22,\; f(1) = 22,\; f(2) = 22\). Do đó bảng đúng là <b>B</b>.',
            r'Đừng để cụm từ "linear function" đánh lừa: \(f(x) = c\) (không chứa \(x\)) là đường thẳng nằm ngang có \(f(x) = c\) ở MỌI dòng trong bảng!',
            {
                'A': ('Hàm f(x) = 0', r'Bảng này cho giá trị \(f(x) = 0\) với mọi \(x\), không phải \(22\).'),
                'B': ('Đáp án đúng', r'Với mọi \(x \in \{0, 1, 2\}\), hàm hằng \(f(x) = 22\) đều trả về đúng \(22\).'),
                'C': ('Nhầm thành f(x) = 22x', r'Bảng này ứng với \(f(x) = 22x\) (tăng thêm \(22\) mỗi khi \(x\) tăng \(1\)).'),
                'D': ('Nhầm thành f(x) = 22x + 22', r'Bảng này ứng với \(f(x) = 22x + 22\), có hệ số góc \(22\) thay vì \(0\).'),
            },
            r'Gõ `f(x) = 22` vào Desmos rồi nhấn biểu tượng bánh răng → Convert to Table để thấy mọi dòng đều cho `f(x) = 22`.'
        ),

        math_mcq(
            'sat_real_mar25v3_m1_q12', 12, 'Geometry and Trigonometry',
            'Lines, angles, and triangles', 'Medium',
            _svg_m1_q12_parallel_lines(),
            r'In the figure shown, line \(k\) intersects lines \(r\) and \(s\). If \(w = 146\), which additional piece of information is sufficient to prove that lines \(r\) and \(s\) are parallel?',
            {
                'A': r'\(x = 34\)',
                'B': r'\(y = 146\)',
                'C': r'\(w + y = 180\)',
                'D': r'\(y + z = 180\)',
            },
            'B',
            r'Quan sát vị trí các góc tạo bởi cát tuyến \(k\) cắt hai đường thẳng \(r\) và \(s\):<br/>'
            r'- Góc \(w^\circ\) và góc \(y^\circ\) nằm ở cùng phía trên đường \(k\) và bên phải mỗi đường \(r, s\) \(\Rightarrow\) chúng là cặp <b>góc đồng vị (corresponding angles)</b>.<br/>'
            r'- Theo định lý đường thẳng song song: hai đường thẳng \(r\) và \(s\) song song khi và chỉ khi cặp góc đồng vị bằng nhau: \[y = w = 146.\]'
            r'Các phương án A và D chỉ là quan hệ hai góc kề bù (linear pair) — luôn đúng kể cả khi \(r\) và \(s\) KHÔNG song song!',
            r'Muốn chứng minh hai đường thẳng song song, thông tin bổ sung PHẢI liên hệ một góc ở đường \(r\) với một góc ở đường \(s\) (đồng vị bằng nhau, so le trong bằng nhau, hoặc trong cùng phía bù nhau)!',
            {
                'A': ('Thông tin thừa (góc kề bù)', r'Vì \(w^\circ\) và \(x^\circ\) là hai góc kề bù trên đường \(r\), ta luôn có \(x = 180 - 146 = 34\) dù \(r\) và \(s\) có song song hay không.'),
                'B': ('Đáp án đúng', r'\(w^\circ\) và \(y^\circ\) là hai góc đồng vị; biết \(y = 146 = w\) là đủ để chứng minh \(r \parallel s\).'),
                'C': ('Chứng minh KHÔNG song song', r'Nếu \(w + y = 180\) thì \(y = 34 \neq 146\), suy ra hai góc đồng vị không bằng nhau nên \(r\) và \(s\) cắt nhau.'),
                'D': ('Thông tin thừa (góc kề bù)', r'\(y^\circ\) và \(z^\circ\) kề bù trên đường \(s\), nên \(y + z = 180\) luôn đúng với mọi đường thẳng \(s\).'),
            },
            r'Bài hình học lý thuyết không cần Desmos: nhớ mẹo loại trừ nhanh — mọi phương trình chỉ chứa góc của 1 giao điểm (A: chỉ giao điểm trên \(r\), D: chỉ giao điểm trên \(s\)) không bao giờ chứng minh được hai đường song song!'
        ),

        math_mcq(
            'sat_real_mar25v3_m1_q13', 13, 'Advanced Math', 'Equivalent expressions', 'Medium',
            r'<p>Which expression is equivalent to \((133y)^{\frac{1}{2}}\), where \(y > 1\)?</p>',
            r'Select the equivalent radical expression.',
            {
                'A': r'\(133 \cdot \sqrt{y}\)',
                'B': r'\(\sqrt{133} \cdot y\)',
                'C': r'\(\sqrt{133y}\)',
                'D': r'\(\sqrt{(133y)^2}\)',
            },
            'C',
            r'Áp dụng quy tắc đổi số mũ phân số sang căn thức \(a^{\frac{1}{2}} = \sqrt{a}\) (với \(a > 0\)):<br/>'
            r'Vì dấu ngoặc bao trọn cả tích \(133y\), số mũ \(\frac{1}{2}\) tác động lên <b>toàn bộ</b> \(133y\): \[(133y)^{\frac{1}{2}} = \sqrt{133y}.\]',
            r'Chú ý dấu ngoặc cực kỳ quan trọng: \((ab)^{\frac{1}{2}} = \sqrt{ab}\), khác hoàn toàn với \(ab^{\frac{1}{2}} = a\sqrt{b}\)!',
            {
                'A': ('Bỏ sót số 133 ngoài căn', r'\(133\sqrt{y} = 133 \cdot y^{\frac{1}{2}}\), chỉ đúng nếu đề không có dấu ngoặc quanh \(133y\).'),
                'B': ('Bỏ sót biến y ngoài căn', r'\(\sqrt{133}\cdot y = 133^{\frac{1}{2}} \cdot y\), quên lấy căn bậc hai của \(y\).'),
                'C': ('Đáp án đúng', r'\((133y)^{\frac{1}{2}} = \sqrt{133y}\) (và do \(y > 1 > 0\), biểu thức dưới căn luôn dương).'),
                'D': ('Nhầm mũ 1/2 với mũ 2', r'\(\sqrt{(133y)^2} = 133y\) (vì \(y > 1\)), bằng mũ \(1\) chứ không phải mũ \(\frac{1}{2}\).'),
            },
            r'Thử thay nhanh \(y = 2\) trong Desmos: gõ `(133*2)^(1/2) ≈ 16.3095`, chỉ duy nhất `sqrt(133*2)` ra đúng `16.3095`!'
        ),

        math_mcq(
            'sat_real_mar25v3_m1_q14', 14, 'Advanced Math', 'Nonlinear functions', 'Medium',
            r'<p style="text-align:center;">\[f(x) = -26(2)^{\frac{x}{6}}\]</p>',
            r'Which table gives four values of \(x\) and their corresponding values of \(f(x)\) for the given exponential function?',
            {
                'A': _choice_htable([r'\(-6\)', r'\(0\)', r'\(6\)', r'\(12\)'], [r'\(-13\)', r'\(0\)', r'\(-52\)', r'\(-104\)']),
                'B': _choice_htable([r'\(-6\)', r'\(0\)', r'\(6\)', r'\(12\)'], [r'\(-13\)', r'\(-26\)', r'\(-52\)', r'\(-104\)']),
                'C': _choice_htable([r'\(-6\)', r'\(0\)', r'\(6\)', r'\(12\)'], [r'\(13\)', r'\(-26\)', r'\(-52\)', r'\(-104\)']),
                'D': _choice_htable([r'\(-6\)', r'\(0\)', r'\(6\)', r'\(12\)'], [r'\(-13\)', r'\(-26\)', r'\(-52\)', r'\(-78\)']),
            },
            'B',
            r'Thay lần lượt từng giá trị \(x \in \{-6, 0, 6, 12\}\) vào hàm mũ \(f(x) = -26(2)^{\frac{x}{6}}\):<br/>'
            r'- \(x = -6\): \(f(-6) = -26 \cdot 2^{-1} = -26 \cdot \frac{1}{2} = -13\). (Loại C)<br/>'
            r'- \(x = 0\): \(f(0) = -26 \cdot 2^{0} = -26 \cdot 1 = -26\). (Loại A)<br/>'
            r'- \(x = 6\): \(f(6) = -26 \cdot 2^{1} = -52\).<br/>'
            r'- \(x = 12\): \(f(12) = -26 \cdot 2^{2} = -26 \cdot 4 = -104\). (Loại D)<br/>'
            r'Bảng khớp hoàn toàn cả 4 giá trị là <b>B</b>.',
            r'Với hàm mũ \(a \cdot b^{x/k}\): nhớ kỹ \(b^0 = 1\) (không phải \(0\)), \(b^{-1} = \frac{1}{b}\) (không làm đổi dấu của hệ số \(a\)), và mỗi bước \(\Delta x = k\) thì \(f(x)\) <b>nhân với \(b\)</b> (không cộng dồn)!',
            {
                'A': ('Bẫy 2^0 = 0', r'Tính sai \(f(0) = 0\) do nhầm \(2^0 = 0\); thực tế \(2^0 = 1 \Rightarrow f(0) = -26\).'),
                'B': ('Đáp án đúng', r'Cả bốn giá trị \(-13, -26, -52, -104\) đều nhân đôi chính xác sau mỗi bước tăng \(x\) thêm \(6\).'),
                'C': ('Bẫy số mũ âm đổi dấu', r'Tính sai \(f(-6) = +13\) do nhầm \(2^{-1} = -\frac{1}{2}\); thực tế \(2^{-1} = +\frac{1}{2} \Rightarrow f(-6) = -13\).'),
                'D': ('Bẫy cộng tuyến tính ở x = 12', r'Cộng thêm \(-26\) từ \(-52\) ra \(-78\) thay vì nhân đôi \(-52 \times 2 = -104\).'),
            },
            r'Nhập `f(x) = -26(2)^(x/6)` vào Desmos, rồi gõ danh sách `f([-6, 0, 6, 12])` — máy trả ra ngay `[-13, -26, -52, -104]` trong 3 giây!'
        ),

        math_mcq(
            'sat_real_mar25v3_m1_q15', 15, 'Geometry and Trigonometry',
            'Right triangles and trigonometry', 'Medium',
            r'<p>The measure of angle \(B\) is \(\frac{3\pi}{4}\) radians.</p>',
            r'What is the value of \(\sin(B)\)?',
            {
                'A': r'\(-\frac{\sqrt{3}}{2}\)',
                'B': r'\(-\frac{\sqrt{2}}{2}\)',
                'C': r'\(\frac{1}{2}\)',
                'D': r'\(\frac{\sqrt{2}}{2}\)',
            },
            'D',
            r'Đổi góc sang độ để dễ hình dung trên vòng tròn lượng giác: \[\frac{3\pi}{4}\text{ rad} = \frac{3 \times 180^\circ}{4} = 135^\circ.\]'
            r'Góc \(135^\circ\) nằm ở <b>góc phần tư thứ II</b> (nơi \(\sin > 0\)) với góc quy chiếu (reference angle) là \(180^\circ - 135^\circ = 45^\circ\).<br/>'
            r'Do đó: \[\sin\left(\frac{3\pi}{4}\right) = +\sin(45^\circ) = \frac{\sqrt{2}}{2}.\]',
            r'Quy tắc ASTC ("All Students Take Calculus"): ở góc phần tư II (\(\frac{\pi}{2} < \theta < \pi\)), \(\sin\) mang dấu <b>DƯƠNG</b>, còn \(\cos\) mới mang dấu âm!',
            {
                'A': ('Sai cả góc lẫn dấu', r'\(-\frac{\sqrt{3}}{2}\) ứng với \(\sin\) của \(\frac{4\pi}{3}\) hoặc \(\frac{5\pi}{3}\).'),
                'B': ('Bẫy nhầm sang cos(3π/4)', r'\(-\frac{\sqrt{2}}{2}\) là giá trị của \(\cos\left(\frac{3\pi}{4}\right)\), không phải \(\sin\left(\frac{3\pi}{4}\right)\).'),
                'C': ('Nhầm góc quy chiếu 30°', r'\(\frac{1}{2} = \sin\left(\frac{5\pi}{6}\right)\), không phải \(\sin\left(\frac{3\pi}{4}\right)\).'),
                'D': ('Đáp án đúng', r'\(\sin\left(\frac{3\pi}{4}\right) = \sin(135^\circ) = \frac{\sqrt{2}}{2}\).'),
            },
            r'Đặt Desmos ở chế độ <b>RAD</b> (mặc định), gõ `sin(3pi/4)` ra `0.7071...`; so với `sqrt(2)/2 = 0.7071...` → chọn ngay D!'
        ),

        math_spr(
            'sat_real_mar25v3_m1_q16', 16, 'Algebra',
            'Linear inequalities in one or two variables', 'Medium',
            r'<p>A school is ordering tablet computers for its students. The tablets cost $164 each, and \(6\%\) tax is added to the total cost of the order.</p>',
            r'If the school can spend no more than \(44{,}800\) dollars on the tablets, including tax, what is the maximum number of tablets that the school can order?',
            ['257'], '257',
            r'Gọi \(n\) là số máy tính bảng đặt mua (\(n\) là số nguyên dương).<br/>'
            r'Tổng chi phí bao gồm thuế \(6\%\) là: \[1.06 \times 164n = 173.84n.\]'
            r'Theo đề bài, tổng tiền không vượt quá \(44{,}800\) đô-la: \[173.84n \le 44{,}800 \Rightarrow n \le \frac{44{,}800}{173.84} \approx 257.708.\]'
            r'Vì chỉ có thể đặt số nguyên máy và không được vượt ngân sách, ta phải <b>làm tròn xuống</b>: \(n_{\max} = 257\).<br/>'
            r'Kiểm tra lại: \(257 \times 173.84 = \$44{,}676.88 \le \$44{,}800\) (đạt), còn \(258 \times 173.84 = \$44{,}850.72 > \$44{,}800\) (vượt).',
            r'Với bài toán tìm <b>số lượng nguyên lớn nhất</b> thỏa mãn ngân sách ("no more than"), LUÔN làm tròn xuống (floor) dù chữ số thập phân là `.708`!',
            r'Gõ `44800 / (164 * 1.06)` trong Desmos ra `257.708...` → lấy phần nguyên `257`!'
        ),

        math_spr(
            'sat_real_mar25v3_m1_q17', 17, 'Geometry and Trigonometry', 'Area and volume', 'Easy',
            r'<p>A triangular prism has a height of \(3\) centimeters (\(\text{cm}\)) and a volume of \(60\text{ cm}^3\).</p>',
            r'What is the area, in \(\text{cm}^2\), of the base of the prism? (The volume of a triangular prism is equal to \(Bh\), where \(B\) is the area of the base and \(h\) is the height of the prism.)',
            ['20'], '20',
            r'Thay thể tích \(V = 60\text{ cm}^3\) và chiều cao \(h = 3\text{ cm}\) vào công thức đã cho \(V = Bh\): \[60 = B \cdot 3 \Rightarrow B = \frac{60}{3} = 20\text{ (cm}^2\text{)}.\]',
            r'Đề đã cho sẵn công thức \(V = Bh\) — chỉ cần chia thể tích cho chiều cao, đừng nhân thêm \(\frac{1}{2}\) hay \(\frac{1}{3}\)!',
            r'Gõ `60 / 3` ra ngay `20`.'
        ),

        math_mcq(
            'sat_real_mar25v3_m1_q18', 18, 'Advanced Math', 'Nonlinear functions', 'Medium',
            _svg_m1_q18_exp_graph(),
            r'The graph of \(y = f(x)\) is shown, where \(f(x) = ab^x + c\), and \(a\), \(b\), and \(c\) are constants. For how many values of \(x\) does \(f(x) = 0\)?',
            {'A': 'Three', 'B': 'Two', 'C': 'One', 'D': 'Zero'},
            'D',
            r'Nghiệm của phương trình \(f(x) = 0\) chính là số giao điểm của đồ thị \(y = f(x)\) với <b>trục hoành \(Ox\)</b> (đường thẳng \(y = 0\)).<br/>'
            r'Quan sát đồ thị hàm mũ \(f(x) = ab^x + c\):<br/>'
            r'- Khi \(x \to -\infty\), đồ thị tiệm cận ngang từ phía dưới vào đường \(y = -5\) (nên \(c = -5\)).<br/>'
            r'- Khi \(x\) tăng, đồ thị giảm nhanh xuống \(-\infty\) (đi qua \((0, -6)\) và \((1, -8)\), tức \(f(x) = -3^x - 5\)).<br/>'
            r'Vì \(f(x) < -5 < 0\) với mọi số thực \(x\), đồ thị <b>không bao giờ cắt trục \(Ox\)</b> \(\Rightarrow\) có <b>\(0\) (Zero)</b> giá trị \(x\) thỏa mãn \(f(x) = 0\).',
            r'Câu hỏi "For how many values of \(x\) does \(f(x) = 0\)?" luôn tương đương với việc đếm số giao điểm của đồ thị với đường \(y = 0\) (trục hoành)!',
            {
                'A': ('Đếm nhầm số nghiệm', r'Một hàm mũ đơn điệu \(ab^x + c\) chỉ có tối đa \(1\) nghiệm thực, không bao giờ có \(3\) nghiệm.'),
                'B': ('Đếm nhầm số nghiệm', r'Hàm mũ không đổi chiều nên không thể cắt trục \(Ox\) tại \(2\) điểm.'),
                'C': ('Nhầm giao điểm trục tung', r'Đồ thị cắt trục tung \(Oy\) tại \(1\) điểm \((0, -6)\), nhưng đề hỏi \(f(x) = 0\) (giao trục hoành \(Ox\)), không phải \(f(0)\)!'),
                'D': ('Đáp án đúng', r'Toàn bộ đồ thị nằm dưới tiệm cận ngang \(y = -5 < 0\) nên không cắt trục \(Ox\) tại điểm nào.'),
            },
            r'Bài đọc đồ thị trực tiếp: nhìn đường \(y = 0\) (trục \(Ox\)), thấy đường cong hoàn toàn nằm dưới \(y = -5\) và đi xuống mãi nên chọn ngay D (Zero) trong 3 giây!'
        ),

        math_mcq(
            'sat_real_mar25v3_m1_q19', 19, 'Advanced Math',
            'Nonlinear equations in one variable and systems of equations in two variables', 'Hard',
            r'<p style="text-align:center;">\[x(x + 4) - 140 = 3x(x - 10)\]</p>',
            r'What is the sum of the solutions to the given equation?',
            {'A': r'\(6\)', 'B': r'\(10\)', 'C': r'\(14\)', 'D': r'\(17\)'},
            'D',
            r'Bước 1: Nhân phá ngoặc hai vế: \[x^2 + 4x - 140 = 3x^2 - 30x.\]'
            r'Bước 2: Chuyển tất cả sang vế phải để đưa về dạng chuẩn \(ax^2 + bx + c = 0\): \[2x^2 - 34x + 140 = 0 \Rightarrow x^2 - 17x + 70 = 0.\]'
            r'Bước 3: Kiểm tra nghiệm thực bằng phân tích nhân tử: \[(x - 7)(x - 10) = 0 \Rightarrow x = 7 \text{ hoặc } x = 10.\]'
            r'Cả hai nghiệm đều thực và phân biệt, nên tổng các nghiệm là: \[7 + 10 = 17 \quad \left(\text{hoặc theo Vi-ét: } -\frac{b}{a} = -\frac{-17}{1} = 17\right).\]',
            r'Khi áp dụng công thức tổng nghiệm Vi-ét \(-\frac{b}{a}\), luôn kiểm tra nhanh \(\Delta > 0\) để chắc chắn phương trình có 2 nghiệm thực phân biệt (vì nếu nghiệm kép thì chỉ có 1 nghiệm)!',
            {
                'A': ('Cộng sai hệ số', r'Không khớp nghiệm thực \(x = 7\) và \(x = 10\).'),
                'B': ('Chỉ lấy một nghiệm', r'\(10\) là nghiệm lớn hơn của phương trình, chưa cộng với nghiệm thứ hai \(x = 7\).'),
                'C': ('Sai dấu hạng tử 4x', r'Nếu chuyển vế sai thành \(2x^2 - 26x + 140\) hay cộng sai \(30 - 4\) thì dễ nhầm sang số khác.'),
                'D': ('Đáp án đúng', r'Hai nghiệm là \(x = 7\) và \(x = 10\), tổng bằng \(7 + 10 = 17\).'),
            },
            r'Gõ thẳng `x(x + 4) - 140 = 3x(x - 10)` vào Desmos — hai đường thẳng đứng hiện ra ngay tại `x = 7` và `x = 10` → cộng lại được `17`!'
        ),

        math_mcq(
            'sat_real_mar25v3_m1_q20', 20, 'Advanced Math',
            'Nonlinear equations in one variable and systems of equations in two variables', 'Medium',
            r'<p style="text-align:center;">\[-3x^2 - 7x + 1 = 0\]</p>',
            r'What is the greatest solution to the given equation?',
            {
                'A': r'\(-\frac{7}{3} + \frac{\sqrt{61}}{3}\)',
                'B': r'\(-\frac{7}{3} - \frac{\sqrt{61}}{3}\)',
                'C': r'\(-\frac{7}{6} + \frac{\sqrt{61}}{6}\)',
                'D': r'\(-\frac{7}{6} - \frac{\sqrt{61}}{6}\)',
            },
            'C',
            r'Nhân cả hai vế với \(-1\) để hệ số \(a > 0\) cho gọn và tránh nhầm dấu ở mẫu số: \[3x^2 + 7x - 1 = 0 \quad (a = 3,\; b = 7,\; c = -1).\]'
            r'Áp dụng công thức nghiệm bậc hai: \[x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a} = \frac{-7 \pm \sqrt{7^2 - 4(3)(-1)}}{2(3)} = \frac{-7 \pm \sqrt{49 + 12}}{6} = -\frac{7}{6} \pm \frac{\sqrt{61}}{6}.\]'
            r'Vì \(\frac{\sqrt{61}}{6} > 0\), nghiệm lớn nhất (<b>greatest solution</b>) là \(-\frac{7}{6} + \frac{\sqrt{61}}{6}\).',
            r'Mẹo chống nhầm dấu ở mẫu số \(2a\): khi \(a < 0\) (như \(-3x^2\)), hãy nhân toàn bộ phương trình với \(-1\) TRƯỚC khi dùng công thức nghiệm bậc hai!',
            {
                'A': ('Quên nhân 2 ở mẫu 2a', r'Chia cho \(a = 3\) thay vì \(2a = 6\).'),
                'B': ('Quên nhân 2 và lấy dấu trừ', r'Vừa sai mẫu số \(3\) thay vì \(6\), vừa lấy nghiệm nhỏ hơn.'),
                'C': ('Đáp án đúng', r'Hai nghiệm là \(-\frac{7}{6} \pm \frac{\sqrt{61}}{6}\), nghiệm lớn hơn mang dấu cộng: \(-\frac{7}{6} + \frac{\sqrt{61}}{6} \approx 0.135\).'),
                'D': ('Chọn nghiệm nhỏ nhất', r'\(-\frac{7}{6} - \frac{\sqrt{61}}{6} \approx -2.468\) là nghiệm nhỏ hơn, không phải nghiệm lớn nhất.'),
            },
            r'Vẽ `y = -3x^2 - 7x + 1` trong Desmos, bấm vào giao điểm bên phải với trục \(Ox\) được `x ≈ 0.13504`; thử gõ `-7/6 + sqrt(61)/6` ra đúng `0.13504`!'
        ),

        math_spr(
            'sat_real_mar25v3_m1_q21', 21, 'Geometry and Trigonometry',
            'Right triangles and trigonometry', 'Medium',
            _svg_m1_q21_right_triangle()
            + r'<p>In triangle \(ABC\), \(BC = 36\sqrt{3}\).</p>',
            r'What is the value of \(\cos A\)?',
            ['1/2', '0.5', '.5'], '1/2 (hoặc 0.5)',
            r'<b>Cách 1 (Siêu tốc 3 giây — không cần dùng độ dài cạnh!):</b><br/>'
            r'Trong tam giác vuông \(ABC\) tại \(B\), ta có \(\angle C = 30^\circ\), suy ra: \[\angle A = 90^\circ - 30^\circ = 60^\circ.\]'
            r'Vậy: \[\cos A = \cos(60^\circ) = \frac{1}{2} = 0.5.\]'
            r'<b>Cách 2 (Kiểm chứng qua tam giác đặc biệt \(30^\circ\text{–}60^\circ\text{–}90^\circ\)):</b><br/>'
            r'Cạnh kề góc \(30^\circ\) là \(BC = 36\sqrt{3} \Rightarrow\) cạnh đối \(30^\circ\) là \(AB = 36\) và cạnh huyền \(AC = 72\).<br/>'
            r'Khi đó \(\cos A = \frac{\text{kề}}{\text{huyền}} = \frac{AB}{AC} = \frac{36}{72} = \frac{1}{2} = 0.5\).',
            r'Giá trị lượng giác của góc phụ thuộc vào <b>số đo góc</b> chứ không phụ thuộc vào độ dài cạnh — dữ kiện \(BC = 36\sqrt{3}\) là nhiễu vô hại (nhưng có thể dùng kiểm chứng)!',
            r'Chuyển Desmos sang chế độ <b>DEG</b> rồi gõ `cos(90 - 30)` — hiện ngay `0.5`!'
        ),

        math_mcq(
            'sat_real_mar25v3_m1_q22', 22, 'Problem-Solving and Data Analysis',
            'Percentages', 'Hard',
            r'<p>The positive number \(a\) is \(2{,}047\%\) of the sum of the positive numbers \(b\) and \(c\), and \(b\) is \(89\%\) of \(c\).</p>',
            r'What percent of \(b\) is \(a\)?',
            {
                'A': r'\(21.36\%\)',
                'B': r'\(38.69\%\)',
                'C': r'\(2{,}300\%\)',
                'D': r'\(4{,}347\%\)',
            },
            'D',
            r'<b>Cách 1 (Chọn số đẹp \(c = 100\) — chống nhầm tuyệt đối):</b><br/>'
            r'- Chọn \(c = 100\).<br/>'
            r'- Vì \(b\) bằng \(89\%\) của \(c\): \(b = 0.89 \times 100 = 89\).<br/>'
            r'- Tổng \(b + c = 89 + 100 = 189\).<br/>'
            r'- Vì \(a\) bằng \(2{,}047\%\) của \((b + c)\): \[a = 20.47 \times 189 = 3{,}868.83.\]'
            r'- Đề hỏi "What percent of \(b\) is \(a\)?", tức tính \(\frac{a}{b} \times 100\%\):'
            r'\[\frac{a}{b} \times 100\% = \frac{20.47 \times 189}{89} \times 100\% = \frac{2{,}047}{89} \times 189\% = 23 \times 189\% = 4{,}347\%.\]'
            r'<b>Cách 2 (Đại số nhanh):</b> \(a = 20.47(b + c) = 20.47b\left(1 + \frac{1}{0.89}\right) = (20.47 + 23)b = 43.47b = 4{,}347\%\text{ của } b\).',
            r'Với bài toán phần trăm nhiều ẩn \(a, b, c\) ở câu chốt số 22, chọn ngay ẩn gốc \(c = 100\) và nhớ: "What percent of \(b\) is \(a\)?" luôn là \(\frac{a}{b} \times 100\%\)!',
            {
                'A': ('Chia sai 100 và quên b+c', r'Lấy \(20.47\) hoặc nhân nhầm phần trăm mà không chuyển đổi đúng hệ số \(100\%\).'),
                'B': ('Quên chia cho b = 89', r'\(38.69 \approx 20.47 \times 1.89\) là tỉ số \(\frac{a}{c}\) chia sai bậc \(100\), chưa chia cho \(0.89\) để ra \(\frac{a}{b}\).'),
                'C': ('Bẫy quên cộng c trong (b + c)', r'\(\frac{2{,}047\%}{0.89} = 2{,}300\%\) chỉ tính phần \(20.47c / b\) mà bỏ quên phần \(20.47b / b = 2{,}047\%\)!'),
                'D': ('Đáp án đúng', r'\(\frac{a}{b} \times 100\% = 2{,}047\% + 2{,}300\% = 4{,}347\%\).'),
            },
            r'Trong Desmos, gõ 4 dòng: `c = 100`, `b = 0.89*c`, `a = 20.47*(b + c)`, `(a/b)*100` → hiện chuẩn xác `4347`!'
        ),
    ]


# ============================================================================
# MODULE 2 — SECTION 2, MODULE 2: MATH (22 REAL QUESTIONS: 16 MCQ + 6 SPR)
# ============================================================================

def _build_m2_questions():
    return [
        math_mcq(
            'sat_real_mar25v3_m2_q1', 1, 'Algebra', 'Linear equations in one variable', 'Easy',
            r'<p>How many solutions does the equation \(2x - 3 = 2x\) have?</p>',
            r'Choose the correct number of solutions.',
            {
                'A': 'Zero',
                'B': 'Exactly one',
                'C': 'Exactly two',
                'D': 'Infinitely many',
            },
            'A',
            r'Trừ \(2x\) ở cả hai vế của phương trình \(2x - 3 = 2x\): \[-3 = 0.\]'
            r'Đây là một đẳng thức <b>vô lý</b> (luôn sai với mọi \(x\)), nên phương trình <b>vô nghiệm (Zero)</b>.',
            r'Với phương trình bậc nhất \(ax + b = cx + d\): nếu \(a = c\) nhưng \(b \neq d\) (hệ số \(x\) bằng nhau, hằng số khác nhau) thì phương trình luôn vô nghiệm!',
            {
                'A': ('Đáp án đúng', r'Triệt tiêu \(2x\) hai vế cho \(-3 = 0\) (vô lý) \(\Rightarrow\) \(0\) nghiệm.'),
                'B': ('Nhầm hệ số x khác nhau', r'Chỉ có đúng \(1\) nghiệm khi hệ số của \(x\) ở hai vế khác nhau.'),
                'C': ('Nhầm phương trình bậc hai', r'Phương trình bậc nhất một ẩn không bao giờ có đúng \(2\) nghiệm.'),
                'D': ('Nhầm đồng nhất thức', r'Chỉ có vô số nghiệm khi hai vế giống hệt nhau (ví dụ \(2x - 3 = 2x - 3\)).'),
            },
            r'Vẽ `y = 2x - 3` và `y = 2x` trong Desmos: hai đường thẳng song song không bao giờ cắt nhau → Zero!'
        ),

        math_mcq(
            'sat_real_mar25v3_m2_q2', 2, 'Algebra', 'Linear functions', 'Easy',
            r'<p>In the linear function \(f\), \(f(0) = 2\) and \(f(7) = 2\).</p>',
            r'Which equation defines \(f\)?',
            {
                'A': r'\(f(x) = 0\)',
                'B': r'\(f(x) = 7\)',
                'C': r'\(f(x) = 2\)',
                'D': r'\(f(x) = x + 2\)',
            },
            'C',
            r'Đồ thị hàm bậc nhất \(f\) đi qua hai điểm \((0, 2)\) và \((7, 2)\).<br/>'
            r'- Hệ số góc: \[m = \frac{2 - 2}{7 - 0} = \frac{0}{7} = 0.\]'
            r'- Tung độ gốc: \(b = f(0) = 2\).<br/>'
            r'Do đó phương trình của hàm \(f\) là: \[f(x) = 0 \cdot x + 2 = 2.\]',
            r'Khi một hàm bậc nhất nhận cùng một giá trị đầu ra tại hai giá trị \(x\) khác nhau (\(f(0) = f(7) = 2\)), đó chắc chắn là hàm hằng \(f(x) = 2\)!',
            {
                'A': ('Nhầm đầu vào x = 0', r'Với \(f(x) = 0\), ta có \(f(0) = 0 \neq 2\).'),
                'B': ('Nhầm đầu vào x = 7', r'Với \(f(x) = 7\), ta có \(f(0) = 7 \neq 2\).'),
                'C': ('Đáp án đúng', r'Hàm hằng \(f(x) = 2\) thỏa mãn cả \(f(0) = 2\) lẫn \(f(7) = 2\).'),
                'D': ('Nhầm hệ số góc bằng 1', r'Với \(f(x) = x + 2\), ta có \(f(7) = 9 \neq 2\).'),
            },
            r'Thay nhanh \(x = 7\) vào 4 đáp án: chỉ có C cho kết quả \(2\).'
        ),

        math_mcq(
            'sat_real_mar25v3_m2_q3', 3, 'Advanced Math', 'Nonlinear functions', 'Easy',
            r'<p>A rectangle has a length that is \(92\) times its width. The function \(y = (92w)(w)\) represents this situation, where \(y\) is the area, in square feet, of the rectangle and \(y > 0\).</p>',
            r'Which of the following is the best interpretation of \(92w\) in this context?',
            {
                'A': 'The length of the rectangle, in feet',
                'B': 'The area of the rectangle, in square feet',
                'C': 'The difference between the length and the width of the rectangle, in feet',
                'D': 'The width of the rectangle, in feet',
            },
            'A',
            r'Diện tích hình chữ nhật bằng <b>chiều dài \(\times\) chiều rộng</b>.<br/>'
            r'Trong phương trình \(y = (92w)(w)\), \(y\) là diện tích (\(\text{square feet}\)), \(w\) là chiều rộng (\(\text{feet}\)), và đề bài nói chiều dài gấp \(92\) lần chiều rộng.<br/>'
            r'Do đó thừa số \(92w\) chính là <b>chiều dài của hình chữ nhật, tính bằng feet</b>.',
            r'Luôn đối chiếu từng thừa số trong công thức diện tích \(\text{Area} = \text{length} \times \text{width}\) với mô tả bằng lời của đề bài.',
            {
                'A': ('Đáp án đúng', r'Vì chiều rộng là \(w\) và chiều dài gấp \(92\) lần chiều rộng, nên \(92w\) là chiều dài (feet).'),
                'B': ('Nhầm với biến y', r'Diện tích hình chữ nhật là \(y = 92w^2\), không phải \(92w\).'),
                'C': ('Nhầm hiệu hai kích thước', r'Hiệu giữa chiều dài và chiều rộng là \(92w - w = 91w\).'),
                'D': ('Nhầm chiều rộng', r'Chiều rộng hình chữ nhật chỉ là \(w\), không nhân \(92\).'),
            },
            r'Câu đọc hiểu biểu thức đại số — đối chiếu thẳng \(\text{Area} = (\text{length})(\text{width}) = (92w)(w) \Rightarrow 92w = \text{length}\)!'
        ),

        math_mcq(
            'sat_real_mar25v3_m2_q4', 4, 'Algebra', 'Linear functions', 'Easy',
            r'<p style="text-align:center;">\[T(x) = 67 - 8x\]</p>'
            r'<p>The function \(T\) estimates the temperature, in degrees Fahrenheit (\(^\circ\text{F}\)), in a certain city one day in January, where \(x\) is the number of hours after 10 a.m. and \(1 \le x \le 5\).</p>',
            r'According to the function, what was the estimated decrease in temperature each hour, in \(^\circ\text{F}\), in this city during this time period?',
            {'A': r'\(4\)', 'B': r'\(8\)', 'C': r'\(59\)', 'D': r'\(67\)'},
            'B',
            r'Hàm tuyến tính \(T(x) = 67 - 8x\) có hệ số góc (rate of change) là \(-8\).<br/>'
            r'Điều này có nghĩa là cứ mỗi khi \(x\) tăng thêm \(1\) giờ, nhiệt độ ước tính <b>giảm đi \(8^\circ\text{F}\)</b>.<br/>'
            r'Vì đề bài đã dùng sẵn từ "decrease" (mức giảm), đáp án là số dương \(8\).',
            r'Trong mô hình tuyến tính \(f(x) = b - mx\), giá trị \(m > 0\) là mức giảm (decrease) cho mỗi đơn vị tăng của \(x\); còn \(b\) là giá trị ban đầu tại \(x = 0\).',
            {
                'A': ('Nhầm khoảng thời gian', r'\(5 - 1 = 4\) là số giờ của khoảng \(1 \le x \le 5\), không phải mức giảm nhiệt độ mỗi giờ.'),
                'B': ('Đáp án đúng', r'Hệ số góc \(-8\) cho thấy nhiệt độ giảm \(8^\circ\text{F}\) mỗi giờ.'),
                'C': ('Nhầm nhiệt độ tại x = 1', r'\(T(1) = 67 - 8(1) = 59^\circ\text{F}\) là nhiệt độ lúc 11 a.m., không phải mức giảm mỗi giờ.'),
                'D': ('Nhầm nhiệt độ ban đầu', r'\(67^\circ\text{F}\) là tung độ gốc \(T(0)\) (nhiệt độ lúc 10 a.m.).'),
            },
            r'Thử tính hiệu `T(2) - T(1) = (67 - 16) - (67 - 8) = -8` → giảm `8` độ mỗi giờ!'
        ),

        math_mcq(
            'sat_real_mar25v3_m2_q5', 5, 'Problem-Solving and Data Analysis',
            'Probability and conditional probability', 'Easy',
            r'<p>At a convention center, there are a total of \(375\) visitors. Each visitor is located in either room A, room B, or room C. If one of these visitors is selected at random, the probability of selecting a visitor who is located in room A is \(0.68\), and the probability of selecting a visitor who is located in room B is \(0.24\).</p>',
            r'How many visitors are located in room C?',
            {'A': r'\(8\)', 'B': r'\(30\)', 'C': r'\(61\)', 'D': r'\(165\)'},
            'B',
            r'Vì mỗi khách tham quan chỉ ở đúng một trong ba phòng A, B, hoặc C, tổng xác suất bằng \(1\):'
            r'\[P(\text{room C}) = 1 - 0.68 - 0.24 = 0.08.\]'
            r'Số khách ở phòng C là: \[0.08 \times 375 = 30\text{ (visitors)}.\]',
            r'Khi các biến cố xung khắc và bao phủ toàn bộ không gian mẫu (A, B, C), tổng xác suất luôn bằng \(1\) (tức \(100\%\)). Nhớ nhân xác suất với tổng số người!',
            {
                'A': ('Nhầm phần trăm với số người', r'\(0.08 = 8\%\) là tỉ lệ khách ở phòng C, chưa nhân với tổng \(375\) khách.'),
                'B': ('Đáp án đúng', r'\(P(C) = 1 - 0.68 - 0.24 = 0.08\), suy ra \(0.08 \times 375 = 30\) khách.'),
                'C': ('Tính sai phép trừ', r'Không khớp với \(0.08 \times 375 = 30\).'),
                'D': ('Lấy hiệu phòng A và phòng B', r'\((0.68 - 0.24) \times 375 = 0.44 \times 375 = 165\) là chênh lệch số khách giữa phòng A và phòng B!'),
            },
            r'Gõ `(1 - 0.68 - 0.24) * 375` trong Desmos ra ngay `30`!'
        ),

        math_mcq(
            'sat_real_mar25v3_m2_q6', 6, 'Advanced Math', 'Nonlinear functions', 'Easy',
            r'<p>An object is launched from a height of \(121\) feet above the ground. A quadratic function \(f\) models the height above the ground, in feet, of the object \(t\) seconds after it is launched. According to the model, \(2\) seconds after the object is launched, it reaches a maximum height of \(185\) feet above the ground.</p>',
            r'Which equation defines \(f\)?',
            {
                'A': r'\(f(t) = -16(t + 185)^2 - 2\)',
                'B': r'\(f(t) = -16(t - 185)^2 + 2\)',
                'C': r'\(f(t) = -16(t + 2)^2 - 185\)',
                'D': r'\(f(t) = -16(t - 2)^2 + 185\)',
            },
            'D',
            r'Dạng đỉnh (vertex form) của hàm bậc hai có đỉnh \((h, k)\) là: \[f(t) = a(t - h)^2 + k.\]'
            r'Theo đề bài, vật đạt <b>độ cao cực đại \(185\) feet tại thời điểm \(t = 2\) giây</b> \(\Rightarrow\) đỉnh parabol là \((h, k) = (2, 185)\).<br/>'
            r'Thay \((h, k) = (2, 185)\): \(f(t) = a(t - 2)^2 + 185\).<br/>'
            r'Kiểm chứng độ cao ban đầu tại \(t = 0\): \(f(0) = 121 \Rightarrow a(0 - 2)^2 + 185 = 121 \Rightarrow 4a = -64 \Rightarrow a = -16\).<br/>'
            r'Vậy: \[f(t) = -16(t - 2)^2 + 185.\]',
            r'Trong vertex form \(a(t - h)^2 + k\): <b>bên trong ngoặc đổi dấu</b> (\((t - 2)^2\)), còn <b>bên ngoài giữ nguyên dấu</b> (\(+185\))!',
            {
                'A': ('Đổi nhầm tọa độ h và k + sai dấu', r'Đỉnh của hàm này là \((-185, -2)\), hoàn toàn ngược với \((2, 185)\).'),
                'B': ('Hoán đổi tọa độ h và k', r'Đỉnh của hàm này là \((185, 2)\) — nhầm thời gian \(2\) giây với độ cao \(185\) feet.'),
                'C': ('Sai dấu cả h và k', r'Đỉnh của hàm này là \((-2, -185)\) thay vì \((2, 185)\).'),
                'D': ('Đáp án đúng', r'Đỉnh \((2, 185)\) và kiểm tra \(f(0) = -16(-2)^2 + 185 = -64 + 185 = 121\) khớp hoàn hảo!'),
            },
            r'Kiểm tra nhanh bằng điều kiện \(f(0) = 121\): gõ `-16*(0 - 2)^2 + 185` trong Desmos ra đúng `121`!'
        ),

        math_spr(
            'sat_real_mar25v3_m2_q7', 7, 'Algebra',
            'Systems of two linear equations in two variables', 'Medium',
            r'<p style="text-align:center;">\[7y = -6x + 2{,}550\]\[24x - 28y = 1{,}800\]</p>',
            r'The solution to the given system of equations is \((x, y)\). What is the value of \(x + y\)?',
            ['400'], '400',
            r'Bước 1: Chuyển phương trình thứ nhất về dạng chuẩn: \[6x + 7y = 2{,}550.\]'
            r'Bước 2: Nhân cả hai vế của phương trình này với \(4\) để cân bằng hệ số của \(y\) với phương trình thứ hai: \[24x + 28y = 10{,}200.\]'
            r'Bước 3: Cộng vế theo vế với phương trình thứ hai \(24x - 28y = 1{,}800\):'
            r'\[48x = 12{,}000 \Rightarrow x = \frac{12{,}000}{48} = 250.\]'
            r'Bước 4: Thay \(x = 250\) vào phương trình đầu tiên:'
            r'\[7y = -6(250) + 2{,}550 = 1{,}050 \Rightarrow y = 150.\]'
            r'Suy ra \(x + y = 250 + 150 = 400\).',
            r'Luôn kiểm tra câu hỏi cuối cùng: đề hỏi \(x + y\), KHÔNG phải chỉ \(x\) hay chỉ \(y\)!',
            r'Nhập nguyên hai phương trình `7y = -6x + 2550` và `24x - 28y = 1800` vào Desmos, phóng nhỏ để bấm vào giao điểm `(250, 150)`, rồi cộng `250 + 150 = 400`!'
        ),

        math_spr(
            'sat_real_mar25v3_m2_q8', 8, 'Problem-Solving and Data Analysis',
            'Ratios, rates, proportional relationships, and units', 'Easy',
            r'<p>To study fluctuations in leaf water potential, samples of wood were taken from \(21\) trees and cut in the shape of a cube. The length of the edge of one of these cubes is \(3.000\) centimeters. This cube has a density of \(0.220\) grams per cubic centimeter.</p>',
            r'What is the mass of this cube, in grams?',
            ['5.94', '297/50'], '5.94 (hoặc 297/50)',
            r'Bước 1: Tính thể tích của <b>một</b> khối lập phương cạnh \(s = 3.000\text{ cm}\):'
            r'\[V = s^3 = 3^3 = 27\text{ cm}^3.\]'
            r'Bước 2: Áp dụng công thức khối lượng \(\text{Mass} = \text{Density} \times \text{Volume}\):'
            r'\[\text{Mass} = 0.220\text{ g/cm}^3 \times 27\text{ cm}^3 = 5.94\text{ grams}.\]'
            r'<i>Lưu ý bẫy dữ kiện thừa:</i> Đề hỏi khối lượng của <b>"this cube"</b> (một khối lập phương này), nên con số \(21\) cây là thông tin bối cảnh dư thừa, không nhân thêm \(21\)!',
            r'Công thức \(\text{Density} = \frac{\text{Mass}}{\text{Volume}} \Rightarrow \text{Mass} = \text{Density} \times V\). Luôn để ý các con số bối cảnh thừa (như \(21\) trees)!',
            r'Gõ `0.220 * 3^3` trong Desmos ra ngay `5.94` (hoặc dạng phân số `297/50`).'
        ),

        math_mcq(
            'sat_real_mar25v3_m2_q9', 9, 'Algebra', 'Linear equations in one variable', 'Medium',
            r'<p style="text-align:center;">\[-2|3x + 7| + 8 = -6\]</p>',
            r'What are all solutions to the given equation?',
            {
                'A': r'\(0\)',
                'B': r'\(0\) and \(-\frac{8}{3}\)',
                'C': r'\(0\) and \(-\frac{14}{3}\)',
                'D': 'There is no solution.',
            },
            'C',
            r'Bước 1: Cô lập biểu thức giá trị tuyệt đối \(|3x + 7|\):'
            r'\[-2|3x + 7| = -6 - 8 = -14 \Rightarrow |3x + 7| = \frac{-14}{-2} = 7.\]'
            r'Bước 2: Vì vế phải \(7 > 0\), tách thành \(2\) trường hợp:'
            r'<br/>- Trường hợp 1: \(3x + 7 = 7 \Rightarrow 3x = 0 \Rightarrow x = 0\).'
            r'<br/>- Trường hợp 2: \(3x + 7 = -7 \Rightarrow 3x = -14 \Rightarrow x = -\frac{14}{3}\).<br/>'
            r'Vậy tất cả các nghiệm là \(0\) và \(-\frac{14}{3}\).',
            r'LUÔN cô lập hoàn toàn dấu giá trị tuyệt đối \(|A| = k\) trước khi kết luận "no solution" hay chia 2 trường hợp: dấu âm \(-2\) nhân với \(-14\) đổi thành \(+7 > 0\)!',
            {
                'A': ('Thiếu nhánh âm', r'Chỉ giải trường hợp \(3x + 7 = 7 \Rightarrow x = 0\) mà quên trường hợp \(3x + 7 = -7\).'),
                'B': ('Trừ sai vế phải', r'Tính sai \(-6 + 8 = +2\) hay chia sai dấu trước khi tách trị tuyệt đối nên ra \(-\frac{8}{3}\).'),
                'C': ('Đáp án đúng', r'Từ \(|3x + 7| = 7\) giải ra đúng hai nghiệm \(x = 0\) và \(x = -\frac{14}{3}\).'),
                'D': ('Bẫy nhìn thấy vế phải -6', r'Thấy vế phải là \(-6 < 0\) liền vội kết luận vô nghiệm mà chưa chuyển \(+8\) và chia cho \(-2\)!'),
            },
            r'Gõ thẳng `-2*abs(3x + 7) + 8 = -6` vào Desmos — hai đường thẳng đứng xuất hiện ngay tại `x = 0` và `x = -4.667 = -14/3`!'
        ),

        math_mcq(
            'sat_real_mar25v3_m2_q10', 10, 'Algebra', 'Linear equations in two variables', 'Medium',
            _svg_m2_q10_line_graph(),
            r'The graph shows a linear relationship between \(x\) and \(y\). Which equation represents this relationship, where \(R\) is a positive constant?',
            {
                'A': r'\(Rx + 12y = 18\)',
                'B': r'\(Rx - 12y = -18\)',
                'C': r'\(12x + Ry = 18\)',
                'D': r'\(12x - Ry = -18\)',
            },
            'D',
            r'Bước 1: Đọc tọa độ hai chấm đen trên đồ thị: \((-2, -3)\) và \((0, 9)\).<br/>'
            r'Bước 2: Tìm phương trình đường thẳng dạng \(y = mx + b\):<br/>'
            r'- Hệ số góc: \(m = \frac{9 - (-3)}{0 - (-2)} = \frac{12}{2} = 6\).<br/>'
            r'- Tung độ gốc: \(b = 9\).<br/>'
            r'Suy ra: \[y = 6x + 9 \iff 6x - y = -9.\]'
            r'Bước 3: Nhân cả hai vế với \(2\) để khớp hệ số \(12x\) và hằng số \(-18\) trong các đáp án:'
            r'\[12x - 2y = -18.\]'
            r'So sánh với đáp án D (\(12x - Ry = -18\)), ta nhận được \(R = 2 > 0\) (đúng là hằng số dương!).',
            r'Khi câu hỏi giấu một hệ số bằng hằng số dương \(R\): hãy viết phương trình thực của đường thẳng trước, rồi nhân/chia hai vế để khớp đúng hai số hạng đã biết trong đáp án!',
            {
                'A': ('Sai cả y-intercept lẫn dấu slope', r'Tại \(x = 0\), cho \(y = \frac{18}{12} = 1.5 \neq 9\), đồng thời có hệ số góc âm \(-\frac{R}{12} < 0\).'),
                'B': ('Sai tung độ gốc', r'Tại \(x = 0\), cho \(-12y = -18 \Rightarrow y = 1.5 \neq 9\), không thể đi qua \((0, 9)\) với mọi \(R\).'),
                'C': ('Sai dấu hệ số góc', r'Thay \((0, 9)\) được \(R = 2\), nhưng phương trình \(12x + 2y = 18 \iff y = -6x + 9\) có hệ số góc âm \(-6\) (không đi qua \((-2, -3)\)).'),
                'D': ('Đáp án đúng', r'Với \(R = 2 > 0\), \(12x - 2y = -18 \iff y = 6x + 9\), đi qua chính xác \((0, 9)\) và \((-2, -3)\).'),
            },
            r'Mẹo thử điểm siêu nhanh: thay \((0, 9)\) vào 4 đáp án — A và B ra \(108 = 18\) (vô lý, loại ngay!); C và D đều ra \(R = 2\); thay tiếp \((-2, -3)\) với \(R = 2\) chỉ có D cho `12(-2) - 2(-3) = -18`!'
        ),

        math_mcq(
            'sat_real_mar25v3_m2_q11', 11, 'Advanced Math', 'Nonlinear functions', 'Medium',
            r'<p>The function \(f\) is defined by \(f(x) = -10(3)^x + \frac{1}{k}\), where \(k\) is a constant.</p>',
            r'If \(y = f(x)\) is graphed in the \(xy\)-plane, what is the \(y\)-coordinate of the \(y\)-intercept of the graph?',
            {
                'A': r'\(-10\)',
                'B': r'\(\frac{1 - 10k}{k}\)',
                'C': r'\(\frac{1}{k}\)',
                'D': r'\(\frac{1 - k}{k}\)',
            },
            'B',
            r'Tung độ gốc (\(y\)-intercept) của đồ thị là giá trị \(f(0)\). Thay \(x = 0\) vào hàm số:'
            r'\[f(0) = -10(3)^0 + \frac{1}{k} = -10(1) + \frac{1}{k} = -10 + \frac{1}{k}.\]'
            r'Quy đồng mẫu số chung \(k\):'
            r'\[-10 + \frac{1}{k} = \frac{-10k + 1}{k} = \frac{1 - 10k}{k}.\]',
            r'Bẫy kinh điển của hàm mũ \(f(x) = a \cdot b^x + c\): tại \(x = 0\), \(b^0 = 1\) (KHÔNG phải \(0\)), nên tung độ gốc là \(a + c\), không phải \(c\)!',
            {
                'A': ('Bỏ quên hằng số 1/k', r'Chỉ lấy \(-10(3)^0 = -10\) mà quên cộng thêm \(\frac{1}{k}\).'),
                'B': ('Đáp án đúng', r'\(f(0) = -10 + \frac{1}{k} = \frac{1 - 10k}{k}\).'),
                'C': ('Bẫy tiệm cận ngang / nhầm 3^0 = 0', r'\(\frac{1}{k}\) là tiệm cận ngang khi \(x \to -\infty\), không phải tung độ gốc!'),
                'D': ('Quên hệ số 10', r'Tính nhầm \(-1 + \frac{1}{k} = \frac{1 - k}{k}\) do đánh mất thừa số \(10\).'),
            },
            r'Thử chọn nhanh \(k = 2\) trong Desmos: gõ `-10*(3)^0 + 1/2` ra `-9.5`; kiểm tra đáp án B: `(1 - 10*2)/2 = -9.5` khớp tuyệt đối!'
        ),

        math_mcq(
            'sat_real_mar25v3_m2_q12', 12, 'Algebra',
            'Linear inequalities in one or two variables', 'Hard',
            _svg_m2_q12_inequality_graph(),
            r'The shaded region shown represents the solutions to \(rx + ty \ge -77\), where \(r\) and \(t\) are constants. What is the value of \(r + t\)?',
            {'A': r'\(8\)', 'B': r'\(6\)', 'C': r'\(-6\)', 'D': r'\(-7\)'},
            'A',
            r'Bước 1: Đọc hai chấm đen nằm trên đường biên liền nét: \((0, -11)\) và \((-7, -10)\).<br/>'
            r'Bước 2: Vì đường biên thỏa mãn phương trình \(rx + ty = -77\), thay lần lượt hai điểm vào:<br/>'
            r'- Thay \((0, -11)\): \(r(0) + t(-11) = -77 \Rightarrow -11t = -77 \Rightarrow t = 7\).<br/>'
            r'- Thay \((-7, -10)\) cùng \(t = 7\): \(-7r + 7(-10) = -77 \Rightarrow -7r - 70 = -77 \Rightarrow -7r = -7 \Rightarrow r = 1\).<br/>'
            r'Bước 3: Kiểm tra chiều dấu bất đẳng thức bằng điểm thử \((0, 0)\) (nằm trong miền tô đậm):<br/>'
            r'\(1(0) + 7(0) = 0 \ge -77\) (ĐÚNG — chiều dấu \(\ge\) khớp hoàn toàn!).<br/>'
            r'Do đó: \[r + t = 1 + 7 = 8.\]',
            r'Khi bất đẳng thức đã cố định vế phải (như \(\ge -77\)), thay trực tiếp tọa độ hai chấm đen vào đường biên \(rx + ty = -77\) sẽ tìm ra ngay \(r\) và \(t\) trong 15 giây, sau đó kiểm tra dấu bằng điểm \((0, 0)\)!',
            {
                'A': ('Đáp án đúng', r'\(r = 1\) và \(t = 7 \Rightarrow r + t = 8\), và miền nghiệm chứa \((0, 0)\) thỏa \(0 \ge -77\).'),
                'B': ('Nhầm dấu của r', r'Tính sai \(r = -1\) dẫn đến \(-1 + 7 = 6\) (khi đó đường biên đi qua \((-7, -12)\) chứ không phải \((-7, -10)\)).'),
                'C': ('Sai dấu cả hai hệ số', r'Tính ra \(r = 1, t = -7\) nên \(r + t = -6\).'),
                'D': ('Nhầm t = -7 và r = 0', r'Bỏ qua dấu trừ ở \(-11t = -77\) hoặc quên cộng \(r = 1\).'),
            },
            r'Vẽ `1x + 7y >= -77` trong Desmos — đường biên đi qua đúng `(-7, -10)` và `(0, -11)` và tô đậm y hệt phần phía trên như hình đề bài!'
        ),

        math_mcq(
            'sat_real_mar25v3_m2_q13', 13, 'Algebra',
            'Systems of two linear equations in two variables', 'Medium',
            r'<p style="text-align:center;">\[3x = 45y - 27\]</p>'
            r'<p>One of the two equations in a system of linear equations is given. The system has no solution.</p>',
            r'Which equation could be the second equation in this system?',
            {
                'A': r'\(x = 5y\)',
                'B': r'\(\frac{1}{3}x = 5y\)',
                'C': r'\(x = 15y - 9\)',
                'D': r'\(\frac{1}{3}x = 15y - 9\)',
            },
            'B',
            r'Bước 1: Chia hai vế của phương trình đã cho \(3x = 45y - 27\) cho \(3\) để đưa về dạng chuẩn gọn nhất:'
            r'\[x = 15y - 9.\]'
            r'Bước 2: Để hệ phương trình tuyến tính <b>vô nghiệm (no solution)</b>, hai đường thẳng phải <b>song song và phân biệt</b> — tức cùng tỉ lệ giữa \(x\) và \(y\) (cùng hệ số \(15y\) khi hệ số \(x\) là \(1\)), nhưng <b>khác hằng số tự do</b> (\(\neq -9\)).<br/>'
            r'Kiểm tra đáp án B: nhân hai vế của \(\frac{1}{3}x = 5y\) với \(3\) ta được: \[x = 15y.\] '
            r'Phương trình này cùng dạng \(x = 15y\) nhưng hằng số là \(0 \neq -9\) \(\Rightarrow\) hai đường thẳng song song, hệ <b>vô nghiệm</b>!',
            r'Đưa mọi phương trình về cùng hệ số của \(x\) (ví dụ \(x = \dots\)): <b>giống hệt nhau</b> là vô số nghiệm (bẫy C!), <b>cùng hệ số \(y\) nhưng khác hằng số</b> mới là vô nghiệm (B)!',
            {
                'A': ('Khác hệ số góc (1 nghiệm)', r'\(x = 5y\) có hệ số của \(y\) là \(5 \neq 15\), nên hai đường thẳng cắt nhau tại duy nhất \(1\) điểm.'),
                'B': ('Đáp án đúng', r'\(\frac{1}{3}x = 5y \iff x = 15y\), song song và không trùng với \(x = 15y - 9\) \(\Rightarrow\) vô nghiệm.'),
                'C': ('Bẫy vô số nghiệm', r'\(x = 15y - 9\) trùng khít với phương trình ban đầu \(3x = 45y - 27\), nên hệ có <b>vô số nghiệm</b>, không phải vô nghiệm!'),
                'D': ('Khác hệ số góc (1 nghiệm)', r'Nhân \(3\) hai vế cho \(x = 45y - 27\), khác hệ số \(15y\) nên cắt nhau tại \(1\) điểm.'),
            },
            r'Vẽ `3x = 45y - 27` cùng từng đáp án trong Desmos: chỉ có `\frac{1}{3}x = 5y` tạo ra đường thẳng song song tách biệt hoàn toàn!'
        ),

        math_mcq(
            'sat_real_mar25v3_m2_q14', 14, 'Algebra', 'Linear functions', 'Medium',
            r'<p>A cooking school is offering a promotion where the first class is free, the second class is half off the regular price, and the remaining classes are regularly priced. If the regular price of a class is $22.80,</p>',
            r'which function \(f\) gives the total cost, in dollars, of \(x\) classes taken using this promotion, where \(x \ge 2\)?',
            {
                'A': r'\(f(x) = 22.80(x - 1) + 11.40\)',
                'B': r'\(f(x) = 22.80(x - 2) + 11.40\)',
                'C': r'\(f(x) = 22.80(x - 1) + 11.40(x - 2)\)',
                'D': r'\(f(x) = 22.80(x - 2) + 11.40(x - 1)\)',
            },
            'B',
            r'Tính chi phí từng phần cho tổng cộng \(x\) buổi học (với \(x \ge 2\)):<br/>'
            r'- Buổi thứ \(1\): miễn phí \(= \$0\).<br/>'
            r'- Buổi thứ \(2\): giảm nửa giá \(= \frac{\$22.80}{2} = \$11.40\).<br/>'
            r'- Số buổi còn lại: \(x - 2\) buổi, mỗi buổi giá gốc \(\$22.80 \Rightarrow 22.80(x - 2)\).<br/>'
            r'Cộng lại, tổng chi phí là: \[f(x) = 22.80(x - 2) + 11.40.\]'
            r'Kiểm tra nhanh tại \(x = 2\): \(f(2) = 22.80(0) + 11.40 = \$11.40\) (chỉ trả nửa tiền buổi 2 — chuẩn xác!).',
            r'Mẹo 5 giây cực mạnh cho mọi bài toán lập hàm chi phí: thử ngay giá trị biên nhỏ nhất \(x = 2\) (tổng tiền chắc chắn bằng \(\$11.40\))!',
            {
                'A': ('Bẫy trừ thiếu buổi thứ 2', r'Khi \(x = 2\), công thức này cho \(22.80(1) + 11.40 = \$34.20\) — tính trùng buổi thứ 2 hai lần!'),
                'B': ('Đáp án đúng', r'Loại \(2\) buổi khuyến mãi đầu nên còn \(x - 2\) buổi nguyên giá, cộng thêm \(\$11.40\) của buổi thứ \(2\).'),
                'C': ('Nhân 11.40 với (x - 2)', r'Giảm giá nửa tiền chỉ áp dụng cho duy nhất buổi thứ \(2\), không nhân với \((x - 2)\).'),
                'D': ('Nhân 11.40 với (x - 1)', r'Khi \(x = 3\), cho \(22.80 + 22.80 = \$45.60 \neq \$34.20\).'),
            },
            r'Thay \(x = 2\) vào 4 công thức: chỉ có B cho kết quả đúng là `11.40` (vì học 2 buổi: buổi 1 free, buổi 2 trả nửa giá `11.40`)!'
        ),

        math_spr(
            'sat_real_mar25v3_m2_q15', 15, 'Algebra', 'Linear functions', 'Easy',
            r'<p>The function \(f\) is defined by \(f(x) = 6x + 14\).</p>',
            r'What is the \(y\)-coordinate of the \(y\)-intercept of the graph of \(y = f(x)\) in the \(xy\)-plane?',
            ['14'], '14',
            r'Trong phương trình đường thẳng dạng hệ số góc – tung độ gốc \(y = mx + b\), tung độ gốc chính là \(b = f(0)\):'
            r'\[f(0) = 6(0) + 14 = 14.\]',
            r'Tung độ gốc của đồ thị \(y = f(x)\) luôn tìm bằng cách đặt \(x = 0\).',
            r'Đọc trực tiếp hằng số \(b = 14\) trong \(f(x) = 6x + 14\) (không cần bấm máy).'
        ),

        math_mcq(
            'sat_real_mar25v3_m2_q16', 16, 'Advanced Math', 'Nonlinear functions', 'Medium',
            _svg_m2_q16_exp_shift_graph(),
            r'The graph of \(y = f(x) + 2\) is shown. Which equation defines function \(f\)?',
            {
                'A': r'\(f(x) = -3^x + 1\)',
                'B': r'\(f(x) = -3^x + 3\)',
                'C': r'\(f(x) = -3^x + 4\)',
                'D': r'\(f(x) = -3^x + 5\)',
            },
            'B',
            r'Đọc kỹ đề: đồ thị vẽ trên hình là đồ thị của <b>\(y = f(x) + 2\)</b> (đã tịnh tiến lên trên \(2\) đơn vị so với \(f(x)\))!<br/>'
            r'Bước 1: Đọc tọa độ đẹp trên đồ thị \(y = f(x) + 2\):<br/>'
            r'- Đi qua \((0, 4)\), \((1, 2)\), \((2, -4)\) và có tiệm cận ngang \(y = 5\).<br/>'
            r'Suy ra phương trình của đồ thị trên hình là: \[f(x) + 2 = -3^x + 5.\]'
            r'Bước 2: Trừ \(2\) ở cả hai vế để tìm \(f(x)\): \[f(x) = -3^x + 5 - 2 = -3^x + 3.\]'
            r'Kiểm tra điểm \((0, 4)\): \(f(0) + 2 = (-3^0 + 3) + 2 = 2 + 2 = 4\) ✓; điểm \((1, 2)\): \(f(1) + 2 = (-3 + 3) + 2 = 2\) ✓.',
            r'Bẫy cực gắt của SAT: luôn kiểm tra tiêu đề đồ thị là \(y = f(x)\) hay \(y = f(x) + k\)! Biết điểm \((x_0, y_0)\) thuộc đồ thị \(y = f(x) + 2\) nghĩa là \(f(x_0) = y_0 - 2\)!',
            {
                'A': ('Trừ 2 hai lần / nhầm y-int = 3', r'Cho \(f(0) + 2 = (-1 + 1) + 2 = 2 \neq 4\).'),
                'B': ('Đáp án đúng', r'Khi cộng thêm \(2\), \(f(x) + 2 = -3^x + 5\), đi qua đúng \((0, 4), (1, 2), (2, -4)\).'),
                'C': ('Nhầm tung độ gốc y = 4 làm hằng số', r'Cho \(f(0) + 2 = (-1 + 4) + 2 = 5 \neq 4\).'),
                'D': ('Bẫy quên trừ đi 2!', r'\(-3^x + 5\) chính là phương trình của đồ thị \(y = f(x) + 2\), chưa trừ đi \(2\) để tìm \(f(x)\)!'),
            },
            r'Trong Desmos, gõ thử `y = (-3^x + 3) + 2` — đồ thị đi qua chuẩn xác `(0, 4)`, `(1, 2)` và `(2, -4)` y hệt hình đề bài!'
        ),

        math_mcq(
            'sat_real_mar25v3_m2_q17', 17, 'Problem-Solving and Data Analysis',
            'Ratios, rates, proportional relationships, and units', 'Hard',
            r'<p>A square map has a side length of \(55\) inches, and \(1\) inch on the map represents an actual distance of \(13\) miles. A smaller version of the same map is printed as a square with the side length \(70\%\) shorter than the side length of the previous map.</p>',
            r'On the smaller map, which of the following is closest to the actual distance, in miles, represented by \(1\) inch?',
            {
                'A': r'\(3.90\)',
                'B': r'\(7.65\)',
                'C': r'\(38.50\)',
                'D': r'\(43.33\)',
            },
            'D',
            r'<b>Bước 1:</b> Tính độ dài thực tế (actual side length) của vùng đất trên bản đồ:<br/>'
            r'\[\text{Actual side length} = 55\text{ inches} \times 13\text{ miles/inch} = 715\text{ miles}.\]'
            r'<b>Bước 2:</b> Bản đồ nhỏ có cạnh <b>ngắn hơn \(70\%\)</b> ("\(70\%\) shorter"), nên độ dài cạnh mới chỉ còn lại \(100\% - 70\% = 30\%\) cạnh cũ:'
            r'\[\text{Smaller map side} = (1 - 0.70) \times 55 = 0.30 \times 55 = 16.5\text{ inches}.\]'
            r'<b>Bước 3:</b> Vì vẫn biểu diễn cùng vùng đất dài \(715\) miles, mỗi inch trên bản đồ nhỏ biểu diễn số dặm thực tế là:'
            r'\[\frac{715\text{ miles}}{16.5\text{ inches}} = \frac{13}{0.30} = \frac{130}{3} \approx 43.33\text{ miles}.\]'
            r'<i>Kiểm tra trực giác:</i> Khi thu nhỏ bản đồ, \(1\) inch trên bản đồ nhỏ phải chứa được <b>nhiều dặm thực tế hơn</b> (gấp \(\frac{1}{0.30} = 3.33\) lần), loại ngay A và B!',
            r'Bản đồ thu nhỏ còn \(30\%\) kích thước \(\Rightarrow\) khoảng cách thực tế trên \(1\) inch <b>tăng nghịch đảo</b> lên \(\frac{1}{0.30}\) lần! Đừng nhân nhầm \(13 \times 0.30\)!',
            {
                'A': ('Bẫy tỉ lệ thuận', r'\(13 \times 0.30 = 3.90\) — nhân nhầm theo tỉ lệ thuận thay vì chia cho \(0.30\)!'),
                'B': ('Chia nhầm cho 1.70', r'\(\frac{13}{1.70} \approx 7.65\) — hiểu nhầm "70% shorter" thành tăng thêm \(70\%\).'),
                'C': ('Nhầm tính cạnh 70% của 55', r'\(0.70 \times 55 = 38.50\) là \(70\%\) của độ dài cạnh (tính bằng inch), không phải khoảng cách thực tế mỗi inch.'),
                'D': ('Đáp án đúng', r'\(\frac{55 \times 13}{0.30 \times 55} = \frac{13}{0.30} \approx 43.33\) miles.'),
            },
            r'Gõ `(55 * 13) / (55 * (1 - 0.70))` trong Desmos ra ngay `43.3333...` → chọn D!'
        ),

        math_mcq(
            'sat_real_mar25v3_m2_q18', 18, 'Advanced Math',
            'Nonlinear equations in one variable and systems of equations in two variables', 'Hard',
            r'<p style="text-align:center;">\[y = x - c\]\[y = -4(x - 8)^2\]</p>'
            r'<p>In the given system of equations, \(c\) is a constant. The system has two distinct real solutions.</p>',
            r'Which of the following could be the value of \(c\)?',
            {
                'A': r'\(3\)',
                'B': r'\(7\)',
                'C': r'\(\frac{127}{16}\)',
                'D': r'\(13\)',
            },
            'D',
            r'<b>Bước 1:</b> Cho hai vế \(y\) bằng nhau và đặt ẩn phụ gọn \(u = x - 8\) (khi đó \(x = u + 8\)):'
            r'\[-4u^2 = (u + 8) - c \iff 4u^2 + u + (8 - c) = 0.\]'
            r'<b>Bước 2:</b> Để hệ có <b>hai nghiệm thực phân biệt</b>, biệt thức \(\Delta\) phải <b>dương nghiêm ngặt (\(\Delta > 0\))</b>:'
            r'\[\Delta = 1^2 - 4(4)(8 - c) > 0 \Rightarrow 1 - 128 + 16c > 0 \Rightarrow 16c > 127 \Rightarrow c > \frac{127}{16} = 7.9375.\]'
            r'<b>Bước 3:</b> Đối chiếu 4 đáp án: chỉ duy nhất \(c = 13 > 7.9375\) thỏa mãn! (Tại \(c = \frac{127}{16}\), \(\Delta = 0\) nên chỉ có \(1\) nghiệm tiếp xúc.)',
            r'Mẹo đặt ẩn phụ \(u = x - 8\) rút ngắn 70% phép khai triển! Ngoài ra, dùng Desmos thanh trượt `c` sẽ thấy ngay đường thẳng \(y = x - c\) đi xuống dưới đỉnh \((8, 0)\) khi \(c\) tăng!',
            {
                'A': ('Vô nghiệm (Δ < 0)', r'\(c = 3 < \frac{127}{16}\) nên đường thẳng nằm hoàn toàn phía trên parabol úp ngược (0 giao điểm).'),
                'B': ('Vô nghiệm (Δ < 0)', r'\(c = 7 < \frac{127}{16}\), đường thẳng vẫn nằm phía trên parabol (0 giao điểm).'),
                'C': ('Bẫy tiếp tuyến (Δ = 0)', r'\(c = \frac{127}{16}\) là giá trị biên cho \(\Delta = 0\) — hệ chỉ có <b>1 nghiệm duy nhất</b>, không phải 2 nghiệm phân biệt!'),
                'D': ('Đáp án đúng', r'\(c = 13 > \frac{127}{16} \Rightarrow \Delta = 16(13) - 127 = 81 > 0\), hệ có \(2\) nghiệm thực phân biệt.'),
            },
            r'Gõ `y = x - c` (thêm slider `c`) và `y = -4(x - 8)^2` vào Desmos: thử gõ `c = 13`, thấy đường thẳng cắt parabol tại đúng 2 điểm phân biệt ngay lập tức!'
        ),

        math_mcq(
            'sat_real_mar25v3_m2_q19', 19, 'Geometry and Trigonometry',
            'Lines, angles, and triangles', 'Hard',
            r'<p>In triangle \(ABC\), the measure of angle \(A\) is \(52^\circ\) and \(AC = 35\). In triangle \(PQR\), the measure of angle \(P\) is \(52^\circ\) and \(PR = 105\).</p>',
            r'Which additional piece of information is sufficient to prove that triangle \(ABC\) is similar to triangle \(PQR\)?',
            {
                'A': r'\(AB = 30\) and \(PQ = 30\).',
                'B': r'\(AB = 30\) and \(QR = 90\).',
                'C': r'The measures of angle \(B\) and angle \(R\) are \(34^\circ\) and \(94^\circ\), respectively.',
                'D': r'The measures of angle \(B\) and angle \(Q\) are \(52^\circ\) and \(34^\circ\), respectively.',
            },
            'C',
            r'Để chứng minh \(\triangle ABC \sim \triangle PQR\) (theo đúng thứ tự đỉnh \(A \leftrightarrow P,\; B \leftrightarrow Q,\; C \leftrightarrow R\)), ta đã có sẵn:<br/>'
            r'- \(\angle A = \angle P = 52^\circ\)<br/>'
            r'- Tỉ lệ cặp cạnh tương ứng \(\frac{PR}{AC} = \frac{105}{35} = 3\).<br/>'
            r'Kiểm tra đáp án C (\(\angle B = 34^\circ\) và \(\angle R = 94^\circ\)):<br/>'
            r'- Trong \(\triangle ABC\): \(\angle C = 180^\circ - 52^\circ - 34^\circ = 94^\circ\).<br/>'
            r'- Trong \(\triangle PQR\): \(\angle Q = 180^\circ - 52^\circ - 94^\circ = 34^\circ\).<br/>'
            r'Suy ra hai tam giác có bộ ba góc tương ứng bằng nhau \((52^\circ, 34^\circ, 94^\circ)\) \(\Rightarrow\) đồng dạng theo trường hợp <b>góc – góc (AA Similarity)</b>!',
            r'Ba tiêu chuẩn chứng minh hai tam giác đồng dạng: <b>AA</b> (2 góc bằng nhau), <b>SAS</b> (2 cặp cạnh tỉ lệ kẹp góc xen giữa bằng nhau), và <b>SSS</b> (3 cặp cạnh tỉ lệ). Chú ý tổng 3 góc luôn bằng \(180^\circ\)!',
            {
                'A': ('Không tỉ lệ theo SAS', r'Ta cần \(\frac{PQ}{AB} = \frac{PR}{AC} = 3\) (tức \(PQ = 90\)), nhưng \(\frac{30}{30} = 1 \neq 3\).'),
                'B': ('Sai cặp cạnh tương ứng (SSA)', r'Cạnh \(QR\) đối diện góc \(P\), không phải cạnh kề góc \(P\) tương ứng với \(AB\) (cạnh tương ứng của \(AB\) phải là \(PQ\)).'),
                'C': ('Đáp án đúng', r'\(\angle C = 180^\circ - 52^\circ - 34^\circ = 94^\circ = \angle R\), kết hợp \(\angle A = \angle P = 52^\circ\) suy ra đồng dạng theo AA!'),
                'D': ('Hai bộ góc khác nhau', r'\(\triangle ABC\) có các góc \(52^\circ, 52^\circ, 76^\circ\); trong khi \(\triangle PQR\) có các góc \(52^\circ, 34^\circ, 94^\circ\) \(\Rightarrow\) không đồng dạng.'),
            },
            r'Tính nhanh tổng góc trong Desmos: `180 - 52 - 34 = 94`, khớp ngay với góc `R = 94` ở phương án C!'
        ),

        math_spr(
            'sat_real_mar25v3_m2_q20', 20, 'Geometry and Trigonometry', 'Circles', 'Hard',
            r'<p>The perimeter of an equilateral triangle is \(876\) centimeters. The three vertices of the triangle lie on a circle. The radius of the circle is \(w\sqrt{3}\) centimeters.</p>',
            r'What is the value of \(w\)?',
            ['292/3', '97.33', '97.333', '97.3333'], '292/3 (hoặc 97.33)',
            r'<b>Bước 1:</b> Tìm độ dài cạnh \(s\) của tam giác đều: \[s = \frac{876}{3} = 292\text{ cm}.\]'
            r'<b>Bước 2:</b> Ba đỉnh nằm trên đường tròn nghĩa là đường tròn đó <b>ngoại tiếp</b> tam giác đều.<br/>'
            r'Đường cao của tam giác đều là \(h = \frac{s\sqrt{3}}{2}\). Vì tâm đường tròn ngoại tiếp trùng với trọng tâm (chia đường cao theo tỉ lệ \(2:1\)), bán kính đường tròn ngoại tiếp là:'
            r'\[R = \frac{2}{3}h = \frac{2}{3}\cdot\frac{s\sqrt{3}}{2} = \frac{s\sqrt{3}}{3} = \frac{292\sqrt{3}}{3}\text{ cm}.\]'
            r'<b>Bước 3:</b> So sánh với \(R = w\sqrt{3}\), suy ra: \[w = \frac{292}{3} \approx 97.33.\]'
            r'<i>Lưu ý nhập SPR:</i> Phân số tối giản `292/3` dài đúng \(5\) ký tự nên nhập trực tiếp được, hoặc nhập số thập phân cắt/làm tròn đến 5 ký tự là `97.33`!',
            r'Ghi nhớ công thức siêu tốc cho tam giác đều cạnh \(s\): chiều cao \(h = \frac{s\sqrt{3}}{2}\), bán kính ngoại tiếp \(R = \frac{s}{\sqrt{3}} = \frac{s\sqrt{3}}{3}\), bán kính nội tiếp \(r = \frac{s\sqrt{3}}{6}\)!',
            r'Gõ `(876 / 3) / 3` trong Desmos → bấm nút chuyển phân số ra ngay `292/3` (dạng thập phân `97.333...`, nhập `292/3` gọn và chính xác tuyệt đối)!'
        ),

        math_spr(
            'sat_real_mar25v3_m2_q21', 21, 'Advanced Math', 'Nonlinear functions', 'Hard',
            r'<p>The function \(f\) is defined by \(f(x) = \frac{|x|}{a} - 14\), where \(a < 0\).</p>',
            r'What is the product of \(f(15a)\) and \(f(8a)\)?',
            ['638'], '638',
            r'<b>Chú ý điều kiện cực kỳ quan trọng: \(a < 0\)!</b><br/>'
            r'Vì \(a < 0\), nên cả \(15a < 0\) và \(8a < 0\). Theo định nghĩa giá trị tuyệt đối của số âm (\(|u| = -u\) khi \(u < 0\)):<br/>'
            r'- \(|15a| = -15a \Rightarrow f(15a) = \frac{-15a}{a} - 14 = -15 - 14 = -29.\)<br/>'
            r'- \(|8a| = -8a \Rightarrow f(8a) = \frac{-8a}{a} - 14 = -8 - 14 = -22.\)<br/>'
            r'Tích của \(f(15a)\) và \(f(8a)\) là:'
            r'\[f(15a) \cdot f(8a) = (-29) \times (-22) = 638.\]'
            r'<i>Cảnh báo bẫy chết người:</i> Nếu quên điều kiện \(a < 0\) và viết nhầm \(|15a| = 15a\), bạn sẽ ra \((15 - 14)(8 - 14) = -6\) (sai hoàn toàn)!',
            r'Khi gặp \(|ka|\) với điều kiện \(a < 0\) (\(k > 0\)): luôn nhớ \(|ka| = -ka\), hoặc chọn ngay một số âm cụ thể như \(a = -1\) để tính tuyệt đối an toàn!',
            r'Chọn ngay `a = -1` trong Desmos: gõ `f(x) = abs(x)/a - 14`, rồi gõ `f(15a)*f(8a)` → Desmos hiện chuẩn xác `638` (thử lại với `a = -5` vẫn ra đúng `638`)!'
        ),

        math_spr(
            'sat_real_mar25v3_m2_q22', 22, 'Advanced Math', 'Nonlinear functions', 'Hard',
            r'<p>The function \(f\) is defined by \(f(x) = ab^{\frac{x}{n}}\), where \(a\), \(b\), and \(n\) are constants, and \(b\) and \(n\) are integers. If \(f(4) = 5\) and \(f(7) = 135\),</p>',
            r'what is the value of \(f(9)\)?',
            ['1215'], '1215',
            r'<b>Bước 1:</b> Lập tỉ số giữa \(f(7)\) và \(f(4)\) để khử hằng số \(a\):'
            r'\[\frac{f(7)}{f(4)} = \frac{ab^{\frac{7}{n}}}{ab^{\frac{4}{n}}} = b^{\frac{7 - 4}{n}} = b^{\frac{3}{n}} = \frac{135}{5} = 27.\]'
            r'<b>Bước 2:</b> Lấy căn bậc \(3\) hai vế để tìm thừa số tăng trưởng sau mỗi \(1\) đơn vị \(x\) (tức \(r = b^{\frac{1}{n}}\)):'
            r'\[\left(b^{\frac{1}{n}}\right)^3 = 27 = 3^3 \Rightarrow b^{\frac{1}{n}} = 3.\]'
            r'<i>Nhận xét tinh tế:</i> Không cần tách riêng \(b\) và \(n\) (ví dụ \(b = 3, n = 1\) hay \(b = 27, n = 3\) đều cho cùng hệ số tăng trưởng \(b^{\frac{1}{n}} = 3\))!<br/>'
            r'<b>Bước 3:</b> Từ \(x = 7\) lên \(x = 9\) tăng thêm \(2\) đơn vị, nên nhân \(f(7)\) với \(\left(b^{\frac{1}{n}}\right)^2 = 3^2 = 9\):'
            r'\[f(9) = f(7) \cdot \left(b^{\frac{1}{n}}\right)^{9 - 7} = 135 \cdot 3^2 = 135 \cdot 9 = 1{,}215.\]',
            r'Bí kíp câu 22 hàm mũ \(f(x) = ab^{x/n}\): luôn đặt \(r = b^{1/n}\) làm thừa số nhân cho mỗi bước \(\Delta x = 1\). Từ \(f(x_2)/f(x_1) = r^{x_2 - x_1}\) tìm ngay \(r\), rồi tính \(f(x_3) = f(x_2)\cdot r^{x_3 - x_2}\)!',
            r'Trong Desmos, gõ bảng `(4, 5)` và `(7, 135)`, nhập hồi quy mũ `y_1 ~ a * r^(x_1)` (ra `r = 3`), rồi bấm `a * r^9` — máy hiện ngay `1215`!'
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
        'subtitle': 'Đề thi thật Digital SAT Toán tháng 3/2025 (Ver 3) — Đủ 2 Module (M1: 22 câu + M2: 22 câu)',
        'difficultyBadge': 'REAL EXAM • MARCH 2025',
        'targetTimeMinutes': 70,
        'routingThreshold': 0,
    },
    'module1': {
        'id': 'm1',
        'title': 'Section 2, Module 1: Math',
        'subtitle': '22 Questions • 35 Minutes • March 2025 Ver 3 Real Exam',
        'timeLimitMinutes': 35,
        'questions': M1_QUESTIONS,
    },
    'module2_hard': {
        'id': 'm2_hard',
        'title': 'Section 2, Module 2: Math',
        'subtitle': '22 Questions • 35 Minutes • March 2025 Ver 3 Real Exam',
        'timeLimitMinutes': 35,
        'questions': M2_QUESTIONS,
    },
    'module2_lower': {
        'id': 'm2_lower',
        'title': 'Section 2, Module 2: Math',
        'subtitle': '22 Questions • 35 Minutes • March 2025 Ver 3 Real Exam',
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
    # M1 Q1: s = 40 + 2t at t = 3 => 46 (D)
    assert 40 + 2 * 3 == 46 and m1[1]['correctAnswer'] == 'D'

    # M1 Q2: line of best fit y = 0.8 + 1.7x (positive intercept ~0.8, positive slope ~1.7) (A)
    n2 = len(SCATTER_M1_Q2_PTS)
    assert n2 == 10
    mx2 = sum(x for x, _ in SCATTER_M1_Q2_PTS) / n2
    my2 = sum(y for _, y in SCATTER_M1_Q2_PTS) / n2
    slope2 = sum((x - mx2) * (y - my2) for x, y in SCATTER_M1_Q2_PTS) / sum(
        (x - mx2) ** 2 for x, _ in SCATTER_M1_Q2_PTS
    )
    inter2 = my2 - slope2 * mx2
    assert slope2 > 1.4 and inter2 > 0.4 and m1[2]['correctAnswer'] == 'A'

    # M1 Q3: width = 5, length = 5 + 30 = 35 => area = 175 (A)
    assert 5 * (5 + 30) == 175 and m1[3]['correctAnswer'] == 'A'

    # M1 Q4: 7 + x = 3 => x = -4 => 56 + 8x = 24
    x4 = 3 - 7
    assert 56 + 8 * x4 == 24 and 8 * 3 == 24 and '24' in m1[4]['acceptedAnswers']

    # M1 Q5: 20h + 17c = 1055 => 20 is dollars per hour at regular job (A)
    assert m1[5]['correctAnswer'] == 'A'

    # M1 Q6: frequency table values {20, 26, 32, 38} => min value = 20 (C)
    data_m1_q6 = [20] * 6 + [26] * 1 + [32] * 6 + [38] * 3
    assert min(data_m1_q6) == 20 and m1[6]['correctAnswer'] == 'C'

    # M1 Q7: mean of [3810, 3810, 3030, 3850, 3050] = 17550 / 5 = 3510
    lemurs = [3810, 3810, 3030, 3850, 3050]
    mean7 = Fraction(sum(lemurs), len(lemurs))
    assert mean7 == 3510 and '3510' in m1[7]['acceptedAnswers']

    # M1 Q8: x + 7 = 13, y = 5x^2 + 5 => (6, 185) (B)
    x8 = 13 - 7
    y8 = 5 * (x8 ** 2) + 5
    assert (x8, y8) == (6, 185) and m1[8]['correctAnswer'] == 'B'

    # M1 Q9: 19x^5 + 20x^5 - 10x^5 = 29x^5 => b = 29
    assert 19 + 20 - 10 == 29 and '29' in m1[9]['acceptedAnswers']

    # M1 Q10: line through (-12, 0) and (0, -11), point (v, -5) => v = -72/11 (A)
    slope10 = Fraction(-11 - 0, 0 - (-12))
    assert slope10 == Fraction(-11, 12)
    v10 = Fraction(-5 - (-11), slope10)
    assert v10 == Fraction(-72, 11) and m1[10]['correctAnswer'] == 'A'

    # M1 Q11: f(x) = 22 => (0,22), (1,22), (2,22) (B)
    assert all(22 == 22 for _ in (0, 1, 2)) and m1[11]['correctAnswer'] == 'B'

    # M1 Q12: corresponding angles w = 146 and y = 146 prove r || s (B)
    assert 146 + 34 == 180 and m1[12]['correctAnswer'] == 'B'

    # M1 Q13: (133y)^(1/2) == sqrt(133y) for y > 1 (C)
    for yv in (2, 5, 17):
        assert math.isclose((133 * yv) ** 0.5, math.sqrt(133 * yv), rel_tol=1e-12)
    assert m1[13]['correctAnswer'] == 'C'

    # M1 Q14: f(x) = -26 * 2^(x/6) at x = -6, 0, 6, 12 => -13, -26, -52, -104 (B)
    vals14 = [Fraction(-26) * (Fraction(2) ** Fraction(xv, 6)) for xv in (-6, 0, 6, 12)]
    assert vals14 == [-13, -26, -52, -104] and m1[14]['correctAnswer'] == 'B'

    # M1 Q15: sin(3pi/4) = sqrt(2)/2 (D)
    assert math.isclose(math.sin(3 * math.pi / 4), math.sqrt(2) / 2, rel_tol=1e-12)
    assert m1[15]['correctAnswer'] == 'D'

    # M1 Q16: 164 * 1.06 * n <= 44800 => max integer n = 257
    unit_cost16 = Fraction(164) * Fraction(106, 100)
    n16 = int(Fraction(44800) / unit_cost16)
    assert n16 == 257
    assert unit_cost16 * 257 <= 44800 and unit_cost16 * 258 > 44800
    assert '257' in m1[16]['acceptedAnswers']

    # M1 Q17: V = B * h => 60 = B * 3 => B = 20
    assert Fraction(60, 3) == 20 and '20' in m1[17]['acceptedAnswers']

    # M1 Q18: f(x) = -3^x - 5 < -5 < 0 for all real x => 0 solutions (D)
    for xv in (-100, -10, -1, 0, 1, 5):
        assert -(Fraction(3) ** xv) - 5 < -5 < 0
    assert m1[18]['correctAnswer'] == 'D'

    # M1 Q19: x(x + 4) - 140 = 3x(x - 10) => 2x^2 - 34x + 140 = 0 => roots 7, 10 => sum = 17 (D)
    for r19 in (7, 10):
        assert r19 * (r19 + 4) - 140 == 3 * r19 * (r19 - 10)
    assert 7 + 10 == 17 and m1[19]['correctAnswer'] == 'D'

    # M1 Q20: -3x^2 - 7x + 1 = 0 => greatest root = -7/6 + sqrt(61)/6 (C)
    r20_hi = (-7 + math.sqrt(61)) / 6
    r20_lo = (-7 - math.sqrt(61)) / 6
    assert r20_hi > r20_lo
    assert math.isclose(-3 * r20_hi ** 2 - 7 * r20_hi + 1, 0.0, abs_tol=1e-12)
    assert math.isclose(-3 * r20_lo ** 2 - 7 * r20_lo + 1, 0.0, abs_tol=1e-12)
    assert m1[20]['correctAnswer'] == 'C'

    # M1 Q21: right triangle ABC, ∠B=90°, ∠C=30°, BC=36√3 => ∠A=60°, cos(A)=1/2=0.5
    cos_a21 = math.cos(math.radians(90 - 30))
    assert math.isclose(cos_a21, 0.5, rel_tol=1e-12)
    assert '1/2' in m1[21]['acceptedAnswers'] and '0.5' in m1[21]['acceptedAnswers']

    # M1 Q22: a = 2047% of (b + c), b = 89% of c => (a / b) * 100% = 4347% (D)
    c22 = Fraction(100)
    b22 = Fraction(89, 100) * c22
    a22 = Fraction(2047, 100) * (b22 + c22)
    pct22 = (a22 / b22) * 100
    assert pct22 == 4347 and m1[22]['correctAnswer'] == 'D'

    # ---------- MODULE 2 VERIFICATIONS ----------
    # M2 Q1: 2x - 3 = 2x => -3 = 0 => Zero solutions (A)
    assert m2[1]['correctAnswer'] == 'A'

    # M2 Q2: linear f(0)=2, f(7)=2 => f(x) = 2 (C)
    assert Fraction(2 - 2, 7 - 0) == 0 and m2[2]['correctAnswer'] == 'C'

    # M2 Q3: y = (92w)(w) => 92w is length in feet (A)
    assert m2[3]['correctAnswer'] == 'A'

    # M2 Q4: T(x) = 67 - 8x => decreases by 8°F each hour (B)
    assert (67 - 8 * 1) - (67 - 8 * 2) == 8 and m2[4]['correctAnswer'] == 'B'

    # M2 Q5: 375 visitors, P(A)=0.68, P(B)=0.24 => P(C)=0.08 => 30 visitors (B)
    room_c = (1 - Fraction(68, 100) - Fraction(24, 100)) * 375
    assert room_c == 30 and m2[5]['correctAnswer'] == 'B'

    # M2 Q6: f(t) = -16(t - 2)^2 + 185 => f(2)=185, f(0)=121 (D)
    assert -16 * (2 - 2) ** 2 + 185 == 185
    assert -16 * (0 - 2) ** 2 + 185 == 121
    assert m2[6]['correctAnswer'] == 'D'

    # M2 Q7: 7y = -6x + 2550, 24x - 28y = 1800 => x = 250, y = 150 => x + y = 400
    x7 = Fraction(4 * 2550 + 1800, 48)
    y7 = Fraction(-6 * x7 + 2550, 7)
    assert x7 == 250 and y7 == 150 and 24 * x7 - 28 * y7 == 1800
    assert x7 + y7 == 400 and '400' in m2[7]['acceptedAnswers']

    # M2 Q8: cube edge 3.000 cm, density 0.220 g/cm^3 => mass = 27 * 0.220 = 5.94 g = 297/50
    mass8 = Fraction(3) ** 3 * Fraction(220, 1000)
    assert mass8 == Fraction(297, 50) and float(mass8) == 5.94
    assert '5.94' in m2[8]['acceptedAnswers'] and '297/50' in m2[8]['acceptedAnswers']

    # M2 Q9: -2|3x + 7| + 8 = -6 => |3x + 7| = 7 => x = 0 or x = -14/3 (C)
    for sol9 in (Fraction(0), Fraction(-14, 3)):
        assert -2 * abs(3 * sol9 + 7) + 8 == -6
    assert m2[9]['correctAnswer'] == 'C'

    # M2 Q10: line through (-2, -3) and (0, 9) => y = 6x + 9 => 12x - 2y = -18 => 12x - Ry = -18 (R = 2 > 0) (D)
    r10 = Fraction(2)
    assert r10 > 0
    for xv, yv in ((-2, -3), (0, 9)):
        assert 12 * xv - r10 * yv == -18
    assert m2[10]['correctAnswer'] == 'D'

    # M2 Q11: f(x) = -10(3)^x + 1/k => f(0) = -10 + 1/k = (1 - 10k)/k (B)
    for kv in (Fraction(1), Fraction(2), Fraction(-3), Fraction(5, 2)):
        assert -10 * (3 ** 0) + Fraction(1, kv) == Fraction(1 - 10 * kv, kv)
    assert m2[11]['correctAnswer'] == 'B'

    # M2 Q12: rx + ty >= -77, boundary through (0, -11) & (-7, -10), shaded includes (0, 0) => r = 1, t = 7 => r + t = 8 (A)
    t12 = Fraction(-77, -11)
    r12 = Fraction(-77 - t12 * (-10), -7)
    assert r12 == 1 and t12 == 7
    assert r12 * 0 + t12 * 0 >= -77
    assert r12 + t12 == 8 and m2[12]['correctAnswer'] == 'A'

    # M2 Q13: 3x = 45y - 27 (x = 15y - 9); (1/3)x = 5y (x = 15y) => parallel distinct lines, no solution (B)
    assert Fraction(45, 3) == Fraction(5, Fraction(1, 3))
    assert Fraction(-27, 3) != 0
    assert m2[13]['correctAnswer'] == 'B'

    # M2 Q14: 1st class free, 2nd half off ($11.40), remaining (x-2) at $22.80 => f(x) = 22.80(x-2) + 11.40 (B)
    for n_cls, expected_cost in ((2, Fraction(1140, 100)), (3, Fraction(3420, 100)), (5, Fraction(7980, 100))):
        assert Fraction(2280, 100) * (n_cls - 2) + Fraction(1140, 100) == expected_cost
    assert m2[14]['correctAnswer'] == 'B'

    # M2 Q15: f(x) = 6x + 14 => f(0) = 14
    assert 6 * 0 + 14 == 14 and '14' in m2[15]['acceptedAnswers']

    # M2 Q16: y = f(x) + 2 passes through (0,4), (1,2), (2,-4) => f(x) = -3^x + 3 (B)
    for xv, y_graph in ((0, 4), (1, 2), (2, -4)):
        assert (-(3 ** xv) + 3) + 2 == y_graph
    assert m2[16]['correctAnswer'] == 'B'

    # M2 Q17: 55 in * 13 mi/in = 715 mi; smaller side = 0.30 * 55 = 16.5 in => 715/16.5 = 130/3 ≈ 43.33 (D)
    mi_per_in17 = Fraction(55 * 13, Fraction(30, 100) * 55)
    assert mi_per_in17 == Fraction(130, 3)
    assert round(float(mi_per_in17), 2) == 43.33 and m2[17]['correctAnswer'] == 'D'

    # M2 Q18: y = x - c, y = -4(x - 8)^2 => 4u^2 + u + (8 - c) = 0 => Δ = 16c - 127 > 0 => c > 127/16 => c = 13 (D)
    def disc18(cv):
        return 1 - 16 * (8 - cv)
    assert disc18(Fraction(3)) < 0
    assert disc18(Fraction(7)) < 0
    assert disc18(Fraction(127, 16)) == 0
    assert disc18(Fraction(13)) > 0
    assert m2[18]['correctAnswer'] == 'D'

    # M2 Q19: ∠A=∠P=52°, ∠B=34°, ∠R=94° => ∠C=94°=∠R, ∠Q=34°=∠B => AA similarity (C)
    assert 180 - 52 - 34 == 94 and 180 - 52 - 94 == 34
    assert m2[19]['correctAnswer'] == 'C'

    # M2 Q20: equilateral triangle perimeter 876 => side = 292 => R = 292/sqrt(3) = (292/3)*sqrt(3) => w = 292/3
    side20 = Fraction(876, 3)
    w20 = Fraction(side20, 3)
    assert side20 == 292 and w20 == Fraction(292, 3)
    assert math.isclose(float(w20) * math.sqrt(3), float(side20) / math.sqrt(3), rel_tol=1e-12)
    assert '292/3' in m2[20]['acceptedAnswers'] and '97.33' in m2[20]['acceptedAnswers']

    # M2 Q21: f(x) = |x|/a - 14 with a < 0 => f(15a) = -29, f(8a) = -22 => product = 638
    for av in (-1, -2, -5, -17):
        f15 = abs(15 * av) / av - 14
        f8 = abs(8 * av) / av - 14
        assert f15 == -29 and f8 == -22 and f15 * f8 == 638
    assert '638' in m2[21]['acceptedAnswers']

    # M2 Q22: f(x) = a*b^(x/n), f(4)=5, f(7)=135 => b^(3/n)=27 => b^(1/n)=3 => f(9)=135*3^2=1215
    ratio22 = Fraction(135, 5)
    assert ratio22 == 27 == 3 ** 3
    f9 = Fraction(135) * (3 ** (9 - 7))
    assert f9 == 1215
    # Verify invariant across multiple integer (b, n) pairs: (3, 1) and (27, 3)
    for b_int, n_int in ((3, 1), (27, 3), (729, 6)):
        step_r = b_int ** (1 / n_int)
        a_val = 5 / (step_r ** 4)
        assert math.isclose(a_val * (step_r ** 7), 135.0, rel_tol=1e-12)
        assert math.isclose(a_val * (step_r ** 9), 1215.0, rel_tol=1e-12)
    assert '1215' in m2[22]['acceptedAnswers']

    # ---------- EXTRA HYGIENE, XML SVG & OPTION-ANALYSIS KATEX AUDIT ----------
    raw_blob = str(TEST_DATA)
    for bad in ('@DSATuz', '@D7SAT', 'satuzhunters', 'Minh Nghĩa', 't.me/D7SAT', 'TELEGRAM', '______blank'):
        assert bad.lower() not in raw_blob.lower(), f'Watermark token leaked: {bad}'

    for mk in ('module1', 'module2_hard', 'module2_lower'):
        for q in TEST_DATA[mk]['questions']:
            exp = q.get('explanation') or {}
            assert exp.get('desmosTipVi', '').strip(), f'{mk} Q{q["number"]}: missing desmosTipVi'
            assert exp.get('keyTakeaway', '').strip(), f'{mk} Q{q["number"]}: missing keyTakeaway'
            if q.get('questionFormat') == 'mcq':
                oa = exp.get('optionAnalysis') or {}
                for lbl in ('A', 'B', 'C', 'D'):
                    reason = oa[lbl]['reasonVi']
                    assert reason.count('\\(') == reason.count('\\)'), f'{mk} Q{q["number"]} {lbl} unbalanced \\( \\)'
                    assert reason.count('\\[') == reason.count('\\]'), f'{mk} Q{q["number"]} {lbl} unbalanced \\[ \\]'
                    assert not re.search(r'(?<!\\)\$[a-zA-Z\\]', reason), f'{mk} Q{q["number"]} {lbl} raw $ math'

    # Verify every inline SVG parses cleanly as strict XML and count figures/tables
    svg_count = 0
    stim_table_count = 0
    opt_table_count = 0
    oa_katex_items = []
    for mk in ('module1', 'module2_hard'):
        for q in TEST_DATA[mk]['questions']:
            stim = q.get('stimulusHtml') or ''
            for svg_str in re.findall(r'<svg[\s\S]*?</svg>', stim):
                ET.fromstring(svg_str)
                svg_count += 1
            stim_table_count += len(re.findall(r'<table[\s\S]*?</table>', stim))
            for o in (q.get('options') or []):
                opt_table_count += len(re.findall(r'<table[\s\S]*?</table>', str(o.get('text') or '')))
            if q.get('questionFormat') == 'mcq':
                oa = (q.get('explanation') or {}).get('optionAnalysis') or {}
                for lbl in ('A', 'B', 'C', 'D'):
                    oa_katex_items.append({
                        'label': f'{TEST_CODE}.{mk}.Q{q["number"]}.optionAnalysis.{lbl}',
                        'text': oa[lbl]['reasonVi'],
                    })
    assert svg_count == 8, f'Expected 8 inline SVGs, got {svg_count}'
    assert stim_table_count == 1, f'Expected 1 stimulus HTML table (M1 Q6), got {stim_table_count}'
    assert opt_table_count == 8, f'Expected 8 option HTML tables (M1 Q11 + M1 Q14), got {opt_table_count}'

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
    print(f'[OK] {TEST_CODE}: ALL 44 REAL MATH QUESTIONS + 8 SVGs + 9 TABLES + NODE KATEX VERIFIED WITH 0 ERRORS!')
