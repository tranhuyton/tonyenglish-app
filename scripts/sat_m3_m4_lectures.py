# -*- coding: utf-8 -*-
from sat_audio_pipeline import build_sat_lecture_html, make_quick_check_html

def get_stage3_lectures():
    lectures = []

    # =========================================================================
    # LECTURE 3.1: Transitions — High-Level Logical Connectors
    # =========================================================================
    html_3_1 = build_sat_lecture_html(
        badge_text="Digital SAT 1500+ • R&W Module 3 • Expression of Ideas",
        title="3.1 Transitions: High-Level Logical Connectors & Hard-Tier Nuance Pairs",
        subtitle="Phân loại chính xác 4 họ từ nối logic và giải mã các cặp từ dễ nhầm nhất của Hard Module 2 (Nevertheless vs. Conversely vs. Instead; Indeed vs. Specifically).",
        intro_points=[
            "Áp dụng quy trình 'Che đáp án → Xác định quan hệ Câu A & Câu B' để tránh bẫy nghe thuận tai.",
            "Làm chủ bảng 4 họ từ nối chuẩn Digital SAT và dùng Quy tắc Đồng nghĩa (Synonym Elimination) để gạch nhanh 2 đáp án cùng chức năng.",
            "Phân biệt rạch ròi 5 cặp từ nối phân hóa 750+: Instead vs. Conversely, Indeed vs. Specifically, Consequently vs. Moreover, Still vs. Regardless, Fittingly vs. Admittedly.",
        ],
        cards_html='''
  <div id="sec-four-families" class="lecture-interactive-card sat-card" data-lecture-section="sec_four_families">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>1. Bốn Họ Từ Nối Cốt Lõi &amp; Quy tắc Loại Trừ Đồng Nghĩa</h2>
    <p>Mọi câu hỏi <b>Transitions</b> trên Digital SAT đều yêu cầu bạn nối <b>Ý Trước (Idea A)</b> với <b>Ý Sau (Idea B)</b>. Quy tắc vàng: <b>ĐỌC CẢ HAI CÂU TRƯỚC KHI NHÌN ĐÁP ÁN</b> và tự gán nhãn quan hệ!</p>
    <table class="sat-table">
      <thead>
        <tr><th>Họ Logic</th><th>Mối quan hệ Idea A → Idea B</th><th>Từ nối chuẩn Digital SAT</th></tr>
      </thead>
      <tbody>
        <tr><td><b>1. Continuers / Addition</b><br/><i>Cùng chiều, bổ sung</i></td><td>B thêm 1 lý lẽ/bằng chứng mới cùng hướng với A, hoặc minh họa/nhấn mạnh A.</td><td><i>Moreover, Furthermore, In addition, Also, Similarly, Likewise, Indeed, Specifically, For instance, In fact</i></td></tr>
        <tr><td><b>2. Contrasts / Concessions</b><br/><i>Ngược chiều, nhượng bộ</i></td><td>B trái ngược, thách thức, hoặc ngoại lệ so với A.</td><td><i>However, Nevertheless, Nonetheless, Still, Yet, Conversely, By contrast, On the other hand, Instead, Regardless, Admittedly</i></td></tr>
        <tr><td><b>3. Cause &amp; Effect</b><br/><i>Nhân – Quả</i></td><td>A là nguyên nhân trực tiếp dẫn tới kết quả B.</td><td><i>Therefore, Thus, Consequently, As a result, Accordingly, Hence, For this reason</i></td></tr>
        <tr><td><b>4. Sequence / Summary</b><br/><i>Trình tự / Kết luận</i></td><td>B xảy ra sau A theo dòng thời gian, hoặc đúc kết lại toàn đoạn.</td><td><i>Subsequently, Thereafter, Meanwhile, Previously, Ultimately, In sum, In other words</i></td></tr>
      </tbody>
    </table>
    <div class="sat-gold-box">
      <b>⚡ Synonym Elimination Shortcut (Cực mạnh ở Module 1 &amp; 2):</b><br/>
      Nếu trong 4 đáp án có hai từ nối <b>hoàn toàn đồng nghĩa về mặt chức năng</b> (VD: <i>Therefore</i> và <i>Consequently</i>; hoặc <i>Moreover</i> và <i>Furthermore</i>; hoặc <i>However</i> và <i>Nevertheless</i>) → <b>CẢ HAI ĐỀU SAI!</b> Gạch ngay lập tức!
    </div>
  </div>

  <div id="sec-hard-pairs" class="lecture-interactive-card sat-card" data-lecture-section="sec_hard_pairs">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>2. Năm Cặp Từ Nối "Sát Thủ" Của Hard Module 2 (750+ Nuance Pairs)</h2>
    <p>Ở Hard Module 2, College Board thường gài <b>2 từ nối CÙNG HỌ</b> (VD: 2 từ cùng mang nghĩa đối lập hoặc 2 từ cùng chiều) để ép bạn phân biệt sắc thái cực mịn:</p>
    <table class="sat-table">
      <thead>
        <tr><th>Cặp dễ nhầm</th><th>Sự khác biệt cốt lõi (Phải thuộc lòng!)</th></tr>
      </thead>
      <tbody>
        <tr>
          <td><b>Instead</b> vs. <b>However / Nevertheless</b></td>
          <td>• <b>Instead (Thay vào đó):</b> Vế A phải mang ý <i>phủ định / không làm X / từ bỏ X</i> → Vế B đưa ra <b>phương án thay thế Y</b>.<br/>• <b>However / Nevertheless (Tuy nhiên):</b> A đúng, nhưng B xảy ra bất chấp A (KHÔNG thay thế A).</td>
        </tr>
        <tr>
          <td><b>Conversely / By contrast</b> vs. <b>Nevertheless</b></td>
          <td>• <b>Conversely / By contrast:</b> So sánh <b>2 đối tượng/trường hợp đối xứng ngược nhau</b> (Loài X ưa nóng; <i>by contrast</i>, Loài Y ưa lạnh).<br/>• <b>Nevertheless / Still:</b> Cùng 1 đối tượng nhưng kết quả trái kỳ vọng (Loài X thiếu nước; <i>nevertheless</i>, nó vẫn sống sót).</td>
        </tr>
        <tr>
          <td><b>Indeed / In fact</b> vs. <b>Moreover / Furthermore</b></td>
          <td>• <b>Indeed / In fact:</b> Đẩy MẠNH hoặc nhấn mạnh CÙNG MỘT ý vừa nói bằng bằng chứng cực đoan hơn.<br/>• <b>Moreover / Furthermore:</b> Thêm một ý/ưu điểm <b>MỚI, ĐỘC LẬP</b> cùng hướng.</td>
        </tr>
        <tr>
          <td><b>Specifically / For instance</b> vs. <b>In other words</b></td>
          <td>• <b>Specifically / For instance:</b> Thu hẹp từ <i>Tổng quát → Ví dụ/Chi tiết cụ thể</i>.<br/>• <b>In other words / That is:</b> Diễn đạt lại <b>cùng cấp độ nghĩa</b> bằng cách nói dễ hiểu hơn.</td>
        </tr>
        <tr>
          <td><b>Admittedly / Granted</b> vs. <b>Regardless</b></td>
          <td>• <b>Admittedly / Granted:</b> Nhượng bộ thừa nhận 1 nhược điểm/giới hạn nhỏ trước khi phản công.<br/>• <b>Regardless:</b> Bất chấp hoàn cảnh vừa nêu, kết quả vẫn xảy ra như vậy.</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div id="sec-middle-trap" class="lecture-interactive-card sat-card" data-lecture-section="sec_middle_trap">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>3. Bẫy Vị Trí Từ Nối &amp; Chuyển Hướng Giữa Chừng</h2>
    <div class="sat-trap-box">
      <b>⚠️ Cạm bẫy kinh điển:</b> Nhiều thí sinh chỉ đọc <b>câu 1</b> và <b>câu 3</b> mà bỏ qua nửa sau của <b>câu 2</b>! Trên Digital SAT, từ nối có thể nằm ở <b>giữa câu 2</b> (bọc trong 2 dấu phẩy: <i>The second prototype, ______, consumed far less power</i>). Khi đó, hãy <b>nhấc từ nối lên ĐẦU câu 2 trong đầu</b> để đọc trơn tru mối nối giữa Câu 1 và Câu 2!
    </div>
    <div class="sat-ex-box">
      <b>Ví dụ:</b> <i>Early solar panels required rare silicon wafers to achieve high efficiency. Newer perovskite coatings, <b>______</b>, can be sprayed onto flexible plastic films at a fraction of the cost.</i><br/>
      → Nhấc lên đầu câu 2: <i>"<b>By contrast</b>, newer perovskite coatings can be sprayed..."</i> → So sánh 2 công nghệ đối nghịch nhau → chọn <b>by contrast</b> (KHÔNG chọn <i>nevertheless</i> hay <i>therefore</i>!).
    </div>
  </div>
''',
        quick_check_html=make_quick_check_html(
            qc_id="qc_3_1",
            passage_html="Many urban historians long believed that medieval Siena relied exclusively on surface cisterns for municipal water. ______, subterranean explorations in the late twentieth century mapped over twenty-five kilometers of hand-carved aqueduct tunnels called <i>bottini</i> running beneath the city streets.",
            question_prompt="Which choice completes the text with the most logical transition?",
            options=[
                "In fact",
                "Instead",
                "By contrast",
                "In reality"
            ],
            correct_idx=3,
            explanation_vi="Câu 1 nêu một niềm tin SAI LẦM trong quá khứ ('long believed... exclusively on surface cisterns'). Câu 2 phơi bày sự thật ngược lại với niềm tin đó ('mapped over 25 km of subterranean aqueducts'). 'In reality' (Trên thực tế) là từ nối chuẩn mực của Digital SAT để lật ngược nhận định sai lầm! Loại A ('In fact' chỉ dùng khi củng cố CÙNG CHIỀU câu 1), B ('Instead' dùng khi 1 chủ thể không làm X mà chọn làm Y), C ('By contrast' so sánh 2 đối tượng song song)."
        )
    )
    seg_3_1 = [
        {
            "id": "intro",
            "title": "Giới thiệu Bài 3.1: Transitions — Từ nối logic bậc cao",
            "selector": "#sec-header",
            "en": "Welcome to Lesson 3.1: Transitions. Alongside grammar, Transitions are your second guaranteed speed bank on the Digital SAT. Today we master the four logical families and the five high-level nuance pairs that separate seven-fifty scorers from the pack.",
            "vi": "Chào mừng các bạn đến với Bài 3.1: Từ nối logic Transitions. Cùng với Ngữ pháp, đây là mỏ điểm tốc độ thứ hai trên Digital SAT. Hôm nay ta làm chủ bốn họ từ nối và năm cặp từ tinh tế thường dùng để phân hóa mốc 750+."
        },
        {
            "id": "sec_four_families",
            "title": "1. Bốn họ từ nối & Mẹo loại trừ đồng nghĩa",
            "selector": "#sec-four-families",
            "en": "Section 1 organizes every transition into four core families: Addition, Contrast, Cause-and-Effect, and Sequence. Always cover the options, summarize the logical bridge between Idea A and Idea B first, and deploy the Synonym Elimination Shortcut: if two choices have identical logical functions—such as therefore and consequently—eliminate both immediately.",
            "vi": "Mục 1 hệ thống hóa bốn họ từ nối: Bổ sung cùng chiều, Đối lập, Nhân quả và Trình tự. Luôn xác định quan hệ giữa hai câu trước khi đọc đáp án, và áp dụng ngay mẹo loại trừ đồng nghĩa: hễ hai từ nối có cùng chức năng y hệt nhau như therefore và consequently thì gạch bỏ cả hai."
        },
        {
            "id": "sec_hard_pairs",
            "title": "2. Năm cặp từ nối sát thủ ở Hard Module 2",
            "selector": "#sec-hard-pairs",
            "en": "Section 2 breaks down five subtle Hard Module 2 pairs. Use instead only when the first sentence states a negation and the second offers a replacement. Use by contrast or conversely to compare two distinct subjects moving in opposite directions, whereas nevertheless applies to a single subject defying expectations. Finally, distinguish indeed—which intensifies the exact same claim—from moreover, which introduces a separate supporting point.",
            "vi": "Mục 2 giải mã năm cặp từ nối khó nhất ở Hard Module 2. Chỉ dùng instead khi vế trước phủ định X và vế sau thay thế bằng Y. Dùng by contrast khi đối chiếu hai đối tượng ngược chiều nhau, còn nevertheless dùng cho cùng một chủ thể xảy ra trái kỳ vọng. Phân biệt rạch ròi indeed dùng để nhấn mạnh sâu hơn chính ý cũ với moreover dùng để bổ sung một luận điểm mới độc lập."
        },
        {
            "id": "sec_middle_trap",
            "title": "3. Bẫy từ nối chen giữa câu",
            "selector": "#sec-middle-trap",
            "en": "Section 3 addresses mid-sentence transitions bracketed by commas. Whenever the blank sits inside the second sentence, mentally move it to the very beginning of that sentence so your brain evaluates the exact bridge between the two full ideas cleanly.",
            "vi": "Mục 3 xử lý bẫy từ nối nằm giữa câu hai trong cặp dấu phẩy. Mẹo cực nhanh là hãy nhấc chỗ trống lên đầu câu hai trong suy nghĩ để cảm nhận chính xác cầu nối logic giữa hai ý trọn vẹn."
        }
    ]
    lectures.append({
        "code": "3_1",
        "module_key": "rw_m3",
        "order_index": 1,
        "title": "3.1 Transitions: High-Level Logical Connectors & Hard-Tier Nuance Pairs",
        "drill_key": "drill_3_1",
        "drill_title": "Drill 3.1: Transitions — High-Level Logical Connectors (14 Qs)",
        "html": html_3_1,
        "segments": seg_3_1,
        "major_sections": {f"{s['id']}": {"start": i, "end": i} for i, s in enumerate(seg_3_1)},
    })

    # =========================================================================
    # LECTURE 3.2: Rhetorical Synthesis — Goal-First SOP
    # =========================================================================
    html_3_2 = build_sat_lecture_html(
        badge_text="Digital SAT 1500+ • R&W Module 3 • Expression of Ideas",
        title="3.2 Rhetorical Synthesis: The Goal-First SOP (100% Accuracy in 25 Seconds)",
        subtitle="Đọc Prompt Goal TRƯỚC khi đọc Bullet Notes — tiêu diệt tận gốc bẫy 'Đúng 100% dữ kiện nhưng sai mục tiêu đề bài'.",
        intro_points=[
            "Áp dụng quy trình Goal-First SOP giúp tiết kiệm 60% thời gian đọc bullet notes ở cuối Module.",
            "Nhận diện 6 nhóm Prompt Goal kinh điển nhất của Digital SAT (Introduce to unfamiliar audience, Compare/Contrast, Emphasize a finding, Present study methodology...).",
            "Kiểm chứng nhanh 2 tầng: (1) Đạt đủ 100% yêu cầu của Goal → (2) Kiểm tra lại Fact Accuracy với Bullet Notes để tránh bẫy bóp méo số liệu ở Hard Module 2.",
        ],
        cards_html='''
  <div id="sec-goal-first" class="lecture-interactive-card sat-card" data-lecture-section="sec_goal_first">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>1. Tại sao học viên mất thời gian ở câu "Bullet Notes"? — Quy trình Goal-First SOP</h2>
    <p>Mỗi bài thi Digital SAT R&amp;W có từ <b>4 đến 6 câu Rhetorical Synthesis</b> nằm ở cuối mỗi Module (Câu 23–27). Đừng bao giờ đọc 5–6 gạch đầu dòng trước rồi mới đọc câu hỏi!</p>
    <div class="sat-gold-box">
      <b>⚡ Quy trình Goal-First SOP 3 bước (≤25 giây/câu):</b><br/>
      <b>• Bước 1 — BỎ QUA bullet notes, nhảy thẳng xuống câu hỏi bên phải:</b> Gạch chân chính xác <b>Động từ &amp; Đối tượng mục tiêu</b> (VD: <i>"emphasize a <b>similarity</b> between X and Y"</i>, <i>"introduce the novel to an <b>unfamiliar audience</b>"</i>).<br/>
      <b>• Bước 2 — Quét 4 đáp án A/B/C/D theo mục tiêu đó:</b> Gạch ngay mọi đáp án không làm đúng yêu cầu của Goal (thường loại được 2–3 đáp án trong 10 giây mà chưa cần đọc kỹ notes!).<br/>
      <b>• Bước 3 — Đối chiếu Fact-Check (BẮT BUỘC ở Hard Module 2!):</b> Với 1–2 đáp án sống sót, liếc ngược lên Bullet Notes kiểm tra xem đáp án đó có <b>gài sai chi tiết, sai năm, hoặc đảo ngược hai đối tượng</b> không!
    </div>
  </div>

  <div id="sec-six-goals" class="lecture-interactive-card sat-card" data-lecture-section="sec_six_goals">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>2. Sáu Dạng Mục Tiêu (Prompt Goals) Kinh Điển &amp; Tiêu Chí Bắt Buộc</h2>
    <table class="sat-table">
      <thead>
        <tr><th>Dạng Prompt Goal</th><th>Tiêu chí BẮT BUỘC trong đáp án đúng</th><th>Bẫy thường gài</th></tr>
      </thead>
      <tbody>
        <tr><td><b>1. Emphasize a difference / contrast</b></td><td>Phải nhắc tên <b>CẢ HAI đối tượng</b> + dùng từ đối chiếu (<i>whereas, unlike, while, by contrast</i>) trên cùng 1 tiêu chí.</td><td>Chỉ mô tả 1 đối tượng, hoặc liệt kê 2 đặc điểm không tương phản nhau.</td></tr>
        <tr><td><b>2. Emphasize a similarity</b></td><td>Nhắc <b>CẢ HAI đối tượng</b> + điểm chung rõ ràng (<i>both, similarly, share</i>).</td><td>Chỉ nói về 1 đối tượng hoặc nêu điểm khác nhau.</td></tr>
        <tr><td><b>3. Introduce X to an audience UNFAMILIAR with X</b></td><td>Phải có <b>định nghĩa / giải thích X là ai hoặc là gì</b> (VD: <i>"Argentine composer Alberto Ginastera"</i>, <i>"the 1929 novel..."</i>).</td><td>Gọi trống không tên X như thể người đọc đã biết sẵn X là ai!</td></tr>
        <tr><td><b>4. Introduce X to an audience FAMILIAR with Y</b></td><td>Dùng <b>Y (thứ đã quen)</b> làm cầu nối để giới thiệu <b>X</b>, KHÔNG định nghĩa dài dòng Y như người lạ.</td><td>Lại đi định nghĩa Y hoặc bỏ quên không nhắc đến Y.</td></tr>
        <tr><td><b>5. Present the study and its findings / methodology</b></td><td>Hỏi <b>methodology</b> → phải nêu <i>cách làm/thí nghiệm</i>. Hỏi <b>findings</b> → phải nêu <i>kết quả phát hiện được</i>.</td><td>Tráo ngược: đề hỏi <i>methodology</i> nhưng đáp án chỉ nêu <i>findings</i>!</td></tr>
        <tr><td><b>6. Make &amp; support a generalization</b></td><td>Phải có <b>1 nhận định tổng quát (generalization)</b> KÈM <b>ví dụ cụ thể (support)</b> từ notes.</td><td>Chỉ có ví dụ cụ thể mà thiếu câu khái quát, hoặc chỉ khái quát không có ví dụ.</td></tr>
      </tbody>
    </table>
  </div>

  <div id="sec-fact-trap" class="lecture-interactive-card sat-card" data-lecture-section="sec_fact_trap">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>3. Bẫy "Cú Lừa Chót" ở Hard Module 2: Đúng Goal nhưng Sai Fact!</h2>
    <div class="sat-trap-box">
      <b>⚠️ Cảnh báo 750+:</b> Ở Module 1, gần như 100% các phương án đều đúng với Bullet Notes (chỉ khác mục tiêu). Nhưng ở <b>Hard Module 2</b>, College Board thỉnh thoảng gài <b>2 đáp án CÙNG ĐẠT GOAL</b>, trong đó 1 đáp án cố tình <b>đổi tên tác giả, đổi năm, hoặc đánh tráo kết quả giữa 2 đối tượng</b>! Vì vậy <b>Bước 3 (Fact-Check nhanh 5 giây với Bullet Notes)</b> là bắt buộc tuyệt đối cho mục tiêu 1500+!
    </div>
  </div>
''',
        quick_check_html=make_quick_check_html(
            qc_id="qc_3_2",
            passage_html="While researching a topic, a student has taken the following notes:<ul><li><i>The Book of Margery Kempe</i> (c. 1436) is widely considered the earliest surviving autobiography in English.</li><li>Margery Kempe dictated her life story to two scribes because she could not read or write.</li><li><i>The Interesting Narrative of the Life of Olaudah Equiano</i> (1789) is a landmark eighteenth-century autobiography written directly by its author.</li><li>Equiano’s book played a major role in the British movement to abolish the transatlantic slave trade.</li></ul>",
            question_prompt="The student wants to emphasize a difference in how the two autobiographies were composed. Which choice most effectively uses relevant information from the notes to accomplish this goal?",
            options=[
                "Both <i>The Book of Margery Kempe</i> and <i>The Interesting Narrative of the Life of Olaudah Equiano</i> are historically significant autobiographies published in Britain.",
                "<i>The Book of Margery Kempe</i> dates to around 1436, whereas Olaudah Equiano’s autobiography was published more than three centuries later in 1789.",
                "Whereas Margery Kempe dictated her autobiography to two scribes, Olaudah Equiano wrote his own narrative directly.",
                "Because Margery Kempe could not read or write, she dictated what is considered the earliest surviving autobiography in English."
            ],
            correct_idx=2,
            explanation_vi="Mục tiêu: 'emphasize a difference in HOW the two autobiographies were COMPOSED' (nhấn mạnh điểm KHÁC NHAU về CÁCH VIẾT/SOẠN THẢO của CẢ HAI cuốn). A nêu điểm giống nhau; B nêu khác nhau về NĂM XUẤT BẢN (không phải cách soạn thảo); D chỉ nhắc 1 cuốn. Duy nhất C đối chiếu trực tiếp cách soạn thảo của cả 2 cuốn (dictated to two scribes vs. wrote directly)."
        )
    )
    seg_3_2 = [
        {
            "id": "intro",
            "title": "Giới thiệu Bài 3.2: Rhetorical Synthesis — Quy trình Goal-First",
            "selector": "#sec-header",
            "en": "Welcome to Lesson 3.2: Rhetorical Synthesis. These bullet-point questions sit at the end of every module and can be solved in twenty-five seconds with one hundred percent accuracy once you stop reading the notes first.",
            "vi": "Chào mừng các bạn đến với Bài 3.2: Tổng hợp tu từ Rhetorical Synthesis. Những câu ghi chú gạch đầu dòng ở cuối mỗi module có thể được giải quyết trong 25 giây với độ chính xác tuyệt đối nếu bạn bỏ thói quen đọc hết ghi chú trước."
        },
        {
            "id": "sec_goal_first",
            "title": "1. Quy trình 3 bước Goal-First SOP",
            "selector": "#sec-goal-first",
            "en": "Section 1 presents the Goal-First routine. Step one: skip the notes and read the exact student goal in the prompt first. Step two: scan the four choices and slash every option that fails to accomplish that exact verb and target. Step three: verify your surviving choice against the bullet notes for factual accuracy.",
            "vi": "Mục 1 giới thiệu quy trình Goal-First ba bước. Bước một: bỏ qua phần gạch đầu dòng và đọc thẳng mục tiêu của học sinh trong câu hỏi. Bước hai: quét bốn đáp án và loại mọi lựa chọn không đáp ứng đúng yêu cầu đó. Bước ba: đối chiếu nhanh đáp án còn lại với ghi chú để kiểm tra tính chính xác dữ kiện."
        },
        {
            "id": "sec_six_goals",
            "title": "2. Sáu dạng mục tiêu kinh điển",
            "selector": "#sec-six-goals",
            "en": "Section 2 details the six recurring prompt goals: emphasizing a difference or a similarity—both of which require mentioning both subjects—introducing a subject to an unfamiliar audience by defining who or what it is, distinguishing study methodology from study findings, and pairing a broad generalization with a concrete supporting example.",
            "vi": "Mục 2 tổng kết sáu dạng mục tiêu quen thuộc nhất: nhấn mạnh điểm khác hay giống nhau đều phải gọi tên cả hai đối tượng; giới thiệu với khán giả chưa biết phải có định nghĩa rõ ràng; phân biệt giữa phương pháp nghiên cứu và kết quả tìm thấy; và luôn kết hợp nhận định khái quát kèm ví dụ cụ thể khi đề yêu cầu."
        },
        {
            "id": "sec_fact_trap",
            "title": "3. Bẫy Đúng Goal nhưng Sai Fact ở Hard Module 2",
            "selector": "#sec-fact-trap",
            "en": "Section 3 warns about a Hard Module 2 twist: occasionally two options satisfy the stated goal, but one silently swaps dates, names, or results from the bullet list. Always spend five seconds verifying every fact in your final answer against the notes.",
            "vi": "Mục 3 cảnh báo bẫy nâng cao ở Hard Module 2: đôi khi có hai đáp án cùng khớp mục tiêu, nhưng một đáp án cố tình tráo năm, tên tác giả hoặc kết quả giữa hai đối tượng. Luôn dành năm giây kiểm chứng lại dữ kiện với danh sách ghi chú trước khi chốt."
        }
    ]
    lectures.append({
        "code": "3_2",
        "module_key": "rw_m3",
        "order_index": 2,
        "title": "3.2 Rhetorical Synthesis: The Goal-First SOP (100% Accuracy in 25 Seconds)",
        "drill_key": "drill_3_2",
        "drill_title": "Drill 3.2: Rhetorical Synthesis — Goal-First Mastery (14 Qs)",
        "html": html_3_2,
        "segments": seg_3_2,
        "major_sections": {f"{s['id']}": {"start": i, "end": i} for i, s in enumerate(seg_3_2)},
    })

    # =========================================================================
    # LECTURE 4.1: Words in Context I — Context Clues & Secondary Meanings
    # =========================================================================
    html_4_1 = build_sat_lecture_html(
        badge_text="Digital SAT 1500+ • R&W Module 4 • Craft and Structure",
        title="4.1 Words in Context I: Predict-Before-Peek, Context Clues & Secondary Meanings",
        subtitle="Chiến thuật 'Tự đoán trước khi nhìn đáp án' giúp vô hiệu hóa bẫy từ đồng âm/từ nghe sang nhưng sai logic ngữ cảnh.",
        intro_points=[
            "Áp dụng quy trình 3 bước Predict-Before-Peek + Positive/Negative Charge (+ / - / 0).",
            "Nhận diện 4 loại manh mối ngữ cảnh (Definition/Colon Clue, Contrast Clue, Cause-Effect Clue, Example Mirroring).",
            "Xử lý thành thạo dạng từ phổ thông mang nghĩa thứ cấp học thuật (Secondary Meanings: pedestrian, check, plastic, qualified, currency, novel, wanting...).",
        ],
        cards_html='''
  <div id="sec-predict" class="lecture-interactive-card sat-card" data-lecture-section="sec_predict">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>1. Phương pháp "Predict-Before-Peek" (Tự đoán nghĩa trước khi nhìn A/B/C/D)</h2>
    <p>Words in Context chiếm <b>4–6 câu đầu tiên</b> của MỖI Module (~10 câu/đề!). Sai lầm chết người nhất là thử lắp lần lượt 4 đáp án vào chỗ trống rồi chọn từ "nghe học thuật nhất" — đó chính là cái bẫy College Board giăng sẵn!</p>
    <div class="sat-rule-box">
      <b>🎯 Quy trình 3 bước chuẩn 780–800:</b><br/>
      <b>1. Tìm "Manh mối gương" (Mirror Clue):</b> Mọi câu Words in Context của College Board ĐỀU chứa sẵn một cụm từ định nghĩa lại hoặc đối lập trực tiếp với chỗ trống (thường nằm sau dấu hai chấm <code>:</code>, gạch ngang <code>—</code>, từ <i>because / although / rather than</i>, hoặc mệnh đề <i>revealing that...</i>).<br/>
      <b>2. Tự điền 1 từ tiếng Anh/Việt đơn giản + Dấu điện tích (+ / − / 0):</b> Trước khi nhìn 4 đáp án, hãy tự chốt trong đầu: <i>"Chỗ này cần từ mang nghĩa <b>ngắn ngủi (−)</b>"</i> hay <i>"<b>khó đoán/mơ hồ</b>"</i>.<br/>
      <b>3. Khớp nghĩa chính xác &amp; Gạch loại trừ:</b> Chỉ giữ đáp án khớp <b>100% logic của Mirror Clue</b>, bất kể từ đó trông đơn giản hay cao siêu!
    </div>
  </div>

  <div id="sec-clues" class="lecture-interactive-card sat-card" data-lecture-section="sec_clues">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>2. Bốn Loại Manh Mối Ngữ Cảnh Trên Digital SAT</h2>
    <table class="sat-table">
      <thead>
        <tr><th>Loại Clue</th><th>Tín hiệu nhận diện</th><th>Ví dụ giải mã nhanh</th></tr>
      </thead>
      <tbody>
        <tr><td><b>1. Restatement / Colon Clue</b></td><td><code>:</code>, <code>—</code>, <code>that is</code>, <code>in other words</code>, dấu phẩy đồng vị</td><td><i>The treaty proved ______: neither nation honored its border terms beyond six months.</i> → Chỗ trống = <b>vô hiệu / ngắn ngủi</b> (<i>ineffectual / short-lived</i>).</td></tr>
        <tr><td><b>2. Contrast Clue</b></td><td><i>Although, While, Whereas, Rather than, Unlike, Far from, However</i></td><td><i>Far from being ______ to local crafts, the museum’s new wing actively commissions rural weavers.</i> → Trái nghĩa với "actively commissions" → <b>thờ ơ / xa cách</b> (<i>indifferent / hostile</i>).</td></tr>
        <tr><td><b>3. Cause &amp; Effect Clue</b></td><td><i>Because, Since, Therefore, So...that, Consequently</i></td><td><i>Because coastal kelp forests grow at astonishing speeds, they can ______ carbon far more rapidly than slow-growing terrestrial shrubs.</i> → Chỗ trống = <b>hấp thụ/tích trữ</b> (<i>sequester</i>).</td></tr>
        <tr><td><b>4. Example / Proof Clue</b></td><td>Câu 2 minh họa cụ thể tính chất nêu ở chỗ trống Câu 1</td><td><i>The composer’s score is remarkably ______; in the third movement alone, she weaves jazz syncopation into Baroque fugues.</i> → Chỗ trống = <b>đa dạng / pha trộn</b> (<i>eclectic</i>).</td></tr>
      </tbody>
    </table>
  </div>

  <div id="sec-secondary" class="lecture-interactive-card sat-card" data-lecture-section="sec_secondary">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>3. Bẫy Nghĩa Thứ Cấp Học Thuật (Secondary Meanings — Đặc sản 750+)</h2>
    <p>Rất nhiều câu khó của Digital SAT dùng những từ bạn TƯỞNG MÌNH BIẾT, nhưng lại kiểm tra <b>nghĩa thứ 2 trong văn bản học thuật</b>:</p>
    <table class="sat-table">
      <thead>
        <tr><th>Từ quen mặt</th><th>Nghĩa phổ thông (Bẫy!)</th><th>Nghĩa học thuật trên Digital SAT (Bắt buộc thuộc!)</th></tr>
      </thead>
      <tbody>
        <tr><td><b>pedestrian</b> (adj)</td><td>người đi bộ</td><td><b>tầm thường, tẻ nhạt, thiếu sáng tạo</b> (<i>uninspired, dull</i>)</td></tr>
        <tr><td><b>qualified</b> (adj)</td><td>đủ năng lực/trình độ</td><td><b>có điều kiện, hạn chế, không tuyệt đối</b> (<i>qualified praise = lời khen có chừng mực</i>)</td></tr>
        <tr><td><b>check</b> (v / n)</td><td>kiểm tra / hóa đơn</td><td><b>kiềm chế, ngăn chặn</b> (<i>to check inflation / hold in check</i>)</td></tr>
        <tr><td><b>plastic</b> (adj)</td><td>bằng nhựa</td><td><b>dẻo, dễ uốn nắn, dễ thích nghi</b> (<i>vocal plasticity = tính linh hoạt giọng kêu</i>)</td></tr>
        <tr><td><b>wanting</b> (adj)</td><td>đang muốn</td><td><b>thiếu sót, chưa đạt chuẩn</b> (<i>found wanting = bị đánh giá còn thiếu hụt</i>)</td></tr>
        <tr><td><b>currency</b> (n)</td><td>tiền tệ</td><td><b>sự phổ biến, độ thịnh hành</b> (<i>gain currency = trở nên thịnh hành</i>)</td></tr>
        <tr><td><b>arrest</b> (v)</td><td>bắt giữ tội phạm</td><td><b>làm ngưng lại / thu hút mạnh sự chú ý</b> (<i>arresting visual detail</i>)</td></tr>
        <tr><td><b>eclipse</b> (v)</td><td>nhật thực/nguyệt thực</td><td><b>làm lu mờ, vượt trội hoàn toàn</b> (<i>eclipsed earlier rivals</i>)</td></tr>
      </tbody>
    </table>
  </div>
''',
        quick_check_html=make_quick_check_html(
            qc_id="qc_4_1",
            passage_html="Reviewers offered only ______ praise for the architect’s renovated train hall: while admiring the soaring glass canopy, they criticized the cramped ticketing concourse and poor acoustic baffling.",
            question_prompt="Which choice completes the text with the most logical and precise word or phrase?",
            options=[
                "unqualified",
                "qualified",
                "pedestrian",
                "exhaustive"
            ],
            correct_idx=1,
            explanation_vi="Sau dấu hai chấm (:) là Mirror Clue cực rõ: 'while admiring X, they criticized Y' → lời khen CÓ ĐIỀU KIỆN / CÓ CHỪNG MỰC (không hoàn toàn!). Trong tiếng Anh học thuật SAT, 'qualified praise' nghĩa là lời khen có giới hạn/điều kiện (trái ngược với 'unqualified praise' = khen ngợi tuyệt đối không chút chê bai). Chọn B!"
        )
    )
    seg_4_1 = [
        {
            "id": "intro",
            "title": "Giới thiệu Bài 4.1: Words in Context I — Predict-Before-Peek",
            "selector": "#sec-header",
            "en": "Welcome to Lesson 4.1: Words in Context Part One. Words in Context opens every Reading and Writing module, and mastering the Predict-Before-Peek method prevents you from falling for fancy-sounding academic decoys.",
            "vi": "Chào mừng các bạn đến với Bài 4.1: Từ vựng trong ngữ cảnh Phần 1. Đây là dạng mở màn của mọi module Đọc – Viết, và phương pháp tự đoán nghĩa trước khi nhìn đáp án sẽ bảo vệ bạn khỏi các từ học thuật nghe kêu nhưng sai logic."
        },
        {
            "id": "sec_predict",
            "title": "1. Quy trình Predict-Before-Peek",
            "selector": "#sec-predict",
            "en": "Section 1 introduces Predict-Before-Peek. Never plug all four options into the blank blindly. Instead, locate the mirror clue—the phrase inside the passage that directly defines or contrasts with the blank—write down a simple prediction and positive or negative charge in your head, and match that exact meaning against the choices.",
            "vi": "Mục 1 trình bày kỹ thuật tự đoán trước khi nhìn đáp án. Đừng lắp thử từng từ một cách cảm tính. Thay vào đó, hãy tìm manh mối gương ngay trong đoạn văn—nơi định nghĩa hoặc đối lập trực tiếp với chỗ trống—rồi tự chốt nghĩa đơn giản và sắc thái tích cực hay tiêu cực trước khi đối chiếu với 4 lựa chọn."
        },
        {
            "id": "sec_clues",
            "title": "2. Bốn loại manh mối ngữ cảnh",
            "selector": "#sec-clues",
            "en": "Section 2 maps the four signal clues: restatement clues after colons or dashes, contrast clues like although or far from, cause-and-effect bridges like because, and concrete examples in the following sentence that prove the missing adjective or verb.",
            "vi": "Mục 2 hệ thống hóa bốn tín hiệu ngữ cảnh: định nghĩa lại sau dấu hai chấm hay gạch ngang, manh mối đối lập như far from hay although, cầu nối nhân quả với because, và câu ví dụ minh họa cụ thể ngay phía sau."
        },
        {
            "id": "sec_secondary",
            "title": "3. Bẫy nghĩa thứ cấp học thuật (Secondary Meanings)",
            "selector": "#sec-secondary",
            "en": "Section 3 reveals a favorite 750-plus College Board weapon: secondary meanings of everyday words. Memorize that pedestrian means dull or uninspired, qualified means limited or conditional, check means restrain, wanting means lacking, currency means widespread acceptance, and eclipse means surpass or overshadow.",
            "vi": "Mục 3 bật mí vũ khí phân hóa 750+ của College Board: nghĩa thứ cấp học thuật của các từ quen thuộc. Hãy thuộc nằm lòng: pedestrian nghĩa là tẻ nhạt tầm thường, qualified là có điều kiện chừng mực, check là kiềm chế, wanting là thiếu sót, currency là độ thịnh hành, và eclipse là làm lu mờ vượt trội."
        }
    ]
    lectures.append({
        "code": "4_1",
        "module_key": "rw_m4",
        "order_index": 1,
        "title": "4.1 Words in Context I: Predict-Before-Peek, Context Clues & Secondary Meanings",
        "drill_key": "drill_4_1",
        "drill_title": "Drill 4.1: Words in Context I — Context Clues & Secondary Meanings (14 Qs)",
        "html": html_4_1,
        "segments": seg_4_1,
        "major_sections": {f"{s['id']}": {"start": i, "end": i} for i, s in enumerate(seg_4_1)},
    })

    # =========================================================================
    # LECTURE 4.2: Words in Context II — 750+ Elite Lexicon & Nuance Traps
    # =========================================================================
    html_4_2 = build_sat_lecture_html(
        badge_text="Digital SAT 1500+ • R&W Module 4 • Craft and Structure",
        title="4.2 Words in Context II: 750+ Elite Lexicon, Word Roots & Nuance Precision",
        subtitle="Chinh phục nhóm từ vựng học thuật tầng Hard Module 2: phân biệt các cặp từ cùng điện tích nhưng khác sắc thái và ứng dụng gốc từ Latin/Hy Lạp.",
        intro_points=[
            "Phân biệt chính xác các cụm từ cùng hướng nghĩa nhưng khác độ mạnh/tác động (VD: mitigate vs. preclude vs. eradicate; corroborate vs. speculate; equivocal vs. obscure).",
            "Khai thác 12 gốc từ Latin/Hy Lạp sinh ra hơn 150 từ SAT cao cấp để giải mã từ mới ngay trong phòng thi.",
            "Kết hợp luyện phản xạ hàng ngày với 10 bộ Game Từ vựng (500 từ SAT 1500+) trong thư mục Elite Vocabulary Games.",
        ],
        cards_html='''
  <div id="sec-nuance-clusters" class="lecture-interactive-card sat-card" data-lecture-section="sec_nuance_clusters">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>1. Sáu Cụm Sắc Thái Tinh Tế (Precision Nuance Clusters) Hay Thi Nhất Hard Module 2</h2>
    <p>Ở Hard Module 2, không còn chuyện 3 từ tiêu cực + 1 từ tích cực. Thường sẽ có <b>2 hoặc 3 từ CÙNG CHIỀU</b>, đòi hỏi bạn phân biệt chính xác <b>mức độ (degree)</b> và <b>đối tượng tác động (collocation)</b>:</p>
    <table class="sat-table">
      <thead>
        <tr><th>Nhóm nghĩa</th><th>Phân biệt sắc thái chuẩn 780–800</th></tr>
      </thead>
      <tbody>
        <tr><td><b>Giảm nhẹ vs. Chặn đứng vs. Xóa sổ</b></td><td>• <b>mitigate / ameliorate / alleviate:</b> làm <i>giảm bớt</i> mức độ nghiêm trọng (vẫn còn tồn tại).<br/>• <b>preclude / forestall / obviate:</b> <i>ngăn chặn từ trước</i> khiến việc gì không thể xảy ra / không còn cần thiết.<br/>• <b>eradicate / obliterate:</b> <i>xóa sổ hoàn toàn</i> 100%.</td></tr>
        <tr><td><b>Ủng hộ / Củng cố bằng chứng</b></td><td>• <b>corroborate / substantiate / buttress:</b> củng cố bằng <i>bằng chứng thực tế độc lập</i>.<br/>• <b>postulate / hypothesize / surmise:</b> chỉ mới <i>đặt giả thuyết / phỏng đoán</i> (chưa chứng minh!).</td></tr>
        <tr><td><b>Bác bỏ / Làm suy yếu</b></td><td>• <b>undermine / subvert:</b> làm suy yếu dần nền tảng.<br/>• <b>repudiate / refute / debunk:</b> bác bỏ thẳng thừng bằng lý lẽ/bằng chứng.<br/>• <b>belie:</b> tạo ra vẻ ngoài mâu thuẫn / phơi bày sự sai lệch của một nhận định.</td></tr>
        <tr><td><b>Mơ hồ vs. Khó hiểu vs. Dễ nhầm</b></td><td>• <b>ambiguous / equivocal:</b> có <i>nhiều cách hiểu</i>, nước đôi, không dứt khoát.<br/>• <b>enigmatic / arcane / esoteric:</b> bí ẩn, chỉ nhóm nhỏ chuyên gia mới hiểu nổi.<br/>• <b>tenuous:</b> mong manh, lỏng lẻo (VD: <i>a tenuous link = mối liên hệ mong manh</i>).</td></tr>
        <tr><td><b>Phổ biến vs. Độc đáo/Dị biệt</b></td><td>• <b>ubiquitous / pervasive / prevalent:</b> có mặt khắp nơi.<br/>• <b>idiosyncratic / singular / sui generis:</b> mang nét đặc thù riêng biệt không trộn lẫn.<br/>• <b>disparate / heterogeneous:</b> hoàn toàn khác biệt nhau về bản chất.</td></tr>
        <tr><td><b>Ngắn ngủi vs. Bền bỉ</b></td><td>• <b>ephemeral / transient / fleeting:</b> sớm nở tối tàn, thoáng qua.<br/>• <b>enduring / perennial / entrenched:</b> lâu dài, ăn sâu bám rễ.</td></tr>
      </tbody>
    </table>
  </div>

  <div id="sec-roots" class="lecture-interactive-card sat-card" data-lecture-section="sec_roots">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>2. Hệ Thống Gốc Từ Latin &amp; Hy Lạp "Mở Khóa" Từ Lạ Trong Phòng Thi</h2>
    <p>Nếu gặp một từ hoàn toàn lạ ở Câu 4 Hard Module 2, đừng hoảng! Tách tiền tố + gốc từ sẽ giúp bạn đoán đúng 80% hướng nghĩa:</p>
    <table class="sat-table">
      <thead>
        <tr><th>Tiền tố / Gốc từ</th><th>Nghĩa gốc</th><th>Các từ SAT 1500+ điển hình</th></tr>
      </thead>
      <tbody>
        <tr><td><span class="sat-code">circum-</span></td><td>xung quanh, vòng tránh</td><td><b>circumvent</b> (lách/tránh), <b>circumspect</b> (thận trọng nhìn quanh), <b>circumscribe</b> (giới hạn phạm vi)</td></tr>
        <tr><td><span class="sat-code">pre- / pro-</span></td><td>trước / tiến về trước</td><td><b>preclude</b> (đóng/ngăn trước), <b>precursor</b> (tiền thân), <b>proliferate</b> (sinh sôi nhanh), <b>propensity</b> (khuynh hướng)</td></tr>
        <tr><td><span class="sat-code">bene- / eu- / mal-</span></td><td>tốt / đẹp / xấu</td><td><b>benevolent</b>, <b>euphemism</b>, <b>malign</b> (bôi nhọ/độc hại), <b>maladaptive</b></td></tr>
        <tr><td><span class="sat-code">equi- / ambi- / omni-</span></td><td>bằng / cả hai / tất cả</td><td><b>equivocal</b> (nước đôi), <b>ambivalent</b> (mâu thuẫn cảm xúc), <b>omnipresent</b> (khắp nơi)</td></tr>
        <tr><td><span class="sat-code">cred / fid / ver</span></td><td>tin / trung thực / sự thật</td><td><b>incredulous</b> (hoài nghi), <b>fidelity</b> (độ chính xác/trung thành), <b>verisimilitude</b> (tính chân thực)</td></tr>
        <tr><td><span class="sat-code">vac / van / void</span></td><td>trống rỗng</td><td><b>vacuous</b> (rỗng tuếch), <b>evanescent</b> (tan biến nhanh), <b>devoid of</b> (hoàn toàn thiếu)</td></tr>
      </tbody>
    </table>
  </div>

  <div id="sec-collocation" class="lecture-interactive-card sat-card" data-lecture-section="sec_collocation">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>3. Bộ Lọc "Chủ Ngữ – Tân Ngữ" (Subject–Object Fit Check)</h2>
    <div class="sat-gold-box">
      <b>🔍 Mẹo chốt hạ khi còn phân vân 2 từ gần nghĩa:</b><br/>
      Kiểm tra xem <b>ai là Chủ ngữ</b> và <b>ai là Tân ngữ</b> của chỗ trống!<br/>
      • <i>Một bằng chứng/nghiên cứu</i> có thể <b>corroborate / undermine / substantiate</b> một <i>giả thuyết</i>, nhưng KHÔNG thể <b>appease</b> (xoa dịu cảm xúc) hay <b>reproach</b> (trách móc người) một giả thuyết!<br/>
      • <i>Một quy định pháp luật</i> có thể <b>stipulate / mandate / preclude</b> một hành động, nhưng KHÔNG thể <b>lament</b> (than khóc) một hành động!
    </div>
  </div>
''',
        quick_check_html=make_quick_check_html(
            qc_id="qc_4_2",
            passage_html="Because the newly drafted preservation ordinance requires property owners to retain original brick facades without banning interior energy-efficiency upgrades, municipal planners hope it will ______ historic neighborhood character while still allowing modern insulation.",
            question_prompt="Which choice completes the text with the most logical and precise word or phrase?",
            options=[
                "safeguard",
                "preclude",
                "fabricate",
                "ameliorate"
            ],
            correct_idx=0,
            explanation_vi="Sắc lệnh bảo tồn ('preservation ordinance') yêu cầu giữ nguyên mặt tiền gạch cổ → nhằm BẢO VỆ/GÌN GIỮ nét đặc trưng khu phố lịch sử ('safeguard historic neighborhood character'). Bẫy D ('ameliorate' = cải thiện một vấn đề xấu/khó khăn) tuy nghe sang và tích cực nhưng sai collocation: ta ameliorate a problem/shortage, không ameliorate historic character! B ('preclude' = ngăn chặn) ngược nghĩa; C ('fabricate' = bịa đặt/chế tạo) sai logic."
        )
    )
    seg_4_2 = [
        {
            "id": "intro",
            "title": "Giới thiệu Bài 4.2: Từ vựng tầng 750+ & Phân biệt sắc thái",
            "selector": "#sec-header",
            "en": "Welcome to Lesson 4.2: Words in Context Part Two, focusing on the 750-plus elite lexicon. On Hard Module 2, multiple choices often share the same positive or negative charge, so precision of degree and collocation becomes decisive.",
            "vi": "Chào mừng các bạn đến với Bài 4.2: Từ vựng học thuật tầng 750+ và phân biệt sắc thái tinh tế. Ở Hard Module 2, nhiều đáp án thường có cùng hướng tích cực hoặc tiêu cực, vì vậy độ chính xác về mức độ và ngữ cảnh kết hợp từ là chìa khóa quyết định."
        },
        {
            "id": "sec_nuance_clusters",
            "title": "1. Sáu cụm từ vựng sắc thái tinh tế",
            "selector": "#sec-nuance-clusters",
            "en": "Section 1 contrasts six high-yield clusters. Distinguish mitigate—which merely softens harm—from preclude, which prevents something altogether, and eradicate, which wipes it out completely. Similarly, separate corroborate—backing a claim with independent proof—from hypothesize, which merely proposes an unproven idea, and distinguish tenuous from equivocal.",
            "vi": "Mục 1 đối chiếu sáu nhóm từ hay thi nhất. Phân biệt mitigate là giảm nhẹ tác hại với preclude là ngăn chặn không cho xảy ra và eradicate là xóa sổ hoàn toàn. Tương tự, tách biệt corroborate là củng cố bằng bằng chứng độc lập với hypothesize chỉ mới đặt giả thuyết, và phân biệt tenuous mong manh với equivocal nước đôi."
        },
        {
            "id": "sec_roots",
            "title": "2. Mở khóa từ lạ bằng gốc từ Latin & Hy Lạp",
            "selector": "#sec-roots",
            "en": "Section 2 equips you with twelve powerhouse roots. Knowing that circum means around unlocks circumvent, circumspect, and circumscribe; knowing vac means empty unlocks vacuous and evanescent; and recognizing equi and ambi helps you spot ambiguity words instantly.",
            "vi": "Mục 2 trang bị hệ thống gốc từ Latin và Hy Lạp đắc lực. Nhớ gốc circum nghĩa là xung quanh giúp bạn giải mã ngay circumvent, circumspect và circumscribe; gốc vac là trống rỗng mở khóa vacuous và evanescent; còn equi và ambi giúp nhận diện lập tức nhóm từ nước đôi mơ hồ."
        },
        {
            "id": "sec_collocation",
            "title": "3. Bộ lọc Chủ ngữ – Tân ngữ (Collocation Fit)",
            "selector": "#sec-collocation",
            "en": "Finally, whenever two choices look equally positive, run the Subject-Object Fit Check. You ameliorate a problem or hardship, never a positive heritage; evidence can corroborate or belie a hypothesis, but it cannot appease or reproach one. Pair this lesson with our ten Elite SAT Vocabulary Games to build instant recall across five hundred core words.",
            "vi": "Cuối cùng, khi còn phân vân hai từ cùng sắc thái, hãy chạy Bộ lọc Chủ ngữ và Tân ngữ. Bạn dùng ameliorate để làm dịu một vấn đề xấu chứ không dùng cho di sản tốt đẹp; bằng chứng có thể củng cố hay bác bỏ một giả thuyết chứ không thể xoa dịu nó. Hãy kết hợp bài học này với 10 bộ Game Từ vựng 500 từ SAT tinh tuyển trên hệ thống."
        }
    ]
    lectures.append({
        "code": "4_2",
        "module_key": "rw_m4",
        "order_index": 2,
        "title": "4.2 Words in Context II: 750+ Elite Lexicon, Word Roots & Nuance Precision",
        "drill_key": "drill_4_2",
        "drill_title": "Drill 4.2: Words in Context II — 750+ Elite Lexicon & Nuance Traps (14 Qs)",
        "html": html_4_2,
        "segments": seg_4_2,
        "major_sections": {f"{s['id']}": {"start": i, "end": i} for i, s in enumerate(seg_4_2)},
    })

    # =========================================================================
    # LECTURE 4.3: Text Structure, Main Purpose & Function
    # =========================================================================
    html_4_3 = build_sat_lecture_html(
        badge_text="Digital SAT 1500+ • R&W Module 4 • Craft and Structure",
        title="4.3 Text Structure, Main Purpose & Underlined Sentence Function",
        subtitle="Đọc văn bản như một kiến trúc sư tu từ: tách biệt 'Nội dung nói gì' với 'Tác giả đang LÀM GÌ' (Rhetorical Action Verbs).",
        intro_points=[
            "Phân biệt chuẩn xác 3 tiểu dạng: Main Purpose (Mục đích tổng thể), Overall Structure (Bố cục trình tự 2–3 chặng), và Underlined Sentence Function (Vai trò của 1 câu cụ thể).",
            "Áp dụng kỹ thuật 'Verbs First' (Kiểm tra Động từ tu từ đầu đáp án: critique, illustrate, qualify, challenge, trace, explain) để loại nhanh 2–3 bẫy.",
            "Giải mã mượt mà các đoạn trích Thơ & Văn học thế kỷ 19 bằng phương pháp bỏ qua từ cổ, bám trục Cảm xúc + Hành động chính.",
        ],
        cards_html='''
  <div id="sec-three-subtypes" class="lecture-interactive-card sat-card" data-lecture-section="sec_three_subtypes">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>1. Ba Tiểu Dạng &amp; Chiến Thuật "Rhetorical Verbs First"</h2>
    <p>Học viên hay nhầm câu hỏi <b>Purpose / Structure</b> với câu hỏi <b>Detail</b>. Điểm cốt lõi: đừng chỉ tìm đáp án "có chứa từ khóa của bài" — hãy kiểm tra <b>ĐỘNG TỪ HÀNH ĐỘNG ĐẦU CÂU</b> của từng đáp án!</p>
    <table class="sat-table">
      <thead>
        <tr><th>Tiểu dạng</th><th>Câu hỏi mẫu Digital SAT</th><th>Chiến thuật 1500+</th></tr>
      </thead>
      <tbody>
        <tr><td><b>1. Main Purpose</b></td><td><i>"Which choice best states the main purpose of the text?"</i></td><td>Bao quát <b>toàn bộ đoạn văn</b> (không quá hẹp vào 1 chi tiết phụ, không quá rộng ngoài văn bản). Kiểm tra động từ đầu tiên: <i>to explain / to challenge / to describe / to argue</i>.</td></tr>
        <tr><td><b>2. Overall Structure</b></td><td><i>"Which choice best describes the overall structure of the text?"</i></td><td>Vẽ nhanh <b>mũi tên 2–3 chặng theo đúng thứ tự thời gian trong đoạn</b>: <code>[Nêu giả thuyết cũ] → [Đưa thí nghiệm mới] → [Đề xuất giải thích thay thế]</code>. Sai thứ tự 1 vế → Loại ngay!</td></tr>
        <tr><td><b>3. Underlined Function</b></td><td><i>"Which choice best describes the function of the underlined sentence in the text as a whole?"</i></td><td>Đọc câu <b>LIỀN TRƯỚC</b> + câu <b>GẠCH CHÂN</b> + câu <b>LIỀN SAU</b>. Hỏi: "Nếu XÓA câu gạch chân này đi, mạch lập luận mất đi vai trò gì?"</td></tr>
      </tbody>
    </table>
  </div>

  <div id="sec-rhetorical-verbs" class="lecture-interactive-card sat-card" data-lecture-section="sec_rhetorical_verbs">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>2. Giải Mã 10 Động Từ Tu Từ (Rhetorical Verbs) Hay Bị Hiểu Nhầm Nhất</h2>
    <table class="sat-table">
      <thead>
        <tr><th>Động từ tu từ trong đáp án</th><th>Nghĩa thực sự trên Digital SAT</th></tr>
      </thead>
      <tbody>
        <tr><td><b>qualify a claim / introduce a caveat</b></td><td>Đặt giới hạn, nêu điều kiện hoặc ngoại lệ cho 1 nhận định (KHÔNG bác bỏ hoàn toàn!).</td></tr>
        <tr><td><b>undermine / challenge / call into question</b></td><td>Đưa bằng chứng/lý lẽ làm lung lay một quan điểm hoặc giả thuyết có sẵn.</td></tr>
        <tr><td><b>elaborate on / expand upon</b></td><td>Bổ sung thêm chi tiết, giải thích sâu hơn cho ý ngay trước đó.</td></tr>
        <tr><td><b>illustrate / exemplify</b></td><td>Đưa ra một ví dụ/trường hợp cụ thể để minh họa cho quy luật chung.</td></tr>
        <tr><td><b>concede / acknowledge</b></td><td>Thừa nhận một hạn chế hoặc điểm hợp lý của phía đối diện (thường có <i>While / Although / Admittedly</i>).</td></tr>
        <tr><td><b>reconcile two viewpoints</b></td><td>Hòa giải, chứng minh hai quan điểm tưởng như mâu thuẫn thực ra cùng khớp với nhau.</td></tr>
      </tbody>
    </table>
  </div>

  <div id="sec-lit-structure" class="lecture-interactive-card sat-card" data-lecture-section="sec_lit_structure">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>3. Mẹo Xử Lý Đoạn Trích Văn Học &amp; Thơ Thế Kỷ 19 (1800s Fiction &amp; Poetry)</h2>
    <div class="sat-rule-box">
      <b>📖 Quy trình đọc trích đoạn văn học cổ trong 25 giây:</b><br/>
      1. Đọc ngay <b>dòng giới thiệu in nghiêng ở đầu</b> (<i>"The following text is adapted from..."</i>) để biết tên nhân vật và bối cảnh.<br/>
      2. <b>Bỏ qua chi tiết ẩn dụ rườm rà</b> nếu không hiểu 1–2 từ cổ; tập trung bắt <b>sự chuyển biến cảm xúc/trạng thái</b> (VD: từ <i>bối rối/lo âu</i> → sang <i>bình tâm/ngưỡng mộ</i>; từ <i>miêu tả cảnh vật bên ngoài</i> → sang <i>suy tư nội tâm</i>).<br/>
      3. Cẩn thận bẫy <b>Literal vs. Figurative</b>: nếu nhà thơ ví nỗi nhớ như mùa đông, đáp án nói "để miêu tả dự báo thời tiết" là bẫy nghĩa đen sai hoàn toàn!
    </div>
  </div>
''',
        quick_check_html=make_quick_check_html(
            qc_id="qc_4_3",
            passage_html="Biologists have long attributed the remarkable longevity of Greenland sharks—some exceeding four centuries—solely to their frigid Arctic habitat slowing cellular metabolism. In 2023, however, geneticists sequencing the species’ genome identified unusual duplications in DNA-repair genes rarely seen in shorter-lived vertebrates. <u>Still, the authors caution that without longitudinal tissue samples from living sharks, it remains impossible to determine how much of the animals’ lifespan stems from genetics versus cold-water physiology.</u>",
            question_prompt="Which choice best describes the function of the underlined sentence in the text as a whole?",
            options=[
                "It refutes the geneticists’ discovery by proving that DNA-repair gene duplications do not occur in Greenland sharks.",
                "It explains the laboratory procedure used to sequence the Greenland shark genome in 2023.",
                "It qualifies the 2023 genetic findings by noting a limitation that prevents isolating the relative contributions of two factors.",
                "It introduces an entirely unrelated species whose longevity rivals that of the Greenland shark."
            ],
            correct_idx=2,
            explanation_vi="Câu gạch chân mở đầu bằng 'Still, the authors caution that...' (Tuy nhiên, các tác giả cảnh báo rằng thiếu mẫu mô theo thời gian nên chưa thể xác định tỉ trọng giữa yếu tố di truyền và nước lạnh). Đây là hành động tu từ điển hình: QUALIFY the findings / introduce a methodological limitation (C). A sai vì không bác bỏ (refute) phát hiện gen; B không nói quy trình giải trình tự; D sai vì không đưa loài khác vào."
        )
    )
    seg_4_3 = [
        {
            "id": "intro",
            "title": "Giới thiệu Bài 4.3: Text Structure, Main Purpose & Function",
            "selector": "#sec-header",
            "en": "Welcome to Lesson 4.3: Text Structure, Main Purpose, and Underlined Sentence Function. Here you learn to read like a rhetorical architect, evaluating what each sentence does rather than merely what topics it mentions.",
            "vi": "Chào mừng các bạn đến với Bài 4.3: Cấu trúc đoạn văn, Mục đích chính và Chức năng câu gạch chân. Ở bài học này, bạn sẽ rèn tư duy của một kiến trúc sư tu từ: đánh giá xem câu văn đang làm chức năng gì thay vì chỉ nhặt từ khóa bề mặt."
        },
        {
            "id": "sec_three_subtypes",
            "title": "1. Ba tiểu dạng & Chiến thuật kiểm tra Động từ tu từ",
            "selector": "#sec-three-subtypes",
            "en": "Section 1 separates the three subtypes. Main Purpose must encompass the whole passage—never just one supporting detail. Overall Structure must match the exact chronological sequence of moves in the text. Underlined Function requires reading the sentence immediately before and after to see what logical link breaks if you remove it.",
            "vi": "Mục 1 phân định ba tiểu dạng. Main Purpose phải bao quát toàn bài chứ không bó hẹp ở một chi tiết lẻ. Overall Structure phải khớp đúng trình tự diễn tiến từ đầu đến cuối đoạn. Còn câu hỏi chức năng câu gạch chân đòi hỏi đọc kỹ câu liền trước và liền sau để thấy vai trò kết nối không thể thiếu của nó."
        },
        {
            "id": "sec_rhetorical_verbs",
            "title": "2. Giải mã 10 động từ tu từ dễ hiểu nhầm",
            "selector": "#sec-rhetorical-verbs",
            "en": "Section 2 decodes ten high-frequency rhetorical verbs. Pay special attention to qualify, which means placing a boundary or caveat on a claim without rejecting it, concede, which means acknowledging a limitation, and reconcile, which means showing two seemingly conflicting views actually align.",
            "vi": "Mục 2 giải mã mười động từ tu từ hay gây nhầm lẫn nhất. Đặc biệt chú ý: qualify là đặt giới hạn hay điều kiện cho một luận điểm chứ không bác bỏ hoàn toàn; concede là thừa nhận một mặt hạn chế; và reconcile là dung hòa hai quan điểm tưởng như mâu thuẫn."
        },
        {
            "id": "sec_lit_structure",
            "title": "3. Xử lý đoạn trích Văn học & Thơ thế kỷ 19",
            "selector": "#sec-lit-structure",
            "en": "Section 3 tackles nineteenth-century prose and poetry. Always read the italicized introductory attribution first, ignore unfamiliar archaic words to track the speaker's core emotional shift, and reject distractors that interpret poetic metaphors literally.",
            "vi": "Mục 3 hướng dẫn xử lý văn học và thơ cổ. Luôn đọc dòng giới thiệu in nghiêng trước để nắm bối cảnh, bỏ qua vài từ cổ khó để bám sát trục chuyển biến cảm xúc của nhân vật, và loại ngay các đáp án diễn giải ẩn dụ theo nghĩa đen."
        }
    ]
    lectures.append({
        "code": "4_3",
        "module_key": "rw_m4",
        "order_index": 3,
        "title": "4.3 Text Structure, Main Purpose & Underlined Sentence Function",
        "drill_key": "drill_4_3",
        "drill_title": "Drill 4.3: Text Structure, Main Purpose & Function (14 Qs)",
        "html": html_4_3,
        "segments": seg_4_3,
        "major_sections": {f"{s['id']}": {"start": i, "end": i} for i, s in enumerate(seg_4_3)},
    })

    # =========================================================================
    # LECTURE 4.4: Cross-Text Connections — Dual-Passage Mapping
    # =========================================================================
    html_4_4 = build_sat_lecture_html(
        badge_text="Digital SAT 1500+ • R&W Module 4 • Craft and Structure",
        title="4.4 Cross-Text Connections: Dual-Passage Mapping & Hypothetical Response",
        subtitle="Làm chủ câu hỏi 2 đoạn văn (Text 1 & Text 2): lập bản đồ quan hệ 4 trạng thái và xử lý dạng 'Tác giả 2 sẽ phản hồi Tác giả 1 thế nào?'.",
        intro_points=[
            "Xác định nhanh Ma trận 4 quan hệ giữa Text 1 và Text 2 (Direct Disagreement, Partial Agreement + Caveat, Corroboration/Extension, Different Focus/Mechanism).",
            "Áp dụng quy tắc 'Chỉ nói những gì Text 2 THỰC SỰ khẳng định' khi trả lời dạng Hypothetical Response.",
            "Tránh tuyệt đối 2 bẫy chết người: Role Swap (đảo ngược quan điểm Text 1 ↔ Text 2) và Overstated Conflict (phóng đại bất đồng nhẹ thành bác bỏ hoàn toàn).",
        ],
        cards_html='''
  <div id="sec-matrix" class="lecture-interactive-card sat-card" data-lecture-section="sec_matrix">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>1. Ma Trận 4 Quan Hệ Giữa Text 1 &amp; Text 2</h2>
    <p>Mỗi Module có 1 câu <b>Cross-Text Connections</b> (~60–75 từ mỗi Text). Đừng đọc trôi tuột cả 2 đoạn rồi quên mất ai nói gì! Hãy tóm tắt mỗi Text thành <b>1 dòng duy nhất</b> trước khi ghép quan hệ:</p>
    <table class="sat-table">
      <thead>
        <tr><th>Kiểu quan hệ</th><th>Cấu trúc thường gặp</th><th>Ngôn ngữ đáp án đúng</th></tr>
      </thead>
      <tbody>
        <tr><td><b>1. Partial Agreement + Caveat</b><br/><i>(Hay thi nhất ở 750+!)</i></td><td>Text 2 đồng ý với kết quả/hiện tượng ở Text 1, nhưng bổ sung một <b>điều kiện, giới hạn, hoặc cơ chế khác</b>.</td><td><i>agrees that X occurs, but contends that it results from Y / notes a key limitation...</i></td></tr>
        <tr><td><b>2. Direct Challenge / Refutation</b></td><td>Text 1 đưa ra giả thuyết A; Text 2 đưa bằng chứng thực nghiệm bác bỏ A.</td><td><i>challenges the claim in Text 1 by presenting evidence that...</i></td></tr>
        <tr><td><b>3. Corroboration / Support</b></td><td>Text 2 cung cấp bằng chứng từ góc độ/thời kỳ khác củng cố nhận định của Text 1.</td><td><i>provides empirical support for the hypothesis outlined in Text 1...</i></td></tr>
        <tr><td><b>4. Shared Consensus (Both Agree)</b></td><td>Cả 2 Text cùng công nhận 1 tiền đề chung dù bất đồng ở chi tiết khác.</td><td><i>Both texts would most likely agree that...</i> (Chỉ chọn điều CÓ MẶT Ở CẢ 2 TEXT!).</td></tr>
      </tbody>
    </table>
  </div>

  <div id="sec-hypothetical" class="lecture-interactive-card sat-card" data-lecture-section="sec_hypothetical">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>2. Giải Mã Dạng "Hypothetical Response" (Tác giả 2 sẽ đáp lời Tác giả 1 ra sao?)</h2>
    <div class="sat-rule-box">
      <b>🎯 Công thức 3 bước cho câu "How would the author of Text 2 most likely respond to X in Text 1?":</b><br/>
      1. <b>Khóa chặt X trong Text 1:</b> X là tuyên bố CỤ THỂ nào? (VD: <i>"Smith's claim in Text 1 that ancient trade collapsed due to drought"</i>).<br/>
      2. <b>Kiểm tra lập trường của Text 2 về ĐÚNG điểm X đó:</b> Text 2 nói gì về hạn hán hay nguyên nhân sụp đổ thương mại? (VD: Text 2 nói hạn hán chỉ ảnh hưởng vùng nội địa, còn các cảng biển vẫn giao thương mạnh nhờ tuyến hàng hải mới).<br/>
      3. <b>Loại ngay bẫy Phóng Đại &amp; Bẫy Đảo Vai:</b> Text 2 KHÔNG nói "chưa từng có hạn hán" — Text 2 chỉ nói hạn hán không làm sụp đổ toàn bộ thương mại!
    </div>
  </div>

  <div id="sec-dual-traps" class="lecture-interactive-card sat-card" data-lecture-section="sec_dual_traps">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>3. Ba Cạm Bẫy Phân Hóa 750–800 Trong Cross-Text Connections</h2>
    <div class="sat-trap-box">
      <b>• Bẫy 1 — One-Text Only (Trong câu "Both authors would agree"):</b> Đáp án hoàn toàn đúng với Text 1 nhưng Text 2 <i>không hề đề cập</i> → SAI 100%! Điểm đồng thuận phải có bằng chứng rõ ở <b>CẢ HAI ĐOẠN</b>.<br/>
      <b>• Bẫy 2 — Overstated Conflict (Thổi phồng bất đồng):</b> Text 2 chỉ nói yếu tố A <i>chưa đủ giải thích toàn bộ</i> (incomplete), nhưng đáp án nhiễu lại viết Text 2 tin rằng yếu tố A <i>hoàn toàn vô tác dụng</i> (irrelevant / completely false) → Gạch ngay!<br/>
      <b>• Bẫy 3 — Role Swap (Đánh tráo tác giả):</b> Mô tả đúng nội dung nhưng gán lập luận của Text 1 thành câu trả lời của Text 2!
    </div>
  </div>
''',
        quick_check_html=make_quick_check_html(
            qc_id="qc_4_4",
            passage_html="<b>Text 1</b><br/>Economist Clara Lindholm argues that congestion pricing in Stockholm succeeded in cutting downtown traffic by 20% primarily because commuters responded rationally to the financial toll, switching to commuter rail to save money.<br/><br/><b>Text 2</b><br/>Analyzing commuter surveys conducted before and after Stockholm’s congestion charge took effect, sociologist Tomas Berg found that toll revenue was simultaneously invested in adding 200 new express buses and expanding park-and-ride lots. Berg argues that financial tolls alone rarely shift commuter behavior unless viable, upgraded transit alternatives are rolled out at the exact same time.",
            question_prompt="Based on the texts, how would Tomas Berg (Text 2) most likely respond to Clara Lindholm’s explanation (Text 1)?",
            options=[
                "By denying that downtown traffic in Stockholm actually declined by 20% after the toll was introduced.",
                "By arguing that financial pricing is an incomplete explanation because simultaneous transit upgrades were critical to shifting commuter behavior.",
                "By claiming that Stockholm commuters ignored financial costs completely when deciding whether to drive downtown.",
                "By asserting that park-and-ride lots should replace commuter rail systems in major European cities."
            ],
            correct_idx=1,
            explanation_vi="Text 1 giải thích giảm 20% xe chủ yếu do phản ứng với phí tiền (financial toll). Text 2 KHÔNG phủ nhận mức giảm 20% (loại A) và KHÔNG nói người đi làm phớt lờ chi phí (loại C — bẫy Overstated Conflict!). Berg lập luận phí tiền ĐƠN LẺ hiếm khi đủ ('financial tolls alone rarely shift...') nếu không có nâng cấp giao thông công cộng đi kèm → B phản ánh chính xác 100% quan hệ Partial Agreement + Crucial Missing Factor."
        )
    )
    seg_4_4 = [
        {
            "id": "intro",
            "title": "Giới thiệu Bài 4.4: Cross-Text Connections — So sánh 2 đoạn văn",
            "selector": "#sec-header",
            "en": "Welcome to Lesson 4.4: Cross-Text Connections. Dual-passage items test your ability to map the exact intellectual relationship between two authors without exaggerating disagreement or mixing up who claimed what.",
            "vi": "Chào mừng các bạn đến với Bài 4.4: Liên kết hai văn bản Cross-Text Connections. Dạng bài này kiểm tra khả năng định vị chính xác mối quan hệ lập luận giữa hai tác giả mà không thổi phồng mâu thuẫn hay nhầm vai hai đoạn."
        },
        {
            "id": "sec_matrix",
            "title": "1. Ma trận 4 quan hệ Text 1 & Text 2",
            "selector": "#sec-matrix",
            "en": "Section 1 presents the four-way relationship matrix. Summarize Text 1 and Text 2 in one short line each, then identify whether Text 2 offers partial agreement with a caveat—the single most common Hard Module 2 pattern—direct refutation, independent corroboration, or shared consensus.",
            "vi": "Mục 1 đưa ra ma trận bốn mối quan hệ. Hãy tóm tắt mỗi đoạn thành một câu ngắn rồi xác định xem Text 2 đang đồng ý một phần kèm điều kiện—mẫu hay gặp nhất ở Hard Module 2—hay phản bác trực tiếp, củng cố bổ sung, hay chia sẻ tiền đề chung."
        },
        {
            "id": "sec_hypothetical",
            "title": "2. Xử lý câu hỏi Hypothetical Response",
            "selector": "#sec-hypothetical",
            "en": "Section 2 shows how to answer how Author Two would respond to Author One. Lock onto the exact claim named in the question, check precisely what Text 2 says about that specific point, and stick strictly to Text 2's stated scope.",
            "vi": "Mục 2 hướng dẫn dạng câu phản hồi giả định. Khóa chặt luận điểm cụ thể mà câu hỏi nhắc tới ở Text 1, đối chiếu xem Text 2 nói gì về đúng điểm đó và bám sát tuyệt đối phạm vi lập luận của Text 2."
        },
        {
            "id": "sec_dual_traps",
            "title": "3. Ba cạm bẫy 750–800 trong Cross-Text",
            "selector": "#sec-dual-traps",
            "en": "Section 3 flags the three deadliest traps: One-Text Only distractors on 'both agree' questions, Overstated Conflict distractors that turn a nuanced caveat into total rejection, and Role Swaps that reverse the two authors' claims.",
            "vi": "Mục 3 cảnh báo ba cạm bẫy nguy hiểm nhất: bẫy chỉ đúng một đoạn khi câu hỏi yêu cầu cả hai cùng đồng ý, bẫy thổi phồng một giới hạn nhỏ thành bác bỏ hoàn toàn, và bẫy đánh tráo quan điểm giữa hai tác giả."
        }
    ]
    lectures.append({
        "code": "4_4",
        "module_key": "rw_m4",
        "order_index": 4,
        "title": "4.4 Cross-Text Connections: Dual-Passage Mapping & Hypothetical Response",
        "drill_key": "drill_4_4",
        "drill_title": "Drill 4.4: Cross-Text Connections — Dual-Passage Mapping (14 Qs)",
        "html": html_4_4,
        "segments": seg_4_4,
        "major_sections": {f"{s['id']}": {"start": i, "end": i} for i, s in enumerate(seg_4_4)},
    })

    return lectures
