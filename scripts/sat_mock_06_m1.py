# -*- coding: utf-8 -*-
"""
Full-Length Adaptive Mock Test #6 — Module 1 (27 Qs, Easy/Medium/Hard Mix, 32 min)
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
            'm6_m1_q1', 1, 'Craft and Structure', 'Words in Context', 'Easy',
            '<p>In an optical lattice atomic clock, physicists trap thousands of ultracold strontium atoms inside an intersecting grid of laser beams so that thermal motion becomes almost ______, allowing researchers to measure atomic oscillation frequencies with extraordinary precision.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            ['turbulent', 'abundant', 'negligible', 'visible'],
            'C',
            'Cause-Effect Clue: làm lạnh cực sâu (ultracold) và giam giữ nguyên tử trong lưới tia laser giúp đo tần số dao động cực kỳ chính xác → chuyển động nhiệt phải trở nên gần như KHÔNG ĐÁNG KỂ → "negligible" (C).',
            'Bẫy nguyên tử siêu lạnh để đo chính xác tuyệt đối ⇒ chuyển động nhiệt gây nhiễu phải bị triệt tiêu gần như bằng không ("negligible").',
            [
                ('Opposite Meaning', 'turbulent = hỗn loạn dữ dội — trái ngược hoàn toàn với mục đích cố định nguyên tử siêu lạnh.'),
                ('Opposite Meaning', 'abundant = dồi dào phong phú — ngược với trạng thái siêu lạnh.'),
                ('Đáp án đúng', 'negligible = nhỏ đến mức không đáng kể — khớp tuyệt đối với mục tiêu triệt tiêu nhiễu nhiệt để đo chuẩn xác.'),
                ('Wrong Context', 'visible = có thể nhìn thấy bằng mắt thường — không liên quan tới độ chính xác dao động nguyên tử.'),
            ]
        ),
        q_item(
            'm6_m1_q2', 2, 'Craft and Structure', 'Words in Context', 'Medium',
            '<p>Before archaeologists unearthed a cache of fourth-century Sogdian merchant letters sealed inside a ruined watchtower near Dunhuang, historians relied almost exclusively on Chinese imperial chronicles to reconstruct Silk Road trade; those private dispatches vividly ______ the day-to-day credit arrangements and family anxieties of caravan agents operating between Samarkand and Luoyang.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            ['illuminate', 'obscure', 'fabricate', 'repudiate'],
            'A',
            'Contrast + Restatement Clue: trước kia sử gia chỉ có chính sử Trung Hoa → nay những bức thư riêng của thương nhân Sogdia SOI SÁNG / LÀM RÕ sinh động đời sống tín dụng và nỗi lo thường nhật của thương đoàn → "illuminate" (A).',
            'Nghĩa học thuật phổ biến của "illuminate" = làm sáng tỏ, mang lại cái nhìn rõ nét về một giai đoạn lịch sử trước đây còn mờ nhạt.',
            [
                ('Đáp án đúng', 'illuminate = soi sáng, làm rõ chi tiết — khớp hoàn hảo với trạng từ "vividly" và bối cảnh bổ sung góc nhìn mới bên cạnh chính sử.'),
                ('Opposite Meaning', 'obscure = làm lu mờ, che khuất — trái ngược với giá trị khai sáng của nguồn tư liệu mới.'),
                ('Wrong Tone', 'fabricate = bịa đặt giả mạo — trái ngược với tính chân thực của thư cổ khảo cổ.'),
                ('Wrong Direction', 'repudiate = bác bỏ kịch liệt — bức thư bổ sung chi tiết đời thường chứ không bác bỏ thỏa thuận tín dụng của chính thương nhân.'),
            ]
        ),
        q_item(
            'm6_m1_q3', 3, 'Craft and Structure', 'Words in Context', 'Medium',
            '<p>In dense subtropical forests where little wind penetrates the understory, several species of <i>Mycena</i> fungi emit a steady greenish glow at night; field experiments indicate that this bioluminescence evolved primarily to ______ nocturnal beetles and fungus gnats, which pick up sticky spores on their bodies and disperse them to distant rotting logs.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            ['repel', 'camouflage', 'exhaust', 'entice'],
            'D',
            'Cause-Effect Clue: rừng rậm ít gió nên nấm cần bọ cánh cứng và ruồi nấm ban đêm tới mang bào tử đi phát tán → ánh sáng phát quang tiến hóa nhằm THU HÚT / DẪN DỤ côn trùng đêm → "entice" (D).',
            'Nấm cần côn trùng lại gần để bám bào tử mang đi → chọn động từ mang nghĩa thu hút ("entice / attract").',
            [
                ('Opposite Meaning', 'repel = xua đuổi — trái ngược mục đích nhờ côn trùng phát tán bào tử.'),
                ('Opposite Meaning', 'camouflage = ngụy trang che giấu — trái ngược vì ánh sáng phát quang làm nổi bật nấm trong đêm.'),
                ('Wrong Meaning', 'exhaust = làm kiệt sức — không phù hợp cơ chế phát tán bào tử.'),
                ('Đáp án đúng', 'entice = thu hút, lôi cuốn — khớp chuẩn mục đích gọi côn trùng đêm tới mang bào tử đi xa.'),
            ]
        ),
        q_item(
            'm6_m1_q4', 4, 'Craft and Structure', 'Words in Context', 'Hard',
            '<p>Mid-twentieth-century Brutalist civic halls erected across arid North African cities relied on massive poured-concrete facades that absorbed intense solar radiation all afternoon and radiated stored heat indoors well past midnight—a thermal flaw that ______ cooling expenses whenever mechanical air-conditioning systems struggled during prolonged summer heat waves.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            ['alleviated', 'compounded', 'stabilized', 'circumvented'],
            'B',
            'Cause-Effect Clue: khuyết điểm nhiệt tích tụ sức nóng suốt chiều rồi tỏa ngược vào trong nhà qua nửa đêm ("a thermal flaw") → LÀM TRẦM TRỌNG THÊM / NHÂN LÊN chi phí làm mát trong đợt nắng nóng kéo dài → "compounded" (B).',
            'Động từ học thuật "compound" = làm trầm trọng thêm một vấn đề/gánh nặng sẵn có (exacerbate / worsen).',
            [
                ('Opposite Meaning', 'alleviated = làm dịu bớt/giảm nhẹ — trái ngược hoàn toàn với "a thermal flaw".'),
                ('Đáp án đúng', 'compounded = làm trầm trọng thêm, chất chồng thêm chi phí làm mát vốn đã căng thẳng trong đợt nắng nóng.'),
                ('Wrong Direction', 'stabilized = làm ổn định — sai với hệ quả tiêu cực của tường bê tông tích nhiệt.'),
                ('Wrong Meaning', 'circumvented = né tránh/đi vòng qua — tường bê tông gây tăng chi phí chứ không giúp né tránh chi phí.'),
            ]
        ),
        q_item(
            'm6_m1_q5', 5, 'Craft and Structure', 'Words in Context', 'Hard',
            '<p>Whereas modern Portland cement seawalls often corrode within decades as saltwater seeps into microscopic fissures, ancient Roman harbor concrete incorporated reactive quicklime inclusions that dissolve upon contact with infiltrating seawater and recrystallize as calcium carbonate—effectively ______ hairline cracks before they can widen into structural failures.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            ['widening', 'exposing', 'arresting', 'accelerating'],
            'C',
            'Contrast + Mechanism Clue: đối lập với xi măng hiện đại nhanh ăn mòn → vôi sống hòa tan và tái kết tinh lấp đầy khe nứt siêu nhỏ TRƯỚC KHI chúng lan rộng thành sụp đổ kết cấu → CHẶN ĐỨNG / LÀM NGƯNG sự lan rộng vết nứt → Nghĩa thứ cấp học thuật của "arrest" = halt / stop the progress of → Chọn C!',
            'Nhớ nghĩa thứ cấp đắt giá trên Digital SAT: "arrest" (trong khoa học/y học/kỹ thuật) = chặn đứng, làm ngừng tiến triển (không phải "bắt giữ tội phạm")!',
            [
                ('Opposite Meaning', 'widening = mở rộng thêm — ngược với cụm "before they can widen".'),
                ('Wrong Direction', 'exposing = làm phơi bày — tái kết tinh canxi cacbonat lấp kín khe nứt chứ không làm lộ khe nứt.'),
                ('Đáp án đúng', 'arresting (nghĩa thứ cấp: chặn đứng tiến trình) khớp hoàn hảo cơ chế tự chữa lành khe nứt trước khi lan rộng.'),
                ('Opposite Meaning', 'accelerating = đẩy nhanh tốc độ — trái hoàn toàn với độ bền hai thiên niên kỷ của bê tông La Mã.'),
            ]
        ),

        # --- Q6-Q7: Craft and Structure — Text Structure and Purpose ---
        q_item(
            'm6_m1_q6', 6, 'Craft and Structure', 'Text Structure and Purpose', 'Medium',
            '<p>During the 1870s, Victorian botanical artist Marianne North traveled unaccompanied across South America, Borneo, and South Africa to paint unfamiliar tropical flora directly in their native habitats. <u>Conventional museum illustrators of her era worked mainly from dried herbarium specimens shipped back to London, whose flattened petals and faded pigments frequently concealed a plant’s true posture and natural pollinators.</u> By painting oil studies outdoors beside living blossoms, North produced visual records that botanists at Kew Gardens later used to identify several previously unclassified species.</p>',
            'Which choice best describes the function of the underlined sentence in the text as a whole?',
            [
                'It argues that dried herbarium specimens were more scientifically reliable than North’s outdoor oil paintings.',
                'It details the chemical formulas Victorian artists used to preserve oil pigments during ocean voyages.',
                'It criticizes botanists at Kew Gardens for refusing to examine Marianne North’s tropical sketches.',
                'It highlights a limitation of standard Victorian botanical illustration to show why North’s fieldwork method was unusually valuable.'
            ],
            'D',
            'Câu 1 giới thiệu cách làm khác biệt của Marianne North (vẽ trực tiếp ngoài tự nhiên). Câu gạch chân mô tả hạn chế của phương pháp truyền thống (vẽ mẫu ép khô gửi về London bị bẹp cánh, phai màu, mất dấu côn trùng thụ phấn) để làm nổi bật giá trị khoa học vượt trội của phương pháp vẽ sống tại chỗ ở câu 3 → Chọn D!',
            'Cấu trúc đối chiếu kinh điển: Câu 1 (phương pháp mới) → Câu 2 gạch chân (nhược điểm phương pháp cũ) → Câu 3 (thành quả của phương pháp mới).',
            [
                ('Reversed Logic', 'Câu gạch chân nhấn mạnh điểm yếu của mẫu ép khô ("flattened petals and faded pigments"), không khen chúng tin cậy hơn tranh vẽ sống.'),
                ('Out of Scope', 'Không đề cập công thức hóa học bảo quản sơn dầu.'),
                ('Contradiction', 'Câu cuối nói các nhà thực vật học ở Kew Gardens ĐÃ dùng tranh của North để định danh nhiều loài mới.'),
                ('Đáp án đúng', 'Nêu rõ nhược điểm của cách vẽ mẫu ép khô truyền thống để làm bật lên giá trị độc đáo trong phương pháp điền dã của North.'),
            ]
        ),
        q_item(
            'm6_m1_q7', 7, 'Craft and Structure', 'Text Structure and Purpose', 'Hard',
            '<p><i>The following text is adapted from a fictional 1889 diary entry by astronomer Clara Henshaw, written inside her hilltop observatory near Edinburgh.</i><br/>At half past two the brass micrometer screw grew so cold it stung through my woolen gloves, and the lantern wick flickered low beside my notebook. Yet whenever I pressed my eye back to the eyepiece and watched the twin golden sparks of Albireo drift across the crosshairs in unhurried silence, the drafty floorboards vanished beneath me; it seemed less like solitary labor than like keeping an appointment with light that had departed its distant sun centuries before this hill bore a single stone wall.</p>',
            'Which choice best states the main purpose of the text?',
            [
                'To convey how the narrator’s awe while observing distant starlight outweighs the physical discomfort of working alone through a freezing night.',
                'To explain how brass micrometer screws measure the surface temperature of double stars such as Albireo.',
                'To lament that nineteenth-century observatories in Edinburgh lacked adequate heating equipment for astronomers.',
                'To argue that historical stonework near Edinburgh interferes with accurate telescopic observations.'
            ],
            'A',
            'Câu đầu tả cái lạnh buốt tay và ánh đèn dầu leo lét lúc 2h30 sáng. Từ chữ "Yet" trở đi, toàn bộ sự bất tiện thể chất tan biến khi nhân vật nhìn thấy cặp sao đôi Albireo trôi qua dây chữ thập — cảm giác như giữ một cuộc hẹn với ánh sáng cổ xưa đầy kinh ngạc và say mê → Chọn A!',
            'Khóa chữ "Yet" chia đôi đoạn văn học: nửa đầu là khó khăn vật lý (lạnh, khuya, đơn độc), nửa sau là sự choáng ngợp đầy say mê xóa tan nhọc nhằn.',
            [
                ('Đáp án đúng', 'Tóm gọn trọn vẹn mạch cảm xúc: niềm kinh ngạc khi ngắm ánh sao cổ xưa lấn át hoàn toàn cái lạnh và sự vất vả lúc đêm khuya.'),
                ('Out of Scope / Literal', 'Không giải thích kỹ thuật đo nhiệt độ bề mặt sao bằng ốc vi kế.'),
                ('Narrow / Wrong Tone', 'Cái lạnh chỉ là phông nền tương phản, không phải bài viết phàn nàn về thiết bị sưởi.'),
                ('Literal Misreading', 'Cụm "before this hill bore a single stone wall" chỉ nhằm nhấn mạnh tuổi đời hàng thế kỷ của ánh sáng sao, không nói tường đá cản kính thiên văn.'),
            ]
        ),

        # --- Q8: Craft and Structure — Cross-Text Connections ---
        q_item(
            'm6_m1_q8', 8, 'Craft and Structure', 'Cross-Text Connections', 'Hard',
            '<p><b>Text 1</b><br/>Transit planner Dr. Henrik Lindqvist argues that installing digital real-time arrival screens on urban subway platforms consistently reduces commuter anxiety, asserting that whenever riders can see exact minute-by-minute countdowns, waiting feels noticeably shorter and overall satisfaction with rail reliability rises.</p><p><b>Text 2</b><br/>In a 2024 behavioral study of 3,400 rail commuters in Toronto and Vienna, economist Dr. Priya Nair confirmed that countdown displays lowered perceived wait times by roughly 20 percent during normal service and brief delays. However, during major signal disruptions—when screens repeatedly froze at "2 minutes" or revised estimates upward—riders on equipped platforms reported significantly higher anger and distrust than riders waiting on stations without digital displays.</p>',
            'Based on the texts, how would Dr. Priya Nair (Text 2) most likely respond to Dr. Henrik Lindqvist’s argument (Text 1)?',
            [
                'By contending that digital countdown displays fail to reduce perceived wait times even when subway trains operate on schedule.',
                'By agreeing that countdown screens ease waiting anxiety during routine service, while cautioning that inaccurate or stalling estimates during severe disruptions can actually worsen rider frustration.',
                'By asserting that commuters in Toronto and Vienna prefer riding municipal buses rather than urban subway trains.',
                'By recommending that transit agencies remove digital arrival screens from all platforms regardless of service reliability.'
            ],
            'B',
            'Text 1 khẳng định tuyệt đối ("consistently reduces... whenever riders can see..."). Text 2 XÁC NHẬN hiệu quả trong vận hành bình thường và chậm nhẹ (giảm ~20% thời gian chờ cảm nhận), NHƯNG CẢNH BÁO tác dụng ngược khi sự cố tín hiệu khiến đồng hồ đứng im hoặc nhảy tăng thời gian (làm tăng giận dữ và mất niềm tin hơn cả ga không có màn hình) → Phản hồi cân bằng "đồng tình có điều kiện + chỉ ra ngoại lệ phản tác dụng" → Chọn B!',
            'Trong Cross-Text, chú ý cấu trúc "confirmed X. However, during Y..." của Text 2 — không bác bỏ sạch trơn (loại A, D) mà tinh chỉnh điều kiện áp dụng (B)!',
            [
                ('Overstated Conflict', 'Text 2 XÁC NHẬN màn hình giảm ~20% thời gian chờ cảm nhận khi tàu chạy bình thường ("confirmed... during normal service").'),
                ('Đáp án đúng', 'Phản ánh chính xác 2 vế của Nair: đồng ý về lợi ích lúc bình thường nhưng cảnh báo tác dụng ngược khi số liệu treo/tăng lúc gặp sự cố lớn.'),
                ('Out of Scope', 'Text 2 không hề nhắc tới xe buýt đô thị.'),
                ('Too Extreme', 'Nair không đề xuất dỡ bỏ toàn bộ màn hình khỏi mọi nhà ga.'),
            ]
        ),

        # --- Q9-Q10: Information and Ideas — Central Ideas and Details ---
        q_item(
            'm6_m1_q9', 9, 'Information and Ideas', 'Central Ideas and Details', 'Medium',
            '<p><i>The following excerpt is from an original contemporary poem titled “Lanterns of the Cedar Floor.”</i></p><p style="margin-left:18px;font-style:italic;">When twilight seals the canopy in slate,<br/>And birds fold silence underneath their wings,<br/>Along the fallen cedar’s dampened bark<br/>A constellation of pale emerald springs.<br/>No fire warms these clustered forest lamps,<br/>No traveler hangs them on a cedar bough;<br/>Yet night-winged beetles gather to their glow<br/>And carry unseen harvests through the dark.</p>',
            'Which choice best states the main idea of the poem?',
            [
                'Forest travelers hang emerald glass lanterns on fallen cedar logs to guide nocturnal birds safely through the dark.',
                'Wildfires frequently sweep through damp cedar forests at twilight, destroying the habitats of nocturnal beetles.',
                'Nocturnal beetles extinguish glowing forest mushrooms before dawn to protect cedar trees from decay.',
                'After nightfall, bioluminescent fungi illuminate damp fallen wood with a cool light that draws nocturnal beetles to help spread their spores.'
            ],
            'D',
            'Đọc hình ảnh thơ: Khi hoàng hôn phủ tán rừng ("twilight seals the canopy"), dọc vỏ gỗ tuyết tùng đổ ẩm ướt bật sáng chùm ánh sáng xanh ngọc lục bảo lạnh ("No fire warms these clustered forest lamps" = phát quang sinh học của nấm). Bọ cánh cứng đêm bay tới ánh sáng ấy và mang đi "unseen harvests" (bào tử vô hình) xuyên bóng tối → Chọn D!',
            'Giải mã ẩn dụ thơ SAT: "pale emerald... No fire warms... forest lamps" = nấm phát quang sinh học; "unseen harvests" = bào tử nấm được bọ đêm phát tán.',
            [
                ('Literal Misreading', 'Thơ phủ định rõ "No traveler hangs them" — không hề có lữ khách treo đèn thủy tinh.'),
                ('Contradiction', 'Thơ viết "No fire warms" (không hề có lửa cháy rừng).'),
                ('Reversed Logic', 'Bọ cánh cứng không dập tắt nấm mà mang bào tử của nấm đi phát tán.'),
                ('Đáp án đúng', 'Diễn đạt chính xác toàn bộ hình ảnh thơ: nấm phát quang ánh sáng lạnh trên thân gỗ ẩm sau hoàng hôn thu hút bọ đêm phát tán bào tử.'),
            ]
        ),
        q_item(
            'm6_m1_q10', 10, 'Information and Ideas', 'Central Ideas and Details', 'Medium',
            '<p>Between the fourth and eighth centuries CE, Sogdian merchants based in the Zarafshan River valley of Central Asia served as the primary commercial intermediaries linking Persian, Indian, and Tang Chinese markets. Rather than hauling bulky chests of silver coins across thousands of kilometers of desert bandit territory, Sogdian family firms stationed trusted relatives at oasis towns from Samarkand to Chang’an, settling accounts through written promissory notes verified by carved personal seals.</p>',
            'According to the text, how did Sogdian merchant firms avoid transporting heavy chests of silver coins across hazardous desert routes?',
            [
                'By abandoning overland caravan routes in favor of direct maritime voyages around southern India.',
                'By hiring Tang imperial soldiers to escort every individual camel caravan between Samarkand and Persia.',
                'By positioning trusted family members in oasis hubs and balancing payments through sealed written promissory notes.',
                'By trading exclusively in perishable agricultural produce rather than precious metals or silk.'
            ],
            'C',
            'Câu hỏi Specific Detail: Tìm đúng cụm "Rather than hauling bulky chests of silver coins..." → vế sau nêu giải pháp: "stationed trusted relatives at oasis towns... settling accounts through written promissory notes verified by carved personal seals" → Paraphrase chính xác ở C!',
            'Tìm cụm phủ định đối chiếu "Rather than [X], [chủ ngữ] did [Y]" → vế Y chính là đáp án chi tiết!',
            [
                ('Out of Scope', 'Không nhắc tuyến hàng hải vòng qua miền Nam Ấn Độ.'),
                ('Out of Scope', 'Không đề cập việc thuê quân lính nhà Đường hộ tống từng đoàn lạc đà.'),
                ('Đáp án đúng', 'Khớp sát từng chi tiết: bố trí người thân đáng tin cậy tại các ốc đảo và thanh toán bằng giấy hẹn nợ có ấn triện.'),
                ('Out of Scope', 'Không nói thương nhân chỉ buôn nông sản dễ hỏng.'),
            ]
        ),

        # --- Q11-Q12: Information and Ideas — Command of Evidence (Textual) ---
        q_item(
            'm6_m1_q11', 11, 'Information and Ideas', 'Command of Evidence (Textual)', 'Hard',
            '<p>Materials scientists examining ancient Roman concrete seawalls long assumed that millimeter-scale white calcium-rich specks ("lime clasts") scattered throughout the mortar were merely signs of careless mixing. However, engineer Dr. Admir Masic and colleagues proposed that Roman builders intentionally added dry, unslaked quicklime at high temperatures ("hot mixing") so that residual lime clasts would act as internal healing reservoirs whenever cracks formed later.</p>',
            'Which finding, if true, would most directly support Dr. Admir Masic and colleagues’ hypothesis?',
            [
                'Laboratory replicas produced by hot-mixing quicklime form fracture-spanning calcium carbonate crystals that completely seal deliberate 0.5-millimeter cracks within two weeks of water exposure, whereas cold-mixed replicas without lime clasts remain permanently cracked.',
                'Chemical analyses show that volcanic ash quarried near the Bay of Naples contains higher concentrations of aluminum than volcanic ash mined in northern Italy.',
                'Surviving architectural treatises from imperial Rome note that marble columns imported from Greece were significantly more expensive than local limestone blocks.',
                'Modern Portland cement bridges built in dry inland climates often require surface resurfacing after thirty years of heavy truck traffic.'
            ],
            'A',
            'Khóa giả thuyết Masic: "hot mixing" tạo hạt vôi sống tồn dư đóng vai trò KHO TỰ CHỮA LÀNH (internal healing reservoirs) khi xuất hiện vết nứt. Đáp án A cung cấp thí nghiệm đối chứng hoàn hảo: mẫu tái tạo bằng hot-mixing tự kết tinh lấp kín vết nứt 0,5 mm trong 2 tuần gặp nước, trong khi mẫu trộn nguội không có hạt vôi sống vẫn nứt vĩnh viễn → Chọn A!',
            'Bằng chứng mạnh nhất cho một cơ chế vật liệu luôn là thí nghiệm đối chứng có nhóm thử nghiệm (hot-mixed with clasts → tự hàn gắn) so với nhóm đối chứng (cold-mixed without clasts → không hàn gắn)!',
            [
                ('Đáp án đúng', 'Thực nghiệm đối chứng trực tiếp xác nhận hạt vôi từ quy trình trộn nóng giúp tự hàn kín khe nứt khi gặp nước, trong khi trộn nguội thất bại.'),
                ('Adjacent Topic Drift', 'Hàm lượng nhôm trong tro núi lửa không kiểm chứng vai trò tự chữa lành của hạt vôi sống trộn nóng.'),
                ('Irrelevant Subject', 'Giá cột đá cẩm thạch Hy Lạp không liên quan đến hóa học bê tông cảng biển.'),
                ('Irrelevant Subject', 'Cầu bê tông hiện đại ở vùng nội địa khô không kiểm chứng giả thuyết về vôi trộn nóng La Mã.'),
            ]
        ),
        q_item(
            'm6_m1_q12', 12, 'Information and Ideas', 'Command of Evidence (Textual)', 'Hard',
            '<p>In a critical review of the 1968 play <i>Sun and Concrete</i>, an architecture scholar argues that although municipal designer Nadia genuinely admires the bold monumental forms of Brutalist concrete towers, she believes they disregard the quiet, climate-adapted wisdom of traditional desert adobe builders.</p>',
            'Which quotation from Nadia in <i>Sun and Concrete</i> most effectively illustrates the scholar’s claim?',
            [
                '“The municipal zoning board approved twelve new highway interchanges before any of us finished surveying the eastern oasis.”',
                '“I still catch my breath at the daring cantilevered sweep of those raw concrete ministries—yet every afternoon they bake like ovens, stubbornly ignoring the shaded courtyards and wind-scoops our grandfathers perfected over six centuries.”',
                '“Imported steel reinforcement bars have doubled in price since last autumn, forcing every contractor in the province to revise his bid.”',
                '“Traditional earthen roofs require a fresh layer of clay plaster after rare winter cloudbursts, which keeps local masons busy every February.”'
            ],
            'B',
            'Checklist 2 vế từ Claim: [1] Ngưỡng mộ thực sự vẻ táo bạo đồ sộ của tháp bê tông Brutalist ("genuinely admires the bold monumental forms") + [2] Cho rằng chúng phớt lờ trí tuệ thích ứng khí hậu của kiến trúc đất nung sa mạc truyền thống ("disregard the climate-adapted wisdom of traditional adobe builders"). Duy nhất B thể hiện trọn cả hai vế: "catch my breath at the daring cantilevered sweep..." ↔ "bake like ovens, stubbornly ignoring the shaded courtyards and wind-scoops..." → Chọn B!',
            'Với nhận định hai vế ("although X, she believes Y"), loại ngay các câu trích dẫn chỉ nói 1 vế hoặc nói chuyện ngoài lề!',
            [
                ('Irrelevant Detail', 'Chỉ nói về việc duyệt nút giao cao tốc của hội đồng quy hoạch.'),
                ('Đáp án đúng', 'Minh họa xuất sắc cả sự ngưỡng mộ hình khối Brutalist lẫn sự phê phán chúng phớt lờ sân râm và tháp đón gió truyền thống.'),
                ('Irrelevant Detail', 'Chỉ bàn giá thép nhập khẩu tăng gấp đôi.'),
                ('Half-Match / Off-Point', 'Chỉ nói việc bảo trì mái đất sét sau mưa đông, không nhắc bê tông Brutalist hay sự phớt lờ trí tuệ khí hậu.'),
            ]
        ),

        # --- Q13-Q14: Information and Ideas — Command of Evidence (Quantitative) ---
        q_item(
            'm6_m1_q13', 13, 'Information and Ideas', 'Command of Evidence (Quantitative)', 'Medium',
            svg_bar_chart(
                'Peak Afternoon Indoor Cooling (°C Below Unshaded Concrete Reference) in Arid Field Trial',
                ['0°C', '2°C', '4°C', '6°C', '8°C', '10°C'],
                [('Insulated Concrete', 2.4, '2.4°C'), ('Lattice Screen', 4.6, '4.6°C'), ('Adobe Courtyard', 6.8, '6.8°C'), ('Adobe+Windcatcher', 9.1, '9.1°C')],
                10
            ) + '<p>Architectural climatologists testing passive cooling designs in an arid summer climate concluded that while adding exterior insulation or perforated lattice screens to modern concrete enclosures produces modest indoor cooling, combining traditional thick adobe walls with a rooftop windcatcher achieves nearly four times the peak afternoon cooling of insulated concrete alone.</p>',
            'Which choice most effectively uses data from the graph to support the climatologists’ conclusion?',
            [
                'Perforated lattice screens cooled indoor air by 4.6°C below the unshaded concrete reference during peak afternoon heat.',
                'An adobe courtyard without a windcatcher lowered peak afternoon indoor temperature by 6.8°C compared with the unshaded reference.',
                'Combining thick adobe walls with a rooftop windcatcher lowered peak afternoon indoor temperature by 9.1°C—almost four times the 2.4°C reduction achieved by insulated concrete alone.',
                'All four passive architectural strategies tested in the arid field trial lowered peak afternoon indoor temperatures relative to unshaded concrete.'
            ],
            'C',
            'Khóa kết luận cần chứng minh: kết hợp tường đất nung + tháp đón gió ("Adobe+Windcatcher") đạt mức hạ nhiệt GẦN GẤP 4 LẦN bê tông cách nhiệt đơn thuần ("nearly four times... of insulated concrete alone"). Kiểm tra phép nhân: 2,4°C × 4 = 9,6°C; thực tế đạt 9,1°C (9,1 / 2,4 ≈ 3,79 → gần gấp 4 lần!). Duy nhất C nêu và đối chiếu trực tiếp hai mốc 9,1°C và 2,4°C → Chọn C!',
            'Khi đề có so sánh tỷ lệ ("nearly four times"), đáp án đúng BẮT BUỘC phải gọi tên đủ cả hai cột được so sánh kèm đúng con số của từng cột!',
            [
                ('True Data / Wrong Claim', 'Số liệu 4,6°C đúng với biểu đồ nhưng không chứng minh tỷ lệ gần gấp 4 giữa Adobe+Windcatcher và Insulated Concrete.'),
                ('True Data / Wrong Claim', 'Chỉ nêu Adobe Courtyard (6,8°C) mà không nhắc tới tổ hợp có windcatcher hay bê tông cách nhiệt.'),
                ('Đáp án đúng', 'Đối chiếu chính xác 9,1°C với 2,4°C, xác thực lập luận gần gấp 4 lần mức hạ nhiệt.'),
                ('Too Broad', 'Chỉ nói cả 4 phương án đều giảm nhiệt, quá chung chung không hỗ trợ khẳng định gấp 4 lần.'),
            ]
        ),
        q_item(
            'm6_m1_q14', 14, 'Information and Ideas', 'Command of Evidence (Quantitative)', 'Hard',
            html_table(
                'Table 1. Mean Insect Visits per Acrylic Trap in Subtropical Forest Plots (72-Hour Trial)',
                ['Insect Order', 'Daytime: Glowing Trap', 'Daytime: Dark Control', 'Nighttime: Glowing Trap', 'Nighttime: Dark Control'],
                [
                    ['Beetles (Coleoptera)', '6', '7', '54', '11'],
                    ['Flies & Gnats (Diptera)', '14', '13', '68', '16'],
                    ['Wasps & Ants (Hymenoptera)', '19', '18', '41', '9'],
                    ['True Bugs (Hemiptera)', '12', '11', '8', '9'],
                ]
            ) + '<p>An evolutionary ecologist claims that because fungal bioluminescence mimics warm starlight across the dark forest floor, glowing traps will attract substantially more nocturnal visitors than dark control traps across every major insect order inhabiting the understory.</p>',
            'Which choice best describes data from the table that directly weaken the ecologist’s claim?',
            [
                'During the nighttime period, glowing traps attracted 68 flies and gnats compared with only 16 on dark control traps.',
                'Across all four insect orders, daytime visit counts were nearly identical between glowing traps and dark control traps.',
                'Nocturnal beetles visited glowing traps nearly five times as frequently (54 visits) as they visited dark control traps (11 visits).',
                'During the nighttime period, true bugs (Hemiptera) visited glowing traps slightly less often (8 visits) than they visited dark control traps (9 visits).'
            ],
            'D',
            'Khóa từ cực đoan trong Claim cần WEAKEN: "across EVERY major insect order" (ở MỌI bộ côn trùng lớn đều thu hút nhiều khách ban đêm hơn bẫy tối!). Quét 2 cột Nighttime trong bảng: Beetles (54 vs 11 ✓), Flies (68 vs 16 ✓), Wasps/Ants (41 vs 9 ✓), NHƯNG **True Bugs (Hemiptera)** chỉ có 8 lượt ở bẫy sáng so với 9 lượt ở bẫy tối! Phản ví dụ sắc lẹm phá vỡ chữ "every" → Chọn D!',
            'Thấy chữ "every / all" trong câu hỏi Weaken → quét bảng tìm đúng hàng NGOẠI LỆ có chiều đảo ngược (8 < 9)!',
            [
                ('Opposite Direction (Supports!)', 'Flies & Gnats tăng mạnh (68 vs 16) — ủng hộ tuyên bố chứ không làm yếu.'),
                ('Irrelevant Time Period', 'Tuyên bố nói về khách BAN ĐÊM ("nocturnal visitors"), không phải ban ngày.'),
                ('Opposite Direction (Supports!)', 'Beetles tăng gần gấp 5 (54 vs 11) — ủng hộ tuyên bố.'),
                ('Đáp án đúng', 'True Bugs là ngoại lệ trực tiếp: bẫy phát sáng (8) thậm chí ít lượt ghé ban đêm hơn bẫy tối (9), bác bỏ chữ "every".'),
            ]
        ),

        # --- Q15: Information and Ideas — Inferences ---
        q_item(
            'm6_m1_q15', 15, 'Information and Ideas', 'Inferences', 'Hard',
            '<p>According to Einstein’s general relativity, an atomic clock ticks slightly faster at higher elevation because Earth’s gravitational pull is marginally weaker there. Modern strontium optical lattice clocks are sensitive enough to detect this gravitational shift across height differences as small as one millimeter; however, when two separate clocks sit on different laboratory benches, tiny differences in room temperature, magnetic fields, and floor vibration easily overwhelm a millimeter-scale gravitational signal. To isolate that minuscule height effect cleanly, quantum metrologists have therefore begun ______</p>',
            'Which choice most logically completes the text?',
            [
                'stacking vertically separated layers of strontium atoms inside the exact same vacuum chamber so both groups share nearly identical environmental disturbances that cancel out upon comparison.',
                'replacing optical lattice lasers with traditional pendulum clocks that are unaffected by floor vibrations or magnetic fields.',
                'abandoning general relativity as a framework for calculating elevation differences on Earth’s surface.',
                'moving optical lattice clocks into outer space where strontium atoms no longer experience any atomic oscillation.'
            ],
            'A',
            'Ghép 2 tiền đề (1-Millimeter Rule): (1) Đồng hồ mạng quang học stronti đủ nhạy để đo độ lệch hấp dẫn ở chênh lệch cao độ 1 mm; (2) NHƯNG khi đặt 2 đồng hồ tách rời ở 2 bàn khác nhau, nhiễu nhiệt độ/từ trường/rung sàn khác biệt sẽ lấn át tín hiệu 1 mm ⇒ Giải pháp logic tất yếu: đặt các lớp nguyên tử stronti tách nhau theo chiều dọc TRONG CÙNG MỘT BUỒNG CHÂN KHÔNG để cả hai cùng chịu môi trường nhiễu giống hệt nhau (nên tự triệt tiêu khi so sánh chênh lệch!) → Chọn A!',
            'Bài toán triệt tiêu nhiễu khác biệt giữa 2 thiết bị tách rời → gộp chung vào 1 buồng duy nhất để nhiễu trở thành nhiễu chung (common-mode noise) và tự triệt tiêu!',
            [
                ('Đáp án đúng', 'Xếp chồng các lớp nguyên tử trong cùng một buồng chân không giải quyết trực diện nguyên nhân nhiễu khác biệt giữa hai bàn thí nghiệm.'),
                ('Absurd / Reversed Logic', 'Đồng hồ quả lắc kém chính xác hơn hàng tỷ lần và chịu rung chấn nặng hơn.'),
                ('Contradiction', 'Thuyết tương đối rộng là nền tảng của hiệu ứng cần đo, không phải thứ bị bác bỏ.'),
                ('Fact Distortion', 'Nguyên tử stronti vẫn dao động bình thường ngoài không gian; dao động lượng tử không phụ thuộc việc ở trên Trái Đất.'),
            ]
        ),

        # --- Q16-Q19: Standard English Conventions — Boundaries ---
        q_item(
            'm6_m1_q16', 16, 'Standard English Conventions', 'Boundaries', 'Easy',
            '<p>In 1898, solar astronomer Annie Maunder traveled to India with a custom lightweight camera to photograph the Sun’s outer corona during a total ______ her long-exposure glass plates captured feathery plasma streamers extending nearly six solar radii into space.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['eclipse,', 'eclipse;', 'eclipse', 'eclipse, and while'],
            'B',
            'Vế 1 là IC hoàn chỉnh ("In 1898, solar astronomer Annie Maunder traveled... during a total eclipse"). Vế 2 cũng là IC hoàn chỉnh ("her long-exposure glass plates captured..."). Giữa 2 IC → chọn dấu chấm phẩy (;) = B!',
            'Cặp IC + IC bắt buộc nối bằng dấu chấm phẩy (;), dấu chấm (.), hoặc ", + FANBOYS" — loại ngay Comma Splice (A), Run-on (C) và mảnh phụ treo lơ lửng (D).',
            [
                ('Comma Splice', 'Một dấu phẩy không thể nối hai mệnh đề độc lập.'),
                ('Đáp án đúng', 'Dấu chấm phẩy (;) ngăn cách chuẩn mực hai mệnh đề độc lập có liên hệ nghĩa chặt chẽ.'),
                ('Run-On Sentence', 'Không có dấu câu phân tách hai IC.'),
                ('Fragment / Subordinate Trap', 'Thêm "and while" biến vế 2 thành mệnh đề phụ treo lơ lửng không có mệnh đề chính theo sau.'),
            ]
        ),
        q_item(
            'm6_m1_q17', 17, 'Standard English Conventions', 'Boundaries', 'Medium',
            '<p>Using multispectral ultraviolet imaging to recover faded ink on birchbark fragments, philologist ______ identified previously untranslated Sogdian trade receipts documenting musk and saffron shipments.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            [', Dr. Ramin Farhadi,', 'Dr. Ramin Farhadi,', ', Dr. Ramin Farhadi', 'Dr. Ramin Farhadi'],
            'D',
            'Quy tắc Title + Name không có mạo từ xác định phía trước: "philologist Dr. Ramin Farhadi" → Essential → 0 dấu phẩy cả trước lẫn sau, nối thẳng tới động từ chính "identified" → Chọn D!',
            'Chức danh không có "a/the" + Tên riêng + Động từ chính → 0 dấu phẩy!',
            [
                ('Non-Essential Trap', 'Chỉ đặt cặp phẩy khi chức danh phía trước có mạo từ xác định duy nhất.'),
                ('No-Comma Zone (S, V)', 'Dấu phẩy đơn cắt đứt chủ ngữ khỏi động từ chính "identified".'),
                ('Unpaired Comma', 'Chèn dấu phẩy lẻ giữa chức danh "philologist" và tên riêng.'),
                ('Đáp án đúng', 'Không dấu phẩy — giữ liền mạch cụm chủ ngữ chức danh–tên riêng với động từ chính.'),
            ]
        ),
        q_item(
            'm6_m1_q18', 18, 'Standard English Conventions', 'Boundaries', 'Medium',
            '<p>To explain how Roman pier concrete resisted two millennia of pounding Mediterranean surf, geochemists pointed to a surprising mineral ______ the gradual growth of interlocking aluminum-tobermorite crystals inside tiny saltwater-filled pores.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['mechanism;', 'mechanism.', 'mechanism:', 'mechanism, and'],
            'C',
            'Vế trước ("To explain..., geochemists pointed to a surprising mineral mechanism") là IC hoàn chỉnh. Vế sau ("the gradual growth of interlocking... crystals...") là Cụm danh từ (Noun Phrase — KHÔNG có động từ chia thì!) giải thích cụ thể cơ chế khoáng học đó là gì → Dùng dấu hai chấm (:) = C!',
            'IC hoàn chỉnh + Cụm danh từ giải thích (không có động từ chính) → chỉ dấu hai chấm (:) hợp lệ; loại sạch (;) và (.) vì tạo Fragment!',
            [
                ('Semicolon + Fragment', 'Vế sau là cụm danh từ không có động từ chia thì → cấm dùng chấm phẩy.'),
                ('Period + Fragment', 'Tách cụm danh từ thành câu độc lập gây lỗi Sentence Fragment.'),
                ('Đáp án đúng', 'Dấu hai chấm (:) sau IC giới thiệu chính xác cụm danh từ định nghĩa "a surprising mineral mechanism".'),
                ('Comma + FANBOYS + Fragment', 'Sau ", and" không có IC cũng không có phần tử song song phù hợp nghĩa.'),
            ]
        ),
        q_item(
            'm6_m1_q19', 19, 'Standard English Conventions', 'Boundaries', 'Hard',
            '<p>Weekly fare-capping policies—which automatically convert pay-as-you-go rail taps into an unlimited pass once a commuter reaches a spending ______ eliminate the financial penalty faced by lower-income riders who cannot afford upfront monthly passes.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['threshold—', 'threshold,', 'threshold;', 'threshold'],
            'A',
            'Cụm giải thích chen giữa Chủ ngữ ("Weekly fare-capping policies") và Động từ chính ("eliminate") mở đầu bằng gạch ngang dài (`—which automatically convert...`) → Phải đóng bằng gạch ngang dài tương ứng (`threshold—`) → Chọn A!',
            'Quy tắc cặp dấu đồng bộ: Mở bằng `—` thì BẮT BUỘC đóng bằng `—` ngay trước động từ chính "eliminate"!',
            [
                ('Đáp án đúng', 'Đóng đúng cặp gạch ngang đôi (— ... —) bao trọn mệnh đề phụ trước động từ chính "eliminate".'),
                ('Mismatched Pair (— ... ,)', 'Cấm mở bằng gạch ngang rồi đóng bằng dấu phẩy.'),
                ('Semicolon Inside Clause', 'Dấu chấm phẩy cắt lìa chủ ngữ khỏi động từ chính.'),
                ('Unclosed Modifier', 'Thiếu dấu đóng gạch ngang khiến toàn bộ phần sau bị nuốt vào cụm bổ ngữ.'),
            ]
        ),

        # --- Q20-Q22: Standard English Conventions — Form, Structure, and Sense ---
        q_item(
            'm6_m1_q20', 20, 'Standard English Conventions', 'Form, Structure, and Sense', 'Easy',
            '<p>A vast subterranean network of threadlike mycorrhizal fungal filaments linking birch, fir, and hemlock roots across old-growth temperate forests ______ phosphorus and water in exchange for tree-produced sugars.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['transport', 'transports', 'have transported', 'transporting'],
            'B',
            'Gạch bỏ chuỗi cụm giới từ & phân từ chen giữa: "A vast subterranean <b>network</b> <s>[of threadlike mycorrhizal fungal filaments linking birch, fir, and hemlock roots across old-growth temperate forests]</s>". Chủ ngữ thật là "A vast subterranean network" (SỐ ÍT), câu chưa có động từ chính → Chọn "transports" (B)!',
            'Quy tắc 3–1: A và C đều là số nhiều (bẫy danh từ gần như "roots / forests"), D là V-ing (Fragment), duy nhất B là động từ chia thì số ít khớp "network"!',
            [
                ('Subject-Verb Mismatch', 'transport là số nhiều — bị lừa bởi "filaments / roots / forests".'),
                ('Đáp án đúng', 'transports (hiện tại đơn số ít) khớp chuẩn chủ ngữ "A vast subterranean network".'),
                ('Subject-Verb Mismatch', 'have transported là số nhiều.'),
                ('Non-Finite Fragment', 'transporting là phân từ V-ing làm câu mất động từ chính.'),
            ]
        ),
        q_item(
            'm6_m1_q21', 21, 'Standard English Conventions', 'Form, Structure, and Sense', 'Medium',
            '<p>Constructed from thick sun-dried adobe bricks and topped with tall louvered shafts angled toward prevailing evening breezes, ______</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            [
                'generations of Persian desert builders perfected traditional windcatcher houses to cool interiors without electricity.',
                'scorching summer heat was naturally flushed out of traditional Persian windcatcher houses.',
                'engineers studying Yazd’s historic neighborhoods marvel at the passive airflow inside traditional windcatcher houses.',
                'traditional Persian windcatcher houses cool indoor living quarters naturally without mechanical air-conditioning.'
            ],
            'D',
            'Dangling Modifier Check! Cụm phân từ mở đầu "Constructed from thick sun-dried adobe bricks and topped with tall louvered shafts..." mô tả NHỮNG NGÔI NHÀ THÁP ĐÓN GIÓ ("traditional Persian windcatcher houses"), KHÔNG phải thợ xây (A), sức nóng mùa hè (B), hay các kỹ sư (C) → Duy nhất D đặt đúng chủ ngữ ngay sau dấu phẩy!',
            'Hỏi ngay: "Thứ gì được XÂY bằng gạch đất nung và có ống đón gió trên mái?" → Chỉ có "traditional Persian windcatcher houses" (D)!',
            [
                ('Dangling Modifier', 'Các thế hệ thợ xây Ba Tư không thể "được xây bằng gạch đất nung".'),
                ('Dangling Modifier', 'Sức nóng mùa hè không được xây từ gạch đất nung.'),
                ('Dangling Modifier', 'Các kỹ sư không phải công trình có ống đón gió trên nóc.'),
                ('Đáp án đúng', 'Chủ ngữ "traditional Persian windcatcher houses" đứng ngay sau dấu phẩy khớp 100% với cụm phân từ mở đầu.'),
            ]
        ),
        q_item(
            'm6_m1_q22', 22, 'Standard English Conventions', 'Form, Structure, and Sense', 'Hard',
            '<p>In a 2023 metrology comparison conducted at the University of Colorado, physicists confirmed that the fractional frequency stability of a three-dimensional strontium optical lattice clock exceeds ______ a standard microwave cesium fountain clock by roughly two orders of magnitude.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['those of', 'compared with', 'that of', 'with'],
            'C',
            'So sánh tương đồng (Apples-to-Apples): Đối tượng so sánh là "<b>the fractional frequency stability</b>" (SỐ ÍT — độ ổn định tần số tương đối) của đồng hồ mạng quang học stronti so với [độ ổn định tần số tương đối] của đồng hồ xêzi vi sóng! Vì "stability" là SỐ ÍT → chọn "<b>that of</b>" (C), loại "those of" (số nhiều) và loại B, D (dư/sai cấu trúc sau "exceeds")!',
            'Sau động từ "exceeds" cần tân ngữ tương đồng với danh từ số ít "stability" → chọn "that of" (không dùng "those of" hay giới từ thừa).',
            [
                ('Pronoun Number Mismatch', '"those of" chỉ thay cho danh từ số nhiều, trong khi "stability" là số ít không đếm được.'),
                ('Redundant / Illogical Structure', '"exceeds compared with" sai ngữ pháp và so sánh khập khiễng độ ổn định với chiếc đồng hồ.'),
                ('Đáp án đúng', '"that of" thay thế chuẩn xác cho danh từ số ít "the fractional frequency stability of".'),
                ('Illogical Comparison', '"exceeds with" sai ngữ pháp và thiếu đại từ thay thế "stability".'),
            ]
        ),

        # --- Q23-Q25: Expression of Ideas — Transitions ---
        q_item(
            'm6_m1_q23', 23, 'Expression of Ideas', 'Transitions', 'Easy',
            '<p>When microscopic cracks open inside ancient Roman harbor breakwaters, infiltrating seawater dissolves embedded quicklime clasts and triggers fresh calcium-rich mineral crystals to grow across the gap. ______, ancient marine concrete actually becomes stronger and more watertight over centuries of wave exposure.</p>',
            'Which choice completes the text with the most logical transition?',
            ['Consequently', 'Nevertheless', 'Similarly', 'Previously'],
            'A',
            'Câu 1 nêu cơ chế nguyên nhân (nước biển thấm vào hòa tan hạt vôi sống tạo tinh thể mới bít khe nứt). Câu 2 nêu HỆ QUẢ TRỰC TIẾP (bê tông biển cổ đại ngày càng bền và kín nước hơn theo hàng thế kỷ) → Quan hệ Nhân – Quả → "Consequently" (A)!',
            'Cơ chế hóa học ở câu 1 dẫn trực tiếp tới hệ quả bền vững hơn ở câu 2 → chọn từ nối nhân quả ("Consequently / Therefore").',
            [
                ('Đáp án đúng', 'Consequently kết nối chuẩn xác nguyên nhân tái kết tinh khoáng chất với hệ quả bê tông bền chắc hơn theo thời gian.'),
                ('False Contrast', 'Nevertheless chỉ sự trái ngược kỳ vọng — sai hoàn toàn hướng nhân quả.'),
                ('Wrong Relationship (Comparison)', 'Similarly chỉ sự tương đồng giữa hai đối tượng khác nhau.'),
                ('Wrong Relationship (Time)', 'Previously chỉ thời điểm trước đó — sai trình tự nhân quả.'),
            ]
        ),
        q_item(
            'm6_m1_q24', 24, 'Expression of Ideas', 'Transitions', 'Medium',
            '<p>Most nineteenth-century botanical atlases depicted flowering specimens isolated against stark white paper to emphasize stem and petal anatomy. ______, painter Marianne North rendered exotic plants tangled among native mosses, tree trunks, and hovering insects so viewers could grasp each species’ living ecological context.</p>',
            'Which choice completes the text with the most logical transition?',
            ['Therefore', 'By contrast', 'For example', 'Furthermore'],
            'B',
            'Câu 1: Phần lớn sách thực vật thế kỷ 19 vẽ mẫu hoa tách biệt trên nền giấy trắng trơn. Câu 2: Marianne North vẽ cây xen lẫn rêu, thân gỗ và côn trùng trong hệ sinh thái sống → Đối chiếu hai phong cách TRÁI NGƯỢC nhau giữa hai chủ thể → "By contrast" (B)!',
            'Đối chiếu trực diện cách làm của nhóm A ("Most atlases... stark white paper") vs. cách làm ngược lại của chủ thể B ("Marianne North... living ecological context") → chọn "By contrast"!',
            [
                ('Wrong Relationship (Cause-Effect)', 'Cách vẽ nền trắng không phải nguyên nhân khiến North vẽ bối cảnh sinh thái.'),
                ('Đáp án đúng', 'By contrast làm nổi bật sự đối lập sắc nét giữa chuẩn minh họa tách nền truyền thống và lối vẽ sinh thái toàn cảnh của North.'),
                ('Wrong Relationship (Example)', 'Phong cách của North trái ngược chứ không phải ví dụ cho sách nền trắng.'),
                ('Wrong Relationship (Addition)', 'Furthermore dùng để bổ sung ý cùng chiều, không phải tương phản.'),
            ]
        ),
        q_item(
            'm6_m1_q25', 25, 'Expression of Ideas', 'Transitions', 'Hard',
            '<p>To ease severe rush-hour crowding on metropolitan subway lines, Singapore’s transit authority did not rely solely on constructing costly new tunnels. ______, behavioral economists helped design an off-peak travel reward scheme offering free pre-7:45 a.m. trips and randomized commuter lotteries that smoothly shifted thousands of daily riders out of peak trains.</p>',
            'Which choice completes the text with the most logical transition?',
            ['Likewise', 'As a result', 'Still', 'Instead'],
            'D',
            'Câu 1 phủ định hướng đi đơn thuần ("did NOT rely solely on constructing costly new tunnels"). Câu 2 đưa giải pháp THAY THẾ về mặt kinh tế học hành vi (ưu đãi miễn phí giờ sớm + xổ số khuyến khích đi lệch giờ cao điểm) → Phủ định X, làm giải pháp thay thế Y = "Instead" (D)!',
            'Gặp khung "did not rely solely on X" ở câu 1 + biện pháp thay thế Y ở câu 2 → chốt ngay "Instead"!',
            [
                ('Wrong Relationship (Comparison)', 'Likewise chỉ sự tương đồng — sai vì câu 1 có phủ định.'),
                ('Wrong Relationship (Cause-Effect)', 'Việc không chỉ xây đường hầm mới không tự sinh ra chương trình xổ số giờ thấp điểm.'),
                ('Contrast Nuance Trap', 'Still (= Nevertheless) mang nghĩa nhượng bộ bất chấp, không thể hiện phương án thay thế cho vế phủ định.'),
                ('Đáp án đúng', 'Instead khớp tuyệt đối logic phủ định giải pháp cũ → triển khai giải pháp hành vi thay thế.'),
            ]
        ),

        # --- Q26-Q27: Expression of Ideas — Rhetorical Synthesis ---
        q_item(
            'm6_m1_q26', 26, 'Expression of Ideas', 'Rhetorical Synthesis', 'Medium',
            '''<p>While researching a topic, a student has taken the following notes:</p>
            <ul>
              <li>The Sogdian Ancient Letters are a collection of early fourth-century CE paper manuscripts discovered near Dunhuang, China, in 1907.</li>
              <li>Written in the Sogdian script, the letters record business correspondence among Central Asian merchants trading silk, wool, musk, and camphor.</li>
              <li>Overland communication between oasis cities like Samarkand and Luoyang often took months and faced banditry or political upheaval.</li>
              <li>To maintain commercial reliability across these distances, Sogdian merchants embedded tight-knit family agents in major hubs and tracked debts through detailed ledgers and stamped wax seals.</li>
            </ul>''',
            'The student wants to explain how Sogdian merchants maintained reliable trade across vast distances despite slow overland communication. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
            [
                'Because overland messages between Silk Road hubs could take months and face hazards, Sogdian merchants preserved trade reliability by stationing tight-knit family agents in key cities and tracking debts with detailed ledgers and stamped wax seals.',
                'Discovered near Dunhuang in 1907, the fourth-century Sogdian Ancient Letters are written on paper in the Sogdian script.',
                'Sogdian merchants traded high-value commodities including silk, wool, musk, and camphor between Central Asia and China.',
                'Political upheaval and banditry frequently delayed overland caravans traveling between Samarkand and Luoyang in the fourth century CE.'
            ],
            'A',
            'Goal-First SOP: Giải thích CÁCH THỨC thương nhân Sogdia duy trì độ tin cậy thương mại qua khoảng cách xa BẤT CHẤP liên lạc đường bộ chậm chạp ("explain HOW... maintained reliable trade... despite slow overland communication"). B chỉ nói địa điểm phát hiện; C chỉ liệt kê hàng hóa; D chỉ nêu khó khăn mà thiếu giải pháp. Duy nhất A nối đủ cả trở ngại liên lạc chậm + cơ chế bố trí đại lý gia đình, sổ nợ và dấu sáp niêm phong → Chọn A!',
            'Soi đúng từ khóa "how... despite" trong Goal: câu đúng phải có cả khó khăn đường dài VÀ giải pháp thực thi cụ thể.',
            [
                ('Đáp án đúng', 'Hoàn thành trọn vẹn mục tiêu: nêu bối cảnh liên lạc chậm trễ/rủi ro và giải thích rõ cách dùng đại lý gia đình, sổ kế toán và dấu sáp.'),
                ('Wrong Synthesis Goal', 'Chỉ nêu thời điểm và nơi phát hiện tập thư cổ.'),
                ('Wrong Synthesis Goal', 'Chỉ liệt kê mặt hàng giao dịch mà không giải thích cơ chế duy trì tin cậy.'),
                ('Incomplete Goal', 'Chỉ nêu khó khăn đường bộ mà bỏ quên hoàn toàn giải pháp của thương nhân.'),
            ]
        ),
        q_item(
            'm6_m1_q27', 27, 'Expression of Ideas', 'Rhetorical Synthesis', 'Hard',
            '''<p>While researching a topic, a student has taken the following notes:</p>
            <ul>
              <li>Brutalist public buildings erected in arid regions during the 1960s featured massive exposed reinforced-concrete walls.</li>
              <li>Exposed concrete absorbs solar heat rapidly and traps warmth indoors into the night, typically requiring energy-intensive mechanical air-conditioning.</li>
              <li>Vernacular desert houses across North Africa and Iran were built with thick earthen adobe walls, shaded interior courtyards, and rooftop windcatchers.</li>
              <li>These traditional vernacular features delay daytime heat transfer and flush warm air out naturally using nighttime breezes, minimizing artificial cooling needs.</li>
            </ul>''',
            'The student wants to contrast how Brutalist concrete buildings and traditional vernacular desert houses manage intense arid-climate heat. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
            [
                'Both Brutalist concrete public buildings from the 1960s and traditional vernacular desert houses from North Africa and Iran have been constructed in arid climates.',
                'Traditional vernacular desert houses use thick adobe walls, shaded courtyards, and windcatchers to keep interiors cool without heavy electricity use.',
                'Whereas Brutalist exposed-concrete buildings absorb solar heat and trap warmth indoors—requiring heavy mechanical air-conditioning—vernacular desert houses rely on adobe walls, shaded courtyards, and windcatchers to delay heat transfer and vent warm air naturally.',
                'Brutalist public buildings constructed during the 1960s are recognizable for their massive exposed reinforced-concrete facades.'
            ],
            'C',
            'Goal-First SOP: Nhấn mạnh SỰ TƯƠNG PHẢN ("contrast") trong CÁCH XỬ LÝ NHIỆT KHÍ HẬU KHÔ CẰN ("manage intense arid-climate heat") của CẢ HAI phong cách kiến trúc. A nêu điểm giống; B chỉ nói nhà bản địa; D chỉ tả diện mạo Brutalist. Duy nhất C dùng "Whereas..." đối chiếu trực tiếp hai cơ chế nhiệt trái ngược của cả hai loại công trình → Chọn C!',
            'Goal yêu cầu "contrast [Subject A] and [Subject B] on [Heat Management]" → bắt buộc phải nhắc đủ cả 2 đối tượng và cơ chế nhiệt trái chiều!',
            [
                ('Wrong Synthesis Goal', 'Nhấn mạnh điểm giống nhau (cùng xây ở vùng khô hạn) thay vì tương phản cách xử lý nhiệt.'),
                ('Single Subject Trap', 'Chỉ mô tả nhà bản địa mà bỏ qua hoàn toàn công trình Brutalist.'),
                ('Đáp án đúng', 'Đối chiếu sắc nét cơ chế tích nhiệt phụ thuộc điều hòa của bê tông Brutalist với cơ chế trì hoãn nhiệt và thông gió tự nhiên của nhà đất nung bản địa.'),
                ('Single Subject & Off-Criterion', 'Chỉ nhắc diện mạo bê tông thập niên 1960, không so sánh cơ chế nhiệt với kiến trúc bản địa.'),
            ]
        ),
    ]
