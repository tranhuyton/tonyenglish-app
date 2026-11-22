# -*- coding: utf-8 -*-
"""
Digital SAT R&W Adaptive Mock Test #4 — Module 2 Hard Route (27 Questions, Hard & Elite 750+ Tier)
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


def get_m2h_questions():
    q13_chart = svg_bar_chart(
        'Observed Mean Ice Melt Rate (m/yr) Beneath Thwaites Shelf by Surface Geometry',
        ['0', '10', '20', '30', '40'],
        [
            ('Flat Base (Model)', 18, '18 m/yr'),
            ('Flat Base (Obs.)', 4, '4 m/yr'),
            ('Sloped Terrace', 19, '19 m/yr'),
            ('Steep Crevasse', 34, '34 m/yr'),
        ],
        40,
    )

    q14_table = html_table(
        'Physical Properties of Four Experimental Thermal-Insulation Aerogels',
        [
            'Material',
            'Density (mg/cm³)',
            'Thermal Conductivity (mW/m·K)',
            'Compressive Recovery After 80% Strain (%)',
            'Max Stable Temp (°C)',
        ],
        [
            ['Silica Aerogel', '110.0', '16.5', '12%', '650'],
            ['Cellulose Aerogel', '34.5', '28.0', '58%', '240'],
            ['Graphene-Oxide Foam', '12.8', '35.2', '91%', '900'],
            ['Ceramic-Graphene Hybrid', '18.4', '19.8', '96%', '1,150'],
        ],
    )

    return [
        # Q1–Q5: Craft and Structure — Words in Context
        q_item(
            'm4_m2h_q1', 1, 'Craft and Structure', 'Words in Context', 'Hard',
            '<p>For centuries, Greek optical theorists debated whether human vision occurred because eyes emitted invisible rays toward objects. In his eleventh-century <i>Book of Optics</i>, Ibn al-Haytham ______ this emission hypothesis through controlled pinhole-chamber experiments demonstrating that light enters the eye from illuminated surfaces rather than radiating outward from the observer.</p>',
            STEM_WIC,
            ['corroborated', 'extrapolated', 'repudiated', 'sanctioned'],
            'C',
            'Thuyết cũ cho rằng mắt phát tia nhìn ra vật thể ("emitted invisible rays"). Thí nghiệm buồng tối lỗ kim của Ibn al-Haytham chứng minh điều NGƯỢC LẠI ("light enters the eye... rather than radiating outward") → ông đã bác bỏ hoàn toàn giả thuyết phát tia → "repudiated".',
            'Xác định chiều logic của thí nghiệm: "rather than radiating outward" trực tiếp phủ nhận "emission hypothesis" → tìm động từ đồng nghĩa với "disproved / rejected".',
            [
                ('Opposite Meaning', 'corroborated = củng cố/chứng thực — ngược hoàn toàn với kết quả thí nghiệm bác bỏ giả thuyết cũ.'),
                ('Wrong Meaning', 'extrapolated = ngoại suy mở rộng từ dữ liệu — không khớp với hành động phản bác một giả thuyết.'),
                ('Đáp án đúng', 'repudiated = bác bỏ / phủ nhận tính đúng đắn của giả thuyết phát tia nhờ bằng chứng thực nghiệm.'),
                ('Opposite Meaning', 'sanctioned = phê chuẩn/chấp thuận — sai hướng đối lập.'),
            ],
        ),
        q_item(
            'm4_m2h_q2', 2, 'Craft and Structure', 'Words in Context', 'Hard',
            '<p>Traditional phylogenetic diagrams depict microbial evolution as a cleanly branching tree in which genetic traits pass strictly from parent to offspring. Yet pervasive horizontal gene transfer—whereby unrelated bacteria exchange DNA across species boundaries—renders any purely vertical genealogy ______, forcing biologists to model microbial ancestry as an entangled web.</p>',
            STEM_WIC,
            ['untenable', 'unequivocal', 'self-evident', 'inconsequential'],
            'A',
            'Sơ đồ truyền thống coi tiến hóa vi sinh vật như cây phân nhánh theo chiều dọc từ cha mẹ sang con. Tuy nhiên ("Yet"), hiện tượng chuyển gen ngang rộng khắp giữa các loài không họ hàng khiến mọi phả hệ thuần chiều dọc trở nên "không thể đứng vững / không thể bảo vệ được" ("untenable"), buộc các nhà sinh học phải mô hình hóa thành mạng lưới đan xen.',
            'Cấu trúc "renders [old model] ______, forcing scientists to [adopt new model]" luôn đòi hỏi tính từ mang nghĩa "không thể duy trì / vô hiệu" (`untenable`).',
            [
                ('Đáp án đúng', 'untenable = không thể đứng vững/không thể bảo vệ về mặt khoa học, khớp hoàn hảo với việc phải thay thế cây dọc bằng mạng lưới.'),
                ('Opposite Meaning', 'unequivocal = rõ ràng, không chút mơ hồ — sai vì mô hình cũ đang bị bác bỏ.'),
                ('Opposite Meaning', 'self-evident = hiển nhiên đúng — trái ngược hoàn toàn với từ chuyển hướng "Yet".'),
                ('Wrong Meaning', 'inconsequential = không quan trọng/nhỏ nhặt — mô hình cây dọc bị chứng minh là SAI về cấu trúc chứ không chỉ "ít quan trọng".'),
            ],
        ),
        q_item(
            'm4_m2h_q3', 3, 'Craft and Structure', 'Words in Context', 'Elite (750+)',
            '<p>Because freshly fallen Antarctic snow remains porous for centuries before compacting into airtight glacial ice, atmospheric gases continue to diffuse downward through the firn layer long after the snow itself is deposited. Paleoclimatologists must therefore account for this gas-age lag; neglecting it would ______ efforts to synchronize trapped carbon dioxide bubbles with the surrounding ice’s temperature record.</p>',
            STEM_WIC,
            ['facilitate', 'vindicate', 'emulate', 'confound'],
            'D',
            'Tuyết Nam Cực xốp hàng thế kỷ khiến khí quyển tiếp tục khuếch tán xuống lớp tuyết cũ, tạo ra độ lệch tuổi giữa bọt khí CO₂ và lớp băng bao quanh ("gas-age lag"). Nếu bỏ qua độ lệch này ("neglecting it"), nỗ lực đồng bộ hóa niên đại giữa khí CO₂ và dữ liệu nhiệt độ băng sẽ bị làm rối loạn / phá hỏng → "confound"!',
            'Trong ngữ cảnh khoa học SAT Elite, "confound" mang nghĩa chính xác là "làm xáo trộn, làm nhiễu loạn hoặc cản trở nỗ lực phân tích/đối chiếu".',
            [
                ('Opposite Meaning', 'facilitate = tạo thuận lợi — bỏ qua sai số niên đại không thể giúp việc đồng bộ dễ dàng hơn.'),
                ('Opposite Meaning', 'vindicate = minh chứng là đúng — sai hoàn toàn hướng tác hại của việc bỏ sót sai số.'),
                ('Wrong Meaning', 'emulate = noi gương/bắt chước — không đi với tân ngữ "efforts to synchronize".'),
                ('Đáp án đúng', 'confound = làm nhiễu loạn / phá vỡ nỗ lực đồng bộ niên đại giữa bọt khí CO₂ và hồ sơ nhiệt độ của băng.'),
            ],
        ),
        q_item(
            'm4_m2h_q4', 4, 'Craft and Structure', 'Words in Context', 'Elite (750+)',
            '<p>Economist Garrett Hardin famously contended that shared grazing pastures inevitably collapse unless subjected either to private ownership or to centralized state policing. Fieldwork by Elinor Ostrom across Swiss alpine meadows and Japanese communal forests exposed this binary as overly ______, showing that self-governing villagers routinely devised durable local rules that prevented overexploitation for centuries.</p>',
            STEM_WIC,
            ['nuanced', 'reductive', 'conciliatory', 'diffident'],
            'B',
            'Hardin áp đặt một thế lưỡng phân cứng nhắc ("this binary"): chỉ có tư nhân hóa HOẶC nhà nước kiểm soát tập trung. Thực địa của Elinor Ostrom chứng minh còn giải pháp thứ ba bền vững suốt nhiều thế kỷ (cộng đồng tự quản địa phương) → vạch trần thế lưỡng phân đó là quá "giản lược / đơn giản hóa quá mức" → "reductive"!',
            'Khi một học giả chỉ ra thế lưỡng phân "either A or B" bỏ sót thực tế phong phú hơn, từ chuẩn xác nhất trên SAT là "reductive" (giản lược thái quá).',
            [
                ('Opposite Meaning', 'nuanced = tinh tế, nhiều sắc thái — trái ngược hoàn toàn với việc bị vạch trần là giản lược cứng nhắc.'),
                ('Đáp án đúng', 'reductive = giản lược thái quá, thu hẹp hiện tượng phức tạp về chỉ hai cực đơn giản.'),
                ('Wrong Meaning', 'conciliatory = mang tính hòa giải — không liên quan đến lập luận kinh tế của Hardin.'),
                ('Wrong Meaning', 'diffident = rụt rè, thiếu tự tin — không mô tả một thế lưỡng phân lý thuyết.'),
            ],
        ),
        q_item(
            'm4_m2h_q5', 5, 'Craft and Structure', 'Words in Context', 'Elite (750+)',
            '<p>Conventional refractive telescope lenses must be ground into thick curved profiles to bend incoming light smoothly toward a focal point, making large spaceborne optics prohibitively heavy. Flat dielectric metasurfaces—wafers patterned with subwavelength titanium-dioxide nanopillars—achieve comparable focal precision at a fraction of the thickness, effectively ______ the bulk constraints that have long dictated optical engineering.</p>',
            STEM_WIC,
            ['entrenching', 'capitulating to', 'exacerbating', 'circumventing'],
            'D',
            'Thấu kính khúc xạ truyền thống buộc phải dày và nặng. Siêu bề mặt phẳng (metasurfaces) đạt độ chính xác hội tụ tương đương với độ dày chỉ bằng một phần nhỏ → tức là đã "lách qua / vượt qua" được giới hạn cồng kềnh từng chi phối kỹ thuật quang học → "circumventing"!',
            'Dùng mẹo 3–1 sắc thái: A (củng cố), B (đầu hàng trước), C (làm trầm trọng thêm) đều mang nghĩa bị kẹt trong giới hạn cũ; duy nhất D ("circumventing") mang nghĩa vượt qua/hóa giải giới hạn.',
            [
                ('Opposite Meaning', 'entrenching = làm ăn sâu/cố định thêm các giới hạn cồng kềnh.'),
                ('Opposite Meaning', 'capitulating to = đầu hàng trước giới hạn — trái ngược với bước đột phá độ mỏng.'),
                ('Opposite Meaning', 'exacerbating = làm trầm trọng thêm — ngược hoàn toàn kết quả giảm khối lượng.'),
                ('Đáp án đúng', 'circumventing = khéo léo vượt qua / né tránh được ràng buộc về độ dày và khối lượng của quang học truyền thống.'),
            ],
        ),

        # Q6–Q7: Craft and Structure — Text Structure and Purpose
        q_item(
            'm4_m2h_q6', 6, 'Craft and Structure', 'Text Structure and Purpose', 'Hard',
            '<p>Romantic poets such as William Wordsworth often contemplated rural landscapes from an elevated, solitary vantage point, treating scenery as a mirror for personal transcendence. By contrast, nineteenth-century agricultural laborer John Clare wrote from inside the working fens of Northamptonshire, naming sedges, skylarks, and ditches in regional dialect. <u>When parliamentary enclosure fenced off the open commons of his childhood, Clare’s verse did not merely lament lost beauty; it cataloged how privatization severed a reciprocal ecological and communal memory.</u> Literary historians consequently regard Clare as a precursor to modern environmental writing rather than a minor imitator of Romantic pastoralism.</p>',
            'Which choice best describes the function of the underlined sentence in the text as a whole?',
            [
                'It illustrates how Clare’s response to landscape transformation went beyond aesthetic nostalgia by linking environmental disruption to the unraveling of communal memory.',
                'It argues that William Wordsworth personally supported parliamentary enclosure laws across Northamptonshire.',
                'It details the parliamentary procedures through which nineteenth-century open commons were legally converted into private estates.',
                'It suggests that John Clare abandoned regional dialect in his poetry after the open commons were fenced off.',
            ],
            'A',
            'Đoạn văn đối chiếu Wordsworth (chiêm ngưỡng phong cảnh thuần túy từ xa) với John Clare (viết từ bên trong vùng đầm lầy lao động). Câu gạch chân minh họa sự khác biệt đó qua phản ứng của Clare trước đạo luật rào đất: thơ ông không chỉ tiếc nuối vẻ đẹp thuần túy mà ghi chép cách tư nhân hóa cắt đứt ký ức sinh thái – cộng đồng, làm tiền đề cho câu kết (coi ông là tiền thân văn học môi trường hiện đại).',
            'Chú ý cấu trúc "not merely X; it cataloged Y" trong câu gạch chân — đáp án chuẩn luôn phản ánh chính xác phép nâng tầng từ thẩm mỹ thuần túy (X) lên chiều sâu sinh thái – cộng đồng (Y).',
            [
                ('Đáp án đúng', 'Nắm trọn vai trò minh họa bước vượt khỏi nỗi hoài niệm thẩm mỹ đơn thuần để gắn biến đổi môi trường với sự đứt gãy ký ức cộng đồng.'),
                ('Out of Scope', 'Đoạn văn hoàn toàn không nói Wordsworth ủng hộ đạo luật rào đất.'),
                ('Out of Scope', 'Câu gạch chân không mô tả trình tự thủ tục pháp lý của Nghị viện Anh.'),
                ('Contradicted / Out of Scope', 'Không có chi tiết nào nói Clare từ bỏ phương ngữ vùng miền sau khi đất chung bị rào.'),
            ],
        ),
        q_item(
            'm4_m2h_q7', 7, 'Craft and Structure', 'Text Structure and Purpose', 'Elite (750+)',
            '<p>Female honeybee larvae that inherit virtually identical genomes can nonetheless develop into either sterile worker bees or fertile, long-lived queens depending solely on whether nurse bees feed them royal jelly. For years, entomologists struggled to pinpoint how diet alone triggers such sweeping anatomical divergence. In 2008, geneticist Ryszard Maleszka and colleagues silenced a single enzyme, Dnmt3, that attaches methyl tags to larval DNA; although the treated larvae received an ordinary worker diet, more than seventy percent developed functional queen ovaries. The experiment revealed that royal jelly acts largely by dialing down enzymatic DNA methylation, thereby keeping queen-associated developmental genes transcriptionally active.</p>',
            'Which choice best states the main purpose of the text?',
            [
                'To challenge the long-standing assumption that queen honeybees and worker honeybees share virtually identical genomes.',
                'To compare the chemical composition of royal jelly produced by different subspecies of honeybees.',
                'To describe an experiment that uncovered the epigenetic mechanism through which larval diet directs caste development in honeybees.',
                'To advocate silencing the Dnmt3 enzyme in commercial apiaries to increase colony honey yields.',
            ],
            'C',
            'Cả đoạn văn đi theo mạch: (1) Nêu câu hỏi sinh học chưa có lời giải (cùng bộ gen, vì sao chỉ khác chế độ ăn sữa ong chúa lại sinh ra ong thợ vs. ong chúa?); (2) Trình bày thí nghiệm năm 2008 của nhóm Maleszka (tắt enzyme methyl hóa DNA Dnmt3); (3) Kết luận cơ chế biểu sinh (epigenetic mechanism: giảm methyl hóa DNA để giữ gen phát triển ong chúa hoạt động) → khớp chính xác mục đích ở C!',
            'Trong câu Main Purpose của bài nghiên cứu khoa học, luôn kiểm tra động từ mở đầu đáp án (describe an experiment vs. challenge / compare / advocate) xem có khớp đúng thái độ trung lập giải thích cơ chế của tác giả không.',
            [
                ('Contradicted', 'Đoạn văn khẳng định chúng có bộ gen gần như giống hệt nhau, không hề thách thức giả định này.'),
                ('Out of Scope', 'Bài không so sánh thành phần hóa học sữa ong chúa giữa các phân loài ong.'),
                ('Đáp án đúng', 'Tóm gọn chính xác mục đích trung tâm: trình bày thí nghiệm làm sáng tỏ cơ chế biểu sinh (DNA methylation) nối chế độ ăn ấu trùng với sự phân hóa đẳng cấp ong.'),
                ('Out of Scope', 'Bài mang tính giải thích cơ chế sinh học cơ bản, không cổ vũ ứng dụng thương mại để tăng sản lượng mật.'),
            ],
        ),

        # Q8: Craft and Structure — Cross-Text Connections
        q_item(
            'm4_m2h_q8', 8, 'Craft and Structure', 'Cross-Text Connections', 'Elite (750+)',
            '<p><b>Text 1</b><br/>Historian Dimitri Gutas argues that the eighth- to tenth-century Greco-Arabic translation movement in Baghdad was neither a passive preservation of Greek manuscripts nor an idiosyncratic hobby of a few caliphs. Rather, Gutas demonstrates that Abbasid rulers, courtiers, and wealthy physicians systematically funded competing translations of Aristotle, Euclid, and Galen to build an imperial scientific ideology capable of rivaling neighboring Sasanian and Byzantine courts.</p>'
            '<p><b>Text 2</b><br/>Science historian George Saliba agrees that Abbasid translation efforts were deeply intentional, yet he cautions against framing Baghdad’s scholars chiefly as translators executing political ideology. Examining eleventh-century critiques of Ptolemaic astronomy by figures such as Ibn al-Haytham and later Maragha astronomers, Saliba contends that Arabic thinkers engaged Greek texts critically from the outset, routinely flagging mathematical contradictions and devising original planetary models to supersede them.</p>',
            'Based on the texts, how would George Saliba (Text 2) most likely respond to Dimitri Gutas’s account (Text 1)?',
            [
                'By denying that Abbasid rulers and courtiers systematically financed translations of Greek scientific works.',
                'By agreeing that the translation movement was deliberate rather than accidental, while emphasizing that Islamic-era scholars actively critiqued and innovated beyond Greek sources rather than primarily serving imperial ideology.',
                'By asserting that Baghdad’s scholars concentrated solely on Ptolemaic astronomy and neglected philosophical or medical treatises by Aristotle and Galen.',
                'By contending that Arabic scholars passively archived Greek manuscripts without revising them until European astronomers challenged Ptolemy.',
            ],
            'B',
            'Phân tích hai lớp lập trường của Saliba (Text 2) đối với Gutas (Text 1): (1) Đồng thuận ("agrees that Abbasid translation efforts were deeply intentional") — tức đồng ý phong trào dịch thuật có chủ đích chứ không ngẫu nhiên; (2) Phản biện/bổ sung ("yet he cautions against framing Baghdad’s scholars chiefly as translators executing political ideology") — nhấn mạnh học giả Hồi giáo đã chủ động phản biện các mâu thuẫn toán học và sáng tạo mô hình hành tinh mới vượt lên nguồn Hy Lạp → đáp án B bao trọn cả hai lớp!',
            'Trong Cross-Text Elite 750+, hầu hết quan hệ giữa hai học giả là "Đồng ý một phần + Chỉnh hướng trọng tâm" (Qualified Agreement); luôn kiểm tra xem đáp án có giữ nguyên điểm đồng thuận hay vô tình bóp méo thành phản đối 100%.',
            [
                ('Contradicted', 'Saliba đồng ý nỗ lực dịch thuật mang tính chủ đích sâu sắc, không phủ nhận sự bảo trợ tài chính của triều Abbasid.'),
                ('Đáp án đúng', 'Phản ánh sắc nét cả sự đồng thuận về tính chủ đích lẫn phản biện rằng các học giả chủ động phê phán và sáng tạo chứ không chỉ thực thi ý thức hệ đế quốc.'),
                ('Extreme / Out of Scope', 'Saliba lấy thiên văn học làm bằng chứng, hoàn toàn không nói học giả Baghdad bỏ qua Aristotle hay Galen.'),
                ('Contradicted', 'Ngược hoàn toàn cả hai văn bản: cả Gutas và Saliba đều bác bỏ quan điểm "bảo quản thụ động".'),
            ],
        ),

        # Q9–Q10: Information and Ideas — Central Ideas and Details
        q_item(
            'm4_m2h_q9', 9, 'Information and Ideas', 'Central Ideas and Details', 'Hard',
            '<p>Marine ecologists long assumed that virtually all dissolved oxygen in the abyssal ocean originates from photosynthetic organisms at the sunlit surface and is carried downward by deep-water currents. However, during benthic chamber deployments four kilometers beneath the Pacific Ocean in the Clarion-Clipperton Zone, oceanographer Andrew Sweetman’s team recorded net oxygen levels rising inside sealed seafloor enclosures containing potato-sized polymetallic nodules—even after all microbial respiration was halted. Measuring electrical potentials up to 0.95 volts across nodule surfaces, the researchers proposed that clustered nodules behave like natural geobatteries capable of splitting seawater molecules through electrolysis in total darkness.</p>',
            'Which choice best states the main idea of the text?',
            [
                'Deep-sea microbes inhabiting the Clarion-Clipperton Zone produce dissolved oxygen through a previously unknown form of non-solar photosynthesis.',
                'Oceanic currents are incapable of transporting surface-generated oxygen to Pacific seafloors deeper than four kilometers.',
                'Commercial harvesting of polymetallic nodules has measurably lowered benthic oxygen levels across the abyssal Pacific.',
                'Seafloor observations from the abyssal Pacific challenge the assumption that deep-ocean oxygen derives exclusively from surface photosynthesis, suggesting that polymetallic nodules may generate oxygen electrochemically in complete darkness.',
            ],
            'D',
            'Đoạn văn đối lập giả định cũ ("long assumed that virtually all dissolved oxygen... originates from photosynthetic organisms at the sunlit surface") với phát hiện thực địa ở độ sâu 4 km: oxy vẫn tăng trong buồng kín chứa các kết hạch đa kim (ngay cả khi đã chặn hô hấp vi sinh), dẫn đến giả thuyết chúng hoạt động như pin địa chất tự nhiên điện phân nước biển trong bóng tối hoàn toàn → D tóm gọn trọn vẹn nhất.',
            'Khi đoạn văn mở đầu bằng "long assumed... However...", Main Idea chuẩn luôn chứa cấu trúc "challenge the assumption that X, suggesting instead that Y".',
            [
                ('Contradicted', 'Oxy vẫn tăng ngay cả khi đã ngừng toàn bộ hoạt động vi sinh vật — không phải do vi sinh vật quang hợp.'),
                ('Extreme / Contradicted', 'Bài không hề khẳng định dòng hải lưu mất khả năng vận chuyển oxy từ tầng mặt xuống sâu 4 km.'),
                ('Out of Scope', 'Đoạn văn không đề cập đến hoạt động khai thác thương mại kết hạch đa kim.'),
                ('Đáp án đúng', 'Bao trọn cả hai vế trung tâm: thách thức giả định nguồn gốc oxy duy nhất từ tầng mặt và nêu cơ chế điện phân nước biển của kết hạch đa kim trong bóng tối.'),
            ],
        ),
        q_item(
            'm4_m2h_q10', 10, 'Information and Ideas', 'Central Ideas and Details', 'Elite (750+)',
            '<p>Classical demographic transition theory predicted that once industrializing societies achieved low infant mortality and widespread secondary schooling, birth rates would stabilize near the replacement threshold of 2.1 children per woman. In several high-income East Asian and Southern European nations, however, total fertility has fallen well below 1.3 and persisted there for decades. Demographer Frances Goldscheider notes that these sharp declines occur most acutely during an incomplete phase of the “gender revolution”: women have entered demanding full-time labor markets at rates comparable to men’s, yet institutional childcare remains scarce and domestic caregiving remains overwhelmingly concentrated on mothers. Only in societies where men’s participation in unpaid household labor rises substantially, Goldscheider observes, do fertility rates partially rebound toward replacement.</p>',
            'According to the text, what best explains why fertility rates have remained far below replacement in certain high-income nations?',
            [
                'An uneven social transition in which women’s widespread entry into full-time paid employment has not yet been accompanied by adequate public childcare or a more equitable sharing of domestic caregiving.',
                'A resurgence of infant mortality in East Asian and Southern European cities that has discouraged families from raising multiple children.',
                'Declining enrollment of women in secondary education, which has prevented households from reaching the income needed for childbearing.',
                'An irreversible cultural preference for childlessness that persists even in societies where men take on a substantial share of household labor.',
            ],
            'A',
            'Đoạn văn nêu nguyên nhân trực tiếp qua phân tích của Goldscheider ("an incomplete phase of the ‘gender revolution’"): phụ nữ tham gia thị trường lao động toàn thời gian ngang nam giới, NHƯNG dịch vụ trông trẻ công còn khan hiếm và gánh nặng chăm sóc gia đình vẫn dồn chủ yếu lên người mẹ → đáp án A diễn đạt lại chính xác 100%!',
            'Trong bài xã hội học Elite, chú ý định nghĩa sau dấu hai chấm (:) của thuật ngữ trong ngoặc kép ("incomplete phase of the ‘gender revolution’") — đó chính là câu trả lời cốt lõi.',
            [
                ('Đáp án đúng', 'Khớp từng yếu tố trong lập luận của Goldscheider: bước chuyển bất đối xứng giữa lao động toàn thời gian của phụ nữ và sự thiếu hụt trông trẻ / chia sẻ việc nhà.'),
                ('Out of Scope / Contradicted', 'Các nước thu nhập cao này đã đạt tỷ lệ tử vong sơ sinh thấp; bài không hề nói tỷ lệ này tăng trở lại.'),
                ('Contradicted / Out of Scope', 'Phổ cập giáo dục trung học đã đạt được, không hề giảm.'),
                ('Contradicted', 'Câu cuối khẳng định rõ tỷ lệ sinh CÓ PHỤC HỒI MỘT PHẦN ở những xã hội nơi nam giới chia sẻ mạnh mẽ việc nhà không lương.'),
            ],
        ),

        # Q11–Q12: Information and Ideas — Command of Evidence (Textual)
        q_item(
            'm4_m2h_q11', 11, 'Information and Ideas', 'Command of Evidence (Textual)', 'Elite (750+)',
            '<p>Self-healing polymers capable of automatically rejoining after cuts typically rely on weak, reversible hydrogen bonds that break and reform rapidly at room temperature. Because those weak bonds also yield easily under tension, materials engineers long assumed an unavoidable trade-off: making a supramolecular elastomer stiff enough to bear heavy structural loads would suppress polymer-chain mobility and thereby prevent autonomous room-temperature healing. Recently, polymer chemist Yu Yanagisawa’s team synthesized a thiourea-based polyether glass that exhibits the rigidity of hard acrylic yet heals completely when pressed together by hand for thirty seconds. The team attributed this paradox to zigzagging arrays of thiourea hydrogen bonds that prevent the polymer chains from crystallizing into rigid, immobile lattices while still interlocking tightly enough to resist bending.</p>',
            'Which finding, if true, would most directly weaken Yanagisawa and colleagues’ explanation for the thiourea polymer’s combination of stiffness and room-temperature self-healing?',
            [
                'Raising the ambient temperature above 50 degrees Celsius reduces the pressure time needed for severed pieces of the thiourea polymer to rejoin.',
                'Conventional acrylic glass lacks thiourea hydrogen bonds and cannot seal surface fractures unless heated above 160 degrees Celsius.',
                'X-ray diffraction demonstrates that a modified variant of the thiourea polymer whose hydrogen bonds align in straight rows—forming dense crystalline lattices—achieves the same stiffness and thirty-second room-temperature healing as the original zigzagging polymer.',
                'When immersed in concentrated hydrochloric acid for seventy-two hours, the thiourea polymer loses roughly one-third of its tensile rigidity.',
            ],
            'C',
            'Bóc tách đúng giải thích (explanation) cần làm yếu: nhóm Yanagisawa cho rằng chìa khóa của nghịch lý (vừa cứng vừa tự lành ở nhiệt độ phòng) là CÁC DÃY LIÊN KẾT HYDRO HÌNH ZIGZAG NGĂN KHÔNG CHO CHUỖI POLYME KẾT TINH THÀNH MẠNG LƯỚI BẤT ĐỘNG. Nếu một biến thể có liên kết xếp thẳng hàng VÀ TẠO THÀNH MẠNG TINH THỂ DÀY ĐẶC nhưng vẫn đạt độ cứng và tốc độ tự lành 30 giây y hệt (C), thì lý giải "tránh kết tinh nhờ cấu trúc zigzag" bị đánh sập trực tiếp!',
            'Để Weaken một lời giải thích cơ chế ("attributed Y to mechanism X"), tìm bằng chứng loại bỏ hẳn X (cho kết tinh mạng thẳng hàng thay vì zigzag phi kết tinh) mà hiệu ứng Y (cứng + tự lành 30 giây) VẪN xảy ra nguyên vẹn!',
            [
                ('Consistent / Irrelevant', 'Nhiệt độ cao hơn giúp liên kết tái tạo nhanh hơn là hệ quả động học bình thường, không phủ nhận vai trò cấu trúc zigzag.'),
                ('Consistent Background', 'So sánh với kính acrylic thường không hề làm yếu lời giải thích về cấu trúc của polymer thiourea.'),
                ('Đáp án đúng', 'Đánh thẳng vào mắt xích nhân-quả cốt lõi: loại bỏ điều kiện "zigzag ngăn kết tinh" mà vẫn giữ nguyên 100% độ cứng và tốc độ tự lành ở nhiệt độ phòng.'),
                ('Out of Scope', 'Độ bền hóa học trong axit mạnh không liên quan đến cơ chế vừa cứng vừa tự lành ở nhiệt độ phòng.'),
            ],
        ),
        q_item(
            'm4_m2h_q12', 12, 'Information and Ideas', 'Command of Evidence (Textual)', 'Hard',
            '<p>In her nineteenth-century nature lyric “A Bird, came down the Walk,” poet Emily Dickinson observes a wild bird at close range. A literary critic argues that when the bird finally takes flight from the speaker, Dickinson renders its airborne movement using serene aquatic metaphors that make the sky resemble weightless water.</p>',
            'Which quotation from “A Bird, came down the Walk” most effectively illustrates the critic’s claim?',
            [
                '“And he unrolled his feathers, / And rowed him softer Home— / Than Oars divide the Ocean, / Too silver for a seam,”',
                '“A Bird, came down the Walk— / He did not know I saw— / He bit an Angle Worm in halves / And ate the fellow, raw,”',
                '“And then, he drank a Dew / From a convenient Grass— / And then hopped sidewise to the Wall / To let a Beetle pass—”',
                '“He glanced with rapid eyes, / That hurried all abroad— / They looked like frightened Beads, I thought, / He stirred his Velvet Head.”',
            ],
            'A',
            'Luận điểm của nhà phê bình gồm 2 thành phần bắt buộc: (1) lúc con chim cất cánh bay ("takes flight / airborne movement"), VÀ (2) ẩn dụ mặt nước êm dịu ("serene aquatic metaphors"). Trích dẫn A hội tụ cả hai: xòe lông bay ("unrolled his feathers") được ví như chèo nhẹ mái chèo rẽ sóng đại dương ("rowed him softer Home— / Than Oars divide the Ocean") → khớp 100%!',
            'Cảnh giác bẫy liên tưởng từ vựng ở C ("drank a Dew" có chất lỏng/giọt sương nhưng con chim đang đứng uống trên cỏ và nhảy né bọ cánh cứng, hoàn toàn không phải ẩn dụ nước cho chuyển động bay!).',
            [
                ('Đáp án đúng', 'Chứa trực tiếp cả hành động cất cánh ("unrolled his feathers") lẫn ẩn dụ chèo thuyền rẽ nước đại dương ("rowed... Than Oars divide the Ocean").'),
                ('Wrong Focus', 'Mô tả cảnh săn giun đất trần trụi trên mặt đất, không liên quan đến bay hay ẩn dụ nước.'),
                ('Word-Association Trap', 'Có chữ "Dew" (sương), dễ gây nhầm với nước, nhưng miêu tả chim uống nước và nhảy sang tường chứ không phải bay lượn trên không.'),
                ('Wrong Focus', 'Miêu tả ánh mắt cảnh giác đầy lo âu ("frightened Beads"), không nhắc tới cất cánh hay hình ảnh nước.'),
            ],
        ),

        # Q13–Q14: Information and Ideas — Command of Evidence (Quantitative)
        q_item(
            'm4_m2h_q13', 13, 'Information and Ideas', 'Command of Evidence (Quantitative)', 'Hard',
            q13_chart + '<p>Before the underwater robot <i>Icefin</i> surveyed the underside of West Antarctica’s Thwaites Glacier, standard ocean-circulation models projected uniform rapid melting across the glacier’s flat horizontal base. Based on <i>Icefin</i>’s sensor logs, glaciologists now contend that a thin layer of cold freshwater insulates flat basal ice—causing observed melting there to fall far below model projections—while warm currents concentrate accelerated erosion along steeply angled fractures.</p>',
            'Which choice best describes data from the graph that support the glaciologists’ contention?',
            [
                'Observed melting along sloped terraces averaged 19 meters per year, nearly matching the 18 meters per year predicted by standard models for the flat base.',
                'Observed melting across the flat base averaged only 4 meters per year—less than a quarter of the 18 meters per year projected by models—whereas melting inside steep crevasses reached 34 meters per year.',
                'Observed melting on the flat base (18 meters per year) was more than four times higher than the modeled rate (4 meters per year), though still lower than in steep crevasses.',
                'Steep crevasses melted at 34 meters per year, which was 15 meters per year faster than the melt rate recorded along sloped terraces (19 meters per year).',
            ],
            'B',
            'Nhận định của các nhà băng học gồm HAI VẾ bắt buộc: (1) tốc độ tan thực tế ở đáy phẳng THẤP HƠN NHIỀU so với dự báo mô hình (Flat Base Obs. = 4 m/yr < 1/4 của Flat Base Model = 18 m/yr, vì 18/4 = 4,5); VÀ (2) sự bào mòn tăng tốc mạnh tập trung ở các khe nứt dốc đứng (Steep Crevasse = 34 m/yr). Chỉ đáp án B vừa khớp số liệu 100% vừa chứng minh ĐỦ cả hai vế!',
            'Với luận điểm hai vế ("causing X... while Y..."), loại ngay các đáp án True Data nhưng chỉ chứng minh 1 nửa (như A, D) và kiểm tra kỹ kẻo bị đảo nhãn cột (như C).',
            [
                ('True Data / Wrong Claim', 'Số liệu đúng (19 vs. 18 m/yr) nhưng không đối chiếu đáy phẳng thực tế với mô hình, cũng không nêu tốc độ tan cực nhanh ở khe nứt dốc.'),
                ('Đáp án đúng', 'Khớp số liệu chính xác 100% (4 < 4.5 = 1/4 của 18; khe dốc 34 m/yr) và chứng minh trọn vẹn cả hai vế lập luận.'),
                ('False Data (Swapped Labels)', 'Đảo ngược hoàn toàn giá trị thực tế (4 m/yr) và giá trị mô hình (18 m/yr).'),
                ('True Data / Half-Match Trap', 'Chỉ so sánh khe dốc (34) với bậc nghiêng (19), bỏ qua hoàn toàn vế đáy phẳng thực tế thấp hơn dự báo mô hình.'),
            ],
        ),
        q_item(
            'm4_m2h_q14', 14, 'Information and Ideas', 'Command of Evidence (Quantitative)', 'Elite (750+)',
            q14_table + '<p>Aerospace engineers designing reusable thermal shields for polar atmospheric probes seek an insulation material that simultaneously meets three criteria: ultralight density (under 25 mg/cm³), low thermal conductivity (below 22 mW/m·K), and high elasticity (at least 90% recovery after 80% compression). Conventional wisdom holds that pure silica aerogels remain the best overall candidates for such reusable shields because they offer the lowest thermal conductivity.</p>',
            'Which choice best uses data from the table to challenge conventional wisdom and identify the sole material meeting all three engineering criteria?',
            [
                'Silica aerogel achieves the lowest thermal conductivity (16.5 mW/m·K) while maintaining 96% compressive recovery and a density of 18.4 mg/cm³.',
                'Graphene-oxide foam has the lowest density of all four materials at 12.8 mg/cm³ and recovers 91% of its shape after compression, making it the only candidate suitable for reusable shields.',
                'Cellulose aerogel offers lower thermal conductivity (28.0 mW/m·K) than graphene-oxide foam (35.2 mW/m·K) and far lower density (34.5 mg/cm³) than silica aerogel (110.0 mg/cm³).',
                'Although silica aerogel has the lowest thermal conductivity (16.5 mW/m·K), its high density (110.0 mg/cm³) and poor 12% compressive recovery disqualify it, leaving only the ceramic-graphene hybrid—at 18.4 mg/cm³, 19.8 mW/m·K, and 96% recovery—to satisfy every requirement.',
            ],
            'D',
            'Kiểm tra từng dòng bảng theo 3 ngưỡng kỹ thuật (< 25 mg/cm³ | < 22 mW/m·K | ≥ 90%): (1) Silica: 110.0 (LOẠI), 16.5 (đạt), 12% (LOẠI); (2) Cellulose: 34.5 (LOẠI), 28.0 (LOẠI), 58% (LOẠI); (3) Graphene-Oxide Foam: 12.8 (đạt), 35.2 (LOẠI — vượt ngưỡng 22!), 91% (đạt); (4) Ceramic-Graphene Hybrid: 18.4 (<25 ĐẠT), 19.8 (<22 ĐẠT), 96% (≥90% ĐẠT). Do đó D vừa bác bỏ Silica vừa chỉ đích danh Ceramic-Graphene Hybrid với đầy đủ 3 chỉ số chính xác!',
            'Trong bài bảng đa tiêu chí Elite, lập tức đánh dấu ✓ / ✗ vào từng ô theo từng ngưỡng số trước khi đọc 4 lựa chọn để không rơi vào bẫy bỏ sót 1 tiêu chí như B.',
            [
                ('False Data (Row Mixing)', 'Trộn số liệu của Ceramic-Graphene Hybrid (96%, 18.4 mg/cm³) gán nhầm cho Silica Aerogel.'),
                ('Fails Criterion Trap', 'Bỏ qua cột độ dẫn nhiệt: Graphene-oxide foam có độ dẫn nhiệt 35.2 mW/m·K, vượt xa ngưỡng tối đa 22 mW/m·K.'),
                ('True Data / Fails All Criteria', 'Số liệu đúng nhưng Cellulose trượt cả 3 tiêu chí (34.5 > 25; 28.0 > 22; 58% < 90%).'),
                ('Đáp án đúng', 'Bác bỏ đúng Silica (quá nặng 110.0 và giòn 12%) và chứng minh Ceramic-Graphene Hybrid là vật liệu duy nhất vượt qua cả 3 ngưỡng (18.4; 19.8; 96%).'),
            ],
        ),

        # Q15: Information and Ideas — Inferences
        q_item(
            'm4_m2h_q15', 15, 'Information and Ideas', 'Inferences', 'Elite (750+)',
            '<p>Analyzing skeletal DNA from fourteenth-century London cemeteries, evolutionary geneticists found that individuals carrying two copies of a specific variant of the immune-regulating gene <i>ERAP2</i> were roughly forty percent more likely to survive the Black Death than those lacking it. Yet when the researchers examined modern European genomes, the protective <i>ERAP2</i> variant had not swept to universal fixation; instead, it persists at intermediate frequencies alongside its non-protective counterpart, even though it still enhances macrophage clearance of <i>Yersinia pestis</i> in laboratory assays. Because the same hyper-responsive <i>ERAP2</i> variant is strongly linked in contemporary clinical cohorts to chronic inflammatory disorders such as Crohn’s disease, evolutionary biologists infer that ______</p>',
            'Which choice most logically completes the text?',
            [
                'the protective <i>ERAP2</i> variant must have lost its biochemical ability to combat <i>Yersinia pestis</i> shortly after the fourteenth century.',
                'chronic inflammatory disorders such as Crohn’s disease were the primary cause of death in fourteenth-century London rather than bubonic plague.',
                'once recurrent plague epidemics subsided, the fitness cost of increased susceptibility to autoimmune inflammation counterbalanced the variant’s historical survival advantage and prevented it from replacing the alternative allele entirely.',
                'modern Europeans who lack the protective <i>ERAP2</i> variant are completely immune to chronic inflammatory bowel conditions.',
            ],
            'C',
            'Xâu chuỗi logic chọn lọc cân bằng (balancing selection): (1) Biến thể ERAP2 bảo vệ mạnh trước dịch hạch thế kỷ 14; (2) Nhưng ngày nay nó KHÔNG thay thế hoàn toàn alen còn lại dù vẫn diệt vi khuẩn dịch hạch tốt trong phòng thí nghiệm; (3) Manh mối cuối ("Because..."): chính biến thể phản ứng quá mức này làm tăng nguy cơ bệnh viêm tự miễn mạn tính (Crohn). Kết luận tất yếu: khi các đợt dịch hạch tái diễn rút đi, cái giá tiến hóa của bệnh viêm tự miễn đã cân bằng lại lợi thế sống sót lịch sử đó, ngăn không cho biến thể này cố định 100% trong quần thể → C!',
            'Trong bài Inferences Elite có cấu trúc "X has benefit A, yet X did not reach 100%; Because X also carries cost B, scientists infer that...", đáp án đúng luôn là sự cân bằng/triệt tiêu (counterbalance) giữa chi phí B và lợi ích A.',
            [
                ('Contradicted', 'Văn bản khẳng định biến thể này VẪN tăng cường khả năng tiêu diệt Yersinia pestis của đại thực bào trong phòng thí nghiệm.'),
                ('Out of Scope / Contradicted', 'Không hề nói bệnh Crohn là nguyên nhân tử vong hàng đầu ở London thế kỷ 14.'),
                ('Đáp án đúng', 'Giải mã chính xác cơ chế chọn lọc cân bằng: khi dịch hạch lắng xuống, bất lợi viêm tự miễn đã đối trọng với lợi thế cũ, giữ biến thể ở tần suất trung gian.'),
                ('Extreme / Unsupported', 'Liên kết với nguy cơ cao hơn không đồng nghĩa người không mang biến thể sẽ "miễn nhiễm hoàn toàn" với bệnh viêm ruột.'),
            ],
        ),

        # Q16–Q19: Standard English Conventions — Boundaries
        q_item(
            'm4_m2h_q16', 16, 'Standard English Conventions', 'Boundaries', 'Hard',
            '<p>Buried beneath twenty meters of volcanic mud in 79 CE, the carbonized papyrus scrolls of Herculaneum resisted physical unrolling for ______ every attempt to peel apart the fused layers turned the ancient Epicurean treatises into illegible ash.</p>',
            STEM_SEC,
            ['centuries:', 'centuries,', 'centuries', 'centuries; because'],
            'A',
            'Vế trước chỗ trống là một Mệnh đề Độc lập hoàn chỉnh ("the carbonized papyrus scrolls... resisted physical unrolling for centuries"). Vế sau cũng là Mệnh đề Độc lập giải thích trực tiếp VÌ SAO chúng không thể cuộn mở ("every attempt... turned the treatises into illegible ash"). Dấu hai chấm (`:`) sau IC để dẫn mệnh đề giải thích là hoàn toàn chuẩn xác (A)!',
            'Nhớ công thức vàng của dấu hai chấm: [Mệnh đề Độc lập] : [Giải thích / Minh họa / Liệt kê]. Loại ngay dấu phẩy đơn (Comma Splice) và `; because` (Chấm phẩy trước mệnh đề phụ thuộc!).',
            [
                ('Đáp án đúng', 'Dấu hai chấm (:) đặt sau mệnh đề độc lập hoàn chỉnh, giới thiệu chính xác lời giải thích cho việc cuộn giấy không thể mở ra suốt nhiều thế kỷ.'),
                ('Comma Splice', 'Chỉ dùng một dấu phẩy nối hai mệnh đề độc lập là lỗi Comma Splice.'),
                ('Run-on Sentence', 'Không có dấu ngăn cách giữa hai mệnh đề độc lập tạo câu dính liền sai ngữ pháp.'),
                ('Semicolon Before Dependent Clause', 'Dấu chấm phẩy (;) cấm đứng trước mệnh đề phụ thuộc mở đầu bằng "because".'),
            ],
        ),
        q_item(
            'm4_m2h_q17', 17, 'Standard English Conventions', 'Boundaries', 'Hard',
            '<p>In his eleventh-century treatise on geodesy, Central Asian polymath Abu Rayhan al-Biruni combined three distinct measurements to calculate Earth’s radius without leaving a single hilltop: the vertical height of a peak near Nandana, computed via astrolabe ______ the dip angle of the flat Punjabi horizon, recorded from the summit at dawn; and a trigonometric equation linking those two values to planetary curvature.</p>',
            STEM_SEC,
            ['sightings,', 'sightings', 'sightings:', 'sightings;'],
            'D',
            'Quan sát dấu chấm phẩy nằm ở phần sau của câu: `; and a trigonometric equation...`! Đây là phép liệt kê 3 thành phần phức tạp (Complex List), trong đó mỗi mục tự chứa dấu phẩy nội bộ (`..., computed via astrolabe sightings;` / `..., recorded from the summit at dawn;` / `and ...`). Vì vậy cuối mục 1 BẮT BUỘC phải dùng dấu chấm phẩy "siêu phẩy" (`;`) để song song với mục 2 → chọn D!',
            'Mẹo nhận diện Complex List Semicolon trong 2 giây: quét về cuối câu xem có chuỗi `; and ...` hay không; nếu có thì mọi ranh giới giữa các mục lớn trong danh sách đó PHẢI dùng dấu chấm phẩy (;).',
            [
                ('Complex List Mismatch', 'Dùng dấu phẩy thường ở cuối mục 1 sẽ lẫn với dấu phẩy nội bộ và phá vỡ cấu trúc song song với "; and" ở mục 2–3.'),
                ('Missing Separator', 'Bỏ dấu câu làm mục 1 và mục 2 dính liền nhau.'),
                ('Wrong Punctuation (Colon)', 'Dấu hai chấm thứ hai xuất hiện giữa danh sách liệt kê là sai quy tắc.'),
                ('Đáp án đúng', 'Dấu chấm phẩy siêu phẩy (;) phân tách rạch ròi mục 1 và mục 2, khớp tuyệt đối với dấu `; and` ở cuối danh sách.'),
            ],
        ),
        q_item(
            'm4_m2h_q18', 18, 'Standard English Conventions', 'Boundaries', 'Elite (750+)',
            '<p>Standard demographic models assume that rapid urban migration automatically lowers fertility within a single generation. Longitudinal household surveys in West African secondary ______ indicate that circular migrants who maintain rural farmsteads often retain higher family-size norms for decades.</p>',
            STEM_SEC,
            ['cities; however,', 'cities, however,', 'cities, however;', 'cities. However,'],
            'B',
            'BẪY KINH ĐIỂN 750+ ("However" giữa Chủ ngữ và Động từ)! Kiểm tra vế TRƯỚC chỗ trống: "Longitudinal household surveys in West African secondary cities" → CHỈ LÀ CỤM DANH TỪ CHỦ NGỮ (chưa hề có động từ!). Động từ chính của nó nằm ngay sau chỗ trống ("indicate")! Vì chỉ có MỘT mệnh đề duy nhất, "however" đang đóng vai trò từ xen giữa (parenthetical interrupter) kẹp giữa S và V → bắt buộc bọc bằng CẶP HAI DẤU PHẨY: `, however,` (B)!',
            'TUYỆT ĐỐI không chọn `; however,` hay `. However,` theo phản xạ! Luôn kiểm tra xem phía trước "however" đã có đầy đủ S + V tạo thành Mệnh đề Độc lập hay chưa!',
            [
                ('Semicolon After Subject Fragment', 'Đặt dấu chấm phẩy sau cụm chủ ngữ chưa có động từ là lỗi tách rời S–V nghiêm trọng.'),
                ('Đáp án đúng', 'Bọc từ chuyển ý xen giữa bằng cặp phẩy `, however,` nằm gọn giữa Chủ ngữ "Longitudinal household surveys..." và Động từ chính "indicate".'),
                ('Semicolon Before Main Verb', 'Dấu chấm phẩy cắt đứt chủ ngữ khỏi động từ chính "indicate".'),
                ('Sentence Fragment', 'Dấu chấm biến toàn bộ cụm chủ ngữ phía trước thành mảnh vỡ không có động từ.'),
            ],
        ),
        q_item(
            'm4_m2h_q19', 19, 'Standard English Conventions', 'Boundaries', 'Elite (750+)',
            '<p>To measure sub-nanometer surface ripples on vibrating graphene membranes, physicists at ETH Zurich focused an interferometric laser onto suspended carbon sheets whose acoustic resonance depends ______ and crystal lattice orientation.</p>',
            STEM_SEC,
            ['on: tension, sheet thickness,', 'on; tension, sheet thickness,', 'on tension, sheet thickness,', 'on, tension, sheet thickness,'],
            'C',
            'Vùng CẤM dấu câu giữa Giới từ và Tân ngữ! Cụm "whose acoustic resonance depends on" CHƯA phải một mệnh đề độc lập hoàn chỉnh (thiếu tân ngữ của giới từ "on"). Vì vậy CẤM đặt dấu hai chấm (`:`), dấu chấm phẩy (`;`) hay dấu phẩy (`,`) ngay sau giới từ "on" → chọn C (`on tension, sheet thickness,`)!',
            'Quy tắc sắt của dấu hai chấm (:): tuyệt đối KHÔNG đặt dấu hai chấm ngay sau giới từ ("on:", "of:", "to:") hoặc động từ nối ("include:", "are:"). Muốn liệt kê trực tiếp sau giới từ thì dùng 0 dấu câu!',
            [
                ('No-Colon Zone (Prep:)', 'Cấm đặt dấu hai chấm trực tiếp sau giới từ "on" vì vế trước chưa hoàn chỉnh thành mệnh đề độc lập.'),
                ('Semicolon After Preposition', 'Dấu chấm phẩy không thể chen vào giữa giới từ "on" và danh sách tân ngữ.'),
                ('Đáp án đúng', 'Không dấu câu sau "on", nối mượt giới từ với chuỗi 3 tân ngữ có dấu phẩy Oxford chuẩn xác.'),
                ('No-Comma Zone (Prep,)', 'Cấm tách rời giới từ "on" khỏi tân ngữ đầu tiên "tension" bằng một dấu phẩy đơn.'),
            ],
        ),

        # Q20–Q22: Standard English Conventions — Form, Structure, and Sense
        q_item(
            'm4_m2h_q20', 20, 'Standard English Conventions', 'Form, Structure, and Sense', 'Hard',
            '<p>Beneath the permanently frozen crust of Antarctica’s Taylor Glacier, trapped in a hypersaline subglacial reservoir cut off from atmospheric oxygen for nearly two million years, ______ an ancient community of iron-breathing microbes that dyes the escaping meltwater crimson.</p>',
            STEM_SEC,
            ['thrive', 'have thrived', 'are thriving', 'thrives'],
            'D',
            'Cấu trúc ĐẢO NGỮ (Inverted Subject–Verb Order): toàn bộ phần đầu câu là cụm giới từ và cụm phân từ chỉ địa điểm ("Beneath... Glacier, trapped in... years,"). Chủ ngữ thật nằm PHÍA SAU chỗ trống: "an ancient community of iron-breathing microbes"! Danh từ lõi là SỐ ÍT ("an ancient community", cũng được xác nhận bởi động từ số ít "dyes" ở cuối câu) → bắt buộc chọn động từ SỐ ÍT "thrives" (D)!',
            'Khi câu mở đầu bằng cụm giới từ chỉ vị trí ("Beneath...", "Inside...", "Among..."), hãy tìm Chủ ngữ thật đứng NGAY SAU động từ để chia số ít/số nhiều, đừng để bị lừa bởi danh từ số nhiều "years" đứng trước chỗ trống!',
            [
                ('Inverted S–V Agreement Trap', '"thrive" là động từ số nhiều, sai với chủ ngữ lõi số ít "an ancient community".'),
                ('Inverted S–V Agreement Trap', '"have thrived" là động từ số nhiều, không khớp "an ancient community".'),
                ('Inverted S–V Agreement Trap', '"are thriving" là động từ số nhiều, bị đánh lừa bởi "years" và "microbes".'),
                ('Đáp án đúng', '"thrives" là động từ số ít duy nhất hòa hợp với chủ ngữ đảo ngữ số ít "an ancient community".'),
            ],
        ),
        q_item(
            'm4_m2h_q21', 21, 'Standard English Conventions', 'Form, Structure, and Sense', 'Elite (750+)',
            '<p>Comparing the ecological lyrics of Chilean Nobel laureate Gabriela Mistral with those of Polish poet Wisława Szymborska, critic Amara Osei observes that while both writers reject sentimental portraits of wilderness, the two ______ diverge sharply in tone: Mistral’s stanzas pulse with elegiac urgency, whereas Szymborska’s rely on wry, clinical irony.</p>',
            STEM_SEC,
            ['poet’s approaches', 'poets’ approaches', 'poets approaches', 'poets’ approach’s'],
            'B',
            'Kiểm tra từng danh từ: (1) Trước danh từ thứ nhất có số đếm "the two" → bắt buộc là danh từ sở hữu SỐ NHIỀU `poets’` (sở hữu cách của hai nhà thơ); (2) Sau đó là danh từ làm chủ ngữ cho động từ số nhiều "diverge" → cần danh từ số nhiều thường KHÔNG có sở hữu cách: `approaches`! Ghép lại thành `poets’ approaches` (B)!',
            'Công thức kiểm tra Apostrophe 2 bước: (1) Xác định số ít (`’s`) hay số nhiều (`s’`) theo từ hạn định ("the two" → số nhiều `s’`); (2) Kiểm tra danh từ thứ hai có sở hữu thứ gì phía sau không — nếu ngay sau là động từ (`diverge`) thì CẤM thêm `’s` vào danh từ thứ hai!',
            [
                ('Singular Possessive Trap', '"poet’s" là sở hữu số ít (của 1 nhà thơ), mâu thuẫn với "the two".'),
                ('Đáp án đúng', 'Sở hữu cách số nhiều "poets’" khớp với "the two", đi cùng chủ ngữ số nhiều "approaches" hòa hợp với động từ "diverge".'),
                ('Missing Apostrophe', '"poets" thiếu dấu nháy sở hữu cách trước danh từ "approaches".'),
                ('Superfluous Possessive', 'Thêm sở hữu cách vào "approach’s" ngay trước động từ "diverge" làm câu sai ngữ pháp.'),
            ],
        ),
        q_item(
            'm4_m2h_q22', 22, 'Standard English Conventions', 'Form, Structure, and Sense', 'Elite (750+)',
            '<p>When maritime archaeologists located the remarkably preserved wooden wreck of Ernest Shackleton’s ship <i>Endurance</i> three kilometers beneath the Weddell Sea in 2022, the vessel’s oak planking—protected from wood-boring shipworms by near-freezing, nutrient-poor Antarctic waters—______ virtually unaltered since the ship sank in 1915.</p>',
            STEM_SEC,
            ['had remained', 'remaining', 'having remained', 'will remain'],
            'A',
            'Phân tích khung câu chính: Chủ ngữ của mệnh đề chính là "the vessel’s oak planking" (cụm gạch ngang `—protected from... waters—` chỉ là bổ ngữ xen giữa). Mệnh đề chính CẦN một động từ chia thì (Finite Verb) diễn tả trạng thái kéo dài liên tục TỪ mốc quá khứ 1915 ("since the ship sank in 1915") CHO ĐẾN mốc quá khứ 2022 ("When maritime archaeologists located... in 2022") → Quá khứ Hoàn thành `had remained` (A)!',
            'Bước 1: Gạch bỏ cụm kẹp giữa hai dấu gạch ngang (— ... —) để lộ rõ chỗ trống cần Finite Verb (loại ngay `remaining` và `having remained`). Bước 2: Trạng thái kéo dài từ một mốc quá khứ (1915) tới một mốc quá khứ sau đó (2022) → chia Past Perfect (`had + V3`).',
            [
                ('Đáp án đúng', '"had remained" vừa là động từ chia thì hoàn chỉnh mệnh đề chính vừa diễn đạt chuẩn thì Quá khứ Hoàn thành cho khoảng thời gian 1915–2022.'),
                ('Non-Finite Verb (Fragment)', '"remaining" là phân từ, khiến chủ ngữ "the vessel’s oak planking" không có động từ chính.'),
                ('Non-Finite Verb (Fragment)', '"having remained" vẫn là cụm phân từ, gây lỗi câu thiếu vị ngữ chính.'),
                ('Tense Mismatch', 'Thì tương lai "will remain" sai hoàn toàn với mốc quá khứ "When... located... in 2022" và giới từ "since... 1915".'),
            ],
        ),

        # Q23–Q25: Expression of Ideas — Transitions
        q_item(
            'm4_m2h_q23', 23, 'Expression of Ideas', 'Transitions', 'Hard',
            '<p>Long before Edward Jenner introduced cowpox vaccination in 1796, Ottoman women practitioners in Istanbul routinely inoculated children against smallpox by introducing minute traces of fluid from mild cases under the skin. English aristocrat Lady Mary Wortley Montagu witnessed this procedure in 1717 and championed it upon returning to London. ______, many Fellows of the Royal Society initially dismissed the method as folk superstition until statistical trials confirmed its dramatic reduction in smallpox mortality.</p>',
            STEM_TRANS,
            ['Consequently', 'Similarly', 'Nonetheless', 'For example'],
            'C',
            'Câu 2 nêu việc phu nhân Montagu đã tận mắt chứng kiến một phương pháp hiệu quả lâu đời và tích cực cổ vũ nó tại London. Câu 3 nêu kết quả TRÁI KỲ VỌNG: nhiều viện sĩ Hội Hoàng gia ban đầu vẫn bác bỏ nó là mê tín dân gian → Quan hệ Nhượng bộ / Trái kỳ vọng → "Nonetheless" (Tuy nhiên / Dẫu vậy).',
            'So sánh kỳ vọng sau câu 2 (được giới y học đón nhận) với thực tế câu 3 (bị bác bỏ là mê tín) → chốt ngay nhóm đối lập nhượng bộ (`Nonetheless` / `Nevertheless`).',
            [
                ('Wrong Relationship (Cause-Effect)', 'Consequently sai vì sự cổ vũ của Montagu không phải nguyên nhân hợp lý khiến giới bác sĩ bác bỏ phương pháp này.'),
                ('Wrong Relationship (Comparison)', 'Similarly chỉ sự tương đồng, trái với sự đối lập giữa ủng hộ và bác bỏ.'),
                ('Đáp án đúng', 'Nonetheless nối chuẩn xác sự nhượng bộ giữa nỗ lực vận động của Montagu và phản ứng bác bỏ ban đầu của Hội Hoàng gia.'),
                ('Wrong Relationship (Example)', 'For example sai vì phản ứng bác bỏ không phải ví dụ minh họa cho việc cổ vũ phương pháp.'),
            ],
        ),
        q_item(
            'm4_m2h_q24', 24, 'Expression of Ideas', 'Transitions', 'Elite (750+)',
            '<p>Popular accounts often portray the third-century BCE scholar Eratosthenes as having relied on crude guesswork to estimate Earth’s circumference from the shadow cast inside a well at Syene. ______, his geometric calculation—comparing zenith angles at Syene and Alexandria and multiplying by professional bematists’ paced road surveys—achieved an accuracy within roughly two percent of modern satellite measurements.</p>',
            STEM_TRANS,
            ['Indeed', 'Accordingly', 'Similarly', 'In reality'],
            'D',
            'Câu 1 trình bày một ĐỊNH KIẾN PHỔ BIẾN SAI LẦM ("Popular accounts often portray... crude guesswork"). Câu 2 lật ngược định kiến đó bằng SỰ THẬT THỰC TẾ (tính toán hình học đo đạc chính xác đến khoảng 2% so với vệ tinh hiện đại) → chọn "In reality" (Thực tế là)! Tuyệt đối tránh "Indeed" vì "Indeed" chỉ dùng để củng cố cùng chiều câu trước.',
            'Nhận diện cặp tín hiệu "Popular accounts / Historians once assumed / Myth..." ở câu 1 + bằng chứng đảo ngược ở câu 2 → chốt ngay "In reality"!',
            [
                ('Reinforcement Trap', 'Indeed chỉ dùng để nhấn mạnh/đẩy mạnh ý CÙNG CHIỀU câu trước, không dùng để bác bỏ nhận định sai về "crude guesswork".'),
                ('Wrong Relationship (Cause-Effect)', 'Accordingly = do đó — sai hoàn toàn hướng tương phản.'),
                ('Wrong Relationship (Comparison)', 'Similarly chỉ sự tương đồng, ngược với việc phủ nhận quan niệm đại chúng.'),
                ('Đáp án đúng', 'In reality lật ngược chính xác hình ảnh sai lệch ("crude guesswork") bằng độ chính xác hình học thực tế của Eratosthenes.'),
            ],
        ),
        q_item(
            'm4_m2h_q25', 25, 'Expression of Ideas', 'Transitions', 'Elite (750+)',
            '<p>To keep chemotherapy agents from damaging healthy organs while circulating through the bloodstream, bioengineers fold synthetic DNA strands into hollow barrel-shaped nanocapsules locked shut by molecular aptamer clasps. Only when those clasps encounter a protein unique to tumor cell surfaces do the barrels snap open to release their payload. ______, the nanoscale carriers concentrate toxic drugs directly at malignant sites while sparing surrounding tissue.</p>',
            STEM_TRANS,
            ['By contrast', 'In doing so', 'Nevertheless', 'Instead'],
            'B',
            'Câu 2 mô tả hành động có điều kiện của viên nang DNA: chỉ bung mở thuốc khi gặp protein đặc hiệu trên bề mặt tế bào ung thư. Câu 3 nêu kết quả đạt được NHỜ HÀNH ĐỘNG ĐÓ (tập trung thuốc độc trực tiếp vào khối u đồng thời bảo vệ mô lành) → "In doing so" (Bằng cách làm như vậy)! Dùng Synonym Shortcut: A, C, D đều thuộc nhóm Đối lập → loại ngay 3 đáp án đối lập!',
            'Mẹo 3–1 cực hiệu quả cho Transitions Elite: khi thấy 3 từ cùng nhóm Đối lập (`By contrast` / `Nevertheless` / `Instead`) và 1 từ chỉ hệ quả trực tiếp từ hành động (`In doing so`), kiểm tra nhanh mạch hành động → lợi ích để chốt chuẩn xác!',
            [
                ('False Contrast', 'By contrast dùng để đối chiếu hai đối tượng ngược nhau.'),
                ('Đáp án đúng', 'In doing so nối hoàn hảo cơ chế chỉ mở khóa tại bề mặt khối u với lợi ích tập trung thuốc và bảo vệ mô lành.'),
                ('False Contrast', 'Nevertheless chỉ kết quả trái kỳ vọng — việc bảo vệ mô lành chính là mục tiêu thiết kế.'),
                ('Substitution Trap', 'Instead đòi hỏi một hành động bị phủ định ở câu trước để thay thế.'),
            ],
        ),

        # Q26–Q27: Expression of Ideas — Rhetorical Synthesis
        q_item(
            'm4_m2h_q26', 26, 'Expression of Ideas', 'Rhetorical Synthesis', 'Hard',
            '''<p>While researching a topic, a student has taken the following notes:</p>
            <ul>
              <li>African American explorer Matthew Henson accompanied Robert Peary on seven Arctic expeditions between 1891 and 1909.</li>
              <li>Henson became fluent in the Inuktitut language and mastered Inuit dog-sled driving, igloo building, and cold-weather survival techniques.</li>
              <li>On April 6, 1909, Henson, Peary, and four Inuit guides—Ootah, Egigingwah, Seegloo, and Ooqueah—reached the vicinity of the geographic North Pole, with Henson breaking trail roughly forty-five minutes ahead of Peary.</li>
              <li>Despite Henson’s essential logistical and linguistic skills, twentieth-century histories long credited Peary almost exclusively until later scholars restored Henson’s and the Inuit guides’ roles.</li>
            </ul>''',
            'The student wants to emphasize how Matthew Henson’s specialized skills and actions on the 1909 expedition challenge histories that credited Robert Peary almost exclusively. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
            [
                'Although twentieth-century histories long credited Robert Peary almost exclusively for reaching the North Pole in 1909, Matthew Henson—who spoke Inuktitut fluently and mastered Inuit sledding and survival techniques—actually broke trail forty-five minutes ahead of Peary alongside four Inuit guides.',
                'Between 1891 and 1909, explorer Matthew Henson accompanied Robert Peary on seven Arctic expeditions and learned to speak the Inuktitut language fluently.',
                'On April 6, 1909, Robert Peary reached the vicinity of the geographic North Pole alongside four Inuit guides—Ootah, Egigingwah, Seegloo, and Ooqueah.',
                'Later historians revised twentieth-century accounts of the 1909 Arctic expedition that had previously attributed the achievement almost solely to Robert Peary.',
            ],
            'A',
            'Goal-First SOP: Mục tiêu yêu cầu hội tụ ĐỦ 3 mảnh ghép: (1) kỹ năng chuyên môn của Henson (thành thạo tiếng Inuktitut, kỹ thuật trượt tuyết & sinh tồn Inuit), (2) hành động cụ thể năm 1909 (mở đường đi trước Peary 45 phút cùng 4 người dẫn đường Inuit), VÀ (3) dùng chúng để phản bác các sử liệu thế kỷ 20 chỉ ghi công Peary. Chỉ có A gắn kết trọn vẹn cả 3 yếu tố trong một câu tương phản sắc bén!',
            'Trong Rhetorical Synthesis Hard, đếm chính xác số thành phần yêu cầu trong câu Goal (ở đây: skills + 1909 actions + challenge Peary-only histories) rồi gạch loại mọi đáp án thiếu dù chỉ 1 thành phần.',
            [
                ('Đáp án đúng', 'Tích hợp đủ cả kỹ năng chuyên môn, hành động mở đường trước 45 phút năm 1909 và thế đối lập bác bỏ sử liệu chỉ ghi công Peary.'),
                ('Half-Match Trap', 'Chỉ kể số chuyến đi và tiếng Inuktitut, bỏ sót hành động năm 1909 lẫn việc phản bác sử liệu thiên lệch.'),
                ('Wrong Synthesis Goal', 'Bỏ quên hoàn toàn Matthew Henson và không phản bác việc ghi công độc quyền cho Peary.'),
                ('Half-Match Trap', 'Chỉ nêu việc sử gia sau này sửa lại tài liệu mà không trình bày kỹ năng hay hành động cụ thể nào của Henson.'),
            ],
        ),
        q_item(
            'm4_m2h_q27', 27, 'Expression of Ideas', 'Rhetorical Synthesis', 'Elite (750+)',
            '''<p>While researching a topic, a student has taken the following notes:</p>
            <ul>
              <li>Sor Juana Inés de la Cruz (1648–1695) was a Mexican Hieronymite nun, scholar, and Baroque poet in New Spain.</li>
              <li>Her 975-line philosophical poem <i>Primero Sueño</i> (<i>First Dream</i>, 1692) traces the disembodied soul’s nocturnal ascent through the cosmos as it attempts to grasp all natural and scientific knowledge.</li>
              <li>Unlike most seventeenth-century lyric poetry centered on romantic devotion or religious dogma, <i>Primero Sueño</i> draws on Renaissance anatomy, optics, and astronomy.</li>
              <li>Although the soul is ultimately overwhelmed by the sheer complexity of nature and awakens at dawn without total mastery, the poem celebrates the fearless intellectual daring of the inquiry itself.</li>
            </ul>''',
            'The student wants to explain how <i>Primero Sueño</i> differs from typical seventeenth-century lyric poetry and characterize the poem’s ultimate stance toward scientific inquiry. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
            [
                'Written by Mexican Baroque poet Sor Juana Inés de la Cruz in 1692, the 975-line poem <i>Primero Sueño</i> follows a disembodied soul ascending through the night sky in search of universal knowledge.',
                'Whereas typical seventeenth-century lyric poetry focused on romantic devotion or religious dogma, Sor Juana Inés de la Cruz’s <i>Primero Sueño</i> incorporates concepts from Renaissance anatomy, optics, and astronomy.',
                'Breaking from seventeenth-century lyric conventions centered on romance or religious dogma by drawing on Renaissance anatomy, optics, and astronomy, Sor Juana’s <i>Primero Sueño</i> ultimately celebrates the intellectual daring of scientific inquiry even though the soul fails to achieve complete mastery.',
                'Because the soul in Sor Juana’s <i>Primero Sueño</i> awakens at dawn overwhelmed by nature’s complexity, the poem concludes that seventeenth-century anatomy and astronomy are inferior to religious dogma.',
            ],
            'C',
            'Mục tiêu KÉP Elite: (1) giải thích *Primero Sueño* KHÁC thơ trữ tình thế kỷ 17 điển hình ra sao (không xoay quanh tình yêu hay giáo điều tôn giáo mà vận dụng giải phẫu, quang học và thiên văn Phục hưng), VÀ (2) nêu LẬP TRƯỜNG CUỐI CÙNG của bài thơ với việc tìm tòi khoa học (ngợi ca sự táo bạo trí tuệ của chính hành trình tìm hiểu dù linh hồn không thể làm chủ toàn bộ tri thức). Chỉ C chuẩn xác cả hai vế!',
            'Trong Rhetorical Synthesis Elite, cẩn thận với bẫy D (bịa đặt kết luận ngược với ghi chú gốc — Distorted Synthesis) và bẫy B (đúng 100% dữ kiện nhưng mới hoàn thành đúng 1 nửa Goal).',
            [
                ('Wrong Synthesis Goal', 'Chỉ giới thiệu bối cảnh và cốt truyện chung của bài thơ, thiếu cả sự đối chiếu với thơ thế kỷ 17 lẫn lập trường cuối cùng.'),
                ('Half-Match Trap', 'Chỉ nêu được điểm khác biệt với thơ trữ tình thế kỷ 17, bỏ sót hoàn toàn lập trường cuối cùng của bài thơ về tìm tòi khoa học.'),
                ('Đáp án đúng', 'Hoàn thành trọn vẹn cả hai vế: đối chiếu chuẩn xác với thơ thế kỷ 17 và nêu đúng lập trường ngợi ca lòng dũng cảm trí tuệ dù không đạt toàn tri.'),
                ('Distorted Synthesis', 'Bóp méo ngược ghi chú gốc: bài thơ ca ngợi sự táo bạo của tìm tòi khoa học chứ không hề coi khoa học kém hơn giáo điều tôn giáo.'),
            ],
        ),
    ]
