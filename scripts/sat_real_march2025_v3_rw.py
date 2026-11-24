# -*- coding: utf-8 -*-
"""
Digital SAT 1500+ Real Past Exam — March 2025 Ver 3 Reading & Writing (54 Questions)
- Module 1: 27 Real Questions (32 minutes)
- Module 2: 27 Real Questions (32 minutes, assigned to both module2_hard and module2_lower with routingThreshold=0)
- Architecture: Runtime OCR loader (`scripts/sat_rw_ocr_parser.py` + `scripts/ocr_data/march_v3_rw_raw.json`)
  with compact verified patches for tables, inline SVG charts, underlines, italics, punctuation & OCR fixes
  verified pixel-by-pixel against `scratch/phase2_clean_imgs/march_v3/`.
- Independent 2-Pass Answer Audit completed across all 54 R&W items with rich Vietnamese explanations & trap analysis.
"""

import copy
import json
import os
import re
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

from scripts.sat_rw_ocr_parser import build_rw_questions_from_ocr

TEST_CODE = 'real_march2025_v3_rw'
FOLDER_KEY = 'real_rw'
ORDER_INDEX = 5
TEST_TITLE = '🏛️ Real Exam — March 2025 Ver 3 Reading & Writing (54 Qs)'

RAW_JSON = os.path.join(
    os.path.dirname(os.path.abspath(__file__)),
    'ocr_data',
    'march_v3_rw_raw.json',
)


# ============================================================================
# VISUAL ASSETS: HTML TABLE & INLINE SVG CHARTS (VERIFIED AGAINST SOURCE IMGS)
# ============================================================================

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
        f'<div data-visual="table" style="margin-bottom:14px;">'
        f'<div style="font-family:\'Segoe UI\',system-ui,sans-serif;font-size:13.5px;'
        f'font-weight:800;color:#0f172a;text-align:center;margin-bottom:6px;">{caption}</div>'
        f'<table><thead><tr>{ths}</tr></thead><tbody>{trs}</tbody></table>'
        f'{fn_html}</div>'
    )


def _svg_m1_q12_fta_exports():
    """Recreates the exact March 2025 Ver 3 M1 Q12 grouped bar chart (Pre- and Post-FTA Export Growth Rate)."""
    x_left, x_right = 82, 412
    y_top, y_bot = 24, 184  # 160px span for -5..15 -> 8px per percentage point

    def fy(val):
        return 144.0 - val * 8.0  # y(0) = 144.0

    parts = []
    for val in (-5, 0, 5, 10, 15):
        y = fy(val)
        stroke = '#334155' if val in (-5, 0) else '#94a3b8'
        sw = '1.4' if val in (-5, 0) else '1'
        parts.append(f'<line x1="{x_left}" y1="{y:.1f}" x2="{x_right}" y2="{y:.1f}" stroke="{stroke}" stroke-width="{sw}"/>')
        parts.append(
            f'<text x="{x_left - 8}" y="{y + 4:.1f}" font-size="11.5" text-anchor="end" '
            f'fill="#1e293b" font-family="sans-serif">{val}</text>'
        )

    parts.append(f'<line x1="{x_left}" y1="{y_top}" x2="{x_left}" y2="{y_bot}" stroke="#334155" stroke-width="1.4"/>')

    bar_w = 34
    # Canada (dark gray), Costa Rica (white with black border), Mexico (solid black)
    groups = [
        (115, [(4.7, '#64748b'), (10.0, '#ffffff'), (-1.5, '#0f172a')]),  # Pre-FTA
        (275, [(3.1, '#64748b'), (13.5, '#ffffff'), (13.6, '#0f172a')]),  # Post-FTA
    ]
    y0 = fy(0)
    for gx, bars in groups:
        for i, (val, fill) in enumerate(bars):
            bx = gx + i * bar_w
            yv = fy(val)
            by = min(y0, yv)
            bh = abs(y0 - yv)
            parts.append(
                f'<rect x="{bx}" y="{by:.1f}" width="{bar_w}" height="{bh:.1f}" '
                f'fill="{fill}" stroke="#0f172a" stroke-width="1.3"/>'
            )

    parts.append('<text x="166" y="204" font-size="12" text-anchor="middle" fill="#0f172a" font-family="sans-serif">Pre-FTA</text>')
    parts.append('<text x="326" y="204" font-size="12" text-anchor="middle" fill="#0f172a" font-family="sans-serif">Post-FTA</text>')
    parts.append('<text x="246" y="227" font-size="12" font-weight="600" text-anchor="middle" fill="#0f172a" font-family="sans-serif">Export growth</text>')
    parts.append(
        '<text x="24" y="104" font-size="12" font-weight="600" text-anchor="middle" fill="#0f172a" '
        'font-family="sans-serif" transform="rotate(-90 24 104)">Growth rate (%)</text>'
    )

    parts.append('<rect x="114" y="242" width="234" height="84" fill="#ffffff" stroke="#475569" stroke-width="1.1"/>')
    legend_items = [
        ('#64748b', 'Canada (NAFTA)'),
        ('#ffffff', 'Costa Rica (CAFTA-DR)'),
        ('#0f172a', 'Mexico (NAFTA)'),
    ]
    for idx, (fill, label) in enumerate(legend_items):
        ly = 256 + idx * 24
        parts.append(f'<rect x="128" y="{ly}" width="13" height="13" fill="{fill}" stroke="#0f172a" stroke-width="1.2"/>')
        parts.append(f'<text x="150" y="{ly + 11}" font-size="12" fill="#0f172a" font-family="sans-serif">{label}</text>')

    return (
        '<div data-visual="chart" style="background:#f8fafc;border:1px solid #cbd5e1;border-radius:10px;padding:12px 14px;margin-bottom:12px;">'
        '<div style="font-family:\'Segoe UI\',sans-serif;font-size:13px;font-weight:800;color:#0f172a;'
        'text-align:center;line-height:1.35;margin-bottom:6px;">'
        'Average Total Agricultural Export Growth Rate, Five Years<br/>Pre- and Post-FTA with the United States</div>'
        '<svg viewBox="0 0 450 338" xmlns="http://www.w3.org/2000/svg" style="max-width:440px;width:100%;height:auto;display:block;margin:0 auto;">'
        '<rect x="0" y="0" width="450" height="338" fill="#ffffff"/>'
        f'{"".join(parts)}'
        '</svg></div>'
    )


def _svg_m2_q10_seagrass():
    """Recreates the exact March 2025 Ver 3 M2 Q10 multi-series line graph (Chesapeake Bay Seagrass Coverage 2012–2019)."""
    years = [2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]
    eelgrass = [5500, 6700, 7200, 8300, 8300, 8300, 9600, 5000]
    widgeon = [6000, 8200, 12200, 15600, 17100, 17900, 16200, 8600]
    total = [19500, 24000, 30500, 37500, 40500, 42500, 44000, 26800]

    x_left, x_right = 88, 458
    y_top, y_bot = 20, 195  # 175px span for 0..45,000
    xs = [110 + i * 47 for i in range(len(years))]

    def fy(val):
        return y_bot - (val / 45000.0) * (y_bot - y_top)

    parts = []
    for val in (0, 9000, 18000, 27000, 36000, 45000):
        y = fy(val)
        stroke = '#334155' if val == 0 else '#cbd5e1'
        sw = '1.4' if val == 0 else '1'
        parts.append(f'<line x1="{x_left}" y1="{y:.1f}" x2="{x_right}" y2="{y:.1f}" stroke="{stroke}" stroke-width="{sw}"/>')
        parts.append(
            f'<text x="{x_left - 8}" y="{y + 4:.1f}" font-size="11" text-anchor="end" '
            f'fill="#1e293b" font-family="sans-serif">{val:,}</text>'
        )

    for x, yr in zip(xs, years):
        parts.append(f'<line x1="{x}" y1="{y_top}" x2="{x}" y2="{y_bot}" stroke="#cbd5e1" stroke-width="1"/>')
        parts.append(f'<line x1="{x}" y1="{y_bot}" x2="{x}" y2="{y_bot + 5}" stroke="#334155" stroke-width="1.2"/>')
        parts.append(
            f'<text x="{x + 3}" y="{y_bot + 18}" font-size="11" text-anchor="end" fill="#1e293b" '
            f'font-family="sans-serif" transform="rotate(-38 {x + 3} {y_bot + 18})">{yr}</text>'
        )

    parts.append(f'<line x1="{x_left}" y1="{y_top}" x2="{x_left}" y2="{y_bot}" stroke="#334155" stroke-width="1.4"/>')

    # Series 1: eelgrass (solid line + filled black triangles)
    eel_pts = ' '.join(f'{x},{fy(v):.1f}' for x, v in zip(xs, eelgrass))
    parts.append(f'<polyline points="{eel_pts}" fill="none" stroke="#0f172a" stroke-width="2"/>')
    for x, v in zip(xs, eelgrass):
        y = fy(v)
        parts.append(f'<polygon points="{x},{y - 5.2:.1f} {x - 4.8},{y + 3.8:.1f} {x + 4.8},{y + 3.8:.1f}" fill="#0f172a"/>')

    # Series 2: widgeon grass (dashed line + white squares with black border)
    wid_pts = ' '.join(f'{x},{fy(v):.1f}' for x, v in zip(xs, widgeon))
    parts.append(f'<polyline points="{wid_pts}" fill="none" stroke="#0f172a" stroke-width="2" stroke-dasharray="6,4"/>')
    for x, v in zip(xs, widgeon):
        y = fy(v)
        parts.append(
            f'<rect x="{x - 4.2:.1f}" y="{y - 4.2:.1f}" width="8.4" height="8.4" '
            f'fill="#ffffff" stroke="#0f172a" stroke-width="1.7"/>'
        )

    # Series 3: total of all types of seagrass (dotted line + white circles with black border)
    tot_pts = ' '.join(f'{x},{fy(v):.1f}' for x, v in zip(xs, total))
    parts.append(f'<polyline points="{tot_pts}" fill="none" stroke="#0f172a" stroke-width="2" stroke-dasharray="2.5,3.5"/>')
    for x, v in zip(xs, total):
        y = fy(v)
        parts.append(f'<circle cx="{x}" cy="{y:.1f}" r="4.5" fill="#ffffff" stroke="#0f172a" stroke-width="1.6"/>')

    parts.append(
        '<text x="20" y="108" font-size="11.5" font-weight="600" text-anchor="middle" fill="#0f172a" '
        'font-family="sans-serif" transform="rotate(-90 20 108)">Seagrass area (hectares)</text>'
    )
    parts.append('<text x="273" y="248" font-size="11.5" font-weight="600" text-anchor="middle" fill="#0f172a" font-family="sans-serif">Year</text>')

    parts.append('<rect x="108" y="264" width="290" height="84" fill="#ffffff" stroke="#475569" stroke-width="1.1"/>')
    parts.append('<line x1="122" y1="283" x2="170" y2="283" stroke="#0f172a" stroke-width="2"/>')
    parts.append('<polygon points="146,277.8 141.2,286.8 150.8,286.8" fill="#0f172a"/>')
    parts.append('<text x="180" y="287" font-size="12" fill="#0f172a" font-family="sans-serif">eelgrass</text>')

    parts.append('<line x1="122" y1="307" x2="170" y2="307" stroke="#0f172a" stroke-width="2" stroke-dasharray="6,4"/>')
    parts.append('<rect x="141.8" y="302.8" width="8.4" height="8.4" fill="#ffffff" stroke="#0f172a" stroke-width="1.7"/>')
    parts.append('<text x="180" y="311" font-size="12" fill="#0f172a" font-family="sans-serif">widgeon grass</text>')

    parts.append('<line x1="122" y1="331" x2="170" y2="331" stroke="#0f172a" stroke-width="2" stroke-dasharray="2.5,3.5"/>')
    parts.append('<circle cx="146" cy="331" r="4.5" fill="#ffffff" stroke="#0f172a" stroke-width="1.6"/>')
    parts.append('<text x="180" y="335" font-size="12" fill="#0f172a" font-family="sans-serif">total of all types of seagrass</text>')

    return (
        '<div data-visual="chart" style="background:#f8fafc;border:1px solid #cbd5e1;border-radius:10px;padding:12px 14px;margin-bottom:12px;">'
        '<div style="font-family:\'Segoe UI\',sans-serif;font-size:13px;font-weight:800;color:#0f172a;'
        'text-align:center;line-height:1.35;margin-bottom:6px;">'
        'Chesapeake Bay Seagrass Coverage 2012–2019</div>'
        '<svg viewBox="0 0 490 360" xmlns="http://www.w3.org/2000/svg" style="max-width:480px;width:100%;height:auto;display:block;margin:0 auto;">'
        '<rect x="0" y="0" width="490" height="360" fill="#ffffff"/>'
        f'{"".join(parts)}'
        '</svg></div>'
    )


# ============================================================================
# HELPER: METADATA BUILDER & OCR REFLOW POST-PROCESSOR
# ============================================================================

def meta(domain, skill, difficulty, answer, summary_vi, takeaway, analysis):
    """Builds a validated metadata + Vietnamese explanation dict for build_rw_questions_from_ocr."""
    labels = ['A', 'B', 'C', 'D']
    assert answer in labels, f'Invalid answer: {answer}'
    assert len(analysis) == 4, f'Expected 4 optionAnalysis tuples, got {len(analysis)}'
    return {
        'domain': domain,
        'skill': skill,
        'difficulty': difficulty,
        'answer': answer,
        'explanation': {
            'summaryVi': summary_vi,
            'keyTakeaway': takeaway,
            'optionAnalysis': {
                labels[i]: {
                    'status': 'correct' if labels[i] == answer else 'trap',
                    'trapTag': analysis[i][0],
                    'reasonVi': analysis[i][1],
                }
                for i, lbl in enumerate(labels)
            },
        },
    }


def _reflow_and_patch(questions, post_patches, bullet_qnums=(), dual_qnums=()):
    """
    Merges spurious per-line </p>\\n<p> splits produced by Tesseract OCR into clean continuous
    paragraphs, formats Rhetorical Synthesis bullet lists (<ul><li>) and Dual Texts (Text 1 / Text 2),
    strips leading stray prompt quotes, and applies exact verified post-reflow patches (asserting every match).
    """
    for q in questions:
        num = q['number']
        stim = q['stimulusHtml']

        # Preserve prepended visual container (table or SVG chart) intact
        visual_prefix = ''
        m_vis = re.match(r'^(\s*<div data-visual="[^"]+"[\s\S]*?</div>)\s*\n(.*)$', stim, re.DOTALL)
        if m_vis:
            visual_prefix = m_vis.group(1) + '\n'
            body_html = m_vis.group(2)
        else:
            body_html = stim

        # Flatten OCR line-wrap <p>...</p> into single clean text while preserving word spacing
        raw_paras = re.findall(r'<p>(.*?)</p>', body_html, re.DOTALL)
        merged = ' '.join(p.strip() for p in raw_paras if p.strip())
        # Rejoin hyphenated line breaks like "mass- produce" / "non- native" (preserving suspended hyphens like "Pre- and")
        merged = re.sub(r'([A-Za-z])-\s+(?!and\b|or\b)([a-z])', r'\1-\2', merged)
        merged = re.sub(r'\s+', ' ', merged).strip()

        # Apply verified targeted post-reflow stimulus replacements (asserting every tuple matches)
        pt = post_patches.get(num, {})
        for old, new in pt.get('stim_replace', []):
            if old not in merged:
                raise AssertionError(f"{q['id']}: stim_replace target not found: {old!r}\n  in: {merged!r}")
            merged = merged.replace(old, new)

        # Format structure cleanly
        if num in bullet_qnums:
            # Split intro line (if present) and bullet items marked by ' ||BULLET|| '
            parts = [p.strip() for p in merged.split('||BULLET||') if p.strip()]
            if parts and parts[0].lower().startswith('while researching'):
                intro = f'<p>{parts[0]}</p>'
                items = parts[1:]
            else:
                intro = ''
                items = parts
            lis = ''.join(f'<li>{it}</li>' for it in items)
            body_out = f'{intro}<ul style="list-style-type:disc;padding-left:1.5em;margin-top:6px;">{lis}</ul>'
        elif num in dual_qnums:
            # Dual text split on ||TEXT2||
            t1, t2 = [p.strip() for p in merged.split('||TEXT2||', 1)]
            t1 = re.sub(r'^Text\s+1\s*', '', t1)
            t2 = re.sub(r'^Text\s+2\s*', '', t2)
            body_out = (
                f'<p><strong>Text 1</strong></p><p>{t1}</p>'
                f'<p style="margin-top:12px;"><strong>Text 2</strong></p><p>{t2}</p>'
            )
        elif '||EXCERPT||' in merged:
            segs = merged.split('||EXCERPT||')
            intro_p = f'<p>{segs[0].strip()}</p>'
            rest = segs[1].strip()
            if '||COPY||' in rest:
                body_txt, copy_txt = [x.strip() for x in rest.split('||COPY||', 1)]
                body_out = (
                    f'{intro_p}'
                    f'<p style="padding-left:1.5em;">{body_txt}</p>'
                    f'<p style="text-align:right;font-size:12px;color:#475569;">{copy_txt}</p>'
                )
            else:
                body_out = f'{intro_p}<p style="padding-left:1.5em;">{rest}</p>'
        else:
            body_out = f'<p>{merged}</p>'

        q['stimulusHtml'] = visual_prefix + body_out

        # Clean stray OCR punctuation/artifacts in questionHtml & options
        qh = q['questionHtml']
        qh = re.sub(r'^<p>\s*[‘\'\"`\-\[\]]+\s*', '<p>', qh)
        for old, new in pt.get('q_replace', []):
            if old not in qh:
                raise AssertionError(f"{q['id']}: q_replace target not found: {old!r} in {qh!r}")
            qh = qh.replace(old, new)
        q['questionHtml'] = qh

        for o in q['options']:
            txt = o['text']
            txt = re.sub(r'([A-Za-z])-\s+([a-z])', r'\1-\2', txt)
            for old, new in pt.get('opt_replace', []):
                txt = txt.replace(old, new)
            o['text'] = txt.strip()


def _clone_module_questions(questions, old_prefix, new_prefix):
    cloned = copy.deepcopy(questions)
    for q in cloned:
        q['id'] = q['id'].replace(old_prefix, new_prefix, 1)
    return cloned


# ============================================================================
# MODULE 1: METADATA, 2-PASS AUDITED ANSWERS, VIETNAMESE EXPLANATIONS & PATCHES
# ============================================================================

M1_META = {
    1: meta(
        'Craft and Structure', 'Words in Context', 'Easy', 'B',
        'Dấu hai chấm mở ra phần giải thích trực tiếp cho chỗ trống: “showcased a diverse range of musical talents in different areas, from orchestral pieces and operas to popular film scores” (thể hiện tài năng âm nhạc đa dạng ở nhiều lĩnh vực khác nhau). Từ đồng nghĩa chuẩn nhất với “diverse” là “varied” (đa dạng, phong phú) → Chọn B.',
        'Khi thấy dấu hai chấm (:) kèm cụm giải nghĩa trực tiếp như “a diverse range... in different areas”, hãy chọn ngay tính từ đồng nghĩa sát nghĩa nhất = varied.',
        [
            ('Opposite Tone', 'outdated = lỗi thời — mâu thuẫn với sắc thái khen ngợi “Especially impressive” và không khớp ý “diverse range”.'),
            ('Đáp án đúng', 'varied = đa dạng, phong phú — khớp 100% với “diverse range of musical talents in different areas”.'),
            ('Opposite Tone', 'forgotten = bị lãng quên — trái với ngữ cảnh ca ngợi kho tàng sáng tác phong phú của Lecuona.'),
            ('Wrong Meaning', 'lonely = cô đơn — không phù hợp để mô tả sự đa dạng thể loại của một sự nghiệp âm nhạc.'),
        ],
    ),
    2: meta(
        'Craft and Structure', 'Words in Context', 'Easy', 'D',
        'Câu ngay trước từ gạch chân nêu rõ yêu cầu đặt ra: “I was supposed to memorize the whole thing” (tôi đáng lẽ phải học thuộc lòng toàn bộ bản nhạc). Thay vì làm đúng yêu cầu đó, cô bé lại vừa đánh vài ô nhịp vừa “cheating, looking up to see what notes followed” (liếc nhìn bản nhạc xem nốt tiếp theo). Vì vậy “cheating” ở đây mang nghĩa cô bé đang phá vỡ kỳ vọng/quy định về cách trình bày bản nhạc → Chọn D.',
        'Với dạng Words in Context hỏi ý nghĩa từ trong văn học, luôn đọc câu liền trước (“was supposed to...”) và cụm giải thích sau dấu phẩy (“looking up to see what notes followed”), tuyệt đối không tự bịa thêm nhân vật không xuất hiện trong đoạn trích.',
        [
            ('Unsupported Context', 'Cô bé chỉ đang tập đàn một mình ở nhà, không hề gian lận để giành lợi thế trước các thí sinh khác trong buổi diễn.'),
            ('Misinterpretation', 'Cô bé không tự lừa dối về năng lực âm nhạc của mình (cô nhận xét thẳng bài nhạc vốn đơn giản và mình chỉ lơ đãng).'),
            ('Not Mentioned', 'Đoạn trích hoàn toàn không nhắc đến nhân vật giáo viên dạy piano nào.'),
            ('Đáp án đúng', 'Khớp hoàn hảo với việc phá vỡ yêu cầu “I was supposed to memorize the whole thing” bằng cách liếc nhìn nốt nhạc.'),
        ],
    ),
    3: meta(
        'Craft and Structure', 'Words in Context', 'Easy', 'A',
        'Cụm sau dấu gạch ngang dài (—) là đồng vị ngữ gọi tên lại hành động “Volunteers share digitized excerpts from personal collections...” (tình nguyện viên chia sẻ các đoạn trích số hóa từ bộ sưu tập cá nhân cho một dự án từ điển cộng đồng / crowdsourced project). Những tư liệu chia sẻ đó chính là các “đóng góp” → Chọn A (“contributions”).',
        'Khi chỗ trống đứng ngay sau dấu gạch ngang (—) để gọi tên lại thứ vừa được tình nguyện viên chia sẻ trong một dự án cộng đồng (“crowdsourced project”), hãy chọn “contributions”.',
        [
            ('Đáp án đúng', 'contributions = những đóng góp — mô tả chính xác các đoạn trích tạp chí số hóa do tình nguyện viên gửi lên dự án.'),
            ('Wrong Meaning', 'resolutions = quyết nghị, sự giải quyết — không thể dùng để gọi các đoạn trích tạp chí khoa học viễn tưởng.'),
            ('Wrong Meaning', 'justifications = lời biện minh, lý do bào chữa — sai hoàn toàn ngữ cảnh.'),
            ('Wrong Meaning', 'negotiations = cuộc đàm phán, thương lượng — không khớp hành động chia sẻ tư liệu.'),
        ],
    ),
    4: meta(
        'Craft and Structure', 'Words in Context', 'Medium', 'D',
        'Hai manh mối trực tiếp trong bài là thuật ngữ “Agglomeration” (tụ tập thành cụm) và động từ ở câu kế tiếp “companies cluster” (các công ty tập trung thành cụm). Khi nhiều doanh nghiệp trong các ngành liên quan tụ họp dày đặc tại một khu vực (như ngành sắt thép và dao kéo ở Wolverhampton), cụm động từ chính xác là “amass in” (tập trung/tích tụ với số lượng lớn tại) → Chọn D.',
        'Luôn quét câu liền sau để tìm từ lặp ý: “companies cluster” chính là lời giải mã trực tiếp cho cụm “amass in” (tụ tập tại một khu vực).',
        [
            ('Wrong Meaning', 'intercede in = can thiệp để hòa giải — không mang nghĩa doanh nghiệp tụ tập địa lý.'),
            ('Wrong Meaning', 'concur with = đồng tình với — sai cả nghĩa lẫn giới từ khi đi cùng “an area”.'),
            ('Wrong Meaning', 'appeal to = thu hút hoặc kêu gọi — không diễn tả hiện tượng hình thành cụm công nghiệp.'),
            ('Đáp án đúng', 'amass in = tụ tập, tập trung với số lượng lớn tại một khu vực — đồng nghĩa trực tiếp với “cluster” và “agglomeration”.'),
        ],
    ),
    5: meta(
        'Craft and Structure', 'Text Structure and Purpose', 'Easy', 'B',
        'Đoạn trích cho thấy Adam tinh ý nhận ra bác Richard thích thú với con tàu (consideration), mời ông nghỉ lại qua đêm trên tàu và sẵn sàng khởi hành vào bất cứ giờ nào, đi bất cứ đâu ông muốn (flexibility). Chính sự chu đáo và linh hoạt ấy đã “won the old man’s heart”, khiến hai bác cháu lập tức trở nên gắn bó gần như những người bạn cũ → Chọn B.',
        'Trong câu hỏi Main Purpose của đoạn văn học, luôn nối hành động trọng tâm của nhân vật (chu đáo + linh hoạt) với hệ quả cảm xúc trực tiếp ở cuối đoạn (tình cảm bác cháu thêm thân thiết).',
        [
            ('Factual Distortion', 'Trái ngược văn bản: câu đầu nói cuộc gặp bắt đầu cực kỳ suôn sẻ (“so auspiciously begun”), không hề có ấn tượng dè chừng (“wary first impressions”).'),
            ('Đáp án đúng', 'Tóm gọn trọn vẹn trọng tâm đoạn trích: sự linh hoạt và chu đáo của Adam đã thắt chặt tình cảm với người bác Richard.'),
            ('Unsupported Comparison', 'Tự bịa chi tiết so sánh với việc “finding lodging on land” và bỏ sót ý chính về mối quan hệ gắn bó.'),
            ('Unsupported Detail', 'Bài không nói họ háo hức cho chuyến hải trình trên tàu — họ chỉ ngủ lại một đêm trên tàu rồi xuất phát theo kế hoạch của ông Richard.'),
        ],
    ),
    6: meta(
        'Craft and Structure', 'Text Structure and Purpose', 'Easy', 'B',
        'Phân tích cấu trúc từng câu theo đúng trình tự: Câu 1 nhận diện và định nghĩa một phương pháp nghiên cứu cụ thể (“Community science”); Câu 2 liệt kê các lợi ích của phương pháp đó (hỗ trợ bảo tồn, khơi dậy đam mê khoa học ở giới trẻ, tăng lượng dữ liệu thu thập); Câu 3 nêu một nghiên cứu thực tế áp dụng phương pháp ấy (nghiên cứu của Abbigail Merrill về màu sắc bướm và lựa chọn hoa) → Chọn B.',
        'Với câu hỏi Overall Structure, hãy gán nhãn chức năng ngắn cho từng câu (1: Định nghĩa phương pháp → 2: Lợi ích → 3: Ví dụ nghiên cứu áp dụng) rồi kiểm tra từng vế theo đúng thứ tự.',
        [
            ('Wrong Order / Missing', 'Câu mở đầu giới thiệu phương pháp “community science” chứ không giới thiệu chủ đề của một nghiên cứu cụ thể, và cuối bài cũng không nêu kết quả nghiên cứu.'),
            ('Đáp án đúng', 'Khớp chính xác cả 3 chặng: nhận diện phương pháp nghiên cứu → liệt kê lợi ích → dẫn ra nghiên cứu đã sử dụng phương pháp đó.'),
            ('Unsupported Detail', 'Bài không tranh luận đây là phương pháp “mới” và hoàn toàn không nhắc đến “dư luận công chúng” (public’s opinion).'),
            ('Unsupported Ending', 'Bài không kể quá trình phát triển lịch sử và cũng không đề xuất các dự án hợp tác trong tương lai.'),
        ],
    ),
    7: meta(
        'Information and Ideas', 'Central Ideas and Details', 'Easy', 'A',
        'Câu thứ 3 của đoạn văn nêu trực tiếp: “For example, scientists used the <i>Voyager 1</i> space probe to discover Adrastea in 1979.” → Mặt trăng Adrastea được phát hiện năm 1979 → Chọn A.',
        'Với câu hỏi Detail (“According to the text...”), quét đúng tên riêng đối tượng (“Adrastea”) để tránh rơi vào bẫy lấy nhầm năm của đối tượng khác (“1610” là năm phát hiện mặt trăng Io).',
        [
            ('Đáp án đúng', 'Trích xuất chính xác mốc thời gian phát hiện Adrastea nhờ tàu Voyager 1: năm 1979.'),
            ('Not Mentioned', 'Năm 1892 không hề xuất hiện trong đoạn văn.'),
            ('Not Mentioned', 'Năm 2001 không hề xuất hiện trong đoạn văn.'),
            ('Wrong Entity', '1610 là năm Galileo phát hiện mặt trăng Io, không phải Adrastea.'),
        ],
    ),
    8: meta(
        'Information and Ideas', 'Central Ideas and Details', 'Easy', 'D',
        'Đối chiếu thông tin xuất hiện ở cả hai bảo tàng: Museo de Las Americas được thành lập năm 1991 (“Founded in 1991”), trong khi LA Plaza de Cultura y Artes mở cửa năm 2011 (“It opened in 2011”). Do đó LA Plaza de Cultura y Artes mở cửa gần đây hơn → Chọn D.',
        'Khi câu hỏi yêu cầu tìm điểm tương phản (“Which contrast...”), chỉ chọn tiêu chí có số liệu/dữ kiện của CẢ HAI đối tượng trong văn bản (1991 vs. 2011).',
        [
            ('Not Mentioned', 'Bài không hề đề cập đến số lượng khách tham quan của hai bảo tàng.'),
            ('One-Sided Data', 'Bài chỉ cho biết Museo de Las Americas có hơn 4.800 hiện vật, không có số liệu của LA Plaza nên không thể so sánh.'),
            ('Not Mentioned', 'Bài không đề cập diện tích hay quy mô tòa nhà của hai bảo tàng.'),
            ('Đáp án đúng', 'Chính xác: Museo de Las Americas thành lập năm 1991 còn LA Plaza de Cultura y Artes mở cửa muộn hơn vào năm 2011.'),
        ],
    ),
    9: meta(
        'Information and Ideas', 'Command of Evidence', 'Easy', 'D',
        'Nhận định cần minh họa: ngôi nhà của một nhân vật đã trở nên “very faded in appearance over time” (rất bạc màu/phai tàn theo thời gian). Đáp án D diễn tả trọn vẹn tiến trình phai màu đó: từng được sơn (“Once the house had been painted”), nhưng nắng làm phồng rộp, mưa rửa trôi lớp sơn, và giờ ngôi nhà trở nên xám xịt ảm đạm (“now the house was as dull and gray as everything else”) → Chọn D.',
        'Với câu hỏi Literary Quotation Evidence, gạch chân cụm từ khóa kép trong nhận định (“character’s house” + “very faded... over time”) và tìm câu trích dẫn thể hiện rõ cả chủ thể lẫn sự phai tàn theo thời gian.',
        [
            ('Opposite Detail', 'Mô tả những ngôi nhà bằng sứ sơn màu rực rỡ nhất (“painted in the brightest colors”) — trái ngược hoàn toàn với “faded”.'),
            ('Off-Topic Detail', 'Chỉ liệt kê nội thất bên trong căn phòng (bếp lò, tủ chén, bàn ghế, giường), không nói về lớp ngoài ngôi nhà bị bạc màu.'),
            ('Wrong Target', 'Từ “gray” ở đây miêu tả thảo nguyên mênh mông bên ngoài (“the great gray prairie”), không phải ngôi nhà bị phai màu theo thời gian.'),
            ('Đáp án đúng', 'Minh họa trực diện quá trình ngôi nhà từng có lớp sơn nhưng bị nắng mưa làm bong tróc và trở nên xám xịt theo thời gian.'),
        ],
    ),
    10: meta(
        'Information and Ideas', 'Command of Evidence', 'Medium', 'D',
        'Nhà hóa học Christian Adlhart cho rằng miếng bọt biển tổng hợp này sẽ khó sản xuất hàng loạt (“difficult to mass-produce”). Câu thứ 2 của bài cho biết miếng bọt biển này cấu tạo chủ yếu từ tinh bột và gelatin (“composed mainly of starch and gelatin”). Nếu nguồn cung tinh bột và gelatin trên toàn cầu đang bị ngành thực phẩm tiêu thụ rất mạnh khiến việc thu mua số lượng lớn trở nên khó khăn (D), thì lập luận “khó sản xuất hàng loạt” của Adlhart được củng cố trực tiếp → Chọn D.',
        'Để củng cố nhận định ở cuối đoạn (“difficult to mass-produce”), luôn nối nó với thành phần/cơ chế cốt lõi đã nêu ở đầu đoạn (“composed mainly of starch and gelatin”).',
        [
            ('Irrelevant Detail', 'Nguồn gốc vi nhựa từ ngành dệt may trong đại dương không liên quan đến khả năng sản xuất hàng loạt miếng bọt biển.'),
            ('Opposite / Weakens', 'Trọng lượng nhẹ dễ vận chuyển lại ủng hộ tính thương mại hóa, không chứng minh nó khó sản xuất hàng loạt.'),
            ('Wrong Target', 'Khả năng hấp thụ thay đổi tùy dung dịch nói về hiệu quả sử dụng, không phải rào cản sản xuất hàng loạt.'),
            ('Đáp án đúng', 'Khó tìm đủ nguồn nguyên liệu cốt lõi (starch và gelatin) với số lượng lớn trực tiếp chứng minh miếng bọt biển khó sản xuất hàng loạt.'),
        ],
    ),
    11: meta(
        'Information and Ideas', 'Command of Evidence', 'Easy', 'C',
        'Nhận định có 2 điều kiện bắt buộc: tác giả Winnemucca (1) trực tiếp xưng hô/nói chuyện với người đọc (“directly addresses the reader”) VÀ (2) giải thích một phong tục nào đó (“explain certain customs”). Chỉ câu C thỏa mãn đồng thời cả hai: “Now, my dear reader” (xưng hô trực tiếp) + “that is why [my people] call all good people father or mother” (giải thích phong tục gọi người tốt là cha hoặc mẹ) → Chọn C.',
        'Cảnh giác bẫy “nửa đúng” kinh điển của SAT Evidence: câu A chỉ giải thích phong tục mà không xưng hô với độc giả; câu D chỉ xưng hô (“dear readers”) mà không giải thích phong tục. Chỉ chọn đáp án đủ cả 2 vế!',
        [
            ('Half-Right Trap', 'Có giải thích phong tục đặt tên con gái theo loài hoa, nhưng KHÔNG hề xưng hô trực tiếp với người đọc.'),
            ('Off-Topic Detail', 'Chỉ kể lại một sự việc thường nhật với mẹ và ông ngoại — không xưng hô với độc giả và cũng không giải thích phong tục.'),
            ('Đáp án đúng', 'Đáp ứng trọn vẹn cả 2 tiêu chí: gọi trực tiếp “my dear reader” và giải thích phong tục gọi mọi người tốt là “father or mother”.'),
            ('Half-Right Trap', 'Có xưng hô trực tiếp “Some of you, dear readers”, nhưng hoàn toàn không giải thích phong tục nào.'),
        ],
    ),
    12: meta(
        'Information and Ideas', 'Command of Evidence', 'Medium', 'D',
        'Nhận định của học sinh: tham gia Hiệp định Thương mại Tự do (FTA) với Mỹ sẽ làm TĂNG tốc độ tăng trưởng xuất khẩu nông sản trung bình của một quốc gia. Để làm suy yếu (weaken) nhận định này, ta cần tìm quốc gia trên biểu đồ có tốc độ tăng trưởng Post-FTA THẤP HƠN Pre-FTA. Quan sát cột màu xám đậm của Canada (NAFTA): Pre-FTA đạt khoảng 4,7%, còn Post-FTA giảm xuống chỉ còn khoảng 3,1%. Dù vẫn tăng trưởng dương, tốc độ sau FTA thấp hơn trước FTA → Chọn D.',
        'Với bài biểu đồ yêu cầu “weaken the claim” rằng X làm tăng Y, hãy quét ngay thanh/cột nào đi NGƯỢC xu hướng (Post-FTA < Pre-FTA): đó chính là Canada (~4,7% giảm còn ~3,1%).',
        [
            ('Strengthens Claim', 'Mexico tăng mạnh từ âm (~ -1,5%) lên dương (~ +13,6%) sau NAFTA — dữ liệu này củng cố chứ không làm suy yếu nhận định.'),
            ('Irrelevant / Too General', 'Chỉ nói cả 3 nước đều có mức tăng trưởng dương sau FTA với tỷ lệ khác nhau, không so sánh Post-FTA với Pre-FTA để bác bỏ nhận định.'),
            ('Strengthens Claim', 'Costa Rica tăng từ ~10% lên ~13,5% sau CAFTA-DR — cũng củng cố nhận định thay vì làm suy yếu.'),
            ('Đáp án đúng', 'Phản ví dụ trực tiếp từ biểu đồ: Canada có tốc độ tăng trưởng nông sản trước NAFTA (~4,7%) cao hơn cả sau khi vào NAFTA (~3,1%).'),
        ],
    ),
    13: meta(
        'Information and Ideas', 'Command of Evidence', 'Medium', 'C',
        'Kết luận của Pereira et al. gồm 2 vế: (1) Tập luyện thể chất (EET) hiệu quả hơn hội thảo sức khỏe (EHP) trong việc kiềm chế tổn thất năng suất, VÀ (2) kết quả này cần thời gian mới bộc lộ rõ (“took time to become apparent”). Dữ liệu bảng chứng minh hoàn hảo cả 2 vế: ở tuần 12, hai nhóm khá sát nhau (EET = 268 AUD vs. EHP = 282 AUD), nhưng đến tháng 12, tổn thất của EHP tăng vọt lên 436 AUD trong khi EET giảm mạnh xuống chỉ còn 171 AUD → Chọn C.',
        'Khi kết luận có vế phụ chỉ thời gian (“took time to become apparent”), đáp án đúng luôn phải mô tả ĐỦ hai mốc: gần tương đương ở mốc đầu (12 tuần: 268 vs. 282) và tách biệt rõ rệt ở mốc sau (12 tháng: 171 vs. 436).',
        [
            ('Not in Table', 'Bảng chỉ đưa ra tổng tổn thất năng suất quy ra tiền, hoàn toàn không tách tỷ lệ giữa absenteeism và presenteeism.'),
            ('Data Distortion', 'Sai số liệu: EET giảm từ 268 xuống 171 AUD (giảm tới ~36%), tuyệt đối không phải “barely decreased” (hầu như không giảm).'),
            ('Đáp án đúng', 'Khớp 100% bảng số liệu và cả hai vế kết luận: tương đương ở tuần 12 (268 vs. 282) rồi phân hóa mạnh ở tháng 12 (EHP tăng vọt 436, EET giảm sâu 171).'),
            ('Data Distortion', 'Sai ngược hướng chênh lệch: khoảng cách giữa hai nhóm TĂNG mạnh từ 14 AUD (tuần 12) lên 265 AUD (tháng 12), không phải “decreased”.'),
        ],
    ),
    14: meta(
        'Information and Ideas', 'Command of Evidence', 'Medium', 'B',
        'Câu gạch chân nêu: khi phong trào lan rộng ra NGOÀI Chile (“spread beyond Chile”), phạm vi các truyền thống âm nhạc được tích hợp vào nền tảng của nó cũng mở rộng (“the breadth of musical traditions incorporated into its foundation also expanded”). Đáp án B minh họa trực tiếp điều này: nhiều ca khúc mang ảnh hưởng phong cách của <i>corrido</i> — một thể loại dân ca tự sự đến từ Mexico (truyền thống âm nhạc ngoài Chile!) → Chọn B.',
        'Đọc sát từng từ khóa của câu gạch chân: “beyond Chile” (ngoài Chile) + “breadth of musical traditions” (truyền thống âm nhạc mới được đưa vào) → loại ngay nhạc cụ vốn có ở Chile (A), nội dung chính trị (C), hay chỉ nêu xuất xứ nghệ sĩ (D).',
        [
            ('Still Inside Chile', 'Sáo <i>quena</i> là nhạc cụ truyền thống có sẵn ở các nước vùng Andes, bao gồm cả Chile — không chứng minh việc tiếp thu truyền thống âm nhạc ngoài Chile.'),
            ('Đáp án đúng', 'Minh họa trọn vẹn việc phong trào tiếp nhận thêm truyền thống âm nhạc bên ngoài Chile (thể loại <i>corrido</i> của Mexico).'),
            ('Wrong Focus', 'Chỉ nhắc tới chủ đề bình luận chính trị về hậu quả thực dân châu Âu, không nói về việc mở rộng “truyền thống âm nhạc”.'),
            ('Geographic Only', 'Chỉ cho thấy nghệ sĩ Argentina và các nước Mỹ Latinh khác sáng tác ca khúc, không nói họ tích hợp thêm truyền thống âm nhạc mới nào.'),
        ],
    ),
    15: meta(
        'Standard English Conventions', 'Form, Structure, and Sense', 'Easy', 'A',
        'Câu thứ hai có chủ ngữ số nhiều là “Puerto Rico’s museums” và chưa hề có động từ chính chia thì (finite verb). Vì vậy chỗ trống bắt buộc phải là động từ chính số nhiều ở thì hiện tại đơn: “inform” → Chọn A.',
        'Luôn kiểm tra câu đã có động từ chính chia thì (finite verb) chưa: các dạng V-ing, to V, having V3 đều là non-finite verbs và sẽ biến câu thành mảnh câu thiếu vị ngữ (fragment).',
        [
            ('Đáp án đúng', 'inform — động từ chính chia thì hiện tại đơn, hòa hợp hoàn hảo với chủ ngữ số nhiều “Puerto Rico’s museums”.'),
            ('Sentence Fragment', 'informing — hiện tại phân từ, không thể làm động từ chính chia thì cho câu.'),
            ('Sentence Fragment', 'to inform — động từ nguyên mẫu có “to”, khiến câu thiếu động từ chính.'),
            ('Sentence Fragment', 'having informed — phân từ hoàn thành, khiến câu trở thành fragment.'),
        ],
    ),
    16: meta(
        'Standard English Conventions', 'Form, Structure, and Sense', 'Easy', 'C',
        'Cụm trạng ngữ chỉ thời gian “nearly 150 years ago” (gần 150 năm trước) xác định một hành động đã hoàn tất trọn vẹn trong quá khứ (và danh họa Van Gogh cũng đã qua đời). Do đó phải chia thì quá khứ đơn “completed” → Chọn C.',
        'Gặp mốc thời gian kết thúc trong quá khứ như “nearly 150 years ago”, luôn dùng thì Quá khứ đơn (Simple Past = completed).',
        [
            ('Wrong Tense', 'is completing — thì hiện tại tiếp diễn, vô lý với hành động diễn ra gần 150 năm trước.'),
            ('Wrong Tense', 'will complete — thì tương lai đơn, mâu thuẫn với mốc quá khứ “150 years ago”.'),
            ('Đáp án đúng', 'completed — thì quá khứ đơn, chuẩn xác 100% với mốc thời gian “nearly 150 years ago”.'),
            ('Wrong Tense', 'has been completing — hiện tại hoàn thành tiếp diễn, hàm ý vẫn đang tiếp tục đến nay (sai).'),
        ],
    ),
    17: meta(
        'Standard English Conventions', 'Boundaries', 'Easy', 'C',
        'Ta có 2 mệnh đề độc lập (Independent Clauses) rõ ràng: IC1 = “Kizomba... has become an international phenomenon” và IC2 = “In 2022, the Indian dance duo... defeated performers...”. Cần dấu chấm câu để tách hai mệnh đề độc lập này thành hai câu hoàn chỉnh → “phenomenon. In” → Chọn C.',
        'Hai mệnh đề độc lập KHÔNG thể nối bằng khoảng trắng (run-on), chỉ một dấu phẩy (comma splice), hay “and” không có dấu phẩy phía trước. Chọn dấu chấm (.) hoặc dấu chấm phẩy (;).',
        [
            ('Run-On Sentence', 'phenomenon in — ghép hai mệnh đề độc lập không có dấu câu hay liên từ (fused sentence).'),
            ('Missing Comma', 'phenomenon and in — nối hai mệnh đề độc lập bằng FANBOYS “and” mà thiếu dấu phẩy phía trước.'),
            ('Đáp án đúng', 'phenomenon. In — tách rành mạch hai mệnh đề độc lập thành hai câu chuẩn xác.'),
            ('Comma Splice', 'phenomenon, in — lỗi dùng chỉ một dấu phẩy để nối hai mệnh đề độc lập.'),
        ],
    ),
    18: meta(
        'Standard English Conventions', 'Boundaries', 'Easy', 'D',
        'Ta có 2 mệnh đề độc lập: IC1 = “Round Rock Chapter, which covers 201,000 acres, is one of the 110 chapters of the Navajo Nation” và IC2 = “In <i>Diné bizaad</i> (the Navajo language), the chapter is called <i>Tsé Nikání</i>.” Phải dùng dấu chấm câu để tách hai mệnh đề độc lập này → “Nation. In” → Chọn D.',
        'Nhận diện hai cấu trúc S + V hoàn chỉnh liên tiếp (“Round Rock Chapter... is...” và “the chapter is called...”) → tách bằng dấu chấm câu “Nation. In”.',
        [
            ('Missing Comma', 'Nation and in — thiếu dấu phẩy trước “and” khi nối hai mệnh đề độc lập.'),
            ('Run-On Sentence', 'Nation in — lỗi fused sentence khi ghép trực tiếp hai mệnh đề độc lập.'),
            ('Comma Splice', 'Nation, in — lỗi comma splice khi chỉ dùng dấu phẩy nối hai mệnh đề độc lập.'),
            ('Đáp án đúng', 'Nation. In — ngắt đúng ranh giới giữa hai mệnh đề độc lập hoàn chỉnh.'),
        ],
    ),
    19: meta(
        'Standard English Conventions', 'Boundaries', 'Medium', 'B',
        'Mệnh đề chính “It explores how Indigenous Haudenosaunee culture shaped the woman suffrage movement in the early nineteenth century” đã trọn vẹn, theo sau bởi một cụm phân từ bổ nghĩa (nonrestrictive participial phrase) “revealing how the personal and political authority... influenced the first suffragists in the US.” Để gắn cụm phân từ giải thích/mở rộng cho cả mệnh đề phía trước, quy tắc chuẩn là dùng một dấu phẩy → “century, revealing” → Chọn B.',
        'Khi một cụm V-ing (“revealing...”) đứng ở cuối câu để bổ nghĩa cho toàn bộ mệnh đề chính phía trước, hãy nối bằng MỘT DẤU PHẨY (, V-ing) — không dùng dấu chấm (tạo fragment) và không bỏ dấu phẩy (khiến V-ing bổ nghĩa nhầm cho danh từ ngay trước nó).',
        [
            ('Improper Colon', 'century: revealing — không dùng dấu hai chấm giữa mệnh đề chính và cụm phân từ bổ nghĩa mở rộng động từ “explores”.'),
            ('Đáp án đúng', 'century, revealing — chuẩn quy tắc dùng dấu phẩy để nối cụm phân từ “revealing...” bổ nghĩa cho mệnh đề phía trước.'),
            ('Sentence Fragment', 'century. Revealing — biến cụm phân từ “Revealing how...” thành một câu riêng không có động từ chính (fragment).'),
            ('Missing Comma', 'century revealing — thiếu dấu phẩy khiến “revealing” bị hiểu nhầm là bổ nghĩa trực tiếp cho “the early nineteenth century”.'),
        ],
    ),
    20: meta(
        'Standard English Conventions', 'Boundaries', 'Medium', 'B',
        'Kiểm tra quan hệ nghĩa của hai mệnh đề độc lập: IC1 = “This has not always been the case, though” (“though” đặt cuối IC1 để tương phản với câu 1 rằng cực từ giữ nguyên vị trí suốt 20 triệu năm qua); IC2 = “throughout geologic history, Earth’s magnetic poles have swapped places several times...” (giải thích/minh chứng cho IC1 chứ KHÔNG tương phản với IC1!). Vì vậy dấu chấm phẩy phải đặt SAU từ “though” để gom “though” vào IC1 → “case, though;” → Chọn B.',
        'Mẹo vàng với trạng từ “though” đứng giữa 2 mệnh đề độc lập: luôn xác định “though” tạo sự tương phản với câu TRƯỚC đó (đặt `, though;`) hay tương phản giữa 2 vế cùng câu (đặt `; though,`).',
        [
            ('Comma Splice', 'case, though, — chỉ dùng dấu phẩy để nối hai mệnh đề độc lập (lỗi comma splice kinh điển).'),
            ('Đáp án đúng', 'case, though; — đưa “though” về cuối IC1 (tương phản với câu 1) rồi dùng dấu chấm phẩy tách rạch ròi sang IC2 giải thích cho IC1.'),
            ('Run-On Sentence', 'case, though — nếu dùng “though” làm liên từ phụ thuộc (“mặc dù cực từ đã đổi chỗ”) thì sai ngược logic nguyên nhân–minh chứng.'),
            ('Wrong Clause Placement', 'case; though, — đẩy “though” sang IC2 khiến nghĩa bị ngược (vế sau minh chứng cho vế trước chứ không đối lập với vế trước).'),
        ],
    ),
    21: meta(
        'Expression of Ideas', 'Transitions', 'Easy', 'B',
        'Câu trước nêu nhận định khái quát: “elephants were ranked higher than crocodiles” (voi được xếp hạng cao hơn cá sấu). Câu chứa chỗ trống cung cấp số liệu xếp hạng cụ thể cho nhận định đó: “elephants were ranked third, and crocodiles were ranked fifteenth” (voi xếp thứ 3, cá sấu xếp thứ 15). Từ nối chuyển từ khái quát sang chi tiết cụ thể là “Specifically,” → Chọn B.',
        'Khi câu trước nêu kết quả chung (“higher than”) và câu sau đưa ra con số chi tiết chứng minh (“third” và “fifteenth”), chọn ngay từ nối cụ thể hóa = Specifically.',
        [
            ('Wrong Relationship', 'Therefore, — chỉ quan hệ nguyên nhân–kết quả, nhưng việc voi xếp thứ 3 và cá sấu thứ 15 là chi tiết cụ thể hóa chứ không phải hệ quả sinh ra từ việc xếp cao hơn.'),
            ('Đáp án đúng', 'Specifically, — chính xác hoàn toàn: đi từ nhận định chung sang dữ liệu thứ hạng chi tiết (3 vs. 15).'),
            ('Wrong Relationship', 'On the other hand, — chỉ sự tương phản, sai hoàn toàn vì hai câu đồng hướng.'),
            ('Wrong Relationship', 'Later, — chỉ trình tự thời gian, không phù hợp vì đây là cùng một bảng xếp hạng.'),
        ],
    ),
    22: meta(
        'Expression of Ideas', 'Transitions', 'Easy', 'A',
        'Câu 1 cho thấy phương pháp cực kỳ thô sơ năm 1920: chỉ dùng một miếng bìa cứng cắt theo hình bang Montana và một sợi dây (“apparently crude technique”). Câu 2 nêu kết quả trái ngược kỳ vọng: kỹ thuật thô sơ đó lại cho ra con số gần chính xác đáng kinh ngạc (chỉ lệch 1 dặm so với máy tính gần 100 năm sau). Cần từ nối nhượng bộ/tương phản nhẹ → “Still,” (Tuy nhiên / Dù vậy) → Chọn A.',
        'Công thức SAT Transitions: phương pháp thô sơ (“cardboard cutout... string” / “apparently crude”) + kết quả lại chính xác bất ngờ (“relatively close approximation”) → luôn chọn từ nối tương phản/nhượng bộ (Still, Yet, Nevertheless).',
        [
            ('Đáp án đúng', 'Still, = Tuy vậy — diễn tả hoàn hảo sự đối lập giữa phương pháp tưởng chừng thô sơ và kết quả cực kỳ chính xác.'),
            ('Opposite Relationship', 'Fittingly, = Một cách hợp lý/đúng như mong đợi — trái ngược hoàn toàn vì kết quả chính xác là điều bất ngờ so với kỹ thuật thô sơ.'),
            ('Wrong Relationship', 'Similarly, = Tương tự — không có hai đối tượng/sự kiện song song để so sánh tương đồng.'),
            ('Wrong Relationship', 'In other words, = Nói cách khác — câu 2 nêu kết quả đối lập chứ không diễn giải lại câu 1.'),
        ],
    ),
    23: meta(
        'Expression of Ideas', 'Transitions', 'Easy', 'D',
        'Câu 1 nêu quy luật vật lý thiên văn: vòng mảnh vỡ nằm NGOÀI giới hạn Roche dự kiến sẽ kết tụ thành vệ tinh (mặt trăng) thay vì duy trì dạng vành đai. Câu 2 nêu một phát hiện ĐI NGƯỢC quy luật đó: Bruno Morgado và cộng sự lại phát hiện một vành đai đặc quanh Quaoar ở khoảng cách 2.500 dặm (vượt xa giới hạn Roche 1.100 dặm) mà vẫn còn nguyên vẹn! Quan hệ tương phản trực tiếp → “though,” → Chọn D.',
        'Khi câu 1 nêu quy luật dự đoán (“expected to... whereas... would likely...”) và câu 2 đưa ra ngoại lệ phá vỡ quy luật đó, hãy chọn ngay từ nối tương phản đặt giữa câu = though.',
        [
            ('Opposite Relationship', 'fittingly, = đúng như mong đợi — trái nghĩa vì phát hiện ở Quaoar đi ngược lý thuyết giới hạn Roche.'),
            ('Wrong Relationship', 'for example, = ví dụ — Quaoar là phản ví dụ (ngoại lệ), không phải ví dụ minh họa cho quy luật câu 1.'),
            ('Wrong Relationship', 'likewise, = tương tự — sai vì hai câu mang chiều hướng trái ngược nhau.'),
            ('Đáp án đúng', 'though, = tuy nhiên — diễn tả chính xác mối quan hệ tương phản giữa lý thuyết và phát hiện ngoại lệ ở Quaoar.'),
        ],
    ),
    24: meta(
        'Expression of Ideas', 'Rhetorical Synthesis', 'Medium', 'C',
        'Mục tiêu của học sinh gồm 2 yêu cầu rõ rệt: (1) sử dụng một câu trích dẫn (“use a quotation”) để (2) bác bỏ nhận định rằng các chương trình slow TV nhàm chán (“refute the claim that slow TV programs are boring”). Chỉ đáp án C thực hiện trọn vẹn cả hai: bác bỏ trực diện bằng cụm “Far from boring,” kết hợp trích dẫn lời khen của Heller “visceral kind of armchair tourism” → Chọn C.',
        'Trong câu hỏi Rhetorical Synthesis có động từ mạnh như “refute the claim that...”, đáp án đúng phải trực tiếp bác bỏ luận điểm đó (“Far from boring,”) chứ không chỉ nhắc trung lập hai chiều (như B) hay bỏ quên luận điểm cần bác bỏ (như A).',
        [
            ('Incomplete Goal', 'Có trích dẫn câu của Heller nhưng hoàn toàn không nhắc tới hay bác bỏ nhận định “slow TV programs are boring”.'),
            ('Neutral / Fails to Refute', 'Chỉ trình bày trung lập hai luồng ý kiến (“While some have praised..., others have called...”), không hề bác bỏ quan điểm cho rằng slow TV nhàm chán.'),
            ('Đáp án đúng', 'Bác bỏ trực diện (“Far from boring,”) và dùng chính xác trích dẫn ca ngợi của Heller (“visceral kind of armchair tourism”).'),
            ('Opposite Goal', 'Lại trích câu “the world’s most boring television” theo hướng đồng tình/củng cố thay vì bác bỏ nhận định.'),
        ],
    ),
    25: meta(
        'Expression of Ideas', 'Rhetorical Synthesis', 'Easy', 'D',
        'Mục tiêu của học sinh: đưa ra một VÍ DỤ về biệt danh của một mẫu hóa thạch khủng long (“provide an example of a dinosaur fossil specimen’s nickname”). Trong 4 lựa chọn, chỉ có đáp án D thực sự nêu ra tên biệt danh cụ thể là “Pops” (cùng danh tính mẫu hóa thạch <i>Triceratops</i> tại bảo tàng Denver) → Chọn D.',
        'Mẹo làm nhanh Rhetorical Synthesis: khi đề yêu cầu “provide an example of X (a nickname)”, quét nhanh xem lựa chọn nào THỰC SỰ chứa cái tên ví dụ cụ thể (“Pops”) — loại tức thì mọi câu nói chung chung.',
        [
            ('Missing Example', 'Chỉ nói chung chung có một mẫu vật ở Denver được đặt biệt danh mà không hề nêu tên biệt danh là gì.'),
            ('Missing Nickname', 'Nhắc tới mẫu hóa thạch <i>Triceratops</i> ở Denver nhưng hoàn toàn không nhắc đến biệt danh “Pops”.'),
            ('Too General', 'Chỉ nhắc lại nhận định chung rằng nhiều hóa thạch khủng long được đặt biệt danh, không có ví dụ cụ thể.'),
            ('Đáp án đúng', 'Nêu trực tiếp ví dụ cụ thể: “Pops” là biệt danh của mẫu hóa thạch <i>Triceratops</i> tại Bảo tàng Tự nhiên và Khoa học Denver.'),
        ],
    ),
    26: meta(
        'Expression of Ideas', 'Rhetorical Synthesis', 'Easy', 'D',
        'Mục tiêu của học sinh: chỉ rõ ĐỊA ĐIỂM nơi có thể nghe thấy một cảnh quan âm thanh mang ý nghĩa văn hóa đối với Nhật Bản (“specify where a soundscape... can be heard”). Chỉ có đáp án D nêu đầy đủ địa điểm cụ thể: cảng Hachinohe, tỉnh Aomori, phía bắc đảo Honshu, Nhật Bản → Chọn D.',
        'Đọc từ khóa hỏi mục tiêu (“specify where... can be heard”) và chọn ngay phương án duy nhất cung cấp tọa độ/địa danh cụ thể từ ghi chú.',
        [
            ('Missing Location', 'Chỉ nói âm thanh mòng biển đuôi đen có trong danh sách 100 cảnh quan âm thanh, không cho biết nghe ở đâu.'),
            ('Missing Location', 'Chỉ nêu cơ quan lựa chọn và tiêu chí ý nghĩa văn hóa, hoàn toàn thiếu địa điểm.'),
            ('Too Vague', 'Chỉ lặp lại định nghĩa “a specific place” chứ không nêu địa điểm cụ thể nào.'),
            ('Đáp án đúng', 'Chỉ rõ chính xác địa điểm có thể nghe cảnh quan âm thanh này: tại cảng Hachinohe ở tỉnh Aomori, phía bắc đảo Honshu, Nhật Bản.'),
        ],
    ),
    27: meta(
        'Expression of Ideas', 'Rhetorical Synthesis', 'Easy', 'C',
        'Mục tiêu của học sinh: nhấn mạnh một ĐIỂM KHÁC BIỆT giữa hai loài thực vật (“emphasize a difference between the two plants”). Theo ghi chú, <i>Ilex anomala</i> là loài bản địa (native), còn <i>Trema orientalis</i> là loài ngoại lai (non-native). Chỉ đáp án C nêu tên cả hai loài và làm nổi bật sự đối lập này bằng cấu trúc tương phản “Though..., only the former plant is native” → Chọn C.',
        'Với mục tiêu “emphasize a difference between the two X”, đáp án đúng BẮT BUỘC phải gọi tên cả hai đối tượng và dùng từ ngữ tương phản (Though, while, unlike, only the former...).',
        [
            ('Only One Plant', 'Chỉ nhắc đến <i>Trema orientalis</i>, hoàn toàn bỏ quên loài thứ hai nên không thể tạo sự so sánh khác biệt.'),
            ('Neither Plant', 'Chỉ tóm tắt mục đích nghiên cứu năm 2019, không hề nhắc tên hai loài thực vật.'),
            ('Đáp án đúng', 'Nêu đủ cả hai loài và nhấn mạnh sắc nét điểm khác biệt cốt lõi: chỉ loài đầu tiên (<i>Ilex anomala</i>) là loài bản địa.'),
            ('Similarity Trap', 'Nhấn mạnh điểm GIỐNG nhau (hạt của cả hai đều có trong mẫu phân chim) thay vì điểm khác biệt.'),
        ],
    ),
}

M1_BUILD_PATCHES = {
    1: {
        'questionHtml': 'Which choice completes the text with the most logical and precise word or phrase?',
        'options': ['outdated', 'varied', 'forgotten', 'lonely'],
    },
    2: {
        'questionHtml': 'Based on the text, when the narrator describes herself as “cheating,” what does she most likely mean?',
        'options': [
            'She was gaining an unfair advantage over other contestants in the talent show.',
            'She was lying to herself about her musical ability.',
            'She was deceiving her piano teacher.',
            'She was violating an expectation about how to perform the piece.',
        ],
    },
    3: {
        'questionHtml': 'Which choice completes the text with the most logical and precise word or phrase?',
        'options': ['contributions', 'resolutions', 'justifications', 'negotiations'],
    },
    4: {
        'questionHtml': 'Which choice completes the text with the most logical and precise word or phrase?',
        'options': ['intercede in', 'concur with', 'appeal to', 'amass in'],
    },
    7: {
        'questionHtml': 'According to the text, in which year was Adrastea discovered?',
        'options': ['1979', '1892', '2001', '1610'],
    },
    12: {
        'prependStimulusHtml': _svg_m1_q12_fta_exports(),
    },
    13: {
        'prependStimulusHtml': html_table(
            'Average Monetized Productivity Loss at Two Points After Programs Began, in Australian Dollars',
            ['Type of training', '12 weeks', '12 months'],
            [
                ['EET', '268', '171'],
                ['EHP', '282', '436'],
            ],
        ),
    },
    19: {
        'options': ['century: revealing', 'century, revealing', 'century. Revealing', 'century revealing'],
    },
    20: {
        'options': ['case, though,', 'case, though;', 'case, though', 'case; though,'],
    },
    22: {
        'questionHtml': 'Which choice completes the text with the most logical transition?',
        'options': ['Still,', 'Fittingly,', 'Similarly,', 'In other words,'],
    },
    23: {
        'questionHtml': 'Which choice completes the text with the most logical transition?',
        'options': ['fittingly,', 'for example,', 'likewise,', 'though,'],
    },
}

M1_POST_PATCHES = {
    1: {
        'stim_replace': [
            ('career. Cuban', 'career, Cuban'),
            ('Lrnesto', 'Ernesto'),
            ('how his body', 'how _______ his body'),
            ('Tecuona', 'Lecuona'),
            ('areas. from', 'areas, from'),
        ],
    },
    2: {
        'stim_replace': [
            ('Uirections ~~ WH ', ''),
            ("Amy Tan's 1989 novel The Joy Luck Club.", 'Amy Tan’s 1989 novel <i>The Joy Luck Club</i>.'),
            ('when she was a child. For the talent', 'when she was a child.||EXCERPT||For the talent'),
            ('“Pleading Child" from Schumann\'s Scenes from Childhood.', '“Pleading Child” from Schumann’s <i>Scenes from Childhood</i>.'),
            ('1t was a simple. moody', 'It was a simple, moody'),
            ('thing. playing', 'thing, playing'),
            ('then cheating. looking', 'then <u>cheating</u>, looking'),
            ('what 1 was', 'what I was'),
            ('else. about', 'else, about'),
            (' £1983 by Amy Tan', '||COPY||©1989 by Amy Tan'),
        ],
    },
    3: {
        'stim_replace': [
            ('sci fi', 'sci-fi'),
            ('libraries— that', 'libraries—_______ that'),
        ],
    },
    4: {
        'stim_replace': [
            ('industries an area', 'industries _______ an area'),
        ],
    },
    5: {
        'stim_replace': [
            ("Bram Stoker's 1911 novel The Lair of the White Worm.", 'Bram Stoker’s 1911 novel <i>The Lair of the White Worm</i>.'),
            ('at a port. The meeting', 'at a port.||EXCERPT||The meeting'),
            ('Adam. seeing', 'Adam, seeing'),
            ('ship. suggested', 'ship, suggested'),
            ('board. and', 'board, and'),
            ('invitation. and', 'invitation, and'),
            ('relationship. but', 'relationship, but'),
        ],
        'opt_replace': [
            ('1t showcases', 'It showcases'),
        ],
    },
    6: {
        'stim_replace': [
            ('Community science. which', 'Community science, which'),
            ('conununity', 'community'),
        ],
        'opt_replace': [
            ('importance. and', 'importance, and'),
            ('Tt argues', 'It argues'),
            ('collaboration. shows', 'collaboration, shows'),
            ('study. and', 'study, and'),
        ],
    },
    7: {
        'stim_replace': [
            ('Voyager 1', '<i>Voyager 1</i>'),
            ('Catuera', 'Camera'),
        ],
    },
    8: {
        'stim_replace': [
            ('1991. the Museo de.as', '1991, the Museo de Las'),
            ('4.800', '4,800'),
            ('L.A Plaza', 'LA Plaza'),
        ],
        'opt_replace': [
            ('more people,', 'more people.'),
            ('1.A Plaza', 'LA Plaza'),
        ],
    },
    9: {
        'stim_replace': [
            ('The Wonderful Wizard of Oz', '<i>The Wonderful Wizard of Oz</i>'),
            ('by 1.. Frank Baum.', 'by L. Frank Baum.'),
            ('novel. the', 'novel, the'),
            ('over time:', 'over time: _______'),
        ],
        'q_replace': [
            ('The Wonderful Wizard of Oz', '<i>The Wonderful Wizard of Oz</i>'),
        ],
        'opt_replace': [
            ('companions)', 'companions]'),
            ('mace entirely', 'made entirely'),
            ('chairs. and', 'chairs, and'),
            ('around. she', 'around, she'),
            ('painted. but', 'painted, but'),
            ('away. and', 'away, and'),
        ],
    },
    10: {
        'stim_replace': [
            ('& To help', 'To help'),
            ('Guoging', 'Guoqing'),
            ('trap. making', 'trap, making'),
            ('applications, Chemist', 'applications. Chemist'),
            ('Adlhart. however. claims', 'Adlhart, however, claims'),
            ('mass-produce,', 'mass-produce.'),
        ],
        'q_replace': [
            ('finding. if true.', 'finding, if true,'),
        ],
        'opt_replace': [
            ('volume. making', 'volume, making'),
            ('liguid', 'liquid'),
            ("teanv's", "team's"),
            ('industry. so', 'industry, so'),
        ],
    },
    11: {
        'stim_replace': [
            ('Life Among the Paintes', '<i>Life Among the Paiutes</i>'),
            ('by sarah ‘Winnemucca Hopkins. a', 'by Sarah Winnemucca Hopkins, a'),
            ('educator. and', 'educator, and'),
            ('customs. writing,', 'customs, writing _______'),
        ],
        'q_replace': [
            ('Life Among the Paiutes', '<i>Life Among the Paiutes</i>'),
        ],
        'opt_replace': [
            ('day. and', 'day, and'),
            ('left. for', 'left, for'),
            ('goed people', 'good people'),
        ],
    },
    12: {
        'stim_replace': [
            (
                'Average Total Agricultural Export Growth Rate, Five Years Pre- and Post-FTA with the United States Zw H Pre-FTA Post-FTA Export growth B Canada (NAFTA) O Costa Rica (CAFTA-DR) BW Mexico (NAFTA) ',
                '',
            ),
            ('agreements (FTAs) agreements', 'agreements (FTAs)—agreements'),
            (
                'experience A',
                'experience changes in total agricultural exports, economist Kayode Ajewole and colleagues calculated average export growth rates for several countries over the five years before and the five years after entering into an FTA with the United States. Examining the graph, a student claims that entering into an FTA with the United States increases a country’s average total agricultural export growth rate.',
            ),
        ],
    },
    13: {
        'stim_replace': [
            ('Average Monetized Productivity Loss at Two Points After Programs Began. in Australian Dollars Tope often ', ''),
        ],
        'opt_replace': [
            ('began. while', 'began, while'),
            ('for the ELT and', 'for the EET and'),
            ('began. but', 'began, but'),
        ],
    },
    14: {
        'stim_replace': [
            ('1917. artist', '1917, artist'),
            ('nueva cancion chilena', '<i>nueva canción chilena</i>'),
            ('Portugal. and', 'Portugal, and'),
            ('nueva cancion.', '<i>nueva canción</i>.'),
            ('moclern', 'modern'),
            (
                'As the movement spread beyond Chile. f musi es cated into {ts f. expanded,',
                '<u>As the movement spread beyond Chile, the breadth of musical traditions incorporated into its foundation also expanded.</u>',
            ),
        ],
        'q_replace': [
            ('neva cancion.', '<i>nueva canción</i>,'),
        ],
        'opt_replace': [
            ('the quena. a', 'the <i>quena</i>, a'),
            ('of corrido,', 'of <i>corrido</i>,'),
            ('soon after,', 'soon after.'),
        ],
    },
    15: {
        'stim_replace': [
            ('Serrallés. a', 'Serrallés, a'),
            ('Rico. is', 'Rico, is'),
            ('museums visitors', 'museums _______ visitors'),
        ],
    },
    16: {
        'stim_replace': [
            ('Snowy Landscape with the Old Tower', '<i>Snowy Landscape with the Old Tower</i>'),
            ('Van Gogh in', 'Van Gogh _______ in'),
        ],
    },
    17: {
        'stim_replace': [
            ('Kizomba. a', 'Kizomba, a'),
            ('international 2022', 'international _______ 2022'),
        ],
    },
    18: {
        'stim_replace': [
            ('Chapter. which', 'Chapter, which'),
            ('201.000 acres.', '201,000 acres,'),
            ('Navajo Diné bizaad', 'Navajo _______ <i>Diné bizaad</i>'),
            ('language).', 'language),'),
            ('Tsé Nikdni', '<i>Tsé Nikání</i>'),
        ],
    },
    19: {
        'stim_replace': [
            ('Without a Whisper—Konnon:Kwe', '<i>Without a Whisper—Konnon:Kwe</i>'),
            ('Haudenosaunece', 'Haudenosaunee'),
            ('nineteenth Tow', 'nineteenth _______ how'),
            ('in the US,', 'in the US.'),
        ],
    },
    20: {
        'stim_replace': [
            ('been the throughout', 'been the _______ throughout'),
            ('history. Earth', 'history, Earth'),
        ],
    },
    21: {
        'stim_replace': [
            ('ee B= As part of a study.', 'As part of a study,'),
            ('“charismatic.”', '“charismatic,”'),
            ('“attractive. fascinating.', '“attractive, fascinating,'),
            ('crocodiles. elephants', 'crocodiles. _______ elephants'),
            ('third. and', 'third, and'),
        ],
        'opt_replace': [
            ('Specifically.', 'Specifically,'),
            ('hand.', 'hand,'),
        ],
    },
    22: {
        'stim_replace': [
            ('1920. the', '1920, the'),
            ('string. this', 'string. _______ this'),
        ],
    },
    23: {
        'stim_replace': [
            ('{e.g..', '(e.g.,'),
            ('colleagues, detected', 'colleagues, _______ detected'),
            ('intact,', 'intact.'),
        ],
    },
    24: {
        'stim_replace': [
            ('‘While researching', 'While researching'),
            ('notes: + Documentary', 'notes:||BULLET||Documentary'),
            ('real time, * MORA: Zeichner', 'real time.||BULLET||<i>MORA: Zeichner</i>'),
            ('program. « The', 'program.||BULLET||The'),
            ('journey. « It', 'journey.||BULLET||It'),
            ('2016. « Slow TV has been called the world\'s', '2016.||BULLET||Slow TV has been called “the world’s'),
            ('television.” + American', 'television.”||BULLET||American'),
            ('that -it affords', 'that “it affords'),
        ],
        'opt_replace': [
            ('MORA: Zeichner', '<i>MORA: Zeichner</i>'),
            ('tourism.” as', 'tourism,” as'),
            ('"a visceral', '“a visceral'),
            ('tourism.” others', 'tourism,” others'),
            ('"visceral', '“visceral'),
            ('puts it. whereby', 'puts it, whereby'),
            ('atwork', 'at work'),
            ('at work. occurring', 'at work, occurring'),
        ],
    },
    25: {
        'stim_replace': [
            ('‘While researching a topic. a', 'While researching a topic, a'),
            ('notes: « Dinosaur', 'notes:||BULLET||Dinosaur'),
            ('world, * Many', 'world.||BULLET||Many'),
            ('nicknames, + The', 'nicknames.||BULLET||The'),
            ('Pops. « Popslived', 'Pops.||BULLET||Pops lived'),
            ('ago. « Itis a member of the genus Triceratops.', 'ago.||BULLET||It is a member of the genus <i>Triceratops</i>.'),
        ],
        'opt_replace': [
            ('specimens. including', 'specimens, including'),
            ('Denver. Colorado.', 'Denver, Colorado.'),
            ('Triceratops', '<i>Triceratops</i>'),
            ('period. which', 'period, which'),
        ],
    },
    26: {
        'stim_replace': [
            ('topic. a', 'topic, a'),
            ('notes: + A soundscape', 'notes:||BULLET||A soundscape'),
            ('place. + The Japanese', 'place.||BULLET||The Japanese'),
            ('Japan. + Each', 'Japan.||BULLET||Each'),
            ('Japan. * The sound', 'Japan.||BULLET||The sound'),
            ('list. + Aomori', 'list.||BULLET||Aomori'),
            ('Island. Japan.', 'Island, Japan.'),
        ],
    },
    27: {
        'stim_replace': [
            ('‘While researching', 'While researching'),
            ('notes: + Most', 'notes:||BULLET||Most'),
            ('non-native. + Ina 2019 study. researchers', 'non-native.||BULLET||In a 2019 study, researchers'),
            ('Oahu. * Researchers', 'Oahu.||BULLET||Researchers'),
            ('birds. * Illex anomala. a flowering shrub. was', 'birds.||BULLET||<i>Ilex anomala</i>, a flowering shrub, was'),
            ('catalogued. + Trema orientalis. a tree. was', 'catalogued.||BULLET||<i>Trema orientalis</i>, a tree, was'),
            ('catalogued. + Researchers', 'catalogued.||BULLET||Researchers'),
            ('non native', 'non-native'),
        ],
        'q_replace': [
            ('two plants, Which', 'two plants. Which'),
        ],
        'opt_replace': [
            ('Trema orientalis.', 'Trema orientalis,'),
            ('Trema orientalis', '<i>Trema orientalis</i>'),
            ('Ilex anomala', '<i>Ilex anomala</i>'),
            ('Oahu. Hawaii. to', 'Oahu, Hawaii, to'),
            ('can bath be', 'can both be'),
            ('birds. according', 'birds, according'),
        ],
    },
}


# ============================================================================
# MODULE 2: METADATA, 2-PASS AUDITED ANSWERS, VIETNAMESE EXPLANATIONS & PATCHES
# ============================================================================

M2_META = {
    1: meta(
        'Craft and Structure', 'Words in Context', 'Easy', 'C',
        'Câu 1 nói giải Nobel Hóa học thường trao cho MỘT người (“given to a single person”). Câu 2 mở đầu bằng từ nối tương phản “But” cho trường hợp Ủy ban Nobel muốn vinh danh công trình của HAI hoặc BA cá nhân — tức giải thưởng được trao ĐỒNG THỜI/CHUNG cho họ → “jointly” → Chọn C.',
        'Nhận diện cặp tương phản trực tiếp: “given to a single person” (một người) vs. “two or three individuals” (nhiều người) → trạng từ chính xác là “jointly” (chung, cùng nhau).',
        [
            ('Wrong Meaning', 'retroactively = có hiệu lực hồi tố về quá khứ — không liên quan đến số lượng người nhận giải.'),
            ('Wrong Meaning', 'ceremoniously = một cách trang trọng, nghi lễ — không tạo đối lập với việc trao cho một cá nhân.'),
            ('Đáp án đúng', 'jointly = chung, đồng trao giải — đối lập chuẩn xác với “given to a single person”.'),
            ('Wrong Meaning', 'reluctantly = miễn cưỡng — sai hoàn toàn sắc thái ngữ cảnh.'),
        ],
    ),
    2: meta(
        'Craft and Structure', 'Words in Context', 'Easy', 'D',
        'Dấu hai chấm định nghĩa trực tiếp từ cần điền: “it is a constantly evolving network of channels and strips of land that change in size and shape” (mạng lưới kênh rạch và dải đất không ngừng biến đổi về kích thước và hình dạng). Từ mang nghĩa “năng động, luôn vận động biến đổi” là “dynamic” → Chọn D.',
        'Gặp dấu hai chấm (:) kèm cụm “constantly evolving... change in size and shape”, chọn ngay tính từ “dynamic” và tránh bẫy từ trái nghĩa “immutable” (bất biến).',
        [
            ('Wrong Meaning', 'sustainable = bền vững — không đồng nghĩa với việc liên tục thay đổi hình dạng, kích thước.'),
            ('Wrong Meaning', 'unrivaled = không đối thủ — sai nghĩa, bài còn mở đầu bằng “As with other river deltas” (cũng giống các châu thổ khác).'),
            ('Antonym Trap', 'immutable = bất biến, không thay đổi — hoàn toàn trái nghĩa với “constantly evolving”.'),
            ('Đáp án đúng', 'dynamic = năng động, biến đổi không ngừng — khớp 100% với phần định nghĩa sau dấu hai chấm.'),
        ],
    ),
    3: meta(
        'Craft and Structure', 'Words in Context', 'Medium', 'D',
        'Có hai manh mối song song: (1) mệnh đề tương phản “While his contemporaries’ approaches... were often sentimental” (trong khi các họa sĩ cùng thời thường ủy mị/giàu cảm tính → Whistler phải trái ngược: lạnh lùng, không bị cảm xúc chi phối); (2) câu kế tiếp ví ông với nhiếp ảnh gia Walker Evans — người tạo ra “objective documentations of life” (tư liệu khách quan). Từ khớp cả hai manh mối là “dispassionate” (khách quan, không thiên cảm xúc) → Chọn D.',
        'Khi thấy “While A was sentimental, B seemed ___” đi kèm cụm “objective documentations”, chọn ngay từ đồng nghĩa với “objective / unemotional” = dispassionate.',
        [
            ('Off-Target', 'tranquil = yên bình, tĩnh lặng — không tạo đối lập chuẩn với “sentimental” và không đồng nghĩa với “objective”.'),
            ('Wrong Meaning', 'peculiar = kỳ lạ, khác thường — không ăn khớp với phong cách ghi chép khách quan của Walker Evans.'),
            ('Opposite Tone', 'nostalgic = hoài niệm — cùng trường nghĩa cảm tính với “sentimental”, trái ngược với điều cần tương phản.'),
            ('Đáp án đúng', 'dispassionate = khách quan, không bị cảm xúc chi phối — đối lập hoàn hảo với “sentimental” và khớp với “objective”.'),
        ],
    ),
    4: meta(
        'Craft and Structure', 'Text Structure and Purpose', 'Medium', 'C',
        'Câu 1 trình bày đánh giá tốt đẹp mà mọi người dành cho mục sư Mr. Ely: giáo dân xem ông là người tài năng, uyên bác, còn đồng nghiệp xem ông là người kín đáo, dễ mến (“favorable opinion”). Câu 2 liệt kê hàng loạt cách ứng xử khôn khéo của ông (không bao giờ tranh luận gay gắt, hiếm khi nói thẳng suy nghĩ, không để lộ vẻ cười nhạo ai và không tạo cơ hội để ai cười mình) — chính những hành vi giúp ông giữ vững thiện cảm đó → Chọn C.',
        'Đọc cấu trúc 2 câu của đoạn văn học: Câu 1 = Ấn tượng tốt đẹp người khác dành cho nhân vật → Câu 2 = Các hành vi khéo léo giúp nhân vật duy trì ấn tượng đó.',
        [
            ('Unsupported Twist', 'Bài không hề nói quan điểm của đồng nghiệp về Mr. Ely bắt đầu thay đổi.'),
            ('Unsupported Comparison', 'Bài không so sánh mức độ ngây thơ giữa hàng xóm ở Milby với người dân ở London.'),
            ('Đáp án đúng', 'Khớp hoàn toàn 2 chặng của đoạn trích: nêu cái nhìn thiện cảm của mọi người rồi mô tả những hành vi giúp Mr. Ely bảo toàn thiện cảm ấy.'),
            ('Unsupported Detail', 'Bài không mô tả hành vi riêng tư (private behavior) và cũng không giải thích lý do sâu xa vì sao ông che giấu bản thân.'),
        ],
    ),
    5: meta(
        'Craft and Structure', 'Text Structure and Purpose', 'Medium', 'D',
        'Theo sát trình tự 3 câu trong bài: Câu 1 đưa ra nhận định tổng quát về sự nghiệp của kiến trúc sư Luis Barragán (trải qua nhiều giai đoạn khác biệt); Câu 2 nêu rõ bước chuyển phong cách sang chủ nghĩa hiện đại sau chuyến đi Mỹ và châu Âu đầu thập niên 1930 (như ở Pizarro Suárez House); Câu 3 phân tích cụ thể bước chuyển ấy thể hiện ra sao qua tác phẩm (hình khối hình học tối giản tương phản với phong cách truyền thống trước đó ở Guadalajara) → Chọn D.',
        'Cẩn thận bẫy ĐẢO THỨ TỰ ở đáp án B! Bài viết giới thiệu bước chuyển sang hiện đại ở câu 2 TRƯỚC rồi mới đối chiếu với giai đoạn đầu ở câu 3, chứ không kể giai đoạn đầu trước rồi mới nói bước chuyển.',
        [
            ('Unsupported Ending', 'Câu cuối không nhấn mạnh tầm ảnh hưởng của sự nghiệp Barragán mà so sánh phong cách hiện đại với công trình thời kỳ đầu của chính ông.'),
            ('Reversed Order Trap', 'Đảo ngược trình tự bài đọc: bài nêu bước chuyển sang chủ nghĩa hiện đại trước (câu 2), rồi mới đối chiếu với các dự án thời đầu (câu 3).'),
            ('Wrong Comparison', 'So sánh với “các kiến trúc sư đi trước” là sai — bài so sánh với chính các công trình thời kỳ đầu của Barragán (“his earlier projects”).'),
            ('Đáp án đúng', 'Khớp hoàn hảo cả 3 câu: nhận định chung về sự nghiệp → nhấn mạnh bước chuyển phong cách → phân tích rõ bước chuyển đó qua tác phẩm.'),
        ],
    ),
    6: meta(
        'Craft and Structure', 'Text Structure and Purpose', 'Medium', 'D',
        'Phân tích cấu trúc từng câu: Câu 1 giới thiệu nghiên cứu/mô hình máy tính của nhóm Hidalgo, Castañer và Sevtsuk về các khu dân cư đô thị; Câu 2 mô tả một khía cạnh phương pháp luận của nghiên cứu (dùng thuật toán phân cụm để xác định ranh giới khu dân cư vốn mang tính chủ quan); Câu 3 nêu ứng dụng tiềm năng của mô hình (“invaluable in determining the optimal mix of a city’s amenities”) → Chọn D.',
        'Chia cấu trúc đoạn khoa học thành 3 phần quen thuộc: (1) Giới thiệu nghiên cứu → (2) Phương pháp (methodology: clustering algorithm) → (3) Ứng dụng tiềm năng (application).',
        [
            ('Factual Distortion', 'Mô hình dự đoán cơ cấu loại hình kinh doanh (“mix of... businesses”), không phải dự đoán sự thành công (“success”), và bài không nhắc đến lĩnh vực khác (“other fields”).'),
            ('Missing Elements', 'Bài không giải thích vì sao các nhà quy hoạch đô thị quan tâm và cũng không trình bày một kết quả nghiên cứu cụ thể (“one key finding”).'),
            ('Unsupported Opening', 'Câu 1 không tóm tắt các xu hướng phát triển đô thị gần đây mà giới thiệu thẳng mô hình nghiên cứu của nhóm tác giả.'),
            ('Đáp án đúng', 'Tóm lược chuẩn xác cả 3 chặng: giới thiệu nghiên cứu khu phố đô thị → mô tả phương pháp thuật toán → gợi mở ứng dụng thực tiễn.'),
        ],
    ),
    7: meta(
        'Craft and Structure', 'Cross-Text Connections', 'Hard', 'C',
        'Text 1: Vùng có thể sống được (HZ — cho phép tồn tại nước lỏng trên bề mặt) ban đầu được tính bắt đầu từ khoảng 1 AU, và Madhusudhan et al. xếp K2-18 b vào nhóm ứng viên hycean vì nó nằm ngay rìa trong của HZ (~1 AU). Text 2: Tsai et al. chỉ ra khí quyển giàu hydro của K2-18 b hấp thụ ánh sáng gây tăng nhiệt độ bề mặt và tăng bốc hơi nước, đẩy rìa trong của HZ ra xa tới 3,85 AU. Như vậy ở khoảng cách ~1 AU (quá gần ngôi sao!), khí quyển giàu hydro khiến bề mặt K2-18 b khó có thể giữ được nước lỏng → Chọn C.',
        'Trong bài Cross-Text khoa học có số liệu khoảng cách (1 AU → 3,85 AU), hãy vẽ nhanh trục số: rìa trong đẩy ra xa hơn (3,85 AU) nghĩa là hành tinh ở 1 AU đang QUÁ GẦN (quá nóng, nước bốc hơi hết), tuyệt đối tránh bẫy đảo chiều “too far” (A) và “too high” (B).',
        [
            ('Reversed Direction Trap', 'Ngược hoàn toàn: đẩy rìa trong HZ từ 1 AU ra 3,85 AU nghĩa là K2-18 b nằm QUÁ GẦN ngôi sao chủ (quá nóng), không phải “too far”.'),
            ('Reversed Direction Trap', 'Ngược hoàn toàn: mô hình cũ đánh giá nhiệt độ bề mặt quá THẤP (chứ không phải “too high”), nên mới tưởng 1 AU đã đủ mát để giữ nước lỏng.'),
            ('Đáp án đúng', 'Khớp 100% lập luận Text 2: thành phần hóa học khí quyển giàu hydro của K2-18 b gây tăng nhiệt và bốc hơi mạnh, khiến bề mặt khó giữ được nước lỏng ở khoảng cách ~1 AU.'),
            ('Unsupported Comparison', 'Text 2 không hề khẳng định đa số các loại hành tinh giàu hydro khác nằm trong vùng HZ.'),
        ],
    ),
    8: meta(
        'Information and Ideas', 'Central Ideas and Details', 'Medium', 'B',
        'Nội dung cốt lõi của đoạn văn: khi nhà văn Kenya Ngũgĩ wa Thiong’o chuyển sang viết bằng tiếng mẹ đẻ Gĩkũyũ vào thập niên 1970, nhiều đồng nghiệp và nhà phê bình tỏ ra hoài nghi/cảnh báo rằng tác phẩm sẽ khó tiếp cận ra ngoài cộng đồng; bất chấp sự hoài nghi đó, ông vẫn sáng tác hàng chục tác phẩm tiếng Gĩkũyũ được ca ngợi và dịch ra hơn 30 ngôn ngữ (thành công rực rỡ) → Chọn B.',
        'Với câu hỏi Main Idea, luôn nắm trục tương phản chính của đoạn: gặp hoài nghi/cảnh báo (“cautioned”) → nhưng vẫn gặt hái thành công văn chương (“dozens of acclaimed works... translated into more than thirty languages”).',
        [
            ('Factual Distortion', 'Sai chi tiết: bài nêu rõ ông đã xuất bản 4 tiểu thuyết đầu bằng tiếng Anh (“previously published four novels in English”), không phải “his first works in Gĩkũyũ”.'),
            ('Đáp án đúng', 'Tóm gọn hoàn hảo ý chính: quyết định viết bằng tiếng Gĩkũyũ vấp phải sự hoài nghi nhưng không hề ngăn cản ông đạt thành công văn chương.'),
            ('Wrong Language Swap', 'Tráo đổi ngôn ngữ: ngôn ngữ được giới phê bình khuyên dùng vì phổ biến rộng rãi là tiếng Kiswahili, KHÔNG phải Gĩkũyũ.'),
            ('Overgeneralization', 'Tự suy diễn thành tuyên ngôn chung cho mọi nhà văn (“literature ought to be written in authors’ native languages”) và bỏ mất trọng tâm về sự hoài nghi vs. thành công.'),
        ],
    ),
    9: meta(
        'Information and Ideas', 'Central Ideas and Details', 'Medium', 'B',
        'Nghiên cứu của Moran, Rodriguez và cộng sự phát hiện tỷ lệ cư dân dùng công viên ở Quito (82,9%) cao hơn Buenos Aires (69,9%), nhưng tỷ lệ người dân Quito báo cáo có các tiện ích mong muốn gần công viên lại thấp hơn nhiều so với Buenos Aires. Kết luận chính ở câu cuối: sự chênh lệch tỷ lệ sử dụng công viên KHÔNG thể giải thích bằng việc cư dân Quito có nhiều tiện ích ngoài công viên gần đó hơn → Chọn B.',
        'Khi câu cuối bắt đầu bằng “Given that..., [Conclusion]”, câu đó gần như luôn nắm giữ Main Idea của toàn đoạn — chỉ cần tìm phương án diễn đạt lại trung thành nhất mà không bịa thêm nguyên nhân.',
        [
            ('Unsupported Extrapolation', 'Bài không hề dự đoán rằng việc xây thêm tiện ích sẽ giúp tăng lượng người dùng công viên ở Quito mà không tăng ở Buenos Aires.'),
            ('Đáp án đúng', 'Diễn đạt lại chính xác 100% kết luận của đoạn văn: tỷ lệ dùng công viên ở Quito cao hơn Buenos Aires, nhưng điều đó không phải do tiếp cận nhiều tiện ích gần công viên hơn.'),
            ('Unsupported Comparison', 'Bài không hề nói Quito có “nhiều tiện ích tổng thể hơn” (more amenities overall) so với Buenos Aires.'),
            ('Unsupported Cause', 'Bài không hề đề cập đến mật độ hay số lượng công viên (“greater prevalence of parks”) ở Quito.'),
        ],
    ),
    10: meta(
        'Information and Ideas', 'Command of Evidence', 'Hard', 'D',
        'Đoạn văn nêu cảnh báo của các nhà nghiên cứu: dù cỏ widgeon phát triển mạnh kéo tổng diện tích cỏ biển tăng lên (từ ~19.500 lên ~44.000 ha giai đoạn 2012–2018), điều đó không đồng nghĩa hệ sinh thái cỏ biển vững vàng hơn trước các cú sốc môi trường (“environmental shocks”). Trên biểu đồ, năm 2019 cả 3 đường (eelgrass, widgeon grass và tổng tất cả các loài) đều SỤT GIẢM ĐỘT NGỘT! Phương án D giải thích hoàn hảo cú sụt giảm diện rộng năm 2019 (mưa lớn đầu 2019 rửa trôi dưỡng chất gây tảo nở hoa chặn ánh sáng của nhiều loài cỏ biển) và minh họa trực tiếp lời cảnh báo về tính dễ tổn thương trước cú sốc môi trường → Chọn D.',
        'Luôn kết hợp 2 điều kiện trong đề: (1) khớp cú rơi thẳng đứng của CẢ 3 đường vào năm 2019 trên đồ thị VÀ (2) minh họa cảnh báo hệ sinh thái vẫn dễ tổn thương trước “environmental shocks”.',
        [
            ('Wrong Year & Scope', 'Sai cả năm lẫn dữ liệu: năm 2018 eelgrass và tổng diện tích đều TĂNG (chứ không giảm), và cú rơi năm 2019 còn ảnh hưởng cả các loài cỏ biển khác (tổng giảm ~17.200 ha, lớn hơn mức giảm gộp ~12.200 ha của widgeon + eelgrass).'),
            ('Contradicts Graph', 'Sai dữ liệu: nếu widgeon grass chịu được đợt tăng nhiệt đầu 2019 thì đường widgeon grass đã không lao dốc gần một nửa (từ ~16.200 xuống ~8.600 ha) trong năm 2019!'),
            ('Misses Researchers’ Point', 'Chỉ mô tả xu hướng tăng giai đoạn 2012–2017, hoàn toàn bỏ qua cú sụt năm 2019 và không minh họa cảnh báo về cú sốc môi trường.'),
            ('Đáp án đúng', 'Giải thích chính xác cú lao dốc đồng loạt năm 2019 của nhiều loài cỏ biển (tảo nở hoa chặn ánh sáng do mưa lớn bất thường) và minh họa hoàn hảo điểm dễ tổn thương trước cú sốc môi trường.'),
        ],
    ),
    11: meta(
        'Information and Ideas', 'Command of Evidence', 'Hard', 'C',
        'Đọc thật kỹ nhận định duy nhất của đoạn văn về thiết bị liên lạc không dây (“the text’s claim about wireless communication devices”): việc cung cấp tải năng lượng ỔN ĐỊNH (“steady energy loads”) là điều kiện tiên quyết tuyệt đối (“an absolute prerequisite”) để các thiết bị liên lạc không dây có thể vận hành bằng năng lượng áp điện. Nếu phát hiện cho thấy nguồn điện chập chờn hoặc khó đoán (“Intermittent or unpredictable electrical supply” = KHÔNG ổn định) làm suy giảm hiệu quả của thiết bị liên lạc không dây (C), thì nhận định “nguồn năng lượng ổn định là điều kiện tiên quyết” được chứng minh trực tiếp → Chọn C.',
        'Cảnh giác bẫy ghép từ khóa ở câu A! Xác định ĐÚNG mệnh đề là nhận định về “wireless communication devices” (“steady energy loads... an absolute prerequisite”) rồi tìm phương án diễn đạt ý đảo tương đương (“Intermittent/unpredictable supply undermines efficacy”).',
        [
            ('Keyword Salad Trap', 'Ghép nhặt từ “high conductivity” + “CFRP” + “sufficient”, nhưng văn bản không hề khẳng định độ dẫn điện cao tạo ra công suất “đủ lớn” — nhận định về thiết bị không dây nằm ở yêu cầu “steady energy loads” (ổn định).'),
            ('Undermines Claim', 'Nói điện cực CFRP không tương thích với phần lớn thiết bị không dây — làm suy yếu thay vì ủng hộ nhận định.'),
            ('Đáp án đúng', 'Chứng minh trực tiếp vì sao “steady energy loads” là điều kiện tiên quyết tuyệt đối: nếu nguồn điện chập chờn/không ổn định thì thiết bị liên lạc không dây mất hiệu quả.'),
            ('Contradicts Text', 'Nói có thể cấp nguồn bằng bộ thu áp điện không dùng CFRP — đi ngược trọng tâm về vai trò cung cấp dòng ổn định của thiết kế mới.'),
        ],
    ),
    12: meta(
        'Information and Ideas', 'Inferences', 'Hard', 'D',
        'Chuỗi lập luận của bài: (1) Các nhà sinh thái học rút ra phần lớn hiểu biết về sự suy giảm của ong hoang dã từ ong nghệ (bumblebees) vì chúng được nghiên cứu nhiều nhất; (2) Tuy nhiên, Ghisbain chỉ ra ong nghệ thuộc số ÍT chi ong hoang dã có tập tính xã hội và chế độ ăn đa dạng — hai đặc điểm giúp tăng sức chống chịu trước một số biến đổi môi trường. Suy luận hợp lý: vì phản ứng của ong nghệ và các loài ong hoang dã khác trước mối đe dọa môi trường không phải lúc nào cũng tương đồng, các nhà nghiên cứu cần thận trọng khi suy rộng dữ liệu suy giảm ong hoang dã từ ong nghệ → Chọn D.',
        'Với bài Inferences dạng “nhà khoa học dựa vào mẫu A để suy ra cả nhóm B, nhưng A lại có đặc điểm hiếm giúp chống chịu tốt hơn”, kết luận chuẩn SAT luôn mang giọng điệu chừng mực: “cần thận trọng khi ngoại suy từ A sang B” (exercise caution when extrapolating).',
        [
            ('Ignores Main Setup', 'Bỏ qua hoàn toàn mạch lập luận về việc ngoại suy nghiên cứu từ ong nghệ, đồng thời suy diễn quá đà về tương lai dù câu 1 nêu rõ ong nghệ vẫn đang suy giảm quần thể.'),
            ('Too Extreme Trap', 'Cực đoan hóa vô lý ở vế cuối (“even ones with feeding patterns and levels of sociability that are similar”) — với loài có cùng đặc điểm tương đồng thì lập luận của Ghisbain không phủ định.'),
            ('Unsupported Comparison', 'Tự bịa sự so sánh giữa nguy cơ từ biến đổi khí hậu so với phá hủy môi trường sống (bài liệt kê cả hai ngang hàng).'),
            ('Đáp án đúng', 'Tổng hợp trọn vẹn tiền đề và kết luận chừng mực chuẩn xác: vì phản ứng không luôn tương đồng nên cần thận trọng khi suy rộng từ ong nghệ sang các loài ong hoang dã khác.'),
        ],
    ),
    13: meta(
        'Information and Ideas', 'Inferences', 'Hard', 'C',
        'Nút thắt trong pin nhiên liệu vi sinh (MFC): electron phải đi qua chuỗi phản ứng oxy hóa–khử (redox) KÉM HIỆU QUẢ để tới điện cực ngoài, khiến công suất hiếm khi vượt 0,30 mW/cm². Khi thêm hạt nano bạc (silver nanoparticles), công suất tăng hơn gấp đôi lên 0,66 mW/cm². Manh mối quyết định: “Since metals such as silver exhibit high electrical conductivity” (vì kim loại như bạc có độ dẫn điện rất cao) → giả thuyết hợp lý nhất là hạt nano bạc giúp dẫn electron ĐI TẮT bỏ qua chuỗi phản ứng redox kém hiệu quả và truyền thẳng tới điện cực → Chọn C.',
        'Trong câu hỏi Inferences khoa học có câu dẫn “Since [tính chất X], the researchers hypothesized that ___”, đáp án đúng PHẢI kết nối trực tiếp tính chất X (“high electrical conductivity” = dẫn điện tốt) với nút thắt đã nêu ở đầu bài (“inefficient redox reactions”).',
        [
            ('Wrong Mechanism', 'Gán nguyên nhân cho việc tăng tốc độ trao đổi chất của vi khuẩn — không hề liên quan đến gợi ý “high electrical conductivity” (độ dẫn điện cao) của bạc.'),
            ('Contradicts Experiment', 'Nói phản ứng tăng tốc “độc lập với sự hiện diện của hạt nano bạc” — mâu thuẫn thẳng với kết quả thí nghiệm thêm bạc và gợi ý về độ dẫn điện của bạc.'),
            ('Đáp án đúng', 'Nối khít nút thắt ban đầu (chuỗi redox kém hiệu quả) với tính dẫn điện cao của bạc: electron đi tắt bỏ qua chuỗi redox để truyền trực tiếp tới điện cực.'),
            ('Illogical Sequence', 'Vô lý về trình tự: nếu electron đã được dẫn thẳng tới điện cực rồi thì sau đó hạt nano bạc còn xúc tác phản ứng redox để làm gì?'),
        ],
    ),
    14: meta(
        'Information and Ideas', 'Inferences', 'Hard', 'A',
        'Chuỗi lập luận của bài: (1) Tỷ lệ mol khí metan ảnh hưởng trực tiếp tới lượng mưa và độ ẩm; (2) Dữ liệu quan sát thực tế trên mặt trăng Titan quá thưa thớt và mâu thuẫn nên không xác định rõ được biên độ tỷ lệ mol metan ở các tầng khí quyển; (3) Mô hình IPSL xử lý khó khăn này bằng cách gán một giá trị ĐỒNG NHẤT (uniform) cho tầng thấp nhất. Hệ quả tất yếu cần lưu ý: vì mô hình dùng một giả định đồng nhất đơn giản hóa thay vì dữ liệu thực tế vốn chưa xác định/biến thiên, nên việc có một số sai lệch giữa mô phỏng lượng mưa/độ ẩm của mô hình với thực tế trên Titan là điều hoàn toàn có thể dự kiến trước → Chọn A.',
        'Khi một mô hình khoa học buộc phải dùng tham số đơn giản hóa (“prescribing a uniform value”) cho biến số quyết định kết quả X (“influences precipitation and humidity”), kết luận logic nhất luôn là: sai lệch nhất định giữa mô phỏng X và thực tế X là điều dễ hiểu/được dự kiến.',
        [
            ('Đáp án đúng', 'Suy luận chừng mực, bám sát 100% logic bài: vì tham số metan đầu vào bị giả định đồng nhất nên một số sai khác giữa mô phỏng và thực tế về mưa/độ ẩm là điều có thể dự kiến.'),
            ('Unsupported Direction', 'Dữ liệu thưa thớt và mâu thuẫn không hề cho thấy giá trị thực tế trên Titan “cao hơn” (higher) giá trị trong mô hình.'),
            ('Backward Logic', 'Ngược hoàn toàn: mô hình HIỆN ĐÃ dùng một giá trị đồng nhất rồi; quan sát thêm sẽ giúp xác định biên độ thực tế chứ không phải để thu về một giá trị duy nhất.'),
            ('Confuses Model vs. Reality', 'Mô hình sử dụng một giá trị đồng nhất nên biến thiên thực tế trên Titan không thể gây ra sự bất nhất “giữa các mô phỏng của chính mô hình”.'),
        ],
    ),
    15: meta(
        'Standard English Conventions', 'Boundaries', 'Medium', 'C',
        'Câu chứa hai mệnh đề độc lập (Independent Clauses): IC1 = “Her work challenges conventional notions of race, gender, history, and memory” và IC2 = “she is credited with expanding the horizons of conceptual photographic art.” Để nối hai mệnh đề độc lập bằng liên từ đẳng lập FANBOYS “and”, BẮT BUỘC phải đặt dấu phẩy ngay trước “and” → “memory, and” → Chọn C.',
        'Công thức bất di bất dịch nối hai mệnh đề độc lập: IC1 + , + FANBOYS (for, and, nor, but, or, yet, so) + IC2. Thiếu dấu phẩy (A) hay thiếu liên từ (B) đều sai!',
        [
            ('Missing Comma', 'memory and — thiếu dấu phẩy trước liên từ đẳng lập “and” khi nối hai mệnh đề độc lập.'),
            ('Comma Splice', 'memory, — chỉ dùng dấu phẩy nối hai mệnh đề độc lập mà không có liên từ (comma splice).'),
            ('Đáp án đúng', 'memory, and — hoàn thành mục cuối trong chuỗi liệt kê rồi dùng đúng cấu trúc “, and” nối hai mệnh đề độc lập.'),
            ('Run-On Sentence', 'memory — ghép thẳng hai mệnh đề độc lập không có bất kỳ dấu câu hay liên từ nào.'),
        ],
    ),
    16: meta(
        'Standard English Conventions', 'Boundaries', 'Hard', 'A',
        'Xét cấu trúc cụm danh từ: “the novelist Lan Samantha Chang, author of <i>Inheritance</i>.” (1) Khi danh từ chỉ nghề nghiệp/chức danh đứng trước tên riêng đi kèm mạo từ “the” (“the novelist Lan Samantha Chang”), tên riêng là thông tin thiết yếu (essential) giúp xác định đó là tiểu thuyết gia nào → KHÔNG đặt dấu phẩy giữa “novelist” và “Lan Samantha Chang”. (2) Cụm “author of <i>Inheritance</i>” là ngữ đồng vị bổ sung (nonessential appositive) đứng sau tên riêng → PHẢI đặt dấu phẩy sau “Chang” → “novelist Lan Samantha Chang,” → Chọn A.',
        'Quy tắc vàng SAT về chức danh + tên riêng + đồng vị ngữ: [the + nghề nghiệp + Tên Riêng] (KHÔNG dấu phẩy ở giữa) + [, cụm đồng vị ngữ giải thích thêm]. Thử bỏ phần giữa dấu phẩy ở C sẽ ra câu vô nghĩa “chose the novelist author of Inheritance”!',
        [
            ('Đáp án đúng', 'novelist Lan Samantha Chang, — không tách rời chức danh và tên riêng thiết yếu, đồng thời có dấu phẩy ngăn cách ngữ đồng vị “author of Inheritance” phía sau.'),
            ('Missing Comma', 'novelist Lan Samantha Chang — thiếu dấu phẩy bắt buộc trước ngữ đồng vị “author of Inheritance”.'),
            ('Broken Essential Pair', 'novelist, Lan Samantha Chang, — biến tên riêng thành phần phụ; bỏ đi sẽ còn “the novelist author of Inheritance” (sai ngữ pháp).'),
            ('Wrong Comma Placement', 'novelist, Lan Samantha Chang — vừa đặt thừa dấu phẩy sau “novelist” vừa thiếu dấu phẩy trước “author”.'),
        ],
    ),
    17: meta(
        'Standard English Conventions', 'Boundaries', 'Medium', 'C',
        'Xét cụm chêm giữa cặp dấu gạch ngang dài: “—including the _______ Gilbertese and Tongan, which are spoken by 120,000 and 108,000 speakers, respectively—”. Cụm “the languages Gilbertese and Tongan” là dạng [the + danh từ phân loại + tên riêng xác định (essential appositive)] — cần nối liền mạch KHÔNG CÓ BẤT KỲ DẤU CÂU NÀO giữa “languages” và “Gilbertese and Tongan” → “languages” → Chọn C.',
        'Cụm [the + danh từ chung + tên riêng cụ thể] như “the languages Gilbertese and Tongan” hay “the hit song ‘A Tear’” KHÔNG BAO GIỜ dùng dấu phẩy, hai chấm hay gạch ngang xen giữa!',
        [
            ('Unnecessary Comma', 'languages, — biến tên hai ngôn ngữ thành phần phụ; nếu lược bỏ sẽ còn “including the languages which are spoken by... respectively” (vô nghĩa vì chưa nêu hai ngôn ngữ nào!).'),
            ('Improper Colon', 'languages: — dấu hai chấm đòi hỏi mệnh đề độc lập trọn vẹn phía trước, nhưng “including the languages” chưa hoàn chỉnh.'),
            ('Đáp án đúng', 'languages — nối trực tiếp danh từ chung với hai tên riêng thiết yếu Gilbertese và Tongan không cần dấu câu.'),
            ('Broken Em-Dash Pair', 'languages— — tự ý đóng sớm cặp dấu gạch ngang dài vốn kết thúc ở sau từ “respectively—”.'),
        ],
    ),
    18: meta(
        'Standard English Conventions', 'Boundaries', 'Medium', 'D',
        'Trong cụm “you would have heard the hit _______ “A Tear” by Gene McDaniels”, tên ca khúc “A Tear” là thông tin thiết yếu xác định rõ “bài hát hit” nào được nhắc đến (essential appositive). Do đó không đặt bất kỳ dấu câu nào giữa “song” và ““A Tear”” → “song” → Chọn D.',
        'Cùng một quy tắc với câu 17: trước tên tác phẩm/bài hát thiết yếu đi liền sau “the + danh từ loại hình” (“the hit song ‘A Tear’”), luôn chọn KHÔNG DẤU CÂU.',
        [
            ('Improper Colon', 'song: — phía trước dấu hai chấm (“chances are you would have heard the hit song”) chưa tạo ngữ cảnh giới thiệu danh sách/giải thích tách biệt mà tên bài hát gắn liền trực tiếp với “hit song”.'),
            ('Improper Semicolon', 'song; — sau dấu chấm phẩy phải là một mệnh đề độc lập, nhưng ““A Tear” by Gene McDaniels” chỉ là cụm danh từ.'),
            ('Unnecessary Comma', 'song, — tách ““A Tear”” thành thông tin không thiết yếu là sai vì Gene McDaniels có nhiều bài hát và cụm “the hit song” cần tên cụ thể để định danh.'),
            ('Đáp án đúng', 'song — không dùng dấu câu giữa danh từ loại hình (“the hit song”) và tên bài hát thiết yếu (“A Tear”).'),
        ],
    ),
    19: meta(
        'Standard English Conventions', 'Boundaries', 'Hard', 'D',
        'Xét hai mệnh đề độc lập ở câu 2: IC1 = “Such interpretations are ultimately speculative, though” (“though” đặt cuối IC1 để tương phản với câu 1 rằng màu đỏ gợi ý thành phần đá); IC2 = “the object’s red coloration may be an incidental effect of radiation...” (giải thích VÌ SAO các diễn giải đó mang tính suy đoán, không đối lập với IC1!). Do đó phải đặt dấu chấm phẩy SAU “though” để gom “though” về IC1 và tách rành mạch với IC2 → “speculative, though;” → Chọn D.',
        'Cặp bài trùng kinh điển với M1 Q20! Khi “though” đóng vai trò trạng từ cuối vế 1 (tương phản câu trước) và vế 2 giải thích cho vế 1, luôn chọn cấu trúc `, though;`.',
        [
            ('Fragment After Semicolon', 'speculative; though — đặt “though” sau dấu chấm phẩy biến vế 2 thành mệnh đề phụ thuộc (“though the object’s red coloration may be...”) đứng trơ trọi (fragment).'),
            ('Comma Splice', 'speculative, though, — lỗi dùng chỉ dấu phẩy để nối hai mệnh đề độc lập.'),
            ('Reversed Logic', 'speculative, though — dùng “though” làm liên từ nhượng bộ (“mặc dù màu đỏ có thể là hiệu ứng phụ”) làm đảo ngược hoàn toàn logic giải thích của câu.'),
            ('Đáp án đúng', 'speculative, though; — gom “though” vào cuối IC1 để tương phản với câu 1 và dùng dấu chấm phẩy tách chuẩn với IC2 giải thích nguyên nhân.'),
        ],
    ),
    20: meta(
        'Standard English Conventions', 'Form, Structure, and Sense', 'Hard', 'A',
        'Phân tích cấu trúc câu cuối: Chủ ngữ chính = “Such a compensatory measure”; Động từ chính chia thì ĐÃ CÓ SẴN ở phía sau = “offers” (“offers an evolutionary explanation of mitochondrial reproduction”). Vì câu đã có động từ chính “offers”, chỗ trống KHÔNG thể là động từ chia thì (loại B, C, D) mà phải là hiện tại phân từ chủ động “counteracting” bổ nghĩa cho “Such a compensatory measure” và nhận tân ngữ “the organelle’s decline” → Chọn A.',
        'Chiến thuật săn câu khó Form, Structure, and Sense: ĐỌC HẾT CÂU để tìm động từ chính chia thì! Khi thấy động từ chính “offers” phía sau, lập tức loại mọi động từ chia thì và chọn phân từ V-ing chủ động (“counteracting”).',
        [
            ('Đáp án đúng', 'counteracting — hiện tại phân từ chủ động tạo cụm bổ nghĩa cho “Such a compensatory measure” trước động từ chính “offers”.'),
            ('Double Finite Verb', 'had counteracted — động từ chia thì quá khứ hoàn thành, tạo lỗi hai động từ chính không có liên từ (“measure had counteracted..., offers...”).'),
            ('Double Verb / Wrong Voice', 'counteracted — vừa tạo lỗi hai động từ chia thì, vừa không thể dùng dạng phân từ bị động vì ngay sau nó có tân ngữ trực tiếp “the organelle’s decline”.'),
            ('Double Finite Verb', 'counteracts — động từ chia thì hiện tại đơn, đụng độ trực tiếp với động từ chính “offers” ở vế sau.'),
        ],
    ),
    21: meta(
        'Standard English Conventions', 'Form, Structure, and Sense', 'Hard', 'B',
        'Cấu trúc song sinh với câu 20! Xác định khung câu 2: Chủ ngữ = “Aslanian’s macroanalysis”; Động từ chính chia thì ĐÃ CÓ SẴN = “shows” (“shows not only the steady popularity of religious texts...”). Do đó phần nằm giữa chủ ngữ và “shows” chỉ là cụm phân từ bổ nghĩa cho “macroanalysis”. Vì ngay sau chỗ trống là tân ngữ trực tiếp “nearly 1,000 book titles”, phải dùng hiện tại phân từ chủ động “examining” → Chọn B.',
        'Đừng để bẫy chủ ngữ số ít (“Aslanian’s macroanalysis”) dụ chọn “examines” (C)! Đọc tiếp 10 từ phía sau sẽ thấy động từ chính “shows” — chỗ trống bắt buộc phải là phân từ V-ing (“examining”).',
        [
            ('Double Verb / Wrong Voice', 'examined — nếu hiểu là quá khứ đơn sẽ đụng độ động từ chính “shows”; nếu hiểu là quá khứ phân từ bị động thì sai vì có tân ngữ “nearly 1,000 book titles” phía sau.'),
            ('Đáp án đúng', 'examining — hiện tại phân từ chủ động bổ nghĩa cho “Aslanian’s macroanalysis” (phân tích vĩ mô khảo sát gần 1.000 tựa sách) trước động từ chính “shows”.'),
            ('Double Finite Verb Trap', 'examines — bẫy kinh điển: tạo hai động từ chính chia thì liên tiếp (“macroanalysis examines... shows...”) mà không có liên từ.'),
            ('Double Finite Verb', 'had examined — động từ chia thì quá khứ hoàn thành, gây lỗi trùng lặp động từ chính với “shows”.'),
        ],
    ),
    22: meta(
        'Expression of Ideas', 'Transitions', 'Hard', 'C',
        'Theo dõi mạch ý 3 câu: Câu 1 nhấn mạnh sao Shaula sáng rực rỡ DÙ cách rất xa Trái Đất (570 năm ánh sáng). Câu 2 đặt sao Alsephina cạnh Shaula vì nó cũng lọt top 50 sao sáng nhất (hạng 45). Câu 3 thừa nhận/nhượng bộ một điểm giảm nhẹ sự tương đồng ấn tượng đó: độ sáng của Alsephina nhiều khả năng chỉ nhờ nó nằm rất gần Trái Đất (chỉ 80 năm ánh sáng). Từ nối mang sắc thái nhượng bộ/thừa nhận điểm ngoại lệ là “Granted,” (Phải thừa nhận rằng / Đành rằng) → Chọn C.',
        'Khi câu 2 đặt đối tượng B ngang hàng với thành tích ấn tượng của A, nhưng câu 3 lại thừa nhận lý do khiến thành tích của B “dễ hơn/ít ấn tượng hơn” (ở gần chỉ 80 ly vs. 570 ly), luôn chọn từ nối nhượng bộ = Granted.',
        [
            ('Wrong Relationship', 'Indeed, = Quả thực/Hơn thế nữa (nhấn mạnh củng cố) — không hợp khi câu 3 đang giải thích yếu tố làm giảm bớt mức độ ấn tượng so với Shaula.'),
            ('Reversed Causality', 'As a result, = Do đó — việc xếp hạng 45 không phải nguyên nhân sinh ra khoảng cách gần Trái Đất.'),
            ('Đáp án đúng', 'Granted, = Phải thừa nhận rằng — diễn tả chuẩn xác sắc thái nhượng bộ khi chỉ ra Alsephina sáng chủ yếu nhờ ở gần (80 ly) chứ không như Shaula ở tận 570 ly.'),
            ('Opposite Relationship', 'Similarly, = Tương tự — sai ngược vì Shaula sáng bất chấp ở xa, còn Alsephina sáng nhờ ở gần.'),
        ],
    ),
    23: meta(
        'Expression of Ideas', 'Transitions', 'Easy', 'B',
        'Câu 2 gồm hai ví dụ song song về thơ miêu tả hội họa (ekphrastic poem) nối bằng dấu chấm phẩy: bài thơ của Robert Hayden chiêm nghiệm bức tranh <i>Water Lilies</i> của Monet; bài thơ “The Kiss” của Sasha Pimentel CŨNG lấy một bức tranh làm chủ đề (<i>The Kiss</i> của Gustav Klimt). Quan hệ song song tương đồng → “likewise,” → Chọn B.',
        'Hai ví dụ song song cùng minh họa một định nghĩa đặt cạnh nhau qua dấu chấm phẩy luôn nối bằng từ chỉ sự tương đồng = likewise / similarly.',
        [
            ('Wrong Relationship', 'nevertheless, = tuy nhiên — sai vì hai ví dụ hoàn toàn đồng hướng, không hề tương phản.'),
            ('Đáp án đúng', 'likewise, = tương tự như vậy — liên kết hoàn hảo hai ví dụ song song về thơ lấy cảm hứng từ hội họa.'),
            ('Wrong Relationship', 'hence, = do đó — bài thơ của Hayden không phải nguyên nhân tạo ra bài thơ của Pimentel.'),
            ('Wrong Relationship', 'conversely, = ngược lại — trái hoàn toàn với quan hệ tương đồng giữa hai vế.'),
        ],
    ),
    24: meta(
        'Expression of Ideas', 'Transitions', 'Medium', 'D',
        'Câu 2 nêu lập luận của các học giả: sự ẩn mình vào thiên nhiên của Wordsworth thực chất là phản ứng thẩm mỹ và lời phê phán ngầm đối với quá trình công nghiệp hóa, đô thị hóa nhanh chóng ở Anh. Câu 3 rút ra hệ quả/kết luận trực tiếp từ câu 2: DO ĐÓ (“As such,”), bất chấp vẻ ngoài thơ mộng, bài thơ vẫn mang đậm dấu ấn của những biến chuyển dữ dội trong đời sống nước Anh → Chọn D.',
        'Đừng để cụm “despite its idyllic quality” trong câu 3 đánh lừa chọn “Nevertheless,” (A)! Cụm “despite...” chỉ đối lập với câu 1, còn bản thân câu 3 là KẾT LUẬN TIẾP NỐI trực tiếp từ câu 2 → chọn “As such,” (= Therefore / Consequently).',
        [
            ('Contrast Trap', 'Nevertheless, = Tuy nhiên — sai vì câu 3 đồng thuận và suy ra trực tiếp từ câu 2, không hề tương phản với câu 2.'),
            ('Wrong Relationship', 'For example, = Ví dụ — câu 3 là một kết luận tổng quát chứ không phải dẫn chứng cụ thể cho câu 2.'),
            ('Weak / Imprecise', 'Moreover, = Hơn nữa (thêm ý mới tách biệt) — kém chính xác hơn vì câu 3 là hệ quả logic trực tiếp suy ra từ luận điểm câu 2.'),
            ('Đáp án đúng', 'As such, = Do đó / Vì thế — diễn đạt chuẩn xác mối quan hệ kết luận trực tiếp rút ra từ lập luận của các học giả ở câu 2.'),
        ],
    ),
    25: meta(
        'Expression of Ideas', 'Rhetorical Synthesis', 'Easy', 'C',
        'Mục tiêu câu hỏi: giải thích MỤC ĐÍCH của các liên đoàn công đoàn quốc gia (“explain the purpose of national union federations”). Ghi chú thứ 2 cho biết SSWTUF (một liên đoàn công đoàn quốc gia) giúp cải thiện điều kiện cho người lao động trong quốc gia đó. Chỉ đáp án C giải thích đúng mục đích này → Chọn C.',
        'Kiểm tra đúng đối tượng và mục tiêu trong câu hỏi: “purpose of NATIONAL union federations” → loại ngay câu B vì B nói mục đích của REGIONAL union federations!',
        [
            ('Missing Purpose', 'Chỉ nói SSWTUF là một liên đoàn quốc gia do ITUC-Africa đại diện, không giải thích mục đích hoạt động của liên đoàn quốc gia.'),
            ('Wrong Target Trap', 'Giải thích mục đích của liên đoàn KHU VỰC (regional union federations), không phải liên đoàn QUỐC GIA (national union federations).'),
            ('Đáp án đúng', 'Giải thích trực tiếp và khái quát chuẩn xác mục đích của các liên đoàn công đoàn quốc gia: cải thiện điều kiện cho người lao động tại quốc gia thành viên.'),
            ('Missing Purpose', 'Chỉ nêu định danh và vị trí châu Phi của SSWTUF, không nhắc tới mục đích hoạt động.'),
        ],
    ),
    26: meta(
        'Expression of Ideas', 'Rhetorical Synthesis', 'Easy', 'A',
        'Mục tiêu của học sinh: giới thiệu khái niệm “cultural analysis” (phân tích văn hóa) cho đối tượng khán giả CHƯA QUEN THUỘC với khái niệm này (“present cultural analysis to an audience unfamiliar with the concept”). Do đó cần giới thiệu rõ nó thuộc lĩnh vực nào (một hướng tiếp cận phê bình nghệ thuật) và định nghĩa cốt lõi của nó (xem xét các xu hướng, niềm tin và giá trị văn hóa ở thời đại của tác phẩm) → Chọn A.',
        'Khi đề yêu cầu giới thiệu khái niệm X cho “an audience unfamiliar with the concept”, đáp án đúng PHẢI chứa phần định nghĩa/phân loại khái quát của X (“An approach to art criticism, cultural analysis considers...”).',
        [
            ('Đáp án đúng', 'Định nghĩa trọn vẹn và dễ hiểu cho người mới: nêu rõ phân loại (“An approach to art criticism”) và nội dung cốt lõi của cultural analysis.'),
            ('Wrong Concept', 'Nói về ví dụ của “emphasis analysis”, hoàn toàn sai khái niệm cần giới thiệu.'),
            ('No Concept Named', 'Chỉ kể ví dụ về bức tranh của Picasso mà không hề gọi tên hay định nghĩa “cultural analysis”.'),
            ('Wrong Focus', 'Tập trung định nghĩa “emphasis analysis” thay vì định nghĩa “cultural analysis”.'),
        ],
    ),
    27: meta(
        'Expression of Ideas', 'Rhetorical Synthesis', 'Hard', 'A',
        'Mục tiêu của học sinh: SO SÁNH giả thuyết của Fodor với giả thuyết của Carruthers (“compare Fodor’s hypothesis with Carruthers’s”). Theo ghi chú: Fodor (1983) cho rằng chỉ các hệ thống nhận thức bậc thấp mới có tính mô-đun (bậc cao thì không); Carruthers (2003) mở rộng tính mô-đun ra TẤT CẢ các hệ thống nhận thức (MMH). Đáp án A so sánh hoàn toàn chuẩn xác: vì chỉ xem một số chứ không phải tất cả hệ thống nhận thức là mô-đun, thuyết của Fodor không rộng mở bằng MMH → Chọn A.',
        'Ở câu Rhetorical Synthesis độ khó Hard, luôn kiểm chứng TÍNH ĐÚNG SỰ THẬT của từng phương án đối chiếu với ghi chú: cả C và D đều có vẻ đang so sánh nhưng cố tình bóp méo nội dung ghi chú!',
        [
            ('Đáp án đúng', 'So sánh sắc bén và chính xác 100% sự khác biệt về phạm vi giữa Fodorian modularity (một số hệ thống) và MMH (toàn bộ hệ thống).'),
            ('No Real Comparison', 'Chỉ nêu trình tự thời gian (“Following Fodor’s 1983 hypothesis...”) mà không hề nói giả thuyết của Fodor có nội dung gì để so sánh.'),
            ('Factual Distortion', 'Bóp méo ghi chú: cả Fodor lẫn Carruthers ĐỀU đồng ý các hệ thống bậc thấp (tri giác, ngôn ngữ) mang tính mô-đun — họ chỉ khác nhau ở hệ thống bậc cao!'),
            ('Factual Distortion', 'Bóp méo ghi chú: Carruthers KHÔNG phản đối ý tưởng tâm trí gồm các cấu trúc thần kinh bẩm sinh (modules), mà còn MỞ RỘNG ý tưởng đó ra mọi hệ thống.'),
        ],
    ),
}

M2_BUILD_PATCHES = {
    10: {
        'prependStimulusHtml': _svg_m2_q10_seagrass(),
    },
    11: {
        'questionHtml': 'Which finding, if true, would most directly support the text’s claim about wireless communication devices?',
        'options': [
            'The high conductivity of the CFRP is what makes the energy output from a piezoelectric harvester sufficient for wireless communication devices.',
            'The CFRP electrode is incompatible with most wireless communication devices.',
            'Intermittent or unpredictable electrical supply undermines the efficacy of wireless communication devices.',
            'The near-constant kinetic vibration of a spacecraft makes it possible to power its wireless communication devices using only non-CFRP piezoelectric harvesters.',
        ],
    },
    12: {
        'questionHtml': 'Which choice most logically completes the text?',
        'options': [
            'because bumblebees and other bees with generalist diets are less negatively affected by environmental stress than bees with specialized diets are, they are less likely to experience major population changes in the future than bees with specialized diets are.',
            'although bumblebees have been more extensively studied than most wild bees, researchers should not use bumblebees to draw conclusions about the decline of other wild bees, even ones with feeding patterns and levels of sociability that are similar to those of bumblebees.',
            'although bumblebees and many other wild bees have experienced similar population declines in the past, compared with other wild bees, bumblebees are likely at greater risk of being harmed by climate variation than by habitat destruction.',
            'because the responses of bumblebees and other wild bees to environmental threats are not always comparable, researchers need to exercise caution when extrapolating information about wild-bee population declines from bumblebees.',
        ],
    },
    13: {
        'questionHtml': 'Which choice most logically completes the text?',
        'options': [
            'silver nanoparticles may increase the metabolic processes of the bacteria, thereby increasing the number of free electrons available to transfer to the electrode.',
            'as the density of the biofilm increases, the series of redox reactions may accelerate independent of the presence of the silver nanoparticles.',
            'silver nanoparticles may allow electrons to bypass the series of redox reactions and transfer directly to the electrode.',
            'electrons may be conducted directly to the electrode before the silver nanoparticles catalyze the redox reactions.',
        ],
    },
    14: {
        'questionHtml': 'Which choice most logically completes the text?',
        'options': [
            'some disagreements between the model’s simulations of Titan’s precipitation and humidity and the moon’s actual precipitation and humidity are to be expected.',
            'even though the model’s outputs sometimes agree with observational data, Titan’s real methane mole fraction is likely higher than the methane mole fraction used in the model.',
            'further observations of Titan may clarify the moon’s methane mole fraction sufficiently for the model to employ a single value rather than a range.',
            'inconsistencies across the model’s simulations of Titan’s precipitation and humidity could be attributable to variations in the moon’s methane mole fraction.',
        ],
    },
    15: {
        'questionHtml': 'Which choice completes the text so that it conforms to the conventions of Standard English?',
        'options': ['memory and', 'memory,', 'memory, and', 'memory'],
    },
    16: {
        'questionHtml': 'Which choice completes the text so that it conforms to the conventions of Standard English?',
        'options': [
            'novelist Lan Samantha Chang,',
            'novelist Lan Samantha Chang',
            'novelist, Lan Samantha Chang,',
            'novelist, Lan Samantha Chang',
        ],
    },
    17: {
        'questionHtml': 'Which choice completes the text so that it conforms to the conventions of Standard English?',
        'options': ['languages,', 'languages:', 'languages', 'languages—'],
    },
    18: {
        'questionHtml': 'Which choice completes the text so that it conforms to the conventions of Standard English?',
        'options': ['song:', 'song;', 'song,', 'song'],
    },
    19: {
        'questionHtml': 'Which choice completes the text so that it conforms to the conventions of Standard English?',
        'options': ['speculative; though', 'speculative, though,', 'speculative, though', 'speculative, though;'],
    },
    20: {
        'questionHtml': 'Which choice completes the text so that it conforms to the conventions of Standard English?',
        'options': ['counteracting', 'had counteracted', 'counteracted', 'counteracts'],
    },
    22: {
        'questionHtml': 'Which choice completes the text with the most logical transition?',
        'options': ['Indeed,', 'As a result,', 'Granted,', 'Similarly,'],
    },
    26: {
        'questionHtml': 'The student wants to present cultural analysis to an audience unfamiliar with the concept. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
        'options': [
            'An approach to art criticism, cultural analysis considers the cultural trends, beliefs, and values of an artwork’s time.',
            'An emphasis analysis of <i>Still Life with Lobster</i> might consider how the painting’s sharply contrasting colors place primary emphasis on the lobster in the foreground.',
            '<i>Les Demoiselles d’Avignon</i>’s portrayal of fragmented human figures challenged conventions of beauty during a time of cultural upheaval (early twentieth century).',
            'Emphasis analysis differs from cultural analysis in that emphasis analysis examines how visual elements are weighted in an artwork’s composition.',
        ],
    },
}

M2_POST_PATCHES = {
    1: {
        'stim_replace': [
            ('Willstatter', 'Willstätter'),
            ('is given.', 'is given _______.'),
            ('instance. in', 'instance, in'),
        ],
    },
    2: {
        'stim_replace': [
            ('delta is «itis', 'delta is _______: it is'),
        ],
    },
    3: {
        'stim_replace': [
            ('nineteenth century', 'nineteenth-century'),
            ('james McNeill', 'James McNeill'),
            ('sentimental. Whistler', 'sentimental, Whistler'),
            ('seemed N In this way.', 'seemed _______. In this way,'),
        ],
    },
    4: {
        'stim_replace': [
            ('town of Milby. By the laity', 'town of Milby.||EXCERPT||By the laity'),
            ('[Mr Fly)', '[Mr. Ely]'),
            ('I.ondon', 'London'),
            ('drawing rooms', 'drawing-rooms'),
            ('fellow, Mr.', 'fellow. Mr.'),
            ('himself: he', 'himself; he'),
            ('laughing at him,', 'laughing at <i>him</i>.'),
        ],
        'opt_replace': [
            ('more naive', 'more naïve'),
            ('Mr. ly', 'Mr. Ely'),
        ],
    },
    5: {
        'stim_replace': [
            ('Barragan', 'Barragán'),
            ('career. which', 'career, which'),
            ('Suarez', 'Suárez'),
            ('forms. typical', 'forms, typical'),
            ('aesthetic. contrasted', 'aesthetic, contrasted'),
            ('Guadalajara. such', 'Guadalajara, such'),
        ],
        'opt_replace': [
            ('architect. states', 'architect, states'),
            ('career. and', 'career, and'),
            ('career. describes', 'career, describes'),
        ],
    },
    6: {
        'stim_replace': [
            ('Castaner', 'Castañer'),
            ('stores. and', 'stores, and'),
            ('houndaries', 'boundaries'),
            ('subjective. so', 'subjective, so'),
            ('algorithm. is', 'algorithm, is'),
        ],
        'opt_replace': [
            ('businesses. discusses', 'businesses, discusses'),
            ('other fields,', 'other fields.'),
            ('methodology. and', 'methodology, and'),
        ],
    },
    7: {
        'stim_replace': [
            ('water —critical', 'water—critical'),
            ('K2 18 b', 'K2-18 b'),
            ('edge of the HZ. Text 2', 'edge of the HZ.||TEXT2||Text 2'),
            ('paper. Shang-Min', 'paper, Shang-Min'),
            ('planets’HZ', 'planets’ HZ'),
        ],
        'q_replace': [
            ('research. as', 'research, as'),
        ],
        'opt_replace': [
            ('discovered. most', 'discovered, most'),
        ],
    },
    8: {
        'stim_replace': [
            ('‘When Kenyan', 'When Kenyan'),
            ("Nguigl wa Thiong'o.", 'Ngũgĩ wa Thiong’o,'),
            ('GIkuy,', 'Gĩkũyũ,'),
            ('Kiswahili —widely', 'Kiswahili—widely'),
            ('Africa would', 'Africa—would'),
            ('Nglgi', 'Ngũgĩ'),
            ('Gikuyil', 'Gĩkũyũ'),
        ],
        'opt_replace': [
            ('Ngugi', 'Ngũgĩ'),
            ('Gikiyu.', 'Gĩkũyũ,'),
            ('Gikliyi', 'Gĩkũyũ'),
            ('language. such as Gikayu.', 'language, such as Gĩkũyũ.'),
            ('1970s. Ngũgĩ', '1970s, Ngũgĩ'),
            ('languages. and', 'languages, and'),
            ('Gikuyn', 'Gĩkũyũ'),
        ],
    },
    9: {
        'stim_replace': [
            ('Moran. Daniel', 'Moran, Daniel'),
            ('Rodriguez. and', 'Rodriguez, and'),
            ('Quito. Ecuador. and', 'Quito, Ecuador, and'),
            ('Quito. 82,9%', 'Quito, 82.9%'),
        ],
        'opt_replace': [
            ('parks In Quito', 'parks in Quito'),
        ],
    },
    10: {
        'stim_replace': [
            (
                'Chesapeake Bay Seagrass Coverage 2012-2019 HIEEDES AN Z O 5 36,000 2 Enea EER = 27,000 O woot LLL LL] 18000 EE gee a z 0 > Ed EG Bla annnEh CE i CIRC TIC SER RN ESR] A NL NS © WTAE AT ADT AST OT Year —h— eelgrass =~ widgeon grass ++=O++ total of all types of seagrass ',
                '',
            ),
            ('Historically. eelgrass', 'Historically, eelgrass'),
            ('predominant. but', 'predominant, but'),
            (
                'tolerating heat hotter and crowing faster than eelarace dnes Althonah the increase in widoean',
                'tolerating heat better and growing faster than eelgrass does. Although the increase in widgeon grass has been associated with a substantial increase in total seagrass coverage in the bay, researchers caution that the latter change does not necessarily make the seagrass ecosystem as a whole more resilient to environmental shocks.',
            ),
        ],
        'q_replace': [
            ('if true. would', 'if true, would'),
        ],
        'opt_replace': [
            ('‘Water temperatures', 'Water temperatures'),
            ('2018. a', '2018, a'),
            ('the hay. leading', 'the bay, leading'),
        ],
    },
    11: {
        'stim_replace': [
            ('Plezoelectric', 'Piezoelectric'),
            ('Kinetic', 'kinetic'),
            ('energy. precluding', 'energy, precluding'),
            ('spacecraft. for', 'spacecraft, for'),
            ('carbon fiber reinforced', 'carbon-fiber-reinforced'),
            ('to he powered', 'to be powered'),
        ],
    },
    12: {
        'stim_replace': [
            ('by. among', 'by, among'),
            ('honeybees, As', 'honeybees. As'),
            ('wild bee declines', 'wild-bee declines'),
            ('species). two', 'species), two'),
        ],
    },
    13: {
        'stim_replace': [
            ('(MICs)', '(MFCs)'),
            ('metal. liberating', 'metal, liberating'),
            ('oxidation reduction', 'oxidation-reduction'),
            ('centimeter im;cme).', 'centimeter (mW/cm<sup>2</sup>).'),
            ('0.66 miW.em®. since', '0.66 mW/cm<sup>2</sup>. Since'),
            ('conductivity. the', 'conductivity, the'),
        ],
    },
    14: {
        'stim_replace': [
            ('intluences', 'influences'),
            ('moon. the', 'moon, the'),
            ('atmespheric', 'atmospheric'),
            ('1PS1. atmospheric', 'IPSL atmospheric'),
            ('note that', 'note that _______'),
        ],
    },
    15: {
        'stim_replace': [
            ('What Absence Is Made Of', '<i>What Absence Is Made Of</i>'),
            ('Washington. DC. was', 'Washington, DC, was'),
            ('Lorna simpson', 'Lorna Simpson'),
            ('gender. history', 'gender, history'),
            ('and she is', 'and _______ she is'),
        ],
    },
    16: {
        'stim_replace': [
            ('I{ome Ground: A Guide to the American Landscape', '<i>Home Ground: A Guide to the American Landscape</i>'),
            ('DJ. ‘Waldie. a nonfiction writer. to', 'D.J. Waldie, a nonfiction writer, to'),
            ('“thalweg.”', '“thalweg,”'),
            ('“cape.”', '“cape,”'),
            ('chose the author of Inheritance.', 'chose the _______ author of <i>Inheritance</i>.'),
        ],
    },
    17: {
        'stim_replace': [
            ('eLUons vo LC & ', ''),
            ('including the Gilbertese', 'including the _______ Gilbertese'),
            ('Tongan. which', 'Tongan, which'),
            ('120.000 and 108.000 speakers. respectively and', '120,000 and 108,000 speakers, respectively—and'),
            ("world's languages. making", "world's languages, making"),
            ('Marian Klamer, xX', 'Marian Klamer.'),
        ],
    },
    18: {
        'stim_replace': [
            ('1f you', 'If you'),
            ('the hit “a Tear”', 'the hit _______ “A Tear”'),
        ],
    },
    19: {
        'stim_replace': [
            ('EX Recent', 'Recent'),
            ('Neptune —has', 'Neptune—has'),
            ('red. suggesting', 'red, suggesting'),
            ('ultimately the', 'ultimately _______ the'),
            ('wind. or', 'wind, or'),
            ('ohjects', 'objects'),
        ],
    },
    20: {
        'stim_replace': [
            ('measure the organelle', 'measure _______ the organelle'),
        ],
    },
    21: {
        'stim_replace': [
            ('ES tn his 2011 book.', 'In his 2011 book,'),
            ('carly modern', 'early modern'),
            ('macroanalysis nearly 1.000 hook', 'macroanalysis _______ nearly 1,000 book'),
        ],
        'q_replace': [
            ('Standard fnglish?', 'Standard English?'),
        ],
    },
    22: {
        'stim_replace': [
            ('ED Despite', 'Despite'),
            ('Farth', 'Earth'),
            ('Shaula. the', 'Shaula, the'),
            ('45th. to', '45th, to'),
            ('exact). Alsephina', 'exact). _______ Alsephina'),
            ('Larth.', 'Earth.'),
        ],
    },
    23: {
        'stim_replace': [
            ('poem. a', 'poem, a'),
            ('drawing. sculpture', 'drawing, sculpture'),
            ('Water Lilies: Sasha', '<i>Water Lilies</i>; Sasha'),
            ('“The Kiss," takes', '“The Kiss,” _______ takes'),
            ('work The Kiss.', 'work <i>The Kiss</i>.'),
        ],
        'opt_replace': [
            ('nevertheless.', 'nevertheless,'),
        ],
    },
    24: {
        'stim_replace': [
            ('ED Contemplating', 'Contemplating'),
            ('landscape. the', 'landscape, the'),
            ('critique of —England', 'critique of—England'),
            ('time. despite', 'time. _______ despite'),
            ('quality. the', 'quality, the'),
        ],
        'opt_replace': [
            ('example.', 'example,'),
            ('such.', 'such,'),
        ],
    },
    25: {
        'stim_replace': [
            ('* The south sudan Workers Trade Union I\'ederation', '||BULLET||The South Sudan Workers Trade Union Federation'),
            ('South sudan. « It', 'South Sudan.||BULLET||It'),
            ('nation. * ITUC-Africa', 'nation.||BULLET||ITUC-Africa'),
            ('Africa. « ttrepresents the SSWTUE.', 'Africa.||BULLET||It represents the SSWTUF.'),
        ],
        'opt_replace': [
            ('SSWTUF ts', 'SSWTUF is'),
            ('ITUC Africa', 'ITUC-Africa'),
            ('federations. such', 'federations, such'),
        ],
    },
    26: {
        'stim_replace': [
            ('topic. a', 'topic, a'),
            ('notes: + Emphasis', 'notes:||BULLET||Emphasis'),
            ('criticism. + Emphasis', 'criticism.||BULLET||Emphasis'),
            ('artworks composition. + such', 'artwork’s composition.||BULLET||Such'),
            ('Still Life with Lobster', '<i>Still Life with Lobster</i>'),
            ('foreground. * Cultural', 'foreground.||BULLET||Cultural'),
            ('trends. beliefs. and', 'trends, beliefs, and'),
            ('time. + Such', 'time.||BULLET||Such'),
            ('Les Demoiselles d Avignon', '<i>Les Demoiselles d’Avignon</i>'),
        ],
    },
    27: {
        'stim_replace': [
            ('‘While researching a topic. a', 'While researching a topic, a'),
            ('notes: * Modularity', 'notes:||BULLET||Modularity'),
            ('fast. necessary', 'fast, necessary'),
            ('tasks. * 1983:', 'tasks.||BULLET||1983:'),
            ('(e.g, perception', '(e.g., perception'),
            ('modular. + In Fodorian modularity. high-level', 'modular.||BULLET||In Fodorian modularity, high-level'),
            ('modular. * 2003:', 'modular.||BULLET||2003:'),
            ('(MMH). * MMH', '(MMH).||BULLET||MMH'),
        ],
        'opt_replace': [
            ('modular. Fodorian', 'modular, Fodorian'),
            ('language. modular.', 'language, modular.'),
            ('2003. Carruthers', '2003, Carruthers'),
            ('hypothesis. disagreeing', 'hypothesis, disagreeing'),
        ],
    },
}


# ============================================================================
# BUILD COMPLETE 54-QUESTION ADAPTIVE MOCK PAYLOAD DYNAMICALLY FROM OCR JSON
# ============================================================================

MODULE_1_QUESTIONS = build_rw_questions_from_ocr(
    RAW_JSON,
    'march2025_v3_rw_m1',
    1,
    27,
    M1_META,
    patches=M1_BUILD_PATCHES,
)
_reflow_and_patch(MODULE_1_QUESTIONS, M1_POST_PATCHES, bullet_qnums=(24, 25, 26, 27))

MODULE_2_QUESTIONS = build_rw_questions_from_ocr(
    RAW_JSON,
    'march2025_v3_rw_m2',
    28,
    54,
    M2_META,
    patches=M2_BUILD_PATCHES,
)
_reflow_and_patch(MODULE_2_QUESTIONS, M2_POST_PATCHES, bullet_qnums=(25, 26, 27), dual_qnums=(7,))

TEST_DATA = {
    'schemaVersion': 1,
    'mode': 'adaptive_mock',
    'section': 'rw',
    'basicInfo': {
        'title': TEST_TITLE,
        'subtitle': 'Đề thi thật Digital SAT tháng 3/2025 (Ver 3) — Đủ 2 Module (M1: 27 câu + M2: 27 câu)',
        'difficultyBadge': 'REAL EXAM • MARCH 2025',
        'targetTimeMinutes': 64,
        'routingThreshold': 0,
    },
    'module1': {
        'id': 'real_march2025_v3_rw_m1',
        'title': 'Section 1, Module 1: Reading and Writing',
        'subtitle': 'March 2025 Ver 3 Real Exam — Module 1 (27 Qs • 32 min)',
        'timeLimitMinutes': 32,
        'questions': MODULE_1_QUESTIONS,
    },
    'module2_hard': {
        'id': 'real_march2025_v3_rw_m2_hard',
        'title': 'Section 1, Module 2: Reading and Writing',
        'subtitle': 'March 2025 Ver 3 Real Exam — Module 2 (27 Qs • 32 min)',
        'timeLimitMinutes': 32,
        'questions': MODULE_2_QUESTIONS,
    },
    'module2_lower': {
        'id': 'real_march2025_v3_rw_m2_lower',
        'title': 'Section 1, Module 2: Reading and Writing',
        'subtitle': 'March 2025 Ver 3 Real Exam — Module 2 (27 Qs • 32 min)',
        'timeLimitMinutes': 32,
        'questions': _clone_module_questions(
            MODULE_2_QUESTIONS,
            'march2025_v3_rw_m2_',
            'march2025_v3_rw_m2l_',
        ),
    },
}


def verify_all():
    """Runs full structural, fidelity, watermark, answer/optionAnalysis, and Bluebook KaTeX checks."""
    from scripts.sat_qa_validator import validate_sat_test
    from scripts.sat_real_exams_pipeline import validate_sat_bluebook_json

    errors = []

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

    if TEST_DATA.get('mode') != 'adaptive_mock':
        errors.append(f"Expected mode='adaptive_mock', got {TEST_DATA.get('mode')}")
    if TEST_DATA.get('section') != 'rw':
        errors.append(f"Expected section='rw', got {TEST_DATA.get('section')}")
    if TEST_DATA['basicInfo'].get('routingThreshold') != 0:
        errors.append(f"Expected routingThreshold=0, got {TEST_DATA['basicInfo'].get('routingThreshold')}")
    if TEST_DATA['basicInfo'].get('targetTimeMinutes') != 64:
        errors.append(f"Expected targetTimeMinutes=64, got {TEST_DATA['basicInfo'].get('targetTimeMinutes')}")

    all_ids = set()
    for mod_key, qs in [('module1', m1_qs), ('module2_hard', m2h_qs), ('module2_lower', m2l_qs)]:
        for idx, q in enumerate(qs, start=1):
            qid = q['id']
            if qid in all_ids:
                errors.append(f'Duplicate global ID: {qid}')
            all_ids.add(qid)
            if q['number'] != idx:
                errors.append(f'{mod_key} Q{idx}: wrong number field {q["number"]}')

            opts = q.get('options') or []
            if len(opts) != 4 or [o.get('label') for o in opts] != ['A', 'B', 'C', 'D']:
                errors.append(f'{qid}: bad options structure')
            opt_texts = [o.get('text', '').strip() for o in opts]
            if any(not t for t in opt_texts) or len(set(t.lower() for t in opt_texts)) != 4:
                errors.append(f'{qid}: blank or duplicate options -> {opt_texts}')

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
            if not (exp.get('summaryVi') or '').strip():
                errors.append(f'{qid}: empty summaryVi')
            if not (exp.get('keyTakeaway') or '').strip():
                errors.append(f'{qid}: empty keyTakeaway')

            q_lower = (q['questionHtml'] or '').lower()
            stim = q['stimulusHtml'] or ''
            if 'table' in q_lower and '<table' not in stim.lower():
                errors.append(f'{qid}: question references table but stimulusHtml lacks <table>')
            if 'graph' in q_lower and '<svg' not in stim.lower():
                errors.append(f'{qid}: question references graph but stimulusHtml lacks <svg>')
            if 'underlined' in q_lower and '<u>' not in stim.lower():
                errors.append(f'{qid}: question references underlined text but stimulusHtml lacks <u>')
            if any(k in q_lower for k in ('completes the text', 'most logically completes')) and '_______' not in stim:
                errors.append(f'{qid}: fill-in-the-blank prompt missing _______ in stimulusHtml')

    for qh, ql in zip(m2h_qs, m2l_qs):
        for field in ('number', 'domain', 'skill', 'stimulusHtml', 'questionHtml', 'options', 'correctAnswer', 'explanation'):
            if qh[field] != ql[field]:
                errors.append(f'module2_lower Q{qh["number"]} differs from module2_hard on field {field}')

    serialized = json.dumps(TEST_DATA, ensure_ascii=False)
    if re.search(r'@dsatuz|dsatuz|@d7sat|d7sat|t\.me/', serialized, re.IGNORECASE):
        errors.append('Found watermark string in TEST_DATA!')
    if re.search(r'_{3,}blank', serialized, re.IGNORECASE):
        errors.append('Found unconverted ___blank artifact in TEST_DATA!')
    if '||BULLET||' in serialized or '||EXCERPT||' in serialized or '||TEXT2||' in serialized or '||COPY||' in serialized:
        errors.append('Found unconverted layout sentinel in TEST_DATA!')
    if '<i><i>' in serialized or '</i></i>' in serialized:
        errors.append('Found nested duplicate <i> tags in TEST_DATA!')

    errors.extend(validate_sat_test(TEST_DATA, TEST_CODE))
    errors.extend(validate_sat_bluebook_json(TEST_DATA, TEST_CODE))

    m1_dist = {c: sum(1 for q in m1_qs if q['correctAnswer'] == c) for c in 'ABCD'}
    m2_dist = {c: sum(1 for q in m2h_qs if q['correctAnswer'] == c) for c in 'ABCD'}
    print(f'[{TEST_CODE}] {TEST_TITLE}')
    print(f'  Module 1: {len(m1_qs)} Qs | Keys: {m1_dist}')
    print(f'  Module 2: {len(m2h_qs)} Qs | Keys: {m2_dist} (mirrored to module2_lower: {len(m2l_qs)} Qs)')
    print(f'  Total unique real Qs: {len(m1_qs) + len(m2h_qs)} | Global unique IDs: {len(all_ids)}')
    print(f'  Table verified: 1 (M1 Q13) | Chart SVGs verified: 2 (M1 Q12, M2 Q10) | Underlines verified: 2 (M1 Q2, M1 Q14)')

    if errors:
        print(f'  [FAILED] {len(errors)} error(s):')
        for e in errors:
            print(f'    - {e}')
        return False

    print('  [PASS] 0 errors — Bluebook schema, KaTeX, verbatim OCR fidelity & 2-pass audit verified!')
    return True


if __name__ == '__main__':
    ok = verify_all()
    sys.exit(0 if ok else 1)
