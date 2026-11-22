# -*- coding: utf-8 -*-
"""
Hand-crafted 1500+ Elite Digital SAT R&W Skill Drills:
- Drill 2.2: Boundaries II — Modifiers, Appositives & Punctuation Traps (15 Qs)
- Drill 2.3: Form, Structure & Sense I — Verbs, Agreement & Tense (15 Qs)
- Drill 2.4: Form, Structure & Sense II — Modifiers, Possessives & Pronouns (15 Qs)
"""

from sat_drills_1_1_and_2_1 import q_item

STEM_SEC = 'Which choice completes the text so that it conforms to the conventions of Standard English?'

def get_drill_2_2():
    questions = [
        q_item(
            'd2_2_q1', 1, 'Standard English Conventions', 'Boundaries', 'Medium',
            '<p>In 2016, astrophysicist ______ led an international collaboration that produced the first direct interferometric image of a supermassive black hole’s shadow.</p>',
            STEM_SEC,
            ['Sheperd Doeleman,', 'Sheperd Doeleman', ', Sheperd Doeleman,', ', Sheperd Doeleman'],
            'B',
            'Cấu trúc "astrophysicist Sheperd Doeleman" là [Nghề nghiệp không có mạo từ a/the] + Tên riêng → Essential (0 dấu phẩy), và làm chủ ngữ trực tiếp cho động từ "led" (không đặt phẩy đơn ngăn S–V).',
            'Không có "a/the/his" trước chức danh + tên riêng → 0 dấu phẩy ở cả 2 đầu!',
            [
                ('No-Comma Zone (S, V)', 'Đặt 1 dấu phẩy đơn ngay trước động từ chính "led" tách rời Chủ ngữ và Động từ.'),
                ('Đáp án đúng', 'Không dấu phẩy — giữ liền mạch cụm chức danh + tên riêng với động từ chính "led".'),
                ('Non-Essential Trap', 'Chỉ dùng cặp phẩy khi chức danh phía trước có mạo từ xác định 1 người duy nhất (VD: "the project’s director, Sheperd Doeleman,").'),
                ('Unpaired Comma', 'Chỉ đặt 1 dấu phẩy mở trước tên mà không có dấu đóng.'),
            ]
        ),
        q_item(
            'd2_2_q2', 2, 'Standard English Conventions', 'Boundaries', 'Hard',
            '<p>The observatory’s founding ______ spent fourteen winters charting southern-hemisphere nebulae from a remote ridge in the Chilean Andes.</p>',
            STEM_SEC,
            ['director, Dr. Beatriz Navarro,', 'director Dr. Beatriz Navarro,', 'director, Dr. Beatriz Navarro', 'director Dr. Beatriz Navarro—'],
            'A',
            'Phía trước chức danh có cụm sở hữu xác định DUY NHẤT 1 người ("The observatory’s founding director") → Tên riêng "Dr. Beatriz Navarro" là thông tin bổ sung (Non-Essential) → Bắt buộc bọc bằng CẶP 2 dấu phẩy: ", Dr. Beatriz Navarro,".',
            'Có sở hữu/mạo từ xác định 1 người duy nhất ("The observatory’s founding director") + Tên riêng → Bọc bằng CẶP phẩy!',
            [
                ('Đáp án đúng', 'Cặp hai dấu phẩy bọc gọn tên riêng bổ sung sau chức danh duy nhất "The observatory’s founding director".'),
                ('Unpaired Comma', 'Thiếu dấu phẩy mở trước tên riêng, biến dấu phẩy sau thành dấu ngăn S–V sai luật.'),
                ('Unpaired Comma', 'Có dấu phẩy mở nhưng thiếu dấu phẩy đóng trước động từ "spent".'),
                ('Unmatched Dash', 'Đặt 1 gạch ngang lẻ trước động từ chính không có cặp mở.'),
            ]
        ),
        q_item(
            'd2_2_q3', 3, 'Standard English Conventions', 'Boundaries', 'Hard',
            '<p>Salt marshes along the Atlantic seaboard—vital nurseries for commercially harvested shrimp, blue crabs, and juvenile ______ also buffer coastal towns against hurricane storm surges.</p>',
            STEM_SEC,
            ['flounder,', 'flounder;', 'flounder', 'flounder—'],
            'D',
            'Nhìn kỹ đầu cụm bổ sung ngay sau "seaboard": có một dấu gạch ngang mở (`—vital nurseries...`)! Theo quy tắc Paired Punctuation, mở bằng em-dash (—) thì BẮT BUỘC đóng bằng em-dash (—) trước động từ chính "also buffer" → Chọn D!',
            'Luôn quét ngược 1–2 dòng trước chỗ trống xem cụm xen giữa mở bằng dấu phẩy (,) hay gạch ngang (—) để đóng đúng cặp!',
            [
                ('Mismatched Pair (— ... ,)', 'Cấm mở bằng gạch ngang (—) rồi đóng bằng dấu phẩy (,).'),
                ('Semicolon Inside Modifier', 'Dấu chấm phẩy không thể đóng cụm bổ ngữ giữa S và V.'),
                ('Unclosed Modifier', 'Bỏ trống không đóng dấu gạch ngang làm câu vỡ cấu trúc.'),
                ('Đáp án đúng', 'Đóng đúng cặp gạch ngang (— ... —) bọc cụm đồng vị ngữ bổ sung ở giữa câu.'),
            ]
        ),
        q_item(
            'd2_2_q4', 4, 'Standard English Conventions', 'Boundaries', 'Hard',
            '<p>Biochemists studying thermophilic archaea have discovered ______ can maintain structural stability even when submerged in boiling volcanic vents.</p>',
            STEM_SEC,
            ['that certain membrane lipids,', 'that, certain membrane lipids', 'that certain membrane lipids', ', that certain membrane lipids'],
            'C',
            'Vùng CẤM dấu phẩy #2 & #3: KHÔNG đặt dấu phẩy ngay trước hoặc ngay sau liên từ "that" mở đầu mệnh đề tân ngữ, và KHÔNG đặt dấu phẩy đơn giữa chủ ngữ "certain membrane lipids" với động từ "can maintain" → Chọn C (0 dấu phẩy!).',
            'Thấy chữ "that" dẫn mệnh đề tân ngữ ("discovered that...", "argued that...") → 99% đáp án chuẩn là 0 dấu phẩy xung quanh "that"!',
            [
                ('No-Comma Zone (S, V)', 'Đặt dấu phẩy đơn ngăn chủ ngữ "certain membrane lipids" khỏi động từ "can maintain".'),
                ('No-Comma Zone (that,)', 'Cấm đặt dấu phẩy lẻ ngay sau "that".'),
                ('Đáp án đúng', 'Không dấu phẩy — giữ mạch V + that + S + V hoàn hảo.'),
                ('No-Comma Zone (V, that)', 'Cấm đặt dấu phẩy giữa động từ "discovered" và mệnh đề tân ngữ "that...".'),
            ]
        ),
        q_item(
            'd2_2_q5', 5, 'Standard English Conventions', 'Boundaries', 'Hard',
            '<p>The newly excavated frescoes at Akrotiri, which depict saffron harvesters navigating rocky volcanic ______ provide historians with rare visual evidence of Bronze Age Aegean trade rituals.</p>',
            STEM_SEC,
            ['slopes', 'slopes,', 'slopes;', 'slopes—'],
            'B',
            'Cụm mệnh đề quan hệ không xác định mở bằng dấu phẩy trước "which" (`, which depict saffron harvesters navigating rocky volcanic slopes`) → Bắt buộc đóng bằng dấu phẩy ngay trước động từ chính "provide" → Chọn B!',
            'Mở bằng `, which` → tìm đúng điểm kết thúc mệnh đề quan hệ (ngay trước động từ chính của câu) và đóng bằng dấu phẩy (,)!',
            [
                ('Unclosed Non-Essential Clause', 'Mở bằng `, which` nhưng quên đóng dấu phẩy trước động từ chính "provide".'),
                ('Đáp án đúng', 'Đóng đúng cặp phẩy cho mệnh đề quan hệ không xác định `, which ... ,`.'),
                ('Semicolon Trap', 'Dấu chấm phẩy tách rời chủ ngữ "The newly excavated frescoes" khỏi động từ "provide".'),
                ('Mismatched Pair (, ... —)', 'Mở bằng dấu phẩy thì cấm đóng bằng gạch ngang.'),
            ]
        ),
        q_item(
            'd2_2_q6', 6, 'Standard English Conventions', 'Boundaries', 'Elite (750+)',
            '<p>Initial laboratory models predicted that adding biochar to acidic tropical soils would immediately double maize yields. Field trials conducted across five Kenyan counties, ______, revealed that yield gains emerged gradually over three consecutive harvest cycles.</p>',
            STEM_SEC,
            ['however', '; however', 'however;', 'therefore'],
            'A',
            'Chú ý 2 dấu phẩy ĐÃ CÓ SẴN ngay hai bên chỗ trống (`, ______,`)! Cụm "Field trials conducted across five Kenyan counties" chỉ là Chủ ngữ (chưa phải IC), nên từ nối chen giữa S và V chỉ cần điền chữ "however" (không thêm dấu phẩy/chấm phẩy thừa) và nghĩa là ĐỐI LẬP với "immediately double" ở câu 1 (gradually over three cycles).',
            'LUÔN đọc sát ký tự ngay trước và ngay sau chỗ trống! Khi đề đã in sẵn 2 dấu phẩy `, ______,`, tuyệt đối không chọn đáp án có thêm dấu câu bên trong!',
            [
                ('Đáp án đúng', '"however" khớp nghĩa đối lập (immediately vs. gradually) và vừa khít giữa cặp dấu phẩy có sẵn.'),
                ('Double Punctuation / Illegal Semicolon', 'Vế trước chỉ là chủ ngữ (chưa có động từ), không thể đặt chấm phẩy, lại trùng dấu phẩy có sẵn.'),
                ('Double Punctuation / Illegal Semicolon', 'Không thể đặt dấu chấm phẩy ngay trước động từ chính "revealed".'),
                ('Wrong Meaning (Cause-Effect)', 'therefore chỉ hệ quả — sai logic vì kết quả thực địa trái ngược dự đoán phòng thí nghiệm.'),
            ]
        ),
        q_item(
            'd2_2_q7', 7, 'Standard English Conventions', 'Boundaries', 'Elite (750+)',
            '<p>Botanical illustrators working in the eighteenth century often relied on dried herbarium specimens ______ had lost much of their original petal pigmentation during long ocean voyages.</p>',
            STEM_SEC,
            ['that', ', that', ', which,', '; which'],
            'A',
            'Mệnh đề quan hệ "that had lost much of their original petal pigmentation" là Essential (giới hạn đúng loại mẫu thực vật bị mất màu) và bắt đầu bằng "that" → Trên Digital SAT, TUYỆT ĐỐI KHÔNG đặt dấu phẩy trước "that"!',
            'Quy tắc vàng: Không bao giờ có ", that" trong mệnh đề quan hệ! (`, which` = Non-essential; `that` không phẩy = Essential).',
            [
                ('Đáp án đúng', 'Mệnh đề quan hệ xác định dùng "that" không có dấu phẩy phía trước.'),
                ('Forbidden Comma Before That', 'Cấm đặt dấu phẩy trước đại từ quan hệ "that".'),
                ('Extra Comma Trap', 'Đặt thêm dấu phẩy ngay sau "which" cắt đứt chủ ngữ "which" khỏi động từ "had lost".'),
                ('Semicolon + Fragment', 'Sau dấu chấm phẩy phải là IC, nhưng "which had lost..." là mệnh đề quan hệ (DC).'),
            ]
        ),
        q_item(
            'd2_2_q8', 8, 'Standard English Conventions', 'Boundaries', 'Hard',
            '<p>Despite its modest wingspan of barely ten centimeters, the ruby-throated hummingbird—a migratory species capable of crossing the Gulf of Mexico in a single nonstop ______ must consume nearly double its body weight in nectar each day before departure.</p>',
            STEM_SEC,
            ['flight,', 'flight—', 'flight;', 'flight:'],
            'B',
            'Cụm bổ sung giữa S và V mở bằng em-dash: `—a migratory species capable of crossing the Gulf of Mexico in a single nonstop flight—` → Phải đóng bằng em-dash (—) trước động từ chính "must consume".',
            'Mở bằng em-dash (—) → Đóng bằng em-dash (—), bỏ qua hoàn toàn độ dài của cụm chen giữa!',
            [
                ('Mismatched Pair (— ... ,)', 'Không được đóng cụm mở bằng gạch ngang với dấu phẩy.'),
                ('Đáp án đúng', 'Hoàn thiện cặp gạch ngang đôi bọc cụm đồng vị ngữ bổ sung trước động từ chính "must consume".'),
                ('Semicolon Trap', 'Dấu chấm phẩy phá vỡ kết nối giữa chủ ngữ "hummingbird" và động từ "must consume".'),
                ('Colon Trap', 'Dấu hai chấm không thể đóng một cụm bổ sung nằm giữa chủ ngữ và động từ.'),
            ]
        ),
        q_item(
            'd2_2_q9', 9, 'Standard English Conventions', 'Boundaries', 'Hard',
            '<p>Marine archaeologists surveying the sunken Roman port of Caesarea Maritima documented hydraulic concrete blocks made with volcanic ash from ______ that actually grew stronger after centuries of seawater exposure.</p>',
            STEM_SEC,
            ['Pozzuoli, a material', 'Pozzuoli a material', 'Pozzuoli; a material', 'Pozzuoli, a material,'],
            'A',
            'Cụm "a material that actually grew stronger after centuries of seawater exposure" là 1 Appositive (đồng vị ngữ) giải thích cho "hydraulic concrete blocks / volcanic ash" ở cuối câu. Phía trước cụm này cần 1 dấu phẩy mở (`, a material`), và KHÔNG ĐƯỢC đặt dấu phẩy giữa "material" và mệnh đề quan hệ xác định "that..." → Chọn A!',
            'Khi đồng vị ngữ đứng ở CUỐI CÂU (`IC, a material that...`), chỉ cần 1 dấu phẩy mở ở đầu cụm và CẤM đặt dấu phẩy trước "that"!',
            [
                ('Đáp án đúng', 'Dấu phẩy mở ra cụm đồng vị ngữ ở cuối câu và nối liền mạch với mệnh đề xác định "that...".'),
                ('Missing Comma Before Appositive', 'Thiếu dấu phẩy ngăn cách địa danh "Pozzuoli" với cụm đồng vị ngữ "a material...".'),
                ('Semicolon + Fragment', 'Sau dấu chấm phẩy phải là IC, nhưng "a material that..." chỉ là cụm danh từ (Fragment).'),
                ('Forbidden Comma Before That', 'Đặt dấu phẩy ngay trước "that" tách rời danh từ khỏi mệnh đề quan hệ xác định.'),
            ]
        ),
        q_item(
            'd2_2_q10', 10, 'Standard English Conventions', 'Boundaries', 'Elite (750+)',
            '<p>Physicists testing superconducting cables at Brookhaven National Laboratory discovered that slight crystalline impurities ______ unexpectedly enhanced the wire’s current-carrying capacity under high magnetic fields.</p>',
            STEM_SEC,
            ['—rather than degrading performance,', ', rather than degrading performance—', 'rather than degrading performance,', '—rather than degrading performance—'],
            'D',
            'Cụm "rather than degrading performance" là cụm bổ sung chen giữa Chủ ngữ ("slight crystalline impurities") và Động từ ("unexpectedly enhanced"). Bắt buộc phải bọc bằng 1 CẶP DẤU GIỐNG NHAU ở cả 2 đầu (`— ... —` hoặc `, ... ,`). Duy nhất D dùng đúng cặp `— ... —`!',
            'Kiểm tra tính đối xứng 2 đầu của cụm chen giữa S và V: chỉ `, ... ,` hoặc `— ... —` là hợp lệ; mọi cặp lệch hay thiếu 1 đầu đều sai 100%!',
            [
                ('Mismatched Pair (— ... ,)', 'Mở bằng gạch ngang mà đóng bằng phẩy.'),
                ('Mismatched Pair (, ... —)', 'Mở bằng phẩy mà đóng bằng gạch ngang.'),
                ('Unpaired Comma', 'Thiếu dấu mở trước "rather than", tạo ra 1 dấu phẩy lẻ chia cắt S–V.'),
                ('Đáp án đúng', 'Cặp hai dấu gạch ngang đối xứng bọc cụm tương phản xen giữa Chủ ngữ và Động từ.'),
            ]
        ),
        q_item(
            'd2_2_q11', 11, 'Standard English Conventions', 'Boundaries', 'Hard',
            '<p>Contemporary ceramicist Magdalene Odundo—whose hand-coiled vessels draw inspiration from both ancient Greek amphorae and traditional Kenyan pottery ______ refuses to use a potter’s wheel, preferring to shape each curve solely by hand.</p>',
            STEM_SEC,
            ['traditions,', 'traditions;', 'traditions', 'traditions—'],
            'D',
            'Phía sau "Magdalene Odundo" có dấu gạch ngang mở (`—whose hand-coiled vessels...`). Mệnh đề "whose..." kết thúc ngay trước động từ chính "refuses" → Phải đóng bằng dấu gạch ngang thứ hai (`traditions—`)!',
            'Xác định cặp chủ–vị chính ("Magdalene Odundo ... refuses") để biết chính xác vị trí đóng dấu gạch ngang.',
            [
                ('Mismatched Pair (— ... ,)', 'Lệch cặp dấu (mở gạch ngang, đóng dấu phẩy).'),
                ('Semicolon Trap', 'Chấm phẩy không thể đóng mệnh đề bổ ngữ giữa S và V.'),
                ('Unclosed Modifier', 'Thiếu dấu đóng gạch ngang.'),
                ('Đáp án đúng', 'Khép đúng cặp gạch ngang đôi cho mệnh đề bổ sung "whose..." ngay trước động từ chính "refuses".'),
            ]
        ),
        q_item(
            'd2_2_q12', 12, 'Standard English Conventions', 'Boundaries', 'Elite (750+)',
            '<p>In a landmark 2022 ethnography, cultural anthropologist ______ examined how seasonal pastoralists in Mongolia integrate satellite weather forecasts with oral ecological knowledge passed down across generations.</p>',
            STEM_SEC,
            ['Dr. Altantsetseg Batbayar', ', Dr. Altantsetseg Batbayar,', 'Dr. Altantsetseg Batbayar,', ', Dr. Altantsetseg Batbayar'],
            'A',
            'Lại là cấu trúc "cultural anthropologist Dr. Altantsetseg Batbayar" (KHÔNG có mạo từ a/the trước chức danh) → Essential Title + Name → 0 dấu phẩy! Và không đặt phẩy lẻ trước động từ "examined".',
            'Đừng bị lừa bởi chức danh dài 2–3 từ ("cultural anthropologist"): hễ không có mạo từ "a/the/her" ở trước thì tên riêng luôn là Essential (0 dấu phẩy)!',
            [
                ('Đáp án đúng', '0 dấu phẩy cho cấu trúc [Nghề nghiệp không mạo từ] + Tên riêng nối thẳng sang động từ "examined".'),
                ('Non-Essential Trap', 'Chỉ đặt cặp phẩy nếu trước chức danh có "the/a/her" xác định một người duy nhất.'),
                ('No-Comma Zone (S, V)', 'Dấu phẩy đơn ngăn cách chủ ngữ khỏi động từ chính "examined".'),
                ('Unpaired Comma', 'Dấu phẩy đơn lẻ giữa chức danh và tên riêng.'),
            ]
        ),
        q_item(
            'd2_2_q13', 13, 'Standard English Conventions', 'Boundaries', 'Hard',
            '<p>The newly installed pedestrian bridge spans the gorge in a single sweeping arch ______ engineered to flex gently under high mountain winds without transferring excessive stress to the canyon walls.</p>',
            STEM_SEC,
            ['of weathered steel,', 'of weathered steel;', 'of weathered steel:', 'of, weathered steel,'],
            'A',
            'Cụm "of weathered steel" bổ nghĩa trực tiếp cho "arch" (vùng CẤM phẩy sau giới từ "of", nên loại D). Phía sau là cụm phân từ quá khứ bổ sung ("engineered to flex gently...") không phải IC → Dùng dấu phẩy đơn mở cụm phân từ bổ sung (`of weathered steel, engineered...`). Loại B và C vì vế sau không phải IC / không phải danh sách giải thích trực tiếp.',
            'Cụm phân từ V-ed/V-ing bổ sung ở cuối câu (non-essential participial phrase) luôn đi sau dấu phẩy (,), KHÔNG đi sau dấu chấm phẩy (;).',
            [
                ('Đáp án đúng', 'Nối liền "of weathered steel" rồi đặt dấu phẩy mở cụm phân từ bổ sung "engineered to flex...".'),
                ('Semicolon + Fragment', '"engineered to flex..." là cụm phân từ, không phải IC nên cấm dùng chấm phẩy.'),
                ('Colon Misuse', 'Dấu hai chấm không phù hợp để ngăn trước cụm phân từ mô tả đơn thuần bằng "engineered".'),
                ('No-Comma Zone (Prep, N)', 'Cấm đặt dấu phẩy ngay sau giới từ "of".'),
            ]
        ),
        q_item(
            'd2_2_q14', 14, 'Standard English Conventions', 'Boundaries', 'Elite (750+)',
            '<p>Linguists analyzing endangered whistling languages on La Gomera found that skilled whistlers can transmit complex messages across valleys exceeding three kilometers in ______ a range far greater than that of shouted speech.</p>',
            STEM_SEC,
            ['width', 'width;', 'width,', 'width: and'],
            'C',
            'Vế trước ("Linguists analyzing... exceeding three kilometers in width") là IC hoàn chỉnh. Vế sau ("a range far greater than that of shouted speech") là cụm đồng vị ngữ (Appositive Phrase) tóm gọn lại "three kilometers in width" → Bắt buộc đặt dấu phẩy (,) ngăn cách trước cụm đồng vị ngữ ở cuối câu! Không có phẩy (A) sẽ làm dính 2 danh từ "width a range".',
            'Nhận diện cụm "a/an + Noun + modifier" tổng kết lại ý ngay trước nó ở cuối câu (summative modifier) → luôn đặt 1 dấu phẩy (,) ngay trước nó!',
            [
                ('Missing Comma Before Appositive', 'Thiếu dấu phẩy làm "width" dính liền vô nghĩa với "a range".'),
                ('Semicolon + Fragment', '"a range far greater..." không có động từ chia thì → không phải IC → cấm dấu chấm phẩy.'),
                ('Đáp án đúng', 'Dấu phẩy chuẩn xác giới thiệu cụm đồng vị ngữ tổng kết (summative appositive) ở cuối câu.'),
                ('Illegal Colon + FANBOYS', 'Dấu hai chấm không đi kèm "and" trước một cụm danh từ.'),
            ]
        ),
        q_item(
            'd2_2_q15', 15, 'Standard English Conventions', 'Boundaries', 'Elite (750+)',
            '<p>Unlike conventional lithium-ion batteries, which rely on flammable liquid ______ solid-state prototypes employ dense ceramic separators that significantly reduce thermal runaway risks.</p>',
            STEM_SEC,
            ['electrolytes;', 'electrolytes,', 'electrolytes—', 'electrolytes'],
            'B',
            'Đầu câu mở bằng cụm giới từ so sánh ("Unlike conventional lithium-ion batteries"), tiếp theo là mệnh đề quan hệ bổ sung mở bằng `, which rely on flammable liquid electrolytes` → Cần đóng bằng dấu phẩy (,) ngay trước chủ ngữ chính "solid-state prototypes" (vừa khép `, which... ,` vừa kết thúc cụm mở đầu "Unlike...,")!',
            'Khi một mệnh đề `, which...` nằm cuối cụm mở đầu ("Unlike X, which..."), một dấu phẩy đóng duy nhất đảm nhiệm cả hai vai trò trước chủ ngữ chính!',
            [
                ('Semicolon After Phrase', 'Toàn bộ phần "Unlike..., which..." chưa có mệnh đề chính (không phải IC) → cấm dùng chấm phẩy.'),
                ('Đáp án đúng', 'Dấu phẩy đóng đúng mệnh đề `, which...` và cụm giới từ mở đầu trước chủ ngữ chính "solid-state prototypes".'),
                ('Mismatched Pair (, ... —)', 'Mở bằng `, which` thì không thể đóng bằng gạch ngang.'),
                ('Unclosed Introductory Modifier', 'Thiếu dấu phẩy làm "electrolytes" dính liền chủ ngữ "solid-state prototypes".'),
            ]
        ),
    ]
    return {
        'schemaVersion': 1,
        'mode': 'drill',
        'section': 'Reading and Writing',
        'basicInfo': {
            'title': 'Drill 2.2: Boundaries II — Modifiers, Appositives & Punctuation Traps (15 Qs)',
            'subtitle': 'Xử lý triệt để Essential vs. Non-Essential, Title+Name, cặp phẩy/gạch ngang và 4 vùng CẤM dấu phẩy.',
            'difficultyBadge': 'SEC • Target 1500+',
            'targetTimeMinutes': 12,
        },
        'drillModule': {
            'id': 'drill_2_2_mod',
            'title': 'Skill Drill 2.2: Boundaries II (Modifiers & Essential Rules)',
            'timeLimitMinutes': 12,
            'questions': questions,
        },
    }


def get_drill_2_3():
    questions = [
        q_item(
            'd2_3_q1', 1, 'Standard English Conventions', 'Form, Structure, and Sense', 'Medium',
            '<p>The intricate network of underground aqueducts engineered by ancient Persian hydrologists ______ arid highland villages with gravity-fed groundwater for more than two millennia.</p>',
            STEM_SEC,
            ['have supplied', 'supply', 'has supplied', 'supplying'],
            'C',
            'Gạch bỏ cụm giới từ & phân từ chen giữa: "The intricate <b>network</b> <s>[of underground aqueducts engineered by ancient Persian hydrologists]</s>". Chủ ngữ thật là "network" (SỐ ÍT), mốc thời gian "for more than two millennia" → Chọn "has supplied" (C). Mẹo 3–1 cũng lộ ngay C là động từ chia thì số ít duy nhất!',
            'Đừng bị đánh lừa bởi danh từ số nhiều "aqueducts" và "hydrologists" đứng sát chỗ trống — luôn truy ngược về danh từ đứng TRƯỚC chữ "of" đầu tiên!',
            [
                ('Subject-Verb Mismatch', 'have supplied chia số nhiều — bị lừa bởi "aqueducts / hydrologists".'),
                ('Subject-Verb Mismatch', 'supply chia số nhiều và không hợp mốc "for more than two millennia".'),
                ('Đáp án đúng', 'has supplied (số ít, hiện tại hoàn thành) khớp hoàn hảo với chủ ngữ "The intricate network" và "for more than two millennia".'),
                ('Non-Finite Fragment', 'supplying là V-ing khiến câu không có động từ chính.'),
            ]
        ),
        q_item(
            'd2_3_q2', 2, 'Standard English Conventions', 'Form, Structure, and Sense', 'Hard',
            '<p>Embedded within the stratified ice cores extracted from East Antarctica ______ microscopic air bubbles that preserve direct samples of Earth’s atmosphere from 800,000 years ago.</p>',
            STEM_SEC,
            ['lies', 'is lying', 'lie', 'has lain'],
            'C',
            'Câu Đảo ngữ (Inverted Subject)! Cụm phân từ mở đầu ("Embedded within the stratified ice cores...") không phải chủ ngữ. Chủ ngữ thật đứng SAU động từ là "microscopic air <b>bubbles</b>" (SỐ NHIỀU) → Chọn động từ số nhiều "lie" (C)! Dùng mẹo 3–1: A, B, D đều số ít, duy nhất C số nhiều!',
            'Mở đầu bằng V-ed/V-ing/Giới từ ("Embedded within...", "Beneath...", "Among...") mà sau chỗ trống là danh từ → Kiểm tra ngay Đảo ngữ (Chủ ngữ nằm SAU chỗ trống)!',
            [
                ('Inverted Subject Trap', 'lies là số ít — bị lừa vì tưởng "East Antarctica" là chủ ngữ.'),
                ('Inverted Subject Trap', 'is lying là số ít và sai thì diễn tả trạng thái tĩnh.'),
                ('Đáp án đúng', 'lie là động từ số nhiều khớp chính xác với chủ ngữ đảo phía sau "microscopic air bubbles".'),
                ('Inverted Subject Trap', 'has lain là số ít — không khớp "bubbles".'),
            ]
        ),
        q_item(
            'd2_3_q3', 3, 'Standard English Conventions', 'Form, Structure, and Sense', 'Hard',
            '<p>Each of the seventeen brass astrolabes housed in the museum’s Islamic astronomy wing ______ delicate Arabic engravings indicating the latitude for which the instrument was calibrated.</p>',
            STEM_SEC,
            ['bear', 'have borne', 'bearing', 'bears'],
            'D',
            'Chủ ngữ là đại từ bất định "Each" (Each of the seventeen brass astrolabes...) → LUÔN CHIA SỐ ÍT! Câu chưa có động từ chính (housed chỉ là phân từ rút gọn, indicating là V-ing) → Chọn "bears" (D).',
            'Học thuộc nhóm chủ ngữ LUÔN SỐ ÍT bất chấp "of + danh từ số nhiều": Each, Every, Either, Neither, One!',
            [
                ('Subject-Verb Mismatch', 'bear là số nhiều — bị lừa bởi "seventeen brass astrolabes".'),
                ('Subject-Verb Mismatch', 'have borne là số nhiều.'),
                ('Non-Finite Fragment', 'bearing làm câu khuyết động từ chia thì.'),
                ('Đáp án đúng', 'bears (số ít) khớp chuẩn với chủ ngữ "Each".'),
            ]
        ),
        q_item(
            'd2_3_q4', 4, 'Standard English Conventions', 'Form, Structure, and Sense', 'Hard',
            '<p>Calibrating optical spectrometers to detect trace amounts of methane in Martian dust storms ______ painstaking corrections for sunlight scattered by suspended iron-oxide particles.</p>',
            STEM_SEC,
            ['require', 'requires', 'have required', 'requiring'],
            'B',
            'Chủ ngữ là cụm danh động từ (Gerund Subject): "<b>Calibrating</b> optical spectrometers to detect trace amounts of methane in Martian dust storms" = VIỆC hiệu chuẩn máy quang phổ → LUÔN LÀ SỐ ÍT! Chọn "requires" (B).',
            'Khi cả cụm chủ ngữ bắt đầu bằng V-ing (Gerund: "Calibrating...", "Analyzing...", "Mapping..."), động từ chính LUÔN chia SỐ ÍT!',
            [
                ('Gerund Subject Trap', 'require là số nhiều — bị lừa bởi "storms / spectrometers".'),
                ('Đáp án đúng', 'requires (số ít) khớp chuẩn với chủ ngữ danh động từ "Calibrating...".'),
                ('Gerund Subject Trap', 'have required là số nhiều.'),
                ('Non-Finite Fragment', 'requiring tạo câu thiếu động từ chính.'),
            ]
        ),
        q_item(
            'd2_3_q5', 5, 'Standard English Conventions', 'Form, Structure, and Sense', 'Elite (750+)',
            '<p>Working alongside marine chemists in Norway, Norwegian engineer Ingrid Solberg ______ a floating wave-energy converter whose hinged pontoons automatically submerge during severe winter gales.</p>',
            STEM_SEC,
            ['patenting', 'to patent', 'patented', 'having patented'],
            'C',
            'Phép thử Finite vs. Non-Finite Verb! Chủ ngữ chính là "Norwegian engineer Ingrid Solberg". Cụm "Working alongside..." ở đầu là phân từ; "submerge" nằm trong mệnh đề quan hệ "whose...". Do đó mệnh đề chính CHƯA CÓ ĐỘNG TỪ CHIA THÌ → Bắt buộc chọn Finite Verb "patented" (C)! Loại sạch 3 dạng Non-Finite (A, B, D).',
            'Đếm số động từ chia thì bên ngoài mệnh đề quan hệ (who/which/that/whose): nếu bằng 0 → BẮT BUỘC chọn Finite Verb!',
            [
                ('Non-Finite Fragment', 'patenting là V-ing khiến chủ ngữ Ingrid Solberg không có động từ chia thì.'),
                ('Non-Finite Fragment', 'to patent là động từ nguyên mẫu, tạo Fragment.'),
                ('Đáp án đúng', 'patented là động từ chia thì (Finite Verb) hoàn thiện mệnh đề chính.'),
                ('Non-Finite Fragment', 'having patented là phân từ hoàn thành, không thể làm động từ chính.'),
            ]
        ),
        q_item(
            'd2_3_q6', 6, 'Standard English Conventions', 'Form, Structure, and Sense', 'Elite (750+)',
            '<p>Constructed from interlocking volcanic tuff blocks without a single drop of mortar, the ceremonial platforms of Easter Island—______ up to eighty tons apiece—have withstood centuries of Pacific seismic activity.</p>',
            STEM_SEC,
            ['weigh', 'weighing', 'they weigh', 'and weigh'],
            'B',
            'Kiểm tra xem mệnh đề chính ĐÃ CÓ ĐỘNG TỪ CHIA THÌ chưa: "the ceremonial platforms of Easter Island ... <b>have withstood</b> centuries..." → ĐÃ CÓ động từ chính "have withstood"! Chỗ trống nằm bên trong cặp gạch ngang bổ sung (`—______ up to eighty tons apiece—`) → Phải chọn Non-Finite participle "weighing" (B) để bổ nghĩa cho "platforms"!',
            'Trong cặp gạch ngang bổ ngữ giữa S và V, nếu không có đại từ quan hệ ("which") thì dùng phân từ (V-ing / V-ed), tránh đưa động từ chia thì trơ trọi!',
            [
                ('Double Finite Verb Trap', 'Đặt động từ chia thì "weigh" không có chủ ngữ/liên từ vào giữa S và V gây lỗi cú pháp.'),
                ('Đáp án đúng', 'Cụm phân từ "weighing up to eighty tons apiece" nằm gọn trong cặp gạch ngang bổ nghĩa cho "platforms".'),
                ('Awkward Independent Clause', '"they weigh" ở dạng IC chen giữa S–V với "apiece" nghe rời rạc và kém chuẩn hơn cụm phân từ rút gọn trong ngữ pháp SAT.'),
                ('Broken Parallelism', 'Không có động từ trước đó trong cặp gạch ngang để nối bằng "and weigh".'),
            ]
        ),
        q_item(
            'd2_3_q7', 7, 'Standard English Conventions', 'Form, Structure, and Sense', 'Hard',
            '<p>Although the number of independent print bookstores in mid-sized American towns ______ steadily between 2005 and 2015, recent retail surveys indicate a surprising resurgence fueled by community reading clubs.</p>',
            STEM_SEC,
            ['were declining', 'have declined', 'declined', 'are declining'],
            'C',
            'Hai bộ lọc song song: (1) Mỏ neo thời gian quá khứ đã khép lại "between 2005 and 2015" → Bắt buộc dùng QUÁ KHỨ ĐƠN ("declined"); (2) Chủ ngữ là "<b>The number</b> of independent print bookstores" → SỐ ÍT (nên loại luôn A "were", B "have", D "are" đều là số nhiều!). C thắng tuyệt đối ở cả thì lẫn số!',
            '"The number of + N" = SỐ ÍT; mốc "between 2005 and 2015" đã kết thúc hoàn toàn trong quá khứ → Quá khứ đơn (Simple Past)!',
            [
                ('Subject-Verb Mismatch', 'were declining là số nhiều — sai với chủ ngữ "The number of...".'),
                ('Tense + Agreement Error', 'have declined vừa sai số nhiều vừa sai thì (không dùng hiện tại hoàn thành cho mốc quá khứ đã đóng "between 2005 and 2015").'),
                ('Đáp án đúng', 'declined (quá khứ đơn) khớp chính xác với giai đoạn 2005–2015 đã kết thúc và dùng được cho chủ ngữ số ít.'),
                ('Tense + Agreement Error', 'are declining sai cả thì hiện tại lẫn số nhiều.'),
            ]
        ),
        q_item(
            'd2_3_q8', 8, 'Standard English Conventions', 'Form, Structure, and Sense', 'Hard',
            '<p>By the time European botanists formally cataloged the Wollemi pine in New South Wales in 1994, the ancient conifer lineage ______ quietly in a single sheltered sandstone gorge for millions of years.</p>',
            STEM_SEC,
            ['persists', 'will persist', 'is persisting', 'had persisted'],
            'D',
            'Mỏ neo thời gian kinh điển của Past Perfect: "By the time European botanists formally cataloged... in 1994" (mốc quá khứ 1994). Hành động tồn tại hàng triệu năm xảy ra TRƯỚC hẳn mốc quá khứ 1994 đó → Bắt buộc chọn Quá khứ hoàn thành "had persisted" (D)!',
            'Nhìn thấy "By the time + [Past Simple]" hoặc "Before [Past Year]" → Tìm ngay Past Perfect (had + V3)!',
            [
                ('Tense Mismatch', 'Hiện tại đơn không khớp với mốc "By the time ... cataloged in 1994".'),
                ('Tense Mismatch', 'Thì tương lai mâu thuẫn hoàn toàn với mốc 1994.'),
                ('Tense Mismatch', 'Hiện tại tiếp diễn không thể đi với "By the time ... in 1994".'),
                ('Đáp án đúng', 'had persisted (Quá khứ hoàn thành) diễn tả chính xác quá trình kéo dài hàng triệu năm trước mốc quá khứ 1994.'),
            ]
        ),
        q_item(
            'd2_3_q9', 9, 'Standard English Conventions', 'Form, Structure, and Sense', 'Hard',
            '<p>The lead violinist, together with two historical-instrument makers from Cremona, ______ conducting acoustic tests on varnished spruce soundboards crafted using seventeenth-century recipes.</p>',
            STEM_SEC,
            ['are', 'were', 'is', 'have been'],
            'C',
            'Chủ ngữ chính là "The lead violinist" (SỐ ÍT). Cụm chen giữa hai dấu phẩy ", together with two historical-instrument makers from Cremona," là cụm bổ sung — KHÔNG làm biến đổi chủ ngữ thành số nhiều! (Gạch bỏ cụm phẩy → "The lead violinist is conducting..."). Chọn C ("is")!',
            'Các cụm ", together with / along with / as well as / accompanied by + N" KHÔNG tương đương chữ "and" — luôn gạch bỏ chúng để chia động từ theo Chủ ngữ 1!',
            [
                ('Additive Phrase Trap', 'are chia số nhiều vì bị lừa cộng dồn "violinist + two makers".'),
                ('Additive Phrase Trap', 'were chia số nhiều.'),
                ('Đáp án đúng', 'is (số ít) khớp chính xác với chủ ngữ duy nhất "The lead violinist".'),
                ('Additive Phrase Trap', 'have been chia số nhiều.'),
            ]
        ),
        q_item(
            'd2_3_q10', 10, 'Standard English Conventions', 'Form, Structure, and Sense', 'Elite (750+)',
            '<p>In 1962, marine biologist Rachel Carson warned that the indiscriminate spraying of synthetic pesticides ______ songbird populations across North America unless federal regulators curtailed chemical runoff.</p>',
            STEM_SEC,
            ['will devastate', 'would devastate', 'devastates', 'has devastated'],
            'B',
            'Mỏ neo thời gian trong câu tường thuật quá khứ: "In 1962, Rachel Carson <b>warned</b> that ... unless regulators <b>curtailed</b>...". Khi tường thuật một dự báo về tương lai đặt trong khung quá khứ (warned / predicted / hypothesized that...), chuẩn Digital SAT bắt buộc lùi "will" thành "<b>would</b>" → Chọn B!',
            'Trong câu tường thuật quá khứ (predicted/warned/expected that...), luôn chọn "would + V", loại "will + V"!',
            [
                ('Sequence of Tenses Trap', 'will không hòa hợp với động từ tường thuật quá khứ "warned" và mệnh đề "unless... curtailed".'),
                ('Đáp án đúng', 'would devastate hòa hợp hoàn hảo về sequence of tenses trong câu dự báo quá khứ (In 1962... warned... unless curtailed).'),
                ('Tense Mismatch', 'Hiện tại đơn sai ngữ cảnh tường thuật quá khứ giả định năm 1962.'),
                ('Tense Mismatch', 'Hiện tại hoàn thành không thể làm lời cảnh báo hướng tới tương lai trong quá khứ.'),
            ]
        ),
        q_item(
            'd2_3_q11', 11, 'Standard English Conventions', 'Form, Structure, and Sense', 'Elite (750+)',
            '<p>A growing number of urban hydrologists ______ permeable asphalt pavements as a cost-effective alternative to expanding subterranean stormwater tunnels in flood-prone cities.</p>',
            STEM_SEC,
            ['is advocating', 'advocates', 'has advocated', 'are advocating'],
            'D',
            'Phân biệt cặp kinh điển: "<b>The</b> number of + N" = SỐ ÍT, nhưng "<b>A</b> (growing) number of + N" (= Many / Numerous) = SỐ NHIỀU! Chủ ngữ "A growing number of urban hydrologists" mang nghĩa nhiều nhà thủy văn học → Chia SỐ NHIỀU → Chọn D ("are advocating"). Mẹo 3–1: A, B, C đều số ít, duy nhất D số nhiều!',
            '"The number of" → ÍT; "A (growing/large) number of" → NHIỀU!',
            [
                ('A Number Of Trap', 'is advocating là số ít — nhầm với "The number of".'),
                ('A Number Of Trap', 'advocates là số ít.'),
                ('A Number Of Trap', 'has advocated là số ít.'),
                ('Đáp án đúng', 'are advocating (số nhiều) khớp chuẩn với "A growing number of urban hydrologists".'),
            ]
        ),
        q_item(
            'd2_3_q12', 12, 'Standard English Conventions', 'Form, Structure, and Sense', 'Elite (750+)',
            '<p>That tiny migratory songbirds weighing barely twelve grams navigate thousands of miles across featureless ocean expanses without ever losing their bearing ______ sensory biologists who study avian magnetoreception.</p>',
            STEM_SEC,
            ['continue to fascinate', 'continues to fascinate', 'have continued to fascinate', 'continuing to fascinate'],
            'B',
            'Chủ ngữ là nguyên một MỆNH ĐỀ DANH NGỮ (Noun Clause Subject): "<b>That</b> tiny migratory songbirds... losing their bearing" = VIỆC những chú chim nhỏ ấy định hướng vượt đại dương → Cả mệnh đề làm chủ ngữ LUÔN CHIA SỐ ÍT! Chọn B ("continues to fascinate")!',
            'Mệnh đề bắt đầu bằng "That / What / Whether + S + V" đứng làm chủ ngữ luôn tính là 1 sự việc duy nhất → Chia động từ SỐ ÍT!',
            [
                ('Clause Subject Trap', 'continue là số nhiều — bị lừa bởi "songbirds / miles / expanses".'),
                ('Đáp án đúng', 'continues to fascinate (số ít) khớp chuẩn với chủ ngữ mệnh đề danh ngữ "That tiny migratory songbirds...".'),
                ('Clause Subject Trap', 'have continued là số nhiều.'),
                ('Non-Finite Fragment', 'continuing thiếu động từ chính cho mệnh đề chủ ngữ.'),
            ]
        ),
        q_item(
            'd2_3_q13', 13, 'Standard English Conventions', 'Form, Structure, and Sense', 'Hard',
            '<p>Developed by chemist Stephanie Kwolek in 1965 while researching lightweight tire reinforcements, Kevlar fibers ______ a tensile strength five times greater than that of steel on an equal-weight basis.</p>',
            STEM_SEC,
            ['possessing', 'to possess', 'possess', 'possesses'],
            'C',
            'Chủ ngữ chính là "Kevlar fibers" (SỐ NHIỀU). Câu chưa có động từ chia thì ("Developed..." ở đầu là phân từ quá khứ). Cần Finite Verb SỐ NHIỀU ở hiện tại đơn (nêu đặc tính vật lý luôn đúng) → Chọn C ("possess")!',
            'Nhớ rằng tính chất vật lý/khoa học luôn đúng vẫn dùng hiện tại đơn ("possess") dù mệnh đề phân từ mở đầu nhắc mốc phát minh năm 1965 ("Developed in 1965")!',
            [
                ('Non-Finite Fragment', 'possessing khiến câu thiếu động từ chính.'),
                ('Non-Finite Fragment', 'to possess tạo Fragment.'),
                ('Đáp án đúng', 'possess là động từ chia thì số nhiều khớp với "Kevlar fibers" và nêu đặc tính vật lý bền vững.'),
                ('Subject-Verb Mismatch', 'possesses là số ít — sai với "Kevlar fibers" (số nhiều).'),
            ]
        ),
        q_item(
            'd2_3_q14', 14, 'Standard English Conventions', 'Form, Structure, and Sense', 'Elite (750+)',
            '<p>In the high-altitude lakes of the Bolivian Altiplano, extreme ultraviolet radiation and hypersaline water chemistry ______ harsh conditions that resemble those believed to have existed on early Mars.</p>',
            STEM_SEC,
            ['creates', 'has created', 'create', 'creating'],
            'C',
            'Chủ ngữ ghép nối bằng chữ "and": "extreme ultraviolet radiation <b>and</b> hypersaline water chemistry" (2 yếu tố riêng biệt → SỐ NHIỀU!). Câu chưa có động từ chính → Chọn C ("create")!',
            'Hai danh từ không đếm được nối bằng "and" ("radiation and chemistry") tạo thành Chủ ngữ ghép SỐ NHIỀU!',
            [
                ('Compound Subject Trap', 'creates là số ít — chỉ nhìn danh từ gần nhất "chemistry" mà quên chữ "and".'),
                ('Compound Subject Trap', 'has created là số ít.'),
                ('Đáp án đúng', 'create (số nhiều) khớp chuẩn với chủ ngữ ghép "radiation and chemistry".'),
                ('Non-Finite Fragment', 'creating khiến câu khuyết động từ chính.'),
            ]
        ),
        q_item(
            'd2_3_q15', 15, 'Standard English Conventions', 'Form, Structure, and Sense', 'Elite (750+)',
            '<p>After analyzing bone isotopes from twenty-four medieval skeletons excavated near York, bioarchaeologist Dr. Clara Jensen concluded that dietary diversity across social classes ______ far less pronounced than earlier chronicles had claimed.</p>',
            STEM_SEC,
            ['is being', 'was', 'were', 'have been'],
            'B',
            'Chủ ngữ bên trong mệnh đề "that" là "dietary <b>diversity</b> <s>[across social classes]</s>" (SỐ ÍT!). Mỏ neo thời gian quá khứ xuyên suốt câu ("concluded", "medieval skeletons", "had claimed") → Chọn Quá khứ đơn SỐ ÍT "was" (B)!',
            'Gạch cụm "across social classes" để không bị số nhiều "classes" đánh lừa, đồng thời giữ đúng thì quá khứ theo "concluded... had claimed"!',
            [
                ('Tense Mismatch', 'is being là hiện tại tiếp diễn — sai ngữ cảnh lịch sử trung cổ và câu tường thuật quá khứ.'),
                ('Đáp án đúng', 'was (quá khứ đơn, số ít) khớp trọn vẹn với "dietary diversity" và động từ tường thuật "concluded".'),
                ('Subject-Verb Mismatch', 'were là số nhiều — bị lừa bởi "social classes".'),
                ('Tense + Agreement Error', 'have been vừa sai số nhiều vừa lệch thì quá khứ.'),
            ]
        ),
    ]
    return {
        'schemaVersion': 1,
        'mode': 'drill',
        'section': 'Reading and Writing',
        'basicInfo': {
            'title': 'Drill 2.3: Form, Structure & Sense I — Verbs, Agreement & Tense (15 Qs)',
            'subtitle': 'Luyện 5 chủ ngữ bẫy Hard Module 2 (Đảo ngữ, Gerund, Clause Subject, Each, The/A number of), Finite vs. Non-Finite và Hòa hợp thì.',
            'difficultyBadge': 'SEC • Target 1500+',
            'targetTimeMinutes': 12,
        },
        'drillModule': {
            'id': 'drill_2_3_mod',
            'title': 'Skill Drill 2.3: Form, Structure & Sense I (Verbs & Tense)',
            'timeLimitMinutes': 12,
            'questions': questions,
        },
    }


def get_drill_2_4():
    questions = [
        q_item(
            'd2_4_q1', 1, 'Standard English Conventions', 'Form, Structure, and Sense', 'Hard',
            '<p>Carved directly into rose-red sandstone cliffs more than two thousand years ago, ______</p>',
            STEM_SEC,
            [
                'the Nabataean merchants engineered Petra’s treasury to channel seasonal flash floods away from its facade.',
                'archaeologists continue to marvel at the Nabataean monuments of Petra in southern Jordan.',
                'the monumental facades of Petra showcase sophisticated Nabataean hydraulic engineering.',
                'Petra’s builders relied on hidden ceramic pipes to supply the desert city with fresh spring water.'
            ],
            'C',
            'Cụm mở đầu "Carved directly into rose-red sandstone cliffs..." (Được chạm khắc trực tiếp vào vách đá sa thạch đỏ hồng) mô tả CÁC CÔNG TRÌNH KIẾN TRÚC (monumental facades), KHÔNG mô tả thương nhân (A), nhà khảo cổ (B), hay thợ xây (D — bẫy sở hữu cách: chủ ngữ của D là "builders")! Duy nhất C đặt đúng "the monumental facades of Petra" làm chủ ngữ ngay sau dấu phẩy.',
            'Hỏi ngay sau dấu phẩy: "Ai/Cái gì bị CHẠM KHẮC vào vách đá?" → Chỉ có "the monumental facades"!',
            [
                ('Dangling Modifier', 'Thương nhân Nabataean không thể bị "chạm khắc vào vách đá sa thạch".'),
                ('Dangling Modifier', 'Các nhà khảo cổ không thể bị "chạm khắc vào vách đá" hơn 2.000 năm trước.'),
                ('Đáp án đúng', 'Đặt đúng chủ ngữ "the monumental facades of Petra" khớp logic hoàn hảo với cụm mở đầu "Carved...".'),
                ('Possessive Subject Trap', 'Trong "Petra’s builders", chủ ngữ thật là "builders" (những người thợ xây), không phải công trình được chạm khắc.'),
            ]
        ),
        q_item(
            'd2_4_q2', 2, 'Standard English Conventions', 'Form, Structure, and Sense', 'Elite (750+)',
            '<p>Having pioneered x-ray diffraction photography to illuminate the molecular geometry of DNA in 1952, ______</p>',
            STEM_SEC,
            [
                'chemist Rosalind Franklin’s Photograph 51 became an indispensable clue to the double-helix model.',
                'the double-helix structure of DNA was rapidly deduced with the aid of Rosalind Franklin’s data.',
                'chemist Rosalind Franklin produced Photograph 51, an image pivotal to identifying the double-helix model.',
                'it was Rosalind Franklin whose meticulous laboratory measurements made Photograph 51 possible.'
            ],
            'C',
            'BẪY SỞ HỮU CÁCH 750+ KINH ĐIỂN! Cụm "Having pioneered x-ray diffraction photography..." mô tả NGƯỜI (nhà hóa học Rosalind Franklin). Trong A, chủ ngữ thật là "Photograph 51" (không phải Franklin!). Trong B là "the double-helix structure". Trong D là đại từ rỗng "it". Duy nhất C đặt trực tiếp "chemist Rosalind Franklin" làm chủ ngữ ngay sau dấu phẩy!',
            'Gặp "Rosalind Franklin’s [Noun]" sau dấu phẩy → Chủ ngữ thật là [Noun], KHÔNG PHẢI Rosalind Franklin → Loại ngay bẫy A!',
            [
                ('Possessive Subject Trap', 'Chủ ngữ ngữ pháp của A là "Photograph 51", không phải Rosalind Franklin — bức ảnh không thể tự "pioneer" kỹ thuật chụp!'),
                ('Dangling Modifier', 'Chủ ngữ là "the double-helix structure", không phải người tiên phong chụp ảnh.'),
                ('Đáp án đúng', 'Chủ ngữ "chemist Rosalind Franklin" đứng ngay sau dấu phẩy, khớp 100% với "Having pioneered...".'),
                ('Dummy Subject Trap', 'Chủ ngữ giả "it" phá vỡ quy tắc Modifier phải bám sát đúng danh từ chủ thể.'),
            ]
        ),
        q_item(
            'd2_4_q3', 3, 'Standard English Conventions', 'Form, Structure, and Sense', 'Medium',
            '<p>When the Arctic fox sheds ______ thick white winter coat in late spring, the underlying brown fur provides effective camouflage against thawed tundra soil.</p>',
            STEM_SEC,
            ['its', 'it’s', 'their', 'its’'],
            'A',
            'Chủ ngữ là "the Arctic fox" (SỐ ÍT) và cần tính từ sở hữu trước "thick white winter coat" → "its" (không dấu nháy!). Loại "it’s" (= it is), "their" (số nhiều), "its’" (không tồn tại trong tiếng Anh).',
            'Thử thay "it is" vào chỗ trống: "sheds it is thick coat" vô nghĩa → chắc chắn chọn "its" không dấu nháy!',
            [
                ('Đáp án đúng', 'its là tính từ sở hữu số ít khớp với "the Arctic fox".'),
                ('Contraction Trap', 'it’s = it is / it has — sai nghĩa hoàn toàn ở đây.'),
                ('Pronoun Number Mismatch', 'their là số nhiều — không khớp với danh từ số ít "the Arctic fox".'),
                ('Non-Existent Word', 'its’ là dạng sai chính tả không hề tồn tại trong chuẩn tiếng Anh.'),
            ]
        ),
        q_item(
            'd2_4_q4', 4, 'Standard English Conventions', 'Form, Structure, and Sense', 'Hard',
            '<p>Astronomers comparing the atmospheric spectra of two newly discovered exoplanets found that both ______ upper clouds contained unexpectedly high concentrations of silicate dust.</p>',
            STEM_SEC,
            ['planet’s', 'planets', 'planets’s', 'planets’'],
            'D',
            'Phía trước có chữ "both" (cả HAI hành tinh → SỐ NHIỀU!) và phía sau có danh từ thuộc quyền sở hữu "upper clouds" → Cần SỞ HỮU SỐ NHIỀU: planets’ (D)!',
            'Hai câu hỏi chốt dấu nháy trong 3 giây: (1) Có sở hữu từ sau không? (upper clouds → CÓ). (2) Số ít hay số nhiều? (both → SỐ NHIỀU) → `planets’`!',
            [
                ('Singular Possessive Trap', 'planet’s là sở hữu của 1 hành tinh — mâu thuẫn với từ "both" (hai).'),
                ('Missing Possessive', 'planets không có sở hữu cách, làm 2 danh từ "planets upper clouds" đụng nhau vô nghĩa.'),
                ('Non-Standard Plural Possessive', 'Danh từ số nhiều tận cùng bằng -s chỉ thêm dấu nháy (planets’), không thêm -’s.'),
                ('Đáp án đúng', 'planets’ là sở hữu cách số nhiều chuẩn mực cho "both planets’ upper clouds".'),
            ]
        ),
        q_item(
            'd2_4_q5', 5, 'Standard English Conventions', 'Form, Structure, and Sense', 'Hard',
            '<p>Although the symphony orchestra expanded ______ repertoire this season to feature contemporary compositions from East Asia, ticket subscriptions among longtime patrons remained remarkably strong.</p>',
            STEM_SEC,
            ['their', 'its', 'it’s', 'our'],
            'B',
            'Danh từ tiền lệ là "the symphony orchestra" — trên chuẩn SAT Mỹ, danh từ tập hợp (orchestra, committee, team, government, species) LUÔN LÀ SỐ ÍT → chọn tính từ sở hữu số ít "its" (B)!',
            'Danh từ tập hợp số ít trên Digital SAT (team, orchestra, jury, panel, species, museum) → dùng it / its, KHÔNG dùng they / their!',
            [
                ('Collective Noun Trap', 'their là số nhiều — sai chuẩn SAT đối với danh từ tập hợp số ít "the symphony orchestra".'),
                ('Đáp án đúng', 'its (sở hữu số ít) khớp chuẩn với "the symphony orchestra".'),
                ('Contraction Trap', 'it’s = it is — không thể đứng trước danh từ "repertoire".'),
                ('Pronoun Person Shift', 'our (ngôi thứ nhất) lệch ngôi so với chủ ngữ ngôi thứ ba "the orchestra".'),
            ]
        ),
        q_item(
            'd2_4_q6', 6, 'Standard English Conventions', 'Form, Structure, and Sense', 'Elite (750+)',
            '<p>Hydrothermal vents along the Mid-Atlantic Ridge host blind shrimp species ______ specialized dorsal organs detect faint infrared radiation emitted by superheated mineral plumes.</p>',
            STEM_SEC,
            ['who’s', 'whose', 'that’s', 'which'],
            'B',
            'Mối quan hệ giữa "blind shrimp species" và "specialized dorsal organs" là SỞ HỮU (cơ quan cảm biến lưng CỦA loài tôm mù này). Đại từ quan hệ sở hữu "<b>whose</b>" dùng chuẩn mực cho CẢ NGƯỜI LẪN ĐỘNG VẬT/VẬT VÔ TRI trên Digital SAT! Loại "who’s" (= who is) và "which" (không mang nghĩa sở hữu).',
            'Đừng bao giờ loại "whose" chỉ vì tiền lệ là con vật hay đồ vật! Trong Standard English, "whose" là đại từ quan hệ sở hữu chuẩn cho cả người lẫn vật!',
            [
                ('Contraction Trap', 'who’s = who is / who has — sai hoàn toàn về ngữ pháp.'),
                ('Đáp án đúng', 'whose biểu thị sở hữu chuẩn mực ("cơ quan lưng của loài tôm này") cho danh từ chỉ loài vật.'),
                ('Contraction Trap', 'that’s = that is — sai cấu trúc mệnh đề quan hệ sở hữu.'),
                ('Missing Possessive', '"which specialized dorsal organs detect..." không có quan hệ sở hữu và gây lỗi cấu trúc chủ ngữ thừa.'),
            ]
        ),
        q_item(
            'd2_4_q7', 7, 'Standard English Conventions', 'Form, Structure, and Sense', 'Elite (750+)',
            '<p>Acoustic measurements confirmed that the reverberation time of a violin varnished with pine resin is substantially more balanced than ______ coated with modern synthetic lacquer.</p>',
            STEM_SEC,
            ['a violin', 'those of a violin', 'that of a violin', 'violins'],
            'C',
            'Bẫy So Sánh Tương Đồng (Apples-to-Apples Comparison)! Đối tượng đang được so sánh ở vế 1 là "<b>the reverberation time</b>" (thời gian vang âm — SỐ ÍT), KHÔNG phải "a violin"! Do đó sau "than" không thể viết "a violin" (so sánh thời gian với cây đàn!) mà bắt buộc dùng "<b>that of</b> a violin" (= the reverberation time of a violin)!',
            'Gặp so sánh "more/less ... than" hoặc "similar to / unlike": đối chiếu chính xác danh từ bị so sánh ở vế 1 → SỐ ÍT dùng "that of", SỐ NHIỀU dùng "those of"!',
            [
                ('Illogical Comparison', 'So sánh "the reverberation time" (thời gian vang) với "a violin" (cây đàn) là khập khiễng.'),
                ('Pronoun Number Mismatch', '"those of" thay thế cho danh từ số nhiều, nhưng "the reverberation time" là số ít.'),
                ('Đáp án đúng', '"that of a violin" thay thế chính xác cho "the reverberation time of a violin" (số ít).'),
                ('Illogical Comparison', 'So sánh thời gian vang âm với những cây đàn violon — vừa khập khiễng vừa sai số.'),
            ]
        ),
        q_item(
            'd2_4_q8', 8, 'Standard English Conventions', 'Form, Structure, and Sense', 'Hard',
            '<p>In an effort to reduce urban glare without impairing nighttime visibility, municipal lighting engineers replaced sodium-vapor lamps with shielded LED fixtures, recalibrated streetlamp angles, and ______</p>',
            STEM_SEC,
            [
                'dimming sensors were installed along quiet residential avenues.',
                'the installation of dimming sensors along quiet residential avenues.',
                'to install dimming sensors along quiet residential avenues.',
                'installed dimming sensors along quiet residential avenues.'
            ],
            'D',
            'Cấu trúc Song song (Parallelism) cho chuỗi 3 động từ quá khứ đơn cùng chủ ngữ "municipal lighting engineers": (1) replaced..., (2) recalibrated..., and (3) installed... → Duy nhất D đồng dạng động từ quá khứ chủ động!',
            'Khi gặp chuỗi liệt kê A, B, and [C]: gạch chân dạng từ đầu tiên của A và B ("replaced", "recalibrated") rồi chọn đúng dạng đó cho C!',
            [
                ('Broken Parallelism', 'Đột ngột chuyển sang mệnh đề bị động ("dimming sensors were installed") phá vỡ chuỗi động từ chủ động.'),
                ('Broken Parallelism', 'Chuyển thành cụm danh từ ("the installation...") không song song với hai động từ "replaced" và "recalibrated".'),
                ('Broken Parallelism', 'Động từ nguyên mẫu "to install" lệch dạng với hai động từ chia thì quá khứ trước đó.'),
                ('Đáp án đúng', '"installed..." tạo chuỗi 3 động từ quá khứ chủ động song song hoàn hảo: replaced, recalibrated, and installed.'),
            ]
        ),
        q_item(
            'd2_4_q9', 9, 'Standard English Conventions', 'Form, Structure, and Sense', 'Elite (750+)',
            '<p>Curators cataloging the estate noted that the textile ______ woven dyes had faded unevenly along folds exposed to nineteenth-century gallery windows, whereas the interior panels remained vibrant.</p>',
            STEM_SEC,
            ['collections', 'collection’s', 'collections’', 'collection'],
            'B',
            'Nhìn kỹ mạo từ phía trước: "<b>the</b> textile [______] woven dyes". "the textile collection" (SỐ ÍT — một bộ sưu tập dệt may của di sản đó) sở hữu "woven dyes" → Chọn sở hữu số ít `collection’s` (B)! Loại A (số nhiều không sở hữu), C (không có dấu hiệu nhiều bộ sưu tập; "the estate" gợi ý 1 bộ sưu tập của điền trang), D (thiếu sở hữu).',
            'Đọc kỹ ngữ cảnh mạo từ và số lượng ("the estate", "the textile collection’s woven dyes") để chốt sở hữu số ít hay số nhiều.',
            [
                ('Missing Possessive', 'collections không có dấu nháy sở hữu, khiến hai danh từ va nhau.'),
                ('Đáp án đúng', 'collection’s (sở hữu số ít) biểu thị chuẩn xác "thuốc nhuộm dệt của bộ sưu tập vải".'),
                ('Plural Possessive Mismatch', 'Không có chỉ dấu số nhiều nào (như "several / both / multiple") cho nhiều bộ sưu tập.'),
                ('Missing Possessive', 'Thiếu sở hữu cách giữa "collection" và "woven dyes".'),
            ]
        ),
        q_item(
            'd2_4_q10', 10, 'Standard English Conventions', 'Form, Structure, and Sense', 'Hard',
            '<p>Unlike the migratory patterns of monarch butterflies, which span multiple generations across North America, ______ complete their entire 4,000-kilometer round-trip journey within a single individual’s lifetime.</p>',
            STEM_SEC,
            [
                'painted lady butterflies',
                'the migratory patterns of painted lady butterflies',
                'a painted lady butterfly',
                'those of painted lady butterflies'
            ],
            'A',
            'Bẫy So sánh + Hòa hợp động từ kép! Vế đầu so sánh với "the migratory monarchs" (LOÀI BƯỚM — số nhiều), và động từ chính ngay sau chỗ trống là "complete their entire 4,000-kilometer seasonal passage within a single individual’s lifetime" (cần chủ ngữ là loài bướm SỐ NHIỀU). Duy nhất A ("painted lady butterflies") đồng loại với "monarchs" và khớp động từ số nhiều "complete" cùng đại từ "their".',
            'Luôn khớp cả 2 điều kiện cùng lúc: đối tượng so sánh sau "Unlike" phải đồng loại VỚI chủ ngữ sau dấu phẩy, VÀ chủ ngữ đó phải khớp động từ + đại từ phía sau ("complete their").',
            [
                ('Đáp án đúng', 'painted lady butterflies (số nhiều) đồng loại với đối tượng so sánh và khớp trọn vẹn với động từ "complete" cùng đại từ "their".'),
                ('Illogical Subject for Verb', 'Các "patterns" (quy luật di cư) không thể tự "complete their journey within an individual’s lifetime".'),
                ('Number Mismatch', 'a painted lady butterfly là số ít — mâu thuẫn với động từ số nhiều "complete" và đại từ "their".'),
                ('Illogical Reference', 'those thay cho danh từ trừu tượng không thể làm chủ thể có vòng đời cá thể.'),
            ]
        ),
        q_item(
            'd2_4_q11', 11, 'Standard English Conventions', 'Form, Structure, and Sense', 'Elite (750+)',
            '<p>While calibrating the interferometric array, engineers noticed that temperature swings altered the copper cables’ electrical resistance far more abruptly than ______ of the newly installed superconducting fibers.</p>',
            STEM_SEC,
            ['that', 'those', 'it', 'the resistance'],
            'A',
            'Đối tượng đang được so sánh ở vế 1 là "electrical resistance" (điện trở — danh từ KHÔNG ĐẾM ĐƯỢC / SỐ ÍT). Phía sau chỗ trống có sẵn chữ "of" ("______ of the newly installed superconducting fibers") → Chọn đại từ chỉ định số ít "that" (= the electrical resistance). Loại B ("those" = số nhiều), C ("it of") và D ("they of") sai cú pháp.',
            'Khi đề đã có sẵn chữ "of" phía sau chỗ trống (`than ______ of...`), chỉ cần xác định danh từ bị so sánh là SỐ ÍT (`that`) hay SỐ NHIỀU (`those`)!',
            [
                ('Đáp án đúng', '"that" thay thế chuẩn xác cho danh từ số ít không đếm được "electrical resistance" trước giới từ "of".'),
                ('Number Mismatch', '"those" chỉ dùng để thay thế cho danh từ số nhiều.'),
                ('Pronoun Syntax Error', 'Không bao giờ viết "it of..." trong cấu trúc so sánh tiếng Anh.'),
                ('Pronoun Syntax Error', 'Không bao giờ viết "they of..." trong cấu trúc so sánh tiếng Anh.'),
            ]
        ),
        q_item(
            'd2_4_q12', 12, 'Standard English Conventions', 'Form, Structure, and Sense', 'Hard',
            '<p>Despite fierce opposition from nineteenth-century academic painters who dismissed open-air sketching as unfinished, ______ persisted in painting directly outdoors to capture fleeting shifts in natural light.</p>',
            STEM_SEC,
            [
                'Claude Monet’s canvases',
                'the canvases of Claude Monet',
                'Claude Monet and his fellow Impressionists',
                'there were Impressionist painters who'
            ],
            'C',
            'Đọc kỹ động từ chính ngay sau chỗ trống: "______ <b>persisted in painting directly outdoors</b>". Ai mới có thể "kiên trì vẽ ngoài trời"? Chỉ có NGƯỜI ("Claude Monet and his fellow Impressionists") — những tấm toan vẽ (canvases) không thể tự vẽ! Đồng thời tránh cấu trúc rườm rà thiếu động từ chính "there were... who persisted" (làm thừa chủ ngữ hoặc phá vỡ tính trực tiếp).',
            'Luôn ghép thử Chủ ngữ của đáp án trực tiếp với Động từ chính ngay sau chỗ trống ("Canvases persisted in painting?" → Vô lý → Gạch ngay A & B!).',
            [
                ('Possessive Subject Trap', 'Chủ ngữ thật là "canvases" — tranh vẽ không thể tự "kiên trì vẽ ngoài trời".'),
                ('Illogical Subject', '"the canvases" không thể là chủ thể thực hiện hành động "painting outdoors".'),
                ('Đáp án đúng', 'Chủ ngữ chỉ người "Claude Monet and his fellow Impressionists" khớp tuyệt đối với động từ "persisted in painting".'),
                ('Broken Clause Structure', 'Đặt "there were Impressionist painters who" tạo cấu trúc lủng củng và thiếu mạch chủ ngữ trực tiếp sau cụm "Despite...".'),
            ]
        ),
        q_item(
            'd2_4_q13', 13, 'Standard English Conventions', 'Form, Structure, and Sense', 'Hard',
            '<p>Although ______ often credited with inventing the movable-type printing press in Europe, Johannes Gutenberg actually refined earlier metallurgical techniques—including alloy casting and oil-based inks—into a scalable workshop system.</p>',
            STEM_SEC,
            ['hes', 'his', 'he’s', 'they’re'],
            'C',
            'Phía sau chỗ trống là phân từ quá khứ "often credited with..." → Mệnh đề phụ "Although..." cần Chủ ngữ + Động từ to-be (bị động: "he is often credited") → Dạng rút gọn chuẩn là "<b>he’s</b>" (= he is)! Loại "his" (sở hữu, không có động từ to-be), "hes" (thiếu dấu nháy sai chính tả), "they’re" (sai số nhiều so với 1 người "Johannes Gutenberg").',
            'Đừng sợ dạng rút gọn "he’s / it’s / they’re" khi câu THỰC SỰ thiếu động từ to-be! Luôn đọc bung ra ("he is often credited") để kiểm chứng.',
            [
                ('Spelling / Missing Apostrophe', '"hes" không phải từ tiếng Anh hợp lệ.'),
                ('Possessive Trap', '"his often credited" thiếu động từ to-be nên sai hoàn toàn cấu trúc mệnh đề.'),
                ('Đáp án đúng', 'he’s (= he is) cung cấp đúng chủ ngữ số ít + động từ to-be cho cấu trúc bị động "is often credited".'),
                ('Number Mismatch', 'they’re là số nhiều — không khớp với một nhân vật duy nhất "Johannes Gutenberg".'),
            ]
        ),
        q_item(
            'd2_4_q14', 14, 'Standard English Conventions', 'Form, Structure, and Sense', 'Elite (750+)',
            '<p>Designed to harvest drinking water from coastal fog without consuming external electricity, ______ have provided arid Chilean fishing villages with thousands of liters of potable water each week.</p>',
            STEM_SEC,
            [
                'engineers erected fine-mesh polypropylene nets that',
                'the fine-mesh polypropylene nets erected by engineers',
                'fine-mesh polypropylene nets’ ability to condense droplets',
                'collecting water droplets on fine-mesh polypropylene nets'
            ],
            'B',
            'Kiểm tra đồng thời 2 điều kiện: (1) Cụm mở đầu "Designed to harvest drinking water..." mô tả CÁC TẤM LƯỚI (nets), KHÔNG mô tả kỹ sư (A) hay khả năng (C) hay hành động (D); (2) Động từ chính phía sau là "<b>have provided</b>" (SỐ NHIỀU) → Chủ ngữ phải là "the fine-mesh polypropylene <b>nets</b>" (SỐ NHIỀU)! Duy nhất B đạt cả 2 tiêu chuẩn 100%!',
            'Bài toán kép 750+: Kết hợp Modifier Logic (Cái gì được "Designed"?) + Subject-Verb Agreement (SỐ NHIỀU khớp "have provided") → Đáp án lộ diện ngay!',
            [
                ('Dangling Modifier', 'Kỹ sư ("engineers") không phải vật được "thiết kế để thu nước từ sương mù".'),
                ('Đáp án đúng', 'Chủ ngữ số nhiều "the fine-mesh polypropylene nets" vừa khớp cụm "Designed...", vừa khớp động từ số nhiều "have provided".'),
                ('Possessive + Agreement Trap', 'Chủ ngữ thật là "ability" (số ít) — vừa sai modifier vừa không khớp "have provided".'),
                ('Gerund + Agreement Trap', 'Chủ ngữ là hành động "collecting" (số ít) — không phải vật được thiết kế và không khớp "have provided".'),
            ]
        ),
        q_item(
            'd2_4_q15', 15, 'Standard English Conventions', 'Form, Structure, and Sense', 'Elite (750+)',
            '<p>Before retiring from the Royal Botanic Gardens, mycologist Dr. Evelyn Park donated both her hand-annotated field notebooks and ______ to the archive’s digital preservation initiative.</p>',
            STEM_SEC,
            [
                'over four hundred spore prints were collected by her',
                'collecting over four hundred spore prints',
                'over four hundred meticulously labeled spore prints',
                'to label over four hundred spore prints'
            ],
            'C',
            'Cấu trúc tương quan song song: "<b>both</b> [A] <b>and</b> [B]". Thành phần [A] là cụm danh từ "her hand-annotated field notebooks" → Thành phần [B] BẮT BUỘC cũng phải là một cụm danh từ đồng đẳng: "over four hundred meticulously labeled spore prints" (C)!',
            'Nhìn thấy cặp liên từ tương quan (`both A and B`, `not only A but also B`, `either A or B`, `neither A nor B`) → A và B bắt buộc song song tuyệt đối về mặt từ loại!',
            [
                ('Broken Parallelism', 'Đưa cả mệnh đề bị động ("...were collected") ghép với cụm danh từ sau "both... and" là sai cấu trúc.'),
                ('Broken Parallelism', 'Đưa V-ing ("collecting...") không song song với cụm danh từ "field notebooks".'),
                ('Đáp án đúng', 'Cụm danh từ "over four hundred meticulously labeled spore prints" song song tuyệt đối với "her hand-annotated field notebooks".'),
                ('Broken Parallelism', 'Đưa động từ nguyên mẫu "to label" phá vỡ cấu trúc "both [Noun] and [Noun]".'),
            ]
        ),
    ]

    # Self-QA fixups noted during careful authoring of Q10 and Q11 so there is ZERO ambiguity:
    questions[9]['stimulusHtml'] = '<p>Unlike the migratory monarchs of eastern North America, which require up to four successive generations to complete a single annual loop, ______ complete their entire 4,000-kilometer seasonal passage within a single individual’s lifetime.</p>'
    questions[10]['options'][3]['text'] = 'they'

    return {
        'schemaVersion': 1,
        'mode': 'drill',
        'section': 'Reading and Writing',
        'basicInfo': {
            'title': 'Drill 2.4: Form, Structure & Sense II — Modifiers, Possessives & Pronouns (15 Qs)',
            'subtitle': 'Diệt gọn Dangling Modifiers (gồm bẫy Sở hữu cách giả chủ ngữ), Apostrophes, Đại từ tập hợp, So sánh that of/those of và Song song.',
            'difficultyBadge': 'SEC • Target 1500+',
            'targetTimeMinutes': 12,
        },
        'drillModule': {
            'id': 'drill_2_4_mod',
            'title': 'Skill Drill 2.4: Form, Structure & Sense II (Modifiers & Possessives)',
            'timeLimitMinutes': 12,
            'questions': questions,
        },
    }
