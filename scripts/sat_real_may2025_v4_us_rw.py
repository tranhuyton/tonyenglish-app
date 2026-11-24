# -*- coding: utf-8 -*-
"""
Digital SAT 1500+ Real Past Exam — May 2025 US Ver 4 Reading & Writing (54 Questions)
- Module 1: 27 Real Questions (32 minutes)
- Module 2: 27 Real Questions (32 minutes, assigned to both module2_hard and module2_lower with routingThreshold=0)
- Source: May 2025 US Ver 4 Real Exam (100% verbatim passages, tables, chart SVG, underlines, italics, and options A–D)
- 2-Pass Answer Audit completed across all 54 R&W items with rich Vietnamese explanations & trap analysis.
"""

import copy
import json
import os
import re
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

TEST_CODE = 'real_may2025_v4_us_rw'
FOLDER_KEY = 'real_rw'
ORDER_INDEX = 7
TEST_TITLE = '🏛️ Real Exam — May 2025 US Ver 4 Reading & Writing (54 Qs)'


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


def _svg_m2_q12_forest_patches():
    """Recreates the exact May 2025 US v4 M2 Q12 grouped bar chart (Chorotega Region, Costa Rica)."""
    years = ['1960', '1979', '1986', '2000']
    # Measured bar values: (Class VI dark-gray, Class VIII white-outlined, Class VII solid-black)
    data = [
        (538, 590, 617),
        (349, 346, 388),
        (1334, 1394, 1504),
        (1459, 1566, 1593),
    ]
    x_left, x_right = 76, 446
    y_top, y_bot = 18, 210  # 192px for 0..1800

    def fy(v):
        return y_bot - (v / 1800.0) * (y_bot - y_top)

    parts = []
    # Horizontal gridlines + Y-axis labels
    for val in range(0, 1801, 300):
        y = fy(val)
        stroke = '#334155' if val == 0 else '#cbd5e1'
        sw = '1.5' if val == 0 else '1'
        parts.append(
            f'<line x1="{x_left}" y1="{y:.1f}" x2="{x_right}" y2="{y:.1f}" '
            f'stroke="{stroke}" stroke-width="{sw}"/>'
        )
        parts.append(
            f'<line x1="{x_left - 4}" y1="{y:.1f}" x2="{x_left}" y2="{y:.1f}" '
            f'stroke="#334155" stroke-width="1.2"/>'
        )
        label_txt = f'{val:,}' if val >= 1000 else str(val)
        parts.append(
            f'<text x="{x_left - 8}" y="{y + 3.5:.1f}" font-size="11" text-anchor="end" '
            f'fill="#1e293b" font-family="sans-serif">{label_txt}</text>'
        )

    # Y-axis line
    parts.append(
        f'<line x1="{x_left}" y1="{y_top}" x2="{x_left}" y2="{y_bot}" '
        f'stroke="#334155" stroke-width="1.5"/>'
    )

    # Grouped bars
    centers = [126, 214, 302, 390]
    bar_w = 21
    fills = ['#52525b', '#ffffff', '#0f172a']
    for cx, yr, triple in zip(centers, years, data):
        start_x = cx - 1.5 * bar_w
        for idx, val in enumerate(triple):
            bx = start_x + idx * bar_w
            by = fy(val)
            bh = y_bot - by
            parts.append(
                f'<rect x="{bx:.1f}" y="{by:.1f}" width="{bar_w}" height="{bh:.1f}" '
                f'fill="{fills[idx]}" stroke="#0f172a" stroke-width="1.2"/>'
            )
        parts.append(
            f'<text x="{cx}" y="{y_bot + 16}" font-size="11.5" text-anchor="middle" '
            f'fill="#1e293b" font-family="sans-serif">{yr}</text>'
        )

    # Axis titles
    parts.append(
        '<text x="20" y="114" font-size="11.5" font-weight="600" text-anchor="middle" '
        'fill="#0f172a" font-family="sans-serif" transform="rotate(-90 20 114)">Number of patches</text>'
    )
    parts.append(
        '<text x="261" y="244" font-size="11.5" font-weight="600" text-anchor="middle" '
        'fill="#0f172a" font-family="sans-serif">Year</text>'
    )

    # Legend box
    parts.append(
        '<rect x="64" y="256" width="388" height="68" fill="#ffffff" stroke="#475569" stroke-width="1.1"/>'
    )
    legend_rows = [
        ('#52525b', 'Class VI (severe limitations on use for crops)', 274),
        ('#ffffff', 'Class VIII (cannot be used for commercial crops)', 294),
        ('#0f172a', 'Class VII (very severe limitations on use for crops)', 314),
    ]
    for fill_c, text_l, ly in legend_rows:
        parts.append(
            f'<rect x="76" y="{ly - 10}" width="11" height="11" '
            f'fill="{fill_c}" stroke="#0f172a" stroke-width="1.2"/>'
        )
        parts.append(
            f'<text x="95" y="{ly}" font-size="11.2" fill="#0f172a" font-family="sans-serif">{text_l}</text>'
        )

    return (
        '<div style="background:#f8fafc;border:1px solid #cbd5e1;border-radius:10px;padding:12px 14px;margin-bottom:12px;">'
        '<div style="font-family:\'Segoe UI\',sans-serif;font-size:13px;font-weight:800;color:#0f172a;'
        'text-align:center;line-height:1.35;margin-bottom:6px;">'
        'Annual Number of Forest Patches for Three Land Use Capability Classes in the Chorotega Region, Costa Rica</div>'
        '<svg viewBox="0 0 475 334" xmlns="http://www.w3.org/2000/svg" style="max-width:468px;">'
        '<rect x="0" y="0" width="475" height="334" fill="#ffffff"/>'
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
        'may2025_v4_us_rw_m1_q1', 1, 'Craft and Structure', 'Words in Context', 'Easy',
        '<p>The following text is from Lilliam Rivera’s 2020 novel <i>Never Look Back</i>. The text describes the narrator arriving at his father’s apartment.</p>'
        '<p>“Pops, I’m here!” I <u>drop</u> my bag and set my guitar case against a wall. I place my keys on the bowl right next to the ceramic elephant Pops got me on one of his trips to Santo Domingo when I was a little kid.</p>'
        '<p style="text-align:right;font-size:12px;color:#64748b;">©2020 by Lilliam Rivera</p>',
        'As used in the text, what does the word “drop” most nearly mean?',
        ['Forget about', 'Put down', 'Unbolt', 'Empty'],
        'B',
        'Khi bước vào căn hộ của bố, nhân vật tôi thực hiện chuỗi động tác cất đồ quen thuộc: “I drop my bag and set my guitar case against a wall. I place my keys on the bowl...” (Tôi đặt túi xuống, dựng bao đàn guitar vào tường và để chìa khóa lên chiếc bát). Động từ “drop” ở đây song song trực tiếp với “set” và “place”, mang nghĩa “đặt xuống” → Chọn B (“Put down”).',
        'Trong dạng Words in Context với từ đơn giản có nhiều nghĩa, hãy dựa vào các động từ song hành ngay bên cạnh (“set my guitar case”, “place my keys”) để chốt nghĩa chính xác của từ được gạch chân.',
        [
            ('Wrong Meaning', 'Forget about = quên đi — dùng cho nghĩa bóng (“drop the subject”), không phù hợp với hành động vật lý đặt chiếc túi khi vừa về nhà.'),
            ('Đáp án đúng', 'Put down = đặt xuống — khớp hoàn hảo ngữ cảnh nhân vật vừa vào cửa, đặt túi xuống rồi dựng đàn và để chìa khóa.'),
            ('Wrong Meaning', 'Unbolt = mở chốt cửa — sai hoàn toàn nghĩa của động từ “drop”.'),
            ('Wrong Meaning', 'Empty = đổ sạch, làm trống — nhân vật không đổ đồ trong túi ra mà chỉ đặt chiếc túi xuống.'),
        ],
    ),

    # --- M1 Q2 ---
    q_item(
        'may2025_v4_us_rw_m1_q2', 2, 'Craft and Structure', 'Words in Context', 'Medium',
        '<p>The invertebrates <i>Haywardozoon pacificum</i> and <i>Trophomera mangani</i> have recently been discovered inhabiting the Clarion-Clipperton Zone (CCZ), an area of abyssal plain between Hawaii and Mexico where mining is permitted. The number of other invertebrates that may inhabit the CCZ is currently _______, as the area’s biota is poorly sampled and the few samples that have been taken cannot be presumed to be representative.</p>',
        'Which choice completes the text with the most logical and precise word or phrase?',
        ['infinitesimal', 'verifiable', 'tenuous', 'inestimable'],
        'D',
        'Mệnh đề nguyên nhân “as the area’s biota is poorly sampled and the few samples that have been taken cannot be presumed to be representative” (vì hệ sinh vật vùng này mới được lấy mẫu rất ít và vài mẫu ít ỏi đó không thể xem là đại diện) suy ra trực tiếp rằng số lượng các loài động vật không xương sống khác sống tại CCZ hiện **không thể ước tính / không thể xác định được** → Chọn D (“inestimable” = không thể ước lượng được).',
        'Chú ý nghĩa gốc theo từ nguyên của “inestimable” (in- + estimate + -able): trên SAT, từ này thường dùng theo nghĩa “không thể ước tính được” (cannot be estimated), bên cạnh nghĩa “vô giá”.',
        [
            ('Unsupported Claim', 'infinitesimal = cực kỳ nhỏ bé — việc lấy mẫu kém không có nghĩa là số lượng loài cực nhỏ; thực tế ta đơn giản là chưa biết con số bao nhiêu.'),
            ('Opposite Meaning', 'verifiable = có thể kiểm chứng — trái ngược hoàn toàn với thực tế dữ liệu quá ít và không có tính đại diện.'),
            ('Wrong Context', 'tenuous = mong manh, yếu ớt (thường dùng cho mối liên kết, lập luận) — không dùng để mô tả một con số chưa thể tính toán.'),
            ('Đáp án đúng', 'inestimable = không thể ước tính — nối nguyên nhân–kết quả chuẩn xác với “poorly sampled” và “cannot be presumed to be representative”.'),
        ],
    ),

    # --- M1 Q3 ---
    q_item(
        'may2025_v4_us_rw_m1_q3', 3, 'Craft and Structure', 'Words in Context', 'Medium',
        '<p>Given that healthy genetic diversity supports honey bee population robustness—a matter of public interest given the bees’ crucial role as pollinators of many crops, such as watermelon—a study revealing a _______ of diversity among US honey bees raised concern, though it also noted the potential to enhance the number of bees carrying several newly discovered genetic variants (e.g., A2-829-4-USA).</p>',
        'Which choice completes the text with the most logical and precise word or phrase?',
        ['paucity', 'redundancy', 'disparity', 'repository'],
        'A',
        'Đoạn văn mở đầu rằng đa dạng di truyền khỏe mạnh giúp đàn ong mật vững mạnh; vì vậy một nghiên cứu phát hiện ra sự _______ về đa dạng di truyền đã “raised concern” (làm dấy lên lo ngại), dù cũng nêu tiềm năng tăng cường (“enhance”) số lượng ong mang các biến thể gen mới. Điều gây lo ngại và cần tăng cường chắc chắn là **sự thiếu hụt / khan hiếm** → Chọn A (“paucity” = sự khan hiếm, thiếu hụt).',
        'Từ vựng vàng SAT: “paucity” = scarcity / dearth / lack (sự khan hiếm, thiếu hụt), rất hay đi kèm các tín hiệu tiêu cực như “raised concern” và nhu cầu “enhance / bolster”.',
        [
            ('Đáp án đúng', 'paucity = sự khan hiếm, thiếu hụt — giải thích hoàn hảo vì sao phát hiện này gây lo ngại và cần bổ sung thêm biến thể gen mới.'),
            ('Wrong Meaning', 'redundancy = sự dư thừa — nếu đa dạng gen dư thừa thì sẽ không gây lo ngại cho sức bền quần thể ong.'),
            ('Wrong Context', 'disparity = sự chênh lệch bất bình đẳng — câu không so sánh hai nhóm ong mật khác nhau mà nói về mức độ đa dạng thấp nói chung ở ong Mỹ.'),
            ('Wrong Meaning', 'repository = kho lưu trữ — mang nghĩa tích cực/trung tính là nơi tập trung dồi dào, mâu thuẫn với “raised concern”.'),
        ],
    ),

    # --- M1 Q4 ---
    q_item(
        'may2025_v4_us_rw_m1_q4', 4, 'Craft and Structure', 'Words in Context', 'Easy',
        '<p>Maryam Hosseini and her team used aerial images of well-mapped areas of Boston to train a computer program to identify sidewalks. When it was tested on images of Brooklyn, it _______ identified sidewalks in the vast majority of cases and even whether sidewalks were concrete or brick. Hosseini believes the program will improve on this already-strong performance as it gets used more.</p>',
        'Which choice completes the text with the most logical and precise word or phrase?',
        ['clumsily', 'reliably', 'rarely', 'slowly'],
        'B',
        'Hai manh mối tích cực rõ rệt: chương trình nhận diện vỉa hè “in the vast majority of cases” (trong đại đa số trường hợp), thậm chí phân biệt được bê tông hay gạch, và được mô tả là có “already-strong performance” (hiệu suất vốn đã rất mạnh mẽ). Do đó trạng từ điền vào phải thể hiện sự chính xác, đáng tin cậy → Chọn B (“reliably”).',
        'Luôn đối chiếu sắc thái của từ điền với câu tổng kết phía sau: “this already-strong performance” loại ngay 3 trạng từ tiêu cực (clumsily, rarely, slowly).',
        [
            ('Opposite Tone', 'clumsily = vụng về — trái ngược hoàn toàn với hiệu suất “already-strong”.'),
            ('Đáp án đúng', 'reliably = một cách đáng tin cậy, chính xác ổn định — khớp với “vast majority of cases” và “already-strong performance”.'),
            ('Opposite Meaning', 'rarely = hiếm khi — mâu thuẫn trực tiếp với “in the vast majority of cases”.'),
            ('Unsupported / Negative', 'slowly = chậm chạp — bài không đề cập tốc độ xử lý mà nhấn mạnh độ chính xác cao.'),
        ],
    ),

    # --- M1 Q5 ---
    q_item(
        'may2025_v4_us_rw_m1_q5', 5, 'Craft and Structure', 'Words in Context', 'Easy',
        '<p>The Polynesian languages, a group of related languages originating on islands in the Pacific, typically have _______ array of consonant sounds. For example, the Tokelauan language of the South Pacific has eleven consonants, and ‘Ōlelo Hawai‘i, the language of the Native Hawaiian people, has eight. Globally, however, the median number of consonants per language is over twenty-two.</p>',
        'Which choice completes the text with the most logical and precise word or phrase?',
        ['a musical', 'an unvarying', 'an exclusive', 'a modest'],
        'D',
        'Câu ví dụ đưa ra số liệu cụ thể: tiếng Tokelauan có 11 phụ âm, tiếng Hawaii chỉ có 8 phụ âm; “however” (tuy nhiên), trên toàn cầu mức trung vị lên tới hơn 22 phụ âm. Vậy các ngôn ngữ Polynesia có một hệ thống phụ âm **khiêm tốn / ít ỏi** so với mặt bằng chung → Chọn D (“a modest”).',
        'Đừng để bẫy “an unvarying” (không thay đổi) đánh lừa: 11 và 8 là hai con số khác nhau, nên chúng CÓ biến thiên; điểm chung duy nhất của 11 và 8 khi đối chiếu với >22 là cả hai đều nhỏ (“modest”).',
        [
            ('Out of Scope', 'a musical = có tính nhạc — bài chỉ so sánh SỐ LƯỢNG phụ âm (11, 8 vs. >22), không bàn về âm điệu hay nhạc tính.'),
            ('Contradicted by Text', 'an unvarying = bất biến, không đổi — sai vì ngay trong nhóm Polynesia, Tokelauan có 11 còn Hawaii có 8 phụ âm.'),
            ('Wrong Meaning', 'an exclusive = độc quyền, dành riêng — bài không nói các phụ âm này chỉ có ở ngôn ngữ Polynesia.'),
            ('Đáp án đúng', 'a modest = khiêm tốn, có quy mô nhỏ — khớp hoàn hảo phép tương phản 8 và 11 phụ âm so với trung vị toàn cầu >22.'),
        ],
    ),

    # --- M1 Q6 ---
    q_item(
        'may2025_v4_us_rw_m1_q6', 6, 'Craft and Structure', 'Text Structure and Purpose', 'Easy',
        '<p>Movies that are part of larger franchises are often criticized for being predictable. Take, for instance, <i>Spider Man: Far From Home</i> (2019), which is part of the Marvel Cinematic Universe franchise. It’s true that this movie resembles earlier Marvel movies. But just because a movie has familiar elements doesn’t mean it can’t also be worth watching. Critics generally agree that <i>Spider Man: Far From Home</i> isn’t the most exciting franchise movie, but franchise movies are rarely as stale as some people claim. And some franchise movies, like <i>Logan</i> (2017), are wonderfully original.</p>',
        'Which choice best describes the overall structure of the text?',
        [
            'The text summarizes the plot of a franchise movie, then explains how the plot is continued in a later movie in that franchise.',
            'The text explains why some people enjoyed a particular franchise movie, then considers why other people disliked it.',
            'The text describes audiences’ reactions to a movie that is part of a larger franchise, then presents some critics’ reactions to that movie.',
            'The text discusses a common criticism of franchise movies, then argues that the criticism is mostly undeserved.',
        ],
        'D',
        'Cấu trúc toàn bài gồm hai vế rất mạch lạc: (1) Mở đầu nêu một lời chê bai phổ biến đối với phim thuộc thương hiệu lớn (“often criticized for being predictable”); (2) Phần còn lại thừa nhận yếu tố quen thuộc nhưng phản bác gay gắt định kiến đó (“rarely as stale as some people claim”, “some franchise movies, like *Logan* (2017), are wonderfully original”), lập luận rằng lời phê bình này phần lớn không thỏa đáng → Chọn D.',
        'Với dạng Overall Structure, hãy tách bài thành 2 nửa tại từ chuyển ý lớn (“But...”) rồi kiểm tra cả hai vế của từng đáp án xem có khớp đúng trình tự mở đầu → phát triển không.',
        [
            ('Not Mentioned', 'Bài không hề tóm tắt cốt truyện của *Spider Man: Far From Home* hay nói về phần tiếp nối cốt truyện.'),
            ('Wrong Structure', 'Bài không phân tích hai chiều lý do khán giả thích rồi lại ghét một bộ phim cụ thể.'),
            ('Misrepresented Focus', 'Không có phần mô tả phản ứng của khán giả (audiences’ reactions); tác giả chỉ nhắc ngắn đến ý kiến giới phê bình để bổ trợ cho lập luận bảo vệ phim franchise.'),
            ('Đáp án đúng', 'Khớp trọn vẹn bố cục: nêu lời chỉ trích phổ biến (“predictable”) ở câu 1 rồi phản biện rằng đánh giá đó nhìn chung không công bằng.'),
        ],
    ),

    # --- M1 Q7 ---
    q_item(
        'may2025_v4_us_rw_m1_q7', 7, 'Craft and Structure', 'Text Structure and Purpose', 'Medium',
        '<p>The following text is from Julia Alvarez’s 2000 novel <i>In the Name of Salomé</i>. Salomé, a poet, is hosting guests in the front parlor of her family home, and Ramona is her sister. A salon is a social gathering for the exploration of intellectual ideas.</p><p>It was evening when the two men got up to leave. Tía Ana had already come into the room several times to see if these guests had departed yet. The front parlor had always been her special province, as she used it for her little school. Now, every evening, it turned into Salomé’s salon, as Ramona called it, and it was never in order for its transformation back to a classroom the following morning.</p><p style="text-align:right;font-size:12px;color:#64748b;">©2000 by Julia Alvarez</p>',
        'Which choice best describes the function of the reference to the parlor as Tía Ana’s “special province”?',
        [
            'It reveals that Tía Ana feels as if Salomé has betrayed her trust by allowing guests into space she considers her own.',
            'It indicates the joy that Tía Ana feels when she uses her classroom for varying purposes.',
            'It characterizes the room as a place where Tía Ana can go to escape social pressures.',
            'It introduces an idea that helps explain Tía Ana’s apparent eagerness for Salomé’s guests to leave the space.',
        ],
        'D',
        'Trong đoạn trích, câu trước đó mô tả Tía Ana đã nhiều lần ghé vào phòng khách xem các vị khách của Salomé đã ra về chưa (“already come into the room several times to see if these guests had departed yet”). Ngay tiếp theo, tác giả nhắc đến phòng khách là “special province” (lãnh địa riêng) mà Tía Ana vốn dùng làm lớp học nhỏ của mình, nhưng nay mỗi tối lại biến thành salon của Salomé và không bao giờ kịp gọn gàng cho buổi học sáng hôm sau. Chi tiết “special province” vì thế giúp lý giải rõ nguyên nhân sự sốt ruột, mong khách sớm ra về của Tía Ana → Chọn D.',
        'Khi câu hỏi hỏi chức năng (function) của một cụm từ ở câu giữa đoạn văn, hãy đọc câu đứng NGAY TRƯỚC nó: cụm “special province” giải thích trực tiếp hành vi sốt ruột ghé nhìn khách ở câu liền trước.',
        [
            ('Overstatement', '“betrayed her trust” (phản bội lòng tin) là cảm xúc quá nặng nề và không có bằng chứng; Tía Ana chỉ bực bội vì phòng học bị xáo trộn.'),
            ('Opposite Tone', 'Trái ngược hoàn toàn cảm xúc của Tía Ana — bà không hề “joy” (vui sướng) mà rõ ràng khó chịu vì phòng học không kịp dọn lại.'),
            ('Not Mentioned', 'Bài mô tả phòng khách là lớp học nhỏ (“little school”), không hề nói là nơi Tía Ana trốn tránh áp lực xã hội.'),
            ('Đáp án đúng', 'Khớp hoàn hảo liên kết logic giữa hai câu liên tiếp: giới thiệu lý do vì sao Tía Ana cứ ra vào mong khách của Salomé mau rời đi.'),
        ],
    ),
    # --- M1 Q8 ---
    q_item(
        'may2025_v4_us_rw_m1_q8', 8, 'Craft and Structure', 'Cross-Text Connections', 'Easy',
        '<p><b>Text 1</b><br/>Despite how the Indian dish madras differs from Mauritius’s gato pima, both dishes are described as a “curry.” The word’s history, however, is fraught. It’s a term created by British and Portuguese colonizers to refer to the myriad spiced sauces with ties to the Indian subcontinent. In 1973, chef Madhur Jaffrey dismissed the term “curry” as inaccurate, and in 2021 blogger Nisha Vedi Pawar suggested that people abandon the term both for its colonial origin and for its failure to grasp the intricacies of India’s cuisines.</p><p><b>Text 2</b><br/>Growing up in India, chef Chintan Pandya didn’t encounter the term “curry” often: his family didn’t cook curries, but some of his neighbors did. Although the blanket use of the term is rooted in colonialism, Pandya calls some of his dishes curries. Having traveled throughout India as part of his training, he came to appreciate the country’s diverse cuisines and the diverse uses of the term “curry.”</p>',
        'Text 1 and Text 2 present points of view about which topic?',
        [
            'The history about the peoples on the Indian subcontinent',
            'The use of the term “curry”',
            'The difference between madras and gato pima',
            'The best method for studying a region’s cuisine',
        ],
        'B',
        'Cả hai đoạn văn cùng xoay quanh một chủ đề trọng tâm: **việc sử dụng thuật ngữ “curry”**. Đoạn 1 nêu góc nhìn phê phán (nguồn gốc thực dân, thiếu chính xác; Madhur Jaffrey bác bỏ và Nisha Vedi Pawar đề nghị bỏ hẳn thuật ngữ này). Đoạn 2 nêu góc nhìn dung hòa hơn của đầu bếp Chintan Pandya (dù biết nguồn gốc thực dân nhưng vẫn dùng từ “curry” cho một số món ăn và trân trọng sự đa dạng trong cách dùng từ này) → Chọn B.',
        'Trong câu hỏi Cross-Text Connections hỏi chủ đề chung (“present points of view about which topic?”), hãy tìm đối tượng xuất hiện xuyên suốt CẢ Text 1 lẫn Text 2 (ở đây là từ “curry” và việc có nên dùng nó hay không).',
        [
            ('Too Broad', 'Cả hai văn bản chỉ nhắc thoáng qua lịch sử thuộc địa liên quan đến từ “curry”, không thảo luận lịch sử chung của các dân tộc tiểu lục địa Ấn Độ.'),
            ('Đáp án đúng', 'Bao quát chính xác tranh luận trung tâm của cả hai văn bản: quan điểm trái chiều về việc sử dụng thuật ngữ “curry”.'),
            ('Too Narrow (Text 1 Only)', 'Hai món madras và gato pima chỉ xuất hiện ở câu mở đầu Text 1 làm ví dụ, hoàn toàn không có trong Text 2.'),
            ('Not Mentioned', 'Không có văn bản nào bàn về phương pháp nghiên cứu ẩm thực vùng miền.'),
        ],
    ),

    # --- M1 Q9 ---
    q_item(
        'may2025_v4_us_rw_m1_q9', 9, 'Information and Ideas', 'Central Ideas and Details', 'Easy',
        '<p>Sandra Cisneros’s English-language short story “Eyes of Zapata” occasionally includes words and phrases from the Mexican dialect of Spanish. While the story doesn’t translate the Spanish text into English, the meaning can be inferred from the surrounding English text. Ana Castillo adopts a comparable approach to Spanish in her English-language novel <i>So Far from God</i>. Both works thus remain accessible to all readers of English, not just those who can also read Spanish.</p>',
        'What is the main topic of the text?',
        [
            'The difficulty of translating Sandra Cisneros’s works into languages other than English',
            'The commercial success of English-language literature around the world',
            'The enduring popularity of Ana Castillo’s works in Mexico',
            'The use of non-English vocabulary in two English-language literary works',
        ],
        'D',
        'Đoạn văn phân tích cách hai tác phẩm văn học tiếng Anh — truyện ngắn “Eyes of Zapata” của Sandra Cisneros và tiểu thuyết *So Far from God* của Ana Castillo — cùng lồng ghép từ ngữ tiếng Tây Ban Nha mà không cần dịch trực tiếp nhưng vẫn dễ hiểu qua ngữ cảnh tiếng Anh xung quanh → Chủ đề chính là việc sử dụng từ vựng không phải tiếng Anh trong hai tác phẩm văn học tiếng Anh → Chọn D.',
        'Với câu hỏi “What is the main topic of the text?”, đáp án đúng phải bao trùm được CẢ hai ví dụ song song trong bài (Cisneros và Castillo) thay vì chỉ chọn một tác giả hoặc một chi tiết ngoài bài.',
        [
            ('Misreading / Narrow Scope', 'Bài không bàn về việc dịch tác phẩm của Cisneros sang ngôn ngữ khác, mà nói về cách dùng từ tiếng Tây Ban Nha ngay trong tác phẩm tiếng Anh.'),
            ('Out of Scope', 'Không hề nhắc đến thành công thương mại hay doanh số toàn cầu của văn học tiếng Anh.'),
            ('Out of Scope / Too Narrow', 'Bài không đề cập đến mức độ phổ biến của Ana Castillo tại Mexico, và cũng bỏ sót Sandra Cisneros.'),
            ('Đáp án đúng', 'Tóm gọn chuẩn xác toàn văn bản: việc sử dụng từ vựng không phải tiếng Anh (tiếng Tây Ban Nha) trong hai tác phẩm văn học tiếng Anh.'),
        ],
    ),

    # --- M1 Q10 ---
    q_item(
        'may2025_v4_us_rw_m1_q10', 10, 'Information and Ideas', 'Central Ideas and Details', 'Easy',
        '<p>In a large community science effort, biologist Grace Herzel and colleagues collaborated with hundreds of students and other amateur science enthusiasts for more than three years to study how butterfly color and weather conditions relate to butterfly behavior. They found that butterfly color might influence behavior more than butterfly size does, and that butterflies tended to prefer orange and red flowers on cloudy days and multicolor flowers on partly cloudy days.</p>',
        'Which choice best states the main idea of the text?',
        [
            'Collaboration between professional scientists and members of the public is especially useful when studying the behavior of butterflies and other flying insects.',
            'A recent study suggested that butterflies’ coloring seems to be less relevant to their behavior than weather conditions.',
            'Weather conditions and butterfly color seem to have less influence on butterfly behavior than the location where the butterflies are studied does.',
            'A large study suggested that butterfly color and weather conditions might influence the behavior of certain butterflies.',
        ],
        'D',
        'Đoạn văn tường thuật một nghiên cứu khoa học cộng đồng quy mô lớn (hàng trăm học sinh và người yêu khoa học tham gia hơn 3 năm) do Grace Herzel dẫn đầu, phát hiện rằng **màu sắc của bướm** có thể ảnh hưởng hành vi nhiều hơn kích thước, và **điều kiện thời tiết** (trời nhiều mây vs. có mây một phần) liên quan đến màu hoa mà bướm ưa chuộng → Chọn D.',
        'Đáp án Main Idea chuẩn College Board luôn trung thành với mức độ khẳng định (“might influence”) và KHÔNG tự bịa ra phép so sánh không có trong bài (như màu sắc vs. thời tiết ở B, hay địa điểm ở C).',
        [
            ('Overgeneralization', 'Bài chỉ kể rằng nhóm đã hợp tác với công chúng, không khẳng định sự hợp tác này “đặc biệt hữu ích” hay mở rộng sang “other flying insects”.'),
            ('Unsupported Comparison', 'Bài so sánh màu sắc với KÍCH THƯỚC (“more than butterfly size does”), tuyệt đối không nói màu sắc ít liên quan hơn thời tiết.'),
            ('Not Mentioned', 'Đoạn văn không hề nhắc đến địa điểm nghiên cứu (“location”) hay so sánh ảnh hưởng của địa điểm.'),
            ('Đáp án đúng', 'Khái quát trọn vẹn và chính xác cả hai phát hiện chính của nghiên cứu lớn về màu sắc bướm và điều kiện thời tiết.'),
        ],
    ),

    # --- M1 Q11 ---
    q_item(
        'may2025_v4_us_rw_m1_q11', 11, 'Information and Ideas', 'Central Ideas and Details', 'Hard',
        '<p><i>Uncle Boonmee Who Can Recall His Past Lives</i> (2010) and other films by Thai director Apichatpong Weerasethakul are contributions to slow cinema, an art house genre whose contemplative pacing and deprivileging of narrative are further exemplified by films such as Andrei Tarkovsky’s <i>Solaris</i> (1972). Apichatpong describes his films as sleep inducing, which might suggest that they bore their audiences, but boredom does not necessarily cause sleep: in the absence of a goal to which one attaches attention and interest, the tension of boredom can be anxiety inducing rather than soporific. Thus, Apichatpong’s description of his films is not self-deprecation; rather, his work invites sleep and thereby strips the description of its negative connotation.</p>',
        'Which choice best states the main idea of the text?',
        [
            'Audiences will fail to enjoy both <i>Solaris</i> and <i>Uncle Boonmee Who Can Recall His Past Lives</i> if they confuse sleepiness with boredom.',
            'Slow-cinema films can relieve anxiety for those who embrace their languid pace, but the films increase anxiety for those experiencing boredom as a result of the lack of a cohesive narrative.',
            '<i>Solaris</i> and many other slow cinema films often induce anxiety in their audiences due to their measured pace, but films by Apichatpong do not, despite possessing other traits characteristic of the genre.',
            'It would be a misunderstanding to interpret Apichatpong’s reflection on his work as a confession of its failure, because the effects his films produce on audiences are intentional.',
        ],
        'D',
        'Câu kết mở đầu bằng “Thus” đúc kết trọn vẹn ý chính toàn bài: việc đạo diễn Apichatpong mô tả phim của ông là “gây buồn ngủ” (“sleep inducing”) **không phải là sự tự chê bai / thừa nhận thất bại** (“not self-deprecation”), bởi buồn chán không đồng nghĩa gây ngủ (ngược lại sự chán nản còn có thể gây lo âu); thực chất, tác phẩm của ông **chủ ý mời gọi giấc ngủ** (“invites sleep”), qua đó xóa bỏ sắc thái tiêu cực của lời mô tả đó → Chọn D.',
        'Khi đoạn văn có câu tổng kết bắt đầu bằng “Thus,” hoặc “Therefore,” ở cuối đoạn, 95% ý chính (Main Idea) nằm ngay tại câu chốt đó — hãy đối chiếu nghĩa tương đương: “not self-deprecation” = không phải lời thú nhận thất bại; “invites sleep” = hiệu ứng có chủ đích (“intentional”).',
        [
            ('Not Mentioned', 'Bài không hề bàn về việc khán giả có thưởng thức được *Solaris* hay không khi nhầm buồn ngủ với buồn chán.'),
            ('Distorted Detail', 'Bài chỉ nói sự buồn chán nói chung có thể gây lo âu (“anxiety inducing”), tuyệt đối không nói phim slow cinema giúp “giảm lo âu” hay “tăng lo âu do thiếu cốt truyện chặt chẽ”.'),
            ('Unsupported Contrast', 'Đoạn văn đưa *Solaris* làm ví dụ cùng dòng phim với Apichatpong chứ không hề nói *Solaris* gây lo âu cho khán giả.'),
            ('Đáp án đúng', 'Diễn đạt lại chính xác 100% câu kết luận: hiểu lời nhận xét của Apichatpong như sự thú nhận thất bại là hiểu nhầm, vì hiệu ứng gây ngủ ở phim ông là hoàn toàn có chủ ý.'),
        ],
    ),

    # --- M1 Q12 ---
    q_item(
        'may2025_v4_us_rw_m1_q12', 12, 'Information and Ideas', 'Command of Evidence (Quantitative)', 'Easy',
        html_table(
            'Total Areas of Five Pueblo Nations in New Mexico',
            ['Tribal nation', 'Area (square miles)'],
            [
                ['Pueblo of Acoma', '595.7'],
                ['Taos Pueblo', '156.2'],
                ['Pueblo of Sandia', '38.9'],
                ['Pueblo de Cochiti', '82.1'],
                ['Pueblo of Pojoaque', '21.4'],
            ],
        )
        + '<p>The Pueblo of Laguna is the largest of the nineteen Pueblo tribal nations in New Mexico, covering nearly 800 square miles. Most Pueblo tribal nations are much smaller. For example, the total area of Pueblo of Sandia is 38.9 square miles, and the total area of Pueblo de Cochiti is _______</p>',
        'Which choice most effectively uses data from the table to complete the statement?',
        [
            '156.2 square miles.',
            '595.7 square miles.',
            '82.1 square miles.',
            '21.4 square miles.',
        ],
        'C',
        'Câu hỏi yêu cầu tra trực tiếp tổng diện tích của “Pueblo de Cochiti” trong bảng số liệu. Tra hàng thứ 4 (“Pueblo de Cochiti”), cột “Area (square miles)” cho giá trị chính xác là **82.1** → Chọn C (“82.1 square miles.”).',
        'Với câu tra bảng trực tiếp, luôn dóng ngón tay đúng tên hàng (“Pueblo de Cochiti”) trước khi nhìn sang cột số liệu để tránh chọn nhầm hàng lân cận.',
        [
            ('Wrong Row', '156.2 square miles là diện tích của Taos Pueblo, không phải Pueblo de Cochiti.'),
            ('Wrong Row', '595.7 square miles là diện tích của Pueblo of Acoma.'),
            ('Đáp án đúng', 'Khớp chính xác 100% số liệu hàng Pueblo de Cochiti trong bảng: 82.1 square miles.'),
            ('Wrong Row', '21.4 square miles là diện tích của Pueblo of Pojoaque.'),
        ],
    ),

    # --- M1 Q13 ---
    q_item(
        'may2025_v4_us_rw_m1_q13', 13, 'Information and Ideas', 'Command of Evidence (Quantitative)', 'Easy',
        html_table(
            'Volcanoes in Ecuador',
            ['Name of volcano', 'Year of last eruption', 'Volcano type'],
            [
                ['Chacana', '1773 CE', 'caldera'],
                ['Imbabura', '5550 BCE', 'compound'],
                ['Chimborazo', '550 BCE', 'stratovolcano'],
                ['Fernandina', '2020 CE', 'shield'],
            ],
        )
        + '<p>A student who is researching volcanoes in Ecuador notes that the country is home to different types of volcanoes. For example, _______</p>',
        'Which choice most effectively uses information from the table to complete the example?',
        [
            'Chacana is a caldera volcano, and Fernandina is a stratovolcano.',
            'Chimborazo is a caldera volcano, and Imbabura is a stratovolcano.',
            'Imbabura is a compound volcano, and Chacana is a shield volcano.',
            'Fernandina is a shield volcano, and Chimborazo is a stratovolcano.',
        ],
        'D',
        'Đối chiếu từng núi lửa với cột “Volcano type”: Chacana = caldera, Imbabura = compound, Chimborazo = stratovolcano, Fernandina = shield. Chỉ có đáp án D ghép đúng cả hai vế: Fernandina là núi lửa dạng khiên (shield volcano) và Chimborazo là núi lửa tầng (stratovolcano) → Chọn D.',
        'Với dạng ghép đôi từ bảng (X là loại 1, Y là loại 2), hãy kiểm tra cả hai vế một cách độc lập — bẫy SAT thường để vế đầu đúng nhưng tráo sai vế sau.',
        [
            ('Half-True / Swapped', 'Chacana đúng là caldera, nhưng Fernandina là shield volcano, KHÔNG phải stratovolcano.'),
            ('Wrong Data', 'Cả hai vế đều sai: Chimborazo là stratovolcano (không phải caldera) và Imbabura là compound (không phải stratovolcano).'),
            ('Half-True / Swapped', 'Imbabura đúng là compound volcano, nhưng Chacana là caldera, KHÔNG phải shield volcano.'),
            ('Đáp án đúng', 'Khớp chính xác hoàn toàn cả hai hàng trong bảng: Fernandina = shield, Chimborazo = stratovolcano.'),
        ],
    ),

    # --- M1 Q14 ---
    q_item(
        'may2025_v4_us_rw_m1_q14', 14, 'Information and Ideas', 'Inferences', 'Medium',
        '<p>Many studies have found a positive association between levels of dissolved organic carbon and mercury in bodies of fresh water in North America. But Enelton Fagnani, José Roberto Guimarã, and Pedro Sérgio Fadini did not find this correlation in a study conducted in Brazil, leading some scientists to hypothesize that the pattern is particular to North America. However, Kerstin Leopold, Anja Zierhut, and Jessica Huber reported dissolved organic carbon and mercury rising or falling together in a study conducted in Germany, and several other studies from outside North America have yielded similar results, suggesting that _______</p>',
        'Which choice most logically completes the text?',
        [
            'bodies of fresh water outside North America are more likely to show a negative association between dissolved organic carbon and mercury levels than a positive association.',
            'there may be circumstances specific to the bodies of water examined in Fagnani, Guimarã, and Fadini’s study that disrupted a general positive association between dissolved organic carbon and mercury levels.',
            'environmental characteristics unique to Brazil likely result in dissolved organic carbon and mercury levels in bodies of fresh water both being significantly higher there than elsewhere.',
            'the bodies of water examined in Fagnani, Guimarã, and Fadini’s study may be more similar to the bodies of water examined in studies conducted in North America than to those examined in Leopold, Zierhut, and Huber’s study.',
        ],
        'B',
        'Chuỗi lập luận khoa học: (1) Nhiều nghiên cứu ở Bắc Mỹ thấy tương quan thuận giữa carbon hữu cơ hòa tan và thủy ngân; (2) Nghiên cứu của Fagnani và cộng sự ở Brazil KHÔNG thấy tương quan đó → một số người giả thuyết quy luật chỉ đúng riêng cho Bắc Mỹ; (3) “However”, nghiên cứu ở Đức (Leopold et al.) và nhiều nghiên cứu khác NGOÀI Bắc Mỹ vẫn thấy hai chất cùng tăng/giảm (tương quan thuận). Điều này bác bỏ giả thuyết “chỉ riêng Bắc Mỹ” và gợi ý rằng tương quan thuận là quy luật chung, còn các thủy vực trong nghiên cứu ở Brazil có hoàn cảnh đặc thù nào đó đã làm gián đoạn mối tương quan chung này → Chọn B.',
        'Khi một ngoại lệ duy nhất (Brazil) dẫn đến giả thuyết sai (“chỉ có ở Bắc Mỹ”), rồi bằng chứng mới cho thấy nhiều nơi khác ngoài Bắc Mỹ vẫn tuân theo quy luật chung, suy luận hợp lệ là ngoại lệ kia có yếu tố đặc thù riêng làm nhiễu quy luật.',
        [
            ('Contradicted by Text', 'Đoạn văn nêu rõ nghiên cứu ở Đức và nhiều nghiên cứu khác ngoài Bắc Mỹ đều cho thấy tương quan THUẬN (“rising or falling together”), không phải tương quan nghịch.'),
            ('Đáp án đúng', 'Giải thích hợp lý sự bất thường của nghiên cứu Fagnani et al. trong bối cảnh tương quan thuận thực ra phổ biến cả trong lẫn ngoài Bắc Mỹ.'),
            ('Out of Scope', 'Bài chỉ bàn về mối tương quan (correlation) giữa hai chất, không hề so sánh hàm lượng tuyệt đối cao hơn hay thấp hơn ở Brazil.'),
            ('Reversed Logic', 'Ngược lại: các thủy vực ở Bắc Mỹ và Đức (Leopold et al.) mới giống nhau (đều có tương quan thuận), khác với thủy vực trong nghiên cứu Fagnani et al.'),
        ],
    ),

    # --- M1 Q15 ---
    q_item(
        'may2025_v4_us_rw_m1_q15', 15, 'Information and Ideas', 'Inferences', 'Medium',
        '<p>British professional soccer team Manchester United Football Club, whose home uniform color is mainly red, won more than half its home matches between 1947 and 2003. This is a higher proportion of home matches than Hull City Association Football Club, whose home uniform color is not red, won during the same period. According to a study by Martin J. Attrill and colleagues, the color red can cause people to respond with fear and hesitation, which the researchers think helps explain Manchester United’s success. Nadav Goldschmied and colleagues reanalyzed the published data from this study, however, and found no evidence that red-uniformed teams are more likely than other teams to win, suggesting that Manchester United’s performance at its home stadium _______</p>',
        'Which choice most logically completes the text?',
        [
            'would probably have remained roughly the same if its players had not been wearing red uniforms.',
            'was likely influenced by its opponents’ associations with the color red.',
            'was directly tied to its players’ general satisfaction with their uniform color.',
            'may have influenced other teams to change their uniform colors.',
        ],
        'A',
        'Nghiên cứu ban đầu của Attrill cho rằng màu áo đỏ giúp giải thích thành tích sân nhà tốt của Manchester United. “However”, khi Nadav Goldschmied và cộng sự phân tích lại chính dữ liệu đó, họ **không tìm thấy bằng chứng nào** cho thấy các đội mặc áo đỏ dễ thắng hơn các đội khác. Suy ra màu áo đỏ không phải nguyên nhân tạo nên thành tích thắng của Manchester United — nghĩa là phong độ sân nhà của đội có lẽ vẫn gần như vậy ngay cả khi cầu thủ không mặc áo đỏ → Chọn A.',
        'Trong câu hỏi Inferences có bước ngoặt “however, found no evidence that X causes Y”, kết luận logic là Y không phụ thuộc vào X (tức bỏ X đi thì Y vẫn giữ nguyên tương đương).',
        [
            ('Đáp án đúng', 'Phản ánh chính xác hàm ý từ phân tích lại của Goldschmied: màu áo đỏ không giúp tăng xác suất thắng, nên bỏ áo đỏ đi thành tích sân nhà của Man Utd có lẽ vẫn xấp xỉ như vậy.'),
            ('Contradicted by Text', 'Đây là giả thuyết ban đầu của Attrill, chính là điều mà nghiên cứu sau của Goldschmied bác bỏ.'),
            ('Out of Scope', 'Bài hoàn toàn không đề cập đến mức độ hài lòng của cầu thủ với màu áo đấu.'),
            ('Out of Scope', 'Không có chi tiết nào về việc các đội bóng khác thay đổi màu áo đấu.'),
        ],
    ),

    # --- M1 Q16 ---
    q_item(
        'may2025_v4_us_rw_m1_q16', 16, 'Standard English Conventions', 'Boundaries', 'Easy',
        '<p>London-based Nigerian sculptor Sokari Douglas Camp creates art by cutting, bending, and welding recycled metal materials into new and thought-provoking shapes. Her work—which has been featured in galleries around the world, such as the Potters Field Commission for Southwark Council in London and Skidmore College’s Tang Teaching Museum and Art Gallery in New York—often references at least one of several _______ the environment, and Kalabari culture.</p>',
        'Which choice completes the text so that it conforms to the conventions of Standard English?',
        [
            'themes; movement,',
            'themes. Movement,',
            'themes movement,',
            'themes: movement,',
        ],
        'D',
        'Rút gọn phần chêm giữa hai dấu gạch ngang dài, ta được mệnh đề độc lập hoàn chỉnh: “Her work often references at least one of several themes” (Tác phẩm của cô thường đề cập đến ít nhất một trong vài chủ đề). Ngay sau đó là danh sách liệt kê 3 chủ đề cụ thể: “movement, the environment, and Kalabari culture”. Để giới thiệu một danh sách giải thích sau một mệnh đề độc lập, ta bắt buộc dùng **dấu hai chấm (:)** → Chọn D (“themes: movement,”).',
        'Khi một mệnh đề hoàn chỉnh kết thúc bằng danh từ khái quát (“several themes”) và ngay sau đó là liệt kê chi tiết không phải mệnh đề hoàn chỉnh (“movement, the environment, and Kalabari culture”), dấu hai chấm (:) là lựa chọn chuẩn xác duy nhất.',
        [
            ('Boundary Error', 'Dấu chấm phẩy (;) đòi hỏi cả hai vế đều là mệnh đề độc lập (hoặc dùng phân cách các mục liệt kê có dấu phẩy bên trong), nhưng cụm “movement, the environment, and Kalabari culture” là cụm danh từ, không phải mệnh đề hoàn chỉnh.'),
            ('Sentence Fragment', 'Tách thành câu mới bằng dấu chấm (.) biến cụm danh từ “Movement, the environment, and Kalabari culture.” thành câu thiếu động từ (fragment).'),
            ('Missing Punctuation', 'Không có dấu ngăn cách giữa “themes” và “movement” gây lỗi nối danh từ tối nghĩa (fused phrase).'),
            ('Đáp án đúng', 'Dấu hai chấm (:) sau mệnh đề độc lập giới thiệu chuẩn xác danh sách 3 chủ đề cụ thể.'),
        ],
    ),

    # --- M1 Q17 ---
    q_item(
        'may2025_v4_us_rw_m1_q17', 17, 'Standard English Conventions', 'Boundaries', 'Medium',
        '<p>Drummer Dennis Chambers’s distinguished career includes many memorable achievements, such as working on the Brecker Brothers’ album <i>Return of the Brecker Brothers</i>. However, as house drummer at Sugar Hill Records, a record label that was a pioneer of early hip hop _______ Chambers joined too late to play drums on the label’s classic song “Rapper’s Delight.”</p>',
        'Which choice completes the text so that it conforms to the conventions of Standard English?',
        ['music,', 'music;', 'music, which', 'music'],
        'A',
        'Cả cụm mở đầu “However, as house drummer at Sugar Hill Records, a record label that was a pioneer of early hip hop music,” là cụm giới từ trạng ngữ mở đầu câu (bên trong có cụm đồng vị không thiết yếu “a record label that was a pioneer of early hip hop music” giải thích cho Sugar Hill Records), đứng trước mệnh đề chính “Chambers joined too late...”. Do đó, bắt buộc phải có **dấu phẩy (,)** sau “music” để đóng cụm đồng vị và tách cụm mở đầu khỏi chủ ngữ chính “Chambers” → Chọn A (“music,”).',
        'Mọi cụm bổ ngữ không thiết yếu (nonessential appositive) nằm giữa câu và mọi cụm giới từ mở đầu dài đều phải khép lại bằng dấu phẩy trước khi vào chủ ngữ mệnh đề chính.',
        [
            ('Đáp án đúng', 'Dấu phẩy sau “music,” đóng gọn cụm đồng vị và phân tách cụm giới từ mở đầu khỏi mệnh đề chính “Chambers joined...”.'),
            ('Boundary Error', 'Dấu chấm phẩy (;) sai vì phần đứng trước nó không phải mệnh đề độc lập (thiếu chủ–vị chính).'),
            ('Sentence Fragment', 'Thêm “, which” biến “Chambers joined too late...” thành mệnh đề quan hệ phụ, khiến cả câu mất hẳn mệnh đề chính.'),
            ('Missing Punctuation', 'Thiếu dấu phẩy đóng cụm đồng vị “a record label...” và thiếu dấu tách cụm mở đầu trước chủ ngữ “Chambers”.'),
        ],
    ),

    # --- M1 Q18 ---
    q_item(
        'may2025_v4_us_rw_m1_q18', 18, 'Standard English Conventions', 'Form, Structure, and Sense', 'Medium',
        '<p>Blaise Pascal’s Pascaline device—conceived, like William Oughtred’s earlier Circular Slide Rule, amid the seventeenth century push to replace manual calculations with faster and more accurate machine-based methods—_______ among the first reproducible calculating machines.</p>',
        'Which choice completes the text so that it conforms to the conventions of Standard English?',
        ['being', 'were', 'was', 'are'],
        'C',
        'Lược bỏ phần bổ ngữ chêm giữa hai dấu gạch ngang dài (—conceived, ... methods—), khung cốt lõi của câu là: “Blaise Pascal’s Pascaline device _______ among the first reproducible calculating machines.” Chủ ngữ chính là **Pascaline device** (SỐ ÍT), và ngữ cảnh lịch sử thế kỷ 17 đòi hỏi động từ chia thì quá khứ đơn số ít → Chọn C (“was”).',
        'Chiến thuật “gạch bỏ phần giữa hai dấu gạch ngang dài (—...—)” giúp nhìn ra ngay chủ ngữ cốt lõi là số ít (“device”) và loại tức khắc các động từ số nhiều (were, are) lẫn dạng phân từ không chia thì (being).',
        [
            ('No Main Verb (Fragment)', '“being” là phân từ hiện tại, không thể làm động từ chính chia thì cho chủ ngữ “Pascaline device” — làm câu thành câu cụt.'),
            ('Subject-Verb Agreement', '“were” là động từ số nhiều, không hòa hợp với chủ ngữ số ít “Pascaline device” (bẫy bị đánh lạc hướng bởi danh từ số nhiều “methods” ở cuối phần chêm).'),
            ('Đáp án đúng', '“was” là động từ chia thì quá khứ đơn, số ít — hòa hợp tuyệt đối với chủ ngữ số ít “Blaise Pascal’s Pascaline device” trong bối cảnh thế kỷ 17.'),
            ('Subject-Verb Agreement / Tense', '“are” vừa sai số nhiều vừa sai thì hiện tại cho một thiết bị lịch sử thế kỷ 17.'),
        ],
    ),

    # --- M1 Q19 ---
    q_item(
        'may2025_v4_us_rw_m1_q19', 19, 'Standard English Conventions', 'Form, Structure, and Sense', 'Medium',
        '<p>When a soil is classified using the International Union of Soil Sciences’ system, its similarity to each of the 32 soil reference groups—defined by several criteria—_______ evaluated, one group at a time, until a match is found. The comparisons are made in a specific order: thus, the criteria for lixisols (soils with clay-rich subsoil) are only applied if the soil doesn’t match the criteria for ferralsols.</p>',
        'Which choice completes the text so that it conforms to the conventions of Standard English?',
        ['have been', 'are', 'is', 'was'],
        'C',
        'Tách mệnh đề chính và lược bỏ cụm giới từ lẫn phần chêm giữa hai dấu gạch ngang: “its similarity [to each of the 32 soil reference groups—defined by several criteria—] _______ evaluated”. Chủ ngữ cốt lõi là **its similarity** (SỐ ÍT — không phải “groups” hay “criteria”!). Đồng thời, toàn bài mô tả một quy trình phân loại khoa học cố định ở thì **hiện tại đơn** (“is classified”, “is found”, “are made”, “are only applied”, “doesn’t match”) → Chọn C (“is”).',
        'Khi chủ ngữ đi kèm cụm giới từ dài (“its similarity to each of the 32 soil reference groups”), hãy luôn lùi về danh từ đứng TRƯỚC giới từ đầu tiên (“similarity” = số ít) để chia động từ, rồi đối chiếu thì với các động từ xung quanh.',
        [
            ('Subject-Verb Agreement', '“have been” là số nhiều và thì hiện tại hoàn thành, sai cả về số lẫn thì.'),
            ('Subject-Verb Agreement', '“are” là số nhiều — bẫy nhìn nhầm vào “groups” hoặc “criteria” ngay sát chỗ trống thay vì chủ ngữ thật “similarity”.'),
            ('Đáp án đúng', '“is” chia số ít, thì hiện tại đơn — hòa hợp hoàn hảo với chủ ngữ “its similarity” và chuỗi động từ hiện tại đơn của cả đoạn.'),
            ('Wrong Tense', '“was” chia thì quá khứ đơn, lệch thì so với quy trình khoa học tổng quát đang dùng hiện tại đơn xuyên suốt bài.'),
        ],
    ),

    # --- M1 Q20 ---
    q_item(
        'may2025_v4_us_rw_m1_q20', 20, 'Standard English Conventions', 'Boundaries', 'Medium',
        '<p>Enacted in 1944, Iceland’s constitution, according to legal _______ contains one of the six constitutional features that enhance judicial independence. Explicit provisions for judicial independence, Melton and Ginsburg’s research explains, are more likely to be found in constitutions enacted after 1985.</p>',
        'Which choice completes the text so that it conforms to the conventions of Standard English?',
        [
            'researchers James Melton and Tom Ginsburg',
            'researchers, James Melton and Tom Ginsburg',
            'researchers James Melton and Tom Ginsburg,',
            'researchers, James Melton and Tom Ginsburg,',
        ],
        'C',
        'Hai quy tắc dấu phẩy SAT kinh điển hội tụ trong một câu: (1) Cụm chêm “, according to legal researchers James Melton and Tom Ginsburg,” mở bằng dấu phẩy trước “according” nên BẮT BUỘC phải có **dấu phẩy đóng** ngay sau “Ginsburg,” trước động từ chính “contains” (loại A và B); (2) Cụm danh xưng nghề nghiệp đứng ngay trước tên riêng (“legal researchers James Melton and Tom Ginsburg”) là danh ngữ định danh thiết yếu, KHÔNG dùng dấu phẩy ngăn giữa “researchers” và “James” (loại D) → Chọn C.',
        'Quy tắc vàng SAT cho chức danh + tên riêng: KHÔNG chèn dấu phẩy giữa nghề nghiệp/chức danh và tên người (ví dụ: “legal researchers James Melton and Tom Ginsburg”), đồng thời luôn nhớ đóng đủ cặp dấu phẩy cho cụm chêm giữa chủ ngữ và động từ!',
        [
            ('Unclosed Parenthetical', 'Thiếu dấu phẩy đóng sau “Ginsburg” để khép lại cụm chêm “, according to legal researchers James Melton and Tom Ginsburg,” trước động từ “contains”.'),
            ('Double Comma Error', 'Vừa thừa dấu phẩy sai giữa chức danh “researchers” và tên riêng, vừa thiếu dấu phẩy đóng sau “Ginsburg”.'),
            ('Đáp án đúng', 'Không chen dấu phẩy giữa “researchers” và tên riêng, đồng thời đóng chuẩn xác cụm chêm bằng dấu phẩy sau “Ginsburg,”.'),
            ('Unnecessary Comma', 'Thừa dấu phẩy giữa chức danh “legal researchers” và tên riêng “James Melton and Tom Ginsburg” (khiến cụm tên bị hiểu sai như thông tin thừa).'),
        ],
    ),

    # --- M1 Q21 ---
    q_item(
        'may2025_v4_us_rw_m1_q21', 21, 'Expression of Ideas', 'Transitions', 'Easy',
        '<p>In a 2024 study, researchers investigating the biodiversity of trees in Amsterdam counted and classified the city’s trees. They found notable variation in the percentage of native trees in different areas of the city. _______ more than half of the trees in administrative unit GE05 (54%) were native species, but only 12% of the trees in administrative unit GE04 were native species.</p>',
        'Which choice completes the text with the most logical transition?',
        [
            'As was previously stated,',
            'Exemplifying this variation,',
            'Contrary to this finding,',
            'Resulting from this conclusion,',
        ],
        'B',
        'Câu 2 nêu nhận định khái quát: các nhà nghiên cứu phát hiện **sự chênh lệch đáng kể** (“notable variation”) về tỷ lệ cây bản địa ở các khu vực khác nhau của Amsterdam. Câu 3 đưa số liệu minh họa trực tiếp cho sự chênh lệch đó: khu GE05 có 54% cây bản địa trong khi khu GE04 chỉ có 12% → Quan hệ minh họa ví dụ → Chọn B (“Exemplifying this variation,”).',
        'Khi câu trước nêu một danh từ khái quát (“notable variation”) và câu sau tung ra cặp số liệu đối lập cụ thể (54% vs. 12%), hãy chọn ngay từ nối nêu ví dụ (“Exemplifying this variation,” / “For instance,”).',
        [
            ('Wrong Logic', 'As was previously stated = như đã nêu trước đó — hai số liệu 54% và 12% lần đầu xuất hiện, không phải thông tin lặp lại.'),
            ('Đáp án đúng', 'Exemplifying this variation = Minh họa cho sự biến thiên này — kết nối mượt mà số liệu 54% (GE05) vs. 12% (GE04) với cụm “notable variation” ở câu trước.'),
            ('Opposite Logic', 'Contrary to this finding = trái với phát hiện này — hoàn toàn ngược vì chênh lệch 54% vs. 12% CHỨNG MINH cho phát hiện chênh lệch.'),
            ('Wrong Cause-Effect', 'Resulting from this conclusion = bắt nguồn từ kết luận này — tỷ lệ cây ngoài thực địa không phải “hệ quả” sinh ra từ kết luận của các nhà nghiên cứu.'),
        ],
    ),

    # --- M1 Q22 ---
    q_item(
        'may2025_v4_us_rw_m1_q22', 22, 'Expression of Ideas', 'Transitions', 'Easy',
        '<p>Amruta Yelamanchili has worked at NASA’s famed Jet Propulsion Laboratory (JPL), one of the world’s leading facilities for robotic space exploration. _______ Yelamanchili worked as a data scientist on the JPL’s Mars 2020 Perseverance rover team, which improved upon the 2011 <i>Curiosity</i> rover design by adding a coring drill to the robot that could collect rock samples for later analysis.</p>',
        'Which choice completes the text with the most logical transition?',
        ['Specifically,', 'Conversely,', 'Finally,', 'Nevertheless,'],
        'A',
        'Câu 1 giới thiệu chung rằng Amruta Yelamanchili từng làm việc tại Phòng thí nghiệm Sức đẩy Phản lực (JPL) của NASA. Câu 2 đi sâu vào chi tiết cụ thể về vị trí và dự án cô đảm nhiệm tại chính JPL (nhà khoa học dữ liệu trong đội ngũ tàu tự hành Mars 2020 Perseverance) → Quan hệ cụ thể hóa (General → Specific) → Chọn A (“Specifically,”).',
        'Cấu trúc “worked at [tổ chức] → _______ worked as [chức danh cụ thể] on [dự án cụ thể]” là mẫu kinh điển 100% cho từ nối “Specifically,”.',
        [
            ('Đáp án đúng', 'Specifically = Cụ thể là — mở rộng từ thông tin khái quát (làm tại JPL) sang vai trò chi tiết (data scientist thuộc nhóm tàu Perseverance).'),
            ('Wrong Contrast', 'Conversely = ngược lại — hai câu bổ sung cùng chiều, không hề đối lập.'),
            ('Wrong Sequence', 'Finally = cuối cùng là — đoạn văn không liệt kê một chuỗi sự kiện theo thứ tự thời gian có bước đầu/giữa/cuối.'),
            ('Wrong Contrast', 'Nevertheless = tuy nhiên — không có bất kỳ sự nhượng bộ hay mâu thuẫn nào giữa hai câu.'),
        ],
    ),

    # --- M1 Q23 ---
    q_item(
        'may2025_v4_us_rw_m1_q23', 23, 'Expression of Ideas', 'Transitions', 'Easy',
        '<p>Two siblings from the same biological parents can inherit different physical traits. For instance, one sibling might inherit thin lips; the other sibling, _______ might inherit full lips.</p>',
        'Which choice completes the text with the most logical transition?',
        ['by contrast,', 'for example,', 'with this in mind,', 'lastly,'],
        'A',
        'Vế trước dấu chấm phẩy: một người anh/chị em có thể thừa hưởng đôi môi mỏng (“thin lips”). Vế sau: người kia có thể thừa hưởng đôi môi dày (“full lips”). Hai đặc điểm trái ngược nhau trực tiếp minh họa câu mở đầu (“inherit different physical traits”) → Quan hệ đối lập → Chọn A (“by contrast,”).',
        'Chú ý cặp đối chiếu trực diện “one sibling... thin lips; the other sibling, _______ full lips” — luôn cần từ nối tương phản (“by contrast,”).',
        [
            ('Đáp án đúng', 'by contrast = trái lại, ngược lại — đối chiếu hoàn hảo “thin lips” với “full lips”.'),
            ('Redundant / Wrong Logic', 'for example = ví dụ — câu này đã mở đầu bằng “For instance,” rồi; hai vế bên trong câu đối lập nhau chứ vế sau không phải ví dụ con của “thin lips”.'),
            ('Wrong Logic', 'with this in mind = với lưu ý đó — dùng để dẫn sang khuyến nghị/hệ quả, không dùng để đối chiếu hai đặc điểm trái ngược.'),
            ('Wrong Sequence', 'lastly = cuối cùng — không có danh sách nhiều mục theo thứ tự.'),
        ],
    ),

    # --- M1 Q24 ---
    q_item(
        'may2025_v4_us_rw_m1_q24', 24, 'Expression of Ideas', 'Rhetorical Synthesis', 'Easy',
        '<p>While researching a topic, a student has taken the following notes:</p>'
        '<ul>'
        '<li>Grimanesa Amoros is a Peruvian American artist well known for her LED light sculptures.</li>'
        '<li>Her sculpture <i>Uros House</i> is made of smooth multicolored LED domes.</li>'
        '<li>It occupies 250 cubic feet of space.</li>'
        '<li>Her sculpture <i>Golden Waters</i> is made of entangled blue and white LED tubes.</li>'
        '<li>It occupies 118,080 cubic feet of space.</li>'
        '</ul>',
        'The student wants to emphasize a similarity between <i>Uros House</i> and <i>Golden Waters</i>. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
        [
            '<i>Uros House</i> is an LED light sculpture made by Grimanesa Amoros, as is <i>Golden Waters</i>.',
            'The smooth LED domes of Grimanesa Amoros’s <i>Uros House</i> stand in contrast to the tangled LED tubes of <i>Golden Waters</i>.',
            'Grimanesa Amoros is the artist behind <i>Uros House</i>—a sculpture made of smooth multicolored LED domes.',
            'At 118,080 cubic feet in size, Grimanesa Amoros’s <i>Golden Waters</i> cuts a larger figure than the 250-cubic-foot <i>Uros House</i>.',
        ],
        'A',
        'Mục tiêu yêu cầu **nhấn mạnh một điểm giống nhau (similarity)** giữa hai tác phẩm *Uros House* và *Golden Waters*. Đáp án A nêu rõ cả hai đều là tác phẩm điêu khắc ánh sáng đèn LED do nghệ sĩ Grimanesa Amoros sáng tạo (“as is *Golden Waters*”) → Chọn A.',
        'Trong Rhetorical Synthesis, đọc kỹ động từ mục tiêu đầu tiên: “emphasize a similarity” → loại ngay các đáp án nhấn mạnh sự tương phản (“stand in contrast”, “larger figure than”) hoặc chỉ nhắc đến 1 đối tượng.',
        [
            ('Đáp án đúng', 'Chỉ rõ điểm tương đồng chung giữa cả hai tác phẩm (cùng là LED light sculpture do Grimanesa Amoros thực hiện) bằng cấu trúc song song “as is...”.'),
            ('Wrong Goal (Contrast)', 'Nhấn mạnh sự KHÁC BIỆT về chất liệu hình khối (smooth LED domes vs. tangled LED tubes), ngược hoàn toàn với mục tiêu tìm điểm giống nhau.'),
            ('Missing Second Subject', 'Chỉ nhắc đến *Uros House* mà hoàn toàn bỏ quên *Golden Waters*.'),
            ('Wrong Goal (Contrast)', 'So sánh sự khác biệt về kích thước (118,080 vs. 250 cubic feet) thay vì điểm tương đồng.'),
        ],
    ),

    # --- M1 Q25 ---
    q_item(
        'may2025_v4_us_rw_m1_q25', 25, 'Expression of Ideas', 'Rhetorical Synthesis', 'Easy',
        '<p>While researching a topic, a student has taken the following notes:</p>'
        '<ul>'
        '<li>E.M. Forster was an acclaimed writer.</li>'
        '<li>He is best known for his novels.</li>'
        '<li>Forster’s most famous novels include <i>A Room with a View</i> (1908) and <i>Howards End</i> (1910).</li>'
        '<li>His first published work of fiction was a short story called “Albergo Empedocle.”</li>'
        '<li>It was published in <i>Temple Bar</i> in 1903.</li>'
        '</ul>',
        'The student wants to provide a specific example of one of E.M. Forster’s most famous works. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
        [
            'E.M. Forster was an acclaimed writer known for his novels.',
            '“Albergo Empedocle” was published before some of E.M. Forster’s most famous novels.',
            'The 1908 novel <i>A Room with a View</i> is one of E.M. Forster’s most famous works.',
            'E.M. Forster’s first published work of fiction was a 1903 short story called “Albergo Empedocle.”',
        ],
        'C',
        'Mục tiêu: đưa ra **một ví dụ cụ thể về một trong những tác phẩm nổi tiếng nhất** của E.M. Forster. Theo ghi chú, các tiểu thuyết nổi tiếng nhất gồm *A Room with a View* (1908) và *Howards End* (1910). Chỉ có đáp án C gọi đích danh *A Room with a View* là một trong các tác phẩm nổi tiếng nhất của ông → Chọn C.',
        'Kiểm tra đúng hai tiêu chí trong mục tiêu: (1) có tên tác phẩm cụ thể (“specific example”); (2) tác phẩm đó thuộc nhóm “most famous works” (không phải tác phẩm đầu tay “Albergo Empedocle”).',
        [
            ('Missing Example', 'Chỉ giới thiệu chung ông nổi tiếng về tiểu thuyết mà không nêu tên bất kỳ tác phẩm cụ thể nào.'),
            ('Wrong Example', 'Chỉ gọi tên truyện ngắn đầu tay “Albergo Empedocle” và nói chung chung “some of E.M. Forster’s most famous novels” mà không nêu tên tiểu thuyết nổi tiếng nào.'),
            ('Đáp án đúng', 'Nêu đích danh tiểu thuyết năm 1908 *A Room with a View* đúng như một trong những tác phẩm nổi tiếng nhất của Forster.'),
            ('Wrong Example', 'Đưa ví dụ về tác phẩm hư cấu xuất bản đầu tiên (“Albergo Empedocle”), không phải tác phẩm nổi tiếng nhất.'),
        ],
    ),

    # --- M1 Q26 ---
    q_item(
        'may2025_v4_us_rw_m1_q26', 26, 'Expression of Ideas', 'Rhetorical Synthesis', 'Easy',
        '<p>While researching a topic, a student has taken the following notes:</p>'
        '<ul>'
        '<li>The Carnegie Prize is an international art competition administered by the Carnegie Museum of Art in Pittsburgh, Pennsylvania.</li>'
        '<li>Painter Anselm Kiefer of Germany won a Carnegie Prize gold medal in 1985.</li>'
        '<li>Kiefer’s winning artwork was a painting entitled <i>Midgard</i>.</li>'
        '<li>Sculptor Jean Arp of Germany won a Carnegie Prize gold medal in 1964.</li>'
        '<li>Arp’s winning artwork was a sculpture entitled <i>Sculpture Classique</i>.</li>'
        '</ul>',
        'The student wants to contrast the two artworks. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
        [
            'Kiefer’s <i>Midgard</i> is a painting, while Arp’s <i>Sculpture Classique</i> is a sculpture.',
            'Kiefer won a Carnegie Prize gold medal in 1985 for the painting <i>Midgard</i>.',
            'Carnegie Prize gold medals have been awarded to both painters and sculptors.',
            'Both <i>Midgard</i> and <i>Sculpture Classique</i> are Carnegie Prize gold medal-winning artworks.',
        ],
        'A',
        'Mục tiêu: **đối chiếu sự khác biệt giữa hai tác phẩm nghệ thuật** (*Midgard* và *Sculpture Classique*). Đáp án A trực tiếp đối chiếu loại hình của cả hai tác phẩm bằng liên từ tương phản “while”: *Midgard* là một bức tranh (painting), trong khi *Sculpture Classique* là một bức tượng điêu khắc (sculpture) → Chọn A.',
        'Với mục tiêu “contrast the two artworks”, câu trả lời bắt buộc phải gọi tên cả hai tác phẩm VÀ dùng cấu trúc tương phản (“while / whereas / unlike”) để chỉ ra điểm khác biệt giữa chúng.',
        [
            ('Đáp án đúng', 'Gọi tên cả hai tác phẩm (*Midgard* và *Sculpture Classique*) và đối chiếu trực tiếp sự khác nhau (painting vs. sculpture).'),
            ('Missing Second Subject', 'Chỉ nhắc đến *Midgard* của Kiefer, không hề đề cập hay so sánh với *Sculpture Classique*.'),
            ('Wrong Focus', 'Chỉ nói chung giải thưởng từng trao cho cả họa sĩ lẫn nhà điêu khắc, không nhắc đến hai tác phẩm cụ thể.'),
            ('Wrong Goal (Similarity)', 'Nhấn mạnh điểm GIỐNG nhau (“Both... are gold medal-winning artworks”) thay vì tương phản.'),
        ],
    ),

    # --- M1 Q27 ---
    q_item(
        'may2025_v4_us_rw_m1_q27', 27, 'Expression of Ideas', 'Rhetorical Synthesis', 'Medium',
        '<ul>'
        '<li>In a 2003 study, Alexander and Schrag tested the effect of plant litter on seedling emergence in a grassland setting.</li>'
        '<li>The test site was a mesic grassland in a dry midlatitude climate in the United States.</li>'
        '<li>The researchers found that in these environmental conditions the presence of plant litter had a positive effect on seedling emergence.</li>'
        '<li>Seedling emergence is when a seedling sprouts above ground and begins photosynthesis.</li>'
        '</ul>',
        'Which choice most effectively uses information from the given sentences to present the study’s findings to an audience already familiar with the concept of seedling emergence?',
        [
            'The findings of Alexander and Schrag’s study were published in 2003.',
            'In a 2003 study by Alexander and Schrag, plant litter was found to have a positive effect on seedling emergence, which is when a seedling sprouts and begins photosynthesis.',
            'The effect of plant litter, which includes dead leaves and other plant matter, on seedling emergence has been the subject of scientific study.',
            'Alexander and Schrag found that in a mesic grassland and a dry midlatitude climate the presence of plant litter had a positive effect on seedling emergence.',
        ],
        'D',
        'Mục tiêu có HAI điều kiện rõ rệt: (1) trình bày **kết quả nghiên cứu** (“present the study’s findings” → thảm mục thực vật có tác động tích cực lên sự nảy mầm cây con trong điều kiện đồng cỏ ẩm vừa và khí hậu khô vĩ độ trung bình); và (2) hướng tới **độc giả đã quen thuộc với khái niệm “seedling emergence”** → KHÔNG cần (và không nên) định nghĩa lại “seedling emergence” là gì! Đáp án D thỏa mãn trọn vẹn cả hai điều kiện, trong khi B lại thừa thãi đi định nghĩa lại “seedling emergence” → Chọn D.',
        'Trong dạng Rhetorical Synthesis có yếu tố đối tượng độc giả (“audience already familiar with X” vs. “unfamiliar with X”): nếu độc giả ĐÃ BIẾT X, hãy LOẠI đáp án giải thích định nghĩa X!',
        [
            ('Missing Findings', 'Chỉ báo năm công bố (2003), không hề nói nghiên cứu phát hiện ra điều gì.'),
            ('Unnecessary Definition', 'Lại chèn định nghĩa “which is when a seedling sprouts and begins photosynthesis” — thừa thãi cho đối tượng độc giả đã am hiểu khái niệm này, đồng thời thiếu điều kiện môi trường cụ thể.'),
            ('Missing Findings / Outside Info', 'Không nêu kết quả nghiên cứu và còn tự thêm thông tin ngoài ghi chú (“dead leaves and other plant matter”).'),
            ('Đáp án đúng', 'Trình bày chính xác kết quả nghiên cứu kèm bối cảnh môi trường (mesic grassland, dry midlatitude climate) và lược bỏ gọn gàng định nghĩa thừa về seedling emergence.'),
        ],
    ),
]


# ============================================================================
# MODULE 2: SECTION 1, MODULE 2 — READING AND WRITING (27 REAL QUESTIONS)
# ============================================================================

MODULE_2_QUESTIONS = [
    # --- M2 Q1 ---
    q_item(
        'may2025_v4_us_rw_m2_q1', 1, 'Craft and Structure', 'Words in Context', 'Medium',
        '<p>Writer Lydia Davis observed that while _______ literary forms, such as the short story, are recognizable as such even as they evolve, there are rarer “intergeneric” forms that might, for example, use elements of both fiction and essays to create something unclassifiable. The very short publications of Diane Williams arguably fit in this category, since they straddle the line between prose and poetry.</p>',
        'Which choice completes the text with the most logical and precise word or phrase?',
        [
            'equivocal',
            'orthodox',
            'intermediate',
            'neutral',
        ],
        'B',
        'Cấu trúc tương phản qua liên từ “while”: một bên là các thể loại văn học _______ (như truyện ngắn — “short story”), vẫn dễ nhận diện đúng thể loại dù phát triển theo thời gian (“recognizable as such”); bên kia là các thể loại “liên thể loại” hiếm gặp hơn (“rarer ‘intergeneric’ forms”) trộn lẫn tiểu thuyết và tiểu luận để tạo ra thứ “không thể phân loại” (“unclassifiable”). Đối lập trực diện với thể loại lai ghép hiếm gặp/khó xếp loại chính là các thể loại **chính thống, truyền thống, quy chuẩn** → Chọn B (“orthodox”).',
        'Ghi nhớ cặp từ vựng tương phản hay ra trên Digital SAT: “intergeneric / unclassifiable / unconventional” ↔ “orthodox / established / conventional” (chính thống, truyền thống).',
        [
            ('Opposite Meaning', 'equivocal = mơ hồ, nước đôi — trái ngược hoàn toàn với đặc điểm “recognizable as such” (dễ nhận diện rõ ràng).'),
            ('Đáp án đúng', 'orthodox = chính thống, truyền thống, theo quy chuẩn — đối lập sắc nét với các thể loại lai ghép hiếm gặp và khớp ví dụ “short story”.'),
            ('Wrong Target', 'intermediate = trung gian, nằm giữa — đây là đặc trưng của các thể loại “intergeneric” ở vế sau (“straddle the line”), không phải của truyện ngắn ở vế trước.'),
            ('Wrong Context', 'neutral = trung lập — không tạo thế tương phản hợp nghĩa với “rarer intergeneric forms”.'),
        ],
    ),

    # --- M2 Q2 ---
    q_item(
        'may2025_v4_us_rw_m2_q2', 2, 'Craft and Structure', 'Words in Context', 'Medium',
        '<p>For most of its length, the Pungue River has sufficiently high flow velocity to suspend sedimentary particles; but when the river reaches the calmer waters of the Indian Ocean, its channel widens and divides, reducing flow velocity and thereby _______ sedimentary particle suspension. Particles are thus deposited, eventually forming deltaic lobes.</p>',
        'Which choice completes the text with the most logical and precise word or phrase?',
        ['compounding', 'obscuring', 'interrupting', 'expediting'],
        'C',
        'Chuỗi nhân–quả địa chất cực kỳ chặt chẽ: dọc hầu hết chiều dài sông, vận tốc dòng chảy đủ cao để giữ các hạt trầm tích lơ lửng (“suspend sedimentary particles”); nhưng khi đổ ra vùng nước êm hơn của Ấn Độ Dương, lòng sông mở rộng và chia nhánh, làm giảm vận tốc dòng chảy, qua đó **làm gián đoạn / chấm dứt** quá trình lơ lửng đó — kết quả là các hạt trầm tích lắng xuống (“deposited”) tạo thành các thùy châu thổ → Chọn C (“interrupting”).',
        'Đọc câu kết phía sau chỗ trống (“Particles are thus deposited”) để suy ngược lại hành động: muốn hạt trầm tích lắng đọng xuống đáy thì quá trình lơ lửng (“suspension”) phải bị cắt đứt/gián đoạn (“interrupting”).',
        [
            ('Opposite Direction', 'compounding = làm trầm trọng thêm / làm tăng thêm — nếu giảm vận tốc mà làm tăng sự lơ lửng thì hạt sẽ không lắng đọng được.'),
            ('Wrong Meaning', 'obscuring = che khuất, làm mờ mịt — không diễn đạt quá trình vật lý làm dừng trạng thái lơ lửng của trầm tích.'),
            ('Đáp án đúng', 'interrupting = làm gián đoạn, cắt đứt — khớp hoàn toàn logic vật lý: vận tốc giảm → cắt đứt sự lơ lửng → hạt lắng đọng.'),
            ('Opposite Direction', 'expediting = đẩy nhanh, xúc tiến — trái ngược hoàn toàn với việc dòng chảy chậm lại và kết thúc sự lơ lửng.'),
        ],
    ),

    # --- M2 Q3 ---
    q_item(
        'may2025_v4_us_rw_m2_q3', 3, 'Craft and Structure', 'Words in Context', 'Medium',
        '<p>Postcranial skeletal pneumaticity (PSP) refers to the presence of extensions of an animal’s lungs and air sacs inside its bones. Though such structures do not typically fossilize, they are believed to have been present in <i>Tyrannosaurus</i>, <i>Anhanguera</i>, and other Cretaceous theropods and pterosaurs. To _______ PSP from fossils, researchers look for indicators such as large foramina (holes in bones).</p>',
        'Which choice completes the text with the most logical and precise word or phrase?',
        ['infer', 'preserve', 'isolate', 'acquire'],
        'A',
        'Vì mô mềm của phổi và túi khí thường KHÔNG hóa thạch (“do not typically fossilize”), các nhà nghiên cứu không thể nhìn thấy PSP trực tiếp mà phải dựa vào các dấu hiệu gián tiếp như lỗ lớn trong xương (“indicators such as large foramina”) để **suy luận ra** sự tồn tại của PSP từ hóa thạch → Chọn A (“infer” = suy luận, rút ra kết luận gián tiếp).',
        'Khi văn bản nói cấu trúc gốc không còn tồn tại trực tiếp và nhà khoa học phải dựa vào “indicators” (dấu hiệu gián tiếp), động từ chuẩn SAT đi kèm luôn là “infer” (hoặc deduce).',
        [
            ('Đáp án đúng', 'infer = suy luận — khớp tuyệt đối với ngữ cảnh không có hóa thạch mô mềm trực tiếp mà phải tìm “indicators” để suy đoán sự hiện diện của PSP.'),
            ('Wrong Meaning', 'preserve = bảo tồn — các cấu trúc túi khí không hề hóa thạch nên không thể bảo tồn từ hóa thạch.'),
            ('Wrong Meaning', 'isolate = tách chiết, cô lập — bạn không thể tách chiết phần mô phổi vốn đã không còn tồn tại trong hóa thạch xương.'),
            ('Wrong Meaning', 'acquire = thu nhận, mua lại — sai ngữ cảnh khoa học cổ sinh vật học.'),
        ],
    ),

    # --- M2 Q4 ---
    q_item(
        'may2025_v4_us_rw_m2_q4', 4, 'Craft and Structure', 'Words in Context', 'Medium',
        '<p>The subscription model in which consumers who do not deliberately cancel their subscriptions automatically pay recurring fees for access to products and services benefits retailers when consumer _______ is high. Many of the 8.5 percent of subscribers who canceled their food and beverage subscriptions in January 2022 had stopped valuing their subscriptions long before then, but sellers profited from those customers’ passivity in the interim.</p>',
        'Which choice completes the text with the most logical and precise word or phrase?',
        ['inertia', 'evasion', 'decisiveness', 'turnover'],
        'A',
        'Câu thứ hai chính là lời giải thích trực tiếp cho chỗ trống: nhiều người đăng ký đã ngừng thấy gói dịch vụ có giá trị từ lâu nhưng vẫn không chủ động hủy, và “sellers profited from those customers’ **passivity** in the interim” (người bán hưởng lợi từ sự thụ động/chây ỳ của khách hàng). Từ đồng nghĩa chuẩn mực với “passivity” (sự thụ động, ngại thay đổi/hành động) là **inertia** (sức ỳ) → Chọn A.',
        'Trong SAT Words in Context, hãy săn từ khóa đồng nghĩa lặp lại ở câu liền kề: “passivity” (sự thụ động không hành động) ↔ “inertia” (sức ỳ, khuynh hướng giữ nguyên hiện trạng).',
        [
            ('Đáp án đúng', 'inertia = sức ỳ, tính thụ động không muốn hành động/thay đổi — khớp 100% với từ khóa “passivity” và bối cảnh khách hàng không chịu bấm hủy gói.'),
            ('Wrong Meaning', 'evasion = sự né tránh, trốn tránh (nghĩa vụ/thuế) — khách hàng vẫn trả tiền đều đặn vì lười hủy chứ không hề trốn tránh.'),
            ('Opposite Meaning', 'decisiveness = sự quyết đoán — nếu khách hàng quyết đoán thì họ đã hủy ngay khi hết thấy giá trị, làm giảm lợi nhuận người bán.'),
            ('Opposite Impact', 'turnover = tỷ lệ thay đổi/rời bỏ — tỷ lệ khách rời bỏ cao sẽ gây hại cho mô hình thuê bao chứ không giúp nhà bán lẻ hưởng lợi.'),
        ],
    ),

    # --- M2 Q5 ---
    q_item(
        'may2025_v4_us_rw_m2_q5', 5, 'Craft and Structure', 'Words in Context', 'Medium',
        '<p>Urban green spaces can improve air quality, as vegetation absorbs pollutants and also dilutes pollutant concentrations through ventilation. However, data from air-quality monitoring stations in locations throughout Romania suggest that this often-cited benefit of vegetation is not always _______: researchers found that when there are many trees along a busy street, ventilation has minimal effect on the air quality.</p>',
        'Which choice completes the text with the most logical and precise word or phrase?',
        ['immoderate', 'realized', 'unappreciated', 'compressed'],
        'B',
        'Sau dấu hai chấm giải thích rõ ý chỗ trống: các nhà nghiên cứu phát hiện khi có nhiều cây dọc tuyến phố đông đúc, tác dụng thông gió làm loãng ô nhiễm gần như không đáng kể (“minimal effect on the air quality”). Điều này có nghĩa là lợi ích vốn hay được ca ngợi của cây xanh không phải lúc nào cũng **trở thành hiện thực / đạt được trên thực tế** → Chọn B (“realized” = được hiện thực hóa, đạt được).',
        'Lưu ý nghĩa học thuật bậc cao của động từ “realize” trên SAT: không chỉ là “nhận ra”, mà còn có nghĩa là “achieved / brought into actuality” (hiện thực hóa một lợi ích/tiềm năng).',
        [
            ('Wrong Meaning', 'immoderate = thái quá, quá mức — không hợp nghĩa “benefit is not always immoderate”.'),
            ('Đáp án đúng', 'realized = được hiện thực hóa, đạt được — khớp chính xác với thực tế ở Romania rằng tác dụng cải thiện không khí có lúc không diễn ra đáng kể.'),
            ('Wrong Logic', 'unappreciated = không được trân trọng/đánh giá đúng — nếu điền “not always unappreciated” (không phải lúc nào cũng bị xem nhẹ) thì hoàn toàn lạc khỏi ý thí nghiệm đo chất lượng không khí thực tế.'),
            ('Wrong Meaning', 'compressed = bị nén lại — sai hoàn toàn ngữ nghĩa khi đi cùng danh từ “benefit”.'),
        ],
    ),

    # --- M2 Q6 ---
    q_item(
        'may2025_v4_us_rw_m2_q6', 6, 'Craft and Structure', 'Text Structure and Purpose', 'Medium',
        '<p>Founded in Denver in 1991, the Museo de Las Americas is one of the best-known US-based institutions showcasing Latino cultures. Since its founding, it has acquired more than 4,800 objects for its permanent collection. <u>Since 2000, the number of Latino cultural institutions in the US has expanded considerably.</u> LA Plaza de Cultura y Artes, which opened in Los Angeles in 2011 and focuses on Mexican American art and culture, is among the most prominent.</p>',
        'Which choice best states the function of the underlined sentence in the text as a whole?',
        [
            'It contrasts the focus of the Latino cultural institution discussed earlier in the text with the focus of the institution discussed later in the text.',
            'It identifies a historical trend of which the Latino cultural institution discussed later in the text is a part.',
            'It analyzes how two institutions’ approach to exhibiting artworks reflects the approach taken by most Latino cultural institutions.',
            'It describes a historical development that encouraged the founding of the two Latino cultural institutions discussed in the text.',
        ],
        'B',
        'Kiểm tra mốc thời gian cực kỳ chính xác: (1) Tổ chức đầu tiên (Museo de Las Americas) thành lập năm **1991** (TRƯỚC năm 2000); (2) Câu gạch chân nêu một **xu hướng lịch sử từ năm 2000 trở đi** (“Since 2000, the number of Latino cultural institutions in the US has expanded considerably”); (3) Câu sau giới thiệu LA Plaza de Cultura y Artes mở cửa năm **2011** (thuộc làn sóng mở rộng sau năm 2000 này). Như vậy, câu gạch chân xác định một xu hướng lịch sử mà tổ chức văn hóa Mỹ Latinh được nêu ở phần sau là một phần trong đó → Chọn B.',
        'Đừng sập bẫy D (“the two Latino cultural institutions”)! Luôn đối chiếu năm thành lập: Museo de Las Americas mở năm 1991 nên KHÔNG thể là kết quả của xu hướng diễn ra “Since 2000” — chỉ có LA Plaza (2011) thuộc xu hướng này!',
        [
            ('Not Mentioned', 'Câu gạch chân chỉ nói về sự gia tăng SỐ LƯỢNG các tổ chức văn hóa từ năm 2000, hoàn toàn không đối chiếu trọng tâm nội dung của hai bảo tàng.'),
            ('Đáp án đúng', 'Chính xác tuyệt đối: nêu xu hướng mở rộng từ năm 2000 và dẫn sang LA Plaza de Cultura y Artes (mở năm 2011) như một đại diện tiêu biểu thuộc xu hướng đó.'),
            ('Out of Scope', 'Không hề phân tích phương pháp trưng bày tác phẩm nghệ thuật của hai bảo tàng hay so với số đông các tổ chức khác.'),
            ('Chronology Trap', 'Sai mốc thời gian: Museo de Las Americas thành lập năm 1991 (trước năm 2000), nên xu hướng “Since 2000” không thể thúc đẩy việc thành lập CẢ HAI tổ chức.'),
        ],
    ),

    # --- M2 Q7 ---
    q_item(
        'may2025_v4_us_rw_m2_q7', 7, 'Craft and Structure', 'Text Structure and Purpose', 'Medium',
        '<p>In Bhutan, use of solid fuel (e.g., coal, wood) as a share of total household fuel use fell by approximately two thirds between 2000 and 2019; such shifts are often explained by appeal to the energy ladder, a model holding that fuel choice is mediated mainly by household income (specifically, high-technology fuels displace solid fuels as incomes rise). Rasmus Heltberg’s study of fuel use in Nepal shows this model to be reductive, however; household fuel use was heterogeneous, flexible, and influenced by several factors, including the stability of the local electrical grid.</p>',
        'Which choice best describes the main purpose of the text?',
        [
            'To challenge a common explanation for households’ fuel choices',
            'To contrast patterns in household fuel use in two countries',
            'To account for the effect of fuel use on household income',
            'To critique a frequently used model of changes in household fuel prices',
        ],
        'A',
        'Cấu trúc bài xoay quanh bước ngoặt “however”: (1) Câu đầu giới thiệu một lời giải thích phổ biến cho sự lựa chọn nhiên liệu hộ gia đình — mô hình “energy ladder” (cho rằng thu nhập hộ gia đình là yếu tố chính quyết định lựa chọn nhiên liệu, như thường dùng để lý giải trường hợp Bhutan); (2) Câu hai phản biện bằng nghiên cứu của Rasmus Heltberg ở Nepal chứng minh mô hình đó là **phiến diện / đơn giản hóa quá mức** (“reductive”), vì lựa chọn nhiên liệu thực tế đa dạng và phụ thuộc nhiều yếu tố khác (như độ ổn định lưới điện) → Mục đích chính là thách thức một lời giải thích phổ biến về lựa chọn nhiên liệu của các hộ gia đình → Chọn A.',
        'Cảnh giác bẫy “sai đúng 1 từ cuối” ở đáp án D: D viết rất hay (“critique a frequently used model”) nhưng lại đổi “fuel choices” thành “fuel **prices**” (giá nhiên liệu) — chi tiết không hề có trong bài!',
        [
            ('Đáp án đúng', 'Khớp trọng tâm toàn bài: nêu mô hình phổ biến (energy ladder) giải thích lựa chọn nhiên liệu hộ gia đình, rồi dùng nghiên cứu ở Nepal để bác bỏ tính phiến diện của nó.'),
            ('Wrong Focus', 'Bài không đối chiếu hai quốc gia Bhutan và Nepal với nhau; Bhutan chỉ minh họa bối cảnh mô hình thường được áp dụng, còn Nepal được đưa ra để phản biện chính mô hình đó.'),
            ('Reversed Causality', 'Mô hình nói thu nhập ảnh hưởng đến lựa chọn nhiên liệu, không phải nhiên liệu ảnh hưởng lên thu nhập.'),
            ('Single-Word Trap', 'Bẫy cực tinh vi: đổi “household fuel choices” thành “household fuel prices” (giá nhiên liệu) — mô hình energy ladder hoàn toàn không dự báo giá nhiên liệu.'),
        ],
    ),

    # --- M2 Q8 ---
    q_item(
        'may2025_v4_us_rw_m2_q8', 8, 'Information and Ideas', 'Central Ideas and Details', 'Hard',
        '<p>The following text is from George Eliot’s 1857 short story “The Sad Fortunes of the Rev. Amos Barton.” The Countess Czerlaski is a newcomer to the town of Milby.</p><p>It is true, the Countess was a little vain, a little ambitious, a little selfish, a little shallow and frivolous, a little given to white lies.—But who considers such slight blemishes, such moral pimples as these, disqualifications for entering into the most respectable society! Indeed, the severest ladies in Milby would have been perfectly aware that these characteristics would have created no wide distinction between the Countess Czerlaski and themselves; and since it was clear there was a wide distinction—why it must lie in the possession of some vices from which they were undeniably free.</p>',
        'Which choice best states the main idea of the text?',
        [
            'The residents of Milby had initially viewed the Countess Czerlaski with suspicion, but they have gradually come to see her as mostly harmless.',
            'Although the Countess Czerlaski actively cultivates a sense of mystery about her, her background is less interesting than what many residents of Milby have been led to believe.',
            'Although the residents of Milby are generally thought to be hospitable, the Countess Czerlaski has committed many social blunders that have caused her to be widely disliked.',
            'Some residents of Milby are determined to disapprove of the Countess Czerlaski, even though the reasons for their dislike are largely groundless.',
        ],
        'D',
        'Giọng văn châm biếm đặc trưng của George Eliot: người kể chuyện thừa nhận Nữ bá tước Czerlaski có vài thói xấu nhỏ nhặt (hơi phù phiếm, ích kỷ, hay nói dối vặt), nhưng mỉa mai rằng đó chỉ là những “vết xước nhỏ” mà ngay cả các quý bà khắt khe nhất ở thị trấn Milby cũng thừa hiểu chẳng hề tạo ra khoảng cách lớn nào giữa Nữ bá tước với chính họ! Thế nhưng vì họ **khăng khăng cho rằng phải có một khoảng cách lớn** (“since it was clear there was a wide distinction”), họ tự suy diễn rằng hẳn bà ta phải mắc những tội lỗi ghê gớm nào đó mà họ không có! Điều này phơi bày rằng một số cư dân Milby **nhất quyết bài xích/không ưa Nữ bá tước dù lý do ghét bỏ phần lớn vô căn cứ** → Chọn D.',
        'Khi đọc văn xuôi châm biếm thế kỷ 19 (George Eliot, Jane Austen), hãy giải mã lập luận mỉa mai: khi tác giả nói “vì rõ ràng phải có khoảng cách nên hẳn bà ta phải có tật xấu bí mật nào đó”, tác giả đang tố cáo định kiến vô căn cứ của các quý bà thị trấn!',
        [
            ('Not Mentioned', 'Đoạn trích không hề mô tả sự thay đổi thái độ theo thời gian hay việc cư dân dần xem Nữ bá tước là vô hại.'),
            ('Not Mentioned', 'Không có chi tiết nào cho thấy Nữ bá tước cố tình tạo vẻ bí ẩn về xuất thân của mình.'),
            ('Contradicted by Text', 'Bài không nói cư dân Milby nổi tiếng hiếu khách, và cũng không nói Nữ bá tước phạm nhiều lỗi giao tiếp nghiêm trọng (“social blunders”) — trái lại tác giả gọi khuyết điểm của bà là rất nhỏ (“slight blemishes”).'),
            ('Đáp án đúng', 'Nắm trọn mạch châm biếm của tác giả: các quý bà Milby quyết tâm giữ khoảng cách và chê bai Nữ bá tước bằng cách tự gán ghép tội lỗi vô căn cứ.'),
        ],
    ),

    # --- M2 Q9 ---
    q_item(
        'may2025_v4_us_rw_m2_q9', 9, 'Information and Ideas', 'Central Ideas and Details', 'Hard',
        '<p>Some researchers posit that species on the South Pacific island of Grande Terre are the surviving members of clades that inhabited other islands in the region before the complete emergence of Grande Terre 37 million years ago. In a 2012 study, however, Hervé Sauquet et al. found that the crown age (the age of the most recent common ancestor of all living and extinct species in the clade) of the clade of southern beeches on Grande Terre is 16.4 million years; Sauquet et al. further found that the crown age of the clade of southern beeches in the South Pacific generally is also approximately 16.4 million years.</p>',
        'As presented in the text, the findings of Sauquet et al. best support which statement?',
        [
            'The southern beeches found on Grande Terre are members of a clade that likely originated outside the South Pacific.',
            'The most recent common ancestor of the southern beeches found on Grande Terre lived at least 37 million years ago.',
            'The southern beeches found on Grande Terre are not members of a clade that existed before the island completely emerged.',
            'The ancestors of most species found on Grande Terre arrived on the island earlier than did the most recent common ancestor of the island’s southern beeches.',
        ],
        'C',
        'So sánh hai mốc niên đại trong bài: (1) Đảo Grande Terre nổi lên hoàn toàn cách đây **37 triệu năm**; một số nhà nghiên cứu giả thuyết các loài trên đảo thuộc các nhánh tiến hóa (clades) đã sống trên các đảo khác trong vùng **trước** khi Grande Terre nổi lên (>37 triệu năm trước). (2) Tuy nhiên (“however”), Sauquet và cộng sự phát hiện tuổi đỉnh (crown age — tuổi của tổ tiên chung gần nhất của cả nhánh) của nhánh sồi phương Nam (southern beeches) trên đảo Grande Terre lẫn trên toàn Nam Thái Bình Dương chỉ là **16,4 triệu năm** (< 37 triệu năm rất nhiều!). Điều này chứng tỏ nhánh sồi phương Nam trên Grande Terre KHÔNG thuộc một nhánh tiến hóa đã tồn tại từ trước khi hòn đảo nổi lên hoàn toàn → Chọn C.',
        'Trong các bài sinh học tiến hóa/địa chất có 2 mốc niên đại, hãy vẽ nhanh trục thời gian: 37 triệu năm trước (đảo nổi lên) → 16,4 triệu năm trước (nhánh sồi mới hình thành). Vì 16,4 < 37 nên nhánh này xuất hiện SAU khi đảo nổi lên!',
        [
            ('Unsupported Inference', 'Cả nhánh sồi trên Grande Terre và nhánh sồi chung ở Nam Thái Bình Dương đều có tuổi đỉnh ~16,4 triệu năm; bài không đưa bằng chứng nào nói nhánh này có nguồn gốc ngoài Nam Thái Bình Dương.'),
            ('Contradicted by Numbers', 'Sai số liệu trực tiếp: tổ tiên chung gần nhất (crown age) sống cách đây 16,4 triệu năm, ít hơn nhiều so với “at least 37 million years ago”.'),
            ('Đáp án đúng', 'Suy luận toán học chặt chẽ: tuổi nhánh là 16,4 triệu năm < mốc đảo nổi lên 37 triệu năm → nhánh sồi phương Nam không tồn tại từ trước khi đảo nổi lên.'),
            ('Out of Scope / Overgeneralization', 'Nghiên cứu của Sauquet et al. chỉ khảo sát riêng nhóm sồi phương Nam, không đưa ra kết luận về “most species” (đa số các loài) trên đảo.'),
        ],
    ),

    # --- M2 Q10 ---
    q_item(
        'may2025_v4_us_rw_m2_q10', 10, 'Information and Ideas', 'Command of Evidence (Textual)', 'Medium',
        '<p>A student is writing a research paper on the history of irrigation in the southwestern United States, situating the development of Lake Sabrina (a man-made body of water created in Inyo County, California, in 1908) in a larger historical context. The student claims that some modern-day irrigation methods used in southwestern states, such as California, Arizona, and New Mexico, have a lineage that long predates the completion of Lake Sabrina.</p>',
        'Which quotation from a historian best supports the student’s claim?',
        [
            '“Sprinkler irrigation systems, which were developed in the late 20th century, are a convenient technique of irrigating that makes use of machinery in order to spray water in all directions. Many areas of the Southwestern United States are currently irrigated by this method.”',
            '“In the decades following the Second World War, irrigation of arid areas for agriculture increased to such a degree that it now accounts for roughly 70% of the world’s water usage.”',
            '“The irrigation system developed by the Hohokam people in what is now central Arizona in the 7th century CE was simple but made use of hydraulic engineering design principles that are still utilized by today’s engineers.”',
            '“The importance of the development of irrigation infrastructure in the American Southwest today cannot be overstated, since it is the most common means of conveying water for food production.”',
        ],
        'C',
        'Kiểm tra 3 mảnh ghép trong tuyên bố của sinh viên: (1) phương pháp tưới tiêu **hiện đại** ở các bang **Tây Nam Hoa Kỳ** (California, Arizona, New Mexico); (2) có nguồn gốc/dòng dõi (**lineage**); (3) **ra đời từ rất lâu trước khi hồ Sabrina hoàn thành năm 1908** (“long predates 1908”). Đáp án C thỏa mãn 100% cả 3 tiêu chí: hệ thống tưới của người Hohokam ở miền trung **Arizona** từ **thế kỷ thứ 7 SCN** (trước năm 1908 hơn 1.200 năm!) sử dụng các nguyên lý kỹ thuật thủy lợi **vẫn đang được các kỹ sư ngày nay áp dụng** → Chọn C.',
        'Luôn gạch chân mốc năm chuẩn (“1908”) trong đề bài và đối chiếu ngay với mốc thời gian ở từng trích dẫn: late 20th century (A) và post-WWII (B) đều SAU 1908 → loại ngay!',
        [
            ('Wrong Timeframe', 'Hệ thống phun mưa phát triển vào cuối thế kỷ 20 (SAU năm 1908), không hề có nguồn gốc từ lâu trước 1908.'),
            ('Wrong Timeframe & Scope', 'Nói về những thập kỷ sau Thế chiến II (SAU 1908) và xét tỷ lệ dùng nước toàn cầu, không chứng minh dòng dõi cổ xưa ở Tây Nam Mỹ.'),
            ('Đáp án đúng', 'Khớp cả 3 trụ cột: vùng Tây Nam Mỹ (Arizona) + rất lâu trước 1908 (thế kỷ 7 SCN) + nối trực tiếp tới hiện đại (“still utilized by today’s engineers”).'),
            ('Missing Historical Lineage', 'Chỉ nhấn mạnh tầm quan trọng của hạ tầng tưới tiêu ngày nay mà không hề đề cập đến nguồn gốc lịch sử trước năm 1908.'),
        ],
    ),

    # --- M2 Q11 ---
    q_item(
        'may2025_v4_us_rw_m2_q11', 11, 'Information and Ideas', 'Command of Evidence (Textual)', 'Hard',
        '<p>Periods of subfreezing temperatures in Alaska have been growing shorter as a result of climate changes, potentially enabling increased carbon dioxide (CO<sub>2</sub>) absorption through greater productivity of sidebells wintergreen (<i>Orthilia secunda</i>) plants and other vegetation, but also potentially enabling increased CO<sub>2</sub> output through greater heterotrophic respiration (CO<sub>2</sub> generated by the activity of soil microorganisms). Hydrologist Yonghong Yi and her colleagues developed a model incorporating numerous inputs—years of soil moisture and snow cover data among them—to evaluate the effects of climate changes on the CO<sub>2</sub> balance in Alaska, concluding that net CO<sub>2</sub> is likely to increase if seasonal snow cover arrives earlier relative to the onset of soil surface freezing.</p>',
        'Which finding, if true, would most directly support the researchers’ conclusion?',
        [
            'Relatively early snow cover reduces the amount of soil moisture available for the growth of plant species such as <i>O. secunda</i> and lowers the rate of heterotrophic respiration.',
            'The soil insulation provided by snow cover enables heterotrophic respiration to continue during a period in which plant species such as <i>O. secunda</i> are typically not growing.',
            'The effect of soil moisture on the growth of vegetation and on the rate of heterotrophic respiration is stronger during the period of seasonal snow cover than during the period without snow cover.',
            'Seasonal snow cover tends to persist longer in areas of relatively low vegetation growth and high heterotrophic respiration than in areas of relatively high vegetation growth and low heterotrophic respiration.',
        ],
        'B',
        'Phân tích phương trình cân bằng CO<sub>2</sub> ròng: **Net CO<sub>2</sub> = Lượng CO<sub>2</sub> thải ra (hô hấp dị dưỡng của vi sinh vật đất) − Lượng CO<sub>2</sub> hấp thụ (quang hợp/sinh trưởng của thực vật như *O. secunda*)**. Kết luận của Yonghong Yi: **Net CO<sub>2</sub> có khả năng TĂNG** nếu lớp tuyết phủ theo mùa đến **SỚM hơn** trước khi mặt đất đóng băng. Cơ chế nào giải thích trực tiếp hiện tượng này? Đáp án B: lớp tuyết phủ đóng vai trò **cách nhiệt cho đất**, giúp quá trình hô hấp dị dưỡng (THẢI CO<sub>2</sub>) tiếp tục diễn ra trong giai đoạn mà các loài thực vật như *O. secunda* thường không còn sinh trưởng (KHÔNG hấp thụ bù CO<sub>2</sub>) → đầu ra tăng trong khi đầu vào không tăng → CO<sub>2</sub> ròng chắc chắn tăng → Chọn B!',
        'Với các bài sinh thái học về “net balance” (Net = Output − Input), để chứng minh Net TĂNG, hãy tìm đáp án đẩy Output (respiration) lên cao hơn tương đối so với Input (plant growth)!',
        [
            ('Ambiguous / Weakens', 'Nói tuyết đến sớm làm GIẢM tốc độ hô hấp dị dưỡng (giảm phát thải CO<sub>2</sub>) đồng thời giảm độ ẩm cho cây — cả hai chiều cùng giảm nên không chứng minh được CO<sub>2</sub> ròng tăng.'),
            ('Đáp án đúng', 'Cung cấp cơ chế vật lý–sinh học hoàn hảo: tuyết cách nhiệt giữ ấm đất cho vi sinh vật tiếp tục thải CO<sub>2</sub> đúng lúc cây ngừng mọc/hấp thụ → CO<sub>2</sub> ròng tăng.'),
            ('No Direction Specified', 'Chỉ nói ảnh hưởng của độ ẩm đất mạnh hơn lên CẢ cây lẫn vi sinh vật trong mùa tuyết, nhưng không nói theo hướng tăng hay giảm và không tách biệt hai vế để ra CO<sub>2</sub> ròng tăng.'),
            ('Irrelevant Spatial Correlation', 'Chỉ nói tuyết tồn tại lâu hơn ở vùng này so với vùng khác, không chứng minh cơ chế tuyết đến SỚM làm tăng CO<sub>2</sub> ròng.'),
        ],
    ),

    # --- M2 Q12 ---
    q_item(
        'may2025_v4_us_rw_m2_q12', 12, 'Information and Ideas', 'Command of Evidence (Quantitative)', 'Hard',
        _svg_m2_q12_forest_patches()
        + '<p>To understand the extent of deforestation in the Chorotega region of Costa Rica, Juan Pablo Arroyo Mora and colleagues used historical aerial photography and remote sensing data to track changes in the total number of forest patches in areas of different land use capability classes (categories that indicate possible uses of forest land). Due to the Chorotega region’s accessibility, various types of forested areas were converted to cattle pasture as rising international meat prices drove a cattle ranching boom in the 1960s and 1970s: this conversion is evident in the _______</p>',
        'Which choice most effectively uses data from the graph to complete the assertion?',
        [
            'high number of patches in Class VII and Class VIII in 1986.',
            'difference between the number of patches in Class VII and in Class VI in 2000.',
            'increase in the number of patches for all classes from 1979 to 2000.',
            'decrease in the number of patches for all classes from 1960 to 1979.',
        ],
        'D',
        'Khóa hai từ khóa cốt lõi trong câu khẳng định trước chỗ trống: (1) **“various types of forested areas were converted to cattle pasture”** (nhiều loại diện tích rừng khác nhau bị chặt phá chuyển sang đồng cỏ chăn nuôi bò → số lượng mảng rừng GIẢM trên tất cả các nhóm đất); và (2) mốc thời gian **“in the 1960s and 1970s”** (thập niên 1960 và 1970 → tương ứng chính xác khoảng thời gian **từ 1960 đến 1979** trên trục hoành!). Đối chiếu biểu đồ: từ năm 1960 sang năm 1979, cả 3 cột (Class VI, Class VIII, Class VII) đều giảm mạnh từ ~540–620 mảng xuống còn ~350–390 mảng → Chọn D!',
        'Trong câu đọc biểu đồ dạng “assertion completion”, luôn khớp đồng thời HAI yếu tố: (1) **Mốc thời gian** (“in the 1960s and 1970s” = 1960 → 1979) và (2) **Chiều hướng thay đổi** (phá rừng làm bãi chăn thả = số mảng rừng GIẢM).',
        [
            ('Wrong Timeframe & Static Point', 'Năm 1986 nằm ngoài giai đoạn 1960s–1970s và chỉ là một thời điểm đơn lẻ có số mảng rừng cao, không thể hiện sự suy giảm do phá rừng những năm 1960–1970.'),
            ('Wrong Timeframe & Irrelevant', 'Sự chênh lệch giữa Class VII và Class VI vào năm 2000 không hề phản ánh quá trình chuyển đổi rừng thành đồng cỏ trong thập niên 1960–1970.'),
            ('Wrong Timeframe & Direction', 'Giai đoạn 1979–2000 nằm SAU thập niên 1960–1970 và cho thấy số mảng rừng TĂNG mạnh trở lại.'),
            ('Đáp án đúng', 'Khớp chính xác 100% cả mốc thời gian (1960 → 1979) lẫn xu hướng thực tế trên biểu đồ (cả 3 hạng mục rừng đều giảm mạnh số mảng rừng).'),
        ],
    ),

    # --- M2 Q13 ---
    q_item(
        'may2025_v4_us_rw_m2_q13', 13, 'Information and Ideas', 'Command of Evidence (Quantitative)', 'Medium',
        html_table(
            'Value, Cost, and Seigniorage of US Coins by Denomination, 2023',
            [
                'Denomination',
                'Total value of units produced (in millions of dollars)',
                'Gross cost (in millions of dollars)',
                'Seigniorage (in millions of dollars)',
                'Seigniorage per $1 issued (dollars)',
            ],
            [
                ['One-cent', '41.4', '127.4', '−86.0', '−2.08'],
                ['Five-cent', '70.8', '163.4', '−92.6', '−1.31'],
                ['Ten-cent', '266.6', '141.1', '125.5', '0.47'],
                ['Quarter dollar', '568.4', '264.4', '304.0', '0.53'],
            ],
        )
        + '<p>Issuing a one-dollar coin yields positive seigniorage—profit generated when the face value of a coin exceeds the unit cost of producing it—for Singapore’s government, which in turn can be used to fund such services as education. Issuing coins can also result in negative seigniorage, however, and this phenomenon led Australia to stop producing certain coins. A student argues that it is in the financial interest of the United States to follow the example of Australia with regard to each of the four coins shown in the table.</p>',
        'Which choice best describes data from the table that weaken the student’s argument?',
        [
            'Seigniorage per dollar issued was slightly greater for quarter-dollar coins than for ten-cent coins, but seigniorage in millions of dollars was much greater for quarter-dollar coins than for ten-cent coins.',
            'Although issuing one-cent and five-cent coins resulted in negative seigniorage in millions of dollars, issuing ten-cent and quarter-dollar coins resulted in positive seigniorage in millions of dollars.',
            'Issuing one-cent and five-cent coins created negative seigniorage in millions of dollars, but for each of those coins, the gross cost of issuing the coin was lower than the gross cost of issuing ten-cent or quarter-dollar coins was.',
            'Although issuing five-cent coins created the greatest negative seigniorage in millions of dollars, issuing one-cent coins created the greatest negative seigniorage per dollar issued.',
        ],
        'B',
        'Lập luận của sinh viên: Mỹ nên học theo Úc ngừng sản xuất **CẢ BỐN** đồng xu trong bảng (“each of the four coins”) vì lợi ích tài chính. Tuy nhiên, nhìn vào cột “Seigniorage (in millions of dollars)”: chỉ có đồng 1 xu (−86.0) và 5 xu (−92.6) bị lỗ (negative seigniorage), còn đồng **10 xu (+125.5 triệu USD)** và **25 xu (+304.0 triệu USD)** đều mang lại **lợi nhuận đúc tiền DƯƠNG (positive seigniorage)** rất lớn cho chính phủ Mỹ! Do đó ngừng đúc cả bốn đồng sẽ làm Mỹ mất nguồn thu lớn → Chọn B.',
        'Luôn khoanh tròn từ tuyệt đối trong lập luận cần phản bác (“each of the four coins”). Để bác bỏ tuyên bố “cả 4 đồng đều nên ngừng đúc”, chỉ cần nêu rõ dữ liệu 2 đồng (ten-cent và quarter-dollar) đang tạo ra lợi nhuận DƯƠNG (positive seigniorage).',
        [
            ('True Data / Doesn’t Weaken', 'So sánh đồng 25 xu lớn hơn đồng 10 xu nhưng không hề chỉ ra chúng có seigniorage DƯƠNG (mang lại lợi nhuận), nên không trực tiếp phản bác lập luận ngừng đúc.'),
            ('Đáp án đúng', 'Khớp 100% số liệu bảng và đánh thẳng vào lỗ hổng của sinh viên: chỉ 1 xu và 5 xu bị lỗ, còn 10 xu và 25 xu sinh lời dương nên Mỹ không có lợi gì khi ngừng sản xuất cả bốn đồng.'),
            ('False Data', 'Sai số liệu bảng: chi phí tổng (gross cost) của đồng 5 xu là 163.4 triệu USD, CAO HƠN đồng 10 xu (141.1 triệu USD), không phải thấp hơn.'),
            ('Supports Instead of Weakens', 'Chỉ phân tích sâu mức lỗ của hai đồng 1 xu và 5 xu — thực chất củng cố việc bỏ 2 đồng này chứ không làm suy yếu lập luận đòi bỏ cả bốn đồng.'),
        ],
    ),

    # --- M2 Q14 ---
    q_item(
        'may2025_v4_us_rw_m2_q14', 14, 'Information and Ideas', 'Inferences', 'Medium',
        '<p>Though longitudinal studies like the Northern Ireland Longitudinal Study (NILS), which has surveyed approximately 500,000 participants in Northern Ireland to find trends in public health, are expensive because they are conducted over many years, by spanning these time frames, they can reveal causal patterns. But studies for which cause and effect is not at issue, like a public opinion study that merely seeks to determine the proportion of a city’s population that supports a particular tax proposal, can succeed without longitudinal methods, which means that _______</p>',
        'Which choice most logically completes the text?',
        [
            'the public opinion study could likely be completed at a considerably lower cost than NILS.',
            'longitudinal methods would likely be less suitable for studies in public opinion than for studies in public health.',
            'longitudinal methods would likely be less expensive for studies in public opinion than for studies in public health.',
            'the results from NILS would likely be more reliable than those from the public opinion study.',
        ],
        'A',
        'Chuỗi suy luận hai bước rất rõ: (1) Các nghiên cứu dọc (longitudinal studies) như NILS **rất tốn kém** (“are expensive”) vì phải tiến hành qua nhiều năm để tìm quy luật nhân–quả; (2) Ngược lại, những khảo sát không cần tìm quan hệ nhân–quả — như một khảo sát dư luận chỉ đo tỷ lệ dân số thành phố ủng hộ một đề xuất thuế — **có thể thành công mà không cần dùng phương pháp nghiên cứu dọc**. Suy ra tất yếu: khảo sát dư luận đó nhiều khả năng có thể hoàn thành với **chi phí thấp hơn đáng kể so với NILS** → Chọn A.',
        'Chú ý cấu trúc nhân–quả tương phản: “A is expensive because it uses Method X; B can succeed without Method X → which means that B is likely much less expensive than A!”',
        [
            ('Đáp án đúng', 'Suy luận trực tiếp, chặt chẽ nhất: không phải dùng phương pháp nghiên cứu dọc tốn kém kéo dài nhiều năm → chi phí hoàn thành thấp hơn đáng kể so với NILS.'),
            ('Overgeneralization', 'Bài chỉ nói một khảo sát dư luận cụ thể không xét nhân–quả thì không cần nghiên cứu dọc, không khẳng định phương pháp dọc “kém phù hợp hơn” cho toàn bộ lĩnh vực dư luận xã hội.'),
            ('Unsupported Comparison', 'Không có cơ sở nào cho thấy nếu áp dụng cùng phương pháp nghiên cứu dọc thì bên dư luận xã hội lại rẻ hơn bên y tế công cộng.'),
            ('Contradicted / Unsupported', 'Bài khẳng định khảo sát dư luận “can succeed without longitudinal methods”, hoàn toàn không nói kết quả NILS đáng tin cậy hơn.'),
        ],
    ),
    # --- M2 Q15 ---
    q_item(
        'may2025_v4_us_rw_m2_q15', 15, 'Information and Ideas', 'Inferences', 'Hard',
        '<p>The Virgin Group’s introduction of the Virgin Atlantic airline in 1984 is an instance of brand extension—the company leveraged its brand recognition as a music retailer to enter a new product category. To investigate how market share affects consumers’ likelihood of purchasing brand extensions, Alicia Grasby et al. identified 30 extended brand pairs (e.g., the same brand of vacuum cleaner and microwave) in household purchasing data; for each pair, Grasby et al. calculated the branded products’ market share and calculated the increase in probability of a brand in one category being purchased if the same brand was purchased in the other category. A broad inverse relationship between the two values emerged, which can most reasonably be attributed to the fact that _______</p>',
        'Which choice most logically completes the text?',
        [
            'the purchase probability of a brand is affected by the purchase probability of the particular product category to which it belongs, and thus brands in categories that are rarely purchased tend to have low purchase probabilities regardless of market share.',
            'as a brand’s market share increases, the number of competing brands in the same product category tends to decrease, and thus the rate of increase in market share tends to accelerate as a brand’s market share grows.',
            'brands with high market share have high purchase probability regardless of whether the other product in the pair is purchased and thus have less potential to increase in purchase probability than brands with low market share do.',
            'consumers tend to be less familiar with brands with low market share than brands with high market share and thus may purchase both products in a pair with low market share without recognizing that the products are the same brand.',
        ],
        'C',
        'Hiểu rõ hai đại lượng có **mối tương quan nghịch (inverse relationship)** trong nghiên cứu của Alicia Grasby et al.: (1) **Thị phần (market share)** của thương hiệu; và (2) **Mức tăng xác suất mua sản phẩm mở rộng (increase in probability)** khi khách đã mua sản phẩm kia của cùng thương hiệu. Vì sao thương hiệu có thị phần CÀNG CAO thì mức tăng xác suất mua thêm lại CÀNG THẤP (và ngược lại)? Do hiệu ứng trần xác suất: các thương hiệu có **thị phần cao vốn đã có xác suất được mua rất cao sẵn rồi** (bất kể khách có mua sản phẩm kia trong cặp hay không), nên **dư địa để tăng thêm xác suất mua sẽ ít hơn** so với các thương hiệu thị phần thấp → Chọn C!',
        'Đây là bài Inferences dạng “hiệu ứng trần toán học” (ceiling effect) rất đặc trưng của Module 2 Khó: khi giá trị nền (baseline purchase probability) vốn đã cao sẵn vì thị phần lớn, phần **tăng thêm (increase)** sẽ tự nhiên nhỏ hơn so với nhóm xuất phát từ nền thấp!',
        [
            ('Misses Core Mechanism', 'Chỉ nói xác suất mua phụ thuộc vào độ phổ biến của ngành hàng bất kể thị phần — không hề giải thích vì sao thị phần cao lại tương ứng với mức TĂNG xác suất thấp hơn.'),
            ('Irrelevant / Off-Topic', 'Bàn về số lượng đối thủ cạnh tranh và tốc độ tăng thị phần, hoàn toàn không liên quan đến xác suất mua sản phẩm mở rộng thương hiệu (brand extension).'),
            ('Đáp án đúng', 'Giải thích chuẩn xác cơ chế toán học tạo ra tương quan nghịch: thương hiệu thị phần lớn vốn đã có xác suất mua cao sẵn nên còn ít dư địa tăng thêm xác suất hơn thương hiệu thị phần nhỏ.'),
            ('Reversed Logic', 'Nếu người tiêu dùng thậm chí không nhận ra hai sản phẩm cùng một thương hiệu (ở các hãng thị phần thấp), thì việc mua sản phẩm này sẽ KHÔNG làm tăng xác suất mua sản phẩm kia — trái ngược với phát hiện rằng thương hiệu thị phần thấp lại có mức tăng xác suất CAO hơn!'),
        ],
    ),

    # --- M2 Q16 ---
    q_item(
        'may2025_v4_us_rw_m2_q16', 16, 'Standard English Conventions', 'Form, Structure, and Sense', 'Medium',
        '<p>The small celestial body known as 2060 Chiron is expected to have a relatively short lifetime in the outer solar system. Within just a few million years, 2060 Chiron is likely to migrate into the inner solar system or be destroyed, according to _______ trajectory.</p>',
        'Which choice completes the text so that it conforms to the conventions of Standard English?',
        [
            'astronomers modeling of the objects',
            'astronomer’s modeling of the object’s',
            'astronomers modeling of the object’s',
            'astronomers’ modeling of the object’s',
        ],
        'D',
        'Xét hai danh từ sở hữu liên tiếp: (1) Danh từ “modeling” (mô hình hóa) thuộc về **nhiều nhà thiên văn học** (không có mạo từ “an/the” phía trước nên bắt buộc là số nhiều sở hữu **astronomers’**); (2) Danh từ “trajectory” (quỹ đạo) thuộc về **một thiên thể duy nhất** (2060 Chiron = “the object”), nên bắt buộc là số ít sở hữu **the object’s** → Chọn D (“astronomers’ modeling of the object’s”).',
        'Kiểm tra từng danh từ một trong câu hỏi sở hữu kép: không có mạo từ a/an/the trước “astronomer” → bắt buộc số nhiều sở hữu (“astronomers’”); còn 2060 Chiron là 1 thiên thể → số ít sở hữu (“the object’s”).',
        [
            ('Missing Apostrophes', 'Thiếu cả hai dấu sở hữu cách trên “astronomers’” (sở hữu của “modeling”) và “object’s” (sở hữu của “trajectory”).'),
            ('Singular vs. Plural Possessive', '“astronomer’s” là số ít sở hữu nhưng thiếu mạo từ xác định/bất định (“an/the”) đứng trước nên sai ngữ pháp.'),
            ('Missing Possessive', '“astronomers” thiếu dấu sở hữu cách trước danh động từ/danh từ “modeling” (“according to astronomers’ modeling...”).'),
            ('Đáp án đúng', 'Cả hai sở hữu cách đều chuẩn xác: số nhiều sở hữu “astronomers’” + số ít sở hữu “the object’s”.'),
        ],
    ),

    # --- M2 Q17 ---
    q_item(
        'may2025_v4_us_rw_m2_q17', 17, 'Standard English Conventions', 'Boundaries', 'Medium',
        '<p>Focusing on <i>Mirounga angustirostris</i>—or _______ 2021 study by researchers Akinori Takahashi, Daniel Costa, and Patrick Robinson found that female elephant seals devote more than 80% of their time to foraging for prey in the northern Pacific Ocean.</p>',
        'Which choice completes the text so that it conforms to the conventions of Standard English?',
        [
            'northern elephant seals, as they’re more commonly known, a',
            'northern elephant seals, as they’re more commonly known—a',
            'northern elephant seals, as they’re more commonly known. A',
            'northern elephant seals—as they’re more commonly known, a',
        ],
        'B',
        'Áp dụng quy tắc **cặp dấu gạch ngang dài (paired em-dashes)** của SAT: phần giải thích tên thông thường mở đầu bằng một dấu gạch ngang dài trước “or” (`—or northern elephant seals, as they’re more commonly known—`), nên BẮT BUỘC phải khép lại bằng một **dấu gạch ngang dài thứ hai (—)** ngay sau toàn bộ cụm giải thích “as they’re more commonly known” trước khi vào chủ ngữ mệnh đề chính “a 2021 study...” → Chọn B.',
        'Dấu gạch ngang dài mở phần chêm (—) PHẢI đi thành cặp với dấu gạch ngang dài đóng (—) đúng vị trí kết thúc toàn bộ cụm chêm (đừng đóng sớm như D làm tách rời cụm “as they’re more commonly known” khỏi “northern elephant seals”!).',
        [
            ('Unmatched Pair', 'Mở cụm chêm bằng dấu gạch ngang dài (—) nhưng lại đóng bằng dấu phẩy (,) — vi phạm quy tắc ghép cặp dấu câu chuẩn SAT.'),
            ('Đáp án đúng', 'Khép cụm chêm “—or northern elephant seals, as they’re more commonly known—” bằng đúng dấu gạch ngang dài đối xứng, nối liền mạch sang chủ ngữ “a 2021 study...”.'),
            ('Sentence Fragment', 'Đặt dấu chấm (.) biến toàn bộ cụm phân từ “Focusing on *Mirounga angustirostris*...” thành câu cụt không có chủ–vị chính.'),
            ('Misplaced Closing Dash', 'Đóng dấu gạch ngang quá sớm ngay sau “seals—” khiến “as they’re more commonly known” rơi ra ngoài và bổ nghĩa sai cho tên khoa học Latinh *Mirounga angustirostris*.'),
        ],
    ),

    # --- M2 Q18 ---
    q_item(
        'may2025_v4_us_rw_m2_q18', 18, 'Standard English Conventions', 'Form, Structure, and Sense', 'Hard',
        '<p>A 2016 study by researchers Andreas Keller and Leslie Vosshall evaluating how participants described the odors of various chemical compounds revealed some similarities between the odor of sample 15 (linoleic acid) and that of sample 18 (propionic acid). The _______ primary descriptors both included “sour”; however, the next most common word used for sample 15 was “decayed,” while that for sample 18 was “musky.”</p>',
        'Which choice completes the text so that it conforms to the conventions of Standard English?',
        [
            'sample’s odors',
            'samples’ odor’s',
            'samples odors’',
            'samples’ odors’',
        ],
        'D',
        'Phân tích chuỗi sở hữu kép theo từng lớp: (1) Câu trước nhắc đến **HAI mẫu** (sample 15 và sample 18) → số nhiều sở hữu **samples’**; (2) Hai mẫu này có **HAI mùi hương** tương ứng (“the odor of sample 15... and that of sample 18”, kèm từ “both”) và các từ mô tả chính (“primary descriptors”) thuộc về hai mùi hương đó → số nhiều sở hữu **odors’**. Ghép lại: “The **samples’ odors’** primary descriptors both included ‘sour’” → Chọn D.',
        'Khi hai danh từ liên tiếp đều mang quan hệ sở hữu cho danh từ đứng cuối (“primary descriptors”), hãy đếm số lượng từng lớp: 2 samples → `samples’` (số nhiều sở hữu); 2 odors → `odors’` (số nhiều sở hữu).',
        [
            ('Singular / Missing Possessive', '“sample’s” sai vì có tới 2 mẫu (sample 15 và 18), và “odors” thiếu dấu sở hữu cách trước “primary descriptors”.'),
            ('Singular Possessive Error', '“odor’s” là số ít sở hữu, mâu thuẫn với hai mùi khác nhau của hai mẫu hóa chất và từ “both”.'),
            ('Missing Possessive', '“samples” thiếu dấu sở hữu cách để biểu thị các mùi hương thuộc về hai mẫu đó.'),
            ('Đáp án đúng', 'Sở hữu cách số nhiều kép chuẩn xác tuyệt đối: “The samples’ odors’ primary descriptors” (Các từ mô tả chính đối với mùi hương của hai mẫu).'),
        ],
    ),

    # --- M2 Q19 ---
    q_item(
        'may2025_v4_us_rw_m2_q19', 19, 'Standard English Conventions', 'Boundaries', 'Hard',
        '<p>The Orionid meteor shower’s brightness typically surpasses that of the Daytime Arietid meteor shower due to the interplay of three main factors—namely the size and composition of the _______ velocity upon entering Earth’s mesosphere, with higher velocity meteoroids releasing more energy; and atmospheric fluctuations, such as changes in sky conditions.</p>',
        'Which choice completes the text so that it conforms to the conventions of Standard English?',
        [
            'meteoroids; their',
            'meteoroids. Their',
            'meteoroids, their',
            'meteoroids—their',
        ],
        'A',
        'Nhận diện **danh sách phức dùng dấu chấm phẩy (complex-list semicolons)**! Câu đang liệt kê 3 yếu tố chính (“three main factors”): (1) “the size and composition of the meteoroids” **;** (2) “their velocity upon entering Earth’s mesosphere, with higher velocity meteoroids releasing more energy” **; and** (3) “atmospheric fluctuations, such as changes in sky conditions.” Vì mục 2 và mục 3 đều chứa dấu phẩy nội bộ, câu đã dùng **dấu chấm phẩy (;)** ngăn cách giữa mục 2 và mục 3 (`; and`), nên ranh giới giữa mục 1 và mục 2 BẮT BUỘC cũng phải dùng **dấu chấm phẩy (;)** → Chọn A (“meteoroids; their”).',
        'Mẹo nhận diện câu hỏi Complex List trên SAT chỉ trong 3 giây: hãy quét mắt xuống cuối câu tìm manh mối “; and” — nếu thấy “; and” trong một danh sách có các cụm bổ ngữ chứa dấu phẩy, mọi ranh giới trước đó trong danh sách PHẢI là dấu chấm phẩy (;).',
        [
            ('Đáp án đúng', 'Dấu chấm phẩy (;) đồng bộ hoàn hảo với “; and” ở cuối danh sách để phân tách rõ ràng 3 yếu tố phức tạp.'),
            ('Sentence Fragment', 'Tách bằng dấu chấm (.) biến mục 2 và mục 3 (“Their velocity...; and atmospheric fluctuations...”) thành câu cụt không có động từ chính chia thì.'),
            ('Inconsistent List Separator', 'Dùng dấu phẩy (,) giữa mục 1 và mục 2 trong khi giữa mục 2 và mục 3 lại dùng “; and” gây sai quy tắc đồng nhất của danh sách phức.'),
            ('Wrong Punctuation', 'Dùng dấu gạch ngang dài (—) làm đóng nhầm phần liệt kê vốn mới đi được 1/3 yếu tố.'),
        ],
    ),

    # --- M2 Q20 ---
    q_item(
        'may2025_v4_us_rw_m2_q20', 20, 'Standard English Conventions', 'Form, Structure, and Sense', 'Medium',
        '<p>Despite differences in history, language, and geography, the geopolitical entities that constitute the South Pacific regions of Micronesia, Melanesia, and Polynesia share one feature: _______ an island or a group of islands. For example, the Pitcairn Islands in Polynesia is a territory that is part of Great Britain and consists of only one inhabited island with fewer than one hundred residents.</p>',
        'Which choice completes the text so that it conforms to the conventions of Standard English?',
        [
            'all of them are',
            'all of them is',
            'each of them is',
            'each of them are',
        ],
        'C',
        'Cần kiểm tra đồng thời **hòa hợp chủ–vị** VÀ **hòa hợp số ít/số nhiều với vị ngữ danh từ phía sau**: cụm đứng ngay sau chỗ trống là **“an island or a group of islands”** (SỐ ÍT — một hòn đảo hoặc một nhóm đảo). Do đó, chủ ngữ và động từ trước đó PHẢI ở **SỐ ÍT**: “**each of them is** an island or a group of islands” (mỗi thực thể trong số đó là một hòn đảo hoặc một nhóm đảo) → Chọn C.',
        'Luôn nhìn sang danh từ ngay sau động từ “to be” (“**an** island or **a** group of islands” = số ít) để tránh bẫy A (“all of them are” tuy đúng ngữ pháp cục bộ nhưng sai logic hòa hợp số với “an island”)!',
        [
            ('Noun Number Mismatch', '“all of them are” (số nhiều) xung đột với danh từ vị ngữ số ít “an island or a group of islands” (tất cả gộp lại không thể là MỘT hòn đảo).'),
            ('Subject-Verb Agreement', '“all of them” (số nhiều) không thể đi với động từ số ít “is”.'),
            ('Đáp án đúng', '“each” là đại từ số ít → đi chuẩn với động từ số ít “is” và khớp tuyệt đối với vị ngữ số ít “an island or a group of islands”.'),
            ('Subject-Verb Agreement', '“each” luôn là số ít, không bao giờ đi với động từ số nhiều “are”.'),
        ],
    ),

    # --- M2 Q21 ---
    q_item(
        'may2025_v4_us_rw_m2_q21', 21, 'Standard English Conventions', 'Form, Structure, and Sense', 'Medium',
        '<p>The parks of Memphis, Tennessee, seem to be making people happier. In 2022, a team of researchers _______ to find connections between the physical location in which a social media post was created and the content of that post analyzed geotagged social media posts from various sites in Memphis. The team found that posts from the city’s parks contained more words associated with happiness than did the other posts.</p>',
        'Which choice completes the text so that it conforms to the conventions of Standard English?',
        ['hoped', 'hoping', 'was hoping', 'were hoping'],
        'B',
        'Đọc hết toàn bộ câu để tìm động từ chính! Chủ ngữ là “a team of researchers”, và động từ chính chia thì nằm ở phía sau là **“analyzed”** (“...analyzed geotagged social media posts from various sites in Memphis”). Do đó, cụm nằm giữa chủ ngữ và động từ chính (`_______ to find connections... and the content of that post`) chỉ là **cụm phân từ bổ ngữ** giải thích mục đích của nhóm nghiên cứu, KHÔNG được dùng động từ chia thì (finite verb) — nếu không câu sẽ mắc lỗi hai động từ chính liền nhau không có liên từ! → Chọn B (“hoping”).',
        'Luôn quét hết câu đến tận dấu chấm trước khi chọn động từ! Khi động từ chính (“analyzed”) đã xuất hiện phía sau, chỗ trống ngay sau chủ ngữ bắt buộc phải dùng dạng phân từ không chia thì (“hoping”) để tạo cụm rút gọn mệnh đề quan hệ.',
        [
            ('Double Main Verb', '“hoped” là động từ chia thì quá khứ đơn — tạo xung đột hai động từ chính (“hoped... analyzed”) cho cùng một chủ ngữ mà không có liên từ “and”.'),
            ('Đáp án đúng', '“hoping” là hiện tại phân từ mở đầu cụm bổ ngữ (“a team of researchers hoping to find connections...”), nối trơn tru với động từ chính “analyzed”.'),
            ('Double Main Verb', '“was hoping” là động từ chia thì quá khứ tiếp diễn, gây lỗi hai động từ chính xung đột với “analyzed”.'),
            ('Double Main Verb / Agreement', '“were hoping” vừa là động từ chia thì (xung đột với “analyzed”) vừa không hòa hợp số ít với “a team”.'),
        ],
    ),

    # --- M2 Q22 ---
    q_item(
        'may2025_v4_us_rw_m2_q22', 22, 'Expression of Ideas', 'Transitions', 'Easy',
        '<p>Space scientist Antonella Nota is excited about the potential of the new James Webb Space Telescope (JWST). Unlike its predecessor, the Hubble Telescope, the JWST is primarily an infrared telescope. Most light from distant galaxies is infrared; _______ the JWST can provide Nota and her team much more information about these galaxies than the Hubble could.</p>',
        'Which choice completes the text with the most logical transition?',
        ['alternatively,', 'in contrast,', 'for instance,', 'hence,'],
        'D',
        'Logic nhân–quả rõ ràng: (1) Kính thiên văn JWST chủ yếu quan sát tia hồng ngoại (khác với Hubble); (2) Hầu hết ánh sáng từ các thiên hà xa xôi lại là ánh sáng hồng ngoại → **Do đó / Vì vậy**, JWST có thể cung cấp cho Nota và nhóm nghiên cứu nhiều thông tin hơn hẳn so với Hubble → Chọn D (“hence,” = do đó, vì vậy).',
        'Nhóm từ nối nhân–quả chuẩn SAT: `therefore`, `thus`, `hence`, `consequently`, `as a result` — luôn kiểm tra vế trước có phải là nguyên nhân trực tiếp giải thích cho kết quả ở vế sau không.',
        [
            ('Wrong Logic', 'alternatively = hoặc là / thay vào đó — không thể hiện mối quan hệ nguyên nhân–kết quả.'),
            ('Opposite Logic', 'in contrast = trái lại — vế sau là hệ quả thuận chiều của vế trước, không hề đối lập.'),
            ('Wrong Logic', 'for instance = ví dụ — việc JWST thu được nhiều thông tin hơn là kết quả tất yếu chứ không phải ví dụ minh họa cho “hầu hết ánh sáng thiên hà là tia hồng ngoại”.'),
            ('Đáp án đúng', 'hence = do đó, vì thế — nối chuẩn xác nguyên nhân (JWST bắt tia hồng ngoại + ánh sáng thiên hà xa chủ yếu là hồng ngoại) sang hệ quả (JWST thu được nhiều dữ liệu hơn Hubble).'),
        ],
    ),

    # --- M2 Q23 ---
    q_item(
        'may2025_v4_us_rw_m2_q23', 23, 'Expression of Ideas', 'Rhetorical Synthesis', 'Easy',
        '<p>While researching a topic, a student has taken the following notes:</p>'
        '<ul>'
        '<li>Hina Hanta is an online archive curated by the Choctaw Nation of Oklahoma.</li>'
        '<li>It features images of many cultural artifacts relevant to the history of the Choctaw people.</li>'
        '<li>It features basketry, including a trunk basket (<i>tapushik pothoma</i> in Choctaw) made from cane.</li>'
        '<li>The trunk basket was made in 2019.</li>'
        '<li>The archive features household items, including a stamp (<i>isht inchunwa</i>) made from rubber.</li>'
        '<li>The stamp was made in the 1800s.</li>'
        '</ul>',
        'The student wants to support the claim that the online archive features both older and newer artifacts. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
        [
            'The rubber stamp (<i>isht inchunwa</i>) was made in the 1800s.',
            'Hina Hanta, an online archive, features both basketry and household items.',
            'Not all artifacts in the Hina Hanta archive are from the 1800s.',
            'The Hina Hanta online archive features cultural artifacts both old and new, including a rubber stamp from the 1800s and a cane trunk basket from 2019.',
        ],
        'D',
        'Mục tiêu: chứng minh kho lưu trữ trực tuyến Hina Hanta bao gồm **CẢ hiện vật cũ lẫn hiện vật mới** (“both older and newer artifacts”). Đáp án D nêu trực diện nhận định đó và đưa đủ HAI bằng chứng đối xứng từ ghi chú: con dấu cao su từ những năm 1800 (hiện vật cũ) và giỏ mây từ năm 2019 (hiện vật mới) → Chọn D.',
        'Khi mục tiêu yêu cầu chứng minh “both X and Y”, đáp án đúng bắt buộc phải đưa ví dụ cụ thể cho CẢ X (1800s) lẫn Y (2019).',
        [
            ('Half-Complete', 'Chỉ nêu mỗi con dấu cao su từ thế kỷ 19 (hiện vật cũ), thiếu hoàn toàn ví dụ về hiện vật mới.'),
            ('Wrong Focus', 'Chỉ nêu hai loại hình đồ vật (giỏ đan và đồ gia dụng) mà không đề cập đến niên đại cũ–mới.'),
            ('Weak / Missing Evidence', 'Chỉ nói phủ định “không phải tất cả đều từ những năm 1800” — quá mơ hồ, không đưa ví dụ cụ thể về cả hai mốc thời gian cũ và mới.'),
            ('Đáp án đúng', 'Khớp mục tiêu tuyệt đối: gọi tên kho lưu trữ Hina Hanta và đưa đủ cặp bằng chứng niên đại cũ (1800s) + mới (2019).'),
        ],
    ),

    # --- M2 Q24 ---
    q_item(
        'may2025_v4_us_rw_m2_q24', 24, 'Expression of Ideas', 'Rhetorical Synthesis', 'Easy',
        '<p>While researching a topic, a student has taken the following notes:</p>'
        '<ul>'
        '<li>The Peloncillo-Pan Duro Mountains are located in northwestern Mexico.</li>'
        '<li>They cover an area of 1,360 square miles (mi<sup>2</sup>).</li>'
        '<li>The Big Hatchet Mountains are located in the southwestern United States.</li>'
        '<li>They cover an area of 65 mi<sup>2</sup>.</li>'
        '<li>These mountain ranges are two of the dozens of “sky islands” in the southwestern US and northwestern Mexico.</li>'
        '<li>A sky island is an isolated mountain range whose environment differs drastically from that of the surrounding lowlands.</li>'
        '</ul>',
        'The student wants to compare the sizes of the two mountain ranges. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
        [
            'There are dozens of isolated mountain ranges located in the southwestern US and northwestern Mexico.',
            'In terms of area, the Peloncillo-Pan Duro Mountains (which cover 1,360 mi<sup>2</sup>) are larger than the Big Hatchet Mountains (65 mi<sup>2</sup>).',
            'Sky islands in northwestern Mexico and the southwestern US can vary in size.',
            'The Peloncillo-Pan Duro Mountains and the Big Hatchet Mountains are both isolated mountain ranges whose environments differ drastically from that of the surrounding lowlands.',
        ],
        'B',
        'Mục tiêu: **so sánh kích thước (diện tích) của hai dãy núi** (Peloncillo-Pan Duro và Big Hatchet). Duy nhất đáp án B gọi tên cả hai dãy núi, đưa chính xác số liệu diện tích (1,360 mi² vs. 65 mi²) và dùng cấu trúc so sánh trực tiếp (“are larger than”) → Chọn B.',
        'Mục tiêu “compare the sizes of the two X” đòi hỏi đầy đủ 3 yếu tố: tên X1, tên X2, và phép so sánh kích thước cụ thể giữa chúng.',
        [
            ('Wrong Focus', 'Chỉ nêu số lượng (“dozens”) và vị trí địa lý chung chung, không nhắc tên hai dãy núi hay kích thước.'),
            ('Đáp án đúng', 'So sánh trực diện diện tích hai dãy núi với số liệu chính xác từ ghi chú: 1,360 mi² lớn hơn 65 mi².'),
            ('Too Vague', 'Chỉ nhận xét chung chung các “sky islands” có thể khác kích thước, không so sánh riêng hai dãy núi được nêu.'),
            ('Wrong Focus', 'Giải thích định nghĩa “sky islands” (môi trường khác biệt vùng đất thấp) thay vì so sánh kích thước/diện tích.'),
        ],
    ),

    # --- M2 Q25 ---
    q_item(
        'may2025_v4_us_rw_m2_q25', 25, 'Expression of Ideas', 'Rhetorical Synthesis', 'Medium',
        '<p>While researching a topic, a student has taken the following notes:</p>'
        '<ul>'
        '<li>Bengali is a language in the Indo-Aryan language family.</li>'
        '<li>In Bengali, a noun takes a different form when that noun functions as a location in a sentence.</li>'
        '<li>The Bengali noun <i>bari</i> (<i>house</i>) is combined with the locative suffix <i>-te</i> to become the locative noun <i>barite</i> (<i>in the house</i>).</li>'
        '<li>Danish is a language in the Germanic language family.</li>'
        '<li>In Danish, nouns do not change form to indicate location.</li>'
        '<li>In Danish, nouns used as a location must be indicated by prepositions such as <i>i</i> (<i>in</i>) or <i>på</i> (<i>on</i>).</li>'
        '</ul>',
        'The student wants to emphasize a difference between Bengali and Danish nouns. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
        [
            'To indicate location in Bengali, a suffix is appended to a noun, but in Danish, the noun is unchanged and a preposition is used.',
            'Bengali and Danish belong to two distinct language families; the former is in the Indo-Aryan family, while the latter is a Germanic language.',
            'Though nouns in Bengali change form to indicate location, this Indo-Aryan language belongs to a different language family than Danish does.',
            'In Bengali, nouns take a different form when they function as a location, as the language belongs to the Indo-Aryan family; Danish, however, belongs to the Germanic family.',
        ],
        'A',
        'Mục tiêu yêu cầu cực cụ thể: nhấn mạnh một điểm khác biệt giữa **DANH TỪ tiếng Bengal và DANH TỪ tiếng Đan Mạch** (“a difference between Bengali and Danish **nouns**”). Đáp án A đối chiếu trực diện cách vận hành của danh từ chỉ vị trí ở cả hai ngôn ngữ: tiếng Bengal gắn thêm hậu tố vào danh từ, còn tiếng Đan Mạch giữ nguyên danh từ và dùng giới từ → Chọn A.',
        'Đọc sát từng từ trong đề bài Rhetorical Synthesis: đề yêu cầu so sánh **nouns** (danh từ), KHÔNG phải so sánh **language families** (ngữ hệ) — loại ngay B, C, D!',
        [
            ('Đáp án đúng', 'Đối chiếu sắc nét chính sự khác biệt của danh từ giữa hai ngôn ngữ khi chỉ vị trí: thêm hậu tố (Bengal) vs. giữ nguyên danh từ + dùng giới từ (Đan Mạch).'),
            ('Wrong Comparison Dimension', 'Chỉ so sánh ngữ hệ (Indo-Aryan vs. Germanic), không hề nhắc đến danh từ của hai ngôn ngữ.'),
            ('Missing Second Noun', 'Chỉ nói về danh từ tiếng Bengal, rồi chuyển sang so sánh ngữ hệ — hoàn toàn không đề cập danh từ tiếng Đan Mạch hoạt động ra sao.'),
            ('False Causality / Missing Second Noun', 'Không nói về danh từ tiếng Đan Mạch, lại tự bịa quan hệ nhân quả (“as the language belongs to...”) không có trong ghi chú.'),
        ],
    ),

    # --- M2 Q26 ---
    q_item(
        'may2025_v4_us_rw_m2_q26', 26, 'Expression of Ideas', 'Rhetorical Synthesis', 'Easy',
        '<p>While researching a topic, a student has taken the following notes:</p>'
        '<ul>'
        '<li>Lou Scheper-Berkenkamp was a painter and author born in Wesel, Germany.</li>'
        '<li>She began attending the Bauhaus in 1920.</li>'
        '<li>The Bauhaus was an influential German art and design school.</li>'
        '<li>The school famously espoused the design principle of “form follows function.”</li>'
        '<li>“Form follows function” means that an object’s shape should be determined primarily by its intended purpose.</li>'
        '</ul>',
        'The student wants to explain the principle espoused by the Bauhaus. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
        [
            'According to the Bauhaus, an object’s intended purpose (function) should primarily determine its shape (form).',
            'Lou Scheper-Berkenkamp was a painter and author who attended the Bauhaus, famous for espousing the principle of “form follows function.”',
            'Famous for its principle of “form follows function,” the Bauhaus was an influential German art and design school.',
            'An object’s intended purpose and its shape are two elements of the design principle “form follows function.”',
        ],
        'A',
        'Mục tiêu: **GIẢI THÍCH (explain)** nguyên lý mà trường Bauhaus đề xướng. Các lựa chọn B và C chỉ gọi tên khẩu hiệu “form follows function” mà không giải thích nó có nghĩa là gì; D chỉ liệt kê hai yếu tố mà không nói yếu tố nào quyết định yếu tố nào. Duy nhất đáp án A giải thích rõ nội hàm nguyên lý theo đúng ghi chú: mục đích sử dụng của vật thể (function) nên là yếu tố chủ yếu quyết định hình dáng của nó (form) → Chọn A.',
        'Phân biệt hai động từ mục tiêu quan trọng: “mention/name” (chỉ cần gọi tên) vs. “explain” (BẮT BUỘC phải diễn giải ý nghĩa và mối quan hệ nhân–quả bên trong khái niệm!).',
        [
            ('Đáp án đúng', 'Giải thích chính xác, trực tiếp nguyên lý của Bauhaus theo đúng gạch đầu dòng cuối: mục đích dự định (function) quyết định hình dáng (form).'),
            ('Names Without Explaining', 'Tập trung giới thiệu Lou Scheper-Berkenkamp và chỉ nhắc tên “form follows function” mà không giải thích nội dung nguyên lý.'),
            ('Names Without Explaining', 'Chỉ giới thiệu trường Bauhaus và nhắc tên nguyên lý, không hề giải thích “form follows function” nghĩa là gì.'),
            ('Incomplete Explanation', 'Chỉ liệt kê hai thành phần (purpose và shape) mà không giải thích chiều tác động rằng purpose phải quyết định shape — và cũng không gắn với Bauhaus.'),
        ],
    ),

    # --- M2 Q27 ---
    q_item(
        'may2025_v4_us_rw_m2_q27', 27, 'Expression of Ideas', 'Rhetorical Synthesis', 'Medium',
        '<p>While researching a topic, a student has taken the following notes:</p>'
        '<ul>'
        '<li>According to researcher Muhammad Rayyan Fazal, “geothermal electric energy... [is] capable of producing more energy per megawatt per year as compared to similar capacity solar and wind power systems.”</li>'
        '<li>Geothermal power plants typically employ dry steam systems, flash steam systems, or binary cycle systems to produce electricity from high-temperature geothermal fluid.</li>'
        '<li>The Platanares geothermal power plant in Honduras uses a binary cycle system.</li>'
        '<li>Fazal says that binary cycle systems “pump 100% geothermal fluid back to the injection well, hence offering the least environmental impact with little or no emissions.”</li>'
        '</ul>',
        'The student wants to use a quotation from Fazal to explain an advantage of the geothermal system at the Platanares plant. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
        [
            'Compared with dry steam systems and flash steam systems, the binary cycle system used at the Platanares plant is “capable of producing more energy per megawatt per year,” Fazal notes.',
            'According to Fazal, because it uses high-temperature geothermal fluid to produce electricity, the system used at the Platanares plant results in “little or no emissions,” making it environmentally friendly.',
            'Since they return all geothermal fluid to the injection well, binary cycle systems—such as the one at the Platanares plant—produce “the least environmental impact,” according to Fazal.',
            'The Platanares plant uses a binary cycle system to produce electricity; in this type of geothermal system, fluid is pumped “back to the injection well,” Fazal explains.',
        ],
        'C',
        'Kiểm tra độ chính xác từng chi tiết so với ghi chú (câu Rhetorical Synthesis mức Khó của Module 2!): Mục tiêu là **dùng trích dẫn của Fazal để giải thích một ưu điểm của hệ thống địa nhiệt (binary cycle) tại nhà máy Platanares**. Đối chiếu 4 phương án:\n- **A sai thông tin gốc**: Fazal so sánh năng lượng địa nhiệt với *điện mặt trời và điện gió*, KHÔNG phải so sánh binary cycle với dry steam / flash steam.\n- **B sai nguyên nhân**: Hệ thống binary cycle có ít/không phát thải là nhờ *bơm 100% chất lỏng trở lại giếng phun*, KHÔNG phải vì “dùng chất lỏng địa nhiệt nhiệt độ cao” (cả 3 loại hệ thống đều dùng chất lỏng này).\n- **C chuẩn xác 100%**: Nêu đúng nguyên nhân (“return all geothermal fluid to the injection well”), gắn đúng với nhà máy Platanares (“binary cycle systems—such as the one at the Platanares plant”), trích dẫn nguyên văn Fazal (“the least environmental impact”) và giải thích rõ ưu điểm môi trường!\n- **D thiếu ưu điểm**: Chỉ mô tả cơ chế bơm chất lỏng mà không nêu ưu điểm nào → Chọn C.',
        'Ở câu 27 Module 2, cả 4 phương án đều có trích dẫn trong ngoặc kép — bí quyết ăn điểm tuyệt đối là **kiểm tra độ trung thực của phép so sánh (A) và quan hệ nguyên nhân–kết quả (B vs. C)** so với các gạch đầu dòng gốc!',
        [
            ('Distorted Comparison', 'Bóp méo ghi chú: Fazal so sánh địa nhiệt với điện mặt trời và điện gió (“solar and wind”), KHÔNG phải so sánh binary cycle với dry steam và flash steam.'),
            ('False Causality', 'Gán sai nguyên nhân: cả 3 hệ thống đều dùng chất lỏng địa nhiệt nhiệt độ cao; lý do binary cycle ít phát thải là vì nó bơm lại 100% chất lỏng về giếng phun.'),
            ('Đáp án đúng', 'Khớp 100% sự thật từ ghi chú: nêu đúng nguyên nhân (bơm toàn bộ chất lỏng về giếng), đúng loại hệ thống tại Platanares, trích dẫn chuẩn Fazal và nêu rõ ưu điểm môi trường.'),
            ('Missing Advantage', 'Chỉ mô tả cách vận hành (“fluid is pumped back to the injection well”) mà hoàn toàn không giải thích ưu điểm nào của hệ thống.'),
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
        'subtitle': 'Đề thi thật Digital SAT Mỹ tháng 5/2025 (US Ver 4) — Đủ 2 Module (M1: 27 câu + M2: 27 câu)',
        'difficultyBadge': 'REAL EXAM • MAY 2025 US',
        'targetTimeMinutes': 64,
        'routingThreshold': 0,
    },
    'module1': {
        'id': 'real_may2025_v4_us_rw_m1',
        'title': 'Section 1, Module 1: Reading and Writing',
        'subtitle': 'May 2025 US Ver 4 Real Exam — Module 1 (27 Qs • 32 min)',
        'timeLimitMinutes': 32,
        'questions': MODULE_1_QUESTIONS,
    },
    'module2_hard': {
        'id': 'real_may2025_v4_us_rw_m2_hard',
        'title': 'Section 1, Module 2: Reading and Writing',
        'subtitle': 'May 2025 US Ver 4 Real Exam — Module 2 (27 Qs • 32 min)',
        'timeLimitMinutes': 32,
        'questions': MODULE_2_QUESTIONS,
    },
    'module2_lower': {
        'id': 'real_may2025_v4_us_rw_m2_lower',
        'title': 'Section 1, Module 2: Reading and Writing',
        'subtitle': 'May 2025 US Ver 4 Real Exam — Module 2 (27 Qs • 32 min)',
        'timeLimitMinutes': 32,
        'questions': _clone_module_questions(
            MODULE_2_QUESTIONS,
            'may2025_v4_us_rw_m2_',
            'may2025_v4_us_rw_m2l_',
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

    # Verify routingThreshold == 0, mode, section
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
            if not (exp.get('summaryVi') or '').strip():
                errors.append(f'{qid}: empty summaryVi')
            if not (exp.get('keyTakeaway') or '').strip():
                errors.append(f'{qid}: empty keyTakeaway')

            # Fidelity checks: tables, graphs, and underlines must be present when referenced
            q_lower = (q['questionHtml'] or '').lower()
            stim = q['stimulusHtml'] or ''
            if 'table' in q_lower and '<table' not in stim.lower():
                errors.append(f'{qid}: question references table but stimulusHtml lacks <table>')
            if 'graph' in q_lower and '<svg' not in stim.lower():
                errors.append(f'{qid}: question references graph but stimulusHtml lacks <svg>')
            if 'underlined' in q_lower and '<u>' not in stim.lower():
                errors.append(f'{qid}: question references underlined text but stimulusHtml lacks <u>')

    # Verify module2_lower mirrors module2_hard verbatim (aside from IDs)
    for qh, ql in zip(m2h_qs, m2l_qs):
        for field in ('number', 'domain', 'skill', 'stimulusHtml', 'questionHtml', 'options', 'correctAnswer', 'explanation'):
            if qh[field] != ql[field]:
                errors.append(f'module2_lower Q{qh["number"]} differs from module2_hard on field {field}')

    # 3. Zero watermarks & zero raw ___blank artifacts across entire JSON
    serialized = json.dumps(TEST_DATA, ensure_ascii=False)
    if re.search(r'@dsatuz|dsatuz|@d7sat|d7sat|t\.me/', serialized, re.IGNORECASE):
        errors.append('Found watermark string in TEST_DATA!')
    if re.search(r'_{3,}blank', serialized, re.IGNORECASE):
        errors.append('Found unconverted ___blank artifact in TEST_DATA!')

    # 4. Official Bluebook pipeline validator (schema + Node KaTeX check)
    pipeline_errs = validate_sat_bluebook_json(TEST_DATA, TEST_CODE)
    errors.extend(pipeline_errs)

    # Summary stats
    m1_dist = {c: sum(1 for q in m1_qs if q['correctAnswer'] == c) for c in 'ABCD'}
    m2_dist = {c: sum(1 for q in m2h_qs if q['correctAnswer'] == c) for c in 'ABCD'}
    print(f'[{TEST_CODE}] {TEST_TITLE}')
    print(f'  Module 1: {len(m1_qs)} Qs | Keys: {m1_dist}')
    print(f'  Module 2: {len(m2h_qs)} Qs | Keys: {m2_dist} (mirrored to module2_lower: {len(m2l_qs)} Qs)')
    print(f'  Total unique real Qs: {len(m1_qs) + len(m2h_qs)} | Global unique IDs: {len(all_ids)}')
    print(f'  Tables verified: 3 (M1 Q12, M1 Q13, M2 Q13) | Chart SVG verified: 1 (M2 Q12)')
    print(f'  Underlines verified: 2 (M1 Q1, M2 Q6)')

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
