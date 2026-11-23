# -*- coding: utf-8 -*-
"""
Full-Length Adaptive Mock Test #6 — Module 2 HARD Route (27 Qs, Hard & Elite 750+, 32 min)
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
        # --- Q1-Q5: Craft and Structure — Words in Context (Elite 750+) ---
        q_item(
            'm6_m2h_q1', 1, 'Craft and Structure', 'Words in Context', 'Elite (750+)',
            '<p>Because room-temperature vacuum chambers constantly emit faint infrared photons that nudge trapped strontium atoms slightly off resonance, optical-clock physicists surround the atomic lattice with liquid-nitrogen-cooled copper shields; while these cryogenic barriers cannot eliminate ambient thermal radiation entirely, they drastically ______ its frequency-shifting interference.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            ['eradicate', 'exacerbate', 'precipitate', 'attenuate'],
            'D',
            'Degree-of-Fit 750+ Clue: vế nhượng bộ khẳng định rõ "cannot eliminate ambient thermal radiation entirely" (KHÔNG thể xóa bỏ hoàn toàn) → động từ cần điền chỉ có thể mang nghĩa LÀM SUY YẾU / GIẢM NHẸ MẠNH chứ không phải xóa sạch 100%! Do đó chọn "attenuate" (D), loại bẫy cường độ quá mạnh "eradicate" (A)!',
            'Mỗi khi vế trước nói "cannot eliminate entirely", loại ngay các từ cực đoan ("eradicate / obliterate / preclude") và chọn từ giảm mức độ ("attenuate / mitigate")!',
            [
                ('Degree Too Strong', 'eradicate = xóa sổ tận gốc 100% — mâu thuẫn trực tiếp với "cannot eliminate... entirely".'),
                ('Opposite Meaning', 'exacerbate = làm trầm trọng thêm — ngược hoàn toàn tác dụng của lớp chắn làm lạnh.'),
                ('Opposite Meaning', 'precipitate = châm ngòi/đẩy nhanh — sai hướng tác động.'),
                ('Đáp án đúng', 'attenuate = làm suy giảm đáng kể cường độ/ảnh hưởng — khớp hoàn hảo với mức giảm mạnh nhưng không bằng không.'),
            ]
        ),
        q_item(
            'm6_m2h_q2', 2, 'Craft and Structure', 'Words in Context', 'Elite (750+)',
            '<p>Because fourth-century Sogdian commercial ledgers routinely omitted explicit currency labels whenever caravan partners relied on unspoken local conventions, modern epigraphers initially found several surviving debt tallies ______: a single numerical line could plausibly be read either as an unpaid balance of silver drachms or as a shipment weight of raw silk.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            ['unimpeachable', 'equivocal', 'perfunctory', 'immutable'],
            'B',
            'Colon Restatement Clue: sau dấu hai chấm giải thích cực rõ "a single numerical line could plausibly be read EITHER as X OR as Y" (một dòng số có thể hiểu hợp lý theo HAI nghĩa khác hẳn nhau) → MẬP MỜ / ĐA NGHĨA KHÓ ĐỊNH ĐOẠT → "equivocal" (B)!',
            'Equivocal = open to more than one interpretation / ambiguous — nhận diện ngay khi câu giải thích đưa ra hai cách diễn giải song song ("either as X or as Y")!',
            [
                ('Opposite Meaning', 'unimpeachable = không thể chê trách/không chút nghi ngờ — ngược với tình trạng khó xác định nghĩa.'),
                ('Đáp án đúng', 'equivocal = mập mờ hai nghĩa, có thể diễn giải theo nhiều cách trái ngược nhau — khớp nguyên văn vế sau dấu hai chấm.'),
                ('Wrong Meaning', 'perfunctory = qua loa chiếu lệ — không phản ánh tính hai nghĩa của đơn vị tiền tệ bị lược bỏ.'),
                ('Wrong Meaning', 'immutable = bất biến không đổi — sai bối cảnh giải mã văn tự cổ.'),
            ]
        ),
        q_item(
            'm6_m2h_q3', 3, 'Craft and Structure', 'Words in Context', 'Elite (750+)',
            '<p>Early popular science books celebrated subterranean mycorrhizal networks as an altruistic "wood-wide web" through which mature trees generously nourish shaded seedlings; however, recent critical meta-analyses ______ that sweeping portrait, noting that field studies rarely prove transferred carbon meaningfully boosts seedling survival or originates from parental altruism rather than fungal self-interest.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            ['qualify', 'ratify', 'emulate', 'galvanize'],
            'A',
            'Secondary Academic Meaning 750+: đối lập với bức tranh tổng quát quá lý tưởng ("sweeping portrait") là các phân tích tổng hợp đưa ra giới hạn/dè dặt thực nghiệm → Nghĩa thứ cấp học thuật kinh điển của "qualify" (v) = modify / make less absolute / add reservations to (hạn định lại, tiết chế bớt một nhận định quá tuyệt đối) → Chọn A!',
            'Từ sát thủ 750+ trên Bluebook: động từ "qualify a claim/portrait" KHÔNG có nghĩa là "đủ tiêu chuẩn", mà nghĩa là "đặt giới hạn, làm bớt tính cực đoan/tuyệt đối của một nhận định"!',
            [
                ('Đáp án đúng', 'qualify (nghĩa học thuật: bổ sung điều kiện giới hạn, tiết chế nhận định khái quát quá mức) khớp 100% với phản biện thận trọng của các phân tích mới.'),
                ('Opposite Meaning', 'ratify = phê chuẩn/xác nhận chính thức — trái ngược sau "however".'),
                ('Wrong Meaning', 'emulate = bắt chước noi theo — vô nghĩa với chủ ngữ "meta-analyses".'),
                ('Wrong Direction', 'galvanize = kích động/thúc đẩy mạnh mẽ — ngược hướng phê phán thận trọng.'),
            ]
        ),
        q_item(
            'm6_m2h_q4', 4, 'Craft and Structure', 'Words in Context', 'Elite (750+)',
            '<p>Whereas midcentury modernist planners dismissed traditional mudbrick courtyard residences as archaic compromises dictated solely by technological poverty, contemporary bioclimatic simulations ______ that assumption, demonstrating that thick adobe envelopes paired with passive roof windcatchers outperform mechanically cooled concrete towers across extreme desert temperature swings.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            ['vindicate', 'sanction', 'confound', 'reiterate'],
            'C',
            'Contrast + Secondary Meaning 750+: "Whereas... dismissed... as archaic compromises" ↔ mô phỏng khí hậu chứng minh nhà đất nung vượt trội hơn cả tháp bê tông lắp điều hòa → LẬT NGƯỢC / BÁC BỎ HOÀN TOÀN giả định khinh miệt đó → Nghĩa học thuật của "confound" = prove wrong / overturn an expectation or assumption → Chọn C!',
            'Nhớ nghĩa học thuật của "confound an assumption/theory" = chứng minh giả định là sai lầm, đảo ngược hoàn toàn kỳ vọng (trái nghĩa với "vindicate")!',
            [
                ('Opposite Meaning', 'vindicate = chứng minh là đúng/minh oan — ngược 180 độ với vế "Whereas".'),
                ('Opposite Meaning', 'sanction = phê duyệt/cho phép — trái chiều phản chứng.'),
                ('Đáp án đúng', 'confound (nghĩa học thuật: bác bỏ/lật ngược một giả định) khớp tuyệt đối với bằng chứng mô phỏng vượt trội.'),
                ('Opposite Meaning', 'reiterate = lặp lại khẳng định cũ — trái hoàn toàn.'),
            ]
        ),
        q_item(
            'm6_m2h_q5', 5, 'Craft and Structure', 'Words in Context', 'Elite (750+)',
            '<p>By installing open-loop bank-card tap readers paired with automatic weekly fare capping across subway gates, urban rail agencies can ______ the expensive custom ticket-vending kiosks and single-use magnetic passes that historically discouraged occasional visitors from boarding public trains.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            ['perpetuate', 'obviate', 'engender', 'mandate'],
            'B',
            'Cause-Effect Clue 750+: thanh toán chạm thẻ ngân hàng trực tiếp kèm trần giá tự động giúp LOẠI BỎ NHU CẦU / LÀM TRỞ NÊN KHÔNG CÒN CẦN THIẾT các máy bán vé cồng kềnh và vé giấy từ tính cũ → "obviate" (B)!',
            'Thuộc lòng động từ học thuật 750+: "obviate" = render unnecessary / remove the need for (khiến thứ gì trở nên thừa thãi, không cần dùng nữa).',
            [
                ('Opposite Meaning', 'perpetuate = duy trì kéo dài mãi — trái với việc thay thế máy bán vé cũ.'),
                ('Đáp án đúng', 'obviate = làm trở nên không còn cần thiết — khớp chính xác tác dụng thay thế kiosk bán vé và thẻ từ dùng một lần.'),
                ('Opposite Meaning', 'engender = sản sinh/gây ra — ngược hoàn toàn.'),
                ('Opposite Meaning', 'mandate = bắt buộc áp dụng — trái ngược mục đích loại bỏ rào cản cũ.'),
            ]
        ),

        # --- Q6-Q7: Craft and Structure — Text Structure and Purpose ---
        q_item(
            'm6_m2h_q6', 6, 'Craft and Structure', 'Text Structure and Purpose', 'Elite (750+)',
            '<p>In 2017, geochemist Dr. Marie Jackson and her team analyzed drill cores extracted from 2,000-year-old Roman breakwaters at Portus Cosanus using synchrotron X-ray micro-diffraction. Rather than finding degraded cement binder eroded by centuries of salt exposure, the researchers observed dense arrays of platy aluminum-tobermorite crystals knitting fractured interfaces tightly together. <u>Because alkaline pore fluids continuously react with volcanic ash grains as seawater percolates through microscopic fissures, the breakwater’s mineral matrix does not merely endure marine weathering passively but progressively synthesizes new structural reinforcement over decades.</u> This geochemical feedback helps explain why ancient imperial harbors outlast modern steel-reinforced concrete piers.</p>',
            'Which choice best describes the function of the underlined sentence in the text as a whole?',
            [
                'It details the ongoing chemical mechanism by which seawater infiltration actively strengthens Roman marine concrete rather than simply being resisted by it.',
                'It argues that synchrotron X-ray micro-diffraction is unreliable when applied to porous volcanic rocks submerged in saltwater.',
                'It warns that modern steel-reinforced piers cannot withstand alkaline pore fluids for longer than a few decades.',
                'It contrasts the volcanic ash quarried near Portus Cosanus with limestone mortar excavated at inland Roman aqueducts.'
            ],
            'A',
            'Câu 2 nêu kết quả quan sát (tinh thể Al-tobermorite đan chặt vào khe nứt). Câu 3 gạch chân bắt đầu bằng "Because..." giải thích CƠ CHẾ HÓA HỌC LIÊN TỤC ("continuously react... does not merely endure passively but progressively synthesizes new structural reinforcement") giúp nước biển trở thành tác nhân CHỦ ĐỘNG GIA CỐ chứ không chỉ bị chống đỡ thụ động → Chọn A!',
            'Chú ý cấu trúc "not merely [passive resistance] but [active synthesis]" trong câu gạch chân — đáp án đúng bắt chuẩn sắc thái "actively strengthens rather than simply being resisted"!',
            [
                ('Đáp án đúng', 'Nắm trọn chức năng của câu gạch chân: làm rõ phản ứng địa hóa liên tục biến nước biển thành động lực chủ động tăng cường kết cấu.'),
                ('Contradiction', 'Kỹ thuật nhiễu xạ tia X synchrotron chính là công cụ đã phát hiện thành công các tinh thể đó, không bị chê kém tin cậy.'),
                ('Out of Scope / Distortion', 'Câu gạch chân giải thích cơ chế bê tông La Mã; câu cuối mới so sánh khái quát với cầu cảng thép hiện đại.'),
                ('Out of Scope', 'Không nhắc cầu dẫn nước La Mã nội địa hay so sánh hai nguồn đá vôi.'),
            ]
        ),
        q_item(
            'm6_m2h_q7', 7, 'Craft and Structure', 'Text Structure and Purpose', 'Elite (750+)',
            '<p><i>The following text is adapted from a fictional 1884 field journal by Victorian botanical illustrator Eleanor Vance, written during an expedition across the Atlas foothills.</i><br/>By ten o’clock the scarlet rock-cistus had already uncurled its papery petals to the dry wind, shivering so fiercely on its wiry stem that no two moments offered the same silhouette. Yet inside my tin sketching box, the watercolor study I completed at dawn lies flat and tranquil—every stamen arrested in crisp vermilion wash as though winter had already claimed the valley. I admire the clear taxonomy my brush has rescued for Kew’s cabinets, even as I suspect that in pinning the flower to permanence I have quietly left behind the very tremor that made it alive.</p>',
            'Which choice best states the main purpose of the text?',
            [
                'To criticize botanical museums at Kew for refusing to fund watercolor expeditions to North Africa.',
                'To describe the seasonal climatic shifts that cause desert rock-cistus plants to wither before noon.',
                'To prove that ink drawings capture plant movement more faithfully than translucent watercolor washes.',
                'To reflect on the bittersweet tension between preserving a living plant’s precise botanical form in art and losing its restless natural vitality.'
            ],
            'D',
            'Nhân vật đối chiếu bông hoa sống đang run rẩy mãnh liệt trong gió khô với bức tranh màu nước phẳng lặng bất động trong hộp vẽ. Câu cuối gói trọn tâm trạng giằng xé tinh tế: vừa tự hào vì cứu được chi tiết phân loại sắc nét cho phòng lưu trữ Kew ("admire the clear taxonomy..."), vừa băn khoăn vì khi cố định nó vào sự vĩnh cửu, mình đã lặng lẽ đánh rơi chính nhịp rung động làm nên sự sống ("pinning the flower to permanence... left behind the very tremor that made it alive") → Chọn D!',
            'Đọc câu kết đoạn nhật ký văn học — cấu trúc "I admire X, even as I suspect that... I have left behind Y" báo hiệu chính xác sắc thái "tension / ambivalence" (D)!',
            [
                ('Out of Scope', 'Không hề phê phán hay nhắc chuyện tài trợ của Kew.'),
                ('Fact Distortion', 'Hoa mở cánh run rẩy trong gió lúc 10 giờ sáng chứ không héo úa vì chuyển mùa.'),
                ('Out of Scope', 'Không so sánh tranh mực với tranh màu nước.'),
                ('Đáp án đúng', 'Bắt trọn sự giằng xé sâu sắc giữa giá trị lưu giữ phân loại chính xác và nỗi tiếc nuối khi làm mất sự sống động tự nhiên của loài hoa.'),
            ]
        ),

        # --- Q8: Craft and Structure — Cross-Text Connections ---
        q_item(
            'm6_m2h_q8', 8, 'Craft and Structure', 'Cross-Text Connections', 'Elite (750+)',
            '<p><b>Text 1</b><br/>Drawing on greenhouse carbon-isotope experiments in which tagged carbon moved from mature Douglas firs to nearby shaded seedlings linked by shared ectomycorrhizal fungi, forest ecologist Dr. Linnea Lindholm argues that older "mother trees" actively channel surplus carbohydrates to struggling offspring, thereby stabilizing multi-generational forest resilience.</p><p><b>Text 2</b><br/>Reviewing twenty-six field studies of mycorrhizal networks across boreal and temperate woodlands, evolutionary mycologist Dr. Henrik Solberg observes that isotopic carbon detected beneath recipient seedlings almost never exceeds one percent of a seedling’s annual growth budget and largely stays locked inside fungal root mantles rather than entering plant tissues. Solberg concludes that underground carbon movement is driven primarily by fungal networks reallocating resources to expand their own mycelial territory, not by adult trees intentionally subsidizing kin.</p>',
            'Based on the texts, how would Dr. Henrik Solberg (Text 2) most likely characterize Dr. Linnea Lindholm’s interpretation (Text 1)?',
            [
                'As flawed because ectomycorrhizal fungi are incapable of connecting the root systems of mature Douglas firs and nearby seedlings.',
                'As overly cautious because carbon transfer from mature trees typically supplies well over half of a shaded seedling’s annual energy needs.',
                'As overstating both the biological impact of transferred carbon on seedlings and the notion that mature trees—rather than self-serving fungi—direct the exchange.',
                'As outdated solely because isotope-labeling experiments cannot detect carbon inside subterranean fungal tissues.'
            ],
            'C',
            'Phân tích đối chiếu 2 điểm đòn đánh của Solberg (Text 2) nhắm vào Lindholm (Text 1): (1) Về QUY MÔ TÁC ĐỘNG: carbon phát hiện gần như không vượt quá 1% ngân sách tăng trưởng của cây non và chủ yếu nằm kẹt trong lớp vỏ nấm → Lindholm đã phóng đại tác động sinh học; (2) Về CHỦ THỂ ĐIỀU KHIỂN (agency): không phải cây mẹ vị tha nuôi con mà là NẤM tự phân bổ tài nguyên để mở rộng mạng sợi nấm của chính nó → Chọn C!',
            'Trong Cross-Text Hard M2, kiểm tra đủ cả 2 mũi phản biện của Text 2: (a) mức độ ảnh hưởng nhỏ hơn nhiều (<1% & kẹt trong vỏ nấm) + (b) đảo ngược chủ thể điều khiển (nấm vì lợi ích riêng, không phải cây mẹ)!',
            [
                ('Overstated Conflict', 'Solberg KHÔNG phủ nhận sự kết nối của mạng nấm; ông chỉ ra mục đích và tỷ lệ trao đổi khác với kết luận của Lindholm.'),
                ('Reversed Logic', 'Text 2 nói carbon truyền sang hầu như không quá 1%, ngược hoàn toàn với "well over half".'),
                ('Đáp án đúng', 'Khớp cả hai mũi phản biện cốt lõi của Solberg: phóng đại tác động sinh học lên cây non và gán nhầm quyền chủ động cho cây mẹ thay vì nấm.'),
                ('Contradiction', 'Chính phương pháp đồng vị đã giúp phát hiện carbon nằm lại trong lớp vỏ nấm — không hề nói phương pháp này không đo được.'),
            ]
        ),

        # --- Q9-Q10: Information and Ideas — Central Ideas and Details ---
        q_item(
            'm6_m2h_q9', 9, 'Information and Ideas', 'Central Ideas and Details', 'Elite (750+)',
            '<p><i>The following excerpt is from an original poem titled “Glass Plates at the Harvard Meridian.”</i></p><p style="margin-left:18px;font-style:italic;">Upstairs beneath the shuttered iron dome,<br/>The senior fellows steer the brass refractor’s eye;<br/>Down here, beside the gas-lamp’s amber hum,<br/>I lift four inches of emulsion-coated sky.<br/>No dome admits my skirts into the frost,<br/>Yet silver halides whisper what the lens conceals:<br/>Here hydrogen burns blue, there calcium is crossed,<br/>And silent stars confess their ages to my quill.<br/>Let others claim the vantage of the height—<br/>I hold ten thousand suns within this table’s light.</p>',
            'Which choice best states the main idea of the poem?',
            [
                'The speaker resents having to maintain fragile glass photographic plates because she believes photographic spectroscopy is inferior to direct visual observation.',
                'Although institutional barriers exclude the speaker from operating the observatory’s main telescope, she exercises deep scientific mastery by decoding the hidden composition of countless stars from photographic plates.',
                'Senior astronomers upstairs rely on the speaker to repair the observatory’s brass refractor whenever winter frost jams the iron dome.',
                'The speaker plans to leave the observatory in order to build a smaller private telescope illuminated by amber gas lamps.'
            ],
            'B',
            'Giải mã cấu trúc thơ: Khổ đầu nêu sự phân tầng không gian & giới tính tại đài thiên văn ("Upstairs... senior fellows steer the brass refractor" ↔ "No dome admits my skirts into the frost" — ám chỉ phụ nữ bị cấm lên vòm kính thiên văn chính). Từ chữ "Yet", giọng thơ chuyển sang khẳng định quyền năng trí tuệ sâu sắc: qua tấm kính ảnh bạc halide bên bàn đèn khí, bà giải mã những gì mắt thường qua ống kính không thấy được ("what the lens conceals" — phổ hydro, canxi, tuổi sao) và "nắm giữ một vạn mặt trời ngay trong ánh đèn bàn" → Chọn B!',
            'Nhận diện sự đảo chiều quyền lực trong thơ: bị gạt ra ngoài vòm kính chính ("No dome admits my skirts") NHƯNG lại nắm tri thức sâu hơn ống kính ("silver halides whisper what the lens conceals... hold ten thousand suns")!',
            [
                ('Contradiction', 'Nhân vật tự hào rằng tấm ảnh phổ tiết lộ điều ống kính che giấu ("whisper what the lens conceals"), không hề coi nó kém hơn.'),
                ('Đáp án đúng', 'Tóm gọn chính xác đối lập giữa rào cản thể chế và bản lĩnh khoa học sâu sắc của nhân vật khi giải mã phổ sao trên bản kính ảnh.'),
                ('Out of Scope / Literal', 'Không hề nhắc việc sửa chữa ống kính hay mái vòm bị kẹt băng.'),
                ('Out of Scope', 'Không có ý định rời đài thiên văn để tự xây kính riêng.'),
            ]
        ),
        q_item(
            'm6_m2h_q10', 10, 'Information and Ideas', 'Central Ideas and Details', 'Hard',
            '<p>Satellite radar interferometry allows geophysicists to map millimeter-scale ground swelling above active volcanic chambers, yet radar detects magma intrusion only after subterranean pressure physically lifts the Earth’s crust. Because optical lattice atomic clocks measure local gravitational potential directly via Einstein’s gravitational redshift, linking transportable optical clocks along buried fiber-optic cables offers volcanologists a complementary diagnostic: dense magma surging into deep rock cavities increases local gravitational pull and subtly slows an overhead clock’s tick rate even when overlying basalt remains rigid and shows zero measurable surface uplift.</p>',
            'According to the text, what distinct advantage do linked optical lattice atomic clocks offer over satellite radar interferometry when monitoring volcanic chambers?',
            [
                'They can register subsurface magma accumulation through shifts in local gravity even before the crust visibly swells at the surface.',
                'They eliminate the need for buried fiber-optic cables by transmitting atomic time signals directly to orbiting radar satellites.',
                'They prevent deep basalt layers from cracking under rising subterranean magma pressure.',
                'They measure ground uplift with greater precision only after a volcanic eruption has already breached the crust.'
            ],
            'A',
            'Câu hỏi Specific Detail nâng cao: Đối chiếu hạn chế của radar vệ tinh ("detects magma intrusion ONLY AFTER subterranean pressure physically lifts the Earth’s crust") với lợi thế của đồng hồ mạng quang học ("increases local gravitational pull and subtly slows an overhead clock’s tick rate EVEN WHEN overlying basalt remains rigid and shows zero measurable surface uplift") → Khớp 100% ở A!',
            'Bắt chính xác cặp tương phản thời điểm: Radar cần bề mặt phồng lên trước ("only after... lifts the crust") ↔ Đồng hồ quang học đo thẳng biến đổi trọng lực do khối magma ngay cả khi bề mặt chưa hề phồng ("zero measurable surface uplift")!',
            [
                ('Đáp án đúng', 'Paraphrase chặt chẽ lợi thế cốt lõi: phát hiện tích tụ magma qua biến thiên trọng lực cục bộ ngay trước khi vỏ Trái Đất phồng lên.'),
                ('Contradiction', 'Bài nói rõ các đồng hồ quang học được nối dọc theo cáp quang chôn ngầm ("linking... along buried fiber-optic cables"), không bỏ cáp quang.'),
                ('Absurd / Out of Scope', 'Đồng hồ chỉ đo đạc chứ không ngăn đá bazan nứt vỡ.'),
                ('Contradiction', 'Giá trị của đồng hồ nằm ở phát hiện SỚM trước khi bề mặt phồng lên, không phải sau khi núi lửa đã phun trào.'),
            ]
        ),

        # --- Q11-Q12: Information and Ideas — Command of Evidence (Textual) ---
        q_item(
            'm6_m2h_q11', 11, 'Information and Ideas', 'Command of Evidence (Textual)', 'Elite (750+)',
            '<p>Since the 1907 excavation of five fourth-century Sogdian letters inside a ruined frontier watchtower west of Dunhuang, historians have debated why correspondence addressed to Samarkand—over two thousand kilometers to the west—ended up buried in a Chinese garrison post. Some scholars suggested that the papers were discarded draft copies left behind by traveling scribes; however, Central Asian historian Dr. Farida Karimova contends that they constituted an active outgoing courier pouch hastily hidden when wartime upheaval severed the Silk Road west of Dunhuang.</p>',
            'Which finding, if true, would most directly support Dr. Farida Karimova’s contention over the rival explanation?',
            [
                'Microscopic fiber tests confirm that the Sogdian letters were fabricated from hemp and mulberry pulp consistent with fourth-century Chinese papermaking.',
                'Several place-names mentioned in the Sogdian letters also appear in later seventh-century Tang dynasty travelogues.',
                'Archaeologists uncovered bronze arrowheads and charred wooden beams in unrelated watchtowers along the southern edge of the Taklamakan Desert.',
                'Physical examination reveals that the letters were still folded inside their intact linen mailbag with unbroken personalized clay address seals, and their final lines report the sudden sacking of the imperial capital just days before frontier post stations were evacuated.'
            ],
            'D',
            'So sánh 2 giả thuyết đối đầu: Rival = bản nháp bỏ đi ("discarded draft copies"); Karimova = túi thư chính thức đang gửi đi ("active outgoing courier pouch") bị giấu vội vì biến loạn chiến tranh làm đứt đường Tây tiến! Để ủng hộ Karimova VÀ loại trừ "bản nháp bỏ đi", bằng chứng phải chứng minh: [1] Thư đã đóng gói hoàn chỉnh sẵn sàng gửi (còn nguyên túi vải lanh + dấu niêm phong đất sét ghi địa chỉ chưa vỡ → KHÔNG phải giấy nháp!) VÀ [2] Bối cảnh chiến tranh đột ngột ngay lúc trạm biên ải sơ tán → Chọn D!',
            'Với dạng bài phân định 2 giả thuyết đối đầu ("over the rival explanation"), bằng chứng chuẩn phải trực tiếp bác bỏ giả thuyết kia (dấu niêm phong nguyên vẹn ≠ bản nháp bỏ đi) đồng thời khớp giả thuyết mục tiêu (biến loạn chiến tranh ngay trước khi sơ tán)!',
            [
                ('Neutral / Consistent with Both', 'Chất liệu giấy gai–dâu tằm phù hợp với cả bản nháp lẫn túi thư chính thức.'),
                ('Irrelevant Detail', 'Địa danh xuất hiện lại thế kỷ thứ 7 không phân định được vì sao tập thư bị chôn ở tháp canh thế kỷ thứ 4.'),
                ('Weak / Unrelated Location', 'Đầu mũi tên ở các tháp canh không liên quan ở phía nam sa mạc không chứng minh tập thư Dunhuang là túi thư chính thức chứ không phải bản nháp.'),
                ('Đáp án đúng', 'Khớp song song 2 bằng chứng quyết định: túi thư vải lanh và dấu niêm phong địa chỉ còn nguyên vẹn (loại bản nháp) + nội dung báo tin kinh đô bị cướp phá ngay sát ngày sơ tán trạm biên ải.'),
            ]
        ),
        q_item(
            'm6_m2h_q12', 12, 'Information and Ideas', 'Command of Evidence (Textual)', 'Elite (750+)',
            '<p>In an essay on the 1974 novel <i>The Windcatcher’s Ledger</i>, a literary critic argues that although young desert architect Tariq begins his career viewing traditional earthen architecture through a lens of romantic nostalgia, he ultimately concludes that adapting vernacular cooling wisdom for modern cities requires rigorous physical engineering rather than decorative mimicry.</p>',
            'Which quotation from Tariq near the end of <i>The Windcatcher’s Ledger</i> most effectively illustrates the critic’s claim?',
            [
                '“Nothing in my university textbooks moved me as deeply as watching twilight settle over my grandmother’s lime-washed courtyard after an August dust storm.”',
                '“If city officials refuse to outlaw high-rise glass offices altogether, then every surviving historic adobe quarter ought to be fenced off as an untouched open-air museum.”',
                '“I once sketched old wind towers as if they were sentimental heirlooms, but pasting hollow fiberglass towers onto air-conditioned shopping malls betrays them; honoring those builders means calculating wall mass, pressure gradients, and nighttime airflow for today’s dense blocks.”',
                '“Modern structural concrete dries quickly enough to house fifty thousand newcomers before next winter, which no team of traditional mudbrick masons could match.”'
            ],
            'C',
            'Checklist 3 thành phần tinh vi trong Claim: [1] Ban đầu nhìn bằng lăng kính hoài niệm lãng mạn ("romantic nostalgia"); [2] Bác bỏ sự bắt chước trang trí bề ngoài ("rather than decorative mimicry"); [3] Đòi hỏi kỹ thuật vật lý nghiêm ngặt để thích ứng cho đô thị hiện đại ("rigorous physical engineering... for modern cities"). Duy nhất C đủ cả 3 lớp nghĩa: "once sketched... as sentimental heirlooms" + "pasting hollow fiberglass towers onto malls betrays them" + "calculating wall mass, pressure gradients, and nighttime airflow for today’s dense blocks" → Chọn C!',
            'Câu hỏi Literary Evidence 750+ thường chứa 3 điều kiện ngầm: Quá khứ (hoài niệm) → Bác bỏ lối sai (nhái trang trí) → Kết luận chuẩn (kỹ thuật vật lý cho hiện đại). Kiểm từng tick chọn C!',
            [
                ('Half-Match (Old View Only)', 'Chỉ thể hiện cảm xúc hoài niệm ban đầu, chưa có bước chuyển sang kỹ thuật thực dụng hiện đại.'),
                ('Wrong Conclusion', 'Đòi rào lại làm bảo tàng bất động trái ngược với mục tiêu thích ứng trí tuệ bản địa vào đô thị hiện đại.'),
                ('Đáp án đúng', 'Hội tụ trọn vẹn cả 3 yếu tố: thú nhận sự hoài niệm cũ, bác bỏ lối gắn tháp sợi thủy tinh trang trí rỗng, và nhấn mạnh tính toán khối nhiệt/áp suất cho đô thị dày đặc.'),
                ('Contradiction / Off-Point', 'Chỉ khen tốc độ xây bê tông mà không thể hiện việc ứng dụng kỹ thuật làm mát bản địa.'),
            ]
        ),

        # --- Q13-Q14: Information and Ideas — Command of Evidence (Quantitative) ---
        q_item(
            'm6_m2h_q13', 13, 'Information and Ideas', 'Command of Evidence (Quantitative)', 'Elite (750+)',
            svg_bar_chart(
                'Six-Month Ridership Retention (%) After Replacing Monthly Rail Passes by Fare Model',
                ['0%', '25%', '50%', '75%', '100%'],
                [('Flat Tap (No Cap)', 64, '64%'), ('Daily Cap Only', 76, '76%'), ('Weekly Cap', 89, '89%'), ('Weekly+Alerts', 94, '94%')],
                100
            ) + '<p>Behavioral transit economists studying four cities that phased out upfront paper monthly passes hypothesized that commuters experience severe "budget-uncertainty aversion" when paying per ride. Consequently, the researchers predicted that introducing a multi-day weekly fare cap would produce a far larger jump in rider retention over a daily cap alone than adding real-time smartphone savings alerts would add on top of a weekly cap.</p>',
            'Which choice most effectively uses data from the graph to support the researchers’ prediction?',
            [
                'Cities that adopted a weekly fare cap paired with real-time smartphone savings alerts recorded the highest six-month rider retention rate at 94%, whereas cities using uncapped flat tap fares retained only 64% of riders.',
                'Moving from a daily cap alone (76% retention) to a weekly fare cap (89% retention) raised rider retention by 13 percentage points, more than double the 5-percentage-point gain achieved by adding real-time savings alerts to the weekly cap (from 89% to 94%).',
                'Replacing uncapped flat tap fares (64% retention) with a daily cap alone (76% retention) increased six-month rider retention by exactly 12 percentage points.',
                'All three capped fare models retained at least three-quarters of former monthly pass holders six months after paper passes were phased out.'
            ],
            'B',
            'Khóa phép so sánh hai bước nhảy trong Prediction: Bước nhảy 1 (`Daily Cap Only → Weekly Cap`) PHẢI LỚN HƠN NHIỀU so với Bước nhảy 2 (`Weekly Cap → Weekly + Alerts`)! Tính chính xác từ biểu đồ: Bước nhảy 1 = `89% − 76% = +13 điểm %`; Bước nhảy 2 = `94% − 89% = +5 điểm %` (13 > gấp đôi 5!). A, C, D đều đọc ĐÚNG 100% số liệu trên biểu đồ nhưng đều là bẫy "True Data / Wrong Comparison" vì không so sánh hai khoảng chênh lệch 76→89 và 89→94! Duy nhất B trúng phóc → Chọn B!',
            'Trên Module 2 Hard, bẫy định lượng nguy hiểm nhất là cả 4 đáp án đều ĐÚNG SỐ LIỆU 100% — hãy viết nhanh công thức so sánh 2 hiệu số `(C − B) > (D − C)` trước khi chọn!',
            [
                ('True Data / Wrong Comparison', 'So sánh cực đại (94%) với cực tiểu (64%), hoàn toàn bỏ qua phép so sánh hai bước nhảy 76→89 vs 89→94.'),
                ('Đáp án đúng', 'Tính và đối chiếu trực tiếp hai mức tăng: +13 điểm % (76% → 89%) lớn hơn gấp đôi mức tăng +5 điểm % (89% → 94%).'),
                ('True Data / Wrong Comparison', 'Chỉ tính bước nhảy 64% → 76% (+12%), không phải hai bước nhảy mà giả thuyết dự đoán.'),
                ('Too Broad / Wrong Claim', 'Đúng số liệu (76%, 89%, 94% đều ≥ 75%) nhưng không kiểm chứng sự chênh lệch giữa hai mức tăng.'),
            ]
        ),
        q_item(
            'm6_m2h_q14', 14, 'Information and Ideas', 'Command of Evidence (Quantitative)', 'Elite (750+)',
            html_table(
                'Table 1. Performance of Four Experimental Marine Mortar Formulations After 180 Days in Artificial Seawater',
                ['Formulation', 'Quicklime Clast Size', 'Volcanic Ash Share', 'Microcrack Closure (180d)', 'Compressive Strength Change (28d → 180d)'],
                [
                    ['Cold-Mix Control', 'None', '35%', '12%', '−6%'],
                    ['Hot-Mix Low-Ash', '1–2 mm', '10%', '88%', '+3%'],
                    ['Hot-Mix Balanced', '1–2 mm', '35%', '94%', '+24%'],
                    ['Hot-Mix Coarse', '5–8 mm', '35%', '91%', '−11%'],
                ]
            ) + '<p>Reviewing preliminary crack-sealing trials, a coastal materials contractor claims that any hot-mixed marine mortar achieving more than 85 percent microcrack closure in seawater is guaranteed to increase its compressive strength by at least 15 percent between day 28 and day 180.</p>',
            'Which choice best describes data from the table that directly weaken the contractor’s claim?',
            [
                'Although both Hot-Mix Low-Ash (88% closure) and Hot-Mix Coarse (91% closure) surpassed 85% microcrack closure, the former gained only 3% in compressive strength while the latter actually lost 11%.',
                'Cold-Mix Control contained no quicklime clasts, sealed only 12% of its microcracks, and suffered a 6% reduction in compressive strength over the 180-day seawater immersion.',
                'Hot-Mix Balanced achieved the highest microcrack closure rate in the trial (94%) alongside a 24% increase in compressive strength.',
                'All three hot-mixed formulations sealed a dramatically higher percentage of microcracks than Cold-Mix Control did over 180 days.'
            ],
            'A',
            'Khóa mệnh đề điều kiện cần WEAKEN: BẤT KỲ vữa trộn nóng nào đạt `Crack Closure > 85%` ĐỀU ĐẢM BẢO `Strength Change ≥ +15%`! Quét bảng tìm các hàng thỏa điều kiện > 85%: (1) `Hot-Mix Low-Ash`: 88% (>85%) NHƯNG độ bền chỉ tăng +3% (<15%) ✗; (2) `Hot-Mix Balanced`: 94% và +24% ✓; (3) `Hot-Mix Coarse`: 91% (>85%) NHƯNG độ bền lại GIẢM −11% ✗! Hai phản ví dụ trực diện đập tan từ "guaranteed" hội tụ trọn vẹn ở A → Chọn A!',
            'Muốn bác bỏ quy luật "Nếu X > 85% thì chắc chắn Y ≥ +15%", lọc ngay các hàng thỏa `X > 85%` nhưng vi phạm `Y < +15%` (hàng Low-Ash và hàng Coarse)!',
            [
                ('Đáp án đúng', 'Chỉ ra cả hai phản ví dụ cùng vượt mốc 85% lấp khe nứt (88% và 91%) nhưng một mẫu chỉ tăng +3% và mẫu kia giảm tới −11% cường độ chịu nén.'),
                ('Irrelevant Row', 'Cold-Mix Control không phải vữa trộn nóng và chỉ lấp 12% (<85%), không vi phạm mệnh đề điều kiện của nhà thầu.'),
                ('Opposite Direction (Supports!)', 'Hot-Mix Balanced (94% và +24%) là hàng duy nhất ủng hộ tuyên bố của nhà thầu.'),
                ('True Data / Wrong Claim', 'Chỉ so sánh tỷ lệ lấp khe nứt, bỏ qua hoàn toàn cột biến thiên cường độ chịu nén.'),
            ]
        ),

        # --- Q15: Information and Ideas — Inferences ---
        q_item(
            'm6_m2h_q15', 15, 'Information and Ideas', 'Inferences', 'Elite (750+)',
            '<p>In open subtropical forests, the bioluminescent mushroom <i>Neonothopanus gardneri</i> relies on an internal circadian clock to extinguish its glow during daylight—when bright sun would make fungal light invisible to spore-carrying insects—and switch luminescence on strictly after dusk, thereby conserving metabolic energy. Surprisingly, however, a closely related bioluminescent strain isolated from a deep limestone cavern without sunlight glows continuously at steady brightness around the clock, even when researchers expose it to artificial twelve-hour light-dark cycles in the laboratory. Taken together, these findings most strongly suggest that ______</p>',
            'Which choice most logically completes the text?',
            [
                'surface-dwelling <i>Neonothopanus gardneri</i> mushrooms produce brighter luminescence during noon sunlight than at midnight.',
                'artificial twelve-hour light-dark cycles immediately destroy the luciferin enzymes required for fungal bioluminescence.',
                'deep limestone caverns contain significantly more nocturnal insect species than open subtropical forests do.',
                'in perpetually dark cave environments where daylight never masks fungal light or structures daily insect activity, maintaining circadian shutoff regulation offers little adaptive advantage over continuous glowing.'
            ],
            'D',
            'Tổng hợp 2 tiền đề theo quy tắc 1-Millimeter: (1) Ngoài rừng mở, nấm cần đồng hồ sinh học tắt sáng ban ngày để tiết kiệm năng lượng vì ban ngày ánh mặt trời làm ánh sáng nấm vô hình với côn trùng; (2) Trong hang đá vôi sâu vĩnh viễn không có mặt trời, chủng nấm họ hàng lại phát sáng liên tục 24/24 bất chấp đưa ra chu kỳ sáng-tối nhân tạo ⇒ Suy diễn tất yếu: Trong môi trường tối vĩnh viễn không có ánh sáng ban ngày che lấp ánh sáng nấm hay tạo nhịp ngày-đêm cho côn trùng, việc duy trì cơ chế đồng hồ sinh học bật-tắt không mang lại lợi thế chọn lọc đáng kể so với phát sáng liên tục (nên tính trạng điều tiết ngày-đêm bị tiêu biến/không được chọn lọc duy trì) → Chọn D!',
            'So sánh hai môi trường tiến hóa: Rừng mở (có mặt trời ban ngày → tốn công phát sáng vô ích → cần tắt ban ngày) ↔ Hang tối vĩnh viễn (không bao giờ có mặt trời → không có lợi thế chọn lọc cho nhịp tắt ban ngày)!',
            [
                ('Contradiction', 'Bài nói rõ nấm rừng mở TẮT ánh sáng vào ban ngày ("extinguish its glow during daylight").'),
                ('Contradiction', 'Chủng trong hang vẫn phát sáng ổn định liên tục ngay cả khi đặt dưới chu kỳ sáng–tối nhân tạo, không bị phá hủy enzyme.'),
                ('Out of Scope / Unwarranted Comparison', 'Bài không hề so sánh số lượng loài côn trùng giữa hang đá vôi và rừng cận nhiệt đới.'),
                ('Đáp án đúng', 'Kết nối chặt chẽ nguyên nhân tiến hóa của cơ chế tắt sáng ban ngày ở rừng mở với sự vắng mặt của áp lực chọn lọc ngày–đêm trong hang tối vĩnh viễn.'),
            ]
        ),

        # --- Q16-Q19: Standard English Conventions — Boundaries ---
        q_item(
            'm6_m2h_q16', 16, 'Standard English Conventions', 'Boundaries', 'Hard',
            '<p>A 2025 retrospective exhibition celebrating nineteenth-century women astronomers assembled rare artifacts from three historic archives: Margaret Huggins’s spectroscopic notebooks in Tulse Hill, ______ Annie Maunder’s solar-corona glass plates in Greenwich, England; and Williamina Fleming’s stellar classification ledgers in Cambridge, Massachusetts.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['London,', 'London:', 'London;', 'London'],
            'C',
            'Quy tắc Super-Commas (Chấm phẩy phân tách liệt kê phức): Các phần tử trong danh sách đều chứa dấu phẩy nội bộ (`Tulse Hill, London` / `Greenwich, England` / `Cambridge, Massachusetts`) và phần tử thứ hai đã đóng bằng dấu chấm phẩy (`England; and`) → Bắt buộc dùng dấu chấm phẩy đồng bộ sau `London;` để tách phần tử 1 và phần tử 2 → Chọn C!',
            'Nhìn ngay dấu câu kết thúc phần tử thứ hai trong chuỗi liệt kê (`England; and`) → phải khớp dấu chấm phẩy `London;` ở phần tử thứ nhất!',
            [
                ('Ambiguous List Comma', 'Dùng dấu phẩy thường gây lẫn lộn với dấu phẩy tách thành phố–khu vực và không đồng bộ với `England; and`.'),
                ('Double Colon Error', 'Đã có dấu hai chấm giới thiệu danh sách trước đó ("three historic archives:"), cấm chèn dấu hai chấm giữa các phần tử.'),
                ('Đáp án đúng', 'Dấu chấm phẩy (;) đóng vai trò super-comma phân tách sắc nét các cụm liệt kê chứa dấu phẩy nội bộ, khớp hoàn hảo với `England; and`.'),
                ('Missing Separator', 'Thiếu hoàn toàn dấu ngăn cách giữa mục 1 và mục 2.'),
            ]
        ),
        q_item(
            'm6_m2h_q17', 17, 'Standard English Conventions', 'Boundaries', 'Elite (750+)',
            '<p>Conventional microwave cesium clocks count roughly nine billion atomic oscillations per second; strontium optical lattice clocks, ______ tally visible-light oscillations nearly fifty thousand times faster, dramatically subdividing each second into finer measurable intervals.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['however,', '; however,', '. However,', 'however'],
            'A',
            'Bẫy 750+ Parenthetical `however`! Quan sát kỹ cấu trúc sau dấu chấm phẩy thứ nhất: Chủ ngữ là `strontium optical lattice clocks`, ngay sau đó là dấu phẩy mở (`,`), rồi tới `______`, rồi mới tới động từ chính `tally`! Chữ `however` đang đứng CHEN GIỮA Chủ ngữ và Động từ chính trong CÙNG MỘT MỆNH ĐỀ (parenthetical interrupter) — phía trước đã có `,` nên chỉ cần đóng bằng `however,` (A)! Nếu chọn B (`; however,`) hoặc C (`. However,`), cụm `strontium optical lattice clocks` bị cắt cụt không có động từ thành Fragment!',
            'BẪY KINH ĐIỂN 750+: Kiểm tra xem phía trái `however` đã là IC hoàn chỉnh chưa! Ở đây trước `however` chỉ mới có mỗi Chủ ngữ `strontium optical lattice clocks` (CHƯA có động từ!) → CẤM dùng `;` hay `.` → dùng cặp phẩy `, however,`!',
            [
                ('Đáp án đúng', 'Đóng đúng cặp phẩy xen giữa (`, however,`) tách trạng từ liên kết nằm giữa Chủ ngữ và Động từ chính "tally".'),
                ('Semicolon Fragment Trap', 'Đặt chấm phẩy ngay sau chủ ngữ "strontium optical lattice clocks" tạo mảnh câu cụt không động từ!'),
                ('Period Fragment Trap', 'Đặt dấu chấm sau chủ ngữ cũng biến "strontium optical lattice clocks" thành Sentence Fragment.'),
                ('Unpaired Comma', 'Đã mở bằng dấu phẩy trước `however` thì bắt buộc phải đóng bằng dấu phẩy sau `however`.'),
            ]
        ),
        q_item(
            'm6_m2h_q18', 18, 'Standard English Conventions', 'Boundaries', 'Elite (750+)',
            '<p>Only after behavioral economists audited three million smartcard tap logs did transit planners uncover an unexpected transfer ______ commuters switched smoothly between intersecting subway lines when platforms stood across the same concourse, yet abandoned trips sharply whenever transfers required riding even a single escalator.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['pattern,', 'pattern', 'pattern, that', 'pattern:'],
            'D',
            'Vế trái ("Only after behavioral economists audited... did transit planners uncover an unexpected transfer pattern") là 1 IC hoàn chỉnh (có đảo ngữ chuẩn sau `Only after`). Vế phải ("commuters switched smoothly...") là 1 IC hoàn chỉnh giải thích chính xác "pattern" đó là gì! Giữa IC giới thiệu và IC giải thích → chọn dấu hai chấm (`pattern:`) = D! Loại A (Comma Splice), B (Run-on), C (dư dấu phẩy và sai cấu trúc trước mệnh đề giải thích).',
            'Sau một IC hoàn chỉnh kết thúc bằng danh từ khái quát ("an unexpected transfer pattern") và theo sau là lời giải thích cụ thể → chọn dấu hai chấm (`:`)!',
            [
                ('Comma Splice', 'Một dấu phẩy không thể nối hai mệnh đề độc lập IC + IC.'),
                ('Run-On Sentence', 'Không có dấu câu phân tách hai mệnh đề độc lập.'),
                ('Syntax / Punctuation Error', 'Không đặt `, that` để nối mệnh đề giải thích sau danh từ "pattern".'),
                ('Đáp án đúng', 'Dấu hai chấm (:) sau IC giới thiệu chính xác mệnh đề giải thích cụ thể cho "an unexpected transfer pattern".'),
            ]
        ),
        q_item(
            'm6_m2h_q19', 19, 'Standard English Conventions', 'Boundaries', 'Elite (750+)',
            '<p>Drawing on archival oil panels preserved at Kew Gardens, art conservator Dr. Hannah Kowalski showed how Victorian illustrator Marianne North layered opaque zinc white beneath translucent botanical ______ a technique enabling her paintings to evoke dew-slicked orchid petals under shifting tropical light.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['glazes; a technique', 'glazes, a technique', 'glazes. A technique', 'glazes: and a technique'],
            'B',
            'Cấu trúc Summative Appositive (750+ Boundaries): Phần sau chỗ trống là `"a technique enabling her paintings to evoke..."` — đây là Cụm danh từ đồng vị có phân từ V-ing (`enabling`), KHÔNG CÓ ĐỘNG TỪ CHIA THÌ (NOT an IC!). Do đó CẤM dùng dấu chấm phẩy (A) và dấu chấm (C) vì tạo Sentence Fragment; D thừa `and` sau dấu hai chấm. Duy nhất B (`glazes, a technique`) dùng dấu phẩy nối cụm đồng vị tóm lược vào cuối IC một cách chuẩn mực!',
            'Kiểm tra nhanh vế sau: `"a technique enabling..."` có động từ chia thì không? KHÔNG (`enabling` là V-ing)! ⇒ Loại ngay `;` và `.`, chốt dấu phẩy `, a technique`!',
            [
                ('Semicolon + Fragment', 'Vế sau chỉ là cụm danh từ + phân từ ("a technique enabling..."), không phải IC → cấm chấm phẩy.'),
                ('Đáp án đúng', 'Dấu phẩy nối chuẩn xác cụm đồng vị tóm lược ("a technique enabling...") bổ nghĩa cho kỹ thuật sơn lớp ở vế trước.'),
                ('Period + Fragment', 'Tách cụm danh từ không động từ chia thì thành câu riêng tạo Fragment.'),
                ('Malformed Colon', 'Không dùng dấu hai chấm rồi nối thêm liên từ "and" trước cụm đồng vị.'),
            ]
        ),

        # --- Q20-Q22: Standard English Conventions — Form, Structure, and Sense ---
        q_item(
            'm6_m2h_q20', 20, 'Standard English Conventions', 'Form, Structure, and Sense', 'Hard',
            '<p>Embedded throughout the porous volcanic mortar of ancient Roman harbor piers ______ thousands of millimeter-scale quicklime clasts that react with infiltrating seawater to seal structural microcracks.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['lies', 'has lain', 'lie', 'lying'],
            'C',
            'Đảo ngữ Chủ – Vị (Inverted Subject-Verb Agreement — 750+ FSS)! Cụm mở đầu `Embedded throughout the porous volcanic mortar of ancient Roman harbor piers` là cụm phân từ–giới từ chỉ vị trí, KHÔNG phải chủ ngữ! Chủ ngữ thật đứng SAU động từ: `thousands of millimeter-scale quicklime clasts` (SỐ NHIỀU!). Câu chưa có động từ chia thì (loại D `lying`) → chọn động từ SỐ NHIỀU `lie` (C)!',
            'Gặp câu mở đầu bằng cụm giới từ/phân từ vị trí (`Embedded throughout...` / `Beneath...`) → tìm CHỦ NGỮ THẬT ở phía sau chỗ trống (`thousands of... clasts` = số nhiều → `lie`)!',
            [
                ('Inverted Subject-Verb Mismatch', 'lies là số ít — bị lừa bởi danh từ "mortar" đứng trước chỗ trống.'),
                ('Inverted Subject-Verb Mismatch', 'has lain là số ít — không khớp chủ ngữ số nhiều "thousands of... clasts".'),
                ('Đáp án đúng', 'lie (hiện tại đơn, số nhiều) khớp chuẩn xác với chủ ngữ đảo sau động từ "thousands of millimeter-scale quicklime clasts".'),
                ('Non-Finite Fragment', 'lying là V-ing khiến câu hoàn toàn mất động từ chính.'),
            ]
        ),
        q_item(
            'm6_m2h_q21', 21, 'Standard English Conventions', 'Form, Structure, and Sense', 'Elite (750+)',
            '<p>Celebrated by twentieth-century astrophysicists for classifying more than ten thousand faint stellar spectra with remarkable consistency, ______</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            [
                'Williamina Fleming transformed Harvard Observatory’s glass-plate archive into a foundation of modern stellar spectroscopy.',
                'Williamina Fleming’s meticulous photographic catalogs transformed Harvard Observatory’s glass-plate archive into a foundation of modern stellar spectroscopy.',
                'Harvard Observatory’s glass-plate archive was transformed into a foundation of modern stellar spectroscopy by Williamina Fleming.',
                'modern stellar spectroscopy gained an indispensable foundation through Williamina Fleming’s meticulous photographic catalogs.'
            ],
            'A',
            'Bẫy 750+ Possessive Dangling Modifier! Cụm mở đầu `Celebrated... for classifying more than ten thousand faint stellar spectra` mô tả CON NGƯỜI trực tiếp thực hiện hành động phân loại (`Williamina Fleming`)! Cảnh giác bẫy B cực độc: chủ ngữ của B là `catalogs` (trong cụm sở hữu `Williamina Fleming’s... catalogs`), KHÔNG phải bản thân bà Fleming! C đặt `archive` và D đặt `spectroscopy` làm chủ ngữ — đều sai! Duy nhất A đặt trực tiếp `Williamina Fleming` làm chủ ngữ ngay sau dấu phẩy!',
            'Cảnh giác bẫy sở hữu kinh điển trên Hard M2: `Name’s + Noun` thì CHỦ NGỮ là `Noun` chứ không phải `Name`! Phải chọn câu có tên người không có `’s` đứng ngay sau dấu phẩy!',
            [
                ('Đáp án đúng', 'Chủ ngữ "Williamina Fleming" đứng trực tiếp sau dấu phẩy, khớp 100% với chủ thể được ca ngợi vì đã phân loại hơn một vạn phổ sao.'),
                ('Possessive Dangling Modifier', 'Chủ ngữ thật của câu B là "catalogs" (danh mục), không phải nhà thiên văn trực tiếp phân loại phổ sao.'),
                ('Dangling Modifier', 'Kho lưu trữ bản kính ảnh không phải là người thực hiện việc phân loại phổ sao.'),
                ('Dangling Modifier', 'Ngành quang phổ học sao hiện đại không thể tự mình phân loại hơn một vạn phổ sao.'),
            ]
        ),
        q_item(
            'm6_m2h_q22', 22, 'Standard English Conventions', 'Form, Structure, and Sense', 'Elite (750+)',
            '<p>Excavated from a dry watchtower west of Dunhuang in 1907, five fragile fourth-century rag-paper manuscripts preserve ______ accounts of silver debts, musk shipments, and frontier raids along the Silk Road.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['exiled merchant’s', 'exiled merchants', 'exiled merchants’s', 'exiled merchants’'],
            'D',
            'Kiểm tra Sở hữu cách danh từ số nhiều (Plural Possessive): Danh từ `accounts` (những ghi chép) thuộc sở hữu của các thương nhân lưu vong → bắt buộc có dấu sở hữu cách (loại B `exiled merchants`). Loại A (`exiled merchant’s`) vì danh từ đếm được số ít `merchant` KHÔNG được đứng trần không có mạo từ (`an`) phía trước! Loại C (`merchants’s`) vì danh từ số nhiều đuôi `-s` chỉ thêm dấu nháy đơn ở cuối → Chọn D (`exiled merchants’`)!',
            'Mẹo kiểm tra Sở hữu cách số ít vs. số nhiều: Không có mạo từ `a/an/the` phía trước danh từ đếm được → BẮT BUỘC dùng số nhiều sở hữu `s’` (`exiled merchants’`)!',
            [
                ('Missing Determiner / Number Trap', 'Danh từ số ít đếm được "exiled merchant’s" sai ngữ pháp khi thiếu mạo từ "an" phía trước.'),
                ('Missing Possessive', 'Thiếu dấu sở hữu cách giữa danh từ chỉ người sở hữu ("merchants") và "accounts".'),
                ('Nonstandard Apostrophe', 'Danh từ số nhiều tận cùng bằng -s chỉ thêm dấu nháy đơn (merchants’), không viết merchants’s.'),
                ('Đáp án đúng', 'Sở hữu cách số nhiều chuẩn mực "exiled merchants’ accounts" (những ghi chép của các thương nhân lưu vong).'),
            ]
        ),

        # --- Q23-Q25: Expression of Ideas — Transitions ---
        q_item(
            'm6_m2h_q23', 23, 'Expression of Ideas', 'Transitions', 'Elite (750+)',
            '<p>Laboratory strontium optical lattice clocks now operate with such astonishing precision that they would neither gain nor lose a single second over fifteen billion years. ______, deploying these clocks for continuous international timekeeping remains technically daunting because subtle blackbody radiation emitted by surrounding chamber walls steadily perturbs atomic resonance frequencies.</p>',
            'Which choice completes the text with the most logical transition?',
            ['Accordingly', 'Specifically', 'Still', 'Moreover'],
            'C',
            'Câu 1 khẳng định độ chính xác kinh ngạc trong phòng thí nghiệm (15 tỷ năm không lệch 1 giây). Câu 2 chỉ ra thực tế TRÁI KỲ VỌNG ("deploying... remains technically daunting" — triển khai liên tục vẫn cực kỳ gian nan do nhiễu bức xạ vật đen) → Quan hệ Nhượng bộ / Đối lập kỳ vọng → "Still" (= Nevertheless / Even so) → Chọn C!',
            'Câu 1 khen ưu điểm tuyệt đỉnh, câu 2 nêu rào cản kỹ thuật dai dẳng → chọn từ nối tương phản/nhượng bộ ("Still / Nevertheless / However")!',
            [
                ('Wrong Relationship (Cause-Effect)', 'Độ chính xác cao không phải nguyên nhân gây ra rào cản kỹ thuật từ bức xạ vật đen.'),
                ('Wrong Relationship (Specification)', 'Câu 2 nêu trở ngại trái chiều chứ không cụ thể hóa độ chính xác 15 tỷ năm.'),
                ('Đáp án đúng', 'Still (= Nevertheless) chuyển mạch sắc nét từ thành tựu chính xác phi thường sang khó khăn kỹ thuật vẫn tồn tại.'),
                ('Wrong Relationship (Addition)', 'Moreover dùng để thêm một ưu điểm cùng chiều, sai với cụm "remains technically daunting".'),
            ]
        ),
        q_item(
            'm6_m2h_q24', 24, 'Expression of Ideas', 'Transitions', 'Elite (750+)',
            '<p>Field mycologists emphasize that underground carbon exchange through shared ectomycorrhizal fungi rarely resembles unconditional charity among neighboring trees. ______, isotopic tracing demonstrates that fungi retain roughly eighty percent of received carbon within their own subterranean filaments, transferring mineral phosphorus mainly to host roots that deliver the highest sugar return.</p>',
            'Which choice completes the text with the most logical transition?',
            ['Nonetheless', 'Specifically', 'Similarly', 'Conversely'],
            'B',
            'Câu 1 nêu nhận định tổng quát (trao đổi carbon qua mạng nấm không giống lòng vị tha vô điều kiện). Câu 2 đi thẳng vào BẰNG CHỨNG CỤ THỂ HÓA CHI TIẾT con số và cơ chế ("retain roughly eighty percent... transferring phosphorus mainly to host roots that deliver the highest sugar return") → Quan hệ Cụ thể hóa / Minh chứng chi tiết → "Specifically" (B)!',
            'Từ nhận định tổng quát (câu 1) sang dữ liệu/cơ chế thực nghiệm cụ thể chứng minh chính nhận định đó (câu 2) → chọn "Specifically"!',
            [
                ('False Contrast', 'Hai câu hoàn toàn cùng chiều chứng minh nấm hành xử theo cơ chế có đi có lại chứ không vị tha.'),
                ('Đáp án đúng', 'Specifically giới thiệu chuẩn xác số liệu 80% và cơ chế trao đổi đường–phốt pho làm rõ nhận định khái quát ở câu 1.'),
                ('Wrong Relationship (Comparison)', 'Câu 2 đào sâu chính hiện tượng câu 1 chứ không so sánh với một đối tượng thứ hai tương tự.'),
                ('False Contrast', 'Conversely dùng để lật ngược sang chiều trái ngược, sai vì câu 2 ủng hộ trực tiếp câu 1.'),
            ]
        ),
        q_item(
            'm6_m2h_q25', 25, 'Expression of Ideas', 'Transitions', 'Elite (750+)',
            '<p>Far from representing makeshift shelters born of material scarcity, historic Iranian windcatcher houses embody remarkably sophisticated aerodynamic design. ______, modern computational fluid-dynamics simulations confirm that multi-directional roof towers generate steady negative-pressure suction capable of cooling interior chambers by more than eight degrees Celsius even on nearly calm summer afternoons.</p>',
            'Which choice completes the text with the most logical transition?',
            ['Indeed', 'Even so', 'Meanwhile', 'By contrast'],
            'A',
            'Câu 1 khẳng định nhà tháp đón gió Iran chứa đựng thiết kế khí động học cực kỳ tinh vi. Câu 2 CỦNG CỐ MẠNH HƠN NỮA ("confirm... cooling by more than eight degrees Celsius even on nearly calm afternoons") bằng mô phỏng động lực học chất lỏng hiện đại → Quan hệ Khẳng định củng cố / Nhấn mạnh tăng tiến → "Indeed" (A)!',
            'Gặp câu 2 củng cố và xác thực mạnh mẽ nhận định đánh giá ở câu 1 ("confirm... even on nearly calm afternoons") → chốt "Indeed / In fact"!',
            [
                ('Đáp án đúng', 'Indeed củng cố và tăng sức nặng trực tiếp cho khẳng định về trình độ khí động học tinh vi ở câu 1.'),
                ('False Contrast', 'Even so (= Nevertheless) chỉ sự trái kỳ vọng — sai vì hai câu hoàn toàn củng cố nhau.'),
                ('Wrong Relationship (Time/Parallel)', 'Meanwhile chỉ hai sự kiện diễn ra đồng thời tách biệt.'),
                ('False Contrast', 'By contrast dùng cho hai đối tượng đối lập, không hợp mạch khẳng định liên hoàn.'),
            ]
        ),

        # --- Q26-Q27: Expression of Ideas — Rhetorical Synthesis ---
        q_item(
            'm6_m2h_q26', 26, 'Expression of Ideas', 'Rhetorical Synthesis', 'Elite (750+)',
            '''<p>While researching urban transit economics, a student has taken the following notes:</p>
            <ul>
              <li>In metropolitan commuter rail networks, riders often must switch trains mid-journey to reach destinations off their home line.</li>
              <li>Transport economists use the term “transfer penalty” to describe the extra reluctance commuters feel toward trips requiring a train change.</li>
              <li>Field surveys show commuters perceive a five-minute platform transfer as roughly equivalent to twelve to fifteen minutes of continuous onboard riding.</li>
              <li>This psychological resistance persists even when total door-to-door travel time is shorter on the transfer route than on a slow direct bus.</li>
            </ul>''',
            'The student wants to introduce the concept of the “transfer penalty” to an audience already familiar with urban commuter rail networks, emphasizing its psychological rather than purely time-based impact. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
            [
                'Metropolitan commuter rail networks frequently require riders to switch trains mid-journey whenever their destination lies off their starting line.',
                'Transport economists have found that slow direct buses can sometimes take longer door-to-door than urban rail trips requiring a mid-journey transfer.',
                'A five-minute platform transfer on an urban rail line adds five minutes of waiting time between two consecutive train rides.',
                'Known to transport economists as the “transfer penalty,” commuters’ extra reluctance to change trains is largely psychological: riders perceive a five-minute transfer as equivalent to twelve to fifteen minutes onboard, deterring them even when transferring yields a faster overall trip.'
            ],
            'D',
            'Goal-First SOP 750+: Kiểm tra đủ 3 yêu cầu trong Goal: [1] Giới thiệu khái niệm “transfer penalty” (A, B, C đều KHÔNG hề gọi tên thuật ngữ “transfer penalty”!); [2] Dành cho độc giả đã quen mạng tàu đô thị (không cần dài dòng định nghĩa lại tàu đô thị là gì); [3] Nhấn mạnh tác động TÂM LÝ hơn là thời gian thuần túy ("perceived 5 min as 12–15 min... even when transferring yields a faster overall trip"). Duy nhất D đánh trúng cả 3 yêu cầu → Chọn D!',
            'Mẹo lọc nhanh Synthesis 750+: Nếu Goal nói "introduce the concept of [X]", loại lập tức mọi đáp án không giới thiệu tên thuật ngữ [X] hoặc bỏ sót sắc thái nhấn mạnh ("psychological rather than purely time-based")!',
            [
                ('Missing Target Concept', 'Chỉ giải thích việc chuyển tàu cơ bản (thừa với độc giả đã quen tàu đô thị) và không hề nhắc "transfer penalty".'),
                ('Missing Target Concept', 'Không nhắc thuật ngữ "transfer penalty" hay khía cạnh tâm lý cảm nhận thời gian.'),
                ('Contradiction / Off-Point', 'Chỉ nói 5 phút chuyển tàu tốn 5 phút chờ — bỏ qua hoàn toàn hiệu ứng tâm lý kéo giãn thành 12–15 phút.'),
                ('Đáp án đúng', 'Giới thiệu gọn gàng "transfer penalty" và chứng minh đậm nét khía cạnh tâm lý vượt lên trên thời gian thực tế.'),
            ]
        ),
        q_item(
            'm6_m2h_q27', 27, 'Expression of Ideas', 'Rhetorical Synthesis', 'Elite (750+)',
            '''<p>While researching ancient materials science, a student has taken the following notes:</p>
            <ul>
              <li>Ancient Roman marine concrete routinely contains millimeter-scale white mineral specks called lime clasts.</li>
              <li>For decades, materials scientists assumed these lime clasts were accidental defects caused by sloppy mortar mixing or low-quality limestone.</li>
              <li>In 2023, MIT engineer Admir Masic and colleagues analyzed Roman concrete samples using high-resolution spectroscopy and laboratory hot-mixing trials.</li>
              <li>The team discovered that Roman builders intentionally hot-mixed dry quicklime to generate reactive lime clasts, which dissolve in infiltrating water and recrystallize to seal cracks automatically.</li>
            </ul>''',
            'The student wants to explain how a 2023 materials-science finding overturned an earlier misconception about white mineral specks inside ancient Roman concrete. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
            [
                'In 2023, MIT engineer Admir Masic and colleagues used high-resolution spectroscopy and laboratory hot-mixing trials to examine samples of ancient Roman marine concrete.',
                'Although scientists long dismissed the white lime clasts inside ancient Roman concrete as accidental mixing defects, a 2023 study by Admir Masic and colleagues showed they were intentionally created through hot-mixing to dissolve in water and automatically seal cracks.',
                'Millimeter-scale white mineral specks known as lime clasts appear throughout ancient Roman marine concrete and recrystallize whenever water penetrates the mortar.',
                'For decades, materials scientists believed that white lime clasts in Roman concrete resulted from sloppy mortar mixing or poor-quality limestone.'
            ],
            'B',
            'Goal-First SOP 750+: Yêu cầu giải thích CÁCH phát hiện năm 2023 LẬT ĐỔ một ngộ nhận trước đó ("overturned an earlier misconception") về các đốm trắng. A chỉ nêu phương pháp nghiên cứu 2023 (thiếu ngộ nhận cũ và kết quả); C chỉ nêu hiện tượng tự kết tinh (thiếu mốc 2023 và ngộ nhận cũ); D chỉ nêu ngộ nhận cũ (thiếu phát hiện 2023 lật đổ nó). Duy nhất B ghép chặt cả hai cực: ngộ nhận hàng thập kỷ (lỗi trộn cẩu thả) ↔ phát hiện 2023 của Masic (cố tình trộn nóng để tự hàn kín khe nứt) → Chọn B!',
            'Goal chứa chữ "overturned an earlier misconception" → đáp án đúng BẮT BUỘC phải nêu rõ CẢ ngộ nhận cũ LẪN phát hiện mới bác bỏ nó!',
            [
                ('Incomplete Goal', 'Chỉ kể phương pháp nghiên cứu năm 2023 mà không nêu ngộ nhận cũ hay kết luận lật đổ.'),
                ('Đáp án đúng', 'Khớp hoàn chỉnh cấu trúc lật đổ ngộ nhận: từ quan niệm lỗi trộn cẩu thả sang phát hiện năm 2023 về trộn nóng có chủ đích để tự chữa lành vết nứt.'),
                ('Missing Misconception & Study', 'Bỏ qua hoàn toàn ngộ nhận cũ lẫn nghiên cứu năm 2023.'),
                ('Incomplete Goal', 'Chỉ mô tả ngộ nhận trước đây mà không hề nhắc phát hiện năm 2023 đã bác bỏ nó ra sao.'),
            ]
        ),
    ]
