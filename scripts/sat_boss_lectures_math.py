# -*- coding: utf-8 -*-
"""
Digital SAT 1500+ — Hard M2 Boss Masterclass: 4 Elite Math Lectures (760–800)
- b5: Desmos Advanced Hacks — Multi-Param Regression & List Tricks
- b6: Parametric Quadratics, Integer Bounds & Hidden Substitutions
- b7: Hard M2 Geometry, Coordinate Circles & 3D Composite Solids
- b8: SPR Grid-In Trap-Proofing — 10 Deadly 800-Point Pitfalls
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from sat_audio_pipeline import build_sat_lecture_html, make_quick_check_html
from sat_math_helpers import svg_circle_sector, svg_cylinder

DESMOS_BOX_STYLE = 'background:#ecfdf5; border-left:4px solid #059669; padding:14px 16px; border-radius:10px; margin:12px 0; font-size:14.5px; color:#064e3b;'

def get_boss_math_lectures():
    lectures = []

    # =========================================================================
    # BOSS LECTURE 5: Desmos Advanced Hacks (Multi-Param Regression & Lists)
    # =========================================================================
    b5_cards = f'''
  <div id="sec-reg-id" class="sat-card lecture-interactive-card" data-lecture-section="reg_id">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>1. Tuyệt chiêu "Hồi quy Đồng nhất thức" (Identity Regression <code>~</code>) — Không cần khai triển tay!</h2>
    <p>Đây là vũ khí bí mật mạnh nhất mà 90% thí sinh không biết trên Digital SAT: Khi đề cho một đồng nhất thức đúng với mọi <code>x</code> (ví dụ <code>A/(x − 2) + B/(x + 5) = (7x + 14)/((x − 2)(x + 5))</code> và hỏi <code>A − B</code>), bạn <b>KHÔNG cần quy đồng đại số</b>!</p>
    <div style="{DESMOS_BOX_STYLE}">
      <b>⚡ Công thức Desmos 10 giây giải thẳng hằng số A, B, C, k:</b>
      <br>1. Dòng 1: Tạo một list các giá trị thử an toàn (tránh giá trị làm mẫu bằng 0): <code>x₁ = [0, 1, 3, 4, 6]</code>.
      <br>2. Dòng 2: Gõ nguyên đồng nhất thức nhưng <b>thay dấu <code>=</code> thành dấu ngã <code>~</code></b> và thay <code>x</code> bằng <code>x₁</code>:
      <br>&nbsp;&nbsp;&nbsp;<code>A/(x₁ − 2) + B/(x₁ + 5) ~ (7x₁ + 14)/((x₁ − 2)(x₁ + 5))</code>
      <br>3. Nhìn xuống phần <b>PARAMETERS</b>: Desmos lập tức in chính xác <code>A = 4</code>, <code>B = 3</code> (với <code>R² = 1</code>)! Gõ <code>A − B</code> ra ngay <b><code>1</code></b> trong 10 giây!
    </div>
    <div class="sat-trap-box">
      <b>🚨 Lưu ý kỹ thuật sống còn:</b> Không dùng các chữ cái dành riêng trong Desmos làm tham số hồi quy (tránh <code>e, x, y, r</code> — thay bằng <code>a, b, c, k, p, q</code>). Và list <code>x₁</code> nên có ít nhất số phần tử bằng <b>số tham số + 2</b>!
    </div>
  </div>

  <div id="sec-sys-reg" class="sat-card lecture-interactive-card" data-lecture-section="sys_reg">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>2. Hồi quy Giải Hệ &amp; Tìm Parabol/Hàm mũ dịch chuyển trong 15 giây</h2>
    <div style="{DESMOS_BOX_STYLE}">
      <b>• Tìm Parabol đi qua 3 điểm bất kỳ (Hard M2 Table):</b> Tạo bảng <code>(x₁, y₁)</code> gồm 3 điểm → gõ <code>y₁ ~ a x₁² + b x₁ + c</code> (hoặc dạng đỉnh <code>y₁ ~ a(x₁ − h)² + k</code> nếu biết trước đỉnh!). Sau đó gõ <code>f(x) = a x² + b x + c</code> để bấm ngay <code>f(12)</code> hay <code>a + b + c</code>!
      <br><b>• Tìm Đường tròn đi qua 3 điểm hoặc biết tâm:</b> Gõ <code>(x₁ − h)² + (y₁ − k)² ~ R</code> → Desmos giải thẳng tâm <code>(h, k)</code> và <code>r² = R</code>!
      <br><b>• Giải nhanh nghiệm bằng List Substitution:</b> Muốn kiểm tra câu <i>"For which value of k does the system have no solution?"</i> với 4 đáp án <code>A, B, C, D</code> → gõ <code>k = [−6, −3, 3, 6]</code> để Desmos vẽ cùng lúc cả 4 đường song song/cắt nhau!
    </div>
  </div>

  <div id="sec-domain-trick" class="sat-card lecture-interactive-card" data-lecture-section="domain_trick">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>3. Mẹo Giới hạn Miền <code>{{...}}</code> &amp; Tìm Cực trị trên Đoạn</h2>
    <div class="sat-rule-box">
      <b>📌 Cú pháp ngoặc nhọn <code>{{}}</code> cực hữu dụng trên Desmos:</b>
      <br>• Khi đề hỏi <i>"What is the maximum value of f(x) for 1 ≤ x ≤ 6?"</i> → gõ <code>f(x) = −2x² + 10x + 3 {{1 ≤ x ≤ 6}}</code>. Desmos chỉ vẽ đúng đoạn từ 1 đến 6 để bạn bấm điểm cao nhất/thấp nhất không bao giờ nhìn nhầm biên!
      <br>• Khi dùng hồi quy cần ép tham số dương (VD: đề nói <code>a &gt; 0</code>) → thêm <code>{{a &gt; 0}}</code> vào cuối dòng hồi quy hoặc kiểm tra nghiệm dương trực tiếp trên đồ thị!
    </div>
  </div>
'''
    b5_qc = make_quick_check_html(
        'qc_b5',
        'Dùng tư duy đồng nhất thức / Desmos Identity Regression: Nếu A/(x − 1) + B/(x + 3) = (5x + 7)/((x − 1)(x + 3)) đúng với mọi x ≠ 1, −3, giá trị của A − B bằng bao nhiêu?',
        'If <b>A/(x − 1) + B/(x + 3) = (5x + 7) / ((x − 1)(x + 3))</b> holds for all x ≠ 1, −3, what is the value of <b>A − B</b>?',
        ['−2', '1', '2', '5'],
        1,
        'Quy đồng tử số: A(x + 3) + B(x − 1) = (A + B)x + (3A − B) = 5x + 7. Suy ra A + B = 5 và 3A − B = 7 → cộng lại: 4A = 12 → A = 3, B = 2 → A − B = 3 − 2 = 1! Trên Desmos chỉ cần gõ x₁ = [0, 2, 4, 5] và dòng hồi quy dấu ~ là ra thẳng A = 3, B = 2 trong 8 giây!'
    )
    b5_html = build_sat_lecture_html(
        '🔥 HARD M2 BOSS MASTERCLASS • MATH BOSS 1 (760–800)',
        'Math Boss 1: Desmos Advanced Hacks — Multi-Param Regression & Lists',
        'Làm chủ vũ khí Desmos cấp độ 800: Hồi quy đồng nhất thức (~) tìm A, B, C không cần khai triển tay, hồi quy Parabol/Đường tròn và lọc miền bằng ngoặc nhọn {}.',
        [
            'Giải thẳng mọi bài đồng nhất thức đa thức & phân thức hữu tỉ bằng List x₁ + dấu hồi quy (~) trong 10 giây.',
            'Dùng hồi quy phi tuyến tìm nhanh phương trình Parabol, Hàm mũ và Đường tròn từ bảng tọa độ Hard M2.',
            'Sử dụng list kiểm tra đồng loạt 4 đáp án và cú pháp miền {a ≤ x ≤ b} để chốt cực trị không bao giờ sai biên.',
        ],
        b5_cards,
        b5_qc
    )
    b5_segs = [
        {
            'id': 'intro',
            'title': 'Tổng quan Desmos Nâng cao 800',
            'selector': '#sec-header',
            'en': 'Every student knows how to graph a line in Desmos. What separates a 720 Math scorer from an effortless 800 scorer is knowing how to weaponize Desmos regressions and lists to solve multi-parameter identity equations in ten seconds flat.',
            'vi': 'Học sinh nào cũng biết vẽ đường thẳng bằng Desmos. Nhưng điều phân biệt mốc 720 với điểm tuyệt đối 800 là khả năng biến hồi quy dấu ngã và danh sách list thành vũ khí giải gọn mọi bài toán đồng nhất thức đa tham số chỉ trong 10 giây.'
        },
        {
            'id': 'reg_id',
            'title': 'Hồi quy Đồng nhất thức (~) 10 giây',
            'selector': '#sec-reg-id',
            'en': 'Whenever a problem states that two algebraic expressions are equivalent for all values of x and asks for constants A, B, or C, define a short list x one equals zero, one, three, four, six, and type the identity with a tilde instead of an equals sign. Desmos instantly outputs exact values for every constant with zero algebra errors. Just avoid reserved letters like e, r, x, or y as parameters.',
            'vi': 'Hễ gặp bài toán cho hai biểu thức bằng nhau với mọi x và yêu cầu tìm hằng số A, B, C, hãy gõ một danh sách x một gồm vài số an toàn tránh mẫu bằng 0, rồi gõ nguyên biểu thức nhưng đổi dấu bằng thành dấu ngã hồi quy. Desmos sẽ trả về ngay giá trị chính xác của từng hằng số mà không lo sai dấu. Nhớ tránh dùng chữ e, r, x, y làm tên tham số.'
        },
        {
            'id': 'sys_reg',
            'title': 'Hồi quy Parabol, Đường tròn & List 4 đáp án',
            'selector': '#sec-sys-reg',
            'en': 'You can also fit parabolas, exponentials, and even circles directly from three table points using tilde regression, then immediately evaluate the fitted function at any target value. And when testing four multiple-choice constants for k, put all four choices in a bracketed list so Desmos plots every candidate at once.',
            'vi': 'Bạn cũng có thể tìm chính xác phương trình parabol, hàm mũ hay thậm chí cả đường tròn từ bảng ba điểm bằng hồi quy dấu ngã, sau đó tính thẳng giá trị hàm tại điểm đề hỏi. Khi cần thử bốn giá trị tham số k của 4 đáp án, hãy gộp cả bốn số vào dấu ngoặc vuông để Desmos vẽ cùng lúc một lượt.'
        },
        {
            'id': 'domain_trick',
            'title': 'Giới hạn miền bằng ngoặc nhọn {}',
            'selector': '#sec-domain-trick',
            'en': 'Use curly braces to restrict the domain of any function—for instance, plotting f of x only for x between one and six—so you can click the true maximum or minimum on that exact interval without falling for an out-of-domain vertex.',
            'vi': 'Dùng dấu ngoặc nhọn để giới hạn miền xác định của hàm số, ví dụ chỉ vẽ trên đoạn từ 1 đến 6, giúp bạn bấm chính xác điểm cực đại hay cực tiểu trên đoạn đó mà không bao giờ chọn nhầm đỉnh nằm ngoài miền.'
        }
    ]
    lectures.append({
        'code': 'b5',
        'module_key': 'boss_m10',
        'order_index': 5,
        'title': 'Math Boss 1: Desmos Advanced Hacks — Multi-Param Regression & Lists',
        'drill_key': 'boss_drill_5',
        'html': b5_html,
        'segments': b5_segs,
        'major_sections': [
            {'title': 'Hồi quy Đồng nhất thức (~)', 'startSegmentId': 'reg_id'},
            {'title': 'Hồi quy Parabol, Đường tròn & Lists', 'startSegmentId': 'sys_reg'},
            {'title': 'Giới hạn miền bằng ngoặc nhọn {}', 'startSegmentId': 'domain_trick'},
        ],
    })

    # =========================================================================
    # BOSS LECTURE 6: Parametric Quadratics, Integer Bounds & Disguised Substitutions
    # =========================================================================
    b6_cards = f'''
  <div id="sec-intbounds" class="sat-card lecture-interactive-card" data-lecture-section="intbounds">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>1. Chặn Biên Số nguyên cho Tham số <code>k</code> (Integer Bound Bosses — Q18–Q22)</h2>
    <p>Trong Module 2 Hard, rất nhiều câu không hỏi giá trị chính xác của <code>k</code>, mà hỏi: <i>"What is the <b>greatest / least integer</b> value of k such that the equation has <b>no real solutions / two distinct real solutions</b>?"</i></p>
    <div class="sat-gold-box">
      <b>⭐ Checklist 3 bước KHÔNG BAO GIỜ sai biên ±1:</b>
      <br>1. Gom sạch về <code>ax² + bx + c = 0</code> (cẩn thận khi hệ số <code>a</code> hay <code>c</code> chứa tham số!).
      <br>2. Lập đúng <b>bất đẳng thức NGHIÊM NGẶT</b>:
      <br>&nbsp;&nbsp;• 2 nghiệm phân biệt → <code>Δ &gt; 0</code> (KHÔNG có dấu =)
      <br>&nbsp;&nbsp;• Vô nghiệm thực → <code>Δ &lt; 0</code> (KHÔNG có dấu =)
      <br>&nbsp;&nbsp;• Có ít nhất 1 nghiệm thực ("at least one real solution") → <code>Δ ≥ 0</code> (CÓ dấu =!)
      <br>3. Chốt số nguyên sát biên: Ví dụ ra <code>k &lt; 16.25</code> → max nguyên là <b><code>16</code></b>; ra <code>k &lt; 16</code> → max nguyên là <b><code>15</code></b>!
    </div>
  </div>

  <div id="sec-usub" class="sat-card lecture-interactive-card" data-lecture-section="usub">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>2. Phương trình Bậc hai Ngụy trang (Disguised Quadratics — Đặt ẩn phụ <code>u</code>)</h2>
    <p>College Board thường giấu phương trình bậc hai quen thuộc dưới 4 lớp mặt nạ kinh điển ở cuối Hard M2:</p>
    <table class="sat-table">
      <thead><tr><th>Dạng Ngụy trang trên đề</th><th>Đặt ẩn phụ <code>u</code></th><th>Bẫy nghiệm cần kiểm tra</th></tr></thead>
      <tbody>
        <tr><td><code>x⁴ − 13x² + 36 = 0</code></td><td><code>u = x² (u ≥ 0)</code></td><td>Mỗi nghiệm <code>u &gt; 0</code> sinh ra <b>2 nghiệm đối nhau ±√u</b> (4 nghiệm tổng, tổng bằng 0!).</td></tr>
        <tr><td><code>(x − 4)² − 7(x − 4) + 10 = 0</code></td><td><code>u = x − 4</code></td><td>Giải ra <code>u = 2, 5</code> → nhớ cộng lại 4 để ra <code>x = 6, 9</code> (tổng <code>x = 15</code>, KHÔNG phải 7!).</td></tr>
        <tr><td><code>x − 5√x + 6 = 0</code></td><td><code>u = √x (u ≥ 0)</code></td><td>Loại mọi nghiệm <code>u &lt; 0</code>! Nghiệm <code>u = 2, 3 ⇒ x = 4, 9</code>!</td></tr>
        <tr><td><code>4^x − 10 · 2^x + 16 = 0</code></td><td><code>u = 2^x (u &gt; 0)</code></td><td><code>u = 2, 8 ⇒ 2^x = 2, 8 ⇒ x = 1, 3</code>!</td></tr>
      </tbody>
    </table>
  </div>

  <div id="sec-vieta-adv" class="sat-card lecture-interactive-card" data-lecture-section="vieta_adv">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>3. Biến thể Vieta 800: Tính <code>r² + s²</code>, <code>1/r + 1/s</code> &amp; Điều kiện Nghiệm dương</h2>
    <div class="sat-rule-box">
      <b>⭐ 2 Hằng đẳng thức Vieta cứu mạng khi nghiệm là số vô tỉ xấu:</b>
      <br>Gọi <code>S = r + s = −b/a</code> và <code>P = r · s = c/a</code>:
      <br>• <b>Tổng bình phương 2 nghiệm:</b> <code>r² + s² = (r + s)² − 2rs = S² − 2P</code>!
      <br>• <b>Tổng nghịch đảo 2 nghiệm:</b> <code>1/r + 1/s = (r + s) / (rs) = −b / c</code>!
      <br>• <b>Cả hai nghiệm đều dương (khi Δ ≥ 0):</b> <code>S &gt; 0</code> VÀ <code>P &gt; 0</code>.
    </div>
    <div style="{DESMOS_BOX_STYLE}">
      <b>⚡ Desmos Check:</b> Vẽ <code>y = ax² + bx + c</code> (hoặc <code>y = x⁴ − 13x² + 36</code>), bấm trực tiếp tọa độ các giao điểm trục Ox để đối chiếu ngay đáp án trong 5 giây!
    </div>
  </div>
'''
    b6_qc = make_quick_check_html(
        'qc_b6',
        'Gọi r và s là hai nghiệm thực của phương trình 2x² − 12x + 7 = 0. Giá trị chính xác của r² + s² là bao nhiêu?',
        'If <i>r</i> and <i>s</i> are the two real solutions to <b>2x² − 12x + 7 = 0</b>, what is the value of <b>r² + s²</b>?',
        ['22', '29', '36', '43'],
        1,
        'Kiểm tra Δ = 144 − 56 = 88 > 0 (có 2 nghiệm thực). Theo Vieta: S = r + s = 12/2 = 6 và P = rs = 7/2 = 3.5. Áp dụng công thức r² + s² = (r + s)² − 2rs = 6² − 2(7/2) = 36 − 7 = 29! Cẩn thận bẫy 36 là (r + s)² quên trừ 2rs, và bẫy 22 là quên chia hệ số a = 2 ở P!'
    )
    b6_html = build_sat_lecture_html(
        '🔥 HARD M2 BOSS MASTERCLASS • MATH BOSS 2 (760–800)',
        'Math Boss 2: Parametric Quadratics, Integer Bounds & Hidden Substitutions',
        'Xử lý gọn gàng các bài toán bậc hai cấp độ trùm cuối: chặn biên số nguyên Δ, đặt ẩn phụ cho phương trình bậc 4/căn/mũ và biến thể Vieta r² + s².',
        [
            'Chốt chuẩn số nguyên sát biên (±1) cho tham số k khi đề yêu cầu 0, 1 hay 2 nghiệm thực phân biệt.',
            'Nhận diện tức thì 4 dạng phương trình bậc hai ngụy trang (x⁴, (x−c)², √x, 2^x) và tránh loại sót/giữ nhầm nghiệm.',
            'Tính tốc hành r² + s² = S² − 2P và 1/r + 1/s = −b/c mà không cần dùng công thức nghiệm căn bậc hai.',
        ],
        b6_cards,
        b6_qc
    )
    b6_segs = [
        {
            'id': 'intro',
            'title': 'Tổng quan Bậc hai Tham số & Ẩn phụ 800',
            'selector': '#sec-header',
            'en': 'In the final stretch of Hard Module Two, quadratic concepts hide behind integer parameter bounds, disguised quartic or radical equations, and symmetric root expressions like r squared plus s squared. Let us dismantle all three.',
            'vi': 'Ở chặng nước rút cuối Hard Module 2, kiến thức bậc hai thường ẩn mình sau các bài toán chặn biên số nguyên tham số k, phương trình bậc 4 hoặc căn thức ngụy trang và các biểu thức đối xứng như r bình cộng s bình. Chúng ta sẽ tháo gỡ sạch cả ba dạng này.'
        },
        {
            'id': 'intbounds',
            'title': 'Chặn biên số nguyên tham số k',
            'selector': '#sec-intbounds',
            'en': 'For integer-bound discriminant questions, always check whether the inequality is strict or inclusive. Two distinct real roots require delta strictly greater than zero; no real roots require delta strictly less than zero; and at least one real root includes zero. If your bound says k is strictly less than sixteen, the greatest integer is fifteen, never sixteen.',
            'vi': 'Với bài toán tìm số nguyên lớn nhất hay nhỏ nhất của tham số k theo biệt thức delta, hãy soi thật kỹ dấu bất đẳng thức có lấy dấu bằng hay không. Hai nghiệm phân biệt đòi delta lớn hơn hẳn 0, vô nghiệm đòi nhỏ hơn hẳn 0, còn ít nhất một nghiệm mới cho phép bằng 0. Nếu ra k nhỏ hơn hẳn 16 thì số nguyên lớn nhất là 15.'
        },
        {
            'id': 'usub',
            'title': '4 Mặt nạ Phương trình Bậc hai Ngụy trang',
            'selector': '#sec-usub',
            'en': 'Watch for four classic u-substitutions: u equals x squared, u equals a shifted block like x minus four, u equals root x, and u equals two to the x. Always remember to solve back for x at the end, and reject negative u values whenever u represents a square, a square root, or an exponential.',
            'vi': 'Nhận diện ngay 4 kiểu đặt ẩn phụ kinh điển: u bằng x bình, u bằng cụm x trừ c, u bằng căn x và u bằng 2 mũ x. Luôn nhớ trả lại biến x ở bước cuối cùng và loại ngay các nghiệm u âm nếu u đại diện cho bình phương, căn bậc hai hoặc hàm mũ.'
        },
        {
            'id': 'vieta_adv',
            'title': 'Biến thể Vieta r² + s² và 1/r + 1/s',
            'selector': '#sec-vieta-adv',
            'en': 'Never plug ugly irrational roots into r squared plus s squared. Use the symmetric Vieta identity: r squared plus s squared equals S squared minus two P, where S is negative b over a and P is c over a. Similarly, one over r plus one over s simplifies instantly to negative b over c.',
            'vi': 'Đừng bao giờ thay nghiệm căn bậc hai xấu vào r bình cộng s bình. Hãy dùng hằng đẳng thức Vieta: r bình cộng s bình bằng S bình trừ hai P, với S là tổng hai nghiệm và P là tích hai nghiệm. Tương tự, một trên r cộng một trên s rút gọn siêu gọn thành trừ b trên c.'
        }
    ]
    lectures.append({
        'code': 'b6',
        'module_key': 'boss_m10',
        'order_index': 6,
        'title': 'Math Boss 2: Parametric Quadratics, Integer Bounds & Hidden Substitutions',
        'drill_key': 'boss_drill_6',
        'html': b6_html,
        'segments': b6_segs,
        'major_sections': [
            {'title': 'Chặn biên số nguyên tham số k', 'startSegmentId': 'intbounds'},
            {'title': '4 Dạng Bậc hai Ngụy trang', 'startSegmentId': 'usub'},
            {'title': 'Biến thể Vieta 800', 'startSegmentId': 'vieta_adv'},
        ],
    })

    # =========================================================================
    # BOSS LECTURE 7: Hard M2 Geometry, Coordinate Circles & 3D Composite Solids
    # =========================================================================
    svg_b7_circ = svg_circle_sector('r', 'θ', note='Tangent ⊥ Radius  |  s = rθ  |  A = ½rs')
    svg_b7_cyl = svg_cylinder('r', 'h', note='Frustum / Composite 3D Solids via k : k² : k³')

    b7_cards = f'''
  <div id="sec-coord-circ" class="sat-card lecture-interactive-card" data-lecture-section="coord_circ">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>1. Đường tròn Tọa độ Nâng cao: Tiếp tuyến, Trục tọa độ &amp; Tham số <code>k</code></h2>
    <div style="display:flex;justify-content:center;margin:10px 0;">{svg_b7_circ}</div>
    <div class="sat-gold-box">
      <b>⭐ 4 Chiêu Hình học Đường tròn Tọa độ 780–800:</b>
      <br>1. <b>Đường tròn tiếp xúc trục tọa độ:</b> Tâm <code>(h, k)</code> tiếp xúc trục Ox → bán kính <code>r = |k|</code>; tiếp xúc trục Oy → <code>r = |h|</code>; tiếp xúc CẢ 2 trục ở Q-I → tâm <code>(r, r)</code>!
      <br>2. <b>Phương trình tiếp tuyến tại điểm <code>P(x₀, y₀)</code>:</b> Tính slope bán kính <code>m_r = (y₀ − k) / (x₀ − h)</code> → slope tiếp tuyến là nghịch đảo đổi dấu <code>m_t = −1 / m_r</code>!
      <br>3. <b>Tiếp tuyến từ điểm ngoài <code>E</code> tới tiếp điểm <code>T</code>:</b> Tam giác <code>△OTE</code> vuông tại <code>T</code> → <code>ET² + r² = OE²</code> (Pythagoras!).
      <br>4. <b>Phím tắt Diện tích Quạt từ Độ dài Cung (không cần góc θ!):</b> Vì <code>s = rθ</code> và <code>A = ½ r²θ</code> → <b><code>A = ½ r · s</code></b>! Biết bán kính <code>r</code> và cung <code>s</code> ra thẳng diện tích quạt trong 3 giây!
    </div>
  </div>

  <div id="sec-alt-trig" class="sat-card lecture-interactive-card" data-lecture-section="alt_trig">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>2. Đường cao Tam giác vuông (Altitude Similarity) &amp; Lượng giác Radian Góc phần tư II–III</h2>
    <div class="sat-rule-box">
      <b>📌 Tam giác vuông có đường cao <code>h</code> hạ xuống cạnh huyền (chia cạnh huyền thành <code>p</code> và <code>q</code>):</b>
      <br>• Ba tam giác vuông đều <b>đồng dạng với nhau</b>!
      <br>• Hệ thức lượng vàng: <b><code>h² = p · q</code></b> (đường cao bình phương bằng tích hai hình chiếu!), và cạnh góc vuông <code>a² = p · (p + q)</code>!
      <br><b>📌 Lượng giác Radian góc tù (ASTC — "All Students Take Calculus"):</b>
      <br>• Q-I (<code>0..π/2</code>): Tất cả dương • Q-II (<code>π/2..π</code>): chỉ <b>sin dương</b> (<code>cos &lt; 0, tan &lt; 0</code>) • Q-III (<code>π..3π/2</code>): chỉ <b>tan dương</b> • Q-IV: chỉ <b>cos dương</b>!
      <br>• VD: <code>cos(2π/3) = −1/2</code> (vì <code>2π/3 = 120°</code> ở Q-II có góc tham chiếu <code>60°</code> và cos âm!).
    </div>
  </div>

  <div id="sec-composite3d" class="sat-card lecture-interactive-card" data-lecture-section="composite3d">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>3. Hình khối 3D Ghép (Composite Solids) &amp; Hình Nón Cụt (Frustum)</h2>
    <div style="display:flex;justify-content:center;margin:10px 0;">{svg_b7_cyl}</div>
    <div class="sat-ex-box">
      <b>Mô hình "Trùm cuối Q22" — Nón cụt (Frustum) bằng Luật Tỉ lệ <code>k³</code>:</b>
      <br>Cắt bỏ phần đỉnh của một hình nón lớn (chiều cao <code>H</code>) ở vị trí cách đỉnh một đoạn <code>h = H / 3</code> (tức tỉ lệ tuyến tính nón nhỏ / nón lớn là <code>k = 1/3</code>).
      <br>• Thể tích nón nhỏ bị cắt = <code>(1/3)³ = 1/27</code> thể tích nón lớn!
      <br>• Thể tích phần <b>nón cụt còn lại (frustum)</b> = <b><code>1 − 1/27 = 26/27</code></b> thể tích nón lớn!
    </div>
    <div class="sat-trap-box">
      <b>🚨 Bẫy Diện tích Toàn phần Hình ghép (Hollowed / Stacked Solids):</b> Khi khoét rỗng một hình nón bên trong hình trụ, đừng trừ diện tích xung quanh — <b>mặt nón bên trong trở thành bề mặt lộ thiên mới nên phải CỘNG THÊM <code>πrℓ</code></b> (và chỉ bỏ đi 1 mặt đáy tròn bị khoét thủng)!
    </div>
  </div>
'''
    b7_qc = make_quick_check_html(
        'qc_b7',
        'Một hình quạt tròn có bán kính r = 8 cm và độ dài cung tròn là s = 5π cm. Diện tích của hình quạt tròn này bằng bao nhiêu cm²?',
        'A sector of a circle has radius <b>r = 8 cm</b> and arc length <b>s = 5π cm</b>. What is the <b>area</b> of the sector, in square centimeters?',
        ['10π', '20π', '40π', '64π'],
        1,
        'Áp dụng phím tắt 3 giây A = ½ · r · s = ½ · (8) · (5π) = 20π cm²! (Hoặc tìm góc θ = s/r = 5π/8 rad, rồi A = ½ r²θ = ½(64)(5π/8) = 20π). Cẩn thận bẫy 40π là quên hệ số ½!'
    )
    b7_html = build_sat_lecture_html(
        '🔥 HARD M2 BOSS MASTERCLASS • MATH BOSS 3 (760–800)',
        'Math Boss 3: Hard M2 Geometry, Coordinate Circles & 3D Composite Solids',
        'Chinh phục nhóm câu Hình học & 3D khó nhất cuối Module 2 Hard: đường tròn tiếp tuyến tọa độ, hệ thức đường cao h² = pq, lượng giác góc tù và nón cụt tỉ lệ k³.',
        [
            'Giải tốc hành các bài đường tròn tiếp xúc trục tọa độ, tiếp tuyến vuông góc bán kính và phím tắt diện tích quạt A = ½rs.',
            'Áp dụng hệ thức đường cao tam giác vuông h² = pq và quy tắc dấu lượng giác ASTC cho góc Radian ở mọi góc phần tư.',
            'Tính chuẩn thể tích hình nón cụt (frustum = 1 − k³) và tránh bẫy diện tích toàn phần của hình khối 3D ghép/khoét rỗng.',
        ],
        b7_cards,
        b7_qc
    )
    b7_segs = [
        {
            'id': 'intro',
            'title': 'Tổng quan Hình học 780–800 & 3D Ghép',
            'selector': '#sec-header',
            'en': 'The hardest Geometry questions at the end of Module Two combine coordinate algebra, circle theorems, right-triangle altitudes, and composite 3D solids. Master four compact shortcuts and these twenty-point bosses become straightforward.',
            'vi': 'Những câu hình học khó nhất cuối Module 2 thường kết hợp tọa độ, định lý đường tròn, đường cao tam giác vuông và hình khối 3D ghép. Nắm chắc bốn phím tắt tinh gọn sau sẽ biến những câu trùm cuối 20 điểm này trở nên cực kỳ dễ xử lý.'
        },
        {
            'id': 'coord_circ',
            'title': 'Đường tròn tọa độ, Tiếp tuyến & Phím tắt A = ½rs',
            'selector': '#sec-coord-circ',
            'en': 'A circle tangent to the x-axis has radius equal to the absolute value of its y-coordinate k, and any tangent line is perpendicular to the radius at the point of tangency—giving you either a negative reciprocal slope or a right triangle for the Pythagorean theorem. And whenever you know radius r and arc length s, skip finding the angle and use sector area equals one half times r times s.',
            'vi': 'Đường tròn tiếp xúc trục hoành có bán kính bằng trị tuyệt đối tung độ tâm k, và tiếp tuyến luôn vuông góc bán kính tại tiếp điểm, cho ta ngay hệ số góc nghịch đảo đổi dấu hoặc tam giác vuông để dùng Pythagoras. Đặc biệt khi biết bán kính r và độ dài cung s, đừng tính góc mà nhân thẳng diện tích quạt bằng một nửa r nhân s.'
        },
        {
            'id': 'alt_trig',
            'title': 'Đường cao tam giác vuông h² = pq & Dấu ASTC',
            'selector': '#sec-alt-trig',
            'en': 'Drawing an altitude to the hypotenuse of a right triangle splits it into two smaller triangles similar to the whole, yielding the instant formula h squared equals p times q. For radian trig angles beyond ninety degrees, check the quadrant sign using All Students Take Calculus—or verify in Desmos Radian mode.',
            'vi': 'Kẻ đường cao xuống cạnh huyền của tam giác vuông tạo ra ba tam giác đồng dạng và hệ thức vàng h bình bằng p nhân q. Với góc lượng giác radian lớn hơn 90 độ, nhớ xét đúng dấu âm dương theo từng góc phần tư hoặc kiểm chứng ngay bằng Desmos ở chế độ Radian.'
        },
        {
            'id': 'composite3d',
            'title': 'Hình nón cụt (Frustum) & Diện tích khối ghép',
            'selector': '#sec-composite3d',
            'en': 'For a frustum or truncated pyramid, never memorize a messy formula—subtract the smaller top cone from the full cone using the volume scaling ratio k cubed. And for hollowed-out solids, remember that an interior carved surface adds new exposed surface area rather than subtracting it.',
            'vi': 'Với hình nón cụt hay chóp cụt, đừng thuộc công thức rườm rà mà hãy lấy hình lớn trừ phần đỉnh nhỏ bằng tỉ lệ thể tích k lập phương. Còn với diện tích toàn phần của hình khối khoét rỗng, nhớ rằng mặt khoét bên trong là bề mặt lộ thiên mới nên phải cộng thêm diện tích xung quanh chứ không được trừ đi.'
        }
    ]
    lectures.append({
        'code': 'b7',
        'module_key': 'boss_m10',
        'order_index': 7,
        'title': 'Math Boss 3: Hard M2 Geometry, Coordinate Circles & 3D Composite Solids',
        'drill_key': 'boss_drill_7',
        'html': b7_html,
        'segments': b7_segs,
        'major_sections': [
            {'title': 'Đường tròn tọa độ & A = ½rs', 'startSegmentId': 'coord_circ'},
            {'title': 'Đường cao h² = pq & Lượng giác', 'startSegmentId': 'alt_trig'},
            {'title': 'Nón cụt k³ & Khối ghép 3D', 'startSegmentId': 'composite3d'},
        ],
    })

    # =========================================================================
    # BOSS LECTURE 8: SPR Grid-In Trap-Proofing — 10 Deadly 800-Point Pitfalls
    # =========================================================================
    b8_cards = '''
  <div id="sec-top5" class="sat-card lecture-interactive-card" data-lecture-section="top5">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>1. Top 5 Cái bẫy Đại số &amp; Hàm số "Đốt 30 điểm" trên câu SPR Tự điền số</h2>
    <p>Ở câu trắc nghiệm (MCQ), nếu tính nhầm bạn còn thấy không khớp 4 đáp án để giật mình sửa lại. Nhưng ở <b>6 câu SPR tự điền số mỗi module</b>, không có đáp án gợi ý — sai 1 milimét là mất trắng 10–20 điểm! Hãy chạy qua <b>10-Point Anti-Trap Checklist</b> này trước khi bấm Next:</p>
    <table class="sat-table">
      <thead><tr><th>#</th><th>Cái bẫy 800-Point</th><th>Cách tự bảo vệ trong 2 giây</th></tr></thead>
      <tbody>
        <tr><td><b>1</b></td><td><b>Giải ra <code>x</code> nhưng đề hỏi <code>5x − 3</code>, <code>a + b</code> hay <code>diameter</code></b></td><td>Gạch chân biểu thức đề hỏi NGAY trước khi nhập số vào ô SPR!</td></tr>
        <tr><td><b>2</b></td><td><b>Quên loại nghiệm ngoại lai (Căn thức &amp; Phân thức)</b></td><td>Thử lại nghiệm vào mẫu số (<code>≠ 0</code>) và vế phải căn thức (<code>≥ 0</code>), hoặc kiểm tra giao điểm thực trên Desmos.</td></tr>
        <tr><td><b>3</b></td><td><b>Quên chia hệ số dẫn đầu <code>a ≠ 1</code> (Vieta &amp; Đường tròn)</b></td><td>Vieta là <code>−b/a</code> và <code>c/a</code>; Đường tròn <code>2x² + 2y² + ...</code> phải chia 2 trước!</td></tr>
        <tr><td><b>4</b></td><td><b>Cộng trùng nghiệm kép khi đề hỏi "sum of distinct solutions"</b></td><td>Nếu <code>(x − 5)² = 0</code> → chỉ có 1 nghiệm phân biệt là <code>5</code> (KHÔNG phải <code>5 + 5 = 10</code>!).</td></tr>
        <tr><td><b>5</b></td><td><b>Bảng giá trị bị dịch chuyển <code>f(x + 2)</code> hoặc <code>f(x) − 5</code></b></td><td>Kiểm tra tiêu đề cột bảng trước khi gõ Table vào Desmos!</td></tr>
      </tbody>
    </table>
  </div>

  <div id="sec-bot5" class="sat-card lecture-interactive-card" data-lecture-section="bot5">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>2. Top 5 Cái bẫy Đơn vị, Phần trăm, Thống kê &amp; Hình học</h2>
    <table class="sat-table">
      <thead><tr><th>#</th><th>Cái bẫy 800-Point</th><th>Cách tự bảo vệ trong 2 giây</th></tr></thead>
      <tbody>
        <tr><td><b>6</b></td><td><b>Đổi đơn vị diện tích/thể tích quên nâng lũy thừa</b></td><td>Diện tích: bình phương (<code>1 ft² = 144 in²</code>); Thể tích: lập phương (<code>1 yd³ = 27 ft³</code>).</td></tr>
        <tr><td><b>7</b></td><td><b>Nhầm "p% greater than" với "p% of"</b></td><td>"140% greater than x" = <code>2.40x</code> (KHÔNG phải <code>1.40x</code>!).</td></tr>
        <tr><td><b>8</b></td><td><b>Làm tròn sai hướng ở Bất phương trình số nguyên</b></td><td><code>x ≤ 14.8 → 14</code>; <code>x ≥ 6.2 → 7</code>; <code>x &lt; 10 → 9</code> (nghiêm ngặt không lấy 10!).</td></tr>
        <tr><td><b>9</b></td><td><b>Nhầm mẫu số Xác suất có điều kiện &amp; Tính chất SD</b></td><td>"Given Group A" → chia tổng hàng/cột A; Cộng <code>+c</code> không làm đổi Standard Deviation!</td></tr>
        <tr><td><b>10</b></td><td><b>Đề yêu cầu "in terms of π" → chỉ nhập hệ số <code>k</code>!</b></td><td>Nếu đề viết <i>"The volume is kπ. What is the value of k?"</i> → chỉ gõ <b><code>160</code></b>, KHÔNG gõ <code>160*3.14</code>!</td></tr>
      </tbody>
    </table>
  </div>

  <div id="sec-spr-format" class="sat-card lecture-interactive-card" data-lecture-section="spr_format">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>3. Quy tắc Vàng Định dạng Ô nhập SPR trên Bluebook Thật</h2>
    <div class="sat-gold-box">
      <b>⭐ 4 Luật Nhập số An toàn Tuyệt đối trên Bluebook:</b>
      <br>1. <b>Ưu tiên phân số tối giản hơn số thập phân tuần hoàn:</b> Với <code>2/3</code>, nhập thẳng <b><code>2/3</code></b> (an toàn 100%, không sợ làm tròn thiếu chữ số như <code>0.66</code> bị chấm SAI!).
      <br>2. <b>TUYỆT ĐỐI KHÔNG nhập hỗn số:</b> Muốn nhập một rưỡi, gõ <code>3/2</code> hoặc <code>1.5</code> (nếu gõ <code>1 1/2</code> máy chấm thành <code>11/2 = 5.5</code>!).
      <br>3. <b>Dấu âm được phép nhập trên Digital SAT:</b> Đặt dấu <code>-</code> ngay đầu (VD: <code>-7/4</code> hoặc <code>-1.75</code>).
      <br>4. <b>Kiểm tra khung Answer Preview:</b> Luôn liếc mắt xác nhận phân số/số âm hiển thị chuẩn trong ô Preview trước khi bấm Next!
    </div>
  </div>
'''
    b8_qc = make_quick_check_html(
        'qc_b8',
        'Cảnh giác Bẫy #4 (Distinct Solutions): Phương trình (x − 6)²(x + 2) = 0 có tổng các nghiệm PHÂN BIỆT (sum of the distinct solutions) bằng bao nhiêu?',
        'What is the <b>sum of the distinct solutions</b> to the equation <b>(x − 6)²(x + 2) = 0</b>?',
        ['4', '10', '14', '−12'],
        0,
        'Các nghiệm phân biệt (distinct solutions) của phương trình là x = 6 (nghiệm kép chỉ tính MỘT lần!) và x = −2. Vậy tổng các nghiệm phân biệt là 6 + (−2) = 4! Bẫy 10 đến từ việc cộng trùng nghiệm kép 6 + 6 + (−2) = 10!'
    )
    b8_html = build_sat_lecture_html(
        '🔥 HARD M2 BOSS MASTERCLASS • MATH BOSS 4 (760–800)',
        'Math Boss 4: SPR Grid-In Trap-Proofing — 10 Deadly 800-Point Pitfalls',
        'Lá chắn bảo vệ điểm 800 Math tuyệt đối: Checklist 10 cái bẫy mất điểm oan trên các câu tự điền số (SPR) và 4 luật nhập phân số/thập phân chuẩn Bluebook.',
        [
            'Rà soát tự động 10 bẫy chí mạng hay làm thí sinh 760+ mất oan 20–30 điểm trên các câu tự điền số SPR.',
            'Phân biệt sắc nét bẫy distinct solutions, bẫy kπ, bẫy đường kính vs bán kính và bẫy "p% greater than".',
            'Tuân thủ 4 luật nhập đáp án SPR chuẩn Bluebook (ưu tiên phân số a/b thay cho thập phân vô hạn, tuyệt đối không nhập hỗn số).',
        ],
        b8_cards,
        b8_qc
    )
    b8_segs = [
        {
            'id': 'intro',
            'title': 'Tổng quan Lá chắn Chống bẫy SPR 800',
            'selector': '#sec-header',
            'en': 'Welcome to the final capstone lesson of Digital SAT 1500 Plus! On multiple-choice questions, an off-by-one mistake often fails to match the four options, giving you a second chance. On Student-Produced Response grid-ins, there is no safety net. Let us build a ten-point shield to guarantee your 800.',
            'vi': 'Chào mừng bạn đến với bài giảng chốt hạ của khóa Digital SAT 1500 Plus! Ở câu trắc nghiệm, nếu tính nhầm bạn còn thấy lệch bốn đáp án để kịp sửa. Nhưng ở dạng tự điền số SPR, không có lưới an toàn nào cả. Hãy cùng dựng bộ lá chắn 10 điểm để khóa chắc mốc 800 Toán.'
        },
        {
            'id': 'top5',
            'title': '5 Bẫy Đại số & Hàm số hay mất oan nhất',
            'selector': '#sec-top5',
            'en': 'Check these five algebraic traps before typing any answer: first, confirm whether the prompt asks for x or an expression like five x minus three or the diameter; second, test radical and rational roots for extraneous solutions; third, divide by the leading coefficient a in Vieta and circle equations; fourth, count a double root only once when asked for distinct solutions; and fifth, check table column headers for shifted functions.',
            'vi': 'Kiểm tra 5 cái bẫy đại số sau trước khi nhập số: một là soi kỹ đề hỏi x hay hỏi biểu thức như 5x trừ 3 hay đường kính; hai là luôn thử lại nghiệm căn thức và phân thức loại nghiệm ngoại lai; ba là nhớ chia hệ số a trong Vieta và đường tròn; bốn là chỉ tính nghiệm kép một lần nếu đề nói distinct solutions; và năm là đọc kỹ tiêu đề cột bảng dữ liệu xem hàm có bị dịch chuyển không.'
        },
        {
            'id': 'bot5',
            'title': '5 Bẫy Đơn vị, Phần trăm, Thống kê & kπ',
            'selector': '#sec-bot5',
            'en': 'Next, guard against five applied traps: square or cube linear factors for area and volume conversions; translate p percent greater than as one plus p over one hundred; round integer inequalities in the exact required direction; restrict conditional probability denominators to the stated group; and when a question asks for k where the answer is k pi, enter only the number k without multiplying by pi.',
            'vi': 'Tiếp theo, cảnh giác 5 bẫy ứng dụng: luôn bình phương hoặc lập phương hệ số khi đổi diện tích và thể tích; dịch đúng lớn hơn p phần trăm là cộng thêm vào 100 phần trăm gốc; làm tròn đúng chiều bất đẳng thức số nguyên; thu gọn mẫu số xác suất có điều kiện đúng hàng cột đề nêu; và khi đề hỏi hệ số k của k pi thì chỉ nhập đúng con số k.'
        },
        {
            'id': 'spr_format',
            'title': '4 Luật nhập SPR chuẩn Bluebook',
            'selector': '#sec-spr-format',
            'en': 'Finally, master SPR entry rules: always enter repeating fractions like two thirds as exact fractions rather than rounded decimals, never type mixed numbers, place a minus sign cleanly at the front for negative answers, and verify the Answer Preview box before clicking Next. You are now fully equipped to crush the Digital SAT 1500 Plus!',
            'vi': 'Cuối cùng, nhớ 4 luật nhập ô SPR: luôn nhập phân số tối giản như 2 trên 3 thay vì làm tròn số thập phân vô hạn, tuyệt đối không nhập hỗn số, đặt dấu trừ ở đầu cho số âm và liếc nhanh khung Answer Preview trước khi chuyển câu. Chúc bạn bùng nổ điểm số 1500 cộng trong kỳ thi Digital SAT!'
        }
    ]
    lectures.append({
        'code': 'b8',
        'module_key': 'boss_m10',
        'order_index': 8,
        'title': 'Math Boss 4: SPR Grid-In Trap-Proofing — 10 Deadly 800-Point Pitfalls',
        'drill_key': 'boss_drill_8',
        'html': b8_html,
        'segments': b8_segs,
        'major_sections': [
            {'title': 'Top 5 Bẫy Đại số & Hàm số', 'startSegmentId': 'top5'},
            {'title': 'Top 5 Bẫy Đơn vị, % & kπ', 'startSegmentId': 'bot5'},
            {'title': '4 Luật nhập SPR chuẩn Bluebook', 'startSegmentId': 'spr_format'},
        ],
    })

    return lectures
