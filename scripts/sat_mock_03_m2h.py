# -*- coding: utf-8 -*-
"""
Digital SAT Reading & Writing Adaptive Mock Test #3
Module 2 Hard Route (27 Questions, Hard & Elite 750+ Tier)
IDs: m3_m2h_q1 .. m3_m2h_q27
"""

from sat_drills_1_1_and_2_1 import q_item
from sat_drills_5_4_to_5_5 import svg_bar_chart, html_table

STEM_WIC = 'Which choice completes the text with the most logical and precise word or phrase?'
STEM_SEC = 'Which choice completes the text so that it conforms to the conventions of Standard English?'
STEM_TRANS = 'Which choice completes the text with the most logical transition?'
STEM_INF = 'Which choice most logically completes the text?'


def get_m2h_questions():
    return [
        # ------------------------------------------------------------------
        # Q1-Q5: Craft and Structure — Words in Context
        # ------------------------------------------------------------------
        q_item(
            'm3_m2h_q1', 1, 'Craft and Structure', 'Words in Context', 'Hard',
            '<p>Because amputees frequently experience vivid phantom-limb sensations years after peripheral nerves have been severed, neuroscientists argue that body maps in the somatosensory cortex are not merely passive mirror images of incoming sensory traffic but ______ representations actively sustained by central neural circuitry.</p>',
            STEM_WIC,
            ['ephemeral', 'derivative', 'autonomous', 'superficial'],
            'C',
            'Cấu trúc tương phản "not merely passive mirror images of incoming sensory traffic but ______ representations actively sustained by central neural circuitry": bản đồ cơ thể không chỉ sao chép thụ động tín hiệu bên ngoài mà tự duy trì hoạt động một cách "độc lập / tự chủ" từ bên trong mạch thần kinh trung ương → "autonomous" (C).',
            'Khóa cặp đối lập "not merely passive... incoming" ↔ "actively sustained by central circuitry" để loại ngay các từ mang nghĩa phụ thuộc ("derivative") hoặc thoáng qua ("ephemeral").',
            [
                ('Opposite Meaning', 'ephemeral = phù du, ngắn ngủi — trái ngược với cảm giác chi ma kéo dài nhiều năm ("years after").'),
                ('Opposite Meaning', 'derivative = phái sinh/phụ thuộc nguồn khác — trùng hướng với "passive mirror images" thay vì đối lập sau "but".'),
                ('Đáp án đúng', 'autonomous = tự chủ/độc lập, khớp chính xác với việc mạch thần kinh trung ương chủ động duy trì bản đồ cơ thể dù dây thần kinh ngoại biên đã bị cắt.'),
                ('Wrong Meaning', 'superficial = hời hợt/bề mặt — không phù hợp với đặc tính cảm giác sâu sắc sống động và được duy trì bền bỉ.'),
            ]
        ),
        q_item(
            'm3_m2h_q2', 2, 'Craft and Structure', 'Words in Context', 'Elite (750+)',
            '<p>Far from resembling a monolithic imperial highway administered by a single court, the early medieval Silk Road functioned as a ______ relay of oasis brokers, regional merchant guilds, and nomadic guides whose itineraries shifted constantly in response to local tolls and desert hydrology.</p>',
            STEM_WIC,
            ['decentralized', 'standardized', 'insular', 'hereditary'],
            'A',
            'Cụm mở đầu "Far from resembling a monolithic imperial highway administered by a single court" tạo thế đối lập 180 độ với chỗ trống: thay vì tập trung quyền lực vào một triều đình duy nhất, Con đường Tơ lụa vận hành như một mạng lưới chuyển tiếp "phi tập trung" của nhiều phường hội, môi giới ốc đảo và dẫn đường du mục → "decentralized" (A).',
            'Cấu trúc "Far from X (single court)" lập tức đòi hỏi từ trái nghĩa trực diện với "single centralized authority" → "decentralized".',
            [
                ('Đáp án đúng', 'decentralized = phi tập trung, đối lập tuyệt đối với "administered by a single court" và khớp với chuỗi tác nhân địa phương linh hoạt.'),
                ('Opposite Meaning', 'standardized = chuẩn hóa đồng nhất — ngược với "itineraries shifted constantly in response to local tolls".'),
                ('Wrong Meaning', 'insular = khép kín/cô lập — sai hoàn toàn với bản chất kết nối thương mại liên vùng của Con đường Tơ lụa.'),
                ('Out of Scope', 'hereditary = cha truyền con nối — văn bản không đề cập quyền thừa kế gia truyền.'),
            ]
        ),
        q_item(
            'm3_m2h_q3', 3, 'Craft and Structure', 'Words in Context', 'Hard',
            '<p>While the allelopathic compound juglone released by black walnut roots severely stunts the growth of nearby tomato and apple plants, native elderberries and black raspberries prove remarkably ______ to the toxin, thriving directly beneath the walnut canopy.</p>',
            STEM_WIC,
            ['susceptible', 'conducive', 'indebted', 'impervious'],
            'D',
            'Mệnh đề "While... severely stunts" đặt cà chua/táo đối lập với cây cơm cháy và mâm xôi đen bản địa mọc xanh tốt ngay dưới tán óc chó ("thriving directly beneath the walnut canopy") → chúng hoàn toàn "miễn nhiễm / không bị ảnh hưởng" bởi độc tố juglone → "impervious" (đi kèm giới từ "to").',
            'Nhận diện cặp đối lập kinh điển trong sinh học: "severely stunts" ↔ "thriving directly beneath" = "impervious to" (miễn nhiễm/trơ trước tác động).',
            [
                ('Opposite Meaning', 'susceptible (to) = dễ bị tổn thương bởi — trái ngược hoàn toàn với "thriving".'),
                ('Wrong Meaning / Collocation', 'conducive (to) = tạo điều kiện thuận lợi cho — cây mâm xôi không phải "tạo điều kiện cho độc tố".'),
                ('Wrong Meaning', 'indebted (to) = mắc nợ/nhờ ơn — sai logic vì độc tố không phải thứ giúp cây mâm xôi sống.'),
                ('Đáp án đúng', 'impervious (to) = không bị xuyên thủng/không chịu ảnh hưởng bởi độc tố — khớp hoàn hảo cả nghĩa lẫn giới từ "to".'),
            ]
        ),
        q_item(
            'm3_m2h_q4', 4, 'Craft and Structure', 'Words in Context', 'Elite (750+)',
            '<p>When acoustic physicists tried to replicate the resonant warmth of eighteenth-century Cremonese violins solely by copying their exterior plate geometry, the resulting prototypes sounded brittle and thin—suggesting that mineral varnish chemistry and aged spruce density play a role far less ______ than purely geometric models had assumed.</p>',
            STEM_WIC,
            ['indispensable', 'negligible', 'consequential', 'ambiguous'],
            'B',
            'Bẫy Đảo Chiều 750+ với cụm "far less ______"! Thực tế: chỉ chép hình học bề mặt khiến đàn kêu chói và mỏng → chứng tỏ hóa học lớp véc-ni và mật độ gỗ vân sam QUAN TRỌNG HƠN NHIỀU so với giả định của mô hình hình học thuần túy. Vì trước chỗ trống có "far less" (ít ... hơn nhiều), từ điền vào phải mang nghĩa "không đáng kể" → "far less negligible" (= ít không đáng kể hơn nhiều = quan trọng hơn nhiều) → Chọn B!',
            'Cảnh giác cao độ với các cụm đảo dấu như "far less ___", "scarcely ___", "hardly ___": luôn thay thử từ vào và đọc ngược lại toàn cụm ("far less negligible" = "far more important")!',
            [
                ('Negation Reversal Trap', '"far less indispensable" = ít thiết yếu hơn nhiều — đảo ngược hoàn toàn kết luận thí nghiệm!'),
                ('Đáp án đúng', '"far less negligible" = ít không đáng kể hơn nhiều (tức đóng vai trò quan trọng vượt xa dự đoán của mô hình hình học).'),
                ('Negation Reversal Trap', '"far less consequential" = ít quan trọng hơn nhiều — rơi thẳng vào bẫy bỏ quên cụm "far less".'),
                ('Wrong Meaning', 'ambiguous = mơ hồ — mô hình hình học xem nhẹ chứ không xem yếu tố gỗ/véc-ni là "mơ hồ".'),
            ]
        ),
        q_item(
            'm3_m2h_q5', 5, 'Craft and Structure', 'Words in Context', 'Elite (750+)',
            '<p>Although early twentieth-century reviewers frequently dismissed Sarah Orne Jewett’s Maine coastal stories as charming exercises in provincial nostalgia, contemporary literary historians argue that her understated sketches of shuttered shipyards and aging mariners astutely ______ the quiet economic dislocation left behind by industrial consolidation.</p>',
            STEM_WIC,
            ['repudiate', 'embellish', 'register', 'forestall'],
            'C',
            'Nghĩa học thuật bậc hai (Secondary Meaning) cực hay ra ở Hard Module 2! "Although early reviewers dismissed... nostalgia" đối lập với đánh giá hiện đại: những phác họa tiết chế về xưởng tàu đóng cửa và thủy thủ già của Jewett đã tinh tế "ghi nhận / phản ánh sắc sảo" sự xáo trộn kinh tế lặng lẽ của công nghiệp hóa → "register" (C).',
            'Ghi nhớ nghĩa học thuật bậc 2 của "register" trên Digital SAT: không chỉ là "đăng ký" mà còn là "ghi nhận tinh tế / phản ánh chính xác" một biến chuyển xã hội hoặc cảm xúc!',
            [
                ('Opposite Meaning', 'repudiate = bác bỏ/chối bỏ — tác phẩm của Jewett khắc họa chứ không phủ nhận sự suy thoái kinh tế.'),
                ('Wrong Tone', 'embellish = thêu dệt/tô vẽ quá mức — trái ngược với tính từ "understated" (tiết chế, mộc mạc).'),
                ('Đáp án đúng', 'register = ghi nhận, phản ánh tinh tường (nghĩa học thuật chuẩn mực khớp với "astutely" và "understated").'),
                ('Wrong Meaning', 'forestall = ngăn chặn trước — truyện ngắn không thể ngăn chặn quá trình tập trung công nghiệp đã diễn ra.'),
            ]
        ),

        # ------------------------------------------------------------------
        # Q6-Q7: Craft and Structure — Text Structure and Purpose
        # ------------------------------------------------------------------
        q_item(
            'm3_m2h_q6', 6, 'Craft and Structure', 'Text Structure and Purpose', 'Hard',
            '<p>For decades, glaciological models projected summer ice loss across western Greenland primarily from air temperatures and snow-grain physics, assuming that surface reflectivity depended mostly on inorganic weather factors. <u>Yet field studies of dark surface sediment known as cryoconite reveal that windblown mineral dust binds with pigmented cyanobacteria into heat-absorbing granules that melt downward into water-filled pockets, sharply reducing ice albedo across vast ablation zones.</u> Consequently, climate researchers now stress that ice-sheet projections must couple biological surface processes with atmospheric thermodynamics.</p>',
            'Which choice best describes the function of the underlined sentence in the text as a whole?',
            [
                'It demonstrates that inorganic air temperatures have no measurable effect on summer ice loss in western Greenland.',
                'It compares the growth rate of Greenland cyanobacteria with that of Antarctic ice-shelf microbes.',
                'It clarifies why older glaciological models underestimated winter snowfall accumulation.',
                'It details a biogeophysical darkening process that challenges the modeling assumption described in the preceding sentence.'
            ],
            'D',
            'Câu 1 nêu giả định cũ của các mô hình băng hà (độ phản xạ bề mặt chủ yếu phụ thuộc yếu tố vô sinh như nhiệt độ và hạt tuyết). Câu gạch chân bắt đầu bằng "Yet" mô tả cơ chế kết hợp sinh học – địa vật lý của cryoconite (bụi khoáng + vi khuẩn lam có sắc tố hấp thụ nhiệt, khoét lỗ nước và giảm mạnh albedo băng), làm cơ sở cho kết luận ở câu cuối rằng mô hình khí hậu phải tích hợp yếu tố sinh học → Chọn D.',
            'Luôn đọc kẹp 3 câu: Câu trước (Old assumption: inorganic factors) → Câu gạch chân ("Yet" + biological-mineral mechanism) → Câu sau ("Consequently" + must couple biological processes).',
            [
                ('Too Extreme', 'Câu gạch chân bổ sung nhân tố sinh học quan trọng chứ KHÔNG khẳng định nhiệt độ không khí vô sinh "vô tác dụng".'),
                ('Out of Scope', 'Không hề so sánh với vi sinh vật ở Nam Cực.'),
                ('Wrong Focus', 'Bài nói về tốc độ tan băng mùa hè ("summer ice loss" / "albedo"), không bàn về lượng tuyết rơi mùa đông.'),
                ('Đáp án đúng', 'Nêu chuẩn xác vai trò câu gạch chân: trình bày cơ chế làm tối bề mặt mang tính sinh-địa-vật lý thách thức giả định thuần vô sinh ở câu liền trước.'),
            ]
        ),
        q_item(
            'm3_m2h_q7', 7, 'Craft and Structure', 'Text Structure and Purpose', 'Elite (750+)',
            '<p>In memory psychology, “retrieval-induced forgetting” describes a counterintuitive effect: when participants repeatedly practice recalling half of the items in a studied category (such as “fruit—orange”), they subsequently perform worse at recalling the unpracticed items from that same category (“fruit—banana”) than unpracticed items from an unrelated category (“metal—copper”). Early associative models attributed this drop to competition at recall—practiced items simply crowded out weaker rivals. However, functional MRI experiments demonstrating elevated lateral prefrontal activation paired with selective suppression of competing hippocampal traces during practice have tilted consensus toward an active inhibitory mechanism, in which the brain deliberately dampens rival memories to sharpen target retrieval.</p>',
            'Which choice best describes the overall structure of the text?',
            [
                'It introduces a neurological disorder, summarizes failed clinical treatments, and proposes a new diagnostic scan.',
                'It defines a surprising memory phenomenon, outlines an earlier theoretical explanation for it, and cites neuroimaging evidence supporting an alternative mechanism.',
                'It compares two experimental groups who studied different word categories and concludes that neither group retained the material.',
                'It traces the chronological biography of the psychologists who coined the term “retrieval-induced forgetting.”'
            ],
            'B',
            'Sơ đồ cấu trúc toàn đoạn: [Phần 1] Định nghĩa hiện tượng trí nhớ phản trực giác ("retrieval-induced forgetting") kèm ví dụ minh họa; [Phần 2] Trình bày lý thuyết cũ giải thích hiện tượng ("Early associative models attributed..."); [Phần 3] Dùng "However" đưa bằng chứng quét fMRI ủng hộ cơ chế thay thế (ức chế chủ động từ vỏ não trước trán) → Khớp hoàn hảo với B!',
            'Trong câu hỏi Overall Structure của Hard Module 2, chia đoạn thành 3 khối rõ ràng (Phenomenon → Older theory → "However" + Evidence for alternative mechanism) và khớp tuần tự từng động từ trong đáp án.',
            [
                ('Wrong Frame', 'Retrieval-induced forgetting là cơ chế trí nhớ bình thường ở người khỏe mạnh, KHÔNG phải rối loạn thần kinh hay điều trị lâm sàng.'),
                ('Đáp án đúng', 'Phản ánh chính xác từng bước triển khai: định nghĩa hiện tượng gây bất ngờ → nêu giải thích lý thuyết cũ → trích bằng chứng fMRI ủng hộ cơ chế mới.'),
                ('Distortion', 'Đoạn văn chỉ so sánh hiệu suất nhớ hai nhóm từ cùng loại/khác loại chứ không kết luận "không nhóm nào nhớ được bài".'),
                ('Out of Scope', 'Không đề cập tiểu sử của bất kỳ nhà tâm lý học nào.'),
            ]
        ),

        # ------------------------------------------------------------------
        # Q8: Craft and Structure — Cross-Text Connections
        # ------------------------------------------------------------------
        q_item(
            'm3_m2h_q8', 8, 'Craft and Structure', 'Cross-Text Connections', 'Elite (750+)',
            '<p><b>Text 1</b><br/>Economic historians have long attributed the decline of the trans-Saharan gold caravans linking Timbuktu to North Africa primarily to the arrival of Portuguese caravels along the West African coast in the late fifteenth century. According to this maritime-diversion model, cheaper ocean transport rapidly siphoned inland gold away from desert camel routes, rendering Saharan commerce marginal by the early 1500s.</p><p><b>Text 2</b><br/>Examining Arabic commercial correspondence and toll accounts preserved in Kano, Gao, and Tripoli, historian Mariama Diallo demonstrates that trans-Saharan trade in gold, kola nuts, and textiles actually remained vigorous throughout most of the sixteenth century. Diallo argues that the decisive contraction of the northern routes occurred only after the 1591 Moroccan military invasion fractured the Songhai Empire’s administrative security along the Niger bend.</p>',
            'Based on the texts, how would Mariama Diallo (Text 2) most likely evaluate the maritime-diversion model described in Text 1?',
            [
                'It overstates the immediate sixteenth-century impact of Portuguese coastal shipping and overlooks the later political upheaval that decisively disrupted caravan volume.',
                'It accurately dates the collapse of trans-Saharan trade to the early 1500s but misidentifies the European nation responsible for coastal shipping.',
                'It underestimates how quickly Portuguese caravels eliminated the demand for kola nuts and textiles in North African cities.',
                'It relies too heavily on Arabic toll accounts from Tripoli while ignoring Portuguese ship logs from the late fifteenth century.'
            ],
            'A',
            'Text 1 khẳng định tàu biển Bồ Đào Nha cuối thế kỷ 15 đã nhanh chóng hút cạn tuyến vàng xuyên Sahara ngay từ đầu thập niên 1500 ("rendering Saharan commerce marginal by the early 1500s"). Text 2 (Diallo) chứng minh bằng sổ sách thương mại rằng thương mại xuyên Sahara vẫn rất sôi động suốt gần trọn thế kỷ 16 và chỉ suy sụp thực sự sau cuộc xâm lược năm 1591 của Maroc làm tan vỡ an ninh quản trị của Đế chế Songhai → Diallo sẽ đánh giá mô hình Text 1 phóng đại tác động tức thời của tuyến biển Bồ Đào Nha và bỏ qua biến cố chính trị sau đó (1591) → Chọn A.',
            'Soi chuẩn mốc thời gian (early 1500s vs. 1591) và nguyên nhân cốt lõi (Portuguese coastal shipping vs. Moroccan military invasion fracturing Songhai security).',
            [
                ('Đáp án đúng', 'Khớp trọn vẹn phản biện của Diallo: Text 1 đánh giá quá cao tác động tức thì của vận tải biển Bồ Đào Nha đầu thế kỷ 16 và bỏ sót cú sốc chính trị năm 1591.'),
                ('Contradiction', 'Diallo bác bỏ hoàn toàn mốc sụp đổ "early 1500s" (bà chứng minh thương mại vẫn mạnh suốt hầu hết thế kỷ 16).'),
                ('Reversed Logic', 'Diallo cho rằng mô hình Text 1 PHÓNG ĐẠI chứ không phải đánh giá thấp tác động của tàu Bồ Đào Nha.'),
                ('Swapped Attribution', 'Chính Diallo mới là người sử dụng sổ sách thuế tiếng Ả Rập ở Tripoli/Kano/Gao, không phải mô hình Text 1.'),
            ]
        ),

        # ------------------------------------------------------------------
        # Q9-Q10: Information and Ideas — Central Ideas and Details
        # ------------------------------------------------------------------
        q_item(
            'm3_m2h_q9', 9, 'Information and Ideas', 'Central Ideas and Details', 'Hard',
            '<p>In extreme-ultraviolet microchip lithography, optical lenses must be positioned with sub-nanometer repeatability inside high-vacuum chambers where conventional ball-bearing slides fail due to microscopic friction, mechanical play, and lubricant evaporation. To overcome these hurdles, precision engineers machine monolithic “compliant flexure” stages out of single blocks of spring alloy: thin, strategically placed elastic hinges flex smoothly without rolling contact, completely eliminating backlash and lubricant contamination—though because metal can bend elastically only so far without fatiguing, such stages are typically restricted to a few millimeters of travel.</p>',
            'Which choice best states the main idea of the text?',
            [
                'Conventional ball-bearing slides outperform compliant flexure stages whenever nanometer repeatability is required inside vacuum chambers.',
                'Compliant flexure stages rely on specialized vacuum-safe liquid lubricants to prevent metal fatigue during long-distance travel.',
                'By using elastic bending in a single piece of metal rather than sliding joints, compliant flexure stages achieve frictionless, ultra-precise positioning at the cost of limited travel range.',
                'Extreme-ultraviolet microchip lithography has become impractical because monolithic spring-alloy stages cannot move more than a few millimeters.'
            ],
            'C',
            'Mạch ý chính: Bàn dịch chuyển biến dạng đàn hồi nguyên khối (compliant flexure stages) thay thế khớp trượt/bi bằng bản lề đàn hồi uốn trong 1 khối kim loại duy nhất → giải quyết dứt điểm ma sát, độ rơ (backlash) và bay hơi dầu bôi trơn cho độ chính xác dưới nanomet, NHƯNG đánh đổi bằng hành trình di chuyển ngắn chỉ vài milimét → Chọn C.',
            'Với đoạn kỹ thuật nêu cả Ưu điểm cơ chế (how it achieves X) lẫn Đánh đổi ("though... restricted to..."), đáp án Main Idea chuẩn phải gói gọn cả hai vế!',
            [
                ('Contradiction', 'Ngược hoàn toàn văn bản: ổ bi truyền thống thất bại trong chân không vì ma sát, độ rơ và bay hơi dầu.'),
                ('Contradiction', 'Bản lề đàn hồi không cần khớp lăn trượt nên loại bỏ hoàn toàn dầu bôi trơn ("eliminating... lubricant contamination").'),
                ('Đáp án đúng', 'Tóm gọn chuẩn xác cả cơ chế (uốn đàn hồi nguyên khối không khớp trượt), lợi ích (không ma sát, siêu chính xác) và đánh đổi (phạm vi hành trình hạn chế).'),
                ('Unsupported Leap', 'Văn bản chỉ nêu giới hạn hành trình vài milimét chứ KHÔNG hề nói công nghệ quang khắc trở nên bất khả thi.'),
            ]
        ),
        q_item(
            'm3_m2h_q10', 10, 'Information and Ideas', 'Central Ideas and Details', 'Elite (750+)',
            '<p>Atmospheric chemists refer to the tropospheric hydroxyl radical (•OH) as Earth’s primary chemical detergent. Generated when ultraviolet sunlight splits ozone and the resulting excited oxygen atoms react with water vapor, each •OH molecule persists for less than a second before oxidizing trace greenhouse gases such as methane into water-soluble compounds that rain washes from the sky. Yet this cleansing pathway harbors a subtle feedback: because neutralizing every methane molecule consumes an •OH radical, sharp surges in global methane emissions can draw down regional •OH concentrations, slowing the removal rate of remaining methane and prolonging its atmospheric lifetime.</p>',
            'According to the text, why can a steep rise in methane emissions extend how long methane remains in the atmosphere?',
            [
                'Methane molecules block ultraviolet sunlight from reaching water vapor, halting all ozone formation in the stratosphere.',
                'Oxidizing methane creates additional water-soluble compounds that prevent rainfall from clearing trace gases.',
                'Higher methane levels cause individual •OH radicals to persist far longer than one second without reacting.',
                'Breaking down excess methane uses up the available •OH radicals needed to oxidize other methane molecules, reducing the overall rate of clearance.'
            ],
            'D',
            'Định vị trực tiếp câu sau dấu hai chấm ở cuối đoạn: "because neutralizing every methane molecule consumes an •OH radical, sharp surges in global methane emissions can draw down regional •OH concentrations, slowing the removal rate of remaining methane and prolonging its atmospheric lifetime" → Do việc oxy hóa methane tiêu thụ chính các gốc •OH cần thiết để làm sạch lượng methane còn lại, tốc độ đào thải chậm lại → Chọn D.',
            'Với câu hỏi Detail "According to the text, why...", lần đúng mệnh đề `because...` giải thích trực tiếp cơ chế phản hồi dương (positive feedback) và loại sạch mọi suy diễn ngoài bài.',
            [
                ('Out of Scope / Distortion', 'Bài không nói methane chặn tia UV hay làm ngừng hình thành ozone tầng bình lưu.'),
                ('Reversed Logic', 'Hợp chất tan trong nước chính là dạng được mưa rửa trôi khỏi khí quyển, không phải thứ cản trở mưa.'),
                ('Contradiction', 'Methane tăng làm cạn kiệt nồng độ •OH vì tiêu thụ chúng, không làm từng gốc •OH sống lâu hơn 1 giây mà không phản ứng.'),
                ('Đáp án đúng', 'Diễn đạt sát 100% cơ chế tiêu thụ gốc •OH làm giảm tốc độ oxy hóa và kéo dài thời gian tồn lưu của methane.'),
            ]
        ),

        # ------------------------------------------------------------------
        # Q11-Q12: Information and Ideas — Command of Evidence (Textual)
        # ------------------------------------------------------------------
        q_item(
            'm3_m2h_q11', 11, 'Information and Ideas', 'Command of Evidence (Textual)', 'Elite (750+)',
            '<p>Neuroscientists investigating spatial navigation in mammals recorded “grid cells” in the entorhinal cortex, whose firing sites form a strikingly regular hexagonal lattice across an animal’s floor space. A research team hypothesized that the orientation of this hexagonal grid is anchored primarily by internal self-motion signals—such as inner-ear acceleration and stride counting—rather than by external visual landmarks in the surrounding enclosure.</p>',
            'Which experimental finding, if true, would most directly weaken the research team’s hypothesis?',
            [
                'When researchers rotate a high-contrast cue card mounted on the wall of a symmetrical circular arena while the animal rests outside, the hexagonal orientation of its grid-cell firing pattern rotates by the exact same angle during the next exploration.',
                'When an arena’s floor area is doubled without changing wall color, grid cells expand the spacing between adjacent firing vertices over several days.',
                'Animals with intact inner-ear balance organs continue to show stable hexagonal grid-cell patterns even after all ambient acoustic noise is eliminated.',
                'Grid cells fire at slightly higher peak rates when an animal sprints across an arena than when it walks slowly along the perimeter.'
            ],
            'A',
            'Phân tích giả thuyết cần BÁC BỎ (Weaken): Nhóm nghiên cứu cho rằng hướng của mạng lưới tế bào lưới (hexagonal grid orientation) được neo chủ yếu bởi tín hiệu tự vận động nội tại (internal self-motion) CHỨ KHÔNG PHẢI bởi mốc thị giác bên ngoài (external visual landmarks). Để phá vỡ trực diện giả thuyết này, cần bằng chứng cho thấy chỉ cần xoay một mốc thị giác trên tường đấu trường thì hướng mạng lưới tế bào lưới xoay theo đúng góc đó → Đáp án A giáng đòn trực diện tuyệt đối!',
            'Với câu hỏi Weaken có cấu trúc "anchored by X rather than Y", bằng chứng bác bỏ mạnh nhất là thí nghiệm can thiệp trực tiếp vào biến Y (xoay thẻ thị giác) và thấy kết quả dịch chuyển khớp chính xác theo Y!',
            [
                ('Đáp án đúng', 'Chứng minh trực tiếp rằng xoay một mốc thị giác trên tường lập tức xoay toàn bộ định hướng mạng lưới tế bào lưới theo đúng góc đó — bác bỏ giả thuyết neo nội tại.'),
                ('Off-Target Variable', 'Thay đổi kích thước sàn làm giãn khoảng cách đỉnh lưới không tách bạch được giữa tín hiệu tự vận động và mốc thị giác đối với hướng lưới.'),
                ('Irrelevant Variable (Audio)', 'Loại bỏ tiếng ồn âm học không kiểm chứng được vai trò của mốc thị giác so với tín hiệu tự vận động.'),
                ('Supports / Irrelevant', 'Tốc độ phát xung tăng khi chạy nhanh thậm chí phù hợp với tín hiệu vận động chứ không làm yếu giả thuyết.'),
            ]
        ),
        q_item(
            'm3_m2h_q12', 12, 'Information and Ideas', 'Command of Evidence (Textual)', 'Hard',
            '<p>In a critique of the 1921 Ohio Valley poem “The Limestone Quarry,” a scholar claims that the speaker’s attitude toward the abandoned excavation shifts from recoiling at it as an unnatural industrial wound to appreciating how wild plants and rainwater have transformed it into a quiet refuge of ecological renewal.</p>',
            'Which quotation from “The Limestone Quarry” most effectively illustrates the scholar’s claim?',
            [
                '“For twenty years the steam drills bit the ridge / Till freight cars hauled our hillside east to bridge / The muddy river towns in blocks of gray.”',
                '“At first I flinched before the blasted stair / Of raw-cut stone, a scar no plow could mend— / Yet now the spring-fed pool shines blue and clear, / Where willow roots and nesting warblers blend.”',
                '“No foreman blows the noon-time whistle now, / Nor grinds the iron crusher down the lane; / Only a rusted winch leans on the brow / Above the silent wagons in the rain.”',
                '“Look how the cedar clutches to the crest / And drops its bitter berries in the grass, / While autumn clouds drift westward without rest / Above the narrow road where farmers pass.”'
            ],
            'B',
            'Checklist 2 vế + sự CHUYỂN BIẾN (shift): [1] Ban đầu ghê sợ/dè chừng mỏ đá như vết thương công nghiệp nhân tạo ("recoiling... unnatural industrial wound") → [2] Chuyển sang trân trọng việc thực vật hoang dã và nước mưa biến nó thành nơi tái sinh tĩnh lặng ("wild plants and rainwater... quiet refuge of ecological renewal"). Chỉ có B chứa trọn cả bước ngoặt ("At first I flinched before the blasted stair / Of raw-cut stone, a scar..." → "Yet now the spring-fed pool shines... Where willow roots and nesting warblers blend") → Chọn B!',
            'Câu hỏi có chữ "shifts from X to Y": BẮT BUỘC phải thấy cả X, cả từ chuyển hướng thời gian/đối lập ("At first... Yet now..."), lẫn Y ngay trong trích dẫn!',
            [
                ('Half-Match Trap', 'Chỉ kể lại lịch sử khai thác đá bằng máy khoan hơi nước, hoàn toàn không có sự chuyển biến sang tái sinh sinh thái.'),
                ('Đáp án đúng', 'Thể hiện trọn vẹn sự chuyển đổi từ "flinched... blasted stair... scar" (vết thương công nghiệp) sang "spring-fed pool... willow roots and nesting warblers" (tái sinh sinh thái).'),
                ('Half-Match Trap', 'Chỉ miêu tả khung cảnh bỏ hoang tĩnh lặng với máy tời rỉ sét, thiếu cả sự phản cảm ban đầu lẫn hình ảnh thiên nhiên tái sinh.'),
                ('Out of Scope', 'Chỉ tả cảnh cây tuyết tùng và mây mùa thu bên con đường nông dân đi qua, không liên quan đến vết thương mỏ đá bị bỏ hoang.'),
            ]
        ),

        # ------------------------------------------------------------------
        # Q13-Q14: Information and Ideas — Command of Evidence (Quantitative)
        # ------------------------------------------------------------------
        q_item(
            'm3_m2h_q13', 13, 'Information and Ideas', 'Command of Evidence (Quantitative)', 'Elite (750+)',
            svg_bar_chart(
                'Mean Annual Precipitation (mm/year) Across a Windward-to-Leeward Mountain Transect',
                ['0', '700', '1400', '2100', '2800'],
                [
                    ('Wind. Lowland', 1120, '1,120 mm'),
                    ('Wind. Mid-Slope', 2480, '2,480 mm'),
                    ('Alpine Crest', 1860, '1,860 mm'),
                    ('Leeward Basin', 340, '340 mm'),
                ],
                2800
            ) + '<p>As humid maritime air is forced upward over coastal mountains, cooling condenses vapor into orographic precipitation, leaving dry air on the sheltered leeward side. A meteorology student reviewing this mechanism assumes that annual precipitation increases steadily with elevation all the way up to the highest alpine crest before falling sharply in the leeward rain-shadow basin.</p>',
            'Which choice best describes data from the graph that directly challenge the student’s assumption?',
            [
                'Mean annual precipitation drops steeply from 1,860 mm at the alpine crest to 340 mm in the leeward rain-shadow basin.',
                'Mean annual precipitation at the windward lowland (1,120 mm) is more than three times greater than in the leeward basin (340 mm).',
                'Mean annual precipitation is higher at the alpine crest (1,860 mm) than at the windward lowland (1,120 mm).',
                'Although annual precipitation rises from 1,120 mm at the windward lowland to 2,480 mm at the windward mid-slope, it actually decreases to 1,860 mm at the higher alpine crest.'
            ],
            'D',
            'Đọc kỹ giả định của sinh viên cần BÁC BỎ (challenge): sinh viên cho rằng lượng mưa tăng đều liên tục theo độ cao CHO TỚI TẬN ĐỈNH CAO NHẤT (Alpine Crest) rồi mới giảm ở sườn khuất gió. Soi biểu đồ: mưa tăng từ 1,120 mm (Lowland) lên đỉnh 2,480 mm ở sườn giữa (Windward Mid-Slope), NHƯNG lại GIẢM xuống còn 1,860 mm tại đỉnh cao nhất (Alpine Crest) — phá vỡ giả định "tăng liên tục tới tận đỉnh"! Chọn D.',
            'Bẫy True Data / Wrong Claim cực hiểm ở Hard M2: Cả A, B, C đều nêu SỐ LIỆU ĐÚNG 100% với biểu đồ, nhưng chúng ỦNG HỘ hoặc không đụng vào điểm sai cốt lõi (tăng liên tục tới đỉnh cao nhất). Chỉ D đánh trúng đoạn đi xuống giữa Mid-Slope và Alpine Crest!',
            [
                ('True Data / Wrong Claim', 'Số liệu đúng (1,860 → 340 mm), nhưng đây chính là phần giảm ở sườn khuất gió mà sinh viên ĐÃ dự đoán đúng, không hề bác bỏ giả định.'),
                ('True Data / Wrong Claim', 'Số liệu đúng (1,120 > 3×340), nhưng so sánh chân núi đón gió với bồn địa khuất gió không kiểm chứng được xu hướng tăng đến đỉnh.'),
                ('True Data / Supports Claim', 'Số liệu đúng (1,860 > 1,120), thậm chí còn dễ gây hiểu nhầm là ủng hộ giả định của sinh viên vì bỏ qua cột Mid-Slope (2,480 mm).'),
                ('Đáp án đúng', 'Chỉ rõ điểm đảo chiều phi tuyến (1,120 → 2,480 → giảm xuống 1,860 mm tại đỉnh cao nhất), bác bỏ trực diện giả định tăng đều tới đỉnh.'),
            ]
        ),
        q_item(
            'm3_m2h_q14', 14, 'Information and Ideas', 'Command of Evidence (Quantitative)', 'Elite (750+)',
            html_table(
                'Five-Year Agronomic Trial Results Across Four Temperate Grain Cropping Systems',
                ['Cropping System', 'Soil Organic Carbon Change (Mg C/ha)', 'Mean Annual Grain Yield (t/ha)', 'Annual Herbicide Applications'],
                [
                    ['Conventional Tilled Wheat', '−0.4', '6.0', '3.0'],
                    ['No-Till Annual Wheat', '+1.1', '5.6', '3.5'],
                    ['Legume-Cover + No-Till Wheat', '+2.8', '5.9', '1.5'],
                    ['Perennial Intermediate Wheatgrass', '+4.3', '3.1', '0.5'],
                ]
            ) + '<p>Agricultural policy analysts evaluating climate-smart grain transitions conclude that although perennial intermediate wheatgrass stores the largest total amount of soil carbon, pairing legume cover crops with no-till annual wheat offers the strongest near-term compromise—achieving substantial carbon gains while keeping grain yields above 5.8 t/ha and cutting herbicide applications in half relative to conventional tilled wheat.</p>',
            'Which choice best describes data from the table that support the analysts’ conclusion?',
            [
                'Whereas perennial wheatgrass gained 4.3 Mg C/ha at a yield of only 3.1 t/ha, legume-cover no-till wheat gained 2.8 Mg C/ha while maintaining a 5.9 t/ha yield and lowering herbicide applications from 3.0 to 1.5 per year.',
                'No-till annual wheat without cover crops gained 1.1 Mg C/ha and reduced annual herbicide applications from 3.5 to 3.0 while sustaining a 5.6 t/ha grain yield.',
                'Conventional tilled wheat delivered the highest mean grain yield (6.0 t/ha) and stored 0.4 Mg C/ha of additional soil carbon over the five-year trial.',
                'Legume-cover no-till wheat surpassed perennial intermediate wheatgrass in both soil organic carbon gain (+4.3 vs. +2.8 Mg C/ha) and annual grain yield (5.9 vs. 3.1 t/ha).'
            ],
            'A',
            'Kiểm tra từng tiêu chí của kết luận: (1) Perennial wheatgrass giữ carbon cao nhất (+4.3) nhưng sản lượng thấp (3.1 t/ha); (2) Legume-Cover + No-Till đạt tăng carbon đáng kể (+2.8 Mg C/ha), giữ sản lượng > 5.8 (5.9 t/ha), và giảm một nửa thuốc diệt cỏ so với cày xới truyền thống (3.0 → 1.5 lần/năm). Đối chiếu 4 đáp án: chỉ A khớp chính xác tuyệt đối mọi con số và mọi vế so sánh → Chọn A!',
            'Trong bảng đa cột (3 biến số), kiểm tra gắt dấu âm/dương (−0.4 là MẤT carbon, không phải lưu thêm — bẫy C!) và chiều tăng/giảm (No-Till tăng thuốc diệt cỏ từ 3.0 lên 3.5 — bẫy B!).',
            [
                ('Đáp án đúng', 'Khớp 100% cả 3 cột dữ liệu cho hai hệ thống then chốt và chứng minh trọn vẹn mọi tiêu chí trong kết luận của chuyên gia.'),
                ('False Data', 'Sai sự thật: No-Till Annual Wheat có mức dùng thuốc diệt cỏ TĂNG lên 3.5 (cao hơn mức 3.0 của Conventional Tilled), không phải giảm.'),
                ('Sign Misreading Trap', 'Bảng ghi −0.4 Mg C/ha (tức MẤT 0.4 Mg carbon), KHÔNG phải lưu trữ thêm 0.4 Mg carbon!'),
                ('Swapped Numbers', 'Đảo ngược số liệu carbon: Perennial wheatgrass mới là +4.3 Mg C/ha, cao hơn mức +2.8 của Legume-cover no-till wheat.'),
            ]
        ),

        # ------------------------------------------------------------------
        # Q15: Information and Ideas — Inferences
        # ------------------------------------------------------------------
        q_item(
            'm3_m2h_q15', 15, 'Information and Ideas', 'Inferences', 'Elite (750+)',
            '<p>Historians long attributed the fourth-century CE abandonment of Niya—a prosperous Silk Road oasis settlement on the southern rim of the Taklamakan Desert—to an abrupt climatic mega-drought that dried up the Niya River. However, recent radiocarbon dating of organic sediment layers inside the ancient riverbed indicates that steady glacial meltwater continued flowing past the town for more than a century after its final dated Kharoshthi wooden administrative tablets were sealed. Meanwhile, contemporaneous Chinese imperial chronicles document the sudden collapse of western frontier garrisons and repeated raids along the southern caravan corridor during the exact decades when Niya’s archives fall silent. Taken together, these findings most strongly suggest that ______</p>',
            STEM_INF,
            [
                'inhabitants of Niya intentionally diverted the Niya River away from their farmland to deter approaching raiders.',
                'radiocarbon dating of riverbed sediments is less reliable than analyzing wooden Kharoshthi tablets for determining fourth-century climate trends.',
                'the depopulation of Niya was driven primarily by regional political and security breakdowns rather than by an immediate failure of its local water supply.',
                'Silk Road trade across the entire Taklamakan Desert ceased permanently during the fourth century CE.'
            ],
            'C',
            'Tổng hợp 2 mảnh bằng chứng độc lập: (1) Lõi trầm tích lòng sông chứng minh nước băng tan vẫn chảy đều hơn 100 năm SAU KHI văn thư Niya chấm dứt → bác bỏ nguyên nhân "sông khô cạn tức thời vì đại hạn"; (2) Biên niên sử đương thời ghi nhận đồn trú biên giới sụp đổ đột ngột và các cuộc đột kích liên miên đúng vào những thập kỷ văn thư ngừng lại → Kết luận hợp lý nhất: việc bỏ hoang Niya chủ yếu do sụp đổ chính trị – an ninh khu vực chứ không phải cạn nguồn nước ngay lập tức → Chọn C.',
            'Công thức bài Inference tổng hợp 2 bằng chứng: Bằng chứng 1 (loại trừ nguyên nhân cũ: nước vẫn chảy >100 năm) + Bằng chứng 2 (chỉ ra nguyên nhân trùng khớp thời điểm: mất đồn trú + bị đột kích) → Chốt ngay kết luận bác bỏ X, ủng hộ Y!',
            [
                ('Unsupported Speculation', 'Không có chi tiết nào cho thấy dân Niya cố ý nắn dòng sông để cản quân đột kích.'),
                ('Out of Scope / Method Attack', 'Đoạn văn tin cậy và kết hợp cả hai nguồn dữ liệu chứ không nghi ngờ độ chính xác của phương pháp định tuổi carbon.'),
                ('Đáp án đúng', 'Kết nối chặt chẽ hai dòng bằng chứng địa chất và sử học: loại trừ cạn nước tức thời và quy nguyên nhân chính cho khủng hoảng an ninh – chính trị.'),
                ('Too Extreme', 'Bằng chứng chỉ nói về sự bỏ hoang thành ốc đảo Niya, không chứng minh toàn bộ thương mại Con đường Tơ lụa qua sa mạc chấm dứt vĩnh viễn.'),
            ]
        ),

        # ------------------------------------------------------------------
        # Q16-Q19: Standard English Conventions — Boundaries
        # ------------------------------------------------------------------
        q_item(
            'm3_m2h_q16', 16, 'Standard English Conventions', 'Boundaries', 'Hard',
            '<p>Unlike thick fiberglass insulation panels that absorb sound passively, acoustic metamaterials employ periodic arrays of coiled microscopic ______ far smaller than the wavelengths they manipulate—to steer low-frequency noise away from sensitive instruments.</p>',
            STEM_SEC,
            ['channels, structures', 'channels—structures', 'channels; structures', 'channels: structures'],
            'B',
            'Nhận diện cặp dấu bao cụm đồng vị ngữ xen giữa câu! Phía sau chỗ trống có dấu gạch ngang dài đóng lại cụm giải thích (`...wavelengths they manipulate—to steer`). Chủ ngữ + động từ + tân ngữ chính là `acoustic metamaterials employ periodic arrays of coiled microscopic channels to steer...`. Cụm `structures far smaller than the wavelengths they manipulate` là đồng vị ngữ xen giữa bổ nghĩa cho `channels` và ĐÃ đóng bằng dấu `—` → Bắt buộc mở bằng dấu `—` tương ứng → `channels—structures` (B)!',
            'Soi dấu câu phía SAU chỗ trống trước khi chọn: thấy `—to steer` là biết ngay cụm xen giữa cần một cặp gạch ngang song sinh `— ... —`!',
            [
                ('Mismatched Punctuation Pair', 'Mở bằng dấu phẩy (,) nhưng đóng bằng dấu gạch ngang (—) là lỗi lệch cặp dấu.'),
                ('Đáp án đúng', 'Khớp hoàn hảo cặp gạch ngang dài (`—structures ... manipulate—`) bao trọn cụm bổ nghĩa không thiết yếu.'),
                ('Illegal Semicolon', 'Không thể dùng dấu chấm phẩy để mở cụm đồng vị ngữ không phải mệnh đề độc lập và không khớp gạch ngang đóng.'),
                ('Illegal Colon Before Em-Dash', 'Dấu hai chấm không thể ghép cặp với dấu gạch ngang đóng ở giữa một mệnh đề chưa hoàn chỉnh.'),
            ]
        ),
        q_item(
            'm3_m2h_q17', 17, 'Standard English Conventions', 'Boundaries', 'Elite (750+)',
            '<p>Drawing on seasonal monsoon calendars compiled by generations of Indian Ocean pilots, Swahili dhow captains timed their northward departures from Zanzibar with exacting ______ Gujarati harbors weeks before violent southwest squalls closed the western Indian coast.</p>',
            STEM_SEC,
            ['precision; reaching', 'precision. Reaching', 'precision, reaching', 'precision, and reaching'],
            'C',
            'Kiểm tra cấu trúc IC + Cụm phân từ (Participial Modifier)! Vế trái là IC hoàn chỉnh ("Swahili dhow captains timed their northward departures from Zanzibar with exacting precision"). Vế phải bắt đầu bằng phân từ `reaching Gujarati harbors...` — lưu ý động từ `closed` nằm bên trong mệnh đề phụ `before...`, nên cả vế phải KHÔNG có động từ chính chia thì (không phải IC)! Vì vế phải là cụm phân từ bổ nghĩa kết quả, chỉ được nối bằng dấu PHẨY ĐƠN (`precision, reaching`) → Chọn C! Loại sạch `;` (A), `.` (B) và `, and` (D) vì đều tạo lỗi Fragment hoặc phá song song.',
            'Bẫy 750+ kinh điển: Đừng để động từ chia thì nằm trong mệnh đề phụ (`before ... closed`) đánh lừa bạn nghĩ vế sau là IC! Kiểm tra từ đầu vế sau (`reaching...`) — không có động từ chính → chỉ dùng dấu phẩy đơn!',
            [
                ('Semicolon + Fragment', 'Sau dấu chấm phẩy là cụm phân từ "reaching..." thiếu chủ ngữ và động từ chính → Fragment!'),
                ('Period + Fragment', 'Tách "Reaching Gujarati harbors..." thành câu độc lập tạo câu cụt (Fragment).'),
                ('Đáp án đúng', 'Dấu phẩy đơn nối mượt mệnh đề độc lập với cụm phân từ kết quả "reaching Gujarati harbors...".'),
                ('Faulty Parallelism / Fragment', '", and reaching" không có động từ nguyên mẫu hay phân từ song song phía trước để nối bằng "and" (động từ chính trước đó là quá khứ đơn "timed").'),
            ]
        ),
        q_item(
            'm3_m2h_q18', 18, 'Standard English Conventions', 'Boundaries', 'Hard',
            '<p>Isotopic tracing experiments conducted across old-growth Pacific Northwest forests demonstrate that the dense subterranean fungal hyphae connecting mature birch trees to shaded understory Douglas fir ______ measurable quantities of carbon during late autumn.</p>',
            STEM_SEC,
            ['saplings, transfer', 'saplings; transfer', 'saplings: transfer', 'saplings transfer'],
            'D',
            'Quy tắc ZERO dấu câu giữa Chủ ngữ và Động từ! Trong mệnh đề `that ...`, toàn bộ cụm danh từ dài `the dense subterranean fungal hyphae connecting mature birch trees to shaded understory Douglas fir saplings` là CHỦ NGỮ, và `transfer` là ĐỘNG TỪ CHÍNH của mệnh đề `that`. TUYỆT ĐỐI KHÔNG chèn dấu phẩy đơn, chấm phẩy hay hai chấm tách chủ ngữ khỏi động từ chính của nó → Chọn D (`saplings transfer`)!',
            'Bẫy "dấu phẩy lấy hơi" (Breath Comma): Dù chủ ngữ dài tới 15 từ, KHÔNG BAO GIỜ đặt một dấu phẩy đơn ngăn cách chủ ngữ với động từ chính!',
            [
                ('Subject-Verb Separation Comma', 'Chèn dấu phẩy đơn giữa chủ ngữ ("the dense subterranean fungal hyphae ... saplings") và động từ chính ("transfer").'),
                ('Illegal Semicolon Split', 'Dấu chấm phẩy cắt lìa chủ ngữ khỏi vị ngữ của nó.'),
                ('Illegal Colon Split', 'Dấu hai chấm chỉ đặt sau một IC hoàn chỉnh, không thể đứng giữa chủ ngữ và động từ.'),
                ('Đáp án đúng', 'Không chen bất kỳ dấu câu thừa nào giữa chủ ngữ và động từ chính "transfer".'),
            ]
        ),
        q_item(
            'm3_m2h_q19', 19, 'Standard English Conventions', 'Boundaries', 'Elite (750+)',
            '<p>Paleoclimatologists reconstructing ancient atmospheric methane rely on ice cores drilled at three landmark polar sites: Dome C, East Antarctica, where basal layers reach back roughly 800,000 ______ Greenland, prized for its high annual snowfall resolution; and Taylor Glacier, Victoria Land, where horizontal ice flow brings Pleistocene strata close to the surface.</p>',
            STEM_SEC,
            ['years; Summit Camp,', 'years, Summit Camp,', 'years; Summit Camp', 'years: Summit Camp,'],
            'A',
            'Quy tắc Super-Semicolon trong danh sách phức hợp! Danh sách 3 địa điểm mở đầu bằng dấu hai chấm (`sites:`) và mỗi mục đều chứa dấu phẩy bên trong (tên địa điểm + khu vực + mệnh đề mô tả). Cuối mục 2 ta thấy dấu hiệu quyết định: `; and Taylor Glacier, Victoria Land,`. Do đó giữa mục 1 và mục 2 BẮT BUỘC dùng Super-Semicolon (`;`), VÀ ngay sau `Summit Camp` phải có dấu phẩy (`,`) ngăn cách tên trạm với `Greenland` (tương xứng với `Dome C, East Antarctica,` và `Taylor Glacier, Victoria Land,`) → Chọn A (`years; Summit Camp,`)!',
            'Soi tính đối xứng của danh sách Super-Semicolon: thấy `; and [Địa điểm], [Vùng],` ở mục 3 → mục 2 PHẢI là `; [Địa điểm], [Vùng],`!',
            [
                ('Đáp án đúng', 'Dùng Super-Semicolon (;) ngăn mục 1 với mục 2 và đặt dấu phẩy chuẩn giữa "Summit Camp" với "Greenland".'),
                ('Weak Delimiter in Complex List', 'Dùng dấu phẩy thường giữa mục 1 và mục 2 làm rối ranh giới mục và phá vỡ cấu trúc song song với "; and" ở mục 3.'),
                ('Missing Geographic Comma', 'Thiếu dấu phẩy ngăn cách tên trạm "Summit Camp" với tên vùng địa lý "Greenland".'),
                ('Illegal Double Colon', 'Không dùng thêm dấu hai chấm bên trong một danh sách đã mở đầu bằng dấu hai chấm.'),
            ]
        ),

        # ------------------------------------------------------------------
        # Q20-Q22: Standard English Conventions — Form, Structure, and Sense
        # ------------------------------------------------------------------
        q_item(
            'm3_m2h_q20', 20, 'Standard English Conventions', 'Form, Structure, and Sense', 'Hard',
            '<p>Although neighboring cortical columns across the mammalian visual cortex receive overlapping signals from the retina, each individual column sharpens ______ firing selectivity to a single preferred edge orientation.</p>',
            STEM_SEC,
            ['their', 'it’s', 'its’', 'its'],
            'D',
            'Kiểm tra Đại từ Sở hữu & Hòa hợp Số ít/Số nhiều! Chủ ngữ của mệnh đề chính là `each individual column` — có từ `each` nên BẮT BUỘC LÀ SỐ ÍT (bất chấp các danh từ số nhiều `columns` và `signals` ở mệnh đề đầu). Tính từ sở hữu ngôi 3 số ít chỉ vật không có dấu nháy đơn là `its` → Chọn D!',
            'Từ khóa vàng: `each / every + danh từ số ít` LUÔN đi với đại từ số ít (`its`, KHÔNG phải `their`), và nhớ `it’s = it is`, còn `its’` KHÔNG tồn tại trong tiếng Anh!',
            [
                ('Pronoun Number Disagreement', '"their" là số nhiều — bị đánh lừa bởi "columns" và "signals" ở vế đầu, sai hòa hợp với "each individual column".'),
                ('Contraction Trap (it’s = it is)', '"it’s" là viết tắt của "it is", đặt vào sẽ thành "sharpens it is firing selectivity" — sai ngữ pháp.'),
                ('Nonexistent Form (its’)', 'Không có dạng "its’" trong tiếng Anh chuẩn.'),
                ('Đáp án đúng', 'Tính từ sở hữu số ít "its" khớp chính xác với tiền ngữ số ít "each individual column".'),
            ]
        ),
        q_item(
            'm3_m2h_q21', 21, 'Standard English Conventions', 'Form, Structure, and Sense', 'Elite (750+)',
            '<p>Among the linked short stories in Sherwood Anderson’s 1919 cycle <i>Winesburg, Ohio</i>—tales whose spare, colloquial cadences broke decisively with nineteenth-century melodrama—______ a persistent portrait of quiet alienation in rapidly industrializing Midwestern towns.</p>',
            STEM_SEC,
            ['emerges', 'emerge', 'emerging', 'having emerged'],
            'A',
            'Bẫy Kép 750+: Câu Đảo Ngữ (Inverted Subject) + Cụm Xen Giữa! Mở đầu bằng cụm giới từ chỉ nơi chốn `Among the linked short stories...` và cụm chen ngang `—tales whose... melodrama—`. Vì đầu câu không có chủ ngữ, CHỦ NGỮ THỰC SỰ nằm ngay SAU chỗ trống: `a persistent portrait` (SỐ ÍT)! Hơn nữa câu chưa có động từ chính nào, nên ta cần một động từ chia thì (finite verb) SỐ ÍT → `emerges` (A)!',
            'Khi câu mở đầu bằng giới từ (`Among...`, `Beneath...`, `Within...`), hãy lật câu về trật tự xuôi để tìm chủ ngữ thật đứng SAU chỗ trống (`a persistent portrait emerges among...`)!',
            [
                ('Đáp án đúng', 'Động từ chia thì số ít "emerges" hòa hợp hoàn hảo với chủ ngữ đảo ngữ số ít "a persistent portrait".'),
                ('Inverted Subject Disagreement', '"emerge" là số nhiều — bị lừa bởi các danh từ số nhiều đứng trước như "stories", "tales", "cadences".'),
                ('Sentence Fragment (-ing)', '"emerging" là hiện tại phân từ, làm cả câu thiếu động từ chính.'),
                ('Sentence Fragment (Participle)', '"having emerged" là phân từ hoàn thành, không thể làm động từ chính cho câu.'),
            ]
        ),
        q_item(
            'm3_m2h_q22', 22, 'Standard English Conventions', 'Form, Structure, and Sense', 'Hard',
            '<p>Because piezoelectric quartz crystals vibrate with far lower internal damping than metal tuning forks, the long-term frequency stability of a miniature quartz oscillator surpasses ______ by several orders of magnitude.</p>',
            STEM_SEC,
            [
                'a conventional mechanical escapement',
                'that of a conventional mechanical escapement',
                'those of a conventional mechanical escapement',
                'conventional mechanical escapements'
            ],
            'B',
            'Quy tắc So sánh Tương đồng (Logical Comparison)! Vế trước động từ `surpasses` so sánh ĐẶC TÍNH `the long-term frequency stability` (danh từ SỐ ÍT) của bộ dao động thạch anh. Do đó vế sau KHÔNG ĐƯỢC so sánh độ ổn định với bản thân một bộ hồi cơ khí (lỗi so táo với cam ở A và D), mà phải dùng đại từ thay thế số ít `that of` (= the long-term frequency stability of) → `that of a conventional mechanical escapement` (B)! Loại C vì `those of` dùng cho danh từ số nhiều.',
            'Hễ thấy các động từ/tính từ so sánh (`surpasses`, `exceeds`, `higher than`, `unlike`), kiểm tra ngay 2 vế xem có cùng cấp độ (stability ↔ that of ...) và khớp số ít/nhiều (`that of` vs. `those of`) không!',
            [
                ('Illogical Comparison', 'So sánh "độ ổn định tần số" (stability) trực tiếp với một thiết bị vật lý ("a mechanical escapement") — sai đối tượng so sánh.'),
                ('Đáp án đúng', 'Dùng đại từ thay thế số ít "that of" để so sánh chuẩn xác "stability of X" với "stability of Y".'),
                ('Number Mismatch (those of)', '"stability" là danh từ số ít không đếm được — dùng số nhiều "those of" là sai hòa hợp số.'),
                ('Illogical Comparison', 'So sánh "độ ổn định tần số" trực tiếp với các bộ hồi cơ khí số nhiều — sai đối tượng so sánh.'),
            ]
        ),

        # ------------------------------------------------------------------
        # Q23-Q25: Expression of Ideas — Transitions
        # ------------------------------------------------------------------
        q_item(
            'm3_m2h_q23', 23, 'Expression of Ideas', 'Transitions', 'Hard',
            '<p>Ectomycorrhizal fungi dramatically improve drought tolerance in young oak seedlings by extending hair-thin absorptive filaments into soil pores far too narrow for tree roots to enter. ______, sustaining these fungal partners requires host trees to export up to twenty percent of their photosynthesized sugars; during severe dry spells, however, the water-uptake advantage far outweighs that carbon cost.</p>',
            STEM_TRANS,
            ['Consequently', 'Similarly', 'Admittedly', 'For example'],
            'C',
            'Quan hệ Nhượng bộ tinh tế (Concession → Reaffirmation)! Câu 1 nêu lợi ích vượt trội của nấm cộng sinh. Câu 2 mở đầu bằng việc THỪA NHẬN một chi phí/hạn chế thực tế (cây chủ phải xuất tới 20% lượng đường quang hợp để nuôi nấm) trước khi dùng `; ... however,` khẳng định lợi ích vẫn vượt xa chi phí đó → Từ chuyển tiếp mở đầu vế thừa nhận chuẩn nhất là "Admittedly" (Phải thừa nhận rằng) → Chọn C!',
            'Cấu trúc Concession kinh điển ở Hard Module 2: `[Ưu điểm X]. Admittedly/Granted, [Nhược điểm/Chi phí]; however, [Ưu điểm vẫn thắng thế].`',
            [
                ('Wrong Relationship (Cause-Effect)', 'Việc cây phải xuất 20% đường không phải hệ quả tất yếu do việc tăng khả năng chịu hạn gây ra mà là cái giá phải trả đi kèm.'),
                ('Wrong Relationship (Similarity)', 'Similarly chỉ sự tương đồng cùng chiều — sai vì vế này nêu một chi phí bất lợi trái chiều với ưu điểm câu 1.'),
                ('Đáp án đúng', 'Admittedly mở đầu hoàn hảo cho vế nhượng bộ thừa nhận chi phí đường trước khi mệnh đề "however" khẳng định lại lợi thế ròng.'),
                ('Wrong Relationship (Example)', 'Chi phí xuất đường không phải là ví dụ minh họa cho việc sợi nấm luồn vào khe đất hẹp.'),
            ]
        ),
        q_item(
            'm3_m2h_q24', 24, 'Expression of Ideas', 'Transitions', 'Elite (750+)',
            '<p>Historians once assumed that ninth-century merchants traversing China’s Hexi Corridor operated almost exclusively as small family peddlers without formal financial institutions. ______, commercial contracts preserved in the Dunhuang library cave reveal organized trading associations pooling silver capital, recording standardized loan interest, and underwriting caravan losses.</p>',
            STEM_TRANS,
            ['Accordingly', 'Likewise', 'Meanwhile', 'In fact'],
            'D',
            'Câu 1 nêu giả định cũ đã lỗi thời ("Historians once assumed... small family peddlers without formal financial institutions"). Câu 2 đưa bằng chứng thực tế từ các hợp đồng lưu giữ tại hang Đôn Hoàng hoàn toàn lật ngược/đính chính giả định đó (tồn tại hiệp hội thương mại góp vốn bạc, tính lãi chuẩn hóa và bảo hiểm đoàn buôn) → "In fact" (Trên thực tế) → Chọn D! Loại ngay A (Nhân quả), B (Tương đồng), C (Đồng thời).',
            'Trên Digital SAT, "In fact" vừa dùng để nhấn mạnh sâu hơn, vừa cực kỳ chuẩn để ĐÍNH CHÍNH một giả định cũ sai lệch (`once assumed X... In fact, evidence shows Y`)!',
            [
                ('Wrong Relationship (Cause-Effect)', 'Hợp đồng tài chính phức tạp ở Đôn Hoàng không phải là hệ quả của giả định sai cũ của giới sử học.'),
                ('Opposite Relationship', 'Likewise biểu thị sự tương đồng — trái ngược hoàn toàn với mâu thuẫn giữa "tiểu thương gia đình" và "hiệp hội tài chính bài bản".'),
                ('Weak Temporal Link', 'Meanwhile chỉ hai sự việc diễn ra song song, đánh mất mũi nhọn phản bác giả định cũ.'),
                ('Đáp án đúng', 'In fact đưa sự thật tư liệu từ hang Đôn Hoàng lên để đính chính trực diện giả định cũ ở câu trước.'),
            ]
        ),
        q_item(
            'm3_m2h_q25', 25, 'Expression of Ideas', 'Transitions', 'Hard',
            '<p>In his 1916 collection <i>Chicago Poems</i>, Carl Sandburg deliberately set aside polished Victorian meter in favor of free-verse cadences modeled on stockyards, rail depots, and everyday Midwestern street speech. ______, he forged an unapologetically vernacular poetic idiom capable of capturing the tempo of an expanding industrial city.</p>',
            STEM_TRANS,
            ['In doing so', 'Nevertheless', 'Conversely', 'By contrast'],
            'A',
            'Câu 1 mô tả hành động sáng tạo có chủ đích của Carl Sandburg (gác lại niêm luật Victoria, chọn nhịp thơ tự do từ ngôn ngữ đời thường). Câu 2 nêu thành quả đạt được CHÍNH NHỜ HÀNH ĐỘNG ĐÓ (kiến tạo ngôn ngữ thơ bản địa phản ánh nhịp sống thành phố công nghiệp) → "In doing so" (Bằng việc làm như vậy) → Chọn A! Dùng mẹo loại nhóm 3–1: B, C, D đều thuộc nhóm Đối lập → loại sạch cả 3 trong 3 giây!',
            'Mẹo 3–1 bất bại cho Transitions: Khi 3 phương án đều mang nghĩa Đối lập (`Nevertheless`, `Conversely`, `By contrast`), phương án duy nhất chỉ hệ quả trực tiếp từ hành động (`In doing so`) là đáp án chắc chắn!',
            [
                ('Đáp án đúng', 'In doing so kết nối trực tiếp lựa chọn thi pháp ở câu 1 với thành quả nghệ thuật đạt được ngay nhờ lựa chọn đó ở câu 2.'),
                ('False Contrast', 'Nevertheless báo hiệu kết quả trái kỳ vọng — sai vì ngôn ngữ thơ bản địa chính là mục đích của lựa chọn nhịp điệu đời thường.'),
                ('False Contrast', 'Conversely dùng để đảo chiều đối nghịch.'),
                ('False Contrast', 'By contrast dùng để đối chiếu hai đối tượng trái ngược nhau.'),
            ]
        ),

        # ------------------------------------------------------------------
        # Q26-Q27: Expression of Ideas — Rhetorical Synthesis
        # ------------------------------------------------------------------
        q_item(
            'm3_m2h_q26', 26, 'Expression of Ideas', 'Rhetorical Synthesis', 'Hard',
            '''<p>While researching forest mycology, a student has taken the following notes:</p>
            <ul>
              <li>Both saprotrophic fungi and ectomycorrhizal fungi are vital decomposers and nutrient cyclers in temperate forest ecosystems.</li>
              <li>Saprotrophic fungi secrete powerful enzymes that break down dead wood and fallen leaves, obtaining carbon from decaying organic matter.</li>
              <li>Ectomycorrhizal fungi form living symbioses around tree root tips rather than feeding on dead timber.</li>
              <li>In these partnerships, ectomycorrhizal fungi deliver soil phosphorus and nitrogen to host trees in exchange for living plant sugars.</li>
            </ul>''',
            'The student wants to contrast the nutritional strategies of saprotrophic and ectomycorrhizal fungi while noting a broader ecological role they share. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
            [
                'Saprotrophic fungi obtain carbon by secreting enzymes that digest dead wood and fallen leaves, whereas ectomycorrhizal fungi wrap around living tree root tips to receive plant sugars.',
                'Although both saprotrophic and ectomycorrhizal fungi play essential roles in temperate forest nutrient cycling, saprotrophs derive carbon by breaking down dead plant matter, whereas ectomycorrhizal fungi obtain sugars symbiotically from living host trees.',
                'In temperate forests, ectomycorrhizal fungi exchange soil phosphorus and nitrogen for sugars from living tree roots instead of decomposing fallen timber.',
                'Both saprotrophic and ectomycorrhizal fungi are crucial to temperate forest ecosystems because both groups secrete enzymes that break down dead wood into plant sugars.'
            ],
            'B',
            'Goal gồm ĐÚNG 2 YÊU CẦU: [1] Đối chiếu chiến lược dinh dưỡng giữa 2 nhóm nấm (saprotrophs ăn gỗ/lá chết vs. ectomycorrhizal cộng sinh rễ cây sống) + [2] Nêu một vai trò sinh thái chung rộng hơn mà cả hai cùng chia sẻ (vital nutrient cyclers in temperate forest ecosystems). A thiếu vế chung [2]; C chỉ nói về một nhóm; D sai sự thật nghiêm trọng (Fact-Blend Trap: gộp nhầm nấm cộng sinh cũng tiết enzyme phân hủy gỗ chết!). Duy nhất B đáp ứng đầy đủ cả [1] và [2] với độ chính xác 100% → Chọn B!',
            'Với câu hỏi Rhetorical Synthesis 2 mục tiêu ("contrast X and Y WHILE noting a shared role"), gạch chân đủ 2 vế rồi loại ngay đáp án thiếu 1 vế (A) và đáp án gộp sai dữ kiện (D)!',
            [
                ('Incomplete Goal', 'Đối chiếu chính xác chiến lược dinh dưỡng của hai nhóm nấm nhưng bỏ sót hoàn toàn vai trò sinh thái chung mà đề bài yêu cầu.'),
                ('Đáp án đúng', 'Hội tụ trọn vẹn cả vai trò chung (essential roles in temperate forest nutrient cycling) lẫn phép đối chiếu chuẩn xác hai cơ chế dinh dưỡng.'),
                ('Incomplete Goal', 'Chỉ tập trung mô tả nấm ectomycorrhizal, thiếu sự đối chiếu đầy đủ và thiếu vai trò chung.'),
                ('Fact Distortion Trap', 'Sai sự thật với ghi chú: nấm ectomycorrhizal KHÔNG phân hủy gỗ chết mà cộng sinh với rễ cây sống.'),
            ]
        ),
        q_item(
            'm3_m2h_q27', 27, 'Expression of Ideas', 'Rhetorical Synthesis', 'Elite (750+)',
            '''<p>While researching acoustic physics, a student has taken the following notes:</p>
            <ul>
              <li>In 1787, German physicist Ernst Chladni dusted thin metal plates with fine sand and drew a violin bow across their edges to make them vibrate.</li>
              <li>The bouncing sand grains migrated away from violently vibrating zones and settled along motionless “nodal lines,” forming intricate geometric designs called Chladni figures.</li>
              <li>Different resonant frequencies produce distinct Chladni figures on the same plate.</li>
              <li>Today, master violin and guitar makers generate laser-illuminated Chladni patterns on unvarnished spruce soundboards to adjust wood thickness for balanced tonal resonance before assembly.</li>
            </ul>''',
            'The student wants to introduce Chladni figures to an audience unfamiliar with the term and explain how modern instrument makers apply them. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
            [
                'In 1787, Ernst Chladni discovered that bowing sand-dusted metal plates at different resonant frequencies generated distinct geometric patterns.',
                'Chladni figures—geometric patterns formed when sand accumulates along the most violently vibrating regions of a plate—are used today by luthiers to tune unvarnished spruce soundboards.',
                'Chladni figures, geometric patterns traced when sand settles along the motionless nodal lines of a vibrating plate, are used today by violin and guitar makers to evaluate and refine spruce soundboard resonance before final assembly.',
                'Before assembling a finished violin or guitar, modern instrument makers rely on laser-illuminated Chladni patterns to carve spruce plates to an even thickness.'
            ],
            'C',
            'BẪY HARD MODULE 2 KINH ĐIỂN (Audience-Unfamiliar + Fact-Swap)! Goal đòi hỏi 2 yếu tố: [1] Giới thiệu định nghĩa Chladni figures cho người chưa biết thuật ngữ này + [2] Giải thích ứng dụng hiện đại của nghệ nhân làm đàn. A thiếu ứng dụng hiện đại; D dùng luôn cụm "Chladni patterns" mà không định nghĩa cho người chưa biết! So sánh B và C: cả hai đều có định nghĩa + ứng dụng, NHƯNG B cài bẫy ĐẢO NGƯỢC SỰ THẬT ("accumulates along the most violently vibrating regions" — sai 100%, ghi chú nêu cát di chuyển TRÁNH XA vùng rung mạnh để tụ dọc đường nút BẤT ĐỘNG "motionless nodal lines"!). Chỉ có C đúng cả mục tiêu lẫn dữ kiện 100% → Chọn C!',
            'Khi thấy 2 đáp án đều thỏa mãn hình thức của Goal (như B và C ở đây), dừng lại 5 giây đối chiếu từng từ khóa khoa học với bullet notes — 90% một phương án chứa bẫy Fact Swap!',
            [
                ('Incomplete Goal', 'Chỉ kể lại thí nghiệm năm 1787 của Chladni, thiếu hoàn toàn ứng dụng hiện đại trong chế tác nhạc cụ.'),
                ('Fact Swap Trap!', 'Đánh tráo hoàn toàn hiện tượng vật lý: cát tụ dọc đường nút BẤT ĐỘNG ("motionless nodal lines"), không phải ở vùng rung mạnh nhất!'),
                ('Đáp án đúng', 'Vừa định nghĩa ngắn gọn, chính xác Chladni figures cho người mới, vừa nêu đúng ứng dụng điều chỉnh cộng hưởng mặt đàn gỗ vân sam trước khi lắp ráp.'),
                ('Unexplained Term (Audience Mismatch)', 'Nhắc "Chladni patterns" mà không hề giải thích khái niệm này là gì cho khán giả chưa quen thuộc.'),
            ]
        ),
    ]
