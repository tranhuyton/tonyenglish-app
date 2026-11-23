# -*- coding: utf-8 -*-
"""
Full-Length Adaptive Mock Test #6 — Module 2 LOWER/STANDARD Route (27 Qs, Easy/Medium, 32 min)
Exact College Board Digital SAT R&W Blueprint:
Q1-5: Words in Context | Q6-7: Text Structure/Purpose | Q8: Cross-Text
Q9-10: Central Ideas/Details | Q11-12: Evidence (Textual) | Q13-14: Evidence (Quantitative)
Q15: Inferences | Q16-19: Boundaries | Q20-22: Form/Structure/Sense
Q23-25: Transitions | Q26-27: Rhetorical Synthesis
"""

from sat_drills_1_1_and_2_1 import q_item
from sat_drills_5_4_to_5_5 import svg_bar_chart, html_table


def get_m2l_questions():
    return [
        # --- Q1-Q5: Craft and Structure — Words in Context (Easy / Medium) ---
        q_item(
            'm6_m2l_q1', 1, 'Craft and Structure', 'Words in Context', 'Easy',
            '<p>Ancient Roman engineers blended volcanic ash from the Bay of Naples with lime and seawater to construct harbor piers so ______ that many still stand unbroken against Mediterranean waves two thousand years later.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            ['fragile', 'durable', 'temporary', 'hollow'],
            'B',
            'Cause-Effect Clue: đứng vững không vỡ trước sóng biển Địa Trung Hải suốt 2.000 năm ("stand unbroken... two thousand years later") → BỀN BỈ / VỮNG CHẮC → "durable" (B).',
            'Kết quả "still stand unbroken two thousand years later" dẫn thẳng tới tính từ "durable" (bền bỉ lâu dài).',
            [
                ('Opposite Meaning', 'fragile = mong manh dễ vỡ — trái ngược hoàn toàn với "stand unbroken".'),
                ('Đáp án đúng', 'durable = bền bỉ chịu lực lâu dài — khớp hoàn hảo tuổi thọ hai thiên niên kỷ của cầu cảng La Mã.'),
                ('Opposite Meaning', 'temporary = tạm thời ngắn ngủi — trái ngược với 2.000 năm.'),
                ('Wrong Meaning', 'hollow = rỗng bên trong — không giải thích độ bền trước sóng biển.'),
            ]
        ),
        q_item(
            'm6_m2l_q2', 2, 'Craft and Structure', 'Words in Context', 'Easy',
            '<p>Working in the 1840s before commercial color photography existed, English botanist Anna Atkins placed pressed algae directly onto light-sensitive paper in sunlight to create ______ blue-and-white prints that recorded every tiny fernlike branch.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            ['careless', 'noisy', 'detailed', 'incomplete'],
            'C',
            'Mirror Clue: "recorded every tiny fernlike branch" (ghi lại từng nhánh tảo nhỏ xíu như lá dương xỉ) → CHI TIẾT, TỈ MỈ → "detailed" (C).',
            'Cụm "recorded every tiny fernlike branch" giải thích trực tiếp cho tính từ "detailed".',
            [
                ('Opposite Meaning', 'careless = cẩu thả — trái với việc ghi lại từng nhánh nhỏ li ti.'),
                ('Wrong Context', 'noisy = ồn ào — không dùng để mô tả bản in ảnh thực vật.'),
                ('Đáp án đúng', 'detailed = giàu chi tiết sắc nét — khớp 100% với khả năng lưu giữ từng nhánh tảo siêu nhỏ.'),
                ('Opposite Meaning', 'incomplete = thiếu sót chưa đủ — trái nghĩa với "every tiny branch".'),
            ]
        ),
        q_item(
            'm6_m2l_q3', 3, 'Craft and Structure', 'Words in Context', 'Easy',
            '<p>When crossing arid stretches of Central Asia where clean drinking water was ______, medieval Sogdian merchant caravans planned every stage of their journey carefully around walled oasis towns and deep roadside wells.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            ['scarce', 'plentiful', 'wasteful', 'familiar'],
            'A',
            'Cause-Effect Clue: vùng đất khô cằn ("arid stretches") buộc thương đoàn phải vạch lộ trình cẩn thận quanh các ốc đảo và giếng sâu → nước uống sạch KHAN HIẾM → "scarce" (A).',
            'Từ khóa "arid stretches" (vùng khô hạn) + "planned carefully around oasis towns and deep wells" ⇒ nước uống rất khan hiếm ("scarce").',
            [
                ('Đáp án đúng', 'scarce = khan hiếm, ít ỏi — khớp hoàn toàn với bối cảnh sa mạc khô hạn phải bám theo giếng và ốc đảo.'),
                ('Opposite Meaning', 'plentiful = dồi dào phong phú — trái ngược hoàn toàn với "arid stretches".'),
                ('Wrong Context', 'wasteful = lãng phí — không dùng để mô tả nguồn nước tự nhiên trong sa mạc.'),
                ('Wrong Meaning', 'familiar = quen thuộc — không giải thích lý do phải bám chặt theo giếng nước.'),
            ]
        ),
        q_item(
            'm6_m2l_q4', 4, 'Craft and Structure', 'Words in Context', 'Medium',
            '<p>Because radio signals from navigation satellites cannot penetrate deep ocean water or underground mines, physicists are building compact optical atomic clocks that can ______ satellite GPS systems whenever crews travel out of signal range.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            ['confuse', 'dismantle', 'prohibit', 'supplement'],
            'D',
            'Cause-Effect Clue: tín hiệu GPS vệ tinh không xuyên qua đáy biển sâu hay hầm mỏ → đồng hồ nguyên tử quang học gọn nhẹ giúp BỔ TRỢ / HỖ TRỢ THÊM cho hệ thống GPS khi mất sóng → "supplement" (D).',
            'Cơ chế hỗ trợ bổ sung khi hệ thống chính mất tín hiệu → chọn động từ "supplement" (bổ sung, bổ trợ).',
            [
                ('Wrong Tone', 'confuse = gây nhầm lẫn — trái ngược mục tiêu hỗ trợ định vị chính xác.'),
                ('Wrong Meaning', 'dismantle = tháo dỡ — đồng hồ không tháo dỡ hệ thống vệ tinh.'),
                ('Wrong Meaning', 'prohibit = ngăn cấm — sai logic kỹ thuật.'),
                ('Đáp án đúng', 'supplement = bổ sung, hỗ trợ bù đắp khoảng trống khi tín hiệu vệ tinh bị chắn dưới biển sâu hoặc hầm mỏ.'),
            ]
        ),
        q_item(
            'm6_m2l_q5', 5, 'Craft and Structure', 'Words in Context', 'Medium',
            '<p>Although the glowing mushroom caps sprouting on damp forest logs wither within a few short days, the hidden web of underground fungal threads nourishing them can ______ for decades beneath the soil, connecting the roots of neighboring trees year after year.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            ['persist', 'vanish', 'hesitate', 'shatter'],
            'A',
            'Contrast Clue: "Although... wither within a few short days" (tuy tai nấm nhanh héo trong vài ngày) ↔ mạng sợi nấm ngầm có thể TỒN TẠI BỀN BỈ hàng thập kỷ ("for decades... year after year") → "persist" (A).',
            'Đối lập trực tiếp với "wither within a few short days" + cụm "for decades... year after year" → chọn "persist" (tồn tại bền bỉ).',
            [
                ('Đáp án đúng', 'persist = tồn tại kéo dài, duy trì bền bỉ qua nhiều thập kỷ — đối lập hoàn hảo với "wither within a few short days".'),
                ('Opposite Meaning', 'vanish = biến mất nhanh chóng — trùng chiều với "wither", sai sau "Although".'),
                ('Wrong Context', 'hesitate = do dự chần chừ — chỉ dùng cho tâm lý con người.'),
                ('Wrong Meaning', 'shatter = vỡ tan tành — sai ngữ cảnh sợi nấm ngầm.'),
            ]
        ),

        # --- Q6-Q7: Craft and Structure — Text Structure and Purpose ---
        q_item(
            'm6_m2l_q6', 6, 'Craft and Structure', 'Text Structure and Purpose', 'Easy',
            '<p>Traditional adobe houses in Iran’s central desert maintain comfortable indoor temperatures without electric air-conditioning largely because of their thick earthen walls. Throughout the blazing afternoon, dense sun-dried clay slowly absorbs outdoor heat before it can reach interior rooms. <u>After sunset, when desert air cools sharply, those same thick walls release their stored warmth outward into the night sky, resetting the home’s cool interior for the next morning.</u></p>',
            'Which choice best describes the function of the underlined sentence in the text as a whole?',
            [
                'It argues that traditional adobe houses become uncomfortably hot after sunset during winter months.',
                'It compares the price of sun-dried clay bricks with the cost of electric air-conditioning units.',
                'It explains how thick adobe walls shed absorbed daytime heat overnight to prepare the house for the following day.',
                'It criticizes modern Iranian architects for building homes with thin glass windows.'
            ],
            'C',
            'Câu 2 mô tả nửa đầu chu kỳ ban ngày (tường đất dày hấp thụ chậm sức nóng chiều). Câu 3 gạch chân mô tả nửa sau chu kỳ BAN ĐÊM (sau hoàng hôn, tường tỏa ngược nhiệt ra trời đêm để làm mát lại cho sáng hôm sau) → Chọn C!',
            'Quan sát trình tự thời gian ngày → đêm: Câu 2 ("Throughout the blazing afternoon") → Câu 3 gạch chân ("After sunset... release their stored warmth... resetting... for the next morning").',
            [
                ('Contradiction', 'Câu gạch chân nói tường tỏa nhiệt RA NGOÀI trời đêm giúp căn nhà mát trở lại, không nói trong nhà nóng bức.'),
                ('Out of Scope', 'Không đề cập chi phí gạch đất nung hay giá máy điều hòa.'),
                ('Đáp án đúng', 'Mô tả chính xác vai trò xả nhiệt ban đêm của tường đất dày để chuẩn bị độ mát cho ngày hôm sau.'),
                ('Out of Scope', 'Không nhắc tới kiến trúc sư hiện đại hay cửa kính.'),
            ]
        ),
        q_item(
            'm6_m2l_q7', 7, 'Craft and Structure', 'Text Structure and Purpose', 'Medium',
            '<p><i>The following text is adapted from a fictional 1904 short story. Ticket clerk Matteo is watching commuters board the city’s newly opened electric underground railway during its first rainy Monday rush hour.</i><br/>At seven o’clock, passengers stepped down the tiled stairwell with cautious glances at the vaulted tunnel ceiling, clutching damp umbrellas as if unsure whether an iron train belonged beneath the boulevard. Yet twenty minutes later, as bright carriages glided silently past the clogged horse-drawn traffic overhead and emptied smiling office workers dry-shoed into the financial square, Matteo heard one skeptical shopkeeper laugh aloud and promise never to wait for a muddy streetcar again.</p>',
            'Which choice best states the main purpose of the text?',
            [
                'To explain the electrical engineering principles that powered early twentieth-century subway trains.',
                'To illustrate how commuters’ initial hesitation toward the new underground railway quickly turned into cheerful approval once they experienced its smooth convenience.',
                'To warn that underground railway tunnels in 1904 frequently flooded during rainy Monday mornings.',
                'To criticize streetcar drivers for failing to clear horse-drawn traffic from the financial square.'
            ],
            'B',
            'Câu 1 khắc họa sự dè dặt e ngại ban đầu của hành khách ("cautious glances... as if unsure"). Từ chữ "Yet", hành khách mỉm cười khô ráo tới quảng trường tài chính và một chủ tiệm vốn hoài nghi bật cười thề không bao giờ chờ xe điện bùn lầy nữa → Chuyển biến cảm xúc từ ngần ngại sang hài lòng phấn khởi → Chọn B!',
            'Khóa bước ngoặt cảm xúc qua từ "Yet": cautious glances / skeptical (ban đầu dè dặt) → smiling / laugh aloud / promise never to go back (vui vẻ ủng hộ).',
            [
                ('Out of Scope', 'Không giải thích nguyên lý kỹ thuật điện của tàu điện ngầm.'),
                ('Đáp án đúng', 'Tóm gọn trọn vẹn bước chuyển tâm lý từ e dè ban đầu sang thích thú đón nhận nhờ sự êm ái và tiện lợi.'),
                ('Contradiction', 'Hành khách đến nơi hoàn toàn khô giày ("dry-shoed"), hầm không hề bị ngập.'),
                ('Out of Scope', 'Không chỉ trích người lái xe điện mặt đất.'),
            ]
        ),

        # --- Q8: Craft and Structure — Cross-Text Connections ---
        q_item(
            'm6_m2l_q8', 8, 'Craft and Structure', 'Cross-Text Connections', 'Medium',
            '<p><b>Text 1</b><br/>Science historian Dr. David Mercer writes that women hired as observatory "computers" during the late nineteenth century performed strictly mechanical arithmetic—tabulating star coordinates recorded by male telescope operators—and seldom made independent contributions to astronomical discovery.</p><p><b>Text 2</b><br/>Archival researcher Dr. Claire Osei highlights the career of Scottish-born astronomer Williamina Fleming, who began as a copyist at Harvard Observatory in 1881. Examining thousands of photographic star spectra, Fleming created the widely adopted Draper letter-classification system for stellar temperatures and independently discovered more than three hundred variable stars, ten novae, and the famous Horsehead Nebula.</p>',
            'Based on the texts, how would Dr. Claire Osei (Text 2) most likely respond to Dr. David Mercer’s claim (Text 1)?',
            [
                'By agreeing that Williamina Fleming worked solely on repetitive arithmetic and never examined stellar photographs.',
                'By arguing that male telescope operators at Harvard Observatory refused to record star coordinates after 1881.',
                'By suggesting that the Horsehead Nebula was discovered centuries before photographic spectroscopy was invented.',
                'By pointing out that Williamina Fleming’s classification system and hundreds of celestial discoveries show that some women observatory assistants made major original scientific breakthroughs.'
            ],
            'D',
            'Text 1 khẳng định các nữ "máy tính" ở đài thiên văn chỉ làm số học máy móc và hiếm khi có đóng góp khoa học độc lập. Text 2 đưa ví dụ phản chứng hùng hồn về Williamina Fleming (sáng tạo hệ phân loại phổ sao Draper + độc lập phát hiện hơn 300 sao biến quang, 10 sao mới và Tinh vân Đầu Ngựa) → Phản bác trực tiếp bằng bằng chứng đóng góp đột phá độc lập → Chọn D!',
            'Text 1 đưa nhận định khái quát hạ thấp vai trò ("seldom made independent contributions"); Text 2 đưa trường hợp thực tế xuất sắc phản chứng → chọn D!',
            [
                ('Contradiction', 'Text 2 nêu rõ Fleming xem hàng nghìn ảnh phổ sao và tạo ra phát kiến độc lập lớn.'),
                ('Out of Scope', 'Text 2 không nói các nhà thiên văn nam ngừng ghi tọa độ sao.'),
                ('Contradiction', 'Text 2 cho thấy chính Fleming phát hiện Tinh vân Đầu Ngựa qua ảnh phổ sao.'),
                ('Đáp án đúng', 'Dùng trực tiếp hệ phân loại Draper và hàng trăm phát hiện thiên văn của Fleming để bác bỏ nhận định hạn hẹp của Mercer.'),
            ]
        ),

        # --- Q9-Q10: Information and Ideas — Central Ideas and Details ---
        q_item(
            'm6_m2l_q9', 9, 'Information and Ideas', 'Central Ideas and Details', 'Easy',
            '<p><i>The following excerpt is from an original poem titled “Courtyard at Dusk.”</i></p><p style="margin-left:18px;font-style:italic;">Behind the whitewashed mudbrick wall,<br/>The afternoon’s fierce glare subsides;<br/>Across the shallow limestone pool,<br/>A silver evening ripple glides.<br/>Down from the tall clay tower above,<br/>A steady breeze begins to pour,<br/>And brings the scent of watered figs<br/>Across the shaded courtyard floor.</p>',
            'Which choice best states the main idea of the poem?',
            [
                'As evening arrives, a sheltered earthen courtyard grows cool and peaceful through still water, shade, and a fresh breeze descending from its rooftop tower.',
                'A sudden desert sandstorm knocks down a whitewashed mudbrick wall and dries up a limestone garden pool.',
                'Residents abandon their mudbrick courtyard at dusk because the tall clay tower blocks the evening wind.',
                'Wild fig trees grow only on the roofs of tall clay towers across desert cities.'
            ],
            'A',
            'Toàn bài thơ khắc họa khung cảnh sân trong kiến trúc đất nung lúc hoàng hôn: ánh nắng gắt dịu xuống sau bức tường đất quét vôi trắng, mặt hồ đá vôi gợn sóng bạc, làn gió mát từ tháp đất trên cao ùa xuống mang hương sung tưới nước khắp sân râm → Chọn A!',
            'Gom trọn các chi tiết thơ yên bình: whitewashed mudbrick wall + glare subsides + limestone pool + breeze pouring down from clay tower = sân trong mát dịu lúc chiều tà (A).',
            [
                ('Đáp án đúng', 'Tóm gọn chính xác khung cảnh thanh bình, mát mẻ của sân đất nung truyền thống lúc chập tối.'),
                ('Contradiction', 'Không có bão cát, tường sập hay hồ cạn — ngược lại mặt hồ còn gợn sóng dịu mát.'),
                ('Reversed Logic', 'Tháp đất cao DẪN làn gió mát ùa xuống ("Down from the tall clay tower... a steady breeze begins to pour"), không phải chắn gió.'),
                ('Literal Misreading', 'Cơn gió mang hương thơm cây sung được tưới nước băng qua sân chứ không nói cây sung chỉ mọc trên nóc tháp.'),
            ]
        ),
        q_item(
            'm6_m2l_q10', 10, 'Information and Ideas', 'Central Ideas and Details', 'Medium',
            '<p>When London’s transport authority introduced contactless bank-card payments across its subway and rail gates in 2014, researchers noticed an immediate surge in off-peak ridership among tourists and occasional suburban visitors. Surveys revealed that unfamiliar travelers previously avoided short rail hops because deciphering complex multi-zone fare charts at crowded ticket machines felt stressful; simply tapping an ordinary credit or debit card removed that mental hurdle completely.</p>',
            'According to the text, why did contactless bank-card payments increase off-peak subway trips among occasional visitors?',
            [
                'Contactless bank cards reduced ticket prices to zero during weekends and holidays.',
                'Ticket machines in London were permanently disconnected from electric power in 2014.',
                'Tapping a familiar payment card eliminated the stress of figuring out complicated multi-zone fare charts at busy ticket kiosks.',
                'Suburban visitors were legally required to ride subway trains at least twice each week.'
            ],
            'C',
            'Câu hỏi Specific Detail: Tìm đúng nguyên nhân trong câu cuối → "unfamiliar travelers previously avoided short rail hops because deciphering complex multi-zone fare charts at crowded ticket machines felt stressful; simply tapping an ordinary credit or debit card removed that mental hurdle completely" → Paraphrase trực tiếp ở C!',
            'Tìm cụm "because..." và vế giải quyết "removed that mental hurdle" để chọn đáp án khớp nghĩa sát nhất.',
            [
                ('Out of Scope / Distortion', 'Bài không nói chạm thẻ ngân hàng làm giá vé giảm về 0 vào cuối tuần.'),
                ('Out of Scope', 'Không nói các máy bán vé bị ngắt điện vĩnh viễn.'),
                ('Đáp án đúng', 'Paraphrase trực tiếp: chạm thẻ quen thuộc giúp xóa bỏ rào cản tâm lý phải giải mã bảng giá nhiều khu vực tại máy bán vé đông đúc.'),
                ('Out of Scope', 'Không có quy định pháp luật bắt buộc cư dân ngoại ô đi tàu điện.'),
            ]
        ),

        # --- Q11-Q12: Information and Ideas — Command of Evidence (Textual) ---
        q_item(
            'm6_m2l_q11', 11, 'Information and Ideas', 'Command of Evidence (Textual)', 'Medium',
            '<p>Forest botanist Dr. Elena Gomez hypothesized that young ponderosa pine seedlings rely heavily on native mycorrhizal fungi to extract scarce phosphorus from rocky mountain soils, meaning seedlings deprived of those fungi will struggle to absorb phosphorus and grow more slowly.</p>',
            'Which finding, if true, would most directly support Dr. Elena Gomez’s hypothesis?',
            [
                'Mature ponderosa pine trees typically develop thicker fire-resistant bark than lodgepole pines growing at higher elevations.',
                'After sixteen weeks in identical low-phosphorus mountain soil, pine seedlings inoculated with native mycorrhizal fungi absorbed nearly three times as much phosphorus and grew 40 percent taller than seedlings raised in sterilized fungus-free soil.',
                'Wildflowers blooming along sunny mountain meadows attract more honeybees during July than during September.',
                'Rocky mountain soils in northern Arizona contain slightly higher iron levels than sandy soils along the Pacific coast.'
            ],
            'B',
            'Khóa giả thuyết Gomez: Cây thông non cần nấm rễ mycorrhizal để hút phốt pho khan hiếm và sinh trưởng nhanh hơn; thiếu nấm sẽ hút ít phốt pho và lớn chậm. Đáp án B đưa đúng thí nghiệm so sánh giữa cây thông có nấm bản địa (hút phốt pho gấp gần 3 lần, cao hơn 40%) với cây trong đất tiệt trùng không nấm → Chọn B!',
            'Tìm đáp án chứa đủ cả 3 biến của giả thuyết: `pine seedlings` + `with vs. without mycorrhizal fungi` + `phosphorus absorption & growth`!',
            [
                ('Irrelevant Subject', 'Độ dày vỏ chống cháy của thông trưởng thành không kiểm chứng vai trò hút phốt pho của nấm rễ ở cây con.'),
                ('Đáp án đúng', 'So sánh trực tiếp cây non có nấm vs không nấm trong cùng đất nghèo phốt pho, chứng minh cả lượng phốt pho hấp thụ lẫn tốc độ sinh trưởng vượt trội.'),
                ('Irrelevant Subject', 'Hoa dại và ong mật không liên quan tới thông non hay nấm rễ.'),
                ('Adjacent Topic Drift', 'Hàm lượng sắt trong đất không kiểm chứng vai trò của nấm mycorrhizal với phốt pho.'),
            ]
        ),
        q_item(
            'm6_m2l_q12', 12, 'Information and Ideas', 'Command of Evidence (Textual)', 'Medium',
            '<p>In a discussion of the 1922 historical novel <i>The Silk Ledger</i>, a literature teacher states that teenage merchant apprentice Davud feels dazzled and overwhelmed by the bewildering mix of languages and exotic merchandise during his very first afternoon in the Samarkand marketplace.</p>',
            'Which quotation from Davud in <i>The Silk Ledger</i> most effectively illustrates the teacher’s statement?',
            [
                '“Before leaving our home village, my father packed two spare pairs of leather boots and a small brass compass inside my saddlebag.”',
                '“Our camel caravan crossed the shallow ford just before sunrise without losing a single bale of raw wool.”',
                '“Every autumn the oasis farmers repair their earthen irrigation ditches before the mountain snowmelt begins.”',
                '“I stopped breathless between towering bolts of crimson Tang silk and jars of Indian pepper, my ears spinning from bargains shouted simultaneously in four tongues I had never heard before.”'
            ],
            'D',
            'Checklist 2 chi tiết của nhận định: [1] Choáng ngợp, hoa mắt ("dazzled and overwhelmed") + [2] Hỗn hợp ngôn ngữ và hàng hóa kỳ lạ ở chợ Samarkand ("bewildering mix of languages and exotic merchandise"). Duy nhất D miêu tả sống động cảm giác nín thở quay cuồng giữa cuộn lụa đỏ nhà Đường, hũ tiêu Ấn Độ và tiếng mặc cả bằng 4 thứ tiếng lạ → Chọn D!',
            'Đối chiếu từ khóa trong Claim: `overwhelmed` = "breathless / ears spinning"; `languages & exotic merchandise` = "crimson Tang silk, Indian pepper, four tongues"!',
            [
                ('Irrelevant Detail', 'Chỉ kể chuyện bố chuẩn bị hành lý ở quê nhà trước khi khởi hành.'),
                ('Irrelevant Detail', 'Chỉ kể đoàn lạc đà vượt suối lúc bình minh.'),
                ('Irrelevant Detail', 'Chỉ nói nông dân sửa kênh tưới tiêu mùa thu.'),
                ('Đáp án đúng', 'Minh họa trọn vẹn cảm giác choáng ngợp giữa hàng hóa ngoại lai và bốn ngôn ngữ xa lạ vang lên cùng lúc tại chợ Samarkand.'),
            ]
        ),

        # --- Q13-Q14: Information and Ideas — Command of Evidence (Quantitative) ---
        q_item(
            'm6_m2l_q13', 13, 'Information and Ideas', 'Command of Evidence (Quantitative)', 'Easy',
            svg_bar_chart(
                'Share of Commuters Rating Platform Wait Experience as "Comfortable" (%) by Station Upgrade',
                ['0%', '20%', '40%', '60%', '80%', '100%'],
                [('Baseline (None)', 34, '34%'), ('Shade Canopy', 52, '52%'), ('Transfer Maps', 63, '63%'), ('Arrival Board', 84, '84%')],
                100
            ) + '<p>After testing several low-cost station improvements across an urban commuter rail network, transit planners concluded that installing a digital real-time arrival board raises commuter comfort ratings by more than twice as many percentage points above baseline as adding an overhead shade canopy does.</p>',
            'Which choice most effectively uses data from the graph to support the transit planners’ conclusion?',
            [
                'Installing a real-time arrival board raised commuter comfort ratings by 50 percentage points above baseline (from 34% to 84%), more than double the 18-percentage-point gain achieved by adding a shade canopy (from 34% to 52%).',
                'Clear transfer maps raised the percentage of commuters rating their platform wait as comfortable to 63%.',
                'Only 34% of surveyed commuters rated their waiting experience as comfortable on baseline platforms without upgrades.',
                'All three tested station upgrades received higher comfort ratings than the baseline platform did.'
            ],
            'A',
            'Kiểm tra phép trừ so sánh với Baseline (34%): Bảng báo giờ tàu (`Arrival Board`) đạt 84% → tăng `84% − 34% = +50 điểm %`. Mái che nắng (`Shade Canopy`) đạt 52% → tăng `52% − 34% = +18 điểm %`. Rõ ràng `50 > 2 × 18 (36)` (hơn gấp đôi)! Duy nhất A nêu đủ và đối chiếu chính xác hai mức tăng +50 điểm % và +18 điểm % → Chọn A!',
            'Đọc kỹ hai đối tượng được so sánh với mốc cơ sở Baseline (34%): Arrival Board (+50%) vs. Shade Canopy (+18%) → khớp 100% ở A!',
            [
                ('Đáp án đúng', 'Tính chuẩn xác mức tăng của cả hai hạng mục so với mức nền 34% (+50 điểm % > gấp đôi +18 điểm %).'),
                ('True Data / Wrong Subject', 'Chỉ nhắc bảng bản đồ chuyển tuyến (63%), không liên quan tới so sánh bảng báo giờ và mái che.'),
                ('Incomplete Data', 'Chỉ nêu mốc cơ sở 34% mà không so sánh hai hạng mục nâng cấp.'),
                ('Too Broad', 'Quá chung chung, không chứng minh tỷ lệ hơn gấp đôi giữa bảng báo giờ và mái che.'),
            ]
        ),
        q_item(
            'm6_m2l_q14', 14, 'Information and Ideas', 'Command of Evidence (Quantitative)', 'Medium',
            html_table(
                'Table 1. Five-Year Saltwater Exposure Results for Four Coastal Concrete Test Blocks',
                ['Concrete Type', 'Contains Volcanic Ash?', 'Mean Crack Width (5 Years)', 'Saltwater Seepage Rate'],
                [
                    ['Standard Portland', 'No', '1.8 mm', '42 mL/day'],
                    ['High-Steel Reinforced', 'No', '1.5 mm', '36 mL/day'],
                    ['Low-Lime Pozzolana', 'Yes', '0.9 mm', '19 mL/day'],
                    ['Hot-Mixed Roman Replica', 'Yes', '0.1 mm', '3 mL/day'],
                ]
            ) + '<p>An engineering student reviewing the five-year test results claims that concrete mixtures containing volcanic ash resist marine cracking and block saltwater seepage far more effectively than concrete mixtures made without volcanic ash.</p>',
            'Which choice most effectively uses data from the table to support the student’s claim?',
            [
                'Standard Portland concrete contained no volcanic ash and showed a mean crack width of 1.8 mm after five years in saltwater.',
                'Hot-Mixed Roman Replica concrete was tested over the exact same five-year period as Standard Portland concrete.',
                'Both volcanic-ash mixtures had much narrower cracks and lower seepage (0.9 mm and 19 mL/day for Low-Lime Pozzolana; 0.1 mm and 3 mL/day for Hot-Mixed Roman Replica) than either ash-free mixture (1.8 mm and 42 mL/day; 1.5 mm and 36 mL/day).',
                'High-Steel Reinforced concrete had slightly narrower cracks (1.5 mm) and less seepage (36 mL/day) than Standard Portland concrete (1.8 mm and 42 mL/day).'
            ],
            'C',
            'Claim so sánh CẢ HAI NHÓM: nhóm CÓ tro núi lửa (`Contains Volcanic Ash = Yes`: Low-Lime Pozzolana & Hot-Mixed Roman Replica) vs. nhóm KHÔNG CÓ tro núi lửa (`No`: Standard Portland & High-Steel Reinforced) trên CẢ HAI CHỈ SỐ (độ rộng vết nứt & tốc độ thấm nước biển). Duy nhất C trích dẫn đầy đủ số liệu của cả hai nhóm trên cả hai tiêu chí → Chọn C!',
            'Khi Claim so sánh nhóm A (có tro) với nhóm B (không tro) về 2 chỉ số, đáp án đúng phải đối chiếu số liệu của CẢ hai nhóm thay vì chỉ nói 1 dòng hoặc so sánh nội bộ 1 nhóm!',
            [
                ('Incomplete Data', 'Chỉ nêu số liệu của Standard Portland, không nhắc gì đến các mẫu có tro núi lửa.'),
                ('Irrelevant Detail', 'Chỉ nói thời gian thử nghiệm 5 năm giống nhau, không đưa số liệu vết nứt hay độ thấm.'),
                ('Đáp án đúng', 'Đối chiếu trọn vẹn cả 2 mẫu có tro (0,9 mm / 19 mL và 0,1 mm / 3 mL) với cả 2 mẫu không tro (1,8 mm / 42 mL và 1,5 mm / 36 mL).'),
                ('Wrong Comparison', 'Chỉ so sánh nội bộ hai mẫu không chứa tro núi lửa với nhau.'),
            ]
        ),

        # --- Q15: Information and Ideas — Inferences ---
        q_item(
            'm6_m2l_q15', 15, 'Information and Ideas', 'Inferences', 'Medium',
            '<p>Centuries before papermaking reached Western Europe, Silk Road Sogdian merchants adopted durable, lightweight mulberry-bark paper from China for their commercial correspondence. Because paper sheets weighed only a tiny fraction as much as clay tablets or wooden tallies and could be rolled compactly inside leather courier pouches, historians conclude that the Sogdians’ embrace of paper ______</p>',
            'Which choice most logically completes the text?',
            [
                'prevented Chinese workshops from ever selling paper to merchants in Samarkand.',
                'made it far more practical for trading families to send detailed business records and instructions across distant caravan hubs.',
                'caused medieval European rulers to outlaw the use of leather courier pouches.',
                'eliminated the need for camel caravans to carry silk or spices along overland desert roads.'
            ],
            'B',
            'Ghép 2 tiền đề: Giấy vỏ dâu tằm bền, cực nhẹ (nhẹ hơn hẳn bảng đất sét hay thẻ gỗ) và cuộn gọn được trong túi da của người đưa thư ⇒ Hệ quả trực tiếp 1-Millimeter: giúp các gia đình thương nhân gửi sổ sách và chỉ dẫn kinh doanh chi tiết qua các chặng thương đoàn xa xôi thuận tiện hơn rất nhiều → Chọn B!',
            'Ưu điểm vật lý "lightweight + rolled compactly inside courier pouches" dẫn trực tiếp tới lợi ích vận chuyển thư tín/hồ sơ thương mại đường xa (B)!',
            [
                ('Contradiction', 'Thương nhân Sogdia tiếp nhận giấy từ Trung Hoa, không hề ngăn xưởng Trung Hoa bán giấy.'),
                ('Đáp án đúng', 'Suy diễn tự nhiên, bám sát dữ kiện trọng lượng nhẹ và dễ đóng gói trong túi đưa thư đường dài.'),
                ('Out of Scope', 'Không có thông tin nào về việc các vua châu Âu cấm túi da.'),
                ('Absurd / Out of Scope', 'Giấy chỉ hỗ trợ ghi chép thương mại chứ không thay thế việc vận chuyển lụa và gia vị.'),
            ]
        ),

        # --- Q16-Q19: Standard English Conventions — Boundaries ---
        q_item(
            'm6_m2l_q16', 16, 'Standard English Conventions', 'Boundaries', 'Easy',
            '<p>Inside an optical lattice clock, trapped strontium atoms absorb precisely tuned red laser ______ physicists count those steady light oscillations to measure time with remarkable accuracy.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['light,', 'light and', 'light', 'light, and'],
            'D',
            'Vế 1 là IC hoàn chỉnh ("Inside an optical lattice clock, trapped strontium atoms absorb precisely tuned red laser light"). Vế 2 cũng là IC hoàn chỉnh ("physicists count those steady light oscillations..."). Nối 2 IC bằng liên từ FANBOYS (`and`) BẮT BUỘC có dấu phẩy đứng trước `and` (`light, and`) → Chọn D!',
            'Công thức chuẩn: `IC, + FANBOYS + IC`. Loại A (Comma Splice), B (thiếu phẩy trước `and`), C (Run-on)!',
            [
                ('Comma Splice', 'Chỉ dùng một dấu phẩy để nối hai mệnh đề độc lập là sai.'),
                ('Missing Comma Before FANBOYS', 'Khi nối hai mệnh đề độc lập bằng "and", bắt buộc có dấu phẩy trước "and".'),
                ('Run-On Sentence', 'Không có dấu câu hoặc liên từ giữa hai mệnh đề độc lập.'),
                ('Đáp án đúng', 'Cấu trúc `IC, and IC` chuẩn mực ngữ pháp tiếng Anh.'),
            ]
        ),
        q_item(
            'm6_m2l_q17', 17, 'Standard English Conventions', 'Boundaries', 'Easy',
            '<p>In 1843, English botanist Anna Atkins published the world’s first photographically illustrated book, filling its hand-bound pages with bright blue cyanotype prints of three coastal plant ______ brown kelp, lacy red algae, and feathery green sea lettuce.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['groups;', 'groups.', 'groups:', 'groups, and'],
            'C',
            'Vế trước chỗ trống là 1 IC hoàn chỉnh kết thúc bằng cụm giới thiệu danh sách ("three coastal plant groups"). Vế sau ("brown kelp, lacy red algae, and feathery green sea lettuce") là danh sách 3 cụm danh từ (KHÔNG phải IC) → Chọn dấu hai chấm (`groups:`) = C!',
            'IC hoàn chỉnh + danh sách liệt kê không có động từ chia thì → dùng dấu hai chấm (`:`); loại `;` và `.` vì tạo Fragment!',
            [
                ('Semicolon + Fragment', 'Danh sách phía sau không phải IC nên cấm dùng dấu chấm phẩy.'),
                ('Period + Fragment', 'Dấu chấm tách danh sách danh từ thành mảnh câu cụt.'),
                ('Đáp án đúng', 'Dấu hai chấm (:) giới thiệu chuẩn xác danh sách 3 nhóm thực vật biển sau IC.'),
                ('Comma + FANBOYS + Fragment', 'Thêm ", and" làm gãy cấu trúc liệt kê giải thích của "three coastal plant groups".'),
            ]
        ),
        q_item(
            'm6_m2l_q18', 18, 'Standard English Conventions', 'Boundaries', 'Medium',
            '<p>Designed by architect Louis Kahn, the National Assembly Building in ______ uses deep geometric wall cutouts to shade interior hallways from harsh afternoon glare.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['Dhaka, a landmark of tropical concrete modernism,', 'Dhaka a landmark of tropical concrete modernism,', 'Dhaka, a landmark of tropical concrete modernism', 'Dhaka; a landmark of tropical concrete modernism;'],
            'A',
            'Cụm đồng vị giải thích thêm ("a landmark of tropical concrete modernism") nằm xen giữa Chủ ngữ ("the National Assembly Building in Dhaka") và Động từ chính ("uses") → Phải bọc kín bằng CẶP DẤU PHẨY ở cả đầu và cuối → Chọn A!',
            'Quy tắc xóa thử Non-Essential: Bỏ cụm nằm giữa hai dấu phẩy, câu còn lại "the National Assembly Building in Dhaka uses..." vẫn trơn tru hoàn chỉnh → Bắt buộc 2 dấu phẩy cân xứng!',
            [
                ('Đáp án đúng', 'Đặt đúng cặp dấu phẩy hai đầu cho cụm đồng vị bổ sung nằm giữa chủ ngữ và động từ "uses".'),
                ('Missing Opening Comma', 'Thiếu dấu phẩy mở ngay sau "Dhaka".'),
                ('Missing Closing Comma', 'Thiếu dấu phẩy đóng trước động từ chính "uses".'),
                ('Semicolon Trap', 'Cấm dùng cặp chấm phẩy để tách cụm đồng vị đơn giản giữa chủ ngữ và động từ.'),
            ]
        ),
        q_item(
            'm6_m2l_q19', 19, 'Standard English Conventions', 'Boundaries', 'Medium',
            '<p>During humid monsoon evenings, clusters of glowing <i>Mycena</i> mushrooms cover fallen bamboo stems across southern ______ local naturalists often lead small evening groups along forest trails to observe their soft emerald light.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['Japan,', 'Japan;', 'Japan', 'Japan, and because'],
            'B',
            'Vế 1 là IC hoàn chỉnh ("During humid monsoon evenings, clusters... across southern Japan"). Vế 2 cũng là IC hoàn chỉnh ("local naturalists often lead..."). Giữa 2 IC → dùng dấu chấm phẩy (`Japan;`) = B!',
            'Kiểm tra IC + IC: Loại Comma Splice (A), Run-on (C), và mảnh phụ treo lơ lửng `, and because` (D) → Chốt dấu chấm phẩy (B)!',
            [
                ('Comma Splice', 'Một dấu phẩy không đủ nối hai mệnh đề độc lập.'),
                ('Đáp án đúng', 'Dấu chấm phẩy (;) ngăn cách chuẩn xác hai mệnh đề độc lập liên quan trực tiếp.'),
                ('Run-On Sentence', 'Không có dấu câu phân tách hai IC.'),
                ('Fragment / Subordinate Trap', 'Thêm "and because" biến vế 2 thành mệnh đề phụ không có mệnh đề chính đi kèm.'),
            ]
        ),

        # --- Q20-Q22: Standard English Conventions — Form, Structure, and Sense ---
        q_item(
            'm6_m2l_q20', 20, 'Standard English Conventions', 'Form, Structure, and Sense', 'Easy',
            '<p>Every weekday morning, a modernized fleet of quiet electric commuter trains ______ thousands of riders from suburban stations into the city center.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['carry', 'have carried', 'carrying', 'carries'],
            'D',
            'Gạch bỏ cụm giới từ chen giữa: "a modernized <b>fleet</b> <s>[of quiet electric commuter trains]</s>". Chủ ngữ thật là danh từ tập hợp SỐ ÍT "a modernized fleet" (một đội tàu), bối cảnh thói quen hàng ngày ("Every weekday morning") → chọn động từ hiện tại đơn số ít `carries` (D)!',
            'Gạch bỏ cụm `of...` để không bị danh từ số nhiều `trains` đánh lừa; chủ ngữ `a fleet` là SỐ ÍT → `carries`!',
            [
                ('Subject-Verb Mismatch', 'carry là số nhiều — bị đánh lừa bởi danh từ "trains".'),
                ('Subject-Verb Mismatch', 'have carried là số nhiều và lệch thì thói quen hàng ngày.'),
                ('Non-Finite Fragment', 'carrying là V-ing khiến câu không có động từ chia thì.'),
                ('Đáp án đúng', 'carries (hiện tại đơn, số ít) khớp chuẩn với chủ ngữ "a modernized fleet".'),
            ]
        ),
        q_item(
            'm6_m2l_q21', 21, 'Standard English Conventions', 'Form, Structure, and Sense', 'Easy',
            '<p>In 2004, coastal archaeologists dove along the submerged harbor of ancient Caesarea, photographed eroded breakwater blocks, and ______ cylindrical mortar samples for laboratory testing.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['collect', 'will collect', 'collected', 'collecting'],
            'C',
            'Quy tắc Thì nhất quán & Cấu trúc song song (Parallel Verbs in Past Tense): Mốc thời gian `In 2004` + chuỗi 3 động từ quá khứ đơn song hành của cùng chủ ngữ "coastal archaeologists": `dove...`, `photographed...`, and `______` → Phải là quá khứ đơn `collected` (C)!',
            'Nhìn 2 động từ đi trước cùng chuỗi (`dove`, `photographed`) + mốc năm `In 2004` → chốt ngay quá khứ đơn `collected`!',
            [
                ('Verb Tense Shift', 'collect là hiện tại đơn — lệch mốc năm 2004 và hai động từ quá khứ trước đó.'),
                ('Verb Tense Shift', 'will collect là tương lai đơn — sai mốc quá khứ 2004.'),
                ('Đáp án đúng', 'collected (quá khứ đơn) song song hoàn hảo với "dove" và "photographed".'),
                ('Parallelism / Fragment Trap', 'collecting không song song với hai động từ chia thì quá khứ trước đó.'),
            ]
        ),
        q_item(
            'm6_m2l_q22', 22, 'Standard English Conventions', 'Form, Structure, and Sense', 'Medium',
            '<p>When Victorian astronomers at Harvard Observatory stored delicate photographic glass plates inside wooden cabinets, assistants carefully labeled ______ by observation date and constellation so future researchers could retrieve any star image quickly.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['them', 'it', 'that', 'one'],
            'A',
            'Hòa hợp Đại từ – Tiền ngữ (Pronoun-Antecedent Agreement): Tiền ngữ mà các trợ lý dán nhãn là `delicate photographic glass plates` (SỐ NHIỀU — những tấm kính ảnh) → Bắt buộc dùng đại từ tân ngữ SỐ NHIỀU `them` (A)! Loại `it`, `that`, `one` vì đều là số ít.',
            'Hỏi: "Trợ lý dán nhãn CÁI GÌ?" → `glass plates` (số nhiều) ⇒ chỉ có đại từ số nhiều `them` (A) khớp chuẩn!',
            [
                ('Đáp án đúng', 'them (đại từ số nhiều) quy chiếu chính xác tới danh từ số nhiều "photographic glass plates".'),
                ('Pronoun Number Mismatch', 'it là số ít — không khớp "plates".'),
                ('Pronoun Number Mismatch', 'that là số ít — không thay cho danh từ số nhiều.'),
                ('Pronoun Number Mismatch', 'one là số ít — sai số so với "glass plates".'),
            ]
        ),

        # --- Q23-Q25: Expression of Ideas — Transitions ---
        q_item(
            'm6_m2l_q23', 23, 'Expression of Ideas', 'Transitions', 'Easy',
            '<p>Traditional desert builders across the Middle East invented clever passive architectural features that cool homes without electricity. ______, historic adobe houses in the Iranian city of Yazd use tall rooftop windcatchers to funnel evening breezes directly into shaded downstairs living rooms.</p>',
            'Which choice completes the text with the most logical transition?',
            ['However', 'Therefore', 'Meanwhile', 'For example'],
            'D',
            'Câu 1 nêu khái quát ("Traditional desert builders... invented clever passive architectural features"). Câu 2 đưa ra MỘT VÍ DỤ CỤ THỂ minh họa (nhà đất nung ở thành phố Yazd, Iran dùng tháp đón gió trên mái) → Quan hệ Nêu ví dụ → "For example" (D)!',
            'Từ ý chung rộng ("across the Middle East... features") sang một thành phố & công trình cụ thể ("Iranian city of Yazd... windcatchers") → chọn "For example"!',
            [
                ('False Contrast', 'However dùng cho ý trái ngược — câu 2 minh họa cùng chiều cho câu 1.'),
                ('Wrong Relationship (Cause-Effect)', 'Câu 2 là ví dụ minh họa chứ không phải kết quả của câu 1.'),
                ('Wrong Relationship (Time)', 'Meanwhile chỉ hai việc xảy ra đồng thời tách biệt.'),
                ('Đáp án đúng', 'For example nối mượt mà từ nhận định khái quát sang ví dụ cụ thể tại Yazd.'),
            ]
        ),
        q_item(
            'm6_m2l_q24', 24, 'Expression of Ideas', 'Transitions', 'Easy',
            '<p>For more than four centuries, Sogdian merchants dominated overland Silk Road trade from Central Asia to the imperial capitals of China. ______, because their language gradually fell out of everyday use after the tenth century, few readers outside academic history recognize their name today.</p>',
            'Which choice completes the text with the most logical transition?',
            ['Similarly', 'However', 'For instance', 'In addition'],
            'B',
            'Câu 1: Suốt hơn 4 thế kỷ, thương nhân Sogdia thống trị thương mại Con đường Tơ lụa (vô cùng lừng lẫy). Câu 2: Ngày nay rất ít độc giả ngoài giới sử học biết tên họ (trái ngược hoàn toàn với tầm ảnh hưởng lớn xưa kia) → Quan hệ Tương phản → "However" (B)!',
            'Lừng lẫy thống trị hơn 400 năm ↔ Ngày nay ít người biết tên ⇒ Đối lập rõ rệt → chốt "However"!',
            [
                ('Wrong Relationship (Comparison)', 'Similarly chỉ sự tương đồng — trái ngược với độ vênh giữa quá khứ lẫy lừng và hiện tại bị lãng quên.'),
                ('Đáp án đúng', 'However chuyển mạch tương phản chuẩn xác giữa tầm ảnh hưởng lịch sử to lớn và sự ít được biết đến ngày nay.'),
                ('Wrong Relationship (Example)', 'Việc ít được biết đến không phải ví dụ cho việc họ thống trị thương mại.'),
                ('Wrong Relationship (Addition)', 'In addition bổ sung thông tin cùng chiều tích cực, không hợp ý đối lập.'),
            ]
        ),
        q_item(
            'm6_m2l_q25', 25, 'Expression of Ideas', 'Transitions', 'Medium',
            '<p>Optical lattice atomic clocks help global communication networks synchronize high-speed data transfers down to trillionths of a second. ______, because their ticking rate responds sensitively to tiny changes in Earth’s gravity, geophysicists are testing them to track gradual shifts in sea level and underground aquifers.</p>',
            'Which choice completes the text with the most logical transition?',
            ['By contrast', 'Nevertheless', 'In addition', 'Instead'],
            'C',
            'Câu 1 nêu ỨNG DỤNG 1 (đồng bộ mạng truyền dữ liệu tốc độ cao). Câu 2 bổ sung ỨNG DỤNG 2 ĐỘC LẬP cùng chiều (đo trọng lực để theo dõi mực nước biển và tầng nước ngầm) → Quan hệ Bổ sung ý mới cùng hướng → "In addition" (C)!',
            'Ứng dụng 1 (viễn thông) + Ứng dụng 2 độc lập (địa vật lý) → dùng từ nối bổ sung "In addition / Furthermore"!',
            [
                ('False Contrast', 'Hai câu đều liệt kê ứng dụng hữu ích của đồng hồ quang học, không đối lập nhau.'),
                ('False Contrast', 'Nevertheless chỉ sự bất chấp trái kỳ vọng — sai hoàn toàn.'),
                ('Đáp án đúng', 'In addition bổ sung trơn tru ứng dụng khoa học thứ hai độc lập tiếp nối ứng dụng ở câu 1.'),
                ('False Substitution', 'Instead chỉ hành động thay thế sau một vế phủ định — không phù hợp ở đây.'),
            ]
        ),

        # --- Q26-Q27: Expression of Ideas — Rhetorical Synthesis ---
        q_item(
            'm6_m2l_q26', 26, 'Expression of Ideas', 'Rhetorical Synthesis', 'Easy',
            '''<p>While researching bioluminescent fungi, a student has taken the following notes:</p>
            <ul>
              <li>More than eighty known species of forest mushrooms naturally glow green in the dark.</li>
              <li>This faint light is produced by a chemical reaction inside the mushroom’s cells.</li>
              <li>A light-emitting compound called luciferin reacts with oxygen in the presence of an enzyme named luciferase.</li>
              <li>Unlike an electric lightbulb, this biological reaction releases almost no heat.</li>
            </ul>''',
            'The student wants to explain the chemical process that makes certain forest mushrooms glow in the dark. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
            [
                'More than eighty known species of forest mushrooms produce a faint greenish glow in the dark.',
                'Certain forest mushrooms glow in the dark through a chemical reaction in which a compound called luciferin reacts with oxygen alongside the enzyme luciferase, releasing light with almost no heat.',
                'Electric lightbulbs release much more heat than glowing forest mushrooms do.',
                'Bioluminescent mushrooms are among the more than eighty fungal species studied by forest biologists.'
            ],
            'B',
            'Goal-First SOP: Giải thích QUÁ TRÌNH HÓA HỌC ("explain the chemical process") khiến nấm rừng phát sáng trong bóng tối. A và D chỉ nêu số lượng loài (>80 loài); C chỉ so sánh nhiệt lượng với bóng đèn điện. Duy nhất B trình bày rõ phản ứng giữa `luciferin`, `oxygen` và enzyme `luciferase` tạo ra ánh sáng gần như không tỏa nhiệt → Chọn B!',
            'Tìm đáp án chứa đúng các thành phần hóa học giải thích cơ chế (`luciferin` + `oxygen` + `luciferase`) theo yêu cầu "chemical process"!',
            [
                ('Wrong Synthesis Goal', 'Chỉ nêu số lượng hơn 80 loài phát sáng xanh, không giải thích phản ứng hóa học.'),
                ('Đáp án đúng', 'Trình bày chính xác và đầy đủ phản ứng hóa học giữa luciferin, oxy và enzyme luciferase tạo ánh sáng lạnh.'),
                ('Wrong Synthesis Goal', 'Chỉ so sánh lượng nhiệt với bóng đèn điện, bỏ qua phản ứng hóa học tạo sáng.'),
                ('Wrong Synthesis Goal', 'Chỉ nêu số loài mà không hề giải thích quá trình hóa học.'),
            ]
        ),
        q_item(
            'm6_m2l_q27', 27, 'Expression of Ideas', 'Rhetorical Synthesis', 'Medium',
            '''<p>While researching nineteenth-century women astronomers, a student has taken the following notes:</p>
            <ul>
              <li>Annie Maunder was an Irish-born solar astronomer who worked at the Royal Observatory in Greenwich during the 1890s.</li>
              <li>She used custom cameras to capture and analyze thousands of glass-plate photographs of sunspots and solar eclipses.</li>
              <li>Williamina Fleming was a Scottish-born astronomer who worked at Harvard College Observatory during the same era.</li>
              <li>She systematically analyzed thousands of glass-plate stellar spectra to classify stars and discover new nebulae.</li>
            </ul>''',
            'The student wants to emphasize a similarity between Annie Maunder and Williamina Fleming’s astronomical work. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
            [
                'Both Annie Maunder and Williamina Fleming advanced nineteenth-century astronomy by systematically analyzing thousands of glass-plate photographs.',
                'Annie Maunder studied sunspots at the Royal Observatory in Greenwich, whereas Williamina Fleming worked at Harvard College Observatory.',
                'Scottish-born astronomer Williamina Fleming classified stars and discovered new nebulae at Harvard College Observatory.',
                'During the 1890s, Annie Maunder traveled with custom cameras to photograph solar eclipses.'
            ],
            'A',
            'Goal-First SOP: Nhấn mạnh ĐIỂM TƯƠNG ĐỒNG ("emphasize a similarity") trong công việc thiên văn của CẢ HAI nhà khoa học. B nhấn mạnh sự khác biệt nơi làm việc ("whereas"); C và D chỉ nhắc 1 người. Duy nhất A nêu rõ điểm chung cốt lõi của cả hai ("Both... analyzing thousands of glass-plate photographs") → Chọn A!',
            'Goal hỏi "similarity between [Person A] and [Person B]" → bắt buộc chọn câu nhắc đủ cả 2 người bằng cấu trúc tương đồng (`Both A and B...`)!',
            [
                ('Đáp án đúng', 'Nêu bật trực diện điểm tương đồng cốt lõi giữa cả hai nhà thiên văn: cùng phân tích hệ thống hàng nghìn tấm ảnh kính thiên văn.'),
                ('Wrong Synthesis Goal (Contrast)', 'Dùng "whereas" để nhấn mạnh sự khác biệt thay vì điểm tương đồng.'),
                ('Single Subject Trap', 'Chỉ nói về Williamina Fleming, bỏ qua Annie Maunder.'),
                ('Single Subject Trap', 'Chỉ nói về Annie Maunder, bỏ qua Williamina Fleming.'),
            ]
        ),
    ]
