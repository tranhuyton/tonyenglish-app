# -*- coding: utf-8 -*-
"""
Full-Length Adaptive Mock Test #5 — Module 2 LOWER/STANDARD Route (27 Qs, Easy/Medium, 32 min)
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
            'm5_m2l_q1', 1, 'Craft and Structure', 'Words in Context', 'Easy',
            '<p>Because deep-sea hydrothermal vents lie miles beneath the ocean surface in total darkness, pale vent crabs rely on sensitive chemical receptors on their antennae rather than eyesight to ______ nearby bacterial mats to eat.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            ['erase', 'conceal', 'invent', 'locate'],
            'D',
            'Cause-Effect Clue: sống dưới đáy biển tối đen không dùng thị giác → cua phải dùng cơ quan cảm nhận hóa học trên râu để XÁC ĐỊNH VỊ TRÍ / TÌM THẤY thảm vi khuẩn để ăn → "locate" (D).',
            'Cơ quan cảm biến thay cho mắt để tìm nguồn thức ăn gần đó → chọn động từ nghĩa "định vị/tìm thấy" ("locate").',
            [
                ('Wrong Meaning', 'erase = xóa bỏ — sai hoàn toàn với mục đích tìm thức ăn.'),
                ('Opposite Meaning', 'conceal = che giấu — cua muốn tìm thức ăn chứ không giấu thức ăn.'),
                ('Wrong Meaning', 'invent = phát minh — cua không phát minh ra thảm vi khuẩn.'),
                ('Đáp án đúng', 'locate = xác định vị trí, tìm thấy — khớp hoàn toàn với việc dùng cảm biến hóa học thay mắt trong bóng tối.'),
            ]
        ),
        q_item(
            'm5_m2l_q2', 2, 'Craft and Structure', 'Words in Context', 'Easy',
            '<p>Before wooden screw printing presses arrived in Venice in 1469, scribes had to copy every book painstakingly by hand onto prepared animal skins, making manuscripts so ______ that only wealthy princes and monasteries could afford a personal library.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            ['fragile', 'costly', 'brief', 'playful'],
            'B',
            'Cause-Effect Clue: chép tay cực nhọc trên da thú khiến chỉ các hoàng thân giàu có và tu viện mới ĐỦ KHẢ NĂNG MUA ("could afford") → RẤT ĐẮT ĐỎ → "costly" (B).',
            'Từ khóa "only wealthy princes... could afford" chỉ thẳng tính từ về giá cả đắt đỏ ("costly").',
            [
                ('Off-Point', 'fragile = dễ vỡ — không trực tiếp giải thích vì sao chỉ giới giàu mới mua nổi ("afford").'),
                ('Đáp án đúng', 'costly = đắt đỏ — khớp 100% với manh mối tài chính "only wealthy... could afford".'),
                ('Wrong Meaning', 'brief = ngắn gọn — không liên quan đến khả năng chi trả.'),
                ('Wrong Tone', 'playful = vui nhộn tinh nghịch — lạc ngữ cảnh hoàn toàn.'),
            ]
        ),
        q_item(
            'm5_m2l_q3', 3, 'Craft and Structure', 'Words in Context', 'Medium',
            '<p>Coating dark urban rooftops with pale solar-reflective sealants helps ______ heat absorption during intense July afternoons, keeping top-floor apartments noticeably cooler while reducing air-conditioning demand.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            ['intensify', 'trigger', 'curb', 'display'],
            'C',
            'Cause-Effect Clue: phủ sơn phản xạ ánh nắng sáng màu giúp căn hộ tầng trên mát hơn rõ rệt và giảm nhu cầu điều hòa → GIẢM BỚT / KIỀM CHẾ sự hấp thụ nhiệt → "curb" (C).',
            'Hiệu quả làm mát căn hộ và giảm điều hòa đòi hỏi động từ nghĩa "hạn chế, kìm giảm" ("curb") sự hấp thụ nhiệt.',
            [
                ('Opposite Meaning', 'intensify = làm tăng mạnh — trái ngược hoàn toàn với mục đích làm mát.'),
                ('Opposite Meaning', 'trigger = kích hoạt gây ra — sai hướng nghĩa.'),
                ('Đáp án đúng', 'curb = kiềm chế, giảm bớt — khớp chuẩn với "solar-reflective" và "noticeably cooler".'),
                ('Wrong Context', 'display = trưng bày — vô nghĩa với "heat absorption".'),
            ]
        ),
        q_item(
            'm5_m2l_q4', 4, 'Craft and Structure', 'Words in Context', 'Medium',
            '<p>Even when thick tropical storm clouds temporarily hide the stars overhead, experienced Polynesian navigators remain ______ rather than anxious, calmly shifting their focus to the steady rhythm of ocean swells rolling beneath the canoe’s hull.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            ['composed', 'frantic', 'distracted', 'impatient'],
            'A',
            'Contrast + Mirror Clue: đối lập trực tiếp với "rather than anxious" (thay vì lo lắng) + phản chiếu trạng từ "calmly shifting their focus" (bình tĩnh chuyển sự chú ý) → ĐIỀM TĨNH, BÌNH TĨNH → "composed" (A).',
            'Bám sát cặp từ "rather than anxious" + "calmly" → chọn tính từ nghĩa điềm tĩnh tự chủ ("composed").',
            [
                ('Đáp án đúng', 'composed = điềm tĩnh, tự chủ — đối lập trực tiếp với "anxious" và đồng điệu với "calmly".'),
                ('Opposite Meaning', 'frantic = hoảng loạn cuống cuồng — trái ngược với "calmly".'),
                ('Negative Tone', 'distracted = mất tập trung — trái với việc chuyển sự chú ý chính xác sang nhịp sóng.'),
                ('Negative Tone', 'impatient = thiếu kiên nhẫn — mâu thuẫn với sự bình tĩnh.'),
            ]
        ),
        q_item(
            'm5_m2l_q5', 5, 'Craft and Structure', 'Words in Context', 'Easy',
            '<p>To prevent ancient air bubbles inside Antarctic ice cores from melting during the long ocean voyage to European laboratories, drilling teams seal every core section inside insulated freezer containers that maintain a ______ temperature well below freezing.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            ['fluctuating', 'constant', 'tropical', 'accidental'],
            'B',
            'Cause-Effect Clue: để ngăn bọt khí cổ tan chảy trong suốt hành trình dài → container đông lạnh cách nhiệt phải duy trì một mức nhiệt độ ỔN ĐỊNH / KHÔNG ĐỔI dưới điểm đóng băng → "constant" (B).',
            'Mục tiêu bảo quản lõi băng không bị tan chảy yêu cầu nhiệt độ ổn định đều đặn ("constant").',
            [
                ('Opposite Meaning', 'fluctuating = dao động lên xuống thất thường — dễ làm hỏng và tan lõi băng.'),
                ('Đáp án đúng', 'constant = ổn định, không thay đổi — khớp chuẩn mục đích bảo quản lạnh.'),
                ('Opposite Meaning', 'tropical = nhiệt đới nóng ẩm — trái ngược hoàn toàn với "well below freezing".'),
                ('Wrong Meaning', 'accidental = tình cờ — nhiệt độ được kiểm soát chủ động bởi container đông lạnh.'),
            ]
        ),

        # --- Q6-Q7: Craft and Structure — Text Structure and Purpose (Easy / Medium) ---
        q_item(
            'm5_m2l_q6', 6, 'Craft and Structure', 'Text Structure and Purpose', 'Easy',
            '<p>Although a pistol shrimp measures barely five centimeters long, it is one of the loudest animals in any tropical coral reef. <u>When the shrimp snaps its oversized claw shut at lightning speed, it fires a high-velocity water jet that forms a tiny vapor bubble, which collapses milliseconds later with a sharp crack loud enough to stun nearby prey.</u> Thousands of these shrimp snapping simultaneously across a reef produce the constant sizzling backdrop heard on marine hydrophones.</p>',
            'Which choice best describes the function of the underlined sentence in the text as a whole?',
            [
                'It explains the physical mechanism by which a pistol shrimp generates its remarkably loud underwater sound.',
                'It questions whether pistol shrimp actually live inside tropical coral reefs.',
                'It compares the body length of pistol shrimp with that of other reef crustaceans.',
                'It warns that marine hydrophones can startle pistol shrimp into dropping their claws.'
            ],
            'A',
            'Câu 1 giới thiệu tôm gõ mõ nhỏ bé nhưng phát âm cực lớn. Câu gạch chân giải thích chi tiết CƠ CHẾ VẬT LÝ tạo ra tiếng nổ ấy (kẹp càng cực nhanh → bắn tia nước tốc độ cao → tạo bọt khí nhỏ → bọt vỡ tung phát tiếng nổ làm choáng con mồi) → Chọn A!',
            'Câu nằm ngay sau lời giới thiệu hiện tượng ấn tượng thường đóng vai trò giải thích "BẰNG CÁCH NÀO / CƠ CHẾ GÌ" tạo nên hiện tượng đó.',
            [
                ('Đáp án đúng', 'Mô tả chính xác cơ chế vật lý tạo tia nước và nổ bọt khí tạo nên tiếng vang cực lớn của tôm gõ mõ.'),
                ('Contradiction', 'Bài khẳng định tôm gõ mõ sống đầy trong rạn san hô nhiệt đới.'),
                ('Out of Scope', 'Không so sánh chiều dài cơ thể tôm gõ mõ với loài giáp xác nào khác.'),
                ('Out of Scope', 'Hydrophone chỉ là máy ghi âm thụ động, không làm tôm rụng càng.'),
            ]
        ),
        q_item(
            'm5_m2l_q7', 7, 'Craft and Structure', 'Text Structure and Purpose', 'Medium',
            '<p><i>The following text is adapted from an 1848 travel letter written in New York’s Hudson Valley. The writer climbs a pine-covered ridge before sunrise to view the river below.</i><br/>At five o’clock the entire valley lay hidden beneath a flat sea of gray vapor, leaving nothing visible except the dark crowns of nearby hemlocks. Within twenty minutes, however, the first copper edge of the sun cleared the eastern hills; golden shafts broke through the mist, parting it into drifting ribbons until white farmhouses, silver creeks, and the broad Hudson itself emerged bright and distinct below.</p>',
            'Which choice best states the main purpose of the text?',
            [
                'To argue that morning fog makes hiking in the Hudson Valley dangerously unpredictable.',
                'To criticize farmers for building white houses along the banks of the Hudson River.',
                'To explain how temperature differences create dense vapor layers over eastern hills.',
                'To depict the gradual visual unveiling of a misty valley landscape as sunrise breaks through.'
            ],
            'D',
            'Đoạn văn miêu tả sự biến chuyển thị giác đầy chất thơ theo thời gian: lúc 5 giờ thung lũng chìm trong biển sương xám đặc → 20 phút sau mặt trời ló rạng, tia nắng vàng xé sương thành từng dải mỏng để lộ dần nhà nông trang trắng, con suối ánh bạc và dòng sông Hudson rực rỡ bên dưới → Chọn D!',
            'Đọc theo trình tự thời gian ("At five o’clock... hidden" → "Within twenty minutes... emerged bright and distinct") để chốt mục đích miêu tả cảnh sắc chuyển biến!',
            [
                ('Out of Scope / Wrong Tone', 'Không hề nhắc đến nguy hiểm khi leo núi.'),
                ('Out of Scope', 'Không có lời chỉ trích nào đối với nông dân hay nhà màu trắng.'),
                ('Literal Misreading', 'Đây là thư du ký miêu tả phong cảnh, không phải bài giảng khí tượng về chênh lệch nhiệt độ.'),
                ('Đáp án đúng', 'Gom gọn trọn vẹn cảnh sương tan dần và phong cảnh thung lũng hiện rõ dưới ánh bình minh.'),
            ]
        ),

        # --- Q8: Craft and Structure — Cross-Text Connections (Medium) ---
        q_item(
            'm5_m2l_q8', 8, 'Craft and Structure', 'Cross-Text Connections', 'Medium',
            '<p><b>Text 1</b><br/>Rare-book curator Dr. Elena Conti notes that during the early sixteenth century, Venetian bookbinders largely abandoned traditional heavy oak boards in favor of thin pasteboard covers made from layered paper sheets. Conti contends that binders made this switch primarily to lighten pocket editions for traveling scholars who carried books in coat pockets and saddlebags.</p><p><b>Text 2</b><br/>Examining Venetian guild expense accounts from 1500 to 1530, book conservator Dr. Marco Bellini confirms that traveling readers appreciated lighter pasteboard bindings. Yet Bellini points out that binders also faced an acute local shortage of seasoned oak lumber because Venice’s massive Arsenal shipyard was buying up nearly all nearby hardwood for naval war galleys, making recycled paper pasteboard a far more economical choice.</p>',
            'Based on the texts, how would Dr. Marco Bellini (Text 2) most likely respond to Dr. Elena Conti’s contention (Text 1)?',
            [
                'By arguing that sixteenth-century traveling scholars preferred carrying heavy oak-bound books rather than lightweight pasteboard volumes.',
                'By asserting that Venetian workshops never actually adopted pasteboard covers during the early sixteenth century.',
                'By agreeing that lighter pasteboard covers appealed to travelers, while adding that oak shortages and timber costs also played a major role in the switch.',
                'By claiming that the Venetian Arsenal shipyard built its naval galleys out of layered paper sheets.'
            ],
            'C',
            'Text 1 giải thích nguyên nhân đổi từ bìa gỗ sồi sang bìa giấy bồi chủ yếu để sách nhẹ cho học giả đi xa. Text 2 mở đầu bằng vế đồng tình ("confirms that traveling readers appreciated lighter pasteboard bindings") rồi bổ sung thêm động lực kinh tế quan trọng ("Yet... also faced an acute local shortage of seasoned oak lumber" vì xưởng đóng tàu Arsenal thu mua hết gỗ cứng, khiến giấy bồi tái chế tiết kiệm hơn nhiều) → Chọn C!',
            'Nhận diện mối quan hệ "Agree + Add another major factor": `confirms... Yet also faced...` → đáp án chuẩn luôn chứa cả hai vế!',
            [
                ('Contradiction', 'Bellini xác nhận độc giả đi xa ĐÁNH GIÁ CAO bìa giấy bồi nhẹ hơn.'),
                ('Contradiction', 'Cả hai văn bản đều bàn về việc các xưởng Venice đã chuyển sang bìa giấy bồi.'),
                ('Đáp án đúng', 'Phản ánh đủ hai vế của Bellini: đồng ý lợi ích nhẹ cho người đi xa + bổ sung nguyên nhân khan hiếm và đắt đỏ gỗ sồi do ngành đóng tàu.'),
                ('Absurd Distortion', 'Xưởng đóng tàu Arsenal thu mua GỖ CỨNG (hardwood) đóng chiến thuyền, không phải đóng tàu bằng giấy bồi.'),
            ]
        ),

        # --- Q9-Q10: Information and Ideas — Central Ideas and Details (Easy / Medium) ---
        q_item(
            'm5_m2l_q9', 9, 'Information and Ideas', 'Central Ideas and Details', 'Easy',
            '<p>Dark conventional asphalt roads absorb up to 90 percent of incoming summer sunlight, storing that solar energy all afternoon and radiating warmth back into city neighborhoods long after sunset. By contrast, high-albedo reflective pavements bounce away a much larger fraction of daytime sunlight, keeping road surfaces cooler during the afternoon and allowing surrounding residential blocks to cool down faster at night.</p>',
            'Which choice best states the main idea of the text?',
            [
                'Dark asphalt roads reflect more daytime sunlight than high-albedo reflective pavements do.',
                'Reflective pavements help keep urban streets and nighttime neighborhoods cooler than dark asphalt because they reflect more sunlight and store less heat.',
                'Residential neighborhoods experience warmer temperatures at night only when summer days are completely cloudy.',
                'City engineers have banned dark conventional asphalt from every residential street worldwide.'
            ],
            'B',
            'Ý chính đối chiếu trực tiếp hai loại mặt đường: nhựa đường tối hấp thụ tới 90% nắng rồi tỏa nhiệt kéo dài sau hoàng hôn ↔ mặt đường phản quang hắt ngược phần lớn ánh nắng ban ngày nên giữ mặt đường mát hơn và giúp khu dân cư hạ nhiệt nhanh hơn ban đêm → Chọn B!',
            'Gom gọn nguyên nhân (reflect more sunlight, store less heat) và kết quả (cooler streets & faster nighttime cooling).',
            [
                ('Reversed Logic', 'Nhựa đường tối HẤP THỤ tới 90% nắng, còn mặt đường phản quang mới là loại phản xạ nhiều hơn.'),
                ('Đáp án đúng', 'Tóm tắt chính xác cả cơ chế phản xạ ánh nắng lẫn lợi ích làm mát ban ngày và ban đêm của mặt đường phản quang.'),
                ('Out of Scope', 'Không hề nhắc đến ngày nhiều mây.'),
                ('Too Extreme / Out of Scope', 'Không hề nói nhựa đường tối đã bị cấm trên toàn thế giới.'),
            ]
        ),
        q_item(
            'm5_m2l_q10', 10, 'Information and Ideas', 'Central Ideas and Details', 'Medium',
            '<p><i>The following poem is adapted from an 1869 American coastal lyric titled “The Lantern on the Pier.”</i><br/>Through harbor fog the iron bell<br/>Clangs steady from the pilings wet,<br/>While Captain Ross trims wick and glass<br/>Before the evening tide has set.<br/><br/>No ship may praise his steady flame<br/>Nor call his quiet watch by name,<br/>Yet every trawler rounding home<br/>Steers safely past the hidden shoal.</p>',
            'According to the poem, what does Captain Ross’s steady lantern achieve for returning fishing boats?',
            [
                'Although his quiet service goes unrecognized by passing crews, his lantern safely guides returning trawlers around a submerged harbor hazard.',
                'It encourages returning crews to stop at the pier and celebrate Captain Ross by name.',
                'It clears away the thick harbor fog before the evening tide rises.',
                'It warns passing vessels that the iron harbor bell has stopped ringing.'
            ],
            'A',
            'Khổ 2 nêu rõ cả hai ý: Không con tàu nào khen ngợi hay gọi tên ca trực lặng lẽ của ông ("No ship may praise his steady flame / Nor call his quiet watch by name"), NHƯNG ("Yet") mọi tàu đánh cá quay về đều lái an toàn vòng qua bãi cạn ẩn dưới nước ("Steers safely past the hidden shoal") → Chọn A!',
            'Đọc trực tiếp 4 dòng cuối của bài thơ: không cần lời khen hay nêu tên, nhưng giúp mọi tàu về bến tránh an toàn bãi cạn ngầm ("hidden shoal")!',
            [
                ('Đáp án đúng', 'Paraphrase chuẩn xác khổ 2: sự cống hiến thầm lặng không được gọi tên nhưng dẫn lối an toàn qua bãi cạn ẩn.'),
                ('Contradiction', 'Bài thơ nói rõ không con tàu nào ca ngợi hay gọi tên ông ("No ship may praise... Nor call... by name").'),
                ('Fact Distortion', 'Ngọn đèn giúp tàu nhìn thấy đường tránh bãi cạn chứ không xua tan được sương mù.'),
                ('Contradiction', 'Khổ 1 nói chuông sắt vẫn vang đều đặn ("Clangs steady").'),
            ]
        ),

        # --- Q11-Q12: Information and Ideas — Command of Evidence (Textual, Easy / Medium) ---
        q_item(
            'm5_m2l_q11', 11, 'Information and Ideas', 'Command of Evidence (Textual)', 'Medium',
            '<p>Stalked barnacles of the genus <i>Neolepas</i> cluster tightly along the warm flanks of deep-sea hydrothermal chimneys in the Pacific Ocean. Marine biologist Dr. Priya Nair hypothesized that these barnacles feed primarily by combing free-floating chemosynthetic bacteria out of rising vent plumes, rather than capturing tiny dead plankton drifting down from sunlit surface waters miles above.</p>',
            'Which finding, if true, would most directly support Dr. Priya Nair’s hypothesis?',
            [
                'Sunlight cannot penetrate deeper than about 200 meters beneath the Pacific Ocean’s surface.',
                'Stalked barnacles living in shallow coastal tide pools commonly eat microscopic surface plankton.',
                'Hydrothermal vent chimneys along the Pacific ridge frequently exceed ten meters in height.',
                'Laboratory analysis of <i>Neolepas</i> digestive tracts reveals almost exclusively sulfur-oxidizing bacteria native to warm vent plumes, with virtually no traces of surface-water plankton.'
            ],
            'D',
            'Khóa giả thuyết Nair: Con hà *Neolepas* ăn chủ yếu VI KHUẨN HÓA TỔNG HỢP từ dòng phun thủy nhiệt (X1), KHÔNG ăn sinh vật phù du rơi từ tầng mặt (NOT X2). Bằng chứng trực tiếp nhất chính là soi trực tiếp BÊN TRONG DẠ DÀY của chính loài *Neolepas*: chứa hầu như toàn vi khuẩn oxy hóa lưu huỳnh của miệng thủy nhiệt và gần như không có dấu vết phù du tầng mặt → Chọn D!',
            'Giả thuyết về chế độ ăn (ăn A chứ không ăn B) → tìm bằng chứng phân tích trực tiếp thức ăn trong ống tiêu hóa chứa A và vắng B!',
            [
                ('Adjacent Topic Drift', 'Việc ánh sáng chỉ xuống sâu 200m không trực tiếp chứng minh con hà ăn gì (sinh vật phù du chết vẫn có thể chìm xuống sâu).'),
                ('Irrelevant Subject', 'Chế độ ăn của loài hà sống ở vùng triều nông không chứng minh chế độ ăn của *Neolepas* dưới đáy sâu.'),
                ('Irrelevant Detail', 'Chiều cao 10 mét của ống khói thủy nhiệt không liên quan đến thức ăn của hà.'),
                ('Đáp án đúng', 'Bằng chứng trực diện từ phân tích ống tiêu hóa: toàn vi khuẩn miệng thủy nhiệt, gần như không có phù du tầng mặt.'),
            ]
        ),
        q_item(
            'm5_m2l_q12', 12, 'Information and Ideas', 'Command of Evidence (Textual)', 'Easy',
            '<p>In a short essay on the 1893 American realist story <i>The Cedar Orchard</i>, a student argues that retired farmer Caleb cherishes his old wooden cider press not for the small profit it earns, but for the warm community gathering it brings together each autumn.</p>',
            'Which quotation from Caleb in <i>The Cedar Orchard</i> most effectively illustrates the student’s claim?',
            [
                '“My grandfather built this oak beam frame in 1854 using timber hauled down from the northern ridge.”',
                '“The cider jugs scarcely cover the cost of new barrels anymore, yet I would never part with that old press while half the county still arrives with apple baskets, swaps news on the porch, and turns October into a neighborhood reunion.”',
                '“Late frosts in May ruined nearly half of the sweet russet blossoms along our lower pasture fence this spring.”',
                '“You must scrub the wooden slats thoroughly with cold spring water every evening so the juice stays crisp.”'
            ],
            'B',
            'Checklist 2 vế từ Claim: [1] Không phải vì lợi nhuận nhỏ bé + [2] Trân quý buổi tụ họp ấm áp của cộng đồng mỗi mùa thu. Duy nhất B thể hiện trọn vẹn cả hai vế: "scarcely cover the cost of new barrels" [1] + "would never part with that old press while half the county... turns October into a neighborhood reunion" [2]! Chọn B!',
            'Tìm đúng câu thoại bác bỏ giá trị tiền bạc ("scarcely cover the cost") và tôn vinh sự sum họp làng xóm ("neighborhood reunion")!',
            [
                ('Irrelevant Detail', 'Chỉ kể năm và nguồn gỗ đóng máy ép táo, không nhắc lợi nhuận hay buổi tụ họp.'),
                ('Đáp án đúng', 'Khớp đủ cả hai vế: tiền bán không bõ chi phí nhưng giữ máy vì cuộc sum họp mùa thu của cả vùng.'),
                ('Off-Point', 'Chỉ nhắc đợt sương giá tháng Năm làm hỏng hoa táo.'),
                ('Irrelevant Detail', 'Chỉ hướng dẫn cách rửa thanh gỗ cho sạch nước ép.'),
            ]
        ),

        # --- Q13-Q14: Information and Ideas — Command of Evidence (Quantitative, Easy / Medium) ---
        q_item(
            'm5_m2l_q13', 13, 'Information and Ideas', 'Command of Evidence (Quantitative)', 'Easy',
            svg_bar_chart(
                'Typical Maximum Sighting Distance (km) of Four Pacific Island-Finding Cues',
                ['0', '15', '30', '45', '60'],
                [('Volcanic Peak', 55, '55 km'), ('Reflected Swell', 42, '42 km'), ('Homing Terns', 36, '36 km'), ('Lagoon Cloud Glow', 28, '28 km')],
                60
            ) + '<p>Traditional Pacific wayfinders use several natural signs to detect unseen islands before land actually appears on the horizon. Although tall volcanic mountain peaks can be spotted from the farthest distance on clear days, navigators approaching flat, low-lying coral atolls—which have no tall mountains—rely first on ocean swells reflected off the island because swells reveal an atoll from farther away than either homing terns or greenish lagoon cloud reflections.</p>',
            'Which choice most effectively uses data from the graph to support the claim about detecting low-lying coral atolls?',
            [
                'Tall volcanic mountain peaks can typically be sighted from up to 55 km away on clear days.',
                'Lagoon cloud glow provides the shortest maximum detection distance in the graph at 28 km.',
                'Reflected ocean swells can typically be detected from up to 42 km away, exceeding the maximum sighting distances of both homing terns (36 km) and lagoon cloud glow (28 km).',
                'All four traditional island-finding cues allow navigators to detect an island from more than 25 km away.'
            ],
            'C',
            'Khóa tuyên bố về rạn san hô thấp (không có đỉnh núi lửa cao): Sóng phản xạ (Reflected Swell) giúp phát hiện đảo TỪ XA HƠN cả chim nhạn về tổ (Homing Terns) lẫn ánh mây đầm phá (Lagoon Cloud Glow)! Đối chiếu số liệu trên biểu đồ: **Reflected Swell = 42 km > Homing Terns (36 km) và Lagoon Cloud Glow (28 km)** → Khớp 100% ở C!',
            'Đối chiếu trực tiếp 3 cột áp dụng cho đảo san hô thấp: 42 km (Reflected Swell) > 36 km (Homing Terns) > 28 km (Lagoon Cloud Glow)!',
            [
                ('Wrong Subject', 'Chỉ nhắc đỉnh núi lửa cao 55 km — đảo san hô thấp không có đỉnh núi lửa.'),
                ('Incomplete Data', 'Chỉ nêu mốc thấp nhất 28 km, bỏ quên số liệu 42 km của Reflected Swell và 36 km của Homing Terns.'),
                ('Đáp án đúng', 'Dẫn đủ và chính xác cả 3 con số chứng minh Reflected Swell (42 km) vượt xa cả Homing Terns (36 km) lẫn Lagoon Cloud Glow (28 km).'),
                ('True Data / Wrong Claim', 'Chỉ nêu cả 4 cột đều trên 25 km, không so sánh thứ tự ưu tiên giữa các dấu hiệu.'),
            ]
        ),
        q_item(
            'm5_m2l_q14', 14, 'Information and Ideas', 'Command of Evidence (Quantitative)', 'Medium',
            html_table(
                'Table 1. Mean Underwater Sound Intensity (dB) Recorded at Four Tropical Reef Sites',
                ['Reef Site', 'Reef Condition', 'Midday Sound (dB)', 'Dusk Chorus (dB)'],
                [
                    ['Emerald Atoll', 'Healthy', '108', '122'],
                    ['Kestrel Cay', 'Healthy', '106', '119'],
                    ['Basalt Shoal', 'Bleached', '95', '97'],
                    ['Pebble Reef', 'Bleached', '94', '96'],
                ]
            ) + '<p>Marine acoustic researchers report that healthy coral reefs not only remain much louder than bleached reefs during both midday and dusk, but also experience a far larger rise in underwater sound intensity when the evening fish chorus begins at dusk.</p>',
            'Which choice most effectively uses data from the table to support the researchers’ report?',
            [
                'Healthy sites Emerald Atoll and Kestrel Cay stayed louder than both bleached sites at midday (108 dB and 106 dB vs. 95 dB and 94 dB) and jumped by 14 dB and 13 dB at dusk, whereas bleached sites Basalt Shoal and Pebble Reef rose by only 2 dB each at dusk.',
                'Basalt Shoal recorded a mean sound intensity of 95 dB at midday and 97 dB at dusk, slightly louder than Pebble Reef at both times of day.',
                'Emerald Atoll recorded the highest dusk chorus sound intensity in the entire study at 122 dB.',
                'All four reef sites listed in the table recorded higher sound levels at dusk than at midday.'
            ],
            'A',
            'Checklist 2 vế báo cáo: [1] Rạn khỏe ồn hơn nhiều ở cả trưa lẫn hoàng hôn (108/106 vs. 95/94 dB buổi trưa; 122/119 vs. 97/96 dB hoàng hôn ✓) + [2] Mức TĂNG lúc hoàng hôn lớn hơn nhiều ở rạn khỏe (Emerald: 122 − 108 = +14 dB; Kestrel: 119 − 106 = +13 dB) so với rạn bị tẩy trắng (Basalt: 97 − 95 = +2 dB; Pebble: 96 − 94 = +2 dB ✓)! Duy nhất A trình bày chuẩn xác cả hai vế và đúng tuyệt đối phép trừ!',
            'Tính nhanh hiệu số (Dusk − Midday) cho từng hàng: +14 dB và +13 dB (Healthy) vs. chỉ +2 dB và +2 dB (Bleached)!',
            [
                ('Đáp án đúng', 'Khớp đầy đủ cả mức âm thanh cao hơn lẫn biên độ tăng đột biến lúc hoàng hôn (+14/+13 dB vs. chỉ +2 dB).'),
                ('Incomplete Data', 'Chỉ so sánh hai rạn bị tẩy trắng với nhau, hoàn toàn không nhắc đến rạn khỏe.'),
                ('Incomplete Data', 'Chỉ nêu một con số đơn lẻ (122 dB), thiếu cả đối chiếu với rạn tẩy trắng lẫn mức tăng từ trưa đến hoàng hôn.'),
                ('True Data / Wrong Claim', 'Chỉ nói cả 4 rạn đều tăng vào hoàng hôn, bỏ qua sự chênh lệch lớn giữa rạn khỏe (+13/+14 dB) và rạn tẩy trắng (+2 dB).'),
            ]
        ),

        # --- Q15: Information and Ideas — Inferences (Medium) ---
        q_item(
            'm5_m2l_q15', 15, 'Information and Ideas', 'Inferences', 'Medium',
            '<p>To estimate prehistoric Antarctic air temperatures from deep ice cores, paleoclimatologists measure the proportion of heavy deuterium atoms relative to ordinary hydrogen atoms in frozen snow layers. Because air masses traveling inland from warm oceans lose heavier deuterium-bearing moisture more rapidly during colder periods than during warmer periods, scientists analyzing an ancient ice layer with an unusually low deuterium concentration can reasonably conclude that ______</p>',
            'Which choice most logically completes the text?',
            [
                'warm ocean currents flowed directly across the center of East Antarctica when that layer formed.',
                'the drilling team accidentally contaminated that section of the ice core with modern ocean water.',
                'ordinary hydrogen atoms disappear entirely from Antarctic snow whenever air temperatures drop.',
                'regional Antarctic air temperatures were unusually cold during the period when that snow originally fell.'
            ],
            'D',
            'Ghép quan hệ trực tiếp: Thời kỳ LẠNH HƠN → khối khí mất hơi nước giàu đơteri nặng NHANH HƠN trên đường đi vào lục địa → tuyết rơi sâu trong Nam Cực còn lại RẤT ÍT đơteri! Do đó khi phát hiện một lớp băng cổ có nồng độ đơteri thấp bất thường → kết luận trực tiếp: nhiệt độ không khí vùng Nam Cực thời điểm tuyết đó rơi xuống ĐẶC BIỆT LẠNH (D)!',
            'Ánh xạ thuận chiều: Colder period → loses deuterium faster → unusually LOW deuterium in ice layer ⇒ unusually cold temperatures!',
            [
                ('Reversed Logic', 'Dòng biển ấm thổi qua trung tâm lục địa băng vừa phi lý vừa ngược hướng nhiệt độ lạnh.'),
                ('Out of Scope', 'Không có chi tiết nào đề cập việc khoan làm nhiễm bẩn mẫu.'),
                ('Too Extreme', 'Bài chỉ nói giảm tỷ lệ đơteri nặng, không hề nói hydro thường biến mất hoàn toàn.'),
                ('Đáp án đúng', 'Suy luận trực tiếp 1 bước từ quy luật mất đơteri nhanh hơn trong thời kỳ lạnh.'),
            ]
        ),

        # --- Q16-Q19: Standard English Conventions — Boundaries (Easy / Medium) ---
        q_item(
            'm5_m2l_q16', 16, 'Standard English Conventions', 'Boundaries', 'Easy',
            '<p>In 1470, master type designer Nicolas Jenson opened a celebrated printing workshop in ______ his crisp, balanced Roman letterforms soon became the standard model for European book design.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['Venice,', 'Venice;', 'Venice', 'Venice, because'],
            'B',
            'Vế 1 là IC hoàn chỉnh ("In 1470, master type designer... in Venice"). Vế 2 cũng là IC hoàn chỉnh ("his crisp, balanced Roman letterforms soon became..."). Giữa 2 IC không có FANBOYS → dùng dấu chấm phẩy (`;`) = B!',
            'Nhận diện 2 mệnh đề độc lập IC + IC → chọn dấu chấm phẩy (;), loại Comma Splice (A) và Run-on (C).',
            [
                ('Comma Splice', 'Nối hai mệnh đề độc lập chỉ bằng một dấu phẩy là lỗi Comma Splice.'),
                ('Đáp án đúng', 'Dấu chấm phẩy (;) ngăn cách chuẩn xác hai mệnh đề độc lập IC + IC.'),
                ('Run-On Sentence', 'Không có dấu câu nào tách hai mệnh đề độc lập.'),
                ('Illogical Subordination', 'Dùng "because" tạo quan hệ nhân quả ngược (ông mở xưởng năm 1470 không phải VÌ kiểu chữ sau đó trở thành chuẩn mực).'),
            ]
        ),
        q_item(
            'm5_m2l_q17', 17, 'Standard English Conventions', 'Boundaries', 'Easy',
            '<p>Hydrothermal vent fluids gush from volcanic fissures at temperatures hot enough to melt ______ crushing deep-ocean pressure prevents the superheated water from boiling into steam.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['lead,', 'lead', 'lead, so', 'lead, but'],
            'D',
            'Vế 1 là IC (nước phun nóng đủ làm tan chảy chì). Vế 2 là IC đối lập bất ngờ (áp suất đáy biển khủng khiếp ngăn nước siêu nóng sôi thành hơi). Nối 2 IC trái ngược nhau bằng dấu phẩy + FANBOYS → `lead, but` (D)!',
            'Hai IC có ý tương phản ("hot enough to melt lead" ↔ "prevents... from boiling") → dùng `, but`!',
            [
                ('Comma Splice', 'Thiếu liên từ FANBOYS sau dấu phẩy tạo lỗi Comma Splice.'),
                ('Run-On Sentence', 'Ghép liền hai IC không có dấu câu hay liên từ.'),
                ('Wrong Conjunction', '", so" chỉ quan hệ kết quả, sai với ý tương phản (nước cực nóng nhưng không sôi).'),
                ('Đáp án đúng', '", but" vừa đúng ngữ pháp nối IC + IC vừa chuẩn nghĩa tương phản.'),
            ]
        ),
        q_item(
            'm5_m2l_q18', 18, 'Standard English Conventions', 'Boundaries', 'Medium',
            '<p>The tiny clownfish ______ listens closely for crackling reef choruses after spending several weeks drifting in the open ocean.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            [
                'larva barely larger than a grain of rice,',
                'larva, barely larger than a grain of rice',
                'larva, barely larger than a grain of rice,',
                'larva; barely larger than a grain of rice;'
            ],
            'C',
            'Cụm miêu tả phụ chen giữa Chủ ngữ ("The tiny clownfish larva") và Động từ chính ("listens") là Non-Essential Modifier ("barely larger than a grain of rice"). Nếu bỏ cụm này đi, câu vẫn hoàn chỉnh: "The tiny clownfish larva listens closely...". Do đó PHẢI bọc bằng một CẶP dấu phẩy ở cả hai đầu → `larva, barely larger than a grain of rice,` (C)!',
            'Quy tắc Cặp Phẩy Bọc Phần Phụ (2 commas or 0 commas): cụm chen giữa S và V phải có đủ phẩy mở và phẩy đóng!',
            [
                ('Unpaired Comma', 'Thiếu dấu phẩy mở đầu cụm bổ sung.'),
                ('Unpaired Comma', 'Thiếu dấu phẩy đóng trước động từ chính "listens".'),
                ('Đáp án đúng', 'Bọc đúng cặp hai dấu phẩy quanh cụm miêu tả phụ giữa chủ ngữ và động từ.'),
                ('Wrong Punctuation', 'Không bao giờ dùng cặp dấu chấm phẩy để bọc cụm bổ ngữ phụ.'),
            ]
        ),
        q_item(
            'm5_m2l_q19', 19, 'Standard English Conventions', 'Boundaries', 'Medium',
            '<p>Every Antarctic ice core preserves three vital climate ______ annual snowfall layers, microscopic volcanic dust, and tiny bubbles of prehistoric air.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['records:', 'records;', 'records.', 'records, because'],
            'A',
            'Vế 1 là 1 IC hoàn chỉnh giới thiệu rõ một danh sách 3 mục ("Every Antarctic ice core preserves three vital climate records"). Vế 2 là chính danh sách 3 cụm danh từ đó (KHÔNG phải IC!). Sau IC + Danh sách giải thích → dùng dấu hai chấm (`:`) = A!',
            'IC hoàn chỉnh + danh sách liệt kê cụ thể (không có động từ chia thì) → Dấu hai chấm (`:`)!',
            [
                ('Đáp án đúng', 'Dấu hai chấm (:) sau IC giới thiệu chuẩn xác danh sách 3 loại dữ liệu khí hậu.'),
                ('Semicolon + Fragment', 'Phần sau là danh sách cụm danh từ, không phải IC → cấm dùng chấm phẩy.'),
                ('Period + Fragment', 'Tách danh sách cụm danh từ thành câu độc lập tạo Sentence Fragment.'),
                ('Fragment / Illogical', '"because" đòi hỏi một mệnh đề đầy đủ có động từ chia thì theo sau.'),
            ]
        ),

        # --- Q20-Q22: Standard English Conventions — Form, Structure, and Sense (Easy / Medium) ---
        q_item(
            'm5_m2l_q20', 20, 'Standard English Conventions', 'Form, Structure, and Sense', 'Easy',
            '<p>A thin layer of solar-reflective white paint applied across flat commercial rooftops ______ midday surface temperatures by up to 20°C during July heat waves.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['lower', 'lowers', 'have lowered', 'lowering'],
            'B',
            'Gạch bỏ cụm giới từ và phân từ chen giữa: "A thin <b>layer</b> <s>[of solar-reflective white paint applied across flat commercial rooftops]</s>". Chủ ngữ thật là "A thin layer" (SỐ ÍT!), câu chưa có động từ chia thì → Chọn `lowers` (B)!',
            'Mẹo 3–1: A và C đều là số nhiều, D là V-ing (Fragment), chỉ duy nhất B (`lowers`) là động từ chia thì số ít khớp "A thin layer"!',
            [
                ('Subject-Verb Mismatch', 'lower là động từ số nhiều — bị đánh lừa bởi danh từ số nhiều gần nhất "rooftops".'),
                ('Đáp án đúng', 'lowers (số ít, hiện tại đơn) khớp chuẩn với chủ ngữ số ít "A thin layer".'),
                ('Subject-Verb Mismatch', 'have lowered là số nhiều.'),
                ('Non-Finite Fragment', 'lowering là V-ing khiến câu không có động từ chính.'),
            ]
        ),
        q_item(
            'm5_m2l_q21', 21, 'Standard English Conventions', 'Form, Structure, and Sense', 'Easy',
            '<p>Centuries before European ships entered the Pacific Ocean, Polynesian navigators mastered star-path wayfinding and ______ thriving island communities across Hawaiʻi, Rapa Nui, and Aotearoa.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['establish', 'will establish', 'established', 'establishing'],
            'C',
            'Kiểm tra tính song song & thì quá khứ: Mốc thời gian quá khứ rõ ràng ("Centuries before European ships entered...") + động từ đứng ngay trước `and` là quá khứ đơn `mastered` → Động từ song song sau `and` BẮT BUỘC chia quá khứ đơn **`established`** (C)!',
            'Cặp động từ song song nối bằng `and` cùng chung chủ ngữ quá khứ: `mastered ... and established ...`!',
            [
                ('Tense Mismatch', 'establish chia hiện tại đơn, lệch với mốc lịch sử "Centuries before..." và động từ "mastered".'),
                ('Tense Mismatch', 'will establish chia tương lai, vô lý với sự kiện lịch sử hàng thế kỷ trước.'),
                ('Đáp án đúng', 'established (quá khứ đơn) song song hoàn hảo với "mastered" trong bối cảnh lịch sử.'),
                ('Parallelism Error', 'establishing (V-ing) phá vỡ cấu trúc song song với động từ chia thì "mastered".'),
            ]
        ),
        q_item(
            'm5_m2l_q22', 22, 'Standard English Conventions', 'Form, Structure, and Sense', 'Medium',
            '<p>Unlike earlier Romantic tales set inside brooding mountain castles, William Dean Howells’s realist fiction drew ______ quiet drama from ordinary family conversations and everyday workplace choices.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['their', 'it’s', 'they’re', 'its'],
            'D',
            'Kiểm tra Đại từ sở hữu (Pronoun Agreement & Apostrophe): Chủ ngữ thực hiện hành động "drew" là "William Dean Howells’s realist <b>fiction</b>" (danh từ KHÔNG ĐẾM ĐƯỢC / SỐ ÍT!). Cần tính từ sở hữu số ít ("của nó") → **`its`** (KHÔNG có dấu nháy đơn!) = D! Lưu ý `it’s` là viết tắt của "it is", còn `their` là số nhiều!',
            'Phân biệt dứt điểm: `its` = sở hữu số ít ("của nó"); `it’s` = "it is / it has"; `their` = số nhiều ("của họ/chúng")!',
            [
                ('Pronoun Number Mismatch', 'their là số nhiều, không khớp với danh từ không đếm được số ít "realist fiction".'),
                ('Contraction Trap', 'it’s nghĩa là "it is" — lắp vào câu thành "drew it is quiet drama" hoàn toàn sai ngữ pháp.'),
                ('Contraction & Number Trap', 'they’re nghĩa là "they are" — sai cả số lẫn dạng sở hữu.'),
                ('Đáp án đúng', 'its (tính từ sở hữu số ít, không dấu nháy) khớp chuẩn xác với "realist fiction".'),
            ]
        ),

        # --- Q23-Q25: Expression of Ideas — Transitions (Easy / Medium) ---
        q_item(
            'm5_m2l_q23', 23, 'Expression of Ideas', 'Transitions', 'Easy',
            '<p>Giant hydrothermal vent tube worms have no mouths, stomachs, or digestive tracts to swallow food from the ocean floor. ______, they depend entirely on internal symbiotic bacteria to synthesize nutrients from volcanic vent chemicals.</p>',
            'Which choice completes the text with the most logical transition?',
            ['However', 'For instance', 'Therefore', 'Previously'],
            'C',
            'Câu 1 (Nguyên nhân): Giun ống khổng lồ không có miệng, dạ dày hay hệ tiêu hóa để nuốt thức ăn. Câu 2 (Hệ quả): Vì thế chúng phụ thuộc hoàn toàn vào vi khuẩn cộng sinh bên trong cơ thể tạo chất dinh dưỡng → Quan hệ Nhân – Quả → **`Therefore`** (C)!',
            'Không có hệ tiêu hóa (nguyên nhân) → phụ thuộc hoàn toàn vào vi khuẩn bên trong (kết quả) = `Therefore`!',
            [
                ('False Contrast', 'However chỉ sự trái ngược, sai vì câu 2 là hệ quả tự nhiên của việc không có hệ tiêu hóa.'),
                ('Wrong Relationship (Example)', 'Câu 2 không phải ví dụ con của việc không có miệng/dạ dày.'),
                ('Đáp án đúng', 'Therefore nối chính xác nguyên nhân thiếu hệ tiêu hóa với hệ quả sống nhờ vi khuẩn cộng sinh.'),
                ('Wrong Relationship (Time)', 'Previously chỉ thời gian trước đó — sai logic.'),
            ]
        ),
        q_item(
            'm5_m2l_q24', 24, 'Expression of Ideas', 'Transitions', 'Easy',
            '<p>Renaissance Venetian pocket books were light enough for traveling students to slip easily into a saddlebag. ______, their slender italic type allowed printers to fit far more words onto each page, cutting the retail cost of every volume.</p>',
            'Which choice completes the text with the most logical transition?',
            ['Moreover', 'However', 'Instead', 'Regardless'],
            'A',
            'Câu 1 nêu ƯU ĐIỂM 1 (nhẹ, dễ bỏ túi yên ngựa). Câu 2 bổ sung ƯU ĐIỂM 2 cùng chiều (chữ nghiêng mảnh xếp được nhiều chữ hơn trên trang giúp giảm giá bán) → Bổ sung thêm lợi thế cùng hướng → **`Moreover`** (A)!',
            'Hai câu liên tiếp nêu hai lợi ích tích cực bổ trợ nhau (nhẹ dễ mang + giá bán rẻ hơn) → chọn từ nối bổ sung (`Moreover`)!',
            [
                ('Đáp án đúng', 'Moreover bổ sung chính xác ưu điểm thứ hai về tiết kiệm trang giấy và giá bán nối tiếp ưu điểm gọn nhẹ.'),
                ('False Contrast', 'Hai câu cùng khen ưu điểm của sách bỏ túi Venice, không hề mâu thuẫn.'),
                ('Wrong Relationship (Replacement)', 'Không có vế phủ định nào ở câu 1 để dùng "Instead".'),
                ('False Contrast', 'Regardless mang sắc thái "bất chấp điều đó", sai hướng bổ sung cùng chiều.'),
            ]
        ),
        q_item(
            'm5_m2l_q25', 25, 'Expression of Ideas', 'Transitions', 'Medium',
            '<p>Freshly painted reflective road coatings immediately lower midday asphalt temperatures across sunny Phoenix neighborhoods. ______, heavy daily traffic gradually deposits dark tire rubber and dust over the bright sealant, steadily weakening its cooling power over time.</p>',
            'Which choice completes the text with the most logical transition?',
            ['Similarly', 'However', 'Consequently', 'For example'],
            'B',
            'Câu 1 (Tích cực): Sơn phản quang mới quét làm mát mặt nhựa đường ngay lập tức. Câu 2 (Tiêu cực / Đối lập): Lưu lượng xe dày đặc bám dần cao su lốp đen và bụi làm suy yếu dần khả năng làm mát → Đảo chiều trực tiếp → **`However`** (B)!',
            'Từ hiệu quả làm mát tức thì (Câu 1) sang tác động làm suy giảm hiệu quả đó theo thời gian (Câu 2) → chọn `However`!',
            [
                ('False Similarity', 'Similarly chỉ sự tương đồng, trái ngược với hướng suy yếu hiệu quả làm mát.'),
                ('Đáp án đúng', 'However chuyển hướng chính xác từ lợi ích ban đầu sang hạn chế mòn bụi do giao thông.'),
                ('Wrong Relationship (Cause-Effect)', 'Lưu lượng xe bám bụi không phải kết quả do việc làm mát mặt đường gây ra.'),
                ('Wrong Relationship (Example)', 'Sự suy giảm hiệu quả không phải ví dụ minh họa cho việc làm mát ngay lập tức.'),
            ]
        ),

        # --- Q26-Q27: Expression of Ideas — Rhetorical Synthesis (Easy / Medium) ---
        q_item(
            'm5_m2l_q26', 26, 'Expression of Ideas', 'Rhetorical Synthesis', 'Easy',
            '''<p>While researching coral reef acoustics, a student has taken the following notes:</p>
            <ul>
              <li>Snapping shrimp belong to the marine family Alpheidae and live abundantly inside tropical coral reefs.</li>
              <li>Each shrimp possesses one oversized snapper claw that closes at extremely high speed.</li>
              <li>Closing the claw launches a fast jet of water that creates a microscopic cavitation bubble.</li>
              <li>When that bubble collapses an instant later, it releases a sharp pop reaching up to 200 decibels—loud enough to stun nearby prey.</li>
            </ul>''',
            'The student wants to explain how a snapping shrimp produces its loud underwater sound. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
            [
                'Snapping shrimp belong to the marine family Alpheidae and live abundantly across tropical coral reefs.',
                'A snapping shrimp’s underwater pop can reach up to 200 decibels, making it loud enough to stun nearby prey.',
                'Each snapping shrimp living inside a tropical coral reef possesses one oversized snapper claw.',
                'By snapping its oversized claw shut at high speed, a snapping shrimp shoots a water jet that forms a tiny cavitation bubble, whose sudden collapse creates a sharp 200-decibel pop.'
            ],
            'D',
            'Goal-First SOP: Giải thích CÁCH THỨC (HOW) tôm gõ mõ tạo ra âm thanh lớn dưới nước. A chỉ nêu tên họ và nơi sống; B chỉ nêu âm lượng 200 dB mà không giải thích cách tạo ra; C chỉ nêu có một chiếc càng lớn. Duy nhất D mô tả đủ chuỗi cơ chế: kẹp càng cực nhanh → bắn tia nước tạo bọt khí cavitation → bọt vỡ tung tạo tiếng nổ 200 dB! Chọn D!',
            'Tìm đúng đáp án giải quyết chữ "how" trong Goal bằng đầy đủ trình tự nguyên nhân – cơ chế!',
            [
                ('Wrong Synthesis Goal', 'Chỉ giới thiệu tên họ khoa học và môi trường sống.'),
                ('Missing Mechanism (How)', 'Chỉ nêu kết quả 200 dB và công dụng làm choáng mồi, không giải thích cách tạo tiếng nổ.'),
                ('Incomplete Detail', 'Chỉ nhắc việc có một chiếc càng to mà thiếu cơ chế tia nước và nổ bọt khí.'),
                ('Đáp án đúng', 'Trình bày mạch lạc toàn bộ cơ chế tạo tiếng nổ 200 dB của tôm gõ mõ.'),
            ]
        ),
        q_item(
            'm5_m2l_q27', 27, 'Expression of Ideas', 'Rhetorical Synthesis', 'Medium',
            '''<p>While researching Indigenous Pacific navigation, a student has taken the following notes:</p>
            <ul>
              <li>The traditional Hawaiian star compass is a mental navigation system rather than a physical magnetic instrument.</li>
              <li>Wayfinders divide the full 360-degree horizon into 32 named directional “houses” (<i>hale</i>).</li>
              <li>By memorizing which horizon houses over 150 bright stars rise from and set into each night, navigators maintain accurate headings across thousands of miles of open Pacific Ocean.</li>
              <li>Modern Polynesian voyaging crews still teach the star compass to steer double-hulled canoes without electronic GPS.</li>
            </ul>''',
            'The student wants to introduce the Hawaiian star compass and explain how navigators use it to steer across the open ocean. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
            [
                'Modern Polynesian crews continue to sail double-hulled canoes across the Pacific Ocean without relying on electronic GPS.',
                'The Hawaiian star compass divides the full 360-degree horizon into 32 separate directional houses known as <i>hale</i>.',
                'A mental navigation system rather than a magnetic instrument, the Hawaiian star compass divides the horizon into 32 directional houses (<i>hale</i>) so wayfinders can steer accurately across the open Pacific by tracking where bright stars rise and set.',
                'In Hawaiian wayfinding, each of the 32 named directional sections along the horizon is called a <i>hale</i>.'
            ],
            'C',
            'Goal-First SOP: Đạt đủ 2 vế: [1] Giới thiệu la bàn sao Hawaii là gì (a mental navigation system rather than a magnetic instrument) + [2] Giải thích CÁCH hoa tiêu dùng nó để lái xuồng vượt đại dương (chia đường chân trời thành 32 "ngôi nhà" phương hướng *hale* và theo dõi điểm mọc/lặn của các ngôi sao sáng). A bỏ qua cả định nghĩa lẫn cách hoạt động; B chỉ nói chia 32 ô mà không nói dùng sao mọc/lặn để lái xuồng; D chỉ giải thích từ *hale*. Duy nhất C hoàn thành gọn gàng cả hai yêu cầu! Chọn C!',
            'Kiểm tra đủ 2 yêu cầu song song trong Goal: `introduce what it is` + `explain how navigators use it to steer`!',
            [
                ('Wrong Synthesis Goal', 'Chỉ nhắc các đoàn xuồng hiện đại không dùng GPS, bỏ qua bản thân la bàn sao và cách dùng.'),
                ('Missing How-To-Steer', 'Chỉ nêu việc chia 32 ô chân trời mà chưa giải thích cách theo dõi sao mọc/lặn để giữ hướng đi.'),
                ('Đáp án đúng', 'Giới thiệu rõ bản chất hệ thống định hướng tư duy và giải thích đầy đủ cách dùng 32 ô chân trời + sao mọc/lặn để lái xuồng.'),
                ('Too Narrow', 'Chỉ định nghĩa thuật ngữ tiếng Hawaii "hale".'),
            ]
        ),
    ]
