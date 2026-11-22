# -*- coding: utf-8 -*-
"""
Digital SAT Reading & Writing Adaptive Mock Test #3
Module 2 Lower / Standard Route (27 Questions, Easy & Medium Tier)
IDs: m3_m2l_q1 .. m3_m2l_q27
"""

from sat_drills_1_1_and_2_1 import q_item
from sat_drills_5_4_to_5_5 import svg_bar_chart, html_table

STEM_WIC = 'Which choice completes the text with the most logical and precise word or phrase?'
STEM_SEC = 'Which choice completes the text so that it conforms to the conventions of Standard English?'
STEM_TRANS = 'Which choice completes the text with the most logical transition?'
STEM_INF = 'Which choice most logically completes the text?'


def get_m2l_questions():
    return [
        # ------------------------------------------------------------------
        # Q1-Q5: Craft and Structure — Words in Context
        # ------------------------------------------------------------------
        q_item(
            'm3_m2l_q1', 1, 'Craft and Structure', 'Words in Context', 'Easy',
            '<p>Cognitive psychologists studying the “spacing effect” have repeatedly found that students who review new vocabulary in brief sessions spread across several days ______ far more words a month later than students who study for the same total time in one exhausting evening.</p>',
            STEM_WIC,
            ['retain', 'abandon', 'invent', 'misplace'],
            'A',
            'Ngữ cảnh nói về hiệu ứng giãn cách học tập ("spacing effect"): học thành nhiều phiên ngắn trải đều vài ngày giúp sinh viên "ghi nhớ / lưu giữ" được nhiều từ vựng hơn sau một tháng so với học nhồi nhét trong một buổi tối → "retain" (A).',
            'Đọc cụm "far more words a month later" để xác định ngay động từ chỉ khả năng ghi nhớ lâu dài ("retain").',
            [
                ('Đáp án đúng', 'retain = lưu giữ/ghi nhớ được lâu dài — khớp tuyệt đối với ngữ cảnh kiểm tra từ vựng sau một tháng.'),
                ('Opposite Meaning', 'abandon = từ bỏ — trái ngược với lợi ích của phương pháp học giãn cách.'),
                ('Wrong Meaning', 'invent = phát minh/bịa ra — học sinh đang ôn từ mới chứ không bịa ra từ.'),
                ('Opposite Meaning', 'misplace = làm thất lạc — không phù hợp với ngữ cảnh ghi nhớ từ vựng.'),
            ]
        ),
        q_item(
            'm3_m2l_q2', 2, 'Craft and Structure', 'Words in Context', 'Easy',
            '<p>During the fourteenth century, the Mali Empire’s control over trans-Saharan gold and salt trade routes brought remarkable ______ to Niger River trading centers such as Djenné and Gao, enabling rulers to fund grand mud-brick mosques, bustling markets, and public schools.</p>',
            STEM_WIC,
            ['isolation', 'fragility', 'prosperity', 'secrecy'],
            'C',
            'Vế sau giải thích kết quả trực tiếp: các vị vua đủ nguồn lực tài trợ xây dựng Đại Thánh đường, chợ sầm uất và trường học ("fund grand mud-brick mosques, bustling markets, and public schools") → thương mại vàng – muối mang lại sự "thịnh vượng" to lớn → "prosperity" (C).',
            'Lần theo dấu hiệu kết quả sau dấu phẩy ("enabling rulers to fund grand mosques, bustling markets...") để chọn danh từ mang sắc thái giàu có, phồn thịnh.',
            [
                ('Opposite Meaning', 'isolation = sự cô lập — trái ngược với các trung tâm thương mại sầm uất kết nối xuyên Sahara.'),
                ('Opposite Meaning', 'fragility = sự mong manh yếu ớt — không khớp với sự phát triển mạnh mẽ của đế chế Mali.'),
                ('Đáp án đúng', 'prosperity = sự thịnh vượng/phồn vinh — giải thích hoàn hảo nguồn lực xây dựng đền đài, chợ và trường học.'),
                ('Wrong Meaning', 'secrecy = sự bí mật — không liên quan đến khả năng tài trợ công trình công cộng.'),
            ]
        ),
        q_item(
            'm3_m2l_q3', 3, 'Craft and Structure', 'Words in Context', 'Medium',
            '<p>Because harvesting corn removes substantial quantities of nitrogen from farmland each autumn, many Midwest growers alternate corn with soybeans every other season. Symbiotic bacteria inside soybean root nodules convert atmospheric nitrogen into usable plant nutrients, helping ______ the soil before the next corn crop is planted.</p>',
            STEM_WIC,
            ['exhaust', 'replenish', 'conceal', 'restrict'],
            'B',
            'Câu 1 nêu việc thu hoạch ngô lấy đi lượng lớn nitơ khỏi đất. Câu 2 giải thích vi khuẩn cộng sinh ở nốt sần rễ đậu nành chuyển hóa nitơ không khí thành dinh dưỡng cho cây → giúp "bổ sung / phục hồi lại" nguồn dinh dưỡng cho đất trước vụ ngô tiếp theo → "replenish" (B).',
            'Chú ý đối chiếu "removes substantial quantities of nitrogen" (lấy đi) với giải pháp luân canh đậu nành (bù đắp trở lại = "replenish").',
            [
                ('Opposite Meaning', 'exhaust = làm cạn kiệt — ngược hoàn toàn với tác dụng bổ sung nitơ của cây đậu nành.'),
                ('Đáp án đúng', 'replenish = bổ sung/làm đầy lại nguồn đã tiêu hao — khớp tuyệt đối với ngữ cảnh luân canh phục hồi đạm đất.'),
                ('Wrong Meaning', 'conceal = che giấu — không có nghĩa hợp lý với tân ngữ "the soil".'),
                ('Wrong Meaning', 'restrict = hạn chế/ràng buộc — không phù hợp với vai trò bồi dưỡng dinh dưỡng cho đất.'),
            ]
        ),
        q_item(
            'm3_m2l_q4', 4, 'Craft and Structure', 'Words in Context', 'Medium',
            '<p>Before weather satellites began orbiting Earth in the 1960s, coastal forecasters lacked overhead views of distant ocean basins and had to depend on radioed barometer readings from merchant ships to ______ approaching tropical storms days before they reached shore.</p>',
            STEM_WIC,
            ['prevent', 'delay', 'dissolve', 'detect'],
            'D',
            'Trước khi có vệ tinh thời tiết, nhà dự báo khí tượng ven biển thiếu ảnh chụp từ trên cao nên phải dựa vào chỉ số áp kế từ tàu buôn để "phát hiện" các cơn bão nhiệt đới đang tiến gần vài ngày trước khi đổ bộ → "detect" (D).',
            'Kiểm tra tính khả thi thực tế với chủ ngữ "coastal forecasters" và công cụ "barometer readings": áp kế chỉ giúp PHÁT HIỆN bão chứ không thể ngăn chặn (A), trì hoãn (B) hay làm tan bão (C)!',
            [
                ('Illogical Action', 'prevent = ngăn chặn — đo áp kế không thể ngăn cơn bão nhiệt đới hình thành hay xảy ra.'),
                ('Illogical Action', 'delay = làm chậm lại — chỉ số áp suất không thể làm chậm tốc độ di chuyển của bão.'),
                ('Illogical Action', 'dissolve = làm tan biến — chuyên gia dự báo không thể làm tan bão bằng điện báo áp kế.'),
                ('Đáp án đúng', 'detect = phát hiện/nhận biết sớm sự xuất hiện của bão đang tiến vào bờ.'),
            ]
        ),
        q_item(
            'm3_m2l_q5', 5, 'Craft and Structure', 'Words in Context', 'Medium',
            '<p>Flat, parallel walls inside an auditorium can reflect sound sharply back and forth, creating harsh echoes that distract listeners. To avoid this flaw, acoustic architects mount curved or angled timber panels along the balcony sides to ______ sound waves smoothly across every seating row.</p>',
            STEM_WIC,
            ['disperse', 'muffle', 'compress', 'trap'],
            'A',
            'Ngữ cảnh: Tường phẳng song song dội âm mạnh gây tiếng vang khó chịu. Kiến trúc sư lắp tấm gỗ cong/vát góc để "phân tán / tán xạ" sóng âm đều khắp mọi hàng ghế ("smoothly across every seating row") → "disperse" (A).',
            'Cụm "smoothly across every seating row" (đều khắp mọi hàng ghế) loại ngay các từ mang nghĩa bóp nghẹt/giữ kín âm thanh như "muffle" hay "trap".',
            [
                ('Đáp án đúng', 'disperse = phân tán/tản đều ra nhiều hướng — khớp hoàn hảo với "smoothly across every seating row".'),
                ('Opposite Purpose', 'muffle = làm nghẹt/giảm nhỏ âm — phòng hòa nhạc cần phân bổ âm đều tới khán giả chứ không làm nghẹt tiếng.'),
                ('Wrong Meaning', 'compress = nén chặt — không phù hợp với cụm "across every seating row".'),
                ('Opposite Purpose', 'trap = bẫy/giữ chặt lại — ngược với mục tiêu đưa âm thanh lan tỏa đều khắp các hàng ghế.'),
            ]
        ),

        # ------------------------------------------------------------------
        # Q6-Q7: Craft and Structure — Text Structure and Purpose
        # ------------------------------------------------------------------
        q_item(
            'm3_m2l_q6', 6, 'Craft and Structure', 'Text Structure and Purpose', 'Easy',
            '<p>Although wildfire is often viewed purely as a destructive force, California’s giant sequoia groves depend on periodic low-intensity ground fires to reproduce. Flames clear thick mats of fallen needles and shade-casting shrubs from the forest floor, exposing bare mineral soil. At the same time, rising heat dries the sticky resin sealing mature sequoia cones high in the canopy, prompting them to pop open and rain thousands of seeds onto the freshly cleared earth below.</p>',
            'Which choice best states the main purpose of the text?',
            [
                'To criticize forestry agencies for allowing low-intensity fires to burn near California sequoia groves',
                'To compare the height of giant sequoias with that of other western evergreen species',
                'To explain how periodic low-intensity fires help giant sequoia trees reproduce',
                'To argue that fallen pine needles provide the best soil nutrients for sequoia seeds'
            ],
            'C',
            'Câu chủ đề (Câu 1) nêu thẳng mục đích trung tâm: rừng cây cự sam California phụ thuộc vào cháy rừng cường độ thấp định kỳ để sinh sản ("depend on periodic low-intensity ground fires to reproduce"). Câu 2 và 3 lần lượt giải thích hai cơ chế hỗ trợ (dọn lớp thảm mục lộ đất khoáng + sức nóng làm bung nón hạt) → Chọn C.',
            'Khi câu đầu tiên có dạng "Although [quan niệm thường gặp], X depends on Y to Z" và các câu sau giải thích từng bước cơ chế, mục đích chính luôn là "explain how Y helps X do Z".',
            [
                ('Opposite Tone', 'Đoạn văn nêu lợi ích sinh thái thiết yếu của cháy cường độ thấp chứ không chỉ trích việc để cháy kiểm soát.'),
                ('Out of Scope', 'Không hề so sánh chiều cao của cự sam với loài cây thường xanh nào khác.'),
                ('Đáp án đúng', 'Bao quát trọn vẹn câu chủ đề và hai cơ chế giải thích vai trò của lửa trong quá trình sinh sản của cây cự sam.'),
                ('Contradiction', 'Đoạn văn nêu lửa phải DỌN SẠCH lớp lá kim rụng để lộ đất khoáng trần cho hạt nảy mầm.'),
            ]
        ),
        q_item(
            'm3_m2l_q7', 7, 'Craft and Structure', 'Text Structure and Purpose', 'Medium',
            '<p>Novelist and anthropologist Zora Neale Hurston grew up in Eatonville, Florida, one of the earliest self-governing all-Black municipalities in the United States. <u>As a child, she lingered for hours on the front porch of Joe Clarke’s general store, absorbing the lively tall tales, sharp wit, and musical cadence of townspeople swapping stories after work.</u> Those early afternoons on the store porch later became the creative foundation for her acclaimed 1930s fiction and folklore collections, which celebrated the richness of rural Southern Black speech.</p>',
            'Which choice best describes the function of the underlined sentence in the text as a whole?',
            [
                'It explains the economic reasons why Joe Clarke opened a general store in Eatonville.',
                'It contrasts Hurston’s childhood in Florida with her later university training in anthropology.',
                'It suggests that Hurston’s neighbors disapproved of her interest in recording local folktales.',
                'It describes a formative childhood experience that helped inspire the storytelling style of Hurston’s later writing.'
            ],
            'D',
            'Câu trước giới thiệu quê hương Eatonville của Zora Neale Hurston. Câu gạch chân miêu tả trải nghiệm tuổi thơ cụ thể (ngồi hàng giờ trên hiên tiệm tạp hóa Joe Clarke lắng nghe truyện dân gian, lối nói dí dỏm và nhịp điệu lời kể). Câu liền sau nối trực tiếp ("Those early afternoons... later became the creative foundation for her acclaimed 1930s fiction") → Chọn D.',
            'Đọc câu LIỀN SAU câu gạch chân: đại từ "Those early afternoons..." chỉ thẳng mối liên hệ từ trải nghiệm tuổi thơ sang nền tảng sáng tác sau này!',
            [
                ('Out of Scope', 'Không đề cập nguyên nhân kinh tế khiến Joe Clarke mở tiệm tạp hóa.'),
                ('Out of Scope', 'Không có sự so sánh nào với quá trình học đại học ngành nhân chủng học.'),
                ('Fabricated Detail', 'Không hề nhắc rằng hàng xóm phản đối việc Hurston lắng nghe chuyện kể.'),
                ('Đáp án đúng', 'Khớp hoàn hảo cầu nối giữa câu gạch chân (nghe chuyện dân gian trên hiên tiệm) và câu cuối (nền tảng sáng tác của bà thập niên 1930).'),
            ]
        ),

        # ------------------------------------------------------------------
        # Q8: Craft and Structure — Cross-Text Connections
        # ------------------------------------------------------------------
        q_item(
            'm3_m2l_q8', 8, 'Craft and Structure', 'Cross-Text Connections', 'Medium',
            '<p><b>Text 1</b><br/>Forest restoration advocates point out that replanting native broadleaf trees across deforested temperate farmland can deliver meaningful climate cooling. As the young trees grow, they pull carbon dioxide from the atmosphere and lock it into woody trunks and forest soils for decades.</p><p><b>Text 2</b><br/>Climate glaciologist Dr. Henrik Solberg cautions that planting dense evergreen forests across snowy, high-latitude northern tundra can actually produce local warming rather than cooling. Whereas open winter snowfields reflect up to eighty percent of incoming sunlight back into space, dark pine canopies absorb solar radiation, heating the regional air faster than their carbon uptake offsets.</p>',
            'Based on the texts, how does Dr. Henrik Solberg’s point in Text 2 relate to the climate benefit described in Text 1?',
            [
                'Solberg argues that trees never absorb carbon dioxide from the atmosphere in any region of the world.',
                'Solberg identifies a high-latitude geographical exception in which planting dark forests reduces snow reflectivity and causes warming instead of cooling.',
                'Solberg claims that planting broadleaf trees on temperate farmland heats regional air more strongly than planting evergreens on tundra does.',
                'Solberg agrees that snowy northern tundra is the most effective place on Earth to plant new evergreen forests.'
            ],
            'B',
            'Text 1 nêu lợi ích làm mát của trồng rừng trên đất nông nghiệp ôn đới (hấp thụ CO₂). Text 2 (Solberg) KHÔNG phủ nhận khả năng hấp thụ carbon của cây, mà chỉ ra một ngoại lệ địa lý quan trọng ở vùng lãnh nguyên phủ tuyết vĩ độ cao: tán thông sẫm màu làm giảm độ phản xạ của tuyết trắng, hấp thụ nhiệt Mặt Trời gây ấm cục bộ nhiều hơn lượng carbon chúng hấp thụ → Chọn B.',
            'Đối chiếu phạm vi địa lý của hai đoạn: Text 1 ("temperate farmland") vs. Text 2 ("snowy, high-latitude northern tundra") — Text 2 đặt điều kiện ngoại lệ theo vùng khí hậu chứ không phủ nhận tuyệt đối Text 1!',
            [
                ('Too Extreme', 'Solberg vẫn nhắc tới "their carbon uptake" (sự hấp thụ carbon của cây), không hề nói cây không bao giờ hấp thụ CO₂.'),
                ('Đáp án đúng', 'Nắm bắt chuẩn xác mối quan hệ bổ sung ngoại lệ: ở lãnh nguyên tuyết vĩ độ cao, tán cây sẫm màu giảm phản xạ ánh sáng gây ấm lên thay vì làm mát.'),
                ('Reversed Comparison', 'Solberg chỉ cảnh báo việc trồng rừng thường xanh trên lãnh nguyên tuyết, không nói cây lá rộng ở đất ôn đới làm nóng mạnh hơn.'),
                ('Contradiction', 'Ngược hoàn toàn cảnh báo của Solberg — ông khuyến cáo trồng cây trên lãnh nguyên tuyết gây ấm cục bộ.'),
            ]
        ),

        # ------------------------------------------------------------------
        # Q9-Q10: Information and Ideas — Central Ideas and Details
        # ------------------------------------------------------------------
        q_item(
            'm3_m2l_q9', 9, 'Information and Ideas', 'Central Ideas and Details', 'Easy',
            '<p>By the late eighth century, workshops in the Silk Road oasis city of Samarkand had mastered rag-papermaking techniques transmitted westward from China. By pounding recycled linen, flax, and hemp fibers into thin, flexible sheets, Samarkand artisans produced smooth paper that proved far lighter and much less costly to manufacture than parchment prepared from animal skins. This affordable writing material soon spread across Central Asia and the Middle East, fueling a dramatic expansion in libraries and scientific translation.</p>',
            'According to the text, what practical advantage did Samarkand rag paper offer over parchment?',
            [
                'It was completely waterproof during long desert caravan journeys.',
                'It was manufactured exclusively from rare silk threads imported from China.',
                'It lasted longer than stone inscriptions carved on public monuments.',
                'It weighed less and was far less expensive to produce than animal-skin parchment.'
            ],
            'D',
            'Câu hỏi Specific Detail ("According to the text..."): định vị thẳng cụm so sánh trong câu 2 — "proved far lighter and much less costly to manufacture than parchment prepared from animal skins" → Paraphrase trực tiếp ở D ("weighed less and was far less expensive to produce")!',
            'Tìm chính xác từ khóa "parchment" trong đoạn văn và đối chiếu từng tính từ so sánh ("far lighter" + "much less costly").',
            [
                ('Out of Scope', 'Đoạn văn không đề cập khả năng chống thấm nước.'),
                ('Contradiction', 'Giấy Samarkand làm từ sợi vải lanh tái chế, lanh và gai dầu ("recycled linen, flax, and hemp"), KHÔNG phải tơ lụa.'),
                ('Out of Scope', 'Không hề so sánh với bia đá.'),
                ('Đáp án đúng', 'Diễn giải chính xác hai ưu điểm trực tiếp được nêu trong bài: nhẹ hơn và rẻ hơn nhiều khi sản xuất so với giấy da động vật.'),
            ]
        ),
        q_item(
            'm3_m2l_q10', 10, 'Information and Ideas', 'Central Ideas and Details', 'Medium',
            '<p>In classic studies of “change blindness,” cognitive psychologists show viewers a brief film clip in which two people converse across a café table. During a half-second camera cut, crew members swap a bright red scarf for a blue one, remove a large potted plant, or even replace one of the seated actors with a different person wearing similar clothes. Remarkably, more than half of observers fail to spot these glaring alterations—demonstrating that although our visual experience feels panoramic and complete, conscious attention actively encodes only a small fraction of a scene at any given moment.</p>',
            'Which choice best states the main idea of the text?',
            [
                'Film editors intentionally hide background mistakes so that moviegoers will pay closer attention to spoken dialogue.',
                'People can remember the color of a scarf more accurately than the facial features of an unfamiliar actor.',
                'Experiments on change blindness show that human visual attention registers far less detail of a scene at once than people intuitively assume.',
                'Viewers who watch café conversations in person never experience change blindness.'
            ],
            'C',
            'Toàn đoạn lấy thí nghiệm "mù thay đổi" (change blindness) làm minh chứng cho câu kết luận sau dấu gạch ngang: dù trải nghiệm thị giác tạo cảm giác toàn cảnh đầy đủ, sự chú ý có ý thức thực chất chỉ mã hóa một phần nhỏ chi tiết của khung cảnh tại một thời điểm → Chọn C.',
            'Tập trung vào mệnh đề sau từ chốt kết luận ("demonstrating that...") để nắm trúng Main Idea, tránh chọn các chi tiết ví dụ lẻ tẻ (khăn quàng cổ, cảnh quán cà phê).',
            [
                ('Out of Scope', 'Đoạn văn mô tả thí nghiệm tâm lý học nhận thức, không bàn về thủ thuật giấu lỗi của biên tập viên phim.'),
                ('Out of Scope', 'Không so sánh khả năng nhớ màu khăn với nhớ gương mặt diễn viên.'),
                ('Đáp án đúng', 'Tóm gọn chính xác ý nghĩa thí nghiệm mù thay đổi: sự chú ý thị giác thực tế ghi nhận ít chi tiết hơn nhiều so với cảm nhận chủ quan của con người.'),
                ('Out of Scope / Too Extreme', 'Đoạn văn không hề khẳng định quan sát trực tiếp ngoài đời không bao giờ bị mù thay đổi.'),
            ]
        ),

        # ------------------------------------------------------------------
        # Q11-Q12: Information and Ideas — Command of Evidence (Textual)
        # ------------------------------------------------------------------
        q_item(
            'm3_m2l_q11', 11, 'Information and Ideas', 'Command of Evidence (Textual)', 'Medium',
            '<p>Sustainable-agriculture researchers in Japan and Vietnam hypothesized that releasing flocks of foraging ducks into flooded rice paddies can effectively suppress weeds and insect pests without synthetic chemical sprays, because the ducks eat tender weeds and insects while their paddling stirs oxygen into the shallow water.</p>',
            'Which finding, if true, would most directly support the researchers’ hypothesis?',
            [
                'Ducks raised in dry barnyard pens gained weight slightly faster when fed commercial grain pellets than when allowed to forage outdoors.',
                'Flooded rice plots stocked with foraging ducks developed 65 percent fewer weeds and sharply reduced insect damage compared with untreated plots, producing comparable rice yields with zero synthetic pesticides.',
                'Rice farmers in mountainous provinces often construct terraced paddies to slow rainwater runoff along steep slopes.',
                'Flooded rice paddies in coastal deltas tend to receive more seasonal rainfall than upland wheat fields do.'
            ],
            'B',
            'Giả thuyết cần chứng minh: thả vịt vào ruộng lúa ngập nước giúp kiểm soát hiệu quả cỏ dại và sâu hại MÀ KHÔNG CẦN thuốc hóa học. Bằng chứng trực tiếp nhất phải so sánh ruộng có thả vịt với ruộng đối chứng và đo lượng cỏ dại, sâu hại cùng năng suất không dùng thuốc → Đáp án B đáp ứng 100%!',
            'Khóa đúng các biến số trong giả thuyết (foraging ducks in flooded rice paddies → fewer weeds + less insect damage + zero synthetic sprays) để loại ngay các câu lạc đề về chuồng nuôi cạn (A) hay ruộng bậc thang (C).',
            [
                ('Out of Scope', 'So sánh tăng trọng của vịt nuôi nhốt cạn với vịt thả ngoài không kiểm chứng tác động lên cỏ dại và sâu hại ruộng lúa.'),
                ('Đáp án đúng', 'Đo trực tiếp hai kết quả giả thuyết dự đoán (giảm 65% cỏ dại, giảm mạnh sâu hại) trong điều kiện không phun thuốc bảo vệ thực vật mà vẫn giữ vững năng suất.'),
                ('Out of Scope', 'Nói về ruộng bậc thang chống rửa trôi, không liên quan đến mô hình lúa – vịt.'),
                ('Out of Scope', 'So sánh lượng mưa giữa đồng bằng lúa và vùng trồng lúa mì không liên quan đến giả thuyết.'),
            ]
        ),
        q_item(
            'm3_m2l_q12', 12, 'Information and Ideas', 'Command of Evidence (Textual)', 'Easy',
            '<p>In an essay on the 1915 Maine coastal short story “The Lobster Buoy,” a student argues that the young fisherman Daniel feels deep personal pride in repairing his grandfather’s weathered cedar dory by hand rather than replacing it with a modern factory-built boat.</p>',
            'Which quotation from “The Lobster Buoy” most effectively illustrates the student’s claim?',
            [
                '“A dealer down in Portland offered me a gleaming motor-skiff on easy credit, yet as I planed each fresh cedar plank to match my grandfather’s ribs, I felt a quiet satisfaction no showroom hull could ever buy.”',
                '“Every August the harbor fog rolled in before noon, hiding the red bell buoy until the tide turned seaward.”',
                '“My grandfather had sailed as far south as Gloucester in his youth before settling on the rocky cove above the wharf.”',
                '“Before winter storms arrived, the harbor master reminded every boat owner to double the hemp lines along the north pier.”'
            ],
            'A',
            'Checklist từ nhận định: [1] Từ chối mua thuyền xưởng hiện đại + [2] Tự hào/mãn nguyện khi tự tay sửa chiếc thuyền gỗ tuyết tùng của ông nội. Duy nhất A có đủ cả hai chi tiết: đối chiếu chiếc "gleaming motor-skiff" từ đại lý với "quiet satisfaction" khi tự bào từng tấm ván gỗ tuyết tùng khớp khung sườn thuyền của ông nội → Chọn A!',
            'Tìm đúng trích dẫn vừa nhắc thái độ cảm xúc ("quiet satisfaction" = pride) vừa có đối chiếu giữa sửa thuyền gỗ thủ công và mua thuyền xưởng mới.',
            [
                ('Đáp án đúng', 'Khớp trọn vẹn lập luận: từ chối thuyền máy mua ở đại lý và cảm thấy niềm tự hào sâu lắng khi tự tay tu sửa thuyền gỗ của ông nội.'),
                ('Out of Scope', 'Chỉ tả cảnh sương mù bến cảng tháng Tám.'),
                ('Topic Keyword Lure', 'Nhắc tên "my grandfather" nhưng chỉ kể chuyện đi biển thời trẻ của ông, không nhắc việc Daniel sửa thuyền hay từ chối thuyền mới.'),
                ('Out of Scope', 'Chỉ là lời nhắc buộc dây neo trước bão mùa đông.'),
            ]
        ),

        # ------------------------------------------------------------------
        # Q13-Q14: Information and Ideas — Command of Evidence (Quantitative)
        # ------------------------------------------------------------------
        q_item(
            'm3_m2l_q13', 13, 'Information and Ideas', 'Command of Evidence (Quantitative)', 'Easy',
            svg_bar_chart(
                'Sound Absorption Coefficient at 1,000 Hz (0 = No Absorption, 1.0 = Total Absorption)',
                ['0.00', '0.25', '0.50', '0.75', '1.00'],
                [
                    ('Concrete', 0.04, '0.04'),
                    ('Solid Oak', 0.12, '0.12'),
                    ('Velour Curtain', 0.58, '0.58'),
                    ('Acoustic Foam', 0.86, '0.86'),
                ],
                1.0
            ) + '<p>An audio technician outfitting a small podcast recording booth wants to line the interior walls with whichever tested material absorbs the greatest share of sound energy at 1,000 Hz in order to minimize room echo.</p>',
            'Which choice most accurately uses data from the graph to identify the best wall material for the technician’s goal?',
            [
                'Concrete, which exhibits the highest sound absorption coefficient at 0.04.',
                'Solid oak, which absorbs more sound energy at 1,000 Hz (0.12) than velour curtain does (0.58).',
                'Acoustic foam, which achieves the highest sound absorption coefficient at 0.86.',
                'Velour curtain, which achieves a sound absorption coefficient of 0.86 at 1,000 Hz.'
            ],
            'C',
            'Kỹ thuật viên cần chọn vật liệu có hệ số hấp thụ âm thanh (Sound Absorption Coefficient) CAO NHẤT ở tần số 1,000 Hz để giảm vang tối đa. Nhìn biểu đồ: Concrete = 0.04; Solid Oak = 0.12; Velour Curtain = 0.58; Acoustic Foam = 0.86 (cao nhất) → Chọn C!',
            'Kiểm tra kỹ tên cột tương ứng với từng con số để không bị mắc bẫy tráo tên cột (D gán 0.86 cho Velour Curtain) hay đọc ngược giá trị cao nhất/thấp nhất (A).',
            [
                ('Reversed Extremum', '0.04 là hệ số hấp thụ THẤP NHẤT trong 4 vật liệu, không phải cao nhất.'),
                ('False Comparison', '0.12 nhỏ hơn nhiều so với 0.58, không phải lớn hơn.'),
                ('Đáp án đúng', 'Đọc chính xác cột cao nhất: Acoustic Foam đạt 0.86.'),
                ('Swapped Labels', 'Gán nhầm chỉ số 0.86 của Acoustic Foam sang cho Velour Curtain (thực tế chỉ đạt 0.58).'),
            ]
        ),
        q_item(
            'm3_m2l_q14', 14, 'Information and Ideas', 'Command of Evidence (Quantitative)', 'Medium',
            html_table(
                'Annual Wind Speed and Clear-Sky Conditions at Four Candidate Wind-Turbine Sites',
                ['Candidate Site', 'Mean Annual Wind Speed (km/h)', 'Clear-Sky Days per Year'],
                [
                    ['Valley Floor', '11', '195'],
                    ['Coastal Bluff', '28', '142'],
                    ['High Summit', '46', '110'],
                    ['Foothill Ridge', '24', '218'],
                ]
            ) + '<p>Utility engineers selecting a location for a community wind turbine must meet two strict criteria: the site must average at least 20 km/h in annual wind speed to generate steady electricity, and it must record more than 200 clear-sky days per year so winter maintenance crews can avoid frequent icing delays.</p>',
            'Which choice most accurately uses data from the table to identify the site that satisfies both engineering criteria?',
            [
                'High Summit, because it records the strongest mean wind speed at 46 km/h and has 218 clear-sky days per year.',
                'Coastal Bluff, because its mean wind speed of 28 km/h and its 142 clear-sky days per year both exceed the engineers’ thresholds.',
                'Valley Floor, because it averages 195 clear-sky days per year and 11 km/h wind speed.',
                'Foothill Ridge, because it is the only site combining a mean wind speed of at least 20 km/h (24 km/h) with more than 200 clear-sky days per year (218 days).'
            ],
            'D',
            'Kiểm tra lần lượt cả 2 điều kiện bắt buộc: (1) Tốc độ gió ≥ 20 km/h VÀ (2) Số ngày quang mây > 200 ngày/năm.\n- Valley Floor: 11 km/h (Loại), 195 ngày (Loại).\n- Coastal Bluff: 28 km/h (Đạt), 142 ngày (Loại).\n- High Summit: 46 km/h (Đạt), 110 ngày (Loại).\n- Foothill Ridge: 24 km/h (Đạt ≥ 20) VÀ 218 ngày (Đạt > 200) → Duy nhất Foothill Ridge (D) thỏa mãn cả 2 tiêu chí!',
            'Với bảng câu hỏi lọc đa điều kiện (Criterion 1 AND Criterion 2), gạch chéo trực tiếp từng hàng không đạt để chốt duy nhất 1 hàng đạt trọn cả 2 cột.',
            [
                ('Swapped Numbers', 'Gán nhầm 218 ngày quang mây của Foothill Ridge cho High Summit (thực tế High Summit chỉ có 110 ngày quang mây).'),
                ('Threshold Violation', '142 ngày quang mây KHÔNG vượt mức yêu cầu trên 200 ngày/năm.'),
                ('Threshold Violation', 'Valley Floor không đạt cả hai ngưỡng (11 < 20 km/h và 195 < 200 ngày).'),
                ('Đáp án đúng', 'Khớp chính xác 100% cả hai chỉ số của Foothill Ridge (24 km/h và 218 ngày) thỏa mãn đồng thời hai điều kiện.'),
            ]
        ),

        # ------------------------------------------------------------------
        # Q15: Information and Ideas — Inferences
        # ------------------------------------------------------------------
        q_item(
            'm3_m2l_q15', 15, 'Information and Ideas', 'Inferences', 'Medium',
            '<p>In a laboratory study of autobiographical memory, psychologists presented adult participants with everyday cues—either a photograph of a familiar object, its spoken name, or its distinctive scent—and asked them to describe the earliest personal memory each cue brought to mind. Although all three cue types prompted similar total numbers of memories, memories triggered by scents dated significantly earlier in childhood and included richer emotional detail than memories triggered by photographs or spoken words. These results suggest that ______</p>',
            STEM_INF,
            [
                'adults struggle to recall any childhood experiences when presented with photographs or spoken words.',
                'olfactory cues are uniquely effective at unlocking early, emotionally vivid autobiographical memories compared with visual or verbal cues.',
                'human vision and hearing play no meaningful role in storing everyday personal memories.',
                'scent cues trigger a much larger total quantity of memories than photographs or spoken words do.'
            ],
            'B',
            'Tổng hợp dữ kiện bài thí nghiệm: Cả 3 loại tín hiệu (ảnh chụp, lời nói, mùi hương) gợi ra TỔNG SỐ LƯỢNG ký ức tương đương nhau ("similar total numbers"), NHƯNG ký ức do MÙI HƯƠNG kích hoạt lại thuộc giai đoạn thơ ấu sớm hơn đáng kể và giàu chi tiết cảm xúc hơn so với ảnh chụp và từ nói → Suy luận trực tiếp: tín hiệu khứu giác (olfactory cues) đặc biệt hiệu quả trong việc khơi gợi các ký ức tự truyện thời thơ ấu giàu cảm xúc hơn tín hiệu thị giác hay ngôn từ → Chọn B!',
            'Trong bài Inference, loại ngay đáp án trái dữ liệu ("much larger total quantity" ở D trái với "similar total numbers") và các câu cực đoan ("struggle to recall any" ở A, "no meaningful role" ở C).',
            [
                ('Too Extreme / Contradiction', 'Ảnh chụp và lời nói vẫn gợi ra tổng số lượng ký ức tương đương mùi hương, không phải người lớn không nhớ được gì.'),
                ('Đáp án đúng', 'Khái quát chuẩn xác và thận trọng kết quả thí nghiệm: mùi hương vượt trội về độ sớm thời thơ ấu và chiều sâu cảm xúc so với hình ảnh/lời nói.'),
                ('Too Extreme', 'Đoạn văn không hề kết luận thị giác và thính giác "không có vai trò ý nghĩa" trong trí nhớ.'),
                ('Direct Contradiction', 'Văn bản nêu rõ cả ba loại tín hiệu gợi ra "similar total numbers of memories" (tổng số lượng tương đương nhau).'),
            ]
        ),

        # ------------------------------------------------------------------
        # Q16-Q19: Standard English Conventions — Boundaries
        # ------------------------------------------------------------------
        q_item(
            'm3_m2l_q16', 16, 'Standard English Conventions', 'Boundaries', 'Easy',
            '<p>By the third century CE, the Kingdom of Aksum controlled the bustling Red Sea port of ______ Mediterranean merchants sailed there each autumn to exchange olive oil and glass vessels for highland ivory and frankincense.</p>',
            STEM_SEC,
            ['Adulis, and', 'Adulis,', 'Adulis', 'Adulis, however,'],
            'A',
            'Vế 1 là mệnh đề độc lập IC ("By the third century CE, the Kingdom of Aksum controlled the bustling Red Sea port of Adulis"). Vế 2 cũng là IC ("Mediterranean merchants sailed there each autumn..."). Để nối 2 IC chuẩn mực, ta dùng `, + FANBOYS` → `Adulis, and` (A). Loại B (Comma Splice), C (Run-on), D (Comma Splice + sai nghĩa đối lập với "however").',
            'Kiểm tra hai vế trước và sau chỗ trống: IC + IC → cần `. `, `; `, hoặc `, + FANBOYS` (for, and, nor, but, or, yet, so)!',
            [
                ('Đáp án đúng', 'Dấu phẩy kèm liên từ đẳng lập "and" nối chuẩn xác hai mệnh đề độc lập có quan hệ bổ sung thuận chiều.'),
                ('Comma Splice', 'Dấu phẩy đơn không thể nối hai mệnh đề độc lập.'),
                ('Run-On Sentence', 'Thiếu hoàn toàn dấu câu ngăn cách hai mệnh đề độc lập.'),
                ('Comma Splice + False Contrast', 'Vừa sai lỗi Comma Splice với trạng từ "however", vừa sai quan hệ nghĩa vì hai vế không đối lập nhau.'),
            ]
        ),
        q_item(
            'm3_m2l_q17', 17, 'Standard English Conventions', 'Boundaries', 'Easy',
            '<p>When autumn daylight shortens and nighttime temperatures fall near ______ deciduous sugar maples stop producing green chlorophyll, allowing brilliant yellow and orange leaf pigments to become visible.</p>',
            STEM_SEC,
            ['freezing;', 'freezing.', 'freezing:', 'freezing,'],
            'D',
            'Mở đầu câu bằng liên từ phụ thuộc "When" nên toàn bộ vế trái ("When autumn daylight shortens and nighttime temperatures fall near freezing") là Mệnh đề phụ (DC), theo sau là Mệnh đề chính (IC: "deciduous sugar maples stop producing..."). Cấu trúc `DC, IC` BẮT BUỘC nối bằng dấu phẩy đơn → `freezing,` (D). Không bao giờ đặt dấu chấm, chấm phẩy hay hai chấm ngay sau mệnh đề phụ!',
            'Quy tắc nền tảng: Mệnh đề mở đầu bằng `When / Although / Because / If` (DC) đứng trước IC → LUÔN dùng dấu PHẨY ĐƠN (`,`), cấm dùng `.`, `;`, `:`!',
            [
                ('Semicolon After DC', 'Dấu chấm phẩy chỉ dùng giữa 2 IC, không dùng ngay sau mệnh đề phụ "When...".'),
                ('Period After DC (Fragment)', 'Đặt dấu chấm biến mệnh đề phụ "When..." thành câu cụt (Fragment).'),
                ('Colon After DC', 'Dấu hai chấm yêu cầu vế trước phải là một mệnh đề độc lập hoàn chỉnh.'),
                ('Đáp án đúng', 'Dấu phẩy đơn ngăn cách chuẩn xác mệnh đề phụ chỉ thời gian (DC) với mệnh đề chính (IC).'),
            ]
        ),
        q_item(
            'm3_m2l_q18', 18, 'Standard English Conventions', 'Boundaries', 'Medium',
            '<p>Glaciologist Lonnie ______ a pioneer in drilling ice cores from remote tropical mountain glaciers, has recovered frozen climate archives from peaks in Peru, Tanzania, and Tibet.</p>',
            STEM_SEC,
            ['Thompson', 'Thompson,', 'Thompson;', 'Thompson—'],
            'B',
            'Cụm `a pioneer in drilling ice cores from remote tropical mountain glaciers` là đồng vị ngữ không thiết yếu (nonessential appositive) bổ nghĩa cho chủ ngữ `Glaciologist Lonnie Thompson`. Phía sau cụm này đã ĐÓNG bằng dấu phẩy (`glaciers, has recovered`), nên phía trước BẮT BUỘC mở bằng một dấu phẩy tương ứng → `Thompson,` (B)!',
            'Kiểm tra dấu đóng ở cuối cụm bổ ngữ (`...glaciers,`): đóng bằng phẩy thì mở PHẢI bằng phẩy để tạo cặp `..., X, ...`!',
            [
                ('Unpaired Comma', 'Thiếu dấu phẩy mở khiến dấu phẩy phía sau "glaciers," tách trái phép chủ ngữ khỏi động từ chính "has recovered".'),
                ('Đáp án đúng', 'Tạo cặp dấu phẩy cân đối bao trọn cụm đồng vị ngữ giải thích cho Lonnie Thompson.'),
                ('Illegal Semicolon', 'Không dùng dấu chấm phẩy trước một cụm danh từ đồng vị ngữ.'),
                ('Mismatched Punctuation Pair', 'Mở bằng gạch ngang (—) nhưng đóng bằng dấu phẩy (,) là lỗi lệch cặp dấu.'),
            ]
        ),
        q_item(
            'm3_m2l_q19', 19, 'Standard English Conventions', 'Boundaries', 'Medium',
            '<p>A traditional mechanical wristwatch movement relies on three core ______ a coiled mainspring that stores energy, a brass gear train that transmits power, and an escapement that regulates each tick.</p>',
            STEM_SEC,
            ['assemblies;', 'assemblies', 'assemblies:', 'assemblies, and'],
            'C',
            'Vế trái là một mệnh đề độc lập hoàn chỉnh ("A traditional mechanical wristwatch movement relies on three core assemblies"). Vế phải là danh sách liệt kê đích danh 3 cụm linh kiện đó (chỉ là cụm danh từ, không phải IC). Để giới thiệu một danh sách giải thích ngay sau IC hoàn chỉnh, ta PHẢI dùng dấu HAI CHẤM (`:`) → `assemblies:` (C)!',
            'Công thức `IC : danh sách giải thích`: Dấu hai chấm (:) mở đầu danh sách cụm danh từ sau mệnh đề đầy đủ, còn chấm phẩy (;) đòi hỏi vế sau cũng phải là IC!',
            [
                ('Semicolon Before List', 'Vế sau chỉ là danh sách 3 cụm danh từ không có động từ chính (không phải IC), nên không dùng dấu chấm phẩy.'),
                ('Missing Delimiter', 'Không có dấu câu dẫn nhập danh sách giải thích khiến câu dính liền tối nghĩa.'),
                ('Đáp án đúng', 'Dấu hai chấm (:) giới thiệu chuẩn mực danh sách ba bộ phận cốt lõi ngay sau mệnh đề độc lập hoàn chỉnh.'),
                ('Faulty Coordination', 'Thêm ", and" biến danh sách liệt kê 3 bộ phận thành cấu trúc nối sai logic với "three core assemblies".'),
            ]
        ),

        # ------------------------------------------------------------------
        # Q20-Q22: Standard English Conventions — Form, Structure, and Sense
        # ------------------------------------------------------------------
        q_item(
            'm3_m2l_q20', 20, 'Standard English Conventions', 'Form, Structure, and Sense', 'Easy',
            '<p>Although both sides of the brain communicate constantly through the corpus callosum, each hemisphere of the human cerebral cortex ______ specialized aspects of language, attention, and spatial reasoning.</p>',
            STEM_SEC,
            ['coordinate', 'coordinates', 'are coordinating', 'have coordinated'],
            'B',
            'Chủ ngữ của mệnh đề chính là `each hemisphere` (từ `each` + danh từ số ít → CHỦ NGỮ SỐ ÍT, gạch bỏ cụm giới từ "of the human cerebral cortex"). Do đó động từ chia ở ngôi 3 số ít thì hiện tại đơn là `coordinates` (B)! Loại A, C, D vì đều là động từ số nhiều.',
            'Mọi chủ ngữ mở đầu bằng `Each` hoặc `Every` (như `each hemisphere`) LUÔN chia động từ SỐ ÍT!',
            [
                ('Subject-Verb Disagreement', '"coordinate" là động từ số nhiều, không khớp với chủ ngữ số ít "each hemisphere".'),
                ('Đáp án đúng', 'Động từ số ít "coordinates" hòa hợp chính xác với chủ ngữ số ít "each hemisphere".'),
                ('Subject-Verb Disagreement', '"are coordinating" là dạng số nhiều, sai hòa hợp với "each hemisphere".'),
                ('Subject-Verb Disagreement', '"have coordinated" là dạng số nhiều, sai hòa hợp với "each hemisphere".'),
            ]
        ),
        q_item(
            'm3_m2l_q21', 21, 'Standard English Conventions', 'Form, Structure, and Sense', 'Medium',
            '<p>In 1914, poet Robert Frost published his second collection, <i>North of Boston</i>, and quickly ______ wide critical acclaim for capturing the quiet cadences of rural New England speech.</p>',
            STEM_SEC,
            ['wins', 'will win', 'won', 'winning'],
            'C',
            'Mốc thời gian lịch sử rõ ràng "In 1914" đi kèm động từ thứ nhất ở thì quá khứ đơn `published`, nối song song bằng liên từ `and` với động từ thứ hai trong vị ngữ ghép (`published ... and quickly ______`). Do đó chỗ trống BẮT BUỘC chia cùng thì quá khứ đơn → `won` (C)!',
            'Kiểm tra tính song song thì trong vị ngữ ghép (`In [năm quá khứ], Subject V1-ed and V2-ed`): hai hành động nối bằng "and" phải đồng nhất thì quá khứ đơn!',
            [
                ('Verb Tense Shift', '"wins" ở thì hiện tại đơn, lệch thì với mốc "In 1914" và động từ "published".'),
                ('Verb Tense Shift', '"will win" ở thì tương lai đơn, sai hẳn mốc lịch sử năm 1914.'),
                ('Đáp án đúng', 'Quá khứ đơn "won" song song chuẩn xác với "published" dưới mốc thời gian năm 1914.'),
                ('Faulty Parallelism (-ing)', '"winning" là phân từ, phá vỡ cấu trúc động từ chia thì song song với "published".'),
            ]
        ),
        q_item(
            'm3_m2l_q22', 22, 'Standard English Conventions', 'Form, Structure, and Sense', 'Medium',
            '<p>Unlike the single-humped dromedary adapted to hot Arabian deserts, the double-humped Bactrian camel grows a thick winter coat that enables ______ to cross frozen Central Asian mountain passes along the Silk Road.</p>',
            STEM_SEC,
            ['them', 'they', 'its', 'it'],
            'D',
            'Kiểm tra Hòa hợp Đại từ & Cách ngữ pháp (Pronoun Agreement & Case): Chủ ngữ làm tiền ngữ là danh từ SỐ ÍT `the double-humped Bactrian camel` (số ít — nhận biết qua `the ... camel` và động từ số ít `grows`). Sau ngoại động từ `enables`, ta cần đại từ tân ngữ (object pronoun) SỐ ÍT → `it` (D)!',
            'Xác định đúng tiền ngữ (`the double-humped Bactrian camel` = số ít) và vị trí tân ngữ sau động từ `enables [object] to V` → chốt ngay `it`!',
            [
                ('Pronoun Number Disagreement', '"them" là số nhiều, sai hòa hợp với tiền ngữ số ít "the double-humped Bactrian camel".'),
                ('Number & Case Error', '"they" vừa là số nhiều vừa là đại từ chủ ngữ (không đứng làm tân ngữ sau "enables").'),
                ('Wrong Pronoun Case', '"its" là tính từ sở hữu, phải đi kèm danh từ phía sau — không thể dùng làm tân ngữ độc lập trước "to cross".'),
                ('Đáp án đúng', 'Đại từ tân ngữ số ít "it" khớp chuẩn xác cả số lẫn vai trò tân ngữ sau động từ "enables".'),
            ]
        ),

        # ------------------------------------------------------------------
        # Q23-Q25: Expression of Ideas — Transitions
        # ------------------------------------------------------------------
        q_item(
            'm3_m2l_q23', 23, 'Expression of Ideas', 'Transitions', 'Easy',
            '<p>Subsurface drip irrigation delivers water slowly right beside crop roots, slashing daytime evaporation losses by nearly half. ______, keeping the soil surface dry between planting rows discourages unwanted weeds from sprouting.</p>',
            STEM_TRANS,
            ['In addition', 'However', 'Instead', 'Otherwise'],
            'A',
            'Câu 1 nêu lợi ích thứ nhất của tưới nhỏ giọt ngầm (giảm gần một nửa lượng nước bay hơi). Câu 2 bổ sung thêm lợi ích thứ hai cùng chiều (giữ khô mặt đất giữa các hàng cây giúp hạn chế cỏ dại nảy mầm) → Quan hệ Bổ sung cùng chiều → "In addition" (A).',
            'Hai lợi ích cùng hướng của cùng một công nghệ (Benefit #1 + Benefit #2) → Chọn ngay nhóm Addition ("In addition", "Moreover", "Furthermore")!',
            [
                ('Đáp án đúng', 'In addition nối mạch lạc lợi ích thứ hai (giảm cỏ dại) vào ngay sau lợi ích thứ nhất (giảm bay hơi nước).'),
                ('False Contrast', 'However báo hiệu sự đối lập — hai câu đều nêu ưu điểm của tưới nhỏ giọt ngầm.'),
                ('Substitution Trap', 'Instead chỉ sự thay thế khi câu 1 nêu hành động bị loại bỏ/phủ định.'),
                ('Wrong Relationship (Condition)', 'Otherwise (= nếu không thì) không hợp nghĩa giữa hai lợi ích bổ sung cho nhau.'),
            ]
        ),
        q_item(
            'm3_m2l_q24', 24, 'Expression of Ideas', 'Transitions', 'Easy',
            '<p>Fast-moving upper-level jet streams strongly influence commercial airline flight times across North America. ______, an eastbound plane riding a winter tailwind from Seattle to Boston often arrives nearly an hour faster than the westbound return flight.</p>',
            STEM_TRANS,
            ['Nevertheless', 'For example', 'Conversely', 'Therefore'],
            'B',
            'Câu 1 nêu nhận định khái quát (dòng tia trên cao ảnh hưởng mạnh tới thời gian bay thương mại ở Bắc Mỹ). Câu 2 đưa ra một trường hợp minh họa cụ thể (chuyến bay chiều đông Seattle → Boston nhanh hơn gần 1 giờ so với chiều về) → Quan hệ Khái quát → Ví dụ minh họa → "For example" (B).',
            'Nhận diện cặp cấu trúc "General statement (across North America) → Specific case (Seattle to Boston)" → Chọn ngay "For example" hoặc "For instance"!',
            [
                ('False Contrast', 'Nevertheless chỉ sự trái kỳ vọng — chuyến bay Seattle–Boston hoàn toàn minh họa đúng câu 1.'),
                ('Đáp án đúng', 'For example giới thiệu ví dụ tuyến bay Seattle–Boston minh họa trực tiếp cho tác động của dòng tia.'),
                ('False Contrast', 'Conversely dùng để đối nghịch hai vế trái chiều.'),
                ('Wrong Relationship (Cause-Effect)', 'Câu 2 là một ví dụ cụ thể cho nhận định chung ở câu 1, không phải hệ quả nhân quả của câu 1.'),
            ]
        ),
        q_item(
            'm3_m2l_q25', 25, 'Expression of Ideas', 'Transitions', 'Medium',
            '<p>Through room-temperature air, sound waves travel at roughly 343 meters per second. ______, because molecules in liquid water are packed far closer together than gas molecules in air, sound moves more than four times faster underwater.</p>',
            STEM_TRANS,
            ['Similarly', 'For instance', 'However', 'Accordingly'],
            'C',
            'Câu 1 nêu tốc độ âm thanh trong không khí (343 m/s). Câu 2 đối chiếu sang môi trường nước lỏng nơi âm thanh truyền nhanh hơn gấp 4 lần (tốc độ khác biệt mạnh so với không khí) → Quan hệ Đối lập / Tương phản → "However" (C).',
            'Kiểm tra sự tương phản giữa hai môi trường vật lý (air: 343 m/s vs. underwater: more than 4x faster) để loại sạch các từ cùng chiều (Similarly, For instance, Accordingly).',
            [
                ('Opposite Relationship', 'Similarly chỉ sự tương đồng — sai vì tốc độ âm thanh trong nước nhanh gấp hơn 4 lần trong không khí.'),
                ('Wrong Relationship (Example)', 'Âm thanh truyền dưới nước không phải ví dụ cho âm thanh truyền qua không khí.'),
                ('Đáp án đúng', 'However tạo nhịp chuyển tương phản chuẩn xác giữa tốc độ âm thanh trong không khí và trong nước.'),
                ('Wrong Relationship (Cause-Effect)', 'Âm thanh truyền nhanh trong nước là do mật độ phân tử nước, không phải hệ quả của tốc độ 343 m/s trong không khí.'),
            ]
        ),

        # ------------------------------------------------------------------
        # Q26-Q27: Expression of Ideas — Rhetorical Synthesis
        # ------------------------------------------------------------------
        q_item(
            'm3_m2l_q26', 26, 'Expression of Ideas', 'Rhetorical Synthesis', 'Easy',
            '''<p>While researching West African history, a student has taken the following notes:</p>
            <ul>
              <li>Between the fourteenth and sixteenth centuries, Timbuktu became famous across Africa and the Mediterranean as a hub of Islamic scholarship.</li>
              <li>Scholars teaching at the Sankore Mosque and nearby colleges attracted thousands of students to study astronomy, law, poetry, and medicine.</li>
              <li>Local scribes copied and bound manuscripts by hand in Arabic and regional West African languages.</li>
              <li>Families in Timbuktu preserved hundreds of thousands of these historic manuscripts in private libraries for centuries.</li>
            </ul>''',
            'The student wants to emphasize Timbuktu’s historical importance as a major center of learning and scholarship. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
            [
                'Families in Timbuktu stored handwritten manuscripts inside private libraries for many centuries.',
                'Manuscripts in Timbuktu were written in both Arabic and regional West African languages.',
                'Timbuktu lay in West Africa and maintained connections across the Mediterranean between the fourteenth and sixteenth centuries.',
                'From the fourteenth to the sixteenth century, Timbuktu flourished as a renowned center of scholarship where thousands of students studied subjects ranging from astronomy to medicine and scribes produced vast manuscript libraries.'
            ],
            'D',
            'Mục tiêu (Goal): nhấn mạnh tầm vóc lịch sử của Timbuktu như một trung tâm học thuật và tri thức lớn ("major center of learning and scholarship"). Các phương án A, B, C chỉ nhặt từng mảnh chi tiết nhỏ lẻ (lưu trữ gia đình, ngôn ngữ chép tay, vị trí địa lý). Duy nhất D tổng hợp đầy đủ các dẫn chứng mạnh nhất về học thuật (trung tâm học thuật danh tiếng thế kỷ 14–16, hàng nghìn học viên học thiên văn đến y học, kho bản thảo đồ sộ) → Chọn D!',
            'Với mục tiêu "emphasize X’s historical importance as a center of learning", chọn phương án hội tụ đầy đủ quy mô học thuật (students, subjects, scholarship, manuscripts) thay vì các chi tiết vụn.',
            [
                ('Too Narrow', 'Chỉ nhắc việc các gia đình bảo quản bản thảo trong thư viện tư, bỏ qua quy mô đào tạo hàng nghìn học viên và các môn học.'),
                ('Too Narrow', 'Chỉ nêu ngôn ngữ viết trên bản thảo, chưa làm nổi bật vai trò trung tâm học thuật.'),
                ('Wrong Synthesis Goal', 'Chỉ nói vị trí địa lý và mối liên hệ với Địa Trung Hải mà không nhắc tới giáo dục hay học thuật.'),
                ('Đáp án đúng', 'Tổng hợp trọn vẹn các ghi chú mạnh nhất để khắc họa tầm vóc trung tâm học thuật lớn của Timbuktu.'),
            ]
        ),
        q_item(
            'm3_m2l_q27', 27, 'Expression of Ideas', 'Rhetorical Synthesis', 'Medium',
            '''<p>While researching precision mechanical engineering, a student has taken the following notes:</p>
            <ul>
              <li>In 1957, American inventor C. Walton Musser patented the strain-wave gear, often called a harmonic drive.</li>
              <li>Unlike traditional gearboxes that rely on multiple heavy, rigid meshing gears, a strain-wave drive uses a thin, flexible toothed steel cup gently deformed by an elliptical inner cam.</li>
              <li>This elastic meshing design achieves virtually zero mechanical backlash and very high gear reduction inside a compact, lightweight housing.</li>
              <li>Because of its precision and low weight, engineers selected strain-wave drives for the electric wheel hubs of NASA’s Apollo Lunar Roving Vehicle and for modern robotic arms.</li>
            </ul>''',
            'The student wants to explain how the design of a strain-wave gear gives it advantages suited to aerospace and robotics. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
            [
                'By replacing heavy rigid gears with a flexible toothed steel cup driven by an elliptical cam, a strain-wave gear delivers compact, lightweight, virtually backlash-free precision ideal for lunar rovers and robotic arms.',
                'American inventor C. Walton Musser received a patent for the strain-wave gear, also known as a harmonic drive, in 1957.',
                'NASA engineers installed strain-wave drives inside the electric wheel hubs of the Apollo Lunar Roving Vehicle.',
                'Traditional gearboxes rely on multiple heavy, rigid meshing gears rather than on an elliptical inner cam.'
            ],
            'A',
            'Mục tiêu gồm 3 mắt xích nối liền nhau: [1] Thiết kế đặc biệt của hộp số sóng biến dạng (cốc thép răng dẻo + cam elip thay bánh răng cứng nặng) → [2] Ưu điểm kỹ thuật (nhỏ gọn, nhẹ, gần như không có độ rơ) → [3] Phù hợp cho hàng không vũ trụ và robot (xe tự hành Mặt Trăng và cánh tay robot). B, C, D mỗi câu chỉ nêu đúng 1 mẩu thông tin rời rạc. Duy nhất A nối liền mạch cả 3 mắt xích đúng 100% ghi chú → Chọn A!',
            'Nhìn chữ "explain HOW the design ... gives it advantages suited to Y" → Tìm câu theo đúng trục `By [Thiết kế], X delivers [Ưu điểm] ideal for [Ứng dụng Y]`!',
            [
                ('Đáp án đúng', 'Kết nối chặt chẽ cả 3 yếu tố theo đúng Goal: cơ chế cốc thép dẻo + lợi thế nhẹ, gọn, không độ rơ + ứng dụng xe Mặt Trăng & cánh tay robot.'),
                ('Wrong Synthesis Goal', 'Chỉ nêu tên nhà phát minh và năm cấp bằng sáng chế 1957.'),
                ('Incomplete Goal', 'Chỉ nêu ứng dụng trên xe Mặt Trăng mà không hề giải thích thiết kế hay ưu điểm kỹ thuật.'),
                ('Incomplete Goal', 'Chỉ nhắc lại nhược điểm của hộp số truyền thống, không giải thích lợi thế hay ứng dụng của hộp số sóng biến dạng.'),
            ]
        ),
    ]
