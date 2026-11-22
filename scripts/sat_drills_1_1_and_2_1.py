# -*- coding: utf-8 -*-
"""
Hand-crafted 1500+ Elite Digital SAT R&W Skill Drills:
- Drill 1.1: Digital SAT 1500+ Diagnostic & Trap Identification (12 Qs)
- Drill 2.1: Boundaries I — Clauses, Linking & Core Punctuation (15 Qs)
"""

def q_item(qid, num, domain, skill, diff, stim, stem, opts, ans, summary_vi, takeaway, analysis):
    labels = ['A', 'B', 'C', 'D']
    return {
        'id': qid,
        'number': num,
        'domain': domain,
        'skill': skill,
        'difficulty': diff,
        'stimulusHtml': stim,
        'questionHtml': stem,
        'options': [{'label': labels[i], 'text': opts[i]} for i in range(4)],
        'correctAnswer': ans,
        'explanation': {
            'summaryVi': summary_vi,
            'keyTakeaway': takeaway,
            'optionAnalysis': {
                labels[i]: {
                    'status': 'correct' if labels[i] == ans else 'trap',
                    'trapTag': analysis[i][0],
                    'reasonVi': analysis[i][1],
                }
                for i in range(4)
            },
        },
    }

def get_drill_1_1():
    svg_chart = '''
    <div style="background:#f8fafc;border:1px solid #cbd5e1;border-radius:10px;padding:12px 14px;margin-bottom:12px;">
      <div style="font-family:'Segoe UI',sans-serif;font-size:13px;font-weight:800;color:#0f172a;text-align:center;margin-bottom:6px;">
        Urban Tree Canopy Cover (%) vs. Summer Surface Temperature Anomaly (°C)
      </div>
      <svg viewBox="0 0 460 190" xmlns="http://www.w3.org/2000/svg" style="max-width:440px;">
        <rect x="0" y="0" width="460" height="190" fill="#ffffff"/>
        <line x1="60" y1="20" x2="60" y2="150" stroke="#334155" stroke-width="1.5"/>
        <line x1="60" y1="150" x2="430" y2="150" stroke="#334155" stroke-width="1.5"/>
        <!-- Y Grid -->
        <line x1="60" y1="120" x2="430" y2="120" stroke="#e2e8f0" stroke-dasharray="3,3"/>
        <line x1="60" y1="90" x2="430" y2="90" stroke="#e2e8f0" stroke-dasharray="3,3"/>
        <line x1="60" y1="60" x2="430" y2="60" stroke="#e2e8f0" stroke-dasharray="3,3"/>
        <line x1="60" y1="30" x2="430" y2="30" stroke="#e2e8f0" stroke-dasharray="3,3"/>
        <text x="52" y="154" font-size="10" text-anchor="end" fill="#475569" font-family="sans-serif">0°C</text>
        <text x="52" y="124" font-size="10" text-anchor="end" fill="#475569" font-family="sans-serif">+1°C</text>
        <text x="52" y="94" font-size="10" text-anchor="end" fill="#475569" font-family="sans-serif">+2°C</text>
        <text x="52" y="64" font-size="10" text-anchor="end" fill="#475569" font-family="sans-serif">+3°C</text>
        <text x="52" y="34" font-size="10" text-anchor="end" fill="#475569" font-family="sans-serif">+4°C</text>
        <!-- Bars: District A (10% canopy, +3.8C), B (22% canopy, +2.6C), C (35% canopy, +1.4C), D (48% canopy, +0.4C) -->
        <rect x="85" y="36" width="52" height="114" fill="#1e3a8a" rx="3"/>
        <text x="111" y="31" font-size="10" font-weight="bold" text-anchor="middle" fill="#1e3a8a" font-family="sans-serif">+3.8°C</text>
        <text x="111" y="166" font-size="10" text-anchor="middle" fill="#0f172a" font-family="sans-serif">Dist. A (10%)</text>

        <rect x="175" y="72" width="52" height="78" fill="#2563eb" rx="3"/>
        <text x="201" y="67" font-size="10" font-weight="bold" text-anchor="middle" fill="#2563eb" font-family="sans-serif">+2.6°C</text>
        <text x="201" y="166" font-size="10" text-anchor="middle" fill="#0f172a" font-family="sans-serif">Dist. B (22%)</text>

        <rect x="265" y="108" width="52" height="42" fill="#0284c7" rx="3"/>
        <text x="291" y="103" font-size="10" font-weight="bold" text-anchor="middle" fill="#0284c7" font-family="sans-serif">+1.4°C</text>
        <text x="291" y="166" font-size="10" text-anchor="middle" fill="#0f172a" font-family="sans-serif">Dist. C (35%)</text>

        <rect x="355" y="138" width="52" height="12" fill="#0d9488" rx="3"/>
        <text x="381" y="133" font-size="10" font-weight="bold" text-anchor="middle" fill="#0d9488" font-family="sans-serif">+0.4°C</text>
        <text x="381" y="166" font-size="10" text-anchor="middle" fill="#0f172a" font-family="sans-serif">Dist. D (48%)</text>
      </svg>
    </div>
    <p>Urban planners hypothesize that increasing neighborhood tree canopy cover systematically reduces the urban heat-island effect—measured as the summer surface temperature anomaly above surrounding rural areas. However, a skeptical councilor claims that canopy cover has no meaningful cooling effect once a neighborhood exceeds 25% coverage.</p>'''

    questions = [
        q_item(
            'd1_1_q1', 1, 'Craft and Structure', 'Words in Context', 'Hard',
            '<p>Although early biographers portrayed the nineteenth-century mathematician Ada Lovelace as a solitary visionary working in isolation, newly digitized correspondence with Charles Babbage and Augustus De Morgan ______ that depiction, revealing an intensely collaborative intellectual network.</p>',
            'Which choice completes the text with the most logical and precise word or phrase?',
            ['corroborates', 'belies', 'emulates', 'perpetuates'],
            'B',
            'Cụm "Although early biographers portrayed... solitary visionary" tạo thế đối lập rõ rệt với "revealing an intensely collaborative intellectual network". Do đó động từ điền vào chỗ trống phải mang nghĩa "bác bỏ / chứng minh điều ngược lại" → belies.',
            'Luôn khóa từ chuyển hướng (Although) và vế giải thích phía sau dấu phẩy (revealing...) để chốt chính xác hướng nghĩa trước khi nhìn đáp án.',
            [
                ('Opposite Meaning', 'corroborates = củng cố/chứng thực — ngược hoàn toàn với ý đối lập "Although".'),
                ('Đáp án đúng', 'belies = phơi bày sự sai lệch / bác bỏ hình ảnh trước đó, khớp tuyệt đối với "collaborative" trái ngược "solitary".'),
                ('Wrong Meaning', 'emulates = bắt chước/noi gương — không phù hợp với chủ ngữ "correspondence".'),
                ('Opposite Meaning', 'perpetuates = duy trì kéo dài — ngược với ý lật ngược quan niệm cũ.'),
            ]
        ),
        q_item(
            'd1_1_q2', 2, 'Craft and Structure', 'Text Structure and Purpose', 'Hard',
            '<p>In 2021, acoustic ecologist Dr. Samir Patel recorded toadfish vocalizations near busy ferry terminals in Chesapeake Bay. Conventional models assumed that marine fish simply stop calling when vessel noise exceeds 110 decibels. <u>Patel’s hydrophone arrays, however, captured toadfish shifting their fundamental call frequency upward by nearly 140 hertz within seconds of an approaching hull.</u> This rapid vocal plasticity indicates that certain benthic species possess active real-time strategies for coping with anthropogenic noise.</p>',
            'Which choice best describes the function of the underlined sentence in the text as a whole?',
            [
                'It explains the mechanical process by which ferry engines generate underwater noise above 110 decibels.',
                'It introduces a methodological limitation that weakens Patel’s conclusion about vocal plasticity.',
                'It compares the acoustic adaptations of toadfish with those of several other Chesapeake Bay species.',
                'It presents empirical evidence that contradicts an established assumption described in the previous sentence.'
            ],
            'D',
            'Câu trước nêu giả định truyền thống ("Conventional models assumed that marine fish simply stop calling"). Câu gạch chân dùng "however" đưa ra dữ liệu thực nghiệm từ mảng hydrophone cho thấy cá không ngừng kêu mà tăng tần số tiếng kêu — trực tiếp bác bỏ giả định cũ.',
            'Với câu hỏi Function of Underlined Sentence, luôn đọc câu LIỀN TRƯỚC và LIỀN SAU để xác định vai trò logic (ở đây: Assumption → however + Empirical Counterevidence).',
            [
                ('Out of Scope', 'Đoạn văn không giải thích cơ chế động cơ phà tạo ra tiếng ồn.'),
                ('Reversed Logic', 'Câu gạch chân củng cố chứ không làm yếu kết luận về vocal plasticity.'),
                ('Out of Scope', 'Câu gạch chân chỉ nói về toadfish, không so sánh với nhiều loài khác.'),
                ('Đáp án đúng', 'Trình bày bằng chứng thực nghiệm (hydrophone arrays captured...) bác bỏ giả định cũ ở câu ngay trước.'),
            ]
        ),
        q_item(
            'd1_1_q3', 3, 'Craft and Structure', 'Cross-Text Connections', 'Elite (750+)',
            '<p><b>Text 1</b><br/>Historian Hannah Sorensen contends that the rapid spread of public lending libraries in industrial Britain was driven primarily by factory owners hoping to cultivate a disciplined, sober workforce. Surviving municipal records frequently cite employers’ donations tied to strict moral reading lists.</p><p><b>Text 2</b><br/>Analyzing nineteenth-century mechanics’ institute ledgers, researcher Devika Rao finds that working-class subscribers routinely bypassed employer-backed libraries to fund independent reading rooms through penny-a-week dues. While philanthropic elites certainly subsidized early buildings, Rao argues that sustained literacy growth stemmed mainly from workers’ self-organized demand for technical and political texts.</p>',
            'Based on the texts, how would Devika Rao (Text 2) most likely respond to Hannah Sorensen’s claim (Text 1)?',
            [
                'By asserting that factory owners never donated money or reading lists to British public libraries.',
                'By agreeing that elite philanthropy played an initial role, while arguing that worker-funded demand was the primary driver of literacy growth.',
                'By demonstrating that working-class subscribers preferred moral novels over technical and political texts.',
                'By concluding that municipal records from industrial Britain were deliberately forged by factory owners.'
            ],
            'B',
            'Text 1 cho rằng giới chủ nhà máy (factory owners) là động lực chính (primarily). Text 2 thừa nhận giới thượng lưu có tài trợ giai đoạn đầu ("While philanthropic elites certainly subsidized early buildings") nhưng nhấn mạnh động lực chính đến từ nhu cầu tự tổ chức của công nhân ("stemmed mainly from workers’ self-organized demand").',
            'Cực kỳ chú ý mệnh đề nhượng bộ "While..." trong Text 2 — đáp án đúng ở Hard Module 2 thường giữ đúng sắc thái "thừa nhận một phần + phản biện trọng tâm", còn bẫy thì dùng từ cực đoan như "never".',
            [
                ('Too Extreme / Contradiction', '"never donated" mâu thuẫn thẳng với câu "While philanthropic elites certainly subsidized early buildings" ở Text 2.'),
                ('Đáp án đúng', 'Phản ánh trọn vẹn cả 2 vế của Rao: thừa nhận vai trò ban đầu của giới tài trợ nhưng khẳng định nhu cầu tự chủ của công nhân mới là động lực chính.'),
                ('Reversed Logic', 'Text 2 nói công nhân tìm đọc "technical and political texts", không phải ưu tiên tiểu thuyết đạo đức.'),
                ('Out of Scope', 'Không có bất kỳ chi tiết nào nói hồ sơ thành phố bị giả mạo (forged).'),
            ]
        ),
        q_item(
            'd1_1_q4', 4, 'Information and Ideas', 'Central Ideas and Details', 'Hard',
            '<p>During the 1970s, textile artist Lenore Tawney moved away from conventional rectangular wall hangings to create monumental woven forms suspended freely in architectural space. Because these gauze-like linen sculptures allowed light and air to pass directly through their open warps, viewers could no longer inspect them from a single fixed vantage point; instead, the pieces shifted visually with every step around the gallery.</p>',
            'Which choice best states the main idea of the text?',
            [
                'Lenore Tawney abandoned linen weaving in the 1970s because galleries lacked sufficient wall space.',
                'Architectural light often damaged Lenore Tawney’s fragile 1970s textiles during public exhibitions.',
                'Conventional rectangular wall hangings were more popular among 1970s viewers than suspended sculptures.',
                'By suspending open-weave linen forms in space, Lenore Tawney transformed weaving into a dynamic, multi-perspective sculptural experience.'
            ],
            'D',
            'Đoạn văn tập trung vào bước chuyển sáng tạo của Tawney (từ tranh treo tường chữ nhật sang các khối dệt mở treo tự do trong không gian), khiến ánh sáng xuyên qua và tác phẩm biến đổi góc nhìn theo từng bước chân người xem.',
            'Đáp án Main Idea chuẩn 1500+ phải ôm trọn cả nguyên nhân/hành động (suspended open-weave forms) lẫn hệ quả nghệ thuật (multi-perspective, shifting visually).',
            [
                ('Contradiction', 'Bà không từ bỏ dệt vải lanh (linen) mà sáng tạo cách trưng bày treo không gian bằng chính vải lanh.'),
                ('Out of Scope', 'Đoạn văn không hề nhắc tới việc ánh sáng làm hư hại tác phẩm.'),
                ('Out of Scope', 'Không có so sánh mức độ phổ biến với công chúng.'),
                ('Đáp án đúng', 'Tóm gọn chính xác cả kỹ thuật (suspending open-weave linen forms) và trải nghiệm thẩm mỹ đa chiều (dynamic, multi-perspective).'),
            ]
        ),
        q_item(
            'd1_1_q5', 5, 'Information and Ideas', 'Command of Evidence (Quantitative)', 'Elite (750+)',
            svg_chart,
            'Which choice best describes data from the graph that weaken the skeptical councilor’s claim?',
            [
                'District A, which has only 10% tree canopy cover, experiences the highest summer surface temperature anomaly at +3.8°C.',
                'Between District B (22% canopy cover) and District A (10% canopy cover), the temperature anomaly rises by 1.2°C.',
                'District D (48% canopy cover) exhibits a summer temperature anomaly of only +0.4°C, substantially lower than the +1.4°C recorded in District C (35% canopy cover).',
                'All four surveyed districts recorded positive summer surface temperature anomalies relative to surrounding rural areas.'
            ],
            'C',
            'Bước 1 — Chốt Claim cần bác bỏ: Nghị sĩ hoài nghi tuyên bố độ phủ cây xanh "không còn tác dụng làm mát đáng kể KHI VƯỢT QUÁ 25%" (exceeds 25%). Bước 2 — Tìm cặp số liệu ĐỀU TRÊN 25%: District C (35%, +1.4°C) → District D (48%, +0.4°C) giảm thêm hẳn 1.0°C! Các đáp án A, B, D tuy đọc đúng biểu đồ nhưng là bẫy "True Data, Wrong Claim" vì không chạm vào ngưỡng >25%.',
            'Bẫy kinh điển nhất câu biểu đồ SAT: Đáp án A, B, D đều ĐÚNG SỐ LIỆU 100%, nhưng chỉ duy nhất C giải quyết đúng điều kiện ">25% coverage" của Claim!',
            [
                ('True Data / Wrong Claim', 'Số liệu District A đúng biểu đồ, nhưng 10% nằm dưới ngưỡng 25% nên không bác bỏ được tuyên bố của nghị sĩ.'),
                ('True Data / Wrong Claim', 'So sánh 10% và 22% đều dưới ngưỡng 25%, hoàn toàn không đụng tới vế "exceeds 25%".'),
                ('Đáp án đúng', 'So sánh trực tiếp 2 khu vực đều trên 25% (35% → 48%) và cho thấy mức tăng nhiệt giảm mạnh từ +1.4°C xuống +0.4°C, bác bỏ hoàn toàn lập luận của nghị sĩ.'),
                ('True Data / Wrong Claim', 'Đúng số liệu nhưng chỉ nói cả 4 khu đều dương, không bác bỏ tuyên bố về ngưỡng >25%.'),
            ]
        ),
        q_item(
            'd1_1_q6', 6, 'Information and Ideas', 'Inferences', 'Elite (750+)',
            '<p>Paleobotanists studying fossilized leaves from the Paleocene-Eocene Thermal Maximum—an abrupt global warming event 56 million years ago—found a sharp spike in insect-feeding damage across mid-latitude forests. Because modern herbivorous insects accelerate their metabolic rates at higher temperatures and must consume more plant tissue to compensate for the lower nutritional density of leaves grown under elevated carbon dioxide, researchers studying these fossils conclude that ______</p>',
            'Which choice most logically completes the text?',
            [
                'ancient mid-latitude trees completely eliminated insect populations by evolving toxic chemical defenses during the warming event.',
                'the surge in fossilized leaf damage was likely driven by warm-climate metabolic demands and reduced leaf nutrition rather than solely by an increase in forest area.',
                'modern herbivorous insects consume significantly less plant tissue than Paleocene insects did under comparable carbon dioxide levels.',
                'carbon dioxide concentrations during the Paleocene-Eocene Thermal Maximum were too low to influence plant growth rates.'
            ],
            'B',
            'Tiền đề 1: Hóa thạch lá thời kỳ ấm lên đột ngột (PETM) có vết côn trùng ăn tăng vọt. Tiền đề 2: Côn trùng ăn cỏ hiện đại tăng tốc trao đổi chất khi nhiệt độ cao và phải ăn nhiều mô lá hơn để bù cho lá kém dinh dưỡng dưới CO2 cao. Kết luận tất yếu: Hiện tượng lá bị ăn tăng vọt trong hóa thạch nhiều khả năng xuất phát từ nhu cầu trao đổi chất do khí hậu ấm và dinh dưỡng lá suy giảm.',
            'Áp dụng 1-Millimeter Rule: Ghép Tiền đề A (hóa thạch PETM) + Tiền đề B (cơ chế nhiệt độ & CO2 hiện đại) → Chọn kết luận khớp thẳng hai cơ chế đó, tránh suy diễn vượt khung.',
            [
                ('Contradiction / Too Extreme', 'Trái ngược hoàn toàn với dữ kiện vết côn trùng cắn tăng vọt (sharp spike) và dùng từ cực đoan "completely eliminated".'),
                ('Đáp án đúng', 'Tổng hợp trực tiếp 2 cơ chế vừa nêu (warm-climate metabolic demands + reduced leaf nutrition) với mức độ thận trọng chuẩn học thuật (likely driven).'),
                ('Out of Scope / Reversed', 'Bài không so sánh côn trùng hiện đại ăn ít hơn côn trùng cổ đại ở cùng mức CO2.'),
                ('Contradiction', 'Đoạn văn gợi ý nồng độ CO2 cao (elevated carbon dioxide), không phải quá thấp.'),
            ]
        ),
        q_item(
            'd1_1_q7', 7, 'Standard English Conventions', 'Boundaries', 'Hard',
            '<p>In 1995, astrophysicists Michel Mayor and Didier Queloz detected 51 Pegasi b, the first confirmed exoplanet orbiting a Sun-like ______ their discovery relied on measuring minuscule wobbles in the host star’s radial velocity rather than imaging the planet directly.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['star,', 'star;', 'star, and because', 'star'],
            'B',
            'Vế trái ("In 1995, astrophysicists... Sun-like star") là 1 IC hoàn chỉnh. Vế phải ("their discovery relied on...") cũng là 1 IC hoàn chỉnh. Giữa 2 IC ta cần dấu chấm phẩy (;) → B. A gây Comma Splice; D gây Run-on; C chèn thừa "because" biến vế 2 thành mệnh đề phụ treo lơ lửng không có mệnh đề chính theo sau.',
            'Đếm nhanh 2 vế tại chỗ trống: IC + IC → chọn dấu chấm phẩy (;) trong 10 giây.',
            [
                ('Comma Splice', 'Chỉ dùng 1 dấu phẩy để nối 2 mệnh đề độc lập là lỗi Comma Splice kinh điển.'),
                ('Đáp án đúng', 'Dấu chấm phẩy (;) nối hợp chuẩn hai mệnh đề độc lập IC + IC.'),
                ('Fragment / Subordinate Trap', 'Thêm "and because" biến toàn bộ vế sau thành mệnh đề phụ (DC) bị treo mà không có IC đi kèm.'),
                ('Run-On Sentence', 'Không có dấu câu hay liên từ giữa 2 IC tạo lỗi câu dính liền (Fused Sentence).'),
            ]
        ),
        q_item(
            'd1_1_q8', 8, 'Standard English Conventions', 'Boundaries', 'Hard',
            '<p>Widely admired for integrating local volcanic stone into modernist concrete structures, Brazilian ______ designed the São Paulo Museum of Art’s iconic suspended glass volume in 1968.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['architect Lina Bo Bardi', 'architect, Lina Bo Bardi,', 'architect Lina Bo Bardi,', 'architect, Lina Bo Bardi'],
            'A',
            'Cấu trúc "Brazilian architect Lina Bo Bardi" thuộc mẫu [Quốc tịch + Nghề nghiệp không có mạo từ a/the] + Tên riêng → Essential (KHÔNG dùng dấu phẩy nào), và đứng ngay trước động từ chính "designed" (cấm đặt dấu phẩy đơn ngăn S–V).',
            'Nhớ quy tắc 1 giây: Không có "a/the" trước nghề nghiệp + tên riêng → 0 dấu phẩy!',
            [
                ('Đáp án đúng', 'Không dấu phẩy giữa chức danh bắt buộc và tên riêng, không ngắt Chủ ngữ khỏi động từ "designed".'),
                ('Non-Essential Trap', 'Đặt cặp phẩy quanh tên riêng chỉ đúng khi trước chức danh có mạo từ xác định duy nhất (VD: "the lead architect, Lina Bo Bardi,").'),
                ('No-Comma Zone (S, V)', 'Đặt 1 dấu phẩy đơn ngay trước động từ chính "designed" tách rời Chủ ngữ khỏi Động từ.'),
                ('Unpaired Comma', 'Đặt 1 dấu phẩy lẻ giữa "architect" và tên riêng làm gãy cụm chủ ngữ.'),
            ]
        ),
        q_item(
            'd1_1_q9', 9, 'Standard English Conventions', 'Form, Structure, and Sense', 'Hard',
            '<p>A comprehensive analysis of more than twelve thousand tidal-gauge records collected across three centuries ______ that regional sea-level rise varies substantially due to local land subsidence and shifting ocean currents.</p>',
            'Which choice completes the text so that it conforms to the conventions of Standard English?',
            ['demonstrate', 'have demonstrated', 'demonstrates', 'demonstrating'],
            'C',
            'Gạch bỏ cụm giới từ chen giữa: "A comprehensive analysis <s>[of more than twelve thousand tidal-gauge records collected across three centuries]</s>". Chủ ngữ thật là "A comprehensive analysis" (SỐ ÍT) và mệnh đề chính chưa có động từ chia thì → Chọn "demonstrates" (C). Mẹo 3–1 cũng xác nhận ngay C là động từ chia thì số ít duy nhất!',
            'Gạch toàn bộ cụm bắt đầu bằng "of..." để lộ chủ ngữ gốc, kiểm tra câu đã có động từ chia thì chưa.',
            [
                ('Subject-Verb Mismatch', 'demonstrate là động từ số nhiều — bị lừa bởi danh từ số nhiều "records/centuries" đứng gần chỗ trống.'),
                ('Subject-Verb Mismatch', 'have demonstrated là thì hiện tại hoàn thành số nhiều — không khớp chủ ngữ số ít "analysis".'),
                ('Đáp án đúng', 'demonstrates là động từ chia thì số ít khớp hoàn hảo với "A comprehensive analysis".'),
                ('Non-Finite Fragment', 'demonstrating là phân từ (V-ing), khiến cả câu thiếu động từ chính (Fragment).'),
            ]
        ),
        q_item(
            'd1_1_q10', 10, 'Expression of Ideas', 'Transitions', 'Hard',
            '<p>For decades, astronomers assumed that the icy moons of the outer solar system were too far from the Sun to maintain liquid water beneath their frozen crusts. ______, flyby measurements from the Cassini spacecraft revealed subsurface oceans kept warm by intense tidal flexing inside Saturn’s moon Enceladus.</p>',
            'Which choice completes the text with the most logical transition?',
            ['Similarly', 'Consequently', 'Nevertheless', 'Furthermore'],
            'C',
            'Câu 1: Trong nhiều thập kỷ giới thiên văn cho rằng các mặt trăng băng quá xa Mặt Trời để có nước lỏng. Câu 2: Dữ liệu tàu Cassini lại phát hiện đại dương ngầm dưới bề mặt Enceladus. Quan hệ giữa 2 câu là ĐỐI LẬP / LẬT NGƯỢC GIẢ ĐỊNH → Chọn "Nevertheless" (Tuy nhiên).',
            'Xác định quan hệ 2 câu (Cùng chiều hay Ngược chiều?) trước khi đọc 4 từ nối; chỉ có duy nhất 1 từ nối thuộc họ Đối lập (Contrast) là thắng ngay.',
            [
                ('Wrong Relationship (Addition)', 'Similarly chỉ sự tương đồng — sai vì câu 2 bác bỏ giả định câu 1.'),
                ('Wrong Relationship (Cause-Effect)', 'Consequently chỉ hệ quả — dữ liệu Cassini không phải kết quả của giả định cũ.'),
                ('Đáp án đúng', 'Nevertheless diễn đạt chính xác sự đối lập/ngược lại kỳ vọng cũ.'),
                ('Wrong Relationship (Addition)', 'Furthermore dùng để bổ sung thêm luận điểm cùng chiều.'),
            ]
        ),
        q_item(
            'd1_1_q11', 11, 'Expression of Ideas', 'Transitions', 'Elite (750+)',
            '<p>In 2018, materials engineers developed a biodegradable packaging film derived from crustacean shells and tree cellulose that blocks oxygen far better than conventional polyethylene. ______, because the raw biopolymers can be harvested from agricultural and seafood waste streams, the film avoids relying on petroleum feedstocks.</p>',
            'Which choice completes the text with the most logical transition?',
            ['Moreover', 'Conversely', 'Instead', 'In other words'],
            'A',
            'Câu 1 nêu ưu điểm 1 của màng sinh học (chặn oxy vượt trội so với nhựa PE). Câu 2 bổ sung thêm ưu điểm 2 độc lập (tận dụng phế phẩm nông-thủy sản, không cần dầu mỏ). Quan hệ là BỔ SUNG THÊM LÝ LẼ CÙNG CHIỀU → "Moreover" (Hơn nữa).',
            'Phân biệt "Moreover" (thêm một ý/ưu điểm MỚI cùng chiều) với "In other words" (chỉ diễn đạt lại cùng 1 ý bằng từ khác).',
            [
                ('Đáp án đúng', 'Moreover bổ sung chính xác ưu điểm thứ hai độc lập (nguồn nguyên liệu không phụ thuộc dầu mỏ).'),
                ('False Contrast', 'Conversely chỉ sự trái ngược — hai câu đều ca ngợi lợi ích của cùng loại màng.'),
                ('False Contrast / Substitution', 'Instead dùng để thay thế một phương án bị phủ định trước đó.'),
                ('Restatement Trap', 'In other words chỉ dùng khi câu sau diễn đạt lại chính ý câu trước (blocking oxygen ≠ avoiding petroleum).'),
            ]
        ),
        q_item(
            'd1_1_q12', 12, 'Expression of Ideas', 'Rhetorical Synthesis', 'Hard',
            '''<p>While researching a topic, a student has taken the following notes:</p>
            <ul>
              <li>The Atacama Large Millimeter/submillimeter Array (ALMA) is a radio telescope observatory located in northern Chile.</li>
              <li>ALMA sits on the Chajnantor Plateau at an elevation of 5,000 meters above sea level.</li>
              <li>Its 66 high-precision antennas operate together as a single interferometer.</li>
              <li>Because water vapor absorbs millimeter-wavelength radio signals, ALMA’s arid, high-altitude location minimizes atmospheric interference.</li>
            </ul>''',
            'The student wants to explain why ALMA’s geographic location is advantageous for its scientific observations. Which choice most effectively uses relevant information from the notes to accomplish this goal?',
            [
                'Located on the Chajnantor Plateau in northern Chile, ALMA operates 66 high-precision antennas together as a single interferometer.',
                'ALMA is an astronomical observatory in northern Chile positioned 5,000 meters above sea level on the Chajnantor Plateau.',
                'Water vapor in Earth’s atmosphere absorbs millimeter-wavelength radio signals, which are studied by observatories using interferometers.',
                'Because ALMA sits in an arid, high-altitude region at 5,000 meters, there is minimal atmospheric water vapor to absorb the millimeter-wavelength signals its antennas detect.'
            ],
            'D',
            'Áp dụng Goal-First SOP: Đọc mục tiêu trước → "explain WHY ALMA’s geographic location is advantageous for its scientific observations" (giải thích VÌ SAO vị trí địa lý có lợi cho việc quan sát). Chỉ có đáp án D kết nối trực tiếp vị trí khô cằn trên cao (arid, high-altitude) với lợi ích khoa học (ít hơi nước hấp thụ sóng millimeter).',
            'Trong Rhetorical Synthesis, 3 đáp án sai thường vẫn chép ĐÚNG 100% thông tin từ bullet notes nhưng KHÔNG thực hiện đúng động từ mục tiêu (explain why advantageous).',
            [
                ('Wrong Synthesis Goal', 'Chỉ liệt kê vị trí và số ăng-ten, không hề giải thích vì sao vị trí đó có lợi.'),
                ('Wrong Synthesis Goal', 'Chỉ mô tả độ cao địa lý mà bỏ qua lý do khoa học về hơi nước và sóng radio.'),
                ('Too General / Missing Subject', 'Nêu hiện tượng vật lý chung chung mà không nhắc đến lợi thế vị trí của ALMA.'),
                ('Đáp án đúng', 'Kết nối nhân-quả hoàn hảo giữa vị trí khô cằn ở độ cao 5.000m và lợi ích giảm nhiễu khí quyển.'),
            ]
        ),
    ]

    return {
        'schemaVersion': 1,
        'mode': 'drill',
        'section': 'Reading and Writing',
        'basicInfo': {
            'title': 'Drill 1.1: Digital SAT 1500+ Diagnostic & Trap Identification (12 Qs)',
            'subtitle': 'Đánh giá nhanh 4 Content Domains & luyện phản xạ phát hiện 5 mẫu bẫy kinh điển của College Board trên giao diện Bluebook.',
            'difficultyBadge': 'Diagnostic • Target 1500+',
            'targetTimeMinutes': 15,
        },
        'drillModule': {
            'id': 'drill_1_1_mod',
            'title': 'Skill Drill 1.1: 1500+ Diagnostic & Trap Mastery',
            'timeLimitMinutes': 15,
            'questions': questions,
        },
    }


def get_drill_2_1():
    stem = 'Which choice completes the text so that it conforms to the conventions of Standard English?'
    questions = [
        q_item(
            'd2_1_q1', 1, 'Standard English Conventions', 'Boundaries', 'Medium',
            '<p>Early cartographers struggled to determine longitude accurately at ______ without a reliable marine chronometer, navigators frequently miscalculated their east-west position by hundreds of miles.</p>',
            stem,
            ['sea,', 'sea;', 'sea, because', 'sea'],
            'B',
            'Vế trái ("Early cartographers struggled... at sea") là 1 IC hoàn chỉnh. Vế phải ("without a reliable marine chronometer, navigators frequently miscalculated...") cũng là 1 IC hoàn chỉnh → Cần dấu chấm phẩy (;) nối 2 IC.',
            'Cụm mở đầu "without a reliable marine chronometer," chỉ là cụm giới từ bổ nghĩa cho IC phía sau — đừng nhầm nó thành mệnh đề phụ!',
            [
                ('Comma Splice', 'Nối 2 IC chỉ bằng 1 dấu phẩy là lỗi Comma Splice.'),
                ('Đáp án đúng', 'Dấu chấm phẩy (;) ngăn cách đúng chuẩn hai mệnh đề độc lập IC + IC.'),
                ('Comma + Subordinate Trap', 'Thêm "because" trước "without...," tạo cấu trúc lặp/gãy: "because without X, navigators..." khiến mệnh đề phụ không ăn khớp ngữ pháp chuẩn.'),
                ('Run-On Sentence', 'Thiếu dấu câu giữa hai mệnh đề độc lập.'),
            ]
        ),
        q_item(
            'd2_1_q2', 2, 'Standard English Conventions', 'Boundaries', 'Medium',
            '<p>The restoration team uncovered three distinct pigment layers beneath the nineteenth-century ______ lead white, Prussian blue, and a rare mineral green imported from Saxony.</p>',
            stem,
            ['varnish:', 'varnish, including:', 'varnish; which were', 'varnish'],
            'A',
            'Vế trước là 1 IC hoàn chỉnh ("The restoration team uncovered three distinct pigment layers beneath the nineteenth-century varnish"). Vế sau liệt kê giải thích 3 lớp màu đó → Dấu hai chấm (:) là chuẩn tuyệt đối.',
            'Trước dấu hai chấm (:) phải là 1 IC hoàn chỉnh; tuyệt đối không đặt dấu (:) sau "including" hay "such as".',
            [
                ('Đáp án đúng', 'IC hoàn chỉnh + dấu hai chấm (:) mở ra danh sách giải thích 3 lớp màu.'),
                ('Colon After Preposition Trap', 'Cấm đặt dấu hai chấm trực tiếp sau "including".'),
                ('Semicolon + Fragment Trap', 'Sau dấu chấm phẩy (;) phải là IC, nhưng "which were..." là mệnh đề quan hệ (DC), tạo Fragment.'),
                ('Missing Punctuation', 'Thiếu dấu câu dẫn nhập danh sách, gây dính liền cấu trúc câu.'),
            ]
        ),
        q_item(
            'd2_1_q3', 3, 'Standard English Conventions', 'Boundaries', 'Hard',
            '<p>Although synthetic fertilizers dramatically increased twentieth-century grain yields across temperate ______ prolonged nitrogen runoff simultaneously depleted dissolved oxygen in coastal estuaries.</p>',
            stem,
            ['regions;', 'regions.', 'regions,', 'regions:'],
            'C',
            'Đầu câu có liên từ phụ thuộc "Although" → toàn bộ vế trước chỗ trống là 1 Dependent Clause (DC)! Phía sau là Independent Clause (IC). Công thức bắt buộc cho DC đứng trước IC là: DC , IC → Chọn C. Ngoài ra dùng Equivalence Shortcut: A (;) và B (.) đều tách 2 IC → gạch cả A, B, D trong 3 giây!',
            'Nhìn thấy "Although/While/Because/Since" ở đầu câu → vế trái là DC → TUYỆT ĐỐI loại dấu chấm (.), chấm phẩy (;), và hai chấm (:)!',
            [
                ('Semicolon After DC', 'Dấu chấm phẩy yêu cầu vế trước là IC; "Although..." là DC nên tạo Fragment.'),
                ('Period After DC', 'Dấu chấm cắt cụt mệnh đề "Although..." thành câu thiếu mệnh đề chính (Fragment).'),
                ('Đáp án đúng', 'Dấu phẩy đơn chuẩn xác nối Dependent Clause (Although...) với Independent Clause phía sau.'),
                ('Colon After DC', 'Dấu hai chấm bắt buộc vế trước phải là IC hoàn chỉnh.'),
            ]
        ),
        q_item(
            'd2_1_q4', 4, 'Standard English Conventions', 'Boundaries', 'Hard',
            '<p>In her comparative study of urban transit systems, economist Maya Okafor examined light-rail networks in Zurich, ______ Portland, Oregon; and Curitiba, Brazil.</p>',
            stem,
            ['Switzerland,', 'Switzerland:', 'Switzerland—', 'Switzerland;'],
            'D',
            'Đây là cấu trúc Super-Semicolon! Danh sách gồm 3 cặp "Thành phố, Quốc gia/Bang" đã chứa dấu phẩy bên trong từng mục, và mục thứ hai kết thúc bằng dấu chấm phẩy ("Portland, Oregon;"). Để đồng bộ danh sách phức hợp, sau "Switzerland" bắt buộc dùng dấu chấm phẩy (;).',
            'Thấy dấu chấm phẩy (;) xuất hiện trong một chuỗi liệt kê địa danh/tên người kèm chức danh → lập tức khớp song song bằng Super-Semicolon!',
            [
                ('List Delimiter Mismatch', 'Dùng phẩy thường sẽ lẫn lộn giữa phẩy nội bộ ("Zurich, Switzerland") và phẩy ngăn mục, lệch với dấu ";" sau Oregon.'),
                ('Wrong Punctuation', 'Dấu hai chấm không dùng để ngăn các mục ngang hàng trong danh sách.'),
                ('Wrong Punctuation', 'Gạch ngang đơn không khớp cấu trúc song song với dấu chấm phẩy sau Oregon.'),
                ('Đáp án đúng', 'Super-Semicolon ngăn cách rành mạch 3 cụm địa danh đã có sẵn dấu phẩy bên trong.'),
            ]
        ),
        q_item(
            'd2_1_q5', 5, 'Standard English Conventions', 'Boundaries', 'Hard',
            '<p>Quantum sensors cooled to near absolute zero can detect gravitational shifts caused by subterranean ______ researchers envision deploying portable arrays to map aquifers without drilling.</p>',
            stem,
            ['water, consequently,', 'water; consequently,', 'water consequently,', 'water, and consequently,'],
            'B',
            'Vế trái là IC ("Quantum sensors... subterranean water"). Vế phải là IC ("researchers envision..."). Từ "consequently" là trạng từ liên kết (conjunctive adverb), KHÔNG phải FANBOYS → Phải dùng dấu chấm phẩy trước và phẩy sau: "; consequently,".',
            'Học thuộc nhóm conjunctive adverbs (however, therefore, consequently, moreover, nevertheless, thus): nối 2 IC luôn đi với "; word," hoặc ". Word,".',
            [
                ('Comma Splice', 'Đặt phẩy trước "consequently" khi nối 2 IC là lỗi Comma Splice kinh điển của Digital SAT.'),
                ('Đáp án đúng', 'Chấm phẩy chấm dứt IC 1, theo sau bởi trạng từ liên kết "consequently," mở đầu IC 2.'),
                ('Run-On Sentence', 'Không có dấu ngắt câu giữa hai IC.'),
                ('Redundant Comma', 'Khi dùng ", and consequently", đặt thêm dấu phẩy ngay sau "consequently" làm ngắt mạch vụng (chuẩn SAT ưu tiên ngắn gọn rõ ràng "; consequently,").'),
            ]
        ),
        q_item(
            'd2_1_q6', 6, 'Standard English Conventions', 'Boundaries', 'Hard',
            '<p>Archaeobotanists recovered charred barley grains from a Neolithic hearth in southern Jordan ______ confirmed through radiocarbon dating that the settlement predated nearby irrigated villages by four centuries.</p>',
            stem,
            ['and', ', and', '; and', '. And'],
            'A',
            'Kiểm tra chủ ngữ vế sau: "...confirmed through radiocarbon dating..." KHÔNG CÓ CHỦ NGỮ mới (dùng chung chủ ngữ "Archaeobotanists" với động từ 1 "recovered"!). Đây là Compound Predicate (S + V1 and V2), KHÔNG phải IC + IC → KHÔNG được đặt dấu phẩy trước "and"!',
            'Cực kỳ cảnh giác bẫy ", and": Chỉ đặt dấu phẩy trước FANBOYS khi vế SAU có chủ ngữ riêng tạo thành IC đầy đủ!',
            [
                ('Đáp án đúng', 'Nối hai động từ cùng chủ ngữ ("recovered ... and confirmed") KHÔNG dùng dấu phẩy.'),
                ('Unnecessary Comma Before FANBOYS', 'Vế sau "confirmed..." thiếu chủ ngữ (không phải IC), nên đặt dấu phẩy trước "and" là sai chuẩn SAT.'),
                ('Semicolon + Fragment Trap', 'Không dùng dấu chấm phẩy trước FANBOYS nối động từ ghép.'),
                ('Fragment Trap', 'Tách thành câu mới "And confirmed..." thiếu chủ ngữ, tạo Sentence Fragment.'),
            ]
        ),
        q_item(
            'd2_1_q7', 7, 'Standard English Conventions', 'Boundaries', 'Hard',
            '<p>Bioluminescent dinoflagellates emit brief flashes of blue light when agitated by breaking ______ researchers believe these sudden bursts startle predatory copepods and attract larger fish that feed on the predators.</p>',
            stem,
            ['waves, yet', 'waves,', 'waves; because', 'waves—'],
            'D',
            'Vế 1 là IC hoàn chỉnh; vế 2 là IC giải thích cơ chế/ý nghĩa của hiện tượng ở vế 1. Dấu gạch ngang đơn (—) hoạt động như dấu hai chấm đơn (IC — IC giải thích), hoàn toàn hợp chuẩn! A sai nghĩa ("yet" là đối lập); B là Comma Splice; C tạo Fragment sau chấm phẩy vì có "because".',
            'Nhớ 2 chức năng của Em-Dash (—): Cặp gạch ngang (— ... —) dùng như cặp phẩy; Gạch ngang đơn (IC — giải thích) dùng như dấu hai chấm!',
            [
                ('False Contrast (FANBOYS)', 'Về dấu câu ", yet" hợp lệ giữa 2 IC, nhưng nghĩa "yet" (tuy nhiên/nhưng) sai hoàn toàn vì vế sau giải thích lý do chứ không đối lập.'),
                ('Comma Splice', 'Chỉ có 1 dấu phẩy nối hai IC.'),
                ('Semicolon + DC Fragment', 'Sau dấu chấm phẩy mà bắt đầu bằng "because" sẽ chỉ còn 1 mệnh đề phụ (Fragment).'),
                ('Đáp án đúng', 'Gạch ngang đơn sau IC hoàn chỉnh dẫn ra lời giải thích mục đích sinh học của ánh sáng phát quang.'),
            ]
        ),
        q_item(
            'd2_1_q8', 8, 'Standard English Conventions', 'Boundaries', 'Elite (750+)',
            '<p>While examining sediment cores from Lake Turkana, geochemist Dr. Lillian Osei identified a sudden spike in volcanic ash ______ the exact chemical signature of an eruption documented in Ethiopian highland deposits dated to 1.9 million years ago.</p>',
            stem,
            ['matching', '; matching', '. Matching', ', it matched'],
            'A',
            'Vế trước ("Dr. Lillian Osei identified a sudden spike in volcanic ash") là IC hoàn chỉnh. Vế sau bắt đầu bằng phân từ ("matching the exact chemical signature...") không có chủ ngữ và không có động từ chia thì — nó là một cụm phân từ bổ nghĩa trực tiếp cho "volcanic ash" → nối liền không cần dấu chấm/chấm phẩy (A). D gây Comma Splice!',
            'Kiểm tra nhanh từ đầu vế sau: "matching" là V-ing (Phrase, KHÔNG phải IC) → loại ngay chấm (.) và chấm phẩy (;).',
            [
                ('Đáp án đúng', 'Cụm phân từ rút gọn "matching..." bổ nghĩa trực tiếp cho "volcanic ash" (essential modifier).'),
                ('Semicolon + Fragment', 'Sau dấu chấm phẩy phải là IC, nhưng "matching..." là cụm phân từ (Fragment).'),
                ('Period + Fragment', 'Dấu chấm tách cụm phân từ thành câu khuyết động từ chính.'),
                ('Comma Splice', 'Đưa chủ ngữ+động từ "it matched" vào sau dấu phẩy tạo lỗi 2 IC nối bằng dấu phẩy.'),
            ]
        ),
        q_item(
            'd2_1_q9', 9, 'Standard English Conventions', 'Boundaries', 'Elite (750+)',
            '<p>Architects restoring Kyoto’s centuries-old machiya townhouses face a delicate balancing ______ preserving breathable cedar-and-plaster walls while upgrading insulation to meet modern seismic and energy standards.</p>',
            stem,
            ['act:', 'act;', 'act.', 'act, for example,'],
            'A',
            'Vế trái ("Architects... face a delicate balancing act") là 1 IC hoàn chỉnh. Vế phải ("preserving breathable cedar-and-plaster walls while upgrading...") là 1 cụm danh động từ (Gerund Phrase, KHÔNG phải IC!) giải thích rõ "balancing act" là gì → Chỉ duy nhất dấu hai chấm (:) nối được `IC : Phrase`! Loại B & C ngay vì sau `;` và `.` bắt buộc là IC.',
            'Khi vế sau chỉ là Cụm từ giải thích (không có chủ ngữ + động từ chia thì) sau 1 IC hoàn chỉnh → Dấu hai chấm (:) hoặc gạch ngang đơn (—) là đáp án duy nhất!',
            [
                ('Đáp án đúng', 'IC hoàn chỉnh + dấu hai chấm (:) giới thiệu cụm từ giải thích cho "a delicate balancing act".'),
                ('Semicolon + Fragment', 'Vế sau "preserving..." là cụm V-ing, không phải IC nên cấm dùng dấu chấm phẩy.'),
                ('Period + Fragment', 'Vế sau không có động từ chia thì, tách câu sẽ tạo Fragment.'),
                ('Comma + Phrase Trap', 'Đặt ", for example," khiến cụm phía sau trôi nổi rời rạc và thừa chữ so với định nghĩa trực tiếp "balancing act".'),
            ]
        ),
        q_item(
            'd2_1_q10', 10, 'Standard English Conventions', 'Boundaries', 'Hard',
            '<p>Because desert tortoises spend up to ninety-five percent of their lives inside subterranean burrows that buffer extreme surface ______ field biologists often rely on radio-telemetry transmitters to track seasonal movement patterns.</p>',
            stem,
            ['temperatures;', 'temperatures,', 'temperatures.', 'temperatures—and'],
            'B',
            'Toàn bộ phần đầu câu bắt đầu bằng "Because desert tortoises spend..." kéo dài tận "extreme surface temperatures" là 1 Dependent Clause (DC) rất dài (có chứa thêm mệnh đề quan hệ "that buffer..."). Phía sau ("field biologists often rely...") là IC → Công thức DC , IC → Chọn B.',
            'Đừng để mệnh đề quan hệ chen bên trong đánh lừa độ dài: miễn đầu câu có "Because" mà chưa có IC thì toàn bộ vế trái vẫn chỉ là DC!',
            [
                ('Semicolon After DC', 'Vế trái bắt đầu bằng "Because" nên là DC, không thể kết thúc bằng dấu chấm phẩy.'),
                ('Đáp án đúng', 'Dấu phẩy đơn ngăn cách chuẩn xác mệnh đề phụ "Because..." với mệnh đề chính phía sau.'),
                ('Period After DC', 'Dấu chấm cắt câu "Because..." thành Fragment.'),
                ('Redundant Conjunction', 'Đã có "Because" ở vế 1 thì CẤM dùng thêm "and/so/but" để nối sang vế 2.'),
            ]
        ),
        q_item(
            'd2_1_q11', 11, 'Standard English Conventions', 'Boundaries', 'Elite (750+)',
            '<p>The manuscript’s provenance remained disputed for over a ______ then, in 2023, multispectral imaging revealed a faded watermark linked exclusively to a seventeenth-century Antwerp paper mill.</p>',
            stem,
            ['century,', 'century;', 'century', 'century, and,'],
            'B',
            'Vế 1 là IC ("The manuscript’s provenance remained disputed for over a century"). Vế 2 là IC ("then, in 2023, multispectral imaging revealed..."). Lưu ý: "then" là trạng từ (KHÔNG PHẢI FANBOYS!), nên nối 2 IC trước "then" bắt buộc dùng dấu chấm (.) hoặc chấm phẩy (;) → Chọn B!',
            'Bẫy siêu hay lừa: "then" KHÔNG nằm trong nhóm FANBOYS (For, And, Nor, But, Or, Yet, So)! Nối 2 IC với "then" mà chỉ dùng dấu phẩy là Comma Splice!',
            [
                ('Comma Splice (Then Trap)', '"then" là trạng từ, không phải FANBOYS — nối 2 IC bằng ", then" là lỗi Comma Splice.'),
                ('Đáp án đúng', 'Dấu chấm phẩy (;) nối 2 IC hoàn chỉnh trước trạng từ "then".'),
                ('Run-On Sentence', 'Thiếu hoàn toàn dấu câu ngăn 2 IC.'),
                ('Punctuation Clutter', 'Tạo chuỗi ", and, then, in 2023," dư dấu phẩy sai quy chuẩn.'),
            ]
        ),
        q_item(
            'd2_1_q12', 12, 'Standard English Conventions', 'Boundaries', 'Hard',
            '<p>Soil microbiologists have found that mycorrhizal fungi exchange scarce phosphorus for plant-synthesized ______ this mutualistic trade network allows seedlings shaded by tall canopies to survive prolonged low-light periods.</p>',
            stem,
            ['sugars,', 'sugars; and', 'sugars:', 'sugars'],
            'C',
            'Vế 1 là IC ("Soil microbiologists have found that... sugars"). Vế 2 là IC giải thích hệ quả/ý nghĩa của mạng lưới trao đổi đó ("this mutualistic trade network allows..."). Dùng dấu hai chấm (:) nối `IC : IC (giải thích)` hoàn toàn chuẩn xác! Loại A (Comma Splice), B (cấm `; and` nối 2 IC đơn giản trong chuẩn SAT), D (Run-on).',
            'Dấu hai chấm (:) hoàn toàn có thể đứng giữa 2 IC đầy đủ miễn vế sau giải thích, làm rõ hoặc mở rộng trực tiếp cho vế trước.',
            [
                ('Comma Splice', 'Dấu phẩy đơn không đủ sức nối 2 IC.'),
                ('Illegal Semicolon + FANBOYS', 'Trong chuẩn Standard English của Digital SAT, không ghép dấu chấm phẩy trước liên từ "and" nối hai mệnh đề thông thường.'),
                ('Đáp án đúng', 'Dấu hai chấm (:) nối 2 IC có quan hệ giải thích/mở rộng trực tiếp.'),
                ('Run-On Sentence', 'Thiếu dấu câu giữa hai mệnh đề độc lập.'),
            ]
        ),
        q_item(
            'd2_1_q13', 13, 'Standard English Conventions', 'Boundaries', 'Elite (750+)',
            '<p>Among the museum’s most fragile holdings are three nineteenth-century daguerreotypes requiring specialized climate ______ a portrait of abolitionist Frederick Douglass, dated 1848; a panoramic view of San Francisco Harbor, taken in 1851; and an early lunar photograph, captured through the Harvard Observatory refractor.</p>',
            stem,
            ['control;', 'control:', 'control,', 'control—which are'],
            'B',
            'Vế trước là 1 IC đảo ngữ hoàn chỉnh ("Among the museum’s most fragile holdings are three nineteenth-century daguerreotypes requiring specialized climate control"). Vế sau liệt kê 3 bức ảnh (dùng Super-Semicolon ngăn cách bên trong). Để MỞ ĐẦU một danh sách giải thích sau IC hoàn chỉnh, ta PHẢI dùng dấu hai chấm (:) chứ không dùng chấm phẩy!',
            'Phân biệt vai trò hai dấu: Dấu hai chấm (:) MỞ ĐẦU danh sách sau IC; còn Super-Semicolon (;) NGĂN CÁCH các mục bên trong danh sách đó!',
            [
                ('Semicolon Before List Trap', 'Dấu chấm phẩy không dùng để giới thiệu một danh sách cụm danh từ (không phải IC).'),
                ('Đáp án đúng', 'IC hoàn chỉnh + dấu hai chấm (:) giới thiệu chính xác danh sách 3 hiện vật (mà bản thân chúng dùng Super-Semicolon ngăn cách).'),
                ('Weak Delimiter / Ambiguity', 'Dấu phẩy không phù hợp để dẫn nhập danh sách dài sử dụng Super-Semicolon và dễ gây nhầm đồng vị ngữ.'),
                ('Wordy / Unmatched Clause', 'Dùng gạch ngang đơn kèm "which are" phá vỡ cấu trúc liệt kê song song chuẩn mực.'),
            ]
        ),
        q_item(
            'd2_1_q14', 14, 'Standard English Conventions', 'Boundaries', 'Hard',
            '<p>Although acoustic engineers initially predicted that the concert hall’s curved timber ceiling would scatter high-frequency notes ______ post-construction measurements showed remarkably even sound distribution across every balcony tier.</p>',
            stem,
            ['unevenly, however,', 'unevenly; however,', 'unevenly.', 'unevenly,'],
            'D',
            'Bẫy đôi kinh điển (Double Contrast Trap)! Đầu câu đã có "Although" (tạo DC đối lập), nên nếu thêm "however" ở giữa sẽ bị dư thừa từ đối lập. Đồng thời vì vế trái là DC, cấm dùng chấm (.) hay chấm phẩy (;) → Chọn duy nhất D ("unevenly,").',
            'Quy tắc 1 từ đối lập duy nhất: Đã có "Although / Though / While" ở đầu câu → TUYỆT ĐỐI KHÔNG dùng thêm "but / yet / however" ở giữa câu!',
            [
                ('Double Contrast Trap', 'Dùng cả "Although" lẫn "however" trong cùng một câu là lỗi lặp liên từ đối lập.'),
                ('Semicolon After DC + Double Contrast', 'Vừa sai dấu chấm phẩy sau DC vừa dư "however" sau "Although".'),
                ('Period After DC', 'Cắt cụt mệnh đề "Although..." thành Fragment.'),
                ('Đáp án đúng', 'Dấu phẩy đơn chuẩn xác nối mệnh đề phụ "Although..." với mệnh đề chính phía sau.'),
            ]
        ),
        q_item(
            'd2_1_q15', 15, 'Standard English Conventions', 'Boundaries', 'Elite (750+)',
            '<p>Geologist Dr. Hannah Lindqvist noticed that basalt columns at Giant’s Causeway fracture into predominantly hexagonal ______ cooling lava contracts evenly around regularly spaced stress centers, minimizing the total energy required to split the rock.</p>',
            stem,
            ['prisms, because', 'prisms; because', 'prisms because', 'prisms. Because'],
            'C',
            'Vế 1 là IC ("Geologist Dr. Hannah Lindqvist noticed that... prisms"). Vế 2 là mệnh đề phụ chỉ nguyên nhân mở đầu bằng "because" ("because cooling lava contracts..."). Theo chuẩn Standard English trên Digital SAT, khi mệnh đề phụ "because..." đứng SAU mệnh đề chính (IC + DC thiết yếu giải thích nguyên nhân) → KHÔNG đặt dấu phẩy, chấm, hay chấm phẩy trước "because"!',
            'DC đứng TRƯỚC IC → CÓ dấu phẩy (DC, IC). DC thiết yếu ("because/when/if") đứng SAU IC → KHÔNG dấu câu (IC because DC)!',
            [
                ('Unnecessary Comma Before Because', 'Thông thường không đặt dấu phẩy trước mệnh đề "because" thiết yếu giải thích trực tiếp nguyên nhân.'),
                ('Semicolon + DC Fragment', 'Sau dấu chấm phẩy là mệnh đề "because..." không có IC đi kèm → Fragment.'),
                ('Đáp án đúng', 'Nối liền mạch IC + mệnh đề phụ nguyên nhân "because..." không thừa dấu câu.'),
                ('Period + DC Fragment', 'Biến "Because cooling lava contracts..." thành 1 câu đứng riêng thiếu mệnh đề chính (Fragment).'),
            ]
        ),
    ]

    return {
        'schemaVersion': 1,
        'mode': 'drill',
        'section': 'Reading and Writing',
        'basicInfo': {
            'title': 'Drill 2.1: Boundaries I — Clauses, Linking & Core Punctuation (15 Qs)',
            'subtitle': 'Luyện phản xạ ≤20 giây/câu với Period, Semicolon, Colon, Em-Dash, FANBOYS và Super-Semicolon ở độ khó Medium → Elite 750+.',
            'difficultyBadge': 'SEC • Target 1500+',
            'targetTimeMinutes': 12,
        },
        'drillModule': {
            'id': 'drill_2_1_mod',
            'title': 'Skill Drill 2.1: Boundaries I (Clauses & Core Punctuation)',
            'timeLimitMinutes': 12,
            'questions': questions,
        },
    }
