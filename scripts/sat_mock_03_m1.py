# -*- coding: utf-8 -*-
"""
Digital SAT Reading & Writing Adaptive Mock Test #3
Module 1 (Routing Module — 27 Questions, Medium & Hard Mix)
IDs: m3_m1_q1 .. m3_m1_q27
"""

from sat_drills_1_1_and_2_1 import q_item
from sat_drills_5_4_to_5_5 import svg_bar_chart, html_table

STEM_WIC = 'Which choice completes the text with the most logical and precise word or phrase?'
STEM_SEC = 'Which choice completes the text so that it conforms to the conventions of Standard English?'
STEM_TRANS = 'Which choice completes the text with the most logical transition?'
STEM_INF = 'Which choice most logically completes the text?'


def get_m1_questions():
    return [
        # ------------------------------------------------------------------
        # Q1-Q5: Craft and Structure — Words in Context
        # ------------------------------------------------------------------
        q_item(
            'm3_m1_q1', 1, 'Craft and Structure', 'Words in Context', 'Medium',
            '<p>Neuroimaging studies of rodents navigating complex mazes show that during deep, slow-wave sleep, hippocampal neurons rapidly fire in the exact sequence recorded during daytime exploration. Researchers conclude that this nocturnal replay ______ fragile newly formed spatial traces into durable long-term memories stored in the neocortex.</p>',
            STEM_WIC,
            ['dissipates', 'consolidates', 'obscures', 'reverses'],
            'B',
            'Ngữ cảnh mô tả hiện tượng tế bào hồi hải mã phát xung lặp lại (nocturnal replay) trong giấc ngủ sâu giúp chuyển đổi dấu vết không gian mới hình thành còn mong manh thành trí nhớ dài hạn bền vững ("fragile newly formed... into durable long-term memories"). Động từ mang nghĩa "củng cố / hợp nhất bền chặt" là "consolidates".',
            'Khóa chặt cấu trúc chuyển trạng thái "fragile newly formed ... into durable long-term memories" để xác định hướng nghĩa tích cực/củng cố trước khi xem 4 lựa chọn.',
            [
                ('Opposite Meaning', 'dissipates = làm tiêu tan/phân tán — ngược hoàn toàn với việc chuyển thành trí nhớ bền vững.'),
                ('Đáp án đúng', 'consolidates = củng cố, hợp nhất thành dạng ổn định lâu dài — thuật ngữ chuẩn xác trong khoa học thần kinh trí nhớ.'),
                ('Opposite Meaning', 'obscures = làm mờ nhạt/che khuất — trái ngược với cơ chế lưu trữ bền vững.'),
                ('Opposite Meaning', 'reverses = đảo ngược — không phù hợp với quá trình lưu giữ ký ức.'),
            ]
        ),
        q_item(
            'm3_m1_q2', 2, 'Craft and Structure', 'Words in Context', 'Medium',
            '<p>Between the fourth and eighth centuries CE, few Chinese silk weavers traveled directly to Persia, and few Mediterranean merchants ventured all the way to Chang’an. Instead, multilingual Sogdian traders settled in oasis towns along the Tarim Basin and served as vital ______, negotiating prices, translating contracts, and relaying luxury textiles across thousands of kilometers.</p>',
            STEM_WIC,
            ['adversaries', 'spectators', 'beneficiaries', 'intermediaries'],
            'D',
            'Câu 1 nhấn mạnh hai đầu tuyến thương mại (thợ dệt lụa Trung Hoa và thương nhân Địa Trung Hải) hiếm khi trực tiếp đi gặp nhau. Câu 2 dùng "Instead" giới thiệu thương nhân Sogdia đứng ở các ốc đảo giữa tuyến để đàm phán giá, dịch hợp đồng và chuyển tiếp hàng hóa → họ đóng vai trò "người trung gian" (intermediaries).',
            'Chú ý cấu trúc "few A traveled directly to B... Instead, C served as..." kèm loạt động từ minh họa (negotiating, translating, relaying) — định nghĩa trực tiếp của "intermediaries".',
            [
                ('Opposite Meaning', 'adversaries = đối thủ/kẻ thù — trái ngược với vai trò kết nối thương mại.'),
                ('Wrong Meaning', 'spectators = khán giả đứng xem thụ động — sai vì thương nhân Sogdia trực tiếp đàm phán và vận chuyển hàng.'),
                ('Wrong Meaning', 'beneficiaries = người thụ hưởng thụ động — không diễn tả đúng vai trò cầu nối thương mại giữa hai bên.'),
                ('Đáp án đúng', 'intermediaries = những người trung gian kết nối, khớp hoàn hảo với bối cảnh cầu nối Con đường Tơ lụa.'),
            ]
        ),
        q_item(
            'm3_m1_q3', 3, 'Craft and Structure', 'Words in Context', 'Hard',
            '<p>Although twentieth-century forestry manuals often portrayed bracket fungi as destructive pathogens that merely ruined marketable timber, long-term studies of old-growth cedar stands reveal that these wood-decay organisms are ______ to forest regeneration: by digesting tough lignin in fallen trunks, they create moist nurse logs where new seedlings take root.</p>',
            STEM_WIC,
            ['indispensable', 'detrimental', 'incidental', 'superfluous'],
            'A',
            'Từ đối lập "Although" đặt quan niệm cũ ("destructive pathogens that merely ruined timber") đối nghịch với phát hiện mới sau dấu hai chấm: nấm phân hủy lignin trong thân cây đổ tạo ra giá thể ẩm ("nurse logs") giúp cây con bén rễ tái sinh rừng → vai trò "không thể thiếu" (indispensable).',
            'Dấu hai chấm (:) phía sau chỗ trống giải thích trực tiếp nghĩa của từ cần điền; kết hợp "Although... destructive" để loại ngay mọi từ tiêu cực hoặc mang nghĩa "thừa thãi".',
            [
                ('Đáp án đúng', 'indispensable = không thể thiếu/thiết yếu, đối lập sắc nét với hình ảnh "kẻ phá hoại" và khớp vế tạo nền cho cây con tái sinh.'),
                ('Opposite Meaning', 'detrimental = có hại — lặp lại quan niệm cũ thay vì đối lập với "Although".'),
                ('Wrong Meaning', 'incidental = phụ thêm/ngẫu nhiên không quan trọng — làm nhẹ sai lệch vai trò thiết yếu của nấm trong tái sinh rừng.'),
                ('Opposite Meaning', 'superfluous = dư thừa không cần thiết — trái ngược hoàn toàn với chức năng tạo giá thể cho cây non.'),
            ]
        ),
        q_item(
            'm3_m1_q4', 4, 'Craft and Structure', 'Words in Context', 'Hard',
            '<p>Unlike steady summer surface melting, which gradually thins the Greenland Ice Sheet over months, the abrupt drainage of a supraglacial lake through a deep fracture can ______ a dramatic surge in glacier flow, lubricating the bedrock beneath and pushing millions of tons of ice rapidly toward the sea.</p>',
            STEM_WIC,
            ['mitigate', 'stabilize', 'precipitate', 'forestall'],
            'C',
            'Phép đối chiếu "Unlike steady... gradually" vs. "abrupt drainage... dramatic surge... pushing rapidly" đòi hỏi một động từ mang nghĩa "kích phát / gây ra đột ngột" → "precipitate" (nghĩa học thuật: gây bùng phát bất ngờ, thường dùng với các hiện tượng đột biến).',
            'Từ học thuật hay thi SAT: "precipitate" (động từ) không chỉ có nghĩa kết tủa hóa học mà còn mang nghĩa "kích phát đột ngột một biến cố/hiện tượng".',
            [
                ('Opposite Meaning', 'mitigate = làm dịu/giảm nhẹ — trái ngược với việc tạo ra đợt tăng tốc dữ dội ("dramatic surge").'),
                ('Opposite Meaning', 'stabilize = làm ổn định — ngược với sự trượt nhanh của dòng băng.'),
                ('Đáp án đúng', 'precipitate = kích phát đột ngột một sự kiện/hiện tượng — khớp tuyệt đối với "abrupt drainage" và "dramatic surge".'),
                ('Opposite Meaning', 'forestall = ngăn chặn trước — hoàn toàn trái nghĩa.'),
            ]
        ),
        q_item(
            'm3_m1_q5', 5, 'Craft and Structure', 'Words in Context', 'Hard',
            '<p>In her 1918 novel <i>My Ántonia</i>, Willa Cather refuses to turn Nebraska’s immigrant homesteaders into sentimental stereotypes of effortless triumph; instead, her narrative maintains an ______ candor about winter blizzards, crushing farm mortgages, and the quiet grief of leaving ancestral homelands behind.</p>',
            STEM_WIC,
            ['ornate', 'unflinching', 'evasive', 'flippant'],
            'B',
            'Cather từ chối tô hồng ("refuses to turn... into sentimental stereotypes of effortless triumph") mà thay vào đó đối diện trực diện với bão tuyết, nợ nần và nỗi buồn xa xứ → tính từ đi với "candor" (sự thẳng thắn) phải mang nghĩa "không né tránh / trực diện kiên định" → "unflinching".',
            'Cụm "refuses to... sentimental... instead... candor about [hardships]" luôn gọi tên các tính từ chỉ sự thẳng thắn không né tránh như "unflinching" hay "unsparing".',
            [
                ('Wrong Meaning', 'ornate = hoa mỹ, cầu kỳ — không khớp với sự mộc mạc thẳng thắn trước gian khổ.'),
                ('Đáp án đúng', 'unflinching = không chùn bước, không né tránh sự thật khắc nghiệt — kết hợp chuẩn xác với "candor".'),
                ('Opposite Meaning', 'evasive = lảng tránh — trái nghĩa trực tiếp với "candor" (sự thẳng thắn).'),
                ('Wrong Tone', 'flippant = cợt nhả, thiếu nghiêm túc — sai hoàn toàn sắc thái tôn trọng nỗi đau của Cather.'),
            ]
        ),

        # ------------------------------------------------------------------
        # Q6-Q7: Craft and Structure — Text Structure and Purpose
        # ------------------------------------------------------------------
        q_item(
            'm3_m1_q6', 6, 'Craft and Structure', 'Text Structure and Purpose', 'Medium',
            '<p>Low-frequency booming resonances—known as standing waves—can muddy audio recordings inside small studios where standard foam panels are too thin to absorb long wavelengths. To counter this distortion, acoustic designers install Helmholtz resonators: sealed wooden cavities pierced by precisely sized narrow necks. When sound waves at a target pitch strike the neck, the plug of air inside oscillates back and forth against the springy air volume within the box, converting troublesome bass energy into harmless microscopic heat through friction.</p>',
            'Which choice best states the main purpose of the text?',
            [
                'To explain an acoustic problem in small recording studios and describe how a specific resonant device resolves it',
                'To argue that foam panels are superior to wooden cavities for absorbing low-frequency sound waves',
                'To trace the historical biography of the physicist who first discovered standing waves',
                'To demonstrate that microscopic friction inside wooden boxes amplifies low-frequency audio recordings'
            ],
            'A',
            'Cấu trúc toàn đoạn gồm 2 phần rõ rệt: Câu 1 nêu vấn đề âm học ở phòng thu nhỏ (sóng đứng tần số thấp mà mút tiêu âm mỏng không hấp thụ được); Câu 2–3 giới thiệu bộ cộng hưởng Helmholtz và giải thích cơ chế vật lý giúp triệt tiêu năng lượng âm trầm gây nhiễu → Chọn A.',
            'Với câu hỏi Main Purpose, luôn tóm gọn động từ hành động chính của toàn đoạn theo trình tự: Problem (standing waves) → Solution + Mechanism (Helmholtz resonators).',
            [
                ('Đáp án đúng', 'Bao quát trọn vẹn cả hai phần của đoạn: vấn đề sóng đứng trong phòng thu nhỏ và cách bộ cộng hưởng Helmholtz xử lý vấn đề đó.'),
                ('Contradiction', 'Đoạn văn nói mút tiêu âm QUÁ MỎNG để hấp thụ sóng dài, không hề nói mút tốt hơn hộp gỗ.'),
                ('Out of Scope', 'Không đề cập tiểu sử lịch sử của nhà vật lý Helmholtz.'),
                ('Reversed Logic', 'Ma sát chuyển hóa năng lượng âm trầm thành nhiệt để TRIỆT TIÊU nhiễu, không phải để khuếch đại bản thu.'),
            ]
        ),
        q_item(
            'm3_m1_q7', 7, 'Craft and Structure', 'Text Structure and Purpose', 'Hard',
            '<p>Constructed without mortar from precisely fitted granite blocks, the towering stone enclosures of Great Zimbabwe impressed early European colonial visitors so deeply that many insisted foreign Phoenician or Arabian builders must have erected them. <u>Subsequent excavations by Gertrude Caton-Thompson and later Zimbabwean archaeologists, however, uncovered continuous layers of indigenous Shona pottery, ironwork, and radiocarbon-dated house floors directly beneath the oldest walls.</u> These stratigraphic records decisively established that Great Zimbabwe was the capital of an African trading kingdom that prospered between the eleventh and fifteenth centuries.</p>',
            'Which choice best describes the function of the underlined sentence in the text as a whole?',
            [
                'It explains the structural engineering technique used to stack granite blocks without mortar.',
                'It summarizes the trade goods exchanged between Great Zimbabwe and Arabian ports.',
                'It presents archaeological evidence that refutes the colonial misconception described in the preceding sentence.',
                'It identifies an unresolved disagreement between Gertrude Caton-Thompson and later Zimbabwean archaeologists.'
            ],
            'C',
            'Câu trước nêu định kiến sai lầm của các nhà thực dân châu Âu (cho rằng người nước ngoài xây dựng Great Zimbabwe). Câu gạch chân mở đầu bằng "however" đưa ra bằng chứng khai quật địa tầng (gốm Shona bản địa, đồ sắt, sàn nhà định tuổi carbon nằm ngay dưới tường cổ nhất) để bác bỏ trực tiếp quan niệm sai đó → Chọn C.',
            'Khi câu gạch chân có tín hiệu "however" ngay sau một quan niệm cũ/sai lầm, chức năng kinh điển là "cung cấp bằng chứng thực nghiệm bác bỏ quan điểm ở câu trước".',
            [
                ('Out of Scope', 'Câu gạch chân không giải thích kỹ thuật xếp đá hoa cương không cần vữa.'),
                ('Out of Scope', 'Không liệt kê mặt hàng giao thương với các cảng Ả Rập.'),
                ('Đáp án đúng', 'Trình bày bằng chứng khảo cổ (gốm Shona, đồ sắt, niên đại carbon) trực tiếp bác bỏ định kiến thực dân ở câu liền trước.'),
                ('Fabricated Conflict', 'Caton-Thompson và các nhà khảo cổ Zimbabwe sau này cùng củng cố một kết luận, không hề bất đồng.'),
            ]
        ),

        # ------------------------------------------------------------------
        # Q8: Craft and Structure — Cross-Text Connections
        # ------------------------------------------------------------------
        q_item(
            'm3_m1_q8', 8, 'Craft and Structure', 'Cross-Text Connections', 'Hard',
            '<p><b>Text 1</b><br/>In the classic McGurk illusion, listeners watch a video of a speaker’s lips forming the syllable “ga” while an audio track plays “ba,” causing most observers to report hearing a fused sound, “da.” Cognitive psychologist Arthur Lin argues that this striking illusion demonstrates a universal, hardwired rule of human speech perception: visual lip movements automatically override conflicting auditory signals.</p><p><b>Text 2</b><br/>Testing speakers across multiple linguistic backgrounds, neuroscientist Keiko Tanabe found that native speakers of tonal languages and extensively trained orchestral musicians experienced the McGurk illusion at far lower rates than monolingual English non-musicians did. Tanabe concludes that the brain does not reflexively prioritize vision over hearing; rather, it flexibly weights each sensory channel according to a listener’s accumulated perceptual experience.</p>',
            'Based on the texts, how would Keiko Tanabe (Text 2) most likely respond to Arthur Lin’s argument (Text 1)?',
            [
                'By asserting that the McGurk illusion never occurs when listeners watch lip movements for “ga” paired with audio for “ba.”',
                'By arguing that visual lip cues are completely ignored by the human brain during everyday conversation.',
                'By agreeing that visual dominance is genetically hardwired, but only in monolingual English speakers.',
                'By contending that visual input does not universally override audio because sensory weighting varies with a listener’s linguistic and auditory experience.'
            ],
            'D',
            'Text 1 (Lin) cho rằng ảo giác McGurk chứng minh một quy luật bẩm sinh phổ quát: thị giác tự động lấn át thính giác. Text 2 (Tanabe) đưa bằng chứng người nói ngôn ngữ thanh điệu và nhạc công ít bị ảo giác hơn nhiều → kết luận não không mặc định ưu tiên thị giác mà điều chỉnh trọng số giác quan linh hoạt theo kinh nghiệm nhận thức → Chọn D.',
            'So sánh trực diện hai câu kết luận: Lin ("universal, hardwired rule... automatically override") ↔ Tanabe ("does not reflexively prioritize... flexibly weights according to experience"). Loại ngay các đáp án cực đoan dùng "never" (A) hoặc "completely ignored" (B).',
            [
                ('Too Extreme', 'Tanabe nói tỷ lệ xảy ra "far lower" (thấp hơn nhiều), KHÔNG nói ảo giác này chưa từng xảy ra ("never occurs").'),
                ('Too Extreme', 'Tanabe khẳng định não cân nhắc linh hoạt cả hai kênh giác quan chứ không hoàn toàn phớt lờ thị giác.'),
                ('Distortion', 'Tanabe bác bỏ tính "hardwired" nói chung và giải thích bằng kinh nghiệm học tập/ngôn ngữ, không nói người nói tiếng Anh bị lập trình di truyền.'),
                ('Đáp án đúng', 'Phản ánh chính xác lập luận của Tanabe: phủ nhận sự áp đảo phổ quát của thị giác và nhấn mạnh sự thay đổi trọng số theo kinh nghiệm ngôn ngữ/thính giác.'),
            ]
        ),

        # ------------------------------------------------------------------
        # Q9-Q10: Information and Ideas — Central Ideas and Details
        # ------------------------------------------------------------------
        q_item(
            'm3_m1_q9', 9, 'Information and Ideas', 'Central Ideas and Details', 'Medium',
            '<p>Agronomists comparing cacao farms across southern Ghana observed that full-sun monoculture plots initially produce slightly more cacao pods per hectare during their first decade than shaded agroforestry plots do. Over a thirty-year cycle, however, plantations intercropped beneath native nitrogen-fixing shade trees retain substantially higher soil moisture, suffer fewer fungal outbreaks, and keep producing healthy harvests during severe dry seasons when exposed full-sun trees decline rapidly.</p>',
            'Which choice best states the main idea of the text?',
            [
                'Full-sun cacao monocultures are incapable of producing marketable pods during their first ten years.',
                'Although full-sun cacao plots yield slightly more at first, shaded agroforestry systems prove more resilient and productive over the long term.',
                'Native Ghanaian shade trees eliminate all fungal plant diseases across West African agriculture.',
                'Ghanaian farmers have completely abandoned full-sun cacao farming in favor of shaded agroforestry.'
            ],
            'B',
            'Cấu trúc "initially... however, over a thirty-year cycle..." cho thấy sự đánh đổi ngắn hạn vs dài hạn: trồng thuần phơi nắng cho năng suất nhỉnh hơn chút ở thập niên đầu, nhưng về dài hạn 30 năm thì nông lâm kết hợp có cây che bóng giữ ẩm tốt hơn, ít nấm bệnh hơn và bền vững hơn qua mùa khô → Chọn B.',
            'Đáp án Main Idea cho đoạn có "however" phải nắm được cả vế nhượng bộ ngắn hạn lẫn kết luận chính về dài hạn, tránh mọi từ cực đoan như "incapable", "all", "completely".',
            [
                ('Contradiction', 'Ngược hoàn toàn với bài: vườn phơi nắng thực tế cho năng suất NHỈNH HƠN trong thập niên đầu.'),
                ('Đáp án đúng', 'Tóm gọn chính xác sự đánh đổi giữa lợi thế năng suất ban đầu của vườn phơi nắng với độ bền bỉ và sản lượng dài hạn của mô hình cây che bóng.'),
                ('Too Extreme', 'Đoạn văn chỉ nói "suffer fewer fungal outbreaks" (ít bùng phát nấm hơn), không nói xóa sổ toàn bộ bệnh nấm ở Tây Phi.'),
                ('Out of Scope / Too Extreme', 'Đoạn văn so sánh kết quả nông học chứ không nói nông dân đã từ bỏ hoàn toàn trồng phơi nắng.'),
            ]
        ),
        q_item(
            'm3_m1_q10', 10, 'Information and Ideas', 'Central Ideas and Details', 'Hard',
            '<p><i>The following text is adapted from a 1916 New England regional story, “The Cider Mill at Dusk.” Two neighboring farmers, Caleb and Hollis, have barely spoken since a dispute over a pasture fence the previous spring.</i><br/>Neither man offered a formal apology when Hollis backed his apple wagon up to Caleb’s timber press on that crisp October afternoon. Yet as the heavy oak screw began to turn and the sweet, sharp scent of crushed Baldwin apples filled the dim shed, they fell naturally into the silent choreography of twenty prior autumns—Hollis shoveling pomace into the burlap cloths while Caleb steadied the straining iron lever—until the old grievance seemed as brittle and weightless as the dry leaves drifting past the doorway.</p>',
            'Based on the text, what helps ease the tension between Caleb and Hollis?',
            [
                'Falling back into the familiar, cooperative rhythm of pressing apples together',
                'Discussing the pasture fence dispute candidly before unloading the wagon',
                'Hiring extra farmhands to operate the heavy oak screw and iron lever',
                'Selling their Baldwin apple harvest jointly at a distant town market'
            ],
            'A',
            'Đọc trực tiếp chi tiết trong văn bản: không ai xin lỗi chính thức ("Neither man offered a formal apology"), nhưng khi máy ép táo quay, hai người tự nhiên hòa vào nhịp phối hợp quen thuộc của 20 mùa thu trước ("fell naturally into the silent choreography of twenty prior autumns") khiến hiềm khích cũ tan biến → Chọn A.',
            'Đọc kỹ câu phủ định mở đầu ("Neither man offered a formal apology") để loại ngay bẫy B ("Discussing... candidly"), rồi bám sát cụm hình ảnh trung tâm ("silent choreography").',
            [
                ('Đáp án đúng', 'Diễn giải chuẩn xác cụm "fell naturally into the silent choreography of twenty prior autumns" — sự phối hợp quen thuộc khi cùng ép táo.'),
                ('Contradiction', 'Đoạn văn khẳng định hai người KHÔNG nói lời xin lỗi chính thức và làm việc trong im lặng ("silent choreography").'),
                ('Out of Scope', 'Chỉ có đúng hai nhân vật Caleb và Hollis trực tiếp vận hành máy ép táo.'),
                ('Out of Scope', 'Không hề nhắc đến việc đi bán táo ở chợ thị trấn xa.'),
            ]
        ),

        # ------------------------------------------------------------------
        # Q11-Q12: Information and Ideas — Command of Evidence (Textual)
        # ------------------------------------------------------------------
        q_item(
            'm3_m1_q11', 11, 'Information and Ideas', 'Command of Evidence (Textual)', 'Hard',
            '<p>Atmospheric chemists studying major explosive volcanic eruptions hypothesized that the resulting multi-year drop in global surface temperatures is caused primarily by stratospheric sulfate aerosol droplets reflecting incoming sunlight back into space, rather than by reductions in lower-atmospheric water vapor.</p>',
            'Which finding, if true, would most directly support the atmospheric chemists’ hypothesis?',
            [
                'Following a large tropical eruption, wind speeds in the upper stratosphere temporarily increased by nearly twenty percent over equatorial oceans.',
                'Surface cooling after major eruptions lasted longer in densely forested regions than in arid continental interiors.',
                'Satellite radiometers recorded a sharp increase in upward-reflected shortwave solar radiation directly above post-eruption sulfate aerosol layers, coinciding with surface cooling even where lower-atmospheric humidity remained constant.',
                'Ice cores from Greenland contain detectable traces of volcanic ash dating to several large eruptions over the past two millennia.'
            ],
            'C',
            'Giả thuyết gồm 2 nhánh rõ ràng: (1) hạ nhiệt bề mặt chủ yếu do hạt sol khí sunfat tầng bình lưu phản xạ bức xạ Mặt Trời ngược ra vũ trụ, (2) chứ KHÔNG phải do giảm hơi nước tầng khí quyển thấp. Đáp án C chứng minh trực diện cả hai vế: vệ tinh đo thấy bức xạ sóng ngắn phản xạ lên trên tăng mạnh đúng tầng sol khí sunfat kèm làm mát bề mặt ngay cả khi độ ẩm tầng thấp không đổi → Chọn C.',
            'Khi giả thuyết có dạng "caused by X rather than Y", bằng chứng mạnh nhất phải vừa đo thấy cơ chế X hoạt động cùng kết quả, vừa loại trừ được biến Y (humidity remained constant).',
            [
                ('Irrelevant Mechanism', 'Tốc độ gió tầng bình lưu tăng không chứng minh cơ chế phản xạ ánh sáng Mặt Trời gây làm mát bề mặt.'),
                ('Off-Target Comparison', 'So sánh thời gian lạnh giữa vùng rừng và vùng khô hạn không kiểm chứng được cơ chế sol khí phản xạ nắng hay vai trò hơi nước.'),
                ('Đáp án đúng', 'Xác nhận trực tiếp cơ chế phản xạ bức xạ Mặt Trời của lớp sol khí sunfat gắn với hạ nhiệt, đồng thời loại trừ yếu tố thay đổi độ ẩm tầng thấp.'),
                ('Background Fact Only', 'Tro núi lửa trong lõi băng chỉ chứng tỏ các vụ phun trào từng xảy ra, không chứng minh cơ chế làm mát.'),
            ]
        ),
        q_item(
            'm3_m1_q12', 12, 'Information and Ideas', 'Command of Evidence (Textual)', 'Medium',
            '<p>In an essay on the 1922 Great Plains novel <i>The Alkali Flat</i>, a literary critic argues that the protagonist, Clara, views the Nebraska prairie with a mixture of reverence for its quiet permanence and unease that its immense scale makes human efforts seem fleeting.</p>',
            'Which quotation from <i>The Alkali Flat</i> most effectively illustrates the critic’s claim?',
            [
                '“By late June the wheat stood waist-high along the section line, promising enough bushels to settle every note at the county bank.”',
                '“All morning the wind rattled the tin chimney pipe until my father gave up reading the almanac and stepped outside to mend the latch.”',
                '“At sunrise the bluestem grass glowed like hammered copper, untouched by a single fence post as far as the horizon curved.”',
                '“Standing beside the sod barn, I felt a solemn wonder at the ancient stillness of the plains, yet I could not shake the chill thought that ten winters of prairie wind would erase our timber house without leaving a mark.”'
            ],
            'D',
            'Checklist 2 vế bắt buộc trong nhận định của nhà phê bình: [1] Lòng kính ngưỡng sự trường tồn tĩnh lặng của thảo nguyên ("reverence for its quiet permanence") + [2] Nỗi bất an vì quy mô mênh mông khiến dấu ấn con người trở nên mong manh ("unease that its scale makes human efforts seem fleeting"). Duy nhất D có đủ cả hai vế ("solemn wonder at the ancient stillness" + "chill thought that ten winters... would erase our timber house without leaving a mark") → Chọn D.',
            'Với dạng trích dẫn văn học chứa "a mixture of X and Y", luôn tách thành 2 ô kiểm tra [X] và [Y] để loại thẳng các trích dẫn chỉ tả cảnh đẹp (C) hoặc chỉ tả đời sống nông trại (A, B).',
            [
                ('Out of Scope', 'Chỉ nói về vụ lúa mì bội thu giúp trả nợ ngân hàng, không có cảm xúc trước sự trường tồn hay nỗi bất an về tính mong manh.'),
                ('Out of Scope', 'Chỉ là một tình tiết sinh hoạt thường ngày sửa chốt cửa.'),
                ('Half-Match Trap', 'Chỉ khắc họa vẻ đẹp bao la của thảo nguyên lúc bình minh, thiếu hẳn nỗi bất an về sự mong manh của nỗ lực con người.'),
                ('Đáp án đúng', 'Hội tụ trọn vẹn cả hai sắc thái cảm xúc: "solemn wonder at the ancient stillness" [1] và "chill thought... erase our timber house without leaving a mark" [2].'),
            ]
        ),

        # ------------------------------------------------------------------
        # Q13-Q14: Information and Ideas — Command of Evidence (Quantitative)
        # ------------------------------------------------------------------
        q_item(
            'm3_m1_q13', 13, 'Information and Ideas', 'Command of Evidence (Quantitative)', 'Medium',
            svg_bar_chart(
                'Mean Pine Seedling Dry Biomass (grams) After 16 Weeks by Soil Inoculation',
                ['0 g', '2 g', '4 g', '6 g', '8 g'],
                [
                    ('Sterile Soil', 1.8, '1.8 g'),
                    ('Saprotrophs', 2.1, '2.1 g'),
                    ('Single Species', 4.2, '4.2 g'),
                    ('Diverse Mix', 6.4, '6.4 g'),
                ],
                8
            ) + '<p>Forest ecologists studying degraded clear-cut soils hypothesized that inoculating young pine seedlings with a diverse mix of native ectomycorrhizal fungi promotes substantially greater biomass accumulation than inoculating them with a single ectomycorrhizal species alone.</p>',
            'Which choice best describes data from the graph that support the ecologists’ hypothesis?',
            [
                'Seedlings grown in sterile control soil reached a mean dry biomass of 1.8 grams, which was slightly lower than the 2.1 grams recorded for seedlings inoculated only with saprotrophic fungi.',
                'Seedlings inoculated with a diverse native mycorrhizal mix reached a mean dry biomass of 6.4 grams, substantially exceeding the 4.2 grams achieved with a single mycorrhizal species.',
                'Seedlings inoculated with a single mycorrhizal species reached a mean dry biomass of 6.4 grams, compared with 4.2 grams for seedlings in the diverse native mix.',
                'All four soil treatments produced pine seedlings with a mean dry biomass greater than 4.0 grams after sixteen weeks.'
            ],
            'B',
            'Giả thuyết so sánh trực tiếp 2 nhóm: hỗn hợp nấm cộng sinh đa dạng bản địa (Diverse Mix = 6.4 g) so với chỉ một loài nấm cộng sinh đơn lẻ (Single Species = 4.2 g). Đáp án B đọc chuẩn xác hai con số (6.4 g vượt trội 4.2 g) và chứng minh thẳng giả thuyết → Chọn B.',
            'Luôn khoanh đúng 2 cột mà giả thuyết đối chiếu (Diverse Mix vs. Single Species) và kiểm tra kỹ xem đáp án có tráo số giữa hai cột (bẫy C) hay không.',
            [
                ('True Data / Wrong Claim', 'Số liệu đúng (1.8 g và 2.1 g), nhưng lại so sánh nhóm đất vô trùng và nấm hoại sinh, hoàn toàn không kiểm chứng giả thuyết về hỗn hợp nấm cộng sinh đa dạng vs đơn loài.'),
                ('Đáp án đúng', 'Khớp chính xác 100% số liệu trên biểu đồ (6.4 g vs. 4.2 g) và chứng minh trực tiếp giả thuyết.'),
                ('Swapped Numbers', 'Đảo ngược hoàn toàn giá trị giữa hai cột (thực tế Single Species là 4.2 g, Diverse Mix là 6.4 g).'),
                ('False Data', 'Sai sự thật với biểu đồ: Sterile Soil (1.8 g) và Saprotrophs (2.1 g) đều dưới 4.0 g.'),
            ]
        ),
        q_item(
            'm3_m1_q14', 14, 'Information and Ideas', 'Command of Evidence (Quantitative)', 'Hard',
            html_table(
                'Daily Rate Drift (Seconds/Day) of Four Marine Chronometer Balance-Wheel Designs by Ambient Temperature',
                ['Balance-Wheel Design', 'At 5°C', 'At 20°C', 'At 35°C'],
                [
                    ['Solid Brass', '+14.2', '+0.4', '−13.8'],
                    ['Solid Steel', '+9.6', '+0.2', '−9.1'],
                    ['Split Bimetallic (Brass-Steel)', '+1.1', '+0.1', '−1.3'],
                    ['Elinvar-Invar Alloy', '+0.3', '0.0', '−0.4'],
                ]
            ) + '<p>A horological engineer argues that nineteenth-century split bimetallic balance wheels dramatically reduced temperature-induced timing error relative to solid single-metal wheels, yet still fell short of the thermal stability later achieved by Elinvar-Invar alloy wheels across both cold and warm extremes.</p>',
            'Which choice best describes data from the table that support the engineer’s argument?',
            [
                'At 20°C, every balance-wheel design listed in the table exhibited a daily drift of at least 1.0 second per day.',
                'Solid steel balance wheels drifted by +9.6 seconds per day at 5°C and −9.1 seconds per day at 35°C, showing larger errors than solid brass wheels did at both temperatures.',
                'At 5°C and 35°C, split bimetallic wheels drifted by +1.1 and −1.3 seconds per day—far less than solid brass or solid steel—yet still more than the +0.3 and −0.4 seconds per day recorded for Elinvar-Invar alloy wheels.',
                'Elinvar-Invar alloy balance wheels showed greater drift at 20°C than split bimetallic balance wheels did at 5°C.'
            ],
            'C',
            'Lập luận cần chứng minh chuỗi so sánh 3 bậc tại hai cực nhiệt (5°C và 35°C): (1) Split bimetallic (+1.1 / −1.3 s/ngày) sai số nhỏ hơn rất nhiều so với Solid Brass (+14.2 / −13.8) và Solid Steel (+9.6 / −9.1), NHƯNG (2) vẫn kém ổn định hơn hợp kim Elinvar-Invar (+0.3 / −0.4). Đáp án C đối chiếu chính xác tuyệt đối mọi con số trong bảng → Chọn C.',
            'Với câu hỏi bảng 3 bậc so sánh (A tốt hơn B, nhưng vẫn kém C), kiểm tra đồng thời độ chính xác từng số liệu lẫn đủ cả 2 vế so sánh.',
            [
                ('False Data', 'Tại 20°C, cả bốn thiết kế đều sai số dưới 0.5 giây/ngày (+0.4, +0.2, +0.1, 0.0), không phải từ 1.0 trở lên.'),
                ('False Comparison', 'Ngược dữ liệu bảng: Solid Steel (±9.6/9.1) có sai số NHỎ HƠN Solid Brass (±14.2/13.8), không phải lớn hơn.'),
                ('Đáp án đúng', 'Khớp 100% số liệu ở cả hai cực 5°C và 35°C và chứng minh trọn vẹn cả hai vế lập luận của kỹ sư.'),
                ('False Data', 'Elinvar-Invar ở 20°C sai số 0.0 giây/ngày, nhỏ hơn mức +1.1 của split bimetallic ở 5°C.'),
            ]
        ),

        # ------------------------------------------------------------------
        # Q15: Information and Ideas — Inferences
        # ------------------------------------------------------------------
        q_item(
            'm3_m1_q15', 15, 'Information and Ideas', 'Inferences', 'Hard',
            '<p>In a three-day memory experiment, neuroscientists trained adult volunteers on Day 1 to memorize a list of thirty paired objects. On Day 2, volunteers in Group A were briefly shown a visual reminder of the Day 1 testing room right before learning a second, competing object list, whereas volunteers in Group B learned the same competing list without seeing any Day 1 reminder. Although both groups mastered the second list equally well, Group A recalled substantially fewer items from the original Day 1 list on Day 3 than Group B did. These results suggest that ______</p>',
            STEM_INF,
            [
                'briefly reactivating an established memory can temporarily make it vulnerable to disruption by newly introduced information.',
                'exposure to familiar visual cues permanently blocks the brain from learning any new competing information.',
                'adults are unable to retain lists of thirty paired objects for longer than forty-eight hours regardless of experimental conditions.',
                'learning a second object list strengthens recall of an earlier list whenever participants receive no visual reminders.'
            ],
            'A',
            'Chuỗi suy luận thực nghiệm: Cả hai nhóm đều học tốt danh sách 2 như nhau, điểm khác biệt duy nhất ở Ngày 2 là Nhóm A nhận tín hiệu gợi nhớ Ngày 1 ngay trước khi học danh sách mới → Kết quả Ngày 3: Nhóm A quên danh sách 1 nhiều hơn hẳn Nhóm B! Suy ra: chính việc tái kích hoạt ngắn ký ức cũ (briefly reactivating) đã tạm thời đưa ký ức đó vào trạng thái dễ bị tổn thương/nhiễu bởi thông tin mới (cơ chế reconsolidation) → Chọn A.',
            'Trong bài Inference thiết kế thí nghiệm đối chứng (Group A vs. Group B), cô lập BIẾN KHÁC BIỆT DUY NHẤT (reminder cue) và nối thẳng nó với KẾT QUẢ KHÁC BIỆT DUY NHẤT (lower recall of Day 1 list).',
            [
                ('Đáp án đúng', 'Suy luận chặt chẽ 100% từ thiết kế thí nghiệm: tín hiệu gợi nhớ làm tái kích hoạt ký ức Ngày 1 khiến nó dễ bị danh sách mới làm nhiễu.'),
                ('Contradiction', 'Đề nói rõ cả hai nhóm đều học danh sách 2 TỐT NHƯ NHAU ("mastered the second list equally well").'),
                ('Too Extreme / Contradiction', 'Nhóm B vẫn nhớ tốt hơn hẳn Nhóm A sau 3 ngày; không hề nói con người không thể nhớ quá 48 giờ.'),
                ('Unsupported Leap', 'Thí nghiệm không so sánh Nhóm B với một nhóm không học danh sách 2, nên không thể kết luận học danh sách 2 "làm mạnh thêm" ký ức danh sách 1.'),
            ]
        ),

        # ------------------------------------------------------------------
        # Q16-Q19: Standard English Conventions — Boundaries
        # ------------------------------------------------------------------
        q_item(
            'm3_m1_q16', 16, 'Standard English Conventions', 'Boundaries', 'Medium',
            '<p>Caravans departing the Sahara salt mines of Taghaza hauled heavy slabs of rock salt southward for nearly two ______ merchants in Timbuktu and Djenné eagerly traded alluvial gold dust for those vital mineral blocks.</p>',
            STEM_SEC,
            ['months,', 'months', 'months, consequently,', 'months, and'],
            'D',
            'Vế 1 là mệnh đề độc lập hoàn chỉnh IC ("Caravans departing... hauled heavy slabs... for nearly two months"). Vế 2 cũng là IC ("merchants in Timbuktu... eagerly traded..."). Để nối 2 IC chuẩn mực, ta có thể dùng `, + FANBOYS` → "months, and" (D). Loại A (Comma Splice), B (Run-on), C (Comma Splice với trạng từ liên kết "consequently").',
            'Nhớ bộ 4 cách nối 2 IC chuẩn Digital SAT: `. ` | `; ` | `, + FANBOYS` | `: ` (khi vế sau giải thích). Trạng từ "consequently" KHÔNG PHẢI FANBOYS!',
            [
                ('Comma Splice', 'Dấu phẩy đơn không thể nối hai mệnh đề độc lập.'),
                ('Run-On Sentence', 'Thiếu hoàn toàn dấu câu ngăn cách hai mệnh đề độc lập.'),
                ('Comma Splice (Conjunctive Adverb)', '"consequently" là trạng từ liên kết, không phải FANBOYS — nối 2 IC bằng ", consequently," là lỗi Comma Splice.'),
                ('Đáp án đúng', 'Dấu phẩy đi kèm liên từ đẳng lập "and" (FANBOYS) nối chuẩn xác hai mệnh đề độc lập.'),
            ]
        ),
        q_item(
            'm3_m1_q17', 17, 'Standard English Conventions', 'Boundaries', 'Medium',
            '<p>Laser Doppler ______ an optical technique that measures minute shifts in the frequency of light reflected off vibrating surfaces—allows mechanical engineers to map jet-turbine blade resonances without attaching physical sensors.</p>',
            STEM_SEC,
            ['vibrometry,', 'vibrometry—', 'vibrometry;', 'vibrometry:'],
            'B',
            'Cụm giải thích xen giữa "an optical technique that measures... vibrating surfaces" được ĐÓNG lại bằng một dấu gạch ngang dài (`—allows`). Theo quy tắc cặp dấu ngăn xen kẽ (Paired Punctuation), dấu MỞ đầu cụm xen giữa này PHẢI đồng bộ là dấu gạch ngang dài (`—`) → Chọn B.',
            'Quy tắc Song sinh Bắt buộc: Cụm bổ ngữ xen giữa câu mở bằng gì phải đóng bằng nấy (`... , X , ...` hoặc `... — X — ...`), cấm tuyệt đối phối trộn phẩy với gạch ngang!',
            [
                ('Mismatched Punctuation Pair', 'Mở bằng dấu phẩy (,) nhưng đóng bằng dấu gạch ngang (—) là lỗi lệch cặp dấu.'),
                ('Đáp án đúng', 'Cặp dấu gạch ngang dài (— ... —) bao gọn cụm đồng vị ngữ giải thích cho chủ ngữ "Laser Doppler vibrometry".'),
                ('Illegal Semicolon in Appositive', 'Dấu chấm phẩy không được dùng để tách chủ ngữ khỏi cụm đồng vị ngữ.'),
                ('Illegal Colon Before Verb', 'Dấu hai chấm không thể đứng ngay sau một danh từ chưa thành mệnh đề độc lập và không khớp với gạch ngang đóng phía sau.'),
            ]
        ),
        q_item(
            'm3_m1_q18', 18, 'Standard English Conventions', 'Boundaries', 'Hard',
            '<p>Dense air cooled over Greenland’s interior ice dome plunges down steep coastal valleys at hurricane ______ these katabatic winds can strip away loose snowpack and expose dark glacial ice within hours.</p>',
            STEM_SEC,
            ['speeds; consequently,', 'speeds, consequently,', 'speeds consequently', 'speeds, consequently'],
            'A',
            'Vế 1 là IC hoàn chỉnh ("Dense air cooled... plunges... at hurricane speeds"). Vế 2 cũng là IC hoàn chỉnh ("these katabatic winds can strip away..."). Khi nối 2 IC bằng trạng từ liên kết "consequently", BẮT BUỘC đặt dấu chấm phẩy (;) trước "consequently" và dấu phẩy (,) ngay sau nó → `speeds; consequently,` (A)!',
            'Công thức vàng cho conjunctive adverbs (however, therefore, consequently, moreover): `IC; adverb, IC` hoặc `IC. Adverb, IC`!',
            [
                ('Đáp án đúng', 'Cấu trúc chuẩn mực `IC; consequently, IC` ngăn cách rõ hai mệnh đề độc lập.'),
                ('Comma Splice', 'Đặt dấu phẩy trước trạng từ liên kết "consequently" giữa 2 IC gây lỗi Comma Splice.'),
                ('Run-On Sentence', 'Thiếu hoàn toàn dấu câu ngăn cách 2 IC và thiếu phẩy sau "consequently".'),
                ('Comma Splice', 'Vẫn là lỗi Comma Splice trước "consequently" và thiếu phẩy ngắt sau trạng từ.'),
            ]
        ),
        q_item(
            'm3_m1_q19', 19, 'Standard English Conventions', 'Boundaries', 'Hard',
            '<p>Seeking to curb topsoil erosion caused by annual plowing, Kansas ______ cofounded the Land Institute in 1976 to breed deep-rooted perennial grain crops modeled on native prairie ecosystems.</p>',
            STEM_SEC,
            ['agronomist, Wes Jackson,', 'agronomist Wes Jackson,', 'agronomist Wes Jackson', 'agronomist, Wes Jackson'],
            'C',
            'Cụm "Kansas agronomist" là chức danh/nghề nghiệp đứng ngay trước tên riêng thiết yếu "Wes Jackson" (chủ ngữ trực tiếp của động từ "cofounded"). Nếu bỏ tên "Wes Jackson" đi, "Kansas agronomist" mất nghĩa xác định → tên riêng là thông tin THIẾT YẾU (essential) nên KHÔNG dùng bất kỳ dấu phẩy nào bao quanh! Hơn nữa, không bao giờ chèn một dấu phẩy đơn giữa chủ ngữ và động từ chính ("cofounded") → Chọn C.',
            'Quy tắc Chức danh + Tên riêng: Không có mạo từ "a/the" phía trước chức danh ngắn (`Kansas agronomist Wes Jackson`) → ZERO dấu phẩy trước và sau tên riêng!',
            [
                ('Unnecessary Commas (Essential Name)', 'Không có mạo từ xác định duy nhất trước "Kansas agronomist", nên tên "Wes Jackson" là thiết yếu — cấm đặt trong cặp dấu phẩy.'),
                ('Subject-Verb Separation Comma', 'Dấu phẩy đơn tách trái phép chủ ngữ "Kansas agronomist Wes Jackson" khỏi động từ chính "cofounded".'),
                ('Đáp án đúng', 'Không chen dấu phẩy nào giữa chức danh, tên riêng thiết yếu và động từ chính "cofounded".'),
                ('Single Comma Split', 'Tách vô lý giữa chức danh "agronomist" và tên riêng "Wes Jackson".'),
            ]
        ),

        # ------------------------------------------------------------------
        # Q20-Q22: Standard English Conventions — Form, Structure, and Sense
        # ------------------------------------------------------------------
        q_item(
            'm3_m1_q20', 20, 'Standard English Conventions', 'Form, Structure, and Sense', 'Medium',
            '<p>The intricate network of neural pathways linking the olfactory bulb directly to the amygdala and hippocampus ______ odors to evoke vivid autobiographical memories faster than visual cues typically do.</p>',
            STEM_SEC,
            ['enables', 'enable', 'have enabled', 'are enabling'],
            'A',
            'Gạch bỏ toàn bộ cụm giới từ và phân từ bẫy số nhiều đứng giữa chủ ngữ và động từ: "of neural pathways linking the olfactory bulb directly to the amygdala and hippocampus". Chủ ngữ lõi duy nhất là danh từ SỐ ÍT "The intricate network" → Động từ chia ngôi thứ 3 số ít thì hiện tại đơn (chân lý sinh học): "enables" (A).',
            'Bẫy Prepositional Phrase kinh điển: Chủ ngữ đứng TRƯỚC giới từ "of" ("The intricate network" = số ít), tuyệt đối không bị đánh lừa bởi danh từ số nhiều "pathways" hay cặp "amygdala and hippocampus"!',
            [
                ('Đáp án đúng', 'Động từ số ít "enables" hòa hợp chính xác với chủ ngữ lõi số ít "The intricate network".'),
                ('Subject-Verb Disagreement', '"enable" là động từ số nhiều — bị lừa bởi danh từ "pathways" trong cụm giới từ.'),
                ('Subject-Verb Disagreement', '"have enabled" là động từ số nhiều, sai hòa hợp với chủ ngữ số ít "network".'),
                ('Subject-Verb Disagreement', '"are enabling" là động từ số nhiều, không khớp với "network".'),
            ]
        ),
        q_item(
            'm3_m1_q21', 21, 'Standard English Conventions', 'Form, Structure, and Sense', 'Hard',
            '<p>Having spent several winters traveling by horseback to transcribe traditional ballads across remote Appalachian communities, ______ in 1917.</p>',
            STEM_SEC,
            [
                'a landmark anthology of mountain folk songs was published by Olive Dame Campbell and Cecil Sharp',
                'the resulting notebooks of Olive Dame Campbell and Cecil Sharp yielded a landmark anthology of folk songs',
                'Appalachian oral traditions gained international scholarly attention through Olive Dame Campbell and Cecil Sharp’s book',
                'Olive Dame Campbell collaborated with Cecil Sharp to publish a landmark anthology of mountain folk songs'
            ],
            'D',
            'Quy tắc Bổ ngữ Mở đầu (Dangling Modifier): Cụm phân từ đầu câu "Having spent several winters traveling by horseback to transcribe traditional ballads..." mô tả hành động của NGƯỜI đi cưỡi ngựa ghi chép dân ca. Do đó danh từ đứng NGAY SAU dấu phẩy BẮT BUỘC phải là con người thực hiện hành động đó ("Olive Dame Campbell") → Chỉ có D thỏa mãn!',
            'Mọi cụm phân từ mở đầu (`Having spent...`, `Walking through...`, `Inspired by...`) PHẢI khớp tuyệt đối với CHỦ NGỮ ĐỨNG NGAY SAU DẤU PHẨY!',
            [
                ('Dangling Modifier', 'Một tuyển tập sách ("a landmark anthology") không thể cưỡi ngựa đi qua các mùa đông để chép nhạc.'),
                ('Dangling Modifier', 'Những cuốn sổ tay ("the resulting notebooks") không phải chủ thể cưỡi ngựa ghi chép dân ca.'),
                ('Dangling Modifier', 'Truyền thống truyền miệng ("Appalachian oral traditions") không thể tự đi cưỡi ngựa ghi chép.'),
                ('Đáp án đúng', 'Đặt đúng chủ thể "Olive Dame Campbell" ngay sau dấu phẩy, xóa bỏ hoàn toàn lỗi bổ ngữ lơ lửng.'),
            ]
        ),
        q_item(
            'm3_m1_q22', 22, 'Standard English Conventions', 'Form, Structure, and Sense', 'Medium',
            '<p>By sealing microscopic bubbles of ancient air inside successive layers of compacted Antarctic snow, deep polar ice sheets ______ scientists with a continuous atmospheric archive spanning roughly 800,000 years.</p>',
            STEM_SEC,
            ['providing', 'to provide', 'provide', 'having provided'],
            'C',
            'Kiểm tra Động từ chính (Finite Verb): Chủ ngữ của mệnh đề chính là danh từ số nhiều "deep polar ice sheets". Sau chỗ trống không hề có động từ chia thì nào khác. Do đó chỗ trống BẮT BUỘC phải điền một động từ chia thì (finite verb) ở thì hiện tại đơn số nhiều để tạo thành câu hoàn chỉnh → "provide" (C). Các đáp án A, B, D đều là dạng phi ngôi (non-finite) gây lỗi thiếu vị ngữ (Fragment).',
            'Mọi mệnh đề độc lập bắt buộc phải có ít nhất MỘT động từ chia thì (finite verb); `V-ing`, `to V`, và `having V-ed` không bao giờ làm động từ chính được!',
            [
                ('Sentence Fragment (-ing)', '"providing" là hiện tại phân từ, không thể làm động từ chính cho chủ ngữ "deep polar ice sheets".'),
                ('Sentence Fragment (Infinitive)', '"to provide" là động từ nguyên mẫu, khiến cả câu thiếu động từ chính.'),
                ('Đáp án đúng', 'Động từ chia thì số nhiều "provide" hoàn thiện vị ngữ cho chủ ngữ "deep polar ice sheets".'),
                ('Sentence Fragment (Participle)', '"having provided" là cụm phân từ hoàn thành, không thể làm động từ chính.'),
            ]
        ),

        # ------------------------------------------------------------------
        # Q23-Q25: Expression of Ideas — Transitions
        # ------------------------------------------------------------------
        q_item(
            'm3_m1_q23', 23, 'Expression of Ideas', 'Transitions', 'Medium',
            '<p>Indian Ocean trading vessels sailing between East Africa and western India could count on steady monsoon winds that reversed direction predictably each season. ______, overland caravans crossing the Taklamakan Desert along the northern Silk Road confronted sudden sandstorms, extreme temperature swings, and erratic oasis water supplies.</p>',
            STEM_TRANS,
            ['Likewise', 'By contrast', 'Therefore', 'For example'],
            'B',
            'Câu 1 nói về sự ổn định, dễ dự đoán của gió mùa trên tuyến hàng hải Ấn Độ Dương. Câu 2 đối chiếu với tuyến đường bộ qua sa mạc Taklamakan đầy bão cát bất ngờ và nguồn nước thất thường → Quan hệ đối chiếu 2 đối tượng trái ngược nhau → "By contrast" (B).',
            'Khi hai câu mô tả hai đối tượng song song (Indian Ocean vessels vs. Taklamakan caravans) mang đặc tính ngược chiều (predictable vs. erratic/sudden), chọn ngay "By contrast".',
            [
                ('Opposite Relationship', 'Likewise chỉ sự tương đồng — trái ngược với tính chất đối nghịch giữa ổn định và thất thường.'),
                ('Đáp án đúng', 'By contrast đối chiếu chuẩn xác hai tuyến thương mại biển và sa mạc với điều kiện tự nhiên trái ngược.'),
                ('Wrong Relationship (Cause-Effect)', 'Bão cát ở sa mạc Taklamakan không phải là hệ quả của gió mùa trên Ấn Độ Dương.'),
                ('Wrong Relationship (Example)', 'Đoàn lạc đà trên sa mạc không phải ví dụ minh họa cho tàu buôn trên Ấn Độ Dương.'),
            ]
        ),
        q_item(
            'm3_m1_q24', 24, 'Expression of Ideas', 'Transitions', 'Medium',
            '<p>Sowing winter cereal rye immediately after the autumn maize harvest covers bare farmland with a dense mat of living roots throughout the cold months. ______, spring snowmelt washes far less topsoil and dissolved phosphorus into nearby streams and watersheds.</p>',
            STEM_TRANS,
            ['Nevertheless', 'Conversely', 'As a result', 'Meanwhile'],
            'C',
            'Câu 1 nêu nguyên nhân/biện pháp: gieo lúa mạch đen vụ đông tạo lớp rễ dày che phủ đất trống suốt mùa lạnh. Câu 2 nêu hệ quả trực tiếp: nước tuyết tan mùa xuân cuốn trôi ít đất mặt và phốt pho hơn hẳn → Quan hệ Nhân – Quả → "As a result" (C).',
            'Kiểm tra mũi tên logic: [Rễ cây che phủ đất trống] → [Ít xói mòn đất và rửa trôi phốt pho vào mùa xuân] = Nhân – Quả trực tiếp!',
            [
                ('False Contrast', 'Nevertheless dùng cho kết quả trái kỳ vọng — giảm xói mòn là kết quả hoàn toàn hợp logic.'),
                ('False Contrast', 'Conversely dùng để đảo chiều đối lập giữa hai đối tượng.'),
                ('Đáp án đúng', 'As a result biểu thị chính xác hệ quả trực tiếp của việc gieo cây che phủ vụ đông.'),
                ('Weak Temporal Link', 'Meanwhile chỉ hai sự việc xảy ra đồng thời, bỏ lỡ mối quan hệ nhân – quả giữa gieo rễ mùa đông và giảm xói mòn mùa xuân.'),
            ]
        ),
        q_item(
            'm3_m1_q25', 25, 'Expression of Ideas', 'Transitions', 'Hard',
            '<p>For decades, optical interferometers capable of measuring vibrations smaller than an atomic nucleus required multi-ton granite tables floated on compressed-air pistons to block floor tremors. ______, mechanical engineers in 2023 fabricated a palm-sized silicon isolation stage that achieved comparable stability on an ordinary laboratory workbench.</p>',
            STEM_TRANS,
            ['Consequently', 'Similarly', 'In addition', 'Nonetheless'],
            'D',
            'Câu 1 nêu ràng buộc khổng lồ suốt nhiều thập kỷ (phải dùng bàn đá granite nặng nhiều tấn đệm khí nén mới chống rung được). Câu 2 nêu bước đột phá TRÁI KỲ VỌNG (kỹ sư năm 2023 tạo được bệ cách ly bằng silicon nhỏ bằng lòng bàn tay đạt độ ổn định tương đương ngay trên bàn thí nghiệm thường) → Quan hệ Nhượng bộ / Đối lập → "Nonetheless" (D).',
            'Dùng mẹo gom nhóm: A (Nhân quả), B (Tương đồng), C (Bổ sung) đều đi cùng chiều với câu 1; duy nhất D ("Nonetheless") rẽ ngược hướng để giới thiệu đột phá thu nhỏ vượt ngoài chuẩn cũ!',
            [
                ('Wrong Relationship (Cause-Effect)', 'Bệ silicon nhỏ gọn không phải là kết quả trực tiếp sinh ra từ việc cần bàn đá granite nhiều tấn.'),
                ('Opposite Relationship', 'Similarly chỉ sự giống nhau, sai vì bệ lòng bàn tay tương phản mạnh với bàn granite nhiều tấn.'),
                ('Wrong Relationship (Addition)', 'In addition bỏ qua sự tương phản rõ rệt giữa yêu cầu cồng kềnh cũ và bước đột phá siêu nhỏ mới.'),
                ('Đáp án đúng', 'Nonetheless tạo nhịp chuyển đối lập sắc bén giữa hạn chế kích thước truyền thống và thành tựu kỹ thuật năm 2023.'),
            ]
        ),

        # ------------------------------------------------------------------
        # Q26-Q27: Expression of Ideas — Rhetorical Synthesis
        # ------------------------------------------------------------------
        q_item(
            'm3_m1_q26', 26, 'Expression of Ideas', 'Rhetorical Synthesis', 'Medium',
            '''<p>While researching medieval East African trade, a student has taken the following notes:</p>
            <ul>
              <li>Kilwa Kisiwani was a thriving Swahili Coast island port in present-day Tanzania between the eleventh and fifteenth centuries.</li>
              <li>Gold mined in the southern African interior traveled through the coastal outpost of Sofala to Kilwa Kisiwani’s warehouses.</li>
              <li>Kilwa’s sultans minted their own inscribed copper coins and constructed grand coral-stone buildings, including the Great Mosque.</li>
              <li>Merchants at Kilwa exchanged African gold and ivory for Chinese celadon porcelain, Persian glazed bowls, and Indian cotton textiles.</li>
            </ul>''',
            'The student wants to emphasize Kilwa Kisiwani’s role as a commercial hub linking inland African resources with wider Indian Ocean trade. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
            [
                'Operating as a major Swahili Coast hub, Kilwa Kisiwani funneled gold and ivory from the African interior into Indian Ocean markets, exchanging them for Chinese porcelain, Persian pottery, and Indian textiles.',
                'Between the eleventh and fifteenth centuries, the sultans of Kilwa Kisiwani minted inscribed copper coins and built the coral-stone Great Mosque on an island in present-day Tanzania.',
                'Kilwa Kisiwani was located on an island off the coast of present-day Tanzania and featured monumental architecture crafted from coral stone.',
                'Merchants traveling to Sofala relied on copper coins minted by the sultans of Kilwa Kisiwani during the medieval period.'
            ],
            'A',
            'Mục tiêu đề bài (Goal): nhấn mạnh vai trò trung tâm thương mại kết nối [1] tài nguyên nội địa châu Phi (African interior gold & ivory) với [2] mạng lưới thương mại Ấn Độ Dương rộng lớn (Chinese porcelain, Persian pottery, Indian textiles). Duy nhất A ghép chuẩn xác cả hai đầu kết nối từ ghi chú → Chọn A.',
            'Đọc câu hỏi Goal trước rồi mới soi 4 đáp án: loại mọi phương án chỉ nói về tiền xu/kiến trúc đá san hô (B, C) hoặc suy diễn sai ghi chú (D).',
            [
                ('Đáp án đúng', 'Khớp 100% mục tiêu: làm nổi bật vai trò trung tâm kết nối vàng/ngà nội địa châu Phi với gốm Trung Hoa, Ba Tư và vải Ấn Độ trên Ấn Độ Dương.'),
                ('Wrong Synthesis Goal', 'Chỉ tập trung vào việc đúc tiền đồng và xây Đại Thánh đường bằng đá san hô, bỏ qua kết nối thương mại nội địa – Ấn Độ Dương.'),
                ('Wrong Synthesis Goal', 'Chỉ nêu vị trí địa lý và vật liệu kiến trúc.'),
                ('Unsupported Inference', 'Ghi chú không hề nói thương nhân tới Sofala phụ thuộc vào tiền đồng của Kilwa.'),
            ]
        ),
        q_item(
            'm3_m1_q27', 27, 'Expression of Ideas', 'Rhetorical Synthesis', 'Hard',
            '''<p>While researching atmospheric chemistry, a student has taken the following notes:</p>
            <ul>
              <li>During the dark Antarctic winter, stratospheric temperatures plunge below −78°C, allowing polar stratospheric clouds (PSCs) to form.</li>
              <li>Chemical reactions on the icy surfaces of PSC particles convert harmless chlorine reservoirs into unstable chlorine gas (Cl₂).</li>
              <li>When sunlight returns to Antarctica in early spring, ultraviolet rays rapidly split Cl₂ molecules into highly reactive chlorine atoms.</li>
              <li>Each reactive chlorine atom can destroy thousands of stratospheric ozone molecules before becoming inactive again.</li>
            </ul>''',
            'The student wants to explain the sequence of steps that triggers severe Antarctic ozone depletion each spring. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
            [
                'Because stratospheric temperatures drop below −78°C during the dark Antarctic winter, polar stratospheric clouds form high above the continent.',
                'During the frigid Antarctic winter, polar stratospheric clouds convert inert chlorine reservoirs into unstable Cl₂ gas, which spring ultraviolet sunlight then splits into reactive chlorine atoms that rapidly break down ozone.',
                'A single reactive chlorine atom in the stratosphere can destroy thousands of ozone molecules before returning to an inactive chemical state.',
                'When ultraviolet rays return to Antarctica each spring, they cause stratospheric temperatures to plunge below −78°C and create polar stratospheric clouds.'
            ],
            'B',
            'Mục tiêu: giải thích CHUỖI CÁC BƯỚC (sequence of steps) kích hoạt sự suy giảm tầng ozone Nam Cực vào mỗi mùa xuân: [Bước 1: Đông cực lạnh tạo mây PSC] → [Bước 2: PSC chuyển kho clo trơ thành Cl₂ kém bền] → [Bước 3: Nắng cực tím mùa xuân tách Cl₂ thành nguyên tử clo hoạt tính] → [Bước 4: Phá hủy ozone]. A và C chỉ nêu 1 mảnh lẻ; D đảo lộn hoàn toàn nhân quả/thời gian (Fact Swap!). Duy nhất B nối đủ trọn chuỗi tiến trình chính xác 100% → Chọn B.',
            'Với mục tiêu "explain the sequence of steps", hãy chọn phương án nối liền mạch từ bước khởi phát đến kết quả cuối cùng, đồng thời cảnh giác bẫy đảo ngược nguyên nhân – kết quả như D!',
            [
                ('Incomplete Sequence', 'Chỉ mới nêu bước đầu tiên (hình thành mây PSC mùa đông), chưa hề giải thích phản ứng hóa học và quá trình phá hủy ozone mùa xuân.'),
                ('Đáp án đúng', 'Trình bày mạch lạc, chính xác 100% chuỗi 4 bước từ mùa đông lạnh tạo PSC đến tia cực tím mùa xuân tách Cl₂ phá hủy ozone.'),
                ('Incomplete Sequence', 'Chỉ nêu hệ quả cuối cùng của một nguyên tử clo mà thiếu toàn bộ chuỗi điều kiện mùa đông – mùa xuân tạo ra nó.'),
                ('Fact Swap / Reversed Sequence', 'Đảo ngược sai sự thật: nhiệt độ xuống dưới −78°C xảy ra trong MÙA ĐÔNG TỐI trước khi ánh nắng mùa xuân quay lại.'),
            ]
        ),
    ]
