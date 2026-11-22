from sat_audio_pipeline import build_sat_lecture_html, make_quick_check_html

def get_stage2_lectures():
    lectures = []

    # =========================================================================
    # LECTURE 1.1: Digital SAT 1500+ Blueprint, Adaptive Routing & Pacing
    # =========================================================================
    html_1_1 = build_sat_lecture_html(
        badge_text="Digital SAT 1500+ • R&W Module 1 • Strategy & Architecture",
        title="1.1 Digital SAT 1500+ Blueprint, Adaptive Routing & Triage Pacing",
        subtitle="Hiểu bản chất thuật toán Adaptive, chiến lược phân bổ 32 phút đạt 750–800 R&W và 5 mẫu bẫy kinh điển của College Board.",
        intro_points=[
            "Nắm trọn cấu trúc 2 Module × 27 câu (32 phút/module) và ngưỡng định tuyến vào Hard Module 2 (≥18–20/27).",
            "Áp dụng chiến thuật Triage Order (làm Grammar/Writing trước) để tiết kiệm 10–12 phút cho Reading Hard.",
            "Nhận diện ngay 5 mẫu bẫy phân hóa 700 → 800 của College Board trước khi đọc đáp án.",
        ],
        cards_html='''
  <div id="sec-blueprint" class="lecture-interactive-card sat-card" data-lecture-section="sec_blueprint">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>1. Cấu trúc Digital SAT R&amp;W &amp; Cơ chế Adaptive Routing</h2>
    <p>Khác hoàn toàn với SAT giấy cũ (5 bài đọc dài 750 từ), <b>Digital SAT Reading &amp; Writing</b> gồm <b>54 câu hỏi độc lập</b>, mỗi câu đi kèm một đoạn văn ngắn (25–150 từ), chia làm 2 Module kéo dài 32 phút mỗi Module.</p>
    <table class="sat-table">
      <thead>
        <tr>
          <th>Content Domain (4 Miền kiến thức)</th>
          <th>Tỉ trọng</th>
          <th>Số câu / Đề</th>
          <th>Thứ tự xuất hiện trong Module</th>
        </tr>
      </thead>
      <tbody>
        <tr><td><b>1. Craft and Structure</b> (Words in Context, Structure/Purpose, Cross-Text)</td><td>~28%</td><td>13–15 câu</td><td>Câu 1 → Câu 7–9</td></tr>
        <tr><td><b>2. Information and Ideas</b> (Central Ideas, Evidence, Inferences)</td><td>~26%</td><td>12–14 câu</td><td>Câu 8–10 → Câu 15–16 <i>(Khó nhất)</i></td></tr>
        <tr><td><b>3. Standard English Conventions</b> (Boundaries, Form/Structure/Sense)</td><td>~26%</td><td>11–15 câu</td><td>Câu 16–17 → Câu 21–23</td></tr>
        <tr><td><b>4. Expression of Ideas</b> (Transitions, Rhetorical Synthesis)</td><td>~20%</td><td>8–12 câu</td><td>Câu 22–24 → Câu 27</td></tr>
      </tbody>
    </table>
    <div class="sat-rule-box">
      <b>⚡ Cơ chế Adaptive (Multistage Adaptive Testing):</b><br/>
      • <b>Module 1</b> là đề hỗn hợp (Easy + Medium + Hard). Muốn đạt <b>1500+ (730–800 R&amp;W)</b>, bạn <b>BẮT BUỘC</b> phải được phân nhánh vào <b>Module 2 Hard</b> (cần đúng khoảng ≥18/27, an toàn nhất là ≥22/27 ở Module 1).<br/>
      • Nếu rơi xuống <b>Module 2 Lower</b>, điểm trần của bạn bị khóa cứng quanh mức <b>580–600/800</b> dù bạn làm đúng 100% Module 2!
    </div>
  </div>

  <div id="sec-triage" class="lecture-interactive-card sat-card" data-lecture-section="sec_triage">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>2. Chiến lược Triage Order: Bí quyết không bao giờ thiếu giờ ở Hard Module 2</h2>
    <p>Thời gian trung bình là <b>71 giây/câu</b>, nhưng độ khó KHÔNG phân bổ đều! Sai lầm lớn nhất của học viên IELTS 7.5–8.0 là làm tuần tự từ câu 1 → câu 27, bị kẹt 12 phút ở cụm câu Reading khó (#10–#16) rồi phải đoán bừa 5 câu Grammar/Synthesis cực dễ ăn điểm ở cuối bài.</p>
    <div class="sat-gold-box">
      <b>🏆 Quy trình Triage 3 Chặng chuẩn 780–800 R&amp;W:</b><br/>
      <b>• Chặng 1 (Phút 0 → 7): Nhảy thẳng tới Câu 16–17 → Câu 27</b> (Standard English Conventions + Transitions + Rhetorical Synthesis). Quét sạch 12–13 câu này với mục tiêu <b>100% chính xác trong 7–8 phút</b> (~30–35 giây/câu).<br/>
      <b>• Chặng 2 (Phút 8 → 14): Quay lại Câu 1 → Câu 7</b> (Words in Context + Text Structure/Purpose). Xử lý dứt điểm 6–7 câu trong ~6 phút.<br/>
      <b>• Chặng 3 (Phút 14 → 30): Dồn toàn bộ 16 phút còn lại cho "Vùng Tử Thần" Câu 8 → Câu 16</b> (Cross-Text, Command of Evidence, Quantitative Charts, Inferences). Bạn có gần <b>2 phút/câu</b> cho những câu khó nhất đề!<br/>
      <b>• Chặng 4 (Phút 30 → 32):</b> Kiểm tra các câu đã <i>Mark for Review</i> và chắc chắn không bỏ trống câu nào (SAT không trừ điểm sai).
    </div>
  </div>

  <div id="sec-traps" class="lecture-interactive-card sat-card" data-lecture-section="sec_traps">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>3. Giải phẫu 5 Mẫu Bẫy Kinh Điển của College Board (Vùng 700 → 800)</h2>
    <p>Trên Digital SAT, đáp án đúng KHÔNG chỉ "nghe có vẻ hợp lý" — nó phải được <b>chứng minh 100% trực tiếp từ văn bản</b>. Mọi đáp án nhiễu ở Hard Module 2 đều rơi vào 5 khuôn bẫy cố định:</p>
    <table class="sat-table">
      <thead>
        <tr><th>Tên bẫy (Trap Archetype)</th><th>Dấu hiệu nhận diện nhanh</th><th>Cách tiêu diệt</th></tr>
      </thead>
      <tbody>
        <tr><td><b>1. Out of Scope / Extrapolation</b></td><td>Đưa khái niệm, nguyên nhân hoặc hệ quả có vẻ đúng ngoài đời thực nhưng đoạn văn <i>không hề nhắc tới</i>.</td><td>Hỏi ngược: "Dòng nào trong bài nói chi tiết này?" Không có → Gạch ngay.</td></tr>
        <tr><td><b>2. Too Extreme / Absolute</b></td><td>Chứa từ cực đoan: <i>solely, exclusively, entirely, never, all, proves conclusively, the primary cause</i>.</td><td>So sánh cường độ ngôn ngữ: bài nói <i>may suggest / partially</i> mà đáp án nói <i>proves</i> → Loại.</td></tr>
        <tr><td><b>3. Half-Right, Half-Wrong</b></td><td>70% đầu khớp hoàn hảo với đoạn văn để đánh lừa mắt đọc lướt, nhưng 3–4 từ cuối gài sai sự thật.</td><td>Đọc kỹ tới <b>chữ cuối cùng</b> của từng phương án trước khi chọn.</td></tr>
        <tr><td><b>4. Reversed Logic / Role Swap</b></td><td>Đảo ngược quan hệ nhân quả (A gây ra B thành B gây ra A) hoặc đánh tráo quan điểm của Tác giả 1 với Tác giả 2.</td><td>Vẽ mũi tên nháp ngắn: <code>X → Y</code> hoặc <code>T1: ủng hộ / T2: phản bác</code>.</td></tr>
        <tr><td><b>5. True Data, Wrong Claim</b></td><td>Đặc sản câu Biểu đồ/Bảng &amp; Synthesis: số liệu hoàn toàn đúng với bảng nhưng <i>không trả lời mục tiêu đề bài</i>.</td><td>Chốt <b>Claim/Goal</b> trước khi nhìn số liệu.</td></tr>
      </tbody>
    </table>
  </div>

  <div id="sec-mindset" class="lecture-interactive-card sat-card" data-lecture-section="sec_mindset">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>4. Quy tắc Loại trừ Chủ động (Active Elimination) trên Bluebook</h2>
    <p>Người đạt 650 tìm 1 đáp án "có vẻ đúng". Người đạt <b>780–800</b> tìm ra <b>lý do chính xác để gạch bỏ 3 đáp án sai</b> bằng công cụ <span class="sat-code">ABC Option Eliminator</span> ngay trên Bluebook.</p>
    <div class="sat-trap-box">
      <b>⚠️ Bẫy tâm lý lớn nhất của học viên giỏi Tiếng Anh:</b> Đọc câu hỏi xong rồi dùng <i>kiến thức nền (background knowledge)</i> để suy diễn thêm. Trên SAT, <b>văn bản là vũ trụ duy nhất</b>. Nếu chỉ cần 1 từ trong đáp án sai với văn bản → toàn bộ đáp án đó sai 100%!
    </div>
  </div>
''',
        quick_check_html=make_quick_check_html(
            qc_id="qc_1_1",
            passage_html="A 2024 marine biology study observed that juvenile coral larvae settled at significantly higher rates on reef tiles where recorded sounds of healthy reefs were played underwater than on silent control tiles. Lead researcher Dr. Elena Vance noted that while acoustic playback alone cannot reverse ocean warming, it could serve as a supplementary tool in localized reef restoration projects.",
            question_prompt="Which choice best states a claim supported by the text without falling into a College Board trap?",
            options=[
                "Playing healthy reef recordings is the primary and most effective solution to reversing global ocean warming.",
                "Acoustic playback of healthy reef sounds may assist localized coral restoration efforts by encouraging larval settlement.",
                "Juvenile coral larvae are completely unable to survive on reefs that lack underwater audio playback equipment.",
                "Dr. Elena Vance proved that adult corals migrate faster toward louder coastal shipping lanes."
            ],
            correct_idx=1,
            explanation_vi="Đáp án B phản ánh chính xác mức độ thận trọng của văn bản (may assist / supplementary tool + encouraging larval settlement). A dính bẫy Too Extreme + Contradiction (bài nói cannot reverse warming); C dính bẫy Too Extreme (completely unable); D dính bẫy Out of Scope (shipping lanes)."
        )
    )
    seg_1_1 = [
        {
            "id": "intro",
            "title": "Giới thiệu Bài 1.1: Kiến trúc Digital SAT 1500+",
            "selector": "#sec-header",
            "en": "Welcome to Digital SAT 1500 Plus, Lesson 1.1: Blueprint, Adaptive Routing, and Triage Pacing. To break 750 in Reading and Writing, strong English alone is not enough. You must master the adaptive test architecture, optimize your thirty-two-minute pacing strategy, and systematically dismantle the five classic College Board trap archetypes.",
            "vi": "Chào mừng các bạn đến với khóa Digital SAT 1500+, Bài 1.1: Kiến trúc Đề thi, Cơ chế Phân nhánh Adaptive và Chiến thuật Triage. Để bứt phá mốc 750–800 phần Ngôn ngữ, giỏi tiếng Anh thôi là chưa đủ: bạn phải làm chủ luật chơi thích ứng, phân bổ 32 phút thông minh và nhìn thấu 5 khuôn bẫy kinh điển của College Board."
        },
        {
            "id": "sec_blueprint",
            "title": "1. Cấu trúc 4 Domains & Adaptive Routing",
            "selector": "#sec-blueprint",
            "en": "Section 1 maps the Reading and Writing blueprint. Every module contains twenty-seven discrete questions spanning four content domains in a predictable sequence: Craft and Structure first, followed by Information and Ideas, then Standard English Conventions, and finally Expression of Ideas. Your Module 1 accuracy determines whether you route into Hard Module 2—essential for any score above six hundred—or Lower Module 2, which caps your maximum score.",
            "vi": "Mục 1 giải mã cấu trúc 4 miền kiến thức. Mỗi module gồm 27 câu hỏi sắp xếp theo đúng thứ tự cố định: mở đầu là Craft and Structure, tiếp theo là vùng khó nhất Information and Ideas, rồi đến Ngữ pháp Standard English Conventions và chốt lại bằng Expression of Ideas. Thành tích ở Module 1 quyết định bạn có vào được Hard Module 2 để tranh điểm 700–800 hay bị khóa trần ở mức 600."
        },
        {
            "id": "sec_triage",
            "title": "2. Chiến thuật Triage Order (Không bao giờ thiếu giờ)",
            "selector": "#sec-triage",
            "en": "Section 2 introduces the elite Triage Order. Instead of marching linearly from question one to twenty-seven and stalling on dense reading items in the middle, jump immediately to question sixteen or seventeen and sweep all Grammar, Transitions, and Rhetorical Synthesis items in seven to eight minutes with zero errors. Then clear Words in Context, banking up to sixteen uninterrupted minutes for the toughest Hard Module 2 reading gauntlet.",
            "vi": "Mục 2 trình bày chiến thuật Triage chuẩn 780–800. Thay vì làm tuần tự rồi kẹt giờ ở giữa bài, hãy nhảy thẳng tới câu 16–17 để quét sạch nhóm Ngữ pháp, Từ nối và Tổng hợp ghi chú trong 7–8 phút với độ chính xác 100%. Sau đó quay lại xử lý từ vựng đầu bài, để dành trọn 15–16 phút đầu óc tỉnh táo nhất cho cụm câu Đọc hiểu phân hóa khó nhất."
        },
        {
            "id": "sec_traps",
            "title": "3. Giải phẫu 5 Mẫu Bẫy Kinh Điển",
            "selector": "#sec-traps",
            "en": "Section 3 dissects the five recurring College Board traps: Out of Scope extrapolations, Too Extreme absolute modifiers like solely or never, Half-Right Half-Wrong lures that hide an error in the final three words, Reversed Logic that swaps cause and effect, and True Data Wrong Claim distractors in chart questions. Recognizing these blueprints turns reading into an exact science.",
            "vi": "Mục 3 giải phẫu 5 mẫu bẫy kinh điển: Suy diễn ngoài văn bản, Ngôn từ cực đoan, Bẫy nửa đúng nửa sai giấu lỗi ở 3 từ cuối, Đảo ngược nhân quả hoặc tráo vai tác giả, và Bẫy đúng số liệu nhưng sai luận điểm. Nhận diện được 5 khuôn bẫy này giúp bạn biến Đọc hiểu thành một môn khoa học chính xác."
        },
        {
            "id": "sec_mindset",
            "title": "4. Tư duy Loại trừ Chủ động (Active Elimination)",
            "selector": "#sec-mindset",
            "en": "Finally, adopt active elimination. High scorers do not search for an option that sounds nice; they prove why three choices are objectively wrong using the Bluebook Option Eliminator. Remember: on the Digital SAT, the passage is the entire universe, and a single unsupported word disqualifies an entire answer choice.",
            "vi": "Cuối cùng, hãy rèn thói quen loại trừ chủ động. Thí sinh 780+ không tìm đáp án nghe có vẻ hay mà chứng minh lý do gạch bỏ 3 đáp án sai bằng nút gạch ngang trên Bluebook. Hãy nhớ: trên SAT, đoạn văn là vũ trụ duy nhất, chỉ cần một từ không có bằng chứng là đủ loại cả phương án đó."
        }
    ]
    lectures.append({
        "code": "1_1",
        "module_key": "rw_m1",
        "order_index": 1,
        "title": "1.1 Digital SAT 1500+ Blueprint, Adaptive Routing & Pacing",
        "drill_key": "drill_1_1",
        "drill_title": "Drill 1.1: Digital SAT 1500+ Diagnostic & Trap Identification (12 Qs)",
        "html": html_1_1,
        "segments": seg_1_1,
        "major_sections": {f"{s['id']}": {"start": i, "end": i} for i, s in enumerate(seg_1_1)},
    })

    # =========================================================================
    # LECTURE 2.1: Boundaries I — Clauses, Linking & Core Punctuation
    # =========================================================================
    html_2_1 = build_sat_lecture_html(
        badge_text="Digital SAT 1500+ • R&W Module 2 • Standard English Conventions",
        title="2.1 Boundaries I: Clauses, Linking & Core Punctuation",
        subtitle="Làm chủ hoàn toàn Period (.), Semicolon (;), Colon (:), Em-Dash (—) và FANBOYS — đạt tốc độ ≤20 giây/câu, 0 lỗi sai.",
        intro_points=[
            "Phân biệt tức thì Independent Clause (IC) vs. Dependent Clause (DC) vs. Phrase (Cụm từ không có động từ chính).",
            "Nắm bảng 5 công thức nối 2 IC hợp lệ và nhận diện ngay bẫy Comma Splice / Fused Sentence.",
            "Ứng dụng quy tắc tương đương dấu câu (Period = Semicolon = Comma + FANBOYS) để loại nhanh 2–3 đáp án trong 5 giây.",
        ],
        cards_html='''
  <div id="sec-ic-dc" class="lecture-interactive-card sat-card" data-lecture-section="sec_ic_dc">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>1. Nền tảng sống còn: Independent Clause (IC) vs. Dependent Clause (DC)</h2>
    <p>Mọi câu hỏi <b>Boundaries</b> trên Digital SAT đều quy về đúng một thao tác: <b>xác định hai vế trước và sau chỗ trống là IC hay DC/Phrase</b>.</p>
    <table class="sat-table">
      <thead>
        <tr><th>Loại đơn vị</th><th>Cấu tạo bắt buộc</th><th>Ví dụ chuẩn SAT</th></tr>
      </thead>
      <tbody>
        <tr><td><b>Independent Clause (IC)</b><br/><i>Mệnh đề độc lập</i></td><td>Chủ ngữ + Động từ chia thì (Finite Verb) + <b>Ý trọn vẹn, đứng 1 mình được</b>.</td><td><i>The observatory recorded a faint radio burst.</i></td></tr>
        <tr><td><b>Dependent Clause (DC)</b><br/><i>Mệnh đề phụ thuộc</i></td><td>Từ phụ thuộc (<i>although, because, while, since, which, that, if, whereas</i>) + S + V → <b>Không thể đứng 1 mình</b>.</td><td><i>Although the observatory recorded a faint radio burst...</i></td></tr>
        <tr><td><b>Phrase / Fragment</b><br/><i>Cụm từ</i></td><td>Thiếu S hoặc thiếu động từ chia thì (chỉ có <i>V-ing, V-ed, to-V</i> hoặc cụm giới từ).</td><td><i>Recording a faint radio burst from a distant galaxy...</i></td></tr>
      </tbody>
    </table>
    <div class="sat-trap-box">
      <b>⚠️ Bẫy 1500+ hay gặp nhất:</b> Các từ nối trạng từ như <b>however, therefore, moreover, nevertheless, consequently, thus, indeed</b> KHÔNG PHẢI từ phụ thuộc (DC) và cũng KHÔNG PHẢI FANBOYS! Đứng trước chúng để nối 2 IC <b>bắt buộc dùng chấm (.) hoặc chấm phẩy (;)</b> — dùng dấu phẩy (,) là <b>Comma Splice</b> sai lập tức!
    </div>
  </div>

  <div id="sec-five-rules" class="lecture-interactive-card sat-card" data-lecture-section="sec_five_rules">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>2. Năm Công Thức Nối 2 Mệnh Đề Độc Lập (IC + IC)</h2>
    <table class="sat-table">
      <thead>
        <tr><th>Công thức hợp lệ</th><th>Cú pháp</th><th>Điều kiện đặc biệt cần nhớ</th></tr>
      </thead>
      <tbody>
        <tr><td><b>1. Period (.)</b></td><td><span class="sat-code">IC . IC</span></td><td>Tách thành 2 câu hoàn chỉnh độc lập.</td></tr>
        <tr><td><b>2. Semicolon (;)</b></td><td><span class="sat-code">IC ; IC</span></td><td>Tương đương 100% dấu chấm về mặt ngữ pháp khi nối 2 IC. (Ngoài ra <code>;</code> còn dùng phân tách các mục đã chứa dấu phẩy bên trong <i>Super-list</i>).</td></tr>
        <tr><td><b>3. Comma + FANBOYS</b></td><td><span class="sat-code">IC , for/and/nor/but/or/yet/so IC</span></td><td>Phải có đủ cả <b>dấu phẩy</b> lẫn <b>FANBOYS</b> và hai vế đều là IC. Nếu vế sau thiếu chủ ngữ (<code>IC and V</code>) → <b>KHÔNG đặt dấu phẩy</b>!</td></tr>
        <tr><td><b>4. Colon (:)</b></td><td><span class="sat-code">IC : IC / Phrase / List</span></td><td><b>Vế TRƯỚC dấu hai chấm BẮT BUỘC phải là 1 IC hoàn chỉnh!</b> Vế sau giải thích, định nghĩa hoặc liệt kê minh họa cho vế trước.</td></tr>
        <tr><td><b>5. Single Em-Dash (—)</b></td><td><span class="sat-code">IC — IC / Phrase</span></td><td>Hoạt động y hệt dấu hai chấm đơn (nhấn mạnh giải thích ở cuối câu). Vế trước phải là IC.</td></tr>
      </tbody>
    </table>
    <div class="sat-gold-box">
      <b>🚀 Mẹo "Tương Đương Dấu Câu" (Equivalence Shortcut — Giải trong 5 giây):</b><br/>
      Vì <code>IC . IC</code> và <code>IC ; IC</code> hoàn toàn tương đương ngữ pháp, nên nếu trong 4 đáp án có cả <b>A. word. Next</b> và <b>B. word; next</b> (giống hệt từ ngữ, chỉ khác <code>.</code> và <code>;</code>) → <b>CẢ HAI ĐỀU SAI!</b> Gạch ngay A và B trong 2 giây!
    </div>
  </div>

  <div id="sec-colon-trap" class="lecture-interactive-card sat-card" data-lecture-section="sec_colon_trap">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>3. Bẫy Dấu Hai Chấm (:) &amp; Danh sách "Super-Semicolon"</h2>
    <div class="sat-ex-box">
      <b>❌ SAI (Bẫy kinh điển):</b> The expedition required three essential tools: such as a compass, a barometer, and a sextant.<br/>
      <b>❌ SAI (Thiếu IC trước dấu <code>:</code>):</b> The three essential tools were: a compass, a barometer, and a sextant.<br/>
      <b>✅ ĐÚNG (IC hoàn chỉnh trước <code>:</code>):</b> The expedition required three essential tools: a compass, a barometer, and a sextant.
    </div>
    <div class="sat-rule-box">
      <b>📌 Super-Semicolon (Dấu chấm phẩy trong danh sách phức hợp):</b><br/>
      Nếu 1 câu liệt kê 3 mục mà bên trong từng mục đã có dấu phẩy (VD: tên thành phố, quốc gia; hoặc tên tác giả, năm xuất bản), Digital SAT dùng <b>dấu chấm phẩy (;)</b> để ngăn cách các mục lớn:<br/>
      <i>The archive holds letters from Kyoto, Japan; Lisbon, Portugal; and Cusco, Peru.</i><br/>
      → Đây là trường hợp <b>DUY NHẤT</b> dấu chấm phẩy KHÔNG cần 2 vế IC!
    </div>
  </div>

  <div id="sec-sop" class="lecture-interactive-card sat-card" data-lecture-section="sec_sop">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>4. Quy trình 3 Bước giải câu Boundaries trong ≤20 giây</h2>
    <ol style="padding-left:20px; margin:8px 0;">
      <li><b>Bước 1 — Nhìn 4 đáp án trước:</b> Thấy cùng 1–2 từ chỉ thay đổi dấu câu (<code>.</code> <code>;</code> <code>:</code> <code>,</code> <code>—</code>) → Xác nhận ngay dạng <b>Boundaries</b>.</li>
      <li><b>Bước 2 — Đọc trọn câu, chia 2 vế tại chỗ trống:</b> Gán nhãn nhanh <code>[Trái: IC hay DC/Phrase]</code> + <code>[Phải: IC hay DC/Phrase]</code>. Đừng để bị lừa bởi mệnh đề phụ chen giữa!</li>
      <li><b>Bước 3 — Khớp công thức &amp; dùng Equivalence Shortcut:</b> Loại ngay mọi cặp dấu tương đương, loại <i>Comma Splice</i> (<code>IC, IC</code>), loại dấu hai chấm sau động từ/giới từ (<code>such as:</code>, <code>were:</code>, <code>including:</code>).</li>
    </ol>
  </div>
''',
        quick_check_html=make_quick_check_html(
            qc_id="qc_2_1",
            passage_html="In 1928, archaeologist Dorothy Garrod excavated Shuqba Cave in the Judean Hills, uncovering stone blades unlike any previously cataloged in the ______ she named the newly identified prehistoric culture the Natufian, after the nearby Wadi en-Natuf.",
            question_prompt="Which choice completes the text so that it conforms to the conventions of Standard English?",
            options=[
                "region, subsequently,",
                "region; subsequently,",
                "region subsequently",
                "region, and subsequently,"
            ],
            correct_idx=1,
            explanation_vi="Vế trước chỗ trống là 1 IC hoàn chỉnh ('archaeologist Dorothy Garrod excavated...'). Vế sau ('she named the newly identified...') cũng là 1 IC hoàn chỉnh. 'subsequently' là trạng từ liên kết (conjunctive adverb), KHÔNG phải FANBOYS → Bắt buộc dùng dấu chấm phẩy trước 'subsequently,' (B). A là Comma Splice; C là Run-on; D thừa dấu phẩy sau subsequently và làm ngắt mạch sai chuẩn."
        )
    )
    seg_2_1 = [
        {
            "id": "intro",
            "title": "Giới thiệu Bài 2.1: Boundaries I & Dấu câu cốt lõi",
            "selector": "#sec-header",
            "en": "Welcome to Lesson 2.1: Boundaries Part One, covering clauses, linking, and core punctuation. On a 1500-plus path, every Boundaries question is free points—your goal is one hundred percent accuracy in under twenty seconds per item.",
            "vi": "Chào mừng các bạn đến với Bài 2.1: Ranh giới câu Phần 1 về mệnh đề và dấu câu cốt lõi. Với mục tiêu 1500+, mọi câu Boundaries đều là điểm chắc chắn phải lấy tuyệt đối trong dưới 20 giây mỗi câu."
        },
        {
            "id": "sec_ic_dc",
            "title": "1. Phân biệt IC, DC và Phrase",
            "selector": "#sec-ic-dc",
            "en": "Section 1 establishes the core foundation: distinguishing an Independent Clause from a Dependent Clause or a Phrase. An independent clause has a subject, a finite verb, and expresses a complete thought. Watch out for conjunctive adverbs like however, therefore, and moreover—they do not act like conjunctions, so putting only a comma before them between two independent clauses creates an illegal comma splice.",
            "vi": "Mục 1 xác lập nền tảng phân biệt Mệnh đề độc lập IC với Mệnh đề phụ DC và Cụm từ. Mệnh đề độc lập có chủ ngữ, động từ chia thì và đứng một mình trọn nghĩa. Đặc biệt cảnh giác với nhóm trạng từ như however, therefore, moreover: chúng không có quyền nối 2 câu bằng dấu phẩy mà bắt buộc dùng chấm hoặc chấm phẩy."
        },
        {
            "id": "sec_five_rules",
            "title": "2. Năm công thức nối 2 IC & Mẹo tương đương",
            "selector": "#sec-five-rules",
            "en": "Section 2 gives you the five legal ways to link two independent clauses: a period, a semicolon, a comma plus FANBOYS, a colon when the second clause explains the first, or a single em-dash. Use the Equivalence Shortcut: whenever two options differ only by a period versus a semicolon between two independent clauses, both must be wrong because the SAT cannot have two equally correct answers.",
            "vi": "Mục 2 tổng hợp 5 công thức nối hai mệnh đề độc lập hợp lệ: dấu chấm, chấm phẩy, phẩy cộng FANBOYS, hai chấm và gạch ngang đơn. Hãy tận dụng Mẹo Tương đương: nếu hai đáp án giống hệt nhau và chỉ khác nhau giữa dấu chấm và dấu chấm phẩy nối hai IC, cả hai đều chắc chắn sai vì đề không bao giờ có hai đáp án cùng đúng."
        },
        {
            "id": "sec_colon_trap",
            "title": "3. Bẫy Dấu Hai Chấm & Super-Semicolon",
            "selector": "#sec-colon-trap",
            "en": "Section 3 highlights two high-yield traps. First, never place a colon directly after a verb or preposition like were, includes, or such as—the clause before a colon must stand completely on its own. Second, remember the super-semicolon: when items in a complex list already contain internal commas, semicolons separate the major list items.",
            "vi": "Mục 3 chỉ rõ hai bẫy hay gặp. Thứ nhất, tuyệt đối không đặt dấu hai chấm ngay sau động từ hay giới từ như were hay such as vì vế trước hai chấm bắt buộc phải là một câu hoàn chỉnh. Thứ hai, nhớ quy tắc Super-Semicolon dùng chấm phẩy để ngăn các mục lớn trong danh sách đã có sẵn dấu phẩy bên trong."
        },
        {
            "id": "sec_sop",
            "title": "4. Quy trình 3 bước giải trong 20 giây",
            "selector": "#sec-sop",
            "en": "Finally, follow the three-step speed routine: scan the answer choices first to spot punctuation shifts, label the left and right sides of the blank as independent or dependent, and apply the five linking rules to eliminate traps instantly.",
            "vi": "Cuối cùng, hãy thực hành quy trình 3 bước: liếc đáp án nhận diện dạng câu dấu câu, chia đôi câu tại chỗ trống để gắn nhãn IC hay DC cho hai vế, rồi áp dụng ngay 5 công thức và mẹo tương đương để chốt đáp án dưới 20 giây."
        }
    ]
    lectures.append({
        "code": "2_1",
        "module_key": "rw_m2",
        "order_index": 1,
        "title": "2.1 Boundaries I: Clauses, Linking & Core Punctuation",
        "drill_key": "drill_2_1",
        "drill_title": "Drill 2.1: Boundaries I — Clauses, Linking & Core Punctuation (15 Qs)",
        "html": html_2_1,
        "segments": seg_2_1,
        "major_sections": {f"{s['id']}": {"start": i, "end": i} for i, s in enumerate(seg_2_1)},
    })

    # =========================================================================
    # LECTURE 2.2: Boundaries II — Modifiers, Appositives & Transitions
    # =========================================================================
    html_2_2 = build_sat_lecture_html(
        badge_text="Digital SAT 1500+ • R&W Module 2 • Standard English Conventions",
        title="2.2 Boundaries II: Essential vs. Non-Essential Elements & Punctuation Traps",
        subtitle="Xử lý dứt điểm quy tắc 'Phẩy đôi / Gạch ngang đôi', bẫy Title + Name (không dấu phẩy) và lỗi ngắt Chủ ngữ – Động từ.",
        intro_points=[
            "Phân biệt chuẩn xác Essential (Bắt buộc — KHÔNG phẩy) vs. Non-Essential (Bổ sung — CẶP phẩy/gạch ngang).",
            "Nắm chắc bẫy 'Nghề nghiệp + Tên riêng' (VD: physicist Marie Curie) — câu ăn điểm kinh điển của Digital SAT.",
            "Tuyệt đối tránh 4 vị trí CẤM đặt dấu phẩy đơn lẻ (giữa S–V, giữa V–O, trước 'that', trước giới từ giới hạn).",
        ],
        cards_html='''
  <div id="sec-essential" class="lecture-interactive-card sat-card" data-lecture-section="sec_essential">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>1. Quy tắc "Nhấc Bỏ" (Cross-Out Test): Essential vs. Non-Essential</h2>
    <p>Khi một cụm bổ ngữ (appositive, participial phrase, hoặc mệnh đề quan hệ) nằm giữa câu, hãy thử <b>che cụm đó lại</b> và đọc phần còn lại của câu:</p>
    <table class="sat-table">
      <thead>
        <tr><th>Phân loại</th><th>Kết quả khi che đi</th><th>Quy tắc dấu câu bắt buộc</th></tr>
      </thead>
      <tbody>
        <tr>
          <td><b>Non-Essential</b><br/><i>(Thông tin bổ sung thêm)</i></td>
          <td>Câu vẫn rõ đối tượng nào đang được nói tới và giữ nguyên nghĩa cốt lõi.</td>
          <td><b>Bọc bằng 1 CẶP dấu giống nhau:</b><br/><span class="sat-code">, ... ,</span> hoặc <span class="sat-code">— ... —</span> hoặc <span class="sat-code">( ... )</span><br/><i>(CẤM ghép lệch <code>, ... —</code>!)</i></td>
        </tr>
        <tr>
          <td><b>Essential</b><br/><i>(Thông tin định danh bắt buộc)</i></td>
          <td>Câu trở nên mơ hồ, không biết đang nói đến ai/vật nào, hoặc sai nghĩa.</td>
          <td><b>KHÔNG DÙNG BẤT KỲ DẤU PHẨY NÀO</b> ở cả 2 đầu cụm từ!</td>
        </tr>
      </tbody>
    </table>
    <div class="sat-ex-box">
      <b>✅ Non-Essential (Đã xác định rõ nhờ tên riêng/từ hạn định):</b><br/>
      <i>Dr. Lin's debut monograph<b>,</b> published in 2019<b>,</b> reshaped urban hydrology.</i> (Có cặp phẩy)<br/>
      <b>✅ Essential (Cần cụm sau để định danh cụ thể):</b><br/>
      <i>Botanists <b>who study alpine lichens</b> rely on high-resolution imagery.</i> (KHÔNG có dấu phẩy!)
    </div>
  </div>

  <div id="sec-name-trap" class="lecture-interactive-card sat-card" data-lecture-section="sec_name_trap">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>2. "Mỏ Vàng" Digital SAT: Quy tắc Chức danh + Tên riêng (Title + Name)</h2>
    <p>Đây là dạng câu xuất hiện với tần suất dày đặc nhất trong mọi đề Digital SAT 2024–2026. Chỉ cần nhìn xem trước chức danh có từ hạn định (<i>the, a, her, this...</i>) hay không:</p>
    <table class="sat-table">
      <thead>
        <tr><th>Cấu trúc</th><th>Bắt buộc hay Bổ sung?</th><th>Dấu phẩy?</th><th>Ví dụ chuẩn</th></tr>
      </thead>
      <tbody>
        <tr>
          <td><b>[Không có mạo từ] + Nghề nghiệp + Tên riêng</b></td>
          <td><b>Essential</b> (tên riêng là phần định danh duy nhất)</td>
          <td><b>KHÔNG PHẨY (0)</b></td>
          <td><i>Japanese architect <b>Kengo Kuma</b> designed the pavilion.</i></td>
        </tr>
        <tr>
          <td><b>[Có mạo từ/sở hữu: the/a/his] + Cụm mô tả duy nhất + Tên riêng</b></td>
          <td><b>Non-Essential</b> (đã xác định 1 người duy nhất trước đó)</td>
          <td><b>CẶP PHẨY (2)</b></td>
          <td><i>The museum's chief curator<b>,</b> <b>Elena Morales,</b> opened the vault.</i></td>
        </tr>
        <tr>
          <td><b>Tên riêng + Cụm nghề nghiệp phía sau</b></td>
          <td><b>Non-Essential</b> (tên đã xác định rõ người)</td>
          <td><b>CẶP PHẨY (2)</b></td>
          <td><i>Kengo Kuma<b>,</b> <b>a renowned Japanese architect,</b> designed the pavilion.</i></td>
        </tr>
      </tbody>
    </table>
    <div class="sat-gold-box">
      <b>💡 Mẹo nhớ 1 giây:</b> Nếu đầu câu là <code>[Nationality/Job] + [Name]</code> KHÔNG có <i>a/the/my</i> (VD: <i>marine biologist Sylvia Earle</i>, <i>novelist Toni Morrison</i>) → <b>TUYỆT ĐỐI KHÔNG BAO GIỜ ĐẶT DẤU PHẨY</b> giữa chức danh và tên, cũng không đặt phẩy ngay sau tên trước động từ!
    </div>
  </div>

  <div id="sec-forbidden" class="lecture-interactive-card sat-card" data-lecture-section="sec_forbidden">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>3. Bốn Vị Trí CẤM Dấu Phẩy Đơn Lẻ (The 4 No-Comma Zones)</h2>
    <p>Trong tiếng Việt đôi khi ta dừng lấy hơi ở chủ ngữ dài nên hay có thói quen chèn dấu phẩy. Trên Digital SAT, <b>KHÔNG BAO GIỜ đặt 1 dấu phẩy đơn lẻ</b> tại 4 vị trí sau:</p>
    <ol style="padding-left:20px; margin:8px 0;">
      <li><b>Giữa Chủ ngữ và Động từ chính (S , V):</b> <i>❌ The discovery of microplastics in Antarctic snow, alarmed climatologists.</i> (Chú ý: cặp 2 dấu phẩy bọc cụm bổ sung ở giữa thì ĐƯỢC, nhưng 1 dấu đơn lẻ thì CẤM!)</li>
      <li><b>Giữa Động từ và Tân ngữ (V , O):</b> <i>❌ The team demonstrated, that the alloy resists corrosion.</i></li>
      <li><b>Ngay trước hoặc ngay sau chữ <span class="sat-code">that</span> (bổ ngữ/mệnh đề danh ngữ):</b> <i>❌ Researchers argued, that..., ❌ Researchers argued that, ...</i></li>
      <li><b>Giữa Giới từ và Danh từ của nó (Prep , N) hoặc trước <span class="sat-code">such as</span> khi liệt kê bắt buộc:</b> <i>❌ The study focused on, glacial meltwater.</i></li>
    </ol>
  </div>

  <div id="sec-interrupt-trans" class="lecture-interactive-card sat-card" data-lecture-section="sec_interrupt_trans">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>4. Dấu câu quanh Từ nối Chen Giữa (Interrupting Transitions)</h2>
    <p>Phân biệt cực kỳ cẩn thận 2 vị trí của <b>however / though / therefore / for instance</b>:</p>
    <div class="sat-ex-box">
      <b>• Trường hợp A — Nối 2 mệnh đề độc lập (IC + IC):</b><br/>
      <i>The prototype passed thermal trials<b>; however,</b> it failed pressure testing.</i> (Chấm phẩy trước + Phẩy sau)<br/><br/>
      <b>• Trường hợp B — Chen vào GIỮA 1 mệnh đề duy nhất (Interrupter):</b><br/>
      <i>The prototype<b>, however,</b> failed pressure testing.</i> (Cặp 2 dấu phẩy bọc lấy <i>however</i>!)<br/>
      <b>⚠️ CẤM:</b> <i>The prototype; however, failed...</i> (Vì <i>The prototype</i> không phải IC nên KHÔNG được dùng dấu chấm phẩy!)
    </div>
  </div>
''',
        quick_check_html=make_quick_check_html(
            qc_id="qc_2_2",
            passage_html="During the 1960s, Mexican ______ helped pioneer a bold geometric style of public sculpture that transformed highway corridors around Mexico City into open-air galleries.",
            question_prompt="Which choice completes the text so that it conforms to the conventions of Standard English?",
            options=[
                "sculptor, Mathias Goeritz,",
                "sculptor Mathias Goeritz",
                "sculptor Mathias Goeritz,",
                "sculptor, Mathias Goeritz"
            ],
            correct_idx=1,
            explanation_vi="Cấu trúc '[Quốc tịch + Nghề nghiệp] + Tên riêng' KHÔNG có mạo từ a/the ở trước ('Mexican sculptor Mathias Goeritz') là cụm danh từ định danh bắt buộc (Essential) và làm Chủ ngữ trực tiếp cho động từ 'helped'. Do đó KHÔNG đặt dấu phẩy nào giữa chức danh–tên và KHÔNG đặt phẩy đơn giữa Chủ ngữ–Động từ. Chọn B."
        )
    )
    seg_2_2 = [
        {
            "id": "intro",
            "title": "Giới thiệu Bài 2.2: Boundaries II — Modifiers & Appositives",
            "selector": "#sec-header",
            "en": "Welcome to Lesson 2.2: Boundaries Part Two. Today we master the highest-frequency punctuation rules on the Digital SAT: essential versus non-essential elements, the title-plus-name rule, forbidden single commas, and interrupting transitions.",
            "vi": "Chào mừng các bạn đến với Bài 2.2: Ranh giới câu Phần 2. Hôm nay chúng ta sẽ làm chủ các quy tắc dấu phẩy hay ra thi nhất trên Digital SAT: phân biệt thông tin bắt buộc và bổ sung, quy tắc chức danh đi với tên riêng, bốn vị trí cấm dấu phẩy và từ nối chen giữa câu."
        },
        {
            "id": "sec_essential",
            "title": "1. Quy tắc Nhấc Bỏ: Essential vs. Non-Essential",
            "selector": "#sec-essential",
            "en": "Section 1 explains the cross-out test. If you can delete a middle phrase and the sentence still clearly identifies who or what it is talking about, the phrase is non-essential and must be bracketed by matching punctuation—two commas, two dashes, or two parentheses. Never mix a comma on one side with a dash on the other. If deleting the phrase breaks the sentence's identification, it is essential and takes zero commas.",
            "vi": "Mục 1 hướng dẫn phép thử nhấc bỏ. Nếu che cụm bổ ngữ đi mà câu vẫn rõ chủ thể và trọn nghĩa, đó là thông tin bổ sung và bắt buộc phải bọc bằng một cặp dấu giống nhau: hai phẩy, hai gạch ngang hoặc ngoặc đơn, tuyệt đối không ghép lệch phẩy với gạch ngang. Ngược lại, nếu thiếu nó câu bị mơ hồ thì đó là thành phần bắt buộc và không dùng dấu phẩy."
        },
        {
            "id": "sec_name_trap",
            "title": "2. Quy tắc Chức danh + Tên riêng",
            "selector": "#sec-name-trap",
            "en": "Section 2 reveals a signature Digital SAT goldmine: the title-plus-name pattern. When a profession or nationality precedes a name with no article like a or the—for example, Japanese architect Kengo Kuma—the name is essential, so you must use zero commas around it. By contrast, when a unique title uses the or a possessive—like the museum's chief curator, Elena Morales—bracket the name with two commas.",
            "vi": "Mục 2 chỉ ra dạng câu ăn điểm đặc trưng của Digital SAT: cấu trúc Chức danh kèm Tên riêng. Khi nghề nghiệp đứng trước tên mà không có mạo từ như a hay the—ví dụ Japanese architect Kengo Kuma—tuyệt đối không đặt dấu phẩy nào. Chỉ khi có mạo từ xác định một người duy nhất phía trước hoặc khi nghề nghiệp đứng sau tên riêng, ta mới dùng cặp hai dấu phẩy."
        },
        {
            "id": "sec_forbidden",
            "title": "3. Bốn vị trí CẤM dấu phẩy đơn lẻ",
            "selector": "#sec-forbidden",
            "en": "Section 3 locks down the four no-comma zones. Never drop a single comma between a subject and its main verb, between a verb and its object, directly before or after the conjunction that, or between a preposition and its noun. When in doubt, fewer commas usually win on the Digital SAT.",
            "vi": "Mục 3 chốt bốn vùng cấm dấu phẩy đơn lẻ: không tách chủ ngữ khỏi động từ chính bằng một dấu phẩy, không tách động từ khỏi tân ngữ, không đặt phẩy sát trước hay sau từ that, và không tách giới từ khỏi danh từ. Trên Digital SAT, nguyên tắc an toàn là không thêm dấu phẩy theo cảm giác ngắt hơi."
        },
        {
            "id": "sec_interrupt_trans",
            "title": "4. Dấu câu quanh Từ nối chen giữa câu",
            "selector": "#sec-interrupt-trans",
            "en": "Section 4 contrasts two uses of however. Between two complete independent clauses, you need a semicolon before however and a comma after it. Inside a single clause—such as The prototype, however, failed pressure testing—however is merely an interrupter, so surround it with two commas, never a semicolon.",
            "vi": "Mục 4 phân biệt hai vị trí của từ nối như however. Khi đứng giữa hai mệnh đề độc lập, nó cần chấm phẩy phía trước và phẩy phía sau. Nhưng khi chen vào giữa chủ ngữ và động từ của cùng một câu, nó chỉ là thành phần xen kẽ nên phải bọc bằng cặp hai dấu phẩy, tuyệt đối không dùng chấm phẩy."
        }
    ]
    lectures.append({
        "code": "2_2",
        "module_key": "rw_m2",
        "order_index": 2,
        "title": "2.2 Boundaries II: Essential vs. Non-Essential Elements & Punctuation Traps",
        "drill_key": "drill_2_2",
        "drill_title": "Drill 2.2: Boundaries II — Modifiers, Appositives & Punctuation Traps (15 Qs)",
        "html": html_2_2,
        "segments": seg_2_2,
        "major_sections": {f"{s['id']}": {"start": i, "end": i} for i, s in enumerate(seg_2_2)},
    })

    # =========================================================================
    # LECTURE 2.3: Form, Structure & Sense I — Verbs & Agreement
    # =========================================================================
    html_2_3 = build_sat_lecture_html(
        badge_text="Digital SAT 1500+ • R&W Module 2 • Standard English Conventions",
        title="2.3 Form, Structure & Sense I: Subject–Verb Agreement, Finite Verbs & Tense",
        subtitle="Tìm đúng Chủ ngữ thật xuyên qua rừng cụm giới từ & đảo ngữ, phân biệt Động từ chia thì (Finite) vs. Phân từ (V-ing/to-V).",
        intro_points=[
            "Áp dụng kỹ thuật 'Gạch bỏ Prepositional & Non-Essential Phrases' để tìm đúng Chủ ngữ thật trong 3 giây.",
            "Nhận diện 5 cấu trúc Chủ ngữ bẫy kinh điển của Hard Module 2 (Gerund, Inverted Subject, Each/Every, The number of vs. A number of).",
            "Phân biệt rạch ròi khi nào chỗ trống cần Động từ chia thì (Finite Verb) vs. Phân từ (Participle / Infinitive).",
        ],
        cards_html='''
  <div id="sec-sv-core" class="lecture-interactive-card sat-card" data-lecture-section="sec_sv_core">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>1. Bẫy "Tách xa Chủ ngữ – Động từ" &amp; Quy tắc 3–1 (Odd-One-Out)</h2>
    <p>College Board hầu như không bao giờ kiểm tra <i>The dog runs</i>. Họ sẽ nhét <b>10–20 từ nhiễu</b> (cụm giới từ <i>of/in/by/with</i>, cụm phân từ, mệnh đề quan hệ) vào giữa Chủ ngữ thật và Động từ!</p>
    <div class="sat-ex-box">
      <i>A recent <b>collection</b> <s>[of terracotta figurines excavated from Bronze Age tombs near the Aegean coast]</s> <b>reveals</b> (số ít!) shifting trade patterns.</i>
    </div>
    <div class="sat-gold-box">
      <b>⚡ Mẹo 3–1 cực đỉnh (Singular vs. Plural Shortcut):</b><br/>
      Khi thấy 4 đáp án đều là dạng của 1 động từ (VD: <i>A. reveal | B. have revealed | C. are revealing | D. reveals</i>):<br/>
      Đếm ngay số đáp án số ít vs. số nhiều! Ở trên có <b>3 đáp án số nhiều</b> (A, B, C) và chỉ <b>1 đáp án số ít</b> (D) → 95% đáp án chính xác là kẻ đơn độc <b>D</b> (nhưng vẫn kiểm tra lại Chủ ngữ trong 3 giây để đạt 100%!).
    </div>
  </div>

  <div id="sec-sv-traps" class="lecture-interactive-card sat-card" data-lecture-section="sec_sv_traps">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>2. Năm Chủ Ngữ Bẫy Đặc Sản Của Hard Module 2</h2>
    <table class="sat-table">
      <thead>
        <tr><th>Cấu trúc Chủ ngữ bẫy</th><th>Động từ chia</th><th>Ví dụ chuẩn Digital SAT</th></tr>
      </thead>
      <tbody>
        <tr><td><b>1. Gerund / Clause Subject</b> (<i>V-ing... / That S+V...</i>)</td><td><b>SỐ ÍT</b></td><td><i><b>Analyzing</b> thousands of lunar samples <b>requires</b>...</i></td></tr>
        <tr><td><b>2. Inverted Subject</b> (Cụm giới từ/trạng ngữ đảo lên đầu)</td><td>Chia theo danh từ <b>SAU động từ</b></td><td><i>Beneath the glacial sediment <b>lie</b> three ancient <b>riverbeds</b>.</i></td></tr>
        <tr><td><b>3. Each / Every / Either / Neither / One</b> (+ of the plural N)</td><td><b>SỐ ÍT</b></td><td><i><b>Each</b> of the fourteen manuscripts <b>contains</b>...</i></td></tr>
        <tr><td><b>4. The number of N</b> vs. <b>A number of N</b></td><td><i>The number</i> → <b>ÍT</b><br/><i>A number</i> → <b>NHIỀU</b></td><td><i><b>The number</b> of species <b>has</b> declined.</i><br/><i><b>A number</b> of species <b>have</b> adapted.</i></td></tr>
        <tr><td><b>5. S1, along with / as well as / accompanied by S2</b></td><td>Chia theo <b>S1</b> (bỏ cụm phẩy)</td><td><i>The <b>composer</b>, along with two cellists, <b>was</b> invited.</i></td></tr>
      </tbody>
    </table>
  </div>

  <div id="sec-finite" class="lecture-interactive-card sat-card" data-lecture-section="sec_finite">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>3. Finite Verb (Động từ chính) vs. Non-Finite (V-ing / to-V / V-ed)</h2>
    <p>Đây là bẫy ngữ pháp khiến nhiều bạn 700+ mất điểm oan nhất! Một câu hoàn chỉnh <b>BẮT BUỘC có đúng 1 động từ chia thì (Finite Verb)</b> cho mỗi mệnh đề độc lập:</p>
    <div class="sat-rule-box">
      <b>🔍 Phép thử Động từ Chính (Main Verb Check):</b><br/>
      • <b>Nếu câu CHƯA có động từ chia thì cho chủ ngữ</b> → Chỗ trống <b>BẮT BUỘC chọn Finite Verb</b> (VD: <i>produces, led, has shaped</i>). Loại ngay <i>producing, to produce, having produced</i> (vì sẽ tạo Fragment!).<br/>
      • <b>Nếu câu ĐÃ CÓ sẵn động từ chia thì phía sau/trước (và không có liên từ nối)</b> → Chỗ trống <b>PHẢI chọn Non-Finite</b> (<i>V-ing, V-ed, to-V</i>) để làm cụm bổ ngữ, tránh tạo lỗi 2 động từ chính đánh nhau!
    </div>
    <div class="sat-ex-box">
      <b>Ví dụ thực chiến:</b><br/>
      <i>Synthesizing insights from acoustics and architecture, researcher Mira Patel ______ a ceiling panel that absorbs low-frequency noise.</i><br/>
      → Chủ ngữ <i>Mira Patel</i> CHƯA có động từ chính (<i>Synthesizing</i> chỉ là phân từ, <i>absorbs</i> nằm trong mệnh đề <i>that</i>) → Bắt buộc chọn động từ chia thì <b>designed</b> (loại <i>designing</i> và <i>to design</i>!).
    </div>
  </div>

  <div id="sec-tense" class="lecture-interactive-card sat-card" data-lecture-section="sec_tense">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>4. Sự Hòa Hợp Thì (Verb Tense Consistency) &amp; Mốc Thời Gian</h2>
    <ul style="padding-left:20px; margin:8px 0;">
      <li><b>Tìm "Mỏ neo thời gian" (Time Anchor):</b> Luôn quét câu trước &amp; cùng câu xem các động từ khác đang ở <i>quá khứ đơn (1920s, discovered)</i>, <i>hiện tại đơn (quy luật khoa học, mô tả tác phẩm văn học)</i> hay <i>hiện tại hoàn thành (since 1998, over the past decade)</i>.</li>
      <li><b>Quá khứ hoàn thành (had + V3):</b> Chỉ dùng khi 1 hành động xảy ra <b>trước hẳn 1 mốc quá khứ cụ thể khác</b> trong câu (VD: <i>By the time the telescope launched in 2021, engineers <b>had spent</b> a decade calibrating its mirrors.</i>).</li>
      <li><b>Conditional / Hypothetical (would + V):</b> Khi vế điều kiện dùng quá khứ giả định (<i>If the glacier melted...</i>) hoặc tường thuật trong quá khứ (<i>predicted that the treaty <b>would</b> stabilize...</i>), chọn <b>would</b> chứ không chọn <i>will</i>.</li>
    </ul>
  </div>
''',
        quick_check_html=make_quick_check_html(
            qc_id="qc_2_3",
            passage_html="Hidden beneath the dense canopy of Costa Rica's Osa Peninsula ______ several previously undocumented species of bioluminescent fungi, which researchers cataloged using long-exposure night photography.",
            question_prompt="Which choice completes the text so that it conforms to the conventions of Standard English?",
            options=[
                "thrives",
                "has thrived",
                "thrive",
                "thriving"
            ],
            correct_idx=2,
            explanation_vi="Đây là câu Đảo ngữ (Inverted Subject): cụm phân từ/giới từ 'Hidden beneath the dense canopy...' đứng đầu câu, còn Chủ ngữ thật nằm PHÍA SAU động từ là 'several previously undocumented species' (SỐ NHIỀU). Đồng thời câu chưa có động từ chính cho mệnh đề độc lập → Loại D (thriving là phân từ). A và B đều số ít → Chọn C (thrive - số nhiều)."
        )
    )
    seg_2_3 = [
        {
            "id": "intro",
            "title": "Giới thiệu Bài 2.3: Subject-Verb Agreement & Finite Verbs",
            "selector": "#sec-header",
            "en": "Welcome to Lesson 2.3: Form, Structure, and Sense Part One. Here we dissect how the Digital SAT disguises true subjects inside dense academic sentences, tests finite versus non-finite verbs, and enforces tense consistency.",
            "vi": "Chào mừng các bạn đến với Bài 2.3: Hình thức, Cấu trúc và Ngữ nghĩa Phần 1. Trong bài này ta sẽ giải mã cách đề Digital SAT giấu chủ ngữ thật giữa rừng cụm giới từ, phân biệt động từ chia thì với phân từ, và xử lý chính xác sự hòa hợp thì."
        },
        {
            "id": "sec_sv_core",
            "title": "1. Bẫy tách xa Chủ ngữ – Động từ & Mẹo 3–1",
            "selector": "#sec-sv-core",
            "en": "Section 1 shows the classic separation trap. Always cross out prepositional phrases starting with of, in, with, or by between the subject and the verb. Then apply the three-to-one shortcut: if three answer choices are plural and only one is singular, the lone singular option is almost certainly the intended answer—verify the core subject to be one hundred percent sure.",
            "vi": "Mục 1 phân tích bẫy tách xa chủ ngữ và động từ. Hãy luôn gạch nhẩm các cụm giới từ như of, in, with chen giữa để lộ ra chủ ngữ gốc. Kết hợp với Mẹo 3–1: nếu có 3 đáp án số nhiều và duy nhất 1 đáp án số ít, phương án đơn độc đó thường chính là đáp án đúng."
        },
        {
            "id": "sec_sv_traps",
            "title": "2. Năm Chủ ngữ bẫy Hard Module 2",
            "selector": "#sec-sv-traps",
            "en": "Section 2 lists five Hard Module 2 subject traps: gerund subjects are always singular; inverted sentences hide the real subject after the verb; indefinite pronouns like each and every take singular verbs even before plural nouns; the number of is singular while a number of is plural; and phrases like along with do not make a singular subject plural.",
            "vi": "Mục 2 điểm mặt 5 chủ ngữ bẫy ở Hard Module 2: chủ ngữ V-ing luôn chia số ít; câu đảo ngữ có chủ ngữ thật nằm sau động từ; each và every luôn chia số ít; the number of đi với số ít còn a number of đi với số nhiều; và cụm along with không làm chủ ngữ biến thành số nhiều."
        },
        {
            "id": "sec_finite",
            "title": "3. Động từ chia thì (Finite) vs. Phân từ (Non-Finite)",
            "selector": "#sec-finite",
            "en": "Section 3 addresses the single most missed grammar item among seven-hundred-plus students: finite versus non-finite verbs. Check whether the main clause already has a conjugated main verb. If it lacks one, you must pick a finite verb and eliminate participles like designing or to design. If a main verb already exists, pick a participle modifier instead.",
            "vi": "Mục 3 xử lý lỗi ngữ pháp dễ mất điểm nhất của học viên trên 700: động từ chia thì so với phân từ. Luôn kiểm tra mệnh đề chính đã có động từ chia thì chưa. Nếu chưa, bắt buộc chọn động từ chia thì và loại các dạng V-ing hay to-V. Nếu đã có rồi, chọn dạng phân từ để tránh lỗi hai động từ chính trong cùng một mệnh đề."
        },
        {
            "id": "sec_tense",
            "title": "4. Hòa hợp thì & Mỏ neo thời gian",
            "selector": "#sec-tense",
            "en": "Section 4 covers tense consistency. Never choose a tense by ear alone—find the time anchor in the surrounding text. Use past perfect had-plus-participle strictly for actions completed before another past anchor, and use would rather than will inside past-tense predictions.",
            "vi": "Mục 4 tổng kết quy tắc hòa hợp thì. Tuyệt đối không chọn thì theo cảm tính mà hãy tìm mỏ neo thời gian trong đoạn văn. Chỉ dùng quá khứ hoàn thành cho sự việc xảy ra trước hẳn một mốc quá khứ khác, và dùng would thay cho will trong các dự đoán đặt ở ngữ cảnh quá khứ."
        }
    ]
    lectures.append({
        "code": "2_3",
        "module_key": "rw_m2",
        "order_index": 3,
        "title": "2.3 Form, Structure & Sense I: Subject–Verb Agreement, Finite Verbs & Tense",
        "drill_key": "drill_2_3",
        "drill_title": "Drill 2.3: Form, Structure & Sense I — Verbs, Agreement & Tense (15 Qs)",
        "html": html_2_3,
        "segments": seg_2_3,
        "major_sections": {f"{s['id']}": {"start": i, "end": i} for i, s in enumerate(seg_2_3)},
    })

    # =========================================================================
    # LECTURE 2.4: Form, Structure & Sense II — Modifiers, Pronouns & Possessives
    # =========================================================================
    html_2_4 = build_sat_lecture_html(
        badge_text="Digital SAT 1500+ • R&W Module 2 • Standard English Conventions",
        title="2.4 Form, Structure & Sense II: Modifiers, Possessives, Pronouns & Parallelism",
        subtitle="Chinh phục 4 chuyên đề còn lại của Standard English Conventions: Dangling Modifiers, Dấu nháy sở hữu, Đại từ và Song song.",
        intro_points=[
            "Tiêu diệt 100% câu hỏi Dangling / Misplaced Modifiers bằng Quy tắc Chủ ngữ sát sau dấu phẩy.",
            "Phân biệt chuẩn xác từng dấu nháy đơn: plural (scientists) vs. singular possessive (scientist's) vs. plural possessive (scientists') & its/it's, whose/who's.",
            "Chốt gọn Đại từ thay thế đúng số lượng (it/its vs. they/their) và so sánh tương đồng (that of / those of).",
        ],
        cards_html='''
  <div id="sec-modifiers" class="lecture-interactive-card sat-card" data-lecture-section="sec_modifiers">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>1. Quy tắc Thép cho Dangling Modifiers (Bổ ngữ lơ lửng)</h2>
    <p>Cực kỳ dễ nhận diện: đầu câu mở bằng <b>1 cụm mô tả</b> (V-ing, V-ed, cụm tính từ hoặc <i>Known for..., Unlike..., Having discovered...</i>) theo sau bởi <b>dấu phẩy (,)</b> rồi tới <b>chỗ trống</b>.</p>
    <div class="sat-rule-box">
      <b>🎯 Quy tắc Bất Di Bất Dịch (Subject-Right-After-Comma Rule):</b><br/>
      Danh từ đóng vai trò <b>CHỦ NGỮ ĐỨNG NGAY SAU DẤU PHẨY</b> bắt buộc phải chính là <b>người/vật thực hiện hoặc được mô tả bởi cụm mở đầu</b>!
    </div>
    <div class="sat-ex-box">
      <b>Đề:</b> <i>Woven from hand-dyed alpaca wool and colored with cochineal pigments, ______</i><br/>
      <b>❌ Bẫy kinh điển (Possessive Subject Trap):</b> <i>Andean weavers' textiles display...</i> → Chủ ngữ thật là <i>textiles</i> (tạm ổn), NHƯNG nếu đáp án là <i><b>Andean weavers</b> create textiles...</i> → SAI! (Chẳng lẽ chính người thợ dệt bị "dệt từ len alpaca"?!).<br/>
      <b>✅ ĐÚNG:</b> <i><b>traditional Andean textiles</b> retain their vivid hues for centuries.</i> (Chính tấm vải được dệt từ len alpaca!)
    </div>
    <div class="sat-trap-box">
      <b>⚠️ Bẫy 750+ cực hiểm — Sở hữu cách giả chủ ngữ:</b><br/>
      Trong cụm <i>"Marie Curie's notebooks"</i>, Chủ ngữ thật là <b>notebooks</b> (những cuốn sổ), KHÔNG PHẢI Marie Curie! Nếu đầu câu viết <i>"Awarded two Nobel Prizes,"</i> thì sau dấu phẩy PHẢI là <b>Marie Curie</b>, KHÔNG ĐƯỢC là <i>Marie Curie's notebooks</i>!
    </div>
  </div>

  <div id="sec-possessives" class="lecture-interactive-card sat-card" data-lecture-section="sec_possessives">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>2. Bảng Quy Tắc Dấu Nháy Đơn (Apostrophes &amp; Possessives)</h2>
    <table class="sat-table">
      <thead>
        <tr><th>Dạng từ</th><th>Ý nghĩa</th><th>Phép thử nhanh ("của...")</th></tr>
      </thead>
      <tbody>
        <tr><td><span class="sat-code">planets</span></td><td>Số nhiều, KHÔNG sở hữu</td><td>Phía sau không có danh từ thuộc quyền sở hữu của nó.</td></tr>
        <tr><td><span class="sat-code">planet's</span></td><td><b>1 hành tinh</b> sở hữu danh từ sau</td><td>"...của <b>một</b> hành tinh" (VD: <i>a planet's orbit</i>).</td></tr>
        <tr><td><span class="sat-code">planets'</span></td><td><b>Nhiều hành tinh</b> sở hữu danh từ sau</td><td>"...của <b>nhiều</b> hành tinh" (VD: <i>both planets' orbits</i>).</td></tr>
        <tr><td><span class="sat-code">its</span> vs. <span class="sat-code">it's</span> vs. <span class="sat-code">its'</span></td><td><code>its</code> = của nó | <code>it's</code> = it is/has | <code>its'</code> = KHÔNG TỒN TẠI!</td><td>Thử thay bằng <b>"it is"</b>: hợp nghĩa thì dùng <code>it's</code>, không hợp thì dùng <code>its</code>.</td></tr>
        <tr><td><span class="sat-code">their / they're / there</span></td><td><code>their</code> = của họ | <code>they're</code> = they are | <code>there</code> = ở đó</td><td>Thử thay bằng <b>"they are"</b> để chốt nhanh.</td></tr>
        <tr><td><span class="sat-code">whose</span> vs. <span class="sat-code">who's</span></td><td><code>whose</code> = của ai/của vật nào | <code>who's</code> = who is/has</td><td>Lưu ý: <b>whose</b> dùng được cho CẢ NGƯỜI LẪN VẬT trên SAT!</td></tr>
      </tbody>
    </table>
  </div>

  <div id="sec-pronouns" class="lecture-interactive-card sat-card" data-lecture-section="sec_pronouns">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>3. Đại từ (Pronoun Agreement) &amp; So sánh tương đồng (Logical Comparison)</h2>
    <ul style="padding-left:20px; margin:8px 0;">
      <li><b>Hòa hợp số ít / số nhiều của Đại từ:</b> Luôn truy ngược chính xác danh từ tiền lệ (Antecedent). Các danh từ tập hợp như <i>the committee, the orchestra, a species, the museum, the species's habitat</i> trên SAT Mỹ đều tính là <b>SỐ ÍT → it / its</b> (KHÔNG dùng <i>they / their</i>).</li>
      <li><b>So sánh cùng cấp (Apples-to-Apples Comparison):</b><br/>
        ❌ <i>The wing structure of a dragonfly is more flexible than <s>a butterfly</s>.</i> (So sánh "cấu trúc cánh" với "con bướm" — SAI!)<br/>
        ✅ <i>The wing structure of a dragonfly is more flexible than <b>that of</b> a butterfly.</i> (Dùng <b>that of</b> cho danh từ số ít, <b>those of</b> cho danh từ số nhiều!).</li>
      <li><b>Cấu trúc Song song (Parallelism):</b> Các yếu tố nối bằng <i>and / or / not only... but also / rather than</i> phải đồng dạng ngữ pháp (cùng danh từ, cùng V-ing, hoặc cùng mệnh đề).</li>
    </ul>
  </div>
''',
        quick_check_html=make_quick_check_html(
            qc_id="qc_2_4",
            passage_html="Renowned for synthesizing complex acoustic patterns from everyday urban noise, ______ premiered at the Kyoto Sound Biennial to widespread acclaim.",
            question_prompt="Which choice completes the text so that it conforms to the conventions of Standard English?",
            options=[
                "composer Kenji Sato's latest symphony",
                "the latest symphony by composer Kenji Sato",
                "composer Kenji Sato had his latest symphony",
                "composer Kenji Sato, whose latest symphony"
            ],
            correct_idx=2,
            explanation_vi="Cụm mở đầu 'Renowned for synthesizing...' mô tả NGƯỜI (nhà soạn nhạc Kenji Sato), KHÔNG mô tả bản giao hưởng! Trong A, chủ ngữ thật là 'symphony' (bẫy Possessive Subject!). Trong B, chủ ngữ cũng là 'symphony'. Trong D, câu thiếu động từ chính cho Kenji Sato (tạo Fragment vì 'premiered' thuộc về mệnh đề 'whose'). Chỉ C đặt đúng chủ ngữ 'composer Kenji Sato' ngay sau dấu phẩy và có động từ chính 'had' hoàn chỉnh!"
        )
    )
    seg_2_4 = [
        {
            "id": "intro",
            "title": "Giới thiệu Bài 2.4: Modifiers, Possessives & Pronouns",
            "selector": "#sec-header",
            "en": "Welcome to Lesson 2.4: Form, Structure, and Sense Part Two. Today we lock down the remaining four Standard English Conventions skills: dangling modifiers, apostrophes and possessives, pronoun agreement, and logical comparisons.",
            "vi": "Chào mừng các bạn đến với Bài 2.4: Hình thức, Cấu trúc và Ngữ nghĩa Phần 2. Hôm nay chúng ta hoàn thiện nốt bốn mảng cuối của Ngữ pháp SAT: bổ ngữ lơ lửng, sở hữu cách, đại từ và cấu trúc so sánh song song."
        },
        {
            "id": "sec_modifiers",
            "title": "1. Dangling Modifiers & Bẫy Sở hữu cách giả Chủ ngữ",
            "selector": "#sec-modifiers",
            "en": "Section 1 gives you the ironclad modifier rule: whenever a sentence opens with a descriptive phrase followed by a comma, the grammatical subject immediately after the comma must be the exact person or thing being described. Watch out for the 750-plus possessive trap: in Marie Curie's notebooks, the subject is notebooks, not Marie Curie.",
            "vi": "Mục 1 đưa ra quy tắc thép cho bổ ngữ mở đầu câu: danh từ làm chủ ngữ đứng ngay sau dấu phẩy bắt buộc phải chính là đối tượng được mô tả. Cảnh giác tuyệt đối với bẫy sở hữu cách: trong cụm Marie Curie's notebooks, chủ ngữ thật là những cuốn sổ chứ không phải nhà khoa học Marie Curie."
        },
        {
            "id": "sec_possessives",
            "title": "2. Dấu nháy đơn & Sở hữu cách",
            "selector": "#sec-possessives",
            "en": "Section 2 demystifies apostrophes. Check two questions: does the noun own the word right after it, and is the owner singular or plural? Remember that its with no apostrophe shows possession, it's always means it is or it has, its-apostrophe does not exist in English, and whose works for both people and inanimate objects.",
            "vi": "Mục 2 hệ thống hóa dấu nháy sở hữu. Chỉ cần kiểm tra hai ý: danh từ đó có sở hữu từ ngay phía sau không, và chủ sở hữu là số ít hay số nhiều. Luôn nhớ its không phẩy là sở hữu, it's là viết tắt của it is, dạng its phẩy sau s không tồn tại, và whose dùng được cho cả người lẫn vật."
        },
        {
            "id": "sec_pronouns",
            "title": "3. Đại từ, So sánh tương đồng & Song song",
            "selector": "#sec-pronouns",
            "en": "Section 3 covers pronoun matching and apples-to-apples comparisons. Collective nouns like a committee or a species take singular pronouns it and its on the American SAT. For comparisons, make sure you compare like with like by using that of for singular nouns and those of for plural nouns.",
            "vi": "Mục 3 chốt quy tắc đại từ và so sánh tương đồng. Danh từ tập hợp như committee hay species trên SAT Mỹ luôn quy về số ít it và its. Khi so sánh hai đối tượng, luôn đối chiếu cùng cấp độ bằng cách dùng that of cho danh từ số ít và those of cho danh từ số nhiều."
        }
    ]
    lectures.append({
        "code": "2_4",
        "module_key": "rw_m2",
        "order_index": 4,
        "title": "2.4 Form, Structure & Sense II: Modifiers, Possessives, Pronouns & Parallelism",
        "drill_key": "drill_2_4",
        "drill_title": "Drill 2.4: Form, Structure & Sense II — Modifiers, Possessives & Pronouns (15 Qs)",
        "html": html_2_4,
        "segments": seg_2_4,
        "major_sections": {f"{s['id']}": {"start": i, "end": i} for i, s in enumerate(seg_2_4)},
    })

    return lectures
