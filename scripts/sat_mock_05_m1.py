# -*- coding: utf-8 -*-
"""
Full-Length Adaptive Mock Test #5 — Module 1 (27 Qs, Easy/Medium/Hard Routing Mix, 32 min)
Exact College Board Digital SAT R&W Blueprint:
Q1-5: Words in Context | Q6-7: Text Structure/Purpose | Q8: Cross-Text
Q9-10: Central Ideas/Details | Q11-12: Evidence (Textual) | Q13-14: Evidence (Quantitative)
Q15: Inferences | Q16-19: Boundaries | Q20-22: Form/Structure/Sense
Q23-25: Transitions | Q26-27: Rhetorical Synthesis
"""

from sat_drills_1_1_and_2_1 import q_item
from sat_drills_5_4_to_5_5 import svg_bar_chart, html_table

def get_m1_questions():
    return [
        # --- Q1-Q5: Craft and Structure — Words in Context ---
        q_item(
            'm5_m1_q1', 1, 'Craft and Structure', 'Words in Context', 'Easy',
            '<p>Along mid-ocean volcanic ridges two miles beneath the Pacific surface, hydrothermal vents expel superheated water saturated with dissolved iron and copper sulfides; as soon as these mineral-rich plumes collide with near-freezing abyssal seawater, the minerals rapidly ______ into jagged, chimney-like towers.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            ['dissolve', 'solidify', 'evaporate', 'disperse'],
            'B',
            'Cause-Effect + Restatement Clue: nước siêu nóng chứa khoáng chất hòa tan ("dissolved") va chạm với nước biển đáy gần đóng băng rồi biến thành "jagged, chimney-like towers" (những tháp ống khói đá cứng lởm chởm) → ĐÔNG CỨNG / KẾT RẮN LẠI → "solidify" (B).',
            'Đối chiếu trạng thái đầu ("dissolved") và kết quả cuối ("jagged, chimney-like towers") → chọn động từ chuyển từ lỏng/hòa tan sang rắn ("solidify").',
            [
                ('Opposite Meaning', 'dissolve = hòa tan trở lại — mâu thuẫn với việc hình thành các tháp ống khói khoáng cứng.'),
                ('Đáp án đúng', 'solidify = hóa rắn, kết khối cứng — khớp hoàn toàn với quá trình kết tủa tạo thành tháp khoáng dưới đáy biển.'),
                ('Wrong Context', 'evaporate = bốc hơi thành khí — không tạo ra tháp khoáng rắn dưới áp suất đáy đại dương.'),
                ('Opposite Meaning', 'disperse = phân tán tản mác — trái ngược với việc tụ lại thành cột tháp cao.'),
            ]
        ),
        q_item(
            'm5_m1_q2', 2, 'Craft and Structure', 'Words in Context', 'Medium',
            '<p>When Renaissance Venetian printer Aldus Manutius launched his pocket-sized <i>octavo</i> editions of Greek and Latin classics in 1501, traveling scholars enthusiastically traded away the ______ medieval folio volumes that had previously required sturdy wooden lecterns to support their weight.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            ['portable', 'fragile', 'ornamental', 'cumbersome'],
            'D',
            'Contrast + Restatement Clue: đối lập với sách bỏ túi nhỏ gọn ("pocket-sized octavo") + vế giải thích ngay sau ("required sturdy wooden lecterns to support their weight" = cần giá đỡ gỗ chắc chắn mới đỡ nổi sức nặng) → CỒNG KỀNH, NẶNG NỀ → "cumbersome" (D).',
            'Cụm "required sturdy wooden lecterns to support their weight" là định nghĩa trực tiếp của "cumbersome" (nặng nề cồng kềnh).',
            [
                ('Opposite Meaning', 'portable = dễ mang theo — đây là đặc tính của sách bỏ túi octavo mới, không phải sách folio cũ.'),
                ('Wrong Meaning', 'fragile = dễ vỡ mong manh — câu nhấn mạnh sức nặng phải có giá gỗ đỡ chứ không phải tính dễ rách vỡ.'),
                ('Off-Point', 'ornamental = có tính trang trí — không đối lập trực tiếp với kích thước bỏ túi và trọng lượng nặng.'),
                ('Đáp án đúng', 'cumbersome = nặng nề, cồng kềnh khó mang vác — đối lập hoàn hảo với sách bỏ túi octavo.'),
            ]
        ),
        q_item(
            'm5_m1_q3', 3, 'Craft and Structure', 'Words in Context', 'Medium',
            '<p>In a three-year municipal trial of reflective cool-pavement coatings across sunlit Phoenix neighborhoods, freshly applied pale sealants initially lowered midday road-surface temperatures by nearly 6°C; however, accumulated tire rubber and desert dust gradually ______ that cooling advantage over the next eighteen months.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            ['eroded', 'amplified', 'preserved', 'initiated'],
            'A',
            'Contrast Clue: "initially lowered... by nearly 6°C; however, accumulated tire rubber and desert dust gradually ______ that cooling advantage" → lớp bụi sa mạc và cao su lốp xe tối màu bám dần làm XÓI MÒN / SUY GIẢM lợi thế làm mát ban đầu → "eroded" (A).',
            'Từ chuyển hướng "however" đảo ngược hiệu quả làm mát ban đầu khi bụi và vết lốp bám phủ lên mặt đường phản quang → chọn "eroded" (làm suy giảm dần).',
            [
                ('Đáp án đúng', 'eroded (nghĩa bóng học thuật: bào mòn, làm suy giảm dần) — khớp chuẩn với "gradually" và tác động của bụi/lốp xe.'),
                ('Opposite Meaning', 'amplified = khuếch đại tăng mạnh — trái ngược hoàn toàn với từ chuyển hướng "however".'),
                ('Opposite Meaning', 'preserved = giữ nguyên bảo toàn — mâu thuẫn với việc bụi bẩn làm tối bề mặt phản quang.'),
                ('Wrong Logic', 'initiated = khởi xướng bắt đầu — lợi thế làm mát đã xuất hiện ngay từ đầu khi mới quét sơn.'),
            ]
        ),
        q_item(
            'm5_m1_q4', 4, 'Craft and Structure', 'Words in Context', 'Hard',
            '<p>Rather than treating rising stars, bent ocean swells, and homing seabirds as disconnected signs, master Micronesian wayfinders synthesize all three environmental cues into a single ______ navigational picture that guides double-hulled canoes safely across hundreds of miles of open Pacific water.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            ['fragmented', 'arbitrary', 'cohesive', 'peripheral'],
            'C',
            'Contrast + Mirror Clue: đối lập với "disconnected signs" (tín hiệu rời rạc) + động từ "synthesize all three... into a single ______ picture" (tổng hợp cả ba thành một bức tranh duy nhất gắn kết chặt chẽ) → MẠCH LẠC, THỐNG NHẤT → "cohesive" (C).',
            'Cặp từ đối lập rõ nét: "disconnected signs" ↔ "synthesize... into a single cohesive picture"!',
            [
                ('Opposite Meaning', 'fragmented = rời rạc vụn vỡ — đồng nghĩa với "disconnected", sai sau "Rather than".'),
                ('Wrong Tone', 'arbitrary = tùy tiện vô căn cứ — trái ngược với khả năng dẫn đường chính xác hàng trăm dặm biển.'),
                ('Đáp án đúng', 'cohesive = gắn kết chặt chẽ thành một chỉnh thể thống nhất — đối lập tuyệt đối với "disconnected".'),
                ('Wrong Meaning', 'peripheral = bên lề thứ yếu — không hợp với bức tranh định hướng cốt lõi.'),
            ]
        ),
        q_item(
            'm5_m1_q5', 5, 'Craft and Structure', 'Words in Context', 'Hard',
            '<p>Because freshly fallen Antarctic snow requires centuries of burial before compacting into airtight glacial ice, ancient air bubbles finally sealed inside an ice core are significantly younger than the surrounding ice crystals; paleoclimatologists must carefully calculate this chronological ______ before matching past greenhouse-gas spikes to regional temperature shifts.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            ['discrepancy', 'concordance', 'uniformity', 'stagnation'],
            'A',
            'Cause-Effect Clue: bọt khí bị niêm phong trẻ hơn nhiều ("significantly younger") so với tinh thể băng xung quanh → tồn tại một SỰ CHÊNH LỆCH / SAI KHÁC về niên đại phải tính toán kỹ trước khi khớp mốc khí nhà kính với nhiệt độ → "discrepancy" (A).',
            'Bọt khí "younger than" tinh thể băng cùng độ sâu = hai mốc thời gian lệch nhau → chọn "discrepancy" (sự chênh lệch/sai khác).',
            [
                ('Đáp án đúng', 'discrepancy = sự chênh lệch/sai khác (ở đây là độ lệch tuổi giữa bọt khí và lớp băng bao quanh).'),
                ('Opposite Meaning', 'concordance = sự trùng khớp hài hòa — trái ngược với việc bọt khí trẻ hơn tinh thể băng.'),
                ('Opposite Meaning', 'uniformity = tính đồng nhất không đổi — mâu thuẫn với sự chênh lệch tuổi tác.'),
                ('Wrong Context', 'stagnation = sự trì trệ đứng yên — không dùng để mô tả độ lệch niên đại giữa hai đại lượng.'),
            ]
        ),

        # --- Q6-Q7: Craft and Structure — Text Structure and Purpose ---
        q_item(
            'm5_m1_q6', 6, 'Craft and Structure', 'Text Structure and Purpose', 'Medium',
            '<p>Although tropical coral reefs appear serene to swimmers glancing down from the surface, underwater hydrophones reveal that thriving reefs are among the loudest biological environments on Earth. <u>Billions of snapping shrimp and chorusing damselfish generate a continuous crackling soundscape that travels several kilometers into open ocean, guiding microscopic coral and fish larvae back toward healthy reef habitats where they can settle.</u> When prolonged marine heat waves bleach a reef, however, this acoustic chorus falls sharply silent, making natural repopulation far slower.</p>',
            'Which choice best describes the function of the underlined sentence in the text as a whole?',
            [
                'It questions whether snapping shrimp actually produce louder sounds than tropical damselfish.',
                'It details the thermal stress mechanism by which marine heat waves bleach healthy coral reefs.',
                'It identifies the biological sources of reef noise and explains the ecological role that soundscape plays in guiding drifting larvae.',
                'It argues that underwater hydrophones interfere with the navigation of microscopic coral larvae.'
            ],
            'C',
            'Câu 1 khẳng định rạn san hô khỏe là môi trường sinh học ồn ào bậc nhất. Câu gạch chân chỉ rõ NGUỒN PHÁT ÂM SINH HỌC (tôm gõ mõ + cá thia hợp xướng) VÀ VAI TRÒ SINH THÁI của âm thanh đó (truyền đi nhiều km giúp ấu trùng san hô và cá định hướng tìm về rạn khỏe để bám cư trú) → Chọn C!',
            'Phân tích hai nửa của câu gạch chân: chủ ngữ nêu nguồn âm (snapping shrimp & damselfish) + cụm phân từ "guiding... larvae" nêu chức năng sinh thái.',
            [
                ('Out of Scope', 'Bài không hề so sánh độ lớn âm thanh giữa tôm gõ mõ và cá thia.'),
                ('Wrong Sentence Reference', 'Hiện tượng tẩy trắng do sóng nhiệt chỉ xuất hiện ở câu cuối cùng, không nằm trong câu gạch chân.'),
                ('Đáp án đúng', 'Tóm gọn chính xác cả hai thành phần của câu gạch chân: nguồn tạo âm sinh học và vai trò dẫn đường cho ấu trùng.'),
                ('Contradiction / Out of Scope', 'Hydrophone chỉ là thiết bị ghi âm giúp con người phát hiện tiếng ồn rạn san hô, không gây nhiễu ấu trùng.'),
            ]
        ),
        q_item(
            'm5_m1_q7', 7, 'Craft and Structure', 'Text Structure and Purpose', 'Medium',
            '<p><i>The following text is adapted from an 1852 New England woodland essay. The narrator walks through a birch hillside after the first hard frost of November.</i><br/>People speak of November as a season of subtraction, mourning the maple crimson and birch gold that October surrendered to the wind. Yet walking the bare ridge this morning, I felt less as though the woods had been emptied than as though a curtain had been lifted. Every dry-laid granite wall, every mossy boulder, and every woven thrush nest tucked in the alder forks stood revealed in crisp slate-blue light, showing me the true architecture that summer’s green abundance had kept modestly hidden.</p>',
            'Which choice best states the main purpose of the text?',
            [
                'To criticize New England farmers for building granite walls across forested birch hillsides.',
                'To challenge the view that late autumn is merely a season of loss by portraying bare November woods as a moment of vivid visual clarity.',
                'To compare the nesting habits of woodland thrushes during summer and early winter.',
                'To urge readers to preserve maple and birch foliage before November frosts arrive.'
            ],
            'B',
            'Câu 1 đưa quan niệm phổ biến ("season of subtraction, mourning..."). Từ "Yet" ở câu 2 lật ngược cảm nhận: tác giả không thấy rừng trống rỗng mà như "một bức màn vừa được vén lên" ("a curtain had been lifted"), làm lộ rõ bức tường đá, tảng rêu và tổ chim vốn bị tán lá hè che khuất → Chọn B!',
            'Bám sát bước ngoặt "Yet... less as though the woods had been emptied than as though a curtain had been lifted" để chốt đúng Main Purpose!',
            [
                ('Out of Scope / Wrong Tone', 'Tác giả ngắm nhìn bức tường đá như nét kiến trúc cảnh quan thú vị, không hề chỉ trích nông dân.'),
                ('Đáp án đúng', 'Khớp hoàn toàn cấu trúc lật ngược: phản bác định kiến tháng 11 chỉ là sự mất mát, thay vào đó tôn vinh độ sắc nét khi tán lá rụng.'),
                ('Narrow Detail', 'Tổ chim hoét chỉ là một trong ba chi tiết minh họa cho sự lộ diện rõ ràng của cảnh rừng.'),
                ('Out of Scope', 'Không có lời kêu gọi bảo tồn lá cây.'),
            ]
        ),

        # --- Q8: Craft and Structure — Cross-Text Connections ---
        q_item(
            'm5_m1_q8', 8, 'Craft and Structure', 'Cross-Text Connections', 'Hard',
            '<p><b>Text 1</b><br/>Urban climate specialist Dr. Nora Lindqvist recommends coating sun-exposed downtown sidewalks and open public plazas with high-albedo white sealants. Because bright pavements reflect far more incoming solar radiation than dark asphalt does, Lindqvist argues that citywide reflective paving uniformly improves daytime thermal comfort for pedestrians during summer heat waves.</p><p><b>Text 2</b><br/>Deploying wearable heat sensors on volunteers walking across sun-drenched reflective plazas in Madrid and Phoenix, biometeorologist Dr. Mateo Vargas confirmed that pale coatings cooled road surfaces by up to 7°C. However, Vargas’s sensors also recorded that shortwave sunlight bouncing upward off the bright ground struck pedestrians from below, raising their overall perceived radiant heat load at noon compared with shaded streets or tree-lined dark asphalt.</p>',
            'Based on the texts, how would Dr. Mateo Vargas (Text 2) most likely respond to Dr. Nora Lindqvist’s argument (Text 1)?',
            [
                'By acknowledging that reflective coatings lower pavement surface temperatures, while arguing that reflected sunlight bouncing upward can worsen midday radiant heat stress on pedestrians in unshaded plazas.',
                'By asserting that high-albedo white sealants actually absorb more solar radiation than dark asphalt roads do.',
                'By agreeing that citywide reflective paving eliminates the need for shade trees along downtown pedestrian plazas.',
                'By claiming that wearable heat sensors are unreliable when measuring surface temperatures in Madrid and Phoenix.'
            ],
            'A',
            'Text 1 tuyên bố lớp phủ phản quang "uniformly improves daytime thermal comfort for pedestrians". Text 2 có 2 vế rõ ràng: (1) Thừa nhận mặt đường mát đi tới 7°C ("confirmed that pale coatings cooled road surfaces"); (2) Phản bác chữ "uniformly improves comfort" vì ánh nắng phản chiếu hắt ngược từ mặt đất lên người đi bộ làm tăng tổng tải nhiệt bức xạ lúc giữa trưa ở quảng trường không bóng cây → Chọn A!',
            'Mô hình phản biện "Yes-but" kinh điển: đồng ý hiệu quả làm mát mặt đường (surface) nhưng chỉ ra tác dụng phụ bức xạ hắt ngược lên người đi bộ (pedestrians)!',
            [
                ('Đáp án đúng', 'Phản ánh đủ cả vế công nhận (hạ nhiệt mặt đường) và vế phản biện (ánh nắng phản xạ hắt lên làm tăng áp lực nhiệt bức xạ cho người đi bộ).'),
                ('Contradiction', 'Vargas xác nhận lớp phủ sáng màu làm mát mặt đường tới 7°C — tức phản xạ tốt hơn nhựa đường tối, không phải hấp thụ nhiều hơn.'),
                ('Reversed Logic', 'Vargas so sánh bất lợi của quảng trường nắng gắt so với đường có cây xanh, không hề nói bỏ cây bóng mát.'),
                ('Out of Scope', 'Vargas sử dụng chính cảm biến đeo người làm bằng chứng, không chê chúng thiếu tin cậy.'),
            ]
        ),

        # --- Q9-Q10: Information and Ideas — Central Ideas and Details ---
        q_item(
            'm5_m1_q9', 9, 'Information and Ideas', 'Central Ideas and Details', 'Medium',
            '<p>Clustered around scalding Pacific hydrothermal vents, giant tube worms (<i>Riftia pachyptila</i>) grow more than two meters long despite lacking a mouth, stomach, or digestive tract. Instead, their bright-red plumes contain specialized hemoglobin molecules capable of binding both oxygen from seawater and toxic hydrogen sulfide from volcanic plumes—safely ferrying both compounds to billions of chemosynthetic bacteria packed inside an internal organ called the trophosome, which synthesize all the organic sugars the worm needs to live.</p>',
            'Which choice best states the main idea of the text?',
            [
                'Giant tube worms consume dissolved organic sugars directly from scalding Pacific seawater through their bright-red plumes.',
                'Hydrogen sulfide from hydrothermal vents destroys hemoglobin molecules inside deep-sea tube worms unless it is filtered out first.',
                'Chemosynthetic bacteria cannot survive inside the internal organs of deep-sea animals taller than two meters.',
                'Lacking a digestive system, giant tube worms sustain themselves by using specialized hemoglobin to deliver vent chemicals to symbiotic internal bacteria that produce their food.'
            ],
            'D',
            'Trục ý chính: Giun ống khổng lồ không có miệng/hệ tiêu hóa → dùng hemoglobin đặc biệt vận chuyển oxy và khí H₂S độc hại vào cơ quan trophosome nuôi vi khuẩn hóa tổng hợp cộng sinh → vi khuẩn tạo toàn bộ đường hữu cơ nuôi sống giun → Chọn D!',
            'Nối đủ chuỗi sinh học 3 bước: không hệ tiêu hóa → hemoglobin chở O₂ + H₂S → vi khuẩn cộng sinh tạo thức ăn.',
            [
                ('Fact Distortion', 'Chùm lông đỏ hấp thụ O₂ và H₂S để đưa cho vi khuẩn tự tổng hợp đường bên trong, chứ không trực tiếp hút sẵn đường hữu cơ từ nước biển.'),
                ('Contradiction', 'Hemoglobin đặc biệt gắn kết và vận chuyển AN TOÀN khí H₂S ("safely ferrying"), không bị phá hủy.'),
                ('Contradiction', 'Hàng tỷ vi khuẩn hóa tổng hợp đang sống khỏe ngay bên trong loài giun dài trên 2 mét này.'),
                ('Đáp án đúng', 'Tóm gọn đầy đủ cơ chế cộng sinh giúp giun ống sống không cần hệ tiêu hóa.'),
            ]
        ),
        q_item(
            'm5_m1_q10', 10, 'Information and Ideas', 'Central Ideas and Details', 'Hard',
            '<p><i>The following poem is adapted from an 1874 American lyric titled “The Mill-Stream at Dusk.”</i><br/>All afternoon the iron wheels<br/>Have churned the brown canal to foam,<br/>And rung their brassy warning peals<br/>Till weary weavers hurry home.<br/><br/>Now shuts the sluice; the clatter dies;<br/>The turbid raceway smooths its glass,<br/>And holds once more the copper skies<br/>And swallows dipping through the grass.</p>',
            'Which choice best states the main idea of the poem?',
            [
                'Textile weavers prefer working inside noisy brick mills rather than watching swallows along the riverbank.',
                'Once the factory’s water gates close at evening, the churned mill-stream settles back into calm clarity that reflects the natural sky.',
                'The iron waterwheels along the canal are too rusted to operate safely after twilight.',
                'Swallows gather near the canal only when the iron wheels stir up foam on the water.'
            ],
            'B',
            'Khổ 1: Suốt buổi chiều bánh xe sắt khuấy kênh thành bọt đục ngầu ồn ào khi nhà máy dệt hoạt động. Khổ 2 ("Now shuts the sluice; the clatter dies"): Khi cửa đập nhà máy đóng lại lúc hoàng hôn, tiếng ầm ĩ tắt lịm, dòng nước đục lắng phẳng như gương ("smooths its glass") phản chiếu lại bầu trời màu đồng và đàn chim én bay là mặt cỏ → Chọn B!',
            'So sánh trực tiếp Khổ 1 (nhà máy chạy → bọt đục & tiếng ồn) với Khổ 2 (đóng cửa cống lúc chạng vạng → nước lắng trong phản chiếu trời chiều)!',
            [
                ('Out of Scope', 'Thợ dệt mệt mỏi vội vã về nhà ("weary weavers hurry home"), không có chi tiết nào nói họ thích xưởng ồn hơn ngắm chim.'),
                ('Đáp án đúng', 'Gom trọn sự chuyển hóa giữa 2 khổ thơ: đóng cửa cống nhà máy → dòng nước lắng êm, phản chiếu bầu trời tự nhiên.'),
                ('Out of Scope', 'Không nhắc bánh xe sắt bị gỉ sét hay hư hỏng.'),
                ('Reversed Logic', 'Chim én xuất hiện ở Khổ 2 SAU KHI cửa cống đóng và mặt nước lắng êm, không phải khi bánh xe khuấy bọt.'),
            ]
        ),

        # --- Q11-Q12: Information and Ideas — Command of Evidence (Textual) ---
        q_item(
            'm5_m1_q11', 11, 'Information and Ideas', 'Command of Evidence (Textual)', 'Hard',
            '<p>Paleoclimatologists analyzing East Antarctic ice cores dating to the peak of the last ice age—roughly 21,000 years ago—discovered a sharp twentyfold surge in microscopic mineral dust embedded in the ice. Geochemist Dr. Henrik Solberg hypothesized that this ancient dust originated primarily from wind-swept glacial floodplains in southern South America carried across the Southern Ocean by intensified westerly winds, rather than eroding off nearby exposed coastal rock outcrops in Antarctica itself.</p>',
            'Which finding, if true, would most directly support Dr. Henrik Solberg’s hypothesis?',
            [
                'Modern satellite imagery shows that Antarctic winter sea ice expands across millions of square kilometers each July.',
                'East Antarctic ice cores dating to 21,000 years ago also contain trace amounts of volcanic sulfate from eruptions in Indonesia.',
                'Strontium and neodymium isotope signatures measured in the 21,000-year-old dust grains closely match sedimentary basins in Patagonia, South America, while differing sharply from the isotopic profile of exposed Antarctic bedrock.',
                'Coastal rock outcrops in East Antarctica contain significantly higher concentrations of quartz than glacial layers formed during warmer interglacial periods.'
            ],
            'C',
            'Khóa giả thuyết Solberg: Bụi khoáng 21.000 năm trước đến từ NAM MỸ (X1), KHÔNG phải từ đá ven bờ Nam Cực (NOT X2). Đáp án C đưa ra "dấu vân tay đồng vị" trực tiếp nhất: tỷ lệ đồng vị stronti và neodymi của hạt bụi khớp sát lưu vực trầm tích Patagonia (Nam Mỹ) đồng thời khác biệt rõ rệt với đá gốc Nam Cực → Xác thực trọn cả hai vế! Chọn C!',
            'Khi giả thuyết tranh luận về NGUỒN GỐC ĐỊA LÝ (South America vs. local Antarctica), bằng chứng mạnh nhất luôn là dấu vân tay đồng vị/hóa học khớp nguồn A và lệch hẳn nguồn B!',
            [
                ('Adjacent Topic Drift', 'Diện tích băng biển hiện đại không chứng minh nguồn gốc địa lý của hạt bụi 21.000 năm trước.'),
                ('Adjacent Topic Drift', 'Sunfat núi lửa từ Indonesia là dấu vết phun trào khác, không chứng minh nguồn bụi khoáng từ Nam Mỹ.'),
                ('Đáp án đúng', 'Khớp cả hai vế của giả thuyết: chữ ký đồng vị trùng lưu vực Patagonia (Nam Mỹ) và khác hẳn đá gốc Nam Cực.'),
                ('Weakens / Off-Point', 'Nói về hàm lượng thạch anh ở đá Nam Cực không chứng minh bụi trong lõi băng bay từ Nam Mỹ sang.'),
            ]
        ),
        q_item(
            'm5_m1_q12', 12, 'Information and Ideas', 'Command of Evidence (Textual)', 'Medium',
            '<p>In a critical introduction to the 1889 American realist novel <i>The Grain Ledger</i>, a literary scholar claims that Clara—a young bookkeeper at a rural Kansas rail depot—comes to see the railroad company’s public rhetoric of “shared frontier prosperity” as a hollow slogan disguising an arrangement that steadily enriches the company while trapping wheat farmers in debt.</p>',
            'Which quotation from Clara in <i>The Grain Ledger</i> most effectively illustrates the scholar’s claim?',
            [
                '“Every painted poster on the depot wall proclaims that iron rails make every homesteader a partner in progress, yet when I tally the autumn freight bills, it is always the company’s ledger that swells while the farmers mortgage next spring’s seed.”',
                '“Two locomotives arrived from Topeka before daybreak carrying pine lumber, kegs of iron nails, and crates of kerosene lanterns.”',
                '“Mr. Halloway insists that every column of wheat bushel weights be totaled twice in black ink before the evening express departs.”',
                '“When July droughts bake the prairie clay hard as brick, no farmer in the county sleeps soundly until rain clouds form west of the ridge.”'
            ],
            'A',
            'Checklist 2 vế từ Claim: [1] Khẩu hiệu công khai "shared frontier prosperity" chỉ là lời rỗng tuếch + [2] Thực tế làm giàu cho công ty đường sắt trong khi đẩy nông dân trồng lúa mì vào nợ nần. Duy nhất A đối chiếu trực diện cả 2 vế: áp phích hứa hẹn "partner in progress" ↔ sổ sách thực tế công ty phình to còn nông dân phải thế chấp hạt giống vụ sau! Chọn A!',
            'Khớp trực tiếp đối lập giữa "painted poster proclaims partner in progress" và "company’s ledger swells while farmers mortgage next spring’s seed"!',
            [
                ('Đáp án đúng', 'Minh họa xuất sắc sự tương phản giữa lời hứa thịnh vượng chung và thực tế công ty hưởng lợi còn nông dân mắc nợ.'),
                ('Irrelevant Detail', 'Chỉ liệt kê hàng hóa tàu chở đến ga.'),
                ('Irrelevant Detail', 'Chỉ nói quy trình kiểm sổ bằng mực đen.'),
                ('Off-Point', 'Chỉ mô tả nỗi lo hạn hán tháng Bảy, không liên quan đến khẩu hiệu đường sắt hay sổ sách nợ nần.'),
            ]
        ),

        # --- Q13-Q14: Information and Ideas — Command of Evidence (Quantitative) ---
        q_item(
            'm5_m1_q13', 13, 'Information and Ideas', 'Command of Evidence (Quantitative)', 'Medium',
            svg_bar_chart(
                'Mean Juvenile Damselfish Settling on Degraded Coral Patches (40 Days)',
                ['0', '5', '10', '15', '20', '25'],
                [('Silent Degraded', 6, '6 fish'), ('White Noise', 7, '7 fish'), ('Boat Engine', 4, '4 fish'), ('Healthy Reef Audio', 23, '23 fish')],
                25
            ) + '<p>Marine acoustic ecologists tested whether underwater loudspeakers playing recorded biological choruses from vibrant reefs could accelerate fish return to bleached coral patches. The researchers concluded that replaying healthy reef sounds attracts more than triple the number of juvenile damselfish compared with silent degraded patches, whereas non-biological noise fails to produce any comparable recruitment boost.</p>',
            'Which choice most effectively uses data from the graph to support the researchers’ conclusion?',
            [
                'Silent degraded coral patches attracted an average of 6 juvenile damselfish over 40 days, slightly more than the 4 fish attracted by boat engine recordings.',
                'Degraded patches playing healthy reef audio attracted an average of 23 juvenile damselfish—more than triple the 6 fish recorded on silent patches—whereas white noise (7 fish) and boat engine audio (4 fish) remained close to or below the silent baseline.',
                'Juvenile damselfish settled across all four experimental coral patch conditions over the 40-day monitoring period.',
                'Patches exposed to boat engine playback recorded the lowest settlement rate in the trial at 4 fish per patch.'
            ],
            'B',
            'Checklist 2 vế kết luận: [1] Healthy Reef Audio thu hút HƠN GẤP 3 LẦN Silent Degraded (23 vs. 6 → 6 × 3 = 18 < 23 ✓) + [2] Tiếng ồn phi sinh học (White Noise = 7, Boat Engine = 4) không tạo cú hích tương đương (sát hoặc thấp hơn mức nền 6 ✓). A, C, D đều đúng biểu đồ nhưng bỏ quên mốc quan trọng nhất (23 con của Healthy Reef Audio)! Chọn B!',
            'Xác minh phép nhân ngay trên biểu đồ: 23 > 3 × 6 (18) và đối chiếu trực tiếp với 7 (white noise) và 4 (boat engine)!',
            [
                ('Incomplete Data', 'Bỏ hoàn toàn số liệu 23 con của Healthy Reef Audio — đối tượng trung tâm của kết luận.'),
                ('Đáp án đúng', 'Khớp đầy đủ cả phép so sánh gấp hơn 3 lần (23 vs. 6) lẫn số liệu đối chứng của tiếng ồn phi sinh học (7 và 4).'),
                ('True Data / Wrong Claim', 'Chỉ nêu chung chung cả 4 nghiệm thức đều có cá đến, không chứng minh hiệu quả vượt trội của âm thanh rạn khỏe.'),
                ('Incomplete Data', 'Chỉ nhắc mức thấp nhất của Boat Engine, bỏ qua Healthy Reef Audio và Silent Degraded.'),
            ]
        ),
        q_item(
            'm5_m1_q14', 14, 'Information and Ideas', 'Command of Evidence (Quantitative)', 'Hard',
            html_table(
                'Table 1. First-Year Sales of Four Renaissance Venetian Print Editions (1501–1504)',
                ['Workshop', 'Book Format', 'Print Run (Copies)', 'Price (Soldi)', 'Copies Sold in Year 1'],
                [
                    ['Aldine Press', 'Pocket Octavo', '1,000', '24', '940'],
                    ['Torresani Shop', 'Medium Quarto', '800', '36', '710'],
                    ['Scotto Press', 'Large Folio', '1,200', '68', '420'],
                    ['Locatelli Shop', 'Medium Quarto', '600', '32', '530'],
                ]
            ) + '<p>A book historian claims that Renaissance Venetian workshops that printed larger total initial runs consistently achieved higher total first-year unit sales than workshops that printed smaller runs.</p>',
            'Which choice best describes data from the table that directly weaken the historian’s claim?',
            [
                'The Aldine Press priced its pocket octavo edition at 24 soldi and sold 940 copies during its first year.',
                'The Torresani Shop printed 800 copies of its medium quarto edition and sold more copies in Year 1 (710) than the Locatelli Shop sold from its 600-copy run (530).',
                'The Locatelli Shop printed the smallest initial run in the table at 600 copies.',
                'Although the Scotto Press printed the largest initial run in the table (1,200 copies), it sold only 420 copies in Year 1—fewer than every workshop with a smaller print run, including the Locatelli Shop (530 copies from a 600-copy run).'
            ],
            'D',
            'Khóa Claim cần WEAKEN: Xưởng nào in số lượng bản đầu (Print Run) LỚN HƠN thì luôn bán được TỔNG SỐ BẢN NĂM ĐẦU (Copies Sold in Year 1) CAO HƠN! Soi phản ví dụ trong bảng: **Scotto Press** in lớn nhất bảng (**1.200 bản**), nhưng năm đầu chỉ bán **420 bản** — ÍT HƠN CẢ 3 xưởng in nhỏ hơn (Aldine 940, Torresani 710, kể cả Locatelli chỉ in 600 bản mà bán 530 bản)! Chọn D!',
            'Để bác bỏ tuyên bố đồng biến ("larger run → consistently higher sales"), tìm ngay hàng có cột Print Run CAO NHẤT nhưng cột Sales THẤP NHẤT!',
            [
                ('True Data / Wrong Claim', 'Aldine Press có lượng in lớn thứ nhì và doanh số cao nhất — không bác bỏ tuyên bố.'),
                ('Opposite Direction (Supports!)', 'Torresani (800 → 710) cao hơn Locatelli (600 → 530), điều này ỦNG HỘ chứ không làm yếu tuyên bố.'),
                ('Incomplete Data', 'Chỉ nêu Locatelli in ít nhất (600 bản) mà không so sánh doanh số với xưởng in lớn hơn.'),
                ('Đáp án đúng', 'Scotto Press là phản ví dụ chí mạng: in nhiều nhất (1.200) nhưng bán ít nhất bảng (420), thua cả xưởng in một nửa số đó (600 → 530).'),
            ]
        ),

        # --- Q15: Information and Ideas — Inferences ---
        q_item(
            'm5_m1_q15', 15, 'Information and Ideas', 'Inferences', 'Hard',
            '<p>In the Marshall Islands, master navigators traditionally wove intricate lattices of coconut-palm ribs and cowrie shells known as <i>rebbelib</i> stick charts to depict how ocean swells bend and intersect around island atolls. Anthropologists have noted two striking habits surrounding these charts: navigators strictly left them ashore rather than consulting them aboard canoes at sea, and each master curved the palm ribs in personal ways that another island’s navigator could not easily read without explanation. Taken together, these practices strongly imply that stick charts functioned primarily as ______</p>',
            'Which choice most logically completes the text?',
            [
                'standardized government charts distributed to help visiting European ships avoid coral reefs.',
                'decorative ceremonial shields strapped to the prows of double-hulled canoes during open-ocean voyages.',
                'individualized shore-based memory and teaching tools rather than universal nautical maps consulted during voyages.',
                'inaccurate sketches that navigators abandoned because ocean swells shift unpredictably every hour.'
            ],
            'C',
            'Ghép 2 tiền đề (1-Millimeter Rule): (A) Thủy thủ luôn ĐỂ BẢN ĐỒ TRÊN BỜ, không mang xuống xuồng khi ra khơi; (B) Mỗi bậc thầy uốn gân dừa theo phong cách CÁ NHÂN mà người khác không tự đọc được nếu không giải thích ⇒ Suy luận trực tiếp: Bản đồ que đóng vai trò là CÔNG CỤ GHI NHỚ VÀ GIẢNG DẠY CÁ NHÂN HÓA TRÊN BỜ chứ không phải hải đồ tiêu chuẩn hóa mang theo tra cứu giữa biển (C)!',
            'Ánh xạ 1-1 hai manh mối: "left ashore" → shore-based memory/teaching tools; "personal ways another could not read" → individualized rather than universal!',
            [
                ('Contradiction', 'Bản đồ làm theo kiểu cá nhân khó đọc nếu không giải thích — trái ngược hoàn toàn với "standardized charts" cho tàu châu Âu.'),
                ('Contradiction', 'Bài nói rõ hoa tiêu ĐỂ CHÚNG TRÊN BỜ ("strictly left them ashore"), không buộc lên mũi xuồng đi biển.'),
                ('Đáp án đúng', 'Kết hợp gọn gàng cả hai dữ kiện (để trên bờ + ký hiệu mang tính cá nhân) mà không suy diễn quá đà.'),
                ('Unsupported Negativity', 'Không hề nói bản đồ sai lệch hay bị từ bỏ vì sóng thay đổi hỗn loạn.'),
            ]
        ),

        # --- Q16-Q19: Standard English Conventions — Boundaries ---
        q_item(
            'm5_m1_q16', 16, 'Standard English Conventions', 'Boundaries', 'Easy',
            '<p>Unlike sunlit coral reefs, deep-sea hydrothermal vents receive zero solar ______ chemosynthetic bacteria harness dissolved hydrogen sulfide to anchor thriving abyssal food webs.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['energy;', 'energy,', 'energy', 'energy, because'],
            'A',
            'Vế 1 là IC hoàn chỉnh ("Unlike sunlit coral reefs, deep-sea hydrothermal vents receive zero solar energy"). Vế 2 cũng là IC hoàn chỉnh ("chemosynthetic bacteria harness... food webs"). Giữa 2 IC → dùng dấu chấm phẩy (`;`) = A!',
            'Phát hiện cấu trúc IC + IC không có liên từ đẳng lập → chốt dấu chấm phẩy (;), loại ngay Comma Splice (B) và Run-on (C).',
            [
                ('Đáp án đúng', 'Dấu chấm phẩy (;) ngăn cách chuẩn xác hai mệnh đề độc lập IC + IC.'),
                ('Comma Splice', 'Nối hai mệnh đề độc lập chỉ bằng một dấu phẩy là lỗi Comma Splice.'),
                ('Run-On Sentence', 'Không có dấu câu phân tách hai IC.'),
                ('Illogical Subordination', 'Thêm "because" làm sai logic nhân quả (việc không có ánh nắng không phải DO vi khuẩn khai thác H₂S gây ra).'),
            ]
        ),
        q_item(
            'm5_m1_q17', 17, 'Standard English Conventions', 'Boundaries', 'Medium',
            '<p>Working in a cramped workshop near the Rialto Bridge in 1500, Venetian punchcutter ______ engraved the slender, slanted metal typeface that printers worldwide now recognize as italics.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            [', Francesco Griffo,', 'Francesco Griffo,', 'Francesco Griffo', ', Francesco Griffo'],
            'C',
            'Quy tắc Title + Name không mạo từ: "Venetian punchcutter Francesco Griffo" (không có mạo từ "a/the" trước nghề nghiệp) → Essential → KHÔNG đặt dấu phẩy ở cả hai đầu, nối liền sang động từ chính "engraved" → Chọn C!',
            'Chức danh không mạo từ + Tên riêng + Động từ chính → 0 dấu phẩy (No-Comma Zone)!',
            [
                ('Non-Essential Trap', 'Chỉ dùng cặp dấu phẩy khi chức danh phía trước có mạo từ xác định duy nhất (VD: "the Venetian punchcutter, Francesco Griffo,").'),
                ('No-Comma Zone (S, V)', 'Một dấu phẩy lẻ chặn ngang giữa chủ ngữ và động từ chính "engraved".'),
                ('Đáp án đúng', 'Không dấu phẩy — giữ mạch chủ ngữ và động từ chính trơn tru theo chuẩn SAT.'),
                ('Unpaired Comma', 'Một dấu phẩy lẻ tách rời chức danh và tên riêng.'),
            ]
        ),
        q_item(
            'm5_m1_q18', 18, 'Standard English Conventions', 'Boundaries', 'Hard',
            '<p>To establish an exact timeline for ancient Antarctic ice cores spanning 800,000 years, glaciologists rely on an unmistakable geological ______ microscopic layers of volcanic ash deposited across the entire polar plateau within days of major Southern Hemisphere eruptions.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['marker;', 'marker:', 'marker.', 'marker, and'],
            'B',
            'Vế trái ("...glaciologists rely on an unmistakable geological marker") là 1 IC hoàn chỉnh. Vế phải ("microscopic layers of volcanic ash deposited...") là Cụm danh từ (Noun Phrase — KHÔNG PHẢI IC vì "deposited" là quá khứ phân từ rút gọn, không có động từ chia thì!) giải thích trực tiếp "geological marker" là gì → Bắt buộc dùng dấu hai chấm (`:`) = B!',
            'IC hoàn chỉnh + Cụm danh từ giải thích (không có động từ chia thì) → Dấu hai chấm (:) là lựa chọn duy nhất hợp chuẩn!',
            [
                ('Semicolon + Fragment', 'Vế sau không có động từ chia thì → không phải IC → cấm dùng chấm phẩy.'),
                ('Đáp án đúng', 'Dấu hai chấm (:) sau IC giới thiệu chính xác cụm danh từ định nghĩa "geological marker".'),
                ('Period + Fragment', 'Tách cụm danh từ thành câu độc lập gây lỗi Sentence Fragment.'),
                ('Comma + FANBOYS + Fragment', 'Sau ", and" không phải mệnh đề độc lập và không song song với động từ "rely".'),
            ]
        ),
        q_item(
            'm5_m1_q19', 19, 'Standard English Conventions', 'Boundaries', 'Hard',
            '<p>Permeable interlocking concrete pavers—which allow storm rainwater to seep directly into underlying gravel beds rather than pooling on hot street ______ are increasingly replacing solid asphalt in flood-prone urban districts.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['surfaces,', 'surfaces;', 'surfaces', 'surfaces—'],
            'D',
            'Cụm bổ ngữ chen giữa Chủ ngữ ("Permeable interlocking concrete pavers") và Động từ chính ("are increasingly replacing") mở đầu bằng dấu gạch ngang dài (`—which allow...`) → Phải đóng bằng chính dấu gạch ngang dài thứ hai (`surfaces—`) → Chọn D!',
            'Quy tắc đối xứng Non-Essential Modifier: mở bằng `—` thì bắt buộc đóng bằng `—`!',
            [
                ('Mismatched Pair (— ... ,)', 'Không được mở bằng em-dash rồi đóng bằng dấu phẩy.'),
                ('Semicolon Inside Modifier', 'Dấu chấm phẩy cắt đứt chủ ngữ khỏi động từ "are increasingly replacing".'),
                ('Unclosed Modifier', 'Bỏ quên dấu đóng khiến mệnh đề quan hệ không tách khỏi động từ chính.'),
                ('Đáp án đúng', 'Khép đúng cặp gạch ngang đôi (— ... —) ngay trước động từ chính "are increasingly replacing".'),
            ]
        ),

        # --- Q20-Q22: Standard English Conventions — Form, Structure, and Sense ---
        q_item(
            'm5_m1_q20', 20, 'Standard English Conventions', 'Form, Structure, and Sense', 'Easy',
            '<p>The synchronized snapping of millions of pistol shrimp inhabiting a healthy tropical coral reef ______ a steady crackling chorus audible to hydrophones several kilometers offshore.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['generate', 'have generated', 'generates', 'generating'],
            'C',
            'Gạch bỏ cụm giới từ và phân từ chen giữa: "The synchronized <b>snapping</b> <s>[of millions of pistol shrimp inhabiting a healthy tropical coral reef]</s>". Chủ ngữ thật là danh động từ "The synchronized snapping" (SỐ ÍT!), câu chưa có động từ chính → Chọn "generates" (C)!',
            'Mẹo 3–1: A và B là số nhiều, D là V-ing (Fragment), duy nhất C là động từ chia thì số ít khớp với "snapping"!',
            [
                ('Subject-Verb Mismatch', 'generate là số nhiều — bị đánh lừa bởi danh từ gần nhất "millions of pistol shrimp".'),
                ('Subject-Verb Mismatch', 'have generated là số nhiều.'),
                ('Đáp án đúng', 'generates (số ít, hiện tại đơn) khớp chuẩn với chủ ngữ số ít "The synchronized snapping".'),
                ('Non-Finite Fragment', 'generating là phân từ khiến cả câu thiếu động từ chính.'),
            ]
        ),
        q_item(
            'm5_m1_q21', 21, 'Standard English Conventions', 'Form, Structure, and Sense', 'Hard',
            '<p>Carved from buoyant breadfruit logs and lashed together with braided coconut coir rather than iron nails, ______</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            [
                'traditional Polynesian double-hulled canoes flexed safely beneath steep open-ocean swells.',
                'Polynesian shipwrights engineered double-hulled canoes to flex beneath steep open-ocean swells.',
                'steep open-ocean swells rarely fractured traditional Polynesian double-hulled canoes.',
                'braided coconut lashings allowed Polynesian canoes to absorb steep open-ocean swells.'
            ],
            'A',
            'Dangling Modifier Check! Cụm phân từ mở đầu "Carved from buoyant breadfruit logs and lashed together with braided coconut coir..." (Được đẽo từ gỗ sa kê nổi và buộc bằng dây xơ dừa tết) mô tả NHỮNG CHIẾC XUỒNG HAI THÂN ("traditional Polynesian double-hulled canoes"), KHÔNG mô tả thợ đóng thuyền (B), sóng đại dương (C), hay dây buộc (D)! Duy nhất A đặt đúng "traditional Polynesian double-hulled canoes" làm chủ ngữ ngay sau dấu phẩy!',
            'Tự hỏi: "Thứ gì được đẽo từ gỗ sa kê và buộc bằng dây xơ dừa?" → Chỉ có những chiếc xuồng (canoes)!',
            [
                ('Đáp án đúng', 'Chủ ngữ "traditional Polynesian double-hulled canoes" đặt sát dấu phẩy khớp hoàn toàn với cụm "Carved... and lashed...".'),
                ('Dangling Modifier', 'Thợ đóng thuyền (shipwrights) không phải vật được đẽo từ thân cây sa kê.'),
                ('Dangling Modifier', 'Sóng đại dương (swells) không thể được đẽo từ gỗ và buộc dây dừa.'),
                ('Dangling Modifier', 'Dây xơ dừa (lashings) không được đẽo từ gỗ sa kê rồi tự buộc bằng dây xơ dừa.'),
            ]
        ),
        q_item(
            'm5_m1_q22', 22, 'Standard English Conventions', 'Form, Structure, and Sense', 'Medium',
            '<p>In 1884, American realist author Sarah Orne Jewett published <i>A Country Doctor</i>, a novel whose quiet portraits of coastal Maine townspeople ______ widely praised by Boston literary critics throughout the following decade.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['is', 'were', 'being', 'will be'],
            'B',
            'Kiểm tra cả SỐ (Number) và THÌ (Tense): Chủ ngữ của mệnh đề quan hệ là "quiet <b>portraits</b>" (SỐ NHIỀU!). Mốc thời gian quá khứ hoàn tất rõ ràng: "In 1884... throughout the following decade" (thập niên sau năm 1884 → quá khứ đơn!). Số nhiều + Quá khứ đơn → Chọn "were" (B)!',
            'Khóa đồng thời 2 tiêu chí: Chủ ngữ số nhiều ("portraits") + Mốc thời gian quá khứ ("In 1884... the following decade") → "were".',
            [
                ('Number & Tense Error', '"is" vừa sai số ít (portraits số nhiều) vừa sai thì hiện tại.'),
                ('Đáp án đúng', '"were" khớp chính xác chủ ngữ số nhiều "portraits" và khung thời gian quá khứ thập niên 1880s–1890s.'),
                ('Non-Finite Fragment', '"being" khiến mệnh đề quan hệ "whose quiet portraits..." thiếu động từ chia thì.'),
                ('Tense Mismatch', '"will be" chia tương lai mâu thuẫn với mốc lịch sử 1884.'),
            ]
        ),

        # --- Q23-Q25: Expression of Ideas — Transitions ---
        q_item(
            'm5_m1_q23', 23, 'Expression of Ideas', 'Transitions', 'Easy',
            '<p>Near the ocean’s sunlit surface, phytoplankton rely on solar energy to drive photosynthesis and support nearly every marine food chain. ______, two miles down around dark hydrothermal vents, microbial ecosystems bypass sunlight altogether by oxidizing volcanic chemicals.</p>',
            'Which choice completes the text with the most logical transition?',
            ['Therefore', 'Similarly', 'For example', 'By contrast'],
            'D',
            'Câu 1: Ở tầng mặt có nắng, sinh vật dựa vào ánh sáng mặt trời quang hợp. Câu 2: Ở độ sâu 2 dặm tối đen quanh miệng thủy nhiệt, vi sinh vật bỏ qua hoàn toàn ánh nắng để oxy hóa hóa chất núi lửa → Hai môi trường đối lập trực tiếp → "By contrast" (D)!',
            'Đối chiếu hai bối cảnh ngược chiều nhau hoàn toàn (sunlit surface vs. dark hydrothermal vents) → chốt "By contrast"!',
            [
                ('Wrong Relationship (Cause-Effect)', 'Hệ sinh thái miệng thủy nhiệt không phải hệ quả của việc tảo quang hợp trên mặt biển.'),
                ('False Similarity', 'Hai cơ chế sống hoàn toàn khác biệt (quang hợp vs. hóa tổng hợp), không tương đồng.'),
                ('Wrong Relationship (Example)', 'Miệng thủy nhiệt tối đen không phải ví dụ minh họa cho vùng biển ngập nắng.'),
                ('Đáp án đúng', 'By contrast đánh dấu sắc nét sự tương phản giữa tầng mặt quang hợp và đáy sâu hóa tổng hợp.'),
            ]
        ),
        q_item(
            'm5_m1_q24', 24, 'Expression of Ideas', 'Transitions', 'Medium',
            '<p>By the late fifteenth century, northern Italian paper mills along the rivers near Venice were producing sturdy linen-rag paper at a fraction of the cost of sheepskin parchment. ______, Venetian printers could turn out hundreds of classical texts at prices affordable to university students rather than only wealthy noblemen.</p>',
            'Which choice completes the text with the most logical transition?',
            ['Nevertheless', 'Consequently', 'Meanwhile', 'Instead'],
            'B',
            'Câu 1 (Nguyên nhân): Xưởng giấy vùng lân cận Venice sản xuất giấy giẻ vải bền với chi phí chỉ bằng một phần nhỏ da cừu. Câu 2 (Hệ quả): Các nhà in Venice có thể in hàng trăm bản sách giá rẻ vừa túi tiền sinh viên đại học → Quan hệ Nhân – Quả → "Consequently" (B)!',
            'Nguyên nhân kinh tế (rẻ hơn da cừu nhiều lần) → Kết quả trực tiếp (giá sách giảm vừa sức sinh viên) = "Consequently".',
            [
                ('False Contrast', 'Nevertheless báo hiệu kết quả trái kỳ vọng — ngược với mối quan hệ thuận chiều chi phí giảm → giá bán giảm.'),
                ('Đáp án đúng', 'Consequently nối chính xác nguyên nhân nguồn giấy giá rẻ với hệ quả sách in phổ cập hơn.'),
                ('Wrong Relationship (Time)', 'Meanwhile chỉ hai việc diễn ra song song nhưng không thể hiện mối liên hệ nguyên nhân – kết quả rõ rệt.'),
                ('Wrong Relationship (Replacement)', 'Instead đòi hỏi vế phủ định trước đó.'),
            ]
        ),
        q_item(
            'm5_m1_q25', 25, 'Expression of Ideas', 'Transitions', 'Hard',
            '<p>Urban engineers evaluating reflective cool-pavement sealants must weigh summer cooling benefits against unexpected seasonal and pedestrian side effects. ______, field studies in northern cities have shown that brighter street coatings can slightly increase winter heating demand in adjacent buildings by reflecting away welcome low-angle winter sunshine.</p>',
            'Which choice completes the text with the most logical transition?',
            ['For instance', 'In contrast', 'As a result', 'Nevertheless'],
            'A',
            'Câu 1 nêu nhận định tổng quát: kỹ sư phải cân nhắc giữa lợi ích làm mát mùa hè và các tác dụng phụ bất ngờ theo mùa/cho người đi bộ ("unexpected seasonal and pedestrian side effects"). Câu 2 đưa ra MỘT VÍ DỤ CỤ THỂ minh họa đúng cho "unexpected seasonal side effects" (nghiên cứu ở các thành phố phía bắc cho thấy mặt đường sáng phản xạ bớt nắng ấm mùa đông làm tăng nhẹ nhu cầu sưởi) → "For instance" (A)!',
            'Tổng quát ("unexpected seasonal side effects") → Trường hợp minh họa cụ thể ("field studies in northern cities... winter heating demand") = "For instance"!',
            [
                ('Đáp án đúng', 'For instance dẫn nhập hoàn hảo ví dụ thực nghiệm minh họa cho tác dụng phụ theo mùa nêu ở câu 1.'),
                ('False Contrast', 'Câu 2 minh họa và chứng thực câu 1, hoàn toàn không mâu thuẫn với câu 1.'),
                ('Wrong Relationship (Cause-Effect)', 'Nghiên cứu ở thành phố phía bắc không phải hệ quả xảy ra do kỹ sư cân nhắc.'),
                ('False Contrast', 'Nevertheless đảo chiều lập luận, sai khi câu 2 cụ thể hóa đúng ý câu 1.'),
            ]
        ),

        # --- Q26-Q27: Expression of Ideas — Rhetorical Synthesis ---
        q_item(
            'm5_m1_q26', 26, 'Expression of Ideas', 'Rhetorical Synthesis', 'Medium',
            '''<p>While researching paleoclimatology, a student has taken the following notes:</p>
            <ul>
              <li>Paleoclimatologists drill deep ice cores at widely separated Antarctic sites such as Dome C and Vostok to reconstruct ancient climate records.</li>
              <li>Because snowfall accumulates at different speeds across Antarctica, two ice cores of the exact same depth often come from different historical centuries.</li>
              <li>Major Southern Hemisphere volcanic eruptions scatter thin, chemically distinct layers of microscopic ash—called tephra—across the entire ice sheet within days.</li>
              <li>By locating the same volcanic tephra layer in multiple ice cores, scientists can lock those separate climate timelines to the exact same calendar year.</li>
            </ul>''',
            'The student wants to explain how scientists align the timelines of Antarctic ice cores drilled at sites with different snowfall rates. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
            [
                'Paleoclimatologists drill deep Antarctic ice cores at distant sites including Dome C and Vostok to study ancient climates.',
                'Snowfall accumulates at uneven speeds across the Antarctic plateau, meaning identical ice depths rarely correspond to the same century.',
                'Because a major volcanic eruption spreads a chemically distinct tephra layer across Antarctica within days, scientists match that shared ash horizon across separate ice cores to synchronize their timelines despite differing snowfall rates.',
                'Microscopic layers of volcanic ash deposited across Antarctica are known to paleoclimatologists as tephra.'
            ],
            'C',
            'Goal-First SOP: Giải thích CÁCH THỨC (HOW) các nhà khoa học đồng bộ mốc thời gian của các lõi băng ở những nơi có tốc độ tuyết rơi khác nhau. A chỉ kể địa điểm khoan; B chỉ nêu vấn đề tuyết rơi không đều mà thiếu giải pháp; D chỉ định nghĩa từ "tephra". Duy nhất C giải thích trọn cơ chế: dùng lớp tro núi lửa tephra có chữ ký hóa học đồng nhất lắng xuống trong vài ngày làm mốc khớp chung giữa các lõi băng! Chọn C!',
            'Tìm đáp án chứa đủ phương tiện ("match shared tephra layer") + mục tiêu giải quyết vấn đề ("synchronize timelines despite differing snowfall rates")!',
            [
                ('Wrong Synthesis Goal', 'Chỉ nêu tên địa điểm khoan lõi băng, không giải thích cách đồng bộ niên đại.'),
                ('Problem Only (Missing How)', 'Chỉ nhắc vấn đề tốc độ tuyết rơi khác nhau mà không nói cách khắc phục bằng lớp tro núi lửa.'),
                ('Đáp án đúng', 'Giải thích đầy đủ và súc tích cách dùng lớp tro tephra chung để khớp mốc thời gian giữa các lõi băng khác tốc độ tuyết.'),
                ('Definition Only', 'Chỉ định nghĩa thuật ngữ tephra, không đề cập đồng bộ lõi băng.'),
            ]
        ),
        q_item(
            'm5_m1_q27', 27, 'Expression of Ideas', 'Rhetorical Synthesis', 'Hard',
            '''<p>While researching nineteenth-century American literature, a student has taken the following notes:</p>
            <ul>
              <li>American Romanticism flourished roughly between 1820 and 1860, represented by essays and poems celebrating untamed wilderness, individual intuition, and sublime spiritual truths.</li>
              <li>American Realism emerged after the Civil War in the late nineteenth century, led by novelists and short-story writers reacting against idealized romance.</li>
              <li>Realist fiction focused closely on ordinary daily labor, regional speech dialects, and the concrete economic pressures shaping working-class and middle-class lives.</li>
              <li>Both literary movements played foundational roles in shaping an independent national voice in nineteenth-century American letters.</li>
            </ul>''',
            'The student wants to highlight a primary thematic contrast between nineteenth-century American Romanticism and American Realism. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
            [
                'Both nineteenth-century American Romanticism and American Realism helped forge an independent national literary voice in the United States.',
                'Emerging after the Civil War, American Realist writers incorporated regional speech dialects and concrete economic pressures into their novels and short stories.',
                'American Romanticism thrived from roughly 1820 to 1860, several decades before American Realism rose to prominence following the Civil War.',
                'Whereas nineteenth-century American Romanticism celebrated untamed wilderness and sublime spiritual intuition, American Realism turned its focus toward ordinary daily labor, regional dialect, and concrete economic pressures.'
            ],
            'D',
            'Goal-First SOP: Làm nổi bật SỰ TƯƠNG PHẢN VỀ CHỦ ĐỀ (thematic contrast) giữa CẢ HAI trào lưu (Romanticism vs. Realism). A nói điểm chung; B chỉ nói về Realism; C chỉ đối chiếu mốc thời gian lịch sử (1820–1860 vs. after Civil War) chứ không phải chủ đề văn học! Duy nhất D dùng "Whereas" đối lập thẳng chủ đề của hai trào lưu (wilderness & spiritual intuition ↔ ordinary daily labor, regional dialect, economic pressures)! Chọn D!',
            'Soát 3 khóa trong Goal: `thematic` (chủ đề, không chỉ niên đại) + `contrast` + `both movements`!',
            [
                ('Wrong Synthesis Goal', 'Nhấn mạnh điểm giống nhau thay vì sự tương phản chủ đề.'),
                ('Single Subject Trap', 'Chỉ mô tả chủ đề của Realism mà thiếu hẳn Romanticism.'),
                ('Wrong Criterion (Time vs. Theme)', 'Chỉ so sánh khung thời gian lịch sử thay vì sự khác biệt về chủ đề sáng tác.'),
                ('Đáp án đúng', 'Đối chiếu chuẩn xác hai trọng tâm chủ đề đối lập giữa Romanticism và Realism.'),
            ]
        ),
    ]
