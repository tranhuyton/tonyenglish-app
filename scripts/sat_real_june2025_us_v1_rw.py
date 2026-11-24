# -*- coding: utf-8 -*-
"""
Digital SAT 1500+ Real Past Exams — June 2025 US Ver 1 Reading & Writing (54 Qs)
- Module 1: 27 verbatim questions (32 min)
- Module 2: 27 verbatim questions (32 min) — assigned to both module2_hard & module2_lower (routingThreshold: 0)

All underlines, tables, line graphs, and diacritics have been visually verified against
the clean watermark-stripped exam strips and high-resolution source pages, and all 54
answer keys have passed an independent 2-pass audit.
"""

import copy
import json
import os
import re
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

_OCR_P40_42 = {
    r['page']: r
    for r in json.load(
        open(
            os.path.join(os.path.dirname(os.path.abspath(__file__)), 'ocr_data', 'june_us_v1_p40_42_raw.json'),
            encoding='utf-8',
        )
    )
}


def _ocr_opts(pno, fixes=()):
    opts = []
    for o in _OCR_P40_42[pno]['options']:
        s = re.sub(r'\s+', ' ', o).strip()
        for old, new in fixes:
            s = s.replace(old, new)
        opts.append(s)
    return opts


def _ocr_para(pno, start_marker, fixes=()):
    raw = _OCR_P40_42[pno]['left']
    idx = raw.find(start_marker)
    txt = raw[idx:] if idx >= 0 else raw
    txt = re.sub(r'\n+Tee\s*$', '', txt).strip()
    txt = re.sub(r'\s+', ' ', txt).strip()
    for old, new in fixes:
        txt = txt.replace(old, new)
    return f'<p>{txt}</p>'

TEST_CODE = 'real_june2025_us_v1_rw'
FOLDER_KEY = 'real_rw'
ORDER_INDEX = 3
TEST_TITLE = '🏛️ Real Exam — June 2025 US Ver 1 Reading & Writing (54 Qs)'


def _q(qid, num, domain, skill, diff, stim, stem, opts, ans, summary_vi, takeaway, analysis):
    """Builds a Bluebook-schema SAT R&W multiple-choice question object."""
    labels = ['A', 'B', 'C', 'D']
    return {
        'id': qid,
        'number': num,
        'domain': domain,
        'skill': skill,
        'difficulty': diff,
        'questionFormat': 'mcq',
        'stimulusHtml': stim,
        'questionHtml': stem,
        'options': [{'label': labels[i], 'text': opts[i]} for i in range(4)],
        'correctAnswer': ans,
        'explanation': {
            'summaryVi': summary_vi,
            'keyTakeaway': takeaway,
            'optionAnalysis': {
                labels[i]: {
                    'status': 'correct' if labels[i] == ans else 'trap',
                    'trapTag': analysis[i][0],
                    'reasonVi': analysis[i][1],
                }
                for i in range(4)
            },
        },
    }


def _html_table(caption, headers, rows):
    """Builds a clean, College Board Bluebook-style HTML data table."""
    ths = ''.join(f'<th>{h}</th>' for h in headers)
    trs = ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>' for r in rows)
    return (
        f'<div style="margin-bottom:12px;">'
        f'<div style="font-family:\'Segoe UI\',sans-serif;font-size:13px;font-weight:800;'
        f'color:#0f172a;text-align:center;margin-bottom:6px;">{caption}</div>'
        f'<table><thead><tr>{ths}</tr></thead><tbody>{trs}</tbody></table></div>'
    )


def _svg_m1_q11_submissions():
    """Recreates the exact June 2025 US Ver 1 M1 Q11 line graph (Science Research Submissions, 2016–2019)."""
    years = [2016, 2017, 2018, 2019]
    bio_vals = [200, 300, 280, 280]
    phys_vals = [95, 90, 88, 98]
    med_vals = [220, 220, 225, 285]
    anim_vals = [50, 50, 50, 90]

    xs = [115, 210, 305, 400]
    x_left, x_right = 80, 445
    y_top, y_bot = 18, 200  # 182px height for 0..350 -> 0.52 px per unit

    def fy(v):
        return y_bot - v * 0.52

    parts = []
    for val in range(0, 351, 50):
        y = fy(val)
        stroke = '#334155' if val == 0 else '#cbd5e1'
        sw = '1.5' if val == 0 else '1'
        parts.append(f'<line x1="{x_left}" y1="{y:.1f}" x2="{x_right}" y2="{y:.1f}" stroke="{stroke}" stroke-width="{sw}"/>')
        parts.append(f'<text x="{x_left - 8}" y="{y + 3.5:.1f}" font-size="10.5" text-anchor="end" fill="#1e293b" font-family="sans-serif">{val}</text>')

    for x, yr in zip(xs, years):
        parts.append(f'<line x1="{x}" y1="{y_top}" x2="{x}" y2="{y_bot}" stroke="#cbd5e1" stroke-width="1"/>')
        parts.append(f'<line x1="{x}" y1="{y_bot}" x2="{x}" y2="{y_bot + 5}" stroke="#334155" stroke-width="1.2"/>')
        parts.append(f'<text x="{x}" y="{y_bot + 18}" font-size="11" text-anchor="middle" fill="#1e293b" font-family="sans-serif">{yr}</text>')

    parts.append(f'<line x1="{x_left}" y1="{y_top}" x2="{x_left}" y2="{y_bot}" stroke="#334155" stroke-width="1.5"/>')

    # 1. cellular and molecular biology (solid black, filled black triangle)
    pts = ' '.join(f'{x},{fy(v):.1f}' for x, v in zip(xs, bio_vals))
    parts.append(f'<polyline points="{pts}" fill="none" stroke="#0f172a" stroke-width="2.2"/>')
    for x, v in zip(xs, bio_vals):
        y = fy(v)
        parts.append(f'<polygon points="{x},{y - 5.5:.1f} {x - 5},{y + 4:.1f} {x + 5},{y + 4:.1f}" fill="#0f172a"/>')

    # 2. physics and space science (dashed black, gray square)
    pts = ' '.join(f'{x},{fy(v):.1f}' for x, v in zip(xs, phys_vals))
    parts.append(f'<polyline points="{pts}" fill="none" stroke="#1e293b" stroke-width="2" stroke-dasharray="6,4"/>')
    for x, v in zip(xs, phys_vals):
        y = fy(v)
        parts.append(f'<rect x="{x - 4.2:.1f}" y="{y - 4.2:.1f}" width="8.4" height="8.4" fill="#cbd5e1" stroke="#0f172a" stroke-width="1.5"/>')

    # 3. medicine and health (dotted black, white circle)
    pts = ' '.join(f'{x},{fy(v):.1f}' for x, v in zip(xs, med_vals))
    parts.append(f'<polyline points="{pts}" fill="none" stroke="#0f172a" stroke-width="2" stroke-dasharray="2,3"/>')
    for x, v in zip(xs, med_vals):
        y = fy(v)
        parts.append(f'<circle cx="{x}" cy="{y:.1f}" r="4.5" fill="#ffffff" stroke="#0f172a" stroke-width="1.6"/>')

    # 4. animal science (solid gray, 4-point star)
    pts = ' '.join(f'{x},{fy(v):.1f}' for x, v in zip(xs, anim_vals))
    parts.append(f'<polyline points="{pts}" fill="none" stroke="#94a3b8" stroke-width="2.2"/>')
    for x, v in zip(xs, anim_vals):
        y = fy(v)
        star = (
            f'{x},{y - 6.5:.1f} {x + 2},{y - 2:.1f} {x + 6.5},{y:.1f} {x + 2},{y + 2:.1f} '
            f'{x},{y + 6.5:.1f} {x - 2},{y + 2:.1f} {x - 6.5},{y:.1f} {x - 2},{y - 2:.1f}'
        )
        parts.append(f'<polygon points="{star}" fill="#94a3b8" stroke="#0f172a" stroke-width="1.1"/>')

    # Axis titles
    parts.append(
        '<text x="24" y="109" font-size="11.5" font-weight="600" text-anchor="middle" fill="#0f172a" '
        'font-family="sans-serif" transform="rotate(-90 24 109)">Number of submissions</text>'
    )
    parts.append(
        '<text x="262" y="236" font-size="11.5" font-weight="600" text-anchor="middle" fill="#0f172a" '
        'font-family="sans-serif">Year</text>'
    )

    # Legend box
    parts.append('<rect x="108" y="248" width="290" height="84" fill="#ffffff" stroke="#475569" stroke-width="1.1"/>')
    # Legend row 1
    parts.append('<line x1="120" y1="264" x2="168" y2="264" stroke="#0f172a" stroke-width="2.2"/>')
    parts.append('<polygon points="144,258.5 139,268 149,268" fill="#0f172a"/>')
    parts.append('<text x="178" y="268" font-size="11.5" fill="#0f172a" font-family="sans-serif">cellular and molecular biology</text>')
    # Legend row 2
    parts.append('<line x1="120" y1="283" x2="168" y2="283" stroke="#1e293b" stroke-width="2" stroke-dasharray="6,4"/>')
    parts.append('<rect x="139.8" y="278.8" width="8.4" height="8.4" fill="#cbd5e1" stroke="#0f172a" stroke-width="1.5"/>')
    parts.append('<text x="178" y="287" font-size="11.5" fill="#0f172a" font-family="sans-serif">physics and space science</text>')
    # Legend row 3
    parts.append('<line x1="120" y1="302" x2="168" y2="302" stroke="#0f172a" stroke-width="2" stroke-dasharray="2,3"/>')
    parts.append('<circle cx="144" cy="302" r="4.5" fill="#ffffff" stroke="#0f172a" stroke-width="1.6"/>')
    parts.append('<text x="178" y="306" font-size="11.5" fill="#0f172a" font-family="sans-serif">medicine and health</text>')
    # Legend row 4
    parts.append('<line x1="120" y1="321" x2="168" y2="321" stroke="#94a3b8" stroke-width="2.2"/>')
    parts.append('<polygon points="144,314.5 146,319 150.5,321 146,323 144,327.5 142,323 137.5,321 142,319" fill="#94a3b8" stroke="#0f172a" stroke-width="1.1"/>')
    parts.append('<text x="178" y="325" font-size="11.5" fill="#0f172a" font-family="sans-serif">animal science</text>')

    return (
        '<div style="background:#f8fafc;border:1px solid #cbd5e1;border-radius:10px;padding:12px 14px;margin-bottom:12px;">'
        '<div style="font-family:\'Segoe UI\',sans-serif;font-size:13px;font-weight:800;color:#0f172a;'
        'text-align:center;line-height:1.35;margin-bottom:6px;">'
        'Total Science Research Submissions by Topic, 2016–2019</div>'
        '<svg viewBox="0 0 475 342" xmlns="http://www.w3.org/2000/svg" style="max-width:475px;">'
        '<rect x="0" y="0" width="475" height="342" fill="#ffffff"/>'
        f'{"".join(parts)}'
        '</svg></div>'
    )


def _svg_m1_q13_forest():
    """Recreates the exact June 2025 US Ver 1 M1 Q13 line graph (Chorotega Region Forest Patch Size, 1960–2000)."""
    years = [1960, 1979, 1986, 2000]
    c8_vals = [127, 125, 37, 61]
    c6_vals = [67, 77, 20, 35]
    c7_vals = [76, 87, 27, 49]

    xs = [120, 210, 300, 390]
    x_left, x_right = 80, 440
    y_top, y_bot = 18, 198  # 180px height for 0..150 -> 1.2 px per unit

    def fy(v):
        return y_bot - v * 1.2

    parts = []
    for val in range(0, 151, 25):
        y = fy(val)
        stroke = '#334155' if val == 0 else '#cbd5e1'
        sw = '1.5' if val == 0 else '1'
        parts.append(f'<line x1="{x_left}" y1="{y:.1f}" x2="{x_right}" y2="{y:.1f}" stroke="{stroke}" stroke-width="{sw}"/>')
        parts.append(f'<text x="{x_left - 8}" y="{y + 3.5:.1f}" font-size="10.5" text-anchor="end" fill="#1e293b" font-family="sans-serif">{val}</text>')

    for x, yr in zip(xs, years):
        parts.append(f'<line x1="{x}" y1="{y_top}" x2="{x}" y2="{y_bot}" stroke="#cbd5e1" stroke-width="1"/>')
        parts.append(f'<line x1="{x}" y1="{y_bot}" x2="{x}" y2="{y_bot + 5}" stroke="#334155" stroke-width="1.2"/>')
        parts.append(f'<text x="{x}" y="{y_bot + 18}" font-size="11" text-anchor="middle" fill="#1e293b" font-family="sans-serif">{yr}</text>')

    parts.append(f'<line x1="{x_left}" y1="{y_top}" x2="{x_left}" y2="{y_bot}" stroke="#334155" stroke-width="1.5"/>')

    # Class VIII (solid black, black upward triangle)
    pts = ' '.join(f'{x},{fy(v):.1f}' for x, v in zip(xs, c8_vals))
    parts.append(f'<polyline points="{pts}" fill="none" stroke="#0f172a" stroke-width="2.2"/>')
    for x, v in zip(xs, c8_vals):
        y = fy(v)
        parts.append(f'<polygon points="{x},{y - 5.5:.1f} {x - 5},{y + 4:.1f} {x + 5},{y + 4:.1f}" fill="#0f172a"/>')

    # Class VI (dashed black, gray square)
    pts = ' '.join(f'{x},{fy(v):.1f}' for x, v in zip(xs, c6_vals))
    parts.append(f'<polyline points="{pts}" fill="none" stroke="#1e293b" stroke-width="2" stroke-dasharray="6,4"/>')
    for x, v in zip(xs, c6_vals):
        y = fy(v)
        parts.append(f'<rect x="{x - 4.2:.1f}" y="{y - 4.2:.1f}" width="8.4" height="8.4" fill="#cbd5e1" stroke="#0f172a" stroke-width="1.5"/>')

    # Class VII (dotted black, white circle)
    pts = ' '.join(f'{x},{fy(v):.1f}' for x, v in zip(xs, c7_vals))
    parts.append(f'<polyline points="{pts}" fill="none" stroke="#0f172a" stroke-width="2" stroke-dasharray="2,3"/>')
    for x, v in zip(xs, c7_vals):
        y = fy(v)
        parts.append(f'<circle cx="{x}" cy="{y:.1f}" r="4.5" fill="#ffffff" stroke="#0f172a" stroke-width="1.6"/>')

    # Axis titles
    parts.append(
        '<text x="24" y="108" font-size="11.5" font-weight="600" text-anchor="middle" fill="#0f172a" '
        'font-family="sans-serif" transform="rotate(-90 24 108)">Mean patch size (hectares)</text>'
    )
    parts.append(
        '<text x="260" y="234" font-size="11.5" font-weight="600" text-anchor="middle" fill="#0f172a" '
        'font-family="sans-serif">Year</text>'
    )

    # Legend box (3 items matching original layout)
    parts.append('<rect x="72" y="246" width="356" height="92" fill="#ffffff" stroke="#475569" stroke-width="1.1"/>')
    # Row 1: Class VIII
    parts.append('<line x1="84" y1="264" x2="130" y2="264" stroke="#0f172a" stroke-width="2.2"/>')
    parts.append('<polygon points="107,258.5 102,268 112,268" fill="#0f172a"/>')
    parts.append('<text x="140" y="268" font-size="11" fill="#0f172a" font-family="sans-serif">Class VIII (cannot be used for commercial crops)</text>')
    # Row 2: Class VI
    parts.append('<line x1="84" y1="292" x2="130" y2="292" stroke="#1e293b" stroke-width="2" stroke-dasharray="6,4"/>')
    parts.append('<rect x="102.8" y="287.8" width="8.4" height="8.4" fill="#cbd5e1" stroke="#0f172a" stroke-width="1.5"/>')
    parts.append('<text x="140" y="296" font-size="11" fill="#0f172a" font-family="sans-serif">Class VI (severe limitations on use for crops)</text>')
    # Row 3: Class VII
    parts.append('<line x1="84" y1="320" x2="130" y2="320" stroke="#0f172a" stroke-width="2" stroke-dasharray="2,3"/>')
    parts.append('<circle cx="107" cy="320" r="4.5" fill="#ffffff" stroke="#0f172a" stroke-width="1.6"/>')
    parts.append('<text x="140" y="324" font-size="11" fill="#0f172a" font-family="sans-serif">Class VII (very severe limitations on use for crops)</text>')

    return (
        '<div style="background:#f8fafc;border:1px solid #cbd5e1;border-radius:10px;padding:12px 14px;margin-bottom:12px;">'
        '<div style="font-family:\'Segoe UI\',sans-serif;font-size:13px;font-weight:800;color:#0f172a;'
        'text-align:center;line-height:1.35;margin-bottom:6px;">'
        'Annual Mean Forest Patch Size for Three Land Use Capability Classes in the Chorotega Region, Costa Rica</div>'
        '<svg viewBox="0 0 475 348" xmlns="http://www.w3.org/2000/svg" style="max-width:475px;">'
        '<rect x="0" y="0" width="475" height="348" fill="#ffffff"/>'
        f'{"".join(parts)}'
        '</svg></div>'
    )


# ============================================================================
# MODULE 1 — ROUTING MODULE (27 Qs — June 2025 US Ver 1)
# ============================================================================

def get_m1_questions():
    return [
        _q(
            'june2025_us_v1_rw_m1_q1', 1, 'Craft and Structure', 'Words in Context', 'Easy',
            '<p><i>Dragon against Tiger</i> is an important work of <i>Nihonga</i>, or classical Japanese painting. Unlike Wada Eisaku, who adopted traditional European methods such as painting with oil on canvas, Hashimoto Gahō _______ traditional Japanese approaches. For instance, Hashimoto produced <i>Dragon against Tiger</i> by applying color pigments to a silk surface.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            ['overlooked', 'distrusted', 'embraced', 'released'],
            'C',
            'Tín hiệu đối lập “Unlike Wada Eisaku, who adopted traditional European methods...” cho thấy Hashimoto Gahō đi theo hướng ngược lại: đón nhận và áp dụng các phương pháp hội họa truyền thống Nhật Bản (bằng chứng ngay sau “For instance”: ông vẽ bột màu lên bề mặt lụa). Do đó từ chính xác là “embraced” (đón nhận/theo đuổi nhiệt thành) → Chọn C.',
            'Cấu trúc đối lập `Unlike A (adopted European), B (_______ Japanese)` + ví dụ cụ thể khẳng định B dùng kỹ thuật truyền thống Nhật → chọn từ mang nghĩa đón nhận (“embraced”).',
            [
                ('Opposite Meaning', 'overlooked = bỏ qua, phớt lờ — trái ngược hoàn toàn với ví dụ vẽ màu lên lụa kiểu truyền thống Nhật.'),
                ('Opposite Meaning', 'distrusted = không tin tưởng — mâu thuẫn với việc ông trực tiếp dùng phương pháp truyền thống Nhật.'),
                ('Đáp án đúng', 'embraced = đón nhận, áp dụng — tương phản chuẩn xác với việc Wada Eisaku chọn kỹ thuật châu Âu.'),
                ('Wrong Meaning', 'released = phát hành, thả ra — không hợp ngữ cảnh áp dụng phương pháp nghệ thuật.'),
            ],
        ),
        _q(
            'june2025_us_v1_rw_m1_q2', 2, 'Craft and Structure', 'Words in Context', 'Easy',
            '<p>The following text is from Kenneth Grahame’s 1908 novel <i>The Wind in the Willows</i>. The Mole is returning home after a visit to Mr. Badger’s house.</p><p style="padding-left:16px;">As he hurried along, eagerly <u>anticipating</u> the moment when he would be at home again among the things he knew and liked, the Mole saw clearly that he was an animal of tilled field and hedge-row, linked to the ploughed furrow, the frequented pasture, the lane of evening lingerings, the cultivated garden-plot.</p>',
            'As used in the text, what does the word “anticipating” most nearly mean?',
            ['Describing', 'Getting ahead of', 'Looking forward to', 'Instructing'],
            'C',
            'Ngữ cảnh: Chuột Chũi vội vã trở về nhà, háo hức (“eagerly”) chờ đợi khoảnh khắc được ở nhà bên những thứ thân quen và yêu thích (“the things he knew and liked”). Vì vậy “anticipating” mang nghĩa mong chờ, trông đợi háo hức = “Looking forward to” → Chọn C.',
            'Trạng từ “eagerly” (háo hức) đi kèm khoảnh khắc tích cực (“at home again among the things he knew and liked”) khóa chặt nghĩa “Looking forward to”.',
            [
                ('Wrong Meaning', 'Describing = mô tả — không hợp với trạng thái háo hức chờ đợi một khoảnh khắc sắp tới.'),
                ('Secondary Meaning Trap', 'Getting ahead of = đi trước/đón đầu (nghĩa khác của anticipate) — không khớp ngữ cảnh háo hức mong về nhà.'),
                ('Đáp án đúng', 'Looking forward to = mong chờ, trông đợi — khớp hoàn hảo với “eagerly” và niềm vui sắp trở về nhà.'),
                ('Wrong Meaning', 'Instructing = hướng dẫn, chỉ dạy — hoàn toàn lệch nghĩa.'),
            ],
        ),
        _q(
            'june2025_us_v1_rw_m1_q3', 3, 'Standard English Conventions', 'Boundaries', 'Easy',
            '<p>The human body has three types of muscle _______ cardiac, and skeletal. The levator anguli oris is a skeletal muscle—of which the body contains more than six hundred—and it helps with raising the corners of the mouth.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['tissue and smooth,', 'tissue: smooth,', 'tissue smooth,', 'tissue. Smooth'],
            'B',
            'Mệnh đề phía trước “The human body has three types of muscle tissue” là một mệnh đề độc lập hoàn chỉnh, giới thiệu danh sách liệt kê 3 loại mô cơ (“smooth, cardiac, and skeletal”). Theo quy tắc dấu câu chuẩn SAT, dùng dấu hai chấm (`:`) sau mệnh đề độc lập để mở ra danh sách giải thích/liệt kê → “tissue: smooth,” → Chọn B.',
            'Gặp cấu trúc `[Mệnh đề độc lập nêu tổng số lượng: three types of X] : [liệt kê A, B, and C]` → dùng dấu hai chấm (`:`).',
            [
                ('Illogical Coordination', 'Chèn “and” khiến “muscle tissue” bị liệt kê ngang hàng với “smooth, cardiac, and skeletal” thành 4 mục phi lý.'),
                ('Đáp án đúng', 'Dấu hai chấm đặt sau mệnh đề độc lập hoàn chỉnh mở ra danh sách chính xác gồm 3 loại: smooth, cardiac, and skeletal.'),
                ('Missing Punctuation', 'Thiếu dấu câu ngăn cách giữa danh từ “muscle tissue” và danh sách liệt kê phía sau.'),
                ('Sentence Fragment', 'Tách bằng dấu chấm khiến phần sau “Smooth cardiac, and skeletal.” trở thành cụm từ cụt thiếu động từ (fragment).'),
            ],
        ),
        _q(
            'june2025_us_v1_rw_m1_q4', 4, 'Craft and Structure', 'Words in Context', 'Medium',
            '<p>The Fly River delta is a remarkably _______ landscape: it is a constantly evolving network of channels and strips of land that change in size and shape as the river deposits new sedimentary particles where the river meets the waters of the Gulf of Papua.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            ['mutable', 'habitable', 'secluded', 'homogeneous'],
            'A',
            'Phần định nghĩa ngay sau dấu hai chấm giải thích trực tiếp cho chỗ trống: “constantly evolving” (không ngừng biến đổi) và “change in size and shape” (thay đổi kích thước và hình dạng). Tính từ mang nghĩa hay thay đổi, dễ biến đổi là “mutable” → Chọn A.',
            'Dấu hai chấm (`:`) là “từ điển trực tiếp” của câu Words in Context: `constantly evolving + change in size and shape` = `mutable`.',
            [
                ('Đáp án đúng', 'mutable = có thể/thường xuyên biến đổi — khớp tuyệt đối với “constantly evolving” và “change in size and shape”.'),
                ('Unsupported Meaning', 'habitable = có thể sinh sống được — đoạn văn không đề cập đến con người hay sinh vật cư trú.'),
                ('Unsupported Meaning', 'secluded = hẻo lánh, biệt lập — không liên quan đến quá trình bồi đắp thay đổi hình dạng.'),
                ('Opposite Meaning', 'homogeneous = đồng nhất — trái ngược với mạng lưới kênh rạch và dải đất liên tục thay đổi.'),
            ],
        ),
        _q(
            'june2025_us_v1_rw_m1_q5', 5, 'Craft and Structure', 'Text Structure and Purpose', 'Easy',
            '<p>Benjamin Prud’homme and colleagues have explored how convergent evolution—<u>a phenomenon that occurs when the same trait evolves independently in two reproductively separate lineages</u>—can result from a genetic mechanism shared by both lineages. Meanwhile, Patricia J. Wittkopp and colleagues have investigated how convergence occurs through different genetic mechanisms, but the relative prevalence of convergence through shared and different genetic processes is still poorly understood. This motivated biologists Delbert A. Green II and Cassandra G. Extavour to evaluate both types of convergence in a single study for their 2012 paper.</p>',
            'Which choice best states the function of the underlined portion in the text as a whole?',
            [
                'It provides examples of how a phenomenon was studied by scientists in the field before Green and Extavour’s study.',
                'It gives a basic description of a phenomenon that is central to the discussion that follows.',
                'It clarifies a concept that the author implies was unclear in the studies mentioned in the text.',
                'It introduces a method of scientific analysis that is discussed in greater detail later in the text.',
            ],
            'B',
            'Phần gạch chân nằm giữa cặp dấu gạch ngang dài (`—...—`) đóng vai trò định nghĩa ngắn gọn khái niệm “convergent evolution” (tiến hóa hội tụ — hiện tượng cùng một đặc điểm tiến hóa độc lập ở hai nhánh tách biệt về mặt sinh sản). Toàn bộ đoạn văn sau đó xoay quanh chính hiện tượng tiến hóa hội tụ này (nghiên cứu của Prud’homme, Wittkopp, và Green & Extavour) → Chọn B.',
            'Cụm đồng vị ngữ kẹp giữa 2 dấu gạch ngang (`X—a phenomenon that...—`) ngay câu 1 gần như luôn có chức năng định nghĩa/mô tả cơ bản hiện tượng trung tâm của đoạn văn.',
            [
                ('Misattributed Role', 'Phần gạch chân chỉ định nghĩa “convergent evolution”, không đưa ra ví dụ về các nghiên cứu trước đó.'),
                ('Đáp án đúng', 'Cung cấp mô tả/định nghĩa cơ bản cho hiện tượng trung tâm (“convergent evolution”) xuyên suốt phần thảo luận tiếp theo.'),
                ('Unsupported Inference', 'Tác giả không hề ngụ ý khái niệm tiến hóa hội tụ chưa rõ ràng trong các nghiên cứu; điều chưa rõ là tỷ lệ tương đối của hai cơ chế.'),
                ('Wrong Category', 'Đây là mô tả một hiện tượng sinh học, không phải một phương pháp phân tích khoa học.'),
            ],
        ),
        _q(
            'june2025_us_v1_rw_m1_q6', 6, 'Craft and Structure', 'Text Structure and Purpose', 'Easy',
            '<p>In what is now Washington state, the Tulalip Tribes operate the Hibulb Cultural Center. Relying on traditional knowledge to guide the design of exhibits, this institution presents Tulalip history and culture to the tribes’ citizens. The Turtle Mountain Band of Chippewa, a tribe in North Dakota, employs a similar strategy in its own cultural center. Both centers contrast with museums that aren’t Indigenous-led; when displaying Indigenous artifacts, such museums tend to anticipate mainly non-Indigenous audiences and rely on Euro-centric strategies for designing exhibits.</p>',
            'Which choice best describes the overall structure of the text?',
            [
                'It describes how tribal cultural centers designed exhibits of a particular set of artifacts, then analyzes how non-Indigenous institutions designed exhibits of the same artifacts.',
                'It examines how tribal citizens respond to exhibits at tribal cultural centers, then speculates how non-Indigenous audiences would respond to the same exhibits.',
                'It discusses two cultural centers operated by tribes, then compares them with non-Indigenous institutions that present Indigenous exhibits.',
                'It outlines an early strategy for exhibit design used by one tribal cultural center, then explains a newer strategy used by a different tribal cultural center.',
            ],
            'C',
            'Bố cục đoạn văn chia làm 2 phần rõ rệt: (1) Câu 1–3 giới thiệu hai trung tâm văn hóa do các bộ tộc điều hành (Hibulb Cultural Center của Tulalip Tribes và trung tâm của Turtle Mountain Band of Chippewa); (2) Câu 4 đối chiếu (“Both centers contrast with...”) hai trung tâm này với các bảo tàng không do người bản địa lãnh đạo khi trưng bày hiện vật bản địa → Chọn C.',
            'Tách đoạn theo từng câu chuyển ý: `[Trung tâm bộ tộc 1 + Trung tâm bộ tộc 2] → [Both centers contrast with non-Indigenous museums]`.',
            [
                ('False Detail', 'Đoạn văn không hề nói cả hai loại bảo tàng trưng bày “cùng một bộ hiện vật” (“the same artifacts”).'),
                ('Unsupported Content', 'Đoạn văn không phân tích hay suy đoán phản ứng của khán giả đối với triển lãm.'),
                ('Đáp án đúng', 'Khớp chính xác cấu trúc 2 chặng: thảo luận 2 trung tâm văn hóa của các bộ tộc, rồi so sánh với các cơ sở không do người bản địa điều hành.'),
                ('Contradicts Text', 'Hai trung tâm bộ tộc áp dụng chiến lược TƯƠNG TỰ (“a similar strategy”), không phải chiến lược cũ và chiến lược mới hơn.'),
            ],
        ),
        _q(
            'june2025_us_v1_rw_m1_q7', 7, 'Craft and Structure', 'Cross-Text Connections', 'Medium',
            '<p><b>Text 1</b></p><p>Uisdean Nicholson and his team have discovered evidence in seismic data of a 40-kilometer-wide subsurface crater beneath nearly a kilometer of water off the coast of West Africa that is consistent with a 400-meter-wide asteroid striking the seafloor. This structure, which the team named Nadir, exhibits all the telltale signs of a high-velocity impact crater: an elevated rim, a circular shape, a terraced floor, and a pronounced area of uplift at its center.</p><p><b>Text 2</b></p><p>Both carbonate dissolution and subsurface salt withdrawal can cause craterlike depressions without the need for a high-velocity impact. However, carbonate dissolution is very unlikely to have occurred in the vicinity of Nadir, and although subsurface salt withdrawal could have plausibly occurred in this area and would result in a depression with a terraced floor or a circular shape, it would not exhibit the area of central uplift seen at Nadir.</p>',
            'Which choice best describes a difference between the approach of Text 1 and the approach of Text 2?',
            [
                'Text 1 dispassionately describes Nicholson and colleagues’ findings and conclusions, whereas Text 2 attempts to convey the researchers’ excitement on discovering Nadir.',
                'Text 1 focuses on features Nadir lacks, whereas Text 2 indicates features it shares with other geological depressions.',
                'Text 1 discusses a single plausible cause of Nadir, whereas Text 2 evaluates two possible causes.',
                'Text 1 emphasizes the evidence supporting an asteroid impact as the cause of Nadir, whereas Text 2 argues against that explanation.',
            ],
            'C',
            'Text 1 chỉ trình bày MỘT nguyên nhân khả dĩ tạo ra miệng hố Nadir (va chạm tiểu hành tinh rộng 400 mét). Trong khi đó, Text 2 đánh giá HAI nguyên nhân thay thế có thể gây ra hố trũng giống miệng hố (hòa tan cacbonat và rút muối dưới lòng đất — và nhận định cả hai đều không thể giải thích trọn vẹn Nadir, đặc biệt là vùng nâng ở tâm). Do đó Text 2 KHÔNG hề bác bỏ giả thuyết tiểu hành tinh (bẫy D!), mà đánh giá hai nguyên nhân thay thế → Chọn C.',
            'Cảnh giác bẫy D: đọc kỹ từ “However” ở Text 2 — Text 2 thực ra LOẠI TRỪ cả 2 cơ chế không do va chạm chứ không phản bác giả thuyết tiểu hành tinh ở Text 1!',
            [
                ('Wrong Tone', 'Text 2 giữ giọng khoa học khách quan, không hề miêu tả sự phấn khích của các nhà nghiên cứu.'),
                ('Reverses Text 1', 'Text 1 liệt kê các đặc điểm Nadir CÓ (“exhibits all the telltale signs”), không phải đặc điểm nó thiếu.'),
                ('Đáp án đúng', 'Khớp chính xác cách tiếp cận: Text 1 bàn một nguyên nhân khả dĩ (va chạm tiểu hành tinh); Text 2 đánh giá hai nguyên nhân có thể khác (carbonate dissolution và subsurface salt withdrawal).'),
                ('Misreads Text 2', 'Text 2 không hề phản bác giả thuyết tiểu hành tinh; trái lại, nó bác bỏ 2 cơ chế phi va chạm vì không tạo ra vùng nâng trung tâm ở Nadir.'),
            ],
        ),
        _q(
            'june2025_us_v1_rw_m1_q8', 8, 'Information and Ideas', 'Central Ideas and Details', 'Easy',
            '<p>“Cocoa” is an example of a loanword—that is, a word that originated in one language and was later adopted by another. The word came to English indirectly from <i>cacao</i>, the Spanish word for the plant that chocolate is made from. Spanish had borrowed it from Nahuatl, an Indigenous language of Central Mexico, in which the word’s original form is <i>cacahuatl</i>. “Puma” is also Indigenous in origin and entered English through Spanish. But in this case, the original source was Quechua, a language of South America, in which the word for the mountain lion is also <i>puma</i>.</p>',
            'The author makes which point about the Spanish language?',
            [
                'It has served as a medium through which Indigenous languages have influenced English.',
                'Its contribution to English vocabulary roughly equals the collective contribution by Indigenous languages.',
                'It adopted Nahuatl and Quechua words in approximately equal numbers.',
                'It has borrowed words from Indigenous languages and contributed words to them.',
            ],
            'A',
            'Cả hai ví dụ trong đoạn (“cocoa” đi từ tiếng Nahuatl → Tây Ban Nha → tiếng Anh; và “puma” đi từ tiếng Quechua → Tây Ban Nha → tiếng Anh) đều cho thấy tiếng Tây Ban Nha đóng vai trò cầu nối/trung gian (“a medium”) đưa từ vựng của các ngôn ngữ bản địa vào tiếng Anh → Chọn A.',
            'Theo dõi dòng chảy ngôn ngữ trong cả 2 ví dụ: `Indigenous (Nahuatl / Quechua) → Spanish → English` = Spanish là “medium” (kênh trung gian).',
            [
                ('Đáp án đúng', 'Khái quát đúng vai trò trung gian của tiếng Tây Ban Nha trong việc truyền các từ mượn bản địa (“cocoa”, “puma”) sang tiếng Anh.'),
                ('Unsupported Comparison', 'Đoạn văn không so sánh số lượng từ tiếng Tây Ban Nha đóng góp với tổng số từ ngôn ngữ bản địa đóng góp.'),
                ('Unsupported Comparison', 'Chỉ đưa 1 ví dụ mỗi ngôn ngữ (1 từ Nahuatl, 1 từ Quechua), không hề nói số lượng vay mượn xấp xỉ nhau.'),
                ('Half-True Trap', 'Đúng là tiếng Tây Ban Nha vay từ ngôn ngữ bản địa, nhưng đoạn văn không nhắc đến chiều ngược lại (đóng góp từ cho các ngôn ngữ bản địa).'),
            ],
        ),
        _q(
            'june2025_us_v1_rw_m1_q9', 9, 'Information and Ideas', 'Central Ideas and Details', 'Medium',
            '<p>Motivated to sell as many paintings as possible, Alfred Hair, an influential figure among the landscape artists known as the Florida Highwaymen, pioneered “fast painting,” which in part involved working across multiple canvasses at once. That many of Hair’s acolytes, including Isaac Knight, imitated the technique accounts in part for the impressionistic qualities that are now synonymous with the group’s shared aesthetic. But not all Highwaymen fully embraced this approach; for instance, though Willie Reagan was also prolific, his paintings were executed with greater attention to detail.</p>',
            'What does the text most strongly suggest about paintings by Knight?',
            [
                'Because of the manner in which they were created, they likely have visual qualities that are regarded as more typical of Florida Highwaymen paintings than the qualities in works by Reagan are.',
                'Although it is evident that Knight adopted some of Hair’s preferred techniques, Knight’s works are less derivative of works by Hair than is typically acknowledged.',
                'The lack of precision with which they were executed suggests that they are inferior to works by either Hair or Reagan.',
                'Knight’s reliance on the technique of fast painting likely accounts for his works being more aesthetically interesting than works by Reagan are.',
            ],
            'A',
            'Chuỗi suy luận chặt chẽ từ văn bản: (1) Isaac Knight bắt chước kỹ thuật “fast painting” của Alfred Hair; (2) Chính kỹ thuật này tạo nên nét ấn tượng (“impressionistic qualities”) gắn liền với thẩm mỹ chung của nhóm Florida Highwaymen; (3) Ngược lại, Willie Reagan không hoàn toàn theo cách này mà vẽ tỉ mỉ chi tiết hơn. Suy ra tranh của Knight (nhờ cách vẽ nhanh) nhiều khả năng mang đặc trưng thị giác tiêu biểu cho nhóm Florida Highwaymen hơn tranh của Reagan → Chọn A.',
            'Loại ngay các phương án đưa ra phán xét giá trị chủ quan không có trong bài (“less derivative”, “inferior”, “more aesthetically interesting”).',
            [
                ('Đáp án đúng', 'Bám sát chuỗi nhân quả: Knight dùng “fast painting” → tạo đặc trưng ấn tượng tiêu biểu cho Florida Highwaymen hơn lối vẽ tỉ mỉ của Reagan.'),
                ('Unsupported Claim', 'Văn bản không hề bàn mức độ “ít bắt chước hơn so với người ta thường nghĩ” của tranh Knight.'),
                ('Extreme / Value Judgment', 'Không có chi tiết nào đánh giá tranh của Knight “kém chất lượng hơn” (“inferior”) tranh của Hair hay Reagan.'),
                ('Unsupported Value Judgment', 'Đoạn văn không so sánh tranh của ai “thú vị về mặt thẩm mỹ hơn” (“more aesthetically interesting”).'),
            ],
        ),
        _q(
            'june2025_us_v1_rw_m1_q10', 10, 'Information and Ideas', 'Central Ideas and Details', 'Easy',
            '<p>The following text is adapted from Daniel Defoe’s 1704 nonfiction book <i>The Storm</i>.</p><p>The sermon is a sound of words spoken to the ear, and prepared only for present meditation, and extends no farther than the strength of memory can convey it; a book printed is a record; remaining in every man’s possession, always ready to renew its acquaintance with his memory, and always ready to be produced as an authority or voucher to any reports he makes out of it, and conveys its contents for ages to come, to the eternity of mortal time, when the author is forgotten in his grave.</p>',
            'Which choice best states the main idea of the text?',
            [
                'Words committed to print have a greater permanence than messages that are merely spoken aloud.',
                'People are less likely to forget a message when they hear it spoken aloud than they are when they read it in print.',
                'Unless a spoken message is delivered by an expert, it can be safely ignored.',
                'Most authors have little hope of being remembered well past their lifetimes.',
            ],
            'A',
            'Tác giả đối lập trực tiếp giữa bài thuyết giáo nói miệng (“sermon... spoken to the ear” — chỉ tồn tại trong chốc lát và phụ thuộc vào trí nhớ mong manh) với sách in (“a book printed is a record” — tồn tại mãi trong tay người đọc, làm bằng chứng và truyền tải nội dung qua nhiều thời đại ngay cả khi tác giả đã khuất). Ý chính: lời văn được in ấn có tính trường tồn cao hơn nhiều so với lời nói thuần túy → Chọn A.',
            'Cấu trúc tương phản trung tâm `spoken sermon (limited to memory)` vs. `printed book (record for ages to come)` → chữ in bền vững hơn lời nói.',
            [
                ('Đáp án đúng', 'Nắm trọn phép đối chiếu cốt lõi: văn bản in ấn có độ bền vững/trường tồn vượt trội so với thông điệp chỉ nói ra miệng.'),
                ('Reverses Claim', 'Đảo ngược hoàn toàn ý tác giả: lời nói mới dễ bị quên theo trí nhớ, còn sách in luôn sẵn sàng nhắc lại trí nhớ.'),
                ('Unsupported Claim', 'Không có câu nào đề cập chuyên gia hay việc phớt lờ thông điệp nói miệng.'),
                ('Detail Trap', 'Cụm “when the author is forgotten in his grave” chỉ là chi tiết phụ để nhấn mạnh độ trường tồn của cuốn sách, không phải ý chính về số phận tác giả.'),
            ],
        ),
        _q(
            'june2025_us_v1_rw_m1_q11', 11, 'Information and Ideas', 'Command of Evidence: Quantitative', 'Easy',
            _svg_m1_q11_submissions() + '<p>A student is researching the trends in the topics submitted to a national science fair for high school students. The graph shows the number of submissions by topic that were made each year. Based on the data in the graph, the student claims that <u>there were more medicine and health research topics submitted in 2019 than in any other year.</u></p>',
            'Which choice most effectively uses data from the graph to support the underlined claim?',
            [
                'In 2016, the number of cellular and molecular biology topic submissions was the same as the number of animal science topic submissions.',
                'In 2019, there were more physics and space science topic submissions than there were medicine and health topic submissions.',
                'The lowest number of animal science topic submissions in a year was approximately 95 in 2016.',
                'The highest number of medicine and health topic submissions during the period shown is approximately 285 in 2019.',
            ],
            'D',
            'Nhận định gạch chân khẳng định: số đề tài “medicine and health” (đường chấm chấm, hình tròn trắng) nộp vào năm 2019 cao hơn mọi năm khác. Kiểm tra trên biểu đồ: đường tròn trắng đạt ~220 (2016), ~220 (2017), ~225 (2018) và vọt lên đỉnh ~285 vào năm 2019. Đáp án D vừa chính xác 100% theo số liệu vừa ủng hộ trực tiếp nhận định gạch chân → Chọn D.',
            'Với câu biểu đồ “support the underlined claim”, luôn kiểm tra 2 bước: (1) Đúng số liệu biểu đồ chưa? (2) Có nói đúng chủ đề & mốc thời gian của câu gạch chân (“medicine and health” + “2019”) không?',
            [
                ('False Data & Off-Topic', 'Sai biểu đồ (năm 2016: cellular ~200 còn animal science ~50) và không nhắc gì đến “medicine and health”.'),
                ('False Data', 'Ngược dữ liệu: năm 2019 physics chỉ ~98, thấp xa so với medicine and health (~285).'),
                ('False Data & Off-Topic', 'Sai biểu đồ (năm 2016 animal science là ~50, còn ~95 là physics) và lệch chủ đề.'),
                ('Đáp án đúng', 'Khớp cả số liệu (đỉnh ~285 năm 2019 trên đường chấm tròn trắng) lẫn khẳng định gạch chân về nhóm “medicine and health”.'),
            ],
        ),
        _q(
            'june2025_us_v1_rw_m1_q12', 12, 'Information and Ideas', 'Command of Evidence: Textual', 'Easy',
            '<p><i>Poems</i> is an 1895 collection of poetry by Frances E.W. Harper. In one of Harper’s poems, the speaker criticizes activists who champion humanitarian causes in other countries while overlooking local concerns, saying, _______</p>',
            'Which quotation from <i>Poems</i> most effectively illustrates the claim?',
            [
                '“Men may tread down the poor and lowly, / May crush them in anger and hate, / But surely the mills of God’s justice / Will grind out the grist of their fate.” (from “An Appeal to My Countrywomen”)',
                '“When ye plead for the wrecked and fallen, / The exile from far-distant shores, / Remember that men are still wasting / Life’s crimson around your own doors.” (from “An Appeal to My Countrywomen”)',
                '“God bless our native land, / Land of the newly free, / Oh may she ever stand / For truth and liberty.” (from “God Bless Our Native Land”)',
                '“Let me make the songs for the people, / Songs for the old and young; / Songs to stir like a battle-cry / Wherever they are sung.” (from “Songs for the People”)',
            ],
            'B',
            'Nhận định cần minh họa có 2 vế đối lập: (1) ủng hộ các mục tiêu nhân đạo ở nước ngoài (“champion humanitarian causes in other countries”) ↔ “plead for the wrecked and fallen, / The exile from far-distant shores”; (2) trong khi bỏ quên nỗi khổ ngay tại địa phương (“overlooking local concerns”) ↔ “Remember that men are still wasting / Life’s crimson around your own doors.” Chỉ đáp án B khớp trọn vẹn cả hai vế → Chọn B.',
            'Khớp hình ảnh ẩn dụ trong thơ với từng cụm từ khóa của Claim: `far-distant shores` = other countries; `around your own doors` = local concerns.',
            [
                ('Wrong Theme', 'Nói về sự trừng phạt công lý của Chúa dành cho kẻ áp bức người nghèo, không đối chiếu nước ngoài với địa phương.'),
                ('Đáp án đúng', 'Đối chiếu trực tiếp việc kêu gọi cho người lưu vong từ bờ biển xa xôi (“far-distant shores”) với nỗi đau đang diễn ra ngay trước cửa nhà (“around your own doors”).'),
                ('Wrong Theme', 'Lời cầu chúc yêu nước dành cho tự do và chân lý của quê hương, không phê phán các nhà hoạt động.'),
                ('Wrong Theme', 'Khát vọng sáng tác những bài ca truyền cảm hứng cho mọi tầng lớp nhân dân, không khớp Claim.'),
            ],
        ),
        _q(
            'june2025_us_v1_rw_m1_q13', 13, 'Information and Ideas', 'Command of Evidence: Quantitative', 'Medium',
            _svg_m1_q13_forest() + '<p>To understand the extent of deforestation in the Chorotega region of Costa Rica, Juan Pablo Arroyo-Mora and colleagues used historical aerial photography and remote sensing data to track changes in the annual mean size of forest patches across different land use capability classes (categories that indicate possible uses of forest land). Due to the Chorotega region’s accessibility, various types of forested areas were converted to cattle pasture as rising international meat prices drove a cattle ranching boom in the 1960s and 1970s. By the mid-1980s, however, increased public awareness and environmental reforms, along with a decline in meat prices, triggered a natural regrowth process, as evidenced by the _______</p>',
            'Which choice most effectively uses data from the graph to complete the assertion?',
            [
                'difference between mean forest patch size in Class VIII and in Class VI in 2000.',
                'steady increase in mean forest patch size from 1960 to 1979, followed by a more sudden increase in 1986 for all classes.',
                'increase in mean forest patch size after 1986 in all classes.',
                'similarity in mean forest patch size in Class VIII and Class VII in 1986.',
            ],
            'C',
            'Vế cần chứng minh ngay trước chỗ trống: từ giữa thập niên 1980 (“By the mid-1980s”), nhận thức cộng đồng, cải cách môi trường và giá thịt giảm đã kích hoạt quá trình tái sinh rừng tự nhiên (“triggered a natural regrowth process”). Trên biểu đồ, sau mốc 1986 đến năm 2000, kích thước mảnh rừng trung bình ở CẢ 3 NHÓM ĐẤT (Class VIII, VII và VI) đều tăng rõ rệt (VIII: ~37 → ~61 ha; VII: ~27 → ~49 ha; VI: ~20 → ~35 ha) → Chọn C.',
            'Bằng chứng cho “tái sinh rừng từ giữa thập niên 1980” phải là xu hướng TĂNG THEO THỜI GIAN sau mốc 1986 — loại ngay ảnh chụp đơn lẻ tại một năm (A, D) và dữ liệu sai chiều (B).',
            [
                ('Static Snapshot', 'Chênh lệch giữa hai nhóm đất trong riêng năm 2000 không chứng minh được quá trình rừng tái sinh theo thời gian.'),
                ('False Data', 'Sai hoàn toàn chiều biểu đồ: từ 1979 đến 1986 cả ba đường đều LAO DỐC mạnh (không phải tăng đột ngột), và Class VIII còn hơi giảm giai đoạn 1960–1979.'),
                ('Đáp án đúng', 'Khớp hoàn hảo biểu đồ (cả 3 đường đều đi lên từ 1986 đến 2000) và minh chứng trực tiếp cho quá trình rừng tự nhiên tái sinh sau giữa thập niên 1980.'),
                ('Static Snapshot', 'Mức gần nhau giữa Class VIII và Class VII tại riêng năm 1986 không thể hiện sự hồi phục/tái sinh rừng.'),
            ],
        ),
        _q(
            'june2025_us_v1_rw_m1_q14', 14, 'Information and Ideas', 'Command of Evidence: Textual', 'Medium',
            '<p>Veronica L. Bura, Akito Y. Kawahara, and Jayne E. Yack investigated the evolution and function of sound production in silk moth and hawk moth caterpillars. They found that during harmless simulated attacks on isolated caterpillars, 33% of the tested species produced sound, which ranged from clicks in <i>Actias luna</i> to whistles in <i>Rhodinia fugax</i>. Although some insects use sound to communicate with members of the same species, the researchers claim that the caterpillar sounds recorded in their study are directed primarily at predators.</p>',
            'Which finding, if true, would most directly support Bura and colleagues’ claim?',
            [
                'In most cases, the sound that a caterpillar species produced during simulated attacks was not produced by other caterpillar species during simulated attacks.',
                'Chickens and yellow warblers, two predators of caterpillars, have been observed to stop their attacks in response to caterpillar sounds.',
                'Each caterpillar species tended to produce one sound during simulated attacks, although individuals occasionally made a variety of other sounds during simulated attacks as well.',
                'Caterpillar clicks were emitted in a frequency detectable by birds that prey on caterpillars, but caterpillar whistles were not.',
            ],
            'B',
            'Luận điểm của nhóm nghiên cứu: âm thanh mà sâu bướm phát ra trong thí nghiệm chủ yếu nhắm tới KẺ SĂN MỒI (“directed primarily at predators”), không phải để giao tiếp cùng loài. Đáp án B cung cấp bằng chứng trực tiếp nhất: hai loài săn sâu bướm là gà và chim chích vàng được quan sát thấy NGỪNG TẤN CÔNG khi nghe âm thanh của sâu bướm → Chọn B.',
            'Muốn chứng minh tín hiệu “directed primarily at predators”, hãy tìm đáp án cho thấy kẻ săn mồi phản ứng trực tiếp trước tín hiệu đó (ngừng tấn công/rút lui).',
            [
                ('Irrelevant Detail', 'Âm thanh mang tính đặc thù theo loài không chứng minh được nó nhắm vào kẻ săn mồi (giao tiếp cùng loài cũng đặc thù theo loài).'),
                ('Đáp án đúng', 'Chứng minh trực tiếp hiệu quả phòng vệ trước thiên địch: hai loài săn mồi thực sự dừng cuộc tấn công khi nghe âm thanh của sâu bướm.'),
                ('Irrelevant Detail', 'Việc mỗi loài thường phát ra một loại âm thanh hay nhiều loại âm thanh không liên quan đến mục tiêu là kẻ săn mồi.'),
                ('Weakens Claim', 'Phản tác dụng: nếu tiếng huýt (“whistles” — một trong hai loại âm thanh ghi nhận) không lọt vào dải nghe của chim săn mồi thì lại làm suy yếu luận điểm của nhóm.'),
            ],
        ),
        _q(
            'june2025_us_v1_rw_m1_q15', 15, 'Information and Ideas', 'Inferences', 'Easy',
            '<p>In dialects of English spoken in Scotland, the “r” sound is strongly emphasized when it appears at the end of syllables (as in “car”) or before other consonant sounds (as in “bird”). English dialects of the Upland South, a region stretching from Oklahoma to western Virginia, place similar emphasis on “r” at the ends of syllables and before other consonant sounds. Historical records show that the Upland South was colonized largely by people whose ancestors came from Scotland. Thus, linguists have concluded that _______</p>',
            'Which choice most logically completes the text?',
            [
                'the English dialects spoken in the Upland South acquired their emphasis on the “r” sound from dialects spoken in Scotland.',
                'emphasis on the “r” sound will eventually spread from English dialects spoken in the Upland South to dialects spoken elsewhere.',
                'the English dialects spoken in Scotland were influenced by dialects spoken in the Upland South.',
                'people from Scotland abandoned their emphasis on the “r” sound after relocating to the Upland South.',
            ],
            'A',
            'Chuỗi dữ kiện: (1) Phương ngữ tiếng Anh ở Scotland nhấn mạnh âm “r” ở cuối âm tiết và trước phụ âm khác; (2) Phương ngữ ở vùng Upland South cũng nhấn mạnh âm “r” ở đúng các vị trí tương tự; (3) Lịch sử ghi nhận vùng Upland South phần lớn do hậu duệ người Scotland đến định cư khai phá. Do đó kết luận hợp lý nhất của các nhà ngôn ngữ học là phương ngữ Upland South đã tiếp thu đặc điểm nhấn âm “r” từ phương ngữ Scotland → Chọn A.',
            'Chú ý CHIỀU LỊCH SỬ của ảnh hưởng: người gốc Scotland di cư đến khai phá Upland South → Scotland ảnh hưởng lên Upland South (tránh bẫy đảo chiều C).',
            [
                ('Đáp án đúng', 'Khớp chính xác chiều tác động lịch sử: cư dân gốc Scotland mang đặc điểm nhấn âm “r” đến hình thành phương ngữ vùng Upland South.'),
                ('Unsupported Prediction', 'Văn bản không hề đưa cơ sở nào để dự đoán tương lai rằng đặc điểm này sẽ lan sang các vùng khác.'),
                ('Reverses Causality', 'Đảo ngược chiều ảnh hưởng lịch sử: Upland South mới là nơi chịu ảnh hưởng từ người định cư gốc Scotland.'),
                ('Contradicts Text', 'Trái ngược dữ kiện: đoạn văn nêu rõ phương ngữ Upland South VẪN giữ cách nhấn mạnh âm “r” tương tự Scotland.'),
            ],
        ),
        _q(
            'june2025_us_v1_rw_m1_q16', 16, 'Standard English Conventions', 'Form, Structure, and Sense', 'Easy',
            '<p>What makes the theremin a unique musical instrument? You play it without touching it. When you place your _______ the pitch will shift as your hands move through the air.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            [
                'hand’s between the two antenna’s,',
                'hands between the two antennas,',
                'hands’ between the two antennas’,',
                'hands’ between the two antennas,',
            ],
            'B',
            'Kiểm tra sở hữu cách vs. số nhiều đơn thuần: (1) “your hands” là danh từ số nhiều bình thường (khớp với “as your hands move” ở cuối câu) và KHÔNG sở hữu danh từ nào theo sau → KHÔNG có dấu nháy đơn; (2) “the two antennas” cũng là danh từ số nhiều bình thường (đi với số đếm “two”) và không sở hữu gì → KHÔNG có dấu nháy đơn; dấu phẩy cuối cùng ngăn cách mệnh đề phụ mở đầu “When you place your hands between the two antennas,” với mệnh đề chính → Chọn B.',
            'Mẹo Plurals vs. Possessives: chỉ thêm dấu nháy đơn (`’s` / `s’`) khi danh từ ĐÓ sở hữu một danh từ khác đi ngay sau nó. Ở đây “between” là giới từ, không phải danh từ → 0 dấu nháy đơn!',
            [
                ('Wrong Possessive', 'Cả “hand’s” và “antenna’s” đều gắn sai sở hữu cách cho danh từ số nhiều không sở hữu vật gì.'),
                ('Đáp án đúng', 'Dùng chuẩn hai danh từ số nhiều không sở hữu cách (“hands” và “antennas”) kèm dấu phẩy kết thúc mệnh đề phụ “When...”.'),
                ('Wrong Possessive', 'Cả “hands’” lẫn “antennas’” đều thừa dấu nháy đơn sở hữu cách.'),
                ('Wrong Possessive', '“hands’” bị thừa dấu nháy đơn sở hữu cách trước giới từ “between”.'),
            ],
        ),
        _q(
            'june2025_us_v1_rw_m1_q17', 17, 'Standard English Conventions', 'Form, Structure, and Sense', 'Medium',
            '<p>Round Rock Chapter is one of the 110 chapters of the Navajo Nation (<i>Naabeehó Bináhásdzo</i>). The chapter, known as <i>Tsé Nikání</i> in the Navajo language (<i>Diné bizaad</i>), was the subject of a profile _______ in the <i>Navajo Times</i> on February 13, 2014.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['appeared', 'appearing', 'appears', 'has appeared'],
            'B',
            'Câu thứ 2 đã có động từ chia thì chính (finite verb) là “was”: “The chapter (...) **was** the subject of a profile _______ in the *Navajo Times* on February 13, 2014.” Do không có đại từ quan hệ (“that/which”) hay liên từ nào trước chỗ trống, ta KHÔNG thể điền thêm động từ chia thì (`appeared`, `appears`, `has appeared`) mà phải dùng phân từ hiện tại (`appearing` = dạng rút gọn của “that appeared”) để bổ nghĩa cho “a profile” → Chọn B.',
            'Quy tắc Finite vs. Non-finite Verb: câu đã có động từ chính (“was”) + không có đại từ quan hệ → chỗ trống bổ nghĩa cho danh từ phía trước bắt buộc dùng dạng không chia thì (`V-ing` chủ động / `V3` bị động). Vì “appear” là nội động từ nên chỉ dùng “appearing”!',
            [
                ('Finite Verb Collision', '“appeared” là động từ chia thì quá khứ (và “appear” là nội động từ nên không thể làm phân từ bị động) → sai ngữ pháp khi đặt thẳng sau “a profile”.'),
                ('Đáp án đúng', 'Phân từ hiện tại “appearing” (rút gọn của “that appeared”) bổ nghĩa chính xác cho danh từ “a profile”.'),
                ('Finite Verb Collision', '“appears” là động từ chia thì hiện tại đơn, tạo lỗi hai động từ chính không có liên kết trong cùng một mệnh đề.'),
                ('Finite Verb Collision', '“has appeared” là động từ chia thì hiện tại hoàn thành, sai cấu trúc mệnh đề và sai mốc thời gian cụ thể “on February 13, 2014”.'),
            ],
        ),
        _q(
            'june2025_us_v1_rw_m1_q18', 18, 'Standard English Conventions', 'Boundaries', 'Medium',
            '<p>San Juan High School and Grand County High School are two of several Utah _______ enormous geoglyph of the letters <i>SJ</i> overlooks San Juan High, while a geoglyph of the letter <i>G</i> overlooks Grand County High.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            [
                'schools that have their own hillside geoglyphs. An',
                'schools, that have their own hillside geoglyphs and an',
                'schools that have their own hillside geoglyphs, an',
                'schools, that have their own hillside geoglyphs, and an',
            ],
            'A',
            'Kiểm tra 2 quy tắc Boundaries cùng lúc: (1) Mệnh đề quan hệ xác định bắt đầu bằng “that” (“schools that have their own hillside geoglyphs”) TUYỆT ĐỐI KHÔNG có dấu phẩy đứng trước “that” → loại ngay B và D; (2) Phần trước (“San Juan High School... geoglyphs”) và phần sau (“An enormous geoglyph... overlooks San Juan High...”) là HAI MỆNH ĐỀ ĐỘC LẬP → không thể nối bằng một dấu phẩy đơn (loại C vì lỗi comma splice), mà tách gọn bằng dấu chấm (`. An`) → Chọn A.',
            'Nhớ cặp quy tắc thép: (1) CẤM đặt dấu phẩy trước đại từ quan hệ xác định “that”; (2) Hai mệnh đề độc lập tách nhau bằng dấu chấm, chấm phẩy, hoặc `, + FANBOYS`.',
            [
                ('Đáp án đúng', 'Không dùng dấu phẩy trước mệnh đề xác định “that...” và tách rạch ròi hai mệnh đề độc lập bằng dấu chấm (“geoglyphs. An”).'),
                ('Comma Before That & Run-on', 'Đặt sai dấu phẩy trước “that” đồng thời thiếu dấu phẩy trước “and” khi nối hai mệnh đề độc lập.'),
                ('Comma Splice', 'Nối hai mệnh đề độc lập chỉ bằng một dấu phẩy đơn (“geoglyphs, an”).'),
                ('Comma Before That', 'Đặt sai cặp dấu phẩy bao quanh mệnh đề bắt đầu bằng “that” (mệnh đề không xác định phải dùng “which”, không dùng “that”).'),
            ],
        ),
        _q(
            'june2025_us_v1_rw_m1_q19', 19, 'Standard English Conventions', 'Boundaries', 'Medium',
            '<p>Deposits of crushed orange limestone and other organic matter lend the sand at Porto Ferro Beach in Italy an unusual orange tint that dazzles _______ they take a bit of sand home, though, it disturbs the beach’s ecosystem by contributing to erosion.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['visitors, when', 'visitors and when', 'visitors when', 'visitors. When'],
            'D',
            'Phân tích ranh giới mệnh đề: Mệnh đề độc lập 1 = “Deposits... lend the sand... an unusual orange tint that dazzles visitors.” Mệnh đề độc lập 2 (mở đầu bằng mệnh đề phụ thuộc trạng ngữ) = “When they take a bit of sand home, though, it disturbs the beach’s ecosystem by contributing to erosion.” Vì hai vế đều là mệnh đề độc lập hoàn chỉnh, đáp án A tạo comma splice, B thiếu dấu phẩy trước “and” khi nối hai mệnh đề độc lập, và C tạo lỗi câu nối liền (run-on). Chỉ D dùng dấu chấm tách rõ hai câu → Chọn D.',
            'Gặp cấu trúc `[IC1] ___ [When + DC, though, IC2]`: tuyệt đối không dùng dấu phẩy đơn hay “and” không có phẩy — hãy tách bằng dấu chấm (`. When`)!',
            [
                ('Comma Splice', 'Nối hai mệnh đề độc lập chỉ bằng dấu phẩy đơn giữa “visitors” và mệnh đề “when..., though, it disturbs...”.'),
                ('Missing Comma Before FANBOYS', 'Nối hai mệnh đề độc lập bằng “and” nhưng thiếu dấu phẩy trước “and” (đồng thời “and” không hợp logic tương phản với “though”).'),
                ('Run-on / Fused Sentence', 'Gắn liền “when they take...” vào “dazzles visitors” khiến vế “it disturbs...” bị nối sai bằng dấu phẩy phía sau.'),
                ('Đáp án đúng', 'Dấu chấm tách rạch ròi câu 1 (kết thúc ở “visitors.”) khỏi câu 2 mở đầu bằng mệnh đề trạng ngữ “When they take a bit of sand home, though, it disturbs...”.'),
            ],
        ),
        _q(
            'june2025_us_v1_rw_m1_q20', 20, 'Standard English Conventions', 'Boundaries', 'Hard',
            '<p>Consider the mechanics of the pinhole camera: light passes through a small hole, resulting in a focused projected image. A ray diagram reveals how this _______ the hole’s small size restricts light to a single ray, all light passing through the hole can only arrive at a single destination, eliminating diffraction and ensuring a clear image.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['works because', 'works. Because', 'works, it’s because', 'works: it’s because'],
            'B',
            'CÂU BẪY BOUNDARIES KINH ĐIỂN! Đọc kỹ phần SAU dấu phẩy ở giữa: “all light passing through the hole can only arrive at a single destination...” là một MỆNH ĐỀ ĐỘC LẬP hoàn chỉnh! Vì vậy cụm “[Because] the hole’s small size restricts light to a single ray,” BẮT BUỘC phải là mệnh đề phụ thuộc mở đầu bổ nghĩa cho mệnh đề độc lập “all light... can only arrive...”. Nếu chọn A, C hay D thì mệnh đề “because...” bị kéo dính vào vế trước (`A ray diagram reveals...` / `it’s because...`), tạo ra lỗi COMMA SPLICE ngay sau chữ “single ray,”! Chỉ duy nhất B (`works. Because`) tách gọn câu 1 và mở câu 2 theo cấu trúc chuẩn `[Because DC], [IC]` → Chọn B.',
            'Luôn đọc HẾT TỚI DẤU CHẤM CUỐI CÂU trong câu Boundaries! Thấy một mệnh đề độc lập đứng sau dấu phẩy (“..., all light can only arrive...”) → kiểm tra ngay liệu vế đứng trước dấu phẩy đó có cần tách thành câu mới dạng `[Because DC, IC]` không!',
            [
                ('Comma Splice', 'Kéo “because...” vào câu trước khiến hai mệnh đề độc lập (“A ray diagram reveals... because... ray” và “all light... can only arrive...”) bị nối sai bằng dấu phẩy đơn.'),
                ('Đáp án đúng', 'Tách trọn vẹn hai câu: Câu 1 = “A ray diagram reveals how this works.”; Câu 2 = “[Because DC], [IC]” hoàn toàn chuẩn ngữ pháp.'),
                ('Double Comma Splice', 'Tạo tới hai lỗi comma splice liên tiếp sau “works,” và sau “single ray,”.'),
                ('Hidden Comma Splice', 'Bẫy cực tinh vi: dù dấu hai chấm sau “works” hợp lệ, nhưng “it’s because the hole’s small size restricts light to a single ray” lại trở thành một mệnh đề độc lập bị nối bằng dấu phẩy đơn với mệnh đề độc lập “all light... can only arrive...”!'),
            ],
        ),
        _q(
            'june2025_us_v1_rw_m1_q21', 21, 'Standard English Conventions', 'Boundaries', 'Easy',
            '<p>While the greater adjutant can be found in places like the Central Tanintharyi Coast in Myanmar and the Prek Toal Bird Sanctuary in Cambodia, more than 80 percent of this endangered stork species is found in Assam, India. There, wildlife biologist Dr. Purnima Devi Barman is on the front lines of conservation efforts that, through community involvement and scientific _______ aim to bring adjutants back from near extinction.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['study', 'study,', 'study:', 'study—'],
            'B',
            'Cụm bổ sung không thiết yếu “through community involvement and scientific study” xen vào giữa đại từ quan hệ “that” và động từ “aim”. Vì cụm này được mở bằng MỘT DẤU PHẨY sau “that,” nên bắt buộc phải đóng lại bằng MỘT DẤU PHẨY tương xứng sau “study,” → Chọn B.',
            'Quy tắc cặp dấu bổ sung (Paired Punctuation): mở bằng phẩy (`,`) thì phải đóng bằng phẩy (`,`) — không được bỏ quên (A), cũng không được trộn với dấu hai chấm (C) hay gạch ngang (D).',
            [
                ('Missing Closing Comma', 'Thiếu dấu phẩy đóng cụm chèn giữa “that,” và động từ “aim”.'),
                ('Đáp án đúng', 'Khép đúng cặp dấu phẩy bao quanh cụm chèn “, through community involvement and scientific study,” trước động từ “aim”.'),
                ('Mismatched Punctuation', 'Không được dùng dấu hai chấm để đóng một cụm mở bằng dấu phẩy và nằm giữa chủ ngữ “that” với động từ “aim”.'),
                ('Mismatched Punctuation', 'Không được ghép lệch dấu phẩy mở (`,`) với dấu gạch ngang đóng (`—`).'),
            ],
        ),
        _q(
            'june2025_us_v1_rw_m1_q22', 22, 'Expression of Ideas', 'Transitions', 'Easy',
            '<p>In 1949, Frank Zamboni developed an ice rink resurfacing machine. As Zamboni’s machine moved along the rink’s surface, it first scraped off the top layer of ice. _______ it sprayed water into the deep grooves left behind by customers’ skates. Lastly, it smoothed over the newly formed ice.</p>',
            'Which choice completes the text with the most logical transition?',
            ['For example,', 'Next,', 'Similarly,', 'In contrast,'],
            'B',
            'Đoạn văn mô tả quy trình 3 bước theo trình tự thời gian rất rõ ràng: bước 1 có “first” (“first scraped off...”), bước 3 có “Lastly” (“Lastly, it smoothed over...”). Do đó bước ở giữa cần từ nối trình tự “Next,” (Tiếp theo) → Chọn B.',
            'Nhận diện chuỗi tín hiệu trình tự kinh điển: `first ... → Next, ... → Lastly, ...`.',
            [
                ('Wrong Relationship', 'For example = Ví dụ — bước phun nước là công đoạn kế tiếp trong quy trình, không phải ví dụ cho bước cạo lớp băng.'),
                ('Đáp án đúng', 'Next = Tiếp theo — kết nối mượt mà bước giữa trong trình tự “first → Next → Lastly”.'),
                ('Wrong Relationship', 'Similarly = Tương tự — phun nước vào rãnh không phải hành động tương đồng với cạo bỏ lớp băng trên mặt.'),
                ('False Contrast', 'In contrast = Ngược lại — hai bước liên tiếp trong cùng quy trình vận hành máy không đối lập nhau.'),
            ],
        ),
        _q(
            'june2025_us_v1_rw_m1_q23', 23, 'Expression of Ideas', 'Rhetorical Synthesis', 'Easy',
            '<p>While researching a topic, a student has taken the following notes:</p><ul><li>A lever is a simple machine consisting of a rigid beam and a fulcrum.</li><li>The fulcrum is the point about which the beam pivots.</li><li>The input force (effort) is the force applied to the lever.</li><li>The output force (load) is the force that the lever exerts on another object.</li><li>In first-class levers, the fulcrum is located between the effort and the load.</li><li>In second-class levers, the load is located between the effort and the fulcrum.</li></ul>',
            'The student wants to contrast first-class levers and second-class levers. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
            [
                'In levers, the effort is the force applied to the lever; the load, in contrast, is the force that the lever exerts on another object.',
                'In first-class and second-class levers, the fulcrum and the load are in different locations.',
                'First-class levers are simple machines consisting of a rigid beam and a fulcrum, but then again, the same is true of second-class levers.',
                'In first-class levers, the fulcrum is located between the effort and the load, but in second-class levers, the load is located between the effort and the fulcrum.',
            ],
            'D',
            'Mục tiêu (Goal): ĐỐI CHIẾU đòn bẩy loại 1 và đòn bẩy loại 2 (“contrast first-class levers and second-class levers”). Đáp án D nêu cụ thể sự khác biệt cốt lõi giữa hai loại bằng liên từ đối lập “but” (loại 1: điểm tựa nằm giữa lực tác động và tải; loại 2: tải nằm giữa lực tác động và điểm tựa) → Chọn D.',
            'Với Goal “contrast X and Y”, đáp án đúng phải nêu RÕ đặc điểm cụ thể đối lập nhau của cả X và Y (tránh đáp án mơ hồ như B chỉ nói chung chung “in different locations”).',
            [
                ('Wrong Subjects', 'Đối chiếu “effort” (lực tác động) và “load” (tải) chứ không đối chiếu đòn bẩy loại 1 và loại 2.'),
                ('Too Vague', 'Chỉ nói chung chung rằng điểm tựa và tải ở các vị trí khác nhau mà không chỉ rõ sự khác biệt cụ thể như ghi chú.'),
                ('Similarity Instead of Contrast', 'Nêu điểm GIỐNG NHAU (“the same is true”) giữa hai loại đòn bẩy thay vì đối chiếu khác biệt.'),
                ('Đáp án đúng', 'Trình bày trực diện, chính xác và đầy đủ sự đối lập về vị trí điểm tựa và tải giữa đòn bẩy loại 1 và loại 2.'),
            ],
        ),
        _q(
            'june2025_us_v1_rw_m1_q24', 24, 'Expression of Ideas', 'Rhetorical Synthesis', 'Easy',
            '<ul><li>Richard Serra is an American artist.</li><li>He is known for his large metal sculptures.</li><li>His large sculpture <i>Open Ended</i> is made of weathering steel.</li><li>His large sculpture <i>Strike: To Roberta and Rudy</i> is made of hot-rolled steel.</li></ul>',
            'Which choice most effectively uses information from the given sentences to emphasize a difference between the two sculptures?',
            [
                '<i>Open Ended</i> and <i>Strike: To Roberta and Rudy</i> are both large metal sculptures by artist Richard Serra.',
                '<i>Strike: To Roberta and Rudy</i> is one of artist Richard Serra’s large metal sculptures.',
                'Artist Richard Serra is the creator of the weathering steel sculpture <i>Open Ended</i>.',
                '<i>Open Ended</i> is made from a different kind of steel than <i>Strike: To Roberta and Rudy</i>.',
            ],
            'D',
            'Mục tiêu (Goal): Nhấn mạnh MỘT SỰ KHÁC BIỆT giữa hai tác phẩm điêu khắc (“emphasize a difference between the two sculptures”). Chỉ đáp án D vừa nhắc cả hai tác phẩm vừa nhấn mạnh trực tiếp điểm khác biệt về chất liệu thép (“made from a different kind of steel”: weathering steel vs. hot-rolled steel) → Chọn D.',
            'Đọc từ khóa Goal “a difference between the two sculptures”: loại ngay câu nêu điểm giống (“both” ở A) và các câu chỉ nhắc 1 tác phẩm (B, C).',
            [
                ('Similarity Instead of Difference', 'Nhấn mạnh điểm giống nhau (“both large metal sculptures”) thay vì khác biệt.'),
                ('Single Subject', 'Chỉ nhắc một tác phẩm (<i>Strike: To Roberta and Rudy</i>), không thể so sánh hai tác phẩm.'),
                ('Single Subject', 'Chỉ nhắc một tác phẩm (<i>Open Ended</i>), bỏ sót tác phẩm thứ hai.'),
                ('Đáp án đúng', 'Nêu cả hai tác phẩm và nhấn mạnh chính xác sự khác biệt về loại thép chế tác giữa chúng.'),
            ],
        ),
        _q(
            'june2025_us_v1_rw_m1_q25', 25, 'Expression of Ideas', 'Rhetorical Synthesis', 'Easy',
            '<ul><li>Maya Lin is an American artist known for her memorials and large-scale installation artworks.</li><li>She became famous in 1982 when she completed the Vietnam Veterans Memorial, which consists of two 246-foot granite walls.</li><li>She completed <i>Water Line</i> in 2006.</li><li>It is an installation composed of aluminum tubing that fills an entire gallery room.</li><li>She completed <i>Seven Earth Mountain</i> in 2015.</li><li>It is an installation composed of soil that fills an entire gallery room.</li></ul>',
            'Which choice most effectively uses information from the given sentences to emphasize a difference between <i>Water Line</i> and <i>Seven Earth Mountain</i>?',
            [
                'After completing the Vietnam Veterans Memorial, Maya Lin completed <i>Water Line</i>, another large-scale work.',
                'The sprawling size of Maya Lin’s Vietnam Veterans Memorial is echoed in <i>Water Line</i>, a work made of aluminum tubing that fills an entire gallery room.',
                'Maya Lin’s <i>Water Line</i> is composed of aluminum tubing; <i>Seven Earth Mountain</i>, by contrast, is composed of soil.',
                'Maya Lin is known for her memorials and installation art, such as <i>Water Line</i> and <i>Seven Earth Mountain</i>.',
            ],
            'C',
            'Mục tiêu (Goal): Nhấn mạnh sự khác biệt giữa <i>Water Line</i> và <i>Seven Earth Mountain</i>. Chỉ đáp án C đối chiếu trực tiếp hai tác phẩm bằng từ nối tương phản “by contrast”: <i>Water Line</i> làm từ ống nhôm (“aluminum tubing”) còn <i>Seven Earth Mountain</i> làm từ đất (“soil”) → Chọn C.',
            'Khóa 3 điều kiện của Goal: có <i>Water Line</i> + có <i>Seven Earth Mountain</i> + nêu rõ điểm khác biệt (“by contrast”).',
            [
                ('Missing Second Work', 'Chỉ nhắc Đài tưởng niệm Cựu chiến binh Việt Nam và <i>Water Line</i>, không hề đề cập <i>Seven Earth Mountain</i>.'),
                ('Missing Second Work', 'So sánh Đài tưởng niệm với <i>Water Line</i>, thiếu <i>Seven Earth Mountain</i>.'),
                ('Đáp án đúng', 'Đối chiếu trực diện sự khác biệt chất liệu giữa <i>Water Line</i> (ống nhôm) và <i>Seven Earth Mountain</i> (đất).'),
                ('No Difference Stated', 'Chỉ liệt kê cả hai là ví dụ cho nghệ thuật sắp đặt của Maya Lin, không nêu điểm khác nhau nào.'),
            ],
        ),
        _q(
            'june2025_us_v1_rw_m1_q26', 26, 'Expression of Ideas', 'Rhetorical Synthesis', 'Easy',
            '<p>While researching a topic, a student has taken the following notes:</p><ul><li>A supercontinent is a single landmass made up of most or all of Earth’s continents.</li><li>Over time, continents merge together to form supercontinents, which then break apart.</li><li>This process is believed to take hundreds of millions of years and is known as the supercontinent cycle.</li><li>Euramerica and Kenorland were supercontinents.</li><li>Euramerica formed about 300 million years ago.</li><li>Kenorland formed about 2.6 billion years ago.</li></ul>',
            'The student wants to specify when Euramerica formed. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
            [
                'The supercontinent Euramerica formed about 300 million years ago.',
                'Over hundreds of millions of years, the supercontinent cycle results in supercontinents forming and breaking apart.',
                'Euramerica was a supercontinent, a single landmass made up of most or all of Earth’s continents.',
                'Long ago, the Earth was home to supercontinents like Euramerica and Kenorland.',
            ],
            'A',
            'Mục tiêu (Goal): Chỉ rõ THỜI ĐIỂM siêu lục địa Euramerica hình thành (“specify when Euramerica formed”). Duy nhất đáp án A nêu chính xác mốc thời gian cụ thể từ ghi chú: “about 300 million years ago” → Chọn A.',
            'Động từ “specify when” đòi hỏi mốc thời gian cụ thể (`about 300 million years ago`) — tránh cách nói mơ hồ như “Long ago” ở D.',
            [
                ('Đáp án đúng', 'Nêu trực diện, súc tích đúng mốc thời gian hình thành của Euramerica (“about 300 million years ago”).'),
                ('Wrong Synthesis Goal', 'Chỉ mô tả chu kỳ siêu lục địa nói chung, không nhắc đến Euramerica hay thời điểm nó hình thành.'),
                ('Wrong Synthesis Goal', 'Chỉ định nghĩa siêu lục địa, bỏ qua thời điểm hình thành của Euramerica.'),
                ('Too Vague', 'Chỉ nói mơ hồ “Long ago”, không chỉ rõ mốc thời gian cụ thể của Euramerica.'),
            ],
        ),
        _q(
            'june2025_us_v1_rw_m1_q27', 27, 'Expression of Ideas', 'Rhetorical Synthesis', 'Medium',
            '<ul><li>The Haystack Mountain School of Crafts (1961) is a building complex designed by American architect Edward Larrabee Barnes.</li><li>It is located in Deer Isle, Maine.</li><li>It features a cluster of cedar-shingled buildings.</li><li>It is considered an impressive example of critical regionalist architecture.</li></ul>',
            'Which choice most effectively uses information from the given sentences to emphasize the location of the Haystack Mountain School of Crafts?',
            [
                'Those wishing to see the Haystack Mountain School of Crafts in person will have to travel to Deer Isle, Maine.',
                'A stunning example of critical regionalist architecture, Edward Larrabee Barnes’s Haystack Mountain School of Crafts features a cluster of cedar-shingled buildings.',
                'The architect responsible for designing the Haystack Mountain School of Crafts in Deer Isle, Maine, was Edward Larrabee Barnes.',
                'Edward Larrabee Barnes is known for designing a building complex that features a cluster of cedar-shingled buildings.',
            ],
            'A',
            'Mục tiêu (Goal): NHẤN MẠNH VỊ TRÍ của Haystack Mountain School of Crafts (“emphasize the location”). B và D hoàn toàn không nhắc tới Deer Isle, Maine. So sánh A và C: C chỉ lướt qua “in Deer Isle, Maine” như một cụm giới từ phụ để nhấn mạnh tên kiến trúc sư Edward Larrabee Barnes; trong khi A đặt trọng tâm toàn bộ vị ngữ vào địa điểm (“will have to travel to Deer Isle, Maine”) → Chọn A.',
            'Phân biệt “nhắc tới thông tin X” (C chỉ chèn địa điểm như phụ chú trong câu nói về kiến trúc sư) vs. “nhấn mạnh thông tin X” (A biến địa điểm thành nội dung trọng tâm chính của cả câu)!',
            [
                ('Đáp án đúng', 'Đặt địa điểm “Deer Isle, Maine” làm trọng tâm vị ngữ của câu, nhấn mạnh rõ nơi tọa lạc của ngôi trường.'),
                ('Missing Location', 'Không đề cập vị trí Deer Isle, Maine — chỉ nhấn mạnh phong cách kiến trúc và vật liệu mái gỗ tuyết tùng.'),
                ('Wrong Emphasis', 'Dù có nhắc “in Deer Isle, Maine” nhưng trọng tâm câu lại nhấn mạnh kiến trúc sư thiết kế (“The architect... was Edward Larrabee Barnes”).'),
                ('Missing Location', 'Không nhắc đến tên ngôi trường lẫn địa điểm Deer Isle, Maine.'),
            ],
        ),
    ]


# ============================================================================
# MODULE 2 (27 Qs — June 2025 US Ver 1; used for module2_hard & module2_lower)
# ============================================================================

def get_m2_questions(prefix='june2025_us_v1_rw_m2h'):
    return [
        _q(
            f'{prefix}_q1', 1, 'Craft and Structure', 'Words in Context', 'Medium',
            '<p>Whether the reign of a French monarch such as Francis II or Louis XI was considered historically significant or, conversely, relatively _______, its trajectory was shaped by questions of legitimacy and therefore cannot be understood without a corollary understanding of the factors that allowed the monarch to assert a claim to the throne successfully.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            ['momentous', 'inconsequential', 'benevolent', 'genuine'],
            'B',
            'Tín hiệu trái nghĩa trực diện: “historically significant or, conversely, relatively _______” (có tầm quan trọng lịch sử hay, ngược lại, tương đối [không đáng kể]). Từ trái nghĩa chính xác với “significant” là “inconsequential” (không đáng kể, ít tầm quan trọng) → Chọn B.',
            'Cặp tín hiệu `X or, conversely, Y` bắt buộc Y phải là từ TRÁI NGHĨA trực tiếp với X: `significant` ↔ `inconsequential`.',
            [
                ('Synonym Trap', 'momentous = trọng đại, có ý nghĩa lớn — đồng nghĩa chứ không trái nghĩa với “significant” sau từ “conversely”.'),
                ('Đáp án đúng', 'inconsequential = không quan trọng, ít hệ trọng — đối lập chính xác với “historically significant”.'),
                ('Off-Axis Meaning', 'benevolent = nhân từ, độ lượng — không phải cặp trái nghĩa với “significant”.'),
                ('Off-Axis Meaning', 'genuine = chân thật, chính thống — không đối lập với “significant”.'),
            ],
        ),
        _q(
            f'{prefix}_q2', 2, 'Craft and Structure', 'Words in Context', 'Hard',
            '<p>In the 2010s, the price of vintage Teenage Mutant Ninja Turtles action figures rose dramatically, which had the counterintuitive effect of _______ demand: buyers who hadn’t previously wanted to purchase old action figures thronged the market, believing prices would continue to rise and the toys could be resold later at a profit.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            ['monetizing', 'appraising', 'engendering', 'exploiting'],
            'C',
            'Thông thường giá tăng mạnh sẽ làm giảm cầu, nhưng ở đây lại gây hiệu ứng ngược trực giác (“counterintuitive effect”) được giải thích ngay sau dấu hai chấm: những người trước đó chưa từng muốn mua nay đổ xô vào thị trường (“buyers who hadn’t previously wanted to purchase... thronged the market”) → tức là TẠO RA / KHƠI DẬY nhu cầu mới. Động từ chuẩn xác là “engendering” (tạo ra, làm nảy sinh) → Chọn C.',
            'Học thuộc từ vựng SAT hay ra: `engender` = tạo ra, sản sinh, khơi dậy (một hiện tượng/nhu cầu/phản ứng).',
            [
                ('Wrong Meaning', 'monetizing = kiếm tiền từ / thương mại hóa — không mang nghĩa “tạo ra” nhu cầu từ người mua mới.'),
                ('Wrong Meaning', 'appraising = định giá, thẩm định — không khớp với việc người mua mới đổ xô vào thị trường.'),
                ('Đáp án đúng', 'engendering = làm nảy sinh, tạo ra — khớp hoàn hảo với tác động ngược trực giác là giá tăng lại sinh thêm nhu cầu mới.'),
                ('Wrong Meaning', 'exploiting = khai thác, lợi dụng — diễn tả hành vi tận dụng nhu cầu sẵn có chứ không phải tạo ra nhu cầu từ những người vốn không muốn mua.'),
            ],
        ),
        _q(
            f'{prefix}_q3', 3, 'Craft and Structure', 'Words in Context', 'Hard',
            '<p>Studying wrappers from discontinued candies, menus from nineteenth-century restaurants, and flyers promoting long-forgotten sporting events may seem like a frivolous pursuit, but ephemeral objects like these are useful as markers of cultural change: they can _______ shifts in norms, values, and concerns that traditional objects of historical inquiry may not.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            ['register', 'vindicate', 'preclude', 'induce'],
            'A',
            'Đọc kỹ cụm khóa trước dấu hai chấm: những đồ vật nhất thời này hữu ích với vai trò “markers of cultural change” (dấu ấn/chỉ báo ghi nhận sự biến chuyển văn hóa). Phần sau dấu hai chấm giải thích: chúng có thể GHI NHẬN / PHẢN ÁNH (“register”) những chuyển biến về chuẩn mực, giá trị và mối quan tâm mà các hiện vật lịch sử truyền thống có thể không thể hiện → Chọn A.',
            'Động từ `register` trên SAT thường kiểm tra nghĩa học thuật thứ cấp: “ghi nhận, phản ánh, thể hiện (như một máy đo/dấu chỉ)” — khớp tuyệt đối với “markers of cultural change”!',
            [
                ('Đáp án đúng', 'register = ghi nhận, phản ánh, biểu thị — khớp hoàn toàn vai trò “markers of cultural change” (dấu chỉ sự biến đổi văn hóa).'),
                ('Wrong Meaning', 'vindicate = minh oan, chứng minh là đúng đắn — không hợp tân ngữ “shifts in norms, values, and concerns”.'),
                ('Wrong Meaning', 'preclude = ngăn ngừa, loại trừ — vô lý vì vỏ kẹo hay thực đơn không ngăn cản chuyển biến văn hóa.'),
                ('Causation Trap', 'induce = gây ra, kích phát — những đồ vật này chỉ là DẤU CHỈ phản ánh thay đổi văn hóa, không phải nguyên nhân gây ra thay đổi đó.'),
            ],
        ),
        _q(
            f'{prefix}_q4', 4, 'Craft and Structure', 'Words in Context', 'Hard',
            '<p>_______ though it seemed to many mathematicians, the Marden tameness conjecture, posed in 1974, eventually yielded to the efforts of Ian Agol, who presented a proof of it in 2004.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            ['Insuperable', 'Unequivocal', 'Irreproachable', 'Ineluctable'],
            'A',
            'Cấu trúc đảo ngữ nhượng bộ `[Tính từ] though it seemed...` đối lập với vế sau “eventually yielded to the efforts of Ian Agol, who presented a proof of it” (cuối cùng đã khuất phục trước nỗ lực chứng minh của Ian Agol). Đối lập với việc “cuối cùng cũng bị chinh phục/giải quyết” là cảm giác ban đầu rằng bài toán KHÔNG THỂ VƯỢT QUA / BẤT KHẢ THI → “Insuperable” → Chọn A.',
            'Bộ 4 từ “In-/Un-” bậc Hard rất hay gặp trên SAT: `Insuperable` (không thể vượt qua — gốc *super-* = vượt lên trên), `Unequivocal` (rõ ràng không mập mờ), `Irreproachable` (không chê trách được), `Ineluctable` (không thể tránh khỏi).',
            [
                ('Đáp án đúng', 'Insuperable = không thể vượt qua, bất khả chinh phục — tương phản sắc nét với “eventually yielded to the efforts”.'),
                ('Wrong Meaning', 'Unequivocal = dứt khoát, rõ ràng không mơ hồ — không đối lập với việc cuối cùng được chứng minh.'),
                ('Wrong Meaning', 'Irreproachable = hoàn hảo, không thể chê trách — không phù hợp với một giả thuyết toán học khó giải.'),
                ('Wrong Meaning', 'Ineluctable = tất yếu, không thể tránh khỏi — sai ngữ nghĩa khi ghép với giả thuyết toán học được chứng minh.'),
            ],
        ),
        _q(
            f'{prefix}_q5', 5, 'Craft and Structure', 'Text Structure and Purpose', 'Easy',
            '<p>Why do rusty-spotted cats purr but jaguars roar? Researchers hypothesize that this difference between the two feline species may be partly due to a U-shaped bone in their throats called the hyoid. Rusty-spotted cats, which are much smaller than jaguars, have a rigid hyoid that rumbles when the cat’s larynx vibrates, resulting in a purr. By contrast, jaguars have a somewhat flexible hyoid, and the bone is attached to the skull with a stretchy ligament that rusty-spotted cats lack. These traits allow jaguars and most other species of big cats to produce powerful roars. The same traits may also prevent most big cats from purring.</p>',
            'Which choice best describes the overall structure of the text?',
            [
                'The text compares the habitats of two species, then explains how those habitats are changing.',
                'The text presents a theory about two species, then discusses facts that weaken it.',
                'The text poses a question about two species, then presents a possible answer.',
                'The text describes a behavior shared by two species, then discusses other behaviors shared by them.',
            ],
            'C',
            'Câu đầu tiên đặt một câu hỏi trực tiếp về hai loài họ mèo (“Why do rusty-spotted cats purr but jaguars roar?”). Toàn bộ phần còn lại trình bày giả thuyết của các nhà nghiên cứu (“Researchers hypothesize... may be partly due to...”) về cấu trúc xương móng (hyoid) như một lời giải đáp khả dĩ → Chọn C.',
            'Nhận diện bố cục ngay từ 2 câu đầu: Câu 1 = Câu hỏi (`Why do... ?`) → Câu 2+ = Câu trả lời khả dĩ (`Researchers hypothesize...`).',
            [
                ('Unsupported Content', 'Đoạn văn không đề cập đến môi trường sống (“habitats”) của hai loài.'),
                ('Opposite Direction', 'Các chi tiết phía sau đều giải thích và minh họa cho giả thuyết xương móng, không hề làm suy yếu nó.'),
                ('Đáp án đúng', 'Khớp hoàn toàn bố cục: đặt câu hỏi về hai loài mèo, sau đó trình bày một lời giải thích khả dĩ từ giới nghiên cứu.'),
                ('Contradicts Text', 'Mèo đốm gỉ (gừ) và báo đốm (gầm) có hành vi KHÁC NHAU, không phải hành vi chung.'),
            ],
        ),
        _q(
            f'{prefix}_q6', 6, 'Craft and Structure', 'Text Structure and Purpose', 'Medium',
            '<p>Scholarly interest in literary juvenilia—writings by children and teenagers—tends to focus on unpublished works by authors who became famous as adults, such as Charles Dickens’s poem “The Bill of Fare,” which he wrote around the ages of 18–20, because they offer insights into their authors’ artistic development. But some scholars also argue that recovering juvenilia by lesser-known writers is essential to understanding literary history: Daisy Ashford’s novels, which she published as a child, were widely read by contemporaries and are therefore deserving of closer attention.</p>',
            'Which choice best states the main purpose of the text?',
            [
                'To describe the challenges famous writers encountered when seeking to publish works written in their childhood',
                'To present reasons why literary scholars consider juvenilia to be valuable resources',
                'To compare the accomplishments of young writers with those of their adult contemporaries',
                'To argue that Ashford’s novels have more literary merit than Dickens’s juvenilia do',
            ],
            'B',
            'Cả hai câu đều trình bày những lý do khiến giới nghiên cứu văn học coi tác phẩm thời niên thiếu (“literary juvenilia”) là nguồn tư liệu giá trị: (1) tác phẩm của các tác giả sau này nổi tiếng (như Dickens) hé lộ quá trình phát triển nghệ thuật (“offer insights into their authors’ artistic development”); (2) tác phẩm của các tác giả ít tên tuổi hơn (như Daisy Ashford) thiết yếu để hiểu lịch sử văn học (“essential to understanding literary history”) → Chọn B.',
            'Khi đoạn văn nêu 2 nhánh cùng chiều (`tends to focus on X because...` + `But some scholars also argue Y is essential...`), mục đích bao trùm là trình bày các lý do khẳng định giá trị của đối tượng chung (juvenilia).',
            [
                ('Unsupported Content', 'Đoạn văn không hề bàn về khó khăn xuất bản các tác phẩm thời thơ ấu của nhà văn nổi tiếng.'),
                ('Đáp án đúng', 'Bao quát trọn vẹn cả hai vế của đoạn: lý do học giả đánh giá cao juvenilia của tác giả nổi tiếng lẫn tác giả ít được biết đến.'),
                ('Wrong Comparison', 'Không hề so sánh thành tựu của nhà văn trẻ với các nhà văn trưởng thành cùng thời.'),
                ('False Comparison', 'Không so sánh giá trị văn chương giữa tiểu thuyết của Ashford và tác phẩm thời trẻ của Dickens.'),
            ],
        ),
        _q(
            f'{prefix}_q7', 7, 'Information and Ideas', 'Inferences', 'Hard',
            '<p>To understand how temperature change affects microorganism-mediated cycling of soil nutrients in alpine ecosystems, Eva Kaštovská et al. collected plant-soil cores in the Tatra Mountains at elevations around 2,100 meters and transplanted them to elevations of 1,700–1,800 meters, where the mean air temperature was warmer by 2°C. Microorganism-mediated nutrient cycling was accelerated in the transplanted cores; crucially, microorganism community composition was unchanged, allowing Kaštovská et al. to attribute the acceleration to temperature-induced increases in microorganism activity.</p>',
            'It can most reasonably be inferred from the text that the finding about the microorganism community composition was important for which reason?',
            [
                'It provided preliminary evidence that microorganism-mediated nutrient cycling was accelerated in the transplanted cores.',
                'It suggested that temperature-induced changes in microorganism activity may be occurring at increasingly high elevations.',
                'It ruled out a potential alternative explanation for the acceleration in microorganism-mediated nutrient cycling.',
                'It clarified that microorganism activity levels in the plant-soil cores varied depending on which microorganisms comprised the community.',
            ],
            'C',
            'Phân tích logic kiểm soát biến thí nghiệm: khi chuyển lõi đất xuống độ cao ấm hơn 2°C, chu trình dinh dưỡng do vi sinh vật thúc đẩy tăng tốc. Có 2 nguyên nhân tiềm năng: (1) thành phần loài vi sinh vật đã thay đổi (xuất hiện loài mới mạnh hơn), HOẶC (2) vẫn các vi sinh vật cũ nhưng hoạt động mạnh hơn do ấm lên. Việc phát hiện thành phần quần xã vi sinh vật KHÔNG ĐỔI (“microorganism community composition was unchanged”) đã LOẠI TRỪ NGUYÊN NHÂN THAY THẾ (1), giúp nhóm nghiên cứu yên tâm quy kết tốc độ tăng là do nhiệt độ kích thích hoạt tính vi sinh vật → Chọn C.',
            'Cụm “crucially, [yếu tố X] was unchanged, allowing researchers to attribute [kết quả] to [nguyên nhân Y]” là dấu hiệu kinh điển của việc **loại trừ một lời giải thích thay thế tiềm tàng** (“ruled out a potential alternative explanation”)!',
            [
                ('Confuses Cause & Effect', 'Việc thành phần vi sinh vật không đổi không phải là bằng chứng cho thấy chu trình dinh dưỡng tăng tốc (sự tăng tốc được đo trực tiếp).'),
                ('Unsupported Claim', 'Đoạn văn không suy luận về xu hướng diễn ra ở các độ cao ngày càng lớn hơn.'),
                ('Đáp án đúng', 'Khớp hoàn hảo logic khoa học: quần xã vi sinh vật không đổi đã loại trừ khả năng sự thay đổi loài gây ra tăng tốc, củng cố kết luận do tăng hoạt tính vì nhiệt độ.'),
                ('Contradicts Text', 'Trái dữ kiện: quần xã vi sinh vật không hề thay đổi nên thí nghiệm không chứng minh hoạt tính biến thiên theo từng loài khác nhau.'),
            ],
        ),
        _q(
            f'{prefix}_q8', 8, 'Information and Ideas', 'Central Ideas and Details', 'Medium',
            '<p>Michael G. Campana and colleagues relied on historical DNA (hDNA)—genomic data incidentally preserved in specimens housed in natural history collections—to investigate the evolutionary origins of a fungal pathogen affecting bats. Although this approach offers unique benefits, such as access to genomic data from extirpated populations, it remains a relatively underutilized resource because hDNA is often to some extent degraded, a situation not easily remediable under current methodological paradigms and with extant DNA extraction and analysis technologies.</p>',
            'Information in the text best supports which statement about hDNA?',
            [
                'It may yield insights that other types of genomic data cannot.',
                'It has thus far proved valuable mainly to researchers studying pathogens.',
                'It may be underused because of its controversial status among scientists.',
                'It tends to be much more degraded than other types of DNA of comparable age.',
            ],
            'A',
            'Văn bản nêu rõ: “Although this approach offers **unique benefits**, such as access to genomic data from extirpated populations...” (“những lợi ích độc nhất, chẳng hạn tiếp cận dữ liệu bộ gen từ các quần thể đã tuyệt diệt ở địa phương”). Do những lợi ích đó mang tính độc nhất (“unique”), hDNA có thể đem lại những hiểu biết mà các loại dữ liệu bộ gen khác không thể cung cấp → Chọn A.',
            'Từ khóa “unique benefits” (lợi ích độc nhất) trong bài đọc tương đương trực tiếp với “insights that other types of genomic data cannot [yield]”.',
            [
                ('Đáp án đúng', 'Khớp trực tiếp với “unique benefits, such as access to genomic data from extirpated populations” — những thông tin mà các nguồn DNA khác không thể có.'),
                ('Overgeneralization', 'Nhóm Campana dùng hDNA để nghiên cứu nấm gây bệnh ở dơi chỉ là MỘT ví dụ, không chứng minh nó hữu ích “chủ yếu” cho giới nghiên cứu mầm bệnh.'),
                ('Unsupported Cause', 'hDNA ít được sử dụng do bị phân hủy và giới hạn công nghệ trích xuất, KHÔNG phải vì “tình trạng gây tranh cãi”.'),
                ('Unsupported Comparison', 'Đoạn văn nói hDNA thường bị phân hủy ở một mức độ nhất định, không hề so sánh mức độ phân hủy với các loại DNA khác cùng độ tuổi.'),
            ],
        ),
        _q(
            f'{prefix}_q9', 9, 'Information and Ideas', 'Command of Evidence: Textual', 'Easy',
            '<p>In a paper for an art history class, a student claims that Rosa Bonheur’s 1855 painting <i>The Horse Fair</i> marks a significant change in Bonheur’s artistic development.</p>',
            'Which quotation from an art history textbook would most effectively support the student’s claim?',
            [
                '“The paintings that Bonheur produced before <i>The Horse Fair</i> can be thought of as belonging to her earlier style, to which she never returned.”',
                '“Of all Bonheur’s paintings, none so clearly represents her abilities and ideas as <i>The Horse Fair</i>.”',
                '“<i>The Horse Fair</i> has been analyzed extensively since it was first exhibited, as no two viewers seem to agree about exactly what the painting means.”',
                '“Although Bonheur was clearly influenced by other artists of her time, she was also an artist ahead of her time, as <i>The Horse Fair</i> demonstrates.”',
            ],
            'A',
            'Nhận định cần chứng minh: bức <i>The Horse Fair</i> (1855) đánh dấu MỘT BƯỚC NGOẶT / THAY ĐỔI LỚN trong quá trình phát triển nghệ thuật của Rosa Bonheur (“marks a significant change in Bonheur’s artistic development”). Chỉ đáp án A khẳng định các bức tranh vẽ trước <i>The Horse Fair</i> thuộc phong cách cũ hơn mà bà KHÔNG BAO GIỜ QUAY LẠI NỮA → chứng minh bức tranh này là cột mốc chuyển đổi rõ rệt → Chọn A.',
            'Khóa chặt cụm từ trọng tâm của Claim: `significant change in artistic development` = mốc chia ranh giới phong cách cũ vs. mới (“earlier style, to which she never returned”).',
            [
                ('Đáp án đúng', 'Khẳng định rõ <i>The Horse Fair</i> là ranh giới tách biệt hoàn toàn với phong cách cũ trước đó mà bà không bao giờ quay lại.'),
                ('Off-Focus Praise', 'Chỉ ca ngợi bức tranh thể hiện rõ nhất tài năng và tư tưởng của bà, không chứng minh sự THAY ĐỔI phong cách.'),
                ('Irrelevant Detail', 'Chỉ nói bức tranh được phân tích nhiều và gây nhiều cách hiểu khác nhau, không liên quan tiến trình phát triển của họa sĩ.'),
                ('Wrong Focus', 'Chỉ bàn việc bà đi trước thời đại so với các nghệ sĩ khác, không chứng minh bước ngoặt trong sự nghiệp riêng của bà.'),
            ],
        ),
        _q(
            f'{prefix}_q10', 10, 'Information and Ideas', 'Command of Evidence: Textual', 'Hard',
            '<p>Neurobiologists Laura Cuaya, Raúl Hernández-Pérez, and colleagues investigated the language detection abilities of eighteen dogs. The researchers monitored the brain activity of Kun-kun (a border collie), Bingo (a mixed breed), and other dogs while the animals listened to three recordings: one of <i>The Little Prince</i> being read in Spanish, the second in Hungarian, and a third made up of short, randomly selected fragments of the first two, scrambled so that they didn’t resemble human speech. Each dog was familiar with either Spanish or Hungarian, but not both. The team concluded that differences in dogs’ anatomical features may affect their ability to distinguish speech from nonspeech.</p>',
            'Which finding from the study, if true, would most directly support the team’s conclusion?',
            [
                'Compared with longer-headed dogs, shorter-headed dogs showed less difference in brain activity when hearing either Spanish or Hungarian than when hearing the scrambled recording.',
                'Compared with longer-headed dogs, shorter-headed dogs showed a greater difference in brain activity when hearing the language they were accustomed to than when hearing the other language.',
                'The pattern of brain activity that long-headed dogs showed when hearing the scrambled recording was different from the pattern of brain activity that short-headed dogs showed when hearing the language they were accustomed to.',
                'Long-headed dogs accustomed to hearing Spanish tended to show more brain activity when hearing Spanish than long-headed dogs accustomed to hearing Hungarian showed when hearing Hungarian.',
            ],
            'A',
            'Tách 2 biến cốt lõi trong kết luận của nhóm nghiên cứu: (1) **khác biệt về đặc điểm giải phẫu của chó** (“differences in dogs’ anatomical features” ↔ chó đầu dài vs. chó đầu ngắn); (2) **khả năng phân biệt tiếng nói với âm thanh không phải tiếng nói** (“distinguish speech from nonspeech” ↔ tiếng Tây Ban Nha/Hungary [speech] vs. bản ghi âm bị xáo trộn [nonspeech]). Chỉ đáp án A kiểm tra đúng cả hai biến: chó đầu ngắn có mức chênh lệch hoạt động não giữa tiếng nói (Spanish/Hungarian) và âm thanh xáo trộn (nonspeech) ít hơn so với chó đầu dài → Chọn A.',
            'Cảnh giác bẫy B cực hay gặp trên SAT Hard: B so sánh “ngôn ngữ quen thuộc vs. ngôn ngữ lạ” (phân biệt HAI NGÔN NGỮ), trong khi kết luận bài đọc là phân biệt “TIẾNG NÓI vs. KHÔNG PHẢI TIẾNG NÓI” (`speech` vs. `scrambled recording`)!',
            [
                ('Đáp án đúng', 'Khớp cả 2 biến trong kết luận: so sánh đặc điểm giải phẫu (chó đầu dài vs. đầu ngắn) dựa trên mức phân biệt não bộ giữa tiếng nói (Spanish/Hungarian) và phi tiếng nói (scrambled recording).'),
                ('Wrong Comparison Pair', 'So sánh ngôn ngữ quen thuộc vs. ngôn ngữ còn lại — tức khả năng phân biệt 2 ngôn ngữ, KHÔNG phải phân biệt “speech” vs. “nonspeech”.'),
                ('Confounded Variables', 'Trộn lẫn cả 2 biến cùng lúc (chó đầu dài nghe âm xáo trộn vs. chó đầu ngắn nghe ngôn ngữ quen), nên không thể tách riêng tác động của hình dạng đầu.'),
                ('Missing Both Key Variables', 'Chỉ xét riêng nhóm chó đầu dài (không so sánh giải phẫu) và chỉ so Spanish vs. Hungarian (không có bản ghi âm nonspeech).'),
            ],
        ),
        _q(
            f'{prefix}_q11', 11, 'Information and Ideas', 'Command of Evidence: Textual', 'Medium',
            '<p>“Poetry” is a 1919 poem by Marianne Moore. The poem highlights an ambivalence toward poetry as the speaker acknowledges its merits while also expressing a sense of displeasure, writing _______</p>',
            'Which quotation from “Poetry” most effectively illustrates the claim?',
            [
                '“nor is it valid / to discriminate against ‘business documents and / school-books’; all these phenomena are important.”',
                '“One must make a distinction / however: when dragged into prominence by half poets, the result is not / poetry”',
                '“when [poems] become so derivative as to become unintelligible, the / same thing may be said for all of us—that we / do not admire what / we cannot understand.”',
                '“Reading [poetry], however, with a perfect contempt for it, one discovers that there is in / it after all, a place for the genuine.”',
            ],
            'D',
            'Nhận định mô tả thái độ nước đôi/mâu thuẫn (“ambivalence”) gồm ĐỒNG THỜI 2 vế: (1) bày tỏ sự khó chịu/chán ghét (“expressing a sense of displeasure” ↔ “with a perfect contempt for it”); và (2) thừa nhận giá trị đích thực của thơ (“acknowledges its merits” ↔ “there is in it after all, a place for the genuine”). Chỉ trích dẫn D chứa trọn vẹn cả hai sắc thái đối lập này → Chọn D.',
            'Từ khóa “ambivalence” luôn đòi hỏi trích dẫn phải thể hiện CẢ HAI MẶT đối lập: chê bai/ghét bỏ (“perfect contempt”) + công nhận giá trị (“a place for the genuine”).',
            [
                ('Missing Ambivalence', 'Chỉ bảo vệ tầm quan trọng của tài liệu thương mại và sách giáo khoa, không thể hiện cảm xúc nước đôi về thơ ca.'),
                ('One-Sided Critique', 'Chỉ phân biệt thơ thật với thứ do “half poets” viết, không đồng thời bộc lộ thái độ chán ghét lẫn công nhận giá trị của thơ.'),
                ('One-Sided Critique', 'Chỉ phê phán những bài thơ bắt chước đến mức khó hiểu, thiếu vế thừa nhận giá trị tích cực của thơ ca.'),
                ('Đáp án đúng', 'Hội tụ trọn vẹn thái độ nước đôi: đọc thơ với “sự khinh ghét tuyệt đối” (“perfect contempt”) nhưng vẫn nhận ra trong đó “chỗ đứng cho những gì chân thực” (“a place for the genuine”).'),
            ],
        ),
        _q(
            f'{prefix}_q12', 12, 'Information and Ideas', 'Command of Evidence: Textual', 'Medium',
            '<p><i>Cane</i> is a 1923 novel by Jean Toomer. In one portion of the novel, Toomer uses figurative language to connect the narrator’s urban environment of Washington, DC, and the rural South of the narrator’s past, writing, _______</p>',
            'Which quotation from <i>Cane</i> most effectively illustrates the claim?',
            [
                '“The [train] engines of this valley have a whistle, the echoes of which sound like iterated gasps and sobs. I always think of them as crude music.”',
                '“I sang, with a strange quiver in my voice, a promise-song.”',
                '“The young trees had not outgrown their [planter] boxes then. V Street [in Washington, DC] was lined with them.”',
                '“And when the wind is from the South, soil of my homeland falls like a fertile shower upon the lean streets of [Washington, DC].”',
            ],
            'D',
            'Nhận định yêu cầu 3 yếu tố cùng lúc: (1) ngôn ngữ hình tượng/ẩn dụ (“figurative language” ↔ “falls like a fertile shower” — phép so sánh); (2) bối cảnh đô thị Washington, DC (“upon the lean streets of [Washington, DC]”); (3) miền Nam nông thôn trong quá khứ người kể chuyện (“when the wind is from the South, soil of my homeland”). Chỉ trích dẫn D kết nối trọn vẹn cả 3 yếu tố này → Chọn D.',
            'Lập bảng kiểm 3 tiêu chí của Claim: `figurative language` + `Washington, DC` + `rural South` — chỉ D đạt 3/3!',
            [
                ('Missing Urban DC', 'Có phép so sánh về tiếng còi tàu trong thung lũng nhưng không hề nhắc tới Washington, DC.'),
                ('Missing Both Places', 'Không nhắc tới Washington, DC lẫn miền Nam nông thôn.'),
                ('Literal / Missing South', 'Mô tả trực tiếp hàng cây non trên phố V ở Washington, DC, không có ngôn ngữ hình tượng nối với miền Nam.'),
                ('Đáp án đúng', 'Dùng phép so sánh giàu hình ảnh (“falls like a fertile shower”) nối đất quê hương miền Nam với những con phố gầy guộc của Washington, DC.'),
            ],
        ),
        _q(
            f'{prefix}_q13', 13, 'Information and Ideas', 'Command of Evidence (Quantitative)', 'Hard',
            _html_table(
                'Simulated Change in Annual Aquifer Input and Irrigation Output if Precipitation Concentration Increases as Climate Models Predict',
                [
                    'Baseline concentration of annual precipitation',
                    '% change in water entering aquifers',
                    '% change in surface water used for irrigation',
                    '% change in groundwater used for irrigation',
                ],
                [
                    ['Precipitation is currently somewhat concentrated', '4.9', '0.4', '0.9'],
                    ['Precipitation is currently evenly distributed', '11.0', '9.0', '7.9'],
                ],
            )
            + _ocr_para(40, 'Some climate models'),
            re.sub(r'\s+', ' ', _OCR_P40_42[40]['prompt']).strip(),
            _ocr_opts(40, [('1f baseline', 'If baseline')]),
            'B',
            'Kết luận của Geeta Persad và cộng sự nhấn mạnh 2 ý: (1) mưa tập trung ít đợt hơn sẽ làm TĂNG tưới tiêu (“triggering more irrigation”), và (2) mức tăng tưới tiêu này “nhạy cảm rất mạnh với mức độ tập trung mưa hiện tại” (“highly sensitive to the baseline concentration”). Đối chiếu bảng: nếu nền mưa hiện tại đã hơi tập trung thì lượng nước tưới chỉ tăng rất nhẹ (+0.4% nước mặt, +0.9% nước ngầm), nhưng nếu nền mưa đang phân bố đều thì lượng nước tưới tăng vọt (+9.0% nước mặt, +7.9% nước ngầm) → Chọn B.',
            'Đề hỏi dữ liệu ủng hộ sự khác biệt về **irrigation output** giữa 2 nhóm baseline: phải so sánh cột *surface water/groundwater used for irrigation* giữa cả 2 hàng bảng (loại A vì so khập khiễng cột irrigation với aquifer, loại C vì chỉ xét 1 hàng, loại D vì sai dấu giảm “decline”).',
            [
                ('Mismatched Metrics', 'So sánh lệch đại lượng: hàng 1 lấy cột nước tưới (0.4%, 0.9%) nhưng hàng 2 lại lấy cột nước ngấm vào tầng chứa (11.0% entering aquifers).'),
                ('Đáp án đúng', 'So sánh trực tiếp mức tăng tưới tiêu giữa 2 nền mưa: chỉ tăng rất nhẹ ở nền “somewhat concentrated” (0.4% / 0.9%) so với tăng mạnh ở nền “evenly distributed” (9.0% / 7.9%).'),
                ('Incomplete Comparison', 'Chỉ nêu số liệu của hàng thứ nhất (nền hơi tập trung), không đối chiếu với hàng thứ hai để chứng minh độ nhạy với nền mưa.'),
                ('Misreads Table Data', 'Đọc sai hoàn toàn dữ liệu bảng: nước tưới KHÔNG hề giảm (“decline”), và 11.0% là cột nước vào tầng chứa chứ không phải surface water.'),
            ],
        ),
        _q(
            f'{prefix}_q14', 14, 'Information and Ideas', 'Inferences', 'Medium',
            '<p>Ships in the British Royal Navy during the Napoleonic Wars (1803–1815) were ranked based on military strength. The system considered the number of a ship’s cannons and decks. “First-rate” was the highest ranking, and “sixth-rate” was the lowest ranking, followed by unranked ships. The size of a ship’s crew was based on this ranking: first-rate ships had between 850 and 875 crewmen, while lower-ranked ships had fewer. Two of the ships in the British Royal Navy from this period were the <i>Boyne</i> (98 cannons and three decks) and the <i>Britannia</i> (120 cannons and three decks). Of these two, only the <i>Britannia</i> was ranked a first-rate ship. It can therefore be concluded that _______</p>',
            'Which choice most logically completes the text?',
            [
                'some ships with three decks had a crew of fewer than 850 people.',
                'the <i>Britannia</i> needed a crew larger than 875 people in order to operate efficiently.',
                'the <i>Boyne</i> had a larger crew than the <i>Britannia</i>.',
                'all ships with at least 98 cannons had a crew of at least 850 people.',
            ],
            'A',
            'Suy luận logic từng bước: (1) Tàu hạng nhất (“first-rate”) có thủy thủ đoàn 850–875 người, còn tàu hạng thấp hơn có ÍT HƠN 850 người; (2) Tàu <i>Boyne</i> có 98 đại bác và 3 boong (“three decks”), nhưng KHÔNG được xếp hạng nhất (chỉ <i>Britannia</i> đạt hạng nhất); (3) Suy ra <i>Boyne</i> thuộc nhóm hạng thấp hơn → thủy thủ đoàn ít hơn 850 người. Vì <i>Boyne</i> có 3 boong và dưới 850 thủy thủ, chắc chắn có một số tàu 3 boong có thủy thủ đoàn ít hơn 850 người → Chọn A.',
            'Lập chuỗi suy luận 3 mắt xích: `Boyne = 3 decks + NOT first-rate` → `lower-ranked` → `< 850 crewmen` → “some ships with three decks had a crew of fewer than 850 people”.',
            [
                ('Đáp án đúng', 'Suy luận chặt chẽ tuyệt đối từ tàu <i>Boyne</i> (có 3 boong, không phải tàu hạng nhất nên có dưới 850 thủy thủ).'),
                ('Contradicts Text', 'Trái dữ kiện: tàu hạng nhất như <i>Britannia</i> có từ 850 đến 875 thủy thủ, không phải nhiều hơn 875.'),
                ('Reverses Comparison', 'Ngược sự thật: <i>Boyne</i> xếp hạng thấp hơn <i>Britannia</i> nên có ít thủy thủ hơn, không phải nhiều hơn.'),
                ('Contradicts Text', 'Bị bác bỏ ngay bởi chính tàu <i>Boyne</i> (có 98 đại bác nhưng lại có dưới 850 thủy thủ).'),
            ],
        ),
        _q(
            f'{prefix}_q15', 15, 'Information and Ideas', 'Inferences', 'Hard',
            _ocr_para(42, 'In a 2018 study', [('together. Zhuang', 'together, Zhuang'), ('suggesting that ~~', 'suggesting that _______')]),
            re.sub(r'\s+', ' ', _OCR_P40_42[42]['prompt']).strip(),
            _ocr_opts(42, [("Jaiswal and Kant's", 'Jaiswal and Kant’s')]),
            'B',
            'Mạch lập luận: (1) Nghiên cứu nhỏ năm 2018 của Jaiswal & Kant (<400 thanh niên ở Ấn Độ) kết luận hiểu biết môi trường KHÔNG ảnh hưởng đến hành vi mua hàng xanh; (2) Giới nghiên cứu nghi ngờ tính đại diện/khái quát (“how reliable and representative”) của kết luận đó; (3) Phân tích tổng hợp 54 nghiên cứu của Zhuang và cộng sự lại tìm thấy tác động TÍCH CỰC rõ rệt. Kết quả trái ngược trên quy mô 54 nghiên cứu chứng tỏ những lo ngại về khả năng áp dụng rộng rãi của nghiên cứu nhỏ Jaiswal & Kant là có cơ sở (“justified”) → Chọn B.',
            'Khi một phân tích tổng hợp (meta-analysis 54 nghiên cứu) cho kết quả trái ngược với một nghiên cứu đơn lẻ bị nghi ngờ về tính đại diện, kết luận logic chặt nhất là: mối nghi ngại về tính khái quát (“broad applicability”) của nghiên cứu nhỏ kia là hoàn toàn có cơ sở!',
            [
                ('Unsupported Detail', 'Đoạn văn chỉ nêu nghiên cứu 202 người là 1 trong 54 nghiên cứu được gộp chung, không hề khẳng định riêng cỡ mẫu 202 là đủ tin cậy.'),
                ('Đáp án đúng', 'Kết quả dương rõ rệt từ tổng hợp 54 nghiên cứu trực tiếp củng cố mối nghi ngại trước đó về tính đại diện rộng rãi của kết luận “không có tác động” từ nghiên cứu nhỏ của Jaiswal & Kant.'),
                ('Out of Scope Comparison', 'Đoạn văn không đưa số liệu cỡ mẫu của “hầu hết các nghiên cứu quyết định mua hàng” (thậm chí còn nhắc 1 nghiên cứu Ấn Độ khác chỉ có 202 người < 400).'),
                ('Unsupported Method Claim', 'Không có bất kỳ thông tin nào so sánh độ chính xác phương pháp luận giữa nghiên cứu Jaiswal & Kant và nghiên cứu năm 2018 ở Indonesia.'),
            ],
        ),
        _q(
            f'{prefix}_q16', 16, 'Standard English Conventions', 'Boundaries', 'Easy',
            '<p>In Norway, the Longyearbyen observatory site monitors activity in the upper atmosphere of the northern _______ in Australia, another observatory site, Buckland Park, monitors the sky of the southern hemisphere. Together, they are part of the Super Dual Auroral Radar Network—or SuperDARN, as space physicists like Tadahiko Ogawa call it.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['hemisphere and', 'hemisphere', 'hemisphere,', 'hemisphere;'],
            'D',
            'Vế trước (“In Norway, the Longyearbyen observatory site monitors activity in the upper atmosphere of the northern hemisphere”) và vế sau (“in Australia, another observatory site, Buckland Park, monitors the sky of the southern hemisphere.”) là HAI MỆNH ĐỀ ĐỘC LẬP có quan hệ song song chặt chẽ. Chỉ dấu chấm phẩy (`;`) ở đáp án D nối hợp lệ hai mệnh đề độc lập này → Chọn D.',
            'Hai mệnh đề độc lập nối với nhau bắt buộc dùng: dấu chấm (`.`), dấu chấm phẩy (`;`), hoặc `, + FANBOYS`. Loại ngay `and` thiếu dấu phẩy (A), nối trần (B) và comma splice (C)!',
            [
                ('Missing Comma Before FANBOYS', 'Nối hai mệnh đề độc lập bằng “and” nhưng thiếu dấu phẩy trước “and”.'),
                ('Run-on / Fused Sentence', 'Ghép trực tiếp hai mệnh đề độc lập không có bất kỳ dấu câu hay từ nối nào.'),
                ('Comma Splice', 'Nối sai hai mệnh đề độc lập chỉ bằng một dấu phẩy đơn.'),
                ('Đáp án đúng', 'Dấu chấm phẩy (“hemisphere;”) nối chuẩn xác hai mệnh đề độc lập song song về đài quan sát ở Bắc và Nam bán cầu.'),
            ],
        ),
        _q(
            f'{prefix}_q17', 17, 'Standard English Conventions', 'Boundaries', 'Medium',
            '<p>Long attributed to Jacques-Louis David, the preeminent Neoclassical painter of his day, the 1801 painting <i>Marie Joséphine Charlotte du Val d’Ognes</i> gained fresh attention in the 1990s when art historians discovered that the painting—which depicts a solitary young woman sketching—was actually the work of little-known French portrait _______ Marie-Denise Villers (1774–1821).</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['artist—', 'artist', 'artist:', 'artist,'],
            'B',
            'Quy tắc Danh xưng/Mô tả nghề nghiệp + Tên riêng (Title/Descriptor + Name): Cụm “of little-known French portrait artist Marie-Denise Villers” KHÔNG có mạo từ xác định (“the” hay “a”) phía trước, nên tên riêng “Marie-Denise Villers” là thành phần THIẾT YẾU (essential) — nếu bỏ đi, cụm “was actually the work of little-known French portrait artist” sẽ sai ngữ pháp vì thiếu mạo từ. Do đó KHÔNG dùng bất kỳ dấu câu nào giữa “artist” và “Marie-Denise Villers” → Chọn B.',
            'Thử che tên riêng đi: “...was actually the work of little-known French portrait artist.” → thiếu mạo từ, câu hỏng! Suy ra tên riêng là thiết yếu → 0 dấu câu!',
            [
                ('Unnecessary Dash', 'Dấu gạch ngang đơn ngắt sai cụm danh từ nghề nghiệp thiết yếu khỏi tên riêng đi liền sau nó.'),
                ('Đáp án đúng', 'Không dùng dấu câu — giữ liền mạch cụm nghề nghiệp không mạo từ “little-known French portrait artist” với tên riêng thiết yếu “Marie-Denise Villers”.'),
                ('Illegal Colon', 'Phần trước dấu hai chấm (“...was actually the work of little-known French portrait artist”) chưa phải mệnh đề độc lập hoàn chỉnh nên cấm đặt dấu hai chấm.'),
                ('False Nonessential Comma', 'Dấu phẩy biến tên riêng thành thông tin thừa, làm phần trước thiếu mạo từ sai ngữ pháp.'),
            ],
        ),
        _q(
            f'{prefix}_q18', 18, 'Standard English Conventions', 'Boundaries', 'Hard',
            '<p>Along the hallowed walls of New York City’s Museum of Modern Art hangs 24.5-by-34.5-inch oil _______ which was created in 1964 by American artist Vija Celmins.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            [
                'painting <i>Gun with Hand #1</i>',
                'painting, <i>Gun with Hand #1</i>,',
                'painting <i>Gun with Hand #1</i>,',
                'painting, <i>Gun with Hand #1</i>',
            ],
            'C',
            'Kết hợp 2 quy tắc Boundaries: (1) Chủ ngữ đảo đứng sau động từ “hangs” là cụm “24.5-by-34.5-inch oil painting <i>Gun with Hand #1</i>” — KHÔNG có mạo từ (“the/a”) trước “24.5-by-34.5-inch oil painting” nên tên tranh <i>Gun with Hand #1</i> là thành phần THIẾT YẾU → KHÔNG đặt dấu phẩy sau “painting” (loại B và D); (2) Mệnh đề quan hệ không xác định “which was created in 1964...” BẮT BUỘC phải có dấu phẩy mở trước “which” (loại A) → Chọn C.',
            'Tách riêng 2 vị trí dấu phẩy để đỡ rối: (1) Trước tên tác phẩm không có mạo từ `the/a` → 0 dấu phẩy; (2) Trước mệnh đề bổ sung `which...` → BẮT BUỘC có dấu phẩy!',
            [
                ('Missing Comma Before Which', 'Đúng ở chỗ không đặt phẩy sau “painting”, nhưng lại thiếu dấu phẩy bắt buộc trước mệnh đề quan hệ không xác định “which was created...”.'),
                ('False Nonessential Title', 'Đặt sai dấu phẩy sau “painting” khiến cụm “hangs 24.5-by-34.5-inch oil painting” bị sai ngữ pháp vì thiếu mạo từ.'),
                ('Đáp án đúng', 'Không đặt phẩy giữa danh từ không mạo từ và tên tác phẩm thiết yếu (“painting <i>Gun with Hand #1</i>”), đồng thời có đủ dấu phẩy mở trước “which”.'),
                ('Double Punctuation Error', 'Vừa thừa dấu phẩy sau “painting” vừa thiếu dấu phẩy trước “which”.'),
            ],
        ),
        _q(
            f'{prefix}_q19', 19, 'Standard English Conventions', 'Form, Structure, and Sense', 'Medium',
            '<p>Legal scholars James Melton and Tom Ginsburg’s analysis of de jure judicial independence and its growth over decades _______ six constitutional features that enhance such independence, including judicial tenure and selection procedure. Romania’s constitution contains one of these features.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['have identified', 'identifies', 'are identifying', 'identify'],
            'B',
            'Xác định đúng danh từ chủ ngữ cốt lõi: “Legal scholars James Melton and Tom Ginsburg’s” chỉ là cụm SỞ HỮU CÁCH bổ nghĩa, còn “of de jure judicial independence and its growth over decades” là cụm giới từ. Chủ ngữ chính là danh từ số ít **“analysis”** (bản phân tích) → cần động từ chia SỐ ÍT. Trong 4 đáp án, A (`have identified`), C (`are identifying`), D (`identify`) đều là số nhiều; duy nhất B (`identifies`) là số ít → Chọn B.',
            'Mẹo “3 số nhiều vs. 1 số ít” cực nhanh trên SAT: quét 4 động từ thấy 3 số nhiều + 1 số ít → gần như chắc chắn chủ ngữ thực là danh từ SỐ ÍT bị che khuất bởi sở hữu cách (`X and Y’s analysis of...`)!',
            [
                ('Plural Verb Trap', '“have identified” là động từ số nhiều — mắc bẫy tên hai học giả (vốn ở dạng sở hữu cách) hoặc danh từ “decades” trong cụm giới từ.'),
                ('Đáp án đúng', 'Động từ số ít “identifies” hòa hợp chuẩn xác với chủ ngữ số ít “analysis”.'),
                ('Plural Verb Trap', '“are identifying” là động từ số nhiều và sai sắc thái thì (phân tích đã công bố nêu rõ 6 đặc trưng → hiện tại đơn).'),
                ('Plural Verb Trap', '“identify” là động từ số nhiều, không hòa hợp với chủ ngữ số ít “analysis”.'),
            ],
        ),
        _q(
            f'{prefix}_q20', 20, 'Standard English Conventions', 'Boundaries', 'Hard',
            '<p>For Spain, a member of the North Atlantic Treaty Organization (NATO) since 1982, NATO’s principle of collective defense confers both benefits and _______ organization’s many members, nations as disparate as the US and Slovenia, are all bound to defend Spain, the reverse is also true.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['obligations; the', 'obligations. The', 'obligations, while the', 'obligations: while the'],
            'D',
            'CÂU BOUNDARIES BẬC HARD CỰC ĐỈNH! Phân tích kỹ vế sau chỗ trống: có HAI mệnh đề nối với nhau chỉ bằng MỘT DẤU PHẨY sau “Spain,”: `[the organization’s many members... are all bound to defend Spain]`, `[the reverse is also true.]`. Nếu chọn A (`; the`) hoặc B (`. The`), hai mệnh đề độc lập phía sau bị dính lỗi COMMA SPLICE ngay sau “Spain,”! Nếu chọn C (`, while the`), mệnh đề độc lập 1 (“NATO’s principle... confers both benefits and obligations”) lại bị nối chỉ bằng dấu phẩy với cụm `[while DC, IC2]` → vẫn là COMMA SPLICE! Duy nhất D (`: while the`) dùng dấu hai chấm sau mệnh đề độc lập 1 để giải thích chính xác “both benefits and obligations”, theo sau là cấu trúc chuẩn `[while DC, IC2]` → Chọn D.',
            'Thấy mô hình `[IC1] ___ [Mệnh đề 2a], [IC2b].`: muốn tránh comma splice ở cả hai dấu ngăn, cần dấu hai chấm (`:`) + liên từ phụ thuộc (`while`) để biến Mệnh đề 2a thành mệnh đề phụ thuộc mở đầu cho IC2b!',
            [
                ('Hidden Comma Splice', 'Không có liên từ phụ thuộc “while” nên phần sau dấu chấm phẩy bị lỗi comma splice giữa “...are all bound to defend Spain” và “the reverse is also true”.'),
                ('Hidden Comma Splice', 'Tương tự A: câu thứ hai không có “while” nên hai mệnh đề độc lập bị nối sai bằng dấu phẩy sau “Spain,”.'),
                ('Comma Splice Trap', 'Bẫy rất dễ dính: dùng `, while` không đủ sức ngăn cách mệnh đề độc lập đầu câu (“...confers both benefits and obligations”) với mệnh đề độc lập cuối câu (“the reverse is also true”).'),
                ('Đáp án đúng', 'Dấu hai chấm đặt sau mệnh đề độc lập mở ra phần giải thích “both benefits and obligations”, và “while...” làm mệnh đề phụ thuộc hợp lệ cho “the reverse is also true”.'),
            ],
        ),
        _q(
            f'{prefix}_q21', 21, 'Standard English Conventions', 'Boundaries', 'Hard',
            '<p>As of 2017, Italy’s top tax rate of 55% was lower than the country’s Laffer curve peak (70%). To some economists, whether a tax cut will ultimately increase Italy’s tax revenue is dependent on the country’s position on the Laffer _______ a theoretical relationship between tax rates and revenues, the curve was famously sketched on a napkin by economist Arthur Laffer in 1974.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['curve', 'curve;', 'curve, which is', 'curve,'],
            'B',
            'Đọc xuyên qua cụm đồng vị ngữ ở giữa tới cuối câu: “**the curve was famously sketched on a napkin by economist Arthur Laffer in 1974.**” là một MỆNH ĐỀ ĐỘC LẬP mới toanh! Còn “a theoretical relationship between tax rates and revenues,” là cụm đồng vị ngữ mở đầu bổ nghĩa cho chủ ngữ “the curve” của mệnh đề độc lập 2. Vì phía trước cũng là mệnh đề độc lập 1 (“To some economists, whether a tax cut... is dependent on the country’s position on the Laffer curve”), ta BẮT BUỘC phải tách hai mệnh đề độc lập bằng dấu chấm phẩy (`curve;`). Nếu chọn C hay D sẽ dính lỗi COMMA SPLICE ngay sau “revenues,” → Chọn B.',
            'Bẫy SAT kinh điển `[IC1] ___ [Cụm đồng vị ngữ], [IC2]`: đừng vội tưởng cụm đồng vị ngữ gắn với danh từ cuối của IC1! Hễ sau dấu phẩy thấy một chủ ngữ + động từ mới (“the curve was sketched...”) → phải đặt dấu chấm phẩy (`;`) TRƯỚC cụm đồng vị ngữ!',
            [
                ('Run-on / Fused Sentence', 'Không có dấu câu nào tách IC1 với phần mệnh đề 2 phía sau.'),
                ('Đáp án đúng', 'Dấu chấm phẩy (“curve;”) tách rạch ròi IC1 khỏi IC2 (“a theoretical relationship..., the curve was famously sketched...”).'),
                ('Comma Splice Trap', 'Kéo cụm “which is a theoretical relationship...” gắn vào IC1 khiến IC2 (“the curve was famously sketched...”) bị nối sai bằng dấu phẩy đơn.'),
                ('Comma Splice Trap', 'Đặt dấu phẩy đơn sau “curve” dẫn đến lỗi comma splice nối hai mệnh đề độc lập.'),
            ],
        ),
        _q(
            f'{prefix}_q22', 22, 'Expression of Ideas', 'Transitions', 'Easy',
            '<p>Working together with the Navajo Nation Department of Water Resources, Dr. Lani Tsinnajinnie analyzed data about snowpack levels in the Chuska Mountains. She found that the snowpack (the amount of snow on the ground) was deepest in early March at lower elevations. At higher elevations, _______ the snowpack was deepest in mid-March.</p>',
            'Which choice completes the text with the most logical transition?',
            ['in other words,', 'for instance,', 'on the other hand,', 'in summary,'],
            'C',
            'Quan hệ đối chiếu giữa hai mức độ cao: ở độ cao thấp hơn (“at lower elevations”), lớp tuyết dày nhất vào đầu tháng 3 (“early March”); còn ở độ cao lớn hơn (“At higher elevations”), lớp tuyết lại dày nhất vào giữa tháng 3 (“mid-March”). Cần từ nối đối chiếu “on the other hand,” (mặt khác / ngược lại) → Chọn C.',
            'Cặp cụm đối chiếu địa điểm/nhóm `at lower elevations ...` vs. `At higher elevations, ...` là tín hiệu cực rõ của “on the other hand,” / “by contrast,”.',
            [
                ('Wrong Relationship', 'in other words = nói cách khác — câu sau đưa kết quả khác cho độ cao lớn hơn, không phải diễn giải lại câu trước.'),
                ('Wrong Relationship', 'for instance = ví dụ — vùng núi cao không phải ví dụ minh họa cho vùng núi thấp.'),
                ('Đáp án đúng', 'on the other hand = mặt khác — đối chiếu chuẩn xác thời điểm tuyết dày nhất giữa độ cao thấp (đầu tháng 3) và độ cao cao (giữa tháng 3).'),
                ('Wrong Relationship', 'in summary = tóm lại — câu sau nêu thêm dữ liệu đối lập chứ không tổng kết đoạn.'),
            ],
        ),
        _q(
            f'{prefix}_q23', 23, 'Expression of Ideas', 'Transitions', 'Medium',
            '<p>Biographer Michael Gorra notes that the novelist Henry James “lived in a world of second thoughts,” frequently tinkering with his novels and stories after their initial publication. However, the differences between the 1881 first edition and the 1908 edition of his novel <i>A Portrait of a Lady</i> are extreme, even by James’s standards; _______ some critics regard the two editions as two different novels altogether.</p>',
            'Which choice completes the text with the most logical transition?',
            ['by contrast,', 'in fact,', 'nevertheless,', 'in other words,'],
            'B',
            'Vế trước dấu chấm phẩy nhận định mức độ khác biệt giữa ấn bản 1881 và 1908 là “cực độ, ngay cả theo tiêu chuẩn của chính James” (“are extreme, even by James’s standards”). Vế sau tăng cường mức độ nhấn mạnh bằng một thực tế còn mạnh hơn: “một số nhà phê bình coi hai ấn bản như hai cuốn tiểu thuyết hoàn toàn khác nhau” → cần từ nối nhấn mạnh/tăng tiến “in fact,” (trên thực tế / thậm chí) → Chọn B.',
            'Khi vế sau đẩy lập luận vế trước lên mức mạnh hơn (extreme differences → regarded as two different novels altogether), chọn “in fact,” / “indeed,” (tránh “in other words,” vốn chỉ dùng để định nghĩa/diễn đạt lại cùng một nội dung).',
            [
                ('False Contrast', 'by contrast = ngược lại — vế sau củng cố thêm ý vế trước, hoàn toàn không đối lập.'),
                ('Đáp án đúng', 'in fact = trên thực tế — tăng cường và minh họa rõ mức độ “cực độ” của sự khác biệt giữa hai ấn bản.'),
                ('False Contrast', 'nevertheless = tuy nhiên — sai chiều logic vì không có sự nhượng bộ hay đảo chiều ý.'),
                ('Restatement Trap', 'in other words = nói cách khác — vế sau đưa thêm nhận định cụ thể của giới phê bình (xem như 2 tiểu thuyết khác nhau), không đơn thuần diễn đạt lại mệnh đề trước.'),
            ],
        ),
        _q(
            f'{prefix}_q24', 24, 'Expression of Ideas', 'Transitions', 'Easy',
            '<p>Scientists studying asteroid deflection have focused on secondary objects such as S/2020 (2013 PY6), a moonlet orbiting the near-Earth asteroid 2013 PY6. In 2022 NASA intentionally crashed a probe into just such an object, successfully altering its orbit. Scientists have yet to demonstrate, _______ that 2013 PY6 and other primary objects would be similarly affected.</p>',
            'Which choice completes the text with the most logical transition?',
            ['for example,', 'though,', 'likewise,', 'moreover,'],
            'B',
            'Quan hệ tương phản rõ nét giữa câu 2 và câu 3: NASA đã THÀNH CÔNG (“successfully altering its orbit”) trong việc làm lệch quỹ đạo một thiên thể phụ (vệ tinh nhỏ), NHƯNG các nhà khoa học VẪN CHƯA CHỨNG MINH ĐƯỢC (“have yet to demonstrate”) rằng thiên thể chính như 2013 PY6 cũng sẽ chịu tác động tương tự → cần từ nối đối lập đặt giữa câu “though,” (tuy nhiên) → Chọn B.',
            'Cặp đối lập `successfully altering [secondary object]` ↔ `have yet to demonstrate [primary objects]` gọi thẳng từ nối tương phản “though,” / “however,”.',
            [
                ('Wrong Relationship', 'for example = ví dụ — câu 3 nêu giới hạn chưa được chứng minh, không phải ví dụ cho thành công năm 2022.'),
                ('Đáp án đúng', 'though = tuy nhiên — nối chính xác sự đối lập giữa thành công trên thiên thể phụ với việc chưa chứng minh được trên thiên thể chính.'),
                ('False Similarity', 'likewise = tương tự — ngược nghĩa vì các nhà khoa học chưa chứng minh điều tương tự xảy ra với thiên thể chính.'),
                ('Wrong Relationship', 'moreover = hơn nữa — dùng để bổ sung ý cùng chiều, không hợp ngữ cảnh đối lập “have yet to demonstrate”.'),
            ],
        ),
        _q(
            f'{prefix}_q25', 25, 'Expression of Ideas', 'Rhetorical Synthesis', 'Easy',
            '<p>While researching a topic, a student has taken the following notes:</p><ul><li>Documentary TV programs in the slow TV genre consist of uninterrupted broadcasts of ordinary events in real time.</li><li><i>Nordlandsbanen: Minutt for Minutt</i> is a Norwegian slow TV program.</li><li>The 10-hour-long program documented a train ride from Trondheim to Bodø.</li><li>It first aired in 2012.</li><li>In her book <i>Spectacular Television: Exploring Televisual Pleasure</i>, British film scholar Helen Wheatley writes that slow TV “offers ‘unspectacular’ spectacle.”</li></ul>',
            'The student wants to provide a specific example of a slow TV program. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
            [
                'British film scholar Helen Wheatley writes about the slow TV genre in her book <i>Spectacular Television: Exploring Televisual Pleasure</i>.',
                'An example of the slow TV genre can be seen in <i>Nordlandsbanen: Minutt for Minutt</i>, a 2012 Norwegian show featuring an uninterrupted 10-hour real-time broadcast of a train ride from Trondheim to Bodø.',
                'Slow TV programs provide uninterrupted broadcasts of ordinary events, such as train rides, in real time.',
                'With their uninterrupted broadcasts, slow TV programs offer what film scholar Helen Wheatley calls the “‘unspectacular’ spectacle” of ordinary events occurring in real time.',
            ],
            'B',
            'Mục tiêu (Goal): Đưa ra MỘT VÍ DỤ CỤ THỂ về một chương trình slow TV (“provide a specific example of a slow TV program”). Chỉ duy nhất đáp án B nêu tên chương trình cụ thể (<i>Nordlandsbanen: Minutt for Minutt</i>) cùng đầy đủ thông tin đặc trưng (chương trình Na Uy năm 2012, phát sóng liên tục 10 giờ theo thời gian thực chuyến tàu từ Trondheim đến Bodø) → Chọn B.',
            'Goal yêu cầu “a specific example of a slow TV program” → tìm ngay đáp án có TÊN RIÊNG chương trình cụ thể (<i>Nordlandsbanen: Minutt for Minutt</i>).',
            [
                ('Wrong Synthesis Goal', 'Chỉ giới thiệu sách của học giả Helen Wheatley, không nêu ví dụ chương trình slow TV nào.'),
                ('Đáp án đúng', 'Cung cấp trực tiếp ví dụ cụ thể là chương trình Na Uy <i>Nordlandsbanen: Minutt for Minutt</i> (2012) cùng mô tả 10 giờ phát sóng thời gian thực.'),
                ('Too General', 'Chỉ định nghĩa thể loại slow TV và nhắc chung chung “chuyến tàu”, không nêu tên chương trình cụ thể nào.'),
                ('Wrong Synthesis Goal', 'Chỉ trích dẫn nhận xét của Helen Wheatley về thể loại slow TV nói chung, thiếu ví dụ chương trình cụ thể.'),
            ],
        ),
        _q(
            f'{prefix}_q26', 26, 'Expression of Ideas', 'Rhetorical Synthesis', 'Easy',
            '<ul><li>Calida Garcia Rawles is an African American painter.</li><li>She is known for her large-scale, hyperrealistic paintings depicting African American figures in water.</li><li>The painting <i>Lightness of Being</i> (24 × 30 in) depicts a young man with his arms outstretched floating on the right side of the canvas.</li><li><i>Lost in the Shuffle</i> (36 × 24 in) depicts two young men with their arms outstretched floating in the bottom left and upper right corners of the canvas.</li><li>She paints the water with vivid blue colors, including periwinkle and cobalt.</li><li>The mood in the paintings is placid.</li></ul>',
            'Which choice most effectively uses information from the given sentences to emphasize the location of the figures in <i>Lost in the Shuffle</i>?',
            [
                'While the number of figures may differ, constant among Rawles’s hyperrealistic works is the placid mood that the paintings evoke.',
                'In Rawles’s painting <i>Lost in the Shuffle</i>, two young men are depicted in the bottom left and upper right corners of the canvas.',
                'At 36 by 24 inches, Rawles’s <i>Lost in the Shuffle</i> is even larger than the sizable 24-by-30-inch painting <i>Lightness of Being</i>.',
                'Rawles captures the water in paintings such as <i>Lightness of Being</i> and <i>Lost in the Shuffle</i> in vivid hues of periwinkle and cobalt.',
            ],
            'B',
            'Mục tiêu (Goal): Nhấn mạnh VỊ TRÍ CỦA CÁC NHÂN VẬT trong bức <i>Lost in the Shuffle</i> (“emphasize the location of the figures in <i>Lost in the Shuffle</i>”). Chỉ duy nhất đáp án B nêu đúng tên bức tranh và vị trí chính xác của hai chàng trai trên khung vải (“in the bottom left and upper right corners of the canvas”) → Chọn B.',
            'Khóa 2 từ khóa của Goal: `location of the figures` + `Lost in the Shuffle` → đối chiếu thẳng với “bottom left and upper right corners of the canvas”.',
            [
                ('Wrong Attribute', 'Chỉ nhấn mạnh sắc thái bình lặng (“placid mood”) chung của các tác phẩm, không nêu vị trí nhân vật.'),
                ('Đáp án đúng', 'Nêu chính xác vị trí của hai nhân vật nam trong bức <i>Lost in the Shuffle</i> (góc dưới bên trái và góc trên bên phải khung vải).'),
                ('Wrong Attribute', 'So sánh kích thước khung tranh giữa hai bức họa, không đề cập vị trí nhân vật.'),
                ('Wrong Attribute', 'Chỉ tập trung vào bảng màu xanh lam của mặt nước (periwinkle và cobalt), không nói về vị trí nhân vật.'),
            ],
        ),
        _q(
            f'{prefix}_q27', 27, 'Expression of Ideas', 'Rhetorical Synthesis', 'Medium',
            '<ul><li>Jean-Michel Basquiat was an American artist who produced more than two thousand drawings and paintings.</li><li>Most of his works were completed in New York City in the 1980s.</li><li>His work <i>Mater</i> was completed in 1982.</li><li>The work is composed of acrylic and oil stick on canvas and measures 72 inches by 84 inches.</li><li><i>Mater</i> was purchased by a private collection for $5.8 million in a 2009 auction.</li></ul>',
            'Which choice most effectively uses information from the given sentences to emphasize the scope of Basquiat’s work?',
            [
                '<i>Mater</i> is just one of more than two thousand drawings and paintings completed by American artist Jean-Michel Basquiat.',
                'Though artist Jean-Michel Basquiat completed most of his two thousand–plus drawings in the 1980s, his work <i>Mater</i> is composed of acrylic and oil stick on canvas.',
                'At a 2009 auction, artist Jean-Michel Basquiat’s <i>Mater</i>, composed of acrylic and oil stick on canvas, sold for $5.8 million.',
                'Decades after artist Jean-Michel Basquiat completed his 1982 work <i>Mater</i>, a private collection purchased it for $5.8 million.',
            ],
            'A',
            'Mục tiêu (Goal): Nhấn mạnh QUY MÔ / PHẠM VI SÁNG TÁC của Basquiat (“emphasize the scope of Basquiat’s work” — tức số lượng đồ sộ hơn hai nghìn bức vẽ và tranh). C và D không hề đề cập con số hơn 2.000 tác phẩm. So sánh A và B: B vừa đẩy chi tiết số lượng xuống mệnh đề nhượng bộ phụ “Though...” vô nghĩa (và bỏ sót “paintings”), vừa dồn trọng tâm mệnh đề chính sang chất liệu của bức <i>Mater</i>; còn A đặt trọn điểm nhấn vào cụm “just one of more than two thousand drawings and paintings” để làm nổi bật quy mô sáng tác đồ sộ của ông → Chọn A.',
            'Cảnh giác bẫy B trong dạng “emphasize X”: mệnh đề phụ bắt đầu bằng “Though...” làm GIẢM nhẹ (subordinate) thông tin cần nhấn mạnh, còn mệnh đề chính mới là nơi đặt trọng tâm!',
            [
                ('Đáp án đúng', 'Dùng cấu trúc nhấn mạnh sắc nét (“is just one of more than two thousand drawings and paintings”) để làm nổi bật quy mô sáng tác khổng lồ của Basquiat.'),
                ('Wrong Emphasis & Inaccurate', 'Hạ thấp quy mô sáng tác vào mệnh đề phụ “Though...” (lại bỏ sót “paintings”), chuyển trọng tâm sang chất liệu acrylic và oil stick của bức <i>Mater</i>.'),
                ('Missing Scope', 'Chỉ nhấn mạnh chất liệu và giá đấu giá $5.8 million năm 2009, không đề cập quy mô toàn bộ sự nghiệp.'),
                ('Missing Scope', 'Chỉ nhấn mạnh mốc thời gian mua đấu giá $5.8 million sau nhiều thập kỷ, không nhắc quy mô sáng tác.'),
            ],
        ),
    ]


# ============================================================================
# FULL BLUEBOOK TEST DATA EXPORT (54 UNIQUE REAL Qs — routingThreshold: 0)
# ============================================================================

_M1_QUESTIONS = get_m1_questions()
_M2_HARD_QUESTIONS = get_m2_questions(prefix='june2025_us_v1_rw_m2h')
_M2_LOWER_QUESTIONS = get_m2_questions(prefix='june2025_us_v1_rw_m2l')

TEST_DATA = {
    'schemaVersion': 1,
    'mode': 'adaptive_mock',
    'section': 'rw',
    'basicInfo': {
        'title': TEST_TITLE,
        'subtitle': 'Đề thi thật Digital SAT Mỹ tháng 6/2025 (US Ver 1) — Đủ 2 Module (M1: 27 câu + M2: 27 câu)',
        'difficultyBadge': 'REAL EXAM • JUNE 2025 US',
        'targetTimeMinutes': 64,
        'routingThreshold': 0,
    },
    'module1': {
        'id': 'june2025_us_v1_rw_m1',
        'title': 'Section 1, Module 1: Reading and Writing',
        'subtitle': 'Module 1 (27 Questions • 32 Minutes)',
        'timeLimitMinutes': 32,
        'questions': _M1_QUESTIONS,
    },
    'module2_hard': {
        'id': 'june2025_us_v1_rw_m2h',
        'title': 'Section 1, Module 2: Reading and Writing',
        'subtitle': 'Module 2 (27 Questions • 32 Minutes)',
        'timeLimitMinutes': 32,
        'questions': _M2_HARD_QUESTIONS,
    },
    'module2_lower': {
        'id': 'june2025_us_v1_rw_m2l',
        'title': 'Section 1, Module 2: Reading and Writing',
        'subtitle': 'Module 2 (27 Questions • 32 Minutes)',
        'timeLimitMinutes': 32,
        'questions': copy.deepcopy(_M2_LOWER_QUESTIONS),
    },
}


# ============================================================================
# SELF-VERIFICATION SUITE
# ============================================================================

VALID_RW_DOMAINS = {
    'Craft and Structure',
    'Information and Ideas',
    'Standard English Conventions',
    'Expression of Ideas',
}

FORBIDDEN_WATERMARKS = ('@DSATuz', '@D7SAT', 'satuzhunters', 'Minh Nghĩa', 't.me/D7SAT', '______blank')


def verify_all():
    """Runs full structural, fidelity, answer-consistency, watermark, and Bluebook pipeline checks."""
    try:
        from scripts.sat_real_exams_pipeline import validate_sat_bluebook_json
    except ImportError:
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        from sat_real_exams_pipeline import validate_sat_bluebook_json

    errors = []
    seen_ids = set()

    if TEST_DATA.get('mode') != 'adaptive_mock':
        errors.append(f'Expected mode=adaptive_mock, got {TEST_DATA.get("mode")}')
    if TEST_DATA.get('section') != 'rw':
        errors.append(f'Expected section=rw, got {TEST_DATA.get("section")}')
    if TEST_DATA.get('basicInfo', {}).get('routingThreshold') != 0:
        errors.append(f'Expected routingThreshold=0, got {TEST_DATA.get("basicInfo", {}).get("routingThreshold")}')

    for mod_key in ('module1', 'module2_hard', 'module2_lower'):
        mod = TEST_DATA.get(mod_key)
        if not mod:
            errors.append(f'Missing module: {mod_key}')
            continue
        if mod.get('timeLimitMinutes') != 32:
            errors.append(f'{mod_key}: expected timeLimitMinutes=32, got {mod.get("timeLimitMinutes")}')
        qs = mod.get('questions') or []
        if len(qs) != 27:
            errors.append(f'{mod_key}: expected 27 questions, got {len(qs)}')

        for idx, q in enumerate(qs, start=1):
            qid = q.get('id')
            if not qid or qid in seen_ids:
                errors.append(f'{mod_key} Q{idx}: missing or duplicate id {qid}')
            seen_ids.add(qid)

            if q.get('number') != idx:
                errors.append(f'{mod_key} Q{idx}: number={q.get("number")} != {idx}')
            if q.get('domain') not in VALID_RW_DOMAINS:
                errors.append(f'{mod_key} Q{idx}: invalid domain {q.get("domain")}')
            if not (q.get('skill') or '').strip():
                errors.append(f'{mod_key} Q{idx}: missing skill')
            if q.get('difficulty') not in ('Easy', 'Medium', 'Hard'):
                errors.append(f'{mod_key} Q{idx}: invalid difficulty {q.get("difficulty")}')

            ans = q.get('correctAnswer')
            if ans not in ('A', 'B', 'C', 'D'):
                errors.append(f'{mod_key} Q{idx}: invalid correctAnswer {ans}')

            exp = q.get('explanation') or {}
            if not (exp.get('summaryVi') or '').strip():
                errors.append(f'{mod_key} Q{idx}: empty summaryVi')
            if not (exp.get('keyTakeaway') or '').strip():
                errors.append(f'{mod_key} Q{idx}: empty keyTakeaway')
            if f'Chọn {ans}' not in (exp.get('summaryVi') or ''):
                errors.append(f'{mod_key} Q{idx}: summaryVi does not confirm "Chọn {ans}"')

            oa = exp.get('optionAnalysis') or {}
            correct_labels = []
            trap_labels = []
            for lbl in ('A', 'B', 'C', 'D'):
                item = oa.get(lbl)
                if not item:
                    errors.append(f'{mod_key} Q{idx}: missing optionAnalysis[{lbl}]')
                    continue
                st = item.get('status')
                if st == 'correct':
                    correct_labels.append(lbl)
                elif st == 'trap':
                    trap_labels.append(lbl)
                else:
                    errors.append(f'{mod_key} Q{idx}: invalid optionAnalysis[{lbl}].status={st}')
                if not (item.get('reasonVi') or '').strip():
                    errors.append(f'{mod_key} Q{idx}: empty optionAnalysis[{lbl}].reasonVi')

            if correct_labels != [ans] or len(trap_labels) != 3:
                errors.append(
                    f'{mod_key} Q{idx}: answer mismatch correctAnswer={ans}, '
                    f'correct_labels={correct_labels}, trap_labels={trap_labels}'
                )

    # Verify M2 hard & lower have identical 27 question contents
    m2h = TEST_DATA['module2_hard']['questions']
    m2l = TEST_DATA['module2_lower']['questions']
    if len(m2h) == len(m2l):
        for i, (qh, ql) in enumerate(zip(m2h, m2l), start=1):
            if qh['stimulusHtml'] != ql['stimulusHtml'] or qh['correctAnswer'] != ql['correctAnswer']:
                errors.append(f'module2_hard vs module2_lower mismatch at Q{i}')

    # Unique count: 27 M1 + 27 M2 = 54
    unique_real_qs = len(TEST_DATA['module1']['questions']) + len(TEST_DATA['module2_hard']['questions'])
    if unique_real_qs != 54:
        errors.append(f'Expected 54 unique real questions (27 + 27), got {unique_real_qs}')

    # Zero watermark check across entire serialized TEST_DATA
    raw_blob = str(TEST_DATA)
    for bad in FORBIDDEN_WATERMARKS:
        if bad.lower() in raw_blob.lower():
            errors.append(f'Leaked watermark/artifact token detected: "{bad}"')

    pipeline_errs = validate_sat_bluebook_json(TEST_DATA, TEST_CODE)
    errors.extend(pipeline_errs)

    if errors:
        print(f'[FAIL] {TEST_CODE}: {len(errors)} error(s):')
        for e in errors:
            print('  -', e)
        sys.exit(1)

    print(f'[PASS] {TEST_CODE} — 0 errors!')
    print(f'       Title: {TEST_TITLE}')
    print(f'       Unique Real Questions: {unique_real_qs} (M1: 27 + M2: 27; total unique IDs across slots: {len(seen_ids)})')
    for mod_key in ('module1', 'module2_hard', 'module2_lower'):
        qs = TEST_DATA[mod_key]['questions']
        dist = {c: sum(1 for q in qs if q['correctAnswer'] == c) for c in 'ABCD'}
        doms = {}
        for q in qs:
            doms[q['domain']] = doms.get(q['domain'], 0) + 1
        print(f'       {mod_key:13s}: {len(qs)} Qs | Keys={dist} | Domains={doms}')


if __name__ == '__main__':
    verify_all()
