# -*- coding: utf-8 -*-
"""
Full-Length Adaptive Mock Test #5 — Module 2 HARD Route (27 Qs, Hard & Elite 750+, 32 min)
Exact College Board Digital SAT R&W Blueprint:
Q1-5: Words in Context | Q6-7: Text Structure/Purpose | Q8: Cross-Text
Q9-10: Central Ideas/Details | Q11-12: Evidence (Textual) | Q13-14: Evidence (Quantitative)
Q15: Inferences | Q16-19: Boundaries | Q20-22: Form/Structure/Sense
Q23-25: Transitions | Q26-27: Rhetorical Synthesis
"""

from sat_drills_1_1_and_2_1 import q_item
from sat_drills_5_4_to_5_5 import svg_bar_chart, html_table

def get_m2h_questions():
    return [
        # --- Q1-Q5: Craft and Structure — Words in Context (Elite 750+) ---
        q_item(
            'm5_m2h_q1', 1, 'Craft and Structure', 'Words in Context', 'Elite (750+)',
            '<p>Unlike hasty commercial printers in fifteenth-century Europe who reproduced corrupt medieval manuscripts verbatim, the Venetian Aldine Press earned continent-wide renown for its ______ editorial standards, convening Greek philologists to compare dozens of surviving codices before a single lead letter was cast.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            ['perfunctory', 'lenient', 'exacting', 'equivocal'],
            'C',
            'Contrast + Restatement Clue: đối lập với các nhà in vội vã chép nguyên bản lỗi ("hasty... reproduced corrupt manuscripts verbatim") + vế chứng minh phía sau (mời các nhà ngữ văn Hy Lạp đối chiếu hàng chục bản chép tay trước khi đúc dù chỉ một con chữ chì) → KHẮT KHE, ĐÒI HỎI ĐỘ CHÍNH XÁC NGHIÊM NGẶT → Nghĩa thứ cấp học thuật của "exacting" = rigorously demanding / meticulous → Chọn C!',
            'Nhớ nghĩa thứ cấp vàng 750+ của "exacting" (adj): khắt khe, đòi hỏi tiêu chuẩn cực cao — đối lập hoàn toàn với "perfunctory" (qua loa) và "lenient" (dễ dãi)!',
            [
                ('Opposite Meaning', 'perfunctory = qua loa chiếu lệ — mô tả nhóm nhà in vội vã chứ không phải xưởng Aldine.'),
                ('Opposite Meaning', 'lenient = dễ dãi lỏng lẻo — mâu thuẫn với quy trình đối chiếu hàng chục bản cổ thư.'),
                ('Đáp án đúng', 'exacting (nghĩa thứ cấp: nghiêm ngặt, đòi hỏi độ chính xác cực cao) khớp 100% với tiêu chuẩn biên tập của Aldine Press.'),
                ('Wrong Meaning', 'equivocal = mập mờ nước đôi — không phù hợp để khen ngợi chuẩn biên tập học thuật.'),
            ]
        ),
        q_item(
            'm5_m2h_q2', 2, 'Craft and Structure', 'Words in Context', 'Elite (750+)',
            '<p>Biochemists once assumed that crushing hydrostatic pressures exceeding 400 atmospheres would inevitably ______ cellular enzyme activity around abyssal hydrothermal vents; instead, piezophilic microbes have evolved water-repelling protein cores that fold reliably and sustain vigorous catalysis even under extreme compression.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            ['arrest', 'engender', 'sanction', 'buttress'],
            'A',
            'Contrast Clue: "once assumed that crushing pressures... would inevitably ______ enzyme activity; instead, microbes... sustain vigorous catalysis" → đối lập trực tiếp với "sustain vigorous catalysis" (duy trì xúc tác mạnh mẽ) → NGĂN CHẶN / LÀM NGƯNG TRỆ hoàn toàn → Nghĩa thứ cấp học thuật của "arrest" (v) = halt / bring to a stop → Chọn A!',
            'Thuộc nghĩa thứ cấp sát thủ trên Hard Module 2: "arrest" (động từ khoa học) = làm ngưng trệ, chặn đứng một quá trình (như "arrest decay / arrest cellular activity"), KHÔNG liên quan đến cảnh sát bắt giữ!',
            [
                ('Đáp án đúng', 'arrest (nghĩa thứ cấp khoa học: chặn đứng, làm ngừng trệ) — đối lập sắc nét với "sustain vigorous catalysis".'),
                ('Opposite Meaning', 'engender = sinh ra, tạo ra — trái ngược với giả định áp suất nghiền nát phá hỏng hoạt động enzyme.'),
                ('Wrong Context', 'sanction = phê chuẩn hoặc trừng phạt pháp lý — không dùng với áp suất thủy tĩnh và enzyme.'),
                ('Opposite Meaning', 'buttress = củng cố, chống đỡ — ngược hoàn toàn với hướng đối lập sau "instead".'),
            ]
        ),
        q_item(
            'm5_m2h_q3', 3, 'Craft and Structure', 'Words in Context', 'Elite (750+)',
            '<p>Whereas early municipal briefings hailed high-albedo white street sealants as a stand-alone cure for urban heat islands, newer microclimate studies offer a more ______ endorsement: reflective coatings lower asphalt surface temperatures substantially, yet they cannot replace tree canopies that shield pedestrians from direct solar radiation.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            ['unequivocal', 'strident', 'unreserved', 'qualified'],
            'D',
            'Contrast + Colon Clue: đối lập với "stand-alone cure" (liều thuốc vạn năng độc lập) + dấu hai chấm giải thích cân bằng hai mặt ("lower asphalt temperatures substantially, YET they cannot replace tree canopies...") → sự ủng hộ CÓ ĐIỀU KIỆN / DÈ DẶT CÓ CHỪNG MỰC → Nghĩa thứ cấp học thuật của "qualified" = limited / conditional / tempered → Chọn D!',
            'Cặp từ 750+ kinh điển: "qualified endorsement / qualified praise" = lời tán đồng có điều kiện (chứ KHÔNG phải "có bằng cấp"!).',
            [
                ('Opposite Meaning', 'unequivocal = dứt khoát tuyệt đối không nghi ngờ — trái với vế hạn chế "yet they cannot replace...".'),
                ('Wrong Tone', 'strident = gay gắt chói tai — sai sắc thái cân bằng thận trọng của nghiên cứu khoa học.'),
                ('Opposite Meaning', 'unreserved = hoàn toàn không chút dè dặt — đối lập trực tiếp với vế hạn chế phía sau dấu hai chấm.'),
                ('Đáp án đúng', 'qualified (nghĩa thứ cấp: có giới hạn, kèm điều kiện) phản ánh trọn vẹn lập trường "tốt cho mặt đường nhưng không thay được tán cây".'),
            ]
        ),
        q_item(
            'm5_m2h_q4', 4, 'Craft and Structure', 'Words in Context', 'Elite (750+)',
            '<p>Near the rocky floor beneath East Antarctica’s Dome C, geothermal heat and slow glacial shearing have folded ancient ice strata back onto themselves; because this turbulent mixing blends air bubbles from vastly different epochs into a single warped band, paleoclimatologists caution that chronological reconstructions drawn from the bottommost hundred meters remain ______.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            ['irrefutable', 'tenuous', 'immutable', 'exhaustive'],
            'B',
            'Cause-Effect Clue: địa nhiệt và trượt băng làm gập lớp, trộn lẫn bọt khí từ nhiều kỷ nguyên khác hẳn nhau vào cùng một dải băng bị méo → các nhà cổ khí hậu học CẢNH BÁO rằng việc tái dựng niên đại ở 100 mét sâu nhất vẫn MONG MANH / THIẾU CHẮC CHẮN → "tenuous" (B)!',
            'Khóa động từ "caution" + nguyên nhân "blends air bubbles from vastly different epochs" → chọn tính từ chỉ độ tin cậy yếu ớt, mong manh ("tenuous").',
            [
                ('Opposite Meaning', 'irrefutable = không thể bác bỏ, chắc chắn tuyệt đối — trái ngược hoàn toàn với lời cảnh báo xáo trộn niên đại.'),
                ('Đáp án đúng', 'tenuous = mong manh, lỏng lẻo, thiếu nền tảng vững chắc — khớp hoàn hảo với dữ liệu băng bị gập trộn.'),
                ('Wrong Meaning', 'immutable = bất biến không thể thay đổi — không phản ánh độ thiếu chắc chắn của phép phục dựng.'),
                ('Opposite Meaning', 'exhaustive = toàn diện đầy đủ từng chi tiết — mâu thuẫn với sự xáo trộn hỗn độn các lớp băng.'),
            ]
        ),
        q_item(
            'm5_m2h_q5', 5, 'Craft and Structure', 'Words in Context', 'Elite (750+)',
            '<p>Deploying underwater speakers to broadcast vibrant reef soundscapes over bleached coral rubble does not ______ the urgent need to curb ocean warming; rather, acoustic enrichment merely buys degraded reefs a narrow ecological reprieve by drawing in algae-grazing fish until thermal conditions stabilize.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            ['accentuate', 'corroborate', 'obviate', 'precipitate'],
            'C',
            'Contrast + Restatement Clue: "does NOT ______ the urgent need to curb ocean warming; rather, acoustic enrichment merely buys... a narrow reprieve" → chỉ giúp câu giờ tạm thời chứ KHÔNG LOẠI BỎ ĐƯỢC SỰ CẦN THIẾT của việc giảm ấm lên đại dương → "obviate" (C)!',
            'Nhớ cụm collocation đinh 800-level: "obviate the need for / to X" = loại bỏ nhu cầu phải làm X (làm X trở nên không còn cần thiết)!',
            [
                ('Opposite Direction', 'accentuate = làm nổi bật thêm — nếu nói "does not accentuate the need" sẽ lệch với ý "merely buys a narrow reprieve".'),
                ('Wrong Meaning', 'corroborate = củng cố bằng chứng — không kết hợp logic với "the urgent need".'),
                ('Đáp án đúng', 'obviate = xóa bỏ sự cần thiết (làm cho không cần phải làm gì nữa) — khớp tuyệt đối cấu trúc "does not obviate the need; rather, merely buys a reprieve".'),
                ('Wrong Meaning', 'precipitate = châm ngòi đột ngột — sai logic hoàn toàn với bối cảnh câu giờ bảo tồn.'),
            ]
        ),

        # --- Q6-Q7: Craft and Structure — Text Structure and Purpose (Hard / Elite) ---
        q_item(
            'm5_m2h_q6', 6, 'Craft and Structure', 'Text Structure and Purpose', 'Elite (750+)',
            '<p>For much of the twentieth century, several European maritime historians contended that prehistoric Polynesian settlers reached remote Pacific archipelagos solely by accidental storm drift. In 1976, the double-hulled voyaging canoe <i>Hōkūleʻa</i> decisively overturned that claim by sailing 4,000 kilometers from Hawaiʻi to Tahiti under Micronesian master navigator Mau Piailug without a single compass or chart. <u>Yet anthropologist Dr. Tevita Kaho cautions against reducing the 1976 crossing to a feat of rote star memorization, noting that Piailug continuously improvised course adjustments by combining faint swell rebounds felt through the canoe’s hull with subtle greenish sky reflections cast upward by unseen lagoon atolls.</u></p>',
            'Which choice best describes the function of the underlined sentence in the text as a whole?',
            [
                'It restores the earlier twentieth-century theory that accidental storm drift played the primary role in Polynesian settlement.',
                'It argues that Mau Piailug relied secretly on European navigational charts during the final stage of the 1976 voyage.',
                'It compares the hull construction of Micronesian outrigger canoes with that of Hawaiian double-hulled vessels.',
                'It nuances popular understanding of the 1976 voyage by emphasizing the dynamic, multisensory improvisation that accompanied star knowledge.'
            ],
            'D',
            'Câu 1–2 trình bày chiến tích năm 1976 bác bỏ thuyết trôi dạt tình cờ. Câu gạch chân mở bằng "Yet... cautions against reducing the 1976 crossing to a feat of rote star memorization" rồi chỉ ra bản chất tinh vi hơn: Piailug liên tục ứng biến bằng đa giác quan (cảm nhận sóng dội qua thân xuồng + sắc phản quang xanh của đầm phá lên mây trời) → Tinh chỉnh / làm sâu sắc cách hiểu giản lược về chuyến hải trình → Chọn D!',
            'Nhận diện cụm "cautions against reducing X to [simplified view], noting instead [richer complexity]" → chức năng luôn là "nuances / refines an interpretation"!',
            [
                ('Contradiction', 'Kaho hoàn toàn không phục hồi thuyết trôi dạt tình cờ — ông chỉ ca ngợi chiều sâu trí tuệ của kỹ thuật dẫn đường chủ động.'),
                ('Contradiction', 'Câu 2 khẳng định chuyến đi không dùng bất kỳ la bàn hay hải đồ nào; Kaho nói về cảm nhận sóng và ánh mây.'),
                ('Out of Scope', 'Không so sánh kỹ thuật đóng thân xuồng Micronesia và Hawaii.'),
                ('Đáp án đúng', 'Khớp sát chức năng tu từ: phản bác lối nhìn đơn giản hóa (chỉ học thuộc sao) để làm nổi bật năng lực ứng biến đa giác quan.'),
            ]
        ),
        q_item(
            'm5_m2h_q7', 7, 'Craft and Structure', 'Text Structure and Purpose', 'Hard',
            '<p><i>The following text is adapted from an 1891 American realist novella. After thirty years piloting timber steamboats along the Missouri River, Captain Silas Mercer watches ironworkers rivet the final span of a railway bridge over the bend where he once memorized every hidden sandbar.</i><br/>Men on the levee expected Mercer to curse the ringing hammers and the black smoke of the rail crane. Instead, he stood quietly beside the willow bank until the last red-hot rivet cooled to gray, then drew from his coat the oilskin ledger in which he had charted thirty winters of shifting shoals and handed it to the young bridge engineer. “Keep the soundings for your piers,” Mercer said evenly. “A river changes its mind faster than iron likes, even after the steamboats are gone.”</p>',
            'Which choice best states the main purpose of the text?',
            [
                'To portray an aging steamboat pilot’s composed, practical acceptance that railway technology is superseding his lifelong trade.',
                'To argue that nineteenth-century railway engineers intentionally ignored safety warnings from experienced river pilots.',
                'To explain the metallurgical process ironworkers used to fasten bridge spans over the Missouri River.',
                'To criticize residents on the levee for encouraging Captain Mercer to abandon his steamboat career prematurely.'
            ],
            'A',
            'Người trên đê tưởng Mercer sẽ nguyền rủa cây cầu sắt cướp nghề của mình ("expected Mercer to curse..."). Trái lại ("Instead"), ông lặng lẽ chờ đóng xong đinh tán cuối, điềm đạm trao quyển sổ ghi 30 năm kinh nghiệm bãi cạn cho kỹ sư cầu trẻ để giúp bảo vệ trụ cầu, chấp nhận bình thản rằng kỷ nguyên tàu hơi nước đang lùi lại ("even after the steamboats are gone") → Chọn A!',
            'Khóa cặp đối lập "expected Mercer to curse... Instead, he stood quietly... handed it to the young bridge engineer" để bắt đúng thái độ điềm tĩnh, thực tế và không cay đắng!',
            [
                ('Đáp án đúng', 'Khắc họa chuẩn xác tâm thế bình thản, thực tế của vị thuyền trưởng già khi chấp nhận bước chuyển giao từ tàu sông sang đường sắt.'),
                ('Out of Scope / Contradiction', 'Không có chi tiết nào cho thấy kỹ sư trẻ phớt lờ lời cảnh báo an toàn.'),
                ('Literal Misreading', 'Cảnh đóng đinh tán chỉ là bối cảnh biểu tượng, không phải bài giảng luyện kim.'),
                ('Distortion', 'Người trên đê chỉ đoán ông sẽ nổi giận, không hề thúc giục ông bỏ nghề sớm.'),
            ]
        ),

        # --- Q8: Craft and Structure — Cross-Text Connections (Elite 750+) ---
        q_item(
            'm5_m2h_q8', 8, 'Craft and Structure', 'Cross-Text Connections', 'Elite (750+)',
            '<p><b>Text 1</b><br/>Deep-sea zoologist Dr. Evelyn Cho observes that the scaly-foot gastropod (<i>Chrysomallon squamiferum</i>), a snail living near Indian Ocean black-smoker vents, embeds dense plates of magnetic iron sulfides—pyrite and greigite—into both its outer shell and the overlapping scales covering its fleshy foot. Because crushing vent crabs patrol the same chimneys, Cho proposes that this metallic outer coating evolved primarily as mechanical armor against predation.</p><p><b>Text 2</b><br/>Comparing scaly-foot gastropods across multiple Indian Ocean vent fields with sharply differing mineral chemistries, biochemist Dr. Rashid Mansour discovered a thriving population at the iron-poor Solitaire vent field whose white shells contain zero iron sulfide yet suffer no elevated crab-predation mortality. Meanwhile, cellular imaging of metallic-shelled snails at sulfur-rich vents revealed specialized internal channels that export toxic excess sulfur ions out of living tissues and lock them safely as inert iron sulfide on the exterior scales.</p>',
            'Based on the texts, how would Dr. Rashid Mansour (Text 2) most likely respond to Dr. Evelyn Cho’s proposal (Text 1)?',
            [
                'By asserting that scaly-foot gastropods do not actually incorporate iron sulfides into their outer shells at any Indian Ocean vent field.',
                'By arguing that iron-sulfide coating may function primarily as a physiological mechanism for detoxifying excess volcanic sulfur rather than having evolved mainly as anti-predator armor.',
                'By claiming that predatory vent crabs are absent from sulfur-rich black-smoker chimneys throughout the Indian Ocean.',
                'By agreeing that metallic iron armor is strictly indispensable for protecting scaly-foot snails from crushing crabs across all vent fields.'
            ],
            'B',
            'Text 1 cho rằng lớp vảy sắt sunfua tiến hóa chủ yếu làm GIÁP CƠ HỌC chống cua ăn thịt. Text 2 đưa 2 bằng chứng đòn bẩy: (1) Ở miệng thủy nhiệt nghèo sắt (Solitaire), ốc KHÔNG có lớp sắt sunfua vẫn sống khỏe, tỷ lệ bị cua ăn thịt không tăng (làm yếu giả thuyết giáp chống cua là chức năng chính); (2) Ở miệng giàu lưu huỳnh, ốc dùng kênh tế bào chuyên biệt ĐẨY ION LƯU HUỲNH ĐỘC HẠI ra ngoài rồi khóa lại thành sắt sunfua trơ trên vảy → Giải thích chức năng chính là CƠ CHẾ THẢI ĐỘC SINH LÝ (physiological detoxification) → Chọn B!',
            'Bẫy 750+ kinh điển: Mansour KHÔNG phủ nhận sự tồn tại của lớp sắt ở miệng giàu lưu huỳnh (loại A), mà chứng minh lớp sắt có chức năng nguyên phát là thải độc lưu huỳnh (detoxification) vì quần thể không có giáp sắt vẫn không bị cua tiêu diệt nhiều hơn!',
            [
                ('Overstated Conflict / Contradiction', 'Mansour xác nhận nhóm ốc ở miệng giàu lưu huỳnh CÓ lớp vỏ kim loại sắt sunfua — ông chỉ kiểm tra thêm quần thể nghèo sắt ở Solitaire.'),
                ('Đáp án đúng', 'Khớp trọn cả hai bằng chứng của Mansour: ốc không giáp sắt không tăng tỷ lệ tử vong vì cua + kênh tế bào xuất lưu huỳnh độc ra vỏ ngoài để thải độc.'),
                ('Out of Scope', 'Text 2 không hề nói cua ăn thịt vắng mặt ở các miệng thủy nhiệt giàu lưu huỳnh.'),
                ('Contradiction', 'Quần thể không có sắt sunfua ở Solitaire vẫn sống phát đạt ("thriving population") → lớp sắt KHÔNG phải là thiết yếu tuyệt đối để sống sót trước cua.'),
            ]
        ),

        # --- Q9-Q10: Information and Ideas — Central Ideas and Details (Elite 750+) ---
        q_item(
            'm5_m2h_q9', 9, 'Information and Ideas', 'Central Ideas and Details', 'Elite (750+)',
            '<p>To attract entrepreneurial printers willing to shoulder the steep capital cost of casting original Greek and italic typefaces, the Venetian Senate began awarding ten-year printing monopolies known as <i>privilegi</i> during the 1490s. Yet because Venetian decrees carried zero legal force beyond the Republic’s territorial borders, rival workshops in Lyon and Florence routinely counterfeited Aldus Manutius’s sleek italic classics within months of publication—ironically circulating Venetian humanist scholarship across northern Europe far more rapidly and cheaply than Venice’s own protected presses could supply.</p>',
            'Which choice best states the main idea of the text?',
            [
                'Venetian printing patents succeeded in preventing workshops in Lyon and Florence from copying italic classics for a full decade.',
                'The Venetian Senate outlawed italic typefaces because rival French publishers refused to pay licensing royalties.',
                'Because Venetian printing monopolies could not be enforced outside the Republic, foreign counterfeiting paradoxically accelerated the European spread of Venetian humanist editions.',
                'Aldus Manutius deliberately distributed his lead typefaces to printers in Lyon and Florence to expand access to Greek scholarship.'
            ],
            'C',
            'Mạch lập luận trớ trêu (ironic paradox) toàn đoạn: Thượng viện Venice cấp đặc quyền độc quyền 10 năm (`privilegi`) để bảo vệ nhà in nội địa → NHƯNG sắc lệnh vô hiệu ngoài biên giới Cộng hòa → Xưởng ở Lyon và Florence in lậu ngay lập tức → Trớ trêu là chính nạn in lậu xuyên biên giới lại phát tán học thuật nhân văn Venice khắp châu Âu nhanh và rẻ hơn cả bản gốc Venice → Chọn C!',
            'Khóa cụm "Yet because... carried zero legal force beyond borders... ironically circulating... far more rapidly" để bắt trọn nghịch lý trung tâm của đoạn!',
            [
                ('Contradiction', 'Bản in lậu ở Lyon và Florence ra đời chỉ trong vài tháng chứ đặc quyền 10 năm hoàn toàn không chặn được chúng.'),
                ('Out of Scope / Contradiction', 'Thượng viện Venice khuyến khích và bảo hộ kiểu chữ mới, không hề cấm.'),
                ('Đáp án đúng', 'Tóm gọn chính xác nghịch lý: phạm vi pháp lý hạn hẹp của đặc quyền Venice mở đường cho in lậu nước ngoài, vô tình đẩy nhanh tốc độ lan tỏa sách nhân văn.'),
                ('Contradiction', 'Các xưởng nước ngoài sao chép lậu ("counterfeited"), không phải được Manutius chủ động chia sẻ khuôn chữ.'),
            ]
        ),
        q_item(
            'm5_m2h_q10', 10, 'Information and Ideas', 'Central Ideas and Details', 'Elite (750+)',
            '<p><i>The following poem is adapted from an 1858 American Romantic lyric titled “Soundings on the Hudson.”</i><br/>The merchant measures all the stream<br/>By draft of keel and freight of pine,<br/>And counts the tide a servant team<br/>To haul his timber down the line.<br/><br/>Yet where the granite palisade<br/>Drops dark reflection to the floor,<br/>A depth no plumb-line ever weighed<br/>Outlasts the wharf and busy shore.</p>',
            'Based on the poem, how does the speaker contrast the merchant’s view of the river with the speaker’s own perspective?',
            [
                'Whereas the merchant fears the river’s treacherous granite cliffs, the speaker celebrates the safe harbors built along the busy shore.',
                'Whereas the merchant refuses to ship timber during high tide, the speaker believes tidal currents are the river’s most commercially valuable asset.',
                'Whereas the merchant values the river only for its dark reflections, the speaker prefers to measure its exact depth using weighted plumb-lines.',
                'Whereas the merchant reduces the river to a utilitarian tool for hauling cargo, the speaker sees in it an enduring, unquantifiable depth that outlives human commerce.'
            ],
            'D',
            'Đối chiếu sắc nét 2 khổ thơ: Khổ 1 mô tả gã thương nhân chỉ đo lường con sông bằng mớn nước tàu, chuyến gỗ thông và coi thủy triều như "đàn ngựa kéo hàng" ("servant team to haul his timber") → cái nhìn thuần túy thương mại thực dụng. Khổ 2 ("Yet...") thể hiện cái nhìn Lãng mạn của thi sĩ: dưới bóng vách đá hoa cương là chiều sâu mà không dây dọi nào cân đo được ("no plumb-line ever weighed"), tồn tại lâu bền hơn mọi bến cảng và bờ bãi sầm uất ("Outlasts the wharf and busy shore") → Chọn D!',
            'Trong thơ Lãng mạn Mỹ thế kỷ 19, luôn đối chiếu vế 1 (thước đo vật chất/thương mại hữu hạn) với vế 2 sau "Yet" (chiều sâu tinh thần/tự nhiên vĩnh cửu)!',
            [
                ('Distortion / Reversed', 'Thương nhân không sợ vách đá, và thi sĩ không ca ngợi bến cảng sầm uất mà nhấn mạnh sông trường tồn vượt lên trên bến cảng.'),
                ('Contradiction', 'Thương nhân tận dụng thủy triều để kéo gỗ, không từ chối; và thi sĩ nhìn vượt khỏi giá trị thương mại.'),
                ('Reversed Roles', 'Đảo ngược hoàn toàn hai nhân vật: chính thương nhân mới là người đo đếm thực dụng, còn thi sĩ nói chiều sâu không dây dọi nào đo nổi.'),
                ('Đáp án đúng', 'Khớp từng ẩn dụ của 2 khổ thơ: thương nhân coi sông là công cụ chở hàng ↔ thi sĩ cảm nhận chiều sâu vô lượng vượt thời gian thương mại.'),
            ]
        ),

        # --- Q11-Q12: Information and Ideas — Command of Evidence (Textual, Elite 750+) ---
        q_item(
            'm5_m2h_q11', 11, 'Information and Ideas', 'Command of Evidence (Textual)', 'Elite (750+)',
            '<p>Marine bioacoustician Dr. Sofia Alverez noted that free-swimming coral larvae navigate toward noisy tropical reefs when selecting a settlement site. Earlier studies attributed this behavior purely to overall sound intensity, driven mostly by high-frequency snapping-shrimp crackle (2–5 kHz). Alverez, however, hypothesized that coral larvae do not rely on snapping-shrimp volume alone; rather, they require low-frequency reef-fish choruses (100–800 Hz) to distinguish thriving coral reefs from barren rocky rubble flats that also teem with noisy snapping shrimp.</p>',
            'Which finding from a controlled laboratory experiment, if true, would most directly support Dr. Sofia Alverez’s hypothesis?',
            [
                'Coral larvae swam strongly toward dual-band reef recordings combining shrimp crackle with low-frequency fish choruses, but exhibited no directional preference toward equally loud recordings containing only high-frequency snapping-shrimp crackle.',
                'Snapping shrimp living on barren rocky rubble flats produced louder peak clicks than snapping shrimp inhabiting healthy branching coral colonies.',
                'Coral larvae failed to settle when exposed to silent saltwater tanks kept at elevated summer temperatures.',
                'Adult reef fish swam away from underwater loudspeakers broadcasting low-frequency boat-engine vibrations between 100 and 800 Hz.'
            ],
            'A',
            'Khóa giả thuyết phân tách của Alverez: Ấu trùng san hô KHÔNG chỉ bị hút bởi độ lớn tiếng tôm gõ mõ tần số cao (2–5 kHz) — chúng CẦN dải tần thấp hợp xướng cá rạn (100–800 Hz) để nhận diện rạn san hô khỏe! Để chứng minh thí nghiệm phải CỐ ĐỊNH ĐỘ LỚN ÂM LƯỢNG ("equally loud") và tách rời 2 biến: [Tôm + Cá] → ấu trùng bơi mạnh tới; [Chỉ Tôm với âm lượng ngang bằng] → không có xu hướng bơi tới! Đáp án A thiết kế thực nghiệm đối chứng chuẩn 800-level → Chọn A!',
            'Trong khoa học thực nghiệm SAT Hard M2, giả thuyết "cần thành phần B chứ không chỉ độ lớn của thành phần A" chỉ được chứng minh bằng thí nghiệm giữ nguyên âm lượng ("equally loud") rồi thử nghiệm [A+B] vs. [chỉ A]!',
            [
                ('Đáp án đúng', 'Tách biến hoàn hảo: cùng âm lượng, chỉ khi có thêm hợp xướng cá tần số thấp ấu trùng mới bơi tới, còn tiếng tôm đơn thuần thì không.'),
                ('Insufficient / Circumstantial', 'Chỉ cho thấy bãi đá trơ cũng có tôm kêu to hơn — không chứng minh hành vi chọn lọc của chính ấu trùng san hô với tiếng cá tần số thấp.'),
                ('Irrelevant Variable', 'Thử nghiệm nước tĩnh ấm liên quan đến nhiệt độ chứ không phân tách tần số âm thanh tôm vs. cá.'),
                ('Irrelevant Subject', 'Phản ứng né tiếng động cơ tàu của cá trưởng thành không kiểm chứng cơ chế định hướng của ấu trùng san hô.'),
            ]
        ),
        q_item(
            'm5_m2h_q12', 12, 'Information and Ideas', 'Command of Evidence (Textual)', 'Elite (750+)',
            '<p>In a scholarly critique of the 1887 American realist drama <i>The Iron Looms</i>, a critic argues that mill owner Harrison displays a self-congratulatory moral blindness: he takes genuine pride in financing a granite public library for his factory town while remaining completely oblivious to the fact that his own grueling fourteen-hour work shifts leave mill operatives too exhausted to ever visit it.</p>',
            'Which quotation from Harrison in <i>The Iron Looms</i> most effectively illustrates the critic’s argument?',
            [
                '“I commissioned the finest Vermont granite and oak shelving in the county so our library facade might rival any lecture hall in Boston.”',
                '“Running the power looms fourteen hours daily is simply what the northern textile market demands if our company is to meet its autumn cloth contracts.”',
                '“I spared no expense on those fine reading rooms so every weaver might elevate his mind—and if the benches sit empty at nine each night, I can only conclude the hands prefer idleness to self-improvement, regardless of how long the looms have run.”',
                '“Several foremen have warned me that young spinners frequently fall asleep beside the cotton bales after supper rather than walking up to the town square.”'
            ],
            'C',
            'Checklist 2 vế bắt buộc của "self-congratulatory moral blindness": [1] Tự hào tài trợ thư viện để nâng cao dân trí + [2] Hoàn toàn mù quáng trước thực tế chính ca làm 14 giờ của mình vắt kiệt sức công nhân (lại đổ lỗi cho công nhân lười biếng). A chỉ có vế khoe kiến trúc thư viện (Half-Match); B chỉ nói chạy máy 14 giờ (Half-Match); D cho thấy quản đốc ĐÃ cảnh báo công nhân kiệt sức buồn ngủ, chưa khắc họa thái độ tự đắc + mù quáng của Harrison. Duy nhất C phơi bày trọn vẹn: "spared no expense... elevate his mind" [1] + đổ lỗi "prefer idleness... regardless of how long the looms have run" [2]! Chọn C!',
            'Kỹ thuật đánh bại bẫy Half-Match trên Hard M2: A chỉ thỏa vế 1, B chỉ thỏa vế 2 → gạt sạch A & B, chốt C chứa trọn vẹn cả hai vế + sự mỉa mai tự mãn!',
            [
                ('Half-Match Trap (Only Vế 1)', 'Chỉ thể hiện niềm tự hào xây thư viện bằng đá hoa cương, thiếu hẳn sự mù quáng trước giờ làm kiệt sức của công nhân.'),
                ('Half-Match Trap (Only Vế 2)', 'Chỉ nhắc ca máy 14 giờ vì hợp đồng thị trường, không nhắc đến thư viện hay niềm tự đắc.'),
                ('Đáp án đúng', 'Khớp xuất sắc cả sự tự hào hào phóng ("spared no expense") lẫn sự mù quáng đạo đức khi đổ lỗi ghế trống cho sự lười biếng bất chấp ca làm kéo dài.'),
                ('Off-Point', 'Lời thuật lại cảnh báo của quản đốc chỉ cho thấy công nhân mệt, không thể hiện trực tiếp niềm tự hào xây thư viện và kết luận mù quáng của Harrison.'),
            ]
        ),

        # --- Q13-Q14: Information and Ideas — Command of Evidence (Quantitative, Elite 750+) ---
        q_item(
            'm5_m2h_q13', 13, 'Information and Ideas', 'Command of Evidence (Quantitative)', 'Elite (750+)',
            svg_bar_chart(
                'Mean Midday Pedestrian Radiant Heat Index (°C) at 1.5 m Height by Street Design',
                ['0°C', '15°C', '30°C', '45°C', '60°C'],
                [('Unshaded Dark', 47, '47°C'), ('Unshaded Cool', 51, '51°C'), ('Shaded Dark', 36, '36°C'), ('Shaded Cool', 34, '34°C')],
                60
            ) + '<p>Urban microclimate researchers investigated how combining reflective “cool” pavement coatings with street-tree canopy shade influences midday thermal comfort at pedestrian body height (1.5 meters). Their field trial revealed a striking conditional effect: reflective pavement delivers the lowest pedestrian heat exposure when paired with overhead shade—slightly outperforming shaded dark asphalt—yet applying the same reflective coating without shade actually worsens midday pedestrian radiant heat compared with unshaded dark asphalt.</p>',
            'Which choice most effectively uses data from the graph to illustrate the researchers’ conditional finding?',
            [
                'Both shaded street designs kept midday pedestrian radiant heat below 40°C, whereas both unshaded designs exceeded 45°C.',
                'Shaded dark asphalt recorded a midday radiant heat index of 36°C, which was 11°C lower than unshaded dark asphalt (47°C).',
                'Unshaded cool pavement recorded the highest midday pedestrian radiant heat index among all four tested street designs at 51°C.',
                'While shaded cool pavement achieved the lowest pedestrian heat index at 34°C—two degrees cooler than shaded dark asphalt (36°C)—unshaded cool pavement reached 51°C, four degrees hotter than unshaded dark asphalt (47°C).'
            ],
            'D',
            'Checklist 2 chiều của "conditional effect" (hiệu ứng có điều kiện): [1] Khi CÓ bóng râm: Shaded Cool đạt mức thấp nhất (34°C), mát hơn nhẹ so với Shaded Dark (36°C, chênh 2°C ✓); [2] Khi KHÔNG bóng râm: Unshaded Cool lại làm NÓNG HƠN (51°C) so với Unshaded Dark (47°C, tăng thêm 4°C ✓). A, B, C đều đúng dữ liệu nhưng chỉ nêu một phần hoặc bỏ qua phép so sánh Cool vs. Dark ở CẢ HAI điều kiện! Duy nhất D ghép đủ cả 4 thanh (34 vs. 36 và 51 vs. 47)!',
            'Hiệu ứng tương tác có điều kiện (interaction effect) đòi hỏi đối chiếu đủ 2 cặp so sánh trái chiều: Cool vs. Dark trong điều kiện Shaded (34 < 36) VÀ trong điều kiện Unshaded (51 > 47)!',
            [
                ('True Data / Missing Interaction', 'Chỉ so sánh chung Shaded (<40°C) vs. Unshaded (>45°C), hoàn toàn không phân biệt được hiệu ứng trái chiều của Cool vs. Dark.'),
                ('True Data / Wrong Comparison', 'Chỉ so sánh Dark có bóng và Dark không bóng (36 vs. 47), bỏ qua hoàn toàn Cool pavement.'),
                ('Half-Match Trap', 'Chỉ nêu vế bất lợi (51°C cao nhất), bỏ quên cả mức đối chứng 47°C lẫn lợi thế 34°C vs. 36°C khi có bóng râm.'),
                ('Đáp án đúng', 'Trình bày chính xác cả hai vế của hiệu ứng điều kiện: 34°C < 36°C khi có bóng râm và 51°C > 47°C khi không bóng râm.'),
            ]
        ),
        q_item(
            'm5_m2h_q14', 14, 'Information and Ideas', 'Command of Evidence (Quantitative)', 'Elite (750+)',
            html_table(
                'Table 1. Glaciological Measurements from Four Antarctic Ice-Core Drilling Sites',
                ['Site', 'Mean Snowfall (cm/yr)', 'Core Depth (m)', 'Continuous Record (kyr)', 'Gas–Ice Age Offset (yrs)'],
                [
                    ['Dome C', '2.5', '3,270', '800', '4,200'],
                    ['Vostok', '2.1', '3,623', '420', '5,100'],
                    ['Dome Fuji', '2.7', '3,035', '720', '3,800'],
                    ['WAIS Divide', '22.0', '3,405', '68', '280'],
                ]
            ) + '<p>Reviewing Table 1 for a geology report, a student claims two things: first, that drilling a deeper ice core always recovers a longer continuous climate record; and second, that sites receiving the least annual snowfall exhibit the smallest chronological offsets between trapped air bubbles and surrounding ice.</p>',
            'Which choice best uses data from the table to refute BOTH parts of the student’s claim?',
            [
                'Dome C yielded the longest continuous climate record in the table (800 kyr), while Dome Fuji yielded the second longest (720 kyr).',
                'Although Vostok (3,623 m) and WAIS Divide (3,405 m) are both deeper than Dome C (3,270 m), each yields a far shorter continuous record (420 kyr and 68 kyr vs. 800 kyr); furthermore, the lowest-snowfall sites—Vostok (2.1 cm/yr) and Dome C (2.5 cm/yr)—show the largest gas–ice age offsets (5,100 yrs and 4,200 yrs) rather than the smallest.',
                'WAIS Divide receives 22.0 cm of annual snowfall—nearly ten times more than Dome C—and exhibits the smallest gas–ice age offset in the table at just 280 years.',
                'Vostok is the deepest core listed at 3,623 meters, whereas Dome Fuji is the shallowest core listed at 3,035 meters.'
            ],
            'B',
            'Câu hỏi yêu cầu bác bỏ ĐỒNG THỜI CẢ HAI VẾ (refute BOTH parts) của học sinh: [Vế 1: Khoan sâu hơn → kỷ lục dài hơn] bị đánh sập bởi Vostok (3.623 m → 420 kyr) và WAIS Divide (3.405 m → 68 kyr) đều SÂU HƠN Dome C (3.270 m → 800 kyr) nhưng cho kỷ lục NGẮN HƠN NHIỀU! [Vế 2: Tuyết rơi ít nhất → độ lệch tuổi khí–băng nhỏ nhất] bị đánh sập bởi Vostok (2.1 cm/yr) và Dome C (2.5 cm/yr) ít tuyết nhất nhưng lại có độ lệch LỚN NHẤT bảng (5.100 năm và 4.200 năm, so với chỉ 280 năm ở nơi nhiều tuyết WAIS Divide)! Duy nhất B phủ sạch cả hai vế với 100% số liệu chính xác!',
            'Khi đề nhấn chữ in hoa "refute BOTH parts", loại ngay lập tức mọi đáp án chỉ xử lý được 1 vế (như C chỉ bác bỏ vế 2)!',
            [
                ('True Data / Wrong Claim', 'Chỉ nêu hai kỷ lục dài nhất (800 kyr và 720 kyr), không bác bỏ mối quan hệ độ sâu hay lượng tuyết.'),
                ('Đáp án đúng', 'Bác bỏ chuẩn xác đồng thời cả hai tuyên bố bằng đúng số liệu đối chứng của Vostok, WAIS Divide và Dome C.'),
                ('Half-Match Trap (Only Vế 2)', 'Chỉ bác bỏ được vế lượng tuyết/độ lệch tuổi mà bỏ quên hoàn toàn vế độ sâu lõi băng (Core Depth vs. Continuous Record).'),
                ('Incomplete Data', 'Chỉ nêu độ sâu lớn nhất và nhỏ nhất mà không đối chiếu với tuổi kỷ lục hay độ lệch khí–băng.'),
            ]
        ),

        # --- Q15: Information and Ideas — Inferences (Elite 750+) ---
        q_item(
            'm5_m2h_q15', 15, 'Information and Ideas', 'Inferences', 'Elite (750+)',
            '<p>Swarming around Mid-Atlantic hydrothermal chimneys 3,600 meters below the ocean surface, the vent shrimp <i>Rimicaris exoculata</i> possesses no conventional image-forming eyes; instead, a bright reflective strip along its back houses rhodopsin visual pigments tuned to detect faint near-infrared thermal radiation emitted by 350°C volcanic plumes. Marine biologists observe that dense crowds of <i>Rimicaris</i> graze on nutrient-rich bacterial mats growing within mere centimeters of scalding vent orifices—where water temperatures plunge from 350°C to 10°C across the width of a hand—yet specimens almost never display fatal thermal burns. Taken together, this anatomy and behavior strongly suggest that the shrimp’s dorsal organ serves primarily to ______</p>',
            'Which choice most logically completes the text?',
            [
                'allow the shrimp to locate and maintain a safe distance from glowing superheated plumes while grazing along nearby bacterial margins.',
                'absorb faint sunlight filtering down 3,600 meters to power photosynthesis inside the bacterial mats.',
                'generate high-intensity infrared heat pulses that stun rival shrimp competing for chimney space.',
                'enable the shrimp to form sharp visual images of distant predators swimming through cold abyssal darkness.'
            ],
            'A',
            'Ghép chuỗi tiền đề 1-Millimeter Rule: (1) Không có mắt tạo ảnh thường, nhưng có cơ quan lưng nhạy với BỨC XẠ HỒNG NGOẠI NHIỆT từ cột nước 350°C; (2) Tôm tụ tập ăn thảm vi khuẩn chỉ cách lỗ phun nước sôi vài cm (chênh nhiệt 350°C → 10°C trong gang tay) mà hầu như KHÔNG BỊ BỎNG CHẾT ⇒ Suy luận chặt chẽ duy nhất: Cơ quan lưng giúp tôm phát hiện luồng nước nóng phát sáng ở cự ly gần để ăn vi khuẩn sát rìa mà giữ khoảng cách an toàn tránh vùng nước sôi chết người (A)!',
            'Nối trực tiếp 2 dữ kiện: phát hiện ánh nhiệt 350°C + ăn sát rìa mà không bị bỏng → định vị và giữ khoảng cách an toàn quanh cột nước nóng!',
            [
                ('Đáp án đúng', 'Khớp sát cả giải phẫu (phát hiện bức xạ nhiệt hồng ngoại gần) lẫn hành vi (ăn sát lỗ phun vài cm mà hầu như không bị bỏng).'),
                ('Contradiction / Scientific Absurdity', 'Ánh sáng mặt trời không thể xuống sâu 3.600 mét, và bài nói rõ cơ quan cảm nhận bức xạ nhiệt từ cột nước núi lửa 350°C.'),
                ('Reversed Function', 'Sắc tố rhodopsin CẢM NHẬN (detect) bức xạ nhiệt chứ không PHÁT RA xung nhiệt làm choáng đối thủ.'),
                ('Contradiction', 'Bài khẳng định tôm KHÔNG có mắt tạo ảnh sắc nét ("no conventional image-forming eyes") và cơ quan cảm nhận nguồn nhiệt nóng, không phải kẻ săn mồi trong nước lạnh.'),
            ]
        ),

        # --- Q16-Q19: Standard English Conventions — Boundaries (Hard / Elite 750+) ---
        q_item(
            'm5_m2h_q16', 16, 'Standard English Conventions', 'Boundaries', 'Elite (750+)',
            '<p>During open-ocean voyages between Tahiti and Hawaiʻi, master Pacific wayfinders cross-check three subtle environmental cues: the rising azimuth of bright guide stars such as Arcturus, known in Hawaiian as Hōkūleʻa; the steady pitch of long-period southern swells, which persist even under heavy cloud ______ and the late-afternoon flight paths of white terns returning to unseen atoll nests.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['cover,', 'cover:', 'cover;', 'cover'],
            'C',
            'Quy tắc Super-Semicolon (Chấm phẩy cấp cao trong danh sách phức tạp): Danh sách gồm 3 mục sau dấu hai chấm, và các mục bản thân đã chứa dấu phẩy bên trong (`Arcturus, known...;`). Mục 1 kết thúc bằng dấu chấm phẩy (`Hōkūleʻa;`) → Mục 2 BẮT BUỘC cũng phải kết thúc bằng dấu chấm phẩy (`cover;`) ngay trước `and` để phân tách rõ 3 phần tử lớn! Chọn C!',
            'Thấy một danh sách liệt kê mà mục 1 đã đóng bằng `;` do chứa phẩy nội bộ → chốt ngay `;` cho mục 2 trước chữ `and`!',
            [
                ('List Hierarchy Error', 'Dùng dấu phẩy sau "cover" sẽ lẫn lộn với dấu phẩy nội bộ của mệnh đề ", which persist..." và phá vỡ tính nhất quán với dấu `;` ở mục 1.'),
                ('Wrong Punctuation', 'Không bao giờ chèn thêm dấu hai chấm thứ hai giữa chừng danh sách.'),
                ('Đáp án đúng', 'Dấu chấm phẩy (;) đồng nhất hoàn hảo với mục 1 để tách gọn 3 mục phức tạp chứa phẩy nội bộ.'),
                ('Missing Separator', 'Thiếu hoàn toàn dấu ngăn giữa mục 2 và mục 3, đồng thời không đóng mệnh đề non-essential ", which persist...".'),
            ]
        ),
        q_item(
            'm5_m2h_q17', 17, 'Standard English Conventions', 'Boundaries', 'Elite (750+)',
            '<p>In 1495, Venetian humanist Aldus Manutius launched an ambitious five-volume Greek edition of Aristotle’s complete ______ scattered Byzantine manuscripts from monasteries across Italy into the first standardized printed corpus of the philosopher’s works.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['writings; uniting', 'writings, uniting', 'writings. Uniting', 'writings, and uniting'],
            'B',
            'Phân tích cấu trúc mệnh đề: Vế 1 ("In 1495, Venetian humanist... complete writings") là 1 IC hoàn chỉnh. Vế 2 ("uniting scattered Byzantine manuscripts... works") là Cụm hiện tại phân từ (Participial Phrase — KHÔNG có chủ ngữ và động từ chia thì → KHÔNG phải IC!). Nối IC với Participial Phrase bổ sung kết quả/phương thức → dùng dấu phẩy (`writings, uniting`) = B!',
            'Cụm bắt đầu bằng V-ing ("uniting...") không có động từ chia thì theo sau KHÔNG PHẢI mệnh đề độc lập → gạch sạch chấm phẩy (A), chấm câu (C), và `, and` (D)!',
            [
                ('Semicolon + Fragment', 'Vế sau "uniting..." là cụm phân từ, không phải IC → cấm dùng chấm phẩy.'),
                ('Đáp án đúng', 'Dấu phẩy nối trơn tru mệnh đề chính với cụm phân từ "uniting..." mô tả tác động của bộ ấn bản.'),
                ('Period + Fragment', 'Chấm tách "Uniting..." thành câu độc lập gây lỗi Sentence Fragment.'),
                ('False Parallelism', '", and uniting" không có dạng V-ing song song phía trước (động từ chính ở vế 1 là "launched", quá khứ đơn).'),
            ]
        ),
        q_item(
            'm5_m2h_q18', 18, 'Standard English Conventions', 'Boundaries', 'Elite (750+)',
            '<p>Freshly applied high-albedo concrete coatings significantly cool midday pavement surfaces across arid ______ because bright street surfaces bounce solar radiation onto adjacent glass storefronts, urban planners must model street-canyon geometry carefully before coating narrow commercial avenues.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['cities, however,', 'cities; however', 'cities. However', 'cities; however,'],
            'D',
            'Phân tích ranh giới 2 mệnh đề độc lập: Vế 1 là IC1 ("Freshly applied... across arid cities"). Vế 2 bắt đầu bằng mệnh đề phụ "because bright street surfaces..." đi kèm IC2 ("urban planners must model..."). Giữa 2 IC có trạng từ nối `however` → Bắt buộc công thức chuẩn: **`IC1; however, [DC,] IC2`** → `cities; however,` = D!',
            'Nhớ cấu trúc bất di bất dịch của trạng từ nối (however, therefore, moreover) giữa 2 IC: trước phải có `;` hoặc `.`, sau PHẢI có `,`!',
            [
                ('Comma Splice', 'Trạng từ nối "however" KHÔNG phải FANBOYS — đặt `, however,` giữa hai IC tạo lỗi Comma Splice kinh điển.'),
                ('Missing Comma After Adverb', 'Thiếu dấu phẩy bắt buộc ngay sau trạng từ mở đầu "however".'),
                ('Missing Comma After Adverb', 'Tách câu bằng dấu chấm hợp lệ nhưng vẫn thiếu dấu phẩy bắt buộc sau "However".'),
                ('Đáp án đúng', 'Công thức chuẩn mực `cities; however,` vừa tách gọn hai IC vừa tách trạng từ chuyển ý bằng dấu phẩy.'),
            ]
        ),
        q_item(
            'm5_m2h_q19', 19, 'Standard English Conventions', 'Boundaries', 'Elite (750+)',
            '<p>Hydrophone transects across bleached reefs in the Coral Sea yielded an unsettling acoustic ______ even two years after ocean temperatures returned to seasonal norms, snapping-shrimp crackle and damselfish dusk choruses remained barely half as loud as on neighboring unbleached reefs.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['finding:', 'finding,', 'finding', 'finding; whereas'],
            'A',
            'Vế 1 là IC hoàn chỉnh giới thiệu một phát hiện ("yielded an unsettling acoustic finding"). Vế 2 là IC hoàn chỉnh giải thích cụ thể nội dung phát hiện đó ("even two years after..., snapping-shrimp crackle and damselfish dusk choruses remained..."). IC + `:` + IC giải thích → Chọn A (`finding:`)!',
            'Khi vế 1 dừng ở danh từ hứa hẹn nội dung ("an unsettling acoustic finding") và vế 2 là câu đầy đủ diễn giải đúng nội dung ấy → Dấu hai chấm (`:`) là đáp án chuẩn nhất!',
            [
                ('Đáp án đúng', 'Dấu hai chấm (:) sau IC dẫn giải hoàn hảo mệnh đề giải thích nội dung của "an unsettling acoustic finding".'),
                ('Comma Splice', 'Chỉ dùng một dấu phẩy để nối hai mệnh đề độc lập tạo lỗi Comma Splice.'),
                ('Run-On Sentence', 'Không có bất kỳ dấu câu nào phân tách hai mệnh đề độc lập.'),
                ('Semicolon + Fragment', 'Thêm "whereas" sau chấm phẩy biến toàn bộ vế sau thành mệnh đề phụ treo lơ lửng không có mệnh đề chính.'),
            ]
        ),

        # --- Q20-Q22: Standard English Conventions — Form, Structure, and Sense (Elite 750+) ---
        q_item(
            'm5_m2h_q20', 20, 'Standard English Conventions', 'Form, Structure, and Sense', 'Elite (750+)',
            '<p>Sealed within the microscopic air pockets of East Antarctica’s oldest glacial strata ______ an unbroken chemical archive of atmospheric methane concentrations spanning eight successive ice ages.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['lie', 'have lain', 'lying', 'lies'],
            'D',
            'Bẫy Đảo Ngữ Chủ – Vị (Inverted Subject-Verb Agreement) kinh điển 750+! Toàn bộ vế đầu ("Sealed within the microscopic air pockets of East Antarctica’s oldest glacial strata") là cụm phân từ + giới từ chỉ vị trí, KHÔNG phải chủ ngữ! Chủ ngữ thật đứng SAU động từ: "<b>an unbroken chemical archive</b> [of atmospheric methane concentrations...]" → SỐ ÍT (`archive`)! Động từ chia thì số ít → `lies` (D)!',
            'Khi câu mở đầu bằng cụm giới từ/phân từ nơi chốn ("Sealed within...", "Beneath..."), lật tìm Chủ ngữ thật NẰM PHÍA SAU chỗ trống ("an unbroken chemical archive" = số ít → "lies")!',
            [
                ('Inverted S-V Mismatch', 'lie là số nhiều — bị đánh lừa bởi danh từ số nhiều "pockets / strata" ở đầu câu.'),
                ('Inverted S-V Mismatch', 'have lain là số nhiều — không khớp chủ ngữ số ít "an unbroken chemical archive".'),
                ('Non-Finite Fragment', 'lying là phân từ khiến cả câu thiếu động từ chia thì.'),
                ('Đáp án đúng', 'lies (số ít, hiện tại đơn) khớp chuẩn xác với chủ ngữ đảo đứng sau "an unbroken chemical archive".'),
            ]
        ),
        q_item(
            'm5_m2h_q21', 21, 'Standard English Conventions', 'Form, Structure, and Sense', 'Elite (750+)',
            '<p>During overcast night crossings in the central Pacific, Micronesian wayfinders detect distant coral atolls lying well below the visible horizon by sensing each refracted ______ subtle rhythmic lift beneath the canoe’s outrigger hull.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['swells’', 'swell’s', 'swells', 'swell'],
            'B',
            'Kiểm tra đồng thời Số ít/Số nhiều + Sở hữu cách (Possessive Precision): Từ hạn định `each` BẮT BUỘC đi với danh từ SỐ ÍT (`swell`, loại ngay số nhiều `swells’` và `swells`). Phía sau là danh từ sở hữu "subtle rhythmic lift" (nhịp nâng nhẹ của MỖI con sóng) → Cần sở hữu cách số ít **`swell’s`** (B)!',
            'Chốt hai bước: (1) `each` → bắt buộc số ít; (2) cần sở hữu trước "subtle rhythmic lift" → `swell’s`!',
            [
                ('Number Mismatch', 'swells’ là sở hữu cách SỐ NHIỀU — sai ngữ pháp khi đứng sau "each".'),
                ('Đáp án đúng', 'swell’s (sở hữu cách số ít) vừa khớp "each" vừa sở hữu đúng cụm danh từ "subtle rhythmic lift".'),
                ('Number & Possessive Error', 'swells là danh từ số nhiều không có dấu sở hữu — sai cả hai tiêu chí.'),
                ('Missing Possessive', 'swell thiếu dấu sở hữu ’s nên hai cụm danh từ đâm sầm vào nhau ("each refracted swell subtle rhythmic lift").'),
            ]
        ),
        q_item(
            'm5_m2h_q22', 22, 'Standard English Conventions', 'Form, Structure, and Sense', 'Elite (750+)',
            '<p>Determined to expose the grueling foundry labor she had witnessed firsthand in Wheeling, Virginia, ______</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            [
                'Rebecca Harding Davis’s groundbreaking 1861 novella <i>Life in the Iron Mills</i> jolted New England literary readers.',
                'the unsparing realism of Rebecca Harding Davis’s 1861 novella jolted New England literary readers.',
                'Rebecca Harding Davis jolted New England literary readers with her unsparing 1861 realist novella <i>Life in the Iron Mills</i>.',
                'New England literary readers were jolted by Rebecca Harding Davis’s unsparing 1861 realist novella.'
            ],
            'C',
            'Dangling Modifier + Possessive Trap kinh điển của Hard Module 2! Cụm mở đầu "Determined to expose the grueling foundry labor she had witnessed..." (Quyết tâm phơi bày lao động xưởng đúc khắc nghiệt mà BÀ đã tận mắt chứng kiến) bắt buộc chủ ngữ ngay sau dấu phẩy phải là CHÍNH CON NGƯỜI đó (`Rebecca Harding Davis`)! A là bẫy sở hữu cực hiểm: chủ ngữ thật của A là `novella` (cuốn truyện vừa), KHÔNG phải tác giả! B (chủ nghĩa hiện thực) và D (độc giả New England) đều sai chủ thể! Duy nhất C đặt thẳng `Rebecca Harding Davis` làm chủ ngữ!',
            'Cảnh giác Possessive Trap ở A: "Author’s novella" có chủ ngữ thật là "novella", KHÔNG phải "Author"! Luôn tìm tên người đứng trần không có ’s!',
            [
                ('Possessive Dangling Trap', 'Chủ ngữ thật là "novella" (cuốn truyện), không thể là người "quyết tâm phơi bày điều bà đã chứng kiến".'),
                ('Dangling Modifier', 'Chủ ngữ "the unsparing realism" không phải người chứng kiến xưởng đúc.'),
                ('Đáp án đúng', 'Chủ ngữ "Rebecca Harding Davis" đứng ngay sau dấu phẩy khớp hoàn hảo với cụm "Determined to expose... she had witnessed".'),
                ('Dangling Modifier', 'Độc giả New England không phải người quyết tâm phơi bày những gì bà chứng kiến ở Wheeling.'),
            ]
        ),

        # --- Q23-Q25: Expression of Ideas — Transitions (Elite 750+) ---
        q_item(
            'm5_m2h_q23', 23, 'Expression of Ideas', 'Transitions', 'Elite (750+)',
            '<p>Several mid-twentieth-century geographers argued that prehistoric Pacific islands must have been populated by accidental drift because indigenous navigators possessed no magnetic compasses. ______, traditional wayfinders lacked European brass instruments; nevertheless, their systematic star compasses and swell-reading techniques enabled intentional two-way voyages spanning thousands of miles.</p>',
            'Which choice completes the text with the most logical transition?',
            ['Granted', 'Instead', 'Consequently', 'By contrast'],
            'A',
            'Bẫy Concession-before-Rebuttal 750+! Đọc kỹ cả HAI nửa của Câu 2: Nửa đầu THỪA NHẬN đúng một phần dữ kiện từ Câu 1 ("traditional wayfinders lacked European brass instruments"), rồi ngay sau dấu chấm phẩy dùng "; nevertheless," để PHẢN ĐÒN (họ vẫn đi hai chiều có chủ đích hàng ngàn dặm nhờ la bàn sao và kỹ thuật đọc sóng)! Do đó từ nối đầu Câu 2 phải mang nghĩa NHƯỢNG BỘ ("Phải thừa nhận rằng...") → **`Granted`** (A)!',
            'Mỗi khi thấy cấu trúc `______, [thừa nhận một phần ý câu 1]; nevertheless/however, [phản biện chính]` → chốt ngay từ nối nhượng bộ (`Granted` / `Admittedly`)!',
            [
                ('Đáp án đúng', 'Granted (Phải thừa nhận rằng) mở màn hoàn hảo cho vế nhượng bộ ngay trước cú phản đòn "; nevertheless,".'),
                ('Wrong Relationship (Replacement)', 'Instead báo hiệu hành động thay thế trái ngược, nhưng vế ngay sau chỗ trống lại ĐỒNG Ý rằng họ thiếu dụng cụ đồng châu Âu.'),
                ('Wrong Relationship (Cause-Effect)', 'Việc thiếu dụng cụ đồng châu Âu không phải hệ quả sinh ra từ lập luận của các nhà địa lý thế kỷ 20.'),
                ('False Contrast Trap', 'Đặt "By contrast" ngay trước một mệnh đề ĐỒNG TÌNH ("lacked instruments") và trước "; nevertheless," sẽ gây đảo chiều kép sai logic!'),
            ]
        ),
        q_item(
            'm5_m2h_q24', 24, 'Expression of Ideas', 'Transitions', 'Elite (750+)',
            '<p>Reconstructing prehistoric climate shifts from Antarctic ice requires glaciologists to cross-check multiple independent chemical proxies preserved at the same depth. ______, ratios of heavy oxygen-18 to lighter oxygen-16 atoms within the frozen crystals record ancient surface temperatures, while microscopic air bubbles trapped beside them preserve direct samples of prehistoric carbon dioxide and methane.</p>',
            'Which choice completes the text with the most logical transition?',
            ['Nevertheless', 'Meanwhile', 'Specifically', 'Therefore'],
            'C',
            'Câu 1 đưa khái niệm tổng quát ("multiple independent chemical proxies"). Câu 2 GIẢI THÍCH CỤ THỂ đích danh hai chỉ dấu hóa học đó là gì (tỷ lệ đồng vị oxy-18/oxy-16 đo nhiệt độ + bọt khí lưu mẫu CO₂/CH₄) → Quan hệ Tổng quát → Cụ thể hóa (Specification) → **`Specifically`** (C)!',
            'Tổng quát ("multiple independent proxies") → Liệt kê đích danh từng loại chi tiết = `Specifically`!',
            [
                ('False Contrast', 'Câu 2 làm rõ cho câu 1 chứ không hề mâu thuẫn.'),
                ('Wrong Relationship (Time)', 'Meanwhile chỉ hai sự kiện diễn ra đồng thời, không diễn đạt mối quan hệ cụ thể hóa khái niệm.'),
                ('Đáp án đúng', 'Specifically chuyển tiếp sắc nét từ khái niệm chung "multiple chemical proxies" sang hai ví dụ hóa học cụ thể.'),
                ('Wrong Relationship (Cause-Effect)', 'Tỷ lệ đồng vị oxy không phải hệ quả do việc nhà băng học đối chiếu sinh ra.'),
            ]
        ),
        q_item(
            'm5_m2h_q25', 25, 'Expression of Ideas', 'Transitions', 'Elite (750+)',
            '<p>When designing his landmark pocket editions of Greek and Roman classics in 1501, Aldus Manutius did not simply shrink the sprawling, dense Gothic letterforms then standard across northern European workshops. ______, he commissioned a narrow, gently slanted italic typeface modeled on humanist cursive handwriting, allowing dense verse to remain legible inside volumes small enough for a coat pocket.</p>',
            'Which choice completes the text with the most logical transition?',
            ['Furthermore', 'Accordingly', 'Still', 'Instead'],
            'D',
            'Câu 1 có phủ định rất rõ ("did NOT simply shrink the sprawling... Gothic letterforms"). Câu 2 nêu giải pháp THAY THẾ hoàn toàn khác ("he commissioned a narrow, gently slanted italic typeface...") → Phủ định phương án X, chọn phương án Y thay thế → **`Instead`** (D)!',
            'Cảnh giác bẫy `Still` (Still = Nevertheless, dùng cho trái kỳ vọng, KHÔNG dùng thay cho `Instead` sau cấu trúc "did not simply X")!',
            [
                ('Wrong Relationship (Addition)', 'Furthermore dùng để cộng thêm ý cùng chiều, không dùng sau mệnh đề phủ định để nêu giải pháp thay thế.'),
                ('Wrong Relationship (Cause-Effect)', 'Việc không thu nhỏ chữ Gothic không tự động kéo theo hệ quả tất yếu phải dùng chữ viết tay nghiêng.'),
                ('Contrast Nuance Trap', 'Still (= bất chấp vậy) không diễn đạt hành động thay thế trực tiếp sau "did not simply...".'),
                ('Đáp án đúng', 'Instead khớp tuyệt đối mô hình phủ định X → chọn giải pháp thiết kế Y thay thế.'),
            ]
        ),

        # --- Q26-Q27: Expression of Ideas — Rhetorical Synthesis (Hard / Elite 750+) ---
        q_item(
            'm5_m2h_q26', 26, 'Expression of Ideas', 'Rhetorical Synthesis', 'Hard',
            '''<p>While researching deep-sea hydrothermal systems, a student has taken the following notes:</p>
            <ul>
              <li>Conventional “black smoker” hydrothermal vents form directly over volcanic magma chambers, discharging intensely acidic, 380°C fluids that precipitate iron-sulfide chimneys.</li>
              <li>Because volcanic magma pulses shift quickly, individual black-smoker chimneys typically remain active for only a few decades before collapsing.</li>
              <li>Discovered in 2000 along the Mid-Atlantic Ridge, the Lost City hydrothermal field is driven instead by slow chemical reactions between seawater and exposed mantle rock.</li>
              <li>Lost City vents release cooler (roughly 75°C), highly alkaline (pH 9–11) fluids that build pale calcium-carbonate towers up to 60 meters tall.</li>
              <li>Radiometric dating confirms that Lost City’s carbonate vents have remained continuously active for more than 30,000 years.</li>
            </ul>''',
            'The student wants to contrast both the fluid chemistry and the operational longevity of Lost City hydrothermal vents with those of conventional black smokers. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
            [
                'Discovered along the Mid-Atlantic Ridge in 2000, the Lost City hydrothermal field features pale calcium-carbonate towers reaching up to 60 meters tall.',
                'Whereas conventional black smokers emit intensely acidic, 380°C fluids from iron-sulfide chimneys that usually collapse within decades, Lost City vents release cooler, alkaline fluids from carbonate towers that have stayed active for over 30,000 years.',
                'Unlike conventional black smokers heated directly by magma chambers, Lost City vents are powered by chemical reactions between seawater and exposed mantle rock.',
                'Lost City’s alkaline vents have remained continuously active for more than 30,000 years, far outlasting conventional black-smoker chimneys.'
            ],
            'B',
            'Goal-First SOP: Đối chiếu ĐỒNG THỜI CẢ HAI TIÊU CHÍ: [1] Hóa học dòng lưu chất (fluid chemistry: acidic 380°C vs. cooler alkaline pH 9–11) VÀ [2] Tuổi thọ hoạt động (operational longevity: collapse within decades vs. active >30,000 years) giữa Lost City và Black Smokers. A chỉ nói chiều cao tháp; C chỉ đối chiếu nguồn nhiệt (magma vs. mantle rock); D chỉ đối chiếu tuổi thọ mà bỏ quên hóa học lưu chất (Half-Match!). Duy nhất B ghép đủ cả hai tiêu chí trong một câu đối xứng sắc nét! Chọn B!',
            'Gặp chữ "both X and Y" trong Goal → gạch thẳng mọi đáp án chỉ đạt 1 tiêu chí như C hoặc D!',
            [
                ('Wrong Synthesis Goal', 'Chỉ mô tả năm phát hiện và chiều cao tháp của Lost City, thiếu hẳn sự so sánh với black smokers.'),
                ('Đáp án đúng', 'Đối chiếu trọn vẹn cả hóa học lưu chất (acidic 380°C vs. cooler alkaline) lẫn tuổi thọ hoạt động (decades vs. >30,000 years).'),
                ('Wrong Criterion', 'Chỉ so sánh cơ chế gia nhiệt (magma vs. đá manti), thiếu cả hóa học lưu chất lẫn tuổi thọ.'),
                ('Half-Match Trap', 'Chỉ đối chiếu tuổi thọ (>30,000 years vs. black smokers) mà bỏ sót hoàn toàn tiêu chí hóa học lưu chất (fluid chemistry).'),
            ]
        ),
        q_item(
            'm5_m2h_q27', 27, 'Expression of Ideas', 'Rhetorical Synthesis', 'Elite (750+)',
            '''<p>While researching urban heat-island mitigation, a student has taken the following notes:</p>
            <ul>
              <li>Field trials in Athens and Phoenix show that high-albedo reflective pavement coatings reduce midday asphalt surface temperatures by up to 6°C and trim nighttime urban air temperatures by roughly 1.2°C.</li>
              <li>However, on unshaded sunlit plazas, upward shortwave glare from bright coatings can raise midday radiant heat load on pedestrians by up to 3°C.</li>
              <li>Applying the same reflective coatings to elevated rooftops, parking decks, and tree-shaded avenues avoids pedestrian glare while retaining neighborhood-scale heat reductions.</li>
              <li>Urban climatologists therefore discourage blanket citywide paving mandates in favor of site-specific deployment.</li>
            </ul>''',
            'The student wants to recommend a targeted urban-planning approach that captures the cooling advantages of reflective coatings while avoiding their main drawback for pedestrians. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
            [
                'Rather than mandating reflective coatings across unshaded plazas where upward glare adds up to 3°C of radiant heat to pedestrians, cities can preserve surface and nighttime cooling gains by targeting rooftops, parking decks, and tree-shaded corridors.',
                'Field trials in Athens and Phoenix demonstrated that high-albedo reflective coatings cut midday asphalt temperatures by up to 6°C and nighttime air temperatures by 1.2°C.',
                'Because upward shortwave glare from bright coatings increases midday pedestrian radiant heat by up to 3°C on unshaded plazas, urban climatologists warn against reflective street sealants.',
                'Urban climatologists studied high-albedo coatings in Athens and Phoenix and concluded that site-specific urban-planning strategies outperform blanket mandates.'
            ],
            'A',
            'Goal-First SOP: Đề xuất một CHIẾN LƯỢC QUY HOẠCH CÓ TRỌNG ĐIỂM (targeted approach) đáp ứng đủ 3 vế: [1] Giữ được lợi ích làm mát (cooling advantages); [2] Tránh nhược điểm chính với người đi bộ (upward glare / radiant heat trên quảng trường không bóng); [3] Nêu rõ giải pháp mục tiêu (rooftops, parking decks, tree-shaded corridors). B chỉ nêu mặt tốt; C chỉ nêu mặt xấu; D nói chung chung "site-specific" mà không hề nhắc đến cả lợi ích làm mát, nhược điểm cho người đi bộ, lẫn địa điểm áp dụng cụ thể! Duy nhất A kết tinh trọn vẹn chiến lược! Chọn A!',
            'Trong Rhetorical Synthesis 750+, đáp án quá chung chung (như D thiếu chi tiết cụ thể từ notes) luôn thua đáp án gom trọn đích danh giải pháp + lợi ích + cách né tác dụng phụ (A)!',
            [
                ('Đáp án đúng', 'Khớp hoàn hảo cả 3 yêu cầu của Goal: né quảng trường nắng gắt gây chói nhiệt (+3°C), giữ lợi ích hạ nhiệt, và chỉ đích danh 3 khu vực áp dụng hiệu quả.'),
                ('Half-Match Trap (Benefits Only)', 'Chỉ nêu kết quả hạ nhiệt, bỏ qua hoàn toàn nhược điểm người đi bộ và giải pháp quy hoạch có trọng điểm.'),
                ('Half-Match Trap (Drawback Only)', 'Chỉ cảnh báo tác hại chói nhiệt mà không đưa ra chiến lược tận dụng lợi ích làm mát.'),
                ('Too Vague / Missing Details', 'Nói chung chung "site-specific strategies" mà không nêu rõ cách né tác dụng phụ người đi bộ hay địa điểm áp dụng cụ thể.'),
            ]
        ),
    ]
