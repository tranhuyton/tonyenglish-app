# -*- coding: utf-8 -*-
"""
Hand-crafted 1500+ Elite Digital SAT R&W Skill Drills:
- Drill 4.1: Words in Context I — Context Clues & Secondary Meanings (14 Qs)
- Drill 4.2: Words in Context II — 750+ Elite Lexicon & Nuance Traps (14 Qs)
"""

from sat_drills_1_1_and_2_1 import q_item

STEM_WIC = 'Which choice completes the text with the most logical and precise word or phrase?'

def get_drill_4_1():
    questions = [
        q_item(
            'd4_1_q1', 1, 'Craft and Structure', 'Words in Context', 'Medium',
            '<p>Although early reviewers dismissed the composer’s minimalist chamber piece as ______—claiming its repeated three-note motifs lacked imagination—subsequent musicologists praised its hypnotic harmonic discipline.</p>',
            STEM_WIC,
            ['pedestrian', 'exuberant', 'incendiary', 'lucrative'],
            'A',
            'Mirror Clue ngay sau dấu gạch ngang: "claiming its repeated three-note motifs lacked imagination" (thiếu trí tưởng tượng, đơn điệu). Nghĩa thứ cấp học thuật của "pedestrian" là "tầm thường, tẻ nhạt, thiếu sáng tạo" → khớp 100%!',
            'Nhớ nghĩa thứ cấp kinh điển trên SAT: pedestrian (adj) = dull / unimaginative (tẻ nhạt, tầm thường), KHÔNG phải "người đi bộ"!',
            [
                ('Đáp án đúng', 'pedestrian (nghĩa học thuật: tầm thường, thiếu sáng tạo) khớp tuyệt đối với manh mối "lacked imagination".'),
                ('Opposite Tone', 'exuberant = tràn đầy năng lượng phấn khởi — trái với lời chê đơn điệu.'),
                ('Wrong Meaning', 'incendiary = kích động, gây tranh cãi dữ dội — không khớp "repeated motifs lacked imagination".'),
                ('Wrong Context', 'lucrative = sinh lời cao về tài chính — sai ngữ cảnh thẩm mỹ âm nhạc.'),
            ]
        ),
        q_item(
            'd4_1_q2', 2, 'Craft and Structure', 'Words in Context', 'Hard',
            '<p>Because migratory monarchs adjust their flight trajectories within minutes whenever wind shear shifts across the Great Lakes, behavioral ecologists characterize the butterflies’ navigational instinct as remarkably ______ rather than rigidly programmed.</p>',
            STEM_WIC,
            ['erratic', 'plastic', 'dormant', 'obsolete'],
            'B',
            'Contrast Clue cực sắc: "______ rather than rigidly programmed" (trái ngược với bị lập trình cứng nhắc) + "adjust their flight trajectories within minutes". Nghĩa thứ cấp học thuật của "plastic" trong sinh học là "linh hoạt, dễ uốn nắn/thích nghi" (như neural plasticity, behavioral plasticity) → Chọn B!',
            'Trong các bài sinh học/thần kinh học Digital SAT, "plastic" = flexible / adaptable (linh hoạt thích nghi), KHÔNG phải "bằng nhựa"!',
            [
                ('Negative Tone Trap', 'erratic = thất thường hỗn loạn (tiêu cực) — trái với sự điều chỉnh có mục đích chuẩn xác của bướm.'),
                ('Đáp án đúng', 'plastic (nghĩa khoa học: linh hoạt, dễ thích nghi) đối lập hoàn hảo với "rigidly programmed".'),
                ('Wrong Meaning', 'dormant = ngủ đông, tạm ngừng hoạt động — ngược với hành vi điều chỉnh liên tục.'),
                ('Wrong Meaning', 'obsolete = lỗi thời — sai ngữ cảnh tiến hóa sinh học.'),
            ]
        ),
        q_item(
            'd4_1_q3', 3, 'Craft and Structure', 'Words in Context', 'Hard',
            '<p>While the museum’s new audio guide has received ______ acclaim from visiting curators—who applaud its archival recordings yet note that its pacing rushes through the Renaissance sculpture galleries—general visitors have rated it overwhelmingly favorably.</p>',
            STEM_WIC,
            ['unanimous', 'unbridled', 'qualified', 'scathing'],
            'C',
            'Mirror Clue trong cặp gạch ngang: "who applaud its archival recordings YET note that its pacing rushes..." (vừa khen phần thu âm NHƯNG lại chê tốc độ vội vã) → lời khen CÓ ĐIỀU KIỆN / CHỪNG MỰC → "qualified acclaim" (C)!',
            'Cặp đối lập vàng: qualified praise/acclaim = khen có điều kiện; unqualified/unbridled praise = khen tuyệt đối không chút chê!',
            [
                ('Too Extreme / Contradiction', 'unanimous = nhất trí 100% — mâu thuẫn với lời phê bình phần tốc độ ở cụm gạch ngang.'),
                ('Too Extreme', 'unbridled = không kiềm chế, nhiệt liệt tuyệt đối — sai vì có lời chê đi kèm.'),
                ('Đáp án đúng', 'qualified (nghĩa thứ cấp: có giới hạn/điều kiện) khớp hoàn hảo với vế "applaud... yet note...".'),
                ('Too Extreme (Negative)', 'scathing = chỉ trích gay gắt — mâu thuẫn với từ "acclaim" (sự tán dương) và "applaud".'),
            ]
        ),
        q_item(
            'd4_1_q4', 4, 'Craft and Structure', 'Words in Context', 'Hard',
            '<p>In the early twentieth century, physicist Alfred Wegener’s theory of continental drift failed to gain wide ______ among geologists, most of whom rejected the idea until seafloor-spreading data confirmed it fifty years later.</p>',
            STEM_WIC,
            ['solitude', 'friction', 'antiquity', 'currency'],
            'D',
            'Mirror Clue: "failed to gain wide ______ among geologists, most of whom rejected the idea" → thuyết không giành được SỰ CHẤP NHẬN / ĐỘ PHỔ BIẾN RỘNG RÃI → Nghĩa thứ cấp kinh điển: "gain currency" = trở nên phổ biến, được giới học thuật chấp nhận rộng rãi → Chọn D!',
            'Thuộc lòng collocation Digital SAT: "gain currency" / "have currency" = trở nên thịnh hành, được chấp nhận rộng rãi!',
            [
                ('Wrong Meaning', 'solitude = sự cô đơn — sai hoàn toàn ngữ cảnh học thuyết khoa học.'),
                ('Opposite Logic', 'Học thuyết gây ra nhiều tranh cãi chứ không "thất bại trong việc tạo ma sát".'),
                ('Wrong Meaning', 'antiquity = thời cổ đại — không ghép với "gain wide...".'),
                ('Đáp án đúng', 'currency (nghĩa học thuật: sự phổ biến, mức độ chấp nhận chung) khớp trọn cụm "gain wide currency".'),
            ]
        ),
        q_item(
            'd4_1_q5', 5, 'Craft and Structure', 'Words in Context', 'Hard',
            '<p>After inspecting the bridge’s corroded suspension cables, structural auditors judged the municipal maintenance protocol severely ______: crucial rust-prevention coatings had not been reapplied for nearly two decades.</p>',
            STEM_WIC,
            ['wanting', 'prolific', 'redundant', 'impartial'],
            'A',
            'Colon Clue: "crucial rust-prevention coatings had not been reapplied for nearly two decades" → quy trình bảo trì THIẾU SÓT NGHIÊM TRỌNG / CHƯA ĐẠT CHUẨN → Nghĩa thứ cấp học thuật của "wanting" = deficient / inadequate ("judged severely wanting") → Chọn A!',
            'Nhớ cụm học thuật kinh điển: "found wanting" / "severely wanting" = bị đánh giá thiếu sót, yếu kém không đạt yêu cầu!',
            [
                ('Đáp án đúng', 'wanting (nghĩa thứ cấp: thiếu sót, không đạt chuẩn) khớp hoàn toàn với việc 20 năm không sơn chống gỉ.'),
                ('Opposite Tone', 'prolific = sung mãn, tạo ra nhiều sản phẩm — trái ngược sự thiếu hụt bảo trì.'),
                ('Wrong Meaning', 'redundant = dư thừa không cần thiết — trái ngược với việc thiếu hẳn lớp phủ bảo vệ.'),
                ('Wrong Meaning', 'impartial = công tâm, không thiên vị — không dùng mô tả quy trình bảo trì cầu.'),
            ]
        ),
        q_item(
            'd4_1_q6', 6, 'Craft and Structure', 'Words in Context', 'Hard',
            '<p>During the 1930s Dust Bowl, federal soil conservationists planted dense windbreaks of native shrubs across Great Plains farmland to ______ severe topsoil erosion driven by relentless prairie winds.</p>',
            STEM_WIC,
            ['foment', 'check', 'compound', 'mimic'],
            'B',
            'Cause-Effect Clue: trồng hàng cây chắn gió (windbreaks) nhằm NGĂN CHẶN / KIỀM CHẾ nạn xói mòn tầng đất mặt → Nghĩa thứ cấp của động từ "check" = restrain / halt (kiềm chế, chặn đứng)! Chọn B!',
            'Gặp động từ "check" trước một hiện tượng xấu ("check erosion", "check inflation", "check the spread") → nghĩa là KIỀM CHẾ / NGĂN CHẶN!',
            [
                ('Opposite Meaning', 'foment = kích động, thổi bùng — ngược hoàn toàn mục tiêu bảo tồn đất.'),
                ('Đáp án đúng', 'check (động từ nghĩa thứ cấp: kiềm chế, chặn lại) khớp chuẩn xác mục đích trồng cây chắn gió.'),
                ('Opposite Meaning', 'compound = làm trầm trọng thêm — ngược mục tiêu chống xói mòn.'),
                ('Wrong Meaning', 'mimic = bắt chước — vô nghĩa trong ngữ cảnh chống xói mòn.'),
            ]
        ),
        q_item(
            'd4_1_q7', 7, 'Craft and Structure', 'Words in Context', 'Medium',
            '<p>Known for her ______ curation style, gallery director Nadia Khoury routinely pairs seventeenth-century Dutch still lifes alongside contemporary West African recycled-metal sculptures in the same exhibition hall.</p>',
            STEM_WIC,
            ['monolithic', 'insular', 'eclectic', 'austere'],
            'C',
            'Example Clue: kết hợp tranh tĩnh vật Hà Lan thế kỷ 17 đặt cạnh điêu khắc kim loại tái chế Tây Phi đương đại → phong cách ĐA DẠNG, PHA TRỘN TỪ NHIỀU NGUỒN → "eclectic" (C)!',
            'Hễ thấy đoạn văn liệt kê sự kết hợp từ nhiều nền văn hóa/thời đại/thể loại khác nhau → 99% là "eclectic"!',
            [
                ('Opposite Meaning', 'monolithic = đồng nhất nguyên khối, cứng nhắc — ngược với việc pha trộn nhiều trường phái.'),
                ('Opposite Meaning', 'insular = khép kín, cô lập — trái với việc kết nối nghệ thuật châu Âu và Tây Phi.'),
                ('Đáp án đúng', 'eclectic = chiết trung, tuyển chọn đa dạng từ nhiều nguồn khác nhau.'),
                ('Wrong Meaning', 'austere = khắc khổ, tối giản nghiêm nghị — không phản ánh sự kết hợp đa nguồn.'),
            ]
        ),
        q_item(
            'd4_1_q8', 8, 'Craft and Structure', 'Words in Context', 'Elite (750+)',
            '<p>Although physicist Lise Meitner’s theoretical calculations were indispensable to explaining nuclear fission, wartime political exile largely ______ her contributions from contemporary public recognition for decades.</p>',
            STEM_WIC,
            ['amplified', 'solicited', 'validated', 'obscured'],
            'D',
            'Contrast Clue: "Although... indispensable" (tuy cực kỳ thiết yếu) đối lập với việc lưu vong thời chiến đã CHE KHUẤT / LÀM MỜ đóng góp của bà khỏi sự ghi nhận của công chúng trong nhiều thập kỷ → "obscured" (D)!',
            'Cấu trúc "obscure X from Y" = che khuất/làm lu mờ X khỏi tầm nhìn hay sự công nhận của Y.',
            [
                ('Opposite Meaning', 'amplified = khuếch đại, phóng đại — trái ngược với vế đối lập "Although indispensable".'),
                ('Wrong Meaning', 'solicited = kêu gọi, xin — không phù hợp với chủ ngữ "political exile".'),
                ('Opposite Meaning', 'validated = xác thực, khẳng định giá trị — ngược với bối cảnh bị lãng quên.'),
                ('Đáp án đúng', 'obscured = che lấp, làm lu mờ — khớp trọn vẹn với sự tương phản "Although indispensable".'),
            ]
        ),
        q_item(
            'd4_1_q9', 9, 'Craft and Structure', 'Words in Context', 'Hard',
            '<p>Because desert ephemeral streams flow for only a few hours after rare cloudbursts, hydrologists consider the resulting blooms of annual wildflowers remarkably ______, vanishing almost as quickly as they appear.</p>',
            STEM_WIC,
            ['fleeting', 'perennial', 'arduous', 'ubiquitous'],
            'A',
            'Restatement Clue ngay sau dấu phẩy: "vanishing almost as quickly as they appear" (biến mất nhanh gần bằng lúc xuất hiện) → NGẮN NGỦI, THOÁNG QUA → "fleeting" (A)!',
            'Cụm "vanishing as quickly as they appear" là dấu hiệu định nghĩa thẳng của nhóm từ: fleeting / ephemeral / transient.',
            [
                ('Đáp án đúng', 'fleeting = thoáng qua, ngắn ngủi — khớp từng chữ với "vanishing almost as quickly as they appear".'),
                ('Opposite Meaning', 'perennial = lâu năm, kéo dài bền bỉ — trái nghĩa trực tiếp.'),
                ('Wrong Meaning', 'arduous = gian khổ, vất vả — không dùng mô tả độ dài tồn tại của hoa dại.'),
                ('Wrong Meaning', 'ubiquitous = có mặt khắp nơi — sai với bối cảnh suối sa mạc hiếm gặp.'),
            ]
        ),
        q_item(
            'd4_1_q10', 10, 'Craft and Structure', 'Words in Context', 'Elite (750+)',
            '<p>Far from being ______ to the economic anxieties of rural tenant farmers, the nineteenth-century novelist filled her notebooks with detailed interviews documenting falling wheat prices and rising land rents.</p>',
            STEM_WIC,
            ['sympathetic', 'indifferent', 'vital', 'attuned'],
            'B',
            'Contrast Clue cực gắt: "<b>Far from being</b> ______ to the economic anxieties..." ("Khác xa với việc [X] trước nỗi lo của nông dân, nữ tiểu thuyết gia ghi chép chi tiết các cuộc phỏng vấn..."). Vì "Far from being X" = KHÔNG HỀ X → X phải mang nghĩa THỜ Ơ / LÃNH ĐẠM → "indifferent" (B)! Cẩn thận bẫy A & D: học viên đọc nhanh quên chữ "Far from" sẽ chọn nhầm "sympathetic" hay "attuned"!',
            'Cảnh giác tuyệt đối với mở đầu "Far from being ___": nó đảo ngược 180 độ dấu điện tích! Tìm từ TRÁI NGHĨA với hành động ở vế sau!',
            [
                ('Polarity Flip Trap!', 'Quên chữ "Far from being"! Nếu điền "sympathetic" sẽ thành "Không hề cảm thông" — trái ngược với việc bà tận tâm phỏng vấn nông dân.'),
                ('Đáp án đúng', '"Far from being indifferent" = Không hề thờ ơ — khớp tuyệt đối với việc ghi chép phỏng vấn tỉ mỉ.'),
                ('Polarity Flip Trap!', 'vital to = thiết yếu — không hợp nghĩa "Far from being vital".'),
                ('Polarity Flip Trap!', 'attuned to = thấu hiểu/đồng điệu — ngược cực khi đi với "Far from being".'),
            ]
        ),
        q_item(
            'd4_1_q11', 11, 'Craft and Structure', 'Words in Context', 'Elite (750+)',
            '<p>Upon entering the newly restored basilica, visitors are immediately struck by an ______ optical illusion: a flat plaster dome painted with precise architectural perspective so convincing that it appears to soar thirty meters overhead.</p>',
            STEM_WIC,
            ['indistinct', 'unassuming', 'arresting', 'apathetic'],
            'C',
            'Mirror Clue: "visitors are immediately struck by..." + "so convincing that it appears to soar thirty meters overhead" → GÂY ẤN TƯỢNG MẠNH, THU HÚT NGAY ÁNH NHÌN → Nghĩa thứ cấp của "arresting" = striking / captivating (cuốn hút, nổi bật khó rời mắt) → Chọn C!',
            'Nhớ nghĩa thứ cấp học thuật: arresting (adj) = strikingly captivating (cuốn hút, gây chú ý mạnh), không liên quan đến cảnh sát bắt giữ!',
            [
                ('Opposite Meaning', 'indistinct = mờ nhạt, không rõ nét — trái với "precise architectural perspective so convincing".'),
                ('Opposite Meaning', 'unassuming = khiêm tốn, không gây chú ý — trái với "immediately struck by".'),
                ('Đáp án đúng', 'arresting (nghĩa thứ cấp: đầy ấn tượng, thu hút mạnh sự chú ý) khớp tuyệt đối với "immediately struck".'),
                ('Wrong Subject', 'apathetic = thờ ơ vô cảm — chỉ dùng cho cảm xúc con người, không mô tả ảo giác quang học.'),
            ]
        ),
        q_item(
            'd4_1_q12', 12, 'Craft and Structure', 'Words in Context', 'Hard',
            '<p>By 1915, inexpensive mass-produced electric streetcars had largely ______ horse-drawn omnibuses across major American cities, rendering equine urban transit virtually extinct within a single generation.</p>',
            STEM_WIC,
            ['preserved', 'resembled', 'endorsed', 'eclipsed'],
            'D',
            'Mirror Clue: "rendering equine urban transit virtually extinct within a single generation" → xe điện đã VƯỢT TRỘI, LÀM LU MỜ / THAY THẾ HOÀN TOÀN xe ngựa kéo → Nghĩa thứ cấp của "eclipse" (v) = surpass / overshadow → Chọn D!',
            'Động từ "eclipse" trên SAT mang nghĩa "vượt xa, làm lu mờ, đẩy lùi đối thủ cũ".',
            [
                ('Opposite Meaning', 'preserved = bảo tồn — trái ngược hoàn toàn với "virtually extinct".'),
                ('Wrong Meaning', 'resembled = giống với — không giải thích việc xe ngựa biến mất.'),
                ('Opposite Meaning', 'endorsed = ủng hộ — sai logic.'),
                ('Đáp án đúng', 'eclipsed (nghĩa thứ cấp: vượt trội hoàn toàn, làm lu mờ) khớp trọn với việc đẩy xe ngựa vào dĩ vãng.'),
            ]
        ),
        q_item(
            'd4_1_q13', 13, 'Craft and Structure', 'Words in Context', 'Hard',
            '<p>Although the medieval manuscript’s margins are crowded with playful sketches of mythical beasts, its central text remains strictly ______, offering dry administrative tallies of grain taxes and vineyard leases.</p>',
            STEM_WIC,
            ['prosaic', 'whimsical', 'cryptic', 'ornate'],
            'A',
            'Contrast + Restatement Clue: đối lập với "playful sketches of mythical beasts" (hình vẽ nghịch ngợm tưởng tượng) + giải thích ngay sau "offering dry administrative tallies" (bảng kê hành chính khô khan thực dụng) → "prosaic" (khô khan, thực tế, không bay bổng) = A!',
            'Nhớ cặp từ đối lập hay thi trong phê bình nghệ thuật/văn học: whimsical/fanciful (bay bổng) ↔ prosaic/matter-of-fact (khô khan thực dụng).',
            [
                ('Đáp án đúng', 'prosaic = khô khan, thực dụng, thiếu bay bổng — khớp từng chữ với "dry administrative tallies".'),
                ('Opposite Meaning', 'whimsical = bay bổng nghịch ngợm — đó là tính chất của hình vẽ bên lề, trái với văn bản chính.'),
                ('Wrong Meaning', 'cryptic = bí ẩn khó giải mã — đoạn văn nói "dry administrative tallies" chứ không nói khó hiểu.'),
                ('Opposite Meaning', 'ornate = cầu kỳ hoa mỹ — trái với "dry".'),
            ]
        ),
        q_item(
            'd4_1_q14', 14, 'Craft and Structure', 'Words in Context', 'Elite (750+)',
            '<p>While laboratory rats rapidly mastered the simplified T-maze, wild-caught voles placed in the exact same apparatus behaved far more ______, pausing repeatedly to inspect every corner before advancing toward the food reward.</p>',
            STEM_WIC,
            ['recklessly', 'tentatively', 'uniformly', 'boisterously'],
            'B',
            'Mirror Clue ngay sau dấu phẩy: "pausing repeatedly to inspect every corner before advancing" (dừng lại liên tục quan sát mọi góc trước khi tiến tới) → hành động THẬN TRỌNG, DÈ DẶT, NGẬP NGỪNG → "tentatively" (B)!',
            'Đọc mệnh đề phân từ ngay sau dấu phẩy (", pausing repeatedly to inspect...") — đó luôn là bản dịch định nghĩa trực tiếp của chỗ trống!',
            [
                ('Opposite Meaning', 'recklessly = liều lĩnh bất cẩn — trái ngược hoàn toàn với việc dừng lại kiểm tra từng góc.'),
                ('Đáp án đúng', 'tentatively = ngập ngừng, dè dặt thận trọng — khớp tuyệt đối với hành vi quan sát kỹ trước khi đi tiếp.'),
                ('Wrong Meaning', 'uniformly = đồng nhất như nhau — không nói về sự dè dặt.'),
                ('Wrong Meaning', 'boisterously = ồn ào náo nhiệt — sai ngữ cảnh thí nghiệm hành vi động vật.'),
            ]
        ),
    ]
    return {
        'schemaVersion': 1,
        'mode': 'drill',
        'section': 'Reading and Writing',
        'basicInfo': {
            'title': 'Drill 4.1: Words in Context I — Context Clues & Secondary Meanings (14 Qs)',
            'subtitle': 'Thực hành Predict-Before-Peek và làm chủ các từ mang nghĩa thứ cấp học thuật (pedestrian, plastic, qualified, currency, wanting, check, arresting, eclipse).',
            'difficultyBadge': 'C&S • Target 1500+',
            'targetTimeMinutes': 12,
        },
        'drillModule': {
            'id': 'drill_4_1_mod',
            'title': 'Skill Drill 4.1: Words in Context I (Secondary Meanings)',
            'timeLimitMinutes': 12,
            'questions': questions,
        },
    }


def get_drill_4_2():
    questions = [
        q_item(
            'd4_2_q1', 1, 'Craft and Structure', 'Words in Context', 'Elite (750+)',
            '<p>Because installing elevated wildlife overpasses across the Trans-Canada Highway cannot eliminate traffic volume altogether, ecologists designed the vegetated bridges to ______ animal-vehicle collisions rather than eradicate them completely.</p>',
            STEM_WIC,
            ['mitigate', 'preclude', 'instigate', 'obliterate'],
            'A',
            'Nuance Cluster 750+ (`mitigate` vs. `preclude` vs. `obliterate`)! Manh mối cực sắc: "______ animal-vehicle collisions RATHER THAN eradicate them completely" (KHÔNG xóa sổ 100% mà chỉ LÀM GIẢM NHẸ mức độ) → "mitigate" (A)! Loại B (preclude = ngăn chặn triệt để không cho xảy ra) và D (obliterate = xóa sổ hoàn toàn — đồng nghĩa với eradicate!).',
            'Nhớ thang độ mạnh: mitigate/ameliorate (giảm bớt) < preclude (ngăn chặn từ đầu) < eradicate/obliterate (xóa sổ 100%).',
            [
                ('Đáp án đúng', 'mitigate = làm giảm nhẹ mức độ nghiêm trọng — đối lập chính xác với "rather than eradicate them completely".'),
                ('Degree Too Strong', 'preclude = ngăn không cho xảy ra hoàn toàn — mâu thuẫn với vế "rather than eradicate them completely".'),
                ('Opposite Meaning', 'instigate = kích động, gây ra — ngược hoàn toàn mục đích bảo vệ động vật.'),
                ('Degree Too Strong', 'obliterate = xóa sổ hoàn toàn — trùng nghĩa với "eradicate" nên sai khi đi với "rather than".'),
            ]
        ),
        q_item(
            'd4_2_q2', 2, 'Craft and Structure', 'Words in Context', 'Elite (750+)',
            '<p>Independent ice-core sulfur measurements from Greenland ______ archival Icelandic chronicles describing a dense volcanic haze that lingered across northern Europe throughout the summer of 1783.</p>',
            STEM_WIC,
            ['repudiate', 'corroborate', 'circumvent', 'speculate'],
            'B',
            'Hai nguồn độc lập (mẫu lõi băng Greenland + biên niên sử Iceland) cùng chỉ về cùng 1 sự kiện mù núi lửa năm 1783 → CỦNG CỐ / CHỨNG THỰC BẰNG BẰNG CHỨNG ĐỘC LẬP → "corroborate" (B)! Loại D ("speculate" = suy đoán, không đi kèm trực tiếp tân ngữ là "chronicles" và bằng chứng thực nghiệm không "suy đoán").',
            'Gặp 2 nguồn độc lập cùng khớp nhau ("independent data ... archival chronicles") → từ chuẩn 100% của College Board là "corroborate" hoặc "substantiate"!',
            [
                ('Opposite Meaning', 'repudiate = bác bỏ — sai vì cả hai nguồn cùng ghi nhận hiện tượng mù núi lửa 1783.'),
                ('Đáp án đúng', 'corroborate = chứng thực, củng cố bằng chứng độc lập cho một ghi chép hay giả thuyết.'),
                ('Wrong Meaning', 'circumvent = đi vòng tránh/lách luật — không khớp với dữ liệu lõi băng.'),
                ('Collocation / Meaning Error', 'speculate = phỏng đoán (và là nội động từ "speculate about", không thể "speculate chronicles").'),
            ]
        ),
        q_item(
            'd4_2_q3', 3, 'Craft and Structure', 'Words in Context', 'Elite (750+)',
            '<p>Because the treaty’s clause on maritime fishing quotas was deliberately worded in ______ terms, diplomats from both nations returned home claiming that the exact same sentence supported their opposing interpretations.</p>',
            STEM_WIC,
            ['exhaustive', 'candid', 'equivocal', 'unambiguous'],
            'C',
            'Mirror Clue: "diplomats from both nations... claiming that the exact same sentence supported their opposing interpretations" (hai bên đối nghịch đều hiểu cùng 1 câu theo hướng có lợi cho mình) → ngôn từ NƯỚC ĐÔI, CỐ TÌNH MƠ HỒ → "equivocal" (C)!',
            'Gốc từ `equi-` (bằng nhau) + `voc` (tiếng nói) → equivocal = nói nước đôi, hiểu theo hai hướng đều được!',
            [
                ('Wrong Meaning', 'exhaustive = toàn diện cặn kẽ — không dẫn tới hai cách hiểu trái ngược.'),
                ('Opposite Meaning', 'candid = thẳng thắn bộc trực — trái ngược với câu chữ nước đôi.'),
                ('Đáp án đúng', 'equivocal = nước đôi, đa nghĩa gây mơ hồ — khớp tuyệt đối với việc cả hai phía diễn giải trái ngược nhau.'),
                ('Opposite Meaning', 'unambiguous = rõ ràng một nghĩa duy nhất — trái nghĩa hoàn toàn.'),
            ]
        ),
        q_item(
            'd4_2_q4', 4, 'Craft and Structure', 'Words in Context', 'Elite (750+)',
            '<p>Although historians initially suspected a link between the sudden abandonment of the hillside fort and an epidemic recorded a century earlier, radiocarbon testing showed that the chronological connection was at best ______.</p>',
            STEM_WIC,
            ['irrefutable', 'lucid', 'resilient', 'tenuous'],
            'D',
            'Contrast Clue: "Although historians initially suspected a link... an epidemic recorded A CENTURY EARLIER" (cách nhau cả thế kỷ!) → mối liên hệ thời gian cùng lắm chỉ MONG MANH, LỎNG LẺO → "tenuous" (D)!',
            'Collocation cực chuẩn SAT: "a tenuous link / connection / grasp" = mối liên hệ mong manh, yếu ớt thiếu thuyết phục.',
            [
                ('Opposite Meaning', 'irrefutable = không thể bác bỏ — trái ngược khoảng cách lệch nhau cả thế kỷ.'),
                ('Wrong Context', 'lucid = sáng sủa, mạch lạc — dùng cho văn phong/tư duy, không mô tả mối liên hệ yếu.'),
                ('Opposite Meaning', 'resilient = bền bỉ kiên cường — ngược nghĩa.'),
                ('Đáp án đúng', 'tenuous = mong manh, lỏng lẻo — khớp tuyệt đối với "at best" và độ lệch cả thế kỷ.'),
            ]
        ),
        q_item(
            'd4_2_q5', 5, 'Craft and Structure', 'Words in Context', 'Elite (750+)',
            '<p>To ______ the steep tariffs imposed on imported raw silk during the 1690s, regional textile merchants quietly shifted their shipments through smaller coastal ports governed by separate trade charters.</p>',
            STEM_WIC,
            ['circumvent', 'buttress', 'emulate', 'stipulate'],
            'A',
            'Gốc từ `circum-` (đi vòng quanh) + hành động lặng lẽ chuyển hàng qua các cảng nhỏ có quy chế riêng để TRÁNH / LÁCH mức thuế quan cao → "circumvent" (A)!',
            'Circumvent = lách qua, tìm đường vòng tránh một quy định, thuế quan hoặc trở ngại.',
            [
                ('Đáp án đúng', 'circumvent = đi vòng tránh, lách quy định thuế quan — khớp hoàn hảo với việc chuyển tuyến sang cảng nhỏ.'),
                ('Opposite Meaning', 'buttress = chống đỡ, củng cố — thương nhân không muốn củng cố mức thuế cao.'),
                ('Wrong Meaning', 'emulate = noi gương/bắt chước — sai nghĩa.'),
                ('Wrong Meaning', 'stipulate = quy định điều khoản — thương nhân đang né thuế chứ không ban hành điều khoản thuế.'),
            ]
        ),
        q_item(
            'd4_2_q6', 6, 'Craft and Structure', 'Words in Context', 'Elite (750+)',
            '<p>Unlike commercial pop recordings engineered to sound polished and uniform, field folklorist Alan Lomax prized ______ vocal timbres—preserving the unrepeatable phrasing, dialect quirks, and regional inflections unique to each rural singer.</p>',
            STEM_WIC,
            ['derivative', 'idiosyncratic', 'homogenous', 'formulaic'],
            'B',
            'Contrast + Restatement Clue: đối lập với "uniform" (đồng nhất) + giải thích sau gạch ngang "unrepeatable phrasing, dialect quirks, and regional inflections unique to each rural singer" → mang nét ĐẶC THÙ CÁ NHÂN RIÊNG BIỆT → "idiosyncratic" (B)! Mẹo 3–1: A (derivative = sao chép), C (homogenous = đồng nhất), D (formulaic = rập khuôn) đều thuộc phe "đồng nhất/bắt chước" → gạch cả 3!',
            'Nhận diện cặp đối lập vàng trong bài Nghệ thuật/Văn học SAT: uniform/formulaic/derivative ↔ idiosyncratic/singular!',
            [
                ('Opposite Meaning', 'derivative = bắt chước, thiếu nguyên bản — trái ngược "unrepeatable / unique".'),
                ('Đáp án đúng', 'idiosyncratic = mang nét đặc thù riêng biệt không trộn lẫn — khớp từng chữ với "quirks... unique to each singer".'),
                ('Opposite Meaning', 'homogenous = đồng nhất — đồng nghĩa với "uniform" ở vế đối lập "Unlike".'),
                ('Opposite Meaning', 'formulaic = rập khuôn công thức — trái ngược hoàn toàn.'),
            ]
        ),
        q_item(
            'd4_2_q7', 7, 'Craft and Structure', 'Words in Context', 'Elite (750+)',
            '<p>Because extreme atmospheric pressure on Venus crushes standard metallic hulls within two hours, existing probe designs ______ long-term surface missions until high-temperature silicon-carbide electronics mature.</p>',
            STEM_WIC,
            ['facilitate', 'ameliorate', 'preclude', 'substantiate'],
            'C',
            'Cause-Effect Clue: áp suất nghiền nát vỏ tàu chỉ trong 2 giờ → thiết kế tàu hiện tại NGĂN CẢN / LÀM KHÔNG THỂ THỰC HIỆN các sứ mệnh bề mặt dài hạn cho đến khi công nghệ mới chín muồi → "preclude" (C)!',
            'Preclude = loại trừ khả năng xảy ra, khiến việc gì trở nên bất khả thi.',
            [
                ('Opposite Meaning', 'facilitate = tạo điều kiện thuận lợi — ngược hoàn toàn với vỏ tàu bị nghiền nát sau 2 giờ.'),
                ('Collocation / Polarity Trap', 'ameliorate = cải thiện tình trạng xấu — sai cực và sai collocation.'),
                ('Đáp án đúng', 'preclude = ngăn cản, khiến không thể thực hiện được các sứ mệnh dài ngày.'),
                ('Wrong Meaning', 'substantiate = chứng minh bằng bằng chứng — không khớp với chủ ngữ "probe designs".'),
            ]
        ),
        q_item(
            'd4_2_q8', 8, 'Craft and Structure', 'Words in Context', 'Elite (750+)',
            '<p>In her 2023 synthesis of global glacier surveys, Dr. Lena Bergström pulled together ______ datasets—ranging from nineteenth-century mountaineer sketches to satellite radar altimetry—into a single coherent timeline of alpine ice loss.</p>',
            STEM_WIC,
            ['interchangeable', 'redundant', 'congruent', 'disparate'],
            'D',
            'Restatement + Contrast Clue: dữ liệu trải dài từ tranh phác họa của người leo núi thế kỷ 19 đến đo cao radar vệ tinh (cực kỳ KHÁC NHAU VỀ BẢN CHẤT) được gom thành "a single coherent timeline" → "disparate" (D)! Dùng Synonym Shortcut: A, B, C đều gợi ý giống nhau/trùng lặp → gạch sạch!',
            'Cặp tương phản kinh điển của bài Khoa học: "bring disparate sources/datasets into a single coherent framework"!',
            [
                ('Opposite Meaning', 'interchangeable = có thể thay thế ngang nhau — sai vì tranh vẽ tay và radar vệ tinh khác hẳn bản chất.'),
                ('Opposite Meaning', 'redundant = trùng lặp dư thừa.'),
                ('Opposite Meaning', 'congruent = trùng khớp đồng dạng.'),
                ('Đáp án đúng', 'disparate = hoàn toàn khác biệt về bản chất — khớp tuyệt đối với cặp ví dụ phác họa thế kỷ 19 và radar vệ tinh.'),
            ]
        ),
        q_item(
            'd4_2_q9', 9, 'Craft and Structure', 'Words in Context', 'Elite (750+)',
            '<p>Rather than delivering a ______ critique that dismissed every aspect of the urban renewal plan, committee chair David Chen offered targeted revisions aimed specifically at preserving neighborhood bus routes.</p>',
            STEM_WIC,
            ['sweeping', 'nuanced', 'measured', 'tentative'],
            'A',
            'Contrast + Restatement Clue: "Rather than delivering a ______ critique that dismissed EVERY aspect..., Chen offered TARGETED revisions" → đối lập với "targeted" (nhắm điểm cụ thể) và khớp với "dismissed every aspect" (bác bỏ sạch trơn mọi khía cạnh) → "sweeping" (toàn diện, vơ đũa cả nắm, bao quát rộng) = A!',
            'Cặp đối lập kinh điển: targeted / specific / nuanced (cụ thể, tinh tế) ↔ sweeping / blanket (vơ đũa cả nắm, đánh đồng toàn bộ).',
            [
                ('Đáp án đúng', 'sweeping = bao trùm toàn bộ, đánh đồng mọi khía cạnh — khớp hoàn hảo với "dismissed every aspect" và đối lập "targeted".'),
                ('Opposite Meaning', 'nuanced = tinh tế có sắc thái — đồng hướng với "targeted", sai sau "Rather than".'),
                ('Opposite Meaning', 'measured = chừng mực cân nhắc — trái với "dismissed every aspect".'),
                ('Wrong Meaning', 'tentative = dè dặt ngập ngừng — không khớp với sự bác bỏ toàn diện.'),
            ]
        ),
        q_item(
            'd4_2_q10', 10, 'Craft and Structure', 'Words in Context', 'Hard',
            '<p>Once restricted to specialized aerospace alloys, carbon-fiber composites have become so ______ in modern manufacturing that they now appear in everything from commuter bicycles to everyday tennis rackets.</p>',
            STEM_WIC,
            ['scarce', 'ubiquitous', 'arcane', 'ephemeral'],
            'B',
            'Contrast + Example Clue: "Once restricted to specialized aerospace..." (trước kia chỉ giới hạn ở hàng không) → giờ xuất hiện trong MỌI THỨ từ xe đạp đi làm đến vợt tennis → CÓ MẶT KHẮP NƠI → "ubiquitous" (B)!',
            'Once restricted/rare → now appear in everything = tín hiệu 100% của "ubiquitous" / "pervasive"!',
            [
                ('Opposite Meaning', 'scarce = khan hiếm — ngược với "appear in everything".'),
                ('Đáp án đúng', 'ubiquitous = phổ biến khắp mọi nơi — đối lập hoàn toàn với "Once restricted".'),
                ('Wrong Meaning', 'arcane = bí truyền, chỉ chuyên gia hiểu — ngược hướng phổ cập đại chúng.'),
                ('Wrong Meaning', 'ephemeral = ngắn ngủi thoáng qua — sai chiều ngữ nghĩa.'),
            ]
        ),
        q_item(
            'd4_2_q11', 11, 'Craft and Structure', 'Words in Context', 'Elite (750+)',
            '<p>To ______ the acute housing shortage facing seasonal farmworkers without straining municipal budgets, the county partnered with local timber cooperatives to construct modular dwellings on surplus public land.</p>',
            STEM_WIC,
            ['exacerbate', 'scrutinize', 'ameliorate', 'perpetuate'],
            'C',
            'Subject-Object Collocation Fit! Tân ngữ là "the acute housing shortage" (một VẤN ĐỀ XẤU/CẤP BÁCH). Huyện xây nhà lắp ghép nhằm LÀM DỊU / CẢI THIỆN tình trạng thiếu hụt nghiêm trọng đó → "ameliorate" (C)! Nhớ bài 4.2: "ameliorate" kết hợp hoàn hảo với problem / shortage / hardship!',
            'Collocation vàng 750+: ameliorate a shortage / crisis / hardship = cải thiện, làm dịu một tình trạng xấu!',
            [
                ('Opposite Meaning', 'exacerbate = làm trầm trọng thêm — ngược hoàn toàn mục đích xây thêm nhà ở.'),
                ('Wrong Action', 'scrutinize = xem xét kỹ lưỡng — xây nhà là hành động giải quyết chứ không phải chỉ quan sát.'),
                ('Đáp án đúng', 'ameliorate = cải thiện/làm giảm bớt tình trạng khó khăn — kết hợp chuẩn xác với "acute housing shortage".'),
                ('Opposite Meaning', 'perpetuate = kéo dài mãi tình trạng thiếu nhà — ngược mục đích.'),
            ]
        ),
        q_item(
            'd4_2_q12', 12, 'Craft and Structure', 'Words in Context', 'Elite (750+)',
            '<p>Although the astronomer’s earliest papers drew skeptical responses for challenging orthodox models of planetary migration, her subsequent computer simulations proved so mathematically rigorous that they ______ her reputation among international peers.</p>',
            STEM_WIC,
            ['imperiled', 'conflated', 'eschewed', 'buttressed'],
            'D',
            'Contrast Clue: "Although... drew skeptical responses" → các mô phỏng cực kỳ chặt chẽ về toán học sau đó đã CỦNG CỐ VỮNG CHẮC uy tín của bà trong giới đồng nghiệp → "buttressed" (D)!',
            'Buttress (v) = chống đỡ, củng cố vững chắc (dùng chuẩn cho reputation, argument, claim, theory).',
            [
                ('Opposite Meaning', 'imperiled = gây nguy hiểm cho uy tín — ngược vế đối lập "Although skeptical... rigorous".'),
                ('Wrong Meaning', 'conflated = gộp lẫn hai khái niệm khác nhau — sai hoàn toàn ngữ cảnh.'),
                ('Wrong Meaning', 'eschewed = tránh xa, kiêng kỵ — mô phỏng toán học không "né tránh uy tín".'),
                ('Đáp án đúng', 'buttressed = củng cố, tăng cường vững chắc uy tín khoa học của bà.'),
            ]
        ),
        q_item(
            'd4_2_q13', 13, 'Craft and Structure', 'Words in Context', 'Elite (750+)',
            '<p>Because the newly translated Sumerian medical tablet relies on obscure botanical nicknames that appear in no other surviving cuneiform archive, philologists regard several of its herbal prescriptions as stubbornly ______.</p>',
            STEM_WIC,
            ['enigmatic', 'transparent', 'superfluous', 'dogmatic'],
            'A',
            'Cause-Effect Clue: dựa vào tên thực vật tối nghĩa không xuất hiện ở bất kỳ văn bản chữ hình nêm nào khác → các bài thuốc vẫn BÍ ẨN, KHÓ GIẢI MÃ → "enigmatic" (A)!',
            'Obscure + no other surviving archive = manh mối của nhóm từ bí ẩn khó giải mã: enigmatic / inscrutable / arcane.',
            [
                ('Đáp án đúng', 'enigmatic = bí ẩn, khó giải mã — khớp trực tiếp với "obscure botanical nicknames... in no other archive".'),
                ('Opposite Meaning', 'transparent = rõ ràng dễ hiểu — trái nghĩa hoàn toàn.'),
                ('Wrong Meaning', 'superfluous = thừa thãi — không nói bài thuốc thừa mà nói không giải mã nổi tên cây.'),
                ('Wrong Meaning', 'dogmatic = giáo điều cứng nhắc — sai ngữ cảnh dịch thuật cổ ngữ.'),
            ]
        ),
        q_item(
            'd4_2_q14', 14, 'Craft and Structure', 'Words in Context', 'Elite (750+)',
            '<p>While the museum’s board initially worried that eliminating admission fees would reduce philanthropic giving, five years of financial audits have ______ that concern: annual donor contributions actually rose by twenty-eight percent after entry became free.</p>',
            STEM_WIC,
            ['vindicated', 'allayed', 'provoked', 'stipulated'],
            'B',
            'Contrast + Colon Clue: Ban quản trị LO NGẠI ("worried... that concern"), nhưng kiểm toán 5 năm cho thấy quyên góp TĂNG 28% → làm DỊU / XUA TAN nỗi lo lắng đó → "allayed" (B)! Cẩn thận bẫy A ("vindicated" = chứng minh là đúng — sẽ thành chứng minh nỗi lo là ĐÚNG, ngược hoàn toàn với "actually rose"!).',
            'Collocation sát thủ 750+: "allay a concern / fear" = xua tan nỗi lo; còn "vindicate a concern" = chứng minh nỗi lo là có cơ sở (ngược cực!).',
            [
                ('Opposite Meaning Trap!', 'vindicated = chứng minh sự đúng đắn — nếu dùng ở đây nghĩa là chứng minh nỗi lo giảm quyên góp là ĐÚNG, trái ngược "actually rose by 28%"!'),
                ('Đáp án đúng', 'allayed = làm dịu đi, xua tan nỗi lo ngại — khớp tuyệt đối với kết quả quyên góp tăng 28%.'),
                ('Opposite Meaning', 'provoked = khơi gợi, châm ngòi nỗi lo — trái ngược dữ kiện tích cực.'),
                ('Wrong Collocation', 'stipulated = quy định điều khoản — kiểm toán không "quy định nỗi lo".'),
            ]
        ),
    ]
    return {
        'schemaVersion': 1,
        'mode': 'drill',
        'section': 'Reading and Writing',
        'basicInfo': {
            'title': 'Drill 4.2: Words in Context II — 750+ Elite Lexicon & Nuance Traps (14 Qs)',
            'subtitle': 'Luyện từ vựng học thuật tầng Hard Module 2 (mitigate vs. preclude, corroborate, equivocal, tenuous, circumvent, idiosyncratic, disparate, allay vs. vindicate).',
            'difficultyBadge': 'C&S • Target 1500+',
            'targetTimeMinutes': 13,
        },
        'drillModule': {
            'id': 'drill_4_2_mod',
            'title': 'Skill Drill 4.2: Words in Context II (750+ Elite Lexicon)',
            'timeLimitMinutes': 13,
            'questions': questions,
        },
    }
