# -*- coding: utf-8 -*-
"""
Full-Length Adaptive Mock Test #1 — Module 1 (27 Qs, Medium/Hard Mix, 32 min)
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
            'm1_m1_q1', 1, 'Craft and Structure', 'Words in Context', 'Medium',
            '<p>Astronomers observing Saturn’s moon Titan once assumed its thick nitrogen haze was completely static; however, twenty years of infrared telescope imaging have shown that methane storm clouds ______ across its polar regions whenever the moon’s long seasons shift.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            ['proliferate', 'stagnate', 'diminish', 'evaporate'],
            'A',
            'Contrast Clue: "once assumed... completely static; however..." → trái ngược với "đứng yên bất động", các đám mây bão metan SINH SÔI / XUẤT HIỆN DỒI DÀO khi mùa chuyển giao → "proliferate" (A).',
            'Đối lập trực tiếp với "completely static" (bất động) + bối cảnh bão hình thành theo mùa → chọn động từ chỉ sự gia tăng/sinh sôi.',
            [
                ('Đáp án đúng', 'proliferate = sinh sôi, gia tăng mạnh mẽ — đối lập sắc nét với giả định bầu khí quyển tĩnh lặng.'),
                ('Opposite Meaning', 'stagnate = trì trệ đứng yên — trùng nghĩa với "static", sai sau "however".'),
                ('Wrong Direction', 'diminish = thu hẹp giảm bớt — không hợp bối cảnh bão mây xuất hiện khi chuyển mùa.'),
                ('Wrong Context', 'evaporate = bốc hơi biến mất — trái ngược với sự xuất hiện của các đám mây bão.'),
            ]
        ),
        q_item(
            'm1_m1_q2', 2, 'Craft and Structure', 'Words in Context', 'Medium',
            '<p>Although conductor Elena Rostova’s rehearsal remarks were remarkably ______—rarely exceeding a single crisp sentence per movement—orchestra players praised how immediately her brief comments clarified complex rhythmic shifts.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            ['verbose', 'succinct', 'circuitous', 'erratic'],
            'B',
            'Mirror Clue ngay trong cặp gạch ngang: "rarely exceeding a single crisp sentence per movement" + "brief comments clarified" → NGẮN GỌN, SÚC TÍCH → "succinct" (B).',
            'Cụm "rarely exceeding a single crisp sentence" là định nghĩa nguyên văn của "succinct" (súc tích).',
            [
                ('Opposite Meaning', 'verbose = dài dòng thừa chữ — trái nghĩa hoàn toàn với "single crisp sentence".'),
                ('Đáp án đúng', 'succinct = ngắn gọn súc tích nhưng rõ ràng — khớp 100% với manh mối sau gạch ngang.'),
                ('Opposite Meaning', 'circuitous = vòng vo dài dòng.'),
                ('Wrong Tone', 'erratic = thất thường hỗn loạn — trái với lời khen "immediately clarified".'),
            ]
        ),
        q_item(
            'm1_m1_q3', 3, 'Craft and Structure', 'Words in Context', 'Hard',
            '<p>Archaeologists mapping the Inca road network across Peru’s Andes marvel at how imperial stonemasons did not force uniform straight highways across treacherous cliffs; instead, their paving designs remained highly ______, adapting effortlessly from suspension rope bridges over gorges to stepped granite staircases up sheer ridges.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            ['inflexible', 'monolithic', 'malleable', 'adaptable'],
            'D',
            'Contrast + Restatement Clue: đối lập với "did not force uniform straight highways" + giải thích ngay sau "adapting effortlessly from suspension rope bridges... to stepped granite staircases" → LINH HOẠT THÍCH ỨNG → "adaptable" (D). Chú ý bẫy C ("malleable"): malleable thường dùng cho kim loại dễ dát mỏng hoặc tâm lý dễ bị người khác uốn nắn/tác động, còn "designs... adapting effortlessly" khớp chuẩn 100% với "adaptable" (hoặc "flexible").',
            'Khi có 2 từ cùng chiều (malleable vs. adaptable), kiểm tra Collocation Fit: kỹ thuật thiết kế cầu/đường thay đổi theo địa hình dùng "adaptable", không dùng "malleable"!',
            [
                ('Opposite Meaning', 'inflexible = cứng nhắc — trái ngược hoàn toàn với "adapting effortlessly".'),
                ('Opposite Meaning', 'monolithic = đồng nhất nguyên khối — đồng nghĩa với "uniform" ở vế phủ định.'),
                ('Collocation Mismatch', 'malleable = dễ dát mỏng (kim loại) hoặc dễ bị sai khiến (tính cách), không chuẩn cho phương án kỹ thuật đường bộ thích ứng địa hình.'),
                ('Đáp án đúng', 'adaptable = linh hoạt thích ứng — phản chiếu trực tiếp mệnh đề "adapting effortlessly".'),
            ]
        ),
        q_item(
            'm1_m1_q4', 4, 'Craft and Structure', 'Words in Context', 'Hard',
            '<p>During municipal hearings over the proposed harbor tramway, merchants expressed ______ enthusiasm: while welcoming the prospect of greater pedestrian foot traffic along the waterfront, they worried that two years of track construction might disrupt seasonal deliveries.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            ['unbridled', 'indifferent', 'tempered', 'unanimous'],
            'C',
            'Colon Clue: "while welcoming X, they worried that Y" → sự hào hứng CÓ CHỪNG MỰC / ĐƯỢC TIẾT CHẾ bởi nỗi lo thi công → Nghĩa thứ cấp học thuật của "tempered" = moderated / restrained (được làm dịu bớt, có chừng mực) → Chọn C!',
            'Nhớ nghĩa thứ cấp vàng: tempered enthusiasm = qualified enthusiasm (sự hào hứng chừng mực đi kèm dè dặt).',
            [
                ('Too Extreme', 'unbridled = không kiềm chế, nhiệt liệt tuyệt đối — trái với vế lo ngại thi công.'),
                ('Contradiction', 'indifferent = thờ ơ — mâu thuẫn với từ "enthusiasm" và "welcoming".'),
                ('Đáp án đúng', 'tempered (nghĩa thứ cấp: được tiết chế, chừng mực) khớp hoàn hảo với thế cân bằng "welcoming X... worried Y".'),
                ('Too Extreme', 'unanimous = nhất trí hoàn toàn — không phản ánh sự dè dặt song song với hào hứng.'),
            ]
        ),
        q_item(
            'm1_m1_q5', 5, 'Craft and Structure', 'Words in Context', 'Hard',
            '<p>Long dismissed by nineteenth-century marine naturalists as barren mudflats devoid of complex life, temperate seagrass meadows are now recognized as ______ carbon sinks capable of locking away organic matter per hectare faster than many tropical rainforests.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            ['prodigious', 'negligible', 'transient', 'tenuous'],
            'A',
            'Contrast + Restatement Clue: đối lập với "barren mudflats devoid of complex life" + chứng minh phía sau "locking away organic matter faster than many tropical rainforests" → TO LỚN, PHI THƯỜNG → "prodigious" (A)!',
            'Nhóm 3 từ B (negligible), C (transient), D (tenuous) đều mang sắc thái nhỏ bé/yếu ớt — chỉ duy nhất A (prodigious = phi thường to lớn) mang sắc thái tích cực mạnh!',
            [
                ('Đáp án đúng', 'prodigious = đồ sộ, phi thường về quy mô/hiệu suất — khớp tuyệt đối với năng lực khóa carbon vượt cả rừng mưa nhiệt đới.'),
                ('Opposite Meaning', 'negligible = nhỏ đến mức không đáng kể — trái ngược hoàn toàn.'),
                ('Wrong Meaning', 'transient = ngắn ngủi thoáng qua — sai với "locking away".'),
                ('Wrong Meaning', 'tenuous = mong manh lỏng lẻo — trái nghĩa.'),
            ]
        ),

        # --- Q6-Q7: Craft and Structure — Text Structure and Purpose ---
        q_item(
            'm1_m1_q6', 6, 'Craft and Structure', 'Text Structure and Purpose', 'Medium',
            '<p>In eighteenth-century Venice, theater architects discovered that plastering auditorium walls over hollow wooden cavities rather than solid masonry significantly warmed the tone of string orchestras. <u>Much like the resonant soundboard of a cello, these concealed air chambers vibrated sympathetically with low-frequency notes, preventing the brass and percussion from drowning out delicate bowed melodies.</u> Today, acoustic designers renovating modern halls still borrow this Venetian cavity principle to achieve balanced orchestral projection.</p>',
            'Which choice best describes the function of the underlined sentence in the text as a whole?',
            [
                'It argues that eighteenth-century Venetian cellos produced louder melodies than modern string instruments.',
                'It explains the physical acoustic mechanism by which the hollow wall cavities improved orchestral sound quality.',
                'It identifies an architectural defect that forced modern designers to abandon Venetian plaster techniques.',
                'It contrasts the construction costs of hollow wooden framing with those of solid brick masonry.'
            ],
            'B',
            'Câu 1 nêu phát hiện thực tiễn (trát tường lên khoang gỗ rỗng làm ấm âm sắc dàn dây). Câu gạch chân giải thích CƠ CHẾ VẬT LÝ tạo nên hiệu ứng đó (ví như thùng cộng hưởng đàn cello, khoang khí rung cộng hưởng với nốt trầm giúp cân bằng dàn dây với bộ đồng/gõ) → Chọn B!',
            'Câu giữa nằm sau câu nêu hiệu quả thường đóng vai trò giải thích "TẠI SAO / BẰNG CƠ CHẾ NÀO" hiệu quả đó xảy ra.',
            [
                ('Literal Misreading', 'Cây đàn cello chỉ được dùng làm phép so sánh ("Much like..."), không phải so sánh độ lớn âm lượng đàn cổ và đàn hiện đại.'),
                ('Đáp án đúng', 'Giải thích cơ chế cộng hưởng âm học giúp khoang rỗng cải thiện độ ấm và cân bằng âm thanh.'),
                ('Contradiction', 'Câu cuối khẳng định kiến trúc sư ngày nay VẪN áp dụng nguyên lý này ("still borrow").'),
                ('Out of Scope', 'Không đề cập chi phí xây dựng.'),
            ]
        ),
        q_item(
            'm1_m1_q7', 7, 'Craft and Structure', 'Text Structure and Purpose', 'Hard',
            '<p><i>The following text is adapted from an 1894 maritime novel. Captain Halvorsen has just anchored his wooden schooner in a sheltered Norwegian fjord after three days battling a North Sea gale.</i><br/>No cheer rose from the soaked deckhands as the anchor chain rattled to a halt; they simply leaned against the wet bulwarks, staring up at the motionless pine ridges that walled out the wind. For seventy-two hours the compass binnacle and the shrieking rigging had demanded every ounce of thought. Now, with only the gentle lap of black fjord water against the hull, Halvorsen felt the tight iron knot behind his shoulders dissolve into a weariness so profound it almost resembled gratitude.</p>',
            'Which choice best states the main purpose of the text?',
            [
                'To criticize the deckhands for failing to celebrate the captain’s skillful navigation through a severe storm.',
                'To describe the technical procedures sailors used in 1894 to secure a schooner’s anchor chain.',
                'To convey the quiet, exhausted sense of relief shared by Captain Halvorsen and his crew upon reaching calm shelter after an arduous storm.',
                'To explain why Norwegian fjords were historically considered hazardous anchorage sites for wooden vessels.'
            ],
            'C',
            'Toàn đoạn khắc họa khoảnh khắc im lặng kiệt sức nhưng nhẹ nhõm sâu sắc sau 72 giờ căng thẳng chống bão: thủy thủ không reo hò mà lặng lẽ tựa lan can ngắm rặng thông đứng gió; nút thắt căng thẳng trên vai thuyền trưởng tan chảy thành sự mệt mỏi sâu lắng gần như lòng biết ơn → Chọn C!',
            'Đọc câu cuối trích đoạn văn học ("weariness so profound it almost resembled gratitude") để chốt chính xác tông cảm xúc chủ đạo!',
            [
                ('Wrong Tone / Distortion', 'Việc không reo hò thể hiện sự kiệt sức trầm lắng chứ không phải lời chê trách thủy thủ.'),
                ('Out of Scope / Literal', 'Không hướng dẫn kỹ thuật thả neo năm 1894.'),
                ('Đáp án đúng', 'Bắt trọn cảm xúc mệt mỏi nhưng nhẹ nhõm sâu sắc khi thoát khỏi 72 giờ bão tố về nơi neo đậu bình yên.'),
                ('Contradiction', 'Vịnh hẹp (sheltered fjord) chắn gió bình yên chứ không nguy hiểm.'),
            ]
        ),

        # --- Q8: Craft and Structure — Cross-Text Connections ---
        q_item(
            'm1_m1_q8', 8, 'Craft and Structure', 'Cross-Text Connections', 'Hard',
            '<p><b>Text 1</b><br/>Urban geographer Dr. Leonid Kovacs contends that constructing high-speed commuter rail links between metropolitan capitals and distant rural towns uniformly revitalizes rural economies by enabling high-earning urban professionals to relocate to affordable villages while keeping their city jobs.</p><p><b>Text 2</b><br/>Studying twelve provincial towns in Spain and Japan connected to bullet-train corridors over a twenty-year span, regional economist Dr. Mei Tanaka found that while towns with distinct tourism assets or university campuses gained new businesses and tax revenue, smaller agricultural towns without local amenities often lost retail shoppers—who rode the fast train straight to the capital’s department stores—while facing steeper local housing prices.</p>',
            'Based on the texts, how would Dr. Mei Tanaka (Text 2) most likely respond to Dr. Leonid Kovacs’s claim (Text 1)?',
            [
                'By asserting that bullet-train corridors have never generated economic benefits for any provincial town in Spain or Japan.',
                'By claiming that rural residents refuse to commute to metropolitan capitals on high-speed rail lines.',
                'By agreeing that high-speed rail automatically lowers local housing prices in connected agricultural villages.',
                'By arguing that the economic effects of high-speed rail are uneven rather than uniformly beneficial, depending heavily on whether a town already possesses local economic attractions.'
            ],
            'D',
            'Text 1 dùng từ cực đoan "uniformly revitalizes" (hồi sinh đồng đều mọi thị trấn nông thôn). Text 2 phân tách 2 nhóm kết quả trái ngược: thị trấn có du lịch/đại học → hưởng lợi; thị trấn nông nghiệp thiếu tiện ích → mất khách mua sắm địa phương và giá nhà tăng cao → Bác bỏ chữ "uniformly", khẳng định tác động KHÔNG ĐỒNG ĐỀU tùy nền tảng sẵn có của thị trấn (D)!',
            'Mỗi khi Text 1 chứa từ tuyệt đối ("uniformly / always / solely") và Text 2 chia thành "nhóm A có lợi, nhóm B chịu thiệt" → đáp án đúng là "uneven / depends on local factors"!',
            [
                ('Overstated Conflict', '"never generated" trái với vế Text 2 khẳng định các thị trấn có du lịch/đại học ĐÃ tăng doanh nghiệp và thuế.'),
                ('Contradiction', 'Text 2 nói dân thị trấn nhỏ bắt tàu nhanh thẳng tới thủ đô mua sắm — họ sử dụng tàu rất nhiều.'),
                ('Reversed Logic', 'Text 2 nói giá nhà địa phương TĂNG cao hơn ("steeper local housing prices"), không phải giảm.'),
                ('Đáp án đúng', 'Khớp hoàn hảo phản biện của Tanaka: tác động không đồng đều, phụ thuộc mạnh vào tài nguyên/tiện ích sẵn có của từng thị trấn.'),
            ]
        ),

        # --- Q9-Q10: Information and Ideas — Central Ideas and Details ---
        q_item(
            'm1_m1_q9', 9, 'Information and Ideas', 'Central Ideas and Details', 'Medium',
            '<p>Along rocky Pacific tidal zones, sea stars such as <i>Pisaster ochraceus</i> serve as "keystone predators" whose ecological impact far outweighs their modest population size. By selectively preying on fast-growing California mussels that would otherwise blanket every square inch of rock, sea stars preserve open patches of intertidal stone where barnacles, limpets, sea anemones, and dozens of algae species can coexist.</p>',
            'Which choice best states the main idea of the text?',
            [
                'By keeping aggressive mussel populations in check, sea stars maintain habitat space that supports rich intertidal biodiversity.',
                'California mussels are the only marine organisms capable of surviving along rocky Pacific tidal zones.',
                'Sea star populations have grown too large along the Pacific coast, crowding out native barnacles and anemones.',
                'Intertidal algae species provide the primary food source for predatory sea stars such as <i>Pisaster ochraceus</i>.'
            ],
            'A',
            'Ý chính toàn đoạn: Sao biển là "loài ăn thịt chủ chốt" (keystone predator) — nhờ ăn bớt vẹm California vốn dễ phủ kín mặt đá, sao biển giữ lại khoảng đá trống giúp hàng chục loài sinh vật gian triều khác cùng tồn tại (đa dạng sinh học) → Chọn A!',
            'Khớp trực tiếp cơ chế sinh thái: Sea stars eat dominant mussels → keep rock space open → boost biodiversity.',
            [
                ('Đáp án đúng', 'Tóm gọn chính xác cơ chế khống chế quần thể vẹm của sao biển nhằm bảo vệ không gian sống và đa dạng sinh học.'),
                ('Contradiction', 'Bài liệt kê cả hà, ốc nón, hải quỳ và hàng chục loài tảo cùng sống ở vùng đá này.'),
                ('Reversed Logic', 'Bài nói quần thể sao biển khiêm tốn ("modest population size") và chính VẸM mới là loài lấn chiếm đá, không phải sao biển.'),
                ('Contradiction', 'Sao biển ăn vẹm California, không nói tảo là nguồn thức ăn chính của sao biển.'),
            ]
        ),
        q_item(
            'm1_m1_q10', 10, 'Information and Ideas', 'Central Ideas and Details', 'Hard',
            '<p>When constructing monumental stone plazas at Tiwanaku near Lake Titicaca around 600 CE, Andean builders joined multi-ton andesite blocks using I-shaped copper-arsenic-nickel clamps poured molten directly into carved T-shaped sockets. Metallurgical tests conducted in 2021 showed that portable ceramic crucibles were carried right up to the masonry walls so workers could smelt and cast each metal cramp in place, creating a flexible seismic lock that held stonework aligned during Andean earthquakes.</p>',
            'According to the text, why did Tiwanaku builders carry portable ceramic crucibles directly to the stone walls?',
            [
                'To transport drinking water from Lake Titicaca to workers carving andesite quarries.',
                'To smelt and pour molten metal clamps directly into carved stone sockets on site, locking blocks together against seismic shaking.',
                'To fire decorative painted pottery vessels buried beneath the ceremonial plazas.',
                'To heat and soften multi-ton andesite blocks before cutting them into rectangular shapes.'
            ],
            'B',
            'Câu hỏi Specific Detail: Tìm đúng câu chứa "portable ceramic crucibles" → "so workers could smelt and cast each metal cramp in place, creating a flexible seismic lock that held stonework aligned during Andean earthquakes" → Paraphrase hoàn hảo ở B!',
            'Bám sát ngay mệnh đề chỉ mục đích "so workers could..." đứng liền sau từ khóa câu hỏi.',
            [
                ('Out of Scope', 'Không hề nói dùng nồi gốm để chở nước uống.'),
                ('Đáp án đúng', 'Paraphrase trực tiếp mục đích nung chảy và đúc chốt kim loại ngay tại chỗ vào khe đá để chống rung chấn động đất.'),
                ('Out of Scope', 'Không nhắc gốm trang trí chôn dưới quảng trường.'),
                ('Fact Distortion', 'Nồi gốm dùng nấu chảy hợp kim đồng–asen–niken, KHÔNG phải làm mềm đá andesite.'),
            ]
        ),

        # --- Q11-Q12: Information and Ideas — Command of Evidence (Textual) ---
        q_item(
            'm1_m1_q11', 11, 'Information and Ideas', 'Command of Evidence (Textual)', 'Hard',
            '<p>Astronomers studying fast-spinning asteroids in the main belt noticed that several kilometer-wide bodies shed sudden plumes of fine dust despite orbiting far too close to the Sun to retain volatile surface ice. Planetary physicist Dr. Ananya Bose hypothesized that rapid sunlight-driven spin acceleration—known as the YORP effect—can push loosely bound "rubble-pile" asteroids past their rotational breakup limit, flinging dust directly off their equators rather than dust being blasted free by micrometeorite impacts.</p>',
            'Which finding, if true, would most directly support Dr. Ananya Bose’s hypothesis?',
            [
                'Spectral observations confirm that main-belt asteroids contain high percentages of iron and magnesium silicates.',
                'Micrometeorite craters are evenly distributed across both the poles and equators of slowly rotating main-belt asteroids.',
                'High-resolution imagery of three active dust-shedding asteroids reveals that all three rotate near their critical breakup speed and eject narrow dust streams strictly along their equatorial planes rather than from random impact craters.',
                'Several comets originating in the outer Kuiper Belt release broad tails of water vapor whenever they approach the inner solar system.'
            ],
            'C',
            'Khóa giả thuyết Bose: Bụi bị văng ra do QUAY QUÁ NHANH VƯỢT NGƯỠNG VỠ (rotational breakup limit) khiến bụi phóng từ ĐƯỜNG XÍCH ĐẠO (equators), KHÔNG phải do thiên thạch nhỏ đâm ngẫu nhiên. Đáp án C xác thực cả 2 chữ ký đặc trưng của cơ chế quay: cả 3 tiểu hành tinh đều quay sát tốc độ vỡ giới hạn VÀ phun luồng bụi hẹp ĐÚNG DỌC MẶT PHẲNG XÍCH ĐẠO thay vì từ hố va chạm ngẫu nhiên! Chọn C!',
            'Soi đúng chữ ký không gian của giả thuyết: quay cực nhanh + phun đúng đường xích đạo (loại trừ va chạm ngẫu nhiên)!',
            [
                ('Adjacent Topic Drift', 'Thành phần khoáng silicat không phân biệt được nguyên nhân phóng bụi do quay nhanh hay do va chạm.'),
                ('Irrelevant Subject', 'Tiểu hành tinh quay chậm không kiểm chứng cơ chế của nhóm quay nhanh phun bụi.'),
                ('Đáp án đúng', 'Khớp đồng thời hai bằng chứng then chốt: quay sát ngưỡng vỡ và bụi chỉ phun dọc xích đạo chứ không từ hố va chạm ngẫu nhiên.'),
                ('Irrelevant Subject', 'Sao chổi giàu băng vùng ngoài thuộc cơ chế thăng hoa băng khác hoàn toàn.'),
            ]
        ),
        q_item(
            'm1_m1_q12', 12, 'Information and Ideas', 'Command of Evidence (Textual)', 'Hard',
            '<p>In an analysis of the 1911 stage play <i>The Foundry Orchestra</i>, a theater critic argues that factory foreman Arthur views the newly formed workers’ brass band not merely as an evening pastime, but as a rare space where exhausted laborers reclaim personal dignity and shared pride.</p>',
            'Which quotation from Arthur in <i>The Foundry Orchestra</i> most effectively illustrates the critic’s claim?',
            [
                '“The foundry whistle blows at six sharp, and anyone arriving two minutes late forfeits a quarter of his daily wage.”',
                '“We purchased two secondhand cornets and a dented trombone from a pawnbroker near the canal dock last November.”',
                '“Our rehearsals sometimes run past nine o’clock on Thursdays, which leaves the younger apprentices yawning through Friday morning.”',
                '“All day at the blast furnace they call us by stamped brass payroll numbers; only when we lift our horns in the hall does a man stand tall again and hear his neighbor answer in harmony.”'
            ],
            'D',
            'Checklist 2 vế từ Claim: [1] Không chỉ là trò giải trí đơn thuần + [2] Không gian hiếm hoi giúp công nhân kiệt sức lấy lại PHẨM GIÁ CÁ NHÂN và NIỀM TỰ HÀO CHUNG ("reclaim personal dignity and shared pride"). A, B, C chỉ kể quy định xưởng, mua nhạc cụ, giờ tập khuya. Duy nhất D đối chiếu sắc nét: cả ngày ở lò cao bị gọi bằng mã số thẻ đồng ↔ chỉ khi nâng kèn lên người thợ mới đứng thẳng kiêu hãnh và hòa âm cùng đồng nghiệp! Chọn D!',
            'Tìm trích dẫn thể hiện rõ sự chuyển biến tâm thế từ bị vật hóa ("payroll numbers") sang phẩm giá & gắn kết ("stand tall... in harmony")!',
            [
                ('Irrelevant Detail', 'Chỉ nói quy định phạt đi làm muộn tại xưởng.'),
                ('Topic Keyword Lure', 'Có nhắc nhạc cụ kèn đồng nhưng chỉ kể chuyện mua đồ cũ.'),
                ('Half-Match / Off-Point', 'Chỉ nhắc việc tập khuya làm thợ học việc buồn ngủ.'),
                ('Đáp án đúng', 'Minh họa xuất sắc cả phẩm giá cá nhân ("stand tall again" thoát khỏi mã số thẻ lương) lẫn niềm tự hào gắn kết ("hear his neighbor answer in harmony").'),
            ]
        ),

        # --- Q13-Q14: Information and Ideas — Command of Evidence (Quantitative) ---
        q_item(
            'm1_m1_q13', 13, 'Information and Ideas', 'Command of Evidence (Quantitative)', 'Hard',
            svg_bar_chart(
                'Mean Recovery Time (Months) of Disturbed Seagrass Beds by Restoration Method',
                ['0', '10', '20', '30', '40'],
                [('Natural Recolon.', 38, '38 mo'), ('Loose Seed Scatter', 29, '29 mo'), ('Burlap Seed Bags', 15, '15 mo'), ('Anchored Sod Plugs', 11, '11 mo')],
                40
            ) + '<p>Coastal restoration biologists noted that scattering loose seagrass seeds onto tidal mudflats often fails to accelerate recovery dramatically because strong currents wash most seeds away before germination. By contrast, enclosing seeds inside biodegradable burlap bags anchored to the seabed cuts recovery time by more than half compared with unassisted natural recolonization—nearly rivaling the speed of labor-intensive transplanted sod plugs.</p>',
            'Which choice most effectively uses data from the graph to support the biologists’ assessment of burlap seed bags?',
            [
                'Burlap seed bags reduced mean recovery time to 15 months—less than half the 38 months required for natural recolonization and only 4 months slower than anchored sod plugs (11 months).',
                'Loose seed scattering required an average of 29 months for disturbed seagrass beds to recover, compared with 38 months for natural recolonization.',
                'Anchored sod plugs achieved the fastest seagrass recovery time in the study at 11 months.',
                'Natural recolonization required the longest recovery period among all four tested methods at 38 months.'
            ],
            'A',
            'Checklist 2 vế đánh giá về Burlap Seed Bags: [1] Giảm hơn một nửa thời gian so với Natural Recolonization (38 / 2 = 19 → 15 < 19 ✓) + [2] Gần bắt kịp tốc độ của Anchored Sod Plugs (15 vs. 11, chỉ chênh 4 tháng ✓). B, C, D đều đúng số liệu nhưng bỏ qua chính đối tượng Burlap Seed Bags! Duy nhất A đối chiếu đủ cả 3 mốc 15, 38 và 11 tháng!',
            'Xác minh phép toán: 15 < 38/2 (19) và so sánh trực tiếp 15 vs. 11 — A khớp trọn 100% đánh giá của nhóm sinh vật học!',
            [
                ('Đáp án đúng', 'Khớp đầy đủ cả hai vế: 15 tháng < một nửa của 38 tháng, và chỉ chậm hơn sod plugs (11 tháng) đúng 4 tháng.'),
                ('True Data / Wrong Subject', 'Chỉ nói về Loose Seed Scatter (29 tháng), không nhắc đến burlap seed bags.'),
                ('Incomplete Data', 'Chỉ nêu tốc độ của sod plugs mà bỏ qua số liệu của burlap seed bags.'),
                ('Incomplete Data', 'Chỉ nêu mốc 38 tháng của natural recolonization.'),
            ]
        ),
        q_item(
            'm1_m1_q14', 14, 'Information and Ideas', 'Command of Evidence (Quantitative)', 'Hard',
            html_table(
                'Table 1. Annual Patron Attendance at Four Municipal Performing Arts Venues (2019 vs. 2024)',
                ['Venue', 'Primary Program', '2019 Attendance', '2024 Attendance', '2024 Ticket Revenue Change'],
                [
                    ['Lyric Hall', 'Classical Symphony', '84,000', '91,000', '+12%'],
                    ['Harbor Stage', 'Contemporary Theater', '62,000', '75,000', '+19%'],
                    ['Civic Pavilion', 'Chamber & Jazz', '48,000', '53,000', '−4%'],
                    ['Granite Playhouse', 'Experimental Dance', '35,000', '31,000', '−9%'],
                ]
            ) + '<p>An arts-funding consultant asserts that any municipal venue that expands its total annual attendance between 2019 and 2024 is guaranteed to post a positive increase in ticket revenue over the same period.</p>',
            'Which choice best describes data from the table that directly weaken the consultant’s assertion?',
            [
                'Granite Playhouse experienced both a decline in annual attendance (from 35,000 to 31,000) and a 9% drop in ticket revenue.',
                'Civic Pavilion increased its annual attendance from 48,000 in 2019 to 53,000 in 2024, yet its ticket revenue declined by 4% over that same period.',
                'Harbor Stage achieved both the largest attendance jump (from 62,000 to 75,000) and the highest revenue gain (+19%).',
                'Lyric Hall hosted the largest total annual audience in both 2019 (84,000) and 2024 (91,000).'
            ],
            'B',
            'Khóa Claim cần WEAKEN: BẤT KỲ nhà hát nào TĂNG lượng khách (2019 → 2024) đều ĐẢM BẢO TĂNG doanh thu vé! Tìm phản ví dụ trong bảng: **Civic Pavilion** tăng khách từ 48.000 lên 53.000 (+5.000 khách), NHƯNG doanh thu vé lại GIẢM −4%! Chọn B!',
            'Tìm đúng hàng có dấu trái chiều giữa hai cột (`Attendance ↑` nhưng `Revenue ↓`) để đập tan từ "guaranteed"!',
            [
                ('True Data / Wrong Claim', 'Granite Playhouse giảm CẢ khách lẫn doanh thu — không bác bỏ tuyên bố về các nhà hát TĂNG khách.'),
                ('Đáp án đúng', 'Civic Pavilion là phản ví dụ trực diện: lượng khách tăng (48k → 53k) nhưng doanh thu vé lại giảm 4%.'),
                ('Opposite Direction (Supports!)', 'Harbor Stage tăng cả khách lẫn doanh thu — ủng hộ tuyên bố của chuyên gia.'),
                ('True Data / Wrong Claim', 'Lyric Hall cũng tăng cả khách lẫn doanh thu.'),
            ]
        ),

        # --- Q15: Information and Ideas — Inferences ---
        q_item(
            'm1_m1_q15', 15, 'Information and Ideas', 'Inferences', 'Hard',
            '<p>Astronomers scanning archival glass photographic plates taken at Mount Wilson Observatory in 1917 recently noticed faint absorption lines indicating heavy elements—calcium and magnesium—polluting the white-dwarf star van Maanen 2. Because a white dwarf’s intense gravity drags heavy elements out of its observable atmosphere into its interior within mere days or years, the continued presence of those heavy elements in both 1917 plates and modern 2024 spectra implies that ______</p>',
            'Which choice most logically completes the text?',
            [
                'glass photographic plates from 1917 are generally too degraded to detect calcium or magnesium lines.',
                'heavy elements inside white dwarfs are pushed outward to the surface by gravity over millions of years.',
                'van Maanen 2 has likely been continually accreting fresh rocky debris—such as shattered asteroids or planetesimals—over the past century.',
                'van Maanen 2 is the only white-dwarf star in the Milky Way surrounded by rocky planetary material.'
            ],
            'C',
            'Ghép 2 tiền đề (1-Millimeter Rule): (A) Trọng lực sao lùn trắng kéo chìm nguyên tố nặng khỏi bầu khí quyển chỉ trong vài ngày đến vài năm; (B) Thế nhưng canxi & magie VẪN CÓ MẶT liên tục từ năm 1917 đến tận năm 2024 (>100 năm) ⇒ Kết luận tất yếu: Ngôi sao này nhiều khả năng đã liên tục hút bồi thêm mảnh vỡ đá mới (tiểu hành tinh/hành tinh vỡ) trong suốt thế kỷ qua (C)!',
            'Áp dụng logic cân bằng dòng chảy: Nếu thứ gì thoát đi trong vài ngày mà 107 năm sau vẫn đầy ở bề mặt → chắc chắn phải có nguồn cung liên tục mới rơi vào!',
            [
                ('Contradiction', 'Các nhà thiên văn VỪA PHÁT HIỆN ĐƯỢC các vạch hấp thụ canxi và magie trên chính tấm kính năm 1917!'),
                ('Reversed Logic', 'Bài nói trọng lực kéo nguyên tố nặng VÀO TRONG lõi ("into its interior"), không phải đẩy ra ngoài.'),
                ('Đáp án đúng', 'Suy diễn 1mm chặt chẽ: để nguyên tố nặng tồn tại suốt 1917–2024 bất chấp chìm nhanh, sao phải liên tục bồi tụ mảnh đá mới.'),
                ('Too Extreme (Only Trap)', 'Không có căn cứ nào khẳng định đây là sao lùn trắng DUY NHẤT trong Ngân Hà có vật chất đá.'),
            ]
        ),

        # --- Q16-Q19: Standard English Conventions — Boundaries ---
        q_item(
            'm1_m1_q16', 16, 'Standard English Conventions', 'Boundaries', 'Medium',
            '<p>In 2022, civil engineers in Rotterdam completed an underground rainwater plaza capable of holding ten million liters of storm ______ during dry summer weeks, the sunken concrete basin doubles as a neighborhood amphitheater and basketball court.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['runoff,', 'runoff, and while', 'runoff', 'runoff;'],
            'D',
            'Vế 1 là IC hoàn chỉnh ("In 2022, civil engineers... storm runoff"). Vế 2 cũng là IC hoàn chỉnh ("during dry summer weeks, the sunken concrete basin doubles..."). Giữa 2 IC → Chọn dấu chấm phẩy (;) = D!',
            'Đếm nhanh 2 IC trước và sau chỗ trống → chọn dấu chấm phẩy (;), loại Comma Splice (A) và Run-on (C).',
            [
                ('Comma Splice', 'Chỉ dùng 1 dấu phẩy để nối hai mệnh đề độc lập là lỗi Comma Splice.'),
                ('Fragment / Subordinate Trap', 'Thêm "and while" biến vế 2 thành mệnh đề phụ treo lơ lửng không có mệnh đề chính theo sau.'),
                ('Run-On Sentence', 'Không có dấu câu ngăn hai IC.'),
                ('Đáp án đúng', 'Dấu chấm phẩy (;) ngăn cách chuẩn xác hai mệnh đề độc lập IC + IC.'),
            ]
        ),
        q_item(
            'm1_m1_q17', 17, 'Standard English Conventions', 'Boundaries', 'Medium',
            '<p>Drawing on archival blueprints from nineteenth-century steamships, maritime historian ______ reconstructed how coal-bunker placement affected vessel stability across stormy Atlantic crossings.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['Dr. Clara Bergmann', ', Dr. Clara Bergmann,', 'Dr. Clara Bergmann,', ', Dr. Clara Bergmann'],
            'A',
            'Quy tắc Title + Name không mạo từ: "maritime historian Dr. Clara Bergmann" (không có "a/the/her" trước chức danh) → Essential → 0 dấu phẩy ở cả 2 đầu, nối thẳng sang động từ chính "reconstructed" → Chọn A!',
            'Nghề nghiệp không mạo từ + Tên riêng + Động từ chính → 0 dấu phẩy!',
            [
                ('Đáp án đúng', 'Không dấu phẩy — giữ liền cụm chức danh bắt buộc + tên riêng với động từ chính "reconstructed".'),
                ('Non-Essential Trap', 'Chỉ dùng cặp phẩy khi chức danh phía trước có mạo từ xác định duy nhất.'),
                ('No-Comma Zone (S, V)', 'Dấu phẩy đơn ngăn cách chủ ngữ khỏi động từ chính "reconstructed".'),
                ('Unpaired Comma', 'Dấu phẩy lẻ giữa chức danh và tên riêng.'),
            ]
        ),
        q_item(
            'm1_m1_q18', 18, 'Standard English Conventions', 'Boundaries', 'Hard',
            '<p>To build the cantilevered timber roof of the Oslo harbor pavilion, architects had to overcome a formidable structural ______ supporting a twenty-four-meter overhang without obstructing waterfront views with vertical steel pillars.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['challenge;', 'challenge:', 'challenge.', 'challenge, and'],
            'B',
            'Vế trái ("...architects had to overcome a formidable structural challenge") là 1 IC hoàn chỉnh. Vế phải ("supporting a twenty-four-meter overhang without obstructing...") là Cụm danh động từ (Gerund Phrase — KHÔNG PHẢI IC!) giải thích trực tiếp "structural challenge" là gì → Bắt buộc dùng dấu hai chấm (:) = B! Loại A (;) và C (.) vì vế phải không phải IC; loại D (", and" nối IC với Phrase).',
            'IC hoàn chỉnh + Cụm giải thích không có động từ chia thì (Phrase) → Dấu hai chấm (:) là công thức chuẩn duy nhất!',
            [
                ('Semicolon + Fragment', 'Vế sau "supporting..." không có chủ ngữ và động từ chia thì → không phải IC → cấm chấm phẩy.'),
                ('Đáp án đúng', 'Dấu hai chấm (:) sau IC giới thiệu chính xác cụm từ định nghĩa cho "a formidable structural challenge".'),
                ('Period + Fragment', 'Tách cụm V-ing thành câu riêng tạo Sentence Fragment.'),
                ('Comma + FANBOYS + Fragment', 'Sau ", and" không có IC đầy đủ và không song song với "to overcome".'),
            ]
        ),
        q_item(
            'm1_m1_q19', 19, 'Standard English Conventions', 'Boundaries', 'Hard',
            '<p>The kelp forests off Monterey Bay—home to sea otters, leopard sharks, and brightly colored rockfish ______ absorb wave energy that would otherwise erode sandy coastal bluffs during winter storms.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['alike,', 'alike;', 'alike—', 'alike'],
            'C',
            'Cụm bổ sung giữa Chủ ngữ ("The kelp forests off Monterey Bay") và Động từ chính ("absorb") mở đầu bằng gạch ngang dài (`—home to sea otters...`) → Phải đóng bằng gạch ngang dài thứ hai (`alike—`) → Chọn C!',
            'Mở bằng em-dash (—) → Đóng bằng em-dash (—)! Không bao giờ ghép lệch với dấu phẩy hay chấm phẩy.',
            [
                ('Mismatched Pair (— ... ,)', 'Cấm mở bằng gạch ngang rồi đóng bằng dấu phẩy.'),
                ('Semicolon Inside Modifier', 'Dấu chấm phẩy tách đứt chủ ngữ khỏi động từ "absorb".'),
                ('Đáp án đúng', 'Khép đúng cặp gạch ngang đôi (— ... —) trước động từ chính "absorb".'),
                ('Unclosed Modifier', 'Thiếu dấu đóng gạch ngang khiến câu vỡ cấu trúc.'),
            ]
        ),

        # --- Q20-Q22: Standard English Conventions — Form, Structure, and Sense ---
        q_item(
            'm1_m1_q20', 20, 'Standard English Conventions', 'Form, Structure, and Sense', 'Medium',
            '<p>A digitized archive of more than six thousand nineteenth-century whaling ship logs stored at the New Bedford museum ______ climate scientists with rare daily wind and sea-ice records from the pre-industrial Arctic.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['provide', 'have provided', 'providing', 'provides'],
            'D',
            'Gạch bỏ toàn bộ cụm giới từ & phân từ chen giữa: "A digitized <b>archive</b> <s>[of more than six thousand nineteenth-century whaling ship logs stored at the New Bedford museum]</s>". Chủ ngữ thật là "A digitized archive" (SỐ ÍT), câu chưa có động từ chính → Chọn "provides" (D)!',
            'Mẹo 3–1: A và B là số nhiều, C là phân từ (Fragment), duy nhất D là động từ chia thì số ít khớp "archive"!',
            [
                ('Subject-Verb Mismatch', 'provide là số nhiều — bị lừa bởi "six thousand... logs".'),
                ('Subject-Verb Mismatch', 'have provided là số nhiều.'),
                ('Non-Finite Fragment', 'providing là V-ing khiến câu không có động từ chia thì.'),
                ('Đáp án đúng', 'provides (số ít, hiện tại đơn) khớp chuẩn với chủ ngữ "A digitized archive".'),
            ]
        ),
        q_item(
            'm1_m1_q21', 21, 'Standard English Conventions', 'Form, Structure, and Sense', 'Hard',
            '<p>Constructed without nails from interlocking cedar joints designed to flex during tremors, ______</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            [
                'the five-story pagoda at Hōryū-ji has stood undamaged in Nara for over thirteen centuries.',
                'ancient Japanese carpenters built the five-story pagoda at Hōryū-ji to endure earthquakes.',
                'Nara’s master builders engineered the Hōryū-ji pagoda to absorb seismic shock waves.',
                'earthquakes have repeatedly failed to topple the five-story pagoda at Hōryū-ji.'
            ],
            'A',
            'Dangling Modifier Check! Cụm mở đầu "Constructed without nails from interlocking cedar joints..." (Được xây dựng không dùng đinh từ các mộng gỗ tuyết tùng) mô tả NGÔI CHÙA ("the five-story pagoda"), KHÔNG mô tả thợ mộc (B), thợ xây (C), hay động đất (D)! Duy nhất A đặt đúng "the five-story pagoda at Hōryū-ji" làm chủ ngữ ngay sau dấu phẩy!',
            'Hỏi ngay: "Cái gì được XÂY KHÔNG DÙNG ĐINH bằng mộng gỗ tuyết tùng?" → Chỉ có ngôi chùa (the five-story pagoda)!',
            [
                ('Đáp án đúng', 'Chủ ngữ "the five-story pagoda at Hōryū-ji" đứng ngay sau dấu phẩy khớp 100% với cụm "Constructed...".'),
                ('Dangling Modifier', 'Thợ mộc cổ đại không phải là vật "được xây bằng mộng gỗ tuyết tùng".'),
                ('Dangling Modifier', 'Các thợ xây Nara không phải công trình được xây từ gỗ tuyết tùng.'),
                ('Dangling Modifier', 'Những trận động đất không thể được xây bằng mộng gỗ.'),
            ]
        ),
        q_item(
            'm1_m1_q22', 22, 'Standard English Conventions', 'Form, Structure, and Sense', 'Hard',
            '<p>Before the Panama Canal opened to commercial shipping in 1914, maritime insurers noted that the hull stresses endured by cargo vessels rounding Cape Horn were far more severe than ______ traversing calmer Mediterranean routes.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['vessels', 'those of vessels', 'that of vessels', 'a vessel'],
            'B',
            'So sánh tương đồng (Apples-to-Apples): Đối tượng bị so sánh ở vế 1 là "<b>the hull stresses</b>" (những ứng suất thân tàu — SỐ NHIỀU!). Không thể so sánh "hull stresses" với "vessels" (con tàu — loại A & D). Vì "stresses" là SỐ NHIỀU → chọn "<b>those of</b> vessels" (B), loại "that of" (chỉ dùng cho số ít)!',
            'So sánh đối tượng SỐ NHIỀU ("the hull stresses") → dùng "those of"; SỐ ÍT → dùng "that of"!',
            [
                ('Illogical Comparison', 'So sánh "ứng suất thân tàu" (hull stresses) trực tiếp với "con tàu" (vessels) là lệch cấp.'),
                ('Đáp án đúng', '"those of vessels" thay thế chính xác cho danh từ số nhiều "the hull stresses of vessels".'),
                ('Pronoun Number Mismatch', '"that of" chỉ thay thế cho danh từ số ít, nhưng "hull stresses" là số nhiều.'),
                ('Illogical Comparison', 'So sánh ứng suất với một con tàu — vừa khập khiễng vừa sai số.'),
            ]
        ),

        # --- Q23-Q25: Expression of Ideas — Transitions ---
        q_item(
            'm1_m1_q23', 23, 'Expression of Ideas', 'Transitions', 'Medium',
            '<p>Unlike terrestrial telescopes, which must peer through Earth’s turbulent atmosphere, space-based observatories orbit cleanly above atmospheric distortion. ______, astronomers can capture razor-sharp optical spectra of distant galaxies without losing faint starlight to air shimmer.</p>',
            'Which choice completes the text with the most logical transition?',
            ['Nevertheless', 'By contrast', 'Consequently', 'Previously'],
            'C',
            'Câu 1: Kính viễn vọng không gian quay phía trên lớp khí quyển nhiễu loạn. Câu 2: KẾT QUẢ là nhà thiên văn thu được quang phổ cực sắc nét không bị nhòe → Quan hệ Nhân – Quả → "Consequently" (C)!',
            'Nguyên nhân (orbit above distortion) → Hệ quả trực tiếp (capture razor-sharp spectra) = "Consequently / Therefore".',
            [
                ('False Contrast', 'Nevertheless chỉ sự trái kỳ vọng — sai hoàn toàn hướng nhân quả.'),
                ('False Contrast', 'By contrast đối chiếu hai đối tượng ngược chiều — câu 2 nói về hệ quả trực tiếp của câu 1.'),
                ('Đáp án đúng', 'Consequently nối chính xác nguyên nhân không bị nhiễu khí quyển với kết quả hình ảnh sắc nét.'),
                ('Wrong Relationship (Time)', 'Previously chỉ thời điểm trước đó — sai logic.'),
            ]
        ),
        q_item(
            'm1_m1_q24', 24, 'Expression of Ideas', 'Transitions', 'Hard',
            '<p>During the 1920s, jazz arranger Mary Lou Williams did not simply transcribe popular dance melodies for big-band brass sections. ______, she pioneered intricate counter-melodies and bold harmonic voicings that reshaped swing orchestration for Kansas City ensembles.</p>',
            'Which choice completes the text with the most logical transition?',
            ['Similarly', 'Therefore', 'Still', 'Instead'],
            'D',
            'Câu 1 chứa phủ định rõ ("did NOT simply transcribe..."). Câu 2 đưa hành động THAY THẾ vượt trội hơn ("she pioneered intricate counter-melodies...") → Phủ định X, làm Y thay thế = "Instead" (D)!',
            'Thấy "did not simply X" ở câu 1 + hành động thay thế Y ở câu 2 → chốt ngay "Instead"!',
            [
                ('Wrong Relationship (Addition)', 'Similarly chỉ sự tương đồng — sai vì câu 1 mang nghĩa phủ định.'),
                ('Wrong Relationship (Cause-Effect)', 'Việc không chỉ chép giai điệu không tự sinh ra đổi mới hòa âm theo kiểu nhân quả tự động.'),
                ('Contrast Nuance Trap', 'Still (= Nevertheless) không diễn đạt hành động thay thế sau cấu trúc "did not simply...".'),
                ('Đáp án đúng', 'Instead khớp tuyệt đối cấu trúc phủ định X → thay bằng hành động tiên phong Y.'),
            ]
        ),
        q_item(
            'm1_m1_q25', 25, 'Expression of Ideas', 'Transitions', 'Hard',
            '<p>Modern urban cable cars in La Paz, Bolivia, glide quietly above congested steep mountain roads, cutting cross-city commute times in half for thousands of daily workers. ______, because the aerial gondolas run on electricity rather than diesel fuel, they emit virtually no street-level exhaust along densely populated valley corridors.</p>',
            'Which choice completes the text with the most logical transition?',
            ['Moreover', 'However', 'For instance', 'In other words'],
            'A',
            'Câu 1 nêu LỢI ÍCH 1 (rút ngắn một nửa thời gian đi lại trên đường núi kẹt xe). Câu 2 bổ sung LỢI ÍCH 2 ĐỘC LẬP cùng chiều (chạy điện nên gần như không xả khói ở mức đường phố) → Bổ sung thêm ưu điểm mới cùng hướng → "Moreover" (A)!',
            'Ưu điểm 1 (thời gian) + Ưu điểm 2 độc lập (khí thải) → "Moreover / Furthermore" (KHÔNG chọn "For instance" hay "In other words"!).',
            [
                ('Đáp án đúng', 'Moreover bổ sung chính xác ưu điểm môi trường độc lập thứ hai tiếp nối ưu điểm thời gian ở câu 1.'),
                ('False Contrast', 'Hai câu cùng nêu ưu điểm tích cực của cáp treo đô thị.'),
                ('Wrong Relationship (Example)', 'Chạy điện không xả khói không phải ví dụ con của việc rút ngắn thời gian đi lại.'),
                ('Restatement Trap', 'Câu 2 đưa lợi ích mới chứ không diễn đạt lại câu 1.'),
            ]
        ),

        # --- Q26-Q27: Expression of Ideas — Rhetorical Synthesis ---
        q_item(
            'm1_m1_q26', 26, 'Expression of Ideas', 'Rhetorical Synthesis', 'Medium',
            '''<p>While researching a topic, a student has taken the following notes:</p>
            <ul>
              <li>The Q’eswachaka bridge is a hand-woven suspension bridge spanning the Apurímac River gorge in southern Peru.</li>
              <li>Built using continuous Inca engineering traditions, the 28-meter bridge is woven entirely from twisted local <i>q’oya</i> grass.</li>
              <li>Because grass ropes weather rapidly in the Andean climate, four neighboring Quechua communities gather every June to cut down the old bridge and weave a brand-new span in just three days.</li>
              <li>UNESCO recognized the annual bridge-renewal festival as Intangible Cultural Heritage in 2013.</li>
            </ul>''',
            'The student wants to explain why the Q’eswachaka bridge must be rebuilt annually despite its long historical continuity. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
            [
                'Recognized by UNESCO in 2013, the Q’eswachaka bridge spans 28 meters across the Apurímac River gorge in southern Peru.',
                'Although the Q’eswachaka bridge preserves centuries-old Inca weaving traditions, its twisted <i>q’oya</i> grass cables weather quickly in the Andean climate, requiring four local Quechua communities to rebuild the span every June.',
                'Four neighboring Quechua communities work together for three days each June to construct a 28-meter suspension bridge across the Apurímac River.',
                'UNESCO added the Q’eswachaka bridge-renewal festival to its Intangible Cultural Heritage list in 2013.'
            ],
            'B',
            'Goal-First SOP: Giải thích VÌ SAO cây cầu phải xây lại hàng năm bất chấp truyền thống lâu đời ("explain WHY... rebuilt annually despite long historical continuity"). A, C, D đều bỏ qua nguyên nhân cốt lõi (dây cỏ q’oya bị phong hóa nhanh trong khí hậu Andes). Duy nhất B nối đủ cả truyền thống Inca lâu đời + nguyên nhân cỏ bị phong hóa nhanh → phải xây lại mỗi tháng Sáu!',
            'Tìm đúng từ nối nhân quả giải quyết chữ "why" trong Goal ("weather quickly... requiring... to rebuild every June")!',
            [
                ('Wrong Synthesis Goal', 'Chỉ nêu danh hiệu UNESCO và chiều dài cầu, không giải thích lý do xây lại hàng năm.'),
                ('Đáp án đúng', 'Khớp cả hai vế: bảo tồn truyền thống Inca lâu đời nhưng dây cỏ phong hóa nhanh nên phải xây lại mỗi năm.'),
                ('Missing Reason (Why)', 'Mô tả việc xây cầu trong 3 ngày nhưng không nêu nguyên nhân cỏ nhanh mục.'),
                ('Wrong Synthesis Goal', 'Chỉ nêu sự kiện UNESCO năm 2013.'),
            ]
        ),
        q_item(
            'm1_m1_q27', 27, 'Expression of Ideas', 'Rhetorical Synthesis', 'Hard',
            '''<p>While researching a topic, a student has taken the following notes:</p>
            <ul>
              <li><i>The Rite of Spring</i> is a 1913 orchestral ballet score composed by Russian-born composer Igor Stravinsky.</li>
              <li>Stravinsky replaced regular dance meters with jarring, constantly shifting rhythmic accents and dissonant polytonal chords.</li>
              <li><i>Boléro</i> is a 1928 orchestral work composed by French composer Maurice Ravel.</li>
              <li>Ravel anchored the entire fifteen-minute piece on a single unchanging snare-drum rhythm and one repeated melody that grows steadily louder through changing orchestral instruments.</li>
            </ul>''',
            'The student wants to emphasize a contrast in how Stravinsky and Ravel used rhythm in these two twentieth-century orchestral works. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
            [
                'Both Igor Stravinsky’s <i>The Rite of Spring</i> (1913) and Maurice Ravel’s <i>Boléro</i> (1928) are landmark twentieth-century orchestral compositions.',
                'In 1928, French composer Maurice Ravel built <i>Boléro</i> around a single repeated melody that grows steadily louder over fifteen minutes.',
                'Whereas Igor Stravinsky built <i>The Rite of Spring</i> around jarring, constantly shifting rhythmic accents, Maurice Ravel anchored <i>Boléro</i> on a single unchanging snare-drum rhythm.',
                'Igor Stravinsky composed <i>The Rite of Spring</i> in 1913 using dissonant polytonal chords, fifteen years before Maurice Ravel composed <i>Boléro</i>.'
            ],
            'C',
            'Goal-First SOP: Nhấn mạnh SỰ TƯƠNG PHẢN về CÁCH DÙNG NHỊP ĐIỆU ("contrast in how Stravinsky and Ravel used RHYTHM") của CẢ HAI tác phẩm. A nói điểm giống; B chỉ nói 1 tác phẩm; D so sánh năm sáng tác & hợp âm chứ không đối chiếu nhịp điệu. Duy nhất C đặt thẳng "constantly shifting rhythmic accents" (Stravinsky) đối nghịch với "single unchanging snare-drum rhythm" (Ravel)!',
            'Kiểm tra đúng cả 3 từ khóa của Goal: `contrast` + `both composers` + `rhythm`!',
            [
                ('Wrong Synthesis Goal', 'Nhấn mạnh điểm tương đồng thay vì tương phản về nhịp điệu.'),
                ('Single Subject Trap', 'Chỉ mô tả tác phẩm của Ravel mà không so sánh với Stravinsky.'),
                ('Đáp án đúng', 'Đối chiếu sắc nét hai cách xử lý nhịp điệu trái ngược giữa Stravinsky (biến đổi liên tục) và Ravel (một nhịp trống duy nhất bất biến).'),
                ('Wrong Criterion', 'Chỉ nêu khoảng cách 15 năm và hợp âm, bỏ qua yếu tố nhịp điệu (rhythm).'),
            ]
        ),
    ]
