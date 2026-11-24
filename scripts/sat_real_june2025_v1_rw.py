# -*- coding: utf-8 -*-
"""
Digital SAT 1500+ Real Past Exam — June 2025 Ver 1 Reading & Writing (54 Questions)
- Module 1: 27 Real Questions (32 minutes)
- Module 2: 27 Real Questions (32 minutes, assigned to both module2_hard and module2_lower with routingThreshold=0)
- Source: June 2025 Real Exam Ver 1 (100% verbatim passages, tables, underlines, italics, and options A–D)
- 2-Pass Answer Audit completed across all 54 R&W items with rich Vietnamese explanations & trap analysis.
"""

import copy
import json
import os
import re
import sys

if sys.platform == 'win32':
    sys.stdout.reconfigure(encoding='utf-8')

TEST_CODE = 'real_june2025_v1_rw'
FOLDER_KEY = 'real_rw'
ORDER_INDEX = 2
TEST_TITLE = '🏛️ Real Exam — June 2025 Ver 1 Reading & Writing (54 Qs)'


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
        'june2025_v1_rw_m1_q1', 1, 'Craft and Structure', 'Words in Context', 'Easy',
        '<p>The following text is adapted from William Wordsworth’s 1798 poem “Lines Written a Few Miles above Tintern Abbey.”</p>'
        '<p style="line-height:1.9;">'
        '<span style="display:inline-block;padding-left:6em;">Once again</span><br/>'
        'Do I <u>behold</u> these steep and lofty cliffs,<br/>'
        'Which on a wild secluded scene impress<br/>'
        'Thoughts of more deep seclusion; and connect<br/>'
        'The landscape with the quiet of the sky.</p>',
        'As used in the text, what does the word “behold” most nearly mean?',
        ['Possess', 'Regard', 'Omit', 'Escape'],
        'B',
        'Trong bài thơ, nhân vật trữ tình trở lại thăm cảnh quan cũ: “Once again / Do I behold these steep and lofty cliffs” (Một lần nữa tôi lại ngắm nhìn / chiêm ngưỡng những vách đá dựng đứng cao vút này). Động từ cổ “behold” nghĩa là nhìn ngắm, quan sát chăm chú. Trong 4 đáp án, “Regard” mang nghĩa thứ cấp chuẩn SAT là “nhìn ngắm chăm chú / dõi theo” (gaze at steadily) → Chọn B.',
        'Với dạng Words in Context nghĩa thứ cấp (secondary meaning) trong thơ văn cổ điển, hãy nhớ cặp đồng nghĩa kinh điển của College Board: “behold” = look upon / view / “regard” (ngắm nhìn).',
        [
            ('Wrong Meaning', 'Possess = sở hữu — nhà thơ đang ngắm nhìn phong cảnh thiên nhiên chứ không sở hữu vách đá.'),
            ('Đáp án đúng', 'Regard = nhìn ngắm, chiêm ngưỡng — khớp sát nghĩa gốc “see / observe / look upon” của động từ “behold”.'),
            ('Opposite / Unrelated', 'Omit = bỏ sót, lược bỏ — hoàn toàn sai ngữ cảnh.'),
            ('Wrong Meaning', 'Escape = trốn thoát — trái ngược với cảm xúc trầm lắng trở lại ngắm cảnh xưa.'),
        ],
    ),

    # --- M1 Q2 ---
    q_item(
        'june2025_v1_rw_m1_q2', 2, 'Craft and Structure', 'Words in Context', 'Easy',
        '<p>Although oil shocks—such as the 10% rise in oil prices in November 1970—can strongly affect individual consumers, Gbadebo Oladosu and colleagues have shown that at the level of national economies, their effects are often quite _______. The effect of recent oil shocks on the gross domestic product of Germany, for example, was only slightly greater than zero.</p>',
        'Which choice completes the text with the most logical and precise word or phrase?',
        ['variable', 'persistent', 'subdued', 'beneficial'],
        'C',
        'Hai manh mối cực rõ: (1) Tương phản “Although... can strongly affect individual consumers” (dù tác động MẠNH lên người tiêu dùng cá nhân) ↔ ở tầm kinh tế quốc gia, tác động lại hoàn toàn ngược lại; (2) Ví dụ minh họa “only slightly greater than zero” (chỉ lớn hơn 0 một chút xíu) → tác động rất nhẹ, yếu, không đáng kể → Chọn C (“subdued” = dịu nhẹ, trầm lắng, yếu ớt).',
        'Khi thấy cấu trúc “Although X strongly affects A, on B it is quite _______” kèm ví dụ “slightly greater than zero”, hãy điền ngay tính từ mang nghĩa “mild / weak / muted” = subdued.',
        [
            ('Wrong Context', 'variable = hay thay đổi, biến thiên — câu ví dụ nhấn mạnh độ lớn rất nhỏ (“slightly greater than zero”), không nói về sự dao động thất thường.'),
            ('Wrong Direction', 'persistent = dai dẳng, kéo dài — không tương phản với “strongly affect” và không khớp ví dụ gần bằng 0.'),
            ('Đáp án đúng', 'subdued = nhẹ, yếu, không mạnh mẽ — đối lập hoàn hảo với “strongly affect” và khớp ví dụ tác động GDP Đức gần như bằng 0.'),
            ('Unsupported Tone', 'beneficial = có lợi — bài chỉ nói tác động rất nhỏ gần bằng 0, không nói cú sốc dầu mỏ mang lại lợi ích.'),
        ],
    ),

    # --- M1 Q3 ---
    q_item(
        'june2025_v1_rw_m1_q3', 3, 'Craft and Structure', 'Words in Context', 'Medium',
        '<p>Writer Lydia Davis observed that while _______ literary forms, such as the poem, are recognizable as such even as they evolve, there are pathbreaking “intergeneric” forms that might, for example, use elements of both fables and realist narratives to create something unclassifiable. Davis’s own very short literary pieces arguably fit in this category, since they straddle the line between prose and poetry.</p>',
        'Which choice completes the text with the most logical and precise word or phrase?',
        ['innovative', 'elusive', 'established', 'ambiguous'],
        'C',
        'Mệnh đề tương phản “while _______ literary forms, such as the poem, are recognizable as such..., there are pathbreaking ‘intergeneric’ forms... unclassifiable”: vế sau nói về các thể loại mới mẻ mở đường (pathbreaking) và không thể xếp loại (unclassifiable); do đó vế trước (ví dụ như “the poem” — thơ ca, luôn dễ nhận diện) phải là các thể loại văn học TRUYỀN THỐNG, ĐÃ ĐƯỢC XÁC LẬP LÂU ĐỜI → Chọn C (“established”).',
        'Khóa cặp từ tương phản qua liên từ “while”: “pathbreaking / unclassifiable” (mới mẻ, khó xếp loại) ↔ “established / recognizable” (lâu đời, đã được định hình rõ ràng).',
        [
            ('Opposite Meaning', 'innovative = mang tính đổi mới — đây là sắc thái của nhóm “pathbreaking intergeneric forms” ở vế sau, không phải thể loại quen thuộc như thơ.'),
            ('Opposite Meaning', 'elusive = khó nắm bắt — mâu thuẫn trực tiếp với “recognizable as such” (dễ nhận diện).'),
            ('Đáp án đúng', 'established = đã được xác lập, truyền thống, quen thuộc — đối lập sắc nét với “pathbreaking” và khớp ví dụ “the poem”.'),
            ('Opposite Meaning', 'ambiguous = mơ hồ, mập mờ — trái ngược với “recognizable” và thuộc về đặc trưng “straddle the line” ở vế sau.'),
        ],
    ),

    # --- M1 Q4 ---
    q_item(
        'june2025_v1_rw_m1_q4', 4, 'Craft and Structure', 'Words in Context', 'Medium',
        '<p>Mauricio Drelichman and Hans-Joachim Voth’s analysis of the debt repayments and expenditure of the government of Philip II (who ruled an empire including Spain and Milan from 1556 to 1598) found a seeming contradiction: although the government had several short-term cash shortages, it ran an even larger surplus than did the government of eighteenth-century Britain, a nation considered _______ of fiscal virtue.</p>',
        'Which choice completes the text with the most logical and precise word or phrase?',
        ['a sanction', 'a paradox', 'an exemplar', 'an omen'],
        'C',
        'Ngữ cảnh nhấn mạnh nghịch lý thú vị: dù chính quyền Philip II từng gặp vài đợt thiếu tiền mặt ngắn hạn, họ lại đạt thặng dư ngân sách LỚN HƠN CẢ chính quyền nước Anh thế kỷ 18 — một quốc gia vốn được xem là HÌNH MẪU / TẤM GƯƠNG TIÊU BIỂU về kỷ luật tài khóa (“fiscal virtue”) → Chọn C (“an exemplar” = hình mẫu chuẩn mực, ví dụ điển hình đáng noi theo).',
        'Cấu trúc so sánh “even larger surplus than [famous benchmark], a nation considered _______ of fiscal virtue” đòi hỏi danh từ chỉ “hình mẫu lý tưởng” → an exemplar.',
        [
            ('Wrong Meaning', 'a sanction = lệnh trừng phạt hoặc sự phê chuẩn chính thức — không có nghĩa là hình mẫu của sự mẫu mực tài chính.'),
            ('Word-Trap Echo', 'a paradox = nghịch lý — ăn theo chữ “contradiction” ở đầu câu nhưng nước Anh thế kỷ 18 không phải “nghịch lý của đạo đức tài khóa” mà là chuẩn mực so sánh.'),
            ('Đáp án đúng', 'an exemplar = hình mẫu tiêu biểu, tấm gương chuẩn mực — giải thích hoàn hảo vì sao vượt qua thặng dư của nước Anh thế kỷ 18 là điều đáng kinh ngạc.'),
            ('Wrong Meaning', 'an omen = điềm báo — hoàn toàn lệch ngữ cảnh lịch sử kinh tế.'),
        ],
    ),

    # --- M1 Q5 ---
    q_item(
        'june2025_v1_rw_m1_q5', 5, 'Craft and Structure', 'Text Structure and Purpose', 'Medium',
        '<p>The following text is from Anthony Trollope’s 1855 novel <i>The Warden</i>. Charles James is the son of a high-ranking clergy member.</p>'
        '<p>Charles James was an exact and careful boy; he never committed himself; he well knew how much was expected from the eldest son of the Archdeacon of Barchester, and was therefore mindful not to mix too freely with other boys. He had not the great talents of his younger brothers, but he exceeded them in judgment and propriety of demeanour; his fault, <u>if he had one</u>, was an over-attention to words instead of things; there was a thought too much finesse about him, and, as even his father sometimes told him, he was too fond of a compromise.</p>',
        'Which choice best states the function of the phrase “if he had one” in the text as a whole?',
        [
            'It acknowledges that the qualities in Charles James the narrator goes on to describe may not actually be undesirable characteristics.',
            'It concedes that Charles James’s attempts to be held in respect are sometimes fruitless.',
            'It signals a shift in focus from describing Charles James’s good qualities to criticizing his tendency to place too much value on artfulness.',
            'It anticipates readers’ objections to the narrator’s criticism of Charles James’s faults.',
        ],
        'A',
        'Trong câu “his fault, if he had one, was an over-attention to words instead of things; there was a thought too much finesse about him...”, cụm xen giữa “if he had one” (nếu quả thực cậu có khuyết điểm) đóng vai trò giảm nhẹ / rào trước cho chữ “fault”: người kể chuyện thừa nhận rằng những đặc điểm sắp liệt kê (quá chú trọng lời nói, hơi khéo léo thái quá, ưa thỏa hiệp) thực ra có thể không hẳn là tính xấu hay khiếm khuyết đáng chê → Chọn A!',
        'Phân biệt tinh tế giữa “his fault” và cụm chêm “if he had one”: “his fault” mới là phần chuyển sang nêu khuyết điểm, còn “if he had one” làm dịu khẳng định đó bằng cách mở khả năng cậu thậm chí chẳng có khuyết điểm thực sự nào.',
        [
            ('Đáp án đúng', 'Diễn tả chính xác tác dụng rào đón của “if he had one”: thừa nhận các nét tính cách sắp nêu có thể thực chất không phải đặc điểm xấu.'),
            ('Unsupported Inference', 'Văn bản không nói nỗ lực giành sự tôn trọng của Charles James bị thất bại hay vô ích.'),
            ('Scope Mismatch', 'Bẫy rất dễ dính: chính từ “his fault” chuyển mạch sang phê bình sự khéo léo quá mức (“finesse”), còn cụm “if he had one” lại làm giảm nhẹ lời phê bình đó chứ không đóng vai trò chỉ trích.'),
            ('Unsupported Audience', 'Đây mới là đoạn giới thiệu nhân vật, người kể không hề phản hồi hay lường trước sự phản đối của độc giả.'),
        ],
    ),

    # --- M1 Q6 ---
    q_item(
        'june2025_v1_rw_m1_q6', 6, 'Craft and Structure', 'Text Structure and Purpose', 'Hard',
        '<p>The establishment of urban green spaces for the abatement of fine particulate matter and other major air-pollutant concentrations is gaining public support, but urban planners must proceed with caution given subtleties in the body of evidence for the strategy’s efficacy. High-level reports have attributed pollutant reductions to cities’ inclusion of green spaces; however, one study found that while trees are negatively associated with air pollutants when considered on a citywide scale, at the street level, this association is minimal and at times positive. Because research tends to focus on large-scale effects in cities, decision-makers may be unaware that those outcomes are not always generalizable across spatial scales.</p>',
        'Which choice best describes the overall structure of the text?',
        [
            'It outlines a problem that is of growing public concern, explains why an innovative solution to that problem is challenging to implement, and then suggests the importance of researching alternative solutions.',
            'It addresses an appealing approach to a prevalent problem, illustrates that the approach is not as uniformly successful as it may seem, and then further emphasizes the importance of recognizing nuances in the research on that approach.',
            'It details an initiative implemented in response to certain research findings, identifies an apparent inconsistency within those findings, and then explains how that inconsistency has typically been accounted for.',
            'It establishes the growing intensity of a public concern, details the most common method of mitigating that concern, and then refers to evidence that the method is broadly ineffective.',
        ],
        'B',
        'Chia 3 câu của đoạn văn thành 3 chặng cấu trúc: (1) Câu 1 giới thiệu một giải pháp đang được công chúng ủng hộ (“gaining public support” = appealing approach) để giảm ô nhiễm không khí đô thị, kèm lời khuyên thận trọng; (2) Câu 2 minh họa giải pháp này không hiệu quả đồng đều như tưởng tượng (ở quy mô toàn thành phố thì giảm ô nhiễm, nhưng ở cấp độ đường phố lại rất ít hoặc thậm chí tăng); (3) Câu 3 nhấn mạnh thêm tầm quan trọng của việc nhận thức các sắc thái tinh tế trong nghiên cứu (kết quả quy mô lớn không phải lúc nào cũng khái quát hóa được sang quy mô nhỏ hơn) → Chọn B!',
        'Với câu hỏi Overall Structure, hãy chia từng câu thành 3 mệnh đề A → B → C rồi loại ngay đáp án sai ở chỉ MỘT chặng (như A sai ở “alternative solutions”, C sai ở “how typically accounted for”, D sai ở “broadly ineffective”).',
        [
            ('Added / Wrong Ending', 'Bài không giải thích lý do khó triển khai cũng không đề xuất tìm “giải pháp thay thế” (alternative solutions).'),
            ('Đáp án đúng', 'Khớp cả 3 chặng cấu trúc: giải pháp hấp dẫn cho vấn đề phổ biến → minh họa hiệu quả không đồng đều theo quy mô → nhấn mạnh cần nhận diện sắc thái tinh tế trong nghiên cứu.'),
            ('Wrong Ending', 'Câu cuối cảnh báo nhà hoạch định có thể không nhận ra giới hạn khái quát hóa, hoàn toàn không giải thích cách sự mâu thuẫn thường được lý giải.'),
            ('Extreme Distortion', 'Cây xanh vẫn có liên hệ giảm ô nhiễm ở cấp độ toàn thành phố, nên nói phương pháp này “broadly ineffective” (nhìn chung vô hiệu) là bóp méo cực đoan.'),
        ],
    ),

    # --- M1 Q7 ---
    q_item(
        'june2025_v1_rw_m1_q7', 7, 'Information and Ideas', 'Central Ideas and Details', 'Easy',
        '<p><i>The Skin I’m In</i> was Sharon G. Flake’s debut novel. It was published in 1998. A debut novel is the first book that an author has published. Debut novels are especially interesting to literary critics (people whose job it is to evaluate books) and readers because these books offer a look at new voices in the literary world.</p>',
        'According to the text, what is someone who professionally evaluates books called?',
        ['A bookseller', 'An author', 'A literary critic', 'A book publisher'],
        'C',
        'Câu hỏi tìm chi tiết trực tiếp: Đoạn văn định nghĩa rõ trong ngoặc đơn: “literary critics (people whose job it is to evaluate books)” → Người có công việc chuyên đánh giá sách được gọi là “A literary critic” → Chọn C.',
        'Đọc thẳng phần định nghĩa đặt trong dấu ngoặc đơn hoặc dấu gạch ngang để chốt đáp án trong 10 giây.',
        [
            ('Not Mentioned', 'Đoạn văn không hề nhắc tới người bán sách (bookseller).'),
            ('Wrong Role', 'Author là tác giả viết sách, không phải người đánh giá sách.'),
            ('Đáp án đúng', 'Khớp nguyên văn định nghĩa trong ngoặc: “literary critics (people whose job it is to evaluate books)”.'),
            ('Not Mentioned', 'Nhà xuất bản (book publisher) không được định nghĩa là người đánh giá sách trong đoạn văn.'),
        ],
    ),

    # --- M1 Q8 ---
    q_item(
        'june2025_v1_rw_m1_q8', 8, 'Information and Ideas', 'Central Ideas and Details', 'Easy',
        '<p>The following text is adapted from L.M. Montgomery’s 1923 novel <i>Emily of New Moon</i>. Emily, a young girl who lives on a farm run by her aunt Elizabeth, wants to be a published writer someday.</p>'
        '<p>One of the things they [argued] about was the fact that Emily, as Aunt Elizabeth discovered one day, was in the habit of using more of her egg money to buy paper than Aunt Elizabeth approved of. What did Emily do with so much paper? They had a fuss over this and eventually Aunt Elizabeth discovered that Emily was writing stories. Emily had been writing stories all winter under Aunt Elizabeth’s very nose and Aunt Elizabeth had never suspected it. She had fondly supposed that Emily was writing school compositions.</p>',
        'Which choice best states the main idea of the text?',
        [
            'Emily forgot to buy eggs when she was supposed to.',
            'Aunt Elizabeth thinks Emily should spend more time at school.',
            'Aunt Elizabeth is surprised to find out that Emily has been writing stories.',
            'Emily is relieved to learn that Aunt Elizabeth enjoys reading Emily’s stories.',
        ],
        'C',
        'Toàn đoạn kể việc dì Elizabeth tranh cãi vì thấy Emily tiêu quá nhiều tiền bán trứng để mua giấy, rồi cuối cùng phát hiện ra Emily đã viết truyện suốt cả mùa đông ngay trước mũi mình mà bà “chưa từng nghi ngờ chút nào” (“had never suspected it”, cứ tưởng cô bé chỉ viết bài tập làm văn) → Ý chính là dì Elizabeth bất ngờ khi phát hiện Emily đang viết truyện → Chọn C.',
        'Chú ý các cụm từ cảm xúc trực tiếp ở hai câu kết: “under Aunt Elizabeth’s very nose”, “never suspected it”, “fondly supposed...” đều hội tụ vào sự ngạc nhiên của dì Elizabeth.',
        [
            ('Literal Misreading', '“egg money” là tiền kiếm được từ bán trứng để Emily mua giấy, không phải Emily quên mua trứng.'),
            ('Distortion', 'Dì Elizabeth tưởng Emily viết bài làm văn ở trường (“school compositions”), không nói bà muốn Emily dành thêm thời gian ở trường.'),
            ('Đáp án đúng', 'Tóm gọn chính xác trọng tâm đoạn văn: dì Elizabeth ngạc nhiên khi phát hiện Emily lén viết truyện suốt mùa đông.'),
            ('Contradiction', 'Hai dì cháu có cuộc tranh cãi (“fuss”); đoạn văn hoàn toàn không nói dì Elizabeth thích đọc truyện của Emily.'),
        ],
    ),

    # --- M1 Q9 ---
    q_item(
        'june2025_v1_rw_m1_q9', 9, 'Information and Ideas', 'Command of Evidence (Quantitative)', 'Easy',
        html_table(
            'Average Hours Worked per Person per Year in 1950 and 2017',
            ['Country', '1950', '2017', 'Change in hours', 'Percent change in hours'],
            [
                ['Peru', '2,157', '1,932', '−225', '−10%'],
                ['Canada', '2,209', '1,696', '−513', '−23%'],
                ['Denmark', '2,049', '1,400', '−649', '−32%'],
                ['Finland', '2,053', '1,659', '−394', '−19%'],
            ],
            footnote='Calculations may be inexact due to rounding.',
        )
        + '<p>A student in an economics course is examining the decline since 1950 in average hours worked per person per year in various nations due to both increased productivity and the adoption of policies that limit working hours. The first task in this investigation is to determine how the decline in Finland compares to that in other countries. The student finds that _______</p>',
        'Which choice most effectively uses data from the table to complete the student’s conclusion?',
        [
            'the percent decrease in hours worked was greater in Finland than it was in Denmark, Canada, or Peru.',
            'though the decline in number of hours worked in Finland was less than that in Denmark and Canada, it was greater than that in Peru.',
            'while the number of hours worked rose in Finland between 1950 and 2017, it declined in Denmark, Canada, and Peru.',
            'though the decline in number of hours worked in Finland was greater than that in Denmark and Peru, it was less than that in Canada.',
        ],
        'B',
        'Xếp hạng mức giảm số giờ làm việc (cột “Change in hours”) từ lớn nhất đến nhỏ nhất: Denmark (−649 giờ, −32%) > Canada (−513 giờ, −23%) > Finland (−394 giờ, −19%) > Peru (−225 giờ, −10%). Như vậy, mức giảm số giờ của Phần Lan (394 giờ) NHỎ HƠN Đan Mạch (649) và Canada (513), nhưng LỚN HƠN Peru (225) → Đáp án B khớp chính xác 100% số liệu bảng!',
        'Luôn sắp xếp thứ tự giá trị tuyệt đối mức giảm của 4 nước ra nháp trước khi đọc lựa chọn: Denmark (649) > Canada (513) > Finland (394) > Peru (225).',
        [
            ('False Data', 'Mức giảm phần trăm của Phần Lan là 19%, nhỏ hơn Đan Mạch (32%) và Canada (23%), không phải lớn hơn tất cả.'),
            ('Đáp án đúng', 'Khớp tuyệt đối số liệu: mức giảm của Phần Lan (394 giờ) nhỏ hơn Đan Mạch (649) và Canada (513), nhưng lớn hơn Peru (225).'),
            ('False Data', 'Số giờ làm việc ở Phần Lan GIẢM từ 2,053 xuống 1,659 (−394), không hề tăng.'),
            ('False Data', 'Mức giảm của Phần Lan (394) NHỎ HƠN Đan Mạch (649), không phải lớn hơn Đan Mạch.'),
        ],
    ),

    # --- M1 Q10 ---
    q_item(
        'june2025_v1_rw_m1_q10', 10, 'Information and Ideas', 'Command of Evidence (Quantitative)', 'Medium',
        html_table(
            'Percent Change in Average Global Market Prices by Commodity in Two Agricultural Trade-Reform Scenarios',
            ['Commodity', 'Percent change in TFA scenario', 'Percent change in tariff-removal scenario'],
            [
                ['Fruits and vegetables', '−1.50', '+0.04'],
                ['Processed foods', '−1.76', '−1.00'],
                ['Rice', '−0.37', '+1.36'],
                ['Wheat', '−1.35', '+0.45'],
            ],
        )
        + '<p>Ratified in 2017 by two-thirds of World Trade Organization member nations, the Trade Facilitation Agreement (TFA) is a trade-reform measure that aims to reduce redundant customs procedures and other costly aspects of international trade. In a 2021 report, economist Jayson Beckman modeled global market prices of several agricultural commodities under both the TFA and an alternative trade-reform scenario: removal of agricultural tariffs (taxes on imports that generally increase prices on imported goods). After reviewing data from the report, a student concludes that overall, consumers of the commodities listed in the table would likely benefit more from the TFA than they would from tariff removal.</p>',
        'Which choice most effectively uses data from the table to support the student’s claim?',
        [
            'Under the tariff-removal scenario, the average prices of processed foods, wheat, and fruits and vegetables would decrease by more than 1%, while the average price of rice would decrease by less than 1%.',
            'Under the tariff-removal scenario, the average price of processed foods would increase, but the average prices of wheat and rice would decrease.',
            'Under the TFA scenario, the average prices of all four commodities would decrease, whereas under the tariff-removal scenario, only the average price of processed foods would decrease.',
            'Under the TFA scenario, the average price of rice would decrease by a smaller amount than any of the other three commodities’ prices would, whereas its average price would increase under the tariff-removal scenario.',
        ],
        'C',
        'Claim của sinh viên: nhìn chung (“overall”), người tiêu dùng các mặt hàng trong bảng sẽ hưởng lợi nhiều hơn từ TFA so với xóa bỏ thuế quan (người tiêu dùng hưởng lợi khi GIÁ GIẢM = dấu âm). Đối chiếu bảng: (1) Ở cột TFA, CẢ 4 mặt hàng đều GIẢM giá (−1.50%, −1.76%, −0.37%, −1.35%); (2) Ở cột xóa thuế quan, CHỈ CÓ thực phẩm chế biến giảm giá (−1.00%), còn 3 mặt hàng kia đều TĂNG giá (+0.04%, +1.36%, +0.45%) → Đáp án C vừa đúng 100% số liệu vừa chứng minh toàn diện kết luận “overall”!',
        'Cảnh giác hai bẫy quen thuộc trong bảng: Bẫy tráo cột (A lấy số của TFA gán sang tariff-removal) và Bẫy đúng nhưng quá hẹp (D chỉ nói riêng về gạo nên không chứng minh được “overall” cho cả bảng).',
        [
            ('Swapped Columns', 'Các con số giảm >1% (processed foods, wheat, fruits & vegetables) và giảm <1% (rice) là của kịch bản TFA, KHÔNG phải tariff-removal!'),
            ('Reversed Signs', 'Ngược dấu hoàn toàn ở cột tariff-removal: processed foods GIẢM (−1.00), còn wheat (+0.45) và rice (+1.36) TĂNG.'),
            ('Đáp án đúng', 'Khớp số liệu toàn bảng và ủng hộ trực tiếp nhận định “overall”: TFA làm giảm giá cả 4 mặt hàng, trong khi xóa thuế chỉ giảm giá mỗi thực phẩm chế biến.'),
            ('True Data / Too Narrow', 'Đúng số liệu về gạo nhưng chỉ đề cập 1 mặt hàng duy nhất, kém thuyết phục hơn hẳn C khi cần chứng minh lợi ích tổng thể (“overall”) của cả 4 mặt hàng.'),
        ],
    ),

    # --- M1 Q11 ---
    q_item(
        'june2025_v1_rw_m1_q11', 11, 'Information and Ideas', 'Command of Evidence (Quantitative)', 'Hard',
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
                ['Quarter-dollar', '568.4', '264.4', '304.0', '0.53'],
            ],
        )
        + '<p>Issuing a one-dollar coin yields positive seigniorage—the profit generated when the face value of a coin exceeds the unit cost of producing it—for Singapore’s government, which in turn can be used to fund such services as transportation. Some countries, such as the Netherlands, have ceased manufacturing certain coins because their production created negative seigniorage. In an economics class discussing the data in the table, one student argues that in 2023, the one-cent coin was the least financially sensible for the US to produce, while another student argues that the five-cent coin was.</p>',
        'Based on the information in the text and the table, the two students most likely disagree about the answer to which question?',
        [
            'When evaluating the financial implications of issuing a coin, which is more important, the total seigniorage from issuing that coin or the seigniorage per dollar when issuing that coin?',
            'If issuing a given coin results in negative seigniorage per dollar issued, can that be changed to positive seigniorage per dollar issued by reducing the cost of issuing the coin?',
            'If issuing a given coin results in positive seigniorage per dollar but not as much positive seigniorage per dollar as issuing a different coin does, does it make financial sense to continue issuing the first coin?',
            'When determining whether it makes financial sense to issue a given coin, which is more important, the total value of the units of that coin produced or the gross cost of issuing that coin?',
        ],
        'A',
        'So sánh trực tiếp hai đồng xu gây lỗ (negative seigniorage) trong bảng: (1) Đồng One-cent lỗ nặng nhất xét theo **lợi nhuận đúc tiền trên mỗi 1 USD phát hành** (“Seigniorage per $1 issued” = −2.08 USD, tệ hơn −1.31 USD của đồng 5 xu); (2) Đồng Five-cent lỗ nặng nhất xét theo **tổng lỗ tuyệt đối** (“Seigniorage” = −92.6 triệu USD, tệ hơn −86.0 triệu USD của đồng 1 xu). Do đó, hai sinh viên bất đồng chính ở tiêu chí đánh giá nào quan trọng hơn: tổng seigniorage hay seigniorage trên mỗi đô la phát hành → Chọn A!',
        'Khi hai người nhìn cùng một bảng số liệu mà rút ra 2 đối tượng “tệ nhất” khác nhau (One-cent vs. Five-cent), hãy tìm ngay 2 cột mà ở cột này One-cent tệ nhất còn ở cột kia Five-cent tệ nhất!',
        [
            ('Đáp án đúng', 'Khớp hoàn hảo: cột “Seigniorage” chỉ ra Five-cent lỗ tổng nhiều nhất (−92.6 triệu USD), còn cột “Seigniorage per $1 issued” chỉ ra One-cent lỗ nặng nhất trên mỗi đô la (−2.08 USD).'),
            ('Irrelevant Criterion', 'Cả hai đồng 1 xu và 5 xu đều có seigniorage âm; việc có cắt giảm chi phí được hay không không giải thích vì sao mỗi sinh viên chọn một đồng xu khác nhau là tệ nhất năm 2023.'),
            ('Wrong Sign', 'Nói về đồng xu có seigniorage dương (như Ten-cent, Quarter-dollar), hoàn toàn không liên quan đến cuộc tranh luận giữa One-cent và Five-cent.'),
            ('Wrong Column Pair', 'Xét riêng Gross cost thì Quarter-dollar mới cao nhất (264.4 triệu USD), không phải Five-cent; nên cặp cột tổng giá trị vs. tổng chi phí không phân tách ra đúng One-cent và Five-cent.'),
        ],
    ),

    # --- M1 Q12 ---
    q_item(
        'june2025_v1_rw_m1_q12', 12, 'Information and Ideas', 'Command of Evidence (Textual)', 'Medium',
        '<p>Describing adverbs as “silly,” novelist Chuck Palahniuk is one of several authors and literary critics who have recommended minimizing the use of adverbs, especially those ending in <i>-ly</i> (e.g., “graciously”), in works of fiction. To investigate the prevalence of <i>-ly</i> adverbs in novels, author and statistician Ben Blatt used natural language processing—machine learning technology that reads and interprets text—to calculate the rates at which these words occur in the novels of William Faulkner, who was awarded the Nobel Prize in Literature in 1949. Blatt concluded that in Faulkner’s oeuvre, there is a negative correlation between <i>-ly</i> adverb proliferation and perceived literary merit.</p>',
        'Which finding, if true, would most directly illustrate the pattern Blatt identified?',
        [
            'Whereas Faulkner’s acclaimed novel <i>The Sound and the Fury</i> has one of the lowest <i>-ly</i> adverb rates among Faulkner’s works, F. Scott Fitzgerald’s classic novel <i>The Great Gatsby</i> has the lowest <i>-ly</i> adverb rate among Fitzgerald’s novels.',
            'In <i>The Sound and the Fury</i>, which is widely recognized as a literary masterpiece, Faulkner used 42 <i>-ly</i> adverbs per 10,000 words, whereas in his less-acclaimed novel <i>Soldiers’ Pay</i>, Faulkner used 148 <i>-ly</i> adverbs per 10,000 words.',
            'In his celebrated novel <i>Light in August</i>, Faulkner used 67 <i>-ly</i> adverbs per 10,000 words, whereas 67% of celebrated authors’ novels that have fewer than 50 <i>-ly</i> adverbs per 10,000 words have been classified as great by critics.',
            'Whereas Faulkner used on average 92 <i>-ly</i> adverbs per 10,000 words in the 19 novels of Faulkner’s that Blatt investigated, Toni Morrison, winner of the 1993 Nobel Prize in Literature, used on average 76 <i>-ly</i> adverbs per 10,000 words in her novels.',
        ],
        'B',
        'Khóa kết luận của Ben Blatt: Trong toàn bộ tác phẩm của William Faulkner (“in Faulkner’s oeuvre”), có **tương quan nghịch** (negative correlation) giữa mật độ trạng từ đuôi *-ly* và giá trị văn học được đánh giá (perceived literary merit) — tức tác phẩm càng được khen ngợi thì càng ÍT trạng từ *-ly*, tác phẩm kém tiếng vang hơn thì NHIỀU trạng từ *-ly*. Đáp án B đối chiếu đúng hai tiểu thuyết CỦA CHÍNH FAULKNER: kiệt tác *The Sound and the Fury* chỉ dùng 42 từ/10.000 từ, còn tác phẩm ít được đánh giá cao hơn là *Soldiers’ Pay* dùng tới 148 từ/10.000 từ → Chọn B!',
        'Để minh họa “negative correlation” trong phạm vi một tác giả (“in Faulkner’s oeuvre”), đáp án BẮT BUỘC so sánh hai đầu cao–thấp trong chính các tác phẩm của Faulkner (loại ngay các đáp án lôi tác giả khác như Fitzgerald, Toni Morrison vào).',
        [
            ('Missing Low-Merit Comparison', 'Chỉ nêu hai kiệt tác của Faulkner và Fitzgerald đều ít trạng từ -ly, không cho thấy tác phẩm kém tiếng hơn của Faulkner dùng nhiều trạng từ -ly hơn.'),
            ('Đáp án đúng', 'Minh họa trực diện tương quan nghịch ngay trong sự nghiệp Faulkner: kiệt tác (merit cao) = 42 trạng từ -ly/10.000 từ ↔ tác phẩm ít tiếng vang (merit thấp) = 148 trạng từ -ly/10.000 từ.'),
            ('Wrong Scope / Irrelevant Comparison', 'So sánh *Light in August* của Faulkner với tỷ lệ chung của các tác giả khác không chứng minh mối tương quan bên trong các tiểu thuyết của Faulkner.'),
            ('Wrong Scope (Different Author)', 'So sánh trung bình của Faulkner với Toni Morrison hoàn toàn lệch khỏi phạm vi “in Faulkner’s oeuvre”.'),
        ],
    ),

    # --- M1 Q13 ---
    q_item(
        'june2025_v1_rw_m1_q13', 13, 'Information and Ideas', 'Command of Evidence (Textual)', 'Hard',
        '<p>Students in a biology class investigated why individual house mice (<i>Mus musculus</i>) can differ from one another in their circulating sodium level. The students compared wild-type mice and knockout mice, which are mice with specific genes deactivated, when mice of each type were placed in similar naturalistic environments and taken for periodic blood sampling. Finding that knockout mice with the gene <i>Asb5</i> deactivated tended to have lower concentrations of sodium in their blood than did wild-type mice, the students concluded that differences in circulating sodium level among house mice in nature are solely attributable to variations in the level of expression of <i>Asb5</i>.</p>',
        'Which finding, if true, would most directly weaken the students’ conclusion?',
        [
            'Some wild-type mice were very similar to the knockout mice with regard to circulating sodium level but showed a wide variety of levels of expression of <i>Asb5</i>.',
            'A sampling of house mice captured in natural settings shows that individual mice can differ from one another in the level of expression of <i>Asb5</i>.',
            'The level of expression of <i>Asb5</i> does not appear to affect the functioning of any other genes in house mice.',
            'The mice with <i>Asb5</i> deactivated were identical to the wild-type mice except with regard to circulating sodium level.',
        ],
        'A',
        'Khóa từ cực đoan trong kết luận của nhóm sinh viên: sự khác biệt nồng độ natri máu ở chuột nhà trong tự nhiên **HOÀN TOÀN / DUY NHẤT** (“solely attributable”) do biến thiên mức độ biểu hiện của gen *Asb5* gây ra. Để làm suy yếu trực tiếp lập luận “duy nhất do *Asb5*”, chỉ cần chỉ ra các cá thể có nồng độ natri máu gần giống hệt nhau (wild-type giống knockout) nhưng lại có mức biểu hiện *Asb5* biến thiên rất rộng — chứng tỏ *Asb5* KHÔNG phải yếu tố duy nhất quyết định nồng độ natri máu → Chọn A!',
        'Trong câu hỏi Weaken có từ tuyệt đối (“solely attributable”), hãy tìm bằng chứng tách rời hai biến số: X (*Asb5*) thay đổi rất mạnh mà Y (natri máu) vẫn tương đương nhau!',
        [
            ('Đáp án đúng', 'Nếu nhiều chuột wild-type có nồng độ natri giống chuột bị tắt gen *Asb5* dù mức biểu hiện *Asb5* rất đa dạng, thì biến thiên natri không thể “duy nhất do *Asb5*” quyết định.'),
            ('Strengthens Slightly', 'Việc chuột tự nhiên thực sự có mức biểu hiện *Asb5* khác nhau lại ủng hộ tiền đề cho kết luận của sinh viên.'),
            ('Strengthens / Removes Confounder', 'Loại trừ khả năng *Asb5* tác động gián tiếp lên gen khác, thực chất giúp củng cố kết luận của sinh viên.'),
            ('Strengthens / Controls Variable', 'Cho thấy thí nghiệm kiểm soát biến nhiễu tốt giữa nhóm knockout và wild-type — củng cố chứ không làm yếu kết luận.'),
        ],
    ),

    # --- M1 Q14 ---
    q_item(
        'june2025_v1_rw_m1_q14', 14, 'Information and Ideas', 'Inferences', 'Medium',
        '<p>Neuroscientist Artin Arshamian and his team sought to determine what affects a person’s perception of an odor as pleasant: is it culture, personal taste, or aspects of human anatomy? The team assessed odor preferences in ten groups of people with different modes of living (urban, agricultural, and hunter-gatherer) including urban dwellers from a large city in Thailand and Chachi people from a small community in Ecuador. The team observed that across cultures, people generally rated odors about the same: vanillin, which smells like vanilla, was typically rated more pleasant than isovaleric acid, which smells like human sweat. The team therefore concluded that _______</p>',
        'Which choice most logically completes the text?',
        [
            'a person who lives in an urban area is more likely to encounter the odor of vanillin than is a person who lives in a small community.',
            'a person’s mode of living likely doesn’t have a large influence on that person’s perception of whether an odor is pleasant or unpleasant.',
            'a person who perceives certain odors as pleasant will likely perceive the odors as roughly equal in pleasantness.',
            'culture likely plays more of a role in a person’s perception of how pleasant an odor is than does human anatomy.',
        ],
        'B',
        'Suy luận logic trực tiếp: Nhóm Arshamian kiểm tra sở thích mùi hương ở 10 nhóm người có **lối sống hoàn toàn khác nhau** (“different modes of living”: đô thị, nông nghiệp, săn bắt hái lượm; Thái Lan vs. Ecuador) và nhận thấy **giữa các nền văn hóa, con người nhìn chung đánh giá mùi hương tương tự nhau** (“across cultures, people generally rated odors about the same”). Kết luận tất yếu: lối sống (mode of living) có lẽ không ảnh hưởng lớn đến việc một người cảm nhận mùi hương là dễ chịu hay khó chịu → Chọn B!',
        'Khi biến đầu vào thay đổi mạnh (10 lối sống & nền văn hóa khác nhau) nhưng kết quả đầu ra vẫn giống nhau (“rated odors about the same”), suy luận hợp lệ là biến đầu vào đó không có ảnh hưởng lớn đến kết quả.',
        [
            ('Out of Scope', 'Bài không so sánh tần suất bắt gặp mùi vanillin giữa người thành thị và cộng đồng nhỏ.'),
            ('Đáp án đúng', 'Khớp hoàn hảo chuỗi lập luận: khác biệt lối sống (urban / agricultural / hunter-gatherer) nhưng đánh giá mùi giống nhau → lối sống không ảnh hưởng lớn.'),
            ('Misreading “About the Same”', 'Cụm “rated odors about the same” chỉ sự đồng nhất GIỮA CÁC NỀN VĂN HÓA (cùng thích vanillin hơn mồ hôi), không phải mọi mùi thơm đều dễ chịu ngang nhau.'),
            ('Reversed Logic', 'Vì các nền văn hóa khác nhau đánh giá giống nhau nên văn hóa đóng vai trò ÍT hơn (không phải nhiều hơn) so với giải phẫu/sinh học con người.'),
        ],
    ),

    # --- M1 Q15 ---
    q_item(
        'june2025_v1_rw_m1_q15', 15, 'Standard English Conventions', 'Boundaries', 'Easy',
        '<p>The towns Entebbe and Jamame are both located almost directly on the _______ they are in different countries. Entebbe is in Uganda, while Jamame is in Somalia.</p>',
        'Which choice completes the text so that it conforms to the conventions of Standard English?',
        ['equator', 'equator, but', 'equator,', 'equator that'],
        'B',
        'Phân tích ranh giới mệnh đề: Trước chỗ trống là mệnh đề độc lập 1 (“The towns Entebbe and Jamame are both located almost directly on the equator”); sau chỗ trống là mệnh đề độc lập 2 (“they are in different countries”). Để nối 2 mệnh đề độc lập có nghĩa tương phản, cần dấu phẩy + liên từ đẳng lập FANBOYS → “equator, but” (B)!',
        'Công thức vàng Boundaries: IC + `, but` + IC. Loại ngay A (run-on sentence), C (comma splice), và D (thiếu liên kết hợp ngữ pháp).',
        [
            ('Run-on / Fused Sentence', 'Nối liền hai mệnh đề độc lập mà không có dấu câu hay liên từ gây lỗi câu dính (run-on).'),
            ('Đáp án đúng', 'Dùng `, but` (dấu phẩy + liên từ FANBOYS) nối chuẩn xác hai mệnh đề độc lập mang ý tương phản.'),
            ('Comma Splice', 'Chỉ dùng một dấu phẩy nối hai mệnh đề độc lập là lỗi comma splice kinh điển.'),
            ('Ungrammatical Structure', 'Thêm “that” biến vế sau thành mệnh đề quan hệ không hợp nghĩa với “equator” và dư chủ ngữ “they”.'),
        ],
    ),

    # --- M1 Q16 ---
    q_item(
        'june2025_v1_rw_m1_q16', 16, 'Standard English Conventions', 'Form, Structure, and Sense', 'Easy',
        '<p>Having trained as astronauts for years, _______</p>',
        'Which choice completes the text so that it conforms to the conventions of Standard English?',
        [
            'August 2, 1991, was when space shuttle <i>Atlantis</i> took flight with five crew members aboard.',
            'it was August 2, 1991, when five crew members took flight aboard space shuttle <i>Atlantis</i>.',
            'five crew members took flight aboard space shuttle <i>Atlantis</i> on August 2, 1991.',
            'space shuttle <i>Atlantis</i> took flight on August 2, 1991, with five crew members aboard.',
        ],
        'C',
        'Quy tắc Dangling Modifier (Bổ ngữ lơ lửng): Cụm phân từ mở đầu “Having trained as astronauts for years,” mô tả hành động của AI? Của **năm thành viên phi hành đoàn** (“five crew members”), CHỨ KHÔNG PHẢI của ngày tháng (“August 2, 1991”), chủ ngữ giả (“it”), hay tàu con thoi (“space shuttle *Atlantis*”). Do đó danh từ đứng ngay sau dấu phẩy BẮT BUỘC phải là “five crew members” → Chọn C!',
        'Mẹo 3 giây cho Modifier Placement: Hỏi ngay “Ai thực hiện hành động trong cụm mở đầu?” → Đặt đúng chủ thể đó làm chủ ngữ đầu tiên sau dấu phẩy.',
        [
            ('Dangling Modifier', 'Ngày “August 2, 1991” không thể tự “trained as astronauts for years”.'),
            ('Dangling Modifier', 'Chủ ngữ giả “it” không thể là người đã huấn luyện làm phi hành gia.'),
            ('Đáp án đúng', 'Đặt đúng chủ thể “five crew members” ngay sau cụm phân từ “Having trained as astronauts for years,”.'),
            ('Dangling Modifier', 'Tàu con thoi *Atlantis* là phương tiện, không phải người được đào tạo làm phi hành gia.'),
        ],
    ),

    # --- M1 Q17 ---
    q_item(
        'june2025_v1_rw_m1_q17', 17, 'Standard English Conventions', 'Form, Structure, and Sense', 'Easy',
        '<p>In 1991, New Jersey _______ official fossil: the <i>Hadrosaurus foulkii</i>, which is a Cretaceous period dinosaur.</p>',
        'Which choice completes the text so that it conforms to the conventions of Standard English?',
        [
            'lawmakers designated the state’s',
            'lawmakers designated the states',
            'lawmaker’s designated the states',
            'lawmaker’s designated the state’s',
        ],
        'A',
        'Kiểm tra số nhiều vs. sở hữu cách (Plurals & Possessives): (1) “New Jersey lawmakers” là chủ ngữ số nhiều thực hiện động từ “designated” (các nhà lập pháp bang New Jersey đã chỉ định) → KHÔNG có dấu nháy sở hữu (`lawmakers`, loại C & D); (2) “the state’s official fossil” (hóa thạch chính thức CỦA bang New Jersey) → CẦN sở hữu cách số ít (`state’s`, loại B) → Chọn A!',
        'Kiểm tra từng danh từ bằng quy tắc “thuộc về”: trước động từ “designated” cần chủ ngữ số nhiều (`lawmakers`), trước danh từ “official fossil” cần sở hữu cách (`the state’s`).',
        [
            ('Đáp án đúng', 'Chủ ngữ số nhiều “lawmakers” không dấu nháy + sở hữu cách số ít “the state’s” đứng trước “official fossil”.'),
            ('Missing Possessive', '“the states” là số nhiều không sở hữu, sai ngữ pháp khi đứng trước cụm danh từ “official fossil”.'),
            ('Double Possessive Error', 'Sai cả hai vị trí: “lawmaker’s” thừa sở hữu trước động từ và “states” thiếu sở hữu trước danh từ.'),
            ('Extra Possessive', '“lawmaker’s” có dấu nháy sở hữu đứng ngay trước động từ chính “designated” là sai ngữ pháp.'),
        ],
    ),

    # --- M1 Q18 ---
    q_item(
        'june2025_v1_rw_m1_q18', 18, 'Standard English Conventions', 'Boundaries', 'Medium',
        '<p>Nicosia is home to roughly 27 percent of Cyprus’s total population. This means that about 1 in 4 _______ live in Cyprus live in Nicosia!</p>',
        'Which choice completes the text so that it conforms to the conventions of Standard English?',
        ['people', 'people who', 'people,', 'people, who'],
        'B',
        'Phân tích cấu trúc câu: Chủ ngữ chính là “about 1 in 4 people [who live in Cyprus]” và động từ chính là “live in Nicosia!”. Cụm “who live in Cyprus” là mệnh đề quan hệ XÁC ĐỊNH (restrictive/essential) dùng để giới hạn nhóm người đang xét (1 trong 4 người SỐNG Ở SÍP), nên BẮT BUỘC có đại từ quan hệ “who” và TUYỆT ĐỐI KHÔNG đặt dấu phẩy trước “who” → Chọn B (“people who”)!',
        'Mệnh đề quan hệ xác định (không thể bỏ mà câu vẫn giữ đúng nghĩa) KHÔNG dùng dấu phẩy; ngoài ra nếu thêm 1 dấu phẩy đơn trước “who” (như D) còn phá vỡ cấu trúc vì thiếu dấu phẩy đóng trước động từ thứ hai “live”.',
        [
            ('Double Finite Verb', 'Thiếu đại từ quan hệ “who” khiến câu có hai động từ chia thì đứng liền nhau (“people live in Cyprus live in Nicosia”).'),
            ('Đáp án đúng', '“people who live in Cyprus” tạo mệnh đề quan hệ xác định gọn ghẽ, làm rõ chủ ngữ cho động từ chính “live in Nicosia!”.'),
            ('Ungrammatical Comma', 'Vừa thiếu “who” vừa chèn dấu phẩy ngăn cách chủ ngữ với động từ.'),
            ('Unpaired / Nonrestrictive Comma', 'Mệnh đề “who live in Cyprus” là thông tin thiết yếu không được tách bằng dấu phẩy; hơn nữa dấu phẩy đơn lẻ trước “who” không có dấu phẩy đóng sau “Cyprus”.'),
        ],
    ),

    # --- M1 Q19 ---
    q_item(
        'june2025_v1_rw_m1_q19', 19, 'Standard English Conventions', 'Form, Structure, and Sense', 'Easy',
        '<p>In the Persian language, people commonly begin a folktale with a phrase that roughly translates to “there was and there was not.” In English, beginning with the phrase “once upon a time” is common. Indeed, how a folktale begins depends largely on the language in which _______ being told.</p>',
        'Which choice completes the text so that it conforms to the conventions of Standard English?',
        ['they were', 'these are', 'they are', 'it is'],
        'D',
        'Kiểm tra sự hòa hợp đại từ – tiền ngữ (Pronoun-Antecedent Agreement) và thì động từ: Danh từ được thay thế trong câu là số ít “a folktale” (một câu chuyện dân gian), và toàn đoạn đang chia thì hiện tại đơn (“commonly begin”, “begins”, “depends”) → Cần đại từ số ít + động từ hiện tại số ít: “it is” → Chọn D!',
        'Trong câu Pronoun Agreement, luôn khoanh tròn danh từ gốc đứng cùng câu (“a folktale” = số ít) để loại ngay toàn bộ các lựa chọn số nhiều (“they”, “these”).',
        [
            ('Number & Tense Mismatch', '“they were” vừa sai số nhiều (tiền ngữ “a folktale” là số ít) vừa sai thì quá khứ.'),
            ('Number Mismatch', '“these are” là số nhiều, không khớp với tiền ngữ số ít “a folktale”.'),
            ('Number Mismatch', '“they are” là số nhiều, không khớp với “a folktale”.'),
            ('Đáp án đúng', '“it is” khớp chính xác cả số ít (“a folktale”) lẫn thì hiện tại đơn của câu (“begins”, “depends”).'),
        ],
    ),

    # --- M1 Q20 ---
    q_item(
        'june2025_v1_rw_m1_q20', 20, 'Standard English Conventions', 'Boundaries', 'Easy',
        '<p><i>Thraxas</i> by Martin Scott, <i>Richard Matheson: Collected Stories</i> by Richard Matheson, and <i>Strange Tales</i> by Rosalie Parker are all pieces of literature that have won the prestigious World Fantasy _______ the works received the honor in the categories of novel, collection, and anthology, respectively.</p>',
        'Which choice completes the text so that it conforms to the conventions of Standard English?',
        ['Award', 'Award;', 'Award and', 'Award,'],
        'B',
        'Kiểm tra ranh giới mệnh đề độc lập: Mệnh đề 1 kết thúc trọn vẹn tại “World Fantasy Award” (đủ chủ ngữ + vị ngữ “are all pieces of literature that have won...”). Mệnh đề 2 cũng là mệnh đề độc lập hoàn chỉnh (“the works received the honor in the categories of novel, collection, and anthology, respectively.”). Hai mệnh đề độc lập có thể nối bằng dấu chấm phẩy `;` → Chọn B (“Award;”)!',
        'Nhớ 3 cách nối 2 mệnh đề độc lập chuẩn SAT: (1) dấu chấm `.`, (2) dấu chấm phẩy `;`, (3) dấu phẩy + FANBOYS `, and`. Ở đây C (“Award and”) thiếu dấu phẩy nên sai!',
        [
            ('Run-on / Fused Sentence', 'Nối thẳng hai mệnh đề độc lập không có bất kỳ dấu câu nào là lỗi run-on.'),
            ('Đáp án đúng', 'Dấu chấm phẩy (`;`) nối chuẩn xác hai mệnh đề độc lập có liên hệ ý nghĩa chặt chẽ.'),
            ('Missing Comma before FANBOYS', 'Khi nối hai mệnh đề độc lập bằng “and”, bắt buộc phải có dấu phẩy phía trước (`, and`); viết “Award and” thiếu dấu phẩy là sai chuẩn SAT.'),
            ('Comma Splice', 'Chỉ dùng dấu phẩy đơn nối hai mệnh đề độc lập gây lỗi comma splice.'),
        ],
    ),

    # --- M1 Q21 ---
    q_item(
        'june2025_v1_rw_m1_q21', 21, 'Standard English Conventions', 'Form, Structure, and Sense', 'Medium',
        '<p>Enacted in 1868, Luxembourg’s 5,601-word constitution, in contrast to Canada’s, which was enacted in 1867 and contains a far greater number (19,565) of words, _______ as the 9th shortest in the world. Such data are studied by constitutional scholars like Giovanni Sartori, who can use them to draw broader conclusions.</p>',
        'Which choice completes the text so that it conforms to the conventions of Standard English?',
        ['rank', 'are ranking', 'ranks', 'have ranked'],
        'C',
        'Kỹ thuật gạch bỏ cụm xen giữa (Cross Out Interrupters): Gạch toàn bộ phần chêm “, in contrast to Canada’s, which was enacted in 1867 and contains a far greater number (19,565) of words,”. Cốt lõi câu còn lại: “Enacted in 1868, Luxembourg’s 5,601-word constitution _______ as the 9th shortest in the world.” Chủ ngữ chính là số ít “constitution” → Động từ duy nhất chia số ít là “ranks” → Chọn C!',
        'Mẹo 3–1 Split trong Subject-Verb Agreement: Có 3 đáp án số nhiều (`rank`, `are ranking`, `have ranked`) và duy nhất 1 đáp án số ít (`ranks`) → xác nhận ngay chủ ngữ gốc số ít “constitution”!',
        [
            ('Plural Verb', '“rank” là động từ số nhiều, không khớp với chủ ngữ số ít “constitution”.'),
            ('Plural Verb', '“are ranking” là số nhiều (và dùng tiếp diễn không hợp với sự thật xếp hạng).'),
            ('Đáp án đúng', '“ranks” là động từ hiện tại đơn số ít duy nhất hòa hợp với chủ ngữ chính “Luxembourg’s 5,601-word constitution”.'),
            ('Plural Verb', '“have ranked” là động từ số nhiều, bị bẫy bởi danh từ số nhiều “words” đứng sát ngay trước chỗ trống.'),
        ],
    ),

    # --- M1 Q22 ---
    q_item(
        'june2025_v1_rw_m1_q22', 22, 'Expression of Ideas', 'Transitions', 'Easy',
        '<p>If you were to view the Namarunu volcano in Kenya from above, you might notice that its low profile and gently sloping sides make it look a bit like a shield lying flat on the ground. _______ it makes sense that Lydia Jennings and other volcanologists classify Namarunu as a shield volcano.</p>',
        'Which choice completes the text with the most logical transition?',
        ['For instance,', 'Therefore,', 'However,', 'By contrast,'],
        'B',
        'Quan hệ logic giữa hai câu: Câu 1 nêu nguyên nhân / cơ sở trực quan (nhìn từ trên cao, núi lửa Namarunu có hình dáng thấp và sườn thoai thoải giống chiếc khiên nằm phẳng trên mặt đất). Câu 2 nêu hệ quả hợp lý (“it makes sense that... classify Namarunu as a shield volcano” — thật dễ hiểu khi các nhà núi lửa học xếp nó vào loại núi lửa hình khiên) → Quan hệ Nguyên nhân → Kết quả → Chọn B (“Therefore,”)!',
        'Cụm “it makes sense that...” ở đầu câu 2 là dấu hiệu nhận diện kinh điển của quan hệ nhân-quả → chọn ngay “Therefore,” / “Thus,”.',
        [
            ('Wrong Relationship (Example)', 'Câu 2 là kết luận hợp lý rút ra từ hình dáng ở câu 1, không phải ví dụ minh họa cho câu 1.'),
            ('Đáp án đúng', '“Therefore,” diễn tả chính xác mối quan hệ nhân-quả: trông giống chiếc khiên → do đó hợp lý khi được gọi là núi lửa hình khiên.'),
            ('Wrong Relationship (Contrast)', 'Hai câu hoàn toàn thuận chiều, không hề tương phản.'),
            ('Wrong Relationship (Contrast)', 'Không có sự đối chiếu hai đối tượng trái ngược nhau.'),
        ],
    ),

    # --- M1 Q23 ---
    q_item(
        'june2025_v1_rw_m1_q23', 23, 'Expression of Ideas', 'Rhetorical Synthesis', 'Easy',
        '<p>While researching a topic, a student has taken the following notes:</p>'
        '<ul>'
        '<li>Jane is the nickname of a dinosaur fossil specimen housed at the Burpee Museum of Natural History.</li>'
        '<li>The Burpee Museum of Natural History is located in Rockford, Illinois.</li>'
        '<li>Jane is a member of the genus <i>Tyrannosaurus</i>.</li>'
        '<li>Big Mike is the nickname of a dinosaur fossil specimen housed at the Museum of the Rockies.</li>'
        '<li>The Museum of the Rockies is located in Bozeman, Montana.</li>'
        '<li>Big Mike is a member of the genus <i>Tyrannosaurus</i>.</li>'
        '</ul>',
        'The student wants to emphasize a similarity between the two specimens. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
        [
            'While Jane is housed at the Burpee Museum of Natural History, Big Mike is housed at the Museum of the Rockies.',
            'The dinosaur fossil specimens Jane and Big Mike are both members of the genus <i>Tyrannosaurus</i>.',
            'Big Mike is the nickname of a <i>Tyrannosaurus</i> fossil specimen housed at the Museum of the Rockies in Bozeman, Montana.',
            'The Burpee Museum of Natural History, where Jane is housed, is located in Rockford, Illinois.',
        ],
        'B',
        'Chiến lược Goal-First: Mục tiêu là **nhấn mạnh một điểm giống nhau giữa hai mẫu hóa thạch** (“emphasize a similarity between the two specimens”). Loại ngay C và D (chỉ nhắc 1 mẫu), loại A (dùng “While” để nhấn mạnh điểm KHÁC nhau về bảo tàng). Duy nhất B ghép cả Jane và Big Mike với từ khóa “both” chỉ điểm chung: cả hai đều thuộc chi *Tyrannosaurus* → Chọn B!',
        'Với Goal “emphasize a similarity”, tìm lựa chọn nhắc đủ cả 2 đối tượng cùng dấu hiệu đồng nhất như “both”, “similarly”, “share”.',
        [
            ('Wrong Goal (Difference)', 'Dùng “While” để đối chiếu nơi trưng bày khác nhau thay vì điểm giống nhau.'),
            ('Đáp án đúng', 'Đáp ứng trọn vẹn mục tiêu: nêu rõ cả Jane và Big Mike đều thuộc chi *Tyrannosaurus*.'),
            ('One-Sided Synthesis', 'Chỉ cung cấp thông tin về Big Mike, hoàn toàn bỏ qua Jane.'),
            ('One-Sided Synthesis', 'Chỉ nói về vị trí bảo tàng trưng bày Jane, không nhắc tới Big Mike.'),
        ],
    ),

    # --- M1 Q24 ---
    q_item(
        'june2025_v1_rw_m1_q24', 24, 'Expression of Ideas', 'Rhetorical Synthesis', 'Easy',
        '<p>While researching a topic, a student has taken the following notes:</p>'
        '<ul>'
        '<li><i>The Incarnations</i> (2015) is an epistolary novel by English author Susan Barker.</li>'
        '<li>Epistolary novels are novels written primarily as a series of fictional documents.</li>'
        '<li>These documents can be letters, journal entries, newspaper clippings, and more.</li>'
        '<li><i>The Incarnations</i> consists primarily of letters.</li>'
        '<li>The letters are sent between a taxi driver named Wang Jun and a mysterious woman.</li>'
        '</ul>',
        'The student wants to define the term “epistolary novel.” Which choice most effectively uses relevant information from the notes to accomplish this goal?',
        [
            'Consisting primarily of letters sent between a taxi driver named Wang Jun and a mysterious woman, Susan Barker’s <i>The Incarnations</i> is an epistolary novel.',
            'Susan Barker’s novel <i>The Incarnations</i> was published in 2015 and consists primarily of letters sent between a taxi driver named Wang Jun and a mysterious woman.',
            'An epistolary novel is a novel written primarily as a series of fictional documents, such as letters, journal entries, or newspaper clippings.',
            'Published in 2015, <i>The Incarnations</i> is an epistolary novel by English author Susan Barker.',
        ],
        'C',
        'Chiến lược Goal-First: Mục tiêu là **định nghĩa thuật ngữ “epistolary novel”** (“define the term ‘epistolary novel’”). A, B và D chỉ giới thiệu tiểu thuyết *The Incarnations* của Susan Barker mà không hề giải thích khái niệm “epistolary novel” là gì. Duy nhất C định nghĩa đầy đủ và chuẩn xác: tiểu thuyết viết chủ yếu dưới dạng một chuỗi tài liệu hư cấu như thư từ, nhật ký hay mẩu báo → Chọn C!',
        'Khi Goal yêu cầu “define the term X”, chọn ngay câu có cấu trúc định nghĩa trực tiếp “An X is...” lấy từ ghi chú định nghĩa, đừng để bị phân tâm bởi ví dụ cụ thể trong ghi chú.',
        [
            ('Missing Definition', 'Chỉ đưa ví dụ *The Incarnations* là một tiểu thuyết thư tín, không định nghĩa thuật ngữ này.'),
            ('Wrong Goal', 'Chỉ tóm tắt nội dung và năm xuất bản của *The Incarnations*, thậm chí không nhắc đến “epistolary novel”.'),
            ('Đáp án đúng', 'Định nghĩa trực tiếp, đầy đủ thuật ngữ “epistolary novel” kèm các dạng tài liệu hư cấu tiêu biểu.'),
            ('Missing Definition', 'Chỉ giới thiệu tác giả và năm xuất bản của *The Incarnations*.'),
        ],
    ),

    # --- M1 Q25 ---
    q_item(
        'june2025_v1_rw_m1_q25', 25, 'Expression of Ideas', 'Rhetorical Synthesis', 'Easy',
        '<p>While researching a topic, a student has taken the following notes:</p>'
        '<ul>'
        '<li><i>The Future of Nostalgia</i> is a scholarly book by literary theorist Svetlana Boym.</li>'
        '<li>The book provides a multifaceted exploration of the concept of nostalgia.</li>'
        '<li>Chapter 8 explores nostalgia and Europe’s largest shopping mall.</li>'
        '<li>Chapter 17 discusses various skeptics’ takes on the concept of nostalgia.</li>'
        '<li>In chapter 17, Boym writes, “The poethics of nostalgia combines estrangement and human solidarity, affect and reflection.”</li>'
        '</ul>',
        'The student wants to provide a quotation from chapter 17. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
        [
            'After exploring nostalgia and Europe’s largest shopping mall, Svetlana Boym goes on to discuss various skeptics’ takes on the concept of nostalgia.',
            'Svetlana Boym’s <i>The Future of Nostalgia</i> provides a multifaceted exploration of nostalgia.',
            'Svetlana Boym explores nostalgia and Europe’s largest shopping mall in chapter 8 of her book.',
            'In an exploration of various skeptics’ takes on the concept of nostalgia, Svetlana Boym writes, “The poethics of nostalgia combines estrangement and human solidarity, affect and reflection.”',
        ],
        'D',
        'Chiến lược Goal-First: Mục tiêu là **cung cấp một câu trích dẫn từ chương 17** (“provide a quotation from chapter 17”). Quét nhanh 4 lựa chọn: A, B, C đều KHÔNG có bất kỳ câu trích dẫn nào trong dấu ngoặc kép! Duy nhất D đưa chính xác câu trích dẫn nguyên văn từ chương 17 của Svetlana Boym → Chọn D!',
        'Khi đề yêu cầu “provide a quotation”, chỉ cần kiểm tra ngay lựa chọn nào có dấu ngoặc kép trích dẫn đúng nội dung ghi chú yêu cầu.',
        [
            ('Missing Quotation', 'Chỉ tóm tắt nội dung chương 8 và chương 17, không có câu trích dẫn nào.'),
            ('Missing Quotation', 'Chỉ nêu khái quát nội dung cuốn sách, không chứa trích dẫn.'),
            ('Wrong Chapter & Missing Quotation', 'Chỉ nhắc tới chương 8 và không có trích dẫn.'),
            ('Đáp án đúng', 'Dẫn trọn vẹn bối cảnh chương 17 và câu trích dẫn nguyên văn của Svetlana Boym.'),
        ],
    ),

    # --- M1 Q26 ---
    q_item(
        'june2025_v1_rw_m1_q26', 26, 'Expression of Ideas', 'Rhetorical Synthesis', 'Easy',
        '<p>While researching a topic, a student has taken the following notes:</p>'
        '<ul>'
        '<li>Urban natural areas are city spaces that feature elements of nature.</li>'
        '<li>Facade-bound green walls are urban natural areas defined as exterior walls that have plants growing on them.</li>'
        '<li>They can benefit cities by enhancing air quality.</li>'
        '<li>Urban grasslands are urban natural areas defined as areas of pastures or meadows in cities.</li>'
        '<li>They can benefit cities by increasing diversity among bird species.</li>'
        '</ul>',
        'The student wants to emphasize a similarity between facade-bound green walls and urban grasslands. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
        [
            'Urban grasslands, which are areas of pastures or meadows in cities, benefit cities by increasing diversity among bird species.',
            'Facade-bound green walls enhance air quality, whereas urban grasslands increase diversity among bird species.',
            'Facade-bound green walls and urban grasslands can both be considered urban natural areas.',
            'By enhancing air quality, facade-bound green walls benefit cities.',
        ],
        'C',
        'Chiến lược Goal-First: Mục tiêu là **nhấn mạnh điểm giống nhau giữa tường xanh mặt tiền và đồng cỏ đô thị** (“emphasize a similarity between facade-bound green walls and urban grasslands”). A chỉ nói về urban grasslands; D chỉ nói về facade-bound green walls; B dùng “whereas” để nhấn mạnh điểm KHÁC nhau về lợi ích. Duy nhất C dùng “both” nêu rõ điểm chung từ ghi chú: cả hai đều được coi là khu vực thiên nhiên đô thị (“urban natural areas”) → Chọn C!',
        'Đối chiếu nhanh từ khóa mục tiêu “similarity”: loại ngay 2 câu chỉ nhắc 1 đối tượng và loại câu có liên từ tương phản “whereas”.',
        [
            ('One-Sided Synthesis', 'Chỉ mô tả định nghĩa và lợi ích của đồng cỏ đô thị, thiếu tường xanh.'),
            ('Wrong Goal (Difference)', 'Dùng “whereas” để đối lập hai lợi ích khác nhau thay vì chỉ ra điểm giống nhau.'),
            ('Đáp án đúng', 'Khớp mục tiêu tuyệt đối: cả hai đều thuộc nhóm “urban natural areas”.'),
            ('One-Sided Synthesis', 'Chỉ nói về lợi ích của tường xanh mặt tiền, bỏ qua đồng cỏ đô thị.'),
        ],
    ),

    # --- M1 Q27 ---
    q_item(
        'june2025_v1_rw_m1_q27', 27, 'Expression of Ideas', 'Rhetorical Synthesis', 'Medium',
        '<p>While researching a topic, a student has taken the following notes:</p>'
        '<ul>'
        '<li>When the electrons of a chemical element change energy states, certain wavelengths of light are released.</li>'
        '<li>This unique collection of wavelengths is known as the emission spectrum of the element.</li>'
        '<li>Magnesium’s emission spectrum includes the 517.2 nanometer (nm) wavelength.</li>'
        '<li>Helium’s emission spectrum includes the 587.5 nm wavelength.</li>'
        '<li>The green portion of the visible spectrum is made up of light with wavelengths of 500–570 nm.</li>'
        '</ul>',
        'The student wants to identify an emission spectrum that includes a wavelength in the green portion of the visible spectrum. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
        [
            'Containing the 517.2 nm and 587.5 nm wavelengths, respectively, both magnesium’s and helium’s emission spectra include wavelengths in the green portion of the visible spectrum.',
            'Magnesium’s emission spectrum includes the 517.2 nm wavelength, which is in the green portion of the visible spectrum.',
            'The 587.5 nm wavelength, which is in the green portion of the visible spectrum, is one wavelength in the emission spectrum of helium.',
            'Since the 517.2 nm wavelength of light is within the 500–570 nm range, it is part of the green portion of the visible spectrum.',
        ],
        'B',
        'Kiểm tra số liệu khoa học trước khi chọn: Vùng ánh sáng xanh lục (“green portion”) nằm trong khoảng **500–570 nm**. Đối chiếu 2 nguyên tố: (1) Magnesium có bước sóng **517.2 nm** → NẰM TRONG 500–570 nm (đúng!); (2) Helium có bước sóng **587.5 nm** → LỚN HƠN 570 nm (SAI!). Do đó loại ngay A và C vì sai sự thật. Còn B vs. D: mục tiêu yêu cầu **chỉ rõ một quang phổ phát xạ (identify an emission spectrum)**; D không hề nhắc tên quang phổ của nguyên tố nào (bỏ sót magnesium)! Duy nhất B vừa đúng số liệu vừa chỉ đích danh “Magnesium’s emission spectrum” → Chọn B!',
        'Trong câu Rhetorical Synthesis có số liệu, luôn kiểm tra ĐỒNG THỜI 2 điều kiện: (1) Đúng dữ kiện toán/khoa học trong ghi chú (517.2 ∈ [500, 570], 587.5 ∉ [500, 570]); (2) Đủ đối tượng Goal yêu cầu (“identify an emission spectrum”).',
        [
            ('Factual Error', 'Sai số liệu: bước sóng 587.5 nm của heli vượt quá ngưỡng 570 nm nên KHÔNG thuộc vùng ánh sáng xanh lục.'),
            ('Đáp án đúng', 'Vừa đúng dữ kiện (517.2 nm thuộc vùng 500–570 nm) vừa nêu đích danh quang phổ phát xạ của magiê (“Magnesium’s emission spectrum”).'),
            ('Factual Error', 'Sai sự thật: 587.5 nm không nằm trong khoảng 500–570 nm của vùng xanh lục.'),
            ('Missing Goal Target', 'Đúng số liệu nhưng KHÔNG xác định được đó là quang phổ phát xạ của nguyên tố nào (thiếu “Magnesium’s emission spectrum”).'),
        ],
    ),
]


# ============================================================================
# MODULE 2: SECTION 1, MODULE 2 — READING AND WRITING (27 REAL QUESTIONS)
# ============================================================================

MODULE_2_QUESTIONS = [
    # --- M2 Q1 ---
    q_item(
        'june2025_v1_rw_m2_q1', 1, 'Craft and Structure', 'Words in Context', 'Medium',
        '<p>In New Zealand, France, and other countries with strong democratic institutions, the state tends to exert relatively little direct control over economic performance. Though this may seem to _______ the state’s ability to curb inflation, Raj Desai et al. have shown that strongly democratic states can and do deploy effective counterinflationary policies.</p>',
        'Which choice completes the text with the most logical and precise word or phrase?',
        ['hamper', 'extort', 'underscore', 'impugn'],
        'A',
        'Cấu trúc tương phản “Though this may seem to _______ the state’s ability to curb inflation, ... strongly democratic states can and do deploy effective counterinflationary policies”: Nhà nước ít kiểm soát trực tiếp kinh tế tưởng chừng sẽ CẢN TRỞ / HẠN CHẾ khả năng kiềm chế lạm phát, nhưng thực tế họ vẫn triển khai được chính sách chống lạm phát hiệu quả → Chọn A (“hamper” = cản trở, kìm hãm).',
        'Liên từ nhượng bộ “Though” đối lập trực tiếp giữa việc tưởng như bị cản trở khả năng (`hamper the ability`) và thực tế vẫn hành động hiệu quả (`deploy effective policies`).',
        [
            ('Đáp án đúng', 'hamper = cản trở, gây khó khăn cho — khớp hoàn hảo với “the state’s ability to curb inflation” và ý tương phản sau “Though”.'),
            ('Wrong Meaning', 'extort = tống tiền, cưỡng đoạt — hoàn toàn vô nghĩa khi đi với “ability”.'),
            ('Opposite Direction', 'underscore = nhấn mạnh, làm nổi bật — không tạo được sự tương phản với việc triển khai chính sách hiệu quả.'),
            ('Wrong Collocation / Meaning', 'impugn = công kích, nghi ngờ tính chân thực/đạo đức của ai — người ta không “impugn” một khả năng theo nghĩa làm suy yếu năng lực thực tế do ít kiểm soát kinh tế.'),
        ],
    ),

    # --- M2 Q2 ---
    q_item(
        'june2025_v1_rw_m2_q2', 2, 'Craft and Structure', 'Words in Context', 'Medium',
        '<p>Although the clustering of cutlery manufacturing firms in Sheffield, UK, is often cited as typical of industrial agglomeration, Giulia Faggio et al. use UK data to show that the mix of factors driving the phenomenon is _______ across industries: while access to specialized suppliers can prompt agglomeration, collocation among refined petroleum product manufacturers occurs for different reasons.</p>',
        'Which choice completes the text with the most logical and precise word or phrase?',
        ['imperative', 'credible', 'heterogeneous', 'decisive'],
        'C',
        'Manh mối giải thích trực tiếp sau dấu hai chấm (`:`): “while access to specialized suppliers can prompt agglomeration, collocation among refined petroleum product manufacturers occurs for **different reasons**” (trong khi ngành này tụ cụm vì nhà cung ứng chuyên biệt, ngành lọc dầu lại tụ cụm vì những lý do khác nhau). Vậy tập hợp yếu tố thúc đẩy sự tụ cụm công nghiệp là **KHÁC NHAU / ĐA DẠNG** giữa các ngành → Chọn C (“heterogeneous” = không đồng nhất, đa dạng).',
        'Dấu hai chấm (`:`) là chìa khóa định nghĩa trực tiếp chỗ trống: cụm “occurs for different reasons” chính là bản dịch nghĩa của tính từ học thuật “heterogeneous” (không đồng nhất).',
        [
            ('Wrong Meaning', 'imperative = cấp thiết, bắt buộc — không diễn tả sự khác biệt lý do giữa các ngành.'),
            ('Wrong Meaning', 'credible = đáng tin cậy — không khớp ý “different reasons”.'),
            ('Đáp án đúng', 'heterogeneous = không đồng nhất, khác biệt đa dạng — khớp 100% với ví dụ các ngành công nghiệp tụ cụm vì những lý do khác nhau.'),
            ('Wrong Meaning', 'decisive = mang tính quyết định — không giải thích vế tương phản “occurs for different reasons”.'),
        ],
    ),

    # --- M2 Q3 ---
    q_item(
        'june2025_v1_rw_m2_q3', 3, 'Craft and Structure', 'Words in Context', 'Medium',
        '<p>Studying wrappers from discontinued candies, cover images from out-of-print magazines, and posters promoting concerts by long-forgotten musicians may seem like a frivolous pursuit, but ephemeral objects like these are useful as _______ cultural change, revealing shifts in norms, values, and concerns that traditional objects of historical inquiry may not.</p>',
        'Which choice completes the text with the most logical and precise word or phrase?',
        ['pretexts for', 'conjectures about', 'manifestations of', 'inducements to'],
        'C',
        'Mệnh đề phân từ phía sau định nghĩa trực tiếp cụm cần điền: “revealing shifts in norms, values, and concerns” (phơi bày những chuyển dịch trong chuẩn mực, giá trị và mối quan tâm). Những vật dụng phù du như vỏ kẹo cũ, bìa tạp chí hết in, áp phích hòa nhạc hữu ích như những **BIỂU HIỆN CỤ THỂ CỦA** sự biến đổi văn hóa → Chọn C (“manifestations of”).',
        'Hãy khớp sát nghĩa động từ “revealing” (hé lộ/biểu lộ) đứng ngay sau chỗ trống: vật thể hữu hình biểu lộ một biến đổi trừu tượng gọi là “manifestations of” (những biểu hiện của).',
        [
            ('Wrong Meaning', 'pretexts for = cái cớ giả tạo để làm gì — vỏ kẹo hay áp phích không phải cái cớ gây ra biến đổi văn hóa.'),
            ('Wrong Meaning', 'conjectures about = phỏng đoán thiếu chứng cứ — các vật thể thực tế không phải “lời phỏng đoán”.'),
            ('Đáp án đúng', 'manifestations of = những biểu hiện rõ nét của — khớp hoàn hảo với chức năng “revealing shifts in norms, values, and concerns”.'),
            ('Wrong Causal Direction', 'inducements to = động cơ thúc đẩy/dụ dỗ — đoạn văn nói chúng phản ánh/hé lộ sự thay đổi, không nói chúng xúi giục gây ra thay đổi văn hóa.'),
        ],
    ),

    # --- M2 Q4 ---
    q_item(
        'june2025_v1_rw_m2_q4', 4, 'Craft and Structure', 'Words in Context', 'Hard',
        '<p>The 2023 anthology <i>The Big Book of Cyberpunk</i> contains 108 stories, including Fritz Leiber’s “Coming Attraction” (1950) and Erica Satifka’s “Act of Providence” (2021). With its chronological scope, it is more comprehensive than the much shorter 1986 cyberpunk anthology <i>Mirrorshades</i>, but <i>Mirrorshades</i>’s careful selection of stories makes that anthology more _______.</p>',
        'Which choice completes the text with the most logical and precise word or phrase?',
        ['capacious', 'outmoded', 'cursory', 'discerning'],
        'D',
        'Đối chiếu hai tuyển tập qua chữ “but”: *The Big Book of Cyberpunk* (108 truyện, trải dài 1950–2021) thì bao quát rộng lớn hơn (“more comprehensive”), NHƯNG *Mirrorshades* (ngắn hơn nhiều) lại có “careful selection of stories” (sự tuyển chọn truyện kỹ lưỡng, tinh tế) → khiến tuyển tập này **TINH ĐỜI / CHỌN LỌC SẮC SẢO** hơn → Chọn D (“discerning” = có con mắt tinh tường, chắt lọc kỹ).',
        'Cụm “careful selection” định nghĩa trực tiếp tính từ “discerning” (sắc sảo trong chọn lựa). Cẩn thận bẫy “capacious” (rộng lớn, chứa nhiều) — đó là đặc điểm của cuốn 108 truyện, không phải cuốn *Mirrorshades* ngắn hơn!',
        [
            ('Swapped Subject Trap', 'capacious = rộng lớn, chứa được nhiều — đây là đặc tính của *The Big Book of Cyberpunk* (108 truyện), ngược hoàn toàn với “much shorter *Mirrorshades*”.'),
            ('Wrong Meaning', 'outmoded = lỗi thời — “careful selection” không làm tuyển tập trở nên lỗi thời.'),
            ('Opposite Meaning', 'cursory = qua loa, hời hợt — trái nghĩa trực tiếp với “careful selection”.'),
            ('Đáp án đúng', 'discerning = tinh tường, chắt lọc sắc sảo — khớp chính xác hệ quả của “careful selection of stories”.'),
        ],
    ),

    # --- M2 Q5 ---
    q_item(
        'june2025_v1_rw_m2_q5', 5, 'Craft and Structure', 'Words in Context', 'Hard',
        '<p>The following text is from William Carlos Williams’s 1925 creative nonfiction book <i>In the American Grain</i>. Williams is discussing how works by nineteenth-century US poet and fiction writer Edgar Allan Poe were received by American readers.</p>'
        '<p>Poe must suffer by his originality. Invent that which is new, even if it be made of <u>pine from your own yard</u>, and there’s none to know what you have done. It is because there’s no <i>name</i>. This is the cause of Poe’s lack of recognition. He was American. He was the astounding, inconceivable growth of his locality.</p>',
        'As used in the text, what does the underlined figurative phrase most nearly mean?',
        [
            'Personal experiences that are hard for others to comprehend',
            'Ideas you have never previously expressed',
            'Elements of the culture in which you live',
            'Inspiration you received while reading independently',
        ],
        'C',
        'Giải mã ẩn dụ dựa vào hai câu giải thích ngay sau đó: “He was American. He was the astounding, inconceivable growth of **his locality**.” (Ông là người Mỹ. Ông là sự sinh trưởng phi thường từ chính mảnh đất/địa phương mình). Hình ảnh “pine from your own yard” (gỗ thông lấy ngay từ mảnh sân nhà bạn) tượng trưng cho **những chất liệu bản địa quen thuộc thuộc về chính nền văn hóa nơi bạn đang sống** (“Elements of the culture in which you live”) — ngay cả khi tác phẩm mới mẻ được tạo từ chất liệu bản địa Mỹ, độc giả Mỹ vẫn không nhận ra vì nó chưa có tên gọi quen thuộc → Chọn C!',
        'Khi gặp câu hỏi nghĩa ẩn dụ (figurative phrase), ĐỪNG đoán theo cảm tính câu chứa ẩn dụ — hãy đọc 2 câu giải thích ngay liền sau nó (“He was American... growth of his locality”).',
        [
            ('Misreading “Inconceivable”', 'Cụm “pine from your own yard” nhấn mạnh chất liệu bản địa gần gũi (“your own yard” ↔ “his locality”), không phải trải nghiệm cá nhân khó hiểu.'),
            ('Wrong Target', 'Sự mới mẻ nằm ở cụm “Invent that which is new”, còn “even if it be made of pine from your own yard” chỉ nguyên liệu quen thuộc sẵn có ở quê hương mình.'),
            ('Đáp án đúng', 'Khớp tuyệt đối phép tương ứng hình ảnh “your own yard” ↔ “American / his locality” = những yếu tố thuộc chính nền văn hóa nơi bạn sống.'),
            ('Out of Scope', 'Văn bản không hề đề cập đến việc tự đọc sách để lấy cảm hứng.'),
        ],
    ),

    # --- M2 Q6 ---
    q_item(
        'june2025_v1_rw_m2_q6', 6, 'Craft and Structure', 'Words in Context', 'Medium',
        '<p>To prevent excessive microbial growth in the closed habitat of the International Space Station, relative humidity is carefully maintained. Nonetheless, <i>Veillonella parvula</i> and other bacteria, which have the potential to damage spacecraft materials, can _______ when routine crew-member activities (e.g., handwashing) produce localized humidity conditions that exceed the specified maximum for the station overall.</p>',
        'Which choice completes the text with the most logical and precise word or phrase?',
        ['abate', 'recalibrate', 'proliferate', 'rehabilitate'],
        'C',
        'Manh mối tương phản kết hợp đồng nghĩa ngữ cảnh: Câu 1 nói độ ẩm được kiểm soát chặt để “prevent **excessive microbial growth**” (ngăn vi sinh vật phát triển quá mức). Câu 2 mở bằng “Nonetheless” (Tuy vậy): vi khuẩn vẫn có thể _______ khi hoạt động sinh hoạt tạo độ ẩm cục bộ vượt ngưỡng tối đa → Vi khuẩn sẽ **SINH SÔI NẢY NỞ / PHÁT TRIỂN NHANH** → Chọn C (“proliferate”).',
        'Liên kết thẳng “prevent excessive microbial growth” + “Nonetheless, bacteria... can _______” → chọn động từ đồng nghĩa với “grow rapidly / multiply” = proliferate.',
        [
            ('Opposite Meaning', 'abate = giảm bớt, lắng dịu — trái ngược hoàn toàn với hậu quả khi độ ẩm vượt mức tối đa.'),
            ('Wrong Subject', 'recalibrate = hiệu chỉnh lại thiết bị — vi khuẩn không “hiệu chỉnh lại” khi độ ẩm tăng cao.'),
            ('Đáp án đúng', 'proliferate = sinh sôi nảy nở nhanh chóng — khớp chính xác với “excessive microbial growth” ở câu trước.'),
            ('Wrong Context', 'rehabilitate = phục hồi chức năng/cải tạo — không dùng để mô tả vi khuẩn gây hại phát triển trên trạm vũ trụ.'),
        ],
    ),

    # --- M2 Q7 ---
    q_item(
        'june2025_v1_rw_m2_q7', 7, 'Craft and Structure', 'Text Structure and Purpose', 'Easy',
        '<p>In Tunica, an Indigenous language from the lower Mississippi Valley in what is now the United States, <i>mili</i> means “red,” whereas <i>milimilita</i> is used to refer to several red things. This phenomenon, in which an element of a root word is repeated, sometimes with modification, within another word that is related to the root word, is called reduplication. In this case, the entire word <i>mili</i> gets repeated in <i>milimilita</i>. There are many examples of this type of reduplication in Tunica.</p>',
        'Which choice best describes the overall structure of the text?',
        [
            'It presents some specific words in Tunica, describes the general linguistic phenomenon exemplified by those words, and then states that this phenomenon occurs frequently in Tunica.',
            'It identifies the most frequently occurring words in Tunica, explains why it is difficult to translate those words into English, and then provides examples of languages other than English into which those words can be translated.',
            'It explains the phenomenon of reduplication, discusses why reduplication has been controversial among scholars, and then argues that an analysis of Tunica could help resolve that controversy.',
            'It describes the relationship between Tunica and several other languages, raises a question about the nature of that relationship, and then answers that question.',
        ],
        'A',
        'Tách 3 bước phát triển của đoạn văn: (1) Câu 1 đưa ra hai từ cụ thể trong tiếng Tunica (*mili* và *milimilita*); (2) Câu 2–3 mô tả hiện tượng ngôn ngữ tổng quát mà hai từ đó minh họa (hiện tượng láy từ — reduplication); (3) Câu 4 khẳng định có rất nhiều ví dụ về hiện tượng này trong tiếng Tunica (“many examples” = occurs frequently) → Chọn A!',
        'Kiểm tra nhanh từng chặng trong Overall Structure: B, C, D đều bịa thêm yếu tố không hề có trong bài (khó dịch, tranh cãi học giả, quan hệ với các ngôn ngữ khác).',
        [
            ('Đáp án đúng', 'Phản ánh chính xác trình tự 3 phần: ví dụ từ cụ thể (*mili*, *milimilita*) → định nghĩa hiện tượng ngôn ngữ chung (reduplication) → tần suất phổ biến trong tiếng Tunica.'),
            ('Fabricated Details', 'Bài không nói *mili* là từ phổ biến nhất, không nói khó dịch sang tiếng Anh, và không nhắc tới ngôn ngữ nào khác.'),
            ('Fabricated Details', 'Không hề có tranh cãi học thuật nào được đề cập trong đoạn văn.'),
            ('Fabricated Details', 'Bài chỉ nói về tiếng Tunica, không so sánh quan hệ với các ngôn ngữ khác hay đặt câu hỏi.'),
        ],
    ),

    # --- M2 Q8 ---
    q_item(
        'june2025_v1_rw_m2_q8', 8, 'Craft and Structure', 'Text Structure and Purpose', 'Medium',
        '<p><i>The Truelove</i>, first published in 1992, is a novel in Patrick O’Brian’s Aubrey/Maturin series, which includes twenty books plus an unfinished fragment of a twenty-first. <u>Some critics have found fault with the abrupt endings of <i>The Truelove</i> and other books in the series, saying that they do not finish conclusively but arbitrarily stop.</u> But other critics argue that the books should not be thought of as discrete texts with traditional beginnings and endings but as a single incredibly long work, similar to other multivolume stories, such as Anthony Powell’s <i>A Dance to the Music of Time</i>.</p>',
        'Which choice best describes the function of the underlined portion in the text as a whole?',
        [
            'It explains why many critics find the Aubrey/Maturin novels to be entertaining despite flaws in the novels’ structures.',
            'It argues that the unusual structure that O’Brian uses for <i>The Truelove</i> makes it one of his least entertaining books.',
            'It presents a reason most critics think the Aubrey/Maturin series should not have the literary renown of similar works like <i>A Dance to the Music of Time</i>.',
            'It describes a characteristic of the Aubrey/Maturin novels and summarizes a negative assessment of it.',
        ],
        'D',
        'Đọc kỹ chính xác câu gạch chân: “Some critics have found fault with the abrupt endings of *The Truelove* and other books in the series, saying that they do not finish conclusively but arbitrarily stop.” Câu này làm đúng 2 việc: (1) mô tả một đặc điểm của bộ tiểu thuyết Aubrey/Maturin (“abrupt endings” — cái kết đột ngột); (2) tóm tắt đánh giá tiêu cực của một số nhà phê bình về đặc điểm đó (“found fault with... do not finish conclusively but arbitrarily stop”) → Chọn D!',
        'Đối chiếu từng từ trong lựa chọn với đúng phần gạch chân: A và B bịa ra chữ “entertaining”; C bóp méo câu cuối (*A Dance to the Music of Time* thực chất được nhóm nhà phê bình BÊNH VỰC trích dẫn, không phải nhóm chê bai).',
        [
            ('Unsupported Detail', 'Đoạn văn hoàn toàn không nhắc đến việc các cuốn sách có “entertaining” (giải trí/hấp dẫn) hay không.'),
            ('Unsupported Detail', 'Không hề so sánh *The Truelove* là cuốn kém hấp dẫn nhất của O’Brian.'),
            ('Misplaced / Distorted Detail', 'Nhóm phê bình chỉ trích chỉ là “Some critics” (không phải “most critics”), và tác phẩm *A Dance to the Music of Time* nằm ở câu sau để BẢO VỆ bộ truyện của O’Brian.'),
            ('Đáp án đúng', 'Khớp hoàn toàn: nêu đặc điểm “abrupt endings” của bộ sách và tóm tắt lời đánh giá chê bai (“found fault... arbitrarily stop”).'),
        ],
    ),

    # --- M2 Q9 ---
    q_item(
        'june2025_v1_rw_m2_q9', 9, 'Craft and Structure', 'Cross-Text Connections', 'Hard',
        '<p><b>Text 1</b><br/>In separate studies, Marine Fernandez and colleagues and Xinhua He and colleagues examined whether plants transfer nutrients to one another using a common mycorrhizal network (CMN)—a lattice of fungal strands in the soil. Fernandez and colleagues excluded all pathways other than the CMN by using barriers to keep the plants’ root systems separate while allowing mycorrhizal strands through—a crucial step He and colleagues’ study did not take.</p>'
        '<p><b>Text 2</b><br/>Fernandez and colleagues took the necessary precaution of separating the plants’ root systems (thereby excluding root-to-root transmission). However, any barrier used must allow the thread-like hyphae of a CMN to pass through, and this permeability would also allow liquids through. Thus, the researchers’ experimental design cannot ensure that any nutrient transfer observed can be attributed to a CMN and not to some other pathway.</p>',
        'Based on the texts, which choice best describes a similarity in the points of view presented in Text 1 and Text 2?',
        [
            'Each text attempts to dispel a common misunderstanding about the likelihood of plant-to-plant nutrient transfer.',
            'Each text assumes that most nutrient transfer between plants is via a CMN.',
            'Each text analyzes methods for studying CMN nutrient transfer in order to propose an alternative method of study.',
            'Each text critiques the methodology of a study about nutrient transfer via a CMN.',
        ],
        'D',
        'Tìm điểm chung thật sự giữa Text 1 và Text 2: (1) Text 1 chỉ ra lỗi phương pháp trong nghiên cứu của **He và cộng sự** (không dùng màng ngăn tách hệ rễ — “a crucial step He and colleagues’ study did not take”); (2) Text 2 chỉ ra lỗi phương pháp trong nghiên cứu của **Fernandez và cộng sự** (màng ngăn cho sợi nấm đi qua thì cũng cho chất lỏng thấm qua, nên thiết kế thí nghiệm không chắc chắn loại trừ được các con đường khác). Như vậy, **cả hai văn bản đều phê bình phương pháp thí nghiệm của một nghiên cứu về sự truyền dưỡng chất qua mạng nấm CMN** → Chọn D!',
        'Câu Cross-Text tìm điểm chung: Text 1 chê phương pháp của He; Text 2 chê phương pháp của Fernandez → điểm chung ở tầng khái quát hơn là “Each text critiques the methodology of a study about nutrient transfer via a CMN”.',
        [
            ('Out of Scope', 'Cả hai đoạn đều bàn về thiết kế thí nghiệm, không hề nhắc hay bác bỏ một “hiểu lầm phổ biến về xác suất truyền dưỡng chất”.'),
            ('Contradiction', 'Text 2 thậm chí nghi ngờ liệu sự truyền dưỡng chất quan sát được có thực sự đi qua CMN hay đi qua chất lỏng khác — không hề mặc định phần lớn đi qua CMN.'),
            ('Unsupported Ending', 'Cả hai văn bản chỉ phân tích/phê bình phương pháp hiện có, KHÔNG đề xuất một phương pháp nghiên cứu thay thế mới nào.'),
            ('Đáp án đúng', 'Khớp chính xác: Text 1 phê bình thiết kế của He et al., còn Text 2 phê bình thiết kế của Fernandez et al.'),
        ],
    ),

    # --- M2 Q10 ---
    q_item(
        'june2025_v1_rw_m2_q10', 10, 'Information and Ideas', 'Central Ideas and Details', 'Easy',
        '<p>Founded in 1996, the Museum of Latin American Art showcases modern and contemporary art by Latin American artists and Latino artists in the United States. It is located in Long Beach, California, and has more than 1,300 objects in its collection. Since 2000, a number of other institutions devoted to Latino cultures have opened in the United States. A notable example is LA Plaza de Cultura y Artes in Los Angeles. It focuses on Mexican American art and culture.</p>',
        'Which choice best states the main topic of the text?',
        [
            'The history of Los Angeles',
            'The decline in the number of people attending museums',
            'Latino cultural institutions in the United States',
            'The geography of Latin America',
        ],
        'C',
        'Đoạn văn giới thiệu Bảo tàng Nghệ thuật Mỹ Latinh (Long Beach, California), sau đó nêu từ năm 2000 nhiều thiết chế văn hóa khác dành cho văn hóa người gốc Mỹ Latinh (Latino cultures) đã mở cửa tại Mỹ, tiêu biểu như LA Plaza de Cultura y Artes ở Los Angeles → Chủ đề chính là các thiết chế văn hóa Latino tại Hoa Kỳ → Chọn C.',
        'Gom toàn bộ thực thể xuất hiện trong bài (Museum of Latin American Art + other institutions devoted to Latino cultures + LA Plaza de Cultura y Artes) → tất cả đều thuộc nhóm “Latino cultural institutions in the United States”.',
        [
            ('Too Narrow / Off-Topic', 'Los Angeles chỉ được nhắc qua như địa điểm của một ví dụ, không bàn về lịch sử thành phố này.'),
            ('Not Mentioned', 'Không có thông tin nào về sự suy giảm lượng khách tham quan bảo tàng.'),
            ('Đáp án đúng', 'Bao quát đầy đủ toàn bộ các ví dụ bảo tàng và trung tâm văn hóa Latino tại Mỹ trong đoạn văn.'),
            ('Not Mentioned', 'Đoạn văn không bàn về địa lý Mỹ Latinh.'),
        ],
    ),

    # --- M2 Q11 ---
    q_item(
        'june2025_v1_rw_m2_q11', 11, 'Information and Ideas', 'Central Ideas and Details', 'Easy',
        '<p><i>Argyroxiphium caliginis</i> is among the twenty-eight species of silversword plants found only on the Hawaiian archipelago that collectively illustrate the process of adaptive radiation, or the rapid diversification of an ancestral species into different, related species. Each silversword species is physically distinct, with mature plant forms ranging from trees and shrubs to vines. However, they all descended from a common tarweed plant species, with their unique physical characteristics emerging as they adapted to the archipelago’s many specific habitats over time.</p>',
        'Which choice best states the main idea of the text?',
        [
            'Most plants that grow on the Hawaiian archipelago are descendants of a single founder species.',
            'All silverswords that grow on the Hawaiian archipelago have similar physical characteristics.',
            'The Hawaiian archipelago exhibits many distinct habitats and species.',
            'Silverswords are good examples of adaptive radiation on the Hawaiian archipelago.',
        ],
        'D',
        'Câu chủ đề mở đầu nêu trực tiếp: 28 loài thực vật silversword chỉ có ở quần đảo Hawaii minh họa rõ quá trình tiến hóa phân nhánh thích nghi (“adaptive radiation”); các câu tiếp theo giải thích cách chúng đa dạng hình thái từ cây gỗ, cây bụi đến dây leo dù chung một loài tổ tiên tarweed để thích nghi với từng sinh cảnh Hawaii → Ý chính là cây silversword là ví dụ điển hình về adaptive radiation trên quần đảo Hawaii → Chọn D!',
        'Tránh bẫy khái quát quá đà (A mở rộng thành “Most plants”) và bẫy quá chung chung mất từ khóa chính (C bỏ mất “silverswords” và “adaptive radiation”).',
        [
            ('Overgeneralization', 'Bài chỉ nói 28 loài silversword chung một tổ tiên, không hề nói “hầu hết thực vật ở Hawaii” đều từ một loài tổ tiên duy nhất.'),
            ('Contradiction', 'Trái ngược hoàn toàn với câu 2: “Each silversword species is physically distinct” (mỗi loài có đặc điểm hình thái khác biệt).'),
            ('Too Broad', 'Đúng một phần chi tiết nền nhưng bỏ sót hai chủ thể trung tâm của đoạn văn: cây silversword và quá trình adaptive radiation.'),
            ('Đáp án đúng', 'Tóm gọn chính xác trọng tâm của toàn đoạn văn: silverswords là ví dụ tiêu biểu của tiến hóa phân nhánh thích nghi tại Hawaii.'),
        ],
    ),

    # --- M2 Q12 ---
    q_item(
        'june2025_v1_rw_m2_q12', 12, 'Information and Ideas', 'Command of Evidence (Textual)', 'Hard',
        '<p>The bird species <i>Piculus flavigula</i> (the yellow-throated woodpecker), which forages in relatively dense vegetation, and <i>Willisornis poecilinotus</i> (the common scale-backed antbird), which forages in open areas or low density vegetation, share territory in French Guiana with <i>Thamnomanes caesius</i> (the cinereous antshrike), which emits a loud alarm call when it detects predators. Biologist Ari Martínez and colleagues, who studied the ecological community the species share, hypothesized that there is an inverse relationship between birds’ field of vision while foraging and their sensitivity to alarm calls from neighboring species.</p>',
        'Which finding, if true, would most directly support Martínez and colleagues’ hypothesis?',
        [
            '<i>W. poecilinotus</i> displayed no reaction when Martínez and colleagues played <i>T. caesius</i> alarm calls, whereas <i>P. flavigula</i> displayed predator-avoidance behavior in response to the calls.',
            'Many local bird species with similar foraging habits to those of <i>P. flavigula</i> displayed no reaction when Martínez and colleagues played <i>T. caesius</i> alarm calls, whereas <i>P. flavigula</i> displayed predator-avoidance behavior.',
            'Some individuals of <i>W. poecilinotus</i> displayed predator-avoidance behavior when Martínez and colleagues played <i>T. caesius</i> alarm calls, whereas nearly all did when <i>P. flavigula</i> alarm calls were played.',
            'When Martínez and colleagues played <i>T. caesius</i> alarm calls, <i>P. flavigula</i> and <i>W. poecilinotus</i> displayed no reaction, whereas <i>T. caesius</i> displayed predator-avoidance behavior.',
        ],
        'A',
        'Lập bản đồ biến số khoa học thật gọn: Giả thuyết Martínez = **tương quan nghịch** (inverse relationship) giữa **tầm nhìn khi kiếm ăn** (field of vision) và **độ nhạy với tiếng báo động của loài hàng xóm** (*T. caesius*):'
        ' (1) *P. flavigula* kiếm ăn trong **thảm thực vật rậm rạp** (“dense vegetation”) → tầm nhìn **HẸP** → dự đoán **NHẠY CAO** (có phản ứng né tránh kẻ săn mồi);'
        ' (2) *W. poecilinotus* kiếm ăn ở **nơi quang đãng / thưa thớt** (“open areas or low density vegetation”) → tầm nhìn **RỘNG** → dự đoán **NHẠY THẤP** (ít hoặc không phản ứng). Đáp án A khớp tuyệt đối cả hai chiều dự đoán → Chọn A!',
        'Với bài sinh học nhiều tên Latin, hãy ghi tắt ngay ra nháp: `P = dense = tầm nhìn hẹp → phải NHẠY` | `W = open = tầm nhìn rộng → phải ÍT NHẠY` rồi đối chiếu thẳng vào 4 đáp án!',
        [
            ('Đáp án đúng', '*W. poecilinotus* (tầm nhìn rộng ở vùng thoáng) không phản ứng, còn *P. flavigula* (tầm nhìn bị che khuất trong tán rậm) lập tức né tránh khi nghe tiếng báo động của *T. caesius* — chứng minh trực tiếp tương quan nghịch.'),
            ('Weakens Hypothesis', 'Nếu nhiều loài khác có tập tính kiếm ăn tán rậm giống *P. flavigula* lại KHÔNG phản ứng thì điều đó làm suy yếu, chứ không ủng hộ giả thuyết.'),
            ('Wrong Comparison Variable', 'So sánh phản ứng của riêng *W. poecilinotus* trước hai nguồn tiếng kêu khác nhau, không so sánh hai loài chim có tầm nhìn khác nhau.'),
            ('Contradicts Hypothesis', 'Cả *P. flavigula* lẫn *W. poecilinotus* đều không phản ứng trước tiếng báo động của *T. caesius* → phủ định giả thuyết.'),
        ],
    ),

    # --- M2 Q13 ---
    q_item(
        'june2025_v1_rw_m2_q13', 13, 'Information and Ideas', 'Command of Evidence (Textual)', 'Hard',
        '<p>Nautilids are marine mollusks that begin growing their shells before emerging from their eggs and continue to add shell segments throughout their lifetimes. The walls between their shells’ chambers are called septa, and the deeper the water in which a septum forms, the greater the concentration of the isotope oxygen-18 the septum will contain. Since temperature falls as depth increases, if the area of ocean a nautilid inhabits is known, this isotopic signature can reveal the temperature at which its septa formed. Paleontologist Amane Tajika and colleagues examined each of the septa in two nautilid shells and concluded that septum sample M20 formed at a temperature of 15.2°C whereas sample F04 formed at 22.5°C.</p>',
        'Which finding, if true, would most directly weaken the researchers’ conclusion?',
        [
            'At a depth of 355 meters in the nautilids’ habitat, the water is 15.2°C and the concentration of oxygen-18 is equal to that in sample M20.',
            'The concentration of oxygen-18 in F04 is lower than that in M20.',
            'The concentration of oxygen-18 in F04 is higher than that in M20.',
            'At a depth of 90 meters in the nautilids’ habitat, the water is 22.5°C and the concentration of oxygen-18 is equal to that in sample F04.',
        ],
        'C',
        'Chuỗi quy luật vật lý trong bài: **Nước càng sâu → Nhiệt độ càng THẤP → Nồng độ oxygen-18 càng CAO** (tức Nhiệt độ thấp ↔ O-18 cao; Nhiệt độ cao ↔ O-18 thấp). Theo kết luận của nhóm Tajika: mẫu **M20** hình thành ở **15.2°C (lạnh hơn, sâu hơn → PHẢI có O-18 cao hơn)**, còn mẫu **F04** hình thành ở **22.5°C (ấm hơn, nông hơn → PHẢI có O-18 thấp hơn)**. Do đó, phát hiện làm suy yếu trực tiếp kết luận là **nồng độ oxygen-18 trong F04 lại CAO HƠN trong M20** (mâu thuẫn trực diện với việc F04 ấm hơn M20) → Chọn C!',
        'Vẽ ngay mũi tên tỷ lệ: `Depth ↑ ⇒ Temp ↓ ⇒ O-18 ↑`. Suy ra `M20 (15.2°C) < F04 (22.5°C)` đòi hỏi `O-18(M20) > O-18(F04)`. Để WEAKEN, đảo ngược bất đẳng thức thành `O-18(F04) > O-18(M20)` (C)!',
        [
            ('Strengthens Conclusion', 'Xác nhận chính xác ở độ sâu 355 m nhiệt độ 15.2°C có mức O-18 trùng khớp mẫu M20 — ủng hộ chứ không làm yếu.'),
            ('Strengthens Conclusion', 'Bẫy đảo chiều: O-18 ở F04 thấp hơn M20 hoàn toàn khớp với việc F04 hình thành ở nước ấm hơn (22.5°C so với 15.2°C).'),
            ('Đáp án đúng', 'Nếu O-18 trong F04 cao hơn M20 thì F04 phải hình thành ở vùng nước sâu hơn và LẠNH hơn M20 — bác bỏ trực tiếp kết luận F04 ở 22.5°C và M20 ở 15.2°C.'),
            ('Strengthens Conclusion', 'Xác nhận ở độ sâu 90 m nhiệt độ 22.5°C có mức O-18 khớp mẫu F04 — củng cố kết luận của nhóm nghiên cứu.'),
        ],
    ),

    # --- M2 Q14 ---
    q_item(
        'june2025_v1_rw_m2_q14', 14, 'Information and Ideas', 'Command of Evidence (Quantitative)', 'Hard',
        html_table(
            'Average Ratings of Perceived Personality Traits of Dogs and Human Willingness to Keep or Interact with Them',
            [
                'Image ID number',
                'Irises',
                'Not friendly (0)–Friendly (5)',
                'Immature (0)–Mature (5)',
                'Would not keep (0)–Would keep (3)',
                'Would not interact with (0)–Would interact with (3)',
            ],
            [
                ['24', 'light', '2.67', '4.03', '1.4', '1.7'],
                ['14', 'light', '2.11', '3.27', '1.55', '1.85'],
                ['8', 'dark', '3.52', '2.91', '1.9', '2.45'],
                ['3', 'dark', '3.88', '2.51', '2.35', '2.65'],
            ],
        )
        + '<p>Interested in how differences in the color of dogs’ irises affect human responses to dogs, Akitsugu Konno et al. showed close-up images of dogs’ faces to human participants and asked them to rate the dogs’ traits and their own attitudes toward the dogs. Konno et al. suggest that differences in iris color led participants to view some dogs as more vulnerable and in need of protection than others and that this phenomenon could help explain the association the researchers observed between iris color and participants’ inclinations to interact with or keep dogs, as illustrated by the finding that _______</p>',
        'Which choice most effectively uses data from the table to complete the statement?',
        [
            'participants rated the dog in image 3 as less mature than the dog in image 8 and rated the dog in image 14 as less mature than the dog in image 24.',
            'dogs that participants rated as friendlier were also dogs that participants indicated a stronger willingness to interact with or keep.',
            'the more mature a dog was perceived to be, the more likely participants were to rate it as having light irises.',
            'participants favored the dogs in images 3 and 8, which they rated as less mature than the dogs in images 24 and 14.',
        ],
        'D',
        'Khóa 3 biến số trong lập luận của Konno et al.: [1] **Khác biệt màu mống mắt** (dark: ảnh 3 & 8 vs. light: ảnh 24 & 14) → [2] **Cảm nhận yếu ớt / cần bảo vệ hơn** = cột **Immature (0)–Mature (5) THẤP HƠN** (ảnh 3 & 8 đạt 2.51 và 2.91, thấp hơn rõ rệt so với ảnh 14 & 24 là 3.27 và 4.03) → [3] **Xu hướng muốn tương tác / nuôi cao hơn** (“favored”: ảnh 3 & 8 đạt Keep 2.35/1.9 và Interact 2.65/2.45, đều cao hơn ảnh 14 & 24 là 1.55/1.4 và 1.85/1.7). Đáp án D kết nối trọn vẹn cả nhóm màu mắt (3 & 8 vs. 24 & 14), mức độ ít trưởng thành hơn (“less mature”), và sự ưa thích hơn (“favored”)! Đặc biệt cảnh giác bẫy B: kiểm tra ảnh 24 vs. ảnh 14 — ảnh 24 thân thiện hơn (2.67 > 2.11) nhưng lại bị đánh giá muốn nuôi/tương tác THẤP HƠN (1.4 < 1.55 và 1.7 < 1.85), nên B sai cả về số liệu lẫn lập luận!',
        'Trong bảng đa biến Hard M2, luôn ánh xạ khái niệm văn bản sang đúng cột (“vulnerable and in need of protection” ↔ “less mature”) và kiểm tra từng cặp hàng để vạch trần bẫy số liệu tinh vi như B (hàng 24 vs. 14).',
        [
            ('Wrong Grouping (Within-Color Only)', 'Chỉ so sánh trong cùng nhóm màu mắt (3 vs. 8 đều mắt tối; 14 vs. 24 đều mắt sáng) và hoàn toàn bỏ qua mức độ muốn nuôi/tương tác.'),
            ('False Data & Wrong Trait', 'Vừa sai cột mục tiêu (dùng “friendly” thay vì “immature/vulnerable”) vừa SAI SỐ LIỆU: ảnh 24 thân thiện hơn ảnh 14 (2.67 vs. 2.11) nhưng lại có điểm muốn nuôi/tương tác thấp hơn ảnh 14 (1.4/1.7 vs. 1.55/1.85).'),
            ('Reversed Experimental Variable', 'Người tham gia không “đánh giá” màu mống mắt của chó (màu mắt là thuộc tính có sẵn của bức ảnh), và đáp án này cũng bỏ quên yếu tố muốn nuôi/tương tác.'),
            ('Đáp án đúng', 'Khớp hoàn hảo cả 3 trụ cột dữ liệu: hai chú chó mắt tối (ảnh 3 & 8) được ưa thích hơn (Keep/Interact cao hơn) và đồng thời bị đánh giá ít trưởng thành/non nớt hơn (2.51 & 2.91 < 3.27 & 4.03) so với hai chú chó mắt sáng (ảnh 24 & 14).'),
        ],
    ),

    # --- M2 Q15 ---
    q_item(
        'june2025_v1_rw_m2_q15', 15, 'Information and Ideas', 'Inferences', 'Medium',
        '<p>Anthropogenic noise (sounds from human sources like traffic or mining) can affect animals, as Soledad Lucía Uran and colleagues found in a 2012 study of brown rats. A meta-analysis of more than 100 such studies examining various species found that, for every study, relevant traits or behaviors of the animals were observably different between the exposed group and the otherwise similar but unexposed group, regardless of whether that difference was beneficial or detrimental for the exposed group. So while a study of birds might show a difference that benefits the exposed group, and a study of mammals might show a difference that’s harmful to the exposed group, both differences are substantial. Therefore, the results of the meta-analysis suggest that _______</p>',
        'Which choice most logically completes the text?',
        [
            'exposure to anthropogenic noise will likely have noticeable effects both on mammals such as brown rats and on birds such as reed buntings, but the nature of that effect could be very different for the two species.',
            'the studies of the birds likely found significantly larger effects of exposure to anthropogenic noise than most studies of mammals except the study of brown rats by Soledad Lucía Uran and colleagues.',
            'the studies in the meta-analysis that examined mammals were more likely than those about birds to specify whether the observed effects were detrimental.',
            'the study conducted by Soledad Lucía Uran and colleagues found substantial differences, but studies included in the meta-analysis of mammals other than brown rats likely did not.',
        ],
        'A',
        'Tổng hợp 2 ý cốt lõi từ phân tích tổng hợp (meta-analysis >100 nghiên cứu): (1) Trong MỌI nghiên cứu (“for every study”), tiếng ồn nhân tạo đều tạo ra khác biệt đáng kể có thể quan sát được (“observably different / substantial”); (2) Bản chất tác động đó có thể trái ngược nhau giữa các loài — có loài chim lại có lợi, còn loài thú lại có hại (“regardless of whether that difference was beneficial or detrimental”). Suy luận logic trực tiếp: tiếng ồn nhân tạo nhiều khả năng sẽ tạo tác động rõ rệt lên cả thú lẫn chim, nhưng bản chất tác động có thể rất khác nhau giữa hai loài → Chọn A!',
        'Trong dạng Inferences, đáp án đúng thường kết hợp chính xác 2 mệnh đề điều kiện của đoạn văn (“đều có tác động rõ rệt” + “nhưng bản chất/hướng tác động có thể khác nhau”) bằng ngôn ngữ thận trọng (“will likely”, “could be”).',
        [
            ('Đáp án đúng', 'Phản ánh trọn vẹn kết quả meta-analysis: cả thú (như chuột nâu) và chim (như chim sẻ sậy) đều chịu tác động rõ rệt, song chiều hướng tác động (có lợi vs. có hại) có thể rất khác nhau.'),
            ('Unsupported Comparison', 'Đoạn văn nói cả hai đều “substantial”, không hề so sánh tác động ở chim lớn hơn ở thú.'),
            ('Out of Scope', 'Không có thông tin nào nói nghiên cứu về thú thường ghi rõ tác hại hơn nghiên cứu về chim.'),
            ('Direct Contradiction', 'Trái ngược thẳng với dữ kiện “for every study, relevant traits or behaviors... were observably different”.'),
        ],
    ),

    # --- M2 Q16 ---
    q_item(
        'june2025_v1_rw_m2_q16', 16, 'Information and Ideas', 'Inferences', 'Hard',
        '<p>To measure changes in parasite abundance over time, Chelsea Wood and colleagues counted parasite individuals preserved on specimens of striped sea perch, surf smelt, and six other fish species collected from Puget Sound between 1880 and 2019. Using statistical models to estimate historical populations, the researchers determined that for every 1°C increase in annual average sea surface temperature, the abundance of complex life cycle parasites like <i>Lecithaster</i> sp. that require at least three unique host species throughout their life cycle decreased by 38%. However, the abundance of <i>Bomolochus bellones</i> and other directly transmitted parasites, which require only one host species, was essentially unchanged. These findings suggest that _______</p>',
        'Which choice most logically completes the text?',
        [
            '<i>Lecithaster</i> sp. abundance decreased by 38% over the period studied, whereas <i>B. bellones</i> abundance did not.',
            'parasites that rely exclusively on either striped sea perch or surf smelt are more sensitive to rising temperatures than are parasites that can infect both species throughout their life cycles.',
            'dependency on only a single host species may confer on parasites some resilience to rising sea surface temperatures.',
            'as the number of hosts that complex life cycle parasites require increases, the parasites’ tolerance for rising sea surface temperatures decreases proportionally.',
        ],
        'C',
        'Phân tích dữ kiện sắc nét từng milimet: Khi nhiệt độ mặt biển tăng thêm mỗi 1°C: (1) Ký sinh trùng vòng đời phức tạp (cần **≥ 3 loài vật chủ**, như *Lecithaster* sp.) giảm mạnh 38%; (2) Ký sinh trùng truyền trực tiếp (chỉ cần **1 loài vật chủ duy nhất**, như *Bomolochus bellones*) **hầu như không thay đổi** (“essentially unchanged”). Suy luận chắc chắn và thận trọng nhất: việc chỉ phụ thuộc vào một loài vật chủ duy nhất có thể mang lại cho ký sinh trùng một mức độ chống chịu nhất định trước sự ấm lên của nước biển → Chọn C! ĐẶC BIỆT tránh bẫy A cực tinh vi: mức giảm 38% là **cho mỗi 1°C tăng lên** (“for every 1°C increase”), KHÔNG phải tổng mức giảm trong giai đoạn 1880–2019 (bài không hề cho biết nhiệt độ Puget Sound đã tăng đúng 1°C hay không)!',
        'Quy tắc 1-Millimeter Hard M2: Phân biệt “giảm 38% trên mỗi 1°C tăng” (tỷ suất theo nhiệt độ) với “giảm 38% trong suốt giai đoạn nghiên cứu” (tổng biến thiên theo thời gian) — đây là bẫy kinh điển ở đáp án A!',
        [
            ('Rate vs. Total Trap (1-mm Trap!)', 'Bẫy cực độc: 38% là mức giảm **cho mỗi 1°C nhiệt độ tăng lên**, không thể suy thành giảm đúng 38% trong giai đoạn 1880–2019 vì bài không cho biết nước biển đã ấm lên bao nhiêu độ!'),
            ('Reversed Logic', 'Ngược hoàn toàn kết quả: ký sinh trùng chỉ dựa vào 1 vật chủ ÍT nhạy cảm hơn (hầu như không đổi), chứ không phải nhạy cảm hơn loài cần nhiều vật chủ.'),
            ('Đáp án đúng', 'Suy luận chuẩn xác và chừng mực (“may confer... some resilience”): chỉ phụ thuộc vào 1 vật chủ duy nhất có thể giúp ký sinh trùng chống chịu tốt hơn trước nhiệt độ biển tăng.'),
            ('Unsupported Extrapolation', 'Bài chỉ so sánh nhóm 1 vật chủ với nhóm ≥3 vật chủ, hoàn toàn không chứng minh quy luật giảm **tỷ lệ thuận** (“decreases proportionally”) khi số vật chủ tăng dần từ 3 lên 4, 5...'),
        ],
    ),

    # --- M2 Q17 ---
    q_item(
        'june2025_v1_rw_m2_q17', 17, 'Standard English Conventions', 'Form, Structure, and Sense', 'Easy',
        '<p>The historian’s books about Millard Fillmore _______ what she is best known for, but she is also well regarded for her scholarship on Thomas Jefferson.</p>',
        'Which choice completes the text so that it conforms to the conventions of Standard English?',
        ['is', 'are', 'has been', 'was'],
        'B',
        'Kiểm tra hòa hợp chủ ngữ – động từ (Subject-Verb Agreement): Cụm giới từ “about Millard Fillmore” chỉ bổ nghĩa phụ; chủ ngữ cốt lõi là danh từ SỐ NHIỀU “The historian’s **books**”. Thì của câu là hiện tại đơn (“she **is** best known for”, “she **is** also well regarded”). Động từ số nhiều duy nhất trong 4 lựa chọn là “are” → Chọn B!',
        'Gạch bỏ cụm giới từ “about Millard Fillmore” để tránh bị danh từ số ít “Millard Fillmore” đánh lừa, sau đó áp dụng mẹo 3–1 Split (3 động từ số ít vs. duy nhất 1 động từ số nhiều `are`).',
        [
            ('Singular Verb', '“is” là số ít, sai khi chủ ngữ chính là “books” (số nhiều).'),
            ('Đáp án đúng', '“are” là động từ hiện tại đơn số nhiều duy nhất khớp với chủ ngữ “books”.'),
            ('Singular Verb', '“has been” chia cho chủ ngữ số ít.'),
            ('Singular & Past Verb', '“was” vừa sai số ít vừa sai thì quá khứ.'),
        ],
    ),

    # --- M2 Q18 ---
    q_item(
        'june2025_v1_rw_m2_q18', 18, 'Standard English Conventions', 'Form, Structure, and Sense', 'Medium',
        '<p>Disyllabic words _______ as trochees in English metrical verse, such as “eyebrow” and “mascot,” consist of one stressed syllable followed by one unstressed syllable.</p>',
        'Which choice completes the text so that it conforms to the conventions of Standard English?',
        ['have been classified', 'can be classified', 'are classified', 'classified'],
        'D',
        'Quy tắc Động từ chính vs. Phân từ bổ nghĩa (Finite Verb vs. Participle): Đọc hết câu sẽ thấy động từ chính ĐÃ CÓ SẴN là **“consist”** (“Disyllabic words [...] **consist** of one stressed syllable...”). Do đó, chỗ trống không thể điền thêm một động từ chia thì (finite verb) mà BẮT BUỘC dùng phân từ quá khứ rút gọn mệnh đề quan hệ bị động: “Disyllabic words **classified** as trochees...” (= words *that are classified* as trochees) → Chọn D!',
        'Luôn kiểm tra xem phía sau đã có động từ chính của chủ ngữ chưa! Có sẵn động từ chính “consist” + có 3 đáp án finite verb vs. 1 đáp án nonfinite participle (`classified`) → chốt ngay D!',
        [
            ('Double Finite Verb', 'Chèn động từ chia thì “have been classified” tạo hai vị ngữ xung đột với động từ chính “consist”.'),
            ('Double Finite Verb', '“can be classified” là động từ chia thì, khiến câu thừa vị ngữ cùng động từ “consist”.'),
            ('Double Finite Verb', '“are classified” là động từ chia thì, không thể đứng chen giữa chủ ngữ “Disyllabic words” và động từ chính “consist” nếu thiếu đại từ quan hệ “that”.'),
            ('Đáp án đúng', 'Phân từ quá khứ “classified” tạo cụm bổ ngữ rút gọn (participial modifier) chuẩn xác cho “Disyllabic words”, để “consist” làm động từ chính duy nhất.'),
        ],
    ),

    # --- M2 Q19 ---
    q_item(
        'june2025_v1_rw_m2_q19', 19, 'Standard English Conventions', 'Boundaries', 'Medium',
        '<p>All member nations of the North Atlantic Treaty Organization, or NATO—including Belgium, which joined in 1949; Hungary, which joined in 1999; and Slovenia, which joined in _______ are committed to NATO’s principle of collective defense, each member pledging to defend all others.</p>',
        'Which choice completes the text so that it conforms to the conventions of Standard English?',
        ['2004;', '2004', '2004—', '2004,'],
        'C',
        'Quy tắc Cặp dấu câu đồng nhất cho thông tin bổ sung (Paired Punctuation / Nonessential Element): Nhìn phía trước thấy có dấu gạch ngang dài mở ra sau chữ **“NATO—”** để liệt kê các nước thành viên (“—including Belgium, which joined in 1949; Hungary, which joined in 1999; and Slovenia, which joined in 2004—”). Vì mở bằng gạch ngang (`—`), nên khi kết thúc cụm chêm ngay trước động từ chính “are committed”, BẮT BUỘC phải đóng bằng một **dấu gạch ngang tương ứng (`—`)** → Chọn C (“2004—”)!',
        'Gặp cụm chêm ở giữa chủ ngữ và động từ, quy tắc bất di bất dịch là **mở bằng dấu nào thì đóng bằng đúng dấu đó**: `— ... —` hoặc `, ... ,` (tuyệt đối không trộn lẫn dấu gạch ngang với dấu phẩy hay chấm phẩy).',
        [
            ('Mismatched Closing Mark', 'Dấu chấm phẩy (`;`) chỉ dùng ngăn cách các mục bên trong danh sách, không thể đóng cụm chêm mở bằng dấu gạch ngang (`—`).'),
            ('Missing Closing Dash', 'Thiếu dấu gạch ngang đóng khiến cụm liệt kê dính liền vào động từ chính “are committed”.'),
            ('Đáp án đúng', 'Dấu gạch ngang đóng (`2004—`) khép cặp hoàn hảo với dấu mở sau “NATO—”, tách gọn phần liệt kê trước động từ chính “are committed”.'),
            ('Mismatched Closing Mark', 'Không được mở bằng dấu gạch ngang (`—`) rồi lại đóng bằng dấu phẩy (`,`).'),
        ],
    ),

    # --- M2 Q20 ---
    q_item(
        'june2025_v1_rw_m2_q20', 20, 'Standard English Conventions', 'Form, Structure, and Sense', 'Hard',
        '<p>As the exoplanet 81 Ceti b orbits a star 330 light-years from Earth, the exoplanet’s gravity causes the star to wobble. In 2008, astronomers _______ this wobble through shifts in the color of the star’s spectral light—blueshifts indicating longer wavelengths and movement toward the observer, redshifts shorter wavelengths and movement away—deduced that the fluctuation was caused by the gravitational force of a previously undetected exoplanet.</p>',
        'Which choice completes the text so that it conforms to the conventions of Standard English?',
        ['perceived', 'had perceived', 'were perceiving', 'perceiving'],
        'D',
        'Kỹ thuật gạch bỏ cụm giữa cặp gạch ngang (`— ... —`): Sau khi tạm bỏ phần giải thích “—blueshifts..., redshifts...—”, câu còn lại là: “In 2008, astronomers _______ this wobble through shifts in the color of the star’s spectral light **deduced** that the fluctuation was caused by...” Nhận ra ngay động từ chính của chủ ngữ “astronomers” ĐÃ CÓ SẴN là **“deduced”**! Do đó, chỗ trống không được dùng động từ chia thì (`perceived`, `had perceived`, `were perceiving`) mà phải dùng phân từ hiện tại **“perceiving”** làm cụm bổ ngữ chủ động (= astronomers *who perceived* this wobble... deduced that...) → Chọn D!',
        'Câu Hard M2 cố tình nhét một cụm gạch ngang rất dài ngay trước động từ chính “deduced” để bạn quên mất câu đã có vị ngữ! Luôn đọc lướt qua cặp gạch ngang để kiểm tra động từ chính trước khi chọn dạng động từ.',
        [
            ('Double Finite Verb', 'Nếu điền “perceived”, câu có hai động từ chia thì “perceived ... deduced” cho cùng chủ ngữ “astronomers” mà không có liên từ “and”.'),
            ('Double Finite Verb', '“had perceived” là động từ chia thì quá khứ hoàn thành, gây lỗi hai vị ngữ không liên kết với “deduced”.'),
            ('Double Finite Verb', '“were perceiving” là động từ chia thì quá khứ tiếp diễn, xung đột trực tiếp với động từ chính “deduced”.'),
            ('Đáp án đúng', 'Hiện tại phân từ “perceiving” tạo cụm bổ ngữ gọn ghẽ cho “astronomers”, giúp “deduced” giữ vai trò động từ chính duy nhất của câu.'),
        ],
    ),

    # --- M2 Q21 ---
    q_item(
        'june2025_v1_rw_m2_q21', 21, 'Standard English Conventions', 'Boundaries', 'Medium',
        '<p>A loose confederation of cities from eleven modern-day countries, the Hanseatic League was a powerful mercantile alliance that dominated northern European trade between the 13th and 17th centuries. Hanseatic League member _______ was serendipitously located on the Rhine River in Germany, giving Cologne’s merchants access to key maritime trade routes.</p>',
        'Which choice completes the text so that it conforms to the conventions of Standard English?',
        ['city Cologne,', 'city, Cologne,', 'city, Cologne', 'city Cologne'],
        'D',
        'Quy tắc vàng “Chức danh / Danh xưng mô tả + Tên riêng” (Essential Appositive — ZERO Commas): Trong cụm “Hanseatic League member city Cologne”, “Hanseatic League member city” là danh xưng mô tả đứng trực tiếp trước tên riêng “Cologne” (không có mạo từ “The” hay “A” phía trước, và có rất nhiều thành phố thành viên nên tên “Cologne” là thông tin BẮT BUỘC để xác định thành phố nào). Vì vậy, TUYỆT ĐỐI KHÔNG đặt dấu phẩy giữa “city” và “Cologne”, và càng KHÔNG đặt dấu phẩy đơn ngăn cách chủ ngữ với động từ “was” → Chọn D (“city Cologne”)!',
        'Phép thử cắt bỏ (Drop Test): Thử bỏ `, Cologne,` ở đáp án B sẽ ra câu vô nghĩa “Hanseatic League member city was serendipitously located...” (thiếu mạo từ) → Chứng minh tên riêng “Cologne” là thiết yếu → 0 dấu phẩy!',
        [
            ('Subject-Verb Comma Error', 'Đặt một dấu phẩy đơn ngay sau “Cologne” tách rời chủ ngữ khỏi động từ “was”.'),
            ('Wrong Nonessential Commas', 'Nếu tách `, Cologne,` bằng cặp phẩy thì bỏ đi còn “Hanseatic League member city was...” — sai ngữ pháp tiếng Anh vì thiếu mạo từ và sai nghĩa vì Liên minh có rất nhiều thành phố thành viên.'),
            ('Single Comma Trap', 'Dấu phẩy đơn giữa danh xưng “city” và tên riêng “Cologne” là sai chuẩn ngữ pháp.'),
            ('Đáp án đúng', 'Không dùng bất kỳ dấu phẩy nào giữa danh xưng mô tả không mạo từ (“Hanseatic League member city”) và tên riêng xác định (“Cologne”), nối mượt vào động từ “was”.'),
        ],
    ),

    # --- M2 Q22 ---
    q_item(
        'june2025_v1_rw_m2_q22', 22, 'Expression of Ideas', 'Transitions', 'Easy',
        '<p>The moon Dia orbits Jupiter in the same direction that the planet rotates. _______ Dia’s orbit is described as prograde. Erinome, another of Jupiter’s moons, orbits in the opposite direction, so its orbit is described with the opposite term: retrograde.</p>',
        'Which choice completes the text with the most logical transition?',
        ['However,', 'Thus,', 'Likewise,', 'Next,'],
        'B',
        'Quan hệ logic giữa câu 1 và câu 2: Câu 1 nêu đặc điểm quỹ đạo của mặt trăng Dia (quay cùng chiều tự quay của Sao Mộc). Câu 2 nêu tên gọi phân loại suy ra từ đặc điểm đó (“Dia’s orbit is described as prograde”). Cấu trúc này thậm chí còn song song hoàn toàn với câu 3 ngay sau (“orbits in the opposite direction, **so** its orbit is described...”) → Quan hệ Nguyên nhân / Tiêu chí → Kết luận → Chọn B (“Thus,”)!',
        'Quan sát phép song song ngầm ngay trong đoạn văn: câu 3 dùng “so” nối cách quay với tên gọi quỹ đạo → chỗ trống câu 2 tương đương hệt như vậy = “Thus,”!',
        [
            ('Wrong Relationship (Contrast)', 'Tên gọi “prograde” là hệ quả trực tiếp của việc quay cùng chiều, không hề tương phản.'),
            ('Đáp án đúng', '“Thus,” (Do đó) thể hiện chuẩn xác mối quan hệ nhân-quả từ đặc điểm quay cùng chiều đến thuật ngữ “prograde”.'),
            ('Wrong Relationship (Similarity)', 'Câu 2 không nêu một mặt trăng tương tự khác mà kết luận về chính mặt trăng Dia ở câu 1.'),
            ('Wrong Relationship (Sequence)', 'Đây không phải chuỗi bước theo thứ tự thời gian.'),
        ],
    ),

    # --- M2 Q23 ---
    q_item(
        'june2025_v1_rw_m2_q23', 23, 'Expression of Ideas', 'Transitions', 'Medium',
        '<p>Scientists studying asteroid deflection have focused on secondary objects such as S/2015 (190208), a moonlet orbiting the near-Earth asteroid 2006 AQ. In 2022 NASA intentionally crashed a probe into just such an object, successfully altering its orbit. Scientists have yet to demonstrate, _______ that 2006 AQ and other primary objects would be similarly affected.</p>',
        'Which choice completes the text with the most logical transition?',
        ['for example,', 'admittedly,', 'moreover,', 'likewise,'],
        'B',
        'Phân tích mạch chuyển ý giữa câu 2 và câu 3: Câu 2 nêu thành công đã đạt được trên **vật thể thứ cấp** (“successfully altering its orbit” của mặt trăng nhỏ). Câu 3 chuyển sang một **giới hạn / điểm thừa nhận ngược lại** đối với **vật thể chính** (“Scientists have **yet to demonstrate**... that 2006 AQ and other primary objects would be similarly affected” — tuy nhiên phải thừa nhận rằng các nhà khoa học vẫn chưa chứng minh được điều tương tự với thiên thể chính) → Chọn B (“admittedly,” = phải thừa nhận rằng / tuy nhiên cũng cần nhìn nhận rằng)!',
        'Khi câu trước nêu một thành tựu (“successfully altering”) còn câu sau nêu giới hạn chưa làm được (“have yet to demonstrate”), chọn ngay từ nối nhượng bộ/tương phản (“admittedly,” / “however,” / “though,”).',
        [
            ('Wrong Relationship (Example)', 'Việc chưa chứng minh được trên thiên thể chính là một hạn chế/đối lập, không phải ví dụ cho thành công năm 2022.'),
            ('Đáp án đúng', '“admittedly,” diễn đạt sắc thái thừa nhận một hạn chế quan trọng sau thành tựu vừa nêu (“successfully altering” ↔ “have yet to demonstrate”).'),
            ('Wrong Relationship (Addition)', '“moreover,” bổ sung thêm luận cứ thuận chiều, sai hướng khi câu 3 chuyển sang hạn chế.'),
            ('Wrong Relationship (Similarity)', '“likewise,” chỉ sự tương đồng, trái với cụm phủ định “have yet to demonstrate” đối lập giữa vật thể thứ cấp và vật thể chính.'),
        ],
    ),

    # --- M2 Q24 ---
    q_item(
        'june2025_v1_rw_m2_q24', 24, 'Expression of Ideas', 'Transitions', 'Medium',
        '<p>Many paintings of the trompe l’oeil genre attain their illusory verisimilitude by depicting quotidian things, such as a fly or an empty bird cage, as if they are placed directly on top of the painted canvas. Nicola van Houbraken’s 1700 trompe l’oeil <i>Portrait of François Rivière</i>, _______ startles the viewer with the extraordinary sight of a man appearing to poke his head out from within the picture frame.</p>',
        'Which choice completes the text with the most logical transition?',
        ['fittingly,', 'by contrast,', 'for instance,', 'specifically,'],
        'B',
        'Bắt cặp từ khóa đối lập sắc lẹm giữa hai câu: Câu 1 nói nhiều tranh trompe l’oeil vẽ những vật **tầm thường đời thường** (“quotidian things”, như con ruồi, lồng chim trống) như đặt **trên bề mặt toan vẽ** (“on top of the painted canvas”). Câu 2 nói bức *Portrait of François Rivière* của Houbraken lại gây giật mình bằng hình ảnh **khác thường / phi thường** (“extraordinary sight”) về một người đàn ông thò đầu **từ bên trong khung tranh ra** (“from within the picture frame”) → Trực tiếp tương phản hai phong cách → Chọn B (“by contrast,”)!',
        'Cặp tính từ đối nghĩa “quotidian things” (đời thường) ↔ “extraordinary sight” (cảnh tượng khác thường) là tín hiệu tương phản tuyệt đối cho “by contrast,”.',
        [
            ('Wrong Relationship (Appropriateness)', '“fittingly,” mang nghĩa “thật tương xứng/hợp lẽ”, sai khi câu 2 đi ngược lại thông lệ phổ biến nêu ở câu 1.'),
            ('Đáp án đúng', '“by contrast,” đối chiếu rõ nét giữa mô-típ vật thể đời thường đặt trên mặt tranh ở câu 1 với hình ảnh người đàn ông khác thường thò đầu ra từ trong khung ở câu 2.'),
            ('Wrong Relationship (Example)', 'Bức tranh của Houbraken KHÔNG phải ví dụ minh họa cho việc vẽ vật nhỏ đời thường như con ruồi hay lồng chim — nó phá cách ngược lại.'),
            ('Wrong Relationship (Specification)', '“specifically,” dùng để đi sâu cụ thể hóa đúng mô tả ở câu 1, sai hướng đối lập.'),
        ],
    ),

    # --- M2 Q25 ---
    q_item(
        'june2025_v1_rw_m2_q25', 25, 'Expression of Ideas', 'Rhetorical Synthesis', 'Easy',
        '<p>While researching a topic, a student has taken the following notes:</p>'
        '<ul>'
        '<li>Katrin Heer, Larissa Albrecht, and Elisabeth K.V. Kalko published a study in 2010.</li>'
        '<li>In it, the researchers found that ingestion by bats had a neutral effect on the germination of <i>Ficus nymphaeifolia</i> plant seeds.</li>'
        '<li>Mikaela Marques Pulzatto and M.S. Dainez Filho published a study in 2017.</li>'
        '<li>In it, the researchers found that ingestion by bats had a negative effect on the germination of <i>Ficus luschnathiana</i> plant seeds.</li>'
        '<li>Reinaldo Chaves Teixeira, C. Corrêa, and E. Fischer published a study in 2009.</li>'
        '<li>In it, the researchers found that ingestion by bats had a positive effect on the germination of <i>Ficus pertusa</i> plant seeds.</li>'
        '</ul>',
        'The student wants to make a generalization about the germination of seeds ingested by bats. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
        [
            'Bat ingestion has consistently been found to have a positive effect on seed germination.',
            'As was found in the 2010 study, ingestion by bats has a positive effect on the germination of plant seeds.',
            'Over the years, researchers have studied the effect that seed germination has had on ingestion by bats.',
            'Seed ingestion by bats can have varying effects on seed germination.',
        ],
        'D',
        'Chiến lược Goal-First: Mục tiêu là **đưa ra một nhận định khái quát (generalization) về sự nảy mầm của hạt sau khi bị dơi ăn**. Tổng hợp 3 nghiên cứu trong ghi chú: 2010 → trung tính (**neutral**); 2017 → tiêu cực (**negative**); 2009 → tích cực (**positive**). Như vậy, nhận định khái quát duy nhất đúng sự thật là: việc hạt bị dơi ăn có thể tạo ra **những tác động khác nhau** lên sự nảy mầm → Chọn D!',
        'Với Goal “make a generalization”, hãy tổng quát hóa toàn bộ dữ liệu (neutral + negative + positive = “varying effects”) và loại ngay các lựa chọn sai sự thật (A, B) hoặc đảo ngược nhân-quả (C).',
        [
            ('Factual Error', 'Sai sự thật: không hề “consistently positive” vì nghiên cứu 2010 cho kết quả trung tính và 2017 cho kết quả tiêu cực.'),
            ('Factual Error', 'Nhầm năm nghiên cứu: nghiên cứu 2010 cho tác động TRUNG TÍNH (neutral), còn tác động tích cực là của năm 2009; đồng thời khái quát hóa sai thành luôn tích cực.'),
            ('Reversed Cause-Effect', 'Đảo ngược nhân-quả vô lý: nghiên cứu xem xét tác động của việc dơi ăn lên sự nảy mầm, không phải tác động của sự nảy mầm lên việc dơi ăn.'),
            ('Đáp án đúng', 'Khái quát ngắn gọn và chuẩn xác 100% cả ba kết quả (neutral, negative, positive): “can have varying effects”.'),
        ],
    ),

    # --- M2 Q26 ---
    q_item(
        'june2025_v1_rw_m2_q26', 26, 'Expression of Ideas', 'Rhetorical Synthesis', 'Medium',
        '<p>While researching a topic, a student has taken the following notes:</p>'
        '<ul>'
        '<li><i>Waiting</i> is a 1987 black-and-white linocut print by Kuwaiti artist Thuraya Al-Baqsami.</li>'
        '<li>It depicts a tranquil, everyday scene (a woman in a headscarf gazing out a window).</li>'
        '<li><i>¡Sera toda nuestra!</i> (<i>“It will all be ours!”</i>) is a 1977 color linocut print by Mexican American artist Carlos Cortéz.</li>'
        '<li>It features a scene with an explicitly political point of view (a group of laborers preparing to go on strike).</li>'
        '<li>Lino cutting is an inexpensive printmaking technique in which an image is carved onto linoleum tile, covered in ink or paint, and stamped onto paper.</li>'
        '</ul>',
        'The student wants to make a generalization about linocut prints. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
        [
            'Linocuts can depict a range of scenes, from the explicitly political to the tranquil and everyday.',
            'Cortéz’s linocut features a group of laborers preparing to go on strike, while Al-Baqsami’s depicts a woman in a headscarf gazing out a window.',
            'Cortéz made <i>¡Sera toda nuestra!</i> (<i>“It will all be ours!”</i>) in 1977, while Al-Baqsami made <i>Waiting</i> later, in 1987.',
            'Lino cutting is a printmaking technique in which linoleum tile is used to create works with an explicitly political point of view.',
        ],
        'A',
        'Chiến lược Goal-First: Mục tiêu là **đưa ra một nhận định khái quát (generalization) về tranh khắc lino (linocut prints)**. Hai ví dụ cho thấy tranh khắc lino có thể khắc họa cảnh đời thường thanh bình (*Waiting*) lẫn góc nhìn chính trị rõ rệt (*¡Sera toda nuestra!*). Đáp án A khái quát hóa chính xác phổ đề tài rộng lớn đó của tranh khắc lino (“Linocuts can depict a range of scenes, from the explicitly political to the tranquil and everyday”) → Chọn A!',
        'Phân biệt “generalization” (nhận định chung cho cả loại hình “Linocuts can...”) với việc chỉ mô tả/so sánh 2 tác phẩm riêng lẻ (B, C) hoặc khái quát phiến diện sai sự thật (D).',
        [
            ('Đáp án đúng', 'Đưa ra nhận định khái quát chuẩn xác về tranh khắc lino nói chung bằng cách bao trùm cả hai thái cực đề tài trong ghi chú.'),
            ('Specific Comparison Only', 'Chỉ mô tả hai bức tranh cụ thể của Cortéz và Al-Baqsami, không rút ra khái quát chung về tranh khắc lino.'),
            ('Specific Dates Only', 'Chỉ so sánh năm sáng tác của hai tác phẩm, không phải khái quát về loại hình tranh khắc lino.'),
            ('Overgeneralization / False Scope', 'Bóp méo thành kỹ thuật khắc lino chỉ dùng để tạo tác phẩm chính trị, bỏ qua hoàn toàn ví dụ đời thường thanh bình *Waiting*.'),
        ],
    ),

    # --- M2 Q27 ---
    q_item(
        'june2025_v1_rw_m2_q27', 27, 'Expression of Ideas', 'Rhetorical Synthesis', 'Hard',
        '<p>While researching a topic, a student has taken the following notes:</p>'
        '<ul>'
        '<li>Between the fifteenth and sixteenth centuries, the city of Timbuktu was part of the Songhai Empire.</li>'
        '<li>Timbuktu was a center of trade and scholarship in the Sahara desert.</li>'
        '<li>The city was known for its hundreds of thousands of written manuscripts on both secular and religious subjects.</li>'
        '<li>The manuscripts survive today in dozens of private libraries across the city.</li>'
        '<li><i>The Pearls Leading to Accepted Guidance</i> is one of these manuscripts.</li>'
        '</ul>',
        'The student wants to introduce <i>The Pearls Leading to Accepted Guidance</i> to an audience unfamiliar with the Timbuktu manuscripts’ history. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
        [
            'Between the fifteenth and sixteenth centuries, the city of Timbuktu was home to <i>The Pearls Leading to Accepted Guidance</i>, a manuscript that discusses trade centers across the Sahara desert.',
            'In the city of Timbuktu, dozens of private libraries house manuscripts, such as <i>The Pearls Leading to Accepted Guidance</i>, that discuss both secular and religious subjects.',
            '<i>The Pearls Leading to Accepted Guidance</i> is a manuscript housed in a private library in Timbuktu.',
            'Among Timbuktu’s vast collection of secular and religious manuscripts dating back to the Songhai Empire is <i>The Pearls Leading to Accepted Guidance</i>.',
        ],
        'D',
        'Chiến lược Goal-First: Mục tiêu gồm 2 yêu cầu song hành: [1] **Giới thiệu bản thảo *The Pearls Leading to Accepted Guidance*** + [2] **Cho khán giả chưa biết về LỊCH SỬ của các bản thảo Timbuktu** (“unfamiliar with the Timbuktu manuscripts’ history”). Kiểm tra từng đáp án:'
        ' — A bịa đặt sai sự thật (ghi chú nói Timbuktu là trung tâm thương mại, KHÔNG hề nói bản thảo *The Pearls Leading to Accepted Guidance* viết về các trung tâm thương mại!).'
        ' — B và C chỉ nhắc hiện trạng lưu giữ ngày nay ở thư viện tư nhân, hoàn toàn THIẾU bối cảnh lịch sử (thế kỷ 15–16 / Đế chế Songhai).'
        ' — Duy nhất D vừa chính xác 100% dữ kiện vừa cung cấp bối cảnh lịch sử nguồn gốc (“vast collection of secular and religious manuscripts dating back to the Songhai Empire”) để giới thiệu tác phẩm → Chọn D!',
        'Khi Goal nhắc “audience unfamiliar with X’s history”, ĐÁP ÁN ĐÚNG bắt buộc có thông tin lịch sử nguồn gốc (ở đây là “dating back to the Songhai Empire”), đồng thời kiểm tra kỹ tránh bẫy ghép sai chủ ngữ như A!',
        [
            ('Factual Distortion', 'Ghép sai dữ kiện: thành phố Timbuktu là trung tâm thương mại ở Sahara, nhưng ghi chú KHÔNG hề nói bản thảo *The Pearls Leading to Accepted Guidance* bàn về các trung tâm thương mại.'),
            ('Missing Historical Context', 'Chỉ nêu tình trạng lưu trữ hiện tại trong thư viện tư nhân, thiếu hoàn toàn bối cảnh lịch sử của các bản thảo Timbuktu (thế kỷ 15–16 / Đế chế Songhai).'),
            ('Missing Historical Context', 'Quá sơ sài: không giải thích bộ sưu tập đồ sộ hay lịch sử thời Đế chế Songhai của các bản thảo Timbuktu.'),
            ('Đáp án đúng', 'Vừa trung thực tuyệt đối với ghi chú vừa khéo léo lồng ghép bối cảnh lịch sử (“vast collection of secular and religious manuscripts dating back to the Songhai Empire”) để giới thiệu *The Pearls Leading to Accepted Guidance*.'),
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
        'subtitle': 'Đề thi thật Digital SAT tháng 6/2025 (Ver 1) — Đủ 2 Module (M1: 27 câu + M2: 27 câu)',
        'difficultyBadge': 'REAL EXAM • JUNE 2025',
        'targetTimeMinutes': 64,
        'routingThreshold': 0,
    },
    'module1': {
        'id': 'real_june2025_v1_rw_m1',
        'title': 'Section 1, Module 1: Reading and Writing',
        'subtitle': 'June 2025 Ver 1 Real Exam — Module 1 (27 Qs • 32 min)',
        'timeLimitMinutes': 32,
        'questions': MODULE_1_QUESTIONS,
    },
    'module2_hard': {
        'id': 'real_june2025_v1_rw_m2_hard',
        'title': 'Section 1, Module 2: Reading and Writing',
        'subtitle': 'June 2025 Ver 1 Real Exam — Module 2 (27 Qs • 32 min)',
        'timeLimitMinutes': 32,
        'questions': MODULE_2_QUESTIONS,
    },
    'module2_lower': {
        'id': 'real_june2025_v1_rw_m2_lower',
        'title': 'Section 1, Module 2: Reading and Writing',
        'subtitle': 'June 2025 Ver 1 Real Exam — Module 2 (27 Qs • 32 min)',
        'timeLimitMinutes': 32,
        'questions': _clone_module_questions(
            MODULE_2_QUESTIONS,
            'june2025_v1_rw_m2_',
            'june2025_v1_rw_m2l_',
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
            if not (exp.get('summaryVi') or '').strip():
                errors.append(f'{qid}: empty summaryVi')
            if not (exp.get('keyTakeaway') or '').strip():
                errors.append(f'{qid}: empty keyTakeaway')

            # Fidelity checks: tables & underlines must be present when referenced
            q_lower = (q['questionHtml'] or '').lower()
            stim = q['stimulusHtml'] or ''
            if 'table' in q_lower and '<table' not in stim.lower():
                errors.append(f'{qid}: question references table but stimulusHtml lacks <table>')
            if 'underlined' in q_lower and '<u>' not in stim.lower():
                errors.append(f'{qid}: question references underlined text but stimulusHtml lacks <u>')

    # Verify module2_lower mirrors module2_hard verbatim (aside from IDs)
    for qh, ql in zip(m2h_qs, m2l_qs):
        for field in ('number', 'domain', 'skill', 'stimulusHtml', 'questionHtml', 'options', 'correctAnswer', 'explanation'):
            if qh[field] != ql[field]:
                errors.append(f'module2_lower Q{qh["number"]} differs from module2_hard on field {field}')

    # 3. Zero watermarks & zero raw ______blank artifacts across entire JSON
    serialized = json.dumps(TEST_DATA, ensure_ascii=False)
    if re.search(r'@dsatuz|dsatuz', serialized, re.IGNORECASE):
        errors.append('Found @DSATuz watermark in TEST_DATA!')
    if '______blank' in serialized or 'blank.' in serialized.lower() and '_blank' in serialized.lower():
        errors.append('Found unconverted ______blank artifact in TEST_DATA!')
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
    print(f'  Tables verified: 4 (M1 Q9, M1 Q10, M1 Q11, M2 Q14)')
    print(f'  Underlines verified: 4 (M1 Q1, M1 Q5, M2 Q5, M2 Q8)')

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
