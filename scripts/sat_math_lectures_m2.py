# -*- coding: utf-8 -*-
"""
Digital SAT Math 1500+ — Module 2 Lectures (Advanced Math — Hard M2 Core):
- m2_1: Quadratics Mastery (Discriminant, Vertex Form & Vieta Formulas)
- m2_2: Polynomials, Factor Theorem, Rational Equations & Extraneous Roots
- m2_3: Exponential Growth/Decay, Compound Percentages & Time-Step Scaling
- m2_4: Nonlinear Systems, Radicals, Absolute Value & Function Transformations
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from sat_audio_pipeline import build_sat_lecture_html, make_quick_check_html

DESMOS_BOX_STYLE = 'background:#ecfdf5; border-left:4px solid #059669; padding:14px 16px; border-radius:10px; margin:12px 0; font-size:14.5px; color:#064e3b;'

def get_m2_lectures():
    lectures = []

    # =========================================================================
    # LECTURE M2.1: Quadratics Mastery
    # =========================================================================
    m2_1_cards = f'''
  <div id="sec-threeforms" class="sat-card lecture-interactive-card" data-lecture-section="threeforms">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>1. Ba dạng Parabol &amp; Câu hỏi kinh điển "Displays as a constant or coefficient"</h2>
    <p>Hàm bậc hai (Quadratics) là chuyên đề xuất hiện dày đặc nhất trong <b>Advanced Math</b>. Mỗi dạng viết của parabol làm lộ diện một đặc trưng đồ thị ngay lập tức:</p>
    <table class="sat-table">
      <thead><tr><th>Dạng Parabol</th><th>Công thức</th><th>Hằng số lộ diện trực tiếp</th></tr></thead>
      <tbody>
        <tr><td><b>Standard Form</b></td><td><code>y = ax² + bx + c</code></td><td><b>y-intercept = (0, c)</b> • Trục đối xứng <code>x = −b / (2a)</code></td></tr>
        <tr><td><b>Vertex Form</b></td><td><code>y = a(x − h)² + k</code></td><td><b>Đỉnh (Vertex) = (h, k)</b> • Min (nếu a &gt; 0) hoặc Max (nếu a &lt; 0) là <code>k</code> tại <code>x = h</code></td></tr>
        <tr><td><b>Factored Form</b></td><td><code>y = a(x − r)(x − s)</code></td><td><b>Hai x-intercepts = (r, 0) và (s, 0)</b> • Hoành độ đỉnh <code>h = (r + s) / 2</code></td></tr>
      </tbody>
    </table>
    <div class="sat-rule-box">
      <b>📌 Tính đối xứng Parabol (Symmetry Shortcut):</b> Nếu đề cho <code>f(3) = f(11)</code> (hai điểm có cùng tung độ!), hoành độ đỉnh lập tức là trung điểm: <code>h = (3 + 11) / 2 = 7</code>! Cực kỳ hay xuất hiện trong câu 750–800!
    </div>
  </div>

  <div id="sec-discriminant" class="sat-card lecture-interactive-card" data-lecture-section="discriminant">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>2. Biệt thức Discriminant (Δ = b² − 4ac) — Vũ khí số 1 cho câu Tham số k</h2>
    <p>Với phương trình bậc hai đã đưa về vế phải bằng 0: <code>ax² + bx + c = 0</code>:</p>
    <div class="sat-gold-box">
      <b>⭐ Bảng tra Biệt thức Δ = b² − 4ac:</b>
      <br>• <b>Δ &gt; 0</b> → <b>2 nghiệm thực phân biệt</b> (cắt trục Ox tại 2 điểm).
      <br>• <b>Δ = 0</b> → <b>Đúng 1 nghiệm thực (nghiệm kép)</b> (tiếp xúc trục Ox tại đỉnh).
      <br>• <b>Δ &lt; 0</b> → <b>Vô nghiệm thực (0 real solutions)</b> (không cắt trục Ox).
    </div>
    <div class="sat-trap-box">
      <b>🚨 2 Cái bẫy khiến 60% thí sinh mất điểm câu Δ:</b>
      <br>1. <b>Quên chuyển toàn bộ về một vế bằng 0</b> trước khi đọc <code>a, b, c</code> (ví dụ <code>2x² + kx = −8</code> phải chuyển thành <code>2x² + kx + 8 = 0</code> nên <code>c = +8</code>, không phải <code>−8</code>!).
      <br>2. <b>Câu hỏi "largest integer value of c" khi vô nghiệm:</b> Nếu giải ra <code>c &gt; 9/4 = 2.25</code> → số nguyên <b>nhỏ nhất</b> là <code>3</code>; nếu giải ra <code>c &lt; 12.25</code> → số nguyên <b>lớn nhất</b> là <code>12</code>!
    </div>
  </div>

  <div id="sec-vieta" class="sat-card lecture-interactive-card" data-lecture-section="vieta">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>3. Định lý Vieta (Sum &amp; Product of Solutions) — Ăn trọn câu 780–800 trong 5 giây</h2>
    <p>Mỗi khi đề hỏi <b>"What is the sum of the solutions..."</b> hoặc <b>"What is the product of the solutions..."</b> của phương trình <code>ax² + bx + c = 0</code> (có nghiệm thực <code>Δ ≥ 0</code>):</p>
    <div class="sat-gold-box">
      <b>⭐ Công thức Vieta Bắt buộc thuộc lòng:</b>
      <br>• <b>Tổng 2 nghiệm:</b> <code>r₁ + r₂ = −b / a</code>
      <br>• <b>Tích 2 nghiệm:</b> <code>r₁ · r₂ = c / a</code>
      <br><i>Chú ý:</i> Nếu đề chỉ hỏi <b>tổng các nghiệm PHÂN BIỆT (sum of distinct solutions)</b> và phương trình có nghiệm kép <code>(x − 5)² = 0</code>, tổng các nghiệm phân biệt chỉ là <code>5</code> (KHÔNG phải <code>5 + 5 = 10</code>)!
    </div>
    <div style="{DESMOS_BOX_STYLE}">
      <b>⚡ Desmos Check:</b> Gõ phương trình <code>y = ax² + bx + c</code> vào Desmos (thêm slider nếu có hằng số <code>k</code>). Click thẳng vào 2 giao điểm trục Ox để cộng/nhân kiểm chứng hoặc kéo slider sao cho đỉnh parabol vừa chạm trục Ox (<code>Δ = 0</code>)!
    </div>
  </div>
'''
    m2_1_qc = make_quick_check_html(
        'qc_m2_1',
        'Phương trình bậc hai 3x² − 18x + k = 0 có đúng một nghiệm thực (exactly one real solution). Giá trị của k là bao nhiêu?',
        'In the equation <b>3x² − 18x + k = 0</b>, where <i>k</i> is a constant, the equation has <b>exactly one real solution</b>. What is the value of <i>k</i>?',
        ['9', '18', '27', '81'],
        2,
        'Để có đúng 1 nghiệm thực thì Δ = b² − 4ac = 0 → (−18)² − 4(3)(k) = 0 → 324 − 12k = 0 → k = 324 / 12 = 27. Mẹo nhanh: rút 3 ra ngoài thành 3(x² − 6x + k/3) = 0 → để là bình phương đủ (x − 3)² thì k/3 = 9 → k = 27!'
    )
    m2_1_html = build_sat_lecture_html(
        'DIGITAL SAT MATH 1500+ • MODULE 2 • ADVANCED MATH',
        '2.1 Quadratics Mastery: Discriminant, Vertex Form & Vieta',
        'Làm chủ trọn bộ vũ khí hàm bậc hai: 3 dạng Parabol, tính đối xứng, biệt thức Δ = b² − 4ac và định lý Vieta xử lý câu 780–800 trong 5 giây.',
        [
            'Phân biệt chính xác thông số hiển thị trực tiếp của Standard, Vertex và Factored Form.',
            'Dùng biệt thức Δ = b² − 4ac giải quyết triệt để mọi câu tham số 0/1/2 nghiệm thực trong Module 2 Hard.',
            'Áp dụng định lý Vieta (−b/a, c/a) và tránh bẫy "distinct solutions" khi có nghiệm kép.',
        ],
        m2_1_cards,
        m2_1_qc
    )
    m2_1_segs = [
        {
            'id': 'intro',
            'title': 'Tổng quan Quadratics 800',
            'selector': '#sec-header',
            'en': 'Quadratics are the single highest-yield topic in SAT Advanced Math. Almost every Hard Module Two contains at least three quadratic questions testing vertex form, the discriminant, and Vieta formulas. Master these three tools and you turn the hardest questions into five-second wins.',
            'vi': 'Phương trình và hàm bậc hai là chuyên đề mang lại nhiều điểm nhất trong phần Advanced Math. Hầu như mọi đề Module 2 Hard đều có ít nhất 3 câu bậc hai kiểm tra dạng đỉnh, biệt thức delta và định lý Vieta. Nắm chắc ba công cụ này sẽ biến những câu khó nhất thành điểm số trong 5 giây.'
        },
        {
            'id': 'threeforms',
            'title': '3 dạng Parabol & Tính đối xứng',
            'selector': '#sec-threeforms',
            'en': 'Know what each quadratic form reveals as a constant. Standard form reveals the y-intercept c. Vertex form reveals the minimum or maximum value k at x equals h. Factored form reveals the x-intercepts r and s. Also remember symmetry: if two different inputs give the same output, like f of three equals f of eleven, the vertex x-coordinate is simply their average, seven.',
            'vi': 'Hãy thuộc chính xác mỗi dạng parabol làm lộ thông số nào: dạng chuẩn cho biết ngay tung độ gốc c; dạng đỉnh cho thấy giá trị cực đại hoặc cực tiểu k tại x bằng h; dạng tích cho biết ngay hai hoành độ giao điểm trục Ox. Đừng quên mẹo đối xứng: nếu f tại 3 bằng f tại 11 thì hoành độ đỉnh chính là trung bình cộng của 3 và 11, tức bằng 7.'
        },
        {
            'id': 'discriminant',
            'title': 'Biệt thức Δ = b² − 4ac & 2 Cái bẫy',
            'selector': '#sec-discriminant',
            'en': 'Whenever a quadratic question mentions two real solutions, exactly one real solution, or no real solutions, immediately think of the discriminant: b squared minus four a c. Positive means two solutions, zero means one, and negative means none. Always move every term to one side equal to zero first so you never misread the sign of c.',
            'vi': 'Hễ thấy câu hỏi bậc hai nhắc tới hai nghiệm thực, đúng một nghiệm thực hoặc vô nghiệm thực, hãy nghĩ ngay lập tức tới biệt thức delta bằng b bình phương trừ bốn a c. Dương là 2 nghiệm, bằng 0 là 1 nghiệm kép, âm là vô nghiệm. Nhớ luôn chuyển hết mọi số hạng sang một vế bằng 0 trước khi lấy dấu của hệ số c.'
        },
        {
            'id': 'vieta',
            'title': 'Định lý Vieta (−b/a, c/a)',
            'selector': '#sec-vieta',
            'en': 'Never waste time using the quadratic formula when a question asks for the sum or product of solutions. By Vieta formulas, the sum of solutions is negative b over a, and the product of solutions is c over a. Just verify that real solutions actually exist, and watch carefully for the phrase distinct solutions in case of a double root.',
            'vi': 'Tuyệt đối đừng mất công bấm nghiệm lẻ khi đề hỏi tổng hoặc tích các nghiệm. Theo Vieta, tổng hai nghiệm bằng trừ b trên a, còn tích hai nghiệm bằng c trên a. Chỉ cần kiểm tra có nghiệm thực và đọc kỹ xem đề có từ distinct solutions hay không để tránh cộng trùng nghiệm kép.'
        }
    ]
    lectures.append({
        'code': 'm2_1',
        'module_key': 'math_m2',
        'order_index': 1,
        'title': '2.1 Quadratics Mastery: Discriminant, Vertex Form & Vieta',
        'drill_key': 'drill_m2_1',
        'html': m2_1_html,
        'segments': m2_1_segs,
        'major_sections': [
            {'title': '3 dạng Parabol & Tính đối xứng', 'startSegmentId': 'threeforms'},
            {'title': 'Biệt thức Δ = b² − 4ac', 'startSegmentId': 'discriminant'},
            {'title': 'Định lý Vieta', 'startSegmentId': 'vieta'},
        ],
    })

    # =========================================================================
    # LECTURE M2.2: Polynomials, Factor Theorem & Rational Equations
    # =========================================================================
    m2_2_cards = f'''
  <div id="sec-factor" class="sat-card lecture-interactive-card" data-lecture-section="factor">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>1. Định lý Nhân tử (Factor Theorem) &amp; Số dư (Remainder Theorem)</h2>
    <p>Trong Digital SAT, bạn hiếm khi phải chia đa thức dài dòng — 95% câu hỏi đa thức được giải bằng đúng 2 mệnh đề tương đương sau:</p>
    <div class="sat-gold-box">
      <b>⭐ Định lý Nhân tử &amp; Số dư:</b>
      <br>• <code>(x − a)</code> là một nhân tử (factor) của đa thức <code>p(x)</code> <b>⇔</b> <code>p(a) = 0</code> (đồ thị cắt trục Ox tại <code>x = a</code>).
      <br>• Tổng quát: Khi chia <code>p(x)</code> cho <code>(x − a)</code>, <b>số dư (remainder)</b> đúng bằng <b><code>p(a)</code></b>!
      <br>• <b>Cảnh giác dấu:</b> Nếu đề cho nhân tử <code>(x + 4)</code> thì giá trị cần thay là <code>x = −4</code> (tức <code>p(−4) = 0</code>), KHÔNG phải <code>+4</code>!
    </div>
    <div class="sat-rule-box">
      <b>📌 Bội nghiệm (Multiplicity) trên đồ thị đa thức:</b>
      <br>• Nghiệm bậc <b>lẻ</b> như <code>(x − r)¹</code> hoặc <code>(x − r)³</code> → đồ thị <b>cắt xuyên qua (crosses)</b> trục Ox tại <code>r</code>.
      <br>• Nghiệm bậc <b>chẵn</b> như <code>(x − r)²</code> → đồ thị <b>chạm rồi bật lại (touches/bounces)</b> tại trục Ox ở <code>r</code>.
    </div>
  </div>

  <div id="sec-matching" class="sat-card lecture-interactive-card" data-lecture-section="matching">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>2. Đồng nhất hệ số (Coefficient Matching) &amp; Hằng đẳng thức 800</h2>
    <p>Khi đề cho hai biểu thức đa thức bằng nhau với mọi giá trị của <code>x</code> (ví dụ <code>(ax + 3)(bx − 5) = 12x² + cx − 15</code> và <code>a + b = 7</code>):</p>
    <div class="sat-ex-box">
      <b>Chiến thuật 3 bước Đồng nhất hệ số:</b>
      <br>1. Khai triển vế trái: <code>abx² + (3b − 5a)x − 15</code>.
      <br>2. So sánh từng bậc của <code>x</code>: <code>ab = 12</code> và <code>c = 3b − 5a</code>.
      <br>3. Kết hợp điều kiện phụ <code>a + b = 7</code> → cặp <code>(a, b)</code> là <code>(3, 4)</code> hoặc <code>(4, 3)</code> → ra hai giá trị khả dĩ của <code>c</code> là <code>3(4)−5(3) = −3</code> hoặc <code>3(3)−5(4) = −11</code>!
    </div>
    <div class="sat-rule-box">
      <b>3 Hằng đẳng thức xuất hiện liên tục:</b>
      <br>• Hiệu hai bình phương: <code>a² − b² = (a − b)(a + b)</code> (cả dạng ẩn bậc 4 như <code>x⁴ − 16 = (x² − 4)(x² + 4)</code>).
      <br>• Bình phương tổng/hiệu: <code>(a ± b)² = a² ± 2ab + b²</code> (KHÔNG bao giờ quên số hạng <code>±2ab</code> ở giữa!).
    </div>
  </div>

  <div id="sec-rational" class="sat-card lecture-interactive-card" data-lecture-section="rational">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>3. Phương trình Phân thức (Rational Equations) &amp; Nghiệm ngoại lai (Extraneous Roots)</h2>
    <p>Phương trình chứa ẩn ở mẫu (ví dụ <code>2 / (x − 3) + 5 / (x + 2) = ...</code>) có 2 nguyên tắc sống còn:</p>
    <div class="sat-trap-box">
      <b>🚨 Bẫy Nghiệm ngoại lai (Extraneous Solution):</b> Sau khi quy đồng khử mẫu và giải ra nghiệm <code>x</code>, <b>BẮT BUỘC kiểm tra mẫu số ban đầu khác 0</b>! Bất kỳ nghiệm nào làm mẫu số bằng 0 đều phải <b>LOẠI NGAY</b>.
    </div>
    <div style="{DESMOS_BOX_STYLE}">
      <b>⚡ Desmos Hack cho Rational Expressions:</b>
      <br>• Với câu rút gọn phân thức <i>"Which expression is equivalent to ... for x &gt; 3?"</i>: Gõ biểu thức gốc thành <code>y = ...</code> rồi gõ lần lượt các đáp án A, B, C, D — đáp án nào vẽ đường cong <b>trùng khít 100%</b> là đáp án đúng! (Hoặc thế nhanh <code>x = 5</code> vào biểu thức gốc và 4 đáp án!).
      <br>• Với phương trình phân thức: gõ vế trái <code>y = LHS</code> và vế phải <code>y = RHS</code> → Desmos tự động KHÔNG vẽ giao điểm tại các nghiệm ngoại lai làm mẫu bằng 0!
    </div>
  </div>
'''
    m2_2_qc = make_quick_check_html(
        'qc_m2_2',
        'Đa thức p(x) = x³ − 4x² + kx + 12 chia hết cho (x − 3). Giá trị của hằng số k là bao nhiêu?',
        'The polynomial <b>p(x) = x³ − 4x² + kx + 12</b> is divisible by <b>(x − 3)</b>. What is the value of the constant <i>k</i>?',
        ['−5', '−1', '1', '5'],
        1,
        'Theo Định lý Nhân tử, p(x) chia hết cho (x − 3) khi và chỉ khi p(3) = 0. Thay x = 3: 3³ − 4(3²) + 3k + 12 = 27 − 36 + 3k + 12 = 3 + 3k = 0 → k = −1!'
    )
    m2_2_html = build_sat_lecture_html(
        'DIGITAL SAT MATH 1500+ • MODULE 2 • ADVANCED MATH',
        '2.2 Polynomials, Factor Theorem & Rational Equations',
        'Chinh phục Định lý Nhân tử/Số dư, kỹ thuật đồng nhất hệ số đa thức và xử lý triệt để phương trình phân thức có nghiệm ngoại lai.',
        [
            'Giải câu chia đa thức và tìm tham số trong 5 giây bằng Định lý Nhân tử p(a) = 0.',
            'Đọc chuẩn bội nghiệm (chạm vs cắt xuyên) từ đồ thị đa thức bậc 3, bậc 4.',
            'Khử mẫu phương trình phân thức an toàn, loại bỏ 100% nghiệm ngoại lai và dùng Desmos kiểm tra biểu thức tương đương.',
        ],
        m2_2_cards,
        m2_2_qc
    )
    m2_2_segs = [
        {
            'id': 'intro',
            'title': 'Tổng quan Đa thức & Phân thức',
            'selector': '#sec-header',
            'en': 'Polynomials and rational equations look intimidating because of long algebraic expressions, yet the SAT tests a remarkably clean set of structural ideas: the Factor Theorem, matching coefficients, and checking for extraneous roots.',
            'vi': 'Đa thức và phương trình phân thức trông có vẻ cồng kềnh với nhiều biểu thức dài, nhưng thực chất SAT chỉ xoay quanh ba ý tưởng cấu trúc rất gọn: Định lý nhân tử, đồng nhất hệ số và kiểm tra nghiệm ngoại lai.'
        },
        {
            'id': 'factor',
            'title': 'Định lý Nhân tử & Bội nghiệm',
            'selector': '#sec-factor',
            'en': 'The Factor Theorem states that x minus a is a factor of polynomial p of x if and only if p of a equals zero. More generally, the remainder when dividing p of x by x minus a is simply p of a. On graphs, odd-multiplicity roots cross the x-axis, while even-multiplicity roots touch and bounce off the x-axis.',
            'vi': 'Định lý nhân tử khẳng định x trừ a là nhân tử của đa thức p x khi và chỉ khi p tại a bằng 0. Tổng quát hơn, số dư khi chia p x cho x trừ a chính bằng p tại a. Trên đồ thị, nghiệm bội lẻ sẽ cắt xuyên qua trục hoành, còn nghiệm bội chẵn sẽ chạm trục hoành rồi bật ngược lại.'
        },
        {
            'id': 'matching',
            'title': 'Đồng nhất hệ số & Hằng đẳng thức',
            'selector': '#sec-matching',
            'en': 'When two polynomial expressions are stated to be equivalent for all values of x, expand both sides and match the coefficients of x squared, x, and the constant term separately. Also stay alert for disguised differences of squares like x to the fourth minus sixteen.',
            'vi': 'Khi hai đa thức bằng nhau với mọi x, hãy khai triển rồi đồng nhất từng hệ số của x bình, x và hằng số tự do. Đừng quên nhận diện nhanh hiệu hai bình phương ngụy trang ở bậc cao như x mũ bốn trừ mười sáu.'
        },
        {
            'id': 'rational',
            'title': 'Phương trình phân thức & Nghiệm ngoại lai',
            'selector': '#sec-rational',
            'en': 'After clearing denominators in a rational equation, always plug your candidate solutions back into the original denominators. Any value that makes a denominator equal to zero is an extraneous root and must be rejected. In Desmos, graphing both sides automatically avoids extraneous intersections.',
            'vi': 'Sau khi quy đồng khử mẫu trong phương trình phân thức, bắt buộc phải thế nghiệm ngược lại kiểm tra mẫu số ban đầu. Bất kỳ giá trị nào làm mẫu bằng không đều là nghiệm ngoại lai và phải loại bỏ. Mẹo nhanh trên Desmos là vẽ cả hai vế để thấy đúng các giao điểm hợp lệ.'
        }
    ]
    lectures.append({
        'code': 'm2_2',
        'module_key': 'math_m2',
        'order_index': 2,
        'title': '2.2 Polynomials, Factor Theorem & Rational Equations',
        'drill_key': 'drill_m2_2',
        'html': m2_2_html,
        'segments': m2_2_segs,
        'major_sections': [
            {'title': 'Định lý Nhân tử & Số dư', 'startSegmentId': 'factor'},
            {'title': 'Đồng nhất hệ số', 'startSegmentId': 'matching'},
            {'title': 'Phân thức & Nghiệm ngoại lai', 'startSegmentId': 'rational'},
        ],
    })

    # =========================================================================
    # LECTURE M2.3: Exponential Growth/Decay & Time-Step Scaling
    # =========================================================================
    m2_3_cards = f'''
  <div id="sec-exp-core" class="sat-card lecture-interactive-card" data-lecture-section="exp_core">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>1. Cấu trúc Hàm mũ <code>f(t) = a · b^(t / k)</code> &amp; Phân biệt Tuyến tính vs Hàm mũ</h2>
    <p>Trong mô hình thực tế của Digital SAT, hãy phân biệt rạch ròi 2 loại tăng trưởng ngay trong 3 giây đọc đề:</p>
    <table class="sat-table">
      <thead><tr><th>Đặc điểm</th><th>Linear (Bậc nhất)</th><th>Exponential (Hàm mũ)</th></tr></thead>
      <tbody>
        <tr><td><b>Từ khóa nhận diện</b></td><td>increases/decreases <b>by a constant amount</b> (VD: +50 mỗi năm)</td><td>increases/decreases <b>by a constant percent / factor</b> (VD: +8% mỗi năm, doubles, halves)</td></tr>
        <tr><td><b>Công thức chuẩn</b></td><td><code>y = mx + b</code></td><td><code>y = a · (1 ± r)^(t / k)</code></td></tr>
        <tr><td><b>Ý nghĩa các tham số</b></td><td><code>b</code> = ban đầu, <code>m</code> = bước cộng</td><td><code>a</code> = giá trị tại <code>t = 0</code>, <code>1 + r</code> = hệ số tăng, <code>1 − r</code> = hệ số giảm, <code>k</code> = chu kỳ</td></tr>
      </tbody>
    </table>
    <div class="sat-trap-box">
      <b>🚨 Bẫy số 1 (Percent vs Base):</b> Nếu một chất phóng xạ <b>giảm đi 18%</b> mỗi giờ, cơ số (growth/decay factor) là <code>1 − 0.18 = 0.82</code>, TUYỆT ĐỐI KHÔNG phải <code>0.18</code>! Ngược lại, nếu thấy <code>y = 500(0.65)^t</code>, tốc độ giảm là <code>1 − 0.65 = 35%</code> (KHÔNG phải 65%!).
    </div>
  </div>

  <div id="sec-timestep" class="sat-card lecture-interactive-card" data-lecture-section="timestep">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>2. Bẫy Chu kỳ số mũ (Time-Step Exponent Scaling — Hard M2)</h2>
    <p>Câu hỏi 750–800 cực kỳ ưa chuộng đổi đơn vị thời gian ngay trên số mũ (từ năm sang tháng, từ ngày sang tuần, hoặc "mỗi 4 năm tăng gấp đôi"):</p>
    <div class="sat-gold-box">
      <b>⭐ Quy tắc kiểm tra số mũ bằng phép thử 1 chu kỳ (Plug-in 1 Cycle Test):</b>
      <br>• <b>"Tăng gấp đôi mỗi 6 năm"</b> (với <code>t</code> tính bằng năm): Khi <code>t = 6</code>, số mũ phải bằng <code>1</code> → công thức là <code>a · 2^(t / 6)</code> (KHÔNG phải <code>2^(6t)</code>!).
      <br>• <b>"Tăng 3% mỗi quý (quarter)"</b> (với <code>t</code> tính bằng năm): Trong <code>t = 1</code> năm có <b>4 quý</b> → số mũ phải bằng <code>4</code> → công thức là <code>a · (1.03)^(4t)</code>!
      <br>• <b>Chuyển đổi cơ số tương đương:</b> <code>(1.03)^(4t) = ((1.03)⁴)^t ≈ (1.1255)^t</code> → tương đương tăng <b>12.55% mỗi năm</b> (KHÔNG phải <code>4 × 3% = 12%</code>!).
    </div>
  </div>

  <div id="sec-yint-trap" class="sat-card lecture-interactive-card" data-lecture-section="yint_trap">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>3. Bẫy "y-Intercept as a Constant" &amp; Tiệm cận ngang (Horizontal Asymptote)</h2>
    <p>Rất nhiều học sinh giỏi bị mất điểm ở câu Hard M2 dạng: <i>"Which equivalent form displays the y-intercept of f(x) as a constant or coefficient?"</i></p>
    <div class="sat-ex-box">
      <b>Ví dụ Hard M2:</b> Cho <code>f(x) = 12 · (2)^(x + 3)</code>. Đừng vội kết luận y-intercept là 12!
      <br>Tính tại <code>x = 0</code>: <code>f(0) = 12 · 2³ = 12 · 8 = 96</code>!
      <br>Viết lại dạng chuẩn để làm lộ y-intercept: <code>f(x) = 12 · 2³ · 2^x = 96 · (2)^x</code>!
    </div>
    <div class="sat-rule-box">
      <b>📌 Tiệm cận ngang (Asymptote) của hàm dịch chuyển <code>f(x) = a · b^x + c</code>:</b>
      <br>• Đường tiệm cận ngang là <b><code>y = c</code></b>.
      <br>• Tung độ gốc là <b><code>f(0) = a + c</code></b> (KHÔNG phải <code>a</code>!).
      <br>• Ví dụ: <code>y = 5(0.5)^x + 4</code> có tiệm cận ngang <code>y = 4</code> và đi qua điểm <code>(0, 9)</code>!
    </div>
    <div style="{DESMOS_BOX_STYLE}">
      <b>⚡ Desmos Regression cho Hàm mũ:</b> Khi đề cho bảng các điểm hàm mũ, nhập Table rồi gõ <code>y₁ ~ a · b^(x₁)</code> (bật Log Mode nếu có nhiều điểm) → Desmos trả về ngay <code>a</code> và <code>b</code>!
    </div>
  </div>
'''
    m2_3_qc = make_quick_check_html(
        'qc_m2_3',
        'Hàm số f(x) = 5 · (3)^(x − 2) được viết lại dưới dạng tương đương nào để hiển thị trực tiếp tung độ gốc (y-intercept) dưới dạng một hằng số hoặc hệ số?',
        'Which equivalent form of <b>f(x) = 5 · 3^(x − 2)</b> displays the <b>y-intercept</b> of the graph of y = f(x) as a constant or coefficient?',
        ['f(x) = 45 · 3^x', 'f(x) = (5/9) · 3^x', 'f(x) = 5 · (1/9)^x', 'f(x) = (5/6) · 3^x'],
        1,
        'Áp dụng quy tắc lũy thừa: 3^(x − 2) = 3^x · 3^(−2) = (1/9) · 3^x. Nhân với 5 ta được f(x) = (5/9) · 3^x. Thử x = 0: f(0) = 5 · 3^(−2) = 5/9 — lộ rõ ngay hệ số 5/9!'
    )
    m2_3_html = build_sat_lecture_html(
        'DIGITAL SAT MATH 1500+ • MODULE 2 • ADVANCED MATH',
        '2.3 Exponential Growth/Decay & Compound Scaling',
        'Xử lý sắc bén mọi bẫy cơ số phần trăm (1 − r), chia/nhân chu kỳ trên số mũ t/k và dạng chuẩn lộ diện y-intercept của hàm mũ.',
        [
            'Phân biệt tức thì mô hình tuyến tính (cộng đều) với mô hình hàm mũ (nhân/phần trăm đều).',
            'Đặt đúng số mũ t/k hay kt bằng phép thử 1 chu kỳ (Plug-in 1 Cycle Test) không bao giờ đảo ngược phân số.',
            'Tách hệ số lũy thừa a · b^(x ± c) để đọc đúng y-intercept và tiệm cận ngang y = c.',
        ],
        m2_3_cards,
        m2_3_qc
    )
    m2_3_segs = [
        {
            'id': 'intro',
            'title': 'Tổng quan Hàm mũ & Tăng trưởng kép',
            'selector': '#sec-header',
            'en': 'Exponential functions appear in nearly every SAT Math module. While the formula a times b to the x looks simple, Hard Module Two disguises y-intercepts inside shifted exponents and swaps time units between months, quarters, and years.',
            'vi': 'Hàm số mũ xuất hiện trong hầu như mọi đề SAT Math. Công thức a nhân b mũ x tưởng rất đơn giản, nhưng ở Module 2 Hard đề luôn giấu tung độ gốc bên trong số mũ bị dịch chuyển và đổi đơn vị thời gian giữa tháng, quý và năm.'
        },
        {
            'id': 'exp_core',
            'title': 'Cơ số tăng/giảm phần trăm (1 ± r)',
            'selector': '#sec-exp-core',
            'en': 'Always separate linear change, which adds a constant amount, from exponential change, which multiplies by a constant factor. If a quantity decreases by eighteen percent each hour, the decay factor is one minus zero point one eight, which is zero point eight two, never zero point one eight.',
            'vi': 'Hãy luôn phân biệt thay đổi tuyến tính là cộng thêm một lượng cố định, còn hàm mũ là nhân với một tỉ lệ cố định. Nếu một đại lượng giảm 18 phần trăm mỗi giờ, cơ số phải là 1 trừ 0 phẩy 18 bằng 0 phẩy 82, tuyệt đối không lấy 0 phẩy 18.'
        },
        {
            'id': 'timestep',
            'title': 'Bẫy chu kỳ số mũ t/k và kt',
            'selector': '#sec-timestep',
            'en': 'To avoid flipping the exponent fraction, run the One-Cycle Test. If a population doubles every six years and t is in years, plugging in t equals six must make the exponent equal to one, so the exponent must be t divided by six. Conversely, if interest compounds quarterly four times a year, plugging in t equals one year must give four periods, so the exponent is four t.',
            'vi': 'Để không bao giờ chia nhầm hay nhân nhầm số mũ, hãy dùng phép thử 1 chu kỳ. Nếu quần thể tăng gấp đôi sau mỗi 6 năm và t tính bằng năm, thay t bằng 6 phải làm số mũ bằng 1, nên số mũ là t chia 6. Ngược lại, nếu lãi gộp theo quý 4 lần mỗi năm, thay t bằng 1 phải ra 4 kỳ, nên số mũ là 4t.'
        },
        {
            'id': 'yint_trap',
            'title': 'Bẫy y-intercept khi số mũ lệch & Tiệm cận',
            'selector': '#sec-yint-trap',
            'en': 'Watch out for shifted exponents like five times three to the power of x minus two. The y-intercept is not five—plugging in x equals zero gives five times three to the negative two, or five ninths. Rewrite the expression as five ninths times three to the x so the true y-intercept appears directly as a coefficient. And if there is a vertical shift plus c, the horizontal asymptote is y equals c and the y-intercept is a plus c.',
            'vi': 'Cực kỳ cảnh giác dạng số mũ lệch như 5 nhân 3 mũ x trừ 2. Tung độ gốc không phải là 5, vì khi thay x bằng 0 ta ra 5 nhân 3 mũ trừ 2 bằng 5 phần 9. Hãy tách thành 5 phần 9 nhân 3 mũ x để làm lộ tung độ gốc. Ngoài ra nếu hàm có cộng thêm hằng số c phía sau, tiệm cận ngang là y bằng c và tung độ gốc là a cộng c.'
        }
    ]
    lectures.append({
        'code': 'm2_3',
        'module_key': 'math_m2',
        'order_index': 3,
        'title': '2.3 Exponential Growth/Decay & Compound Scaling',
        'drill_key': 'drill_m2_3',
        'html': m2_3_html,
        'segments': m2_3_segs,
        'major_sections': [
            {'title': 'Linear vs Exponential & Cơ số (1 ± r)', 'startSegmentId': 'exp_core'},
            {'title': 'Bẫy chu kỳ số mũ t/k', 'startSegmentId': 'timestep'},
            {'title': 'Bẫy y-intercept & Tiệm cận', 'startSegmentId': 'yint_trap'},
        ],
    })

    # =========================================================================
    # LECTURE M2.4: Nonlinear Systems, Radicals, Abs Value & Transformations
    # =========================================================================
    m2_4_cards = f'''
  <div id="sec-nonlin" class="sat-card lecture-interactive-card" data-lecture-section="nonlin">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>1. Hệ Phương trình Phi tuyến (Line + Parabola / Circle)</h2>
    <p>Hệ gồm một đường thẳng <code>y = mx + b</code> và một parabol <code>y = ax² + px + q</code> là "đặc sản" của câu Q16–Q22 trong Module 2 Hard:</p>
    <div class="sat-rule-box">
      <b>Phương pháp đại số chuẩn:</b> Cho hai vế <code>y</code> bằng nhau → rút gọn về phương trình bậc hai <code>Ax² + Bx + C = 0</code> rồi áp dụng <b>Discriminant Δ = B² − 4AC</b>:
      <br>• Cắt tại <b>2 điểm</b> ⇔ <code>Δ &gt; 0</code>
      <br>• Tiếp xúc tại <b>đúng 1 điểm (tangent)</b> ⇔ <code>Δ = 0</code>
      <br>• <b>Không giao nhau (no solution)</b> ⇔ <code>Δ &lt; 0</code>
    </div>
    <div style="{DESMOS_BOX_STYLE}">
      <b>⚡ Desmos Slider Shortcut:</b> Gõ thẳng đường thẳng và parabol (kèm tham số <code>c</code> hoặc <code>k</code>) vào Desmos → kéo slider cho đến khi đường thẳng vừa chạm đúng 1 điểm vào parabol để xác nhận ngay giá trị chính xác của tham số!
    </div>
  </div>

  <div id="sec-rad-abs" class="sat-card lecture-interactive-card" data-lecture-section="rad_abs">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>2. Phương trình Căn thức (Radicals), Lũy thừa hữu tỉ &amp; Giá trị tuyệt đối</h2>
    <table class="sat-table">
      <thead><tr><th>Dạng bài</th><th>Quy tắc cốt lõi</th><th>Bẫy 750+ cần tránh</th></tr></thead>
      <tbody>
        <tr><td><b>Căn thức</b><br><code>√(ax + b) = cx + d</code></td><td>Cô lập căn một vế, bình phương 2 vế, giải bậc hai.</td><td><b>BẮT BUỘC thử lại nghiệm!</b> Vì <code>√(...) ≥ 0</code>, bất kỳ nghiệm nào làm vế phải <code>cx + d &lt; 0</code> là <b>nghiệm ngoại lai (LOẠI)</b>!</td></tr>
        <tr><td><b>Lũy thừa hữu tỉ</b><br><code>x^(m/n)</code></td><td><code>x^(m/n) = ⁿ√(x^m)</code> • <code>x^(−k) = 1 / x^k</code></td><td>Mũ <b>tử là bậc lũy thừa</b>, mũ <b>mẫu là bậc căn</b> ("Flower Power": Power on top, Root on bottom!).</td></tr>
        <tr><td><b>Giá trị tuyệt đối</b><br><code>|ax + b| = c</code></td><td>• <code>c &gt; 0</code>: 2 nghiệm (<code>ax+b = c</code> hoặc <code>−c</code>)<br>• <code>c = 0</code>: 1 nghiệm<br>• <code>c &lt; 0</code>: <b>Vô nghiệm!</b></td><td>Cô lập <code>|...|</code> trước khi xét dấu <code>c</code>! Ví dụ <code>|x − 3| + 7 = 2</code> → <code>|x − 3| = −5</code> → <b>0 nghiệm</b>!</td></tr>
      </tbody>
    </table>
    <div class="sat-gold-box">
      <b>⭐ Phím tắt Tổng 2 nghiệm của <code>|ax + b| = c</code> (với c &gt; 0):</b> Vì hai nghiệm luôn đối xứng quanh tâm <code>x₀ = −b / a</code>, <b>tổng 2 nghiệm luôn bằng <code>−2b / a</code></b> (hoàn toàn KHÔNG phụ thuộc vào <code>c</code> miễn là <code>c &gt; 0</code>)!
    </div>
  </div>

  <div id="sec-transform" class="sat-card lecture-interactive-card" data-lecture-section="transform">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>3. Phép biến đổi Hàm số <code>f(x − h) + k</code> &amp; Cô lập biến (Isolating Variables)</h2>
    <div class="sat-rule-box">
      <b>📌 Quy tắc "Trong NGOẶC đi NGƯỢC — Ngoài NGOẶC đi XUÔI":</b>
      <br>• <code>f(x) + k</code>: Dịch <b>LÊN</b> k đơn vị • <code>f(x) − k</code>: Dịch <b>XUỐNG</b> k đơn vị.
      <br>• <code>f(x − h)</code>: Dịch sang <b>PHẢI</b> h đơn vị (nghiệm <code>x</code> CỘNG thêm <code>h</code>!).
      <br>• <code>f(x + h)</code>: Dịch sang <b>TRÁI</b> h đơn vị (nghiệm <code>x</code> TRỪ đi <code>h</code>!).
      <br>• <code>−f(x)</code>: Đối xứng qua <b>trục Ox</b> • <code>f(−x)</code>: Đối xứng qua <b>trục Oy</b>.
    </div>
    <div class="sat-ex-box">
      <b>Ví dụ Hard M2:</b> Đồ thị <code>y = f(x)</code> có điểm cực tiểu tại <code>(4, −6)</code>. Tìm tọa độ điểm cực tiểu của <code>g(x) = f(x + 3) + 10</code>.
      <br><b>Giải trong 3 giây:</b> Trong ngoặc là <code>x + 3</code> → dịch <b>trái 3</b> (<code>x_mới = 4 − 3 = 1</code>). Ngoài ngoặc là <code>+10</code> → dịch <b>lên 10</b> (<code>y_mới = −6 + 10 = 4</code>). Đỉnh mới là <b><code>(1, 4)</code></b>!
    </div>
  </div>
'''
    m2_4_qc = make_quick_check_html(
        'qc_m2_4',
        'Tìm tất cả các nghiệm thực của phương trình √(2x + 15) = x + 6.',
        'What is the solution set of the equation <b>√(2x + 15) = x + 6</b>?',
        ['x = −3 và x = −7', 'Chỉ x = −3', 'Chỉ x = −7', 'Vô nghiệm'],
        1,
        'Bình phương hai vế: 2x + 15 = x² + 12x + 36 → x² + 10x + 21 = 0 → (x + 3)(x + 7) = 0 → x = −3 hoặc x = −7. BẮT BUỘC thử lại vế phải (x + 6 ≥ 0): với x = −3 thì −3 + 6 = 3 ≥ 0 (nhận, √9 = 3); với x = −7 thì −7 + 6 = −1 < 0 (LOẠI vì căn bậc hai không thể âm!). Vậy chỉ có x = −3.'
    )
    m2_4_html = build_sat_lecture_html(
        'DIGITAL SAT MATH 1500+ • MODULE 2 • ADVANCED MATH',
        '2.4 Nonlinear Systems, Radicals, Absolute Value & Transformations',
        'Khóa chặt 4 chủ đề chuyên phân loại 750–800 của Advanced Math: Hệ đường thẳng–parabol, nghiệm ngoại lai căn thức, giá trị tuyệt đối và biến đổi đồ thị hàm số.',
        [
            'Giải hệ đường thẳng – parabol tiếp xúc bằng phương pháp thế kết hợp Δ = 0 và kiểm chứng Desmos.',
            'Loại bỏ 100% bẫy nghiệm ngoại lai ở phương trình căn thức và bẫy vô nghiệm của giá trị tuyệt đối.',
            'Áp dụng quy tắc "Trong ngoặc ngược, ngoài ngoặc xuôi" cho mọi bài toán dịch chuyển đỉnh/nghiệm của hàm f(x).',
        ],
        m2_4_cards,
        m2_4_qc
    )
    m2_4_segs = [
        {
            'id': 'intro',
            'title': 'Tổng quan Hệ phi tuyến, Căn thức & Biến đổi hàm',
            'selector': '#sec-header',
            'en': 'This final lesson of Advanced Math targets the exact topics that separate a 720 from a perfect 800: line-parabola tangent systems, extraneous radical roots, absolute value traps, and function transformations.',
            'vi': 'Bài học cuối của Module Advanced Math nhắm thẳng vào bốn chuyên đề phân tách mốc 720 với điểm tuyệt đối 800: hệ tiếp xúc đường thẳng parabol, nghiệm ngoại lai căn thức, bẫy giá trị tuyệt đối và phép biến đổi đồ thị hàm số.'
        },
        {
            'id': 'nonlin',
            'title': 'Hệ đường thẳng & Parabol tiếp xúc',
            'selector': '#sec-nonlin',
            'en': 'When a system pairs a line with a parabola, set the two y expressions equal and move everything to one side to form a single quadratic. If the system has exactly one solution, the line is tangent to the parabola and the discriminant must equal zero. You can always verify the exact tangent point visually in Desmos.',
            'vi': 'Khi hệ gồm một đường thẳng và một parabol, hãy cho hai vế y bằng nhau rồi chuyển hết sang một vế thành phương trình bậc hai. Nếu hệ có đúng một nghiệm, đường thẳng tiếp xúc parabol và biệt thức delta phải bằng không. Bạn luôn có thể kiểm chứng ngay điểm tiếp xúc trên Desmos.'
        },
        {
            'id': 'rad_abs',
            'title': 'Căn thức, Lũy thừa hữu tỉ & Giá trị tuyệt đối',
            'selector': '#sec-rad-abs',
            'en': 'For radical equations, squaring both sides can create fake extraneous roots. Always check that the non-radical side is zero or positive. For fractional exponents, remember Power on top, Root on bottom. For absolute value equations, isolate the bars first: if the bars equal a negative number, there is immediately no solution.',
            'vi': 'Với phương trình căn thức, bình phương hai vế có thể sinh ra nghiệm ngoại lai, vì vậy luôn phải thử lại để chắc chắn vế không chứa căn không âm. Với lũy thừa phân số, tử số là số mũ còn mẫu số là bậc căn. Với giá trị tuyệt đối, luôn cô lập dấu trị tuyệt đối trước: nếu bằng một số âm thì kết luận ngay vô nghiệm.'
        },
        {
            'id': 'transform',
            'title': 'Phép biến đổi hàm f(x − h) + k',
            'selector': '#sec-transform',
            'en': 'For function transformations, remember inside is opposite and outside is direct. Adding k outside shifts the graph up k units. Replacing x with x minus h inside shifts the graph right by h units, while x plus h shifts it left by h units.',
            'vi': 'Với phép tịnh tiến đồ thị, hãy nhớ câu thần chú trong ngoặc đi ngược, ngoài ngoặc đi xuôi. Cộng k bên ngoài sẽ đẩy đồ thị lên trên k đơn vị. Còn bên trong ngoặc, x trừ h là dịch sang phải h đơn vị, trong khi x cộng h lại dịch sang trái h đơn vị.'
        }
    ]
    lectures.append({
        'code': 'm2_4',
        'module_key': 'math_m2',
        'order_index': 4,
        'title': '2.4 Nonlinear Systems, Radicals, Absolute Value & Transformations',
        'drill_key': 'drill_m2_4',
        'html': m2_4_html,
        'segments': m2_4_segs,
        'major_sections': [
            {'title': 'Hệ đường thẳng & Parabol', 'startSegmentId': 'nonlin'},
            {'title': 'Căn thức & Giá trị tuyệt đối', 'startSegmentId': 'rad_abs'},
            {'title': 'Biến đổi đồ thị f(x − h) + k', 'startSegmentId': 'transform'},
        ],
    })

    return lectures
