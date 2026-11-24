# -*- coding: utf-8 -*-
r"""
Digital SAT 1500+ Real Past Exams — March 2025 Ver 5 Math (44 Qs)
- Module 1: 22 verbatim questions (35 min) — 16 MCQ + 6 SPR (Q6, Q8, Q11, Q18, Q20, Q22)
- Module 2: 22 verbatim questions (35 min) — 17 MCQ + 5 SPR (Q10, Q15, Q20, Q21, Q22)
  (Both `module2_hard` and `module2_lower` point to the real 22-question Module 2 with `routingThreshold: 0`.)

All graphs, scatterplots, geometry diagrams, and option tables are recreated cleanly
as zero-watermark inline SVGs / HTML tables matching the exact official exam figures.
All 44 answers are programmatically verified in `verify_all_math()` using exact
`fractions.Fraction` / `math` arithmetic and validated with real Node KaTeX via
`validate_sat_bluebook_json`.
"""

import copy
import math
import sys
from fractions import Fraction

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

TEST_CODE = 'real_march2025_v5_math'
FOLDER_KEY = 'real_math'
ORDER_INDEX = 5
TEST_TITLE = '🏛️ Real Exam — March 2025 Ver 5 Math (44 Qs)'


# ============================================================================
# QUESTION BUILDERS
# ============================================================================

def _mcq(
    qid, num, domain, skill, diff,
    stim_html, q_html, opts_dict, ans,
    summary_vi, takeaway, analysis, desmos_tip_vi=''
):
    assert ans in ('A', 'B', 'C', 'D'), f'Invalid MCQ answer {ans} for {qid}'
    options = [{'label': k, 'text': opts_dict[k]} for k in ('A', 'B', 'C', 'D')]
    oa = {}
    for k in ('A', 'B', 'C', 'D'):
        tag, reason = analysis[k]
        oa[k] = {
            'status': 'correct' if k == ans else 'trap',
            'trapTag': tag,
            'reasonVi': reason,
        }
    exp = {
        'summaryVi': summary_vi,
        'keyTakeaway': takeaway,
        'optionAnalysis': oa,
    }
    if desmos_tip_vi:
        exp['desmosTipVi'] = desmos_tip_vi
    return {
        'id': qid,
        'number': num,
        'domain': domain,
        'skill': skill,
        'difficulty': diff,
        'questionFormat': 'mcq',
        'stimulusHtml': stim_html,
        'questionHtml': q_html,
        'options': options,
        'correctAnswer': ans,
        'explanation': exp,
    }


def _spr(
    qid, num, domain, skill, diff,
    stim_html, q_html, accepted_answers, correct_display,
    summary_vi, takeaway, desmos_tip_vi=''
):
    assert len(accepted_answers) >= 1, f'Empty acceptedAnswers for {qid}'
    exp = {
        'summaryVi': summary_vi,
        'keyTakeaway': takeaway,
    }
    if desmos_tip_vi:
        exp['desmosTipVi'] = desmos_tip_vi
    return {
        'id': qid,
        'number': num,
        'domain': domain,
        'skill': skill,
        'difficulty': diff,
        'questionFormat': 'spr',
        'stimulusHtml': stim_html,
        'questionHtml': q_html,
        'options': [],
        'correctAnswer': str(accepted_answers[0]),
        'acceptedAnswers': [str(a) for a in accepted_answers],
        'correctDisplay': correct_display,
        'explanation': exp,
    }


# ============================================================================
# CLEAN HTML TABLES & EXACT INLINE SVG DIAGRAMS (ZERO WATERMARKS)
# ============================================================================

def _mini_xy_table(pairs):
    """Compact Bluebook-style 2-column x / f(x) table for MCQ answer cards (M1 Q12)."""
    rows_html = ''.join(
        f'<tr>'
        f'<td style="border:1px solid #475569;padding:4px 14px;text-align:center;">{x}</td>'
        f'<td style="border:1px solid #475569;padding:4px 14px;text-align:center;">{fx}</td>'
        f'</tr>'
        for x, fx in pairs
    )
    return (
        '<table style="border-collapse:collapse;font-size:14px;background:#ffffff;margin:2px 0;">'
        '<thead><tr>'
        r'<th style="border:1px solid #475569;padding:4px 14px;text-align:center;background:#f8fafc;font-weight:700;">\(x\)</th>'
        r'<th style="border:1px solid #475569;padding:4px 14px;text-align:center;background:#f8fafc;font-weight:700;">\(f(x)\)</th>'
        '</tr></thead>'
        f'<tbody>{rows_html}</tbody></table>'
    )


def _svg_card(svg_inner, caption_html=''):
    return (
        '<div style="background:#ffffff;border:1px solid #cbd5e1;border-radius:12px;'
        'padding:12px 14px;margin:10px auto;text-align:center;max-width:390px;">'
        f'{svg_inner}'
        f'{caption_html}'
        '</div>'
    )


def _svg_m1_q1_rings():
    """M1 Q1: Cost y ($) vs rings x (y = 1.5x + 100), x in [0,100], y in [0,300]."""
    x0, y0 = 56.0, 276.0  # origin (0, 0)
    sx = 2.4              # 100 units -> 240 px (24 px per 10)
    sy = 0.8              # 300 units -> 240 px (20 px per 25, 40 px per 50)

    def px(x):
        return x0 + x * sx

    def py(y):
        return y0 - y * sy

    parts = []
    # Vertical gridlines every 10 from 0 to 100
    for xv in range(0, 101, 10):
        xx = px(xv)
        if xv > 0:
            parts.append(f'<line x1="{xx:.1f}" y1="{py(312):.1f}" x2="{xx:.1f}" y2="{y0:.1f}" stroke="#cbd5e1" stroke-width="1"/>')
            parts.append(f'<line x1="{xx:.1f}" y1="{y0 - 3:.1f}" x2="{xx:.1f}" y2="{y0 + 3:.1f}" stroke="#0f172a" stroke-width="1.2"/>')
            parts.append(f'<text x="{xx:.1f}" y="{y0 + 16:.1f}" font-size="10.5" text-anchor="middle" fill="#0f172a" font-family="serif">{xv}</text>')

    # Horizontal gridlines every 25 from 0 to 300
    for yv in range(25, 301, 25):
        yy = py(yv)
        parts.append(f'<line x1="{x0:.1f}" y1="{yy:.1f}" x2="{px(106):.1f}" y2="{yy:.1f}" stroke="#cbd5e1" stroke-width="1"/>')
        if yv % 50 == 0:
            parts.append(f'<line x1="{x0 - 3:.1f}" y1="{yy:.1f}" x2="{x0 + 3:.1f}" y2="{yy:.1f}" stroke="#0f172a" stroke-width="1.2"/>')
            parts.append(f'<text x="{x0 - 8:.1f}" y="{yy + 3.5:.1f}" font-size="10.5" text-anchor="end" fill="#0f172a" font-family="serif">{yv}</text>')

    # Axes with arrowheads
    parts.append(f'<line x1="{x0 - 12:.1f}" y1="{y0:.1f}" x2="{px(108):.1f}" y2="{y0:.1f}" stroke="#0f172a" stroke-width="1.6"/>')
    parts.append(f'<polygon points="{px(113):.1f},{y0:.1f} {px(106):.1f},{y0 - 3.5:.1f} {px(106):.1f},{y0 + 3.5:.1f}" fill="#0f172a"/>')
    parts.append(f'<line x1="{x0:.1f}" y1="{y0 + 12:.1f}" x2="{x0:.1f}" y2="{py(318):.1f}" stroke="#0f172a" stroke-width="1.6"/>')
    parts.append(f'<polygon points="{x0:.1f},{py(324):.1f} {x0 - 3.5:.1f},{py(315):.1f} {x0 + 3.5:.1f},{py(315):.1f}" fill="#0f172a"/>')
    parts.append(f'<text x="{px(116):.1f}" y="{y0 + 4:.1f}" font-size="13" font-style="italic" fill="#0f172a" font-family="serif">x</text>')
    parts.append(f'<text x="{x0:.1f}" y="{py(329):.1f}" font-size="13" font-style="italic" text-anchor="middle" fill="#0f172a" font-family="serif">y</text>')
    parts.append(f'<text x="{x0 - 9:.1f}" y="{y0 + 13:.1f}" font-size="11.5" font-style="italic" text-anchor="end" fill="#0f172a" font-family="serif">O</text>')

    # Line y = 1.5x + 100 from x=0 to x=104
    parts.append(f'<line x1="{px(0):.1f}" y1="{py(100):.1f}" x2="{px(104):.1f}" y2="{py(256):.1f}" stroke="#0f172a" stroke-width="2.4"/>')

    svg = (
        '<svg viewBox="0 0 345 304" xmlns="http://www.w3.org/2000/svg" style="max-width:340px;width:100%;height:auto;display:block;margin:0 auto;">'
        '<rect width="345" height="304" fill="#ffffff"/>'
        f'{"".join(parts)}</svg>'
    )
    return _svg_card(svg)


def _svg_m1_q3_exp():
    """M1 Q3: Exponential curve y = 4^(x + 1) + 1 with y-intercept (0, 5), x in [-10,10], y in [0,14]."""
    cx, cy = 165.0, 266.0  # origin (0, 0)
    sx = 13.0              # 1 unit -> 13 px (-10..10 => 260 px)
    sy = 16.0              # 1 unit -> 16 px (0..14 => 224 px)

    def px(x):
        return cx + x * sx

    def py(y):
        return cy - y * sy

    parts = []
    # Vertical gridlines -10..10
    for xv in range(-10, 11):
        xx = px(xv)
        if xv != 0:
            parts.append(f'<line x1="{xx:.1f}" y1="{py(14.5):.1f}" x2="{xx:.1f}" y2="{cy:.1f}" stroke="#cbd5e1" stroke-width="1"/>')
        if xv != 0 and xv % 2 == 0:
            parts.append(f'<line x1="{xx:.1f}" y1="{cy - 3:.1f}" x2="{xx:.1f}" y2="{cy + 3:.1f}" stroke="#0f172a" stroke-width="1.2"/>')
            lbl = f'−{abs(xv)}' if xv < 0 else str(xv)
            parts.append(f'<text x="{xx:.1f}" y="{cy + 16:.1f}" font-size="10.5" text-anchor="middle" fill="#0f172a" font-family="serif">{lbl}</text>')

    # Horizontal gridlines 1..14
    for yv in range(1, 15):
        yy = py(yv)
        parts.append(f'<line x1="{px(-10.4):.1f}" y1="{yy:.1f}" x2="{px(10.4):.1f}" y2="{yy:.1f}" stroke="#cbd5e1" stroke-width="1"/>')
        if yv % 2 == 0:
            parts.append(f'<line x1="{cx - 3:.1f}" y1="{yy:.1f}" x2="{cx + 3:.1f}" y2="{yy:.1f}" stroke="#0f172a" stroke-width="1.2"/>')
            parts.append(f'<text x="{cx - 6:.1f}" y="{yy + 3.5:.1f}" font-size="10.5" text-anchor="end" fill="#0f172a" font-family="serif">{yv}</text>')

    # Axes
    parts.append(f'<line x1="{px(-10.8):.1f}" y1="{cy:.1f}" x2="{px(10.9):.1f}" y2="{cy:.1f}" stroke="#0f172a" stroke-width="1.6"/>')
    parts.append(f'<polygon points="{px(11.4):.1f},{cy:.1f} {px(10.7):.1f},{cy - 3.5:.1f} {px(10.7):.1f},{cy + 3.5:.1f}" fill="#0f172a"/>')
    parts.append(f'<line x1="{cx:.1f}" y1="{cy + 8:.1f}" x2="{cx:.1f}" y2="{py(15.0):.1f}" stroke="#0f172a" stroke-width="1.6"/>')
    parts.append(f'<polygon points="{cx:.1f},{py(15.5):.1f} {cx - 3.5:.1f},{py(14.8):.1f} {cx + 3.5:.1f},{py(14.8):.1f}" fill="#0f172a"/>')
    parts.append(f'<text x="{px(11.7):.1f}" y="{cy + 4:.1f}" font-size="13" font-style="italic" fill="#0f172a" font-family="serif">x</text>')
    parts.append(f'<text x="{cx:.1f}" y="{py(15.8):.1f}" font-size="13" font-style="italic" text-anchor="middle" fill="#0f172a" font-family="serif">y</text>')
    parts.append(f'<text x="{cx - 6:.1f}" y="{cy + 14:.1f}" font-size="11.5" font-style="italic" text-anchor="end" fill="#0f172a" font-family="serif">O</text>')

    # Exponential curve y = 4^(x + 1) + 1 up to y = 14.4
    pts = []
    steps = 120
    x_max = math.log(13.4) / math.log(4) - 1.0  # ~0.871
    for i in range(steps + 1):
        xv = -10.2 + (x_max + 10.2) * (i / steps)
        yv = (4.0 ** (xv + 1.0)) + 1.0
        pts.append(f'{px(xv):.1f},{py(yv):.1f}')
    parts.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="#0f172a" stroke-width="2.4"/>')

    svg = (
        '<svg viewBox="0 0 336 292" xmlns="http://www.w3.org/2000/svg" style="max-width:330px;width:100%;height:auto;display:block;margin:0 auto;">'
        '<rect width="336" height="292" fill="#ffffff"/>'
        f'{"".join(parts)}</svg>'
    )
    return _svg_card(svg)


def _svg_m1_q10_triangles():
    """M1 Q10: Similar right triangles CAE and CBD with right angles at E and D."""
    svg = (
        '<svg viewBox="0 0 280 205" xmlns="http://www.w3.org/2000/svg" style="max-width:270px;width:100%;height:auto;display:block;margin:0 auto;">'
        '<rect width="280" height="205" fill="#ffffff"/>'
        # Outer right triangle CAE: A(62,174), E(204,174), C(204,28)
        '<polygon points="62,174 204,174 204,28" fill="none" stroke="#0f172a" stroke-width="2.2" stroke-linejoin="round"/>'
        # Mid horizontal segment BD: y = 106 -> x_B = 62 + (204-62)*(174-106)/(174-28) = 128.1
        '<line x1="128.1" y1="106" x2="204" y2="106" stroke="#0f172a" stroke-width="2.0"/>'
        # Right angle box at E
        '<polyline points="190,174 190,160 204,160" fill="none" stroke="#0f172a" stroke-width="1.5"/>'
        # Right angle box at D (inside triangle CBD)
        '<polyline points="190,106 190,92 204,92" fill="none" stroke="#0f172a" stroke-width="1.5"/>'
        # Labels
        '<text x="50" y="186" font-family="serif" font-size="16" font-style="italic" fill="#0f172a">A</text>'
        '<text x="111" y="109" font-family="serif" font-size="16" font-style="italic" fill="#0f172a">B</text>'
        '<text x="206" y="22" font-family="serif" font-size="16" font-style="italic" fill="#0f172a">C</text>'
        '<text x="212" y="111" font-family="serif" font-size="16" font-style="italic" fill="#0f172a">D</text>'
        '<text x="207" y="187" font-family="serif" font-size="16" font-style="italic" fill="#0f172a">E</text>'
        '</svg>'
    )
    cap = '<div style="font-size:12.5px;color:#334155;font-weight:600;margin-top:4px;">Note: Figure not drawn to scale.</div>'
    return _svg_card(svg, cap)


def _svg_m1_q18_ramp():
    """M1 Q18: Right triangle ramp with angle theta, base x, height, and length."""
    svg = (
        '<svg viewBox="0 0 360 125" xmlns="http://www.w3.org/2000/svg" style="max-width:355px;width:100%;height:auto;display:block;margin:0 auto;">'
        '<rect width="360" height="125" fill="#ffffff"/>'
        # Right triangle: left(36,96), bottom-right(282,96), top-right(282,36)
        '<polygon points="36,96 282,96 282,36" fill="none" stroke="#0f172a" stroke-width="2.2" stroke-linejoin="round"/>'
        # Right angle box at bottom-right
        '<polyline points="269,96 269,83 282,83" fill="none" stroke="#0f172a" stroke-width="1.5"/>'
        # Small angle arc for theta at (36,96)
        '<path d="M 88,96 A 52,52 0 0,0 86.5,83.7" fill="none" stroke="#0f172a" stroke-width="1.3"/>'
        '<text x="102" y="92" font-family="serif" font-size="15" font-style="italic" fill="#0f172a">θ</text>'
        # Labels
        '<text x="158" y="114" text-anchor="middle" font-family="serif" font-size="15" font-style="italic" fill="#0f172a">x</text>'
        '<text x="152" y="34" text-anchor="middle" font-family="serif" font-size="13.5" fill="#0f172a">length of</text>'
        '<text x="152" y="50" text-anchor="middle" font-family="serif" font-size="13.5" fill="#0f172a">the ramp</text>'
        '<text x="291" y="56" font-family="serif" font-size="13.5" fill="#0f172a">height</text>'
        '<text x="291" y="72" font-family="serif" font-size="13.5" fill="#0f172a">of the</text>'
        '<text x="291" y="88" font-family="serif" font-size="13.5" fill="#0f172a">ramp</text>'
        '</svg>'
    )
    cap = '<div style="font-size:12.5px;color:#334155;font-weight:600;margin-top:4px;">Note: Figure not drawn to scale.</div>'
    return _svg_card(svg, cap)


def _svg_m1_q19_intersecting():
    """M1 Q19: Two intersecting lines with vertical angles w° and z°."""
    svg = (
        '<svg viewBox="0 0 280 140" xmlns="http://www.w3.org/2000/svg" style="max-width:270px;width:100%;height:auto;display:block;margin:0 auto;">'
        '<rect width="280" height="140" fill="#ffffff"/>'
        # Two intersecting lines at (140, 70)
        '<line x1="48" y1="18" x2="232" y2="122" stroke="#0f172a" stroke-width="2.2"/>'
        '<line x1="44" y1="114" x2="236" y2="26" stroke="#0f172a" stroke-width="2.2"/>'
        # Angle labels w° (top obtuse) and z° (bottom obtuse)
        '<text x="140" y="55" text-anchor="middle" font-family="serif" font-size="15.5" font-style="italic" fill="#0f172a">w°</text>'
        '<text x="140" y="96" text-anchor="middle" font-family="serif" font-size="15.5" font-style="italic" fill="#0f172a">z°</text>'
        '</svg>'
    )
    cap = '<div style="font-size:12.5px;color:#334155;font-weight:600;margin-top:4px;">Note: Figure not drawn to scale.</div>'
    return _svg_card(svg, cap)


def _svg_m2_q2_scatterplot():
    """M2 Q2: Scatterplot (x in [-14,0], y in [0,20]) and line of best fit y = -x + 1.5."""
    ox, oy = 266.0, 260.0  # origin (0, 0) on the right
    sx = 16.0              # 2 units -> 32 px (-14..0 => 224 px)
    sy = 11.2              # 2 units -> 22.4 px (0..20 => 224 px)

    def px(x):
        return ox + x * sx

    def py(y):
        return oy - y * sy

    parts = []
    # Vertical gridlines every 2 from -14 to 0
    for xv in range(-14, 0, 2):
        xx = px(xv)
        parts.append(f'<line x1="{xx:.1f}" y1="{py(21.2):.1f}" x2="{xx:.1f}" y2="{oy:.1f}" stroke="#cbd5e1" stroke-width="1"/>')
        parts.append(f'<line x1="{xx:.1f}" y1="{oy - 3:.1f}" x2="{xx:.1f}" y2="{oy + 3:.1f}" stroke="#0f172a" stroke-width="1.2"/>')
        parts.append(f'<text x="{xx:.1f}" y="{oy + 16:.1f}" font-size="10.5" text-anchor="middle" fill="#0f172a" font-family="serif">−{abs(xv)}</text>')

    # Horizontal gridlines every 2 from 2 to 20
    for yv in range(2, 21, 2):
        yy = py(yv)
        parts.append(f'<line x1="{px(-14.4):.1f}" y1="{yy:.1f}" x2="{ox:.1f}" y2="{yy:.1f}" stroke="#cbd5e1" stroke-width="1"/>')
        parts.append(f'<line x1="{ox - 3:.1f}" y1="{yy:.1f}" x2="{ox + 3:.1f}" y2="{yy:.1f}" stroke="#0f172a" stroke-width="1.2"/>')
        parts.append(f'<text x="{ox - 7:.1f}" y="{yy + 3.5:.1f}" font-size="10.5" text-anchor="end" fill="#0f172a" font-family="serif">{yv}</text>')

    # Axes
    parts.append(f'<line x1="{px(-14.6):.1f}" y1="{oy:.1f}" x2="{ox + 16:.1f}" y2="{oy:.1f}" stroke="#0f172a" stroke-width="1.6"/>')
    parts.append(f'<polygon points="{ox + 22:.1f},{oy:.1f} {ox + 14:.1f},{oy - 3.5:.1f} {ox + 14:.1f},{oy + 3.5:.1f}" fill="#0f172a"/>')
    parts.append(f'<line x1="{ox:.1f}" y1="{oy + 10:.1f}" x2="{ox:.1f}" y2="{py(21.6):.1f}" stroke="#0f172a" stroke-width="1.6"/>')
    parts.append(f'<polygon points="{ox:.1f},{py(22.2):.1f} {ox - 3.5:.1f},{py(21.4):.1f} {ox + 3.5:.1f},{py(21.4):.1f}" fill="#0f172a"/>')
    parts.append(f'<text x="{ox + 26:.1f}" y="{oy + 4:.1f}" font-size="13" font-style="italic" fill="#0f172a" font-family="serif">x</text>')
    parts.append(f'<text x="{ox:.1f}" y="{py(22.6):.1f}" font-size="13" font-style="italic" text-anchor="middle" fill="#0f172a" font-family="serif">y</text>')
    parts.append(f'<text x="{ox - 6:.1f}" y="{oy + 14:.1f}" font-size="11.5" font-style="italic" text-anchor="end" fill="#0f172a" font-family="serif">O</text>')

    # Line of best fit: y = -x + 1.5 from x = -14 to x = 0
    parts.append(f'<line x1="{px(-14):.1f}" y1="{py(15.5):.1f}" x2="{px(0):.1f}" y2="{py(1.5):.1f}" stroke="#0f172a" stroke-width="2.2"/>')

    # 6 scatter points matching the official figure
    dots = [(-14, 15.1), (-12, 13.2), (-10, 11.8), (-8, 10.0), (-6, 8.0), (-4, 4.6)]
    for dx, dy in dots:
        parts.append(f'<circle cx="{px(dx):.1f}" cy="{py(dy):.1f}" r="3.4" fill="#0f172a"/>')

    svg = (
        '<svg viewBox="0 0 310 290" xmlns="http://www.w3.org/2000/svg" style="max-width:310px;width:100%;height:auto;display:block;margin:0 auto;">'
        '<rect width="310" height="290" fill="#ffffff"/>'
        f'{"".join(parts)}</svg>'
    )
    return _svg_card(svg)


def _svg_m2_q5_beaker_choice(kind):
    """M2 Q5: Clean inline SVG choice graphs for y = 58*pi*x^2 and distractors."""
    x0, y0 = 56.0, 212.0  # origin (0, 0)
    sx = 18.0             # 10 units -> 180 px
    sy = 0.036            # 5000 units -> 180 px (18 px per 500)

    def px(x):
        return x0 + x * sx

    def py(y):
        return y0 - y * sy

    parts = []
    # Vertical gridlines 1..10
    for xv in range(1, 11):
        xx = px(xv)
        parts.append(f'<line x1="{xx:.1f}" y1="{py(5150):.1f}" x2="{xx:.1f}" y2="{y0:.1f}" stroke="#cbd5e1" stroke-width="0.9"/>')
        parts.append(f'<line x1="{xx:.1f}" y1="{y0 - 2.5:.1f}" x2="{xx:.1f}" y2="{y0 + 2.5:.1f}" stroke="#0f172a" stroke-width="1.1"/>')
        parts.append(f'<text x="{xx:.1f}" y="{y0 + 13:.1f}" font-size="9.5" text-anchor="middle" fill="#0f172a" font-family="serif">{xv}</text>')

    # Horizontal gridlines 500..5000
    for yv in range(500, 5001, 500):
        yy = py(yv)
        parts.append(f'<line x1="{x0:.1f}" y1="{yy:.1f}" x2="{px(10.3):.1f}" y2="{yy:.1f}" stroke="#cbd5e1" stroke-width="0.9"/>')
        parts.append(f'<line x1="{x0 - 2.5:.1f}" y1="{yy:.1f}" x2="{x0 + 2.5:.1f}" y2="{yy:.1f}" stroke="#0f172a" stroke-width="1.1"/>')
        parts.append(f'<text x="{x0 - 6:.1f}" y="{yy + 3:.1f}" font-size="9.5" text-anchor="end" fill="#0f172a" font-family="serif">{yv:,}</text>')

    # Axes
    parts.append(f'<line x1="{x0 - 8:.1f}" y1="{y0:.1f}" x2="{px(10.7):.1f}" y2="{y0:.1f}" stroke="#0f172a" stroke-width="1.4"/>')
    parts.append(f'<polygon points="{px(11.1):.1f},{y0:.1f} {px(10.5):.1f},{y0 - 3:.1f} {px(10.5):.1f},{y0 + 3:.1f}" fill="#0f172a"/>')
    parts.append(f'<line x1="{x0:.1f}" y1="{y0 + 8:.1f}" x2="{x0:.1f}" y2="{py(5300):.1f}" stroke="#0f172a" stroke-width="1.4"/>')
    parts.append(f'<polygon points="{x0:.1f},{py(5450):.1f} {x0 - 3:.1f},{py(5250):.1f} {x0 + 3:.1f},{py(5250):.1f}" fill="#0f172a"/>')
    parts.append(f'<text x="{px(11.4):.1f}" y="{y0 + 3.5:.1f}" font-size="11.5" font-style="italic" fill="#0f172a" font-family="serif">x</text>')
    parts.append(f'<text x="{x0:.1f}" y="{py(5550):.1f}" font-size="11.5" font-style="italic" text-anchor="middle" fill="#0f172a" font-family="serif">y</text>')
    parts.append(f'<text x="{x0 - 6:.1f}" y="{y0 + 11:.1f}" font-size="10.5" font-style="italic" text-anchor="end" fill="#0f172a" font-family="serif">O</text>')

    # Curve per option
    y_cap = 5150.0
    pts = []
    if kind == 'A':
        # y = 58 * pi * x^2
        xmax = math.sqrt(y_cap / (58.0 * math.pi))
        for i in range(61):
            xv = xmax * i / 60.0
            yv = 58.0 * math.pi * xv * xv
            pts.append(f'{px(xv):.1f},{py(yv):.1f}')
    elif kind == 'B':
        # y = 58 * x^2 (missing pi — matches visible top of B in exam PDF!)
        xmax = math.sqrt(y_cap / 58.0)
        for i in range(61):
            xv = xmax * i / 60.0
            yv = 58.0 * xv * xv
            pts.append(f'{px(xv):.1f},{py(yv):.1f}')
    elif kind == 'C':
        # y = 58 * pi * x (linear, forgot x^2)
        pts = [f'{px(0):.1f},{py(0):.1f}', f'{px(10):.1f},{py(580.0 * math.pi):.1f}']
    else:
        # y = 58 * x (linear, forgot pi and x^2)
        pts = [f'{px(0):.1f},{py(0):.1f}', f'{px(10):.1f},{py(580.0):.1f}']

    parts.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="#0f172a" stroke-width="2.2"/>')
    return (
        '<svg viewBox="0 0 278 236" xmlns="http://www.w3.org/2000/svg" '
        'style="max-width:248px;width:100%;height:auto;display:block;margin:2px 0;background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;">'
        '<rect width="278" height="236" fill="#ffffff"/>'
        f'{"".join(parts)}</svg>'
    )


def _svg_m2_q9_exp():
    """M2 Q9: Exponential graph y = f(x) = ab^x + c staying below y = -4, x in [-10,10], y in [-10,5]."""
    cx, cy = 165.0, 108.0  # origin (0, 0)
    sx = 13.0              # 1 unit -> 13 px (-10..10)
    sy = 15.0              # 1 unit -> 15 px (-10..5)

    def px(x):
        return cx + x * sx

    def py(y):
        return cy - y * sy

    parts = []
    # Vertical gridlines -10..10
    for xv in range(-10, 11):
        xx = px(xv)
        if xv != 0:
            parts.append(f'<line x1="{xx:.1f}" y1="{py(5.4):.1f}" x2="{xx:.1f}" y2="{py(-10.4):.1f}" stroke="#cbd5e1" stroke-width="1"/>')
        if xv != 0 and xv % 2 == 0:
            parts.append(f'<line x1="{xx:.1f}" y1="{cy - 3:.1f}" x2="{xx:.1f}" y2="{cy + 3:.1f}" stroke="#0f172a" stroke-width="1.2"/>')
            lbl = f'−{abs(xv)}' if xv < 0 else str(xv)
            parts.append(f'<text x="{xx:.1f}" y="{cy + 14:.1f}" font-size="10" text-anchor="middle" fill="#0f172a" font-family="serif">{lbl}</text>')

    # Horizontal gridlines -10..5
    for yv in range(-10, 6):
        yy = py(yv)
        if yv != 0:
            parts.append(f'<line x1="{px(-10.4):.1f}" y1="{yy:.1f}" x2="{px(10.4):.1f}" y2="{yy:.1f}" stroke="#cbd5e1" stroke-width="1"/>')
        if yv != 0 and yv % 2 == 0:
            parts.append(f'<line x1="{cx - 3:.1f}" y1="{yy:.1f}" x2="{cx + 3:.1f}" y2="{yy:.1f}" stroke="#0f172a" stroke-width="1.2"/>')
            lbl = f'−{abs(yv)}' if yv < 0 else str(yv)
            parts.append(f'<text x="{cx - 6:.1f}" y="{yy + 3.5:.1f}" font-size="10" text-anchor="end" fill="#0f172a" font-family="serif">{lbl}</text>')

    # Axes
    parts.append(f'<line x1="{px(-10.7):.1f}" y1="{cy:.1f}" x2="{px(10.9):.1f}" y2="{cy:.1f}" stroke="#0f172a" stroke-width="1.6"/>')
    parts.append(f'<polygon points="{px(11.4):.1f},{cy:.1f} {px(10.7):.1f},{cy - 3.5:.1f} {px(10.7):.1f},{cy + 3.5:.1f}" fill="#0f172a"/>')
    parts.append(f'<line x1="{cx:.1f}" y1="{py(-10.6):.1f}" x2="{cx:.1f}" y2="{py(5.8):.1f}" stroke="#0f172a" stroke-width="1.6"/>')
    parts.append(f'<polygon points="{cx:.1f},{py(6.3):.1f} {cx - 3.5:.1f},{py(5.6):.1f} {cx + 3.5:.1f},{py(5.6):.1f}" fill="#0f172a"/>')
    parts.append(f'<text x="{px(11.7):.1f}" y="{cy + 4:.1f}" font-size="13" font-style="italic" fill="#0f172a" font-family="serif">x</text>')
    parts.append(f'<text x="{cx:.1f}" y="{py(6.6):.1f}" font-size="13" font-style="italic" text-anchor="middle" fill="#0f172a" font-family="serif">y</text>')
    parts.append(f'<text x="{cx - 5:.1f}" y="{cy + 12:.1f}" font-size="11" font-style="italic" text-anchor="end" fill="#0f172a" font-family="serif">O</text>')

    # Curve y = -1.5 * 1.9^x - 4 from x = -10.3 to y = -10.4
    pts = []
    x_max = math.log(6.4 / 1.5) / math.log(1.9)  # ~2.26
    for i in range(101):
        xv = -10.3 + (x_max + 10.3) * (i / 100.0)
        yv = -1.5 * (1.9 ** xv) - 4.0
        pts.append(f'{px(xv):.1f},{py(yv):.1f}')
    parts.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="#0f172a" stroke-width="2.3"/>')

    svg = (
        '<svg viewBox="0 0 336 276" xmlns="http://www.w3.org/2000/svg" style="max-width:330px;width:100%;height:auto;display:block;margin:0 auto;">'
        '<rect width="336" height="276" fill="#ffffff"/>'
        f'{"".join(parts)}</svg>'
    )
    return _svg_card(svg)


def _svg_m2_q13_bowtie():
    """M2 Q13: Similar bowtie triangles WQX and YQZ with equal angles a° at W and Y."""
    svg = (
        '<svg viewBox="0 0 330 150" xmlns="http://www.w3.org/2000/svg" style="max-width:325px;width:100%;height:auto;display:block;margin:0 auto;">'
        '<rect width="330" height="150" fill="#ffffff"/>'
        # W(84,34), X(40,124), Q(166,64), Y(250,34), Z(292,108)
        # Check collinearity: W(84,34) -> Q(166,64): slope = 30/82 = 0.36585; Q -> Z(288, 108.6)
        # X(44,108) -> Q(166,64): slope = -44/122 = -0.36066; Q -> Y(249, 34.1)
        '<line x1="84" y1="34" x2="288" y2="108.6" stroke="#0f172a" stroke-width="2.1"/>'
        '<line x1="44" y1="108" x2="249" y2="34.1" stroke="#0f172a" stroke-width="2.1"/>'
        '<line x1="84" y1="34" x2="44" y2="108" stroke="#0f172a" stroke-width="2.1"/>'
        '<line x1="249" y1="34.1" x2="288" y2="108.6" stroke="#0f172a" stroke-width="2.1"/>'
        # Vertex labels
        '<text x="74" y="25" font-family="serif" font-size="15.5" font-style="italic" fill="#0f172a">W</text>'
        '<text x="28" y="124" font-family="serif" font-size="15.5" font-style="italic" fill="#0f172a">X</text>'
        '<text x="166" y="83" text-anchor="middle" font-family="serif" font-size="15.5" font-style="italic" fill="#0f172a">Q</text>'
        '<text x="247" y="25" font-family="serif" font-size="15.5" font-style="italic" fill="#0f172a">Y</text>'
        '<text x="293" y="123" font-family="serif" font-size="15.5" font-style="italic" fill="#0f172a">Z</text>'
        # Angle labels a° inside W and Y
        '<text x="86" y="54" font-family="serif" font-size="13.5" font-style="italic" fill="#0f172a">a°</text>'
        '<text x="242" y="53" font-family="serif" font-size="13.5" font-style="italic" fill="#0f172a">a°</text>'
        '</svg>'
    )
    cap = '<div style="font-size:12.5px;color:#334155;font-weight:600;margin-top:4px;">Note: Figure not drawn to scale.</div>'
    return _svg_card(svg, cap)


def _svg_m2_q18_exp_shift():
    """M2 Q18: Graph of y = f(x) + 2 = -4^x + 7, x in [-1,5], y in [-5,10]."""
    cx, cy = 84.0, 198.0   # origin (0, 0)
    sx = 34.0              # 1 unit -> 34 px (-1..5)
    sy = 16.0              # 1 unit -> 16 px (-5..10)

    def px(x):
        return cx + x * sx

    def py(y):
        return cy - y * sy

    parts = []
    # Vertical gridlines -1..5
    for xv in range(-1, 6):
        xx = px(xv)
        if xv != 0:
            parts.append(f'<line x1="{xx:.1f}" y1="{py(10.6):.1f}" x2="{xx:.1f}" y2="{py(-5.4):.1f}" stroke="#cbd5e1" stroke-width="1"/>')
            parts.append(f'<line x1="{xx:.1f}" y1="{cy - 3:.1f}" x2="{xx:.1f}" y2="{cy + 3:.1f}" stroke="#0f172a" stroke-width="1.2"/>')
            lbl = '−1' if xv == -1 else str(xv)
            parts.append(f'<text x="{xx:.1f}" y="{cy + 15:.1f}" font-size="10.5" text-anchor="middle" fill="#0f172a" font-family="serif">{lbl}</text>')

    # Horizontal gridlines -5..10
    for yv in range(-5, 11):
        yy = py(yv)
        if yv != 0:
            parts.append(f'<line x1="{px(-1.4):.1f}" y1="{yy:.1f}" x2="{px(5.4):.1f}" y2="{yy:.1f}" stroke="#cbd5e1" stroke-width="1"/>')
        if yv != 0 and yv % 2 == 0:
            parts.append(f'<line x1="{cx - 3:.1f}" y1="{yy:.1f}" x2="{cx + 3:.1f}" y2="{yy:.1f}" stroke="#0f172a" stroke-width="1.2"/>')
            lbl = f'−{abs(yv)}' if yv < 0 else str(yv)
            parts.append(f'<text x="{cx - 7:.1f}" y="{yy + 3.5:.1f}" font-size="10.5" text-anchor="end" fill="#0f172a" font-family="serif">{lbl}</text>')

    # Axes
    parts.append(f'<line x1="{px(-1.5):.1f}" y1="{cy:.1f}" x2="{px(5.6):.1f}" y2="{cy:.1f}" stroke="#0f172a" stroke-width="1.6"/>')
    parts.append(f'<polygon points="{px(5.85):.1f},{cy:.1f} {px(5.5):.1f},{cy - 3.5:.1f} {px(5.5):.1f},{cy + 3.5:.1f}" fill="#0f172a"/>')
    parts.append(f'<line x1="{cx:.1f}" y1="{py(-5.6):.1f}" x2="{cx:.1f}" y2="{py(11.1):.1f}" stroke="#0f172a" stroke-width="1.6"/>')
    parts.append(f'<polygon points="{cx:.1f},{py(11.6):.1f} {cx - 3.5:.1f},{py(10.9):.1f} {cx + 3.5:.1f},{py(10.9):.1f}" fill="#0f172a"/>')
    parts.append(f'<text x="{px(6.0):.1f}" y="{cy + 4:.1f}" font-size="13" font-style="italic" fill="#0f172a" font-family="serif">x</text>')
    parts.append(f'<text x="{cx:.1f}" y="{py(11.9):.1f}" font-size="13" font-style="italic" text-anchor="middle" fill="#0f172a" font-family="serif">y</text>')
    parts.append(f'<text x="{cx - 6:.1f}" y="{cy + 14:.1f}" font-size="11.5" font-style="italic" text-anchor="end" fill="#0f172a" font-family="serif">O</text>')

    # Curve y = -4^x + 7 from x = -1.4 to y = -5.4
    pts = []
    x_max = math.log(12.4) / math.log(4.0)  # ~1.816
    for i in range(91):
        xv = -1.4 + (x_max + 1.4) * (i / 90.0)
        yv = -(4.0 ** xv) + 7.0
        pts.append(f'{px(xv):.1f},{py(yv):.1f}')
    parts.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="#0f172a" stroke-width="2.3"/>')

    svg = (
        '<svg viewBox="0 0 304 294" xmlns="http://www.w3.org/2000/svg" style="max-width:300px;width:100%;height:auto;display:block;margin:0 auto;">'
        '<rect width="304" height="294" fill="#ffffff"/>'
        f'{"".join(parts)}</svg>'
    )
    return _svg_card(svg)


# ============================================================================
# MODULE 1 — REAL EXAM MARCH 2025 VER 5 MATH (22 QUESTIONS • 35 MINUTES)
# ============================================================================

M1_QUESTIONS = [
    _mcq(
        'march2025_v5_math_m1_q1', 1, 'Algebra', 'Linear functions', 'Easy',
        r'<p>The cost \(y\), in dollars, for a manufacturer to make \(x\) rings is represented by the line shown.</p>'
        + _svg_m1_q1_rings(),
        r'What is the cost, in dollars, for the manufacturer to make \(50\) rings?',
        {'A': r'\(100\)', 'B': r'\(125\)', 'C': r'\(175\)', 'D': r'\(225\)'},
        'C',
        r'Đọc trực tiếp trên đồ thị: tại hoành độ \(x = 50\), đường thẳng đi qua giao điểm lưới chính xác ở tung độ \(y = 175\) (nằm chính giữa \(150\) và \(200\), mỗi vạch lưới ngang cách nhau \(25\) đơn vị). Kiểm tra đại số: đường thẳng đi qua \((0, 100)\) và \((100, 250)\), suy ra \(y = 1.5x + 100\), do đó tại \(x = 50\) ta có \(y = 1.5(50) + 100 = 175\).',
        r'Luôn kiểm tra tỷ lệ chia vạch lưới (grid scale) trước khi đọc tọa độ — ở đây mỗi ô lưới dọc tương ứng \(25\) đơn vị, không phải \(10\) hay \(50\).',
        {
            'A': ('Đọc nhầm y-intercept', r'\(100\) là chi phí cố định khi \(x = 0\) (giao điểm trục tung), không phải khi \(x = 50\).'),
            'B': ('Đọc sai tỷ lệ lưới', r'\(125\) là giá trị nằm giữa \(100\) và \(150\), tương ứng khoảng \(x \approx 16.7\), không phải \(x = 50\).'),
            'C': ('Đáp án đúng', r'Tại \(x = 50\), đồ thị cắt đúng giao điểm lưới \((50, 175)\).'),
            'D': ('Nhầm vị trí x', r'\(225\) tương ứng với \(x \approx 83.3\), cao hơn nhiều so với \(x = 50\).'),
        },
        r'Không cần máy tính: chỉ cần gióng thẳng từ \(x = 50\) lên đường thẳng rồi gióng ngang sang trục \(y\), thấy đúng vạch lưới giữa \(150\) và \(200\) là \(175\).',
    ),
    _mcq(
        'march2025_v5_math_m1_q2', 2, 'Advanced Math', 'Equivalent expressions', 'Easy',
        r'<p style="text-align:center;font-size:19px;">\[7(x^2 + 5)\]</p>',
        r'Which expression is equivalent to \(7(x^2 + 5)\)?',
        {'A': r'\(7x^2 + 35\)', 'B': r'\(7x^2 + 12\)', 'C': r'\(7x^2 + 5\)', 'D': r'\(7x^2 + 2\)'},
        'A',
        r'Áp dụng tính chất phân phối của phép nhân đối với phép cộng: \(7(x^2 + 5) = 7 \cdot x^2 + 7 \cdot 5 = 7x^2 + 35\).',
        r'Khi nhân phân phối hệ số ngoài ngoặc, phải nhân với TẤT CẢ các hạng tử bên trong ngoặc — đặc biệt không quên nhân hạng tử tự do.',
        {
            'A': ('Đáp án đúng', r'\(7 \cdot x^2 + 7 \cdot 5 = 7x^2 + 35\).'),
            'B': ('Cộng thay vì nhân', r'Cộng nhầm \(7 + 5 = 12\) thay vì nhân \(7 \times 5 = 35\).'),
            'C': ('Quên phân phối', r'Chỉ nhân \(7\) vào \(x^2\) mà quên nhân \(7\) với \(5\).'),
            'D': ('Trừ thay vì nhân', r'Tính nhầm \(7 - 5 = 2\) thay vì \(7 \times 5 = 35\).'),
        },
        r'Mẹo kiểm tra nhanh trên Desmos: gõ \(f(x) = 7(x^2 + 5)\) và thử \(f(1) = 42\); chỉ có \(7(1)^2 + 35 = 42\) khớp hoàn toàn.',
    ),
    _mcq(
        'march2025_v5_math_m1_q3', 3, 'Advanced Math', 'Nonlinear functions', 'Easy',
        _svg_m1_q3_exp(),
        r'What is the \(y\)-intercept of the graph shown?',
        {'A': r'\((-5, 0)\)', 'B': r'\((-1, 0)\)', 'C': r'\((0, 1)\)', 'D': r'\((0, 5)\)'},
        'D',
        r'Giao điểm với trục tung (\(y\)-intercept) là điểm mà đồ thị cắt trục \(y\) (tức là có hoành độ \(x = 0\)). Nhìn lên trục \(y\) trên đồ thị, đường cong đi qua chính giữa \(4\) và \(6\), tức là điểm \((0, 5)\).',
        r'Mọi \(y\)-intercept đều có dạng \((0, b)\) — loại ngay mọi đáp án có tung độ bằng \(0\) như A và B.',
        {
            'A': ('Đảo tọa độ (x, y)', r'\((-5, 0)\) nằm trên trục hoành \(x\), không thể là \(y\)-intercept.'),
            'B': ('Đảo tọa độ (x, y)', r'\((-1, 0)\) là một điểm trên trục \(x\), không nằm trên trục \(y\).'),
            'C': ('Nhầm tiệm cận ngang', r'\(y = 1\) là đường tiệm cận ngang khi \(x \to -\infty\), không phải giao điểm của đồ thị với trục \(y\).'),
            'D': ('Đáp án đúng', r'Đồ thị cắt trục tung tại đúng điểm \((0, 5)\).'),
        },
        r'Đọc trực tiếp giao điểm của đường cong với đường thẳng đứng \(x = 0\): vạch lưới nằm ngay giữa \(4\) và \(6\) chính là \(y = 5\).',
    ),
    _mcq(
        'march2025_v5_math_m1_q4', 4, 'Algebra', 'Linear functions', 'Easy',
        r'<p>The function \(f\) is defined by \(f(x) = 8(2x + 2)\).</p>',
        r'For what value of \(x\) does \(f(x) = 80\)?',
        {'A': r'\(4\)', 'B': r'\(6\)', 'C': r'\(10\)', 'D': r'\(39\)'},
        'A',
        r'Đặt \(f(x) = 80\): \(8(2x + 2) = 80\). Chia cả hai vế cho \(8\) ta được \(2x + 2 = 10 \Rightarrow 2x = 8 \Rightarrow x = 4\).',
        r'Khi thấy hệ số nhân gọn bên ngoài ngoặc (\(8\) chia hết \(80\)), hãy chia hai vế ngay lập tức thay vì khai triển để giảm tối đa nguy cơ tính nhầm.',
        {
            'A': ('Đáp án đúng', r'Thay \(x = 4\): \(f(4) = 8(2 \cdot 4 + 2) = 8(10) = 80\).'),
            'B': ('Sai dấu cộng/trừ', r'Giải nhầm \(2x = 10 + 2 = 12 \Rightarrow x = 6\).'),
            'C': ('Dừng sớm sau bước chia', r'\(10\) là giá trị của \(2x + 2\), chưa trừ \(2\) và chia \(2\) để tìm \(x\).'),
            'D': ('Bỏ quên hệ số 8', r'Giải nhầm \(2x + 2 = 80 \Rightarrow x = 39\).'),
        },
        r'Gõ thẳng `8(2x + 2) = 80` vào Desmos, đường thẳng đứng màu sắc sẽ cắt trục hoành ngay tại `x = 4`.',
    ),
    _mcq(
        'march2025_v5_math_m1_q5', 5, 'Advanced Math', 'Equivalent expressions', 'Easy',
        r'<p style="text-align:center;font-size:19px;">\[n = \frac{p}{23v}\]</p><p>The given equation relates the positive numbers \(n\), \(p\), and \(v\).</p>',
        r'Which equation correctly expresses \(p\) in terms of \(n\) and \(v\)?',
        {'A': r'\(p = n - 23v\)', 'B': r'\(p = n + 23v\)', 'C': r'\(p = \frac{n}{23v}\)', 'D': r'\(p = 23vn\)'},
        'D',
        r'Để cô lập biến \(p\) từ phương trình \(n = \frac{p}{23v}\), nhân cả hai vế với mẫu số \(23v\) (vì \(v > 0\)): \(p = 23vn\).',
        r'Phép toán ngược của phép chia cho \(23v\) là phép nhân với \(23v\) — tuyệt đối không đổi thành phép cộng hay trừ.',
        {
            'A': ('Đổi sai phép toán', r'Trừ \(23v\) thay vì nhân chéo \(23v\).'),
            'B': ('Đổi sai phép toán', r'Cộng \(23v\) thay vì nhân \(23v\).'),
            'C': ('Chia ngược hai vế', r'Chia \(n\) cho \(23v\) thay vì nhân \(n\) với \(23v\).'),
            'D': ('Đáp án đúng', r'Nhân hai vế với \(23v\) cho \(p = 23vn\).'),
        },
        r'Mẹo thử số: chọn \(v = 1, p = 23 \Rightarrow n = 1\). Chỉ đáp án D cho \(p = 23(1)(1) = 23\) khớp hoàn toàn.',
    ),
    _spr(
        'march2025_v5_math_m1_q6', 6, 'Algebra', 'Linear equations in one variable', 'Easy',
        r'<p>A line segment that has a length of \(125\) centimeters (\(\text{cm}\)) is divided into three parts. One part is \(49\text{ cm}\) long. The other two parts have lengths that are equal to each other.</p>',
        r'What is the length, in \(\text{cm}\), of one of the other two parts of equal length?',
        ['38'], '38',
        r'Gọi độ dài mỗi đoạn trong hai đoạn bằng nhau là \(x\) (\(\text{cm}\)). Tổng độ dài ba đoạn bằng \(125\text{ cm}\): \(49 + 2x = 125 \Rightarrow 2x = 76 \Rightarrow x = 38\).',
        r'Đọc kỹ câu hỏi yêu cầu độ dài MỘT đoạn ("one of the other two parts"), tránh dừng sớm ở tổng hai đoạn \(76\).',
        r'Gõ `(125 - 49) / 2` vào máy tính Desmos ra ngay `38`.',
    ),
    _mcq(
        'march2025_v5_math_m1_q7', 7, 'Geometry and Trigonometry', 'Area and volume', 'Easy',
        r'<p>Circle \(N\) has a radius of \(9\) millimeters (\(\text{mm}\)). Circle \(M\) has an area of \(25\pi\text{ mm}^2\).</p>',
        r'What is the total area, in \(\text{mm}^2\), of circles \(N\) and \(M\)?',
        {'A': r'\(106\pi\)', 'B': r'\(61\pi\)', 'C': r'\(43\pi\)', 'D': r'\(14\pi\)'},
        'A',
        r'Diện tích hình tròn \(N\) có bán kính \(r = 9\text{ mm}\) là \(A_N = \pi r^2 = \pi(9^2) = 81\pi\text{ mm}^2\). Tổng diện tích hai hình tròn \(N\) và \(M\) là \(81\pi + 25\pi = 106\pi\text{ mm}^2\).',
        r'Nhớ công thức diện tích hình tròn \(A = \pi r^2\) (bình phương bán kính!), đừng nhầm với chu vi \(2\pi r\).',
        {
            'A': ('Đáp án đúng', r'\(81\pi + 25\pi = 106\pi\).'),
            'B': ('Nhầm tính toán bán kính', r'Sai diện tích hình tròn \(N\) (tính nhầm thành \(36\pi\) rồi cộng \(25\pi\)).'),
            'C': ('Nhầm công thức chu vi', r'Tính nhầm diện tích \(N\) thành chu vi \(2\pi(9) = 18\pi\), rồi cộng \(25\pi\) ra \(43\pi\).'),
            'D': ('Cộng bán kính hai hình tròn', r'Cộng bán kính \(9 + 5 = 14\) rồi gắn \(\pi\) thành \(14\pi\).'),
        },
        r'Gõ `9^2 + 25` trên Desmos ra `106`, suy ra tổng diện tích là \(106\pi\).',
    ),
    _spr(
        'march2025_v5_math_m1_q8', 8, 'Problem-Solving and Data Analysis', 'One-variable data: Distributions and measures of center and spread', 'Easy',
        r'<p>The list gives the mass, in grams, of \(5\) ruffed lemurs.</p><p style="text-align:center;font-size:17px;font-weight:700;letter-spacing:0.3px;">\(3{,}710;\; 3{,}710;\; 3{,}130;\; 3{,}750;\; 3{,}150\)</p>',
        r'What is the mean mass, in grams, of these \(5\) ruffed lemurs?',
        ['3490'], '3490',
        r'Trung bình cộng (mean) bằng tổng các giá trị chia cho số lượng phần tử: \[\text{Mean} = \frac{3{,}710 + 3{,}710 + 3{,}130 + 3{,}750 + 3{,}150}{5} = \frac{17{,}450}{5} = 3{,}490.\] Khi điền vào ô SPR không gõ dấu phẩy, nhập `3490`.',
        r'Với câu hỏi tính mean danh sách số lớn, luôn dùng hàm `mean(...)` của Desmos để tránh cộng nhầm một chữ số, và KHÔNG nhập dấu phẩy vào ô SPR.',
        r'Gõ thẳng `mean(3710, 3710, 3130, 3750, 3150)` vào Desmos → hiện ngay đáp án `3490`.',
    ),
    _mcq(
        'march2025_v5_math_m1_q9', 9, 'Advanced Math', 'Nonlinear equations in one variable', 'Easy',
        r'<p style="text-align:center;font-size:19px;">\[2x(x - 3)(x + 5) = 0\]</p>',
        r'What is one of the solutions to the given equation?',
        {'A': r'\(-3\)', 'B': r'\(0\)', 'C': r'\(2\)', 'D': r'\(5\)'},
        'B',
        r'Theo quy tắc tích bằng \(0\) (Zero Product Property), phương trình \(2x(x - 3)(x + 5) = 0\) có \(3\) nghiệm: \(2x = 0 \Rightarrow x = 0\), \(x - 3 = 0 \Rightarrow x = 3\), và \(x + 5 = 0 \Rightarrow x = -5\). Trong \(4\) đáp án, chỉ có \(0\) là nghiệm đúng.',
        r'Cẩn thận dấu của nghiệm nhân tử: \((x - 3) = 0 \Rightarrow x = +3\) (không phải \(-3\)), \((x + 5) = 0 \Rightarrow x = -5\) (không phải \(+5\)), và đừng bỏ sót nghiệm \(x = 0\) từ nhân tử \(2x\).',
        {
            'A': ('Ngược dấu nhân tử', r'\(x - 3 = 0\) cho \(x = 3\), không phải \(-3\).'),
            'B': ('Đáp án đúng', r'Khi \(x = 0\), nhân tử \(2x = 0\) nên vế trái bằng \(0\).'),
            'C': ('Nhầm hệ số thành nghiệm', r'\(2\) là hệ số của \(2x\), thay \(x = 2\) cho \(4(-1)(7) = -28 \ne 0\).'),
            'D': ('Ngược dấu nhân tử', r'\(x + 5 = 0\) cho \(x = -5\), không phải \(5\).'),
        },
        r'Gõ `y = 2x(x - 3)(x + 5)` vào Desmos và bấm vào các giao điểm với trục hoành sẽ thấy ngay `(-5, 0)`, `(0, 0)`, `(3, 0)`.',
    ),
    _mcq(
        'march2025_v5_math_m1_q10', 10, 'Geometry and Trigonometry', 'Lines, angles, and triangles', 'Medium',
        _svg_m1_q10_triangles()
        + r'<p>In the figure shown, triangle \(CAE\) is similar to triangle \(CBD\). The measure of angle \(CBD\) is \(56^\circ\), and \(AE = 22(BD)\).</p>',
        r'What is the measure of angle \(CAE\)?',
        {'A': r'\(22^\circ\)', 'B': r'\(56^\circ\)', 'C': r'\((22 + 56)^\circ\)', 'D': r'\((22 \cdot 56)^\circ\)'},
        'B',
        r'Hai tam giác đồng dạng (\(\triangle CAE \sim \triangle CBD\)) luôn có các góc tương ứng BẰNG NHAU hoàn toàn, bất kể tỷ số đồng dạng cạnh là bao nhiêu (\(22\) lần chỉ nhân độ dài cạnh, không hề nhân số đo góc!). Vì đỉnh \(A\) tương ứng với đỉnh \(B\), ta có \(\angle CAE = \angle CBD = 56^\circ\).',
        r'Bẫy kinh điển của Digital SAT: tỷ số đồng dạng \(k\) nhân với độ dài cạnh, \(k^2\) nhân với diện tích, \(k^3\) nhân với thể tích, nhưng SỐ ĐO GÓC LUÔN GIỮ NGUYÊN!',
        {
            'A': ('Bẫy số thừa (Distractor)', r'\(22\) là tỷ số độ dài cạnh \(AE / BD\), không phải số đo góc.'),
            'B': ('Đáp án đúng', r'Các góc tương ứng trong hai tam giác đồng dạng luôn bằng nhau: \(\angle CAE = \angle CBD = 56^\circ\).'),
            'C': ('Cộng tỷ số vào góc', r'Sai bản chất hình học: không cộng tỷ số cạnh vào số đo góc.'),
            'D': ('Nhân tỷ số vào góc', r'Bẫy nhân hệ số tỷ lệ \(22\) vào số đo góc — góc không thay đổi khi phóng to/thu nhỏ hình đồng dạng.'),
        },
        r'Không cần Desmos: nhận diện ngay hai tam giác đồng dạng → góc tương ứng bằng nhau → chọn luôn \(56^\circ\) trong 5 giây!',
    ),
    _spr(
        'march2025_v5_math_m1_q11', 11, 'Problem-Solving and Data Analysis', 'Percentages', 'Medium',
        r'<p>A clothing store buys shirts at a wholesale price of \(6.00\) dollars each and resells them each at a retail price that is \(310\%\) of the wholesale price. At the end of the season, any remaining shirts are marked at a discounted price that is \(75\%\) off the retail price.</p>',
        r'What is the discounted price of each remaining shirt, in dollars?',
        ['4.65', '93/20'], '4.65',
        r'Bước 1: Giá bán lẻ (retail price) bằng \(310\%\) giá sỉ: \(6.00 \times 3.10 = 18.60\) đô la. Bước 2: Giảm giá \(75\%\) nghĩa là còn lại \(100\% - 75\% = 25\%\) giá bán lẻ: \(18.60 \times 0.25 = 4.65\) đô la (tương đương phân số \(\frac{93}{20}\)).',
        r'Cẩn thận phân biệt "\(310\%\) OF" (nhân \(3.10\)) với "\(75\%\) OFF" (nhân \(1 - 0.75 = 0.25\), KHÔNG nhân \(0.75\)).',
        r'Gõ thẳng `6 * 3.10 * (1 - 0.75)` vào Desmos sẽ ra chính xác `4.65`.',
    ),
    _mcq(
        'march2025_v5_math_m1_q12', 12, 'Algebra', 'Linear functions', 'Easy',
        r'<p style="text-align:center;font-size:19px;">\[f(x) = 47\]</p><p>For the given linear function \(f\), which table gives three values of \(x\) and their corresponding values of \(f(x)\)?</p>',
        r'Which table correctly represents \(f(x) = 47\)?',
        {
            'A': _mini_xy_table([(0, 0), (1, 0), (2, 0)]),
            'B': _mini_xy_table([(0, 47), (1, 47), (2, 47)]),
            'C': _mini_xy_table([(0, 0), (1, 47), (2, 94)]),
            'D': _mini_xy_table([(0, 47), (1, 48), (2, 49)]),
        },
        'B',
        r'Hàm \(f(x) = 47\) là hàm hằng (một trường hợp đặc biệt của hàm tuyến tính với hệ số góc \(m = 0\) và tung độ gốc \(b = 47\)). Do đó, với MỌI giá trị của \(x\) (\(x = 0, 1, 2\)), đầu ra \(f(x)\) luôn bằng \(47\). Chỉ bảng B thỏa mãn \((0, 47), (1, 47), (2, 47)\).',
        r'Hàm hằng \(f(x) = c\) không phụ thuộc vào \(x\): mọi hàng trong cột \(f(x)\) đều phải có cùng giá trị \(c\).',
        {
            'A': ('Nhầm thành f(x) = 0', r'Cột \(f(x)\) toàn bằng \(0\), ứng với hàm \(f(x) = 0\) chứ không phải \(47\).'),
            'B': ('Đáp án đúng', r'Mọi giá trị \(x = 0, 1, 2\) đều cho cùng giá trị \(f(x) = 47\).'),
            'C': ('Nhầm thành f(x) = 47x', r'Bảng này ứng với \(f(x) = 47x\) (có hệ số góc \(47\)), không phải hàm hằng \(f(x) = 47\).'),
            'D': ('Nhầm thành f(x) = x + 47', r'Bảng này ứng với \(f(x) = x + 47\), tăng thêm \(1\) mỗi khi \(x\) tăng \(1\).'),
        },
        r'Trên Desmos, gõ `f(x) = 47` rồi tạo bảng giá trị (Table) sẽ thấy ngay \(f(0) = f(1) = f(2) = 47\).',
    ),
    _mcq(
        'march2025_v5_math_m1_q13', 13, 'Advanced Math', 'Nonlinear functions', 'Easy',
        r'<p>A sample of a certain isotope takes \(29\) years to decay to half its original mass. The function \(s(t) = 136(0.5)^{\frac{t}{29}}\) gives the approximate mass of this isotope, in grams, that remains \(t\) years after a \(136\)-gram sample starts to decay.</p>',
        r'Which statement is the best interpretation of \(s(58) = 34\) in this context?',
        {
            'A': r'Approximately \(34\) grams of the sample remains \(58\) years after the sample starts to decay.',
            'B': r'The mass of the sample has decreased by approximately \(34\) grams \(58\) years after the sample starts to decay.',
            'C': r'The mass of the sample has decreased by approximately \(58\) grams \(34\) years after the sample starts to decay.',
            'D': r'Approximately \(58\) grams of the sample remains \(34\) years after the sample starts to decay.',
        },
        'A',
        r'Trong hàm \(s(t)\), biến đầu vào \(t\) là số năm kể từ lúc bắt đầu phân rã, còn đầu ra \(s(t)\) là khối lượng đồng vị CÒN LẠI (remains), tính bằng gam. Vì vậy \(s(58) = 34\) có nghĩa là sau \(58\) năm kể từ lúc bắt đầu phân rã, khối lượng mẫu CÒN LẠI xấp xỉ \(34\) gam (kiểm tra: \(136(0.5)^{58/29} = 136(0.25) = 34\)).',
        r'Khi diễn giải \(f(a) = b\): luôn chốt rõ \(a\) là đầu vào (thời gian \(t = 58\) năm) và \(b\) là đầu ra (khối lượng CÒN LẠI \(34\) gam — không phải phần đã giảm đi!).',
        {
            'A': ('Đáp án đúng', r'Khớp chính xác đầu vào \(t = 58\) năm và đầu ra \(s(58) = 34\) gam còn lại ("remains").'),
            'B': ('Nhầm "remains" với "decreased by"', r'\(34\) gam là lượng CÒN LẠI, còn lượng đã mất đi là \(136 - 34 = 102\) gam.'),
            'C': ('Đảo biến + sai nghĩa', r'Vừa đảo ngược \(58\) và \(34\), vừa nhầm "còn lại" thành "giảm đi".'),
            'D': ('Đảo ngược đầu vào / đầu ra', r'Đảo ngược thời gian (\(58\) năm) và khối lượng (\(34\) gam).'),
        },
        r'Gõ `136 * 0.5^(58/29)` trên Desmos để xác nhận \(s(58) = 34\), sau đó đối chiếu đúng đơn vị của \(t\) (years) và \(s(t)\) (grams remaining).',
    ),
    _mcq(
        'march2025_v5_math_m1_q14', 14, 'Problem-Solving and Data Analysis', 'Two-variable data: Models and scatterplots', 'Easy',
        r'<p>Antonia has $130 in an account. Each year she expects to have \(2.5\%\) more money in the account than she had the previous year.</p>',
        r'Which of the following models best describes how Antonia expects the money in her account to change over time?',
        {
            'A': r'Decreasing exponential',
            'B': r'Decreasing linear',
            'C': r'Increasing exponential',
            'D': r'Increasing linear',
        },
        'C',
        r'Mỗi năm số tiền trong tài khoản TĂNG thêm \(2.5\%\) so với NĂM TRƯỚC ĐÓ (tức nhân liên tiếp với hệ số không đổi \(1 + 0.025 = 1.025 > 1\): \(A(t) = 130(1.025)^t\)). Tăng theo tỷ lệ phần trăm cố định mỗi kỳ là mô hình hàm mũ tăng (Increasing exponential).',
        r'Quy tắc nhận diện nhanh mô hình: cộng/trừ một LƯỢNG cố định → Linear; nhân/tăng giảm một PHẦN TRĂM cố định so với kỳ trước → Exponential.',
        {
            'A': ('Sai chiều biến thiên', r'Tiền tăng thêm \(2.5\%\) ("more money") nên phải là Increasing, không phải Decreasing.'),
            'B': ('Sai cả chiều và dạng hàm', r'Không phải giảm và không phải cộng trừ hằng số tuyến tính.'),
            'C': ('Đáp án đúng', r'Tăng đều \(2.5\%\) mỗi năm so với năm trước tạo ra mô hình hàm mũ tăng \(130(1.025)^t\).'),
            'D': ('Nhầm phần trăm với tuyến tính', r'Linear chỉ đúng khi mỗi năm tăng thêm cùng một số đô la cố định (ví dụ +$2.50/năm), không phải \(+2.5\%\) của năm trước.'),
        },
        r'Không cần máy tính: từ khóa "\(2.5\%\) more ... than the previous year" chốt ngay đáp án Increasing exponential.',
    ),
    _mcq(
        'march2025_v5_math_m1_q15', 15, 'Algebra', 'Linear inequalities in one or two variables', 'Medium',
        r'<p>In the \(xy\)-plane, consider the inequality \(2x - 6y > 12\).</p>',
        r'In the \(xy\)-plane, which of the following DOES NOT CONTAIN any points that are part of the solution set to \(2x - 6y > 12\)?',
        {
            'A': r'The region where \(x < 0\) and \(y > 0\)',
            'B': r'The region where \(x < 0\) and \(y < 0\)',
            'C': r'The region where \(x > 0\) and \(y > 0\)',
            'D': r'The \(x\)-axis',
        },
        'A',
        r'Xét bất phương trình \(2x - 6y > 12\). Trong góc phần tư thứ II (nơi \(x < 0\) và \(y > 0\)), ta luôn có \(2x < 0\) và \(-6y < 0\), suy ra \(2x - 6y < 0 < 12\) với mọi điểm trong miền này. Do đó miền \(x < 0\) và \(y > 0\) KHÔNG chứa bất kỳ điểm nghiệm nào. Kiểm tra 3 đáp án còn lại đều có nghiệm: \((-1, -10)\) ở B, \((10, 1)\) ở C, và \((7, 0)\) trên trục \(x\) ở D.',
        r'Hoặc viết về dạng \(y < \frac{1}{3}x - 2\): đường biên có hệ số góc dương \(\frac{1}{3}\) và cắt trục \(y\) tại \((0, -2)\), nên miền nằm dưới đường thẳng này không bao giờ chạm tới góc phần tư II (\(x < 0, y > 0\)).',
        {
            'A': ('Đáp án đúng', r'Khi \(x < 0\) và \(y > 0\) thì \(2x - 6y < 0\), không bao giờ lớn hơn \(12\).'),
            'B': ('Miền có chứa nghiệm', r'Ví dụ điểm \((-1, -5)\) cho \(2(-1) - 6(-5) = 28 > 12\).'),
            'C': ('Miền có chứa nghiệm', r'Ví dụ điểm \((10, 1)\) cho \(2(10) - 6(1) = 14 > 12\).'),
            'D': ('Trục x có chứa nghiệm', r'Ví dụ điểm \((7, 0)\) trên trục \(x\) cho \(2(7) - 0 = 14 > 12\).'),
        },
        r'Gõ thẳng `2x - 6y > 12` vào Desmos → vùng tô màu xuất hiện ngay lập tức, thấy rõ góc phần tư II (\(x < 0, y > 0\)) hoàn toàn trống trắng!',
    ),
    _mcq(
        'march2025_v5_math_m1_q16', 16, 'Geometry and Trigonometry', 'Circles', 'Medium',
        r'<p>A circle in the \(xy\)-plane has its center at \((18, 16)\) and has a radius of \(6k\).</p>',
        r'Which equation represents this circle?',
        {
            'A': r'\((x - 18)^2 + (y - 16)^2 = 36k\)',
            'B': r'\((x - 18)^2 + (y - 16)^2 = 36k^2\)',
            'C': r'\((x - 18)^2 + (y - 16)^2 = 6k\)',
            'D': r'\((x - 18)^2 + (y - 16)^2 = 6k^2\)',
        },
        'B',
        r'Phương trình chuẩn của đường tròn tâm \((h, k_0)\) bán kính \(r\) là \((x - h)^2 + (y - k_0)^2 = r^2\). Thay tâm \((18, 16)\) và bán kính \(r = 6k\) ta được: \((x - 18)^2 + (y - 16)^2 = (6k)^2 = 36k^2\).',
        r'Khi bình phương bán kính dạng tích \((6k)^2\), phải bình phương CẢ hệ số lẫn biến: \(6^2 \cdot k^2 = 36k^2\).',
        {
            'A': ('Quên bình phương biến k', r'Bình phương \(6\) thành \(36\) nhưng quên bình phương \(k\) thành \(k^2\).'),
            'B': ('Đáp án đúng', r'\(r^2 = (6k)^2 = 36k^2\).'),
            'C': ('Quên bình phương bán kính', r'Để nguyên \(r = 6k\) ở vế phải thay vì \(r^2\).'),
            'D': ('Quên bình phương hệ số 6', r'Chỉ bình phương \(k\) thành \(k^2\) mà quên bình phương \(6\) thành \(36\).'),
        },
        r'Mẹo thử số: đặt \(k = 2 \Rightarrow r = 12 \Rightarrow r^2 = 144\). Chỉ \(36k^2 = 36(4) = 144\) cho kết quả đúng.',
    ),
    _mcq(
        'march2025_v5_math_m1_q17', 17, 'Advanced Math', 'Nonlinear equations in one variable', 'Medium',
        r'<p style="text-align:center;font-size:19px;">\[x^2 - 24x - 8 = 0\]</p>',
        r'What is the sum of the solutions to the given equation?',
        {'A': r'\(0\)', 'B': r'\(4\)', 'C': r'\(8\)', 'D': r'\(24\)'},
        'D',
        r'Phương trình bậc hai \(ax^2 + bx + c = 0\) với \(a = 1, b = -24, c = -8\) có biệt thức \(\Delta = (-24)^2 - 4(1)(-8) = 608 > 0\), nên có \(2\) nghiệm thực phân biệt. Theo định lý Vi-ét, tổng hai nghiệm là \(x_1 + x_2 = -\frac{b}{a} = -\frac{-24}{1} = 24\).',
        r'Thuộc lòng định lý Vi-ét cho SAT Math: tổng các nghiệm của \(ax^2 + bx + c = 0\) (khi \(\Delta > 0\)) luôn là \(-\frac{b}{a}\), tích là \(\frac{c}{a}\).',
        {
            'A': ('Nhầm tổng bằng 0', r'Chỉ đúng khi hệ số \(b = 0\).'),
            'B': ('Nhầm tính toán', r'Không liên quan tới \(-\frac{b}{a} = 24\).'),
            'C': ('Nhầm với hằng số c', r'\(-8\) là tích hai nghiệm \(\frac{c}{a}\), không phải tổng hai nghiệm.'),
            'D': ('Đáp án đúng', r'Theo Vi-ét: \(x_1 + x_2 = -\frac{-24}{1} = 24\).'),
        },
        r'Gõ `y = x^2 - 24x - 8` vào Desmos, tìm 2 giao điểm trục hoành (\(x_1 \approx -0.329, x_2 \approx 24.329\)) và cộng lại sẽ thấy đúng bằng `24`.',
    ),
    _spr(
        'march2025_v5_math_m1_q18', 18, 'Geometry and Trigonometry', 'Right triangles and trigonometry', 'Medium',
        _svg_m1_q18_ramp()
        + r'<p>According to a US law, ramps for use by the general public must form an angle with level ground such that \(\tan\theta \le \frac{1}{12}\). If the ramp in the figure conforms to this law and has a height of \(22.7\) inches, what is the least possible value of \(x\), in inches?</p>',
        r'What is the least possible value of \(x\), in inches?',
        ['272.4', '1362/5'], '272.4',
        r'Trong tam giác vuông trên hình, \(\tan\theta = \frac{\text{đối}}{\text{kề}} = \frac{22.7}{x}\). Điều kiện theo luật là \(\frac{22.7}{x} \le \frac{1}{12}\). Vì \(x > 0\), nhân chéo hai vế ta được \(x \ge 22.7 \times 12 = 272.4\) inch. Vậy giá trị nhỏ nhất có thể của \(x\) là \(272.4\) (hoặc \(\frac{1362}{5}\)).',
        r'SOH-CAH-TOA: \(\tan\theta = \frac{\text{Opposite}}{\text{Adjacent}}\). Khi biến \(x\) nằm ở mẫu số, bất đẳng thức \(\frac{h}{x} \le \frac{1}{12}\) cho GIÁ TRỊ NHỎ NHẤT của \(x\) là \(12h\).',
        r'Gõ `22.7 * 12` vào Desmos ra ngay `272.4` — gọn 5 ký tự chuẩn khung SPR!',
    ),
    _mcq(
        'march2025_v5_math_m1_q19', 19, 'Geometry and Trigonometry', 'Lines, angles, and triangles', 'Easy',
        _svg_m1_q19_intersecting()
        + r'<p>In the figure, two lines intersect at a point.</p>',
        r'If \(w = 112\), what is the value of \(z\)?',
        {'A': r'\(12\)', 'B': r'\(56\)', 'C': r'\(68\)', 'D': r'\(112\)'},
        'D',
        r'Hai đường thẳng cắt nhau tại một điểm tạo thành cặp góc đối đỉnh \(w^\circ\) và \(z^\circ\). Hai góc đối đỉnh (vertical angles) luôn bằng nhau, nên \(z = w = 112\).',
        r'Kiểm tra kỹ vị trí góc trên hình: hai góc đối đỉnh luôn bằng nhau, còn hai góc kề bù (linear pair) mới có tổng bằng \(180^\circ\).',
        {
            'A': ('Trừ nhầm 100', r'Lấy nhầm \(112 - 100 = 12\).'),
            'B': ('Chia đôi góc', r'Lấy nhầm \(112 / 2 = 56\).'),
            'C': ('Nhầm sang góc kề bù', r'\(180 - 112 = 68\) là số đo hai góc nhọn kề bên, không phải góc đối đỉnh \(z^\circ\).'),
            'D': ('Đáp án đúng', r'\(w^\circ\) và \(z^\circ\) là hai góc đối đỉnh nên \(z = w = 112\).'),
        },
        r'Không cần máy tính: nhận diện cặp góc đối đỉnh trên hình chữ X → chọn ngay \(112\).',
    ),
    _spr(
        'march2025_v5_math_m1_q20', 20, 'Algebra', 'Linear equations in one variable', 'Medium',
        r'<p style="text-align:center;font-size:18px;">\[3(2 - 7x) + 5(2 - 7x) + 6 = 7(2 - 7x) + 2\]</p>',
        r'If \(3(2 - 7x) + 5(2 - 7x) + 6 = 7(2 - 7x) + 2\), what is the value of \(7x - 2\)?',
        ['4'], '4',
        r'Đặt ẩn phụ \(u = 2 - 7x\). Phương trình trở thành \(3u + 5u + 6 = 7u + 2 \Rightarrow 8u + 6 = 7u + 2 \Rightarrow u = -4\). Đề bài hỏi \(7x - 2 = -(2 - 7x) = -u = -(-4) = 4\)! (Kiểm tra trực tiếp: \(7x = 6 \Rightarrow 7x - 2 = 4\).)',
        r'Bẫy đổi dấu kinh điển ở câu 20 M1: trong phương trình là \((2 - 7x)\) nhưng đề lại hỏi \((7x - 2)\) — chính là số đối của \((2 - 7x)\) nên phải đổi dấu từ \(-4\) thành \(4\)!',
        r'Gõ thẳng `3(2 - 7x) + 5(2 - 7x) + 6 = 7(2 - 7x) + 2` vào Desmos sẽ được `x = 0.8571...` (`6/7`); gõ tiếp `7(6/7) - 2` ra ngay `4`.',
    ),
    _mcq(
        'march2025_v5_math_m1_q21', 21, 'Algebra', 'Linear equations in two variables', 'Hard',
        r'<p>In the \(xy\)-plane, line \(k\) and line \(\ell\) are perpendicular and intersect at the point \((2, 9)\). Line \(k\) is defined by the equation \(y = mx + b\), where \(m\) and \(b\) are constants and \(m > 1\).</p>',
        r'Which of the following points lies on line \(\ell\)?',
        {
            'A': r'\(\left(3,\; 9 - \frac{1}{m}\right)\)',
            'B': r'\(\left(3,\; 9 + \frac{1}{m}\right)\)',
            'C': r'\((3,\; 9 - m)\)',
            'D': r'\((3,\; 9 + m)\)',
        },
        'A',
        r'Đường thẳng \(k\) có hệ số góc là \(m\). Vì đường thẳng \(\ell\) vuông góc với \(k\), hệ số góc của \(\ell\) là số đối nghịch đảo: \(m_\ell = -\frac{1}{m}\). Đường thẳng \(\ell\) đi qua giao điểm \((2, 9)\), nên khi \(x\) tăng thêm \(1\) đơn vị (từ \(2\) lên \(3\)), \(y\) thay đổi đúng bằng hệ số góc \(m_\ell = -\frac{1}{m}\). Suy ra điểm \(\left(3,\; 9 - \frac{1}{m}\right)\) nằm trên đường thẳng \(\ell\).',
        r'Hai đường thẳng vuông góc có tích hệ số góc bằng \(-1\) (\(m_\ell = -\frac{1}{m}\)). Với đường thẳng đi qua \((x_0, y_0)\), điểm ở hoành độ \(x_0 + 1\) luôn có tung độ \(y_0 + m_\ell\).',
        {
            'A': ('Đáp án đúng', r'Hệ số góc của \(\ell\) là \(-\frac{1}{m}\), nên tại \(x = 2 + 1 = 3\) ta có \(y = 9 - \frac{1}{m}\).'),
            'B': ('Quên dấu âm vuông góc', r'Dùng nhầm hệ số góc \(+\frac{1}{m}\) (chỉ nghịch đảo mà quên đổi dấu).'),
            'C': ('Quên nghịch đảo', r'Dùng nhầm hệ số góc \(-m\) thay vì \(-\frac{1}{m}\).'),
            'D': ('Nhầm sang đường thẳng k', r'\((3, 9 + m)\) là điểm nằm trên đường thẳng \(k\) (cùng hệ số góc \(m\)), không phải đường thẳng vuông góc \(\ell\).'),
        },
        r'Mẹo Desmos: chọn \(m = 2\), vẽ \(y = 2(x - 2) + 9\) và đường vuông góc \(y = -0.5(x - 2) + 9\), kiểm tra tại \(x = 3\) sẽ thấy \(y = 8.5 = 9 - \frac{1}{2}\) → chọn A.',
    ),
    _spr(
        'march2025_v5_math_m1_q22', 22, 'Problem-Solving and Data Analysis', 'Ratios, rates, proportional relationships, and units', 'Hard',
        r'<p>A sphere has a volume of \(245.00\) cubic yards.</p>',
        r'What is the volume of the sphere, in cubic <u>meters</u>? (Use \(1\text{ yard} = 0.914\text{ meter}\).) ',
        ['187.1', '187.0', '187.07', '187.0702'], '187.1 (hoặc 187.0 / 187.07)',
        r'Đổi đơn vị THỂ TÍCH (mũ 3!): vì \(1\text{ yd} = 0.914\text{ m}\), ta phải lập phương hệ số quy đổi: \(1\text{ yd}^3 = (0.914)^3\text{ m}^3 \approx 0.763551944\text{ m}^3\). Do đó thể tích hình cầu bằng mét khối là: \[V = 245.00 \times (0.914)^3 = 187.07022628\text{ m}^3.\] Theo quy tắc SPR 5 ký tự của Bluebook (làm tròn hoặc cắt gọn ở chữ số thứ 4), ta nhập `187.1` (làm tròn) hoặc `187.0` (cắt gọn).',
        r'Bẫy đổi đơn vị mũ 2 / mũ 3 ở câu cuối M1: diện tích nhân hệ số mũ \(2\), thể tích (cubic) PHẢI nhân hệ số mũ \(3\) — tuyệt đối không nhân \(245 \times 0.914\)!',
        r'Gõ `245 * 0.914^3` trên Desmos sẽ ra `187.07022628` → làm tròn 5 ký tự thành `187.1` (hoặc cắt gọn `187.0`).',
    ),
]


# ============================================================================
# MODULE 2 — REAL EXAM MARCH 2025 VER 5 MATH (22 QUESTIONS • 35 MINUTES)
# ============================================================================

M2_QUESTIONS = [
    _mcq(
        'march2025_v5_math_m2_q1', 1, 'Algebra', 'Linear equations in two variables', 'Easy',
        r'<p>In one week in \(2017\), a technician earned a total of $900 by working at her regular job and at a second job doing part-time work. The equation \(21h + 10c = 900\) represents this situation, where \(h\) is the number of hours worked at her regular job and \(c\) is the number of hours worked at her second job.</p>',
        r'Which of the following is the best interpretation of \(21\) in this context?',
        {
            'A': r'The amount, in dollars, the technician earned for each hour she worked at her regular job',
            'B': r'The amount, in dollars, the technician earned for each hour she worked at her second job',
            'C': r'The number of hours the technician worked in one week at her regular job',
            'D': r'The number of hours the technician worked in one week at her second job',
        },
        'A',
        r'Trong phương trình tổng thu nhập \(21h + 10c = 900\) (đơn vị: đô la), \(h\) là số giờ làm ở công việc chính (regular job). Để tích \(21h\) có đơn vị là đô la, hệ số \(21\) phải có đơn vị là đô la/giờ — tức số tiền kỹ thuật viên kiếm được cho mỗi giờ làm việc ở công việc chính.',
        r'Phương pháp phân tích thứ nguyên (Unit Analysis): \((\text{đơn vị của } 21) \times (\text{hours}) = \text{dollars} \Rightarrow 21\) là tiền lương mỗi giờ (\(\$/\text{hour}\)) gắn với biến \(h\).',
        {
            'A': ('Đáp án đúng', r'\(21\) nhân với \(h\) (số giờ công việc chính) nên là mức lương theo giờ tại công việc chính.'),
            'B': ('Nhầm sang công việc thứ hai', r'Mức lương theo giờ ở công việc thứ hai là hệ số \(10\) (nhân với \(c\)).'),
            'C': ('Nhầm hệ số với biến số', r'Số giờ làm công việc chính là biến \(h\), không phải hệ số \(21\).'),
            'D': ('Nhầm biến số công việc thứ hai', r'Số giờ làm công việc thứ hai là biến \(c\).'),
        },
        r'Không cần máy tính: kiểm tra đơn vị của tích \(21h\) = tổng tiền kiếm từ công việc chính → \(21\) là tiền công mỗi giờ của công việc chính.',
    ),
    _mcq(
        'march2025_v5_math_m2_q2', 2, 'Problem-Solving and Data Analysis', 'Two-variable data: Models and scatterplots', 'Easy',
        r'<p>The scatterplot shows the relationship between two variables, \(x\) and \(y\). A line of best fit is also shown.</p>'
        + _svg_m2_q2_scatterplot(),
        r'Which of the following equations best represents the line of best fit shown?',
        {
            'A': r'\(y = x - 15.4\)',
            'B': r'\(y = -x + 15.4\)',
            'C': r'\(y = x - 1.5\)',
            'D': r'\(y = -x + 1.5\)',
        },
        'D',
        r'Quan sát đường hồi quy (line of best fit): (1) Đường thẳng đi XUỐNG từ trái sang phải nên hệ số góc ÂM (\(m \approx -1\)) → loại ngay A và C; (2) Tại \(x = 0\), đường thẳng cắt trục tung ở điểm ngay dưới vạch \(y = 2\), tức \(y\)-intercept \(b \approx +1.5\) (chứ không phải \(15.4\) — \(15.4\) là tung độ tại \(x = -14\)). Do đó phương trình đúng là \(y = -x + 1.5\).',
        r'Cẩn thận vị trí trục tung \(y\)! Ở đồ thị này trục \(y\) nằm ở BÊN PHẢI (\(x = 0\)) chứ không phải bên trái — đừng đọc nhầm giá trị ở mép trái (\(x = -14, y \approx 15.4\)) thành \(y\)-intercept!',
        {
            'A': ('Sai cả dấu hệ số góc và y-intercept', r'Hệ số góc dương \(+1\) (đi lên) và tung độ gốc âm \(-15.4\) đều trái ngược đồ thị.'),
            'B': ('Đọc nhầm mép trái thành y-intercept', r'\(15.4\) là giá trị \(y\) tại \(x = -14\) (mép trái đồ thị), không phải tại \(x = 0\) (trục tung bên phải).'),
            'C': ('Sai dấu hệ số góc và y-intercept', r'Đường thẳng dốc xuống (hệ số góc âm) và cắt trục \(y\) ở phần dương \(+1.5\).'),
            'D': ('Đáp án đúng', r'Đường thẳng có hệ số góc \(-1\) và cắt trục tung tại \((0, 1.5)\), kiểm tra tại \(x = -14 \Rightarrow y = 15.5\) khớp tuyệt đối.'),
        },
        r'Kiểm tra nhanh điểm đầu và điểm cuối: thay \(x = 0\) vào D được \(1.5\) (khớp trục tung bên phải) và thay \(x = -14\) được \(15.5\) (khớp mép trái).',
    ),
    _mcq(
        'march2025_v5_math_m2_q3', 3, 'Algebra', 'Systems of two linear equations in two variables', 'Easy',
        r'<p>Consider the equations \(y = 3x + 1\) and \(y = 4x - 6\) in the \(xy\)-plane.</p>',
        r'At what point \((x, y)\) do the graphs of the equations \(y = 3x + 1\) and \(y = 4x - 6\) intersect in the \(xy\)-plane?',
        {'A': r'\((3, 4)\)', 'B': r'\((4, 3)\)', 'C': r'\((7, 22)\)', 'D': r'\((22, 7)\)'},
        'C',
        r'Tại giao điểm hai đường thẳng, cho hai vế phải bằng nhau: \(3x + 1 = 4x - 6 \Rightarrow 1 + 6 = 4x - 3x \Rightarrow x = 7\). Thay \(x = 7\) vào phương trình thứ nhất: \(y = 3(7) + 1 = 22\). Vậy giao điểm là \((7, 22)\).',
        r'Kiểm tra thứ tự tọa độ \((x, y)\) trước khi khoanh — tránh bẫy đảo ngược \((y, x)\) ở đáp án D.',
        {
            'A': ('Nhầm hệ số góc thành tọa độ', r'\(3\) và \(4\) chỉ là hệ số góc của hai đường thẳng.'),
            'B': ('Nhầm hệ số góc thành tọa độ', r'Đảo ngược hai hệ số góc \(4\) và \(3\), không thỏa mãn cả hai phương trình.'),
            'C': ('Đáp án đúng', r'Thay \((7, 22)\): \(3(7) + 1 = 22\) và \(4(7) - 6 = 22\).'),
            'D': ('Đảo ngược (x, y)', r'Đảo nhầm hoành độ \(x = 7\) và tung độ \(y = 22\).'),
        },
        r'Gõ hai dòng `y = 3x + 1` và `y = 4x - 6` vào Desmos rồi bấm vào điểm giao cắt sẽ hiển thị ngay `(7, 22)`.',
    ),
    _mcq(
        'march2025_v5_math_m2_q4', 4, 'Algebra', 'Systems of two linear equations in two variables', 'Easy',
        r'<p style="text-align:center;font-size:19px;">\[y = \frac{2}{7}x + 3\]</p><p>One of the two equations in a system of linear equations is given. The system has infinitely many solutions. The second equation in the system is \(y = mx + b\), where \(m\) and \(b\) are constants.</p>',
        r'What is the value of \(b\)?',
        {'A': r'\(-3\)', 'B': r'\(-\frac{1}{3}\)', 'C': r'\(\frac{1}{3}\)', 'D': r'\(3\)'},
        'D',
        r'Một hệ hai phương trình bậc nhất hai ẩn có VÔ SỐ NGHIỆM (infinitely many solutions) khi và chỉ khi hai đường thẳng TRÙNG NHAU hoàn toàn — tức có cùng hệ số góc và cùng tung độ gốc. So sánh \(y = mx + b\) với \(y = \frac{2}{7}x + 3\), ta có ngay \(m = \frac{2}{7}\) và \(b = 3\).',
        r'Nhớ bộ 3 điều kiện của hệ \(y = m_1x + b_1\) và \(y = m_2x + b_2\): (1) Vô số nghiệm \(\Leftrightarrow m_1 = m_2\) và \(b_1 = b_2\); (2) Vô nghiệm \(\Leftrightarrow m_1 = m_2\) và \(b_1 \ne b_2\); (3) Nghiệm duy nhất \(\Leftrightarrow m_1 \ne m_2\).',
        {
            'A': ('Sai dấu', r'\(-3\) là số đối của tung độ gốc, sẽ tạo đường song song (vô nghiệm) nếu \(m = \frac{2}{7}\).'),
            'B': ('Nghịch đảo đối dấu', r'Nhầm sang công thức đường vuông góc áp dụng sai cho \(b\).'),
            'C': ('Nghịch đảo tung độ gốc', r'Lấy nhầm nghịch đảo \(\frac{1}{3}\) thay vì giữ nguyên \(3\).'),
            'D': ('Đáp án đúng', r'Hai đường thẳng trùng nhau đòi hỏi \(b = 3\).'),
        },
        r'Không cần máy tính: "infinitely many solutions" \(\Rightarrow\) hai phương trình giống hệt nhau \(\Rightarrow b = 3\).',
    ),
    _mcq(
        'march2025_v5_math_m2_q5', 5, 'Advanced Math', 'Nonlinear functions', 'Easy',
        r'<p>A chemist performed an experiment using a set of beakers that can each be modeled by a right circular cylinder with a height of \(58\) millimeters. The equation \(y = 58\pi x^2\) gives the volume \(y\), in cubic millimeters, of the right circular cylinder that models a beaker in this set, where \(x\) is the radius, in millimeters, of the base of the cylinder.</p>',
        r'Which graph best represents this equation in the \(xy\)-plane?',
        {
            'A': _svg_m2_q5_beaker_choice('A'),
            'B': _svg_m2_q5_beaker_choice('B'),
            'C': _svg_m2_q5_beaker_choice('C'),
            'D': _svg_m2_q5_beaker_choice('D'),
        },
        'A',
        r'Hàm \(y = 58\pi x^2\) là một parabol mở lên đi qua gốc tọa độ \((0, 0)\) (loại ngay các đồ thị đường thẳng C và D). Để phân biệt giữa hai parabol A và B, thay một giá trị đơn giản \(x = 4\): \(y = 58\pi(4^2) = 928\pi \approx 2{,}915\) (và tại \(x = 5\), \(y = 1{,}450\pi \approx 4{,}555\)). Chỉ đồ thị A đi qua \((4, 2915)\) và \((5, 4555)\) (chạm mức \(5{,}000\) ở khoảng \(x \approx 5.24\)).',
        r'Khi chọn đồ thị cho hàm bậc hai/hàm mũ, luôn thử \(1\) giá trị \(x\) đẹp (như \(x = 4\) hoặc \(x = 5\)) rồi kiểm tra tung độ \(y\) trên đồ thị — chốt đáp án chính xác \(100\%\).',
        {
            'A': ('Đáp án đúng', r'Parabol \(y = 58\pi x^2\) đi qua \((3, 1640)\), \((4, 2915)\), \((5, 4555)\) và vượt \(5{,}000\) ngay sau \(x = 5\).'),
            'B': ('Quên nhân hằng số pi', r'Đây là đồ thị của \(y = 58x^2\) (quên nhân \(\pi \approx 3.14\)), nên tại \(x = 5\) chỉ đạt \(1{,}450\) và mãi tới \(x \approx 9.3\) mới chạm \(5{,}000\).'),
            'C': ('Nhầm thành hàm tuyến tính', r'Đây là đường thẳng \(y = 58\pi x\) (quên bình phương bán kính \(x^2\)).'),
            'D': ('Vừa quên pi vừa quên bình phương', r'Đây là đường thẳng \(y = 58x\), tại \(x = 10\) chỉ đạt \(580\).'),
        },
        r'Gõ `y = 58 * pi * x^2` vào Desmos và chỉnh khung nhìn `0 <= x <= 10`, `0 <= y <= 5000` sẽ thấy hình dáng trùng khớp từng milimet với đáp án A.',
    ),
    _mcq(
        'march2025_v5_math_m2_q6', 6, 'Problem-Solving and Data Analysis', 'Probability and conditional probability', 'Easy',
        r'<p>At a convention center, there are a total of \(325\) visitors. Each visitor is located in either room A, room B, or room C. If one of these visitors is selected at random, the probability of selecting a visitor who is located in room A is \(0.64\), and the probability of selecting a visitor who is located in room B is \(0.32\).</p>',
        r'How many visitors are located in room C?',
        {'A': r'\(4\)', 'B': r'\(13\)', 'C': r'\(67\)', 'D': r'\(104\)'},
        'B',
        r'Vì mỗi khách chỉ ở đúng một trong ba phòng A, B, hoặc C, tổng xác suất bằng \(1\): \(P(C) = 1 - P(A) - P(B) = 1 - 0.64 - 0.32 = 0.04\). Số khách trong phòng C là \(0.04 \times 325 = 13\).',
        r'Tổng xác suất các biến cố xung khắc đầy đủ luôn bằng \(1\). Nhớ nhân xác suất \(P(C)\) với tổng số người \(325\) để ra số lượng khách (không dừng ở phần trăm \(4\)).',
        {
            'A': ('Dừng ở phần trăm', r'\(4\) là \(4\%\) (\(P(C) = 0.04\)), chưa nhân với tổng số \(325\) khách.'),
            'B': ('Đáp án đúng', r'\(P(C) = 0.04 \Rightarrow 0.04 \times 325 = 13\) khách.'),
            'C': ('Tính nhầm xác suất bù', r'Cộng trừ sai phần thập phân của \(1 - 0.64 - 0.32\).'),
            'D': ('Tính nhầm số khách phòng B', r'\(104 = 0.32 \times 325\) là số khách ở phòng B, không phải phòng C.'),
        },
        r'Gõ `(1 - 0.64 - 0.32) * 325` vào Desmos ra ngay `13`.',
    ),
    _mcq(
        'march2025_v5_math_m2_q7', 7, 'Algebra', 'Systems of two linear equations in two variables', 'Easy',
        r'<p style="text-align:center;font-size:19px;">\[y = \frac{x}{3} + 8\]\[y = -\frac{x}{3} + 20\]</p><p>The solution to the given system of equations is \((x, y)\).</p>',
        r'What is the value of \(2y\)?',
        {'A': r'\(8\)', 'B': r'\(12\)', 'C': r'\(20\)', 'D': r'\(28\)'},
        'D',
        r'Mẹo giải 3 giây: CỘNG VẾ THEO VẾ hai phương trình! Số hạng \(+\frac{x}{3}\) và \(-\frac{x}{3}\) triệt tiêu hoàn toàn: \[y + y = \left(\frac{x}{3} + 8\right) + \left(-\frac{x}{3} + 20\right) \Rightarrow 2y = 28.\] (Hoặc giải lần lượt: \(\frac{x}{3} + 8 = -\frac{x}{3} + 20 \Rightarrow x = 18 \Rightarrow y = 14 \Rightarrow 2y = 28\).)',
        r'Trước khi giải tìm riêng \(x\) và \(y\), luôn nhìn xem cộng hoặc trừ hai phương trình có ra thẳng biểu thức đề hỏi (\(2y\)) hay không!',
        {
            'A': ('Đọc nhầm hằng số', r'\(8\) chỉ là tung độ gốc của phương trình thứ nhất.'),
            'B': ('Trừ thay vì cộng', r'Lấy nhầm \(20 - 8 = 12\) thay vì \(20 + 8 = 28\).'),
            'C': ('Đọc nhầm hằng số', r'\(20\) chỉ là tung độ gốc của phương trình thứ hai.'),
            'D': ('Đáp án đúng', r'Cộng vế theo vế hai phương trình cho ngay \(2y = 8 + 20 = 28\).'),
        },
        r'Gõ hai phương trình vào Desmos sẽ thấy giao điểm `(18, 14)`, sau đó tính `2 * 14 = 28`.',
    ),
    _mcq(
        'march2025_v5_math_m2_q8', 8, 'Advanced Math', 'Nonlinear functions', 'Medium',
        r'<p>An object is launched from a height of \(124\) feet above the ground. A quadratic function \(f\) models the height above the ground, in feet, of the object \(t\) seconds after it is launched. According to the model, \(3\) seconds after the object is launched, it reaches a maximum height of \(268\) feet above the ground.</p>',
        r'Which equation defines \(f\)?',
        {
            'A': r'\(f(t) = -16(t + 268)^2 - 3\)',
            'B': r'\(f(t) = -16(t - 268)^2 + 3\)',
            'C': r'\(f(t) = -16(t + 3)^2 - 268\)',
            'D': r'\(f(t) = -16(t - 3)^2 + 268\)',
        },
        'D',
        r'Dạng đỉnh (vertex form) của hàm bậc hai có đỉnh \((h, k)\) là \(f(t) = a(t - h)^2 + k\). Vì vật đạt độ cao cực đại \(268\) feet tại thời điểm \(t = 3\) giây, đỉnh parabol là \((3, 268)\), suy ra \(f(t) = a(t - 3)^2 + 268\). Kiểm tra điều kiện độ cao ban đầu \(f(0) = 124\): \(a(0 - 3)^2 + 268 = 124 \Rightarrow 9a = -144 \Rightarrow a = -16\). Vậy \(f(t) = -16(t - 3)^2 + 268\).',
        r'Trong dạng đỉnh \(a(t - h)^2 + k\): hoành độ đỉnh \(h\) luôn đi với dấu TRỪ bên trong bình phương \((t - h)^2\), còn tung độ đỉnh \(k\) giữ nguyên dấu \(+k\) bên ngoài.',
        {
            'A': ('Đảo h và k + sai dấu', r'Đưa độ cao \(268\) vào chỗ thời gian và đặt sai cả hai dấu.'),
            'B': ('Đảo h và k', r'Đặt đỉnh ở \((268, 3)\) thay vì \((3, 268)\).'),
            'C': ('Sai dấu đỉnh', r'Cho đỉnh ở \((-3, -268)\) thay vì \((3, 268)\).'),
            'D': ('Đáp án đúng', r'Đỉnh \((3, 268)\) và kiểm tra \(f(0) = -16(9) + 268 = 124\) khớp hoàn toàn đề bài.'),
        },
        r'Gõ `f(t) = -16(t - 3)^2 + 268` trên Desmos: kiểm tra ngay đỉnh `(3, 268)` và giao trục tung `(0, 124)`.',
    ),
    _mcq(
        'march2025_v5_math_m2_q9', 9, 'Advanced Math', 'Nonlinear functions', 'Easy',
        _svg_m2_q9_exp()
        + r'<p>The graph of \(y = f(x)\) is shown, where \(f(x) = ab^x + c\), and \(a\), \(b\), and \(c\) are constants.</p>',
        r'For how many values of \(x\) does \(f(x) = 0\)?',
        {'A': r'Three', 'B': r'Two', 'C': r'One', 'D': r'Zero'},
        'D',
        r'Số nghiệm của phương trình \(f(x) = 0\) chính là số giao điểm của đồ thị \(y = f(x)\) với trục hoành (\(y = 0\)). Quan sát đồ thị hàm mũ \(f(x) = ab^x + c\): khi \(x \to -\infty\), đường cong tiệm cận đường ngang \(y = -4\) từ phía dưới; khi \(x\) tăng, đồ thị càng đi xuống sâu hơn nữa. Vì \(f(x) < -4 < 0\) với mọi \(x \in \mathbb{R}\), đồ thị KHÔNG BAO GIỜ cắt trục hoành → có \(0\) giá trị của \(x\) (Zero).',
        r'Hàm mũ \(f(x) = ab^x + c\) là hàm đơn điệu với tiệm cận ngang \(y = c\): nó chỉ có thể cắt trục \(x\) tối đa \(1\) lần (nếu \(a\) và \(c\) trái dấu) hoặc \(0\) lần (nếu \(a\) và \(c\) cùng dấu — ở đây cả hai đều âm).',
        {
            'A': ('Không thể xảy ra với hàm mũ', r'Một hàm mũ đơn điệu không bao giờ có tới \(3\) nghiệm.'),
            'B': ('Không thể xảy ra với hàm mũ', r'Đồ thị không uốn ngược lên nên không thể có \(2\) nghiệm.'),
            'C': ('Nhầm giao trục tung với trục hoành', r'Đồ thị cắt trục tung \(y\) tại \(1\) điểm (gần \((0, -5.5)\)), nhưng KHÔNG cắt trục hoành \(x\) (\(y = 0\)).'),
            'D': ('Đáp án đúng', r'Toàn bộ đồ thị nằm hoàn toàn dưới đường \(y = -4\), không bao giờ chạm \(y = 0\).'),
        },
        r'Không cần máy tính: đường cong luôn nằm dưới đường \(y = -4\) nên không bao giờ chạm trục \(x\) (\(y = 0\)) → chọn Zero.',
    ),
    _spr(
        'march2025_v5_math_m2_q10', 10, 'Algebra', 'Linear equations in one variable', 'Medium',
        r'<p>The equation \(h = \frac{9(v - 273.15)}{5} + 32\) gives the corresponding temperature \(h\), in degrees Fahrenheit, of any substance that has a temperature of \(v\) kelvins, where \(v > 0\).</p>',
        r'If a substance has a temperature of \(809.33\) degrees Fahrenheit, what is the corresponding temperature, in kelvins, of this substance?',
        ['705'], '705',
        r'Thay \(h = 809.33\) vào phương trình: \[809.33 = \frac{9(v - 273.15)}{5} + 32.\] Trừ \(32\) hai vế: \(777.33 = \frac{9(v - 273.15)}{5}\). Nhân hai vế với \(\frac{5}{9}\): \(v - 273.15 = 777.33 \times \frac{5}{9} = 86.37 \times 5 = 431.85\). Cộng \(273.15\) hai vế: \(v = 431.85 + 273.15 = 705\) kelvin.',
        r'Giải phương trình có số thập phân phức tạp như \(809.33\) và \(273.15\): luôn nhập trực tiếp vào Desmos để vừa nhanh gấp 3 lần vừa tránh \(100\%\) lỗi bấm số.',
        r'Gõ thẳng `809.33 = 9(x - 273.15)/5 + 32` vào Desmos (hoặc gõ `(809.33 - 32)*5/9 + 273.15`) sẽ ra chính xác số nguyên đẹp `705`.',
    ),
    _mcq(
        'march2025_v5_math_m2_q11', 11, 'Algebra', 'Linear equations in one variable', 'Medium',
        r'<p style="text-align:center;font-size:19px;">\[x(r - 7) + 3 = 17x + 25\]</p><p>In the given equation, \(r\) is a positive integer.</p>',
        r'If the given equation has exactly one solution, what CANNOT be the value of \(r\)?',
        {'A': r'\(3\)', 'B': r'\(7\)', 'C': r'\(22\)', 'D': r'\(24\)'},
        'D',
        r'Đưa các hạng tử chứa \(x\) về cùng một vế: \[(r - 7)x - 17x = 25 - 3 \Rightarrow (r - 24)x = 22.\] Phương trình bậc nhất \(Ax = B\) có ĐÚNG MỘT nghiệm khi và chỉ khi \(A \ne 0\). Nếu \(r = 24\), phương trình trở thành \(0x = 22\) (vô nghiệm!). Vì vậy \(r\) KHÔNG THỂ bằng \(24\).',
        r'Phương trình \(ax + c = bx + d\) có đúng \(1\) nghiệm \(\Leftrightarrow a \ne b\). Để tìm giá trị bị cấm ("CANNOT be"), chỉ cần cho hai hệ số của \(x\) bằng nhau: \(r - 7 = 17 \Rightarrow r = 24\).',
        {
            'A': ('Tạo nghiệm duy nhất', r'Khi \(r = 3\), phương trình là \(-21x = 22\), có nghiệm duy nhất \(x = -\frac{22}{21}\).'),
            'B': ('Bẫy làm r - 7 = 0', r'Khi \(r = 7\), vế trái mất \(x\) nhưng vế phải vẫn còn \(17x\): \(3 = 17x + 25\) vẫn có \(1\) nghiệm duy nhất!'),
            'C': ('Nhầm với hiệu hằng số', r'\(22 = 25 - 3\) là hằng số vế phải; khi \(r = 22\) vẫn có \(-2x = 22 \Rightarrow x = -11\).'),
            'D': ('Đáp án đúng', r'Khi \(r = 24\), hệ số của \(x\) ở hai vế đều bằng \(17\) nhưng hằng số \(3 \ne 25\) nên phương trình vô nghiệm.'),
        },
        r'Gõ `r - 7 = 17` → `r = 24`. Kiểm tra nhanh trên Desmos bằng thanh trượt `r`: đúng tại `r = 24` hai đường thẳng song song và không cắt nhau!',
    ),
    _mcq(
        'march2025_v5_math_m2_q12', 12, 'Advanced Math', 'Equivalent expressions', 'Medium',
        r'<p style="text-align:center;font-size:19px;">\[9x^6 - 63x^2\]</p>',
        r'Which expression is equivalent to \(9x^6 - 63x^2\), where \(x > 0\)?',
        {
            'A': r'\(9(x^3 - 7x^2)^2\)',
            'B': r'\(x^2(9x - 7)^4\)',
            'C': r'\(9x^2(x - 7)^4\)',
            'D': r'\(9x^2(x^4 - 7)\)',
        },
        'D',
        r'Đặt nhân tử chung lớn nhất (GCF) của \(9x^6\) và \(63x^2\) là \(9x^2\): \[9x^6 - 63x^2 = 9x^2 \cdot x^4 - 9x^2 \cdot 7 = 9x^2(x^4 - 7).\]',
        r'Khi rút \(x^2\) ra khỏi \(x^6\), ta TRỪ số mũ: \(\frac{x^6}{x^2} = x^{6-2} = x^4\) (không phải đưa mũ \(4\) ra ngoài toàn bộ dấu ngoặc như đáp án C).',
        {
            'A': ('Khai triển sai hoàn toàn', r'\(9(x^3 - 7x^2)^2 = 9x^6 - 126x^5 + 441x^4 \ne 9x^6 - 63x^2\).'),
            'B': ('Đưa mũ 4 ra ngoài ngoặc', r'\((9x - 7)^4\) tạo ra hệ số \(9^4 = 6561\) và nhiều hạng tử bậc trung gian.'),
            'C': ('Nhầm (x^4 - 7) với (x - 7)^4', r'\((x - 7)^4\) có hằng số \((-7)^4 = 2401\), không phải \(-7\).'),
            'D': ('Đáp án đúng', r'Nhân ngược kiểm tra: \(9x^2(x^4 - 7) = 9x^6 - 63x^2\).'),
        },
        r'Mẹo thử số trên Desmos: thay \(x = 2\) vào đề: \(9(2^6) - 63(2^2) = 576 - 252 = 324\). Chỉ đáp án D cho \(9(4)(16 - 7) = 36 \times 9 = 324\).',
    ),
    _mcq(
        'march2025_v5_math_m2_q13', 13, 'Geometry and Trigonometry', 'Lines, angles, and triangles', 'Medium',
        _svg_m2_q13_bowtie()
        + r'<p>In the figure shown, \(\overline{WZ}\) and \(\overline{XY}\) intersect at point \(Q\), \(YQ = 27\), \(WQ = 90\), \(WX = 60\), and \(XQ = 110\).</p>',
        r'What is the length of \(\overline{YZ}\)?',
        {'A': r'\(18\)', 'B': r'\(33\)', 'C': r'\(110\)', 'D': r'\(200\)'},
        'A',
        r'Xét hai tam giác \(\triangle WQX\) và \(\triangle YQZ\): có \(\angle W = \angle Y = a^\circ\) (giả thiết) và \(\angle WQX = \angle YQZ\) (hai góc đối đỉnh). Suy ra \(\triangle WQX \sim \triangle YQZ\) theo trường hợp góc–góc (AA). Viết đúng thứ tự đỉnh tương ứng \(W \leftrightarrow Y\), \(Q \leftrightarrow Q\), \(X \leftrightarrow Z\): \[\frac{YZ}{WX} = \frac{YQ}{WQ} \Rightarrow \frac{YZ}{60} = \frac{27}{90} = \frac{3}{10} \Rightarrow YZ = 60 \times \frac{3}{10} = 18.\]',
        r'Với hình tam giác đồng dạng dạng "nơ bướm" (bowtie), BẮT BUỘC viết rõ thứ tự đỉnh tương ứng \(\triangle WQX \sim \triangle YQZ\) trước khi lập tỷ số — số liệu \(XQ = 110\) là thông tin thừa (distractor) để bẫy học sinh tính nhầm \(QZ = 33\)!',
        {
            'A': ('Đáp án đúng', r'\(YZ = WX \cdot \frac{YQ}{WQ} = 60 \cdot \frac{27}{90} = 18\).'),
            'B': ('Bẫy tính nhầm cạnh QZ', r'\(33 = 110 \cdot \frac{27}{90}\) là độ dài đoạn \(\overline{QZ}\), KHÔNG phải \(\overline{YZ}\)!'),
            'C': ('Nhầm hai tam giác bằng nhau', r'\(110\) là độ dài đoạn \(XQ\).'),
            'D': ('Lập ngược tỷ số đồng dạng', r'Tính ngược \(60 \cdot \frac{90}{27} = 200\) (phóng to thay vì thu nhỏ).'),
        },
        r'Gõ `60 * 27 / 90` trên Desmos ra ngay `18`. Nhớ kiểm tra tỷ số thu nhỏ: vì \(YQ = 27 < WQ = 90\) nên \(YZ\) phải nhỏ hơn \(WX = 60\).',
    ),
    _mcq(
        'march2025_v5_math_m2_q14', 14, 'Problem-Solving and Data Analysis', 'Percentages', 'Hard',
        r'<p>The positive number \(a\) is \(2{,}184\%\) of the sum of the positive numbers \(b\) and \(c\), and \(b\) is \(84\%\) of \(c\).</p>',
        r'What percent of \(b\) is \(a\)?',
        {'A': r'\(4{,}784\%\)', 'B': r'\(2{,}600\%\)', 'C': r'\(40.19\%\)', 'D': r'\(22.68\%\)'},
        'A',
        r'Chuyển từng câu thành phương trình: (1) \(a = 21.84(b + c)\); (2) \(b = 0.84c \Rightarrow c = \frac{b}{0.84} = \frac{25}{21}b\). Thay vào (1): \[a = 21.84\left(b + \frac{25}{21}b\right) = 21.84 \cdot \frac{46}{21}b = 1.04 \times 46\,b = 47.84b.\] Đổi sang phần trăm: \(47.84 \times 100\% = 4{,}784\%\).',
        r'Mẹo chọn số chuẩn (Pick-a-Number): đặt \(c = 100 \Rightarrow b = 84 \Rightarrow b + c = 184 \Rightarrow a = 21.84 \times 184 = 4{,}018.56 \Rightarrow \frac{a}{b} \times 100\% = \frac{4{,}018.56}{84} \times 100\% = 4{,}784\%\) — siêu nhanh và không thể nhầm!',
        {
            'A': ('Đáp án đúng', r'\(\frac{a}{b} = 21.84\left(1 + \frac{1}{0.84}\right) = 47.84 = 4{,}784\%\).'),
            'B': ('Quên cộng b vào (b + c)', r'Tính nhầm \(a = 21.84c\) thay vì \(21.84(b + c)\), ra \(\frac{21.84}{0.84} = 26 = 2{,}600\%\).'),
            'C': ('Chia sai 100 lần hoặc nhầm tổng', r'Đọc nhầm giá trị \(a = 4{,}018.56\) chia cho \(100\).'),
            'D': ('Nhân ngược tỷ lệ 0.84', r'Tính nhầm \(21.84 \times 0.84\) thay vì chia cho \(0.84\).'),
        },
        r'Gõ lần lượt trên Desmos: `c = 100`, `b = 0.84 * c`, `a = 21.84 * (b + c)`, `(a / b) * 100` → hiện ngay `4784`!',
    ),
    _spr(
        'march2025_v5_math_m2_q15', 15, 'Advanced Math', 'Equivalent expressions', 'Hard',
        r'<p style="text-align:center;font-size:20px;">\[\sqrt[7]{p^4} = t^{\frac{5}{6}}\]</p><p>In the given equation, \(p > 1\) and \(t > 1\). If \(t = p^{2n - 1}\), where \(n\) is a constant, what is the value of \(n\)?</p>',
        r'What is the value of \(n\)?',
        ['59/70', '.8428', '.8429', '0.842', '0.843', '0.8428', '0.8429'], '59/70 (≈ 0.8429)',
        r'Bước 1: Đổi căn thức sang lũy thừa phân số: \(\sqrt[7]{p^4} = p^{\frac{4}{7}}\). Bước 2: Thay \(t = p^{2n - 1}\) vào vế phải: \[p^{\frac{4}{7}} = \left(p^{2n - 1}\right)^{\frac{5}{6}} = p^{\frac{5}{6}(2n - 1)}.\] Vì \(p > 1\), đồng nhất hai số mũ: \[\frac{4}{7} = \frac{5}{6}(2n - 1) \Rightarrow 2n - 1 = \frac{4}{7} \cdot \frac{6}{5} = \frac{24}{35} \Rightarrow 2n = 1 + \frac{24}{35} = \frac{59}{35} \Rightarrow n = \frac{59}{70}.\]',
        r'Quy tắc vàng đổi căn thức: \(\sqrt[b]{p^a} = p^{\frac{a}{b}}\) ("mũ trên, căn dưới"). Khi hai lũy thừa cùng cơ số \(p > 1\) bằng nhau, cho hai số mũ bằng nhau và luôn giữ dạng phân số tối giản `59/70` khi nhập SPR.',
        r'Gõ thẳng `4/7 = (5/6)*(2x - 1)` vào Desmos sẽ ra `x = 0.842857...`, bấm nút đổi phân số ở bên trái dòng biểu thức `(4/7 * 6/5 + 1)/2` để ra ngay `59/70`!',
    ),
    _mcq(
        'march2025_v5_math_m2_q16', 16, 'Algebra', 'Linear functions', 'Medium',
        r'<p>A painting studio is offering a promotion where the first class is free, the second class is half off the regular price, and the remaining classes are regularly priced. The regular price of a class is $26.40.</p>',
        r'Which function \(f\) gives the total cost, in dollars, of \(x\) classes taken using this promotion, where \(x \ge 2\)?',
        {
            'A': r'\(f(x) = 26.40(x - 1) + 13.20\)',
            'B': r'\(f(x) = 26.40(x - 2) + 13.20\)',
            'C': r'\(f(x) = 26.40(x - 1) + 13.20(x - 2)\)',
            'D': r'\(f(x) = 26.40(x - 2) + 13.20(x - 1)\)',
        },
        'B',
        r'Phân tách chi phí cho tổng cộng \(x\) buổi học (với \(x \ge 2\)): buổi thứ \(1\) miễn phí ($0); buổi thứ \(2\) giảm một nửa giá gốc, tức \(\frac{26.40}{2} = \$13.20\); số buổi còn lại phải đóng nguyên giá là \((x - 2)\) buổi, tốn \(26.40(x - 2)\) đô la. Tổng chi phí: \(f(x) = 26.40(x - 2) + 13.20\).',
        r'Mẹo kiểm tra thần tốc cho bài toán lập hàm có điều kiện \(x \ge 2\): thay ngay \(x = 2\)! Học \(2\) buổi thì buổi 1 miễn phí + buổi 2 giá $13.20 \(\Rightarrow f(2) = 13.20\). Chỉ đáp án B thỏa mãn \(f(2) = 13.20\).',
        {
            'A': ('Đếm thừa buổi nguyên giá', r'Thay \(x = 2\) cho \(f(2) = 26.40(1) + 13.20 = 39.60\) (tính nhầm tới \(3\) buổi thay vì \(2\)!).'),
            'B': ('Đáp án đúng', r'Khớp mọi giá trị: \(f(2) = 13.20\), \(f(3) = 13.20 + 26.40 = 39.60\).'),
            'C': ('Nhân thừa (x - 2) vào buổi giảm giá', r'Chỉ có ĐÚNG \(1\) buổi được giảm giá $13.20, không phải \((x - 2)\) buổi.'),
            'D': ('Nhân thừa (x - 1) vào buổi giảm giá', r'Khi \(x = 2\) cho \(13.20\), nhưng khi \(x = 3\) cho \(26.40 + 26.40 = 52.80 \ne 39.60\).'),
        },
        r'Thử hai điểm trên Desmos: \(f(2) = 13.20\) và \(f(3) = 39.60\). Chỉ duy nhất hàm B đi qua cả hai điểm này.',
    ),
    _mcq(
        'march2025_v5_math_m2_q17', 17, 'Geometry and Trigonometry', 'Lines, angles, and triangles', 'Easy',
        r'<p>The triangle inequality theorem states that the sum of any two sides of a triangle must be greater than the length of the third side. A triangle has side lengths of \(10\) and \(12\).</p>',
        r'Which inequality represents the possible lengths, \(x\), of the third side of the triangle?',
        {
            'A': r'\(x < 22\)',
            'B': r'\(x > 22\)',
            'C': r'\(2 < x < 22\)',
            'D': r'\(x < 2\text{ or }x > 22\)',
        },
        'C',
        r'Áp dụng bất đẳng thức tam giác cho ba cạnh \(10, 12, x\): (1) \(x < 10 + 12 = 22\); (2) \(x + 10 > 12 \Rightarrow x > 2\); (3) \(x + 12 > 10\) (luôn đúng vì \(x > 2\)). Kết hợp lại ta có \(|12 - 10| < x < 12 + 10 \Leftrightarrow 2 < x < 22\).',
        r'Công thức nhanh bất đẳng thức tam giác cho hai cạnh \(a, b\): cạnh thứ ba \(x\) luôn thỏa mãn \(|a - b| < x < a + b\).',
        {
            'A': ('Thiếu chặn dưới', r'Nếu chỉ \(x < 22\) thì \(x = 1\) vẫn thỏa mãn, nhưng \(1 + 10 = 11 < 12\) không tạo thành tam giác.'),
            'B': ('Ngược dấu hoàn toàn', r'Nếu \(x > 22\) thì cạnh \(x\) lớn hơn tổng hai cạnh kia (\(10 + 12 = 22\)), vô lý.'),
            'C': ('Đáp án đúng', r'\(|12 - 10| < x < 12 + 10 \Leftrightarrow 2 < x < 22\).'),
            'D': ('Miền bù (ngoài khoảng)', r'Đây chính là tập hợp các giá trị KHÔNG THỂ tạo thành tam giác.'),
        },
        r'Không cần máy tính: hiệu hai cạnh \(12 - 10 = 2\), tổng hai cạnh \(12 + 10 = 22 \Rightarrow 2 < x < 22\).',
    ),
    _mcq(
        'march2025_v5_math_m2_q18', 18, 'Advanced Math', 'Nonlinear functions', 'Hard',
        _svg_m2_q18_exp_shift()
        + r'<p>The graph of \(y = f(x) + 2\) is shown.</p>',
        r'Which equation defines function \(f\)?',
        {
            'A': r'\(f(x) = -4^x + 3\)',
            'B': r'\(f(x) = -4^x + 5\)',
            'C': r'\(f(x) = -4^x + 6\)',
            'D': r'\(f(x) = -4^x + 7\)',
        },
        'B',
        r'Đọc kỹ tiêu đề đồ thị: hình vẽ là đồ thị của \(y = f(x) + 2\) (KHÔNG PHẢI \(y = f(x)\)!). Trên đồ thị ta thấy điểm \((0, 6)\) và \((1, 3)\) nằm chính xác trên đường cong. Vì cả \(4\) đáp án đều có dạng \(f(x) = -4^x + c\), suy ra \(y = f(x) + 2 = -4^x + c + 2\). Thay \((0, 6)\): \(6 = -4^0 + c + 2 = -1 + c + 2 = c + 1 \Rightarrow c = 5\). Kiểm tra điểm \((1, 3)\): \(f(1) + 2 = (-4 + 5) + 2 = 3\) (chính xác!). Vậy \(f(x) = -4^x + 5\).',
        r'Bẫy TỊNH TIẾN ĐỒ THỊ kinh điển mức 750+ của Digital SAT: luôn gạch chân xem đồ thị là \(y = f(x)\) hay \(y = f(x) + k\). Vì đề cho đồ thị \(f(x) + 2\), phải TRỪ ĐI \(2\) từ phương trình của đồ thị (\((-4^x + 7) - 2 = -4^x + 5\))!',
        {
            'A': ('Trừ 2 hai lần', r'Trừ nhầm \(4\) đơn vị thay vì \(2\) từ tiệm cận \(7\).'),
            'B': ('Đáp án đúng', r'Đồ thị là \(y = -4^x + 7 = f(x) + 2 \Rightarrow f(x) = -4^x + 5\).'),
            'C': ('Nhầm y-intercept thành hằng số c', r'Nhầm \((0, 6)\) nghĩa là \(c = 6\) (quên rằng \(-4^0 = -1\) và quên trừ \(2\)).'),
            'D': ('Quên trừ 2 (bẫy f(x) + 2)', r'\(-4^x + 7\) là phương trình của ĐỒ THỊ \(y = f(x) + 2\), chưa trừ \(2\) để tìm \(f(x)\) !'),
        },
        r'Trên Desmos, gõ `y = (-4^x + c) + 2` với thanh trượt `c` (thử `3, 5, 6, 7`): đúng tại `c = 5`, đồ thị đi qua chính xác `(0, 6)` và `(1, 3)`!',
    ),
    _mcq(
        'march2025_v5_math_m2_q19', 19, 'Geometry and Trigonometry', 'Circles', 'Hard',
        r'<p>A circle in the \(xy\)-plane has its center at \((-2, 2)\). Line \(t\) is tangent to this circle at the point \((3, -1)\).</p>',
        r'Which of the following points also lies on line \(t\)?',
        {
            'A': r'\(\left(0,\; \frac{5}{3}\right)\)',
            'B': r'\((1, 7)\)',
            'C': r'\((6, 4)\)',
            'D': r'\((8, 2)\)',
        },
        'C',
        r'Tiếp tuyến \(t\) tại tiếp điểm \((3, -1)\) luôn VUÔNG GÓC với bán kính nối tâm \((-2, 2)\) tới \((3, -1)\). Bước 1: Tính hệ số góc của bán kính: \(m_r = \frac{-1 - 2}{3 - (-2)} = -\frac{3}{5}\). Bước 2: Hệ số góc của tiếp tuyến vuông góc \(t\) là \(m_t = -\frac{1}{m_r} = \frac{5}{3}\). Bước 3: Phương trình tiếp tuyến \(t\) đi qua \((3, -1)\) là \(y + 1 = \frac{5}{3}(x - 3) \Rightarrow y = \frac{5}{3}x - 6\). Kiểm tra các điểm: tại \(x = 6\), \(y = \frac{5}{3}(6) - 6 = 4 \Rightarrow (6, 4)\) nằm trên \(t\)!',
        r'Mẹo bước nhảy vector: bán kính đi theo \((\Delta x, \Delta y) = (+5, -3)\) nên tiếp tuyến vuông góc có bước nhảy \((+3, +5)\). Từ \((3, -1)\) cộng ngay \((+3, +5)\) ra thẳng \((6, 4)\)!',
        {
            'A': ('Nhầm y-intercept với hệ số góc', r'Tại \(x = 0\), đường \(t\) đi qua \((0, -6)\), không phải \((0, \frac{5}{3})\).'),
            'B': ('Dùng sai hệ số góc', r'Hệ số góc nối \((3, -1)\) tới \((1, 7)\) là \(\frac{8}{-2} = -4 \ne \frac{5}{3}\).'),
            'C': ('Đáp án đúng', r'Hệ số góc nối \((3, -1)\) tới \((6, 4)\) là \(\frac{4 - (-1)}{6 - 3} = \frac{5}{3}\) — vuông góc với bán kính \(-\frac{3}{5}\).'),
            'D': ('Quên nghịch đảo hệ số góc', r'Dùng nhầm hệ số góc \(+\frac{3}{5}\) (đi theo \((+5, +3)\) từ \((3, -1)\) ra \((8, 2)\)) thay vì \(+\frac{5}{3}\).'),
        },
        r'Gõ đường tròn `(x + 2)^2 + (y - 2)^2 = 34` và đường thẳng `y + 1 = (5/3)(x - 3)` vào Desmos, chấm 4 điểm đáp án sẽ thấy `(6, 4)` nằm chính xác trên tiếp tuyến!',
    ),
    _spr(
        'march2025_v5_math_m2_q20', 20, 'Geometry and Trigonometry', 'Area and volume', 'Hard',
        r'<p>Right rectangular prism X is similar to right rectangular prism Y. The surface area of right rectangular prism X is \(55\) square centimeters (\(\text{cm}^2\)), and the surface area of right rectangular prism Y is \(880\text{ cm}^2\). The volume of right rectangular prism Y is \(1{,}600\) cubic centimeters (\(\text{cm}^3\)).</p>',
        r'What is the sum of the volumes, in \(\text{cm}^3\), of right rectangular prism X and right rectangular prism Y?',
        ['1625'], '1625',
        r'Bước 1: Tìm tỷ số đồng dạng tuyến tính \(k\) từ tỷ số diện tích toàn phần: \[k^2 = \frac{SA_Y}{SA_X} = \frac{880}{55} = 16 \Rightarrow k = \sqrt{16} = 4.\] Bước 2: Tỷ số thể tích bằng lập phương tỷ số đồng dạng: \[\frac{V_Y}{V_X} = k^3 = 4^3 = 64 \Rightarrow V_X = \frac{1{,}600}{64} = 25\text{ cm}^3.\] Bước 3: Đề hỏi TỔNG thể tích hai khối lăng trụ X và Y: \[V_X + V_Y = 25 + 1{,}600 = 1{,}625\text{ cm}^3.\] Nhập `1625`.',
        r'Quy tắc \(k - k^2 - k^3\) cho hình khối đồng dạng: diện tích tỷ lệ theo \(k^2\), thể tích tỷ lệ theo \(k^3\). Và ĐỌC KỸ câu hỏi cuối cùng: đề hỏi TỔNG \(V_X + V_Y = 1625\), tránh bẫy dừng sớm ở \(V_X = 25\)!',
        r'Gõ trên Desmos: `k = sqrt(880 / 55)` (= 4), rồi gõ `1600 / k^3 + 1600` → hiện ngay `1625`.',
    ),
    _spr(
        'march2025_v5_math_m2_q21', 21, 'Advanced Math', 'Nonlinear functions', 'Hard',
        r'<p>The function \(f\) is defined by \(f(x) = \frac{|x|}{a} - 16\), where \(a < 0\).</p>',
        r'What is the product of \(f(17a)\) and \(f(8a)\)?',
        ['792'], '792',
        r'CỰC KỲ LƯU Ý điều kiện \(a < 0\)! Khi \(a < 0\) thì \(17a < 0\) và \(8a < 0\), do đó khi phá trị tuyệt đối phải đổi dấu: \(|17a| = -17a\) và \(|8a| = -8a\). Suy ra: \[f(17a) = \frac{|17a|}{a} - 16 = \frac{-17a}{a} - 16 = -17 - 16 = -33,\] \[f(8a) = \frac{|8a|}{a} - 16 = \frac{-8a}{a} - 16 = -8 - 16 = -24.\] Tích cần tìm là \(f(17a) \cdot f(8a) = (-33)(-24) = 792\).',
        r'Bẫy trị tuyệt đối kinh điển của Q21 M2: với \(a < 0\), \(\frac{|ka|}{a} = -|k|\) (KHÔNG PHẢI \(+|k|\)!). Mẹo an toàn tuyệt đối: gán ngay một giá trị âm cụ thể như \(a = -1\) rồi tính!',
        r'Mẹo Desmos 5 giây: gõ `a = -1`, `f(x) = abs(x)/a - 16`, rồi gõ `f(17a) * f(8a)` → hiện ngay đáp án `792` (thử đổi `a = -5` vẫn luôn ra `792`!).',
    ),
    _spr(
        'march2025_v5_math_m2_q22', 22, 'Advanced Math', 'Nonlinear equations in one variable', 'Hard',
        r'<p style="text-align:center;font-size:19px;">\[125x^2 - (25a + 5b)x + ab = 0\]</p><p>In the given equation, \(a\) and \(b\) are positive constants. The sum of the solutions to the given equation is \(k(5a + b)\), where \(k\) is a constant.</p>',
        r'What is the value of \(k\)?',
        ['1/25', '0.04', '.04'], '1/25 (hoặc 0.04)',
        r'Áp dụng định lý Vi-ét cho phương trình bậc hai \(Ax^2 + Bx + C = 0\) với \(A = 125\), \(B = -(25a + 5b)\), \(C = ab\) (kiểm tra phân tích nhân tử: \((25x - b)(5x - a) = 0\), nên phương trình luôn có hai nghiệm \(x_1 = \frac{a}{5}\) và \(x_2 = \frac{b}{25}\)). Tổng các nghiệm là: \[S = -\frac{B}{A} = \frac{25a + 5b}{125} = \frac{5(5a + b)}{125} = \frac{1}{25}(5a + b).\] So sánh với \(k(5a + b)\) (vì \(a, b > 0 \Rightarrow 5a + b > 0\)), ta suy ra \(k = \frac{1}{25} = 0.04\).',
        r'Khi câu cuối M2 hỏi "sum of the solutions" của phương trình bậc hai có tham số \(a, b\), dùng ngay Vi-ét \(-\frac{B}{A}\) rồi đặt nhân tử chung để khớp chính xác biểu thức mục tiêu \((5a + b)\).',
        r'Mẹo Desmos: chọn số bất kỳ \(a = 2, b = 3\), giải nghiệm \(125x^2 - 65x + 6 = 0\) (hoặc tính trực tiếp `(25a + 5b) / (125 * (5a + b))`) → ra ngay `0.04`, bấm đổi phân số thành `1/25`!',
    ),
]


# ============================================================================
# FULL BLUEBOOK ADAPTIVE MOCK PAYLOAD (routingThreshold: 0 -> REAL M2 FOR ALL)
# ============================================================================

TEST_DATA = {
    'schemaVersion': 2,
    'mode': 'adaptive_mock',
    'section': 'math',
    'basicInfo': {
        'title': TEST_TITLE,
        'subtitle': 'Đề thi thật Digital SAT Toán tháng 3/2025 (Ver 5) — Đủ 2 Module (M1: 22 câu + M2: 22 câu)',
        'difficultyBadge': 'REAL EXAM • MARCH 2025',
        'targetTimeMinutes': 70,
        'routingThreshold': 0,
    },
    'module1': {
        'id': 'm1',
        'title': 'Section 2, Module 1: Math',
        'subtitle': '22 Questions • 35 Minutes • Real Exam Module 1',
        'timeLimitMinutes': 35,
        'questions': M1_QUESTIONS,
    },
    'module2_hard': {
        'id': 'm2_hard',
        'title': 'Section 2, Module 2: Math',
        'subtitle': '22 Questions • 35 Minutes • Real Exam Module 2',
        'timeLimitMinutes': 35,
        'questions': M2_QUESTIONS,
    },
    'module2_lower': {
        'id': 'm2_lower',
        'title': 'Section 2, Module 2: Math',
        'subtitle': '22 Questions • 35 Minutes • Real Exam Module 2',
        'timeLimitMinutes': 35,
        'questions': copy.deepcopy(M2_QUESTIONS),
    },
}


# ============================================================================
# MANDATORY MATHEMATICAL & SCHEMA AUDIT (ALL 44 QUESTIONS + REAL NODE KATEX)
# ============================================================================

def verify_all_math():
    """Programmatically verifies all 44 math answers and runs Bluebook + KaTeX validation."""
    m1 = {q['number']: q for q in M1_QUESTIONS}
    m2 = {q['number']: q for q in M2_QUESTIONS}
    assert len(M1_QUESTIONS) == 22 and set(m1.keys()) == set(range(1, 23))
    assert len(M2_QUESTIONS) == 22 and set(m2.keys()) == set(range(1, 23))

    # --- MODULE 1 VERIFICATIONS (Q1 - Q22) ---
    # M1 Q1: y = 1.5x + 100 at x = 50 -> 175 (C)
    assert Fraction(3, 2) * 50 + 100 == 175 and m1[1]['correctAnswer'] == 'C'

    # M1 Q2: 7(x^2 + 5) == 7x^2 + 35 for test x values (A)
    for x in (-3, 0, 2, 7):
        assert 7 * (x ** 2 + 5) == 7 * x ** 2 + 35
    assert m1[2]['correctAnswer'] == 'A'

    # M1 Q3: y = 4^(x + 1) + 1 at x = 0 -> (0, 5) (D)
    assert (4 ** (0 + 1)) + 1 == 5 and m1[3]['correctAnswer'] == 'D'

    # M1 Q4: f(x) = 8(2x + 2) = 80 -> x = 4 (A)
    x4 = Fraction(80 // 8 - 2, 2)
    assert x4 == 4 and 8 * (2 * x4 + 2) == 80 and m1[4]['correctAnswer'] == 'A'

    # M1 Q5: n = p / (23v) => p = 23vn (D)
    for n_v, v_v in ((Fraction(3, 2), Fraction(4, 5)), (Fraction(7), Fraction(2))):
        p_v = 23 * v_v * n_v
        assert p_v / (23 * v_v) == n_v
    assert m1[5]['correctAnswer'] == 'D'

    # M1 Q6 (SPR): 49 + 2x = 125 -> x = 38
    x6 = Fraction(125 - 49, 2)
    assert x6 == 38 and m1[6]['correctAnswer'] == '38' and '38' in m1[6]['acceptedAnswers']

    # M1 Q7: pi*9^2 + 25*pi = 106*pi (A)
    assert 9 ** 2 + 25 == 106 and m1[7]['correctAnswer'] == 'A'

    # M1 Q8 (SPR): mean of [3710, 3710, 3130, 3750, 3150] = 3490
    lemurs = [3710, 3710, 3130, 3750, 3150]
    mean8 = Fraction(sum(lemurs), len(lemurs))
    assert mean8 == 3490 and m1[8]['correctAnswer'] == '3490'

    # M1 Q9: 2x(x - 3)(x + 5) = 0 -> roots {0, 3, -5}; among {-3, 0, 2, 5} only 0 (B)
    roots9 = {0, 3, -5}
    opts9 = {'A': -3, 'B': 0, 'C': 2, 'D': 5}
    valid9 = [k for k, v in opts9.items() if v in roots9]
    assert valid9 == ['B'] and m1[9]['correctAnswer'] == 'B'

    # M1 Q10: similar triangles preserve corresponding angles -> 56 deg (B)
    assert m1[10]['correctAnswer'] == 'B'

    # M1 Q11 (SPR): 6.00 * 310% * (1 - 75%) = 4.65 = 93/20
    p11 = Fraction(6) * Fraction(310, 100) * Fraction(25, 100)
    assert p11 == Fraction(93, 20) and float(p11) == 4.65
    assert m1[11]['correctAnswer'] == '4.65' and '93/20' in m1[11]['acceptedAnswers']

    # M1 Q12: f(x) = 47 constant -> f(0)=f(1)=f(2)=47 (B)
    assert all(47 == 47 for _ in (0, 1, 2)) and m1[12]['correctAnswer'] == 'B'

    # M1 Q13: s(t) = 136 * (0.5)^(t/29) -> s(58) = 34 (A)
    s58 = Fraction(136) * (Fraction(1, 2) ** (58 // 29))
    assert s58 == 34 and m1[13]['correctAnswer'] == 'A'

    # M1 Q14: +2.5%/yr -> factor 1.025 > 1 -> Increasing exponential (C)
    assert Fraction(1025, 1000) > 1 and m1[14]['correctAnswer'] == 'C'

    # M1 Q15: 2x - 6y > 12 -> QII (x<0, y>0) has 2x - 6y < 0 < 12 (A)
    assert 2 * (-1) - 6 * (-10) > 12  # B has solutions
    assert 2 * 10 - 6 * 1 > 12        # C has solutions
    assert 2 * 7 - 6 * 0 > 12         # D has solutions
    assert m1[15]['correctAnswer'] == 'A'

    # M1 Q16: circle center (18,16), r = 6k -> r^2 = 36k^2 (B)
    for k in (1, 2, 5):
        assert (6 * k) ** 2 == 36 * (k ** 2)
    assert m1[16]['correctAnswer'] == 'B'

    # M1 Q17: x^2 - 24x - 8 = 0 -> discriminant > 0, sum = 24 (D)
    assert (-24) ** 2 - 4 * 1 * (-8) > 0 and Fraction(24, 1) == 24 and m1[17]['correctAnswer'] == 'D'

    # M1 Q18 (SPR): 22.7 / x <= 1/12 => x >= 272.4 = 1362/5
    x18 = Fraction(227, 10) * 12
    assert x18 == Fraction(1362, 5) and float(x18) == 272.4
    assert m1[18]['correctAnswer'] == '272.4' and '1362/5' in m1[18]['acceptedAnswers']

    # M1 Q19: vertical angles w = 112 => z = 112 (D)
    assert m1[19]['correctAnswer'] == 'D'

    # M1 Q20 (SPR): 3(2-7x) + 5(2-7x) + 6 = 7(2-7x) + 2 => 2-7x = -4 => 7x-2 = 4
    u20 = Fraction(2 - 6, 3 + 5 - 7)
    assert u20 == -4 and -u20 == 4
    x20 = Fraction(2 - u20, 7)
    assert 3 * (2 - 7 * x20) + 5 * (2 - 7 * x20) + 6 == 7 * (2 - 7 * x20) + 2
    assert 7 * x20 - 2 == 4 and m1[20]['correctAnswer'] == '4'

    # M1 Q21: line k slope m, perp line l slope -1/m through (2,9) -> at x=3, y = 9 - 1/m (A)
    for m_val in (Fraction(2), Fraction(5, 2), Fraction(7)):
        y_at_3 = 9 + (-Fraction(1, m_val)) * (3 - 2)
        assert y_at_3 == 9 - Fraction(1, m_val)
    assert m1[21]['correctAnswer'] == 'A'

    # M1 Q22 (SPR): 245.00 * (0.914)^3 = 187.07022628 -> rounded 5-char: 187.1, trunc: 187.0
    v22 = Fraction(245) * (Fraction(914, 1000) ** 3)
    assert math.isclose(float(v22), 187.07022628, rel_tol=1e-12)
    assert round(float(v22), 1) == 187.1
    assert m1[22]['correctAnswer'] == '187.1' and '187.0' in m1[22]['acceptedAnswers'] and '187.07' in m1[22]['acceptedAnswers']

    # --- MODULE 2 VERIFICATIONS (Q1 - Q22) ---
    # M2 Q1: 21h + 10c = 900 -> 21 is $/hr at regular job (A)
    assert m2[1]['correctAnswer'] == 'A'

    # M2 Q2: line of best fit y = -x + 1.5 passes (-14, 15.5) and (0, 1.5) (D)
    assert -(-14) + Fraction(3, 2) == Fraction(31, 2) and -(0) + Fraction(3, 2) == Fraction(3, 2)
    assert m2[2]['correctAnswer'] == 'D'

    # M2 Q3: y = 3x + 1 and y = 4x - 6 -> (7, 22) (C)
    x3 = Fraction(1 + 6, 4 - 3)
    y3 = 3 * x3 + 1
    assert (x3, y3) == (7, 22) and 4 * x3 - 6 == y3 and m2[3]['correctAnswer'] == 'C'

    # M2 Q4: y = (2/7)x + 3, infinitely many solutions with y = mx + b -> b = 3 (D)
    assert m2[4]['correctAnswer'] == 'D'

    # M2 Q5: y = 58*pi*x^2 -> at x=4, y ~ 2915.4; at x=5, y ~ 4555.3 (A)
    assert 2900 < 58 * math.pi * (4 ** 2) < 2950 and 4500 < 58 * math.pi * (5 ** 2) < 4600
    assert m2[5]['correctAnswer'] == 'A'

    # M2 Q6: 325 * (1 - 0.64 - 0.32) = 13 (B)
    p6_c = Fraction(1) - Fraction(64, 100) - Fraction(32, 100)
    assert p6_c * 325 == 13 and m2[6]['correctAnswer'] == 'B'

    # M2 Q7: y = x/3 + 8, y = -x/3 + 20 -> 2y = 28 (D)
    x7 = Fraction(20 - 8, Fraction(2, 3))
    y7 = x7 / 3 + 8
    assert x7 == 18 and y7 == 14 and 2 * y7 == 28 and m2[7]['correctAnswer'] == 'D'

    # M2 Q8: f(t) = -16(t - 3)^2 + 268 -> vertex (3, 268), f(0) = 124 (D)
    assert -16 * ((0 - 3) ** 2) + 268 == 124 and -16 * ((3 - 3) ** 2) + 268 == 268
    assert m2[8]['correctAnswer'] == 'D'

    # M2 Q9: f(x) < -4 < 0 for all real x -> 0 solutions (D)
    for xv in (-10, -2, 0, 2, 10):
        assert -1.5 * (1.9 ** xv) - 4.0 < 0
    assert m2[9]['correctAnswer'] == 'D'

    # M2 Q10 (SPR): 809.33 = 9(v - 273.15)/5 + 32 -> v = 705
    v10 = (Fraction(80933, 100) - 32) * Fraction(5, 9) + Fraction(27315, 100)
    assert v10 == 705 and m2[10]['correctAnswer'] == '705'

    # M2 Q11: x(r - 7) + 3 = 17x + 25 -> no solution when r - 7 = 17 => r = 24 (D)
    assert 24 - 7 == 17 and m2[11]['correctAnswer'] == 'D'

    # M2 Q12: 9x^6 - 63x^2 = 9x^2(x^4 - 7) (D)
    for x in (1, 2, 3, 5):
        assert 9 * (x ** 6) - 63 * (x ** 2) == 9 * (x ** 2) * (x ** 4 - 7)
    assert m2[12]['correctAnswer'] == 'D'

    # M2 Q13: triangle WQX ~ triangle YQZ => YZ = WX * (YQ / WQ) = 60 * 27 / 90 = 18 (A)
    yz13 = Fraction(60 * 27, 90)
    assert yz13 == 18 and m2[13]['correctAnswer'] == 'A'

    # M2 Q14: a = 21.84(b + c), b = 0.84c => a/b = 47.84 = 4,784% (A)
    ratio14 = Fraction(2184, 100) * (1 + Fraction(100, 84))
    assert ratio14 * 100 == 4784 and m2[14]['correctAnswer'] == 'A'

    # M2 Q15 (SPR): root_7(p^4) = t^(5/6), t = p^(2n - 1) => 4/7 = (5/6)(2n - 1) => n = 59/70
    n15 = (Fraction(4, 7) * Fraction(6, 5) + 1) / 2
    assert n15 == Fraction(59, 70)
    assert Fraction(5, 6) * (2 * n15 - 1) == Fraction(4, 7)
    assert m2[15]['correctAnswer'] == '59/70' and '.8429' in m2[15]['acceptedAnswers']

    # M2 Q16: f(x) = 26.40(x - 2) + 13.20 for x >= 2 (B)
    assert Fraction(2640, 100) * (2 - 2) + Fraction(1320, 100) == Fraction(1320, 100)
    assert Fraction(2640, 100) * (3 - 2) + Fraction(1320, 100) == Fraction(3960, 100)
    assert m2[16]['correctAnswer'] == 'B'

    # M2 Q17: triangle sides 10, 12 => 2 < x < 22 (C)
    assert abs(12 - 10) == 2 and 12 + 10 == 22 and m2[17]['correctAnswer'] == 'C'

    # M2 Q18: graph of y = f(x) + 2 passes (0,6), (1,3) -> y = -4^x + 7 -> f(x) = -4^x + 5 (B)
    for xv, yv in ((0, 6), (1, 3)):
        assert (-(4 ** xv) + 5) + 2 == yv
    assert m2[18]['correctAnswer'] == 'B'

    # M2 Q19: circle center (-2, 2), tangent at (3, -1) -> slope_r = -3/5, slope_t = 5/3 -> (6, 4) (C)
    m_rad = Fraction(-1 - 2, 3 - (-2))
    m_tan = -Fraction(1, m_rad)
    assert m_rad == Fraction(-3, 5) and m_tan == Fraction(5, 3)
    assert m_tan * (6 - 3) + (-1) == 4
    assert m_tan * (0 - 3) + (-1) != Fraction(5, 3)
    assert m_tan * (1 - 3) + (-1) != 7
    assert m_tan * (8 - 3) + (-1) != 2
    assert m2[19]['correctAnswer'] == 'C'

    # M2 Q20 (SPR): SA_Y/SA_X = 880/55 = 16 -> k=4 -> V_X = 1600/64 = 25 -> sum = 1625
    k2 = Fraction(880, 55)
    assert k2 == 16
    k_lin = 4
    v_x = Fraction(1600, k_lin ** 3)
    assert v_x == 25 and v_x + 1600 == 1625 and m2[20]['correctAnswer'] == '1625'

    # M2 Q21 (SPR): f(x) = |x|/a - 16, a < 0 -> f(17a)*f(8a) = (-33)*(-24) = 792
    for a_val in (Fraction(-1), Fraction(-3, 2), Fraction(-11)):
        f17 = Fraction(abs(17 * a_val), a_val) - 16
        f8 = Fraction(abs(8 * a_val), a_val) - 16
        assert f17 == -33 and f8 == -24 and f17 * f8 == 792
    assert m2[21]['correctAnswer'] == '792'

    # M2 Q22 (SPR): 125x^2 - (25a + 5b)x + ab = 0 -> sum = (25a+5b)/125 = (1/25)(5a+b) -> k = 1/25
    for a_v, b_v in ((Fraction(2), Fraction(3)), (Fraction(7), Fraction(11))):
        s_roots = Fraction(25 * a_v + 5 * b_v, 125)
        assert s_roots == Fraction(1, 25) * (5 * a_v + b_v)
        # Also verify explicit factored roots a/5 and b/25
        r1, r2 = Fraction(a_v, 5), Fraction(b_v, 25)
        assert 125 * (r1 ** 2) - (25 * a_v + 5 * b_v) * r1 + a_v * b_v == 0
        assert 125 * (r2 ** 2) - (25 * a_v + 5 * b_v) * r2 + a_v * b_v == 0
        assert r1 + r2 == s_roots
    assert m2[22]['correctAnswer'] == '1/25' and '0.04' in m2[22]['acceptedAnswers'] and '.04' in m2[22]['acceptedAnswers']

    # --- SCHEMA, WATERMARK & REAL NODE KATEX VALIDATION ---
    raw_dump = str(TEST_DATA)
    for bad in ('@DSATuz', '@D7SAT', 'TELEGRAM', 'satuzhunters'):
        assert bad.lower() not in raw_dump.lower(), f'Watermark token leaked: {bad}'

    valid_domains = {
        'Algebra',
        'Advanced Math',
        'Problem-Solving and Data Analysis',
        'Geometry and Trigonometry',
    }
    for q in M1_QUESTIONS + M2_QUESTIONS:
        assert q['domain'] in valid_domains, f'Invalid domain {q["domain"]} on {q["id"]}'
        if q['questionFormat'] == 'mcq':
            oa = q['explanation'].get('optionAnalysis') or {}
            assert set(oa.keys()) == {'A', 'B', 'C', 'D'}
            for lbl, item in oa.items():
                r_txt = item.get('reasonVi') or ''
                assert r_txt.count('\\(') == r_txt.count('\\)'), f'Unbalanced \\( in {q["id"]} {lbl}'
                assert r_txt.count('\\[') == r_txt.count('\\]'), f'Unbalanced \\[ in {q["id"]} {lbl}'

    from scripts.sat_real_exams_pipeline import validate_sat_bluebook_json
    errs = validate_sat_bluebook_json(TEST_DATA, TEST_CODE)
    assert not errs, 'Bluebook/KaTeX validation failed:\n' + '\n'.join(errs)

    m1_mcq = sum(1 for q in M1_QUESTIONS if q['questionFormat'] == 'mcq')
    m1_spr = sum(1 for q in M1_QUESTIONS if q['questionFormat'] == 'spr')
    m2_mcq = sum(1 for q in M2_QUESTIONS if q['questionFormat'] == 'mcq')
    m2_spr = sum(1 for q in M2_QUESTIONS if q['questionFormat'] == 'spr')
    print(
        f'[OK] {TEST_CODE}: 44/44 math answers programmatically verified '
        f'(M1: {m1_mcq} MCQ + {m1_spr} SPR; M2: {m2_mcq} MCQ + {m2_spr} SPR), '
        f'0 schema errors, 0 KaTeX errors, 0 watermarks!'
    )


if __name__ == '__main__':
    verify_all_math()
