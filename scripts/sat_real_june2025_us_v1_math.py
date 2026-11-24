# -*- coding: utf-8 -*-
r"""
Digital SAT 1500+ Real Past Exams — June 2025 US Ver 1 Math (44 Qs)
- Module 1: 22 verbatim questions (35 min) — 16 MCQ + 6 SPR
- Module 2: 22 verbatim questions (35 min) — 16 MCQ + 6 SPR
  (routingThreshold = 0; both module2_hard and module2_lower point to the real Module 2)

All formulas, numbers, coordinate graphs, data tables, and dot plots have been
verified pixel-by-pixel against the June 2025 US Ver 1 exam images & high-DPI PDF crops,
and all 44 answers are programmatically verified in `verify_all_math()`.
"""

from fractions import Fraction
import json
import math
import os
import re
import subprocess
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

from scripts.sat_real_exams_pipeline import validate_sat_bluebook_json

TEST_CODE = 'real_june2025_us_v1_math'
FOLDER_KEY = 'real_math'
ORDER_INDEX = 4
TEST_TITLE = '🏛️ Real Exam — June 2025 US Ver 1 Math (44 Qs)'


# ============================================================================
# BUILDERS
# ============================================================================

def _mcq(
    qid, number, domain, skill, difficulty,
    stimulus_html, question_html,
    options_dict, correct_label,
    summary_vi, key_takeaway, option_analysis,
    desmos_tip_vi='',
):
    assert correct_label in ('A', 'B', 'C', 'D'), f'Bad label {correct_label}'
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
    desmos_tip_vi='',
):
    assert len(accepted_answers) >= 1, 'Must provide at least one accepted answer'
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


def _html_table(headers, rows, caption=''):
    ths = ''.join(f'<th>{h}</th>' for h in headers)
    trs = ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>' for r in rows)
    cap = (
        f'<div style="font-weight:800;font-size:13.5px;color:#0f172a;text-align:center;margin-bottom:6px;">{caption}</div>'
        if caption else ''
    )
    return f'<div style="margin:10px 0;">{cap}<table><thead><tr>{ths}</tr></thead><tbody>{trs}</tbody></table></div>'


# ============================================================================
# EXACT BLUEBOOK-STYLE SVG DIAGRAMS (ZERO WATERMARKS)
# ============================================================================

def _svg_m1_q1_line():
    """Exact coordinate plane graph of y = -(1/5)x - 6 for M1 Q1."""
    cx, cy, step = 160, 160, 16
    parts = []
    # Gridlines -8..8
    for i in range(-8, 9):
        gx = cx + i * step
        gy = cy - i * step
        if i != 0:
            parts.append(
                f'<line x1="{gx}" y1="{cy - 8 * step - 4}" x2="{gx}" y2="{cy + 8 * step + 4}" '
                f'stroke="#cbd5e1" stroke-width="1"/>'
            )
            parts.append(
                f'<line x1="{cx - 8 * step - 4}" y1="{gy}" x2="{cx + 8 * step + 4}" y2="{gy}" '
                f'stroke="#cbd5e1" stroke-width="1"/>'
            )
    # Axes with arrowheads
    parts.append(
        f'<line x1="{cx - 8 * step - 8}" y1="{cy}" x2="{cx + 8 * step + 14}" y2="{cy}" '
        f'stroke="#0f172a" stroke-width="1.8"/>'
    )
    parts.append(
        f'<polygon points="{cx + 8 * step + 18},{cy} {cx + 8 * step + 10},{cy - 4} {cx + 8 * step + 10},{cy + 4}" '
        f'fill="#0f172a"/>'
    )
    parts.append(
        f'<line x1="{cx}" y1="{cy + 8 * step + 8}" x2="{cx}" y2="{cy - 8 * step - 14}" '
        f'stroke="#0f172a" stroke-width="1.8"/>'
    )
    parts.append(
        f'<polygon points="{cx},{cy - 8 * step - 18} {cx - 4},{cy - 8 * step - 10} {cx + 4},{cy - 8 * step - 10}" '
        f'fill="#0f172a"/>'
    )
    # Axis labels x, y, O
    parts.append(
        f'<text x="{cx + 8 * step + 22}" y="{cy + 4}" font-family="serif" font-style="italic" '
        f'font-size="14" font-weight="bold" fill="#0f172a">x</text>'
    )
    parts.append(
        f'<text x="{cx}" y="{cy - 8 * step - 21}" text-anchor="middle" font-family="serif" font-style="italic" '
        f'font-size="14" font-weight="bold" fill="#0f172a">y</text>'
    )
    parts.append(
        f'<text x="{cx - 7}" y="{cy + 14}" text-anchor="end" font-family="serif" font-style="italic" '
        f'font-size="12" fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3">O</text>'
    )
    # Tick labels at even integers
    for v in (-8, -6, -4, -2, 2, 4, 6, 8):
        lbl = f'−{abs(v)}' if v < 0 else str(v)
        lx = cx + v * step
        ly = cy - v * step
        parts.append(
            f'<text x="{lx}" y="{cy + 15}" text-anchor="middle" font-family="serif" font-size="11.5" '
            f'fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3">{lbl}</text>'
        )
        parts.append(
            f'<text x="{cx - 7}" y="{ly + 4}" text-anchor="end" font-family="serif" font-size="11.5" '
            f'fill="#0f172a" paint-order="stroke" stroke="#ffffff" stroke-width="3">{lbl}</text>'
        )
    # Line y = -(1/5)x - 6 from x = -8 (y = -4.4) to x = 8 (y = -7.6)
    x1, y1 = cx + (-8) * step, cy - (-4.4) * step
    x2, y2 = cx + 8 * step, cy - (-7.6) * step
    parts.append(
        f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" '
        f'stroke="#1e3a8a" stroke-width="2.6" stroke-linecap="round"/>'
    )
    body = '\n  '.join(parts)
    return (
        '<div style="display:flex;justify-content:center;margin:10px 0;">'
        '<svg viewBox="0 0 326 320" width="300" height="295" xmlns="http://www.w3.org/2000/svg" '
        'style="background:#ffffff;border:1px solid #e2e8f0;border-radius:12px;">\n  '
        f'{body}\n</svg></div>'
    )


M2_Q9_COUNTS = {
    720: 2,
    721: 0,
    722: 0,
    723: 3,
    724: 2,
    725: 0,
    726: 1,
    727: 1,
    728: 1,
    729: 0,
    730: 2,
    731: 0,
    732: 1,
}


def _svg_m2_q9_dotplot():
    """Exact dot plot of 13 Jupiter moons' orbital periods (720–732 days) for M2 Q9."""
    x0, step, axis_y = 42, 28, 95
    parts = [
        f'<line x1="22" y1="{axis_y}" x2="{x0 + 12 * step + 20}" y2="{axis_y}" stroke="#0f172a" stroke-width="1.8"/>'
    ]
    for val in range(720, 733):
        x = x0 + (val - 720) * step
        parts.append(f'<line x1="{x}" y1="{axis_y - 6}" x2="{x}" y2="{axis_y + 6}" stroke="#0f172a" stroke-width="1.4"/>')
        if val % 2 == 0:
            parts.append(
                f'<text x="{x}" y="{axis_y + 23}" text-anchor="middle" font-family="serif" '
                f'font-size="13" fill="#0f172a">{val}</text>'
            )
        cnt = M2_Q9_COUNTS[val]
        for k in range(cnt):
            cy = axis_y - 18 - k * 15
            parts.append(f'<circle cx="{x}" cy="{cy}" r="4.5" fill="#1e3a8a"/>')
    parts.append(
        f'<text x="{x0 + 6 * step}" y="{axis_y + 47}" text-anchor="middle" font-family="serif" '
        f'font-size="14" font-weight="600" fill="#0f172a">Orbital period (days)</text>'
    )
    body = '\n  '.join(parts)
    return (
        '<div style="display:flex;justify-content:center;margin:10px 0;">'
        '<svg viewBox="0 0 420 156" width="400" height="148" xmlns="http://www.w3.org/2000/svg" '
        'style="background:#ffffff;border:1px solid #e2e8f0;border-radius:12px;">\n  '
        f'{body}\n</svg></div>'
    )


# ============================================================================
# MODULE 1 — 22 QUESTIONS (16 MCQ + 6 SPR)
# ============================================================================

def _build_m1_questions():
    tbl_m1_q2 = _html_table(
        ['Classification', 'Frequency'],
        [
            ['igneous', '10'],
            ['metamorphic', '38'],
            ['sedimentary', '22'],
        ],
    )

    return [
        # M1 Q1
        _mcq(
            'june25_usv1_m1_q1', 1, 'Algebra', 'Linear functions', 'Easy',
            _svg_m1_q1_line() + r'<p>The graph of the linear function \(f\) is shown, where \(y = f(x)\).</p>',
            r'What is the \(y\)-intercept of the graph of \(f\)?',
            {
                'A': r'\((0, 6)\)',
                'B': r'\((0, 0)\)',
                'C': r'\((0, -4)\)',
                'D': r'\((0, -6)\)',
            },
            'D',
            r'Giao điểm với trục tung (\(y\)-intercept) là điểm mà đồ thị cắt trục \(y\) (tại \(x = 0\)). Nhìn trực tiếp trên đồ thị, đường thẳng cắt trục \(y\) đúng tại vạch \(y = -6\), tức điểm \((0, -6)\). (Đường thẳng đi qua \((-5, -5)\), \((0, -6)\), \((5, -7)\) có phương trình \(f(x) = -\frac{1}{5}x - 6\)).',
            r'\(y\)-intercept luôn có dạng \((0, b)\) — đọc ngay cao độ nơi đường thẳng cắt trục dọc \(Oy\), chú ý kỹ dấu âm/dương.',
            {
                'A': ('Sai dấu y', r'Đọc nhầm dấu dương \((0, 6)\) nằm phía trên trục hoành trong khi đường thẳng cắt trục tung ở phía dưới.'),
                'B': ('Gốc tọa độ', r'Đường thẳng không đi qua gốc tọa độ \((0, 0)\).'),
                'C': ('Đọc nhầm biên trái', r'Tại biên trái \(x = -8\), tung độ mới gần \(-4\) (\(y = -4.4\)), không phải tại \(x = 0\).'),
                'D': ('Đáp án đúng', r'Đồ thị cắt trục tung tại đúng điểm \((0, -6)\).'),
            },
            r'Đọc trực tiếp giao điểm trên trục dọc \(Oy\) không cần máy tính; nếu muốn kiểm chứng bằng bảng điểm, nhập hai điểm `(-5, -5)` và `(5, -7)` vào Desmos sẽ thấy đường nối cắt trục \(y\) tại `(0, -6)`.',
        ),
        # M1 Q2
        _mcq(
            'june25_usv1_m1_q2', 2, 'Problem-Solving and Data Analysis', 'Probability and conditional probability', 'Easy',
            r'<p>Each rock in a collection of \(70\) rocks was classified as either igneous, metamorphic, or sedimentary, as shown in the frequency table.</p>' + tbl_m1_q2,
            r'If one of these rocks is selected at random, what is the probability of selecting a rock that is igneous?',
            {
                'A': r'\(\frac{10}{70}\)',
                'B': r'\(\frac{10}{60}\)',
                'C': r'\(\frac{10}{38}\)',
                'D': r'\(\frac{10}{22}\)',
            },
            'A',
            r'Tổng số viên đá trong bộ sưu tập là \(10 + 38 + 22 = 70\). Số viên đá magma (igneous) là \(10\). Do đó xác suất chọn ngẫu nhiên được một viên đá igneous là \(P = \frac{10}{70}\).',
            r'Xác suất cơ bản \(P = \frac{\text{favorable outcomes}}{\text{total outcomes}}\). Trên SAT nhiều đáp án giữ nguyên phân số chưa rút gọn như \(\frac{10}{70}\).',
            {
                'A': ('Đáp án đúng', r'Có \(10\) viên igneous trên tổng số \(70\) viên đá, nên xác suất là \(\frac{10}{70}\).'),
                'B': ('Nhầm tỷ số odds', r'\(60 = 38 + 22\) là số viên đá không phải igneous; \(\frac{10}{60}\) là tỷ số odds chứ không phải xác suất.'),
                'C': ('Sai mẫu số', r'Lấy mẫu số là số viên đá metamorphic (\(38\)) thay vì tổng \(70\).'),
                'D': ('Sai mẫu số', r'Lấy mẫu số là số viên đá sedimentary (\(22\)) thay vì tổng \(70\).'),
            },
            r'Kiểm tra nhanh tổng mẫu số: gõ `10 + 38 + 22` ra `70`, suy ra xác suất là `10/70`.',
        ),
        # M1 Q3
        _mcq(
            'june25_usv1_m1_q3', 3, 'Geometry and Trigonometry', 'Area and volume', 'Easy',
            r'<p>Each side of square A has a length of \(13\) inches. Each side of square A is multiplied by a scale factor of \(3\) to create square B.</p>',
            r'What is the length, in inches, of each side of square B?',
            {
                'A': r'\(10\)',
                'B': r'\(13\)',
                'C': r'\(16\)',
                'D': r'\(39\)',
            },
            'D',
            r'Mỗi cạnh của hình vuông A dài \(13\text{ inches}\) và được nhân với hệ số tỉ lệ (scale factor) là \(3\) để tạo hình vuông B. Vậy độ dài cạnh hình vuông B là \(13 \times 3 = 39\text{ inches}\).',
            r'Khi phóng to cạnh bằng hệ số tỉ lệ \(k\), độ dài cạnh mới tăng \(k\) lần (lấy cạnh cũ nhân \(k\)), không phải cộng hay trừ \(k\).',
            {
                'A': ('Trừ thay vì nhân', r'Tính nhầm \(13 - 3 = 10\).'),
                'B': ('Chưa nhân hệ số tỉ lệ', r'\(13\) là độ dài cạnh ban đầu của hình vuông A.'),
                'C': ('Cộng thay vì nhân', r'Tính nhầm \(13 + 3 = 16\).'),
                'D': ('Đáp án đúng', r'\(13 \times 3 = 39\text{ inches}\).'),
            },
            r'Gõ nhanh `13 * 3` vào Desmos để chắc chắn không tính nhầm.',
        ),
        # M1 Q4
        _mcq(
            'june25_usv1_m1_q4', 4, 'Advanced Math', 'Nonlinear functions', 'Easy',
            r'<p>The function \(f(x) = \frac{1}{9}(x - 6)^2 + 3\) gives a toy car’s height above the ground \(f(x)\), in inches, \(x\) seconds after it started moving on an elevated track, where \(0 \le x \le 10\).</p>',
            r'Which of the following is the best interpretation of the vertex of the graph of \(y = f(x)\) in the \(xy\)-plane?',
            {
                'A': r'The toy car’s minimum height was \(3\) inches above the ground.',
                'B': r'The toy car’s minimum height was \(6\) inches above the ground.',
                'C': r'The toy car’s height was \(3\) inches above the ground when it started moving.',
                'D': r'The toy car’s height was \(6\) inches above the ground when it started moving.',
            },
            'A',
            r'Hàm số bậc hai ở dạng đỉnh \(f(x) = a(x - h)^2 + k\) với \(a = \frac{1}{9} > 0\) (parabol hướng lên) và đỉnh \((h, k) = (6, 3)\). Vì \(x = 6\) thuộc miền \(0 \le x \le 10\), tại thời điểm \(x = 6\) giây, xe đồ chơi đạt độ cao nhỏ nhất là \(f(6) = 3\text{ inches}\) so với mặt đất.',
            r'Với \(f(x) = a(x - h)^2 + k\) (\(a > 0\)): hoành độ đỉnh \(h\) là thời điểm/đầu vào, còn tung độ đỉnh \(k\) là giá trị nhỏ nhất (minimum). Đừng nhầm với giá trị ban đầu \(f(0)\)!',
            {
                'A': ('Đáp án đúng', r'Đỉnh \((6, 3)\) cho biết độ cao nhỏ nhất của xe đồ chơi là \(3\text{ inches}\) (đạt được sau \(6\) giây).'),
                'B': ('Đảo ngược h và k', r'\(6\) là thời gian \(x\) (giây) để đạt cực tiểu, không phải độ cao.'),
                'C': ('Nhầm đỉnh với y-intercept', r'Khi bắt đầu chuyển động (\(x = 0\)), độ cao là \(f(0) = \frac{1}{9}(-6)^2 + 3 = 7\text{ inches}\), không phải \(3\).'),
                'D': ('Nhầm cả hai khái niệm', r'Vừa nhầm hoành độ đỉnh \(6\) thành độ cao, vừa nhầm đỉnh với thời điểm ban đầu \(x = 0\).'),
            },
            r'Gõ `y = (1/9)(x - 6)^2 + 3 {0 <= x <= 10}` vào Desmos rồi click vào đáy parabol để thấy ngay điểm đỉnh `(6, 3)` — giá trị cực tiểu của \(y\) là `3`.',
        ),
        # M1 Q5
        _mcq(
            'june25_usv1_m1_q5', 5, 'Algebra', 'Linear equations in one variable', 'Easy',
            r'<p>Consider the given equation:</p><p style="text-align:center;font-size:18px;">\[3x = 8\]</p>',
            r'If \(3x = 8\), what is the value of \(21x\)?',
            {
                'A': r'\(1\)',
                'B': r'\(15\)',
                'C': r'\(31\)',
                'D': r'\(56\)',
            },
            'D',
            r'Nhận thấy \(21x = 7 \cdot (3x)\). Thay trực tiếp \(3x = 8\), ta có ngay \(21x = 7 \times 8 = 56\) mà không cần giải tìm phân số \(x = \frac{8}{3}\).',
            r'Thủ thuật bội số SAT: tìm tỉ lệ giữa biểu thức cần tính (\(21x\)) và biểu thức đã cho (\(3x\)) để nhân trực tiếp hai vế cho \(7\).',
            {
                'A': ('Sai phép tính', r'Nhầm \(8 - 7 = 1\).'),
                'B': ('Cộng thay vì nhân', r'Cộng nhầm \(8 + 7 = 15\) thay vì nhân \(8 \times 7\).'),
                'C': ('Sai công thức', r'Cộng nhầm \(21 + 8 + 2\) hoặc ghép sai hằng số.'),
                'D': ('Đáp án đúng', r'\(21x = 7(3x) = 7(8) = 56\).'),
            },
            r'Gõ `x = 8/3` rồi dòng dưới gõ `21x` trong Desmos sẽ trả về ngay `56`.',
        ),
        # M1 Q6
        _mcq(
            'june25_usv1_m1_q6', 6, 'Algebra', 'Linear inequalities in one or two variables', 'Easy',
            r'<p>A car travels at a speed of at least \(25\) miles per hour but no more than \(50\) miles per hour for a certain part of a trip.</p>',
            r'Which inequality represents this situation, where \(x\) is the speed of the car, in miles per hour, on this part of the trip?',
            {
                'A': r'\(x \ge 25\)',
                'B': r'\(x \ge 50\)',
                'C': r'\(25 \le x \le 50\)',
                'D': r'\(x \le 75\)',
            },
            'C',
            r'Cụm từ “at least \(25\)” (ít nhất \(25\)) nghĩa là \(x \ge 25\), và “no more than \(50\)” (không quá \(50\)) nghĩa là \(x \le 50\). Kết hợp cả hai điều kiện ta được bất đẳng thức kép \(25 \le x \le 50\).',
            r'Từ khóa dịch bất đẳng thức SAT: “at least” \(\leftrightarrow \ge\), “no more than / at most” \(\leftrightarrow \le\).',
            {
                'A': ('Thiếu cận trên', r'Chỉ thể hiện điều kiện tốc độ ít nhất \(25\text{ mph}\), thiếu điều kiện không quá \(50\text{ mph}\).'),
                'B': ('Ngược chiều bất đẳng thức', r'\(x \ge 50\) nghĩa là tối thiểu \(50\text{ mph}\), trái ngược với “no more than \(50\)”.'),
                'C': ('Đáp án đúng', r'Biểu diễn trọn vẹn khoảng tốc độ từ \(25\) đến \(50\text{ mph}\) (tính cả hai đầu mút).'),
                'D': ('Cộng hai cận', r'Cộng nhầm \(25 + 50 = 75\) thành cận trên không có ý nghĩa.'),
            },
            r'Câu dịch bất đẳng thức lý thuyết — đối chiếu từng vế “at least 25” (\(25 \le x\)) và “no more than 50” (\(x \le 50\)).',
        ),
        # M1 Q7
        _mcq(
            'june25_usv1_m1_q7', 7, 'Problem-Solving and Data Analysis', 'One-variable data: Distributions and measures of center and spread', 'Easy',
            r'<p>A list of \(10\) data values is shown.</p><p style="text-align:center;font-size:18px;letter-spacing:0.4px;">\(10,\; 14,\; 22,\; 6,\; 24,\; 26,\; 14,\; 8,\; 8,\; 8\)</p>',
            r'What is the mean of these data?',
            {
                'A': r'\(8\)',
                'B': r'\(12\)',
                'C': r'\(14\)',
                'D': r'\(20\)',
            },
            'C',
            r'Giá trị trung bình cộng (mean) bằng tổng tất cả các số chia cho số lượng phần tử (\(10\)): \[\text{mean} = \frac{10 + 14 + 22 + 6 + 24 + 26 + 14 + 8 + 8 + 8}{10} = \frac{140}{10} = 14.\]',
            r'Phân biệt rõ ba đại lượng thống kê SAT: Mean (trung bình cộng \(= 14\)), Median (trung vị \(= 12\)), và Mode (giá trị xuất hiện nhiều nhất \(= 8\)).',
            {
                'A': ('Bẫy Mode', r'\(8\) là mode (xuất hiện \(3\) lần) chứ không phải mean.'),
                'B': ('Bẫy Median', r'Khi sắp xếp tăng dần \(6, 8, 8, 8, 10, 14, 14, 22, 24, 26\), trung vị là \(\frac{10 + 14}{2} = 12\), không phải mean.'),
                'C': ('Đáp án đúng', r'Tổng \(10\) số bằng \(140\), suy ra \(\text{mean} = \frac{140}{10} = 14\).'),
                'D': ('Bẫy Range', r'\(26 - 6 = 20\) là khoảng biến thiên (range) chứ không phải mean.'),
            },
            r'Gõ thẳng `mean(10, 14, 22, 6, 24, 26, 14, 8, 8, 8)` vào Desmos sẽ trả về ngay `14` — tránh tuyệt đối lỗi cộng tay hoặc nhầm sang median/mode!',
        ),
        # M1 Q8
        _mcq(
            'june25_usv1_m1_q8', 8, 'Algebra', 'Linear functions', 'Easy',
            r'<p style="text-align:center;font-size:18px;">\[f(x) = 7x + 3\]</p><p>The function \(f\) gives the estimated height, in feet, of a willow tree \(x\) years after its height was first measured.</p>',
            r'Which statement is the best interpretation of \(3\) in this context?',
            {
                'A': r'The tree will be measured each year for \(3\) years.',
                'B': r'The tree is estimated to grow to a maximum height of \(3\) feet.',
                'C': r'The estimated height of the tree increased by \(3\) feet each year.',
                'D': r'The estimated height of the tree was \(3\) feet when it was first measured.',
            },
            'D',
            r'Trong hàm tuyến tính \(f(x) = 7x + 3\), hệ số góc \(7\) là tốc độ tăng chiều cao mỗi năm (\(7\text{ ft/yr}\)), còn hằng số tự do \(3\) là tung độ gốc \(f(0) = 3\), biểu thị chiều cao ước tính ban đầu của cây liễu khi được đo lần đầu tiên (\(x = 0\)).',
            r'Trong mô hình tuyến tính \(f(x) = mx + b\): \(m\) luôn là tốc độ thay đổi (rate of change per unit), còn \(b = f(0)\) luôn là giá trị ban đầu (initial value).',
            {
                'A': ('Sai vai trò biến số', r'\(3\) có đơn vị là feet (chiều cao), không phải số năm đo đạc.'),
                'B': ('Nhầm với cực đại', r'Hàm tuyến tính có hệ số góc dương tăng liên tục, \(3\text{ feet}\) là chiều cao ban đầu chứ không phải chiều cao tối đa.'),
                'C': ('Nhầm với hệ số góc', r'Tốc độ tăng chiều cao mỗi năm là \(7\text{ feet}\), không phải \(3\text{ feet}\).'),
                'D': ('Đáp án đúng', r'Khi \(x = 0\) (lần đo đầu tiên), \(f(0) = 7(0) + 3 = 3\text{ feet}\).'),
            },
            r'Thay `x = 0` vào \(f(x) = 7x + 3\) được `f(0) = 3` — khẳng định ngay \(3\) là chiều cao ban đầu.',
        ),
        # M1 Q9
        _mcq(
            'june25_usv1_m1_q9', 9, 'Advanced Math', 'Equivalent expressions', 'Medium',
            r'<p>Consider the polynomial expression:</p><p style="text-align:center;font-size:18px;">\[2x^3 + 8x^2y + xy^2 + 4y^3\]</p>',
            r'Which expression is equivalent to \(2x^3 + 8x^2y + xy^2 + 4y^3\)?',
            {
                'A': r'\((2x^2 + 4y)(x + y^2)\)',
                'B': r'\((2x^2 + y^2)(x + 4y)\)',
                'C': r'\((2x^3 + y^2)(x^2 + 4y^3)\)',
                'D': r'\((2x^3 + y^3)(x + 4y)\)',
            },
            'B',
            r'Phân tích đa thức thành nhân tử bằng phương pháp nhóm hạng tử (factoring by grouping): \[2x^3 + 8x^2y + xy^2 + 4y^3 = 2x^2(x + 4y) + y^2(x + 4y) = (2x^2 + y^2)(x + 4y).\]',
            r'Với đa thức 4 hạng tử dạng \(ax^3 + bx^2y + cxy^2 + dy^3\), hãy nhóm 2 hạng tử đầu và 2 hạng tử sau để rút nhân tử chung \((x + 4y)\).',
            {
                'A': ('Khai triển sai hạng tử giữa', r'\((2x^2 + 4y)(x + y^2) = 2x^3 + 2x^2y^2 + 4xy + 4y^3\), sai hoàn toàn bậc của hai số hạng giữa.'),
                'B': ('Đáp án đúng', r'\((2x^2 + y^2)(x + 4y) = 2x^3 + 8x^2y + xy^2 + 4y^3\).'),
                'C': ('Sai bậc đa thức', r'Tích bậc cao nhất là \(2x^5\) và \(4y^5\), không phải bậc \(3\).'),
                'D': ('Sai bậc đa thức', r'Tích bậc cao nhất là \(2x^4\) và \(4y^4\), không phải bậc \(3\).'),
            },
            r'Thử số nhanh trên Desmos: đặt `x = 2`, `y = 3`, tính biểu thức gốc `2x^3 + 8x^2y + xy^2 + 4y^3 = 238`, rồi thử từng đáp án — chỉ đáp án B cho đúng `238`!',
        ),
        # M1 Q10 (SPR)
        _spr(
            'june25_usv1_m1_q10', 10, 'Advanced Math', 'Nonlinear functions', 'Easy',
            r'<p style="text-align:center;font-size:18px;">\[f(x) = x^3 + 8x + 17\]</p><p>For the given function \(f\), the graph of \(y = f(x)\) in the \(xy\)-plane passes through the point \((0, b)\), where \(b\) is a constant.</p>',
            r'What is the value of \(b\)?',
            ['17'],
            '17',
            r'Vì đồ thị \(y = f(x)\) đi qua điểm \((0, b)\), ta có \(b = f(0)\). Thay \(x = 0\) vào công thức hàm số: \[b = 0^3 + 8(0) + 17 = 17.\]',
            r'Điểm \((0, b)\) chính là \(y\)-intercept của đồ thị hàm đa thức — luôn bằng hệ số tự do (constant term) \(17\).',
            r'Gõ `f(x) = x^3 + 8x + 17` rồi gõ `f(0)` vào Desmos sẽ hiện ngay `17`.',
        ),
        # M1 Q11
        _mcq(
            'june25_usv1_m1_q11', 11, 'Problem-Solving and Data Analysis', 'Two-variable data: Models and scatterplots', 'Easy',
            r'<p>Scientists collected fallen acorns that each housed a colony of the ant species <em>P. ohioensis</em> and analyzed each colony’s structure. For any of these colonies, if the colony has \(x\) worker ants, the equation \(y = 0.67x + 2.6\), where \(20 \le x \le 110\), gives the predicted number of larvae, \(y\), in the colony.</p>',
            r'If one of these colonies has \(35\) worker ants, which of the following is closest to the predicted number of larvae in the colony?',
            {
                'A': r'\(114\)',
                'B': r'\(48\)',
                'C': r'\(38\)',
                'D': r'\(26\)',
            },
            'D',
            r'Thay \(x = 35\) (thỏa mãn \(20 \le 35 \le 110\)) vào phương trình hồi quy \(y = 0.67x + 2.6\): \[y = 0.67(35) + 2.6 = 23.45 + 2.6 = 26.05 \approx 26.\]',
            r'Xác định đúng biến đầu vào (\(x = 35\) kiến thợ) và biến đầu ra (\(y =\) số ấu trùng dự đoán), sau đó thế trực tiếp vào phương trình.',
            {
                'A': ('Dùng nhầm cận trên', r'Thế nhầm số khác hoặc tính sai hoàn toàn (ví dụ \(0.67(110) + 2.6 \approx 76.3\) hoặc nhầm hệ số).'),
                'B': ('Giải ngược x theo y', r'Nếu giải ngược \(35 = 0.67x + 2.6\) sẽ ra \(x \approx 48.36\) — đây là bẫy thế nhầm \(35\) vào \(y\) thay vì \(x\)!'),
                'C': ('Cộng nhầm hằng số', r'Cộng nhầm \(35 + 2.6 \approx 38\), bỏ quên hệ số góc \(0.67\).'),
                'D': ('Đáp án đúng', r'\(0.67(35) + 2.6 = 26.05\), gần nhất với \(26\).'),
            },
            r'Gõ trực tiếp `0.67 * 35 + 2.6` vào Desmos ra `26.05`, làm tròn ngay sang `26`.',
        ),
        # M1 Q12
        _mcq(
            'june25_usv1_m1_q12', 12, 'Advanced Math', 'Equivalent expressions', 'Easy',
            r'<p style="text-align:center;font-size:18px;">\[b - 49 = \frac{x}{y}\]</p><p>The given equation relates the positive numbers \(b\), \(x\), and \(y\).</p>',
            r'Which equation correctly expresses \(x\) in terms of \(b\) and \(y\)?',
            {
                'A': r'\(x = \frac{by - 49}{y}\)',
                'B': r'\(x = by - 49y\)',
                'C': r'\(x = by - 49\)',
                'D': r'\(x = \frac{b - 49}{y}\)',
            },
            'B',
            r'Nhân cả hai vế của phương trình \(b - 49 = \frac{x}{y}\) với \(y\) (vì \(y > 0\)): \[y(b - 49) = x \implies x = by - 49y.\]',
            r'Khi nhân hai vế với \(y\), BẮT BUỘC phân phối \(y\) cho TẤT CẢ các số hạng trong vế trái (\(by - 49y\)), tránh quên nhân \(-49\) với \(y\) (bẫy C).',
            {
                'A': ('Biến đổi sai mẫu số', r'Vừa nhân vừa chia cho \(y\) sai quy tắc đại số.'),
                'B': ('Đáp án đúng', r'Nhân hai vế với \(y\) và phân phối chuẩn: \(x = y(b - 49) = by - 49y\).'),
                'C': ('Quên phân phối y', r'Chỉ nhân \(b\) với \(y\) mà quên nhân \(-49\) với \(y\).'),
                'D': ('Chia thay vì nhân', r'Chia hai vế cho \(y\) thay vì nhân hai vế với \(y\).'),
            },
            r'Thử số trên Desmos: chọn `b = 51`, `y = 3` thì `x = (51 - 49) * 3 = 6`. Kiểm tra 4 đáp án: chỉ `by - 49y = 51(3) - 49(3) = 6` khớp!',
        ),
        # M1 Q13
        _mcq(
            'june25_usv1_m1_q13', 13, 'Algebra', 'Systems of two linear equations in two variables', 'Medium',
            r'<p style="text-align:center;font-size:18px;">\[\begin{aligned} 2y &= 5x + 16 \\ -2y &= 7x - 22 \end{aligned}\]</p><p>The solution to the given system of equations is \((x, y)\).</p>',
            r'What is the value of \(24x\)?',
            {
                'A': r'\(-12\)',
                'B': r'\(-6\)',
                'C': r'\(6\)',
                'D': r'\(12\)',
            },
            'D',
            r'Cộng vế theo vế hai phương trình để khử ngay \(y\): \[(2y) + (-2y) = (5x + 16) + (7x - 22) \implies 0 = 12x - 6 \implies 12x = 6.\] Nhân hai vế với \(2\), ta có ngay \(24x = 12\) (với \(x = \frac{1}{2}\)).',
            r'Luôn quan sát hệ số đối nhau (\(2y\) và \(-2y\)) để cộng trực tiếp, và gạch chân biểu thức cần tìm (\(24x\)) để không dừng sớm ở \(12x = 6\).',
            {
                'A': ('Sai dấu', r'Chuyển vế sai dấu thành \(12x = -6 \Rightarrow 24x = -12\).'),
                'B': ('Sai dấu và chưa nhân 2', r'Nhầm dấu của \(12x\) và quên nhân đôi để ra \(24x\).'),
                'C': ('Dừng ở 12x', r'\(6\) là giá trị của \(12x\), chưa nhân \(2\) để ra \(24x\).'),
                'D': ('Đáp án đúng', r'\(12x = 6 \implies 24x = 12\).'),
            },
            r'Gõ hai phương trình `2y = 5x + 16` và `-2y = 7x - 22` vào Desmos, bấm vào giao điểm `(0.5, 9.25)` rồi tính `24 * 0.5 = 12`.',
        ),
        # M1 Q14 (SPR)
        _spr(
            'june25_usv1_m1_q14', 14, 'Algebra', 'Linear equations in two variables', 'Medium',
            r'<p style="text-align:center;font-size:18px;">\[19.5x + 24.25y = 583\]</p><p>Odalys ordered mulch and river rock, which cost a total of $583, for her home. The given equation represents the relationship between the number of cubic yards of mulch, \(x\), and the number of tons of river rock, \(y\), Odalys ordered.</p>',
            r'How much more, in dollars, did a ton of river rock cost Odalys than a cubic yard of mulch?',
            ['4.75', '19/4'],
            '4.75 (hoặc 19/4)',
            r'Trong phương trình tổng chi phí \(19.5x + 24.25y = 583\): hệ số của \(x\) là đơn giá mỗi cubic yard lớp phủ mulch (\(\$19.50\)), còn hệ số của \(y\) là đơn giá mỗi tấn đá cuội river rock (\(\$24.25\)). Mức chênh lệch giá là: \[24.25 - 19.5 = 4.75\text{ dollars}.\]',
            r'Với phương trình tổng chi phí dạng \(p_1 x + p_2 y = T\), các hệ số \(p_1, p_2\) chính là đơn giá từng loại hàng hóa; chỉ cần lấy hiệu \(p_2 - p_1\).',
            r'Gõ thẳng `24.25 - 19.5` vào Desmos ra `4.75` (hoặc nhấn biểu tượng phân số ra `19/4`).',
        ),
        # M1 Q15
        _mcq(
            'june25_usv1_m1_q15', 15, 'Advanced Math', 'Nonlinear functions', 'Medium',
            r'<p>James purchased a certain baseball card on January 1. The function \(f(x) = 55(1.04)^x\), where \(0 \le x \le 10\), gives the predicted value, in dollars, of the baseball card \(x\) years after James purchased it.</p>',
            r'What is the best interpretation of the statement “\(f(7)\) is approximately equal to \(72\)” in this context?',
            {
                'A': r'When the baseball card’s predicted value is approximately \(72\) dollars, it is \(7\%\) greater than the predicted value, in dollars, on January 1 of the previous year.',
                'B': r'When the baseball card’s predicted value is approximately \(72\) dollars, it is \(7\) times the predicted value, in dollars, on January 1 of the previous year.',
                'C': r'From the day James purchased the baseball card to \(7\) years after James purchased the card, its predicted value increased by a total of approximately \(72\) dollars.',
                'D': r'\(7\) years after James purchased the baseball card, its predicted value is approximately \(72\) dollars.',
            },
            'D',
            r'Trong hàm số \(f(x)\), biến đầu vào \(x\) là số năm kể từ ngày James mua thẻ bóng chày, và đầu ra \(f(x)\) là giá trị dự đoán (tính bằng đô la) của chiếc thẻ tại thời điểm đó. Vì vậy “\(f(7) \approx 72\)” có nghĩa là: \(7\) năm sau khi mua, giá trị dự đoán của chiếc thẻ là khoảng \(72\) đô la (kiểm tra: \(55(1.04)^7 \approx 72.38\)).',
            r'Khi diễn giải \(f(a) = b\): luôn dịch trực tiếp “tại đầu vào \(x = a\), đầu ra là \(b\)” — không bao giờ là “tăng thêm \(b\)” hay “tăng \(a\%\)”.',
            {
                'A': ('Nhầm x thành phần trăm tăng', r'Tỉ lệ tăng mỗi năm là \(4\%\) (từ cơ số \(1.04\)), không phải \(7\%\).'),
                'B': ('Nhầm x thành số lần gấp', r'\(7\) là số năm, không phải bội số tăng trưởng so với năm trước.'),
                'C': ('Nhầm giá trị với độ tăng', r'\(72\) đô la là tổng giá trị dự đoán tại năm thứ \(7\), không phải phần tăng thêm (phần tăng thêm chỉ là \(72 - 55 = 17\) đô la).'),
                'D': ('Đáp án đúng', r'Diễn giải chính xác ý nghĩa của đầu vào \(x = 7\) năm và đầu ra \(f(7) \approx 72\) đô la.'),
            },
            r'Kiểm tra nhanh trong Desmos: `55 * 1.04^7 ≈ 72.38` — đúng là giá trị chiếc thẻ sau `7` năm.',
        ),
        # M1 Q16
        _mcq(
            'june25_usv1_m1_q16', 16, 'Advanced Math', 'Nonlinear functions', 'Medium',
            r'<p>Consider the quadratic equation in the \(xy\)-plane:</p><p style="text-align:center;font-size:18px;">\[y = x^2 + 18x - 23\]</p>',
            r'At what value of \(x\) does the graph of \(y = x^2 + 18x - 23\) reach its minimum in the \(xy\)-plane?',
            {
                'A': r'\(-23\)',
                'B': r'\(-9\)',
                'C': r'\(9\)',
                'D': r'\(18\)',
            },
            'B',
            r'Parabol \(y = ax^2 + bx + c\) với \(a = 1 > 0\), \(b = 18\) hướng bề lõm lên trên nên đạt cực tiểu tại hoành độ đỉnh: \[x = -\frac{b}{2a} = -\frac{18}{2(1)} = -9.\]',
            r'Hoành độ đỉnh parabol \(x = -\frac{b}{2a}\) — luôn chú ý dấu trừ ở đầu công thức!',
            {
                'A': ('Nhầm với y-intercept', r'\(-23\) là hệ số tự do \(c\) (tung độ gốc tại \(x = 0\)), không phải hoành độ cực tiểu.'),
                'B': ('Đáp án đúng', r'\(x = -\frac{18}{2} = -9\).'),
                'C': ('Quên dấu trừ', r'Tính nhầm \(\frac{b}{2a} = 9\) mà quên dấu âm trong công thức \(-\frac{b}{2a}\).'),
                'D': ('Quên chia 2 và sai dấu', r'\(18\) chỉ là hệ số \(b\), chưa chia \(2a\) và đổi dấu.'),
            },
            r'Gõ `y = x^2 + 18x - 23` vào Desmos rồi click vào điểm thấp nhất của parabol sẽ thấy ngay tọa độ đỉnh `(-9, -104)` \(\Rightarrow x = -9\).',
        ),
        # M1 Q17
        _mcq(
            'june25_usv1_m1_q17', 17, 'Advanced Math', 'Nonlinear functions', 'Medium',
            r'<p style="text-align:center;font-size:18px;">\[P(t) = 260(1.03)^{\left(\frac{3}{2}\right)t}\]</p><p>The function \(P\) models the population, in thousands, of a certain city \(t\) years after \(2009\). According to the model, the population is predicted to increase by \(n\%\) every \(8\) months.</p>',
            r'What is the value of \(n\)?',
            {
                'A': r'\(0.22\)',
                'B': r'\(1.03\)',
                'C': r'\(2\)',
                'D': r'\(3\)',
            },
            'D',
            r'Đổi \(8\) tháng sang năm: \(8\text{ months} = \frac{8}{12} = \frac{2}{3}\text{ year}\). Khi \(t\) tăng thêm \(\frac{2}{3}\) năm, số mũ \(\left(\frac{3}{2}\right)t\) tăng thêm đúng \(\frac{3}{2} \cdot \frac{2}{3} = 1\) đơn vị! Do đó cứ mỗi \(8\) tháng, dân số nhân với hệ số \(1.03 = 1 + \frac{3}{100}\), tức tăng thêm \(3\% \implies n = 3\).',
            r'Với hàm mũ \(A(1 + r)^{t / T}\): mỗi chu kỳ dài \(T\) (ở đây \(T = \frac{2}{3}\) năm \(= 8\) tháng), số mũ tăng đúng \(1\) và đại lượng tăng thêm đúng \(100r\%\).',
            {
                'A': ('Nhầm tính toán', r'Tính nhầm do đổi sai đơn vị hoặc cộng sai mũ.'),
                'B': ('Nhầm cơ số với phần trăm', r'\(1.03\) là hệ số nhân (growth factor \(= 1 + 0.03\)), còn phần trăm tăng là \(3\%\) chứ không phải \(1.03\%\).'),
                'C': ('Nhầm mẫu số mũ', r'Lấy nhầm số \(2\) từ phân số \(\frac{3}{2}\) hoặc tính sai tỉ lệ năm.'),
                'D': ('Đáp án đúng', r'Mỗi \(8\) tháng (\(\frac{2}{3}\) năm), biểu thức nhân với \(1.03\), tức tăng \(3\% \Rightarrow n = 3\).'),
            },
            r'Gõ `P(t) = 260 * 1.03^((3/2)t)` vào Desmos rồi tính `(P(8/12) - P(0)) / P(0) * 100` sẽ ra chính xác `3`.',
        ),
        # M1 Q18 (SPR)
        _spr(
            'june25_usv1_m1_q18', 18, 'Problem-Solving and Data Analysis', 'Ratios, rates, proportional relationships, and units', 'Easy',
            r'<p>Use the conversion \(1\text{ meter} = 100\text{ centimeters}\).</p>',
            r'How many <u>centimeters</u> are equivalent to \(47\) meters? (\(1\) meter = \(100\) centimeters)',
            ['4700'],
            '4700',
            r'Vì \(1\text{ m} = 100\text{ cm}\), ta nhân \(47\) mét với \(100\): \[47 \times 100 = 4{,}700\text{ centimeters}.\]',
            r'Đổi từ đơn vị lớn (meter) sang đơn vị nhỏ (centimeter) thì nhân với hệ số quy đổi \(100\). Không nhập dấu phẩy khi điền vào ô Grid-In (`4700`).',
            r'Gõ `47 * 100` ra `4700`.',
        ),
        # M1 Q19 (SPR)
        _spr(
            'june25_usv1_m1_q19', 19, 'Geometry and Trigonometry', 'Area and volume', 'Medium',
            r'<p>Circle \(A\) has a radius of \(3x\) and circle \(B\) has a radius of \(135x\).</p>',
            r'The area of circle \(B\) is how many times the area of circle \(A\)?',
            ['2025'],
            '2025',
            r'Tỉ số bán kính giữa hình tròn \(B\) và hình tròn \(A\) là: \[k = \frac{135x}{3x} = 45.\] Vì diện tích hình tròn tỉ lệ thuận với bình phương bán kính (\(S = \pi r^2\)), diện tích hình tròn \(B\) gấp diện tích hình tròn \(A\) số lần là: \[k^2 = 45^2 = 2{,}025.\]',
            r'Bán kính gấp \(k\) lần \(\implies\) Chu vi gấp \(k\) lần, Diện tích gấp \(k^2\) lần, Thể tích gấp \(k^3\) lần! Đừng quên bình phương \(45\) lên \(2025\).',
            r'Gõ `(135 / 3)^2` vào Desmos sẽ trả về ngay `2025`.',
        ),
        # M1 Q20 (SPR)
        _spr(
            'june25_usv1_m1_q20', 20, 'Algebra', 'Linear equations in two variables', 'Medium',
            r'<p>The graph of a line in the \(xy\)-plane passes through the point \((1, 5)\) and crosses the \(x\)-axis at the point \((9, 0)\). The line crosses the \(y\)-axis at the point \((0, b)\).</p>',
            r'What is the value of \(b\)?',
            ['45/8', '5.625'],
            '45/8 (hoặc 5.625)',
            r'Hệ số góc của đường thẳng đi qua \((1, 5)\) và \((9, 0)\) là: \[m = \frac{0 - 5}{9 - 1} = -\frac{5}{8}.\] Phương trình đường thẳng: \(y - 0 = -\frac{5}{8}(x - 9) \implies y = -\frac{5}{8}x + \frac{45}{8}\). Khi \(x = 0\), ta được \(b = \frac{45}{8} = 5.625\).',
            r'Dùng công thức hệ số góc \(m = \frac{y_2 - y_1}{x_2 - x_1}\) rồi thế 1 điểm để tìm \(b = y - mx\). Kiểm tra lại cả hai điểm đều thỏa phương trình!',
            r'Tạo bảng (Table) trong Desmos với 2 điểm `(1, 5)` và `(9, 0)`, rồi gõ hồi quy `y1 ~ m*x1 + b` sẽ hiện ngay `b = 5.625` (tức `45/8`).',
        ),
        # M1 Q21 (SPR)
        _spr(
            'june25_usv1_m1_q21', 21, 'Algebra', 'Linear equations in one variable', 'Hard',
            r'<p>Consider the two equations relating \(a\), \(b\), and \(n\):</p><p style="text-align:center;font-size:18px;">\[\frac{2a}{b} = 6.5 \qquad \text{and} \qquad \frac{a}{bn} = 26\]</p>',
            r'If \(\frac{2a}{b} = 6.5\) and \(\frac{a}{bn} = 26\), what is the value of \(n\)?',
            ['1/8', '0.125', '.125'],
            '1/8 (hoặc 0.125)',
            r'Từ phương trình thứ nhất \(\frac{2a}{b} = 6.5\), chia hai vế cho \(2\) ta được: \[\frac{a}{b} = 3.25 = \frac{13}{4}.\] Thay vào phương trình thứ hai \(\frac{a}{b} \cdot \frac{1}{n} = 26\): \[\frac{3.25}{n} = 26 \implies n = \frac{3.25}{26} = \frac{13}{104} = \frac{1}{8} = 0.125.\]',
            r'Xem cả cụm \(\frac{a}{b}\) như một ẩn duy nhất để thế thẳng vào phương trình thứ hai — tránh đặt giá trị bừa bãi mất thời gian.',
            r'Mẹo thử số Desmos: đặt `b = 1` thì `2a = 6.5 => a = 3.25`; gõ `3.25 / (1 * n) = 26` hoặc `3.25 / 26` ra ngay `0.125` (`1/8`).',
        ),
        # M1 Q22
        _mcq(
            'june25_usv1_m1_q22', 22, 'Geometry and Trigonometry', 'Right triangles and trigonometry', 'Medium',
            r'<p>For two acute angles, \(\angle Q\) and \(\angle R\), \(\cos(Q) = \sin(R)\). The measures, in degrees, of \(\angle Q\) and \(\angle R\) are \(x + 61\) and \(4x + 4\), respectively.</p>',
            r'What is the value of \(x\)?',
            {
                'A': r'\(5\)',
                'B': r'\(19\)',
                'C': r'\(23\)',
                'D': r'\(29\)',
            },
            'A',
            r'Với hai góc nhọn \(\angle Q\) và \(\angle R\), đẳng thức \(\cos(Q) = \sin(R)\) xảy ra khi và chỉ khi hai góc phụ nhau (tổng bằng \(90^\circ\)): \[(x + 61) + (4x + 4) = 90 \implies 5x + 65 = 90 \implies 5x = 25 \implies x = 5.\] Kiểm tra: \(\angle Q = 66^\circ\), \(\angle R = 24^\circ\) đều là góc nhọn và \(66^\circ + 24^\circ = 90^\circ\).',
            r'Đẳng thức vàng lượng giác SAT: \(\sin(A) = \cos(B) \iff A + B = 90^\circ\) (với hai góc nhọn).',
            {
                'A': ('Đáp án đúng', r'\((x + 61) + (4x + 4) = 90 \implies 5x = 25 \implies x = 5\).'),
                'B': ('Nhầm hiệu hai góc', r'Giải nhầm phương trình \((4x + 4) - (x + 61) = 0 \implies 3x = 57 \implies x = 19\) (cho hai góc bằng nhau thay vì phụ nhau).'),
                'C': ('Nhầm tổng bằng 180°', r'Giải nhầm \((x + 61) + (4x + 4) = 180 \implies 5x = 115 \implies x = 23\) (nhầm góc phụ \(90^\circ\) thành góc bù \(180^\circ\)).'),
                'D': ('Sai phép tính dấu', r'Cộng nhầm hằng số hoặc tính sai phương trình góc.'),
            },
            r'Chuyển Desmos sang chế độ **Degrees**, gõ `cos(x + 61) = sin(4x + 4)` và tìm nghiệm sao cho cả \(x + 61\) và \(4x + 4\) nằm trong \((0, 90)\) sẽ thấy ngay đường đứng tại `x = 5`.',
        ),
    ]


# ============================================================================
# MODULE 2 — 22 QUESTIONS (16 MCQ + 6 SPR)
# ============================================================================

def _build_m2_questions(id_prefix='june25_usv1_m2'):
    return [
        # M2 Q1
        _mcq(
            f'{id_prefix}_q1', 1, 'Advanced Math', 'Equivalent expressions', 'Easy',
            r'<p>Consider the algebraic expression:</p><p style="text-align:center;font-size:18px;">\[14(x^2 - 6)\]</p>',
            r'Which expression is equivalent to \(14(x^2 - 6)\)?',
            {
                'A': r'\(14x^2 - 84\)',
                'B': r'\(14x^2 - 20\)',
                'C': r'\(14x^2 - 6\)',
                'D': r'\(14x^2 + 8\)',
            },
            'A',
            r'Áp dụng tính chất phân phối của phép nhân đối với phép trừ: \[14(x^2 - 6) = 14 \cdot x^2 - 14 \cdot 6 = 14x^2 - 84.\]',
            r'Luôn nhân thừa số bên ngoài với CẢ HAI số hạng bên trong ngoặc và giữ nguyên dấu trừ.',
            {
                'A': ('Đáp án đúng', r'\(14 \cdot x^2 - 14 \cdot 6 = 14x^2 - 84\).'),
                'B': ('Cộng thay vì nhân', r'Cộng nhầm \(14 + 6 = 20\) rồi gắn dấu trừ thành \(-20\).'),
                'C': ('Quên nhân hằng số', r'Chỉ nhân \(14\) với \(x^2\) mà quên nhân \(14\) với \(-6\).'),
                'D': ('Trừ thay vì nhân', r'Tính nhầm \(14 - 6 = +8\).'),
            },
            r'Gõ nhanh `14 * 6` vào Desmos ra `84`, suy ra \(14x^2 - 84\).',
        ),
        # M2 Q2
        _mcq(
            f'{id_prefix}_q2', 2, 'Problem-Solving and Data Analysis', 'Percentages', 'Easy',
            r'<p>A scientist analyzed a soil sample with a mass of \(900\) grams and determined that it contained \(189\) grams of water.</p>',
            r'What is the percentage of water, by mass, in this soil sample?',
            {
                'A': r'\(9\%\)',
                'B': r'\(9.9\%\)',
                'C': r'\(18.9\%\)',
                'D': r'\(21\%\)',
            },
            'D',
            r'Phần trăm khối lượng nước trong mẫu đất là: \[\frac{189}{900} \times 100\% = \frac{189}{9}\% = 21\%.\]',
            r'Phần trăm thành phần \(= \frac{\text{part}}{\text{whole}} \times 100\%\). Chú ý không chia nhầm cho \(1000\) để dính bẫy \(18.9\%\).',
            {
                'A': ('Lấy nhầm tổng', r'\(9\%\) xuất phát từ chữ số \(9\) trong \(900\), không phải tỉ lệ nước.'),
                'B': ('Sai phép tính', r'Tính nhầm tỉ số phần trăm.'),
                'C': ('Chia nhầm cho 1000', r'Lấy \(\frac{189}{1000} = 18.9\%\) thay vì chia cho tổng khối lượng mẫu đất là \(900\text{ g}\).'),
                'D': ('Đáp án đúng', r'\(\frac{189}{900} = 0.21 = 21\%\).'),
            },
            r'Gõ `(189 / 900) * 100` vào Desmos ra chính xác `21`.',
        ),
        # M2 Q3
        _mcq(
            f'{id_prefix}_q3', 3, 'Advanced Math', 'Nonlinear equations in one variable and systems of equations in two variables', 'Easy',
            r'<p style="text-align:center;font-size:18px;">\[\begin{aligned} x + 5 &= 11 \\ y &= 3x^2 + 3 \end{aligned}\]</p>',
            r'At what point \((x, y)\) do the graphs of the equations in the given system intersect?',
            {
                'A': r'\((6, 108)\)',
                'B': r'\((6, 111)\)',
                'C': r'\((11, 3)\)',
                'D': r'\((11, 366)\)',
            },
            'B',
            r'Từ phương trình thứ nhất: \(x + 5 = 11 \implies x = 6\). Thay \(x = 6\) vào phương trình thứ hai: \[y = 3(6)^2 + 3 = 3(36) + 3 = 108 + 3 = 111.\] Vậy hai đồ thị cắt nhau tại điểm \((6, 111)\).',
            r'Giao điểm hai đồ thị chính là nghiệm \((x, y)\) của hệ phương trình — giải tìm \(x\) trước rồi thay chính xác từng bước vào \(y\), đừng quên cộng \(+3\).',
            {
                'A': ('Quên cộng 3', r'Chỉ tính \(3(6)^2 = 108\) mà quên cộng thêm \(3\).'),
                'B': ('Đáp án đúng', r'\(x = 6\) và \(y = 3(36) + 3 = 111\).'),
                'C': ('Đọc nhầm số đề cho', r'Lấy nhầm vế phải \(11\) làm \(x\) và hằng số \(3\) làm \(y\).'),
                'D': ('Quên trừ 5 khi tìm x', r'Thế nhầm \(x = 11\) vào \(3(11)^2 + 3 = 366\).'),
            },
            r'Gõ `x + 5 = 11` và `y = 3x^2 + 3` vào Desmos (zoom ra ngoài), click vào giao điểm sẽ thấy ngay `(6, 111)`.',
        ),
        # M2 Q4 (SPR)
        _spr(
            f'{id_prefix}_q4', 4, 'Algebra', 'Linear equations in one variable', 'Easy',
            r'<p>Consider the linear equation:</p><p style="text-align:center;font-size:18px;">\[\frac{6}{7}p + 42 = 84\]</p>',
            r'If \(\frac{6}{7}p + 42 = 84\), what is the value of \(7p\)?',
            ['343'],
            '343',
            r'Trừ \(42\) ở cả hai vế: \[\frac{6}{7}p = 84 - 42 = 42.\] Nhân hai vế với \(\frac{7}{6}\): \[p = 42 \cdot \frac{7}{6} = 49.\] Đề bài hỏi giá trị của \(7p\): \[7p = 7 \times 49 = 343.\]',
            r'Đọc kỹ câu hỏi cuối cùng: đề hỏi \(7p\) (không phải \(p = 49\))! Nhiều học sinh giỏi vẫn mất điểm oan ở câu dễ vì điền \(49\).',
            r'Gõ `(6/7)p + 42 = 84` (thay `p` bằng `x`) trong Desmos ra `x = 49`, sau đó gõ `7 * 49` được `343`.',
        ),
        # M2 Q5
        _mcq(
            f'{id_prefix}_q5', 5, 'Algebra', 'Linear equations in one variable', 'Easy',
            r'<p>Consider the linear equation:</p><p style="text-align:center;font-size:18px;">\[5(x + 4) = 4(x + 4) + 58\]</p>',
            r'If \(5(x + 4) = 4(x + 4) + 58\), what is the value of \(x + 4\)?',
            {
                'A': r'\(-4\)',
                'B': r'\(54\)',
                'C': r'\(58\)',
                'D': r'\(62\)',
            },
            'C',
            r'Đặt \(u = x + 4\). Phương trình trở thành \(5u = 4u + 58\). Trừ \(4u\) ở cả hai vế, ta thu được ngay \(u = 58\), tức \(x + 4 = 58\).',
            r'Khi cả hai vế cùng chứa biểu thức \((x + 4)\) và đề cũng hỏi đúng \((x + 4)\), hãy xem cả cụm đó như 1 ẩn \(u\) để ra đáp án trong 2 giây và tránh bẫy giải ra \(x = 54\).',
            {
                'A': ('Nghiệm của x + 4 = 0', r'Lấy nhầm giá trị làm cho \(x + 4 = 0\).'),
                'B': ('Bẫy giải tìm x', r'\(54\) là giá trị của \(x\) (\(58 - 4 = 54\)), nhưng đề bài hỏi \(x + 4\).'),
                'C': ('Đáp án đúng', r'\(5(x + 4) - 4(x + 4) = 58 \implies x + 4 = 58\).'),
                'D': ('Cộng thêm 4 hai lần', r'Lấy nhầm \(58 + 4 = 62\).'),
            },
            r'Gõ `5(x + 4) = 4(x + 4) + 58` vào Desmos ra `x = 54`, sau đó gõ `54 + 4` ra `58`.',
        ),
        # M2 Q6
        _mcq(
            f'{id_prefix}_q6', 6, 'Geometry and Trigonometry', 'Circles', 'Easy',
            r'<p>Circle \(N\) has a radius of \(6\) millimeters (mm). Circle \(M\) has an area of \(121\pi\text{ mm}^2\).</p>',
            r'What is the total area, in \(\text{mm}^2\), of circles \(N\) and \(M\)?',
            {
                'A': r'\(17\pi\)',
                'B': r'\(133\pi\)',
                'C': r'\(145\pi\)',
                'D': r'\(157\pi\)',
            },
            'D',
            r'Diện tích hình tròn \(N\) có bán kính \(r = 6\text{ mm}\) là: \[A_N = \pi r^2 = \pi(6)^2 = 36\pi\text{ mm}^2.\] Tổng diện tích của hai hình tròn \(N\) và \(M\) là: \[A_N + A_M = 36\pi + 121\pi = 157\pi\text{ mm}^2.\]',
            r'Chú ý đơn vị đã cho: hình tròn \(N\) cho bán kính (\(6\)), còn hình tròn \(M\) đã cho sẵn diện tích (\(121\pi\)). Tính \(A_N = \pi r^2 = 36\pi\) rồi cộng lại.',
            {
                'A': ('Cộng hai bán kính', r'Tính bán kính hình tròn \(M\) là \(\sqrt{121} = 11\), rồi cộng nhầm \(6 + 11 = 17\) và gắn \(\pi\).'),
                'B': ('Dùng công thức chu vi 2πr', r'Tính nhầm diện tích hình tròn \(N\) thành chu vi \(2\pi(6) = 12\pi\), rồi cộng \(12\pi + 121\pi = 133\pi\).'),
                'C': ('Sai phép bình phương', r'Tính nhầm \(6^2 = 24\), dẫn đến \(24\pi + 121\pi = 145\pi\).'),
                'D': ('Đáp án đúng', r'\(36\pi + 121\pi = 157\pi\).'),
            },
            r'Gõ `6^2 + 121` vào Desmos ra `157`, suy ra tổng diện tích là `157π`.',
        ),
        # M2 Q7
        _mcq(
            f'{id_prefix}_q7', 7, 'Algebra', 'Linear equations in two variables', 'Medium',
            r'<p>Consider the linear equation in the \(xy\)-plane:</p><p style="text-align:center;font-size:18px;">\[y = \frac{1}{4}(27x + 12) + 7x\]</p>',
            r'What is the slope of the graph of \(y = \frac{1}{4}(27x + 12) + 7x\) in the \(xy\)-plane?',
            {
                'A': r'\(\frac{27}{4}\)',
                'B': r'\(\frac{55}{4}\)',
                'C': r'\(27\)',
                'D': r'\(34\)',
            },
            'B',
            r'Khai triển và gom các số hạng chứa \(x\) về dạng \(y = mx + b\): \[y = \frac{27}{4}x + 3 + 7x = \left(\frac{27}{4} + \frac{28}{4}\right)x + 3 = \frac{55}{4}x + 3.\] Vậy hệ số góc (slope) của đường thẳng là \(m = \frac{55}{4}\).',
            r'Đừng quên cộng thêm số hạng \(+ 7x\) nằm ngoài dấu ngoặc! Quy đồng mẫu số chung \(4\): \(7 = \frac{28}{4}\), nên \(\frac{27}{4} + \frac{28}{4} = \frac{55}{4}\).',
            {
                'A': ('Bỏ sót +7x', r'Chỉ lấy hệ số của \(x\) từ \(\frac{1}{4}(27x) = \frac{27}{4}\) mà quên cộng thêm \(7\).'),
                'B': ('Đáp án đúng', r'\(\frac{27}{4} + 7 = \frac{27 + 28}{4} = \frac{55}{4}\).'),
                'C': ('Bỏ quên cả 1/4 và +7x', r'Chỉ đọc số \(27\) đứng trước \(x\) trong ngoặc.'),
                'D': ('Bỏ quên hệ số 1/4', r'Cộng trực tiếp \(27 + 7 = 34\) mà quên nhân \(27\) với \(\frac{1}{4}\).'),
            },
            r'Gõ `27/4 + 7` vào Desmos rồi nhấn nút chuyển sang phân số (biểu tượng phân số bên trái ô nhập) sẽ ra ngay `55/4`.',
        ),
        # M2 Q8
        _mcq(
            f'{id_prefix}_q8', 8, 'Algebra', 'Linear functions', 'Easy',
            r'<p>The function \(f\) is defined by \(f(x) = \frac{x + 16}{5}\), and \(f(a) = -19\), where \(a\) is a constant.</p>',
            r'What is the value of \(a\)?',
            {
                'A': r'\(-111\)',
                'B': r'\(-79\)',
                'C': r'\(-\frac{79}{5}\)',
                'D': r'\(-\frac{3}{5}\)',
            },
            'A',
            r'Thay \(x = a\) vào công thức hàm số và cho bằng \(-19\): \[\frac{a + 16}{5} = -19 \implies a + 16 = -95 \implies a = -95 - 16 = -111.\]',
            r'Cẩn thận dấu âm khi chuyển vế: \(-95 - 16 = -111\) (cộng hai số âm), tránh nhầm thành \(-95 + 16 = -79\) (bẫy B).',
            {
                'A': ('Đáp án đúng', r'\(\frac{-111 + 16}{5} = \frac{-95}{5} = -19\).'),
                'B': ('Chuyển vế sai dấu', r'Tính nhầm \(-95 + 16 = -79\) thay vì \(-95 - 16 = -111\).'),
                'C': ('Chưa nhân 5 cho 16', r'Tính nhầm \(a = -19 + \frac{16}{5} = -\frac{79}{5}\).'),
                'D': ('Tính nhầm f(-19)', r'Thế nhầm \(x = -19\) vào \(f(x)\): \(f(-19) = \frac{-19 + 16}{5} = -\frac{3}{5}\).'),
            },
            r'Gõ `(x + 16)/5 = -19` vào Desmos sẽ hiện ngay đường đứng tại `x = -111` — tuyệt đối không bị sai dấu!',
        ),
        # M2 Q9
        _mcq(
            f'{id_prefix}_q9', 9, 'Problem-Solving and Data Analysis', 'One-variable data: Distributions and measures of center and spread', 'Medium',
            _svg_m2_q9_dotplot() + r'<p>A data set of the orbital periods, rounded to the nearest whole number of Earth days, for \(13\) of Jupiter’s moons is represented in the dot plot. An additional moon with an orbital period of \(251\) days is added to the original data set to create a new data set of \(14\) orbital periods.</p>',
            r'Which statement best compares the mean and median of the new data set to the mean and median of the original data set?',
            {
                'A': r'The mean of the new data set is equal to the mean of the original data set, and the median of the new data set is equal to the median of the original data set.',
                'B': r'The mean of the new data set is equal to the mean of the original data set, and the median of the new data set is less than the median of the original data set.',
                'C': r'The mean of the new data set is less than the mean of the original data set, and the median of the new data set is less than the median of the original data set.',
                'D': r'The mean of the new data set is less than the mean of the original data set, and the median of the new data set is equal to the median of the original data set.',
            },
            'D',
            r'Liệt kê \(13\) giá trị ban đầu theo thứ tự tăng dần từ dot plot: \[720,\; 720,\; 723,\; 723,\; 723,\; 724,\; \mathbf{724},\; 726,\; 727,\; 728,\; 730,\; 730,\; 732.\] • Trung bình (mean) ban đầu là \(\frac{9430}{13} \approx 725.38\). Khi thêm ngoại lai rất nhỏ là \(251\) vào, trung bình mới giảm mạnh còn \(\frac{9681}{14} = 691.5 < 725.38\).<br/>• Trung vị (median) ban đầu (\(13\) số) là số đứng thứ \(7\): \(724\). Khi thêm \(251\) ở đầu dãy (\(14\) số), trung vị mới là trung bình của số thứ \(7\) và thứ \(8\): cả hai vị trí này đều là \(724\) nên \(\text{new median} = \frac{724 + 724}{2} = 724\) (KHÔNG ĐỔI)!',
            r'Đừng đoán vội rằng thêm ngoại lai nhỏ thì trung vị phải giảm! Phải đếm chính xác vị trí trung vị cũ (thứ \(7\)) và hai vị trí trung vị mới (thứ \(7\) & thứ \(8\)): khi hai số kề nhau ở giữa trùng giá trị (\(724\) và \(724\)), trung vị giữ nguyên!',
            {
                'A': ('Sai về Mean', r'Thêm một giá trị \(251\) nhỏ hơn tất cả các giá trị cũ chắc chắn kéo giá trị trung bình (mean) giảm xuống.'),
                'B': ('Sai cả Mean và Median', r'Mean chắc chắn giảm, trong khi median thực tế không đổi.'),
                'C': ('Bẫy đếm thiếu chấm ở 724', r'Mean đúng là giảm, nhưng do tại \(724\) có tới \(2\) chấm (vị trí thứ \(6\) và \(7\) cũ \(\to\) thứ \(7\) và \(8\) mới), trung vị vẫn bằng \(724\), không hề giảm.'),
                'D': ('Đáp án đúng', r'Mean giảm (từ \(\approx 725.38\) xuống \(691.5\)), còn median giữ nguyên bằng \(724\).'),
            },
            r'Tạo danh sách trong Desmos: `A = [720,720,723,723,723,724,724,726,727,728,730,730,732]` và `B = [251,720,720,723,723,723,724,724,726,727,728,730,730,732]`, rồi bấm `mean(A)`, `mean(B)`, `median(A)`, `median(B)` để kiểm chứng tuyệt đối!',
        ),
        # M2 Q10
        _mcq(
            f'{id_prefix}_q10', 10, 'Algebra', 'Linear functions', 'Medium',
            r'<p>For the linear function \(p\), \(p(c) = -2\), where \(c\) is a constant, \(p(5) = 34\), and the slope of the graph of \(y = p(x)\) in the \(xy\)-plane is \(6\). For the linear function \(t\), \(t(c) = -4\) and \(t(6) = 52\).</p>',
            r'What is the slope of the graph of \(y = t(x)\) in the \(xy\)-plane?',
            {
                'A': r'\(-1\)',
                'B': r'\(4\)',
                'C': r'\(6\)',
                'D': r'\(8\)',
            },
            'D',
            r'Bước 1 — Tìm \(c\) từ hàm tuyến tính \(p\): Đồ thị \(p\) đi qua \((c, -2)\) và \((5, 34)\) với hệ số góc \(6\): \[\frac{34 - (-2)}{5 - c} = 6 \implies \frac{36}{5 - c} = 6 \implies 5 - c = 6 \implies c = -1.\] Bước 2 — Tính hệ số góc của hàm tuyến tính \(t\) đi qua \((c, -4) = (-1, -4)\) và \((6, 52)\): \[m_t = \frac{52 - (-4)}{6 - (-1)} = \frac{56}{7} = 8.\]',
            r'Bài toán 2 bước liên kết qua hằng số chung \(c\): dùng công thức hệ số góc của hàm thứ nhất để tìm \(c = -1\), sau đó thế ngay \(c\) vào hàm thứ hai để tính hệ số góc mới.',
            {
                'A': ('Bẫy dừng ở c', r'\(-1\) là giá trị của hằng số \(c\), chưa phải hệ số góc của \(t\).'),
                'B': ('Sai dấu khi trừ số âm', r'Tính sai mẫu số hoặc tử số khi trừ số âm \((-1)\) và \((-4)\).'),
                'C': ('Nhầm hệ số góc của p', r'\(6\) là hệ số góc của hàm \(p\), không phải hàm \(t\).'),
                'D': ('Đáp án đúng', r'Với \(c = -1\), hệ số góc của \(t\) là \(\frac{52 - (-4)}{6 - (-1)} = \frac{56}{7} = 8\).'),
            },
            r'Gõ `(34 - (-2))/(5 - c) = 6` vào Desmos ra `c = -1`, rồi gõ `(52 - (-4))/(6 - (-1))` được ngay `8`.',
        ),
        # M2 Q11 (SPR)
        _spr(
            f'{id_prefix}_q11', 11, 'Advanced Math', 'Nonlinear equations in one variable and systems of equations in two variables', 'Medium',
            r'<p style="text-align:center;font-size:18px;">\[18x^2 - 24x + c = 0\]</p><p>In the given equation, \(c\) is a constant. The equation has exactly one solution.</p>',
            r'What is the value of \(c\)?',
            ['8'],
            '8',
            r'Phương trình bậc hai \(ax^2 + bx + c = 0\) có đúng một nghiệm (nghiệm kép) khi và chỉ khi biệt thức \(\Delta = b^2 - 4ac = 0\): \[(-24)^2 - 4(18)(c) = 0 \implies 576 - 72c = 0 \implies c = \frac{576}{72} = 8.\] (Kiểm tra: \(18x^2 - 24x + 8 = 2(3x - 2)^2 = 0\) có nghiệm duy nhất \(x = \frac{2}{3}\)).',
            r'Từ khóa “exactly one solution” (đúng 1 nghiệm) của phương trình bậc hai \(\iff \Delta = b^2 - 4ac = 0\).',
            r'Gõ `y = 18x^2 - 24x + c` kèm thanh trượt (slider) `c` vào Desmos, hoặc gõ thẳng `(-24)^2 / (4 * 18)` để nhận ngay kết quả `8`.',
        ),
        # M2 Q12
        _mcq(
            f'{id_prefix}_q12', 12, 'Geometry and Trigonometry', 'Area and volume', 'Medium',
            r'<p>A conservation specialist hung artificial nesting structures each in the shape of a right rectangular prism for a species of native owl. Each structure has a height of \(11\) inches. The length of each structure’s base is \(x\) inches, which is \(1\) inch more than the width of the structure’s base.</p>',
            r'Which function \(V\) gives the volume of each structure, in cubic inches, in terms of the length of the structure’s base?',
            {
                'A': r'\(V(x) = 11x(x - 1)\)',
                'B': r'\(V(x) = 11x(x + 1)\)',
                'C': r'\(V(x) = x(x + 11)(x - 1)\)',
                'D': r'\(V(x) = x(x + 11)(x + 1)\)',
            },
            'A',
            r'• Chiều cao: \(h = 11\text{ inches}\).<br/>• Chiều dài đáy: \(l = x\text{ inches}\).<br/>• Vì chiều dài lớn hơn chiều rộng \(1\text{ inch}\) (“is \(1\) inch more than the width”), suy ra chiều rộng nhỏ hơn chiều dài \(1\text{ inch}\): \(w = x - 1\text{ inches}\).<br/>Thể tích hình hộp chữ nhật: \[V(x) = l \cdot w \cdot h = 11x(x - 1).\]',
            r'Đọc cẩn thận quan hệ chiều dài — chiều rộng: “length is \(x\), which is \(1\) more than width” nghĩa là \(x = w + 1 \implies w = x - 1\) (KHÔNG phải \(x + 1\))!',
            {
                'A': ('Đáp án đúng', r'Chiều cao \(11\), dài \(x\), rộng \(x - 1 \implies V(x) = 11x(x - 1)\).'),
                'B': ('Nhầm dấu width', r'Dịch ngược “\(1\) inch more than the width” thành \(w = x + 1\).'),
                'C': ('Nhầm chiều cao thành x + 11', r'Đề cho chiều cao cố định bằng \(11\), không phải “hơn chiều dài \(11\) inch”.'),
                'D': ('Sai cả chiều cao và chiều rộng', r'Nhầm cả \(h = x + 11\) lẫn \(w = x + 1\).'),
            },
            r'Thử số trực quan: giả sử dài \(x = 5\), thì rộng phải là \(4\) (nhỏ hơn dài \(1\) inch) và cao \(11\), nên thể tích là \(5 \times 4 \times 11 = 220\). Thế `x = 5` vào 4 đáp án: chỉ A cho `11 * 5 * 4 = 220`.',
        ),
        # M2 Q13 (SPR)
        _spr(
            f'{id_prefix}_q13', 13, 'Advanced Math', 'Nonlinear equations in one variable and systems of equations in two variables', 'Hard',
            r'<p style="text-align:center;font-size:18px;">\[\frac{x + 1}{5x^2} = \frac{k}{x}\]</p><p>In the given equation, \(k\) is a constant. The solution to the given equation is \(\frac{1}{224}\).</p>',
            r'What is the value of \(k\)?',
            ['45'],
            '45',
            r'Vì \(x = \frac{1}{224} \ne 0\), nhân hai vế phương trình với \(x\) để cô lập \(k\): \[k = \frac{x + 1}{5x} = \frac{1}{5} + \frac{1}{5x}.\] Thay \(x = \frac{1}{224}\) (tức \(\frac{1}{x} = 224\)): \[k = \frac{1 + 224}{5} = \frac{225}{5} = 45.\] Kiểm tra ngược: với \(k = 45\), \(\frac{x + 1}{5x^2} = \frac{45}{x} \iff x + 1 = 225x \iff 224x = 1 \iff x = \frac{1}{224}\).',
            r'Mẹo rút gọn phương trình phân thức: nhân hai vế với \(x\) trước khi thay số sẽ biến \(\frac{1}{x}\) thành số nguyên \(224\) siêu gọn gàng!',
            r'Đặt `x = 1/224` trong Desmos, rồi gõ `((x + 1) / (5 * x^2)) * x` sẽ hiện ngay chính xác `45`.',
        ),
        # M2 Q14
        _mcq(
            f'{id_prefix}_q14', 14, 'Advanced Math', 'Nonlinear functions', 'Hard',
            r'<p>The function \(f\) is defined by \(f(x) = -39^x\). The function \(g\) is a decreasing linear function. In the \(xy\)-plane, the graphs of \(y = f(x)\) and \(y = g(x)\) intersect at two points, \((h, j)\) and \((k, m)\), where \(j > m\).</p>',
            r'When \(g(x) < f(x)\), which of the following must also be true?',
            {
                'A': r'\(x > k\)',
                'B': r'\(x < h\)',
                'C': r'\(x > k\) or \(x < h\)',
                'D': r'\(h < x < k\)',
            },
            'D',
            r"Xét đồ thị hàm mũ \(f(x) = -39^x\): đây là hàm **nghịch biến** (giảm dần) và **lõm xuống** (concave down, vì \(f''(x) = -(\ln 39)^2 \cdot 39^x < 0\)), đồ thị cong hình mái vòm hướng xuống dưới.<br/>• Do cả \(f\) và \(g\) đều nghịch biến và hai giao điểm \((h, j), (k, m)\) thỏa \(j > m\), nên điểm \((h, j)\) nằm bên trái điểm \((k, m)\), tức \(h < k\).<br/>• Một đường thẳng \(g(x)\) cắt một đường cong lõm xuống \(f(x)\) tại hai điểm \(x = h\) và \(x = k\) thì trên đoạn giữa hai giao điểm (\(h < x < k\)), dây cung \(g(x)\) nằm **bên dưới** đường cong \(f(x)\), tức \(g(x) < f(x)\)! Ngược lại, ở ngoài khoảng (\(x < h\) hoặc \(x > k\)), đường thẳng \(g(x)\) nằm phía trên \(f(x)\).<br/><em>Thử số kiểm chứng:</em> chọn \(h = 0 \Rightarrow j = -1\), \(k = 1 \Rightarrow m = -39\), đường thẳng \(g(x) = -38x - 1\). Tại \(x = 0.5 \in (0, 1)\): \(g(0.5) = -20 < -\sqrt{39} \approx -6.24 = f(0.5)\) \(\implies\) ĐÚNG!",
            r'Bí kíp đồ thị lồi/lõm SAT 750+: Đường cong \(y = -a^x\) (\(a > 1\)) luôn lõm xuống (concave down), nên dây cung nối 2 giao điểm luôn nằm DƯỚI đường cong trên khoảng giữa \((h, k)\). Khi gặp bài trừu tượng, hãy vẽ mẫu trên Desmos với 2 điểm đẹp như \(x = 0\) và \(x = 1\)!',
            {
                'A': ('Miền ngoài phải', r'Khi \(x > k\), hàm mũ \(-39^x\) lao xuống âm vô cực nhanh hơn nhiều so với đường thẳng \(g(x)\), nên \(g(x) > f(x)\).'),
                'B': ('Miền ngoài trái', r'Khi \(x < h\), \(f(x) = -39^x\) tiệm cận \(0\) (bị chặn trên bởi \(0\)), trong khi đường thẳng nghịch biến \(g(x) \to +\infty\), nên \(g(x) > f(x)\).'),
                'C': ('Ngược miền bất đẳng thức', r'\(x > k\) hoặc \(x < h\) là miền mà \(g(x) > f(x)\), ngược dấu với điều kiện \(g(x) < f(x)\) của đề bài.'),
                'D': ('Đáp án đúng', r'Trên khoảng giữa hai giao điểm \(h < x < k\), đường cong lõm xuống \(f(x)\) nằm phía trên dây cung \(g(x)\), tức \(g(x) < f(x)\).'),
            },
            r'Mẹo Desmos cực mạnh: gõ `f(x) = -39^x`, chọn 2 giao điểm `(0, -1)` và `(1, -39)` rồi gõ đường thẳng đi qua hai điểm đó `g(x) = -38x - 1`. Nhìn hình sẽ thấy ngay đoạn `g(x)` nằm DƯỚI `f(x)` chính là khoảng giữa `0 < x < 1` (tức `h < x < k`)!',
        ),
        # M2 Q15
        _mcq(
            f'{id_prefix}_q15', 15, 'Problem-Solving and Data Analysis', 'Ratios, rates, proportional relationships, and units', 'Medium',
            r'<p>One gallon of sealant costs $29 and will cover \(300\) square feet of a surface. A deck has a total surface area of \(d\) square feet.</p>',
            r'Which equation represents the cost \(c\), in dollars, of the sealant needed to cover the deck twice?',
            {
                'A': r'\(c = \frac{300d}{29}\)',
                'B': r'\(c = \frac{600d}{29}\)',
                'C': r'\(c = 29\left(\frac{d}{150}\right)\)',
                'D': r'\(c = 29\left(\frac{d}{300}\right)\)',
            },
            'C',
            r'Để phủ sân gỗ **hai lần** (cover the deck twice), tổng diện tích cần phủ là \(2d\text{ square feet}\). Vì mỗi gallon phủ được \(300\text{ square feet}\), số gallon chất phủ cần dùng là: \[\frac{2d}{300} = \frac{d}{150}\text{ (gallons)}.\] Nhân với đơn giá \(\$29/\text{gallon}\), ta được tổng chi phí: \[c = 29\left(\frac{d}{150}\right).\]',
            r'Luôn gạch chân từ khóa số lần phủ (“twice”) và kiểm tra đơn vị (dimensional analysis): \(\text{dollars} = \frac{\$29}{1\text{ gal}} \times \frac{2d\text{ ft}^2}{300\text{ ft}^2/\text{gal}}\).',
            {
                'A': ('Đảo ngược tỉ lệ', r'Nhân nhầm với \(300\) và chia cho \(29\), sai hoàn toàn thứ nguyên đơn vị.'),
                'B': ('Đảo ngược tỉ lệ', r'Vừa đảo ngược công thức vừa nhân đôi sai chỗ.'),
                'C': ('Đáp án đúng', r'Phủ hai lần diện tích \(d\) cần \(\frac{2d}{300} = \frac{d}{150}\) gallon, chi phí \(c = 29\left(\frac{d}{150}\right)\).'),
                'D': ('Quên từ "twice"', r'Chỉ tính chi phí phủ sân \(1\) lần (\(\frac{d}{300}\) gallon), bỏ sót yêu cầu phủ \(2\) lần.'),
            },
            r'Thử số nhanh: nếu sân rộng \(d = 150\text{ ft}^2\), phủ \(2\) lần là \(300\text{ ft}^2 = 1\) gallon \(\Rightarrow c = \$29\). Thay `d = 150` vào 4 đáp án, chỉ C cho đúng `29`.',
        ),
        # M2 Q16 (SPR)
        _spr(
            f'{id_prefix}_q16', 16, 'Geometry and Trigonometry', 'Area and volume', 'Easy',
            r'<p>A triangular prism has a height of \(9\) centimeters (cm) and a volume of \(234\text{ cm}^3\). (The volume of a triangular prism is equal to \(Bh\), where \(B\) is the area of the base and \(h\) is the height of the prism.)</p>',
            r'What is the area, in \(\text{cm}^2\), of the base of the prism?',
            ['26'],
            '26',
            r'Áp dụng công thức thể tích lăng trụ \(V = Bh\) với \(V = 234\text{ cm}^3\) và \(h = 9\text{ cm}\): \[234 = B \cdot 9 \implies B = \frac{234}{9} = 26\text{ cm}^2.\]',
            r'Không bị đánh lừa bởi từ “triangular” mà chia thêm cho \(2\) hoặc \(3\) — đề đã cho sẵn công thức \(V = Bh\), chỉ cần chia \(V\) cho \(h\).',
            r'Gõ `234 / 9` vào Desmos ra ngay `26`.',
        ),
        # M2 Q17 (SPR)
        _spr(
            f'{id_prefix}_q17', 17, 'Problem-Solving and Data Analysis', 'Ratios, rates, proportional relationships, and units', 'Medium',
            r'<p>An area of \(56.00\) square nautical miles is equivalent to \(k\) square kilometers. (\(1\text{ nautical mile} = 1.852\text{ kilometers}\))</p>',
            r'To the nearest tenth, what is the value of \(k\)?',
            ['192.1'],
            '192.1',
            r'Chú ý đây là đổi đơn vị **DIỆN TÍCH** (square nautical miles \(\to\) square kilometers), nên phải BÌNH PHƯƠNG hệ số quy đổi độ dài: \[1\text{ sq nautical mile} = (1.852)^2\text{ km}^2 = 3.429904\text{ km}^2.\] Do đó: \[k = 56.00 \times (1.852)^2 = 56 \times 3.429904 = 192.074624.\] Làm tròn đến hàng phần mười (nearest tenth): \(k \approx 192.1\).',
            r'Bẫy kinh điển SAT: đổi đơn vị diện tích (\(\text{square units}\)) BẮT BUỘC phải bình phương tỉ lệ quy đổi \((1.852)^2\) — tuyệt đối không nhân mỗi \(56 \times 1.852\)!',
            r'Gõ `56 * 1.852^2` vào Desmos ra `192.074624`, làm tròn đến 1 chữ số thập phân thành `192.1`.',
        ),
        # M2 Q18 (SPR)
        _spr(
            f'{id_prefix}_q18', 18, 'Geometry and Trigonometry', 'Circles', 'Hard',
            r'<p>A circle in the \(xy\)-plane has its center at \((-7, 3)\) and has a radius of \(9\). An equation of this circle is \(x^2 + y^2 + ax + by + c = 0\), where \(a\), \(b\), and \(c\) are constants.</p>',
            r'What is the value of \(c\)?',
            ['-23'],
            '-23',
            r'Phương trình chính tắc của đường tròn tâm \((h, k) = (-7, 3)\), bán kính \(r = 9\) là: \[(x + 7)^2 + (y - 3)^2 = 9^2.\] Khai triển và chuyển hết sang vế trái: \[(x^2 + 14x + 49) + (y^2 - 6y + 9) - 81 = 0\] \[x^2 + y^2 + 14x - 6y + (49 + 9 - 81) = 0 \implies x^2 + y^2 + 14x - 6y - 23 = 0.\] Đối chiếu với \(x^2 + y^2 + ax + by + c = 0\), ta được \(c = -23\).',
            r'Công thức nhanh cho hệ số tự do \(c\) của phương trình đường tròn tổng quát \(x^2 + y^2 + ax + by + c = 0\): \(c = h^2 + k^2 - r^2 = (-7)^2 + 3^2 - 9^2 = 49 + 9 - 81 = -23\).',
            r'Gõ `(-7)^2 + 3^2 - 9^2` vào Desmos ra ngay `-23`. Kiểm chứng lại bằng cách vẽ đồng thời `(x + 7)^2 + (y - 3)^2 = 81` và `x^2 + y^2 + 14x - 6y - 23 = 0` — hai đường tròn chồng khít 100%!',
        ),
        # M2 Q19
        _mcq(
            f'{id_prefix}_q19', 19, 'Advanced Math', 'Nonlinear equations in one variable and systems of equations in two variables', 'Hard',
            r'<p style="text-align:center;font-size:18px;">\[\begin{aligned} y &= x - c \\ y &= -4(x - 6)^2 \end{aligned}\]</p><p>In the given system of equations, \(c\) is a constant. The system has two distinct real solutions.</p>',
            r'Which of the following could be the value of \(c\)?',
            {
                'A': r'\(1\)',
                'B': r'\(5\)',
                'C': r'\(\frac{95}{16}\)',
                'D': r'\(11\)',
            },
            'D',
            r'Cho hai vế phải bằng nhau để lập phương trình hoành độ giao điểm: \[x - c = -4(x - 6)^2 \implies x - c = -4(x^2 - 12x + 36)\] \[\implies 4x^2 - 47x + (144 - c) = 0.\] Hệ có **hai nghiệm thực phân biệt** khi và chỉ khi biệt thức \(\Delta > 0\): \[\Delta = (-47)^2 - 4(4)(144 - c) > 0 \implies 2209 - 2304 + 16c > 0\] \[\implies 16c > 95 \implies c > \frac{95}{16} = 5.9375.\] Trong 4 đáp án, chỉ có \(c = 11 > 5.9375\) thỏa mãn!',
            r'Hệ đường thẳng + parabol có \(2\) nghiệm thực phân biệt \(\iff\) phương trình bậc hai sau khi thế có \(\Delta > 0\). Chú ý bẫy C (\(\frac{95}{16}\)) là nghiệm biên cho \(\Delta = 0\) (chỉ có ĐÚNG \(1\) nghiệm tiếp xúc)!',
            {
                'A': ('Vô nghiệm (Δ < 0)', r'Với \(c = 1 < \frac{95}{16}\), \(\Delta = 16(1) - 95 = -79 < 0\), đường thẳng nằm hoàn toàn phía trên parabol (0 giao điểm).'),
                'B': ('Vô nghiệm (Δ < 0)', r'Với \(c = 5 < \frac{95}{16}\), \(\Delta = 16(5) - 95 = -15 < 0\), hệ vô nghiệm thực.'),
                'C': ('Bẫy biên tiếp xúc (Δ = 0)', r'Với \(c = \frac{95}{16}\), \(\Delta = 0\) nên hệ chỉ có ĐÚNG \(1\) nghiệm thực (đường thẳng tiếp tuyến parabol), không phải \(2\) nghiệm phân biệt.'),
                'D': ('Đáp án đúng', r'Với \(c = 11 > \frac{95}{16}\), \(\Delta = 16(11) - 95 = 81 > 0\), hệ có \(2\) nghiệm thực phân biệt.'),
            },
            r'Gõ `y = -4(x - 6)^2` và `y = x - c` kèm slider `c` vào Desmos: kéo/nhập lần lượt `c = 1, 5, 95/16, 11` sẽ thấy ngay chỉ `c = 11` cắt parabol tại 2 điểm rõ rệt!',
        ),
        # M2 Q20
        _mcq(
            f'{id_prefix}_q20', 20, 'Advanced Math', 'Nonlinear functions', 'Hard',
            r'<p>The functions \(f\) and \(g\) are defined by the equations shown, where \(a\) and \(b\) are integer constants, \(a < b\) and \(b < 0\). If \(y = f(x)\) and \(y = g(x)\) are graphed in the \(xy\)-plane, consider the two equations:</p><div style="margin:8px 0 8px 18px;line-height:2;">I. \(f(x) = a(4.2)^{x+b}\)<br/>II. \(g(x) = a(4.2)^x + b\)</div>',
            r'Which of the following equations displays, as a constant or coefficient, the \(y\)-coordinate of the \(y\)-intercept of the graph of the corresponding function?',
            {
                'A': r'I only',
                'B': r'II only',
                'C': r'I and II',
                'D': r'Neither I nor II',
            },
            'D',
            r'Tung độ của giao điểm với trục tung (\(y\)-intercept) chính là giá trị hàm số tại \(x = 0\). Ta biết \(a < b < 0\) (cả hai đều là số nguyên âm, \(b \le -1\), \(a \le -2\)):<br/>• <b>Xét I:</b> \(f(0) = a(4.2)^{0+b} = a(4.2)^b\). Các hằng số/hệ số hiển thị trong công thức I là \(a\), \(4.2\), \(b\). Vì \(b < 0\), \((4.2)^b \ne 1\) nên \(a(4.2)^b \ne a\); hơn nữa \(a(4.2)^b < 0 < 4.2\) và do \((4.2)^b = \left(\frac{5}{21}\right)^{|b|}\) khiến \(a(4.2)^b\) không bao giờ bằng nguyên \(b\) (bởi \(5^{|b|} > |b|\)). Vậy I KHÔNG hiển thị tung độ gốc.<br/>• <b>Xét II:</b> \(g(0) = a(4.2)^0 + b = a + b\). Các hằng số/hệ số hiển thị trong công thức II là \(a\), \(4.2\), \(b\). Vì \(a < 0\) và \(b < 0\), ta có \(a + b < a\), \(a + b < b\) và \(a + b < 0 < 4.2\). Vậy II cũng KHÔNG hiển thị tung độ gốc.<br/>Kết luận: <b>Neither I nor II</b>.',
            r'Câu tủ SAT Hard Band 750+: Chỉ phương trình dạng chuẩn \(y = A(r)^x\) (không có \(+b\) ở mũ lẫn \(+b\) ở ngoài) mới hiển thị trực tiếp tung độ gốc \(y(0) = A\) là hệ số! Có thêm \(+b\) ở mũ thì \(y(0) = a \cdot r^b\), còn thêm \(+b\) ở ngoài thì \(y(0) = a + b\).',
            {
                'A': ('Bẫy bỏ quên +b ở mũ', r'Nhầm \(f(0) = a\), quên mất số mũ \(x + b\) khiến \(f(0) = a(4.2)^b \ne a\).'),
                'B': ('Bẫy nhầm hàm mũ với tuyến tính', r'Nhầm \(+b\) là \(y\)-intercept giống đường thẳng \(y = mx + b\), quên mất tại \(x = 0\) thì \((4.2)^0 = 1\) (không phải \(0\)), nên \(g(0) = a + b \ne b\).'),
                'C': ('Dính cả hai bẫy', r'Cả hai phương trình đều không hiển thị giá trị tại \(x = 0\) dưới dạng hằng số hay hệ số.'),
                'D': ('Đáp án đúng', r'\(f(0) = a(4.2)^b\) và \(g(0) = a + b\) đều không xuất hiện dưới dạng hằng số hay hệ số trong hai phương trình.'),
            },
            r'Thử cặp số nguyên thỏa \(a < b < 0\) trên Desmos, ví dụ `a = -2`, `b = -1`: `f(0) = -2*(4.2)^(-1) ≈ -0.476` (khác `-2`, `-1`, `4.2`) và `g(0) = -2*(4.2)^0 + (-1) = -3` (khác `-2`, `-1`, `4.2`) \(\implies\) chọn ngay D!',
        ),
        # M2 Q21
        _mcq(
            f'{id_prefix}_q21', 21, 'Algebra', 'Systems of two linear equations in two variables', 'Hard',
            r'<p style="text-align:center;font-size:18px;">\[\begin{aligned} 5x + 4y &= 3 \\ 15x + 12y &= 9 \end{aligned}\]</p>',
            r'For each real number \(r\), which of the following points lies on the graph of each equation in the \(xy\)-plane for the given system?',
            {
                'A': r'\(\left(r, -\frac{4r}{5} + \frac{3}{5}\right)\)',
                'B': r'\(\left(r, \frac{5r}{4} + \frac{3}{4}\right)\)',
                'C': r'\(\left(-\frac{4r}{5} + \frac{3}{5}, r\right)\)',
                'D': r'\(\left(\frac{r}{3} + 3, -\frac{r}{3} + 9\right)\)',
            },
            'C',
            r'Nhận xét: phương trình thứ hai \(15x + 12y = 9\) chính là phương trình thứ nhất nhân với \(3\), nên hai đường thẳng trùng nhau (vô số nghiệm chung cùng nằm trên đường thẳng \(5x + 4y = 3\)).<br/>Đặt \(y = r\), giải tìm \(x\) theo \(r\): \[5x + 4r = 3 \implies 5x = -4r + 3 \implies x = -\frac{4r}{5} + \frac{3}{5}.\] Do đó mọi điểm dạng \(\left(-\frac{4r}{5} + \frac{3}{5},\; r\right)\) đều thuộc đồ thị của cả hai phương trình.<br/><em>Kiểm tra lại:</em> \(5\left(-\frac{4r}{5} + \frac{3}{5}\right) + 4(r) = -4r + 3 + 4r = 3\) (đúng với mọi \(r \in \mathbb{R}\)).',
            r'Đừng chỉ giải \(y\) theo \(x = r\)! Nếu giải \(y = -\frac{5r}{4} + \frac{3}{4}\) không thấy trong đáp án, hãy lập tức đặt \(y = r\) và giải \(x\) theo \(r\) (hoặc thử \(r = 0\) và \(r = 1\) vào phương trình \(5x + 4y = 3\) để loại đáp án trong 5 giây).',
            {
                'A': ('Đảo ngược tọa độ x và y', r'Thế \(r = 0\) được \((0, \frac{3}{5})\): \(5(0) + 4(\frac{3}{5}) = \frac{12}{5} \ne 3\). Thực ra đây là kết quả khi giải \(x\) theo \(y\) nhưng đặt nhầm vào vị trí \(y\).'),
                'B': ('Sai dấu hệ số góc', r'Nếu đặt \(x = r\) thì \(y = -\frac{5r}{4} + \frac{3}{4}\) (dấu trừ), không phải \(+\frac{5r}{4}\). Thế \(r = 1\): \((1, 2) \Rightarrow 5(1) + 4(2) = 13 \ne 3\).'),
                'C': ('Đáp án đúng', r'Với mọi \(r\), \(5\left(-\frac{4r}{5} + \frac{3}{5}\right) + 4r = 3\) và \(15x + 12y = 9\) đều đúng.'),
                'D': ('Không thỏa phương trình', r'Thế \(r = 0\) được \((3, 9)\): \(5(3) + 4(9) = 51 \ne 3\).'),
            },
            r'Mẹo thử số Desmos 5 giây: chọn `r = 0`, kiểm tra xem điểm nào thỏa `5x + 4y = 3` — A cho `(0, 0.6)` (`5*0 + 4*0.6 = 2.4`), B cho `(0, 0.75)` (`3` — thử tiếp `r = 1` cho `(1, 2)` \(\Rightarrow 13 \ne 3\)), C cho `(0.6, 0)` (`3`) và `r = 1` cho `(-0.2, 1)` (`5*(-0.2) + 4*1 = 3` — ĐÚNG)!',
        ),
        # M2 Q22
        _mcq(
            f'{id_prefix}_q22', 22, 'Geometry and Trigonometry', 'Lines, angles, and triangles', 'Hard',
            r'<p>In triangle \(ABC\) and triangle \(DEF\), sides \(AB\) and \(DE\) each have a side length of \(10\) inches, and angles \(A\) and \(D\) each have an angle measure of \(40^\circ\). Consider the following three additional pieces of information:</p><div style="margin:8px 0 8px 18px;line-height:1.9;">I. The measures of angles \(B\) and \(C\) are equal.<br/>II. The lengths of sides \(AC\) and \(DF\) are equal.<br/>III. The lengths of sides \(BC\) and \(EF\) are equal.</div>',
            r'Which of the following additional pieces of information is(are) sufficient to prove whether triangle \(ABC\) is congruent to triangle \(DEF\)?',
            {
                'A': r'I is sufficient, but II and III are not.',
                'B': r'II is sufficient, but I and III are not.',
                'C': r'III is sufficient, but I and II are not.',
                'D': r'II is sufficient and III is sufficient, but I is not.',
            },
            'B',
            r'Đã có sẵn: \(AB = DE = 10\text{ in}\) và \(\angle A = \angle D = 40^\circ\). Xét từng điều kiện bổ sung:<br/>• <b>Điều kiện I</b> (\(\angle B = \angle C\)): Chỉ xác định được tam giác \(ABC\) (\(\angle B = \angle C = 70^\circ\)), hoàn toàn KHÔNG có thông tin gì thêm về tam giác \(DEF\) (\(\angle E, \angle F\) vẫn tùy ý). Do đó không thể kết luận hai tam giác có bằng nhau hay không \(\implies\) <b>I KHÔNG đủ</b>.<br/>• <b>Điều kiện II</b> (\(AC = DF\)): Khi đó hai tam giác có \(AB = DE\), góc xen giữa \(\angle A = \angle D = 40^\circ\), và \(AC = DF\) \(\implies\) bằng nhau theo trường hợp **cạnh – góc – cạnh (SAS)** \(\implies\) <b>II ĐỦ</b>.<br/>• <b>Điều kiện III</b> (\(BC = EF\)): Cạnh \(BC\) và \(EF\) nằm đối diện góc \(40^\circ\), tạo thành trường hợp **cạnh – cạnh – góc (SSA)** — KHÔNG phải điều kiện bằng nhau của tam giác! Cụ thể, nếu \(10\sin 40^\circ < BC = EF < 10\) (ví dụ \(BC = EF = 8\)), tồn tại \(2\) tam giác KHÔNG bằng nhau (một tam giác có \(\angle C\) nhọn, một tam giác có \(\angle F = 180^\circ - \angle C\) tù) cùng thỏa dữ kiện \(\implies\) <b>III KHÔNG đủ</b>.',
            r'5 trường hợp bằng nhau hợp lệ của tam giác: **SSS, SAS, ASA, AAS, HL** (tam giác vuông). Hai bẫy kinh điển KHÔNG đảm bảo bằng nhau: **AAA** (chỉ đồng dạng) và **SSA** (trường hợp mơ hồ)!',
            {
                'A': ('Bẫy thiếu thông tin tam giác thứ hai', r'Điều kiện I chỉ nói về \(\triangle ABC\), không ràng buộc gì với \(\triangle DEF\).'),
                'B': ('Đáp án đúng', r'Chỉ điều kiện II tạo ra trường hợp SAS (\(AB = DE\), \(\angle A = \angle D\), \(AC = DF\)) đủ chứng minh \(\triangle ABC \cong \triangle DEF\).'),
                'C': ('Bẫy SSA', r'Điều kiện III chỉ cho trường hợp SSA (góc \(40^\circ\) không xen giữa hai cạnh bằng nhau), có thể tạo hai tam giác khác nhau.'),
                'D': ('Bẫy SSA kinh điển', r'Nhầm rằng biết \(2\) cạnh và \(1\) góc bất kỳ là đủ bằng nhau — quên rằng SSA không bảo đảm bằng nhau khi góc không xen giữa hai cạnh.'),
            },
            r'Kiểm chứng phản ví dụ SSA (điều kiện III) bằng Desmos (chế độ Degrees): với `AB = 10`, `A = 40°`, `BC = 8`, định lý sin cho `sin(C) = 10*sin(40)/8 ≈ 0.8035`, ra hai góc bù nhau hợp lệ `C ≈ 53.5°` (nhọn) và `F ≈ 126.5°` (tù) — hai tam giác hoàn toàn khác nhau!',
        ),
    ]


# ============================================================================
# ASSEMBLE FULL BLUEBOOK TEST DATA
# ============================================================================

M1_QUESTIONS = _build_m1_questions()
M2_HARD_QUESTIONS = _build_m2_questions('june25_usv1_m2')
M2_LOWER_QUESTIONS = _build_m2_questions('june25_usv1_m2l')

TEST_DATA = {
    'schemaVersion': 2,
    'mode': 'adaptive_mock',
    'section': 'math',
    'basicInfo': {
        'title': TEST_TITLE,
        'subtitle': 'Đề thi thật Digital SAT Toán Mỹ tháng 6/2025 (US Ver 1) — Đủ 2 Module (M1: 22 câu + M2: 22 câu)',
        'difficultyBadge': 'REAL EXAM • JUNE 2025 US',
        'targetTimeMinutes': 70,
        'routingThreshold': 0,
    },
    'module1': {
        'id': 'm1',
        'title': 'Section 2, Module 1: Math',
        'subtitle': '22 Questions • 35 Minutes • June 2025 US Ver 1',
        'timeLimitMinutes': 35,
        'questions': M1_QUESTIONS,
    },
    'module2_hard': {
        'id': 'm2_hard',
        'title': 'Section 2, Module 2: Math',
        'subtitle': '22 Questions • 35 Minutes • June 2025 US Ver 1',
        'timeLimitMinutes': 35,
        'questions': M2_HARD_QUESTIONS,
    },
    'module2_lower': {
        'id': 'm2_lower',
        'title': 'Section 2, Module 2: Math',
        'subtitle': '22 Questions • 35 Minutes • June 2025 US Ver 1',
        'timeLimitMinutes': 35,
        'questions': M2_LOWER_QUESTIONS,
    },
}


# ============================================================================
# MANDATORY MATHEMATICAL & SCHEMA AUDIT (ALL 44 QUESTIONS)
# ============================================================================

def verify_all_math():
    """Programmatically verifies all 44 math answers, options/SPR keys, KaTeX, and zero watermarks."""
    m1 = {q['number']: q for q in TEST_DATA['module1']['questions']}
    m2 = {q['number']: q for q in TEST_DATA['module2_hard']['questions']}
    assert len(m1) == 22 and len(m2) == 22, 'Expected 22 questions in each module'

    def _opt_text(q, lbl):
        return next(o['text'] for o in q['options'] if o['label'] == lbl)

    def _assert_mcq(q, expected_label):
        assert q['questionFormat'] == 'mcq', f"{q['id']}: expected mcq"
        assert q['correctAnswer'] == expected_label, (
            f"{q['id']}: expected {expected_label}, got {q['correctAnswer']}"
        )
        oa = q['explanation']['optionAnalysis']
        for lbl in ('A', 'B', 'C', 'D'):
            assert lbl in oa and oa[lbl]['reasonVi'].strip(), f"{q['id']}: missing optionAnalysis[{lbl}]"
            assert oa[lbl]['status'] == ('correct' if lbl == expected_label else 'trap')

    def _assert_spr(q, expected_val, expected_str):
        assert q['questionFormat'] == 'spr', f"{q['id']}: expected spr"
        assert q['correctAnswer'] == expected_str, (
            f"{q['id']}: expected correctAnswer={expected_str}, got {q['correctAnswer']}"
        )
        assert expected_str in q['acceptedAnswers'], f"{q['id']}: {expected_str} not in acceptedAnswers"
        for a in q['acceptedAnswers']:
            if '/' in a:
                num, den = a.split('/')
                val = Fraction(int(num), int(den))
            else:
                val = Fraction(a)
            assert val == expected_val, f"{q['id']}: acceptedAnswer {a} != {expected_val}"

    # ------------------------------------------------------------------
    # MODULE 1 VERIFICATION (Q1–Q22)
    # ------------------------------------------------------------------
    # M1 Q1: Line through (-5, -5) and (5, -7) -> y = -(1/5)x - 6 -> y-intercept (0, -6) -> D
    slope_m1q1 = Fraction(-7 - (-5), 5 - (-5))
    yint_m1q1 = -5 - slope_m1q1 * (-5)
    assert slope_m1q1 == Fraction(-1, 5) and yint_m1q1 == -6
    assert '(0, -6)' in _opt_text(m1[1], 'D')
    _assert_mcq(m1[1], 'D')

    # M1 Q2: Igneous probability = 10 / (10 + 38 + 22) = 10/70 -> A
    total_rocks = 10 + 38 + 22
    assert total_rocks == 70 and Fraction(10, total_rocks) == Fraction(1, 7)
    assert r'\frac{10}{70}' in _opt_text(m1[2], 'A')
    _assert_mcq(m1[2], 'A')

    # M1 Q3: Square A side 13, scale factor 3 -> Square B side 39 -> D
    assert 13 * 3 == 39 and '39' in _opt_text(m1[3], 'D')
    _assert_mcq(m1[3], 'D')

    # M1 Q4: f(x) = (1/9)(x - 6)^2 + 3, 0 <= x <= 10 -> min height at vertex (6, 3) is 3 -> A
    f_m1q4 = lambda x: Fraction(1, 9) * (x - 6) ** 2 + 3
    assert f_m1q4(6) == 3 and f_m1q4(0) == 7 and all(f_m1q4(x) >= 3 for x in range(11))
    _assert_mcq(m1[4], 'A')

    # M1 Q5: 3x = 8 -> 21x = 56 -> D
    x_m1q5 = Fraction(8, 3)
    assert 3 * x_m1q5 == 8 and 21 * x_m1q5 == 56 and '56' in _opt_text(m1[5], 'D')
    _assert_mcq(m1[5], 'D')

    # M1 Q6: at least 25, no more than 50 -> 25 <= x <= 50 -> C
    assert all((25 <= v <= 50) for v in (25, 37, 50)) and not (25 <= 24 <= 50) and not (25 <= 51 <= 50)
    assert r'25 \le x \le 50' in _opt_text(m1[6], 'C')
    _assert_mcq(m1[6], 'C')

    # M1 Q7: Mean of [10, 14, 22, 6, 24, 26, 14, 8, 8, 8] = 140/10 = 14 -> C
    data_m1q7 = [10, 14, 22, 6, 24, 26, 14, 8, 8, 8]
    assert len(data_m1q7) == 10 and Fraction(sum(data_m1q7), len(data_m1q7)) == 14
    assert '14' in _opt_text(m1[7], 'C')
    _assert_mcq(m1[7], 'C')

    # M1 Q8: f(x) = 7x + 3 -> f(0) = 3 (initial height when first measured) -> D
    assert 7 * 0 + 3 == 3 and (7 * 1 + 3) - (7 * 0 + 3) == 7
    _assert_mcq(m1[8], 'D')

    # M1 Q9: 2x^3 + 8x^2y + xy^2 + 4y^3 == (2x^2 + y^2)(x + 4y) -> B
    for xv, yv in ((2, 3), (-1, 5), (3, -2), (4, 1)):
        orig = 2 * xv**3 + 8 * xv**2 * yv + xv * yv**2 + 4 * yv**3
        optA = (2 * xv**2 + 4 * yv) * (xv + yv**2)
        optB = (2 * xv**2 + yv**2) * (xv + 4 * yv)
        optC = (2 * xv**3 + yv**2) * (xv**2 + 4 * yv**3)
        optD = (2 * xv**3 + yv**3) * (xv + 4 * yv)
        assert optB == orig and optA != orig and optC != orig and optD != orig
    _assert_mcq(m1[9], 'B')

    # M1 Q10 (SPR): f(x) = x^3 + 8x + 17 -> f(0) = 17
    b_m1q10 = 0**3 + 8 * 0 + 17
    assert b_m1q10 == 17
    _assert_spr(m1[10], Fraction(17), '17')

    # M1 Q11: y = 0.67(35) + 2.6 = 26.05 -> closest is 26 -> D
    y_m1q11 = Fraction(67, 100) * 35 + Fraction(26, 10)
    assert y_m1q11 == Fraction(521, 20)  # 26.05
    closest_m1q11 = min([114, 48, 38, 26], key=lambda v: abs(y_m1q11 - v))
    assert closest_m1q11 == 26 and '26' in _opt_text(m1[11], 'D')
    _assert_mcq(m1[11], 'D')

    # M1 Q12: b - 49 = x / y -> x = by - 49y -> B
    for bv, yv in ((51, 3), (60, 4), (100, 7)):
        xv = (bv - 49) * yv
        assert bv * yv - 49 * yv == xv
        assert Fraction(bv * yv - 49, yv) != xv
        assert bv * yv - 49 != xv
        assert Fraction(bv - 49, yv) != xv
    _assert_mcq(m1[12], 'B')

    # M1 Q13: 2y = 5x + 16, -2y = 7x - 22 -> x = 1/2, y = 37/4 -> 24x = 12 -> D
    x_m1q13 = Fraction(6, 12)
    y_m1q13 = Fraction(5 * x_m1q13 + 16, 2)
    assert 2 * y_m1q13 == 5 * x_m1q13 + 16 and -2 * y_m1q13 == 7 * x_m1q13 - 22
    assert 24 * x_m1q13 == 12 and '12' in _opt_text(m1[13], 'D')
    _assert_mcq(m1[13], 'D')

    # M1 Q14 (SPR): 19.5x + 24.25y = 583 -> 24.25 - 19.5 = 4.75 = 19/4
    diff_m1q14 = Fraction(2425, 100) - Fraction(1950, 100)
    assert diff_m1q14 == Fraction(19, 4)
    _assert_spr(m1[14], Fraction(19, 4), '4.75')

    # M1 Q15: f(x) = 55(1.04)^x -> f(7) ≈ 72.376 ≈ 72 -> D
    val_m1q15 = 55 * (1.04 ** 7)
    assert round(val_m1q15) == 72
    _assert_mcq(m1[15], 'D')

    # M1 Q16: y = x^2 + 18x - 23 -> vertex x = -9 -> B
    vx_m1q16 = Fraction(-18, 2)
    assert vx_m1q16 == -9
    f_m1q16 = lambda x: x**2 + 18 * x - 23
    assert all(f_m1q16(x) >= f_m1q16(-9) for x in (-23, -10, -9, -8, 9, 18))
    assert '-9' in _opt_text(m1[16], 'B')
    _assert_mcq(m1[16], 'B')

    # M1 Q17: P(t) = 260(1.03)^((3/2)t), every 8 months (2/3 yr) -> factor 1.03 -> 3% -> n = 3 -> D
    dt = Fraction(8, 12)
    assert Fraction(3, 2) * dt == 1
    growth_pct = (Fraction(103, 100) - 1) * 100
    assert growth_pct == 3 and '3' in _opt_text(m1[17], 'D')
    _assert_mcq(m1[17], 'D')

    # M1 Q18 (SPR): 47 meters = 4700 cm
    assert 47 * 100 == 4700
    _assert_spr(m1[18], Fraction(4700), '4700')

    # M1 Q19 (SPR): r_A = 3x, r_B = 135x -> area ratio = (135/3)^2 = 45^2 = 2025
    ratio_m1q19 = Fraction(135, 3) ** 2
    assert ratio_m1q19 == 2025
    _assert_spr(m1[19], Fraction(2025), '2025')

    # M1 Q20 (SPR): Line through (1, 5) and (9, 0) -> y-intercept (0, 45/8) = 5.625
    m_m1q20 = Fraction(0 - 5, 9 - 1)
    b_m1q20 = 5 - m_m1q20 * 1
    assert m_m1q20 == Fraction(-5, 8) and b_m1q20 == Fraction(45, 8) and m_m1q20 * 9 + b_m1q20 == 0
    _assert_spr(m1[20], Fraction(45, 8), '45/8')

    # M1 Q21 (SPR): 2a/b = 6.5 and a/(bn) = 26 -> n = 1/8 = 0.125
    ab_ratio = Fraction(65, 10) / 2
    n_m1q21 = ab_ratio / 26
    assert n_m1q21 == Fraction(1, 8) and ab_ratio / n_m1q21 == 26
    _assert_spr(m1[21], Fraction(1, 8), '1/8')

    # M1 Q22: cos(x + 61) = sin(4x + 4) acute -> (x + 61) + (4x + 4) = 90 -> x = 5 -> A
    x_m1q22 = Fraction(90 - 65, 5)
    assert x_m1q22 == 5 and 0 < (x_m1q22 + 61) < 90 and 0 < (4 * x_m1q22 + 4) < 90
    assert math.isclose(math.cos(math.radians(66)), math.sin(math.radians(24)))
    assert '5' in _opt_text(m1[22], 'A')
    _assert_mcq(m1[22], 'A')

    # ------------------------------------------------------------------
    # MODULE 2 VERIFICATION (Q1–Q22)
    # ------------------------------------------------------------------
    # M2 Q1: 14(x^2 - 6) = 14x^2 - 84 -> A
    for xv in (0, 1, 2, -3):
        orig = 14 * (xv**2 - 6)
        assert 14 * xv**2 - 84 == orig
        assert 14 * xv**2 - 20 != orig and 14 * xv**2 - 6 != orig and 14 * xv**2 + 8 != orig
    _assert_mcq(m2[1], 'A')

    # M2 Q2: 189 / 900 * 100 = 21% -> D
    assert Fraction(189, 900) * 100 == 21 and '21' in _opt_text(m2[2], 'D')
    _assert_mcq(m2[2], 'D')

    # M2 Q3: x + 5 = 11, y = 3x^2 + 3 -> (6, 111) -> B
    x_m2q3 = 11 - 5
    y_m2q3 = 3 * x_m2q3**2 + 3
    assert (x_m2q3, y_m2q3) == (6, 111) and '(6, 111)' in _opt_text(m2[3], 'B')
    _assert_mcq(m2[3], 'B')

    # M2 Q4 (SPR): (6/7)p + 42 = 84 -> p = 49 -> 7p = 343
    p_m2q4 = Fraction(84 - 42, 1) * Fraction(7, 6)
    assert p_m2q4 == 49 and 7 * p_m2q4 == 343
    _assert_spr(m2[4], Fraction(343), '343')

    # M2 Q5: 5(x + 4) = 4(x + 4) + 58 -> x + 4 = 58 -> C
    x_m2q5 = 54
    assert 5 * (x_m2q5 + 4) == 4 * (x_m2q5 + 4) + 58 and (x_m2q5 + 4) == 58
    assert '58' in _opt_text(m2[5], 'C')
    _assert_mcq(m2[5], 'C')

    # M2 Q6: r_N = 6 -> Area_N = 36pi, Area_M = 121pi -> total = 157pi -> D
    assert 6**2 + 121 == 157 and r'157\pi' in _opt_text(m2[6], 'D')
    _assert_mcq(m2[6], 'D')

    # M2 Q7: y = (1/4)(27x + 12) + 7x -> slope = 27/4 + 7 = 55/4 -> B
    slope_m2q7 = Fraction(27, 4) + 7
    assert slope_m2q7 == Fraction(55, 4) and r'\frac{55}{4}' in _opt_text(m2[7], 'B')
    _assert_mcq(m2[7], 'B')

    # M2 Q8: f(x) = (x + 16)/5, f(a) = -19 -> a = -111 -> A
    a_m2q8 = -19 * 5 - 16
    assert a_m2q8 == -111 and Fraction(a_m2q8 + 16, 5) == -19 and '-111' in _opt_text(m2[8], 'A')
    _assert_mcq(m2[8], 'A')

    # M2 Q9: Dot plot of 13 moons + 251 -> mean decreases, median stays 724 -> D
    orig_moons = sorted(val for val, cnt in M2_Q9_COUNTS.items() for _ in range(cnt))
    assert len(orig_moons) == 13
    new_moons = sorted(orig_moons + [251])
    assert len(new_moons) == 14
    orig_mean = Fraction(sum(orig_moons), 13)
    new_mean = Fraction(sum(new_moons), 14)
    orig_med = Fraction(orig_moons[6])  # 7th of 13 (0-indexed: 6)
    new_med = Fraction(new_moons[6] + new_moons[7], 2)  # avg of 7th & 8th of 14
    assert orig_med == 724 and new_med == 724 and new_mean < orig_mean and new_med == orig_med
    _assert_mcq(m2[9], 'D')

    # M2 Q10: p(c) = -2, p(5) = 34, slope 6 -> c = -1; t(-1) = -4, t(6) = 52 -> slope 8 -> D
    c_m2q10 = 5 - Fraction(34 - (-2), 6)
    slope_t = Fraction(52 - (-4), 6 - c_m2q10)
    assert c_m2q10 == -1 and slope_t == 8 and '8' in _opt_text(m2[10], 'D')
    _assert_mcq(m2[10], 'D')

    # M2 Q11 (SPR): 18x^2 - 24x + c = 0 has exactly 1 solution -> c = 8
    c_m2q11 = Fraction((-24) ** 2, 4 * 18)
    assert c_m2q11 == 8 and (-24) ** 2 - 4 * 18 * c_m2q11 == 0
    _assert_spr(m2[11], Fraction(8), '8')

    # M2 Q12: h = 11, l = x, w = x - 1 -> V(x) = 11x(x - 1) -> A
    for xv in (2, 5, 10):
        vol = 11 * xv * (xv - 1)
        assert 11 * xv * (xv - 1) == vol
        assert 11 * xv * (xv + 1) != vol and xv * (xv + 11) * (xv - 1) != vol and xv * (xv + 11) * (xv + 1) != vol
    _assert_mcq(m2[12], 'A')

    # M2 Q13 (SPR): (x + 1)/(5x^2) = k/x with solution x = 1/224 -> k = 45
    x_m2q13 = Fraction(1, 224)
    k_m2q13 = (x_m2q13 + 1) / (5 * x_m2q13)
    assert k_m2q13 == 45 and (x_m2q13 + 1) / (5 * x_m2q13**2) == k_m2q13 / x_m2q13
    _assert_spr(m2[13], Fraction(45), '45')

    # M2 Q14: f(x) = -39^x (decreasing, concave down), g(x) decreasing linear intersecting at (h,j),(k,m) j>m -> h<k
    # g(x) < f(x) iff h < x < k -> D
    f14 = lambda x: -(39.0 ** x)
    for h_v, k_v in ((0.0, 1.0), (-0.5, 0.5), (0.2, 1.5)):
        j_v, m_v = f14(h_v), f14(k_v)
        assert j_v > m_v and h_v < k_v
        slope_g = (m_v - j_v) / (k_v - h_v)
        assert slope_g < 0
        g14 = lambda x, hv=h_v, jv=j_v, sg=slope_g: jv + sg * (x - hv)
        # Strictly inside (h, k): g(x) < f(x)
        mid = (h_v + k_v) / 2.0
        assert g14(mid) < f14(mid)
        # Strictly outside: g(x) > f(x)
        assert g14(h_v - 0.5) > f14(h_v - 0.5) and g14(k_v + 0.5) > f14(k_v + 0.5)
    _assert_mcq(m2[14], 'D')

    # M2 Q15: $29/gal covers 300 ft^2; cover deck of area d twice -> c = 29*(2d/300) = 29*(d/150) -> C
    for d_v in (150, 300, 450):
        cost = Fraction(29 * 2 * d_v, 300)
        assert cost == 29 * Fraction(d_v, 150)
        assert cost != Fraction(300 * d_v, 29) and cost != Fraction(600 * d_v, 29) and cost != 29 * Fraction(d_v, 300)
    _assert_mcq(m2[15], 'C')

    # M2 Q16 (SPR): V = Bh, 234 = B*9 -> B = 26
    assert Fraction(234, 9) == 26
    _assert_spr(m2[16], Fraction(26), '26')

    # M2 Q17 (SPR): 56.00 * (1.852)^2 = 192.074624 -> nearest tenth 192.1
    k_exact = Fraction(56, 1) * (Fraction(1852, 1000) ** 2)
    assert round(float(k_exact), 1) == 192.1 and abs(float(k_exact) - 192.074624) < 1e-9
    _assert_spr(m2[17], Fraction(1921, 10), '192.1')

    # M2 Q18 (SPR): (x + 7)^2 + (y - 3)^2 = 9^2 -> c = 49 + 9 - 81 = -23
    c_m2q18 = (-7) ** 2 + 3 ** 2 - 9 ** 2
    assert c_m2q18 == -23
    _assert_spr(m2[18], Fraction(-23), '-23')

    # M2 Q19: y = x - c, y = -4(x - 6)^2 -> 4x^2 - 47x + (144 - c) = 0, Delta = 16c - 95 > 0 -> c > 95/16 -> D (11)
    disc_m2q19 = lambda c: (-47) ** 2 - 4 * 4 * (144 - c)
    assert disc_m2q19(1) < 0 and disc_m2q19(5) < 0 and disc_m2q19(Fraction(95, 16)) == 0 and disc_m2q19(11) > 0
    assert '11' in _opt_text(m2[19], 'D')
    _assert_mcq(m2[19], 'D')

    # M2 Q20: a < b < 0 integers; I: f(0) = a*(4.2)^b, II: g(0) = a + b -> Neither displays y-intercept -> D
    for a_v in range(-10, -1):
        for b_v in range(a_v + 1, 0):
            f0 = Fraction(a_v) * (Fraction(42, 10) ** b_v)
            g0 = Fraction(a_v + b_v)
            displayed = {Fraction(a_v), Fraction(b_v), Fraction(42, 10)}
            assert f0 not in displayed and g0 not in displayed
    _assert_mcq(m2[20], 'D')

    # M2 Q21: 5x + 4y = 3 & 15x + 12y = 9 -> point (-4r/5 + 3/5, r) -> C
    for r_v in (Fraction(0), Fraction(1), Fraction(-2), Fraction(5, 3)):
        xC, yC = -Fraction(4, 5) * r_v + Fraction(3, 5), r_v
        assert 5 * xC + 4 * yC == 3 and 15 * xC + 12 * yC == 9
    # Verify A, B, D fail for r = 1
    assert 5 * 1 + 4 * (-Fraction(4, 5) + Fraction(3, 5)) != 3  # A fails
    assert 5 * 1 + 4 * (Fraction(5, 4) + Fraction(3, 4)) != 3    # B fails
    assert 5 * (Fraction(1, 3) + 3) + 4 * (-Fraction(1, 3) + 9) != 3  # D fails
    _assert_mcq(m2[21], 'C')

    # M2 Q22: AB = DE = 10, angle A = D = 40 deg. I (B=C only ABC), II (AC=DF -> SAS), III (BC=EF -> SSA ambiguous) -> B
    # Numerical SSA counterexample for III: BC = EF = 8 in (10*sin(40°) ≈ 6.428 < 8 < 10)
    sin_c = 10 * math.sin(math.radians(40)) / 8
    assert 0 < sin_c < 1
    ang_c1 = math.degrees(math.asin(sin_c))
    ang_c2 = 180.0 - ang_c1
    assert 40 + ang_c1 < 180 and 40 + ang_c2 < 180 and not math.isclose(ang_c1, ang_c2)
    _assert_mcq(m2[22], 'B')

    # ------------------------------------------------------------------
    # CROSS-MODULE INTEGRITY, ZERO WATERMARKS & REAL NODE KATEX CHECK
    # ------------------------------------------------------------------
    all_ids = set()
    for mk in ('module1', 'module2_hard', 'module2_lower'):
        qs = TEST_DATA[mk]['questions']
        assert len(qs) == 22, f'{mk}: expected 22 questions, got {len(qs)}'
        for idx, q in enumerate(qs, 1):
            assert q['number'] == idx, f"{mk} Q{idx}: number mismatch {q['number']}"
            assert q['id'] not in all_ids, f"Duplicate global id {q['id']}"
            all_ids.add(q['id'])
            # Verify optionAnalysis KaTeX delimiter balance as well
            oa = q.get('explanation', {}).get('optionAnalysis') or {}
            for lbl, item in oa.items():
                rv = item.get('reasonVi', '')
                assert rv.count('\\(') == rv.count('\\)'), f"{q['id']} opt {lbl}: unbalanced \\( \\)"
                assert rv.count('\\[') == rv.count('\\]'), f"{q['id']} opt {lbl}: unbalanced \\[ \\]"
                assert not re.search(r'(?<!\\)\$[a-zA-Z\\]', rv), f"{q['id']} opt {lbl}: raw $ math delimiter"

    raw = str(TEST_DATA)
    for bad in ('@DSATuz', '@D7SAT', 'satuzhunters', 'Minh Nghĩa', 't.me/D7SAT', '______blank'):
        assert bad.lower() not in raw.lower(), f'Leaked watermark token "{bad}"!'

    errs = validate_sat_bluebook_json(TEST_DATA, TEST_CODE)
    assert not errs, f'validate_sat_bluebook_json failed:\n' + '\n'.join(errs)

    # Also verify optionAnalysis reasonVi through real Node KaTeX
    root_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    oa_blocks = []
    for mk in ('module1', 'module2_hard'):
        for q in TEST_DATA[mk]['questions']:
            oa = q.get('explanation', {}).get('optionAnalysis') or {}
            for lbl, item in oa.items():
                oa_blocks.append({'label': f"{mk}.Q{q['number']}.oa.{lbl}", 'text': item.get('reasonVi', '')})
    payload_path = os.path.join(root_dir, 'scratch', 'igcse_katex_payload.json')
    os.makedirs(os.path.dirname(payload_path), exist_ok=True)
    with open(payload_path, 'w', encoding='utf-8') as f:
        json.dump(oa_blocks, f, ensure_ascii=False)
    res = subprocess.run(
        ['node', os.path.join(root_dir, 'scripts', 'igcse_maths_verify_katex.mjs')],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, encoding='utf-8',
    )
    if os.path.exists(payload_path):
        os.remove(payload_path)
    assert res.returncode == 0, f'optionAnalysis KaTeX failed:\n{res.stdout}\n{res.stderr}'

    print(f'[PASS] {TEST_CODE} — 44/44 Math questions verified, 0 errors!')
    for mk in ('module1', 'module2_hard'):
        qs = TEST_DATA[mk]['questions']
        mcq_qs = [q for q in qs if q['questionFormat'] == 'mcq']
        spr_qs = [q for q in qs if q['questionFormat'] == 'spr']
        dist = {c: sum(1 for q in mcq_qs if q['correctAnswer'] == c) for c in 'ABCD'}
        doms = {}
        for q in qs:
            doms[q['domain']] = doms.get(q['domain'], 0) + 1
        print(f'       {mk:13s}: {len(qs)} Qs ({len(mcq_qs)} MCQ + {len(spr_qs)} SPR) | MCQ Keys={dist} | Domains={doms}')


if __name__ == '__main__':
    verify_all_math()
