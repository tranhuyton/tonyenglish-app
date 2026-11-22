# -*- coding: utf-8 -*-
from sat_audio_pipeline import build_sat_lecture_html, make_quick_check_html

def get_stage4_lectures():
    lectures = []

    # =========================================================================
    # LECTURE 5.1: Central Ideas & Details — Dense Prose & Poetry
    # =========================================================================
    html_5_1 = build_sat_lecture_html(
        badge_text="Digital SAT 1500+ • R&W Module 5 • Information and Ideas (Hard M2)",
        title="5.1 Central Ideas & Details: Decoding Dense Academic Prose & 19th-Century Poetry",
        subtitle="Tách trục ý chính khỏi chi tiết trang trí, tiêu diệt bẫy Too Broad / Too Narrow / Distortion và đọc chuẩn từng chữ cho câu hỏi Detail.",
        intro_points=[
            "Phân biệt rạch ròi chiến thuật làm Main Idea (tổng hợp toàn đoạn) vs. Detail (định vị đúng 1 câu bằng chứng duy nhất).",
            "Ứng dụng quy trình 'Bóc vỏ Câu phức' (Subject + Core Action + Contrast Pivot) cho các đoạn văn khoa học dài 140 từ.",
            "Loại trừ triệt để 4 bẫy kinh điển của Information & Ideas: Too Narrow, Too Broad, Unsupported Comparison và Subtle Distortion.",
        ],
        cards_html='''
  <div id="sec-main-vs-detail" class="lecture-interactive-card sat-card" data-lecture-section="sec_main_vs_detail">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>1. Tách Chiến Thuật: Main Idea vs. Specific Detail</h2>
    <table class="sat-table">
      <thead>
        <tr><th>Dạng câu hỏi</th><th>Câu hỏi mẫu Digital SAT</th><th>Quy trình giải chuẩn 780–800</th></tr>
      </thead>
      <tbody>
        <tr><td><b>Central Idea / Main Idea</b></td><td><i>"Which choice best states the main idea of the text?"</i></td><td>Gom <b>Chủ thể chính + Điểm xoay (However/Yet/Instead) + Kết luận trọng tâm</b>. Phải bao quát ĐỦ toàn đoạn (không bị lọt vào 1 ví dụ phụ).</td></tr>
        <tr><td><b>Specific Detail</b></td><td><i>"According to the text, why did X...?"</i> / <i>"Based on the text, what is true about Y?"</i></td><td>Bắt chính xác <b>từ khóa định vị</b> trong câu hỏi → quay lại đúng 1–2 câu chứa từ khóa đó → tìm đáp án là <b>bản diễn giải sát nghĩa (Direct Paraphrase)</b> của đúng câu đó!</td></tr>
      </tbody>
    </table>
    <div class="sat-gold-box">
      <b>🔍 Quy tắc "Chữ Đồng Nghĩa Thay Cho Chữ Lặp" (Paraphrase vs. Word-Salad Trap):</b><br/>
      Đáp án NHIỄU ở Hard Module 2 thường <b>nhại lại nguyên si 5–6 từ vựng nổi bật trong bài</b> nhưng ghép chúng sai mối quan hệ! Ngược lại, đáp án ĐÚNG thường <b>diễn đạt lại bằng từ vựng khác (paraphrase)</b> nhưng bảo toàn 100% logic gốc!
    </div>
  </div>

  <div id="sec-four-traps" class="lecture-interactive-card sat-card" data-lecture-section="sec_four_traps">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>2. Bốn Bẫy Chết Người Của Central Ideas &amp; Details</h2>
    <table class="sat-table">
      <thead>
        <tr><th>Loại bẫy</th><th>Cách nhận diện nhanh</th></tr>
      </thead>
      <tbody>
        <tr><td><b>1. Too Narrow (Quá hẹp)</b></td><td>Hoàn toàn đúng sự thật trong bài, nhưng chỉ tóm tắt <b>1 câu ví dụ phụ</b> chứ không phải thông điệp bao trùm (đặc biệt nguy hiểm cho câu Main Idea!).</td></tr>
        <tr><td><b>2. Too Broad / Out of Scope</b></td><td>Mở rộng kết quả của 1 nghiên cứu/1 loài thành quy luật của <i>"all species" / "most historians" / "worldwide"</i>.</td></tr>
        <tr><td><b>3. Unsupported Comparison</b></td><td>Bài nhắc cả X và Y, nhưng KHÔNG hề so sánh "X lớn hơn / tốt hơn / phổ biến hơn Y" — đáp án nhiễu lén nhét từ <i>more than / superior / primarily</i>!</td></tr>
        <tr><td><b>4. Subtle Distortion (Đánh tráo sắc thái)</b></td><td>Bài nói <i>"researchers were unable to verify X"</i> → đáp án nhiễu bẻ thành <i>"researchers proved X was false"</i>! (Không xác minh được ≠ Chứng minh là sai!).</td></tr>
      </tbody>
    </table>
  </div>

  <div id="sec-poetry-detail" class="lecture-interactive-card sat-card" data-lecture-section="sec_poetry_detail">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>3. Đọc Thẳng Tâm Điểm Trong Văn Học &amp; Thơ Cổ Điển</h2>
    <div class="sat-rule-box">
      <b>📚 Kỹ thuật "Lột Bỏ Tính Từ Hoa Mỹ":</b><br/>
      Khi gặp câu thơ hoặc văn xuôi thế kỷ 19 dài 50 từ, hãy tìm ngay cặp <b>Chủ ngữ – Động từ cốt lõi</b> của từng câu và gạt bỏ các cụm ẩn dụ xen giữa trong lần đọc đầu.<br/>
      <i>Ví dụ:</i> Thay vì rối trước <i>"Beneath the gilded boughs of autumn’s fading splendor, the solitary traveler tarried not for solace..."</i> → rút gọn ngay: <b>"The traveler stopped — NOT for comfort, but for [X]!"</b> → Trả lời câu hỏi chính xác 100% không tốn thời gian!
    </div>
  </div>
''',
        quick_check_html=make_quick_check_html(
            qc_id="qc_5_1",
            passage_html="In a 2023 archival review of seventeenth-century Japanese botanical encyclopedias, historian Dr. Akiko Sato observed that illustrations of medicinal roots were far more anatomically exact than portraits of ornamental blossoms. Because physicians relied on these woodblock plates to distinguish toxic look-alikes from healing herbs in rural clinics without access to fresh specimens, Sato concluded that functional survival demands—rather than purely decorative tastes—drove the era’s precision in botanical printmaking.",
            question_prompt="Which choice best states the main idea of the text?",
            options=[
                "Seventeenth-century Japanese artists lacked the technical skill required to depict ornamental blossoms accurately.",
                "Practical medical needs, rather than purely aesthetic preferences, motivated the high anatomical precision found in seventeenth-century Japanese depictions of medicinal plants.",
                "Rural clinics in seventeenth-century Japan had abundant access to fresh medicinal herbs throughout the year.",
                "Dr. Akiko Sato proved that woodblock printmaking was more accurate than oil painting for documenting medicinal herbs."
            ],
            correct_idx=1,
            explanation_vi="Câu cuối chốt trực tiếp Main Idea: nhu cầu thực tiễn y học để phân biệt cây độc và cây thuốc ('functional survival demands') — chứ không phải gu trang trí thuần túy — đã thúc đẩy độ chính xác giải phẫu trong tranh in thực vật (B). A suy diễn sai ('lacked technical skill'); C mâu thuẫn thẳng ('without access to fresh specimens'); D dính bẫy Unsupported Comparison ('oil painting' không hề có trong bài)."
        )
    )
    seg_5_1 = [
        {
            "id": "intro",
            "title": "Giới thiệu Bài 5.1: Central Ideas & Details",
            "selector": "#sec-header",
            "en": "Welcome to Module 5, the Hard Module 2 Gauntlet. Lesson 5.1 tackles Central Ideas and Details—the foundation of Information and Ideas. Mastering accurate paraphrasing while rejecting word-salad traps is essential for breaking 750.",
            "vi": "Chào mừng các bạn bước vào Module 5, vùng phân hóa quyết định của Hard Module 2. Bài 5.1 xử lý dạng Ý chính và Chi tiết—nền móng của miền Information and Ideas. Làm chủ kỹ năng nhận diện diễn giải tương đương và loại bỏ bẫy nhại chữ là chìa khóa vượt mốc 750."
        },
        {
            "id": "sec_main_vs_detail",
            "title": "1. Tách chiến thuật Main Idea vs. Detail",
            "selector": "#sec-main-vs-detail",
            "en": "Section 1 distinguishes Main Idea from Detail. For Main Idea, synthesize the subject, contrast pivot, and central conclusion across the whole passage. For Detail questions, locate the exact anchor sentence and match its direct paraphrase. Beware the Word-Salad Trap: wrong answers often recycle flashy words straight from the passage while scrambling their actual relationship.",
            "vi": "Mục 1 tách biệt chiến thuật hai tiểu dạng. Với Ý chính, hãy gom chủ thể, bước ngoặt đối lập và kết luận bao trùm cả đoạn. Với Chi tiết, tìm đúng câu chứa từ khóa rồi khớp bản diễn đạt lại sát nghĩa. Đặc biệt tránh bẫy nhại chữ: đáp án sai thường chép y nguyên từ vựng nổi bật trong bài nhưng ghép sai mối quan hệ."
        },
        {
            "id": "sec_four_traps",
            "title": "2. Bốn bẫy chết người của Central Ideas & Details",
            "selector": "#sec-four-traps",
            "en": "Section 2 exposes four classic distractors: Too Narrow choices that summarize only one supporting example; Too Broad extrapolations; Unsupported Comparisons that sneak in words like more than or superior; and Subtle Distortions—for instance, turning unable to verify into proved false.",
            "vi": "Mục 2 vạch trần bốn cái bẫy kinh điển: đáp án quá hẹp chỉ tóm tắt một ví dụ lẻ; suy rộng quá phạm vi bài; so sánh không có căn cứ khi bài không hề nói cái nào hơn cái nào; và đánh tráo sắc thái tinh vi, chẳng hạn biến chưa thể xác minh thành đã chứng minh là sai."
        },
        {
            "id": "sec_poetry_detail",
            "title": "3. Lột bỏ tính từ hoa mỹ trong văn học & thơ cổ",
            "selector": "#sec-poetry-detail",
            "en": "Section 3 shows how to strip ornate nineteenth-century prose and poetry down to its core subject-verb skeleton. Ignore decorative adjectives on your first pass and lock onto the exact emotional or narrative action.",
            "vi": "Mục 3 hướng dẫn cách đọc nhanh văn học và thơ cổ thế kỷ 19: lược bỏ các cụm tính từ trang trí ở lượt đọc đầu để tóm gọn ngay bộ khung chủ ngữ và hành động cốt lõi của nhân vật."
        }
    ]
    lectures.append({
        "code": "5_1",
        "module_key": "rw_m5",
        "order_index": 1,
        "title": "5.1 Central Ideas & Details: Decoding Dense Academic Prose & 19th-Century Poetry",
        "drill_key": "drill_5_1",
        "drill_title": "Drill 5.1: Central Ideas & Details — Hard Module 2 Prose & Poetry (13 Qs)",
        "html": html_5_1,
        "segments": seg_5_1,
        "major_sections": {f"{s['id']}": {"start": i, "end": i} for i, s in enumerate(seg_5_1)},
    })

    # =========================================================================
    # LECTURE 5.2: Command of Evidence — Textual (Scientific Claims)
    # =========================================================================
    html_5_2 = build_sat_lecture_html(
        badge_text="Digital SAT 1500+ • R&W Module 5 • Information and Ideas (Hard M2)",
        title="5.2 Command of Evidence — Textual: Supporting & Weakening Scientific Hypotheses",
        subtitle="Chinh phục câu hỏi phân hóa số 1 của Hard Module 2: khóa chặt Giả thuyết (Hypothesis), kiểm soát Biến nhiễu và phân biệt Support vs. Weaken.",
        intro_points=[
            "Áp dụng công thức 2 biến 'Cause (X) → Effect (Y)' để tóm gọn mọi giả thuyết khoa học phức tạp trong 10 giây.",
            "Nắm cơ chế Support (X có → Y có; loại trừ biến nhiễu khác) và Weaken (X có → Y KHÔNG xảy ra; hoặc Y xảy ra dù KHÔNG có X; hoặc do biến nhiễu Z gây ra!).",
            "Tiêu diệt bẫy 'Nghe có vẻ khoa học nhưng lệch trục X → Y' trên các bài sinh thái, khảo cổ và tâm lý học.",
        ],
        cards_html='''
  <div id="sec-claim-lock" class="lecture-interactive-card sat-card" data-lecture-section="sec_claim_lock">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>1. Công Thức "Khóa Trục Giả Thuyết" (X → Y Hypothesis Lock)</h2>
    <p>Trong dạng <i>"Which finding, if true, would most directly <b>support / weaken</b> the researchers’ hypothesis?"</i>, đoạn văn thường dài 120–150 từ chứa rất nhiều chi tiết nền. <b>90% lỗi sai đến từ việc học sinh đánh nhầm giả thuyết!</b></p>
    <div class="sat-rule-box">
      <b>🎯 Bước 1 — Tìm đúng CHỦ SỞ HỮU của Hypothesis trong câu hỏi:</b><br/>
      Đoạn văn có thể nhắc <b>Giả thuyết CŨ của giới khoa học</b> (Traditional view) lẫn <b>Giả thuyết MỚI của nhóm nghiên cứu</b> (Dr. Lee’s hypothesis). Đọc câu hỏi thật kỹ xem họ yêu cầu support/weaken <b>AI</b>!<br/><br/>
      <b>🎯 Bước 2 — Rút gọn giả thuyết đó thành mũi tên 2 biến:</b><br/>
      Ví dụ: <i>"Dr. Lee hypothesizes that nocturnal moths avoid bat predation primarily by evolving fuzzy thorax scales that absorb ultrasonic echoes."</i><br/>
      → Khóa trục: <span class="sat-code">Fuzzy Scales (X) → Absorb Echoes / Reduce Bat Detection (Y)</span>.
    </div>
  </div>

  <div id="sec-support-weaken" class="lecture-interactive-card sat-card" data-lecture-section="sec_support_weaken">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>2. Ma Trận Support vs. Weaken Chuẩn 780–800</h2>
    <table class="sat-table">
      <thead>
        <tr><th>Yêu cầu đề bài</th><th>Bằng chứng ĐÚNG phải chứng minh điều gì?</th><th>Ví dụ với trục <code>Fuzzy Scales (X) → Reduce Detection (Y)</code></th></tr>
      </thead>
      <tbody>
        <tr>
          <td><b>DIRECTLY SUPPORT</b><br/><i>(Ủng hộ trực tiếp)</i></td>
          <td>• Có X → Y xảy ra rõ rệt; bỏ X đi (nhóm đối chứng) → Y biến mất!<br/>• Loại bỏ được nguyên nhân thay thế (Z).</td>
          <td>Khi cạo lớp lông ngực (bỏ X), tiếng vang siêu âm phản xạ lại mạnh hơn hẳn và dơi bắt bướm đêm dễ hơn nhiều (Y biến mất)!</td>
        </tr>
        <tr>
          <td><b>DIRECTLY WEAKEN / UNDERMINE</b><br/><i>(Làm suy yếu trực tiếp)</i></td>
          <td><b>1 trong 3 đòn chí mạng:</b><br/>1. Có X nhưng <b>KHÔNG có Y</b>.<br/>2. Không có X nhưng <b>vẫn có Y y hệt</b>.<br/>3. Đưa ra <b>Biến nhiễu Z (Alternative Cause)</b> mới là nguyên nhân thực sự tạo ra Y!</td>
          <td>Bướm đêm bị cạo sạch lớp lông ngực (không có X) vẫn né được dơi ở tỉ lệ y hệt bướm còn nguyên lông — hóa ra loài này phát tín hiệu nhiễu từ cơ quan ở chân (biến Z)!</td>
        </tr>
      </tbody>
    </table>
  </div>

  <div id="sec-science-traps" class="lecture-interactive-card sat-card" data-lecture-section="sec_science_traps">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>3. Ba Bẫy Kinh Điển Khi Chọn Bằng Chứng Khoa Học</h2>
    <div class="sat-trap-box">
      <b>• Bẫy 1 — Missing Control Comparison (Thiếu nhóm đối chứng):</b> Chỉ nói <i>"Bướm đêm có lông sống trong rừng nhiệt đới"</i> mà không so sánh giữa có X vs. không X → Không chứng minh được X gây ra Y!<br/>
      <b>• Bẫy 2 — Wrong Direction (Ngược chiều Support ↔ Weaken):</b> Đáp án hoàn toàn liên quan đến đúng X và Y, nhưng lại <b>ủng hộ</b> trong khi đề hỏi <b>weaken</b> (hoặc ngược lại) — học sinh hay sập bẫy khi đọc nhanh quên chữ <i>weaken / undermine</i>!<br/>
      <b>• Bẫy 3 — Adjacent Topic Drift:</b> Bàn về một đặc điểm khác của loài dơi (tốc độ bay, mùa sinh sản) không dính dáng đến biến X (lông hấp thụ sóng âm).
    </div>
  </div>
''',
        quick_check_html=make_quick_check_html(
            qc_id="qc_5_2",
            passage_html="Geologists studying the arid Atacama Desert noticed enigmatic patches of small quartz stones arranged in neat concentric rings across flat clay basins. Dr. Mateo Ruiz hypothesized that these rings form purely through abiotic freeze-thaw cycles that gradually push pebbles outward as subterranean moisture expands and contracts, rather than through any activity by burrowing animals.",
            question_prompt="Which finding, if true, would most directly weaken Dr. Mateo Ruiz’s hypothesis?",
            options=[
                "Quartz pebbles in the Atacama Desert exhibit slightly higher iron-oxide staining than pebbles in neighboring valleys.",
                "Identical concentric quartz rings occur exclusively around the entrances of active subterranean rodent burrows and never appear in adjacent clay basins experiencing identical freeze-thaw cycles without rodents.",
                "Subterranean moisture levels in the Atacama Desert fluctuate significantly between winter nights and summer afternoons.",
                "Several other arid basins in South America contain flat clay plains formed by ancient evaporated lakes."
            ],
            correct_idx=1,
            explanation_vi="Khóa giả thuyết Ruiz: Purely abiotic freeze-thaw (X) → quartz rings (Y), NOT animals. Để WEAKEN trực tiếp: tìm bằng chứng cho thấy cùng chu kỳ freeze-thaw (có X) mà KHÔNG có động vật thì KHÔNG có vòng đá (không có Y), trong khi vòng đá chỉ xuất hiện quanh hang động vật gặm nhấm (Alternative Cause Z)! Chọn B! C thực ra là Support nhẹ (ngược chiều); A và D là Adjacent Topic Drift."
        )
    )
    seg_5_2 = [
        {
            "id": "intro",
            "title": "Giới thiệu Bài 5.2: Command of Evidence — Khoa học",
            "selector": "#sec-header",
            "en": "Welcome to Lesson 5.2: Textual Command of Evidence for Scientific Claims. These Support and Weaken questions are the signature separator of Hard Module 2—and they become crystal clear once you translate every hypothesis into an X-to-Y causal arrow.",
            "vi": "Chào mừng các bạn đến với Bài 5.2: Bằng chứng văn bản cho Giả thuyết Khoa học. Dạng câu hỏi Ủng hộ hay Làm suy yếu giả thuyết là cửa ải phân hóa khốc liệt nhất của Hard Module 2, nhưng sẽ trở nên cực kỳ rõ ràng khi bạn quy mọi giả thuyết về trục nhân quả X dẫn tới Y."
        },
        {
            "id": "sec_claim_lock",
            "title": "1. Khóa đúng Chủ sở hữu & Trục X → Y",
            "selector": "#sec-claim-lock",
            "en": "Section 1 shows the Hypothesis Lock. First, confirm whose hypothesis the question asks about—never mix up an old consensus with the researcher's new proposal. Second, boil that exact claim down to a clean two-variable arrow: Cause X produces Effect Y.",
            "vi": "Mục 1 hướng dẫn kỹ thuật Khóa Giả thuyết. Trước hết phải xác minh chính xác câu hỏi muốn chứng minh hay bác bỏ giả thuyết của ai, tránh nhầm giữa quan điểm cũ và đề xuất mới. Sau đó rút gọn ngay giả thuyết ấy thành mũi tên hai biến: Nguyên nhân X tạo ra Hệ quả Y."
        },
        {
            "id": "sec_support_weaken",
            "title": "2. Ma trận Support vs. Weaken chuẩn 780–800",
            "selector": "#sec-support-weaken",
            "en": "Section 2 details the exact logic of proof. To directly support X causes Y, show that adding X produces Y while removing X eliminates Y. To directly weaken it, deploy one of three knockout blows: X occurs without Y, Y occurs without X, or an alternative confounding variable Z actually drives Y.",
            "vi": "Mục 2 trình bày ma trận chứng minh chuẩn xác. Để ủng hộ trực tiếp X gây ra Y, hãy tìm bằng chứng có X thì có Y và khi bỏ X ở nhóm đối chứng thì Y biến mất. Để làm suy yếu trực tiếp, tìm một trong ba đòn quyết định: có X mà không có Y, không có X vẫn có Y, hoặc một biến nhiễu Z khác mới là nguyên nhân thật sự."
        },
        {
            "id": "sec_science_traps",
            "title": "3. Ba bẫy kinh điển của bài khoa học",
            "selector": "#sec-science-traps",
            "en": "Section 3 highlights the three traps to eliminate: findings lacking any control comparison, Opposite-Direction lures that support when the prompt demands weaken, and adjacent-topic drift that sounds scientific while ignoring variable X altogether.",
            "vi": "Mục 3 cảnh báo ba cạm bẫy phổ biến: dữ kiện thiếu nhóm đối chứng, đáp án ngược chiều khi đọc vội bỏ sót chữ weaken, và thông tin nghe rất khoa học nhưng trôi lệch hẳn khỏi biến X của giả thuyết."
        }
    ]
    lectures.append({
        "code": "5_2",
        "module_key": "rw_m5",
        "order_index": 2,
        "title": "5.2 Command of Evidence — Textual: Supporting & Weakening Scientific Hypotheses",
        "drill_key": "drill_5_2",
        "drill_title": "Drill 5.2: Command of Evidence — Scientific Claims (13 Qs)",
        "html": html_5_2,
        "segments": seg_5_2,
        "major_sections": {f"{s['id']}": {"start": i, "end": i} for i, s in enumerate(seg_5_2)},
    })

    # =========================================================================
    # LECTURE 5.3: Command of Evidence — Literary & Historical Quotations
    # =========================================================================
    html_5_3 = build_sat_lecture_html(
        badge_text="Digital SAT 1500+ • R&W Module 5 • Information and Ideas (Hard M2)",
        title="5.3 Command of Evidence — Literary & Historical Quotations",
        subtitle="Quy trình 'Checklist Từng Vế' (Checklist Matching) giúp chọn chính xác trích dẫn thơ hoặc tiểu thuyết minh họa cho nhận định phê bình.",
        intro_points=[
            "Tách nhận định phê bình (Literary Claim) thành 2–3 yêu cầu thành phần bắt buộc (Checkboxes) trước khi đọc 4 đoạn trích.",
            "Loại ngay các trích dẫn chỉ thỏa mãn 1 nửa Claim (bẫy Half-Match) hoặc chỉ lặp lại danh từ chủ đề mà sai cảm xúc/thái độ.",
            "Dịch nhanh ẩn dụ & giọng điệu trong thơ/văn xuôi cổ sang ngôn ngữ hiện đại để đối chiếu chuẩn 100%.",
        ],
        cards_html='''
  <div id="sec-checklist" class="lecture-interactive-card sat-card" data-lecture-section="sec_checklist">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>1. Phương Pháp "Checklist Từng Vế" (Multi-Part Claim Checklist)</h2>
    <p>Trong dạng <i>"Which quotation from [novel/poem] most effectively illustrates the claim?"</i>, đoạn văn mở đầu chỉ dài 2–3 câu nhưng <b>MỌI TÍNH TỪ trong câu Claim đều là điều kiện lọc</b>!</p>
    <div class="sat-gold-box">
      <b>✅ Cách tách Claim thành Checklist 2–3 ô vuông:</b><br/>
      <i>Claim mẫu:</i> "A literary critic argues that in the novel, the narrator views the industrial shipyard with <b>[1] awe at its mechanical power</b> yet <b>[2] unease over its human toll</b>."<br/><br/>
      → Bạn lập ngay 2 ô kiểm: <code>[✓] Ngưỡng mộ sức mạnh cơ khí</code> + <code>[✓] Bất an về cái giá con người phải trả</code>.<br/>
      • Trích dẫn A chỉ khen máy móc hùng vĩ (đạt [1], thiếu [2]) → <b>LOẠI!</b><br/>
      • Trích dẫn B chỉ tả công nhân kiệt sức (đạt [2], thiếu [1]) → <b>LOẠI!</b><br/>
      • Trích dẫn C thể hiện RÕ CẢ HAI vế đối nghịch trong cùng 2 câu trích → <b>CHỐT 100%!</b>
    </div>
  </div>

  <div id="sec-lit-traps" class="lecture-interactive-card sat-card" data-lecture-section="sec_lit_traps">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>2. Ba Bẫy Kinh Điển Của Câu Trích Dẫn Văn Học</h2>
    <table class="sat-table">
      <thead>
        <tr><th>Loại bẫy</th><th>Cách College Board đánh lừa</th><th>Cách hóa giải</th></tr>
      </thead>
      <tbody>
        <tr><td><b>1. Topic Keyword Lure</b></td><td>Trích dẫn chứa đúng tên nhân vật, địa danh hoặc đồ vật trong Claim (VD: nhắc chữ "shipyard" hoặc "river") nhưng hành động/cảm xúc lại hoàn toàn khác!</td><td>Không bao giờ chọn trích dẫn chỉ vì thấy trùng danh từ — luôn đối chiếu <b>Thái độ &amp; Luận điểm</b> của Claim.</td></tr>
        <tr><td><b>2. Half-Match Trap</b></td><td>Khớp tuyệt vời nửa đầu của Claim nhưng thiếu hẳn nửa sau (đặc biệt khi Claim có từ <i>both... and..., yet, while, simultaneously</i>).</td><td>Đánh số [1] và [2] lên Claim; trích dẫn thiếu bất kỳ vế nào → gạch thẳng tay!</td></tr>
        <tr><td><b>3. Wrong Character / Direction</b></td><td>Claim nói <i>Nhân vật A không tin tưởng Nhân vật B</i>, nhưng trích dẫn lại tả <i>Nhân vật B không tin tưởng Nhân vật A</i> (đảo chiều!).</td><td>Kiểm tra đại từ nhân xưng ("I / he / she / they") xem ai là người đang nói và nói về ai!</td></tr>
      </tbody>
    </table>
  </div>

  <div id="sec-metaphor" class="lecture-interactive-card sat-card" data-lecture-section="sec_metaphor">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>3. Dịch Ẩn Dụ Thơ Sang Ngôn Ngữ Trực Tiếp</h2>
    <div class="sat-rule-box">
      <b>🎭 Mẹo dịch ẩn dụ nhanh:</b><br/>
      • Hình ảnh thiên nhiên <i>(frozen brook, winter ash, crumbling stone)</i> thường đại diện cho <b>thời gian trôi qua, sự tàn phai hoặc nỗi cô đơn</b>.<br/>
      • Hình ảnh ánh sáng/nhịp điệu <i>(unbroken loom, steady ember, returning tide)</i> thường đại diện cho <b>sự bền bỉ, ký ức dai dẳng hoặc hy vọng tái sinh</b>.<br/>
      • Nếu Claim dùng từ <i>"irony / skepticism / quiet defiance"</i>, hãy tìm những câu trích mang <b>độ vênh mỉa mai giữa lời nói lịch sự bề ngoài và thực tế bên trong</b>!
    </div>
  </div>
''',
        quick_check_html=make_quick_check_html(
            qc_id="qc_5_3",
            passage_html="In an analysis of the 1912 novel <i>The Harbor Lantern</i>, a student claims that the protagonist, Miriam, experiences a sudden realization that her childhood memory of her hometown is far more idealized than the worn, ordinary town standing before her.",
            question_prompt="Which quotation from <i>The Harbor Lantern</i> most effectively illustrates the student’s claim?",
            options=[
                "“Miriam stepped onto the wooden ferry dock and immediately recognized the familiar salt scent drifting across the harbor.”",
                "“For ten years she had carried the main street in her mind like a painted boulevard of white marble; seeing its peeling shutters and narrow muddy lane now made her wonder how a single decade could shrink a kingdom into a village.”",
                "“Neighbors waved warmly from the bakery doorway as Miriam carried her leather suitcase up the steep hill toward her aunt’s house.”",
                "“Had she stayed in the coastal town after turning eighteen, Miriam often reflected, she might never have seen the museums and theaters of the capital.”"
            ],
            correct_idx=1,
            explanation_vi="Checklist từ Claim: [1] Ký ức tuổi thơ được lý tưởng hóa quá mức ('idealized') + [2] Thị trấn thực tế cũ kỹ tầm thường ('worn, ordinary') + [3] Nhận ra độ vênh giữa hai hình ảnh ('sudden realization'). Trích dẫn B khớp tuyệt đối cả 3 vế: ký ức như 'painted boulevard of white marble / kingdom' đối lập thẳng với thực tế 'peeling shutters and narrow muddy lane / village'!"
        )
    )
    seg_5_3 = [
        {
            "id": "intro",
            "title": "Giới thiệu Bài 5.3: Trích dẫn Văn học & Lịch sử",
            "selector": "#sec-header",
            "en": "Welcome to Lesson 5.3: Command of Evidence with Literary and Historical Quotations. Instead of getting lost in nineteenth-century prose or poetry, you will convert every critic's claim into a strict multi-part checklist.",
            "vi": "Chào mừng các bạn đến với Bài 5.3: Bằng chứng trích dẫn Văn học và Lịch sử. Thay vì bị choáng trước thơ hay tiểu thuyết cổ, bạn sẽ chuyển mọi nhận định phê bình thành một danh sách kiểm tra từng vế cực kỳ chính xác."
        },
        {
            "id": "sec_checklist",
            "title": "1. Phương pháp Checklist Từng Vế",
            "selector": "#sec-checklist",
            "en": "Section 1 demonstrates Multi-Part Claim Checklisting. Break the claim into two or three concrete checkboxes—especially whenever words like both, yet, or while appear. Any quotation that matches only half of the claim must be crossed out immediately.",
            "vi": "Mục 1 hướng dẫn phương pháp lập Checklist từng vế. Hãy tách nhận định phê bình thành hai hoặc ba tiêu chí bắt buộc—đặc biệt khi câu chứa từ both, yet hoặc while. Bất kỳ câu trích nào chỉ khớp được một nửa yêu cầu đều phải gạch bỏ ngay lập tức."
        },
        {
            "id": "sec_lit_traps",
            "title": "2. Ba bẫy kinh điển của câu trích dẫn văn học",
            "selector": "#sec-lit-traps",
            "en": "Section 2 warns against three traps: Topic Keyword Lures that repeat nouns from the claim without proving its point, Half-Match quotations missing one key adjective, and Wrong-Direction quotes that reverse which character holds which attitude.",
            "vi": "Mục 2 vạch trần ba bẫy hay gặp: bẫy lặp từ khóa chủ đề nhưng lệch luận điểm, bẫy chỉ khớp một nửa nhận định, và bẫy đảo chiều nhân vật khiến thái độ bị gán nhầm người."
        },
        {
            "id": "sec_metaphor",
            "title": "3. Giải mã ẩn dụ thơ nhanh gọn",
            "selector": "#sec-metaphor",
            "en": "Section 3 shows how to translate poetic imagery directly into plain English themes—matching motifs of winter and stone to impermanence, embers and tides to endurance, and polite understatement to quiet irony.",
            "vi": "Mục 3 hướng dẫn dịch nhanh hình ảnh thơ ẩn dụ sang ý nghĩa trực diện: mùa đông hay đá vỡ thường gợi sự tàn phai, than hồng hay thủy triều gợi sự bền bỉ, còn sự vênh giữa lời lẽ lịch sự và thực tế thường báo hiệu giọng điệu mỉa mai."
        }
    ]
    lectures.append({
        "code": "5_3",
        "module_key": "rw_m5",
        "order_index": 3,
        "title": "5.3 Command of Evidence — Literary & Historical Quotations",
        "drill_key": "drill_5_3",
        "drill_title": "Drill 5.3: Command of Evidence — Literary & Historical Quotations (13 Qs)",
        "html": html_5_3,
        "segments": seg_5_3,
        "major_sections": {f"{s['id']}": {"start": i, "end": i} for i, s in enumerate(seg_5_3)},
    })

    # =========================================================================
    # LECTURE 5.4: Command of Evidence — Quantitative (Graphs & Tables)
    # =========================================================================
    html_5_4 = build_sat_lecture_html(
        badge_text="Digital SAT 1500+ • R&W Module 5 • Information and Ideas (Hard M2)",
        title="5.4 Command of Evidence — Quantitative: Charts, Tables & The 'True Data, Wrong Claim' Trap",
        subtitle="Quy trình 3 bước bất bại cho mọi câu Biểu đồ & Bảng số liệu: Chốt Claim → Lọc sai số liệu → Khớp logic chứng minh.",
        intro_points=[
            "KHÔNG phân tích hết toàn bộ bảng trước khi đọc bài — hãy đọc Text & Chốt Claim TRƯỚC để biết cần nhìn vào hàng/cột nào.",
            "Nhận diện và tiêu diệt bẫy số 1 của Quantitative Evidence: 'True Data, Wrong Claim' (đọc đúng 100% số liệu bảng nhưng không hề chứng minh/bác bỏ Claim!).",
            "Kiểm tra kỹ Đơn vị trục (%, thousands, log scale, per capita vs. total) và Chú thích (Legend) để không bao giờ mất điểm oan.",
        ],
        cards_html='''
  <div id="sec-three-step-quant" class="lecture-interactive-card sat-card" data-lecture-section="sec_three_step_quant">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>1. Quy Trình 3 Bước Đọc Biểu Đồ &amp; Bảng Chuẩn 780–800</h2>
    <p>Sai lầm khiến học sinh mất 2 phút ở câu biểu đồ là cắm cúi soi từng con số trong bảng ngay từ giây đầu tiên! Hãy đảo ngược quy trình:</p>
    <div class="sat-gold-box">
      <b>⚡ Quy trình 3 Bước Quantitative SOP (≤60 giây/câu):</b><br/>
      <b>• Bước 1 — Đọc ĐOẠN VĂN &amp; CÂU HỎI TRƯỚC:</b> Gạch chân chính xác <b>Claim cần Support / Weaken / Complete</b> (VD: <i>"tuyên bố rằng doanh thu tăng nhờ xuất khẩu chứ không phải bán nội địa"</i>). Chỉ lúc này mới liếc tiêu đề bảng, trục X/Y và đơn vị!<br/>
      <b>• Bước 2 — Bộ lọc Sự thật (Data Accuracy Filter):</b> Quét nhanh 4 đáp án đối chiếu với bảng/biểu đồ. Bất kỳ đáp án nào <b>nói sai số liệu, ngược xu hướng, hoặc nhầm cột/đơn vị</b> → Gạch ngay (thường loại được 1–2 đáp án).<br/>
      <b>• Bước 3 — Bộ lọc Luận điểm (Claim Relevance Filter — CỬA ẢI 750+!):</b> Trong 2–3 đáp án ĐỀU ĐÚNG SỐ LIỆU, chỉ giữ đáp án <b>trực tiếp chứng minh (hoặc bác bỏ) ĐÚNG VẾ LOGIC của Claim</b>!
    </div>
  </div>

  <div id="sec-quant-traps" class="lecture-interactive-card sat-card" data-lecture-section="sec_quant_traps">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>2. Bốn Bẫy Sát Thủ Trên Biểu Đồ &amp; Bảng Digital SAT</h2>
    <table class="sat-table">
      <thead>
        <tr><th>Loại bẫy</th><th>Cơ chế đánh lừa</th><th>Cách kiểm chứng 2 giây</th></tr>
      </thead>
      <tbody>
        <tr><td><b>1. True Data, Wrong Claim</b><br/><i>(Xuất hiện trong 90% câu!)</i></td><td>Chép đúng hoàn hảo các con số trong bảng, nhưng lại so sánh sai cặp biến hoặc bỏ qua điều kiện của Claim.</td><td>Hỏi: "Nếu con số này đúng, nó có THỰC SỰ chứng minh/bác bỏ tuyên bố của tác giả không?"</td></tr>
        <tr><td><b>2. Raw Count vs. Percentage / Rate</b></td><td>Bảng cho <b>Tỉ lệ %</b> (VD: 40% ở nhóm A vs. 30% ở nhóm B), nhưng đáp án nhiễu kết luận về <b>tổng số lượng tuyệt đối</b> mà không biết cỡ mẫu!</td><td>Kiểm tra kỹ đơn vị trục Y / tiêu đề cột: <code>%</code> ≠ <code>total number</code>!</td></tr>
        <tr><td><b>3. Legend / Axis Swap</b></td><td>Nhìn lướt nhầm đường nét đứt với đường nét liền, hoặc đọc nhầm cột 2010 thành cột 2020.</td><td>Dùng chuột/mắt dóng thẳng từ Legend vào đúng thanh/đường trước khi đọc giá trị.</td></tr>
        <tr><td><b>4. Unstated Cause (Suy diễn nguyên nhân ngoài bảng)</b></td><td>Bảng chỉ cho thấy A tăng cùng lúc B giảm, nhưng đáp án nhiễu thêm lý do nguyên nhân <i>"because of government subsidies"</i> không hề có trong bảng hay văn bản!</td><td>Bảng chỉ chứng minh <b>SỐ LIỆU &amp; TƯƠNG QUAN</b>, không tự sinh ra nguyên nhân ngoài bài!</td></tr>
      </tbody>
    </table>
  </div>

  <div id="sec-complete-sentence" class="lecture-interactive-card sat-card" data-lecture-section="sec_complete_sentence">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>3. Tiểu dạng "Hoàn thiện câu bằng số liệu" (Complete the Example / Statement)</h2>
    <div class="sat-rule-box">
      <b>📊 Lưu ý riêng khi chỗ trống nằm cuối đoạn văn:</b><br/>
      Câu hỏi dạng: <i>"Which choice most effectively uses data from the table to complete the example / statement?"</i><br/>
      → Hãy đọc cực kỹ <b>từ nối ngay trước chỗ trống</b>! Nếu trước chỗ trống là <b>"whereas / however / by contrast"</b>, bạn phải tìm cặp số liệu <b>ĐỐI LẬP</b> trong bảng; nếu là <b>"for example / similarly"</b>, bạn phải tìm ví dụ <b>KHỚP ĐÚNG QUY LUẬT</b> vừa phát biểu ở câu trước!
    </div>
  </div>
''',
        quick_check_html=make_quick_check_html(
            qc_id="qc_5_4",
            passage_html='''<table style="width:100%;border-collapse:collapse;font-family:sans-serif;font-size:13px;margin-bottom:10px;">
              <thead><tr style="background:#0f172a;color:#fff;"><th style="padding:6px 8px;border:1px solid #cbd5e1;">Battery Prototype</th><th style="padding:6px 8px;border:1px solid #cbd5e1;">Energy Density (Wh/kg)</th><th style="padding:6px 8px;border:1px solid #cbd5e1;">Capacity Retained After 1,000 Cycles</th></tr></thead>
              <tbody>
                <tr><td style="padding:6px 8px;border:1px solid #cbd5e1;">Alloy-X</td><td style="padding:6px 8px;border:1px solid #cbd5e1;">310</td><td style="padding:6px 8px;border:1px solid #cbd5e1;">74%</td></tr>
                <tr><td style="padding:6px 8px;border:1px solid #cbd5e1;">Alloy-Y</td><td style="padding:6px 8px;border:1px solid #cbd5e1;">285</td><td style="padding:6px 8px;border:1px solid #cbd5e1;">93%</td></tr>
                <tr><td style="padding:6px 8px;border:1px solid #cbd5e1;">Alloy-Z</td><td style="padding:6px 8px;border:1px solid #cbd5e1;">240</td><td style="padding:6px 8px;border:1px solid #cbd5e1;">89%</td></tr>
              </tbody>
            </table>
            A materials engineer claims that engineers face an unavoidable trade-off in which any battery prototype exceeding 250 Wh/kg cannot retain more than 80% of its capacity after 1,000 charge cycles.''',
            question_prompt="Which choice best describes data from the table that directly weaken the engineer’s claim?",
            options=[
                "Alloy-X achieves the highest energy density in the table at 310 Wh/kg while retaining 74% of its capacity.",
                "Alloy-Z retains 89% of its capacity after 1,000 cycles, which is higher than the 74% retained by Alloy-X.",
                "Alloy-Y achieves an energy density of 285 Wh/kg—well above 250 Wh/kg—yet still retains 93% of its capacity after 1,000 cycles.",
                "Alloy-Z has the lowest energy density among the three tested prototypes at 240 Wh/kg."
            ],
            correct_idx=2,
            explanation_vi="Chốt Claim cần bác bỏ: BẤT KỲ pin nào > 250 Wh/kg đều KHÔNG THỂ giữ > 80% dung lượng. Kiểm tra bảng: Alloy-Y đạt 285 Wh/kg (>250) NHƯNG giữ tới 93% (>80%) → phản ví dụ đập tan tuyên bố! Cả A, B, D đều 100% ĐÚNG SỐ LIỆU nhưng là bẫy 'True Data, Wrong Claim' (Alloy-X ủng hộ Claim chứ không bác bỏ; Alloy-Z ở mức 240 < 250 nên nằm ngoài ngưỡng của Claim!)."
        )
    )
    seg_5_4 = [
        {
            "id": "intro",
            "title": "Giới thiệu Bài 5.4: Biểu đồ & Bảng số liệu Quantitative Evidence",
            "selector": "#sec-header",
            "en": "Welcome to Lesson 5.4: Quantitative Command of Evidence. On the Digital SAT, graph and table questions rarely test difficult math—they test whether you can separate accurate data that proves the exact claim from accurate data that misses the point.",
            "vi": "Chào mừng các bạn đến với Bài 5.4: Bằng chứng định lượng trên Biểu đồ và Bảng số liệu. Trên Digital SAT, câu biểu đồ hiếm khi đòi hỏi tính toán khó—thử thách thực sự là tách bạch dữ liệu đúng chứng minh chuẩn luận điểm khỏi dữ liệu tuy đúng bảng nhưng lệch mục tiêu."
        },
        {
            "id": "sec_three_step_quant",
            "title": "1. Quy trình 3 bước đọc biểu đồ dưới 60 giây",
            "selector": "#sec-three-step-quant",
            "en": "Section 1 lays out the three-step Quantitative SOP. First, read the text and lock onto the exact claim before staring at the chart. Second, slash any option that misreads a number, unit, or trend. Third, among the remaining factually true options, pick the one that directly proves or refutes the claim's exact threshold or comparison.",
            "vi": "Mục 1 trình bày quy trình ba bước tốc độ cao. Bước một: đọc đoạn văn và khóa chặt luận điểm trước khi soi số liệu. Bước hai: gạch ngay mọi phương án đọc sai số, sai đơn vị hoặc ngược xu hướng. Bước ba: trong các phương án cùng đúng số liệu, chọn đúng phương án giải quyết trọn vẹn điều kiện của luận điểm."
        },
        {
            "id": "sec_quant_traps",
            "title": "2. Bốn bẫy sát thủ trên biểu đồ",
            "selector": "#sec-quant-traps",
            "en": "Section 2 dissects the four recurring chart traps: True Data Wrong Claim, confusing percentages with raw totals, swapping legend lines or columns, and inventing outside causal explanations that never appear in the graphic.",
            "vi": "Mục 2 chỉ rõ bốn bẫy kinh điển: đúng số liệu nhưng sai luận điểm, nhầm phần trăm với tổng số lượng tuyệt đối, nhìn lệch chú giải hay cột bảng, và tự suy diễn nguyên nhân không hề xuất hiện trên biểu đồ."
        },
        {
            "id": "sec_complete_sentence",
            "title": "3. Mẹo câu hoàn thiện ví dụ cuối đoạn",
            "selector": "#sec-complete-sentence",
            "en": "Section 3 addresses fill-in-the-blank quantitative items. Check the transition right before the blank: whereas or however demands a contrasting data pair, while for example demands numbers confirming the exact pattern just stated.",
            "vi": "Mục 3 lưu ý riêng cho dạng điền số liệu cuối câu: luôn kiểm tra từ nối ngay trước chỗ trống như whereas hay for example để chọn đúng cặp số liệu tương phản hoặc tương đồng."
        }
    ]
    lectures.append({
        "code": "5_4",
        "module_key": "rw_m5",
        "order_index": 4,
        "title": "5.4 Command of Evidence — Quantitative: Charts, Tables & The 'True Data, Wrong Claim' Trap",
        "drill_key": "drill_5_4",
        "drill_title": "Drill 5.4: Command of Evidence — Quantitative Charts & Tables (13 Qs)",
        "html": html_5_4,
        "segments": seg_5_4,
        "major_sections": {f"{s['id']}": {"start": i, "end": i} for i, s in enumerate(seg_5_4)},
    })

    # =========================================================================
    # LECTURE 5.5: Inferences — Tight Deductive Completion (1-Millimeter Rule)
    # =========================================================================
    html_5_5 = build_sat_lecture_html(
        badge_text="Digital SAT 1500+ • R&W Module 5 • Information and Ideas (Hard M2)",
        title="5.5 Inferences: Tight Deductive Completion & The 1-Millimeter Rule",
        subtitle="Chinh phục câu hỏi khó nhất toàn đề Digital SAT ('Which choice most logically completes the text?'): ghép chuỗi tiền đề A + B → Kết luận tất yếu C.",
        intro_points=[
            "Hiểu bản chất SAT Inference: KHÔNG PHẢI suy đoán bay bổng như trong môn Văn — mà là phép CỘNG LOGIC TẤT YẾU (Premise A + Premise B = Conclusion C).",
            "Áp dụng Quy tắc 1 Milimét (The 1-Millimeter Rule): đáp án đúng chỉ bước đúng 1 milimét từ dữ kiện bài cho, tuyệt đối không phóng đại hay thêm biến mới.",
            "Làm chủ 4 khuôn lập luận hay ra nhất Hard Module 2: Elimination of Alternative, Conditional Bridge, Unexpected Contrast Resolution và Scope Limitation.",
        ],
        cards_html='''
  <div id="sec-one-mm" class="lecture-interactive-card sat-card" data-lecture-section="sec_one_mm">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>1. Bản Chất Của SAT Inference: "Quy Tắc 1 Milimét" (The 1-Millimeter Rule)</h2>
    <p>Câu hỏi <i>"Which choice most logically completes the text?"</i> thường đứng ở vị trí <b>Câu 13–15 của Hard Module 2</b> và là nguyên nhân số 1 khiến thí sinh tụt từ 780 xuống 720. Sai lầm lớn nhất là tưởng "Inference" nghĩa là phải "suy diễn thật sâu xa sáng tạo"!</p>
    <div class="sat-gold-box">
      <b>📐 Định luật Thép 780–800 (The 1-Millimeter Rule):</b><br/>
      Trên Digital SAT, đáp án Inference đúng <b>KHÔNG BAO GIỜ nhảy cóc 10 mét</b> — nó chỉ nối 2 tiền đề đã cho sẵn thành một <b>kết luận gần như hiển nhiên (cách văn bản đúng 1 milimét!)</b>:<br/>
      <code>[Tiền đề A: Loài chim X chỉ làm tổ được trên cây già &gt;100 tuổi]</code><br/>
      <code>+ [Tiền đề B: Toàn bộ rừng khu vực Y vừa bị khai thác sạch cây &gt;60 tuổi]</code><br/>
      <code>⇒ [Kết luận 1mm (ĐÚNG): Loài chim X nhiều khả năng không thể làm tổ tại khu vực Y trong tương lai gần.]</code><br/>
      <code>✗ [Nhảy cóc 10m (BẪY!): Loài chim X sẽ tuyệt chủng trên toàn cầu vào năm 2030.]</code>
    </div>
  </div>

  <div id="sec-four-engines" class="lecture-interactive-card sat-card" data-lecture-section="sec_four_engines">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>2. Bốn Khuôn Lập Luận (Logical Engines) Hay Thi Nhất Hard Module 2</h2>
    <table class="sat-table">
      <thead>
        <tr><th>Khuôn lập luận</th><th>Cấu trúc tiền đề trong đoạn văn</th><th>Đầu ra kết luận chuẩn</th></tr>
      </thead>
      <tbody>
        <tr><td><b>1. Either/Or Elimination</b><br/><i>(Loại trừ phương án A → chốt B)</i></td><td>Hiện tượng Y chỉ có thể do X1 hoặc X2. Thí nghiệm mới cho thấy X1 không xảy ra ở vùng đó. Therefore, ...</td><td>...nhiều khả năng X2 (hoặc một cơ chế khác ngoài X1) đứng sau hiện tượng Y.</td></tr>
        <tr><td><b>2. Methodological Caveat</b><br/><i>(Hạn chế mẫu/phương pháp → giới hạn kết luận)</i></td><td>Nghiên cứu khẳng định quy luật X trên 1.000 người, nhưng sau đó phát hiện mẫu chỉ gồm sinh viên 18–22 tuổi. Thus, ...</td><td>...kết quả có thể không khái quát hóa được cho các nhóm tuổi lớn hơn.</td></tr>
        <tr><td><b>3. Mismatched Scale / Exception</b><br/><i>(Ngoại lệ phá vỡ quy luật chung)</i></td><td>Giả định rằng tất cả loài X cần điều kiện A; nhưng phát hiện loài X1 phát triển mạnh nơi thiếu A. This suggests that...</td><td>...điều kiện A không hoàn toàn thiết yếu cho mọi loài thuộc nhóm X.</td></tr>
        <tr><td><b>4. Trade-Off / Double Effect</b><br/><i>(Hiệu ứng kép triệt tiêu nhau)</i></td><td>Chính sách giảm giá điện làm tăng mua xe điện (+), nhưng cũng khiến người dân chạy điều hòa nhiều hơn (−). Consequently, ...</td><td>...mức giảm phát thải ròng có thể nhỏ hơn dự tính ban đầu nếu chỉ xét riêng xe điện.</td></tr>
      </tbody>
    </table>
  </div>

  <div id="sec-bridge-words" class="lecture-interactive-card sat-card" data-lecture-section="sec_bridge_words">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>3. Đọc Cực Kỹ Từ Chốt Ngay Trước Chỗ Trống!</h2>
    <div class="sat-trap-box">
      <b>⚠️ Mấu chốt quyết định ở 5 từ cuối cùng trước dấu gạch ngang `______`:</b><br/>
      • Nếu trước chỗ trống là <b>"researchers caution that ______"</b> hoặc <b>"this limitation suggests that ______"</b> → kết luận phải mang tính <b>thận trọng / giới hạn phạm vi</b>.<br/>
      • Nếu trước chỗ trống là <b>"it is unlikely that ______"</b> hoặc <b>"historians doubt that ______"</b> → CẨN THẬN PHỦ ĐỊNH KÉP! Tìm mệnh đề MÀ CÁC NHÀ SỬ HỌC NGHI NGỜ (tức điều BỊ BÁC BỎ bởi bằng chứng trước đó)!<br/>
      • Ưu tiên ngôn ngữ khiêm tốn chuẩn khoa học (<i>may not apply to, likely played a smaller role than assumed, does not necessarily indicate</i>) và nghi ngờ ngay mọi từ cực đoan (<i>never, solely, completely impossible</i>)!
    </div>
  </div>
''',
        quick_check_html=make_quick_check_html(
            qc_id="qc_5_5",
            passage_html="Archaeologists analyzing bronze arrowheads from a fourth-century BCE fortress in northern Greece initially assumed that every weapon bearing the king’s monogram had been cast inside the royal capital’s central foundry. Recent lead-isotope testing, however, revealed that while the monograms are stylistically identical, the copper ore in nearly half the arrowheads originated from three distant provincial mines located hundreds of kilometers away—mines whose smelters routinely cast finished bronze goods locally rather than shipping raw ingots. Consequently, the researchers concluded that ______",
            question_prompt="Which choice most logically completes the text?",
            options=[
                "provincial workshops were unable to replicate the artistic quality of the royal capital’s monogram stamps.",
                "the fortress’s weapons were likely produced across multiple regional foundries following a standardized royal stamp design, rather than exclusively in the capital.",
                "the king’s central foundry ceased operating entirely during the fourth century BCE due to copper shortages.",
                "ancient Greek soldiers preferred provincial bronze arrowheads over weapons forged in the royal capital."
            ],
            correct_idx=1,
            explanation_vi="Ghép 2 tiền đề (1-Millimeter Rule): (A) Dấu ấn hoàng gia giống hệt nhau trên mũi tên + (B) Quặng đồng của gần một nửa số mũi tên đến từ 3 mỏ địa phương xa hàng trăm km mà các lò ở đó vốn đúc thành phẩm tại chỗ thay vì xuất phôi đồng thô ⇒ Kết luận tất yếu: Vũ khí có khả năng được sản xuất ở nhiều xưởng địa phương theo cùng mẫu dấu chuẩn của hoàng gia chứ không chỉ đúc độc quyền tại kinh đô (B)! A mâu thuẫn ('stylistically identical'); C quá cực đoan ('ceased operating entirely'); D suy diễn tâm lý binh lính (Out of Scope)."
        )
    )
    seg_5_5 = [
        {
            "id": "intro",
            "title": "Giới thiệu Bài 5.5: Inferences — Quy tắc 1 Milimét",
            "selector": "#sec-header",
            "en": "Welcome to Lesson 5.5, the final lecture of the Reading and Writing mastery path: Inferences. These logical-completion items are the hardest questions on the entire exam—yet they obey strict mathematical deduction once you apply the One-Millimeter Rule.",
            "vi": "Chào mừng các bạn đến với Bài 5.5, bài giảng chốt hạ lộ trình Reading and Writing 1500+: Suy luận logic Inferences. Đây là dạng câu khó nhất toàn đề thi, nhưng lại tuân theo phép suy diễn chặt chẽ như toán học một khi bạn áp dụng Quy tắc 1 Milimét."
        },
        {
            "id": "sec_one_mm",
            "title": "1. Quy tắc 1 Milimét (The 1-Millimeter Rule)",
            "selector": "#sec-one-mm",
            "en": "Section 1 defines the One-Millimeter Rule. On the Digital SAT, an inference is never a wild creative leap; it is the inevitable sum of Premise A plus Premise B sitting just one millimeter beyond the written text. Any answer that extrapolates into unmentioned future dates or global claims is automatically a trap.",
            "vi": "Mục 1 xác lập Quy tắc 1 Milimét. Trên Digital SAT, suy luận không bao giờ là sự bay bổng sáng tạo; nó là tổng tất yếu của Tiền đề A cộng Tiền đề B, chỉ bước thêm đúng một milimét từ dữ kiện có sẵn. Mọi đáp án nhảy cóc ra ngoài phạm vi thời gian hay không gian của bài đều là bẫy."
        },
        {
            "id": "sec_four_engines",
            "title": "2. Bốn khuôn lập luận hay thi nhất Hard Module 2",
            "selector": "#sec-four-engines",
            "en": "Section 2 maps the four deductive engines that power Hard Module 2 inferences: eliminating one of two possible causes, exposing a methodological sample limit that restricts generalization, using a counterexample to soften an absolute assumption, and spotting competing trade-off effects that partially cancel each other out.",
            "vi": "Mục 2 hệ thống hóa bốn khuôn suy diễn chủ đạo ở Hard Module 2: loại trừ một trong hai nguyên nhân, chỉ ra giới hạn mẫu thử ngăn không cho khái quát hóa rộng, dùng phản ví dụ để thu hẹp giả định tuyệt đối, và nhận diện hai hiệu ứng trái chiều phần nào triệt tiêu nhau."
        },
        {
            "id": "sec_bridge_words",
            "title": "3. Cảnh giác 5 từ chốt ngay trước chỗ trống",
            "selector": "#sec-bridge-words",
            "en": "Finally, inspect the last five words immediately before the blank. Phrases like researchers doubt that or it is unlikely that flip polarity, requiring you to choose the idea the evidence disproves rather than supports. Favor calibrated scientific wording like likely or does not necessarily indicate over extreme absolutes.",
            "vi": "Cuối cùng, luôn soi kỹ năm từ ngay trước chỗ trống. Các cụm như researchers doubt that hay it is unlikely that sẽ đảo ngược chiều logic, đòi hỏi bạn chọn nhận định bị bác bỏ chứ không phải nhận định được ủng hộ. Luôn ưu tiên ngôn ngữ học thuật chừng mực thay vì các từ cực đoan tuyệt đối."
        }
    ]
    lectures.append({
        "code": "5_5",
        "module_key": "rw_m5",
        "order_index": 5,
        "title": "5.5 Inferences: Tight Deductive Completion & The 1-Millimeter Rule",
        "drill_key": "drill_5_5",
        "drill_title": "Drill 5.5: Inferences — Hard Module 2 Deductive Completion (13 Qs)",
        "html": html_5_5,
        "segments": seg_5_5,
        "major_sections": {f"{s['id']}": {"start": i, "end": i} for i, s in enumerate(seg_5_5)},
    })

    return lectures
