# -*- coding: utf-8 -*-
"""
Full-Length Adaptive Mock Test #7 — Module 2 HARD Route (27 Qs, Hard & Elite 750+, 32 min)
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
        # --- Q1-Q5: Craft and Structure — Words in Context (Hard / Elite 750+) ---
        q_item(
            'm7_m2h_q1', 1, 'Craft and Structure', 'Words in Context', 'Elite (750+)',
            '<p>Because cool dark starspots on red-dwarf host stars naturally contain water vapor molecules, starlight passing across a spotted stellar hemisphere can mimic a planetary absorption signature and ______ spectroscopists attempting to verify whether a rocky exoplanet actually possesses an atmosphere of its own.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            ['corroborate', 'ameliorate', 'confound', 'expunge'],
            'C',
            'Cause-Effect Clue: vết đen sao (starspots) chứa sẵn hơi nước → tạo tín hiệu giả y hệt khí quyển hành tinh → LÀM BỐI RỐI / GÂY NHIỄU LOẠN ĐÁNH LẠC HƯỚNG các nhà quang phổ học → "confound" (C)!',
            'Nhận diện cặp động từ học thuật 750+: "mimic a signature" (giả mạo tín hiệu) dẫn thẳng tới "confound" (gây nhầm lẫn, làm bối rối phép đo).',
            [
                ('Opposite Meaning', 'corroborate = chứng thực củng cố — trái ngược hoàn toàn với việc giả mạo tín hiệu làm sai lệch xác minh.'),
                ('Wrong Meaning', 'ameliorate = cải thiện làm dịu bớt tình trạng xấu — sai ngữ cảnh.'),
                ('Đáp án đúng', 'confound = gây bối rối, làm rối tung khả năng phân biệt tín hiệu thật – giả của nhà khoa học.'),
                ('Degree / Collocation Error', 'expunge = xóa sổ hoàn toàn khỏi hồ sơ — không dùng với tân ngữ con người ("spectroscopists").'),
            ]
        ),
        q_item(
            'm7_m2h_q2', 2, 'Craft and Structure', 'Words in Context', 'Elite (750+)',
            '<p>High-resolution multispectral imaging of early nineteenth-century Edo woodblock prints has ______ art historians of the long-standing assumption that workshops kept botanical dyes strictly separate from mineral pigments, revealing deliberate blends of organic turmeric yellow and mineral arsenic sulfide in vibrant foliage layers.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            ['disabused', 'convinced', 'divested', 'exonerated'],
            'A',
            'Contrast + Syntax Clue: "has ______ art historians of the long-standing assumption that [X], revealing [opposite of X]" → GIẢI THOÁT KHỎI NGỘ NHẬN / PHÁ BỎ GIẢ ĐỊNH SAI LẦM → Cấu trúc kinh điển 750+: **"disabuse someone of a misconception/assumption"** → Chọn A!',
            'Ghi nhớ cụm vàng 750+: "disabuse [person] of [false belief]" = giúp ai đó nhận ra giả định lâu nay là sai lầm!',
            [
                ('Đáp án đúng', 'disabused (of an assumption) = phá bỏ ngộ nhận lâu nay khi bằng chứng quang phổ cho thấy nghệ nhân có pha trộn phẩm thực vật và khoáng.'),
                ('Opposite Meaning', 'convinced = thuyết phục tin vào giả định cũ — trái ngược hoàn toàn với bằng chứng phản bác phía sau.'),
                ('Collocation Mismatch', 'divested = tước bỏ tài sản, quyền lợi hoặc cổ phần — không dùng để phá bỏ giả định học thuật.'),
                ('Wrong Context', 'exonerated = minh oan khỏi tội lỗi/trách nhiệm — không phù hợp với "assumption".'),
            ]
        ),
        q_item(
            'm7_m2h_q3', 3, 'Craft and Structure', 'Words in Context', 'Elite (750+)',
            '<p>Early theoretical models posited that Saramaccan, a maroon creole language of Suriname, crystallized entirely within a single generation of contact; recently cataloged eighteenth-century colonial court transcripts, however, ______ that sweeping timeline, documenting a protracted multilingual transition spanning several decades.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            ['vindicate', 'replicate', 'obliterate', 'qualify'],
            'D',
            'Nuance & Degree Clue 750+: Giả thuyết cũ nói tiếng Saramaccan định hình *hoàn toàn trong đúng 1 thế hệ* ("crystallized entirely within a single generation"); hồ sơ mới cho thấy thực tế là quá trình chuyển tiếp kéo dài vài thập kỷ → KHÔNG xóa sổ toàn bộ học thuyết hình thành creole, mà ĐIỀU CHỈNH / GIỚI HẠN LẠI ("temper / moderate") khung thời gian khái quát quá mức đó → Nghĩa thứ cấp học thuật của **"qualify"** = limit / modify a sweeping claim → Chọn D!',
            'Bẫy 750+ kinh điển: "qualify" trong văn học thuật SAT nghĩa là "hạn định, tiết chế lại một tuyên bố quá khái quát" — chính xác hơn nhiều so với "obliterate" (xóa sổ sạch)!',
            [
                ('Opposite Meaning', 'vindicate = chứng minh hoàn toàn đúng — trái ngược sau "however".'),
                ('Wrong Meaning', 'replicate = sao chép lặp lại — không hợp ngữ cảnh hồ sơ tòa án đối chiếu mốc thời gian.'),
                ('Degree Too Strong', 'obliterate = tiêu diệt, xóa sạch không còn dấu vết — quá cực đoan vì hồ sơ chỉ điều chỉnh tốc độ kéo dài vài thập kỷ thay vì bác bỏ toàn bộ quá trình hình thành ngôn ngữ.'),
                ('Đáp án đúng', 'qualify (nghĩa thứ cấp: điều chỉnh, giới hạn mức độ khái quát của tuyên bố) khớp tuyệt đối với "that sweeping timeline".'),
            ]
        ),
        q_item(
            'm7_m2h_q4', 4, 'Craft and Structure', 'Words in Context', 'Elite (750+)',
            '<p>Rather than retreating into an ______ musical orthodoxy that policed strict borders between folk idioms and concert traditions, 1930s Harlem symphonic arrangers enthusiastically fused stride-piano syncopation, Baptist choir harmonies, and impressionist woodwind voicings into a cosmopolitan sound.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            ['eclectic', 'insular', 'effervescent', 'ephemeral'],
            'B',
            'Contrast + Restatement Clue: "Rather than retreating into an ______ musical orthodoxy that policed strict borders..." đối lập hoàn toàn với "enthusiastically fused... into a cosmopolitan sound" → CỤC BỘ, KHÉP KÍN, CÔ LẬP KHÔNG GIAO LƯU → "insular" (B)!',
            'Cụm "policed strict borders" (canh giữ ranh giới cứng nhắc) + đối lập "cosmopolitan" (đa văn hóa rộng mở) định nghĩa chuẩn 100% tính từ "insular"!',
            [
                ('Opposite Meaning', 'eclectic = chiết trung, kết hợp đa nguồn — đây chính là phong cách của các nhà phối khí Harlem ở vế sau, trái với vế "Rather than".'),
                ('Đáp án đúng', 'insular = khép kín, hẹp hòi cục bộ — khớp hoàn toàn với việc dựng rào chắn giữa truyền thống dân gian và hàn lâm.'),
                ('Wrong Meaning', 'effervescent = sôi nổi sủi bọt đầy sức sống — sai nghĩa đối lập với "orthodoxy".'),
                ('Wrong Meaning', 'ephemeral = ngắn ngủi chóng tàn — không phản ánh tính khép kín ranh giới.'),
            ]
        ),
        q_item(
            'm7_m2h_q5', 5, 'Craft and Structure', 'Words in Context', 'Elite (750+)',
            '<p>When glacial erratic boulders have been intermittently shielded by deep winter snowpacks or rolled downhill by freeze-thaw cycles, cosmogenic beryllium-10 exposure dates derived from their quartz grains become ______, leaving geomorphologists unable to resolve whether a moraine formed during the Younger Dryas or several millennia earlier.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            ['unassailable', 'prescriptive', 'equivocal', 'redundant'],
            'C',
            'Cause-Effect + Restatement Clue: tuyết dày che chắn và đá lăn làm nhiễu tuổi phơi sáng → khiến nhà địa mạo học KHÔNG THỂ PHÂN ĐỊNH CHẮC CHẮN giữa hai kịch bản niên đại khác nhau ("unable to resolve whether [A] or [B]") → MẬP MỜ, ĐA NGHĨA, CHƯA NGÃ NGŨ → "equivocal" (C)!',
            'Nhớ định nghĩa sắc bén của "equivocal": open to two or more competing interpretations / uncertain (mập mờ không ngã ngũ giữa hai khả năng)!',
            [
                ('Opposite Meaning', 'unassailable = không thể bác bỏ, chắc chắn tuyệt đối — trái ngược hoàn toàn với "unable to resolve".'),
                ('Wrong Meaning', 'prescriptive = mang tính áp đặt quy tắc — không dùng cho dữ liệu niên đại địa chất.'),
                ('Đáp án đúng', 'equivocal = mập mờ, có thể giải thích theo nhiều hướng — khớp hoàn toàn với việc không phân định nổi hai mốc thời gian.'),
                ('Wrong Meaning', 'redundant = dư thừa lặp lại — không nói dữ liệu bị trùng lặp mà là bị nhiễu không rõ nghĩa.'),
            ]
        ),

        # --- Q6-Q7: Craft and Structure — Text Structure and Purpose (Hard / Elite) ---
        q_item(
            'm7_m2h_q6', 6, 'Craft and Structure', 'Text Structure and Purpose', 'Elite (750+)',
            '<p>Because small, cool M-dwarf stars emit relatively dim light, astronomers prioritize rocky exoplanets orbiting them as prime targets for atmospheric transmission spectroscopy with space telescopes. <u>Yet M-dwarfs frequently rotate rapidly and generate dense clusters of cool magnetic starspots and bright hot faculae whose uneven surface brightness can imprint false molecular slopes onto transit spectra—even when an orbiting planet is completely airless.</u> Consequently, spectroscopists increasingly pair transit observations with multi-week stellar brightness monitoring before declaring any detection of planetary water or carbon dioxide.</p>',
            'Which choice best describes the function of the underlined sentence in the text as a whole?',
            [
                'It introduces a stellar interference mechanism that complicates interpreting transit data from the targets praised in the first sentence.',
                'It demonstrates that rocky exoplanets orbiting M-dwarf stars can never retain atmospheric water or carbon dioxide.',
                'It explains why space telescopes cannot observe exoplanets orbiting stars larger and hotter than M-dwarfs.',
                'It summarizes the multi-week stellar monitoring technique astronomers invented to remove starspots from M-dwarf surfaces.'
            ],
            'A',
            'Câu 1 nêu lý do M-dwarf là mục tiêu hàng đầu cho quang phổ truyền qua. Câu gạch chân mở bằng "Yet" nêu CƠ CHẾ NHIỄU TỪ CHÍNH NGÔI SAO MẸ (vết đen và đốm sáng từ trường tạo ra tín hiệu phân tử giả ngay cả khi hành tinh trơ trụi không khí quyển) — giải thích trở ngại buộc câu 3 phải kết hợp theo dõi độ sáng sao nhiều tuần → Chọn A!',
            'Nhận diện mạch "Ưu điểm mục tiêu [Câu 1] → Yet [Trở ngại gây nhiễu phép đo — Câu 2] → Consequently [Biện pháp khắc phục — Câu 3]".',
            [
                ('Đáp án đúng', 'Chỉ rõ chức năng của câu gạch chân: nêu cơ chế nhiễu từ bề mặt sao mẹ làm phức tạp việc diễn giải quang phổ của mục tiêu câu 1.'),
                ('Too Extreme', 'Câu gạch chân nói "even when an orbiting planet is completely airless" (ngay cả khi hành tinh không có khí quyển), KHÔNG khẳng định mọi hành tinh quanh sao lùn M đều không thể giữ khí quyển.'),
                ('Out of Scope', 'Không giải thích về sao lớn nóng hơn M-dwarf.'),
                ('Fact Distortion', 'Câu gạch chân không tóm tắt kỹ thuật theo dõi (câu 3 mới nhắc) và càng không nói nhà thiên văn "xóa vết đen khỏi bề mặt ngôi sao" (vô lý về vật lý!).'),
            ]
        ),
        q_item(
            'm7_m2h_q7', 7, 'Craft and Structure', 'Text Structure and Purpose', 'Elite (750+)',
            '<p><i>The following text is adapted from a 1931 Harlem memoir recalling the quiet hours after a ballroom set had ended.</i><br/>Long after the dancers had filed down the marble stairs of the Renaissance Casino and the brass players had snapped shut their velvet-lined cases, old Mr. Bell stayed bent beneath a single green-shaded lamp at the edge of the empty bandstand. Dipping his steel nib into India ink, he copied each improvised saxophone chorus from the arranger’s penciled shorthand onto heavy manuscript cards, smoothing smudges with a razor blade until every triplet stood crisp as carved ivory. Nobody applauded a copyist at curtain call, yet without his midnight patience the fleeting miracles of Friday night would have vanished before the tour bus reached Baltimore.</p>',
            'Which choice best states the main purpose of the text?',
            [
                'To contrast the acoustics of Harlem ballrooms with those of touring concert halls in Baltimore.',
                'To argue that jazz soloists depended too heavily on written sheet music rather than spontaneous improvisation.',
                'To lament that Renaissance Casino audiences frequently departed before the band finished its final set.',
                'To honor the uncelebrated, meticulous behind-the-scenes craft that preserves ephemeral jazz improvisations for future performances.'
            ],
            'D',
            'Toàn đoạn khắc họa hình ảnh ông Bell — người chép tổng phổ lặng lẽ ngồi dưới ngọn đèn chao xanh lúc nửa đêm tỉ mỉ chép mực từng đoạn solo ngẫu hứng để chúng không tan biến trước chuyến lưu diễn tới Baltimore; câu kết tôn vinh trực tiếp giá trị thầm lặng ấy ("Nobody applauded a copyist... yet without his midnight patience the fleeting miracles... would have vanished") → Chọn D!',
            'Chú ý tông trân trọng ở câu kết ("yet without his midnight patience the fleeting miracles... would have vanished") → tôn vinh công lao thầm lặng gìn giữ nghệ thuật ngẫu hứng.',
            [
                ('Out of Scope', 'Baltimore chỉ được nhắc như chặng lưu diễn tiếp theo, không hề so sánh âm học khán phòng.'),
                ('Distortion', 'Chính các đoạn solo vốn được ngẫu hứng ("improvised saxophone chorus"), việc chép lại là để lưu giữ chứ không phê phán nhạc công lệ thuộc bản nhạc.'),
                ('Misreading', 'Khán giả rời đi sau khi buổi diễn đã kết thúc ("after a ballroom set had ended"), không phải bỏ về giữa chừng.'),
                ('Đáp án đúng', 'Bắt trọn chủ đích tôn vinh tay nghề tỉ mỉ, thầm lặng giúp biến phép màu ngẫu hứng thoáng qua thành di sản biểu diễn lâu dài.'),
            ]
        ),

        # --- Q8: Craft and Structure — Cross-Text Connections (Elite 750+) ---
        q_item(
            'm7_m2h_q8', 8, 'Craft and Structure', 'Cross-Text Connections', 'Elite (750+)',
            '<p><b>Text 1</b><br/>Geomorphologist Dr. Henrik Lindqvist contends that the vast swarms of streamlined, teardrop-shaped hills known as drumlins across western New York were sculpted not by solid glacier ice, but by catastrophic subglacial megafloods—enormous pressurized sheets of meltwater that surged beneath collapsing ice sheets and carved the landscape in mere weeks.</p><p><b>Text 2</b><br/>Examining deep sediment cores drilled across forty western New York drumlins, glacial geologist Dr. Priya Nair found continuous, steeply folded beds of unsorted clay-rich till characteristic of slow shearing beneath moving ice rather than turbulent water-sorted gravel. Nair notes, however, that narrow bands of water-rounded cobbles do cut across the lower margins of several drumlins, recording localized meltwater streams that incised the hills’ flanks well after the landforms themselves had taken shape.</p>',
            'Based on the texts, how would Dr. Priya Nair (Text 2) most likely respond to Dr. Henrik Lindqvist’s contention (Text 1)?',
            [
                'By asserting that meltwater played no geological role whatsoever anywhere in western New York’s drumlin fields.',
                'By arguing that the drumlins’ internal sediment structures point to gradual deformation by moving ice rather than formation by subglacial megafloods, even though localized meltwater later eroded their lower margins.',
                'By agreeing that catastrophic subglacial megafloods originally shaped the drumlins, while adding that moving ice subsequently reshaped their outer flanks.',
                'By suggesting that sediment cores cannot distinguish between deposits left by moving glacier ice and gravel sorted by turbulent meltwater.'
            ],
            'B',
            'So sánh 2 văn bản cực sắc: Text 1 quy toàn bộ quá trình tạo đồi drumlin cho đại hồng thủy băng tan dưới đáy (megafloods). Text 2 bác bỏ nguyên nhân tạo hình đó bằng lõi trầm tích (lớp sét băng tích không phân loại bị uốn nếp chậm dưới băng trượt, KHÔNG phải sỏi phân loại do lũ xiết), NHƯNG vẫn thừa nhận có dải cuội nước bào mòn cục bộ ở chân đồi *sau khi đồi đã hình thành*. Bẫy A quá cực đoan ("no role whatsoever"); Bẫy C đảo ngược trình tự băng và nước; Duy nhất B giữ trọn cả vế phản bác chính lẫn phần thừa nhận sắc thái (localized later erosion)!',
            'Câu Cross-Text 750+ luôn cài một nhượng bộ nhỏ ở câu cuối Text 2 ("however, narrow bands..."). Loại ngay đáp án cực đoan xóa sạch nhượng bộ (A) và chọn đáp án phản ánh đủ cả hai tầng ý (B)!',
            [
                ('Overstated Conflict', '"no geological role whatsoever" bác bỏ chính phát hiện của Nair về các dòng nước băng tan cục bộ cắt qua mép dưới đồi.'),
                ('Đáp án đúng', 'Phản ánh chính xác lập trường có sắc thái của Nair: lõi trầm tích chứng minh băng trượt chậm tạo đồi (bác megaflood), còn nước băng tan chỉ xói mòn cục bộ mép dưới về sau.'),
                ('Reversed Chronology', 'Đảo ngược hoàn toàn trình tự và vai trò giữa lũ băng tan và băng trượt của Nair.'),
                ('Contradiction', 'Nair đã DÙNG CHÍNH lõi trầm tích để phân biệt rõ băng tích chưa phân loại với sỏi nước chảy.'),
            ]
        ),

        # --- Q9-Q10: Information and Ideas — Central Ideas and Details (Hard / Elite) ---
        q_item(
            'm7_m2h_q9', 9, 'Information and Ideas', 'Central Ideas and Details', 'Hard',
            '<p><i>The following poem, “Moraine,” is adapted from a 1924 alpine verse collection.</i><br/>Where century-deep blue rivers froze and ground<br/>The stubborn granite to a chalky flour,<br/>The retreating ice leaves neither root nor sound—<br/>Only raw ridges scarred by vanished power.<br/>Yet meltwater gathers in each bruised hollow,<br/>And wind-borne lupine seeds lodge in the grit;<br/>Beneath bare frost, pale stubborn shoots will follow,<br/>Claiming the stone the glacier had to quit.</p>',
            'Which choice best states the main idea of the poem?',
            [
                'Retreating mountain glaciers permanently destroy alpine granite, leaving terrain incapable of supporting plant life.',
                'Windstorms in high alpine valleys strip away chalky granite soil faster than melting glaciers can deposit it.',
                'Although a receding glacier initially exposes a bleak, scarred landscape, its meltwater and ground rock gradually enable resilient vegetation to take hold.',
                'Alpine lupines survive winter freezes only when sheltered beneath deep, permanent sheets of blue glacial ice.'
            ],
            'C',
            'Bố cục 2 nửa rõ rệt quanh từ chuyển hướng "Yet": 4 dòng đầu mô tả cảnh hoang tàn đá bị nghiền nát không rễ cây khi sông băng rút đi; 4 dòng sau mở bằng "Yet" cho thấy nước băng tan đọng lại trong hốc đá, hạt hoa lupin theo gió bám vào sạn đá và những mầm cây kiên cường dần chiếm lĩnh mảnh đá sông băng bỏ lại → Chọn C!',
            'Tìm từ chuyển mạch "Yet" chia đôi bài thơ: Nửa 1 (hoang tàn sau khi băng rút) + Nửa 2 (sự sống dần tái sinh nhờ nước tan và hạt giống) → gộp cả hai nửa vào Main Idea!',
            [
                ('Half-Passage / Contradiction', 'Bỏ qua hoàn toàn 4 dòng cuối nói hạt lupin và mầm cây đang nảy nở chiếm lĩnh vùng đá.'),
                ('Misreading', 'Gió mang hạt giống lupin tới bám vào sạn đá ("wind-borne lupine seeds lodge in the grit"), không nói gió thổi bay đất.'),
                ('Đáp án đúng', 'Bao trọn trọn vẹn cả hai nửa đối lập của bài thơ: cảnh hoang vu ban đầu và sự tái sinh kiên cường của thực vật.'),
                ('Reversed Logic', 'Cây mọc lên sau khi băng rút đi ("stone the glacier had to quit"), không sống dưới lớp băng vĩnh cửu.'),
            ]
        ),
        q_item(
            'm7_m2h_q10', 10, 'Information and Ideas', 'Central Ideas and Details', 'Elite (750+)',
            '<p>Laboratory trials have sparked enthusiasm for using native freshwater mussels (<i>Elliptio complanata</i>) to strip synthetic microplastics from polluted urban rivers. Yet recent multi-week mesocosm studies reveal an ecological trade-off: while mussels efficiently clear suspended polyethylene fibers from the water column and pack them into sunken pseudofeces, sustained exposure to dense fiber loads lowers the mussels’ own gill-clearance efficiency by up to 35 percent and concentrates plastic pellets on the riverbed, where bottom-dwelling crayfish and amphipods readily ingest them.</p>',
            'Which choice best states the main idea of the text?',
            [
                'Although native freshwater mussels effectively remove microplastics from open river currents, prolonged heavy exposure can impair their filtration performance and redirect plastic pollution into bottom-dwelling food webs.',
                'Bottom-dwelling crayfish and amphipods are far more efficient than native freshwater mussels at breaking down polyethylene fibers into harmless compounds.',
                'Native freshwater mussels cannot filter synthetic microplastics out of urban rivers unless suspended fiber concentrations remain extremely low.',
                'Laboratory trials have definitively disproved the hypothesis that freshwater mussels produce mucus-bound pseudofeces when exposed to river algae.'
            ],
            'A',
            'Ý chính toàn đoạn nằm ở cụm "an ecological trade-off" sau "Yet": mặt tích cực là trai lọc hiệu quả sợi nhựa khỏi cột nước; NHƯNG mặt đánh đổi kép là [1] phơi nhiễm đậm đặc kéo dài làm giảm tới 35% hiệu suất lọc mang của chính con trai VÀ [2] gom nhựa thành viên dưới đáy khiến tôm càng và giáp xác tầng đáy ăn phải (đẩy ô nhiễm vào lưới thức ăn tầng đáy) → Chọn A!',
            'Nhận diện khung "Enthusiasm for X. Yet trade-off: [benefit] comes with [cost 1] and [cost 2]" → Đáp án đúng phải bao quát cả ưu điểm lẫn hai hệ lụy đánh đổi!',
            [
                ('Đáp án đúng', 'Tóm gọn chuẩn xác cả lợi ích lọc cột nước lẫn hai mặt trái (suy giảm hiệu suất lọc của trai + chuyển nhựa sang sinh vật đáy).'),
                ('Fact Distortion', 'Tôm càng và giáp xác đáy chỉ ăn nhầm viên nhựa tập trung ở đáy, bài không hề nói chúng phân hủy nhựa thành chất vô hại.'),
                ('Contradiction', 'Ngay cả dưới tải lượng dày, hiệu suất lọc giảm tới 35% chứ không phải hoàn toàn không lọc được ("cannot filter").'),
                ('Out of Scope / False', 'Không hề phủ nhận việc trai tạo giả phân khi gặp tảo.'),
            ]
        ),

        # --- Q11-Q12: Information and Ideas — Command of Evidence (Textual — Elite 750+) ---
        q_item(
            'm7_m2h_q11', 11, 'Information and Ideas', 'Command of Evidence (Textual)', 'Elite (750+)',
            '<p>Many nineteenth-century Edo woodblock prints displayed in modern museums feature subdued, pale tan skies that art critics long admired as deliberate autumn minimalism. Art chemist Dr. Fumiko Sato, however, hypothesized that those muted skies were not originally printed in tan at all; instead, printmakers had applied vibrant organic crimson and violet dyes extracted from safflower (<i>beni</i>) and dayflower petals that subsequently bleached under decades of gallery lighting.</p>',
            'Which finding, if true, would most directly support Dr. Fumiko Sato’s hypothesis?',
            [
                'Historical guild price ledgers from 1842 show that imported mineral pigments cost roughly three times as much per ounce as locally grown safflower dye.',
                'Chemical analyses of unprinted mulberry paper sheets from Edo workshops confirm that sizing glue made from animal gelatin yellows slightly with age.',
                'Modern printmakers attempting to recreate Utagawa Hiroshige’s landscapes often mix mineral ocher with charcoal soot to obtain warm autumn sky tones.',
                'Micro-spectroscopic scans of an 1840s landscape print reveal vivid safflower crimson and dayflower violet chromophores surviving intact along a narrow top-edge border shielded beneath its original wooden frame, shifting abruptly to pale tan at the exact boundary where light reached the paper.'
            ],
            'D',
            'Khóa giả thuyết Sato: Bầu trời màu nâu nhạt hiện nay VỐN DĨ được in bằng phẩm hữu cơ đỏ thắm (*beni*) và tím (*dayflower*), sau đó bị ánh sáng phòng trưng bày làm bạc màu thành nâu nhạt. Đáp án D đưa ra bằng chứng đối chứng tự nhiên hoàn hảo (protected-margin evidence): phần mép giấy bị khung gỗ che khuất ánh sáng vẫn còn nguyên sắc đỏ thắm safflower và tím dayflower rực rỡ, và đổi đột ngột sang nâu nhạt ĐÚNG TẠI RANH GIỚI ánh sáng chiếu tới! Chọn D!',
            'Tìm bằng chứng đối chứng không gian cùng một bản in: vùng bị khung che sáng còn nguyên phẩm gốc ↔ vùng phơi sáng chuyển nâu nhạt đúng ngay đường ranh sáng!',
            [
                ('Adjacent Topic Drift', 'Giá rẻ của phẩm safflower chỉ gợi ý khả năng kinh tế, không chứng minh bầu trời nâu nhạt thực chất từng được in bằng phẩm đó rồi bạc màu.'),
                ('Alternative Explanation (Weakens!)', 'Keo giấy tự ngả vàng theo thời gian gợi ý nguyên nhân từ chất liệu giấy, KHÔNG chứng minh phẩm đỏ/tím bị phai sáng.'),
                ('Irrelevant Subject', 'Kỹ thuật của nghệ nhân hiện đại không kiểm chứng màu gốc của bản in thế kỷ 19.'),
                ('Đáp án đúng', 'Bằng chứng trực diện không thể chối cãi: đúng hóa chất safflower & dayflower còn nguyên nơi khuất sáng và chuyển sang nâu nhạt ngay ranh giới chiếu sáng.'),
            ]
        ),
        q_item(
            'm7_m2h_q12', 12, 'Information and Ideas', 'Command of Evidence (Textual)', 'Elite (750+)',
            '<p>In a study of Harlem Renaissance cultural criticism, a literary scholar argues that essayist Marcus Thorne championed Caribbean and Southern vernacular speech in modern literature not as picturesque local color meant to charm metropolitan readers, but as a rigorous intellectual medium capable of capturing philosophical nuances that standardized academic prose flattens.</p>',
            'Which quotation from Marcus Thorne’s 1925 essay <i>Notes on the Vernacular Line</i> most effectively illustrates the scholar’s claim?',
            [
                '“Tourists strolling past Lenox Avenue bookstalls eagerly buy dialect pamphlets because the unfamiliar spellings lend an entertaining flavor of distant islands.”',
                '“To treat our island and delta speech as quaint parlor ornament is to misread its sharpest virtue: its compressed cadence and layered double meanings carry moral ironies that polite textbook English routinely irons smooth.”',
                '“Because printing houses rarely cast special accent marks, young poets writing in Jamaican Patois must negotiate carefully with typesetters before going to press.”',
                '“Every living tongue borrows freely from maritime trade, and standard English itself absorbed countless nautical phrases across three centuries of Atlantic commerce.”'
            ],
            'B',
            'Checklist 2 vế từ Claim: [1] Bác bỏ việc xem ngôn ngữ bản địa chỉ là "màu sắc địa phương dễ thương để làm vui lòng độc giả đô thị" ("not as picturesque local color") + [2] Khẳng định nó là phương tiện trí tuệ sắc bén truyền tải tầng nghĩa triết học/đạo đức tinh vi mà văn học thuật chuẩn hóa thường làm phẳng mất ("flattens"). Đáp án B phản chiếu trực diện từng vế: "quaint parlor ornament" (bác bỏ vật trang trí dễ thương) ↔ "carry moral ironies that polite textbook English routinely irons smooth" (= flattens)! Chọn B!',
            'So khớp cặp đối lập chính xác: "quaint parlor ornament" ↔ "picturesque local color", và "irons smooth" ↔ "flattens"!',
            [
                ('Opposite Viewpoint Trap', 'Trích dẫn này chỉ mô tả chính thái độ nông cạn của khách du lịch mà Thorne bác bỏ.'),
                ('Đáp án đúng', 'Khớp hoàn mỹ cả hai vế: bác bỏ vai trò trang trí dễ thương và tôn vinh năng lực biểu đạt chiều sâu mỉa mai đạo đức vượt lên thứ tiếng Anh sách giáo khoa bị làm phẳng.'),
                ('Irrelevant Detail', 'Chỉ nói về khó khăn kỹ thuật sắp chữ in dấu phụ tại nhà in.'),
                ('Too Broad / Off-Point', 'Nói chung chung về vay mượn từ ngữ hàng hải của tiếng Anh chuẩn, không bảo vệ chiều sâu trí tuệ của ngôn ngữ bản địa.'),
            ]
        ),

        # --- Q13-Q14: Information and Ideas — Command of Evidence (Quantitative — Elite 750+) ---
        q_item(
            'm7_m2h_q13', 13, 'Information and Ideas', 'Command of Evidence (Quantitative)', 'Elite (750+)',
            svg_bar_chart(
                'Mean Post-Fire Riparian Vegetation Survival (%) Across Three Western Megafires',
                ['0%', '25%', '50%', '75%', '100%'],
                [('Undammed Steep', 18, '18%'), ('Undammed Flat', 41, '41%'), ('Abandoned Dams', 53, '53%'), ('Active Beaver Dams', 89, '89%')],
                100
            ) + '<p>A forestry skeptic argues that beaver-dammed stream reaches appear more resilient to western megafires solely because beavers choose to colonize broad, flat valley floors—which naturally retain more moisture than steep canyons—rather than because active dam maintenance by beavers provides any substantial extra fire protection.</p>',
            'Which choice best describes data from the graph that most directly undermine the forestry skeptic’s argument?',
            [
                'Undammed flat valley streams retained 41% of their riparian vegetation after megafires, more than double the 18% survival rate recorded in undammed steep canyons.',
                'Abandoned beaver-dam sites preserved 53% of their vegetation, which was 35 percentage points higher than the survival rate in undammed steep canyons (18%).',
                'Reaches with active beaver dams preserved 89% of riparian vegetation—more than double the 41% survival rate in comparable undammed flat valleys and 36 percentage points above flat valleys with abandoned dams (53%).',
                'None of the four stream categories analyzed across the three western megafires achieved 100% post-fire riparian vegetation survival.'
            ],
            'C',
            'Khóa lập luận cần PHẢN BÁC (Undermine): Người hoài nghi cho rằng đập hải ly chỉ ăn may nhờ nằm ở **thung lũng phẳng** (vốn tự nhiên ẩm hơn hẻm dốc), chứ **sự duy trì đập chủ động của hải ly không mang lại bảo vệ đáng kể thêm**. Để đập tan lập luận này, phải KIỂM SOÁT biến địa hình phẳng: so sánh `Active Beaver Dams` (89%) trực tiếp với `Undammed Flat` (41%) và `Abandoned Dams` (53%)! Kết quả: 89% vượt hơn gấp đôi thung lũng phẳng không có đập (41%) và hơn tới 36 điểm phần trăm so với đập bỏ hoang (53%) → Chứng minh chính hoạt động duy trì đập chủ động mới tạo ra mức bảo vệ khổng lồ! Chọn C!',
            'Câu hỏi kiểm soát biến nhiễu (Confounding Variable Control) chuẩn 750+: giữ cố định địa hình phẳng (`Flat`), đối chiếu `Active` (89%) vs. `Undammed Flat` (41%) & `Abandoned` (53%) — loại bẫy A (lại đi ỦNG HỘ lập luận thung lũng phẳng ẩm hơn hẻm dốc)!',
            [
                ('Opposite Direction (Supports Skeptic!)', 'So sánh Undammed Flat (41%) với Undammed Steep (18%) lại củng cố ý của người hoài nghi rằng thung lũng phẳng vốn tự nhiên giữ ẩm tốt hơn!'),
                ('Wrong Comparison Group', 'So sánh Abandoned Dams với Steep Canyons không kiểm soát biến địa hình phẳng và bỏ qua Active Beaver Dams.'),
                ('Đáp án đúng', 'Cô lập chính xác tác động của việc duy trì đập chủ động (89%) so với thung lũng phẳng không đập (41%) và đập bị bỏ hoang (53%).'),
                ('True Data / Wrong Claim', 'Việc không có nhóm nào đạt 100% hoàn toàn không phản bác giả thuyết về vai trò địa hình của người hoài nghi.'),
            ]
        ),
        q_item(
            'm7_m2h_q14', 14, 'Information and Ideas', 'Command of Evidence (Quantitative)', 'Elite (750+)',
            html_table(
                'Table 1. Southern Quechua Evidential Suffix (-mi / -si) Mastery Among Bilingual Young Adults (Ages 18–30) in Four Peruvian Highland Districts',
                ['District', 'Spanish Loanword Share in Speech', 'Daily Quechua Home Use', 'Correct Use of -mi / -si Evidentials'],
                [
                    ['Paucartambo', '34%', '82%', '89%'],
                    ['Chinchero', '29%', '76%', '84%'],
                    ['Urubamba', '22%', '41%', '57%'],
                    ['Calca', '18%', '38%', '52%'],
                ]
            ) + '<p>A contact linguist hypothesizes that incorporating a higher percentage of borrowed Spanish vocabulary into everyday Quechua speech inevitably erodes younger speakers’ grammatical mastery of traditional Quechua evidential suffixes (<i>-mi</i> and <i>-si</i>).</p>',
            'Which choice best describes data from the table that directly challenge the contact linguist’s hypothesis?',
            [
                'In Calca, young adults incorporated the lowest share of Spanish loanwords (18%) and also reported the lowest daily Quechua home use (38%).',
                'Across all four highland districts surveyed, fewer than 90% of young adults demonstrated consistent mastery of the <i>-mi</i> and <i>-si</i> evidential suffixes.',
                'Young adults in Chinchero showed higher daily Quechua home use (76%) and higher evidential mastery (84%) than young adults in Urubamba (41% and 57%).',
                'Although young adults in Paucartambo and Chinchero used the highest shares of Spanish loanwords (34% and 29%), they achieved far higher mastery of Quechua evidential suffixes (89% and 84%) than speakers in Urubamba (22% loanwords; 57% mastery) and Calca (18% loanwords; 52% mastery).'
            ],
            'D',
            'Khóa giả thuyết cần CHALLENGE: Tỷ lệ từ mượn tiếng Tây Ban Nha càng CAO → độ thành thạo hậu tố chứng cứ Quechua (`-mi/-si`) càng BỊ XÓI MÒN (THẤP ĐI). Soi bảng: Hai quận có tỷ lệ từ mượn Tây Ban Nha CAO NHẤT là **Paucartambo (34%)** và **Chinchero (29%)** lại đạt độ thành thạo ngữ pháp chứng cứ CAO VƯỢT TRỘI (**89%** và **84%**), cao hơn hẳn **Urubamba (22% từ mượn → 57% thành thạo)** và **Calca (18% từ mượn → 52% thành thạo)**! Chọn D!',
            'So sánh trực tiếp hai cột trong Claim (`Spanish Loanword Share` vs. `Correct Use of -mi/-si`): hai cột tăng CÙNG CHIỀU thay vì ngược chiều → đập tan hoàn toàn giả thuyết xói mòn!',
            [
                ('Incomplete Data', 'Chỉ nêu thông số một quận Calca và lại dẫn cột Home Use thay vì đối chiếu loanwords vs. evidential mastery giữa các quận.'),
                ('True Data / Wrong Claim', 'Việc mọi quận đều dưới 90% không hề phản bác mối quan hệ giữa tỷ lệ từ mượn và độ thành thạo ngữ pháp.'),
                ('Wrong Variable Comparison', 'So sánh Home Use với Evidential Mastery mà bỏ qua biến chính "Spanish Loanword Share" của giả thuyết.'),
                ('Đáp án đúng', 'Đối chiếu trọn vẹn xu hướng ngược hẳn giả thuyết: nhóm mượn từ Tây Ban Nha nhiều nhất (34%, 29%) lại giữ vững hậu tố chứng cứ tốt nhất (89%, 84%).'),
            ]
        ),

        # --- Q15: Information and Ideas — Inferences (Elite 750+) ---
        q_item(
            'm7_m2h_q15', 15, 'Information and Ideas', 'Inferences', 'Elite (750+)',
            '<p>In static laboratory aquariums, invasive zebra mussels (<i>Dreissena polymorpha</i>) clear suspended microplastic beads from water nearly twice as fast per gram of body weight as native unionid mussels (<i>Lampsilis siliquoidea</i>). Yet field studies in turbulent Great Lakes tributaries show that when dense zebra mussel colonies encrust native unionids’ shells, long-term watershed retention of microplastics actually declines: zebra mussels expel fragile, loosely packed pellets onto exposed rock surfaces where spring flood currents readily resuspend and flush them downstream, whereas unimpeded unionids burrow into gravel beds and deposit cohesive mucus-bound pellets directly into deep subsurface sediment. Taken together, these findings suggest that ______</p>',
            'Which choice most logically completes the text?',
            [
                'judging bivalve species’ long-term microplastic remediation potential solely from laboratory filtration rates can overestimate the watershed-scale benefits of invasive zebra mussels relative to native burrowing species.',
                'invasive zebra mussels are physiologically incapable of filtering synthetic microplastic beads in turbulent tributary waters.',
                'spring flood currents along Great Lakes tributaries sweep away native burrowing unionid mussels before they can produce mucus-bound pellets.',
                'eliminating zebra mussels from Great Lakes tributaries would immediately remove all microplastics currently buried in deep subsurface sediment.'
            ],
            'A',
            'Ghép 2 tiền đề (1-Millimeter Rule 750+): (A) Trong bể tĩnh phòng thí nghiệm, trai vằn ngoại lai lọc nhanh gấp đôi trai bản địa tính theo gram khối lượng; (B) NHƯNG ngoài sông suối thực địa có lũ mùa xuân, trai vằn thải viên lỏng trên đá lộ thiên nên bị lũ cuốn trôi mất, còn trai bản địa đào hang chôn chặt viên nhầy xuống trầm tích sâu → khiến việc lưu giữ lâu dài giảm xuống khi trai vằn lấn át trai bản địa ⇒ Kết luận 1mm duy nhất hợp lý: Đánh giá tiềm năng xử lý vi nhựa dài hạn chỉ dựa vào tốc độ lọc trong phòng thí nghiệm có thể đánh giá QUÁ CAO lợi ích quy mô lưu vực của trai vằn ngoại lai so với loài bản địa đào hang (A)!',
            'Công thức Inference 750+: "Lab metric favors X, YET real-world physical mechanism favors Y → relying solely on lab metric overestimates X relative to Y"!',
            [
                ('Đáp án đúng', 'Suy diễn 1mm chặt chẽ kết nối sự chênh lệch giữa tốc độ lọc phòng thí nghiệm và cơ chế giữ trầm tích dài hạn ngoài thực địa.'),
                ('Contradiction', 'Trai vằn VẪN lọc và thải viên ra mặt đá ở sông suối, vấn đề là viên lỏng bị lũ cuốn trôi chứ không phải chúng không lọc được.'),
                ('Reversed Logic', 'Bài nói chính trai bản địa đào sâu vào tầng sỏi để khóa chặt viên nhầy, còn viên của trai vằn mới bị cuốn trôi.'),
                ('Too Extreme / Nonsense', 'Loại bỏ trai vằn không làm biến mất vi nhựa đã chôn sâu dưới trầm tích (và bài không hề đề cập việc xóa sạch nhựa đã chôn).'),
            ]
        ),

        # --- Q16-Q19: Standard English Conventions — Boundaries (Hard / Elite) ---
        q_item(
            'm7_m2h_q16', 16, 'Standard English Conventions', 'Boundaries', 'Hard',
            '<p>In a 2024 spectroscopic review, astrophysicist Dr. Elena Ruiz classified close-in exoplanets into three atmospheric regimes: ultra-hot Jupiters, whose tidally locked daysides vaporize titanium oxide; temperate sub-Neptunes, whose hydrogen-rich envelopes harbor methane and carbon ______ and airless rocky worlds, whose exposed basalt crusts emit bare thermal radiation.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['dioxide,', 'dioxide;', 'dioxide:', 'dioxide'],
            'B',
            'Quy tắc Super-Comma (Chấm phẩy phân tách chuỗi phức tạp có dấu phẩy nội bộ)! Chuỗi gồm 3 hạng mục dài đều chứa dấu phẩy nội bộ (`whose...`): [1] `ultra-hot Jupiters, whose... titanium oxide;` → [2] `temperate sub-Neptunes, whose... carbon dioxide;` → [3] `and airless rocky worlds, whose... thermal radiation.` Bắt buộc dùng dấu chấm phẩy (`;`) để khớp song song với dấu `;` sau `titanium oxide;` → Chọn B!',
            'Nhận diện tín hiệu "Super-Comma List": Thấy một dấu chấm phẩy đứng giữa các cụm danh từ song song có mệnh đề phụ `, whose...` → lập tức đóng tiếp bằng dấu chấm phẩy `;`!',
            [
                ('List Separator Mismatch', 'Dấu phẩy thường bị hòa lẫn với dấu phẩy nội bộ của các mệnh đề "whose..." và lệch nhịp với dấu chấm phẩy đầu chuỗi.'),
                ('Đáp án đúng', 'Dấu chấm phẩy (;) phân tách chuẩn xác hạng mục thứ 2 và thứ 3 trong danh sách phức tạp.'),
                ('Improper Colon', 'Không dùng dấu hai chấm giữa các phần tử song song của một danh sách.'),
                ('Missing Separator', 'Thiếu dấu phân cách làm cụm thứ 2 dính liền vào "and airless rocky worlds".'),
            ]
        ),
        q_item(
            'm7_m2h_q17', 17, 'Standard English Conventions', 'Boundaries', 'Elite (750+)',
            '<p>During the late 1920s, Harlem bandleader Fletcher Henderson transformed stiff, march-like dance numbers into buoyant swing ______ call-and-response riffs between reed and brass sections so that each choir seemed to converse with the other.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['anthems; trading', 'anthems. Trading', 'anthems, he traded', 'anthems, trading'],
            'D',
            'Vế 1 là 1 IC hoàn chỉnh ("During the late 1920s, Harlem bandleader Fletcher Henderson transformed... into buoyant swing anthems"). Vế 2 ("trading call-and-response riffs...") là Cụm phân từ V-ing (Participial Phrase — KHÔNG phải IC!) bổ sung cách thức cho mệnh đề chính → Nối IC với cụm phân từ bằng 1 dấu phẩy (`, trading`) = D! Loại A (`;` + Fragment), B (`.` + Fragment), và C (Comma Splice: IC + `,` + IC)!',
            'Kiểm tra nhanh vế sau: bắt đầu bằng `trading` (V-ing, không có chủ ngữ và động từ chia thì) → KHÔNG phải IC → loại sạch chấm phẩy (;), dấu chấm (.) và tránh Comma Splice!',
            [
                ('Semicolon + Fragment', 'Vế sau bắt đầu bằng phân từ "trading", không phải IC → cấm dấu chấm phẩy.'),
                ('Period + Fragment', 'Tách cụm phân từ "Trading..." thành câu độc lập tạo Sentence Fragment.'),
                ('Comma Splice', '"anthems, he traded..." ghép hai IC bằng một dấu phẩy → lỗi Comma Splice.'),
                ('Đáp án đúng', 'Dấu phẩy + phân từ ("anthems, trading") nối chuẩn xác cụm bổ sung cách thức vào IC.'),
            ]
        ),
        q_item(
            'm7_m2h_q18', 18, 'Standard English Conventions', 'Boundaries', 'Elite (750+)',
            '<p>Because Caribbean creole languages crystallized rapidly across multilingual plantation colonies, nineteenth-century scholars assumed their verb systems lacked grammatical ______ archival research, however, has documented intricate tense-aspect distinctions preserved intact since the seventeenth century.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['depth; subsequent', 'depth, subsequent', 'depth subsequent', 'depth: while subsequent'],
            'A',
            'Bẫy 750+ kinh điển với trạng từ liên kết `however` đứng GIỮA vế sau! Vế 1 là IC hoàn chỉnh ("Because..., nineteenth-century scholars assumed their verb systems lacked grammatical depth"). Vế 2 cũng là IC hoàn chỉnh ("subsequent archival research, however, has documented..."). Vì `however` nằm xen giữa (chứ không nối được 2 IC bằng dấu phẩy!), ranh giới giữa `depth` và `subsequent` BẮT BUỘC phải là dấu chấm phẩy (`;`) → Chọn A!',
            'Nhớ quy tắc sắt: `however` là trạng từ liên kết (KHÔNG phải FANBOYS!). Giữa 2 IC luôn phải ngắt bằng `;` hoặc `.` — ngay cả khi `, however,` trốn sâu ở giữa vế 2!',
            [
                ('Đáp án đúng', 'Dấu chấm phẩy (;) ngắt chuẩn xác hai mệnh đề độc lập, để ", however," đóng vai trò trạng từ xen giữa hợp lệ ở vế 2.'),
                ('Comma Splice', 'Đặt dấu phẩy ở ranh giới hai IC dù có ", however," phía sau vẫn là lỗi Comma Splice kinh điển.'),
                ('Run-On Sentence', 'Thiếu hoàn toàn dấu câu ngăn hai mệnh đề độc lập.'),
                ('Fragment After Colon', 'Thêm "while" biến vế 2 thành mệnh đề phụ treo lơ lửng không có mệnh đề chính theo sau.'),
            ]
        ),
        q_item(
            'm7_m2h_q19', 19, 'Standard English Conventions', 'Boundaries', 'Elite (750+)',
            '<p>By trapping nutrient-rich silt behind terraced wooden walls, beaver ______ ecosystems that geologists classify as “biogeomorphic” because living animals physically reshape valley topography—create fertile wet meadows that persist for centuries even after the rodents depart.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['ponds,', 'ponds:', 'ponds—', 'ponds;'],
            'C',
            'Soi thật kỹ đoạn giữa Chủ ngữ ("beaver ponds") và Động từ chính ("create"): ngay trước `create` có một dấu gạch ngang dài đóng (`topography—`)! Điều đó chứng tỏ cụm dài `ecosystems that geologists classify as “biogeomorphic” because living animals physically reshape valley topography` là một cụm đồng vị bổ sung (Non-essential Appositive) nằm trong CẶP GẠCH NGANG ĐÔI (`— ... —`) → Bắt buộc mở bằng gạch ngang dài (`ponds—`) = C!',
            'Mẹo giải nhanh câu có modifier cực dài: luôn quét qua bên phải tìm động từ chính (`create`) và xem ngay trước động từ có dấu `,` hay `—` đóng lại không → đóng bằng `—` thì mở PHẢI bằng `—`!',
            [
                ('Mismatched Pair (, ... —)', 'Không được mở bằng dấu phẩy rồi đóng bằng gạch ngang dài.'),
                ('Invalid Colon', 'Không dùng dấu hai chấm tách chủ ngữ "beaver ponds" khỏi động từ "create", và không ghép đôi với "—".'),
                ('Đáp án đúng', 'Khớp hoàn chỉnh cặp gạch ngang đôi (— ... —) bao trọn cụm bổ sung giữa chủ ngữ và động từ chính.'),
                ('Semicolon Inside Clause', 'Dấu chấm phẩy cắt đứt chủ ngữ khỏi động từ chính.'),
            ]
        ),

        # --- Q20-Q22: Standard English Conventions — Form, Structure, and Sense (Hard / Elite) ---
        q_item(
            'm7_m2h_q20', 20, 'Standard English Conventions', 'Form, Structure, and Sense', 'Hard',
            '<p>Hidden within the subtle infrared dips recorded as starlight filters through a distant planet’s upper haze layer ______ telltale spectral fingerprints of methane, carbon dioxide, and trace sulfur compounds.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['lies', 'has lain', 'lying', 'lie'],
            'D',
            'Bẫy 750+: **Đảo ngữ Chủ ngữ (Inverted Subject)**! Cụm mở đầu `Hidden within the subtle infrared dips... upper haze layer` là cụm phân từ chỉ vị trí — KHÔNG phải chủ ngữ! Chủ ngữ thật đứng SAU chỗ trống: **"telltale spectral fingerprints"** (SỐ NHIỀU!). Đừng bị đánh lừa bởi danh từ số ít `layer` ngay trước chỗ trống → Động từ chính chia thì SỐ NHIỀU là **"lie"** (D)!',
            'Gặp câu mở đầu bằng cụm giới từ/phân từ vị trí (`Hidden within...`, `Beneath...`, `Among...`) → nhìn sang PHẢI chỗ trống để tìm Chủ ngữ thật chia động từ!',
            [
                ('Subject-Verb Mismatch', 'lies là số ít — rơi vào bẫy danh từ số ít "upper haze layer" ngay sát chỗ trống.'),
                ('Subject-Verb Mismatch', 'has lain là số ít — không khớp chủ ngữ số nhiều "telltale spectral fingerprints".'),
                ('Non-Finite Fragment', 'lying là phân từ V-ing khiến cả câu không có động từ chính chia thì.'),
                ('Đáp án đúng', 'lie (số nhiều, hiện tại đơn) khớp chuẩn với chủ ngữ đảo đứng sau "telltale spectral fingerprints".'),
            ]
        ),
        q_item(
            'm7_m2h_q21', 21, 'Standard English Conventions', 'Form, Structure, and Sense', 'Elite (750+)',
            '<p>Comparing late-eighteenth-century Kabuki actor portraits with 1830s landscape editions, print historian Dr. Naomi Fujita demonstrated that Edo ______ shifted dramatically once Dutch merchants began importing synthetic Prussian blue into Nagasaki.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['printmakers palettes', 'printmakers’ palettes', 'printmakers’ palette’s', 'printmaker’s palettes’'],
            'B',
            'Quy tắc Sở hữu cách (Possessives): "bảng màu của các nghệ nhân in thời Edo" → `printmakers’` (sở hữu cách số nhiều: của nhiều nghệ nhân in) sở hữu danh từ số nhiều `palettes` (các bảng màu — KHÔNG có dấu nháy sở hữu vì theo sau là động từ `shifted`, không phải danh từ nào thuộc sở hữu của `palettes`!) → Chọn **"printmakers’ palettes"** (B)!',
            'Kiểm tra từng danh từ một: (1) Danh từ 1 sở hữu Danh từ 2 → cần `’` (`printmakers’`); (2) Sau Danh từ 2 là động từ `shifted` (không sở hữu gì nữa) → TUYỆT ĐỐI KHÔNG gắn `’` lên `palettes`!',
            [
                ('Missing Apostrophe', 'Thiếu dấu nháy sở hữu trên "printmakers" khi chỉ bảng màu thuộc về các nghệ nhân.'),
                ('Đáp án đúng', 'printmakers’ (sở hữu cách số nhiều) + palettes (danh từ số nhiều làm chủ ngữ của "shifted") — chuẩn xác 100%.'),
                ('Extra Apostrophe Trap', 'palette’s là sở hữu cách sai vì ngay sau đó là động từ "shifted", không có danh từ bị sở hữu.'),
                ('Extra Apostrophe Trap', 'palettes’ gắn thừa dấu sở hữu trước động từ "shifted".'),
            ]
        ),
        q_item(
            'm7_m2h_q22', 22, 'Standard English Conventions', 'Form, Structure, and Sense', 'Elite (750+)',
            '<p>Trained in classical counterpoint at the Boston Conservatory before settling in Harlem in 1924, ______</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            [
                'composer Lillian Carter infused big-band brass arrangements with intricate polyphonic voicings rarely heard in commercial dance halls.',
                'Lillian Carter’s big-band brass arrangements introduced intricate polyphonic voicings rarely heard in commercial dance halls.',
                'intricate polyphonic voicings were introduced into Harlem big-band brass arrangements by composer Lillian Carter.',
                'the commercial dance halls of Harlem soon echoed with composer Lillian Carter’s intricate polyphonic brass arrangements.'
            ],
            'A',
            'Bẫy 750+ cực hiểm: **Possessive Dangling Modifier**! Cụm mở đầu `Trained in classical counterpoint at the Boston Conservatory...` mô tả CON NGƯỜI được đào tạo tại nhạc viện — tức **composer Lillian Carter**. Bẫy B (`Lillian Carter’s big-band brass arrangements`) đặt tên Lillian Carter ngay sau dấu phẩy nhưng ở dạng SỞ HỮU CÁCH, khiến chủ ngữ thật của câu lại là `arrangements` (các bản phối không thể "được đào tạo ở Nhạc viện Boston"!). Duy nhất A đặt đúng `composer Lillian Carter` làm chủ ngữ thật!',
            'Cảnh giác bẫy sở hữu cách (Possessive Trap): `Name’s + Noun` thì chủ ngữ là `Noun`, KHÔNG phải `Name`! Luôn kiểm tra danh từ trung tâm đứng trước động từ chính!',
            [
                ('Đáp án đúng', 'Chủ ngữ thật "composer Lillian Carter" đứng ngay sau dấu phẩy khớp hoàn hảo với cụm "Trained in classical counterpoint...".'),
                ('Possessive Dangling Modifier', 'Chủ ngữ thật là "arrangements" (những bản phối) — bản phối không thể được đào tạo tại Nhạc viện Boston!'),
                ('Passive Dangling Modifier', 'Chủ ngữ là "intricate polyphonic voicings" — hòa âm không thể theo học nhạc viện.'),
                ('Dangling Modifier', 'Chủ ngữ là "the commercial dance halls" — vũ trường không thể được đào tạo về đối âm cổ điển.'),
            ]
        ),

        # --- Q23-Q25: Expression of Ideas — Transitions (Hard / Elite) ---
        q_item(
            'm7_m2h_q23', 23, 'Expression of Ideas', 'Transitions', 'Hard',
            '<p>During unusually violent spring snowmelts, individual timber-and-mud beaver dams along steep mountain tributaries occasionally breach under the pressure of surging runoff. ______, watershed engineers observe that even partially breached cascades of beaver ponds still dissipate downstream flood peaks far more effectively than bare, channelized streambeds.</p>',
            'Which choice completes the text with the most logical transition?',
            ['Accordingly', 'In other words', 'Likewise', 'Nonetheless'],
            'D',
            'Câu 1 nhượng bộ điểm hạn chế: đập hải ly đôi khi bị vỡ trong đợt băng tan cực lớn. Câu 2 đảo ngược kỳ vọng tiêu cực đó: ngay cả chuỗi ao có đập bị vỡ một phần vẫn cắt đỉnh lũ hạ lưu tốt hơn nhiều so với lòng suối trơ trụi → Quan hệ Nhượng bộ – Phản kỳ vọng → **"Nonetheless"** (D)!',
            'Cấu trúc "Hạn chế X có xảy ra; [Transition], lợi ích Y vẫn vượt trội" → chốt nhóm nhượng bộ "Nonetheless / Nevertheless / Even so".',
            [
                ('Wrong Relationship (Cause-Effect)', 'Accordingly (= Therefore) sai vì việc đập vỡ không phải nguyên nhân khiến nó cắt lũ tốt hơn.'),
                ('Restatement Trap', 'Câu 2 không diễn đạt lại câu 1 mà đưa ra thực tế tích cực trái kỳ vọng.'),
                ('Wrong Relationship (Similarity)', 'Likewise chỉ sự tương đồng song song — sai hướng đối lập.'),
                ('Đáp án đúng', 'Nonetheless kết nối chuẩn xác sự nhượng bộ ở câu 1 với hiệu quả giảm lũ đáng kể vẫn được duy trì ở câu 2.'),
            ]
        ),
        q_item(
            'm7_m2h_q24', 24, 'Expression of Ideas', 'Transitions', 'Elite (750+)',
            '<p>Freshwater unionid mussels can steadily strip suspended synthetic fibers from flowing urban rivers and lock them into dense riverbed deposits. ______, deep sediment cores extracted beneath long-established mussel reefs in the Ohio River basin preserve continuous layers of trapped microplastics dating back to the 1960s.</p>',
            'Which choice completes the text with the most logical transition?',
            ['Nevertheless', 'Conversely', 'Indeed', 'Instead'],
            'C',
            'Câu 1 nêu khả năng khóa vi sợi nhựa vào trầm tích đáy sông của trai nước ngọt. Câu 2 XÁC NHẬN VÀ NÂNG TẦM bằng chứng thực địa cực mạnh (lõi trầm tích dưới bãi trai lâu năm lưu giữ các lớp vi nhựa bị khóa liên tục từ tận thập niên 1960) → Quan hệ Xác nhận – Củng cố tăng tiến → **"Indeed"** (C)!',
            'Thấy câu 2 cung cấp bằng chứng thực tế xác nhận và đẩy mạnh hơn nữa khẳng định ở câu 1 (không có phủ định, không đối lập) → chọn "Indeed"!',
            [
                ('False Contrast', 'Nevertheless sai hoàn toàn vì hai câu cùng chiều khẳng định năng lực giữ vi nhựa.'),
                ('False Contrast', 'Conversely chỉ sự đảo ngược — trái hoàn toàn mạch củng cố dữ liệu.'),
                ('Đáp án đúng', 'Indeed xác nhận và khuếch đại trực tiếp nhận định ở câu 1 bằng chứng cứ lõi trầm tích kéo dài nhiều thập kỷ.'),
                ('Wrong Relationship (Replacement)', 'Instead chỉ dùng sau mệnh đề phủ định để nêu phương án thay thế.'),
            ]
        ),
        q_item(
            'm7_m2h_q25', 25, 'Expression of Ideas', 'Transitions', 'Elite (750+)',
            '<p>Linguists documenting endangered Ancash Quechua dialects aim to capture spontaneous conversational evidentiality rather than stilted word-for-word translations elicited by formal Spanish questionnaires. ______, field teams in Huaraz now train local community members to record unscripted kitchen-table storytelling and marketplace conversations.</p>',
            'Which choice completes the text with the most logical transition?',
            ['Regardless', 'To that end', 'By comparison', 'Even so'],
            'B',
            'Câu 1 nêu rõ MỤC TIÊU NGHIÊN CỨU (`aim to capture spontaneous conversational evidentiality...`). Câu 2 nêu BIỆN PHÁP HÀNH ĐỘNG CỤ THỂ nhằm thực hiện mục tiêu đó (`train local community members to record unscripted storytelling...`) → Nhằm đạt được mục tiêu ấy = **"To that end"** (B)!',
            'Dấu hiệu vàng 750+ của "To that end": Câu 1 có động từ mục tiêu (`aim to / seek to / hope to`) → Câu 2 nêu bước hành động cụ thể phục vụ mục tiêu đó!',
            [
                ('False Contrast', 'Regardless (= bất chấp điều đó) sai hoàn toàn vì câu 2 thực thi trực tiếp mục tiêu câu 1.'),
                ('Đáp án đúng', 'To that end (= nhằm phục vụ mục tiêu đó) nối khít ý định thu thập hội thoại tự nhiên với phương pháp ghi âm đời thực ở câu 2.'),
                ('Wrong Relationship (Comparison)', 'By comparison so sánh hai đối tượng khác nhau — không có phép so sánh ngang hàng ở đây.'),
                ('False Concession', 'Even so chỉ sự tương phản bất chấp tiền đề — ngược hoàn toàn quan hệ mục tiêu – giải pháp.'),
            ]
        ),

        # --- Q26-Q27: Expression of Ideas — Rhetorical Synthesis (Hard / Elite) ---
        q_item(
            'm7_m2h_q26', 26, 'Expression of Ideas', 'Rhetorical Synthesis', 'Hard',
            '''<p>While researching a topic, a student has taken the following notes:</p>
            <ul>
              <li>Transmission spectroscopy measures how an exoplanet’s atmosphere absorbs specific wavelengths of starlight as the planet crosses in front of its host star.</li>
              <li>Rocky exoplanets orbiting small, cool red-dwarf stars produce relatively large transit signals, making them prime targets for space telescopes.</li>
              <li>Red-dwarf stars frequently host uneven patches of cooler dark starspots and hotter bright faculae on their surfaces.</li>
              <li>When an exoplanet transits an unspotted strip of a spotted red dwarf, water vapor inside the cool starspots outside the transit chord can imprint false water-absorption features onto the spectrum—a distortion called the transit light source effect.</li>
            </ul>''',
            'The student wants to explain how stellar surface features can generate misleading atmospheric readings during transmission spectroscopy of exoplanets orbiting red-dwarf stars. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
            [
                'Because red-dwarf stars often carry cool starspots containing water vapor alongside brighter surface patches, a transiting planet passing across an unspotted region can trigger the transit light source effect, imprinting false water-absorption signals onto the planet’s transmission spectrum.',
                'Transmission spectroscopy detects atmospheric gases by measuring the wavelengths of starlight absorbed as an exoplanet transits in front of its host star.',
                'Space telescopes prioritize rocky exoplanets orbiting small, cool red-dwarf stars because those worlds produce proportionally large transit signals.',
                'Uneven patches of cooler dark starspots and hotter bright faculae occur commonly on the surfaces of small, cool red-dwarf stars.'
            ],
            'A',
            'Goal-First SOP: Giải thích CÁCH THỨC đặc điểm bề mặt ngôi sao gây ra tín hiệu khí quyển sai lệch trong quang phổ truyền qua của hành tinh quanh sao lùn đỏ. B chỉ định nghĩa quang phổ truyền qua; C chỉ nói vì sao sao lùn đỏ là mục tiêu ưu tiên; D chỉ nói sao lùn đỏ có vết đen/đốm sáng mà không giải thích cơ chế tạo tín hiệu giả! Duy nhất A kết nối trọn cơ chế: vết đen lạnh chứa hơi nước + hành tinh đi qua vùng không vết đen → hiệu ứng nguồn sáng quá cảnh (transit light source effect) → in dấu hấp thụ nước giả lên quang phổ! Chọn A!',
            'Mục tiêu có động từ "explain HOW [stellar features] generate [misleading readings]" → đáp án phải chứa trọn cơ chế nhân quả dẫn tới tín hiệu giả!',
            [
                ('Đáp án đúng', 'Tổng hợp đầy đủ chuỗi cơ chế từ vết đen sao chứa hơi nước đến hiệu ứng nguồn sáng quá cảnh tạo tín hiệu hấp thụ giả.'),
                ('Wrong Synthesis Goal', 'Chỉ định nghĩa chung về quang phổ truyền qua, hoàn toàn bỏ qua vết đen sao và tín hiệu giả.'),
                ('Wrong Synthesis Goal', 'Chỉ nêu lý do sao lùn đỏ là mục tiêu ưu tiên, không nói đến sự gây nhiễu.'),
                ('Missing Mechanism/Effect', 'Chỉ nêu sự tồn tại của vết đen và đốm sáng trên sao lùn đỏ, chưa giải thích chúng tạo tín hiệu sai lệch ra sao.'),
            ]
        ),
        q_item(
            'm7_m2h_q27', 27, 'Expression of Ideas', 'Rhetorical Synthesis', 'Elite (750+)',
            '''<p>While researching a topic, a student has taken the following notes:</p>
            <ul>
              <li>Radiocarbon dating reconstructs past glacial retreats by measuring carbon-14 decay in preserved organic fossils such as wood or peat.</li>
              <li>High-altitude alpine moraines left behind by retreating glaciers often consist of bare granite boulders lacking any organic material.</li>
              <li>Once melting ice uncovers a granite boulder, high-energy cosmic rays strike quartz grains on the rock’s surface and steadily produce the rare isotope beryllium-10.</li>
              <li>By measuring accumulated beryllium-10 concentrations in surface quartz, geomorphologists can calculate precisely how many millennia ago the glacier abandoned that moraine.</li>
            </ul>''',
            'The student wants to explain how cosmogenic beryllium-10 dating overcomes a specific limitation of radiocarbon dating in reconstructing ancient glacier retreats. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
            [
                'When retreating alpine glaciers abandon high-altitude moraines, they often leave behind bare granite boulders containing quartz grains.',
                'Radiocarbon dating relies on measuring the decay of carbon-14 in preserved organic fossils such as ancient wood and peat.',
                'Whereas radiocarbon dating requires organic fossils that are often absent from barren alpine moraines, cosmogenic dating measures cosmic-ray-produced beryllium-10 accumulated directly in exposed granite quartz to determine when a glacier retreated.',
                'High-energy cosmic rays generate the rare isotope beryllium-10 whenever they strike quartz minerals on the surface of an exposed rock.'
            ],
            'C',
            'Goal-First SOP: Giải thích cách định tuổi bằng beryllium-10 KHẮC PHỤC HẠN CHẾ CỤ THỂ của định tuổi carbon phóng xạ (radiocarbon) khi tái dựng thời điểm sông băng rút lui. Kiểm tra đủ 3 mảnh bắt buộc: [1] Hạn chế của radiocarbon (cần hóa thạch hữu cơ vốn thường vắng bóng trên băng tích đá trần); [2] Cơ chế beryllium-10 (đo đồng vị do tia vũ trụ tạo trực tiếp trong thạch anh đá granite phơi lộ); [3] Mục đích xác định thời điểm sông băng rút! A, B, D mỗi câu đều khuyết ít nhất 2 mảnh. Duy nhất C tích hợp trọn vẹn cả 3 mảnh! Chọn C!',
            'Goal có cụm "overcomes a specific limitation of X" → Đáp án BẮT BUỘC phải gọi tên hạn chế của X (thiếu hóa thạch hữu cơ) VÀ chỉ rõ cơ chế thay thế của Y (beryllium-10 trong thạch anh)!',
            [
                ('Incomplete Synthesis', 'Chỉ mô tả tảng đá granite trên băng tích, bỏ qua cả radiocarbon lẫn beryllium-10.'),
                ('One-Sided Information', 'Chỉ mô tả nguyên lý radiocarbon, không nhắc tới hạn chế hay phương pháp beryllium-10.'),
                ('Đáp án đúng', 'Khớp hoàn chỉnh cả 3 yêu cầu: hạn chế thiếu vật chất hữu cơ của radiocarbon, cơ chế đo beryllium-10 trong thạch anh, và việc xác định mốc băng rút.'),
                ('Missing Contrast/Limitation', 'Chỉ nêu cơ chế vật lý tạo beryllium-10 mà không liên hệ tới hạn chế của radiocarbon hay thời điểm băng rút.'),
            ]
        ),
    ]
