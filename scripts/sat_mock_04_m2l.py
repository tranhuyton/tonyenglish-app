# -*- coding: utf-8 -*-
"""
Digital SAT R&W Adaptive Mock Test #4 — Module 2 Lower / Standard Route (27 Questions, Easy & Medium Tier)
Exclusive Topic Pools:
- Genetics / Microbiology / Public Health History
- Classical Mediterranean & Islamic Golden Age Scholarship
- Deep-Sea Hydrothermal & Polar Exploration
- Sociology / Civic Institutions & Demography
- Soft Robotics / Photonics / Nanomaterials
- World Literature & Nature Poetry
"""

from sat_drills_1_1_and_2_1 import q_item
from sat_drills_5_4_to_5_5 import svg_bar_chart, html_table

STEM_WIC = 'Which choice completes the text with the most logical and precise word or phrase?'
STEM_SEC = 'Which choice completes the text so that it conforms to the conventions of Standard English?'
STEM_TRANS = 'Which choice completes the text with the most logical transition?'


def get_m2l_questions():
    q13_chart = svg_bar_chart(
        'Annual Typhoid Deaths per 100,000 Residents Around Sand Filtration (1905)',
        ['0', '20', '40', '60', '80'],
        [
            ('1903 (Pre)', 68, '68'),
            ('1904 (Pre)', 72, '72'),
            ('1905 (Inst.)', 38, '38'),
            ('1906 (Post)', 14, '14'),
            ('1907 (Post)', 9, '9'),
        ],
        80,
    )

    q14_table = html_table(
        'Peak Voltage Output (mV) of Four Wearable Piezoelectric Nanofiber Textiles',
        ['Textile Prototype', 'Fiber Material', 'Voltage at 30° Bend (mV)', 'Voltage at 90° Bend (mV)', 'Wash Cycles Survived'],
        [
            ['Proto A', 'PVDF Polymer', '120', '310', '50'],
            ['Proto B', 'ZnO Nanowire', '185', '420', '15'],
            ['Proto C', 'Barium Titanate Composite', '240', '610', '45'],
            ['Proto D', 'Silk-Graphene Blend', '95', '210', '80'],
        ],
    )

    return [
        # Q1–Q5: Craft and Structure — Words in Context
        q_item(
            'm4_m2l_q1', 1, 'Craft and Structure', 'Words in Context', 'Easy',
            '<p>In 1861, French chemist Louis Pasteur boiled nutrient broth inside glass flasks with long, curved necks that let air enter while trapping airborne dust particles. Because the broth remained completely free of microbes until the curved necks were snapped off, Pasteur’s experiment ______ the widespread belief that bacteria spontaneously appeared out of thin air.</p>',
            STEM_WIC,
            ['confirmed', 'inspired', 'imitated', 'disproved'],
            'D',
            'Nước dùng vô trùng hoàn toàn không có vi sinh vật cho tới khi cổ bình cong bị bẻ gãy để bụi rơi vào → thí nghiệm của Pasteur đã "bác bỏ / chứng minh là sai" niềm tin cũ về sự tự sinh vi khuẩn từ không khí → "disproved".',
            'Khóa quan hệ kết quả thí nghiệm (không có vi khuẩn cho tới khi bụi vào) đối lập với niềm tin cũ (vi khuẩn tự sinh từ không khí) → chọn động từ mang nghĩa phủ bác.',
            [
                ('Opposite Meaning', 'confirmed = xác nhận là đúng — ngược hoàn toàn với kết quả thí nghiệm.'),
                ('Wrong Meaning', 'inspired = truyền cảm hứng — niềm tin tự sinh vốn đã phổ biến trước thí nghiệm.'),
                ('Wrong Meaning', 'imitated = bắt chước — không phù hợp với thí nghiệm kiểm chứng một giả thuyết.'),
                ('Đáp án đúng', 'disproved = bác bỏ / chứng minh niềm tin tự sinh là sai lầm.'),
            ],
        ),
        q_item(
            'm4_m2l_q2', 2, 'Craft and Structure', 'Words in Context', 'Easy',
            '<p>Weddell seals can dive beneath Antarctic sea ice for more than an hour without surfacing for air. To ______ their oxygen supply during these long underwater hunts, the seals dramatically slow their heart rates and store extra oxygen in specialized muscle proteins.</p>',
            STEM_WIC,
            ['exhaust', 'conserve', 'replace', 'measure'],
            'B',
            'Hải cẩu lặn hơn một giờ không trồi lên thở và làm chậm nhịp tim đáng kể → nhằm "tiết kiệm / bảo toàn" lượng oxy dự trữ → "conserve".',
            'Hành động "slow their heart rates" giúp giảm tiêu hao năng lượng và giữ lại oxy lâu hơn → động từ cần điền là "conserve".',
            [
                ('Opposite Meaning', 'exhaust = làm cạn kiệt — ngược với mục tiêu lặn lâu dưới băng.'),
                ('Đáp án đúng', 'conserve = tiết kiệm / bảo tồn nguồn oxy trong chuyến lặn dài.'),
                ('Wrong Meaning', 'replace = thay thế — dưới lớp băng hải cẩu không thể thay mới oxy cho tới khi ngoi lên.'),
                ('Wrong Meaning', 'measure = đo lường — không khớp với mục đích làm chậm nhịp tim.'),
            ],
        ),
        q_item(
            'm4_m2l_q3', 3, 'Craft and Structure', 'Words in Context', 'Easy',
            '<p>Founded in Fez, Morocco, in 859 CE by scholar and philanthropist Fatima al-Fihri, Al-Qarawiyyin began as a mosque and teaching center that attracted students of astronomy, law, and medicine from across North Africa and Andalusia. Today, historians recognize it as one of the world’s oldest continuously operating universities, prized for a library that ______ manuscripts dating back over a thousand years.</p>',
            STEM_WIC,
            ['discards', 'fabricates', 'preserves', 'outlaws'],
            'C',
            'Thư viện được đánh giá cao ("prized for a library") vì những bản thảo có niên đại hơn một nghìn năm → thư viện "lưu giữ / bảo tồn" các bản thảo cổ → "preserves".',
            'Khóa từ sắc thái tích cực "prized for" (được trân trọng vì) kết hợp với "manuscripts dating back over a thousand years" → chọn "preserves".',
            [
                ('Opposite Meaning', 'discards = vứt bỏ — trái ngược với giá trị của thư viện cổ.'),
                ('Wrong Meaning', 'fabricates = bịa đặt/làm giả — mâu thuẫn với việc các bản thảo có niên đại thật hơn 1.000 năm.'),
                ('Đáp án đúng', 'preserves = bảo tồn / gìn giữ các bản thảo cổ suốt hàng thế kỷ.'),
                ('Opposite Meaning', 'outlaws = cấm đoán theo luật — không hợp ngữ cảnh thư viện.'),
            ],
        ),
        q_item(
            'm4_m2l_q4', 4, 'Craft and Structure', 'Words in Context', 'Medium',
            '<p>Unlike industrial assembly-line robots built from steel joints that can move only along fixed axes, silicone robotic tentacles modeled on octopus arms bend smoothly around corners and squeeze through narrow crevices. This exceptional ______ makes soft robots well suited for inspecting collapsed pipes and fragile underwater reefs.</p>',
            STEM_WIC,
            ['flexibility', 'rigidity', 'fragility', 'uniformity'],
            'A',
            'Câu 1 mô tả xúc tu robot bằng silicone có thể uốn cong mượt mà qua các góc và luồn lách qua khe hẹp ("bend smoothly around corners and squeeze through narrow crevices") → phẩm chất nổi bật đó là "độ dẻo dai, linh hoạt" → "flexibility".',
            'Từ đại diện "This exceptional ______" luôn tóm gọn chính xác đặc tính vừa được mô tả ở câu trước ("bend smoothly... squeeze through narrow crevices").',
            [
                ('Đáp án đúng', 'flexibility = tính linh hoạt / khả năng uốn dẻo vượt trội, tóm tắt hoàn hảo câu 1.'),
                ('Opposite Meaning', 'rigidity = sự cứng nhắc — là đặc tính của robot khớp thép ở vế "Unlike", trái ngược với robot mềm.'),
                ('Wrong Meaning', 'fragility = sự dễ vỡ — là đặc điểm của rạn san hô chứ không phải ưu điểm của robot.'),
                ('Wrong Meaning', 'uniformity = sự đồng nhất — không mô tả khả năng uốn cong qua khe hẹp.'),
            ],
        ),
        q_item(
            'm4_m2l_q5', 5, 'Craft and Structure', 'Words in Context', 'Medium',
            '<p>Instead of expecting every household to buy rarely used equipment such as power saws, ladders, and pressure washers, municipal tool libraries lend these items out just like public books. Urban sociologists note that such lending programs not only cut household expenses but also ______ neighborhood solidarity as residents trade repair advice at the checkout counter.</p>',
            STEM_WIC,
            ['undermine', 'foster', 'conceal', 'restrict'],
            'B',
            'Cấu trúc song song tích cực "not only cut household expenses but also ______ neighborhood solidarity" (không chỉ giảm chi tiêu hộ gia đình mà còn thúc đẩy/nuôi dưỡng sự gắn kết khu phố khi hàng xóm trao đổi kinh nghiệm sửa chữa) → "foster".',
            'Cấu trúc "not only [lợi ích 1] but also [______ + danh từ tích cực]" đòi hỏi động từ mang sắc thái tích cực thúc đẩy/xây dựng.',
            [
                ('Opposite Meaning', 'undermine = làm suy yếu — ngược với lợi ích giao lưu tích cực ở cuối câu.'),
                ('Đáp án đúng', 'foster = nuôi dưỡng / thúc đẩy tình đoàn kết cộng đồng.'),
                ('Wrong Meaning', 'conceal = che giấu — không hợp nghĩa với "neighborhood solidarity".'),
                ('Opposite Meaning', 'restrict = hạn chế/kìm hãm — trái ngược với việc hàng xóm trao đổi thân thiện.'),
            ],
        ),

        # Q6–Q7: Craft and Structure — Text Structure and Purpose
        q_item(
            'm4_m2l_q6', 6, 'Craft and Structure', 'Text Structure and Purpose', 'Easy',
            '<p>Throughout literary history, traditional odes typically praised heroic conquerors, ancient gods, or grand philosophical ideals in elevated, formal diction. In 1954, Chilean poet Pablo Neruda upended this convention with <i>Elemental Odes</i>, writing short, conversational lines devoted to ordinary objects such as an onion, a pair of socks, and a wooden spoon. <u>In “Ode to the Onion,” for instance, Neruda calls the humble kitchen vegetable a “luminous flask” and celebrates its role in feeding working families.</u> By treating everyday items with lyric reverence, Neruda sought to make poetry accessible to readers from all walks of life.</p>',
            'Which choice best describes the function of the underlined sentence in the text as a whole?',
            [
                'It criticizes classical poets for choosing heroic conquerors and ancient gods as their subjects.',
                'It explains traditional methods for cooking onions in mid-twentieth-century Chile.',
                'It contrasts Pablo Neruda’s early political career with his later poetry.',
                'It offers a specific example of how Neruda honored an everyday object in <i>Elemental Odes</i>.',
            ],
            'D',
            'Tín hiệu rõ rệt ngay đầu câu gạch chân là cụm "for instance" (chẳng hạn như)! Câu trước giới thiệu việc Neruda phá bỏ quy ước cũ để ca ngợi những đồ vật bình dị; câu gạch chân đưa ra ví dụ cụ thể bài "Ode to the Onion" (gọi củ hành là "luminous flask" và tôn vinh vai trò nuôi sống gia đình lao động) → chọn D!',
            'Nhìn thấy "for instance / for example" ở đầu câu gạch chân → ưu tiên tìm đáp án mô tả chức năng minh họa cụ thể (provides/offers a specific example) cho luận điểm ở câu liền trước.',
            [
                ('Out of Scope', 'Câu gạch chân không hề chỉ trích các nhà thơ cổ điển.'),
                ('Literal Distractor', 'Bài nói về hình tượng thơ ca chứ không dạy cách nấu ăn ở Chile.'),
                ('Out of Scope', 'Đoạn văn không đề cập sự nghiệp chính trị của Neruda.'),
                ('Đáp án đúng', 'Mô tả đúng vai trò đưa ví dụ cụ thể minh họa cách Neruda tôn vinh vật dụng đời thường.'),
            ],
        ),
        q_item(
            'm4_m2l_q7', 7, 'Craft and Structure', 'Text Structure and Purpose', 'Medium',
            '<p>Quantum dots are semiconductor crystals just a few nanometers wide—so tiny that their physical size determines the exact color of light they emit when excited by electricity or blue LEDs. Crystals measuring roughly two nanometers across glow bright blue, whereas crystals of the exact same chemical compound measuring six nanometers across glow vivid red. Because engineers can dial in virtually any color simply by adjusting crystal diameter during synthesis, quantum dots have enabled television screens and medical imaging dyes with far purer color precision than earlier fluorescent materials.</p>',
            'Which choice best states the main purpose of the text?',
            [
                'To explain how the physical size of quantum dots controls the color of light they emit and why that property is valuable in modern applications.',
                'To argue that semiconductor crystals are too fragile to be used reliably in commercial television displays.',
                'To compare the production costs of blue LEDs with those of older fluorescent dyes.',
                'To trace the early twentieth-century history of quantum physics.',
            ],
            'A',
            'Đoạn văn giải thích rõ hai phần nối tiếp nhau: (1) Cách kích thước vật lý của chấm lượng tử quyết định màu sắc ánh sáng phát ra (2 nm phát xanh dương, 6 nm cùng hợp chất phát đỏ tươi); (2) Vì sao tính chất dễ tinh chỉnh này hữu ích cho màn hình TV và thuốc nhuộm hình ảnh y khoa có độ chuẩn màu cao hơn → khớp trọn vẹn với A!',
            'Đọc câu mở đầu (cơ chế) và câu kết (ứng dụng thực tiễn) để chọn đáp án Main Purpose bao quát đủ toàn đoạn văn.',
            [
                ('Đáp án đúng', 'Bao quát đủ cả hai phần: cơ chế kích thước quyết định màu phát sáng và giá trị ứng dụng trong TV/hình ảnh y khoa.'),
                ('Contradicted', 'Bài nêu rõ chấm lượng tử đã giúp tạo ra màn hình TV ưu việt hơn, không hề nói chúng quá mong manh.'),
                ('Out of Scope', 'Đoạn văn không so sánh chi phí sản xuất giữa LED xanh và thuốc nhuộm huỳnh quang cũ.'),
                ('Out of Scope', 'Bài không trình bày lịch sử vật lý lượng tử đầu thế kỷ 20.'),
            ],
        ),

        # Q8: Craft and Structure — Cross-Text Connections
        q_item(
            'm4_m2l_q8', 8, 'Craft and Structure', 'Cross-Text Connections', 'Medium',
            '<p><b>Text 1</b><br/>In her landmark 1961 book <i>The Death and Life of Great American Cities</i>, urbanist Jane Jacobs argued that neighborhoods mixing small shops, cafés, and apartments along short blocks feel safer than single-use residential zones. According to Jacobs, steady sidewalk foot traffic throughout the day provides informal “eyes on the street” that naturally deter petty crime.</p>'
            '<p><b>Text 2</b><br/>Analyzing five years of crime logs and smartphone foot-traffic data across Chicago neighborhoods, criminologist David Morales found that mixed-use streets with active ground-floor shops indeed experienced fewer nighttime break-ins than isolated residential blocks. However, Morales also noted that the busiest commercial intersections saw higher rates of pickpocketing during peak rush hours, suggesting that heavy crowds can create opportunities for certain offenses even as they discourage others.</p>',
            'Based on the texts, how would David Morales (Text 2) most likely respond to Jane Jacobs’s argument (Text 1)?',
            [
                'By asserting that mixed-use neighborhoods with sidewalk shops never reduce any category of urban crime.',
                'By contending that smartphone foot-traffic records are too unreliable to evaluate pedestrian safety.',
                'By agreeing that lively mixed-use streets help deter some crimes such as nighttime break-ins, while noting that dense rush-hour crowds can simultaneously raise rates of other offenses like pickpocketing.',
                'By recommending that city officials close ground-floor cafés and replace them with single-use apartment blocks.',
            ],
            'C',
            'Text 2 có chữ "indeed" xác nhận một phần luận điểm của Jane Jacobs (phố đa chức năng thực sự giảm trộm đột nhập ban đêm), theo sau là "However" bổ sung ngoại lệ quan trọng (ngã tư thương mại quá đông giờ cao điểm lại tăng nạn móc túi) → phản hồi chuẩn xác là đồng ý với tác dụng ngăn chặn một số loại tội phạm nhưng lưu ý đám đông dày đặc cũng làm tăng loại tội phạm khác (C)!',
            'Tìm cặp từ khóa "indeed... However..." trong Text 2 để ghép chính xác hai vế: Đồng thuận phần nào + Bổ sung hạn chế/ngoại lệ.',
            [
                ('Extreme / Contradicted', 'Morales thừa nhận rõ ràng các tuyến phố đa chức năng giảm số vụ đột nhập ban đêm.'),
                ('Out of Scope', 'Morales trực tiếp sử dụng dữ liệu di động cho nghiên cứu chứ không nghi ngờ độ tin cậy của nó.'),
                ('Đáp án đúng', 'Phản ánh cân bằng cả hai phát hiện của Morales: đồng ý giảm đột nhập ban đêm nhưng chỉ ra móc túi tăng khi quá đông giờ cao điểm.'),
                ('Out of Scope', 'Morales không hề đề xuất đóng cửa quán cà phê hay xây khu căn hộ đơn chức năng.'),
            ],
        ),

        # Q9–Q10: Information and Ideas — Central Ideas and Details
        q_item(
            'm4_m2l_q9', 9, 'Information and Ideas', 'Central Ideas and Details', 'Easy',
            '<p>Although Scottish bacteriologist Alexander Fleming famously noticed in 1928 that a stray mold colony killed bacteria on an uncovered laboratory dish, he struggled for years to extract enough stable penicillin to test in human patients. More than a decade later, Oxford scientists Howard Florey, Ernst Chain, and Norman Heatley developed deep-tank fermentation and purification techniques—ultimately using a high-yield mold strain found on a bruised cantaloupe in Peoria, Illinois—that turned Fleming’s fragile laboratory curiosity into a lifesaving medicine produced by the ton during World War II.</p>',
            'Which choice best states the main idea of the text?',
            [
                'Alexander Fleming originally isolated penicillin from a cantaloupe he discovered in Peoria, Illinois.',
                'Although Alexander Fleming first noticed penicillin’s antibacterial properties, later purification and mass-production advances by other scientists turned it into a practical medicine.',
                'Penicillin remained completely ineffective against bacteria until after World War II ended.',
                'Howard Florey and Ernst Chain proved that penicillin cured plant infections more reliably than human diseases.',
            ],
            'B',
            'Câu 1 nói Fleming phát hiện ra hiện tượng diệt khuẩn năm 1928 nhưng chật vật chiết xuất ổn định; câu 2 nói hơn một thập kỷ sau nhóm Florey, Chain và Heatley đã phát triển kỹ thuật lên men và tinh chế quy mô lớn biến nó thành thuốc cứu sống hàng triệu người trong Thế chiến II → B tóm gọn trọn vẹn ý chính!',
            'Với đoạn văn 2 câu nối bằng "Although... More than a decade later...", Main Idea luôn gom gọn cả công lao mở đầu lẫn bước ngoặt thực thi phía sau.',
            [
                ('Distorted Detail', 'Chủng nấm trên quả dưa lưới ở Peoria được nhóm sau này sử dụng, không phải phát hiện ban đầu năm 1928 của Fleming.'),
                ('Đáp án đúng', 'Khớp trọn vẹn vai trò của cả Fleming (phát hiện đầu tiên) và nhóm Oxford (tinh chế & sản xuất hàng loạt).'),
                ('Contradicted', 'Penicillin diệt khuẩn ngay từ 1928 và được sản xuất hàng tấn TRONG Thế chiến II.'),
                ('Out of Scope', 'Đoạn văn không đề cập đến việc chữa bệnh cho thực vật.'),
            ],
        ),
        q_item(
            'm4_m2l_q10', 10, 'Information and Ideas', 'Central Ideas and Details', 'Medium',
            '<p>For more than a thousand years, Mediterranean and European physicians accepted the second-century Greek doctor Galen’s claim that blood passed directly from the right side of the heart to the left through tiny invisible pores in the central muscular wall (the septum). In his 1242 commentary on Ibn Sina’s <i>Canon of Medicine</i>, Damascus-born physician Ibn al-Nafis rejected Galen’s model after observing that the heart’s septum is thick and completely solid. Ibn al-Nafis correctly deduced that blood must instead travel from the right ventricle through the pulmonary artery to the lungs, mix with air, and return to the left side of the heart—the earliest recorded description of pulmonary circulation.</p>',
            'According to the text, what anatomical observation led Ibn al-Nafis to reject Galen’s explanation of blood flow inside the heart?',
            [
                'He found that human lungs contain no blood vessels capable of carrying blood.',
                'He noted that the pulmonary artery connects the heart directly to the stomach.',
                'He demonstrated that Ibn Sina’s <i>Canon of Medicine</i> omitted any mention of the heart.',
                'He observed that the central muscular wall separating the right and left sides of the heart is thick and completely solid, without the invisible pores Galen claimed existed.',
            ],
            'D',
            'Đọc đúng câu trả lời trực tiếp ngay sau cụm "rejected Galen’s model after observing that...": "the heart’s septum is thick and completely solid" (vách cơ ngăn hai nửa tim dày và đặc hoàn toàn, không có lỗ li ti vô hình như Galen tuyên bố) → khớp tuyệt đối với D!',
            'Với câu hỏi chi tiết ("According to the text, what... led X to..."), tìm ngay từ khóa "after observing that" trong bài để chốt đáp án chính xác từng chữ.',
            [
                ('Contradicted', 'Ibn al-Nafis suy luận chính xác rằng máu đi qua động mạch phổi lên phổi rồi quay về tim.'),
                ('Fabricated / Out of Scope', 'Không có chi tiết nào liên kết động mạch phổi với dạ dày.'),
                ('Out of Scope', 'Ibn al-Nafis viết bài bình luận trực tiếp về *Canon of Medicine*, không nói cuốn sách bỏ sót trái tim.'),
                ('Đáp án đúng', 'Khớp nguyên văn quan sát giải phẫu của Ibn al-Nafis rằng vách ngăn tim dày và đặc hoàn toàn, không có các lỗ vô hình.'),
            ],
        ),

        # Q11–Q12: Information and Ideas — Command of Evidence (Textual)
        q_item(
            'm4_m2l_q11', 11, 'Information and Ideas', 'Command of Evidence (Textual)', 'Medium',
            '<p>During the dark Arctic winter, sea ice appears lifeless from above, yet microscopic brine channels threading through the bottom of the ice floes harbor dense communities of ice algae. Marine ecologist Dr. Karin Lindholm hypothesized that when spring sunlight penetrates thin first-year sea ice, blooms of these ice-dwelling algae—rather than open-water phytoplankton—provide the earliest critical pulse of nutrition for grazing Arctic copepods.</p>',
            'Which finding, if true, would most directly support Lindholm’s hypothesis?',
            [
                'Lipid analyses of Arctic copepods collected in early spring reveal that over eighty percent of their stored body fat contains molecular markers produced exclusively by ice-dwelling algae rather than open-water phytoplankton.',
                'Satellite measurements confirm that Arctic sea ice reaches its greatest seasonal surface area every March before thinning in late spring.',
                'Open-water phytoplankton reproduce rapidly in warm tropical oceans where sea ice never develops.',
                'Polar bears hunt ringed seals most frequently along cracks in Arctic pack ice during early spring.',
            ],
            'A',
            'Giả thuyết của Lindholm: đầu mùa xuân, tảo sống TRONG BĂNG (ice-dwelling algae) — chứ không phải thực vật phù du nước mở — là nguồn dinh dưỡng sớm thiết yếu cho loài chân chèo Bắc Cực (copepods). Phân tích lipid cho thấy >80% chất béo tích trữ trong cơ thể copepods đầu xuân mang dấu ấn phân tử ĐỘC QUYỀN của tảo băng (A) chứng minh trực tiếp chúng thực sự ăn tảo băng làm nguồn dinh dưỡng chính!',
            'Tìm bằng chứng đo trực tiếp đối tượng được nêu trong giả thuyết (Arctic copepods + nguồn thức ăn ice-dwelling algae vs. open-water phytoplankton).',
            [
                ('Đáp án đúng', 'Bằng chứng sinh hóa trực tiếp xác nhận trên 80% dưỡng chất tích trữ đầu xuân của copepods đến từ tảo băng thay vì phù du nước mở.'),
                ('Irrelevant Background', 'Chỉ nói về diện tích băng cực đại tháng Ba, không chứng minh copepods ăn gì.'),
                ('Out of Scope', 'Nói về đại dương nhiệt đới, không liên quan hệ sinh thái băng Bắc Cực.'),
                ('Out of Scope', 'Nói về gấu Bắc Cực săn hải cẩu, hoàn toàn lệch khỏi đối tượng copepods và tảo băng.'),
            ],
        ),
        q_item(
            'm4_m2l_q12', 12, 'Information and Ideas', 'Command of Evidence (Textual)', 'Easy',
            '<p>In his 1865 poem “When I Heard the Learn’d Astronomer,” Walt Whitman contrasts dry, technical scientific lectures with the quiet awe of experiencing nature directly outdoors.</p>',
            'Which quotation from “When I Heard the Learn’d Astronomer” best illustrates the speaker’s shift toward quiet awe while experiencing nature directly?',
            [
                '“When the proofs, the figures, were ranged in columns before me,”',
                '“When I was shown the charts and diagrams, to add, divide, and measure them,”',
                '“Till rising and gliding out I wander’d off by myself, / In the mystical moist night-air, and from time to time, / Look’d up in perfect silence at the stars.”',
                '“When I sitting heard the astronomer where he lectured with much applause in the lecture-room,”',
            ],
            'C',
            'Câu hỏi yêu cầu trích dẫn minh họa BƯỚC CHUYỂN sang cảm giác kinh ngạc tĩnh lặng khi trải nghiệm thiên nhiên trực tiếp ngoài trời. A, B, D đều chỉ mô tả phần bài giảng kỹ thuật trong giảng đường (chứng minh, con số, biểu đồ, tràng pháo tay). Duy nhất C mô tả nhân vật đứng dậy bước ra ngoài trời đêm ẩm ướt huyền bí và ngước nhìn các vì sao trong sự tĩnh lặng tuyệt đối ("Look’d up in perfect silence at the stars")!',
            'Chú ý đúng vế mà câu hỏi stem yêu cầu ("speaker’s shift toward quiet awe while experiencing nature directly") để không chọn nhầm nửa đầu về bài giảng kỹ thuật.',
            [
                ('Wrong Half of Contrast', 'Chỉ mô tả bảng chứng minh và con số trong bài giảng, chưa bước ra thiên nhiên.'),
                ('Wrong Half of Contrast', 'Chỉ mô tả biểu đồ và phép đo đạc kỹ thuật trong lớp học.'),
                ('Đáp án đúng', 'Thể hiện trực tiếp khoảnh khắc bước ra ngoài trời đêm và ngước nhìn bầu trời sao trong im lặng đầy kinh ngạc.'),
                ('Wrong Half of Contrast', 'Chỉ mô tả cảnh ngồi nghe diễn giả thuyết trình trong giảng đường.'),
            ],
        ),

        # Q13–Q14: Information and Ideas — Command of Evidence (Quantitative)
        q_item(
            'm4_m2l_q13', 13, 'Information and Ideas', 'Command of Evidence (Quantitative)', 'Easy',
            q13_chart + '<p>In 1905, public health engineers in an industrial river city completed a municipal slow-sand water filtration plant to remove waterborne pathogens from the city’s drinking supply. Historians cite the city’s annual typhoid mortality records as clear evidence that sand filtration sharply reduced deaths from the disease within two years of installation.</p>',
            'Which choice best describes data from the graph that support the historians’ claim?',
            [
                'Annual typhoid deaths rose from 68 per 100,000 residents in 1903 to 72 per 100,000 residents in 1907.',
                'In the two years before filtration was installed, annual typhoid deaths increased slightly from 68 to 72 per 100,000 residents.',
                'Annual typhoid deaths fell completely to 0 per 100,000 residents in 1907, two years after installation.',
                'After standing at 72 deaths per 100,000 residents in 1904, annual typhoid mortality fell to 38 in 1905 and dropped further to just 9 per 100,000 residents by 1907.',
            ],
            'D',
            'Kiểm tra số liệu từng cột: 1903 = 68; 1904 = 72; 1905 (lắp đặt hệ thống lọc cát) = 38; 1906 = 14; 1907 (sau 2 năm) = 9. Đáp án D trích dẫn chính xác đà giảm mạnh từ 72 (1904) xuống 38 (1905) và chỉ còn 9 (1907) — chứng minh trực tiếp khẳng định của các sử gia!',
            'Đối chiếu từng con số và năm giữa đáp án với nhãn trên đầu cột biểu đồ để loại nhanh các đáp án sai số liệu (A, C) và đáp án chỉ nói giai đoạn trước khi lọc nước (B).',
            [
                ('False Data', 'Sai hoàn toàn số liệu năm 1907: cột năm 1907 là 9, không phải 72.'),
                ('True Data / Wrong Claim', 'Số liệu năm 1903–1904 đúng (68 → 72) nhưng chỉ nói giai đoạn TRƯỚC khi lắp lọc cát, không chứng minh hiệu quả giảm tử vong sau năm 1905.'),
                ('False Data', 'Số liệu năm 1907 là 9 ca/100.000 dân chứ không giảm về 0.'),
                ('Đáp án đúng', 'Trích đúng số liệu từng mốc (72 năm 1904 → 38 năm 1905 → 9 năm 1907), chứng minh mức giảm mạnh trong vòng 2 năm sau lắp đặt.'),
            ],
        ),
        q_item(
            'm4_m2l_q14', 14, 'Information and Ideas', 'Command of Evidence (Quantitative)', 'Medium',
            q14_table + '<p>Biomedical engineers are developing washable smart fabrics that harvest mechanical energy from elbow and knee movement to power pulse monitors. A research team notes that although the silk-graphene blend endures the most wash cycles, the barium titanate composite produces the highest voltage output at both shallow and deep bending angles while still surviving dozens of washes.</p>',
            'Which choice best describes data from the table that support the research team’s observation?',
            [
                'Proto D (Silk-Graphene Blend) generated 610 mV at a 90° bend and survived 80 wash cycles, outperforming every other prototype.',
                'While Proto D survived the highest number of wash cycles (80), Proto C (Barium Titanate Composite) produced the highest voltage at both 30° (240 mV) and 90° (610 mV) while withstanding 45 wash cycles.',
                'Proto B (ZnO Nanowire) generated 420 mV at a 90° bend, which was higher than the 310 mV produced by Proto A (PVDF Polymer) at the same angle.',
                'Proto C survived more wash cycles (45) than Proto A (50) and produced a lower voltage at a 30° bend than Proto B.',
            ],
            'B',
            'Đối chiếu 3 ý trong nhận xét của nhóm nghiên cứu với bảng số liệu: (1) Silk-Graphene Blend (Proto D) chịu nhiều chu kỳ giặt nhất = 80 lần; (2) Barium Titanate Composite (Proto C) tạo điện áp cao nhất ở cả góc gập nông 30° (240 mV) lẫn góc gập sâu 90° (610 mV); (3) Proto C vẫn chịu được hàng chục lần giặt = 45 lần. Đáp án B khớp 100% từng ô dữ liệu!',
            'Khi nhận xét so sánh hai mẫu (Proto D vs. Proto C) trên nhiều cột, kiểm tra tuần tự từng con số theo đúng hàng để tránh bẫy đọc nhầm hàng như A hoặc so sánh ngược số như D.',
            [
                ('False Data (Row Mixing)', 'Proto D chỉ đạt 210 mV ở góc 90°; con số 610 mV là của Proto C.'),
                ('Đáp án đúng', 'Khớp chính xác 100% số liệu của cả Proto D (80 lần giặt) và Proto C (240 mV ở 30°, 610 mV ở 90°, 45 lần giặt).'),
                ('True Data / Wrong Claim', 'Số liệu đúng bảng nhưng chỉ so sánh Proto B với Proto A, không nhắc đến Proto D hay Proto C trong nhận xét.'),
                ('False Data', '45 ít hơn 50 (không phải nhiều hơn), và ở góc 30° thì Proto C (240 mV) cao hơn Proto B (185 mV).'),
            ],
        ),

        # Q15: Information and Ideas — Inferences
        q_item(
            'm4_m2l_q15', 15, 'Information and Ideas', 'Inferences', 'Medium',
            '<p>No complete manuscript written directly by the fourth-century Alexandrian mathematician and astronomer Hypatia has survived to the present day. Nevertheless, surviving letters written by her devoted student Synesius of Cyrene praise her lectures on geometry and philosophy and explicitly ask her to construct a brass hydrometer and an astrolabe for his astronomical studies. Historians therefore conclude that even without Hypatia’s original treatises, ______</p>',
            'Which choice most logically completes the text?',
            [
                'contemporary accounts from her students provide reliable evidence of both her respected status as a teacher and her practical skill with scientific instruments.',
                'Synesius of Cyrene must have invented both the brass hydrometer and the astrolabe without any help from Alexandrian scholars.',
                'Hypatia focused exclusively on literature and never taught mathematics or astronomy in Alexandria.',
                'every manuscript written in fourth-century Alexandria was destroyed before Synesius composed his letters.',
            ],
            'A',
            'Xâu chuỗi bằng chứng từ lá thư còn lưu lại của học trò Synesius: (1) khen ngợi bài giảng hình học và triết học của Hypatia → chứng minh vị thế đáng kính của bà trong vai trò người thầy; (2) trực tiếp nhờ bà chế tạo tỷ trọng kế bằng đồng và thước đo thiên văn (astrolabe) → chứng minh tay nghề thực hành chế tạo dụng cụ khoa học của bà → kết luận hợp lý nhất là A!',
            'Kết luận đúng trong Inferences phải bám sát CHÍNH XÁC hai mảnh bằng chứng vừa nêu ở câu trước ("praise her lectures" + "ask her to construct... instruments"), không suy diễn quá đà.',
            [
                ('Đáp án đúng', 'Tổng hợp chính xác hai bằng chứng từ thư của Synesius: danh tiếng giảng dạy và kỹ năng chế tạo dụng cụ khoa học thực tế của Hypatia.'),
                ('Reversed Logic', 'Synesius nhờ Hypatia chế tạo thiết bị chứ không phải ông tự phát minh không cần ai giúp.'),
                ('Contradicted', 'Đoạn văn gọi rõ bà là nhà toán học – thiên văn học dạy hình học và triết học.'),
                ('Contradicted / Extreme', 'Bản thân các bức thư của Synesius còn tồn tại, và bài không nói mọi bản thảo ở Alexandria bị hủy trước khi ông viết thư.'),
            ],
        ),

        # Q16–Q19: Standard English Conventions — Boundaries
        q_item(
            'm4_m2l_q16', 16, 'Standard English Conventions', 'Boundaries', 'Easy',
            '<p>In 1928, British bacteriologist Frederick Griffith studied two strains of pneumonia ______ one strain possessed a smooth protective capsule that caused lethal infection in mice, whereas the rough strain lacked that capsule and was harmless.</p>',
            STEM_SEC,
            ['bacteria,', 'bacteria', 'bacteria:', 'bacteria, and while'],
            'C',
            'Vế trước chỗ trống là một Mệnh đề Độc lập hoàn chỉnh giới thiệu "two strains of pneumonia bacteria". Vế sau giải thích cụ thể từng chủng trong hai chủng đó ("one strain possessed..., whereas the rough strain lacked..."). Dùng dấu hai chấm (`:`) sau IC để giải thích/liệt kê chi tiết là chuẩn xác tuyệt đối (C)!',
            'Thấy vế trước giới thiệu một cụm số lượng ("two strains...") rồi vế sau mô tả cụ thể từng cái → dấu hai chấm (`:`) là lựa chọn số 1, loại ngay Comma Splice (A) và Run-on (B).',
            [
                ('Comma Splice', 'Chỉ dùng dấu phẩy nối hai mệnh đề độc lập gây lỗi Comma Splice.'),
                ('Run-on Sentence', 'Không có dấu câu giữa hai mệnh đề độc lập tạo lỗi câu dính liền.'),
                ('Đáp án đúng', 'Dấu hai chấm (:) đứng sau mệnh đề độc lập hoàn chỉnh để giới thiệu phần giải thích chi tiết về hai chủng vi khuẩn.'),
                ('Fragment / Broken Structure', '", and while" phá vỡ quan hệ đối chiếu vốn đã có liên từ "whereas" ở vế sau, khiến câu hỏng cấu trúc.'),
            ],
        ),
        q_item(
            'm4_m2l_q17', 17, 'Standard English Conventions', 'Boundaries', 'Easy',
            '<p>During its 2012 solo descent to the Mariana Trench’s Challenger Deep, the submersible <i>Deepsea Challenger</i> collected sediment samples from nearly eleven kilometers below the ______ and captured high-definition video of translucent sea cucumbers gliding across the ocean floor.</p>',
            STEM_SEC,
            ['surface;', 'surface', 'surface,', 'surface.'],
            'B',
            'Chủ ngữ "the submersible Deepsea Challenger" thực hiện HAI động từ song song nối bằng "and": `collected sediment samples... and captured high-definition video...` (Compound Predicate: S + V1 and V2). Theo quy tắc Standard English, KHÔNG đặt bất kỳ dấu phẩy, chấm phẩy hay dấu chấm nào trước `and` khi vế sau không có chủ ngữ riêng → chọn B (0 dấu câu)!',
            'Kiểm tra ngay sau chữ "and": nếu chỉ có Động từ thứ hai (`captured`) mà KHÔNG có Chủ ngữ mới → đó là Compound Predicate → CẤM đặt dấu phẩy hay chấm phẩy trước `and`!',
            [
                ('Semicolon Before Fragment', 'Dấu chấm phẩy không thể đứng trước "and captured..." vì vế sau không phải mệnh đề độc lập.'),
                ('Đáp án đúng', 'Không dấu câu — nối mượt hai vị ngữ song song "collected... and captured..." của cùng một chủ ngữ.'),
                ('No-Comma Zone (V1, and V2)', 'Không đặt dấu phẩy trước "and" khi chỉ nối hai động từ chung một chủ ngữ.'),
                ('Sentence Fragment', 'Dấu chấm biến "And captured high-definition video..." thành mảnh câu thiếu chủ ngữ.'),
            ],
        ),
        q_item(
            'm4_m2l_q18', 18, 'Standard English Conventions', 'Boundaries', 'Medium',
            '<p>Persian polymath Ibn Sina, who compiled the five-volume medical encyclopedia known as <i>The Canon of Medicine</i> in ______ shaped clinical education in both Baghdad and medieval European universities for more than five centuries.</p>',
            STEM_SEC,
            ['1025', '1025;', '1025—', '1025,'],
            'D',
            'Mệnh đề quan hệ không xác định mở bằng dấu phẩy ngay sau "Ibn Sina" (`, who compiled... in 1025`). Để trả lại mạch câu cho động từ chính "shaped", BẮT BUỘC phải đóng bằng dấu phẩy tương ứng ngay sau "1025" → chọn D (`1025,`)!',
            'Mở cụm bổ ngữ bằng `, who` → tìm đúng điểm kết thúc ngay trước động từ chính của câu (`shaped`) và đóng đúng bằng dấu phẩy (,).',
            [
                ('Unclosed Non-Essential Clause', 'Mở bằng `, who` nhưng quên đóng dấu phẩy trước động từ chính "shaped".'),
                ('Semicolon Inside Modifier', 'Dấu chấm phẩy cắt rời chủ ngữ "Persian polymath Ibn Sina" khỏi động từ "shaped".'),
                ('Mismatched Pair (, ... —)', 'Mở mệnh đề bổ sung bằng dấu phẩy thì không được đóng bằng dấu gạch ngang.'),
                ('Đáp án đúng', 'Đóng đúng cặp phẩy cho mệnh đề quan hệ không xác định `, who ... ,` trước động từ chính "shaped".'),
            ],
        ),
        q_item(
            'm4_m2l_q19', 19, 'Standard English Conventions', 'Boundaries', 'Medium',
            '<p>Although public postal banking systems have operated in Japan and much of Western Europe for over a ______ many rural towns in the United States still lack convenient access to low-fee neighborhood financial branches.</p>',
            STEM_SEC,
            ['century,', 'century;', 'century.', 'century, but'],
            'A',
            'Vế trước chỗ trống mở đầu bằng liên từ phụ thuộc "Although" → đó là Mệnh đề Phụ thuộc (DC). Vế sau là Mệnh đề Độc lập (IC: "many rural towns... still lack..."). Công thức chuẩn nối DC đứng trước IC là `[DC] , [IC]` → chọn A (`century,`)! Tuyệt đối tránh D (`Although ... , but`) vì thừa liên từ đối lập!',
            'Gặp "Although / Because / While" ở đầu câu → kết thúc mệnh đề phụ thuộc bằng MỘT dấu phẩy đơn, KHÔNG dùng chấm (.), chấm phẩy (;), và KHÔNG thêm "but" hay "so" phía sau!',
            [
                ('Đáp án đúng', 'Dấu phẩy đơn phân tách chuẩn xác mệnh đề phụ thuộc mở đầu bằng "Although" với mệnh đề chính phía sau.'),
                ('Semicolon After Dependent Clause', 'Dấu chấm phẩy cấm đứng sau mệnh đề phụ thuộc "Although...".'),
                ('Sentence Fragment', 'Dấu chấm biến mệnh đề "Although..." thành mảnh vỡ phụ thuộc đứng trơ trọi.'),
                ('Double Conjunction Error', 'Trong tiếng Anh chuẩn, đã dùng "Although" ở đầu câu thì CẤM dùng thêm "but" ở giữa câu.'),
            ],
        ),

        # Q20–Q22: Standard English Conventions — Form, Structure, and Sense
        q_item(
            'm4_m2l_q20', 20, 'Standard English Conventions', 'Form, Structure, and Sense', 'Easy',
            '<p>Each microscopic layer of carbon atoms inside a graphene sheet ______ arranged in a flat hexagonal honeycomb pattern that conducts electricity efficiently.</p>',
            STEM_SEC,
            ['are', 'were', 'is', 'have been'],
            'C',
            'Gạch bỏ các cụm giới từ bổ nghĩa ("of carbon atoms inside a graphene sheet"): Chủ ngữ lõi là "Each microscopic layer" (từ "Each" luôn chia SỐ ÍT!). Đồng thời câu phát biểu một sự thật khoa học hiện tại ("conducts") → chọn động từ hiện tại số ít "is" (C)!',
            'Từ khóa "Each / Every + danh từ số ít" LUÔN đòi hỏi động từ SỐ ÍT, bất chấp các danh từ số nhiều ("atoms") đứng ngay phía sau giới từ "of".',
            [
                ('Subject-Verb Agreement Trap', '"are" là số nhiều, bị lừa bởi danh từ số nhiều "carbon atoms".'),
                ('Subject-Verb Agreement Trap', '"were" vừa sai số nhiều vừa sai thì quá khứ.'),
                ('Đáp án đúng', '"is" là động từ hiện tại số ít hòa hợp hoàn hảo với "Each microscopic layer" và hiện tại đơn "conducts".'),
                ('Subject-Verb Agreement Trap', '"have been" là trợ động từ số nhiều, sai với "Each... layer".'),
            ],
        ),
        q_item(
            'm4_m2l_q21', 21, 'Standard English Conventions', 'Form, Structure, and Sense', 'Medium',
            '<p>In her essay collection <i>Upstream</i>, American poet Mary Oliver recalls walking through coastal marshes at dawn and notes that wild herons rarely allow an impatient observer to approach ______ nests undisturbed.</p>',
            STEM_SEC,
            ['its', 'their', 'they’re', 'it’s'],
            'B',
            'Đại từ sở hữu cần thay cho chủ thể sở hữu "nests" (tổ chim) — chính là "wild herons" (những con diệc hoang, danh từ SỐ NHIỀU) → cần tính từ sở hữu số nhiều `their` (B)!',
            'Bước 1: Xác định đúng danh từ tiền ngữ sở hữu ("nests" thuộc về "wild herons" → số nhiều). Bước 2: Phân biệt tính từ sở hữu `their` với dạng viết tắt `they’re` (= they are).',
            [
                ('Pronoun Number Mismatch', '"its" là sở hữu số ít, không khớp với danh từ số nhiều "wild herons".'),
                ('Đáp án đúng', '"their" là tính từ sở hữu số nhiều khớp hoàn toàn với "wild herons".'),
                ('Contraction Trap', '"they’re" là viết tắt của "they are", sai ngữ pháp trước danh từ "nests".'),
                ('Contraction Trap', '"it’s" là viết tắt của "it is", vừa sai số ít vừa sai dạng rút gọn.'),
            ],
        ),
        q_item(
            'm4_m2l_q22', 22, 'Standard English Conventions', 'Form, Structure, and Sense', 'Medium',
            '<p>In 1911, Norwegian explorer Roald Amundsen established his base camp at the Bay of Whales on Antarctica’s Ross Ice Shelf, carefully stocked supply depots along his planned route, and ______ the geographic South Pole on December 14.</p>',
            STEM_SEC,
            ['reaches', 'will reach', 'reaching', 'reached'],
            'D',
            'Câu kể chuỗi 3 hành động quá khứ liên tiếp năm 1911 của cùng chủ ngữ Roald Amundsen theo cấu trúc song song: `established ..., stocked ..., and ______` → bắt buộc chia đồng bộ ở thì Quá khứ đơn `reached` (D)!',
            'Khi gặp chuỗi liệt kê động từ `V1, V2, and V3`, luôn kiểm tra dạng thức và thì của V1 và V2 (`established`, `stocked`) để điền V3 song song tuyệt đối.',
            [
                ('Tense Shift', '"reaches" ở thì hiện tại đơn, lệch thì với mốc "In 1911" và hai động từ quá khứ trước đó.'),
                ('Tense Shift', '"will reach" ở thì tương lai, vô lý với sự kiện lịch sử năm 1911.'),
                ('Parallelism Error', '"reaching" là phân từ, phá vỡ cấu trúc song song của 3 động từ chia thì quá khứ.'),
                ('Đáp án đúng', '"reached" hòa hợp chuẩn xác về thì quá khứ đơn và cấu trúc song song với "established" và "stocked".'),
            ],
        ),

        # Q23–Q25: Expression of Ideas — Transitions
        q_item(
            'm4_m2l_q23', 23, 'Expression of Ideas', 'Transitions', 'Easy',
            '<p>Many bacteria protect themselves from invading viruses using a genetic defense system known as CRISPR. ______, when a bacteriophage attacks a <i>Streptococcus</i> cell, the bacterium can snip a small segment of the viral DNA and store it in its own genome to recognize and destroy future attacks by the same virus.</p>',
            STEM_TRANS,
            ['For example', 'However', 'Instead', 'In conclusion'],
            'A',
            'Câu 1 nêu nhận định tổng quát ("Many bacteria protect themselves... using CRISPR"). Câu 2 đưa ra một trường hợp cụ thể minh họa cơ chế đó ở vi khuẩn *Streptococcus* → quan hệ Minh họa ví dụ → "For example" (A)!',
            'Khi câu 1 nói chung ("Many bacteria...") và câu 2 thu hẹp vào một loài/tình huống cụ thể ("when a bacteriophage attacks a Streptococcus cell..."), chọn ngay từ nối ví dụ (`For example` / `For instance`).',
            [
                ('Đáp án đúng', 'For example giới thiệu chuẩn xác minh họa cụ thể về cách vi khuẩn Streptococcus dùng CRISPR phòng vệ.'),
                ('False Contrast', 'However chỉ sự đối lập — sai vì câu 2 minh họa cùng chiều cho câu 1.'),
                ('Substitution Trap', 'Instead dùng để thay thế hành động phủ định ở câu trước.'),
                ('Wrong Relationship (Summary)', 'In conclusion dùng để tổng kết toàn bài chứ không dùng để đưa ví dụ chi tiết.'),
            ],
        ),
        q_item(
            'm4_m2l_q24', 24, 'Expression of Ideas', 'Transitions', 'Easy',
            '<p>Perovskite solar cells can be printed cheaply onto flexible plastic films and convert sunlight into electricity almost as efficiently as conventional silicon panels. ______, standard perovskite films degrade quickly when exposed to outdoor humidity and heat, limiting their current commercial lifespan.</p>',
            STEM_TRANS,
            ['Therefore', 'Similarly', 'However', 'Furthermore'],
            'C',
            'Câu 1 nêu ưu điểm nổi bật của pin mặt trời perovskite (in giá rẻ lên màng dẻo, hiệu suất chuyển hóa gần ngang silicon). Câu 2 nêu nhược điểm cản trở (nhanh xuống cấp khi gặp ẩm và nhiệt ngoài trời, giới hạn tuổi thọ thương mại) → Quan hệ Đối lập (Ưu điểm vs. Nhược điểm) → "However" (C)!',
            'Nhận diện ngay cặp chiều nghĩa Tích cực (+) ở câu 1 → Hạn chế/Tiêu cực (-) ở câu 2 để chốt từ nối đối lập (`However`).',
            [
                ('Wrong Relationship (Cause-Effect)', 'Therefore sai vì ưu điểm rẻ và hiệu suất cao không phải nguyên nhân khiến màng pin nhanh hỏng.'),
                ('Wrong Relationship (Comparison)', 'Similarly dùng để so sánh điểm giống nhau giữa hai đối tượng.'),
                ('Đáp án đúng', 'However chuyển mạch chính xác từ ưu điểm của pin perovskite sang hạn chế về độ bền ngoài trời.'),
                ('Wrong Relationship (Addition)', 'Furthermore dùng để thêm một ưu điểm cùng chiều, không dùng để nêu nhược điểm trái ngược.'),
            ],
        ),
        q_item(
            'm4_m2l_q25', 25, 'Expression of Ideas', 'Transitions', 'Medium',
            '<p>Cooperative housing associations in Zurich keep monthly rents affordable by removing land from speculative real-estate markets and capping rents at construction and maintenance costs. ______, these cooperatives frequently dedicate ground-floor space to shared daycare centers, music rooms, and workshops that strengthen ties among neighbors.</p>',
            STEM_TRANS,
            ['Nevertheless', 'Moreover', 'Conversely', 'Instead'],
            'B',
            'Câu 1 nêu lợi ích thứ nhất của mô hình nhà ở hợp tác xã ở Zurich (giữ tiền thuê nhà phải chăng). Câu 2 bổ sung lợi ích thứ hai cùng chiều (dành tầng trệt cho nhà trẻ chung, phòng nhạc và xưởng thủ công giúp gắn kết hàng xóm) → Quan hệ Bổ sung cùng chiều → "Moreover" (Hơn nữa)! Dùng mẹo 3–1: A, C, D đều thuộc nhóm Đối lập → loại cả ba!',
            'Mẹo 3–1 nhanh gọn: 3 từ nhóm Đối lập (`Nevertheless` / `Conversely` / `Instead`) + 1 từ nhóm Bổ sung cùng chiều (`Moreover`) → kiểm tra 2 câu đều nêu ưu điểm rồi chốt B!',
            [
                ('False Contrast', 'Nevertheless chỉ sự trái kỳ vọng — sai vì cả hai câu đều nêu mặt tích cực của hợp tác xã nhà ở.'),
                ('Đáp án đúng', 'Moreover bổ sung mạch lạc lợi ích cộng đồng thứ hai tiếp nối lợi ích giá thuê rẻ ở câu 1.'),
                ('False Contrast', 'Conversely chỉ sự đối nghịch hoàn toàn.'),
                ('Substitution Trap', 'Instead chỉ dùng để nêu lựa chọn thay thế cho vế phủ định trước đó.'),
            ],
        ),

        # Q26–Q27: Expression of Ideas — Rhetorical Synthesis
        q_item(
            'm4_m2l_q26', 26, 'Expression of Ideas', 'Rhetorical Synthesis', 'Easy',
            '''<p>While researching a topic, a student has taken the following notes:</p>
            <ul>
              <li>Marcus Vitruvius Pollio was a Roman architect and military engineer during the first century BCE.</li>
              <li>He wrote <i>De Architectura</i> (<i>On Architecture</i>), the only complete treatise on architecture to survive from classical antiquity.</li>
              <li>In the treatise, Vitruvius argued that every well-designed building must combine three qualities: durability (<i>firmitas</i>), utility (<i>utilitas</i>), and beauty (<i>venustas</i>).</li>
              <li>Renaissance artists such as Leonardo da Vinci later studied Vitruvius’s writings on proportion.</li>
            </ul>''',
            'The student wants to summarize the three qualities that Vitruvius argued every well-designed building must possess. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
            [
                'Marcus Vitruvius Pollio worked as both a Roman architect and a military engineer during the first century BCE.',
                'Centuries after the Roman Empire fell, Renaissance artists such as Leonardo da Vinci studied Vitruvius’s writings on proportion.',
                'Written by Marcus Vitruvius Pollio, <i>De Architectura</i> is the only complete architectural treatise surviving from classical antiquity.',
                'In his surviving treatise <i>De Architectura</i>, the Roman architect Vitruvius argued that every well-designed building must combine durability, utility, and beauty.',
            ],
            'D',
            'Goal-First SOP: Mục tiêu hỏi trực tiếp "summarize the three qualities that Vitruvius argued every well-designed building must possess" (tóm tắt 3 phẩm chất của một công trình kiến trúc tốt). Chỉ có duy nhất đáp án D liệt kê đủ 3 phẩm chất: durability (độ bền), utility (công năng) và beauty (vẻ đẹp)!',
            'Đọc câu hỏi Goal trước khi đọc ghi chú: chỉ cần quét nhanh 4 lựa chọn xem câu nào chứa đúng 3 phẩm chất (durability, utility, beauty) là chốt ngay trong 5 giây!',
            [
                ('Wrong Synthesis Goal', 'Chỉ nêu nghề nghiệp và thời đại của Vitruvius, không nhắc 3 phẩm chất kiến trúc.'),
                ('Wrong Synthesis Goal', 'Chỉ nói về ảnh hưởng tới Leonardo da Vinci thời Phục hưng.'),
                ('Wrong Synthesis Goal', 'Chỉ nêu việc tác phẩm còn sót lại từ thời cổ đại mà bỏ sót 3 phẩm chất.'),
                ('Đáp án đúng', 'Tóm gọn chính xác cả 3 phẩm chất kiến trúc mà Vitruvius đề ra: durability, utility và beauty.'),
            ],
        ),
        q_item(
            'm4_m2l_q27', 27, 'Expression of Ideas', 'Rhetorical Synthesis', 'Medium',
            '''<p>While researching a topic, a student has taken the following notes:</p>
            <ul>
              <li>Both hydrothermal vents and cold seeps are deep-sea ecosystems that support marine life without sunlight through chemosynthesis.</li>
              <li>Hydrothermal vents occur mainly along volcanic mid-ocean ridges, where superheated mineral-rich water erupts from the seafloor at temperatures above 300 degrees Celsius.</li>
              <li>Cold seeps occur along continental margins, where methane and hydrogen sulfide slowly bubble up through seafloor sediments at ambient near-freezing temperatures.</li>
              <li>Because cold seeps release chemicals slowly over thousands of years, some tubeworm species living there can grow to be more than 250 years old.</li>
            </ul>''',
            'The student wants to emphasize both a similarity and a difference between hydrothermal vents and cold seeps. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
            [
                'Both hydrothermal vents and cold seeps are sunless deep-sea ecosystems that rely on chemosynthesis to support marine life.',
                'Cold seeps along continental margins release methane and hydrogen sulfide slowly at near-freezing temperatures, allowing some tubeworms to live over 250 years.',
                'Although both hydrothermal vents and cold seeps sustain sunless deep-sea ecosystems through chemosynthesis, hydrothermal vents erupt with superheated water above 300 degrees Celsius along mid-ocean ridges, whereas cold seeps release chemicals slowly at near-freezing temperatures along continental margins.',
                'Hydrothermal vents erupt with superheated mineral-rich water along volcanic mid-ocean ridges, whereas some tubeworms near cold seeps can grow to be more than 250 years old.',
            ],
            'C',
            'Goal-First SOP: Mục tiêu yêu cầu ĐỦ CẢ HAI VẾ: (1) một ĐIỂM GIỐNG NHAU (đều là hệ sinh thái biển sâu không ánh nắng duy trì bằng hóa tổng hợp), VÀ (2) một ĐIỂM KHÁC BIỆT (miệng phun thủy nhiệt phun nước siêu nóng >300°C ở sống núi giữa đại dương, còn mạch thấm lạnh giải phóng hóa chất chậm ở nhiệt độ gần đóng băng dọc rìa lục địa). A chỉ có điểm giống; B chỉ nói 1 đối tượng; D thiếu điểm giống. Chỉ C trọn vẹn cả hai vế!',
            'Gặp yêu cầu "both a similarity and a difference", cấu trúc vàng luôn là "Although both X and Y [similarity], X [feature 1], whereas Y [feature 2]."',
            [
                ('Half-Match Trap', 'Chỉ nêu điểm giống nhau (hóa tổng hợp không ánh sáng), thiếu hẳn điểm khác biệt.'),
                ('Single Subject Trap', 'Chỉ trình bày thông tin về cold seeps, hoàn toàn không nhắc tới hydrothermal vents.'),
                ('Đáp án đúng', 'Đáp ứng trọn vẹn cả điểm giống nhau (chemosynthesis không ánh nắng) lẫn điểm khác biệt trực tiếp (nhiệt độ & vị trí địa chất) giữa hai hệ sinh thái.'),
                ('Half-Match Trap', 'Chỉ nêu khác biệt (và ghép hai tiêu chí không cân xứng) mà bỏ sót hoàn toàn điểm giống nhau.'),
            ],
        ),
    ]
