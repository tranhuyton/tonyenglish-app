# -*- coding: utf-8 -*-
"""
Full-Length Adaptive Mock Test #1 — Module 2 LOWER/STANDARD Route (27 Qs, Easy/Medium, 32 min)
Exact College Board Digital SAT R&W Blueprint.
"""

from sat_drills_1_1_and_2_1 import q_item
from sat_drills_5_4_to_5_5 import svg_bar_chart, html_table

def get_m2l_questions():
    return [
        # --- Q1-Q5: Words in Context (Easy / Medium) ---
        q_item(
            'm1_m2l_q1', 1, 'Craft and Structure', 'Words in Context', 'Easy',
            '<p>Because wooden sailing ships quickly rotted when berthed in warm tropical harbors inhabited by shipworms, eighteenth-century naval engineers began sheathing hulls in thin copper plates to ______ timber decay during long voyages.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            ['prevent', 'accelerate', 'celebrate', 'imitate'],
            'A',
            'Cause-Effect Clue: tàu gỗ nhanh mục vì hà biển → bọc đồng mỏng để NGĂN NGỪA sự mục nát gỗ → "prevent" (A).',
            'Xác định mục tiêu hành động bảo vệ thân tàu → chọn động từ nghĩa "ngăn chặn".',
            [
                ('Đáp án đúng', 'prevent = ngăn ngừa — khớp hoàn hảo mục đích bọc đồng bảo vệ gỗ khỏi hà biển.'),
                ('Opposite Meaning', 'accelerate = đẩy nhanh tốc độ mục nát — ngược hoàn toàn mục đích.'),
                ('Wrong Meaning', 'celebrate = ăn mừng — vô nghĩa.'),
                ('Wrong Meaning', 'imitate = bắt chước — sai logic.'),
            ]
        ),
        q_item(
            'm1_m2l_q2', 2, 'Craft and Structure', 'Words in Context', 'Easy',
            '<p>Although violinist Clara Schumann composed numerous chamber pieces early in her career, she later focused predominantly on concert touring across Europe, earning ______ praise from audiences and fellow musicians alike for her expressive precision.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            ['reluctant', 'widespread', 'hostile', 'accidental'],
            'B',
            'Mirror Clue: "from audiences and fellow musicians alike for her expressive precision" (cả khán giả lẫn đồng nghiệp đều ca ngợi) → sự tán dương RỘNG KHẮP → "widespread" (B).',
            'Cụm "audiences and fellow musicians alike" báo hiệu quy mô phổ biến rộng khắp ("widespread").',
            [
                ('Negative Tone', 'reluctant = miễn cưỡng — mâu thuẫn với sự ghi nhận nồng nhiệt của cả khán giả lẫn đồng nghiệp.'),
                ('Đáp án đúng', 'widespread = rộng khắp — khớp hoàn toàn với sự khen ngợi trên khắp châu Âu.'),
                ('Opposite Meaning', 'hostile = thù địch — trái nghĩa với "praise".'),
                ('Wrong Meaning', 'accidental = tình cờ — sai ngữ cảnh tài năng âm nhạc.'),
            ]
        ),
        q_item(
            'm1_m2l_q3', 3, 'Craft and Structure', 'Words in Context', 'Medium',
            '<p>In 2020, astronomers using the ALMA observatory detected faint radio signals from a nursery of newborn stars hidden behind dense interstellar dust clouds that normally ______ visible starlight from reaching Earth-based optical telescopes.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            ['amplify', 'generate', 'obstruct', 'simplify'],
            'C',
            'Mirror Clue: "hidden behind dense interstellar dust clouds" → đám mây bụi dày đặc CẢN TRỞ / CHẶN ĐỨNG ánh sáng khả kiến → "obstruct" (C).',
            'Từ khóa "hidden behind dense dust clouds" dẫn thẳng tới động từ "obstruct / block".',
            [
                ('Opposite Meaning', 'amplify = khuếch đại — ngược hoàn toàn với "hidden behind".'),
                ('Wrong Meaning', 'generate = tạo ra — bụi không tạo ra ánh sáng sao.'),
                ('Đáp án đúng', 'obstruct = cản trở, chắn lối — khớp hoàn toàn với mây bụi dày che khuất ngôi sao.'),
                ('Wrong Context', 'simplify = đơn giản hóa — không dùng với ánh sáng.'),
            ]
        ),
        q_item(
            'm1_m2l_q4', 4, 'Craft and Structure', 'Words in Context', 'Medium',
            '<p>While the museum’s main entrance hall is grand and echoing, the adjacent textile reading room was purposefully designed to feel ______, with low oak ceilings, soft desk lamps, and plush wool rugs.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            ['forbidding', 'chaotic', 'barren', 'intimate'],
            'D',
            'Contrast + Restatement Clue: đối lập với "grand and echoing" (rộng lớn vang vọng) + mô tả "low oak ceilings, soft desk lamps, plush wool rugs" → ẤM CÚNG, GẦN GŨI → "intimate" (D).',
            'Cặp đối lập kiến trúc thường gặp trên SAT: grand/echoing (đồ sộ vang vọng) ↔ intimate/cozy (ấm cúng thân mật).',
            [
                ('Negative Tone', 'forbidding = đáng sợ lạnh lẽo — ngược hoàn toàn với đèn bàn dịu và thảm len êm.'),
                ('Negative Tone', 'chaotic = hỗn loạn — trái ngược phòng đọc yên tĩnh.'),
                ('Opposite Meaning', 'barren = trống trải cằn cỗi — trái với nội thất gỗ sồi và thảm dày.'),
                ('Đáp án đúng', 'intimate = ấm cúng, thân mật — đối lập hoàn hảo với đại sảnh rộng vang.'),
            ]
        ),
        q_item(
            'm1_m2l_q5', 5, 'Craft and Structure', 'Words in Context', 'Medium',
            '<p>Because desert bighorn sheep rely on widely scattered mountain springs during scorching summer months, wildlife agencies map every reliable waterhole carefully so highway fencing does not ______ the animals’ seasonal routes.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            ['sever', 'broaden', 'repair', 'illuminate'],
            'A',
            'Cause-Effect Clue: cừu sừng lớn phụ thuộc các con suối rải rác → lập bản đồ cẩn thận để hàng rào cao tốc không CẮT ĐỨT tuyến đường di chuyển theo mùa của chúng → "sever" (A).',
            'Hàng rào cao tốc cắt ngang đường đi của động vật hoang dã → động từ chuẩn là "sever" (cắt đứt).',
            [
                ('Đáp án đúng', 'sever = cắt đứt hoàn toàn đường đi/kết nối — khớp chuẩn xác với rủi ro từ hàng rào cao tốc.'),
                ('Opposite Meaning', 'broaden = mở rộng — hàng rào không mở rộng tuyến đường của cừu.'),
                ('Wrong Meaning', 'repair = sửa chữa — sai nghĩa.'),
                ('Wrong Meaning', 'illuminate = soi sáng — không hợp bối cảnh hàng rào cao tốc.'),
            ]
        ),

        # --- Q6-Q7: Text Structure and Purpose (Easy / Medium) ---
        q_item(
            'm1_m2l_q6', 6, 'Craft and Structure', 'Text Structure and Purpose', 'Easy',
            '<p>Every summer, thousands of humpback whales migrate more than 5,000 kilometers from warm tropical breeding lagoons to cold Alaskan fjords. <u>They undertake this grueling journey because nutrient-rich northern currents fuel massive seasonal blooms of krill and herring during the long sunlit Arctic days.</u> By feeding intensively throughout summer, the whales build thick blubber reserves that sustain them during their winter return south.</p>',
            'Which choice best describes the function of the underlined sentence in the text as a whole?',
            [
                'It questions whether humpback whales actually migrate as far as 5,000 kilometers each year.',
                'It explains the primary ecological reason why humpback whales make the long seasonal migration introduced in the first sentence.',
                'It compares the swimming speed of humpback whales with that of krill and herring.',
                'It warns that Alaskan fjords are running out of nutrient-rich northern currents.'
            ],
            'B',
            'Câu 1 nêu sự kiện di cư hơn 5.000 km. Câu gạch chân mở đầu bằng "They undertake this grueling journey because..." — trực tiếp giải thích LÝ DO SINH THÁI của cuộc di cư (dòng hải lưu giàu dinh dưỡng tạo nguồn nhuyễn thể và cá trích dồi dào) → Chọn B!',
            'Cụm "They undertake this journey because..." chỉ thẳng chức năng "explain the reason why...".',
            [
                ('Contradiction', 'Câu gạch chân không hề nghi ngờ quãng đường 5.000 km.'),
                ('Đáp án đúng', 'Giải thích trực tiếp động lực nguồn thức ăn thúc đẩy cuộc di cư xa ở câu 1.'),
                ('Out of Scope', 'Không so sánh tốc độ bơi.'),
                ('Out of Scope', 'Không cảnh báo thiếu hụt dòng hải lưu.'),
            ]
        ),
        q_item(
            'm1_m2l_q7', 7, 'Craft and Structure', 'Text Structure and Purpose', 'Medium',
            '<p><i>The following text is adapted from a 1909 short story. Samuel is unpacking crates of books inside the modest frontier schoolhouse where he will teach his first class Monday morning.</i><br/>The pine floor tilted slightly toward the stove, and two windowpanes had been patched with brown wrapping paper against the draft. Still, as Samuel aligned twelve battered geography atlases along the chalk rail and smelled the fresh cedar shavings from his pencil sharpener, he smiled at the quiet room; rough as the walls were, every bench promised twenty curious pairs of eyes waiting to look far beyond the valley.</p>',
            'Which choice best states the main purpose of the text?',
            [
                'To complain that the frontier community failed to provide Samuel with enough geography atlases.',
                'To show that Samuel regrets leaving his previous teaching position for a poorly built schoolhouse.',
                'To illustrate Samuel’s quiet optimism and enthusiasm for teaching despite the humble condition of his new schoolroom.',
                'To explain how frontier settlers repaired broken schoolhouse windows using wrapping paper.'
            ],
            'C',
            'Câu 1 tả ngôi trường đơn sơ (sàn gỗ nghiêng, kính vá giấy). Câu 2 dùng "Still" làm nổi bật nụ cười và sự lạc quan háo hức của thầy giáo Samuel khi nghĩ tới 20 đôi mắt học trò tò mò sắp học tại đây → Chọn C!',
            'Nhận diện bước ngoặt cảm xúc sau từ "Still" (dù phòng học đơn sơ, nhân vật vẫn mỉm cười đầy hy vọng).',
            [
                ('Contradiction', 'Samuel xếp 12 tập bản đồ với niềm vui, không hề phàn nàn thiếu sách.'),
                ('Contradiction', 'Anh mỉm cười háo hức ("he smiled... promised twenty curious pairs of eyes"), hoàn toàn không hối tiếc.'),
                ('Đáp án đúng', 'Bắt trọn sự lạc quan và nhiệt huyết dạy học của Samuel bất chấp điều kiện phòng học mộc mạc.'),
                ('Too Narrow', 'Chi tiết vá cửa kính chỉ làm nền cho hoàn cảnh đơn sơ, không phải mục đích hướng dẫn sửa cửa.'),
            ]
        ),

        # --- Q8: Cross-Text Connections (Medium) ---
        q_item(
            'm1_m2l_q8', 8, 'Craft and Structure', 'Cross-Text Connections', 'Medium',
            '<p><b>Text 1</b><br/>Urban planner Dr. Robert Miller recommends replacing traditional four-way traffic-light intersections with circular roundabouts, arguing that roundabouts cut severe side-impact collisions sharply because drivers must slow down and yield before entering the circle.</p><p><b>Text 2</b><br/>Studying traffic data from thirty mid-sized towns that converted signalized crossroads into single-lane roundabouts, safety engineer Dr. Priya Shah confirmed a 65% drop in serious vehicle crashes. However, Shah notes that cities installing roundabouts near elementary schools should add raised crosswalks and flashing pedestrian beacons so young walkers can cross safely without waiting for gaps in continuously flowing traffic.</p>',
            'Based on the texts, how would Dr. Priya Shah (Text 2) most likely respond to Dr. Robert Miller’s recommendation (Text 1)?',
            [
                'By rejecting roundabouts completely because they increase severe side-impact collisions.',
                'By arguing that flashing pedestrian beacons should replace all traffic lights nationwide.',
                'By asserting that drivers never slow down when entering single-lane roundabouts.',
                'By agreeing that roundabouts dramatically lower serious car crashes, while recommending additional safety features for pedestrians near schools.'
            ],
            'D',
            'Text 2 xác nhận mạnh mẽ lợi ích của Text 1 ("confirmed a 65% drop in serious vehicle crashes"), đồng thời bổ sung khuyến nghị thêm vạch sang đường nâng cao và đèn nháy cho người đi bộ gần trường học → Partial Agreement + Safety Addition = Chọn D!',
            'Ghép 2 vế Text 2: `confirmed 65% drop` (đồng ý lợi ích xe cộ) + `However, should add raised crosswalks/beacons near schools` (bổ sung an toàn người đi bộ).',
            [
                ('Contradiction', 'Shah xác nhận giảm tới 65% tai nạn nghiêm trọng chứ không bác bỏ vòng xuyến.'),
                ('Out of Scope / Too Extreme', 'Shah chỉ khuyến nghị thêm đèn nháy cho người đi bộ ở vòng xuyến gần trường học.'),
                ('Contradiction', 'Không hề nói tài xế không giảm tốc độ.'),
                ('Đáp án đúng', 'Phản ánh trọn vẹn cả sự đồng thuận (giảm mạnh tai nạn ô tô) lẫn đề xuất bổ sung an toàn cho học sinh đi bộ.'),
            ]
        ),

        # --- Q9-Q10: Central Ideas and Details (Easy / Medium) ---
        q_item(
            'm1_m2l_q9', 9, 'Information and Ideas', 'Central Ideas and Details', 'Easy',
            '<p>At the ancient Mesoamerican metropolis of Teotihuacan near modern Mexico City, archaeologists uncovered spacious multi-family apartment compounds built around open central courtyards. Unlike the isolated huts typical of smaller villages, these stone-and-plaster compounds housed dozens of related artisan families together, featuring shared rainwater cisterns, plastered drainage floors, and dedicated workshops for crafting obsidian blades and ceramic figurines.</p>',
            'Which choice best states the main idea of the text?',
            [
                'Excavations at Teotihuacan show that ordinary artisans lived in well-planned multi-family apartment compounds equipped with shared infrastructure and workspaces.',
                'Residents of Teotihuacan abandoned stone apartment compounds to live in isolated wooden huts.',
                'Obsidian blades crafted in Teotihuacan were sold exclusively to merchants in South America.',
                'Teotihuacan lacked sufficient rainfall to sustain plastered courtyard cisterns.'
            ],
            'A',
            'Ý chính toàn đoạn: Các khu căn hộ đa gia đình ở Teotihuacan là nơi sinh sống của nhiều gia đình nghệ nhân với hạ tầng dùng chung quy củ (sân trong, bể chứa nước mưa, sàn thoát nước, xưởng chế tác đá hắc diện & gốm) → Chọn A!',
            'Tóm gọn đặc điểm nổi bật nhất được lặp lại xuyên suốt đoạn: multi-family compounds + shared infrastructure + artisan workshops.',
            [
                ('Đáp án đúng', 'Bao quát trọn vẹn mô hình khu căn hộ đa gia đình có hạ tầng dùng chung và xưởng nghề của nghệ nhân Teotihuacan.'),
                ('Contradiction', 'Bài đối chiếu khu căn hộ đá của Teotihuacan với túp lều riêng lẻ ở làng nhỏ, không nói họ bỏ sang ở lều.'),
                ('Out of Scope', 'Không nhắc thương nhân Nam Mỹ.'),
                ('Contradiction', 'Các khu nhà có sẵn bể chứa nước mưa và hệ thống thoát nước.'),
            ]
        ),
        q_item(
            'm1_m2l_q10', 10, 'Information and Ideas', 'Central Ideas and Details', 'Medium',
            '<p>Many deep-water squid possess specialized skin organs called photophores that emit faint downward blue light matching the dim sunlight filtering from the ocean surface above. By adjusting this glow to match ambient brightness, the squid erases its dark silhouette from beneath—a camouflage strategy known as counter-illumination that hides the animal from upward-gazing predators swimming deeper below.</p>',
            'According to the text, how does counter-illumination protect deep-water squid from predators swimming below them?',
            [
                'By blinding upward-gazing predators with sudden bursts of bright red light.',
                'By emitting downward blue light matched to surface brightness, erasing the squid’s dark shadow against the water above.',
                'By warming the surrounding water so deep-sea fish cannot track the squid’s scent.',
                'By signaling neighboring squid to form a defensive circle around the predator.'
            ],
            'B',
            'Câu hỏi Detail trực tiếp: Định vị cụm "counter-illumination" → phát ánh sáng xanh hướng xuống khớp với ánh sáng mờ từ mặt biển phía trên, xóa mờ chiếc bóng tối của con mực trước mắt kẻ săn mồi nhìn từ dưới lên → Paraphrase chính xác ở B!',
            'Soi thẳng định nghĩa ngay trước cụm "a camouflage strategy known as counter-illumination"!',
            [
                ('Fact Distortion', 'Bài nói ánh sáng XANH NHẸ khớp độ sáng nền ("faint downward blue light"), không phải chớp đỏ gây mù.'),
                ('Đáp án đúng', 'Diễn giải sát nghĩa hoàn toàn cơ chế xóa bóng tối bằng ánh sáng xanh hướng xuống khớp ánh sáng mặt biển.'),
                ('Out of Scope', 'Không liên quan nhiệt độ nước hay mùi hương.'),
                ('Out of Scope', 'Không nói đến hành vi báo hiệu bầy đàn tạo vòng tròn phòng thủ.'),
            ]
        ),

        # --- Q11-Q12: Command of Evidence — Textual (Medium) ---
        q_item(
            'm1_m2l_q11', 11, 'Information and Ideas', 'Command of Evidence (Textual)', 'Medium',
            '<p>Marine ecologist Dr. Grace Chen observed that harbor seals resting on floating glacial ice floes in Alaska rarely haul out on sandy beaches during spring pupping season even when beaches are nearby. Chen hypothesized that mother seals prefer floating ice floes primarily because deep surrounding water shields newborn pups from land predators such as wolves and brown bears.</p>',
            'Which finding, if true, would most directly support Dr. Grace Chen’s hypothesis?',
            [
                'Glacial ice floes in Alaskan fjords melt significantly faster in August than in May.',
                'Adult male harbor seals spend more hours diving for cod than mother seals do during spring.',
                'Harbor seals resting on isolated offshore rocky islets surrounded by deep water—where wolves and bears cannot swim—exhibit similarly high pup survival rates to seals on glacial ice floes, whereas pups born on mainland beaches suffer much higher predation by terrestrial carnivores.',
                'Harbor seal pups develop thick insulating blubber layers within their first three weeks of life.'
            ],
            'C',
            'Khóa giả thuyết Chen: Chọn băng trôi chủ yếu vì NƯỚC SÂU XUNG QUANH CHẮN KẺ SĂN MỒI TRÊN CẠN (sói, gấu nâu). Bằng chứng C so sánh đối chứng hoàn hảo: đảo đá xa bờ có nước sâu chắn sói/gấu có tỉ lệ sống sót cao ngang băng trôi, trong khi bãi biển đất liền bị thú ăn thịt trên cạn săn hại cao hơn hẳn! Chọn C!',
            'Tìm bằng chứng kiểm chứng trực tiếp yếu tố bảo vệ khỏi "land predators" bằng phép so sánh nơi có vs. không có thú săn mồi đất liền!',
            [
                ('Adjacent Topic Drift', 'Tốc độ tan băng tháng 8 không kiểm chứng giả thuyết tránh thú ăn thịt trên cạn.'),
                ('Adjacent Topic Drift', 'Thời gian lặn tìm cá tuyết của hải cẩu đực nằm ngoài giả thuyết.'),
                ('Đáp án đúng', 'Đối chiếu rõ rệt nơi được nước sâu chắn sói/gấu (tỉ lệ sống cao) với bãi biển đất liền (bị thú ăn thịt cạn tấn công nhiều).'),
                ('Adjacent Topic Drift', 'Lớp mỡ giữ ấm không giải thích việc tránh bãi biển đất liền.'),
            ]
        ),
        q_item(
            'm1_m2l_q12', 12, 'Information and Ideas', 'Command of Evidence (Textual)', 'Medium',
            '<p>In a literary essay on the 1916 novel <i>The Timber Line</i>, a student claims that the young surveyor, Owen, initially underestimates the physical difficulty of working in the northern mountains until his very first day climbing through snowdrifts humbles him.</p>',
            'Which quotation from <i>The Timber Line</i> most effectively illustrates the student’s claim?',
            [
                '“Owen packed two woolen blankets, a brass transit level, and a tin of roasted coffee inside his canvas rucksack.”',
                '“The timber camp sat beside a frozen creek roughly fourteen miles north of the county rail depot.”',
                '“Every autumn the logging company hired thirty additional laborers to haul pine trunks down to the river.”',
                '“Before boarding the train, Owen had boasted that mountain surveying sounded like a brisk holiday walk; by noon of his first ascent through hip-deep snow, lungs burning and calves trembling, he silently apologized to the ridge.”'
            ],
            'D',
            'Checklist 2 vế từ Claim: [1] Ban đầu xem nhẹ độ khó ("initially underestimates physical difficulty") + [2] Ngay ngày đầu leo tuyết đã bị khuất phục/khiêm tốn lại ("first day through snowdrifts humbles him"). A, B, C chỉ kể đồ đạc và vị trí trại. Duy nhất D khớp đủ cả hai vế: từng khoác lác đó chỉ như "chuyến đi dạo nghỉ mát" → đến trưa ngày leo đầu tiên qua tuyết ngập hông, phổi rát bắp chân run, anh thầm xin lỗi ngọn núi! Chọn D!',
            'Khớp đủ 2 chặng chuyển biến của Owen: tự tin thái quá lúc đầu → bị khuất phục ngay ngày đầu leo tuyết!',
            [
                ('Irrelevant Detail', 'Chỉ liệt kê vật dụng Owen bỏ vào ba lô.'),
                ('Irrelevant Setting', 'Chỉ mô tả vị trí trại gỗ.'),
                ('Wrong Focus', 'Chỉ nói việc công ty tuyển thêm nhân công mùa thu.'),
                ('Đáp án đúng', 'Thể hiện trọn vẹn sự chủ quan ban đầu ("boasted... brisk holiday walk") và cú sốc thực tế ngay trưa ngày leo đầu tiên qua tuyết sâu.'),
            ]
        ),

        # --- Q13-Q14: Command of Evidence — Quantitative (Easy / Medium) ---
        q_item(
            'm1_m2l_q13', 13, 'Information and Ideas', 'Command of Evidence (Quantitative)', 'Easy',
            svg_bar_chart(
                'Average Daily Ridership (Thousands) on Four City Ferry Routes (2024)',
                ['0', '5k', '10k', '15k', '20k'],
                [('North Pier', 18, '18k'), ('East Cove', 12, '12k'), ('South Bay', 9, '9k'), ('West Island', 15, '15k')],
                20
            ) + '<p>A harbor transit planner claims that North Pier carries twice as many average daily ferry passengers as South Bay.</p>',
            'Which choice best uses data from the graph to verify the transit planner’s claim?',
            [
                'North Pier averages 18,000 daily riders, which is exactly double the 9,000 daily riders averaged on the South Bay route.',
                'West Island averages 15,000 daily riders, making it the second busiest ferry route in the harbor.',
                'East Cove carries 12,000 average daily passengers, exceeding South Bay by 3,000 passengers.',
                'All four city ferry routes carry fewer than 20,000 average daily passengers.'
            ],
            'A',
            'Claim cần kiểm chứng: North Pier chở GẤP ĐÔI số khách mỗi ngày của South Bay. Đọc biểu đồ: North Pier = 18k, South Bay = 9k (18 = 2 × 9 → chính xác gấp đôi!) → Chọn A!',
            'Bám đúng 2 thanh dữ liệu mà Claim nêu tên: North Pier (18k) và South Bay (9k).',
            [
                ('Đáp án đúng', 'Xác thực chính xác số liệu 18.000 của North Pier gấp đúng 2 lần 9.000 của South Bay.'),
                ('True Data / Wrong Subject', 'Nói về West Island, không nhắc North Pier hay South Bay.'),
                ('True Data / Wrong Subject', 'So sánh East Cove với South Bay thay vì North Pier.'),
                ('True Data / Wrong Claim', 'Nhận xét chung <20.000 không kiểm chứng tỉ lệ gấp đôi giữa North Pier và South Bay.'),
            ]
        ),
        q_item(
            'm1_m2l_q14', 14, 'Information and Ideas', 'Command of Evidence (Quantitative)', 'Medium',
            html_table(
                'Table 3. Average Annual Rainfall (mm) and Reservoir Fill Level (%) Across Four Regions (2024)',
                ['Region', '2024 Annual Rainfall (mm)', 'Reservoir Fill Level (%)'],
                [
                    ['Valley North', '640', '88%'],
                    ['Coastal Plain', '920', '71%'],
                    ['Highland Basin', '510', '94%'],
                    ['River Delta', '780', '82%'],
                ]
            ) + '<p>A hydrology student asserts that regions with higher annual rainfall always maintain higher reservoir fill percentages than drier regions.</p>',
            'Which choice best describes data from the table that weaken the student’s assertion?',
            [
                'River Delta received 780 mm of annual rainfall and maintained a reservoir fill level of 82%.',
                'Although Coastal Plain received the highest annual rainfall at 920 mm, it recorded the lowest reservoir fill level at 71%—far below Highland Basin’s 94% fill level despite receiving only 510 mm of rain.',
                'Valley North received 640 mm of rainfall in 2024, which was more than Highland Basin’s 510 mm.',
                'All four surveyed regions maintained reservoir fill levels above 70% in 2024.'
            ],
            'B',
            'Claim cần WEAKEN: Mưa càng nhiều → mực nước hồ chứa (%) càng cao! Soi bảng thấy nghịch đảo rõ rệt: Coastal Plain mưa NHIỀU NHẤT (920 mm) nhưng hồ chứa THẤP NHẤT (71%), trong khi Highland Basin mưa ÍT NHẤT (510 mm) nhưng hồ đầy CAO NHẤT (94%)! Chọn B!',
            'Tìm ngay cặp cực trị đi ngược quy luật của Claim (Mưa nhiều nhất nhưng Hồ thấp nhất vs. Mưa ít nhất nhưng Hồ đầy nhất)!',
            [
                ('True Data / Wrong Claim', 'Chỉ đọc 1 hàng River Delta, không tạo phép so sánh bác bỏ quy luật.'),
                ('Đáp án đúng', 'Đối chiếu cực trị đảo ngược: Coastal Plain (920 mm → 71%) vs. Highland Basin (510 mm → 94%) đập tan chữ "always".'),
                ('Incomplete Data', 'Chỉ so lượng mưa giữa hai vùng mà bỏ quên cột mực nước hồ chứa.'),
                ('True Data / Wrong Claim', 'Chỉ nêu cả 4 vùng đều trên 70%, không bác bỏ quan hệ mưa nhiều ↔ hồ đầy.'),
            ]
        ),

        # --- Q15: Inferences (Medium) ---
        q_item(
            'm1_m2l_q15', 15, 'Information and Ideas', 'Inferences', 'Medium',
            '<p>Archaeologists studying bronze bells buried in ancient Chinese tombs from the fifth century BCE discovered that each bell was cast with an almond-shaped cross-section rather than a round circular shape. Acoustic testing revealed that striking the center of an almond-shaped bell produces one clear musical pitch, whereas striking its side edge produces a second distinct pitch a musical third apart—and unlike circular bells whose tones linger and clash together, the almond shape dampens vibrations quickly. Consequently, musicians performing with sets of these ancient bells could ______</p>',
            'Which choice most logically completes the text?',
            [
                'play only a single monotonous note per set of bronze bells during court ceremonies.',
                'rely on circular bronze bells to keep tones from clashing during rapid melodies.',
                'execute rapid, multi-note melodies clearly without lingering overtones blurring successive notes together.',
                'tune each bell’s pitch simply by bending its solid bronze walls by hand during a performance.'
            ],
            'C',
            'Ghép 2 tiền đề (1-Millimeter Rule): (A) Mỗi chuông tạo được 2 cao độ rõ nét khác nhau (tùy gõ giữa hay cạnh); (B) Hình quả hạnh dập tắt độ ngân nhanh để âm trước không hòa nhòe vào âm sau ⇒ Kết luận 1mm: Nhạc công có thể chơi các giai điệu nhanh nhiều nốt một cách rõ ràng mà không bị dư âm trước làm nhòe nốt sau (C)!',
            'Nối thẳng 2 lợi ích vật lý vừa nêu (`2 distinct pitches` + `dampens vibrations quickly`) sang khả năng trình diễn âm nhạc tất yếu!',
            [
                ('Contradiction', 'Mỗi chiếc chuông đã tạo được tới 2 cao độ khác nhau, không thể chỉ chơi 1 nốt đơn điệu.'),
                ('Reversed Logic', 'Bài nói chính chuông TRÒN (circular) mới ngân lâu và gây chói lẫn nhau!'),
                ('Đáp án đúng', 'Suy diễn 1mm trực tiếp từ 2 nốt/chuông và khả năng tắt ngân nhanh giúp chơi giai điệu nhanh rõ nét.'),
                ('Out of Scope / Implausible', 'Không thể bẻ cong tường đồng đúc bằng tay khi đang biểu diễn.'),
            ]
        ),

        # --- Q16-Q19: Boundaries (Easy / Medium) ---
        q_item(
            'm1_m2l_q16', 16, 'Standard English Conventions', 'Boundaries', 'Easy',
            '<p>When constructing traditional adobe homes in New Mexico, builders mix sun-dried clay with chopped ______ the straw fibers bind the dried mud together and prevent deep cracking as bricks cure in the desert heat.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['straw,', 'straw', 'straw, because', 'straw;'],
            'D',
            'Vế 1 là IC hoàn chỉnh ("When constructing..., builders mix sun-dried clay with chopped straw"). Vế 2 cũng là IC hoàn chỉnh ("the straw fibers bind..."). Nối 2 IC → chọn dấu chấm phẩy (;) = D!',
            'Nhận diện hai IC hoàn chỉnh hai bên chỗ trống → chọn `;` (loại Comma Splice A và Run-on B).',
            [
                ('Comma Splice', 'Nối hai IC chỉ bằng 1 dấu phẩy là Comma Splice.'),
                ('Run-On Sentence', 'Thiếu dấu câu ngăn cách hai mệnh đề độc lập.'),
                ('Unnecessary Comma Before Because', 'Đặt dấu phẩy trước mệnh đề "because" thiết yếu ở đây sai chuẩn SAT.'),
                ('Đáp án đúng', 'Dấu chấm phẩy (;) ngăn cách hợp lệ hai mệnh đề độc lập.'),
            ]
        ),
        q_item(
            'm1_m2l_q17', 17, 'Standard English Conventions', 'Boundaries', 'Easy',
            '<p>In 1969, architect ______ won the municipal competition to design Vancouver’s iconic sunken public library plaza.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['Arthur Erickson', ', Arthur Erickson,', 'Arthur Erickson,', ', Arthur Erickson'],
            'A',
            'Cấu trúc [Nghề nghiệp không có mạo từ a/the] + Tên riêng (`architect Arthur Erickson`) → Essential (0 dấu phẩy), nối thẳng sang động từ chính "won" → Chọn A!',
            'Title không mạo từ + Name + Verb → 0 dấu phẩy!',
            [
                ('Đáp án đúng', 'Không dấu phẩy — giữ liền mạch chủ ngữ "architect Arthur Erickson" với động từ "won".'),
                ('Non-Essential Trap', 'Chỉ dùng cặp phẩy khi có mạo từ xác định 1 người duy nhất trước chức danh.'),
                ('No-Comma Zone (S, V)', 'Dấu phẩy đơn ngăn Chủ ngữ khỏi Động từ chính "won".'),
                ('Unpaired Comma', 'Dấu phẩy lẻ giữa "architect" và tên riêng.'),
            ]
        ),
        q_item(
            'm1_m2l_q18', 18, 'Standard English Conventions', 'Boundaries', 'Medium',
            '<p>The botanical conservatory displays three rare highland orchids from the ______ <i>Masdevallia veitchiana</i>, <i>Dracula vampira</i>, and <i>Odontoglossum crispum</i>.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['Andes;', 'Andes:', 'Andes', 'Andes, such as:'],
            'B',
            'Vế trước là 1 IC hoàn chỉnh ("The botanical conservatory displays three rare highland orchids from the Andes"). Vế sau liệt kê tên 3 loài lan đó → Dùng dấu hai chấm (:) mở danh sách = B!',
            'IC hoàn chỉnh + danh sách liệt kê cụ thể → Dấu hai chấm (:); CẤM dùng "such as:"!',
            [
                ('Semicolon Before List', 'Sau dấu chấm phẩy phải là IC, không phải danh sách cụm danh từ.'),
                ('Đáp án đúng', 'IC hoàn chỉnh + dấu hai chấm (:) giới thiệu danh sách 3 loài lan hiếm.'),
                ('Missing Punctuation', 'Thiếu dấu câu dẫn nhập danh sách.'),
                ('Colon After Preposition Trap', 'Cấm đặt dấu hai chấm sau "such as".'),
            ]
        ),
        q_item(
            'm1_m2l_q19', 19, 'Standard English Conventions', 'Boundaries', 'Medium',
            '<p>Because wooden violins respond sensitively to sudden drops in winter ______ museum conservators house historic Italian instruments inside glass cases regulated at precisely fifty percent relative humidity.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['humidity;', 'humidity.', 'humidity,', 'humidity:'],
            'C',
            'Đầu câu mở bằng "Because..." → toàn bộ vế trái là Dependent Clause (DC)! Phía sau là Independent Clause (IC) → Công thức `DC , IC` → Chọn C! (Mẹo tương đương: A `;` và B `.` đều tách 2 IC → gạch ngay A, B, D!).',
            'Thấy "Because..." ở đầu câu → vế trái là DC → chỉ chọn dấu phẩy đơn (,).',
            [
                ('Semicolon After DC', 'Không dùng chấm phẩy sau mệnh đề phụ "Because...".'),
                ('Period After DC', 'Dấu chấm cắt mệnh đề "Because..." thành Fragment.'),
                ('Đáp án đúng', 'Dấu phẩy đơn chuẩn xác nối Dependent Clause với Independent Clause.'),
                ('Colon After DC', 'Trước dấu hai chấm phải là IC hoàn chỉnh.'),
            ]
        ),

        # --- Q20-Q22: Form, Structure, and Sense (Easy / Medium) ---
        q_item(
            'm1_m2l_q20', 20, 'Standard English Conventions', 'Form, Structure, and Sense', 'Easy',
            '<p>A collection of bronze coins minted during the reign of Emperor Augustus ______ recently donated to the university’s classical archaeology museum.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['were', 'have been', 'are', 'was'],
            'D',
            'Gạch bỏ cụm giới từ chen giữa: "A <b>collection</b> <s>[of bronze coins minted during the reign of Emperor Augustus]</s>". Chủ ngữ thật là "A collection" (SỐ ÍT) + ngữ cảnh quá khứ ("recently donated") → Chọn "was" (D)! Mẹo 3–1: A, B, C đều số nhiều, duy nhất D số ít!',
            'Mẹo 3–1: thấy 3 đáp án số nhiều (were, have been, are) và 1 số ít (was) → kiểm tra chủ ngữ gốc "A collection" → chốt D trong 5 giây!',
            [
                ('Subject-Verb Mismatch', 'were là số nhiều — bị lừa bởi "bronze coins".'),
                ('Subject-Verb Mismatch', 'have been là số nhiều.'),
                ('Subject-Verb Mismatch', 'are là số nhiều.'),
                ('Đáp án đúng', 'was (số ít, quá khứ đơn) khớp chuẩn với chủ ngữ "A collection".'),
            ]
        ),
        q_item(
            'm1_m2l_q21', 21, 'Standard English Conventions', 'Form, Structure, and Sense', 'Medium',
            '<p>Every spring, the coastal harbor authority inspects ______ concrete seawalls for tiny fractures caused by winter wave impacts.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['its', 'it’s', 'their', 'its’'],
            'A',
            'Danh từ tiền lệ là "the coastal harbor authority" (1 cơ quan/tổ chức → SỐ ÍT trên chuẩn SAT Mỹ) và cần tính từ sở hữu trước "concrete seawalls" → Chọn "its" (A)!',
            'Tổ chức/cơ quan (authority, agency, committee) trên SAT Mỹ luôn là SỐ ÍT → dùng "its" không dấu nháy.',
            [
                ('Đáp án đúng', 'its là tính từ sở hữu số ít khớp chuẩn với "the coastal harbor authority".'),
                ('Contraction Trap', 'it’s = it is — không thể đứng trước "concrete seawalls".'),
                ('Collective Noun Trap', 'their là số nhiều — sai với danh từ tổ chức số ít trên SAT.'),
                ('Non-Existent Word', 'its’ không tồn tại trong tiếng Anh.'),
            ]
        ),
        q_item(
            'm1_m2l_q22', 22, 'Standard English Conventions', 'Form, Structure, and Sense', 'Medium',
            '<p>To prepare for the marathon recital, pianist David Cho practiced scales for two hours every morning, memorized every concerto movement by heart, and ______</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            [
                'recording his practice sessions to evaluate tonal balance.',
                'recorded his practice sessions to evaluate tonal balance.',
                'his practice sessions were recorded to evaluate tonal balance.',
                'to record his practice sessions to evaluate tonal balance.'
            ],
            'B',
            'Cấu trúc Song song (Parallelism): chuỗi 3 động từ quá khứ chủ động cùng chủ ngữ David Cho: (1) <b>practiced</b>..., (2) <b>memorized</b>..., and (3) <b>recorded</b>... → Chọn B!',
            'Khớp đúng dạng động từ quá khứ đơn chủ động của 2 mục đầu tiên ("practiced", "memorized") → "recorded"!',
            [
                ('Broken Parallelism', 'recording (V-ing) không song song với hai động từ quá khứ "practiced" và "memorized".'),
                ('Đáp án đúng', 'recorded tạo chuỗi 3 động từ quá khứ chủ động song song hoàn hảo.'),
                ('Broken Parallelism', 'Chuyển đột ngột sang mệnh đề bị động phá vỡ cấu trúc song song.'),
                ('Broken Parallelism', 'Động từ nguyên mẫu "to record" lệch dạng với chuỗi quá khứ đơn.'),
            ]
        ),

        # --- Q23-Q25: Transitions (Easy / Medium) ---
        q_item(
            'm1_m2l_q23', 23, 'Expression of Ideas', 'Transitions', 'Easy',
            '<p>Traditional lighthouse lenses made from thick flat glass wasted nearly eighty percent of their lamp light by scattering it in every direction. ______, French physicist Augustin-Jean Fresnel designed a stepped concentric glass lens in 1822 that focused almost all the beam into a tight horizontal shaft visible thirty kilometers out at sea.</p>',
            'Which choice completes the text with the most logical transition?',
            ['Similarly', 'For example', 'In response', 'Previously'],
            'C',
            'Câu 1 nêu VẤN ĐỀ kỹ thuật (thấu kính phẳng cũ lãng phí 80% ánh sáng). Câu 2 nêu GIẢI PHÁP ra đời để khắc phục vấn đề đó (Fresnel chế tạo thấu kính bậc thang hội tụ tia sáng) → Vấn đề → Giải pháp = "In response" (C)!',
            'Nhận diện mạch `Problem (wasted 80% light)` → `Engineering Solution (Fresnel designed...)` → "In response"!',
            [
                ('Opposite Relationship', 'Similarly sai vì thiết kế của Fresnel khắc phục nhược điểm cũ chứ không giống cũ.'),
                ('Wrong Relationship (Example)', 'Thấu kính Fresnel không phải ví dụ về thấu kính phẳng lãng phí ánh sáng.'),
                ('Đáp án đúng', 'In response nối mượt vấn đề lãng phí ánh sáng với giải pháp cải tiến của Fresnel.'),
                ('Wrong Relationship (Time)', 'Thiết kế năm 1822 ra đời SAU các thấu kính phẳng truyền thống, không phải "Previously".'),
            ]
        ),
        q_item(
            'm1_m2l_q24', 24, 'Expression of Ideas', 'Transitions', 'Medium',
            '<p>Public ferries operating across Sydney Harbour transport tens of thousands of commuters each weekday without adding congestion to downtown bridges. ______, ferry terminals connect directly to neighborhood bus routes, allowing passengers to complete cross-city journeys smoothly on a single transit card.</p>',
            'Which choice completes the text with the most logical transition?',
            ['However', 'Instead', 'Consequently', 'In addition'],
            'D',
            'Câu 1 nêu ƯU ĐIỂM 1 (chở hàng vạn người không gây kẹt cầu). Câu 2 bổ sung ƯU ĐIỂM 2 độc lập cùng chiều (kết nối trực tiếp tuyến xe buýt dùng chung 1 thẻ) → Bổ sung thêm ý cùng chiều = "In addition" (D)!',
            'Ưu điểm 1 + Ưu điểm 2 độc lập → "In addition / Moreover / Furthermore".',
            [
                ('False Contrast', 'However sai vì hai câu đều ca ngợi ưu điểm hệ thống phà.'),
                ('Substitution Trap', 'Không có ý phủ định nào ở câu 1 để thay thế bằng "Instead".'),
                ('False Causation', 'Việc không gây kẹt cầu không tự sinh ra việc bến phà nối với xe buýt cùng 1 thẻ.'),
                ('Đáp án đúng', 'In addition bổ sung chính xác tiện ích kết nối thứ hai của hệ thống phà Sydney.'),
            ]
        ),
        q_item(
            'm1_m2l_q25', 25, 'Expression of Ideas', 'Transitions', 'Medium',
            '<p>Astronomers initially expected Jupiter’s innermost large moon, Io, to be a cold, geologically dead rock like Earth’s Moon. ______, close-up photographs sent back by Voyager 1 revealed towering sulfur plumes erupting from hundreds of active volcanoes across Io’s surface.</p>',
            'Which choice completes the text with the most logical transition?',
            ['However', 'Therefore', 'Furthermore', 'Specifically'],
            'A',
            'Câu 1: Kỳ vọng ban đầu (lạnh lẽo, chết về địa chất). Câu 2: Thực tế trái ngược 180 độ (hàng trăm núi lửa đang phun trào lưu huỳnh) → Quan hệ Đối lập → "However" (A)!',
            'Kỳ vọng sai ("initially expected cold, dead") ↔ Thực tế đảo ngược ("hundreds of active volcanoes") → "However / Nevertheless".',
            [
                ('Đáp án đúng', 'However đánh dấu chính xác sự đối lập hoàn toàn giữa dự đoán ban đầu và thực tế núi lửa hoạt động dữ dội trên Io.'),
                ('Wrong Relationship (Cause-Effect)', 'Therefore chỉ nhân quả — sai hoàn toàn.'),
                ('Wrong Relationship (Addition)', 'Furthermore dùng cho hai ý cùng chiều.'),
                ('Wrong Relationship (Example)', 'Núi lửa phun trào không phải ví dụ minh họa cho một thiên thể chết lạnh.'),
            ]
        ),

        # --- Q26-Q27: Rhetorical Synthesis (Easy / Medium) ---
        q_item(
            'm1_m2l_q26', 26, 'Expression of Ideas', 'Rhetorical Synthesis', 'Easy',
            '''<p>While researching a topic, a student has taken the following notes:</p>
            <ul>
              <li>The Panama Canal connects the Atlantic Ocean and the Pacific Ocean across the Isthmus of Panama.</li>
              <li>Opened in 1914, the canal is roughly 82 kilometers long.</li>
              <li>Rather than cutting at sea level, engineers built a system of giant water-filled locks that lift ships 26 meters above sea level to cross Gatun Lake.</li>
              <li>Using the canal saves ships traveling between New York and San Francisco roughly 13,000 kilometers compared with sailing around Cape Horn.</li>
            </ul>''',
            'The student wants to explain how the Panama Canal moves ships across Gatun Lake above sea level. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
            [
                'Opened in 1914, the 82-kilometer Panama Canal connects the Atlantic Ocean and the Pacific Ocean across the Isthmus of Panama.',
                'Instead of running at sea level, the Panama Canal uses a system of giant water-filled locks that raise ships 26 meters above sea level to cross Gatun Lake.',
                'Ships sailing between New York and San Francisco save roughly 13,000 kilometers by passing through the Panama Canal instead of rounding Cape Horn.',
                'The Panama Canal is an 82-kilometer waterway that dramatically shortens commercial shipping routes between the Atlantic and Pacific Oceans.'
            ],
            'B',
            'Goal-First SOP: Giải thích CÁCH kênh đào Panama đưa tàu vượt qua Hồ Gatun cao hơn mực nước biển ("explain HOW... moves ships across Gatun Lake above sea level"). Chỉ có B giải thích chính xác cơ chế hệ thống âu tàu chứa nước khổng lồ nâng tàu lên độ cao 26m!',
            'Khớp trực tiếp từ khóa Goal ("how... across Gatun Lake above sea level") → chỉ B nhắc hệ thống âu tàu (locks) nâng 26m qua Gatun Lake!',
            [
                ('Wrong Synthesis Goal', 'Chỉ nêu năm mở cửa và chiều dài kênh, không giải thích cách nâng tàu qua Hồ Gatun.'),
                ('Đáp án đúng', 'Giải thích chính xác cơ chế hệ thống âu tàu khổng lồ nâng tàu lên 26 mét để đi qua Hồ Gatun.'),
                ('Wrong Synthesis Goal', 'Chỉ nói lợi ích rút ngắn 13.000 km hành trình.'),
                ('Wrong Synthesis Goal', 'Chỉ tóm tắt chung vai trò rút ngắn tuyến vận tải.'),
            ]
        ),
        q_item(
            'm1_m2l_q27', 27, 'Expression of Ideas', 'Rhetorical Synthesis', 'Medium',
            '''<p>While researching a topic, a student has taken the following notes:</p>
            <ul>
              <li>The Sydney Opera House in Australia was designed by Danish architect Jørn Utzon and opened in 1973.</li>
              <li>Its roof consists of interlocking white precast concrete shells covered with more than one million Swedish ceramic tiles.</li>
              <li>The Guggenheim Museum Bilbao in Spain was designed by Canadian-American architect Frank Gehry and opened in 1997.</li>
              <li>Its sweeping exterior curves are clad in roughly 33,000 paper-thin titanium sheets.</li>
            </ul>''',
            'The student wants to emphasize a difference in the exterior cladding materials used on the two famous cultural buildings. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
            [
                'Both the Sydney Opera House (1973) and the Guggenheim Museum Bilbao (1997) are internationally celebrated cultural landmarks.',
                'Designed by Danish architect Jørn Utzon, the Sydney Opera House opened in Australia in 1973, twenty-four years before Frank Gehry’s Guggenheim Museum Bilbao opened in Spain.',
                'Whereas the Sydney Opera House’s concrete roof shells are clad in over one million ceramic tiles, the Guggenheim Museum Bilbao’s curved exterior is covered in roughly 33,000 thin titanium sheets.',
                'Canadian-American architect Frank Gehry used roughly 33,000 paper-thin titanium sheets to cover the sweeping exterior of the Guggenheim Museum Bilbao.'
            ],
            'C',
            'Goal-First SOP: Nhấn mạnh ĐIỂM KHÁC NHAU về VẬT LIỆU ỐP BỀ MẶT NGOÀI ("exterior cladding materials") của CẢ HAI công trình. A nói điểm giống; B so sánh năm khánh thành; D chỉ nhắc 1 công trình. Duy nhất C đối chiếu trực tiếp >1 triệu viên gạch men Thụy Điển (Sydney Opera House) với ~33.000 tấm titan mỏng (Guggenheim Bilbao)!',
            'Đủ 3 tiêu chí Goal: `difference` + `both buildings` + `exterior cladding materials` (ceramic tiles vs. titanium sheets)!',
            [
                ('Wrong Synthesis Goal', 'Nhấn mạnh điểm tương đồng thay vì khác biệt vật liệu.'),
                ('Wrong Criterion', 'So sánh kiến trúc sư và năm khánh thành chứ không phải vật liệu ốp ngoài.'),
                ('Đáp án đúng', 'Đối chiếu trọn vẹn vật liệu ốp bên ngoài của cả hai công trình (gạch men vs. tấm titan).'),
                ('Single Subject Trap', 'Chỉ mô tả bảo tàng Bilbao mà không đối chiếu với Nhà hát Sydney.'),
            ]
        ),
    ]
