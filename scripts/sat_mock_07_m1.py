# -*- coding: utf-8 -*-
"""
Full-Length Adaptive Mock Test #7 — Module 1 (27 Qs, Easy/Medium/Hard Mix, 32 min)
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
            'm7_m1_q1', 1, 'Craft and Structure', 'Words in Context', 'Easy',
            '<p>When an exoplanet crosses in front of its host star, astronomers analyze the filtered starlight to identify atmospheric gases; however, high-altitude photochemical hazes frequently ______ those faint molecular absorption lines, leaving spectroscopists with flat, featureless readings.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            ['magnify', 'obscure', 'verify', 'generate'],
            'B',
            'Contrast + Result Clue: "however, high-altitude photochemical hazes... leaving spectroscopists with flat, featureless readings" → lớp sương mù quang hóa CHE KHUẤT / LÀM MỜ các vạch hấp thụ phân tử yếu ớt → "obscure" (B).',
            'Kết quả "flat, featureless readings" (tín hiệu phẳng không thấy đặc trưng) chỉ thẳng hành động che mờ tín hiệu → chọn "obscure".',
            [
                ('Opposite Meaning', 'magnify = phóng đại làm rõ hơn — trái ngược với kết quả tín hiệu phẳng không thấy vạch hấp thụ.'),
                ('Đáp án đúng', 'obscure = che khuất, làm mờ — khớp hoàn hảo với việc lớp sương mù xóa nhòa vạch quang phổ.'),
                ('Wrong Meaning', 'verify = xác minh — sương mù khí quyển không xác minh vạch hấp thụ.'),
                ('Wrong Context', 'generate = tạo ra — trái với kết quả mất sạch đặc trưng quang phổ ("featureless").'),
            ]
        ),
        q_item(
            'm7_m1_q2', 2, 'Craft and Structure', 'Words in Context', 'Medium',
            '<p>Before imported mineral blues reached Edo print shops in the 1820s, Japanese ukiyo-e artists relied heavily on dayflower-petal extract (<i>aigami</i>), a luminous sky-blue colorant that proved notoriously ______: even brief exposure to moisture or direct sunlight caused its vivid hue to bleach into pale tan.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            ['durable', 'abundant', 'opaque', 'ephemeral'],
            'D',
            'Colon Restatement Clue: "even brief exposure to moisture or direct sunlight caused its vivid hue to bleach into pale tan" → sắc xanh chiết xuất cánh hoa rất CHÓNG PHAI / NGẮN NGỦI → "ephemeral" (D).',
            'Mệnh đề sau dấu hai chấm định nghĩa trực tiếp đặc tính kém bền, dễ phai màu trong thời gian ngắn → chọn "ephemeral".',
            [
                ('Opposite Meaning', 'durable = bền lâu — trái ngược hoàn toàn với việc phai thành màu nâu nhạt chỉ sau khi tiếp xúc nhẹ ánh sáng/ẩm.'),
                ('Wrong Context', 'abundant = dồi dào — không giải thích vì sao màu nhanh bạc đi.'),
                ('Wrong Meaning', 'opaque = đục không xuyên sáng — không liên quan đến độ phai màu theo thời gian.'),
                ('Đáp án đúng', 'ephemeral = ngắn ngủi, chóng phai — phản chiếu chính xác việc sắc xanh nhanh chóng mất màu.'),
            ]
        ),
        q_item(
            'm7_m1_q3', 3, 'Craft and Structure', 'Words in Context', 'Medium',
            '<p>Hydrologists working across semi-arid basins in Utah found that reintroducing North American beavers can ______ local watershed stability: by slowing spring snowmelt behind terraced timber dams, the animals replenish underground aquifers that keep streams flowing well into late summer.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            ['bolster', 'undermine', 'exhaust', 'bypass'],
            'A',
            'Colon Explanation Clue: "slowing spring snowmelt... replenish underground aquifers that keep streams flowing well into late summer" → hành động tích cực CỦNG CỐ / TĂNG CƯỜNG độ ổn định lưu vực sông → "bolster" (A).',
            'Mệnh đề sau dấu hai chấm mô tả cơ chế nạp nước ngầm duy trì dòng chảy suốt mùa hè → chọn động từ mang nghĩa củng cố ("bolster").',
            [
                ('Đáp án đúng', 'bolster = củng cố, tăng cường — khớp tuyệt đối với vai trò nạp tầng chứa nước và giữ dòng suối ổn định.'),
                ('Opposite Meaning', 'undermine = làm suy yếu — ngược chiều hoàn toàn với tác động tích cực của hải ly.'),
                ('Opposite Meaning', 'exhaust = làm cạn kiệt — trái ngược với "replenish underground aquifers".'),
                ('Wrong Meaning', 'bypass = đi vòng bỏ qua — đập hải ly làm chậm dòng nước chứ không né bỏ sự ổn định lưu vực.'),
            ]
        ),
        q_item(
            'm7_m1_q4', 4, 'Craft and Structure', 'Words in Context', 'Hard',
            '<p>Whereas many manifesto writers during the 1920s Harlem Renaissance adopted fiery polemics to denounce conservative art critics, essayist Clara Vance favored a more ______ register, advancing her case for Black modernist aesthetics through patient historical comparisons and understated irony.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            ['bombastic', 'frantic', 'measured', 'ambiguous'],
            'C',
            'Contrast + Mirror Clue: đối lập với "fiery polemics" (luận chiến nảy lửa) + giải thích phía sau "patient historical comparisons and understated irony" (so sánh lịch sử kiên nhẫn và châm biếm nhẹ nhàng) → giọng văn CHỪNG MỰC, ĐIỀM TĨNH, CÂN NHẮC → Nghĩa thứ cấp học thuật của "measured" = deliberate, calm, and restrained → Chọn C!',
            'Nhớ nghĩa thứ cấp cực hay ra thi của "measured" (adj): điềm đạm, có chừng mực, cân nhắc kỹ (đối lập với "fiery / impulsive").',
            [
                ('Opposite Meaning', 'bombastic = khoa trương ồn ào — cùng chiều với "fiery polemics", sai sau "Whereas".'),
                ('Opposite Meaning', 'frantic = cuống cuồng hấp tấp — trái ngược với "patient" và "understated".'),
                ('Đáp án đúng', 'measured (nghĩa thứ cấp: điềm tĩnh, chừng mực) khớp hoàn hảo với cách lập luận kiên nhẫn và tinh tế.'),
                ('Wrong Meaning', 'ambiguous = mơ hồ khó hiểu — sự châm biếm tiết chế không đồng nghĩa với lập luận mơ hồ.'),
            ]
        ),
        q_item(
            'm7_m1_q5', 5, 'Craft and Structure', 'Words in Context', 'Hard',
            '<p>Before Swiss geologist Louis Agassiz proposed the continental Ice Age theory in 1837, naturalists struggled to explain why house-sized granite boulders sat atop limestone ridges hundreds of kilometers from the nearest granite mountain range; without glacial transport as a mechanism, such out-of-place rocks appeared utterly ______.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            ['predictable', 'anomalous', 'derivative', 'uniform'],
            'B',
            'Mirror Clue: "struggled to explain why house-sized granite boulders sat atop limestone ridges hundreds of kilometers from the nearest granite mountain range... out-of-place rocks" → những tảng đá lạc chỗ BẤT THƯỜNG, TRÁI QUY LUẬT → "anomalous" (B).',
            'Cụm "out-of-place rocks" kết hợp "struggled to explain" dẫn trực tiếp đến tính từ "anomalous" (bất thường, lệch chuẩn).',
            [
                ('Opposite Meaning', 'predictable = dễ đoán — mâu thuẫn trực tiếp với việc giới tự nhiên học chật vật tìm lời giải thích.'),
                ('Đáp án đúng', 'anomalous = bất thường, lạc quy luật — khớp hoàn toàn với đá hoa cương nằm lạc lõng trên đỉnh núi đá vôi.'),
                ('Wrong Meaning', 'derivative = bắt chước, thiếu nguyên bản — thường dùng cho tác phẩm nghệ thuật/học thuật.'),
                ('Opposite Meaning', 'uniform = đồng đều — trái ngược với sự xuất hiện dị biệt của đá tảng khác loại.'),
            ]
        ),

        # --- Q6-Q7: Craft and Structure — Text Structure and Purpose ---
        q_item(
            'm7_m1_q6', 6, 'Craft and Structure', 'Text Structure and Purpose', 'Medium',
            '<p>Freshwater unionid mussels filter dozens of liters of river water per day, capturing suspended algae alongside microscopic synthetic fibers shed from laundered textiles. <u>Using rows of microscopic gill cilia, however, a mussel can recognize indigestible plastic strands, bind them in sticky mucus, and expel them as dense pellets called pseudofeces that sink harmlessly into riverbed sediment before ever entering the animal’s digestive tract.</u> Environmental engineers are now investigating whether restoring native mussel beds downstream of wastewater outfalls could help trap urban microplastics out of open currents.</p>',
            'Which choice best describes the function of the underlined sentence in the text as a whole?',
            [
                'It argues that wastewater treatment plants should be replaced entirely by native unionid mussel beds.',
                'It challenges the claim in the first sentence that freshwater mussels encounter synthetic fibers in river water.',
                'It lists the chemical polymers found most frequently in laundered synthetic textiles.',
                'It explains the biological sorting mechanism by which freshwater mussels separate and remove ingested microplastics from water without digesting them.'
            ],
            'D',
            'Câu 1 nêu việc trai nước ngọt lọc tảo lẫn vi sợi nhựa từ nước sông. Câu gạch chân giải thích CƠ CHẾ PHÂN LOẠI SINH HỌC (dùng lông rung mang nhận diện sợi nhựa không tiêu hóa được, bọc nhầy và thải thành hạt giả phân chìm xuống trầm tích trước khi vào ruột) → Chọn D!',
            'Đoạn giữa sau câu mở đầu mô tả hoạt động thường đảm nhiệm vai trò giải thích cơ chế vận hành cụ thể ("how the process works").',
            [
                ('Too Extreme', 'Câu cuối chỉ nói kỹ sư đang nghiên cứu phục hồi bãi trai để hỗ trợ giữ vi nhựa, không đòi thay thế hoàn toàn nhà máy xử lý nước thải.'),
                ('Contradiction', 'Câu gạch chân xác nhận trai xử lý sợi nhựa chứ không bác bỏ câu 1.'),
                ('Out of Scope', 'Không liệt kê tên các loại polymer hóa học cụ thể.'),
                ('Đáp án đúng', 'Tóm gọn chính xác chức năng giải thích cơ chế phân loại bằng lông mang và thải giả phân của trai nước ngọt.'),
            ]
        ),
        q_item(
            'm7_m1_q7', 7, 'Craft and Structure', 'Text Structure and Purpose', 'Hard',
            '<p><i>The following text is adapted from a 1926 literary sketch set in Harlem. Julian, a young band arranger, pauses on the stoop of a brownstone at dusk with a folded sheet of staff paper in his coat pocket.</i><br/>From the open cellar window below came three trumpets testing a ragged blues phrase, pausing whenever the saxophonist shouted a new chord through the stairwell. Across the avenue, an elevated train clattered northward in triple time, and a fruit vendor’s rhythmic call rose cleanly between the iron beats. Listening to those overlapping voices knit themselves into a single restless pulse, Julian pulled out his pencil; the counter-melody he had struggled all afternoon to invent at his quiet desk was already alive on 135th Street.</p>',
            'Which choice best states the main purpose of the text?',
            [
                'To illustrate how the layered everyday sounds of a Harlem street spark an arranger’s musical inspiration.',
                'To criticize cellar musicians for disturbing neighborhood vendors during evening rush hour.',
                'To explain the formal conservatory rules required to notate triple-time train rhythms on staff paper.',
                'To show that Julian prefers working alone at his desk because street noise breaks his concentration.'
            ],
            'A',
            'Toàn đoạn vẽ nên bản hòa âm sống động của phố 135th Street ở Harlem: tiếng kèn trumpet từ tầng hầm, nhịp tàu điện trên cao, tiếng rao của người bán trái cây hòa thành một nhịp đập chung khiến Julian rút bút chì ra vì giai điệu đối âm anh bí suốt buổi chiều đã hiện hữu ngay trên phố → Chọn A!',
            'Đọc câu kết ("the counter-melody he had struggled all afternoon to invent... was already alive on 135th Street") để bắt trọn ý đồ tác giả!',
            [
                ('Đáp án đúng', 'Khắc họa chính xác cách các lớp âm thanh đời thường ở Harlem khơi nguồn cảm hứng phối khí cho Julian.'),
                ('Wrong Tone / Distortion', 'Không hề có sự phàn nàn hay chỉ trích; các âm thanh được mô tả hòa quyện giàu nhạc tính.'),
                ('Out of Scope', 'Không giải thích quy tắc nhạc viện về ký âm.'),
                ('Reversed Logic', 'Trái ngược hoàn toàn: ngồi một mình ở bàn yên tĩnh Julian bị bí, còn ra phố nghe âm thanh đời sống lại tìm thấy giai điệu.'),
            ]
        ),

        # --- Q8: Craft and Structure — Cross-Text Connections ---
        q_item(
            'm7_m1_q8', 8, 'Craft and Structure', 'Cross-Text Connections', 'Hard',
            '<p><b>Text 1</b><br/>Nineteenth-century philologists frequently described Caribbean French-lexifier creoles such as Haitian Creole as simplified dialects of colonial French, arguing that their streamlined verb endings arose simply because enslaved laborers had limited exposure to standard Parisian grammar.</p><p><b>Text 2</b><br/>Comparing syntactic archives from West Africa and the Caribbean, linguist Dr. Mireille Joseph demonstrates that while Haitian Creole draws most of its everyday vocabulary from French, its core grammatical architecture—including preverbal tense-aspect markers, serial verb constructions, and post-nominal determiners—closely parallels Fon and other Gbe languages spoken in historical Benin.</p>',
            'Based on the texts, how would Dr. Mireille Joseph (Text 2) most likely respond to the nineteenth-century philologists’ characterization (Text 1)?',
            [
                'By agreeing that Haitian Creole lacks systematic grammatical rules for expressing tense and aspect.',
                'By asserting that Haitian Creole shares no everyday vocabulary whatsoever with colonial French.',
                'By contending that Haitian Creole’s grammar is not merely a simplified offshoot of French, but reflects systematic structural patterns inherited from West African substrate languages.',
                'By arguing that speakers of Fon and other Gbe languages originally adopted their syntax from nineteenth-century Parisian dialects.'
            ],
            'C',
            'Text 1 coi tiếng Creole Haiti chỉ là "phương ngữ Pháp bị đơn giản hóa" do thiếu tiếp xúc ngữ pháp Paris. Text 2 công nhận phần lớn từ vựng mượn từ tiếng Pháp, NHƯNG chỉ ra khung ngữ pháp cốt lõi (dấu thời-thể trước động từ, chuỗi động từ, định từ sau danh từ) phản chiếu chặt chẽ tiếng Fon và nhóm ngôn ngữ Gbe ở Tây Phi → Phản biện Text 1 theo hướng: ngữ pháp Creole không chỉ là bản rút gọn của tiếng Pháp mà mang cấu trúc hệ thống từ ngôn ngữ nền Tây Phi (C)!',
            'Tách rõ 2 lớp trong Text 2: Từ vựng (phần lớn từ Pháp) vs. Ngữ pháp cốt lõi (song song tiếng Fon/Gbe Tây Phi) → loại bẫy cực đoan ở B và chọn C!',
            [
                ('Contradiction', 'Text 2 nêu rõ tiếng Creole Haiti có hệ thống dấu chỉ thời-thể (tense-aspect markers) chặt chẽ chứ không thiếu quy tắc.'),
                ('Overstated Conflict', 'Text 2 thừa nhận rõ "draws most of its everyday vocabulary from French", nên "no vocabulary whatsoever" là sai hoàn toàn.'),
                ('Đáp án đúng', 'Khớp chính xác phản biện của Joseph: ngữ pháp mang cấu trúc hệ thống từ ngôn ngữ nền Tây Phi chứ không đơn thuần là tiếng Pháp rút gọn.'),
                ('Reversed Logic', 'Đảo ngược chiều ảnh hưởng lịch sử giữa Tây Phi và Paris.'),
            ]
        ),

        # --- Q9-Q10: Information and Ideas — Central Ideas and Details ---
        q_item(
            'm7_m1_q9', 9, 'Information and Ideas', 'Central Ideas and Details', 'Medium',
            '<p><i>The following poem is from a 1929 Harlem literary journal.</i><br/>Midnight leans against the brass bell of his horn,<br/>A silver breath drawn steady through the smoke,<br/>Not fleeing sorrow—holding every thorn<br/>Until the low note answers what it spoke.<br/>Across the tables, weary shoulders lift;<br/>One battered trumpet turns the heavy night<br/>Into a shared and incandescent gift,<br/>Where sorrow’s weight transforms to ringing light.</p>',
            'Which choice best states the main idea of the poem?',
            [
                'A trumpeter abandons jazz performance because late-night club audiences seem too weary to listen.',
                'Through steady musical expression, a jazz horn player transforms shared sorrow into uplifting communal radiance.',
                'Harlem nightclub patrons prefer cheerful fast dance tunes over slow blues melodies.',
                'Brass instruments require years of solitary repair before they can produce clear silver tones.'
            ],
            'B',
            'Ý chính bài thơ: Người thổi kèn không né tránh nỗi buồn ("Not fleeing sorrow—holding every thorn"), mà dùng tiếng kèn chuyển hóa đêm nặng nề thành "món quà rực sáng chung" khiến những bờ vai mệt mỏi bừng dậy và sức nặng nỗi buồn hóa thành ánh sáng vang vọng → Chọn B!',
            'Bám sát cặp hình ảnh chuyển hóa ở khổ cuối: "turns the heavy night into a shared and incandescent gift / sorrow’s weight transforms to ringing light".',
            [
                ('Contradiction', 'Khán giả mệt mỏi nhưng ngay lập tức "weary shoulders lift" khi nghe tiếng kèn, không phải bỏ diễn.'),
                ('Đáp án đúng', 'Nắm trọn mạch cảm xúc chuyển hóa nỗi buồn thành ánh sáng sẻ chia qua âm nhạc.'),
                ('Out of Scope', 'Không hề so sánh nhạc nhảy nhanh với nhạc blues chậm.'),
                ('Literal Misreading', 'Cụm "battered trumpet" chỉ cây kèn cũ nhiều dấu thời gian, không nói về nghề sửa chữa nhạc cụ.'),
            ]
        ),
        q_item(
            'm7_m1_q10', 10, 'Information and Ideas', 'Central Ideas and Details', 'Hard',
            '<p>Around 1830, Edo-period woodblock printmakers began importing synthetic Prussian blue—known in Japan as <i>bero-ai</i>—through Dutch trading posts at Nagasaki. Unlike fragile botanical blues extracted from indigo or dayflower petals, Prussian blue resisted fading under light and allowed master carvers and printers working with Katsushika Hokusai and Utagawa Hiroshige to achieve smooth tonal gradations (<i>bokashi</i>) ranging from luminous pale sky to deep oceanic midnight blue, sparking a surge of landscape prints such as <i>Thirty-Six Views of Mount Fuji</i>.</p>',
            'According to the text, what technical advantages prompted Edo-period printmakers to embrace imported Prussian blue?',
            [
                'It could be harvested directly from wild Japanese dayflowers without relying on Dutch maritime trade.',
                'It eliminated the need for wooden key blocks when printing large landscape editions.',
                'It dried instantly on silk canvas, allowing painters to abandon paper scrolls completely.',
                'It resisted light-induced fading and enabled smooth color gradations spanning pale sky tints to deep dark blues.'
            ],
            'D',
            'Câu hỏi Specific Detail: Tìm đúng câu liệt kê ưu thế kỹ thuật của Prussian blue ("Unlike fragile botanical blues..., Prussian blue resisted fading under light and allowed... to achieve smooth tonal gradations (bokashi) ranging from luminous pale sky to deep oceanic midnight blue") → Paraphrase chuẩn xác ở D!',
            'Khoanh vùng ngay cụm "resisted fading under light and allowed... smooth tonal gradations" để chọn đáp án bám sát 100% văn bản.',
            [
                ('Contradiction', 'Màu này là phẩm tổng hợp nhập khẩu qua thương điếm Hà Lan ở Nagasaki, đối lập hoàn toàn với màu cánh hoa dayflower bản địa.'),
                ('Out of Scope', 'Không nói bỏ ván khắc gỗ; bài nhắc rõ "master carvers and printers".'),
                ('Out of Scope', 'Không đề cập lụa hay cuộn tranh giấy.'),
                ('Đáp án đúng', 'Khớp nguyên vẹn hai ưu thế kỹ thuật: bền màu dưới ánh sáng và tạo chuyển sắc mịn từ xanh trời nhạt đến xanh thẫm đại dương.'),
            ]
        ),

        # --- Q11-Q12: Information and Ideas — Command of Evidence (Textual) ---
        q_item(
            'm7_m1_q11', 11, 'Information and Ideas', 'Command of Evidence (Textual)', 'Hard',
            '<p>During severe wildfires across the western United States, satellite imagery repeatedly reveals bright green ribbons of unburned willows and sedges winding through blackened forests wherever North American beavers maintain active dam complexes. Ecohydrologist Dr. Hannah Morales hypothesized that these riparian corridors survive fire primarily not because open pond water physically douses blowing embers, but because beaver-dug channels raise surrounding groundwater tables enough to keep floodplain plant tissues too water-saturated to ignite.</p>',
            'Which finding, if true, would most directly support Dr. Hannah Morales’s hypothesis?',
            [
                'Across five burned western watersheds, vegetation growing fifty meters away from open beaver ponds—but fed by shallow beaver-dug irrigation canals with elevated soil moisture—escaped scorching at nearly the same rate as bankside plants, whereas dry brush along undammed creeks of equal water width burned completely.',
                'Beavers typically fell aspen and cottonwood saplings within thirty meters of stream banks during autumn to stockpile winter food caches.',
                'Satellite thermal sensors detect peak wildfire flame temperatures exceeding 800°C along steep pine ridges far above valley floors.',
                'Historical fur-trapping records indicate that North American beaver populations numbered in the tens of millions prior to 1800.'
            ],
            'A',
            'Khóa giả thuyết Morales: Hành lang xanh sống sót KHÔNG chủ yếu nhờ mặt nước ao dập tàn lửa trực tiếp, MÀ nhờ hệ thống kênh đào của hải ly NÂNG MỰC NƯỚC NGẦM khiến đất ẩm và mô thực vật vùng bãi bồi ngậm nước khó bén lửa. Đáp án A tách bạch hoàn hảo 2 cơ chế: thực vật cách xa ao mở tới 50m (nước ao không tạt tới được) nhưng có kênh ngầm ẩm ướt vẫn thoát cháy ngang cây ven bờ, trong khi bụi khô ven suối không có đập (dù lòng suối rộng tương đương) bị thiêu rụi hoàn toàn → Chọn A!',
            'Tìm bằng chứng tách biến độc lập: cách xa mặt ao (loại yếu tố nước dập trực tiếp) + độ ẩm đất cao vẫn xanh ↔ suối không đập bị cháy rụi!',
            [
                ('Đáp án đúng', 'Cô lập hoàn hảo cơ chế mực nước ngầm & độ ẩm đất (cách xa ao 50m vẫn không cháy; suối cùng bề rộng nhưng không có đập bị thiêu rụi).'),
                ('Adjacent Topic Drift', 'Tập tính dự trữ thức ăn mùa đông của hải ly không kiểm chứng cơ chế chống cháy rừng.'),
                ('Irrelevant Detail', 'Nhiệt độ đám cháy trên sườn thông cao không phân biệt giữa hai giả thuyết ở đáy thung lũng.'),
                ('Irrelevant History', 'Số lượng hải ly trước năm 1800 không chứng minh cơ chế thủy văn chống cháy.'),
            ]
        ),
        q_item(
            'm7_m1_q12', 12, 'Information and Ideas', 'Command of Evidence (Textual)', 'Medium',
            '<p>In an essay examining the 1928 stage drama <i>The Blue Note Ledger</i>, a music historian argues that bandleader Silas rejects rigid, uniform orchestral charts because he believes an arrangement succeeds only when it leaves room for each soloist’s distinctive temperament to shine through.</p>',
            'Which quotation from Silas in <i>The Blue Note Ledger</i> most effectively illustrates the historian’s claim?',
            [
                '“Check the valves on your cornet before curtain call; a sticky spring ruined our opening ballad last Friday.”',
                '“The ballroom manager pays us forty dollars for the Friday matinee and sixty if the floor stays full past midnight.”',
                '“I write the brass frame tight enough to hold the room together, then I leave sixteen open bars so Mae’s clarinet and Booker’s trombone can speak in their own unmistakable voices instead of marching like tin soldiers.”',
                '“We took the uptown subway from 125th Street to reach the recording studio before the afternoon session ended.”'
            ],
            'C',
            'Checklist Claim: [1] Từ chối bản phối cứng nhắc đồng loạt ("rejects rigid, uniform charts") + [2] Chừa không gian để cá tính độc đáo của từng nghệ sĩ solo tỏa sáng ("each soloist’s distinctive temperament to shine through"). Đáp án C khớp hoàn mỹ từng chữ: tạo khung kèn vừa đủ giữ nhịp, rồi chừa 16 ô nhịp mở để kèn clarinet của Mae và trombone của Booker cất lên bằng "giọng nói riêng không lẫn vào đâu được" thay vì "diễu hành như lính chì"! Chọn C!',
            'Tìm trích dẫn có cả 2 vế: từ chối sự đồng phục máy móc ("tin soldiers") + nhường chỗ cho bản sắc cá nhân của từng nhạc công ("unmistakable voices")!',
            [
                ('Topic Keyword Lure', 'Chỉ nhắc việc bảo trì van kèn cornet, không liên quan đến triết lý phối khí.'),
                ('Irrelevant Detail', 'Chỉ nói về tiền cát-xê ở vũ trường.'),
                ('Đáp án đúng', 'Minh họa trực tiếp cả việc chừa không gian solo cho cá tính từng nghệ sĩ lẫn việc bác bỏ sự đồng đều cứng nhắc.'),
                ('Irrelevant Detail', 'Chỉ kể chuyện đi tàu điện ngầm tới phòng thu.'),
            ]
        ),

        # --- Q13-Q14: Information and Ideas — Command of Evidence (Quantitative) ---
        q_item(
            'm7_m1_q13', 13, 'Information and Ideas', 'Command of Evidence (Quantitative)', 'Medium',
            svg_bar_chart(
                'Suspended Polyester Microfiber Removal (%) Over 24 Hours by Filtration Setup',
                ['0%', '25%', '50%', '75%', '100%'],
                [('Untreated Control', 6, '6%'), ('Sand Filter Only', 24, '24%'), ('Unionid Mussels', 68, '68%'), ('Mussels+Plants', 84, '84%')],
                100
            ) + '<p>Aquatic toxicologists evaluating low-cost bioremediation tanks reported that adding live native unionid mussels removes nearly three times as much suspended textile microfiber as passive sand filtration alone, and pairing those mussels with submerged aquatic plants pushes total removal efficiency even higher.</p>',
            'Which choice most effectively uses data from the graph to support the toxicologists’ report?',
            [
                'Untreated control tanks lost only 6% of suspended polyester microfibers over 24 hours through natural settling.',
                'Tanks stocked with unionid mussels removed 68% of microfibers—nearly three times the 24% removed by sand filtration alone—while tanks combining mussels and submerged plants reached 84% removal.',
                'Passive sand filtration removed 24% of suspended microfibers, representing a fourfold increase over untreated control tanks (6%).',
                'All four experimental tank configurations removed at least 6% of suspended polyester microfibers within 24 hours.'
            ],
            'B',
            'Checklist 2 vế trong báo cáo: [1] Trai nước ngọt (68%) lọc gần gấp 3 lần lọc cát thụ động (24%; 24 × 3 = 72, 68% gần gấp 3 ✓) + [2] Kết hợp thêm thực vật thủy sinh đẩy hiệu suất lên cao hơn nữa (84% > 68% ✓). A, C, D đều đúng số liệu nhưng bỏ sót hoàn toàn cột Unionid Mussels và Mussels+Plants! Duy nhất B nêu đủ cả 3 mốc 68%, 24%, và 84%!',
            'Đối chiếu đúng hai phép so sánh trong đề: Mussels (68%) vs. Sand Only (24%) và Mussels+Plants (84%)!',
            [
                ('True Data / Wrong Subject', 'Chỉ nêu số liệu nhóm đối chứng (6%), không nhắc tới trai hay thực vật.'),
                ('Đáp án đúng', 'Dẫn trọn cả hai dữ kiện hỗ trợ báo cáo: 68% gần gấp ba 24%, và tổ hợp thêm thực vật tăng lên 84%.'),
                ('True Data / Wrong Claim', 'So sánh lọc cát với đối chứng (24% vs. 6%), bỏ qua hoàn toàn hiệu suất của trai và thực vật.'),
                ('Incomplete Data', 'Chỉ nêu mức tối thiểu chung 6%, không chứng minh ưu thế của trai hay tổ hợp trai + thực vật.'),
            ]
        ),
        q_item(
            'm7_m1_q14', 14, 'Information and Ideas', 'Command of Evidence (Quantitative)', 'Hard',
            html_table(
                'Table 1. Infrared Transmission Spectroscopy of Four Sub-Neptune Exoplanets',
                ['Exoplanet', 'Equilibrium Temp (K)', 'Photochemical Haze Index (0–10)', 'Water Vapor Signal (ppm)'],
                [
                    ['K2-18 b', '280 K', '1.8 (Low)', '142 ppm'],
                    ['TOI-270 d', '350 K', '2.1 (Low)', '118 ppm'],
                    ['GJ 1214 b', '560 K', '8.9 (Very High)', '14 ppm'],
                    ['HD 97658 b', '750 K', '7.6 (High)', '26 ppm'],
                ]
            ) + '<p>An astrophysics graduate student claims that among sub-Neptune exoplanets, higher atmospheric equilibrium temperatures reliably produce stronger detectable water-vapor absorption signals in transmission spectra.</p>',
            'Which choice best describes data from the table that directly weaken the graduate student’s claim?',
            [
                'Although GJ 1214 b (560 K) and HD 97658 b (750 K) have much higher equilibrium temperatures than K2-18 b (280 K) and TOI-270 d (350 K), both hotter worlds exhibit dramatically weaker water-vapor signals (14 ppm and 26 ppm versus 142 ppm and 118 ppm).',
                'Among the two high-haze exoplanets listed, HD 97658 b has both a higher equilibrium temperature (750 K) and a slightly stronger water-vapor signal (26 ppm) than GJ 1214 b (560 K; 14 ppm).',
                'K2-18 b has the lowest equilibrium temperature in the table at 280 K and the lowest photochemical haze index at 1.8.',
                'All four sub-Neptune exoplanets in the survey yielded water-vapor absorption signals above 10 ppm.'
            ],
            'A',
            'Khóa Claim cần WEAKEN: Nhiệt độ cân bằng càng CAO → tín hiệu hấp thụ hơi nước càng MẠNH. Soi bảng: 2 hành tinh NÓNG NHẤT là GJ 1214 b (560 K) và HD 97658 b (750 K) lại có tín hiệu hơi nước YẾU THÊ THẢM (14 ppm và 26 ppm), trong khi 2 hành tinh LẠNH HƠN là K2-18 b (280 K) và TOI-270 d (350 K) có tín hiệu MẠNH GẤP NHIỀU LẦN (142 ppm và 118 ppm) → Chọn A!',
            'Tìm cặp đối chiếu ngược chiều tuyên bố: Temp cao nhất (560 K, 750 K) nhưng Signal yếu nhất (14, 26 ppm) so với Temp thấp hơn (280 K, 350 K) có Signal 142, 118 ppm!',
            [
                ('Đáp án đúng', 'Phản bác trực diện tuyên bố: hai ngoại hành tinh nóng hơn nhiều lại cho tín hiệu hơi nước yếu hơn rõ rệt so với hai hành tinh lạnh hơn.'),
                ('Opposite Direction (Supports!)', 'So sánh riêng HD 97658 b với GJ 1214 b lại đi CÙNG chiều với tuyên bố của sinh viên (nóng hơn → tín hiệu nhỉnh hơn).'),
                ('Incomplete Data', 'Chỉ nêu thông số một hành tinh K2-18 b, không đối chiếu xu hướng nhiệt độ cao vs. thấp.'),
                ('True Data / Wrong Claim', 'Việc cả 4 đều trên 10 ppm không hề bác bỏ mối tương quan thuận giữa nhiệt độ và tín hiệu.'),
            ]
        ),

        # --- Q15: Information and Ideas — Inferences ---
        q_item(
            'm7_m1_q15', 15, 'Information and Ideas', 'Inferences', 'Hard',
            '<p>In Southern Quechua, speakers routinely attach mandatory evidential suffixes to statements to specify how they learned a fact—using <i>-mi</i> for direct eyewitness knowledge and <i>-si</i> for secondhand hearsay. Sociolinguists interviewing Quechua–Spanish bilinguals in Cusco observed that even when speaking exclusively in Spanish—which lacks mandatory evidential suffixes—these speakers consistently used the Spanish pluperfect tense (<i>había llegado</i>, "had arrived") to report events they had only heard about from neighbors while reserving the simple past (<i>llegó</i>) for events they had witnessed personally. This pattern suggests that ______</p>',
            'Which choice most logically completes the text?',
            [
                'Standard Spanish grammar forbids speakers from using the simple past tense to describe witnessed events.',
                'bilingual residents of Cusco are rapidly replacing Quechua evidential suffixes with borrowed Spanish vocabulary.',
                'Southern Quechua speakers rarely rely on secondhand information when recounting community news.',
                'grammatical habits formed by Quechua’s evidential system can influence bilingual speakers to repurpose existing Spanish verb tenses to mark information source.'
            ],
            'D',
            'Ghép 2 tiền đề (1-Millimeter Rule): (A) Tiếng Quechua bắt buộc phân biệt nguồn thông tin trực tiếp (`-mi`) vs. nghe kể (`-si`); (B) Khi nói hoàn toàn bằng tiếng Tây Ban Nha (vốn không có hậu tố chứng cứ bắt buộc), người song ngữ ở Cusco lại nhất quán phân vai thì Quá khứ hoàn thành (nghe kể) vs. Quá khứ đơn (tận mắt thấy) ⇒ Suy luận trực tiếp: Thói quen ngữ pháp của hệ thống chứng cứ Quechua đã tác động khiến người song ngữ TÁI SỬ DỤNG các thì động từ sẵn có trong tiếng Tây Ban Nha để đánh dấu nguồn tin (D)!',
            'Áp dụng quy tắc suy diễn 1mm: Thấy cấu trúc nguồn tin từ ngôn ngữ A tái hiện qua thì động từ của ngôn ngữ B → kết luận về sự chuyển giao chức năng ngữ pháp ở người song ngữ.',
            [
                ('Out of Scope / False', 'Bài không nói tiếng Tây Ban Nha chuẩn cấm dùng quá khứ đơn cho sự kiện tận mắt thấy.'),
                ('Reversed Direction', 'Bài nói ảnh hưởng đi từ Quechua → cách dùng thì Tây Ban Nha, KHÔNG nói tiếng Quechua đang bị thay bằng từ vựng Tây Ban Nha.'),
                ('Contradiction', 'Người nói vẫn tường thuật tin nghe từ hàng xóm bằng thì quá khứ hoàn thành, không phải hiếm khi dùng tin nghe kể.'),
                ('Đáp án đúng', 'Khớp sát từng chi tiết: thói quen phân biệt nguồn tin trong Quechua dẫn tới việc tận dụng thì động từ Tây Ban Nha cho chức năng tương tự.'),
            ]
        ),

        # --- Q16-Q19: Standard English Conventions — Boundaries ---
        q_item(
            'm7_m1_q16', 16, 'Standard English Conventions', 'Boundaries', 'Easy',
            '<p>As an alpine glacier retreats up a mountain valley, melting ice deposits unsorted ridges of gravel and boulders called terminal ______ these curved earthworks serve as geological benchmarks showing exactly how far the ice front once advanced.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['moraines,', 'moraines', 'moraines;', 'moraines, while'],
            'C',
            'Vế 1 là IC hoàn chỉnh ("As an alpine glacier retreats..., melting ice deposits... terminal moraines"). Vế 2 cũng là IC hoàn chỉnh ("these curved earthworks serve as geological benchmarks..."). Nối 2 IC trực tiếp → Dùng dấu chấm phẩy (;) = C!',
            'Phân tích ranh giới IC + IC → Chọn chấm phẩy (;), loại ngay Comma Splice (A), Run-on (B) và câu lệch logic phụ thuộc (D).',
            [
                ('Comma Splice', 'Chỉ đặt 1 dấu phẩy giữa hai mệnh đề độc lập là lỗi Comma Splice.'),
                ('Run-On Sentence', 'Không có dấu câu ngăn cách hai mệnh đề độc lập.'),
                ('Đáp án đúng', 'Dấu chấm phẩy (;) ngăn cách chuẩn xác hai mệnh đề độc lập có quan hệ nghĩa chặt chẽ.'),
                ('Wrong Subordination', 'Thêm ", while" tạo quan hệ đối lập hoặc đồng thời không hợp lý với câu định nghĩa vai trò địa chất của băng tích cuối.'),
            ]
        ),
        q_item(
            'm7_m1_q17', 17, 'Standard English Conventions', 'Boundaries', 'Medium',
            '<p>Using noninvasive fiber-optic reflectance spectroscopy at the Tokyo National Museum, print conservator ______ identified trace mixtures of natural indigo and synthetic Prussian blue in an 1832 impression of Hokusai’s <i>The Great Wave</i>.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['Kenji Watanabe', ', Kenji Watanabe,', 'Kenji Watanabe,', ', Kenji Watanabe'],
            'A',
            'Quy tắc Chức danh không mạo từ + Tên riêng: "print conservator Kenji Watanabe" (không có "a/the" trước "print conservator") → Tên riêng là thành phần BẮT BUỘC (Essential) → 0 dấu phẩy ở cả hai đầu, đi thẳng vào động từ chính "identified" → Chọn A!',
            'Chức danh không mạo từ + Tên riêng + Động từ chính → tuyệt đối 0 dấu phẩy!',
            [
                ('Đáp án đúng', 'Không dấu phẩy — giữ liền chức danh bắt buộc + tên riêng với động từ chính "identified".'),
                ('Non-Essential Trap', 'Chỉ đặt cặp phẩy khi chức danh trước đó có mạo từ xác định duy nhất.'),
                ('No-Comma Zone (S, V)', 'Dấu phẩy đơn cắt đứt chủ ngữ khỏi động từ chính "identified".'),
                ('Unpaired Comma', 'Dấu phẩy lẻ sai vị trí giữa chức danh và tên riêng.'),
            ]
        ),
        q_item(
            'm7_m1_q18', 18, 'Standard English Conventions', 'Boundaries', 'Hard',
            '<p>In 2023, transit measurements of the warm exoplanet WASP-39 b confirmed a long-predicted photochemical ______ sulfur dioxide, a pungent gas formed only when intense ultraviolet starlight breaks apart hydrogen sulfide molecules high in the planet’s atmosphere.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['byproduct;', 'byproduct.', 'byproduct, it is', 'byproduct:'],
            'D',
            'Vế trái ("In 2023, transit measurements... confirmed a long-predicted photochemical byproduct") là 1 IC hoàn chỉnh. Vế phải ("sulfur dioxide, a pungent gas formed only when...") là Cụm danh từ đồng vị (Noun Phrase — KHÔNG có động từ chính chia thì, nên KHÔNG PHẢI IC!) chỉ tên cụ thể "byproduct" đó là gì → Dùng dấu hai chấm (:) = D!',
            'IC hoàn chỉnh + Cụm danh từ giải thích cụ thể (không phải IC) → Dấu hai chấm (:) là lựa chọn chuẩn duy nhất; cấm chấm phẩy (;) và dấu chấm (.)!',
            [
                ('Semicolon + Fragment', 'Vế sau "sulfur dioxide, a pungent gas..." là cụm danh từ, không phải IC → cấm dấu chấm phẩy.'),
                ('Period + Fragment', 'Tách cụm danh từ thành câu độc lập gây lỗi Sentence Fragment.'),
                ('Comma Splice', '"byproduct, it is sulfur dioxide..." ghép 2 IC bằng dấu phẩy → lỗi Comma Splice.'),
                ('Đáp án đúng', 'Dấu hai chấm (:) sau IC giới thiệu chính xác sản phẩm quang hóa được đề cập.'),
            ]
        ),
        q_item(
            'm7_m1_q19', 19, 'Standard English Conventions', 'Boundaries', 'Hard',
            '<p>Beaver dam analogs—low-tech woven willow barriers installed by restoration crews to mimic natural rodent ______ have rapidly raised dry-season water tables across degraded rangeland streams in Oregon and Idaho.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['dams,', 'dams—', 'dams;', 'dams'],
            'B',
            'Cụm giải thích xen giữa Chủ ngữ ("Beaver dam analogs") và Động từ chính ("have rapidly raised") mở đầu bằng gạch ngang dài (`—low-tech woven willow barriers...`) → Bắt buộc đóng bằng gạch ngang dài thứ hai (`dams—`) → Chọn B!',
            'Quy tắc đối xứng dấu cặp: Mở bằng em-dash (—) → Phải đóng bằng em-dash (—), cấm pha trộn với dấu phẩy hay chấm phẩy!',
            [
                ('Mismatched Pair (— ... ,)', 'Không được mở bằng gạch ngang rồi đóng bằng dấu phẩy.'),
                ('Đáp án đúng', 'Đóng đúng cặp gạch ngang đôi (— ... —) trước động từ chính "have rapidly raised".'),
                ('Semicolon Inside Modifier', 'Dấu chấm phẩy phá vỡ cấu trúc chủ ngữ – động từ.'),
                ('Unclosed Modifier', 'Thiếu dấu đóng khiến mệnh đề bị dính liền vào động từ chính.'),
            ]
        ),

        # --- Q20-Q22: Standard English Conventions — Form, Structure, and Sense ---
        q_item(
            'm7_m1_q20', 20, 'Standard English Conventions', 'Form, Structure, and Sense', 'Easy',
            '<p>A multi-year field survey of thirty-eight freshwater mussel beds along the upper Mississippi River ______ that dense native clam colonies trap significantly more synthetic microfibers in riverbed mud than sparse colonies do.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['indicate', 'have indicated', 'indicates', 'indicating'],
            'C',
            'Gạch cụm giới từ chen giữa: "A multi-year field <b>survey</b> <s>[of thirty-eight freshwater mussel beds along the upper Mississippi River]</s>". Chủ ngữ thật là "survey" (SỐ ÍT), câu cần động từ chính chia thì → Chọn "indicates" (C)!',
            'Đừng để bị đánh lừa bởi "thirty-eight freshwater mussel beds" (số nhiều) nằm trong cụm giới từ `of...` — chủ ngữ thật là `A... survey` (số ít)!',
            [
                ('Subject-Verb Mismatch', 'indicate là động từ số nhiều — không khớp chủ ngữ số ít "survey".'),
                ('Subject-Verb Mismatch', 'have indicated là động từ số nhiều.'),
                ('Đáp án đúng', 'indicates (số ít, hiện tại đơn) khớp chuẩn chủ ngữ "A multi-year field survey".'),
                ('Non-Finite Fragment', 'indicating là phân từ V-ing, làm câu thiếu động từ chính.'),
            ]
        ),
        q_item(
            'm7_m1_q21', 21, 'Standard English Conventions', 'Form, Structure, and Sense', 'Medium',
            '<p>Scored in 1934 for an eleven-piece Harlem jazz ensemble featuring four saxophones and three muted trombones, ______</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            [
                'the orchestral suite blends blues harmonies with shimmering impressionist woodwind voicings.',
                'composer Evelyn Brooks blended blues harmonies with shimmering impressionist woodwind voicings in the suite.',
                'Harlem audiences first heard blues harmonies blended with impressionist woodwind voicings at the Savoy.',
                'four brass soloists performed the suite’s blues harmonies alongside shimmering woodwind voicings.'
            ],
            'A',
            'Dangling Modifier Check! Cụm phân từ mở đầu "Scored in 1934 for an eleven-piece Harlem jazz ensemble..." (Được phối khí năm 1934 cho ban nhạc 11 người...) chỉ có thể bổ nghĩa cho TÁC PHẨM ÂM NHẠC ("the orchestral suite"), KHÔNG thể bổ nghĩa cho nhà soạn nhạc (B), khán giả (C), hay 4 nghệ sĩ kèn đồng (D) → Chọn A!',
            'Hỏi ngay: "Thứ gì được phối khí (Scored) cho ban nhạc 11 người?" → "the orchestral suite" phải đứng ngay sau dấu phẩy!',
            [
                ('Đáp án đúng', 'Chủ ngữ "the orchestral suite" đứng ngay sau dấu phẩy khớp hoàn hảo với phân từ "Scored...".'),
                ('Dangling Modifier', 'Nhà soạn nhạc Evelyn Brooks là người phối khí chứ không phải vật "được phối khí".'),
                ('Dangling Modifier', 'Khán giả Harlem không phải bản nhạc được phối khí.'),
                ('Dangling Modifier', 'Bốn nghệ sĩ kèn đồng không thể là đối tượng "Scored in 1934".'),
            ]
        ),
        q_item(
            'm7_m1_q22', 22, 'Standard English Conventions', 'Form, Structure, and Sense', 'Hard',
            '<p>Comparing field recordings collected across highland Peru, dialectologists noted that the aspirated stop consonant system of Cuzco Quechua differs markedly from ______ Ancash Quechua, which preserves older palatal sounds lost farther south.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['those of', 'the dialect of', 'them in', 'that of'],
            'D',
            'So sánh tương đồng (Apples-to-Apples): Đối tượng ở vế 1 là "<b>the aspirated stop consonant system</b>" (hệ thống phụ âm tắc bật hơi — danh từ SỐ ÍT!). So sánh với hệ thống tương ứng của tiếng Ancash Quechua → Bắt buộc dùng đại từ thay thế SỐ ÍT "<b>that of</b>" (D)! Loại A ("those of" cho số nhiều) và B (so sánh "hệ thống phụ âm" với cả "phương ngữ").',
            'Kiểm tra danh từ trung tâm được so sánh: "system" là SỐ ÍT → chọn "that of" (chỉ dùng "those of" khi danh từ gốc là số nhiều)!',
            [
                ('Pronoun Number Mismatch', '"those of" thay thế danh từ số nhiều, nhưng "the... system" là số ít.'),
                ('Illogical Comparison', 'So sánh "hệ thống phụ âm" với cả "phương ngữ" (the dialect) là lệch cấp.'),
                ('Pronoun Number & Form Error', '"them in" sai cả số nhiều lẫn cấu trúc so sánh học thuật.'),
                ('Đáp án đúng', '"that of" thay thế chuẩn xác cho danh từ số ít "the aspirated stop consonant system of".'),
            ]
        ),

        # --- Q23-Q25: Expression of Ideas — Transitions ---
        q_item(
            'm7_m1_q23', 23, 'Expression of Ideas', 'Transitions', 'Easy',
            '<p>Drumlins are smooth, teardrop-shaped hills sculpted parallel to the direction of advancing continental ice sheets. ______, terminal moraines form jagged, irregular ridges running perpendicular to the glacier’s former path where melting ice dumped rocky debris.</p>',
            'Which choice completes the text with the most logical transition?',
            ['Consequently', 'By contrast', 'Furthermore', 'For instance'],
            'B',
            'Câu 1: Đồi drumlin nhẵn, chạy SONG SONG hướng băng tiến. Câu 2: Băng tích cuối (terminal moraines) gồ ghề, chạy VUÔNG GÓC với đường băng → Đối chiếu trực tiếp hai địa hình băng hà trái ngược nhau → "By contrast" (B)!',
            'So sánh 2 đối tượng đối lập về hình dạng & phương hướng (smooth/parallel ↔ jagged/perpendicular) → chọn "By contrast".',
            [
                ('Wrong Relationship (Cause-Effect)', 'Hình dạng drumlin không gây ra hình dạng băng tích cuối.'),
                ('Đáp án đúng', 'By contrast nối chính xác phép đối chiếu trực diện giữa drumlin và băng tích cuối.'),
                ('Wrong Relationship (Addition)', 'Hai câu đối lập hình thái, không phải bổ sung cùng chiều.'),
                ('Wrong Relationship (Example)', 'Terminal moraines không phải ví dụ con của drumlins.'),
            ]
        ),
        q_item(
            'm7_m1_q24', 24, 'Expression of Ideas', 'Transitions', 'Medium',
            '<p>Because cooler red-dwarf stars are far smaller than our Sun, an Earth-sized exoplanet passing across a red dwarf blocks a proportionally much larger fraction of the star’s light. ______, astronomers can measure atmospheric transmission spectra for rocky worlds orbiting red dwarfs far more readily than for identical planets orbiting Sun-like stars.</p>',
            'Which choice completes the text with the most logical transition?',
            ['Nevertheless', 'Meanwhile', 'Consequently', 'Similarly'],
            'C',
            'Câu 1 (Nguyên nhân): Sao lùn đỏ nhỏ hơn nhiều nên hành tinh cỡ Trái Đất che khuất tỷ lệ ánh sáng lớn hơn nhiều. Câu 2 (Hệ quả): Nhà thiên văn đo quang phổ truyền qua của các hành tinh đá quanh sao lùn đỏ dễ dàng hơn hẳn → Quan hệ Nhân – Quả → "Consequently" (C)!',
            'Cặp câu mở đầu bằng "Because [Nguyên nhân]" → câu sau nêu kết quả trực tiếp trong quan sát thiên văn → "Consequently / Therefore".',
            [
                ('False Contrast', 'Nevertheless chỉ sự trái kỳ vọng — sai hoàn toàn hướng nhân quả.'),
                ('Wrong Relationship (Time)', 'Meanwhile diễn tả sự việc song song về thời gian, không nêu hệ quả.'),
                ('Đáp án đúng', 'Consequently liên kết chuẩn xác lợi thế hình học ở câu 1 với kết quả đo quang phổ dễ hơn ở câu 2.'),
                ('Wrong Relationship (Similarity)', 'Câu 2 là hệ quả trực tiếp chứ không phải sự tương đồng độc lập.'),
            ]
        ),
        q_item(
            'm7_m1_q25', 25, 'Expression of Ideas', 'Transitions', 'Hard',
            '<p>In her 1927 cultural essays, critic Nora Delacroix did not treat jazz improvisation as an impulsive departure from musical discipline. ______, she analyzed swing solos as a rigorous compositional craft demanding instant mastery of harmonic progression and rhythmic architecture.</p>',
            'Which choice completes the text with the most logical transition?',
            ['Instead', 'Moreover', 'Therefore', 'Still'],
            'A',
            'Câu 1 phủ định rõ ("did NOT treat jazz improvisation as an impulsive departure..."). Câu 2 đưa ra cách tiếp cận THAY THẾ đối lập hoàn toàn ("analyzed swing solos as a rigorous compositional craft...") → Cấu trúc "Not X; Instead, Y" → Chọn "Instead" (A)!',
            'Dấu hiệu kinh điển của "Instead": câu 1 phủ định quan niệm X (`did not treat...`), câu 2 thay thế bằng hành động/góc nhìn Y!',
            [
                ('Đáp án đúng', 'Instead khớp tuyệt đối với cấu trúc bác bỏ X và thay thế bằng quan điểm Y.'),
                ('Wrong Relationship (Addition)', 'Moreover nối hai ý cùng khẳng định, sai sau mệnh đề phủ định đối lập.'),
                ('Wrong Relationship (Cause-Effect)', 'Không phải quan hệ nguyên nhân – kết quả.'),
                ('Contrast Nuance Trap', 'Still (= Nevertheless) mang nghĩa "tuy vậy vẫn..." thay vì thay thế hoàn toàn hành động ở câu phủ định.'),
            ]
        ),

        # --- Q26-Q27: Expression of Ideas — Rhetorical Synthesis ---
        q_item(
            'm7_m1_q26', 26, 'Expression of Ideas', 'Rhetorical Synthesis', 'Medium',
            '''<p>While researching a topic, a student has taken the following notes:</p>
            <ul>
              <li>North American beavers build porous timber-and-mud dams across shallow mountain creeks.</li>
              <li>Water backed up behind a beaver dam is forced down into gravel riverbeds and re-emerges downstream as cool subsurface flow.</li>
              <li>Hydrologists in Washington’s Methow Valley measured stream temperatures up to 2.5°C cooler immediately below active beaver dam complexes during August heat waves.</li>
              <li>Native juvenile steelhead trout require cold, well-oxygenated water pockets to survive late-summer heat waves.</li>
            </ul>''',
            'The student wants to explain how beaver dams help native steelhead trout survive late-summer heat waves. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
            [
                'North American beavers construct porous timber-and-mud dams across shallow creeks in Washington’s Methow Valley.',
                'Native juvenile steelhead trout depend on cold, well-oxygenated stream pockets during August heat waves.',
                'By forcing backed-up creek water through gravel beds so it re-emerges up to 2.5°C cooler downstream, beaver dams create the cold-water pockets that juvenile steelhead trout need to survive late-summer heat waves.',
                'Hydrologists studying Washington’s Methow Valley recorded August stream temperatures immediately downstream of active beaver dam complexes.'
            ],
            'C',
            'Goal-First SOP: Giải thích CÁCH THỨC (HOW) đập hải ly giúp cá hồi steelhead sống sót qua sóng nhiệt cuối hè. A, B, D mỗi câu chỉ chép lại 1 gạch đầu dòng rời rạc. Duy nhất C nối trọn chuỗi cơ chế: đẩy nước qua lớp sỏi đáy → trồi lên mát hơn tới 2,5°C ở hạ lưu → tạo hốc nước lạnh giúp cá hồi con sống sót qua sóng nhiệt! Chọn C!',
            'Mục tiêu có chữ "explain HOW X helps Y" → đáp án phải nối đầy đủ cả cơ chế làm mát nước lẫn lợi ích cho cá hồi steelhead.',
            [
                ('Missing Mechanism & Trout', 'Chỉ nói hải ly xây đập gỗ bùn ở Methow Valley, bỏ qua hoàn toàn cơ chế làm mát và cá hồi.'),
                ('Missing Beaver Mechanism', 'Chỉ nêu nhu cầu nước lạnh của cá hồi mà không nói đập hải ly giúp ích ra sao.'),
                ('Đáp án đúng', 'Tổng hợp trọn vẹn cơ chế thấm qua tầng sỏi làm mát tới 2,5°C và liên hệ trực tiếp tới sự sống sót của cá hồi steelhead.'),
                ('Incomplete Synthesis', 'Chỉ nói nhà thủy văn đo nhiệt độ mà không nêu kết quả hay vai trò đối với cá hồi.'),
            ]
        ),
        q_item(
            'm7_m1_q27', 27, 'Expression of Ideas', 'Rhetorical Synthesis', 'Hard',
            '''<p>While researching a topic, a student has taken the following notes:</p>
            <ul>
              <li>Early Edo-period woodblock printmakers frequently used <i>aigami</i>, an organic blue dye extracted from Asiatic dayflower petals.</li>
              <li><i>Aigami</i> produced delicate translucent sky tones, but it faded rapidly when exposed to sunlight or humidity.</li>
              <li>Around 1830, synthetic Prussian blue (<i>bero-ai</i>) arrived in Japan through Dutch traders in Nagasaki.</li>
              <li>Prussian blue was chemically lightfast and enabled bold, high-contrast shading across broad ocean and sky expanses.</li>
            </ul>''',
            'The student wants to emphasize a contrast in durability and visual effect between <i>aigami</i> and Prussian blue in Edo-period woodblock prints. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
            [
                'Both <i>aigami</i> and synthetic Prussian blue (<i>bero-ai</i>) were blue pigments used by Edo-period woodblock printmakers in Japan.',
                'Whereas the organic dayflower dye <i>aigami</i> yielded delicate translucent tints that faded rapidly in light or humidity, synthetic Prussian blue was lightfast and enabled bold, high-contrast shading.',
                'Synthetic Prussian blue arrived in Japan around 1830 via Dutch traders in Nagasaki and quickly became known as <i>bero-ai</i>.',
                'Early Edo-period printmakers extracted <i>aigami</i> from Asiatic dayflower petals to color delicate sky areas before 1830.'
            ],
            'B',
            'Goal-First SOP: Nhấn mạnh SỰ TƯƠNG PHẢN về ĐỘ BỀN (durability) và HIỆU ỨNG THỊ GIÁC (visual effect) giữa <i>aigami</i> và Prussian blue. A chỉ nêu điểm chung; C và D mỗi câu chỉ nói một loại màu. Duy nhất B dùng "Whereas" đối chiếu trực diện cả 2 tiêu chí: <i>aigami</i> (sắc nhẹ trong mờ + phai nhanh) ↔ Prussian blue (bền sáng + chuyển sắc đậm tương phản cao)! Chọn B!',
            'Goal yêu cầu "contrast in X and Y between A and B" → kiểm tra đủ 4 mảnh: tên A, tên B, tiêu chí độ bền, tiêu chí hiệu ứng thị giác!',
            [
                ('Similarity Instead of Contrast', 'Nhấn mạnh điểm chung (cả hai đều là màu xanh) thay vì sự tương phản.'),
                ('Đáp án đúng', 'Đối chiếu song song cả độ bền màu (faded rapidly ↔ lightfast) lẫn hiệu ứng thị giác (delicate translucent ↔ bold, high-contrast).'),
                ('One-Sided Information', 'Chỉ kể lịch sử nhập khẩu của Prussian blue, thiếu hoàn toàn aigami và sự đối chiếu.'),
                ('One-Sided Information', 'Chỉ nói về aigami, không so sánh với Prussian blue.'),
            ]
        ),
    ]
