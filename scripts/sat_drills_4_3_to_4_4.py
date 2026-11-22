# -*- coding: utf-8 -*-
"""
Hand-crafted 1500+ Elite Digital SAT R&W Skill Drills:
- Drill 4.3: Text Structure, Main Purpose & Function (14 Qs)
- Drill 4.4: Cross-Text Connections — Dual-Passage Mapping (14 Qs)
"""

from sat_drills_1_1_and_2_1 import q_item

def get_drill_4_3():
    questions = [
        q_item(
            'd4_3_q1', 1, 'Craft and Structure', 'Text Structure and Purpose', 'Hard',
            '<p>For much of the twentieth century, marine biologists believed that giant kelp forests along California’s coast were governed primarily by water temperature and nutrient upwelling. <u>In 1974, however, ecologist James Estes compared Aleutian islands with thriving sea otter populations against nearby islands where otters had been hunted out, demonstrating that otters keep kelp-grazing sea urchins from stripping reefs bare.</u> Estes’s fieldwork established the concept of a "trophic cascade," proving that apex predators can reshape entire coastal habitats from the top down.</p>',
            'Which choice best describes the function of the underlined sentence in the text as a whole?',
            [
                'It introduces the empirical comparison that overturned an earlier ecological assumption and laid the groundwork for the concept named in the final sentence.',
                'It explains why commercial fur hunting eradicated sea otter populations across the Aleutian islands during the nineteenth century.',
                'It questions whether water temperature and nutrient upwelling exert any measurable influence on California kelp forests.',
                'It describes a methodological flaw in James Estes’s 1974 comparison of Pacific island ecosystems.'
            ],
            'A',
            'Câu 1 nêu quan điểm cũ (rừng tảo bẹ chủ yếu do nhiệt độ nước & dòng trồi dinh dưỡng chi phối). Câu gạch chân đưa so sánh thực địa năm 1974 của Estes (đảo có rái cá vs. đảo mất rái cá) bác bỏ quan điểm cũ đó và dẫn thẳng tới khái niệm "trophic cascade" ở câu 3 → Chọn A!',
            'Khớp chính xác 2 đầu móc của câu gạch chân: ĐẦU TRƯỚC ("however" bác bỏ câu 1) + ĐẦU SAU (làm nền cho "trophic cascade" ở câu 3).',
            [
                ('Đáp án đúng', 'Tóm gọn chính xác cả vai trò bác bỏ giả định cũ (câu 1) lẫn vai trò đặt nền móng cho khái niệm "trophic cascade" (câu 3).'),
                ('Out of Scope', 'Đoạn văn không giải thích nguyên nhân kinh tế/lịch sử của việc săn bắt lông thú.'),
                ('Too Extreme', 'Câu gạch chân không bác bỏ hoàn toàn mọi ảnh hưởng của nhiệt độ hay dinh dưỡng ("any measurable influence").'),
                ('Reversed Logic', 'Bài ca ngợi phát hiện của Estes chứ không nêu lỗi phương pháp nào.'),
            ]
        ),
        q_item(
            'd4_3_q2', 2, 'Craft and Structure', 'Text Structure and Purpose', 'Hard',
            '<p><i>The following text is adapted from a 1904 short story. Clara is visiting her late grandfather’s watchmaking shop for the first time since his passing.</i><br/>The brass pendulums hung motionless behind the counter, each arrested at a different hour as though time itself had fractured on the afternoon he locked the door. Clara reached toward a tarnished pocket watch lying beside his loupe, hesitated, and then wound its stem three gentle turns. When the tiny balance wheel stirred to life with a crisp, steady ticking, the silence in the room seemed less like an emptiness and more like a quiet conversation resumed.</p>',
            'Which choice best describes the overall structure of the text?',
            [
                'It argues that traditional mechanical watchmaking is superior to modern timekeeping, then provides biographical details about Clara’s grandfather.',
                'It establishes a mood of stillness and loss inside an empty workshop, then depicts a small action that softens the narrator’s sense of absence.',
                'It describes a heated disagreement Clara remembers having with her grandfather, then shows her regretting her decision to visit the shop.',
                'It explains the intricate mechanical workings of a pocket watch, then contrasts them with the simpler motion of a brass pendulum.'
            ],
            'B',
            'Cấu trúc 2 chặng cực rõ của trích đoạn văn học: Chặng 1 (câu 1) tả không gian bất động, tĩnh lặng đầy mất mát (quả lắc đứng yên, thời gian như vỡ vụn). Chặng 2 (câu 2–3) tả hành động nhỏ bé vặn dây cót chiếc đồng hồ bỏ túi, khiến sự tĩnh lặng bớt trống rỗng mà trở thành cuộc trò chuyện tiếp nối → Chọn B!',
            'Trong Overall Structure của đoạn văn học, luôn theo dõi sự chuyển dịch TÂM TRẠNG/KHÔNG KHÍ từ nửa đầu sang nửa cuối!',
            [
                ('Out of Scope', 'Đoạn văn không tranh luận về đồng hồ cơ so với đồng hồ hiện đại.'),
                ('Đáp án đúng', 'Bắt trọn chuyển biến 2 chặng: không khí bất động/mất mát → hành động vặn dây cót làm dịu cảm giác trống vắng.'),
                ('Out of Scope', 'Không hề có bất kỳ cuộc tranh cãi hay sự hối tiếc nào.'),
                ('Literal / Misplaced Focus', 'Tác giả dùng chi tiết đồng hồ để gợi cảm xúc tưởng nhớ chứ không giảng kỹ thuật cơ khí.'),
            ]
        ),
        q_item(
            'd4_3_q3', 3, 'Craft and Structure', 'Text Structure and Purpose', 'Elite (750+)',
            '<p>When urban planners propose converting underused downtown parking lots into public plazas, merchants frequently worry that losing curbside spaces will reduce retail foot traffic. Yet longitudinal sales-tax studies in Madrid, Oslo, and New York City consistently found that pedestrianized streets recorded double-digit revenue increases within two years. <u>Admittedly, businesses selling bulky appliances or wholesale building supplies sometimes require dedicated loading bays near storefronts.</u> Even accounting for those exceptions, however, converting asphalt lots into walkable spaces reliably revitalizes most neighborhood commercial corridors.</p>',
            'Which choice best describes the function of the underlined sentence in the text as a whole?',
            [
                'It demonstrates that the sales-tax studies in Madrid, Oslo, and New York City contained serious accounting errors.',
                'It provides the primary evidence explaining why downtown merchants enthusiastically support removing curbside parking.',
                'It concedes a narrow practical exception to the passage’s general argument before the final sentence reaffirms the broader trend.',
                'It introduces a new policy proposal requiring cities to subsidize appliance stores located near pedestrian plazas.'
            ],
            'C',
            'Từ khóa vàng ngay đầu câu gạch chân: "<b>Admittedly</b>, businesses selling bulky appliances... sometimes require dedicated loading bays" → thừa nhận một NGOẠI LỆ THỰC TẾ HẸP (concedes a narrow exception), rồi ngay sau đó câu cuối dùng "Even accounting for those exceptions, however," để tái khẳng định luận điểm chung! Chọn C!',
            'Nhìn thấy "Admittedly / Granted / To be sure" ở câu gạch chân + "Still / Even so / However" ở câu kế tiếp → 100% chức năng là CONCEDE A LIMITATION / EXCEPTION!',
            [
                ('Out of Scope', 'Không hề chỉ ra lỗi kế toán nào trong các nghiên cứu thuế doanh thu.'),
                ('Contradiction', 'Đoạn văn nói thương nhân lo ngại (worry), không nói họ hào hứng ủng hộ.'),
                ('Đáp án đúng', 'Khớp từng chi tiết tu từ: nhượng bộ một ngoại lệ hẹp (cửa hàng đồ cồng kềnh) trước khi câu cuối khẳng định lại xu hướng chung.'),
                ('Out of Scope', 'Không đề xuất chính sách trợ cấp tài chính nào.'),
            ]
        ),
        q_item(
            'd4_3_q4', 4, 'Craft and Structure', 'Text Structure and Purpose', 'Hard',
            '<p>Unlike modern violins, whose strings are wound with synthetic cores or steel under high tension, seventeenth-century Baroque violins used gut strings made from twisted sheep intestine paired with a lighter, outward-curved bow. Because this setup generated lower downward pressure on the bridge, Baroque instruments produced a softer, more transparent articulation that allowed individual contrapuntal lines in chamber ensembles to remain crisp without overpowering one another.</p>',
            'Which choice best states the main purpose of the text?',
            [
                'To argue that contemporary orchestras should abandon steel strings in favor of historical gut strings.',
                'To trace the economic history of sheep-intestine string workshops in seventeenth-century Italy.',
                'To criticize modern violin makers for altering the bridge curvature of Baroque instruments.',
                'To explain how the physical construction of Baroque violins shaped their distinctive acoustic qualities.'
            ],
            'D',
            'Câu 1 mô tả cấu tạo vật lý của đàn violin Baroque (dây ruột cừu, cung nhẹ cong ngoài, lực ép thấp). Câu 2 dùng "Because this setup..." giải thích cấu tạo đó tạo ra chất âm thanh thoát, sắc nét cho nhạc đối âm ra sao → Mục đích chính: giải thích cấu tạo vật lý định hình đặc tính âm học (D)!',
            'Kiểm tra giọng điệu (Tone Check): đoạn văn hoàn toàn trung tính mô tả – giải thích ("to explain"), loại ngay các động từ mang tính chỉ trích/kêu gọi ("argue should abandon", "criticize")!',
            [
                ('Wrong Tone / Out of Scope', 'Tác giả chỉ giải thích khách quan chứ không kêu gọi dàn nhạc hiện đại từ bỏ dây thép.'),
                ('Out of Scope', 'Không hề nhắc lịch sử kinh tế các xưởng sản xuất dây ở Ý.'),
                ('Wrong Tone', 'Không có thái độ chỉ trích thợ làm đàn hiện đại.'),
                ('Đáp án đúng', 'Bao quát trọn vẹn cả 2 câu: cấu tạo vật lý (physical construction) → đặc trưng âm học (distinctive acoustic qualities).'),
            ]
        ),
        q_item(
            'd4_3_q5', 5, 'Craft and Structure', 'Text Structure and Purpose', 'Elite (750+)',
            '<p>Astronomers have long debated why the Sun’s outer atmosphere—the corona—burns at over one million degrees Celsius while the visible solar surface below sits at roughly 5,500 degrees. Two competing hypotheses dominated for decades: one attributed the heat to Alfvén magnetic waves rippling upward, while the other pointed to millions of microscopic "nanoflares" erupting constantly across the magnetic field. Recent data from NASA’s Parker Solar Probe indicate that both mechanisms operate simultaneously, with nanoflares dominating in dense active regions and magnetic waves transferring energy across quieter coronal holes.</p>',
            'Which choice best describes the overall structure of the text?',
            [
                'It poses an enduring scientific puzzle, outlines two rival hypotheses, and presents recent findings that reconcile both explanations across different zones.',
                'It summarizes a classic astrophysical paradox, proves why two early theories were completely mistaken, and proposes a third unrelated cause.',
                'It explains the engineering architecture of the Parker Solar Probe, then lists several solar phenomena the spacecraft failed to measure.',
                'It contrasts the temperature of the Sun’s core with that of neighboring stars before questioning the reliability of solar probes.'
            ],
            'A',
            'Cấu trúc 3 nhịp hoàn hảo: (1) Nêu bài toán hóc búa lâu năm ("long debated why the corona burns at over 1 million °C"), (2) Trình bày 2 giả thuyết cạnh tranh (Alfvén waves vs. nanoflares), (3) Dữ liệu Parker Solar Probe dung hòa (reconcile) cả hai cơ chế cùng vận hành ở hai vùng khác nhau → Chọn A!',
            'Nhớ động từ tu từ 750+: "reconcile" = dung hòa hai giả thuyết tưởng như đối lập bằng cách chỉ ra cả hai cùng đúng ở những điều kiện khác nhau!',
            [
                ('Đáp án đúng', 'Khớp từng nhịp 1 → 2 → 3 của đoạn văn, đặc biệt chính xác ở động từ "reconcile both explanations".'),
                ('Contradiction', 'Dữ liệu mới KHÔNG chứng minh hai thuyết cũ sai hoàn toàn, mà chứng minh cả hai cùng hoạt động!'),
                ('Out of Scope', 'Không mô tả cấu tạo kỹ thuật tàu vũ trụ hay những thất bại đo đạc.'),
                ('Out of Scope', 'Không so sánh với các ngôi sao lân cận và không nghi ngờ độ tin cậy của tàu thăm dò.'),
            ]
        ),
        q_item(
            'd4_3_q6', 6, 'Craft and Structure', 'Text Structure and Purpose', 'Hard',
            '<p><i>The following text is from an 1898 poem describing a coastal lighthouse seen through an autumn fog.</i><br/>No harbor bell proclaims its watchful post,<br/>No gilded spire commands the evening sky;<br/>Yet steady through the shifting gray it sends<br/>A narrow silver finger out to sea,<br/>And where the hidden reef awaits the keel,<br/>That quiet beam writes safety on the dark.</p>',
            'Which choice best states the main purpose of the text?',
            [
                'To lament that modern lighthouses have replaced traditional harbor bells along rocky coastlines.',
                'To emphasize the understated yet vital protective role of a lighthouse guiding ships past unseen hazards.',
                'To warn sailors against navigating coastal waters during severe autumn storms.',
                'To contrast the architectural grandeur of gilded spires with the decay of an abandoned lighthouse.'
            ],
            'B',
            '2 dòng đầu nhấn mạnh vẻ khiêm nhường, không phô trương ("No harbor bell... No gilded spire"). 4 dòng sau dùng "Yet" làm nổi bật tia sáng thầm lặng nhưng sống còn dẫn đường qua bãi đá ngầm ("writes safety on the dark") → Mục đích chính: tôn vinh vai trò bảo vệ thầm lặng nhưng thiết yếu của ngọn hải đăng (B)!',
            'Với thơ cổ trên SAT, luôn tìm từ chuyển hướng ("Yet / But") ở giữa bài — đó chính là trái tim thông điệp của nhà thơ!',
            [
                ('Literal Misreading', 'Bài thơ không than phiền chuyện hải đăng thay thế chuông cảng; câu 1 chỉ nhấn mạnh sự yên lặng không ồn ào.'),
                ('Đáp án đúng', 'Bắt trọn cả hai sắc thái: "understated" (không chuông, không tháp dát vàng) + "vital protective role" (writes safety on the dark).'),
                ('Wrong Purpose', 'Bài thơ ca ngợi ngọn đèn an toàn chứ không viết như lời cảnh báo cấm đi biển.'),
                ('Contradiction', 'Ngọn hải đăng đang hoạt động bền bỉ ("steady... sends"), hoàn toàn không bị bỏ hoang (abandoned).'),
            ]
        ),
        q_item(
            'd4_3_q7', 7, 'Craft and Structure', 'Text Structure and Purpose', 'Elite (750+)',
            '<p>Linguists studying sign languages have demonstrated that facial expressions such as raised eyebrows or furrowed brows do not merely convey emotion; they function as mandatory grammatical markers equivalent to word order or intonation in spoken languages. <u>In American Sign Language, for instance, signing the exact same sequence of manual words with raised eyebrows turns a declarative statement into a yes-or-no question, whereas lowered eyebrows signal an open-ended "wh-" question.</u> Recognizing these non-manual signals is therefore essential for developing accurate automated sign-language translation software.</p>',
            'Which choice best describes the function of the underlined sentence in the text as a whole?',
            [
                'It qualifies the claim in the first sentence by showing that facial expressions are optional in American Sign Language.',
                'It contrasts the grammatical complexity of American Sign Language with the simpler structure of spoken English.',
                'It provides a concrete linguistic illustration of the general grammatical principle stated in the preceding sentence.',
                'It explains the computer-vision algorithms engineers use to build automated sign-language translation software.'
            ],
            'C',
            'Tín hiệu quá rõ: "In American Sign Language, <b>for instance</b>," → đưa ra một ví dụ cụ thể bằng ASL (nhướng mày = câu hỏi Yes/No; hạ mày = câu hỏi Wh-) để MINH HỌA cho nguyên tắc ngữ pháp tổng quát vừa nêu ở câu 1 → Chọn C!',
            'Nhìn thấy "for instance / for example" ở đầu câu gạch chân → động từ tu từ chuẩn là "illustrate / provide a concrete example of the preceding claim"!',
            [
                ('Contradiction', 'Câu gạch chân củng cố tính bắt buộc ngữ pháp, không hề nói biểu cảm khuôn mặt là tùy chọn.'),
                ('Out of Scope', 'Không nói tiếng Anh nói có cấu trúc "đơn giản hơn".'),
                ('Đáp án đúng', 'Minh họa cụ thể bằng trường hợp ASL cho nguyên lý ngữ pháp khái quát ở câu 1.'),
                ('Out of Scope', 'Thuật toán thị giác máy tính không hề được trình bày trong câu gạch chân.'),
            ]
        ),
        q_item(
            'd4_3_q8', 8, 'Craft and Structure', 'Text Structure and Purpose', 'Elite (750+)',
            '<p>Art historians frequently treat Renaissance bronze statues as the solitary triumphs of master sculptors such as Donatello or Verrocchio. Examining Florentine guild contracts and foundry account books, however, scholar Elena Conti reveals that casting a single life-size figure required intricate coordination among wax modelers, furnace builders, metallurgists who calibrated tin-copper alloys, and chasers who polished the cooled surface. <u>Even the master’s signature on the finished plinth reflected legal workshop responsibility rather than sole physical authorship.</u></p>',
            'Which choice best describes the function of the underlined sentence in the text as a whole?',
            [
                'It introduces archival proof that Renaissance sculptors frequently forged one another’s signatures on bronze plinths.',
                'It challenges Elena Conti’s argument by showing that master sculptors personally executed every stage of bronze casting.',
                'It explains the metallurgical formula Florentine foundries used to calibrate tin and copper alloys.',
                'It reinforces Conti’s thesis about collective workshop production by reframing an apparent sign of individual authorship.'
            ],
            'D',
            'Câu 2 nêu luận điểm của Elena Conti: đúc tượng đồng là công trình tập thể của cả xưởng gồm nhiều nghệ nhân. Câu gạch chân ("Even the master’s signature... reflected legal workshop responsibility rather than sole physical authorship") lấy ngay chi tiết tưởng như chứng minh công lao cá nhân (chữ ký bậc thầy trên bệ tượng) và diễn giải lại nó để CỦNG CỐ SÂU HƠN luận điểm sản xuất tập thể của Conti! Chọn D!',
            'Từ "Even..." ở câu cuối thường báo hiệu tác giả đang đẩy mạnh/củng cố luận điểm chính bằng cách hóa giải một phản ví dụ tiềm tàng!',
            [
                ('Distortion / Out of Scope', 'Không hề có chuyện giả mạo chữ ký (forged) — chữ ký thể hiện trách nhiệm pháp lý của chủ xưởng.'),
                ('Reversed Logic', 'Câu gạch chân củng cố chứ không bác bỏ luận điểm của Conti.'),
                ('Out of Scope', 'Không nói tới công thức hợp kim thiếc – đồng.'),
                ('Đáp án đúng', 'Củng cố luận điểm sản xuất tập thể bằng cách diễn giải lại ý nghĩa của chữ ký chủ xưởng trên bệ tượng.'),
            ]
        ),
        q_item(
            'd4_3_q9', 9, 'Craft and Structure', 'Text Structure and Purpose', 'Hard',
            '<p>In 2020, wildlife geneticists analyzing museum pelts of the extinct Tasmanian tiger (<i>Thylacinus cynocephalus</i>) discovered unexpectedly low genetic diversity dating back tens of thousands of years—long before European settlers arrived in Tasmania in 1803. While nineteenth-century bounty hunting undeniably delivered the fatal blow that drove the marsupial predator to extinction in 1936, the researchers note that prolonged geographic isolation on the island had already rendered the population genetically vulnerable to disease and environmental shifts.</p>',
            'Which choice best states the main purpose of the text?',
            [
                'To show that long-term genetic vulnerability predated, and compounded the impact of, nineteenth-century human hunting in the Tasmanian tiger’s extinction.',
                'To argue that nineteenth-century bounty hunting played no meaningful role in the disappearance of the Tasmanian tiger.',
                'To describe the preservation techniques museums use to extract DNA from historical animal pelts.',
                'To compare the genetic diversity of the Tasmanian tiger with that of surviving Australian marsupials.'
            ],
            'A',
            'Đoạn văn kết hợp 2 sự thật: (1) Săn bắt thế kỷ 19 đúng là đòn chí tử (undeniably delivered the fatal blow), NHƯNG (2) dữ liệu DNA cho thấy sự nghèo nàn di truyền do cô lập địa lý đã diễn ra hàng vạn năm trước đó, khiến quần thể vốn dễ tổn thương sẵn → Chọn A! Tránh bẫy Too Extreme B ("no meaningful role")!',
            'Khi đoạn văn có câu "While X undeniably..., Y had already..." → đáp án đúng phải giữ đủ cả 2 vế mà không xóa bỏ X!',
            [
                ('Đáp án đúng', 'Phản ánh trọn vẹn sự cộng hưởng giữa tình trạng dễ tổn thương di truyền lâu dài và đòn chí tử từ săn bắt thế kỷ 19.'),
                ('Contradiction / Too Extreme', 'Trái thẳng với "bounty hunting undeniably delivered the fatal blow".'),
                ('Out of Scope', 'Không mô tả quy trình kỹ thuật tách chiết DNA trong bảo tàng.'),
                ('Out of Scope', 'Không so sánh với các loài thú có túi còn sống ở Úc.'),
            ]
        ),
        q_item(
            'd4_3_q10', 10, 'Craft and Structure', 'Text Structure and Purpose', 'Hard',
            '<p>Early economic textbooks modeled human consumers as purely rational utility maximizers who weigh every purchase with cold mathematical consistency. Behavioral economists Daniel Kahneman and Amos Tversky dismantled that idealization through simple choice experiments: people routinely felt the pain of losing $100 roughly twice as intensely as the pleasure of gaining $100. That asymmetry—termed "loss aversion"—helped explain puzzling real-world habits, from investors holding losing stocks too long to shoppers balking at tiny surcharge fees.</p>',
            'Which choice best describes the overall structure of the text?',
            [
                'It defends classical economic theory against criticisms raised by behavioral psychologists.',
                'It contrasts an older idealized model of decision-making with experimental findings that revealed an asymmetrical bias, then notes real-world behaviors explained by that bias.',
                'It traces the biographical partnership of Kahneman and Tversky before proposing reforms to stock-market regulation.',
                'It lists several irrational habits among retail shoppers, then concludes that no mathematical model can predict human spending.'
            ],
            'B',
            'Cấu trúc 3 bước chuẩn mực: (1) Mô hình lý tưởng hóa cũ ("purely rational utility maximizers") → (2) Thí nghiệm của Kahneman & Tversky lật đổ mô hình đó bằng thiên lệch bất đối xứng ("loss aversion": đau mất tiền gấp đôi vui được tiền) → (3) Nêu các hành vi đời thực được giải thích nhờ thiên lệch này (giữ cổ phiếu lỗ, ngại phụ phí) → Chọn B!',
            'Kiểm tra xem đáp án Overall Structure có đủ TẤT CẢ các chặng của đoạn văn theo đúng thứ tự từ câu 1 → câu cuối không.',
            [
                ('Reversed Logic', 'Đoạn văn cho thấy lý thuyết cổ điển bị "dismantled" (phá vỡ), không hề bênh vực nó.'),
                ('Đáp án đúng', 'Khớp từng nhịp: mô hình cũ → bằng chứng thực nghiệm về thiên lệch bất đối xứng → ứng dụng giải thích hành vi thực tế.'),
                ('Out of Scope', 'Không kể tiểu sử và không đề xuất cải cách luật chứng khoán.'),
                ('Wrong Order / Too Extreme', 'Sai thứ tự trình bày và tự bịa kết luận "no mathematical model can predict".'),
            ]
        ),
        q_item(
            'd4_3_q11', 11, 'Craft and Structure', 'Text Structure and Purpose', 'Elite (750+)',
            '<p>Because deep-ocean trenches exceed pressures of one thousand atmospheres, standard rigid-glass submersibles require thick titanium spheres that severely limit maneuverability. Drawing inspiration from the gelatinous, boneless anatomy of Mariana snailfish, robotics engineers in Hangzhou fabricated a soft-bodied untethered robot whose silicone fins flex using artificial muscles. <u>Instead of housing delicate microchips inside a single heavy pressure vessel, the team distributed tiny circuit components directly within the pliable silicone matrix to equalize internal stress.</u> In 2021, the palm-sized machine swam freely at nearly eleven kilometers beneath the Pacific surface.</p>',
            'Which choice best describes the function of the underlined sentence in the text as a whole?',
            [
                'It highlights a structural weakness that prevented the soft-bodied robot from reaching the bottom of the Mariana Trench.',
                'It argues that artificial muscles are less durable than traditional titanium pressure spheres in deep-sea research.',
                'It specifies a key engineering innovation that enabled the robot to withstand extreme pressure without a bulky rigid shell.',
                'It compares the swimming speed of the silicone robot with that of live Mariana snailfish.'
            ],
            'C',
            'Câu 1 nêu hạn chế vỏ titan cồng kềnh; câu 2 giới thiệu robot thân mềm lấy cảm hứng từ cá ốc Mariana; câu gạch chân giải thích chi tiết SÁNG KIẾN KỸ THUẬT CỐT LÕI giúp robot chịu áp suất khổng lồ mà không cần vỏ cứng (phân tán linh kiện mạch trực tiếp vào lớp silicone dẻo để cân bằng ứng suất) → nối sang thành công lặn sâu 11 km ở câu cuối → Chọn C!',
            'Hỏi ngược: "Vì sao tác giả thêm câu này giữa câu giới thiệu robot và câu lặn thành công 11km?" → Để giải thích CƠ CHẾ KỸ THUẬT giúp nó chịu được áp suất 1.000 atm!',
            [
                ('Contradiction', 'Robot đã bơi thành công ở độ sâu gần 11 km chứ không hề thất bại vì lỗi cấu trúc.'),
                ('Reversed Logic', 'Bài đang nêu ưu thế đột phá của thiết kế thân mềm thay cho vỏ titan cứng.'),
                ('Đáp án đúng', 'Nêu rõ cải tiến kỹ thuật then chốt (phân tán vi mạch trong silicone cân bằng áp suất) thay thế khoang chịu áp cồng kềnh.'),
                ('Out of Scope', 'Không có so sánh tốc độ bơi giữa robot và cá ốc thật.'),
            ]
        ),
        q_item(
            'd4_3_q12', 12, 'Craft and Structure', 'Text Structure and Purpose', 'Hard',
            '<p><i>The following text is adapted from a 1922 novel. Dr. Aris has just been offered a prestigious directorship in the capital city, far from the coastal clinic where he has worked for twenty years.</i><br/>He folded the ministry’s embossed letter twice and laid it beside the salt-stained tide chart on his desk. Outside, two fishermen were hauling dories above the wrack line before a squall rolled in, calling out to one another by first names he had known since boyhood. The capital promised marble corridors, generous stipends, and learned committees—everything, in short, except a single window that smelled of low tide or a patient who would remember to leave fresh mackerel on his porch.</p>',
            'Which choice best states the main purpose of the text?',
            [
                'To criticize the ministry for offering inadequate financial compensation to rural physicians.',
                'To show that Dr. Aris has decided to retire from medical practice in order to become a fisherman.',
                'To portray the coastal village as an impoverished community in urgent need of modern hospital corridors.',
                'To convey Dr. Aris’s quiet attachment to his coastal community by contrasting its familiar warmth with the impersonal prestige of the capital.'
            ],
            'D',
            'Tác giả đặt hai thế giới đối lập nhau cực tinh tế: bức thư dập nổi của Bộ, hành lang cẩm thạch, lương bổng hậu hĩnh ở thủ đô vs. bảng thủy triều bám muối, tiếng gọi tên thân thuộc của ngư dân, mùi triều xuống và cá thu bệnh nhân biếu trên hiên nhà → thể hiện tình cảm gắn bó thầm lặng của Dr. Aris với làng biển (D)!',
            'Trong trích đoạn tiểu thuyết, hãy đọc câu cuối ("everything, in short, except...") — chính cụm ngoại trừ đó tiết lộ giá trị nhân vật thực sự trân quý!',
            [
                ('Contradiction', 'Đoạn văn nói thủ đô hứa hẹn "generous stipends" (lương bổng hậu hĩnh), không phải trả lương thấp.'),
                ('Out of Scope', 'Không hề có chi tiết ông muốn nghỉ hưu đi đánh cá.'),
                ('Distortion', 'Làng biển được khắc họa ấm áp thân thuộc chứ không phải khung cảnh nghèo đói đòi hỏi bệnh viện hiện đại.'),
                ('Đáp án đúng', 'Bắt trọn sự tương phản giữa danh vọng lạnh lẽo nơi thủ đô và sự gắn bó thân tình với cộng đồng ven biển.'),
            ]
        ),
        q_item(
            'd4_3_q13', 13, 'Craft and Structure', 'Text Structure and Purpose', 'Elite (750+)',
            '<p>When cities install reflective "cool roofs" painted with high-albedo white coatings, building air-conditioning demand drops sharply during summer heat waves. <u>However, atmospheric modeler Dr. Kenji Watanabe points out that in high-latitude cities with long, frigid winters, those same reflective rooftops also bounce away welcome winter sunlight, slightly increasing seasonal heating fuel consumption.</u> Consequently, urban climate engineers now evaluate roof coatings on an annual net-energy balance rather than relying solely on peak summer cooling metrics.</p>',
            'Which choice best describes the function of the underlined sentence in the text as a whole?',
            [
                'It introduces a seasonal trade-off that explains why urban engineers adopted the broader evaluation standard described in the final sentence.',
                'It proves that reflective white roof coatings fail to lower summer air-conditioning demand in high-latitude cities.',
                'It recommends banning reflective roof coatings in all regions outside tropical latitudes.',
                'It contrasts the financial cost of white paint with that of solar photovoltaic rooftop panels.'
            ],
            'A',
            'Câu 1 nêu lợi ích mùa hè. Câu gạch chân dùng "However" nêu ĐÁNH ĐỔI THEO MÙA ở các thành phố vĩ độ cao (mùa đông phản xạ mất nắng ấm → tăng nhẹ năng lượng sưởi), làm lý do trực tiếp ("Consequently" ở câu 3) khiến kỹ sư chuyển sang đánh giá cân bằng năng lượng ròng cả năm! Chọn A!',
            'Khi câu cuối bắt đầu bằng "Consequently / Therefore", câu gạch chân ngay trước nó luôn đóng vai trò NGUYÊN NHÂN / LÝ DO dẫn tới hành động ở câu cuối!',
            [
                ('Đáp án đúng', 'Khớp hoàn hảo chuỗi 3 câu: nêu sự đánh đổi theo mùa (winter trade-off) giải thích nguyên nhân thay đổi tiêu chuẩn đánh giá ở câu cuối.'),
                ('Contradiction', 'Câu gạch chân không phủ nhận hiệu quả làm mát mùa hè; nó chỉ bổ sung chi phí sưởi mùa đông.'),
                ('Too Extreme', 'Đoạn văn không kêu gọi cấm (banning) — chỉ nói cần tính cân bằng năng lượng cả năm.'),
                ('Out of Scope', 'Không hề nhắc đến pin mặt trời (solar photovoltaic panels) hay giá sơn.'),
            ]
        ),
        q_item(
            'd4_3_q14', 14, 'Craft and Structure', 'Text Structure and Purpose', 'Elite (750+)',
            '<p>Archaeologists excavating Pompeii have uncovered dozens of modest neighborhood eateries known as <i>thermopolia</i>, featuring masonry counters studded with deep terracotta jars called <i>dolia</i>. Because many working-class Roman apartments lacked private kitchens due to cramped quarters and fire hazards, residents purchased hot lentil stews, spiced wine, and salted fish directly from these street counters. Far from being a modern invention of twentieth-century cities, convenient grab-and-go dining was woven into the daily rhythm of ancient Roman urban life.</p>',
            'Which choice best states the main purpose of the text?',
            [
                'To detail the architectural fire-safety codes enforced in ancient Roman apartment buildings.',
                'To show how excavated street-food counters in Pompeii reveal that quick takeout dining was a routine feature of ancient Roman city life.',
                'To argue that twentieth-century fast-food restaurants directly copied recipes preserved inside Pompeian terracotta jars.',
                'To explain why wealthy Roman aristocrats preferred dining at neighborhood <i>thermopolia</i> over hosting private banquets.'
            ],
            'B',
            'Đoạn văn giới thiệu bằng chứng khảo cổ về các quầy <i>thermopolia</i> ở Pompeii, giải thích vì sao cư dân lao động mua đồ ăn nóng tại đây, rồi khái quát ở câu cuối: ăn uống tiện lợi mang đi vốn là nhịp sống thường nhật của đô thị La Mã cổ đại → Chọn B!',
            'Câu cuối ("Far from being a modern invention...") tóm gọn trực tiếp luận điểm trọng tâm (Main Purpose) của toàn đoạn!',
            [
                ('Too Narrow / Out of Scope', 'Nguy cơ cháy nổ chỉ được nhắc thoáng qua như một lý do khiến căn hộ không có bếp, không phải trọng tâm luật PCCC.'),
                ('Đáp án đúng', 'Bao quát đầy đủ cả bằng chứng khảo cổ (street-food counters in Pompeii) và kết luận văn hóa – lịch sử ở câu cuối.'),
                ('Out of Scope / Distortion', 'Bài không nói nhà hàng thế kỷ 20 sao chép trực tiếp công thức món ăn La Mã.'),
                ('Contradiction', 'Đoạn văn nói về tầng lớp lao động ("working-class Roman apartments"), không phải giới quý tộc giàu có.'),
            ]
        ),
    ]
    return {
        'schemaVersion': 1,
        'mode': 'drill',
        'section': 'Reading and Writing',
        'basicInfo': {
            'title': 'Drill 4.3: Text Structure, Main Purpose & Function (14 Qs)',
            'subtitle': 'Luyện chiến thuật Rhetorical Verbs First trên cả văn bản khoa học, lịch sử, nghệ thuật và trích đoạn văn học – thơ thế kỷ 19.',
            'difficultyBadge': 'C&S • Target 1500+',
            'targetTimeMinutes': 15,
        },
        'drillModule': {
            'id': 'drill_4_3_mod',
            'title': 'Skill Drill 4.3: Text Structure, Purpose & Function',
            'timeLimitMinutes': 15,
            'questions': questions,
        },
    }


def get_drill_4_4():
    questions = [
        q_item(
            'd4_4_q1', 1, 'Craft and Structure', 'Cross-Text Connections', 'Hard',
            '<p><b>Text 1</b><br/>Paleontologist Dr. Marcus Hale argues that the sudden disappearance of North America’s Pleistocene megafauna—including mammoths and giant ground sloths—roughly 11,500 years ago resulted almost entirely from intensive hunting by newly arrived human populations, whose stone projectile points appear alongside mammoth bones at several kill sites.</p><p><b>Text 2</b><br/>Analyzing ancient lake-sediment pollen and permafrost DNA across Alaska and the Yukon, ecologist Dr. Natsuki Sato found that mammoth populations had already declined by more than seventy percent during a rapid warming episode that replaced dry grasslands with mossy shrubland centuries before local human hunting intensified. Sato concludes that climate-driven habitat loss severely weakened megafauna before human hunters delivered the final pressure.</p>',
            'Based on the texts, how would Dr. Natsuki Sato (Text 2) most likely respond to Dr. Marcus Hale’s argument (Text 1)?',
            [
                'By contending that climate-driven habitat shifts had already dramatically reduced mammoth populations prior to intensive human hunting, making hunting only a contributing final factor.',
                'By asserting that human hunters never killed mammoths or giant ground sloths anywhere in North America.',
                'By agreeing that human hunting was the sole cause of megafauna extinction while questioning the radiocarbon dates of kill sites.',
                'By claiming that mossy shrubland actually provided mammoths with far more nutritious forage than dry Pleistocene grasslands.'
            ],
            'A',
            'Text 1 quy lỗi gần như hoàn toàn ("almost entirely") cho săn bắt của con người. Text 2 không phủ nhận vai trò cuối cùng của con người ("before human hunters delivered the final pressure"), nhưng chứng minh quần thể voi ma mút đã sụt hơn 70% do biến đổi khí hậu làm mất đồng cỏ trước đó → Partial Agreement + Primary Earlier Cause = Chọn A!',
            'Mẫu kinh điển 750+ của Cross-Text: Text 1 nói "chủ yếu do X" → Text 2 nói "Y đã làm suy yếu trước, X chỉ là đòn cuối" (KHÔNG phủ nhận hoàn toàn X!).',
            [
                ('Đáp án đúng', 'Phản ánh chính xác lập trường hai vế của Sato: mất môi trường sống do khí hậu đã giảm mạnh quần thể trước, còn săn bắt chỉ là áp lực cuối cùng.'),
                ('Overstated Conflict', '"never killed" mâu thuẫn thẳng với câu cuối Text 2 ("before human hunters delivered the final pressure").'),
                ('Reversed Logic', 'Sato phản đối quan điểm "sole cause", không đồng tình với nó.'),
                ('Contradiction', 'Việc đồng cỏ biến thành bụi rêu là nguyên nhân suy giảm (habitat loss), không phải nguồn thức ăn tốt hơn.'),
            ]
        ),
        q_item(
            'd4_4_q2', 2, 'Craft and Structure', 'Cross-Text Connections', 'Hard',
            '<p><b>Text 1</b><br/>Architectural critic Arthur Vance maintains that open-plan corporate offices—stripped of interior walls and private doors—foster spontaneous cross-departmental collaboration by making colleagues constantly visible and accessible to one another throughout the workday.</p><p><b>Text 2</b><br/>Tracking wearable sociometric badges and email logs at two Fortune 500 headquarters before and after a transition from cubicles to open-plan floors, management scholars Ethan Bernstein and Stephen Turban recorded a 70% drop in face-to-face interaction alongside a surge in instant messaging and email. Rather than talking aloud in full view of peers, employees put on headphones to reclaim privacy.</p>',
            'Based on the texts, how would Bernstein and Turban (Text 2) most likely view Arthur Vance’s claim (Text 1)?',
            [
                'They would endorse it as an accurate description of how open-plan offices increase spontaneous spoken conversations.',
                'They would challenge it with empirical evidence showing that removing walls actually reduced face-to-face interaction as workers withdrew into digital communication.',
                'They would argue that Vance’s claim applies exclusively to Fortune 500 technology firms rather than traditional offices.',
                'They would dismiss it because employees in their study refused to wear sociometric tracking badges.'
            ],
            'B',
            'Text 1: Văn phòng không gian mở thúc đẩy tương tác tự phát trực tiếp. Text 2: Dữ liệu thực nghiệm ngược lại 180 độ — tương tác mặt đối mặt GIẢM 70%, nhân viên đeo tai nghe và nhắn tin/email để giữ riêng tư → Direct Empirical Challenge = Chọn B!',
            'So sánh 2 dòng tóm tắt: T1 = Open plan → (+) face-to-face; T2 = Open plan → (−70%) face-to-face, (+) digital → Bác bỏ trực diện!',
            [
                ('Reversed Logic', 'Kết quả Text 2 hoàn toàn trái ngược chứ không ủng hộ nhận định của Vance.'),
                ('Đáp án đúng', 'Nắm chính xác bằng chứng thực nghiệm (giảm tương tác trực tiếp, tăng giao tiếp số) bác bỏ giả định ở Text 1.'),
                ('Out of Scope', 'Text 2 không nói luận điểm của Vance đúng với hãng công nghệ — chính tại 2 công ty lớn tương tác mặt đối mặt đã giảm 70%.'),
                ('Out of Scope', 'Không hề có chuyện nhân viên từ chối đeo thẻ đo.'),
            ]
        ),
        q_item(
            'd4_4_q3', 3, 'Craft and Structure', 'Cross-Text Connections', 'Elite (750+)',
            '<p><b>Text 1</b><br/>Literary scholar Evelyn Cho observes that nineteenth-century serialized novels—published installment by installment in weekly magazines—frequently employed dramatic cliffhangers at chapter endings to keep readers purchasing the next issue. As a result, Cho views serialization primarily as a commercial constraint that disrupted cohesive artistic pacing.</p><p><b>Text 2</b><br/>Examining Charles Dickens’s archived letters to readers during the monthly release of <i>Bleak House</i>, historian David Alston notes that serialization created a lively feedback loop between novelist and public. Although the installment schedule certainly demanded regular suspenseful hooks, Alston contends that reader reactions enabled Dickens to deepen minor characters and sharpen social satire in ways a closed, pre-written book never permitted.</p>',
            'Based on the texts, both Evelyn Cho (Text 1) and David Alston (Text 2) would most likely agree with which statement?',
            [
                'Nineteenth-century serialized publication prevented authors from developing memorable secondary characters.',
                'Reader letters exerted a stronger influence on chapter cliffhangers than magazine sales targets did.',
                'Publishing novels in periodic installments encouraged authors to build recurring moments of suspense into their chapters.',
                '<i>Bleak House</i> would have achieved tighter artistic pacing had it been released all at once as a single volume.'
            ],
            'C',
            'Câu hỏi "BOTH authors would agree" — kiểm tra điều CÓ MẶT Ở CẢ 2 TEXT! Text 1: "frequently employed dramatic cliffhangers at chapter endings". Text 2: "Although the installment schedule certainly demanded regular suspenseful hooks". Điểm đồng thuận duy nhất giữa hai tác giả nằm ngay ở mệnh đề nhượng bộ của Text 2 → C!',
            'Mẹo cực đỉnh cho câu "Both texts would agree": Điểm đồng thuận hầu như luôn ẩn trong mệnh đề nhượng bộ ("Although / While...") ở đầu Text 2!',
            [
                ('Contradiction with Text 2', 'Text 2 nói điều ngược lại: Dickens làm sâu sắc thêm các nhân vật phụ (deepen minor characters).'),
                ('One-Text / Unsupported', 'Text 1 không nhắc tới thư độc giả và Text 2 không so sánh lực tác động giữa thư với mục tiêu doanh số.'),
                ('Đáp án đúng', 'Cả Text 1 ("dramatic cliffhangers") lẫn Text 2 ("certainly demanded regular suspenseful hooks") đều công nhận điểm này.'),
                ('One-Text Only / Out of Scope', 'Text 1 không nhắc Bleak House, còn Text 2 đánh giá rất cao lợi thế sáng tạo của hình thức đăng kỳ.'),
            ]
        ),
        q_item(
            'd4_4_q4', 4, 'Craft and Structure', 'Cross-Text Connections', 'Elite (750+)',
            '<p><b>Text 1</b><br/>Neuroscientist Dr. Rosa Mendez contends that bilingual adults outperform monolinguals on laboratory attention-switching tasks because managing two active language systems every day trains general-purpose executive control networks in the prefrontal cortex.</p><p><b>Text 2</b><br/>In a 2021 meta-analysis pooling 152 studies across twenty-four countries, psychologist Dr. Owen Brooks found that once researchers corrected for publication bias—the tendency for journals to publish positive results while shelving studies showing no difference—the average bilingual advantage on generic attention-switching tests shrank to statistical zero. Brooks suggests that bilingualism yields undeniable communicative and cultural benefits, yet does not reliably enhance non-linguistic executive tests.</p>',
            'Based on the texts, how would Dr. Owen Brooks (Text 2) most likely respond to Dr. Rosa Mendez’s explanation (Text 1)?',
            [
                'By arguing that bilingualism offers no meaningful communicative or cultural advantages over speaking a single language.',
                'By asserting that laboratory attention-switching tests actually measure vocabulary size rather than executive control.',
                'By agreeing that bilingual adults consistently outperform monolinguals on attention-switching tests, but attributing the gap to schooling.',
                'By questioning the premise of Mendez’s explanation, since corrected large-scale data show no consistent bilingual advantage on generic attention-switching tasks.'
            ],
            'D',
            'Text 1 đưa ra cơ chế giải thích CHO GIẢ ĐỊNH rằng người song ngữ vượt trội trong bài test chuyển đổi chú ý. Text 2 dùng phân tích gộp 152 nghiên cứu chứng minh sau khi loại bỏ thiên lệch xuất bản (publication bias), lợi thế đó bằng 0 về mặt thống kê → đánh thẳng vào TIỀN ĐỀ của lời giải thích ở Text 1! Chọn D!',
            'Khi Text 2 phủ nhận chính hiện tượng mà Text 1 đang cố gắng giải thích → động từ chuẩn là "questioning the premise of Text 1’s explanation"!',
            [
                ('Contradiction / Overstated Conflict', 'Text 2 khẳng định rõ song ngữ mang lại "undeniable communicative and cultural benefits" — không hề phủ nhận điều này.'),
                ('Out of Scope', 'Text 2 không nói bài test đo vốn từ vựng.'),
                ('Contradiction', 'Text 2 chứng minh lợi thế co về 0 ("shrank to statistical zero"), không đồng ý rằng song ngữ vượt trội.'),
                ('Đáp án đúng', 'Đánh đúng bản chất phản biện của Brooks: tiền đề mà Mendez đang giải thích không đứng vững sau khi hiệu chỉnh publication bias.'),
            ]
        ),
        q_item(
            'd4_4_q5', 5, 'Craft and Structure', 'Cross-Text Connections', 'Hard',
            '<p><b>Text 1</b><br/>Marine ecologist Dr. Liam O’Connor argues that decommissioning obsolete offshore oil platforms by completely removing their steel jackets restores seafloor ecosystems to their natural pre-industrial state and eliminates long-term industrial debris.</p><p><b>Text 2</b><br/>Underwater surveys of twenty-seven aging oil rigs off southern California led by biologist Dr. Annika Lind revealed that submerged steel latticework supports some of the densest fish biomass per square meter recorded anywhere in the Pacific, sheltering juvenile rockfish from trawling nets. Lind advocates "rigs-to-reefs" policies that cap wells safely and leave cleaned lower structures in place rather than hauling away thriving artificial reefs.</p>',
            'Which choice best describes a key point of disagreement between the authors of Text 1 and Text 2?',
            [
                'Whether removing the submerged steel structures of retired offshore oil platforms is ecologically preferable to leaving them underwater.',
                'Whether offshore oil drilling should be expanded along the coast of southern California.',
                'Whether steel latticework corrodes faster in cold Pacific waters than in warmer oceans.',
                'Whether juvenile rockfish are commercially more valuable than deep-sea crustaceans.'
            ],
            'A',
            'Text 1 ủng hộ tháo dỡ hoàn toàn khung thép giàn khoan cũ để trả lại đáy biển nguyên sơ. Text 2 ủng hộ để lại phần khung thép dưới đáy (đã làm sạch và bịt giếng) vì nó đã biến thành rạn nhân tạo có sinh khối cá cực dày đặc → Tranh luận cốt lõi xoay quanh việc tháo bỏ hoàn toàn hay giữ lại khung thép dưới biển (A)!',
            'Tách riêng lập trường mỗi bên thành 3 từ: T1 = Remove steel jackets; T2 = Leave cleaned jackets as reefs → Điểm bất đồng hiện ra tức thì!',
            [
                ('Đáp án đúng', 'Chốt chuẩn xác trọng tâm bất đồng giữa tháo dỡ hoàn toàn (Text 1) và giữ lại làm rạn nhân tạo (Text 2).'),
                ('Out of Scope', 'Cả hai văn bản đều bàn về giàn khoan ĐÃ NGỪNG HOẠT ĐỘNG (decommissioning / aging), không bàn về mở rộng khai thác mới.'),
                ('Out of Scope', 'Không nhắc tốc độ ăn mòn giữa các đại dương.'),
                ('Out of Scope', 'Không so sánh giá trị thương mại giữa cá và giáp xác.'),
            ]
        ),
        q_item(
            'd4_4_q6', 6, 'Craft and Structure', 'Cross-Text Connections', 'Elite (750+)',
            '<p><b>Text 1</b><br/>Economist Dr. Priya Deshmukh contends that public transit agencies should expand contactless mobile ticketing primarily because faster boarding reduces bus dwell times at busy intersections, allowing existing fleets to complete more daily trips without buying additional vehicles.</p><p><b>Text 2</b><br/>Evaluating ridership data across six European transit networks that adopted mobile tap-to-pay systems, transportation analyst Mateo Silva confirmed measurable reductions in bus boarding delays. Silva emphasizes, however, that eliminating cash fareboxes entirely can inadvertently exclude unbanked and elderly riders unless agencies retain cash-reloading kiosks at neighborhood stations.</p>',
            'Based on the texts, how would Mateo Silva (Text 2) most likely respond to Dr. Priya Deshmukh’s recommendation (Text 1)?',
            [
                'By disputing Deshmukh’s claim that contactless ticketing speeds up passenger boarding times.',
                'By validating the operational speed benefits Deshmukh highlights, while cautioning that cash-accessible options must remain available to avoid excluding vulnerable riders.',
                'By recommending that transit agencies purchase additional buses rather than upgrading fare-collection hardware.',
                'By claiming that European commuters strongly prefer paying with physical coins over contactless mobile cards.'
            ],
            'B',
            'Text 2 xác nhận trực tiếp lợi ích tốc độ của Text 1 ("confirmed measurable reductions in bus boarding delays"), nhưng gắn kèm điều kiện/cảnh báo về công bằng xã hội ("cautioning... unless agencies retain cash-reloading kiosks" để không loại trừ người không có tài khoản ngân hàng và người cao tuổi) → Partial Agreement + Equity Caveat = Chọn B!',
            'Nhận diện cặp cấu trúc "confirmed X. However, Y unless Z" trong Text 2 → đáp án đúng phải chứa cả vế xác nhận X lẫn vế cảnh báo Z!',
            [
                ('Contradiction', 'Silva ĐÃ XÁC NHẬN ("confirmed measurable reductions") chứ không bác bỏ hiệu quả giảm chậm trễ.'),
                ('Đáp án đúng', 'Giữ trọn hai vế của Silva: xác nhận lợi ích tốc độ lên xe và cảnh báo duy trì điểm nạp tiền mặt cho nhóm yếu thế.'),
                ('Out of Scope', 'Silva không khuyến nghị mua thêm xe buýt thay cho nâng cấp vé.'),
                ('Out of Scope', 'Không nói người châu Âu nói chung thích dùng tiền xu hơn.'),
            ]
        ),
        q_item(
            'd4_4_q7', 7, 'Craft and Structure', 'Cross-Text Connections', 'Elite (750+)',
            '<p><b>Text 1</b><br/>Art historian Claire Beaumont attributes the luminous, jewel-like depth of Jan van Eyck’s fifteenth-century oil paintings to a closely guarded workshop secret—specifically, a proprietary amber varnish recipe that van Eyck supposedly refused to share with rival Flemish painters.</p><p><b>Text 2</b><br/>Using non-invasive infrared spectroscopy and microscopic cross-sections on seven authenticated van Eyck panels, conservation scientist Dr. Jonas Vermeer detected standard linseed oil and common pine resin rather than exotic amber compounds. According to Vermeer, van Eyck’s unmatched optical brilliance stemmed not from secret ingredients, but from applying extraordinarily thin translucent glazes in precisely timed layers that allowed light to bounce off the bright chalk ground beneath.</p>',
            'Based on the texts, how do the conclusions of Claire Beaumont (Text 1) and Dr. Jonas Vermeer (Text 2) differ?',
            [
                'Beaumont believes van Eyck used tempera paint instead of oil, whereas Vermeer proves he used linseed oil.',
                'Beaumont argues that van Eyck’s paintings lack luminous depth, whereas Vermeer praises their optical brilliance.',
                'Beaumont credits van Eyck’s luminosity to secret materials, whereas Vermeer attributes it to masterful layering technique using standard materials.',
                'Beaumont focuses on van Eyck’s religious symbolism, whereas Vermeer analyzes the economic cost of Flemish pigments.'
            ],
            'C',
            'Cả hai đều công nhận độ sáng rực rỡ của tranh van Eyck, nhưng bất đồng ở NGUYÊN NHÂN: Text 1 quy cho NGUYÊN LIỆU BÍ MẬT ("secret amber varnish recipe"); Text 2 bằng phân tích quang phổ chỉ ra ông chỉ dùng dầu lanh và nhựa thông phổ thông, còn bí quyết nằm ở KỸ THUẬT PHỦ LỚP MEN MỎNG ("extraordinarily thin translucent glazes in precisely timed layers") → Chọn C!',
            'Tóm gọn bản chất đối lập: Secret Ingredients (T1) vs. Standard Materials + Layering Technique (T2)!',
            [
                ('Fact Distortion', 'Text 1 nói rõ "oil paintings", không hề nói van Eyck dùng màu tempera.'),
                ('Contradiction', 'Cả hai tác giả đều ca ngợi độ sâu rực rỡ ("luminous, jewel-like depth" / "unmatched optical brilliance").'),
                ('Đáp án đúng', 'Tóm gọn sắc nét sự khác biệt giữa nguyên liệu bí truyền (Beaumont) và kỹ thuật phủ lớp bằng vật liệu chuẩn (Vermeer).'),
                ('Out of Scope', 'Không đoạn nào bàn về biểu tượng tôn giáo hay giá thành phẩm màu.'),
            ]
        ),
        q_item(
            'd4_4_q8', 8, 'Craft and Structure', 'Cross-Text Connections', 'Hard',
            '<p><b>Text 1</b><br/>Botanist Dr. Samuel Mensah notes that many tropical orchid species produce no nectar at all, yet still achieve reliable pollination by mimicking the scent and petal geometry of rewarding neighboring flowers, tricking foraging bees into visiting them briefly.</p><p><b>Text 2</b><br/>Tracking solitary bees across Costa Rican cloud forests, ecologist Dr. Elena Alvarez discovered that bees deceived by nectarless orchids quickly learn to recognize the trick and fly substantially farther away before landing on another orchid. Paradoxically, Alvarez found that this frustrated long-distance flight benefits the orchids by promoting cross-pollination between genetically distant plants rather than self-pollination.</p>',
            'Which choice best describes the relationship between Text 1 and Text 2?',
            [
                'Text 2 refutes Text 1 by proving that tropical orchids actually secrete abundant hidden nectar.',
                'Text 2 criticizes the fieldwork methods Dr. Mensah used to catalog orchid petal geometry.',
                'Text 2 argues that deceptive pollination harms orchid reproduction by causing bees to abandon cloud forests entirely.',
                'Text 2 builds on the phenomenon described in Text 1 by revealing an unexpected evolutionary advantage resulting from bees’ reaction to being deceived.'
            ],
            'D',
            'Text 1 mô tả hiện tượng hoa lan không mật đánh lừa ong. Text 2 KHÔNG phản bác Text 1 mà MỞ RỘNG SÂU THÊM: giải thích phản ứng bực tức bay đi thật xa của ong sau khi bị lừa lại vô tình tạo lợi thế tiến hóa bất ngờ (thụ phấn chéo giữa các cây xa nhau về mặt di truyền)! Chọn D!',
            'Đừng mặc định Text 2 lúc nào cũng chống lại Text 1! Khi Text 2 tiếp nối cùng hiện tượng và giải thích thêm lợi ích/cơ chế sâu hơn → "builds on / extends"!',
            [
                ('Contradiction', 'Text 2 tiếp tục nói về "nectarless orchids" (hoa lan không mật), không bác bỏ Text 1.'),
                ('Out of Scope', 'Text 2 không hề phê bình phương pháp nghiên cứu của Dr. Mensah.'),
                ('Reversed Logic', 'Text 2 nói hành vi bay xa của ong mang lại LỢI ÍCH thụ phấn chéo ("benefits the orchids"), không gây hại.'),
                ('Đáp án đúng', 'Phản ánh chính xác mối quan hệ bổ sung – mở rộng: từ hiện tượng đánh lừa (Text 1) sang lợi thế tiến hóa bất ngờ từ phản ứng của ong (Text 2).'),
            ]
        ),
        q_item(
            'd4_4_q9', 9, 'Craft and Structure', 'Cross-Text Connections', 'Elite (750+)',
            '<p><b>Text 1</b><br/>Historian Dr. Rachel Goldstein contends that the rapid growth of seventeenth-century Dutch landscape painting stemmed largely from a newly prosperous Protestant merchant class seeking secular, domestic-sized artworks to decorate townhome parlors rather than monumental cathedral altarpieces.</p><p><b>Text 2</b><br/>Analyzing auction inventories from Haarlem and Delft between 1620 and 1670, economic historian Willem de Vries finds that painters also adopted streamlined "tonal" techniques—using restricted palettes of ochres and grays that dried rapidly—which slashed studio production time in half. De Vries argues that while bourgeois patronage certainly expanded demand, falling unit prices driven by faster painting methods were equally crucial in placing landscapes on ordinary Dutch walls.</p>',
            'Based on the texts, how would Willem de Vries (Text 2) most likely view Dr. Rachel Goldstein’s explanation (Text 1)?',
            [
                'As identifying an important demand-side factor while overlooking supply-side technical innovations that lowered painting prices.',
                'As completely mistaken because seventeenth-century Dutch merchants rarely purchased landscape paintings for their homes.',
                'As overly focused on workshop pigment chemistry at the expense of religious and cultural history.',
                'As valid only for monumental cathedral altarpieces rather than domestic-sized landscapes.'
            ],
            'A',
            'Text 1 tập trung vào phía CẦU (thương nhân giàu có muốn mua tranh nhỏ trang trí nhà). Text 2 xác nhận yếu tố cầu đó ("while bourgeois patronage certainly expanded demand") nhưng nhấn mạnh một yếu tố phía CUNG quan trọng ngang ngửa (kỹ thuật vẽ "tonal" nhanh khô giảm nửa thời gian sản xuất → hạ giá thành) → Chọn A!',
            'Cấu trúc "while X certainly..., Y were equally crucial" = Text 1 nêu đúng một nửa câu chuyện nhưng bỏ sót yếu tố quan trọng ngang hàng!',
            [
                ('Đáp án đúng', 'Khớp tuyệt đối quan điểm của de Vries: thừa nhận yếu tố cầu (Goldstein) và bổ sung đổi mới kỹ thuật phía cung giúp giảm giá thành.'),
                ('Overstated Conflict', 'de Vries khẳng định "bourgeois patronage certainly expanded demand", không bác bỏ nó.'),
                ('Role Swap Trap!', 'Chính de Vries (Text 2) mới là người phân tích kỹ thuật màu vẽ xưởng, KHÔNG phải Goldstein (Text 1)!'),
                ('Contradiction', 'Cả hai văn bản đều bàn về tranh phong cảnh cỡ gia đình, không phải tranh bàn thờ nhà thờ.'),
            ]
        ),
        q_item(
            'd4_4_q10', 10, 'Craft and Structure', 'Cross-Text Connections', 'Hard',
            '<p><b>Text 1</b><br/>Geophysicist Dr. Tariq Al-Mansoor suggests that Mars lost most of its early liquid surface water because the weakening of the Martian magnetic field allowed energetic solar wind particles to strip atmospheric hydrogen and oxygen steadily into outer space.</p><p><b>Text 2</b><br/>Re-examining orbital mineral maps collected by NASA’s Mars Reconnaissance Orbiter, planetary geologist Dr. Eva Scheller estimates that between 30% and 99% of Mars’s ancient water never escaped into space at all; instead, it reacted chemically with basaltic rocks to become permanently locked inside hydrated crust minerals. Scheller acknowledges that atmospheric escape occurred, yet maintains that crustal trapping played a far larger role than space-loss models assumed.</p>',
            'Based on the texts, both Dr. Al-Mansoor (Text 1) and Dr. Scheller (Text 2) would most likely agree with which statement?',
            [
                'Nearly all of Mars’s ancient liquid water remains chemically trapped inside hydrated crustal minerals.',
                'Some portion of early Martian water was lost through atmospheric escape into space.',
                'Mars never possessed sufficient liquid surface water to alter basaltic rocks chemically.',
                'Solar wind stripping ceased entirely before NASA’s Mars Reconnaissance Orbiter mapped the Martian crust.'
            ],
            'B',
            'Câu hỏi "BOTH would agree": Text 1 cho rằng nước Sao Hỏa mất chủ yếu do thoát khí quyển ra không gian. Text 2 cho rằng phần lớn bị khóa trong khoáng vật vỏ đá, NHƯNG thừa nhận rõ ràng ở câu cuối: "Scheller <b>acknowledges that atmospheric escape occurred</b>" → Điểm đồng thuận 100% ở cả 2 đoạn là có một phần nước Sao Hỏa đã thoát ra không gian qua khí quyển (B)!',
            'Một lần nữa: trong câu "Both authors agree", đáp án đúng ẩn gọn gàng trong cụm "acknowledges that..." của Text 2!',
            [
                ('One-Text Only (Text 2)', 'Đây là luận điểm riêng của Scheller (Text 2), mâu thuẫn với Al-Mansoor (Text 1).'),
                ('Đáp án đúng', 'Cả Al-Mansoor (chủ đạo) lẫn Scheller ("acknowledges that atmospheric escape occurred") đều công nhận hiện tượng thoát khí quyển có xảy ra.'),
                ('Contradiction', 'Cả hai văn bản đều giả định Sao Hỏa từng có lượng nước lỏng bề mặt đáng kể thời sơ khai.'),
                ('Out of Scope', 'Không đoạn nào nhắc thời điểm chấm dứt hiện tượng gió Mặt Trời.'),
            ]
        ),
        q_item(
            'd4_4_q11', 11, 'Craft and Structure', 'Cross-Text Connections', 'Elite (750+)',
            '<p><b>Text 1</b><br/>Music theorist Dr. Julian Vance argues that the dramatic emotional impact of Ludwig van Beethoven’s late string quartets arises primarily from his deliberate breaking of Classical formal symmetry—inserting unexpected pauses, abrupt key changes, and six-movement structures that disorient listeners accustomed to four-movement predictability.</p><p><b>Text 2</b><br/>In a computational harmonic study of Beethoven’s Opus 131 quartet, musicologist Dr. Mei-Ling Zhou demonstrates that beneath the work’s unconventional seven-movement exterior lies an unusually tight web of recurring four-note motifs linking the opening fugue directly to the finale. Zhou argues that the quartet feels emotionally devastating not because it abandons structural unity, but because it disguises rigorous thematic coherence beneath apparent fragmentation.</p>',
            'Based on the texts, how would Dr. Mei-Ling Zhou (Text 2) most likely characterize Dr. Julian Vance’s view of Beethoven’s late string quartets (Text 1)?',
            [
                'It fails to recognize that Opus 131 follows a conventional four-movement Classical outline.',
                'It exaggerates the emotional intensity experienced by audiences listening to Beethoven’s late quartets.',
                'It focuses on surface departures from Classical form while missing the deep underlying thematic unity that actually drives the music’s emotional power.',
                'It relies too heavily on computational harmonic software rather than close listening.'
            ],
            'C',
            'Text 1 cho rằng sức mạnh cảm xúc đến từ sự phá vỡ đối xứng hình thức bề ngoài (disorient listeners). Text 2 thừa nhận bề ngoài khác thường ("unconventional seven-movement exterior / apparent fragmentation"), nhưng chỉ ra bên dưới là mạng lưới mô-típ 4 nốt liên kết chặt chẽ — chính sự thống nhất chìm sâu dưới lớp vỡ vụn bề mặt mới tạo sức công phá cảm xúc! Chọn C!',
            'Bắt đúng cặp đối lập tinh tế của Text 2: Surface appearance (apparent fragmentation) vs. Underlying reality (rigorous thematic coherence)!',
            [
                ('Contradiction', 'Text 2 nói rõ Opus 131 có cấu trúc bảy chương khác thường ("unconventional seven-movement exterior"), không phải 4 chương cổ điển.'),
                ('Contradiction', 'Zhou cũng gọi tác phẩm là "emotionally devastating", đồng tình về sức mạnh cảm xúc.'),
                ('Đáp án đúng', 'Bắt trọn lập luận cốt lõi của Zhou: Vance chỉ nhìn lớp phá vỡ hình thức bề ngoài mà bỏ qua tính thống nhất chủ đề sâu bên dưới.'),
                ('Role Swap Trap!', 'Chính Zhou (Text 2) mới là người dùng nghiên cứu tính toán hòa âm, không phải Vance (Text 1)!'),
            ]
        ),
        q_item(
            'd4_4_q12', 12, 'Craft and Structure', 'Cross-Text Connections', 'Hard',
            '<p><b>Text 1</b><br/>Urban forestry advocates routinely promote large-scale "million-tree" planting campaigns as a straightforward, universally beneficial method for cooling overheated cities and offsetting municipal carbon emissions.</p><p><b>Text 2</b><br/>Auditing twenty-two municipal tree-planting initiatives across arid southwestern cities, ecologist Dr. Carlos Mendez found that nearly forty percent of newly planted non-native saplings died within five years due to heat stress and unbudgeted irrigation costs. Mendez contends that tree-planting pledges deliver lasting climate benefits only when cities shift funding from headline sapling counts toward drought-adapted native species and multi-year maintenance.</p>',
            'Based on the texts, how would Dr. Carlos Mendez (Text 2) most likely respond to the campaigns described in Text 1?',
            [
                'By urging cities to cancel all urban forestry programs in southwestern regions permanently.',
                'By arguing that planting trees increases summer urban temperatures rather than cooling cities.',
                'By asserting that non-native saplings require less irrigation than drought-adapted native trees.',
                'By warning that high-volume planting campaigns frequently fall short unless paired with native species selection and sustained maintenance funding.'
            ],
            'D',
            'Text 1 coi chiến dịch trồng triệu cây là giải pháp đơn giản, có lợi phổ quát. Text 2 kiểm toán 22 dự án thấy gần 40% cây ngoại lai chết trong 5 năm do nắng nóng và thiếu ngân sách chăm sóc → chỉ có hiệu quả khí hậu bền vững NẾU chọn loài bản địa chịu hạn và cấp ngân sách duy trì nhiều năm! Chọn D!',
            'Cảnh giác bẫy Overstated Conflict (A: "cancel all programs permanently"): Text 2 dùng cấu trúc "deliver benefits ONLY WHEN..." → góp ý điều kiện để thành công, KHÔNG đòi hủy bỏ toàn bộ!',
            [
                ('Overstated Conflict', 'Mendez không đòi hủy bỏ mọi chương trình trồng cây — ông nêu điều kiện để chúng mang lại lợi ích lâu dài.'),
                ('Out of Scope / Contradiction', 'Mendez không phủ nhận cây xanh giúp làm mát nếu chúng sống sót.'),
                ('Reversed Logic', 'Ngược hoàn toàn: chính cây ngoại lai (non-native) mới chết vì thiếu nước tưới, còn cây bản địa chịu hạn tốt hơn.'),
                ('Đáp án đúng', 'Tóm gọn trọn vẹn cảnh báo thực tế và 2 điều kiện cốt lõi (native species + sustained maintenance) của Mendez.'),
            ]
        ),
        q_item(
            'd4_4_q13', 13, 'Craft and Structure', 'Cross-Text Connections', 'Elite (750+)',
            '<p><b>Text 1</b><br/>Archaeologist Dr. Hannah Brooks argues that the monumental stone circles of Göbekli Tepe in southeastern Turkey—built around 9600 BCE—proves that organized communal religion preceded and actually spurred the invention of agriculture, since hunter-gatherers would have needed to domesticate wild wheat to feed large crowds gathering for seasonal temple feasts.</p><p><b>Text 2</b><br/>Re-evaluating domestic hearth layers, grinding stones, and water cisterns recently excavated around the same enclosures at Göbekli Tepe, archaeologist Dr. Emre Kaya argues that the site was not an uninhabited wilderness sanctuary visited only for rare ceremonies. Instead, Kaya suggests it functioned as a permanent, year-round settlement where ritual pillars and everyday domestic life evolved side by side alongside gradual wild-grain harvesting.</p>',
            'Which choice best describes a fundamental difference between Dr. Brooks’s interpretation (Text 1) and Dr. Kaya’s interpretation (Text 2) of Göbekli Tepe?',
            [
                'Brooks interprets Göbekli Tepe as a ritual gathering site that catalyzed agriculture among visiting hunter-gatherers, whereas Kaya views it as a permanent settlement where ritual and domestic practices co-evolved.',
                'Brooks dates Göbekli Tepe to around 9600 BCE, whereas Kaya proves the enclosures were built thousands of years later.',
                'Brooks contends that Göbekli Tepe residents never harvested wild grain, whereas Kaya argues they relied exclusively on domesticated wheat.',
                'Brooks believes the stone pillars served purely residential purposes, whereas Kaya argues they had no domestic surroundings.'
            ],
            'A',
            'So sánh 2 góc nhìn về Göbekli Tepe: Text 1 (Brooks) = Thánh địa nghi lễ thu hút thợ săn theo mùa → chính lễ hội kích hoạt sự ra đời nông nghiệp. Text 2 (Kaya) = Khu định cư quanh năm (có bếp lửa, cối đá, bể nước) nơi nghi lễ và đời sống thường nhật đồng tiến hóa → Chọn A!',
            'Nhớ kiểm tra bẫy Role Swap (như D đảo ngược Brooks và Kaya!) và Fact Distortion (B bịa bất đồng niên đại, C bịa "exclusively domesticated")!',
            [
                ('Đáp án đúng', 'Khớp 100% hai mô hình diễn giải của Brooks (sanctuary catalyzing agriculture) và Kaya (permanent settlement with co-evolving ritual & domestic life).'),
                ('Out of Scope', 'Kaya không hề phản đối niên đại 9600 BCE.'),
                ('Contradiction / Distortion', 'Kaya nói "gradual wild-grain harvesting", không phải "exclusively domesticated wheat"; còn Brooks cũng nói về thu hoạch/thuần hóa lúa mì hoang.'),
                ('Role Swap Trap!', 'Đảo ngược hoàn toàn quan điểm của hai nhà khảo cổ.'),
            ]
        ),
        q_item(
            'd4_4_q14', 14, 'Craft and Structure', 'Cross-Text Connections', 'Elite (750+)',
            '<p><b>Text 1</b><br/>Behavioral biologist Dr. Fiona Gallagher proposes that urban crows drop hard-shelled walnuts onto paved city streets specifically in front of oncoming cars so that heavy tires will crack the shells open—demonstrating sophisticated causal reasoning about moving vehicles.</p><p><b>Text 2</b><br/>Filming 140 walnut-dropping sequences by crows across four Japanese intersections, ethologist Dr. Kenzo Takahashi observed that crows dropped nuts onto asphalt just as frequently when no cars were approaching as when traffic was heavy; moreover, the birds rarely positioned nuts directly in tire lanes. Takahashi suggests the crows primarily exploit the hard asphalt surface to shatter shells upon impact, with passing cars merely acting as an occasional unintended bonus.</p>',
            'Based on the texts, how would Dr. Kenzo Takahashi (Text 2) most likely respond to Dr. Fiona Gallagher’s proposal (Text 1)?',
            [
                'By agreeing that crows deliberately align walnuts in tire tracks to exploit oncoming vehicles.',
                'By arguing that crows use hard paved roads primarily as a rigid drop surface rather than deliberately timing drops for oncoming car tires.',
                'By claiming that urban crows in Japan have never been observed dropping walnuts onto paved streets.',
                'By asserting that passing tires prevent crows from retrieving cracked walnut kernels safely.'
            ],
            'B',
            'Text 1: Quạ cố tình thả quả óc chó ngay trước xe chạy để bánh xe cán vỡ (suy luận nhân quả về xe). Text 2: Quay 140 lần thấy quạ thả trên đường nhựa nhiều ngang nhau KHI KHÔNG CÓ XE lẫn khi đông xe và hiếm khi đặt đúng vệt bánh xe → Quạ chủ yếu tận dụng MẶT ĐƯỜNG NHỰA CỨNG để làm vỡ khi rơi, còn xe cán qua chỉ là tình cờ ăn may! Chọn B!',
            'Xác định chính xác biến số gây tác động theo mỗi tác giả: T1 = Oncoming Tires; T2 = Hard Asphalt Surface (cars = incidental bonus)!',
            [
                ('Contradiction', 'Takahashi ghi nhận quạ hiếm khi đặt quả đúng vệt bánh xe ("rarely positioned nuts directly in tire lanes").'),
                ('Đáp án đúng', 'Phản ánh chính xác lập luận thay thế của Takahashi: dùng mặt đường cứng làm bệ đập chứ không cố tình căn xe.'),
                ('Contradiction', 'Takahashi đã quay tận 140 lần quạ thả quả óc chó trên đường nhựa ở Nhật!'),
                ('Out of Scope', 'Text 2 gọi xe chạy qua là "occasional unintended bonus", không bàn chuyện xe cản quạ lấy nhân.'),
            ]
        ),
    ]
    return {
        'schemaVersion': 1,
        'mode': 'drill',
        'section': 'Reading and Writing',
        'basicInfo': {
            'title': 'Drill 4.4: Cross-Text Connections — Dual-Passage Mapping (14 Qs)',
            'subtitle': 'Luyện ma trận 4 quan hệ Text 1 ↔ Text 2, câu hỏi Hypothetical Response, Both Agree và chống bẫy Overstated Conflict / Role Swap.',
            'difficultyBadge': 'C&S • Target 1500+',
            'targetTimeMinutes': 16,
        },
        'drillModule': {
            'id': 'drill_4_4_mod',
            'title': 'Skill Drill 4.4: Cross-Text Connections (Dual Passages)',
            'timeLimitMinutes': 16,
            'questions': questions,
        },
    }
