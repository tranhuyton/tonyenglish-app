# -*- coding: utf-8 -*-
"""
Hand-crafted 1500+ Elite Digital SAT R&W Skill Drills (Module 5 Hard M2 Gauntlet):
- Drill 5.1: Central Ideas & Details (13 Qs)
- Drill 5.2: Command of Evidence — Scientific Claims (13 Qs)
- Drill 5.3: Command of Evidence — Literary & Historical Quotations (13 Qs)
"""

from sat_drills_1_1_and_2_1 import q_item

def get_drill_5_1():
    questions = [
        q_item(
            'd5_1_q1', 1, 'Information and Ideas', 'Central Ideas and Details', 'Hard',
            '<p>While excavating an eighth-century Viking trading outpost at Ribe, Denmark, archaeologists recovered thousands of glass beads whose chemical trace elements matched workshops in the eastern Mediterranean and Mesopotamia rather than northern Europe. Because these beads turned up even in modest craft cottages rather than solely in royal burial mounds, historians argue that long-distance Eurasian trade networks reached ordinary Scandinavian households far earlier than previously assumed.</p>',
            'Which choice best states the main idea of the text?',
            [
                'Chemical analyses of glass beads from Ribe suggest that long-distance Eurasian trade penetrated ordinary Scandinavian life earlier than scholars once thought.',
                'Eighth-century Danish craftspeople learned how to manufacture Mediterranean-style glass beads inside their own modest cottages.',
                'Royal Viking burial mounds in Denmark contain no glass beads originating from Mesopotamia or the eastern Mediterranean.',
                'The trading outpost at Ribe was larger and wealthier than contemporary ports in Mesopotamia.'
            ],
            'A',
            'Trục lập luận toàn đoạn: (1) Hạt thủy tinh từ Đông Địa Trung Hải/Lưỡng Hà được tìm thấy tại Ribe; (2) Xuất hiện ở cả nhà thợ thủ công bình dân chứ không chỉ mộ hoàng gia → Kết luận: mạng lưới thương mại Á–Âu đường dài đã chạm tới đời sống người dân Scandinavia bình thường sớm hơn giả định trước đây (A)!',
            'Ghép bằng chứng (glass beads from Mediterranean/Mesopotamia in modest cottages) + kết luận (reached ordinary households earlier than assumed).',
            [
                ('Đáp án đúng', 'Tóm gọn chính xác bằng chứng hóa học từ hạt thủy tinh ở Ribe và kết luận về thương mại đường dài lan tới tầng lớp bình dân.'),
                ('Contradiction', 'Phân tích hóa học cho thấy hạt được chế tạo ở Đông Địa Trung Hải và Lưỡng Hà rồi nhập khẩu, KHÔNG phải do thợ Đan Mạch tự làm.'),
                ('Distortion / Too Extreme', 'Bài nói "rather than solely in royal burial mounds" (không CHỈ ở mộ hoàng gia), chứ không nói mộ hoàng gia không có hạt nào!'),
                ('Unsupported Comparison', 'Không hề so sánh quy mô hay sự giàu có giữa Ribe và cảng Lưỡng Hà.'),
            ]
        ),
        q_item(
            'd5_1_q2', 2, 'Information and Ideas', 'Central Ideas and Details', 'Hard',
            '<p>In 2022, botanist Dr. Elena Varga investigated why alpine cushion plants in the Carpathian Mountains frequently shelter seedlings of completely unrelated wildflower species within their dense mossy domes. By embedding micro-thermometers inside and outside the cushions during late-spring frosts, Varga recorded daytime soil temperatures up to 7°C warmer inside the domes and wind speeds reduced by eighty percent—demonstrating that these hardy "nurse plants" act as biological micro-greenhouses in severe alpine zones.</p>',
            'According to the text, how do alpine cushion plants benefit seedlings of unrelated wildflower species?',
            [
                'By secreting specialized soil nutrients that accelerate wildflower root growth during winter.',
                'By creating a sheltered microclimate inside their dense domes that raises daytime soil warmth and blocks harsh winds.',
                'By attracting alpine pollinators that cross-fertilize both the cushion plants and the neighboring wildflowers.',
                'By preventing snow from accumulating on Carpathian Mountain slopes during late spring.'
            ],
            'B',
            'Câu hỏi Specific Detail ("According to the text, how do..."): Định vị trực tiếp câu đo bằng micro-thermometer → nhiệt độ đất ban ngày ấm hơn tới 7°C và tốc độ gió giảm 80%, đóng vai trò như "nhà kính sinh học thu nhỏ" (biological micro-greenhouses) → Paraphrase hoàn hảo ở B!',
            'Với câu hỏi Detail, bám sát 100% cơ chế thực nghiệm được nêu đích danh trong đoạn (warmth +80% wind reduction).',
            [
                ('Out of Scope', 'Không hề nhắc đến việc tiết chất dinh dưỡng đất.'),
                ('Đáp án đúng', 'Diễn giải sát nghĩa hoàn hảo kết quả đo nhiệt độ ấm hơn 7°C và giảm 80% tốc độ gió bên trong vòm cây.'),
                ('Out of Scope', 'Không đề cập côn trùng thụ phấn.'),
                ('Out of Scope', 'Không nói cây ngăn tuyết tích tụ trên sườn núi.'),
            ]
        ),
        q_item(
            'd5_1_q3', 3, 'Information and Ideas', 'Central Ideas and Details', 'Elite (750+)',
            '<p><i>The following text is adapted from an 1889 novel. Julian, a young botanist, is writing to his sister after spending six months cataloging ferns on a rainy Scottish island.</i><br/>You asked whether the relentless mist has soured my spirits or turned me impatient for London’s paved avenues. On the contrary, I find that a week of steady rain strips away the trivial haste of city correspondence; when the ferry arrives only on alternate Thursdays, one learns to examine a single frond of spleenwort with a patience that no crowded lecture hall ever taught me.</p>',
            'Based on the text, how has living on the Scottish island affected Julian?',
            [
                'It has made him deeply homesick for the intellectual stimulation of London’s crowded lecture halls.',
                'It has prevented him from completing his fern catalog because the irregular ferry delays his supplies.',
                'It has cultivated in him a slower, more attentive way of observing nature free from urban urgency.',
                'It has convinced him to abandon botany permanently and settle on the island as a ferryman.'
            ],
            'C',
            'Đọc câu trả lời trực tiếp của Julian sau "On the contrary": mưa liên miên gột bỏ sự vội vã tầm thường của thành phố; chuyến phà cách tuần dạy anh sự kiên nhẫn quan sát từng nhánh dương xỉ sâu sắc hơn bất kỳ giảng đường đông đúc nào → Chọn C!',
            'Trong văn học cổ, chú ý cụm đảo chiều "On the contrary" — Julian phủ nhận nỗi buồn chán và ca ngợi sự điềm tĩnh sâu sắc mà hòn đảo mang lại.',
            [
                ('Contradiction', 'Anh phủ nhận sự nóng lòng trở về London ("On the contrary").'),
                ('Out of Scope / Distortion', 'Phà thưa chuyến giúp anh học tính kiên nhẫn, không hề nói thiếu tiếp tế hay đình trệ việc lập danh mục.'),
                ('Đáp án đúng', 'Paraphrase tinh tế cả hai vế: "strips away trivial haste" (free from urban urgency) + "examine with a patience" (more attentive way of observing).'),
                ('Out of Scope', 'Không có ý định bỏ ngành thực vật học hay làm người lái phà.'),
            ]
        ),
        q_item(
            'd5_1_q4', 4, 'Information and Ideas', 'Central Ideas and Details', 'Elite (750+)',
            '<p>During the 1950s, urban sociologists assumed that residents displaced from older dense neighborhoods into newly built high-rise public housing towers would quickly form close-knit social ties thanks to modern elevators and shared hallways. Longitudinal interviews conducted by Jane Jacobs and later researchers, however, found that vertical corridors lacked the casual "eyes on the street" created by ground-level stoops and corner grocers, leaving many tower residents reporting greater isolation despite living physically closer to more neighbors.</p>',
            'Which choice best states the main idea of the text?',
            [
                'Modern elevators and shared hallways were too costly to maintain in 1950s public housing towers.',
                'Residents of older neighborhoods refused to move into high-rise housing towers during the 1950s.',
                'Jane Jacobs demonstrated that living physically far away from neighbors is the sole cause of urban loneliness.',
                'Contrary to 1950s expectations, high-rise housing towers often increased social isolation because vertical layouts lacked informal street-level spaces for neighborly contact.'
            ],
            'D',
            'Mạch đoạn: Giả định thập niên 1950 (chung cư cao tầng sẽ gắn kết cộng đồng hơn) → "however" (phỏng vấn dài hạn cho thấy hành lang đứng thiếu không gian giao tiếp tự nhiên cấp mặt phố như bậc thềm, tiệm tạp hóa góc phố → cư dân cô lập hơn dù ở gần nhau về mặt vật lý) → Chọn D!',
            'Khớp trọn bước ngoặt "assumed X... however, found Y because Z".',
            [
                ('Out of Scope', 'Không bàn chi phí bảo trì thang máy.'),
                ('Contradiction', 'Đoạn văn nói về cư dân ĐÃ chuyển vào các tòa tháp ("displaced... into newly built towers").'),
                ('Too Extreme / Contradiction', 'Cư dân chung cư sống RẤT GẦN nhau về mặt vật lý nhưng vẫn cô lập hơn — trái ngược "living physically far away".'),
                ('Đáp án đúng', 'Gói gọn đầy đủ sự đối lập với kỳ vọng thập niên 1950, kết quả cô lập xã hội tăng lên và nguyên nhân thiếu không gian tương tác mặt phố.'),
            ]
        ),
        q_item(
            'd5_1_q5', 5, 'Information and Ideas', 'Central Ideas and Details', 'Hard',
            '<p>Unlike ordinary steel beams that bend abruptly when overloaded, modern "shape-memory alloy" dampers installed in Japanese earthquake-resistant bridges undergo a reversible crystal-phase shift under severe tremor stress. As soon as ground shaking subsides, the nickel-titanium alloy springs back to its original geometry, allowing the bridge deck to recenter itself automatically rather than requiring expensive structural demolition after a major quake.</p>',
            'According to the text, what key advantage do shape-memory alloy dampers offer over ordinary steel beams during an earthquake?',
            [
                'They absorb extreme tremor stress through a reversible phase shift and return to their original shape afterward, helping the bridge self-recenter.',
                'They are significantly less expensive to mine and manufacture than conventional carbon steel.',
                'They completely prevent seismic waves from reaching bridge foundations during major earthquakes.',
                'They permanently harden into a rigid crystalline block after experiencing their first tremor.'
            ],
            'A',
            'So sánh trực tiếp trong bài: thép thường bị cong gãy vĩnh viễn khi quá tải ("bend abruptly"); ngược lại, bộ giảm chấn hợp kim nhớ hình chuyển pha tinh thể thuận nghịch và tự bật về hình dạng ban đầu giúp mặt cầu tự căn chỉnh lại (A)!',
            'Cảnh giác bẫy Too Extreme (C: "completely prevent seismic waves") và Contradiction (D: "permanently harden" trái với "reversible")!',
            [
                ('Đáp án đúng', 'Bám sát 100% cơ chế "reversible crystal-phase shift" và lợi ích tự khôi phục hình dạng/căn chỉnh lại cầu.'),
                ('Out of Scope', 'Đoạn văn nói tránh chi phí phá dỡ sau động đất, KHÔNG nói hợp kim niken-titan rẻ hơn thép khi khai thác sản xuất.'),
                ('Too Extreme', 'Giảm chấn giúp cầu chịu tải và tự cân chỉnh lại, không thể "ngăn hoàn toàn sóng địa chấn tới móng cầu".'),
                ('Contradiction', 'Đoạn văn nhấn mạnh chuyển pha thuận nghịch ("reversible"), không phải hóa cứng vĩnh viễn.'),
            ]
        ),
        q_item(
            'd5_1_q6', 6, 'Information and Ideas', 'Central Ideas and Details', 'Elite (750+)',
            '<p>Paleontologists once wondered how massive sauropod dinosaurs such as <i>Argentinosaurus</i>—weighing over seventy metric tons—avoided collapsing under their own skeletal mass. High-resolution CT scans of fossilized vertebrae have revealed that sauropod neck and back bones were honeycombed with air sacs connected to an avian-style respiratory system, dramatically reducing skeletal weight while preserving high structural stiffness through thin internal struts.</p>',
            'Which choice best states the main idea of the text?',
            [
                'CT scanning technology has revealed that modern birds evolved directly from <i>Argentinosaurus</i>.',
                'Internal air-filled cavities reinforced by thin struts allowed massive sauropods to lighten their skeletons without sacrificing structural strength.',
                'Sauropod dinosaurs weighed less than seventy metric tons because their vertebrae contained hollow chambers.',
                'Fossilized sauropod vertebrae are too fragile to be examined without specialized avian respiratory models.'
            ],
            'B',
            'Câu hỏi khoa học (làm sao khủng long cổ dài >70 tấn không bị sập dưới sức nặng khung xương) → phát hiện CT: xương sống rỗng tổ ong chứa túi khí nối hệ hô hấp kiểu chim giúp giảm mạnh trọng lượng mà vẫn giữ độ cứng nhờ thanh chống mỏng bên trong → Chọn B!',
            'Tránh bẫy Distortion (A: "avian-style" = kiểu chim, KHÔNG có nghĩa chim tiến hóa trực tiếp từ Argentinosaurus; C: bẻ ngược trọng lượng >70 tấn đã tính cả xương rỗng rồi!).',
            [
                ('Subtle Distortion', '"avian-style respiratory system" chỉ sự tương đồng về kiểu hô hấp, không nói chim hiện đại tiến hóa trực tiếp từ Argentinosaurus.'),
                ('Đáp án đúng', 'Tổng hợp chính xác cả 2 chức năng của xương tổ ong: giảm trọng lượng (lighten skeletons) nhưng vẫn giữ độ cứng vững (without sacrificing structural strength).'),
                ('Contradiction', 'Đoạn văn nêu rõ loài này nặng HƠN 70 tấn ("weighing over seventy metric tons").'),
                ('Out of Scope / Distortion', 'Không nói hóa thạch quá mong manh để kiểm tra.'),
            ]
        ),
        q_item(
            'd5_1_q7', 7, 'Information and Ideas', 'Central Ideas and Details', 'Elite (750+)',
            '<p>Historian Dr. Miriam Al-Khatib analyzed 340 merchant contracts preserved in the Cairo Geniza—a medieval synagogue storeroom—dating from the eleventh and twelfth centuries. Rather than relying solely on formal royal courts when cross-border disputes arose between traders in Alexandria and Sicily, merchants predominantly enforced contracts through dense reputation networks: a trader who cheated a single partner risked immediate ostracism from credit and shipping consortia across the entire Mediterranean.</p>',
            'According to the text, how did medieval Mediterranean merchants documented in the Cairo Geniza mainly ensure that distant trading partners honored contracts?',
            [
                'By stationing armed royal court officials aboard every commercial vessel sailing between Alexandria and Sicily.',
                'By requiring all trading partners to store their written contracts inside the Cairo Geniza before departure.',
                'Through tightly linked reputation networks in which dishonest behavior led to swift exclusion from regional credit and shipping groups.',
                'By restricting trade exclusively to family members residing in the same port city.'
            ],
            'C',
            'Tìm đúng câu trả lời trong bài: "merchants predominantly enforced contracts through dense reputation networks: a trader who cheated a single partner risked immediate ostracism from credit and shipping consortia" → Paraphrase hoàn hảo ở C!',
            'Chú ý chữ "mainly" trong câu hỏi khớp trực tiếp với chữ "predominantly" trong đoạn văn!',
            [
                ('Out of Scope', 'Không hề nhắc đến quan chức vũ trang trên tàu.'),
                ('Distortion', 'Cairo Geniza là nơi các hợp đồng được lưu giữ lại tới ngày nay, không phải cơ chế ép thi hành hợp đồng trước khi khởi hành.'),
                ('Đáp án đúng', 'Diễn đạt lại chính xác cơ chế mạng lưới uy tín và nguy cơ bị tẩy chay khỏi nhóm tín dụng–vận tải khu vực.'),
                ('Contradiction', 'Đoạn văn nói rõ thương mại XUYÊN BIÊN GIỚI ("cross-border disputes between Alexandria and Sicily"), không bó hẹp trong một thành phố.'),
            ]
        ),
        q_item(
            'd5_1_q8', 8, 'Information and Ideas', 'Central Ideas and Details', 'Hard',
            '<p><i>The following text is adapted from a 1915 poem about a prairie windmill standing beside an abandoned homestead.</i><br/>The gate hangs loose upon a single hinge,<br/>The clapboard roof has yielded to the snow;<br/>Yet still the iron wheel above the ridge<br/>Turns tirelessly against the western blow,<br/>Pumping clear silver to an empty trough<br/>Where neither horse nor herdsman comes to drink.</p>',
            'Which choice best states the main idea of the text?',
            [
                'A fierce winter snowstorm has permanently broken the iron wheel of an old prairie windmill.',
                'A herdsman returns to an abandoned prairie farm each winter to repair its broken wooden gate.',
                'Prairie windmills are more reliable sources of clean water than natural streams during droughts.',
                'An old windmill continues operating steadfastly even though the farm and people it once served are long gone.'
            ],
            'D',
            'Hai dòng đầu tả trang trại đã hoang phế ("gate hangs loose", "roof yielded to snow"). Bốn dòng sau dùng "Yet still" tả bánh xe sắt vẫn quay không mệt mỏi bơm nước trong vào máng trống không có bóng ngựa hay người chăn → Chọn D!',
            'Bám đúng cặp đối lập trong thơ: trang trại đổ nát/bỏ hoang ↔ cối xay gió vẫn bền bỉ vận hành vô ích cho máng nước trống.',
            [
                ('Contradiction', 'Bánh xe sắt vẫn "turns tirelessly" (quay không ngừng nghỉ), không bị gãy.'),
                ('Contradiction', 'Dòng cuối nói rõ "Where neither horse nor herdsman comes to drink" (không có ai quay lại).'),
                ('Out of Scope', 'Bài thơ không so sánh cối xay gió với suối tự nhiên.'),
                ('Đáp án đúng', 'Tóm gọn chính xác hình ảnh tương phản cốt lõi của bài thơ.'),
            ]
        ),
        q_item(
            'd5_1_q9', 9, 'Information and Ideas', 'Central Ideas and Details', 'Elite (750+)',
            '<p>When audio engineers first digitized classic analog vinyl albums in the 1980s, many listeners complained that compact discs sounded strangely "sterile" compared with warm vinyl pressings. Acoustic physicist Dr. Tomasz Kowalski notes that although digital CDs objectively capture a wider dynamic range and lower background hiss, subtle harmonic distortions produced by a diamond stylus vibrating inside a vinyl groove add faint overtones that human ears often interpret as richness and warmth.</p>',
            'Based on the text, why do some listeners perceive analog vinyl recordings as sounding "warmer" than digital CDs?',
            [
                'Minor harmonic distortions created by the physical stylus-in-groove playback introduce subtle overtones perceived as tonal richness.',
                'Digital compact discs are incapable of reproducing the full dynamic range found on analog vinyl pressings.',
                'Listeners in the 1980s lacked high-quality stereo speakers capable of playing compact discs properly.',
                'Vinyl pressings completely eliminate all background hiss that mars digital recordings.'
            ],
            'A',
            'Đọc kỹ câu 2: CD khách quan có dải động rộng hơn và ít tiếng rè hơn (nên loại ngay B và D — cả hai đều đảo ngược sự thật!). Lý do đĩa than nghe "ấm" hơn là những méo hài tinh vi ("subtle harmonic distortions") do kim đọc rung trong rãnh đĩa tạo ra các họa âm nhẹ được tai người cảm nhận là độ dày/ấm → Chọn A!',
            'Cẩn thận bẫy Reversed Logic (B và D lật ngược ưu thế khách quan của CD thành ưu thế của đĩa than)!',
            [
                ('Đáp án đúng', 'Khớp từng chữ với giải thích của Dr. Kowalski về méo hài tinh vi của kim đĩa than tạo cảm giác giàu âm sắc.'),
                ('Reversed Logic', 'Bài nói ngược lại: CD khách quan bắt được dải động RỘNG HƠN ("wider dynamic range") đĩa than.'),
                ('Out of Scope', 'Không hề đề cập chất lượng loa thập niên 1980.'),
                ('Reversed Logic', 'Bài nói CD có tiếng rè nền THẤP HƠN ("lower background hiss"), không phải đĩa than.'),
            ]
        ),
        q_item(
            'd5_1_q10', 10, 'Information and Ideas', 'Central Ideas and Details', 'Hard',
            '<p>While modern GPS navigation relies on atomic clocks aboard orbiting satellites, traditional Polynesian wayfinders crossed thousands of kilometers of open Pacific Ocean without mechanical compasses or written charts. Navigators memorized a mental "star compass" of rising and setting constellations alongside subtle ocean swell refractions bouncing off unseen islands over fifty kilometers beyond the horizon, allowing double-hulled canoes to pinpoint tiny atolls with extraordinary precision.</p>',
            'Which choice best states the main idea of the text?',
            [
                'Polynesian double-hulled canoes traveled faster across the open Pacific than modern motorized vessels.',
                'By integrating memorized celestial patterns with readings of subtle ocean swells, traditional Polynesian navigators achieved precise long-distance voyaging without instruments.',
                'Modern GPS satellites were modeled directly after the traditional Polynesian mental star compass.',
                'Ocean swell refractions can only be detected within five kilometers of an island shoreline.'
            ],
            'B',
            'Ý chính toàn đoạn: Không cần la bàn cơ học hay hải đồ viết tay, các nhà hàng hải Polynesia kết hợp "la bàn sao" ghi nhớ trong đầu cùng việc đọc sóng lừng phản xạ từ đảo khuất chân trời để định vị chuẩn xác xuyên Thái Bình Dương → Chọn B!',
            'Gom đầy đủ cả 2 công cụ tự nhiên trong bài (celestial patterns + ocean swells) và kết quả (precise long-distance voyaging without instruments).',
            [
                ('Unsupported Comparison', 'Không hề so sánh tốc độ thuyền với tàu động cơ hiện đại.'),
                ('Đáp án đúng', 'Bao quát trọn vẹn phương pháp hàng hải không thiết bị của người Polynesia và độ chính xác ấn tượng của họ.'),
                ('Out of Scope', 'Bài chỉ đặt GPS làm mốc tương phản ban đầu, không nói GPS mô phỏng theo la bàn sao.'),
                ('Fact Distortion', 'Đoạn văn nói sóng lừng dội từ đảo cách HƠN 50 km ("over fifty kilometers"), không phải 5 km.'),
            ]
        ),
        q_item(
            'd5_1_q11', 11, 'Information and Ideas', 'Central Ideas and Details', 'Elite (750+)',
            '<p>In a 2023 linguistics study, Dr. Mei-Hua Lin examined why bilingual speakers occasionally insert a single word from Language B into a sentence spoken predominantly in Language A—a practice called code-switching. Challenging an outdated pedagogical stereotype that equated code-switching with vocabulary gaps or linguistic confusion, Lin’s corpus of 1,400 natural conversations revealed that over eighty percent of switched terms occurred precisely at grammatically valid clause boundaries and served to convey cultural nuances or social solidarity absent from direct translations.</p>',
            'According to the text, what did Dr. Mei-Hua Lin’s corpus analysis reveal about code-switching?',
            [
                'It occurs primarily when bilingual speakers have forgotten the equivalent word in their first language.',
                'It frequently violates the grammatical rules of both languages involved in a conversation.',
                'It predominantly respects grammatical boundaries and serves deliberate expressive or social purposes rather than stemming from confusion.',
                'It is used more often in formal written essays than in everyday spoken conversations.'
            ],
            'C',
            'Phân tích của Lin bác bỏ định kiến cũ (cho rằng do hổng từ vựng hay rối loạn ngôn ngữ — loại A & B), chỉ ra >80% diễn ra đúng ranh giới ngữ pháp hợp lệ nhằm truyền đạt sắc thái văn hóa hoặc sự gắn kết xã hội → Chọn C!',
            'Nhận diện cặp bác bỏ: "Challenging an outdated stereotype [A/B] ... revealed [C]"!',
            [
                ('Old Stereotype Trap', 'Đây chính là định kiến cũ ("outdated pedagogical stereotype") mà Lin bác bỏ!'),
                ('Contradiction', 'Hơn 80% xảy ra ở vị trí ranh giới mệnh đề ĐÚNG NGỮ PHÁP ("grammatically valid clause boundaries").'),
                ('Đáp án đúng', 'Khớp trọn kết quả khảo sát 1.400 hội thoại của Lin: tuân thủ ranh giới ngữ pháp và phục vụ sắc thái văn hóa/gắn kết xã hội.'),
                ('Out of Scope', 'Nghiên cứu chỉ phân tích hội thoại tự nhiên, không so sánh với văn viết trang trọng.'),
            ]
        ),
        q_item(
            'd5_1_q12', 12, 'Information and Ideas', 'Central Ideas and Details', 'Elite (750+)',
            '<p>For decades, museum conservators cleaned darkened Renaissance oil paintings using harsh alkaline solvents that stripped away yellowed nineteenth-century varnishes along with microscopic traces of the artist’s original translucent glazes. Recent adoption of custom-formulated hydrogel poultices—moist polymer films that release water molecules only into the top few microns of aged grime—enables restorers to lift surface soot selectively without disturbing underlying pigment layers.</p>',
            'Which choice best states the main idea of the text?',
            [
                'Nineteenth-century museum curators deliberately applied yellow varnish to conceal mistakes made by Renaissance artists.',
                'Most Renaissance oil paintings have already been permanently ruined by alkaline cleaning solvents.',
                'Hydrogel poultices are faster and cheaper to apply than traditional liquid solvents.',
                'Unlike older harsh solvents that risked damaging original paint glazes, modern hydrogel films allow conservators to remove surface grime with microscopic precision.'
            ],
            'D',
            'Cấu trúc tương phản trước – sau cực rõ: Dung môi kiềm cũ làm bong luôn lớp men màu nguyên bản ↔ Miếng dán hydrogel hiện đại chỉ giải phóng nước vào vài micron lớp bụi trên cùng, làm sạch chọn lọc mà không đụng lớp màu gốc → Chọn D!',
            'Giữ nguyên cặp đối chiếu cốt lõi (harsh solvents vs. selective hydrogel precision) và loại các bẫy suy diễn về chi phí hay tốc độ (C)!',
            [
                ('Out of Scope', 'Không nói người thế kỷ 19 cố tình phủ vecni vàng để che lỗi họa sĩ.'),
                ('Too Extreme', 'Đoạn văn nói dung môi cũ làm mất dấu vết vi mô lớp men, không nói "most paintings have been permanently ruined".'),
                ('Out of Scope', 'Không hề so sánh tốc độ hay giá thành giữa hai phương pháp.'),
                ('Đáp án đúng', 'Tóm gọn hoàn hảo sự cải tiến từ dung môi kiềm dễ làm hại lớp men gốc sang màng hydrogel làm sạch chọn lọc cấp độ micron.'),
            ]
        ),
        q_item(
            'd5_1_q13', 13, 'Information and Ideas', 'Central Ideas and Details', 'Hard',
            '<p>Although honeybees are famous for communicating food locations through the intricate "waggle dance," ecologist Dr. Samir Haddad found that when foraging in dense, structurally complex forests where floral patches are abundant within a hundred meters of the hive, scout bees frequently skip the directional dance altogether. Instead, recruits rely primarily on floral scents lingering on returning scouts’ bodies to locate nearby blossoms—suggesting that waggle-dance communication yields its greatest payoff mainly when food sources are sparse and distant.</p>',
            'Based on the text, when do honeybees rely most heavily on the waggle dance rather than solely on lingering floral scents?',
            [
                'When floral food patches are scarce and located far away from the hive.',
                'When dense forest canopies prevent returning scout bees from retaining floral scents on their bodies.',
                'When abundant flowers bloom within one hundred meters of the hive.',
                'When rival honeybee colonies compete for blossoms inside the same forest.'
            ],
            'A',
            'Câu cuối trả lời trực tiếp câu hỏi Detail: "suggesting that waggle-dance communication yields its greatest payoff mainly when food sources are <b>sparse and distant</b>" → Paraphrase hoàn hảo: "scarce and located far away from the hive" (A)!',
            'Tìm cụm từ chốt "yields its greatest payoff mainly when..." để định vị đáp án chính xác trong 5 giây!',
            [
                ('Đáp án đúng', 'Diễn đạt lại chính xác cụm "sparse and distant" (khan hiếm và ở xa tổ).'),
                ('Contradiction', 'Trong rừng rậm gần tổ, ong vẫn giữ mùi hoa trên cơ thể và DÙNG mùi hoa đó để tìm bông.'),
                ('Reversed Condition', 'Khi hoa dồi dào trong vòng 100m, ong trinh sát THƯỜNG BỎ QUA điệu nhảy ("skip the directional dance").'),
                ('Out of Scope', 'Không hề nhắc đến sự cạnh tranh giữa các đàn ong đối thủ.'),
            ]
        ),
    ]
    return {
        'schemaVersion': 1,
        'mode': 'drill',
        'section': 'Reading and Writing',
        'basicInfo': {
            'title': 'Drill 5.1: Central Ideas & Details — Hard Module 2 Prose & Poetry (13 Qs)',
            'subtitle': 'Luyện kỹ năng paraphrase chuẩn xác và nhận diện 4 bẫy Too Narrow / Too Broad / Unsupported Comparison / Subtle Distortion.',
            'difficultyBadge': 'I&I • Target 1500+',
            'targetTimeMinutes': 15,
        },
        'drillModule': {
            'id': 'drill_5_1_mod',
            'title': 'Skill Drill 5.1: Central Ideas & Details',
            'timeLimitMinutes': 15,
            'questions': questions,
        },
    }


def get_drill_5_2():
    questions = [
        q_item(
            'd5_2_q1', 1, 'Information and Ideas', 'Command of Evidence (Textual)', 'Hard',
            '<p>Plant physiologist Dr. Hannah Lindholm observed that wild tobacco plants bitten by hornworm caterpillars release airborne green-leaf volatiles within thirty minutes of attack. Lindholm hypothesized that these airborne compounds serve primarily as an indirect defense signal—summoning predatory big-eyed bugs from surrounding vegetation to feed on the caterpillars—rather than directly poisoning the caterpillars themselves.</p>',
            'Which finding, if true, would most directly support Dr. Hannah Lindholm’s hypothesis?',
            [
                'When hornworm caterpillars are reared in sealed chambers filled with concentrated tobacco green-leaf volatiles, they grow and feed normally; in open fields, however, plants engineered not to emit those volatiles attract far fewer predatory bugs and suffer triple the caterpillar damage.',
                'Wild tobacco plants produce significantly higher concentrations of green-leaf volatiles during dry summer afternoons than during cool spring mornings.',
                'Hornworm caterpillars immediately stop feeding and die within two hours when exposed to purified green-leaf volatiles in a predator-free laboratory cage.',
                'Big-eyed bugs feed on a wide variety of insect larvae in addition to hornworm caterpillars across desert ecosystems.'
            ],
            'A',
            'Khóa trục giả thuyết Lindholm: Volatiles (X) → Summon predatory bugs (Y1), NOT directly poison caterpillars (NOT Y2). Đáp án A chứng minh TRỌN VẸN CẢ 2 VẾ có đối chứng: (1) Trong buồng kín không có bọ săn mồi, khí không làm hại sâu (chứng minh NOT poison); (2) Ngoài đồng, cây bị tắt gen phát khí thu hút ít bọ săn mồi hơn hẳn và bị ăn hại gấp 3 lần (chứng minh indirect predator signal)!',
            'Bằng chứng Support hoàn hảo nhất cho giả thuyết "X works via Mechanism A rather than Mechanism B" phải kiểm chứng đồng thời CẢ A LẪN B bằng thí nghiệm đối chứng!',
            [
                ('Đáp án đúng', 'Củng cố đồng thời cả hai vế giả thuyết: chứng minh khí không trực tiếp đầu độc sâu VÀ việc tắt khí làm giảm hẳn bọ săn mồi khiến sâu phá gấp 3.'),
                ('Adjacent Topic Drift', 'Chênh lệch thời tiết sáng/chiều không kiểm chứng được cơ chế gọi thiên địch hay đầu độc.'),
                ('Opposite Direction (Weakens!)', 'Nếu khí trực tiếp giết chết sâu trong phòng thí nghiệm không có thiên địch → BÁC BỎ hoàn toàn giả thuyết của Lindholm!'),
                ('Adjacent Topic Drift', 'Chế độ ăn đa dạng của bọ săn mồi không chứng minh chúng bị thu hút bởi hợp chất bay hơi của cây thuốc lá.'),
            ]
        ),
        q_item(
            'd5_2_q2', 2, 'Information and Ideas', 'Command of Evidence (Textual)', 'Elite (750+)',
            '<p>Archaeologists excavating an Early Bronze Age coastal settlement in Oman discovered hundreds of copper fishhooks alongside fragments of bitumen-coated reed boats. Researcher Dr. Tariq Al-Harthi hypothesized that the settlement’s residents relied primarily on deep-water open-ocean fishing—venturing several kilometers offshore in reed boats—rather than shallow lagoon net-fishing to sustain their diet.</p>',
            'Which finding, if true, would most directly weaken Dr. Tariq Al-Harthi’s hypothesis?',
            [
                'Bitumen used to waterproof the reed boat fragments was imported from inland natural seepages located over fifty kilometers from the coast.',
                'Chemical and anatomical analysis of more than 4,000 fish bones excavated from the settlement’s cooking hearths reveals that 94% belonged to tiny juvenile reef and lagoon species rarely found outside calm, waist-deep coastal shallows.',
                'Several intact copper fishhooks recovered from the site show distinctive wear marks consistent with repeated immersion in saltwater.',
                'Contemporary Bronze Age settlements farther north along the Persian Gulf also constructed reed vessels waterproofed with bitumen.'
            ],
            'B',
            'Khóa giả thuyết Al-Harthi: Cư dân chủ yếu dựa vào đánh bắt BIỂN SÂU XA BỜ (deep-water open-ocean) chứ không phải đầm phá nông (shallow lagoon). Đòn WEAKEN chí mạng: Kiểm tra thẳng thực đơn thực tế trong bếp lửa (4.000 xương cá) → 94% là cá nhỏ sống ở đầm phá nước nông đến thắt lưng! Bác bỏ thẳng giả thuyết đánh bắt biển sâu chủ đạo → Chọn B!',
            'Trong khảo cổ học, bằng chứng trực tiếp nhất về chế độ ăn thực tế là phân tích xương/hóa thạch thức ăn trong bếp lửa (direct dietary evidence).',
            [
                ('Adjacent Topic Drift', 'Nguồn gốc nhựa đường nhập từ nội địa không cho biết thuyền dùng đi biển sâu hay đi ven bờ/giao thương.'),
                ('Đáp án đúng', 'Bằng chứng xương cá trực tiếp (94% cá đầm phá nước nông) đánh sập giả thuyết chủ yếu đánh bắt biển sâu xa bờ.'),
                ('Neutral / Weak Support', 'Vết mòn do nước mặn đúng với cả nước mặn đầm phá lẫn biển khơi, không làm yếu giả thuyết.'),
                ('Adjacent Topic Drift', 'Tập quán đóng thuyền ở vùng khác không bác bỏ chế độ ăn của khu định cư này.'),
            ]
        ),
        q_item(
            'd5_2_q3', 3, 'Information and Ideas', 'Command of Evidence (Textual)', 'Elite (750+)',
            '<p>Cognitive psychologist Dr. Claire Osei hypothesized that taking handwritten lecture notes improves students’ conceptual comprehension compared with typing on a laptop primarily because slower handwriting forces students to synthesize and paraphrase complex ideas in their own words, rather than because laptop screens introduce distracting notifications.</p>',
            'Which finding from a controlled experiment, if true, would most directly support Dr. Claire Osei’s hypothesis?',
            [
                'Students using internet-connected laptops scored lower on conceptual exams than students using paper notebooks because laptop users frequently checked social media.',
                'Students writing by hand recorded nearly twice as many verbatim words per minute as students typing on offline laptops.',
                'Even when laptops were stripped of Wi-Fi and all notifications, students who typed verbatim transcripts scored significantly lower on conceptual questions than both handwritten note-takers and a third group instructed to type paraphrased summaries.',
                'Students who reviewed their handwritten notes twice before an exam outperformed students who never reviewed their typed notes.'
            ],
            'C',
            'Khóa giả thuyết Osei: Cơ chế cải thiện hiểu sâu là TỔNG HỢP/DIỄN GIẢI BẰNG LỜI MÌNH (paraphrasing — X1), KHÔNG PHẢI vì tránh thông báo gây xao nhãng trên laptop (NOT X2). Thí nghiệm trong C loại sạch biến nhiễu X2 (tắt Wi-Fi & thông báo) VÀ tách rõ cơ chế X1: nhóm gõ chép nguyên văn điểm kém hơn CẢ nhóm viết tay LẪN nhóm gõ tóm tắt diễn giải → chứng minh 100% yếu tố quyết định là hành vi tóm tắt/paraphrase! Chọn C!',
            'Bằng chứng 800-level luôn cô lập biến nhiễu (tắt Wi-Fi) và kiểm chứng trực tiếp cơ chế thật (typed paraphrased summaries cũng đạt điểm cao)!',
            [
                ('Opposite Mechanism (Weakens!)', 'Chứng minh do mạng xã hội gây xao nhãng — ủng hộ cơ chế X2 mà Osei đang bác bỏ!'),
                ('Implausible / Contradicts Premise', 'Chép nguyên văn nhiều hơn đi ngược tiền đề "slower handwriting forces synthesis".'),
                ('Đáp án đúng', 'Tắt sạch biến nhiễu Wi-Fi/thông báo và chứng minh việc tóm tắt diễn giải (dù viết tay hay gõ máy) mới là nhân tố quyết định hiểu sâu.'),
                ('Confounding Variable Trap', 'Khác biệt nằm ở việc ôn bài 2 lần vs. không ôn, không kiểm chứng được cơ chế ghi chép.'),
            ]
        ),
        q_item(
            'd5_2_q4', 4, 'Information and Ideas', 'Command of Evidence (Textual)', 'Hard',
            '<p>Marine biologist Dr. Javier Morales noticed that Caribbean cleaner wrasse fish routinely remove external parasites from large predatory groupers without being eaten. Morales hypothesized that groupers refrain from eating cleaner wrasses solely because they recognize the wrasses’ distinctive bright-blue lateral stripe as a visual "do-not-eat" badge.</p>',
            'Which finding, if true, would most directly weaken Dr. Javier Morales’s hypothesis?',
            [
                'When cleaner wrasses have their blue lateral stripes painted black in laboratory tanks, groupers immediately eat them rather than allowing cleaning.',
                'Cleaner wrasses spend more hours grooming groupers near shallow coral heads than near deep sandy slopes.',
                'Juvenile cleaner wrasses develop their bright-blue lateral stripe before reaching full adult length.',
                'Groupers continue to allow cleaner wrasses to groom their gills without attacking even in pitch-dark experimental tanks where visual stripe coloration is completely invisible, provided the wrasses perform their signature rhythmic tactile fin-touch.'
            ],
            'D',
            'Khóa giả thuyết Morales: Cá mú không ăn cá dọn vệ sinh CHỈ VÌ ("solely because") nhận diện sọc xanh bằng thị giác (X). Đòn WEAKEN hoàn hảo: Trong bể TỐI ĐEN KHÔNG THỂ NHÌN THẤY SỌC XANH (bỏ X), cá mú VẪN không ăn cá dọn vệ sinh (vẫn có Y) miễn cá chạm vây theo nhịp (biến Z: tín hiệu xúc giác)! Chọn D!',
            'Thấy chữ "solely because X" trong giả thuyết → chỉ cần chứng minh Y VẪN XẢY RA khi hoàn toàn vắng mặt X là hạ gục 100%!',
            [
                ('Opposite Direction (Supports!)', 'Nếu che sọc xanh khiến cá mú ăn thịt ngay → đây là bằng chứng ỦNG HỘ mạnh giả thuyết thị giác, ngược với yêu cầu WEAKEN!'),
                ('Adjacent Topic Drift', 'Vị trí rạn nông hay sâu không kiểm chứng cơ chế nhận diện sọc xanh.'),
                ('Adjacent Topic Drift', 'Thời điểm mọc sọc xanh ở cá non không làm yếu giả thuyết về phản ứng của cá mú.'),
                ('Đáp án đúng', 'Trong bóng tối tuyệt đối (bỏ hoàn toàn yếu tố thị giác X), hành vi không ăn vẫn xảy ra nhờ tín hiệu chạm vây (Alternative Cause Z) — đánh thẳng vào chữ "solely".'),
            ]
        ),
        q_item(
            'd5_2_q5', 5, 'Information and Ideas', 'Command of Evidence (Textual)', 'Elite (750+)',
            '<p>Economist Dr. Priya Kapoor studied municipal bike-share programs in twelve mid-sized cities and hypothesized that offering discounted annual memberships to low-income households fails to boost usage among those residents unless docking stations are also expanded into lower-income outer neighborhoods rather than concentrated solely in downtown business districts.</p>',
            'Which finding, if true, would most directly support Dr. Priya Kapoor’s hypothesis?',
            [
                'In three cities that cut annual pass prices by 80% for low-income residents without adding outer-neighborhood docks, low-income ridership rose by less than 2%, whereas two comparable cities that paired the exact same discount with forty new outer-neighborhood docks saw low-income ridership jump by 290%.',
                'Downtown business commuters accounted for more than seventy percent of total weekday bike-share trips across all twelve surveyed cities.',
                'Cities that replaced traditional pedal bikes with electric-assist bicycles experienced higher maintenance expenses during winter months.',
                'Low-income residents who already owned private bicycles rarely purchased municipal bike-share memberships regardless of dock location.'
            ],
            'A',
            'Khóa giả thuyết Kapoor: Giảm giá thẻ (X1) THẤT BẠI nếu không đi kèm mở rộng trạm xe ở khu ngoại ô thu nhập thấp (X2); chỉ khi có CẢ X1 + X2 thì lượng đi mới tăng mạnh! Đáp án A đưa ra so sánh đối chứng hoàn hảo: 3 thành phố chỉ có X1 (tăng <2%) vs. 2 thành phố tương đồng có cả X1 + X2 (tăng 290%) → Chọn A!',
            'Với giả thuyết điều kiện ("X fails unless paired with Y"), tìm đối chứng trực tiếp: `[Chỉ có X → thất bại]` vs. `[Có cả X + Y → bùng nổ]`!',
            [
                ('Đáp án đúng', 'Đối chứng chuẩn xác giữa nhóm chỉ giảm giá (<2%) và nhóm giảm giá + mở rộng trạm ngoại ô (+290%).'),
                ('Missing Control / Irrelevant', 'Tỉ lệ người đi làm trung tâm cao không kiểm chứng tác động của việc giảm giá hay mở trạm ngoại ô.'),
                ('Adjacent Topic Drift', 'Chi phí bảo trì xe đạp điện mùa đông nằm ngoài giả thuyết.'),
                ('Narrow / Irrelevant', 'Người đã có sẵn xe đạp riêng không đại diện cho tác động của vị trí trạm xe lên nhóm thu nhập thấp nói chung.'),
            ]
        ),
        q_item(
            'd5_2_q6', 6, 'Information and Ideas', 'Command of Evidence (Textual)', 'Hard',
            '<p>Agronomist Dr. Samuel Boateng observed that smallholder farms intercropping maize with pigeon-pea shrubs consistently maintained stable maize yields during moderate droughts, whereas adjacent monoculture maize plots withered. Boateng hypothesized that pigeon-pea shrubs protect neighboring maize primarily by tapping deep groundwater with their two-meter taproots and releasing a portion of that moisture into upper soil layers at night—a process called hydraulic lift.</p>',
            'Which finding, if true, would most directly support Dr. Samuel Boateng’s hypothesis?',
            [
                'Pigeon-pea pods provide farming families with an important dietary source of protein during dry seasons.',
                'Isotopic water-tracing experiments show that water molecules tagged exclusively at a depth of two meters beneath intercropped plots appear inside shallow maize roots by dawn, accompanied by significantly higher overnight upper-soil moisture around pigeon-pea shrubs than in monoculture plots.',
                'Pigeon-pea shrubs fix atmospheric nitrogen in root nodules, gradually enriching soil fertility over multiple rainy seasons.',
                'Intercropped maize plots shaded by artificial plastic canopies retain lower daytime leaf temperatures than unshaded monoculture plots.'
            ],
            'B',
            'Khóa giả thuyết Boateng: Cơ chế cụ thể là HYDRAULIC LIFT — rễ cọc sâu 2m của cây đậu chiều hút nước ngầm sâu rồi nhả ra tầng đất nông ban đêm cho rễ ngô! Đáp án B dùng đồng vị đánh dấu nước ở độ sâu 2m và phát hiện đúng các phân tử nước đó xuất hiện trong rễ ngô tầng nông lúc rạng sáng → Bằng chứng trực diện 100% cho hydraulic lift! (Chú ý C là cơ chế cố định đạm — một lợi ích khác của cây họ đậu nhưng KHÔNG chứng minh cơ chế hydraulic lift!).',
            'Cảnh giác bẫy Alternative Mechanism (C: cố định đạm là sự thật sinh học có thật, nhưng không kiểm chứng cơ chế cụ thể "hydraulic lift" mà giả thuyết nêu!).',
            [
                ('Adjacent Topic Drift', 'Giá trị dinh dưỡng protein của hạt đậu không liên quan đến cơ chế giữ ẩm đất.'),
                ('Đáp án đúng', 'Đánh dấu đồng vị chứng minh trực tiếp nước từ tầng sâu 2m được bơm lên tầng nông vào ban đêm và đi vào rễ ngô.'),
                ('Alternative Mechanism Trap', 'Cố định đạm là cơ chế khác, không chứng minh giả thuyết "hydraulic lift" vận chuyển nước tầng sâu.'),
                ('Alternative Mechanism (Weakens!)', 'Nếu bóng râm nhựa nhân tạo cũng bảo vệ ngô thì lại gợi ý cơ chế che nắng chứ không chứng minh hydraulic lift.'),
            ]
        ),
        q_item(
            'd5_2_q7', 7, 'Information and Ideas', 'Command of Evidence (Textual)', 'Elite (750+)',
            '<p>Geologist Dr. Astrid Lindqvist proposed that ancient Viking ironworkers in Iceland achieved unusually durable axe blades not by importing high-carbon Swedish steel, as traditionally believed, but by smelting local bog-iron ore with birch charcoal in high-draft clay furnaces capable of infusing carbon directly during smelting.</p>',
            'Which finding, if true, would most directly support Dr. Astrid Lindqvist’s proposal?',
            [
                'Written medieval Icelandic sagas frequently praise the craftsmanship of weapons acquired through trade voyages to Scandinavia.',
                'Experimental reconstructions show that birch trees were far more scarce in fourteenth-century Iceland than in tenth-century Iceland.',
                'Metallurgical analysis of Viking-era axe blades excavated in Iceland reveals microscopic slag inclusions matching the unique trace-element fingerprint of local Icelandic bog iron alongside carbon-distribution patterns characteristic of direct charcoal smelting rather than Swedish forge welding.',
                'Several Swedish iron mines operated continuously from the ninth through the twelfth centuries, exporting ingots across the Baltic Sea.'
            ],
            'C',
            'Khóa giả thuyết Lindqvist: Lưỡi rìu bền làm từ QUẶNG SẮT ĐẦM LẦY ĐỊA PHƯƠNG ICELAND + luyện trực tiếp bằng than củi để nạp carbon, KHÔNG phải nhập thép Thụy Điển. Đáp án C chứng minh trực tiếp bằng dấu vân tay nguyên tố vi lượng của tạp chất xỉ khớp 100% quặng đầm lầy Iceland VÀ cấu trúc phân bố carbon đặc trưng của luyện trực tiếp bằng than củi → Chọn C!',
            'Tìm bằng chứng hóa lý/luyện kim kiểm tra đúng nguồn gốc vật liệu (Icelandic bog iron) + quy trình chế tạo (direct charcoal smelting)!',
            [
                ('Opposite Direction (Weakens!)', 'Truyện cổ ca ngợi vũ khí nhập từ Scandinavia lại nghiêng về giả thuyết cũ (nhập khẩu).'),
                ('Weakening / Irrelevant', 'Cây bạch dương khan hiếm hơn ở thế kỷ 14 không chứng minh kỹ thuật luyện quặng địa phương.'),
                ('Đáp án đúng', 'Khẳng định đồng thời nguồn quặng địa phương Iceland và dấu vết luyện carbon trực tiếp chứ không phải rèn thép Thụy Điển.'),
                ('Opposite Direction', 'Thông tin mỏ sắt Thụy Điển xuất khẩu chỉ làm nền cho giả thuyết truyền thống.'),
            ]
        ),
        q_item(
            'd5_2_q8', 8, 'Information and Ideas', 'Command of Evidence (Textual)', 'Elite (750+)',
            '<p>Behavioral neuroscientist Dr. Owen Takahashi investigated why urban song sparrows sing at significantly higher minimum pitches than rural sparrows of the same species. Takahashi hypothesized that this upward pitch shift is a fixed genetic adaptation evolved over generations in noisy cities rather than a short-term behavioral adjustment that individual birds turn on and off in response to immediate traffic sound.</p>',
            'Which finding, if true, would most directly weaken Dr. Owen Takahashi’s hypothesis?',
            [
                'Urban song sparrows captured in downtown parks have slightly longer average beaks than rural sparrows captured in nearby meadows.',
                'During the spring of 2020, when pandemic lockdowns abruptly reduced San Francisco traffic noise to rural levels, individual adult urban sparrows within days dropped their minimum song pitch back down to match rural norms—and raised it again immediately once traffic resumed.',
                'Low-frequency engine rumble in metropolitan centers masks the lower notes of traditional rural sparrow songs.',
                'Young sparrows raised in quiet aviaries learn their melodies primarily by imitating adult tutors during their first three months of life.'
            ],
            'B',
            'Khóa giả thuyết Takahashi: Hát tông cao hơn là THÍCH NGHI DI TRUYỀN CỐ ĐỊNH qua nhiều thế hệ (fixed genetic adaptation), KHÔNG phải điều chỉnh hành vi ngắn hạn bật/tắt theo tiếng xe (NOT short-term behavioral adjustment). Đòn WEAKEN tuyệt đối: Khi phong tỏa 2020 làm tiếng xe giảm đột ngột, chính những con chim trưởng thành đô thị lập tức HẠ tông xuống mức nông thôn trong vài ngày rồi lại TĂNG lên ngay khi xe đông lại! Điều này chứng minh đó là điều chỉnh hành vi tức thời chứ KHÔNG cố định di truyền! Chọn B!',
            'Thí nghiệm tự nhiên (Natural Experiment: tắt tiếng xe → chim lập tức hạ tông, bật tiếng xe → chim lập tức nâng tông) là bằng chứng mạnh nhất bác bỏ tính "fixed genetic"!',
            [
                ('Adjacent Topic Drift', 'Chiều dài mỏ không trực tiếp chứng minh hay bác bỏ việc chỉnh cao độ theo tiếng ồn.'),
                ('Đáp án đúng', 'Chim trưởng thành bật/tắt cao độ trong vài ngày theo tiếng xe chứng minh đó là điều chỉnh hành vi ngắn hạn, bác bỏ thẳng giả thuyết di truyền cố định.'),
                ('Background Context Only', 'Giải thích lý do tiếng ồn che lấp nốt trầm đúng cho cả hai giả thuyết (di truyền lẫn hành vi), không làm yếu giả thuyết nào.'),
                ('Adjacent Topic Drift', 'Cách chim non học hót trong lồng yên tĩnh không bác bỏ giả thuyết thích nghi di truyền ở chim đô thị.'),
            ]
        ),
        q_item(
            'd5_2_q9', 9, 'Information and Ideas', 'Command of Evidence (Textual)', 'Hard',
            '<p>Paleoclimatologist Dr. Sofia Delgado noticed thick bands of Saharan quartz dust embedded in seafloor sediments off the coast of Barbados dating to 3,200 years ago. Delgado hypothesized that an abrupt multi-decade drought across West Africa—rather than localized changes in Caribbean hurricane tracks—caused the sudden spike in transatlantic dust deposition.</p>',
            'Which finding, if true, would most directly support Dr. Sofia Delgado’s hypothesis?',
            [
                'Independent lake-level cores from Ghana and Senegal dating to 3,200 years ago show severe basin desiccation and pollen shifts from rainforest to dry savanna at the exact same time, while sediment cores from both West Africa’s shelf and the western Atlantic record matching dust spikes.',
                'Modern Caribbean hurricanes occasionally transport small quantities of Saharan dust northward toward Florida.',
                'Barbados seafloor sediments from 1,000 years ago contain higher concentrations of marine microfossils than layers from 3,200 years ago.',
                'Computer simulations indicate that shifting hurricane paths can alter rainfall totals on small Caribbean islands.'
            ],
            'A',
            'Khóa giả thuyết Delgado: Đợt tăng bụi 3.200 năm trước là do HẠN HÁN LỚN Ở TÂY PHI (X1), chứ không phải thay đổi cục bộ đường đi bão Caribe (NOT X2). Đáp án A cung cấp 2 bằng chứng độc lập: hồ nước ở Ghana & Senegal cạn kiệt biến thành xavan khô đúng mốc 3.200 năm trước + cả thềm lục địa Tây Phi lẫn Tây Đại Tây Dương đều tăng bụi đồng bộ → chứng minh nguồn gốc hạn hán Tây Phi quy mô vùng! Chọn A!',
            'Tìm bằng chứng địa lý độc lập ngay tại nguồn gốc giả định (Ghana/Senegal desiccation) khớp chuẩn mốc 3.200 năm trước!',
            [
                ('Đáp án đúng', 'Xác thực đồng bộ hạn hán khắc nghiệt tại Tây Phi (Ghana, Senegal) đúng mốc 3.200 năm và sự gia tăng bụi trên cả hai bờ Đại Tây Dương.'),
                ('Adjacent Topic Drift', 'Bão hiện đại thỉnh thoảng mang bụi tới Florida không chứng minh nguyên nhân đợt tăng bụi 3.200 năm trước.'),
                ('Irrelevant Time Period', 'Mốc 1.000 năm trước và vi hóa thạch biển không liên quan đợt hạn hán 3.200 năm trước.'),
                ('Alternative Mechanism Context', 'Chỉ nêu khả năng bão đổi lượng mưa, không ủng hộ giả thuyết hạn hán Tây Phi.'),
            ]
        ),
        q_item(
            'd5_2_q10', 10, 'Information and Ideas', 'Command of Evidence (Textual)', 'Elite (750+)',
            '<p>Art conservator Dr. Matteo Conti suspected that a small unsigned oil sketch in a Milan private collection was painted by eighteenth-century Venetian master Giovanni Battista Tiepolo as a preparatory study for his famous ceiling fresco in Würzburg, rather than by a nineteenth-century imitator copying the finished ceiling.</p>',
            'Which finding, if true, would most directly support Dr. Matteo Conti’s suspicion?',
            [
                'The oil sketch depicts the exact same arrangement of allegorical figures and architectural columns that appears in the completed Würzburg ceiling fresco.',
                'Infrared reflectography of the Milan sketch reveals bold underdrawing changes—such as a figure’s arm shifted twice and a column eliminated—that match preliminary sketches in Tiepolo’s workshop, while pigment analysis detects no synthetic colors invented after 1760.',
                'Several nineteenth-century German painters traveled to Würzburg to study Tiepolo’s fresco techniques firsthand.',
                'The gilded wooden frame surrounding the Milan oil sketch was crafted in Milan during the 1840s.'
            ],
            'B',
            'Khóa giả thuyết Conti: Tranh là BẢN PHÁC THẢO CHUẨN BỊ CỦA CHÍNH TIEPOLO (preparatory study), KHÔNG phải bản chép lại của họa sĩ thế kỷ 19 (copyist)! Chú ý bẫy A: một người chép tranh thế kỷ 19 cũng sẽ vẽ Y HỆT bố cục trần nhà hoàn chỉnh — thậm chí càng giống y hệt càng dễ là bản chép! Ngược lại, trong B: ảnh hồng ngoại lộ ra các nét phác SỬA ĐỔI SÁNG TÁC NGAY TRÊN TRANH (pentimenti — đặc trưng bản sáng tác gốc chứ người chép không sửa bố cục!) + phân tích màu KHÔNG có sắc tố tổng hợp sau 1760 → chứng minh sắc lẹm! Chọn B!',
            'Tư duy kiểm chứng nghệ thuật 800-level: Bản phác thảo gốc chứa nét sửa sáng tác (underdrawing revisions) + màu đúng niên đại; còn sự "giống y hệt bản hoàn chỉnh" (A) KHÔNG phân biệt được bản gốc với bản chép!',
            [
                ('Fails to Distinguish Copy vs. Original', 'Bản sao chép thế kỷ 19 cũng sẽ vẽ giống y hệt bố cục bức bích họa đã hoàn thành — không chứng minh đây là bản phác thảo gốc.'),
                ('Đáp án đúng', 'Nét phác sửa đổi bố cục dưới lớp sơn (đặc trưng bản sáng tác thử) kết hợp vắng mặt màu tổng hợp sau 1760 củng cố trực tiếp giả thuyết của Conti.'),
                ('Weakening Context', 'Việc họa sĩ thế kỷ 19 tới học kỹ thuật Tiepolo chỉ càng làm tăng khả năng có bản sao chép.'),
                ('Irrelevant Object (Frame)', 'Khung tranh đóng năm 1840 có thể dễ dàng thay khung mới cho một bức tranh cổ hơn nhiều.'),
            ]
        ),
        q_item(
            'd5_2_q11', 11, 'Information and Ideas', 'Command of Evidence (Textual)', 'Hard',
            '<p>Sleep researcher Dr. Nadia Al-Mansoor hypothesized that afternoon memory consolidation depends not merely on total nap duration, but specifically on whether a nap includes slow-wave deep sleep—which typically begins only after twenty minutes of resting—rather than light stage-1 dozing alone.</p>',
            'Which finding from a sleep-lab study, if true, would most directly support Dr. Nadia Al-Mansoor’s hypothesis?',
            [
                'Participants who drank caffeine immediately before a forty-five-minute nap fell asleep more slowly than participants who drank decaffeinated tea.',
                'Participants who slept for eight full hours at night scored higher on morning vocabulary recall than sleep-deprived participants.',
                'Among participants who all napped for exactly thirty-five minutes, those whose EEG scans confirmed slow-wave deep sleep improved on post-nap word-pair recall by 26%, whereas those who remained strictly in light stage-1 and stage-2 sleep showed virtually no improvement over awake controls.',
                'Participants who napped for fifteen minutes reported feeling more alert and less fatigued than participants who stayed awake.'
            ],
            'C',
            'Khóa giả thuyết Al-Mansoor: Củng cố trí nhớ phụ thuộc cụ thể vào GIẤC NGỦ SÂU SÓNG CHẬM (slow-wave deep sleep), không chỉ tổng thời lượng ngủ (total nap duration). Để kiểm chứng sạch biến thời lượng, giữ cố định tổng thời lượng ngủ như nhau (cùng 35 phút!) rồi so nhóm CÓ slow-wave (+26%) vs. nhóm CHỈ ngủ nông (gần như 0%) → C là thí nghiệm chuẩn mực 100%!',
            'Khi giả thuyết tách biến chất lượng (slow-wave) khỏi biến số lượng (duration), bằng chứng mạnh nhất luôn GIỮ CỐ ĐỊNH thời lượng để so sánh hai nhóm!',
            [
                ('Adjacent Topic Drift', 'Tác động của caffeine đến tốc độ vào giấc không kiểm chứng vai trò của slow-wave sleep với trí nhớ.'),
                ('Irrelevant Condition', 'Ngủ đêm 8 tiếng so với thiếu ngủ không kiểm tra giả thuyết về giấc ngủ trưa ngắn.'),
                ('Đáp án đúng', 'Cố định tổng thời gian 35 phút và cho thấy chỉ nhóm có slow-wave deep sleep mới tăng 26% khả năng ghi nhớ.'),
                ('Wrong Variable (Alertness ≠ Memory)', 'Cảm giác tỉnh táo sau 15 phút ngủ nông không kiểm chứng củng cố trí nhớ.'),
            ]
        ),
        q_item(
            'd5_2_q12', 12, 'Information and Ideas', 'Command of Evidence (Textual)', 'Elite (750+)',
            '<p>Hydrologist Dr. Lukas Weber observed that beaver reintroduction along degraded Oregon streams led to a dramatic rebound in juvenile salmon survival during hot summers. Weber hypothesized that beaver dams aid young salmon primarily by creating deep, shaded cool-water pools fed by chilled groundwater seepage, rather than by blocking predatory birds from reaching the streams.</p>',
            'Which finding, if true, would most directly weaken Dr. Lukas Weber’s hypothesis?',
            [
                'Water temperatures inside Oregon beaver ponds drop by an average of 2.8°C below temperatures measured in adjacent undammed shallow riffles.',
                'Stream reaches containing beaver dams support higher densities of aquatic insects eaten by juvenile salmon than undammed reaches.',
                'Predatory herons frequently perch on fallen willow logs located near newly built beaver dams.',
                'Detailed thermal logging across thirty Oregon beaver ponds shows that pond water actually warms 1.5°C higher than undammed stream reaches during July heat waves, yet juvenile salmon survival still doubles in the ponds because tangled woody debris shelters the fish from kingfishers and herons.'
            ],
            'D',
            'Khóa giả thuyết Weber: Đập hải ly cứu cá hồi chủ yếu nhờ TẠO HỒ NƯỚC MÁT (X1), KHÔNG phải vì cản chim săn mồi (NOT X2). Đòn WEAKEN hạ gục hoàn toàn: Đo nhiệt độ 30 hồ hải ly thấy nước THỰC RA ẤM HƠN 1.5°C (không có X1!), nhưng cá hồi vẫn sống gấp đôi nhờ cành cây rối che chắn khỏi chim bói cá & diệc (đúng cơ chế X2 mà Weber bác bỏ)! Chọn D!',
            'Đòn Weaken đỉnh cao: Chứng minh cơ chế giả thuyết X1 đi ngược chiều (ấm hơn thay vì mát hơn) + cơ chế bị loại trừ X2 mới là nguyên nhân thực!',
            [
                ('Opposite Direction (Supports!)', 'Hồ mát hơn 2.8°C là bằng chứng ỦNG HỘ mạnh giả thuyết nước mát của Weber.'),
                ('Mild Alternative / Doesn’t Refute Thermal Claim', 'Thêm côn trùng là yếu tố phụ, không trực tiếp bác bỏ cơ chế nước mát mạnh như D.'),
                ('Weak / Ambiguous', 'Diệc đậu gần đập không cho biết tỉ lệ sống của cá hồi hay nhiệt độ nước.'),
                ('Đáp án đúng', 'Bác bỏ trực tiếp cơ chế nước mát (hồ ấm hơn 1.5°C!) và chứng minh che chắn khỏi chim săn mồi mới là lý do tăng gấp đôi tỉ lệ sống.'),
            ]
        ),
        q_item(
            'd5_2_q13', 13, 'Information and Ideas', 'Command of Evidence (Textual)', 'Elite (750+)',
            '<p>Astronomers studying the dwarf planet Ceres detected bright white salt deposits gleaming inside Occator Crater. Planetary scientist Dr. Kenji Sato hypothesized that these deposits formed relatively recently—within the past few million years—as salty liquid brine welled up from a lingering subsurface reservoir beneath the crater floor, rather than being ancient four-billion-year-old surface salts merely exposed by the meteorite impact.</p>',
            'Which finding, if true, would most directly support Dr. Kenji Sato’s hypothesis?',
            [
                'Spectral readings from the Dawn spacecraft detect hydrohalite—a hydrated salt mineral that dehydrates and breaks down within a few hundred years when exposed to space vacuum—still actively present at the bright center of Occator Crater.',
                'Occator Crater measures roughly ninety-two kilometers in diameter and displays steep terraced walls typical of large asteroid impacts.',
                'Several much older craters on Ceres’s southern hemisphere lack any visible bright white deposits on their floors.',
                'Laboratory tests confirm that anhydrous sodium carbonate can survive unchanged on an airless planetary surface for billions of years.'
            ],
            'A',
            'Khóa giả thuyết Sato: Muối mới hình thành GẦN ĐÂY từ nước muối lỏng trào lên từ hồ ngầm, KHÔNG phải muối cổ 4 tỉ năm. Bằng chứng A là tuyệt phẩm khoa học hành tinh: phát hiện khoáng vật **hydrohalite** — loại muối ngậm nước sẽ tự phân hủy chỉ sau vài trăm năm ngoài chân không — VẪN ĐANG TỒN TẠI ở tâm hố thiên thạch! Điều đó chứng minh 100% nước muối lỏng mới trào lên cực kỳ gần đây! Chọn A!',
            'Chú ý chi tiết "đồng hồ sinh/hóa học" trong khoa học: phát hiện một chất phân hủy nhanh trong vài trăm năm vẫn còn nguyên vẹn = bằng chứng bất khả chối cãi về hoạt động địa chất gần đây!',
            [
                ('Đáp án đúng', 'Sự tồn tại của hydrohalite (vốn phân hủy sau vài trăm năm ngoài chân không) chứng minh chắc chắn muối mới trào lên rất gần đây từ nguồn lỏng ngầm.'),
                ('Adjacent Topic Drift', 'Đường kính và vách hố thiên thạch không phân biệt được tuổi của lớp muối.'),
                ('Weak / Ambiguous', 'Các hố cũ không có muối có thể do nhiều nguyên nhân, không chứng minh trực tiếp nguồn nước ngầm mới trào lên ở Occator.'),
                ('Opposite Direction (Weakens!)', 'Muối khan tồn tại được hàng tỉ năm chỉ hỗ trợ khả năng muối cổ xưa bị lộ ra, không ủng hộ giả thuyết nước muối mới trào lên.'),
            ]
        ),
    ]
    return {
        'schemaVersion': 1,
        'mode': 'drill',
        'section': 'Reading and Writing',
        'basicInfo': {
            'title': 'Drill 5.2: Command of Evidence — Scientific Claims (13 Qs)',
            'subtitle': 'Thực chiến cửa ải Support / Weaken giả thuyết khoa học Hard Module 2 với cơ chế kiểm soát biến nhiễu và nhóm đối chứng.',
            'difficultyBadge': 'I&I • Target 1500+',
            'targetTimeMinutes': 16,
        },
        'drillModule': {
            'id': 'drill_5_2_mod',
            'title': 'Skill Drill 5.2: Command of Evidence (Scientific Claims)',
            'timeLimitMinutes': 16,
            'questions': questions,
        },
    }


def get_drill_5_3():
    questions = [
        q_item(
            'd5_3_q1', 1, 'Information and Ideas', 'Command of Evidence (Textual)', 'Hard',
            '<p>In an essay on the 1908 novel <i>The Glass Conservatory</i>, a critic argues that the narrator feels simultaneously drawn to the fragile beauty of the estate’s greenhouse and unsettled by how artificially isolated it is from the harsh winter world outside.</p>',
            'Which quotation from <i>The Glass Conservatory</i> most effectively illustrates the critic’s claim?',
            [
                '“Beneath the steamed panes, orchids blazed in impossible violet splendor, yet the warm, perfumed stillness felt almost suffocating whenever I pressed my palm against the glass and felt January’s iron frost biting just a millimeter away.”',
                '“Every Tuesday morning the head gardener scrubbed the iron framing with linseed soap so that not a trace of moss dimmed the winter light.”',
                '“Standing inside the arched doorway, I marveled that any architect could bend so many delicate sheets of glass without shattering a single pane.”',
                '“Beyond the stone wall, the January gale stripped the last dry leaves from the elm trees and piled drifts across the carriage road.”'
            ],
            'A',
            'Checklist 2 vế bắt buộc từ Claim: [1] Bị cuốn hút bởi vẻ đẹp mong manh của nhà kính ("drawn to fragile beauty") + [2] Bất an trước sự cách ly nhân tạo với mùa đông khắc nghiệt bên ngoài ("unsettled by artificial isolation from harsh winter"). C chỉ có [1]; D chỉ tả mùa đông; B tả công việc làm vườn. Duy nhất A hội tụ đủ cả 2 vế: "orchids blazed in impossible violet splendor" [1] + "yet the warm, perfumed stillness felt almost suffocating... January’s iron frost a millimeter away" [2]!',
            'Tách ngay 2 ô vuông từ chữ "simultaneously ... and ...": loại mọi trích dẫn chỉ thỏa 1 nửa!',
            [
                ('Đáp án đúng', 'Khớp trọn cả hai vế đối nghịch: vẻ đẹp rực rỡ mê hoặc của hoa lan + cảm giác ngột ngạt bất an khi sờ thấy sương giá cách chỉ 1 milimét.'),
                ('Topic Keyword Lure', 'Chỉ mô tả công việc vệ sinh nhà kính, không có sự cuốn hút lẫn cảm giác bất an.'),
                ('Half-Match Trap', 'Chỉ thể hiện sự ngưỡng mộ kỹ thuật kiến trúc, thiếu hẳn sự bất an về sự cô lập với mùa đông.'),
                ('Half-Match Trap', 'Chỉ miêu tả gió đông bên ngoài, không nhắc vẻ đẹp hay cảm giác bên trong nhà kính.'),
            ]
        ),
        q_item(
            'd5_3_q2', 2, 'Information and Ideas', 'Command of Evidence (Textual)', 'Hard',
            '<p>A student studying nineteenth-century abolitionist speeches claims that orator Frederick Douglass frequently exposed the hypocrisy of patriotic celebrations by contrasting America’s lofty ideals of liberty with the ongoing reality of enslavement.</p>',
            'Which quotation from an 1852 speech by Frederick Douglass most effectively illustrates the student’s claim?',
            [
                '“The papers and placards say that I am to deliver a Fourth of July oration, and I rise today with grateful respect for the citizens gathered in this hall.”',
                '“Your high independence only reveals the immeasurable distance between us: the sunlight that brought life and healing to you has brought stripes and death to me.”',
                '“Across the Atlantic, European nations have watched the rapid commercial rise of American ports with a mixture of envy and astonishment.”',
                '“It is essential that every young citizen study the constitutional debates of 1787 with patience and scholarly discipline.”'
            ],
            'B',
            'Checklist từ Claim: [1] Phơi bày sự đạo đức giả của lễ kỷ niệm yêu nước (Fourth of July / high independence) + [2] Đối chiếu lý tưởng tự do cao đẹp với thực tại nô lệ tàn khốc. Trích dẫn B tạo tương phản kinh điển: "high independence / sunlight that brought life and healing to you" ↔ "stripes and death to me" → Chọn B!',
            'Tìm đúng phép đối chiếu (contrast) ngay bên trong câu trích dẫn!',
            [
                ('Topic Keyword Lure', 'Có nhắc cụm "Fourth of July" nhưng chỉ là câu mở lời lịch sự, chưa hề đối chiếu hay phê phán sự đạo đức giả.'),
                ('Đáp án đúng', 'Đối chiếu sắc lẹm giữa tự do rực rỡ của ngày lễ độc lập với đòn roi và cái chết của thân phận nô lệ.'),
                ('Out of Scope', 'Chỉ nói về thương mại cảng biển Mỹ dưới góc nhìn châu Âu.'),
                ('Topic Keyword Lure', 'Chỉ khuyên học lịch sử Hiến pháp, không nhắc thực tại nô lệ.'),
            ]
        ),
        q_item(
            'd5_3_q3', 3, 'Information and Ideas', 'Command of Evidence (Textual)', 'Elite (750+)',
            '<p>In a literary study of the 1924 short story “The Cartographer’s Daughter,” a researcher claims that the protagonist, Lin, views her father’s obsession with mapping exact borders as futile because natural landscapes constantly erase human boundaries.</p>',
            'Which quotation from “The Cartographer’s Daughter” most effectively illustrates the researcher’s claim?',
            [
                '“My father sharpened three drafting pencils every dawn, insisting that a surveyor’s ink line must never tremble by even half a millimeter.”',
                '“Before the spring thaw reached the valley, villagers relied on my father’s folded parchment maps to locate the safest timber bridges.”',
                '“He spent forty years ruling crimson county lines across the delta, yet each monsoon carved fresh channels through the mud as effortlessly as if his finest atlases were drawn on water.”',
                '“I inherited his brass dividers and compass box, though I preferred sketching migrating herons in the margins of his old ledger.”'
            ],
            'C',
            'Checklist 3 vế: [1] Nỗi ám ảnh vẽ ranh giới chính xác của người cha + [2] Tính vô ích (futile) + [3] Thiên nhiên liên tục xóa nhòa ranh giới con người. A chỉ có [1]; B nói bản đồ hữu ích (ngược nghĩa "futile"!); D chỉ nói sở thích vẽ chim của con gái. Duy nhất C chốt trọn cả 3: 40 năm kẻ đường biên đỏ thẫm ↔ mỗi mùa mưa lũ lại xẻ dòng mới khiến tập bản đồ chẳng khác nào "vẽ trên mặt nước"! Chọn C!',
            'Hình ảnh ẩn dụ "as if his finest atlases were drawn on water" dịch thẳng sang ý "futile" (vô ích trước sức mạnh thiên nhiên)!',
            [
                ('Half-Match Trap', 'Chỉ thể hiện sự tỉ mỉ ám ảnh của người cha [1], thiếu hẳn yếu tố thiên nhiên xóa bỏ hay sự vô ích [2][3].'),
                ('Contradiction', 'Khẳng định bản đồ hữu ích với dân làng — trái ngược với nhận định "futile".'),
                ('Đáp án đúng', 'Khớp cả 3 vế: nỗi ám ảnh 40 năm kẻ biên giới + thiên nhiên mùa lũ xẻ dòng mới + ẩn dụ "vẽ trên nước" (vô ích).'),
                ('Topic Keyword Lure', 'Chỉ nhắc dụng cụ vẽ bản đồ và sở thích riêng của Lin.'),
            ]
        ),
        q_item(
            'd5_3_q4', 4, 'Information and Ideas', 'Command of Evidence (Textual)', 'Elite (750+)',
            '<p>A poetry scholar claims that in the 1895 lyric “The Stonecutter’s Song,” the speaker finds quiet dignity not in achieving personal fame, but in contributing anonymously to a structure that will outlast every individual builder.</p>',
            'Which quotation from “The Stonecutter’s Song” most effectively illustrates the scholar’s claim?',
            [
                '“My hammer rings from break of day till bell, / And heavy aches the wrist that guides the blade.”',
                '“No merchant passing through the market square / Stops long to weigh the price of quarried lime.”',
                '“I envy kings whose marble statues stand / Unbroken where the river meets the sea.”',
                '“No passerby shall read my vanished name, / Yet high above the rain my keystone holds / The vaulted arch for centuries to come.”'
            ],
            'D',
            'Checklist 3 vế: [1] Không cầu danh tiếng cá nhân / vô danh ("anonymously") + [2] Đóng góp cho công trình trường tồn qua thời gian ("outlast every builder") + [3] Niềm tự hào/phẩm giá thầm lặng ("quiet dignity"). A chỉ than mỏi cổ tay; B bàn giá vôi đá; C ghen tị với tượng vua (ngược hoàn toàn "not in personal fame"!). Duy nhất D trọn vẹn: "No passerby shall read my vanished name" [1] + "Yet high above the rain my keystone holds the vaulted arch for centuries to come" [2][3]!',
            'Trong thơ, từ khóa "No passerby shall read my vanished name, Yet..." tương ứng 100% với "anonymously" + "quiet dignity"!',
            [
                ('Topic Keyword Lure', 'Chỉ mô tả sự vất vả thể xác của nghề đục đá.'),
                ('Irrelevant Detail', 'Nói về thương nhân không quan tâm giá đá vôi.'),
                ('Contradiction', 'Nói người thợ ghen tị với danh vọng tượng đá của nhà vua — trái ngược hẳn với nhận định của học giả.'),
                ('Đáp án đúng', 'Thể hiện trọn vẹn sự vô danh ("vanished name") đi liền niềm tự hào thầm lặng khi viên đá khóa vòm giữ công trình bền vững nhiều thế kỷ.'),
            ]
        ),
        q_item(
            'd5_3_q5', 5, 'Information and Ideas', 'Command of Evidence (Textual)', 'Hard',
            '<p>In an analysis of the 1931 novel <i>Copper Harbor</i>, a student asserts that the town’s longtime residents react to the arrival of wealthy summer tourists with polite outward hospitality that conceals quiet resentment.</p>',
            'Which quotation from <i>Copper Harbor</i> most effectively illustrates the student’s assertion?',
            [
                '“Mrs. Gallagher beamed as she handed the visitors fresh blackberry jam across the porch rail, keeping her smile perfectly fixed until their motorcar vanished—only then muttering that their dust had coated her wash line twice since Tuesday.”',
                '“Each July the harbor docks filled with gleaming white sailboats arriving from Chicago and Detroit, bringing brisk business to the local chandlery.”',
                '“Several fishermen openly argued with the visiting yacht owners on the pier, demanding that the outer anchorage remain reserved for working trawlers.”',
                '“After the summer visitors departed in September, the harbor settled back into its quiet autumn routine of mending nets and stacking firewood.”'
            ],
            'A',
            'Checklist 2 vế: [1] Bề ngoài hiếu khách lịch thiệp ("polite outward hospitality") + [2] Bên trong che giấu sự bực dọc âm thầm ("conceals quiet resentment"). Chú ý bẫy C: ngư dân tranh cãi CÔNG KHAI ("openly argued") → vi phạm hoàn toàn yếu tố "polite outward / conceals"! Duy nhất A thể hiện chính xác nụ cười rạng rỡ tặng mứt dâu bên ngoài, chỉ chờ xe khách đi khuất mới lầm bầm bực bội bên trong!',
            'Chú ý từng phó từ trong Claim: "conceals quiet resentment" loại ngay phương án "openly argued" (C)!',
            [
                ('Đáp án đúng', 'Minh họa hoàn hảo hai lớp thái độ: niềm nở tặng mứt tươi bên ngoài + lầm bầm khó chịu sau khi khách khuất bóng.'),
                ('Missing Resentment', 'Chỉ mô tả khách du lịch mang lại doanh thu tốt, không có sự bực dọc ngầm.'),
                ('Contradiction ("Openly" Trap)', 'Tranh cãi công khai trên bến tàu mâu thuẫn với "polite outward hospitality that conceals quiet resentment".'),
                ('Missing Both Attitudes', 'Chỉ tả nhịp sống mùa thu sau khi khách về.'),
            ]
        ),
        q_item(
            'd5_3_q6', 6, 'Information and Ideas', 'Command of Evidence (Textual)', 'Elite (750+)',
            '<p>A historian reviewing nineteenth-century scientific memoirs claims that astronomer Maria Mitchell viewed rigorous mathematical discipline not as an enemy of poetic wonder, but as a gateway that deepens one’s emotional awe of the night sky.</p>',
            'Which quotation from Maria Mitchell’s notebooks most effectively illustrates the historian’s claim?',
            [
                '“Every observer who wishes to chart a comet’s orbit must verify her logarithmic tables twice before sunrise, lest a tiny error spoil a week’s labor.”',
                '“Some imagine that measuring a star’s parallax strips the heavens of enchantment; yet the more closely I calculate those staggering distances, the more breathless I grow before the sheer majesty of the cosmos.”',
                '“Few institutions of higher learning in 1850 permitted young women to operate refracting telescopes without a male chaperone.”',
                '“When clouds obscure the meridian for three nights in succession, an astronomer must turn her attention to sorting correspondence and cleaning lenses.”'
            ],
            'B',
            'Checklist 2 vế: [1] Kỷ luật toán học chặt chẽ KHÔNG tiêu diệt sự kỳ diệu thơ mộng + [2] Ngược lại càng đào sâu sự kinh ngạc cảm xúc trước bầu trời đêm. A chỉ có toán học; C nói rào cản giới; D nói đêm nhiều mây. Duy nhất B nối thẳng: bác bỏ quan niệm đo đạc làm mất phép màu ("strips the heavens of enchantment") và khẳng định càng tính toán khoảng cách càng sững sờ trước sự hùng vĩ của vũ trụ!',
            'Tìm cấu trúc đối lập bác bỏ định kiến rồi khẳng định tác dụng bổ trợ ("Some imagine X strips Y; yet the more I do X, the more Y...")!',
            [
                ('Half-Match Trap', 'Chỉ nhấn mạnh sự chính xác toán học, thiếu hoàn toàn yếu tố cảm xúc kỳ diệu thơ mộng.'),
                ('Đáp án đúng', 'Khớp 100% hai vế: bác bỏ ý nghĩ tính toán giết chết vẻ kỳ ảo và khẳng định nó càng làm sâu sắc sự kinh ngạc trước vũ trụ.'),
                ('Out of Scope', 'Bàn về rào cản giới tính trong giáo dục đại học năm 1850.'),
                ('Irrelevant Detail', 'Nói công việc làm khi trời nhiều mây.'),
            ]
        ),
        q_item(
            'd5_3_q7', 7, 'Information and Ideas', 'Command of Evidence (Textual)', 'Hard',
            '<p>In a review of the 1919 novel <i>The Clockmaker’s Apprentice</i>, a literary scholar argues that although the apprentice, Mateo, initially resents his master’s demanding perfectionism, he eventually recognizes that those strict standards were intended to ensure Mateo’s independence as a craftsman.</p>',
            'Which quotation from <i>The Clockmaker’s Apprentice</i> most effectively illustrates the scholar’s claim?',
            [
                '“Whenever Master Alvarez rejected a brass gear for being a hair’s breadth uneven, Mateo bit his lip in silent fury and wished he had apprenticed to a baker instead.”',
                '“Master Alvarez had learned his trade in Geneva before opening a cramped repair shop near the Valencia cathedral square.”',
                '“For two years Mateo cursed the old man’s merciless eye; only on the morning he opened his own workbench and repaired a governor’s chronometer unaided did he realize Alvarez had forged his rigor so Mateo would never have to beg another master for work.”',
                '“By the end of his third winter in the shop, Mateo could assemble a pocket watch escapement twice as fast as any other youth in the guild.”'
            ],
            'C',
            'Checklist 3 vế: [1] Ban đầu oán giận sự cầu toàn khắc nghiệt + [2] Về sau nhận ra mục đích + [3] Mục đích là giúp Mateo ĐỘC LẬP nghề nghiệp ("ensure independence"). A chỉ có [1] (oán giận ban đầu); D chỉ nói tốc độ làm nhanh; B kể tiểu sử thầy. Duy nhất C gói trọn toàn bộ hành trình từ "cursed the old man’s merciless eye" → "realize Alvarez had forged his rigor so Mateo would never have to beg another master for work"!',
            'Nhận định có diễn tiến thời gian ("initially X... eventually recognizes Y") → trích dẫn đúng bắt buộc chứa CẢ hai giai đoạn thời gian!',
            [
                ('Half-Match Trap', 'Chỉ thể hiện sự bực tức ban đầu, thiếu hẳn sự nhận ra về sau và mục đích tự lập.'),
                ('Irrelevant Background', 'Chỉ nêu xuất thân nghề nghiệp của Master Alvarez.'),
                ('Đáp án đúng', 'Đủ trọn 3 chặng: ban đầu nguyền rủa sự khắt khe → khi tự mở bàn thợ mới hiểu thầy rèn mình để tự lập không phụ thuộc ai.'),
                ('Half-Match / Missing Insight', 'Chỉ nêu tốc độ thao tác, không nhắc sự oán giận ban đầu hay nhận thức về mục đích của thầy.'),
            ]
        ),
        q_item(
            'd5_3_q8', 8, 'Information and Ideas', 'Command of Evidence (Textual)', 'Elite (750+)',
            '<p>A critic examining the 1882 poem “The Orchard Wall” claims that the speaker regards an inherited boundary wall not as a necessary safeguard against neighbors, but as an outdated barrier that persists solely out of unexamined habit.</p>',
            'Which quotation from “The Orchard Wall” most effectively illustrates the critic’s claim?',
            [
                '“Before the frost heaves loose the granite base, / We stack the fallen boulders back in line.”',
                '“Tall apple boughs cast cool and dappled shade / Across the mossy grass where children play.”',
                '“My grandfather once feared stray cattle here, / And built the masonry three courses high.”',
                '“No herd has grazed these hills for forty years; / We mend the gap each spring because our fathers did, / Guarding an empty lane from nothing at all.”'
            ],
            'D',
            'Checklist 2 vế: [1] KHÔNG còn cần thiết để bảo vệ ("not a necessary safeguard") + [2] Chỉ tồn tại vì THÓI QUEN KHÔNG SUY XÉT ("unexamined habit"). A chỉ tả việc xếp đá; C giải thích lý do HỢP LÝ trong quá khứ của ông nội (không chứng minh hiện tại vô ích); B tả bóng cây táo. Duy nhất D vạch trần: 40 năm nay không còn đàn gia súc nào, chỉ sửa tường mỗi xuân "vì cha ông xưa làm thế, canh giữ con đường trống khỏi chẳng thứ gì cả"! Chọn D!',
            'Đọc sâu câu thơ cuối: "because our fathers did" = unexamined habit; "Guarding an empty lane from nothing at all" = not a necessary safeguard!',
            [
                ('Topic Keyword Lure', 'Chỉ miêu tả hành động xếp lại đá tường mà không nêu thái độ coi nó lỗi thời vô ích.'),
                ('Irrelevant Detail', 'Chỉ tả cảnh vườn táo yên bình.'),
                ('Past Context Only', 'Chỉ kể lý do hữu ích của bức tường thời ông nội, không cho thấy hiện tại nó lỗi thời.'),
                ('Đáp án đúng', 'Khớp cả hai vế: không còn gia súc 40 năm (hết cần thiết) + sửa chỉ vì cha ông từng làm (thói quen không suy xét).'),
            ]
        ),
        q_item(
            'd5_3_q9', 9, 'Information and Ideas', 'Command of Evidence (Textual)', 'Hard',
            '<p>In an essay on the 1927 novel <i>Northern Rails</i>, a student contends that stationmaster Jonas takes genuine comfort in the rigid predictability of train timetables because they provide a sense of order during an otherwise turbulent period in his personal life.</p>',
            'Which quotation from <i>Northern Rails</i> most effectively illustrates the student’s contention?',
            [
                '“While letters from his estranged brother went unanswered and debts mounted on his kitchen table, Jonas stood beside the brass clock each evening, calmed by the certainty that the 8:14 express would round the pine bend on the exact second promised.”',
                '“Whenever heavy blizzards drifted across the northern switchyard, the 8:14 express arrived up to three hours behind schedule.”',
                '“Jonas had memorized every freight stop between Duluth and Winnipeg before his twenty-fifth birthday.”',
                '“Passengers hurried off the 8:14 express with collars turned high against the sleet, barely glancing at the illuminated timetable board.”'
            ],
            'A',
            'Checklist 2 vế: [1] Tìm thấy sự an ủi thực sự ở tính đều đặn chính xác của lịch tàu ("comfort in rigid predictability") + [2] Giữa giai đoạn đời tư đầy biến động ("turbulent personal life"). B nói tàu bị trễ (ngược predictability!); C chỉ nói trí nhớ tốt; D tả hành khách. Duy nhất A ghép trọn đời tư rối ren (anh trai xa cách, nợ nần chồng chất) với cảm giác bình tâm trước chuyến tàu 8:14 đúng từng giây!',
            'Kiểm tra xem trích dẫn có đủ CẢ BỐI CẢNH (turbulent personal life) LẪN CẢM XÚC (calmed by certainty) không!',
            [
                ('Đáp án đúng', 'Đặt thẳng nỗi lo đời tư (anh trai xa cách, nợ nần) ngay cạnh sự an tâm từ giờ tàu 8:14 chính xác từng giây.'),
                ('Contradiction', 'Nói tàu bị trễ tới 3 tiếng — trái với "rigid predictability".'),
                ('Half-Match / Missing Emotion', 'Chỉ nói trí nhớ lịch trình tốt, không nhắc giai đoạn đời tư rối ren hay cảm giác an ủi.'),
                ('Wrong Character Focus', 'Tập trung vào hành khách thay vì tâm trạng của trưởng ga Jonas.'),
            ]
        ),
        q_item(
            'd5_3_q10', 10, 'Information and Ideas', 'Command of Evidence (Textual)', 'Elite (750+)',
            '<p>A historian studying nineteenth-century naturalists claims that botanist Marianne North was frustrated by museum directors who valued pressed, colorless herbarium specimens over her vibrant oil paintings of living plants in their native ecosystems.</p>',
            'Which quotation from Marianne North’s correspondence most effectively illustrates the historian’s claim?',
            [
                '“In Brazil I rose before five every morning to paint the passionflower before noon heat curled its delicate tendrils.”',
                '“How maddening it is that the gentlemen of the Royal Society treasure a flattened brown stalk glued to rag paper, yet dismiss my canvases showing the living tree, its pollinating moths, and the red volcanic soil that feeds it as mere amateur ornament!”',
                '“Sir Joseph Hooker kindly arranged for a brick gallery at Kew Gardens to display more than eight hundred of my botanical paintings to the public.”',
                '“Pressed specimens are easily packed inside flat tin trunks and rarely suffer damp mildew during six-week ocean crossings.”'
            ],
            'B',
            'Checklist 3 vế: [1] Sự bức bối ("frustrated") + [2] Nhắm vào giới lãnh đạo bảo tàng/học viện chuộng mẫu thực vật ép khô mất màu + [3] Hơn tranh sơn dầu vẽ cây sống trong hệ sinh thái tự nhiên. A tả lịch vẽ ở Brazil; C kể sự ủng hộ tử tế của Hooker (ngược frustration!); D khen ưu điểm bảo quản mẫu ép khô (ngược!). Duy nhất B bùng nổ trọn vẹn sự bức bối ("How maddening it is...") và đối chiếu mẫu ép nâu dẹt với tranh vẽ cây sống cùng bướm thụ phấn và đất núi lửa!',
            'Tìm đúng giọng điệu cảm xúc ("frustrated" → "How maddening it is...") cùng phép đối chiếu chính xác hai loại hiện vật!',
            [
                ('Topic Keyword Lure', 'Chỉ kể thói quen vẽ hoa lạc tiên buổi sáng ở Brazil.'),
                ('Đáp án đúng', 'Thể hiện rõ sự bực bội trước các học giả tôn thờ mẫu cây ép khô mất màu và xem thường tranh vẽ cây sống gắn với hệ sinh thái.'),
                ('Contradiction', 'Nói về sự trân trọng và hỗ trợ trưng bày hơn 800 bức tranh — trái ngược với sự bức bối bị coi nhẹ.'),
                ('Opposite Attitude', 'Khen ưu điểm vận chuyển của mẫu ép khô, không có sự bất bình.'),
            ]
        ),
        q_item(
            'd5_3_q11', 11, 'Information and Ideas', 'Command of Evidence (Textual)', 'Elite (750+)',
            '<p>A literary critic examining the 1906 novel <i>The Salt Road</i> argues that although the protagonist, Tariq, initially travels eastward hoping to escape memories of his childhood home, encountering unfamiliar landscapes unexpectedly sharpens his appreciation for the subtle beauty of his native desert.</p>',
            'Which quotation from <i>The Salt Road</i> most effectively illustrates the critic’s claim?',
            [
                '“When Tariq sold his father’s storehouse and joined the spice caravan, he swore he would never look back at the dry ochre cliffs of his youth.”',
                '“Along the emerald river valleys of the east, travelers traded cinnamon, silk, and hammered silver bowls under canvas awnings.”',
                '“Standing amid the lush cedar forests he had once dreamed of reaching, Tariq felt a sudden pang of surprise: only against this relentless green did he finally perceive the luminous violet shadows and crystalline silence of the dunes he had fled.”',
                '“After three months on the eastern road, Tariq realized that merchant guilds in coastal cities charged far higher taxes than caravan leaders had warned.”'
            ],
            'C',
            'Checklist 3 vế: [1] Ban đầu bỏ đi tìm cách thoát khỏi quê nhà sa mạc + [2] Gặp cảnh quan xa lạ (rừng tuyết tùng xanh mướt) + [3] Bất ngờ làm sâu sắc thêm cảm nhận vẻ đẹp tinh tế của sa mạc quê hương. A chỉ có [1]; B chỉ tả chợ phương đông; D nói về thuế thương hội. Duy nhất C trọn vẹn: giữa rừng tuyết tùng xanh mướt anh từng mơ tới, chính nền xanh đó khiến anh bất ngờ nhận ra sắc bóng tím rực rỡ và sự tĩnh lặng pha lê của cồn cát mình từng chạy trốn!',
            'Bẫy Half-Match (A) chỉ cắt đúng đoạn bỏ đi lúc đầu — luôn kiểm tra xem trích dẫn đã có bước ngoặt "unexpectedly sharpens appreciation" chưa!',
            [
                ('Half-Match Trap', 'Chỉ thể hiện ý định trốn chạy lúc đầu [1], chưa có bước ngoặt nhận ra vẻ đẹp quê nhà [2][3].'),
                ('Irrelevant Setting', 'Chỉ mô tả cảnh buôn bán dọc thung lũng sông.'),
                ('Đáp án đúng', 'Khớp trọn 3 yếu tố: giữa cảnh rừng xanh lạ lẫm → bất ngờ nhận ra vẻ đẹp tinh tế của cồn cát mình từng chạy trốn.'),
                ('Out of Scope', 'Chỉ nói về thuế của các phường hội thương nhân.'),
            ]
        ),
        q_item(
            'd5_3_q12', 12, 'Information and Ideas', 'Command of Evidence (Textual)', 'Hard',
            '<p>A theater scholar writing about the 1938 play <i>Backstage at Nine</i> argues that veteran actress Nora views stage fright not as a flaw to be eradicated, but as a vital source of creative alertness that keeps a performance alive.</p>',
            'Which quotation from Nora in <i>Backstage at Nine</i> most effectively illustrates the scholar’s claim?',
            [
                '“Before every opening night I pace behind the velvet curtain until my hands turn cold as porcelain.”',
                '“Young actors often forget their opening cues when the auditorium lights dim too abruptly.”',
                '“I have played this final monologue four hundred times, yet I still check the props table every evening.”',
                '“The evening my pulse stops racing before the curtain rises is the evening I hang up my costume—that sharp edge of terror is the very spark that stops a speech from turning into dead recitation.”'
            ],
            'D',
            'Checklist 2 vế: [1] Không coi nỗi hồi hộp sân khấu là khuyết điểm cần xóa bỏ + [2] Coi nó là nguồn năng lượng tỉnh táo sáng tạo giúp vai diễn sống động. A chỉ tả triệu chứng hồi hộp (tay lạnh), chưa nói quan điểm tích cực của Nora! D chốt sắc nét: đêm nào tim hết đập rộn là đêm bà giải nghệ — chính lưỡi dao lo âu ấy là tia lửa ngăn lời thoại biến thành bài học thuộc lòng vô hồn! Chọn D!',
            'Phân biệt "Mô tả hiện tượng" (A: tay lạnh trước giờ diễn) với "Quan điểm đánh giá về hiện tượng" (D: coi đó là tia lửa sống còn của nghệ thuật)!',
            [
                ('Incomplete / Symptom Only', 'Chỉ mô tả triệu chứng hồi hộp (đi lại, tay lạnh), không thể hiện quan điểm coi nó là nguồn sinh khí sáng tạo.'),
                ('Wrong Character / Irrelevant', 'Nói về diễn viên trẻ quên thoại khi tắt đèn.'),
                ('Irrelevant Habit', 'Chỉ nêu thói quen kiểm tra đạo cụ, không nhắc stage fright.'),
                ('Đáp án đúng', 'Khẳng định mạnh mẽ nỗi lo sân khấu là "tia lửa" giữ cho diễn xuất sống động chứ không phải lỗi cần diệt bỏ.'),
            ]
        ),
        q_item(
            'd5_3_q13', 13, 'Information and Ideas', 'Command of Evidence (Textual)', 'Elite (750+)',
            '<p>In a critical study of the 1899 novella <i>The Amber Ledger</i>, a student asserts that the bookkeeper, Henrik, quietly uses his mastery of mundane financial records to expose corruption among the shipping company’s wealthy directors.</p>',
            'Which quotation from <i>The Amber Ledger</i> most effectively illustrates the student’s assertion?',
            [
                '“Without raising his voice at the annual board meeting, Henrik simply laid three neatly tabbed freight ledgers beside the chairman’s teacup, pointing a calm forefinger to the columns where twelve phantom cargo losses matched deposits in the directors’ private coastal accounts.”',
                '“Henrik spent twelve hours a day copying timber manifests in copperplate ink, proud that no blot had ever marred a single page under his care.”',
                '“The company’s directors arrived at the dockside office in lacquered carriages, discussing railway shares while ignoring the clerks at the lower desks.”',
                '“Furious over his meager winter bonus, Henrik slammed the counting-house door and vowed to seek employment at a rival brokerage in Hamburg.”'
            ],
            'A',
            'Checklist 3 vế: [1] Lặng lẽ/điềm tĩnh ("quietly") + [2] Dùng sự am hiểu sổ sách tài chính thường nhật ("mastery of mundane financial records") + [3] Phơi bày tham nhũng của ban giám đốc giàu có ("expose corruption"). B chỉ nói chép sổ sạch đẹp; C chỉ tả sự kiêu ngạo của giám đốc; D tức giận đòi nghỉ việc vì thưởng thấp (sai "quietly" và không phơi bày tham nhũng!). Duy nhất A khớp 100% cả 3 vế!',
            'Kiểm tra đủ cả hành động ("expose corruption"), phương tiện ("freight ledgers") và phong thái ("without raising his voice / calm forefinger")!',
            [
                ('Đáp án đúng', 'Khớp trọn 3 vế: thái độ điềm tĩnh không lớn tiếng + dùng 3 cuốn sổ vận đơn gắn thẻ gọn gàng + chỉ thẳng 12 khoản tổn thất ma chảy vào tài khoản riêng giám đốc.'),
                ('Half-Match Trap', 'Chỉ nói về sự cẩn thận trong ghi chép sổ sách, không có yếu tố phơi bày tham nhũng.'),
                ('Missing Action', 'Chỉ miêu tả vẻ giàu có kiêu ngạo của giám đốc.'),
                ('Contradiction + Wrong Motive', 'Đập cửa giận dữ vì tiền thưởng thấp — trái với phong thái lặng lẽ và không phơi bày tham nhũng.'),
            ]
        ),
    ]
    return {
        'schemaVersion': 1,
        'mode': 'drill',
        'section': 'Reading and Writing',
        'basicInfo': {
            'title': 'Drill 5.3: Command of Evidence — Literary & Historical Quotations (13 Qs)',
            'subtitle': 'Thực hành phương pháp Multi-Part Claim Checklist trên trích dẫn tiểu thuyết, thơ cổ và tư liệu lịch sử thế kỷ 19–20.',
            'difficultyBadge': 'I&I • Target 1500+',
            'targetTimeMinutes': 15,
        },
        'drillModule': {
            'id': 'drill_5_3_mod',
            'title': 'Skill Drill 5.3: Literary & Historical Quotations',
            'timeLimitMinutes': 15,
            'questions': questions,
        },
    }
