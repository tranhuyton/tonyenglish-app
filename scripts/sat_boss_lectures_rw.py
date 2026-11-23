# -*- coding: utf-8 -*-
"""
Digital SAT 1500+ — Hard M2 Boss Masterclass: 4 Elite R&W Lectures (730–800)
- b1: Dense Science Logic & Multi-Variable Mapping (Q11–Q15)
- b2: 50/50 Trap Elimination — The 1-Millimeter Rule (750–800)
- b3: Archaic Literature, 19th-Century Poetry & Dual-Text Nuance
- b4: 32-Minute Time-Triage SOP & Nested Hard Grammar Combos
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from sat_audio_pipeline import build_sat_lecture_html, make_quick_check_html

def get_boss_rw_lectures():
    lectures = []

    # =========================================================================
    # BOSS LECTURE 1: Dense Science Logic & Multi-Variable Mapping (Q11-Q15)
    # =========================================================================
    b1_cards = '''
  <div id="sec-skeleton" class="sat-card lecture-interactive-card" data-lecture-section="skeleton">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>1. Phương pháp "Khung xương 4 Ô" (H → V → R → C) cho đoạn Khoa học dài</h2>
    <p>Tại câu 11–15 Hard Module 2, College Board cố tình nhồi nhét hàng loạt thuật ngữ sinh học, vật lý lượng tử hay cổ sinh vật học (<i>methylation, paleomagnetic susceptibility, epipelagic zooplankton</i>) để khiến thí sinh bị <b>ngợp chữ</b>. Bí quyết của học viên 780–800: <b>ĐỪNG dịch từng danh từ khoa học — hãy thay chúng bằng chữ cái X, Y, Z và chỉ đọc động từ nhân-quả!</b></p>
    <table class="sat-table">
      <thead><tr><th>Ô phân tích</th><th>Câu hỏi cần đặt trong 5 giây</th><th>Ví dụ rút gọn 1 dòng</th></tr></thead>
      <tbody>
        <tr><td><b>H — Hypothesis (Giả thuyết)</b></td><td>Nhà khoa học đang muốn chứng minh hay bác bỏ điều gì?</td><td><i>"X làm tăng Y"</i> hoặc <i>"Chính A chứ không phải B gây ra Y"</i></td></tr>
        <tr><td><b>V — Variables (Biến số)</b></td><td>Nhóm thí nghiệm khác nhóm đối chứng ở điểm nào?</td><td><i>Nhóm 1: có X + có Z | Nhóm 2: chỉ có Z (Control)</i></td></tr>
        <tr><td><b>R — Results (Kết quả)</b></td><td>Dữ liệu thực tế đo được ra sao?</td><td><i>Cả hai nhóm đều tăng Y như nhau!</i></td></tr>
        <tr><td><b>C — Conclusion / Gap</b></td><td>Kết quả ủng hộ hay đập vỡ giả thuyết? Còn biến nhiễu nào?</td><td><i>→ X KHÔNG phải nguyên nhân chính; Z mới là thủ phạm!</i></td></tr>
      </tbody>
    </table>
  </div>

  <div id="sec-confound" class="sat-card lecture-interactive-card" data-lecture-section="confound">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>2. Giải phẫu Biến gây nhiễu (Confounding Variables) &amp; Câu hỏi Support / Weaken</h2>
    <div class="sat-gold-box">
      <b>⭐ Công thức Chốt 100% cho Câu Support &amp; Weaken (750–800):</b>
      <br>• <b>Để SUPPORT (Ủng hộ giả thuyết "X gây ra Y"):</b> Đáp án đúng phải <b>loại trừ nguyên nhân thay thế Z</b>, hoặc chỉ ra <b>nhóm có X thay đổi Y mạnh hơn rõ rệt so với nhóm đối chứng không có X</b>.
      <br>• <b>Để WEAKEN / UNDERMINE (Làm suy yếu giả thuyết "X gây ra Y"):</b> Đáp án đúng phải chỉ ra 1 trong 3 lỗ hổng:
      <br>&nbsp;&nbsp;1. <b>Biến nhiễu (Confounder):</b> Nhóm có X vô tình có luôn yếu tố Z (VD: nhiệt độ cao hơn, giống loài khác).
      <br>&nbsp;&nbsp;2. <b>Không có khác biệt so với Control:</b> Nhóm KHÔNG có X cũng xảy ra kết quả Y y hệt!
      <br>&nbsp;&nbsp;3. <b>Đảo chiều nhân-quả (Reverse Causality):</b> Chính Y xuất hiện trước và gây ra X!
    </div>
    <div class="sat-trap-box">
      <b>🚨 Bẫy kinh điển Q13–Q14 (Quantitative Science):</b> Đáp án A và C đọc đều <b>chính xác 100% theo bảng số liệu</b>, nhưng một đáp án chỉ nhắc tới 1 nhóm đơn lẻ mà <b>KHÔNG tạo ra phép so sánh chứng minh giả thuyết</b>. Luôn kiểm tra 2 tầng: (1) Đúng số liệu bảng, VÀ (2) Trúng đúng logic giả thuyết!
    </div>
  </div>

  <div id="sec-infer-chain" class="sat-card lecture-interactive-card" data-lecture-section="infer_chain">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>3. Chuỗi Suy luận Khoa học nhiều bước (Multi-Step Inferences — Q15 Boss)</h2>
    <div class="sat-ex-box">
      <b>Mô hình Q15 Hard M2 thường gặp:</b>
      <br>Câu 1: Loài A phát ra hợp chất X để đẩy lùi côn trùng P.<br>
      Câu 2: Loài B mọc gần loài A nhưng <b>không tự tổng hợp được X</b>, vậy mà vẫn ít bị P cắn khi trồng sát loài A.<br>
      Câu 3: Tuy nhiên, khi trồng loài B trong nhà kính tách biệt bằng vách ngăn kín khí cạnh loài A, loài B lại bị P tấn công nặng.<br>
      → <b>Suy luận 1 milimét:</b> Loài B chỉ nhận được sự bảo vệ nhờ <b>hợp chất X khuếch tán qua không khí (airborne transmission)</b> từ loài A (KHÔNG phải qua rễ hay do loài B đột biến gen!).
    </div>
    <div class="sat-rule-box">
      <b>⚡ Quy tắc Vàng "Đánh dấu chữ However / Yet / By contrast":</b> Trong câu 15 Hard M2, 85% manh mối quyết định nằm ngay ở <b>2 câu cuối cùng sau từ nối tương phản</b>. Hãy đọc kỹ xem yếu tố nào bị loại bỏ ở thí nghiệm phụ (như "vách ngăn kín khí") — chính yếu tố bị chặn đó là câu trả lời!
    </div>
  </div>
'''
    b1_qc = make_quick_check_html(
        'qc_b1',
        'Đáp án nào làm SUY YẾU (undermine) mạnh nhất kết luận của nhóm nghiên cứu?',
        'Biologists hypothesized that alpine marmots hibernate earlier solely because daytime temperatures drop below 5°C in autumn. In a field study, marmots at Site A (where temperatures fell below 5°C in September) began hibernating three weeks earlier than marmots at Site B (where temperatures stayed above 10°C until October). However, the researchers did not measure snowpack depth or seed availability at either site.',
        [
            'Marmots at Site A were slightly heavier on average than marmots at Site B during spring.',
            'At Site A, a late-summer drought depleted edible grasses and seeds in early September, whereas food remained abundant at Site B until October.',
            'Previous studies showed that lowland rodents also respond strongly to seasonal shifts in temperature.',
            'Temperatures at Site B occasionally dropped to 6°C during nighttime storms in late September.',
        ],
        1,
        'Giả thuyết dùng từ cực đoan "solely because daytime temperatures drop" (chỉ do nhiệt độ). Đáp án B đưa ra một BIẾN GÂY NHIỄU (Confounding Variable) trực tiếp giải thích tại sao Site A ngủ đông sớm hơn 3 tuần: hạn hán làm cạn kiệt nguồn thức ăn ở Site A đầu tháng 9, trong khi Site B vẫn dồi dào thức ăn tới tháng 10!'
    )
    b1_html = build_sat_lecture_html(
        '🔥 HARD M2 BOSS MASTERCLASS • R&W BOSS 1 (730–800)',
        'R&W Boss 1: Dense Science Logic & Multi-Variable Mapping',
        'Giải phẫu các câu Khoa học mật độ cao khó nhất ở Q11–Q15 Hard Module 2: đọc khung xương X–Y–Z, bắt biến gây nhiễu và xử lý suy luận thí nghiệm nhiều bước.',
        [
            'Đọc xuyên qua thuật ngữ khoa học dày đặc bằng Khung xương 4 ô (H → V → R → C) thay thế thuật ngữ bằng X, Y, Z.',
            'Nhận diện ngay 3 kiểu đòn Weaken (Confounder, Control Match, Reverse Causality) và bẫy đúng-số-liệu-nhưng-lạc-luận ở Q13–Q14.',
            'Khóa chuẩn câu Inference Q15 bằng phương pháp đối chiếu biến số bị chặn ở thí nghiệm phụ.',
        ],
        b1_cards,
        b1_qc
    )
    b1_segs = [
        {
            'id': 'intro',
            'title': 'Tổng quan R&W Boss 1: Khoa học mật độ cao',
            'selector': '#sec-header',
            'en': 'Welcome to the Hard Module Two Boss Masterclass! Questions eleven through fifteen on Hard Reading and Writing are where 1450 scorers get separated from 1550 plus scorers. Today we turn dense, intimidating scientific passages into simple X, Y, and Z causal chains.',
            'vi': 'Chào mừng bạn đến với chuỗi bài giảng chuyên sâu Hard Module 2 Boss Masterclass! Cụm câu 11 đến 15 phần Reading and Writing Hard chính là nơi phân tách mốc 1450 với mốc 1550 trở lên. Hôm nay ta sẽ biến những đoạn khoa học dày đặc thuật ngữ thành sơ đồ nhân quả X, Y, Z cực kỳ đơn giản.'
        },
        {
            'id': 'skeleton',
            'title': 'Khung xương 4 ô H-V-R-C',
            'selector': '#sec-skeleton',
            'en': 'Never waste precious seconds trying to pronounce or translate intimidating scientific jargon. Replace complex chemical or biological names with simple placeholders like X, Y, and Z, and map four boxes in your head: the Hypothesis, the experimental Variables, the measured Results, and the logical Conclusion.',
            'vi': 'Đừng bao giờ phí giây quý giá để dịch hay đánh vần những thuật ngữ sinh hóa dài ngoằng. Hãy thay thế tên khoa học phức tạp bằng X, Y, Z và dựng nhanh 4 ô trong đầu: Giả thuyết, Biến thí nghiệm, Kết quả đo được và Kết luận logic.'
        },
        {
            'id': 'confound',
            'title': 'Biến gây nhiễu & Đòn Support/Weaken',
            'selector': '#sec-confound',
            'en': 'To weaken a causal claim that X causes Y, look for one of three attacks: a confounding variable Z that changed alongside X, a control group without X that still produced Y, or reverse causality where Y actually caused X. On quantitative charts, verify both factual accuracy and logical relevance to the claim.',
            'vi': 'Để làm suy yếu giả thuyết X gây ra Y, hãy săn đúng một trong ba đòn đánh: một biến gây nhiễu Z thay đổi song hành cùng X, nhóm đối chứng không có X nhưng vẫn ra kết quả Y, hoặc đảo ngược nhân quả khi Y mới là nguyên nhân gây ra X. Với câu bảng biểu số liệu, luôn kiểm tra cả hai tầng: đúng số và trúng luận điểm.'
        },
        {
            'id': 'infer_chain',
            'title': 'Suy luận nhiều bước ở Q15',
            'selector': '#sec-infer-chain',
            'en': 'On the toughest inference questions, compare the main experiment with the follow-up test introduced after words like however or yet. Whatever specific pathway was blocked or altered in the second condition is almost always the exact mechanism that fills the final blank.',
            'vi': 'Ở câu suy luận khó nhất Q15, hãy so sánh thí nghiệm chính với thí nghiệm phụ xuất hiện ngay sau các từ nối tương phản như however hoặc yet. Chính cơ chế bị chặn lại hoặc bị thay đổi ở điều kiện thứ hai hầu như luôn là mảnh ghép điền vào chỗ trống cuối cùng.'
        }
    ]
    lectures.append({
        'code': 'b1',
        'module_key': 'boss_m10',
        'order_index': 1,
        'title': 'R&W Boss 1: Dense Science Logic & Multi-Variable Mapping',
        'drill_key': 'boss_drill_1',
        'html': b1_html,
        'segments': b1_segs,
        'major_sections': [
            {'title': 'Khung xương 4 ô H-V-R-C', 'startSegmentId': 'skeleton'},
            {'title': 'Biến gây nhiễu & Support/Weaken', 'startSegmentId': 'confound'},
            {'title': 'Suy luận Q15 nhiều bước', 'startSegmentId': 'infer_chain'},
        ],
    })

    # =========================================================================
    # BOSS LECTURE 2: 50/50 Trap Elimination — The 1-Millimeter Rule (750–800)
    # =========================================================================
    b2_cards = '''
  <div id="sec-anatomy" class="sat-card lecture-interactive-card" data-lecture-section="anatomy">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>1. Giải phẫu 5 Cái bẫy "Lệch 1 Milimét" ở tình huống 50/50</h2>
    <p>Khi học viên đã đạt 700+, bạn gần như luôn loại được 2 đáp án sai rõ ràng — nhưng lại mất điểm ở <b>cuộc đấu tay đôi 50/50 giữa 2 đáp án còn lại</b>. Đáp án bẫy ở band 750–800 thường đúng tới <b>90% nội dung</b>, nhưng gài đúng <b>1 từ sai chết người</b>:</p>
    <table class="sat-table">
      <thead><tr><th>Tên Bẫy 750+</th><th>Dấu hiệu nhận diện trong 1 giây</th><th>Ví dụ lệch 1 milimét</th></tr></thead>
      <tbody>
        <tr><td><b>1. One-Word Extremity</b></td><td><code>solely, exclusively, entirely, always, never, proved</code></td><td>Bài viết nói "partially contributed" → Bẫy viết "was the sole driver".</td></tr>
        <tr><td><b>2. Unstated Comparison</b></td><td><code>more than, faster than, superior to, primarily</code></td><td>Bài nhắc cả A và B đều hiệu quả, KHÔNG so sánh cái nào hơn → Bẫy viết "A is more effective than B"!</td></tr>
        <tr><td><b>3. Reverse Direction</b></td><td>Đảo ngược chủ thể – đối tượng hoặc nguyên nhân – kết quả</td><td>Bài nói "nhiệt độ làm đổi màu vỏ" → Bẫy viết "màu vỏ làm thay đổi nhiệt độ".</td></tr>
        <tr><td><b>4. Half-Right / Half-Wrong</b></td><td>Nửa đầu trích cực trúng bài, <b>nửa cuối sau dấu phẩy tự bịa thêm</b></td><td>Luôn đọc tới <b>từ cuối cùng</b> của đáp án trước khi chọn!</td></tr>
        <tr><td><b>5. Collocation &amp; Degree (WIC)</b></td><td>2 từ gần nghĩa nhưng khác sắc thái/đối tượng kết hợp</td><td><code>mitigate</code> (giảm nhẹ tác hại) vs <code>eradicate</code> (xóa sổ hoàn toàn); <code>skeptical</code> vs <code>hostile</code>.</td></tr>
      </tbody>
    </table>
  </div>

  <div id="sec-method" class="sat-card lecture-interactive-card" data-lecture-section="method">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>2. Kỹ thuật "Soi Kính Lúp Đối Đầu" (Head-to-Head Diff Check)</h2>
    <div class="sat-rule-box">
      <b>🎯 Khi phân vân giữa 2 đáp án B và D, TUYỆT ĐỐI KHÔNG đọc lại cả đoạn văn từ đầu một cách mù quáng!</b>
      <br>Hãy làm đúng 3 bước trong 15 giây:
      <br><b>Bước 1 (Tìm điểm khác biệt):</b> Khoanh chính xác <b>2–3 từ mà B và D khác nhau</b> (VD: B dùng <i>"cautiously questioned"</i>, D dùng <i>"firmly rejected"</i>).
      <br><b>Bước 2 (Đối chiếu bằng chứng nguyên văn):</b> Quay lên đoạn văn tìm đúng 1 câu nhắc đến chi tiết đó — tác giả thực sự "nghi ngờ thận trọng" hay "bác bỏ hoàn toàn"?
      <br><b>Bước 3 (Loại đáp án có từ không chứng minh được):</b> Nguyên tắc vàng của College Board là <b>100% Every Word Must Be Supported</b> — đáp án nào chứa dù chỉ 1 chi tiết phải "đoán thêm" là BẪY!
    </div>
  </div>

  <div id="sec-wic750" class="sat-card lecture-interactive-card" data-lecture-section="wic750">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>3. Bộ 8 Cặp từ Nghĩa Thứ Cấp (Secondary Meanings) hay lừa nhất Hard M2</h2>
    <div class="sat-gold-box">
      <b>⭐ Thuộc lòng 8 "Sát thủ từ vựng" của Q1–Q5 Hard Module 2:</b>
      <br>• <b>temper (v):</b> làm dịu bớt, tiết chế (= moderate) — <i>KHÔNG phải nổi nóng!</i>
      <br>• <b>check (v):</b> kiềm chế, chặn đà tăng (= restrain/halt) — <i>VD: check inflation</i>.
      <br>• <b>qualify (v):</b> đặt giới hạn, bổ sung điều kiện cho một tuyên bố (= limit/moderate).
      <br>• <b>wanting (adj):</b> thiếu hụt, không đạt chuẩn (= lacking/deficient) — <i>VD: found wanting</i>.
      <br>• <b>pedestrian (adj):</b> tẻ nhạt, tầm thường (= dull/unimaginative) — <i>KHÔNG phải người đi bộ!</i>
      <br>• <b>novel (adj):</b> mới lạ, độc đáo (= original/innovative) — <i>KHÔNG phải tiểu thuyết!</i>
      <br>• <b>arresting (adj):</b> thu hút mạnh mẽ sự chú ý (= striking/captivating).
      <br>• <b>credit (v):</b> công nhận, tin tưởng vào tính xác thực (= believe/attribute).
    </div>
  </div>
'''
    b2_qc = make_quick_check_html(
        'qc_b2',
        'Soi kính lúp 50/50 — Đáp án nào được đoạn văn CHỨNG MINH 100% mà không lệch 1 milimét?',
        'Although marine ecologist Dr. Lin’s 2023 survey documented higher juvenile fish counts near artificial basalt reefs than near bare sandy seabeds, she noted that the study lasted only nine months and could not determine whether the reefs increased overall regional fish populations or merely attracted fish away from nearby natural outcrops.',
        [
            'Dr. Lin proved that artificial basalt reefs increase total regional fish populations more effectively than natural outcrops do.',
            'Dr. Lin’s findings are compatible with the possibility that artificial basalt reefs redistribute existing fish rather than raising regional fish totals.',
            'Dr. Lin concluded that artificial basalt reefs harm nearby natural outcrops by drawing away all of their juvenile fish.',
            'Because the survey lasted only nine months, Dr. Lin dismissed her finding of higher juvenile fish counts near basalt reefs as invalid.',
        ],
        1,
        'Soi từng bẫy 1 milimét: A sai vì "proved" + "more effectively" (ngược hẳn với "could not determine"); C sai vì từ cực đoan "harm" và "all" không có trong bài; D sai vì "dismissed... as invalid" (bà không phủ nhận số liệu đếm được, chỉ giới hạn kết luận). B khớp tuyệt đối 100% với sắc thái thận trọng "compatible with the possibility that... redistribute existing fish"!'
    )
    b2_html = build_sat_lecture_html(
        '🔥 HARD M2 BOSS MASTERCLASS • R&W BOSS 2 (750–800)',
        'R&W Boss 2: 50/50 Trap Elimination — The 1-Millimeter Rule',
        'Làm chủ kỹ thuật phân xử tình huống 50/50 trong 15 giây: giải phẫu 5 bẫy lệch 1 milimét và bộ 8 từ vựng nghĩa thứ cấp sát thủ nhất Hard Module 2.',
        [
            'Nhận diện tức thì 5 bẫy tinh vi nhất ở band 750–800: One-Word Extremity, Unstated Comparison, Reverse Direction, Half-Right và Collocation Mismatch.',
            'Áp dụng quy trình Head-to-Head Diff Check 3 bước để dứt điểm câu phân vân 50/50 mà không mất thời gian đọc lại toàn bài.',
            'Thuộc lòng 8 từ vựng nghĩa thứ cấp (temper, check, qualify, wanting, pedestrian, novel, arresting, credit) chuyên xuất hiện ở Q1–Q5 Hard M2.',
        ],
        b2_cards,
        b2_qc
    )
    b2_segs = [
        {
            'id': 'intro',
            'title': 'Tổng quan Phá bẫy 50/50 (750–800)',
            'selector': '#sec-header',
            'en': 'Almost every high-scoring SAT student knows the frustration of narrowing a question down to two tempting choices and picking the wrong one. On Hard Module Two, the runner-up trap is designed to look ninety percent right while hiding a single fatal distortion.',
            'vi': 'Hầu như học sinh điểm cao nào cũng từng trải qua cảm giác cay đắng khi loại còn đúng 2 đáp án 50/50 rồi lại chọn nhầm câu bẫy. Ở Hard Module 2, đáp án nhiễu hạng hai được thiết kế đúng tới 90 phần trăm nhưng gài đúng một từ lệch chết người.'
        },
        {
            'id': 'anatomy',
            'title': '5 Cái bẫy Lệch 1 Milimét',
            'selector': '#sec-anatomy',
            'en': 'Memorize the five classic 750-plus traps: first, one-word extremity like solely or proved; second, an unstated comparison claiming A is greater than B when the passage never ranked them; third, reverse causal direction; fourth, half-right choices that sneak an unsupported claim after the final comma; and fifth, collocation mismatches in Words in Context.',
            'vi': 'Hãy khắc cốt ghi tâm 5 cái bẫy kinh điển của vùng 750 cộng: một là từ cực đoan như solely hay proved; hai là so sánh ngầm không có trong bài kiểu A hơn B; ba là đảo ngược chiều nhân quả; bốn là bẫy nửa đầu đúng nhưng nửa cuối sau dấu phẩy tự suy diễn thêm; và năm là từ đồng nghĩa nhưng sai ngữ cảnh kết hợp.'
        },
        {
            'id': 'method',
            'title': 'Kỹ thuật Soi Kính Lúp Đối Đầu',
            'selector': '#sec-method',
            'en': 'When stuck between two finalists, stop rereading the entire passage. Instead, run a Head-to-Head Diff Check: isolate the exact two or three words where Choice B and Choice D disagree, check that exact detail in the text, and eliminate whichever choice contains even a single word you have to guess or stretch to justify.',
            'vi': 'Khi phân vân giữa hai đáp án cuối, đừng đọc lại cả bài một cách dàn trải. Thay vào đó, hãy soi kính lúp đối đầu: khoanh đúng 2 đến 3 từ mà hai đáp án khác nhau, đối chiếu đúng chi tiết đó trong bài và loại thẳng đáp án nào chứa dù chỉ một từ khiến bạn phải tự suy diễn thêm.'
        },
        {
            'id': 'wic750',
            'title': '8 Từ vựng Nghĩa thứ cấp sát thủ',
            'selector': '#sec-wic750',
            'en': 'Finally, watch for classic secondary meanings on Hard Words in Context: temper means to moderate, check means to restrain, qualify means to limit a claim, wanting means lacking, pedestrian means dull, novel means original, arresting means striking, and credit means to believe or attribute.',
            'vi': 'Cuối cùng, hãy nằm lòng 8 nghĩa thứ cấp sát thủ hay xuất hiện nhất: temper là tiết chế, check là kiềm chế chặn lại, qualify là đặt giới hạn cho nhận định, wanting là thiếu hụt, pedestrian là tẻ nhạt, novel là mới lạ, arresting là cuốn hút mạnh mẽ và credit là tin tưởng hoặc quy công trạng.'
        }
    ]
    lectures.append({
        'code': 'b2',
        'module_key': 'boss_m10',
        'order_index': 2,
        'title': 'R&W Boss 2: 50/50 Trap Elimination — The 1-Millimeter Rule',
        'drill_key': 'boss_drill_2',
        'html': b2_html,
        'segments': b2_segs,
        'major_sections': [
            {'title': '5 Bẫy lệch 1 milimét', 'startSegmentId': 'anatomy'},
            {'title': 'Soi kính lúp đối đầu 50/50', 'startSegmentId': 'method'},
            {'title': '8 Từ nghĩa thứ cấp Hard M2', 'startSegmentId': 'wic750'},
        ],
    })

    # =========================================================================
    # BOSS LECTURE 3: Archaic Literature, 19th-Century Poetry & Dual-Text Nuance
    # =========================================================================
    b3_cards = '''
  <div id="sec-poetry" class="sat-card lecture-interactive-card" data-lecture-section="poetry">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>1. Giải mã Thơ thế kỷ 18–19 &amp; Văn xuôi cổ Đảo ngữ (Syntax Unscrambling)</h2>
    <p>Học sinh quốc tế hay mất bình tĩnh nhất khi gặp một khổ thơ cổ hoặc trích đoạn tiểu thuyết thế kỷ 19 vì câu bị <b>đảo trật tự Chủ–Vị</b> và có nhiều hình ảnh ẩn dụ. Đừng dừng lại ở từng dòng thơ — hãy dùng <b>3 bước "Duỗi thẳng câu"</b>:</p>
    <div class="sat-rule-box">
      <b>1. Đọc theo DẤU CÂU (Punctuation), KHÔNG dừng ở cuối dòng thơ (Enjambment):</b> Một ý thơ thường vắt qua 2–3 dòng cho tới khi gặp dấu chấm hoặc chấm phẩy.<br>
      <b>2. Tìm bộ khung S + V gốc:</b> Gạt bỏ các cụm giới từ chen giữa (<i>"Across the frost-bound meadow, where no footfall rings, the lantern..."</i> → Chủ ngữ gốc là <b>the lantern</b>!).<br>
      <b>3. Gắn nhãn Cảm xúc (Tone Tag: +, −, hay Chuyển biến + → −):</b> Trong 90% câu thơ SAT, chỉ cần bắt đúng <b>sự chuyển biến thái độ</b> (VD: từ <i>nostalgic admiration</i> sang <i>quiet resignation</i>) là loại ngay được 3 đáp án sai!
    </div>
  </div>

  <div id="sec-lit-ev" class="sat-card lecture-interactive-card" data-lecture-section="lit_ev">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>2. Trích dẫn Văn học (Literary Quotations) — Quy tắc "Bắt đúng Tính từ Cốt lõi"</h2>
    <div class="sat-gold-box">
      <b>⭐ Chiến thuật 10 giây cho Literary Command of Evidence:</b>
      <br>Đề bài luôn cho sẵn một nhận định học thuật về nhân vật/tác phẩm (VD: <i>"the narrator feels <b>both fascinated by and uneasy about</b> the estate's silence"</i>).
      <br>• Gạch chân <b>MỌI thành phần của nhận định</b> (ở ví dụ trên phải có ĐỦ 2 vế: vừa <b>fascinated [+]</b> VỪA <b>uneasy [−]</b>!).
      <br>• Đáp án bẫy thường chỉ minh họa được <b>1 nửa</b> (chỉ thấy đẹp mà không thấy bất an) hoặc khớp sai đối tượng (nhân vật khác mới thấy bất an!).
    </div>
  </div>

  <div id="sec-dual" class="sat-card lecture-interactive-card" data-lecture-section="dual">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>3. Dual-Text Hard M2 (Q8): Phân biệt "Bác bỏ toàn phần" vs "Bổ sung/Thu hẹp phạm vi"</h2>
    <p>Ở Module 1, Text 1 và Text 2 thường đối lập trắng–đen (Ủng hộ vs Phản đối). Nhưng ở <b>Hard Module 2</b>, mối quan hệ giữa 2 văn bản tinh tế hơn rất nhiều:</p>
    <table class="sat-table">
      <thead><tr><th>Quan hệ Dual-Text Hard M2</th><th>Bản chất</th><th>Từ khóa chuẩn trong Đáp án đúng</th></tr></thead>
      <tbody>
        <tr><td><b>Qualified Agreement (Đồng tình có điều kiện)</b></td><td>Text 2 đồng ý với phát hiện của Text 1 nhưng cảnh báo giới hạn/ngoại lệ</td><td><code>acknowledges... but cautions that / qualifies / narrows the scope</code></td></tr>
        <tr><td><b>Shared Premise, Different Mechanism</b></td><td>Cùng công nhận hiện tượng Y, nhưng giải thích nguyên nhân khác nhau</td><td><code>agrees that Y occurs, but attributes it to Z rather than X</code></td></tr>
        <tr><td><b>Methodological Critique</b></td><td>Text 2 không nói kết luận của Text 1 sai hẳn, mà chỉ ra phương pháp đo chưa đủ bằng chứng</td><td><code>questions whether the evidence is sufficient / points out a confounding factor</code></td></tr>
      </tbody>
    </table>
    <div class="sat-trap-box">
      <b>🚨 Bẫy Dual-Text kinh điển:</b> Đề hỏi <i>"How would the author of Text 2 most likely respond to the claim in Text 1?"</i> — hãy kiểm tra kỹ chiều mũi tên <b>Text 2 → Text 1</b> (KHÔNG đảo ngược sang Text 1 đánh giá Text 2!).
    </div>
  </div>
'''
    b3_qc = make_quick_check_html(
        'qc_b3',
        'Đoạn văn nào thể hiện đúng nhất mối quan hệ giữa Text 2 và Text 1?',
        '<b>Text 1:</b> Art historians have long attributed the luminous blue skies in sixteenth-century Venetian altarpieces primarily to the city’s privileged maritime access to imported Afghan lapis lazuli.<br><br><b>Text 2:</b> While chemical spectroscopy confirms that Venetian workshops possessed abundant lapis lazuli, conservator Clara Moretti’s pigment cross-sections reveal that painters achieved their signature luminosity not through raw mineral purity alone, but by layering translucent oil glazes over finely ground chalk undercoats.',
        [
            'Text 2 disputes Text 1’s claim that sixteenth-century Venetian workshops had access to imported lapis lazuli.',
            'Text 2 concedes the availability of lapis lazuli noted in Text 1 but argues that layering technique was essential to producing the luminous effect.',
            'Text 2 argues that chalk undercoats were far more expensive to import than Afghan lapis lazuli.',
            'Text 2 concludes that sixteenth-century Venetian altarpieces were actually less luminous than earlier Florentine paintings.',
        ],
        1,
        'Text 2 mở đầu bằng "While chemical spectroscopy confirms that Venetian workshops possessed abundant lapis lazuli" (nhượng bộ đồng ý về nguồn cung đá quý trong Text 1 — loại ngay A!), rồi bổ sung cơ chế quyết định là kỹ thuật phủ lớp men dầu trên nền phấn → Qualified Agreement / Different Mechanism → B chính xác 100%!'
    )
    b3_html = build_sat_lecture_html(
        '🔥 HARD M2 BOSS MASTERCLASS • R&W BOSS 3 (750–800)',
        'R&W Boss 3: Archaic Literature, 19th-Century Poetry & Dual-Text Nuance',
        'Gỡ rối triệt để thơ cổ đảo ngữ, câu trích dẫn văn học 2 vế và các quan hệ nhượng bộ tinh vi giữa Text 1 – Text 2 trong Hard Module 2.',
        [
            'Đọc xuyên qua đảo ngữ thơ thế kỷ 18–19 bằng quy tắc đọc theo dấu câu và bắt đường cong cảm xúc (Tone Shift).',
            'Kiểm tra đủ 100% các vế tính từ trong nhận định để chọn trích dẫn văn học không bị sập bẫy "đúng 1 nửa".',
            'Phân biệt chuẩn 3 mô hình Dual-Text 750+: Qualified Agreement, Shared Premise–Different Mechanism và Methodological Critique.',
        ],
        b3_cards,
        b3_qc
    )
    b3_segs = [
        {
            'id': 'intro',
            'title': 'Tổng quan Văn học cổ, Thơ & Dual-Text',
            'selector': '#sec-header',
            'en': 'Nineteenth-century poetry, archaic prose, and nuanced Dual-Text passages intimidate even fluent English readers. Yet you do not need to be a literature professor to ace them—you just need a systematic decoding method.',
            'vi': 'Thơ thế kỷ 19, văn xuôi cổ đảo ngữ và các đoạn Dual-Text tinh tế có thể làm chùn bước cả những thí sinh tiếng Anh rất giỏi. Nhưng bạn không cần là giáo sư văn học để lấy trọn điểm — bạn chỉ cần một quy trình giải mã có hệ thống.'
        },
        {
            'id': 'poetry',
            'title': 'Duỗi thẳng cú pháp Thơ & Văn cổ',
            'selector': '#sec-poetry',
            'en': 'When reading poetry, never stop at line breaks—follow the punctuation until a period or semicolon ends the sentence. Strip away interrupting prepositional phrases to locate the core subject and verb, and label the emotional shift from beginning to end. That tone shift alone eliminates three wrong answers almost immediately.',
            'vi': 'Khi đọc thơ, tuyệt đối đừng dừng mắt ở cuối dòng thơ mà hãy đọc liền mạch theo dấu chấm và chấm phẩy. Gạt bỏ các cụm giới từ chen ngang để bắt đúng chủ ngữ và động từ chính, đồng thời gắn nhãn sự chuyển biến cảm xúc từ đầu tới cuối khổ thơ.'
        },
        {
            'id': 'lit_ev',
            'title': 'Trích dẫn văn học 2 vế',
            'selector': '#sec-lit-ev',
            'en': 'For literary quotation questions, underline every key adjective or tension in the prompt claim. If the claim states that a character feels both admiration and unease, a quotation showing only admiration is a half-right trap. The right quote must deliver every single element of the claim.',
            'vi': 'Với câu chọn trích dẫn văn học, hãy gạch chân mọi tính từ hoặc sắc thái kép trong nhận định đề cho. Nếu nhận định nói nhân vật vừa ngưỡng mộ vừa bất an, câu trích dẫn chỉ thể hiện sự ngưỡng mộ chính là bẫy đúng một nửa. Đáp án chuẩn phải khớp trọn vẹn tất cả các vế.'
        },
        {
            'id': 'dual',
            'title': 'Quan hệ Dual-Text tinh tế ở Hard M2',
            'selector': '#sec-dual',
            'en': 'On Hard Module Two, Text Two rarely calls Text One completely false. Instead, look for qualified agreement, a shared observation explained by a different mechanism, or a methodological critique pointing out insufficient evidence. Always double-check the direction of the question: is Text Two responding to Text One, or vice versa?',
            'vi': 'Trên Hard Module 2, Text 2 hiếm khi bác bỏ sạch trơn Text 1. Thay vào đó hãy chú ý ba mô hình tinh vi: đồng tình có điều kiện, cùng hiện tượng nhưng khác cơ chế giải thích, hoặc phê bình phương pháp nghiên cứu thiếu bằng chứng. Luôn kiểm tra đúng chiều câu hỏi đang xét Text 2 phản hồi Text 1 hay ngược lại.'
        }
    ]
    lectures.append({
        'code': 'b3',
        'module_key': 'boss_m10',
        'order_index': 3,
        'title': 'R&W Boss 3: Archaic Literature, 19th-Century Poetry & Dual-Text Nuance',
        'drill_key': 'boss_drill_3',
        'html': b3_html,
        'segments': b3_segs,
        'major_sections': [
            {'title': 'Giải mã Thơ & Văn xuôi cổ', 'startSegmentId': 'poetry'},
            {'title': 'Trích dẫn văn học đủ vế', 'startSegmentId': 'lit_ev'},
            {'title': '3 Mô hình Dual-Text 750+', 'startSegmentId': 'dual'},
        ],
    })

    # =========================================================================
    # BOSS LECTURE 4: 32-Minute Time-Triage SOP & Nested Hard Grammar Combos
    # =========================================================================
    b4_cards = '''
  <div id="sec-triage" class="sat-card lecture-interactive-card" data-lecture-section="triage">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>1. Chiến thuật Đảo thứ tự 32 Phút (The 1500+ Reverse-Order Triage SOP)</h2>
    <p>Sai lầm số 1 khiến học viên 1450 hụt hơi ở Hard Module 2: làm tuần tự Q1 → Q27, kẹt 12 phút ở cụm Reading Q10–Q15 rồi đến 3 phút cuối phải <b>khoanh bừa Q20–Q27 (những câu Grammar &amp; Notes dễ ăn điểm nhất!)</b>.</p>
    <div class="sat-gold-box">
      <b>⭐ Lộ trình 3 chặng chuẩn 780–800 trong 32 phút:</b>
      <br>• <b>Chặng 1 (Phút 0–4):</b> Làm sạch <b>Q1–Q5 (Words in Context)</b> — ~40 giây/câu.
      <br>• <b>Chặng 2 (Phút 4–12):</b> Bấm Question Navigator <b>nhảy thẳng tới Q16–Q27</b> (Boundaries, Form/Structure, Transitions, Rhetorical Synthesis) — 12 câu quy tắc cứng làm cực nhanh (~35–40 giây/câu), khóa chắc 12/12 điểm!
      <br>• <b>Chặng 3 (Phút 12–32):</b> Dành trọn <b>20 phút thảnh thơi cho 10 câu Reading nặng nhất (Q6–Q15)</b> — tức hẳn <b>2 phút/câu</b>! Gặp câu nào quá 90 giây chưa thông, bấm <b>Mark for Review</b> + chọn tạm 1 phương án để quay lại sau.
    </div>
  </div>

  <div id="sec-nested" class="sat-card lecture-interactive-card" data-lecture-section="nested">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>2. 4 Combo Ngữ pháp "Xếp tầng" hay gài bẫy nhất ở Q16–Q22 Hard M2</h2>
    <table class="sat-table">
      <thead><tr><th>Combo Ngữ pháp Hard M2</th><th>Bẫy thường gặp</th><th>Quy tắc phá bẫy 5 giây</th></tr></thead>
      <tbody>
        <tr><td><b>1. Super-Comma (Dấu chấm phẩy trong danh sách)</b></td><td>Thấy dấu <code>;</code> tưởng nối 2 mệnh đề độc lập rồi loại oan!</td><td>Khi các mục trong liệt kê <b>đã chứa dấu phẩy bên trong</b> (VD: <i>Paris, France; Kyoto, Japan; and Lima, Peru</i>), dấu <code>;</code> đóng vai trò phân tách mục liệt kê!</td></tr>
        <tr><td><b>2. Inverted Subject–Verb</b></td><td>Nhìn danh từ đứng ngay trước động từ tưởng là chủ ngữ</td><td>Trong câu đảo ngữ (<i>"Beneath the glacier’s fractured ridges <b>lie</b> three subglacial lakes"</i>), <b>chủ ngữ thật đứng SAU động từ</b> (<i>three lakes → lie</i>)!</td></tr>
        <tr><td><b>3. Finite vs. Non-Finite Verb</b></td><td>Chọn <code>V-ing</code> khiến cả câu không có động từ chính (Fragment!)</td><td>Gạch bỏ mọi mệnh đề <code>which/that/who</code> và cụm chen giữa hai dấu phẩy → kiểm tra câu đã có ĐÚNG 1 động từ chia thì hay chưa!</td></tr>
        <tr><td><b>4. Essential Title/Name vs. Appositive</b></td><td>Thấy tên riêng là tự động kẹp 2 dấu phẩy sai!</td><td><i>"Marine biologist <b>Dr. Maya Sato</b> discovered..."</i> → <b>KHÔNG DẤU PHẨY</b> trước hay sau tên khi chức danh đi ngay trước tên!</td></tr>
      </tbody>
    </table>
  </div>

  <div id="sec-trans-synth" class="sat-card lecture-interactive-card" data-lecture-section="trans_synth">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>3. Transitions "Sắc thái siêu mịn" &amp; Rhetorical Synthesis Đa điều kiện</h2>
    <div class="sat-rule-box">
      <b>• Transitions Hard M2:</b> College Board cho 2 từ cùng nhóm (VD: <code>Specifically</code> vs <code>Consequently</code>, hoặc <code>Indeed</code> vs <code>Similarly</code>). Nhớ phân biệt:
      <br>&nbsp;&nbsp;– <code>Indeed / In fact</code>: nhấn mạnh sâu hơn/nâng cấp chính ý câu trước (cùng 1 chủ thể).
      <br>&nbsp;&nbsp;– <code>Similarly / Likewise</code>: chuyển sang <b>chủ thể/ví dụ thứ hai</b> có tính chất tương đồng.
      <br>&nbsp;&nbsp;– <code>Granted / Admittedly</code>: thừa nhận nhượng bộ một điểm (thường câu sau sẽ có <i>however/yet</i>).
      <br><b>• Rhetorical Synthesis (Q26–Q27):</b> Đọc <b>câu hỏi Goal TRƯỚC khi đọc bullet notes</b>! Gạch chân từng yêu cầu nhỏ (VD: "emphasize a <u>difference</u> between X and Y <u>to an audience unfamiliar with X</u>") — 3 đáp án sai đều đúng sự thật nhưng thiếu 1 vế mục tiêu!
    </div>
  </div>
'''
    b4_qc = make_quick_check_html(
        'qc_b4',
        'Chọn đáp án tuân thủ đúng quy tắc Standard English Conventions cho câu đảo ngữ + danh sách phức tạp:',
        'Archived inside the observatory’s temperature-controlled vault, which survived two coastal earthquakes intact, ______ hand-drawn lunar atlases from 1647, brass transit micrometers, and glass photographic plates.',
        ['remains', 'is remaining', 'remain', 'having remained'],
        2,
        'Gạt cụm phân từ đầu câu và mệnh đề phụ "which survived... intact", đây là CÂU ĐẢO NGỮ (Inverted Subject–Verb): Chủ ngữ thật nằm PHÍA SAU chỗ trống là một danh sách số nhiều gồm 3 vật thể ("atlases, micrometers, and plates") → phải chia động từ chính SỐ NHIỀU ở hiện tại là "remain" (C)! "having remained" (D) tạo lỗi Fragment không có động từ chính.'
    )
    b4_html = build_sat_lecture_html(
        '🔥 HARD M2 BOSS MASTERCLASS • R&W BOSS 4 (750–800)',
        'R&W Boss 4: 32-Minute Time-Triage SOP & Nested Hard Grammar Combos',
        'Chiến thuật đảo thứ tự làm bài 32 phút giúp dư 20 phút cho cụm Reading Hard + phá gọn 4 combo ngữ pháp xếp tầng và Transitions siêu mịn.',
        [
            'Áp dụng chiến thuật Reverse-Order Triage (Q1–Q5 → nhảy Q16–Q27 → quay về Q6–Q15) không bao giờ thiếu giờ khoanh bừa cuối bài.',
            'Xử lý chuẩn xác 4 combo ngữ pháp Hard M2: Super-Comma, Inverted Subject–Verb, Finite/Non-Finite Verb và Essential Title.',
            'Phân biệt cặp Transitions sắc thái mịn (Indeed vs Similarly, Granted) và áp dụng quy trình Goal-First cho Rhetorical Synthesis đa điều kiện.',
        ],
        b4_cards,
        b4_qc
    )
    b4_segs = [
        {
            'id': 'intro',
            'title': 'Tổng quan Quản trị 32 Phút & Ngữ pháp xếp tầng',
            'selector': '#sec-header',
            'en': 'Even brilliant readers lose forty points on Hard Module Two simply by running out of time and rushing through the grammar questions at the end. In this lesson, you will master the exact 32-minute pacing order used by 780-plus scorers along with the four trickiest nested grammar traps.',
            'vi': 'Ngay cả những thí sinh đọc rất giỏi vẫn mất oan 40 điểm trên Hard Module 2 chỉ vì hết giờ và phải làm vội nhóm câu ngữ pháp ở cuối bài. Bài học này sẽ trang bị cho bạn đúng thứ tự phân bổ 32 phút của nhóm 780 cộng cùng 4 combo ngữ pháp xếp tầng hiểm hóc nhất.'
        },
        {
            'id': 'triage',
            'title': 'Lộ trình Đảo thứ tự 32 phút',
            'selector': '#sec-triage',
            'en': 'Do not march blindly from question one to question twenty-seven. Finish Words in Context one through five in four minutes, then jump immediately via the Navigator to questions sixteen through twenty-seven to lock in all twelve grammar, transition, and synthesis points in eight minutes. That leaves a full twenty calm minutes—two minutes per question—for the ten toughest reading passages.',
            'vi': 'Đừng làm tuần tự một mạch từ câu 1 tới câu 27. Hãy xử lý xong câu 1 đến câu 5 trong 4 phút, sau đó bấm Navigator nhảy thẳng sang câu 16 đến 27 để khóa chắc trọn vẹn 12 điểm Ngữ pháp, Từ nối và Tổng hợp ghi chú chỉ trong 8 phút. Bạn sẽ còn nguyên 20 phút thảnh thơi, tức trọn 2 phút cho mỗi câu trong 10 bài đọc nặng nhất từ câu 6 đến câu 15.'
        },
        {
            'id': 'nested',
            'title': '4 Combo Ngữ pháp Xếp tầng Hard M2',
            'selector': '#sec-nested',
            'en': 'Watch for four favorite Hard Module Two grammar traps: first, super-commas where semicolons separate complex list items that already contain commas; second, inverted sentences where the true subject sits after the verb; third, fragment traps disguising a participle like having remained as a main verb; and fourth, zero commas around a title directly preceding a person’s name.',
            'vi': 'Cảnh giác bốn bẫy ngữ pháp xếp tầng ưa thích của Hard Module 2: một là dấu chấm phẩy super-comma dùng để tách các mục liệt kê đã có dấu phẩy bên trong; hai là câu đảo ngữ có chủ ngữ thật nằm sau động từ; ba là bẫy thiếu động từ chính khi nhầm V-ing thành vị ngữ; và bốn là không đặt dấu phẩy quanh chức danh đứng sát ngay trước tên riêng.'
        },
        {
            'id': 'trans_synth',
            'title': 'Transitions sắc thái mịn & Synthesis đa điều kiện',
            'selector': '#sec-trans-synth',
            'en': 'For high-level transitions, distinguish indeed, which reinforces the same subject, from similarly, which pivots to a second parallel case. And on Rhetorical Synthesis, read the prompt goal before the bullet points and verify that your choice satisfies every single constraint in that goal.',
            'vi': 'Với từ nối nâng cao, phân biệt rạch ròi indeed dùng để nhấn sâu thêm cùng một chủ thể với similarly dùng để chuyển sang đối tượng song song thứ hai. Còn với câu tổng hợp ghi chú, luôn đọc kỹ mục tiêu câu hỏi trước khi đọc các gạch đầu dòng và kiểm tra đáp án có đáp ứng đủ mọi điều kiện hay không.'
        }
    ]
    lectures.append({
        'code': 'b4',
        'module_key': 'boss_m10',
        'order_index': 4,
        'title': 'R&W Boss 4: 32-Minute Time-Triage SOP & Nested Hard Grammar Combos',
        'drill_key': 'boss_drill_4',
        'html': b4_html,
        'segments': b4_segs,
        'major_sections': [
            {'title': 'Lộ trình Đảo thứ tự 32 phút', 'startSegmentId': 'triage'},
            {'title': '4 Combo Ngữ pháp xếp tầng', 'startSegmentId': 'nested'},
            {'title': 'Transitions & Synthesis 750+', 'startSegmentId': 'trans_synth'},
        ],
    })

    return lectures
