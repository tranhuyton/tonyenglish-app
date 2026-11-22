# -*- coding: utf-8 -*-
"""
Hand-crafted 1500+ Elite Digital SAT R&W Skill Drills:
- Drill 3.1: Transitions — High-Level Logical Connectors (14 Qs)
- Drill 3.2: Rhetorical Synthesis — Goal-First Mastery (14 Qs)
"""

from sat_drills_1_1_and_2_1 import q_item

STEM_TRANS = 'Which choice completes the text with the most logical transition?'

def get_drill_3_1():
    questions = [
        q_item(
            'd3_1_q1', 1, 'Expression of Ideas', 'Transitions', 'Medium',
            '<p>In 2019, oceanographers deployed autonomous drifting floats equipped with biogeochemical sensors across the Southern Ocean. ______, the fleet transmitted continuous vertical profiles of oxygen, nitrate, and chlorophyll levels even through winter months when ice prevents research vessels from entering the region.</p>',
            STEM_TRANS,
            ['Consequently', 'Nevertheless', 'By contrast', 'Instead'],
            'A',
            'Câu 1: Hải dương học thả các phao tự hành gắn cảm biến. Câu 2: KẾT QUẢ là đội phao truyền về dữ liệu liên tục ngay cả mùa đông khi tàu nghiên cứu không vào được → Quan hệ Nhân – Quả → "Consequently".',
            'Kiểm tra xem câu 2 có phải là hệ quả trực tiếp của hành động ở câu 1 hay không (thả phao → thu được dữ liệu mùa đông).',
            [
                ('Đáp án đúng', 'Consequently diễn đạt chính xác quan hệ nhân – quả giữa việc triển khai phao tự hành và kết quả thu được dữ liệu mùa đông.'),
                ('False Contrast', 'Nevertheless chỉ sự trái kỳ vọng — việc phao truyền dữ liệu hoàn toàn đúng mục tiêu triển khai.'),
                ('False Contrast', 'By contrast dùng để đối chiếu hai đối tượng ngược chiều.'),
                ('Substitution Trap', 'Instead chỉ dùng khi câu 1 nêu hành động bị từ chối/phủ định.'),
            ]
        ),
        q_item(
            'd3_1_q2', 2, 'Expression of Ideas', 'Transitions', 'Hard',
            '<p>Unlike deciduous trees that drop all their foliage before winter, bristlecone pines in Nevada’s White Mountains retain individual needles for up to forty-five years. ______, they conserve scarce nutrients and energy during short, frigid alpine growing seasons.</p>',
            STEM_TRANS,
            ['However', 'In doing so', 'Conversely', 'Nonetheless'],
            'B',
            'Câu 1 nêu hành động giữ lá kim tới 45 năm. Câu 2 nêu lợi ích xảy ra NHỜ HÀNH ĐỘNG ĐÓ ("bằng việc làm như vậy, chúng tiết kiệm được dinh dưỡng và năng lượng") → "In doing so" (B). Dùng Synonym Shortcut: A, C, D đều thuộc nhóm Đối lập → loại sạch 3 đáp án đối lập trong 3 giây!',
            'Mẹo 3–1 cực mạnh cho Transitions: 3 từ cùng họ Đối lập (However / Conversely / Nonetheless) + 1 từ chỉ kết quả từ hành động ("In doing so") → chốt ngay!',
            [
                ('False Contrast', 'However mang nghĩa đối lập — sai vì câu 2 nêu lợi ích trực tiếp của câu 1.'),
                ('Đáp án đúng', 'In doing so nối mượt hành động giữ lá lâu với hệ quả tiết kiệm năng lượng ngay nhờ hành động đó.'),
                ('False Contrast', 'Conversely chỉ sự đảo ngược/đối nghịch.'),
                ('False Contrast', 'Nonetheless chỉ sự nhượng bộ trái kỳ vọng.'),
            ]
        ),
        q_item(
            'd3_1_q3', 3, 'Expression of Ideas', 'Transitions', 'Hard',
            '<p>Traditional lithium extraction from South American salt flats evaporates millions of liters of brine in open ponds over eighteen months. Direct lithium extraction (DLE) systems, ______, pump brine through selective mineral sieves and reinject the depleted water underground within hours.</p>',
            STEM_TRANS,
            ['similarly', 'therefore', 'by contrast', 'for instance'],
            'C',
            'Nhấc chỗ trống lên đầu câu 2: So sánh 2 đối tượng ĐỐI NGHỊCH NHAU (Traditional extraction mất 18 tháng làm bay hơi nước vs. DLE Systems xử lý trong vài giờ và bơm hoàn trả nước xuống đất) → So sánh 2 đối tượng ngược chiều = "by contrast" (C)!',
            'So sánh Đối tượng X với Đối tượng Y đi theo hai hướng trái ngược → chọn "by contrast" hoặc "conversely"!',
            [
                ('Opposite Relationship', 'similarly chỉ sự giống nhau — hai phương pháp hoàn toàn trái ngược về thời gian và cách xử lý nước.'),
                ('Wrong Relationship (Cause-Effect)', 'DLE không phải là kết quả tự động sinh ra từ phương pháp truyền thống.'),
                ('Đáp án đúng', 'by contrast đối chiếu chuẩn xác phương pháp chiết xuất truyền thống với công nghệ DLE hiện đại.'),
                ('Wrong Relationship (Example)', 'DLE không phải là một ví dụ minh họa cho phương pháp bay hơi truyền thống.'),
            ]
        ),
        q_item(
            'd3_1_q4', 4, 'Expression of Ideas', 'Transitions', 'Elite (750+)',
            '<p>Early twentieth-century urban planners did not integrate natural floodplains into municipal drainage designs. ______, they encased urban creeks inside rigid concrete culverts designed to rush rainwater out of city centers as rapidly as possible.</p>',
            STEM_TRANS,
            ['Nevertheless', 'Meanwhile', 'Moreover', 'Instead'],
            'D',
            'CẶP SÁT THỦ HARD MODULE 2 (`Instead` vs. `Nevertheless`)! Câu 1 chứa PHỦ ĐỊNH RÕ RỆT ("did NOT integrate natural floodplains"). Câu 2 nêu PHƯƠNG ÁN THAY THẾ mà họ thực sự đã làm ("encased urban creeks inside rigid concrete culverts"). Phủ định X → làm Y thay thế = "Instead" (D)!',
            'Nhìn thấy "did not / never / rather than" ở câu 1 + hành động thay thế ở câu 2 → chọn "Instead" (Thay vào đó)!',
            [
                ('Contrast Nuance Trap', 'Nevertheless nghĩa là "bất chấp X, Y vẫn xảy ra" — không diễn đạt sự thay thế trực tiếp sau câu phủ định "did not X".'),
                ('Wrong Relationship (Time)', 'Meanwhile chỉ hai việc diễn ra song song cùng lúc bởi hai chủ thể khác nhau.'),
                ('Wrong Relationship (Addition)', 'Moreover dùng để bổ sung thêm ý cùng chiều.'),
                ('Đáp án đúng', 'Instead khớp tuyệt đối cấu trúc phủ định X ("did not integrate") → thay thế bằng hành động Y ("encased inside concrete culverts").'),
            ]
        ),
        q_item(
            'd3_1_q5', 5, 'Expression of Ideas', 'Transitions', 'Elite (750+)',
            '<p>Historians once assumed that the Bronze Age Indus Valley civilization maintained stability through a centralized monarchy backed by monumental palaces and standing armies. ______, decades of excavations at Mohenjo-daro and Harappa have uncovered standardized brick drains, uniform weights, and civic granaries—yet not a single identifiable royal palace or dynastic tomb.</p>',
            STEM_TRANS,
            ['In fact', 'In reality', 'Accordingly', 'Furthermore'],
            'B',
            'Câu 1 nêu giả định CŨ SAI LẦM ("Historians once assumed... centralized monarchy"). Câu 2 đưa bằng chứng khai quật PHƠI BÀY SỰ THẬT NGƯỢC LẠI ("yet not a single identifiable royal palace"). Chọn "In reality" (B)! Cẩn thận bẫy A ("In fact"): trên Digital SAT, "In fact" dùng để CỦNG CỐ CÙNG CHIỀU, KHÔNG dùng để lật ngược giả định sai!',
            'Phân biệt sống còn trên SAT: "In fact / Indeed" = CỦNG CỐ CÙNG CHIỀU; "In reality / Actually / However" = LẬT NGƯỢC GIẢ ĐỊNH SAI!',
            [
                ('In Fact Trap', 'Trên Digital SAT, "In fact" chỉ dùng để nhấn mạnh/đẩy mạnh ý CÙNG CHIỀU câu trước, không dùng để bác bỏ giả định cũ.'),
                ('Đáp án đúng', 'In reality lật ngược chính xác giả định cũ ("once assumed") bằng bằng chứng khảo cổ thực tế.'),
                ('Wrong Relationship (Cause-Effect)', 'Accordingly = do đó, sai hoàn toàn hướng đối lập.'),
                ('Wrong Relationship (Addition)', 'Furthermore dùng để thêm luận điểm cùng chiều.'),
            ]
        ),
        q_item(
            'd3_1_q6', 6, 'Expression of Ideas', 'Transitions', 'Elite (750+)',
            '<p>Biologist Dr. Amara Osei demonstrated that African giant pouched rats possess an extraordinary capacity for detecting volatile organic compounds. ______, trained rats in Tanzania can screen one hundred human sputum samples for tuberculosis in under twenty minutes—a volume that takes a lab technician four full days to examine by microscope.</p>',
            STEM_TRANS,
            ['In other words', 'Specifically', 'Regardless', 'Conversely'],
            'B',
            'CẶP SÁT THỦ (`Specifically` vs. `In other words`)! Câu 1 nói TỔNG QUÁT ("extraordinary capacity for detecting volatile organic compounds"). Câu 2 thu hẹp xuống MỘT VÍ DỤ ĐỊNH LƯỢNG CỤ THỂ (chuột ở Tanzania sàng lọc 100 mẫu bệnh phẩm lao trong dưới 20 phút) → Tổng quát → Cụ thể = "Specifically" (B)!',
            'Tổng quát → Ví dụ/Con số cụ thể: chọn "Specifically / For example / For instance". Chỉ chọn "In other words" khi hai câu cùng cấp độ nghĩa, chỉ đổi cách diễn đạt!',
            [
                ('Restatement Trap', 'In other words chỉ dùng để giải thích lại cùng 1 khái niệm, không dùng để chuyển từ năng lực tổng quát sang ví dụ cụ thể tại Tanzania.'),
                ('Đáp án đúng', 'Specifically chuyển mạch mượt mà từ nhận định khái quát sang trường hợp minh họa định lượng cụ thể.'),
                ('False Contrast', 'Regardless mang nghĩa bất chấp, sai hướng logic.'),
                ('False Contrast', 'Conversely chỉ sự trái ngược.'),
            ]
        ),
        q_item(
            'd3_1_q7', 7, 'Expression of Ideas', 'Transitions', 'Hard',
            '<p>The acoustic design of the ancient Greek theater at Epidaurus relies heavily on limestone seating rows whose corrugated surfaces filter out low-frequency background wind and crowd murmur. ______, the stepped geometry amplifies high-frequency vocal harmonics, allowing unamplified whispers on stage to reach the top row sixty meters away.</p>',
            STEM_TRANS,
            ['Furthermore', 'Instead', 'Nevertheless', 'As a result'],
            'A',
            'Câu 1 nêu cơ chế âm học 1 (lọc tạp âm tần số thấp). Câu 2 bổ sung cơ chế âm học 2 ĐỘC LẬP cùng giúp tăng độ rõ âm thanh (khuếch đại họa âm giọng nói tần số cao) → Bổ sung thêm yếu tố mới cùng chiều → "Furthermore" (A)!',
            'Cơ chế 1 + Cơ chế 2 cùng hướng (chứ cơ chế 1 không GÂY RA cơ chế 2) → chọn "Furthermore / Moreover", loại "As a result"!',
            [
                ('Đáp án đúng', 'Furthermore bổ sung chính xác cơ chế âm học thứ hai độc lập cùng cải thiện độ rõ của âm thanh.'),
                ('Substitution Trap', 'Không có phủ định nào ở câu 1 để thay thế bằng "Instead".'),
                ('False Contrast', 'Hai cơ chế bổ trợ cùng chiều chứ không đối lập.'),
                ('False Causation', 'Việc lọc gió tần số thấp không phải nguyên nhân tạo ra cấu trúc bậc thang khuếch đại giọng nói.'),
            ]
        ),
        q_item(
            'd3_1_q8', 8, 'Expression of Ideas', 'Transitions', 'Elite (750+)',
            '<p>When constructing wooden bridges without iron nails, Song Dynasty master carpenters relied on interlocking beam weaves that appeared remarkably simple from below. ______, the structural load calculations required to balance friction and compression across every timber joint were extraordinarily sophisticated.</p>',
            STEM_TRANS,
            ['In addition', 'Indeed', 'Even so', 'Thus'],
            'C',
            'Câu 1: Nhìn từ dưới lên trông cực kỳ đơn giản ("appeared remarkably simple"). Câu 2: Trái ngược vẻ ngoài đó, tính toán chịu lực bên trong cực kỳ tinh vi ("extraordinarily sophisticated") → Đối lập / Bất chấp vẻ ngoài đơn giản → "Even so" (Dù vậy / Tuy nhiên) = C!',
            '"Even so" và "Still" là hai từ nối đối lập gọn nhẹ rất hay xuất hiện ở Hard Module 2 thay cho "However"!',
            [
                ('Wrong Relationship (Addition)', 'In addition là bổ sung cùng chiều — sai với cặp tương phản "simple" vs. "sophisticated".'),
                ('Emphasis Trap', 'Indeed nhấn mạnh cùng chiều câu trước.'),
                ('Đáp án đúng', 'Even so diễn đạt chính xác sự tương phản giữa vẻ ngoài đơn giản và kỹ thuật chịu lực phức tạp bên trong.'),
                ('Wrong Relationship (Cause-Effect)', 'Thus chỉ hệ quả — vẻ ngoài đơn giản không gây ra tính toán phức tạp.'),
            ]
        ),
        q_item(
            'd3_1_q9', 9, 'Expression of Ideas', 'Transitions', 'Elite (750+)',
            '<p>Not only did the 1815 eruption of Mount Tambora inject massive plumes of sulfate aerosols into the stratosphere, cooling global temperatures for over a year, it also disrupted monsoon circulation across Asia. ______, the volcanic blast triggered cascading crop failures across hemispheres so severe that 1816 became known in Europe and North America as the "Year Without a Summer."</p>',
            STEM_TRANS,
            ['Indeed', 'By contrast', 'Otherwise', 'Previously'],
            'A',
            'Câu 1 nói vụ phun trào làm lạnh toàn cầu và phá vỡ gió mùa. Câu 2 ĐẨY MẠNH / NHẤN SÂU THÊM CHÍNH TẦM VÓC NGHIÊM TRỌNG ĐÓ ("triggered cascading crop failures... so severe that 1816 became known as the Year Without a Summer") → Đẩy mạnh cùng 1 luận điểm = "Indeed" (A)!',
            'Khi câu 2 chứng minh sâu hơn/kịch tính hơn cho đúng quy mô vừa nêu ở câu 1 (không phải đối lập, không phải ví dụ nhỏ lẻ) → "Indeed"!',
            [
                ('Đáp án đúng', 'Indeed nhấn mạnh và mở rộng sâu thêm hệ lụy nghiêm trọng toàn cầu của vụ phun trào vừa nêu ở câu 1.'),
                ('False Contrast', 'By contrast dùng cho đối chiếu ngược chiều.'),
                ('Wrong Relationship (Condition)', 'Otherwise = nếu không thì (chỉ giả định trái ngược).'),
                ('Wrong Relationship (Time)', '1816 xảy ra SAU năm 1815, không phải "Previously" (trước đó).'),
            ]
        ),
        q_item(
            'd3_1_q10', 10, 'Expression of Ideas', 'Transitions', 'Hard',
            '<p>In 1974, paleoanthropologist Donald Johanson unearthed a remarkably complete 3.2-million-year-old <i>Australopithecus afarensis</i> skeleton in Ethiopia’s Afar region. ______, teams working at Laetoli in Tanzania uncovered fossilized footprints preserved in volcanic ash that corroborated the species’ habitual bipedal locomotion.</p>',
            STEM_TRANS,
            ['Subsequently', 'For example', 'On the contrary', 'In summary'],
            'A',
            'Câu 1: Năm 1974 khai quật hóa thạch tại Ethiopia. Câu 2: Sau đó (vào cuối thập niên 1970 tại Laetoli, Tanzania), các nhóm nghiên cứu phát hiện dấu chân hóa thạch củng cố thêm bằng chứng đi bằng hai chân → Quan hệ Trình tự thời gian (Sequence) → "Subsequently" (Sau đó) = A! (Wait: let\'s make sure the timing cue is unmistakable by adding "Four years later" or keeping 1978? Even cleaner: "In 1978," wouldn\'t pair with "Subsequently" redundantly; adding "At a later excavation in Tanzania" or "Within a few years,"? No, "teams working at Laetoli... uncovered" clearly happened after 1974 and corroborated the 1974 discovery, while B/C/D are 100% logically impossible: footprints in Tanzania aren\'t an "example" of Johanson\'s excavation, aren\'t "on the contrary", and aren\'t a "summary"!)',
            'Khi 3 đáp án còn lại sai hoàn toàn quan hệ logic (Example / Contrast / Summary), trình tự tiến triển nghiên cứu ("Subsequently") nổi bật ngay!',
            [
                ('Đáp án đúng', 'Subsequently diễn đạt mạch thời gian tiếp nối giữa phát hiện năm 1974 ở Ethiopia và phát hiện củng cố sau đó ở Tanzania.'),
                ('Wrong Relationship (Example)', 'Phát hiện dấu chân ở Tanzania không phải là ví dụ con của bộ xương Johanson tìm thấy ở Ethiopia.'),
                ('False Contrast', 'Phát hiện dấu chân củng cố (corroborated) chứ không trái ngược (on the contrary).'),
                ('Wrong Relationship (Summary)', 'Câu 2 đưa thêm sự kiện mới chứ không tóm tắt câu 1.'),
            ]
        ),
        q_item(
            'd3_1_q11', 11, 'Expression of Ideas', 'Transitions', 'Elite (750+)',
            '<p>Most deep-sea hydrothermal vent organisms rely on chemosynthetic bacteria rather than sunlight for primary energy. ______, shallow-water coral reefs depend directly on photosynthetic dinoflagellates that convert solar radiation into sugars.</p>',
            STEM_TRANS,
            ['Likewise', 'Accordingly', 'In other words', 'Conversely'],
            'D',
            'Câu 1: Sinh vật khe nứt thủy nhiệt đáy sâu dựa vào vi khuẩn hóa tổng hợp (KHÔNG dùng ánh sáng). Câu 2: Rạn san hô nước nông lại phụ thuộc trực tiếp vào quang hợp ánh sáng mặt trời → Đối chiếu 2 hệ sinh thái NGƯỢC CHIỀU ĐỐI XỨNG → "Conversely" (Ngược lại) = D!',
            'Đối tượng 1 làm A (không dùng nắng) vs. Đối tượng 2 làm ngược lại (dùng nắng) → "Conversely / By contrast"!',
            [
                ('Opposite Relationship', 'Likewise = tương tự như vậy — trái ngược hoàn toàn hai cơ chế hóa tổng hợp và quang hợp.'),
                ('Wrong Relationship (Cause-Effect)', 'Rạn san hô quang hợp không phải hệ quả của vi khuẩn đáy sâu.'),
                ('Restatement Trap', 'Câu 2 nói về hệ sinh thái khác hoàn toàn chứ không diễn đạt lại câu 1.'),
                ('Đáp án đúng', 'Conversely đối chiếu chính xác hai cơ chế năng lượng trái ngược giữa sinh vật đáy sâu và san hô nước nông.'),
            ]
        ),
        q_item(
            'd3_1_q12', 12, 'Expression of Ideas', 'Transitions', 'Elite (750+)',
            '<p>Seismologists monitoring Kīlauea volcano can now detect harmonic tremors days before lava breaches surface fissures. ______, pinpointing the exact hour and vent location of an impending eruption remains frustratingly elusive because underground magma pathways fracture unpredictably.</p>',
            STEM_TRANS,
            ['Granted', 'Still', 'Therefore', 'Similarly'],
            'B',
            'Câu 1: Tiến bộ tích cực (phát hiện rung chấn trước nhiều ngày). Câu 2: Hạn chế đối lập bất chấp tiến bộ đó (vẫn rất khó dự đoán đúng giờ và vị trí miệng phun). Chọn "Still" (Tuy nhiên / Dù vậy) = B! Chú ý bẫy A ("Granted" = Phải thừa nhận rằng — thường dùng khi thừa nhận điểm mạnh của ĐỐI PHƯƠNG ở câu đầu tiên trước khi phản công ở câu sau, không dùng để nối Tiến bộ → Hạn chế bằng giọng bất ngờ).',
            '"Still" ở đầu câu = "Nevertheless / However" — cực phổ biến ở Hard Module 2 Digital SAT!',
            [
                ('Concession Direction Trap', 'Granted (= Admittedly) dùng để nhượng bộ 1 điểm trước khi bác bỏ nó ở vế sau, không khớp mạch chuyển Tiến bộ → Tuy nhiên vẫn còn hạn chế lớn.'),
                ('Đáp án đúng', 'Still (= Nevertheless) diễn đạt sắc nét sự đối lập giữa khả năng phát hiện sớm và giới hạn chưa thể định vị chính xác.'),
                ('Wrong Relationship (Cause-Effect)', 'Khả năng phát hiện sớm không phải nguyên nhân khiến việc định vị trở nên khó khăn.'),
                ('Opposite Relationship', 'Similarly sai vì hai vế đi theo hai hướng trái ngược (thành công vs. hạn chế).'),
            ]
        ),
        q_item(
            'd3_1_q13', 13, 'Expression of Ideas', 'Transitions', 'Elite (750+)',
            '<p>Critics initially dismissed director Yasujirō Ozu’s rigid low-angle "tatami shot" camera placement as overly austere and repetitive. ______, film scholars today celebrate that very restraint as a visual grammar that invites viewers into quiet contemplation of ordinary family life.</p>',
            STEM_TRANS,
            ['Today', 'Fittingly', 'However', 'For instance'],
            'C',
            'Câu 1: Ban đầu giới phê bình chê bai kỹ thuật quay góc thấp là khô khan lặp lại ("initially dismissed"). Câu 2: Ngày nay học giả lại ca ngợi chính sự tiết chế đó ("celebrate that very restraint"). Chú ý: Câu 2 ĐÃ CÓ SẴN chữ "today" bên trong ("film scholars today") → loại ngay bẫy lặp chữ A ("Today")! Chọn "However" (C)!',
            'Luôn quét xem trong câu 2 đã có trạng từ thời gian ("today", "later") chưa để không dính bẫy lặp chữ như "Today, film scholars today..."!',
            [
                ('Redundancy Trap', 'Câu 2 đã có sẵn từ "today" ("film scholars today"), đặt "Today," ở đầu vừa lặp từ vừa mất quan hệ tương phản.'),
                ('Wrong Tone', 'Fittingly = một cách thích đáng/phù hợp — sai vì nhận định ngày nay đảo ngược nhận định ban đầu.'),
                ('Đáp án đúng', 'However đánh dấu chính xác bước ngoặt tương phản giữa sự chê bai ban đầu và sự tán dương ngày nay.'),
                ('Wrong Relationship (Example)', 'Sự ca ngợi ngày nay không phải ví dụ minh họa cho sự chê bai ban đầu.'),
            ]
        ),
        q_item(
            'd3_1_q14', 14, 'Expression of Ideas', 'Transitions', 'Elite (750+)',
            '<p>In high-density coastal aquaculture, densely packed salmon pens frequently suffer outbreaks of parasitic sea lice that require costly chemical treatments. ______, integrated multitrophic aquaculture pairs fish cages with surrounding kelp lines and mussel beds that naturally filter organic waste and improve water quality.</p>',
            STEM_TRANS,
            ['Consequently', 'In this way', 'In response', 'Likewise'],
            'C',
            'Câu 1 nêu một VẤN ĐỀ nghiêm trọng (mật độ nuôi dày đặc gây bùng phát rận biển và tốn hóa chất). Câu 2 đưa ra MỘT GIẢI PHÁP ĐƯỢC TẠO RA ĐỂ ĐỐI PHÓ VỚI VẤN ĐỀ ĐÓ (nuôi trồng đa dinh dưỡng tích hợp tảo bẹ và vẹm để lọc nước tự nhiên) → Vấn đề → Giải pháp đối phó = "In response" (C)! Cẩn thận bẫy A ("Consequently"): rận biển không tự sinh ra mô hình tảo bẹ — con người phát triển mô hình đó ĐỂ ỨNG PHÓ ("In response")!',
            'Phân biệt tinh tế 750+: Hiện tượng A tự gây ra hậu quả B → "Consequently"; Vấn đề A khiến con người/ngành thiết kế giải pháp B → "In response"!',
            [
                ('Automatic Causation Trap', 'Consequently gợi ý mô hình nuôi tảo-vẹm tự động xảy ra như hậu quả vật lý của rận biển, thiếu sắc thái chủ động giải quyết vấn đề.'),
                ('Wrong Reference', 'In this way = bằng cách này — câu 1 mô tả vấn đề xấu chứ không mô tả cách làm dẫn tới lọc nước tự nhiên.'),
                ('Đáp án đúng', 'In response nối hoàn hảo giữa vấn đề môi trường ở câu 1 và giải pháp nuôi trồng tích hợp nhằm ứng phó ở câu 2.'),
                ('Opposite Relationship', 'Likewise chỉ sự tương đồng, sai vì câu 2 đưa giải pháp khắc phục câu 1.'),
            ]
        ),
    ]

    # Balance A/B/C/D nicely: currently A:4, B:4, C:4, D:2 -> rotate Q7 (A->D) for 3/4/4/3!
    questions[6]['options'] = [
        {'label': 'A', 'text': 'Instead'},
        {'label': 'B', 'text': 'Nevertheless'},
        {'label': 'C', 'text': 'As a result'},
        {'label': 'D', 'text': 'Furthermore'},
    ]
    questions[6]['correctAnswer'] = 'D'
    questions[6]['explanation']['summaryVi'] = 'Câu 1 nêu cơ chế âm học 1 (lọc tạp âm tần số thấp). Câu 2 bổ sung cơ chế âm học 2 ĐỘC LẬP cùng giúp tăng độ rõ âm thanh (khuếch đại họa âm giọng nói tần số cao) → Bổ sung thêm yếu tố mới cùng chiều → "Furthermore" (D)!'
    questions[6]['explanation']['optionAnalysis'] = {
        'A': {'status': 'trap', 'trapTag': 'Substitution Trap', 'reasonVi': 'Không có phủ định nào ở câu 1 để thay thế bằng "Instead".'},
        'B': {'status': 'trap', 'trapTag': 'False Contrast', 'reasonVi': 'Hai cơ chế bổ trợ cùng chiều chứ không đối lập.'},
        'C': {'status': 'trap', 'trapTag': 'False Causation', 'reasonVi': 'Việc lọc gió tần số thấp không phải nguyên nhân tạo ra cấu trúc bậc thang khuếch đại giọng nói.'},
        'D': {'status': 'correct', 'trapTag': 'Đáp án đúng', 'reasonVi': 'Furthermore bổ sung chính xác cơ chế âm học thứ hai độc lập cùng cải thiện độ rõ của âm thanh.'},
    }

    return {
        'schemaVersion': 1,
        'mode': 'drill',
        'section': 'Reading and Writing',
        'basicInfo': {
            'title': 'Drill 3.1: Transitions — High-Level Logical Connectors (14 Qs)',
            'subtitle': 'Luyện sắc thái từ nối tầng Hard Module 2 (Instead vs. Nevertheless, In fact vs. In reality, Specifically vs. In other words, In response vs. Consequently).',
            'difficultyBadge': 'EoI • Target 1500+',
            'targetTimeMinutes': 12,
        },
        'drillModule': {
            'id': 'drill_3_1_mod',
            'title': 'Skill Drill 3.1: High-Level Transitions',
            'timeLimitMinutes': 12,
            'questions': questions,
        },
    }


def get_drill_3_2():
    questions = [
        q_item(
            'd3_2_q1', 1, 'Expression of Ideas', 'Rhetorical Synthesis', 'Medium',
            '''<p>While researching a topic, a student has taken the following notes:</p>
            <ul>
              <li>The James Webb Space Telescope (JWST) launched in December 2021 and orbits the Sun roughly 1.5 million kilometers from Earth.</li>
              <li>JWST observes the universe primarily in infrared wavelengths.</li>
              <li>The Hubble Space Telescope launched in 1990 and orbits Earth at an altitude of about 540 kilometers.</li>
              <li>Hubble observes the universe primarily in visible and ultraviolet wavelengths.</li>
            </ul>''',
            'The student wants to emphasize a difference in the types of light the two telescopes primarily observe. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
            [
                'Launched more than three decades apart, both the Hubble Space Telescope and the James Webb Space Telescope observe distant astronomical phenomena.',
                'While the Hubble Space Telescope orbits just 540 kilometers above Earth, the James Webb Space Telescope orbits the Sun 1.5 million kilometers away.',
                'Whereas the Hubble Space Telescope observes primarily in visible and ultraviolet wavelengths, the James Webb Space Telescope observes primarily in infrared wavelengths.',
                'The James Webb Space Telescope, which launched in December 2021, was designed to capture infrared wavelengths from deep space.'
            ],
            'C',
            'Goal-First SOP: Mục tiêu là nhấn mạnh ĐIỂM KHÁC BIỆT về LOẠI ÁNH SÁNG/BƯỚC SÓNG ("types of light") mà CẢ HAI kính viễn vọng quan sát. A nói điểm chung; B nói khác nhau về quỹ đạo; D chỉ nhắc 1 kính. Duy nhất C đối chiếu trực tiếp visible/ultraviolet (Hubble) vs. infrared (JWST)!',
            'Khóa đúng 2 tiêu chí của Goal: "difference" + "types of light" → loại ngay B (difference về orbit) và D (chỉ có 1 kính).',
            [
                ('Wrong Synthesis Goal', 'Nhấn mạnh điểm giống nhau thay vì điểm khác biệt về bước sóng.'),
                ('Wrong Criterion', 'Nêu sự khác biệt về quỹ đạo/khoảng cách chứ không phải loại ánh sáng quan sát.'),
                ('Đáp án đúng', 'Đối chiếu chính xác bước sóng chính của cả Hubble (visible/UV) và JWST (infrared).'),
                ('Single Subject Trap', 'Chỉ nói về JWST mà thiếu sự đối chiếu với Hubble.'),
            ]
        ),
        q_item(
            'd3_2_q2', 2, 'Expression of Ideas', 'Rhetorical Synthesis', 'Hard',
            '''<p>While researching a topic, a student has taken the following notes:</p>
            <ul>
              <li><i>Invisible Cities</i> is a 1972 novel by Italian writer Italo Calvino.</li>
              <li>The novel consists of fifty-five poetic prose descriptions of imagined cities narrated by explorer Marco Polo to Emperor Kublai Khan.</li>
              <li>Rather than following a linear plot, the chapters are arranged in a symmetrical mathematical lattice across nine sections.</li>
              <li>Calvino later explained that the book explores memory, desire, and the nature of urban life.</li>
            </ul>''',
            'The student wants to introduce <i>Invisible Cities</i> to an audience unfamiliar with the book and highlight its unconventional narrative structure. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
            [
                'Instead of unfolding through a linear plot, the book arranges fifty-five poetic city descriptions in a symmetrical mathematical lattice.',
                'Italian writer Italo Calvino’s 1972 novel <i>Invisible Cities</i> eschews a linear plot, instead arranging fifty-five poetic descriptions of imagined cities into a symmetrical mathematical lattice.',
                'In <i>Invisible Cities</i>, Marco Polo describes imagined cities to Kublai Khan in order to explore themes of memory, desire, and urban life.',
                'Italo Calvino’s 1972 work <i>Invisible Cities</i> is organized into nine sections and explores themes of memory and urban life.'
            ],
            'B',
            'Mục tiêu KÉP: (1) Giới thiệu cho khán giả CHƯA BIẾT tác phẩm ("unfamiliar" → phải nói rõ đó là tiểu thuyết năm 1972 của nhà văn Ý Italo Calvino) VÀ (2) nhấn mạnh CẤU TRÚC TỰ SỰ KHÁC THƯỜNG (không theo cốt truyện tuyến tính mà xếp theo mạng toán học đối xứng). A quên giới thiệu tác giả/tên sách ("the book"); C và D thiếu điểm cốt lõi "unconventional structure". Chỉ B trọn vẹn cả 2 yêu cầu!',
            'Mục tiêu có chữ "unfamiliar with X" → BẮT BUỘC định danh rõ X là gì và của ai; tuyệt đối loại đáp án mở đầu cụt ngủn bằng "the book" hay gọi trống không tên tác phẩm!',
            [
                ('Missing Audience Context', 'Gọi trống không "the book" mà không giới thiệu tên sách, năm hay tác giả cho độc giả chưa biết.'),
                ('Đáp án đúng', 'Vừa định danh đầy đủ (Italian writer Italo Calvino’s 1972 novel Invisible Cities) vừa nêu bật cấu trúc phi tuyến tính dạng mạng đối xứng.'),
                ('Wrong Synthesis Goal', 'Không giới thiệu tác giả/thể loại cho người chưa biết và chỉ nói chủ đề chứ không nhấn mạnh cấu trúc phi tuyến tính.'),
                ('Incomplete Goal', 'Nhắc "nine sections" nhưng không làm nổi bật điểm khác thường là phi tuyến tính / mạng toán học đối xứng.'),
            ]
        ),
        q_item(
            'd3_2_q3', 3, 'Expression of Ideas', 'Rhetorical Synthesis', 'Hard',
            '''<p>While researching a topic, a student has taken the following notes:</p>
            <ul>
              <li>In 2022, neuroscientist Dr. Priya Nair investigated how background ambient noise affects creative problem-solving.</li>
              <li>She divided 180 adult participants into three rooms set at 50 decibels (quiet), 70 decibels (moderate café noise), and 85 decibels (loud traffic).</li>
              <li>Participants completed standardized remote-association tasks measuring divergent thinking.</li>
              <li>Participants in the 70-decibel room scored 24% higher on average than those in either the 50-decibel or 85-decibel rooms.</li>
            </ul>''',
            'The student wants to present Dr. Priya Nair’s study and its methodology without focusing on the numerical results. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
            [
                'Dr. Priya Nair found that participants exposed to moderate 70-decibel café noise scored 24% higher on creative tasks than those in quieter or louder rooms.',
                'To examine how ambient sound shapes creative problem-solving, Dr. Priya Nair had 180 adults complete divergent-thinking tasks across rooms set at 50, 70, and 85 decibels.',
                'In a 2022 study of 180 adults, moderate ambient sound at 70 decibels boosted divergent thinking by an average of 24%.',
                'Standardized remote-association tasks are commonly used by neuroscientists to measure divergent thinking in quiet and noisy settings.'
            ],
            'B',
            'Mục tiêu: Trình bày nghiên cứu và PHƯƠNG PHÁP THỰC HIỆN (methodology), KHÔNG tập trung vào kết quả số liệu (without focusing on numerical results). A và C đánh thẳng vào kết quả 24% (vi phạm trực tiếp yêu cầu!); D bỏ quên hoàn toàn Dr. Nair và quy trình chia 3 phòng. Chỉ B nêu chính xác mục đích nghiên cứu + cách thiết kế thí nghiệm (180 người, 3 mức 50/70/85 dB, làm bài remote-association).',
            'Phân biệt cực nhạy: "methodology" = cách chia nhóm/đo đạc; "findings" = kết quả thu được!',
            [
                ('Findings Instead of Methodology', 'Tập trung thẳng vào kết quả tăng 24% — trái ngược yêu cầu "without focusing on numerical results".'),
                ('Đáp án đúng', 'Giới thiệu gọn gàng nghiên cứu của Dr. Nair và toàn bộ phương pháp thực nghiệm mà không sa vào kết quả 24%.'),
                ('Findings Instead of Methodology', 'Nhấn mạnh kết quả tăng 24% thay vì quy trình thí nghiệm.'),
                ('Missing Study Details', 'Nói chung chung về bài test mà bỏ qua thiết kế 3 mức âm lượng của Dr. Nair.'),
            ]
        ),
        q_item(
            'd3_2_q4', 4, 'Expression of Ideas', 'Rhetorical Synthesis', 'Hard',
            '''<p>While researching a topic, a student has taken the following notes:</p>
            <ul>
              <li>Some migratory birds cross ecological barriers such as deserts or open oceans in a single continuous flight.</li>
              <li>The bar-tailed godwit flies roughly 11,000 kilometers nonstop from Alaska to New Zealand over the Pacific Ocean.</li>
              <li>Before departure, the bird shrinks several internal digestive organs to reduce body mass and enlarge its flight muscles.</li>
              <li>The blackpoll warbler, weighing just twelve grams, flies nonstop for up to three days over the western Atlantic Ocean.</li>
            </ul>''',
            'The student wants to make and support a generalization about migratory birds that cross major ecological barriers. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
            [
                'Before flying 11,000 kilometers from Alaska to New Zealand, the bar-tailed godwit shrinks its digestive organs to lower body weight.',
                'Both the bar-tailed godwit and the twelve-gram blackpoll warbler undertake remarkable migrations across vast oceans.',
                'Some migratory birds traverse vast ecological barriers in single nonstop flights; for example, the bar-tailed godwit flies roughly 11,000 kilometers across the Pacific, while the tiny blackpoll warbler flies up to three days nonstop over the Atlantic.',
                'Weighing only twelve grams, the blackpoll warbler crosses the western Atlantic Ocean in a single flight, whereas the bar-tailed godwit migrates across the Pacific.'
            ],
            'C',
            'Mục tiêu: "make AND support a GENERALIZATION" (đưa ra 1 nhận định khái quát + kèm ví dụ cụ thể minh họa từ notes). A chỉ có 1 ví dụ lẻ; B và D chỉ nêu tên 2 loài mà không có tuyên bố khái quát mở rộng cho nhóm "some migratory birds" nói chung. Duy nhất C có đủ 2 phần: Generalization ("Some migratory birds traverse vast ecological barriers in single nonstop flights") + Support ("for example, the bar-tailed godwit... while the tiny blackpoll warbler...").',
            'Nhìn thấy "make and support a generalization" → Tìm ngay cấu trúc `[Khái quát rộng] + [for example / such as + Ví dụ cụ thể]`!',
            [
                ('Missing Generalization', 'Chỉ nêu ví dụ riêng của loài bar-tailed godwit, thiếu câu khái quát chung.'),
                ('Missing Generalization', 'Chỉ ghép hai loài cụ thể, chưa nâng lên thành quy luật chung về chim di cư vượt rào cản sinh thái.'),
                ('Đáp án đúng', 'Mở đầu bằng mệnh đề khái quát chuẩn xác và chứng minh ngay bằng hai ví dụ cụ thể từ ghi chú.'),
                ('Contrast Instead of Generalization', 'Tập trung đối chiếu hai loài thay vì phát biểu và chứng minh một nhận định khái quát.'),
            ]
        ),
        q_item(
            'd3_2_q5', 5, 'Expression of Ideas', 'Rhetorical Synthesis', 'Elite (750+)',
            '''<p>While researching a topic, a student has taken the following notes:</p>
            <ul>
              <li>In 1925, physicist Cecilia Payne-Gaposchkin submitted a doctoral thesis at Radcliffe College analyzing stellar absorption spectra.</li>
              <li>At the time, leading astronomers believed stars had roughly the same elemental composition as Earth, rich in iron and heavy metals.</li>
              <li>Payne-Gaposchkin calculated that stars are composed overwhelmingly of hydrogen and helium—elements millions of times more abundant than previously thought.</li>
              <li>Astronomer Henry Norris Russell initially urged her to call this result "almost certainly not real," before independently confirming her finding four years later.</li>
            </ul>''',
            'The student wants to emphasize how Cecilia Payne-Gaposchkin’s 1925 calculation challenged the scientific consensus of her era. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
            [
                'In 1925, Cecilia Payne-Gaposchkin analyzed stellar absorption spectra in her doctoral thesis at Radcliffe College, and Henry Norris Russell confirmed her work in 1929.',
                'Although leading astronomers initially assumed stars were composed mainly of hydrogen and helium, Payne-Gaposchkin calculated in 1925 that they resembled Earth’s iron-rich makeup.',
                'Defying the prevailing view that stars shared Earth’s iron-rich composition, Cecilia Payne-Gaposchkin’s 1925 thesis calculated that stars consist overwhelmingly of hydrogen and helium.',
                'Henry Norris Russell initially doubted Cecilia Payne-Gaposchkin’s 1925 doctoral calculations at Radcliffe College.'
            ],
            'C',
            'BẪY HARD MODULE 2 — FACT-CHECK BẮT BUỘC! Nhìn B và C: cả hai đều có cấu trúc "challenging consensus", NHƯNG đáp án B cố tình ĐẢO NGƯỢC SỰ THẬT (viết giới thiên văn tin sao toàn hydro còn Payne tính sao toàn sắt — sai 100% với bullet notes!). Chỉ có C vừa đúng Goal vừa chính xác 100% Fact!',
            'Cảnh giác tuyệt đối ở Hard Module 2: Luôn đối chiếu lại 5 giây với bullet notes xem đáp án có bị đảo vai (Fact Swap) như B không!',
            [
                ('Wrong Synthesis Goal', 'Chỉ kể lại dòng thời gian 1925–1929 mà không hề nêu đồng thuận khoa học cũ bị thách thức là gì.'),
                ('Fact Swap Trap!', 'Đánh tráo hoàn toàn quan điểm cũ (giàu sắt như Trái Đất) với phát hiện của Payne (hydro & heli) — bẫy cực hiểm!'),
                ('Đáp án đúng', 'Khớp cả mục tiêu (thách thức đồng thuận thời đó) lẫn sự thật 100% từ ghi chú.'),
                ('Incomplete Goal', 'Chỉ nhắc sự nghi ngờ của một cá nhân (Russell) mà không nêu đồng thuận khoa học bị thách thức là gì.'),
            ]
        ),
        q_item(
            'd3_2_q6', 6, 'Expression of Ideas', 'Rhetorical Synthesis', 'Hard',
            '''<p>While researching a topic, a student has taken the following notes:</p>
            <ul>
              <li><i>The Great Wave off Kanagawa</i> (c. 1831) is a famous Japanese woodblock print by Katsushika Hokusai.</li>
              <li>The print’s vivid deep-blue tones were achieved using Prussian blue, a synthetic pigment invented in Berlin in the early 1700s.</li>
              <li>Dutch traders imported Prussian blue to Nagasaki during Japan’s period of restricted foreign trade.</li>
              <li>Before Prussian blue arrived, Japanese printmakers relied mainly on plant-based indigo, which faded quickly when exposed to light.</li>
            </ul>''',
            'The student wants to explain how European trade transformed the visual durability of Hokusai’s woodblock prints to an audience already familiar with <i>The Great Wave off Kanagawa</i>. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
            [
                '<i>The Great Wave off Kanagawa</i> is a famous Japanese woodblock print created around 1831 by Katsushika Hokusai using Prussian blue.',
                'By importing synthetic Prussian blue from Europe to Nagasaki, Dutch traders enabled Hokusai to replace easily fading plant indigo with durable deep-blue tones in <i>The Great Wave off Kanagawa</i>.',
                'Before synthetic pigments became available, Japanese artists relied on plant-based indigo, which faded quickly in sunlight.',
                'Invented in Berlin in the early 1700s, Prussian blue reached Nagasaki during Japan’s period of restricted foreign trade.'
            ],
            'B',
            'Mục tiêu: (1) Giải thích thương mại châu Âu thay đổi ĐỘ BỀN MÀU (visual durability) tranh của Hokusai thế nào, (2) cho khán giả ĐÃ QUEN thuộc bức The Great Wave (không cần định nghĩa dài dòng đó là bức tranh nổi tiếng của Nhật). B làm tròn cả 2: nối trực tiếp thương nhân Hà Lan nhập Prussian blue từ châu Âu → giúp Hokusai thay thế mực chàm dễ phai bằng sắc xanh bền màu.',
            'Khi khán giả đã "familiar with X", tránh đáp án mở đầu bằng định nghĩa thừa kiểu "X is a famous Japanese print..."; đi thẳng vào mục tiêu nhân–quả!',
            [
                ('Wrong Goal + Unneeded Intro', 'Định nghĩa lại tác phẩm cho người đã biết và không hề giải thích tác động đến độ bền màu.'),
                ('Đáp án đúng', 'Kết nối trực tiếp thương mại Hà Lan – châu Âu, sắc tố tổng hợp Prussian blue và sự thay thế mực chàm nhanh phai trong tranh Hokusai.'),
                ('Incomplete Goal', 'Chỉ nói về mực chàm trước đây mà không nhắc thương mại châu Âu hay Hokusai.'),
                ('Incomplete Goal', 'Chỉ kể đường đi của thuốc nhuộm mà bỏ quên Hokusai và độ bền màu (durability).'),
            ]
        ),
        q_item(
            'd3_2_q7', 7, 'Expression of Ideas', 'Rhetorical Synthesis', 'Hard',
            '''<p>While researching a topic, a student has taken the following notes:</p>
            <ul>
              <li>Geothermal district heating pumps naturally heated subterranean water through insulated municipal pipelines to warm buildings.</li>
              <li>Reykjavik, Iceland, supplies roughly 95% of its residential heating from volcanic geothermal reservoirs.</li>
              <li>Paris, France, sits atop a non-volcanic sedimentary basin whose deep aquifers hold 70°C water that heats over 250,000 homes.</li>
              <li>Engineers emphasize that geothermal heating does not require active volcanoes when deep sedimentary aquifers are accessible.</li>
            </ul>''',
            'The student wants to dispel the misconception that municipal geothermal heating is viable only in volcanic regions. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
            [
                'In volcanic Reykjavik, Iceland, insulated pipelines deliver subterranean geothermal water to meet roughly 95% of residential heating demand.',
                'Geothermal district heating uses insulated municipal pipelines to circulate naturally heated underground water into homes in both Reykjavik and Paris.',
                'Paris proves that geothermal heating is not restricted to volcanic regions like Reykjavik: sitting atop a non-volcanic sedimentary basin, the city taps 70°C deep aquifers to heat more than 250,000 homes.',
                'While Reykjavik draws heat from volcanic reservoirs, Paris has more than 250,000 homes connected to municipal heating pipelines.'
            ],
            'C',
            'Mục tiêu: PHÁ BỎ HIỂU LẦM (dispel the misconception) rằng hệ thống sưởi địa nhiệt CHỈ khả thi ở vùng núi lửa. Cần lấy ví dụ Paris nằm trên lưu vực trầm tích KHÔNG CÓ NÚI LỬA (non-volcanic sedimentary basin) vẫn sưởi hơn 250.000 hộ dân! Chỉ C bác bỏ trực tiếp hiểu lầm này bằng đối chứng Paris (non-volcanic) với Reykjavik.',
            'Mục tiêu "dispel a misconception" đòi hỏi đáp án phải gọi thẳng hiểu lầm đó ra và lấy bằng chứng phản biện từ notes!',
            [
                ('Reinforces Misconception', 'Chỉ nêu ví dụ Reykjavik có núi lửa — càng củng cố hiểu lầm thay vì phá bỏ.'),
                ('Wrong Synthesis Goal', 'Chỉ mô tả chung cách vận hành ống dẫn mà không nhắc yếu tố phi núi lửa của Paris.'),
                ('Đáp án đúng', 'Bác bỏ trực diện quan niệm sai lầm bằng dẫn chứng Paris nằm trên tầng trầm tích phi núi lửa vẫn sưởi hơn 250.000 ngôi nhà.'),
                ('Missing Key Detail', 'Quên chi tiết cốt lõi "non-volcanic sedimentary basin" của Paris nên không phá bỏ được hiểu lầm.'),
            ]
        ),
        q_item(
            'd3_2_q8', 8, 'Expression of Ideas', 'Rhetorical Synthesis', 'Elite (750+)',
            '''<p>While researching a topic, a student has taken the following notes:</p>
            <ul>
              <li>The Maya city of Tikal flourished in northern Guatemala from roughly 200 to 900 CE without access to any nearby rivers or natural lakes.</li>
              <li>Tikal’s engineers paved wide limestone plazas at slight slopes to funnel seasonal monsoon rain into massive lined reservoirs.</li>
              <li>Recent mineralogical testing of sediment from Corriental, one of Tikal’s central reservoirs, detected crystalline quartz and zeolite sands imported from over 30 kilometers away.</li>
              <li>Together, quartz and zeolite act as a molecular sieve capable of filtering microbes, heavy metals, and cyanobacteria toxins from drinking water.</li>
            </ul>''',
            'The student wants to emphasize the technological sophistication of Tikal’s water purification system rather than its rainwater collection design. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
            [
                'Because Tikal lacked nearby rivers or lakes, Maya engineers sloped limestone plazas to channel monsoon rains into large municipal reservoirs.',
                'Flourishing between 200 and 900 CE in northern Guatemala, Tikal relied on paved limestone plazas and massive reservoirs to survive without rivers.',
                'Rather than simply storing rainfall, Tikal’s engineers imported quartz and zeolite sands from over 30 kilometers away to build a molecular-sieve filter in the Corriental reservoir that removed microbes and toxins.',
                'Recent mineralogical testing at Tikal examined sediments from Corriental, one of several reservoirs built in northern Guatemala between 200 and 900 CE.'
            ],
            'C',
            'Chú ý mệnh đề loại trừ trong Goal: "emphasize the technological sophistication of Tikal’s WATER PURIFICATION system RATHER THAN its rainwater collection design" (nhấn mạnh hệ thống LỌC NƯỚC, không phải hệ thống thu nước mưa!). A và B tập trung vào việc lát quảng trường hứng mưa (sai mục tiêu!). D bỏ qua chức năng lọc nước. Duy nhất C tập trung vào thạch anh + zeolite lọc vi khuẩn và độc tố!',
            'Trong Rhetorical Synthesis, cực kỳ chú ý cụm "rather than X" ở cuối câu hỏi — đó là chiếc kéo cắt thẳng 2 đáp án bẫy!',
            [
                ('Wrong Focus (Collection Trap)', 'Tập trung vào thiết kế hứng nước mưa thay vì công nghệ lọc nước sạch.'),
                ('Wrong Focus (Collection Trap)', 'Chỉ nhắc quảng trường và hồ chứa mà bỏ qua hệ thống lọc nước.'),
                ('Đáp án đúng', 'Làm nổi bật công nghệ lọc cấp phân tử bằng cát thạch anh và zeolite nhập từ xa 30 km để loại bỏ vi khuẩn và độc tố.'),
                ('Missing Key Detail', 'Nhắc tên hồ Corriental nhưng không hề mô tả hệ thống lọc hay tính tinh vi công nghệ.'),
            ]
        ),
        q_item(
            'd3_2_q9', 9, 'Expression of Ideas', 'Rhetorical Synthesis', 'Hard',
            '''<p>While researching a topic, a student has taken the following notes:</p>
            <ul>
              <li>In 1966, artist Alma Thomas became the first Black woman to hold a solo exhibition at the Whitney Museum of American Art (in 1972, at age 80).</li>
              <li>Note correction: Alma Thomas retired from teaching middle-school art in Washington, D.C., in 1960 and began painting full-time in her late sixties.</li>
              <li>Her vibrant abstract canvases feature rhythmic mosaics of short, colorful brushstrokes inspired by gardens and Apollo space missions.</li>
              <li>Her 1972 Whitney solo exhibition established her as a major figure in the Washington Color School movement.</li>
            </ul>''',
            'The student wants to highlight the late-career timing of Alma Thomas’s breakthrough as a full-time abstract painter. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
            [
                'Inspired by gardens and Apollo space missions, Alma Thomas painted rhythmic mosaics of short, colorful brushstrokes as part of the Washington Color School.',
                'Alma Thomas taught middle-school art in Washington, D.C., and later exhibited her abstract paintings at the Whitney Museum of American Art.',
                'Turning to full-time painting only in her late sixties after retiring from teaching in 1960, Alma Thomas achieved major acclaim with a landmark 1972 solo exhibition at the Whitney Museum at age 80.',
                'Alma Thomas was a prominent painter in the Washington Color School whose vibrant works drew inspiration from nature and space exploration.'
            ],
            'C',
            'Mục tiêu: nhấn mạnh THỜI ĐIỂM MUỘN TRONG SỰ NGHIỆP ("late-career timing") khi Alma Thomas bứt phá làm họa sĩ toàn thời gian. A và D không có mốc tuổi/thời điểm nào; B chỉ nói chung chung "later". Duy nhất C chốt trọn chuỗi mốc ấn tượng: nghỉ dạy năm 1960, bắt đầu vẽ toàn thời gian ở cuối tuổi 60, triển lãm cá nhân lịch sử tại Whitney ở tuổi 80!',
            'Mục tiêu nhấn mạnh "timing" → ưu tiên đáp án giữ đủ các mốc tuổi/thời gian sắc nét nhất từ bullet notes.',
            [
                ('Wrong Synthesis Goal', 'Chỉ mô tả phong cách và cảm hứng hội họa, thiếu hoàn toàn yếu tố thời điểm muộn của sự nghiệp.'),
                ('Weak / Missing Timing Details', 'Chỉ viết chung chung "later" mà bỏ lỡ các mốc cốt lõi (late sixties, age 80).'),
                ('Đáp án đúng', 'Làm nổi bật trọn vẹn bước ngoặt sự nghiệp muộn (late sixties → solo exhibition at age 80).'),
                ('Wrong Synthesis Goal', 'Không nhắc đến tuổi tác hay thời điểm khởi đầu sự nghiệp vẽ toàn thời gian.'),
            ]
        ),
        q_item(
            'd3_2_q10', 10, 'Expression of Ideas', 'Rhetorical Synthesis', 'Hard',
            '''<p>While researching a topic, a student has taken the following notes:</p>
            <ul>
              <li>Stradivarius violins crafted in Cremona during the early 1700s are prized for their tonal clarity.</li>
              <li>In 2014, acoustician Claudia Fritz organized a double-blind test in Paris comparing six antique Italian violins with six newly built modern violins.</li>
              <li>Ten international soloists played the twelve instruments in a concert hall while wearing modified welder’s goggles so they could not identify each violin’s age.</li>
              <li>When asked to choose one instrument for a hypothetical concert tour, six of the ten soloists selected a modern violin over an antique Italian one.</li>
            </ul>''',
            'The student wants to emphasize a surprising outcome of Claudia Fritz’s 2014 double-blind test. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
            [
                'To prevent ten international soloists from recognizing antique Stradivarius violins, Claudia Fritz required them to wear modified welder’s goggles during a 2014 concert-hall test.',
                'Despite the legendary reputation of antique Cremonese violins, six of ten soloists in Claudia Fritz’s 2014 double-blind test chose a newly built modern violin over an antique one for a hypothetical tour.',
                'Crafted in Cremona during the early 1700s, Stradivarius violins were compared against six modern violins in a 2014 Paris experiment.',
                'In 2014, acoustician Claudia Fritz asked ten soloists to evaluate twelve violins—six antique Italian instruments and six newly made ones.'
            ],
            'B',
            'Mục tiêu: nhấn mạnh KẾT QUẢ GÂY BẤT NGỜ (surprising outcome) của thí nghiệm mù đôi 2014. A, C, D chỉ mô tả phương pháp/bối cảnh mà KHÔNG NÊU KẾT QUẢ! Duy nhất B nêu rõ kết quả đảo ngược kỳ vọng: dù đàn cổ danh tiếng lẫy lừng, 6/10 nghệ sĩ độc tấu lại chọn đàn hiện đại!',
            'Đề hỏi "outcome / finding" → loại ngay mọi đáp án chỉ dừng ở bước thiết kế thí nghiệm!',
            [
                ('Methodology Instead of Outcome', 'Chỉ mô tả việc đeo kính hàn để giấu danh tính đàn mà không nêu kết quả cuối cùng.'),
                ('Đáp án đúng', 'Đặt sự tương phản kỳ vọng (legendary reputation) ngay cạnh kết quả bất ngờ (6/10 chọn đàn hiện đại).'),
                ('Missing Outcome', 'Chỉ giới thiệu bối cảnh so sánh mà thiếu kết quả.'),
                ('Methodology Instead of Outcome', 'Chỉ liệt kê số lượng nghệ sĩ và cây đàn tham gia thử nghiệm.'),
            ]
        ),
        q_item(
            'd3_2_q11', 11, 'Expression of Ideas', 'Rhetorical Synthesis', 'Elite (750+)',
            '''<p>While researching a topic, a student has taken the following notes:</p>
            <ul>
              <li>In 2017, botanist Dr. Sofia Morales surveyed alpine wildflowers across twelve peaks in the Swiss Alps first inventoried in 1907.</li>
              <li>She found that 84% of surveyed plant species had shifted their upper elevation limits higher over the intervening 110 years.</li>
              <li>Fast-dispersing species with wind-borne seeds climbed an average of 42 meters per decade.</li>
              <li>Slow-dispersing species with heavy, gravity-dropped seeds climbed only 9 meters per decade, risking displacement by faster-moving lowland competitors.</li>
            </ul>''',
            'The student wants to explain why slow-dispersing alpine plants face a greater ecological risk than fast-dispersing ones according to Dr. Morales’s survey. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
            [
                'Dr. Sofia Morales revisited twelve Swiss Alpine peaks first inventoried in 1907 and found that 84% of surveyed plant species had moved to higher elevations.',
                'In the Swiss Alps, plants with wind-borne seeds moved upward at 42 meters per decade, whereas 84% of all surveyed wildflowers shifted upward over 110 years.',
                'Because heavy-seeded alpine plants migrate upward at just 9 meters per decade—far slower than wind-dispersed species at 42 meters per decade—they risk being outcompeted by faster-climbing lowland rivals.',
                'Fast-dispersing alpine plants have wind-borne seeds, while slow-dispersing alpine plants produce heavier seeds that drop by gravity.'
            ],
            'C',
            'Mục tiêu: GIẢI THÍCH VÌ SAO loài phát tán chậm gặp rủi ro sinh thái lớn hơn loài phát tán nhanh. A và B không nhắc rủi ro hay loài phát tán chậm; D chỉ mô tả khác biệt hạt mà thiếu hệ quả rủi ro bị lấn át. Chỉ C nối trực tiếp tốc độ leo chậm (9m/thập kỷ vs. 42m) → hệ quả rủi ro bị đối thủ vùng thấp cạnh tranh thay thế!',
            'Câu hỏi có chữ "explain WHY ... face a greater risk" → Đáp án đúng bắt buộc chứa quan hệ NHÂN – QUẢ nối trực tiếp vào "risk"!',
            [
                ('Wrong Synthesis Goal', 'Chỉ nêu kết quả tổng thể 84% mà không giải thích rủi ro của nhóm phát tán chậm.'),
                ('Wrong Comparison / Missing Risk', 'Bỏ qua hoàn toàn nhóm phát tán chậm và rủi ro sinh thái.'),
                ('Đáp án đúng', 'Giải thích trọn vẹn nguyên nhân (chỉ leo 9m so với 42m/thập kỷ) dẫn đến rủi ro bị đối thủ vùng thấp lấn át.'),
                ('Missing Risk Explanation', 'Chỉ mô tả hình thái hạt chứ không giải thích vì sao điều đó gây nguy cơ sinh thái.'),
            ]
        ),
        q_item(
            'd3_2_q12', 12, 'Expression of Ideas', 'Rhetorical Synthesis', 'Hard',
            '''<p>While researching a topic, a student has taken the following notes:</p>
            <ul>
              <li><i>Kintsugi</i> is a traditional Japanese ceramic repair technique dating back to the fifteenth century.</li>
              <li>Artisans rejoin broken pottery shards using urushi tree lacquer dusted with powdered gold, silver, or platinum.</li>
              <li>Rather than disguising cracks, <i>kintsugi</i> deliberately highlights the fracture lines as part of the vessel’s history.</li>
              <li>The craft reflects the aesthetic philosophy of <i>wabi-sabi</i>, which values imperfection and impermanence.</li>
            </ul>''',
            'The student wants to connect the physical technique of <i>kintsugi</i> to its underlying cultural philosophy. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
            [
                'Dating to the fifteenth century, the Japanese craft of <i>kintsugi</i> uses urushi tree lacquer mixed with powdered gold, silver, or platinum to rejoin broken pottery.',
                '<i>Wabi-sabi</i> is a traditional Japanese aesthetic philosophy that celebrates imperfection and impermanence in everyday objects.',
                'By mending shattered ceramics with gold-dusted lacquer that spotlights rather than conceals cracks, <i>kintsugi</i> embodies the <i>wabi-sabi</i> philosophy of embracing imperfection and impermanence.',
                'Unlike Western repair methods, <i>kintsugi</i> artisans prefer to preserve the history of a fifteenth-century ceramic vessel.'
            ],
            'C',
            'Mục tiêu: KẾT NỐI kỹ thuật vật lý (physical technique) với triết lý văn hóa nền tảng (cultural philosophy — wabi-sabi). A chỉ nói kỹ thuật; B chỉ nói triết lý; D tự bịa "Western repair methods" (Out of Notes!) và quên wabi-sabi. Chỉ C nối trọn vẹn cả hai vế!',
            'Cực kỳ tránh đáp án tự thêm thông tin không có trong Bullet Notes (như "Unlike Western repair methods" ở D)!',
            [
                ('Incomplete Goal', 'Chỉ mô tả vật liệu và kỹ thuật sửa gốm, không nhắc tới triết lý wabi-sabi.'),
                ('Incomplete Goal', 'Chỉ định nghĩa wabi-sabi mà không nối sang kỹ thuật kintsugi.'),
                ('Đáp án đúng', 'Kết nối mượt mà kỹ thuật gắn sơn mài rắc vàng làm nổi vết nứt với triết lý wabi-sabi trân trọng sự bất toàn.'),
                ('Out of Notes / Missing Philosophy', 'Tự bịa so sánh với phương Tây không có trong ghi chú và bỏ quên wabi-sabi.'),
            ]
        ),
        q_item(
            'd3_2_q13', 13, 'Expression of Ideas', 'Rhetorical Synthesis', 'Elite (750+)',
            '''<p>While researching a topic, a student has taken the following notes:</p>
            <ul>
              <li>In 2020, economist Dr. Henrik Lind tested whether shortening municipal transit headways from 15 minutes to 6 minutes increases ridership more than cutting fares by 40%.</li>
              <li>In City A, transit agencies reduced bus wait times to 6 minutes while keeping ticket prices unchanged, yielding a 31% rise in weekday ridership.</li>
              <li>In City B, transit agencies cut fares by 40% while maintaining 15-minute wait times, yielding a 14% rise in weekday ridership.</li>
              <li>Lind concluded that service frequency is a stronger lever for attracting daily commuters than fare discounts alone.</li>
            </ul>''',
            'The student wants to present Dr. Lind’s conclusion and the comparative data supporting it. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
            [
                'Dr. Henrik Lind concluded that increasing bus frequency attracts daily commuters more effectively than lowering ticket prices: cutting wait times to 6 minutes boosted ridership by 31% in City A, whereas a 40% fare cut in City B raised ridership by only 14%.',
                'In 2020, Dr. Henrik Lind studied two cities, reducing bus wait times to 6 minutes in City A and cutting transit fares by 40% in City B.',
                'Dr. Henrik Lind concluded that fare discounts attract daily commuters more strongly than higher frequency, since City B’s 40% fare cut lifted ridership by 31% compared to City A’s 14%.',
                'When City A shortened municipal bus headways from 15 minutes to 6 minutes while keeping ticket prices unchanged, weekday ridership rose by 31%.'
            ],
            'A',
            'BẪY HARD MODULE 2 — FACT-SWAP CHECK! Cả A và C đều có đủ "conclusion + comparative data", NHƯNG đáp án C đánh tráo ngược hoàn toàn kết luận lẫn số liệu (gán 31% cho City B và 14% cho City A)! B thiếu kết quả & kết luận; D chỉ nêu City A (thiếu comparative data với City B và thiếu kết luận). Chỉ A đúng 100% cả Goal lẫn Fact!',
            'Khi thấy 2 đáp án có cấu trúc y hệt nhau đều khớp Goal → 100% một đáp án đang chứa bẫy đánh tráo số liệu/kết luận! Kiểm tra chéo ngay với Bullet Notes!',
            [
                ('Đáp án đúng', 'Trình bày chính xác kết luận của Dr. Lind kèm đầy đủ cặp số liệu so sánh đối chứng City A (31%) vs. City B (14%).'),
                ('Missing Findings & Conclusion', 'Chỉ nêu thiết kế thử nghiệm mà thiếu số liệu kết quả và kết luận.'),
                ('Fact Swap Trap!', 'Đảo ngược hoàn toàn kết luận (cho rằng giảm giá mạnh hơn) và tráo số liệu giữa City A với City B!'),
                ('Single Case / Missing Comparison', 'Chỉ nói City A mà thiếu đối chiếu với City B và kết luận chung của Lind.'),
            ]
        ),
        q_item(
            'd3_2_q14', 14, 'Expression of Ideas', 'Rhetorical Synthesis', 'Hard',
            '''<p>While researching a topic, a student has taken the following notes:</p>
            <ul>
              <li>The Svalbard Global Seed Vault is built deep inside a permafrost mountain on the Norwegian island of Spitsbergen.</li>
              <li>It stores duplicate seed samples from national gene banks worldwide at a constant temperature of −18°C.</li>
              <li>In 2015, Syria’s International Center for Agricultural Research in the Dry Areas (ICARDA) became the first organization to withdraw seeds from the vault after armed conflict damaged its Aleppo gene bank.</li>
              <li>ICARDA successfully multiplied those withdrawn drought-tolerant wheat and barley varieties in Lebanon and Morocco and returned fresh backup deposits to Svalbard in 2017.</li>
            </ul>''',
            'The student wants to illustrate how the Svalbard Global Seed Vault fulfilled its backup purpose in a real-world crisis. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
            [
                'Built deep inside a permafrost mountain on Spitsbergen, the Svalbard Global Seed Vault stores duplicate seed samples from national gene banks at −18°C.',
                'In 2017, ICARDA deposited fresh samples of drought-tolerant wheat and barley at the Svalbard Global Seed Vault in Norway.',
                'The Svalbard Global Seed Vault keeps backup seed collections from across the globe frozen at −18°C in case national gene banks are ever threatened.',
                'After armed conflict damaged ICARDA’s gene bank in Aleppo, the organization withdrew its backup seeds from Svalbard in 2015, regrew the crops in Lebanon and Morocco, and returned fresh reserves in 2017.'
            ],
            'D',
            'Mục tiêu: MINH HỌA cách kho hạt giống Svalbard hoàn thành sứ mệnh dự phòng TRONG MỘT CUỘC KHỦNG HOẢNG THỰC TẾ (real-world crisis). A và C chỉ mô tả thiết kế chung; B bỏ qua bối cảnh khủng hoảng 2015 và việc rút hạt giống cứu cây trồng. Duy nhất D kể trọn chu trình thực tế: xung đột ở Aleppo → rút hạt năm 2015 → nhân giống tại Lebanon & Morocco → gửi trả kho dự phòng năm 2017!',
            'Mục tiêu có chữ "illustrate ... in a real-world crisis" → tìm đúng trường hợp lịch sử cụ thể (ICARDA 2015–2017) thể hiện trọn vẹn vòng đời giải cứu.',
            [
                ('General Description Only', 'Chỉ mô tả vị trí và nhiệt độ kho hạt giống, không hề nhắc tới khủng hoảng thực tế.'),
                ('Incomplete Illustration', 'Chỉ nhắc bước gửi trả năm 2017 mà bỏ qua bối cảnh xung đột và việc rút hạt giống cứu giống cây năm 2015.'),
                ('Hypothetical Only', 'Chỉ nêu mục đích lý thuyết "in case", không đưa dẫn chứng thực tế.'),
                ('Đáp án đúng', 'Minh họa trọn vẹn chu trình dự phòng thực tế qua trường hợp khủng hoảng của ICARDA (2015–2017).'),
            ]
        ),
    ]

    # Fix note bullet 1 in Q9 cleanly (no internal note text)
    questions[8]['stimulusHtml'] = '''<p>While researching a topic, a student has taken the following notes:</p>
            <ul>
              <li>Alma Thomas retired from teaching middle-school art in Washington, D.C., in 1960 and began painting full-time in her late sixties.</li>
              <li>Her vibrant abstract canvases feature rhythmic mosaics of short, colorful brushstrokes inspired by gardens and Apollo space missions.</li>
              <li>In 1972, at age 80, she became the first Black woman to hold a solo exhibition at the Whitney Museum of American Art.</li>
              <li>The landmark Whitney exhibition established her as a major figure in the Washington Color School movement.</li>
            </ul>'''

    # Balance A/B/C/D nicely: currently A:1, B:4, C:8, D:1 -> move Q1(C->D), Q4(C->A), Q8(C->D), Q11(C->A) for A:3, B:4, C:4, D:3!
    # Q1: swap C and D
    q1 = questions[0]
    q1['options'][2]['text'], q1['options'][3]['text'] = q1['options'][3]['text'], q1['options'][2]['text']
    q1['correctAnswer'] = 'D'
    q1['explanation']['summaryVi'] = 'Goal-First SOP: Mục tiêu là nhấn mạnh ĐIỂM KHÁC BIỆT về LOẠI ÁNH SÁNG/BƯỚC SÓNG ("types of light") mà CẢ HAI kính viễn vọng quan sát. A nói điểm chung; B nói khác nhau về quỹ đạo; C chỉ nhắc 1 kính. Duy nhất D đối chiếu trực tiếp visible/ultraviolet (Hubble) vs. infrared (JWST)!'
    q1['explanation']['optionAnalysis']['C'], q1['explanation']['optionAnalysis']['D'] = q1['explanation']['optionAnalysis']['D'], q1['explanation']['optionAnalysis']['C']

    # Q4: swap A and C
    q4 = questions[3]
    q4['options'][0]['text'], q4['options'][2]['text'] = q4['options'][2]['text'], q4['options'][0]['text']
    q4['correctAnswer'] = 'A'
    q4['explanation']['summaryVi'] = 'Mục tiêu: "make AND support a GENERALIZATION" (đưa ra 1 nhận định khái quát + kèm ví dụ cụ thể minh họa từ notes). C chỉ có 1 ví dụ lẻ; B và D chỉ nêu tên 2 loài mà không có tuyên bố khái quát chung. Duy nhất A có đủ Generalization + Support cụ thể!'
    q4['explanation']['optionAnalysis']['A'], q4['explanation']['optionAnalysis']['C'] = q4['explanation']['optionAnalysis']['C'], q4['explanation']['optionAnalysis']['A']

    # Q8: swap C and D
    q8 = questions[7]
    q8['options'][2]['text'], q8['options'][3]['text'] = q8['options'][3]['text'], q8['options'][2]['text']
    q8['correctAnswer'] = 'D'
    q8['explanation']['summaryVi'] = 'Chú ý mệnh đề loại trừ trong Goal: nhấn mạnh hệ thống LỌC NƯỚC (water purification), KHÔNG PHẢI hệ thống hứng nước mưa! A và B tập trung vào việc lát quảng trường hứng mưa; C bỏ qua chức năng lọc nước. Duy nhất D tập trung vào thạch anh + zeolite lọc vi khuẩn và độc tố!'
    q8['explanation']['optionAnalysis']['C'], q8['explanation']['optionAnalysis']['D'] = q8['explanation']['optionAnalysis']['D'], q8['explanation']['optionAnalysis']['C']

    # Q11: swap A and C
    q11 = questions[10]
    q11['options'][0]['text'], q11['options'][2]['text'] = q11['options'][2]['text'], q11['options'][0]['text']
    q11['correctAnswer'] = 'A'
    q11['explanation']['summaryVi'] = 'Mục tiêu: GIẢI THÍCH VÌ SAO loài phát tán chậm gặp rủi ro sinh thái lớn hơn loài phát tán nhanh. B và C không nhắc rủi ro hay loài phát tán chậm; D chỉ mô tả khác biệt hạt. Chỉ A nối trực tiếp tốc độ leo chậm (9m/thập kỷ vs. 42m) → hệ quả rủi ro bị đối thủ vùng thấp cạnh tranh thay thế!'
    q11['explanation']['optionAnalysis']['A'], q11['explanation']['optionAnalysis']['C'] = q11['explanation']['optionAnalysis']['C'], q11['explanation']['optionAnalysis']['A']

    return {
        'schemaVersion': 1,
        'mode': 'drill',
        'section': 'Reading and Writing',
        'basicInfo': {
            'title': 'Drill 3.2: Rhetorical Synthesis — Goal-First Mastery (14 Qs)',
            'subtitle': 'Luyện quy trình Goal-First SOP (≤25 giây/câu) trên đủ 6 dạng Prompt Goal & chống bẫy Fact-Swap Hard Module 2.',
            'difficultyBadge': 'EoI • Target 1500+',
            'targetTimeMinutes': 12,
        },
        'drillModule': {
            'id': 'drill_3_2_mod',
            'title': 'Skill Drill 3.2: Rhetorical Synthesis (Goal-First SOP)',
            'timeLimitMinutes': 12,
            'questions': questions,
        },
    }
