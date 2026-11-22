# -*- coding: utf-8 -*-
"""
Digital SAT R&W Adaptive Mock Test #4 — Module 1 (27 Questions, Medium/Hard Mix)
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


def get_m1_questions():
    q13_chart = svg_bar_chart(
        'Mean Reduction in Biofilm Bacteria (%) After 24 Hours by Treatment',
        ['0%', '25%', '50%', '75%', '100%'],
        [
            ('Control', 4, '4%'),
            ('Antibiotic Only', 28, '28%'),
            ('Phage Only', 52, '52%'),
            ('Phage+Antibiotic', 89, '89%'),
        ],
        100,
    )

    q14_table = html_table(
        'Civic Participation and Public Third-Place Density in Four Cities (2024)',
        ['City', 'Third Places per 10k Residents', 'Median Household Income ($)', 'Voter Turnout (%)', 'Volunteer Rate (%)'],
        [
            ['Aarhus', '14.2', '64,500', '78%', '46%'],
            ['Braga', '13.8', '38,200', '74%', '43%'],
            ['Calgary', '6.5', '76,800', '54%', '29%'],
            ['Dresden', '11.4', '51,900', '69%', '39%'],
        ],
    )

    return [
        # Q1–Q5: Craft and Structure — Words in Context
        q_item(
            'm4_m1_q1', 1, 'Craft and Structure', 'Words in Context', 'Medium',
            '<p>In the light organs of the Hawaiian bobtail squid, symbiotic <i>Vibrio fischeri</i> bacteria do not glow continuously while floating at low densities in open seawater. Instead, individual cells ______ luminescence until their population multiplies enough for shared chemical signals to trigger synchronized illumination.</p>',
            STEM_WIC,
            ['intensify', 'withhold', 'exaggerate', 'dissipate'],
            'B',
            'Câu 1 khẳng định vi khuẩn "do not glow continuously" ở mật độ thấp. Câu 2 dùng "Instead" giải thích: từng tế bào riêng lẻ kìm giữ / chưa phát sáng cho đến khi mật độ đạt ngưỡng kích hoạt đồng bộ → "withhold" (giữ lại, không phóng thích).',
            'Khóa cụm phủ định ở câu trước ("do not glow continuously") và mốc điều kiện ("until...") để suy ra động từ mang nghĩa "tạm giữ lại chưa phát ra".',
            [
                ('Opposite Meaning', 'intensify = làm mạnh thêm — mâu thuẫn với việc chưa phát sáng ở mật độ thấp.'),
                ('Đáp án đúng', 'withhold = kìm lại / chưa giải phóng, khớp hoàn toàn với việc chỉ phát sáng sau khi đạt ngưỡng mật độ.'),
                ('Wrong Meaning', 'exaggerate = phóng đại — không phù hợp với hiện tượng phát quang sinh học.'),
                ('Wrong Meaning', 'dissipate = làm tiêu tan ánh sáng đã có — sai vì vi khuẩn vốn chưa phát sáng.'),
            ],
        ),
        q_item(
            'm4_m1_q2', 2, 'Craft and Structure', 'Words in Context', 'Medium',
            '<p>Unlike medieval European cartographers who copied ancient Ptolemaic coastlines without revision, twelfth-century geographer Muhammad al-Idrisi spent fifteen years interviewing merchants and sailors at the Sicilian court, producing a world atlas notable for its ______: even distant port distances were cross-checked against eyewitness itineraries.</p>',
            STEM_WIC,
            ['brevity', 'obscurity', 'ornamentation', 'empiricism'],
            'D',
            'Sau dấu hai chấm (:) là mệnh đề giải nghĩa trực tiếp cho chỗ trống: "cross-checked against eyewitness itineraries" (đối chiếu chéo với nhật ký nhân chứng thực địa) cùng với việc phỏng vấn thương nhân và thủy thủ suốt 15 năm → đặc trưng của chủ nghĩa thực nghiệm dựa trên quan sát trực tiếp → "empiricism".',
            'Khi chỗ trống đứng ngay trước dấu hai chấm (:), phần giải thích phía sau chính là định nghĩa trực tiếp của từ cần điền.',
            [
                ('Wrong Meaning', 'brevity = sự ngắn gọn — trái ngược với công trình đồ sộ nghiên cứu suốt 15 năm.'),
                ('Wrong Meaning', 'obscurity = sự tối nghĩa/ít người biết — không liên quan đến việc kiểm chứng thực địa.'),
                ('Wrong Meaning', 'ornamentation = sự trang trí cầu kỳ — không khớp với vế giải thích về kiểm chứng dữ liệu nhân chứng.'),
                ('Đáp án đúng', 'empiricism = tính thực nghiệm (dựa trên quan sát và bằng chứng thực tế), khớp hoàn hảo với việc phỏng vấn và đối chiếu lộ trình thực tế.'),
            ],
        ),
        q_item(
            'm4_m1_q3', 3, 'Craft and Structure', 'Words in Context', 'Medium',
            '<p>Naval architects warned that Arctic pack ice would crush any wooden vessel trapped through winter, yet Norwegian explorer Fridtjof Nansen built the <i>Fram</i> with a rounded, keel-less hull that let advancing ice floes lift the ship upward rather than crack its ribs; this hull geometry effectively ______ the lateral pressure of the frozen sea.</p>',
            STEM_WIC,
            ['neutralized', 'compounded', 'replicated', 'solicited'],
            'A',
            'Thiết kế thân tàu tròn giúp tảng băng đẩy tàu trượt lên trên thay vì ép vỡ mạn tàu → hình học thân tàu đã "vô hiệu hóa" áp lực ép ngang của biển băng → "neutralized".',
            'Tập trung vào quan hệ nhân-quả sau dấu chấm phẩy: tàu được nâng lên thay vì bị ép vỡ = áp lực ngang đã bị hóa giải/vô hiệu hóa.',
            [
                ('Đáp án đúng', 'neutralized = vô hiệu hóa / triệt tiêu tác động nguy hiểm của áp lực băng ép.'),
                ('Opposite Meaning', 'compounded = làm trầm trọng thêm — ngược hoàn toàn với kết quả bảo vệ tàu.'),
                ('Wrong Meaning', 'replicated = sao chép/tái tạo — thân tàu không sao chép áp lực của băng.'),
                ('Wrong Meaning', 'solicited = kêu gọi/thỉnh cầu — không hợp ngữ cảnh vật lý.'),
            ],
        ),
        q_item(
            'm4_m1_q4', 4, 'Craft and Structure', 'Words in Context', 'Hard',
            '<p>Conventional metallic robotic claws often tear delicate gelatinous organisms during deep-sea specimen collection. Because soft actuators cast from liquid-crystal elastomers conform gently to irregular surfaces, marine roboticists designed them to ______ the mechanical trauma associated with rigid manipulators.</p>',
            STEM_WIC,
            ['precipitate', 'substantiate', 'mitigate', 'enumerate'],
            'C',
            'Càng robot kim loại cứng làm rách sinh vật biển mềm yếu, còn bộ chấp hành mềm ôm nhẹ theo bề mặt không đều → được thiết kế để "giảm thiểu" chấn thương cơ học → "mitigate".',
            'Khóa cặp đối chiếu: rigid claws ("tear delicate organisms") vs. soft actuators ("conform gently") → động từ phải mang nghĩa giảm bớt tác hại.',
            [
                ('Opposite Meaning', 'precipitate = gây ra đột ngột/thúc đẩy nhanh — sai vì bộ kẹp mềm nhằm tránh gây tổn thương.'),
                ('Wrong Meaning', 'substantiate = chứng minh bằng bằng chứng — không đi với "mechanical trauma".'),
                ('Đáp án đúng', 'mitigate = làm giảm nhẹ / giảm thiểu tổn thương cơ học, chuẩn xác về ngữ nghĩa và sắc thái học thuật.'),
                ('Wrong Meaning', 'enumerate = liệt kê từng mục — sai hoàn toàn ngữ cảnh kỹ thuật.'),
            ],
        ),
        q_item(
            'm4_m1_q5', 5, 'Craft and Structure', 'Words in Context', 'Hard',
            '<p>Readers sometimes assume that seventeenth-century Japanese poet Matsuo Bashō’s travel diary <i>Oku no Hosomichi</i> provides an unedited log of his journey across northern Honshu. Yet notebooks kept by his traveling companion Sora reveal that Bashō altered dates, rearranged routes, and invented roadside encounters—aesthetic liberties that ______ the diary’s reputation as a purely documentary chronicle.</p>',
            STEM_WIC,
            ['complicate', 'vindicate', 'standardize', 'supersede'],
            'A',
            'Người đọc tưởng nhật ký là ghi chép nguyên bản, nhưng sổ tay người bạn đồng hành cho thấy Bashō đã chỉnh ngày, đổi lộ trình và hư cấu cuộc gặp gỡ → những tự do nghệ thuật này làm "phức tạp hóa / thách thức tính đơn giản của" danh tiếng ghi chép thuần tư liệu → "complicate" (từ cực kinh điển của Digital SAT).',
            'Trên Digital SAT, "complicate" thường mang nghĩa học thuật là "làm cho một nhận định/danh tiếng đơn giản trở nên phức tạp hơn, không còn đúng tuyệt đối".',
            [
                ('Đáp án đúng', 'complicate = làm phức tạp hóa / phủ bóng nghi vấn lên danh tiếng "thuần tư liệu" của tác phẩm.'),
                ('Opposite Meaning', 'vindicate = chứng minh là đúng/minh oan — ngược với bằng chứng Bashō đã hư cấu chi tiết.'),
                ('Wrong Meaning', 'standardize = tiêu chuẩn hóa — không khớp với việc chỉnh sửa ngày tháng mang tính nghệ thuật.'),
                ('Wrong Meaning', 'supersede = thay thế hoàn toàn — "aesthetic liberties" không thể thay thế một "reputation".'),
            ],
        ),

        # Q6–Q7: Craft and Structure — Text Structure and Purpose
        q_item(
            'm4_m1_q6', 6, 'Craft and Structure', 'Text Structure and Purpose', 'Medium',
            '<p>During London’s 1854 cholera outbreak, most physicians endorsed miasma theory, attributing the epidemic to noxious vapors rising from decaying matter. Physician John Snow doubted this consensus and mapped every fatal case in Soho by street address. <u>Clustering the deaths around a single communal water pump on Broad Street, his map also showed that workers at a nearby brewery—who drank malt liquor rather than pump water—escaped the disease almost entirely.</u> When municipal officials removed the pump handle at Snow’s urging, local transmission subsided, laying a methodological cornerstone for modern epidemiology.</p>',
            'Which choice best describes the function of the underlined sentence in the text as a whole?',
            [
                'It explains the biochemical process by which malt liquor prevents cholera bacteria from multiplying.',
                'It summarizes why most nineteenth-century London physicians continued to defend miasma theory after 1854.',
                'It presents spatial evidence from Snow’s mapping that linked the outbreak to a contaminated water source rather than airborne vapors.',
                'It highlights a statistical error in Snow’s records that initially delayed the removal of the Broad Street pump handle.',
            ],
            'C',
            'Câu trước nêu việc John Snow nghi ngờ thuyết chướng khí (miasma) và vẽ bản đồ ca tử vong. Câu gạch chân trình bày bằng chứng không gian từ bản đồ (tử vong tụ quanh bơm nước Broad Street, còn công nhân xưởng bia gần đó không uống nước bơm lại thoát bệnh), liên kết dịch bệnh với nguồn nước thay vì hơi độc trong không khí.',
            'Với câu hỏi Function of Underlined Sentence, nối vai trò của câu gạch chân với câu liền trước (hoài nghi miasma + vẽ bản đồ) và câu liền sau (tháo tay bơm → dịch giảm).',
            [
                ('Out of Scope', 'Đoạn văn không giải thích cơ chế sinh hóa nào của bia mạch nha.'),
                ('Out of Scope', 'Câu gạch chân không nói về lý do bác sĩ tiếp tục bảo vệ thuyết miasma sau năm 1854.'),
                ('Đáp án đúng', 'Mô tả chính xác chức năng: cung cấp bằng chứng không gian gắn ổ dịch với bơm nước Broad Street thay vì không khí.'),
                ('Reversed Logic', 'Chi tiết xưởng bia củng cố phát hiện của Snow chứ không phải lỗi thống kê.'),
            ],
        ),
        q_item(
            'm4_m1_q7', 7, 'Craft and Structure', 'Text Structure and Purpose', 'Hard',
            '<p>Unlike pigments, which produce color by absorbing specific wavelengths of light and gradually fade under sunlight, the iridescent blue of <i>Morpho</i> butterfly wings arises from microscopic ridges spaced roughly 200 nanometers apart. Because these chitin nanostructures scatter blue wavelengths through constructive optical interference, the wings retain their brilliance for centuries in museum collections. Inspired by this architecture, materials scientists in Delft have imprinted analogous silicon-nitride nanogratings onto architectural glass, achieving vivid, pigment-free exterior coatings that resist ultraviolet degradation.</p>',
            'Which choice best describes the overall structure of the text?',
            [
                'It introduces a debate among physicists over structural color and then resolves it through museum measurements of butterfly specimens.',
                'It explains how a biological nanostructure produces durable color unlike chemical pigments and then describes an engineering application modeled on that structure.',
                'It criticizes conventional architectural glass coatings for environmental toxicity and then recommends replacing them with natural chitin.',
                'It traces the chronological history of optical interference theory from nineteenth-century entomology to modern solar-panel manufacturing.',
            ],
            'B',
            'Bố cục 2 phần rõ rệt: (1) Câu 1–2 đối chiếu sắc tố hóa học (hay phai màu) với cấu trúc nano trên cánh bướm Morpho (tạo màu bền hàng thế kỷ nhờ giao thoa quang học); (2) Câu 3 ("Inspired by this architecture...") trình bày ứng dụng kỹ thuật lấy cảm hứng từ cấu trúc sinh học đó lên kính kiến trúc bằng silicon-nitride.',
            'Tách đoạn văn thành 2–3 bước chuyển ý chính và loại ngay các đáp án thêm chi tiết không hề có trong bài ("debate", "toxicity", "solar-panel").',
            [
                ('Out of Scope', 'Không có cuộc tranh luận nào giữa các nhà vật lý được nhắc tới trong đoạn văn.'),
                ('Đáp án đúng', 'Khớp từng chặng bố cục: giải thích cơ chế màu cấu trúc bền vững ở cánh bướm (khác sắc tố) → mô tả lớp phủ kính mô phỏng cấu trúc đó.'),
                ('Distorted Detail', 'Bài dùng silicon-nitride mô phỏng cấu trúc chứ không dùng chitin tự nhiên, và không nhắc độc tính môi trường.'),
                ('Out of Scope', 'Đoạn văn không trình bày lịch sử theo trình tự thời gian và không đề cập pin mặt trời.'),
            ],
        ),

        # Q8: Craft and Structure — Cross-Text Connections
        q_item(
            'm4_m1_q8', 8, 'Craft and Structure', 'Cross-Text Connections', 'Hard',
            '<p><b>Text 1</b><br/>Political scientist Renata Oliveira contends that municipal participatory budgeting—a process allowing residents to vote directly on how a share of city capital funds is spent—substantially narrows civic inequality. Analyzing twelve years of municipal records in Porto Alegre, Brazil, she found that after participatory assemblies began, water-pipe installation and street paving expanded far more rapidly in low-income peripheral districts than in affluent neighborhoods.</p>'
            '<p><b>Text 2</b><br/>Sociologist Tomasz Kowalski observes that while Porto Alegre’s early participatory budgeting redirected public infrastructure toward poorer wards, more recent adaptations across European and North American cities often devote less than two percent of municipal budgets to resident votes. Moreover, Kowalski’s attendance surveys show that evening assembly schedules disproportionately exclude shift workers, causing many contemporary programs to amplify the preferences of wealthier homeowners.</p>',
            'Based on the texts, how would Tomasz Kowalski (Text 2) most likely respond to Renata Oliveira’s conclusion (Text 1)?',
            [
                'By disputing Oliveira’s spending records and arguing that low-income neighborhoods in Porto Alegre received no infrastructure improvements.',
                'By asserting that participatory budgeting works better in European and North American cities than it ever did in Brazil.',
                'By claiming that public infrastructure projects such as water pipes should never be funded through municipal capital budgets.',
                'By acknowledging that participatory budgeting narrowed disparities in Porto Alegre’s early experience while arguing that smaller budget allocations and scheduling barriers often undermine that effect in newer programs.',
            ],
            'D',
            'Text 2 mở đầu bằng nhượng bộ rõ ràng ("while Porto Alegre’s early participatory budgeting redirected public infrastructure toward poorer wards") — tức thừa nhận kết quả ở Porto Alegre — nhưng lập luận rằng các mô hình mới hơn tại châu Âu và Bắc Mỹ cấp ngân sách quá nhỏ (<2%) và giờ họp buổi tối loại trừ công nhân làm ca, khiến hiệu quả giảm bất bình đẳng bị đảo ngược.',
            'Với câu Cross-Text có cấu trúc nhượng bộ "while X, Y", đáp án chuẩn luôn giữ đủ cả hai vế: thừa nhận trường hợp gốc (Porto Alegre) + nêu điều kiện làm suy yếu ở các chương trình mới.',
            [
                ('Extreme / Contradicted', 'Kowalski thừa nhận rõ ràng Porto Alegre đã chuyển hạ tầng về các khu nghèo hơn, không bác bỏ dữ liệu này.'),
                ('Reversed Logic', 'Ngược hoàn toàn: Kowalski cho rằng các bản triển khai ở châu Âu/Bắc Mỹ kém công bằng hơn mô hình đầu ở Porto Alegre.'),
                ('Out of Scope', 'Text 2 không hề nói ống nước không nên tài trợ từ ngân sách đô thị.'),
                ('Đáp án đúng', 'Tóm gọn chính xác lập trường nhượng bộ + phản biện của Kowalski: công nhận Porto Alegre, chỉ ra hạn chế tỷ trọng ngân sách và rào cản giờ họp ở mô hình mới.'),
            ],
        ),

        # Q9–Q10: Information and Ideas — Central Ideas and Details
        q_item(
            'm4_m1_q9', 9, 'Information and Ideas', 'Central Ideas and Details', 'Medium',
            '<p>When the deep-sea submersible <i>Alvin</i> first photographed two-meter-long tube worms (<i>Riftia pachyptila</i>) clustered around Galápagos Rift hydrothermal vents in 1977, marine biologists were baffled to discover that adult worms lack both a mouth and a digestive tract. Subsequent anatomical studies solved the puzzle: the worms’ blood transports dissolved hydrogen sulfide and oxygen from superheated vent plumes into a specialized internal organ called the trophosome, where billions of symbiotic bacteria convert those inorganic compounds into organic nutrients that sustain the host.</p>',
            'Which choice best states the main idea of the text?',
            [
                'Adult giant tube worms thrive near hydrothermal vents without a digestive tract by relying on internal symbiotic bacteria to synthesize nutrients from vent chemicals.',
                'The 1977 expedition of the submersible <i>Alvin</i> proved that hydrothermal vents contain higher concentrations of oxygen than surface ocean waters.',
                'Because giant tube worms lose their mouths during adulthood, they can survive only by migrating periodically between shallow reefs and deep ocean rifts.',
                'Symbiotic bacteria inside the trophosome protect giant tube worms from the extreme temperatures of superheated hydrothermal plumes.',
            ],
            'A',
            'Đoạn văn đặt câu đố (giun ống khổng lồ trưởng thành không có miệng và ống tiêu hóa) rồi giải đáp trực tiếp ở câu hai: máu giun đưa H₂S và O₂ vào cơ quan trophosome để hàng tỷ vi khuẩn cộng sinh hóa tổng hợp chất hữu cơ nuôi sống vật chủ → đáp án A tóm trọn ý trung tâm.',
            'Main Idea phải bao phủ cả câu hỏi/bối cảnh lẫn lời giải cốt lõi của đoạn văn, không sa vào chi tiết bịa đặt hoặc ngoài phạm vi.',
            [
                ('Đáp án đúng', 'Tóm tắt chính xác cách giun ống khổng lồ sống không cần ống tiêu hóa nhờ vi khuẩn cộng sinh chuyển hóa hóa chất miệng phun thủy nhiệt.'),
                ('Out of Scope', 'Bài không so sánh nồng độ oxy giữa miệng phun thủy nhiệt và nước tầng mặt.'),
                ('Contradicted / Fabricated', 'Bài không hề nói giun ống di cư lên rạn san hô nông.'),
                ('Distorted Detail', 'Vi khuẩn trong trophosome tạo chất dinh dưỡng chứ không được mô tả là lá chắn cách nhiệt.'),
            ],
        ),
        q_item(
            'm4_m1_q10', 10, 'Information and Ideas', 'Central Ideas and Details', 'Hard',
            '<p>Modern Portland-cement seawalls typically corrode within fifty years as saltwater penetrates steel reinforcement bars, yet harbor piers poured by Roman engineers two millennia ago remain structurally intact under Mediterranean waves. For decades, historians attributed this longevity solely to volcanic ash (<i>pozzolana</i>) mined near Pozzuoli. However, high-resolution spectroscopy conducted in 2023 revealed that Roman builders also practiced “hot mixing” with quicklime, leaving millimeter-scale calcium clasts embedded throughout the mortar; whenever hairline cracks admit seawater, these clasts dissolve and recrystallize as calcite, autonomously sealing fractures before structural failure occurs.</p>',
            'According to the text, what did the 2023 spectroscopic analysis reveal about Roman maritime concrete?',
            [
                'It lacked volcanic ash altogether and instead relied exclusively on steel reinforcements coated in calcite.',
                'It degrades at roughly the same fifty-year rate as Portland cement whenever seawater penetrates hairline fractures.',
                'Quicklime clasts formed during hot mixing react with infiltrating seawater to precipitate calcite that self-heals small cracks.',
                'Roman engineers intentionally submerged finished piers in freshwater ponds before exposing them to Mediterranean waves.',
            ],
            'C',
            'Câu cuối nêu trực tiếp kết quả quang phổ năm 2023: kỹ thuật trộn nóng với vôi sống (quicklime) để lại các hạt canxi cỡ milimet trong vữa; khi vết nứt li ti đón nước biển, hạt này hòa tan rồi kết tinh lại thành canxit (calcite), tự hàn kín vết nứt trước khi kết cấu hỏng → khớp tuyệt đối với C.',
            'Với câu hỏi Detail ("According to the text"), đối chiếu thẳng với câu chứa mốc thời gian/tác giả được hỏi ("conducted in 2023") và cảnh giác với từ cực đoan ("exclusively", "lacked altogether").',
            [
                ('Contradicted', 'Bài dùng từ "also practiced" — tức bê tông La Mã vẫn có tro núi lửa, và không dùng cốt thép.'),
                ('Contradicted', 'Bê tông La Mã bền vững suốt 2.000 năm, trái ngược với mức 50 năm của xi măng Portland.'),
                ('Đáp án đúng', 'Diễn đạt lại chính xác cơ chế tự chữa lành vết nứt bằng kết tinh canxit từ các hạt vôi sống tạo ra khi trộn nóng.'),
                ('Out of Scope', 'Đoạn văn không hề nhắc tới việc ngâm trụ cầu trong ao nước ngọt.'),
            ],
        ),

        # Q11–Q12: Information and Ideas — Command of Evidence (Textual)
        q_item(
            'm4_m1_q11', 11, 'Information and Ideas', 'Command of Evidence (Textual)', 'Hard',
            '<p>The extremophile bacterium <i>Deinococcus radiodurans</i> withstands ionizing radiation doses thousands of times higher than those lethal to humans. Early geneticists hypothesized that this resilience stemmed primarily from uniquely rapid DNA-repair enzymes absent in radiation-sensitive bacteria. Biochemist Michael Daly and colleagues proposed an alternative hypothesis: the bacterium’s DNA-repair proteins are chemically ordinary, and its extraordinary survival instead depends on an unusually high intracellular ratio of manganese to iron, which forms small antioxidant complexes that shield those ordinary repair proteins from oxidative destruction during irradiation.</p>',
            'Which finding, if true, would most directly support Daly and colleagues’ hypothesis?',
            [
                'Ionizing radiation induces double-strand breaks in the DNA of <i>Deinococcus radiodurans</i> at nearly the same frequency per unit of radiation as it does in radiation-sensitive bacteria.',
                'When <i>Deinococcus radiodurans</i> cells are grown in a manganese-depleted medium that lowers their intracellular manganese-to-iron ratio, their DNA-repair enzymes suffer severe oxidative damage during irradiation and cell survival plummets.',
                'Purified DNA-repair enzymes extracted from <i>Deinococcus radiodurans</i> mend broken DNA strands ten times faster in manganese-free test tubes than homologous enzymes from other bacteria do.',
                'Several species of desert fungi that tolerate prolonged drought also accumulate elevated concentrations of intracellular iron compared with aquatic fungi.',
            ],
            'B',
            'Giả thuyết của Daly: khả năng sống sót sau phóng xạ phụ thuộc vào tỷ lệ mangan/sắt (Mn:Fe) cao trong tế bào nhằm tạo phức chất chống oxy hóa bảo vệ enzyme sửa chữa DNA bình thường khỏi bị phá hủy do oxy hóa. Nếu giảm mangan khiến tỷ lệ Mn:Fe tụt xuống và hậu quả trực tiếp là enzyme sửa chữa DNA bị tổn thương oxy hóa nặng + tế bào chết hàng loạt (B), giả thuyết nhân-quả của Daly được củng cố trực tiếp nhất!',
            'Để Support một giả thuyết cơ chế (X bảo vệ Y nên gây ra Z), hãy tìm bằng chứng thao tác trực tiếp vào X (làm giảm Mn:Fe) và đo đúng hai mắt xích Y (enzyme bị oxy hóa) và Z (tỷ lệ sống giảm).',
            [
                ('Incomplete Support', 'Chỉ cho thấy DNA bị gãy với tần suất tương tự — chưa kiểm chứng vai trò của tỷ lệ mangan/sắt hay việc bảo vệ enzyme.'),
                ('Đáp án đúng', 'Kiểm chứng trọn vẹn chuỗi nhân-quả của Daly: giảm tỷ lệ Mn:Fe → enzyme sửa chữa DNA bị oxy hóa nặng → tỷ lệ sống sụt giảm mạnh.'),
                ('Supports Rival Hypothesis', 'Ủng hộ giả thuyết cũ của các nhà di truyền học đầu tiên rằng bản thân enzyme sửa DNA vượt trội ngay cả khi không có mangan.'),
                ('Out of Scope', 'Nói về nấm sa mạc chịu hạn và tích lũy sắt — sai đối tượng và sai cơ chế.'),
            ],
        ),
        q_item(
            'm4_m1_q12', 12, 'Information and Ideas', 'Command of Evidence (Textual)', 'Medium',
            '<p>In his 1912 prose-poem collection <i>Gitanjali</i>, Bengali poet Rabindranath Tagore rejects a sharp division between human vitality and the natural world, portraying both as expressions of a single continuous life force.</p>',
            'Which quotation from <i>Gitanjali</i> most effectively illustrates the claim?',
            [
                '“Clouds heap upon clouds and it darkens. Ah, love, why dost thou let me wait outside at the door all alone?”',
                '“Leave this chanting and singing and telling of beads! Whom dost thou worship in this lonely dark corner of a temple with doors all shut?”',
                '“On the seashore of endless worlds children meet. Tempest roams in the pathless sky, ships are wrecked in the trackless water.”',
                '“The same stream of life that runs through my veins night and day runs through the world and dances in rhythmic measures. It is the same life that shoots in joy through the dust of the earth in numberless blades of grass.”',
            ],
            'D',
            'Luận điểm cần minh họa gồm 2 yếu tố: (1) xóa ranh giới giữa sức sống con người và thế giới tự nhiên, (2) xem cả hai là biểu hiện của MỘT dòng sinh mệnh liên tục duy nhất. Trích dẫn D lặp lại trực tiếp cụm "The same stream of life that runs through my veins... runs through the world... It is the same life that shoots... in numberless blades of grass" → khớp 100%!',
            'Trong câu Literary Quotation, khoanh tròn cụm từ khóa lõi trong Claim ("single continuous life force" nối "human vitality" với "natural world") rồi đối chiếu trực tiếp với hình ảnh trong trích dẫn.',
            [
                ('Wrong Theme', 'Diễn tả nỗi cô đơn chờ đợi trong bóng tối của mây mù, không nói về sự hợp nhất một dòng sinh mệnh.'),
                ('Wrong Theme', 'Phê phán sự tách biệt của nghi lễ tôn giáo khép kín trong đền thờ, không đề cập thế giới tự nhiên.'),
                ('Half-Match Trap', 'Có hình ảnh con người (children) và thiên nhiên (seashore, tempest) nhưng không thể hiện chúng chung một dòng sinh lực duy nhất.'),
                ('Đáp án đúng', 'Khẳng định trực tiếp cùng một dòng sự sống chảy trong huyết quản con người cũng chảy khắp thế giới và nảy mầm trong từng ngọn cỏ.'),
            ],
        ),

        # Q13–Q14: Information and Ideas — Command of Evidence (Quantitative)
        q_item(
            'm4_m1_q13', 13, 'Information and Ideas', 'Command of Evidence (Quantitative)', 'Medium',
            q13_chart + '<p>Hospital-acquired <i>Pseudomonas aeruginosa</i> infections frequently form protective biofilms that blunt conventional antibiotics. Microbiologists testing a bacteriophage—a virus that selectively infects bacteria—alongside ciprofloxacin hypothesized that combining the two agents would eliminate a greater percentage of biofilm bacteria than the sum of the reductions achieved by either agent used alone.</p>',
            'Which choice best describes data from the graph that support the microbiologists’ hypothesis?',
            [
                'The combined phage-and-antibiotic treatment reduced biofilm bacteria by 89%, exceeding the 80% combined total of phage alone (52%) and antibiotic alone (28%).',
                'The phage-only treatment reduced biofilm bacteria by 52%, nearly double the 28% reduction observed in the antibiotic-only group.',
                'All three active treatments achieved substantially higher reductions in biofilm bacteria than the 4% reduction recorded in the untreated control.',
                'The combined phage-and-antibiotic treatment eliminated 80% of biofilm bacteria, matching the combined percentage of the two individual treatments.',
            ],
            'A',
            'Giả thuyết cần chứng minh: kết hợp phage + kháng sinh tiêu diệt tỷ lệ vi khuẩn LỚN HƠN TỔNG của hai tác nhân dùng riêng lẻ. Kiểm tra số liệu biểu đồ: Phage Only (52%) + Antibiotic Only (28%) = 80%, trong khi Phage+Antibiotic đạt 89% (> 80%) → đáp án A khớp tuyệt đối cả số liệu lẫn phép so sánh logic!',
            'Khi giả thuyết có cụm "greater than the sum of either agent used alone", phải lập tức cộng hai cột đơn lẻ rồi đối chiếu với cột kết hợp.',
            [
                ('Đáp án đúng', 'Số liệu chính xác 100% (89% vs. 52% + 28% = 80%) và chứng minh trực tiếp giả thuyết cộng hưởng vượt tổng.'),
                ('True Data / Wrong Claim', 'Số liệu đúng biểu đồ (52% vs. 28%) nhưng không nhắc đến nghiệm thức kết hợp (89%).'),
                ('True Data / Wrong Claim', 'Đúng số liệu (control = 4%) nhưng không kiểm chứng được liệu tổ hợp có vượt tổng hai đơn chất hay không.'),
                ('False Data', 'Đọc sai biểu đồ: cột Phage+Antibiotic là 89%, không phải 80%.'),
            ],
        ),
        q_item(
            'm4_m1_q14', 14, 'Information and Ideas', 'Command of Evidence (Quantitative)', 'Hard',
            q14_table + '<p>Urban sociologists debate whether high local voter turnout and volunteerism stem primarily from a city’s economic affluence or from the abundance of accessible “third places”—informal gathering spaces such as public libraries, plazas, and neighborhood cafés. Researcher Linnea Holm claims that third-place density is a stronger predictor of civic engagement than median household income is.</p>',
            'Which choice best describes data from the table that support Holm’s claim?',
            [
                'Aarhus recorded both the highest third-place density at 14.2 per 10,000 residents and the highest voter turnout (78%) and volunteer rate (46%) among the four cities.',
                'Aarhus had both a higher median household income ($64,500) and a higher volunteer rate (46%) than Dresden ($51,900 and 39%), suggesting that affluence tracks volunteerism.',
                'Although Braga had the lowest median household income ($38,200) and Calgary had the highest ($76,800), Braga’s much higher third-place density (13.8 vs. 6.5) coincided with substantially higher voter turnout (74% vs. 54%) and volunteerism (43% vs. 29%).',
                'Calgary had the fewest third places per 10,000 residents (6.5) and the lowest median household income ($76,800) among all four surveyed cities.',
            ],
            'C',
            'Để chứng minh yếu tố A (mật độ third places) dự báo mạnh hơn yếu tố B (thu nhập hộ gia đình), ta phải chọn cặp thành phố mà A và B đi NGƯỢC CHIỀU nhau! So sánh Braga và Calgary: Braga có thu nhập THẤP NHẤT ($38,200) còn Calgary CAO NHẤT ($76,800), nhưng Braga có mật độ third places cao hơn hẳn (13.8 vs. 6.5) và đạt tỷ lệ đi bầu (74% vs. 54%) lẫn tình nguyện (43% vs. 29%) cao hơn nhiều → C tách biến chuẩn xác tuyệt đối!',
            'Khi đề yêu cầu chứng minh biến X dự báo tốt hơn biến Y, luôn tìm cặp đối chứng có X cao + Y thấp nhưng kết quả vẫn cao (tách riêng hai biến khỏi nhau).',
            [
                ('True Data / Wrong Claim', 'Đúng số liệu nhưng không tách được thu nhập khỏi mật độ third places vì Aarhus cũng có thu nhập khá cao ($64,500).'),
                ('Supports Opposite Claim', 'So sánh Aarhus và Dresden lại khiến thu nhập và mức độ gắn kết cộng đồng cùng chiều nhau, làm yếu luận điểm của Holm.'),
                ('Đáp án đúng', 'Tách biến sắc bén qua cặp cực trị Braga (thu nhập thấp nhất, third places cao) vs. Calgary (thu nhập cao nhất, third places thấp), mọi con số khớp bảng 100%.'),
                ('False Data', 'Sai dữ kiện bảng: $76,800 của Calgary là thu nhập CAO NHẤT, không phải thấp nhất.'),
            ],
        ),

        # Q15: Information and Ideas — Inferences
        q_item(
            'm4_m1_q15', 15, 'Information and Ideas', 'Inferences', 'Hard',
            '<p>As artificial-intelligence clusters process ever larger datasets, conventional copper wires connecting adjacent processors lose substantial energy as heat whenever electrical signals travel at high frequencies. Silicon photonics replaces those electrons with pulses of infrared light guided through microscopic waveguides, slashing transmission heat over distances exceeding a few centimeters. However, converting electrical logic signals inside a processor into optical pulses—and converting them back again—imposes a fixed energy penalty at each link’s endpoints. Consequently, computer architects predict that in next-generation supercomputers, optical interconnects will most likely ______</p>',
            'Which choice most logically completes the text?',
            [
                'completely eliminate the use of metallic wiring even across nanometer-scale circuits inside individual processor cores.',
                'replace copper pathways primarily across longer board-to-board and rack-to-rack links where transmission savings outweigh the energy cost of signal conversion.',
                'require higher electrical voltages than copper interconnects do in order to prevent infrared light from heating silicon waveguides.',
                'slow down data transfer rates between distant server racks compared with conventional copper cables.',
            ],
            'B',
            'Tổng hợp hai tiền đề: (1) Quang tử học silicon giảm mạnh hao phí nhiệt khi truyền tín hiệu ở khoảng cách lớn hơn vài centimet; (2) Nhưng việc chuyển đổi điện ↔ quang tại hai đầu dây tốn một mức năng lượng cố định. Hệ quả tất yếu (Consequently): kết nối quang chỉ có lợi nhất ở các đường truyền dài hơn (giữa các bo mạch và tủ máy chủ), nơi lượng nhiệt tiết kiệm trên đường truyền vượt quá chi phí chuyển đổi ở hai đầu → B!',
            'Trong bài Inferences dạng chi phí–lợi ích (fixed cost vs. distance savings), kết luận logic luôn là công nghệ mới thắng thế ở quy mô/khoảng cách đủ lớn để lợi ích vượt chi phí cố định.',
            [
                ('Contradicted / Extreme', 'Ở cấp độ nanomet bên trong lõi chip, quãng đường quá ngắn nên chi phí chuyển đổi điện–quang sẽ làm quang tử học kém hiệu quả hơn dây kim loại.'),
                ('Đáp án đúng', 'Kết nối hoàn hảo ưu điểm giảm nhiệt trên quãng đường dài với ràng buộc chi phí chuyển đổi cố định tại hai đầu.'),
                ('Out of Scope', 'Đoạn văn không nói về điện áp cao hơn hay việc ánh sáng hồng ngoại làm nóng ống dẫn sóng.'),
                ('Out of Scope', 'Không có thông tin nào cho thấy kết nối quang truyền dữ liệu chậm hơn dây đồng.'),
            ],
        ),

        # Q16–Q19: Standard English Conventions — Boundaries
        q_item(
            'm4_m1_q16', 16, 'Standard English Conventions', 'Boundaries', 'Medium',
            '<p>In 1206, Mesopotamian polymath Ismail al-Jazari illustrated a monumental elephant water clock that integrated Indian, Greek, Egyptian, and Chinese design ______ its hidden float-and-pulley mechanism chimed on the half hour and tracked unequal seasonal daylight.</p>',
            STEM_SEC,
            ['motifs,', 'motifs', 'motifs, and while', 'motifs;'],
            'D',
            'Vế trước chỗ trống là 1 Mệnh đề Độc lập (IC: "Ismail al-Jazari illustrated... design motifs"). Vế sau chỗ trống cũng là 1 Mệnh đề Độc lập (IC: "its hidden float-and-pulley mechanism chimed... and tracked..."). Nối IC + IC phải dùng dấu chấm phẩy (`;`), chấm (`.`), hoặc `, + FANBOYS` → chọn D (`motifs;`).',
            'Kiểm tra nhanh hai vế quanh chỗ trống: IC + IC → loại ngay dấu phẩy đơn (Comma Splice) và không dấu (Run-on).',
            [
                ('Comma Splice', 'Nối hai mệnh đề độc lập chỉ bằng một dấu phẩy đơn là lỗi Comma Splice.'),
                ('Run-on Sentence', 'Không có dấu câu hay liên từ giữa hai mệnh đề độc lập gây lỗi câu dính liền (fused sentence).'),
                ('Fragment / Broken Structure', 'Thêm "and while" biến mệnh đề sau thành mệnh đề phụ thuộc bỏ lửng, không có mệnh đề chính đi kèm.'),
                ('Đáp án đúng', 'Dấu chấm phẩy (;) ngăn cách chuẩn xác hai mệnh đề độc lập liên quan chặt chẽ về nghĩa.'),
            ],
        ),
        q_item(
            'm4_m1_q17', 17, 'Standard English Conventions', 'Boundaries', 'Medium',
            '<p>In December 2018, glaciologists drilled through more than one kilometer of Antarctic ice to sample Lake ______ an isolated subglacial water body untouched by sunlight for millennia.</p>',
            STEM_SEC,
            ['Mercer,', 'Mercer;', 'Mercer.', 'Mercer, and'],
            'A',
            'Vế trước là Mệnh đề Độc lập hoàn chỉnh ("glaciologists drilled... to sample Lake Mercer"). Cụm phía sau ("an isolated subglacial water body untouched by sunlight for millennia") là cụm danh từ đồng vị ngữ (appositive phrase) KHÔNG có động từ chính chia thì. Vì vậy chỉ được nối bằng dấu phẩy đơn (A)!',
            'Dấu chấm (.), chấm phẩy (;) và `, and` đều đòi hỏi vế sau phải là Mệnh đề Độc lập (trừ trường hợp liệt kê hoặc vị ngữ chung); thấy cụm danh từ giải thích → dùng dấu phẩy!',
            [
                ('Đáp án đúng', 'Dấu phẩy đơn mở ra cụm đồng vị ngữ giải thích cho "Lake Mercer" một cách mạch lạc.'),
                ('Semicolon Before Fragment', 'Dấu chấm phẩy cấm đứng trước cụm danh từ không có động từ chính.'),
                ('Sentence Fragment', 'Dấu chấm biến cụm "an isolated subglacial water body..." thành mảnh câu thiếu động từ chính.'),
                ('False Compound Clause', '", and" cần một mệnh đề độc lập hoặc một thành phần song song tương đương phía sau, không thể nối thẳng vào cụm đồng vị ngữ bổ nghĩa cho "Lake Mercer".'),
            ],
        ),
        q_item(
            'm4_m1_q18', 18, 'Standard English Conventions', 'Boundaries', 'Hard',
            '<p>Through meticulous cytogenetic staining of variegated maize kernels in the 1940s, geneticist Barbara McClintock demonstrated ______ could physically excise themselves from one chromosomal locus and reinsert into another.</p>',
            STEM_SEC,
            ['that, certain mobile DNA segments', 'that certain mobile DNA segments,', 'that certain mobile DNA segments', ', that certain mobile DNA segments'],
            'C',
            'Động từ "demonstrated" nối trực tiếp vào mệnh đề tân ngữ bắt đầu bằng "that", theo sau là Chủ ngữ "certain mobile DNA segments" + Động từ "could physically excise". Theo quy tắc No-Comma Zone: CẤM đặt dấu phẩy trước "that", sau "that", hoặc giữa Chủ ngữ và Động từ → chọn C (0 dấu phẩy).',
            'Gặp động từ tường thuật/chứng minh + `that` + S + V → không đặt bất kỳ dấu phẩy đơn nào xen vào giữa mạch V – that – S – V!',
            [
                ('No-Comma Zone (that,)', 'Không được đặt dấu phẩy lẻ ngay sau liên từ "that".'),
                ('No-Comma Zone (S, V)', 'Dấu phẩy đơn tách rời chủ ngữ "certain mobile DNA segments" khỏi động từ "could physically excise".'),
                ('Đáp án đúng', 'Không dấu phẩy — giữ liền mạch tuyệt đối cấu trúc V + that + S + V.'),
                ('No-Comma Zone (V, that)', 'Cấm đặt dấu phẩy ngăn cách động từ "demonstrated" và mệnh đề tân ngữ "that...".'),
            ],
        ),
        q_item(
            'm4_m1_q19', 19, 'Standard English Conventions', 'Boundaries', 'Hard',
            '<p>Compiled at the Heian imperial court around the year 1002, Sei Shōnagon’s <i>The Pillow Book</i>—a witty miscellany of seasonal observations, architectural sketches, and satirical lists of annoying ______ remains a landmark of classical Japanese prose.</p>',
            STEM_SEC,
            ['habits,', 'habits—', 'habits;', 'habits'],
            'B',
            'Quan sát dấu mở ngay sau "The Pillow Book": có một dấu gạch ngang em-dash (`—a witty miscellany...`). Theo nguyên tắc Paired Punctuation, cụm đồng vị ngữ mở bằng em-dash (—) BẮT BUỘC phải đóng bằng em-dash (—) ngay trước động từ chính "remains" → chọn B!',
            'Luôn quét ngược lên trước chỗ trống để tìm dấu mở (phẩy hay gạch ngang) của cụm bổ ngữ xen giữa S và V, rồi đóng đúng cặp dấu đó.',
            [
                ('Mismatched Pair (— ... ,)', 'Mở cụm chêm bằng gạch ngang (—) thì cấm đóng bằng dấu phẩy (,).'),
                ('Đáp án đúng', 'Đóng đúng cặp gạch ngang (— ... —) khép lại cụm đồng vị ngữ ngay trước động từ chính "remains".'),
                ('Semicolon Inside Modifier', 'Dấu chấm phẩy không thể đóng cụm bổ ngữ và làm đứt gãy Chủ ngữ với Động từ.'),
                ('Unclosed Modifier', 'Không đóng dấu gạch ngang khiến động từ "remains" bị nuốt vào bên trong cụm liệt kê.'),
            ],
        ),

        # Q20–Q22: Standard English Conventions — Form, Structure, and Sense
        q_item(
            'm4_m1_q20', 20, 'Standard English Conventions', 'Form, Structure, and Sense', 'Medium',
            '<p>A growing archive of nineteenth-century mutual-aid ledgers compiled from boardinghouses, dockworkers’ unions, and neighborhood bakeries ______ how newly arrived immigrants pooled small weekly dues to insure one another against illness.</p>',
            STEM_SEC,
            ['documents', 'document', 'have documented', 'are documenting'],
            'A',
            'Gạch bỏ toàn bộ cụm giới từ và cụm phân từ chen giữa ("of nineteenth-century mutual-aid ledgers compiled from boardinghouses, dockworkers’ unions, and neighborhood bakeries"): Chủ ngữ lõi là danh từ SỐ ÍT "A growing archive" → bắt buộc chọn động từ số ít "documents" (A)!',
            'Mẹo 3–1 cho Subject–Verb Agreement: thấy 3 đáp án số nhiều (document / have documented / are documenting) và chỉ 1 đáp án số ít (documents) → xác nhận ngay chủ ngữ lõi số ít!',
            [
                ('Đáp án đúng', 'Động từ số ít "documents" hòa hợp chính xác với chủ ngữ lõi số ít "A growing archive".'),
                ('Subject-Verb Agreement Trap', 'Bị đánh lừa bởi các danh từ số nhiều đứng gần hơn ("ledgers", "bakeries").'),
                ('Subject-Verb Agreement Trap', '"have documented" là trợ động từ số nhiều, sai với "archive".'),
                ('Subject-Verb Agreement Trap', '"are documenting" là động từ số nhiều, sai với "archive".'),
            ],
        ),
        q_item(
            'm4_m1_q21', 21, 'Standard English Conventions', 'Form, Structure, and Sense', 'Medium',
            '<p>Engineered with microscopic hierarchical hairs modeled directly on the toe pads of tokay geckos, ______ without leaving behind chemical residue.</p>',
            STEM_SEC,
            [
                'engineers can attach the dry adhesive tape to vertical glass panes',
                'vertical glass panes can support the dry adhesive tape',
                'repeated detachment does not degrade the dry adhesive tape’s grip',
                'the dry adhesive tape clings securely to vertical glass panes',
            ],
            'D',
            'Cụm phân từ mở đầu ("Engineered with microscopic hierarchical hairs...") mô tả vật gì được chế tạo với sợi lông vi mô mô phỏng bàn chân tắc kè? Chính là "the dry adhesive tape" (băng dính khô)! Theo quy tắc Dangling Modifier, danh từ đó BẮT BUỘC phải đứng ngay sau dấu phẩy làm chủ ngữ mệnh đề chính → chọn D!',
            'Thấy cụm V-ed / V-ing đứng đầu câu kết thúc bằng dấu phẩy → hỏi ngay "AI/CÁI GÌ thực hiện hoặc chịu hành động đó?" và đặt đúng chủ thể ấy ngay sau dấu phẩy.',
            [
                ('Dangling Modifier', 'Biến "engineers" thành đối tượng "được chế tạo bằng lông vi mô giống chân tắc kè" — vô nghĩa.'),
                ('Dangling Modifier', 'Tấm kính thẳng đứng ("vertical glass panes") không phải vật được thiết kế bằng lông vi mô.'),
                ('Dangling Modifier', 'Hành động tháo rời ("repeated detachment") không thể được chế tạo bằng lông vi mô.'),
                ('Đáp án đúng', 'Đặt đúng chủ thể "the dry adhesive tape" ngay sau dấu phẩy khớp trọn vẹn với cụm bổ ngữ đầu câu.'),
            ],
        ),
        q_item(
            'm4_m1_q22', 22, 'Standard English Conventions', 'Form, Structure, and Sense', 'Hard',
            '<p>Hidden beneath thirteenth-century liturgical prayers on a recycled parchment codex, several previously lost treatises by the Greek mathematician Archimedes ______ to light in 1998 when multispectral imaging distinguished the iron-gall ink of the original text from the medieval overwriting.</p>',
            STEM_SEC,
            ['coming', 'to come', 'came', 'having come'],
            'C',
            'Phân tích khung mệnh đề chính: Chủ ngữ là "several previously lost treatises by the Greek mathematician Archimedes", phía sau là mệnh đề phụ thời gian "when multispectral imaging distinguished...". Mệnh đề chính CHƯA CÓ động từ chia thì (finite verb)! Cả "coming", "to come" và "having come" đều là động từ không chia thì (gây lỗi Fragment). Duy nhất "came" (quá khứ đơn, khớp mốc "in 1998") tạo thành câu hoàn chỉnh!',
            'Trước khi chọn dạng động từ, luôn kiểm tra xem mệnh đề chính đã có Finite Verb hay chưa; nếu chưa có thì loại sạch V-ing, to-V và having + V3.',
            [
                ('Non-Finite Verb (Fragment)', '"coming" là phân từ, khiến mệnh đề chính thiếu động từ chia thì.'),
                ('Non-Finite Verb (Fragment)', '"to come" là động từ nguyên mẫu, không làm vị ngữ chính cho chủ ngữ "treatises".'),
                ('Đáp án đúng', '"came" là động từ chia thì quá khứ đơn duy nhất hoàn chỉnh mệnh đề chính và khớp mốc thời gian "in 1998".'),
                ('Non-Finite Verb (Fragment)', '"having come" là phân từ hoàn thành, vẫn để câu thành mảnh vỡ thiếu động từ chính.'),
            ],
        ),

        # Q23–Q25: Expression of Ideas — Transitions
        q_item(
            'm4_m1_q23', 23, 'Expression of Ideas', 'Transitions', 'Medium',
            '<p>In 1847, Hungarian physician Ignaz Semmelweis noticed that maternity patients examined by doctors arriving directly from autopsy rooms died of puerperal fever at rates far exceeding those cared for by midwives. ______, he mandated that every physician wash his hands in a chlorinated lime solution before entering the maternity ward, causing mortality rates to plunge by nearly ninety percent.</p>',
            STEM_TRANS,
            ['Nevertheless', 'Accordingly', 'By contrast', 'Meanwhile'],
            'B',
            'Câu 1 nêu phát hiện nguyên nhân (bác sĩ đi thẳng từ phòng giải phẫu làm sản phụ tử vong cao hơn hẳn nữ hộ sinh). Câu 2 nêu hành động ứng phó trực tiếp TỪ PHÁT HIỆN ĐÓ (bắt buộc bác sĩ rửa tay bằng dung dịch vôi clo) → Quan hệ Nhân – Quả → "Accordingly" (Theo đó / Do vậy).',
            'Xác định mũi tên logic giữa 2 câu: Phát hiện nguy cơ → Áp dụng biện pháp xử lý phù hợp = Cause–Effect (`Accordingly` / `Therefore`).',
            [
                ('False Contrast', 'Nevertheless chỉ kết quả trái kỳ vọng — việc bắt rửa tay hoàn toàn hợp lý với phát hiện trước đó.'),
                ('Đáp án đúng', 'Accordingly diễn đạt chính xác mối quan hệ nhân – quả giữa quan sát lâm sàng và quy định rửa tay.'),
                ('False Contrast', 'By contrast dùng để đối chiếu hai đối tượng khác biệt nhau.'),
                ('Wrong Relationship (Time)', 'Meanwhile chỉ hai sự việc diễn ra đồng thời, không nêu quan hệ nguyên nhân – hành động.'),
            ],
        ),
        q_item(
            'm4_m1_q24', 24, 'Expression of Ideas', 'Transitions', 'Hard',
            '<p>Volcanic “black smoker” hydrothermal vents along mid-ocean ridges discharge scorching, acidic fluids exceeding 350 degrees Celsius and rely on magma chambers directly beneath the seafloor. The Lost City hydrothermal field on the Mid-Atlantic Ridge, ______, vents cooler, highly alkaline fluids powered not by volcanism but by a chemical reaction between seawater and uplifted mantle rock.</p>',
            STEM_TRANS,
            ['conversely', 'moreover', 'therefore', 'for instance'],
            'A',
            'Đặt từ nối lên đầu câu 2 để đọc logic: Câu 1 mô tả "black smoker" (rất nóng, có tính axit, chạy bằng magma). Câu 2 mô tả "The Lost City" (mát hơn, có tính kiềm cao, không chạy bằng núi lửa mà bằng phản ứng hóa học) → Đối chiếu hai đối tượng NGƯỢC CHIỀU NHAU → "conversely" (ngược lại).',
            'Khi từ nối nằm kẹp giữa hai dấu phẩy ở giữa câu 2, hãy nhấc nó lên đầu câu 2 để nhận diện rõ quan hệ đối lập giữa Chủ thể 1 và Chủ thể 2.',
            [
                ('Đáp án đúng', 'conversely đối chiếu sắc nét hai kiểu miệng phun thủy nhiệt trái ngược nhau (nóng/axit/magma vs. mát/kiềm/phản ứng hóa học).'),
                ('Wrong Relationship (Addition)', 'moreover dùng để bổ sung ý cùng chiều, sai với sự tương phản giữa hai hệ thống miệng phun.'),
                ('Wrong Relationship (Cause-Effect)', 'therefore chỉ hệ quả — Lost City không phải kết quả do black smokers tạo ra.'),
                ('Wrong Relationship (Example)', 'for instance dùng cho ví dụ minh họa — Lost City không phải một ví dụ của black smoker.'),
            ],
        ),
        q_item(
            'm4_m1_q25', 25, 'Expression of Ideas', 'Transitions', 'Hard',
            '<p>When municipal planners in Vienna expanded social housing during the 1920s, they did not restrict eligibility exclusively to the city’s poorest households. ______, they opened subsidized apartments to middle-income artisans, teachers, and clerks as well, fostering socioeconomically mixed complexes that retained broad political support for a century.</p>',
            STEM_TRANS,
            ['Nevertheless', 'Consequently', 'Similarly', 'Instead'],
            'D',
            'Câu 1 có PHỦ ĐỊNH trực tiếp ("did NOT restrict eligibility exclusively to the city’s poorest households"). Câu 2 nêu phương án THAY THẾ mà họ thực sự áp dụng ("opened subsidized apartments to middle-income... as well") → Phủ định X → Làm Y thay thế = "Instead"!',
            'Thấy "did not / never" ở câu 1 đi kèm hành động thay thế cụ thể ở câu 2 → ưu tiên tuyệt đối "Instead" thay vì "Nevertheless".',
            [
                ('Contrast Nuance Trap', 'Nevertheless nghĩa là "dẫu vậy vẫn xảy ra", không diễn đạt sự thay thế trực tiếp sau cấu trúc "did not X".'),
                ('Wrong Relationship (Cause-Effect)', 'Consequently sai vì câu 2 không phải hậu quả tất yếu mà là lựa chọn thay thế trực tiếp cho chính sách bị bác bỏ ở câu 1.'),
                ('Wrong Relationship (Comparison)', 'Similarly dùng để nêu sự tương đồng giữa hai trường hợp riêng biệt.'),
                ('Đáp án đúng', 'Instead khớp chuẩn mẫu câu "did not do X. Instead, they did Y".'),
            ],
        ),

        # Q26–Q27: Expression of Ideas — Rhetorical Synthesis
        q_item(
            'm4_m1_q26', 26, 'Expression of Ideas', 'Rhetorical Synthesis', 'Medium',
            '''<p>While researching a topic, a student has taken the following notes:</p>
            <ul>
              <li>In 1917, French-Canadian microbiologist Félix d’Hérelle isolated an invisible agent that destroyed dysentery bacteria in laboratory cultures.</li>
              <li>He named these bacteria-eating viruses “bacteriophages.”</li>
              <li>In 1919, d’Hérelle successfully used purified bacteriophages to treat patients with severe bacterial dysentery in Paris.</li>
              <li>After penicillin became widely available in the 1940s, Western medicine largely abandoned phage therapy in favor of broad-spectrum antibiotics.</li>
              <li>Rising antibiotic resistance in the twenty-first century has prompted clinical researchers to revive phage therapy for stubborn infections.</li>
            </ul>''',
            'The student wants to explain why interest in bacteriophage therapy declined in Western medicine and why it has recently returned. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
            [
                'In 1917, microbiologist Félix d’Hérelle isolated bacteria-eating viruses called bacteriophages and soon used them to treat dysentery patients in Paris.',
                'Following the widespread availability of penicillin in the 1940s, Western clinicians largely turned away from bacteriophage therapy in favor of broad-spectrum antibiotics.',
                'Although Western medicine largely abandoned bacteriophage therapy after penicillin became widespread in the 1940s, rising antibiotic resistance has prompted modern researchers to revive it for stubborn infections.',
                'Clinical researchers in the twenty-first century are revisiting bacteriophages—viruses first named by Félix d’Hérelle—to treat infections that resist standard drugs.',
            ],
            'C',
            'Goal-First SOP: Mục tiêu có 2 vế bắt buộc: (1) giải thích VÌ SAO liệu pháp phage suy giảm ở y học phương Tây (vì penicillin / kháng sinh phổ rộng thập niên 1940), VÀ (2) VÌ SAO nó quay trở lại gần đây (vì tình trạng kháng kháng sinh gia tăng). Chỉ có C đáp ứng trọn vẹn cả hai vế!',
            'Gạch chân chữ "and" trong câu hỏi Goal: đáp án đúng phải hoàn thành ĐỦ cả 2 yêu cầu chứ không được thiếu 1 nửa.',
            [
                ('Wrong Synthesis Goal', 'Chỉ kể lịch sử phát hiện năm 1917–1919, không giải thích sự suy giảm lẫn sự hồi sinh.'),
                ('Half-Match Trap', 'Chỉ giải thích lý do suy giảm ở thập niên 1940, bỏ sót lý do hồi sinh gần đây.'),
                ('Đáp án đúng', 'Bao trọn cả hai vế của mục tiêu: suy giảm do penicillin thập niên 1940 và được hồi sinh nhờ tình trạng kháng kháng sinh.'),
                ('Half-Match Trap', 'Chỉ nêu lý do hồi sinh hiện đại mà thiếu hẳn nguyên nhân suy giảm trong quá khứ.'),
            ],
        ),
        q_item(
            'm4_m1_q27', 27, 'Expression of Ideas', 'Rhetorical Synthesis', 'Hard',
            '''<p>While researching a topic, a student has taken the following notes:</p>
            <ul>
              <li>Wang Wei (c. 701–761) was a Chinese poet, painter, and statesman of the Tang dynasty.</li>
              <li>He is renowned for twenty-character landscape quatrains known as <i>jueju</i>, particularly those collected in his <i>Wang River Collection</i>.</li>
              <li>Rather than explicitly describing human emotion, Wang Wei’s quatrains use austere natural images—such as moss, empty mountains, and evening light—to evoke quiet stillness.</li>
              <li>Centuries later, Northern Song poet Su Shi remarked that “there is painting in Wang Wei’s poetry, and poetry in his painting.”</li>
            </ul>''',
            'The student wants to introduce Wang Wei’s <i>jueju</i> quatrains to an audience unfamiliar with his work and emphasize how they convey mood. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
            [
                'Rather than naming human emotions outright, the <i>jueju</i> quatrains evoke quiet stillness through austere natural imagery such as moss and evening light.',
                'Tang dynasty poet and painter Wang Wei’s twenty-character <i>jueju</i> landscape quatrains evoke quiet stillness not by stating emotions directly, but through austere natural images such as moss, empty mountains, and evening light.',
                'Centuries after Wang Wei’s death, Northern Song poet Su Shi praised the Tang dynasty artist by observing that there is painting in his poetry and poetry in his painting.',
                'Tang dynasty statesman and artist Wang Wei composed the <i>Wang River Collection</i>, a renowned group of twenty-character landscape quatrains known as <i>jueju</i>.',
            ],
            'B',
            'Mục tiêu KÉP: (1) Giới thiệu thơ tuyệt cú *jueju* của Vương Duy cho độc giả CHƯA BIẾT về ông ("unfamiliar" → phải định danh rõ ông là nhà thơ/họa sĩ đời Đường và *jueju* là thơ tứ tuyệt phong cảnh 20 chữ), VÀ (2) nhấn mạnh CÁCH CHÚNG TRUYỀN TẢI TÂM TRẠNG (không gọi thẳng cảm xúc mà dùng hình ảnh thiên nhiên tối giản như rêu, núi vắng, ánh chiều để gợi tĩnh lặng). Duy nhất B đủ cả hai vế!',
            'Gặp cụm "introduce X to an audience unfamiliar with..." → loại ngay đáp án bỏ qua phần định danh tác giả/thể loại (như A) và loại đáp án thiếu vế thứ hai sau chữ "and" (như D).',
            [
                ('Missing Audience Context', 'Gọi trống không "the jueju quatrains" mà không giới thiệu Vương Duy là ai hay thể thơ này có đặc điểm gì.'),
                ('Đáp án đúng', 'Vừa định danh đầy đủ Vương Duy (nhà thơ, họa sĩ đời Đường) + thơ tứ tuyệt 20 chữ, vừa nêu rõ thủ pháp gợi tĩnh lặng bằng hình ảnh thiên nhiên tối giản.'),
                ('Wrong Synthesis Goal', 'Tập trung vào lời khen của Tô Thức (Su Shi), không nói gì về thể *jueju* hay cách gợi tâm trạng.'),
                ('Half-Match Trap', 'Chỉ giới thiệu Vương Duy và thể thơ *jueju*, bỏ sót hoàn toàn cách bài thơ truyền tải tâm trạng.'),
            ],
        ),
    ]
