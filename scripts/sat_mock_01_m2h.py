# -*- coding: utf-8 -*-
"""
Full-Length Adaptive Mock Test #1 — Module 2 HARD Route (27 Qs, Hard & Elite 750+, 32 min)
Exact College Board Digital SAT R&W Blueprint.
"""

from sat_drills_1_1_and_2_1 import q_item
from sat_drills_5_4_to_5_5 import svg_bar_chart, html_table

def get_m2h_questions():
    return [
        # --- Q1-Q5: Words in Context (Hard / Elite 750+) ---
        q_item(
            'm1_m2h_q1', 1, 'Craft and Structure', 'Words in Context', 'Elite (750+)',
            '<p>While popular histories often portray the ancient Mesoamerican ballgame as a purely ceremonial rite divorced from politics, newly deciphered Maya stelae ______ that narrow view, documenting high-stakes matches staged explicitly to seal diplomatic treaties and humiliate rival dynasties.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            ['substantiate', 'belie', 'emulate', 'stipulate'],
            'B',
            'Contrast Clue: "While popular histories often portray... purely ceremonial rite divorced from politics" đối lập hoàn toàn với bia ký Maya mới giải mã cho thấy trò chơi gắn chặt với ngoại giao và chính trị → PHƠI BÀY SỰ SAI LỆCH / BÁC BỎ quan điểm hẹp đó → "belie" (B)!',
            'Bia ký mới phơi bày tính sai lệch của cái nhìn cũ → chọn "belie" (trái ngược hoàn toàn với "substantiate" = chứng thực).',
            [
                ('Opposite Meaning', 'substantiate = chứng minh/củng cố — sai hoàn toàn với vế đối lập "While...".'),
                ('Đáp án đúng', 'belie = mâu thuẫn/phơi bày sự sai lệch của một nhận định hẹp hòi trước đó.'),
                ('Wrong Meaning', 'emulate = bắt chước — không phù hợp với chủ ngữ "Maya stelae".'),
                ('Wrong Meaning', 'stipulate = quy định điều khoản — sai ngữ cảnh phản bác sử học.'),
            ]
        ),
        q_item(
            'm1_m2h_q2', 2, 'Craft and Structure', 'Words in Context', 'Elite (750+)',
            '<p>Because orbital dust storms on Mars periodically coat solar-panel arrays in fine iron oxide, mission planners found solar power ______ for multi-year polar rovers and turned instead to radioisotope thermoelectric generators capable of running reliably through pitch-dark Martian winters.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            ['wanting', 'indispensable', 'lucrative', 'prolific'],
            'A',
            'Cause-Effect Clue: bão bụi liên tục phủ kín pin mặt trời + mùa đông cực tối đen → các nhà hoạch định đánh giá điện mặt trời CHƯA ĐẠT YÊU CẦU / THIẾU SÓT nên phải chuyển sang máy phát đồng vị phóng xạ → Nghĩa thứ cấp học thuật của "wanting" = deficient / inadequate ("found solar power wanting") → Chọn A!',
            'Nhớ cấu trúc học thuật kinh điển: "find X wanting" = đánh giá X còn thiếu sót, không đủ đáp ứng chuẩn yêu cầu!',
            [
                ('Đáp án đúng', 'wanting (nghĩa thứ cấp: thiếu sót, không đủ tin cậy) khớp trọn cụm "found solar power wanting".'),
                ('Opposite Meaning', 'indispensable = không thể thiếu — trái với việc họ từ bỏ nó để chuyển sang máy phát đồng vị.'),
                ('Wrong Context', 'lucrative = sinh lợi nhuận cao — không dùng cho nguồn năng lượng xe tự hành Sao Hỏa.'),
                ('Wrong Meaning', 'prolific = sung mãn tạo ra nhiều tác phẩm/con cái.'),
            ]
        ),
        q_item(
            'm1_m2h_q3', 3, 'Craft and Structure', 'Words in Context', 'Elite (750+)',
            '<p>Although early twentieth-century opera critics accused modernist composer Alban Berg of abandoning emotional expressiveness in favor of sterile mathematical tone rows, listeners today frequently find his <i>Violin Concerto</i> deeply ______—a poignant elegy shaped by tender folk melodies woven seamlessly into strict twelve-tone counterpoint.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            ['clinical', 'cacophonous', 'affecting', 'perfunctory'],
            'C',
            'Contrast + Restatement Clue: đối lập với lời buộc tội "sterile mathematical" (lạnh lẽo toán học) + giải thích sau gạch ngang "a poignant elegy shaped by tender folk melodies" (khúc bi ca sâu lắng đầy dịu dàng) → CHẠM SÂU VÀO CẢM XÚC, GÂY XÚC ĐỘNG MẠNH → Nghĩa thứ cấp học thuật của "affecting" (adj) = deeply moving / touching → Chọn C!',
            'Thuộc nghĩa thứ cấp sát thủ của "affecting" (adj): KHÔNG phải "đang tác động", mà nghĩa là "xúc động sâu sắc, chạm đến trái tim" (moving / poignant)!',
            [
                ('Opposite Meaning', 'clinical = lạnh lùng vô cảm — đồng nghĩa với "sterile mathematical", trái sau "Although".'),
                ('Opposite Meaning', 'cacophonous = chói tai hỗn tạp — trái ngược "tender folk melodies... seamlessly".'),
                ('Đáp án đúng', 'affecting (tính từ học thuật: đầy xúc cảm, làm rung động lòng người) khớp tuyệt đối với "poignant elegy".'),
                ('Wrong Meaning', 'perfunctory = qua loa chiếu lệ — sai hoàn toàn với sự trau chuốt và xúc động.'),
            ]
        ),
        q_item(
            'm1_m2h_q4', 4, 'Craft and Structure', 'Words in Context', 'Elite (750+)',
            '<p>Installing porous oyster-shell breakwaters along eroding Louisiana bayous cannot halt global sea-level rise, but coastal engineers emphasize that these living reefs substantially ______ wave-driven shoreline retreat by dissipating storm surge energy before it reaches fragile marsh banks.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            ['precipitate', 'preclude', 'obliterate', 'mitigate'],
            'D',
            'Nuance Cluster 750+: "cannot halt global sea-level rise, but... substantially ______ wave-driven shoreline retreat" (KHÔNG chặn đứng 100% mà LÀM GIẢM NHẸ đáng kể bằng cách tiêu tán bớt năng lượng sóng) → "mitigate" (D)! Loại B (preclude = ngăn triệt để không cho xảy ra) và C (obliterate = xóa sổ hoàn toàn) vì quá mạnh so với bối cảnh chỉ làm tiêu tán bớt năng lượng sóng.',
            'Cảnh giác mức độ từ: tiêu tán bớt năng lượng sóng (dissipating) mà không chặn đứng được nước biển dâng → chọn "mitigate" (giảm nhẹ), loại "preclude / obliterate"!',
            [
                ('Opposite Meaning', 'precipitate = châm ngòi/đẩy nhanh — ngược hoàn toàn mục đích bảo vệ bờ biển.'),
                ('Degree Too Strong', 'preclude = ngăn chặn triệt để không cho xảy ra — quá mạnh khi câu đầu thừa nhận không chặn được nước biển dâng.'),
                ('Degree Too Strong', 'obliterate = xóa sổ sạch 100% — quá cực đoan về mặt vật lý.'),
                ('Đáp án đúng', 'mitigate = làm giảm nhẹ đáng kể mức độ xói lở bờ biển.'),
            ]
        ),
        q_item(
            'm1_m2h_q5', 5, 'Craft and Structure', 'Words in Context', 'Elite (750+)',
            '<p>Because colonial-era surveyors mapped Andean mountain terraces solely to assess silver-mining tribute while omitting local irrigation canals and sacred shrines, modern ethnohistorians treat those archival charts as ______ sources that reflect imperial tax priorities rather than lived community geography.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            ['tendentious', 'exhaustive', 'impartial', 'inscrutable'],
            'A',
            'Cause-Effect + Restatement Clue: chỉ vẽ bản đồ để thu thuế mỏ bạc, cố tình bỏ qua kênh thủy lợi và đền thiêng bản địa → phản ánh ưu tiên đế quốc chứ không khách quan → THIÊN LỆCH / PHỤC VỤ MỤC ĐÍCH CHỦ QUAN → "tendentious" (A)!',
            'Tendentious (adj) = biased / promoting a particular agenda (thiên vị, phục vụ mục đích áp đặt — trái ngược hoàn toàn với "impartial" và "exhaustive")!',
            [
                ('Đáp án đúng', 'tendentious = mang thiên kiến chủ quan phục vụ mục đích áp đặt (ở đây là mục tiêu thu thuế của đế quốc).'),
                ('Opposite Meaning', 'exhaustive = toàn diện đầy đủ — mâu thuẫn trực tiếp với việc bỏ sót kênh tưới và đền thiêng.'),
                ('Opposite Meaning', 'impartial = công tâm không thiên vị — trái ngược hoàn toàn.'),
                ('Wrong Meaning', 'inscrutable = bí ẩn không thể đọc hiểu — các nhà sử học HIỂU RÕ mục đích thu thuế của bản đồ chứ không bó tay giải mã.'),
            ]
        ),

        # --- Q6-Q7: Text Structure and Purpose (Hard / Elite) ---
        q_item(
            'm1_m2h_q6', 6, 'Craft and Structure', 'Text Structure and Purpose', 'Elite (750+)',
            '<p>When urban planners redesigned Copenhagen’s harborfront during the 1990s, municipal leaders resisted selling prime waterfront parcels to private luxury condominium developers. Instead, they spent a decade upgrading sewage overflow reservoirs until harbor water met strict swimming standards, opening free wooden harbor baths directly beside downtown offices. <u>Real-estate analysts initially predicted that dedicating prime shoreline to public swimming decks would depress adjacent commercial rents, yet surrounding districts ultimately attracted higher long-term tax revenue than comparable privatized European ports.</u></p>',
            'Which choice best describes the function of the underlined sentence in the text as a whole?',
            [
                'It explains the civil-engineering process Copenhagen used to upgrade its municipal sewage reservoirs.',
                'It counters a skeptical economic forecast by noting that Copenhagen’s public-waterfront strategy ultimately outperformed privatized alternatives financially.',
                'It concedes that private luxury condominiums generate higher commercial rents than public harbor baths.',
                'It introduces an unrelated debate over water-quality testing standards across European ports.'
            ],
            'B',
            'Câu gạch chân mở đầu bằng dự đoán hoài nghi của giới phân tích bất động sản ("initially predicted... would depress commercial rents"), rồi dùng "yet" để phản chứng bằng thực tế tài chính vượt trội (thu thuế dài hạn cao hơn các cảng tư nhân hóa ở châu Âu) → Chọn B!',
            'Nhận diện cặp cấu trúc tu từ trong 1 câu: "Analysts initially predicted [Bad Outcome], yet [Superior Actual Outcome]" = counters a skeptical forecast!',
            [
                ('Out of Scope', 'Không mô tả quy trình kỹ thuật cải tạo hồ chứa nước thải.'),
                ('Đáp án đúng', 'Khớp trọn hai vế câu gạch chân: phản bác dự báo kinh tế bi quan bằng kết quả thu thuế dài hạn vượt trội.'),
                ('Reversed Logic', 'Câu gạch chân chứng minh điều NGƯỢC LẠI: mô hình công cộng thắng về doanh thu thuế dài hạn.'),
                ('Out of Scope', 'Không mở ra tranh luận ngoài lề về tiêu chuẩn kiểm tra nước.'),
            ]
        ),
        q_item(
            'm1_m2h_q7', 7, 'Craft and Structure', 'Text Structure and Purpose', 'Elite (750+)',
            '<p><i>The following text is adapted from an 1886 frontier memoir describing a lone surveyor camping on the Kansas plains during an autumn drought.</i><br/>By dusk the dry buffalo grass lay flattened like pale hammered copper, stretching unbroken to a horizon so level that even a distant cottonwood seemed as monumental as a cathedral tower. When a single freight train passed six miles to the south, its faint whistle carried cleanly across the stillness long after its smoke had vanished—reminding me not of the city I had left behind, but of how vast the silence was that swallowed every human sound back into itself.</p>',
            'Which choice best states the main purpose of the text?',
            [
                'To criticize railway companies for disturbing fragile prairie wildlife during autumn droughts.',
                'To argue that frontier surveyors felt more comfortable living in bustling eastern cities than on the open plains.',
                'To evoke the overwhelming spatial vastness and deep silence of the autumn prairie through contrasting visual and auditory details.',
                'To explain how dry atmospheric conditions alter the speed at which train whistles travel over flat terrain.'
            ],
            'C',
            'Tác giả phối hợp 2 giác quan để khắc họa sự bao la choáng ngợp và tĩnh lặng sâu thẳm của thảo nguyên: thị giác (chỉ một cây bông đơn độc cũng đồ sộ như tháp nhà thờ trên đường chân trời phẳng tắp) + thính giác (tiếng còi tàu từ xa 6 dặm càng tô đậm khoảng im lặng mênh mông nuốt chửng mọi âm thanh con người) → Chọn C!',
            'Chú ý chữ "reminding me NOT of the city..., but of how vast the silence was" — nó bác bỏ bẫy nhớ thành phố (B) và chốt thẳng Main Purpose (C)!',
            [
                ('Out of Scope / Wrong Tone', 'Không có lời chỉ trích ngành đường sắt hay nhắc động vật hoang dã.'),
                ('Contradiction', 'Tác giả nói rõ tiếng còi KHÔNG gợi nhớ thành phố mà gợi cảm nhận về sự tĩnh lặng bao la.'),
                ('Đáp án đúng', 'Gom gọn hoàn hảo cả chi tiết thị giác (cottonwood like cathedral tower) lẫn thính giác (train whistle swallowed by vast silence).'),
                ('Literal Misreading', 'Đây là đoạn hồi ký văn học giàu cảm xúc, không phải bài giảng vật lý tốc độ âm thanh.'),
            ]
        ),

        # --- Q8: Cross-Text Connections (Elite 750+) ---
        q_item(
            'm1_m2h_q8', 8, 'Craft and Structure', 'Cross-Text Connections', 'Elite (750+)',
            '<p><b>Text 1</b><br/>Planetary astronomer Dr. Victor Alvarez proposes that the mysterious brightening of distant icy dwarf planet Makemake observed in 2022 resulted from a brief cryo-volcanic eruption venting fresh nitrogen frost across its reddish surface, temporarily raising its reflectivity.</p><p><b>Text 2</b><br/>Re-analyzing the same 2022 infrared data alongside James Webb Space Telescope thermal measurements, astrophysicist Dr. Linnea Lindholm detects no warm surface hotspots or escaping gas plumes consistent with active cryo-volcanism. Instead, Lindholm notes that Makemake’s subtle brightening coincided precisely with a geometric alignment in which its newly discovered dark moon passed directly behind the dwarf planet, momentarily removing the moon’s darker light from the combined telescopic signal.</p>',
            'Based on the texts, how would Dr. Linnea Lindholm (Text 2) most likely respond to Dr. Victor Alvarez’s proposal (Text 1)?',
            [
                'By asserting that the 2022 telescopic measurements showing Makemake brightening were completely fabricated.',
                'By agreeing that a cryo-volcanic eruption occurred on Makemake, while arguing it emitted methane rather than nitrogen frost.',
                'By claiming that Makemake’s dark moon regularly triggers cryo-volcanic eruptions through tidal heating.',
                'By arguing that the observed brightening was an observational artifact caused by an orbital alignment of Makemake’s moon rather than surface cryo-volcanism.'
            ],
            'D',
            'Text 1 giải thích độ sáng tăng năm 2022 bằng núi lửa băng (cryo-volcanism). Text 2 dùng dữ liệu JWST chỉ ra KHÔNG có điểm nóng hay luồng khí thoát, mà độ sáng tăng khớp đúng thời điểm mặt trăng tối của Makemake khuất sau hành tinh → chỉ là hiệu ứng hình học quan sát (observational artifact) khi ánh sáng tối của mặt trăng bị che khuất khỏi tín hiệu gộp! Chọn D!',
            'Phân biệt sắc nét: Hiện tượng vật lý trên bề mặt (T1: cryo-volcanism) ↔ Hiệu ứng hình học quan sát do mặt trăng khuất sau (T2: orbital alignment artifact)!',
            [
                ('Overstated Conflict / Out of Scope', 'Lindholm không nói dữ liệu bị bịa đặt — bà tái phân tích CHÍNH dữ liệu năm 2022 đó và giải thích nguyên nhân khác!'),
                ('Contradiction', 'Lindholm khẳng định KHÔNG phát hiện điểm nóng hay luồng khí nào phù hợp với cryo-volcanism.'),
                ('Out of Scope / Distortion', 'Mặt trăng không kích hoạt núi lửa — nó chỉ đi ra phía sau hành tinh làm thay đổi tín hiệu quang học gộp.'),
                ('Đáp án đúng', 'Phản ánh chính xác lập luận của Lindholm: bác bỏ núi lửa băng và giải thích độ sáng tăng là hiệu ứng hình học quỹ đạo của mặt trăng tối.'),
            ]
        ),

        # --- Q9-Q10: Central Ideas and Details (Hard / Elite) ---
        q_item(
            'm1_m2h_q9', 9, 'Information and Ideas', 'Central Ideas and Details', 'Elite (750+)',
            '<p>In eighteenth-century London, theatrical patent laws granted only two royal playhouses—Drury Lane and Covent Garden—the legal right to stage spoken-word dramas. Rather than shutting down, dozens of unlicensed neighborhood theaters circumvented the monopoly by staging "burlettas": fast-paced productions that included at least five musical numbers per act and continuous quiet piano accompaniment beneath dialogue, legally classifying the plays as musical entertainment while smuggling sharp political satire and Shakespearean tragedies to working-class audiences.</p>',
            'Which choice best states the main idea of the text?',
            [
                'Unlicensed London theaters creatively exploited musical-performance loopholes to stage spoken drama and satire despite royal monopoly laws.',
                'Eighteenth-century working-class London audiences preferred silent piano recitals over spoken Shakespearean tragedies.',
                'Drury Lane and Covent Garden went bankrupt because unlicensed neighborhood theaters staged lower-priced musical comedies.',
                'British lawmakers passed theatrical patent laws specifically to encourage the invention of the musical burletta.'
            ],
            'A',
            'Trục lập luận toàn đoạn: Luật độc quyền chỉ cho 2 nhà hát hoàng gia diễn kịch nói → Các nhà hát ngoài luồng lách luật sáng tạo bằng thể loại "burletta" (chèn ≥5 đoạn nhạc & đệm piano nhẹ dưới lời thoại) để hợp pháp hóa việc diễn bi kịch Shakespeare và châm biếm chính trị cho khán giả bình dân → Chọn A!',
            'Bám sát động từ trung tâm "circumvented the monopoly by..." để chốt Main Idea chính xác!',
            [
                ('Đáp án đúng', 'Tóm gọn trọn vẹn việc các nhà hát không phép khéo léo lách luật độc quyền hoàng gia bằng yếu tố âm nhạc để diễn kịch và châm biếm.'),
                ('Distortion', 'Nhạc đệm chỉ là vỏ bọc pháp lý để diễn kịch nói Shakespeare và châm biếm, không nói khán giả thích hòa tấu piano không lời hơn.'),
                ('Out of Scope', 'Không hề nhắc đến việc Drury Lane hay Covent Garden bị phá sản.'),
                ('Reversed Logic', 'Luật bản quyền nhằm hạn chế độc quyền cho 2 nhà hát hoàng gia, còn burletta là cách LÁCH luật đó.'),
            ]
        ),
        q_item(
            'm1_m2h_q10', 10, 'Information and Ideas', 'Central Ideas and Details', 'Elite (750+)',
            '<p>Bioacoustic surveys in the Gulf of Maine revealed that North Atlantic right whales alter their low-frequency "upcall" vocalizations differently depending on the type of background sound. When steady wind-driven wave noise rises, whales simply raise their call volume while keeping pitch steady; when rhythmic low-frequency shipping noise dominates the same frequency band, however, whales shift their call frequency upward into a quieter acoustic window—even though producing higher-pitched calls carries a slightly shorter underwater transmission range.</p>',
            'According to the text, how do North Atlantic right whales adjust their vocalizations differently in response to shipping noise compared with wind-driven wave noise?',
            [
                'They stop vocalizing completely during shipping noise, whereas they sing continuously during wind storms.',
                'They shift their call pitch upward into a less crowded frequency band despite reduced transmission distance, rather than merely increasing call volume at the same pitch.',
                'They lower their call pitch to achieve longer underwater transmission range whenever vessels pass nearby.',
                'They mimic the rhythmic frequency pattern of ship engines so their calls travel farther through turbulent waves.'
            ],
            'B',
            'Đối chiếu trực tiếp 2 câu trong bài: Wind noise → tăng âm lượng, giữ nguyên cao độ ("raise volume while keeping pitch steady"); Shipping noise → NÂNG CAO ĐỘ lên vùng tần số ít nhiễu hơn dù tầm truyền ngắn hơn một chút ("shift call frequency upward... even though... shorter transmission range") → Paraphrase chính xác 100% ở B!',
            'Trong câu Detail có phép so sánh 2 trường hợp (A vs. B), gạch đôi 2 cột đối chiếu ngay trong đầu để không bị bẫy đảo chiều!',
            [
                ('Too Extreme / Contradiction', 'Cá voi KHÔNG ngừng phát âm — chúng dịch chuyển tần số lên cao hơn.'),
                ('Đáp án đúng', 'Khớp từng chi tiết giữa phản ứng với tàu thuyền (nâng cao độ, chấp nhận tầm truyền ngắn hơn) và phản ứng với gió (chỉ tăng âm lượng).'),
                ('Reversed Logic', 'Bài nói cá voi dịch tần số LÊN CAO ("upward") với tầm truyền NGẮN HƠN ("shorter"), không phải hạ thấp để truyền xa hơn.'),
                ('Out of Scope', 'Không nói cá voi bắt chước nhịp động cơ tàu.'),
            ]
        ),

        # --- Q11-Q12: Command of Evidence — Textual (Elite 750+) ---
        q_item(
            'm1_m2h_q11', 11, 'Information and Ideas', 'Command of Evidence (Textual)', 'Elite (750+)',
            '<p>Archaeologists excavating Chavín de Huántar—a 3,000-year-old ceremonial center in the Peruvian Andes—discovered a labyrinth of narrow, windowless stone galleries threaded with tiny ventilation ducts and resonant chambers. Acoustician Dr. Miriam Kolar hypothesized that Andean priests deliberately engineered these subterranean stone channels to channel and amplify the blast of marine conch-shell trumpets (<i>pututus</i>), producing disorienting acoustic illusions inside the dark galleries rather than the ducts serving purely as ordinary air-circulation vents.</p>',
            'Which finding, if true, would most directly support Dr. Miriam Kolar’s hypothesis?',
            [
                'Marine conch shells used to craft <i>pututus</i> were traded hundreds of kilometers inland from the warm waters of Ecuador’s Pacific coast.',
                'Airflow measurements indicate that fresh outside air enters the central chambers slowly through the upper roof stairwells.',
                'Acoustic mapping demonstrates that the stone ducts’ exact interior dimensions resonate selectively at the exact fundamental frequencies produced by excavated Chavín conch trumpets—and include deliberate right-angle acoustic baffles that degrade airflow while sharply projecting trumpet sound toward ceremonial alcoves.',
                'Several modern Andean communities still blow marine conch shells during annual agricultural festivals.'
            ],
            'C',
            'Khóa giả thuyết Kolar: Các ống đá được CỐ TÌNH THIẾT KẾ CHO ÂM HỌC KÈN ỐC BIỂN (X1), chứ KHÔNG chỉ là ống thông gió bình thường (NOT X2). Đáp án C chứng minh đồng thời cả 2 vế siêu thuyết phục: (1) Kích thước ống cộng hưởng chính xác ở đúng tần số kèn ốc biển Chavín; (2) Có vách đổi góc cố tình LÀM KÉM KHẢ NĂNG THÔNG GIÓ (bác bỏ mục đích thuần thông gió!) nhưng lại hướng âm thanh kèn sắc nét vào hốc nghi lễ! Chọn C!',
            'Bằng chứng 800-level tuyệt đối cho giả thuyết "designed for A rather than B": chỉ ra chi tiết thiết kế CỐ TÌNH làm hại chức năng B (degrade airflow) nhưng lại tối ưu hóa đúng chức năng A (exact resonant frequency of pututus)!',
            [
                ('Adjacent Topic Drift', 'Nguồn gốc thương mại của vỏ ốc từ Ecuador không chứng minh cấu trúc ống đá được thiết kế cho âm học.'),
                ('Irrelevant / Weak', 'Không khí vào qua cầu thang mái không trực tiếp chứng minh thiết kế âm học có chủ đích của các ống dẫn.'),
                ('Đáp án đúng', 'Bằng chứng kép cực sắc: cộng hưởng chính xác tần số kèn ốc + có vách ngăn làm giảm lưu thông khí nhưng khuếch đại âm thanh về hốc nghi lễ.'),
                ('Adjacent Topic Drift', 'Tập quán hiện đại không chứng minh ý đồ kiến trúc 3.000 năm trước.'),
            ]
        ),
        q_item(
            'm1_m2h_q12', 12, 'Information and Ideas', 'Command of Evidence (Textual)', 'Elite (750+)',
            '<p>In a critical study of the 1897 maritime novel <i>The Cape Soundings</i>, a scholar asserts that veteran navigator Eliza views the company’s newly introduced steam-powered freighters with conflicted admiration: she respects their reliable speed against headwinds, yet mourns the loss of the intimate dialogue between sailor and sea required under sail.</p>',
            'Which quotation from Eliza in <i>The Cape Soundings</i> most effectively illustrates the scholar’s assertion?',
            [
                '“A triple-expansion steam engine burns forty tons of Welsh coal between Liverpool and Halifax, leaving soot across every brass railing.”',
                '“Under full canvas a helmsman had to read every shiver in the rigging and every ripple on the swell as if the Atlantic were speaking directly to his palms.”',
                '“No sailing bark could ever keep a schedule like those iron steamers when winter gales howl dead ahead from Newfoundland.”',
                '“I grant the new iron steamers their punctual majesty—they march straight into a gale that would pin a clipper for a week—yet my heart aches for the wooden wheel that forced a sailor to listen to every mood of wind and tide.”'
            ],
            'D',
            'Checklist 2 vế bắt buộc từ "conflicted admiration": [1] Tôn trọng tốc độ đáng tin cậy bất chấp gió ngược ("respects reliable speed against headwinds") + [2] Tiếc nuối sự mất đi mối đối thoại tinh tế giữa thủy thủ và biển cả dưới cánh buồm ("mourns loss of intimate dialogue under sail"). B chỉ có [2] (Half-Match!); C chỉ có [1] (Half-Match!); A chỉ nói chuyện đốt than bám muội. Duy nhất D ôm trọn cả 2 vế đối nghịch trong một câu: "grant... punctual majesty—march straight into a gale" [1] + "yet my heart aches for the wooden wheel that forced a sailor to listen to every mood of wind and tide" [2]!',
            'Điển hình bẫy Hard Module 2: B và C mỗi câu đều cực hay nhưng chỉ đáp ứng ĐÚNG 1 NỬA của Claim → gạch cả B và C, chốt D!',
            [
                ('Negative Detail Only', 'Chỉ chê bụi than bám lan can đồng, thiếu cả sự tôn trọng tốc độ lẫn nỗi tiếc nuối thuyền buồm.'),
                ('Half-Match Trap (Only Vế 2)', 'Chỉ mô tả mối giao cảm với biển dưới thuyền buồm, thiếu hẳn sự tôn trọng tốc độ của tàu hơi nước.'),
                ('Half-Match Trap (Only Vế 1)', 'Chỉ khen tàu hơi nước đúng lịch trong gió ngược, thiếu hẳn nỗi tiếc nuối sự gắn kết với biển cả.'),
                ('Đáp án đúng', 'Khớp đủ cả hai vế của "conflicted admiration": tôn trọng sức vượt gió ngược của tàu hơi nước + đau đáu tiếc mối đối thoại cùng gió triều trên tàu buồm.'),
            ]
        ),

        # --- Q13-Q14: Command of Evidence — Quantitative (Elite 750+) ---
        q_item(
            'm1_m2h_q13', 13, 'Information and Ideas', 'Command of Evidence (Quantitative)', 'Elite (750+)',
            svg_bar_chart(
                'Share of Urban Commute Trips Under 3 km Made by Bicycle (%) in Four Cities (2024)',
                ['0%', '15%', '30%', '45%', '60%'],
                [('City W (Painted)', 12, '12%'), ('City X (Painted)', 16, '16%'), ('City Y (Curb-Prot.)', 44, '44%'), ('City Z (Curb-Prot.)', 51, '51%')],
                60
            ) + '<p>Transportation planners evaluated whether merely painting dashed bicycle lanes onto car traffic roadways encourages high rates of short-distance urban cycling, or whether physically separating cyclists behind concrete curbs ("curb-protected" lanes) is necessary to push short-trip cycling shares above 30%. Data from four comparable mid-sized cities reinforce the importance of physical separation: ______</p>',
            'Which choice most effectively uses data from the graph to complete the text?',
            [
                'while both cities relying on painted lanes remained well below the 30% threshold—at 12% in City W and 16% in City X—both cities with curb-protected lanes comfortably surpassed it, reaching 44% in City Y and 51% in City Z.',
                'City Z achieved the highest short-trip cycling share at 51%, which was 7 percentage points higher than City Y’s share of 44%.',
                'City X recorded a higher short-trip cycling share (16%) than City W (12%) despite both cities using painted lanes.',
                'none of the four surveyed cities exceeded a 60% bicycle share for commute trips under three kilometers.'
            ],
            'A',
            'Khóa đối chiếu cần chứng minh: Painted lanes (dưới 30%) vs. Curb-protected lanes (vượt trên 30%). Đáp án B và C chỉ so sánh nội bộ trong cùng một nhóm (Y vs. Z hoặc W vs. X), không chứng minh được sự vượt trội của làn có dải phân cách cứng so với làn chỉ kẻ vạch! Duy nhất A đối chiếu trực diện cả 2 nhóm quanh ngưỡng 30% (12% & 16% < 30% vs. 44% & 51% > 30%)! Chọn A!',
            'Khi giả thuyết đối chiếu Nhóm 1 vs. Nhóm 2 quanh một ngưỡng (30%), loại ngay mọi đáp án chỉ so sánh nội bộ trong 1 nhóm!',
            [
                ('Đáp án đúng', 'Đối chiếu trọn vẹn cả hai nhóm quanh mốc 30%: Painted (12%, 16%) đều dưới xa 30%, còn Curb-Protected (44%, 51%) đều vượt xa 30%.'),
                ('Within-Group Only', 'Chỉ so sánh giữa hai thành phố đều có dải phân cách cứng (Y vs. Z), bỏ quên nhóm Painted lanes.'),
                ('Within-Group Only', 'Chỉ so sánh hai thành phố kẻ vạch (W vs. X), không chứng minh lợi thế của Curb-Protected lanes.'),
                ('True Data / Wrong Claim', 'Nhận xét <60% không liên quan gì đến so sánh hai loại hạ tầng quanh mốc 30%.'),
            ]
        ),
        q_item(
            'm1_m2h_q14', 14, 'Information and Ideas', 'Command of Evidence (Quantitative)', 'Elite (750+)',
            html_table(
                'Table 2. Detected Exoplanets Orbiting Four Nearby Red Dwarf Stars by Detection Method',
                ['Host Star', 'Radial Velocity Detections', 'Transit Detections', 'Total Confirmed Planets', 'Est. Orbital Tilt (Inclination)'],
                [
                    ['Star Alpha', '4', '0', '4', '42°'],
                    ['Star Beta', '3', '3', '3', '89°'],
                    ['Star Gamma', '5', '0', '5', '55°'],
                    ['Star Delta', '2', '2', '2', '88°'],
                ]
            ) + '<p>Exoplanet astronomers explain that while the radial-velocity method can detect planets orbiting at nearly any viewing tilt relative to Earth, the transit method—which measures tiny dips in starlight when a planet crosses directly in front of its star—works only when a planetary system is viewed nearly edge-on (an orbital inclination close to 90°). Data in the table align closely with this geometric constraint: ______</p>',
            'Which choice most effectively uses data from the table to complete the text?',
            [
                'Star Gamma hosts the largest total number of confirmed planets in the table (5), whereas Star Delta hosts the fewest (2).',
                'the transit method detected planets only around Star Beta (89°) and Star Delta (88°)—where systems are viewed nearly edge-on—while missing all nine planets detected via radial velocity around the more steeply tilted systems Star Alpha (42°) and Star Gamma (55°).',
                'Star Beta and Star Delta each recorded equal numbers of radial-velocity detections and total confirmed planets.',
                'across all four host stars, radial velocity detected fewer planets than the transit method combined.'
            ],
            'B',
            'Kiểm tra quy luật hình học cần chứng minh: Radial velocity hoạt động ở MỌI góc nghiêng (42°, 55°, 88°, 89°), còn Transit CHỈ hoạt động gần góc cạnh 90° (88° và 89° → phát hiện 3 & 2 hành tinh; còn 42° và 55° → 0 hành tinh dù có 4 + 5 = 9 hành tinh phát hiện bởi radial velocity!). Kiểm tra số học ở B: 4 + 5 = 9 hành tinh bị bỏ sót ở Alpha & Gamma → chính xác 100%! (D sai số liệu: radial velocity = 14 > transit = 5!).',
            'Kiểm tra mọi phép cộng nhẩm trong đáp án SAT: Alpha (4) + Gamma (5) = 9 hành tinh; Beta (89°) & Delta (88°) đều sát 90° → B chuẩn tuyệt đối!',
            [
                ('True Data / Wrong Claim', 'Chỉ nêu tổng số hành tinh nhiều/ít nhất mà không liên hệ với góc nghiêng hay hai phương pháp phát hiện.'),
                ('Đáp án đúng', 'Khớp hoàn hảo quy luật hình học: Transit chỉ bắt được ở góc sát 90° (89°, 88°) và bỏ sót toàn bộ 9 hành tinh ở góc nghiêng 42° và 55°.'),
                ('True Data / Wrong Claim', 'Bỏ qua hoàn toàn biến cốt lõi là góc nghiêng quỹ đạo (inclination) và việc Transit = 0 ở Alpha/Gamma.'),
                ('Data Reading Error', 'Sai ngược số liệu: Radial velocity phát hiện 14 hành tinh, nhiều hơn hẳn 5 hành tinh của Transit.'),
            ]
        ),

        # --- Q15: Inferences (Elite 750+) ---
        q_item(
            'm1_m2h_q15', 15, 'Information and Ideas', 'Inferences', 'Elite (750+)',
            '<p>When cities widen congested arterial avenues by adding extra vehicle lanes, traffic engineers often observe that rush-hour travel times initially drop—yet within three to five years, average commute delays typically return to pre-widening levels because faster initial speeds induce previously deterred drivers, longer commuter trips, and new suburban developments to fill the added capacity. In contrast, when Seoul demolished its elevated Cheonggyecheon expressway in 2003 and replaced it with a pedestrian stream park alongside expanded bus rapid transit lanes, citywide downtown commute times did not surge catastrophically as critics had warned; in fact, cross-town transit speeds slightly improved. Taken together, these contrasting outcomes suggest that ______</p>',
            'Which choice most logically completes the text?',
            [
                'demolishing every highway inside a metropolitan region automatically eliminates all traffic congestion within five years.',
                'expanding roadway capacity for private cars rarely relieves congestion permanently, whereas removing car capacity can work smoothly when paired with attractive public-transit alternatives that shift travel demand.',
                'Seoul’s traffic engineers widened the Cheonggyecheon expressway before 2003 to induce suburban housing construction.',
                'urban commuters never alter their driving habits or travel routes in response to changes in road infrastructure.'
            ],
            'B',
            'Ghép 2 nửa tương phản (1-Millimeter Rule): (A) Mở rộng làn xe hơi thường không giảm kẹt xe vĩnh viễn vì tạo cầu dẫn dụ (induced demand) lấp đầy sau 3–5 năm; (B) Phá bỏ cao tốc trên cao ở Seoul NHƯNG đi kèm mở rộng làn xe buýt nhanh BRT không gây thảm họa kẹt xe mà còn cải thiện nhẹ tốc độ di chuyển ⇒ Kết luận 1mm: Mở rộng làn xe cá nhân hiếm khi giải quyết kẹt xe lâu dài, còn thu hẹp đường xe hơi có thể vận hành êm đẹp khi đi kèm giải pháp giao thông công cộng hấp dẫn giúp chuyển dịch nhu cầu đi lại (B)!',
            'Luôn tránh bẫy cực đoan ("every highway / automatically eliminates all congestion" ở A) và chọn kết luận giữ đúng điều kiện kép của văn bản ("when paired with attractive public-transit alternatives")!',
            [
                ('Too Extreme', '"demolishing every highway... automatically eliminates all congestion" phóng đại quá xa phạm vi 1 dự án đi kèm mở rộng BRT ở Seoul.'),
                ('Đáp án đúng', 'Tổng hợp chính xác cả hai vế tương phản (induced demand của mở đường + điều kiện kèm BRT của dự án Seoul).'),
                ('Fact Distortion', 'Bài không nói Seoul từng mở rộng Cheonggyecheon trước 2003 để tạo nhà ngoại ô.'),
                ('Contradiction', 'Cả hai ví dụ đều chứng minh người đi làm THAY ĐỔI MẠNH hành vi di chuyển theo hạ tầng đường sá.'),
            ]
        ),

        # --- Q16-Q19: Standard English Conventions — Boundaries (Hard / Elite) ---
        q_item(
            'm1_m2h_q16', 16, 'Standard English Conventions', 'Boundaries', 'Elite (750+)',
            '<p>In 2023, marine acousticians deployed autonomous hydrophones along three deep-sea canyons off Monterey, ______ Cape Hatteras, North Carolina; and Kaikōura, New Zealand, to compare how beaked whales react to distant cargo-vessel propellers.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['California,', 'California:', 'California;', 'California—'],
            'C',
            'Super-Semicolon! Quét phía sau thấy chuỗi 3 cặp `Thành phố/Mũi biển, Bang/Quốc gia` ngăn cách nhau bằng dấu chấm phẩy (`Cape Hatteras, North Carolina; and Kaikōura, New Zealand`). Do đó sau "Monterey, California" bắt buộc dùng dấu chấm phẩy (;) để khớp song song danh sách phức hợp → Chọn C!',
            'Luôn quét về phía sau chỗ trống 1 dòng: thấy `; and` trong danh sách địa danh có phẩy bên trong → Super-Semicolon 100%!',
            [
                ('List Delimiter Mismatch', 'Dùng phẩy thường sẽ trộn lẫn dấu phẩy nội bộ với dấu ngăn mục lớn và lệch với `; and` phía sau.'),
                ('Wrong Punctuation', 'Dấu hai chấm không thể ngăn mục đầu với mục thứ hai trong cùng danh sách.'),
                ('Đáp án đúng', 'Super-Semicolon phân tách mạch lạc mục 1 ("Monterey, California") với mục 2 và mục 3.'),
                ('Wrong Punctuation', 'Gạch ngang phá vỡ chuỗi Super-Semicolon.'),
            ]
        ),
        q_item(
            'm1_m2h_q17', 17, 'Standard English Conventions', 'Boundaries', 'Elite (750+)',
            '<p>Astronomers once assumed that globular star clusters formed all of their stars in a single brief burst; Hubble spectral surveys of Omega Centauri, ______, uncovered multiple distinct stellar generations separated by hundreds of millions of years.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['however', '; however', 'however;', 'therefore'],
            'A',
            'Soi cực kỹ hai ký tự in sẵn hai bên chỗ trống: `, ______,` (đã có sẵn CẶP DẤU PHẨY bọc chỗ trống!). Vế sau dấu chấm phẩy là 1 IC duy nhất ("Hubble spectral surveys of Omega Centauri, however, uncovered..."), nên "however" chỉ là từ nối chen giữa S và V (Interrupter) → KHÔNG thêm bất kỳ dấu chấm phẩy nào, chọn "however" (A)!',
            'Hễ thấy đề đã đặt sẵn cặp `, ______,` chen giữa Chủ ngữ và Động từ → tuyệt đối không chọn đáp án có thêm dấu `;` hay `,`!',
            [
                ('Đáp án đúng', 'however khớp chính xác nghĩa đối lập (single burst vs. multiple generations) và lọt vừa khít giữa cặp dấu phẩy có sẵn.'),
                ('Double Punctuation / Illegal Semicolon', 'Cấm đặt chấm phẩy giữa Chủ ngữ ("Hubble spectral surveys...") và Động từ ("uncovered").'),
                ('Double Punctuation / Illegal Semicolon', 'Cấm đặt chấm phẩy ngay trước động từ chính "uncovered".'),
                ('Wrong Meaning', 'therefore chỉ hệ quả — sai hoàn toàn quan hệ tương phản giữa 1 đợt hình thành và nhiều thế hệ sao.'),
            ]
        ),
        q_item(
            'm1_m2h_q18', 18, 'Standard English Conventions', 'Boundaries', 'Elite (750+)',
            '<p>Although medieval guild ledgers rarely recorded the individual names of female manuscript illuminators working inside monastic workshops ______ marginal self-portraits signed by nuns such as Guda of Frankfurt provide unmistakable proof of their artistic authorship.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['; nevertheless,', ', nevertheless,', '.', ','],
            'D',
            'Bẫy Double Contrast + DC Boundary! Đầu câu đã có "Although..." → Toàn bộ phần trước chỗ trống là 1 Dependent Clause (DC) mang sẵn nghĩa đối lập. Vì vậy: (1) CẤM dùng chấm (.) hay chấm phẩy (;) sau DC (loại A và C); (2) CẤM lặp thêm từ đối lập "nevertheless" sau "Although" (loại A và B) → Chỉ duy nhất D (`,`) đúng chuẩn `DC , IC`!',
            'Đã có "Although" ở đầu câu → KHÔNG chấm/chấm phẩy, KHÔNG thêm "but/however/nevertheless" → chỉ cần 1 dấu phẩy đơn!',
            [
                ('Semicolon After DC + Double Contrast', 'Vừa sai dấu chấm phẩy sau mệnh đề phụ "Although" vừa lặp từ đối lập "nevertheless".'),
                ('Double Contrast Trap', 'Không bao giờ dùng đồng thời cả "Although" và "nevertheless" cho cùng hai mệnh đề.'),
                ('Period After DC', 'Dấu chấm cắt cụt mệnh đề "Although..." thành câu thiếu mệnh đề chính (Fragment).'),
                ('Đáp án đúng', 'Dấu phẩy đơn nối hoàn hảo Dependent Clause ("Although...") với Independent Clause ("marginal self-portraits... provide...").'),
            ]
        ),
        q_item(
            'm1_m2h_q19', 19, 'Standard English Conventions', 'Boundaries', 'Hard',
            '<p>The newly commissioned opera house features an unusual acoustic canopy suspended above the ______ an undulating lattice of solid ash ribs tuned mathematically to scatter soprano overtones evenly toward the rear balcony.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['orchestra pit;', 'orchestra pit:', 'orchestra pit', 'orchestra pit, it is'],
            'B',
            'Vế trái là IC hoàn chỉnh ("The newly commissioned opera house features an unusual acoustic canopy suspended above the orchestra pit"). Vế phải là Cụm danh từ giải thích chi tiết tán âm học đó là gì ("an undulating lattice of solid ash ribs..." — KHÔNG có động từ chia thì, không phải IC!). Nối `IC : Phrase giải thích` → chọn dấu hai chấm (:) = B! (A tạo Fragment sau `;`; C làm dính danh từ "pit an undulating lattice"; D tạo Comma Splice!).',
            'Kiểm tra vế sau: không có động từ chia thì ("tuned" là phân từ quá khứ) → không phải IC → gạch ngay `;` (A) và bẫy Comma Splice `, it is` (D)!',
            [
                ('Semicolon + Fragment', 'Vế sau chỉ là cụm danh từ ("an undulating lattice..."), không phải IC nên cấm dùng chấm phẩy.'),
                ('Đáp án đúng', 'IC hoàn chỉnh + dấu hai chấm (:) mở ra cụm mô tả giải thích trực tiếp cho "an unusual acoustic canopy".'),
                ('Missing Punctuation', 'Thiếu dấu câu khiến "orchestra pit" đụng thẳng vào "an undulating lattice".'),
                ('Comma Splice', 'Đưa chủ ngữ + động từ "it is" vào sau dấu phẩy tạo lỗi 2 IC nối bằng dấu phẩy.'),
            ]
        ),

        # --- Q20-Q22: Form, Structure, and Sense (Elite 750+) ---
        q_item(
            'm1_m2h_q20', 20, 'Standard English Conventions', 'Form, Structure, and Sense', 'Elite (750+)',
            '<p>Submerged thirty meters beneath the silt of Alexandria’s eastern harbor ______ the colossal granite sphinxes and temple columns of the sunken royal quarter, mapped piece by piece through sonar surveys since 1996.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['rests', 'is resting', 'rest', 'resting'],
            'C',
            'Câu Đảo Ngữ (Inverted Subject)! Cụm phân từ mở đầu ("Submerged thirty meters beneath the silt...") không phải chủ ngữ. Chủ ngữ thật nằm PHÍA SAU động từ là chủ ngữ ghép SỐ NHIỀU: "the colossal granite <b>sphinxes and temple columns</b>" → Cần Finite Verb SỐ NHIỀU → Chọn "rest" (C)!',
            'Mở đầu bằng V-ed ("Submerged...") + sau chỗ trống là danh từ ghép số nhiều ("sphinxes and temple columns") → Đảo ngữ chia SỐ NHIỀU!',
            [
                ('Inverted Subject Trap', 'rests là số ít — bị lừa bởi danh từ số ít "harbor" đứng gần chỗ trống.'),
                ('Inverted Subject Trap', 'is resting vừa sai số ít vừa sai thì cho di tích nằm hàng nghìn năm.'),
                ('Đáp án đúng', 'rest (động từ chia thì số nhiều) khớp hoàn hảo với chủ ngữ đảo "the colossal granite sphinxes and temple columns".'),
                ('Non-Finite Fragment', 'resting là V-ing khiến câu không có động từ chia thì.'),
            ]
        ),
        q_item(
            'm1_m2h_q21', 21, 'Standard English Conventions', 'Form, Structure, and Sense', 'Elite (750+)',
            '<p>Celebrated across Latin America for fusing Indigenous Andean pentatonic scales with lush European orchestral harmonies, ______</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            [
                'composer Gabriela Lena Frank’s string quartets are performed by ensembles worldwide.',
                'worldwide ensembles regularly perform the string quartets of composer Gabriela Lena Frank.',
                'it is composer Gabriela Lena Frank whose string quartets have earned international renown.',
                'composer Gabriela Lena Frank has composed string quartets performed by ensembles worldwide.'
            ],
            'D',
            'Bẫy Sở Hữu Cách Giả Chủ Ngữ 750+! Cụm mở đầu "Celebrated across Latin America for fusing..." mô tả NGƯỜI NHẠC SĨ (Gabriela Lena Frank). Trong A, chủ ngữ thật là "string quartets" (những bản tứ tấu không thể tự "fusing"!). Trong B, chủ ngữ là "worldwide ensembles". Trong C là chủ ngữ giả "it". Duy nhất D đặt trực tiếp "composer Gabriela Lena Frank" làm chủ ngữ ngay sau dấu phẩy!',
            'Gạch thẳng bẫy Possessive Subject (A: "Gabriela Lena Frank’s string quartets" có chủ ngữ là "string quartets", KHÔNG phải Gabriela Lena Frank!).',
            [
                ('Possessive Subject Trap', 'Chủ ngữ ngữ pháp của A là "string quartets", không khớp logic với cụm mô tả người sáng tác "fusing...".'),
                ('Dangling Modifier', 'Chủ ngữ là "worldwide ensembles", không phải nhà soạn nhạc.'),
                ('Dummy Subject Trap', 'Chủ ngữ giả "it" làm gãy liên kết trực tiếp với cụm phân từ mở đầu.'),
                ('Đáp án đúng', 'Đặt đúng chủ ngữ "composer Gabriela Lena Frank" ngay sau dấu phẩy, khớp hoàn hảo với "Celebrated... for fusing".'),
            ]
        ),
        q_item(
            'm1_m2h_q22', 22, 'Standard English Conventions', 'Form, Structure, and Sense', 'Elite (750+)',
            '<p>By the time astronomers confirmed the existence of Jupiter’s faint gossamer dust rings using Voyager 1 imagery in 1979, theorists studying planetary dynamics ______ for nearly a decade that micrometeorites blasting tiny inner moons could sustain tenuous ring bands.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['had hypothesized', 'hypothesize', 'will hypothesize', 'are hypothesizing'],
            'A',
            'Mỏ neo thời gian Past Perfect kinh điển: "<b>By the time</b> astronomers confirmed... in 1979" (mốc quá khứ 1979) + hành động đã kéo dài trước đó gần 10 năm ("for nearly a decade" trước năm 1979) → Quá khứ hoàn thành "had hypothesized" (A)!',
            'Công thức bất bại: `By the time + [Past Simple 1979]` + `for nearly a decade` → `had + V3`!',
            [
                ('Đáp án đúng', 'had hypothesized (Quá khứ hoàn thành) khớp tuyệt đối mốc xảy ra suốt gần 10 năm TRƯỚC sự kiện quá khứ 1979.'),
                ('Tense Mismatch', 'Hiện tại đơn không khớp mốc quá khứ 1979.'),
                ('Tense Mismatch', 'Thì tương lai vô lý với sự kiện năm 1979.'),
                ('Tense Mismatch', 'Hiện tại tiếp diễn sai hoàn toàn khung thời gian quá khứ.'),
            ]
        ),

        # --- Q23-Q25: Expression of Ideas — Transitions (Elite 750+) ---
        q_item(
            'm1_m2h_q23', 23, 'Expression of Ideas', 'Transitions', 'Elite (750+)',
            '<p>Early critics assumed that the steep, narrow stone stairways connecting residential terraces at Machu Picchu were built solely to save quarried granite. ______, modern drainage simulations reveal that the stepped terraces and stair channels functioned together as a precision stormwater grid capable of shedding two meters of annual mountain rain without triggering landslides.</p>',
            'Which choice completes the text with the most logical transition?',
            ['In fact', 'In reality', 'Accordingly', 'Similarly'],
            'B',
            'Cặp sát thủ Hard Module 2 (`In fact` vs. `In reality`)! Câu 1 nêu một giả định SAI LẦM/HẸP HÒI ("Early critics assumed... solely to save granite"). Câu 2 phơi bày sự thật phức tạp hoàn toàn ngược lại (hệ thống thoát nước chính xác chống sạt lở). Trên Digital SAT, "In reality" dùng để lật ngược giả định sai, còn "In fact" chỉ dùng để củng cố CÙNG CHIỀU! Chọn B!',
            'Nhớ ranh giới tuyệt đối: "assumed [Wrong View]" → "In reality, [True Explanation]" (KHÔNG chọn "In fact"!).',
            [
                ('In Fact Trap', 'Trên Digital SAT, "In fact" củng cố cùng chiều câu trước chứ không lật ngược giả định sai.'),
                ('Đáp án đúng', 'In reality lật ngược chính xác giả định đơn giản trước đó bằng kết quả mô phỏng thoát nước hiện đại.'),
                ('Wrong Relationship (Cause-Effect)', 'Accordingly = do đó, sai hoàn toàn hướng tương phản.'),
                ('Wrong Relationship (Addition)', 'Similarly = tương tự, ngược hẳn hướng phản biện.'),
            ]
        ),
        q_item(
            'm1_m2h_q24', 24, 'Expression of Ideas', 'Transitions', 'Elite (750+)',
            '<p>Observing that giant kelp canopies dampen coastal wave force, marine restoration teams in Tasmania seeded artificial limestone reefs with heat-tolerant kelp strains. ______, the restored reefs began hosting juvenile abalone and rock lobster populations within eighteen months, offering local fisheries a buffer against warming currents.</p>',
            'Which choice completes the text with the most logical transition?',
            ['Nevertheless', 'Conversely', 'In turn', 'For example'],
            'C',
            'Chuỗi tiến triển tiếp nối/hệ quả dây chuyền: Đội phục hồi gieo tảo bẹ chịu nhiệt lên rạn nhân tạo (Bước 1) → Đến lượt mình / Theo đó, các rạn được phục hồi bắt đầu thu hút bào ngư non và tôm hùm đá quay lại trong vòng 18 tháng (Bước 2 — hệ quả tiếp nối) → "In turn" (C)!',
            '"In turn" diễn tả hoàn hảo hiệu ứng domino / kết quả kế tiếp trong một chuỗi sinh thái (A phục hồi → đến lượt nó tạo ra B)!',
            [
                ('False Contrast', 'Nevertheless sai vì việc xuất hiện bào ngư và tôm hùm là kết quả tích cực tiếp nối, không trái kỳ vọng.'),
                ('False Contrast', 'Conversely chỉ sự đối lập ngược chiều.'),
                ('Đáp án đúng', 'In turn diễn đạt chính xác chuỗi hiệu ứng kế tiếp từ gieo tảo bẹ sang phục hồi quần thể hải sản.'),
                ('Wrong Relationship (Example)', 'Bào ngư và tôm hùm quay lại là hệ quả sinh thái của việc gieo tảo, không phải "ví dụ" về hành động gieo tảo.'),
            ]
        ),
        q_item(
            'm1_m2h_q25', 25, 'Expression of Ideas', 'Transitions', 'Elite (750+)',
            '<p>Classical opera houses built in the nineteenth century relied on curved plaster proscenium arches to project unamplified singers’ voices into balconies fifty meters away. Open-air amphitheaters, ______, lacked overhead ceilings entirely, forcing designers to depend on steep limestone seating tiers and wind-sheltered hillside acoustics.</p>',
            'Which choice completes the text with the most logical transition?',
            ['moreover', 'therefore', 'indeed', 'by contrast'],
            'D',
            'Nhấc chỗ trống lên đầu câu 2: Đối chiếu 2 loại hình nhà hát NGƯỢC HẲN NHAU về cấu trúc âm học — Nhà hát opera có vòm trần thạch cao cong ↔ Nhà hát ngoài trời hoàn toàn KHÔNG có trần, phải dựa vào bậc đá dốc và sườn đồi → Đối chiếu 2 đối tượng trái ngược = "by contrast" (D)!',
            'Nhấc từ nối chen giữa lên đầu câu 2: Nhà hát A có trần vòm ↔ Nhà hát B không có trần = "by contrast"!',
            [
                ('Wrong Relationship (Addition)', 'moreover là bổ sung cùng chiều, sai với sự đối lập có trần vs. không trần.'),
                ('Wrong Relationship (Cause-Effect)', 'Nhà hát ngoài trời không thiếu trần vì lý do nhà hát opera có vòm thạch cao.'),
                ('Emphasis Trap', 'indeed nhấn mạnh cùng một đối tượng/luận điểm, không dùng để chuyển sang đối tượng trái ngược.'),
                ('Đáp án đúng', 'by contrast đối chiếu sắc nét thiết kế âm học giữa nhà hát opera trong nhà và nhà hát ngoài trời.'),
            ]
        ),

        # --- Q26-Q27: Rhetorical Synthesis (Hard / Elite) ---
        q_item(
            'm1_m2h_q26', 26, 'Expression of Ideas', 'Rhetorical Synthesis', 'Elite (750+)',
            '''<p>While researching a topic, a student has taken the following notes:</p>
            <ul>
              <li>In 2021, astrophysicist Dr. Hannah Cho analyzed radio pulses from PSR J0740+6620, one of the most massive neutron stars ever measured.</li>
              <li>Although PSR J0740+6620 packs roughly 2.1 times the Sun’s mass into a sphere, NASA’s NICER X-ray telescope measured its diameter at approximately 24.8 kilometers—unexpectedly wide for such a heavy neutron star.</li>
              <li>Older theoretical models predicted that ultra-heavy neutron stars would collapse tightly into spheres less than 20 kilometers wide as core matter compressed under extreme gravity.</li>
              <li>Cho concluded that subatomic matter inside neutron-star cores is significantly stiffer and more resistant to gravitational squeezing than older models assumed.</li>
            </ul>''',
            'The student wants to present Dr. Cho’s conclusion alongside the specific observational discrepancy that prompted it. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
            [
                'Because NICER measured the massive neutron star PSR J0740+6620 at an unexpectedly wide 24.8 kilometers rather than the sub-20-kilometer diameter older models predicted, Dr. Hannah Cho concluded that neutron-star core matter resists gravitational squeezing more stiffly than previously thought.',
                'Because older models predicted that PSR J0740+6620 would measure 24.8 kilometers wide while NICER found it collapsed below 20 kilometers, Dr. Hannah Cho concluded that core matter is softer than previously assumed.',
                'In 2021, Dr. Hannah Cho used NASA’s NICER X-ray telescope to measure PSR J0740+6620, a neutron star packing roughly 2.1 times the mass of the Sun.',
                'Older theoretical models of neutron stars assumed that extreme gravity compresses subatomic core matter into tight spheres smaller than 20 kilometers wide.'
            ],
            'A',
            'BẪY HARD MODULE 2 FACT-SWAP! Cả A và B đều có cấu trúc "conclusion + discrepancy", NHƯNG B đánh tráo ngược hoàn toàn số liệu (24.8 km vs. <20 km) lẫn kết luận ("softer" thay vì "stiffer")! C và D thiếu hẳn kết luận hoặc độ vênh quan sát. Duy nhất A đúng 100% cả Goal lẫn Fact!',
            'Luôn dành 5 giây kiểm tra chéo số liệu (NICER = 24.8 km > dự đoán cũ <20 km → lõi CỨNG HƠN = stiffer) để bẫy Fact-Swap B không bao giờ lừa được bạn!',
            [
                ('Đáp án đúng', 'Trình bày chính xác cả độ vênh quan sát (24.8 km so với dự đoán <20 km) lẫn kết luận lõi sao cứng hơn giả định cũ.'),
                ('Fact Swap Trap!', 'Đánh tráo ngược 100% số đo NICER với dự đoán cũ và đảo kết luận từ "stiffer" thành "softer"!'),
                ('Missing Discrepancy & Conclusion', 'Chỉ nêu khối lượng sao và tên kính viễn vọng, thiếu cả độ vênh đường kính lẫn kết luận.'),
                ('Missing Observation & Conclusion', 'Chỉ nhắc mô hình lý thuyết cũ mà bỏ qua đo đạc NICER và kết luận của Cho.'),
            ]
        ),
        q_item(
            'm1_m2h_q27', 27, 'Expression of Ideas', 'Rhetorical Synthesis', 'Elite (750+)',
            '''<p>While researching a topic, a student has taken the following notes:</p>
            <ul>
              <li><i>The Great Map of the World</i> (<i>Kunyu Wanguo Quantu</i>) is a monumental 1602 woodblock world map printed in Beijing.</li>
              <li>It was co-created by Ming Dynasty cartographer and astronomer Li Zhizao alongside Italian Jesuit scholar Matteo Ricci.</li>
              <li>Unlike earlier European maps that placed the Atlantic Ocean at the center, the 1602 map centered China and the Pacific Ocean across six folding screen panels.</li>
              <li>The map synthesized European geometric latitude-longitude grids with detailed Chinese geographic records of East Asia and Southeast Asian sea routes.</li>
            </ul>''',
            'The student wants to introduce the 1602 map to an audience unfamiliar with it while emphasizing its collaborative cross-cultural synthesis. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
            [
                'Unlike earlier European maps centered on the Atlantic Ocean, the map arranged six folding screen panels with the Pacific Ocean in the middle.',
                'Co-created in Beijing in 1602 by Ming Dynasty scholar Li Zhizao and Italian Jesuit Matteo Ricci, the woodblock world map <i>Kunyu Wanguo Quantu</i> blended European latitude-longitude grids with detailed Chinese geographic records of East and Southeast Asia.',
                'Printed in Beijing in 1602, <i>Kunyu Wanguo Quantu</i> was displayed across six monumental folding screen panels featuring China near the center.',
                'Matteo Ricci was an Italian Jesuit scholar who collaborated with Ming Dynasty astronomer Li Zhizao in Beijing during the early seventeenth century.'
            ],
            'B',
            'Checklist 2 yêu cầu của Goal: [1] Giới thiệu cho khán giả CHƯA BIẾT bản đồ 1602 ("unfamiliar" → phải nêu rõ đó là bản đồ thế giới in mộc bản năm 1602 tại Bắc Kinh mang tên Kunyu Wanguo Quantu) + [2] Nhấn mạnh sự TỔNG HỢP HỢP TÁC LIÊN VĂN HÓA ("collaborative cross-cultural synthesis" → Li Zhizao + Matteo Ricci; kết hợp lưới kinh-vĩ độ châu Âu với tư liệu địa lý Trung Hoa). A gọi trống không "the map"; C quên yếu tố hợp tác & tổng hợp 2 nền tri thức; D không giới thiệu bản đồ! Duy nhất B hoàn hảo cả 2 vế!',
            'Khóa 2 vế Goal: `unfamiliar audience` (giới thiệu đầy đủ loại hình + tên + năm) + `collaborative cross-cultural synthesis` (cả 2 tác giả + sự kết hợp 2 truyền thống bản đồ)!',
            [
                ('Missing Audience Context & Synthesis', 'Gọi trống không "the map" và chỉ nói bố cục đặt Thái Bình Dương ở giữa, thiếu hợp tác liên văn hóa.'),
                ('Đáp án đúng', 'Giới thiệu trọn vẹn bản đồ 1602 cho người mới biết và làm nổi bật sự kết hợp giữa Li Zhizao–Ricci cùng hai hệ tri thức bản đồ Âu–Á.'),
                ('Missing Cross-Cultural Synthesis', 'Chỉ nêu định dạng bình phong 6 tấm, bỏ qua sự hợp tác Âu–Á và việc kết hợp 2 hệ dữ liệu.'),
                ('Missing Subject (The Map)', 'Chỉ giới thiệu hai nhân vật mà thậm chí không nhắc tới tấm bản đồ 1602!'),
            ]
        ),
    ]
