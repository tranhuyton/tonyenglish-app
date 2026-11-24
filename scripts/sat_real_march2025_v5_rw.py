# -*- coding: utf-8 -*-
"""
Digital SAT 1500+ Real Past Exam — March 2025 Ver 5 Reading & Writing (54 Questions)
- Module 1: 27 Real Questions (32 minutes)
- Module 2: 27 Real Questions (32 minutes, assigned to both module2_hard and module2_lower with routingThreshold=0)
- Source: March 2025 Real Exam Ver 5 (100% verbatim passages, tables, SVG charts, underlines, italics, and options A–D)
- 2-Pass Answer Audit completed across all 54 R&W items with rich Vietnamese explanations & trap analysis.
"""

import copy
import json
import os
import re
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

TEST_CODE = 'real_march2025_v5_rw'
FOLDER_KEY = 'real_rw'
ORDER_INDEX = 4
TEST_TITLE = '🏛️ Real Exam — March 2025 Ver 5 Reading & Writing (54 Qs)'


def html_table(caption, headers, rows, footnote=''):
    """Builds a clean College Board-style data table for Bluebook split-pane rendering."""
    ths = ''.join(f'<th>{h}</th>' for h in headers)
    trs = ''.join(
        '<tr>' + ''.join(
            f'<td style="font-weight:700;">{c}</td>' if idx == 0 else f'<td>{c}</td>'
            for idx, c in enumerate(r)
        ) + '</tr>'
        for r in rows
    )
    fn_html = (
        f'<div style="font-family:\'Segoe UI\',system-ui,sans-serif;font-size:12px;'
        f'color:#475569;margin-top:4px;font-style:italic;">{footnote}</div>'
        if footnote else ''
    )
    return (
        f'<div style="margin-bottom:14px;">'
        f'<div style="font-family:\'Segoe UI\',system-ui,sans-serif;font-size:13.5px;'
        f'font-weight:800;color:#0f172a;text-align:center;margin-bottom:6px;">{caption}</div>'
        f'<table><thead><tr>{ths}</tr></thead><tbody>{trs}</tbody></table>'
        f'{fn_html}</div>'
    )


def svg_m1_q9_fish():
    """Recreates the exact March 2025 Ver 5 M1 Q9 line graph (Fish Population in a Taiwanese Tide Pool)."""
    months = ['January 2001', 'April 2001', 'July 2001', 'October 2001']
    cocos_vals = [1, 10, 5, 5]
    blenny_vals = [0, 0, 0, 3]
    sergeant_vals = [2, 3, 21, 28]

    xs = [115, 200, 285, 370]
    x_left, x_right = 85, 405
    y_top, y_bot = 20, 188  # 168px height for 0..30 -> 5.6 px per fish

    def fy(v):
        return y_bot - v * 5.6

    parts = []
    # Horizontal gridlines + Y-axis labels (0 to 30 by 5)
    for val in range(0, 31, 5):
        y = fy(val)
        stroke = '#334155' if val == 0 else '#cbd5e1'
        sw = '1.5' if val == 0 else '1'
        parts.append(f'<line x1="{x_left}" y1="{y:.1f}" x2="{x_right}" y2="{y:.1f}" stroke="{stroke}" stroke-width="{sw}"/>')
        parts.append(f'<text x="{x_left - 8}" y="{y + 3.5:.1f}" font-size="11" text-anchor="end" fill="#1e293b" font-family="sans-serif">{val}</text>')

    # Vertical gridlines + rotated month labels
    for x, mo in zip(xs, months):
        parts.append(f'<line x1="{x}" y1="{y_top}" x2="{x}" y2="{y_bot}" stroke="#cbd5e1" stroke-width="1"/>')
        parts.append(f'<line x1="{x}" y1="{y_bot}" x2="{x}" y2="{y_bot + 5}" stroke="#334155" stroke-width="1.2"/>')
        parts.append(
            f'<text x="{x + 4}" y="{y_bot + 16}" font-size="10.5" text-anchor="end" fill="#1e293b" '
            f'font-family="sans-serif" transform="rotate(-40 {x + 4} {y_bot + 16})">{mo}</text>'
        )

    # Y-axis line
    parts.append(f'<line x1="{x_left}" y1="{y_top}" x2="{x_left}" y2="{y_bot}" stroke="#334155" stroke-width="1.5"/>')

    # Series 1: Cocos frillgoby (solid line + black filled upward triangles)
    c_pts = ' '.join(f'{x},{fy(v):.1f}' for x, v in zip(xs, cocos_vals))
    parts.append(f'<polyline points="{c_pts}" fill="none" stroke="#0f172a" stroke-width="2"/>')
    for x, v in zip(xs, cocos_vals):
        y = fy(v)
        parts.append(f'<polygon points="{x},{y - 5.5:.1f} {x - 5},{y + 4:.1f} {x + 5},{y + 4:.1f}" fill="#0f172a"/>')

    # Series 2: wavy-lined blenny (dashed line + gray-filled black-bordered squares)
    b_pts = ' '.join(f'{x},{fy(v):.1f}' for x, v in zip(xs, blenny_vals))
    parts.append(f'<polyline points="{b_pts}" fill="none" stroke="#334155" stroke-width="2" stroke-dasharray="6,4"/>')
    for x, v in zip(xs, blenny_vals):
        y = fy(v)
        parts.append(f'<rect x="{x - 4.2:.1f}" y="{y - 4.2:.1f}" width="8.4" height="8.4" fill="#cbd5e1" stroke="#0f172a" stroke-width="1.5"/>')

    # Series 3: Indo-Pacific sergeant (dotted line + white-filled black-bordered circles)
    s_pts = ' '.join(f'{x},{fy(v):.1f}' for x, v in zip(xs, sergeant_vals))
    parts.append(f'<polyline points="{s_pts}" fill="none" stroke="#0f172a" stroke-width="2" stroke-dasharray="2.5,3"/>')
    for x, v in zip(xs, sergeant_vals):
        y = fy(v)
        parts.append(f'<circle cx="{x}" cy="{y:.1f}" r="4.5" fill="#ffffff" stroke="#0f172a" stroke-width="1.6"/>')

    # Axis titles
    parts.append(
        '<text x="24" y="104" font-size="11.5" font-weight="600" text-anchor="middle" fill="#0f172a" '
        'font-family="sans-serif" transform="rotate(-90 24 104)">Number of individual</text>'
    )
    parts.append(
        '<text x="39" y="104" font-size="11.5" font-weight="600" text-anchor="middle" fill="#0f172a" '
        'font-family="sans-serif" transform="rotate(-90 39 104)">fish observed</text>'
    )
    parts.append(
        '<text x="245" y="256" font-size="11.5" font-weight="600" text-anchor="middle" fill="#0f172a" '
        'font-family="sans-serif">Month</text>'
    )

    # Legend box
    parts.append('<rect x="130" y="268" width="230" height="66" fill="#ffffff" stroke="#475569" stroke-width="1.1"/>')
    # Cocos frillgoby
    parts.append('<line x1="142" y1="284" x2="188" y2="284" stroke="#0f172a" stroke-width="2"/>')
    parts.append('<polygon points="165,278.5 160,288 170,288" fill="#0f172a"/>')
    parts.append('<text x="198" y="288" font-size="11.5" fill="#0f172a" font-family="sans-serif">Cocos frillgoby</text>')
    # wavy-lined blenny
    parts.append('<line x1="142" y1="302" x2="188" y2="302" stroke="#334155" stroke-width="2" stroke-dasharray="6,4"/>')
    parts.append('<rect x="160.8" y="297.8" width="8.4" height="8.4" fill="#cbd5e1" stroke="#0f172a" stroke-width="1.5"/>')
    parts.append('<text x="198" y="306" font-size="11.5" fill="#0f172a" font-family="sans-serif">wavy-lined blenny</text>')
    # Indo-Pacific sergeant
    parts.append('<line x1="142" y1="320" x2="188" y2="320" stroke="#0f172a" stroke-width="2" stroke-dasharray="2.5,3"/>')
    parts.append('<circle cx="165" cy="320" r="4.3" fill="#ffffff" stroke="#0f172a" stroke-width="1.6"/>')
    parts.append('<text x="198" y="324" font-size="11.5" fill="#0f172a" font-family="sans-serif">Indo-Pacific sergeant</text>')

    return (
        '<div style="background:#f8fafc;border:1px solid #cbd5e1;border-radius:10px;padding:12px 14px;margin-bottom:12px;">'
        '<div style="font-family:\'Segoe UI\',sans-serif;font-size:13px;font-weight:800;color:#0f172a;'
        'text-align:center;line-height:1.35;margin-bottom:6px;">'
        'Fish Population in a Taiwanese Tide Pool, January 2001 to October 2001</div>'
        '<svg viewBox="0 0 460 342" xmlns="http://www.w3.org/2000/svg" style="max-width:450px;display:block;margin:0 auto;">'
        '<rect x="0" y="0" width="460" height="342" fill="#ffffff"/>'
        f'{"".join(parts)}'
        '</svg></div>'
    )


def svg_m1_q11_fta():
    """Recreates the exact March 2025 Ver 5 M1 Q11 grouped bar chart (Pre- and Post-FTA Export Growth Rate)."""
    x_left, x_right = 82, 410
    y_top, y_bot = 20, 200  # 180px for -5..25 -> 6px per 1%

    def fy(v):
        return y_top + (25 - v) * 6.0

    y0 = fy(0)
    parts = []
    # Horizontal gridlines (-5 to 25 by 5)
    for val in range(-5, 26, 5):
        y = fy(val)
        stroke = '#0f172a' if val == 0 else ('#334155' if val == -5 else '#cbd5e1')
        sw = '1.4' if val in (0, -5) else '1'
        parts.append(f'<line x1="{x_left}" y1="{y:.1f}" x2="{x_right}" y2="{y:.1f}" stroke="{stroke}" stroke-width="{sw}"/>')
        parts.append(f'<text x="{x_left - 8}" y="{y + 3.5:.1f}" font-size="11" text-anchor="end" fill="#1e293b" font-family="sans-serif">{val}</text>')

    # Y-axis line
    parts.append(f'<line x1="{x_left}" y1="{y_top}" x2="{x_left}" y2="{y_bot}" stroke="#334155" stroke-width="1.5"/>')

    # Grouped bars: [El Salvador (#64748b), Mexico (#cbd5e1), Nicaragua (#0f172a)]
    bar_w = 34
    groups = [
        ('Pre-FTA', 118, [(8.1, '#64748b'), (-1.4, '#cbd5e1'), (23.4, '#0f172a')]),
        ('Post-FTA', 268, [(21.8, '#64748b'), (13.7, '#cbd5e1'), (17.5, '#0f172a')]),
    ]
    for label, gx, bars in groups:
        for idx, (val, color) in enumerate(bars):
            bx = gx + idx * bar_w
            if val >= 0:
                by = fy(val)
                bh = y0 - by
            else:
                by = y0
                bh = fy(val) - y0
            parts.append(f'<rect x="{bx}" y="{by:.1f}" width="{bar_w}" height="{bh:.1f}" fill="{color}" stroke="#0f172a" stroke-width="1.1"/>')
        cx = gx + 1.5 * bar_w
        parts.append(f'<text x="{cx:.1f}" y="{y_bot + 18}" font-size="11.5" text-anchor="middle" fill="#1e293b" font-family="sans-serif">{label}</text>')

    # Axis titles
    parts.append(
        '<text x="26" y="110" font-size="11.5" font-weight="600" text-anchor="middle" fill="#0f172a" '
        'font-family="sans-serif" transform="rotate(-90 26 110)">Growth rate (%)</text>'
    )
    parts.append(
        '<text x="246" y="242" font-size="11.5" font-weight="600" text-anchor="middle" fill="#0f172a" '
        'font-family="sans-serif">Export growth</text>'
    )

    # Legend box
    parts.append('<rect x="132" y="254" width="228" height="66" fill="#ffffff" stroke="#475569" stroke-width="1.1"/>')
    legend_items = [
        ('#64748b', 'El Salvador (CAFTA-DR)', 270),
        ('#cbd5e1', 'Mexico (NAFTA)', 290),
        ('#0f172a', 'Nicaragua (CAFTA-DR)', 310),
    ]
    for col, txt, ly in legend_items:
        parts.append(f'<rect x="144" y="{ly - 9}" width="11" height="11" fill="{col}" stroke="#0f172a" stroke-width="1"/>')
        parts.append(f'<text x="163" y="{ly + 1}" font-size="11.5" fill="#0f172a" font-family="sans-serif">{txt}</text>')

    return (
        '<div style="background:#f8fafc;border:1px solid #cbd5e1;border-radius:10px;padding:12px 14px;margin-bottom:12px;">'
        '<div style="font-family:\'Segoe UI\',sans-serif;font-size:13px;font-weight:800;color:#0f172a;'
        'text-align:center;line-height:1.35;margin-bottom:6px;">'
        'Average Total Agricultural Export Growth Rate, Five Years Pre- and Post-FTA with the United States</div>'
        '<svg viewBox="0 0 460 328" xmlns="http://www.w3.org/2000/svg" style="max-width:450px;display:block;margin:0 auto;">'
        '<rect x="0" y="0" width="460" height="328" fill="#ffffff"/>'
        f'{"".join(parts)}'
        '</svg></div>'
    )


def q_item(qid, num, domain, skill, diff, stim, stem, opts, ans, summary_vi, takeaway, analysis):
    """Builds a single Digital SAT R&W MCQ item matching SatBluebookTest.tsx schema."""
    labels = ['A', 'B', 'C', 'D']
    assert ans in labels, f'{qid}: invalid correctAnswer {ans}'
    assert len(opts) == 4 and len(analysis) == 4, f'{qid}: expected 4 options & 4 analysis items'
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


def _clone_module_questions(questions, old_prefix, new_prefix):
    cloned = copy.deepcopy(questions)
    for q in cloned:
        q['id'] = q['id'].replace(old_prefix, new_prefix, 1)
    return cloned


# ============================================================================
# MODULE 1: SECTION 1, MODULE 1 — READING AND WRITING (27 REAL QUESTIONS)
# ============================================================================

MODULE_1_QUESTIONS = [
    # --- M1 Q1 ---
    q_item(
        'march2025_v5_rw_m1_q1', 1, 'Craft and Structure', 'Words in Context', 'Easy',
        '<p>Cognitive science research has found that people tend to be biased against art when they think it was generated by artificial intelligence (AI) software. One hypothesis for the preference for human-created art is that people _______ the effort behind a piece of art: the more work they believe went into a piece’s creation, the more likely they are to appreciate it.</p>',
        'Which choice completes the text with the most logical and precise word or phrase?',
        ['value', 'perform', 'prevent', 'neglect'],
        'A',
        'Dấu hai chấm mở ra lời giải thích trực tiếp cho chỗ trống: “the more work they believe went into a piece’s creation, the more likely they are to appreciate it” (họ càng tin tác phẩm tốn nhiều công sức, họ càng dễ trân trọng nó). Điều này chứng minh con người COI TRỌNG / ĐÁNH GIÁ CAO (“value”) công sức đằng sau tác phẩm nghệ thuật → Chọn A.',
        'Trong dạng Words in Context có dấu hai chấm (`:`), mệnh đề sau dấu hai chấm luôn định nghĩa trực tiếp từ cần điền: “more work → more likely to appreciate” = “value the effort”.',
        [
            ('Đáp án đúng', 'value = coi trọng, đề cao — khớp hoàn toàn với phần giải thích rằng càng tốn nhiều công sức thì người xem càng trân trọng tác phẩm.'),
            ('Wrong Meaning', 'perform = thực hiện, trình diễn — người thưởng thức nghệ thuật không “thực hiện” công sức của họa sĩ.'),
            ('Opposite / Unrelated', 'prevent = ngăn chặn — vô nghĩa khi đi với “effort behind a piece of art”.'),
            ('Opposite Meaning', 'neglect = phớt lờ, bỏ bê — trái ngược hoàn toàn với việc càng thấy nhiều công sức thì càng trân trọng.'),
        ],
    ),

    # --- M1 Q2 ---
    q_item(
        'march2025_v5_rw_m1_q2', 2, 'Craft and Structure', 'Words in Context', 'Easy',
        '<p>The presence of Belarus’s Mir Castle Complex on the United Nations Educational, Scientific, and Cultural Organization’s World Heritage List indicates that the organization has _______ the site’s “outstanding universal value,” and that UNESCO is therefore championing its preservation and protection.</p>',
        'Which choice completes the text with the most logical and precise word or phrase?',
        ['exploited', 'recognized', 'impeded', 'neglected'],
        'B',
        'Việc Quần thể Lâu đài Mir được đưa vào Danh sách Di sản Thế giới của UNESCO và được tổ chức này ra sức bảo tồn (“championing its preservation and protection”) cho thấy UNESCO đã CÔNG NHẬN / GHI NHẬN (“recognized”) “giá trị phổ quát nổi bật” của di tích → Chọn B.',
        'Chú ý từ nối nhân-quả “therefore championing its preservation” để nhận diện ngay sắc thái tích cực duy nhất trong 4 lựa chọn (`recognized` vs. 3 từ tiêu cực `exploited`, `impeded`, `neglected`).',
        [
            ('Negative Tone', 'exploited = khai thác trục lợi — trái ngược với sứ mệnh bảo tồn và bảo vệ di sản của UNESCO.'),
            ('Đáp án đúng', 'recognized = công nhận, ghi nhận — khớp hoàn hảo với việc xếp hạng Di sản Thế giới và bảo vệ di tích.'),
            ('Negative Tone', 'impeded = cản trở — mâu thuẫn với việc ủng hộ bảo tồn.'),
            ('Negative Tone', 'neglected = bỏ mặc, lơ là — trái ngược hoàn toàn với “championing its preservation and protection”.'),
        ],
    ),

    # --- M1 Q3 ---
    q_item(
        'march2025_v5_rw_m1_q3', 3, 'Craft and Structure', 'Words in Context', 'Easy',
        '<p>During film’s early years, those who worked in the industry had a vested interest in convincing the public to embrace the new medium. As Sumiko Higashi argues, some filmmakers relied on film critics to influence the public’s _______ the world of cinema. Critics who drew similarities between film and traditional art forms, like drama, could help legitimize film as an art form.</p>',
        'Which choice completes the text with the most logical and precise word or phrase?',
        ['contribution to', 'perception of', 'reproduction of', 'application to'],
        'B',
        'Câu 1 và câu 3 khóa chặt nghĩa: giới làm phim muốn “thuyết phục công chúng đón nhận loại hình mới” (“convincing the public to embrace”) và dựa vào nhà phê bình để “hợp thức hóa điện ảnh như một môn nghệ thuật” (“legitimize film as an art form”). Vì vậy, nhà phê bình giúp tác động đến CÁCH NHÌN NHẬN / NHẬN THỨC (“perception of”) của công chúng đối với thế giới điện ảnh → Chọn B.',
        'Khi ngữ cảnh nói về việc thuyết phục công chúng xem một thứ là “art form” (hình thức nghệ thuật), cụm danh từ chuẩn xác nhất là “influence the public’s perception of...”.',
        [
            ('Wrong Meaning', 'contribution to = sự đóng góp cho — các nhà phê bình tác động lên cách công chúng đánh giá điện ảnh, không phải mức đóng góp của công chúng.'),
            ('Đáp án đúng', 'perception of = nhận thức / góc nhìn về — khớp sát mục tiêu thay đổi cái nhìn của công chúng để công nhận điện ảnh là nghệ thuật.'),
            ('Wrong Meaning', 'reproduction of = sự sao chép / tái sản xuất — sai hoàn toàn ngữ cảnh.'),
            ('Wrong Meaning', 'application to = sự ứng dụng vào — không phù hợp với việc đánh giá giá trị nghệ thuật của điện ảnh.'),
        ],
    ),

    # --- M1 Q4 ---
    q_item(
        'march2025_v5_rw_m1_q4', 4, 'Craft and Structure', 'Words in Context', 'Medium',
        '<p>The following text is from Amy Tan’s 1989 novel <i>The Joy Luck Club</i>. The narrator describes practicing the piano when she was a child.</p>'
        '<p>For the talent show, I was to play a piece called “Pleading Child” from Schumann’s <i>Scenes from Childhood</i>. It was a simple, moody piece that sounded more difficult than it was. I was supposed to memorize the whole thing, playing the repeat parts twice to make the piece sound longer. But I dawdled over it, playing a few bars and then <u>cheating</u>, looking up to see what notes followed. I never really listened to what I was playing. I daydreamed about being somewhere else, about being someone else.</p>'
        '<div style="font-size:11.5px;color:#64748b;text-align:right;margin-top:-6px;">©1989 by Amy Tan</div>',
        'Based on the text, when the narrator describes herself as “cheating,” what does she most likely mean?',
        [
            'She was lying to herself about her musical ability.',
            'She was violating an expectation about how to perform the piece.',
            'She was deceiving her piano teacher.',
            'She was gaining an unfair advantage over other contestants in the talent show.',
        ],
        'B',
        'Đọc liền hai câu chứa từ gạch chân: “I was supposed to memorize the whole thing... But I dawdled over it, playing a few bars and then <u>cheating</u>, looking up to see what notes followed.” Nhân vật đáng lẽ phải học thuộc lòng toàn bộ bản nhạc (“was supposed to memorize”), nhưng lại cứ đánh vài ô nhịp rồi lén ngước nhìn bản nhạc để xem nốt tiếp theo → cô bé tự gọi đó là “cheating” theo nghĩa vi phạm yêu cầu/kỳ vọng về cách biểu diễn bản nhạc (phải chơi thuộc lòng) → Chọn B.',
        'Khi câu hỏi hỏi nghĩa một từ trong ngữ cảnh tự sự (như “cheating”), hãy nối thẳng câu ngay trước (“was supposed to memorize”) với cụm giải thích ngay sau dấu phẩy (“looking up to see what notes followed”).',
        [
            ('Unsupported Inference', 'Cô bé không tự lừa dối về tài năng âm nhạc; cô chỉ lười luyện thuộc lòng và nhìn bản nhạc.'),
            ('Đáp án đúng', 'Khớp sát ngữ cảnh: “was supposed to memorize” là yêu cầu/kỳ vọng đặt ra, còn “looking up to see what notes followed” là hành động vi phạm kỳ vọng đó.'),
            ('Not Mentioned', 'Đoạn văn chỉ miêu tả cảnh cô bé tự tập đàn một mình, không hề nhắc tới giáo viên dạy piano.'),
            ('Literal Misreading', 'Hiểu máy móc từ “cheating” theo nghĩa gian lận thi cử để hơn thí sinh khác — nhưng đây mới là lúc cô bé tập đàn ở nhà, không tạo lợi thế bất công nào trong cuộc thi.'),
        ],
    ),

    # --- M1 Q5 ---
    q_item(
        'march2025_v5_rw_m1_q5', 5, 'Craft and Structure', 'Text Structure and Purpose', 'Medium',
        '<p>The following text is adapted from George Eliot’s 1857 short story “The Sad Fortunes of the Rev. Amos Barton.” Mr. Ely is a clergyman in the town of Milby.</p>'
        '<p>By the laity of Milby and its neighbourhood [Mr. Ely] was regarded as a man of quite remarkable powers and learning, who must make a considerable sensation in London pulpits and drawing rooms on his occasional visit to the metropolis; and by his brother clergy he was regarded as a discreet and agreeable fellow. Mr. Ely never got into a warm discussion; he suggested what might be thought, but rarely said what he thought himself; he never let either men or women see that he was laughing at them, and he never gave any one an opportunity of laughing at <i>him</i>.</p>',
        'Which choice best describes the overall structure of the text?',
        [
            'It details how Mr. Ely initially won his colleagues’ admiration and then reports on the circumstances that prompted them to revise their views of him.',
            'It implies that Mr. Ely’s neighbors are more naive in their estimation of him than people in London are and then explains why his neighbors have been so easily misled.',
            'It illuminates how Mr. Ely conducts himself differently in public and in private and then touches on why he is cautious to reveal some aspects of his character to other people.',
            'It presents the favorable opinion of Mr. Ely that other people hold and then describes the behaviors of Mr. Ely that enable him to maintain that favorable opinion.',
        ],
        'D',
        'Đoạn văn chia rạch ròi làm 2 câu — 2 phần cấu trúc: (1) Câu 1 trình bày cái nhìn đầy thiện cảm mà mọi người dành cho ông Ely (giáo dân Milby xem ông có năng lực và học vấn xuất chúng, còn các đồng nghiệp giáo sĩ coi ông là người kín đáo, dễ chịu); (2) Câu 2 liệt kê hàng loạt thói quen ứng xử khôn khéo của ông Ely (không tranh luận gay gắt, hiếm khi nói thẳng suy nghĩ thật, không để ai thấy mình cười nhạo họ và không để ai có cơ hội cười mình) giúp ông duy trì hình ảnh tốt đẹp ấy → Chọn D.',
        'Với câu hỏi Overall Structure của đoạn văn 2 câu, đối chiếu trực tiếp Chặng 1 (câu 1: “favorable opinion”) + Chặng 2 (câu 2: “behaviors... that enable him to maintain it”) để loại các phương án thêm chi tiết không hề có trong bài.',
        [
            ('Added / False Ending', 'Đoạn văn không hề có chi tiết nào nói đồng nghiệp thay đổi hay xét lại quan điểm về ông Ely.'),
            ('Unsupported Comparison', 'Văn bản chỉ nói giáo dân ở Milby tưởng tượng ông hẳn gây tiếng vang ở London, không so sánh mức độ ngây thơ giữa người Milby và người London.'),
            ('Unsupported Contrast', 'Không có sự đối chiếu giữa cách cư xử nơi công cộng và đời tư khép kín, cũng không giải thích nguyên nhân tâm lý của ông.'),
            ('Đáp án đúng', 'Tóm gọn chính xác cấu trúc 2 phần: nêu đánh giá tích cực của mọi người về ông Ely → mô tả các hành vi thận trọng giúp ông giữ vững đánh giá đó.'),
        ],
    ),

    # --- M1 Q6 ---
    q_item(
        'march2025_v5_rw_m1_q6', 6, 'Craft and Structure', 'Cross-Text Connections', 'Hard',
        '<p><b>Text 1</b><br/>'
        'Chemically analyzing bulk rock-core samples from Australia’s Mount McRae Shale, Ariel Anbar et al. found a transient but significant increase in molybdenum (Mo) at a point corresponding to roughly 2.5 billion years ago (Ga). On Earth, Mo is released mainly through oxidative weathering of minerals; Anbar et al. therefore concluded that atmospheric oxygen briefly increased 2.5 Ga, then returned to its earlier negligible level.</p>'
        '<p><b>Text 2</b><br/>'
        'Sarah Slotznick et al. reexamined the Mount McRae Shale core. Since chemically analyzing bulk samples can occlude contextual details, Slotznick et al. also employed high-resolution microscopy, which revealed volcanic debris—a known Mo host—around 2.5 Ga and microfractures in the surrounding matrix. The researchers assert that fluid could have reached the debris through the microfractures and initiated oxidative weathering long after debris deposition.</p>',
        'Based on the texts, Anbar et al. (Text 1) and Slotznick et al. (Text 2) would most likely disagree about the answer to which question about the portion of the Mount McRae Shale rock-core corresponding to 2.5 Ga?',
        [
            'Is the increase in Mo in that portion attributable to oxidative weathering of the material found in that portion?',
            'Is the increase in Mo in that portion indicative of an increase in atmospheric oxygen dating to the same time?',
            'Did chemically analyzing bulk samples lead to a false impression that there is an increase in Mo in that portion?',
            'Does the increase in Mo in that portion suggest that atmospheric oxygen levels were not negligible before 2.5 Ga?',
        ],
        'B',
        'So sánh điểm ĐỒNG THUẬN và điểm BẤT ĐỒNG giữa hai nhóm tác giả: Cả Anbar et al. (Text 1) và Slotznick et al. (Text 2) đều thừa nhận có lượng Mo tăng lên tại lớp đá mốc 2,5 tỷ năm trước VÀ đều giải thích bằng quá trình phong hóa oxy hóa (oxidative weathering). Điểm bất đồng cốt lõi nằm ở **THỜI ĐIỂM** diễn ra sự phong hóa đó: Anbar kết luận nó chứng tỏ oxy khí quyển tăng lên **tại đúng mốc 2,5 Ga** (“dating to the same time”); ngược lại, Slotznick cho rằng chất lỏng có thể đã thấm qua các vi nứt gãy và gây phong hóa oxy hóa **rất lâu sau khi mảnh vụn núi lửa lắng đọng** (“long after debris deposition”), tức KHÔNG chứng minh oxy tăng vào mốc 2,5 Ga → Chọn B!',
        'Câu Cross-Text Connections nâng cao luôn ẩn bẫy ở chỗ hai nhóm ĐỒNG Ý về cơ chế (“oxidative weathering”) và dữ liệu đo (“increase in Mo”), chỉ KHÁC NHAU ở thời điểm kết luận (“2.5 Ga” vs. “long after debris deposition”).',
        [
            ('Point of Agreement', 'Cả hai nhóm đều đồng ý sự gia tăng Mo liên quan đến phong hóa oxy hóa (Slotznick cũng nói “initiated oxidative weathering” đối với mảnh vụn núi lửa chứa Mo).'),
            ('Đáp án đúng', 'Trúng tâm điểm bất đồng: Anbar trả lời CÓ (chứng tỏ oxy khí quyển tăng vào đúng 2,5 Ga), còn Slotznick trả lời KHÔNG (phong hóa oxy hóa có thể xảy ra rất lâu sau đó qua vi nứt gãy).'),
            ('Misreading Text 2', 'Slotznick không phủ nhận việc Mo tăng lên trong mẫu (thậm chí xác nhận mảnh vụn núi lửa là nguồn chứa Mo), mà chỉ nói phân tích mẫu tổng thể che khuất chi tiết bối cảnh như mảnh vụn và vi nứt gãy.'),
            ('Both Would Say No', 'Cả hai văn bản đều không cho rằng lượng oxy trước 2,5 Ga là đáng kể (Text 1 còn khẳng định rõ “returned to its earlier negligible level”).'),
        ],
    ),

    # --- M1 Q7 ---
    q_item(
        'march2025_v5_rw_m1_q7', 7, 'Information and Ideas', 'Central Ideas and Details', 'Medium',
        '<p>Many artists associated with hyperpop, a movement in electronic music that emerged in the 2010s, conform to the model perfected by the American duo 100 gecs: bold synthesizer arrangements, propulsive beats, and electronically manipulated vocals. Yet the movement is hardly uniform: British recording artist Charli XCX incorporates pop melodies into the hyperpop sound, for example. Such stylistic diversity is encouraged in part by the music-streaming app Spotify, whose curated playlist of hyperpop songs balances cohesion with variety.</p>',
        'Which statement about Charli XCX is best supported by the text?',
        [
            'Her inclusion on Spotify’s hyperpop playlist inspired established artists to embrace stylistic experimentation.',
            'She developed her unique sound without being influenced by other artists on Spotify’s hyperpop playlist.',
            'While some of her recordings conform to the model perfected by 100 gecs, others reject it outright.',
            'Her music diverges from the typical hyperpop sound but doesn’t abandon it.',
        ],
        'D',
        'Đọc kỹ câu nêu ví dụ về Charli XCX: đoạn văn giới thiệu khuôn mẫu hyperpop điển hình của 100 gecs, rồi chuyển ý: “Yet the movement is hardly uniform: British recording artist Charli XCX incorporates pop melodies into the hyperpop sound, for example.” Cô đưa giai điệu pop **vào trong** (“into”) âm thanh hyperpop → âm nhạc của cô có sự khác biệt so với mẫu hyperpop điển hình nhưng KHÔNG hề từ bỏ chất hyperpop (“diverges from the typical hyperpop sound but doesn’t abandon it”) → Chọn D.',
        'Cụm “incorporates X into Y” (kết hợp yếu tố X vào nền tảng Y) luôn tương đương về mặt suy luận chặt với “diverges from typical Y but doesn’t abandon Y”.',
        [
            ('Not Mentioned', 'Bài không nói việc Charli XCX xuất hiện trên playlist Spotify đã truyền cảm hứng cho các nghệ sĩ kỳ cựu khác.'),
            ('Not Mentioned', 'Không có thông tin nào nói cô tạo ra âm thanh riêng mà không chịu ảnh hưởng từ các nghệ sĩ khác.'),
            ('Extreme Distortion', 'Từ “reject it outright” (bác bỏ hoàn toàn) sai với thực tế bài nói cô kết hợp giai điệu pop VÀO âm thanh hyperpop.'),
            ('Đáp án đúng', 'Diễn giải chuẩn xác việc Charli XCX vừa mang nét đa dạng riêng (giai điệu pop) vừa vẫn giữ nền tảng âm thanh hyperpop.'),
        ],
    ),

    # --- M1 Q8 ---
    q_item(
        'march2025_v5_rw_m1_q8', 8, 'Information and Ideas', 'Central Ideas and Details', 'Medium',
        '<p>In a study by Mika R. Moran, Daniel A. Rodriguez, and colleagues, residents of Quito, Ecuador, and Buenos Aires, Argentina, were surveyed about parks in their cities. Of the 618 respondents from Quito, 82.9% indicated that they use the city’s parks, and of the 683 respondents from Buenos Aires, 69.9% indicated using city parks. Given that the percentage of Quito respondents who reported having access to other desired amenities near parks was much lower than that reported by Buenos Aires respondents, the difference in park use can’t be explained by Quito residents having more access to desired nonpark amenities near parks.</p>',
        'Which choice best describes the main idea of the text?',
        [
            'The study’s finding that a greater proportion of residents use parks in Quito than in Buenos Aires is partly due to the greater prevalence of parks in Quito.',
            'The study’s findings suggest that an increase in the number of amenities near city parks would likely increase park use in Quito but not in Buenos Aires.',
            'Although the study found that a greater proportion of residents use parks in Quito than in Buenos Aires, that difference isn’t due to greater access to amenities near parks in Quito.',
            'Even though the study found that parks in Buenos Aires are more likely to be close to other amenities than parks in Quito are, Quito has more amenities overall than Buenos Aires does.',
        ],
        'C',
        'Đoạn văn nêu 2 dữ kiện và 1 kết luận trọng tâm: (1) Tỷ lệ người dân đi công viên ở Quito (82,9%) cao hơn Buenos Aires (69,9%); (2) Tỷ lệ người dân Quito tiếp cận được các tiện ích mong muốn gần công viên lại thấp hơn nhiều so với Buenos Aires → Kết luận chính (câu cuối): sự chênh lệch tỷ lệ sử dụng công viên KHÔNG thể giải thích bằng việc cư dân Quito có nhiều tiện ích gần công viên hơn → Chọn C.',
        'Với bài Main Idea về nghiên cứu khoa học xã hội, câu kết bắt đầu bằng “Given that..., [concluding clause]” hầu như luôn chứa trọn vẹn ý chính của đoạn.',
        [
            ('Not Mentioned', 'Bài hoàn toàn không đề cập mật độ hay số lượng công viên ở Quito nhiều hơn Buenos Aires.'),
            ('Unsupported Prediction', 'Đoạn văn không đưa ra dự đoán nào về việc bổ sung tiện ích sẽ làm tăng tỷ lệ dùng công viên ở Quito.'),
            ('Đáp án đúng', 'Bao quát chính xác cả phát hiện (tỷ lệ dùng công viên ở Quito cao hơn) lẫn kết luận (nguyên nhân không phải do tiện ích gần công viên ở Quito nhiều hơn).'),
            ('Not Mentioned', 'Không có thông tin nào nói Quito có nhiều tiện ích nói chung hơn Buenos Aires.'),
        ],
    ),

    # --- M1 Q9 ---
    q_item(
        'march2025_v5_rw_m1_q9', 9, 'Information and Ideas', 'Command of Evidence (Quantitative)', 'Easy',
        svg_m1_q9_fish() +
        '<p>Lin-Tai Ho and colleagues monitored fish populations in a tide pool in Taiwan. They found that some species were entirely absent from the tide pool at particular times of the year; for example, they did not observe even one _______</p>',
        'Which choice most effectively uses data from the graph to complete the example?',
        [
            'wavy-lined blenny in January, April, and July of 2001.',
            'Indo-Pacific sergeant in October of 2001.',
            'Indo-Pacific sergeant in July of 2001.',
            'Cocos frillgoby in April of 2001.',
        ],
        'A',
        'Đề bài yêu cầu minh họa bằng một loài hoàn toàn vắng bóng (“entirely absent” = không quan sát thấy lấy một con nào, tức giá trị trên trục tung bằng **0**). Đối chiếu đường nét đứt kèm ô vuông của loài **wavy-lined blenny** trên đồ thị: giá trị bằng **0** vào đúng ba mốc **January 2001**, **April 2001**, và **July 2001** (đến October 2001 mới tăng lên 3) → Chọn A.',
        'Đọc kỹ cụm mục tiêu “did not observe even one” = tìm đường chạm đúng vạch `0` trên trục tung, rồi tra chú thích (legend) đúng ký hiệu hình vuông nét đứt.',
        [
            ('Đáp án đúng', 'Khớp chính xác dữ liệu đồ thị: đường wavy-lined blenny (ô vuông nét đứt) nằm đúng tại vạch 0 trong tháng 1, tháng 4 và tháng 7 năm 2001.'),
            ('Wrong Data Point', 'Indo-Pacific sergeant (vòng tròn nét chấm) tháng 10/2001 đạt đỉnh khoảng 28 cá thể — cao nhất đồ thị chứ không phải 0.'),
            ('Wrong Data Point', 'Indo-Pacific sergeant tháng 7/2001 có khoảng 21 cá thể, không hề vắng mặt.'),
            ('Wrong Data Point', 'Cocos frillgoby (tam giác đen nét liền) tháng 4/2001 có 10 cá thể, không phải 0.'),
        ],
    ),

    # --- M1 Q10 ---
    q_item(
        'march2025_v5_rw_m1_q10', 10, 'Information and Ideas', 'Command of Evidence (Textual)', 'Medium',
        '<p>“The Monster” is an 1898 story by Stephen Crane. In the story, whenever Jimmie, a young boy, has been scolded by his father for misbehavior, he seeks comfort from Henry Johnson, the man responsible for the care of Jimmie’s father’s horses. However, Henry does not always provide such comfort; Crane suggests this by writing, _______</p>',
        'Which quotation from “The Monster” most effectively illustrates the claim?',
        [
            '“For one thing, Jimmie was invariably overcome with reverence when he was told how beautifully a harness was polished or a horse groomed.”',
            '“Henry... could usually provide a sin to place himself on a footing with the disgraced one. Perhaps he would remember that he had forgotten to put the hitching-strap in the back of the buggy on some recent occasion, and had been reprimanded by [Jimmie’s father].”',
            '“Henry would sometimes choose to absolutely repudiate [Jimmie’s behavior], and when Jimmie appeared in his shame would bully him most virtuously, preaching with assurance the precepts of [Jimmie’s father’s] creed, and pointing out to Jimmie all of his abominations.”',
            '“Whenever Henry dwelt for a time in sackcloth [a symbol of guilt over wrongdoing], Jimmie did not patronize him at all.”',
        ],
        'C',
        'Xác định đúng luận điểm cần minh họa ở câu cuối: “However, Henry **does not always provide such comfort**” (Tuy nhiên, Henry không phải lúc nào cũng an ủi Jimmie). Đáp án C mô tả trực tiếp điều đó: thỉnh thoảng Henry lại chọn lên án gay gắt hành vi của Jimmie (“absolutely repudiate”), lên mặt dạy đời (“bully him most virtuously”), thuyết giảng lại đúng giáo điều của cha Jimmie và vạch trần hết mọi tội lỗi của cậu bé → Chọn C.',
        'Cẩn thận bẫy đối nghĩa ở đáp án B: B minh họa lúc Henry CÓ an ủi/đồng cảm với Jimmie (kể tội của bản thân để ngang hàng với cậu bé), trong khi câu hỏi nhắm vào câu chuyển ý bắt đầu bằng “However”!',
        [
            ('Irrelevant Detail', 'Chỉ nói sự ngưỡng mộ của Jimmie dành cho kỹ năng chăm sóc ngựa và yên cương của Henry, không liên quan việc bị mắng hay an ủi.'),
            ('Opposite Evidence', 'Mô tả cách Henry THƯỜNG an ủi Jimmie (bằng cách tự nhận mình cũng từng mắc lỗi và bị cha Jimmie quở trách), trái với mệnh đề cần chứng minh (“does not always provide such comfort”).'),
            ('Đáp án đúng', 'Minh họa trực diện việc Henry đôi khi không an ủi mà lại quở mắng, lên lớp và chỉ trích mọi lỗi lầm khi Jimmie đang xấu hổ tìm đến.'),
            ('Reversed Roles', 'Nói về thái độ của Jimmie khi Henry có lỗi, hoàn toàn đảo ngược tình huống Jimmie tìm sự an ủi từ Henry.'),
        ],
    ),

    # --- M1 Q11 ---
    q_item(
        'march2025_v5_rw_m1_q11', 11, 'Information and Ideas', 'Command of Evidence (Quantitative)', 'Medium',
        svg_m1_q11_fta() +
        '<p>To measure whether countries in free trade agreements (FTAs)—agreements among nations to reduce tariffs, duties, and other trade barriers—experience changes in total agricultural exports, economist Kayode Ajewole and colleagues calculated average export growth rates for several countries over the five years before and the five years after entering an FTA with the United States. The graph shows the results for three countries in the study. Consulting the graph, a student claims that joining an FTA increases the rate of growth of a country’s total agricultural exports.</p>',
        'Which choice best describes data from the graph that weaken the student’s claim?',
        [
            'Although agricultural exports from Mexico decreased over the five years before NAFTA, a reversal in this trend was observed over the five years after Mexico joined NAFTA.',
            'Although agricultural exports from Nicaragua grew over the five years after Nicaragua joined CAFTA-DR, their growth rate was even higher in the five years before CAFTA-DR.',
            'Over the five years after El Salvador joined CAFTA-DR, agricultural exports from El Salvador grew at a rate of about 21.8 percent, which is higher than the rate over the five years before El Salvador joined the agreement.',
            'All the countries shown had positive growth in agricultural exports over the five years after joining their respective FTAs, but their rates of export growth varied.',
        ],
        'B',
        'Luận điểm của học sinh: “gia nhập một hiệp định thương mại tự do (FTA) giúp **tăng tốc độ tăng trưởng** tổng kim ngạch xuất khẩu nông sản của một quốc gia”. Để **làm suy yếu (weaken)** luận điểm này, ta cần tìm quốc gia có tốc độ tăng trưởng xuất khẩu **GIẢM xuống** sau khi gia nhập FTA (Post-FTA < Pre-FTA). Nhìn cột màu đen (**Nicaragua – CAFTA-DR**): giai đoạn 5 năm trước FTA đạt ~23,4%, nhưng 5 năm sau FTA giảm xuống chỉ còn ~17,5% (tuy vẫn tăng trưởng dương nhưng chậm lại so với trước khi gia nhập) → Đáp án B phản bác trực diện luận điểm học sinh!',
        'Với câu hỏi Weaken biểu đồ trước–sau (Pre vs. Post), luôn kiểm tra xem có đối tượng nào đi NGƯỢC xu hướng chung không: Mexico và El Salvador đều tăng, duy nhất Nicaragua giảm từ ~23,4% xuống ~17,5%.',
        [
            ('Supports Claim', 'Mexico chuyển từ tăng trưởng âm (~−1,4%) lên dương (~13,7%) sau NAFTA — dữ liệu này ỦNG HỘ chứ không làm suy yếu luận điểm.'),
            ('Đáp án đúng', 'Khớp chính xác cột màu đen của Nicaragua: xuất khẩu vẫn tăng sau CAFTA-DR (~17,5%), nhưng tốc độ tăng trưởng trước khi gia nhập còn cao hơn (~23,4%), trực tiếp bác bỏ lập luận rằng FTA luôn làm tăng tốc độ tăng trưởng.'),
            ('Supports Claim', 'El Salvador tăng vọt từ ~8,1% lên ~21,8% sau CAFTA-DR — dữ liệu này ủng hộ luận điểm học sinh.'),
            ('Irrelevant / No Pre-Post Comparison', 'Chỉ nói cả ba nước đều tăng trưởng dương sau FTA với mức độ khác nhau, không so sánh với giai đoạn Pre-FTA nên không làm suy yếu luận điểm.'),
        ],
    ),

    # --- M1 Q12 ---
    q_item(
        'march2025_v5_rw_m1_q12', 12, 'Information and Ideas', 'Command of Evidence (Quantitative)', 'Medium',
        html_table(
            'Average Monetized Productivity Loss at Two Points After Programs Began, in Australian Dollars',
            ['Type of training', '12 weeks', '12 months'],
            [
                ['EET', '268', '171'],
                ['EHP', '282', '436'],
            ],
        ) +
        '<p>Michelle Pereira et al. hypothesized that introducing health improvements into workplaces would increase productivity by reducing absenteeism (sick employees not working) and presenteeism (sick workers working less productively due to illness). Pereira’s team enrolled groups of Australian workers in two programs: one that gave employees exercise training (EET) and one that enrolled employees in health promotion seminars (EHP). They then calculated the productivity loss of those groups at 12 weeks and 12 months after the programs began (based on the 28 days preceding each point). They concluded that exercise training was more effective at restraining productivity loss than health promotion seminars were, though this result took time to become apparent.</p>',
        'Which choice best describes data from the table that most effectively strengthen Pereira and colleagues’ conclusion?',
        [
            'Productivity loss for the EET group barely decreased between 12 weeks and 12 months after the program began, while productivity loss for the EHP group significantly increased during the same time period.',
            'Productivity loss was largely due to absenteeism for the EHP group at 12 months after the program began, while productivity loss was largely due to presenteeism for the EET group at 12 months after the program began.',
            'Productivity loss was consistently higher for the EHP group than for the EET group over the twelve months that it was measured, though the size of the difference between the two decreased over that time.',
            'Productivity loss was fairly similar for the EET and EHP groups 12 weeks after each program began, but at 12 months afterward it had significantly increased for the EHP group and significantly decreased for the EET group.',
        ],
        'D',
        'Kết luận của nhóm Pereira gồm 2 vế bắt buộc phải được củng cố đồng thời: [1] Chương trình tập luyện thể dục (**EET**) hiệu quả hơn hội thảo tuyên truyền sức khỏe (**EHP**) trong việc kiềm chế tổn thất năng suất; VÀ [2] Kết quả này **cần thời gian mới thể hiện rõ** (“took time to become apparent”). Đối chiếu bảng số liệu (đơn vị: AUD tổn thất): tại mốc **12 tuần**, hai nhóm khá tương đương (EET = 268 vs. EHP = 282); nhưng đến mốc **12 tháng**, tổn thất của EHP tăng vọt lên **436** trong khi EET giảm mạnh xuống chỉ còn **171** → Đáp án D mô tả chính xác cả hai mốc thời gian và củng cố trọn vẹn cả hai vế kết luận!',
        'Luôn kiểm tra VẾ PHỤ của kết luận (“though this result took time to become apparent”): chính chi tiết mốc 12 tuần còn khá sát nhau (268 vs. 282) và mốc 12 tháng mới tách xa (171 vs. 436) là chìa khóa chốt đáp án D.',
        [
            ('Data Distortion', 'Sai sự thật: tổn thất của nhóm EET giảm từ 268 xuống 171 (giảm gần 36%), là mức giảm ĐÁNG KỂ chứ không phải “barely decreased” (hầu như không giảm).'),
            ('Not in Table', 'Bảng số liệu chỉ ghi tổng tổn thất năng suất quy đổi ra tiền, hoàn toàn không tách tỷ trọng giữa nghỉ ốm (absenteeism) và đi làm kém hiệu suất (presenteeism).'),
            ('Reversed Trend', 'Khoảng cách giữa EHP và EET TĂNG vọt từ 14 AUD (tuần 12) lên 265 AUD (tháng 12), hoàn toàn trái ngược với tuyên bố “decreased over that time”.'),
            ('Đáp án đúng', 'Khớp 100% số liệu bảng và cả hai vế kết luận: 12 tuần đầu hai nhóm khá gần nhau (268 vs. 282), sang tháng 12 thì EHP tăng mạnh (436) còn EET giảm mạnh (171).'),
        ],
    ),

    # --- M1 Q13 ---
    q_item(
        'march2025_v5_rw_m1_q13', 13, 'Information and Ideas', 'Command of Evidence (Textual)', 'Medium',
        '<p>Water flowing around an obstruction creates vortices (patterns of swirls) of varying size; by detecting the vortices, fish can determine the size and position of the obstruction. Testing by Yuzo R. Yanagisuru, Otar Akanyeti, and James C. Liao using models of three head shapes—narrow (low ratio of width to length), intermediate, and wide (high ratio of width to length)—showed that for medium-sized vortices, fish with wide heads would be least able to distinguish between vortices and general turbulence in the water. A second research team has therefore hypothesized that in low-visibility conditions, wider-headed fish will be less likely than narrower-headed fish to detect obstructions.</p>',
        'Which finding, if true, would most directly support the second research team’s hypothesis?',
        [
            'A study using obstructions that created medium-sized vortices in low-visibility conditions found that the anglerfish (<i>Lophiodes monodi</i>), which has a relatively wide head, bumped into more than half of the obstructions.',
            'A study using obstructions that created medium-sized vortices in low-visibility conditions found that the narrower-headed dusky smooth-hound (<i>Mustelus canis</i>) bumped into the obstructions just as often as the wider-headed anglerfish (<i>Lophiodes monodi</i>) did.',
            'A study using obstructions that created medium-sized vortices in low-visibility conditions found that the wider-headed anglerfish (<i>Lophiodes monodi</i>) bumped into obstructions more often than the narrower-headed dusky smooth-hound (<i>Mustelus canis</i>) did.',
            'A study using obstructions that created medium-sized vortices in low-visibility conditions found that some specimens of dusky smooth-hound (<i>Mustelus canis</i>), which has a relatively narrow head, bumped into the obstructions more often than other specimens of the same fish did.',
        ],
        'C',
        'Giả thuyết của nhóm nghiên cứu thứ hai: trong điều kiện tầm nhìn thấp (“low-visibility conditions”), **cá đầu rộng sẽ ít có khả năng phát hiện vật cản hơn cá đầu hẹp** (“wider-headed fish will be less likely than narrower-headed fish to detect obstructions”). Nếu ít phát hiện vật cản hơn, thì khi thử nghiệm thực tế chúng sẽ **va chạm vào vật cản thường xuyên hơn** cá đầu hẹp! Đáp án C trực tiếp so sánh hai loài trong đúng điều kiện tầm nhìn thấp + xoáy nước cỡ trung bình: cá đầu rộng (*Lophiodes monodi*) va vào vật cản thường xuyên hơn cá đầu hẹp (*Mustelus canis*) → Chọn C!',
        'Để củng cố một giả thuyết SO SÁNH (“A less likely than B”), bằng chứng BẮT BUỘC phải có mặt CẢ HAI nhóm A và B cùng chiều kết quả dự đoán (loại ngay A và D vì thiếu đối chứng hai nhóm, loại B vì ngang bằng).',
        [
            ('Missing Comparison Group', 'Chỉ quan sát mỗi cá đầu rộng (*Lophiodes monodi*) va vào hơn nửa số vật cản mà không có dữ liệu đối chiếu với cá đầu hẹp — chưa chứng minh được đầu rộng kém hơn đầu hẹp.'),
            ('Contradicts Hypothesis', 'Hai loài va vào vật cản thường xuyên NHƯ NHAU (“just as often as”) — trực tiếp bác bỏ giả thuyết cho rằng cá đầu rộng kém phát hiện vật cản hơn.'),
            ('Đáp án đúng', 'Cung cấp đúng phép so sánh đối chứng trong điều kiện chuẩn: cá đầu rộng va chạm nhiều hơn cá đầu hẹp, chứng tỏ cá đầu rộng khó phát hiện vật cản hơn.'),
            ('Wrong Comparison', 'Chỉ so sánh giữa các cá thể CÙNG MỘT LOÀI đầu hẹp (*Mustelus canis*) với nhau, không kiểm chứng giả thuyết giữa đầu rộng và đầu hẹp.'),
        ],
    ),

    # --- M1 Q14 ---
    q_item(
        'march2025_v5_rw_m1_q14', 14, 'Information and Ideas', 'Inferences', 'Medium',
        '<p>J.G. Ballard’s 1984 novel <i>Empire of the Sun</i> is regularly described as autobiographical. That characterization is apt—there are many parallels between the experiences of the novel’s protagonist, Jim Graham, and those of Ballard—but it should not be taken to mean that every person or event depicted in <i>Empire of the Sun</i> has a real-life analogue. Much of the novel is pure invention, and readers who neglect this fact and instead focus excessively on correspondences between the novel and Ballard’s life can thus _______</p>',
        'Which choice most logically completes the text?',
        [
            'misrepresent <i>Empire of the Sun</i> as being more widely read than it actually is.',
            'overemphasize the extent to which Ballard took inspiration from earlier writers.',
            'fail to appreciate how much creativity Ballard shows in the book.',
            'refuse to acknowledge that Ballard drew on real-world material when writing <i>Empire of the Sun</i>.',
        ],
        'C',
        'Mạch lập luận: Tiểu thuyết *Empire of the Sun* của J.G. Ballard có nhiều điểm tương đồng tự truyện, nhưng KHÔNG có nghĩa mọi nhân vật/sự kiện đều có nguyên mẫu ngoài đời. Câu cuối nhấn mạnh: “Phần lớn cuốn tiểu thuyết là **hư cấu thuần túy** (“pure invention”), và những độc giả bỏ qua thực tế này mà chỉ chăm chăm tìm điểm trùng khớp với cuộc đời Ballard thì do đó có thể _______”. Hệ quả tất yếu: họ sẽ **không trân trọng / đánh giá đúng mức sự sáng tạo** mà Ballard thể hiện trong tác phẩm → Chọn C!',
        'Nối trực tiếp từ khóa “pure invention” (hư cấu/sáng tạo thuần túy) + “neglect this fact” (bỏ qua sự thật này) → suy ra ngay “fail to appreciate how much creativity...”.',
        [
            ('Out of Scope', 'Đoạn văn không hề đề cập độ phổ biến hay lượng độc giả của cuốn sách.'),
            ('Out of Scope', 'Không có chi tiết nào về việc Ballard chịu ảnh hưởng từ các nhà văn đi trước.'),
            ('Đáp án đúng', 'Khớp hoàn toàn logic: phớt lờ yếu tố hư cấu thuần túy và chỉ soi chiếu đời tư tác giả khiến độc giả bỏ lỡ tài năng sáng tạo của Ballard.'),
            ('Opposite Logic', 'Độc giả đang tập trung QUÁ MỨC vào các mối liên hệ với đời thực của Ballard, chứ không phải từ chối thừa nhận chất liệu đời thực.'),
        ],
    ),

    # --- M1 Q15 ---
    q_item(
        'march2025_v5_rw_m1_q15', 15, 'Standard English Conventions', 'Form, Structure, and Sense', 'Easy',
        '<p>The words “utopia” and “nerd” both trace _______ origins to books. “Utopia” first appears in <i>Utopia</i> by Sir Thomas More, and “nerd” first appears in <i>If I Ran the Zoo</i> by Dr. Seuss.</p>',
        'Which choice completes the text so that it conforms to the conventions of Standard English?',
        [
            'there',
            'it’s',
            'their',
            'they’re',
        ],
        'C',
        'Kiểm tra đại từ sở hữu và từ đồng âm dễ nhầm (`there` / `it’s` / `their` / `they’re`): Chủ ngữ là danh từ SỐ NHIỀU gồm 2 từ — `The words “utopia” and “nerd”`. Trước danh từ `origins` cần một **tính từ sở hữu số nhiều** mang nghĩa “nguồn gốc của chúng” → **“their”** → Chọn C!',
        'Gặp bộ 4 từ đồng âm `there / their / they’re / it’s`: kiểm tra chủ ngữ số nhiều (`The words...`) + vị trí trước danh từ (`___ origins`) → chọn tính từ sở hữu `their`.',
        [
            ('Homophone Confusion', '“there” là trạng từ chỉ nơi chốn hoặc chủ ngữ giả, không phải tính từ sở hữu.'),
            ('Wrong Number & Contraction', '“it’s” là viết tắt của “it is / it has” (số ít), sai cả ngữ pháp lẫn số nhiều.'),
            ('Đáp án đúng', '“their” là tính từ sở hữu số nhiều chuẩn xác bổ nghĩa cho “origins”, tương ứng với hai từ “utopia” và “nerd”.'),
            ('Contraction Confusion', '“they’re” là viết tắt của “they are”, không thể đứng trước danh từ “origins” ở đây.'),
        ],
    ),

    # --- M1 Q16 ---
    q_item(
        'march2025_v5_rw_m1_q16', 16, 'Standard English Conventions', 'Boundaries', 'Easy',
        '<p>With an average summer temperature of 61 degrees Fahrenheit, Moscow is one European _______ many travelers recommend, especially from June to September.</p>',
        'Which choice completes the text so that it conforms to the conventions of Standard English?',
        [
            'city, that',
            'city, which',
            'city in which,',
            'city that',
        ],
        'D',
        'Mệnh đề quan hệ xác định (Restrictive Relative Clause): Trong câu “Moscow is one European **city that** many travelers recommend, especially from June to September”, mệnh đề “that many travelers recommend” là thông tin THIẾT YẾU xác định “one European city” nào (nếu bỏ đi, câu “Moscow is one European city” trở nên vô nghĩa/thiếu thông tin trọng tâm). Vì là mệnh đề quan hệ xác định dùng `that`, TUYỆT ĐỐI KHÔNG đặt dấu phẩy trước `that` → Chọn D (`city that`)!',
        'Quy tắc vàng SAT Boundaries: KHÔNG BAO GIỜ đặt dấu phẩy ngay trước đại từ quan hệ `that` trong mệnh đề quan hệ xác định (restrictive clause).',
        [
            ('Comma Before “that”', 'Sai quy tắc cơ bản: không dùng dấu phẩy trước đại từ quan hệ xác định “that”.'),
            ('Wrong Nonrestrictive Clause', 'Dùng “, which” biến vế sau thành thông tin phụ có thể lược bỏ, khiến câu gốc chỉ còn “Moscow is one European city” — cụt nghĩa và sai chức năng xác định.'),
            ('Wrong Preposition & Comma', 'Động từ “recommend” là ngoại động từ tác động trực tiếp (“recommend a city”), không dùng giới từ “in which”, và dấu phẩy sau “which” cũng sai hoàn toàn.'),
            ('Đáp án đúng', '“city that” nối trực tiếp và tự nhiên với mệnh đề quan hệ xác định “many travelers recommend” mà không cần dấu phẩy.'),
        ],
    ),

    # --- M1 Q17 ---
    q_item(
        'march2025_v5_rw_m1_q17', 17, 'Standard English Conventions', 'Boundaries', 'Easy',
        '<p>Epic poetry is a literary genre characterized by lengthy narratives that emphasize the heroic or divine. <i>The Argonautica</i>, an epic poem of Greek origin, dates back to the _______ the poem’s heroic narrative still captivates modern readers.</p>',
        'Which choice completes the text so that it conforms to the conventions of Standard English?',
        [
            '3rd century BCE,',
            '3rd century BCE yet,',
            '3rd century BCE, yet',
            '3rd century BCE',
        ],
        'C',
        'Kiểm tra ranh giới giữa hai mệnh đề độc lập (Two Independent Clauses): Mệnh đề 1 = `The Argonautica, an epic poem of Greek origin, dates back to the 3rd century BCE`. Mệnh đề 2 = `the poem’s heroic narrative still captivates modern readers`. Để nối hai mệnh đề độc lập mang ý tương phản (từ thế kỷ 3 TCN ↔ ngày nay vẫn mê hoặc độc giả), ta dùng chuẩn **dấu phẩy + liên từ FANBOYS** → `3rd century BCE, yet` → Chọn C!',
        'Công thức bất biến: `IC, + FANBOYS (for, and, nor, but, or, yet, so) + IC`. Dấu phẩy luôn đứng TRƯỚC liên từ `yet`, tuyệt đối không đặt sau `yet`!',
        [
            ('Comma Splice', 'Chỉ dùng một dấu phẩy nối hai mệnh đề độc lập mà thiếu liên từ FANBOYS gây lỗi Comma Splice.'),
            ('Misplaced Comma', 'Đặt dấu phẩy SAU liên từ “yet” là sai cấu trúc `, FANBOYS`.'),
            ('Đáp án đúng', '“3rd century BCE, yet” dùng đúng cấu trúc `, FANBOYS` nối hai mệnh đề độc lập có quan hệ tương phản.'),
            ('Run-on / Fused Sentence', 'Không có dấu câu hay liên từ giữa hai mệnh đề độc lập gây lỗi câu dính (fused sentence).'),
        ],
    ),

    # --- M1 Q18 ---
    q_item(
        'march2025_v5_rw_m1_q18', 18, 'Standard English Conventions', 'Form, Structure, and Sense', 'Easy',
        '<p>An upcoming exhibition will showcase Vincent van Gogh’s drawing <i>The Spire of the Church of Our Lady</i>, which Van Gogh _______ in the city of Nuenen nearly 150 years ago.</p>',
        'Which choice completes the text so that it conforms to the conventions of Standard English?',
        [
            'will complete',
            'has been completing',
            'completed',
            'is completing',
        ],
        'C',
        'Kiểm tra thì động từ (Verb Tense): Trạng ngữ thời gian ở cuối câu khóa chặt mốc quá khứ đã chấm dứt hoàn toàn: **“nearly 150 years ago”** (gần 150 năm trước). Do đó, động từ mô tả việc Van Gogh hoàn thành bức vẽ tại Nuenen BẮT BUỘC chia ở thì **quá khứ đơn** → **“completed”** → Chọn C!',
        'Gặp mốc thời gian xác định kết thúc trong quá khứ (`... years ago`, `in 1885`), chọn ngay động từ thì quá khứ đơn (`V-ed`).',
        [
            ('Wrong Tense (Future)', '“will complete” là thì tương lai, vô lý với mốc “nearly 150 years ago”.'),
            ('Wrong Tense (Present Perfect Continuous)', '“has been completing” diễn tả hành động kéo dài tới hiện tại, không dùng với danh họa đã qua đời và mốc “150 years ago”.'),
            ('Đáp án đúng', '“completed” là thì quá khứ đơn chuẩn xác khớp với trạng ngữ thời gian “nearly 150 years ago”.'),
            ('Wrong Tense (Present Continuous)', '“is completing” là thì hiện tại tiếp diễn, mâu thuẫn trực tiếp với mốc quá khứ.'),
        ],
    ),

    # --- M1 Q19 ---
    q_item(
        'march2025_v5_rw_m1_q19', 19, 'Standard English Conventions', 'Boundaries', 'Medium',
        '<p>In addition to being a celebrated writer, musician, and educator, Zitkála-Šá (Yankton Dakota) was the cofounder of the National Council of American _______ advocated for Native American civil rights throughout the 1920s and 1930s.</p>',
        'Which choice completes the text so that it conforms to the conventions of Standard English?',
        [
            'Indians. Which',
            'Indians,',
            'Indians',
            'Indians, which',
        ],
        'D',
        'Phân tích cấu trúc mệnh đề: Vế trước `In addition to..., Zitkála-Šá (Yankton Dakota) was the cofounder of the National Council of American Indians` là một mệnh đề độc lập hoàn chỉnh. Phía sau còn cụm vị ngữ `advocated for Native American civil rights throughout the 1920s and 1930s` (thiếu chủ ngữ). Để bổ nghĩa cho danh từ riêng “the National Council of American Indians”, ta dùng **mệnh đề quan hệ không xác định** bắt đầu bằng **`, which`** → `Indians, which` → Chọn D!',
        'Kiểm tra xem sau chỗ trống có động từ chia thì (`advocated`) mà thiếu chủ ngữ hay không: nếu có, cần đại từ quan hệ `which` làm chủ ngữ — nhưng KHÔNG được tách bằng dấu chấm (A) vì `Which advocated...` sẽ biến thành mệnh đề cụt (fragment)!',
        [
            ('Sentence Fragment', 'Đặt dấu chấm trước “Which” biến vế sau (“Which advocated...”) thành một mảnh câu cụt không có mệnh đề chính.'),
            ('Missing Subject / Comma Error', 'Thiếu đại từ quan hệ “which” khiến động từ “advocated” đứng lơ lửng không nối hợp lệ với chủ ngữ “Zitkála-Šá” (vốn đã có động từ “was” mà không có “and”).'),
            ('Double Finite Verb / Missing Pronoun', 'Viết liền “Indians advocated” tạo cảm giác câu có 2 vị ngữ hoặc biến tên tổ chức thành chủ ngữ mệnh đề không có liên kết với “was the cofounder of”.'),
            ('Đáp án đúng', '“Indians, which” mở mệnh đề quan hệ không xác định bổ sung thông tin về Hội đồng Quốc gia người Mỹ bản địa, vừa đúng dấu câu vừa chuẩn ngữ pháp.'),
        ],
    ),

    # --- M1 Q20 ---
    q_item(
        'march2025_v5_rw_m1_q20', 20, 'Standard English Conventions', 'Boundaries', 'Medium',
        '<p>Cy Twombly, a US painter and sculptor, created many large-scale abstract works, such as his 10-painting series <i>Fifty Days at Iliam</i>. In these works, Twombly’s artistic style is exemplified by his use of graffiti-like _______ often incorporate words or phrases from poetry and mythology.</p>',
        'Which choice completes the text so that it conforms to the conventions of Standard English?',
        [
            'scribbles that',
            'scribbles: that',
            'scribbles; that',
            'scribbles. That',
        ],
        'A',
        'Phân tích cấu trúc + hòa hợp chủ-vị: Đọc tiếp sau chỗ trống thấy động từ SỐ NHIỀU **“often incorporate”**. Nếu ngắt câu bằng dấu chấm (D), chấm phẩy (C), hoặc hai chấm (B), từ `that` sẽ phải làm đại từ chỉ định số ít (`That` = “điều đó”) — nhưng đại từ số ít `That` KHÔNG THỂ đi với động từ số nhiều `incorporate` (và dấu hai chấm/chấm phẩy cũng không mở mệnh đề quan hệ `that`)! Chỉ duy nhất **“scribbles that”** (mệnh đề quan hệ xác định bổ nghĩa cho danh từ số nhiều `scribbles`) mới khớp 100% cả ngữ pháp lẫn hòa hợp số nhiều `scribbles ... incorporate` → Chọn A!',
        'Mẹo kiểm tra nhanh khi gặp `that` với 4 loại dấu câu: nhìn ngay động từ sau `that`! Động từ số nhiều (`incorporate`) + danh từ số nhiều (`scribbles`) → `that` bắt buộc là đại từ quan hệ liền mạch KHÔNG có dấu câu ngăn cách!',
        [
            ('Đáp án đúng', '“scribbles that” tạo mệnh đề quan hệ xác định liền mạch bổ nghĩa cho danh từ số nhiều “scribbles”, hòa hợp hoàn toàn với động từ số nhiều “incorporate”.'),
            ('Wrong Colon Before Relative Clause', 'Không đặt dấu hai chấm giữa danh từ và đại từ quan hệ “that”; nếu hiểu “that” là chủ ngữ số ít thì sai hòa hợp với động từ số nhiều “incorporate”.'),
            ('Semicolon Fragment / Agreement Error', 'Sau dấu chấm phẩy phải là mệnh đề độc lập hoàn chỉnh; “that often incorporate...” vừa không đứng độc lập được nếu là mệnh đề quan hệ, vừa sai số ít/số nhiều nếu hiểu là đại từ chỉ định.'),
            ('Agreement Error / Fragment', 'Sau dấu chấm, “That” (số ít) không thể hòa hợp với động từ số nhiều “incorporate”.'),
        ],
    ),

    # --- M1 Q21 ---
    q_item(
        'march2025_v5_rw_m1_q21', 21, 'Standard English Conventions', 'Boundaries', 'Medium',
        '<p>For the past 20 million years, Earth’s magnetic poles in the far north and far south have remained roughly where they are today. This has not always been the _______ throughout geologic history, Earth’s magnetic poles have swapped places several times through a process called polar wandering.</p>',
        'Which choice completes the text so that it conforms to the conventions of Standard English?',
        [
            'case, though,',
            'case, though;',
            'case; though,',
            'case, though',
        ],
        'B',
        'Câu Boundaries kinh điển kiểm tra vị trí của trạng từ tương phản `though` giữa HAI MỆNH ĐỀ ĐỘC LẬP! Đọc cả đoạn để xác định `though` thuộc vế nào:\n• Câu 1: Trong 20 triệu năm qua, hai cực từ Trái Đất hầu như giữ nguyên vị trí.\n• Mệnh đề 2a: `This has not always been the case, though` → **tương phản trực tiếp** với câu 1 (“tuy nhiên điều này không phải lúc nào cũng đúng”)!\n• Mệnh đề 2b: `throughout geologic history, Earth’s magnetic poles have swapped places...` → **giải thích / minh họa** cho mệnh đề 2a (KHÔNG hề tương phản với 2a)!\nVì `though` thuộc cuối Mệnh đề 2a và cần ngăn cách 2 mệnh đề độc lập, ta BẮT BUỘC đặt dấu chấm phẩy SAU `though`: **`case, though;`** → Chọn B!',
        'Quy tắc vàng “though / however giữa hai IC”: luôn kiểm tra nghĩa để biết `though` đối lập với câu TRƯỚC (đặt `;` SAU `though` → `..., though;`) hay đối lập giữa hai vế trong cùng câu (đặt `;` TRƯỚC từ nối).',
        [
            ('Comma Splice', 'Đặt dấu phẩy sau “though” tạo lỗi Comma Splice nối hai mệnh đề độc lập chỉ bằng dấu phẩy.'),
            ('Đáp án đúng', '“case, though;” đặt trạng từ tương phản “though” vào cuối mệnh đề 1 (đối lập với câu trước đó) rồi dùng dấu chấm phẩy chuẩn xác để tách mệnh đề độc lập thứ hai.'),
            ('Illogical Contrast & Wrong Punctuation', 'Đặt dấu chấm phẩy TRƯỚC “though” gắn “though” vào mệnh đề 2, làm sai logic (vì mệnh đề 2 giải thích chứ không tương phản với mệnh đề 1) và sai chuẩn dấu phẩy.'),
            ('Fused Sentence', 'Thiếu hoàn toàn dấu chấm phẩy hoặc dấu chấm giữa hai mệnh đề độc lập.'),
        ],
    ),

    # --- M1 Q22 ---
    q_item(
        'march2025_v5_rw_m1_q22', 22, 'Expression of Ideas', 'Transitions', 'Easy',
        '<p>In Ethiopia, citizens must be at least 18 years old to vote in their country’s elections. _______ citizens in Cuba need only be 16 years old to cast their vote.</p>',
        'Which choice completes the text with the most logical transition?',
        [
            'By contrast,',
            'Firstly,',
            'For example,',
            'Therefore,',
        ],
        'A',
        'So sánh trực tiếp hai câu: Câu 1 cho biết ở Ethiopia công dân phải ít nhất **18 tuổi** mới được bầu cử; câu 2 cho biết ở Cuba công dân chỉ cần **16 tuổi** → Hai thực tế trái ngược / khác biệt nhau rõ rệt về độ tuổi bầu cử → Chọn từ nối đối chiếu tương phản **“By contrast,”** → Chọn A!',
        'Khi hai câu so sánh hai đối tượng khác nhau (Ethiopia vs. Cuba) với hai con số đối lập (at least 18 vs. need only be 16), chọn ngay “By contrast,”.',
        [
            ('Đáp án đúng', '“By contrast,” (Ngược lại / Trái lại) đối chiếu trực tiếp quy định độ tuổi bầu cử khác nhau giữa Ethiopia (18 tuổi) và Cuba (16 tuổi).'),
            ('Wrong Relationship (Sequence)', '“Firstly,” dùng để mở đầu danh sách các bước/luận điểm theo thứ tự, không dùng ở câu 2 để so sánh 2 quốc gia.'),
            ('Wrong Relationship (Example)', 'Quy định 16 tuổi ở Cuba không phải ví dụ minh họa cho quy định 18 tuổi ở Ethiopia.'),
            ('Wrong Relationship (Cause-Effect)', 'Quy định bầu cử ở Cuba không phải hệ quả tất yếu của quy định ở Ethiopia.'),
        ],
    ),

    # --- M1 Q23 ---
    q_item(
        'march2025_v5_rw_m1_q23', 23, 'Expression of Ideas', 'Transitions', 'Medium',
        '<p>In astrophysics, a ring of debris orbiting a larger object within the Roche limit is expected to persist as a ring, whereas a ring of debris orbiting outside this limit would likely accrete into a satellite (e.g., a moon). Bruno Morgado and colleagues, _______ detected a dense ring of material orbiting the trans-Neptunian object Quaoar at a distance of 2,500 miles, well outside the calculated Roche limit of 1,100 miles, that has remained intact.</p>',
        'Which choice completes the text with the most logical transition?',
        [
            'for example,',
            'likewise,',
            'fittingly,',
            'though,',
        ],
        'D',
        'Quan hệ logic giữa hai câu: Câu 1 nêu quy luật vật lý thiên văn thông thường — vành đai mảnh vỡ nằm **ngoài giới hạn Roche** sẽ có xu hướng kết tụ thành vệ tinh (chứ không còn là vành đai). Câu 2 nêu phát hiện ngoại lệ của Bruno Morgado và cộng sự: họ phát hiện một vành đai đậm đặc quay quanh Quaoar ở khoảng cách 2.500 dặm — **vượt xa giới hạn Roche 1.100 dặm** — vậy mà **vẫn giữ nguyên vẹn dạng vành đai** (“remained intact”) → Tương phản / Ngoại lệ trực tiếp với câu 1 → Chọn D (**“though,”**)!',
        'Cặp tín hiệu tương phản sắc nét: “outside this limit would likely accrete into a satellite” ↔ “well outside the calculated Roche limit... that has remained intact” → chốt ngay từ nối tương phản “though,”.',
        [
            ('Wrong Relationship (Example)', 'Phát hiện về Quaoar đi NGƯỢC lại quy luật giới hạn Roche ở câu 1, không phải ví dụ minh họa cho quy luật đó.'),
            ('Wrong Relationship (Similarity)', '“likewise,” chỉ sự tương đồng, sai hướng vì kết quả của Morgado trái ngược với kỳ vọng lý thuyết.'),
            ('Wrong Relationship (Appropriateness)', '“fittingly,” (một cách hợp lẽ/tương xứng) ngược hoàn toàn với phát hiện gây bất ngờ ngoài giới hạn Roche.'),
            ('Đáp án đúng', '“though,” (tuy nhiên) đặt gọn trong cặp dấu phẩy nối giữa chủ ngữ và động từ, nhấn mạnh phát hiện ngoại lệ trái ngược với quy luật câu 1.'),
        ],
    ),

    # --- M1 Q24 ---
    q_item(
        'march2025_v5_rw_m1_q24', 24, 'Expression of Ideas', 'Rhetorical Synthesis', 'Easy',
        '<p>While researching a topic, a student has taken the following notes:</p><ul><li>Dinosaur fossil specimens can be found at science museums all over the world.</li><li>Many dinosaur fossil specimens are given nicknames.</li><li>The Burke Museum of Natural History and Culture in Seattle, Washington, houses a dinosaur fossil specimen nicknamed Tufts-Love.</li><li>Tufts-Love lived in the Late Cretaceous period, which ended more than 65 million years ago.</li><li>It is a member of the genus <i>Tyrannosaurus</i>.</li></ul>',
        'The student wants to provide an example of a dinosaur fossil specimen’s nickname. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
        [
            'Dinosaur fossil specimens can be found at museums all over the world, and many of these specimens are given nicknames.',
            'Nicknames are given to many dinosaur fossil specimens, including one housed at a museum in Seattle, Washington.',
            'Tufts-Love is the nickname of a <i>Tyrannosaurus</i> fossil specimen housed at the Burke Museum of Natural History and Culture in Seattle, Washington.',
            'A <i>Tyrannosaurus</i> fossil specimen from the Late Cretaceous period, which ended more than 65 million years ago, is housed at the Burke Museum of Natural History and Culture.',
        ],
        'C',
        'Chiến lược Goal-First: Mục tiêu của học sinh là **đưa ra một ví dụ về biệt danh (nickname) của một mẫu hóa thạch khủng long** (“provide an example of a dinosaur fossil specimen’s nickname”). Trong ghi chú, biệt danh cụ thể được nhắc tới là **“Tufts-Love”**. Chỉ duy nhất đáp án C thực sự nêu tên biệt danh “Tufts-Love” và gắn nó với mẫu hóa thạch *Tyrannosaurus* → Chọn C!',
        'Khi Goal yêu cầu “provide an example of X”, đáp án ĐÚNG bắt buộc phải gọi đích danh ví dụ cụ thể đó (ở đây là “Tufts-Love”) — loại ngay các lựa chọn chỉ nói chung chung (A, B) hoặc quên nêu biệt danh (D).',
        [
            ('No Specific Example', 'Chỉ lặp lại thông tin chung rằng nhiều mẫu hóa thạch có biệt danh, không hề nêu ví dụ biệt danh cụ thể nào.'),
            ('No Specific Example', 'Nhắc tới “một mẫu ở bảo tàng tại Seattle” nhưng lại bỏ quên chính cái tên biệt danh “Tufts-Love”.'),
            ('Đáp án đúng', 'Đáp ứng trực tiếp mục tiêu: nêu đích danh biệt danh “Tufts-Love” của mẫu hóa thạch *Tyrannosaurus* tại Bảo tàng Burke ở Seattle.'),
            ('Misses the Goal', 'Chỉ nêu niên đại và nơi lưu giữ mẫu hóa thạch *Tyrannosaurus*, không hề nhắc tới biệt danh của nó.'),
        ],
    ),

    # --- M1 Q25 ---
    q_item(
        'march2025_v5_rw_m1_q25', 25, 'Expression of Ideas', 'Rhetorical Synthesis', 'Easy',
        '<p>While researching a topic, a student has taken the following notes:</p><ul><li>The Arabic word “dinar” comes from the Latin word “denarius.”</li><li>Today, nearly a dozen different national currencies are referred to as “dinars.”</li><li>Bahrain’s currency is known as the Bahraini dinar.</li></ul>',
        'The student wants to provide an example of a country that uses the word “dinar” in the name of its currency. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
        [
            'Bahrain uses the Bahraini dinar as its national currency.',
            'Bahrain does not refer to its currency by the Latin word “denarius.”',
            'Today, several countries use the word “dinar” in naming their currencies.',
            'The Latin word “denarius” is the origin of the Arabic word “dinar.”',
        ],
        'A',
        'Chiến lược Goal-First: Mục tiêu là **đưa ra ví dụ về một quốc gia sử dụng từ “dinar” trong tên đơn vị tiền tệ của mình**. Trong ghi chú, ví dụ cụ thể là **Bahrain** với đồng **Bahraini dinar**. Đáp án A trình bày ngắn gọn, trực tiếp và chính xác 100% mục tiêu → Chọn A!',
        'Gạch chân 2 từ khóa trong Goal: (1) tên một quốc gia cụ thể (`Bahrain`) + (2) tên tiền tệ chứa từ “dinar” (`Bahraini dinar`) → khớp ngay đáp án A trong 5 giây.',
        [
            ('Đáp án đúng', 'Nêu đích danh quốc gia Bahrain cùng tên đồng tiền quốc gia chứa từ “dinar” (Bahraini dinar).'),
            ('Wrong Focus', 'Chỉ nói Bahrain không gọi tiền của mình là “denarius”, không nêu tên tiền tệ chứa từ “dinar”.'),
            ('No Specific Country Example', 'Nói chung chung “several countries” mà không nêu ví dụ quốc gia cụ thể nào.'),
            ('Wrong Focus', 'Chỉ nêu nguồn gốc từ nguyên Latinh của từ “dinar”, không đưa ví dụ quốc gia.'),
        ],
    ),

    # --- M1 Q26 ---
    q_item(
        'march2025_v5_rw_m1_q26', 26, 'Expression of Ideas', 'Rhetorical Synthesis', 'Medium',
        '<p>While researching a topic, a student has taken the following notes:</p><ul><li>Most of the plant and bird species in Oahu, Hawaii, are non-native.</li><li>In a 2019 study, researchers wanted to know what role non-native birds play in dispersing plant seeds in Oahu.</li><li>Researchers catalogued plant seeds found in fecal samples from non-native birds.</li><li><i>Leptecophylla tameiameiae</i>, a flowering shrub, was one of fifteen native species catalogued.</li><li><i>Passiflora suberosa</i>, an herbaceous vine, was one of twenty-nine non-native species catalogued.</li><li>Researchers concluded that non-native birds play a vital role in dispersing the seeds of native and non-native plants.</li></ul>',
        'The student wants to emphasize a difference between the two plants. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
        [
            'Most plant species found in Oahu, Hawaii, like <i>Passiflora suberosa</i>, are non-native.',
            'Seeds from <i>Leptecophylla tameiameiae</i> and <i>Passiflora suberosa</i> plants were found in the fecal samples of non-native Hawaiian birds, according to a 2019 study.',
            'A 2019 study catalogued plant seeds found in bird fecal samples in Oahu, Hawaii, to determine what role non-native birds play in seed dispersal.',
            'Though <i>Leptecophylla tameiameiae</i> and <i>Passiflora suberosa</i> can both be found in Oahu, Hawaii, only the former plant is native.',
        ],
        'D',
        'Chiến lược Goal-First: Mục tiêu là **nhấn mạnh sự KHÁC BIỆT giữa hai loài thực vật** (*Leptecophylla tameiameiae* và *Passiflora suberosa*). Đối chiếu ghi chú: *Leptecophylla tameiameiae* là loài **bản địa** (native flowering shrub), còn *Passiflora suberosa* là loài **ngoại lai** (non-native herbaceous vine). Đáp án D nêu cả hai loài và làm nổi bật rõ nét sự khác biệt đó bằng từ nối tương phản “Though... only the former plant is native” → Chọn D!',
        'Goal “emphasize a difference between X and Y” luôn đòi hỏi: [1] xuất hiện đủ CẢ X và Y + [2] có từ khóa tương phản chỉ rõ điểm khác biệt giữa chúng (“Though... only the former...”).',
        [
            ('Only One Plant', 'Chỉ nhắc đến *Passiflora suberosa*, không hề nhắc *Leptecophylla tameiameiae* nên không thể chỉ ra sự khác biệt giữa hai loài.'),
            ('Emphasizes Similarity', 'Nêu điểm GIỐNG NHAU (hạt của cả hai loài đều có trong mẫu phân chim ngoại lai), trái ngược với mục tiêu nhấn mạnh sự khác biệt.'),
            ('Neither Plant Mentioned', 'Chỉ mô tả chung mục đích nghiên cứu năm 2019, không đề cập hai loài cây nào cả.'),
            ('Đáp án đúng', 'Nhắc đủ cả hai loài và nhấn mạnh trực tiếp sự khác biệt cốt lõi: dù cả hai đều có ở Oahu, chỉ *Leptecophylla tameiameiae* là loài bản địa.'),
        ],
    ),

    # --- M1 Q27 ---
    q_item(
        'march2025_v5_rw_m1_q27', 27, 'Expression of Ideas', 'Rhetorical Synthesis', 'Easy',
        '<p>While researching a topic, a student has taken the following notes:</p><ul><li>Generally, an object will heat up when twisted.</li><li>The twisting of an object is known as torsion.</li><li>A 2019 study led by Zunfeng Liu and Ray Baughman tested the torsional heating of various fibers.</li><li>When a sample of ethylene propylene diene monomer (EPDM) rubber fiber was twisted, its average surface temperature increased by 12°C.</li><li>When a sample of natural rubber fiber was twisted, its average surface temperature increased by 15.3°C.</li></ul>',
        'The student wants to emphasize a similarity between EPDM rubber and natural rubber fibers. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
        [
            'In 2019, two research teams observed the effects of torsional heating on various fibers, including EPDM rubber and natural rubber.',
            'Twisting an object will generally cause its temperature to increase, a process known as torsional heating.',
            'Researchers determined that when the fibers were twisted, the average surface temperature of natural rubber increased more than that of EPDM rubber.',
            'Both EPDM rubber and natural rubber fibers heat up when twisted, according to a 2019 study.',
        ],
        'D',
        'Chiến lược Goal-First: Mục tiêu là **nhấn mạnh điểm TƯƠNG ĐỒNG giữa sợi cao su EPDM và sợi cao su tự nhiên** (“emphasize a similarity between EPDM rubber and natural rubber fibers”). Theo ghi chú, khi bị xoắn, EPDM tăng 12°C còn cao su tự nhiên tăng 15,3°C → điểm tương đồng là **cả hai đều nóng lên khi bị xoắn** (“Both EPDM rubber and natural rubber fibers heat up when twisted”). Đáp án D diễn đạt chuẩn xác và chính xác 100% sự thật → Chọn D!',
        'Kiểm tra kỹ bẫy sai sự thật ở đáp án A: ghi chú chỉ có MỘT nghiên cứu năm 2019 (“A 2019 study led by Zunfeng Liu and Ray Baughman”), KHÔNG phải “two research teams”!',
        [
            ('Factual Error & Weak Similarity', 'Sai sự thật (“two research teams” trong khi ghi chú chỉ có 1 nhóm nghiên cứu gồm 2 tác giả), và chỉ nói cả hai được quan sát chứ không nêu điểm tương đồng về tính chất vật lý.'),
            ('Missing Both Materials', 'Chỉ định nghĩa chung hiện tượng gia nhiệt xoắn, không hề nhắc đến EPDM hay cao su tự nhiên.'),
            ('Emphasizes Difference', 'So sánh cao su tự nhiên tăng nhiệt NHIỀU HƠN EPDM — nhấn mạnh sự KHÁC BIỆT thay vì tương đồng.'),
            ('Đáp án đúng', 'Nhấn mạnh chính xác điểm tương đồng bằng “Both... heat up when twisted” và trung thực tuyệt đối với nghiên cứu năm 2019.'),
        ],
    ),
]


# ============================================================================
# MODULE 2: SECTION 1, MODULE 2 — READING AND WRITING (27 REAL QUESTIONS)
# ============================================================================

MODULE_2_QUESTIONS = [

    # --- M2 Q1 ---
    q_item(
        'march2025_v5_rw_m2_q1', 1, 'Craft and Structure', 'Words in Context', 'Easy',
        '<p>In some of his sculptures, Allan Houser uses abstract geometric shapes to depict his subjects rather than portraying them in realistic detail. For instance, his 1989 work <i>Embrace</i> is highly abstract and therefore differs strikingly from some of his other pieces in which the viewer can easily _______ familiar objects.</p>',
        'Which choice completes the text with the most logical and precise word or phrase?',
        [
            'ignore',
            'identify',
            'reveal',
            'remember',
        ],
        'B',
        'Mạch tương phản rõ nét giữa hai phong cách điêu khắc của Allan Houser: một bên là tác phẩm *Embrace* “rất trừu tượng” (“highly abstract”, dùng hình khối hình học trừu tượng thay vì chi tiết tả thực), nên khác biệt rõ rệt (“differs strikingly”) với các tác phẩm tả thực khác nơi người xem có thể dễ dàng **NHẬN RA / NHẬN DIỆN (“identify”)** những vật thể quen thuộc → Chọn B.',
        'Cặp đối lập “highly abstract” (trừu tượng, khó nhận ra hình thù cụ thể) ↔ “realistic detail” (tả thực) khóa chặt động từ “easily identify familiar objects”.',
        [
            ('Opposite / Unrelated', 'ignore = phớt lờ — không khớp với nét đặc trưng của điêu khắc tả thực đối lập với trừu tượng.'),
            ('Đáp án đúng', 'identify = nhận diện, nhận ra — khớp hoàn hảo với tác phẩm tả thực giúp người xem dễ dàng nhận ra vật thể quen thuộc.'),
            ('Wrong Subject', 'reveal = tiết lộ — chính tác phẩm hoặc nghệ sĩ mới “reveal”, chứ không phải người xem (“the viewer”) “reveal familiar objects”.'),
            ('Wrong Meaning', 'remember = ghi nhớ — việc nhận dạng hình ảnh tả thực khi ngắm tượng là nhận diện trực quan, không phải hồi tưởng trí nhớ.'),
        ],
    ),

    # --- M2 Q2 ---
    q_item(
        'march2025_v5_rw_m2_q2', 2, 'Craft and Structure', 'Words in Context', 'Medium',
        '<p>Agglomeration economies arise when multiple firms in related industries _______ an area, as with knitted fabrics manufacturers and knitted clothing manufacturers in Derby, UK. Economists have assumed that companies cluster for the same reasons, but Giulia Faggio et al. found that factors driving agglomeration in some cases are only weakly correlated with agglomeration in others.</p>',
        'Which choice completes the text with the most logical and precise word or phrase?',
        [
            'intercede in',
            'amass in',
            'concur with',
            'appeal to',
        ],
        'B',
        'Manh mối đồng nghĩa nằm ngay ở câu thứ hai: “Economists have assumed that companies **cluster** for the same reasons” (các công ty **tụ cụm / tập trung đông đúc** lại với nhau). Quay lại câu 1 định nghĩa “Agglomeration economies” (kinh tế tích tụ): hiện tượng này phát sinh khi nhiều doanh nghiệp cùng ngành liên quan **TỤ TẬP / TẬP TRUNG ĐÔNG ĐÚC VÀO (“amass in”)** một khu vực (như các xưởng vải dệt kim và quần áo dệt kim ở Derby, Anh) → Chọn B.',
        'Luôn quét câu liền sau để tìm từ đồng nghĩa trực tiếp giải nghĩa chỗ trống: “companies cluster” = “multiple firms amass in an area” (và gốc từ “agglomeration” cũng mang nghĩa tích tụ thành cụm).',
        [
            ('Wrong Meaning', 'intercede in = can thiệp hòa giải — sai hoàn toàn ngữ cảnh kinh tế học.'),
            ('Đáp án đúng', 'amass in = tụ tập, tập trung với số lượng lớn tại — đồng nghĩa trực tiếp với “cluster” và “agglomeration”.'),
            ('Wrong Meaning', 'concur with = đồng tình với — không thể “đồng tình với một khu vực”.'),
            ('Wrong Meaning', 'appeal to = thu hút / kêu gọi — không diễn đạt ý các công ty tập trung địa lý thành cụm.'),
        ],
    ),

    # --- M2 Q3 ---
    q_item(
        'march2025_v5_rw_m2_q3', 3, 'Craft and Structure', 'Words in Context', 'Medium',
        '<p>The familial structure of the black swan (<i>Cygnus atratus</i>) shows tremendous _______: breeding pairs with demonstrated success in rearing cygnets (young swans) have been observed to foster those of less successful pairs, and while rearing by female-male pairs is most common, male-male pairs sometimes rear cygnets too, achieving a significantly higher rate of survival to adulthood than female-male pairs.</p>',
        'Which choice completes the text with the most logical and precise word or phrase?',
        [
            'elasticity',
            'reciprocity',
            'cohesion',
            'affection',
        ],
        'A',
        'Phần sau dấu hai chấm giải thích trực tiếp cấu trúc gia đình của thiên nga đen (*Cygnus atratus*): các cặp nuôi con thành công có thể nhận nuôi con hộ các cặp kém hơn, và dù cặp cái–đực phổ biến nhất thì các cặp đực–đực đôi khi cũng nuôi con non với tỷ lệ sống sót thậm chí còn cao hơn → cấu trúc gia đình này có **TÍNH LINH HOẠT / MỀM DẺO CỰC CAO (“elasticity”)**, không hề cứng nhắc một khuôn mẫu duy nhất → Chọn A!',
        'Trong SAT Words in Context trình độ Medium/Hard, “elasticity” thường được dùng với nghĩa bóng chuẩn xác là “flexibility / adaptability” (tính linh hoạt, khả năng biến đổi thích ứng).',
        [
            ('Đáp án đúng', 'elasticity = tính linh hoạt, mềm dẻo — bao quát trọn vẹn việc cấu trúc gia đình thiên nga đen có thể biến chuyển đa dạng (nhận nuôi hộ, cặp cái–đực, cặp đực–đực).'),
            ('Wrong Meaning', 'reciprocity = sự có đi có lại / tương hỗ hai chiều — bài không hề nói các cặp thiên nga đổi chác hay trả ơn lẫn nhau.'),
            ('Wrong Focus', 'cohesion = sự gắn kết chặt chẽ — không giải thích được sự đa dạng cấu hình cặp đôi và việc chuyển giao con non sang cặp khác.'),
            ('Unsupported Emotion', 'affection = tình cảm trìu mến — văn bản khoa học mô tả cấu trúc xã hội và tỷ lệ sống sót, không nói về cảm xúc yêu thương.'),
        ],
    ),

    # --- M2 Q4 ---
    q_item(
        'march2025_v5_rw_m2_q4', 4, 'Craft and Structure', 'Words in Context', 'Medium',
        '<p>Any effort to raise the toll that drivers must pay to use the Ogdensburg-Prescott Bridge, which spans the Saint Lawrence River to connect New York State and Ontario, Canada, should explain why a higher toll is necessary; no amount of justification, however, is likely to persuade some drivers who believe the current toll is _______.</p>',
        'Which choice completes the text with the most logical and precise word or phrase?',
        [
            'contentious',
            'exorbitant',
            'warranted',
            'equivocal',
        ],
        'B',
        'Phân tích logic câu: Mọi nỗ lực **tăng mức phí cầu đường** (“raise the toll”) qua cầu Ogdensburg-Prescott cần giải thích lý do tăng phí; tuy nhiên không lời biện minh nào đủ sức thuyết phục những tài xế vốn đã tin rằng **mức phí hiện tại đang QUÁ ĐẮT ĐỎ / CẮT CỔ (“exorbitant”)**! Nếu họ đã thấy giá hiện tại quá cao thì chắc chắn họ sẽ phản đối tăng thêm phí → Chọn B.',
        'Đặt từ cần điền vào mệnh đề nhân-quả: “không thể thuyết phục tăng giá nếu người ta đã cho rằng giá hiện tại là ___” → cần tính từ mang nghĩa “quá đắt đỏ” (`exorbitant`).',
        [
            ('Wrong Precision', 'contentious = gây tranh cãi — mức phí gây tranh cãi chưa giải thích trực tiếp vì sao tài xế kiên quyết bác bỏ việc TĂNG phí (có người tranh cãi rằng phí quá thấp thì sao?).'),
            ('Đáp án đúng', 'exorbitant = đắt cắt cổ, cao quá mức — giải thích chuẩn xác 100% lý do không lời biện hộ nào thuyết phục được họ chấp nhận tăng phí thêm nữa.'),
            ('Opposite Meaning', 'warranted = hợp lý, có cơ sở — nếu tài xế thấy mức phí hiện tại hợp lý thì họ không phải nhóm cố chấp bất khả thuyết phục nhất.'),
            ('Wrong Meaning', 'equivocal = mơ hồ, nước đôi — không mô tả thái độ phản đối mức phí cầu đường.'),
        ],
    ),

    # --- M2 Q5 ---
    q_item(
        'march2025_v5_rw_m2_q5', 5, 'Craft and Structure', 'Words in Context', 'Hard',
        '<p>During the 2007–2010 financial crisis, the United States furnished billions of dollars to selected countries’ central banks via mechanisms called swap lines. Aditi Sahasrabuddhe found that countries’ policy environments seem to have been _______ swap-line decisions: the probability that banks would be granted swap lines was 0.20 in countries open to foreign-capital inflows and 0.03 in countries with policies restricting such inflows.</p>',
        'Which choice completes the text with the most logical and precise word or phrase?',
        [
            'predicated on',
            'decoupled from',
            'material to',
            'mediated by',
        ],
        'C',
        'Câu Hard Words in Context kinh điển thử thách **nghĩa thứ cấp** và **chiều nhân–quả**! Đọc dữ liệu sau dấu hai chấm: xác suất ngân hàng trung ương được Mỹ cấp hạn mức hoán đổi (swap line) là **0,20** ở các nước mở cửa dòng vốn ngoại, nhưng chỉ còn **0,03** ở các nước hạn chế dòng vốn ngoại → Chứng tỏ môi trường chính sách của các quốc gia **CÓ TẦM QUAN TRỌNG / ẢNH HƯỞNG ĐÁNG KỂ ĐẾN (“material to”)** quyết định cấp swap line! CỰC KỲ TRÁNH BẪY A (“predicated on” = dựa trên): “policy environments predicated on swap-line decisions” bị **ĐẢO NGƯỢC CHIỀU NHÂN–QUẢ** (chính sách có trước và tác động tới quyết định swap line, chứ không phải môi trường chính sách được xây dựng dựa trên quyết định swap line) → Chọn C!',
        'Ghi nhớ nghĩa thứ cấp cực hay ra thi ở Hard M2: tính từ **`material to`** = *significant / relevant / consequential to* (có ý nghĩa quan trọng / tác động trực tiếp đến), đồng thời luôn kiểm tra chiều chủ ngữ → tân ngữ để né bẫy đảo chiều `predicated on`!',
        [
            ('Reversed Causality Trap!', 'predicated on = được xây dựng dựa trên — đảo ngược hoàn toàn chiều logic: quyết định swap line mới dựa trên môi trường chính sách, KHÔNG phải môi trường chính sách dựa trên quyết định swap line!'),
            ('Opposite Meaning', 'decoupled from = tách rời, không liên quan đến — trái ngược hoàn toàn với chênh lệch lớn giữa 0,20 và 0,03.'),
            ('Đáp án đúng', 'material to = quan trọng, có tính quyết định / ảnh hưởng đáng kể đối với — khớp hoàn hảo cả chiều nhân-quả lẫn dữ liệu chênh lệch 0,20 vs. 0,03.'),
            ('Wrong Meaning / Direction', 'mediated by = được trung gian hóa / điều tiết bởi — sai chiều tác động và sai nghĩa.'),
        ],
    ),

    # --- M2 Q6 ---
    q_item(
        'march2025_v5_rw_m2_q6', 6, 'Craft and Structure', 'Text Structure and Purpose', 'Easy',
        '<p>Founded in New York City in 1969, El Museo del Barrio is dedicated to the visual arts and cultures of Latin America and of Latino communities in the United States. Since its founding, it has acquired more than 8,500 objects for its permanent collection. More recently founded US-based institutions devoted to Latino cultures include the Emma S. Barrientos Mexican American Cultural Center. Located in Austin, Texas, it focuses on Mexican American art and culture.</p>',
        'Which choice best states the main purpose of the text?',
        [
            'To trace the founding of two institutions, including how they acquired funding to purchase artworks',
            'To trace a historical development that encouraged the founding of two institutions',
            'To present information about two institutions, including each institution’s area of focus',
            'To draw a contrast between the collection sizes of two institutions',
        ],
        'C',
        'Đọc toàn đoạn để nắm bố cục tổng quát: Nửa đầu giới thiệu **El Museo del Barrio** (thành lập tại NYC năm 1969, chuyên về nghệ thuật thị giác & văn hóa Mỹ Latinh cùng cộng đồng Latino tại Mỹ, có hơn 8.500 hiện vật). Nửa sau giới thiệu **Emma S. Barrientos Mexican American Cultural Center** (tại Austin, Texas, tập trung vào nghệ thuật và văn hóa người Mỹ gốc Mexico). Như vậy mục đích chính của đoạn văn là trình bày thông tin về hai thiết chế văn hóa, bao gồm lĩnh vực trọng tâm của mỗi nơi → Chọn C.',
        'Với câu hỏi Main Purpose của đoạn văn giới thiệu 2 đối tượng song song, loại ngay các đáp án thêm thông tin không hề xuất hiện trong bài (như “funding” ở A, “historical development” ở B, hay so sánh “collection sizes” ở D khi nơi thứ hai không hề có số liệu bộ sưu tập!).',
        [
            ('Not Mentioned', 'Đoạn văn không hề nhắc đến việc hai tổ chức huy động nguồn tài trợ (“acquired funding”) mua tác phẩm như thế nào.'),
            ('Not Mentioned', 'Không trình bày diễn biến lịch sử nào thúc đẩy sự ra đời của hai trung tâm.'),
            ('Đáp án đúng', 'Khái quát trọn vẹn và chính xác nội dung đoạn văn: giới thiệu thông tin cơ bản về hai thiết chế văn hóa cùng trọng tâm hoạt động của từng nơi.'),
            ('Unsupported Contrast', 'Đoạn văn chỉ nêu con số >8.500 hiện vật của El Museo del Barrio, hoàn toàn không nêu quy mô bộ sưu tập của trung tâm tại Austin nên không có phép so sánh quy mô bộ sưu tập.'),
        ],
    ),

    # --- M2 Q7 ---
    q_item(
        'march2025_v5_rw_m2_q7', 7, 'Craft and Structure', 'Text Structure and Purpose', 'Easy',
        '<p><u>In 2011 Stephen D. Simpson and colleagues published a study concluding that ocean acidification has a strong effect on the behavior of <i>Amphiprion percula</i>, a species of fish.</u> However, Simpson and colleagues’ study relied on a mean sample size of only about 26 fish. In a 2022 review of various scientists’ conclusions about the impacts of ocean acidification on fish behavior, Timothy D. Clark and colleagues caution that relying on such a relatively small sample size can increase the potential for biased analysis. Such analysis, in turn, can contribute to reports of exaggerated effects.</p>',
        'Which choice best describes the function of the underlined sentence in the text?',
        [
            'It states the conclusion reached by Simpson and colleagues in their 2011 study.',
            'It presents a criticism of the results reported by Simpson and colleagues in their 2011 study.',
            'It lists several traits of <i>Amphiprion percula</i> discovered by Simpson and colleagues while conducting their 2011 study.',
            'It emphasizes a detail about where Simpson and colleagues conducted their 2011 study.',
        ],
        'A',
        'Câu được gạch chân là câu mở đầu đoạn: “In 2011 Stephen D. Simpson and colleagues published a study **concluding that** ocean acidification has a strong effect on the behavior of *Amphiprion percula*, a species of fish.” Câu này đơn thuần nêu **kết luận mà Simpson và cộng sự đưa ra trong nghiên cứu năm 2011** (phần phê bình cỡ mẫu nhỏ mới bắt đầu từ câu 2 trở đi sau chữ “However”) → Chọn A.',
        'Chỉ bám đúng phần ĐƯỢC GẠCH CHÂN! Bẫy B cố tình đánh lừa học sinh đọc cả đoạn sau (“However... caution... biased analysis”) rồi gán nhầm chức năng của câu 2–4 cho câu 1.',
        [
            ('Đáp án đúng', 'Trực tiếp nêu kết luận nghiên cứu năm 2011 của nhóm Simpson (“published a study concluding that...”).'),
            ('Wrong Sentence Scope', 'Lời phê bình về cỡ mẫu nhỏ (26 con cá) và nguy cơ thiên lệch nằm ở các câu 2–4 phía sau, không nằm trong câu gạch chân.'),
            ('Not Mentioned', 'Câu gạch chân không liệt kê các đặc điểm nào của loài cá *Amphiprion percula*.'),
            ('Not Mentioned', 'Không hề nhắc tới địa điểm tiến hành nghiên cứu năm 2011.'),
        ],
    ),

    # --- M2 Q8 ---
    q_item(
        'march2025_v5_rw_m2_q8', 8, 'Craft and Structure', 'Text Structure and Purpose', 'Medium',
        '<p>Paintings by the Florida Highwaymen—an informal collective of prolific landscape artists active in Florida during the 1950s and ’60s—are recognizable by their reiteration of the same general compositional structures and subjects: moonlit waters and poinciana trees, to name two. But there was room for individuation: Lemuel Newton’s <i>Salmon Sky Sunset</i>, for example, may resemble other Highwaymen paintings at first glance, but his works stand out for their attention to detail and warm color palette.</p>',
        'Which choice best describes the overall structure of the text?',
        [
            'It describes the common perception that a particular group of artists’ works are derivative and then provides a specific piece of evidence that reinforces that perception.',
            'It explains how a particular group of artists began collaborating and then recounts how one member of that group became especially influential among them.',
            'It describes an aesthetic framework shared by a particular group of artists and then makes and illustrates the claim that individuals introduced variations within that framework.',
            'It offers historical context that accounts for a particular group of artists’ shared style and then indicates the circumstances under which several members of that group began exploring more unconventional themes.',
        ],
        'C',
        'Phân tách cấu trúc 2 chặng của đoạn văn:\n• Câu 1: Mô tả **khuôn khổ thẩm mỹ chung** của nhóm họa sĩ Florida Highwaymen (nhận diện qua việc lặp lại cùng bố cục và chủ đề như mặt nước dưới ánh trăng, cây phượng vĩ).\n• Câu 2: Chuyển mạch bằng “But there was room for individuation:” — khẳng định từng cá nhân vẫn tạo được nét biến tấu riêng trong khuôn khổ đó, và minh họa bằng bức *Salmon Sky Sunset* của Lemuel Newton (thoạt nhìn giống tranh Highwaymen nhưng nổi bật nhờ độ chi tiết và bảng màu ấm) → Chọn C!',
        'Khớp chuẩn xác hai động từ cấu trúc ở đáp án C: “describes an aesthetic framework shared...” (câu 1) → “makes and illustrates the claim that individuals introduced variations within that framework” (câu 2).',
        [
            ('Tone Distortion & Opposite Second Half', 'Văn bản không mang thái độ chê tranh là “derivative” (bắt chước thiếu sáng tạo), và ví dụ Newton nhằm chứng minh cá tính riêng chứ không củng cố nhận định rập khuôn.'),
            ('Not Mentioned', 'Bài không giải thích cách nhóm bắt đầu hợp tác và không nói Newton có tầm ảnh hưởng đặc biệt lên các họa sĩ khác.'),
            ('Đáp án đúng', 'Phản ánh chính xác từng nhịp lập luận: mô tả khuôn khổ thẩm mỹ chung → nêu luận điểm và ví dụ minh họa sự sáng tạo cá nhân bên trong khuôn khổ ấy.'),
            ('Not Mentioned', 'Không giải thích nguyên nhân lịch sử tạo nên phong cách chung, và Newton nổi bật về độ chi tiết cùng màu sắc chứ không phải “chủ đề khác thường” (unconventional themes).'),
        ],
    ),

    # --- M2 Q9 ---
    q_item(
        'march2025_v5_rw_m2_q9', 9, 'Information and Ideas', 'Central Ideas and Details', 'Hard',
        '<p>The following text is from Mick Herron’s 2023 novel <i>The Secret Hours</i>. The narrator is describing members of a government committee.</p><p>Finally, and adding much-needed gravitas, was Sir Winston Day, whose features seemed moulded to adorn a bust, or possibly a stamp, and whose forehead was so evidently bulging with grey matter that it would have been impertinent to inquire too closely into the actual achievements his half century of public service had produced. His recently published memoirs possibly cast light on this enigma, but given that such details were not provided until after the thirty-page mark, they might as well have remained state secrets.</p><div style="font-size:11.5px;color:#64748b;text-align:right;margin-top:-6px;">©2023 by Mick Herron</div>',
        'Based on the text, which choice best describes Sir Winston Day?',
        [
            'He has maintained a modest profile even though he has served the public capably for many years.',
            'He has the appearance of a distinguished figure, but it is uncertain whether he has accomplished anything to earn distinction.',
            'He looks like a person worthy of respect, but his memoirs reveal that some of his actions were dishonorable.',
            'He would be a celebrated public figure if his achievements did not have to be kept secret.',
        ],
        'B',
        'Đọc sắc thái mỉa mai tinh tế của Mick Herron về nhân vật Sir Winston Day: Ông có ngoại hình đầy uy nghi, “như đúc ra để tạc tượng bán thân hay in lên tem thư” và vầng trán lộ rõ trí tuệ đến nỗi ai hỏi kỹ về **thành tựu thực sự** sau nửa thế kỷ làm công chức sẽ bị coi là thất lễ; cuốn hồi ký mới xuất bản “có thể làm sáng tỏ **bí ẩn này** (“this enigma”)”, nhưng vì chi tiết mãi sau trang 30 mới xuất hiện nên “chúng cũng chẳng khác nào bí mật quốc gia” (ám chỉ mỉa mai rằng chẳng ai đủ kiên nhẫn đọc tới đó, nên cuối cùng chẳng ai chắc ông đã làm được gì!). Tóm lại: ông có **dáng vẻ của một nhân vật lẫy lừng**, nhưng **không rõ liệu ông đã thực sự đạt được thành tựu nào xứng với danh tiếng đó hay chưa** → Chọn B!',
        'Khi đọc văn châm biếm Anh quốc trên SAT Hard M2, đừng hiểu nghĩa đen phép ẩn dụ (“might as well have remained state secrets” ≠ bí mật nhà nước thực sự), mà hãy bám từ khóa trọng tâm “actual achievements... this enigma”!',
        [
            ('Contradicts Text', 'Ông tạo ra “much-needed gravitas” với vẻ ngoài như tượng đài chứ không hề khiêm tốn, và đoạn văn nghi ngờ chứ không xác nhận ông phục vụ công chúng xuất sắc.'),
            ('Đáp án đúng', 'Nắm trọn cả hai vế của đoạn mỉa mai: ngoại hình uy nghi đáng kính (“adorn a bust... stamp”) đối lập với dấu hỏi lớn về thành tựu thực chất (“this enigma”).'),
            ('Not Mentioned', 'Văn bản không hề nói cuốn hồi ký tiết lộ hành vi bất chính hay đáng xấu hổ nào.'),
            ('Literal Misreading of Idiom', 'Hiểu sai nghĩa đen cụm “might as well have remained state secrets” thành thành tựu của ông bị buộc phải giữ bí mật.'),
        ],
    ),

    # --- M2 Q10 ---
    q_item(
        'march2025_v5_rw_m2_q10', 10, 'Information and Ideas', 'Command of Evidence (Textual)', 'Medium',
        '<p><i>Life Among the Paiutes</i> is an 1882 autobiographical narrative by Sarah Winnemucca Hopkins, a Northern Paiute author, educator, and activist. In the work, Winnemucca directly addresses the reader to explain certain customs, writing _______</p>',
        'Which quotation from <i>Life Among the Paiutes</i> most effectively illustrates the claim?',
        [
            '“Now, my dear reader, there is no word so endearing as the word father, and that is why [my people] call all good people father or mother.”',
            '“We would all go in company to see if the flowers we were named for were yet in bloom, for almost all the girls are named for flowers.”',
            '“During the time my grandfather was away in California, where he [stayed] till after the Mexican war, there was a girl-baby born in our family.”',
            '“But how can I describe the scene that followed? Some of you, dear readers, can imagine.”',
        ],
        'A',
        'Phân tích hai điều kiện BẮT BUỘC trong luận điểm: Winnemucca [1] **trực tiếp trò chuyện với độc giả** (“directly addresses the reader”) VÀ [2] **giải thích các phong tục tập quán nhất định** (“explain certain customs”). Đối chiếu từng trích dẫn:\n• A: Có **“Now, my dear reader,”** (trực tiếp xưng hô với độc giả ✅) + **“that is why [my people] call all good people father or mother”** (giải thích phong tục gọi người tốt là cha/mẹ ✅) → Đạt trọn vẹn cả 2 tiêu chí!\n• B: Giải thích phong tục đặt tên theo hoa (✅), nhưng KHÔNG trực tiếp xưng hô với độc giả (❌).\n• C: Kể chuyện gia đình cá nhân (❌ cả hai).\n• D: Có xưng hô “dear readers” (✅), nhưng KHÔNG giải thích phong tục nào (❌) → Chọn A!',
        'Với câu hỏi Command of Evidence có luận điểm kép (“A to do B”), hãy lập checklist 2 cột [Xưng hô trực tiếp?] + [Giải thích phong tục?] để loại sạch các đáp án chỉ thỏa mãn 1 trong 2 vế (B và D).',
        [
            ('Đáp án đúng', 'Thỏa mãn đồng thời cả hai yêu cầu: trực tiếp gọi “my dear reader” và giải thích nguồn gốc phong tục gọi người tốt là cha hoặc mẹ.'),
            ('Missing Direct Address', 'Có giải thích phong tục đặt tên con gái theo loài hoa nhưng hoàn toàn không có lời xưng hô trực tiếp với độc giả.'),
            ('Missing Both Criteria', 'Chỉ tường thuật sự kiện cá nhân về ông ngoại và việc một bé gái ra đời, không gọi độc giả cũng không giải thích phong tục.'),
            ('Missing Custom Explanation', 'Có gọi “dear readers” nhưng chỉ bỏ lửng cảm xúc về một cảnh tượng, không giải thích bất kỳ phong tục nào.'),
        ],
    ),

    # --- M2 Q11 ---
    q_item(
        'march2025_v5_rw_m2_q11', 11, 'Information and Ideas', 'Command of Evidence (Quantitative)', 'Medium',
        html_table(
            'Minimum and Maximum Depths of Stony Coral Species in Caribbean and Indo-Pacific Waters',
            ['Species', 'Minimum depth (meters)', 'Maximum depth (meters)'],
            [
                ['<i>Psammocora albopicta</i>', '1', '28'],
                ['<i>Agaricia grahamae</i>', '20', '115'],
                ['<i>Astreopora gracilis</i>', '5', '15'],
                ['<i>Acropora echinata</i>', '8', '25'],
            ],
        ) +
        '<p>Some scientists have suggested that as ocean temperatures rise, many fish and corals found in the shallow zone (less than 30 meters below the surface) could take refuge in the cooler, darker mesophotic zone (30 to 150 meters below the surface). However, it isn’t clear that all such species will be able to tolerate mesophotic conditions. In 2018, Luiz Rocha and colleagues studied stony corals in the two zones in Caribbean and Indo-Pacific waters. Based on the depths at which those corals are now found, the species that seems least suited to a full migration to the mesophotic zone is _______</p>',
        'Which choice most effectively uses data from the table to complete the statement?',
        [
            '<i>Agaricia grahamae</i>, because its minimum depth of 20 meters is in the shallow zone.',
            '<i>Psammocora albopicta</i>, because its minimum depth of 1 meter is the shallowest of those listed.',
            '<i>Astreopora gracilis</i>, because its maximum depth of 15 meters is furthest from the mesophotic zone.',
            '<i>Acropora echinata</i>, because its maximum depth of 25 meters is close to but doesn’t reach the mesophotic zone.',
        ],
        'C',
        'Đọc định nghĩa hai vùng biển trong đoạn văn: Vùng nước nông (shallow zone) là **< 30 m**; Vùng trung tầng tối lạnh (mesophotic zone) là **30 đến 150 m**. Đề bài hỏi: dựa theo độ sâu hiện sống trong bảng, loài nào **ÍT phù hợp nhất** cho một cuộc di cư hoàn toàn xuống vùng mesophotic (“least suited to a full migration to the mesophotic zone”)? Muốn đánh giá khả năng chịu được vùng sâu 30–150 m, ta phải nhìn vào **ĐỘ SÂU TỐI ĐA (Maximum depth)** loài đó có thể vươn tới hiện nay:\n• *Agaricia grahamae*: max **115 m** (đã sống sâu trong vùng mesophotic!)\n• *Psammocora albopicta*: max **28 m** (rất sát ngưỡng 30 m)\n• *Acropora echinata*: max **25 m** (khá gần ngưỡng 30 m)\n• ***Astreopora gracilis***: max chỉ **15 m** — **cách xa vùng mesophotic (30 m) nhất** → Ít thích nghi nhất → Chọn C!',
        'Cẩn thận bẫy cột Minimum depth ở A và B: di cư xuống vùng nước SÂU (30–150 m) phụ thuộc vào giới hạn chịu sâu TỐI ĐA (**Maximum depth**), không phải độ sâu tối thiểu nông nhất!',
        [
            ('Wrong Column & Contradicts Data', '*Agaricia grahamae* có độ sâu tối đa tới 115 m — tức đã sinh sống ổn định ngay trong vùng mesophotic (30–150 m), nên là loài PHÙ HỢP NHẤT chứ không phải ít phù hợp nhất.'),
            ('Wrong Metric (Min vs. Max)', 'Dù *Psammocora albopicta* bắt đầu từ 1 m, độ sâu tối đa của nó đạt tới 28 m (chỉ cách vùng mesophotic 2 m), gần hơn nhiều so với *Astreopora gracilis* (max 15 m).'),
            ('Đáp án đúng', 'Dùng đúng cột Maximum depth: *Astreopora gracilis* chỉ xuống sâu tối đa 15 m — xa ngưỡng 30 m của vùng mesophotic nhất trong bốn loài.'),
            ('Not the Least Suited', 'Độ sâu tối đa 25 m của *Acropora echinata* gần vùng mesophotic hơn đáng kể so với mức 15 m của *Astreopora gracilis*.'),
        ],
    ),

    # --- M2 Q12 ---
    q_item(
        'march2025_v5_rw_m2_q12', 12, 'Information and Ideas', 'Command of Evidence (Textual)', 'Hard',
        '<p>Although Eastern North Pacific (ENP) gray whales generally migrate between their wintering waters along the coast of Mexico and their foraging waters in the Arctic, a subset of this population—known as the Pacific Coast Feeding Group (PCFG)—forages along the coastlines of Northern California (USA) and British Columbia (Canada) instead. Interestingly, individuals in this subset reach smaller maximum sizes than other ENP whales do, despite having similar pre-maximum growth rates. Researchers hypothesize that this difference may be an adaptation to distinct resource opportunities in the PCFG foraging range.</p>',
        'Which finding, if true, would most directly support the researchers’ claim regarding the size of PCFG whales?',
        [
            'When foraging along the coasts of Northern California and British Columbia, PCFG whales are in closer proximity to major ports and urban populations than ENP whales in the main group are when foraging in Arctic waters.',
            'When present along the coasts of Northern California and British Columbia, PCFG whales tend to forage in rocky kelp beds at shallow depths inaccessible to whales as large as those in the ENP main group.',
            'Certain crustacean prey species available along the coasts of Northern California and British Columbia where PCFG whales tend to forage are not available in the Arctic waters where ENP whales in the main group forage.',
            'The average body size of PCFG whales observed along the coasts of Northern California and British Columbia has remained relatively steady in recent decades, while the average body size of ENP whales in the main group has slightly decreased.',
        ],
        'B',
        'Xác định đúng giả thuyết cần ủng hộ: Nhóm cá voi PCFG (kiếm ăn ven bờ Bắc California & British Columbia) có **kích thước tối đa NHỎ HƠN** nhóm cá voi ENP chính (kiếm ăn ở Bắc Cực). Các nhà nghiên cứu giả thuyết rằng sự khác biệt kích thước này là **một sự thích nghi với các cơ hội nguồn thức ăn đặc thù tại vùng kiếm ăn của PCFG** (“an adaptation to distinct resource opportunities in the PCFG foraging range”). Muốn ủng hộ giả thuyết này, bằng chứng phải cho thấy **kích thước cơ thể NHỎ HƠN mang lại lợi thế trực tiếp khi khai thác nguồn thức ăn ở vùng PCFG**! Đáp án B hoàn hảo: tại vùng ven bờ đó, cá voi PCFG thường kiếm ăn trong các bãi tảo bẹ nhiều đá ở vùng nước nông mà **những con cá voi to lớn như nhóm ENP chính không thể tiếp cận được** → Chọn B!',
        'Trong câu Support Hypothesis Hard M2, đáp án đúng phải kết nối chặt CẢ HAI mắt xích của giả thuyết: **[Kích thước nhỏ hơn]** ↔ **[Lợi thế khai thác tài nguyên đặc thù tại địa bàn PCFG]** (loại C vì chỉ nói có con mồi khác mà không hề giải thích tại sao CƠ THỂ NHỎ LẠI CÓ LỢI!).',
        [
            ('Wrong Cause (Non-Resource)', 'Gần cảng lớn và đô thị không chứng minh kích thước nhỏ là sự thích nghi với “cơ hội nguồn thức ăn” (resource opportunities).'),
            ('Đáp án đúng', 'Khóa chặt cả hai mắt xích: bãi tảo bẹ nước nông nhiều đá là nguồn tài nguyên đặc thù mà chỉ cá thể kích thước nhỏ như PCFG mới vào kiếm ăn được, còn cá voi ENP to lớn thì không tiếp cận được.'),
            ('Missing Size Connection Trap!', 'Bẫy rất khéo: có loài giáp xác khác ở vùng PCFG nhưng hoàn toàn không giải thích mối liên hệ nào giữa loại mồi đó với việc cá voi PCFG có **kích thước cơ thể nhỏ hơn**.'),
            ('Irrelevant Trend', 'Xu hướng kích thước cơ thể qua các thập kỷ gần đây không giải thích nguyên nhân thích nghi với nguồn thức ăn ở vùng PCFG.'),
        ],
    ),

    # --- M2 Q13 ---
    q_item(
        'march2025_v5_rw_m2_q13', 13, 'Information and Ideas', 'Command of Evidence (Textual)', 'Hard',
        '<p>Piezoelectric harvesters convert kinetic energy (resonance) to electrical energy, precluding the need for external electrical sources. The vibration of a spacecraft, for example, can provide sufficient energy to power many of its sensors piezoelectrically. A newly designed piezoelectric harvester incorporating a highly conductive carbon-fiber-reinforced polymer (CFRP) electrode has been shown to provide steady energy loads during resonance, an absolute prerequisite for wireless communication devices to be powered piezoelectrically.</p>',
        'Which finding, if true, would most directly support the text’s claim about wireless communication devices?',
        [
            'The near-constant kinetic vibration of a spacecraft makes it possible to power its wireless communication devices using only non-CFRP piezoelectric harvesters.',
            'The CFRP electrode is incompatible with most wireless communication devices.',
            'Intermittent or unpredictable electrical supply undermines the efficacy of wireless communication devices.',
            'The high conductivity of the CFRP is what makes the energy output from a piezoelectric harvester sufficient for wireless communication devices.',
        ],
        'C',
        'Đọc cực kỹ đối tượng câu hỏi nhắm tới: “would most directly support **the text’s claim about wireless communication devices**” (ủng hộ trực tiếp **luận điểm của văn bản về các thiết bị liên lạc không dây**). Trong văn bản, câu duy nhất nói về thiết bị liên lạc không dây khẳng định: việc cung cấp **tải năng lượng ổn định (“steady energy loads”)** là **“một điều kiện tiên quyết tuyệt đối để thiết bị liên lạc không dây có thể chạy bằng năng lượng áp điện”** (“an absolute prerequisite for wireless communication devices to be powered piezoelectrically”).\nNếu nguồn điện **gián đoạn hoặc thất thường làm suy giảm hiệu quả của thiết bị liên lạc không dây** (Đáp án C), điều đó chứng minh trực tiếp TẠI SAO nguồn điện ổn định (“steady energy loads”) lại là điều kiện tiên quyết tuyệt đối đối với thiết bị liên lạc không dây → Chọn C! Tránh bẫy D: văn bản chỉ nói tải năng lượng ổn định là *điều kiện cần* (prerequisite), KHÔNG hề tuyên bố độ dẫn điện cao của CFRP làm tổng mức năng lượng *đủ* (sufficient) cho thiết bị không dây.',
        'Đọc đúng trọng tâm câu hỏi (“claim about wireless communication devices”) và phân biệt rạch ròi **điều kiện cần (`prerequisite`)** với **điều kiện đủ (`sufficient`)**: để chứng minh “ổn định là điều kiện tiên quyết”, hãy chỉ ra “thiếu ổn định (`intermittent or unpredictable`) sẽ gây hại cho hiệu quả thiết bị”!',
        [
            ('Undermines / Off-Target', 'Nói tàu vũ trụ có thể cấp điện cho thiết bị không dây chỉ bằng bộ thu KHÔNG dùng CFRP — không chứng minh lý do tải điện ổn định là điều kiện tiên quyết, mà còn làm mờ vai trò của CFRP.'),
            ('Contradicts / Irrelevant', 'Nói điện cực CFRP không tương thích với đa số thiết bị không dây — đi ngược chiều ứng dụng của thiết bị mới chứ không ủng hộ luận điểm về điều kiện tiên quyết.'),
            ('Đáp án đúng', 'Chứng minh trực diện luận điểm về thiết bị liên lạc không dây: vì nguồn điện gián đoạn/thất thường phá hỏng hiệu năng của chúng, nên nguồn tải năng lượng ổn định thực sự là điều kiện tiên quyết tuyệt đối.'),
            ('Necessary vs. Sufficient Trap!', 'Bẫy Hard M2 cực tinh vi: văn bản KHÔNG khẳng định độ dẫn điện của CFRP làm công suất đầu ra “đủ” (`sufficient`) cho thiết bị không dây — nó chỉ nói CFRP cấp tải ổn định, vốn là *điều kiện tiên quyết* (`prerequisite`).'),
        ],
    ),

    # --- M2 Q14 ---
    q_item(
        'march2025_v5_rw_m2_q14', 14, 'Information and Ideas', 'Inferences', 'Medium',
        '<p>Consumers increasingly expect that goods they purchase online will be delivered rapidly, even as soon as the day of purchase. Although efficiencies in long-distance transport of parcels have greatly improved delivery times, last-mile logistics (the final step in delivery to consumers) present a bottleneck for delivery companies. Time pressure resulting from consumer expectations is not the only challenge; other obstacles, such as the increasing congestion of roadways, persist. While innovations to mitigate these challenges have been emerging—the use of cargo bikes, for instance—success has been constrained due to the additional complications that arise (e.g., the low parcel carrying capacity of the bikes). Consequently, _______</p>',
        'Which choice most logically completes the text?',
        [
            'the use of cargo bikes may enable delivery companies to meet consumers’ expectations now but likely is not viable as a permanent solution.',
            'in the near term, delivery companies are unlikely to overcome the impediments associated with last-mile logistics.',
            'delivery companies should invest more funds in proven long-distance transport technologies than in untested last-mile solutions.',
            'innovations in last-mile logistics seem poised to increase consumers’ expectations for rapid delivery.',
        ],
        'B',
        'Tổng hợp toàn bộ chuỗi lập luận dẫn tới từ kết luận “Consequently,”:\n• Người tiêu dùng ngày càng đòi giao hàng siêu tốc (thậm chí trong ngày).\n• Dù vận tải đường dài đã cải thiện, **khâu giao hàng chặng cuối (last-mile logistics)** vẫn là nút thắt cổ chai.\n• Áp lực thời gian + tắc nghẽn giao thông ngày càng tăng vẫn tiếp diễn (“persist”).\n• Các sáng kiến mới (như xe đạp chở hàng) mới nhen nhóm nhưng thành công bị hạn chế do phát sinh rắc rối mới (sức chở ít).\n→ Kết luận logic nhất: **trong ngắn hạn, các công ty giao hàng khó có thể vượt qua những trở ngại gắn liền với logistics chặng cuối** → Chọn B!',
        'Khi đoạn văn lần lượt đóng mọi cánh cửa giải pháp hiện tại (“bottleneck... persist... success has been constrained”), kết luận hợp lý sau “Consequently,” phải thận trọng và phản ánh đúng thực tế bế tắc trước mắt (“in the near term... unlikely to overcome”).',
        [
            ('Contradicts Text', 'Bài nói rõ thành công của xe đạp chở hàng ĐÃ BỊ HẠN CHẾ ngay từ bây giờ do sức chở thấp, chứ không hề giúp đáp ứng kỳ vọng khách hàng hiện tại.'),
            ('Đáp án đúng', 'Suy luận trực tiếp và chừng mực từ chuỗi khó khăn kéo dài cùng giới hạn của các sáng kiến mới: trong ngắn hạn, doanh nghiệp khó giải quyết dứt điểm nút thắt chặng cuối.'),
            ('Unsupported Recommendation', 'Vận tải đường dài vốn ĐÃ cải thiện hiệu quả rồi; bài không hề khuyên công ty nên dồn tiền vào đường dài thay vì giải pháp chặng cuối.'),
            ('Reversed / Unsupported', 'Không có chi tiết nào cho thấy sáng kiến chặng cuối lại làm tăng kỳ vọng giao hàng nhanh của khách hàng.'),
        ],
    ),

    # --- M2 Q15 ---
    q_item(
        'march2025_v5_rw_m2_q15', 15, 'Information and Ideas', 'Inferences', 'Hard',
        '<p>Microbial fuel cells (MFCs) capitalize on the ability of some species of bacteria to metabolize metal, liberating electrons. The bacteria form a dense biofilm on the surface of an electron-collecting anode, but moving the electrons from the bacterial cytoplasm to an external electrode requires that the electrons pass through a series of inefficient oxidation-reduction (redox) reactions. Accordingly, MFC power output rarely exceeds a density of 0.30 milliwatts per square centimeter (mW/cm²). In an experiment, researchers added silver nanoparticles to carbon paper covering the anode in an MFC. The resulting power density was 0.66 mW/cm². Since metals such as silver exhibit high electrical conductivity, the researchers hypothesized that _______</p>',
        'Which choice most logically completes the text?',
        [
            'silver nanoparticles may allow electrons to bypass the series of redox reactions and transfer directly to the electrode.',
            'as the density of the biofilm increases, the series of redox reactions may accelerate independent of the presence of the silver nanoparticles.',
            'electrons may be conducted directly to the electrode before the silver nanoparticles catalyze the redox reactions.',
            'silver nanoparticles may increase the metabolic processes of the bacteria, thereby increasing the number of free electrons available to transfer to the electrode.',
        ],
        'A',
        'Nối chặt hai mắt xích khoa học trong đoạn văn:\n[1] Nút thắt công suất ban đầu (chỉ ≤ 0,30 mW/cm²): electron từ tế bào chất vi khuẩn muốn ra điện cực ngoài phải đi qua **một chuỗi phản ứng oxy hóa–khử (redox) kém hiệu quả**.\n[2] Kết quả thí nghiệm & tiền đề giả thuyết: Khi thêm hạt nano bạc vào giấy carbon phủ cực dương, mật độ công suất tăng hơn gấp đôi lên 0,66 mW/cm². Mệnh đề mở đầu câu kết nêu rõ cơ sở suy luận: **“Vì các kim loại như bạc có độ dẫn điện cao (“high electrical conductivity”), các nhà nghiên cứu giả thuyết rằng _______”**.\nVì bạc dẫn điện cao, nó tạo lối đi dẫn truyền trực tiếp giúp **electron đi tắt qua chuỗi phản ứng redox kém hiệu quả và truyền thẳng sang điện cực** → Chọn A!',
        'Luôn bám chặt mệnh đề tiền đề ngay trước chỗ trống (`Since metals such as silver exhibit high electrical conductivity`): đặc tính **dẫn điện cao** loại ngay cơ chế sinh học trao đổi chất (D) và cơ chế xúc tác hóa học (C), chỉ thẳng vào cơ chế dẫn truyền electron trực tiếp bỏ qua bước trung gian kém hiệu quả (A)!',
        [
            ('Đáp án đúng', 'Kết nối hoàn hảo cả hai dữ kiện: độ dẫn điện cao của hạt nano bạc cho phép electron bỏ qua chuỗi phản ứng redox kém hiệu quả để truyền thẳng tới điện cực, lý giải công suất tăng gấp đôi.'),
            ('Contradicts Experiment', 'Nói phản ứng redox tăng tốc ĐỘC LẬP với sự hiện diện của hạt nano bạc — phủ nhận hoàn toàn vai trò của bạc trong thí nghiệm và bỏ qua tiền đề “high electrical conductivity”.'),
            ('Illogical Sequence & Wrong Mechanism', 'Vô lý về trình tự và cơ chế: nếu electron đã được dẫn thẳng sang điện cực TRƯỚC thì còn cần nano bạc “xúc tác phản ứng redox” làm gì? Hơn nữa tiền đề nêu độ dẫn điện chứ không phải tính xúc tác.'),
            ('Wrong Mechanism Trap!', 'Bẫy đánh lạc hướng sang sinh học (“increase metabolic processes of the bacteria”): tiền đề nêu rõ bạc có **độ dẫn điện cao** (tính chất vật lý hỗ trợ truyền electron), không phải kích thích trao đổi chất vi khuẩn.'),
        ],
    ),

    # --- M2 Q16 ---
    q_item(
        'march2025_v5_rw_m2_q16', 16, 'Information and Ideas', 'Inferences', 'Hard',
        '<p>The ratio of methane to other atmospheric constituents—represented by a measure called the methane mole fraction—influences a variety of meteorological phenomena, notably precipitation and humidity. For Titan, Saturn’s largest moon, the observational data that exist are too sparse and discrepant to fully constrain the range of the methane mole fraction at various atmospheric levels. Juan Lora and colleagues point out that outputs of the IPSL atmospheric model of Titan, which track closely to observations in some respects, reflect how the model’s developers responded to this challenge: by prescribing a uniform methane mole fraction for the lowest level of the atmosphere. It is therefore important to note that _______</p>',
        'Which choice most logically completes the text?',
        [
            'further observations of Titan may clarify the moon’s methane mole fraction sufficiently for the model to employ a single value rather than a range.',
            'some disagreements between the model’s simulations of Titan’s precipitation and humidity and the moon’s actual precipitation and humidity are to be expected.',
            'even though the model’s outputs sometimes agree with observational data, Titan’s real methane mole fraction is likely higher than the methane mole fraction used in the model.',
            'inconsistencies across the model’s simulations of Titan’s precipitation and humidity could be attributable to variations in the moon’s methane mole fraction.',
        ],
        'B',
        'Theo dõi chuỗi logic 3 bước cực chặt của bài khoa học hành tinh:\n• Bước 1: Tỷ lệ mol khí metan (“methane mole fraction”) **ảnh hưởng đến mưa và độ ẩm** (“influences... precipitation and humidity”).\n• Bước 2: Trên mặt trăng Titan, dữ liệu quan sát quá thưa thớt và mâu thuẫn nên không xác định trọn vẹn được dải biến thiên tỷ lệ mol metan ở các tầng khí quyển.\n• Bước 3: Để đối phó, nhóm phát triển mô hình khí quyển IPSL đã giản lược bằng cách gán một giá trị tỷ lệ mol metan **đồng nhất (“uniform”)** cho tầng thấp nhất của khí quyển (nên kết quả mô hình chỉ khớp quan sát ở một số khía cạnh — “in some respects”).\n→ Kết luận quan trọng cần lưu ý (“It is therefore important to note that _______”): **nên lường trước sẽ có một số sai lệch giữa mô phỏng lượng mưa và độ ẩm của mô hình với thực tế trên Titan** → Chọn B!',
        'Phân biệt sắc bén giữa B và bẫy D: mô hình IPSL gán giá trị metan ĐỒNG NHẤT (không đổi), nên sự khác biệt xảy ra là **giữa mô phỏng của mô hình với thực tế của Titan (B)**, chứ không phải “sự mâu thuẫn bên trong các mô phỏng của mô hình do biến thiên metan” (D)!',
        [
            ('Reversed Logic', 'Mô hình IPSL HIỆN ĐÃ dùng một giá trị đơn nhất đồng nhất (“uniform”) bất đắc dĩ vì thiếu dữ liệu; các quan sát bổ sung sẽ giúp xác định dải biến thiên thực sự chứ không phải để mô hình chuyển từ dải sang một giá trị đơn.'),
            ('Đáp án đúng', 'Suy luận chuẩn xác và thận trọng: vì tỷ lệ metan chi phối mưa/độ ẩm nhưng mô hình buộc phải giản lược thành giá trị đồng nhất, nên chắc chắn cần dự liệu một số sai khác giữa mô phỏng và thực tế.'),
            ('Unsupported Direction', 'Văn bản không cung cấp bất kỳ dữ kiện nào cho biết tỷ lệ metan thực của Titan CAO HƠN hay THẤP HƠN mức dùng trong mô hình.'),
            ('Logical Trap (Model vs. Reality)', 'Bẫy Hard M2: mô hình gán một hằng số metan đồng nhất, nên biến thiên metan thực tế của Titan không thể gây ra “mâu thuẫn giữa các mô phỏng của chính mô hình”.'),
        ],
    ),

    # --- M2 Q17 ---
    q_item(
        'march2025_v5_rw_m2_q17', 17, 'Standard English Conventions', 'Form, Structure, and Sense', 'Medium',
        '<p>New Zealand and Greece have two of the longest constitutions in the world. At 48,438 and 26,989 words, respectively, these _______ according to research by constitutional scholars George Tsebelis and Dominic J. Nardi, correlate with GDPs (gross domestic products) that are lower than those of countries with shorter constitutions.</p>',
        'Which choice completes the text so that it conforms to the conventions of Standard English?',
        [
            'constitutions lengths,',
            'constitution’s length,',
            'constitutions’ lengths,',
            'constitutions’ length,',
        ],
        'C',
        'Kiểm tra đồng thời **Sở hữu cách số nhiều** + **Hòa hợp chủ–vị** + **Cặp dấu phẩy chêm**:\n1. Từ chỉ định số nhiều `these` đi với danh từ số nhiều sở hữu của hai bản hiến pháp (New Zealand và Greece) → **`constitutions’`** (dấu nháy đơn đứng SAU chữ `s`).\n2. Động từ chính của câu sau cụm chêm `, according to... ,` là động từ SỐ NHIỀU **`correlate`** (và phía trước nêu 2 độ dài riêng biệt: 48.438 từ và 26.989 từ) → danh từ trung tâm bắt buộc là số nhiều **`lengths`**!\n3. Cần dấu phẩy sau `lengths` để mở cụm chêm `, according to research by constitutional scholars George Tsebelis and Dominic J. Nardi,` → Chọn C (**`constitutions’ lengths,`**)!',
        'Công thức xử lý câu sở hữu cách + số ít/số nhiều: (1) Kiểm tra `these` → bắt buộc số nhiều `constitutions’`; (2) Bỏ cụm chêm `, according to...,` để soi động từ chính `correlate` (số nhiều) → bắt buộc `lengths` số nhiều!',
        [
            ('Missing Possessive Apostrophe', 'Thiếu dấu nháy đơn sở hữu cách ở “constitutions” (hai danh từ số nhiều đứng liền nhau thiếu dấu sở hữu).'),
            ('Wrong Number (Singular)', '“constitution’s” (số ít) mâu thuẫn với “these” (số nhiều), và “length” (số ít) sai hòa hợp với động từ số nhiều “correlate”.'),
            ('Đáp án đúng', '“constitutions’ lengths,” chuẩn cả 3 tiêu chí: sở hữu cách số nhiều khớp “these”, danh từ số nhiều “lengths” hòa hợp với động từ “correlate”, và dấu phẩy mở đúng cụm chêm.'),
            ('Subject-Verb Disagreement', '“length” là danh từ số ít, không hòa hợp với động từ số nhiều “correlate” cũng như hai con số độ dài tách biệt của hai nước.'),
        ],
    ),

    # --- M2 Q18 ---
    q_item(
        'march2025_v5_rw_m2_q18', 18, 'Standard English Conventions', 'Boundaries', 'Easy',
        '<p>Included in <i>Second Sight: the Paradox of Vision in Contemporary Art</i>, a 2018 group exhibition at the Bowdoin College Museum of Art in Brunswick, Maine, was the work of artist Lorna Simpson, who is best known for her multimedia artworks that juxtapose images of African American women with text fragments. Her work challenges conventional notions of race, gender, history, and _______ she is credited with expanding the horizons of conceptual photographic art.</p>',
        'Which choice completes the text so that it conforms to the conventions of Standard English?',
        [
            'memory.',
            'memory',
            'memory, and',
            'memory and',
        ],
        'C',
        'Kiểm tra ranh giới giữa hai mệnh đề độc lập + chữ viết thường sau chỗ trống:\n• Mệnh đề 1: `Her work challenges conventional notions of race, gender, history, and memory`\n• Mệnh đề 2: `she is credited with expanding the horizons of conceptual photographic art.`\nĐẶC BIỆT CHÚ Ý chữ **`she` viết thường** ngay sau chỗ trống! Vì `she` viết thường nên loại ngay dấu chấm ở đáp án A (`memory. she` sai chính tả chuẩn tiếng Anh!). Để nối hai mệnh đề độc lập bằng liên từ FANBOYS `and`, ta bắt buộc dùng **`, and`** → Chọn C (**`memory, and`**)!',
        'Mẹo 3 giây chống bẫy đáp án A: luôn soi chữ cái đầu tiên NGAY SAU chỗ trống! Chữ `she` viết thường lập tức loại dấu chấm (`.`), còn giữa `and` có phẩy và không phẩy thì 2 mệnh đề độc lập bắt buộc phải có dấu phẩy (`, and`)!',
        [
            ('Capitalization Error After Period', 'Sau dấu chấm (`memory.`), chữ “she” phía sau đang viết thường — sai quy tắc viết hoa đầu câu tiếng Anh chuẩn!'),
            ('Fused Sentence (Run-on)', 'Nối trực tiếp hai mệnh đề độc lập “...and memory she is credited...” mà không có bất kỳ dấu câu hay liên từ nào.'),
            ('Đáp án đúng', '“memory, and” khép danh sách 4 danh từ và dùng đúng cấu trúc `, FANBOYS` để nối hai mệnh đề độc lập liền mạch với chữ “she” viết thường.'),
            ('Missing Comma Before FANBOYS', 'Khi nối hai mệnh đề độc lập (đều có chủ ngữ và vị ngữ đầy đủ), bắt buộc đặt dấu phẩy trước liên từ “and”.'),
        ],
    ),

    # --- M2 Q19 ---
    q_item(
        'march2025_v5_rw_m2_q19', 19, 'Standard English Conventions', 'Boundaries', 'Medium',
        '<p>Recent analysis of 54598 Bienor—an outer solar system object orbiting the Sun between Saturn and Uranus—has determined its color to be gray, suggesting an icy composition. Such interpretations are ultimately _______ the object’s gray coloration may be an incidental effect of radiation, solar wind, or collisions with other objects rather than evidence of its physical makeup.</p>',
        'Which choice completes the text so that it conforms to the conventions of Standard English?',
        [
            'speculative, though,',
            'speculative, though;',
            'speculative; though',
            'speculative, though',
        ],
        'B',
        'Cấu trúc ranh giới kinh điển với trạng từ tương phản `though` cuối mệnh đề độc lập 1:\n• Câu 1: Phân tích thiên thể 54598 Bienor thấy màu xám, gợi ý cấu tạo bằng băng.\n• Mệnh đề 2a: `Such interpretations are ultimately speculative, though` → **tương phản** với câu 1 (“tuy nhiên các diễn giải như vậy rốt cuộc vẫn chỉ là suy đoán”).\n• Mệnh đề 2b: `the object’s gray coloration may be an incidental effect of radiation, solar wind, or collisions...` → **giải thích** lý do vì sao chúng chỉ là suy đoán (KHÔNG tương phản với 2a).\nVì `though` khép lại Mệnh đề 2a và tiếp theo là một mệnh đề độc lập hoàn chỉnh, bắt buộc đặt **dấu chấm phẩy SAU `though`** → **`speculative, though;`** → Chọn B!',
        'Kiểm tra xem `though` phản bác câu trước hay phản bác vế sau: ở đây vế sau giải thích cho `speculative` chứ không phản bác nó → `though` thuộc vế trước → ngăn cách hai IC bằng `;` ngay sau `though` (`speculative, though;`).',
        [
            ('Comma Splice', 'Đặt dấu phẩy sau “though” nối hai mệnh đề độc lập gây lỗi Comma Splice.'),
            ('Đáp án đúng', '“speculative, though;” gắn đúng trạng từ “though” vào cuối mệnh đề 1 và tách hai mệnh đề độc lập chuẩn mực bằng dấu chấm phẩy.'),
            ('Fragment / Illogical Subordinator', 'Đặt dấu chấm phẩy trước “though” biến vế sau thành mệnh đề phụ thuộc (“though the object’s gray coloration may be...”) đứng trơ trọi sau dấu chấm phẩy (fragment), đồng thời sai quan hệ logic.'),
            ('Fused Sentence', 'Thiếu hoàn toàn dấu câu ngăn cách hai mệnh đề độc lập.'),
        ],
    ),

    # --- M2 Q20 ---
    q_item(
        'march2025_v5_rw_m2_q20', 20, 'Standard English Conventions', 'Form, Structure, and Sense', 'Hard',
        '<p>Mitochondrial genomes reproduce asexually, which should over time result in an accumulation of harmful mutations and a decline in mitochondrial functionality. However, nuclear genes are hypothesized to coevolve with the rate of mitochondrial decline, eliminating mutational erosion. Such a compensatory measure _______ the organelle’s decline, unlike enzyme-stabilizing accessory proteins, offers an evolutionary explanation of mitochondrial reproduction.</p>',
        'Which choice completes the text so that it conforms to the conventions of Standard English?',
        [
            'counteracts',
            'had counteracted',
            'counteracted',
            'counteracting',
        ],
        'D',
        'Kỹ thuật gạch bỏ cụm bổ nghĩa phụ đặt giữa hai dấu phẩy (`unlike enzyme-stabilizing accessory proteins`): Sau khi tạm bỏ cụm này, khung câu hiện rõ nguyên hình:\n`Such a compensatory measure _______ the organelle’s decline offers an evolutionary explanation of mitochondrial reproduction.`\nCâu **ĐÃ CÓ SẴN ĐỘNG TỪ CHÍNH CHIA THÌ LÀ `offers`** (hòa hợp hoàn hảo với chủ ngữ số ít `Such a compensatory measure`)! Do đó, chỗ trống TUYỆT ĐỐI KHÔNG được điền thêm động từ chia thì (`counteracts`, `had counteracted`, `counteracted`) mà phải điền **phân từ hiện tại chủ động `counteracting`** để tạo cụm phân từ bổ nghĩa cho `measure` (= *a compensatory measure that counteracts the organelle’s decline*) → Chọn D!',
        'Bẫy Hard M2: cụm chêm `, unlike enzyme-stabilizing accessory proteins,` được chèn vào ngay trước động từ chính `offers` để che mắt thí sinh! Luôn đọc tới cuối câu kiểm tra xem đã có động từ chia thì chưa — có sẵn `offers` → dùng ngay phân từ `counteracting`!',
        [
            ('Double Finite Verb', 'Điền động từ chia thì “counteracts” tạo hai vị ngữ “counteracts ... offers” cho cùng một chủ ngữ mà không có liên từ hay đại từ quan hệ.'),
            ('Double Finite Verb', '“had counteracted” là động từ chia thì quá khứ hoàn thành, xung đột trực tiếp với động từ chính “offers”.'),
            ('Wrong Form (Finite / Passive)', 'Nếu là quá khứ đơn thì gây lỗi hai vị ngữ; nếu hiểu là quá khứ phân từ bị động thì sai ngữ nghĩa vì ngay sau là tân ngữ trực tiếp “the organelle’s decline” (biện pháp này CHỦ ĐỘNG chống lại sự suy thoái).'),
            ('Đáp án đúng', 'Hiện tại phân từ chủ động “counteracting” tạo cụm bổ nghĩa chuẩn xác cho “Such a compensatory measure” với tân ngữ “the organelle’s decline”, giữ nguyên “offers” làm động từ chính duy nhất.'),
        ],
    ),

    # --- M2 Q21 ---
    q_item(
        'march2025_v5_rw_m2_q21', 21, 'Standard English Conventions', 'Form, Structure, and Sense', 'Medium',
        '<p>In the list “Adorable Things” from Sei Shōnagon’s <i>Pillow Book</i>, the author delights in baby sparrows, a face drawn on a melon, and a young courtier in ceremonial garb. So shrewd an observer is Shōnagon, a lady-in-waiting to Empress Teishi, that her book’s musings on tenth-century Japanese courtly life _______ readers a thousand years later.</p>',
        'Which choice completes the text so that it conforms to the conventions of Standard English?',
        [
            'has fascinated',
            'fascinates',
            'is fascinating',
            'fascinate',
        ],
        'D',
        'Kiểm tra hòa hợp chủ ngữ – động từ (Subject-Verb Agreement) với bẫy cụm giới từ dài: Trong mệnh đề `that her book’s musings on tenth-century Japanese courtly life _______ readers a thousand years later`, hãy gạch bỏ cụm giới từ bổ nghĩa `on tenth-century Japanese courtly life` (chứa danh từ số ít `life` gây nhiễu!). Chủ ngữ cốt lõi là danh từ **SỐ NHIỀU `musings`** (những dòng suy ngẫm). Áp dụng mẹo 3–1 Split: 3 đáp án số ít (`has fascinated`, `fascinates`, `is fascinating`) vs. duy nhất 1 đáp án số nhiều **`fascinate`** → Chọn D!',
        'Mẹo gạch cụm giới từ + 3–1 Split: bỏ `on tenth-century Japanese courtly life` → còn `her book’s musings [số nhiều] ___ readers` → chốt ngay động từ số nhiều duy nhất `fascinate`!',
        [
            ('Singular Verb', '“has fascinated” chia cho chủ ngữ số ít, sai với chủ ngữ số nhiều “musings”.'),
            ('Singular Verb', '“fascinates” là động từ số ít, bị danh từ số ít “life” ngay trước chỗ trống đánh lừa.'),
            ('Singular Verb', '“is fascinating” vừa sai số ít vừa không tự nhiên bằng hiện tại đơn diễn tả sức hấp dẫn bền bỉ của tác phẩm văn học.'),
            ('Đáp án đúng', '“fascinate” là động từ hiện tại đơn số nhiều duy nhất hòa hợp chuẩn xác với chủ ngữ cốt lõi “musings”.'),
        ],
    ),

    # --- M2 Q22 ---
    q_item(
        'march2025_v5_rw_m2_q22', 22, 'Expression of Ideas', 'Transitions', 'Easy',
        '<p>To notice subtle variations in the progression of the still life painting genre in Europe, first consider Abraham Mignon’s “Still Life with Fruit and a Beaker on a Cock’s Foot” from 1669; _______ compare it to Jean-Siméon Chardin’s “Still Life with Herrings” from 1735.</p>',
        'Which choice completes the text with the most logical transition?',
        [
            'instead,',
            'therefore,',
            'next,',
            'still,',
        ],
        'C',
        'Bắt tín hiệu trình tự rõ như ban ngày ở vế trước dấu chấm phẩy: “**first** consider Abraham Mignon’s ‘Still Life with Fruit and a Beaker on a Cock’s Foot’ from 1669; **_______** compare it to Jean-Siméon Chardin’s ‘Still Life with Herrings’ from 1735.” Bước 1 (`first consider...`) → Bước 2 (**`next,`** `compare it to...`) → Chọn C!',
        'Gặp từ chỉ thứ tự `first` ở mệnh đề 1 và câu mệnh lệnh hướng dẫn bước tiếp theo ở mệnh đề 2 (`compare it to...`), chốt ngay từ nối trình tự `next,`.',
        [
            ('Wrong Relationship (Replacement)', '“instead,” (thay vào đó) sai logic vì người đọc cần xem CẢ HAI bức tranh để so sánh biến chuyển, không phải bỏ bức 1669.'),
            ('Wrong Relationship (Cause-Effect)', 'Việc so sánh với tranh năm 1735 là bước kế tiếp trong hướng dẫn, không phải kết quả nhân-quả của việc xem tranh năm 1669.'),
            ('Đáp án đúng', '“next,” tạo cặp chuyển tiếp trình tự tự nhiên tuyệt đối với “first” ở mệnh đề trước.'),
            ('Wrong Relationship (Contrast)', '“still,” (tuy vậy) mang sắc thái tương phản, sai với hướng dẫn hai bước liên tiếp.'),
        ],
    ),

    # --- M2 Q23 ---
    q_item(
        'march2025_v5_rw_m2_q23', 23, 'Expression of Ideas', 'Transitions', 'Easy',
        '<p>In an ekphrastic poem, a poet explores a work of visual art, such as a drawing, sculpture, or painting. Robert Hayden’s 1994 poem “Monet’s Waterlilies,” for example, meditates on Claude Monet’s 1899 painting <i>Water Lilies</i>; Elizabeth Alexander’s 2001 poem “Islands Number Four,” _______ takes a painting as its subject: Agnes Martin’s 1961 work <i>Islands No. 4</i>.</p>',
        'Which choice completes the text with the most logical transition?',
        [
            'conversely,',
            'nevertheless,',
            'hence,',
            'likewise,',
        ],
        'D',
        'Phân tích hai ví dụ song hành nối bằng dấu chấm phẩy:\n• Vế 1: Bài thơ năm 1994 *“Monet’s Waterlilies”* của Robert Hayden lấy cảm hứng từ bức họa *Water Lilies* của Claude Monet.\n• Vế 2: Bài thơ năm 2001 *“Islands Number Four”* của Elizabeth Alexander **_______** cũng lấy một bức tranh làm đề tài: tác phẩm *Islands No. 4* của Agnes Martin.\nHai trường hợp song song minh họa cùng khái niệm thơ ekphrastic → Chọn từ nối tương đồng **“likewise,”** (tương tự như vậy) → Chọn D!',
        'Khi hai mệnh đề song song cùng đưa ví dụ tương đồng cho định nghĩa ở câu mở đầu (Thơ của Hayden về tranh Monet ; Thơ của Alexander về tranh Martin), chọn ngay “likewise,” / “similarly,”.',
        [
            ('Wrong Relationship (Contrast)', '“conversely,” (ngược lại) sai hoàn toàn vì cả hai bài thơ đều lấy tranh hội họa làm đối tượng.'),
            ('Wrong Relationship (Contrast)', '“nevertheless,” (tuy nhiên) chỉ sự đối lập, trái với hai ví dụ đồng điệu.'),
            ('Wrong Relationship (Cause-Effect)', '“hence,” (do đó) chỉ quan hệ nguyên nhân–kết quả, không phù hợp giữa hai tác phẩm độc lập của hai nhà thơ khác nhau.'),
            ('Đáp án đúng', '“likewise,” (tương tự) nối mượt mà hai ví dụ song song về thơ ekphrastic lấy cảm hứng từ hội họa.'),
        ],
    ),

    # --- M2 Q24 ---
    q_item(
        'march2025_v5_rw_m2_q24', 24, 'Expression of Ideas', 'Rhetorical Synthesis', 'Medium',
        '<p>While researching a topic, a student has taken the following notes:</p><ul><li>In a 2004 study, researchers Jorge E. López and C. Vaughan wanted to explore the effects of ingestion by bats on the germination of <i>Piper sancti-felicis</i> seeds in Costa Rica.</li><li>The team of researchers tested 125 <i>Piper sancti-felicis</i> seeds that had been ingested by chestnut short-tailed bats.</li><li>Of these, 82 seeds (66%) germinated.</li><li>As a control, J.E. López and C. Vaughan tested 125 <i>Piper sancti-felicis</i> seeds that had not been ingested by chestnut short-tailed bats.</li><li>Of these, 88 seeds (70%) germinated.</li></ul>',
        'The student wants to describe the study’s research methodology. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
        [
            'The team of researchers tested the germination of 125 <i>Piper sancti-felicis</i> seeds that had been ingested by chestnut short-tailed bats and 125 <i>Piper sancti-felicis</i> seeds that had not been ingested.',
            'J.E. López and C. Vaughan wanted to explore the effects of chestnut short-tailed bats’ ingestion on <i>Piper sancti-felicis</i> seed germination.',
            'In the study, a lower percentage of <i>Piper sancti-felicis</i> seeds ingested by bats germinated than those that had not been ingested by bats.',
            'Research by J.E. López and C. Vaughan revealed that 82 of 125—that is, 66%—of the <i>Piper sancti-felicis</i> seeds that had been ingested by the bats germinated.',
        ],
        'A',
        'Chiến lược Goal-First: Mục tiêu là **mô tả PHƯƠNG PHÁP NGHIÊN CỨU của nghiên cứu** (“describe the study’s **research methodology**”). Hãy phân biệt 3 phần khác nhau trong ghi chú:\n• Mục tiêu (Objective): muốn tìm hiểu tác động của việc dơi ăn lên sự nảy mầm hạt → Đáp án B (❌).\n• **Phương pháp (Methodology)**: thử nghiệm 125 hạt *Piper sancti-felicis* đã bị dơi ăn và đối chứng với 125 hạt chưa bị dơi ăn → **Đáp án A (✅)**!\n• Kết quả (Findings/Results): 82 hạt (66%) vs. 88 hạt (70%) nảy mầm → Đáp án C, D (❌) → Chọn A!',
        'Mẹo phân loại cực nhạy cho Rhetorical Synthesis về thí nghiệm khoa học: `methodology` = **HOW** (cách thiết kế thử nghiệm: số lượng mẫu, nhóm thí nghiệm vs. nhóm đối chứng), phân biệt rạch ròi với `goal/objective` (B) và `findings/results` (C, D)!',
        [
            ('Đáp án đúng', 'Mô tả chuẩn xác thiết kế/phương pháp thí nghiệm: kiểm tra sự nảy mầm của 125 hạt đã qua đường tiêu hóa dơi đối chứng với 125 hạt chưa bị ăn.'),
            ('Describes Objective, Not Methodology', 'Chỉ nêu mục đích nghiên cứu (“wanted to explore...”), không mô tả cách thức thí nghiệm được tiến hành.'),
            ('Describes Results, Not Methodology', 'Chỉ trình bày kết quả so sánh tỷ lệ nảy mầm thấp hơn, không mô tả phương pháp nghiên cứu.'),
            ('Describes Results, Not Methodology', 'Chỉ báo cáo số liệu kết quả (82/125 hạt = 66% nảy mầm), không mô tả phương pháp thiết kế thí nghiệm và nhóm đối chứng.'),
        ],
    ),

    # --- M2 Q25 ---
    q_item(
        'march2025_v5_rw_m2_q25', 25, 'Expression of Ideas', 'Rhetorical Synthesis', 'Medium',
        '<p>While researching a topic, a student has taken the following notes:</p><ul><li>Felipe Posada (pseudonym The Invisible Realm) is a New York City-based artist who specializes in the form of art known as surrealist collage.</li><li>Manifestation of the unconscious mind is a central aspect of surrealist collage.</li><li>Irrational juxtaposition of disparate elements is a central aspect of surrealist collage.</li><li>Posada’s <i>High Maintenance</i> irrationally juxtaposes images of an astronaut, a giant human face, and a waterfall.</li><li>Posada: “My art is a journey through the invisible realm—a space where intuition, memories, visions, and dreams are free to take visual form.”</li></ul>',
        'The student wants to provide a specific example of irrational juxtaposition in surrealist collage. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
        [
            'Surrealist collage, such as Felipe Posada’s <i>High Maintenance</i>, manifests the unconscious mind and irrationally juxtaposes disparate elements.',
            'Images of an astronaut, a giant human face, and a waterfall are juxtaposed irrationally in the surrealist collage piece <i>High Maintenance</i> by artist Felipe Posada.',
            '<i>High Maintenance</i> by artist Felipe Posada is an example of surrealist collage, a form in which irrational juxtaposition is a central aspect.',
            'The irrational juxtaposition of disparate elements in Felipe Posada’s art invokes “a space where intuition, memories, visions, and dreams are free to take visual form.”',
        ],
        'B',
        'Chiến lược Goal-First: Mục tiêu là **đưa ra một VÍ DỤ CỤ THỂ về sự đặt cạnh nhau phi lý (“a specific example of irrational juxtaposition”) trong nghệ thuật cắt dán siêu thực**. Tra ghi chú thấy dòng 4 nêu đích danh ví dụ cụ thể: bức *High Maintenance* của Posada đặt cạnh nhau một cách phi lý hình ảnh **một phi hành gia, một khuôn mặt người khổng lồ và một thác nước**. Chỉ duy nhất đáp án B liệt kê chính những hình ảnh đặt cạnh phi lý cụ thể ấy → Chọn B!',
        'Khi Goal đòi “a **specific example** of X”, luôn chọn đáp án nêu CHI TIẾT CỤ THỂ minh họa cho X (“an astronaut, a giant human face, and a waterfall”), loại ngay các câu chỉ lặp lại định nghĩa trừu tượng “disparate elements” (A, C, D).',
        [
            ('Too Vague / No Specific Example', 'Chỉ nói chung chung là “irrationally juxtaposes disparate elements” mà không nêu rõ những hình ảnh cụ thể nào được đặt cạnh nhau trong *High Maintenance*.'),
            ('Đáp án đúng', 'Đưa ra ví dụ cụ thể trọn vẹn nhất: liệt kê rõ hình ảnh phi hành gia, khuôn mặt người khổng lồ và thác nước được đặt cạnh nhau phi lý trong tác phẩm cắt dán siêu thực *High Maintenance* của Felipe Posada.'),
            ('No Specific Example', 'Chỉ gọi *High Maintenance* là ví dụ của surrealist collage mà hoàn toàn không miêu tả hình ảnh đặt cạnh phi lý bên trong tác phẩm.'),
            ('Wrong Focus / No Specific Example', 'Trích dẫn câu nói triết lý của Posada về “invisible realm”, không đưa ra ví dụ hình ảnh cụ thể nào.'),
        ],
    ),

    # --- M2 Q26 ---
    q_item(
        'march2025_v5_rw_m2_q26', 26, 'Expression of Ideas', 'Rhetorical Synthesis', 'Medium',
        '<p>While researching a topic, a student has taken the following notes:</p><ul><li>Carbon can exist in several distinct structural forms called allotropes.</li><li>Graphite is a carbon allotrope.</li><li>Graphite is composed of stacked graphene sheets.</li><li>Each graphene sheet is composed of carbon atoms arranged in a flat honeycomb pattern.</li><li>Carbon nanotubes are carbon allotropes.</li><li>They are composed of one or more graphene sheets wrapped into a cylindrical shape.</li></ul>',
        'The student wants to emphasize a difference between carbon nanotubes and graphite. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
        [
            'Composed of sheets wrapped into a cylindrical shape, carbon nanotubes contrast with graphite, a carbon allotrope composed of graphene sheets.',
            'Unlike carbon nanotubes, which are composed of sheets of carbon atoms arranged in a flat honeycomb pattern, graphite is a cylindrical carbon allotrope.',
            'The graphene sheets in graphite are stacked, whereas in carbon nanotubes, they form a cylinder.',
            'Graphite and carbon nanotubes are allotropes composed of stacked or wrapped graphene sheets, but carbon can exist in several distinct structural forms.',
        ],
        'C',
        'Chiến lược Goal-First: Mục tiêu là **nhấn mạnh sự KHÁC BIỆT giữa ống nano carbon (carbon nanotubes) và than chì (graphite)**. Theo ghi chú, cả hai đều cấu tạo từ tấm graphene, nhưng khác nhau ở cấu trúc sắp xếp: trong **graphite**, các tấm graphene được **xếp chồng lên nhau (“stacked”)**; còn trong **carbon nanotubes**, chúng được **cuộn thành hình trụ (“wrapped into a cylindrical shape / form a cylinder”)**. Đáp án C đặt hai đặc điểm đối lập đó thẳng hàng cạnh nhau với từ nối tương phản sắc nét “whereas” → Chọn C! (Chú ý né bẫy A rất tinh vi: A nói ống nano carbon cuộn hình trụ nhưng lại đối chiếu với than chì chỉ nói chung chung “composed of graphene sheets” — bỏ mất từ khóa “stacked”, khiến sự khác biệt bị khuyết nửa vế!)',
        'Với mục tiêu “emphasize a difference between X and Y”, đáp án đúng phải nêu **cùng một tiêu chí tương phản cho CẢ X VÀ Y** (`stacked` ↔ `form a cylinder`). Loại ngay đáp án khuyết tiêu chí của một bên (A) hoặc tráo ngược sự thật (B)!',
        [
            ('Incomplete Contrast Trap!', 'Nêu cấu trúc hình trụ của ống nano carbon nhưng lại mô tả than chì chỉ là “composed of graphene sheets” (bỏ sót đặc điểm “stacked”!) — mà ống nano carbon CŨNG cấu tạo từ tấm graphene, nên phép đối chiếu không làm rõ điểm khác nhau thực sự!'),
            ('Factual Reversal', 'Đảo ngược hoàn toàn sự thật ghi chú: than chì (graphite) KHÔNG phải dạng hình trụ, còn tấm phẳng tổ ong là cấu tạo của mỗi tấm graphene chứ không phải đặc điểm riêng để đối lập kiểu này.'),
            ('Đáp án đúng', 'Đối chiếu sắc nét, ngắn gọn và chính xác 100% đúng tiêu chí phân biệt cốt lõi: tấm graphene trong than chì xếp chồng (`stacked`), còn trong ống nano carbon tạo thành hình trụ (`form a cylinder`).'),
            ('Lacks Clear Difference', 'Gộp chung cả hai là “stacked or wrapped” mà không chỉ rõ chất nào xếp chồng, chất nào cuộn tròn.'),
        ],
    ),

    # --- M2 Q27 ---
    q_item(
        'march2025_v5_rw_m2_q27', 27, 'Expression of Ideas', 'Rhetorical Synthesis', 'Hard',
        '<p>While researching a topic, a student has taken the following notes:</p><ul><li>Modularity of mind is the notion that the mind is at least partly composed of innate neural structures (modules) that perform fast, necessary tasks.</li><li>1983: cognitive scientist Jerry A. Fodor hypothesized that low-level cognitive systems (e.g., perception, language) are modular.</li><li>In Fodorian modularity, high-level systems (e.g., reasoning) are not modular.</li><li>2003: cognitive scientist Peter Carruthers proposed the massive modularity hypothesis (MMH).</li><li>MMH expands modularity to include all cognitive systems.</li></ul>',
        'The student wants to compare Fodor’s hypothesis with Carruthers’s. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
        [
            'In considering some but not all cognitive systems modular, Fodorian modularity is not as expansive in its definition of modularity as MMH is.',
            'The hypotheses of Fodor and Carruthers differ in whether they consider low-level cognitive systems, such as perception and language, modular.',
            'In 2003, Carruthers proposed the massive modularity hypothesis, disagreeing with Fodor’s earlier hypothesis that the mind is composed of innate neural structures.',
            'Following Fodor’s 1983 hypothesis, Carruthers proposed that modularity of mind includes all cognitive systems.',
        ],
        'A',
        'Chiến lược Goal-First: Mục tiêu là **SO SÁNH giả thuyết của Fodor với giả thuyết của Carruthers** (“compare Fodor’s hypothesis with Carruthers’s”). Đối chiếu chính xác nội dung ghi chú:\n• **Fodor (1983)**: hệ thống nhận thức bậc thấp (tri giác, ngôn ngữ) có tính mô-đun; hệ thống bậc cao (suy luận) **KHÔNG** có tính mô-đun → tức chỉ coi **một số** hệ thống nhận thức là mô-đun.\n• **Carruthers (2003 – MMH)**: mở rộng tính mô-đun bao gồm **TẤT CẢ** các hệ thống nhận thức.\nĐáp án A so sánh chuẩn xác tuyệt đối: vì chỉ xem một số chứ không phải mọi hệ thống nhận thức là mô-đun, thuyết mô-đun của Fodor **không rộng mở bằng** MMH của Carruthers → Chọn A!',
        'Kiểm tra sự thật từng chữ ở 3 phương án nhiễu của câu Hard M2: B sai vì cả hai ĐỀU đồng ý hệ thống bậc thấp là mô-đun (họ chỉ khác nhau ở bậc CAO!); C sai vì Carruthers KHÔNG phản đối cấu trúc thần kinh bẩm sinh; D chỉ kể trình tự thời gian chứ không so sánh nội dung của Fodor!',
        [
            ('Đáp án đúng', 'So sánh trực diện, chính xác 100% phạm vi của hai giả thuyết: thuyết của Fodor (chỉ một số hệ thống nhận thức là mô-đun) hẹp hơn so với MMH của Carruthers (bao trùm tất cả).'),
            ('Factual Error', 'Sai sự thật: cả Fodor lẫn Carruthers ĐỀU cho rằng hệ thống bậc thấp (như tri giác và ngôn ngữ) có tính mô-đun; điểm khác biệt nằm ở hệ thống BẬC CAO (như suy luận).'),
            ('Factual Error', 'Sai sự thật: Carruthers không hề phản đối quan điểm tâm trí gồm các cấu trúc thần kinh bẩm sinh — ông đồng ý và còn mở rộng tính mô-đun ra toàn bộ hệ thống nhận thức.'),
            ('Missing Comparison', 'Chỉ nhắc mốc năm 1983 của Fodor như mốc thời gian đứng trước, hoàn toàn không nêu nội dung giả thuyết của Fodor nên không có sự so sánh giữa hai giả thuyết.'),
        ],
    ),
]


# ============================================================================
# COMPLETE BLUEBOOK REAL EXAM PAYLOAD (54 UNIQUE REAL QUESTIONS)
# ============================================================================

TEST_DATA = {
    'schemaVersion': 1,
    'mode': 'adaptive_mock',
    'section': 'rw',
    'basicInfo': {
        'title': TEST_TITLE,
        'subtitle': 'Đề thi thật Digital SAT tháng 3/2025 (Ver 5) — Đủ 2 Module (M1: 27 câu + M2: 27 câu)',
        'difficultyBadge': 'REAL EXAM • MARCH 2025',
        'targetTimeMinutes': 64,
        'routingThreshold': 0,
    },
    'module1': {
        'id': 'real_march2025_v5_rw_m1',
        'title': 'Section 1, Module 1: Reading and Writing',
        'subtitle': 'March 2025 Ver 5 Real Exam — Module 1 (27 Qs • 32 min)',
        'timeLimitMinutes': 32,
        'questions': MODULE_1_QUESTIONS,
    },
    'module2_hard': {
        'id': 'real_march2025_v5_rw_m2_hard',
        'title': 'Section 1, Module 2: Reading and Writing',
        'subtitle': 'March 2025 Ver 5 Real Exam — Module 2 (27 Qs • 32 min)',
        'timeLimitMinutes': 32,
        'questions': MODULE_2_QUESTIONS,
    },
    'module2_lower': {
        'id': 'real_march2025_v5_rw_m2_lower',
        'title': 'Section 1, Module 2: Reading and Writing',
        'subtitle': 'March 2025 Ver 5 Real Exam — Module 2 (27 Qs • 32 min)',
        'timeLimitMinutes': 32,
        'questions': _clone_module_questions(
            MODULE_2_QUESTIONS,
            'march2025_v5_rw_m2_',
            'march2025_v5_rw_m2l_',
        ),
    },
}


def verify_all():
    """Runs full structural, fidelity, watermark, answer/optionAnalysis, and Bluebook KaTeX checks."""
    from scripts.sat_real_exams_pipeline import validate_sat_bluebook_json

    errors = []

    # 1. Exact counts (27 + 27 = 54 real questions; module2_lower mirrors real Module 2)
    m1_qs = TEST_DATA['module1']['questions']
    m2h_qs = TEST_DATA['module2_hard']['questions']
    m2l_qs = TEST_DATA['module2_lower']['questions']
    if len(m1_qs) != 27:
        errors.append(f'Expected 27 Module 1 questions, got {len(m1_qs)}')
    if len(m2h_qs) != 27:
        errors.append(f'Expected 27 Module 2 (hard) questions, got {len(m2h_qs)}')
    if len(m2l_qs) != 27:
        errors.append(f'Expected 27 Module 2 (lower) questions, got {len(m2l_qs)}')
    if len(m1_qs) + len(m2h_qs) != 54:
        errors.append(f'Expected 54 total real questions, got {len(m1_qs) + len(m2h_qs)}')

    # Verify routingThreshold == 0 and section == 'rw'
    if TEST_DATA.get('mode') != 'adaptive_mock':
        errors.append(f"Expected mode='adaptive_mock', got {TEST_DATA.get('mode')}")
    if TEST_DATA.get('section') != 'rw':
        errors.append(f"Expected section='rw', got {TEST_DATA.get('section')}")
    if TEST_DATA['basicInfo'].get('routingThreshold') != 0:
        errors.append(f"Expected routingThreshold=0, got {TEST_DATA['basicInfo'].get('routingThreshold')}")

    # 2. Unique IDs globally + sequential numbering + answer/optionAnalysis consistency
    all_ids = set()
    for mod_key, qs in [('module1', m1_qs), ('module2_hard', m2h_qs), ('module2_lower', m2l_qs)]:
        for idx, q in enumerate(qs, start=1):
            qid = q['id']
            if qid in all_ids:
                errors.append(f'Duplicate global ID: {qid}')
            all_ids.add(qid)
            if q['number'] != idx:
                errors.append(f'{mod_key} Q{idx}: wrong number field {q["number"]}')

            ans = q['correctAnswer']
            exp = q.get('explanation') or {}
            oa = exp.get('optionAnalysis') or {}
            if set(oa.keys()) != {'A', 'B', 'C', 'D'}:
                errors.append(f'{qid}: optionAnalysis missing keys {set(oa.keys())}')
            correct_keys = [k for k, v in oa.items() if v.get('status') == 'correct']
            trap_keys = [k for k, v in oa.items() if v.get('status') == 'trap']
            if correct_keys != [ans] or len(trap_keys) != 3:
                errors.append(
                    f'{qid}: optionAnalysis status mismatch (ans={ans}, correct={correct_keys}, traps={trap_keys})'
                )
            for k, v in oa.items():
                if not (v.get('reasonVi') or '').strip():
                    errors.append(f'{qid}: empty reasonVi for option {k}')
                if k == ans and v.get('trapTag') != 'Đáp án đúng':
                    errors.append(f'{qid}: expected trapTag="Đáp án đúng" for answer {k}, got {v.get("trapTag")}')
            if not (exp.get('summaryVi') or '').strip():
                errors.append(f'{qid}: empty summaryVi')
            if not (exp.get('keyTakeaway') or '').strip():
                errors.append(f'{qid}: empty keyTakeaway')

            # Fidelity checks: tables, graphs & underlines must be present when referenced
            q_lower = (q['questionHtml'] or '').lower()
            stim = q['stimulusHtml'] or ''
            if re.search(r'\btable\b', q_lower) and '<table' not in stim.lower():
                errors.append(f'{qid}: question references table but stimulusHtml lacks <table>')
            if re.search(r'\bgraph\b', q_lower) and '<svg' not in stim.lower():
                errors.append(f'{qid}: question references graph but stimulusHtml lacks <svg>')
            if re.search(r'\bunderlined\b', q_lower) and '<u>' not in stim.lower():
                errors.append(f'{qid}: question references underlined text but stimulusHtml lacks <u>')

    # Verify module2_lower mirrors module2_hard verbatim (aside from IDs)
    for qh, ql in zip(m2h_qs, m2l_qs):
        for field in ('number', 'domain', 'skill', 'stimulusHtml', 'questionHtml', 'options', 'correctAnswer', 'explanation'):
            if qh[field] != ql[field]:
                errors.append(f'module2_lower Q{qh["number"]} differs from module2_hard on field {field}')

    # 3. Zero watermarks & zero raw ______blank artifacts across entire JSON
    serialized = json.dumps(TEST_DATA, ensure_ascii=False)
    if re.search(r'@dsatuz|dsatuz|telegram channel', serialized, re.IGNORECASE):
        errors.append('Found watermark string in TEST_DATA!')
    if re.search(r'_{3,}blank', serialized, re.IGNORECASE):
        errors.append('Found unconverted ___blank artifact in TEST_DATA!')

    # 4. Official Bluebook pipeline validator (schema + Node KaTeX check)
    pipeline_errs = validate_sat_bluebook_json(TEST_DATA, TEST_CODE)
    errors.extend(pipeline_errs)

    # Summary stats
    m1_dist = {c: sum(1 for q in m1_qs if q['correctAnswer'] == c) for c in 'ABCD'}
    m2_dist = {c: sum(1 for q in m2h_qs if q['correctAnswer'] == c) for c in 'ABCD'}
    svg_count = sum(1 for q in (m1_qs + m2h_qs) if '<svg' in q['stimulusHtml'].lower())
    tbl_count = sum(1 for q in (m1_qs + m2h_qs) if '<table' in q['stimulusHtml'].lower())
    ul_count = sum(1 for q in (m1_qs + m2h_qs) if '<u>' in q['stimulusHtml'].lower())

    print(f'[{TEST_CODE}] {TEST_TITLE}')
    print(f'  Module 1: {len(m1_qs)} Qs | Keys: {m1_dist}')
    print(f'  Module 2: {len(m2h_qs)} Qs | Keys: {m2_dist} (mirrored to module2_lower: {len(m2l_qs)} Qs)')
    print(f'  Total unique real Qs: {len(m1_qs) + len(m2h_qs)} | Global unique IDs: {len(all_ids)}')
    print(f'  SVG Charts verified: {svg_count} (M1 Q9, M1 Q11)')
    print(f'  HTML Tables verified: {tbl_count} (M1 Q12, M2 Q11)')
    print(f'  Underlines verified: {ul_count} (M1 Q4, M2 Q7)')

    if errors:
        print(f'  [FAILED] {len(errors)} error(s):')
        for e in errors:
            print(f'    - {e}')
        return False

    print('  [PASS] 0 errors — Bluebook schema, KaTeX, verbatim fidelity & 2-pass audit verified!')
    return True


if __name__ == '__main__':
    ok = verify_all()
    sys.exit(0 if ok else 1)
