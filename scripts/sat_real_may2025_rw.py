# -*- coding: utf-8 -*-
"""
Digital SAT 1500+ Real Past Exams — May 2025 Reading & Writing (Full Adaptive • 81 Qs)
- Module 1: 27 verbatim questions (32 min) — source: mod1_rw.txt
- Module 2 Hard Route: 27 verbatim questions (32 min) — source: mod3_rw.txt
- Module 2 Lower/Easy Route: 27 verbatim questions (32 min) — source: mod2_rw.txt

All underlines, tables, line graphs, and mathematical/scientific notations have been
visually verified against the original exam PNGs, and all 81 answer keys have passed
an independent 2-pass audit.
"""

import os
import re
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

TEST_CODE = 'real_may2025_rw'
FOLDER_KEY = 'real_rw'
ORDER_INDEX = 1
TEST_TITLE = '🏛️ Real Exam — May 2025 Reading & Writing (Full Adaptive • 81 Qs)'


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


def _svg_m1_q10_employment():
    """Recreates the exact May 2025 M1 Q10 line graph (Czech Republic vs Austria, 1995–2013)."""
    years = [1995, 1998, 2001, 2004, 2007, 2010, 2013]
    cz_vals = [231, 214, 183, 150, 129, 111, 115]
    at_vals = [19, 19, 18, 20, 20, 20, 23]

    x_start, x_step = 100, 57
    xs = [x_start + i * x_step for i in range(len(years))]
    x_left, x_right = 75, 470
    y_top, y_bot = 20, 220  # 200px height for 0..250 -> 0.8 px per unit

    def fy(v):
        return y_bot - v * 0.8

    parts = []
    # Horizontal gridlines + Y-axis labels
    for val in range(0, 251, 25):
        y = fy(val)
        stroke = '#334155' if val == 0 else '#cbd5e1'
        sw = '1.5' if val == 0 else '1'
        parts.append(f'<line x1="{x_left}" y1="{y:.1f}" x2="{x_right}" y2="{y:.1f}" stroke="{stroke}" stroke-width="{sw}"/>')
        parts.append(f'<text x="{x_left - 8}" y="{y + 3.5:.1f}" font-size="10.5" text-anchor="end" fill="#1e293b" font-family="sans-serif">{val}</text>')

    # Vertical gridlines + X-axis rotated year labels
    for x, yr in zip(xs, years):
        parts.append(f'<line x1="{x}" y1="{y_top}" x2="{x}" y2="{y_bot}" stroke="#cbd5e1" stroke-width="1"/>')
        parts.append(f'<line x1="{x}" y1="{y_bot}" x2="{x}" y2="{y_bot + 5}" stroke="#334155" stroke-width="1.2"/>')
        parts.append(
            f'<text x="{x}" y="{y_bot + 19}" font-size="10.5" text-anchor="end" fill="#1e293b" '
            f'font-family="sans-serif" transform="rotate(-38 {x} {y_bot + 19})">{yr}</text>'
        )

    # Y axis line
    parts.append(f'<line x1="{x_left}" y1="{y_top}" x2="{x_left}" y2="{y_bot}" stroke="#334155" stroke-width="1.5"/>')

    # Czech Republic polyline (solid) + upward triangles
    cz_pts = ' '.join(f'{x},{fy(v):.1f}' for x, v in zip(xs, cz_vals))
    parts.append(f'<polyline points="{cz_pts}" fill="none" stroke="#0f172a" stroke-width="2.2"/>')
    for x, v in zip(xs, cz_vals):
        y = fy(v)
        parts.append(f'<polygon points="{x},{y - 5.5:.1f} {x - 5},{y + 4:.1f} {x + 5},{y + 4:.1f}" fill="#0f172a"/>')

    # Austria polyline (dashed) + gray-filled bordered squares
    at_pts = ' '.join(f'{x},{fy(v):.1f}' for x, v in zip(xs, at_vals))
    parts.append(f'<polyline points="{at_pts}" fill="none" stroke="#334155" stroke-width="2" stroke-dasharray="6,4"/>')
    for x, v in zip(xs, at_vals):
        y = fy(v)
        parts.append(f'<rect x="{x - 4.2:.1f}" y="{y - 4.2:.1f}" width="8.4" height="8.4" fill="#cbd5e1" stroke="#0f172a" stroke-width="1.5"/>')

    # Axis titles
    parts.append(
        '<text x="20" y="120" font-size="11.5" font-weight="600" text-anchor="middle" fill="#0f172a" '
        'font-family="sans-serif" transform="rotate(-90 20 120)">Number of employees (in thousands)</text>'
    )
    parts.append(
        '<text x="272" y="264" font-size="11.5" font-weight="600" text-anchor="middle" fill="#0f172a" '
        'font-family="sans-serif">Year</text>'
    )

    # Legend box
    parts.append('<rect x="172" y="274" width="200" height="44" fill="#ffffff" stroke="#475569" stroke-width="1.1"/>')
    parts.append('<line x1="184" y1="289" x2="230" y2="289" stroke="#0f172a" stroke-width="2.2"/>')
    parts.append('<polygon points="207,283.5 202,293 212,293" fill="#0f172a"/>')
    parts.append('<text x="240" y="293" font-size="11.5" fill="#0f172a" font-family="sans-serif">Czech Republic</text>')

    parts.append('<line x1="184" y1="307" x2="230" y2="307" stroke="#334155" stroke-width="2" stroke-dasharray="6,4"/>')
    parts.append('<rect x="202.8" y="302.8" width="8.4" height="8.4" fill="#cbd5e1" stroke="#0f172a" stroke-width="1.5"/>')
    parts.append('<text x="240" y="311" font-size="11.5" fill="#0f172a" font-family="sans-serif">Austria</text>')

    return (
        '<div style="background:#f8fafc;border:1px solid #cbd5e1;border-radius:10px;padding:12px 14px;margin-bottom:12px;">'
        '<div style="font-family:\'Segoe UI\',sans-serif;font-size:13px;font-weight:800;color:#0f172a;'
        'text-align:center;line-height:1.35;margin-bottom:6px;">'
        'Employment in Agriculture, Hunting, and Forestry in the Czech Republic and Austria, 1995–2013</div>'
        '<svg viewBox="0 0 495 326" xmlns="http://www.w3.org/2000/svg" style="max-width:485px;">'
        '<rect x="0" y="0" width="495" height="326" fill="#ffffff"/>'
        f'{"".join(parts)}'
        '</svg></div>'
    )


# ============================================================================
# MODULE 1 — ROUTING MODULE (27 Qs — Source: mod1_rw.txt)
# ============================================================================

def get_m1_questions():
    return [
        _q(
            'may2025_rw_m1_q1', 1, 'Craft and Structure', 'Words in Context', 'Easy',
            '<p>The National Heritage Fellowship was created to _______ exceptional folk and traditional artists in the United States. One artist who received the fellowship, the Irish American accordionist Joe Derrane, was chosen for his lifetime contributions to the arts.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            ['honor', 'begin', 'distract', 'overshadow'],
            'A',
            'Manh mối ngữ cảnh: Giải thưởng/Học bổng Di sản Quốc gia (National Heritage Fellowship) trao cho nghệ sĩ xuất sắc Joe Derrane vì “những đóng góp trọn đời cho nghệ thuật” → mục đích thành lập là để TÔN VINH (“honor”) các nghệ sĩ dân gian xuất sắc → Chọn A.',
            'Học bổng/giải thưởng ghi nhận đóng góp trọn đời (“chosen for his lifetime contributions”) → chọn động từ mang nghĩa tôn vinh/ghi nhận (“honor”).',
            [
                ('Đáp án đúng', 'honor = tôn vinh, vinh danh — khớp hoàn toàn với mục đích trao giải thưởng ghi nhận đóng góp trọn đời của nghệ sĩ.'),
                ('Wrong Meaning', 'begin = bắt đầu — không thể “bắt đầu các nghệ sĩ”.'),
                ('Wrong Meaning', 'distract = làm phân tâm — trái ngược với mục đích ghi nhận nghệ sĩ.'),
                ('Wrong Meaning', 'overshadow = làm lu mờ — mang nghĩa tiêu cực, trái ngược với việc trao giải tôn vinh.'),
            ],
        ),
        _q(
            'may2025_rw_m1_q2', 2, 'Craft and Structure', 'Words in Context', 'Easy',
            '<p>Some cities estimate where sidewalks are located using road maps, which is not very accurate. Maryam Hosseini and her team trained a computer program to identify sidewalks in aerial images of Boston and used it on images of Philadelphia. The program’s performance was _______ to that of the road-map method: it more accurately identified sidewalks, and it even distinguished between concrete and brick.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            ['similar', 'supportive', 'superior', 'changed'],
            'C',
            'Dấu hai chấm giải thích trực tiếp chỗ trống: chương trình máy tính “xác định vỉa hè chính xác hơn” và “thậm chí phân biệt được bê tông với gạch” so với phương pháp bản đồ vốn kém chính xác → hiệu năng VƯỢT TRỘI HƠN (“superior to”) → Chọn C.',
            'Cụm giải thích sau dấu hai chấm (“more accurately... even distinguished”) + giới từ “to” khóa chặt cụm “superior to”.',
            [
                ('Opposite Meaning', 'similar = tương tự — mâu thuẫn vì chương trình chính xác hơn hẳn phương pháp bản đồ.'),
                ('Wrong Context', 'supportive = mang tính hỗ trợ — không hợp ngữ cảnh so sánh hiệu năng giữa hai phương pháp.'),
                ('Đáp án đúng', 'superior = vượt trội hơn — vừa đúng nghĩa “chính xác hơn và phân biệt chi tiết hơn”, vừa đi chuẩn với giới từ “to”.'),
                ('Wrong Meaning / Usage', 'changed = bị thay đổi — không diễn đạt sự hơn kém và không đi tự nhiên với “to that of”.'),
            ],
        ),
        _q(
            'may2025_rw_m1_q3', 3, 'Craft and Structure', 'Words in Context', 'Easy',
            '<p>Often, the Nobel Prize in Chemistry is given to a single person, such as George de Hevesy in 1943. But recognition isn’t restricted to _______ individuals. Instead, success in fields like chemistry is usually achieved through collaboration with other experts, as was the case for Max Ferdinand Perutz, who was among those awarded for “their studies of the structures of globular proteins.”</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            ['coincidental', 'solitary', 'coordinated', 'considerate'],
            'B',
            'Mạch tương phản rõ rệt: câu 1 nhắc giải Nobel hay trao cho “a single person” (một cá nhân đơn lẻ); câu 2 nói sự ghi nhận không chỉ giới hạn ở những cá nhân ĐƠN ĐỘC (“solitary”); câu 3 đối lập bằng “Instead” — thành công thường đạt được qua “collaboration” (hợp tác) → Chọn B.',
            'Ánh xạ trực tiếp “a single person” + đối lập “Instead... collaboration” → chọn từ đồng nghĩa với “single/alone” (“solitary”).',
            [
                ('Wrong Meaning', 'coincidental = trùng hợp ngẫu nhiên — không liên quan đến việc làm việc một mình hay hợp tác.'),
                ('Đáp án đúng', 'solitary = đơn độc, làm việc một mình — song song với “a single person” và đối lập hoàn hảo với “collaboration”.'),
                ('Opposite Meaning', 'coordinated = phối hợp nhịp nhàng — đồng nghĩa với “collaboration”, ngược logic câu phủ định “isn’t restricted to... Instead”.'),
                ('Wrong Meaning', 'considerate = chu đáo, ân cần — sai ngữ cảnh hoàn toàn.'),
            ],
        ),
        _q(
            'may2025_rw_m1_q4', 4, 'Craft and Structure', 'Words in Context', 'Medium',
            '<p>The Apollo Moon landings (1969–1972) brought charged particle detectors and equipment too heavy for liftoff to the Moon and produced large amounts of data, much of which was stored on outdated technologies. A data-transfer project is making the data available again, thereby _______ the Apollo data’s usefulness, as the data are used to study the long-term effects of being on the Moon.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            ['installing', 'persisting', 'renewing', 'exceeding'],
            'C',
            'Dữ liệu Apollo trước kia lưu trên công nghệ lỗi thời nên khó dùng; nay dự án chuyển dữ liệu giúp dữ liệu “available again” (khả dụng trở lại) → qua đó LÀM MỚI / KHÔI PHỤC LẠI tính hữu ích (“renewing”) của dữ liệu → Chọn C.',
            'Cụm “making the data available again” gợi thẳng tiền tố “re-” (làm lại/khôi phục) → “renewing”.',
            [
                ('Collocation Mismatch', 'installing = cài đặt (thiết bị/phần mềm) — không dùng “install usefulness”.'),
                ('Grammar / Usage Trap', 'persisting = kiên trì/tồn tại dai dẳng — là nội động từ, không nhận tân ngữ trực tiếp “usefulness”.'),
                ('Đáp án đúng', 'renewing = khôi phục, làm mới lại — phản chiếu chuẩn xác cụm “making the data available again”.'),
                ('Wrong Direction', 'exceeding = vượt quá — không hợp lý khi nói việc chuyển dữ liệu “vượt quá tính hữu ích của dữ liệu”.'),
            ],
        ),
        _q(
            'may2025_rw_m1_q5', 5, 'Craft and Structure', 'Text Structure and Purpose', 'Medium',
            '<p>Movies that are part of larger franchises are often criticized for being predictable. Take, for instance, <i>Minions</i> (2015), which is part of the <i>Despicable Me</i> franchise. It’s true that this movie resembles earlier <i>Despicable Me</i> movies. But just because a movie has familiar elements doesn’t mean it can’t also be worth watching. Critics generally agree that <i>Minions</i> isn’t the most exciting franchise movie, but franchise movies are rarely as stale as some people claim. And some franchise movies, like <i>Creed</i> (2015), are wonderfully original.</p>',
            'Which choice best describes the overall structure of the text?',
            [
                'The text describes audiences’ reactions to a movie that is part of a larger franchise, then presents some critics’ reactions to that movie.',
                'The text discusses a common criticism of franchise movies, then argues that the criticism is mostly undeserved.',
                'The text explains why some people enjoyed a particular franchise movie, then considers why other people disliked it.',
                'The text summarizes the plot of a franchise movie, then explains how the plot is continued in a later movie in that franchise.',
            ],
            'B',
            'Cấu trúc 2 phần rõ ràng: [1] Nêu một lời chê bai phổ biến về phim thương hiệu (“often criticized for being predictable”) kèm ví dụ <i>Minions</i>; [2] Phản biện từ “But...” trở đi rằng lời chê đó phần lớn không xác đáng (“rarely as stale as some people claim” và có những phim cực kỳ sáng tạo như <i>Creed</i>) → Chọn B.',
            'Với câu Overall Structure, chia đoạn tại từ chuyển hướng (“But...”) để tóm đúng 2 bước: Nêu định kiến/phê bình → Bác bỏ định kiến đó.',
            [
                ('Scope / Distortion', 'Đoạn không đối chiếu phản ứng của khán giả với phản ứng của giới phê bình cho một bộ phim cụ thể.'),
                ('Đáp án đúng', 'Khớp chính xác 2 nhịp cấu trúc: nêu lời chỉ trích phổ biến về phim thương hiệu, rồi lập luận rằng lời chê đó phần lớn không đáng.'),
                ('Fact Distortion', 'Đoạn không phân tích lý do cụ thể vì sao người thích và người ghét một bộ phim nhất định.'),
                ('Out of Scope', 'Hoàn toàn không tóm tắt cốt truyện (plot) của bất kỳ bộ phim nào.'),
            ],
        ),
        _q(
            'may2025_rw_m1_q6', 6, 'Craft and Structure', 'Cross-Text Connections', 'Medium',
            '<p><b>Text 1</b><br/>In 2010 Chengdu, China, was named a City of Gastronomy by UNESCO in recognition of the city’s unique food culture. The honor is well known among residents of the city as well as tourists who visit. <u>It’s obvious that the selection of Chengdu by UNESCO has brought awareness to local recipes, cooking practices, and chefs and has provided a boost to the city’s tourism industry.</u></p><p><b>Text 2</b><br/>Many people in Chengdu’s restaurant industry hoped that food tourism would increase after the city was chosen as a City of Gastronomy in 2010. However, as researcher Eerang Park and colleagues argue, cities must still create effective marketing strategies to benefit fully from being named a City of Gastronomy. Without an intentional effort to promote the city’s food scene, many current and potential visitors to Chengdu may not even be aware that it’s home to uniquely delicious food.</p>',
            'Based on the texts, what would the author of Text 2 most likely say in response to the underlined claim in Text 1?',
            [
                'The naming of Chengdu as a City of Gastronomy was long overdue, given the city’s unique and delicious food.',
                'Many people worked together to help Chengdu be recognized by UNESCO, but chefs deserve the most credit for Chengdu’s selection as a City of Gastronomy.',
                'The benefits of being named a City of Gastronomy extend well beyond tourism.',
                'Chengdu may have benefited from being selected by UNESCO, but tourism can likely be further increased by making more potential visitors aware of the city’s status as a City of Gastronomy.',
            ],
            'D',
            'Câu gạch chân ở Text 1 khẳng định chắc nịch rằng danh hiệu UNESCO hiển nhiên đã mang lại nhận diện và thúc đẩy du lịch Thành Đô. Text 2 phản hồi có chừng mực: để “hưởng lợi trọn vẹn” (“benefit fully”), thành phố vẫn phải có chiến lược tiếp thị hiệu quả; nếu không chủ động quảng bá, nhiều du khách hiện tại và tiềm năng thậm chí còn chẳng biết đến ẩm thực độc đáo nơi đây → Chọn D.',
            'Chú ý từ khóa định lượng nhẹ nhàng trong Text 2 (“benefit fully”, “may not even be aware”) → Text 2 không phủ nhận sạch trơn mà bổ sung điều kiện cần thiết để tăng du lịch hơn nữa.',
            [
                ('Out of Scope', 'Text 2 không hề nói danh hiệu này “đáng lẽ phải trao từ lâu” (“long overdue”).'),
                ('Out of Scope', 'Text 2 không bàn ai hay các đầu bếp xứng đáng nhận công lao lớn nhất.'),
                ('Out of Scope', 'Text 2 chỉ tập trung vào du lịch ẩm thực, không nói về các lợi ích ngoài du lịch.'),
                ('Đáp án đúng', 'Khớp sát lập luận của Park và cộng sự trong Text 2: có thể đã có lợi ích, nhưng cần quảng bá để thêm nhiều du khách tiềm năng biết đến thì du lịch mới tăng tối đa.'),
            ],
        ),
        _q(
            'may2025_rw_m1_q7', 7, 'Information and Ideas', 'Central Ideas and Details', 'Hard',
            '<p><i>The following text is adapted from Daniel Defoe’s 1704 nonfiction book</i> The Storm.</p><p style="padding-left:16px;">If I judge right, ’tis the duty of an historian to set everything in its own light, and to convey matter of fact upon its legitimate authority, and no other: I mean thus, (for I would be as explicit as I can) that where a story is vouched to him with sufficient authority, he ought to give the world the special testimonial of its proper voucher, or else he is not just to the story: and where it comes without such sufficient authority, he ought to say so; otherwise he is not just to himself.</p>',
            'Which choice best states the main idea of the text?',
            [
                'Historians are unlikely to be completely accurate, and so they will eventually want to revise the work they have produced.',
                'Historians should clearly indicate the extent to which each of their sources is trustworthy.',
                'The only figures that a historian should quote are those who are widely viewed as credible.',
                'Because historians cannot tell whose memories they should trust, they should avoid relying on eyewitness accounts of events.',
            ],
            'B',
            'Defoe chia làm 2 vế đối xứng về bổn phận của sử gia: (1) nếu câu chuyện có nguồn xác thực đủ tin cậy (“sufficient authority”) → phải nêu rõ người/nguồn bảo chứng; (2) nếu câu chuyện thiếu nguồn xác thực đủ tin cậy (“without such sufficient authority”) → phải nói rõ điều đó ra. Gom 2 vế: sử gia phải chỉ rõ mức độ đáng tin cậy của từng nguồn tin → Chọn B.',
            'Đừng sập bẫy C! Defoe KHÔNG cấm kể chuyện thiếu nguồn bảo chứng — ông yêu cầu sử gia phải “say so” (nói rõ mức độ đáng tin của nguồn).',
            [
                ('Out of Scope', 'Không đề cập đến việc sử gia phải chỉnh sửa (revise) tác phẩm về sau.'),
                ('Đáp án đúng', 'Bao quát trọn vẹn cả hai vế của Defoe: có bảo chứng thì nêu bảo chứng, thiếu bảo chứng thì nói rõ là thiếu bảo chứng.'),
                ('Too Extreme / Distortion', 'Trái với vế hai: Defoe cho phép ghi lại câu chuyện thiếu nguồn bảo chứng miễn là sử gia nói rõ điều đó.'),
                ('Out of Scope', 'Không nói sử gia không phân biệt được ký ức hay phải tránh nhân chứng (eyewitness accounts).'),
            ],
        ),
        _q(
            'may2025_rw_m1_q8', 8, 'Information and Ideas', 'Central Ideas and Details', 'Easy',
            '<p>In Nimipuutimt, an Indigenous language from the interior Northwest region of what is now the United States, <i>pit’íin’</i> means “girl,” whereas <i>pi-pít’in’</i> is used to refer to two or more girls. This phenomenon, in which an element of a root word is repeated, sometimes with modification, within another word that is related to the root word, is called reduplication. In this case, the element “pi” in <i>pit’íin’</i> gets repeated in <i>pi-pít’in’</i>. There are many examples of this type of reduplication in Nimipuutimt.</p>',
            'The text makes which point about Nimipuutimt?',
            [
                'It contains many instances of the type of reduplication seen in the words <i>pit’íin’</i> and <i>pi-pít’in’</i>.',
                'It has a wide variety of reduplicated words and phrases that mean “girl.”',
                'It is one of the only languages in the world that makes use of reduplication.',
                'It is closely related to another language from the interior Northwest region of what is now the United States that also makes use of reduplication.',
            ],
            'A',
            'Câu cuối cùng của đoạn khẳng định nguyên văn: “There are many examples of this type of reduplication in Nimipuutimt” (Có nhiều ví dụ về kiểu láy này trong tiếng Nimipuutimt) → Đáp án A diễn đạt lại chính xác 100%!',
            'Câu hỏi Specific Detail bám thẳng câu kết luận của đoạn văn; cẩn thận bẫy B đánh tráo “nhiều ví dụ kiểu láy” thành “nhiều từ mang nghĩa cô gái”.',
            [
                ('Đáp án đúng', 'Paraphrase trực tiếp câu cuối: tiếng Nimipuutimt có nhiều ví dụ về kiểu láy như ở cặp từ <i>pit’íin’</i> và <i>pi-pít’in’</i>.'),
                ('Fact Distortion', 'Đoạn chỉ nêu một cặp từ chỉ cô gái/các cô gái, không nói có nhiều từ láy khác nhau đều có nghĩa là “girl”.'),
                ('Too Extreme / Out of Scope', 'Không hề nói Nimipuutimt là một trong số ít ngôn ngữ duy nhất trên thế giới có hiện tượng láy.'),
                ('Out of Scope', 'Không đề cập đến mối quan hệ họ hàng với bất kỳ ngôn ngữ nào khác.'),
            ],
        ),
        _q(
            'may2025_rw_m1_q9', 9, 'Information and Ideas', 'Central Ideas and Details', 'Medium',
            '<p><i>The Federalist Papers</i> are a collection of 85 essays written by Alexander Hamilton, John Jay, and James Madison. Their publication (under a single pen name) was divided among the <i>Independent Journal</i> and other New York newspapers in 1787–88. The essays argue that New Yorkers should vote to ratify the proposed United States Constitution. Though the authorship of most of the individual essays is certain, that of a few is in question: for instance, while No. 15, “The Insufficiency of the Present Confederation to Preserve the Union,” was surely penned by Hamilton, No. 52, “The House of Representatives,” may have been written by either Hamilton or Madison.</p>',
            'Based on the text, what do the essays “The Insufficiency of the Present Confederation to Preserve the Union” and “The House of Representatives” have in common?',
            [
                'They were both published sometime during 1787 or 1788.',
                'They were both collaborative efforts between Alexander Hamilton and James Madison.',
                'They were both written by one of the three authors of the <i>Federalist Papers</i>, but which of the authors wrote either is not entirely clear.',
                'They were both published in the <i>Independent Journal</i>.',
            ],
            'A',
            'Cả hai bài tiểu luận số 15 và số 52 đều thuộc bộ 85 bài <i>Federalist Papers</i>, mà toàn bộ bộ tiểu luận này được xuất bản trên các tờ báo New York “in 1787–88” → Điểm chung chắc chắn là cả hai đều được xuất bản trong giai đoạn 1787–1788 → Chọn A.',
            'Loại trừ bằng kiểm chứng từng chi tiết nhỏ: “divided among A and other newspapers” ≠ cả hai đều đăng trên báo A (bẫy D)!',
            [
                ('Đáp án đúng', 'Cả hai đều thuộc bộ 85 bài <i>Federalist Papers</i> xuất bản vào năm 1787–1788.'),
                ('Fact Distortion', 'Bài số 15 chắc chắn do riêng Hamilton viết; bài số 52 có thể do Hamilton HOẶC Madison viết, không nói là đồng sáng tác.'),
                ('Contradiction', 'Quyền tác giả bài số 15 là hoàn toàn chắc chắn (“surely penned by Hamilton”), không hề mơ hồ.'),
                ('Overgeneralization', 'Bài nói 85 tiểu luận được CHIA RẢI trên tờ <i>Independent Journal</i> và các báo New York khác — không thể kết luận cả hai bài này đều đăng ở <i>Independent Journal</i>.'),
            ],
        ),
        _q(
            'may2025_rw_m1_q10', 10, 'Information and Ideas', 'Command of Evidence (Quantitative)', 'Easy',
            _svg_m1_q10_employment() + '<p>A student is using the graph for a class presentation on historic employment trends in the agriculture, hunting, and forestry sectors in two European countries. The student notes that from 1995 to 2007 _______</p>',
            'Which choice most effectively uses data from the graph to complete the example?',
            [
                'employment in these sectors remained stable in both Austria and the Czech Republic.',
                'the majority of employees in Austria were working in these sectors.',
                'the number of employees working in these sectors decreased in the Czech Republic while remaining relatively steady in Austria.',
                'the number of employees working in these sectors increased in the Czech Republic.',
            ],
            'C',
            'Đọc đồ thị giai đoạn 1995–2007: đường Cộng hòa Séc (nét liền, tam giác) giảm mạnh liên tục từ 231 nghìn (1995) xuống còn 129 nghìn (2007); đường Áo (nét đứt, ô vuông) gần như đi ngang ổn định quanh mức 18–20 nghìn (19 → 19 → 18 → 20 → 20 nghìn) → Chọn C.',
            'Luôn khoanh đúng khung năm đề hỏi (1995–2007) và chú ý trục tung là SỐ LƯỢNG tuyệt đối (thousands), không phải tỷ lệ phần trăm (“majority”).',
            [
                ('Misreads Data', 'Cộng hòa Séc giảm mạnh từ 231 nghìn xuống 129 nghìn, không hề ổn định.'),
                ('Unsupported Metric', 'Đồ thị chỉ cho số lượng lao động (nghìn người), không cho biết tổng lực lượng lao động của Áo để suy ra “đa số” (majority).'),
                ('Đáp án đúng', 'Mô tả chuẩn xác hai đường dữ liệu 1995–2007: Séc giảm đều (231k → 129k) còn Áo gần như giữ nguyên (18k–20k).'),
                ('Reversed Trend', 'Cộng hòa Séc giảm mạnh chứ không tăng trong giai đoạn 1995–2007.'),
            ],
        ),
        _q(
            'may2025_rw_m1_q11', 11, 'Information and Ideas', 'Command of Evidence (Quantitative)', 'Easy',
            _html_table(
                'Volcanoes in Ecuador',
                ['Name of volcano', 'Year of last eruption', 'Volcano type'],
                [
                    ['<b>Imbabura</b>', '5550 BCE', 'compound'],
                    ['<b>Pululahua</b>', '290 CE', 'caldera'],
                    ['<b>Sumaco</b>', '2016 CE', 'stratovolcano'],
                    ['<b>Santiago</b>', '1906 CE', 'shield'],
                ],
            ) + '<p>A student is researching volcanoes in Ecuador. The student claims that Ecuador is home to several different types of volcanoes.</p>',
            'Which choice best describes information from the table that supports the student’s claim?',
            [
                'Santiago, Sumaco, and Imbabura are all stratovolcanoes, whereas Pululahua is the only caldera volcano.',
                'Santiago is a shield volcano, Sumaco is a stratovolcano, Imbabura is a compound volcano, and Pululahua is a caldera volcano.',
                'Santiago and Sumaco are both shield volcanoes, whereas Imbabura and Pululahua are both compound volcanoes.',
                'Santiago, Sumaco, Imbabura, and Pululahua each most recently erupted in different years.',
            ],
            'B',
            'Luận điểm của học sinh: Ecuador có nhiều LOẠI núi lửa khác nhau (“several different types of volcanoes”). Tra cột 3 (“Volcano type”): Santiago = shield, Sumaco = stratovolcano, Imbabura = compound, Pululahua = caldera → cả 4 núi lửa đều thuộc 4 loại khác nhau → Chọn B.',
            'Cảnh giác bẫy D (“True Data, Wrong Claim”): dữ liệu năm phun trào đúng với bảng nhưng không chứng minh về “loại núi lửa” (volcano type)!',
            [
                ('False Data', 'Sai bảng dữ liệu: chỉ Sumaco là stratovolcano, còn Santiago là shield và Imbabura là compound.'),
                ('Đáp án đúng', 'Khớp 100% cột “Volcano type” của cả 4 núi lửa và chứng minh trực tiếp sự đa dạng loại núi lửa ở Ecuador.'),
                ('False Data', 'Sai bảng dữ liệu: Sumaco là stratovolcano (không phải shield) và Pululahua là caldera (không phải compound).'),
                ('True Data / Wrong Claim', 'Đúng số liệu cột năm phun trào nhưng không hỗ trợ luận điểm về các LOẠI núi lửa khác nhau.'),
            ],
        ),
        _q(
            'may2025_rw_m1_q12', 12, 'Information and Ideas', 'Command of Evidence (Textual)', 'Medium',
            '<p><i>Memoirs of Elleanor Eldridge</i> is an 1838 historical account by Elleanor Eldridge and Frances Harriet Whipple Green. In the book, the authors assert that all people naturally have an emotional attachment to where they live, writing, _______</p>',
            'Which quotation from <i>Memoirs of Elleanor Eldridge</i> most effectively illustrates the claim?',
            [
                '“Having thus so comfortably established ourselves, with no evil-minded eaves-dropper to make us afraid, bend now, dear reader, thy most earnest and delicately adjusted ear; for I am going to tell thee a secret.”',
                '“Home is home, to the lowly as well as the great; and no rank, or color, destroys its sacred character, its power over the mind, and the affections.”',
                '“Blessed are the slumbers of the innocent! They are kindlier than balm, and they refresh and gladden the spirit of childhood, like ministerings from a better world.”',
                '“To give some idea of the high esteem in which the subject of the following narrative is held, and the strong interest her misfortunes have excited, a few, from the great number of recommendations in her possession, are selected.”',
            ],
            'B',
            'Checklist 2 ý từ luận điểm: [1] MỌI NGƯỜI đều như vậy (“all people”) + [2] Sự gắn bó CẢM XÚC với NƠI Ở (“emotional attachment to where they live”). Câu B khớp hoàn hảo: “Home is home, to the lowly as well as the great; and no rank, or color” (= mọi người bất kể địa vị/màu da) + “its sacred character, its power over the mind, and the affections” (= sức mạnh gắn kết cảm xúc sâu sắc với mái nhà) → Chọn B.',
            'Tách luận điểm thành các cụm từ khóa bắt buộc (“all people” + “emotional attachment” + “where they live”) rồi đối chiếu trực diện từng trích dẫn.',
            [
                ('Off-Point', 'Chỉ là lời dẫn chuyện mời độc giả nghe một bí mật, không nói về tình cảm gắn bó với nhà cửa.'),
                ('Đáp án đúng', 'Khớp đủ cả hai yếu tố: tính phổ quát cho mọi người (“lowly as well as the great... no rank, or color”) và tình cảm gắn bó với mái ấm (“power over the mind, and the affections”).'),
                ('Off-Point', 'Nói về giấc ngủ yên lành của trẻ thơ ngây thơ, không liên quan tới nơi ở.'),
                ('Off-Point', 'Giới thiệu các thư tiến cử dành cho nhân vật chính, không đề cập tình cảm với nhà ở.'),
            ],
        ),
        _q(
            'may2025_rw_m1_q13', 13, 'Information and Ideas', 'Inferences', 'Hard',
            '<p>Chemists M.H. Gamble, P. Rice, and J.D. Selman studied the mass and heat transfer processes that occur when foods, such as the Indian snacks dahibara aludam and samosas, are oil fried. During frying, water in the crust evaporates, leaving voids that oil (a pure fat) can fill. As the process continues, water from the food’s center moves to the crust as long as the crust remains permeable. Therefore, it is likely that, all other things being equal, sections of a food that lose less moisture during the frying process _______</p>',
            'Which choice most logically completes the text?',
            [
                'will develop a thicker crust during the frying process than sections that lose more moisture.',
                'will have a lower fat content after frying is completed than sections that lose more moisture.',
                'will have a crust that loses its permeability less quickly during the frying process than sections that lose more moisture.',
                'will have a higher temperature after frying is completed than sections that lose more moisture.',
            ],
            'B',
            'Chuỗi nhân quả trực tiếp trong bài: Nước bay hơi (mất độ ẩm) → tạo ra các lỗ rỗng (“voids”) → dầu (một chất béo nguyên chất — “a pure fat”) lấp đầy các lỗ rỗng đó. Do đó, nếu các yếu tố khác như nhau, phần thức ăn MẤT ÍT ĐỘ ẨM HƠN → tạo ít lỗ rỗng hơn → ít dầu/chất béo thấm vào hơn → hàm lượng chất béo thấp hơn (“lower fat content”) → Chọn B.',
            'Mọi chi tiết trong ngoặc đơn của SAT — như “(a pure fat)” — đều là manh mối cố ý để bắc cầu sang đáp án (“lower fat content”)!',
            [
                ('Out of Scope', 'Bài không hề thiết lập mối quan hệ giữa lượng ẩm mất đi và độ dày lớp vỏ (thicker crust).'),
                ('Đáp án đúng', 'Suy luận chặt chẽ từ cơ chế thế chỗ: mất ít nước → ít lỗ rỗng → ít dầu (pure fat) điền vào → ít chất béo hơn.'),
                ('Reversed Logic', 'Nếu vỏ mất tính thấm chậm hơn (duy trì thấm lâu hơn), nước từ lõi sẽ thoát ra vỏ NHIỀU hơn chứ không phải mất ít ẩm hơn.'),
                ('Out of Scope', 'Không có dữ kiện nào liên hệ việc mất ít độ ẩm với nhiệt độ cao hơn sau khi chiên.'),
            ],
        ),
        _q(
            'may2025_rw_m1_q14', 14, 'Information and Ideas', 'Inferences', 'Hard',
            '<p>Ants and aphids are known to be mutualistic: ants feed on the honeydew produced by aphids, while aphids benefit from ants’ protection against predators. If aphid colonies—which generally require relatively stable surfaces, such as trees or other woody plants, to thrive—are too small to produce significant volumes of honeydew, however, ants will prey on aphids. Researcher Tae-Sung Kwon examined ant and aphid abundance in two habitats in South Korea, one on the mainland and one on Jeju Island. Though the habitats differed in some important respects, both were predominantly grassland, which could help explain why Kwon observed _______</p>',
            'Which choice most logically completes the text?',
            [
                'diminished ant and aphid abundance on the mainland compared to that on the island.',
                'a negative correlation between ant and aphid abundance on both the mainland and the island.',
                'different ant and aphid species on the mainland compared to those on the island.',
                'a positive correlation between aphid diversity and abundance on both the mainland and the island.',
            ],
            'B',
            'Nối chuỗi logic 3 mắt xích: (1) Đàn rệp cần bề mặt ổn định như cây thân gỗ mới phát triển lớn được; (2) Cả đất liền lẫn đảo Jeju đều chủ yếu là ĐỒNG CỎ (“predominantly grassland” — thiếu cây thân gỗ) → đàn rệp bị nhỏ, không tiết đủ dịch mật; (3) Khi đàn rệp quá nhỏ, kiến chuyển sang ĂN THỊT rệp (“ants will prey on aphids”) → càng nhiều kiến thì rệp càng ít đi → TƯƠNG QUAN NGHỊCH giữa mật độ kiến và rệp ở cả hai nơi → Chọn B!',
            'Nhận diện cụm điểm chung “both were predominantly grassland” → kết quả phải đúng cho CẢ HAI sinh cảnh, loại ngay các đáp án so sánh khác biệt giữa đất liền và đảo (A, C).',
            [
                ('Wrong Comparison', 'Tiền đề nhấn mạnh điểm GIỐNG NHAU (cả hai đều là đồng cỏ), không giải thích sự khác biệt mật độ giữa đất liền và đảo.'),
                ('Đáp án đúng', 'Đồng cỏ thiếu cây thân gỗ → đàn rệp nhỏ → kiến ăn thịt rệp → tương quan âm (nhiều kiến hơn thì ít rệp hơn) ở cả đất liền lẫn đảo Jeju.'),
                ('Wrong Comparison', 'Không có căn cứ giải thích sự khác biệt về thành phần loài giữa hai vùng.'),
                ('Out of Scope', 'Đoạn không hề đề cập đến độ đa dạng loài rệp (“aphid diversity”).'),
            ],
        ),
        _q(
            'may2025_rw_m1_q15', 15, 'Standard English Conventions', 'Boundaries', 'Easy',
            '<p>Museo del Autonomismo Puertorriqueño is a history museum in Ponce, Puerto Rico. It’s one of more than eighty museums in the US territory. Puerto Rico’s _______ showcase everything from the territory’s history to its architecture to its coffee.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['museums—', 'museums:', 'museums', 'museums,'],
            'C',
            'Cấu trúc câu cơ bản: Chủ ngữ “Puerto Rico’s museums” + Động từ chính “showcase”. Theo chuẩn Standard English, TUYỆT ĐỐI KHÔNG đặt dấu câu đơn lẻ (gạch ngang, hai chấm hay dấu phẩy) ngăn cách trực tiếp giữa chủ ngữ và động từ chính → Chọn C.',
            'Quy tắc thép Boundaries: Không bao giờ chèn dấu câu đơn giữa Subject (“Puerto Rico’s museums”) và Verb (“showcase”).',
            [
                ('Subject-Verb Split', 'Đặt gạch ngang đơn tách chủ ngữ khỏi động từ chính là sai ngữ pháp.'),
                ('Subject-Verb Split', 'Dấu hai chấm không thể đứng giữa chủ ngữ và động từ chính.'),
                ('Đáp án đúng', 'Không dùng dấu câu — nối liền mạch chủ ngữ số nhiều “Puerto Rico’s museums” với động từ “showcase”.'),
                ('Subject-Verb Split', 'Dấu phẩy đơn không được phép chia cắt chủ ngữ khỏi động từ.'),
            ],
        ),
        _q(
            'may2025_rw_m1_q16', 16, 'Standard English Conventions', 'Form, Structure, and Sense', 'Easy',
            '<p><i>Creek Council Tree</i> (1967) and <i>Cimarron Iron Bridge</i> (1972) are two oil landscape paintings by renowned Pawnee Nation artist Brummett Echohawk. In 2023, _______ displayed alongside other works by Echohawk at the student-curated exhibition <i>Brummett Echohawk: An Artist’s Journey</i> at the Oklahoma State University Museum of Art.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['this was', 'it was', 'some were', 'they were'],
            'D',
            'Tiền ngữ ở câu trước là HAI bức tranh sơn dầu cụ thể: <i>Creek Council Tree</i> và <i>Cimarron Iron Bridge</i> (danh từ số nhiều xác định) → đại từ thay thế phải là số nhiều “they” đi với động từ số nhiều “were” → Chọn D.',
            'Xác định đúng số ít/số nhiều và tính xác định của tiền ngữ: 2 bức tranh cụ thể → “they were” (không dùng “some” mơ hồ).',
            [
                ('Number Disagreement', '“this was” là số ít, không khớp với 2 bức tranh.'),
                ('Number Disagreement', '“it was” là số ít, không thể thay cho 2 bức tranh.'),
                ('Vague Pronoun', '“some” dùng cho một bộ phận không xác định trong tập lớn, không hợp để chỉ lại đúng 2 bức tranh vừa nêu tên.'),
                ('Đáp án đúng', '“they were” hòa hợp chuẩn xác về số nhiều và chỉ rõ cả 2 bức tranh đã nêu ở câu trước.'),
            ],
        ),
        _q(
            'may2025_rw_m1_q17', 17, 'Standard English Conventions', 'Boundaries', 'Easy',
            '<p>In the 1980s, Latino filmmakers Luis Valdez, Gregory Nava, and Ramón Menéndez helped expand on-screen representation of Latino Americans with the films <i>Zoot Suit</i> _______ and <i>Stand and Deliver</i> (1988), respectively.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            [
                '(1981)—<i>El Norte</i> (1983)—',
                '(1981) <i>El Norte</i> (1983)',
                '(1981), <i>El Norte</i> (1983),',
                '(1981) <i>El Norte</i> (1983),',
            ],
            'C',
            'Liệt kê song song 3 đạo diễn với 3 bộ phim tương ứng (“respectively”): [1] <i>Zoot Suit</i> (1981), [2] <i>El Norte</i> (1983), and [3] <i>Stand and Deliver</i> (1988). Cần đầy đủ dấu phẩy phân tách giữa mục 1 với mục 2 và giữa mục 2 với “and” + mục 3 → Chọn C.',
            'Chuỗi liệt kê 3 thành phần “X, Y, and Z”: nhớ đặt dấu phẩy sau cả mục 1 và mục 2!',
            [
                ('Nonessential Trap', 'Dùng cặp gạch ngang biến bộ phim thứ 2 thành phần phụ có thể bỏ đi — phá hỏng sự tương ứng 3-3 (“respectively”) với 3 đạo diễn.'),
                ('Missing Commas', 'Thiếu hoàn toàn dấu phẩy phân cách 3 tên phim.'),
                ('Đáp án đúng', 'Đặt đủ hai dấu phẩy chuẩn cho chuỗi liệt kê 3 phần tử: <i>Zoot Suit</i> (1981), <i>El Norte</i> (1983), and <i>Stand and Deliver</i> (1988).'),
                ('Missing Comma', 'Thiếu dấu phẩy giữa bộ phim thứ nhất (1981) và bộ phim thứ hai (<i>El Norte</i>).'),
            ],
        ),
        _q(
            'may2025_rw_m1_q18', 18, 'Standard English Conventions', 'Boundaries', 'Medium',
            '<p>Miguel Angel Asturias of Guatemala won it; Bob Dylan of the United States won it, too. These are just two examples of the wide range of writers to be granted what is arguably the most prestigious _______ the Nobel Prize in Literature.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            [
                'award for a person of letters:',
                'award; for a person of letters,',
                'award for a person of letters;',
                'award: for a person of letters',
            ],
            'A',
            'Trước chỗ nối là mệnh đề độc lập hoàn chỉnh kết thúc ở cụm “the most prestigious award for a person of letters”. Sau đó là cụm danh từ gọi tên cụ thể giải thưởng đó (“the Nobel Prize in Literature”) — KHÔNG phải mệnh đề độc lập → Dùng dấu hai chấm (:) sau “letters” để giới thiệu cụm danh từ giải thích → Chọn A.',
            'Công thức Colon: `[Mệnh đề độc lập hoàn chỉnh]: [Cụm danh từ giải thích/gọi tên]`. Không dùng chấm phẩy (;) khi vế sau không có động từ chính!',
            [
                ('Đáp án đúng', 'Hoàn thành trọn vẹn mệnh đề độc lập rồi dùng dấu hai chấm giới thiệu tên giải thưởng cụ thể (“the Nobel Prize in Literature”).'),
                ('Semicolon Error', 'Vế sau dấu chấm phẩy (“for a person of letters, the Nobel Prize in Literature”) là mảnh câu thiếu động từ chính.'),
                ('Semicolon Error', 'Sau dấu chấm phẩy phải là mệnh đề độc lập, nhưng “the Nobel Prize in Literature” chỉ là cụm danh từ.'),
                ('Misplaced Colon', 'Đặt dấu hai chấm trước “for a person of letters” tạo thành phần sau lủng củng vô nghĩa (“for a person of letters the Nobel Prize in Literature”).'),
            ],
        ),
        _q(
            'may2025_rw_m1_q19', 19, 'Standard English Conventions', 'Form, Structure, and Sense', 'Medium',
            '<p>The Grootbos florilegium in South Africa contains a collection of botanical paintings, with each painting depicting a local plant species in exquisite detail. The florilegium includes a vignette painting by contributing artist Sibonelo Chiliza. Unlike most paintings in the florilegium, _______</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            [
                'Chiliza’s vignette contextualizes a plant within an ecosystem.',
                'a plant’s ecosystem is contextualized in Chiliza’s vignette.',
                'the contextualization of a plant within an ecosystem occurs in Chiliza’s vignette.',
                'Chiliza contextualizes a plant within an ecosystem in his vignette.',
            ],
            'A',
            'Bẫy Dangling Modifier (Bổ ngữ lơ lửng) kinh điển! Cụm mở đầu “Unlike most paintings in the florilegium,” đang so sánh với BỨC TRANH → Chủ ngữ đứng ngay sau dấu phẩy BẮT BUỘC phải là một bức tranh! Chỉ A có chủ ngữ “Chiliza’s vignette” (bức họa vignette của Chiliza) so sánh đồng đẳng với “most paintings” → Chọn A.',
            'Hễ thấy cụm mở đầu “Unlike [X], _______” → chủ ngữ ngay sau dấu phẩy PHẢI cùng loại với [X] (paintings ↔ vignette)!',
            [
                ('Đáp án đúng', 'Chủ ngữ “Chiliza’s vignette” (một bức tranh) khớp trực tiếp với đối tượng so sánh “most paintings in the florilegium”.'),
                ('Dangling Modifier', 'Đặt “a plant’s ecosystem” ngay sau dấu phẩy khiến câu so sánh sai lệch giữa hệ sinh thái với các bức tranh.'),
                ('Dangling Modifier', 'So sánh “the contextualization” (sự đặt vào bối cảnh) với các bức tranh — sai logic bổ ngữ.'),
                ('Dangling Modifier', 'So sánh con người (“Chiliza”) với các bức tranh (“most paintings”) — bẫy cực phổ biến trên SAT.'),
            ],
        ),
        _q(
            'may2025_rw_m1_q20', 20, 'Standard English Conventions', 'Boundaries', 'Medium',
            '<p>On April 12, 1985, the space shuttle <i>Discovery</i> blasted off into space, commencing Mission _______ six days and twenty-three hours, the mission ended when the shuttle landed at Kennedy Space Center in Florida.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            [
                'STS-51-D, it lasted',
                'STS-51-D, lasting',
                'STS-51-D lasting',
                'STS-51-D. Lasting',
            ],
            'D',
            'Phân tích hai mệnh đề độc lập: IC1 = “On April 12, 1985, the space shuttle <i>Discovery</i> blasted off into space, commencing Mission STS-51-D.”; IC2 = “the mission ended when the shuttle landed at Kennedy Space Center in Florida.” Vì cả hai vế đều có chủ ngữ–động từ chính riêng, phải tách bằng dấu chấm câu! Cụm phân từ mở câu mới “Lasting six days and twenty-three hours,” bổ nghĩa chuẩn xác cho chủ ngữ “the mission” → Chọn D.',
            'Luôn tìm động từ chính của vế sau (“the mission ended”)! Nếu phía trước đã có một IC hoàn chỉnh (“Discovery blasted off...”) thì dùng dấu chấm tách câu để tránh Comma Splice.',
            [
                ('Comma Splice', 'Tạo liền hai lỗi nối câu bằng dấu phẩy giữa 3 mệnh đề độc lập (“Discovery blasted off”, “it lasted”, “the mission ended”).'),
                ('Comma Splice', 'Vẫn ghép hai mệnh đề độc lập (“Discovery blasted off...” và “the mission ended...”) chỉ bằng dấu phẩy.'),
                ('Comma Splice / Run-on', 'Không tách ranh giới hai mệnh đề độc lập, gây lỗi dính câu (comma splice).'),
                ('Đáp án đúng', 'Dấu chấm tách sạch hai mệnh đề độc lập; câu 2 mở bằng cụm phân từ “Lasting six days and twenty-three hours,” bổ nghĩa chuẩn cho “the mission”.'),
            ],
        ),
        _q(
            'may2025_rw_m1_q21', 21, 'Standard English Conventions', 'Boundaries', 'Medium',
            '<p>For scientists to produce new iron nanoparticles of a specific size or strength, they must first be able to monitor reactions between oxygen and existing iron nanoparticles at a near-atomic level of detail. Fortunately, chemistry _______ and his colleagues at Temple University recently developed a new approach that does just that.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            [
                'professor, Yugang Sun',
                'professor Yugang Sun',
                'professor, Yugang Sun,',
                'professor Yugang Sun,',
            ],
            'B',
            'Quy tắc Chức danh + Tên riêng (Title + Name): Khi không có mạo từ xác định đứng trước (“chemistry professor Yugang Sun”), tên riêng là thành phần THIẾT YẾU (essential) nên KHÔNG dùng dấu phẩy bao quanh; đồng thời chủ ngữ ghép “chemistry professor Yugang Sun and his colleagues” không được tách bằng dấu phẩy trước “and” → Chọn B.',
            'Thử xóa phần giữa 2 dấu phẩy: “Fortunately, chemistry professor and his colleagues...” → sai ngữ pháp vì thiếu mạo từ! Do đó tên riêng là thiết yếu → 0 dấu phẩy.',
            [
                ('Single Comma Split', 'Dấu phẩy đơn tách sai chức danh “chemistry professor” khỏi tên riêng thiết yếu “Yugang Sun”.'),
                ('Đáp án đúng', 'Không dùng dấu phẩy — giữ liền mạch cụm danh từ thiết yếu “chemistry professor Yugang Sun” trong chủ ngữ ghép với “and his colleagues”.'),
                ('False Nonessential', 'Đặt hai dấu phẩy biến “Yugang Sun” thành thông tin thừa; khi bỏ đi câu thành “chemistry professor and his colleagues” bị sai ngữ pháp.'),
                ('Compound Subject Split', 'Không đặt dấu phẩy trước “and” khi nối hai thành phần của một chủ ngữ ghép.'),
            ],
        ),
        _q(
            'may2025_rw_m1_q22', 22, 'Expression of Ideas', 'Transitions', 'Medium',
            '<p>In 1941, activists sought to persuade President Franklin Roosevelt to ban racial segregation in the military. _______ civil rights leader A. Philip Randolph planned a large anti-segregation march on Washington for July 1. Responding to the pressure, the president agreed to the ban, and the march was called off.</p>',
            'Which choice completes the text with the most logical transition?',
            ['To that end,', 'Apart from that,', 'In some cases,', 'By comparison,'],
            'A',
            'Quan hệ Mục tiêu → Hành động thực hiện mục tiêu: Câu 1 nêu mục tiêu của các nhà hoạt động (thuyết phục Tổng thống Roosevelt cấm phân biệt chủng tộc trong quân đội). Câu 2 nêu hành động cụ thể để đạt mục tiêu đó (lên kế hoạch tuần hành lớn ở Washington) → “To that end,” (= Nhằm mục đích đó) → Chọn A.',
            'Gặp mô hình `[Mục tiêu: sought to / aimed to] → [Hành động cụ thể để đạt mục tiêu]` → nhớ ngay từ nối vàng “To that end,”!',
            [
                ('Đáp án đúng', 'To that end = Nhằm mục đích đó — nối trực tiếp mục tiêu thuyết phục Tổng thống với hành động tổ chức cuộc tuần hành gây áp lực.'),
                ('Wrong Relationship', 'Apart from that = Ngoài điều đó ra — mang nghĩa tách sang ý khác thay vì phục vụ chính mục tiêu vừa nêu.'),
                ('Wrong Relationship', 'In some cases = Trong một số trường hợp — không khớp với một sự kiện lịch sử cụ thể.'),
                ('False Comparison', 'By comparison = So sánh với điều đó — không có hai đối tượng nào được đem ra so sánh.'),
            ],
        ),
        _q(
            'may2025_rw_m1_q23', 23, 'Expression of Ideas', 'Transitions', 'Medium',
            '<p>Analyses of Rembrandt’s seventeenth-century painting <i>The Night Watch</i>, citing its richly saturated colors and stark contrasts between light and shadow, often characterize the work as an exemplar of the Baroque-era style. Many art historians, however, challenge the very notion of a distinct Baroque era. They claim that the so-called Baroque aesthetic was, _______ just an extension of the stylings of the Renaissance era.</p>',
            'Which choice completes the text with the most logical transition?',
            ['nevertheless,', 'similarly,', 'first of all,', 'in reality,'],
            'D',
            'Câu 2 nói nhiều sử gia nghệ thuật bác bỏ khái niệm một thời kỳ Baroque riêng biệt. Câu 3 tiếp tục giải thích quan điểm phản biện đó: thứ “được gọi là” (“so-called”) mỹ học Baroque ấy, TRÊN THỰC TẾ (“in reality,”), chỉ là sự nối dài của phong cách Phục hưng → Chọn D.',
            'Cụm “so-called X” (cái gọi là X) báo hiệu đối lập giữa bề ngoài/tên gọi và bản chất thật → khớp hoàn hảo với “in reality,” / “in fact,”.',
            [
                ('False Contrast', 'nevertheless = tuy nhiên — câu 3 không tương phản với câu 2 mà giải thích sâu thêm quan điểm ở câu 2.'),
                ('False Similarity', 'similarly = tương tự — không nêu một trường hợp tương đồng mới.'),
                ('Wrong Sequence', 'first of all = trước hết — đoạn không liệt kê chuỗi luận điểm theo thứ tự.'),
                ('Đáp án đúng', 'in reality = trên thực tế — tương ứng sắc nét với cụm “so-called Baroque aesthetic” để khẳng định bản chất thật theo các sử gia này.'),
            ],
        ),
        _q(
            'may2025_rw_m1_q24', 24, 'Expression of Ideas', 'Transitions', 'Easy',
            '<p>Physicist Walter Massey led numerous scientific organizations over his long career. His most prominent appointment came in 1990, when Massey was named director of the National Science Foundation. _______ Massey had served as the first president of the National Society of Black Physicists.</p>',
            'Which choice completes the text with the most logical transition?',
            ['For example,', 'Previously,', 'In conclusion,', 'Thus,'],
            'B',
            'Nhìn thì động từ cực rõ: câu 2 dùng quá khứ đơn mốc năm 1990 (“came in 1990, when Massey was named...”), còn câu 3 lùi về thì QUÁ KHỨ HOÀN THÀNH (“had served”) để nhắc một chức vụ đảm nhiệm TRƯỚC năm 1990 → “Previously,” (Trước đó) → Chọn B.',
            'Thì quá khứ hoàn thành (“had + V3”) ngay sau một mốc năm quá khứ đơn là tín hiệu kinh điển cho từ nối thời gian lùi: “Previously,” / “Earlier,”.',
            [
                ('Wrong Relationship', 'Câu 3 không phải ví dụ minh họa cho chức giám đốc NSF năm 1990.'),
                ('Đáp án đúng', 'Previously = Trước đó — khớp hoàn toàn với thì quá khứ hoàn thành “had served” xảy ra trước sự kiện năm 1990.'),
                ('Wrong Relationship', 'In conclusion = Tóm lại — câu 3 bổ sung một sự kiện tiểu sử sớm hơn, không phải kết luận.'),
                ('False Cause', 'Thus = Do đó — việc giữ chức trước đó không thể là kết quả của việc bổ nhiệm năm 1990.'),
            ],
        ),
        _q(
            'may2025_rw_m1_q25', 25, 'Expression of Ideas', 'Rhetorical Synthesis', 'Easy',
            '<p>While researching a topic, a student has taken the following notes:</p><ul><li>Soap forms as the result of a chemical reaction between fats and either sodium or potassium hydroxide.</li><li>One end of a soap molecule is hydrophobic (water repelling), and one end is hydrophilic (water attracting).</li><li>The hydrophobic ends of soap molecules adhere to hydrophobic surface contaminants, such as dirt and oils.</li><li>The soap molecules form circular structures (micelles) around contaminants.</li><li>The hydrophilic ends of the molecules encase the micelles in water, lifting the micelles and contaminants off surfaces.</li></ul>',
            'The student wants to explain how soap removes a surface contaminant. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
            [
                'To remove dirt from a surface, soap molecules form a circular structure, or micelle, around the contaminant; next, the molecules encase the micelle in water, lifting it—and the dirt—off the surface.',
                'Surface contaminants like dirt and oils are hydrophobic, not hydrophilic—meaning they repel water rather than attract it.',
                'Micelles are circular structures created when soap molecules attach themselves to dirt or oils.',
                'Dirt, an example of a hydrophobic surface contaminant, can be removed from a surface by soap, which forms as the result of a chemical reaction between fats and either sodium or potassium hydroxide.',
            ],
            'A',
            'Mục tiêu (Goal): Giải thích CÁCH xà phòng loại bỏ chất bẩn trên bề mặt (“explain how soap removes a surface contaminant”). Chỉ đáp án A trình bày trọn vẹn quy trình cơ chế làm sạch: tạo micelle bao quanh chất bẩn → bọc micelle trong nước → nhấc cả micelle lẫn vết bẩn ra khỏi bề mặt → Chọn A.',
            'Đọc câu Goal trước tiên: từ khóa “how soap removes” đòi hỏi trình tự cơ chế tách bẩn khỏi bề mặt, không phải định nghĩa bẩn hay cách điều chế xà phòng.',
            [
                ('Đáp án đúng', 'Trình bày rõ ràng, đầy đủ từng bước cơ chế xà phòng bọc chất bẩn thành micelle rồi dùng nước nhấc khỏi bề mặt.'),
                ('Wrong Synthesis Goal', 'Chỉ định nghĩa tính kỵ nước của vết bẩn, không nói xà phòng loại bỏ chúng ra sao.'),
                ('Incomplete Process', 'Chỉ dừng ở bước hình thành micelle, bỏ sót bước quyết định là nhấc chất bẩn ra khỏi bề mặt.'),
                ('Wrong Synthesis Goal', 'Nói cách điều chế xà phòng (fats + hydroxide) thay vì cơ chế tẩy rửa vết bẩn.'),
            ],
        ),
        _q(
            'may2025_rw_m1_q26', 26, 'Expression of Ideas', 'Rhetorical Synthesis', 'Easy',
            '<p>While researching a topic, a student has taken the following notes:</p><ul><li>In music theory, the term “key” refers to the set of musical notes that forms the foundation of a piece of music.</li><li>In <i>Règles de Composition</i> (1682), French composer Marc-Antoine Charpentier describes the moods of various musical keys.</li><li>He describes the key of E major as “quarrelsome and boisterous.”</li><li>He describes the key of B minor as “solitary and melancholic.”</li><li>“Hero” (1993) by Mariah Carey is a song written in E major.</li><li>“Hotel California” (1976) by the Eagles is a song written in B minor.</li></ul>',
            'The student wants to compare Charpentier’s descriptions of E major and B minor. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
            [
                'The two songs possess a notable difference: “Hero” is written in the key of E major, while “Hotel California” is written in B minor.',
                'E major is the key in which “Hero” by Mariah Carey was written, and its mood has been described as “quarrelsome and boisterous.”',
                'While Charpentier describes E major as “quarrelsome and boisterous,” he describes B minor as “solitary and melancholic.”',
                'In <i>Règles de Composition</i>, Charpentier describes the mood of individual keys, including E major.',
            ],
            'C',
            'Mục tiêu (Goal): So sánh MÔ TẢ CỦA CHARPENTIER về giọng Mi trưởng (E major) và Si thứ (B minor). Chỉ đáp án C đối chiếu trực tiếp cả hai mô tả của Charpentier (“quarrelsome and boisterous” vs. “solitary and melancholic”) bằng cấu trúc “While...” → Chọn C.',
            'Khóa chặt 3 từ khóa của Goal: `compare` + `Charpentier’s descriptions` + `both E major and B minor`.',
            [
                ('Wrong Subject', 'So sánh hai ca khúc hiện đại thay vì so sánh mô tả của Charpentier về hai giọng nhạc.'),
                ('Single Subject Trap', 'Chỉ nhắc mô tả giọng E major, thiếu B minor và thiếu tên Charpentier.'),
                ('Đáp án đúng', 'Đối chiếu trực diện và súc tích đúng hai mô tả của Charpentier cho E major và B minor.'),
                ('Incomplete / Vague', 'Chỉ nhắc chung chung việc mô tả tâm trạng giọng nhạc và chỉ kể mỗi E major.'),
            ],
        ),
        _q(
            'may2025_rw_m1_q27', 27, 'Expression of Ideas', 'Rhetorical Synthesis', 'Easy',
            '<p>While researching a topic, a student has taken the following notes:</p><ul><li>Vasile Alecsandri National College in Galați, Romania, is home to a Foucault pendulum.</li><li>The pendulum consists of a weighted ball that swings at the end of a roughly 10-meter-long cable.</li><li>Like all Foucault pendulums, it dangles from a fixed point that ensures the swing path of the pendulum doesn’t change.</li><li>To an observer, the swing path of a Foucault pendulum appears to change over time because Earth rotates beneath it.</li><li>Foucault pendulums are used as a simple way to provide evidence of Earth’s rotation.</li></ul>',
            'The student wants to specify the parts of a Foucault pendulum. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
            [
                'With a swing path that appears to change over time, a Foucault pendulum provides evidence of Earth’s rotation.',
                'The Foucault pendulum at Vasile Alecsandri National College in Galați, Romania, includes a cable that is roughly 10 meters long.',
                'Dangling from a fixed point, the Foucault pendulum at Vasile Alecsandri National College consists of a cable with a weighted ball at the end.',
                'The swing path of the Foucault pendulum at Vasile Alecsandri National College appears to change over time.',
            ],
            'C',
            'Mục tiêu (Goal): Chỉ rõ CÁC BỘ PHẬN CẤU TẠO (“specify the parts”) của con lắc Foucault. Theo ghi chú, con lắc gồm quả cầu nặng gắn ở đầu sợi dây cáp (treo từ một điểm cố định). Đáp án B chỉ nhắc mỗi sợi dây cáp (thiếu quả cầu nặng); chỉ đáp án C nêu đầy đủ các bộ phận cấu tạo → Chọn C.',
            'Chú ý số nhiều “the parts” trong Goal: đáp án phải liệt kê đầy đủ cấu tạo (dây cáp + quả cầu nặng + điểm treo cố định), tránh bẫy B chỉ nhắc 1 bộ phận.',
            [
                ('Wrong Synthesis Goal', 'Chỉ nói về quỹ đạo dao động và công dụng chứng minh Trái Đất tự quay, không nêu bộ phận cấu tạo.'),
                ('Incomplete Parts', 'Chỉ nêu sợi dây cáp 10 mét mà bỏ quên quả cầu nặng (“weighted ball”).'),
                ('Đáp án đúng', 'Chỉ rõ đầy đủ các bộ phận cấu tạo: điểm treo cố định, sợi dây cáp và quả cầu nặng ở đầu dây.'),
                ('Wrong Synthesis Goal', 'Chỉ mô tả hiện tượng quỹ đạo dao động trông như thay đổi theo thời gian.'),
            ],
        ),
    ]


# ============================================================================
# MODULE 2 HARD ROUTE (27 Qs — Source: mod3_rw.txt)
# ============================================================================

def get_m2_hard_questions():
    return [
        _q(
            'may2025_rw_m2h_q1', 1, 'Craft and Structure', 'Words in Context', 'Medium',
            '<p>Postcranial skeletal pneumaticity (PSP) refers to the presence of extensions of an animal’s lungs and air sacs inside its bones. Though such structures do not typically fossilize, they are believed to have been present in <i>Ornithomimus</i>, <i>Phuwiangosaurus</i>, and other Cretaceous theropods and sauropods. To _______ PSP from fossils, researchers look for indicators such as large foramina (holes in bones).</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            ['isolate', 'infer', 'acquire', 'preserve'],
            'B',
            'Vì các cấu trúc mô mềm (phổi và túi khí) thường không hóa thạch (“do not typically fossilize”), các nhà nghiên cứu không thể trực tiếp nhìn thấy hay tách chúng ra mà phải dựa vào dấu hiệu gián tiếp (“look for indicators such as large foramina”) để SUY LUẬN (“infer”) sự tồn tại của PSP từ hóa thạch → Chọn B.',
            'Cụm “do not typically fossilize” + “look for indicators” là dấu hiệu trực diện cho động từ suy đoán gián tiếp “infer”.',
            [
                ('Wrong Meaning', 'isolate = tách biệt/cô lập về mặt vật lý — không thể cô lập mô phổi/túi khí vốn đã không hóa thạch.'),
                ('Đáp án đúng', 'infer = suy ra, suy luận gián tiếp từ các dấu hiệu chỉ báo (foramina trên xương hóa thạch).'),
                ('Wrong Meaning', 'acquire = thu nhận, mua/đạt được — không dùng cho việc xác định đặc điểm sinh học cổ đại từ dấu tích.'),
                ('Wrong Meaning', 'preserve = bảo tồn — không thể bảo tồn cấu trúc không hóa thạch bằng cách tìm lỗ trên xương.'),
            ],
        ),
        _q(
            'may2025_rw_m2h_q2', 2, 'Craft and Structure', 'Words in Context', 'Hard',
            '<p>In 2018, Costa Rica, which has strong democratic institutions, experienced an inflation rate of 2.22%, much higher than the 0.25% rate seen in Qatar, which has relatively weak democratic institutions. Such a result is _______, however: Raj Desai et al. have shown that democratic institution strength tends to restrain inflationary pressures.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            ['anomalous', 'inexplicable', 'facetious', 'unfounded'],
            'A',
            'Quy luật chung mà Raj Desai và cộng sự chứng minh: thể chế dân chủ mạnh thường KIỀM CHẾ lạm phát (“tends to restrain inflationary pressures”). Trường hợp năm 2018 (Costa Rica dân chủ mạnh nhưng lạm phát cao hơn Qatar dân chủ yếu) đi ngược xu hướng chung đó (“however”) → kết quả đó mang tính BẤT THƯỜNG / NGOẠI LỆ (“anomalous”) → Chọn A.',
            'Phân biệt sắc thái học thuật: “anomalous” = lệch khỏi quy luật chung (“tends to”), khác với “inexplicable” (bất khả giải thích — quá cực đoan) và “unfounded” (vô căn cứ).',
            [
                ('Đáp án đúng', 'anomalous = bất thường, ngoại lệ so với quy luật chung — khớp hoàn hảo với xu hướng “tends to restrain” ở vế sau dấu hai chấm.'),
                ('Too Extreme', 'inexplicable = không thể nào giải thích nổi — đoạn văn chỉ nói nó đi ngược xu hướng chung chứ không nói không thể giải thích.'),
                ('Wrong Tone', 'facetious = bông đùa thiếu nghiêm túc — hoàn toàn sai ngữ cảnh kinh tế học.'),
                ('Wrong Meaning', 'unfounded = không có cơ sở/vô căn cứ — số liệu lạm phát 2,22% và 0,25% là dữ liệu thực tế chứ không phải khẳng định vô căn cứ.'),
            ],
        ),
        _q(
            'may2025_rw_m2h_q3', 3, 'Craft and Structure', 'Words in Context', 'Hard',
            '<p>Some robots such as KHR-1 (developed in 2004) and Epi (developed in 2015) are designed to resemble humans so that people will find it easier to interact with them. To that end, certain features such as the ability to respond to voice commands can help to _______ the effect of the more unnatural aspects of a robot’s appearance, but a robot that looks too human can fall into the “uncanny valley,” meaning that its appearance unintentionally unsettles those who encounter it.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            ['ameliorate', 'substantiate', 'augment', 'coalesce'],
            'A',
            'Mục tiêu thiết kế (“To that end”): giúp con người dễ tương tác hơn với robot. “The effect of the more unnatural aspects of a robot’s appearance” là tác động tiêu cực/khó chịu. Do đó, tính năng phản hồi giọng nói giúp LÀM GIẢM NHẸ / CẢI THIỆN (“ameliorate”) tác động tiêu cực ấy → Chọn A.',
            'Từ khóa “ameliorate” (làm dịu bớt, cải thiện một tình trạng bất lợi/tiêu cực) là từ vựng Module 2 Hard kinh điển trên Digital SAT.',
            [
                ('Đáp án đúng', 'ameliorate = làm dịu bớt, giảm nhẹ tác động tiêu cực của những nét ngoại hình kém tự nhiên.'),
                ('Wrong Meaning', 'substantiate = chứng minh bằng bằng chứng — sai hoàn toàn về nghĩa.'),
                ('Opposite Direction', 'augment = làm tăng thêm — đi ngược mục tiêu làm con người dễ tương tác hơn.'),
                ('Wrong Meaning', 'coalesce = hợp nhất, kết tụ lại thành một khối — không hợp nghĩa.'),
            ],
        ),
        _q(
            'may2025_rw_m2h_q4', 4, 'Craft and Structure', 'Words in Context', 'Hard',
            '<p>Demosthenes, a prominent fourth-century BCE Athenian orator, is said to have been _______ of <i>parrhesia</i>, or speaking freely and openly to ensure productive civic deliberation. He is noted for characterizing <i>parrhesia</i> in several public addresses as the foundation of democracy in classical Athens rather than, more simply, as a facilitator of the political system.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            ['a harbinger', 'a steward', 'an apprentice', 'a proponent'],
            'D',
            'Câu 2 làm rõ thái độ của Demosthenes: ông nhiều lần ca ngợi <i>parrhesia</i> (nói năng tự do cởi mở) trong các bài diễn văn công khai như “nền tảng của nền dân chủ Athens cổ đại” → Ông là NGƯỜI ỦNG HỘ / NGƯỜI ĐỀ XƯỚNG mạnh mẽ (“a proponent”) của nguyên tắc đó → Chọn D.',
            'Khi nhân vật công khai đề cao một tư tưởng/thực hành trong các bài diễn văn → chọn danh từ chỉ người ủng hộ (“proponent / advocate”).',
            [
                ('Wrong Meaning', 'a harbinger = điềm báo/người báo trước sự xuất hiện sắp tới — không khớp với việc công khai đề cao một giá trị đang tồn tại.'),
                ('Collocation / Shade Trap', 'a steward = người quản lý/trông nom tài sản hay tài nguyên được giao phó, không chuẩn bằng “proponent” cho người cổ vũ một tư tưởng trong diễn văn.'),
                ('Wrong Meaning', 'an apprentice = người học việc — trái với mô tả “prominent Athenian orator”.'),
                ('Đáp án đúng', 'a proponent = người ủng hộ, cổ vũ nhiệt thành — khớp tuyệt đối với việc Demosthenes nhiều lần tôn vinh <i>parrhesia</i> là nền tảng dân chủ.'),
            ],
        ),
        _q(
            'may2025_rw_m2h_q5', 5, 'Craft and Structure', 'Text Structure and Purpose', 'Medium',
            '<p>Hezekiah Baker’s <i>Wind Surf</i>, a beach scene whose pastel blue skies and sands are sharply contrasted with dark silhouetted palm trees and deep blue water, is typical of paintings by the Florida Highwaymen, loosely affiliated landscape artists mainly active in Fort Pierce, Florida, during the 1950s and ’60s. Some art historians suggest that Highwaymen paintings played a role in shaping popular perceptions of the state that persist today: the natural iconography that Baker and colleagues constantly revisited—majestic ocean scenes, windswept palm trees—is now seen as classically Floridian.</p>',
            'Which choice best states the main purpose of the text?',
            [
                'To contrast the public’s reaction during the 1950s and ’60s to a particular painting by Hezekiah Baker with more recent reactions to it',
                'To describe the historical circumstances in which paintings by the Florida Highwaymen experienced a resurgence in popularity',
                'To explain that a particular painting by Hezekiah Baker has had greater influence on the broader culture of the state of Florida than is generally acknowledged',
                'To present the argument that paintings by the Florida Highwaymen likely helped to create a particular widespread impression of Florida',
            ],
            'D',
            'Câu 1 lấy <i>Wind Surf</i> làm ví dụ điển hình để giới thiệu nhóm họa sĩ Florida Highwaymen. Câu 2 (trọng tâm toàn đoạn) nêu lập luận của các sử gia nghệ thuật: tranh của nhóm Highwaymen đã góp phần định hình ấn tượng phổ biến kéo dài đến tận hôm nay về Florida (cảnh đại dương hùng vĩ, hàng cọ trong gió là hình ảnh “đậm chất Florida kinh điển”) → Chọn D.',
            'Đừng bị cuốn vào ví dụ mở đoạn (tranh <i>Wind Surf</i>); mục đích chính nằm ở luận điểm khái quát của cả nhóm họa sĩ ở câu 2!',
            [
                ('Out of Scope', 'Không hề so sánh phản ứng công chúng thập niên 1950–60 với phản ứng hiện nay đối với riêng bức <i>Wind Surf</i>.'),
                ('Out of Scope', 'Không nói về hoàn cảnh lịch sử của một đợt “hồi sinh mức độ nổi tiếng” (resurgence).'),
                ('Scope / Distortion', 'Thu hẹp sai vào một bức tranh duy nhất và tự thêm ý “hơn mức thường được công nhận”.'),
                ('Đáp án đúng', 'Tóm gọn chuẩn xác trọng tâm câu 2: trình bày lập luận rằng tranh của nhóm Florida Highwaymen góp phần tạo nên hình dung phổ biến về bang Florida.'),
            ],
        ),
        _q(
            'may2025_rw_m2h_q6', 6, 'Craft and Structure', 'Text Structure and Purpose', 'Hard',
            '<p><i>Chorioactis geaster</i>, a species of mushroom that makes a distinctive hissing sound when it releases its spores, is an elusive fungus that has been observed only in Texas and Oklahoma in the US and in the Miyazaki and Nara Prefectures in Japan. Scientists aren’t entirely sure why <i>C. geaster</i> is distributed in this way (genetic analysis reveals that the US and Japanese strains diverged 19 million years ago), but the mushroom appears to be very selective: <u>it is typically found on the decaying stumps and roots of only a few tree species that are abundant in these areas.</u></p>',
            'Which choice best describes the function of the underlined portion in the text as a whole?',
            [
                'It highlights the negative impact <i>C. geaster</i> has on the trees on which it’s found.',
                'It elaborates on a characterization of <i>C. geaster</i> presented earlier in the text.',
                'It provides an explanation for the relationship between <i>C. geaster</i> and its habitats.',
                'It emphasizes the uncertainty about <i>C. geaster</i> alluded to earlier in the text.',
            ],
            'B',
            'Nhìn ngay trước dấu hai chấm: “the mushroom appears to be **very selective**: [phần gạch chân]”. Phần gạch chân đứng sau dấu hai chấm nhằm TRIỂN KHAI / LÀM RÕ THÊM đặc điểm mô tả (“characterization”) rằng loài nấm này rất kén chọn môi trường sống (chỉ mọc trên gốc và rễ mục của vài loài cây nhất định) → Chọn B.',
            'Dấu hai chấm ngay trước phần gạch chân luôn là tín hiệu vàng của chức năng “elaborates on / specifies” (làm rõ chi tiết cho nhận định đứng ngay trước nó)! Cẩn thận bẫy C: phần gạch chân chỉ MÔ TẢ nó mọc ở đâu chứ không GIẢI THÍCH VÌ SAO nó có mối quan hệ đó.',
            [
                ('Fact Distortion', 'Nấm mọc trên gốc và rễ ĐÃ MỤC (“decaying stumps and roots”), không hề nói nấm gây hại cho cây.'),
                ('Đáp án đúng', 'Triển khai cụ thể nhận định mô tả <i>C. geaster</i> ngay trước dấu hai chấm (“appears to be very selective”).'),
                ('Explanation Trap', 'Chỉ mô tả cụ thể tính kén chọn (mọc trên vài loài cây nhất định), KHÔNG giải thích nguyên nhân/cơ chế vì sao loài nấm có mối quan hệ với sinh cảnh đó.'),
                ('Opposite Focus', 'Phần gạch chân nêu đặc điểm quan sát được (“very selective”), không nhằm nhấn mạnh sự bất định của giới khoa học.'),
            ],
        ),
        _q(
            'may2025_rw_m2h_q7', 7, 'Craft and Structure', 'Text Structure and Purpose', 'Hard',
            '<p>In South Africa, use of solid fuel (e.g., coal, wood) as a share of total household fuel use fell by more than half between 2000 and 2019; such shifts are often explained by appeal to the energy ladder, a model holding that fuel choice is mediated mainly by household income (specifically, high-technology fuels displace solid fuels as incomes rise). Rasmus Heltberg’s study of fuel use in Vietnam shows this model to be reductive, however: household fuel use was heterogeneous, flexible, and influenced by several factors, including local electrical and plumbing infrastructure.</p>',
            'Which choice best describes the main purpose of the text?',
            [
                'To contrast patterns in household fuel use in two countries',
                'To critique a frequently used model of changes in household fuel prices',
                'To account for the effect of fuel use on household income',
                'To challenge a common explanation for households’ fuel choices',
            ],
            'D',
            'Mạch văn chuẩn “Cách giải thích phổ biến → Tuy nhiên nghiên cứu mới phản bác”: Câu 1 giới thiệu mô hình phổ biến “energy ladder” (giải thích lựa chọn nhiên liệu hộ gia đình chủ yếu theo thu nhập). Câu 2 dùng nghiên cứu của Heltberg tại Việt Nam (“shows this model to be reductive, however”) để PHẢN BIỆN cách giải thích phổ biến ấy → Chọn D.',
            'Soi cực kỹ từng từ cuối của đáp án nhiễu! Bẫy B cố tình thay “fuel choices” thành “fuel prices” — sai một chữ là loại ngay!',
            [
                ('Secondary Detail Trap', 'Nam Phi chỉ là ví dụ mở đầu cho sự dịch chuyển thường được giải thích bằng mô hình “energy ladder”; trọng tâm toàn đoạn là phê phán mô hình lý thuyết đó, không phải đối chiếu Nam Phi với Việt Nam.'),
                ('Single-Word Swap Trap', 'Sai từ khóa “fuel prices” (giá nhiên liệu)! Mô hình “energy ladder” nói về sự LỰA CHỌN nhiên liệu (“fuel choice”), không phải biến động giá nhiên liệu.'),
                ('Reversed Causality', 'Đảo ngược nhân quả: mô hình xem xét tác động của thu nhập lên lựa chọn nhiên liệu, không phải tác động của nhiên liệu lên thu nhập.'),
                ('Đáp án đúng', 'Khớp hoàn toàn cấu trúc toàn đoạn: thách thức một lý thuyết giải thích phổ biến (“energy ladder”) về lựa chọn nhiên liệu của các hộ gia đình.'),
            ],
        ),
        _q(
            'may2025_rw_m2h_q8', 8, 'Information and Ideas', 'Central Ideas and Details', 'Hard',
            '<p><i>The following text is adapted from Fanny Burney’s 1778 novel</i> Evelina. <i>The text is an excerpt from a letter by Lady Howard to Evelina’s guardian, Reverend Villars, in which Lady Howard discusses an upcoming trip to London planned by her daughter Mrs. Mirvan’s family.</i></p><p style="padding-left:16px;">It is very earnestly [the Mirvans’] wish to enlarge and enliven their party by the addition of your amiable ward, who would share, equally with her own daughter, the care and attention of Mrs. Mirvan. Do not start at this proposal; it is time that [Evelina] should see something of the world. When young people are too rigidly sequestered from it, their lively and romantic imaginations paint it to them as a paradise of which they have been beguiled; but when they are shown it properly, and in due time, they see it such as it really is, equally shared by pain and pleasure, hope and disappointment.</p>',
            'Based on the text, Lady Howard would most likely agree with which statement about Reverend Villars?',
            [
                'Although his desire to guard Evelina from unscrupulous people is commendable, his general mistrust has led him to be unduly wary of the Mirvans.',
                'Although the manner in which he has raised Evelina is in many ways exemplary, he has been misguided in shielding her from the influence of other young people.',
                'He is overly protective of Evelina, who would likely benefit from a greater variety of experiences than she has had thus far.',
                'He has imparted to Evelina his own idealistic view of the world, which results in her being unprepared to face inevitable disappointments.',
            ],
            'C',
            'Lady Howard đoán trước Villars sẽ giật mình phản đối (“Do not start at this proposal”), khuyên đã đến lúc Evelina nên bước ra ngắm nhìn thế giới (“it is time that [Evelina] should see something of the world”), và cảnh báo khi người trẻ bị tách biệt quá nghiêm ngặt (“too rigidly sequestered”), họ sẽ mộng tưởng sai lệch; trái lại, được trải nghiệm đúng lúc sẽ giúp nhìn rõ thực tế cuộc đời → Bà cho rằng Villars đang bảo bọc Evelina quá mức và cô sẽ có lợi khi có thêm trải nghiệm đa dạng hơn → Chọn C.',
            'Đọc văn cổ thế kỷ 18 theo cấu trúc lập luận: “too rigidly sequestered” = overly protective; “shown it properly... see it such as it really is” = benefit from broader experience.',
            [
                ('Unsupported Inference', 'Bức thư không nhắc đến “kẻ vô lương tâm” (unscrupulous people) hay việc Villars nghi ngờ riêng gia đình Mirvan.'),
                ('Fact Distortion', 'Lady Howard nói về việc tách khỏi “the world” (thế giới bên ngoài) chứ không nói riêng “ảnh hưởng của các bạn trẻ khác”, cũng không khen cách nuôi dạy là “exemplary”.'),
                ('Đáp án đúng', 'Khớp sát cả hai vế lập luận của Lady Howard: Villars giữ Evelina quá chặt (“too rigidly sequestered”) và cô sẽ hưởng lợi khi được mở mang trải nghiệm đúng lúc.'),
                ('Wrong Cause', 'Trái với văn bản: chính trí tưởng tượng lãng mạn của người trẻ khi bị nhốt kín mới tô hồng thế giới thành thiên đường, KHÔNG phải Villars truyền cho cô thế giới quan lý tưởng hóa.'),
            ],
        ),
        _q(
            'may2025_rw_m2h_q9', 9, 'Information and Ideas', 'Command of Evidence (Textual)', 'Medium',
            '<p>Many music streaming services also function as social media platforms: by giving users the option to follow friends and share curated playlists or information about their listening history, these platforms allow people to convey their music preferences and listening activities directly to their social networks. In a 2023 study, researcher Michael James Walsh interviewed frequent users of a popular music streaming platform to investigate how its social media dimensions shape their listening habits. Walsh found that these dimensions tended to make study participants feel more mindful of how their listening activities may be perceived, which in turn influenced how they managed those activities.</p>',
            'Which quotation from a music streaming platform user would best illustrate Walsh’s finding?',
            [
                '“Because the predictions the platform makes about what new songs I might like depend on my past listening habits, at times its recommendations can feel overly repetitive and unvarying.”',
                '“Listening to music through a streaming platform feels a lot more passive, since I don’t need to make any deliberate choices about what music I’m going to consume, like I do when buying digital downloads or records and CDs.”',
                '“The social aspects of music streaming make it really easy to create a sense of a shared listening experience with my friends, even if we aren’t in the same room.”',
                '“When I create playlists or choose songs to listen to, I often pick songs that I think the friends who are following me might be interested in listening to, rather than what I might actually prefer listening to in that moment.”',
            ],
            'D',
            'Khóa 2 thành phần trong kết quả của Walsh: [1] ý thức rõ việc nghe nhạc của mình bị người khác nhìn nhận ra sao (“more mindful of how their listening activities may be perceived”) → [2] điều chỉnh cách quản lý/lựa chọn hoạt động nghe nhạc (“influenced how they managed those activities”). Chỉ D thể hiện rõ cả hai: khi tạo playlist hay chọn bài, người dùng cố tình chọn bài bạn bè theo dõi thích thay vì gu thực sự lúc đó của mình → Chọn D.',
            'Cảnh giác bẫy C (“Topic Keyword Lure”): có từ “social aspects” và “friends”, nhưng không hề thể hiện việc để ý ánh nhìn người khác rồi điều chỉnh cách chọn nhạc!',
            [
                ('Off-Point', 'Nói về thuật toán gợi ý bài hát lặp lại, không liên quan đến yếu tố mạng xã hội hay nhận thức của người khác.'),
                ('Off-Point', 'So sánh tính thụ động của streaming với việc mua đĩa CD/nhạc số, không nhắc yếu tố xã hội.'),
                ('Topic Keyword Lure', 'Nhắc yếu tố xã hội (“shared listening experience”), nhưng không minh họa việc tự ý thức cách người khác nhìn nhận để điều chỉnh thói quen chọn bài.'),
                ('Đáp án đúng', 'Minh họa trọn vẹn kết quả nghiên cứu của Walsh: để tâm đến cảm nhận của người theo dõi và thay đổi cách chọn bài/tạo playlist theo đó.'),
            ],
        ),
        _q(
            'may2025_rw_m2h_q10', 10, 'Information and Ideas', 'Command of Evidence (Quantitative)', 'Easy',
            _html_table(
                'Examples of Hoards found in Ireland and Northern Ireland',
                ['Hoard name', 'Date of contents', 'Year of discovery', 'Description'],
                [
                    ['<b>Coleraine Hoard</b>', '5th century CE', '1854', 'silver pieces'],
                    ['<b>Derrynaflan Hoard</b>', '10th century CE', '1980', 'silver and bronze pieces'],
                    ['<b>Dooyork Hoard</b>', '3rd century BCE–2nd century CE', '2001', 'gold, bronze, and beads'],
                ],
            ) + '<p>Deposits of valuable objects, called hoards, have been unearthed in many different parts of Ireland and Northern Ireland. Technological advancements in the twenty-first century have made it easier to locate hoards, but plenty of hoards were found earlier. For example, _______</p>',
            'Which choice most effectively uses data from the table to complete the statement?',
            [
                'the Coleraine Hoard and Derrynaflan Hoard were both found before 2000.',
                'Derrynaflan Hoard and Dooyork Hoard were both discovered in the 1900s.',
                'the Derrynaflan Hoard was found in 1854.',
                'the Coleraine Hoard, Derrynaflan Hoard, and Dooyork Hoard have all been found since 1854.',
            ],
            'A',
            'Luận điểm cần minh họa ngay trước chỗ trống: công nghệ thế kỷ 21 (từ năm 2001 trở đi) giúp tìm kho báu dễ hơn, “nhưng rất nhiều kho báu đã được tìm thấy TỪ TRƯỚC ĐÓ” (“plenty of hoards were found earlier”). Tra cột “Year of discovery”: Coleraine Hoard (1854) và Derrynaflan Hoard (1980) đều được tìm thấy TRƯỚC năm 2000 → Chọn A.',
            'Đối chiếu cẩn thận cột “Year of discovery” (năm phát hiện) với mốc “twenty-first century” — tránh nhầm với cột “Date of contents” và tránh đáp án D gộp cả năm 2001!',
            [
                ('Đáp án đúng', 'Đúng tuyệt đối bảng dữ liệu (1854 và 1980 đều trước năm 2000) và minh họa trực tiếp việc nhiều kho báu được tìm thấy trước thế kỷ 21.'),
                ('False Data', 'Sai dữ liệu: Dooyork Hoard được phát hiện năm 2001 (thế kỷ 21), không phải thập niên/thế kỷ 1900s.'),
                ('False Data', 'Sai hàng bảng: kho báu tìm thấy năm 1854 là Coleraine Hoard; Derrynaflan Hoard tìm thấy năm 1980.'),
                ('True Data / Wrong Claim', 'Gộp cả Dooyork Hoard (2001) và chỉ nói “từ năm 1854 trở đi” không minh họa được ý “tìm thấy trước thế kỷ 21”.'),
            ],
        ),
        _q(
            'may2025_rw_m2h_q11', 11, 'Information and Ideas', 'Command of Evidence (Textual)', 'Medium',
            '<p>A student is writing a research paper on the history of irrigation in the southwestern United States, situating the development of Mittry Lake (a man-made body of water created in Imperial County, California, in 1909) in a larger historical context. The student claims that some modern-day irrigation methods used in southwestern states, such as California, Arizona, and New Mexico, have a lineage that long predates the completion of Mittry Lake.</p>',
            'Which quotation from a historian best supports the student’s claim?',
            [
                '“In the decades following the Second World War, irrigation of arid areas for agriculture increased to such a degree that it now accounts for roughly 70% of the world’s water usage.”',
                '“The importance of the development of irrigation infrastructure in the American Southwest today cannot be overstated, since it is the most common means of conveying water for food production.”',
                '“The irrigation system developed by the Hohokam people in what is now central Arizona in the 7th century CE was simple but made use of hydraulic engineering design principles that are still utilized by today’s engineers.”',
                '“Sprinkler irrigation systems, which were developed in the late 20th century, are a convenient technique of irrigating that makes use of machinery in order to spray water in all directions. Many areas of the Southwestern United States are currently irrigated by this method.”',
            ],
            'C',
            'Checklist 3 yếu tố từ luận điểm: [1] Phương pháp tưới tiêu HIỆN ĐẠI (“modern-day”), [2] ở các bang TÂY NAM MỸ (California/Arizona/New Mexico), [3] có nguồn gốc LÂU ĐỜI TRƯỚC NĂM 1909 (“long predates the completion of Mittry Lake”). Câu C khớp cả 3: hệ thống của người Hohokam ở miền trung Arizona vào thế kỷ 7 CN (xa xưa hơn 1909 rất nhiều) sử dụng nguyên lý kỹ thuật thủy lực mà kỹ sư ngày nay VẪN còn áp dụng → Chọn C.',
            'Kiểm tra trục thời gian! Mittry Lake hoàn thành năm 1909 → loại ngay A (sau Thế chiến II), B (chỉ nói hiện tại), D (cuối thế kỷ 20).',
            [
                ('Wrong Timeframe / Scope', 'Nói về giai đoạn sau Thế chiến II (sau 1909) và ở quy mô toàn cầu.'),
                ('Missing Historical Lineage', 'Chỉ nhấn mạnh tầm quan trọng hiện nay, không chứng minh nguồn gốc lịch sử trước năm 1909.'),
                ('Đáp án đúng', 'Khớp hoàn hảo cả không gian (Arizona), mốc lịch sử xa xưa trước 1909 (thế kỷ 7 CN) và tính kế thừa đến hiện đại (“still utilized by today’s engineers”).'),
                ('Wrong Timeframe', 'Hệ thống phun mưa phát triển vào cuối thế kỷ 20 — sau năm 1909 rất lâu.'),
            ],
        ),
        _q(
            'may2025_rw_m2h_q12', 12, 'Information and Ideas', 'Command of Evidence (Quantitative)', 'Medium',
            _html_table(
                'Properties of TRAPPIST-1 Exoplanets Compared to Earth’s Properties',
                ['Planet', 'Orbital period (days)', 'Planet radius (Earth radii)'],
                [
                    ['<b>Earth</b>', '365.26', '1'],
                    ['<b>TRAPPIST-1b</b>', '1.51', '1.09'],
                    ['<b>TRAPPIST-1d</b>', '4.05', '0.77'],
                    ['<b>TRAPPIST-1e</b>', '6.1', '0.92'],
                    ['<b>TRAPPIST-1f</b>', '9.21', '1.04'],
                ],
            ) + '<p>TRAPPIST-1 is a planetary system with a central red dwarf star and several Earth-sized exoplanets. Each planet in this system is so close in orbit to the star that the gravitational forces acting between the planet and the star cause the planet’s rotational period around its axis and orbital period around the star to be equal. For example, the orbital period of TRAPPIST-1e is _______</p>',
            'Which choice most effectively uses data from the table to complete the example?',
            [
                '1.51 days, which is the shortest rotational period of any of the TRAPPIST planets.',
                '9.21 days, which is the same as the rotational period of TRAPPIST-1f.',
                '6.1 days, and its rotational period is 0.92 days.',
                '6.1 days, and its rotational period is also 6.1 days.',
            ],
            'D',
            'Kết hợp quy tắc trong đoạn văn + dữ liệu bảng: Đoạn văn khẳng định mỗi hành tinh trong hệ TRAPPIST-1 có chu kỳ tự quay (rotational period) BẰNG chu kỳ quỹ đạo (orbital period). Tra hàng **TRAPPIST-1e**: Orbital period = **6.1 days** → do đó rotational period cũng là **6.1 days**! Cẩn thận bẫy C lấy nhầm số 0.92 (đó là cột Bán kính hành tinh, không phải chu kỳ quay) → Chọn D.',
            'Với câu bảng kết hợp quy tắc vật lý/toán học trong bài, luôn đọc kỹ tiêu đề cột để không bị gài bẫy đổi cột (0.92 là bán kính, không phải ngày!).',
            [
                ('Wrong Row', '1.51 ngày là chu kỳ quỹ đạo của TRAPPIST-1b, không phải TRAPPIST-1e.'),
                ('Wrong Row', '9.21 ngày là chu kỳ quỹ đạo của TRAPPIST-1f, không phải TRAPPIST-1e.'),
                ('Column Swap Trap', '0.92 là bán kính hành tinh theo bán kính Trái Đất (“Planet radius”), KHÔNG phải chu kỳ tự quay theo ngày.'),
                ('Đáp án đúng', 'Tra đúng hàng TRAPPIST-1e (6.1 ngày) và áp dụng đúng quy tắc khóa thủy triều trong bài (chu kỳ tự quay = chu kỳ quỹ đạo = 6.1 ngày).'),
            ],
        ),
        _q(
            'may2025_rw_m2h_q13', 13, 'Information and Ideas', 'Command of Evidence (Textual)', 'Hard',
            '<p><i>The Clouds</i> is a 423 BCE play by Aristophanes, originally written in ancient Greek. At the time, professional intellectuals called sophists taught customers rhetorical techniques to use in public speaking, along with providing instruction in other subjects. In the play, Aristophanes satirizes sophists as having an exaggerated sense of their own wisdom, as seen when the character _______</p>',
            'Which choice most effectively uses a quotation from a translation of <i>The Clouds</i> to illustrate the claim?',
            [
                'Socrates, a sophist, says to a new customer, “Come, then, take care that, whenever I propound any clever dogma about abstruse matters, you [seize] immediately.”',
                'Strepsiades says of a sophist business, “There dwell men who in speaking of the heavens persuade people that it is an oven, and that it encompasses us, and that we are the embers. These men teach, if one give them money, to conquer in speaking, right or wrong.”',
                'Socrates, a sophist, says to a potential customer, “Is the power of speaking, pray, implanted in your nature?”',
                'Strepsiades encourages his son to learn to be a sophist, saying, “Reform your habits as quickly as possible, and go and learn what I advise.”',
            ],
            'A',
            'Khóa đúng sắc thái của luận điểm: Aristophanes châm biếm các nhà ngụy biện (sophists) vì có **ý thức thổi phồng về trí tuệ của chính mình** (“an exaggerated sense of their own wisdom” — tự mãn, khoe khoang trí tuệ cao siêu). Trong A, chính nhân vật Socrates (được khắc họa là một sophist) tự tâng bốc lời giảng của mình là “clever dogma about abstruse matters” (những học thuyết tài tình về các vấn đề uyên thâm) và bảo học trò phải lập tức chộp lấy → Chọn A!',
            'Phân biệt cực kỹ giữa B và A: B châm biếm sự xảo biện trục lợi (“if one give them money, to conquer... right or wrong”), KHÔNG minh họa việc bản thân họ tự ảo tưởng về sự thông thái của chính mình như A!',
            [
                ('Đáp án đúng', 'Socrates tự xưng lời giảng của mình là “clever dogma about abstruse matters” — minh họa trực tiếp sự tự phụ thổi phồng về trí tuệ bản thân.'),
                ('Different Criticism Trap', 'Chỉ trích việc ngụy biện lấy tiền để bẻ cong đúng sai và thuyết phục chuyện phi lý, không thể hiện sự tự mãn về trí tuệ của bản thân họ.'),
                ('Off-Point', 'Chỉ là câu hỏi thăm dò năng khiếu hùng biện tự nhiên của khách hàng.'),
                ('Off-Point', 'Chỉ là lời Strepsiades khuyên con trai sửa thói quen và đi học nghề ngụy biện.'),
            ],
        ),
        _q(
            'may2025_rw_m2h_q14', 14, 'Information and Ideas', 'Command of Evidence (Textual)', 'Medium',
            '<p>A student is writing an essay on the subject of cultured meat, which is grown in a laboratory and is intended to help reduce the number of livestock harvested for food. The student wants to make the case that cultured meat production may be useful in responding to an expected widespread change in the public’s behavior.</p>',
            'Which quotation from a publication by a researcher would most effectively support the student’s claim?',
            [
                '“The flavor of meat from livestock differs across species (from pig to chicken to cow), and is also influenced by farming conditions and the breeds and genders of animals.”',
                '“Consumers tend to believe that using less packaging when selling meat products in stores would have a significant effect on the environment.”',
                '“A growing population that is including significantly more meat in its diet will contribute to an increasing demand for meat products in the 21st century.”',
                '“Researchers who advocate for the development of lab-grown meat claim that it’s better for the environment than conventional meat because it requires less water consumption.”',
            ],
            'C',
            'Khóa cụm trọng tâm trong luận điểm: “responding to an **expected widespread change in the public’s behavior**” (ứng phó với một sự thay đổi rộng khắp được dự báo trong hành vi của công chúng). Chỉ trích dẫn C nêu rõ sự thay đổi hành vi tiêu dùng diện rộng được dự báo trong thế kỷ 21: dân số tăng lên và đưa NHIỀU THỊT HƠN ĐÁNG KỂ vào khẩu phần ăn → nhu cầu thịt tăng mạnh → thịt nuôi cấy giúp đáp ứng nhu cầu mà giảm giết mổ gia súc → Chọn C.',
            'Luôn đối chiếu đúng từng từ khóa của luận điểm (“expected widespread change in public’s behavior”) thay vì chọn các lợi ích môi trường chung chung (bẫy D).',
            [
                ('Irrelevant Detail', 'Chỉ nói về các yếu tố ảnh hưởng đến hương vị thịt gia súc, không liên quan đến sự thay đổi hành vi công chúng.'),
                ('Off-Point', 'Chỉ nói niềm tin của người tiêu dùng về bao bì đóng gói thịt.'),
                ('Đáp án đúng', 'Trực tiếp nêu sự thay đổi rộng khắp được dự báo trong hành vi ăn uống của công chúng (ăn nhiều thịt hơn hẳn trong thế kỷ 21).'),
                ('Related Benefit / Wrong Claim', 'Nhắc ưu điểm tiết kiệm nước của thịt nuôi cấy — không chứng minh việc ứng phó với thay đổi hành vi tiêu dùng của công chúng.'),
            ],
        ),
        _q(
            'may2025_rw_m2h_q15', 15, 'Information and Ideas', 'Inferences', 'Hard',
            '<p>Omar Asensio and colleagues used machine-learning algorithms to examine consumer reviews of 12,720 electric-vehicle (EV) charging stations in the US. They found that privately owned or managed charging stations at or near hotels and restaurants had relatively low proportions of negative reviews, while stations at or near parking garages and lots had significantly higher proportions of negative reviews. Additionally, stations at or near parking garages and lots tend to require consumers to pay full price to use them, while stations elsewhere often offer subsidized or even complimentary charging. Assuming that stations at different sites provide roughly equivalent levels of service, these results suggest that _______</p>',
            'Which choice most logically completes the text?',
            [
                'charging stations located near parking garages and lots are more frequently visited than charging stations located near hotels and restaurants.',
                'EV drivers are more likely to visit areas with many hotels and restaurants than they are to visit areas with fewer such businesses.',
                'EV owners are usually unaware of the fees for using charging stations.',
                'users who are offered a discount have lower expectations of the quality of charging stations than users who are not offered a discount do.',
            ],
            'D',
            'Phân tích điều kiện cố định biến số: Giả sử chất lượng dịch vụ ở mọi địa điểm là **tương đương nhau** (“roughly equivalent levels of service”). Thế nhưng: trạm tính ĐỦ GIÁ (bãi đỗ xe) lại nhận tỷ lệ đánh giá tiêu cực CAO hơn hẳn, còn trạm được TRỢ GIÁ / MIỄN PHÍ (khách sạn, nhà hàng) nhận ít đánh giá tiêu cực hơn. Lý giải logic duy nhất từ chênh lệch giá cả khi chất lượng bằng nhau: người dùng được giảm giá/miễn phí có kỳ vọng khắt khe thấp hơn về chất lượng so với người phải trả đủ tiền → Chọn D!',
            'Trong câu Inferences có giả định kiểm soát biến (“Assuming that X is roughly equivalent...”), hãy đối chiếu biến số CÒN LẠI DUY NHẤT khác biệt giữa hai nhóm (trả đủ giá vs. trợ giá/miễn phí)!',
            [
                ('Metric Confusion', 'Tỷ lệ phần trăm (“proportions”) đánh giá tiêu cực cao hơn không chứng minh tần suất ghé thăm cao hơn.'),
                ('Out of Scope', 'Không có dữ liệu về thói quen chọn khu vực di chuyển của tài xế xe điện.'),
                ('Contradiction', 'Nếu người dùng thường không biết mức phí thì yếu tố trả đủ tiền hay miễn phí đã không thể tạo ra khác biệt tỷ lệ đánh giá tiêu cực.'),
                ('Đáp án đúng', 'Khi chất lượng dịch vụ ngang nhau, sự khác biệt về tỷ lệ đánh giá tiêu cực giữa nhóm trả đủ phí và nhóm được giảm/miễn phí cho thấy nhóm được ưu đãi có kỳ vọng thấp hơn.'),
            ],
        ),
        _q(
            'may2025_rw_m2h_q16', 16, 'Information and Ideas', 'Inferences', 'Hard',
            '<p>Many contemporary Indigenous painters practice a specifically Indigenous mode of abstraction; for example, Dyani White Hawk assembles compositions out of motifs common in the beadwork and other traditional arts of her tribe. In contrast, the prominent Indigenous practitioners of abstract painting during the mid-twentieth century, such as the Southern Cheyenne artist Dick West, typically aligned their compositional strategies with Abstract Expressionism—a school of painting dominated by European American artists—instead of with traditionally nonrepresentational forms of Indigenous art. Thus, in the case of West’s generation, the identification of an abstract painting as Indigenous art tends to _______</p>',
            'Which choice most logically completes the text?',
            [
                'obscure the Indigenous origins of certain motifs associated with Abstract Expressionism.',
                'place a greater emphasis on the artist’s biography than on the aesthetic merit of the painting.',
                'deny the extent to which cultural identity influences an artist’s work.',
                'depend not on stylistic details but instead on an awareness of the artist’s identity.',
            ],
            'D',
            'So sánh hai thế hệ họa sĩ trừu tượng Bản địa: (1) Thế hệ đương đại (Dyani White Hawk) đưa họa tiết truyền thống bộ tộc trực tiếp vào bố cục → nhìn phong cách là nhận ra ngay nghệ thuật Bản địa; (2) Thế hệ giữa thế kỷ 20 (Dick West) lại dùng phong cách Biểu hiện Trừu tượng (vốn do họa sĩ Mỹ gốc Âu chi phối) thay vì hình thức truyền thống Bản địa. Do đó, với thế hệ của West, việc nhận diện một bức tranh trừu tượng là nghệ thuật Bản địa không dựa trên chi tiết phong cách trên tranh mà dựa vào việc biết danh tính của người họa sĩ → Chọn D!',
            'Đặt phép đối lập trực tiếp: Contemporary (nhận diện qua họa tiết/phong cách) ↔ Mid-20th century (dùng phong cách Mỹ gốc Âu → muốn nhận diện là nghệ thuật Bản địa thì phải dựa vào danh tính nghệ sĩ).',
            [
                ('Unsupported Premise', 'Bài không hề nói các họa tiết của trường phái Biểu hiện Trừu tượng có nguồn gốc Bản địa.'),
                ('Out of Scope', 'Đoạn không bàn về “giá trị thẩm mỹ” (aesthetic merit) hay việc xem nhẹ thẩm mỹ so với tiểu sử.'),
                ('Out of Scope / Distortion', 'Việc nhận diện tác phẩm là nghệ thuật Bản địa không hề “phủ nhận” ảnh hưởng của bản sắc văn hóa.'),
                ('Đáp án đúng', 'Suy luận sắc bén: vì phong cách giống trường phái Mỹ gốc Âu, việc xếp bức tranh vào nghệ thuật Bản địa phụ thuộc vào hiểu biết về danh tính họa sĩ thay vì chi tiết tạo hình.'),
            ],
        ),
        _q(
            'may2025_rw_m2h_q17', 17, 'Standard English Conventions', 'Boundaries', 'Medium',
            '<p>In rural Minnesota, ecologist Leroy Walston conducted a study to determine whether seeding solar panel fields with wildflowers could bolster pollinator populations in nearby food crops. Walston’s findings indicate that—assuming solar panel installers’ _______ practice has the potential to increase the number of native bees in crops near solar fields throughout the Midwest by up to 20 percent.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['cooperation, this', 'cooperation this', 'cooperation—this', 'cooperation: this'],
            'C',
            'Quy tắc Cặp dấu bổ sung đồng nhất (Paired Punctuation): Ngay sau “indicate that” có dấu gạch ngang dài mở phần chêm xen: `that—assuming solar panel installers’ cooperation—this practice has...`. Đã mở bằng gạch ngang (—) thì BẮT BUỘC phải đóng bằng gạch ngang (—) → Chọn C.',
            'Thấy dấu `—` mở mệnh đề/cụm chêm xen ngay trước chỗ trống → chốt ngay dấu `—` đóng lại, tuyệt đối không phối lệch gạch ngang với dấu phẩy hay hai chấm!',
            [
                ('Mismatched Pair', 'Mở bằng gạch ngang (—) nhưng đóng bằng dấu phẩy (,) là sai quy tắc cặp dấu.'),
                ('Unclosed Parenthetical', 'Thiếu hoàn toàn dấu đóng cho cụm chêm xen “assuming solar panel installers’ cooperation”.'),
                ('Đáp án đúng', 'Đóng chuẩn cặp gạch ngang: “indicate that—assuming solar panel installers’ cooperation—this practice has...”.'),
                ('Mismatched Pair', 'Mở bằng gạch ngang (—) nhưng đóng bằng dấu hai chấm (:) là sai ngữ pháp.'),
            ],
        ),
        _q(
            'may2025_rw_m2h_q18', 18, 'Standard English Conventions', 'Boundaries', 'Medium',
            '<p>George Saunders concludes his essay “What Writers Really Do When They Write” by comparing the work of fiction writing to the act of juggling. The author-as-juggler performs a _______ gathering of central themes and tensions, the tossing of these elements into a dynamic narrative, and the catching of the resolutions that emerge.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['routine, the', 'routine. The', 'routine; the', 'routine: the'],
            'D',
            'Trước chỗ trống là mệnh đề độc lập hoàn chỉnh: “The author-as-juggler performs a routine”. Phần sau chỗ trống là chuỗi liệt kê 3 cụm danh động từ giải thích cụ thể màn biểu diễn (“routine”) đó gồm những động tác nào (“the gathering..., the tossing..., and the catching...”) — KHÔNG có động từ chính nên không phải mệnh đề độc lập → Dùng dấu hai chấm (:) để giới thiệu danh sách giải thích → Chọn D.',
            'Loại ngay dấu chấm (B) và dấu chấm phẩy (C) vì phần sau không có động từ chia thì (mảnh câu); chọn dấu hai chấm (D) để mở danh sách 3 hành động giải thích cho “a routine”.',
            [
                ('List Ambiguity', 'Dùng dấu phẩy khiến “a routine” trông như mục 1 ngang hàng với 3 cụm sau thay vì là danh từ bao quát được giải thích bởi 3 động tác tung hứng.'),
                ('Fragment', 'Tách câu bằng dấu chấm biến chuỗi “The gathering..., the tossing..., and the catching...” thành câu cụt không có động từ chính.'),
                ('Semicolon Error', 'Sau dấu chấm phẩy phải là mệnh đề độc lập hoàn chỉnh, không thể là chuỗi cụm danh từ.'),
                ('Đáp án đúng', 'Dấu hai chấm chuẩn xác nối mệnh đề độc lập với danh sách 3 động tác giải thích chi tiết cho “a routine”.'),
            ],
        ),
        _q(
            'may2025_rw_m2h_q19', 19, 'Standard English Conventions', 'Boundaries', 'Hard',
            '<p>The Balkan nation of Bosnia and Herzegovina does not have one president but _______ as members of the office of the presidency, one representing the nation’s Bosniaks, one its Serbs, and one its Croats, these elected officials take turns serving as the office’s chairperson.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['three who are known', 'three, known', 'three, who are known', 'three. Known'],
            'D',
            'Soi tận cuối câu để phát hiện mệnh đề độc lập thứ 2: “these elected officials take turns serving as the office’s chairperson.” (chủ ngữ `these elected officials` + động từ chính `take`). Phía trước cũng đã là một mệnh đề độc lập hoàn chỉnh (“The Balkan nation... does not have one president but three”). Do đó BẮT BUỘC tách thành 2 câu bằng dấu chấm (`three. Known`) để tránh lỗi Comma Splice! Cụm phân từ quá khứ “Known as members...” mở câu 2 bổ nghĩa hoàn hảo cho “these elected officials” → Chọn D.',
            'Mẹo xử lý câu dài M2 Hard: Luôn đọc tới dấu chấm cuối câu tìm động từ chính thứ hai (“take turns”)! Thấy 2 IC mà không có liên từ → bắt buộc tách câu bằng dấu chấm/chấm phẩy.',
            [
                ('Comma Splice', 'Nối mệnh đề độc lập đầu với mệnh đề độc lập sau (“these elected officials take turns...”) chỉ bằng dấu phẩy.'),
                ('Comma Splice', 'Vẫn để hai mệnh đề độc lập dính nhau bằng dấu phẩy ở trước “these elected officials”.'),
                ('Comma Splice', 'Mệnh đề quan hệ “who are known...” không giải quyết được lỗi hai mệnh đề độc lập nối nhau bằng dấu phẩy.'),
                ('Đáp án đúng', 'Tách hai mệnh đề độc lập sạch sẽ bằng dấu chấm; mở câu 2 bằng cụm phân từ “Known as members..., these elected officials take turns...”.'),
            ],
        ),
        _q(
            'may2025_rw_m2h_q20', 20, 'Standard English Conventions', 'Boundaries', 'Medium',
            '<p>In his work, Tlingit/Nisga’a artist Da-ka-xeen Mehner uses photography, performance, and sculpture to explore his identity and cultural history. Since 1989, Indianapolis’s Eiteljorg Museum has celebrated the work of groundbreaking contemporary Native _______ in 2015, it awarded Mehner one of its prestigious artist fellowships.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['artists and', 'artists;', 'artists, thus', 'artists,'],
            'B',
            'Hai mệnh đề độc lập hoàn chỉnh: IC1 = “Since 1989, Indianapolis’s Eiteljorg Museum has celebrated the work of groundbreaking contemporary Native artists”; IC2 = “in 2015, it awarded Mehner one of its prestigious artist fellowships.” Chỉ có dấu chấm phẩy (;) ở B nối hợp chuẩn hai mệnh đề độc lập này → Chọn B.',
            'Thuộc lòng 3 lỗi nối IC bị loại ngay: `, [IC]` (comma splice), `, thus [IC]` (`thus` là trạng từ nối, KHÔNG phải FANBOYS!), và `and [IC]` thiếu dấu phẩy trước FANBOYS!',
            [
                ('Missing Comma + FANBOYS', 'Nối hai mệnh đề độc lập bằng “and” bắt buộc phải có dấu phẩy đứng trước (`, and`).'),
                ('Đáp án đúng', 'Dấu chấm phẩy (;) nối chuẩn xác hai mệnh đề độc lập có quan hệ ý nghĩa chặt chẽ.'),
                ('Comma Splice (Conjunctive Adverb)', '“thus” là trạng từ liên kết (không phải FANBOYS), đứng sau dấu phẩy giữa hai IC sẽ tạo lỗi Comma Splice.'),
                ('Comma Splice', 'Dấu phẩy đơn không thể nối hai mệnh đề độc lập.'),
            ],
        ),
        _q(
            'may2025_rw_m2h_q21', 21, 'Standard English Conventions', 'Form, Structure, and Sense', 'Hard',
            '<p>If an animal can recognize itself in a reflective surface (“the mirror test”), it is considered to have self-awareness. In a recent study, scientists _______ for evidence of self-awareness in snakes, species that rely primarily on olfactory rather than visual processing, adapted the test to foreground smell, modifying the scent trails of North American eastern garter snakes and African ball pythons.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['searched', 'searching', 'have searched', 'were searching'],
            'B',
            'Tìm động từ chính của chủ ngữ “scientists”: bỏ cụm đồng vị giữa 2 dấu phẩy “, species that rely primarily on olfactory rather than visual processing,” → ta thấy động từ chia thì chính là **adapted** (“scientists ... adapted the test to foreground smell”)! Vì câu đã có động từ chính “adapted”, chỗ trống KHÔNG thể điền thêm động từ chia thì (finite verb) mà PHẢI dùng phân từ hiện tại **searching** để làm cụm phân từ bổ nghĩa cho “scientists” → Chọn B.',
            'Khi có 3 đáp án là động từ chia thì (`searched / have searched / were searching`) và chỉ 1 đáp án là phân từ (`searching`) → kiểm tra xem phía sau đã có động từ chính (`adapted`) chưa!',
            [
                ('Double Finite Verb', 'Nếu điền “searched” (động từ chia thì) sẽ đụng độ với động từ chính “adapted” mà không có liên từ nối.'),
                ('Đáp án đúng', 'Phân từ hiện tại “searching” tạo cụm bổ nghĩa gọn gàng (“scientists searching for evidence... adapted the test”).'),
                ('Double Finite Verb', '“have searched” là động từ chia thì, tạo lỗi câu có hai động từ chính không liên kết.'),
                ('Double Finite Verb', '“were searching” là động từ chia thì, gây xung đột với động từ chính “adapted”.'),
            ],
        ),
        _q(
            'may2025_rw_m2h_q22', 22, 'Standard English Conventions', 'Form, Structure, and Sense', 'Hard',
            '<p>The parks of Detroit, Michigan, seem to be making people happier. In 2022, a team of researchers _______ to find connections between the physical location in which a social media post was created and the content of that post analyzed geotagged social media posts from various sites in Detroit. The team found that posts from the city’s parks contained more words associated with happiness than did the other posts.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['hoping', 'were hoping', 'hoped', 'was hoping'],
            'A',
            'Cấu trúc tương tự câu 21! Chủ ngữ chính là “a team of researchers”, và động từ chia thì chính nằm phía sau là **analyzed** (“a team of researchers ... analyzed geotagged social media posts”). Do đó chỗ trống phải dùng phân từ hiện tại **hoping** (non-finite participle) để bổ nghĩa cho “a team of researchers”, tránh lỗi hai động từ chính liên tiếp → Chọn A.',
            'Quy tắc 1-Chủ-Ngữ-1-Động-Từ-Chính: Thấy động từ chính “analyzed” đứng cuối mệnh đề → chỗ trống giữa câu phải là dạng phân từ rút gọn (“hoping”), không chia thì!',
            [
                ('Đáp án đúng', 'Phân từ “hoping” mở cụm bổ nghĩa (“a team of researchers hoping to find connections... analyzed...”), giữ đúng 1 động từ chính duy nhất.'),
                ('Double Finite Verb', '“were hoping” là động từ chia thì (lại sai hòa hợp số ít với “a team”), đụng độ với động từ chính “analyzed”.'),
                ('Double Finite Verb', '“hoped” là động từ chia thì, tạo lỗi ghép hai động từ chính “hoped ... analyzed” thiếu liên từ.'),
                ('Double Finite Verb', '“was hoping” là động từ chia thì, không thể đứng cùng động từ chính “analyzed” trong cùng một mệnh đề.'),
            ],
        ),
        _q(
            'may2025_rw_m2h_q23', 23, 'Expression of Ideas', 'Transitions', 'Medium',
            '<p>A team of ornithologists documented patterns of conspecific brood parasitism among wood ducks (<i>Aix sponsa</i>) in California. The researchers observed several female wood ducks visiting dozens of nesting sites and laying eggs to be incubated by other nesting <i>A. sponsa</i>. Subject 7F64B, _______ visited a select few nesting sites before laying and incubating her eggs herself.</p>',
            'Which choice completes the text with the most logical transition?',
            ['similarly,', 'alternatively,', 'in particular,', 'for example,'],
            'B',
            'Quan hệ tương phản hành vi rõ nét: Câu 2 mô tả nhiều con vịt cái ghé HÀNG CHỤC tổ và đẻ trứng cho con KHÁC ấp (“incubated by other nesting <i>A. sponsa</i>”). Câu 3 mô tả cá thể 7F64B chỉ ghé VÀI tổ chọn lọc rồi TỰ ấp trứng của mình (“incubating her eggs herself”). Ba phương án A, C, D đều cùng chiều/minh họa; duy nhất B (“alternatively,” = trái lại / theo một hướng khác) diễn đạt đúng sự khác biệt → Chọn B.',
            'Chiến lược loại nhóm: `similarly`, `in particular`, `for example` đều mang chiều thuận/cụ thể hóa — chỉ duy nhất `alternatively` mang chiều tương phản/hành vi khác biệt!',
            [
                ('False Similarity', 'similarly = tương tự — sai vì cá thể 7F64B tự ấp trứng, trái ngược hoàn toàn với việc đẻ nhờ.'),
                ('Đáp án đúng', 'alternatively = theo cách khác / trái lại — thể hiện chính xác chiến lược sinh sản khác hẳn của cá thể 7F64B.'),
                ('Wrong Relationship', 'in particular = cụ thể là — 7F64B không phải trường hợp điển hình cho hành vi ký sinh tổ ở câu trước.'),
                ('Wrong Relationship', 'for example = ví dụ — 7F64B làm ngược lại chứ không minh họa cho hành vi đẻ nhờ ở câu trước.'),
            ],
        ),
        _q(
            'may2025_rw_m2h_q24', 24, 'Expression of Ideas', 'Rhetorical Synthesis', 'Easy',
            '<p>While researching a topic, a student has taken the following notes:</p><ul><li>“Organ²/ASLSP (As Slow as Possible)” is a musical piece by avant-garde composer John Cage.</li><li>A specially designed automated organ in St. Burchardi Church in Halberstadt, Germany, began playing the piece in 2001.</li><li>It is scheduled to stop playing the piece in 2640.</li><li>The performance will last 639 years.</li><li>It will be the longest continuous musical performance in history.</li></ul>',
            'The student wants to indicate how long John Cage’s musical piece will last. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
            [
                'John Cage is the composer of the musical piece “Organ²/ASLSP (As Slow as Possible).”',
                'An organ in St. Burchardi Church in Halberstadt, Germany, began playing a musical piece by avant-garde composer John Cage.',
                '“Organ²/ASLSP (As Slow as Possible)” is a musical piece currently being played in St. Burchardi Church in Halberstadt, Germany.',
                'Lasting 639 years, John Cage’s musical piece will be the longest continuous musical performance in history.',
            ],
            'D',
            'Mục tiêu (Goal): Cho biết bản nhạc của John Cage sẽ kéo dài BAO LÂU (“indicate how long John Cage’s musical piece will last”). Chỉ duy nhất đáp án D nêu thời lượng cụ thể “Lasting 639 years” → Chọn D.',
            'Với Goal yêu cầu thông số cụ thể (“how long”), quét ngay con số thời lượng (639 years) trong 4 đáp án — xử lý trong 5 giây!',
            [
                ('Missing Duration', 'Chỉ giới thiệu tên tác giả và tác phẩm, không có thời lượng.'),
                ('Missing Duration', 'Chỉ nêu địa điểm biểu diễn và tác giả, không nói kéo dài bao lâu.'),
                ('Missing Duration', 'Chỉ nói bản nhạc đang được biểu diễn tại nhà thờ ở Đức, thiếu thời lượng.'),
                ('Đáp án đúng', 'Nêu rõ thời lượng “Lasting 639 years” và gắn đúng với tác phẩm của John Cage.'),
            ],
        ),
        _q(
            'may2025_rw_m2h_q25', 25, 'Expression of Ideas', 'Rhetorical Synthesis', 'Easy',
            '<p>While researching a topic, a student has taken the following notes:</p><ul><li>The El Carmen-Verde Mountains are located in northwestern Mexico.</li><li>They cover an area of 1,141 square miles (mi<sup>2</sup>).</li><li>The Perilla Mountains are located in the southwestern United States.</li><li>They cover an area of 82 mi<sup>2</sup>.</li><li>These mountain ranges are two of the dozens of “sky islands” in the southwestern US and northwestern Mexico.</li><li>A sky island is an isolated mountain range whose environment differs drastically from that of the surrounding lowlands.</li></ul>',
            'The student wants to compare the sizes of the two mountain ranges. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
            [
                'There are dozens of isolated mountain ranges located in the southwestern US and northwestern Mexico.',
                'Sky islands in northwestern Mexico and the southwestern US can vary in size.',
                'In terms of area, the El Carmen-Verde Mountains (which cover 1,141 mi<sup>2</sup>) are larger than the Perilla Mountains (82 mi<sup>2</sup>).',
                'The El Carmen-Verde Mountains and the Perilla Mountains are both isolated mountain ranges whose environments differ drastically from that of the surrounding lowlands.',
            ],
            'C',
            'Mục tiêu (Goal): So sánh KÍCH THƯỚC của HAI dãy núi (“compare the sizes of the two mountain ranges”). Chỉ đáp án C nêu tên cả hai dãy núi, kèm diện tích cụ thể (1,141 mi<sup>2</sup> vs. 82 mi<sup>2</sup>) và so sánh trực tiếp (“are larger than”) → Chọn C.',
            'Tránh bẫy B quá chung chung (“Sky islands... can vary in size”) — Goal đòi hỏi so sánh trực tiếp HAI dãy núi cụ thể!',
            [
                ('Wrong Synthesis Goal', 'Chỉ nêu số lượng và vị trí các dãy núi biệt lập, không so sánh kích thước hai dãy núi.'),
                ('Too General', 'Chỉ nói chung chung rằng các “sky islands” có thể khác nhau về kích thước, không so sánh cụ thể El Carmen-Verde và Perilla.'),
                ('Đáp án đúng', 'So sánh trực tiếp diện tích của hai dãy núi cụ thể: El Carmen-Verde (1,141 mi<sup>2</sup>) lớn hơn Perilla (82 mi<sup>2</sup>).'),
                ('Wrong Criterion', 'Nêu điểm tương đồng về đặc tính “sky island”, không đề cập kích thước.'),
            ],
        ),
        _q(
            'may2025_rw_m2h_q26', 26, 'Expression of Ideas', 'Rhetorical Synthesis', 'Medium',
            '<p>While researching a topic, a student has taken the following notes:</p><ul><li>Gertrud Arndt was a photographer born in Racibórz, Poland.</li><li>She began attending the Bauhaus in 1923.</li><li>The Bauhaus was an influential German art and design school.</li><li>The school famously espoused the design principle of “form follows function.”</li><li>“Form follows function” means that an object’s shape should be determined primarily by its intended purpose.</li></ul>',
            'The student wants to explain the principle espoused by the Bauhaus. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
            [
                'According to the Bauhaus, an object’s intended purpose (function) should primarily determine its shape (form).',
                'An object’s intended purpose and its shape are two elements of the design principle “form follows function.”',
                'Famous for its principle of “form follows function,” the Bauhaus was an influential German art and design school.',
                'Gertrud Arndt was a photographer who attended the Bauhaus, famous for espousing the principle of “form follows function.”',
            ],
            'A',
            'Mục tiêu (Goal): GIẢI THÍCH nguyên lý do trường Bauhaus đề xướng (“explain the principle espoused by the Bauhaus”). C và D chỉ nêu TÊN khẩu hiệu “form follows function” chứ không giải thích ý nghĩa; B chỉ liệt kê hai yếu tố chứ không nói yếu tố nào quyết định yếu tố nào và cũng bỏ mất tên Bauhaus. Duy nhất A vừa gắn đúng với Bauhaus vừa giải thích rõ bản chất nguyên lý (mục đích sử dụng quyết định hình dáng) → Chọn A.',
            'Động từ “explain the principle” bắt buộc đáp án phải diễn giải NỘI DUNG/Ý NGHĨA của nguyên lý đó, không chỉ lặp lại tên gọi nguyên lý!',
            [
                ('Đáp án đúng', 'Vừa quy đúng về trường Bauhaus vừa giải thích rõ ràng nguyên lý “form follows function”: mục đích sử dụng phải quyết định chủ yếu hình dáng vật thể.'),
                ('Incomplete Explanation', 'Chỉ liệt kê “mục đích” và “hình dáng” là hai yếu tố, không giải thích mối quan hệ nhân quả giữa chúng và thiếu tên Bauhaus.'),
                ('Names Without Explaining', 'Chỉ gọi tên khẩu hiệu “form follows function” mà không giải thích ý nghĩa của nó.'),
                ('Wrong Focus / No Explanation', 'Tập trung vào Gertrud Arndt và chỉ nêu tên khẩu hiệu chứ không giải thích nội dung nguyên lý.'),
            ],
        ),
        _q(
            'may2025_rw_m2h_q27', 27, 'Expression of Ideas', 'Rhetorical Synthesis', 'Hard',
            '<ul><li>Warrick Dunn and Tiki Barber had historic careers as running backs in the National Football League (NFL).</li><li>The running back position entails running, or rushing, down the field with the football to gain yards for the team.</li><li>Warrick Dunn gained a total of 10,967 rushing yards in his career.</li><li>He played for the Tampa Bay Buccaneers and the Atlanta Falcons.</li><li>Tiki Barber gained a total of 10,449 rushing yards in his career.</li><li>He played for the New York Giants.</li></ul>',
            'Which choice most effectively uses information from the given sentences to begin a narrative about one of the athletes?',
            [
                'While Dunn finished his career with more rushing yards, both Dunn and Barber reached the career milestone of rushing for over 10,000 yards total.',
                'Dunn began his career with the Tampa Bay Buccaneers; Barber started with New York Giants.',
                'When Dunn put on his Tampa Bay Buccaneers uniform for his first NFL game, he began what would become a legendary professional career.',
                'Dunn’s blend of speed, power, and agility helped him accrue 10,967 rushing yards by the end of his career, etching his name into the NFL’s record books.',
            ],
            'C',
            'Mục tiêu (Goal): **Mở đầu một câu chuyện tự sự về MỘT trong hai vận động viên** (“begin a narrative about one of the athletes”). A và B nói về CẢ HAI vận động viên theo kiểu so sánh/bách khoa khô khan. D lại tổng kết CUỐI sự nghiệp (“by the end of his career”) và tự thêm chi tiết không có trong ghi chú (“speed, power, and agility”). Chỉ C mở màn đúng kiểu kể chuyện ngay khoảnh khắc khởi đầu sự nghiệp của riêng Dunn (“When Dunn put on his Tampa Bay Buccaneers uniform for his first NFL game, he began what would become a legendary professional career.”) → Chọn C.',
            'Với dạng Rhetorical Synthesis “begin a narrative about one of X”: chọn câu có giọng văn tự sự mở màn từ mốc khởi đầu và chỉ tập trung vào ĐÚNG MỘT nhân vật!',
            [
                ('Wrong Focus / Non-Narrative', 'So sánh thành tích tổng kết của cả hai vận động viên theo văn phong phân tích, không phải mở đầu tự sự cho một người.'),
                ('Two Subjects / Non-Narrative', 'Liệt kê khô khan đội bóng của cả hai người (và thiếu mạo từ “the” trước New York Giants), không có khung mở đầu tự sự.'),
                ('Đáp án đúng', 'Tập trung vào đúng một vận động viên (Warrick Dunn) và dùng giọng tự sự giàu hình ảnh mở ngay khoảnh khắc khởi đầu sự nghiệp NFL huyền thoại.'),
                ('End-of-Career Summary / Unsupported', 'Tổng kết cuối sự nghiệp thay vì mở đầu câu chuyện, đồng thời bịa thêm chi tiết không có trong ghi chú (“speed, power, and agility”).'),
            ],
        ),
    ]


# ============================================================================
# MODULE 2 LOWER / EASY ROUTE (27 Qs — Source: mod2_rw.txt)
# ============================================================================

def get_m2_lower_questions():
    return [
        _q(
            'may2025_rw_m2l_q1', 1, 'Craft and Structure', 'Words in Context', 'Easy',
            '<p>Ancient Inca inhabiting the Andes Mountains used terraces, rows of flattened land with built-in irrigation systems, to grow crops at different altitudes. This method of farming proved to be highly _______, as evidenced by the great number and variety of crops grown at that time.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            ['uniform', 'effective', 'chaotic', 'burdensome'],
            'B',
            'Bằng chứng ngay sau cụm “as evidenced by”: “the great number and variety of crops grown at that time” (số lượng lớn và sự đa dạng cây trồng trồng được thời bấy giờ) → chứng tỏ phương pháp canh tác ruộng bậc thang vô cùng HIỆU QUẢ (“effective”) → Chọn B.',
            'Cụm “as evidenced by” báo hiệu manh mối chứng minh trực tiếp cho tính từ cần điền: sản lượng dồi dào & đa dạng → “effective”.',
            [
                ('Wrong Meaning', 'uniform = đồng nhất — trái với việc trồng nhiều loại cây đa dạng ở các độ cao khác nhau.'),
                ('Đáp án đúng', 'effective = hiệu quả — được chứng minh trực tiếp qua số lượng lớn và sự đa dạng của các loại cây trồng.'),
                ('Wrong Tone', 'chaotic = hỗn loạn — trái với hệ thống ruộng bậc thang có tưới tiêu quy củ và hiệu quả.'),
                ('Wrong Tone', 'burdensome = nặng nề, phiền phức — trái chiều với bằng chứng thành công về sản lượng cây trồng.'),
            ],
        ),
        _q(
            'may2025_rw_m2l_q2', 2, 'Craft and Structure', 'Words in Context', 'Easy',
            '<p><i>The following text is from Meredith Nicholson’s 1910 short story “The Girl with the Red Feather.”</i></p><p style="padding-left:16px;">Mrs. Webster G. Burgess always maintains that nothing her husband may do can shock her. When her husband had not <u>appeared</u> at seven she explained to her guest that he had been detained by an unexpected meeting of a clearing-house committee.</p>',
            'As used in the text, what does the word “appeared” most nearly mean?',
            ['Pretended', 'Developed', 'Responded', 'Arrived'],
            'D',
            'Ngữ cảnh: Đã bảy giờ mà chồng bà vẫn chưa “appeared”, nên bà giải thích với khách rằng ông bị giữ lại vì cuộc họp đột xuất (“detained by an unexpected meeting”) → “appeared” ở đây có nghĩa là xuất hiện / CÓ MẶT / TỚI NƠI (“Arrived”) → Chọn D.',
            'Thử thay trực tiếp từng đáp án vào câu: “When her husband had not arrived at seven... he had been detained” → khớp tự nhiên 100%!',
            [
                ('Wrong Meaning', 'Pretended = giả vờ — hoàn toàn vô nghĩa khi ghép với “at seven” và “detained”.'),
                ('Wrong Meaning', 'Developed = phát triển — không hợp ngữ cảnh.'),
                ('Wrong Meaning', 'Responded = phản hồi — không khớp với lý do bị giữ chân tại cuộc họp.'),
                ('Đáp án đúng', 'Arrived = đến nơi, có mặt — khớp chính xác hoàn cảnh ông chồng chưa về kịp lúc 7 giờ vì bận họp.'),
            ],
        ),
        _q(
            'may2025_rw_m2l_q3', 3, 'Craft and Structure', 'Words in Context', 'Easy',
            '<p><i>The following text is from Jhumpa Lahiri’s 2003 novel</i> The Namesake. <i>Gogol, a child, is at a beach in Massachusetts with his father.</i></p><p style="padding-left:16px;">He watches his father raise a kite within minutes into the wind, so high that Gogol must <u>tip</u> his head back in order to see, a rippling speck against the sky. The wind whips around their ears, turning their faces cold.</p><p style="text-align:right;font-size:13px;color:#475569;">©2003 by Jhumpa Lahiri</p>',
            'As used in the text, what does the word “tip” most nearly mean?',
            ['Lean', 'Inform', 'Pay', 'Produce'],
            'A',
            'Con diều bay cao đến mức cậu bé Gogol phải ngửa/nghiêng đầu ra sau (“tip his head back”) mới nhìn thấy → “tip” có nghĩa là NGHIÊNG / NGẢ (“Lean”) → Chọn A.',
            'Cảnh giác các nghĩa khác của từ đa nghĩa “tip” (cho tiền boa = Pay, mật báo = Inform) — bám sát cụm vật lý “tip his head back” → “Lean” (nghiêng/ngửa).',
            [
                ('Đáp án đúng', 'Lean = nghiêng, ngả — khớp hoàn toàn động tác ngửa đầu ra sau để nhìn con diều bay cao trên trời.'),
                ('Secondary Meaning Trap', 'Inform = báo tin (như “tip off”) — sai nghĩa trong ngữ cảnh động tác đầu.'),
                ('Secondary Meaning Trap', 'Pay = trả tiền boa (như “tip a waiter”) — sai hoàn toàn ngữ cảnh.'),
                ('Wrong Meaning', 'Produce = tạo ra — không khớp nghĩa với “his head back”.'),
            ],
        ),
        _q(
            'may2025_rw_m2l_q4', 4, 'Craft and Structure', 'Words in Context', 'Easy',
            '<p>Geomagnetic storms can disturb Earth’s ionosphere, causing the models underlying the Global Positioning System (GPS) to produce inaccurate calculations. This illustrates the effect that space weather events can have on the _______ of GPS and other systems that are dependent on satellite navigation.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            ['significance', 'reliability', 'extent', 'complexity'],
            'B',
            'Câu 1 nêu bão địa từ làm các mô hình GPS tạo ra những phép tính KHÔNG CHÍNH XÁC (“inaccurate calculations”). Việc tính toán thiếu chính xác tác động trực tiếp đến ĐỘ TIN CẬY (“reliability”) của hệ thống GPS → Chọn B.',
            'Ánh xạ trực tiếp: “produce inaccurate calculations” ↔ ảnh hưởng đến “reliability” (độ tin cậy/tính chính xác ổn định).',
            [
                ('Wrong Meaning', 'significance = tầm quan trọng/ý nghĩa — sai trọng tâm về tính chính xác của phép tính.'),
                ('Đáp án đúng', 'reliability = độ tin cậy — phản ánh trực tiếp tác động của việc sinh ra “inaccurate calculations”.'),
                ('Wrong Meaning', 'extent = quy mô/mức độ rộng — không khớp ngữ cảnh sai lệch tính toán.'),
                ('Wrong Meaning', 'complexity = sự phức tạp — bão địa từ làm giảm độ chính xác, không làm thay đổi mức độ phức tạp của hệ thống.'),
            ],
        ),
        _q(
            'may2025_rw_m2l_q5', 5, 'Craft and Structure', 'Text Structure and Purpose', 'Medium',
            '<p>Popularized in sixteenth- and seventeenth-century England by such poets as William Shakespeare and Edmund Spenser, the sonnet sequence (a series of fourteen-line poems unified by overarching thematic concerns) remains a prevalent poetic genre. Although the sonnet’s intricate, rule-bound structure makes writing even one sonnet—let alone an entire series—intrinsically challenging, more recent poets from Gwendolyn Brooks to Marilyn Nelson have undertaken sonnet sequences, likely in part because of the opportunity the genre presents for showcasing a poet’s virtuosity and ingenuity.</p>',
            'Which choice best states the main purpose of the text?',
            [
                'To describe some of the innovations Brooks and Nelson have introduced to the sonnet sequence',
                'To contrast the more creative sonnet sequences of Brooks and Nelson with the more conventional ones of Shakespeare and Spenser',
                'To enumerate the structural features of sonnet sequences that make them challenging to compose',
                'To suggest a reason for the enduring appeal of the sonnet sequence among poets despite its challenging form',
            ],
            'D',
            'Cấu trúc chính: Giới thiệu thể thơ chuỗi sonnet vẫn phổ biến từ thế kỷ 16–17 đến nay; mặc dù hình thức chặt chẽ rất khó viết (“Although... intrinsically challenging”), các nhà thơ gần đây vẫn chọn thể thơ này, có lẽ một phần vì (“likely in part because”) nó cho họ cơ hội thể hiện tài năng bậc thầy và sự sáng tạo → Mục đích chính: gợi ra lý do cho sức hút bền bỉ của chuỗi sonnet bất chấp hình thức khó → Chọn D.',
            'Đọc mệnh đề chính sau “Although...”: `recent poets have undertaken sonnet sequences, likely in part because...` → tóm đúng cấu trúc “enduring appeal... despite its challenging form”.',
            [
                ('Out of Scope', 'Đoạn không hề mô tả những cải tiến (innovations) cụ thể nào mà Brooks và Nelson đưa vào thể thơ.'),
                ('False Contrast', 'Không hề so sánh thơ của Brooks/Nelson “sáng tạo hơn” hay Shakespeare/Spenser “truyền thống hơn”.'),
                ('Incomplete / Wrong Focus', 'Không liệt kê (enumerate) hàng loạt đặc điểm cấu trúc — chỉ nhắc ngắn gọn 14 dòng và luật chặt để làm nền cho lý do thể thơ vẫn hấp dẫn.'),
                ('Đáp án đúng', 'Khớp hoàn toàn ý chính: gợi ý lý do chuỗi sonnet vẫn bền bỉ thu hút các nhà thơ bất chấp hình thức đầy thách thức.'),
            ],
        ),
        _q(
            'may2025_rw_m2l_q6', 6, 'Craft and Structure', 'Text Structure and Purpose', 'Medium',
            '<p>Can tomato plants grow on Mars? Can pea plants? <u>You might think the answer to these questions is obviously no</u>, but researchers in the Netherlands recently showed that the seeds of many common plant species can germinate in soil designed to simulate Martian conditions, as long as water is supplied. In fact, some species actually did <i>better</i> in Martian soil than in Earth soil: 90 percent of tomato seeds sprouted when planted in simulated Martian soil, compared with 66 percent that did when planted in soil from their home planet.</p>',
            'Which choice best describes the function of the underlined portion in the text as a whole?',
            [
                'It signals the surprising nature of the findings discussed in the text.',
                'It acknowledges that readers may object to the method used in the experiment discussed in the text.',
                'It clarifies a potential point of confusion about the hypothesis tested in the study discussed in the text.',
                'It draws a distinction between the two species discussed in the text.',
            ],
            'A',
            'Tác giả mở đầu bằng 2 câu hỏi rồi đặt giả định trực giác của người đọc (“You might think the answer to these questions is obviously no”) ngay trước chữ **but** dẫn tới phát hiện ngược hẳn trực giác (hạt giống không những nảy mầm được mà cà chua còn nảy mầm TỐT HƠN trong đất mô phỏng sao Hỏa: 90% vs. 66%) → Nhấn mạnh tính BẤT NGỜ của kết quả nghiên cứu → Chọn A.',
            'Cấu trúc tu từ “You might think X is obviously no, BUT actually Y!” luôn có chức năng làm nổi bật tính gây ngạc nhiên (“surprising nature”) của phát hiện.',
            [
                ('Đáp án đúng', 'Đặt trước kỳ vọng tự nhiên của người đọc (“obviously no”) để tôn lên sự bất ngờ của kết quả nghiên cứu phía sau chữ “but”.'),
                ('Fact Distortion', 'Không đề cập đến việc người đọc phản đối phương pháp thí nghiệm.'),
                ('Off-Point', 'Không giải thích điểm gây nhầm lẫn về giả thuyết nghiên cứu.'),
                ('Off-Point', '“these questions” gộp chung cả hai loài cây, không hề phân biệt cà chua với đậu Hà Lan.'),
            ],
        ),
        _q(
            'may2025_rw_m2l_q7', 7, 'Craft and Structure', 'Text Structure and Purpose', 'Hard',
            '<p>Julie Dash’s lyrical film <i>Daughters of the Dust</i>, first released in 1991, follows members of a Gullah family as they depart from their island home near Georgia in 1902. <u>Though an imaginative, critically acclaimed film with a wide release—and a highly appreciative global audience—Dash’s work never received the plaudits it deserved within the US film industry.</u> Interest in the film reignited, however, with Beyoncé’s release of <i>Lemonade</i> in 2016, due to the visual album’s numerous allusions to Dash’s film in the form of stylistic references to its scenes, costumes, and celebration of Black life in the US South.</p>',
            'Which choice best describes the function of the underlined portion in the text as a whole?',
            [
                'It gives a brief overview of how Dash’s film was received at the time of release and alludes to the reception of a similar work that is described later in the text.',
                'It expands on an attribute of Dash’s film that is described earlier in the text in order to draw distinctions between the film and a later work that was influenced by it.',
                'It presents a discrepancy between the value of Dash’s film and the industry’s response to it that the text goes on to demonstrate was partially rectified by the film’s influence on a later work.',
                'It introduces the implication that had Dash’s film received more recognition from the US film industry at the time of its release, it wouldn’t have attained such influence on Beyoncé’s <i>Lemonade</i>.',
            ],
            'C',
            'Đọc câu gạch chân trong quan hệ với câu cuối: Câu gạch chân nêu SỰ CHÊNH LỆCH / BẤT CÂN XỨNG (“discrepancy”) giữa giá trị nghệ thuật lớn lao của bộ phim (giàu trí tưởng tượng, được giới phê bình khen ngợi, khán giả toàn cầu trân trọng) với sự thiếu ghi nhận của ngành điện ảnh Mỹ (“never received the plaudits it deserved within the US film industry”). Câu tiếp theo (“Interest in the film reignited, however...”) cho thấy sự thiệt thòi đó được khắc phục phần nào nhờ ảnh hưởng lên album <i>Lemonade</i> của Beyoncé → Chọn C.',
            'Với câu Function “in the text as a whole”, luôn kiểm tra cả 2 nửa của đáp án: [Nửa 1: chức năng câu gạch chân] + [Nửa 2: cách phần còn lại của đoạn nối tiếp nó]!',
            [
                ('Half-True / False Tail', 'Câu gạch chân hoàn toàn không ám chỉ (“alludes to”) cách tiếp nhận của tác phẩm <i>Lemonade</i>.'),
                ('False Goal', 'Đoạn nhấn mạnh điểm ảnh hưởng/liên hệ (allusions, stylistic references) giữa hai tác phẩm chứ không phân biệt (draw distinctions) chúng.'),
                ('Đáp án đúng', 'Khớp trọn vẹn hai vế: nêu sự chênh lệch giữa giá trị phim và phản ứng của ngành điện ảnh Mỹ, rồi câu sau cho thấy điều đó phần nào được bù đắp nhờ ảnh hưởng tới <i>Lemonade</i>.'),
                ('Unsupported Speculation', 'Đoạn không hề ngụ ý rằng nếu phim được công nhận sớm hơn thì đã không ảnh hưởng tới <i>Lemonade</i>.'),
            ],
        ),
        _q(
            'may2025_rw_m2l_q8', 8, 'Information and Ideas', 'Central Ideas and Details', 'Easy',
            '<p>Sometimes an animal will encounter another member of its own species that it doesn’t have any connection with. (For example, African lions that aren’t in the same pride might meet.) When that happens, the animals have to make decisions. Will they compete for a mate? Will they help in a fight with a predator? Will there be another outcome? In other words, the animals have to think carefully about possible risks and benefits.</p>',
            'What is the main topic of the text?',
            [
                'Animal species that do not have any predators',
                'A kind of meeting between animals of the same species',
                'Animal species that are close to becoming extinct',
                'Different environments that some animal species live in',
            ],
            'B',
            'Câu mở đầu nêu thẳng chủ đề: đôi khi một cá thể động vật chạm trán một cá thể cùng loài mà nó không có mối liên hệ nào (“encounter another member of its own species”), và cả đoạn phân tích những quyết định cân nhắc rủi ro – lợi ích xảy ra trong kiểu cuộc gặp gỡ đó → Chọn B.',
            'Đọc câu 1 và từ đại diện xuyên suốt đoạn (“When that happens...”) để chốt đúng chủ đề trung tâm.',
            [
                ('Out of Scope', 'Bài nhắc việc chiến đấu với kẻ săn mồi (“predator”), không nói về loài không có kẻ săn mồi.'),
                ('Đáp án đúng', 'Tóm gọn chính xác chủ đề trung tâm: một kiểu chạm trán giữa các cá thể động vật cùng loài.'),
                ('Out of Scope', 'Không hề đề cập đến các loài có nguy cơ tuyệt chủng.'),
                ('Out of Scope', 'Không thảo luận các môi trường sống khác nhau.'),
            ],
        ),
        _q(
            'may2025_rw_m2l_q9', 9, 'Information and Ideas', 'Command of Evidence (Quantitative)', 'Easy',
            _html_table(
                'Millions of Metric Tons of Copper Mined in 1995 and 2020',
                ['Country', '1995', '2020'],
                [
                    ['<b>United States</b>', '1.85', '1.20'],
                    ['<b>Chile</b>', '2.49', '5.73'],
                    ['<b>Zambia</b>', '0.33', '0.85'],
                    ['<b>Indonesia</b>', '0.44', '0.51'],
                ],
            ) + '<p>A student is researching changes in copper mining from 1995 to 2020. The student learns that most copper-mining countries mined more in 2020 than in 1995, but some did not. For example, one country that produced less copper through mining in 2020 than in 1995 is _______</p>',
            'Which choice most effectively uses data from the table to complete the example?',
            ['the United States.', 'Zambia.', 'Chile.', 'Indonesia.'],
            'A',
            'So sánh cột 2020 với cột 1995 của từng quốc gia: United States giảm từ 1.85 xuống 1.20 triệu tấn; Chile tăng (2.49 → 5.73); Zambia tăng (0.33 → 0.85); Indonesia tăng (0.44 → 0.51). Duy nhất Hoa Kỳ (the United States) khai thác ÍT đồng hơn vào năm 2020 so với năm 1995 → Chọn A.',
            'So sánh trực tiếp từng hàng giữa cột 1995 và cột 2020 để tìm duy nhất quốc gia có số liệu năm 2020 < năm 1995.',
            [
                ('Đáp án đúng', 'Hoa Kỳ giảm sản lượng khai thác đồng từ 1.85 triệu tấn (1995) xuống 1.20 triệu tấn (2020).'),
                ('Reversed Comparison', 'Zambia tăng từ 0.33 lên 0.85 triệu tấn.'),
                ('Reversed Comparison', 'Chile tăng mạnh từ 2.49 lên 5.73 triệu tấn.'),
                ('Reversed Comparison', 'Indonesia tăng từ 0.44 lên 0.51 triệu tấn.'),
            ],
        ),
        _q(
            'may2025_rw_m2l_q10', 10, 'Information and Ideas', 'Command of Evidence (Quantitative)', 'Easy',
            _html_table(
                'Examples of Hoards found in Ireland and Northern Ireland',
                ['Hoard name', 'Date of contents', 'Year of discovery', 'Description'],
                [
                    ['<b>Coleraine Hoard</b>', '5th century CE', '1854', 'silver pieces'],
                    ['<b>Derrynaflan Hoard</b>', '10th century CE', '1980', 'silver and bronze pieces'],
                    ['<b>Dooyork Hoard</b>', '3rd century BCE–2nd century CE', '2001', 'gold, bronze, and beads'],
                ],
            ) + '<p>Deposits of valuable objects, called hoards, have been unearthed in many different parts of Ireland and Northern Ireland. Technological advancements in the twenty-first century have made it easier to locate hoards, but plenty of hoards were found earlier. For example, _______</p>',
            'Which choice most effectively uses data from the table to complete the statement?',
            [
                'the Derrynaflan Hoard was found in 1854.',
                'the Coleraine Hoard, Derrynaflan Hoard, and Dooyork Hoard have all been found since 1854.',
                'the Coleraine Hoard and Derrynaflan Hoard were both found before 2000.',
                'Derrynaflan Hoard and Dooyork Hoard were both discovered in the 1900s.',
            ],
            'C',
            'Luận điểm cần minh họa: nhiều kho báu đã được phát hiện TRƯỚC thế kỷ 21 (“plenty of hoards were found earlier”). Tra cột “Year of discovery”: Coleraine Hoard (1854) và Derrynaflan Hoard (1980) đều được tìm thấy trước năm 2000 → Chọn C.',
            'Kiểm tra chính xác cả hai điều kiện: ĐÚNG dữ liệu trong cột “Year of discovery” VÀ minh họa đúng ý “tìm thấy trước thế kỷ 21”.',
            [
                ('False Data', 'Sai hàng bảng: Derrynaflan Hoard được phát hiện năm 1980 (Coleraine Hoard mới là năm 1854).'),
                ('True Data / Wrong Claim', 'Bao gồm cả Dooyork Hoard (2001) và chỉ nói “từ năm 1854 trở lại đây” nên không chứng minh được việc phát hiện trước thế kỷ 21.'),
                ('Đáp án đúng', 'Khớp chuẩn bảng (1854 và 1980 đều trước năm 2000) và chứng minh trực tiếp các kho báu được tìm thấy trước thế kỷ 21.'),
                ('False Data', 'Sai dữ liệu: Dooyork Hoard được tìm thấy năm 2001 (không phải thập niên/thế kỷ 1900s).'),
            ],
        ),
        _q(
            'may2025_rw_m2l_q11', 11, 'Information and Ideas', 'Command of Evidence (Textual)', 'Easy',
            '<p>A student is writing a paper about classical composer Florence Beatrice Price for a music class. In the paper, the student claims that <u>Price used African instruments in one of her compositions.</u></p>',
            'Which quotation from a work by a music historian would most directly support the underlined claim?',
            [
                '“After moving to Chicago in 1927, Price continued her music studies.”',
                '“In 2009, dozens of Price’s compositions, including her Symphony no. 4, were found in an abandoned house outside of St. Anne, Illinois.”',
                '“In her composition Symphony no. 1, Price included African drums.”',
                '“Price’s success as a composer was notable in part because before her, no African American woman had had a work performed by a major US orchestra.”',
            ],
            'C',
            'Luận điểm gạch chân: Price đã sử dụng NHẠC CỤ CHÂU PHI trong một tác phẩm của bà (“used African instruments in one of her compositions”). Trích dẫn C xác nhận trực tiếp: trong bản Giao hưởng số 1 (<i>Symphony no. 1</i>), Price đã đưa trống châu Phi (“African drums”) vào tác phẩm → Chọn C.',
            'Ánh xạ trực tiếp “African instruments” → “African drums” và “one of her compositions” → “Symphony no. 1”.',
            [
                ('Off-Point', 'Chỉ kể việc Price tiếp tục học âm nhạc tại Chicago năm 1927.'),
                ('Off-Point', 'Chỉ kể sự kiện phát hiện bản thảo các tác phẩm của bà năm 2009.'),
                ('Đáp án đúng', 'Bằng chứng trực tiếp 100%: trong tác phẩm <i>Symphony no. 1</i>, Price đã sử dụng trống châu Phi (một nhạc cụ châu Phi).'),
                ('Off-Point', 'Nói về cột mốc lịch sử được dàn nhạc lớn của Mỹ trình diễn, không đề cập nhạc cụ châu Phi.'),
            ],
        ),
        _q(
            'may2025_rw_m2l_q12', 12, 'Information and Ideas', 'Command of Evidence (Textual)', 'Medium',
            '<p>“The Monster” is an 1898 story by Stephen Crane. In the story, the character of Jim, a young boy, is playing in his yard while his father mows the lawn; while Jim is pulling a cart behind him, he accidentally damages a peony (a flower). Crane depicts Jim’s initial belief that the damage might be repaired or concealed: _______</p>',
            'Which quotation from “The Monster” most effectively illustrates the claim?',
            [
                '“Finally [Jim] went to the peony and tried to stand it on its pins, resuscitated, but the spine of it was hurt, and it could only hang limply from his hand.”',
                '“Together [Jim and his father] crossed the lawn towards the flower-bed. At some yards from the broken peony Jimmie began to lag. ‘There!’ The word came [from Jim] almost breathlessly.”',
                '“Little Jim was, for the time, engine Number 36, and he was making the run between Syracuse and Rochester. He was fourteen minutes behind time, and the throttle was wide open.”',
                '“[Jim’s father] had his back to the accident, and he continued to pace slowly to and fro, pushing the mower.”',
            ],
            'A',
            'Luận điểm cần minh họa: Crane khắc họa niềm tin ban đầu của cậu bé Jim rằng bông hoa mẫu đơn bị hỏng có thể được SỬA LẠI HOẶC CHE GIẤU (“repaired or concealed”). Trong A, Jim tiến tới bông hoa và “cố dựng nó đứng thẳng lại như hồi sinh” (“tried to stand it on its pins, resuscitated”) — hành động chứng tỏ ban đầu cậu tin mình có thể sửa cho bông hoa đứng lại bình thường → Chọn A.',
            'Tìm đúng trích dẫn có hành động cố khắc phục hư hại (“tried to stand it on its pins, resuscitated”) thay vì lúc cậu thú nhận (B) hay lúc trước tai nạn (C).',
            [
                ('Đáp án đúng', 'Hành động cố dựng bông mẫu đơn đứng thẳng lại như cũ (“tried to stand it on its pins, resuscitated”) minh họa rõ niềm tin ban đầu của Jim rằng có thể sửa/giấu vết hỏng.'),
                ('Wrong Moment', 'Mô tả cảnh Jim dẫn bố ra chỉ chỗ bông hoa gãy với vẻ lo lắng — không phải nỗ lực sửa hay che giấu.'),
                ('Wrong Moment', 'Mô tả trò chơi đóng giả đầu máy xe lửa của Jim trước khi nhận ra bông hoa bị hỏng.'),
                ('Wrong Subject', 'Chỉ mô tả người bố đang quay lưng đẩy máy cắt cỏ, không cho thấy suy nghĩ hay hành động của Jim.'),
            ],
        ),
        _q(
            'may2025_rw_m2l_q13', 13, 'Information and Ideas', 'Command of Evidence (Textual)', 'Medium',
            '<p>“‘No, Thank You, John’” is an 1862 poem by Christina Rossetti. In the poem, Rossetti depicts a female speaker’s rejection of the romantic advances of a man named John. The speaker encourages John to pursue another relationship rather than wait for her to change her mind, saying _______</p>',
            'Which quotation from “‘No, Thank You, John’” most effectively illustrates the claim?',
            [
                '“I never said I loved you, John: / Why will you teaze me day by day, / And wax a weariness to think upon / With always ‘do’ and ‘pray’?”',
                '“I dare say Meg or Moll would take / Pity upon you, if you’d ask. / And pray don’t remain single for my sake / Who can’t perform that task.”',
                '“Here’s friendship for you if you like; but love— / No, thank you, John.”',
                '“Let’s strike hands as hearty friends; / No more, no less; and friendship’s good: / Only don’t keep in view ulterior ends / and points not understood.”',
            ],
            'B',
            'Checklist 2 ý của luận điểm: [1] Khuyên John theo đuổi MỐI QUAN HỆ KHÁC (“pursue another relationship”) + [2] thay vì chờ cô đổi ý (“rather than wait for her to change her mind”). Câu B khớp cả hai ý từng chữ một: gợi ý John hỏi cưới Meg hoặc Moll (“Meg or Moll would take / Pity upon you, if you’d ask”) và khuyên anh đừng ở độc thân vì cô (“pray don’t remain single for my sake / Who can’t perform that task”) → Chọn B.',
            'Phân biệt giữa “từ chối/đề nghị làm bạn” (A, C, D) với “khuyên đi tìm người yêu khác đừng chờ mình” (B)!',
            [
                ('Incomplete / Off-Point', 'Chỉ trách móc John đeo bám dai dẳng, không khuyên anh tìm mối quan hệ khác.'),
                ('Đáp án đúng', 'Gợi ý đích danh Meg hoặc Moll và khuyên John đừng ở độc thân chờ cô vì cô không thể đáp lại tình yêu.'),
                ('Off-Point', 'Chỉ từ chối tình yêu và đề nghị tình bạn, không khuyên John theo đuổi người khác.'),
                ('Off-Point', 'Chỉ đề nghị làm bạn chân thành không có ẩn ý, không nhắc việc tìm mối quan hệ mới.'),
            ],
        ),
        _q(
            'may2025_rw_m2l_q14', 14, 'Information and Ideas', 'Command of Evidence (Textual)', 'Medium',
            '<p>A student is writing an essay on the subject of cultured meat, which is grown in a laboratory and is intended to help reduce the number of livestock harvested for food. The student wants to make the case that cultured meat production may be useful in responding to an expected widespread change in the public’s behavior.</p>',
            'Which quotation from a publication by a researcher would most effectively support the student’s claim?',
            [
                '“Researchers who advocate for the development of lab-grown meat claim that it’s better for the environment than conventional meat because it requires less water consumption.”',
                '“The flavor of meat from livestock differs across species (from pig to chicken to cow), and is also influenced by farming conditions and the breeds and genders of animals.”',
                '“A growing population that is including significantly more meat in its diet will contribute to an increasing demand for meat products in the 21st century.”',
                '“Consumers tend to believe that using less packaging when selling meat products in stores would have a significant effect on the environment.”',
            ],
            'C',
            'Khóa đúng cụm mục tiêu: ứng phó với “một sự thay đổi rộng khắp được dự báo trong hành vi của công chúng” (“an expected widespread change in the public’s behavior”). Trích dẫn C chỉ rõ sự thay đổi hành vi tiêu dùng diện rộng được dự báo trong thế kỷ 21: dân số tăng lên và đưa thêm nhiều thịt hơn hẳn vào chế độ ăn, làm tăng mạnh nhu cầu tiêu thụ thịt → Chọn C.',
            'Đừng chọn bẫy A chỉ vì có từ khóa “lab-grown meat” — A nói về lợi ích tiết kiệm nước chứ không nói về thay đổi hành vi của công chúng!',
            [
                ('Topic Keyword Lure', 'Nhắc thịt nuôi cấy ít tốn nước hơn, nhưng không đề cập sự thay đổi hành vi của công chúng.'),
                ('Irrelevant Detail', 'Nói về các yếu tố tạo nên hương vị thịt gia súc.'),
                ('Đáp án đúng', 'Chứng minh trực tiếp xu hướng thay đổi hành vi ăn uống rộng khắp (ăn nhiều thịt hơn hẳn) làm tăng nhu cầu thịt trong thế kỷ 21.'),
                ('Off-Point', 'Chỉ nói về quan điểm của người tiêu dùng đối với bao bì đóng gói.'),
            ],
        ),
        _q(
            'may2025_rw_m2l_q15', 15, 'Information and Ideas', 'Inferences', 'Easy',
            '<p>Archaeologists have traditionally thought that many cities in ancient Mesopotamia, including Uruk and Ur, lay on the extremely dry banks of the Tigris and Euphrates rivers. Jennifer Pournelle and her team found evidence that the land these ancient cities sat on consisted of marshy wetlands. This finding suggests that _______</p>',
            'Which choice most logically completes the text?',
            [
                'Uruk was founded at an earlier time than Ur was.',
                'far fewer fish species are found in rivers today than in ancient times.',
                'the land many ancient Mesopotamian cities sat on wasn’t as dry as previously believed.',
                'people in Ur engaged in trade with people from many parts of ancient Mesopotamia.',
            ],
            'C',
            'Đối chiếu 2 câu: Trước đây khảo cổ học tin rằng đất nền các thành phố Lưỡng Hà cổ nằm trên bờ sông “cực kỳ khô cằn” (“extremely dry”). Nhóm của Jennifer Pournelle lại tìm thấy bằng chứng vùng đất đó thực chất là “đầm lầy ẩm ướt” (“marshy wetlands”) → Kết luận trực tiếp: vùng đất ấy không khô cằn như người ta từng nghĩ → Chọn C.',
            'Suy luận sát mặt văn bản (zero extrapolation): đối lập trực tiếp “traditionally thought... extremely dry” với “marshy wetlands”.',
            [
                ('Out of Scope', 'Đoạn không so sánh thời điểm thành lập giữa Uruk và Ur.'),
                ('Out of Scope', 'Không hề nhắc tới loài cá trong sông xưa hay nay.'),
                ('Đáp án đúng', 'Suy luận trực tiếp từ bằng chứng đầm lầy: đất nền các thành phố Lưỡng Hà cổ không khô cằn như quan niệm trước đây.'),
                ('Out of Scope', 'Không đề cập hoạt động thương mại của cư dân Ur.'),
            ],
        ),
        _q(
            'may2025_rw_m2l_q16', 16, 'Information and Ideas', 'Inferences', 'Hard',
            '<p>Like many other fruit-eating birds on the Hawaiian island of Oahu, the northern cardinal helps forest plants spread by carrying seeds from the plants’ fruits to different locations (a process called seed dispersal). Ecologists have found that fruit-eating birds disperse some seeds from plants native to Oahu that are at risk of extinction in the wild, such as the kawau tree, but disperse many more seeds from soapbush shrubs, night-blooming jessamine shrubs, and other non-native plants that are already widespread. Believing that the great availability of fruit from non-native plants might be making birds less likely to eat fruit from native plants, the ecologists conclude that _______</p>',
            'Which choice most logically completes the text?',
            [
                'the kawau tree, the soapbush shrub, and the night-blooming jessamine shrub are the plant species on Oahu most in danger of going extinct in the wild.',
                'vulnerable native plants would probably benefit if the populations of non-native plants, such as the soapbush shrub and night-blooming jessamine shrub, were reduced.',
                'the northern cardinal and other fruit-eating birds on Oahu would likely favor fruits from native forest plants if native and non-native plants were equally widespread.',
                'roughly equal numbers of seeds from native and non-native plants would be dispersed if the populations of fruit-eating birds, such as the northern cardinal, increased.',
            ],
            'B',
            'Mạch suy luận của các nhà sinh thái học: [1] Chim ăn quả giúp phát tán hạt cho cây bản địa đang nguy cấp (cây kawau), nhưng hiện phát tán nhiều hạt cây ngoại lai hơn hẳn; [2] Nguyên nhân nghi ngờ: lượng quả quá dồi dào từ cây ngoại lai (“great availability of fruit from non-native plants”) khiến chim ít ăn quả cây bản địa hơn → Suy ra hệ quả logic: nếu GIẢM quần thể cây ngoại lai (soapbush, night-blooming jessamine), chim sẽ ăn và phát tán nhiều hạt cây bản địa hơn, nhờ đó các loài thực vật bản địa dễ tổn thương sẽ có lợi → Chọn B.',
            'Kiểm tra độ chặt chẽ của suy luận: C bịa thêm giả định chim “ưa thích hơn” (favor) quả bản địa nếu mật độ ngang nhau — bài KHÔNG hề nói chim thích vị quả bản địa hơn!',
            [
                ('Contradiction', 'Sai hoàn toàn: soapbush và night-blooming jessamine là cây NGOẠI LAI đang lan rộng (“already widespread”), không phải loài sắp tuyệt chủng.'),
                ('Đáp án đúng', 'Suy luận trực tiếp từ nguyên nhân “quá nhiều quả ngoại lai làm chim ít ăn quả bản địa”: giảm bớt cây ngoại lai sẽ giúp các loài bản địa nguy cấp hưởng lợi.'),
                ('Unsupported Assumption', 'Bài chỉ nói sự dồi dào của quả ngoại lai làm giảm khả năng chim ăn quả bản địa, KHÔNG chứng minh chim sẽ ưu tiên quả bản địa hơn nếu mật độ hai nhóm bằng nhau.'),
                ('Illogical Inference', 'Tăng số lượng chim khi cây ngoại lai vẫn áp đảo sẽ vẫn khiến hạt cây ngoại lai được phát tán nhiều hơn nhiều chứ không bằng nhau.'),
            ],
        ),
        _q(
            'may2025_rw_m2l_q17', 17, 'Standard English Conventions', 'Form, Structure, and Sense', 'Easy',
            '<p>We came to see the famous artworks inside the Museo Soumaya in Mexico City, yet the building itself _______ us the most. The building, we later learned, had been designed by Mexican architect Fernando Romero in 2011.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['to impress', 'having impressed', 'impressed', 'impressing'],
            'C',
            'Sau liên từ kết hợp “, yet” là mệnh đề độc lập thứ hai có chủ ngữ “the building itself” → BẮT BUỘC cần một ĐỘNG TỪ CHIA THÌ (finite verb) hòa hợp thì quá khứ đơn với vế trước (“We came...”) và câu sau (“we later learned”) → **impressed** → Chọn C.',
            'Ba đáp án A (`to impress`), B (`having impressed`), D (`impressing`) đều là dạng động từ không chia thì (non-finite) — chỉ C là động từ chia thì hoàn chỉnh cho mệnh đề!',
            [
                ('Fragment (Non-Finite)', '“to impress” là động từ nguyên mẫu, không thể làm động từ chính của mệnh đề.'),
                ('Fragment (Non-Finite)', '“having impressed” là cụm phân từ, khiến mệnh đề sau “yet” thiếu động từ chính.'),
                ('Đáp án đúng', '“impressed” là động từ chia thì quá khứ đơn, hoàn thành mệnh đề độc lập thứ hai và khớp thì với “came”.'),
                ('Fragment (Non-Finite)', '“impressing” là phân từ hiện tại, thiếu trợ động từ để làm vị ngữ chính.'),
            ],
        ),
        _q(
            'may2025_rw_m2l_q18', 18, 'Standard English Conventions', 'Form, Structure, and Sense', 'Easy',
            '<p>Alicia Pérez-Porro, whose research focuses mainly on sea sponges, _______ as a biologist at the Smithsonian Institution.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['work', 'works', 'are working', 'have worked'],
            'B',
            'Hòa hợp chủ ngữ – động từ (Subject-Verb Agreement): Gạch bỏ mệnh đề quan hệ phụ giữa 2 dấu phẩy “, whose research focuses mainly on sea sponges,” → Chủ ngữ chính là một người **Alicia Pérez-Porro** (ngôi 3 số ít) → Chỉ duy nhất **works** là động từ chia số ít → Chọn B.',
            'Mẹo 3 giây: 3 phương án số nhiều (`work`, `are working`, `have worked`) vs. 1 phương án số ít (`works`) — nhìn thấy chủ ngữ số ít chốt ngay B!',
            [
                ('Subject-Verb Disagreement', '“work” là dạng số nhiều, không khớp với chủ ngữ số ít “Alicia Pérez-Porro”.'),
                ('Đáp án đúng', '“works” là động từ hiện tại đơn số ít, khớp chính xác với chủ ngữ “Alicia Pérez-Porro” và thì hiện tại của câu.'),
                ('Subject-Verb Disagreement', '“are working” là số nhiều, sai hòa hợp với chủ ngữ một người.'),
                ('Subject-Verb Disagreement', '“have worked” là số nhiều, không khớp với chủ ngữ số ít.'),
            ],
        ),
        _q(
            'may2025_rw_m2l_q19', 19, 'Standard English Conventions', 'Boundaries', 'Easy',
            '<p>In 2012, Ken Liu’s hard work paid off. Before an audience _______ fantasy writers from around the world, Liu’s “The Paper Menagerie” received the World Fantasy Award, one of the most prestigious honors in fantasy literature, for Best Short Fiction.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['of', 'of:', 'of,', 'of;'],
            'A',
            'Quy tắc Giới từ + Tân ngữ (Preposition + Object): Giới từ “of” kết nối trực tiếp với cụm danh từ tân ngữ “fantasy writers from around the world” tạo thành cụm “an audience of fantasy writers from around the world”. KHÔNG ĐƯỢC đặt bất kỳ dấu câu nào (hai chấm, phẩy, chấm phẩy) chen giữa giới từ và tân ngữ của nó → Chọn A.',
            'Không bao giờ ngăn cách giới từ (“of”, “in”, “by”, “for”...) với cụm danh từ đứng ngay sau nó bằng dấu câu!',
            [
                ('Đáp án đúng', 'Không dùng dấu câu — giữ liền mạch cụm giới từ “an audience of fantasy writers from around the world”.'),
                ('Preposition Split', 'Dấu hai chấm sai hoàn toàn khi đứng sau giới từ “of” và trước khi kết thúc mệnh đề độc lập.'),
                ('Preposition Split', 'Dấu phẩy cắt rời giới từ “of” khỏi tân ngữ “fantasy writers”.'),
                ('Preposition Split', 'Dấu chấm phẩy chỉ nối hai mệnh đề độc lập, tuyệt đối không đặt ngay sau giới từ “of”.'),
            ],
        ),
        _q(
            'may2025_rw_m2l_q20', 20, 'Standard English Conventions', 'Form, Structure, and Sense', 'Easy',
            '<p>On the 2021 “100 Best Jobs” list published by <i>U.S. News &amp; World Report</i>, lawyers, ranked thirty-eighth, were projected _______ an impressive 32,300 new jobs between 2019 and 2029. In contrast, the projection for optometrists was 1,900.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['are gaining', 'to gain', 'had gained', 'gains'],
            'B',
            'Cấu trúc bị động chuẩn trong tiếng Anh: `be projected + to V` (được dự báo sẽ làm gì) → “lawyers... were projected **to gain** an impressive 32,300 new jobs”. Ba đáp án còn lại đều là động từ chia thì (finite verbs) gây xung đột trực tiếp với vị ngữ “were projected” → Chọn B.',
            'Khi câu đã có động từ chia thì ở thể bị động (`were projected / expected / estimated`), theo sau là động từ nguyên mẫu có “to” (`to gain`), không chia thêm động từ thứ hai!',
            [
                ('Double Finite Verb', '“are gaining” là động từ chia thì, không thể đứng ngay sau “were projected”.'),
                ('Đáp án đúng', 'Cấu trúc chuẩn “be projected to + V”: “were projected to gain”.'),
                ('Double Finite Verb', '“had gained” là động từ chia thì quá khứ hoàn thành, sai cấu trúc sau “were projected”.'),
                ('Double Finite Verb', '“gains” là động từ chia thì số ít, sai cả cấu trúc lẫn số nhiều.'),
            ],
        ),
        _q(
            'may2025_rw_m2l_q21', 21, 'Standard English Conventions', 'Form, Structure, and Sense', 'Easy',
            '<p>As an object-oriented computer programming language, Java is used by coders like Black Girls Code founder Kimberly Bryant _______ programs by manipulating “objects” (that is, specifically defined variables or combinations of variables) into interacting with each other. Conversely, S-Lang, used in software development and scripting, is not an object-oriented language.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['created', 'create', 'is creating', 'to create'],
            'D',
            'Cấu trúc chỉ mục đích đi với bị động: `Java is used by [coders...] to [do something]` (Java được các lập trình viên sử dụng ĐỂ tạo ra các chương trình) → cần động từ nguyên mẫu chỉ mục đích **to create** → Chọn D.',
            'Động từ chính của câu đã là “is used” → phần chỉ mục đích phía sau phải dùng `to + V` (“to create”), loại mọi động từ chia thì!',
            [
                ('Wrong Verb Form', '“created” không thể diễn đạt mục đích sau “is used by coders...”.'),
                ('Wrong Verb Form', '“create” (nguyên mẫu không “to” / chia thì) sai ngữ pháp sau “is used by coders...”.'),
                ('Double Finite Verb', '“is creating” là động từ chia thì, tạo lỗi hai vị ngữ chính trong cùng một mệnh đề.'),
                ('Đáp án đúng', '“to create” là động từ nguyên mẫu chỉ mục đích khớp chuẩn với cấu trúc “is used by ... to V”.'),
            ],
        ),
        _q(
            'may2025_rw_m2l_q22', 22, 'Expression of Ideas', 'Transitions', 'Easy',
            '<p>Modernist architect Adolf Loos argued that buildings shouldn’t have ornaments, such as elaborate carvings, because such ornaments don’t have a meaningful purpose. Post-modernist architect Denise Brown argued that ornaments can serve a purpose. _______ they can communicate useful information about a city’s history and culture.</p>',
            'Which choice completes the text with the most logical transition?',
            ['However,', 'As a result,', 'For instance,', 'Finally,'],
            'C',
            'Câu 2 nêu khẳng định khái quát của Denise Brown: chi tiết trang trí có thể phục vụ một mục đích (“can serve a purpose”). Câu 3 đưa ra một VÍ DỤ CỤ THỂ cho mục đích đó: chúng có thể truyền tải thông tin hữu ích về lịch sử và văn hóa của thành phố → “For instance,” (Ví dụ) → Chọn C.',
            'Mô hình `[Nhận định chung: can serve a purpose] → [Một mục đích cụ thể minh họa]` → chọn ngay từ nối nêu ví dụ “For instance,” / “For example,”.',
            [
                ('False Contrast', 'However = Tuy nhiên — câu 3 hoàn toàn ủng hộ và minh họa câu 2, không hề tương phản.'),
                ('False Cause', 'As a result = Kết quả là — việc truyền tải thông tin văn hóa là một ví dụ của “serve a purpose”, không phải hệ quả của việc Brown tranh luận.'),
                ('Đáp án đúng', 'For instance = Chẳng hạn / Ví dụ — nêu ví dụ cụ thể cho mục đích mà các chi tiết trang trí có thể đảm nhiệm.'),
                ('Wrong Sequence', 'Finally = Cuối cùng — không có danh sách các bước/luận điểm theo thứ tự trước đó.'),
            ],
        ),
        _q(
            'may2025_rw_m2l_q23', 23, 'Expression of Ideas', 'Rhetorical Synthesis', 'Easy',
            '<p>While researching a topic, a student has taken the following notes:</p><ul><li>Michael López-Alegría is a US astronaut.</li><li>López-Alegría was the commander of Expedition 14.</li><li>It was the fourteenth expedition to the International Space Station (ISS).</li><li>It began on September 18, 2006.</li><li>It ended on April 21, 2007.</li></ul>',
            'The student wants to indicate what López-Alegría’s role was on Expedition 14. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
            [
                'Expedition 14 was the fourteenth expedition to the ISS.',
                'Expedition 14 began on September 18, 2006, and ended on April 21, 2007.',
                'López-Alegría, a US astronaut, was the commander of Expedition 14.',
                'In 2006, López-Alegría traveled to the ISS.',
            ],
            'C',
            'Mục tiêu (Goal): Cho biết VAI TRÒ (“role”) của López-Alegría trong sứ mệnh Expedition 14. Theo ghi chú thứ 2, ông là chỉ huy trưởng (“the commander of Expedition 14”). Duy nhất đáp án C nêu vai trò “commander” → Chọn C.',
            'Quét thẳng từ khóa chức danh/vai trò (“commander”) tương ứng với chữ “role” trong câu hỏi!',
            [
                ('Missing Role', 'Chỉ giải thích Expedition 14 là sứ mệnh thứ 14 tới ISS, không nhắc tới López-Alegría hay vai trò của ông.'),
                ('Missing Role', 'Chỉ nêu ngày bắt đầu và kết thúc sứ mệnh.'),
                ('Đáp án đúng', 'Nêu rõ vai trò của López-Alegría là chỉ huy trưởng (“the commander”) của Expedition 14.'),
                ('Missing Role', 'Chỉ nói năm 2006 ông bay lên ISS, không cho biết vai trò trên Expedition 14.'),
            ],
        ),
        _q(
            'may2025_rw_m2l_q24', 24, 'Expression of Ideas', 'Rhetorical Synthesis', 'Easy',
            '<p>While researching a topic, a student has taken the following notes:</p><ul><li>Blackberries are commonly considered fruits because they taste sweet.</li><li>In botany, blackberries are classified as fruits.</li><li>Tomatoes are commonly considered vegetables because they taste savory.</li><li>In botany, tomatoes are classified as fruits.</li></ul>',
            'The student wants to emphasize the botanical classification of tomatoes. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
            [
                'In addition to tasting sweet, blackberries are botanically classified as fruits.',
                'Although commonly considered vegetables, tomatoes are botanically classified as fruits.',
                'Tomatoes taste savory, but blackberries taste sweet.',
                'Blackberries, which are botanically classified as fruits, taste sweet and thus are commonly considered fruits.',
            ],
            'B',
            'Mục tiêu (Goal): Nhấn mạnh PHÂN LOẠI THỰC VẬT HỌC CỦA CÀ CHUA (“the botanical classification of tomatoes”). A và D nói về quả mâm xôi (blackberries); C chỉ so sánh vị giác. Duy nhất B đặt trọng tâm vào cà chua và phân loại thực vật học của nó (“tomatoes are botanically classified as fruits”) → Chọn B.',
            'Khóa 2 từ khóa bắt buộc của Goal: `botanical classification` + `tomatoes` → loại A, C, D trong tích tắc.',
            [
                ('Wrong Subject', 'Nói về quả mâm xôi đen (blackberries) thay vì cà chua (tomatoes).'),
                ('Đáp án đúng', 'Dùng mệnh đề nhượng bộ “Although...” để làm nổi bật phân loại thực vật học của cà chua là trái cây (“botanically classified as fruits”).'),
                ('Missing Classification', 'Chỉ so sánh mùi vị của cà chua và mâm xôi, không nhắc phân loại thực vật học.'),
                ('Wrong Subject', 'Chỉ nói về quả mâm xôi đen, không nhắc cà chua.'),
            ],
        ),
        _q(
            'may2025_rw_m2l_q25', 25, 'Expression of Ideas', 'Rhetorical Synthesis', 'Medium',
            '<ul><li>Jean-Michel Basquiat was an American artist who produced more than two thousand drawings and paintings.</li><li>His work <i>Untitled (Pollo Frito)</i> was completed in 1982 and sold at auction in 2018 for $25.7 million.</li><li><i>Untitled (Pollo Frito)</i> is composed of acrylic, oil, and enamel on canvas and has an area of 7,230 square inches.</li><li>His work <i>Danny Rosen</i> was completed in 1983 and sold at auction in 2013 for $4.9 million.</li><li><i>Danny Rosen</i> is composed of acrylic, oil stick, and paper collage on canvas and has an area of 4,507 square inches.</li></ul>',
            'Which choice most effectively uses information from the given sentences to emphasize a difference between the two works?',
            [
                'Decades after Jean-Michel Basquiat completed <i>Untitled (Pollo Frito)</i> and <i>Danny Rosen</i>, the works were sold at auction.',
                '<i>Untitled (Pollo Frito)</i> (1982) and <i>Danny Rosen</i> (1983) are just two of the more than two thousand drawings and paintings produced by American artist Jean-Michel Basquiat.',
                '<i>Untitled (Pollo Frito)</i> and <i>Danny Rosen</i>, two works by artist Jean-Michel Basquiat, were completed in the same decade, but the former fetched a higher price at auction.',
                'Composed by artist Jean-Michel Basquiat in 1982 and 1983, respectively, both <i>Untitled (Pollo Frito)</i> and <i>Danny Rosen</i> use acrylic paint as a medium.',
            ],
            'C',
            'Mục tiêu (Goal): Nhấn mạnh MỘT ĐIỂM KHÁC BIỆT giữa hai tác phẩm (“emphasize a difference between the two works”). A, B và D đều chỉ nêu điểm GIỐNG NHAU (đều bán đấu giá sau nhiều thập kỷ; đều thuộc hơn 2.000 tác phẩm; đều dùng sơn acrylic). Duy nhất C nhấn mạnh sự khác biệt bằng từ nối “but”: tác phẩm đầu (25,7 triệu USD) đạt mức giá đấu giá cao hơn tác phẩm sau (4,9 triệu USD) → Chọn C.',
            'Hễ Goal yêu cầu “emphasize a difference”, tìm ngay cấu trúc đối lập (`but / whereas / while / higher than`) và kiểm chứng số liệu đúng với ghi chú ($25.7M > $4.9M)!',
            [
                ('Similarity Trap', 'Nhấn mạnh điểm giống nhau (cả hai đều được bán đấu giá sau nhiều thập kỷ) thay vì điểm khác biệt.'),
                ('Similarity Trap', 'Chỉ giới thiệu cả hai cùng là tác phẩm của Basquiat, không nêu điểm khác biệt.'),
                ('Đáp án đúng', 'Đối chiếu rõ ràng điểm khác biệt xác thực theo ghi chú: <i>Untitled (Pollo Frito)</i> bán được giá cao hơn ($25.7 triệu so với $4.9 triệu).'),
                ('Similarity Trap', 'Nhấn mạnh điểm tương đồng về chất liệu (“both... use acrylic paint”).'),
            ],
        ),
        _q(
            'may2025_rw_m2l_q26', 26, 'Expression of Ideas', 'Rhetorical Synthesis', 'Medium',
            '<p>While researching a topic, a student has taken the following notes:</p><ul><li>Ursula K. Le Guin was an acclaimed writer.</li><li>Le Guin’s first published work of fiction was a 1962 short story called “April in Paris.”</li><li>It is about an American professor living in Paris who travels through time.</li><li>This story showcases Le Guin’s nuanced portrayal of characters’ thoughts.</li><li>Le Guin’s nuanced portrayal of characters’ thoughts is a hallmark of her subsequent novels and stories.</li><li>Le Guin’s most famous novels include <i>A Wizard of Earthsea</i> (1968) and <i>The Left Hand of Darkness</i> (1969).</li></ul>',
            'The student wants to emphasize a stylistic similarity between Le Guin’s 1962 short story and some of her subsequent works. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
            [
                'Similar to Le Guin’s most famous novels, such as <i>A Wizard of Earthsea</i> (1968) and <i>The Left Hand of Darkness</i> (1969), the 1962 short story “April in Paris” is about an American professor living in Paris who travels through time.',
                '“April in Paris” (1962) showcases Le Guin’s nuanced portrayal of characters’ thoughts, a hallmark of later works such as <i>A Wizard of Earthsea</i> (1968) and <i>The Left Hand of Darkness</i> (1969).',
                'Both <i>A Wizard of Earthsea</i> (1968) and <i>The Left Hand of Darkness</i> (1969) are novels that showcase Le Guin’s nuanced portrayal of characters’ thoughts.',
                '“April in Paris” (1962) is a short story, and <i>A Wizard of Earthsea</i> (1968) and <i>The Left Hand of Darkness</i> (1969) are novels.',
            ],
            'B',
            'Mục tiêu (Goal): Nhấn mạnh SỰ TƯƠNG ĐỒNG VỀ PHONG CÁCH (“stylistic similarity”) giữa truyện ngắn năm 1962 (“April in Paris”) VÀ các tác phẩm sau này của Le Guin. Đáp án A mắc lỗi sai sự thật nghiêm trọng (bịa rằng hai cuốn tiểu thuyết kia cũng kể về vị giáo sư Mỹ du hành thời gian ở Paris!); C quên nhắc truyện ngắn năm 1962; D lại nêu sự khác biệt về thể loại. Chỉ B nêu chuẩn xác nét tương đồng phong cách (“nuanced portrayal of characters’ thoughts”) gắn kết cả “April in Paris” lẫn các tác phẩm sau đó → Chọn B.',
            'Cẩn thận bẫy A (“False Fact”): tuy có chữ “Similar to” nhưng gán sai cốt truyện của “April in Paris” cho các tiểu thuyết khác!',
            [
                ('False Fact', 'Sai sự thật so với ghi chú: chỉ “April in Paris” kể về giáo sư Mỹ ở Paris du hành thời gian, không phải <i>A Wizard of Earthsea</i> hay <i>The Left Hand of Darkness</i>.'),
                ('Đáp án đúng', 'Kết nối chính xác điểm tương đồng về phong cách (“nuanced portrayal of characters’ thoughts”) giữa truyện ngắn năm 1962 và các tiểu thuyết sau đó.'),
                ('Missing Subject', 'Bỏ quên hoàn toàn truyện ngắn năm 1962 (“April in Paris”).'),
                ('Difference Instead of Similarity', 'Chỉ nêu khác biệt về thể loại (truyện ngắn vs. tiểu thuyết), không nêu điểm tương đồng phong cách.'),
            ],
        ),
        _q(
            'may2025_rw_m2l_q27', 27, 'Expression of Ideas', 'Rhetorical Synthesis', 'Medium',
            '<p>While researching a topic, a student has taken the following notes:</p><ul><li>The Clovis First hypothesis proposes that ancient humans known as Clovis were the first to populate North America.</li><li>The Clovis arrived around 13,000 years ago.</li><li>They settled in various locations over a roughly 200-year period.</li><li>Stone tools found at the Sand Creek site in Texas date to approximately 16,540 years ago.</li><li>These items support the idea that humans were present in North America before the Clovis population arrived.</li><li>More than a dozen North American sites containing pre-Clovis items have been identified.</li></ul>',
            'The student wants to emphasize the number of sites containing pre-Clovis items. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
            [
                'After arriving in North America around 13,000 years ago, the Clovis, an ancient human population, settled in numerous locations over a roughly 200-year period.',
                'Far from being the only place where evidence of human activity predating Clovis has been found, the Sand Creek site in Texas is among more than a dozen such locations in North America.',
                'Dating to approximately 16,540 years old, the items found at Sand Creek, a site in Texas, predate the arrival of the Clovis population.',
                'North American sites where pre-Clovis items have been found include Sand Creek, a site in Texas.',
            ],
            'B',
            'Mục tiêu (Goal): Nhấn mạnh SỐ LƯỢNG ĐỊA ĐIỂM chứa hiện vật tiền-Clovis (“emphasize the number of sites containing pre-Clovis items”). Theo ghi chú cuối, đã xác định được “hơn một tá địa điểm” (“More than a dozen North American sites”). Duy nhất đáp án B nêu và nhấn mạnh số lượng này bằng cụm “Far from being the only place... is among more than a dozen such locations” → Chọn B.',
            'Bám sát từ khóa “the number of sites” trong Goal → tìm ngay cụm định lượng “more than a dozen”!',
            [
                ('Wrong Subject', 'Chỉ nói về các địa điểm định cư của người Clovis, không đề cập các địa điểm tiền-Clovis.'),
                ('Đáp án đúng', 'Nhấn mạnh nổi bật số lượng địa điểm tiền-Clovis (“Far from being the only place... more than a dozen such locations in North America”).'),
                ('Missing Number of Sites', 'Chỉ nói về niên đại ~16.540 năm của một địa điểm duy nhất (Sand Creek).'),
                ('Missing Number of Sites', 'Chỉ nêu ví dụ Sand Creek mà không cho biết tổng số lượng địa điểm là hơn một tá.'),
            ],
        ),
    ]


# ============================================================================
# FULL ADAPTIVE MOCK PAYLOAD (81 Qs: 27 M1 + 27 M2 Hard + 27 M2 Lower)
# ============================================================================

TEST_DATA = {
    'schemaVersion': 1,
    'mode': 'adaptive_mock',
    'section': 'rw',
    'basicInfo': {
        'title': TEST_TITLE,
        'subtitle': 'Đề thi thật Digital SAT tháng 5/2025 — Đủ 3 Module Adaptive (M1: 27 + M2 Easy: 27 + M2 Hard: 27)',
        'difficultyBadge': 'REAL EXAM • MAY 2025',
        'targetTimeMinutes': 64,
        'routingThreshold': 15,
    },
    'module1': {
        'id': 'may2025_rw_m1',
        'title': 'Section 1, Module 1: Reading and Writing',
        'subtitle': 'Routing Module (27 Questions • 32 Minutes)',
        'timeLimitMinutes': 32,
        'questions': get_m1_questions(),
    },
    'module2_hard': {
        'id': 'may2025_rw_m2h',
        'title': 'Section 1, Module 2: Reading and Writing (Hard Route)',
        'subtitle': 'Upper Adaptive Module (27 Questions • 32 Minutes)',
        'timeLimitMinutes': 32,
        'questions': get_m2_hard_questions(),
    },
    'module2_lower': {
        'id': 'may2025_rw_m2l',
        'title': 'Section 1, Module 2: Reading and Writing (Lower/Easy Route)',
        'subtitle': 'Lower Adaptive Module (27 Questions • 32 Minutes)',
        'timeLimitMinutes': 32,
        'questions': get_m2_lower_questions(),
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


def verify_all():
    """Runs full structural, fidelity, answer-consistency, and Bluebook pipeline checks."""
    try:
        from scripts.sat_real_exams_pipeline import validate_sat_bluebook_json
    except ImportError:
        sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
        from sat_real_exams_pipeline import validate_sat_bluebook_json

    errors = []
    seen_ids = set()
    total_qs = 0

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
        total_qs += len(qs)

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

            # Check for leftover PDF artifacts
            all_text = ' '.join([
                q.get('stimulusHtml', ''),
                q.get('questionHtml', ''),
                ' '.join(o.get('text', '') for o in q.get('options', [])),
            ])
            if '______blank' in all_text or 'blank' in re.findall(r'_{3,}blank', all_text):
                errors.append(f'{mod_key} Q{idx}: leftover ______blank artifact')
            if 'm i squared' in all_text or 'mi2m' in all_text:
                errors.append(f'{mod_key} Q{idx}: leftover mi2m i squared artifact')

    if total_qs != 81:
        errors.append(f'Total questions expected 81, got {total_qs}')

    pipeline_errs = validate_sat_bluebook_json(TEST_DATA, TEST_CODE)
    errors.extend(pipeline_errs)

    if errors:
        print(f'[FAIL] {TEST_CODE}: {len(errors)} error(s):')
        for e in errors:
            print('  -', e)
        sys.exit(1)

    print(f'[PASS] {TEST_CODE} — 0 errors!')
    print(f'       Title: {TEST_TITLE}')
    print(f'       Total questions: {total_qs} (unique IDs: {len(seen_ids)})')
    for mod_key in ('module1', 'module2_hard', 'module2_lower'):
        qs = TEST_DATA[mod_key]['questions']
        dist = {c: sum(1 for q in qs if q['correctAnswer'] == c) for c in 'ABCD'}
        doms = {}
        for q in qs:
            doms[q['domain']] = doms.get(q['domain'], 0) + 1
        print(f'       {mod_key:13s}: {len(qs)} Qs | Keys={dist} | Domains={doms}')


if __name__ == '__main__':
    verify_all()
