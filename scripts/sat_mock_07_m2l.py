# -*- coding: utf-8 -*-
"""
Full-Length Adaptive Mock Test #7 — Module 2 LOWER/STANDARD Route (27 Qs, Easy/Medium, 32 min)
Exact College Board Digital SAT R&W Blueprint:
Q1-5: Words in Context | Q6-7: Text Structure/Purpose | Q8: Cross-Text
Q9-10: Central Ideas/Details | Q11-12: Evidence (Textual) | Q13-14: Evidence (Quantitative)
Q15: Inferences | Q16-19: Boundaries | Q20-22: Form/Structure/Sense
Q23-25: Transitions | Q26-27: Rhetorical Synthesis
"""

from sat_drills_1_1_and_2_1 import q_item
from sat_drills_5_4_to_5_5 import svg_bar_chart, html_table

def get_m2l_questions():
    return [
        # --- Q1-Q5: Craft and Structure — Words in Context (Easy / Medium) ---
        q_item(
            'm7_m2l_q1', 1, 'Craft and Structure', 'Words in Context', 'Easy',
            '<p>As a distant exoplanet passes directly in front of its star, space telescopes measure tiny dips in specific colors of starlight to ______ atmospheric gases such as water vapor, methane, and sodium.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            ['ignore', 'erase', 'postpone', 'detect'],
            'D',
            'Cause-Effect Clue: kính viễn vọng không gian đo những sụt giảm cực nhỏ ở từng dải màu ánh sáng sao nhằm PHÁT HIỆN các khí khí quyển như hơi nước, metan, natri → "detect" (D).',
            'Xác định mục đích khoa học của kính viễn vọng khi đo ánh sáng sao → chọn động từ nghĩa "phát hiện" ("detect").',
            [
                ('Opposite Meaning', 'ignore = phớt lờ bỏ qua — trái ngược hoàn toàn mục đích đo quang phổ.'),
                ('Wrong Meaning', 'erase = tẩy xóa — kính viễn vọng không xóa khí quyển hành tinh.'),
                ('Wrong Meaning', 'postpone = trì hoãn — vô nghĩa trong bối cảnh quang phổ học.'),
                ('Đáp án đúng', 'detect = phát hiện — khớp hoàn hảo với mục đích nhận diện các khí trong khí quyển ngoại hành tinh.'),
            ]
        ),
        q_item(
            'm7_m2l_q2', 2, 'Craft and Structure', 'Words in Context', 'Easy',
            '<p>Because carved cherry-wood printing blocks gradually softened after hundreds of pressings, museum curators prize the earliest impressions of Edo-period ukiyo-e landscapes for their remarkably ______ black outlines.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            ['blurred', 'crisp', 'silent', 'clumsy'],
            'B',
            'Contrast Clue: bản khắc gỗ anh đào dần bị mòn mềm sau hàng trăm lần in (làm nét bị nhòe), nên các bản in ĐẦU TIÊN được trân trọng nhờ đường viền đen cực kỳ SẮC NÉT → "crisp" (B).',
            'Đối lập trực tiếp với ván gỗ bị mòn sau hàng trăm lần in → chọn tính từ chỉ đường nét sắc gọn ("crisp").',
            [
                ('Opposite Meaning', 'blurred = mờ nhòe — đây là nhược điểm của bản in muộn khi ván đã mòn, không phải ưu điểm của bản đầu.'),
                ('Đáp án đúng', 'crisp = sắc nét, rõ ràng — khớp hoàn toàn lý do bản in sớm được giám tuyển trân quý.'),
                ('Wrong Context', 'silent = im lặng — không dùng để mô tả nét mực in.'),
                ('Negative Tone', 'clumsy = vụng về thô kệch — trái với từ "prize" (trân quý).'),
            ]
        ),
        q_item(
            'm7_m2l_q3', 3, 'Craft and Structure', 'Words in Context', 'Medium',
            '<p>In dry mountain valleys of Wyoming, terraced beaver ponds ______ runoff from melting spring snow so that surrounding meadows stay green and streams keep flowing even through rainless August afternoons.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            ['pollute', 'scatter', 'retain', 'evaporate'],
            'C',
            'Cause-Effect Clue: kết quả "surrounding meadows stay green and streams keep flowing even through rainless August afternoons" → các ao đập hải ly GIỮ LẠI nước tuyết tan mùa xuân → "retain" (C).',
            'Mệnh đề kết quả "giữ đồng cỏ xanh và suối chảy suốt tháng Tám không mưa" dẫn thẳng đến động từ "retain" (giữ lại).',
            [
                ('Negative Tone', 'pollute = làm ô nhiễm — trái ngược lợi ích sinh thái trong câu.'),
                ('Wrong Direction', 'scatter = làm phân tán mất — không giải thích việc tích trữ nước đến tận cuối hè.'),
                ('Đáp án đúng', 'retain = lưu giữ, tích trữ — khớp hoàn hảo với vai trò trữ nước tuyết tan của ao hải ly.'),
                ('Opposite Meaning', 'evaporate = làm bốc hơi cạn nước — trái ngược hoàn toàn với mục tiêu giữ suối chảy.'),
            ]
        ),
        q_item(
            'm7_m2l_q4', 4, 'Craft and Structure', 'Words in Context', 'Medium',
            '<p>During the 1930s, Harlem big-band arrangers broke away from rigid dance-hall formulas, blending blues call-and-response with shimmering brass harmonies in ______ ways that transformed modern American orchestral music.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            ['innovative', 'repetitive', 'hesitant', 'outdated'],
            'A',
            'Contrast + Result Clue: "broke away from rigid dance-hall formulas... transformed modern American orchestral music" → những cách phối khí ĐỔI MỚI, SÁNG TẠO → "innovative" (A).',
            'Cụm "broke away from rigid formulas" (phá bỏ khuôn sáo cứng nhắc) + "transformed" (làm biến đổi) chỉ thẳng tính từ "innovative".',
            [
                ('Đáp án đúng', 'innovative = đầy sáng tạo, đổi mới — đối lập rõ nét với khuôn sáo cứng nhắc trước đó.'),
                ('Opposite Meaning', 'repetitive = lặp đi lặp lại nhàm chán — trái với "broke away from rigid formulas".'),
                ('Wrong Tone', 'hesitant = rụt rè do dự — trái với thành tựu làm thay đổi cả nền âm nhạc giao hưởng.'),
                ('Opposite Meaning', 'outdated = lỗi thời — trái ngược hoàn toàn với "modern".'),
            ]
        ),
        q_item(
            'm7_m2l_q5', 5, 'Craft and Structure', 'Words in Context', 'Medium',
            '<p>Although colonial authorities discouraged local vernaculars in official schools for centuries, vibrant storytelling traditions in Caribbean Creole and Andean Quechua continue to ______ today through radio dramas, poetry festivals, and family gatherings.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            ['vanish', 'falter', 'retreat', 'endure'],
            'D',
            'Contrast Clue: "Although colonial authorities discouraged local vernaculars... vibrant storytelling traditions... continue to ______ today through radio dramas, poetry festivals..." → trái với áp lực ngăn cản nhiều thế kỷ, truyền thống kể chuyện vẫn TIẾP TỤC TỒN TẠI BỀN BỈ đến hôm nay → "endure" (D).',
            'Từ chuyển hướng "Although discouraged..." + tính từ tích cực "vibrant" đòi hỏi động từ chỉ sự trường tồn bền bỉ ("endure").',
            [
                ('Opposite Meaning', 'vanish = biến mất — trái ngược hoàn toàn với sức sống sôi nổi trên đài phát thanh và lễ hội thơ.'),
                ('Opposite Meaning', 'falter = chùn bước suy yếu — trái với tính từ "vibrant" (sôi động).'),
                ('Opposite Meaning', 'retreat = rút lui thu hẹp — mâu thuẫn ngữ cảnh.'),
                ('Đáp án đúng', 'endure = tồn tại bền bỉ qua thời gian — khớp tuyệt đối sau "Although discouraged... continue to".'),
            ]
        ),

        # --- Q6-Q7: Craft and Structure — Text Structure and Purpose (Easy / Medium) ---
        q_item(
            'm7_m2l_q6', 6, 'Craft and Structure', 'Text Structure and Purpose', 'Easy',
            '<p>As colossal Ice Age glaciers crept across northern North America, boulders frozen tightly into the bottom of the moving ice scraped long, parallel grooves—called glacial striations—into solid granite bedrock. <u>By measuring the compass orientation of these scratched grooves across hills and rocky outcrops, geologists can reconstruct the exact direction in which ancient ice sheets flowed thousands of years ago.</u> Even where the ice vanished long before human history began, the stone floor retains a clear map of its journey.</p>',
            'Which choice best describes the function of the underlined sentence in the text as a whole?',
            [
                'It argues that glacial striations appear only in granite hills of southern North America.',
                'It questions whether boulders frozen inside glaciers are hard enough to scratch solid bedrock.',
                'It explains how geologists use the bedrock grooves introduced in the first sentence to determine past glacial movement.',
                'It compares the speed of ancient Ice Age glaciers with the speed of modern mountain rivers.'
            ],
            'C',
            'Câu 1 giải thích cách hình thành các rãnh xước băng hà (glacial striations) trên nền đá. Câu gạch chân nêu CÁCH CÁC NHÀ ĐỊA CHẤT SỬ DỤNG các rãnh xước đó (đo phương hướng la bàn của rãnh để tái dựng chính xác hướng dòng chảy sông băng cổ đại) → Chọn C!',
            'Cấu trúc "By measuring [feature from Sentence 1], geologists can reconstruct..." cho thấy ngay chức năng giải thích ứng dụng khoa học của đặc điểm địa chất!',
            [
                ('Contradiction', 'Câu 1 ghi rõ "northern North America", không nói "only in southern North America".'),
                ('Contradiction', 'Câu gạch chân khẳng định giá trị của rãnh xước chứ không nghi ngờ khả năng tạo rãnh của đá tảng.'),
                ('Đáp án đúng', 'Khớp trực tiếp công dụng khoa học của rãnh xước: đo hướng la bàn để tái dựng chiều chảy sông băng cổ.'),
                ('Out of Scope', 'Không hề so sánh tốc độ sông băng với sông núi hiện đại.'),
            ]
        ),
        q_item(
            'm7_m2l_q7', 7, 'Craft and Structure', 'Text Structure and Purpose', 'Medium',
            '<p><i>The following text is adapted from a 1924 short story set in Harlem. Pianist Evelyn is rehearsing an original composition in a sunlit parlor before her neighborhood literary club arrives for its Sunday gathering.</i><br/>Her left hand began with the steady, rocking cadence her grandmother used to hum while shelling peas on a Georgia porch, warm and unhurried. Then her right hand answered with bright, quick chords borrowed from the clatter of Manhattan streetcars and the lively chatter along Seventh Avenue. Smiling as the two themes braided seamlessly across the ivory keys, Evelyn realized her song belonged equally to both worlds—carrying the warmth of home straight into the pulsing heart of the city.</p>',
            'Which choice best states the main purpose of the text?',
            [
                'To show that Evelyn feels anxious about performing in front of demanding literary club critics.',
                'To illustrate Evelyn’s delight in weaving memories of Southern heritage together with the lively energy of modern Harlem through her music.',
                'To explain why Manhattan streetcars made more rhythmic noise than neighborhood gatherings on Seventh Avenue.',
                'To criticize Evelyn’s grandmother for preferring traditional Georgia hymns over modern piano compositions.'
            ],
            'B',
            'Toàn đoạn khắc họa niềm vui mỉm cười của Evelyn ("Smiling as the two themes braided seamlessly...") khi tay trái gợi lại nhịp ngân nga ấm áp của bà ngoại ở Georgia còn tay phải hòa hợp âm rộn ràng của tàu điện và đại lộ Manhattan — bản nhạc thuộc về cả hai thế giới → Chọn B!',
            'Bắt tín hiệu cảm xúc "Smiling" + câu chốt "belonged equally to both worlds" để chọn ngay đáp án hòa quyện di sản miền Nam và nhịp sống Harlem!',
            [
                ('Wrong Tone', 'Evelyn mỉm cười đầy hài lòng, hoàn toàn không lo âu trước ban giám khảo hay nhà phê bình nào.'),
                ('Đáp án đúng', 'Khắc họa trọn vẹn niềm vui của Evelyn khi đan cài ký ức cội nguồn miền Nam với nhịp điệu sôi động của Harlem.'),
                ('Literal Misreading', 'Tàu điện và tiếng trò chuyện trên đại lộ Seventh đều là nguồn cảm hứng cho tay phải, không phải phép so sánh độ ồn.'),
                ('Out of Scope', 'Không hề có lời chê trách nào đối với bà ngoại.'),
            ]
        ),

        # --- Q8: Craft and Structure — Cross-Text Connections (Medium) ---
        q_item(
            'm7_m2l_q8', 8, 'Craft and Structure', 'Cross-Text Connections', 'Medium',
            '<p><b>Text 1</b><br/>Waterways advocate Dr. Omar Hassan argues that restoring beds of native freshwater mussels along polluted urban rivers offers a simple, self-sustaining cure for synthetic microfiber pollution because each mussel filters microplastics out of moving currents every day.</p><p><b>Text 2</b><br/>Freshwater ecologist Dr. Claire Bennett agrees that restored mussel colonies can remove impressive quantities of suspended microfibers from river water during calm weather. However, Bennett emphasizes that heavy rainstorms can stir settled plastic pellets back into the current and argues that cities must still install microfiber filters inside household washing machines to curb plastic waste at its source.</p>',
            'Based on the texts, how would Dr. Claire Bennett (Text 2) most likely respond to Dr. Omar Hassan’s argument (Text 1)?',
            [
                'By acknowledging that native mussels effectively filter microfibers from river currents, while warning that they are not a complete cure on their own without upstream laundry filtration.',
                'By asserting that freshwater mussels are completely unable to remove synthetic microfibers from urban river water.',
                'By claiming that heavy rainstorms permanently destroy synthetic microfibers before they can reach urban rivers.',
                'By agreeing that restoring freshwater mussel beds eliminates the need for filters inside household washing machines.'
            ],
            'A',
            'Text 1 xem phục hồi bãi trai như "phương thuốc đơn giản, tự duy trì hoàn hảo" cho vi sợi nhựa. Text 2 mở đầu bằng "agrees that restored mussel colonies can remove impressive quantities...", NHƯNG nối bằng "However" cảnh báo bão lớn có thể khuấy nhựa lên lại và thành phố VẪN phải lắp bộ lọc máy giặt để chặn từ nguồn → Chọn A (vừa ghi nhận hiệu quả của trai, vừa cảnh báo cần kết hợp lọc từ nguồn)!',
            'Nhận diện mẫu Cross-Text kinh điển: "Agrees with part X. However, warns about limitation Y and needs extra step Z" → Chọn đáp án dung hòa cả hai vế!',
            [
                ('Đáp án đúng', 'Phản ánh trung thực cả sự đồng tình một phần của Bennett lẫn cảnh báo rằng cần thêm bộ lọc máy giặt từ nguồn.'),
                ('Overstated Conflict', 'Bennett đồng ý rõ ràng rằng trai lọc được lượng lớn vi sợi khi thời tiết êm ("agrees... remove impressive quantities").'),
                ('Contradiction', 'Bão lớn khuấy viên nhựa quay lại dòng chảy chứ không phá hủy chúng.'),
                ('Reversed Logic', 'Bennett khẳng định ngược lại: các thành phố VẪN PHẢI lắp bộ lọc cho máy giặt.'),
            ]
        ),

        # --- Q9-Q10: Information and Ideas — Central Ideas and Details (Easy / Medium) ---
        q_item(
            'm7_m2l_q9', 9, 'Information and Ideas', 'Central Ideas and Details', 'Easy',
            '<p><i>The following poem, “The Willow Dam,” is adapted from a 1919 nature anthology.</i><br/>Across the narrow gravel ditch,<br/>Where April runoff raced away,<br/>The beaver laid a willow switch<br/>And packed each gap with river clay.<br/>Now where a dry bed used to bake,<br/>A quiet glassy pond expands;<br/>Blue herons wade the sheltered lake,<br/>And tree frogs sing in evening bands.</p>',
            'Which choice best states the main idea of the poem?',
            [
                'Spring runoff in April routinely washes away wooden beaver dams built across gravel ditches.',
                'Blue herons and tree frogs struggle to find food whenever shallow streams fill with river clay.',
                'Willow branches grow poorly along the edges of calm, sheltered ponds.',
                'By building a simple willow-and-clay dam, a beaver transforms a fast-draining ditch into a calm pond teeming with wildlife.'
            ],
            'D',
            'Ý chính bài thơ: 4 dòng đầu kể con hải ly đắp cành liễu và đất sét chặn ngang rãnh sỏi nơi nước xuân chảy mất nhanh; 4 dòng sau mô tả nơi từng là lòng suối khô nứt nay thành hồ yên ả thu hút diệc xanh lội nước và ếch cây ca hát → Chọn D!',
            'Đối chiếu hình ảnh "trước" (narrow gravel ditch / dry bed) và "sau" (quiet glassy pond / blue herons / tree frogs) để chốt Main Idea!',
            [
                ('Contradiction', 'Đập của hải ly chặn thành công nước chảy xiết tạo thành hồ yên tĩnh, không bị cuốn trôi.'),
                ('Reversed Logic', 'Diệc xanh và ếch cây tìm đến sinh sống vui vẻ ở hồ mới tạo, không gặp khó khăn tìm thức ăn.'),
                ('Out of Scope', 'Không bình luận về tốc độ mọc của cây liễu ven hồ.'),
                ('Đáp án đúng', 'Tóm gọn chính xác sự chuyển hóa từ rãnh thoát nước nhanh thành hồ yên ả giàu sự sống nhờ đập hải ly.'),
            ]
        ),
        q_item(
            'm7_m2l_q10', 10, 'Information and Ideas', 'Central Ideas and Details', 'Medium',
            '<p>Spoken across the Caribbean islands of Aruba, Bonaire, and Curaçao, Papiamento stands out among creole languages for its broad institutional prestige. Forged during the seventeenth century from Portuguese, Spanish, Dutch, and West African linguistic roots, Papiamento is not restricted to informal conversation; instead, residents use it daily in public classrooms, parliamentary debates, daily newspapers, and literary fiction.</p>',
            'According to the text, what distinguishes Papiamento from many other creole languages?',
            [
                'It is spoken exclusively during informal household conversations rather than in public offices.',
                'It borrowed its entire vocabulary from seventeenth-century Dutch without Spanish or Portuguese influence.',
                'It enjoys wide institutional use across education, government, journalism, and literature.',
                'It originated in the twentieth century specifically for radio broadcasts in Aruba and Bonaire.'
            ],
            'C',
            'Câu hỏi Specific Detail: Tìm ngay câu chứa "stands out among creole languages" → "for its broad institutional prestige... residents use it daily in public classrooms, parliamentary debates, daily newspapers, and literary fiction" → Paraphrase chính xác ở C!',
            'Ánh xạ trực tiếp từng lĩnh vực trong bài: classrooms (education), parliamentary debates (government), newspapers (journalism), literary fiction (literature)!',
            [
                ('Contradiction', 'Bài nói rõ Papiamento KHÔNG bị giới hạn trong hội thoại thân mật ("not restricted to informal conversation").'),
                ('Contradiction', 'Bài ghi rõ ngôn ngữ này kết hợp cả tiếng Bồ Đào Nha, Tây Ban Nha, Hà Lan và Tây Phi.'),
                ('Đáp án đúng', 'Khớp trọn vẹn danh sách lĩnh vực chính thức giúp Papiamento nổi bật về vị thế thể chế.'),
                ('Fact Distortion', 'Ngôn ngữ hình thành từ thế kỷ 17 ("during the seventeenth century"), không phải thế kỷ 20.'),
            ]
        ),

        # --- Q11-Q12: Information and Ideas — Command of Evidence (Textual — Easy / Medium) ---
        q_item(
            'm7_m2l_q11', 11, 'Information and Ideas', 'Command of Evidence (Textual)', 'Medium',
            '<p>Winding for fifteen kilometers across forested valleys in Maine, the Horseback Ridge is a steep, snake-like mound of sand and rounded gravel. Geologist Dr. Thomas Lind claims that the ridge is an esker—a streambed deposited by pressurized meltwater flowing inside an enclosed tunnel beneath an Ice Age glacier—rather than a former ocean shoreline built by open coastal waves.</p>',
            'Which finding, if true, would most directly support Dr. Thomas Lind’s claim?',
            [
                'Several modern pine forests growing atop the Horseback Ridge provide nesting habitat for regional songbirds.',
                'Cross-section surveys show that the ridge’s water-rounded gravel beds climb smoothly uphill over low bedrock rises—a path possible for water driven under pressure inside a closed ice tunnel, but impossible for level ocean shoreline waves.',
                'Nearby coastal beaches along southern Maine contain fine quartz sand eroded from granite headlands.',
                'Local nineteenth-century farmers built dirt wagon roads along the flat crest of the Horseback Ridge to avoid swampy lowlands.'
            ],
            'B',
            'Khóa giả thuyết của Lind: Dải sỏi hình thành từ DÒNG NƯỚC BĂNG TAN CÓ ÁP SUẤT chảy trong đường hầm kín dưới đáy sông băng (esker), KHÔNG phải đường bờ biển sóng vỗ mặt ngang. Đáp án B đưa ra dấu ấn vật lý phân biệt tuyệt đối hai giả thuyết: lớp sỏi cuội tròn nước chảy LEO LÊN DỐC qua gờ đá gốc — điều chỉ dòng nước có áp suất trong ống băng kín mới làm được, còn sóng bờ biển mặt ngang hoàn toàn bất khả thi! Chọn B!',
            'Tìm bằng chứng tách biệt hai giả thuyết ("subglacial pressurized tunnel" vs. "level ocean waves") → nước chảy ngược lên dốc đá chỉ có thể xảy ra trong đường hầm băng chịu áp suất!',
            [
                ('Irrelevant Detail', 'Rừng thông và chim làm tổ ngày nay không giải thích nguồn gốc địa chất từ Kỷ Băng Hà.'),
                ('Đáp án đúng', 'Bằng chứng vật lý sắc bén chứng minh cơ chế dòng chảy có áp suất dưới băng và loại trừ giả thuyết sóng bờ biển.'),
                ('Adjacent Topic Drift', 'Cát thạch anh trên bãi biển hiện đại ở nam Maine không chứng minh nguồn gốc của Horseback Ridge.'),
                ('Irrelevant History', 'Việc nông dân thế kỷ 19 làm đường xe ngựa trên sống đồi không liên quan đến quá trình tạo đồi.'),
            ]
        ),
        q_item(
            'm7_m2l_q12', 12, 'Information and Ideas', 'Command of Evidence (Textual)', 'Easy',
            '<p>In a review of the 1927 play <i>The Lenox Avenue Salon</i>, a literary critic states that author Beatrice urges young Harlem poets to draw their imagery from the vibrant neighborhood right outside their windows rather than imitating distant European pastoral poems.</p>',
            'Which quotation from Beatrice in <i>The Lenox Avenue Salon</i> most effectively illustrates the critic’s statement?',
            [
                '“The subway fare rose by a nickel last autumn, so many students now walk home along Amsterdam Avenue.”',
                '“Our literary club meets every Tuesday evening at seven in the back room of the neighborhood library.”',
                '“I misplaced my notebook somewhere between the corner bakery and the brownstone stoop this morning.”',
                '“Why keep borrowing skylarks and English meadows from dusty primers when the neon dusk, brownstone stoops, and laughter along Lenox Avenue already give us poetry enough for a lifetime?”'
            ],
            'D',
            'Checklist 2 vế: [1] Khuyên nhà thơ trẻ Harlem lấy chất liệu từ khu phố sống động quanh mình + [2] Tránh sao chép phong cảnh đồng quê châu Âu xa xôi. Đáp án D phản chiếu trực tiếp từng chi tiết: từ chối "mượn chim sơn ca và đồng cỏ nước Anh từ sách cũ" ↔ ca ngợi ánh đèn neon, bậc thềm nhà gạch nâu và tiếng cười trên đại lộ Lenox! Chọn D!',
            'So khớp đối lập ngay trong lời thoại: "English meadows" (đồng quê châu Âu) ↔ "Lenox Avenue" (khu phố Harlem ngay ngoài cửa sổ)!',
            [
                ('Irrelevant Detail', 'Chỉ nói về giá vé tàu điện ngầm.'),
                ('Irrelevant Detail', 'Chỉ thông báo lịch họp câu lạc bộ văn học tối thứ Ba.'),
                ('Irrelevant Detail', 'Chỉ kể chuyện làm rơi sổ tay.'),
                ('Đáp án đúng', 'Minh họa trực diện cả việc từ bỏ khuôn mẫu đồng quê châu Âu lẫn lời kêu gọi lấy cảm hứng từ đời sống đại lộ Lenox.'),
            ]
        ),

        # --- Q13-Q14: Information and Ideas — Command of Evidence (Quantitative — Easy / Medium) ---
        q_item(
            'm7_m2l_q13', 13, 'Information and Ideas', 'Command of Evidence (Quantitative)', 'Easy',
            svg_bar_chart(
                'Primary Sky Pigment in 120 Edo Landscape Woodblock Prints (1830–1850)',
                ['0%', '20%', '40%', '60%', '80%'],
                [('Prussian Blue', 64, '64%'), ('Natural Indigo', 22, '22%'), ('Dayflower Dye', 10, '10%'), ('Other Mineral', 4, '4%')],
                80
            ) + '<p>Art historians studying mid-nineteenth-century Japanese landscape prints note that shortly after synthetic Prussian blue became widely available in Edo workshops around 1830, it rapidly surpassed traditional plant-based blues to become the dominant sky colorant in well over half of surveyed prints.</p>',
            'Which choice most effectively uses data from the graph to support the art historians’ observation?',
            [
                'Prussian blue served as the primary sky pigment in 64% of the 120 surveyed prints—more than half the total and far surpassing both natural indigo (22%) and dayflower dye (10%).',
                'Other mineral pigments accounted for only 4% of the primary sky colorants in the 120 surveyed landscape prints.',
                'Natural indigo appeared as the primary sky pigment in 22% of surveyed prints, more than double the 10% share of dayflower dye.',
                'All four categories of blue and mineral pigments appeared in at least 4% of the surveyed landscape prints.'
            ],
            'A',
            'Checklist 2 vế nhận xét: [1] Prussian blue chiếm "well over half" (>50% → 64% ✓) + [2] Vượt xa các màu xanh thực vật truyền thống là natural indigo (22%) và dayflower dye (10%) ✓. B, C, D đều đúng biểu đồ nhưng không nhắc tới Prussian blue! Duy nhất A dẫn đầy đủ cả mốc 64% (>50%) lẫn so sánh với 22% và 10%! Chọn A!',
            'Kiểm tra đúng chủ thể của Claim ("Prussian blue" > 50% và vượt hai màu thực vật) → chọn ngay phương án nêu rõ 64% vs. 22% và 10%!',
            [
                ('Đáp án đúng', 'Khớp đầy đủ cả hai vế: Prussian blue đạt 64% (vượt xa mốc 50%) và bỏ xa natural indigo (22%) lẫn dayflower dye (10%).'),
                ('True Data / Wrong Subject', 'Chỉ nhắc Other Mineral (4%), bỏ qua Prussian blue.'),
                ('True Data / Wrong Subject', 'Chỉ so sánh hai màu thực vật với nhau (22% vs. 10%), bỏ sót Prussian blue.'),
                ('Incomplete Data', 'Chỉ nêu mức tối thiểu chung 4%, không chứng minh ưu thế áp đảo của Prussian blue.'),
            ]
        ),
        q_item(
            'm7_m2l_q14', 14, 'Information and Ideas', 'Command of Evidence (Quantitative)', 'Medium',
            html_table(
                'Table 1. Late-Summer Hydrological Measurements Across Four Mountain Creeks in Idaho (August 2024)',
                ['Creek Name', 'Active Beaver Dams', 'Mean Water Temp (°C)', 'Adjacent Wet Meadow Area (Hectares)'],
                [
                    ['Alder Creek', '14', '13.2°C', '18.5 ha'],
                    ['Willow Fork', '9', '14.6°C', '12.2 ha'],
                    ['Cedar Run', '3', '16.8°C', '4.1 ha'],
                    ['Granite Wash', '0', '19.4°C', '0.6 ha'],
                ]
            ) + '<p>Watershed biologists monitoring Idaho mountain streams report that creeks with larger numbers of active beaver dams maintain noticeably cooler August water temperatures and substantially broader adjacent wet meadows than creeks with few or no dams.</p>',
            'Which choice most effectively uses data from the table to support the biologists’ report?',
            [
                'Granite Wash contained zero active beaver dams and recorded an August water temperature of 19.4°C.',
                'All four surveyed mountain creeks in Idaho maintained adjacent wet meadow areas of at least 0.6 hectares in August 2024.',
                'Alder Creek (14 active dams) and Willow Fork (9 active dams) had cooler August temperatures (13.2°C and 14.6°C) and far wider wet meadows (18.5 ha and 12.2 ha) than Cedar Run (3 dams; 16.8°C; 4.1 ha) and Granite Wash (0 dams; 19.4°C; 0.6 ha).',
                'Cedar Run had three active beaver dams in August 2024, six fewer than Willow Fork had.'
            ],
            'C',
            'Checklist 2 vế báo cáo: so sánh suối NHIỀU đập (Alder Creek 14, Willow Fork 9) với suối ÍT/KHÔNG đập (Cedar Run 3, Granite Wash 0) trên CẢ HAI tiêu chí: nhiệt độ mát hơn (13,2°C & 14,6°C vs. 16,8°C & 19,4°C) VÀ đồng cỏ ẩm rộng hơn nhiều (18,5 ha & 12,2 ha vs. 4,1 ha & 0,6 ha). A, B, D mỗi câu đều thiếu đối chiếu hoặc bỏ sót biến số. Duy nhất C đối chiếu đầy đủ cả 4 con suối trên cả hai chỉ số! Chọn C!',
            'Tìm phương án đối chiếu đầy đủ nhóm nhiều đập vs. ít/không đập trên CẢ hai cột kết quả (nhiệt độ + diện tích đồng cỏ ẩm)!',
            [
                ('Incomplete Data', 'Chỉ nêu thông số 1 con suối Granite Wash mà không so sánh với các suối có đập và bỏ qua cột đồng cỏ ẩm.'),
                ('True Data / Wrong Claim', 'Chỉ nêu mức tối thiểu 0,6 ha, không thể hiện xu hướng tăng diện tích đồng cỏ và giảm nhiệt độ theo số đập.'),
                ('Đáp án đúng', 'Đối chiếu chính xác và đầy đủ cả hai nhóm suối trên cả hai biến nhiệt độ mát hơn và đồng cỏ ẩm rộng hơn.'),
                ('Incomplete Data', 'Chỉ so sánh số lượng đập giữa hai con suối, bỏ qua hoàn toàn nhiệt độ và đồng cỏ ẩm.'),
            ]
        ),

        # --- Q15: Information and Ideas — Inferences (Medium) ---
        q_item(
            'm7_m2l_q15', 15, 'Information and Ideas', 'Inferences', 'Medium',
            '<p>When astronomers analyze starlight passing through an exoplanet’s atmosphere, lightweight hydrogen-rich atmospheres puff far outward from the planet and produce large, easily detected absorption dips. Heavier atmospheres composed mainly of carbon dioxide or nitrogen hug tightly to the planet’s surface and create much smaller signals. During recent space-telescope transits of the warm rocky planet Kepler-99x, astronomers found a completely flat spectrum showing no large absorption dips, even though their instrument was sensitive enough to spot a puffy hydrogen envelope effortlessly. These observations therefore suggest that ______</p>',
            'Which choice most logically completes the text?',
            [
                'Kepler-99x orbits too far from its host star to ever cross in front of the star from Earth’s viewpoint.',
                'Kepler-99x is unlikely to possess a thick, puffy hydrogen-rich atmosphere.',
                'carbon dioxide atmospheres expand farther into space than lightweight hydrogen atmospheres do.',
                'modern space telescopes are completely incapable of detecting lightweight hydrogen gas on any exoplanet.'
            ],
            'B',
            'Suy luận trực tiếp: (1) Nếu có khí quyển giàu hydro phồng rộng → sẽ tạo vạch hấp thụ lớn, dễ đo; (2) Thiết bị dư sức phát hiện khí quyển hydro phồng rộng nhưng quang phổ đo được lại hoàn toàn phẳng ⇒ Kết luận hợp lý nhất: Kepler-99x nhiều khả năng KHÔNG có khí quyển giàu hydro dày phồng (B)!',
            'Logic phủ định thuận chiều: Nếu có A thì chắc chắn thấy tín hiệu lớn → Thiết bị đủ nhạy nhưng không thấy tín hiệu lớn → Suy ra không có A!',
            [
                ('Contradiction', 'Bài nói rõ các nhà thiên văn VỪA quan sát các lần quá cảnh ("recent space-telescope transits") của Kepler-99x.'),
                ('Đáp án đúng', 'Suy diễn chặt chẽ từ việc phổ phẳng dù kính đủ độ nhạy bắt khí quyển hydro phồng rộng.'),
                ('Reversed Logic', 'Bài nêu ngược lại: khí quyển carbon dioxide nặng bám sát bề mặt, còn hydro mới phồng rộng ra xa.'),
                ('Contradiction', 'Bài khẳng định thiết bị đủ nhạy để phát hiện vỏ hydro phồng một cách dễ dàng ("effortlessly").'),
            ]
        ),

        # --- Q16-Q19: Standard English Conventions — Boundaries (Easy / Medium) ---
        q_item(
            'm7_m2l_q16', 16, 'Standard English Conventions', 'Boundaries', 'Easy',
            '<p>During the height of the Inca Empire, imperial administrators promoted Quechua as a shared language across the ______ today, more than seven million people in Peru, Bolivia, and Ecuador still speak regional Quechua varieties.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['Andes,', 'Andes', 'Andes, because', 'Andes;'],
            'D',
            'Vế 1 là 1 IC hoàn chỉnh ("During the height..., imperial administrators promoted Quechua... across the Andes"). Vế 2 cũng là 1 IC hoàn chỉnh ("today, more than seven million people... still speak regional Quechua varieties"). Giữa 2 IC → Chọn dấu chấm phẩy (`;`) = D!',
            'Nhận diện ranh giới IC + IC → chọn ngay dấu chấm phẩy (`;`), loại Comma Splice (A) và Run-on (B)!',
            [
                ('Comma Splice', 'Nối hai mệnh đề độc lập chỉ bằng một dấu phẩy là lỗi Comma Splice.'),
                ('Run-On Sentence', 'Không có dấu câu ngăn cách hai mệnh đề độc lập.'),
                ('Wrong Logic', 'Thêm "because" đảo ngược vô lý quan hệ nhân quả (người Inca quảng bá ngôn ngữ không phải VÌ ngày nay có 7 triệu người nói!).'),
                ('Đáp án đúng', 'Dấu chấm phẩy (;) ngăn cách chuẩn xác hai mệnh đề độc lập IC + IC.'),
            ]
        ),
        q_item(
            'm7_m2l_q17', 17, 'Standard English Conventions', 'Boundaries', 'Easy',
            '<p>Although an individual freshwater mussel measures only a few inches ______ a dense riverbed colony of several thousand mussels can filter millions of liters of river water every day.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['long;', 'long.', 'long,', 'long'],
            'C',
            'Vế 1 bắt đầu bằng liên từ phụ thuộc `Although` → đây là Mệnh đề phụ thuộc (DC: "Although an individual freshwater mussel measures only a few inches long"). Vế 2 là Mệnh đề độc lập (IC: "a dense riverbed colony... can filter..."). Quy tắc chuẩn: **DC + `,` + IC** → Chọn `long,` (C)!',
            'Công thức nền tảng: Mệnh đề mở đầu bằng `Although / Because / While` (DC) + dấu phẩy `,` + Mệnh đề chính (IC)! Cấm dùng `;` hoặc `.` sau DC!',
            [
                ('Semicolon After DC', 'Cấm đặt dấu chấm phẩy sau mệnh đề phụ thuộc mở đầu bằng "Although".'),
                ('Period After DC (Fragment)', 'Chấm câu sau "Although..." tạo thành Sentence Fragment.'),
                ('Đáp án đúng', 'Dấu phẩy (,) ngăn cách chuẩn xác mệnh đề phụ mở đầu ("Although...") với mệnh đề chính.'),
                ('Missing Comma', 'Thiếu dấu phẩy sau mệnh đề phụ thuộc mở đầu dài.'),
            ]
        ),
        q_item(
            'm7_m2l_q18', 18, 'Standard English Conventions', 'Boundaries', 'Medium',
            '<p>Bandleader Duke Ellington, ______ composed landmark orchestral works such as <i>Black, Brown and Beige</i> that expanded jazz far beyond brief three-minute dance records.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['a pioneering Harlem pianist and composer', 'a pioneering Harlem pianist and composer,', 'a pioneering Harlem pianist and composer;', 'a pioneering Harlem pianist and composer.'],
            'B',
            'Cụm đồng vị bổ sung (`a pioneering Harlem pianist and composer`) đứng xen giữa Chủ ngữ ("Bandleader Duke Ellington") và Động từ chính ("composed"). Phía trước chỗ trống ĐÃ CÓ dấu phẩy mở (`Ellington,`) → Bắt buộc phải có dấu phẩy đóng ngay cuối cụm (`composer,`) → Chọn B!',
            'Quy tắc Cặp phẩy kẹp đồng vị (Non-essential Appositive Pair): Mở bằng dấu phẩy `,` → Phải đóng bằng dấu phẩy `,` trước động từ chính `composed`!',
            [
                ('Unclosed Appositive', 'Thiếu dấu phẩy đóng sau "composer" để khép cụm đồng vị đã mở bằng dấu phẩy sau "Ellington".'),
                ('Đáp án đúng', 'Khép đúng cặp dấu phẩy (, ... ,) bao quanh cụm đồng vị trước động từ chính "composed".'),
                ('Semicolon Inside Clause', 'Dấu chấm phẩy tách đứt chủ ngữ khỏi động từ chính.'),
                ('Period Fragment', 'Đặt dấu chấm biến nửa đầu thành đoạn cụt không có động từ chính.'),
            ]
        ),
        q_item(
            'm7_m2l_q19', 19, 'Standard English Conventions', 'Boundaries', 'Medium',
            '<p>Retreating alpine glaciers leave behind three classic geological ______ polished bedrock grooves, unsorted boulder ridges, and bowl-shaped mountain basins called cirques.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['features:', 'features;', 'features.', 'features, and'],
            'A',
            'Vế trái là 1 IC hoàn chỉnh ("Retreating alpine glaciers leave behind three classic geological features"). Vế phải là DANH SÁCH CỤM DANH TỪ liệt kê rõ 3 đặc điểm địa chất đó (KHÔNG phải IC!). Sau IC giới thiệu danh sách → Bắt buộc dùng dấu hai chấm (`:`) = A!',
            'IC hoàn chỉnh + Danh sách cụm danh từ minh họa (không phải IC) → chọn dấu hai chấm (`:`), loại ngay `;` và `.`!',
            [
                ('Đáp án đúng', 'Dấu hai chấm (:) sau IC giới thiệu chính xác danh sách ba đặc điểm địa chất cổ điển.'),
                ('Semicolon + Fragment', 'Vế sau là danh sách cụm danh từ, không phải IC → cấm dấu chấm phẩy.'),
                ('Period + Fragment', 'Tách danh sách cụm danh từ thành câu độc lập tạo Sentence Fragment.'),
                ('Wrong Coordination', '", and" nối mệnh đề với danh sách 3 cụm danh từ không song song về mặt cấu trúc.'),
            ]
        ),

        # --- Q20-Q22: Standard English Conventions — Form, Structure, and Sense (Easy / Medium) ---
        q_item(
            'm7_m2l_q20', 20, 'Standard English Conventions', 'Form, Structure, and Sense', 'Easy',
            '<p>The tightly woven willow branches inside a beaver dam ______ rushing spring floodwaters while allowing clean stream flow to seep steadily downstream.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['slows', 'slow', 'has slowed', 'slowing'],
            'B',
            'Gạch cụm giới từ chen giữa: "The tightly woven willow <b>branches</b> <s>[inside a beaver dam]</s>". Chủ ngữ thật là **"branches"** (SỐ NHIỀU!). Câu cần động từ chính chia thì số nhiều → Chọn **"slow"** (B)!',
            'Đừng bị lừa bởi danh từ số ít `a beaver dam` ngay sát chỗ trống — gạch cụm giới từ `inside...` đi sẽ thấy ngay chủ ngữ số nhiều `branches`!',
            [
                ('Subject-Verb Mismatch', 'slows là số ít — bị lừa bởi "a beaver dam".'),
                ('Đáp án đúng', 'slow (số nhiều, hiện tại đơn) khớp chuẩn với chủ ngữ số nhiều "The tightly woven willow branches".'),
                ('Subject-Verb Mismatch', 'has slowed là số ít.'),
                ('Non-Finite Fragment', 'slowing là phân từ V-ing khiến câu không có động từ chính.'),
            ]
        ),
        q_item(
            'm7_m2l_q21', 21, 'Standard English Conventions', 'Form, Structure, and Sense', 'Medium',
            '<p>In 1831, Edo publisher Nishimuraya Yohachi commissioned Katsushika Hokusai to design a Mount Fuji print series and ______ thousands of affordable woodblock sheets to enthusiastic travelers.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['sells', 'will sell', 'has sold', 'sold'],
            'D',
            'Kiểm tra thì động từ và cấu trúc song song: Mốc thời gian quá khứ xác định **`In 1831`** + động từ quá khứ đơn **`commissioned`** nối bằng **`and`** → Động từ thứ hai bắt buộc chia Quá khứ đơn song song là **`sold`** (D)!',
            'Thấy mốc lịch sử cụ thể (`In 1831`) + `commissioned ... and [VERB]` → chọn ngay Quá khứ đơn (`sold`) để giữ song song thì!',
            [
                ('Tense Shift Error', 'sells là hiện tại đơn — mâu thuẫn với mốc quá khứ "In 1831" và "commissioned".'),
                ('Tense Shift Error', 'will sell là tương lai — vô lý cho sự kiện năm 1831.'),
                ('Tense Shift Error', 'has sold (hiện tại hoàn thành) không dùng song song cho hành động hoàn tất tại mốc quá khứ xác định "In 1831".'),
                ('Đáp án đúng', 'sold (quá khứ đơn) song song chính xác với "commissioned" trong bối cảnh năm 1831.'),
            ]
        ),
        q_item(
            'm7_m2l_q22', 22, 'Standard English Conventions', 'Form, Structure, and Sense', 'Medium',
            '<p>When a rocky exoplanet orbits extremely close to a host star, intense stellar radiation heats the planet’s upper atmosphere and gradually strips away ______ lightest gases.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['their', 'it’s', 'its', 'there'],
            'C',
            'Kiểm tra đại từ sở hữu & số ít/số nhiều: Danh từ tiền lệ được nhắc là **"the planet’s upper atmosphere"** (SỐ ÍT!). Cần tính từ sở hữu số ít đứng trước `lightest gases` → Chọn **`its`** (C)! Lưu ý bẫy `it’s` = `it is` (sai!), `their` = số nhiều (sai!), `there` = trạng từ chỉ nơi chốn (sai!).',
            'Nhớ phân biệt tuyệt đối: `its` (sở hữu của nó — KHÔNG có dấu nháy) vs. `it’s` (= `it is / it has`)!',
            [
                ('Pronoun Number Mismatch', 'their là số nhiều — không khớp tiền lệ số ít "the planet’s upper atmosphere".'),
                ('Contraction Trap', 'it’s = it is / it has — sai ngữ pháp trước "lightest gases".'),
                ('Đáp án đúng', 'its là tính từ sở hữu số ít khớp chuẩn với "the planet’s upper atmosphere".'),
                ('Homophone Error', 'there chỉ địa điểm, không phải tính từ sở hữu.'),
            ]
        ),

        # --- Q23-Q25: Expression of Ideas — Transitions (Easy / Medium) ---
        q_item(
            'm7_m2l_q23', 23, 'Expression of Ideas', 'Transitions', 'Easy',
            '<p>Caribbean creole languages weave vocabulary and grammatical features from multiple continents into vibrant new tongues. ______, Jamaican Patois blends English words with West African Akan expressions and distinctive rhythmic intonation.</p>',
            'Which choice completes the text with the most logical transition?',
            ['For example', 'However', 'Instead', 'Consequently'],
            'A',
            'Câu 1 nêu nhận định tổng quát về các ngôn ngữ creole vùng Caribe. Câu 2 đưa ra một trường hợp minh họa cụ thể là tiếng **Jamaican Patois** → Quan hệ Minh họa ví dụ → **"For example"** (A)!',
            'Từ nhóm khái quát ("Caribbean creole languages") thu hẹp xuống một ví dụ cụ thể ("Jamaican Patois") → chốt ngay "For example / For instance"!',
            [
                ('Đáp án đúng', 'For example nối chính xác nhận định chung ở câu 1 với ví dụ cụ thể Jamaican Patois ở câu 2.'),
                ('False Contrast', 'However sai vì câu 2 minh họa cùng chiều cho câu 1.'),
                ('Wrong Relationship (Replacement)', 'Instead sai vì không có câu phủ định cần thay thế.'),
                ('Wrong Relationship (Cause-Effect)', 'Jamaican Patois là ví dụ minh họa chứ không phải hệ quả nhân quả của câu 1.'),
            ]
        ),
        q_item(
            'm7_m2l_q24', 24, 'Expression of Ideas', 'Transitions', 'Medium',
            '<p>Massive valley glaciers slowly grind rocky boulders across both the floor and steep side walls of a mountain channel like giant sheets of sandpaper. ______, valleys sculpted by ancient glaciers typically display wide, U-shaped troughs rather than narrow, V-shaped river gorges.</p>',
            'Which choice completes the text with the most logical transition?',
            ['Nevertheless', 'Therefore', 'Meanwhile', 'Similarly'],
            'B',
            'Câu 1 nêu nguyên nhân vật lý (sông băng mài mòn cả đáy lẫn vách dốc thung lũng như giấy nhám khổng lồ). Câu 2 nêu kết quả địa mạo trực tiếp (thung lũng băng hà thường có lòng chữ U rộng thay vì hẻm chữ V hẹp) → Quan hệ Nhân – Quả → **"Therefore"** (B)!',
            'Quá trình bào mòn đáy và vách (Nguyên nhân) → Hình dạng thung lũng chữ U (Kết quả) → chọn "Therefore / Consequently"!',
            [
                ('False Contrast', 'Nevertheless chỉ sự trái kỳ vọng — ngược hoàn toàn quan hệ nguyên nhân – kết quả.'),
                ('Đáp án đúng', 'Therefore nối chính xác cơ chế mài mòn băng hà ở câu 1 với hình thái thung lũng chữ U ở câu 2.'),
                ('Wrong Relationship (Time)', 'Meanwhile chỉ hai sự việc diễn ra song song về thời gian.'),
                ('Wrong Relationship (Similarity)', 'Similarly dùng để so sánh hai đối tượng tương đồng độc lập, không phải nguyên nhân – kết quả.'),
            ]
        ),
        q_item(
            'm7_m2l_q25', 25, 'Expression of Ideas', 'Transitions', 'Medium',
            '<p>Mechanical mesh screens at municipal wastewater plants easily catch large plastic wrappers and bottle caps before treated water returns to local rivers. ______, microscopic synthetic fibers shed during household laundry readily slip straight through standard mechanical filters.</p>',
            'Which choice completes the text with the most logical transition?',
            ['In addition', 'Consequently', 'For instance', 'However'],
            'D',
            'Câu 1: Lưới lọc cơ học dễ dàng chặn rác nhựa lớn (túi bọc, nắp chai). Câu 2: Trái lại, vi sợi tổng hợp siêu nhỏ từ máy giặt lại dễ dàng lọt thẳng qua bộ lọc tiêu chuẩn → Quan hệ Tương phản trực tiếp → **"However"** (D)!',
            'Đối lập rõ nét giữa "easily catch large plastic" (chặn dễ rác lớn) và "readily slip straight through" (lọt thẳng qua lưới đối với vi sợi nhỏ) → chọn "However"!',
            [
                ('Wrong Relationship (Addition)', 'In addition nối hai ý cùng chiều — sai vì câu 2 nêu hạn chế trái ngược câu 1.'),
                ('Wrong Relationship (Cause-Effect)', 'Việc chặn được nắp chai không phải nguyên nhân khiến vi sợi lọt qua.'),
                ('Wrong Relationship (Example)', 'Vi sợi lọt lưới là trường hợp đối lập, không phải ví dụ cho rác lớn bị chặn.'),
                ('Đáp án đúng', 'However thể hiện sắc nét sự đối lập giữa hiệu quả chặn rác lớn và điểm yếu trước vi sợi siêu nhỏ.'),
            ]
        ),

        # --- Q26-Q27: Expression of Ideas — Rhetorical Synthesis (Easy / Medium) ---
        q_item(
            'm7_m2l_q26', 26, 'Expression of Ideas', 'Rhetorical Synthesis', 'Easy',
            '''<p>While researching a topic, a student has taken the following notes:</p>
            <ul>
              <li><i>The New Negro</i> is a landmark 1925 anthology of essays, poetry, fiction, and visual art edited by philosopher Alain Locke.</li>
              <li>The volume brought together emerging Black writers, musicians, and critics centered in Harlem during the 1920s.</li>
              <li>Locke edited the anthology to showcase African American artistic innovation and challenge outdated cultural stereotypes.</li>
              <li>The book became widely recognized as a defining manifesto of the Harlem Renaissance.</li>
            </ul>''',
            'The student wants to introduce the 1925 anthology <i>The New Negro</i> and explain Alain Locke’s main goal in editing it. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
            [
                'Edited by philosopher Alain Locke in 1925, the landmark anthology <i>The New Negro</i> gathered Harlem essays, poetry, fiction, and art to showcase African American artistic innovation and challenge outdated cultural stereotypes.',
                'During the 1920s, many emerging Black writers, musicians, and critics lived and worked in Harlem.',
                '<i>The New Negro</i> included multiple literary and artistic genres, such as essays, poetry, fiction, and visual art.',
                'Philosopher Alain Locke edited a book in 1925 that later came to be recognized as a defining manifesto of the Harlem Renaissance.'
            ],
            'A',
            'Goal-First SOP: Giới thiệu tuyển tập năm 1925 *The New Negro* VÀ giải thích MỤC TIÊU CHÍNH của Alain Locke khi biên tập nó. Kiểm tra đủ 2 vế: [1] Giới thiệu cuốn sách (tuyển tập 1925 do Alain Locke biên tập); [2] Mục tiêu chính ("to showcase African American artistic innovation and challenge outdated cultural stereotypes"). B, C, D đều bỏ sót hoàn toàn mục tiêu biên tập của Locke! Duy nhất A gói trọn cả hai vế! Chọn A!',
            'Tìm đúng cụm mục tiêu "to showcase... and challenge..." trong các phương án — chỉ duy nhất A thực hiện trọn vẹn Goal!',
            [
                ('Đáp án đúng', 'Giới thiệu rõ ràng tuyển tập năm 1925 và nêu đầy đủ mục tiêu tôn vinh sáng tạo nghệ thuật, phá bỏ định kiến cũ của Alain Locke.'),
                ('Wrong Synthesis Goal', 'Không nhắc tên cuốn sách lẫn mục tiêu của Alain Locke.'),
                ('Missing Goal', 'Chỉ liệt kê các thể loại trong sách mà bỏ qua mục tiêu biên tập của Locke.'),
                ('Missing Goal', 'Chỉ nêu tác động về sau của cuốn sách, không giải thích mục đích của Locke khi biên tập.'),
            ]
        ),
        q_item(
            'm7_m2l_q27', 27, 'Expression of Ideas', 'Rhetorical Synthesis', 'Medium',
            '''<p>While researching a topic, a student has taken the following notes:</p>
            <ul>
              <li>Cusco Quechua and Ayacucho Quechua are two major Southern Quechua dialects spoken in highland Peru.</li>
              <li>Both dialects share core grammar, including evidential suffixes that show how a speaker learned information.</li>
              <li>Speakers of both dialects can generally understand one another in everyday conversation.</li>
              <li>Unlike Ayacucho Quechua, however, Cusco Quechua distinguishes between plain, aspirated, and glottalized stop consonants.</li>
            </ul>''',
            'The student wants to highlight both a key similarity and a key pronunciation difference between Cusco Quechua and Ayacucho Quechua. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
            [
                'Cusco Quechua and Ayacucho Quechua are two major Southern Quechua dialects spoken in the Peruvian highlands.',
                'Because Cusco Quechua and Ayacucho Quechua share core grammar, speakers of the two dialects can generally understand each other.',
                'Although Cusco Quechua and Ayacucho Quechua share core grammatical features such as evidential suffixes, Cusco Quechua differs in pronunciation by distinguishing among plain, aspirated, and glottalized stop consonants.',
                'Cusco Quechua distinguishes among plain, aspirated, and glottalized stop consonants in highland Peru.'
            ],
            'C',
            'Goal-First SOP: Làm nổi bật CẢ ĐIỂM TƯƠNG ĐỒNG CHÍNH (similarity) LẪN ĐIỂM KHÁC BIỆT PHÁT ÂM (pronunciation difference) giữa Cusco Quechua và Ayacucho Quechua. A và B chỉ nêu điểm chung; D chỉ nói một mình Cusco Quechua. Duy nhất C kết hợp trọn vẹn bằng "Although": điểm chung (chung ngữ pháp cốt lõi như hậu tố chứng cứ) + điểm khác biệt phát âm (Cusco phân biệt 3 loại phụ âm tắc plain/aspirated/glottalized)! Chọn C!',
            'Goal yêu cầu "both a similarity AND a pronunciation difference" → loại mọi phương án chỉ có 1 vế, chọn câu chứa cấu trúc đối chiếu `Although [similarity], [pronunciation difference]`!',
            [
                ('Missing Pronunciation Difference', 'Chỉ nêu cả hai là phương ngữ Quechua miền Nam ở Peru, thiếu khác biệt phát âm.'),
                ('Missing Pronunciation Difference', 'Chỉ nêu điểm tương đồng về ngữ pháp và khả năng hiểu nhau.'),
                ('Đáp án đúng', 'Khớp hoàn chỉnh cả hai yêu cầu: tương đồng về ngữ pháp cốt lõi và khác biệt cụ thể về hệ phụ âm tắc.'),
                ('One-Sided Information', 'Chỉ nói về phụ âm của Cusco Quechua, bỏ qua hoàn toàn Ayacucho Quechua và điểm tương đồng.'),
            ]
        ),
    ]
