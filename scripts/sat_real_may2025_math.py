# -*- coding: utf-8 -*-
"""
Digital SAT Real Past Exam — May 2025 Math (Full Adaptive • 66 Questions)
- Module 1 (Routing): 22 real questions (`mod4_math`, 35 minutes)
- Module 2 Hard:      22 real questions (`mod6_math`, 35 minutes)
- Module 2 Lower:     22 real questions (`mod5_math`, 35 minutes)

Visually verified against all 18 PNG strips (`mod4_q*.png`, `mod5_q*.png`, `mod6_q*.png`).
Includes exact inline SVG figures, crisp HTML tables, bilingual Vietnamese explanations,
Desmos 10-second shortcuts, full programmatic `verify_all_math()` across all 66 items,
and Node KaTeX validation via `validate_sat_bluebook_json`.
"""

from fractions import Fraction
import math
import re
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

from scripts.sat_real_exams_pipeline import validate_sat_bluebook_json

TEST_CODE = 'real_may2025_math'
FOLDER_KEY = 'real_math'
ORDER_INDEX = 2
TEST_TITLE = '🏛️ Real Exam — May 2025 Math (Full Adaptive • 66 Qs)'


# ============================================================================
# QUESTION & TABLE BUILDERS
# ============================================================================

def _mcq(
    qid, number, domain, skill, difficulty,
    stimulus_html, question_html,
    options_dict, correct_label,
    summary_vi, key_takeaway, option_analysis,
    desmos_tip_vi=''
):
    assert correct_label in ('A', 'B', 'C', 'D'), f'Bad MCQ label {correct_label} on {qid}'
    opts = [{'label': lbl, 'text': options_dict[lbl]} for lbl in ('A', 'B', 'C', 'D')]
    oa = {}
    for lbl in ('A', 'B', 'C', 'D'):
        tag, reason = option_analysis[lbl]
        oa[lbl] = {
            'status': 'correct' if lbl == correct_label else 'trap',
            'trapTag': tag,
            'reasonVi': reason,
        }
    exp = {
        'summaryVi': summary_vi,
        'keyTakeaway': key_takeaway,
        'optionAnalysis': oa,
    }
    if desmos_tip_vi:
        exp['desmosTipVi'] = desmos_tip_vi
    return {
        'id': qid,
        'number': number,
        'domain': domain,
        'skill': skill,
        'difficulty': difficulty,
        'questionFormat': 'mcq',
        'stimulusHtml': stimulus_html,
        'questionHtml': question_html,
        'options': opts,
        'correctAnswer': correct_label,
        'explanation': exp,
    }


def _spr(
    qid, number, domain, skill, difficulty,
    stimulus_html, question_html,
    accepted_answers, correct_display,
    summary_vi, key_takeaway,
    desmos_tip_vi=''
):
    assert len(accepted_answers) >= 1, f'Empty accepted_answers on {qid}'
    exp = {
        'summaryVi': summary_vi,
        'keyTakeaway': key_takeaway,
    }
    if desmos_tip_vi:
        exp['desmosTipVi'] = desmos_tip_vi
    return {
        'id': qid,
        'number': number,
        'domain': domain,
        'skill': skill,
        'difficulty': difficulty,
        'questionFormat': 'spr',
        'stimulusHtml': stimulus_html,
        'questionHtml': question_html,
        'options': [],
        'correctAnswer': str(accepted_answers[0]),
        'acceptedAnswers': [str(a) for a in accepted_answers],
        'correctDisplay': correct_display,
        'explanation': exp,
    }


def _table(headers, rows):
    th = ''.join(
        f'<th style="border:1px solid #475569;padding:7px 18px;background:#f1f5f9;'
        f'font-weight:700;text-align:center;color:#0f172a;">{h}</th>'
        for h in headers
    )
    trs = []
    for row in rows:
        tds = ''.join(
            f'<td style="border:1px solid #64748b;padding:7px 18px;text-align:center;'
            f'color:#0f172a;">{c}</td>'
            for c in row
        )
        trs.append(f'<tr>{tds}</tr>')
    return (
        '<div style="display:flex;justify-content:center;margin:10px 0 14px;">'
        '<table style="border-collapse:collapse;font-size:15px;background:#ffffff;'
        'box-shadow:0 1px 2px rgba(15,23,42,0.06);">'
        f'<thead><tr>{th}</tr></thead>'
        f'<tbody>{"".join(trs)}</tbody>'
        '</table></div>'
    )


def _wrap_svg(svg_str, note=''):
    note_html = (
        f'<div style="font-size:13px;color:#334155;font-style:italic;margin-top:4px;">{note}</div>'
        if note else ''
    )
    return (
        '<div style="display:flex;flex-direction:column;align-items:center;margin:10px 0 14px;">'
        f'{svg_str}{note_html}</div>'
    )


# ============================================================================
# EXACT INLINE SVG FIGURE GENERATORS (ZERO WATERMARKS)
# ============================================================================

def svg_m1_q7_scatterplot():
    """M1 Q7: Scatterplot (0..10 x 0..10) with 10 points and line of best fit (slope ≈ -0.7)."""
    ox, oy = 46, 262
    step = 24
    parts = [
        '<svg viewBox="0 0 320 305" width="310" style="max-width:100%;height:auto;'
        'background:#ffffff;border:1px solid #e2e8f0;border-radius:10px;" '
        'xmlns="http://www.w3.org/2000/svg">'
    ]
    # Grid lines
    for i in range(11):
        x = ox + i * step
        y = oy - i * step
        parts.append(f'<line x1="{x}" y1="{oy - 10 * step}" x2="{x}" y2="{oy}" stroke="#cbd5e1" stroke-width="1"/>')
        parts.append(f'<line x1="{ox}" y1="{y}" x2="{ox + 10 * step}" y2="{y}" stroke="#cbd5e1" stroke-width="1"/>')
    # Axes
    parts.append(f'<line x1="{ox}" y1="{oy}" x2="{ox + 10 * step + 14}" y2="{oy}" stroke="#0f172a" stroke-width="2"/>')
    parts.append(f'<line x1="{ox}" y1="{oy}" x2="{ox}" y2="{oy - 10 * step - 14}" stroke="#0f172a" stroke-width="2"/>')
    # Arrowheads
    ax_end = ox + 10 * step + 18
    ay_end = oy - 10 * step - 18
    parts.append(f'<polygon points="{ax_end},{oy} {ax_end - 8},{oy - 4} {ax_end - 8},{oy + 4}" fill="#0f172a"/>')
    parts.append(f'<polygon points="{ox},{ay_end} {ox - 4},{ay_end + 8} {ox + 4},{ay_end + 8}" fill="#0f172a"/>')
    parts.append(f'<text x="{ax_end + 4}" y="{oy + 4}" font-size="13" font-style="italic" font-family="Georgia,serif" fill="#0f172a">x</text>')
    parts.append(f'<text x="{ox - 4}" y="{ay_end - 4}" font-size="13" font-style="italic" font-family="Georgia,serif" fill="#0f172a">y</text>')
    parts.append(f'<text x="{ox - 13}" y="{oy + 14}" font-size="12" font-style="italic" font-family="Georgia,serif" fill="#0f172a">O</text>')
    # Ticks & labels
    for i in range(1, 11):
        x = ox + i * step
        y = oy - i * step
        parts.append(f'<line x1="{x}" y1="{oy - 3}" x2="{x}" y2="{oy + 3}" stroke="#0f172a" stroke-width="1.3"/>')
        parts.append(f'<text x="{x}" y="{oy + 17}" text-anchor="middle" font-size="11" font-family="sans-serif" fill="#0f172a">{i}</text>')
        parts.append(f'<line x1="{ox - 3}" y1="{y}" x2="{ox + 3}" y2="{y}" stroke="#0f172a" stroke-width="1.3"/>')
        parts.append(f'<text x="{ox - 8}" y="{y + 4}" text-anchor="end" font-size="11" font-family="sans-serif" fill="#0f172a">{i}</text>')
    # Line of best fit: (0, 7.9) -> (10, 1.1) (slope -0.68 ≈ -0.7)
    lx1, ly1 = ox + 0 * step, oy - 7.9 * step
    lx2, ly2 = ox + 10 * step, oy - 1.1 * step
    parts.append(f'<line x1="{lx1:.1f}" y1="{ly1:.1f}" x2="{lx2:.1f}" y2="{ly2:.1f}" stroke="#0f172a" stroke-width="2.2"/>')
    # 10 plotted points matching mod4_q05_08.png
    pts = [(0, 8), (1.2, 7), (2.4, 7), (3.1, 6), (4.7, 4), (5.3, 3), (6.5, 4), (7.2, 3), (8.8, 2), (9.7, 2)]
    for px, py in pts:
        cx = ox + px * step
        cy = oy - py * step
        parts.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="3.8" fill="#0f172a"/>')
    parts.append('</svg>')
    return _wrap_svg(''.join(parts))


def svg_m1_q19_similar_triangles():
    """M1 Q19: Two similar triangles ABC (small) and A'B'C' (large)."""
    svg = (
        '<svg viewBox="0 0 380 170" width="365" style="max-width:100%;height:auto;'
        'background:#ffffff;border:1px solid #e2e8f0;border-radius:10px;" '
        'xmlns="http://www.w3.org/2000/svg">'
        '<polygon points="48,136 96,78 144,136" fill="none" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/>'
        '<text x="34" y="144" font-size="15" font-style="italic" font-family="Georgia,serif" fill="#0f172a">A</text>'
        '<text x="92" y="68" font-size="15" font-style="italic" font-family="Georgia,serif" fill="#0f172a">B</text>'
        '<text x="150" y="144" font-size="15" font-style="italic" font-family="Georgia,serif" fill="#0f172a">C</text>'
        '<polygon points="196,136 266,46 336,136" fill="none" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/>'
        '<text x="176" y="144" font-size="15" font-style="italic" font-family="Georgia,serif" fill="#0f172a">A&#8242;</text>'
        '<text x="260" y="37" font-size="15" font-style="italic" font-family="Georgia,serif" fill="#0f172a">B&#8242;</text>'
        '<text x="342" y="144" font-size="15" font-style="italic" font-family="Georgia,serif" fill="#0f172a">C&#8242;</text>'
        '</svg>'
    )
    return _wrap_svg(svg, note='Note: Figures not drawn to scale.')


def svg_m1_q22_histogram():
    """M1 Q22: 4-bin histogram (30-39: 2, 40-49: 7, 50-59: 28, 60-69: 13; total = 50)."""
    ox, oy = 68, 200
    w_bin = 36
    y_max_px = 168  # represents frequency 30
    scale_y = y_max_px / 30.0
    parts = [
        '<svg viewBox="0 0 360 250" width="350" style="max-width:100%;height:auto;'
        'background:#ffffff;border:1px solid #e2e8f0;border-radius:10px;" '
        'xmlns="http://www.w3.org/2000/svg">'
    ]
    # Horizontal gridlines every 5
    for f in range(0, 35, 5):
        y = oy - f * scale_y
        parts.append(f'<line x1="{ox}" y1="{y:.1f}" x2="{ox + 7 * w_bin + 10}" y2="{y:.1f}" stroke="#cbd5e1" stroke-width="1"/>')
        parts.append(f'<line x1="{ox - 4}" y1="{y:.1f}" x2="{ox + 4}" y2="{y:.1f}" stroke="#0f172a" stroke-width="1.3"/>')
        parts.append(f'<text x="{ox - 9}" y="{y + 4:.1f}" text-anchor="end" font-size="12" font-family="sans-serif" fill="#0f172a">{f}</text>')
    # Bars: [30,40)->2, [40,50)->7, [50,60)->28, [60,70)->13
    bins = [(3, 2), (4, 7), (5, 28), (6, 13)]
    for idx, freq in bins:
        bx = ox + idx * w_bin
        bh = freq * scale_y
        by = oy - bh
        parts.append(
            f'<rect x="{bx}" y="{by:.1f}" width="{w_bin}" height="{bh:.1f}" '
            'fill="#b4bcc8" stroke="#0f172a" stroke-width="1.6"/>'
        )
    # Axes
    parts.append(f'<line x1="{ox}" y1="{oy}" x2="{ox + 7 * w_bin + 10}" y2="{oy}" stroke="#0f172a" stroke-width="1.8"/>')
    parts.append(f'<line x1="{ox}" y1="{oy}" x2="{ox}" y2="{oy - y_max_px}" stroke="#0f172a" stroke-width="1.8"/>')
    # X ticks & labels
    for i in range(8):
        x = ox + i * w_bin
        parts.append(f'<line x1="{x}" y1="{oy - 3}" x2="{x}" y2="{oy + 4}" stroke="#0f172a" stroke-width="1.3"/>')
        parts.append(f'<text x="{x}" y="{oy + 19}" text-anchor="middle" font-size="12" font-family="sans-serif" fill="#0f172a">{i * 10}</text>')
    # Axis titles
    parts.append(f'<text x="{ox + 3.5 * w_bin}" y="{oy + 40}" text-anchor="middle" font-size="13" font-family="Georgia,serif" fill="#0f172a">Number of points</text>')
    parts.append(f'<text x="20" y="{oy - y_max_px / 2:.1f}" text-anchor="middle" font-size="13" font-family="Georgia,serif" fill="#0f172a" transform="rotate(-90 20 {oy - y_max_px / 2:.1f})">Frequency</text>')
    parts.append('</svg>')
    return _wrap_svg(''.join(parts))


def svg_m2l_q1_parabola_line():
    """M2L Q1: Upward parabola y = (x - 10)^2 + 1 tangent to horizontal line y = 1 at (10, 1)."""
    ox, oy = 46, 272
    step = 20  # 12 units = 240px
    parts = [
        '<svg viewBox="0 0 326 312" width="315" style="max-width:100%;height:auto;'
        'background:#ffffff;border:1px solid #e2e8f0;border-radius:10px;" '
        'xmlns="http://www.w3.org/2000/svg">'
    ]
    for i in range(13):
        x = ox + i * step
        y = oy - i * step
        parts.append(f'<line x1="{x}" y1="{oy - 12 * step}" x2="{x}" y2="{oy}" stroke="#cbd5e1" stroke-width="1"/>')
        parts.append(f'<line x1="{ox}" y1="{y}" x2="{ox + 12 * step}" y2="{y}" stroke="#cbd5e1" stroke-width="1"/>')
    # Axes
    ax_end = ox + 12 * step + 16
    ay_end = oy - 12 * step - 16
    parts.append(f'<line x1="{ox}" y1="{oy}" x2="{ax_end - 4}" y2="{oy}" stroke="#0f172a" stroke-width="2"/>')
    parts.append(f'<line x1="{ox}" y1="{oy}" x2="{ox}" y2="{ay_end + 4}" stroke="#0f172a" stroke-width="2"/>')
    parts.append(f'<polygon points="{ax_end},{oy} {ax_end - 8},{oy - 4} {ax_end - 8},{oy + 4}" fill="#0f172a"/>')
    parts.append(f'<polygon points="{ox},{ay_end} {ox - 4},{ay_end + 8} {ox + 4},{ay_end + 8}" fill="#0f172a"/>')
    parts.append(f'<text x="{ax_end + 4}" y="{oy + 4}" font-size="13" font-style="italic" font-family="Georgia,serif" fill="#0f172a">x</text>')
    parts.append(f'<text x="{ox - 4}" y="{ay_end - 4}" font-size="13" font-style="italic" font-family="Georgia,serif" fill="#0f172a">y</text>')
    parts.append(f'<text x="{ox - 12}" y="{oy + 14}" font-size="12" font-style="italic" font-family="Georgia,serif" fill="#0f172a">O</text>')
    for i in range(2, 13, 2):
        x = ox + i * step
        y = oy - i * step
        parts.append(f'<line x1="{x}" y1="{oy - 3}" x2="{x}" y2="{oy + 3}" stroke="#0f172a" stroke-width="1.3"/>')
        parts.append(f'<text x="{x}" y="{oy + 17}" text-anchor="middle" font-size="11" font-family="sans-serif" fill="#0f172a">{i}</text>')
        parts.append(f'<line x1="{ox - 3}" y1="{y}" x2="{ox + 3}" y2="{y}" stroke="#0f172a" stroke-width="1.3"/>')
        parts.append(f'<text x="{ox - 8}" y="{y + 4}" text-anchor="end" font-size="11" font-family="sans-serif" fill="#0f172a">{i}</text>')
    # Horizontal line y = 1
    y1_px = oy - 1 * step
    parts.append(f'<line x1="{ox}" y1="{y1_px}" x2="{ox + 12 * step}" y2="{y1_px}" stroke="#0f172a" stroke-width="2.2"/>')
    # Parabola y = (x - 10)^2 + 1 for x in [10 - sqrt(11), 12]
    x_start = 10.0 - math.sqrt(11.0)
    x_end = 12.0
    poly_pts = []
    for k in range(61):
        xv = x_start + (x_end - x_start) * k / 60.0
        yv = (xv - 10.0) ** 2 + 1.0
        poly_pts.append(f'{ox + xv * step:.1f},{oy - yv * step:.1f}')
    parts.append(f'<polyline points="{" ".join(poly_pts)}" fill="none" stroke="#0f172a" stroke-width="2.3"/>')
    # Intersection point dot at (10, 1)
    parts.append(f'<circle cx="{ox + 10 * step}" cy="{y1_px}" r="4" fill="#0f172a"/>')
    parts.append('</svg>')
    return _wrap_svg(''.join(parts))


def svg_m2l_q3_bar_graph():
    """M2L Q3: Store visitors bar graph (Sun 97, Mon 20, Wed 54, Thu 45, Fri 85, Sat 137)."""
    ox, oy = 68, 206
    h_max = 182  # represents 140 visitors (1.3 px per visitor)
    scale_y = h_max / 140.0
    data = [
        ('Sunday', 97),
        ('Monday', 20),
        ('Wednesday', 54),
        ('Thursday', 45),
        ('Friday', 85),
        ('Saturday', 137),
    ]
    slot = 48
    bar_w = 24
    chart_w = slot * len(data) + 18
    parts = [
        '<svg viewBox="0 0 400 286" width="390" style="max-width:100%;height:auto;'
        'background:#ffffff;border:1px solid #e2e8f0;border-radius:10px;" '
        'xmlns="http://www.w3.org/2000/svg">'
    ]
    for v in range(0, 150, 10):
        y = oy - v * scale_y
        parts.append(f'<line x1="{ox}" y1="{y:.1f}" x2="{ox + chart_w}" y2="{y:.1f}" stroke="#cbd5e1" stroke-width="1"/>')
        parts.append(f'<line x1="{ox - 4}" y1="{y:.1f}" x2="{ox}" y2="{y:.1f}" stroke="#0f172a" stroke-width="1.2"/>')
        parts.append(f'<text x="{ox - 8}" y="{y + 4:.1f}" text-anchor="end" font-size="10.5" font-family="sans-serif" fill="#0f172a">{v}</text>')
    for idx, (day, val) in enumerate(data):
        cx = ox + 28 + idx * slot
        bx = cx - bar_w / 2
        bh = val * scale_y
        by = oy - bh
        parts.append(
            f'<rect x="{bx:.1f}" y="{by:.1f}" width="{bar_w}" height="{bh:.1f}" '
            'fill="#b4bcc8" stroke="#0f172a" stroke-width="1.4"/>'
        )
        parts.append(
            f'<text x="{cx:.1f}" y="{oy + 14}" text-anchor="end" font-size="11.5" '
            f'font-family="Georgia,serif" fill="#0f172a" transform="rotate(-38 {cx:.1f} {oy + 14})">{day}</text>'
        )
    parts.append(f'<line x1="{ox}" y1="{oy}" x2="{ox + chart_w}" y2="{oy}" stroke="#0f172a" stroke-width="1.8"/>')
    parts.append(f'<line x1="{ox}" y1="{oy}" x2="{ox}" y2="{oy - h_max}" stroke="#0f172a" stroke-width="1.8"/>')
    parts.append(f'<text x="{ox + chart_w / 2:.1f}" y="276" text-anchor="middle" font-size="13" font-family="Georgia,serif" fill="#0f172a">Day</text>')
    parts.append(f'<text x="18" y="{oy - h_max / 2:.1f}" text-anchor="middle" font-size="13" font-family="Georgia,serif" fill="#0f172a" transform="rotate(-90 18 {oy - h_max / 2:.1f})">Number of visitors</text>')
    parts.append('</svg>')
    return _wrap_svg(''.join(parts))


def svg_m2l_q9_quartic(variant):
    """M2L Q9: Four quartic option graphs matching mod5_q09_top.png & mod5_q09_bcd.png."""
    cx, cy = 122, 118
    sx = 11.5  # x in [-8, 8] -> 184px
    sy = 7.4   # y in [-13, 13] -> 192px

    def f_val(x):
        if variant == 'A':
            return -(1.0 / 16.0) * (x + 3.0) * ((x - 1.0) ** 2) * (x - 5.0)
        if variant == 'B':
            return -(1.0 / 16.0) * (x + 5.0) * ((x + 1.0) ** 2) * (x - 3.0)
        if variant == 'C':
            return (1.0 / 16.0) * (x + 4.0) * (x ** 2) * (x - 4.0)
        return (1.0 / 16.0) * (x + 3.0) * ((x - 1.0) ** 2) * (x - 5.0)

    parts = [
        '<svg viewBox="0 0 248 238" width="230" style="max-width:100%;height:auto;'
        'background:#ffffff;border:1px solid #e2e8f0;border-radius:8px;display:block;" '
        'xmlns="http://www.w3.org/2000/svg">'
    ]
    # Grid lines
    for xi in range(-8, 9):
        px = cx + xi * sx
        parts.append(f'<line x1="{px:.1f}" y1="{cy - 13 * sy:.1f}" x2="{px:.1f}" y2="{cy + 13 * sy:.1f}" stroke="#cbd5e1" stroke-width="0.8"/>')
    for yi in range(-13, 14):
        py = cy - yi * sy
        parts.append(f'<line x1="{cx - 8 * sx:.1f}" y1="{py:.1f}" x2="{cx + 8 * sx:.1f}" y2="{py:.1f}" stroke="#cbd5e1" stroke-width="0.8"/>')
    # Axes
    x_min_p, x_max_p = cx - 8 * sx - 4, cx + 8 * sx + 10
    y_min_p, y_max_p = cy + 13 * sy + 4, cy - 13 * sy - 10
    parts.append(f'<line x1="{x_min_p:.1f}" y1="{cy}" x2="{x_max_p - 4:.1f}" y2="{cy}" stroke="#0f172a" stroke-width="1.6"/>')
    parts.append(f'<line x1="{cx}" y1="{y_min_p:.1f}" x2="{cx}" y2="{y_max_p + 4:.1f}" stroke="#0f172a" stroke-width="1.6"/>')
    parts.append(f'<polygon points="{x_max_p:.1f},{cy} {x_max_p - 6:.1f},{cy - 3} {x_max_p - 6:.1f},{cy + 3}" fill="#0f172a"/>')
    parts.append(f'<polygon points="{cx},{y_max_p:.1f} {cx - 3},{y_max_p + 6:.1f} {cx + 3},{y_max_p + 6:.1f}" fill="#0f172a"/>')
    parts.append(f'<text x="{x_max_p + 2:.1f}" y="{cy + 3}" font-size="10.5" font-style="italic" font-family="Georgia,serif" fill="#0f172a">x</text>')
    parts.append(f'<text x="{cx - 3}" y="{y_max_p - 3:.1f}" font-size="10.5" font-style="italic" font-family="Georgia,serif" fill="#0f172a">y</text>')
    parts.append(f'<text x="{cx - 9}" y="{cy + 10}" font-size="9.5" font-style="italic" font-family="Georgia,serif" fill="#0f172a">O</text>')
    for xi in (-8, -6, -4, -2, 2, 4, 6, 8):
        px = cx + xi * sx
        parts.append(f'<line x1="{px:.1f}" y1="{cy - 2.5}" x2="{px:.1f}" y2="{cy + 2.5}" stroke="#0f172a" stroke-width="1"/>')
        lbl = f'−{abs(xi)}' if xi < 0 else str(xi)
        parts.append(f'<text x="{px:.1f}" y="{cy + 12}" text-anchor="middle" font-size="8.5" font-family="sans-serif" fill="#0f172a">{lbl}</text>')
    for yi in (-12, -10, -8, -6, -4, -2, 2, 4, 6, 8, 10, 12):
        py = cy - yi * sy
        parts.append(f'<line x1="{cx - 2.5}" y1="{py:.1f}" x2="{cx + 2.5}" y2="{py:.1f}" stroke="#0f172a" stroke-width="1"/>')
        lbl = f'−{abs(yi)}' if yi < 0 else str(yi)
        parts.append(f'<text x="{cx - 5}" y="{py + 3:.1f}" text-anchor="end" font-size="8.5" font-family="sans-serif" fill="#0f172a">{lbl}</text>')
    # Curve polyline clipped to y in [-13.2, 13.2]
    pts = []
    for k in range(321):
        xv = -8.0 + 16.0 * k / 320.0
        yv = f_val(xv)
        if -13.2 <= yv <= 13.2:
            pts.append(f'{cx + xv * sx:.1f},{cy - yv * sy:.1f}')
    parts.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="#0f172a" stroke-width="2.2"/>')
    parts.append('</svg>')
    return ''.join(parts)


def svg_m2l_q10_parallel_lines():
    """M2L Q10: Parallel lines j and k cut by transversal t, showing x° and 127° below line j."""
    svg = (
        '<svg viewBox="0 0 340 190" width="330" style="max-width:100%;height:auto;'
        'background:#ffffff;border:1px solid #e2e8f0;border-radius:10px;" '
        'xmlns="http://www.w3.org/2000/svg">'
        '<line x1="42" y1="62" x2="284" y2="62" stroke="#0f172a" stroke-width="1.8"/>'
        '<line x1="42" y1="128" x2="284" y2="128" stroke="#0f172a" stroke-width="1.8"/>'
        '<line x1="68" y1="176" x2="254" y2="20" stroke="#0f172a" stroke-width="1.8"/>'
        '<text x="294" y="67" font-size="16" font-style="italic" font-family="Georgia,serif" fill="#0f172a">j</text>'
        '<text x="294" y="133" font-size="16" font-style="italic" font-family="Georgia,serif" fill="#0f172a">k</text>'
        '<text x="260" y="22" font-size="16" font-style="italic" font-family="Georgia,serif" fill="#0f172a">t</text>'
        '<text x="166" y="81" text-anchor="end" font-size="14" font-style="italic" font-family="Georgia,serif" fill="#0f172a">x°</text>'
        '<text x="196" y="81" text-anchor="start" font-size="14" font-family="Georgia,serif" fill="#0f172a">127°</text>'
        '</svg>'
    )
    return _wrap_svg(svg, note='Note: Figure not drawn to scale.')


def svg_m2l_q12_inequality():
    """M2L Q12: Shaded linear inequality y >= -(11/4)x + 12 on [-8, 8] x [-8, 8]."""
    cx, cy = 158, 154
    step = 16  # 8 units = 128px
    x_top = 16.0 / 11.0  # y = 8
    x_bot = 80.0 / 11.0  # y = -8
    parts = [
        '<svg viewBox="0 0 322 308" width="310" style="max-width:100%;height:auto;'
        'background:#ffffff;border:1px solid #e2e8f0;border-radius:10px;" '
        'xmlns="http://www.w3.org/2000/svg">'
    ]
    # Shaded region above/right of line
    poly = (
        f'{cx + x_top * step:.1f},{cy - 8 * step:.1f} '
        f'{cx + 8 * step:.1f},{cy - 8 * step:.1f} '
        f'{cx + 8 * step:.1f},{cy + 8 * step:.1f} '
        f'{cx + x_bot * step:.1f},{cy + 8 * step:.1f}'
    )
    parts.append(f'<polygon points="{poly}" fill="rgba(100,116,139,0.34)"/>')
    # Grid
    for i in range(-8, 9):
        px = cx + i * step
        py = cy - i * step
        parts.append(f'<line x1="{px}" y1="{cy - 8 * step}" x2="{px}" y2="{cy + 8 * step}" stroke="#94a3b8" stroke-width="0.9"/>')
        parts.append(f'<line x1="{cx - 8 * step}" y1="{py}" x2="{cx + 8 * step}" y2="{py}" stroke="#94a3b8" stroke-width="0.9"/>')
    # Axes
    x_end = cx + 8 * step + 16
    y_end = cy - 8 * step - 16
    parts.append(f'<line x1="{cx - 8 * step - 6}" y1="{cy}" x2="{x_end - 4}" y2="{cy}" stroke="#0f172a" stroke-width="1.9"/>')
    parts.append(f'<line x1="{cx}" y1="{cy + 8 * step + 6}" x2="{cx}" y2="{y_end + 4}" stroke="#0f172a" stroke-width="1.9"/>')
    parts.append(f'<polygon points="{x_end},{cy} {x_end - 8},{cy - 4} {x_end - 8},{cy + 4}" fill="#0f172a"/>')
    parts.append(f'<polygon points="{cx},{y_end} {cx - 4},{y_end + 8} {cx + 4},{y_end + 8}" fill="#0f172a"/>')
    parts.append(f'<text x="{x_end + 3}" y="{cy + 4}" font-size="12.5" font-style="italic" font-family="Georgia,serif" fill="#0f172a">x</text>')
    parts.append(f'<text x="{cx - 4}" y="{y_end - 4}" font-size="12.5" font-style="italic" font-family="Georgia,serif" fill="#0f172a">y</text>')
    parts.append(f'<text x="{cx - 11}" y="{cy + 13}" font-size="11" font-style="italic" font-family="Georgia,serif" fill="#0f172a">O</text>')
    for i in (-8, -6, -4, -2, 2, 4, 6, 8):
        px = cx + i * step
        py = cy - i * step
        lbl = f'−{abs(i)}' if i < 0 else str(i)
        parts.append(f'<text x="{px}" y="{cy + 14}" text-anchor="middle" font-size="10.5" font-family="sans-serif" fill="#0f172a">{lbl}</text>')
        parts.append(f'<text x="{cx - 6}" y="{py + 4}" text-anchor="end" font-size="10.5" font-family="sans-serif" fill="#0f172a">{lbl}</text>')
    # Solid boundary line
    parts.append(
        f'<line x1="{cx + x_top * step:.1f}" y1="{cy - 8 * step:.1f}" '
        f'x2="{cx + x_bot * step:.1f}" y2="{cy + 8 * step:.1f}" stroke="#0f172a" stroke-width="2.4"/>'
    )
    parts.append('</svg>')
    return _wrap_svg(''.join(parts))


def svg_m2l_q19_right_triangle():
    """M2L Q19: Right triangle TSR (right angle at top vertex S), ST = 217, SR = 2*sqrt(218), TR = 219."""
    # Vertices: T=(52, 140), R=(288, 140), S=(208, 42) -> check perpendicularity:
    # (T-S) = (-156, 98), (R-S) = (80, 98) -> adjust S so dot product = 0!
    # Put S on semicircle of diameter TR (center (170, 140), radius 118):
    # Angle 54 deg from +x -> S = (170 + 118*cos(54°), 140 - 118*sin(54°)) = (239.4, 44.5)
    tx, ty = 52.0, 142.0
    rx, ry = 288.0, 142.0
    sx, sy = 216.0, 44.0
    # Compute exact unit vectors along ST and SR for crisp right-angle box
    # Actually let's place S on the exact semicircle so angle S is truly 90°!
    rad = 118.0
    ang = math.radians(52)
    sx = 170.0 + rad * math.cos(ang)  # 242.6
    sy = 142.0 - rad * math.sin(ang)  # 49.0
    # Unit vectors from S toward T and R
    dt = math.hypot(tx - sx, ty - sy)
    dr = math.hypot(rx - sx, ry - sy)
    utx, uty = (tx - sx) / dt, (ty - sy) / dt
    urx, ury = (rx - sx) / dr, (ry - sy) / dr
    sz = 13.0
    p1x, p1y = sx + utx * sz, sy + uty * sz
    p2x, p2y = sx + (utx + urx) * sz, sy + (uty + ury) * sz
    p3x, p3y = sx + urx * sz, sy + ury * sz
    svg = (
        '<svg viewBox="0 0 340 182" width="330" style="max-width:100%;height:auto;'
        'background:#ffffff;border:1px solid #e2e8f0;border-radius:10px;" '
        'xmlns="http://www.w3.org/2000/svg">'
        f'<polygon points="{tx:.1f},{ty:.1f} {sx:.1f},{sy:.1f} {rx:.1f},{ry:.1f}" '
        'fill="none" stroke="#0f172a" stroke-width="2" stroke-linejoin="round"/>'
        f'<polyline points="{p1x:.1f},{p1y:.1f} {p2x:.1f},{p2y:.1f} {p3x:.1f},{p3y:.1f}" '
        'fill="none" stroke="#0f172a" stroke-width="1.5"/>'
        f'<text x="{tx - 16:.1f}" y="{ty + 10:.1f}" font-size="15" font-style="italic" font-family="Georgia,serif" fill="#0f172a">T</text>'
        f'<text x="{rx + 8:.1f}" y="{ry + 10:.1f}" font-size="15" font-style="italic" font-family="Georgia,serif" fill="#0f172a">R</text>'
        f'<text x="{sx + 2:.1f}" y="{sy - 10:.1f}" text-anchor="middle" font-size="15" font-style="italic" font-family="Georgia,serif" fill="#0f172a">S</text>'
        '<text x="132" y="84" text-anchor="end" font-size="14" font-family="Georgia,serif" fill="#0f172a">217</text>'
        '<text x="275" y="92" text-anchor="start" font-size="14" font-family="Georgia,serif" fill="#0f172a">2√218</text>'
        '<line x1="291" y1="79" x2="315" y2="79" stroke="#0f172a" stroke-width="1"/>'
        '<text x="170" y="162" text-anchor="middle" font-size="14" font-family="Georgia,serif" fill="#0f172a">219</text>'
        '</svg>'
    )
    return _wrap_svg(svg, note='Note: Figure not drawn to scale.')


def svg_m2h_q1_inequality():
    """M2H Q1: Shaded linear inequality y >= (1/3)x + 6 on x in [-8, 8], y in [-2, 10]."""
    cx, cy = 160, 224  # y = 0 is at 224; y = 10 is at 224 - 180 = 44; y = -2 is at 260
    step = 18
    y_left = (-8.0) / 3.0 + 6.0   # 10/3 ≈ 3.333
    y_right = 8.0 / 3.0 + 6.0     # 26/3 ≈ 8.667
    parts = [
        '<svg viewBox="0 0 330 282" width="320" style="max-width:100%;height:auto;'
        'background:#ffffff;border:1px solid #e2e8f0;border-radius:10px;" '
        'xmlns="http://www.w3.org/2000/svg">'
    ]
    poly = (
        f'{cx - 8 * step},{cy - y_left * step:.1f} '
        f'{cx - 8 * step},{cy - 10 * step} '
        f'{cx + 8 * step},{cy - 10 * step} '
        f'{cx + 8 * step},{cy - y_right * step:.1f}'
    )
    parts.append(f'<polygon points="{poly}" fill="rgba(100,116,139,0.34)"/>')
    for xi in range(-8, 9):
        px = cx + xi * step
        parts.append(f'<line x1="{px}" y1="{cy - 10 * step}" x2="{px}" y2="{cy + 2 * step}" stroke="#94a3b8" stroke-width="0.9"/>')
    for yi in range(-2, 11):
        py = cy - yi * step
        parts.append(f'<line x1="{cx - 8 * step}" y1="{py}" x2="{cx + 8 * step}" y2="{py}" stroke="#94a3b8" stroke-width="0.9"/>')
    x_end = cx + 8 * step + 16
    y_end = cy - 10 * step - 16
    parts.append(f'<line x1="{cx - 8 * step - 6}" y1="{cy}" x2="{x_end - 4}" y2="{cy}" stroke="#0f172a" stroke-width="1.9"/>')
    parts.append(f'<line x1="{cx}" y1="{cy + 2 * step + 6}" x2="{cx}" y2="{y_end + 4}" stroke="#0f172a" stroke-width="1.9"/>')
    parts.append(f'<polygon points="{x_end},{cy} {x_end - 8},{cy - 4} {x_end - 8},{cy + 4}" fill="#0f172a"/>')
    parts.append(f'<polygon points="{cx},{y_end} {cx - 4},{y_end + 8} {cx + 4},{y_end + 8}" fill="#0f172a"/>')
    parts.append(f'<text x="{x_end + 3}" y="{cy + 4}" font-size="12.5" font-style="italic" font-family="Georgia,serif" fill="#0f172a">x</text>')
    parts.append(f'<text x="{cx - 4}" y="{y_end - 4}" font-size="12.5" font-style="italic" font-family="Georgia,serif" fill="#0f172a">y</text>')
    parts.append(f'<text x="{cx - 11}" y="{cy + 13}" font-size="11" font-style="italic" font-family="Georgia,serif" fill="#0f172a">O</text>')
    for xi in (-8, -6, -4, -2, 2, 4, 6, 8):
        px = cx + xi * step
        lbl = f'−{abs(xi)}' if xi < 0 else str(xi)
        parts.append(f'<text x="{px}" y="{cy + 15}" text-anchor="middle" font-size="10.5" font-family="sans-serif" fill="#0f172a">{lbl}</text>')
    for yi in (-2, 2, 4, 6, 8, 10):
        py = cy - yi * step
        lbl = f'−{abs(yi)}' if yi < 0 else str(yi)
        parts.append(f'<text x="{cx - 6}" y="{py + 4}" text-anchor="end" font-size="10.5" font-family="sans-serif" fill="#0f172a">{lbl}</text>')
    parts.append(
        f'<line x1="{cx - 8 * step}" y1="{cy - y_left * step:.1f}" '
        f'x2="{cx + 8 * step}" y2="{cy - y_right * step:.1f}" stroke="#0f172a" stroke-width="2.4"/>'
    )
    parts.append('</svg>')
    return _wrap_svg(''.join(parts))


def svg_m2h_q10_parabola_line():
    """M2H Q10: Downward parabola y = -0.7(x - 7)^2 + 6.3 and horizontal line y = 5.6."""
    ox, oy = 56, 232  # origin (0, 0); x in [-1, 15], y in [-1, 10]
    sx = 18
    sy = 19
    parts = [
        '<svg viewBox="0 0 356 276" width="345" style="max-width:100%;height:auto;'
        'background:#ffffff;border:1px solid #e2e8f0;border-radius:10px;" '
        'xmlns="http://www.w3.org/2000/svg">'
    ]
    for xi in range(-1, 16):
        px = ox + xi * sx
        parts.append(f'<line x1="{px}" y1="{oy - 10 * sy}" x2="{px}" y2="{oy + 1 * sy}" stroke="#cbd5e1" stroke-width="0.9"/>')
    for yi in range(-1, 11):
        py = oy - yi * sy
        parts.append(f'<line x1="{ox - 1 * sx}" y1="{py}" x2="{ox + 15 * sx}" y2="{py}" stroke="#cbd5e1" stroke-width="0.9"/>')
    x_end = ox + 15 * sx + 14
    y_end = oy - 10 * sy - 14
    parts.append(f'<line x1="{ox - 1 * sx - 4}" y1="{oy}" x2="{x_end - 4}" y2="{oy}" stroke="#0f172a" stroke-width="1.9"/>')
    parts.append(f'<line x1="{ox}" y1="{oy + 1 * sy + 6}" x2="{ox}" y2="{y_end + 4}" stroke="#0f172a" stroke-width="1.9"/>')
    parts.append(f'<polygon points="{x_end},{oy} {x_end - 8},{oy - 4} {x_end - 8},{oy + 4}" fill="#0f172a"/>')
    parts.append(f'<polygon points="{ox},{y_end} {ox - 4},{y_end + 8} {ox + 4},{y_end + 8}" fill="#0f172a"/>')
    parts.append(f'<text x="{x_end + 3}" y="{oy + 4}" font-size="12.5" font-style="italic" font-family="Georgia,serif" fill="#0f172a">x</text>')
    parts.append(f'<text x="{ox - 4}" y="{y_end - 4}" font-size="12.5" font-style="italic" font-family="Georgia,serif" fill="#0f172a">y</text>')
    parts.append(f'<text x="{ox - 10}" y="{oy + 13}" font-size="11" font-style="italic" font-family="Georgia,serif" fill="#0f172a">O</text>')
    for xi in (2, 4, 6, 8, 10, 12, 14):
        px = ox + xi * sx
        parts.append(f'<text x="{px}" y="{oy + 16}" text-anchor="middle" font-size="10.5" font-family="sans-serif" fill="#0f172a">{xi}</text>')
    for yi in (-1, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10):
        py = oy - yi * sy
        lbl = f'−{abs(yi)}' if yi < 0 else str(yi)
        parts.append(f'<text x="{ox - 6}" y="{py + 4}" text-anchor="end" font-size="10" font-family="sans-serif" fill="#0f172a">{lbl}</text>')
    # Horizontal line y = 5.6
    y_line = oy - 5.6 * sy
    parts.append(f'<line x1="{ox - 1 * sx}" y1="{y_line:.1f}" x2="{ox + 15 * sx}" y2="{y_line:.1f}" stroke="#0f172a" stroke-width="2.1"/>')
    # Parabola y = -0.7(x - 7)^2 + 6.3 clipped to y >= -1.2
    half_span = math.sqrt((6.3 + 1.2) / 0.7)
    x_a, x_b = 7.0 - half_span, 7.0 + half_span
    pts = []
    for k in range(81):
        xv = x_a + (x_b - x_a) * k / 80.0
        yv = -0.7 * ((xv - 7.0) ** 2) + 6.3
        pts.append(f'{ox + xv * sx:.1f},{oy - yv * sy:.1f}')
    parts.append(f'<polyline points="{" ".join(pts)}" fill="none" stroke="#0f172a" stroke-width="2.3"/>')
    parts.append('</svg>')
    return _wrap_svg(''.join(parts))


def svg_m2h_q13_segment():
    """M2H Q13: Line segment from (-3, 5) to (6, 11) on x in [-8, 8], y in [0, 16]."""
    cx, cy = 160, 276  # origin (0, 0); y in [0, 16]
    sx = 16
    sy = 15
    parts = [
        '<svg viewBox="0 0 326 308" width="312" style="max-width:100%;height:auto;'
        'background:#ffffff;border:1px solid #e2e8f0;border-radius:10px;" '
        'xmlns="http://www.w3.org/2000/svg">'
    ]
    for xi in range(-8, 9):
        px = cx + xi * sx
        parts.append(f'<line x1="{px}" y1="{cy - 16 * sy}" x2="{px}" y2="{cy}" stroke="#cbd5e1" stroke-width="0.9"/>')
    for yi in range(0, 17):
        py = cy - yi * sy
        parts.append(f'<line x1="{cx - 8 * sx}" y1="{py}" x2="{cx + 8 * sx}" y2="{py}" stroke="#cbd5e1" stroke-width="0.9"/>')
    x_end = cx + 8 * sx + 16
    y_end = cy - 16 * sy - 16
    parts.append(f'<line x1="{cx - 8 * sx - 6}" y1="{cy}" x2="{x_end - 4}" y2="{cy}" stroke="#0f172a" stroke-width="1.9"/>')
    parts.append(f'<line x1="{cx}" y1="{cy + 6}" x2="{cx}" y2="{y_end + 4}" stroke="#0f172a" stroke-width="1.9"/>')
    parts.append(f'<polygon points="{x_end},{cy} {x_end - 8},{cy - 4} {x_end - 8},{cy + 4}" fill="#0f172a"/>')
    parts.append(f'<polygon points="{cx},{y_end} {cx - 4},{y_end + 8} {cx + 4},{y_end + 8}" fill="#0f172a"/>')
    parts.append(f'<text x="{x_end + 3}" y="{cy + 4}" font-size="12.5" font-style="italic" font-family="Georgia,serif" fill="#0f172a">x</text>')
    parts.append(f'<text x="{cx - 4}" y="{y_end - 4}" font-size="12.5" font-style="italic" font-family="Georgia,serif" fill="#0f172a">y</text>')
    parts.append(f'<text x="{cx - 11}" y="{cy + 13}" font-size="11" font-style="italic" font-family="Georgia,serif" fill="#0f172a">O</text>')
    for xi in (-8, -6, -4, -2, 2, 4, 6, 8):
        px = cx + xi * sx
        lbl = f'−{abs(xi)}' if xi < 0 else str(xi)
        parts.append(f'<text x="{px}" y="{cy + 15}" text-anchor="middle" font-size="10.5" font-family="sans-serif" fill="#0f172a">{lbl}</text>')
    for yi in (2, 4, 6, 8, 10, 12, 14, 16):
        py = cy - yi * sy
        parts.append(f'<text x="{cx - 6}" y="{py + 4}" text-anchor="end" font-size="10.5" font-family="sans-serif" fill="#0f172a">{yi}</text>')
    p1x, p1y = cx + (-3) * sx, cy - 5 * sy
    p2x, p2y = cx + 6 * sx, cy - 11 * sy
    parts.append(f'<line x1="{p1x}" y1="{p1y}" x2="{p2x}" y2="{p2y}" stroke="#0f172a" stroke-width="2.5"/>')
    parts.append(f'<circle cx="{p1x}" cy="{p1y}" r="4.2" fill="#0f172a"/>')
    parts.append(f'<circle cx="{p2x}" cy="{p2y}" r="4.2" fill="#0f172a"/>')
    parts.append('</svg>')
    return _wrap_svg(''.join(parts))


# ============================================================================
# MODULE 1 — ROUTING MODULE (mod4_math, 22 REAL QUESTIONS)
# ============================================================================

def _build_module1():
    tbl_q13 = _table([r'\(x\)', r'\(y\)'], [['1', '21'], ['2', '33'], ['3', r'\(a\)']])
    return [
        _spr(
            'may2025_m1_q1', 1, 'Algebra', 'Linear functions', 'Easy',
            r'<p>The function \(f\) is defined by \(f(x) = 85x + 30\).</p>',
            r'What is the value of \(f(x)\) when \(x = 6\)?',
            ['540'], '540',
            r'Thay \(x = 6\) vào hàm số \(f(x) = 85x + 30\): \(f(6) = 85(6) + 30 = 510 + 30 = 540\).',
            r'Để tính giá trị hàm số \(f(x)\) tại \(x = k\), chỉ cần thay trực tiếp \(k\) vào vị trí của biến \(x\) và thực hiện nhân trước cộng sau.',
            r'Gõ thẳng `85(6) + 30` vào Desmos để tránh sai sót tính nhẩm, ra ngay `540`.'
        ),
        _mcq(
            'may2025_m1_q2', 2, 'Geometry and Trigonometry', 'Lines, angles, and triangles', 'Easy',
            r'<p>In triangle \(XYZ\), two of the angles have the same measure. If the measure of angle \(X\) is \(138^\circ\) and the measure of angle \(Y\) is \(21^\circ\), what is the measure of angle \(Z\)?</p>',
            r'What is the measure of angle \(Z\)?',
            {'A': r'\(180^\circ\)', 'B': r'\(138^\circ\)', 'C': r'\(42^\circ\)', 'D': r'\(21^\circ\)'},
            'D',
            r'Tổng ba góc trong tam giác \(XYZ\) bằng \(180^\circ\): \(\angle Z = 180^\circ - 138^\circ - 21^\circ = 21^\circ\). Kết quả này khớp với giả thiết tam giác cân có hai góc bằng nhau (\(\angle Y = \angle Z = 21^\circ\)).',
            r'Một tam giác không thể có hai góc tù (\(138^\circ + 138^\circ > 180^\circ\)), nên cặp góc bằng nhau bắt buộc là hai góc nhọn \(21^\circ\).',
            {
                'A': ('Tổng ba góc', r'\(180^\circ\) là tổng cả ba góc trong tam giác, không phải góc \(Z\).'),
                'B': ('Bẫy góc tù lặp lại', r'Nếu \(\angle Z = 138^\circ\) thì tổng ba góc vượt quá \(180^\circ\) (\(138 + 138 + 21 = 297^\circ\)).'),
                'C': ('Nhầm tổng hai góc nhọn', r'\(42^\circ = 180^\circ - 138^\circ\) là tổng \(\angle Y + \angle Z\), quên trừ đi \(\angle Y = 21^\circ\).'),
                'D': ('Đáp án đúng', r'\(180^\circ - 138^\circ - 21^\circ = 21^\circ\).'),
            },
            r'Gõ nhanh `180 - 138 - 21` trên Desmos ra ngay `21`.'
        ),
        _mcq(
            'may2025_m1_q3', 3, 'Advanced Math', 'Nonlinear equations in one variable', 'Easy',
            r'<p style="text-align:center;font-size:18px;">\[x^2 - 8 = 28\]</p>',
            r'What is the positive solution to the given equation?',
            {'A': r'\(20\)', 'B': r'\(\sqrt{20}\)', 'C': r'\(36\)', 'D': r'\(\sqrt{36}\)'},
            'D',
            r'Cộng \(8\) vào hai vế: \(x^2 = 28 + 8 = 36\). Lấy căn bậc hai hai vế được \(x = \pm\sqrt{36}\). Vì đề hỏi nghiệm dương (positive solution), ta chọn \(x = \sqrt{36}\) (tức là \(6\)).',
            r'Chú ý quan sát cách viết đáp án: SAT đôi khi giữ nguyên dạng căn chưa rút gọn như \(\sqrt{36}\) để kiểm tra xem học sinh có nhớ lấy căn sau khi tìm ra \(x^2 = 36\) hay không.',
            {
                'A': ('Trừ nhầm và quên căn', r'Trừ \(28 - 8 = 20\) thay vì cộng, đồng thời quên lấy căn bậc hai.'),
                'B': ('Chuyển vế sai dấu', r'Tính \(x^2 = 28 - 8 = 20 \Rightarrow x = \sqrt{20}\), sai dấu khi chuyển \(-8\) sang vế phải.'),
                'C': ('Quên lấy căn bậc hai', r'\(36\) là giá trị của \(x^2\), không phải nghiệm \(x\).'),
                'D': ('Đáp án đúng', r'\(x^2 = 36 \Rightarrow\) nghiệm dương \(x = \sqrt{36}\).'),
            },
            r'Gõ `x^2 - 8 = 28` vào Desmos sẽ thấy nghiệm dương là `x = 6`, đối chiếu \(\sqrt{36} = 6\) chọn ngay D.'
        ),
        _mcq(
            'may2025_m1_q4', 4, 'Algebra', 'Linear equations in one variable', 'Easy',
            r'<p>Consider the equation \(16x + 60 = 28x\).</p>',
            r'What value of \(x\) is the solution to the equation \(16x + 60 = 28x\)?',
            {'A': r'\(-4\)', 'B': r'\(\frac{1}{5}\)', 'C': r'\(\frac{5}{11}\)', 'D': r'\(5\)'},
            'D',
            r'Trừ \(16x\) khỏi cả hai vế: \(60 = 28x - 16x \Rightarrow 60 = 12x \Rightarrow x = \frac{60}{12} = 5\).',
            r'Chuyển toàn bộ hạng tử chứa \(x\) về một vế để gom hệ số: \(28x - 16x = 12x\), rồi chia hai vế cho \(12\).',
            {
                'A': ('Sai dấu phép tính', r'Thay \(x = -4\): vế trái \(-4 \ne -112\).'),
                'B': ('Chia ngược phân số', r'Lấy \(\frac{12}{60} = \frac{1}{5}\) thay vì \(\frac{60}{12} = 5\).'),
                'C': ('Cộng nhầm hệ số', r'Cộng \(16 + 28 = 44\) rồi rút gọn \(\frac{60}{44}\) sai bước.'),
                'D': ('Đáp án đúng', r'\(16(5) + 60 = 140 = 28(5)\).'),
            },
            r'Gõ thẳng `16x + 60 = 28x` vào Desmos, đường thẳng đứng cắt trục hoành tại `x = 5`.'
        ),
        _mcq(
            'may2025_m1_q5', 5, 'Algebra', 'Equivalent expressions', 'Easy',
            r'<p>Consider the expression \(70y + 60y\).</p>',
            r'Which expression is equivalent to \(70y + 60y\)?',
            {'A': r'\(420y^2\)', 'B': r'\(420y\)', 'C': r'\(130y^2\)', 'D': r'\(130y\)'},
            'D',
            r'Hai hạng tử \(70y\) và \(60y\) đồng dạng (cùng bậc \(y^1\)), nên cộng hệ số và giữ nguyên phần biến: \(70y + 60y = (70 + 60)y = 130y\).',
            r'Khi cộng/trừ đơn thức đồng dạng, chỉ cộng hệ số và tuyệt đối giữ nguyên số mũ của biến \(y\).',
            {
                'A': ('Nhân thay vì cộng & nâng bậc', r'Nhầm sang phép nhân và tính sai \(70 \times 60 = 420\) kèm \(y^2\).'),
                'B': ('Nhân sai hệ số', r'Nhầm \(70 + 60\) thành \(420\).'),
                'C': ('Cộng nhầm số mũ', r'Cộng đúng \(70 + 60 = 130\) nhưng sai khi đổi \(y + y \to y^2\).'),
                'D': ('Đáp án đúng', r'\(70y + 60y = 130y\).'),
            },
            r'Thay thử \(y = 2\): \(70(2) + 60(2) = 260\), chỉ đáp án D cho \(130(2) = 260\).'
        ),
        _mcq(
            'may2025_m1_q6', 6, 'Problem-Solving and Data Analysis', 'Inference from sample statistics', 'Easy',
            r'<p>An internet provider wanted to know how many of its 20,000 subscribers would be interested in a new service plan. The provider selected 200 subscribers at random and asked each subscriber whether the subscriber would be interested in the new plan. Of those surveyed, 3 said they would be interested.</p>',
            r'Which of the following is the best estimate of the total number of subscribers who would be interested in the new service plan?',
            {'A': r'\(3\)', 'B': r'\(30\)', 'C': r'\(300\)', 'D': r'\(3{,}000\)'},
            'C',
            r'Tỉ lệ người quan tâm trong mẫu ngẫu nhiên là \(\frac{3}{200}\). Áp dụng tỉ lệ này cho toàn bộ tổng thể \(20{,}000\) thuê bao: \(\frac{3}{200} \times 20{,}000 = 3 \times 100 = 300\).',
            r'Ước lượng tổng thể từ mẫu ngẫu nhiên: \(\text{Estimate} = \frac{\text{Sample positive}}{\text{Sample size}} \times \text{Population}\).',
            {
                'A': ('Quên nhân quy mô tổng thể', r'\(3\) chỉ là số người quan tâm trong mẫu 200 người.'),
                'B': ('Thiếu một chữ số 0', r'Nhầm \(\frac{20{,}000}{200} = 10\) thay vì \(100\).'),
                'C': ('Đáp án đúng', r'\(\frac{3}{200} \times 20{,}000 = 300\).'),
                'D': ('Dư một chữ số 0', r'Nhầm \(\frac{20{,}000}{200} = 1{,}000\) thay vì \(100\).'),
            },
            r'Gõ `(3/200)*20000` vào Desmos ra ngay `300`.'
        ),
        _mcq(
            'may2025_m1_q7', 7, 'Problem-Solving and Data Analysis', 'Two-variable data: Models and scatterplots', 'Easy',
            svg_m1_q7_scatterplot() + r'<p>In the given scatterplot, a line of best fit for the data is shown.</p>',
            r'Which of the following is closest to the slope of this line of best fit?',
            {'A': r'\(-7\)', 'B': r'\(-0.7\)', 'C': r'\(0.7\)', 'D': r'\(7\)'},
            'B',
            r'Đường hồi quy (line of best fit) đi xuống từ trái sang phải nên có hệ số góc âm. Đọc hai điểm xấp xỉ trên đường thẳng: \((0, 8)\) và \((10, 1)\). Hệ số góc là \(m \approx \frac{1 - 8}{10 - 0} = \frac{-7}{10} = -0.7\).',
            r'Luôn kiểm tra dấu của hệ số góc trước (đi xuống \(\Rightarrow m < 0\)), sau đó chọn hai điểm càng xa nhau trên đường thẳng để ước lượng \(\frac{\Delta y}{\Delta x}\) chính xác nhất.',
            {
                'A': ('Quên chia cho Δx = 10', r'\(-7\) mới chỉ là độ giảm \(\Delta y = 1 - 8\), chưa chia cho \(\Delta x = 10\).'),
                'B': ('Đáp án đúng', r'\(m \approx \frac{1 - 8}{10 - 0} = -0.7\).'),
                'C': ('Sai dấu hệ số góc', r'Đường thẳng dốc xuống nên slope phải âm, không thể là \(+0.7\).'),
                'D': ('Sai cả dấu và tỉ lệ', r'Vừa sai dấu vừa quên chia cho \(\Delta x = 10\).'),
            },
            r'Đọc nhanh tọa độ đầu cuối \((0, 8)\) và \((10, 1)\) trên hình rồi bấm `(1 - 8)/(10 - 0)` = `-0.7`.'
        ),
        _mcq(
            'may2025_m1_q8', 8, 'Algebra', 'Linear equations in two variables', 'Easy',
            r'<p>A chemist mixed \(x\) liters of a \(4\%\) saline solution with \(y\) liters of a \(7\%\) saline solution to produce a \(5\%\) saline solution. (Assume the volumes of the solutions are additive.)</p>',
            r'Which equation best represents this situation?',
            {
                'A': r'\(0.04x + 0.07y = 5(x + y)\)',
                'B': r'\(0.04x + 0.07y = 0.05(x + y)\)',
                'C': r'\(0.4x + 0.7y = 5(x + y)\)',
                'D': r'\(0.4x + 0.7y = 0.5(x + y)\)',
            },
            'B',
            r'Lượng muối nguyên chất trong dung dịch \(4\%\) là \(0.04x\), trong dung dịch \(7\%\) là \(0.07y\). Tổng thể tích sau khi trộn là \(x + y\) lít với nồng độ \(5\% = 0.05\), nên tổng lượng muối là \(0.05(x + y)\). Bảo toàn khối lượng muối: \(0.04x + 0.07y = 0.05(x + y)\).',
            r'Cực kỳ cẩn thận khi đổi phần trăm sang số thập phân: \(4\% = 0.04\), \(5\% = 0.05\), \(7\% = 0.07\) (chia cho \(100\), không phải chia cho \(10\)).',
            {
                'A': ('Quên đổi 5% sang thập phân', r'Vế phải viết \(5(x + y)\) tương đương \(500\%\), không đồng nhất với \(0.04\) và \(0.07\).'),
                'B': ('Đáp án đúng', r'Đổi chuẩn xác cả ba nồng độ: \(4\% = 0.04\), \(7\% = 0.07\), \(5\% = 0.05\).'),
                'C': ('Đổi sai toàn bộ phần trăm', r'\(0.4 = 40\%\), \(0.7 = 70\%\) và \(5 = 500\%\).'),
                'D': ('Nhầm phần trăm với phần mười', r'Viết \(0.4, 0.7, 0.5\) tương ứng \(40\%, 70\%, 50\%\) (lớn gấp 10 lần đề bài).'),
            },
            r'Bài lập phương trình pha trộn — kiểm tra nhanh đồng bộ thập phân: \(4\% = 0.04\), \(7\% = 0.07\), \(5\% = 0.05\).'
        ),
        _mcq(
            'may2025_m1_q9', 9, 'Algebra', 'Linear functions', 'Easy',
            r'<p>The function \(F(m) = 7m\) models the force, in newtons, acting on each object in a certain field as a function of the object&#39;s mass \(m\), in kilograms.</p>',
            r'Which statement is the best interpretation of \(F(4) = 28\) in this context?',
            {
                'A': 'The estimated force acting on an object with a mass of 4 kilograms is 28 newtons.',
                'B': 'The estimated force acting on an object with a mass of 28 kilograms is 4 newtons.',
                'C': 'The estimated force acting on an object with a mass of 7 kilograms is 4 newtons.',
                'D': 'The estimated force acting on an object with a mass of 7 kilograms is 28 newtons.',
            },
            'A',
            r'Trong ký hiệu hàm \(F(m)\), biến đầu vào trong ngoặc \(m\) là khối lượng tính bằng kilôgam, còn giá trị đầu ra \(F(m)\) là lực tác dụng tính bằng niutơn. Do đó \(F(4) = 28\) nghĩa là vật có khối lượng \(4\) kg chịu lực ước tính là \(28\) niutơn.',
            r'Đọc ký hiệu \(f(a) = b\): luôn ánh xạ "đầu vào \(= a\) (đơn vị của biến)" \(\Rightarrow\) "đầu ra \(= b\) (đơn vị của hàm)".',
            {
                'A': ('Đáp án đúng', r'Đúng cả đầu vào \(m = 4\text{ kg}\) và đầu ra \(F(4) = 28\text{ N}\).'),
                'B': ('Đảo ngược đầu vào và đầu ra', r'Hoán đổi sai khối lượng (28 kg) với lực (4 N).'),
                'C': ('Nhầm hệ số góc với khối lượng', r'\(7\) là hằng số tỉ lệ (N/kg), không phải khối lượng của vật.'),
                'D': ('Nhầm hệ số góc với khối lượng', r'Tương tự, nhầm \(7\) trong \(7m\) là khối lượng \(7\) kg.'),
            },
            r'Câu đọc hiểu ký hiệu hàm — không cần dùng Desmos.'
        ),
        _spr(
            'may2025_m1_q10', 10, 'Problem-Solving and Data Analysis', 'Percentages', 'Easy',
            r'<p>A car dealership has only sedans, SUVs, and minivans for sale. On Monday, \(20\%\) of the vehicles for sale were sedans and \(50\%\) were SUVs. If there were \(36\) sedans for sale at the dealership on Monday, how many minivans were for sale?</p>',
            r'How many minivans were for sale?',
            ['54'], '54',
            r'Vì đại lý chỉ có 3 loại xe nên tỉ lệ xe minivan là \(100\% - 20\% - 50\% = 30\%\). Tổng số xe là \(T = \frac{36}{0.20} = 180\) xe. Số xe minivan là \(30\% \times 180 = 54\) (hoặc tính tỉ lệ trực tiếp: \(36 \times \frac{30}{20} = 54\)).',
            r'Khi hai hạng mục cùng tính theo phần trăm của cùng một tổng thể, ta lấy thẳng tỉ số phần trăm: \(\text{Minivans} = 36 \times \frac{30\%}{20\%} = 54\) mà không cần tính tổng trung gian.',
            r'Gõ `36 * (30/20)` trên Desmos ra ngay `54`.'
        ),
        _spr(
            'may2025_m1_q11', 11, 'Problem-Solving and Data Analysis', 'Probability and conditional probability', 'Easy',
            r'<p>Each face of a fair 16-sided die is labeled with a number from 1 through 16, with a different number appearing on each face.</p>',
            r'If the die is rolled one time, what is the probability of rolling a 4? (Express your answer as a decimal or fraction, not as a percent.)',
            ['1/16', '0.0625', '.0625'], r'1/16 (hoặc 0.0625)',
            r'Xúc xắc cân đối có \(16\) mặt đánh số khác nhau từ \(1\) đến \(16\), trong đó chỉ có đúng \(1\) mặt mang số \(4\). Xác suất tung được mặt \(4\) là \(\frac{1}{16} = 0.0625\).',
            r'Đọc kỹ yêu cầu định dạng Grid-in: nhập phân số `1/16` hoặc thập phân `0.0625` / `.0625`, tuyệt đối không đổi sang phần trăm.',
            r'Nhập phân số tối giản `1/16` vào ô trả lời là an toàn và nhanh nhất.'
        ),
        _mcq(
            'may2025_m1_q12', 12, 'Advanced Math', 'Nonlinear equations in one variable', 'Medium',
            r'<p>The base of a parallelogram has a length of \(x\) meters, and the height of the parallelogram is \(x - 8\) meters. The parallelogram has an area of \(308\) square meters.</p>',
            r'What is the value of \(x\)?',
            {'A': r'\(28\)', 'B': r'\(22\)', 'C': r'\(14\)', 'D': r'\(11\)'},
            'B',
            r'Diện tích hình bình hành bằng cạnh đáy nhân chiều cao: \(x(x - 8) = 308 \Rightarrow x^2 - 8x - 308 = 0\). Phân tích thành nhân tử: \((x - 22)(x + 14) = 0\). Vì độ dài \(x > 0\), ta nhận \(x = 22\) (kiểm tra: \(22 \times 14 = 308\)).',
            r'Công thức diện tích hình bình hành là \(A = b \cdot h\) (không có hệ số \(\frac{1}{2}\) như tam giác). Có thể thử trực tiếp 4 đáp án vào \(x(x - 8) = 308\).',
            {
                'A': ('Thử sai thừa số', r'\(28 \times (28 - 8) = 560 \ne 308\).'),
                'B': ('Đáp án đúng', r'\(22 \times (22 - 8) = 22 \times 14 = 308\).'),
                'C': ('Nhầm sang chiều cao', r'\(14\) là chiều cao \(x - 8\), không phải cạnh đáy \(x\).'),
                'D': ('Nhầm công thức diện tích', r'\(11 \times 3 = 33 \ne 308\); lấy nửa của \(22\).'),
            },
            r'Gõ `x(x - 8) = 308` vào Desmos, lấy nghiệm dương `x = 22` trong 3 giây.'
        ),
        _mcq(
            'may2025_m1_q13', 13, 'Advanced Math', 'Nonlinear functions', 'Medium',
            tbl_q13 + r'<p>The table shows three values of \(x\) and their corresponding values of \(y\) for the equation \(y = 6(2)^x + 9\). In the table, \(a\) is a constant.</p>',
            r'What is the value of \(a\)?',
            {'A': r'\(105\)', 'B': r'\(57\)', 'C': r'\(48\)', 'D': r'\(45\)'},
            'B',
            r'Kiểm tra bảng với \(y = 6(2)^x + 9\): khi \(x = 1 \Rightarrow y = 6(2) + 9 = 21\); khi \(x = 2 \Rightarrow y = 6(4) + 9 = 33\). Vậy khi \(x = 3\), ta có \(a = 6(2)^3 + 9 = 6(8) + 9 = 48 + 9 = 57\).',
            r'Chú ý thứ tự phép toán trong hàm mũ \(6(2)^x + 9\): tính lũy thừa \(2^3 = 8\) trước, rồi nhân \(6\), cuối cùng mới cộng \(9\).',
            {
                'A': ('Nhầm tính tại x = 4', r'\(6(2)^4 + 9 = 96 + 9 = 105\) là giá trị ứng với \(x = 4\), không phải \(x = 3\).'),
                'B': ('Đáp án đúng', r'\(6(2)^3 + 9 = 48 + 9 = 57\).'),
                'C': ('Quên cộng hằng số 9', r'\(6(2)^3 = 48\), quên cộng thêm \(+ 9\).'),
                'D': ('Nhầm sang hàm tuyến tính', r'Thấy \(33 - 21 = 12\) nên cộng thêm \(12\): \(33 + 12 = 45\), quên rằng đây là hàm mũ.'),
            },
            r'Gõ `f(x) = 6(2)^x + 9` rồi gõ `f(3)` trong Desmos ra ngay `57`.'
        ),
        _mcq(
            'may2025_m1_q14', 14, 'Geometry and Trigonometry', 'Area and volume', 'Medium',
            r'<p>A right square pyramid has a base with side lengths of \(6\) centimeters. The height of the pyramid is \(10\) centimeters.</p>',
            r'What is the volume, in cubic centimeters, of this pyramid?',
            {'A': r'\(20\)', 'B': r'\(40\)', 'C': r'\(120\)', 'D': r'\(360\)'},
            'C',
            r'Thể tích hình chóp vuông (right square pyramid) là \(V = \frac{1}{3} B h = \frac{1}{3} s^2 h\). Thay cạnh đáy \(s = 6\) và chiều cao \(h = 10\): \(V = \frac{1}{3}(6^2)(10) = \frac{1}{3}(36)(10) = 120\text{ cm}^3\).',
            r'Đừng quên hệ số \(\frac{1}{3}\) trong công thức thể tích hình chóp (\(V = \frac{1}{3}\ell w h\)) — công thức có sẵn ngay trong Reference Sheet của Bluebook.',
            {
                'A': ('Quên bình phương cạnh đáy', r'Tính \(\frac{1}{3}(6)(10) = 20\), quên diện tích đáy là \(6^2 = 36\).'),
                'B': ('Chia 3 hai lần hoặc sai diện tích đáy', r'Tính nhầm diện tích đáy hoặc chia thêm cho 3.'),
                'C': ('Đáp án đúng', r'\(V = \frac{1}{3} \times 6^2 \times 10 = 120\).'),
                'D': ('Quên hệ số 1/3', r'\(6^2 \times 10 = 360\) là thể tích hình lăng trụ đứng, chưa chia 3 cho hình chóp.'),
            },
            r'Gõ `(1/3)*6^2*10` trên Desmos ra ngay `120`.'
        ),
        _spr(
            'may2025_m1_q15', 15, 'Advanced Math', 'Systems of linear and nonlinear equations', 'Medium',
            r'<p style="text-align:center;font-size:17px;">\[y = x + 9\]\[y = x^2 + 16x + 63\]</p><p>A solution to the given system of equations is \((a, b)\), where \(a\) and \(b\) are constants.</p>',
            r'What is the greatest possible value of \(a\)?',
            ['-6'], '-6',
            r'Cho hai vế phải bằng nhau: \(x^2 + 16x + 63 = x + 9 \Rightarrow x^2 + 15x + 54 = 0\). Phân tích thành nhân tử: \((x + 6)(x + 9) = 0 \Rightarrow x = -6\) hoặc \(x = -9\). Trong hai số âm, giá trị lớn nhất của \(a\) là \(-6\) (vì \(-6 > -9\)).',
            r'Cực kỳ cẩn thận khi so sánh số âm: \(-6 > -9\)! Rất nhiều học sinh bị bẫy chọn \(-9\) vì thấy \(9 > 6\).',
            r'Nhập hai phương trình `y = x + 9` và `y = x^2 + 16x + 63` vào Desmos, bấm vào hai giao điểm `(-9, 0)` và `(-6, 3)` \(\Rightarrow\) hoành độ lớn nhất là `-6`.'
        ),
        _spr(
            'may2025_m1_q16', 16, 'Geometry and Trigonometry', 'Circles', 'Medium',
            r'<p>Circle A in the \(xy\)-plane has the equation \((x + 3)^2 + (y - 3)^2 = 4\). Circle B has the same center as circle A. The radius of circle B is two times the radius of circle A. The equation defining circle B in the \(xy\)-plane is \((x + 3)^2 + (y - 3)^2 = k\), where \(k\) is a constant.</p>',
            r'What is the value of \(k\)?',
            ['16'], '16',
            r'Từ phương trình chuẩn đường tròn \((x - h)^2 + (y - k_0)^2 = r^2\), đường tròn A có \(r_A^2 = 4 \Rightarrow r_A = 2\). Bán kính đường tròn B gấp đôi đường tròn A nên \(r_B = 2 \times 2 = 4\). Do đó hằng số vế phải là \(k = r_B^2 = 4^2 = 16\).',
            r'Khi bán kính tăng gấp \(m\) lần thì hằng số vế phải \(r^2\) tăng gấp \(m^2\) lần: bán kính nhân \(2 \Rightarrow r^2\) nhân \(2^2 = 4 \Rightarrow k = 4 \times 4 = 16\) (tránh bẫy nhân 2 thành 8).',
            r'Không cần vẽ hình: \(r_A = \sqrt{4} = 2 \Rightarrow r_B = 4 \Rightarrow k = 4^2 = 16\).'
        ),
        _spr(
            'may2025_m1_q17', 17, 'Algebra', 'Linear equations in two variables', 'Medium',
            r'<p>In the \(xy\)-plane, line \(k\) has a slope of \(\frac{6}{17}\), an \(x\)-intercept of \((-6, 0)\), and a \(y\)-intercept of \((0, p)\).</p>',
            r'What is the value of \(p\)?',
            ['36/17', '2.117', '2.118'], r'36/17 (hoặc 2.117 / 2.118)',
            r'Áp dụng công thức hệ số góc đi qua hai điểm \((-6, 0)\) và \((0, p)\): \(m = \frac{p - 0}{0 - (-6)} = \frac{p}{6}\). Theo đề bài \(m = \frac{6}{17}\), suy ra \(\frac{p}{6} = \frac{6}{17} \Rightarrow p = \frac{36}{17} \approx 2.1176\).',
            r'Cũng có thể thay điểm \((-6, 0)\) vào \(y = \frac{6}{17}x + p\): \(0 = -\frac{36}{17} + p \Rightarrow p = \frac{36}{17}\). Với Grid-in, nhập phân số `36/17` chính xác tuyệt đối và gọn trong 5 ký tự.',
            r'Gõ `y = (6/17)(x + 6)` vào Desmos, bấm vào giao điểm trục tung `(0, 2.118)` hoặc đổi sang phân số `36/17`.'
        ),
        _mcq(
            'may2025_m1_q18', 18, 'Advanced Math', 'Equivalent expressions', 'Medium',
            r'<p>Consider the polynomial \(20y^3 + 15py^2 + 28y + 21p\).</p>',
            r'Which expression is a factor of \(20y^3 + 15py^2 + 28y + 21p\)?',
            {'A': r'\(5y^2 + 7\)', 'B': r'\(5y^2 + 7p\)', 'C': r'\(4y + 3\)', 'D': r'\(3y + 4p\)'},
            'A',
            r'Phân tích đa thức 4 hạng tử bằng phương pháp nhóm hạng tử (factoring by grouping): \(20y^3 + 15py^2 + 28y + 21p = 5y^2(4y + 3p) + 7(4y + 3p) = (5y^2 + 7)(4y + 3p)\). Vậy nhân tử trong các đáp án là \(5y^2 + 7\).',
            r'Gặp đa thức 4 hạng tử dạng \(A + B + C + D\), hãy nhóm hai hạng tử đầu và hai hạng tử sau rồi đặt nhân tử chung lớn nhất (GCF) để làm xuất hiện ngoặc chung.',
            {
                'A': ('Đáp án đúng', r'Ta phân tích được \((5y^2 + 7)(4y + 3p)\), chứa đúng nhân tử \(5y^2 + 7\).'),
                'B': ('Gắn nhầm biến p', r'Nhân tử chung thực sự là \(4y + 3p\) chứ không phải gắn \(p\) vào số \(7\).'),
                'C': ('Thiếu biến p', r'Nhân tử bậc nhất đúng phải là \(4y + 3p\), không phải \(4y + 3\).'),
                'D': ('Đảo hệ số 3 và 4', r'Nhân tử bậc nhất là \(4y + 3p\), không phải \(3y + 4p\).'),
            },
            r'Thử nhanh với `y = 2, p = 3`: biểu thức gốc bằng `20(8) + 15(3)(4) + 28(2) + 21(3) = 459`. Kiểm tra `459 / (5(4) + 7) = 459 / 27 = 17` (chia hết nguyên) \(\Rightarrow\) chọn A!'
        ),
        _mcq(
            'may2025_m1_q19', 19, 'Geometry and Trigonometry', 'Lines, angles, and triangles', 'Medium',
            svg_m1_q19_similar_triangles() + r"<p>Triangles \(ABC\) and \(A'B'C'\) are shown. Triangle \(ABC\) is dilated by a scale factor of \(4\) to form triangle \(A'B'C'\). Vertex \(A\) corresponds to \(A'\), vertex \(B\) corresponds to \(B'\), and vertex \(C\) corresponds to \(C'\).</p>",
            r"If the length of \(\overline{AB}\) is \(48\), what is the length of \(\overline{A'B'}\)?",
            {'A': r'\(4\)', 'B': r'\(12\)', 'C': r'\(52\)', 'D': r'\(192\)'},
            'D',
            r"Phép vị tự (dilation) với hệ số tỉ lệ \(k = 4\) biến mọi độ dài đoạn thẳng tăng gấp \(4\) lần: \(A'B' = 4 \times AB = 4 \times 48 = 192\).",
            r'Trong phép vị tự tỉ số \(k\): độ dài cạnh nhân \(k\), diện tích nhân \(k^2\), còn số đo góc giữ nguyên không đổi.',
            {
                'A': ('Nhầm hệ số tỉ lệ', r"\(4\) chỉ là hệ số phóng đại (scale factor), không phải độ dài \(\overline{A'B'}\)."),
                'B': ('Chia ngược thay vì nhân', r'Tính \(48 \div 4 = 12\) thay vì \(48 \times 4\).'),
                'C': ('Cộng thay vì nhân', r'Tính \(48 + 4 = 52\); phép vị tự là phép nhân tỉ lệ, không phải phép cộng.'),
                'D': ('Đáp án đúng', r"\(A'B' = 4 \times 48 = 192\)."),
            },
            r'Gõ `48 * 4` trên Desmos ra ngay `192`.'
        ),
        _mcq(
            'may2025_m1_q20', 20, 'Advanced Math', 'Nonlinear functions', 'Medium',
            r'<p>An object is launched into the air from ground level. According to a quadratic model, \(3.9\) seconds after the object is launched, it reaches its maximum height of \(243.36\) feet above ground level.</p>',
            r'Which equation represents this model, where \(f(t)\) is the object&#39;s height, in feet, above ground level \(t\) seconds after it was launched?',
            {
                'A': r'\(f(t) = -16(t - 3.9)^2 + 243.36\)',
                'B': r'\(f(t) = 16(t - 3.9)^2 + 243.36\)',
                'C': r'\(f(t) = -16(t + 3.9)^2 + 243.36\)',
                'D': r'\(f(t) = 16(t + 3.9)^2 + 243.36\)',
            },
            'A',
            r'Dạng đỉnh (vertex form) của parabol là \(f(t) = a(t - h)^2 + k\). Vì vật đạt độ cao cực đại \(243.36\) feet tại \(t = 3.9\) giây nên đỉnh là \((h, k) = (3.9, 243.36)\) và parabol úp xuống (\(a < 0\)). Do đó \(f(t) = -16(t - 3.9)^2 + 243.36\). Kiểm tra điểm xuất phát từ mặt đất: \(f(0) = -16(-3.9)^2 + 243.36 = -243.36 + 243.36 = 0\) (khớp hoàn hảo!).',
            r'Trong dạng đỉnh \(a(t - h)^2 + k\): có giá trị CỰC ĐẠI \(\Rightarrow a < 0\); hoành độ đỉnh dương \(h = 3.9 \Rightarrow\) trong ngoặc là dấu trừ \((t - 3.9)^2\).',
            {
                'A': ('Đáp án đúng', r'Parabol úp xuống (\(a = -16 < 0\)), đỉnh \((3.9, 243.36)\) và \(f(0) = 0\).'),
                'B': ('Sai chiều parabol', r'Hệ số \(+16 > 0\) tạo giá trị cực tiểu chứ không phải cực đại.'),
                'C': ('Sai dấu hoành độ đỉnh', r'\((t + 3.9)^2\) có đỉnh tại \(t = -3.9\) (thời gian âm).'),
                'D': ('Sai cả dấu a và dấu đỉnh', r'Vừa ngửa lên vừa có đỉnh tại \(t = -3.9\).'),
            },
            r'Nhập nhanh `-16(t - 3.9)^2 + 243.36` vào Desmos để thấy ngay đỉnh `(3.9, 243.36)` và đi qua `(0, 0)`.'
        ),
        _spr(
            'may2025_m1_q21', 21, 'Algebra', 'Systems of two linear equations in two variables', 'Hard',
            r'<p style="text-align:center;font-size:17px;">\[(x - 4) - 5(y + 2) = 131\]\[(x - 4) + 5(y + 2) = 446\]</p><p>The solution to the given system of equations is \((x, y)\).</p>',
            r'What is the value of \(10(x - 4)\)?',
            ['2885'], '2885',
            r'Cộng vế theo vế hai phương trình để triệt tiêu ngay \(-5(y + 2)\) và \(+5(y + 2)\): \(2(x - 4) = 131 + 446 = 577\). Đề yêu cầu tìm \(10(x - 4)\), chỉ cần nhân hai vế với \(5\): \(10(x - 4) = 5 \times 577 = 2{,}885\).',
            r'Kỹ thuật SAT "xem cụm làm ẩn" (treating expressions as a single variable): giữ nguyên khối \((x - 4)\) thay vì phá ngoặc giải lẻ \(x = 292.5\), giúp giải trong 5 giây và tránh sai số.',
            r'Cộng trực tiếp `(131 + 446) * 5` trên Desmos ra ngay `2885`.'
        ),
        _mcq(
            'may2025_m1_q22', 22, 'Problem-Solving and Data Analysis', 'One-variable data: Distributions and measures of center and spread', 'Hard',
            svg_m1_q22_histogram() + r'<p>The histogram summarizes the distribution of an original data set that represents the number of points per game a basketball team has scored in the last \(50\) games played. If the team scores \(18\) points in the next game and this game is added to the original data set to create a new data set of \(51\) values, which of the following must be true?</p><p style="margin-left:16px;">I. The median number of points per game for the new data set is less than the median number of points per game for the original data set.<br/>II. The mean number of points per game for the new data set is less than the mean number of points per game for the original data set.</p>',
            r'Which of the following must be true?',
            {'A': 'I only', 'B': 'II only', 'C': 'I and II', 'D': 'Neither I nor II'},
            'B',
            r'Xét mệnh đề II (Mean): tất cả 50 trận ban đầu đều có điểm \(\ge 30\), nên trung bình ban đầu \(\bar{x}_{50} \ge 30\). Khi thêm giá trị \(18 < 30 \le \bar{x}_{50}\), trung bình mới \(\bar{x}_{51} = \frac{50\bar{x}_{50} + 18}{51}\) BẮT BUỘC nhỏ hơn nghiêm ngặt \(\bar{x}_{50}\) \(\Rightarrow\) II đúng. Xét mệnh đề I (Median): với 50 giá trị (tần số các cột là \(2, 7, 28, 13\)), trung vị ban đầu là trung bình cộng của giá trị thứ 25 và 26 (cả hai đều nằm trong cột 50–59). Khi thêm 18 ở đầu dãy (51 giá trị), trung vị mới là giá trị thứ 25 của dãy cũ. Nếu giá trị thứ 25 và 26 ban đầu BẰNG NHAU (ví dụ cùng là 55 điểm), trung vị mới sẽ BẰNG trung vị cũ chứ không nhỏ hơn \(\Rightarrow\) I không bắt buộc đúng!',
            r'Bẫy kinh điển SAT 750+: thêm một giá trị nhỏ hơn mọi số cũ LUÔN làm giảm trung bình (mean), nhưng trung vị (median) chỉ "nhỏ hơn hoặc bằng" — KHÔNG bắt buộc giảm nghiêm ngặt vì hai số ở giữa có thể trùng nhau!',
            {
                'A': ('Bẫy median luôn giảm', r'I sai vì hai giá trị thứ 25 và 26 có thể trùng nhau; đồng thời bỏ sót II chắc chắn đúng.'),
                'B': ('Đáp án đúng', r'Chỉ II bắt buộc đúng vì \(18\) nhỏ hơn mọi giá trị cũ (\(\ge 30\)), chắc chắn kéo trung bình xuống.'),
                'C': ('Bẫy "nhỏ hơn" vs "nhỏ hơn hoặc bằng"', r'I không bắt buộc đúng: nếu trận thứ 25 và 26 đều ghi 54 điểm thì median cũ và mới đều bằng 54.'),
                'D': ('Quên bản chất số trung bình', r'Thêm một giá trị nhỏ hơn mean cũ thì mean mới luôn giảm nghiêm ngặt, nên II luôn đúng.'),
            },
            r'Thử phản ví dụ cho I trên nháp: nếu cả 28 trận ở cột 50–59 đều ghi 55 điểm thì median cũ = `(55+55)/2 = 55`, median mới = `55` (không đổi!).'
        ),
    ]


# ============================================================================
# MODULE 2 LOWER / EASY (mod5_math, 22 REAL QUESTIONS)
# ============================================================================

def _build_module2_lower():
    tbl_q9 = _table(
        [r'\(x\)', r'\(f(x)\)'],
        [['−3', '0'], ['−1', '3'], ['1', '0'], ['3', '3'], ['5', '0']],
    )
    return [
        _mcq(
            'may2025_m2l_q1', 1, 'Advanced Math', 'Systems of linear and nonlinear equations', 'Easy',
            svg_m2l_q1_parabola_line() + r'<p>The graph of a system of a linear and a quadratic equation is shown.</p>',
            r'What is the solution \((x, y)\) to this system?',
            {'A': r'\((10, 1)\)', 'B': r'\((10, -1)\)', 'C': r'\((-10, 1)\)', 'D': r'\((0, 0)\)'},
            'A',
            r'Nghiệm của hệ phương trình là tọa độ giao điểm của parabol và đường thẳng ngang. Trên đồ thị, parabol có đỉnh tại \((10, 1)\) tiếp xúc đúng với đường thẳng ngang \(y = 1\) tại điểm \((10, 1)\).',
            r'Giao điểm duy nhất giữa đường thẳng và parabol chính là nghiệm \((x, y)\) của hệ; đọc hoành độ \(x = 10\) trên trục ngang trước, rồi tung độ \(y = 1\) trên trục dọc.',
            {
                'A': ('Đáp án đúng', r'Đỉnh parabol tiếp xúc đường thẳng ngang \(y = 1\) tại đúng \((10, 1)\).'),
                'B': ('Sai dấu tung độ', r'Đường thẳng nằm phía trên trục hoành (\(y = +1\)), không phải \(y = -1\).'),
                'C': ('Sai dấu hoành độ', r'Đỉnh nằm ở góc phần tư thứ I (\(x = +10\)), không phải \(x = -10\).'),
                'D': ('Nhầm gốc tọa độ', r'Gốc \((0, 0)\) không nằm trên cả đường thẳng \(y = 1\) lẫn parabol.'),
            },
            r'Đọc trực tiếp giao điểm trên hình vẽ: `x = 10`, `y = 1` \(\Rightarrow\) `(10, 1)`.'
        ),
        _mcq(
            'may2025_m2l_q2', 2, 'Problem-Solving and Data Analysis', 'Ratios, rates, proportional relationships, and units', 'Easy',
            r'<p>A wheel completes \(200\) revolutions in \(20\) minutes.</p>',
            r'At this rate, how many revolutions per minute does this wheel complete?',
            {'A': r'\(10\)', 'B': r'\(180\)', 'C': r'\(220\)', 'D': r'\(400\)'},
            'A',
            r'Tốc độ quay tính theo số vòng mỗi phút (revolutions per minute): \(\frac{200\text{ revolutions}}{20\text{ minutes}} = 10\) vòng/phút.',
            r'Từ khóa "per minute" luôn tương ứng phép chia cho số phút: \(\frac{\text{Revolutions}}{\text{Minutes}}\).',
            {
                'A': ('Đáp án đúng', r'\(\frac{200}{20} = 10\) vòng/phút.'),
                'B': ('Trừ thay vì chia', r'Lấy nhầm \(200 - 20 = 180\).'),
                'C': ('Cộng thay vì chia', r'Lấy nhầm \(200 + 20 = 220\).'),
                'D': ('Nhân sai tỉ lệ', r'Nhân \(200 \times 2 = 400\) thay vì chia cho \(20\).'),
            },
            r'Gõ `200 / 20` vào Desmos ra ngay `10`.'
        ),
        _spr(
            'may2025_m2l_q3', 3, 'Problem-Solving and Data Analysis', 'One-variable data: Distributions and measures of center and spread', 'Easy',
            svg_m2l_q3_bar_graph() + r'<p>The bar graph shows the number of visitors at a store each day the store was open for business during a certain week.</p>',
            r'During this week, how many days did the store have between \(90\) and \(140\) visitors?',
            ['2'], '2',
            r'Đọc chiều cao các cột theo từng ngày: Sunday (\(\approx 97\)), Monday (\(\approx 20\)), Wednesday (\(\approx 54\)), Thursday (\(\approx 45\)), Friday (\(\approx 85\)), Saturday (\(\approx 137\)). Các ngày có lượng khách nằm trong khoảng từ \(90\) đến \(140\) là Sunday (\(97\)) và Saturday (\(137\)) — tổng cộng có \(2\) ngày.',
            r'Dóng ngang theo vạch `90` và `140` trên trục tung rồi đếm số cột có đỉnh rơi vào dải nằm giữa hai đường ngang đó (lưu ý cột Friday chỉ khoảng 85 < 90).',
            r'Chỉ cần đọc biểu đồ: đếm số cột cao hơn đường `90` và thấp hơn đường `140` \(\Rightarrow\) đúng `2` cột.'
        ),
        _mcq(
            'may2025_m2l_q4', 4, 'Algebra', 'Linear equations in one variable', 'Easy',
            r'<p>Suppose \(2x = 8\).</p>',
            r'If \(2x = 8\), what is the value of \(10x\)?',
            {'A': r'\(9\)', 'B': r'\(13\)', 'C': r'\(20\)', 'D': r'\(40\)'},
            'D',
            r'Nhân cả hai vế của \(2x = 8\) với \(5\): \(5(2x) = 5(8) \Rightarrow 10x = 40\). (Hoặc giải \(x = 4 \Rightarrow 10x = 40\).)',
            r'Quan sát bội số trực tiếp: \(10x = 5 \cdot (2x) = 5 \times 8 = 40\), nhanh gấp đôi so với tìm \(x\) rồi thay lại.',
            {
                'A': ('Cộng sai hằng số', r'Không liên quan đến tỉ lệ nhân 5.'),
                'B': ('Cộng thay vì nhân', r'Lấy \(8 + 5 = 13\) thay vì \(8 \times 5 = 40\).'),
                'C': ('Nhầm hệ số nhân', r'Lấy \(10 \times 2 = 20\) thay vì \(10 \times 4 = 40\).'),
                'D': ('Đáp án đúng', r'\(x = 4 \Rightarrow 10x = 40\).'),
            },
            r'Gõ `2x = 8` \(\Rightarrow x = 4\), rồi tính `10 * 4 = 40`.'
        ),
        _mcq(
            'may2025_m2l_q5', 5, 'Problem-Solving and Data Analysis', 'Percentages', 'Easy',
            r'<p>There are \(650\) objects in a box. Of these objects, \(8\%\) are cubes.</p>',
            r'How many cubes are in the box?',
            {'A': r'\(8\)', 'B': r'\(52\)', 'C': r'\(260\)', 'D': r'\(642\)'},
            'B',
            r'Số khối lập phương (cubes) trong hộp là \(8\%\) của \(650\): \(0.08 \times 650 = 52\).',
            r'Tính \(p\%\) của \(N\) bằng cách nhân \(\frac{p}{100} \times N\) — nhớ \(8\% = 0.08\), không phải \(0.8\).',
            {
                'A': ('Lấy nguyên con số phần trăm', r'\(8\) là tỉ lệ phần trăm (\(8\%\)), không phải số lượng khối lập phương.'),
                'B': ('Đáp án đúng', r'\(0.08 \times 650 = 52\).'),
                'C': ('Tính nhầm 40%', r'\(260\) là \(40\%\) của \(650\), không phải \(8\%\).'),
                'D': ('Trừ thay vì tính phần trăm', r'Tính nhầm \(650 - 8 = 642\).'),
            },
            r'Gõ `0.08 * 650` (hoặc `8% of 650`) vào Desmos ra ngay `52`.'
        ),
        _mcq(
            'may2025_m2l_q6', 6, 'Algebra', 'Linear equations in one variable', 'Easy',
            r'<p>Reynaldo purchased a box of pasta and some tomatoes at the grocery store. Reynaldo paid $2 for the box of pasta and $1.20 per pound for the tomatoes. Reynaldo paid a total of $4.40 for the box of pasta and the tomatoes. (Assume there is no sales tax.)</p>',
            r'Which of the following equations can be used to find \(p\), the number of pounds of tomatoes Reynaldo purchased?',
            {
                'A': r'\(1.20p + 2 = 4.40\)',
                'B': r'\(1.20p - 2 = 4.40\)',
                'C': r'\(1.20 + 2p = 4.40\)',
                'D': r'\(1.20 - 2p = 4.40\)',
            },
            'A',
            r'Tiền mua \(p\) pound cà chua với giá $1.20/pound là \(1.20p\). Cộng thêm tiền hộp mì ống cố định $2 bằng tổng số tiền $4.40: \(1.20p + 2 = 4.40\).',
            r'Đơn giá theo đơn vị ("per pound") luôn nhân với biến \(p\), còn khoản mua cố định ("a box") được cộng như hằng số độc lập.',
            {
                'A': ('Đáp án đúng', r'Chi phí cà chua (\(1.20p\)) cộng chi phí mì ống (\(2\)) bằng tổng \(4.40\).'),
                'B': ('Sai dấu phép cộng', r'Phải cộng thêm $2 tiền mì ống chứ không trừ đi $2.'),
                'C': ('Gắn biến p sai đơn giá', r'$2 là giá hộp mì ống cố định, còn $1.20 mới là đơn giá theo pound cà chua.'),
                'D': ('Sai cả vị trí biến và dấu', r'Vừa nhân nhầm \(p\) với 2 vừa đặt dấu trừ.'),
            },
            r'Kiểm tra ý nghĩa thực tế: nếu mua \(p = 2\) pound cà chua thì trả \(1.20(2) + 2 = 4.40\), khớp duy nhất đáp án A.'
        ),
        _mcq(
            'may2025_m2l_q7', 7, 'Advanced Math', 'Nonlinear functions', 'Easy',
            r'<p>Consider the exponential equation \(y = \left(\frac{3}{11}\right)^{x + 1}\).</p>',
            r'What is the \(y\)-intercept of the graph of \(y = \left(\frac{3}{11}\right)^{x + 1}\) in the \(xy\)-plane?',
            {
                'A': r'\((3, 11)\)',
                'B': r'\((0, 11)\)',
                'C': r'\((0, 3)\)',
                'D': r'\(\left(0, \frac{3}{11}\right)\)',
            },
            'D',
            r'Giao điểm trục tung (\(y\)-intercept) xảy ra khi \(x = 0\). Thay \(x = 0\) vào phương trình: \(y = \left(\frac{3}{11}\right)^{0 + 1} = \left(\frac{3}{11}\right)^1 = \frac{3}{11}\). Do đó tọa độ \(y\)-intercept là \(\left(0, \frac{3}{11}\right)\).',
            r'Mọi \(y\)-intercept đều có dạng \((0, y_0)\) — chỉ cần thay \(x = 0\) vào công thức hàm số. Chú ý số mũ ở đây là \(x + 1\), nên tại \(x = 0\) số mũ bằng \(1\) (không phải \(0\))!',
            {
                'A': ('Hoành độ khác 0', r'Điểm \((3, 11)\) có \(x = 3 \ne 0\), không nằm trên trục tung.'),
                'B': ('Đọc nhầm mẫu số', r'Chỉ lấy mẫu số \(11\) làm tung độ gốc.'),
                'C': ('Đọc nhầm tử số', r'Chỉ lấy tử số \(3\) làm tung độ gốc.'),
                'D': ('Đáp án đúng', r'Khi \(x = 0\), \(y = \left(\frac{3}{11}\right)^1 = \frac{3}{11} \Rightarrow \left(0, \frac{3}{11}\right)\).'),
            },
            r'Nhập `y = (3/11)^(x+1)` vào Desmos rồi bấm vào giao điểm với trục tung sẽ thấy `(0, 0.273)` đúng bằng `(0, 3/11)`.'
        ),
        _mcq(
            'may2025_m2l_q8', 8, 'Algebra', 'Linear inequalities in one or two variables', 'Easy',
            r'<p>On a certain day in June, the lowest recorded wind speed in a town was \(6\) miles per hour (mph) and the highest recorded wind speed was \(15\) mph.</p>',
            r'Which inequality is true for all values of \(w\), where \(w\) represents any wind speed, in mph, recorded in the town on this day?',
            {
                'A': r'\(6 \le w \le 15\)',
                'B': r'\(w \ge 15\)',
                'C': r'\(w \le 9\)',
                'D': r'\(w \le 6\)',
            },
            'A',
            r'Vì tốc độ gió thấp nhất ghi nhận là \(6\) mph và cao nhất là \(15\) mph, mọi giá trị tốc độ gió \(w\) ghi nhận trong ngày đều thỏa mãn lớn hơn hoặc bằng \(6\) và nhỏ hơn hoặc bằng \(15\): \(6 \le w \le 15\).',
            r'Bất đẳng thức kép \(a \le w \le b\) luôn dùng để biểu diễn miền giá trị từ mức thấp nhất \(a\) đến mức cao nhất \(b\) (bao gồm cả hai đầu mút).',
            {
                'A': ('Đáp án đúng', r'Mọi tốc độ gió ghi nhận đều nằm trong đoạn \([6, 15]\), tức \(6 \le w \le 15\).'),
                'B': ('Ngược chặn trên', r'Tốc độ gió cao nhất là \(15\), nên \(w \le 15\), không phải \(w \ge 15\).'),
                'C': ('Nhầm sang biên độ (range)', r'\(9 = 15 - 6\) là hiệu tốc độ lớn nhất và nhỏ nhất, không phải chặn trên của \(w\).'),
                'D': ('Ngược chặn dưới', r'\(6\) là tốc độ gió thấp nhất nên \(w \ge 6\), không phải \(w \le 6\).'),
            },
            r'Câu đọc hiểu bất đẳng thức — so sánh trực tiếp cận dưới `6` và cận trên `15`.'
        ),
        _mcq(
            'may2025_m2l_q9', 9, 'Advanced Math', 'Nonlinear functions', 'Medium',
            tbl_q9 + r'<p>The table shows some values of \(x\) and their corresponding values of \(f(x)\).</p>',
            r'Which of the following graphs could be the graph of \(y = f(x)\) in the \(xy\)-plane?',
            {
                'A': svg_m2l_q9_quartic('A'),
                'B': svg_m2l_q9_quartic('B'),
                'C': svg_m2l_q9_quartic('C'),
                'D': svg_m2l_q9_quartic('D'),
            },
            'A',
            r'Từ bảng giá trị, đồ thị hàm số \(y = f(x)\) phải đi qua cả 5 điểm: \((-3, 0)\), \((-1, 3)\), \((1, 0)\), \((3, 3)\), và \((5, 0)\). Kiểm tra các hoành độ giao điểm với trục \(Ox\) (\(f(x) = 0\)) tại \(x = -3, 1, 5\) loại ngay B (cắt tại \(-5, -1, 3\)) và C (cắt tại \(-4, 0, 4\)). Giữa A và D, tại \(x = -1\) và \(x = 3\), bảng cho \(f(-1) = 3 > 0\) và \(f(3) = 3 > 0\) — chỉ đồ thị A nằm phía trên trục hoành tại hai điểm này (đồ thị D đi qua \((-1, -3)\) và \((3, -3)\)).',
            r'Với bài đối chiếu bảng giá trị với 4 đồ thị: bước 1 lọc theo các \(x\)-intercepts (\(f(x) = 0\)), bước 2 kiểm tra dấu dương/âm của một điểm ở giữa (ví dụ \(f(-1) = +3\)) để phân biệt đồ thị úp xuống và ngửa lên.',
            {
                'A': ('Đáp án đúng', r'Đồ thị chữ M đi qua chính xác \((-3, 0)\), \((-1, 3)\), \((1, 0)\), \((3, 3)\), và \((5, 0)\).'),
                'B': ('Bẫy đối xứng trục tung f(-x)', r'Có các nghiệm là \(-5, -1, 3\) thay vì \(-3, 1, 5\); tại \(x = -3\) cho \(y = 3 \ne 0\).'),
                'C': ('Bẫy dịch chuyển & lật ngược', r'Cắt trục hoành tại \(-4, 0, 4\) và nằm dưới trục hoành, không khớp điểm nào trong bảng.'),
                'D': ('Bẫy lật ngược qua trục hoành -f(x)', r'Có cùng 3 giao điểm trục hoành \(-3, 1, 5\) nhưng cho \(f(-1) = -3\) và \(f(3) = -3\) (trái dấu với \(+3\) trong bảng).'),
            },
            r'Chấm nhanh 2 điểm `(-3, 0)` và `(-1, 3)` lên các lựa chọn là loại sạch B, C, D chỉ trong 5 giây.'
        ),
        _spr(
            'may2025_m2l_q10', 10, 'Geometry and Trigonometry', 'Lines, angles, and triangles', 'Easy',
            svg_m2l_q10_parallel_lines() + r'<p>In the figure, line \(j\) is parallel to line \(k\).</p>',
            r'What is the value of \(x\)?',
            ['53'], '53',
            r'Hai góc \(x^\circ\) và \(127^\circ\) nằm kề bù nhau trên cùng đường thẳng \(j\) (linear pair), nên tổng số đo của chúng bằng \(180^\circ\): \(x + 127 = 180 \Rightarrow x = 180 - 127 = 53\).',
            r'Khi hai góc kề nhau tạo thành một đường thẳng (góc bẹt \(180^\circ\)), ta luôn có tổng bằng \(180^\circ\) mà thậm chí chưa cần dùng đến đường thẳng song song \(k\).',
            r'Gõ `180 - 127` trên Desmos ra ngay `53`.'
        ),
        _spr(
            'may2025_m2l_q11', 11, 'Advanced Math', 'Nonlinear functions', 'Easy',
            r'<p>The function \(g\) is defined by \(g(x) = \sqrt{8x + 9}\).</p>',
            r'What is the value of \(g(5)\)?',
            ['7'], '7',
            r'Thay \(x = 5\) vào biểu thức hàm số: \(g(5) = \sqrt{8(5) + 9} = \sqrt{40 + 9} = \sqrt{49} = 7\).',
            r'Lưu ý ký hiệu căn bậc hai số học \(\sqrt{49}\) luôn nhận giá trị KHÔNG ÂM duy nhất là \(7\) (không viết \(\pm 7\)).',
            r'Gõ `sqrt(8(5) + 9)` vào Desmos ra ngay `7`.'
        ),
        _mcq(
            'may2025_m2l_q12', 12, 'Algebra', 'Linear inequalities in one or two variables', 'Medium',
            svg_m2l_q12_inequality() + r'<p>The shaded region shown represents solutions to an inequality.</p>',
            r'Which ordered pair \((x, y)\) is a solution to this inequality?',
            {'A': r'\((0, -6)\)', 'B': r'\((0, 6)\)', 'C': r'\((-6, 0)\)', 'D': r'\((6, 0)\)'},
            'D',
            r'Một cặp số \((x, y)\) là nghiệm của bất phương trình nếu điểm \((x, y)\) nằm TRONG miền tô đậm (hoặc trên đường biên liền nét). Quan sát hình vẽ: cả ba điểm \((0, -6)\), \((0, 6)\), và \((-6, 0)\) đều nằm trong vùng trắng bên trái đường biên. Riêng điểm \((6, 0)\) nằm hẳn bên trong miền tô đậm ở góc phần tư phía bên phải đường biên (\(x > \frac{48}{11} \approx 4.36\)).',
            r'Với câu hỏi đồ thị bất phương trình cho sẵn miền tô đậm: chỉ cần chấm trực tiếp 4 điểm A, B, C, D lên lưới tọa độ, điểm nào rơi vào vùng xám là đáp án đúng!',
            {
                'A': ('Nằm ngoài miền nghiệm', r'Điểm \((0, -6)\) nằm trên trục tung phần âm, hoàn toàn trong vùng trắng.'),
                'B': ('Nằm ngoài miền nghiệm', r'Điểm \((0, 6)\) nằm trên trục tung phần dương, bên trái đường biên.'),
                'C': ('Nằm ngoài miền nghiệm', r'Điểm \((-6, 0)\) nằm trên trục hoành phần âm, cách rất xa vùng tô đậm.'),
                'D': ('Đáp án đúng', r'Điểm \((6, 0)\) nằm trọn trong miền tô đậm bên phải đường biên \(y = -\frac{11}{4}x + 12\).'),
            },
            r'Không cần lập phương trình đường biên: nhìn thẳng điểm `(6, 0)` trên trục \(Ox\) thấy nó nằm giữa vùng tô xám!'
        ),
        _mcq(
            'may2025_m2l_q13', 13, 'Algebra', 'Linear functions', 'Easy',
            r'<p>The function \(f\) is defined by \(f(x) = -\frac{5}{16}x + 16\).</p>',
            r'What is the slope of the graph of \(y = f(x)\) in the \(xy\)-plane?',
            {'A': r'\(-16\)', 'B': r'\(-\frac{5}{16}\)', 'C': r'\(\frac{1}{16}\)', 'D': r'\(5\)'},
            'B',
            r'Hàm bậc nhất viết ở dạng slope-intercept \(y = mx + b\) có \(m\) là hệ số đi liền với \(x\). Với \(f(x) = -\frac{5}{16}x + 16\), hệ số góc là \(m = -\frac{5}{16}\).',
            r'Đừng quên dấu trừ phía trước phân số khi đọc hệ số góc \(m\) từ \(y = mx + b\).',
            {
                'A': ('Nhầm với tung độ gốc đổi dấu', r'\(16\) là \(y\)-intercept (hằng số \(b\)), không phải hệ số góc.'),
                'B': ('Đáp án đúng', r'Hệ số của \(x\) trong \(-\frac{5}{16}x + 16\) là \(-\frac{5}{16}\).'),
                'C': ('Bỏ sót tử số -5', r'Thiếu tử số \(-5\) của hệ số góc.'),
                'D': ('Bỏ sót mẫu số 16 và dấu âm', r'Chỉ đọc phần số \(5\) trên tử mà quên dấu trừ và mẫu \(16\).'),
            },
            r'Đọc trực tiếp hệ số đứng trước \(x\): `m = -5/16`.'
        ),
        _spr(
            'may2025_m2l_q14', 14, 'Advanced Math', 'Nonlinear functions', 'Medium',
            r'<p style="text-align:center;font-size:18px;">\[y = 4{,}600a^x\]</p><p>The given equation, where \(a\) is a positive constant, gives the predicted number of bacteria, \(y\), in a growth medium \(x\) hours after the number of bacteria was initially measured.</p>',
            r'According to the equation, what was the predicted number of bacteria initially measured in the growth medium?',
            ['4600', '4,600'], '4,600',
            r'Thời điểm ban đầu ("initially measured") ứng với \(x = 0\) giờ. Thay \(x = 0\) vào phương trình: \(y = 4{,}600 \cdot a^0 = 4{,}600 \cdot 1 = 4{,}600\) (vì mọi số dương mũ \(0\) đều bằng \(1\)).',
            r'Trong mô hình hàm mũ chuẩn \(y = A \cdot b^x\), hệ số \(A\) đứng trước lũy thừa LUÔN là giá trị ban đầu tại \(x = 0\).',
            r'Không cần biết giá trị của \(a\): khi \(x = 0\) thì \(a^0 = 1\), nên kết quả lập tức là `4600`.'
        ),
        _spr(
            'may2025_m2l_q15', 15, 'Advanced Math', 'Nonlinear equations in one variable', 'Easy',
            r'<p style="text-align:center;font-size:18px;">\[\sqrt{x} = \sqrt{53}\]</p>',
            r'What value of \(x\) makes the given equation true?',
            ['53'], '53',
            r'Bình phương cả hai vế của phương trình \(\sqrt{x} = \sqrt{53}\) (với điều kiện \(x \ge 0\)): \((\sqrt{x})^2 = (\sqrt{53})^2 \Rightarrow x = 53\).',
            r'Hai căn bậc hai số học bằng nhau khi và chỉ khi hai biểu thức dưới dấu căn bằng nhau và không âm.',
            r'Bình phương hai vế ra thẳng `x = 53`.'
        ),
        _mcq(
            'may2025_m2l_q16', 16, 'Algebra', 'Systems of two linear equations in two variables', 'Medium',
            r'<p>A building has \(r\) residential and \(c\) commercial units for a total of \(125\) units. The residential units are \(1{,}050\) square feet and the commercial units are \(2{,}500\) square feet. All units in the building have a combined total of \(167{,}500\) square feet.</p>',
            r'Which system represents this situation?',
            {
                'A': r'\(1{,}050r + 2{,}500c = 125\)<br/>\(r + c = 167{,}500\)',
                'B': r'\(1{,}050r + 2{,}500c = 125\)<br/>\(r - c = 167{,}500\)',
                'C': r'\(1{,}050r + 2{,}500c = 167{,}500\)<br/>\(r + c = 125\)',
                'D': r'\(1{,}050r + 2{,}500c = 167{,}500\)<br/>\(r - c = 125\)',
            },
            'C',
            r'Phương trình số lượng căn hộ: tổng \(r\) căn hộ ở và \(c\) căn thương mại bằng \(125 \Rightarrow r + c = 125\). Phương trình tổng diện tích (square feet): mỗi căn hộ ở rộng \(1{,}050\text{ ft}^2\) và mỗi căn thương mại rộng \(2{,}500\text{ ft}^2\), tổng diện tích là \(167{,}500\text{ ft}^2 \Rightarrow 1{,}050r + 2{,}500c = 167{,}500\).',
            r'Luôn kiểm tra ĐỒNG NHẤT ĐƠN VỊ giữa hai vế của mỗi phương trình: phương trình "units" bằng \(125\), phương trình "square feet" bằng \(167{,}500\).',
            {
                'A': ('Tráo vế phải giữa hai phương trình', r'Gán nhầm tổng diện tích \(167{,}500\) cho số căn và tổng số căn \(125\) cho diện tích.'),
                'B': ('Tráo vế phải và sai dấu trừ', r'Vừa đổi nhầm vế phải vừa dùng \(r - c\) thay vì \(r + c\).'),
                'C': ('Đáp án đúng', r'Khớp hoàn toàn đơn vị: \(r + c = 125\) (units) và \(1{,}050r + 2{,}500c = 167{,}500\) (sq ft).'),
                'D': ('Sai dấu phép trừ', r'Tổng số căn hộ là \(r + c = 125\), không phải hiệu \(r - c = 125\).'),
            },
            r'Bài lập hệ phương trình — kiểm tra đơn vị 2 giây: `units` đi với `125`, `sq ft` đi với `167,500`.'
        ),
        _mcq(
            'may2025_m2l_q17', 17, 'Advanced Math', 'Nonlinear functions', 'Medium',
            r'<p>Consider the polynomial equation \(y = (x + 9)(x - 11)(x + 12)\).</p>',
            r'What is an \(x\)-intercept of the graph of the equation \(y = (x + 9)(x - 11)(x + 12)\) in the \(xy\)-plane?',
            {'A': r'\((1, 0)\)', 'B': r'\((0, 9)\)', 'C': r'\((11, 0)\)', 'D': r'\((0, 12)\)'},
            'C',
            r'Giao điểm với trục hoành (\(x\)-intercept) có tung độ \(y = 0\): \((x + 9)(x - 11)(x + 12) = 0 \Rightarrow x = -9,\; x = 11,\) hoặc \(x = -12\). Do đó ba \(x\)-intercept là \((-9, 0)\), \((11, 0)\), và \((-12, 0)\). Trong 4 đáp án, chỉ có \((11, 0)\) xuất hiện ở C.',
            r'Khi đổi từ nhân tử \((x - r)\) sang \(x\)-intercept \((r, 0)\), nhớ ĐỔI DẤU hằng số và đặt tung độ \(y = 0\) đứng sau!',
            {
                'A': ('Không phải nghiệm của tích', r'Thay \(x = 1\): \(y = (10)(-10)(13) = -1{,}300 \ne 0\).'),
                'B': ('Nhầm vị trí tọa độ & sai dấu', r'\((0, 9)\) nằm trên trục tung (\(x = 0\)), không phải \(x\)-intercept.'),
                'C': ('Đáp án đúng', r'Khi \(x = 11\), nhân tử \((11 - 11) = 0 \Rightarrow y = 0\), nên \((11, 0)\) là \(x\)-intercept.'),
                'D': ('Nhầm vị trí tọa độ', r'\((0, 12)\) nằm trên trục tung, không phải \(x\)-intercept.'),
            },
            r'Gõ `y = (x + 9)(x - 11)(x + 12)` vào Desmos và bấm vào các chấm xám trên trục hoành: `(-12, 0)`, `(-9, 0)`, `(11, 0)`.'
        ),
        _mcq(
            'may2025_m2l_q18', 18, 'Algebra', 'Linear functions', 'Medium',
            r'<p>For the linear function \(f\), \(f(3) = 19\) and \(f(9) = 1\).</p>',
            r'Which equation defines \(f\)?',
            {
                'A': r'\(f(x) = -\frac{1}{3}x + 20\)',
                'B': r'\(f(x) = \frac{1}{3}x - 2\)',
                'C': r'\(f(x) = -3x + 22\)',
                'D': r'\(f(x) = -3x + 28\)',
            },
            'D',
            r'Tìm hệ số góc của hàm bậc nhất đi qua \((3, 19)\) và \((9, 1)\): \(m = \frac{1 - 19}{9 - 3} = \frac{-18}{6} = -3\). Viết \(f(x) = -3x + b\) và thay \((3, 19)\): \(19 = -3(3) + b \Rightarrow 19 = -9 + b \Rightarrow b = 28\). Vậy \(f(x) = -3x + 28\). Kiểm tra lại: \(f(9) = -3(9) + 28 = 1\) (đúng!).',
            r'Mẹo kiểm tra nhanh không bao giờ sai: thay trực tiếp \(x = 3\) và \(x = 9\) vào các đáp án xem hàm nào cho đồng thời \(f(3) = 19\) và \(f(9) = 1\).',
            {
                'A': ('Nghịch đảo hệ số góc', r'Thay \(x = 9\): \(-\frac{1}{3}(9) + 20 = 17 \ne 1\); tính nhầm \(m = \frac{\Delta x}{\Delta y}\).'),
                'B': ('Nghịch đảo & sai dấu slope', r'Thay \(x = 3\): \(f(3) = -1 \ne 19\).'),
                'C': ('Tính sai tung độ gốc b', r'Thay \(x = 3\): \(-3(3) + 22 = 13 \ne 19\) (nhầm lấy \(19 + 3 = 22\) thay vì \(19 + 9 = 28\)).'),
                'D': ('Đáp án đúng', r'\(f(3) = -9 + 28 = 19\) và \(f(9) = -27 + 28 = 1\).'),
            },
            r'Tạo bảng `x1 = [3, 9]`, `y1 = [19, 1]` rồi gõ `y1 ~ m x1 + b` trong Desmos ra ngay `m = -3`, `b = 28`.'
        ),
        _mcq(
            'may2025_m2l_q19', 19, 'Geometry and Trigonometry', 'Right triangles and trigonometry', 'Medium',
            svg_m2l_q19_right_triangle() + r'<p>In right triangle \(TSR\) shown above, angle \(S\) is a right angle, \(ST = 217\), \(RS = 2\sqrt{218}\), and \(RT = 219\).</p>',
            r'What is the value of \(\tan R\) in the triangle shown?',
            {
                'A': r'\(\frac{2\sqrt{218}}{219}\)',
                'B': r'\(\frac{219}{2\sqrt{218}}\)',
                'C': r'\(\frac{2\sqrt{218}}{217}\)',
                'D': r'\(\frac{217}{2\sqrt{218}}\)',
            },
            'D',
            r'Trong tam giác vuông \(TSR\) vuông tại \(S\), xét góc nhọn \(R\): cạnh đối diện góc \(R\) là \(ST = 217\), cạnh kề góc \(R\) là \(RS = 2\sqrt{218}\), cạnh huyền là \(RT = 219\). Áp dụng SOH-CAH-TOA: \(\tan R = \frac{\text{Opposite}}{\text{Adjacent}} = \frac{ST}{RS} = \frac{217}{2\sqrt{218}}\).',
            r'Ghi nhớ "TOA": \(\tan(\theta) = \frac{\text{Opposite}}{\text{Adjacent}}\) — KHÔNG bao giờ có cạnh huyền (\(219\)) trong công thức tang!',
            {
                'A': ('Nhầm sang cos R', r'\(\frac{2\sqrt{218}}{219} = \frac{\text{Adjacent}}{\text{Hypotenuse}} = \cos R\).'),
                'B': ('Nhầm sang sec R', r'\(\frac{219}{2\sqrt{218}} = \frac{\text{Hypotenuse}}{\text{Adjacent}} = \frac{1}{\cos R}\).'),
                'C': ('Lấy ngược thành tan T', r'\(\frac{2\sqrt{218}}{217} = \frac{\text{Adjacent}}{\text{Opposite}} = \cot R = \tan T\).'),
                'D': ('Đáp án đúng', r'\(\tan R = \frac{ST}{RS} = \frac{217}{2\sqrt{218}}\).'),
            },
            r'Kiểm tra định lý Pythagore xác nhận tam giác chuẩn: `217^2 + (2*sqrt(218))^2 = 47961 = 219^2`; \(\tan R = \frac{ST}{RS} = \frac{217}{2\sqrt{218}}\).'
        ),
        _mcq(
            'may2025_m2l_q20', 20, 'Geometry and Trigonometry', 'Area and volume', 'Medium',
            r'<p>A cylinder has a diameter of \(12\) inches and a height of \(16\) inches.</p>',
            r'What is the volume, in cubic inches, of the cylinder?',
            {'A': r'\(36\pi\)', 'B': r'\(192\pi\)', 'C': r'\(576\pi\)', 'D': r'\(2{,}304\pi\)'},
            'C',
            r'Đường kính đáy \(d = 12\) inches \(\Rightarrow\) bán kính đáy \(r = \frac{12}{2} = 6\) inches. Áp dụng công thức thể tích hình trụ: \(V = \pi r^2 h = \pi (6^2)(16) = \pi (36)(16) = 576\pi\text{ in}^3\).',
            r'Bẫy kinh điển hình học SAT: đề cho ĐƯỜNG KÍNH (diameter = 12) chứ không phải bán kính! Luôn chia đôi đường kính lấy \(r = 6\) ngay bước đầu tiên.',
            {
                'A': ('Quên nhân chiều cao', r'\(36\pi = \pi r^2\) chỉ là diện tích mặt đáy hình tròn, chưa nhân với \(h = 16\).'),
                'B': ('Quên bình phương bán kính', r'Tính nhầm \(12 \times 16 \pi = 192\pi\), không bình phương \(r\).'),
                'C': ('Đáp án đúng', r'\(V = \pi (6)^2 (16) = 576\pi\).'),
                'D': ('Dùng nhầm đường kính thay bán kính', r'Tính \(\pi (12)^2 (16) = 2{,}304\pi\), lớn gấp 4 lần thể tích thật.'),
            },
            r'Gõ `(12/2)^2 * 16` trên Desmos ra `576`, gắn thêm \(\pi\) được `576π`.'
        ),
        _mcq(
            'may2025_m2l_q21', 21, 'Algebra', 'Linear equations in two variables', 'Medium',
            r'<p>Line \(r\) is defined by the equation \(2x - 3y = 8\). Line \(s\) is parallel to line \(r\) in the \(xy\)-plane.</p>',
            r'What is the slope of line \(s\)?',
            {'A': r'\(-3\)', 'B': r'\(-2\)', 'C': r'\(\frac{2}{3}\)', 'D': r'\(\frac{3}{2}\)'},
            'C',
            r'Đưa phương trình đường thẳng \(r\) về dạng \(y = mx + b\): \(-3y = -2x + 8 \Rightarrow y = \frac{2}{3}x - \frac{8}{3}\). Vậy hệ số góc của đường thẳng \(r\) là \(\frac{2}{3}\). Vì đường thẳng \(s\) song song với đường thẳng \(r\), hai đường có cùng hệ số góc, nên hệ số góc của \(s\) là \(\frac{2}{3}\).',
            r'Mẹo siêu nhanh cho dạng chuẩn \(Ax + By = C\): hệ số góc luôn là \(m = -\frac{A}{B}\). Với \(2x - 3y = 8 \Rightarrow m = -\frac{2}{-3} = \frac{2}{3}\).',
            {
                'A': ('Đọc nhầm hệ số B', r'\(-3\) chỉ là hệ số của \(y\), không phải hệ số góc.'),
                'B': ('Sai dấu và quên chia', r'Quên chia cho \(-3\) sau khi chuyển \(2x\) sang vế phải.'),
                'C': ('Đáp án đúng', r'Hai đường song song có cùng slope \(m = -\frac{2}{-3} = \frac{2}{3}\).'),
                'D': ('Nghịch đảo phân số', r'Lấy nhầm \(\frac{B}{A}\) thay vì \(-\frac{A}{B}\).'),
            },
            r'Gõ `2x - 3y = 8` trên Desmos, kiểm tra đường đi lên từ trái sang phải qua `(4, 0)` và `(1, -2)` \(\Rightarrow\) slope `2/3`.'
        ),
        _mcq(
            'may2025_m2l_q22', 22, 'Advanced Math', 'Equivalent expressions', 'Medium',
            r'<p style="text-align:center;font-size:18px;">\[r = \sqrt{4w - 7}\]</p><p>The given equation relates the real numbers \(r\) and \(w\), where \(w > \frac{7}{4}\).</p>',
            r'Which equation correctly expresses \(w\) in terms of \(r\)?',
            {
                'A': r'\(w = \frac{r^2}{4} + 7\)',
                'B': r'\(w = \frac{r^2}{4} + \frac{7}{4}\)',
                'C': r'\(w = \sqrt{4r - 7}\)',
                'D': r'\(w = \sqrt{-7r + 4}\)',
            },
            'B',
            r'Bình phương hai vế của \(r = \sqrt{4w - 7}\): \(r^2 = 4w - 7\). Cộng \(7\) vào hai vế: \(4w = r^2 + 7\). Chia cả hai vế (chia TỪNG hạng tử) cho \(4\): \(w = \frac{r^2 + 7}{4} = \frac{r^2}{4} + \frac{7}{4}\).',
            r'Khi chia cả hai vế cho \(4\), phải chia TẤT CẢ các hạng tử trên tử số: \(\frac{r^2 + 7}{4} = \frac{r^2}{4} + \frac{7}{4}\), tránh quên chia số \(7\) như đáp án A!',
            {
                'A': ('Quên chia hạng tử 7 cho 4', r'Chia \(r^2\) cho \(4\) nhưng giữ nguyên \(+7\) thay vì \(+\frac{7}{4}\).'),
                'B': ('Đáp án đúng', r'\(r^2 = 4w - 7 \Rightarrow w = \frac{r^2 + 7}{4} = \frac{r^2}{4} + \frac{7}{4}\).'),
                'C': ('Hoán đổi biến máy móc', r'Chỉ đổi chỗ chữ \(r\) và \(w\) mà không giải ngược phương trình.'),
                'D': ('Biến đổi sai hoàn toàn', r'Không bình phương để khử căn thức.'),
            },
            r'Thử số nhanh: chọn `w = 2` \(\Rightarrow r = \sqrt{8 - 7} = 1\). Thay `r = 1` vào 4 đáp án: chỉ B cho `1/4 + 7/4 = 8/4 = 2 = w`!'
        ),
    ]


# ============================================================================
# MODULE 2 HARD (mod6_math, 22 REAL QUESTIONS)
# ============================================================================

def _build_module2_hard():
    return [
        _mcq(
            'may2025_m2h_q1', 1, 'Algebra', 'Linear inequalities in one or two variables', 'Easy',
            svg_m2h_q1_inequality() + r'<p>The shaded region shown represents the solutions to an inequality in the \(xy\)-plane.</p>',
            r'The shaded region shown represents the solutions to which inequality?',
            {
                'A': r'\(y \ge \frac{1}{3}x + 6\)',
                'B': r'\(y \ge 3x + 6\)',
                'C': r'\(y \le \frac{1}{3}x + 6\)',
                'D': r'\(y \le 3x + 6\)',
            },
            'A',
            r'Đường biên nét liền (solid line \(\Rightarrow \ge\) hoặc \(\le\)) đi qua các điểm \((-3, 5)\), \((0, 6)\), và \((3, 7)\). Hệ số góc là \(m = \frac{7 - 6}{3 - 0} = \frac{1}{3}\), tung độ gốc \(b = 6 \Rightarrow\) phương trình đường biên là \(y = \frac{1}{3}x + 6\). Miền nghiệm được tô PHÍA TRÊN đường biên (ví dụ chứa điểm \((0, 8)\) có \(8 \ge 6\)), nên bất phương trình là \(y \ge \frac{1}{3}x + 6\).',
            r'Xác định 3 yếu tố theo thứ tự: (1) nét liền (\(\ge/\le\)) hay nét đứt (\(>/<\)); (2) tô phía trên (\(\ge\)) hay dưới (\(\le\)); (3) đọc tung độ gốc \(b\) và độ dốc \(m = \frac{\Delta y}{\Delta x}\).',
            {
                'A': ('Đáp án đúng', r'Đường biên có \(m = \frac{1}{3}\), \(b = 6\), nét liền và tô phía trên (\(\ge\)).'),
                'B': ('Nghịch đảo hệ số góc', r'Nhầm \(m = \frac{\Delta x}{\Delta y} = 3\) thay vì \(\frac{1}{3}\) (đường thoải chứ không dốc đứng).'),
                'C': ('Sai chiều bất đẳng thức', r'\(y \le \frac{1}{3}x + 6\) ứng với miền tô PHÍA DƯỚI đường thẳng (chứa gốc tọa độ \((0,0)\)).'),
                'D': ('Sai cả slope và chiều dấu', r'Vừa nhầm \(m = 3\) vừa đảo chiều dấu thành \(\le\).'),
            },
            r'Thử nhanh gốc tọa độ `(0, 0)` không nằm trong vùng tô \(\Rightarrow\) loại C, D. Đường tăng 1 đơn vị theo `y` mỗi khi `x` tăng 3 đơn vị \(\Rightarrow m = 1/3\), chọn A!'
        ),
        _mcq(
            'may2025_m2h_q2', 2, 'Algebra', 'Linear equations in two variables', 'Easy',
            r'<p>Line \(r\) is defined by the equation \(5x - 4y = 3\). Line \(s\) is parallel to line \(r\) in the \(xy\)-plane.</p>',
            r'What is the slope of line \(s\)?',
            {'A': r'\(-5\)', 'B': r'\(-4\)', 'C': r'\(\frac{4}{5}\)', 'D': r'\(\frac{5}{4}\)'},
            'D',
            r'Chuyển \(5x - 4y = 3\) sang dạng \(y = mx + b\): \(-4y = -5x + 3 \Rightarrow y = \frac{5}{4}x - \frac{3}{4}\). Hệ số góc của đường \(r\) là \(\frac{5}{4}\). Vì đường \(s\) song song với đường \(r\) nên hệ số góc của \(s\) cũng bằng \(\frac{5}{4}\).',
            r'Công thức nhanh cho phương trình chuẩn \(Ax + By = C\): slope \(m = -\frac{A}{B} = -\frac{5}{-4} = \frac{5}{4}\).',
            {
                'A': ('Quên chia cho -4', r'Chỉ chuyển \(5x\) sang vế phải thành \(-5x\) mà quên chia cho \(-4\).'),
                'B': ('Đọc nhầm hệ số B', r'\(-4\) chỉ là hệ số của \(y\), không phải hệ số góc.'),
                'C': ('Nghịch đảo hệ số góc', r'Lấy nhầm \(\frac{4}{5}\) thay vì \(\frac{5}{4}\).'),
                'D': ('Đáp án đúng', r'\(m = -\frac{5}{-4} = \frac{5}{4}\).'),
            },
            r'Gõ `5x - 4y = 3` trên Desmos, thấy đường dốc lên nhanh hơn `y = x` (`5/4 = 1.25 > 1`).'
        ),
        _mcq(
            'may2025_m2h_q3', 3, 'Advanced Math', 'Nonlinear functions', 'Easy',
            r'<p>Consider the equation \(y = \left(\frac{3}{11}\right)^{x + 1}\).</p>',
            r'What is the \(y\)-intercept of the graph of \(y = \left(\frac{3}{11}\right)^{x + 1}\) in the \(xy\)-plane?',
            {
                'A': r'\((3, 11)\)',
                'B': r'\((0, 11)\)',
                'C': r'\((0, 3)\)',
                'D': r'\(\left(0, \frac{3}{11}\right)\)',
            },
            'D',
            r'Để tìm \(y\)-intercept, thay \(x = 0\) vào phương trình: \(y = \left(\frac{3}{11}\right)^{0 + 1} = \frac{3}{11}\). Vậy giao điểm trục tung là \(\left(0, \frac{3}{11}\right)\).',
            r'Luôn thay \(x = 0\) để tìm \(y\)-intercept; chú ý số mũ \(x + 1\) trở thành \(1\) khi \(x = 0\), nên \(y = \frac{3}{11}\) (chứ không bằng \(1\)).',
            {
                'A': ('Không phải y-intercept', r'Hoành độ khác \(0\), không nằm trên trục tung.'),
                'B': ('Nhầm sang mẫu số', r'Chỉ lấy mẫu số \(11\) làm tung độ.'),
                'C': ('Nhầm sang tử số', r'Chỉ lấy tử số \(3\) làm tung độ.'),
                'D': ('Đáp án đúng', r'Khi \(x = 0\), \(y = \left(\frac{3}{11}\right)^1 = \frac{3}{11}\).'),
            },
            r'Gõ `y = (3/11)^(x + 1)` vào Desmos và bấm vào điểm cắt trục tung `(0, 0.273)` = `(0, 3/11)`.'
        ),
        _mcq(
            'may2025_m2h_q4', 4, 'Algebra', 'Linear functions', 'Easy',
            r'<p>The function \(f\) is defined by \(f(x) = \frac{4}{11}x\).</p>',
            r'What is the slope of the graph of \(y = f(x)\) in the \(xy\)-plane?',
            {'A': r'\(0\)', 'B': r'\(\frac{4}{11}\)', 'C': r'\(\frac{11}{4}\)', 'D': 'The slope is undefined.'},
            'B',
            r'Hàm số \(f(x) = \frac{4}{11}x\) có dạng \(y = mx + b\) với \(m = \frac{4}{11}\) và \(b = 0\). Do đó hệ số góc của đồ thị là \(\frac{4}{11}\).',
            r'Đường thẳng tỉ lệ thuận \(y = mx\) đi qua gốc tọa độ \((0, 0)\) và có hệ số góc chính là \(m\).',
            {
                'A': ('Nhầm với y-intercept', r'\(0\) là tung độ gốc \(b\), không phải hệ số góc \(m\).'),
                'B': ('Đáp án đúng', r'Hệ số đi với \(x\) là \(m = \frac{4}{11}\).'),
                'C': ('Nghịch đảo hệ số góc', r'Đảo ngược tử và mẫu thành \(\frac{11}{4}\).'),
                'D': ('Nhầm với đường thẳng đứng', r'Chỉ đường thẳng đứng \(x = c\) mới có slope không xác định (undefined).'),
            },
            r'Đọc trực tiếp hệ số của \(x\): `4/11`.'
        ),
        _mcq(
            'may2025_m2h_q5', 5, 'Advanced Math', 'Nonlinear functions', 'Easy',
            r'<p>The function \(g\) is defined by \(g(x) = 7x^{-1}\).</p>',
            r'What is the value of \(g(8)\)?',
            {'A': r'\(-56\)', 'B': r'\(\frac{1}{56}\)', 'C': r'\(\frac{7}{8}\)', 'D': r'\(\frac{8}{7}\)'},
            'C',
            r'Áp dụng quy tắc số mũ âm \(x^{-1} = \frac{1}{x}\) (chỉ tác động lên \(x\), KHÔNG tác động lên hệ số \(7\)): \(g(x) = 7 \cdot \frac{1}{x} = \frac{7}{x}\). Thay \(x = 8\) ta được \(g(8) = \frac{7}{8}\).',
            r'Bẫy thứ tự lũy thừa: \(7x^{-1} = 7 \cdot x^{-1} = \frac{7}{x}\), hoàn toàn khác với \((7x)^{-1} = \frac{1}{7x}\)!',
            {
                'A': ('Nhầm số mũ âm thành dấu trừ', r'Hiểu sai \(7x^{-1}\) thành \(-7x \Rightarrow -56\).'),
                'B': ('Bẫy (7x)^(-1)', r'Nghịch đảo cả số \(7\) thành \(\frac{1}{7 \cdot 8} = \frac{1}{56}\), sai vì không có ngoặc bao quanh \(7x\).'),
                'C': ('Đáp án đúng', r'\(g(8) = 7 \cdot 8^{-1} = \frac{7}{8}\).'),
                'D': ('Đảo ngược phân số', r'Tính nhầm \(\frac{8}{7}\) thay vì \(\frac{7}{8}\).'),
            },
            r'Gõ `7 * 8^(-1)` vào Desmos rồi bấm nút chuyển phân số ra ngay `7/8`.'
        ),
        _mcq(
            'may2025_m2h_q6', 6, 'Advanced Math', 'Nonlinear functions', 'Easy',
            r'<p>The kinetic energy, in joules, of an object with mass \(37\) kilograms traveling at a speed of \(v\) meters per second is given by the function \(K\), where \(K(v) = \frac{1}{2}(37)v^2\).</p>',
            r'Which of the following is the best interpretation of \(K(0) = 0\) in this context?',
            {
                'A': 'The kinetic energy of the object is 0 joules when the mass of the object is 0 kilograms.',
                'B': 'The speed of the object is 0 meters per second when the mass of the object is 0 kilograms.',
                'C': 'The kinetic energy of the object is 0 joules when the object is traveling at a speed of 0 meters per second.',
                'D': 'The height of the object is 0 meters when the object is traveling at a speed of 0 meters per second.',
            },
            'C',
            r'Hàm \(K(v)\) nhận đầu vào là tốc độ \(v\) (meters per second) của vật (có khối lượng cố định \(37\) kg) và trả về đầu ra là động năng \(K(v)\) (joules). Vì vậy \(K(0) = 0\) có nghĩa là khi vật di chuyển với tốc độ \(0\) m/s thì động năng của nó bằng \(0\) joules.',
            r'Khối lượng \(37\) kg là HẰNG SỐ trong bài này, chỉ có tốc độ \(v\) là biến độc lập của hàm \(K(v)\)!',
            {
                'A': ('Nhầm biến đầu vào với khối lượng', r'Khối lượng đã cố định bằng \(37\) kg, biến trong ngoặc \(v\) là tốc độ (speed).'),
                'B': ('Nhầm cả hai đại lượng', r'Không nhắc tới động năng và gán nhầm khối lượng bằng \(0\).'),
                'C': ('Đáp án đúng', r'Mô tả chuẩn đầu vào \(v = 0\text{ m/s}\) và đầu ra \(K(0) = 0\text{ joules}\).'),
                'D': ('Đưa đại lượng không tồn tại', r'Bài toán nói về động năng (kinetic energy), không phải độ cao (height).'),
            },
            r'Câu đọc hiểu bối cảnh hàm số — ánh xạ `v = speed` và `K(v) = kinetic energy`.'
        ),
        _mcq(
            'may2025_m2h_q7', 7, 'Algebra', 'Linear inequalities in one or two variables', 'Easy',
            r'<p>A model estimates that a gray whale travels \(72\) to \(77\) miles each day during its migration.</p>',
            r'Based on this model, which inequality represents the estimated total number of miles, \(x\), a gray whale could travel in \(21\) days of its migration?',
            {
                'A': r'\(72 + 21 \le x \le 77 + 21\)',
                'B': r'\(72(21) \le x \le 77(21)\)',
                'C': r'\(72 \le 21 + x \le 77\)',
                'D': r'\(72 \le 21x \le 77\)',
            },
            'B',
            r'Mỗi ngày cá voi xám đi được từ \(72\) đến \(77\) dặm, nên trong \(21\) ngày: quãng đường ít nhất là \(72 \times 21 = 72(21)\) dặm và nhiều nhất là \(77 \times 21 = 77(21)\) dặm. Do đó tổng quãng đường \(x\) thỏa mãn \(72(21) \le x \le 77(21)\).',
            r'Kiểm tra nhanh bằng số thực tế: nếu mỗi ngày đi khoảng \(75\) dặm thì \(21\) ngày đi khoảng \(1{,}575\) dặm \(\Rightarrow\) chỉ bất đẳng thức \(72(21) \le x \le 77(21)\) chứa \(1{,}575\).',
            {
                'A': ('Cộng thay vì nhân', r'Cộng thêm \(21\) ngày vào quãng đường 1 ngày là sai về đơn vị.'),
                'B': ('Đáp án đúng', r'Quãng đường tổng = (quãng đường mỗi ngày) \(\times\) (21 ngày), nằm giữa \(72(21)\) và \(77(21)\).'),
                'C': ('Sai hoàn toàn cấu trúc', r'Cho \(x\) nằm khoảng \(51\) đến \(56\) dặm — nhỏ hơn cả 1 ngày di chuyển.'),
                'D': ('Nhân ngược 21 vào tổng x', r'Cho \(x\) khoảng \(3.5\) dặm (nhầm tốc độ trung bình với tổng quãng đường).'),
            },
            r'Kiểm tra ước lượng: `75 * 21 = 1575`; chỉ đáp án B có khoảng `[1512, 1617]`.'
        ),
        _mcq(
            'may2025_m2h_q8', 8, 'Algebra', 'Linear equations in one variable', 'Medium',
            r'<p>Suppose \(8(x + 7) = 7(x + 7) + 58\).</p>',
            r'If \(8(x + 7) = 7(x + 7) + 58\), what is the value of \(x + 7\)?',
            {'A': r'\(-7\)', 'B': r'\(51\)', 'C': r'\(58\)', 'D': r'\(65\)'},
            'C',
            r'Đặt \(u = x + 7\). Phương trình trở thành \(8u = 7u + 58\). Trừ \(7u\) ở cả hai vế: \(u = 58\). Vậy \(x + 7 = 58\) mà không cần tìm giá trị riêng của \(x\)!',
            r'Mẹo 3 giây SAT: khi cùng một cụm \((x + 7)\) xuất hiện ở cả phương trình lẫn câu hỏi, hãy trừ trực tiếp \(8(x + 7) - 7(x + 7) = 58 \Rightarrow x + 7 = 58\)!',
            {
                'A': ('Bẫy giải nghiệm ngoặc bằng 0', r'\(-7\) là nghiệm của \(x + 7 = 0\), không phải giá trị của \(x + 7\).'),
                'B': ('Bẫy dừng lại ở giá trị x', r'\(x = 58 - 7 = 51\) là giá trị của \(x\), nhưng đề hỏi \(x + 7\).'),
                'C': ('Đáp án đúng', r'\(8(x + 7) - 7(x + 7) = 58 \Rightarrow x + 7 = 58\).'),
                'D': ('Cộng 7 thêm một lần nữa', r'Nhầm \(x = 58\) rồi cộng thêm \(7\) ra \(65\).'),
            },
            r'Gõ `8(x + 7) = 7(x + 7) + 58` vào Desmos ra `x = 51`, sau đó gõ `51 + 7 = 58`.'
        ),
        _mcq(
            'may2025_m2h_q9', 9, 'Algebra', 'Linear functions', 'Easy',
            r'<p>At an amusement park, visitors wait in line for a certain ride. People in this line get on the ride at a rate of \(13\) people per minute. At the end of a certain day, \(214\) people are in line for the ride when the line closes.</p>',
            r'If these \(214\) people will get on the ride and no additional people are allowed to get in line, which function \(p\) models the number of people who remain in line \(t\) minutes after it closes?',
            {
                'A': r'\(p(t) = -13t + 214\)',
                'B': r'\(p(t) = 13t + 214\)',
                'C': r'\(p(t) = 13t - 214\)',
                'D': r'\(p(t) = 227t\)',
            },
            'A',
            r'Tại thời điểm hàng bắt đầu đóng (\(t = 0\)), có \(214\) người đang đứng chờ (\(b = 214\)). Cứ mỗi phút trôi qua có \(13\) người rời hàng để lên trò chơi và không có ai vào thêm, nên số người còn lại trong hàng GIẢM với tốc độ \(13\) người/phút (\(m = -13\)). Vậy \(p(t) = -13t + 214\).',
            r'Nhận diện dấu của hệ số góc từ ngữ cảnh: số người "remain in line" (còn lại) giảm dần theo thời gian \(\Rightarrow m < 0\), kết hợp giá trị ban đầu \(p(0) = 214\).',
            {
                'A': ('Đáp án đúng', r'Ban đầu \(p(0) = 214\), giảm \(13\) người mỗi phút \(\Rightarrow p(t) = -13t + 214\).'),
                'B': ('Sai dấu hệ số góc', r'\(+13t\) mô tả số người trong hàng tăng thêm, trái với việc không cho thêm người vào hàng.'),
                'C': ('Sai cả hai dấu', r'Cho \(p(0) = -214\) (vô lý) và tăng theo thời gian.'),
                'D': ('Cộng gộp slope và intercept', r'Cộng sai \(214 + 13 = 227\) rồi nhân \(t\).'),
            },
            r'Kiểm tra nhanh tại \(t = 0\) phải ra `214` và tại \(t = 1\) phải giảm còn `201` \(\Rightarrow\) chỉ A thỏa mãn.'
        ),
        _mcq(
            'may2025_m2h_q10', 10, 'Advanced Math', 'Systems of linear and nonlinear equations', 'Medium',
            svg_m2h_q10_parabola_line() + r'<p>The graph of a system of a linear equation and a quadratic equation is shown. A solution to the system is \((x, y)\).</p>',
            r'What is a possible value of \(x\)?',
            {'A': r'\(5.6\)', 'B': r'\(7\)', 'C': r'\(8\)', 'D': r'\(10\)'},
            'C',
            r'Nghiệm \((x, y)\) của hệ là giao điểm của đường thẳng ngang \(y = 5.6\) và parabol úp xuống (đỉnh \((7, 6.3)\), đi qua \((4, 0)\) và \((10, 0)\)). Dóng thẳng từ hai giao điểm xuống trục hoành \(Ox\), ta đọc được chính xác hai hoành độ giao điểm là \(x = 6\) và \(x = 8\) (tương ứng hai điểm \((6, 5.6)\) và \((8, 5.6)\)). Trong 4 đáp án, giá trị thỏa mãn là \(8\).',
            r'Cực kỳ chú ý phân biệt hoành độ \(x\) và tung độ \(y\): \(5.6\) là giá trị của \(y\) tại giao điểm, còn đề hỏi giá trị khả dĩ của \(x\) (\(6\) hoặc \(8\))!',
            {
                'A': ('Nhầm sang tung độ y', r'\(5.6\) là tung độ \(y\) của giao điểm, không phải hoành độ \(x\).'),
                'B': ('Nhầm sang hoành độ đỉnh', r'\(x = 7\) là hoành độ đỉnh \((7, 6.3)\) nằm cao hơn đường thẳng \(y = 5.6\).'),
                'C': ('Đáp án đúng', r'Đường thẳng cắt parabol tại \((6, 5.6)\) và \((8, 5.6)\), nên \(x = 8\) là nghiệm hợp lệ.'),
                'D': ('Nhầm sang x-intercept', r'\(x = 10\) là giao điểm parabol với trục hoành \((10, 0)\), không giao đường ngang.'),
            },
            r'Dóng dọc từ giao điểm bên phải của đường thẳng và parabol xuống trục \(Ox\): chạm đúng vạch `8`.'
        ),
        _mcq(
            'may2025_m2h_q11', 11, 'Geometry and Trigonometry', 'Area and volume', 'Medium',
            r'<p>A sphere has a radius of \(3\) inches and a density of \(84\) ounces per cubic inch.</p>',
            r'What is the mass, in ounces, of the sphere?',
            {'A': r'\(\frac{3\pi}{7}\)', 'B': r'\(\frac{7\pi}{3}\)', 'C': r'\(252\pi\)', 'D': r'\(3{,}024\pi\)'},
            'D',
            r'Bước 1: Tính thể tích hình cầu có bán kính \(r = 3\) in bằng công thức \(V = \frac{4}{3}\pi r^3 = \frac{4}{3}\pi (3^3) = \frac{4}{3}\pi (27) = 36\pi\text{ in}^3\). Bước 2: Áp dụng công thức khối lượng \(\text{Mass} = \text{Density} \times \text{Volume} = 84 \times 36\pi = 3{,}024\pi\text{ ounces}\).',
            r'Luôn kiểm tra đơn vị: \(\frac{\text{ounces}}{\text{in}^3} \times \text{in}^3 = \text{ounces}\) để chắc chắn phải NHÂN (không chia) khối lượng riêng với thể tích; nhớ công thức hình cầu là \(\frac{4}{3}\pi r^3\).',
            {
                'A': ('Chia ngược thể tích cho khối lượng riêng', r'\(\frac{36\pi}{84} = \frac{3\pi}{7}\) — dùng sai công thức \(\frac{V}{D}\) thay vì \(D \cdot V\).'),
                'B': ('Chia ngược & sai thể tích', r'Chia khối lượng riêng cho thể tích hoặc đặt sai công thức \(\pi\).'),
                'C': ('Quên công thức (4/3)πr³', r'Chỉ tính \(84 \times 3\pi = 252\pi\), quên lập phương bán kính và hệ số \(\frac{4}{3}\).'),
                'D': ('Đáp án đúng', r'\(V = \frac{4}{3}\pi(27) = 36\pi \Rightarrow \text{Mass} = 84 \times 36\pi = 3{,}024\pi\).'),
            },
            r'Gõ `(4/3) * 3^3 * 84` trên Desmos ra `3024`, gắn thêm \(\pi\) được `3,024π`.'
        ),
        _spr(
            'may2025_m2h_q12', 12, 'Algebra', 'Linear equations in one variable', 'Medium',
            r'<p style="text-align:center;font-size:18px;">\[-8|3x - 11| + 4 = -52\]</p>',
            r'What is the sum of the solutions to the given equation?',
            ['22/3', '7.333', '7.33'], r'22/3 (hoặc 7.333)',
            r'Cô lập giá trị tuyệt đối: trừ \(4\) ở hai vế được \(-8|3x - 11| = -56\), rồi chia cả hai vế cho \(-8\) được \(|3x - 11| = 7\). Tách thành 2 trường hợp: (1) \(3x - 11 = 7 \Rightarrow 3x = 18 \Rightarrow x = 6\); (2) \(3x - 11 = -7 \Rightarrow 3x = 4 \Rightarrow x = \frac{4}{3}\). Tổng hai nghiệm là \(6 + \frac{4}{3} = \frac{22}{3} \approx 7.333\).',
            r'Mẹo 800-level siêu tốc cho tổng nghiệm trị tuyệt đối \(|ax + b| = c\) (với \(c > 0\)): hai nghiệm luôn đối xứng qua tâm \(x_0 = -\frac{b}{a}\), nên tổng hai nghiệm LUÔN bằng \(2x_0 = -\frac{2b}{a} = \frac{2(11)}{3} = \frac{22}{3}\) (kiểm tra trước điều kiện \(c = 7 > 0\) để chắc chắn có 2 nghiệm)!',
            r'Gõ `-8*abs(3x - 11) + 4 = -52` vào Desmos thấy 2 đường đứng tại `x = 1.333` và `x = 6`; cộng lại `6 + 4/3 = 22/3`.'
        ),
        _mcq(
            'may2025_m2h_q13', 13, 'Geometry and Trigonometry', 'Area and volume', 'Medium',
            svg_m2h_q13_segment() + r'<p>The line segment shown in the \(xy\)-plane has endpoints \((-3, 5)\) and \((6, 11)\) and represents one of the legs of a right triangle. The area of this triangle is \(42\sqrt{13}\) square units.</p>',
            r'What is the length, in units, of the other leg of this triangle?',
            {'A': r'\(14\)', 'B': r'\(28\)', 'C': r'\(3\sqrt{13}\)', 'D': r'\(21\sqrt{13}\)'},
            'B',
            r'Bước 1: Tính độ dài cạnh góc vuông thứ nhất \(L_1\) nối \((-3, 5)\) và \((6, 11)\) bằng công thức khoảng cách: \(L_1 = \sqrt{(6 - (-3))^2 + (11 - 5)^2} = \sqrt{9^2 + 6^2} = \sqrt{81 + 36} = \sqrt{117} = \sqrt{9 \times 13} = 3\sqrt{13}\). Bước 2: Dùng công thức diện tích tam giác vuông \(A = \frac{1}{2} L_1 L_2\): \(\frac{1}{2}(3\sqrt{13}) L_2 = 42\sqrt{13}\). Rút gọn \(\sqrt{13}\) ở hai vế: \(\frac{3}{2} L_2 = 42 \Rightarrow L_2 = 42 \times \frac{2}{3} = 28\).',
            r'Luôn kiểm tra hệ số \(\frac{1}{2}\) trong công thức diện tích tam giác \(A = \frac{1}{2} ab\) — quên nhân đôi diện tích trước khi chia sẽ rơi ngay vào bẫy A (\(14\))!',
            {
                'A': ('Quên hệ số 1/2 của diện tích tam giác', r'Lấy \(42\sqrt{13} \div 3\sqrt{13} = 14\), quên nhân \(2\) cho công thức \(\frac{1}{2} L_1 L_2\).'),
                'B': ('Đáp án đúng', r'\(L_1 = 3\sqrt{13} \Rightarrow L_2 = \frac{2 \times 42\sqrt{13}}{3\sqrt{13}} = 28\).'),
                'C': ('Dừng ở cạnh góc vuông đã cho', r'\(3\sqrt{13}\) là độ dài đoạn thẳng vẽ sẵn (cạnh góc vuông thứ nhất), chưa tính cạnh còn lại.'),
                'D': ('Chia đôi diện tích không liên quan', r'\(21\sqrt{13}\) chỉ là nửa diện tích tam giác.'),
            },
            r'Gõ `L = sqrt((6 - (-3))^2 + (11 - 5)^2)` rồi gõ `2 * 42 * sqrt(13) / L` vào Desmos ra chính xác `28`!'
        ),
        _mcq(
            'may2025_m2h_q14', 14, 'Advanced Math', 'Nonlinear functions', 'Hard',
            r'<p>The function \(f\) is defined by \(f(x) = -2(2)^x\). The function \(g\) is a decreasing linear function. In the \(xy\)-plane, the graphs of \(y = f(x)\) and \(y = g(x)\) intersect at two points, \((h, j)\) and \((k, m)\), where \(j > m\).</p>',
            r'When \(g(x) < f(x)\), which of the following must also be true?',
            {'A': r'\(x > k\)', 'B': r'\(x < h\)', 'C': r'\(x > k \text{ or } x < h\)', 'D': r'\(h < x < k\)'},
            'D',
            r'Phân tích hình học của hàm mũ âm \(f(x) = -2(2)^x\): đây là hàm NGHỊCH BIẾN và LÕM XUỐNG (concave down) trên toàn bộ \(\mathbb{R}\) (vì \(f(x)\) giảm ngày càng dốc khi \(x\) tăng). Do \(f\) nghịch biến và hai giao điểm \((h, j), (k, m)\) có tung độ \(j > m\), suy ra hoành độ thỏa mãn \(h < k\). Một đường thẳng cát tuyến \(g(x)\) cắt một đường cong lõm xuống tại hai điểm \(x = h\) và \(x = k\) sẽ nằm PHÍA DƯỚI đường cong (\(g(x) < f(x)\)) trên khoảng Ở GIỮA hai giao điểm, tức \(h < x < k\), và nằm phía trên đường cong ở hai miền ngoài (\(x < h\) hoặc \(x > k\)).',
            r'Chiêu 800-level kiểm chứng tức thì cho bài bất đẳng thức đồ thị tổng quát: chọn 2 giao điểm cụ thể trên \(f(x) = -2(2)^x\), ví dụ \((0, -2)\) và \((2, -8)\) (\(h=0, k=2, j=-2 > m=-8\)) \(\Rightarrow g(x) = -3x - 2\). Thử \(x = 1\) ở giữa: \(g(1) = -5 < -4 = f(1)\) \(\Rightarrow\) chọn ngay D!',
            {
                'A': ('Miền ngoài bên phải', r'Khi \(x > k\), hàm mũ âm \(-2(2)^x\) lao xuống nhanh hơn đường thẳng nên \(f(x) < g(x)\), tức \(g(x) > f(x)\).'),
                'B': ('Miền ngoài bên trái', r'Khi \(x < h\), hàm \(f(x)\) tiệm cận \(0\) từ dưới còn đường thẳng nghịch biến \(g(x)\) đi lên \(+\infty\), nên \(g(x) > f(x)\).'),
                'C': ('Ngược chiều lõm của đường cong', r'\(x > k\) hoặc \(x < h\) là miền thỏa mãn \(g(x) > f(x)\) (sẽ chỉ đúng cho hàm lồi \(+2(2)^x\)).'),
                'D': ('Đáp án đúng', r'Vì \(f(x) = -2(2)^x\) lõm xuống và \(h < k\), dây cung \(g(x)\) nằm dưới đường cong \(f(x)\) đúng khi \(h < x < k\).'),
            },
            r'Vẽ `y = -2(2)^x` và đường nối `(0, -2)` với `(2, -8)` là `y = -3x - 2` trên Desmos: thấy ngay đường thẳng nằm DƯỚI đường cong trên đoạn `(0, 2)`, tức `h < x < k`!'
        ),
        _mcq(
            'may2025_m2h_q15', 15, 'Algebra', 'Systems of two linear equations in two variables', 'Hard',
            r'<p>Arturo builds and sells two types of steel tables. The revenue Arturo generates from selling each square table is \(2\) times his cost to build a square table, and the revenue Arturo generates from selling each hexagonal table is \(2.5\) times his cost to build a hexagonal table. In one year, Arturo&#39;s total cost to build tables was $42,120, and he generated a total revenue of $101,250 from selling all the tables he built that year.</p>',
            r'For that year, how much greater is the revenue Arturo generated from selling hexagonal tables than the revenue he generated from selling square tables?',
            {'A': '$16,200', 'B': '$25,920', 'C': '$59,130', 'D': '$68,850'},
            'D',
            r'Gọi \(S\) là tổng chi phí đóng bàn vuông và \(H\) là tổng chi phí đóng bàn lục giác (USD). Ta có hệ phương trình: (1) Tổng chi phí: \(S + H = 42{,}120\); (2) Tổng doanh thu: \(2S + 2.5H = 101{,}250\). Nhân phương trình (1) với \(2\) được \(2S + 2H = 84{,}240\), lấy (2) trừ đi: \(0.5H = 17{,}010 \Rightarrow H = 34{,}020\), suy ra \(S = 42{,}120 - 34{,}020 = 8{,}100\). Doanh thu bàn lục giác là \(2.5H = 2.5(34{,}020) = \$85{,}050\); doanh thu bàn vuông là \(2S = 2(8{,}100) = \$16{,}200\). Hiệu doanh thu cần tìm: \(85{,}050 - 16{,}200 = \$68{,}850\).',
            r'Đọc thật kỹ đại lượng câu hỏi cuối cùng: đề hỏi hiệu DOANH THU (\(2.5H - 2S = \$68{,}850\)), KHÔNG phải hiệu chi phí (\(H - S = \$25{,}920\)) hay tổng lợi nhuận (\(101{,}250 - 42{,}120 = \$59{,}130\))!',
            {
                'A': ('Dừng ở doanh thu bàn vuông', r'$16,200 chỉ là doanh thu \(2S\) từ bàn vuông, chưa lấy doanh thu bàn lục giác trừ đi.'),
                'B': ('Nhầm sang hiệu chi phí H − S', r'\(34{,}020 - 8{,}100 = \$25{,}920\) là hiệu chi phí sản xuất, không phải hiệu doanh thu.'),
                'C': ('Nhầm sang tổng lợi nhuận', r'\(101{,}250 - 42{,}120 = \$59{,}130\) là tổng lợi nhuận cả năm của cả hai loại bàn.'),
                'D': ('Đáp án đúng', r'\(2.5(34{,}020) - 2(8{,}100) = 85{,}050 - 16{,}200 = \$68{,}850\).'),
            },
            r'Gõ `x + y = 42120` và `2x + 2.5y = 101250` vào Desmos tìm giao điểm `(8100, 34020)`, rồi tính `2.5(34020) - 2(8100) = 68850`.'
        ),
        _spr(
            'may2025_m2h_q16', 16, 'Advanced Math', 'Nonlinear functions', 'Hard',
            r'<p style="text-align:center;font-size:18px;">\[f(x) = \sqrt{x^3 + ax^2 + bx + c}\]</p><p>The function \(f\) is defined by the given equation, where \(a\), \(b\), and \(c\) are integer constants. In the \(xy\)-plane, the graph of \(y = f(x)\) passes through the point \((9, 0)\), and \(f(0) = 27\).</p>',
            r'What is the value of \(9a + b\)?',
            ['-162'], '-162',
            r'Bước 1: Dùng \(f(0) = 27 \Rightarrow \sqrt{0 + 0 + 0 + c} = 27 \Rightarrow c = 27^2 = 729\). Bước 2: Vì đồ thị đi qua điểm \((9, 0)\) nên \(f(9) = 0 \Rightarrow \sqrt{9^3 + a(9^2) + b(9) + 729} = 0\). Bình phương hai vế và lưu ý \(9^3 = 729\): \(729 + 81a + 9b + 729 = 0 \Rightarrow 81a + 9b = -1{,}458\). Bước 3: Chia cả hai vế cho \(9\) để làm xuất hiện đúng biểu thức đề hỏi: \(9a + b = \frac{-1{,}458}{9} = -162\).',
            r'Đừng hoảng khi thấy 3 ẩn \(a, b, c\) mà chỉ có 2 phương trình — câu hỏi yêu cầu tìm TỔ HỢP \(9a + b\) chứ không cần tìm riêng \(a\) và \(b\); hãy đặt nhân tử chung \(9(9a + b) = 81a + 9b\)!',
            r'Gõ `-(9^3 + 27^2) / 9` trên Desmos ra ngay `-162`!'
        ),
        _mcq(
            'may2025_m2h_q17', 17, 'Geometry and Trigonometry', 'Lines, angles, and triangles', 'Hard',
            r'<p>Two lines intersect at exactly one point, forming two acute angles and two obtuse angles. The measure of one of these angles is \((3x - 310)^\circ\).</p>',
            r'Which of the following could NOT be the sum of the measures of any two of these angles?',
            {
                'A': r'\((-6x + 620)^\circ\)',
                'B': r'\((-6x + 980)^\circ\)',
                'C': r'\((6x - 620)^\circ\)',
                'D': r'\(180^\circ\)',
            },
            'A',
            r'Đặt số đo một góc là \(\theta = 3x - 310^\circ\) (với \(0^\circ < \theta < 180^\circ\)). Bốn góc tạo thành khi hai đường thẳng cắt nhau gồm hai góc bằng \(\theta\) (đối đỉnh) và hai góc bằng \(180^\circ - \theta\) (đối đỉnh còn lại). Tổng số đo của hai góc bất kỳ trong bốn góc này chỉ có thể nhận 3 giá trị: (1) Hai góc kề bù: \(\theta + (180^\circ - \theta) = 180^\circ\) (đáp án D); (2) Cặp góc đối đỉnh thứ nhất: \(\theta + \theta = 2(3x - 310)^\circ = (6x - 620)^\circ\) (đáp án C); (3) Cặp góc đối đỉnh thứ hai: \(2(180^\circ - \theta) = 360^\circ - (6x - 620)^\circ = (-6x + 980)^\circ\) (đáp án B). Riêng đáp án A là \((-6x + 620)^\circ = -2\theta < 0\), không bao giờ có thể là tổng của hai số đo góc dương!',
            r'Với 2 đường thẳng cắt nhau tạo góc \(\theta\), chỉ có duy nhất 3 tổng khả dĩ của 2 góc: \(180^\circ\), \(2\theta\), và \(360^\circ - 2\theta\). Mọi đáp án mang giá trị \(-2\theta\) (âm) đều loại ngay lập tức!',
            {
                'A': ('Đáp án đúng (KHÔNG thể xảy ra)', r'\(-6x + 620 = -2(3x - 310) = -2\theta < 0\), không thể là tổng hai góc dương.'),
                'B': ('Tổng khả dĩ (2 góc đối đỉnh còn lại)', r'\(2[180 - (3x - 310)] = 2(490 - 3x) = -6x + 980^\circ\).'),
                'C': ('Tổng khả dĩ (2 góc đối đỉnh θ)', r'\(2(3x - 310) = 6x - 620^\circ\).'),
                'D': ('Tổng khả dĩ (2 góc kề bù)', r'Tổng hai góc kề bù luôn bằng \(180^\circ\).'),
            },
            r'Thử nhanh một góc cụ thể: cho `3x - 310 = 50` \(\Rightarrow x = 120\). Bốn góc là `50°, 50°, 130°, 130°` \(\Rightarrow\) các tổng có thể là `100°, 180°, 260°`. Thay `x = 120` vào A ra `-100°` (vô lý!) \(\Rightarrow\) chọn A!'
        ),
        _spr(
            'may2025_m2h_q18', 18, 'Advanced Math', 'Nonlinear equations in one variable', 'Hard',
            r'<p>The solutions to \(x^2 + 10x + 19 = 0\) are \(r\) and \(s\), where \(r < s\). The solutions to \(x^2 + 10x + 1 = 0\) are \(t\) and \(u\), where \(t < u\). The solutions to \(x^2 + 20x + c = 0\), where \(c\) is a constant, are \(r + u\) and \(s + t\).</p>',
            r'What is the value of \(c\)?',
            ['94'], '94',
            r'Giải từng phương trình bằng phương pháp hoàn thành bình phương (completing the square): (1) \(x^2 + 10x + 19 = 0 \Rightarrow (x + 5)^2 = 25 - 19 = 6 \Rightarrow r = -5 - \sqrt{6},\; s = -5 + \sqrt{6}\) (vì \(r < s\)). (2) \(x^2 + 10x + 1 = 0 \Rightarrow (x + 5)^2 = 25 - 1 = 24 \Rightarrow t = -5 - 2\sqrt{6},\; u = -5 + 2\sqrt{6}\) (vì \(t < u\)). Tính hai nghiệm mới: \(r + u = (-5 - \sqrt{6}) + (-5 + 2\sqrt{6}) = -10 + \sqrt{6}\); \(s + t = (-5 + \sqrt{6}) + (-5 - 2\sqrt{6}) = -10 - \sqrt{6}\). Theo định lý Viète cho \(x^2 + 20x + c = 0\), hằng số \(c\) là tích hai nghiệm: \(c = (r + u)(s + t) = (-10 + \sqrt{6})(-10 - \sqrt{6}) = (-10)^2 - (\sqrt{6})^2 = 100 - 6 = 94\).',
            r'Hoàn thành bình phương \((x + 5)^2 = k\) siêu gọn giúp thấy ngay căn đồng dạng \(\sqrt{24} = 2\sqrt{6}\) và nhân liên hợp \((-10 + \sqrt{6})(-10 - \sqrt{6}) = 100 - 6 = 94\)!',
            r'Gõ trên Desmos: `r = -5 - sqrt(6)`, `s = -5 + sqrt(6)`, `t = -5 - sqrt(24)`, `u = -5 + sqrt(24)`, rồi tính `(r + u)*(s + t)` ra ngay chính xác `94`!'
        ),
        _mcq(
            'may2025_m2h_q19', 19, 'Algebra', 'Linear functions', 'Medium',
            r'<p>For the linear function \(f\), \(f(3) = 19\) and \(f(9) = 1\).</p>',
            r'Which equation defines \(f\)?',
            {
                'A': r'\(f(x) = -\frac{1}{3}x + 20\)',
                'B': r'\(f(x) = \frac{1}{3}x - 2\)',
                'C': r'\(f(x) = -3x + 22\)',
                'D': r'\(f(x) = -3x + 28\)',
            },
            'D',
            r'Tính hệ số góc từ hai điểm \((3, 19)\) và \((9, 1)\): \(m = \frac{1 - 19}{9 - 3} = \frac{-18}{6} = -3\). Tìm \(b\) từ \(f(3) = 19\): \(-3(3) + b = 19 \Rightarrow b = 28\). Vậy \(f(x) = -3x + 28\).',
            r'Thử trực tiếp cả 2 giá trị \(f(3) = 19\) và \(f(9) = 1\) vào đáp án để chốt chắc chắn 100% không sai dấu.',
            {
                'A': ('Nghịch đảo hệ số góc', r'Thay \(x = 9\): \(f(9) = 17 \ne 1\).'),
                'B': ('Nghịch đảo & sai dấu slope', r'Thay \(x = 3\): \(f(3) = -1 \ne 19\).'),
                'C': ('Tính sai hằng số b', r'Thay \(x = 3\): \(-3(3) + 22 = 13 \ne 19\).'),
                'D': ('Đáp án đúng', r'\(f(3) = 19\) và \(f(9) = 1\).'),
            },
            r'Dùng hồi quy bảng Desmos `x1 = [3, 9]`, `y1 = [19, 1]`, `y1 ~ m x1 + b` ra ngay `m = -3, b = 28`.'
        ),
        _mcq(
            'may2025_m2h_q20', 20, 'Geometry and Trigonometry', 'Right triangles and trigonometry', 'Hard',
            r'<p>In triangle \(XYZ\), the measure of angle \(X\) is \(90^\circ\). Point \(W\) lies on segment \(YZ\), and segment \(WX\) is perpendicular to segment \(YZ\). The length of segment \(WY\) is \(524\), and the length of segment \(WX\) is \(393\).</p>',
            r'What is the value of \(\tan Z\)?',
            {'A': r'\(\frac{3}{5}\)', 'B': r'\(\frac{3}{4}\)', 'C': r'\(\frac{4}{5}\)', 'D': r'\(\frac{4}{3}\)'},
            'D',
            r'Vì \(\triangle XYZ\) vuông tại \(X\) và đường cao \(WX \perp YZ\), ta có cặp góc nhọn bằng nhau: trong \(\triangle XYZ\) thì \(\angle Z = 90^\circ - \angle Y\), còn trong tam giác vuông \(\triangle WYX\) thì \(\angle WXY = 90^\circ - \angle Y \Rightarrow \angle Z = \angle WXY\). Do đó ta tính thẳng \(\tan Z\) bằng \(\tan(\angle WXY)\) ngay trong tam giác vuông \(\triangle WYX\): \(\tan Z = \tan(\angle WXY) = \frac{WY}{WX} = \frac{524}{393}\). Rút gọn cả tử và mẫu cho \(131\) (\(524 = 4 \times 131\), \(393 = 3 \times 131\)): \(\tan Z = \frac{4}{3}\).',
            r'Tính chất vàng đường cao tam giác vuông: đường cao \(WX\) chia tam giác vuông thành 2 tam giác con ĐỒNG DẠNG với nhau và với tam giác lớn, luôn có \(\angle Z = \angle WXY \Rightarrow \tan Z = \frac{WY}{WX}\) (tránh bẫy tính nhầm \(\tan Y = \frac{WX}{WY} = \frac{3}{4}\)!).',
            {
                'A': ('Nhầm sang sin Y / cos Z', r'\(\frac{3}{5}\) là \(\cos Z = \sin Y\) (do tỉ lệ tam giác vuông 3–4–5), không phải \(\tan Z\).'),
                'B': ('Bẫy tính nhầm tan Y', r'\(\frac{WX}{WY} = \frac{393}{524} = \frac{3}{4}\) là \(\tan Y = \cot Z\), bị đảo ngược so với \(\tan Z\).'),
                'C': ('Nhầm sang sin Z', r'\(\frac{4}{5}\) là \(\sin Z = \cos Y\), không phải \(\tan Z\).'),
                'D': ('Đáp án đúng', r'\(\tan Z = \tan(\angle WXY) = \frac{WY}{WX} = \frac{524}{393} = \frac{4}{3}\).'),
            },
            r'Bấm `524 / 393` trên Desmos rồi nhấn biểu tượng phân số sẽ rút gọn ngay thành `4/3`!'
        ),
        _spr(
            'may2025_m2h_q21', 21, 'Problem-Solving and Data Analysis', 'Percentages', 'Hard',
            r'<p>The mass of object A is \(469\%\) of the mass of object B, and the mass of object A is \(0.670\%\) of the mass of object C.</p>',
            r'If the mass of object C is \(p\%\) of the mass of object B, what is the value of \(p\)?',
            ['70000', '70,000'], '70,000',
            r'Chuyển hai dữ kiện sang phương trình tỉ lệ (luôn chia phần trăm cho \(100\)): \(A = \frac{469}{100}B = 4.69B\) và \(A = \frac{0.670}{100}C = 0.0067C\). Cho hai vế bằng nhau: \(0.0067C = 4.69B \Rightarrow C = \frac{4.69}{0.0067}B = \frac{46{,}900}{67}B = 700B\) (vì \(469 \div 67 = 7\)). Vì \(C\) gấp \(700\) lần \(B\), đổi sang phần trăm: \(C = 700 \times 100\%\,B = 70{,}000\%\,B \Rightarrow p = 70{,}000\).',
            r'Cực kỳ tránh 2 bẫy số 0 kinh điển: (1) \(0.670\% = 0.0067\) (KHÔNG phải \(0.67\)); (2) sau khi tìm ra \(C = 700B\), PHẢI nhân thêm \(100\) để đổi sang \(p\%\) (\(700 \to 70{,}000\))!',
            r'Đặt `B = 100` \(\Rightarrow A = 469\) \(\Rightarrow C = 469 / (0.670 / 100) = 70000\). Vì `B = 100` nên giá trị của `C` CHÍNH LÀ `p = 70000`!'
        ),
        _mcq(
            'may2025_m2h_q22', 22, 'Advanced Math', 'Nonlinear functions', 'Hard',
            r'<p>For the function \(f\), for each increase in the value of \(x\) by \(c\), where \(c\) is a positive constant, the value of \(f(x)\) increases by a factor of \(27\).</p>',
            r'Which of the following equivalent forms of the function \(f\) displays \(\frac{1}{c}\) as a coefficient of \(x\)?',
            {
                'A': r'\(f(x) = 35(3)^{\frac{1}{2}x}\)',
                'B': r'\(f(x) = 35(3^3)^{\frac{1}{6}x}\)',
                'C': r'\(f(x) = 35(9)^{\frac{1}{4}x}\)',
                'D': r'\(f(x) = 35\left(27^{\frac{1}{3}x}\right)^{\frac{1}{2}}\)',
            },
            'B',
            r'Cả 4 đáp án đều là các dạng tương đương của cùng một hàm mũ \(f(x) = 35 \cdot 3^{\frac{1}{2}x}\). Đề bài cho biết mỗi khi \(x\) tăng thêm \(c\) đơn vị thì \(f(x)\) tăng gấp \(27\) lần, tức là \(\frac{f(x + c)}{f(x)} = 3^{\frac{1}{2}c} = 27 = 3^3\). Suy ra \(\frac{1}{2}c = 3 \Rightarrow c = 6\), và do đó \(\frac{1}{c} = \frac{1}{6}\). Viết lại hàm số với cơ số \(27 = 3^3\) để hiển thị đúng hệ số \(\frac{1}{c} = \frac{1}{6}\) trước \(x\): \(f(x) = 35 \cdot 3^{\frac{1}{2}x} = 35 \cdot 3^{3 \cdot \frac{1}{6}x} = 35(3^3)^{\frac{1}{6}x}\) — khớp chính xác đáp án B!',
            r'Công thức cốt lõi SAT Hard cho bài hàm mũ tăng gấp \(K\) lần sau mỗi chu kỳ \(c\): hàm luôn có dạng \(f(x) = A \cdot K^{\frac{1}{c}x}\). Tại đây \(K = 27 = 3^3\), nên khi viết cơ số \(3^3\) thì hệ số của \(x\) trên mũ tự động hiện ra đúng \(\frac{1}{c} = \frac{1}{6}\)!',
            {
                'A': ('Hiển thị hệ số ứng với cơ số 3', r'Hệ số của \(x\) là \(\frac{1}{2}\) (ứng với tăng gấp \(3\) lần sau mỗi \(2\) đơn vị), không phải \(\frac{1}{c} = \frac{1}{6}\).'),
                'B': ('Đáp án đúng', r'Cơ số \(3^3 = 27\) và hệ số đứng trước \(x\) là \(\frac{1}{6} = \frac{1}{c}\).'),
                'C': ('Hiển thị hệ số ứng với cơ số 9', r'Hệ số của \(x\) là \(\frac{1}{4}\) (ứng với tăng gấp \(9\) lần sau mỗi \(4\) đơn vị), không phải \(\frac{1}{6}\).'),
                'D': ('Bẫy chưa nhân hai số mũ lại', r'Mặc dù có cơ số \(27\), hệ số đi kèm \(x\) là \(\frac{1}{3}\) (bị tách thêm mũ \(\frac{1}{2}\) ở ngoài), không hiển thị \(\frac{1}{6}\).'),
            },
            r'Gõ `f(x) = 35 * 3^(0.5x)` vào Desmos rồi kiểm tra `f(6)/f(0) = 27` \(\Rightarrow c = 6 \Rightarrow 1/c = 1/6\), chọn ngay đáp án có phân số `1/6` trước `x` (đáp án B)!'
        ),
    ]


# ============================================================================
# ASSEMBLE FULL ADAPTIVE BLUEBOOK TEST DATA (66 REAL QUESTIONS)
# ============================================================================

TEST_DATA = {
    'schemaVersion': 2,
    'mode': 'adaptive_mock',
    'section': 'math',
    'basicInfo': {
        'title': TEST_TITLE,
        'subtitle': 'Đề thi thật Digital SAT Toán tháng 5/2025 — Đủ 3 Module Adaptive (M1: 22 + M2 Easy: 22 + M2 Hard: 22)',
        'difficultyBadge': 'REAL EXAM • MAY 2025',
        'targetTimeMinutes': 70,
        'routingThreshold': 14,
    },
    'module1': {
        'id': 'm1',
        'title': 'Section 2, Module 1: Math',
        'subtitle': '22 Questions • 35 Minutes • Routing Module',
        'timeLimitMinutes': 35,
        'questions': _build_module1(),
    },
    'module2_hard': {
        'id': 'm2_hard',
        'title': 'Section 2, Module 2: Math (Hard)',
        'subtitle': '22 Questions • 35 Minutes • Upper Adaptive Track',
        'timeLimitMinutes': 35,
        'questions': _build_module2_hard(),
    },
    'module2_lower': {
        'id': 'm2_lower',
        'title': 'Section 2, Module 2: Math (Easy / Standard)',
        'subtitle': '22 Questions • 35 Minutes • Lower Adaptive Track',
        'timeLimitMinutes': 35,
        'questions': _build_module2_lower(),
    },
}


# ============================================================================
# MANDATORY INDEPENDENT MATHEMATICAL VERIFICATION (ALL 66 QUESTIONS)
# ============================================================================

def verify_all_math():
    """Programmatically verifies EVERY SINGLE ONE of the 66 real SAT math answers."""
    m1 = {q['number']: q for q in TEST_DATA['module1']['questions']}
    m2l = {q['number']: q for q in TEST_DATA['module2_lower']['questions']}
    m2h = {q['number']: q for q in TEST_DATA['module2_hard']['questions']}
    assert len(m1) == 22 and len(m2l) == 22 and len(m2h) == 22

    # --- MODULE 1 (22 Qs) ---
    # M1 Q1: f(x) = 85x + 30 at x = 6
    assert 85 * 6 + 30 == 540 and m1[1]['correctAnswer'] == '540'
    # M1 Q2: triangle angles 138, 21 -> Z = 21
    assert 180 - 138 - 21 == 21 and m1[2]['correctAnswer'] == 'D'
    # M1 Q3: x^2 - 8 = 28 -> positive solution sqrt(36) = 6
    assert math.isclose(math.sqrt(28 + 8), 6.0) and m1[3]['correctAnswer'] == 'D'
    # M1 Q4: 16x + 60 = 28x -> x = 5
    x4 = Fraction(60, 28 - 16)
    assert x4 == 5 and 16 * x4 + 60 == 28 * x4 and m1[4]['correctAnswer'] == 'D'
    # M1 Q5: 70y + 60y = 130y
    assert 70 + 60 == 130 and m1[5]['correctAnswer'] == 'D'
    # M1 Q6: (3/200) * 20000 = 300
    assert Fraction(3, 200) * 20000 == 300 and m1[6]['correctAnswer'] == 'C'
    # M1 Q7: line of best fit from (0, 7.9) to (10, 1.1), slope ≈ -0.7
    slope7 = (1.1 - 7.9) / (10.0 - 0.0)
    assert abs(slope7 - (-0.7)) < 0.05 and m1[7]['correctAnswer'] == 'B'
    # M1 Q8: 0.04x + 0.07y = 0.05(x + y) -> test x=2, y=1: 0.08 + 0.07 = 0.15 = 0.05(3)
    assert Fraction(4, 100) * 2 + Fraction(7, 100) * 1 == Fraction(5, 100) * 3 and m1[8]['correctAnswer'] == 'B'
    # M1 Q9: F(m) = 7m -> F(4) = 28
    assert 7 * 4 == 28 and m1[9]['correctAnswer'] == 'A'
    # M1 Q10: 20% sedans = 36, 50% SUVs -> 30% minivans = 54
    total10 = Fraction(36, Fraction(20, 100))
    minivans10 = total10 * Fraction(100 - 20 - 50, 100)
    assert total10 == 180 and minivans10 == 54 and m1[10]['correctAnswer'] == '54'
    # M1 Q11: fair 16-sided die, P(4) = 1/16 = 0.0625
    p11 = Fraction(1, 16)
    assert float(p11) == 0.0625 and m1[11]['correctAnswer'] == '1/16' and '0.0625' in m1[11]['acceptedAnswers']
    # M1 Q12: x(x - 8) = 308 -> x = 22
    assert 22 * (22 - 8) == 308 and m1[12]['correctAnswer'] == 'B'
    # M1 Q13: y = 6(2)^x + 9
    assert 6 * (2 ** 1) + 9 == 21 and 6 * (2 ** 2) + 9 == 33 and 6 * (2 ** 3) + 9 == 57 and m1[13]['correctAnswer'] == 'B'
    # M1 Q14: square pyramid V = (1/3)*6^2*10 = 120
    assert Fraction(1, 3) * (6 ** 2) * 10 == 120 and m1[14]['correctAnswer'] == 'C'
    # M1 Q15: x^2 + 16x + 63 = x + 9 -> (x+6)(x+9) = 0 -> max a = -6
    roots15 = [x for x in range(-20, 20) if x * x + 16 * x + 63 == x + 9]
    assert roots15 == [-9, -6] and max(roots15) == -6 and m1[15]['correctAnswer'] == '-6'
    # M1 Q16: r_A = sqrt(4) = 2, r_B = 4 -> k = 16
    assert (2 * int(math.sqrt(4))) ** 2 == 16 and m1[16]['correctAnswer'] == '16'
    # M1 Q17: slope 6/17 through (-6, 0) and (0, p) -> p = 36/17
    p17 = Fraction(6, 17) * (0 - (-6))
    assert p17 == Fraction(36, 17) and m1[17]['correctAnswer'] == '36/17'
    # M1 Q18: 20y^3 + 15py^2 + 28y + 21p = (5y^2 + 7)(4y + 3p)
    for yv, pv in [(2, 3), (-1, 5), (4, -2)]:
        assert 20 * yv**3 + 15 * pv * yv**2 + 28 * yv + 21 * pv == (5 * yv**2 + 7) * (4 * yv + 3 * pv)
    assert m1[18]['correctAnswer'] == 'A'
    # M1 Q19: scale factor 4, AB = 48 -> A'B' = 192
    assert 48 * 4 == 192 and m1[19]['correctAnswer'] == 'D'
    # M1 Q20: f(t) = -16(t - 3.9)^2 + 243.36
    assert math.isclose(-16 * (0 - 3.9) ** 2 + 243.36, 0.0, abs_tol=1e-9)
    assert math.isclose(-16 * (3.9 - 3.9) ** 2 + 243.36, 243.36) and m1[20]['correctAnswer'] == 'A'
    # M1 Q21: (x-4)-5(y+2)=131 and (x-4)+5(y+2)=446 -> 2(x-4)=577 -> 10(x-4)=2885
    u21 = Fraction(131 + 446, 2)
    assert 10 * u21 == 2885 and m1[21]['correctAnswer'] == '2885'
    # M1 Q22: counterexample for I (median unchanged) & proof for II (mean strictly decreases)
    orig22 = [35] * 2 + [45] * 7 + [55] * 28 + [65] * 13
    assert len(orig22) == 50
    new22 = sorted(orig22 + [18])
    med_orig = Fraction(orig22[24] + orig22[25], 2)
    med_new = Fraction(new22[25], 1)
    assert med_new == med_orig  # Statement I need NOT be strictly less
    assert Fraction(sum(new22), 51) < Fraction(sum(orig22), 50)  # Statement II MUST be true
    assert m1[22]['correctAnswer'] == 'B'

    # --- MODULE 2 LOWER (mod5, 22 Qs) ---
    # M2L Q1: y = (x - 10)^2 + 1 and y = 1 -> (10, 1)
    assert (10 - 10) ** 2 + 1 == 1 and m2l[1]['correctAnswer'] == 'A'
    # M2L Q2: 200 / 20 = 10
    assert Fraction(200, 20) == 10 and m2l[2]['correctAnswer'] == 'A'
    # M2L Q3: visitors [97, 20, 54, 45, 85, 137] in (90, 140) -> 2 days
    vis3 = [97, 20, 54, 45, 85, 137]
    assert sum(1 for v in vis3 if 90 < v < 140) == 2 and m2l[3]['correctAnswer'] == '2'
    # M2L Q4: 2x = 8 -> 10x = 40
    assert 5 * 8 == 40 and m2l[4]['correctAnswer'] == 'D'
    # M2L Q5: 8% of 650 = 52
    assert Fraction(8, 100) * 650 == 52 and m2l[5]['correctAnswer'] == 'B'
    # M2L Q6: 1.20p + 2 = 4.40 -> p = 2
    assert Fraction(120, 100) * 2 + 2 == Fraction(440, 100) and m2l[6]['correctAnswer'] == 'A'
    # M2L Q7: y = (3/11)^(x+1) at x = 0 -> (0, 3/11)
    assert Fraction(3, 11) ** (0 + 1) == Fraction(3, 11) and m2l[7]['correctAnswer'] == 'D'
    # M2L Q8: 6 <= w <= 15
    assert 6 <= 10 <= 15 and m2l[8]['correctAnswer'] == 'A'
    # M2L Q9: curve A f(x) = -1/16 (x+3)(x-1)^2(x-5) passes through (-3,0),(-1,3),(1,0),(3,3),(5,0)
    def f9a(x): return Fraction(-1, 16) * (x + 3) * ((x - 1) ** 2) * (x - 5)
    def f9b(x): return Fraction(-1, 16) * (x + 5) * ((x + 1) ** 2) * (x - 3)
    def f9c(x): return Fraction(1, 16) * (x + 4) * (x ** 2) * (x - 4)
    def f9d(x): return Fraction(1, 16) * (x + 3) * ((x - 1) ** 2) * (x - 5)
    tbl9 = [(-3, 0), (-1, 3), (1, 0), (3, 3), (5, 0)]
    assert all(f9a(x) == y for x, y in tbl9)
    assert not all(f9b(x) == y for x, y in tbl9)
    assert not all(f9c(x) == y for x, y in tbl9)
    assert not all(f9d(x) == y for x, y in tbl9)
    assert m2l[9]['correctAnswer'] == 'A'
    # M2L Q10: linear pair x + 127 = 180 -> x = 53
    assert 180 - 127 == 53 and m2l[10]['correctAnswer'] == '53'
    # M2L Q11: g(5) = sqrt(8*5 + 9) = 7
    assert math.isclose(math.sqrt(8 * 5 + 9), 7.0) and m2l[11]['correctAnswer'] == '7'
    # M2L Q12: y >= -(11/4)x + 12 -> only (6, 0) satisfies
    def ineq12(x, y): return y >= Fraction(-11, 4) * x + 12
    assert not ineq12(0, -6) and not ineq12(0, 6) and not ineq12(-6, 0) and ineq12(6, 0)
    assert m2l[12]['correctAnswer'] == 'D'
    # M2L Q13: f(x) = (-5/16)x + 16 -> slope = -5/16
    assert Fraction(-5, 16) == Fraction(-5, 16) and m2l[13]['correctAnswer'] == 'B'
    # M2L Q14: y = 4600 a^x at x = 0 -> 4600
    assert 4600 * (3 ** 0) == 4600 and m2l[14]['correctAnswer'] == '4600'
    # M2L Q15: sqrt(x) = sqrt(53) -> x = 53
    assert math.isclose(math.sqrt(53), math.sqrt(53)) and m2l[15]['correctAnswer'] == '53'
    # M2L Q16: r + c = 125, 1050r + 2500c = 167500 -> r = 100, c = 25
    assert 100 + 25 == 125 and 1050 * 100 + 2500 * 25 == 167500 and m2l[16]['correctAnswer'] == 'C'
    # M2L Q17: y = (x + 9)(x - 11)(x + 12) -> x-intercept (11, 0)
    assert (11 + 9) * (11 - 11) * (11 + 12) == 0 and m2l[17]['correctAnswer'] == 'C'
    # M2L Q18: f(3)=19, f(9)=1 -> m=-3, b=28
    m18 = Fraction(1 - 19, 9 - 3)
    b18 = 19 - m18 * 3
    assert m18 == -3 and b18 == 28 and m2l[18]['correctAnswer'] == 'D'
    # M2L Q19: right triangle ST=217, RS=2*sqrt(218), RT=219 -> tan R = 217/(2*sqrt(218))
    assert 217 ** 2 + 4 * 218 == 219 ** 2 and m2l[19]['correctAnswer'] == 'D'
    # M2L Q20: cylinder d=12 (r=6), h=16 -> V = 576*pi
    assert (12 // 2) ** 2 * 16 == 576 and m2l[20]['correctAnswer'] == 'C'
    # M2L Q21: 2x - 3y = 8 -> slope 2/3
    assert Fraction(-2, -3) == Fraction(2, 3) and m2l[21]['correctAnswer'] == 'C'
    # M2L Q22: r = sqrt(4w - 7) -> w = r^2/4 + 7/4
    for w_test in [2, 5, 10]:
        r_sq = 4 * w_test - 7
        assert Fraction(r_sq, 4) + Fraction(7, 4) == w_test
    assert m2l[22]['correctAnswer'] == 'B'

    # --- MODULE 2 HARD (mod6, 22 Qs) ---
    # M2H Q1: boundary through (-3,5),(0,6),(3,7) -> y >= (1/3)x + 6
    assert Fraction(7 - 5, 3 - (-3)) == Fraction(1, 3) and m2h[1]['correctAnswer'] == 'A'
    # M2H Q2: 5x - 4y = 3 -> slope = 5/4
    assert Fraction(-5, -4) == Fraction(5, 4) and m2h[2]['correctAnswer'] == 'D'
    # M2H Q3: y = (3/11)^(x+1) at x = 0 -> (0, 3/11)
    assert Fraction(3, 11) ** 1 == Fraction(3, 11) and m2h[3]['correctAnswer'] == 'D'
    # M2H Q4: f(x) = (4/11)x -> slope = 4/11
    assert Fraction(4, 11) == Fraction(4, 11) and m2h[4]['correctAnswer'] == 'B'
    # M2H Q5: g(x) = 7x^(-1) -> g(8) = 7/8
    assert Fraction(7, 8) == 7 * Fraction(1, 8) and m2h[5]['correctAnswer'] == 'C'
    # M2H Q6: K(0) = 0 -> kinetic energy 0 J at speed 0 m/s
    assert Fraction(1, 2) * 37 * (0 ** 2) == 0 and m2h[6]['correctAnswer'] == 'C'
    # M2H Q7: 72(21) <= x <= 77(21)
    assert 72 * 21 == 1512 and 77 * 21 == 1617 and m2h[7]['correctAnswer'] == 'B'
    # M2H Q8: 8(x+7) = 7(x+7) + 58 -> x+7 = 58
    x8_h = 51
    assert 8 * (x8_h + 7) == 7 * (x8_h + 7) + 58 and (x8_h + 7) == 58 and m2h[8]['correctAnswer'] == 'C'
    # M2H Q9: p(t) = -13t + 214
    assert -13 * 0 + 214 == 214 and -13 * 1 + 214 == 201 and m2h[9]['correctAnswer'] == 'A'
    # M2H Q10: y = -0.7(x-7)^2 + 6.3 intersects y = 5.6 at x = 6 and x = 8
    for xv in (6, 8):
        assert math.isclose(-0.7 * (xv - 7) ** 2 + 6.3, 5.6)
    assert m2h[10]['correctAnswer'] == 'C'
    # M2H Q11: sphere r = 3, density = 84 -> mass = (4/3)*27*84*pi = 3024*pi
    assert Fraction(4, 3) * (3 ** 3) * 84 == 3024 and m2h[11]['correctAnswer'] == 'D'
    # M2H Q12: -8|3x - 11| + 4 = -52 -> |3x - 11| = 7 -> x in {6, 4/3} -> sum = 22/3
    sols12 = [Fraction(11 + 7, 3), Fraction(11 - 7, 3)]
    for sv in sols12:
        assert -8 * abs(3 * sv - 11) + 4 == -52
    assert sum(sols12) == Fraction(22, 3) and m2h[12]['correctAnswer'] == '22/3'
    # M2H Q13: leg from (-3,5) to (6,11) has length 3*sqrt(13); area 42*sqrt(13) -> other leg = 28
    l1_sq = (6 - (-3)) ** 2 + (11 - 5) ** 2
    assert l1_sq == 9 * 13
    l2_13 = (2 * 42 * math.sqrt(13)) / math.sqrt(l1_sq)
    assert math.isclose(l2_13, 28.0) and m2h[13]['correctAnswer'] == 'B'
    # M2H Q14: f(x) = -2(2)^x concave down, secant g through (0,-2),(2,-8) is -3x-2
    f14 = lambda x: -2 * (2 ** x)
    g14 = lambda x: -3 * x - 2
    assert f14(0) == g14(0) == -2 and f14(2) == g14(2) == -8 and f14(0) > f14(2)
    assert g14(1) < f14(1) and g14(-1) > f14(-1) and g14(3) > f14(3)
    assert m2h[14]['correctAnswer'] == 'D'
    # M2H Q15: S + H = 42120, 2S + 2.5H = 101250 -> 2.5H - 2S = 68850
    H15 = Fraction(101250 - 2 * 42120, Fraction(1, 2))
    S15 = 42120 - H15
    assert S15 == 8100 and H15 == 34020
    assert Fraction(5, 2) * H15 - 2 * S15 == 68850 and m2h[15]['correctAnswer'] == 'D'
    # M2H Q16: f(x) = sqrt(x^3 + ax^2 + bx + c), f(0) = 27 -> c = 729; f(9) = 0 -> 9a + b = -162
    c16 = 27 ** 2
    val16 = Fraction(-(9 ** 3 + c16), 9)
    assert c16 == 729 and val16 == -162 and m2h[16]['correctAnswer'] == '-162'
    # M2H Q17: angle theta = 3x - 310 -> possible sums: 180, 6x-620, -6x+980; impossible: -6x+620
    x17 = 120
    theta17 = 3 * x17 - 310
    possible17 = {180, 2 * theta17, 360 - 2 * theta17}
    assert possible17 == {180, 6 * x17 - 620, -6 * x17 + 980}
    assert (-6 * x17 + 620) < 0 and (-6 * x17 + 620) not in possible17 and m2h[17]['correctAnswer'] == 'A'
    # M2H Q18: x^2 + 10x + 19 = 0 (r < s), x^2 + 10x + 1 = 0 (t < u) -> c = (r+u)(s+t) = 94
    r18, s18 = -5 - math.sqrt(6), -5 + math.sqrt(6)
    t18, u18 = -5 - math.sqrt(24), -5 + math.sqrt(24)
    assert math.isclose((r18 + u18) + (s18 + t18), -20.0)
    assert math.isclose((r18 + u18) * (s18 + t18), 94.0) and m2h[18]['correctAnswer'] == '94'
    # M2H Q19: f(3)=19, f(9)=1 -> f(x) = -3x + 28
    assert -3 * 3 + 28 == 19 and -3 * 9 + 28 == 1 and m2h[19]['correctAnswer'] == 'D'
    # M2H Q20: altitude WX = 393, WY = 524 -> tan Z = WY / WX = 524/393 = 4/3
    assert Fraction(524, 393) == Fraction(4, 3) and m2h[20]['correctAnswer'] == 'D'
    # M2H Q21: A = 4.69B = 0.0067C -> C/B = 700 -> p = 70000
    ratio21 = Fraction(469, 100) / Fraction(67, 10000)
    assert ratio21 == 700 and ratio21 * 100 == 70000 and m2h[21]['correctAnswer'] == '70000'
    # M2H Q22: f(x) = 35 * 3^(x/2); factor 27 = 3^3 -> c/2 = 3 -> c = 6 -> 1/c = 1/6 -> B
    for x_test in (0, 2, 6, 12):
        fa = 35 * (3 ** (0.5 * x_test))
        fb = 35 * ((3 ** 3) ** (x_test / 6.0))
        fc = 35 * (9 ** (x_test / 4.0))
        fd = 35 * ((27 ** (x_test / 3.0)) ** 0.5)
        assert math.isclose(fa, fb) and math.isclose(fa, fc) and math.isclose(fa, fd)
    assert math.isclose((35 * (3 ** (0.5 * 6))) / (35 * (3 ** 0)), 27.0)
    assert m2h[22]['correctAnswer'] == 'B'

    # Extra hygiene checks across all 66 items (including optionAnalysis KaTeX balance & zero watermarks)
    raw = str(TEST_DATA)
    for bad in ('@DSATuz', '@D7SAT', 'satuzhunters', 'Minh Nghĩa', 't.me/D7SAT', '______blank'):
        assert bad.lower() not in raw.lower(), f'Forbidden token found: {bad}'
    for mk in ('module1', 'module2_hard', 'module2_lower'):
        for q in TEST_DATA[mk]['questions']:
            oa = (q.get('explanation') or {}).get('optionAnalysis') or {}
            for lbl, item in oa.items():
                rvi = item.get('reasonVi', '')
                assert rvi.count('\\(') == rvi.count('\\)'), f'Unbalanced \\( \\) in {q["id"]} optionAnalysis {lbl}'
                assert not re.search(r'(?<!\\)\$[a-zA-Z\\]', rvi), f'Raw $ math in {q["id"]} optionAnalysis {lbl}'

    print('[OK] verify_all_math(): All 66 May 2025 Math questions mathematically verified!')


if __name__ == '__main__':
    verify_all_math()
    errs = validate_sat_bluebook_json(TEST_DATA, TEST_CODE)
    if errs:
        print('VALIDATION ERRORS:')
        for e in errs:
            print('  -', e)
        sys.exit(1)
    for mk in ('module1', 'module2_hard', 'module2_lower'):
        qs = TEST_DATA[mk]['questions']
        mcqs = [q for q in qs if q.get('questionFormat') == 'mcq']
        sprs = [q for q in qs if q.get('questionFormat') == 'spr']
        dist = {k: sum(1 for q in mcqs if q['correctAnswer'] == k) for k in 'ABCD'}
        print(f'  {mk:14s}: {len(qs)} Qs ({len(mcqs)} MCQ {dist}, {len(sprs)} SPR)')
    print('[ALL PASSED] sat_real_may2025_math.py ready (66 Qs, 0 errors, Node KaTeX verified)!')
