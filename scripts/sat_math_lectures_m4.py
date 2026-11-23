# -*- coding: utf-8 -*-
"""
Digital SAT Math 1500+ — Module 4 Lectures (Geometry & Trigonometry 750–800):
- m4_1: Triangles, Parallel Lines, Similarity & Special Right Triangles
- m4_2: Circle Equations (Completing the Square), Arcs, Sectors & Radians
- m4_3: Trigonometry (SOH-CAH-TOA, Cofunctions) & 3D Solid Scaling (k, k², k³)
"""

import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from sat_audio_pipeline import build_sat_lecture_html, make_quick_check_html
from sat_math_helpers import svg_right_triangle, svg_parallel_transversal, svg_circle_sector, svg_cylinder

DESMOS_BOX_STYLE = 'background:#ecfdf5; border-left:4px solid #059669; padding:14px 16px; border-radius:10px; margin:12px 0; font-size:14.5px; color:#064e3b;'

def get_m4_lectures():
    lectures = []

    # =========================================================================
    # LECTURE M4.1: Triangles, Parallel Lines, Similarity & Special Right Triangles
    # =========================================================================
    svg_tri_ref = svg_right_triangle('x', 'x√3', '2x', angle_bottom_right='30°', angle_top_left='60°', note='30°–60°–90° Special Right Triangle')
    svg_par_ref = svg_parallel_transversal('ℓ', 'm', ang1_lbl='x°', ang2_lbl='x°', ang3_lbl='(180−x)°', note='Parallel Lines: Acute = Acute, Acute + Obtuse = 180°')

    m4_1_cards = f'''
  <div id="sec-angles" class="sat-card lecture-interactive-card" data-lecture-section="angles">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>1. Đường thẳng Song song, Định lý Góc ngoài &amp; Đa giác n cạnh</h2>
    <div style="display:flex;justify-content:center;margin:10px 0;">{svg_par_ref}</div>
    <div class="sat-rule-box">
      <b>⚡ Quy tắc "2 loại góc" khi cát tuyến cắt 2 đường song song:</b>
      <br>• Mọi góc <b>nhọn đều bằng nhau</b>, mọi góc <b>tù đều bằng nhau</b>, và <b>1 góc nhọn + 1 góc tù = 180°</b>!
      <br>• <b>Định lý Góc ngoài tam giác (Exterior Angle Theorem):</b> Góc ngoài bằng <b>tổng 2 góc trong không kề với nó</b> (<code>d = a + b</code>).
      <br>• <b>Tổng các góc trong đa giác n cạnh:</b> <code>S = (n − 2) × 180°</code> (tứ giác = 360°, ngũ giác = 540°, lục giác = 720°).
    </div>
  </div>

  <div id="sec-similar" class="sat-card lecture-interactive-card" data-lecture-section="similar">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>2. Tam giác Đồng dạng (AA Similarity) &amp; Quy tắc Tỉ số Diện tích <code>k²</code></h2>
    <p>Chỉ cần hai tam giác có <b>2 cặp góc bằng nhau (AA)</b> — đặc biệt phổ biến là mô hình 1 đoạn thẳng song song cắt ngang tam giác lớn hoặc mô hình "đồng hồ cát" (hourglass) — ta lập tức có hai tam giác đồng dạng!</p>
    <div class="sat-gold-box">
      <b>⭐ 3 Luật Đồng dạng bắt buộc thuộc cho Hard M2:</b>
      <br>1. <b>Thứ tự đỉnh tương ứng:</b> Khi đề viết <code>△ABC ~ △DEF</code>, cạnh <code>AB</code> tương ứng <code>DE</code>, <code>BC</code> tương ứng <code>EF</code>, <code>∠A = ∠D</code> — kiểm tra kỹ thứ tự chữ cái!
      <br>2. <b>Tỉ lệ Chu vi &amp; Đường cao = k</b> (tỉ lệ độ dài cạnh).
      <br>3. <b>Tỉ lệ Diện tích = k²</b> (bình phương tỉ số cạnh!). Nếu cạnh tăng gấp 3 lần → diện tích tăng <b>9 lần</b>!
    </div>
    <div class="sat-trap-box">
      <b>🚨 Bẫy Tam giác lồng nhau (Nested Triangle Trap):</b> Khi đoạn <code>DE ∥ BC</code> chia cạnh <code>AB</code> thành <code>AD = 4</code> và <code>DB = 6</code>, tỉ số đồng dạng giữa <code>△ADE</code> và <code>△ABC</code> là <code>AD / AB = 4 / (4 + 6) = 4 / 10 = 2 / 5</code> (TUYỆT ĐỐI KHÔNG lấy <code>4 / 6</code>!).
    </div>
  </div>

  <div id="sec-special" class="sat-card lecture-interactive-card" data-lecture-section="special">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>3. Bộ ba Pythagoras &amp; Tam giác vuông đặc biệt 30°–60°–90° / 45°–45°–90°</h2>
    <div style="display:flex;justify-content:center;margin:10px 0;">{svg_tri_ref}</div>
    <table class="sat-table">
      <thead><tr><th>Bộ tỉ lệ đặc biệt</th><th>Cạnh (hoặc Góc)</th><th>Ứng dụng 5 giây trên SAT</th></tr></thead>
      <tbody>
        <tr><td><b>Pythagorean Triples</b></td><td><code>3–4–5</code>, <code>5–12–13</code>, <code>8–15–17</code>, <code>7–24–25</code></td><td>Và các bội số: <code>6–8–10</code>, <code>9–12–15</code>, <code>10–24–26</code> — nhìn ra ngay không cần bấm căn!</td></tr>
        <tr><td><b>30°–60°–90°</b></td><td><code>x : x√3 : 2x</code></td><td><b>Tam giác đều cạnh s:</b> Đường cao <code>h = (s√3)/2</code>, Diện tích <code>A = (s²√3)/4</code>!</td></tr>
        <tr><td><b>45°–45°–90°</b></td><td><code>s : s : s√2</code></td><td><b>Hình vuông cạnh s:</b> Đường chéo <code>d = s√2</code> → biết đường chéo <code>d</code>, cạnh là <code>d / √2</code>!</td></tr>
      </tbody>
    </table>
  </div>
'''
    m4_1_qc = make_quick_check_html(
        'qc_m4_1',
        'Hai tam giác đồng dạng △ABC ~ △DEF có tỉ số cạnh tương ứng AB / DE = 3 / 5. Biết diện tích của △ABC bằng 36 cm². Diện tích của △DEF bằng bao nhiêu cm²?',
        'Triangles <b>△ABC</b> and <b>△DEF</b> are similar, with corresponding sides <b>AB / DE = 3 / 5</b>. If the area of △ABC is <b>36 cm²</b>, what is the area of △DEF?',
        ['60', '75', '100', '150'],
        2,
        'Tỉ số cạnh là k = 5 / 3 (từ ABC sang DEF) → Tỉ số DIỆN TÍCH phải là k² = (5/3)² = 25 / 9! Vậy Area(△DEF) = 36 × (25 / 9) = 4 × 25 = 100 cm². Bẫy 60 đến từ việc quên bình phương tỉ số (chỉ nhân 5/3)!'
    )
    m4_1_html = build_sat_lecture_html(
        'DIGITAL SAT MATH 1500+ • MODULE 4 • GEOMETRY & TRIGONOMETRY',
        '4.1 Triangles, Parallel Lines, Similarity & Special Right Triangles',
        'Giải nhanh hình học phẳng chuẩn 800: quy tắc 2 loại góc song song, bẫy tam giác lồng nhau, tỉ lệ diện tích k² và tam giác vuông đặc biệt 30-60-90 / 45-45-90.',
        [
            'Xử lý gọn các bài toán góc song song, góc ngoài tam giác và tổng góc đa giác trong 15 giây.',
            'Tránh 100% bẫy cạnh toàn phần (AD / AB) trong tam giác lồng nhau và luôn bình phương k² cho tỉ số diện tích.',
            'Thuộc lòng 4 bộ ba Pythagoras và công thức đường cao/diện tích tam giác đều từ tỉ lệ 30°–60°–90°.',
        ],
        m4_1_cards,
        m4_1_qc
    )
    m4_1_segs = [
        {
            'id': 'intro',
            'title': 'Tổng quan Hình học phẳng & Tam giác',
            'selector': '#sec-header',
            'en': 'Geometry and Trigonometry make up fifteen percent of Digital SAT Math, and these questions frequently show up as high-value problems near the end of Hard Module Two. Let us lock down angles, similar triangles, and special right triangles.',
            'vi': 'Hình học và Lượng giác chiếm 15 phần trăm bài thi Toán SAT và thường xuất hiện ở nhóm câu điểm cao cuối Module 2 Hard. Bài học này sẽ khóa chặt ba vũ khí cốt lõi: góc song song, tam giác đồng dạng và tam giác vuông đặc biệt.'
        },
        {
            'id': 'angles',
            'title': 'Góc song song, Góc ngoài & Đa giác',
            'selector': '#sec-angles',
            'en': 'When a transversal cuts two parallel lines, you only have two angle sizes: all acute angles are equal, all obtuse angles are equal, and any acute plus obtuse angle equals one hundred eighty degrees. Also remember the Exterior Angle Theorem: an exterior angle of a triangle equals the sum of the two remote interior angles.',
            'vi': 'Khi một đường thẳng cắt hai đường song song, thực chất chỉ có đúng hai cỡ góc: tất cả góc nhọn bằng nhau, tất cả góc tù bằng nhau, và một góc nhọn cộng một góc tù bằng 180 độ. Đừng quên định lý góc ngoài tam giác bằng tổng hai góc trong không kề với nó.'
        },
        {
            'id': 'similar',
            'title': 'Tam giác đồng dạng & Bẫy tỉ số diện tích k²',
            'selector': '#sec-similar',
            'en': 'In similar triangles, two big traps catch students. First, in nested triangles where a parallel segment cuts across a larger triangle, always compare the small side to the ENTIRE big side, never to the bottom segment alone. Second, if the linear scale factor is k, the ratio of their areas is k squared.',
            'vi': 'Trong bài tam giác đồng dạng có hai cái bẫy kinh điển. Thứ nhất, với hai tam giác lồng nhau có đoạn song song, luôn so cạnh nhỏ với toàn bộ cạnh lớn chứ không so với đoạn dư phía dưới. Thứ hai, nếu tỉ số cạnh là k thì tỉ số diện tích bắt buộc phải là k bình phương.'
        },
        {
            'id': 'special',
            'title': 'Pythagoras & Tam giác đặc biệt 30-60-90 / 45-45-90',
            'selector': '#sec-special',
            'en': 'Memorize the four classic Pythagorean triples: 3-4-5, 5-12-13, 8-15-17, and 7-24-25. For 30-60-90 triangles, the sides follow the ratio x to x root three to two x, which also gives the height of an equilateral triangle as s root three over two. For 45-45-90 triangles, the diagonal of a square of side s is always s root two.',
            'vi': 'Hãy thuộc lòng bốn bộ ba Pythagoras kinh điển: 3-4-5, 5-12-13, 8-15-17 và 7-24-25. Trong tam giác 30-60-90, tỉ lệ ba cạnh là x, x căn 3 và 2x, từ đó suy ra ngay đường cao tam giác đều cạnh s bằng s căn 3 chia 2. Còn trong tam giác 45-45-90, đường chéo hình vuông cạnh s luôn bằng s căn 2.'
        }
    ]
    lectures.append({
        'code': 'm4_1',
        'module_key': 'math_m4',
        'order_index': 1,
        'title': '4.1 Triangles, Parallel Lines, Similarity & Special Right Triangles',
        'drill_key': 'drill_m4_1',
        'html': m4_1_html,
        'segments': m4_1_segs,
        'major_sections': [
            {'title': 'Góc song song & Đa giác', 'startSegmentId': 'angles'},
            {'title': 'Tam giác đồng dạng & k²', 'startSegmentId': 'similar'},
            {'title': '30-60-90 & 45-45-90', 'startSegmentId': 'special'},
        ],
    })

    # =========================================================================
    # LECTURE M4.2: Circles — Completing the Square, Arcs, Sectors & Radians
    # =========================================================================
    svg_circ_ref = svg_circle_sector('r', 'θ', note='Arc s = rθ  |  Sector A = ½r²θ (θ in radians)')

    m4_2_cards = f'''
  <div id="sec-circle-eq" class="sat-card lecture-interactive-card" data-lecture-section="circle_eq">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>1. Phương trình Đường tròn &amp; Hoàn thành Bình phương (Completing the Square)</h2>
    <p>Phương trình chuẩn của đường tròn tâm <code>(h, k)</code> và bán kính <code>r</code> là: <b><code>(x − h)² + (y − k)² = r²</code></b>.</p>
    <div class="sat-gold-box">
      <b>⭐ Quy trình 3 bước Hoàn thành Bình phương cho dạng khai triển <code>x² + y² + Dx + Ey + F = 0</code>:</b>
      <br>1. <b>Nếu có hệ số <code>a</code> trước <code>x², y²</code></b> (ví dụ <code>2x² + 2y² − 12x + 8y = 6</code>) → <b>CHIA toàn bộ phương trình cho <code>a</code> trước!</b> (<code>x² + y² − 6x + 4y = 3</code>).
      <br>2. <b>Lấy nửa hệ số x và y rồi bình phương cộng vào cả 2 vế:</b>
      <br>&nbsp;&nbsp;&nbsp;<code>(x − 3)² + (y + 2)² = 3 + (−3)² + 2² = 3 + 9 + 4 = 16</code>.
      <br>3. Đọc kết quả: Tâm <b><code>(3, −2)</code></b> (nhớ ĐỔI DẤU!), bán kính <b><code>r = √16 = 4</code></b> (KHÔNG phải 16!), đường kính <code>d = 8</code>!
    </div>
    <div style="{DESMOS_BOX_STYLE}">
      <b>⚡ Desmos Hack 5 giây cho Đường tròn:</b> Gõ <b>nguyên văn</b> <code>2x² + 2y² − 12x + 8y = 6</code> vào Desmos! Desmos vẽ ngay hình tròn → bấm vào đỉnh cao nhất và thấp nhất để lấy ngay đường kính <code>d = y_max − y_min</code>, bán kính <code>r = d / 2</code> và tâm chính giữa!
    </div>
  </div>

  <div id="sec-radians" class="sat-card lecture-interactive-card" data-lecture-section="radians">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>2. Radian, Độ dài Cung (Arc Length) &amp; Diện tích Hình quạt (Sector Area)</h2>
    <div style="display:flex;justify-content:center;margin:10px 0;">{svg_circ_ref}</div>
    <div class="sat-rule-box">
      <b>📌 Đổi Độ ↔ Radian (nhớ duy nhất <code>π rad = 180°</code>):</b>
      <br>• Độ → Radian: nhân với <code>π / 180°</code> (VD: <code>120° = 2π/3</code>, <code>45° = π/4</code>, <code>60° = π/3</code>, <code>30° = π/6</code>).
      <br>• Radian → Độ: thay thẳng chữ <code>π</code> bằng <code>180°</code> (VD: <code>5π/6 = 5(180°)/6 = 150°</code>!).
      <br><b>📌 Công thức Tỉ lệ Vàng (Dùng được cho CẢ Độ lẫn Radian):</b>
      <br><b><code>(Góc ở tâm) / (360° hoặc 2π) = (Độ dài cung s) / (2πr) = (Diện tích quạt A) / (πr²)</code></b>
      <br>• Riêng khi góc <code>θ</code> tính bằng <b>Radian</b>: <code>s = rθ</code> và <code>A = ½ r²θ</code>!
    </div>
  </div>

  <div id="sec-theorems" class="sat-card lecture-interactive-card" data-lecture-section="theorems">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>3. Góc nội tiếp, Tiếp tuyến &amp; Vị trí điểm (Hard M2)</h2>
    <div class="sat-rule-box">
      <b>1. Góc nội tiếp (Inscribed Angle):</b> Bằng <b>một nửa</b> góc ở tâm cùng chắn một cung (<code>∠inscribed = ½ ∠central</code>). Đặc biệt, góc nội tiếp chắn <b>đường kính</b> luôn bằng <b>90°</b>!
      <br><b>2. Tiếp tuyến (Tangent Line):</b> Luôn <b>vuông góc (90°)</b> với bán kính tại tiếp điểm → tạo ngay tam giác vuông để dùng Pythagoras!
      <br><b>3. Điểm nằm TRONG / TRÊN / NGOÀI đường tròn <code>(x−h)² + (y−k)² = r²</code>:</b>
      <br>• Thay tọa độ điểm vào vế trái: <b><code>&lt; r²</code></b> (bên trong), <b><code>= r²</code></b> (trên đường tròn), <b><code>&gt; r²</code></b> (bên ngoài).
    </div>
  </div>
'''
    m4_2_qc = make_quick_check_html(
        'qc_m4_2',
        'Trong mặt phẳng Oxy, phương trình đường tròn là x² + y² − 10x + 6y − 2 = 0. Bán kính r của đường tròn này bằng bao nhiêu?',
        'In the xy-plane, the equation of a circle is <b>x² + y² − 10x + 6y − 2 = 0</b>. What is the <b>radius</b> of the circle?',
        ['4', '6', '18', '36'],
        1,
        'Chuyển −2 sang vế phải: (x² − 10x) + (y² + 6y) = 2. Cộng (−5)² = 25 và (3)² = 9 vào cả hai vế: (x − 5)² + (y + 3)² = 2 + 25 + 9 = 36. Do r² = 36 nên bán kính r = √36 = 6! Cẩn thận bẫy 36 là r² chứ không phải r!'
    )
    m4_2_html = build_sat_lecture_html(
        'DIGITAL SAT MATH 1500+ • MODULE 4 • GEOMETRY & TRIGONOMETRY',
        '4.2 Circle Equations, Completing the Square, Arcs & Radians',
        'Chinh phục tuyệt đối chuyên đề Đường tròn: kỹ thuật hoàn thành bình phương không sai dấu, mẹo Desmos đo bán kính, công thức cung/quạt Radian và tiếp tuyến.',
        [
            'Hoàn thành bình phương chính xác (kể cả khi hệ số x², y² khác 1) và không bao giờ nhầm r² với r.',
            'Chuyển đổi Độ ↔ Radian tức thì và áp dụng tỉ lệ vàng cho độ dài cung s = rθ và diện tích quạt A = ½r²θ.',
            'Sử dụng định lý góc nội tiếp (½ góc ở tâm), tiếp tuyến vuông góc bán kính và kiểm tra điểm trong/ngoài đường tròn.',
        ],
        m4_2_cards,
        m4_2_qc
    )
    m4_2_segs = [
        {
            'id': 'intro',
            'title': 'Tổng quan Đường tròn trên Digital SAT',
            'selector': '#sec-header',
            'en': 'Circle problems are guaranteed on every single Digital SAT Math test—from completing the square in the coordinate plane to radian arc lengths and tangent lines. Let us make circles automatic.',
            'vi': 'Bài toán đường tròn chắc chắn xuất hiện trong mọi đề thi SAT Math, từ hoàn thành bình phương trong mặt phẳng tọa độ cho đến độ dài cung theo radian và tiếp tuyến. Hãy biến chuyên đề này thành điểm chắc chắn trong túi bạn.'
        },
        {
            'id': 'circle_eq',
            'title': 'Hoàn thành bình phương & Desmos Check',
            'selector': '#sec-circle-eq',
            'en': 'In standard circle form, x minus h squared plus y minus k squared equals r squared. To convert expanded form, first divide out any leading coefficient other than one. Then take half of the x coefficient and half of the y coefficient, square both, and add them to the right side. Finally, always take the square root of the right side to get the radius, never stop at r squared. You can also type the raw equation directly into Desmos to read the exact diameter visually.',
            'vi': 'Phương trình chuẩn của đường tròn là x trừ h tất cả bình cộng y trừ k tất cả bình bằng r bình. Khi gặp dạng khai triển, nếu trước x bình và y bình có hệ số khác 1 thì phải chia trước. Sau đó lấy một nửa hệ số x và y, bình phương rồi cộng cả hai vào vế phải. Nhớ lấy căn bậc hai vế phải để ra bán kính r, tuyệt đối đừng chọn nhầm r bình. Mẹo nhanh nhất là gõ thẳng phương trình vào Desmos để đo trực tiếp.'
        },
        {
            'id': 'radians',
            'title': 'Radian, Độ dài cung & Diện tích quạt',
            'selector': '#sec-radians',
            'en': 'To convert radians to degrees instantly, simply replace pi with one hundred eighty degrees. For arc length and sector area, remember the golden proportion: the central angle over the full circle equals arc length over circumference, which also equals sector area over full circle area. When theta is in radians, arc length simplifies cleanly to r times theta.',
            'vi': 'Để đổi từ radian sang độ trong nháy mắt, chỉ cần thay chữ pi bằng 180 độ. Với độ dài cung và diện tích quạt, hãy nhớ tỉ lệ vàng: góc ở tâm chia cả vòng tròn bằng độ dài cung chia chu vi, và bằng diện tích quạt chia diện tích cả hình tròn. Khi góc đo bằng radian, độ dài cung rút gọn siêu đẹp thành r nhân theta.'
        },
        {
            'id': 'theorems',
            'title': 'Góc nội tiếp, Tiếp tuyến & Vị trí điểm',
            'selector': '#sec-theorems',
            'en': 'Keep three circle theorems ready for Hard Module Two: an inscribed angle is always half the central angle intercepting the same arc; a tangent line is always perpendicular to the radius at the point of tangency; and plugging a point into the circle equation tells you whether it lies inside, on, or outside the circle.',
            'vi': 'Ghi nhớ ba định lý đường tròn cho Module 2 Hard: góc nội tiếp luôn bằng một nửa góc ở tâm cùng chắn một cung; tiếp tuyến luôn vuông góc với bán kính tại tiếp điểm; và thay tọa độ điểm vào phương trình đường tròn cho biết ngay điểm đó nằm trong, trên hay ngoài đường tròn.'
        }
    ]
    lectures.append({
        'code': 'm4_2',
        'module_key': 'math_m4',
        'order_index': 2,
        'title': '4.2 Circle Equations, Completing the Square, Arcs & Radians',
        'drill_key': 'drill_m4_2',
        'html': m4_2_html,
        'segments': m4_2_segs,
        'major_sections': [
            {'title': 'Hoàn thành bình phương', 'startSegmentId': 'circle_eq'},
            {'title': 'Radian, Cung & Quạt', 'startSegmentId': 'radians'},
            {'title': 'Góc nội tiếp & Tiếp tuyến', 'startSegmentId': 'theorems'},
        ],
    })

    # =========================================================================
    # LECTURE M4.3: Trigonometry & 3D Solid Scaling (k, k², k³)
    # =========================================================================
    svg_cyl_ref = svg_cylinder('r', 'h', note='V = πr²h  |  If r & h scale by k → V scales by k³')

    m4_3_cards = f'''
  <div id="sec-sohcahtoa" class="sat-card lecture-interactive-card" data-lecture-section="sohcahtoa">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>1. Lượng giác Tam giác vuông (SOH-CAH-TOA) &amp; Tính bất biến Đồng dạng</h2>
    <div class="sat-gold-box">
      <b>⭐ SOH — CAH — TOA &amp; Công thức phụ nhau (Complementary Identity):</b>
      <br>• <code>sin(θ) = Opposite / Hypotenuse</code> &nbsp;|&nbsp; <code>cos(θ) = Adjacent / Hypotenuse</code> &nbsp;|&nbsp; <code>tan(θ) = Opposite / Adjacent = sin(θ) / cos(θ)</code>.
      <br>• <b>Định lý Hai góc phụ nhau (Xuất hiện gần như MỌI đề SAT!):</b>
      <br>&nbsp;&nbsp;Nếu <code>A + B = 90°</code> (hoặc <code>π/2 rad</code>) → <b><code>sin(A) = cos(B)</code></b> và <b><code>cos(A) = sin(B)</code></b>!
      <br>&nbsp;&nbsp;Ngược lại, nếu đề cho <code>sin(2x + 10°) = cos(3x − 20°)</code> với hai góc nhọn → lập tức cho tổng bằng 90°: <code>(2x + 10) + (3x − 20) = 90</code> → <code>5x = 100</code> → <code>x = 20</code>!
    </div>
    <div class="sat-rule-box">
      <b>📌 Tính bất biến tỉ số lượng giác ở Tam giác đồng dạng (Hard M2 Favorite):</b>
      <br>Nếu <code>△ABC ~ △DEF</code> (vuông tại B và E), dù cạnh tam giác <code>DEF</code> lớn gấp 5 lần cạnh tam giác <code>ABC</code>, thì <b><code>sin(D) = sin(A)</code>, <code>cos(D) = cos(A)</code>, <code>tan(D) = tan(A)</code> — TUYỆT ĐỐI KHÔNG NHÂN 5!</b> Tỉ số lượng giác chỉ phụ thuộc vào GÓC!
    </div>
  </div>

  <div id="sec-unitcircle" class="sat-card lecture-interactive-card" data-lecture-section="unitcircle">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>2. Đường tròn Lượng giác &amp; Góc đặc biệt theo Radian</h2>
    <table class="sat-table">
      <thead><tr><th>Góc (Độ / Radian)</th><th><code>sin θ</code></th><th><code>cos θ</code></th><th><code>tan θ</code></th></tr></thead>
      <tbody>
        <tr><td><b>30° (<code>π/6</code>)</b></td><td><code>1/2</code></td><td><code>√3 / 2</code></td><td><code>1 / √3</code></td></tr>
        <tr><td><b>45° (<code>π/4</code>)</b></td><td><code>√2 / 2</code></td><td><code>√2 / 2</code></td><td><code>1</code></td></tr>
        <tr><td><b>60° (<code>π/3</code>)</b></td><td><code>√3 / 2</code></td><td><code>1/2</code></td><td><code>√3</code></td></tr>
      </tbody>
    </table>
    <div style="{DESMOS_BOX_STYLE}">
      <b>⚡ Desmos Radian/Degree Mode:</b> Bấm biểu tượng cờ-lê (Settings 🔧) góc phải Desmos để chuyển chuẩn giữa <b>Radians</b> và <b>Degrees</b>! Kiểm tra ngay giá trị <code>cos(5π/6)</code> hay <code>sin(2π/3)</code> mà không bao giờ sợ nhầm dấu dương/âm ở góc phần tư II, III, IV!
    </div>
  </div>

  <div id="sec-solids" class="sat-card lecture-interactive-card" data-lecture-section="solids">
    <div class="sat-listen-pill">🎧 Nghe phần này</div>
    <h2>3. Hình học Không gian 3D &amp; Luật Tỉ lệ Tương đồng <code>k : k² : k³</code> (Hard M2 Boss)</h2>
    <div style="display:flex;justify-content:center;margin:10px 0;">{svg_cyl_ref}</div>
    <p>Tất cả công thức Thể tích (Lăng trụ chữ nhật, Trụ, Cầu, Nón, Chóp) đều nằm sẵn trong nút <b>Reference</b> trên Bluebook! Điều thực sự phân loại 780–800 là <b>Tỉ lệ co giãn 3D (Scaling Laws)</b> và <b>Diện tích toàn phần (Surface Area)</b>:</p>
    <div class="sat-gold-box">
      <b>⭐ Luật Co giãn 3D cho 2 hình khối đồng dạng (Similar Solids) với tỉ lệ cạnh <code>k</code>:</b>
      <br>• <b>Độ dài (bán kính, chiều cao, cạnh, chu vi đáy):</b> nhân <b><code>k</code></b>
      <br>• <b>Diện tích (Surface Area, diện tích mặt đáy):</b> nhân <b><code>k²</code></b>
      <br>• <b>Thể tích (Volume) &amp; Khối lượng (cùng chất liệu):</b> nhân <b><code>k³</code></b>!
      <br><b>Ví dụ:</b> Nếu Hình lập phương B có thể tích gấp <b>64 lần</b> Hình lập phương A → tỉ lệ cạnh <code>k = ∛64 = 4</code> → Diện tích toàn phần của B gấp <b><code>k² = 4² = 16 lần</code></b> của A!
    </div>
    <div class="sat-trap-box">
      <b>🚨 Bẫy "Chỉ đổi 1 kích thước":</b> Nếu hình trụ <b>tăng bán kính r gấp 3 lần</b> nhưng <b>giảm chiều cao h đi một nửa</b>: <code>V_mới = π(3r)²(h/2) = (9/2)πr²h = 4.5 V_cũ</code>! Luôn thay trực tiếp hệ số vào công thức gốc <code>V = πr²h</code>.
    </div>
  </div>
'''
    m4_3_qc = make_quick_check_html(
        'qc_m4_3',
        'Hai hình lăng trụ vuông tương đồng A và B có diện tích toàn phần (surface area) lần lượt là 45 cm² và 180 cm². Nếu thể tích của hình A là 20 cm³, thể tích của hình B bằng bao nhiêu cm³?',
        'Two similar rectangular prisms A and B have surface areas of <b>45 cm²</b> and <b>180 cm²</b>, respectively. If the volume of prism A is <b>20 cm³</b>, what is the volume of prism B?',
        ['80', '160', '320', '640'],
        1,
        'Tỉ số diện tích là k² = 180 / 45 = 4 → suy ra tỉ số cạnh tuyến tính là k = √4 = 2! Do đó tỉ số THỂ TÍCH là k³ = 2³ = 8 → Volume(B) = 20 × 8 = 160 cm³! Bẫy 80 là nhân nhầm với k² = 4 thay vì k³ = 8.'
    )
    m4_3_html = build_sat_lecture_html(
        'DIGITAL SAT MATH 1500+ • MODULE 4 • GEOMETRY & TRIGONOMETRY',
        '4.3 Trigonometry (SOH-CAH-TOA, Cofunctions) & 3D Solid Scaling',
        'Khóa chặt 100% điểm Lượng giác & Hình học Không gian 3D: định lý sin A = cos B, tính bất biến tỉ số lượng giác và luật tỉ lệ 3D k : k² : k³.',
        [
            'Giải ngay phương trình lượng giác phụ nhau sin(A) = cos(B) bằng tổng A + B = 90° trong 5 giây.',
            'Nhận diện tính bất biến của sin/cos/tan trong các tam giác vuông đồng dạng (không bị lừa nhân theo hệ số cạnh).',
            'Vận dụng thuần thục luật tỉ lệ 3D (k, k², k³) chuyển đổi giữa Cạnh, Diện tích toàn phần và Thể tích các khối đồng dạng.',
        ],
        m4_3_cards,
        m4_3_qc
    )
    m4_3_segs = [
        {
            'id': 'intro',
            'title': 'Tổng quan Lượng giác & Hình khối 3D 800',
            'selector': '#sec-header',
            'en': 'Welcome to the final Math theory lesson! Trigonometry and 3D solid scaling appear right at the top of Hard Module Two, yet once you recognize the complementary angle identity and the k, k-squared, k-cubed scaling ladder, these become some of the cleanest questions on the test.',
            'vi': 'Chào mừng bạn đến với bài giảng lý thuyết cuối cùng của khóa SAT Math 1500 Plus! Lượng giác và tỉ lệ hình khối 3D thường là những câu chốt ở cuối Module 2 Hard, nhưng một khi nắm chắc định lý góc phụ nhau và bậc thang tỉ lệ k, k bình, k lập phương, đây lại là những câu cực kỳ gọn và đẹp.'
        },
        {
            'id': 'sohcahtoa',
            'title': 'SOH-CAH-TOA, Góc phụ nhau & Tính bất biến',
            'selector': '#sec-sohcahtoa',
            'en': 'Beyond basic SOH-CAH-TOA, remember two high-yield SAT rules. First, for complementary angles that add up to ninety degrees, the sine of one angle always equals the cosine of the other. Second, trigonometric ratios depend solely on angle size—if two right triangles are similar, their sines, cosines, and tangents are identical even if one triangle is five times larger.',
            'vi': 'Bên cạnh công thức sin cos tan cơ bản, hãy khắc cốt ghi tâm hai quy tắc vàng. Thứ nhất, với hai góc nhọn phụ nhau có tổng bằng 90 độ thì sin góc này luôn bằng cos góc kia. Thứ hai, tỉ số lượng giác chỉ phụ thuộc vào số đo góc: hai tam giác vuông đồng dạng dù kích thước lớn gấp 5 lần nhau vẫn có giá trị sin, cos và tan hoàn toàn bằng nhau.'
        },
        {
            'id': 'unitcircle',
            'title': 'Góc lượng giác đặc biệt & Cài đặt Desmos',
            'selector': '#sec-unitcircle',
            'en': 'Know the exact sine and cosine values for pi over six, pi over four, and pi over three. And remember to check the wrench icon in Desmos to make sure you are in Radian or Degree mode before evaluating any trig function.',
            'vi': 'Thuộc nằm lòng bảng giá trị lượng giác của các góc 30, 45 và 60 độ dưới dạng radian. Và khi kiểm tra bằng Desmos, luôn bấm vào biểu tượng cài đặt cờ lê góc phải để chọn đúng chế độ Radian hoặc Degree trước khi tính.'
        },
        {
            'id': 'solids',
            'title': 'Luật Tỉ lệ 3D k : k² : k³',
            'selector': '#sec-solids',
            'en': 'All volume formulas are provided in the Bluebook Reference Sheet. What you must master is the 3D scaling ladder: for any two similar solids, if lengths scale by k, surface areas scale by k squared, and volumes scale by k cubed. If you are given a surface area ratio first, take the square root to find k, and then cube k to get the volume ratio.',
            'vi': 'Mọi công thức thể tích hình trụ, nón, cầu, chóp đều có sẵn trong bảng Reference Sheet của Bluebook. Điều bạn cần thuộc nằm lòng là bậc thang tỉ lệ 3D: khi hai khối đồng dạng có tỉ lệ cạnh là k thì tỉ lệ diện tích toàn phần là k bình phương và tỉ lệ thể tích là k lập phương. Nếu đề cho tỉ lệ diện tích trước, hãy lấy căn bậc hai để tìm k, sau đó lập phương lên để ra tỉ lệ thể tích.'
        }
    ]
    lectures.append({
        'code': 'm4_3',
        'module_key': 'math_m4',
        'order_index': 3,
        'title': '4.3 Trigonometry (SOH-CAH-TOA, Cofunctions) & 3D Solid Scaling',
        'drill_key': 'drill_m4_3',
        'html': m4_3_html,
        'segments': m4_3_segs,
        'major_sections': [
            {'title': 'SOH-CAH-TOA & sin A = cos B', 'startSegmentId': 'sohcahtoa'},
            {'title': 'Góc đặc biệt & Radian', 'startSegmentId': 'unitcircle'},
            {'title': 'Luật tỉ lệ 3D k : k² : k³', 'startSegmentId': 'solids'},
        ],
    })

    return lectures
