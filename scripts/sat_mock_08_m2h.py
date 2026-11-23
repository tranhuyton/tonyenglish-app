# -*- coding: utf-8 -*-
"""
Full-Length Adaptive Mock Test #8 — Module 2 HARD Route (27 Qs, Hard & Elite 750+, 32 min)
Exact College Board Digital SAT R&W Blueprint.
"""

from sat_drills_1_1_and_2_1 import q_item
from sat_drills_5_4_to_5_5 import svg_bar_chart, html_table


def get_m2h_questions():
    return [
        # --- Q1-Q5: Craft and Structure — Words in Context (Hard / Elite 750+) ---
        q_item(
            'm8_m2h_q1', 1, 'Craft and Structure', 'Words in Context', 'Elite (750+)',
            '<p>Early historians of science often dismissed eleventh-century Andalusian astronomer al-Zarqālī’s universal astrolabe (the <i>ṣafīḥa</i>) as an overly intricate desk curiosity never intended for practical observation, yet pronounced friction marks along the engraved sighting rules of surviving Toledo brass plates ______ that assumption, showing astronomers rotated its double coordinate grid routinely in the field.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            ['buttress', 'confound', 'canonize', 'codify'],
            'B',
            'Contrast Clue: "often dismissed... as an overly intricate desk curiosity never intended for practical observation, yet pronounced friction marks... showing astronomers rotated it routinely" → vết mòn thực tế trên đĩa đồng BÁC BỎ / LÀM ĐẢO LỘN giả định sai lầm của sử gia → "confound" (nghĩa học thuật: prove wrong / refute) → Chọn B!',
            'Nhớ nghĩa thứ cấp 750+ của "confound": KHÔNG chỉ là "gây bối rối", mà trong ngữ cảnh học thuật mang nghĩa "bác bỏ, làm sụp đổ một giả thuyết" (refute / contradict).',
            [
                ('Opposite Meaning', 'buttress = củng cố, chống đỡ — trái ngược hoàn toàn sau liên từ tương phản "yet".'),
                ('Đáp án đúng', 'confound (nghĩa học thuật: bác bỏ, chứng minh giả định là sai) khớp 100% với vết mòn sử dụng thực tế phản bác giả định cũ.'),
                ('Wrong Context', 'canonize = phong thánh / tôn làm kinh điển — sai ngữ cảnh phản bác giả thuyết.'),
                ('Wrong Meaning', 'codify = hệ thống hóa thành bộ luật — không hợp với vết mòn trên đĩa đồng.'),
            ]
        ),
        q_item(
            'm8_m2h_q2', 2, 'Craft and Structure', 'Words in Context', 'Elite (750+)',
            '<p>Because broadly disabling stress-response transcription factors in cereal crops can inadvertently stunt flowering and slash grain weight, sorghum geneticists prefer promoter-targeted CRISPR edits whose physiological effects remain tightly ______, deepening root architecture during soil moisture deficits without perturbing panicle maturation.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            ['ubiquitous', 'amorphous', 'disseminated', 'circumscribed'],
            'D',
            'Contrast + Restatement Clue: đối lập với "broadly disabling... inadvertently stunt flowering" (tác động lan rộng gây hại) + giải thích ngay sau "deepening root architecture... without perturbing panicle maturation" (chỉ tác động hẹp lên rễ mà không đụng tới bông hạt) → ĐƯỢC KHOANH VÙNG CHẶT CHẼ / GIỚI HẠN PHẠM VI → "circumscribed" (D)!',
            'Đối lập với "broadly" (lan rộng) + vế sau "chỉ làm X mà không ảnh hưởng Y" → chọn "circumscribed" (giới hạn chặt trong phạm vi cụ thể).',
            [
                ('Opposite Meaning', 'ubiquitous = có mặt khắp nơi — trái hoàn toàn với tác động khu trú chỉ ở rễ.'),
                ('Wrong Meaning', 'amorphous = vô định hình, mơ hồ — trái với tính chính xác có kiểm soát ("tightly").'),
                ('Opposite Meaning', 'disseminated = phát tán rộng rãi — ngược với mục tiêu cô lập tác động chỉnh sửa gen.'),
                ('Đáp án đúng', 'circumscribed = được khoanh vùng, giới hạn chặt chẽ — khớp hoàn hảo vế "deepening root architecture without perturbing panicle maturation".'),
            ]
        ),
        q_item(
            'm8_m2h_q3', 3, 'Craft and Structure', 'Words in Context', 'Elite (750+)',
            '<p>Although eighteenth-century reviewers originally brushed aside the fictional correspondence in <i>The Salt-Merchant’s Ward</i> (1768) as lighthearted salon gossip, contemporary feminist scholars reveal how the protagonist’s seemingly ______ remarks about tea tariffs, silk ribbons, and parish weddings quietly chronicle the legal precarity of unmarried women.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            ['innocuous', 'incendiary', 'pedantic', 'trenchant'],
            'A',
            'Contrast Clue kép: "seemingly ______ remarks about tea tariffs, silk ribbons... quietly chronicle the legal precarity" → Vẻ ngoài TƯỞNG CHỪNG VÔ HẠI / TẦM PHÀO ("lighthearted salon gossip") nhưng ẩn sau lại ghi chép sắc sảo thực trạng pháp lý bấp bênh → "innocuous" (A)! Bẫy D ("trenchant" = sắc bén) mô tả tầng nghĩa sâu chứ KHÔNG mô tả vẻ ngoài "seemingly..." về giá trà và ruy-băng!',
            'Chú ý trạng từ "seemingly" (tưởng chừng như): từ điền vào phải phản ánh VẺ BỀ NGOÀI nhẹ nhàng vô hại (khớp "lighthearted gossip"), đối lập với chiều sâu phê phán thực sự phía sau!',
            [
                ('Đáp án đúng', 'innocuous = vô hại, tưởng chừng vô thưởng vô phạt — khớp tuyệt đối cấu trúc "seemingly innocuous... quietly chronicle precarity".'),
                ('Opposite Meaning', 'incendiary = kích động, nảy lửa — trái ngược với vẻ ngoài "lighthearted salon gossip" và "quietly".'),
                ('Wrong Tone', 'pedantic = học phiệt, khoe chữ — không khớp chuyện phiếm giá trà, ruy-băng, đám cưới.'),
                ('Layer Trap (Depth vs. Surface)', 'trenchant = sắc bén sâu cay — mô tả tầng nghĩa ẩn chứ không phải vẻ ngoài "seemingly..." tưởng chừng nhẹ bẫng.'),
            ]
        ),
        q_item(
            'm8_m2h_q4', 4, 'Craft and Structure', 'Words in Context', 'Hard',
            '<p>While Reykjavík’s geothermal heating utility shields residents from volatile global natural-gas markets, energy economists offer only a ______ endorsement of replicating Iceland’s district-heating blueprint abroad, noting that municipalities lacking shallow volcanic fracture zones face prohibitive deep-drilling capital costs.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            ['categorical', 'disdainful', 'qualified', 'perfunctory'],
            'C',
            'Contrast + Reasoning Clue: dù công nhận lợi ích chống sốc giá khí đốt của Reykjavík, các nhà kinh tế chỉ đưa ra sự ủng hộ CÓ ĐIỀU KIỆN / DÈ DẶT ("only a ______ endorsement... noting that municipalities lacking shallow volcanic fracture zones face prohibitive costs") → Nghĩa thứ cấp học thuật của "qualified" = limited / conditional / accompanied by reservations → Chọn C!',
            'Nắm chắc nghĩa thứ cấp 750+ của "qualified": KHÔNG phải "đủ trình độ", mà là "có giới hạn, đi kèm điều kiện/dè dặt" ("a qualified endorsement").',
            [
                ('Too Extreme / Opposite', 'categorical = tuyệt đối, không kèm ngoại lệ — trái hoàn toàn với cảnh báo chi phí khoan sâu quá đắt ở nơi thiếu đứt gãy núi lửa.'),
                ('Too Extreme (Wrong Polarity)', 'disdainful = khinh miệt — mâu thuẫn với danh từ "endorsement" (sự ủng hộ).'),
                ('Đáp án đúng', 'qualified (nghĩa thứ cấp: có điều kiện, hạn chế kèm bảo lưu) khớp chuẩn xác với sự ủng hộ có nêu rào cản địa chất.'),
                ('Wrong Meaning', 'perfunctory = qua loa chiếu lệ — các nhà kinh tế phân tích chi phí vốn rất cẩn trọng, không qua loa.'),
            ]
        ),
        q_item(
            'm8_m2h_q5', 5, 'Craft and Structure', 'Words in Context', 'Elite (750+)',
            '<p>Spectrogram studies indicate that wild gelada monkeys produce lip-smacking "wobble" vocalizations whose rapid rhythmic cadence closely mirrors the syllable rate of human speech; however, evolutionary morphologists warn that convergent acoustic patterns can emerge independently across distant lineages, rendering evolutionary claims based on vocal rhythm alone notoriously ______.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            ['irrefutable', 'axiomatic', 'unanimous', 'equivocal'],
            'D',
            'Cause-Effect Clue: vì mô thức âm học giống nhau có thể phát sinh độc lập qua tiến hóa hội tụ (chứ không nhất thiết do chung tổ tiên), nên các kết luận tiến hóa chỉ dựa trên nhịp giọng vốn dĩ MƠ HỒ / ĐA NGHĨA / KHÔNG NGÃ NGŨ → "equivocal" (D)!',
            'Ba đáp án A (irrefutable = không thể bác bỏ), B (axiomatic = hiển nhiên), C (unanimous = đồng thuận tuyệt đối) đều mang nghĩa chắc chắn 100% — chỉ duy nhất D ("equivocal" = lấp lửng, không khẳng định chắc chắn được) khớp với lời cảnh báo khoa học!',
            [
                ('Opposite Meaning', 'irrefutable = không thể bác bỏ — ngược hoàn toàn với lời cảnh báo về tiến hóa hội tụ.'),
                ('Opposite Meaning', 'axiomatic = hiển nhiên như tiên đề — trái nghĩa hoàn toàn.'),
                ('Wrong Meaning', 'unanimous = nhất trí hoàn toàn — mâu thuẫn với sự tranh cãi của các nhà hình thái học tiến hóa.'),
                ('Đáp án đúng', 'equivocal = mơ hồ, có thể diễn giải theo nhiều hướng không dứt khoát — khớp trọn logic tiến hóa hội tụ làm mờ suy luận nguồn gốc.'),
            ]
        ),

        # --- Q6-Q7: Craft and Structure — Text Structure and Purpose ---
        q_item(
            'm8_m2h_q6', 6, 'Craft and Structure', 'Text Structure and Purpose', 'Hard',
            '<p>For nearly a century and a half, biology textbooks defined Arctic and boreal lichens as a strictly two-partner symbiosis: one filamentous ascomycete fungus providing structural shelter and one photosynthetic alga or cyanobacterium supplying sugars. Yet in 2016, metagenomic sequencing of hair lichens across Montana and Norway uncovered a third embedded partner—a single-celled basidiomycete yeast living within the outer fungal cortex. <u>Subsequent assays comparing chemically identical lichen thalli showed that specimens abundant in this cortex yeast produced high concentrations of vulpinic acid, a vivid yellow ultraviolet shield, whereas yeast-depleted specimens remained pale and vulnerable to radiation damage.</u> The finding compelled mycologists to reclassify lichens not as binary pairs, but as miniature multi-kingdom ecosystems.</p>',
            'Which choice best describes the function of the underlined sentence in the text as a whole?',
            [
                'It provides experimental evidence of a concrete physiological function performed by the newly discovered cortex yeast, reinforcing the argument that lichens operate as multi-partner systems.',
                'It challenges the validity of the 2016 metagenomic sequencing data by showing that vulpinic acid is synthesized solely by photosynthetic algae.',
                'It explains why Arctic and boreal lichens are unable to survive outside Montana and Norway.',
                'It summarizes the nineteenth-century consensus that filamentous fungi shelter photosynthetic algae.'
            ],
            'A',
            'Câu 2 nêu phát hiện đối tác thứ ba (nấm men basidiomycete nằm trong lớp vỏ). Câu gạch chân trình bày kết quả so sánh đối chứng cho thấy nấm men này giữ vai trò sinh lý thực sự (tạo axit vulpinic chắn tia cực tím; mẫu thiếu nấm men thì nhợt nhạt và dễ tổn thương bức xạ) — từ đó củng cố kết luận ở câu cuối rằng địa y là hệ sinh thái đa đối tác chứ không phải cặp đôi hai loài → Chọn A!',
            'Trong mạch khoa học [Phát hiện cấu trúc mới → Câu gạch chân → Kết luận đổi phân loại], câu gạch chân đóng vai trò chứng minh TÁC DỤNG SINH LÝ THỰC SỰ của nhân tố mới phát hiện!',
            [
                ('Đáp án đúng', 'Đưa bằng chứng đối chứng về vai trò sinh lý cụ thể (tạo lớp chắn UV vulpinic acid) của nấm men vỏ, củng cố mô hình đa đối tác.'),
                ('Contradiction', 'Câu gạch chân khẳng định mẫu giàu nấm men mới tạo nhiều vulpinic acid, củng cố (không hề bác bỏ) dữ liệu năm 2016.'),
                ('Out of Scope / Distortion', 'Montana và Na Uy chỉ là nơi thu mẫu giải trình tự, không nói địa y không sống được nơi khác.'),
                ('Misplaced Detail', 'Quan niệm thế kỷ 19 nằm ở câu 1, không phải câu gạch chân.'),
            ]
        ),
        q_item(
            'm8_m2h_q7', 7, 'Craft and Structure', 'Text Structure and Purpose', 'Elite (750+)',
            '<p>Art conservators monitoring the celebrated vermilion frescoes inside Pompeii’s Villa of the Mysteries have long struggled to explain why vibrant red cinnabar panels mysteriously darken into patchy gray-black crusts after excavation. For decades, restoration manuals blamed atmospheric chlorine alone, hypothesizing that sea salt slowly converted red mercuric sulfide into a stable black mineral called metacinnabar. Recent synchrotron X-ray micro-spectroscopy on microscopic wall flakes, however, detected virtually no metacinnabar; instead, researchers traced the blackening to metallic mercury nanoparticles formed when bright gallery lighting triggers photochemical reactions at humid junctions between cinnabar grains and chloride-rich lime plaster. In response, museum curators have lowered gallery light wavelengths and strictly stabilized relative humidity across exposed Pompeiian chambers.</p>',
            'Which choice best describes the overall structure of the text?',
            [
                'It introduces a debate over which Roman workshop painted the Villa of the Mysteries, evaluates stylistic clues, and attributes the panels to a specific painter.',
                'It chronicles the chronological excavation of Pompeii since the eighteenth century and recommends halting further archaeological digs.',
                'It presents a persistent art-conservation mystery, outlines an earlier chemical hypothesis, details spectroscopic evidence that revises the causal mechanism, and notes the resulting shift in preservation practices.',
                'It compares the durability of Pompeiian cinnabar with that of ancient Maya pigments and argues that volcanic humidity preserves red minerals indefinitely.'
            ],
            'C',
            'Tách 4 chặng mạch văn cực rõ: [1] Nêu bài toán bảo tồn kéo dài (tại sao mảng thần sa đỏ bị hóa đen sau khai quật) → [2] Trình bày giả thuyết hóa học cũ (đổ cho clo tạo metacinnabar) → [3] Dữ liệu quang phổ synchrotron bác bỏ metacinnabar và chỉ ra cơ chế mới (hạt nano thủy ngân kim loại sinh ra do phản ứng quang hóa dưới ánh đèn + ẩm muối) → [4] Hệ quả thực tiễn trong bảo tồn (hạ bước sóng đèn & ổn định độ ẩm phòng trưng bày) → Khớp chuẩn từng nhịp với C!',
            'Đối chiếu trình tự 4 câu của đoạn văn với đúng chuỗi động từ cấu trúc trong đáp án: presents mystery → outlines earlier hypothesis → details revising evidence → notes preservation shift!',
            [
                ('Out of Scope', 'Hoàn toàn không tranh luận về tác giả hay xưởng vẽ nào tạo nên bức bích họa.'),
                ('Out of Scope', 'Không trình bày lịch sử khai quật từ thế kỷ 18 hay đề xuất dừng khai quật.'),
                ('Đáp án đúng', 'Khớp tuần tự 100% bốn chặng logic của đoạn văn từ bí ẩn bảo tồn đến điều chỉnh quy trình bảo quản.'),
                ('Contradiction / Out of Scope', 'Không nhắc đến màu vẽ Maya; độ ẩm lại thúc đẩy (không phải bảo vệ) sự biến đen.'),
            ]
        ),

        # --- Q8: Craft and Structure — Cross-Text Connections ---
        q_item(
            'm8_m2h_q8', 8, 'Craft and Structure', 'Cross-Text Connections', 'Elite (750+)',
            '<p><b>Text 1</b><br/>Literary theorist Dr. Valeria Orozco contends that the political power of mid-twentieth-century Latin American magical realism resides chiefly in its deadpan narrative posture: by presenting impossible occurrences without hesitation or explanation, authors compel European-trained readers to question the authority of Western scientific rationalism.</p><p><b>Text 2</b><br/>Comparative scholar Dr. Tomás Echeverría agrees that matter-of-fact narration sharply distinguishes magical realism from Gothic fantasy, yet warns that reducing the genre to a philosophical rebuttal of European rationalism obscures the specific local traditions—from Andean oral cosmologies to regional memories of plantation labor—that actually animate individual writers’ imagery.</p>',
            'Based on the texts, how would Dr. Tomás Echeverría (Text 2) most likely respond to Dr. Valeria Orozco’s argument (Text 1)?',
            [
                'By rejecting the claim that Latin American magical realism uses matter-of-fact narration to describe impossible events.',
                'By conceding that deadpan narration is a defining stylistic feature of magical realism, while arguing that Orozco’s framework is overly reductive because it overlooks locally rooted cultural and historical sources.',
                'By asserting that mid-twentieth-century Latin American authors modeled their supernatural imagery directly on nineteenth-century European Gothic fantasy.',
                'By concluding that Andean oral cosmologies had no discernible influence on twentieth-century Latin American fiction.'
            ],
            'B',
            'Quan hệ giữa Text 2 và Text 1 là **ĐỒNG Ý MỘT PHẦN + PHÊ BÌNH GIỚI HẠN (Concession + Qualification)**: Echeverría thừa nhận ("agrees") rằng lối kể thản nhiên không giải thích (deadpan / matter-of-fact narration) đúng là nét nhận diện của dòng văn học này, NHƯNG ("yet warns") việc quy giản nó chỉ thành cuộc phản biện chủ nghĩa duy lý châu Âu sẽ che mờ các truyền thống bản địa cụ thể (vũ trụ quan truyền miệng Andes, ký ức lao động đồn điền) → Chọn B!',
            'Ở câu Cross-Text 750+, cảnh giác với bẫy phủ định cực đoan (A: "rejecting..."). Đọc kỹ cụm nhượng bộ "agrees that..." + "yet warns that reducing..." để chọn phương án cân bằng "conceding X while arguing Y is overly reductive"!',
            [
                ('Overstated Conflict', 'Echeverría ĐỒNG Ý ("agrees") rằng lối kể thản nhiên là đặc trưng phân biệt dòng văn học này.'),
                ('Đáp án đúng', 'Tái hiện chính xác thái độ hai vế của Echeverría: công nhận đặc trưng giọng kể nhưng phê phán góc nhìn của Orozco quá quy giản khi bỏ qua gốc rễ lịch sử–văn hóa bản địa.'),
                ('Contradiction', 'Text 2 nói lối kể thản nhiên PHÂN BIỆT RÕ (sharply distinguishes) hiện thực huyền ảo với Gothic fantasy, không phải bắt chước.'),
                ('Reversed Logic', 'Text 2 nhấn mạnh vũ trụ quan truyền miệng Andes thực sự nuôi dưỡng ("actually animate") hình ảnh của các nhà văn.'),
            ]
        ),

        # --- Q9-Q10: Information and Ideas — Central Ideas and Details ---
        q_item(
            'm8_m2h_q9', 9, 'Information and Ideas', 'Central Ideas and Details', 'Elite (750+)',
            '<p><i>The following text is adapted from an original 1781 epistolary novel,</i> The Lisbon Dispatch<i>. Field botanist Edmund Vance writes from a rainbound Portuguese inn to his aristocratic patron, Lord Hargrave, regarding a shipment of botanical specimens.</i><br/>“Your Lordship will no doubt open Friday’s crate expecting the scarlet cliff-orchid I pledged to procure from the Pernambuco packet; you will discover instead twelve pressed stalks of common coastal fennel. Pray do not mistake this substitution for indolence. Two mornings ago at the quay, I observed Lord Belmore’s private agent purchasing every remaining Brazilian root at thrice its maritime value so that Belmore might unveil the bloom first at Kew. Rather than saddle your purse with a ruinous bidding contest for bruised petals, I spent the rainstorm cataloging a salt-tolerant fennel variety unknown to London herbariums—one that may yet outlast Belmore’s wilted trophy by a century.”</p>',
            'Based on the text, which choice best characterizes Edmund Vance’s explanation to Lord Hargrave?',
            [
                'He apologizes for accidentally misplacing the scarlet cliff-orchids during a coastal storm at the Lisbon quay.',
                'He advises Lord Hargrave to abandon botanical collecting entirely because Lord Belmore controls all trade routes from Brazil.',
                'He boasts that he outbid Lord Belmore’s agent to secure the finest Brazilian specimens for Lord Hargrave’s greenhouse.',
                'He justifies sending an unglamorous but scientifically novel local specimen by arguing that chasing an inflated luxury orchid against a rival patron would have been financially foolish.'
            ],
            'D',
            'Phân tích tầng lập luận tinh tế của bức thư thế kỷ 18: Vance KHÔNG làm mất hoa lan và KHÔNG đấu giá thắng tay sai của Belmore; ông cố tình không lao vào cuộc đấu giá đắt gấp 3 lần cho mấy cánh hoa dập nát ("bruised petals") nhằm tránh gây thiệt hại tài chính cho chủ nhân ("saddle your purse with a ruinous bidding contest"), mà thay vào đó thu thập giống thì là chịu mặn chưa từng có ở phòng tiêu bản London — giản dị nhưng có giá trị khoa học bền vững hơn ("outlast Belmore’s wilted trophy by a century") → Chọn D!',
            'Trong văn xuôi thư tín thế kỷ 18, chú ý nghệ thuật thuyết phục khéo léo: từ chối chi phí vô nghĩa ("ruinous bidding contest") và nâng tầm giá trị khoa học lâu dài của mẫu vật thay thế ("unknown to London herbariums").',
            [
                ('Fact Distortion', 'Ông chủ động thay thế mẫu vật chứ không hề làm thất lạc hoa lan trong cơn bão.'),
                ('Too Extreme', 'Vance vẫn tiếp tục thu thập tiêu bản cho Hargrave và không hề khuyên chủ từ bỏ thú chơi thực vật học.'),
                ('Reversed Logic', 'Vance chủ động KHÔNG tham gia cuộc đấu giá với đại diện của Lord Belmore.'),
                ('Đáp án đúng', 'Bắt trọn lý lẽ tài chính lẫn giá trị khoa học bền vững mà Vance dùng để thuyết phục bá tước Hargrave.'),
            ]
        ),
        q_item(
            'm8_m2h_q10', 10, 'Information and Ideas', 'Central Ideas and Details', 'Hard',
            '<p>Most modern summaries celebrate eleventh-century polymath Ibn al-Haytham primarily for proving that physical light enters the eye rather than radiating outward from it. Yet historians of cognitive science point out that his <i>Book of Optics</i> advanced an equally radical psychological thesis: raw visual sensations hitting the eye’s crystalline humor remain meaningless patches of color and brightness until the mind performs rapid, unconscious acts of comparative judgment (<i>tamyīz</i>). To illustrate this mental layer, Ibn al-Haytham analyzed the familiar Moon Illusion—why the full moon appears substantially larger near a tree-lined horizon than high overhead—contending that the eye receives virtually identical optical angles in both positions, but the brain subconsciously scales up the horizon moon after gauging the intervening terrain stretching into the distance.</p>',
            'Which choice best states the main idea of the text?',
            [
                'Ibn al-Haytham proved that the full moon physically expands when passing behind dense forests along Earth’s horizon.',
                'Beyond his famous optical physics, Ibn al-Haytham pioneered the insight that human vision relies on unconscious cognitive inference, which he used to explain perceptual illusions such as the apparent enlargement of the horizon moon.',
                'Modern historians of cognitive science reject Ibn al-Haytham’s physical theory of light in favor of ancient Greek visual geometry.',
                'The Moon Illusion occurs primarily because the eye’s crystalline humor bends light rays at wider angles near the horizon than overhead.'
            ],
            'B',
            'Ý chính toàn đoạn xoay quanh chữ "Yet": Ngoài thành tựu vật lý ánh sáng nổi tiếng, cuốn *Book of Optics* của Ibn al-Haytham còn đưa ra luận điểm tâm lý học táo bạo rằng thị giác cần suy luận so sánh vô thức của não bộ (*tamyīz*), minh họa sắc nét qua việc giải thích Ảo giác Mặt Trăng ở đường chân trời (góc quang học gần như y hệt, nhưng não bộ phóng đại kích thước dựa trên địa hình trung gian) → Chọn B!',
            'Đọc kỹ câu mở đầu "Most modern summaries celebrate X. Yet... advanced an equally radical thesis Y" — ý chính luôn nằm ở vế sau "Yet" cộng với ví dụ minh họa của nó!',
            [
                ('Literal Absurdity', 'Mặt trăng không hề giãn nở vật lý; góc quang học tới mắt gần như giống hệt nhau.'),
                ('Đáp án đúng', 'Khái quát đầy đủ cả hai mảnh ghép trọng tâm: đóng góp tiên phong về suy luận nhận thức vô thức và ứng dụng giải thích Ảo giác Mặt Trăng.'),
                ('Contradiction', 'Các sử gia khoa học nhận thức ca ngợi thêm chiều sâu tâm lý học của ông chứ không bác bỏ vật lý ánh sáng của ông.'),
                ('Contradiction', 'Bài khẳng định mắt nhận góc quang học "virtually identical" ở cả hai vị trí — hiện tượng là do não bộ, không phải do thấu kính mắt bẻ cong góc rộng hơn.'),
            ]
        ),

        # --- Q11-Q12: Information and Ideas — Command of Evidence (Textual) ---
        q_item(
            'm8_m2h_q11', 11, 'Information and Ideas', 'Command of Evidence (Textual)', 'Elite (750+)',
            '<p>In a landmark physiological model of alpine treeline formation, forest ecologists proposed that the abrupt upper altitude boundary of European larch trees across Swiss valleys is enforced exclusively by a thermal floor: wherever growing-season root-zone soil temperatures fall below 6.5°C, tree meristem cells cannot divide rapidly enough to construct woody trunks, regardless of how much sunlight or rainfall reaches the slope.</p>',
            'Which finding from a field study in the Swiss Alps, if true, would most directly weaken the ecologists’ model?',
            [
                'European larch trees growing at 1,800 meters produce thicker annual growth rings during warm, sunny summers than during unusually cold, cloudy summers.',
                'Soil sensors buried along shaded north-facing slopes at 2,550 meters recorded average growing-season temperatures of 5.2°C and zero naturally established larch trees.',
                'Experimental plots at 2,400 meters where growing-season soil temperatures averaged 7.8°C remained entirely treeless until researchers erected wire enclosures keeping out grazing alpine ibex and marmots, after which transplanted larch saplings formed sturdy woody trunks within three summers.',
                'Laboratory tests confirm that European larch seeds germinate more rapidly at 15°C than at 4°C when grown in sterilized greenhouse trays.'
            ],
            'C',
            'Khóa mệnh đề cần WEAKEN: Ranh giới đường cây mọc trên núi cao bị quyết định **DUY NHẤT (exclusively)** bởi ngưỡng nhiệt độ đất 6.5°C! Để đánh sập thuyết "độc nhất nhiệt độ", cần chứng minh có nơi ĐẠT DƯ NHỆT ĐỘ ĐẤT (>6.5°C) nhưng vẫn không có cây — và nguyên nhân thực sự là yếu tố khác! Đáp án C cực sắc: ở độ cao 2.400m có nhiệt độ đất trung bình tới 7.8°C (>6.5°C) nhưng vẫn trơ trụi hoàn toàn, cho tới khi dựng rào chắn sơn dương ibex & sóc marmot gặm phá thì cây non lập tức tạo thân gỗ khỏe mạnh chỉ sau 3 mùa hè → Trực tiếp bác bỏ giả thuyết giới hạn độc quyền do nhiệt độ đất! Chọn C!',
            'Mỗi khi giả thuyết chứa từ tuyệt đối ("enforced exclusively by X threshold"), bằng chứng phản bác mạnh nhất là trường hợp thỏa mãn dư điều kiện X (>6.5°C) nhưng vẫn thất bại do biến thứ hai (động vật gặm cỏ)!',
            [
                ('Supports / Consistent', 'Vòng năm dày hơn vào hè ấm ở độ cao 1.800m phù hợp với (không bác bỏ) mô hình nhiệt độ.'),
                ('Supports Model', 'Đất lạnh 5.2°C (<6.5°C) và không có cây là bằng chứng ỦNG HỘ mô hình, hoàn toàn ngược yêu cầu WEAKEN.'),
                ('Đáp án đúng', 'Bác bỏ trực diện chữ "exclusively": đất ấm tới 7.8°C nhưng chỉ mọc được thân gỗ khi rào chắn động vật ăn cỏ gặm phá.'),
                ('Irrelevant Scope', 'Tốc độ nảy mầm hạt trong nhà kính 15°C vs 4°C không phủ nhận ngưỡng 6.5°C ngoài tự nhiên.'),
            ]
        ),
        q_item(
            'm8_m2h_q12', 12, 'Information and Ideas', 'Command of Evidence (Textual)', 'Elite (750+)',
            '<p>In a critical study of the original magical-realist poem “Inventory of the Salt-House” by fictional poet Lucía Méndez, a scholar contends that the speaker portrays ancestral grief not as a paralyzing affliction, but as a tangible household craft handed down across generations and reworked into practical shelter.</p>',
            'Which quotation from “Inventory of the Salt-House” most effectively illustrates the scholar’s claim?',
            [
                '“My great-aunts never locked sorrow inside a cedar trunk; they spun its salt threads on the porch loom until grief became the rainproof canvas stretched tight above our beds.”',
                '“Whenever November trade winds rattle the louvered shutters, the whitewashed courtyard walls smell faintly of dried clove and harbor brine.”',
                '“Our grandfather’s pocket watch halted at half past four on the afternoon the railway bridge collapsed, and no watchmaker in the province could persuade its gears to turn again.”',
                '“In the quiet hours before market wagons roll past the plaza, sparrows gather along the fountain rim to drink rainwater left by the night squall.”'
            ],
            'A',
            'Checklist 2 vế từ Claim: [1] Nỗi đau tổ tiên KHÔNG làm tê liệt ("not as a paralyzing affliction") + [2] Là một NGHỀ THỦ CÔNG HỮU HÌNH được truyền lại và biến thành MÁI CHE THỰC TIỄN ("tangible household craft... reworked into practical shelter"). B, C, D chỉ tả hương vị sân nhà, chiếc đồng hồ ngừng chạy (biểu tượng bế tắc!), hoặc chim sẻ uống nước. Duy nhất A chuyển hóa nỗi buồn thành sợi muối dệt trên khung cửi thành tấm bạt chống mưa căng trên giường ngủ → Chọn A!',
            'Kiểm tra khớp từng ẩn dụ cốt lõi của Claim: "not paralyzing" (never locked sorrow) + "craft" (spun on the porch loom) + "practical shelter" (rainproof canvas stretched above our beds)!',
            [
                ('Đáp án đúng', 'Minh họa xuất sắc cả ba yếu tố: nỗi đau không bị đóng kín tê liệt mà được dệt thành tấm bạt che mưa thiết thực cho gia đình.'),
                ('Atmosphere Only', 'Chỉ miêu tả mùi đinh hương và hơi muối biển, không đề cập nỗi đau hay nghề thủ công.'),
                ('Opposite Implication', 'Chiếc đồng hồ ngừng vĩnh viễn tượng trưng cho sự đông cứng tê liệt — ngược hẳn luận điểm của học giả.'),
                ('Irrelevant Imagery', 'Chỉ là hình ảnh chim sẻ uống nước mưa buổi sáng sớm.'),
            ]
        ),

        # --- Q13-Q14: Information and Ideas — Command of Evidence (Quantitative) ---
        q_item(
            'm8_m2h_q13', 13, 'Information and Ideas', 'Command of Evidence (Quantitative)', 'Elite (750+)',
            svg_bar_chart(
                'Mean Acoustic Attenuation (dB Loss per 100 m) Across Dense Rainforest Canopy',
                ['0', '15', '30', '45', '60'],
                [('0.4 kHz (Territ.)', 11, '11 dB'), ('1.2 kHz (Territ.)', 16, '16 dB'), ('3.5 kHz (Alarm)', 31, '31 dB'), ('6.0 kHz (Alarm)', 48, '48 dB')],
                60
            ) + '<p>Bioacousticians studying arboreal primates argue that dense rainforest foliage creates two distinct evolutionary signaling niches: long-distance territorial calls cluster inside a low-frequency "sound window" (0.4–1.2 kHz) where acoustic loss remains minimal, whereas close-range predator alarms operate at much higher frequencies (3.5–6.0 kHz) whose steep attenuation advantageously prevents distant rival troops from eavesdropping. Data from canopy transmission trials support both halves of this acoustic trade-off: ______</p>',
            'Which choice most effectively uses data from the graph to complete the text?',
            [
                'across all four tested frequencies, sound waves lost at least 11 decibels per 100 meters while traveling through dense rainforest foliage.',
                'territorial calls broadcast at 1.2 kHz experienced 5 decibels more attenuation per 100 meters than territorial calls broadcast at 0.4 kHz.',
                'predator alarms at 6.0 kHz attenuated at a rate of 48 decibels per 100 meters, which was 17 decibels higher than the attenuation observed at 3.5 kHz.',
                'whereas territorial frequencies at 0.4 kHz and 1.2 kHz suffered modest losses of only 11 dB and 16 dB per 100 meters, alarm frequencies at 3.5 kHz and 6.0 kHz dropped sharply by 31 dB and 48 dB per 100 meters—roughly two to four times the attenuation of the low-frequency window.'
            ],
            'D',
            'Khóa yêu cầu hỗ trợ CẢ HAI VẾ của sự đánh đổi âm học ("support both halves of this acoustic trade-off"): [1] Vùng tần số thấp (0.4–1.2 kHz) suy hao cực thấp (11 & 16 dB) + [2] Vùng tần số cao (3.5–6.0 kHz) suy hao tăng vọt (31 & 48 dB — gấp khoảng 2 đến 4 lần vùng thấp: 31 ≈ 2×16, 48 ≈ 3×16 và >4×11 ✓). B và C chỉ so sánh nội bộ trong 1 nhóm; A quá chung chung không tách 2 vùng tần số! Duy nhất D đối chiếu trọn vẹn cả 2 nhóm cùng tỷ lệ chênh lệch chính xác!',
            'Gặp yêu cầu "support BOTH halves", loại ngay các đáp án chỉ so sánh nội bộ trong 1 nửa (B: 0.4 vs 1.2; C: 3.5 vs 6.0) và kiểm tra phép nhân tỷ lệ ở đáp án đối chiếu liên nhóm (D)!',
            [
                ('Too General / Misses Contrast', 'Chỉ nêu mức suy hao tối thiểu 11 dB chung cho cả 4 tần số, bỏ qua độ chênh khổng lồ giữa hai vùng tần số.'),
                ('Within-Group Only', 'Chỉ so sánh nội bộ vùng tần số thấp (0.4 vs 1.2 kHz), thiếu hoàn toàn nửa tần số cao.'),
                ('Within-Group Only', 'Chỉ so sánh nội bộ vùng báo động cao (3.5 vs 6.0 kHz), thiếu hoàn toàn nửa tần số thấp.'),
                ('Đáp án đúng', 'Đối chiếu chính xác cả hai vùng tần số (11 & 16 dB so với 31 & 48 dB) kèm tỷ lệ gấp 2–4 lần chuẩn xác.'),
            ]
        ),
        q_item(
            'm8_m2h_q14', 14, 'Information and Ideas', 'Command of Evidence (Quantitative)', 'Elite (750+)',
            html_table(
                'Table 2. Field Performance of Four CRISPR-Edited Sorghum Lines by Leaf Stomatal Density',
                ['Sorghum Genotype', 'Stomatal Density (per mm²)', 'Irrigated Yield (t/ha)', 'Drought Yield (t/ha)', 'Water-Use Efficiency (g/L)'],
                [
                    ['Control (WT)', '142', '6.4', '2.6', '1.8'],
                    ['Line S-15', '118', '6.3', '3.5', '2.5'],
                    ['Line S-30', '96', '6.1', '4.2', '3.2'],
                    ['Line S-55', '62', '4.7', '2.9', '2.8'],
                ]
            ) + '<p>Crop physiologist Dr. Kwame Mensah contends that using CRISPR to reduce leaf stomatal density boosts drought grain yields only up to an optimal threshold, beyond which stripping away too many leaf pores restricts carbon dioxide intake so severely that grain yields drop sharply under both irrigated and drought conditions.</p>',
            'Which choice most effectively uses data from the table to support Dr. Kwame Mensah’s contention?',
            [
                'Control (WT) recorded the highest stomatal density (142 per mm²) and the highest irrigated yield (6.4 t/ha) in the experiment.',
                'Lowering stomatal density from 142 per mm² (Control) to 96 per mm² (Line S-30) raised drought yield from 2.6 to 4.2 t/ha while keeping irrigated yield nearly steady (6.4 vs. 6.1 t/ha), whereas cutting density further to 62 per mm² (Line S-55) depressed both irrigated yield (4.7 t/ha) and drought yield (2.9 t/ha).',
                'Line S-15 achieved a higher drought yield (3.5 t/ha) and greater water-use efficiency (2.5 g/L) than Control (WT) did (2.6 t/ha and 1.8 g/L).',
                'All three CRISPR-edited sorghum lines produced higher drought yields and higher water-use efficiency than the unedited Control (WT) genotype.'
            ],
            'B',
            'Khóa quy luật **ĐẢO CHIỀU QUA NGƯỠNG TỐI ƯU (Optimal Threshold Reversal)**: [1] Giảm mật độ khí khổng vừa phải (142 → 118 → 96 ở Line S-30) giúp tăng mạnh năng suất hạn (2.6 → 4.2 t/ha) mà năng suất tưới gần như giữ nguyên (6.4 → 6.1); [2] Giảm quá sâu xuống 62 (Line S-55) làm CẢ năng suất tưới (6.1 → 4.7) LẪN năng suất hạn (4.2 → 2.9) cùng lao dốc! A, C, D đều đúng số liệu nhưng không chỉ ra sự đảo chiều sụt giảm từ S-30 sang S-55! Duy nhất B chứng minh đủ cả pha tăng tới ngưỡng tối ưu lẫn pha sụt giảm sau ngưỡng!',
            'Với giả thuyết có "optimal threshold, beyond which...", đáp án đúng BẮT BUỘC phải chỉ ra đỉnh tối ưu (S-30: 96/mm²) rồi đối chiếu cú rơi đồng thời của cả hai cột năng suất khi vượt quá ngưỡng đó (S-55: 62/mm²)!',
            [
                ('True Data / Wrong Claim', 'Chỉ nêu số liệu gốc của Control (WT), không chứng minh xu hướng tăng rồi đảo chiều.'),
                ('Đáp án đúng', 'Trình bày chính xác đỉnh tối ưu tại S-30 (96/mm² → 4.2 t/ha hạn, 6.1 t/ha tưới) và cú sụt giảm kép tại S-55 (62/mm² → 2.9 hạn, 4.7 tưới).'),
                ('Half-Trend Trap', 'Chỉ nêu pha tăng từ WT sang S-15, bỏ sót hoàn toàn cú đảo chiều giảm sút ở S-55.'),
                ('Misses Threshold Drop', 'Đúng là S-55 (2.9) vẫn nhỉnh hơn WT (2.6), nhưng che mất cú sụt mạnh so với S-30 (4.2) và cú giảm nặng ở tưới (6.4 → 4.7).'),
            ]
        ),

        # --- Q15: Information and Ideas — Inferences (Elite 750+) ---
        q_item(
            'm8_m2h_q15', 15, 'Information and Ideas', 'Inferences', 'Elite (750+)',
            '<p>Mineralogical fingerprinting of Late Classic Maya murals and ritual ceramics indicates that virtually all palygorskite clay used to manufacture Maya Blue originated from just two geological deposits in the northern Yucatán Peninsula. Nevertheless, spectroscopists recently identified authentic Maya Blue coatings not only in royal palace murals, but also on modest household incense burners excavated in Guatemalan highland settlements hundreds of kilometers south—including layers dated precisely to decades when hieroglyphic stelae record bitter military hostilities between northern Yucatán dynasties and southern lowland polities. Taken together, these findings most strongly suggest that ______</p>',
            'Which choice most logically completes the text?',
            [
                'northern Yucatán rulers halted all ceramic production whenever military conflicts erupted with southern Maya polities.',
                'Guatemalan highland artisans independently mined local deposits of palygorskite clay without ever importing materials from northern Yucatán.',
                'long-distance exchange networks supplying palygorskite clay or finished Maya Blue pigment extended beyond strictly elite court commissions and persisted even amid political warfare between major dynasties.',
                'hieroglyphic stelae from the Late Classic period consistently fabricated accounts of military conflict between northern and southern Maya cities.'
            ],
            'C',
            'Ghép 3 tiền đề theo 1-Millimeter Rule: (1) Gần như 100% đất sét palygorskite làm màu Maya Blue chỉ đến từ 2 mỏ ở bắc Yucatán; (2) Màu Maya Blue thật vẫn xuất hiện trên cả lư hương hộ gia đình bình dân (modest household incense burners — không chỉ cung điện hoàng gia!) tại cao nguyên Guatemala cách hàng trăm km về phía nam; (3) Hiện diện ngay cả trong các thập kỷ có chiến tranh khốc liệt giữa triều đại bắc Yucatán và các thành bang phía nam ⇒ Kết luận tất yếu: Mạng lưới trao đổi đường dài cung ứng đất sét/bột màu Maya Blue không bị giới hạn trong đơn đặt hàng hoàng gia VÀ vẫn duy trì xuyên qua xung đột quân sự cấp triều đại (C)!',
            'Kiểm tra từng mảnh bằng chứng trong kết luận: "modest household incense burners" → vượt khỏi phạm vi hoàng gia; "hundreds of km south... during military hostilities" → thương mại đường dài vẫn tồn tại bất chấp chiến tranh chính trị!',
            [
                ('Contradiction', 'Bằng chứng màu vẫn được sử dụng rộng rãi trong thời chiến chứng tỏ sản xuất không hề ngừng hẳn.'),
                ('Contradiction', 'Câu 1 nêu rõ gần như toàn bộ đất sét palygorskite xuất phát từ 2 mỏ ở bắc Yucatán, không phải khai thác tại chỗ ở Guatemala.'),
                ('Đáp án đúng', 'Tổng hợp chính xác cả hai hàm ý 1mm: lưu thông vượt phạm vi hoàng gia ("modest household") và bền bỉ bất chấp xung đột giữa các triều đại.'),
                ('Unsupported Leap', 'Không có căn cứ nào kết luận bia ký cổ đại bịa đặt chuyện chiến tranh; thương mại vẫn có thể vận hành song song với chiến tranh.'),
            ]
        ),

        # --- Q16-Q19: Standard English Conventions — Boundaries (Hard / Elite 750+) ---
        q_item(
            'm8_m2h_q16', 16, 'Standard English Conventions', 'Boundaries', 'Hard',
            '<p>Iceland’s national geothermal grid draws high-enthalpy steam from three principal volcanic fields: Hellisheiði, southwest of ______ Lake Þingvallavatn; and Krafla, in the island’s northeastern rift zone.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            [
                'Reykjavík; Nesjavellir, along',
                'Reykjavík, Nesjavellir, along',
                'Reykjavík; Nesjavellir along',
                'Reykjavík, Nesjavellir; along'
            ],
            'A',
            'Quy tắc **Super-Comma (Semicolon List)**: Danh sách 3 địa điểm mà bản thân từng mục đã chứa dấu phẩy nội bộ (`Tên mỏ, vị trí địa lý`): [1] `Hellisheiði, southwest of Reykjavík;` [2] `Nesjavellir, along Lake Þingvallavatn;` [3] `and Krafla, in the island’s northeastern rift zone.` Dấu chấm phẩy sau `Þingvallavatn;` khẳng định đây là danh sách dùng chấm phẩy để tách mục, đồng thời cần dấu phẩy giữa `Nesjavellir` và cụm vị trí `along Lake Þingvallavatn` cho song song cấu trúc → Chọn A!',
            'Nhìn thấy dấu chấm phẩy nằm trước "; and [Mục 3]" trong danh sách phức hợp → Chốt ngay công thức `[Mục 1]; [Tên mục 2], [vị trí 2]; and [Mục 3]`!',
            [
                ('Đáp án đúng', 'Dùng chấm phẩy (;) ngăn rạch ròi mục 1 với mục 2, và giữ dấu phẩy nội bộ sau "Nesjavellir" song song với hai mục còn lại.'),
                ('Ambiguous Comma List', 'Dùng dấu phẩy sau "Reykjavík" làm lẫn lộn ranh giới giữa mục 1 và mục 2 trong danh sách đã có chấm phẩy.'),
                ('Missing Internal Comma', 'Thiếu dấu phẩy ngăn cách tên "Nesjavellir" với cụm vị trí bổ sung "along Lake Þingvallavatn".'),
                ('Misplaced Semicolon', 'Đặt chấm phẩy cắt ngang giữa tên mỏ "Nesjavellir" và vị trí của chính nó ("along...").'),
            ]
        ),
        q_item(
            'm8_m2h_q17', 17, 'Standard English Conventions', 'Boundaries', 'Elite (750+)',
            '<p>Ibn al-Haytham’s spherical-mirror reflection problem resisted classical compass-and-straightedge ______ he derived an exact geometric construction by intersecting a circle with a hyperbola.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['methods, however,', 'methods, however;', 'methods; however', 'methods; however,'],
            'D',
            'Xác định 2 mệnh đề độc lập (IC): IC 1 = "Ibn al-Haytham’s spherical-mirror reflection problem resisted classical compass-and-straightedge methods." IC 2 = "he derived an exact geometric construction by intersecting a circle with a hyperbola." Từ nối trạng từ (Conjunctive Adverb) `however` mang ý tương phản cho vế 2 (dù phương pháp cổ điển bó tay, TUY NHIÊN ông vẫn dựng được lời giải bằng giao điểm đường tròn và hyperbol) → Công thức chuẩn: `IC 1; however, IC 2` → Chọn D!',
            'Phân biệt sống còn giữa `IC; however, IC` (D) và `IC, however; IC` (B): kiểm tra `however` thuộc chiều tương phản của câu 1 hay câu 2! Ở đây câu 1 là câu mở đầu chưa tương phản với câu nào trước đó, nên `however` BẮT BUỘC mở đầu cho IC 2 (`; however,`)!',
            [
                ('Comma Splice with However', '", however," giữa hai IC là lỗi Comma Splice kinh điển hay bẫy thí sinh 700+!'),
                ('Wrong Clause Attachment', '", however;" gán "however" về phía IC 1 — sai logic vì IC 1 là câu đầu đoạn, không tương phản với câu nào trước nó.'),
                ('Missing Comma After Adverb', 'Thiếu dấu phẩy sau trạng từ liên kết "however" đứng đầu IC 2.'),
                ('Đáp án đúng', 'Chuẩn mực tuyệt đối `IC 1; however, IC 2` cho trạng từ liên kết mở đầu mệnh đề độc lập thứ hai.'),
            ]
        ),
        q_item(
            'm8_m2h_q18', 18, 'Standard English Conventions', 'Boundaries', 'Elite (750+)',
            '<p>Eighteenth-century epistolary novelists who deliberately planted contradictory dates and forged postscripts inside their fictional ______ readers to scrutinize every narrator’s hidden motives.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['letters, compelled', 'letters compelled', 'letters; compelled', 'letters—compelled'],
            'B',
            'Quy tắc **Vùng Cấm Dấu Phẩy (No-Comma Zone: Subject — Verb)**: Toàn bộ cụm "Eighteenth-century epistolary novelists [who deliberately planted contradictory dates and forged postscripts inside their fictional letters]" là một CHỦ NGỮ dài chứa mệnh đề quan hệ xác định (Restrictive `who`-clause, không có dấu phẩy mở!). Theo sau là động từ chính "compelled" → TUYỆT ĐỐI KHÔNG đặt bất kỳ dấu câu đơn nào cắt giữa chủ ngữ và động từ chính → Chọn B (`letters compelled`)!',
            'Chủ ngữ dài đến mấy nhưng mở bằng `who...` KHÔNG có dấu phẩy mở → TUYỆT ĐỐI KHÔNG được đặt dấu phẩy đóng trước động từ chính ("compelled")!',
            [
                ('Subject-Verb Comma Splice', 'Đặt dấu phẩy đơn cắt đứt chủ ngữ "novelists..." khỏi động từ chính "compelled".'),
                ('Đáp án đúng', '0 dấu câu — nối thẳng cụm chủ ngữ có mệnh đề quan hệ xác định vào động từ chính "compelled".'),
                ('Semicolon Fragment', 'Dấu chấm phẩy cắt câu thành hai mảnh cụt không hoàn chỉnh.'),
                ('Unpaired Dash', 'Gạch ngang đơn không có cặp mở, làm đứt mạch chủ ngữ–động từ.'),
            ]
        ),
        q_item(
            'm8_m2h_q19', 19, 'Standard English Conventions', 'Boundaries', 'Hard',
            '<p>Conservation physicists inspecting faded wall plaster in Pompeii confirmed ______ microscopic traces of synthetic Egyptian blue emit bright near-infrared luminescence even when the pigment appears completely invisible to the naked eye.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['that:', 'that,', 'that', ', that'],
            'C',
            'Quy tắc **Không dấu câu quanh `that` bổ ngữ**: Động từ ngoại động `confirmed` nối trực tiếp với mệnh đề danh ngữ tân ngữ bắt đầu bằng `that` ("confirmed that microscopic traces... emit...") → CẤM đặt dấu hai chấm, dấu phẩy trước hoặc sau `that` → Chọn C (`that`)!',
            'Nhớ quy tắc vàng Digital SAT: Không bao giờ đặt dấu hai chấm (:) hoặc dấu phẩy (,) ngay sau liên từ phụ thuộc `that` (hoặc ngay sau động từ/giới từ dẫn vào mệnh đề `that`)!',
            [
                ('Colon After Subordinator', 'Cấm đặt dấu hai chấm sau "that" vì "confirmed that" không phải mệnh đề độc lập hoàn chỉnh.'),
                ('Comma After That', 'Không đặt dấu phẩy đơn tách "that" khỏi chủ ngữ mệnh đề phụ "microscopic traces".'),
                ('Đáp án đúng', '0 dấu câu — nối mượt động từ "confirmed" với mệnh đề bổ ngữ "that microscopic traces...".'),
                ('Comma Before That', 'Cấm đặt dấu phẩy giữa động từ chính "confirmed" và tân ngữ trực tiếp "that...".'),
            ]
        ),

        # --- Q20-Q22: Standard English Conventions — Form, Structure, and Sense ---
        q_item(
            'm8_m2h_q20', 20, 'Standard English Conventions', 'Form, Structure, and Sense', 'Elite (750+)',
            '<p>Extending well above the upright conifer canopy along wind-scoured Tibetan slopes ______ low-slung cushions of dwarf juniper and crustose lichen capable of withstanding freezing summer gales.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['thrives', 'has thrived', 'is thriving', 'thrive'],
            'D',
            'Bẫy **Đảo ngữ Chủ ngữ (Inverted Syntax S-V Agreement)** cực đặc trưng của 750+! Cụm phân từ mở đầu "Extending well above the upright conifer canopy along wind-scoured Tibetan slopes" đứng trước động từ; CHỦ NGỮ THẬT đứng NGAY SAU ĐỘNG TỪ là "**low-slung cushions** of dwarf juniper and crustose lichen" (SỐ NHIỀU!). Loại ngay 3 động từ số ít A (`thrives`), B (`has thrived`), C (`is thriving`) → Chốt D (`thrive`)!',
            'Mẹo đảo ngữ & mẹo 3–1: Viết xuôi lại câu ("Low-slung cushions... thrive extending well above...") → Chủ ngữ SỐ NHIỀU + 3 đáp án số ít vs 1 đáp án số nhiều = D chắc chắn 100%!',
            [
                ('Inverted S-V Mismatch', 'thrives là số ít — bẫy nhìn nhầm chủ ngữ nằm trước động từ ("canopy").'),
                ('Inverted S-V Mismatch', 'has thrived là số ít, không khớp chủ ngữ số nhiều "low-slung cushions".'),
                ('Inverted S-V Mismatch', 'is thriving là số ít.'),
                ('Đáp án đúng', 'thrive (hiện tại đơn, số nhiều) khớp hoàn hảo với chủ ngữ đảo ngữ số nhiều "low-slung cushions".'),
            ]
        ),
        q_item(
            'm8_m2h_q21', 21, 'Standard English Conventions', 'Form, Structure, and Sense', 'Elite (750+)',
            '<p>By tracking vocal-tract formants across twenty-four wild white-handed gibbon pairs over three monsoon seasons, ______</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            [
                'bioacoustician Dr. Kenji Sato’s spectrogram archive revealed that mated pairs adjust duet pitch to overcome heavy rain noise.',
                'bioacoustician Dr. Kenji Sato demonstrated that mated pairs shift duet pitch upward to cut cleanly above heavy rain noise.',
                'the territorial duets of mated gibbons were found by Dr. Kenji Sato to shift upward during heavy rainstorms.',
                'rain-driven acoustic shifts in gibbon duets became clear to bioacoustician Dr. Kenji Sato.'
            ],
            'B',
            'Bẫy **Possessive Dangling Modifier** sát thủ ở 750+! Cụm mở đầu "By tracking vocal-tract formants..." đòi hỏi CHỦ THỂ THỰC HIỆN hành động "tracking" (theo dõi) phải đứng làm chủ ngữ thật ngay sau dấu phẩy. Nhìn kỹ A: "Dr. Kenji Sato’s **spectrogram archive**" có danh từ chính là *kho lưu trữ phổ âm* (archive không tự theo dõi vượn được — bẫy sở hữu cách!). C đặt "territorial duets" làm chủ ngữ, D đặt "shifts" làm chủ ngữ. Duy nhất B đặt đúng con người **bioacoustician Dr. Kenji Sato** làm chủ ngữ!',
            'Luôn gạch chân danh từ chính đằng sau sở hữu cách `’s`: `Dr. Sato’s archive` → chủ ngữ là `archive`, KHÔNG phải `Dr. Sato`! Cực hay ra ở Module 2 Hard!',
            [
                ('Possessive Dangling Modifier', 'Chủ ngữ thật ở A là "spectrogram archive" (kho lưu trữ), không thể tự thực hiện hành động "By tracking...".'),
                ('Đáp án đúng', 'Chủ ngữ "bioacoustician Dr. Kenji Sato" là người trực tiếp thực hiện hành động "By tracking vocal-tract formants...".'),
                ('Dangling Modifier', 'Các bản song ca lãnh thổ ("territorial duets") không tự đi đo cộng hưởng thanh quản.'),
                ('Dangling Modifier', 'Những dịch chuyển âm thanh ("shifts") không thể thực hiện hành động theo dõi kéo dài 3 mùa mưa.'),
            ]
        ),
        q_item(
            'm8_m2h_q22', 22, 'Standard English Conventions', 'Form, Structure, and Sense', 'Hard',
            '<p>Long before seventeenth-century European astronomers fitted brass quadrants with telescopic sights, medieval Islamic instrument makers ______ precision trigonometric sine grids onto the backs of pocket astrolabes to solve spherical elevation problems without parchment tables.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['had inscribed', 'have inscribed', 'inscribing', 'are inscribing'],
            'A',
            'Quy tắc **Trình tự thời gian Quá khứ Hoàn thành (Past Perfect)**: Mệnh đề thời gian mở đầu "Long before seventeenth-century European astronomers **fitted**..." đặt một mốc quá khứ đơn (thế kỷ 17). Hành động khắc lưới sin lượng giác của các nghệ nhân Hồi giáo thời Trung Cổ xảy ra **RẤT LÂU TRƯỚC** mốc quá khứ đó → Bắt buộc dùng Quá khứ Hoàn thành (`had inscribed`) → Chọn A!',
            'Gặp mốc "Long before [Past Simple]" + sự kiện hoàn tất trước mốc quá khứ đó → chốt ngay Past Perfect (`had + V3/ed`), loại Hiện tại Hoàn thành (`have + V3/ed`)!',
            [
                ('Đáp án đúng', 'had inscribed (Past Perfect) biểu đạt chính xác hành động đã hoàn tất từ trước mốc quá khứ thế kỷ 17 ("Long before... fitted").'),
                ('Tense Mismatch (Present Perfect)', 'have inscribed nối với hiện tại, xung đột trực tiếp với mốc thời gian lịch sử khép kín "Long before seventeenth-century...".'),
                ('Non-Finite Fragment', 'inscribing là phân từ, khiến mệnh đề chính mất động từ chia thì.'),
                ('Tense Mismatch (Present Progressive)', 'are inscribing là thì hiện tại tiếp diễn, sai hoàn toàn về thời gian lịch sử.'),
            ]
        ),

        # --- Q23-Q25: Expression of Ideas — Transitions (Hard / Elite 750+) ---
        q_item(
            'm8_m2h_q23', 23, 'Expression of Ideas', 'Transitions', 'Elite (750+)',
            '<p>In eighteenth-century epistolary fiction, the physical circulation of letters often carries as much dramatic weight as the personal confessions inked inside them. ______, crucial plot reversals in the genre frequently hinge on broken wax seals, misdirected postbags, or intercepted pages rather than face-to-face confrontations.</p>',
            'Which choice completes the text with the most logical transition?',
            ['Nevertheless', 'Conversely', 'Indeed', 'Consequently'],
            'C',
            'Câu 1 nêu nhận định tổng quát: sự lưu hành vật lý của bức thư mang sức nặng kịch tính ngang với lời bộc bạch bên trong. Câu 2 **CỦNG CỐ & NHẤN MẠNH** nhận định đó bằng minh chứng cụ thể (các bước ngoặt cốt truyện xoay quanh dấu niêm sáp vỡ, túi thư gửi nhầm, trang thư bị chặn) → Chọn từ nối khẳng định tăng cường **"Indeed"** (C)! (Loại `Consequently` vì bước ngoặt xoay quanh dấu sáp không phải *hệ quả* sinh ra từ nhận định ở câu 1 mà là *sự xác thực* câu 1).',
            'Khi Câu 2 xác thực và nhấn mạnh sâu thêm nhận định ở Câu 1 (không phải nguyên nhân–hệ quả, không phải tương phản) → chốt ngay **"Indeed"**!',
            [
                ('False Contrast', 'Nevertheless chỉ sự trái kỳ vọng — sai vì câu 2 hoàn toàn củng cố câu 1.'),
                ('False Contrast', 'Conversely chỉ sự đảo chiều ngược lại.'),
                ('Đáp án đúng', 'Indeed xác thực và tăng cường chính xác nhận định về sức nặng vật lý của bức thư bằng chi tiết cốt truyện cụ thể.'),
                ('False Cause-Effect', 'Các tình tiết niêm sáp vỡ không phải kết quả bị gây ra bởi nhận định câu 1, mà là minh chứng cụ thể cho nhận định đó.'),
            ]
        ),
        q_item(
            'm8_m2h_q24', 24, 'Expression of Ideas', 'Transitions', 'Elite (750+)',
            '<p>Multi-year field trials in southern Mali verified that CRISPR-edited stay-green sorghum hybrids retained active leaf chlorophyll nearly three weeks longer during terminal drought than conventional local varieties. ______, agricultural economists caution that smallholder adoption will remain sluggish unless regional seed cooperatives can reproduce the hybrids affordably without restrictive licensing fees.</p>',
            'Which choice completes the text with the most logical transition?',
            ['Furthermore', 'Accordingly', 'In other words', 'Even so'],
            'D',
            'Câu 1 nêu kết quả sinh học rất ấn tượng (giống cao lương chỉnh sửa gen giữ diệp lục lâu hơn gần 3 tuần trong hạn cuối vụ). Câu 2 đưa ra một **CẢNH BÁO / RÀO CẢN NGƯỢC CHIỀU** về kinh tế (việc nông hộ nhỏ áp dụng vẫn sẽ chậm chạp nếu hợp tác xã giống không thể nhân giống giá rẻ) → Quan hệ Nhượng bộ – Tương phản ("Dù thành tích đồng ruộng xuất sắc như vậy, DẪU SAO...") → Chọn **"Even so"** (D)!',
            'Thành tựu kỹ thuật tích cực ở Câu 1 ↔ Rào cản kinh tế/triển khai ở Câu 2 → luôn dùng nhóm tương phản nhượng bộ (`Even so / Still / Nevertheless / However`)!',
            [
                ('Wrong Relationship (Addition)', 'Furthermore bổ sung ý cùng chiều tích cực — sai khi câu 2 nêu rào cản kìm hãm việc áp dụng.'),
                ('Wrong Relationship (Cause-Effect)', 'Accordingly (= Therefore) sai hoàn toàn vì thành công sinh học không gây ra sự chậm áp dụng.'),
                ('Restatement Trap', 'Câu 2 đưa cảnh báo kinh tế mới chứ không diễn đạt lại kết quả sinh học câu 1.'),
                ('Đáp án đúng', 'Even so diễn đạt chính xác bước ngoặt nhượng bộ: dù hiệu quả chịu hạn rất cao, việc nhân rộng vẫn đối mặt rào cản chi phí bản quyền.'),
            ]
        ),
        q_item(
            'm8_m2h_q25', 25, 'Expression of Ideas', 'Transitions', 'Hard',
            '<p>Ancient Maya painters at Bonampak brushed mineral and organic pigments onto lime plaster that had already cured completely, relying on sticky tree-bark gums to bind each layer onto the dry surface. ______, Roman fresco artisans in Pompeii worked rapidly on freshly troweled damp plaster so that pigments fused chemically into a crystalline calcium carbonate crust as the wall dried.</p>',
            'Which choice completes the text with the most logical transition?',
            ['Therefore', 'By contrast', 'Similarly', 'For instance'],
            'B',
            'Câu 1 mô tả kỹ thuật vẽ trên vữa ĐÃ KHÔ dùng nhựa vỏ cây kết dính (*fresco secco* của người Maya). Câu 2 mô tả kỹ thuật ngược hẳn của người La Mã ở Pompeii: vẽ nhanh trên vữa VỪA TRÁT CÒN ẨM để màu kết tinh hóa học trực tiếp vào lớp canxi cacbonat (*buon fresco*) → Đối chiếu hai kỹ thuật trái ngược → Chọn **"By contrast"** (B)!',
            'So sánh trực diện hai đối tượng có quy trình trái ngược (Maya: dry cured plaster + bark gums ↔ Pompeii: damp fresh plaster + chemical fusion) → chốt **"By contrast"**!',
            [
                ('Wrong Relationship (Cause-Effect)', 'Kỹ thuật của người Maya không hề là nguyên nhân gây ra kỹ thuật của thợ vẽ Pompeii.'),
                ('Đáp án đúng', 'By contrast đối chiếu chuẩn xác hai kỹ thuật vẽ tường trái ngược nhau (vữa khô vs vữa ẩm).'),
                ('Opposite Direction', 'Similarly chỉ sự tương đồng — trái ngược hoàn toàn giữa bề mặt khô và bề mặt ẩm.'),
                ('Wrong Relationship (Example)', 'Thợ vẽ Pompeii không phải ví dụ minh họa cho kỹ thuật vữa khô của người Maya.'),
            ]
        ),

        # --- Q26-Q27: Expression of Ideas — Rhetorical Synthesis (Elite 750+) ---
        q_item(
            'm8_m2h_q26', 26, 'Expression of Ideas', 'Rhetorical Synthesis', 'Elite (750+)',
            '''<p>While researching Icelandic geothermal economics, a student has taken the following notes:</p>
            <ul>
              <li>High-temperature geothermal power plants in Iceland spin steam turbines to generate electricity, but turbine generation alone converts only about 12 to 15 percent of the borehole’s thermal energy into electrical power.</li>
              <li>Rather than venting leftover warm brine (80–120°C) as waste, Icelandic utilities route the residual fluid through "cascaded" thermal applications.</li>
              <li>First-stage residual hot water heats municipal apartment radiators; cooler outflow water then warms commercial tomato greenhouses, aquaculture fish tanks, and snow-melting sidewalks.</li>
              <li>By monetizing multiple temperature tiers from the same drilled borehole, cascaded geothermal systems raise total thermal utilization above 75 percent and substantially shorten capital payback periods.</li>
            </ul>''',
            'The student wants to explain how cascaded thermal utilization improves both the energy efficiency and economic returns of Icelandic geothermal plants compared with generating electricity alone. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
            [
                'Instead of wasting residual heat from steam turbines—which convert just 12 to 15 percent of borehole energy into electricity—Icelandic plants pipe cooling geothermal water sequentially through municipal heating, greenhouses, aquaculture, and snow-melting grids, lifting total energy utilization above 75 percent while shortening capital payback periods.',
                'High-temperature geothermal power plants in Iceland rely on deep boreholes to spin steam turbines that generate renewable electricity for national grids.',
                'In Iceland, warm geothermal outflow water is used to heat commercial tomato greenhouses, aquaculture fish tanks, and municipal snow-melting sidewalks.',
                'Although geothermal steam turbines in Iceland convert only 12 to 15 percent of thermal energy into electricity, deep boreholes supply fluids between 80°C and 120°C.'
            ],
            'A',
            'Goal-First SOP: Giải thích CÁCH khai thác nhiệt theo tầng (cascaded utilization) cải thiện CẢ [1] HIỆU SUẤT NĂNG LƯỢNG (so với chỉ phát điện: 12–15% → >75%) LẪN [2] HIỆU QUẢ KINH TẾ (rút ngắn thời gian hoàn vốn đầu tư — shortening capital payback periods). B, C, D đều bỏ sót ít nhất 2 trong 3 mảnh ghép (đặc biệt bỏ sót hẳn lợi ích kinh tế "payback periods" và con số so sánh 12–15% vs >75%). Duy nhất A tích hợp hoàn mỹ toàn bộ quy trình nối tầng, mức nhảy hiệu suất và lợi ích hoàn vốn!',
            'Gặp Goal kép ("both energy efficiency AND economic returns compared with electricity alone"), gạch kiểm đủ 3 trụ: [1] So sánh mốc phát điện đơn thuần (12–15%), [2] Hiệu suất mới (>75%) qua cơ chế nối tầng, [3] Lợi ích kinh tế (shortening payback periods)!',
            [
                ('Đáp án đúng', 'Khớp đủ cả ba mảnh ghép của Goal: đối chiếu mốc phát điện (12–15%), giải thích cơ chế nối tầng tăng hiệu suất (>75%) và nêu lợi ích kinh tế (rút ngắn hoàn vốn).'),
                ('Wrong Synthesis Goal', 'Chỉ mô tả chung việc phát điện bằng tuabin hơi, không nhắc đến khai thác nối tầng hay kinh tế.'),
                ('Missing Comparison & Economics', 'Chỉ liệt kê vài ứng dụng phụ mà bỏ qua so sánh hiệu suất với phát điện và hiệu quả hoàn vốn.'),
                ('Missing Cascaded Mechanism & Economics', 'Không hề nêu hệ thống nối tầng, hiệu suất >75% hay thời gian hoàn vốn.'),
            ]
        ),
        q_item(
            'm8_m2h_q27', 27, 'Expression of Ideas', 'Rhetorical Synthesis', 'Elite (750+)',
            '''<p>While researching primate bioacoustics, a student has taken the following notes:</p>
            <ul>
              <li>West African Diana monkeys produce acoustically distinct alarm barks for crowned eagles versus leopards.</li>
              <li>Playback experiments show that listening Diana monkeys scan the canopy after hearing eagle barks and climb higher into thin branches after hearing leopard barks, demonstrating predator-specific referential signaling.</li>
              <li>Wild Ethiopian gelada monkeys emit rhythmic, undulating vocal "wobbles" accompanied by rapid lip-smacking during close-range grooming bouts.</li>
              <li>Bioacousticians have found that gelada wobbles convey no external predator warnings; instead, their synchronized cadence strengthens social bonds within large multi-family bands.</li>
            </ul>''',
            'The student wants to highlight a functional contrast between the vocalizations of Diana monkeys and gelada monkeys, emphasizing that one species transmits predator-specific warnings while the other reinforces internal group cohesion. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
            [
                'Both West African Diana monkeys and Ethiopian gelada monkeys have been studied by bioacousticians interested in how primates communicate through complex vocal signals.',
                'West African Diana monkeys emit separate alarm barks for crowned eagles and leopards, prompting listeners either to scan the forest canopy or to climb into thinner upper branches.',
                'Whereas West African Diana monkeys use distinct alarm barks to broadcast predator-specific warnings about eagles or leopards, Ethiopian gelada monkeys employ rhythmic lip-smacking "wobbles" during grooming to reinforce social cohesion within large groups.',
                'During close-range grooming bouts, Ethiopian gelada monkeys produce undulating vocal "wobbles" that do not warn group members about approaching predators.'
            ],
            'C',
            'Goal-First SOP: Nhấn mạnh SỰ TƯƠNG PHẢN CHỨC NĂNG giữa hai loài: Diana monkeys (truyền cảnh báo ĐẶC THÙ THEO LOÀI SĂN MỒI) ↔ Gelada monkeys (củng cố SỰ GẮN KẾT NỘI BỘ BẦY ĐÀN). A chỉ nói điểm giống chung chung; B chỉ nói Diana monkeys; D chỉ nói Gelada monkeys (và còn thiếu mục đích gắn kết xã hội!). Duy nhất C dùng "Whereas" đối chiếu chính xác cả hai loài và đúng hai chức năng trong Goal!',
            'Checklist 3 điểm bắt buộc: [1] Từ nối tương phản ("Whereas") + [2] Diana = cảnh báo đặc thù theo kẻ săn mồi (eagle/leopard) + [3] Gelada = củng cố gắn kết xã hội nội nhóm!',
            [
                ('Wrong Synthesis Goal (Similarity)', 'Nhấn mạnh điểm chung chung ("Both...") thay vì sự tương phản chức năng.'),
                ('One-Sided Synthesis', 'Chỉ nói về khỉ Diana, thiếu hoàn toàn khỉ Gelada.'),
                ('Đáp án đúng', 'Đối chiếu sắc nét chức năng cảnh báo đặc thù loài săn mồi của khỉ Diana với chức năng củng cố gắn kết xã hội của khỉ Gelada.'),
                ('One-Sided & Incomplete', 'Chỉ nhắc khỉ Gelada và mới chỉ nói chúng "không cảnh báo thú dữ", bỏ quên chức năng gắn kết bầy đàn.'),
            ]
        ),
    ]
