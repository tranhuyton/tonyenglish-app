# -*- coding: utf-8 -*-
"""
Full-Length Adaptive Mock Test #8 — Module 1 (27 Qs, Easy/Medium/Hard Routing Mix, 32 min)
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
            'm8_m1_q1', 1, 'Craft and Structure', 'Words in Context', 'Easy',
            '<p>Unlike imported heating oil, whose market price fluctuates sharply with global supply disruptions, Iceland’s deep volcanic aquifers furnish municipal district-heating utilities with a remarkably ______ thermal supply throughout the subarctic winter.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            ['fragile', 'temporary', 'consistent', 'expensive'],
            'C',
            'Contrast Clue: "Unlike imported heating oil, whose market price fluctuates sharply..." → đối lập với sự biến động thất thường của dầu nhập khẩu, nguồn nước nóng địa nhiệt từ tầng chứa nước núi lửa Iceland cung cấp nhiệt năng ỔN ĐỊNH / ĐỀU ĐẶN suốt mùa đông cận Bắc Cực → "consistent" (C).',
            'Xác định từ khóa tương phản "Unlike... fluctuates sharply" → chọn tính từ trái nghĩa mang sắc thái ổn định đều đặn ("consistent").',
            [
                ('Wrong Context', 'fragile = mong manh dễ vỡ — không hợp bối cảnh nguồn năng lượng địa nhiệt bền vững.'),
                ('Opposite Meaning', 'temporary = tạm thời ngắn hạn — mâu thuẫn với khả năng cung cấp suốt mùa đông.'),
                ('Đáp án đúng', 'consistent = ổn định, đều đặn — đối lập chính xác với sự biến động thất thường ("fluctuates sharply").'),
                ('Wrong Direction', 'expensive = đắt đỏ — bài không so sánh theo hướng địa nhiệt đắt hơn dầu nhập khẩu.'),
            ]
        ),
        q_item(
            'm8_m1_q2', 2, 'Craft and Structure', 'Words in Context', 'Medium',
            '<p>Chemists examining ancient Maya temple murals discovered that heating organic indigo dye inside the microscopic channels of palygorskite clay produces a hybrid blue pigment so chemically ______ that centuries of tropical humidity and weak acids fail to fade its brilliance.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            ['resilient', 'volatile', 'opaque', 'delicate'],
            'A',
            'Cause-Effect Clue: "so chemically ______ that centuries of tropical humidity and weak acids fail to fade its brilliance" → hàng thế kỷ độ ẩm nhiệt đới và axit nhẹ vẫn không làm phai màu → sắc tố cực kỳ BỀN VỮNG / CHỐNG CHỊU TỐT → "resilient" (A).',
            'Cấu trúc "so [adj] that [tác nhân khắc nghiệt] fail to fade" dẫn thẳng đến tính từ chỉ độ bền chống chịu cao ("resilient").',
            [
                ('Đáp án đúng', 'resilient = bền bỉ, chống chịu tốt — khớp tuyệt đối với việc không phai màu trước ẩm nhiệt đới và axit.'),
                ('Opposite Meaning', 'volatile = dễ bay hơi, dễ biến chất — trái ngược hoàn toàn với khả năng giữ màu hàng thế kỷ.'),
                ('Wrong Meaning', 'opaque = đục, không trong suốt — không giải thích vì sao màu không bị axit làm phai.'),
                ('Opposite Meaning', 'delicate = mỏng manh dễ hỏng — trái nghĩa hoàn toàn.'),
            ]
        ),
        q_item(
            'm8_m1_q3', 3, 'Craft and Structure', 'Words in Context', 'Medium',
            '<p>Bioacousticians observing wild Bornean orangutans noticed that individuals frequently cup a hand or hold stripped leaves directly over their mouths while emitting warning "kiss-squeaks," acoustically deepening the call’s frequency to ______ their apparent body size to approaching predators or rivals.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            ['conceal', 'diminish', 'verify', 'exaggerate'],
            'D',
            'Cause-Effect Clue: hạ trầm tần số tiếng rít ("acoustically deepening the call’s frequency") nhằm khiến kích thước cơ thể *có vẻ* ("apparent body size") lớn hơn trước kẻ thù/đối thủ → PHÓNG ĐẠI kích thước cơ thể trong mắt đối phương → "exaggerate" (D).',
            'Trong sinh học âm thanh, giọng trầm hơn gắn với động vật to lớn hơn; kết hợp cụm "apparent body size" → chọn "exaggerate" (phóng đại).',
            [
                ('Wrong Direction', 'conceal = che giấu — đười ươi không giấu kích thước mà cố làm mình nghe to lớn hơn.'),
                ('Opposite Meaning', 'diminish = làm giảm nhỏ đi — trái ngược với mục đích răn đe kẻ thù bằng âm trầm.'),
                ('Wrong Meaning', 'verify = xác minh sự thật — trái với hành vi tạo ảo giác "apparent body size".'),
                ('Đáp án đúng', 'exaggerate = phóng đại — khớp chính xác cơ chế hạ tông âm để tạo ấn tượng thân hình to lớn hơn thực tế.'),
            ]
        ),
        q_item(
            'm8_m1_q4', 4, 'Craft and Structure', 'Words in Context', 'Hard',
            '<p>In his eleventh-century treatise <i>Kitāb al-Manāẓir</i> (<i>Book of Optics</i>), Ibn al-Haytham broke sharply with earlier classical thinkers who accepted ancient visual theories on philosophical authority alone; instead, he insisted on ______ proof gathered through repeatable pinhole-chamber experiments with candles and screens.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            ['conjectural', 'empirical', 'allegorical', 'arbitrary'],
            'B',
            'Contrast + Restatement Clue: đối lập với "accepted ancient visual theories on philosophical authority alone" + giải thích trực tiếp phía sau "gathered through repeatable pinhole-chamber experiments" → bằng chứng THỰC NGHIỆM (dựa trên thí nghiệm có thể lặp lại) → "empirical" (B)!',
            'Manh mối "repeatable... experiments" là định nghĩa trực tiếp của từ học thuật "empirical" (thực nghiệm).',
            [
                ('Opposite Meaning', 'conjectural = mang tính phỏng đoán suông — cùng chiều với suy đoán triết học mà ông phản bác.'),
                ('Đáp án đúng', 'empirical = dựa trên quan sát và thí nghiệm thực chứng — khớp 100% với thí nghiệm buồng tối có thể lặp lại.'),
                ('Wrong Context', 'allegorical = mang tính ngụ ngôn biểu tượng — dùng cho văn học, không dùng cho thí nghiệm quang học.'),
                ('Wrong Meaning', 'arbitrary = tùy tiện, thiếu quy luật — trái ngược với thí nghiệm có kiểm soát và lặp lại.'),
            ]
        ),
        q_item(
            'm8_m1_q5', 5, 'Craft and Structure', 'Words in Context', 'Hard',
            '<p>Using CRISPR base editors to dial down a regulatory gene that governs leaf-pore spacing in sorghum, plant geneticists created drought-resilient lines with 30 percent fewer stomata—an anatomical adjustment that sharply ______ evaporative water loss under Sahel heatwaves without starving photosynthesis of carbon dioxide.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            ['curtails', 'precipitates', 'replicates', 'magnifies'],
            'A',
            'Cause-Effect Clue: tạo giống cao lương chịu hạn ít hơn 30% lỗ khí khổng (stomata) trên lá → CẮT GIẢM / HẠN CHẾ mạnh lượng nước bốc hơi thất thoát trong nắng nóng Sahel → "curtails" (A)!',
            'Đọc kỹ đối tượng chịu tác động sau chỗ trống là "evaporative water loss" (sự thất thoát nước) → giống chịu hạn phải GIẢM BỚT ("curtails") thất thoát nước.',
            [
                ('Đáp án đúng', 'curtails = cắt giảm, hạn chế mạnh — khớp hoàn hảo với tác dụng chống mất nước của việc giảm mật độ khí khổng.'),
                ('Opposite Meaning', 'precipitates = đẩy nhanh/gây ra đột ngột — sai hướng hoàn toàn.'),
                ('Wrong Meaning', 'replicates = sao chép lặp lại — không hợp với "evaporative water loss".'),
                ('Opposite Meaning', 'magnifies = phóng đại, làm trầm trọng thêm — trái ngược với tính chịu hạn.'),
            ]
        ),

        # --- Q6-Q7: Craft and Structure — Text Structure and Purpose ---
        q_item(
            'm8_m1_q6', 6, 'Craft and Structure', 'Text Structure and Purpose', 'Medium',
            '<p>Visitors touring excavated houses in Pompeii often admire expanses of deep crimson plaster across dining-room walls, assuming Roman painters overwhelmingly favored red pigments. Yet portable X-ray fluorescence scans conducted in 2023 revealed that nearly a third of those crimson surfaces were originally painted golden yellow. <u>During the 79 CE eruption of Mount Vesuvius, superheated pyroclastic gases exceeding 300°C chemically dehydrated yellow ochre (goethite) right on the wall, transforming its iron-hydroxide crystals into brick-red hematite.</u> Consequently, art historians are now digitally recoloring virtual reconstructions of Pompeiian interiors to reflect their brighter pre-eruption palettes.</p>',
            'Which choice best describes the function of the underlined sentence in the text as a whole?',
            [
                'It questions the reliability of portable X-ray fluorescence scans for identifying ancient Roman iron pigments.',
                'It argues that Roman fresco painters intentionally heated yellow ochre to imitate expensive imported red dyes.',
                'It summarizes the digital software methods art historians use to generate virtual models of Pompeii.',
                'It explains the physical and chemical process by which originally yellow Pompeiian wall paintings turned crimson.'
            ],
            'D',
            'Câu trước nêu phát hiện bất ngờ (gần 1/3 mảng tường đỏ thẫm vốn từng được vẽ màu vàng óng). Câu gạch chân giải thích CƠ CHẾ HÓA - LÝ gây ra sự đổi màu đó (khí núi lửa >300°C làm mất nước khoáng chất goethite vàng, biến đổi thành hematite đỏ gạch) → Chọn D!',
            'Luôn đối chiếu vị trí câu gạch chân với câu ngay trước nó: câu trước đưa sự thật gây ngạc nhiên ("originally painted golden yellow") → câu gạch chân giải thích nguyên nhân hóa học tạo nên sự biến đổi đó.',
            [
                ('Contradiction', 'Bài dùng kết quả quét X-ray làm bằng chứng tin cậy, không hề nghi ngờ thiết bị này.'),
                ('Fact Distortion', 'Sự biến đổi nhiệt xảy ra do luồng khí núi lửa Vesuvius năm 79 SCN, KHÔNG phải do thợ vẽ cố tình nung.'),
                ('Misplaced Detail', 'Việc tái tạo màu kỹ thuật số nằm ở câu cuối ("Consequently..."), không phải trong câu gạch chân.'),
                ('Đáp án đúng', 'Giải thích chính xác quá trình nhiệt-hóa biến đổi màu vàng goethite nguyên bản thành đỏ hematite.'),
            ]
        ),
        q_item(
            'm8_m1_q7', 7, 'Craft and Structure', 'Text Structure and Purpose', 'Hard',
            '<p><i>The following text is adapted from an original 1774 epistolary novel,</i> Letters from a Cádiz Countinghouse<i>. Young shipping clerk Mateo writes to his sister Clara about his employer, merchant Don Esteban.</i><br/>“You would think, seeing our mahogany desks polished to a mirror sheen and the clerks’ silver inkstands aligned like soldiers, that this firm floats upon an ocean of certainty. Yet every evening after the bell clears the courtyard, Don Esteban lingers alone by the harbor window with his brass spyglass, counting each lantern on the breakwater and folding the uninsured bills of lading twice inside his cuff whenever the Vera Cruz packet boat is a single tide overdue.”</p>',
            'Which choice best states the main purpose of the text?',
            [
                'To accuse Don Esteban of embezzling money from the Vera Cruz trading fleet.',
                'To contrast the outward appearance of calm prosperity in the countinghouse with Don Esteban’s private financial anxiety.',
                'To explain how eighteenth-century shipping clerks maintained mahogany furniture and silver inkstands.',
                'To celebrate the navigational skill required to bring packet boats safely into Cádiz harbor.'
            ],
            'B',
            'Cấu trúc tương phản sắc nét qua chữ "Yet": Nửa đầu mô tả bề ngoài giàu sang, trật tự, vững chắc như "đại dương của sự chắc chắn" (bàn gỗ gụ bóng loáng, lọ mực bạc ngay hàng). Nửa sau hé lộ nỗi bất an thầm kín của chủ hãng khi tối xuống (lặng lẽ cầm ống nhòm ngóng tàu Vera Cruz trễ một con nước, giấu vận đơn chưa mua bảo hiểm vào tay áo) → Chọn B!',
            'Trong trích đoạn văn học, chữ "Yet" ở giữa đoạn là điểm xoay cấu trúc: Tương phản giữa Vẻ ngoài (outward appearance) và Nội tâm/Thực tế ẩn giấu (private anxiety).',
            [
                ('Unsupported Inference', 'Không có chi tiết nào tố cáo Don Esteban biển thủ tiền; ông chỉ lo lắng về vận đơn chưa có bảo hiểm.'),
                ('Đáp án đúng', 'Nắm trọn trục tương phản giữa diện mạo bề thế của phòng kế toán và nỗi lo tài chính thầm lặng của chủ hãng.'),
                ('Literal / Minor Detail', 'Bàn gỗ gụ và lọ mực bạc chỉ là hình ảnh tạo ấn tượng thịnh vượng bề ngoài, không phải hướng dẫn bảo quản đồ đạc.'),
                ('Out of Scope', 'Đoạn văn không ca ngợi kỹ năng hàng hải của thủy thủ tàu thư.'),
            ]
        ),

        # --- Q8: Craft and Structure — Cross-Text Connections ---
        q_item(
            'm8_m1_q8', 8, 'Craft and Structure', 'Cross-Text Connections', 'Hard',
            '<p><b>Text 1</b><br/>Alpine ecologist Dr. Henrik Solberg maintains that because subalpine tree growth is strictly limited by cold growing seasons, rising summer air temperatures across northern mountain ranges will steadily and predictably push conifer treelines to higher elevations over the coming century.</p><p><b>Text 2</b><br/>Tracking sixty-five mountain transects across the Pyrenees and the Canadian Rockies over thirty years, forest botanist Dr. Mireia Navarro found that nearly half of the sites showed zero upward treeline advance despite substantial summer warming. On wind-scoured upper ridges lacking deep winter snowpack and symbiotic soil fungi, warmer summer air dried out young pine seedlings faster than they could establish roots.</p>',
            'Based on the texts, how would Dr. Mireia Navarro (Text 2) most likely respond to Dr. Henrik Solberg’s prediction (Text 1)?',
            [
                'By contending that summer air temperatures across the Pyrenees and Canadian Rockies have actually cooled over the past thirty years.',
                'By asserting that conifer treelines can expand upward only when winter snowpack melts completely before spring.',
                'By arguing that Solberg’s temperature-driven prediction overlooks local moisture, wind, and soil-fungus constraints that can stall upward treeline migration even as summers warm.',
                'By agreeing that warming summers guarantee steady treeline expansion across virtually all northern mountain slopes.'
            ],
            'C',
            'Text 1 khẳng định nhiệt độ mùa hè tăng sẽ đẩy ranh giới rừng cây lá kim leo cao "đều đặn và dễ dự đoán". Text 2 đưa dữ liệu 30 năm trên 65 lát cắt: gần một nửa số điểm KHÔNG hề tiến lên cao dù mùa hè ấm lên rõ rệt, do gió quét khô, thiếu tuyết che phủ mùa đông và thiếu nấm đất cộng sinh làm chết khô cây non → Phản biện Text 1 đã bỏ sót các rào cản sinh thái cục bộ ngoài nhiệt độ (C)!',
            'Nhận diện mẫu phản biện kinh điển: Text 1 nêu yếu tố đơn nhất ("rising temperatures will steadily push") → Text 2 chỉ ra các nhân tố cản trở cục bộ ("wind, snowpack, soil fungi") khiến kết quả không xảy ra đồng loạt.',
            [
                ('Contradiction', 'Text 2 nêu rõ đã có "substantial summer warming" (mùa hè ấm lên đáng kể), không phải lạnh đi.'),
                ('Reversed Logic', 'Text 2 nói việc THIẾU lớp tuyết mùa đông dày (lacking deep winter snowpack) mới là nguyên nhân gây hại cho cây non.'),
                ('Đáp án đúng', 'Tóm gọn chính xác phản biện của Navarro: dự báo chỉ dựa vào nhiệt độ của Solberg bỏ qua độ ẩm, gió và nấm cộng sinh.'),
                ('Opposite Stance', 'Gần một nửa địa điểm không có sự mở rộng nào — bác bỏ hoàn toàn ý "guarantee steady expansion".'),
            ]
        ),

        # --- Q9-Q10: Information and Ideas — Central Ideas and Details ---
        q_item(
            'm8_m1_q9', 9, 'Information and Ideas', 'Central Ideas and Details', 'Medium',
            '<p><i>The following excerpt is from an original poem, “The Clockmaker’s Patio,” written in the tradition of Latin American magical realism.</i><br/>After the afternoon cloudburst clears the tiles,<br/>our patio puddles keep yesterday’s clouds intact,<br/>unbothered by the broom my grandmother drags across the stones.<br/>Beneath the lime tree, three silver-winged moths<br/>nudge the brass pendulum of her stopped hallway clock<br/>until the chime remembers every cousin’s laugh<br/>from summers before the river changed its course.</p>',
            'Which choice best states the main idea of the text?',
            [
                'The speaker portrays a tranquil domestic courtyard where ordinary post-rain scenes blend effortlessly with quiet, wondrous traces of family memory.',
                'The speaker expresses frustration that afternoon rainstorms repeatedly damage the grandmother’s antique brass clock.',
                'The speaker warns that changing river currents threaten to flood the family’s lime orchard and patio.',
                'The speaker recounts a scientific effort to study silver-winged moths gathering near stone courtyards.'
            ],
            'A',
            'Bài thơ miêu tả khung cảnh sân nhà yên bình sau cơn mưa rào theo bút pháp hiện thực huyền ảo: vũng nước giữ nguyên đám mây hôm qua, bướm cánh bạc khẽ đẩy quả lắc chiếc đồng hồ đã ngừng để tiếng chuông "nhớ lại" tiếng cười của họ hàng những mùa hè cũ → Khung cảnh đời thường hòa quyện tự nhiên với sắc màu kỳ ảo và ký ức gia đình (A)!',
            'Chú ý giọng điệu êm dịu ("unbothered", "nudge", "remembers every cousin’s laugh") — đặc trưng của hiện thực huyền ảo là miêu tả điều kỳ diệu thật bình thản, giàu hoài niệm.',
            [
                ('Đáp án đúng', 'Khắc họa trọn vẹn sân nhà thanh bình nơi chi tiết thường ngày giao thoa tự nhiên với phép màu ký ức gia đình.'),
                ('Wrong Tone / Distortion', 'Không có sự bực bội hay cảnh mưa làm hỏng đồng hồ; chiếc đồng hồ chỉ đơn giản là đã dừng và vang lại ký ức.'),
                ('Literal Misreading', 'Cụm "before the river changed its course" chỉ là mốc thời gian xa xưa trong ký ức, không phải lời cảnh báo lũ lụt.'),
                ('Out of Scope', 'Không hề có nghiên cứu khoa học nào về loài bướm.'),
            ]
        ),
        q_item(
            'm8_m1_q10', 10, 'Information and Ideas', 'Central Ideas and Details', 'Medium',
            '<p>In tenth-century Aleppo, master instrument maker Maryam al-Ijliyyah gained acclaim for crafting precision brass planispheric astrolabes used by astronomers and travelers across the Levant. Because the apparent path of stars across the night sky shifts with an observer’s distance from the equator, a single fixed coordinate grid would yield inaccurate altitude readings in distant cities. To solve this problem, artisans recessed the astrolabe’s hollow body (<i>mater</i>) to hold a stack of interchangeable engraved brass discs—called tympans—each calibrated for a specific latitude so the owner could swap plates upon arriving in a new region.</p>',
            'According to the text, why did medieval astrolabe makers include a stack of interchangeable brass tympans inside the instrument’s hollow body?',
            [
                'To add extra brass weight so strong desert winds could not blow the astrolabe out of alignment.',
                'To protect delicate glass lenses from cracking during long overland caravan journeys.',
                'To allow users to switch coordinate grids calibrated for different latitudes so celestial measurements remained accurate across regions.',
                'To record written trade receipts and travel diaries on spare metal plates between cities.'
            ],
            'C',
            'Câu hỏi Specific Detail: Tìm đúng cụm "interchangeable engraved brass discs—called tympans" → "each calibrated for a specific latitude so the owner could swap plates upon arriving in a new region" nhằm tránh sai số khi khoảng cách tới xích đạo thay đổi → Paraphrase chuẩn xác tại C!',
            'Tìm mệnh đề chỉ mục đích ("each calibrated for... so the owner could...") gắn trực tiếp với từ khóa "brass tympans".',
            [
                ('Out of Scope', 'Không nhắc đến việc tăng trọng lượng để chống gió sa mạc.'),
                ('Out of Scope', 'Thước đo tinh tú bằng đồng không dùng thấu kính thủy tinh trong đoạn văn này.'),
                ('Đáp án đúng', 'Khớp nguyên ý: cho phép thay đĩa lưới tọa độ hiệu chuẩn theo từng vĩ độ để đo chính xác khi di chuyển sang vùng khác.'),
                ('Out of Scope', 'Không dùng đĩa đồng để ghi biên lai buôn bán hay nhật ký.'),
            ]
        ),

        # --- Q11-Q12: Information and Ideas — Command of Evidence (Textual) ---
        q_item(
            'm8_m1_q11', 11, 'Information and Ideas', 'Command of Evidence (Textual)', 'Hard',
            '<p>Wild common marmosets in northeastern Brazil exchange rhythmic long-distance "phee" calls in alternating turns that closely resemble human conversational timing. Neurobiologist Dr. Rafael Costa hypothesized that infant marmosets do not inherit a fixed vocal turn-taking tempo purely by genetic instinct; rather, they actively calibrate the spacing of their calls by listening to the timing of parental responses.</p>',
            'Which finding, if true, would most directly support Dr. Rafael Costa’s hypothesis?',
            [
                'Adult common marmosets produce louder "phee" calls during rainy mornings than during dry afternoons.',
                'In controlled acoustic nurseries, infant marmosets exposed to parent-voice recordings programmed with slightly longer reply pauses gradually lengthened their own inter-call intervals to match the delayed rhythm, whereas control infants exposed to standard pauses kept shorter intervals.',
                'Genetic sequencing reveals that common marmosets share several vocal-cord muscle proteins with closely related tamarin monkeys.',
                'Wild marmoset troops living in dense coastal forests forage primarily on tree gum and insects during the dry season.'
            ],
            'B',
            'Khóa giả thuyết Costa: Khỉ con KHÔNG chỉ thừa hưởng nhịp đối đáp cố định theo bản năng di truyền, mà CHỦ ĐỘNG hiệu chỉnh giãn cách tiếng kêu dựa trên nhịp phản hồi của bố mẹ. Đáp án B đưa ra thí nghiệm đối chứng sắc nét: nhóm khỉ con nghe bản ghi giọng bố mẹ có khoảng dừng dài hơn đã tự điều chỉnh kéo dài nhịp kêu của mình cho khớp, trong khi nhóm đối chứng giữ nhịp ngắn hơn → Trực tiếp chứng minh cơ chế học theo phản hồi âm thanh! Chọn B!',
            'Giả thuyết phân biệt "bẩm sinh di truyền" vs "học từ phản hồi bố mẹ" → bằng chứng mạnh nhất phải cho thấy sự thay đổi nhịp phản hồi của bố mẹ dẫn đến sự điều chỉnh tương ứng ở khỉ con.',
            [
                ('Adjacent Topic Drift', 'Âm lượng lớn hơn vào sáng mưa ở khỉ trưởng thành không kiểm chứng cơ chế học nhịp đối đáp ở khỉ con.'),
                ('Đáp án đúng', 'Chứng minh trực tiếp rằng khỉ con chủ động hiệu chỉnh khoảng nghỉ tiếng kêu theo tốc độ phản hồi của giọng bố mẹ.'),
                ('Weakens / Off-Point', 'Dữ liệu di truyền giống khỉ tamarin không chứng minh việc học nhịp qua phản hồi âm thanh.'),
                ('Irrelevant Detail', 'Chế độ ăn nhựa cây và côn trùng hoàn toàn không liên quan đến giao tiếp âm thanh.'),
            ]
        ),
        q_item(
            'm8_m1_q12', 12, 'Information and Ideas', 'Command of Evidence (Textual)', 'Hard',
            '<p>In an essay on the original 1786 epistolary novel <i>The Glass Conservatory</i>, a literary critic argues that young heiress Lady Beatrice uses seemingly polite botanical reports in her letters to a trusted friend to subtly reveal how strictly her uncle controls her daily freedom.</p>',
            'Which quotation from Lady Beatrice’s letters in <i>The Glass Conservatory</i> most effectively illustrates the critic’s claim?',
            [
                '“My uncle has ordered thirty crates of Dutch tulip bulbs from Amsterdam, insisting that the southern terrace be planted before the first frost.”',
                '“The glass roof leaked slightly during Tuesday’s squall, forcing the head gardener to move our potted lemon trees near the brick hearth.”',
                '“Our parlor tea service arrived safely from Worcester on Thursday, though one porcelain saucer bore a faint hairline crack along its gilt rim.”',
                '“Uncle’s laurel hedges are trimmed every morning to an exact square and locked behind wrought-iron gates by dusk—an arrangement he fondly describes as protection, though both the laurels and I are permitted to grow only along the lines his shears allow.”'
            ],
            'D',
            'Checklist 2 vế từ Claim: [1] Dùng lời kể lịch thiệp về thực vật/vườn cây + [2] Khéo léo bộc lộ sự kiểm soát gắt gao của người chú đối với tự do cá nhân của mình. A, B, C chỉ kể chuyện mua hoa tulip, mái kính dột, bộ ấm trà. Duy nhất D mượn hình ảnh hàng rào nguyệt quế bị cắt tỉa vuông vức và khóa sau cổng sắt để ngầm so sánh với chính bản thân ("both the laurels and I are permitted to grow only along the lines his shears allow") → Chọn D!',
            'Tìm trích dẫn có phép ẩn dụ thực vật gắn trực tiếp với sự giới hạn tự do của nhân vật nữ ("both the laurels and I...")!',
            [
                ('Topic Keyword Lure', 'Có nhắc hoa tulip và người chú nhưng chỉ là việc đặt mua giống cây bình thường.'),
                ('Topic Keyword Lure', 'Nhắc nhà kính và cây chanh nhưng không hề phản ánh sự kiểm soát tự do cá nhân.'),
                ('Irrelevant Detail', 'Chỉ nói về bộ ấm trà sứ không liên quan đến thực vật hay quyền tự do.'),
                ('Đáp án đúng', 'Khớp hoàn hảo: mượn hình ảnh cắt tỉa hàng rào nguyệt quế để ngầm phơi bày sự kìm kẹp tự do của người chú.'),
            ]
        ),

        # --- Q13-Q14: Information and Ideas — Command of Evidence (Quantitative) ---
        q_item(
            'm8_m1_q13', 13, 'Information and Ideas', 'Command of Evidence (Quantitative)', 'Medium',
            svg_bar_chart(
                'Mean Sorghum Grain Yield (Metric Tons/Hectare) Under Severe Drought',
                ['0.0', '1.0', '2.0', '3.0', '4.0'],
                [('Wild-Type', 1.8, '1.8 t/ha'), ('Wax-Cuticle Edit', 2.4, '2.4 t/ha'), ('Root-Angle Edit', 2.7, '2.7 t/ha'), ('Dual-Trait Edit', 3.9, '3.9 t/ha')],
                4.0
            ) + '<p>Agronomists testing CRISPR-edited sorghum in semi-arid Niger reported that individual single-gene modifications—thickening leaf surface wax or steepening root angles—each lifted grain yields moderately during severe drought. However, stacking both edits together in a single dual-trait cultivar dramatically outperformed either individual modification and more than doubled the harvest of unedited wild-type sorghum.</p>',
            'Which choice most effectively uses data from the graph to support the agronomists’ assessment of the dual-trait sorghum cultivar?',
            [
                'The dual-trait cultivar produced 3.9 metric tons per hectare—surpassing both the wax-cuticle edit (2.4 t/ha) and root-angle edit (2.7 t/ha) and more than doubling the 1.8 t/ha harvest of wild-type sorghum.',
                'The root-angle edit yielded 2.7 metric tons per hectare under severe drought, outperforming the wax-cuticle edit at 2.4 metric tons per hectare.',
                'Wild-type sorghum generated the lowest drought grain yield in the trial at 1.8 metric tons per hectare.',
                'Both single-gene edited lines exceeded 2.0 metric tons per hectare during the Niger field study.'
            ],
            'A',
            'Checklist 2 vế đánh giá về Dual-Trait Edit: [1] Vượt xa từng chỉnh sửa đơn lẻ (3.9 vs 2.4 và 2.7 ✓) + [2] Hơn gấp đôi giống hoang dại Wild-Type (1.8 × 2 = 3.6 → 3.9 > 3.6 ✓). B, C, D đều đúng biểu đồ nhưng không nhắc đến Dual-Trait Edit! Duy nhất A đối chiếu đủ cả bốn con số then chốt 3.9, 2.4, 2.7 và 1.8!',
            'Kiểm chứng phép nhân: 2 × 1.8 = 3.6 < 3.9 → A chứng minh trọn vẹn cả hai vế so sánh của nhóm nhà nông học!',
            [
                ('Đáp án đúng', 'Trích đúng toàn bộ dữ liệu hỗ trợ hai vế: 3.9 t/ha vượt 2.4 & 2.7 t/ha và lớn hơn gấp đôi mốc 1.8 t/ha (3.6 t/ha).'),
                ('True Data / Wrong Subject', 'Chỉ so sánh hai dòng chỉnh sửa đơn, bỏ qua dòng Dual-Trait.'),
                ('Incomplete Data', 'Chỉ nêu kết quả của Wild-Type mà không nhắc Dual-Trait.'),
                ('Incomplete Data', 'Chỉ nói về hai dòng chỉnh sửa đơn lẻ.'),
            ]
        ),
        q_item(
            'm8_m1_q14', 14, 'Information and Ideas', 'Command of Evidence (Quantitative)', 'Hard',
            html_table(
                'Table 1. Geothermal District Heating Benchmarks in Four Icelandic Municipalities (2024)',
                ['Municipality', 'Borehole Water Temp (°C)', 'Main Pipeline Length (km)', 'Annual Household Heating Cost (USD)', 'Geothermal Coverage'],
                [
                    ['Reykjavík', '104°C', '27 km', '610 USD', '99%'],
                    ['Akureyri', '92°C', '14 km', '690 USD', '97%'],
                    ['Húsavík', '126°C', '48 km', '845 USD', '94%'],
                    ['Selfoss', '86°C', '9 km', '580 USD', '98%'],
                ]
            ) + '<p>An energy policy commentator claims that among Icelandic municipal heating networks, tapping hotter geothermal boreholes reliably translates into lower annual heating bills for households.</p>',
            'Which choice best describes data from the table that directly weaken the commentator’s claim?',
            [
                'Reykjavík draws water at 104°C and supplies geothermal heating to 99% of its households.',
                'Akureyri maintains a 14 km main pipeline and charges households an average of 690 USD per year.',
                'Although Húsavík taps the hottest borehole water in the table (126°C), its residents pay the highest annual heating bill (845 USD), whereas Selfoss draws the coolest water (86°C) yet has the lowest annual bill (580 USD).',
                'All four municipalities provide geothermal heating to at least 94% of local homes.'
            ],
            'C',
            'Khóa Claim cần WEAKEN: Giếng địa nhiệt NÓNG HƠN → hóa đơn sưởi hàng năm THẤP HƠN! Soi bảng lập tức thấy chiều ngược lại ở hai cực: **Húsavík** nóng nhất (126°C) nhưng cước ĐẮT NHẤT (845 USD), trong khi **Selfoss** nguội nhất (86°C) lại có cước RẺ NHẤT (580 USD)! Chọn C!',
            'Tìm cặp hàng đảo chiều trực tiếp giữa hai biến của lập luận ("Hotter Borehole" đi kèm "Higher Bill", và "Cooler Borehole" đi kèm "Lower Bill")!',
            [
                ('True Data / Wrong Claim', 'Chỉ nêu nhiệt độ và độ phủ của Reykjavík, không đối chiếu hóa đơn theo nhiệt độ.'),
                ('True Data / Wrong Claim', 'Chỉ nêu số liệu đơn lẻ của Akureyri mà không so sánh với thành phố khác.'),
                ('Đáp án đúng', 'Phản ví dụ trực diện đập tan tuyên bố: Húsavík nóng nhất (126°C) lại đắt nhất (845 USD), còn Selfoss nguội nhất (86°C) lại rẻ nhất (580 USD).'),
                ('Irrelevant Metric', 'Tỷ lệ độ phủ >=94% không kiểm chứng mối quan hệ giữa nhiệt độ giếng và giá cước.'),
            ]
        ),

        # --- Q15: Information and Ideas — Inferences ---
        q_item(
            'm8_m1_q15', 15, 'Information and Ideas', 'Inferences', 'Hard',
            '<p>Across Arctic Scandinavia, pale mats of reindeer lichen (<i>Cladonia stellaris</i>) cover vast stretches of tundra soil, reflecting up to 35 percent of incoming summer sunlight back into space and shielding underlying frozen ground from thawing. Over the past two decades, warmer spring temperatures have enabled dark-leaved dwarf birch shrubs to grow taller and cast heavy shade over slow-growing lichen beds, causing lichen cover to shrink markedly. Because dark shrub foliage absorbs far more solar energy than pale lichens do, the ongoing replacement of lichen mats by dwarf birch shrubs will likely ______</p>',
            'Which choice most logically completes the text?',
            [
                'restore reindeer lichen cover to historical levels by sheltering the lichens from excess sunlight.',
                'accelerate summer warming and thawing of the underlying Arctic permafrost.',
                'prevent dwarf birch shrubs from surviving spring warming in northern Scandinavia.',
                'eliminate all incoming solar radiation across Arctic tundra regions during winter.'
            ],
            'B',
            'Ghép 3 tiền đề theo quy tắc 1-Millimeter: (1) Địa y sáng màu phản xạ tới 35% ánh nắng mùa hè giúp bảo vệ tầng đất đóng băng vĩnh cửu (permafrost) khỏi tan chảy; (2) Bụi bạch dương lá tối màu đang lấn át làm thu hẹp thảm địa y; (3) Lá bụi tối màu HẤP THỤ nhiều bức xạ mặt trời hơn hẳn địa y sáng màu ⇒ Hệ quả trực tiếp: Tăng hấp thụ nhiệt xuống mặt đất và ĐẨY NHANH quá trình nóng lên & tan chảy tầng đất đóng băng vĩnh cửu bên dưới (B)!',
            'Chuỗi nhân quả khép kín: Ít bề mặt phản xạ sáng (lichen ↓) + Nhiều tán lá tối hấp thụ nhiệt (dark shrub ↑) → Đất băng bên dưới nóng lên và tan nhanh hơn!',
            [
                ('Contradiction', 'Bài nói rõ bóng râm của bụi bạch dương làm thảm địa y THU HẸP MẠNH ("shrink markedly"), không phải phục hồi.'),
                ('Đáp án đúng', 'Suy diễn 1mm chặt chẽ: mất lớp phản xạ sáng và tăng tán lá tối hấp thụ nhiệt dẫn thẳng tới việc đẩy nhanh tan băng vĩnh cửu.'),
                ('Contradiction', 'Mùa xuân ấm lên chính là điều kiện giúp bụi bạch dương phát triển cao lớn hơn.'),
                ('Too Extreme / Nonsense', 'Bụi cây không thể "xóa sạch mọi bức xạ mặt trời" trong mùa đông.'),
            ]
        ),

        # --- Q16-Q19: Standard English Conventions — Boundaries ---
        q_item(
            'm8_m1_q16', 16, 'Standard English Conventions', 'Boundaries', 'Easy',
            '<p>Conservationists excavating a bakery courtyard in Pompeii uncovered a remarkably intact fresco depicting figs, pomegranates, and a silver ______ analysts noted that the vibrant mineral pigments had been bonded directly into wet lime plaster before the wall dried.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['goblet,', 'goblet', 'goblet, while', 'goblet;'],
            'D',
            'Vế 1 là IC hoàn chỉnh ("Conservationists excavating... silver goblet"). Vế 2 cũng là IC hoàn chỉnh ("analysts noted that... dried"). Giữa 2 IC độc lập → Chọn dấu chấm phẩy (;) = D!',
            'Hai mệnh đề độc lập đứng liền nhau: loại dấu phẩy đơn (Comma Splice - A), loại không dấu (Run-on - B), loại ", while" sai quan hệ logic/nhượng bộ → chốt chấm phẩy (;).',
            [
                ('Comma Splice', 'Không thể dùng duy nhất 1 dấu phẩy để nối hai mệnh đề độc lập.'),
                ('Run-On Sentence', 'Thiếu hoàn toàn dấu ngăn giữa hai IC.'),
                ('Wrong Subordination', 'Thêm ", while" tạo sắc thái tương phản gượng ép không phù hợp vì hai vế bổ sung thông tin về cùng bức bích họa.'),
                ('Đáp án đúng', 'Dấu chấm phẩy (;) phân tách chuẩn xác hai mệnh đề độc lập IC + IC.'),
            ]
        ),
        q_item(
            'm8_m1_q17', 17, 'Standard English Conventions', 'Boundaries', 'Medium',
            '<p>Working in eleventh-century Cairo, optical physicist ______ demonstrated through dark-chamber lantern tests that vision occurs when light rays enter the eye rather than shoot outward from it.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['Ibn al-Haytham', ', Ibn al-Haytham,', 'Ibn al-Haytham,', ', Ibn al-Haytham'],
            'A',
            'Quy tắc Chức danh không mạo từ + Tên riêng: "optical physicist Ibn al-Haytham" không có "a/the" phía trước → Cụm tên là thiết yếu (Essential) → 0 dấu phẩy ở cả hai đầu, nối thẳng vào động từ chính "demonstrated" → Chọn A!',
            'Không có mạo từ trước chức danh ("optical physicist") + Tên riêng + Động từ chính → 0 dấu phẩy!',
            [
                ('Đáp án đúng', '0 dấu phẩy — giữ liền chức danh thiết yếu, tên riêng và động từ chính "demonstrated".'),
                ('Non-Essential Trap', 'Dùng cặp phẩy biến tên nhà vật lý thành thông tin phụ sai ngữ pháp khi thiếu mạo từ trước "optical physicist".'),
                ('No-Comma Zone (S, V)', 'Dấu phẩy đơn cắt đứt chủ ngữ khỏi động từ chính "demonstrated".'),
                ('Unpaired Comma', 'Dấu phẩy lẻ đặt sai giữa chức danh và tên riêng.'),
            ]
        ),
        q_item(
            'm8_m1_q18', 18, 'Standard English Conventions', 'Boundaries', 'Hard',
            '<p>To breed sorghum capable of thriving across Mali’s driest northern millet belt, molecular agronomists focused on one decisive physiological ______ preserving green photosynthetic leaves well into the late grain-filling stage.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['trait;', 'trait.', 'trait:', 'trait, and'],
            'C',
            'Vế trái ("To breed sorghum... one decisive physiological trait") là IC hoàn chỉnh. Vế phải ("preserving green photosynthetic leaves well into the late grain-filling stage") là Cụm danh động từ (Gerund Phrase — KHÔNG PHẢI IC!) định nghĩa cụ thể đặc tính đó là gì → Bắt buộc dùng dấu hai chấm (:) = C!',
            'IC hoàn chỉnh + Cụm định nghĩa không có động từ chia thì (Phrase) → Loại dấu chấm (.) và chấm phẩy (;), chọn ngay dấu hai chấm (:)!',
            [
                ('Semicolon + Fragment', 'Vế sau bắt đầu bằng "preserving..." không có chủ ngữ & động từ chia thì → không phải IC → cấm dùng chấm phẩy.'),
                ('Period + Fragment', 'Tách cụm danh động từ thành câu đứng riêng gây lỗi Fragment.'),
                ('Đáp án đúng', 'Dấu hai chấm (:) sau IC giới thiệu chuẩn xác cụm giải thích cho "one decisive physiological trait".'),
                ('Comma + FANBOYS + Fragment', 'Sau ", and" thiếu IC hoàn chỉnh và không song song cấu trúc.'),
            ]
        ),
        q_item(
            'm8_m1_q19', 19, 'Standard English Conventions', 'Boundaries', 'Hard',
            '<p>The dawn duets of Javan gibbons—complex exchanges of rising whistles, trills, and soaring solo codas ______ can reverberate clearly across more than two kilometers of dense montane forest.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['combined,', 'combined—', 'combined;', 'combined'],
            'B',
            'Cụm bổ sung chen giữa Chủ ngữ ("The dawn duets of Javan gibbons") và Động từ chính ("can reverberate") mở đầu bằng gạch ngang dài (`—complex exchanges...`) → Bắt buộc đóng bằng gạch ngang dài tương ứng (`combined—`) → Chọn B!',
            'Quy tắc đồng bộ cặp dấu: Mở bằng em-dash (—) → Đóng bằng em-dash (—)!',
            [
                ('Mismatched Pair (— ... ,)', 'Cấm mở bằng gạch ngang nhưng đóng bằng dấu phẩy.'),
                ('Đáp án đúng', 'Khép đúng cặp em-dash (— ... —) ngay trước cụm động từ chính "can reverberate".'),
                ('Semicolon Inside Subject-Verb', 'Dấu chấm phẩy cắt rời chủ ngữ khỏi động từ chính.'),
                ('Unclosed Modifier', 'Thiếu dấu gạch ngang đóng khiến câu bị gãy cấu trúc.'),
            ]
        ),

        # --- Q20-Q22: Standard English Conventions — Form, Structure, and Sense ---
        q_item(
            'm8_m1_q20', 20, 'Standard English Conventions', 'Form, Structure, and Sense', 'Medium',
            '<p>The finely engraved network of curved arcs and dagger-shaped star pointers mounted on a medieval astrolabe’s rotating brass plate ______ an observer to calculate local solar time within minutes.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['enables', 'enable', 'have enabled', 'enabling'],
            'A',
            'Gạch bỏ toàn bộ cụm giới từ & phân từ chen giữa: "The finely engraved <b>network</b> <s>[of curved arcs and dagger-shaped star pointers mounted on a medieval astrolabe’s rotating brass plate]</s>". Chủ ngữ thật là "network" (SỐ ÍT!), câu chưa có động từ chính → Chọn "enables" (A)!',
            'Áp dụng mẹo 3–1: B và C đều là số nhiều, D là V-ing (Fragment), duy nhất A ("enables") là động từ chia thì số ít khớp với chủ ngữ "network"!',
            [
                ('Đáp án đúng', 'enables (hiện tại đơn, số ít) khớp tuyệt đối với chủ ngữ chính "The finely engraved network".'),
                ('Subject-Verb Mismatch', 'enable là số nhiều — bẫy nhìn nhầm danh từ số nhiều "arcs and star pointers".'),
                ('Subject-Verb Mismatch', 'have enabled là số nhiều.'),
                ('Non-Finite Fragment', 'enabling là phân từ, làm câu mất động từ chính.'),
            ]
        ),
        q_item(
            'm8_m1_q21', 21, 'Standard English Conventions', 'Form, Structure, and Sense', 'Hard',
            '<p>Sealed for more than two millennia beneath collapsed limestone rubble inside a buried Guatemalan pyramid, ______</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            [
                'archaeologists unearthed the San Bartolo murals in 2001 with astonishingly intact brushwork.',
                'the excavation team at San Bartolo carefully documented the newly uncovered Maya murals.',
                'humidity levels inside the buried chamber remained low enough to protect the San Bartolo murals.',
                'the San Bartolo murals preserved their delicate red-and-black mythological scenes in remarkable detail.'
            ],
            'D',
            'Kiểm tra Dangling Modifier! Cụm phân từ quá khứ mở đầu "Sealed for more than two millennia beneath collapsed limestone rubble..." (Được niêm phong suốt hơn hai thiên niên kỷ bên dưới đống đá vôi sụp đổ) mô tả NHỮNG BỨC BÍCH HỌA ("the San Bartolo murals"), KHÔNG mô tả nhà khảo cổ (A), đội khai quật (B), hay độ ẩm (C)! Duy nhất D đặt đúng "the San Bartolo murals" làm chủ ngữ ngay sau dấu phẩy!',
            'Hỏi ngay: "Thứ gì bị niêm phong suốt hơn 2.000 năm dưới đá vôi?" → Chính là các bức bích họa ("the San Bartolo murals")!',
            [
                ('Dangling Modifier', 'Các nhà khảo cổ không bị niêm phong suốt hai thiên niên kỷ dưới kim tự tháp.'),
                ('Dangling Modifier', 'Đội khai quật không phải đối tượng bị chôn vùi hai nghìn năm.'),
                ('Dangling Modifier', 'Mức độ ẩm không phải thứ được niêm phong làm chủ thể chính cho mệnh đề này.'),
                ('Đáp án đúng', 'Chủ ngữ "the San Bartolo murals" đứng ngay sau dấu phẩy khớp 100% với cụm bổ ngữ "Sealed...".'),
            ]
        ),
        q_item(
            'm8_m1_q22', 22, 'Standard English Conventions', 'Form, Structure, and Sense', 'Hard',
            '<p>In a 2023 feasibility report on Nordic heating transitions, economists noted that the upfront drilling expense of a deep geothermal district network is considerably steeper than ______ a conventional natural-gas boiler plant, even though long-term operating costs are far lower.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['those of', 'compared to', 'that of', 'with'],
            'C',
            'So sánh tương đồng (Apples-to-Apples): Đối tượng đem so sánh ở vế 1 là "<b>the upfront drilling expense</b>" (chi phí khoan ban đầu — SỐ ÍT!). Không thể so sánh chi phí với cả một nhà máy khí đốt; cần đại từ thay thế cho danh từ SỐ ÍT "expense" → chọn "<b>that of</b>" (C), loại "those of" (số nhiều)!',
            'So sánh danh từ SỐ ÍT ("the upfront drilling expense") → dùng "that of"; SỐ NHIỀU → dùng "those of"!',
            [
                ('Pronoun Number Mismatch', '"those of" chỉ thay thế cho danh từ số nhiều, trong khi "expense" là số ít.'),
                ('Redundant / Illogical Comparison', '"steeper than compared to a... plant" vừa thừa từ vừa so sánh lệch cấp chi phí với nhà máy.'),
                ('Đáp án đúng', '"that of" thay thế chính xác cho danh từ số ít "the upfront drilling expense of".'),
                ('Illogical Comparison', '"than with a... plant" sai ngữ pháp và so sánh khập khiễng.'),
            ]
        ),

        # --- Q23-Q25: Expression of Ideas — Transitions ---
        q_item(
            'm8_m1_q23', 23, 'Expression of Ideas', 'Transitions', 'Easy',
            '<p>Unlike flowering tundra plants, Arctic crustose lichens lack true roots or waterproof cuticles to regulate internal hydration. ______, they absorb moisture directly from passing fog and quickly enter metabolic dormancy whenever dry winds strip away surface water.</p>',
            'Which choice completes the text with the most logical transition?',
            ['Nevertheless', 'As a result', 'For example', 'Previously'],
            'B',
            'Câu 1 nêu nguyên nhân cấu tạo sinh học (địa y vỏ Bắc Cực thiếu rễ thật và lớp biểu bì chống thấm để điều tiết nước). Câu 2 nêu hệ quả thích nghi trực tiếp (hút ẩm trực tiếp từ sương mù và nhanh chóng rơi vào trạng thái ngủ đông khi gió khô thổi qua) → Nhân – Quả → "As a result" (B)!',
            'Thiếu rễ & lớp giữ nước (Nguyên nhân) → Hút ẩm trực tiếp từ sương & ngủ đông khi khô (Hệ quả) → chọn "As a result".',
            [
                ('False Contrast', 'Nevertheless chỉ sự trái kỳ vọng — sai vì hành vi câu 2 hoàn toàn thuận logic với câu 1.'),
                ('Đáp án đúng', 'As a result kết nối chuẩn xác đặc điểm giải phẫu thiếu rễ ở câu 1 với cơ chế thích nghi hệ quả ở câu 2.'),
                ('Wrong Relationship (Example)', 'Hút ẩm từ sương mù không phải ví dụ con của việc "thiếu rễ".'),
                ('Wrong Relationship (Time)', 'Previously chỉ thời điểm quá khứ trước đó — sai hoàn toàn.'),
            ]
        ),
        q_item(
            'm8_m1_q24', 24, 'Expression of Ideas', 'Transitions', 'Medium',
            '<p>Traditional nineteenth-century Gothic tales typically build suspense by portraying supernatural apparitions as terrifying disruptions of ordinary reality. ______, Latin American magical realist novels treat impossible occurrences—such as flowers raining from a clear sky—as unremarkable details of everyday village life.</p>',
            'Which choice completes the text with the most logical transition?',
            ['By contrast', 'Therefore', 'Furthermore', 'In other words'],
            'A',
            'Câu 1 nói về truyện Gothic thế kỷ 19 (coi yếu tố siêu nhiên là cú sốc rùng rợn phá vỡ thực tại). Câu 2 đối chiếu trực diện với tiểu thuyết hiện thực huyền ảo Mỹ Latinh (coi điều phi lý như chi tiết bình thường của đời sống làng quê) → So sánh đối lập hai đối tượng → "By contrast" (A)!',
            'Đối chiếu cách xử lý yếu tố kỳ ảo giữa Gothic (terrifying disruptions) và Magical Realism (unremarkable details) → chốt "By contrast".',
            [
                ('Đáp án đúng', 'By contrast nối chính xác hai trường phái văn học có cách tiếp cận trái ngược nhau đối với yếu tố siêu nhiên.'),
                ('Wrong Relationship (Cause-Effect)', 'Cách viết Gothic không phải nguyên nhân sinh ra cách viết hiện thực huyền ảo.'),
                ('Wrong Relationship (Addition)', 'Furthermore bổ sung thông tin cùng chiều, không dùng khi hai vế đối lập.'),
                ('Restatement Trap', 'Câu 2 giới thiệu trường phái ngược lại, không diễn đạt lại câu 1.'),
            ]
        ),
        q_item(
            'm8_m1_q25', 25, 'Expression of Ideas', 'Transitions', 'Hard',
            '<p>Roman fresco workshops in Pompeii did not rely solely on costly imported pigments shipped across the Mediterranean to decorate wealthy villas. ______, local painters routinely blended abundant regional volcanic earths and slaked lime to produce rich ochres, greens, and velvety blacks at a fraction of the expense.</p>',
            'Which choice completes the text with the most logical transition?',
            ['Similarly', 'Consequently', 'Admittedly', 'Instead'],
            'D',
            'Câu 1 có cấu trúc phủ định rõ ("did NOT rely solely on costly imported pigments"). Câu 2 đưa phương án THAY THẾ thực tế của thợ vẽ địa phương (pha trộn đất núi lửa bản địa và vôi tôi) → Phủ định X → làm Y thay thế = "Instead" (D)!',
            'Nhận diện cặp cấu trúc vàng: Câu 1 "did not rely solely on X" + Câu 2 hành động thay thế Y → chọn ngay "Instead"!',
            [
                ('Wrong Relationship (Similarity)', 'Similarly chỉ sự giống nhau — sai hướng sau mệnh đề phủ định.'),
                ('Wrong Relationship (Cause-Effect)', 'Không phụ thuộc hoàn toàn vào bột màu nhập khẩu không tự gây ra việc pha đất núi lửa theo chiều nhân-quả thuần túy.'),
                ('Concession Trap', 'Admittedly dùng để thừa nhận một nhượng bộ trái ý chính — sai mạch lập luận.'),
                ('Đáp án đúng', 'Instead khớp hoàn hảo vai trò chuyển từ điều không làm ở câu 1 sang phương án thay thế thực tế ở câu 2.'),
            ]
        ),

        # --- Q26-Q27: Expression of Ideas — Rhetorical Synthesis ---
        q_item(
            'm8_m1_q26', 26, 'Expression of Ideas', 'Rhetorical Synthesis', 'Medium',
            '''<p>While researching medieval optics, a student has taken the following notes:</p>
            <ul>
              <li>Ancient Greek thinkers such as Euclid and Ptolemy championed extramission theory, proposing that human eyes emit invisible visual beams to touch distant objects.</li>
              <li>In his eleventh-century <i>Book of Optics</i> (<i>Kitāb al-Manāẓir</i>), scholar Ibn al-Haytham challenged extramission theory through controlled experiments.</li>
              <li>He observed that staring directly at the bright sun causes immediate pain and lingering afterimages—effects inexplicable if eyes merely emitted outgoing rays.</li>
              <li>Using a dark room with a tiny aperture (<i>camera obscura</i>), he proved that external light rays travel in straight lines from illuminated objects into the eye (intromission theory).</li>
            </ul>''',
            'The student wants to explain how Ibn al-Haytham used experimental evidence to overturn the ancient extramission theory of vision. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
            [
                'Ancient Greek thinkers such as Euclid and Ptolemy proposed the extramission theory, which Ibn al-Haytham discussed in his eleventh-century <i>Book of Optics</i>.',
                'Ibn al-Haytham’s eleventh-century treatise <i>Kitāb al-Manāẓir</i> is widely known in English as the <i>Book of Optics</i>.',
                'Challenging ancient Greek claims that eyes emit visual beams, Ibn al-Haytham cited painful solar afterimages and <i>camera obscura</i> pinhole tests to prove that external light travels in straight lines into the eye.',
                'A <i>camera obscura</i> is a darkened room equipped with a tiny aperture through which light passes.'
            ],
            'C',
            'Goal-First SOP: Giải thích CÁCH Ibn al-Haytham dùng BẰNG CHỨNG THỰC NGHIỆM để LẬT ĐỔ thuyết phát xạ cổ đại ("how... used experimental evidence to overturn extramission theory"). A chỉ nhắc sơ ông thảo luận về nó; B chỉ dịch tên sách; D chỉ định nghĩa camera obscura. Duy nhất C nêu đủ thuyết cũ + hai bằng chứng thực nghiệm (dư ảnh đau mắt khi nhìn mặt trời & buồng tối lỗ kim) + kết luận lật đổ (ánh sáng đi từ ngoài vào mắt)!',
            'Kiểm tra đủ 3 mảnh ghép trong Goal: [1] Thuyết extramission cũ + [2] Bằng chứng thực nghiệm cụ thể + [3] Kết luận chứng minh ánh sáng đi vào mắt.',
            [
                ('Missing Method & Outcome', 'Chỉ nói ông "thảo luận" về thuyết cổ đại, thiếu hoàn toàn bằng chứng thực nghiệm và việc lật đổ nó.'),
                ('Wrong Synthesis Goal', 'Chỉ dịch tên sách từ tiếng Ả Rập sang tiếng Anh.'),
                ('Đáp án đúng', 'Kết hợp trọn vẹn cả thuyết bị bác bỏ, thí nghiệm thực chứng (dư ảnh mặt trời & camera obscura) và kết luận chứng minh thuyết intromission.'),
                ('Wrong Synthesis Goal', 'Chỉ định nghĩa camera obscura, không hề nhắc tới Ibn al-Haytham hay thuyết thị giác.'),
            ]
        ),
        q_item(
            'm8_m1_q27', 27, 'Expression of Ideas', 'Rhetorical Synthesis', 'Hard',
            '''<p>While researching ancient pigments, a student has taken the following notes:</p>
            <ul>
              <li>Maya Blue was synthesized by ancient Mesoamerican artisans who heated organic indigo dye extracted from <i>Indigofera</i> plants together with fibrous palygorskite clay.</li>
              <li>Heating locked the organic dye molecules tightly inside the clay’s natural microscopic channels.</li>
              <li>Egyptian Blue, widely used in Roman Pompeii frescoes, was an entirely inorganic synthetic pigment.</li>
              <li>Roman pigment makers fired mixtures of silica sand, copper compounds, and calcium carbonate in kilns at temperatures above 850°C to fuse calcium copper silicate crystals.</li>
            </ul>''',
            'The student wants to emphasize a contrast in the raw materials and manufacturing processes used to produce Maya Blue and Egyptian Blue. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
            [
                'Both Maya Blue and Egyptian Blue were durable blue pigments valued by ancient mural painters in Mesoamerica and Roman Pompeii.',
                'Whereas Maya Blue bound organic plant-derived indigo inside natural palygorskite clay through gentle heating, Egyptian Blue was forged entirely from inorganic sand, copper, and calcium compounds fired in kilns above 850°C.',
                'Maya Blue owed its stability to microscopic channels in fibrous palygorskite clay that trapped indigo molecules from <i>Indigofera</i> plants.',
                'Roman workshops created Egyptian Blue for Pompeii frescoes by fusing silica sand, copper compounds, and calcium carbonate into crystalline calcium copper silicate.'
            ],
            'B',
            'Goal-First SOP: Nhấn mạnh SỰ TƯƠNG PHẢN về NGUYÊN LIỆU và QUY TRÌNH CHẾ TẠO giữa Maya Blue và Egyptian Blue. A nhấn mạnh điểm giống (sai Goal!); C chỉ nói Maya Blue; D chỉ nói Egyptian Blue. Duy nhất B dùng từ nối tương phản "Whereas" đối chiếu rõ: hữu cơ thực vật + đất sét nung nhiệt nhẹ ↔ hoàn toàn vô cơ (cát, đồng, canxi) nung lò trên 850°C!',
            'Goal có chữ "contrast" + 2 đối tượng + 2 tiêu chí ("raw materials" & "manufacturing processes") → Đáp án đúng BẮT BUỘC có từ nối tương phản và đủ cả 2 tiêu chí cho cả 2 màu xanh!',
            [
                ('Wrong Synthesis Goal (Similarity)', 'Nhấn mạnh điểm giống nhau ("Both...") thay vì sự tương phản như Goal yêu cầu.'),
                ('Đáp án đúng', 'Đối chiếu sắc nét cả nguyên liệu (hữu cơ+đất sét vs hoàn toàn vô cơ) lẫn quy trình nhiệt độ của cả hai loại bột màu.'),
                ('One-Sided Synthesis', 'Chỉ mô tả Maya Blue, bỏ qua hoàn toàn Egyptian Blue.'),
                ('One-Sided Synthesis', 'Chỉ mô tả Egyptian Blue, bỏ qua hoàn toàn Maya Blue.'),
            ]
        ),
    ]
