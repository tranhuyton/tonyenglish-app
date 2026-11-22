# -*- coding: utf-8 -*-
"""
Hand-crafted 1500+ Elite Digital SAT R&W Skill Drills (Module 5 Hard M2 Gauntlet):
- Drill 5.4: Command of Evidence — Quantitative Charts & Tables (13 Qs)
- Drill 5.5: Inferences — Hard Module 2 Deductive Completion (13 Qs)
"""

from sat_drills_1_1_and_2_1 import q_item

def svg_bar_chart(title, y_labels, bars, max_val):
    """Builds a crisp, College Board-style inline SVG bar chart."""
    # Plot box: x from 65 to 440, y from 25 to 155 (height = 130)
    grid_lines = []
    steps = len(y_labels) - 1
    for i, lbl in enumerate(y_labels):
        y = 155 - (i / max(1, steps)) * 130
        grid_lines.append(f'<line x1="65" y1="{y:.1f}" x2="440" y2="{y:.1f}" stroke="#e2e8f0" stroke-dasharray="3,3"/>')
        grid_lines.append(f'<text x="58" y="{y+3.5:.1f}" font-size="10" text-anchor="end" fill="#475569" font-family="sans-serif">{lbl}</text>')

    bar_elems = []
    n = len(bars)
    slot = 365 / max(1, n)
    bw = min(54, slot * 0.56)
    colors = ['#1e3a8a', '#2563eb', '#0284c7', '#0d9488', '#4f46e5']
    for i, (label, val, val_str) in enumerate(bars):
        cx = 72 + i * slot + slot / 2
        h = (val / max_val) * 130
        y = 155 - h
        col = colors[i % len(colors)]
        bar_elems.append(f'<rect x="{cx - bw/2:.1f}" y="{y:.1f}" width="{bw:.1f}" height="{h:.1f}" fill="{col}" rx="3"/>')
        bar_elems.append(f'<text x="{cx:.1f}" y="{y - 5:.1f}" font-size="10" font-weight="bold" text-anchor="middle" fill="{col}" font-family="sans-serif">{val_str}</text>')
        bar_elems.append(f'<text x="{cx:.1f}" y="171" font-size="10" text-anchor="middle" fill="#0f172a" font-family="sans-serif">{label}</text>')

    return (
        f'<div style="background:#f8fafc;border:1px solid #cbd5e1;border-radius:10px;padding:10px 12px;margin-bottom:12px;">'
        f'<div style="font-family:\'Segoe UI\',sans-serif;font-size:12.5px;font-weight:800;color:#0f172a;text-align:center;margin-bottom:6px;">{title}</div>'
        f'<svg viewBox="0 0 460 185" xmlns="http://www.w3.org/2000/svg" style="max-width:450px;">'
        f'<rect x="0" y="0" width="460" height="185" fill="#ffffff"/>'
        f'{"".join(grid_lines)}'
        f'<line x1="65" y1="20" x2="65" y2="155" stroke="#334155" stroke-width="1.5"/>'
        f'<line x1="65" y1="155" x2="440" y2="155" stroke="#334155" stroke-width="1.5"/>'
        f'{"".join(bar_elems)}'
        f'</svg></div>'
    )

def html_table(caption, headers, rows):
    ths = ''.join(f'<th>{h}</th>' for h in headers)
    trs = ''.join('<tr>' + ''.join(f'<td>{c}</td>' for c in r) + '</tr>' for r in rows)
    return (
        f'<div style="margin-bottom:12px;">'
        f'<div style="font-family:\'Segoe UI\',sans-serif;font-size:13px;font-weight:800;color:#0f172a;margin-bottom:6px;">{caption}</div>'
        f'<table><thead><tr>{ths}</tr></thead><tbody>{trs}</tbody></table></div>'
    )

def get_drill_5_4():
    questions = [
        q_item(
            'd5_4_q1', 1, 'Information and Ideas', 'Command of Evidence (Quantitative)', 'Hard',
            svg_bar_chart(
                'Mean Crop Yield Increase (%) Over Untreated Control by Soil Amendment',
                ['0%', '10%', '20%', '30%', '40%'],
                [('Compost', 14, '+14%'), ('Biochar', 19, '+19%'), ('Kelp Meal', 11, '+11%'), ('Biochar+Compost', 36, '+36%')],
                40
            ) + '<p>Agronomists studying sandy coastal soils hypothesized that combining biochar with organic compost produces a synergistic effect—raising crop yields by more than the sum of the separate yield increases achieved when biochar and compost are applied individually.</p>',
            'Which choice best describes data from the graph that support the agronomists’ hypothesis?',
            [
                'Combining biochar and compost boosted crop yield by 36%, which exceeds the 33% combined total of applying biochar alone (+19%) and compost alone (+14%).',
                'Biochar applied by itself generated a +19% yield gain, outperforming both compost alone (+14%) and kelp meal alone (+11%).',
                'All four soil amendments tested in the trial produced positive mean yield increases above the untreated control plots.',
                'Kelp meal yielded the smallest increase among the four tested treatments at +11% over control plots.'
            ],
            'A',
            'Khóa định nghĩa "synergistic effect" trong Claim: tổ hợp Biochar+Compost tăng NHIỀU HƠN TỔNG của hai thành phần riêng lẻ! Tính ngay: Biochar (+19%) + Compost (+14%) = 33%, còn tổ hợp đạt +36% (>33%)! B, C, D đều đúng số liệu 100% nhưng là bẫy "True Data, Wrong Claim" vì không kiểm chứng phép cộng tổng hợp 19+14 vs. 36!',
            'Đọc kỹ định nghĩa toán học nhúng trong văn bản ("more than the sum of the separate increases") rồi làm phép cộng đơn giản kiểm chứng ngay!',
            [
                ('Đáp án đúng', 'Chứng minh trực tiếp hiệu ứng cộng hưởng (synergy): +36% vượt tổng riêng lẻ 19% + 14% = 33%.'),
                ('True Data / Wrong Claim', 'Đúng biểu đồ nhưng chỉ so sánh riêng lẻ, không chứng minh tổ hợp vượt tổng thành phần.'),
                ('True Data / Wrong Claim', 'Chỉ nêu cả 4 nghiệm thức đều dương, hoàn toàn không kiểm chứng giả thuyết cộng hưởng.'),
                ('True Data / Wrong Claim', 'Chỉ nói về Kelp meal, không liên quan đến tổ hợp Biochar + Compost.'),
            ]
        ),
        q_item(
            'd5_4_q2', 2, 'Information and Ideas', 'Command of Evidence (Quantitative)', 'Hard',
            html_table(
                'Table 1. Performance of Four Public Library Branches After Extending Evening Hours (2022–2024)',
                ['Branch', 'Weekly Hours Added', 'Evening Checkouts Change', 'Study Room Bookings Change'],
                [
                    ['Northgate', '+6 hrs', '+18%', '+44%'],
                    ['Riverside', '+10 hrs', '+12%', '+61%'],
                    ['Oakwood', '+6 hrs', '+29%', '+35%'],
                    ['Harborview', '+12 hrs', '+9%', '+72%'],
                ]
            ) + '<p>A municipal analyst claims that adding more weekly evening hours reliably produces proportionally larger percentage increases in evening book checkouts across library branches.</p>',
            'Which choice best describes data from the table that weaken the municipal analyst’s claim?',
            [
                'Harborview added the most evening hours (+12 hrs) and recorded the largest jump in study room bookings (+72%).',
                'Although Harborview (+12 hrs) and Riverside (+10 hrs) added substantially more weekly hours than Oakwood (+6 hrs), both recorded much smaller percentage gains in evening checkouts (+9% and +12%) than Oakwood did (+29%).',
                'Northgate and Oakwood each added exactly 6 weekly evening hours between 2022 and 2024.',
                'All four library branches experienced higher percentage gains in study room bookings than in evening checkouts.'
            ],
            'B',
            'Khóa Claim cần WEAKEN: Thêm CÀNG NHIỀU giờ mở tối → phần trăm mượn sách (evening checkouts) tăng CÀNG MẠNH tương ứng! Nhìn bảng cột Hours Added vs. Evening Checkouts: Harborview (+12h) chỉ tăng +9%, Riverside (+10h) tăng +12%, trong khi Oakwood chỉ thêm +6h mà tăng vọt +29% (ngược hoàn toàn xu hướng tỉ lệ thuận)! Chọn B! Cẩn thận bẫy A & D: chúng bàn về "study room bookings" (nhầm cột biến mục tiêu!).',
            'Kiểm tra đúng CỘT biến của Claim ("evening book checkouts", KHÔNG phải "study room bookings"!) để tránh bẫy lệch cột!',
            [
                ('Wrong Column Trap', 'Đúng số liệu nhưng nói về "study room bookings" — Claim đang nói về "evening book checkouts"!'),
                ('Đáp án đúng', 'Chỉ ra nghịch đảo trực tiếp: thêm giờ nhiều nhất (+12h, +10h) lại tăng mượn sách ít hơn hẳn (+9%, +12%) so với chi nhánh chỉ thêm +6h (+29%).'),
                ('True Data / Wrong Claim', 'Chỉ nêu sự giống nhau về số giờ thêm của hai chi nhánh, không bác bỏ quan hệ tỉ lệ thuận.'),
                ('True Data / Wrong Claim', 'So sánh giữa 2 cột kết quả với nhau, không bác bỏ tuyên bố về giờ mở cửa và checkouts.'),
            ]
        ),
        q_item(
            'd5_4_q3', 3, 'Information and Ideas', 'Command of Evidence (Quantitative)', 'Elite (750+)',
            html_table(
                'Table 2. Acoustic Detection of Three Nocturnal Bat Species by Streetlight Type',
                ['Streetlight Spectrum', 'Pipistrelle (passes/hr)', 'Long-Eared Bat (passes/hr)', 'Horseshoe Bat (passes/hr)'],
                [
                    ['Unlit Dark Control', '24.2', '18.6', '15.4'],
                    ['Broad-Spectrum White LED', '31.5', '3.2', '2.1'],
                    ['Warm Amber LED', '28.9', '11.4', '9.8'],
                    ['Narrow-Band Red LED', '25.0', '17.9', '14.9'],
                ]
            ) + '<p>Urban ecologists hypothesized that artificial nighttime lighting does not affect all bat species uniformly: light-tolerant aerial hunters like pipistrelles may actually forage more frequently near bright white streetlights that attract moths, whereas light-averse woodland species experience sharp declines unless narrow-band red illumination is used instead. Data from a field trial support this distinction: ______</p>',
            'Which choice most effectively uses data from the table to complete the sentence?',
            [
                'narrow-band red LEDs resulted in lower pipistrelle activity (25.0 passes/hr) than warm amber LEDs (28.9 passes/hr).',
                'under dark control conditions, pipistrelles recorded 24.2 passes per hour, compared with 18.6 for long-eared bats and 15.4 for horseshoe bats.',
                'under broad-spectrum white LEDs, pipistrelle passes rose from 24.2 to 31.5 per hour while long-eared and horseshoe bat passes plummeted to 3.2 and 2.1—yet under narrow-band red LEDs, both light-averse species remained nearly at dark-control levels (17.9 and 14.9 passes/hr).',
                'warm amber LEDs attracted fewer horseshoe bats (9.8 passes/hr) than broad-spectrum white LEDs attracted pipistrelles (31.5 passes/hr).'
            ],
            'C',
            'Checklist 3 phần trong giả thuyết cần hoàn thiện sau dấu hai chấm: [1] Pipistrelle tăng hoạt động dưới White LED (24.2 → 31.5); [2] Hai loài sợ sáng sụt giảm mạnh dưới White LED (18.6 → 3.2 và 15.4 → 2.1); [3] Dưới Narrow-Band Red LED, hai loài sợ sáng giữ gần ngang mức tối tự nhiên (17.9 và 14.9 vs. 18.6 và 15.4). Duy nhất C bao trọn cả 3 mảnh ghép chính xác từng con số!',
            'Trong câu hoàn thiện bằng bảng số liệu, đáp án đúng phải phản ánh ĐẦY ĐỦ cả các vế tương phản trong giả thuyết ngay trước dấu hai chấm!',
            [
                ('Incomplete / True Data', 'Chỉ so sánh riêng pipistrelle giữa Red và Amber, bỏ qua hoàn toàn White LED và hai loài sợ sáng.'),
                ('Incomplete / Baseline Only', 'Chỉ đọc hàng Unlit Dark Control, không cho thấy tác động của bất kỳ loại đèn nào.'),
                ('Đáp án đúng', 'Khớp cả 3 nhánh số liệu: pipistrelle tăng dưới đèn trắng, 2 loài sợ sáng lao dốc dưới đèn trắng, và phục hồi gần nguyên trạng dưới đèn đỏ.'),
                ('Meaningless Cross-Species Comparison', 'So sánh chéo số lượt của loài này dưới đèn vàng với loài kia dưới đèn trắng không chứng minh giả thuyết.'),
            ]
        ),
        q_item(
            'd5_4_q4', 4, 'Information and Ideas', 'Command of Evidence (Quantitative)', 'Elite (750+)',
            svg_bar_chart(
                'Share of Commuters Switching From Cars to Transit (%) After Policy Launch',
                ['0%', '10%', '20%', '30%', '40%'],
                [('Free Fare Only', 8, '8%'), ('Dedicated Bus Lanes', 21, '21%'), ('Parking Cap Only', 13, '13%'), ('Lanes + Freq. Boost', 34, '34%')],
                40
            ) + '<p>A transit policy director asserts that eliminating bus fares altogether is far more effective at convincing car drivers to switch to public transit than investing in service reliability or dedicated road space.</p>',
            'Which choice best describes data from the graph that directly refute the transit policy director’s assertion?',
            [
                'Implementing a downtown parking cap alone convinced 13% of car commuters to switch to public transit.',
                'All four municipal policies succeeded in shifting at least 8% of automobile commuters to public transit.',
                'The highest commuter shift occurred when cities combined dedicated bus lanes with increased service frequency (34%).',
                'Free-fare policies alone shifted only 8% of car commuters to transit—less than half the 21% shift achieved by dedicated bus lanes alone and far below the 34% achieved by pairing bus lanes with higher frequency.'
            ],
            'D',
            'Khóa Claim cần bác bỏ (refute): Miễn vé (Free Fare) hiệu quả HƠN HẲN so với đầu tư làn đường riêng/độ tin cậy dịch vụ! Để bác bỏ trực tiếp, PHẢI so sánh thẳng Free Fare Only (8%) với Dedicated Bus Lanes (21%) và Lanes + Freq. Boost (34%) → Duy nhất D đặt trực diện 8% cạnh 21% và 34%! (Chú ý bẫy C: chỉ nhắc mức cao nhất 34% mà không nhắc Free Fare = 8% nên chưa bác bỏ trọn vẹn phép so sánh của giám đốc!).',
            'Khi Claim so sánh X > Y, đáp án bác bỏ mạnh nhất BẮT BUỘC nêu số liệu của CẢ X LẪN Y để chứng minh X < Y!',
            [
                ('True Data / Wrong Claim', 'Bàn về parking cap (13%) mà không nhắc tới free fare hay làn xe buýt.'),
                ('True Data / Wrong Claim', 'Chỉ nói cả 4 chính sách đều ≥8%, không phản bác phép so sánh giữa miễn vé và làn ưu tiên.'),
                ('Incomplete Comparison', 'Nêu mức 34% nhưng không dẫn số liệu 8% của Free Fare Only để đối chiếu bác bỏ trực diện.'),
                ('Đáp án đúng', 'Đối chiếu thẳng Free Fare Only (8%) thấp hơn rất nhiều so với Dedicated Bus Lanes (21%) và Lanes + Freq. Boost (34%).'),
            ]
        ),
        q_item(
            'd5_4_q5', 5, 'Information and Ideas', 'Command of Evidence (Quantitative)', 'Elite (750+)',
            html_table(
                'Table 3. Microplastic Fiber Counts per Liter in Four Coastal Rivers (2023)',
                ['River Basin', 'Total Fibers / L', 'Synthetic Polyester (%)', 'Natural Cotton/Wool (%)'],
                [
                    ['Estuary Alpha', '42.0', '28%', '72%'],
                    ['Estuary Beta', '18.5', '64%', '36%'],
                    ['Estuary Gamma', '30.0', '25%', '75%'],
                    ['Estuary Delta', '12.0', '70%', '30%'],
                ]
            ) + '<p>An environmental reporter claims that because Estuary Delta has the highest percentage of synthetic polyester fibers (70%), it must also contain the highest absolute concentration of synthetic polyester fibers per liter among the four surveyed rivers.</p>',
            'Which choice best describes data from the table that expose the flaw in the reporter’s reasoning?',
            [
                'Although synthetic polyester accounts for only 28% of fibers in Estuary Alpha and 64% in Estuary Beta, multiplying those shares by their much larger total fiber counts yields 11.76 and 11.84 synthetic fibers per liter—both higher than Estuary Delta’s 8.40 synthetic fibers per liter (70% of 12.0).',
                'Natural cotton and wool fibers outnumber synthetic polyester fibers in both Estuary Alpha (72%) and Estuary Gamma (75%).',
                'Estuary Alpha records the highest total fiber count overall at 42.0 fibers per liter, more than triple Estuary Delta’s 12.0 fibers per liter.',
                'Estuary Gamma has the lowest percentage of synthetic polyester fibers in the table at 25%.'
            ],
            'A',
            'BẪY 800-LEVEL KINH ĐIỂN: Percentage vs. Raw Absolute Count! Phóng viên nhầm % cao nhất (Delta: 70%) = số sợi nhựa tuyệt đối/lít cao nhất! Tính thật từ bảng: Delta = 70% × 12.0 = **8.40 sợi/L**; trong khi Alpha = 28% × 42.0 = **11.76 sợi/L** và Beta = 64% × 18.5 = **11.84 sợi/L** (cả hai đều CAO HƠN hẳn Delta)! Chọn A!',
            'Không bao giờ quên quy tắc toán-đọc SAT: `% cao hơn` trên một `tổng nhỏ hơn` có thể cho `số tuyệt đối THẤP HƠN`!',
            [
                ('Đáp án đúng', 'Chỉ rõ sai lầm % vs. số tuyệt đối bằng phép nhân chính xác: Alpha (11.76/L) và Beta (11.84/L) đều vượt Delta (8.40/L).'),
                ('True Data / Wrong Claim', 'Chỉ nêu tỉ lệ bông/len tự nhiên ở Alpha và Gamma, không đụng tới số sợi polyester tuyệt đối của Delta.'),
                ('Incomplete Reasoning', 'Chỉ so tổng sợi (bao gồm cả bông/len tự nhiên), chưa tính ra nồng độ sợi polyester để phản bác trực tiếp.'),
                ('True Data / Wrong Claim', 'Chỉ nêu tỉ lệ thấp nhất ở Gamma, không bác bỏ lỗi suy luận về Delta.'),
            ]
        ),
        q_item(
            'd5_4_q6', 6, 'Information and Ideas', 'Command of Evidence (Quantitative)', 'Hard',
            html_table(
                'Table 4. Survival Rate of Transplanted Coral Fragments by Nursery Origin (18 Months)',
                ['Nursery Temperature Regime', 'Transplant Site: Cool Reef (27°C)', 'Transplant Site: Warm Reef (30.5°C)'],
                [
                    ['Constant Cool Nursery (27°C)', '88%', '31%'],
                    ['Variable Heat-Pulse Nursery (27°C–30°C)', '85%', '74%'],
                    ['Constant High Nursery (30°C)', '52%', '68%'],
                ]
            ) + '<p>Marine biologists sought a nursery protocol that prepares juvenile corals to survive severe marine heatwaves (30.5°C) without substantially compromising their survival when planted back onto normal cool reefs (27°C). Based on the table, the most promising protocol is ______</p>',
            'Which choice most effectively uses data from the table to complete the text?',
            [
                'the constant cool nursery, which achieved the highest overall survival rate on cool reefs at 88%.',
                'the variable heat-pulse nursery, which raised warm-reef survival dramatically to 74% while maintaining cool-reef survival at 85%—nearly matching the constant cool nursery’s 88%.',
                'the constant high nursery, because its 68% survival rate on warm reefs exceeded its 52% survival rate on cool reefs.',
                'the constant cool nursery, because its survival rate dropped by 57 percentage points between cool reefs and warm reefs.'
            ],
            'B',
            'Checklist 2 điều kiện của nhóm sinh vật biển: [1] Tỉ lệ sống cao ở rạn nóng 30.5°C + [2] KHÔNG làm giảm đáng kể tỉ lệ sống ở rạn mát 27°C. So 3 hàng: Constant Cool (88% mát / 31% nóng → chết thảm khi nóng); Constant High (52% mát / 68% nóng → tụt sâu ở rạn mát); **Variable Heat-Pulse (85% mát / 74% nóng)** → Vừa cao nhất ở rạn nóng (74%), vừa giữ 85% gần ngang ngửa 88% ở rạn mát! Chọn B!',
            'Bài toán tối ưu 2 tiêu chí trong bảng: gạch ngay mọi hàng làm tốt 1 cột nhưng sụp đổ ở cột còn lại!',
            [
                ('Fails Criterion 1', 'Constant cool nursery chỉ sống 31% ở rạn nóng — thất bại hoàn toàn ở tiêu chí chịu sóng nhiệt.'),
                ('Đáp án đúng', 'Khớp cả 2 tiêu chí: 74% cao nhất ở rạn nóng và vẫn giữ 85% gần sát mức chuẩn 88% ở rạn mát.'),
                ('Fails Criterion 2', 'Constant high tụt xuống chỉ còn 52% ở rạn mát (giảm sâu so với 88%) và ở rạn nóng (68%) cũng thua Heat-Pulse (74%).'),
                ('Contradicts Goal', 'Tụt 57 điểm phần trăm là bằng chứng cho thấy nó KÉM chứ không phải đầy hứa hẹn.'),
            ]
        ),
        q_item(
            'd5_4_q7', 7, 'Information and Ideas', 'Command of Evidence (Quantitative)', 'Hard',
            svg_bar_chart(
                'Average Daily Vocabulary Words Retained After 30 Days by Study Schedule',
                ['0', '10', '20', '30', '40'],
                [('Massed 1 Day', 11, '11 words'), ('3-Day Spacing', 23, '23 words'), ('7-Day Spacing', 34, '34 words'), ('21-Day Spacing', 26, '26 words')],
                40
            ) + '<p>Memory researchers note that while spacing study sessions apart generally outperforms cramming ("massed" practice), excessively long gaps between reviews can cause learners to forget material before reinforcing it—producing an inverted-U curve with an optimal intermediate interval.</p>',
            'Which choice best describes data from the graph that support the researchers’ description of an inverted-U pattern?',
            [
                'Students using 3-day spacing retained 23 words after 30 days, more than double the 11 words retained by students using massed practice.',
                'All three spaced-repetition schedules yielded higher 30-day vocabulary retention than massed 1-day cramming.',
                'Retention climbed steadily from 11 words (massed) to 23 words (3-day) and peaked at 34 words with 7-day spacing, before declining to 26 words when the gap widened to 21 days.',
                'Students on a 21-day spacing schedule retained 15 more words on average than students who crammed in a single day.'
            ],
            'C',
            'Khóa hình dạng đường cong "inverted-U curve with an optimal intermediate interval" (tăng lên đạt ĐỈNH ở khoảng giữa rồi GIẢM XUỐNG khi khoảng cách quá dài)! A, B, D chỉ cho thấy phần TĂNG (spacing > massed) chứ không hề cho thấy nhánh GIẢM khi giãn quá rộng (34 → 26 ở 21-day spacing)! Duy nhất C mô tả trọn vẹn cả nhánh lên (11 → 23 → đỉnh 34) lẫn nhánh xuống (→ 26)! Chọn C!',
            'Gặp khái niệm "inverted-U" / "diminishing returns / peak then decline" → đáp án đúng BẮT BUỘC nêu đủ 3 mốc: Điểm khởi đầu thấp → Đỉnh giữa → Điểm cuối tụt xuống!',
            [
                ('Incomplete Pattern', 'Chỉ nêu nhánh đi lên (11 → 23), thiếu đỉnh 34 và nhánh giảm xuống 26.'),
                ('Incomplete Pattern', 'Chỉ khẳng định spacing tốt hơn cramming, không cho thấy đường cong chữ U ngược.'),
                ('Đáp án đúng', 'Mô tả đầy đủ toàn bộ quỹ đạo hình chữ U ngược: tăng 11 → 23 → đỉnh 34 (7-day) → giảm xuống 26 (21-day).'),
                ('Incomplete Pattern', 'Chỉ so sánh hai đầu mút (21-day vs. 1-day), bỏ qua đỉnh trung gian 7-day.'),
            ]
        ),
        q_item(
            'd5_4_q8', 8, 'Information and Ideas', 'Command of Evidence (Quantitative)', 'Elite (750+)',
            html_table(
                'Table 5. Museum Attendance Before and After Removing General Admission Fees',
                ['Museum', 'First-Time Visitors Change', 'Total Annual Attendance Change', 'Average Donation per Visitor'],
                [
                    ['City Art Hall', '+46%', '+38%', '$4.20 → $5.10'],
                    ['Maritime Museum', '+52%', '+41%', '$2.80 → $3.95'],
                    ['Natural Science Ctr', '+39%', '+33%', '$3.50 → $3.15'],
                    ['Textile Archive', '+61%', '+49%', '$1.90 → $2.75'],
                ]
            ) + '<p>A museum finance trustee argues that while dropping ticket fees reliably boosts overall attendance, it inevitably lowers voluntary donations per visitor because people who enter for free feel less financially invested in supporting the institution.</p>',
            'Which choice best describes data from the table that weaken the trustee’s argument?',
            [
                'At the Natural Science Center, average donations per visitor fell from $3.50 to $3.15 even as annual attendance climbed by 33%.',
                'The Textile Archive recorded the sharpest rise in first-time visitors at +61% after removing admission fees.',
                'All four museums recorded double-digit percentage increases in both first-time visitors and total annual attendance.',
                'At three of the four surveyed museums—City Art Hall, Maritime Museum, and Textile Archive—average voluntary donations per visitor actually increased after general admission fees were removed.'
            ],
            'D',
            'Khóa Claim cần WEAKEN: Bỏ vé "inevitably lowers voluntary donations per visitor" (TẤT YẾU làm giảm tiền quyên góp bình quân mỗi khách). Soi cột Average Donation: 3 trong 4 bảo tàng (City Art Hall $4.20→$5.10, Maritime $2.80→$3.95, Textile $1.90→$2.75) ĐỀU TĂNG tiền quyên góp mỗi khách sau khi miễn vé! Chọn D! (A là bảo tàng duy nhất giảm — nó ỦNG HỘ Claim của trustee chứ không làm yếu!).',
            'Đọc kỹ từ cực đoan trong Claim ("inevitably lowers"): chỉ cần chỉ ra 3/4 bảo tàng đi ngược lại xu hướng đó là đánh sập Claim ngay!',
            [
                ('Opposite Direction (Supports!)', 'Natural Science Center giảm $3.50 → $3.15 là dẫn chứng ủng hộ lập luận của trustee, ngược yêu cầu WEAKEN.'),
                ('True Data / Wrong Claim', 'Chỉ nêu tăng lượng khách lần đầu (+61%), không chạm vào cột tiền quyên góp.'),
                ('True Data / Wrong Claim', 'Trustee ĐÃ đồng ý rằng lượt khách tăng ("while dropping ticket fees reliably boosts overall attendance")!'),
                ('Đáp án đúng', 'Chỉ ra 3/4 bảo tàng tăng mức quyên góp bình quân/khách, bác bỏ thẳng tuyên bố "inevitably lowers".'),
            ]
        ),
        q_item(
            'd5_4_q9', 9, 'Information and Ideas', 'Command of Evidence (Quantitative)', 'Hard',
            html_table(
                'Table 6. Seed Germination Rate (%) of Four Native Prairie Grasses After Controlled Fire',
                ['Grass Species', 'Unburned Plot', 'Low-Intensity Fire', 'High-Intensity Fire'],
                [
                    ['Big Bluestem', '48%', '76%', '79%'],
                    ['Little Bluestem', '52%', '74%', '41%'],
                    ['Indian Grass', '44%', '69%', '71%'],
                    ['Prairie Dropseed', '63%', '61%', '22%'],
                ]
            ) + '<p>Prairie restoration managers note that while controlled burning stimulates germination in several native grasses, not every species responds favorably—and for some grasses, excessive fire intensity reverses the germination gains observed under milder burns.</p>',
            'Which choice most effectively uses data from the table to illustrate the specific reversal described in the final clause?',
            [
                'Little Bluestem’s germination rate jumped from 52% in unburned plots to 74% under low-intensity fire, but plunged to 41% under high-intensity fire.',
                'Big Bluestem’s germination rate rose from 48% in unburned plots to 76% under low-intensity fire and reached 79% under high-intensity fire.',
                'Prairie Dropseed achieved its highest germination rate of 63% in unburned plots and declined slightly to 61% under low-intensity fire.',
                'Indian Grass germinated at a lower rate in unburned plots (44%) than Big Bluestem (48%) or Little Bluestem (52%).'
            ],
            'A',
            'Chốt đúng yêu cầu ở "the final clause": "excessive fire intensity REVERSES the germination GAINS observed under milder burns" (lửa nhẹ giúp TĂNG so với không đốt, nhưng lửa mạnh làm ĐẢO NGƯỢC TỤT XUỐNG). Kiểm tra 4 loài: Big Bluestem & Indian Grass đều tăng tiếp ở lửa mạnh; Prairie Dropseed không hề tăng ở lửa nhẹ (63%→61%); duy nhất **Little Bluestem** tăng từ 52% → 74% (lửa nhẹ) rồi tụt thảm xuống 41% (lửa mạnh)! Chọn A!',
            'Soi đúng cụm "reverses the gains observed under milder burns" → phải có đủ 2 bước: Tăng (Unburned → Low) rồi Tụt mạnh (Low → High)!',
            [
                ('Đáp án đúng', 'Little Bluestem minh họa chính xác tuyệt đối: tăng ở lửa nhẹ (52% → 74%) rồi đảo ngược tụt mạnh ở lửa mạnh (41%).'),
                ('No Reversal', 'Big Bluestem tiếp tục tăng ở lửa mạnh (76% → 79%), không đảo ngược.'),
                ('No Initial Gain', 'Prairie Dropseed giảm ngay từ lửa nhẹ (63% → 61%), không có "gains observed under milder burns".'),
                ('True Data / Wrong Claim', 'Chỉ so sánh cột Unburned, không nhắc tác động của lửa nhẹ hay lửa mạnh.'),
            ]
        ),
        q_item(
            'd5_4_q10', 10, 'Information and Ideas', 'Command of Evidence (Quantitative)', 'Elite (750+)',
            svg_bar_chart(
                'Mean Repair Cost per 100 km of Roadway ($ Thousands) by Pavement Mix (10-Year Total)',
                ['$0', '$100k', '$200k', '$300k', '$400k'],
                [('Standard Asphalt', 380, '$380k'), ('Recycled Rubber', 245, '$245k'), ('Polymer-Modified', 210, '$210k'), ('Porous Concrete', 290, '$290k')],
                400
            ) + '<p>Civil engineers noted that although polymer-modified asphalt and recycled-rubber mixes cost roughly $60,000 more per 100 km to pave initially than standard asphalt, their dramatically lower 10-year repair costs more than offset that upfront premium. By contrast, a skeptics’ report claimed that no alternative pavement mix saves more than $100,000 per 100 km in 10-year repair costs relative to standard asphalt.</p>',
            'Which choice best describes data from the graph that refute the skeptics’ report?',
            [
                'Porous concrete incurs $290,000 in 10-year repair costs per 100 km, which is $90,000 less than standard asphalt’s $380,000.',
                'Both polymer-modified asphalt ($210,000) and recycled-rubber asphalt ($245,000) reduce 10-year repair costs by $170,000 and $135,000 respectively compared with standard asphalt ($380,000)—well above the $100,000 threshold.',
                'Standard asphalt has the highest 10-year repair cost in the chart at $380,000 per 100 km.',
                'Polymer-modified asphalt saves $80,000 per 100 km in 10-year repair costs compared with porous concrete.'
            ],
            'B',
            'Khóa Claim cần bác bỏ (skeptics’ report): KHÔNG loại mặt đường thay thế nào tiết kiệm quá $100k chi phí sửa chữa 10 năm so với Standard Asphalt ($380k). Tính phép trừ: Porous Concrete tiết kiệm $380k − $290k = $90k (<$100k → không bác bỏ được!); **Polymer-Modified** tiết kiệm $380k − $210k = **$170k** và **Recycled Rubber** tiết kiệm $380k − $245k = **$135k** (cả hai đều vượt xa mốc $100k!) → Chọn B!',
            'Làm nhanh phép trừ kiểm tra ngưỡng $100k: $380k − $290k = $90k (A bẫy dưới ngưỡng!), còn $170k và $135k (B) vượt hẳn ngưỡng!',
            [
                ('Below Threshold Trap', 'Porous concrete chỉ tiết kiệm $90k — vẫn nằm DƯỚI ngưỡng $100k nên không bác bỏ được báo cáo hoài nghi!'),
                ('Đáp án đúng', 'Tính đúng mức tiết kiệm $170k và $135k so với Standard Asphalt ($380k), đánh sập trực tiếp ngưỡng $100k.'),
                ('Incomplete Comparison', 'Chỉ nêu chi phí của Standard Asphalt mà không tính khoản tiết kiệm so với vật liệu thay thế.'),
                ('Wrong Baseline Comparison', 'So sánh với porous concrete thay vì so sánh với standard asphalt như yêu cầu của skeptics’ report.'),
            ]
        ),
        q_item(
            'd5_4_q11', 11, 'Information and Ideas', 'Command of Evidence (Quantitative)', 'Elite (750+)',
            html_table(
                'Table 7. Share of Global Cobalt Production (%) vs. Share of Global Battery Refining Capacity (%) by Region (2023)',
                ['Region', 'Share of Mined Cobalt (%)', 'Share of Refined Battery-Grade Cobalt (%)'],
                [
                    ['Central Africa', '73%', '4%'],
                    ['East Asia', '3%', '76%'],
                    ['Southeast Asia', '11%', '9%'],
                    ['Rest of World', '13%', '11%'],
                ]
            ) + '<p>Supply-chain analysts emphasize that geographic dominance in mining a critical mineral does not automatically translate into dominance over the higher-value refining stage required to manufacture electric-vehicle batteries. This geographic disconnect is starkly illustrated in the table: ______</p>',
            'Which choice most effectively uses data from the table to complete the text?',
            [
                'Southeast Asia mines 11% of global cobalt and performs 9% of global battery-grade cobalt refining.',
                'the Rest of World accounts for 13% of mined cobalt and 11% of refined battery-grade cobalt.',
                'Central Africa produces 73% of the world’s mined cobalt yet holds only 4% of refining capacity, whereas East Asia mines just 3% but controls 76% of global battery-grade refining.',
                'global mined cobalt shares and refined battery-grade cobalt shares each sum to 100% across the four listed regions.'
            ],
            'C',
            'Khóa ý cần minh họa: "geographic disconnect" (sự tách rời địa lý cực mạnh giữa nơi khai thác quặng thô và nơi tinh luyện giá trị cao). Nhìn 4 hàng: Southeast Asia (11% vs. 9%) và Rest of World (13% vs. 11%) gần như CÂN BẰNG (ngược với "disconnect"!); chỉ cặp **Central Africa (73% khai thác / 4% tinh luyện)** ↔ **East Asia (3% khai thác / 76% tinh luyện)** minh họa trọn vẹn sự đứt gãy khổng lồ này! Chọn C!',
            'Tìm đúng hàng có độ chênh lớn nhất phản ánh từ khóa "starkly illustrated... geographic disconnect"!',
            [
                ('Opposite of Disconnect', '11% và 9% gần bằng nhau — không minh họa sự tách rời rõ rệt.'),
                ('Opposite of Disconnect', '13% và 11% gần tương đương nhau.'),
                ('Đáp án đúng', 'Đối chiếu sắc nét hai cực đảo ngược: Trung Phi 73% mỏ / 4% tinh luyện ↔ Đông Á 3% mỏ / 76% tinh luyện.'),
                ('Trivial Math Fact', 'Tổng hai cột bằng 100% là tính chất hiển nhiên của bảng phần trăm, không minh họa sự tách rời địa lý.'),
            ]
        ),
        q_item(
            'd5_4_q12', 12, 'Information and Ideas', 'Command of Evidence (Quantitative)', 'Hard',
            html_table(
                'Table 8. Acoustic Clarity Scores (0–100 Scale) in Four Historic Concert Halls',
                ['Concert Hall', 'Stage Shape', 'Empty Hall Clarity', 'Full Audience Clarity'],
                [
                    ['Hall A (Vienna)', 'Shoebox', '68', '84'],
                    ['Hall B (Boston)', 'Shoebox', '70', '86'],
                    ['Hall C (Berlin)', 'Vineyard', '79', '83'],
                    ['Hall D (Tokyo)', 'Vineyard', '81', '84'],
                ]
            ) + '<p>Acoustic architects note that while classic "shoebox" concert halls achieve slightly higher or comparable clarity to modern "vineyard" halls once every seat is filled, shoebox designs depend much more heavily on the sound-absorbing effect of a full audience to tame excessive echo—as shown by the much larger gap between empty and full-house scores.</p>',
            'Which choice best describes data from the table that support the acoustic architects’ observation?',
            [
                'Hall D (vineyard) achieved the highest empty-hall clarity score in the table at 81.',
                'All four historic concert halls achieved full-audience clarity scores between 83 and 86.',
                'Hall B (shoebox) recorded a slightly higher full-audience clarity score (86) than Hall C (83) or Hall D (84).',
                'Whereas the two vineyard halls improved by only 3 to 4 points from empty to full (79→83 and 81→84), both shoebox halls jumped by 16 points once filled (68→84 and 70→86).'
            ],
            'D',
            'Khóa điểm cốt lõi ở nửa sau câu: "much larger GAP between empty and full-house scores" ở nhà hát Shoebox so với Vineyard! Tính khoảng chênh: Vineyard tăng chỉ 4 điểm (79→83) và 3 điểm (81→84); trong khi Shoebox vọt tới 16 điểm (68→84 và 70→86) → Duy nhất D tính và so sánh trực tiếp độ chênh Empty ↔ Full của cả 2 loại thiết kế! Chọn D!',
            'Khi văn bản nhấn mạnh "much larger gap between X and Y", đáp án đúng phải tính ra hiệu số `(Full − Empty)` cho CẢ hai nhóm để đối chiếu!',
            [
                ('Incomplete Data', 'Chỉ nêu điểm phòng trống của 1 nhà hát, không tính độ chênh khi kín khán giả hay so sánh với Shoebox.'),
                ('True Data / Wrong Claim', 'Chỉ nói điểm khi đầy khán giả gần nhau (83–86), không chứng minh mức phụ thuộc vào khán giả lớn hơn của Shoebox.'),
                ('True Data / Wrong Claim', 'Chỉ nhắc phần mệnh đề phụ "comparable or slightly higher", bỏ qua luận điểm chính về khoảng chênh Empty→Full.'),
                ('Đáp án đúng', 'Đối chiếu chính xác biên độ tăng 3–4 điểm ở Vineyard với 16 điểm ở cả hai nhà hát Shoebox.'),
            ]
        ),
        q_item(
            'd5_4_q13', 13, 'Information and Ideas', 'Command of Evidence (Quantitative)', 'Elite (750+)',
            html_table(
                'Table 9. Glacier Mass Balance (Meters Water Equivalent / Year) in Four Mountain Ranges',
                ['Mountain Range', '1980–1999 Mean', '2000–2019 Mean', '2020–2024 Mean'],
                [
                    ['European Alps', '−0.42', '−0.89', '−1.65'],
                    ['Southern Andes', '−0.38', '−0.74', '−1.22'],
                    ['Karakoram', '+0.04', '+0.09', '−0.18'],
                    ['Alaska Coast', '−0.51', '−0.85', '−1.31'],
                ]
            ) + '<p>For decades, glaciologists puzzled over the "Karakoram Anomaly," a rare regional exception in which glaciers in the Karakoram range held steady or even gained slight mass even as other major mountain ranges lost ice rapidly. However, the most recent 2020–2024 measurements indicate that ______</p>',
            'Which choice most effectively uses data from the table to complete the text?',
            [
                'the Karakoram Anomaly appears to have reversed, with Karakoram glaciers shifting from slight gains (+0.04 and +0.09 m/yr) to net ice loss (−0.18 m/yr) alongside accelerating losses in every other range.',
                'glaciers in the European Alps lost ice at a faster rate during 2020–2024 (−1.65 m/yr) than glaciers along the Alaska Coast (−1.31 m/yr).',
                'the Southern Andes experienced a steady positive mass balance between 1980 and 2019.',
                'the Karakoram range gained more ice per year between 2020 and 2024 than it did between 2000 and 2019.'
            ],
            'A',
            'Nhìn ngay từ chuyển hướng "<b>However</b>, the most recent 2020–2024 measurements indicate that ______": Trước 2020, Karakoram là ngoại lệ dương (+0.04 rồi +0.09); sang giai đoạn 2020–2024, dấu đã ĐỔI CHIỀU SANG ÂM (−0.18 m/yr) trong khi 3 dãy núi kia tiếp tục mất băng nhanh hơn → Ngoại lệ Karakoram đã chấm dứt/đảo chiều! Chọn A! (C và D sai số liệu bảng hoàn toàn; B đúng số liệu nhưng bỏ quên Karakoram — nhân vật chính của đoạn!).',
            'Kiểm tra đồng thời: (1) Đọc đúng dấu âm/dương (`+` vs. `−`), (2) Bám sát từ chuyển hướng "However" áp vào đúng chủ thể chính "Karakoram"!',
            [
                ('Đáp án đúng', 'Bắt trọn sự đảo chiều của Karakoram (+0.04 / +0.09 → −0.18) khớp hoàn hảo với từ nối "However".'),
                ('True Data / Wrong Subject', 'Số liệu Alps vs. Alaska đúng nhưng bỏ rơi chủ thể trung tâm của đoạn là "Karakoram Anomaly".'),
                ('Data Reading Error', 'Southern Andes là số ÂM (−0.38 và −0.74), không phải dương.'),
                ('Data Reading Error', '2020–2024 của Karakoram là −0.18 (mất băng), không phải tăng thêm băng.'),
            ]
        ),
    ]
    return {
        'schemaVersion': 1,
        'mode': 'drill',
        'section': 'Reading and Writing',
        'basicInfo': {
            'title': 'Drill 5.4: Command of Evidence — Quantitative Charts & Tables (13 Qs)',
            'subtitle': 'Luyện biểu đồ SVG & bảng số liệu Hard Module 2: diệt bẫy True Data / Wrong Claim, % vs. Số tuyệt đối, và đường cong chữ U ngược.',
            'difficultyBadge': 'I&I • Target 1500+',
            'targetTimeMinutes': 16,
        },
        'drillModule': {
            'id': 'drill_5_4_mod',
            'title': 'Skill Drill 5.4: Quantitative Evidence (Charts & Tables)',
            'timeLimitMinutes': 16,
            'questions': questions,
        },
    }


def get_drill_5_5():
    stem = 'Which choice most logically completes the text?'
    questions = [
        q_item(
            'd5_5_q1', 1, 'Information and Ideas', 'Inferences', 'Elite (750+)',
            '<p>Astronomers initially assumed that closely packed "hot Jupiter" gas giants could form only far beyond a star’s frost line before migrating slowly inward over millions of years, scattering any smaller rocky planets out of the system along the way. Recently, however, the TESS space telescope detected two Earth-sized rocky worlds orbiting smoothly right alongside a hot Jupiter in the WASP-47 system—both in flat, undisturbed circular orbits. This discovery suggests that ______</p>',
            stem,
            [
                'the hot Jupiter in WASP-47 either formed closer to its star or migrated inward through a gentler mechanism that does not inevitably eject neighboring rocky planets.',
                'the TESS space telescope is incapable of measuring the orbital shapes of gas giant planets accurately.',
                'most Earth-sized rocky worlds in our galaxy orbit stars far older than WASP-47.',
                'all hot Jupiters previously discovered by astronomers must be accompanied by hidden rocky planets.'
            ],
            'A',
            'Khuôn Mismatched Exception (1-Millimeter Rule): Tiền đề 1 = Giả định cũ cho rằng sự di cư của hot Jupiter luôn hất văng các hành tinh đá nhỏ. Tiền đề 2 = WASP-47 có cả hot Jupiter lẫn 2 hành tinh đá nhỏ quay ổn định tròn đều ngay cạnh nhau → Kết luận 1mm: Hot Jupiter ở WASP-47 hình thành gần sao hơn hoặc di cư nhẹ nhàng hơn mà không nhất thiết hất văng hành tinh đá lân cận (A)!',
            'Chỉ bước đúng 1 milimét: 1 ngoại lệ (WASP-47) đủ chứng minh quy luật cũ "không phải lúc nào cũng xảy ra" (does not inevitably), nhưng KHÔNG đủ suy rộng sang "all hot Jupiters" (D)!',
            [
                ('Đáp án đúng', 'Suy diễn 1mm cực chặt từ ngoại lệ WASP-47: mở ra khả năng hình thành gần sao hoặc di cư ôn hòa không tất yếu hất văng hành tinh đá.'),
                ('Out of Scope', 'Bài không hề nghi ngờ độ chính xác của kính thiên văn TESS.'),
                ('Out of Scope', 'Không có bất kỳ dữ kiện nào về tuổi sao hay phần lớn hành tinh đá trong thiên hà.'),
                ('Too Extreme (All Trap)', 'Một hệ sao (WASP-47) không thể chứng minh TẤT CẢ các hot Jupiter khác đều có hành tinh đá ẩn.'),
            ]
        ),
        q_item(
            'd5_5_q2', 2, 'Information and Ideas', 'Inferences', 'Elite (750+)',
            '<p>To estimate historical literacy rates in eighteenth-century rural France, demographers have long counted the proportion of brides and grooms able to sign their own names on marriage registers rather than drawing a simple cross. Historians note, however, that village schools of the era taught reading first—often to children who left school to work the harvest before ever receiving writing instruction. Consequently, relying strictly on marriage-register signatures likely ______</p>',
            stem,
            [
                'proves that rural French children were forbidden from learning to read before learning to write.',
                'underestimates the proportion of eighteenth-century rural French adults who were actually able to read.',
                'overstates the percentage of villagers who worked on farms during harvest season.',
                'demonstrates that brides had consistently higher writing proficiency than grooms across rural France.'
            ],
            'B',
            'Ghép 2 tiền đề (Methodological Caveat): (A) Nhà nhân khẩu đo tỉ lệ biết chữ chỉ bằng việc KÝ ĐƯỢC TÊN (viết). (B) Trường làng dạy ĐỌC trước, nhiều em bỏ học đi gặt trước khi kịp học VIẾT → Vậy có nhiều người BIẾT ĐỌC nhưng KHÔNG BIẾT KÝ TÊN → Chỉ đếm chữ ký sẽ ĐÁNH GIÁ THẤP (underestimates) tỉ lệ người thực sự biết đọc! Chọn B!',
            'Xác định chiều lệch của phương pháp đo (Bias Direction): Có nhóm người Biết Đọc nhưng không qua bài kiểm tra Ký Tên → bài kiểm tra Ký Tên cho con số THẤP HƠN thực tế (underestimates)!',
            [
                ('Reversed Logic', 'Bài nói ngược lại: trẻ được dạy đọc TRƯỚC khi dạy viết, không hề bị cấm.'),
                ('Đáp án đúng', 'Suy luận toán học chặt chẽ: vì nhiều người biết đọc nhưng chưa kịp học viết chữ ký, nên đếm chữ ký sẽ đánh giá thấp tỉ lệ biết đọc thực tế.'),
                ('Out of Scope', 'Số chữ ký kết hôn không đo tỉ lệ người làm nông mùa gặt.'),
                ('Out of Scope', 'Đoạn văn không so sánh trình độ giữa cô dâu và chú rể.'),
            ]
        ),
        q_item(
            'd5_5_q3', 3, 'Information and Ideas', 'Inferences', 'Elite (750+)',
            '<p>In an effort to reduce electricity usage during summer peaks, a regional utility introduced "smart" thermostats that automatically raise indoor cooling setpoints by 2°C during afternoon surges. A follow-up audit found that although total peak electricity fell by 11% across participating homes, nearly a third of households manually overrode the thermostat—turning temperatures down even colder than usual right before the afternoon surge to "pre-cool" their rooms, which shifted part of the load into the late morning. Therefore, evaluating the program solely by measuring afternoon peak electricity reduction may ______</p>',
            stem,
            [
                'show that smart thermostats failed to lower afternoon peak electricity use at all.',
                'prove that households prefer warmer indoor temperatures during late-morning hours.',
                'overstate the program’s net daily electricity savings by overlooking extra energy consumed during pre-cooling hours.',
                'eliminate the need for electric utilities to monitor indoor temperatures altogether.'
            ],
            'C',
            'Khuôn Trade-Off / Double Effect: (A) Điện giờ cao điểm buổi chiều giảm 11% (+); (B) Gần 1/3 hộ bật lạnh sâu hơn vào cuối buổi sáng để "làm mát trước" (−). Do đó nếu CHỈ đo mức giảm điện buổi chiều → sẽ PHÓNG ĐẠI / ĐÁNH GIÁ QUÁ CAO mức tiết kiệm điện ròng cả ngày (overstate net daily savings) vì bỏ sót lượng điện tăng thêm buổi sáng! Chọn C!',
            'Hiệu ứng dịch chuyển tải (giảm chiều, tăng sáng) → chỉ nhìn chiều sẽ làm con số tiết kiệm ròng bị THỔI PHỒNG (overstate)!',
            [
                ('Contradiction', 'Điện cao điểm buổi chiều THỰC SỰ đã giảm 11%, không phải không giảm chút nào.'),
                ('Reversed Logic', 'Họ chỉnh LẠNH HƠN bình thường buổi sáng, không phải thích ấm hơn.'),
                ('Đáp án đúng', 'Chốt chuẩn xác hệ quả đo lường: bỏ qua điện tiêu thụ thêm khi làm mát trước sẽ khiến mức tiết kiệm ròng cả ngày bị đánh giá quá cao.'),
                ('Out of Scope / Too Extreme', 'Không liên quan đến việc xóa bỏ nhu cầu theo dõi nhiệt độ.'),
            ]
        ),
        q_item(
            'd5_5_q4', 4, 'Information and Ideas', 'Inferences', 'Hard',
            '<p>Paleontologists studying the Late Cretaceous Hell Creek Formation frequently find intact skeletons of large herbivorous dinosaurs such as <i>Triceratops</i>, yet very few fossils of small, delicate-boned tree-dwelling birds from the same era. Because acidic floodplain soils in Hell Creek dissolve thin, hollow bones rapidly before mineralization can occur, paleontologists caution that the scarcity of small bird fossils in the formation ______</p>',
            stem,
            [
                'proves that small tree-dwelling birds had already gone extinct before <i>Triceratops</i> evolved.',
                'confirms that <i>Triceratops</i> skeletons were completely immune to chemical weathering.',
                'indicates that small birds lived exclusively outside North America during the Late Cretaceous.',
                'does not necessarily reflect low historical abundance of those birds, as preservation bias favored thicker skeletons.'
            ],
            'D',
            'Khuôn Preservation Bias (cực hay thi trong bài Khảo cổ/Cổ sinh SAT!): (A) Tìm thấy rất ít hóa thạch chim xương nhỏ rỗng; (B) Đất đồng bằng có tính axit hòa tan nhanh xương mỏng rỗng trước khi kịp hóa đá → Kết luận thận trọng: Sự hiếm hoi hóa thạch KHÔNG NHẤT THIẾT chứng tỏ xưa ít chim, mà do thiên lệch bảo quản ưu ái xương lớn dày! Chọn D!',
            'Gặp câu hỏi có chữ "caution that..." trong bài cổ sinh → gần như luôn chọn ngôn ngữ thận trọng "does not necessarily reflect..."!',
            [
                ('Over-Extrapolation', 'Sự khan hiếm hóa thạch do đất axit hòa tan KHÔNG chứng minh loài chim đã tuyệt chủng.'),
                ('Too Extreme', 'Chữ "completely immune" (miễn nhiễm hoàn toàn) quá cực đoan và không có trong bài.'),
                ('Out of Scope', 'Không thể suy ra loài chim chỉ sống ngoài Bắc Mỹ khi đất ở Hell Creek làm tan xương chúng.'),
                ('Đáp án đúng', 'Phản ánh chính xác lập luận thiên lệch bảo quản (preservation bias) với ngôn từ thận trọng chuẩn khoa học.'),
            ]
        ),
        q_item(
            'd5_5_q5', 5, 'Information and Ideas', 'Inferences', 'Elite (750+)',
            '<p>Linguist Dr. Elena Sorokina compared vocabulary retention among adults studying Finnish through two smartphone apps. App X presented new words alongside vivid cartoon illustrations, whereas App Y presented the exact same words inside short audio dialogues without pictures. On a vocabulary test administered immediately after one week of study, App X users outscored App Y users by 19%; however, when both groups were retested unexpectedly six weeks later without additional review, App Y users outperformed App X users by 14%. Taken together, these results suggest that ______</p>',
            stem,
            [
                'immediate post-study test scores alone may not reliably predict which instructional method promotes superior long-term vocabulary retention.',
                'cartoon illustrations prevent adult learners from recognizing Finnish words during the first week of study.',
                'App Y users spent significantly more hours reviewing Finnish dialogues between week one and week six than App X users did.',
                'audio dialogues are ineffective for teaching any language other than Finnish.'
            ],
            'A',
            'Ghép 2 kết quả đảo chiều theo thời gian: Tuần 1 (thi ngay) App X thắng +19% ↔ Tuần 6 (thi bất ngờ không ôn thêm) App Y lật ngược thắng +14%! Kết luận 1mm: Điểm kiểm tra ngay sau khi học KHÔNG đáng tin để dự đoán phương pháp nào giúp ghi nhớ dài hạn tốt hơn (A)! Loại C vì đề nêu rõ "without additional review"!',
            'Đọc cực kỹ cụm loại biến nhiễu "without additional review" — nó giết chết bẫy C ngay lập tức!',
            [
                ('Đáp án đúng', 'Tổng hợp chính xác sự đảo chiều giữa kết quả ngắn hạn (tuần 1) và dài hạn (tuần 6).'),
                ('Contradiction', 'Ở tuần đầu, nhóm dùng tranh hoạt hình (App X) thắng tới +19%, không hề bị cản trở.'),
                ('Contradiction', 'Đề nói rõ cả hai nhóm thi lại bất ngờ "without additional review" (không ôn thêm).'),
                ('Out of Scope / Too Extreme', 'Không thể suy rộng sang mọi ngôn ngữ khác ngoài tiếng Phần Lan.'),
            ]
        ),
        q_item(
            'd5_5_q6', 6, 'Information and Ideas', 'Inferences', 'Elite (750+)',
            '<p>In 2018, marine biologists noticed that juvenile green sea turtles off Okinawa frequently congregated near floating mats of brown <i>Sargassum</i> seaweed. One team proposed that the seaweed primarily offered shade from intense tropical ultraviolet radiation; another proposed that it provided a dense food source of tiny crabs and shrimp hiding inside the fronds. When researchers anchored identical dark shade cloths made of inert synthetic mesh—which blocked sunlight just as effectively as <i>Sargassum</i> but harbored virtually no crustaceans—juvenile turtles largely ignored the artificial mats. Consequently, the researchers concluded that ______</p>',
            stem,
            [
                'juvenile green sea turtles are unable to distinguish natural brown seaweed from dark synthetic mesh.',
                'protection from ultraviolet sunlight alone is unlikely to be the primary factor attracting juvenile turtles to <i>Sargassum</i> mats.',
                'floating <i>Sargassum</i> mats completely block all ultraviolet light from reaching coastal waters off Okinawa.',
                'adult green sea turtles feed exclusively on tiny crabs and shrimp rather than marine plants.'
            ],
            'B',
            'Khuôn Either/Or Elimination: 2 giả thuyết (X1 = Che nắng UV vs. X2 = Nguồn thức ăn cua/tôm nhỏ). Thí nghiệm giữ X1 (tấm vải lưới che nắng tốt ngang nhau) nhưng bỏ X2 (không có cua/tôm) → rùa phớt lờ hoàn toàn! Kết luận 1mm: Riêng việc che nắng UV khó có thể là yếu tố chính thu hút rùa non tới thảm rong biển (B)!',
            'Thí nghiệm giữ X1 + loại X2 → Kết quả Y biến mất ⇒ X1 đơn lẻ KHÔNG đủ tạo ra Y!',
            [
                ('Contradiction', 'Rùa phớt lờ vải nhân tạo nhưng tụ tập quanh rong thật → chứng tỏ chúng PHÂN BIỆT RẤT RÕ!'),
                ('Đáp án đúng', 'Loại trừ chuẩn xác yếu tố che nắng đơn lẻ nhờ thí nghiệm đối chứng với lưới che nắng không có thức ăn.'),
                ('Too Extreme / Out of Scope', 'Không có dữ kiện nào nói rong chặn 100% tia UV của toàn vùng biển.'),
                ('Out of Scope / Wrong Group', 'Bài chỉ nghiên cứu rùa NON ("juvenile"), không bàn chế độ ăn độc quyền của rùa trưởng thành.'),
            ]
        ),
        q_item(
            'd5_5_q7', 7, 'Information and Ideas', 'Inferences', 'Hard',
            '<p>Because classical Roman concrete structures such as the Pantheon’s dome have endured two millennia without steel reinforcement, engineers long assumed that small white lumps of unmixed quicklime embedded inside ancient Roman mortar were simply signs of sloppy mixing. Yet microscopic imaging in 2023 revealed that whenever rainwater seeps into hairline cracks, those unreacted lime nodules dissolve and recrystallize as solid calcium carbonate, sealing fractures shut within weeks. Therefore, what modern engineers once dismissed as a manufacturing defect ______</p>',
            stem,
            [
                'was actually introduced during nineteenth-century restoration repairs rather than original Roman construction.',
                'explains why Roman concrete domes are lighter in weight than modern steel-reinforced bridges.',
                'actually functioned as a self-healing mechanism that contributed to Roman concrete’s extraordinary durability.',
                'prevented ancient Roman builders from constructing harbor breakwaters submerged in seawater.'
            ],
            'C',
            'Tiền đề 1: Từng bị coi là lỗi trộn ẩu (sloppy mixing / defect). Tiền đề 2: Ảnh vi mô 2023 phát hiện cục vôi sống đó hòa tan khi gặp nước mưa và tái kết tinh bít kín vết nứt trong vài tuần → Kết luận 1mm: Thứ từng bị chê là lỗi sản xuất thực chất là cơ chế TỰ CHỮA LÀNH góp phần tạo nên độ bền phi thường của bê tông La Mã! Chọn C!',
            'Cấu trúc đảo ngược kinh điển trên SAT: "long assumed to be a flaw/defect → actually revealed to be a functional advantage"!',
            [
                ('Out of Scope', 'Không có chi tiết nào về trùng tu thế kỷ 19.'),
                ('Out of Scope', 'Đoạn văn không so sánh trọng lượng với cầu thép hiện đại.'),
                ('Đáp án đúng', 'Nối thẳng cơ chế tái kết tinh bít vết nứt với độ bền 2.000 năm của bê tông La Mã.'),
                ('Out of Scope / Contradiction', 'Bài không nhắc đê chắn sóng cảng biển bị cản trở.'),
            ]
        ),
        q_item(
            'd5_5_q8', 8, 'Information and Ideas', 'Inferences', 'Elite (750+)',
            '<p>Botanists studying coffee plantations in Colombia observed that shade-grown coffee trees yielded roughly 15% fewer beans per hectare in a single harvest year than full-sun monoculture plantations. However, shade-grown farms maintained diverse populations of insect-eating songbirds that suppressed coffee berry borer beetles naturally without synthetic pesticides, and their trees remained productive for over twenty-five years—whereas full-sun trees required costly chemical spraying and typically became exhausted and had to be replanted after twelve years. Accordingly, judging the economic viability of shade-grown coffee strictly by single-year harvest volume ______</p>',
            stem,
            [
                'proves that full-sun coffee plantations require less chemical pesticide than shaded farms.',
                'guarantees that shade-grown coffee farmers always earn higher annual profits than full-sun farmers.',
                'demonstrates that songbirds prefer nesting inside full-sun monoculture plantations.',
                'fails to capture longer-term cost savings from natural pest control and extended tree lifespan.'
            ],
            'D',
            'Khuôn Scope Limitation / Trade-Off: So sánh ngắn hạn 1 năm: Shade kém hơn 15% sản lượng; nhưng dài hạn: tiết kiệm thuốc trừ sâu nhờ chim tự nhiên + tuổi thọ cây gấp đôi (>25 năm vs. 12 năm không phải trồng lại). Vậy nếu CHỈ đánh giá bằng sản lượng 1 năm duy nhất → bỏ sót các khoản tiết kiệm chi phí dài hạn từ kiểm soát sâu tự nhiên và tuổi thọ cây lâu hơn (D)! Cẩn thận bẫy B ("guarantees always higher profits" — quá cực đoan vì bài không đưa giá bán hay bảng lợi nhuận cụ thể!).',
            'Cảnh giác bẫy Too Extreme (B: "guarantees always higher profits"): đoạn văn cho biết có lợi ích dài hạn bị bỏ sót (D), nhưng chưa cho đủ số liệu tài chính để "đảm bảo luôn lãi cao hơn"!',
            [
                ('Reversed Logic', 'Ngược hoàn toàn: chính đồn điền nắng gắt mới cần phun hóa chất tốn kém ("costly chemical spraying").'),
                ('Too Extreme (Guarantees Always)', 'Đoạn văn không đưa giá thị trường hay tổng chi phí lao động để khẳng định "always earn higher profits".'),
                ('Reversed Logic', 'Chim ăn sâu sống đa dạng ở đồn điền CÓ BÓNG RÂM (shade-grown).'),
                ('Đáp án đúng', 'Bắt đúng thiếu sót của thước đo 1 năm: bỏ qua lợi thế chi phí dài hạn về kiểm soát sâu tự nhiên và tuổi thọ cây.'),
            ]
        ),
        q_item(
            'd5_5_q9', 9, 'Information and Ideas', 'Inferences', 'Elite (750+)',
            '<p>Because deep-sea anglerfish live in perpetual darkness at depths exceeding 1,000 meters where potential mates are extraordinarily rare, evolutionary biologists wondered how males manage to locate females across vast empty ocean volumes. Genetic sequencing of deep-sea anglerfish recently revealed that males possess vastly enlarged olfactory organs alongside dozens of intact pheromone-receptor genes that are completely nonfunctional in females of the exact same species. This genetic asymmetry strongly suggests that ______</p>',
            stem,
            [
                'male anglerfish rely heavily on detecting female chemical cues across dark waters to locate mates.',
                'female anglerfish hunt prey primarily by following faint pheromone trails released by males.',
                'deep-sea anglerfish evolved in sunlit shallow reefs before migrating downward during the past century.',
                'both male and female anglerfish possess identical sensory organs adapted for visual mate recognition.'
            ],
            'A',
            'Ghép 2 tiền đề (1-Millimeter Rule): (A) Biển sâu tối đen 100%, bạn tình cực hiếm → câu hỏi làm sao con đực tìm thấy con cái; (B) Con đực có cơ quan khứu giác phì đại + hàng chục gen thụ thể pheromone hoạt động mạnh, trong khi các gen đó bất hoạt hoàn toàn ở con cái ⇒ Kết luận 1mm: Con đực dựa chủ yếu vào việc đánh hơi tín hiệu hóa học (pheromone) của con cái trong bóng tối để tìm bạn tình (A)!',
            'Khớp chính xác chiều bất đối xứng: Con đực có khứu giác + thụ thể pheromone mạnh → Con đực đi tìm con cái bằng tín hiệu hóa học!',
            [
                ('Đáp án đúng', 'Suy ra trực tiếp 1mm từ cơ quan khứu giác phì đại và bộ gen thụ thể pheromone chuyên biệt ở con đực.'),
                ('Reversed Logic', 'Gen thụ thể pheromone bất hoạt hoàn toàn ở con cái — không thể là con cái lần theo mùi con đực.'),
                ('Out of Scope', 'Không có dữ kiện nào về việc di cư từ rạn nông trong thế kỷ qua.'),
                ('Contradiction', 'Môi trường tối vĩnh viễn và hai giới có cơ quan cảm giác bất đối xứng hoàn toàn, không hề giống nhau hay dựa vào thị giác.'),
            ]
        ),
        q_item(
            'd5_5_q10', 10, 'Information and Ideas', 'Inferences', 'Elite (750+)',
            '<p>Historians studying nineteenth-century whaling logbooks noticed that the average distance ships sailed to harvest a single barrel of whale oil doubled between 1830 and 1860, even as shipbuilders introduced faster hull designs and explosive harpoons that dramatically improved hunting efficiency. Economic historians point out that if whale populations had remained stable, technological improvements would have shortened voyages rather than lengthening them. Thus, the logbook trend implies that ______</p>',
            stem,
            [
                'explosive harpoons were less effective at capturing whales than earlier hand-thrown lances.',
                'rapid depletion of accessible whale stocks outpaced gains in nineteenth-century whaling technology.',
                'whaling captains deliberately chose longer scenic routes between 1830 and 1860 to avoid coastal storms.',
                'global demand for whale oil vanished entirely after 1830 due to new hull designs.'
            ],
            'B',
            'Khuôn Trade-Off / Counterfactual Deduction: Công nghệ đánh bắt (tàu nhanh hơn + lao nổ) đáng lẽ phải RÚT NGẮN hành trình nếu đàn cá voi ổn định; thế nhưng quãng đường đi săn thực tế lại TĂNG GẤP ĐÔI (1830–1860)! Kết luận tất yếu: Sự cạn kiệt nhanh chóng của các đàn cá voi dễ tiếp cận đã lấn át cả tiến bộ công nghệ săn bắt! Chọn B!',
            'Áp dụng phép phản chứng có sẵn trong bài: "If whale populations had remained stable → voyages would have shortened. Thực tế: voyages doubled → whale populations severely depleted!"',
            [
                ('Contradiction', 'Đoạn văn nói rõ lao nổ "dramatically improved hunting efficiency".'),
                ('Đáp án đúng', 'Phép suy luận phản chứng hoàn hảo: đàn cá voi cạn kiệt nhanh hơn tốc độ cải tiến công nghệ.'),
                ('Out of Scope', 'Không có chuyện thuyền trưởng cố tình đi đường vòng ngắm cảnh tránh bão.'),
                ('Out of Scope / Contradiction', 'Nhu cầu không biến mất — các tàu vẫn tăng cường công nghệ và đi xa gấp đôi để săn dầu cá voi.'),
            ]
        ),
        q_item(
            'd5_5_q11', 11, 'Information and Ideas', 'Inferences', 'Hard',
            '<p>Before launching a redesigned mobile banking app, product researchers tested two onboarding tutorials: Tutorial A walked users through all twelve app features upfront in a mandatory five-minute video, whereas Tutorial B skipped the video entirely and surfaced brief ten-second tooltips only when a user actually tapped a specific feature for the first time. One month after launch, Tutorial B users completed complex bill-pay tasks 32% faster and contacted customer support half as often as Tutorial A users. Based on these outcomes, designers can reasonably infer that ______</p>',
            stem,
            [
                'presenting every feature in a mandatory upfront video is the most effective strategy for training users on complex financial apps.',
                'users who watched Tutorial A permanently forgot how to log into their mobile banking accounts.',
                'delivering brief, context-timed guidance at the moment of need helped users learn complex app features more effectively than front-loading all instructions at once.',
                'mobile banking users prefer longer instructional videos whenever an app introduces more than twelve features.'
            ],
            'C',
            'Tiền đề: Hướng dẫn dài 5 phút nhồi nhét từ đầu (A) thua hẳn hướng dẫn ngắn 10 giây bật đúng lúc người dùng bấm vào tính năng (B: nhanh hơn 32%, gọi hỗ trợ ít hơn một nửa). Kết luận 1mm: Cung cấp hướng dẫn ngắn đúng ngữ cảnh thời điểm cần thiết giúp người dùng học tính năng phức tạp hiệu quả hơn nhồi toàn bộ ngay từ đầu (C)!',
            'Bám sát bản chất biến độc lập tạo ra khác biệt: `upfront mandatory video` vs. `context-timed tooltips at the moment of need`!',
            [
                ('Reversed Logic', 'Tutorial A có kết quả KÉM HƠN hẳn Tutorial B ở cả tốc độ lẫn số lần gọi hỗ trợ.'),
                ('Too Extreme / Out of Scope', 'Không có dữ kiện nào nói họ quên vĩnh viễn cách đăng nhập.'),
                ('Đáp án đúng', 'Tóm gọn chính xác bài học thiết kế suy ra trực tiếp từ so sánh đối chứng A vs. B.'),
                ('Reversed Logic / Out of Scope', 'Kết quả chỉ ra hiệu quả của tooltip ngắn, không nói người dùng thích video dài hơn.'),
            ]
        ),
        q_item(
            'd5_5_q12', 12, 'Information and Ideas', 'Inferences', 'Elite (750+)',
            '<p>In a 2024 materials study, physicists discovered that twisting two atom-thin sheets of graphene at a precise "magic angle" of 1.1 degrees causes electrons to slow dramatically and pair up into a zero-resistance superconducting state—but only when the device is chilled to nearly −271°C and the twist angle stays accurate within 0.05 degrees across the entire wafer. Because current industrial lithography machines struggle to hold atomic-scale alignment within 0.05 degrees over centimeter-wide chips, engineers note that it is unlikely that ______</p>',
            stem,
            [
                'twisted bilayer graphene exhibits superconductivity under extreme laboratory cooling.',
                'physicists will continue investigating the theoretical behavior of electrons in graphene layers.',
                'current industrial lithography tools can reliably align macroscopic steel plates.',
                'magic-angle graphene superconductors will enter mass commercial electronics manufacturing without major advances in precision fabrication and cooling.'
            ],
            'D',
            'CẢNH BÁO PHỦ ĐỊNH NGAY TRƯỚC CHỖ TRỐNG: "...engineers note that **it is unlikely that** ______"! (KHÓ CÓ KHẢ NĂNG RẰNG điều gì xảy ra?). Tiền đề: Cần làm lạnh cực sâu −271°C + sai số góc xoắn ≤0.05° trên cả tấm wafer, nhưng máy công nghiệp hiện tại không đạt được độ chính xác đó trên chip cỡ cm ⇒ KHÓ CÓ KHẢ NĂNG công nghệ này bước vào sản xuất thương mại đại trà nếu chưa có đột phá lớn về chế tạo chính xác và làm lạnh (D)!',
            'Gặp "it is unlikely that ______" → đọc ghép cả cụm thành một câu hoàn chỉnh để kiểm tra chiều phủ định không bị ngược!',
            [
                ('Polarity Flip Trap!', 'Siêu dẫn ở nhiệt độ phòng thí nghiệm ĐÃ ĐƯỢC PHÁT HIỆN RỒI — nói "it is unlikely that..." sẽ thành phủ nhận chính phát hiện của bài!'),
                ('Polarity Flip / Out of Scope', 'Không có lý do gì nói các nhà vật lý sẽ ngừng nghiên cứu lý thuyết.'),
                ('Out of Scope', 'Đoạn văn không bàn về tấm thép vĩ mô.'),
                ('Đáp án đúng', 'Ghép hoàn hảo với "it is unlikely that": khó có khả năng thương mại hóa đại trà khi chưa vượt qua 2 nút thắt chế tạo chính xác và làm lạnh cực sâu.'),
            ]
        ),
        q_item(
            'd5_5_q13', 13, 'Information and Ideas', 'Inferences', 'Elite (750+)',
            '<p>When behavioral economists introduced clear calorie labels on chain-restaurant menus in a major city, average calories ordered per meal declined by 6% during the first three months. However, when researchers revisited the exact same restaurants eighteen months later, customer orders had drifted almost all the way back to pre-labeling levels—except at chains that had simultaneously reformulated their default menu items to contain fewer calories behind the scenes. These findings suggest that ______</p>',
            stem,
            [
                'menu labeling produces more durable calorie reductions when it prompts restaurants to reformulate recipes than when it relies solely on sustained conscious restraint by diners.',
                'customers completely ignored calorie labels during the first three months after menus were updated.',
                'restaurants that reformulated their recipes saw a sharp drop in overall customer satisfaction after eighteen months.',
                'mandating calorie labels causes average calories ordered per meal to rise by 6% over an eighteen-month period.'
            ],
            'A',
            'Ghép chuỗi tiền đề: (1) Chỉ dựa vào ý thức thực khách nhìn nhãn → giảm 6% lúc đầu rồi trôi về mức cũ sau 18 tháng; (2) Ngoại lệ duy nhất giữ được mức giảm bền vững là chuỗi nhà hàng đồng thời CẢI TIẾN CÔNG THỨC MẶC ĐỊNH ít calo hơn! Kết luận 1mm: Nhãn calo tạo mức giảm bền vững hơn khi thúc đẩy nhà hàng cải tiến công thức thay vì chỉ trông chờ vào sự tự kiềm chế lâu dài của thực khách (A)!',
            'Đọc kỹ cụm ngoại lệ vàng ("—except at chains that...") — chính cụm ngoại lệ đó định hình 100% kết luận ở chỗ trống!',
            [
                ('Đáp án đúng', 'Đối chiếu chính xác hiệu quả bền vững của việc cải tiến công thức nhà hàng với hiệu ứng phai dần của việc chỉ dựa vào ý thức thực khách.'),
                ('Contradiction', 'Trong 3 tháng đầu lượng calo ĐÃ GIẢM 6% — chứng tỏ khách không hề phớt lờ ngay từ đầu.'),
                ('Out of Scope', 'Đoạn văn không nhắc đến mức độ hài lòng của khách hàng.'),
                ('Fact Distortion', 'Calo chỉ quay gần về mức cũ (pre-labeling levels), không phải TĂNG thêm 6% trên mức cũ.'),
            ]
        ),
    ]
    return {
        'schemaVersion': 1,
        'mode': 'drill',
        'section': 'Reading and Writing',
        'basicInfo': {
            'title': 'Drill 5.5: Inferences — Hard Module 2 Deductive Completion (13 Qs)',
            'subtitle': 'Luyện Quy tắc 1 Milimét trên 4 khuôn suy diễn Hard Module 2 (Elimination, Preservation Bias, Trade-Off, Polarity Flip "it is unlikely that").',
            'difficultyBadge': 'I&I • Target 1500+',
            'targetTimeMinutes': 16,
        },
        'drillModule': {
            'id': 'drill_5_5_mod',
            'title': 'Skill Drill 5.5: Inferences (1-Millimeter Deduction)',
            'timeLimitMinutes': 16,
            'questions': questions,
        },
    }
